import json, numpy as np, sys
sys.path.insert(0,'/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T29_scratch')
from ana import stat
M='/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt'
res=[]
for L in ['12x12x12x24','16x16x16x32','24x24x24x48']:
    d=json.load(open(f'{M}/outputs/alpha_s_wilson_loop_production/ensemble_{L}_unsmeared.json'))
    W=np.array(d['raw_wilson_loops'])  # (ncfg, R, T)
    w11=W[:,0,0]
    m,e,t=stat(w11)
    print(L,'n=',len(w11),'W11=%.6f +/- %.6f  (tau=%.2f)  d=%.2e  d/sigma=%.1f'%(m,e,t,m-0.5934,(m-0.5934)/e), 'sep',d['separation_sweeps'],'beta',d['beta'])
    res.append((m,e))
w=np.array([1/e**2 for m,e in res]); mm=np.array([m for m,e in res])
mean=(w*mm).sum()/w.sum(); err=1/np.sqrt(w.sum())
print('weighted mean of 3 repo ensembles: %.6f +/- %.6f ; d=%.2e (%.1f sigma) ; chi2=%.2f'%(mean,err,mean-0.5934,(mean-0.5934)/err,(w*(mm-mean)**2).sum()))
json.dump({'mean':mean,'err':err,'per':res},open('/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T29_scratch/repo_ensembles_result.json','w'))
