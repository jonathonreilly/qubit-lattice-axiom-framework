#!/bin/zsh
# usage: zsh capped.sh OUTFILE python3 script.py args...
# Kills the run if RSS > 400 MB (OBS4 cap) and logs the peak RSS. Also polls child processes.
out=$1; shift
OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 MKL_NUM_THREADS=2 VECLIB_MAXIMUM_THREADS=2 "$@" > $out 2>&1 &
pid=$!
peak=0
while kill -0 $pid 2>/dev/null; do
  rss=$(ps -o rss= -p $pid $(pgrep -P $pid) 2>/dev/null | awk '{s+=$1} END {print s+0}')
  if [[ -n "$rss" ]]; then
    (( rss > peak )) && peak=$rss
    if (( rss > 400000 )); then pkill -9 -P $pid; kill -9 $pid; echo "CAPPED: killed at RSS ${rss} KB" >> $out; fi
  fi
  sleep 0.2
done
echo "watchdog peak RSS ${peak} KB" >> $out
