#!/bin/zsh
cd ${0:a:h}
until [ -f chainC2.done ]; do sleep 3; done
./capped.sh INF2_torus_Lt16_t03.out python3 uv1_inf.py torus 8 3 24 9103
./capped.sh INF2_torus_Lt20_t03.out python3 uv1_inf.py torus 10 3 24 9503
./capped.sh INF2_torus_Lt20_t04.out python3 uv1_inf.py torus 10 4 24 9504
./capped.sh LOC_free_overlap.out python3 uv1_locality.py
echo done > chainD.done
