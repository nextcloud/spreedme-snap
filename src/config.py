#!/usr/bin/python3
"""python3 config hook for Spreed WebRTC"""

import collections
import configparser
import os
import subprocess
import sys
import yaml

SPREED_WEBRTC_DATA_PATH = os.environ['SNAP_DATA']
SPREED_WEBRTC_VERSION = os.environ['SNAP_VERSION']
SPREED_WEBRTC_CONFIG_FILE = os.path.join(SPREED_WEBRTC_DATA_PATH,
                                         'server.conf')
START_CONFIG_FILE = os.path.join(SPREED_WEBRTC_DATA_PATH, 'start.conf')
SPREED_WEBRTC_CONFIG_FILE_IN = os.path.join(os.environ['SNAP'],
                                            'server.conf.in')

DEFAULT_REVERSE_PORT = 8080

OPENSSL = "/usr/bin/openssl"
if not os.path.exists(OPENSSL):
    OPENSSL = os.path.join(os.path.join(os.environ['SNAP'],
                                        'usr', 'bin', 'openssl'))


class SimpleConfig:
    """SimpleConfig is a parser for simple key=value files"""

    def __init__(self):
        # We use a ordered dict similar to configparser.
        self.data = collections.OrderedDict()

    def read(self, fn):
        try:
            with open(fn, 'r') as f:
                for line in f:
                    name, var = line.partition('=')[::2]
                    name = name.strip()
                    if name:
                        self.data[name] = var.strip()
        except EnvironmentError:
            pass

    def write(self, f):
        for k, v in self.data.items():
            if k:
                f.write('%s=%s\n' % (k, v))

    def get(self, key, value=''):
        return self.data.get(key, value)

    def set(self, key, value=''):
        self.data[key] = value


def main():
    """main is the main function"""
    args = sys.argv[1:]
    if args:
        if args[0] == "update":
            return run(None, update=True)

    return hook()


def hook():
    """hook reads the config from sys.stdin and applies it"""
    config_in = yaml.load(sys.stdin)
    run(config_in)


def run(config_in, update=False):
    """run takes the config_in configuration and applies it"""

    spreed_config = start_config = None

    if config_in:
        config_out, spreed_config, start_config = set_config(config_in)

    config_out, spreed_config, start_config = \
        get_config(spreed_config, start_config)
    if not (os.path.exists(SPREED_WEBRTC_CONFIG_FILE) and
            os.path.exists(START_CONFIG_FILE)):
        # Set read configuration, to bring in defaults.
        config_out, spreed_config, start_config = set_config(config_out)
        config_in = config_out

    if config_in or update:
        with open(SPREED_WEBRTC_CONFIG_FILE, 'w') as f:
            spreed_config.write(f, space_around_delimiters=True)
        with open(START_CONFIG_FILE, 'w') as f:
            start_config.write(f)

    yaml.dump(config_out, stream=sys.stdout, default_flow_style=False)
    sys.exit(0)


def exec_cmd_and_get_output(command, **kwargs):
    """exec_cmd executes a given command as subprocess"""
    assert isinstance(command, list), 'exec_cmd command must be a list'
    return subprocess.check_output(command, **kwargs)


def get_random_hex(bytes=32):
    """get_random_hex generates random hex strings with OpenSSL"""
    return exec_cmd_and_get_output([OPENSSL, "rand", "-hex",
                                   "%d" % bytes]).strip().decode("UTF-8")


def load_config():
    """load_config loads the configuration from file and
    return spreed_config and start_config"""
    spreed_config = configparser.ConfigParser()
    if os.path.exists(SPREED_WEBRTC_CONFIG_FILE):
        spreed_config.read(SPREED_WEBRTC_CONFIG_FILE)
    else:
        spreed_config.read(SPREED_WEBRTC_CONFIG_FILE_IN)
        # Add our defaults.
        spreed_config['http']['root'] = 'www'  # Will be replaced on start.
        spreed_config['app']['sessionSecret'] = get_random_hex(64)
        spreed_config['app']['encryptionSecret'] = get_random_hex(32)
        spreed_config['app']['serverToken'] = get_random_hex(16)
    start_config = SimpleConfig()
    if os.path.exists(START_CONFIG_FILE):
        start_config.read(START_CONFIG_FILE)
    else:
        # Add our defaults.
        start_config.set("WEBAPP_PORT", DEFAULT_REVERSE_PORT)
    return spreed_config, start_config


def set_config(config_yaml):
    """set_config sets a configuration and returns config,
    spreed_config and start_config"""

    config = config_yaml['config']['spreed-webrtc']

    app = config.get('app', {})
    http = config.get('http', {})
    ports = config.get('ports', {})

    spreed_config, start_config = load_config()

    # set value
    def sv(section, name, value):
        if not spreed_config.has_section(section):
            spreed_config.add_section(section)
        spreed_config[section][name] = value

    # get value
    def gv(section, name, value=None):
        if spreed_config.has_section(section):
            return spreed_config[section].get(name, value)
        return value

    # from yaml to ini
    def tc(section, name):
        c = config.get(section, {})
        if name in c:
            sv(section, name, c[name])

    tc('app', 'title')
    tc('app', 'globalRoom')
    tc('app', 'defaultRoomEnabled')
    tc('app', 'serverRealm')
    tc('app', 'contentSecurityPolicy')

    ports_internal = ports.get('internal', {})
    ports_external = ports.get('external', {})

    http_reverse = http.get('reverse', gv('http', 'listen') and True)

    if http_reverse:
        port = DEFAULT_REVERSE_PORT
        if 'reverse' in ports_internal:
            port = int(ports_internal['reverse']['port'])
        listen = "127.0.0.1:%s" % port
        sv('http', 'listen', listen)
    else:
        try:
            spreed_config.remove_option('http', 'listen')
        except configparser.NoSectionError:
            pass

    config_out = {
        'config': {
            'spreed-webrtc': config
        }
    }
    return config_out, spreed_config, start_config


def get_config(spreed_config, start_config):
    """get_config returns config with the current configuration,
    spreed_config and start_config"""

    config = {}
    app = config.setdefault('app', {})
    http = config.setdefault('http', {})
    ports = {}

    if not spreed_config or not start_config:
        spreed_config, start_config = load_config()

    # from ini to yaml
    def tc(section, name):
        c = config.setdefault(section, {})
        try:
            c[name] = spreed_config[section][name]
        except KeyError:
            pass

    tc('app', 'title')
    tc('app', 'defaultRoomEnabled')
    tc('app', 'globalRoom')
    tc('app', 'defaultRoomEnabled')
    tc('app', 'serverRealm')
    tc('app', 'contentSecurityPolicy')

    try:
        http_listen = spreed_config['http'].get('listen', None)
    except KeyError:
        http_listen = None
    if http_listen:
        port = http_listen.rsplit(":", 1)[1]
        internal = ports.setdefault('internal', {})
        internal['reverse'] = {
            'port': int(port)
        }
        http['reverse'] = True
    else:
        http['reverse'] = False

    http['ui'] = False

    if ports:
        config['ports'] = ports

    config_out = {
        'config': {
            'spreed-webrtc': config
        }
    }
    return config_out, spreed_config, start_config

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
