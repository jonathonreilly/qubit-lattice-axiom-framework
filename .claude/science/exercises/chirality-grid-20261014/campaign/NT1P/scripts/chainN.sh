#!/bin/zsh
cd /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/campaign/NT1P/scripts
until [ -f chainM.done ]; do sleep 10; done
zsh capped.sh LOC_Lx8_Lt12_11112_desc_s302.out python3 nt1p_locality.py 8 6 11112 302 1
echo done > chainN.done
