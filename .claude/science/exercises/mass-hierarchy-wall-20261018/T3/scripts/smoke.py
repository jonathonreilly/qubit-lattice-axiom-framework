import time, numpy as np
from t3_landau import *
S,C=bz_axis(16)
for lam in [np.array([1,0,0.]), np.array([0,0,1.]), np.array([0.3,-0.5,0.8])/np.linalg.norm([0.3,-0.5,0.8])]:
  for w in (False,True):
    t0=time.time(); R=run_coupling_A(2.0, lam, S, C, w)
    print(lam, w, f'{time.time()-t0:.2f}s', 're',round(R['re'],3),'b',R['b'],'c',R['c'],'q',R['q'][:3])
    print('   realised', np.round(R['rr'][R['real']],3), [classify(R['tstar'][j]) for j in R['real']], np.round(np.degrees(R['tstar']),1)[::5])
# convergence of b3,c6 with M
lam=np.array([0.3,-0.5,0.8])/np.linalg.norm([0.3,-0.5,0.8])
for M in (12,16,24):
  S,C=bz_axis(M); R=run_coupling_A(2.0, lam, S, C, False); print('M',M,'b3',R['b'][0],'c6',R['c'][0], 'a2', R['q'][1])
