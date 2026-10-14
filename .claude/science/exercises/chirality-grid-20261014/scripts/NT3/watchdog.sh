#!/bin/bash
# usage: watchdog.sh <logprefix> <python args...>   kills the run if RSS > 950 MB
pre=$1; shift
OMP_NUM_THREADS=2 /usr/bin/time -l python3 "$@" > $pre.log 2> $pre.err &
pid=$!
while kill -0 $pid 2>/dev/null; do
  for c in $(pgrep -P $pid); do
    r=$(ps -o rss= -p $c 2>/dev/null | tr -d ' ')
    if [ -n "$r" ] && [ "$r" -gt 972800 ]; then echo "WATCHDOG KILL rss=${r}KB" >> $pre.err; kill $c; fi
  done
  sleep 2
done
