#!/bin/zsh
cd /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/campaign/NT1P/scripts
zsh capped.sh K_PA_Lt8_1504.out python3 nt1p_kernel.py pool_NT1P_PA_wsearchO_Lx4_Lt8_seed1504.npz 4
zsh capped.sh K_PB_Lt8_2504.out python3 nt1p_kernel.py pool_NT1P_PB_random_Lx4_Lt8_seed2504.npz 4
echo done > chainK.done
