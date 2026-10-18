import numpy as np
from chi2 import *
Hr=np.load('clean_Hr.npy'); bl=blocks_from(Hr); mu=np.linalg.eigvalsh(Hk(bl,kst))[0]
res={}
for name,Qv in (('0',np.zeros(3)),('Q',Q)):
    for N in (12,16):
        chi=chi_matrix(bl,mu,Qv,N=N,T=0.005)
        idv=np.array([np.trace(B).real for B in Bm])/np.sqrt(12); Pr=np.eye(144)-np.outer(idv,idv)
        top=np.linalg.eigvalsh(Pr@chi@Pr)[-1]
        sec={}
        for char in ('A1','A2'):
            for part in ('real','imag'):
                Vs=proj_sector(char,part)
                if Vs.shape[1]==0: continue
                Vs=Pr@Vs; Vs,_=np.linalg.qr(Vs); sec[(char,part)]=round(np.linalg.eigvalsh(Vs.conj().T@chi@Vs)[-1],4)
        print(f'Q={name} N={N}: leading chi over all traceless on-site channels {top:.4f}; by sector {sec}',flush=True)
