#!/bin/bash
cd "$(dirname "$0")/.."
python3 scripts/step2_validate_L2.py > logs/step2_validate_L2.log 2>&1
python3 scripts/jobqueue.py scripts/jobs_B.txt > logs/queue_B.log 2>&1
