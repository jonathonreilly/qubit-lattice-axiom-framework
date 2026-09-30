import sys,numpy as np
sys.path.insert(0,'/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T14_scratch')
from yukawa_euclid_gap import run
from indep import fermion_coeffs
def full(eps,m,mu,N):
    Nt=N if abs(eps-1)<1e-12 else int(round(N/eps))
    r=run(Nt,N,eps,m,mu)
    ft,fx,bt,bx=fermion_coeffs(Nt,N,eps,m,mu,h=0.05)
    apsi=fx-ft-m*(bx-bt)
    return r['a_psi'],apsi,r['a_phi']
print("m mu : attacker slope(gap) | corrected slope(gap) ; central diff h=0.02, N=32")
for (m,mu) in [(1.0,1.0),(0.7,0.7),(0.5,0.5),(0.35,0.35),(0.25,0.25)]:
    N=32
    h=0.02
    ap,bp,fp=full(1+h,m,mu,N); am,bm,fm=full(1-h,m,mu,N)
    sa=((ap-fp)-(am-fm))/(2*h); sb=((bp-fp)-(bm-fm))/(2*h)
    print(m,mu,f"{sa:.4f} | {sb:.4f}   (fermion-only attacker {(ap-am)/(2*h):.4f}, corrected {(bp-bm)/(2*h):.4f})")
