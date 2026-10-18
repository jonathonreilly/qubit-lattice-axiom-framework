#!/bin/zsh
cd /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/campaign/NT1P/scripts
until [ -f chainK.done ]; do sleep 10; done
zsh capped.sh INDEP_PA.out python3 nt1p_indep.py pool_NT1P_PA_wsearchO_Lx4_Lt8_seed1504.npz
zsh capped.sh LOC_Lx8_Lt12_11112_desc.out python3 nt1p_locality.py 8 6 11112 301 1
zsh capped.sh LOC_Lx8_Lt12_L1_desc.out python3 nt1p_locality.py 8 6 L1 301 1
echo done > chainL.done
