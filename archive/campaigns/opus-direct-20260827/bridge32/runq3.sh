#!/bin/zsh
cd "$(dirname "$0")"
while pgrep -f "t32_dK.py" > /dev/null; do sleep 15; done
python3 t36_joint.py 64 6,8,10,12,16,20,25,32 > t36_L64.log 2>&1
echo ALLDONE >> t36_L64.log
