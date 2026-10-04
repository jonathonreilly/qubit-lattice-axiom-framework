#!/bin/zsh
# Queue runner: picks the lexically first file in jobs/ (p_* priority before q_*), one job line per file, runs it via
# run.sh (one at a time); SKIPPED (exit 2/3) -> requeue at the front and wait 60 s.  Exits after 15 min idle.
cd ${0:A:h}
idle=0
while (( idle < 30 )); do
  f=$(ls jobs 2>/dev/null | sort | head -1)
  if [[ -z "$f" ]]; then sleep 30; idle=$((idle+1)); continue; fi
  idle=0; line=$(cat jobs/$f)
  ./run.sh ${=line} >> chain.log 2>&1; rc=$?
  if (( rc == 2 || rc == 3 )); then echo "[skipped rc=$rc, retry in 60s] $line" >> chain.log; sleep 60; continue; fi
  rm -f jobs/$f
done
echo "CHAIN2 IDLE EXIT $(date)" >> chain.log
