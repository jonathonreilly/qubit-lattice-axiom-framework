#!/bin/bash
# B26 screens, sequential, 3 workers each
cd "$(dirname "$0")"
nice python3 b26_screen.py one:PC:0-74 3 > screen_one_PC_0-74.log 2>&1
nice python3 b26_screen.py two:0-3 3 > screen_two_0-3.log 2>&1
