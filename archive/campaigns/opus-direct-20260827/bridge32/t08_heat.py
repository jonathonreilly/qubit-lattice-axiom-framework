"""T08 - (task item 1)  Does Delta + Delta^2/24 reproduce the EXACT flat-torus heat
trace at the tau0 actually used (2.7-4), and is a_1 unchanged?

(a) flat torus: K_exact(s) = (4 pi s)^-2 L^4 sum_{w in Z^4} exp(-|w|^2 L^2/(4s))
(b) curved: the O(s) term of the heat trace must still be (4 pi s)^-2 s (1/6) int sqrt(g) R
    with int sqrt(g) R = 2 S_Regge -- measured directly from the exact spectrum.
"""
import numpy as np, itertools, sys; sys.path.insert(0,".")
from bridge_geom import *; from bridge_spec import *

def windsum(s, L, W=6):
    n2 = np.array([sum(x*x for x in w) for w in itertools.product(range(-W,W+1),repeat=4)])
    return float(np.exp(-n2*L*L/(4.0*s)).sum())
def Kexact(s, L): return L**4/(4*np.pi*s)**2*windsum(s,L)
def Klat(s, L, improved, chunk=64):
    m = 2*(1-np.cos(2*np.pi*np.arange(L)/L))
    tot = 0.0
    for i in range(0, L, chunk):
        a = m[i:i+chunk][:,None,None,None]+m[None,:,None,None]+m[None,None,:,None]+m[None,None,None,:]
        if improved: a = a + a*a/24.0
        tot += float(np.exp(-s*a).sum())
    return tot

print("T08(a) flat-torus heat trace, relative error |K_lat - K_exact|/K_exact")
print(f"    {'s':>6} " + "".join(f"{'L=%d plain'%L:>14}{'L=%d impr'%L:>14}" for L in (32,64)))
for s in (2.0,2.7,3.0,4.0,6.0,8.0):
    row=f"    {s:6.2f} "
    for L in (32,64):
        Ke=Kexact(s,L)
        row += f"{abs(Klat(s,L,False)-Ke)/Ke:14.3e}{abs(Klat(s,L,True)-Ke)/Ke:14.3e}"
    print(row, flush=True)
print()
print("T08(b) a_1 on a CURVED configuration (exact spectrum, Bloch).")
print("    measured a1_int := [ K(s) - (4 pi s)^-2 Vol ] * (4 pi s)^2 / s   vs   (1/6) int sqrt(g) R = S_Regge/3")
L=12; AMP=0.25; NKW=1; AL=[0.0,1.0,1.0,1.0]
S=edge_s(L,AMP,NKW,AL); g=geometry(S,L)
_,lam = local_Hmatrix(S,L,{'z':lambda w: w*0},ret_spec=True,geom=g)
Vol=g['Vol']; Reg=g['Reg']; pred=Reg/3.0
print(f"    L={L} amp={AMP} conformal-type: Vol={Vol:.6f}  S_Regge={Reg:.6f}  (1/6)int R = {pred:.6f}")
print(f"    {'s':>6} {'plain a1_int':>16} {'improved a1_int':>16} {'predicted':>14}")
for s in (0.6,1.0,1.5,2.0,3.0,4.0):
    out=[]
    for imp in (False,True):
        mu = lam+lam*lam/24.0 if imp else lam
        K=float(np.exp(-s*mu).sum())
        out.append((K-(4*np.pi*s)**-2*Vol)*(4*np.pi*s)**2/s)
    print(f"    {s:6.2f} {out[0]:16.5f} {out[1]:16.5f} {pred:14.5f}")
