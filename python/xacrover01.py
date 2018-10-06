#!/usr/bin/env python3

from evdev import InputDevice, categorize, ecodes
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveSteering
from time import sleep

TIME_TURN = 0.1
TIME_WALK = 0.2
SPEED_PCT = 75
TURN_LEFT = -100
TURN_RIGHT = 100
FORWARD = 0

RELEASE = 0
PRESS = 1
HOLD = 2

steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

dev = InputDevice('/dev/input/event2')
print(dev)

#print('**********************')
#print('Device Capabilities:')
#print(dev.capabilities(verbose=True))
#print('**********************')

print('Ready...')

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
         if event.code == 304 or event.code == 305 or event.code == 311:
             # not very good here, using just the last code of a dual code event
             # (304 + 319) (305+704) (311+710)
             continue
         elif event.code == 319:
             print('A ', end='')
             if event.value == PRESS or event.value == HOLD:
                 print('pressed')
                 steering_drive.on_for_seconds(TURN_LEFT,SpeedPercent(SPEED_PCT),TIME_TURN)
                 sleep(TIME_TURN)
                 while dev.read_one() != None:
                     pass
         elif event.code == 704:
             print('B ', end='')
             if event.value == PRESS or event.value == HOLD:
                 print('pressed')
                 steering_drive.on_for_seconds(TURN_RIGHT,SpeedPercent(SPEED_PCT),TIME_TURN)
                 sleep(TIME_TURN)
                 while dev.read_one() != None:
                     pass
         elif event.code == 710:
             print('RB ', end='')
             if event.value == PRESS or event.value == HOLD:
                 print('pressed')
                 steering_drive.on_for_seconds(FORWARD,SpeedPercent(SPEED_PCT),TIME_WALK)
                 sleep(TIME_WALK)
                 while dev.read_one() != None:
                     pass
         else:
             print('Code: ', event.code, end='')

    elif event.type == ecodes.EV_ABS:
        # print('type: EV_ABS', repr(event))
        pass
    elif event.type == ecodes.EV_SYN:
        # print('type: EV_SYN')
        pass
    elif event.type == ecodes.EV_MSC:
        #print('type: EV_MSC')
        pass
    elif event.type == ecodes.EV_REL:
        #print('type: EV_REL', repr(event))
        pass
