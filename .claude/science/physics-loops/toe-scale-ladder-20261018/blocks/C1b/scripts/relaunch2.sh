#!/bin/bash
cd "$(dirname "$0")"
while pgrep -f "run_pt.py L6_" > /dev/null; do sleep 10; done
nohup ./queue.sh jobs_A2.txt A2 > /dev/null 2>&1 &
nohup ./queue.sh jobs_B2.txt B2 > /dev/null 2>&1 &
