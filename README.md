# Spreed.ME snap

## Description

Chat and make audio/video calls straight from Nextcloud using [Spreed WebRTC](https://github.com/strukturag/spreed-webrtc/) on Ubuntu Snappy.

A good hardware companion for this Snap is the [Nextcloud Box](https://nextcloud.com/box) which comes with a 1TB hard drive and Nextcloud, a next-generation Files, Sync and Share solution.

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

`$ sudo snap install spreedme_0.28.1snap1-1_amd64.snap --force-dangerous`

*Note: Replace the filename with the one which has been generated*

## Installation

This downloads the app from the Ubuntu app store

`$ sudo snap install spreedme`

## How to use

### 1. Enable SSL for Nextcloud

Follow the instructions at: [Enabling HTTPS (SSLS, TLS)](https://github.com/nextcloud/nextcloud-snap/wiki/Enabling-HTTPS-(SSLS,-TLS))

### 2. Install the Spreed.ME app

#### From the app store

1. Go to the app store inside Nextcloud
1. Enable experimental apps support (wheel icon, bottom left)
1. Click on "Tools" in the left sidebar
1. Scroll down until you see the Spreed.ME app

#### From the command line (not recommended)

Install via Git

```bash
cd /var/snap/nextcloud/current/nextcloud/extra-apps/
git clone https://github.com/strukturag/nextcloud-spreedme-git spreedme
```

Or download from https://github.com/strukturag/nextcloud-spreedme/releases
and place it in the following path:
`/var/snap/nextcloud/current/nextcloud/extra-apps/`

### 3. Configure the Spreed.ME app

1. Go to the admin panel, click on Spreed.ME on the left side-bar
1. Click on "Generate Spreed WebRTC config"
1. Copy-paste the random string next to "sharedsecret_secret" for later use
1. Edit the Spreed me configuration file located at:
`/var/snap/spreedme/current/server.conf`
1. In the [users] section, add the shared secret copy-pasted from earlier, like this
`sharedsecret_secret = bb04fb058e2d7fd19c5bdaa129e7883195f73a9c49414a7eXXXXXXXXXXXXXXXX`
1. Restart Spreed.ME:
`$ systemctl restart snap.spreedme.spreed-webrtc.service`

### 4. Start spreeding!

1. Open the Spreed.ME app in the apps menu
1. Authorise your browser to send your notifications and to use your microphone and camera
1. Ask other users to come and have a chat

#### Additional features

* You can create rooms and share the link to other Nextcloud users on the same instance
* You can define the video quality in the settings panel, after clicking on the wheels icon, top right

----
Spreed WebRTC & Spreed.ME (c)2016 struktur AG