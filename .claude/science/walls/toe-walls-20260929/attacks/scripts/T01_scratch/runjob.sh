#!/bin/bash
# args: graph clause p q r L n nblk seed
out="runs/$2_$3_$4_$5_L$6.csv"
./sim "$@" > "$out"
