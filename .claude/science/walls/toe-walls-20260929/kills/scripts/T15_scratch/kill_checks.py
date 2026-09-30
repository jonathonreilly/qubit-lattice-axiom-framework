"""Kill-round independent checks for T15 (Claude Sonnet 5.5, same family as attacker).
K1: independent determinant (eigenvalue product, not slogdet) vs doubled KS, incl. anisotropy kappa.
K2: first-order (Wilson-like / KS) time action gives ONE copy -> Test A does discriminate.
K3: analytic closed form prod_l (mu^2 + kappa^2 sin^2 p_l).
K4: node table of exp(-i tau H_KS) vs a shift-type (Weyl walk) tick, to see what 'N=8' in Route C really refers to.
"""
import itertools, math, numpy as np

def ops(N,d):
    sites=list(itertools.product(range(N),repeat=d)); idx={s:i for i,s in enumerate(sites)}; n=len(sites)
    A=np.zeros((n,n),complex); P=np.zeros(n)
    for s in sites:
        i=idx[s]; P[i]=(-1)**sum(s)
        for mu in range(d):
            eta=(-1)**sum(s[:mu]); sp=list(s); sp[mu]=(sp[mu]+1)%N; sm=list(s); sm[mu]=(sm[mu]-1)%N
            A[i,idx[tuple(sp)]]+=0.5*eta; A[i,idx[tuple(sm)]]-=0.5*eta
    return A,np.diag(P),n

def S_anti(L):
    S=np.zeros((L,L))
    for t in range(L):
        S[t,(t+1)%L]+= 1 if t+1<L else -1
        S[t,(t-1)%L]-= 1 if t-1>=0 else -1
    return S

def lnZ(levels,beta):
    x=0.5*beta*levels
    return float(np.sum(np.abs(x)+np.log1p(np.exp(-2*np.abs(x)))))

print("K1: independent eigenvalue-product determinant, anisotropy kappa (temporal hop coefficient)")
for (d,N,m,L,kap) in [(1,4,0.5,4,1.0),(2,4,0.5,4,1.0),(2,4,0.5,6,3.0),(2,4,0.3,6,10.0),(3,4,0.4,4,0.7),(3,4,0.3,6,5.0)]:
    A,P,n=ops(N,d)
    D=m*np.eye(n*L)+np.kron(A,np.eye(L))+0.5*kap*np.kron(P,S_anti(L))
    ev=np.linalg.eigvals(D); lhs=float(np.sum(np.log(np.abs(ev))))
    B=P@(A+m*np.eye(n)); mu=np.linalg.eigvalsh(B)
    e=np.sign(mu)*np.arcsinh(np.abs(mu)/kap)
    rhs=n*L*math.log(kap)-n*L*math.log(2)+2*lnZ(e,L)
    one=n*L*math.log(kap)-0.5*n*L*math.log(2)+lnZ(e,L)
    print(f" d={d} N={N} m={m} L={L} kappa={kap}: |lhs-doubled|={abs(lhs-rhs):.2e}  |lhs-single|={abs(lhs-one):.3f}")

print("K2: first-order-in-time action  D1 = (1+eps(m+A)) - Fwd(antiperiodic): expect ONE copy prod(1+a_j^L)")
for (d,N,m,L,eps) in [(1,4,0.5,4,0.3),(2,4,0.5,6,0.2),(3,4,0.3,4,0.15)]:
    A,P,n=ops(N,d)
    F=np.zeros((L,L))
    for t in range(L): F[t,(t+1)%L]= 1 if t+1<L else -1
    M=np.eye(n)+eps*(m*np.eye(n)+A)
    D1=np.kron(M,np.eye(L))-np.kron(np.eye(n),F)
    ev=np.linalg.eigvals(D1); lhs=float(np.sum(np.log(np.abs(ev))))
    a=np.linalg.eigvals(M)
    rhs=float(np.sum(np.log(np.abs(1+a**L))))
    print(f" d={d} L={L}: n={n} modes (Fock dim 2^n): |lhs-rhs|={abs(lhs-rhs):.2e}  (single copy, n modes)")

print("K3: closed form for the staggered time product, r=sinh u, L even, antiperiodic:")
for (r,L) in [(0.4,4),(0.9,6),(1.5,8)]:
    p=np.pi*(2*np.arange(L)+1)/L
    lhs=np.prod(r**2+np.sin(p)**2); u=math.asinh(r)
    rhs=(2*math.cosh(L*u/2))**4/2**(2*L)
    print(f" r={r} L={L}: prod={lhs:.10f} (2cosh(Lu/2))^4/2^(2L)={rhs:.10f}")

print("K4: quasi-energy nodes per spatial corner for (i) exp(-i tau H_KS) tau=1 and (ii) 1D shift-type Dirac walk U=diag(e^{ik},e^{-ik})")
k=np.linspace(-np.pi,np.pi,2001)
# 1D Dirac walk massless: eigenphases +-k ; count k where quasienergy=0 and where =pi
om=np.stack([k,-k])
def near(x,t): return np.sum(np.abs(np.angle(np.exp(1j*(x-t))))<2e-3)
print(" walk 1D massless: grid points with |omega-0|<2e-3:",near(om[0],0)+near(om[1],0)," with |omega-pi|<2e-3:",near(om[0],np.pi)+near(om[1],np.pi))
print(" (walk bands wind the quasi-energy circle: nodes at 0 (k=0) and at pi (k=pi); the KS exp(-i tau H) table in Test D has none at pi)")
