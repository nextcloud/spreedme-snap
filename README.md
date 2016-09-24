# Spreed WebRTC snap

## Description

Chat and make audio/video calls using [Spreed WebRTC](https://github.com/strukturag/spreed-webrtc/) on Ubuntu Snappy.

A good hardware companion for this Snap is the [Nextcloud Box](https://nextcloud.com/box) which comes with a 1TB hard drive and Nextcloud, a next-generation Files, Sync and Share solution.

If you are a user, just wanting a secure and private alternative for online communication make sure to check out the [Spreedbox](http://spreedbox.com/), providing a ready to use hardware with Spreed WebRTC included.

## Authors

* [Simon Eisenmann](https://github.com/longsleep)
* [Olivier Paroz](https://github.com/oparoz)

## Compilation

*Prerequisite: You need to have both snapcraft and snapd installed. See https://snapcraft.io*

Download the source

`$ git clone https://github.com/oparoz/spreed-webrtc-snap`

Compile the snap

```bash
$ cd spreed-webrtc-snap
$ sudo snapcraft
```

Install it locally

`$ sudo snap install spreed-webrtc_0.28.1-1_amd64.snap --force-dangerous`

*Note: Replace the filename with the one which has been generated*

## Installation

This downloads the app from the Ubuntu app store

`$ sudo snap install spreed-webrtc`

## How to use

### Web interface

Go with your browser to the URL of the device on which the snap was installed, but use port 8443.

Per example: `http://nextcloud.local:8443`

----
Spreed-WebRTC (c)2016 struktur AG