# Lemma F check in 2D: 3x3 periodic torus, free spinless fermions with on-site mass and NN hopping,
# rho_x = eps0 n_x + (1/2) sum of hopping bonds touching x. Joint eigenvectors of all 9 rho_x, by particle number.
import numpy as np, sys
sys.path.insert(0,'.')
from r112_lemmaF import fermion_ops, joint_eigvecs
out=[]
def p(s): print(s); out.append(s)
Lx=Ly=3; L=Lx*Ly
def sid(x,y): return (x%Lx)+Lx*(y%Ly)
bonds=set()
for x in range(Lx):
    for y in range(Ly):
        for (dx,dy) in [(1,0),(0,1)]:
            a,b=sid(x,y),sid(x+dx,y+dy); bonds.add(tuple(sorted((a,b))))
c=fermion_ops(L); cd=[m.T for m in c]; n=[cd[j]@c[j] for j in range(L)]
for eps0,t in [(1.0,1.0),(0.3,1.0)]:
    rho=[eps0*n[x]+0.5*sum(-t*(cd[a]@c[b]+cd[b]@c[a]) for (a,b) in bonds if x in (a,b)) for x in range(L)]
    res=[]
    for N in range(L+1):
        basis=np.eye(2**L)[:, [s for s in range(2**L) if bin(s).count('1')==N]]
        res.append(sum(W.shape[1] for W in joint_eigvecs(rho,basis)))
    p(f"3x3 torus, eps0={eps0}, t={t}: joint-eigvec dimension by N=0..9: {res}")
open('r112_lemmaF_2d.out','w').write('\n'.join(out)+'\n')
