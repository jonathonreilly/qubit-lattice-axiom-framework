#!/bin/zsh
# A53 queue: runs jobs/<name> files (one command line each, args to run.sh) in name order, one at a time, via run.sh.
# SKIPPED (exit 2/3) -> wait 30 s and retry (max 20).  Output appended to chain.log.  Stops when jobs/ is empty.
cd ${0:A:h}
while true; do
  j=$(ls jobs 2>/dev/null | sort | head -1); [[ -z $j ]] && break
  args=$(cat jobs/$j); rm jobs/$j
  for t in {1..20}; do
    ./run.sh ${=args} >> chain.log 2>&1; rc=$?
    (( rc == 2 || rc == 3 )) || break
    echo "  [chain] retry $t for $args" >> chain.log; sleep 30
  done
done
echo "[chain] queue empty $(date)" >> chain.log
