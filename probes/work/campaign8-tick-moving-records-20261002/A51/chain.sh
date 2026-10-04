#!/bin/zsh
# Sequential job chain through run.sh; retries SKIPPED jobs (exit 2/3) after 60 s, up to 20 times.  Usage: chain.sh jobsfile
cd ${0:A:h}
while read -r line; do
  [[ -z "$line" || "$line" == \#* ]] && continue
  for try in {1..20}; do
    ./run.sh ${=line} >> chain.log 2>&1; rc=$?
    if (( rc == 2 || rc == 3 )); then echo "[retry $try in 60s] $line" >> chain.log; sleep 60; else break; fi
  done
done < $1
echo "CHAIN DONE $1 $(date)" >> chain.log
