#!/bin/bash
# B24 taste-designed screens (sequential; 4 workers; reduced Nelder-Mead starts B24_NM=15)
cd /home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B24_taste_enlarged_steps
B24_NM=15 timeout 1500 python3 b24_screen.py taste:A 4 > screen_taste_A.log 2>&1
B24_NM=15 timeout 1500 python3 b24_screen.py taste:B,C 4 > screen_taste_B-C.log 2>&1
