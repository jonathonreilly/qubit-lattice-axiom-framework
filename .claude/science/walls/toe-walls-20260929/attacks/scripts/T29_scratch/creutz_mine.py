import numpy as np, glob, math, os, sys
here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,here)
from ana import load
for Ltag in ('L8','L12'):
    Ws=[]
    for fn in sorted(glob.glob(f'{here}/runs/hb_{Ltag}_*.txt')):
        P,W,h=load(fn)
        Ws+= [np.array(w).reshape(4,4) for w in W if w is not None]
    if not Ws: continue
    Ws=np.array(Ws); n=len(Ws)
    def chi_all(Wm):
        Wm=0.5*(Wm+Wm.T); out=[]
        for R in (2,3,4):
            out.append(-math.log(Wm[R-1,R-1]*Wm[R-2,R-2]/(Wm[R-1,R-2]*Wm[R-2,R-1])))
        return np.array(out)
    c=chi_all(Ws.mean(0))
    # jackknife
    jk=np.array([chi_all(np.delete(Ws,i,axis=0).mean(0)) for i in range(n)])
    err=np.sqrt((n-1)/n*((jk-jk.mean(0))**2).sum(0))
    print(Ltag,'n_meas=',n,'W11=%.5f'%Ws[:,0,0].mean())
    for R,ch,e in zip((2,3,4),c,err):
        r=R-0.5; print(f'  chi({R},{R})={ch:.4f}+/-{e:.4f}  r={r}  alpha_qq(Creutz)={r*r*ch/(4/3):.3f}')
