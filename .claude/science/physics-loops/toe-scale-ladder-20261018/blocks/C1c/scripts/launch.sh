#!/bin/bash
# (re)launch the three C1c workers (safe to rerun after a restart; locks prevent double-running a tag)
cd "$(dirname "$0")"
for w in w1 w2 w3; do
  pgrep -f "worker.sh $w" >/dev/null || nohup setsid ./worker.sh $w ${1:-1635} >/dev/null 2>&1 &
  sleep 20
done
