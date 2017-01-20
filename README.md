# Spreed.ME snap

## Description

Chat and make audio/video calls straight from Nextcloud using [Spreed WebRTC](https://github.com/strukturag/spreed-webrtc/) on Ubuntu Snappy.

If you are a company wanting a secure and private alternative for online communication make sure to check out the [Spreedbox](http://spreedbox.com/), providing a ready to use hardware with Spreed.ME included.

## Maintainers

* [Simon Eisenmann](https://github.com/longsleep)
* [Olivier Paroz](https://github.com/oparoz)

## Compilation

*Prerequisite: You need to have both snapcraft and snapd installed. See https://snapcraft.io*

Download the source

`$ git clone https://github.com/nextcloud/spreedme-snap`

Compile the snap

```bash
$ cd spreedme-snap
$ sudo snapcraft
```

Install it locally

`$ sudo snap install spreedme_0.29.2snap1-1_amd64.snap --force-dangerous`

*Note: Replace the filename with the one which has been generated*

## Installation

This downloads the app from the Ubuntu app store

`$ sudo snap install spreedme`

## How to use

### 1. Set up your reverse proxy

You need to configure your reverse proxy so that Nextcloud can communicate with the snap

#### Apache

Make sure the following modules are installed

* mod_proxy
* mod_proxy_http
* mod_proxy_wstunnel

Add an entry in your Nextcloud virtualhost which points the /webrtc directory to the Spreed.ME snap.

```
	<Location /webrtc>
		ProxyPass http://127.0.0.1:8080/webrtc
		ProxyPassReverse /webrtc
	</Location>

	<Location /webrtc/ws>
		ProxyPass ws://127.0.0.1:8080/webrtc/ws
	</Location>

	ProxyVia On
	ProxyPreserveHost On
	RequestHeader set X-Forwarded-Proto 'https' env=HTTPS
```

### 2. Install the Spreed.ME app

#### From the app store

1. Go to the app store inside Nextcloud
1. Enable experimental apps support (wheel icon, bottom left)
1. Click on "Tools" in the left sidebar
1. Scroll down until you see the Spreed.ME app

#### From the command line (not recommended)

Go to the Nextcloud sub-folder where you install your apps

**Install via Git**

Clone the Spreed.ME Nextcloud app or download it from https://github.com/strukturag/nextcloud-spreedme/releases
```bash
git clone https://github.com/strukturag/nextcloud-spreedme.git spreedme
```

**Install via wget**

```bash
$ wget https://github.com/strukturag/nextcloud-spreedme/archive/v0.3.6.tar.gz
$ tar zxvf v0.3.6.tar.gz
$ mv nextcloud-spreedme-0.3.6 spreedme
$ sudo -u www-data php /var/www/nextcloud/occ app:enable spreedme
```

*Note: You need to adjust the version number*

### 3. Configure the Spreed.ME app

1. Go to the admin panel, click on Spreed.ME on the left side-bar
1. Click on "Generate Spreed WebRTC config"
1. Copy-paste the random string next to "sharedsecret_secret" for later use
1. Edit the Spreed me configuration file located at:
`/var/snap/spreedme/current/server.conf`
1. In the [users] section, add the shared secret copy-pasted from earlier, like this
`sharedsecret_secret = bb04fb058e2d7fd19c5bdaa129e7883195f73a9c49414a7eXXXXXXXXXXXXXXXX`
1. Restart Spreed.ME. On a system using systemd, this can be done like this:
`$ systemctl restart snap.spreedme.spreed-webrtc.service`

### 4. Start spreeding!

1. Open the Spreed.ME app in the apps menu
1. Authorise your browser to send your notifications and to use your microphone and camera
1. Ask other users to come and have a chat

#### Additional features

* You can create rooms and share the link to other Nextcloud users on the same instance
* You can define the video quality in the settings panel, after clicking on the wheels icon, top right

### Nextloucd VM
This snap is included in the [Nextcloud VM](https://github.com/nextcloud/vm) and installed when you boot for the first time.

----
Spreed WebRTC & Spreed.ME (c)2016 struktur AG
