#!/bin/zsh
# usage: capped.sh OUTFILE python3 script args...   (kills the run if RSS > 300 MB; logs peak RSS)
out=$1; shift
OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 MKL_NUM_THREADS=2 "$@" > $out 2>&1 &
pid=$!
peak=0
while kill -0 $pid 2>/dev/null; do
  rss=$(ps -o rss= -p $pid 2>/dev/null | tr -d ' ')
  if [[ -n "$rss" ]]; then
    (( rss > peak )) && peak=$rss
    if (( rss > 307200 )); then kill -9 $pid; echo "CAPPED: killed at RSS ${rss} KB" >> $out; fi
  fi
  sleep 0.1
done
echo "watchdog peak RSS ${peak} KB" >> $out
