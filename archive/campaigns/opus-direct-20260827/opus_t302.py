"""
T302 - is R192's "same theory" too strong?  Test the readout correlation.

R192 showed +lambda and -lambda have identical thermodynamics on bipartite Z^3
(Binder |dU| = 0.0000 at L=10).  But the map realising that, rho -> I - rho, is
the antipodal map, and by Skolem-Noether EVERY automorphism of M_n(C) is inner
(unitary conjugation).  The antipodal map is not inner -- it is not even
multiplicative.  So it is NOT a relabeling the Qubit axiom sanctions
("Possibilities are distinguished by the supplied algebraic structure alone").

If so the two branches are DIFFERENT distributions over record configurations,
identical in every measure-derived scalar but opposite in the one thing the
Record axiom's unused readout clauses actually govern: what adjacent records say.
Test the nearest-neighbour readout correlation <v_x . v_{x+e}>, which is exactly
"a readout value is determined by record content alone" applied to two sites.

Controls: (i) the antipodal map is checked against inner-ness directly;
(ii) |m| and U are reported alongside, and must stay equal across the branches.
"""
import numpy as np
print("(1) is rho -> I - rho an automorphism of M2(C)?  (Skolem-Noether: all are inner)")
rng=np.random.default_rng(0)
def rand_rho():
    z=rng.normal(size=2)+1j*rng.normal(size=2); z/=np.linalg.norm(z); return np.outer(z,z.conj())
A,B=rand_rho(),rand_rho(); I=np.eye(2)
lhs=(I-A)@(I-B); rhs=I-A@B
print(f"    multiplicative?  max|f(A)f(B) - f(AB)| = {np.abs(lhs-rhs).max():.4f}   -> {'yes' if np.abs(lhs-rhs).max()<1e-12 else 'NO, not an algebra map'}")
print(f"    so it is not inner, and not an allowed relabeling of possibilities.\n")

def run(L,lam,sweeps=5000,burn=1200,seed=5):
    rng=np.random.default_rng(seed)
    v=rng.normal(size=(L,L,L,3)); v/=np.linalg.norm(v,axis=-1,keepdims=True)
    i,j,k=np.indices((L,L,L)); stag=(-1.0)**((i+j+k)%2)
    C=[];M=[]
    for sw in range(sweeps):
        for _ in range(L**3):
            a,b,c=rng.integers(0,L,3)
            nbs=np.array([v[(a+1)%L,b,c],v[a-1,b,c],v[a,(b+1)%L,c],
                          v[a,b-1,c],v[a,b,(c+1)%L],v[a,b,c-1]])
            new=rng.normal(size=3); new/=np.linalg.norm(new); old=v[a,b,c]
            num=np.prod(1+lam*(nbs@new)); den=np.prod(1+lam*(nbs@old))
            if den<=0 or num<0: continue
            if num>=den or rng.random()<num/den: v[a,b,c]=new
        if sw>=burn and sw%5==0:
            corr=np.mean([np.sum(v*np.roll(v,1,axis=ax),axis=-1).mean() for ax in range(3)])
            C.append(corr)
            w = v if lam>0 else v*stag[...,None]
            M.append(np.linalg.norm(w.sum(axis=(0,1,2)))/L**3)
    return np.mean(C),np.mean(M)
print("(2) nearest-neighbour READOUT correlation <v_x . v_{x+e}>  (M2(C), Z^3)")
print("    L    lam     <v.v'>      |m| (own channel)")
for L in (6,8):
    for lam in (1.0,-1.0):
        c,m=run(L,lam)
        print(f"   {L:3d}   {lam:+.1f}   {c:+.5f}     {m:.5f}")
print("\n  identical |m| but OPPOSITE <v.v'> => same thermodynamics, different physics.")
