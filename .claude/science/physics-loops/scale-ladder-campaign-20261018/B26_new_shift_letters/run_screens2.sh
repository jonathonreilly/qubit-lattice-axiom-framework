#!/bin/bash
# B26 screens, second batch (declared before results): full PHL for the 22 length<=4 one-slot classes; seeded samples elsewhere
cd "$(dirname "$0")"
nice python3 b26_screen.py one:PHL:0-22 3 > screen_one_PHL_0-22.log 2>&1
nice python3 b26_screen.py onesample:PHL:22-74:300 3 > screen_onesample_PHL_22-74_300.log 2>&1
nice python3 b26_screen.py twosample:3-40:300 3 > screen_twosample_3-40_300.log 2>&1
