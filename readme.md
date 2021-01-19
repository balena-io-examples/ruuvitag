# ruuvitag
A ruuvitag is a weatherproof, battery powered sensor which reports temperature, humidity, pressure and motion via Bluetooth Low Energy (BLE) beacons. Deploying this repo turns a raspberry pi (3, 4 or 400) or a [balenaFin](https://www.balena.io/fin/) into a data collector for the ruuvitag, and displays the data over time in the [dashboard](https://github.com/balenablocks/dashboard) balenaBlock.

## Deploy
[![](https://balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/balenalabs-incubator/ruuvitag)

Just click the button, create or sign-in to your balenaCloud account, add your device and start charting your ruuvitag data!

We live-hacked this app on an episode of balena IOT Happy Hour - check it out here:

[![IOT Happy Hour Episode 38: balenaBlocks](https://img.youtube.com/vi/Mllay6Z2-qQ/0.jpg)](https://youtu.be/Mllay6Z2-qQ?t=1852)

## Hardware required
* Raspberry Pi or balenaFin (see [supported devices](#supported-devices) )
* A [ruuvitag](https://shop.ruuvi.com/product/ruuvitag-1-pack/)

## Software required
* A free [balenaCloud account](https://dashboard.balena-cloud.com/signup) (first ten devices are free and fully-featured, no credit card needed to start)
* A tool to flash OS images to SD cards, like [balenaEtcher](https://www.balena.io/etcher/)

## Supported devices
This project has been tested to work on the following devices:

| Device Type  | Status |
| ------------- | ------------- |
| Raspberry Pi 4 2Gb | ✔ |
| Raspberry Pi 4 4Gb | ✔ |
| Raspberry Pi 4 8Gb | ✔ |
| Raspberry Pi 4 1Gb | ✔ |
| Raspberry Pi 400 | ✔ |
| Raspberry Pi 3b+ | ✔ |
| Raspberry Pi 3b+ (64-bit OS) | ✔ |
| balena Fin | ✔ |
| Nanopi Neo Air | ✔ |
