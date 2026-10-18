#!/bin/bash
# C8 class-3 screen (4 cores).  Skeleton index ranges refer to c8_skeletons.generate() sorted by (length, tokens):
# one-slot classes 0-7 length 3, 8-59 length 4, 60-347 length 5; two-slot classes 0-3 length 4, 4-83 length 5.
cd "$(dirname "$0")"
for TAG in one:PC:0-60 onesample:PC:60-348:40 one:PHL:0-8 twosample:0-84:120; do
  python3 c8_screen.py $TAG 4 > "screen_$(echo $TAG | tr ':' '_').log" 2>&1
done
echo ALLDONE > run_screens.done
# added after the first four runs: full PC x PC fills of the 4 length-4 two-slot classes
# python3 c8_screen.py two:0-4 4 > screen_two_0-4.log 2>&1
# NOTE: the first five runs wrote their .pkl files into ../B26_new_shift_letters/ (c8lib's HERE was shadowed by b26lib's;
# fixed afterwards in c8lib.py); the pickles were moved here unchanged (no B26 file was overwritten: distinct names).
