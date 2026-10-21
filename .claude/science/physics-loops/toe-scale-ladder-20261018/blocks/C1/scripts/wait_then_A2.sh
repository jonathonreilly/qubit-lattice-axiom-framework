#!/bin/bash
cd "$(dirname "$0")/.."
while kill -0 20568 2>/dev/null; do sleep 10; done
python3 scripts/jobqueue.py scripts/jobs_A2.txt > logs/queue_A2.log 2>&1
