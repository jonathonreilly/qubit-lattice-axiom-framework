# Lemma F check: on the joint kernel of C_x = S_x - kappa rho_x (S_x commuting gravity ops), matter components are
# joint eigenvectors of ALL local energy densities rho_x.  Count such joint eigenvectors for free spinless lattice fermions.
import numpy as np, itertools
from scipy.linalg import null_space, orth
out=[]
def p(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
def fermion_ops(L):
    dim=2**L; c=[]
    for j in range(L):
        M=np.zeros((dim,dim))
        for s in range(dim):
            if (s>>j)&1:
                t=s^(1<<j); sign=(-1)**bin(s & ((1<<j)-1)).count('1')
                M[t,s]=sign
        c.append(M)
    return c
def joint_eigvecs(ops, sector_basis):
    # recursively intersect eigenspaces of each op restricted to current subspaces
    subs=[sector_basis]
    for O in ops:
        new=[]
        for W in subs:
            # O must map W into W on the joint eigenvectors; eigvecs of O inside W: solve (O - lam)v=0, v in W
            A=W.T@O@W  # not nec. invariant; joint eigvec v=W y needs O W y = lam W y
            # find all lam: eigenvalues of compressed op as candidates, then verify
            lams=np.unique(np.round(np.linalg.eigvals(A).real,9))
            for lam in lams:
                N=null_space(np.vstack([(O-lam*np.eye(O.shape[0]))@W]),rcond=1e-9)
                if N.shape[1]>0:
                    new.append(orth(W@N))
        subs=new
    return subs
def run(L, eps0, t, choice, dims=1):
    c=fermion_ops(L); cd=[x.T for x in c]; n=[cd[j]@c[j] for j in range(L)]
    bonds=[(j,(j+1)%L) for j in range(L)]
    def hop(a,b): return -(t)*(cd[a]@c[b]+cd[b]@c[a])
    if choice=='site-symmetrized':
        rho=[eps0*n[x]+0.5*sum(hop(a,b) for (a,b) in bonds if x in (a,b)) for x in range(L)]
    elif choice=='bond-left':
        rho=[eps0*n[x]+hop(x,(x+1)%L) for x in range(L)]
    H=sum(rho)
    Nop=sum(n); dim=2**L
    res=[]
    for N in range(L+1):
        basis=np.eye(dim)[:, [s for s in range(dim) if bin(s).count('1')==N]]
        subs=joint_eigvecs(rho, basis)
        d=sum(W.shape[1] for W in subs)
        res.append(d)
    # sanity: H commutes with N; rho_x do not commute
    comm=max(np.abs(rho[0]@rho[1]-rho[1]@rho[0]).max(), 0)
    p(f"L={L} ring, eps0={eps0}, t={t}, rho choice={choice}: max|[rho_0,rho_1]|={comm:.3f}; joint-eigvec dimension by particle number N=0..L: {res}")
    return res
if __name__=="__main__":
  for choice in ['site-symmetrized','bond-left']:
      for L in [6,8]:
          run(L,1.0,1.0,choice)
  p("Control: t=0 (on-site rho, commuting, H_m has no hopping => frozen):")
  run(6,1.0,0.0,'site-symmetrized')
  open(__file__.replace('.py','.out'),'w').write('\n'.join(out)+'\n')
