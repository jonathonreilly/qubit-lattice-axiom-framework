"""T26 - P(s) at L=64 (k^2 = 0.00964), where the lattice window a^2/s and the
derivative-expansion window s k^2 are open together over s = 4 .. 60."""
import numpy as np, sys; sys.path.insert(0,".")
z=np.load("spec_L64_a0.06_nk1.npz")
lf=z['flat_lam']; Vf,Rf=z['flat_VR']; k2=(2*np.pi/64)**2
print(f"T26  L=64 amp=0.06 nk=1  k^2={k2:.6f}   Vol={Vf:.0f}")
for imp in (True,False):
    muf=lf+lf*lf/24.0 if imp else lf
    print(f"\n  {'improved' if imp else 'plain'} operator:  (P(s)-dVol)/s   [-> dS_Regge/3]")
    hdr=f"    {'s':>5} {'s k^2':>7}"
    for t in ('gauge','tran','TT','conf'):
        dR=z[t+'_VR'][1]-Rf; hdr+=f"{t+' (%.3f)'%(dR/3):>18}"
    print(hdr)
    for s in (3,4,5,6,8,10,12,16,20,25,32,40,50,60,80):
        if s*k2>1.3: break
        row=f"    {s:5.1f} {s*k2:7.3f}"
        for t in ('gauge','tran','TT','conf'):
            lp=z[t+'_lam']; Vp,Rp=z[t+'_VR']; mu=lp+lp*lp/24.0 if imp else lp
            P=(float(np.exp(-s*mu).sum())-float(np.exp(-s*muf).sum()))*(4*np.pi*s)**2
            v=(P-(Vp-Vf))/s; dR=Rp-Rf
            row+=f"{v:10.4f}"+(f"{v/(dR/3):8.4f}" if abs(dR)>1e-3 else f"{'null':>8}")
        print(row,flush=True)
