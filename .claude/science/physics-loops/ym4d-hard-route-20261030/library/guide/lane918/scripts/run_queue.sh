#!/bin/bash
# GUIDE run queue (row 918): one run at a time, nice 10, BLAS=1, memory check before each run.
# Each line of the queue file: <logname> <command args...>
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
cd "$(dirname "$0")/.."
while read -r name rest; do
  [ -z "$name" ] && continue
  free=$(memory_pressure | tail -1 | grep -o '[0-9]*%' | tr -d '%')
  if [ "$free" -lt 30 ]; then echo "SKIP $name: memory free $free%"; continue; fi
  echo "START $name free=$free% $(date +%H:%M:%S)"
  /usr/bin/time -l nice -n 10 python3 $rest > out/$name.log 2> out/$name.err
  rss=$(grep "maximum resident" out/$name.err | awk '{print int($1/1048576)}')
  echo "END $name rc=$? rss=${rss}MB $(date +%H:%M:%S) $(grep -c Traceback out/$name.err) tracebacks"
done < "$1"
echo "QUEUE DONE"
