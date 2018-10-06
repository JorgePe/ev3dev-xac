# ev3dev-xac
Using a Microsoft Xbox Adaptive Controller with MINDSTORMS EV3 running ev3dev

I really liked Microsoft's idea of exposing all gamepad buttons and axles with common 3.5 mm audio jacks. A switch is a very simple device and audio jacks are common everyhere so we can connect almost anything we want to a computer and use it as a gamepad or keyboard without having to create drivers.

Even better: since the XAC is recognized as an HID Gamepad by probably all decent opeating systems, we can use it with EV3 running ev3dev.

Tested with strecth version of ev3dev, September/October 2018 releases (kernel 4.14.71-ev3dev-2.3.0-ev3).

Please note that there seems to be a bug when having 2 large motors connected that sometimes prevent ev3de to properly iniatilize bluetooth, when this happens we need to reboot until we have bluetooth.

The internal bluetooth controller works with the XAC but first we have to disable ertm by editing '/sys/module/bluetooth/parameters/disable_ertm' and replacing 'N' with 'Y' or '1'. Then we can pair and connect the XAC through BrickMan (the LCD tool).

This only last until next reboot but we can make it permanent by creating a service that runs a script on startup. I created a '/etc/systemd/system/xac.service' containg:

```
[Unit]
Description=XAC Disable ERM
After=multi-user.target

[Install]
WantedBy=multi-user.target

[Service]
Type=simple
ExecStart=/home/robot/XAC/disable-erm.sh
```

and '/home/robot/XAC/disable-erm.sh' containing:

```
#!/usr/bin/env bash
echo 1 > /sys/module/bluetooth/parameters/disable_ertm
```

to enable the service:

```
sudo systemctl enable xac.service
sudo systemctl daemon-reload
```

the last command complained about not enough memory so I just rebooted.

The XAC will appear like this in dmesg:

```
[  186.891778] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
[  186.891891] Bluetooth: HIDP socket layer initialized
[  187.248216] hid-generic 0005:045E:0B0C.0001: unknown main item tag 0x0
[  187.281750] input: Xbox Adaptive Controller as /devices/platform/soc@1c00000/serial8250.2/tty/ttyS2/hci0/hci0:1/0005:045E:0B0C.0001/input/input2
[  187.297632] hid-generic 0005:045E:0B0C.0001: input,hidraw0: BLUETOOTH HID v9.03 Gamepad [Xbox Adaptive Controller] on a0:e6:f8:60:16:60
```

In my Ubuntu laptop I would have a '/dev/input/js0' device that I could test with 'jstest' but since ev3dev doesn't have the old 'joydev' module enabled we will have to check for the presence of a new '/dev/input/event#' device

```
ls /dev/input/
by-path  event0  event1  event2
```

In my case '/dev/input/event2' is the XAC and we can use it with python-evdev.

I connected a common guitar pedal switch to the 'RB' input of the XAC and wrote a pyhton script [xacrover01.py](https://github.com/JorgePe/ev3dev-xac/blob/master/python/xacrover01.py) that reacts to the large round buttons ('A' and 'B') and 'RB' ('Right Bumper') events:

Demo video for the script

[![Microsoft Xbox Adaptive Controller and LEGO MINDSTORMS EV3](http://img.youtube.com/vi/e14kfSoBP94/0.jpg)](http://www.youtube.com/watch?v=e14kfSoBP94)





