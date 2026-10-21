#!/bin/bash
# usage: wait_pid_then.sh PID jobfile logname
cd "$(dirname "$0")/.."
while kill -0 $1 2>/dev/null; do sleep 10; done
python3 scripts/jobqueue.py $2 > logs/$3 2>&1
