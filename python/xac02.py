#!/usr/bin/env python3

from evdev import InputDevice, categorize, ecodes

dev = InputDevice('/dev/input/event2')
print(dev)

#print('**********************')
#print('Device Capabilities:')
#print(dev.capabilities(verbose=True))
#print('**********************')


for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
#        print('type: EV_KEY', repr(event))
         if event.code == 304 or event.code == 305 or event.code == 311:
             # (304 + 319) (305+704) (311+710)
             continue
         elif event.code == 319:
             print('A ', end='')
         elif event.code == 704:
             print('B ', end='')
         elif event.code == 710:
             print('RB ', end='')
         else:
             print('Code: ', event.code, end='')

#         print('Event Value: ', event.value, end='')
         if event.value == 1:
             print('pressed')
         elif event.value == 0:
             print('released')
         elif event.value == 2:
             print('holded')
         else:
             print('unknown: ', event.value)

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
