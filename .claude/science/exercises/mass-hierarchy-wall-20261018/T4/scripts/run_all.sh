#!/bin/zsh
cd ${0:a:h}
zsh capped.sh ../t4_leak_NO_min.out   python3 t4_leak.py 1000 NO 21 8
zsh capped.sh ../t4_leak_NO_count.out python3 t4_leak.py 1000 NO 22 count
zsh capped.sh ../t4_leak_NO0_min.out  python3 t4_leak.py 1000 NO0 23 8
zsh capped.sh ../t4_leak_IO_min.out   python3 t4_leak.py 1000 IO 24 8
zsh capped.sh ../t4_vacB.out          python3 t4_vacuum.py B 500 7
zsh capped.sh ../t4_vacA.out          python3 t4_vacuum.py A 300 8
echo ALLDONE > ../run_all.done
