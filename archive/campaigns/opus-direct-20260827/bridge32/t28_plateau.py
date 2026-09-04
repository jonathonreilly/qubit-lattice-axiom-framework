"""T28 - the plateau, quantified.  r(s) = [measured a_1]/[S_Regge/3] carries
   + a lattice tail  c1/s (+c1'/s^2)          [dies as a -> 0]
   + a derivative-expansion tail  c2 * s k^2  [dies as k -> 0]
so fitting r(s) = r0 + c1/s + c2 s (+ c1'/s^2) over the open window and reading r0
is the plateau value.  Done for both operators, both lattices, several channels."""
import numpy as np, sys
def rs(z,pre,post,ss,imp):
    lf=z['flat'+post]; Vf,Rf=z['flat'+pre]; muf=lf+lf*lf/24.0 if imp else lf
    def f(t):
        lp=z[t+post]; Vp,Rp=z[t+pre]; mu=lp+lp*lp/24.0 if imp else lp
        dV=Vp-Vf; dR=Rp-Rf
        return np.array([((float(np.exp(-s*mu).sum())-float(np.exp(-s*muf).sum()))*(4*np.pi*s)**2-dV)/s/(dR/3) for s in ss]),dR
    return f
def fit(ss,r,basis):
    M=np.stack([ss**0.0 if b=='1' else (ss if b=='s' else ss**float(b)) for b in basis],1)
    c,*_=np.linalg.lstsq(M,r,rcond=None); return c[0], np.linalg.norm(r-M@c)/np.sqrt(len(r))
print("T28  plateau value r0 of the induced a_1 relative to the Regge/Einstein prediction")
for fn,L,pre,post,chans in (("spec_L64_a0.06_nk1.npz",64,'_VR','_lam',['TT','conf']),
                            ("struct_L32_a0.06_nk1_14.npz",32,'VR','lam',['(0, 1, -1, 0)','(1, 1, 1, 1)'])):
    z=np.load(fn); k2=(2*np.pi/L)**2
    for imp in (True,False):
        for t in chans:
            for (s0,s1) in (((6,60),(8,40)) if L==64 else ((5,20),(6,25))):
                ss=np.array([x for x in (5,6,8,10,12,16,20,25,32,40,50,60) if s0<=x<=s1],float)
                g=rs(z,pre,post,ss,imp); r,dR=g(t)
                a,_=fit(ss,r,['1','-1','s']); b,_=fit(ss,r,['1','-1','-2','s'])
                print(f"  L={L:3d} {'imp' if imp else 'pln'} {str(t)[:14]:>14} s in [{s0:2d},{s1:2d}] "
                      f"s k^2<={s1*k2:5.3f}:  r0 = {a:8.4f} (1+1/s+s) , {b:8.4f} (+1/s^2)   "
                      f"raw r at ends {r[0]:.4f}..{r[-1]:.4f}")
        print()
