#!/bin/zsh
# start phase3 when phase2's last run has finished
cd "$(dirname "$0")"
until [ -f runs/L4_one_W1.log ] && grep -q watchdog runs/L4_one_W1.log; do sleep 15; done
zsh phase3.sh > runs/phase3.out 2>&1
