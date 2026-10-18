#!/bin/zsh
cd /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/campaign/NT1P/scripts
until [ -f chainL.done ]; do sleep 10; done
H=$(date -u +%H%M); if [ $H -ge 1415 ]; then echo "too late $H" > chainM.done; exit 0; fi
zsh capped.sh SEARCH_PC_Lt12_1512.out python3 nt1p_search.py 6 8 1512
zsh capped.sh K_PC_Lt12_1512.out python3 nt1p_kernel.py pool_NT1P_PA_wsearchO_Lx4_Lt12_seed1512.npz 6 3 4 5 8
echo done > chainM.done
