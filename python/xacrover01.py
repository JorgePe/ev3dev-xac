#!/usr/bin/env python3

# the script assumes two large motors at ports A and B
# and XAC already paired and associated to event '/dev/input/event2'

from evdev import InputDevice, categorize, ecodes
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveSteering

XAC_DEVICE = '/dev/input/event2'

TIME_TURN = 0.15
TIME_WALK = 0.30
SPEED_PCT = 75
TURN_LEFT = -100
TURN_RIGHT = 100
FORWARD = 0

RELEASE = 0
PRESS = 1
HOLD = 2

# I get 2 event codes for Button A, B, RB
# I will use just the second code, ignoring the first

BUTTON_A_1 = 304 # BTN_SOUTH
BUTTON_B_1 = 305 # BTN_EAST
BUTTON_RB_1 = 311 # BTN_TR

BUTTON_A_2 = 319 # ?
BUTTON_B_2 = 704 # ?
BUTTON_RB_2 = 710 # ?


steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

dev = InputDevice(XAC_DEVICE)
print(dev)

#print('**********************')
#print('Device Capabilities:')
#print(dev.capabilities(verbose=True))
#print('**********************')

print('Ready...')

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
         if event.code == BUTTON_A_1 or event.code == BUTTON_B_1 or event.code == BUTTON_RB_1:
             continue
         elif event.code == BUTTON_A_2:
             print('A ', end='')
             if event.value == PRESS or event.value == HOLD:
                 print('pressed')
                 steering_drive.on_for_seconds(TURN_LEFT,SpeedPercent(SPEED_PCT),TIME_TURN)
                 while dev.read_one() != None:
                     pass
         elif event.code == BUTTON_B_2:
             print('B ', end='')
             if event.value == PRESS or event.value == HOLD:
                 print('pressed')
                 steering_drive.on_for_seconds(TURN_RIGHT,SpeedPercent(SPEED_PCT),TIME_TURN)
                 sleep(TIME_TURN)
                 while dev.read_one() != None:
                     pass
         elif event.code == BUTTON_RB_2:
             print('RB ', end='')
             if event.value == PRESS or event.value == HOLD:
                 print('pressed')
                 steering_drive.on_for_seconds(FORWARD,SpeedPercent(SPEED_PCT),TIME_WALK)
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
