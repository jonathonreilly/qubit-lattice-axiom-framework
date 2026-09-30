"""Test B: can the lane's chart H(m,delta,q_+) (copied from scripts/frontier_pmns_selector_three_identity_support_2026_04_21.py)
reach the TM1+reflection triple and the TM2+theta_e+phi triple, and what delta does it then predict? Also: do the three
identities survive re-pinning?"""
import math, numpy as np
from scipy import optimize
from common import observables, BOX61
GAMMA=0.5; E1=math.sqrt(8/3); E2=math.sqrt(8)/3; SEL=math.sqrt(6)/3; Q=2/3
T_M=np.array([[1,0,0],[0,0,1],[0,1,0]],dtype=complex)
T_D=np.array([[0,-1,1],[-1,1,0],[1,0,-1]],dtype=complex)
T_Q=np.array([[0,1,1],[1,0,1],[1,1,0]],dtype=complex)
HB=np.array([[0,E1,-E1-1j*GAMMA],[E1,0,-E2],[-E1+1j*GAMMA,-E2,0]],dtype=complex)
PERM=(2,1,0)
def H(m,d,q): return HB+m*T_M+d*T_D+q*T_Q
def U_of(x):
    w,V=np.linalg.eigh(H(*x)); o=np.argsort(w.real); V=V[:,o]; return V[list(PERM),:]
def obs(x): return observables(U_of(x))
def det(x): return float(np.linalg.det(H(*x)).real)
rng=np.random.default_rng(7)

def solve(target, nstarts=400):
    sols=[]
    def res(x):
        o=obs(x); return [o[0]-target[0], o[1]-target[1], o[2]-target[2]]
    for _ in range(nstarts):
        x0=np.array([rng.uniform(-1.5,3.0), rng.uniform(0.0,2.6), rng.uniform(0.0,3.0)])
        if x0[1]+x0[2] < E1: continue
        try:
            x,info,ier,msg=optimize.fsolve(res,x0,xtol=1e-13,full_output=True)
        except Exception: continue
        if ier!=1 or max(abs(r) for r in res(x))>1e-9: continue
        if x[1]+x[2]-E1 < -1e-9: continue         # chamber
        if not any(np.allclose(x,s,atol=1e-5) for s in sols): sols.append(x)
    return sols

targets = {
 "TM1+reflection @ s13^2=0.0222": (((1-3*0.0222)/(3*(1-0.0222))), 0.0222, 0.5),
 "TM2+theta_e+phi (L10 scratch) ": (0.307, 0.0222, 0.4887),
 "three-identity point (control) ": (0.306178, 0.022139, 0.543623),
 "TM1 free-phase @ s23^2=0.470   ": (0.31802, 0.02245, 0.470),
 "TM1 free-phase @ s23^2=0.545   ": (0.31802, 0.02245, 0.545),
}
for nm, tgt in targets.items():
    sols = solve(tgt)
    print(f"\n{nm} target (s12^2,s13^2,s23^2) = ({tgt[0]:.4f},{tgt[1]:.4f},{tgt[2]:.4f}); chamber solutions found: {len(sols)}")
    for x in sols:
        o=obs(x); d=math.degrees(math.atan2(o[3],o[4]))%360
        m,dl,q=x
        print(f"   (m,delta,q+)=({m:.5f},{dl:.5f},{q:.5f})  sin d={o[3]:+.5f} cos d={o[4]:+.5f} delta_CP={d:.1f} deg  "
              f"dev from identities: Tr {abs(m-Q)/Q:.3f}, dq {abs(dl*q-Q)/Q:.3f}, det {abs(det(x)-E2)/E2:.3f}")
