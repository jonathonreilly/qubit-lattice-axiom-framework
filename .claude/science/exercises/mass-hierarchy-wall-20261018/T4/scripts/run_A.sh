#!/bin/zsh
cd ${0:a:h}
zsh capped.sh ../t4_vacA.out python3 t4_vacuum.py A 300 8
zsh capped.sh ../t4_vacA2.out python3 t4_vacA2.py A2 10 9
echo DONE > ../run_A.done
