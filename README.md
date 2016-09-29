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

### Web interface

1. Log in into Nextcloud
1. Install the Spreed.ME app
1. Click on the Spreed.ME app

----
Spreed WebRTC & Spreed.ME (c)2016 struktur AG