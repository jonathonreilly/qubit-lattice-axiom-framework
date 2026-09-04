"""T16 — IS THE RECORD WEIGHT ALREADY A BORN PROBABILITY?
W9-style weights are the trace-normalised diagonal of the hermitian part of the
on-site block of Q^-1.  Write  rho = herm(Q^-1)_onsite / Tr(...).  IF rho is
positive semidefinite with unit trace it is a DENSITY MATRIX, and then
        W9_a = <a| rho |a> = Tr(rho P_a)
is literally the Born rule for the derived state rho.  Nothing would need to be
postulated: the framework's record weights would already BE Born probabilities.
Check positivity exactly, on-locus and off-locus, uniform and inhomogeneous."""
import sympy as sp
R = sp.Rational
BAS = [(), (0,), (1,), (0,1)]; IDX = {b:i for i,b in enumerate(BAS)}
def epsm(a):
    M = sp.zeros(4,4)
    for Sx in BAS:
        if a in Sx: continue
        T = tuple(sorted(Sx+(a,))); M[IDX[T], IDX[Sx]] = (-1)**sum(1 for i in Sx if i < a)
    return M
def iota(a, gi):
    M = sp.zeros(4,4)
    for Sx in BAS:
        for pos,i in enumerate(Sx):
            T = tuple(x for x in Sx if x != i); M[IDX[T], IDX[Sx]] += (-1)**pos * gi[a,i]
    return M
def run(cfun, vfun, L=4, m=R(1,2), label=""):
    sites = [(x,y) for x in range(L) for y in range(L)]
    sid = {s:i for i,s in enumerate(sites)}; N = L*L
    def wrap(s): return (s[0]%L, s[1]%L)
    def Dof(s):
        cc, vv = cfun(s), vfun(s)
        g = sp.Matrix([[1,cc],[cc,1]]); gi = g.inv()
        D = sp.zeros(4,4); D[0,0]=vv; D[3,3]=vv*gi.det()
        D[1,1]=vv*gi[0,0]; D[2,2]=vv*gi[1,1]; D[1,2]=vv*gi[0,1]; D[2,1]=vv*gi[1,0]
        return D, gi
    def Gam(s,a):
        _, gi = Dof(s); return sp.Matrix(sp.expand(epsm(a)+iota(a,gi)))
    def U(s,r):
        Ds,_ = Dof(s); Dr,_ = Dof(r)
        Ls = Ds.cholesky(hermitian=False); Lr = Dr.cholesky(hermitian=False)
        return sp.Matrix(sp.expand(Ls.inv().T*Lr.T))
    K = sp.zeros(4*N,4*N)
    for s in sites:
        for a in range(2):
            for sgn, r in ((+1, wrap((s[0]+(a==0), s[1]+(a==1)))), (-1, wrap((s[0]-(a==0), s[1]-(a==1))))):
                Uu = U(s,r); blk = R(1,2)*(Gam(s,a)*Uu + Uu*Gam(r,a))
                i,j = sid[s]*4, sid[r]*4
                for p in range(4):
                    for q in range(4): K[i+p,j+q] += sgn*R(1,2)*blk[p,q]
    Q = sp.Matrix(4*N,4*N, lambda i,j: (m if i==j else 0)+K[i,j])
    Qi = Q.inv()
    psd_all, unit_all, samples = True, True, []
    for s in sites:
        i = sid[s]*4
        G = sp.Matrix(4,4, lambda p,q: R(1,2)*(Qi[i+p,i+q]+Qi[i+q,i+p]))
        tr = sum(G[k,k] for k in range(4))
        rho = sp.Matrix(4,4, lambda p,q: sp.cancel(G[p,q]/tr))
        mins = [sp.cancel(rho[:k,:k].det()) for k in range(1,5)]
        if not all(mn > 0 for mn in mins): psd_all = False
        if sp.cancel(sum(rho[k,k] for k in range(4)) - 1) != 0: unit_all = False
        if len(samples) < 1: samples.append((s, mins, [sp.cancel(rho[k,k]) for k in range(4)]))
    print(f"{label}", flush=True)
    print(f"   rho = herm(Q^-1)_onsite / trace :  unit trace everywhere: {unit_all}", flush=True)
    print(f"   POSITIVE DEFINITE at every site (all leading minors > 0): {psd_all}", flush=True)
    if samples:
        s, mins, diag = samples[0]
        print(f"   sample site {s}: leading minors {[str(x) for x in mins]}", flush=True)
        print(f"                    Born weights <a|rho|a> = {[str(x) for x in diag]}", flush=True)
run(lambda s: R(3,5), lambda s: R(4,5),  label="ON  locus, uniform   (c=3/5, v=4/5)")
run(lambda s: R(3,5), lambda s: R(5,6),  label="OFF locus, uniform   (c=3/5, v=5/6)")
run(lambda s: R(3,5), lambda s: R(1+((3*s[0]+2*s[1])%5),3)+R(1,2), label="OFF locus, INHOMOGENEOUS (lane-style graded volumes)")
