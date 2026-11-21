#!/bin/bash
cd "$(dirname "$0")/.."
while pgrep -f "scripts/ti.py 3 6 6 6" >/dev/null; do sleep 3; done
grep -q "^{" out/ti_3_6.log && echo "END ti_3_6 (finished under old queue)" >> out/queue_main.log
scripts/run_queue.sh out/q_main3.txt >> out/queue_main.log 2>&1
