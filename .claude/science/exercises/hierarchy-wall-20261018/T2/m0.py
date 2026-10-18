import numpy as np, sys
def binerr(x, nb=40):
    n=len(x)//nb*nb; b=x[:n].reshape(nb,-1).mean(1); return b.mean(), b.std(ddof=1)/np.sqrt(nb)
L=8; N=L**3
for beta,tag in [(0.50,'50'),(0.60,'60')]:
    w=np.fromfile(f'data/m0_w{tag}.bin').reshape(-1,4)
    l=np.fromfile(f'data/m0_l{tag}.bin').reshape(-1,2)
    a,ea=binerr(w[:,2]/N**2); b,eb=binerr(l[:,0]/N**2)
    # also pair energy per site
    c,ec=binerr(w[:,0]/N); d,ed=binerr(l[:,1]/N)
    print(f'beta={beta}: <|m_level|^2> wolff(pair law) {a:.5f}+-{ea:.5f}  landed kernel {b:.5f}+-{eb:.5f}  diff/sigma {(a-b)/np.hypot(ea,eb):+.2f}')
    print(f'          pair energy/site   wolff {c:.5f}+-{ec:.5f}  landed kernel {d:.5f}+-{ed:.5f}  diff/sigma {(c-d)/np.hypot(ec,ed):+.2f}')
