import math, sys
import numpy as np
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts")
import repeated_formation_check as rf
delta=1.3
for m in (2,3,4,None):
    model=rf.tree_model(m)
    W=model['W'].astype(float);T=model['T'].astype(float);Nd=np.diag(model['N'])
    print(model['label'], "N sectors", sorted(set(int(n) for n in Nd)))
    for eps in (0.1,0.05,0.025):
        Hp=delta*W/eps**2+delta*T/eps
        line=[]
        for n in sorted(set(Nd)):
            idx=np.where(Nd==n)[0]
            e=np.linalg.eigvalsh(Hp[np.ix_(idx,idx)])[0]
            line.append(f"N={int(n)}: E_gs/delta={e/delta:.4f}")
        print(f"   eps={eps}: "+"; ".join(line))
