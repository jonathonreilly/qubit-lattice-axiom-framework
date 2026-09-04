"""
T299 - the admissibility parameter's NEGATIVE half, never examined.

R136 forced phi = a + lambda(v.v'); R137 explored lambda in [0,1] and reported
"two-thirds of the admissible range [0,1]" excluded.  But positivity of
1 + lambda(v.v') with v.v' in [-1,1] admits lambda in [-1,1].  T298 confirms the
positivity region is a SPINDLE with two apexes: lambda=+1 (Born, vanishes on
ORTHOGONAL neighbours) and lambda=-1 (vanishes on IDENTICAL neighbours).

Z^3 is bipartite, so v_x -> -v_x on one sublattice sends every edge factor
(1 + lambda v.v') -> (1 - lambda v.v').  That is an exact measure-preserving
bijection between +lambda and -lambda, so the two branches must have IDENTICAL
thermodynamics with uniform <-> staggered order parameters exchanged.

Test: Binder cumulant at +lambda (uniform m) vs -lambda (staggered m).
Controls: U -> 4/9 disordered, 2/3 ordered for a 3-component order parameter.
"""
import numpy as np
def run(L,lam,sweeps=6000,burn=1500,seed=5):
    rng=np.random.default_rng(seed)
    v=rng.normal(size=(L,L,L,3)); v/=np.linalg.norm(v,axis=-1,keepdims=True)
    i,j,k=np.indices((L,L,L)); stag=(-1.0)**((i+j+k)%2)
    m2=[];m4=[]
    for sw in range(sweeps):
        for _ in range(L**3):
            a,b,c=rng.integers(0,L,3)
            nb=(v[(a+1)%L,b,c]+v[a-1,b,c]+v[a,(b+1)%L,c]+v[a,b-1,c]
                +v[a,b,(c+1)%L]+v[a,b,c-1])
            new=rng.normal(size=3); new/=np.linalg.norm(new)
            old=v[a,b,c]
            # weight ratio = prod_nb (1+lam new.v_nb)/(1+lam old.v_nb)
            nbs=np.array([v[(a+1)%L,b,c],v[a-1,b,c],v[a,(b+1)%L,c],
                          v[a,b-1,c],v[a,b,(c+1)%L],v[a,b,c-1]])
            num=np.prod(1+lam*(nbs@new)); den=np.prod(1+lam*(nbs@old))
            if den<=0 or num<0: continue
            if num>=den or rng.random()<num/den: v[a,b,c]=new
        if sw>=burn and sw%5==0:
            w = v if lam>0 else v*stag[...,None]      # uniform vs staggered
            m=np.linalg.norm(w.sum(axis=(0,1,2)))/L**3
            m2.append(m*m); m4.append(m**4)
    m2=np.mean(m2); m4=np.mean(m4)
    return 1-m4/(3*m2*m2), np.sqrt(m2)
print("Binder U (3-component: 4/9=0.4444 disordered, 2/3=0.6667 ordered)")
print("lam>0 uses the UNIFORM order parameter, lam<0 the STAGGERED one.\n")
print("   L    lam     U         |m|        lam     U         |m|      |dU|")
for L in (6,8,10):
    for lam in (0.50,1.00):
        up,mp=run(L,lam); un,mn=run(L,-lam)
        print(f"  {L:3d}  {lam:+.2f}  {up:.4f}  {mp:.4f}     {-lam:+.2f}  {un:.4f}  {mn:.4f}   {abs(up-un):.4f}")
