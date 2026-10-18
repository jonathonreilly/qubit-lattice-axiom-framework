#!/usr/bin/env python3
"""B12 independent check, part 1 (different path from b12_lambda_ratio.py).
(a) tadpole normalisation w = <q_P^a q_P^a> per colour component, from the gauge-invariant
    projector diag of the plaquette-link incidence (no gauge fixing) on an L^d torus; compare
    with 2g^2/d and with the textbook <1-P> = (N^2-1) g^2/(8N) (4D) / equipartition.
(b) heat kernel -log K small-field coefficients by direct character sums + polynomial fit at two tau.
(c) symbolic contraction sum_a T^a M T^a -> c(d); Lambda ratios; MSbar via 38.853 exp(-3pi^2/11N^2)."""
import itertools, math
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl
import sympy as S
FAIL=[]
def chk(n,ok,d=""):
    print(("PASS" if ok else "FAIL")+": "+n+" "+d); (None if ok else FAIL.append(n))
# (a) projector diag: action (1/2g^2) sum_P theta_P^2, theta = B A. <theta_P^2> = g^2 [B (B^T B)^+ B^T]_PP
def incidence(L,d):
    V=L**d; idx=lambda x:sum(c*L**i for i,c in enumerate(x))
    link=lambda x,mu: idx(x)*d+mu
    rows=[];cols=[];vals=[];P=0
    for x in itertools.product(range(L),repeat=d):
        for mu in range(d):
            for nu in range(mu+1,d):
                xm=list(x);xm[mu]=(xm[mu]+1)%L; xn=list(x);xn[nu]=(xn[nu]+1)%L
                for l,s in ((link(x,mu),1),(link(xm,nu),1),(link(xn,mu),-1),(link(x,nu),-1)):
                    rows.append(P);cols.append(l);vals.append(s)
                P+=1
    return sp.csr_matrix((vals,(rows,cols)),shape=(P,V*d)).toarray()
for L,d in ((4,2),(3,4),(4,3)):
    B=incidence(L,d); Pr=B@np.linalg.pinv(B.T@B)@B.T; dg=np.diag(Pr)
    rank=np.linalg.matrix_rank(B); V=L**d
    exact=(d*V-(V-1)-d)/(V*d*(d-1)/2)   # (links - gauge orbits - harmonic) / plaquettes
    print(f"   L={L} d={d}: mean diag = {dg.mean():.6f}, spread={dg.max()-dg.min():.1e}, (rank/nP={rank/len(dg):.6f}, counting={exact:.6f}); infinite-volume 2/d={2/d:.4f}")
    chk(f"d={d} plaquette tadpole -> 2/d up to O(1/V)",abs(dg.mean()-exact)<1e-5 and abs(exact-2/d)<2*d/V+1e-12)
# 4D <1-P> textbook: (N^2-1) w/(4N) with w=g^2/2 -> (N^2-1)g^2/(8N): SU(3) beta=6/g^2 -> 2/beta ; SU(2) beta=4/g^2 -> 3/(4beta)
for N,lit in ((2,lambda b:3/(4*b)),(3,lambda b:2/b)):
    b=10.0; g2=2*N/b; chk(f"SU({N}) <1-P>=(N^2-1)w/(4N), w=g^2/2 reproduces textbook",abs((N*N-1)*(g2/2)/(4*N)-lit(b))<1e-15)
# (b) heat kernel by direct character sums (SU(2) closed form; SU(3) Weyl dims/Casimirs from Dynkin labels)
def logK2(phi,tau,jmax=4000):
    j=np.arange(0,jmax)/2; n=2*j+1
    return math.log(np.sum(n*np.sin(n*phi)/np.sin(phi)*np.exp(-tau*j*(j+1))))
def logK3(p1,p2,tau,M=160):
    ph=np.array([p1,p2,-p1-p2]); s=0.0
    den=np.linalg.det(np.exp(1j*np.outer([2,1,0],ph)))
    for a in range(M):
        for b in range(M):
            C2=(a*a+b*b+a*b+3*a+3*b)/3; dm=(a+1)*(b+1)*(a+b+2)/2
            lam=[a+b+2,b+1,0]
            if tau*C2>60: continue
            s+=dm*np.exp(-tau*C2)*(np.linalg.det(np.exp(1j*np.outer(lam,ph)))/den).real
    return math.log(s)
def fit(fun,trX2,ts):
    # -log K(X) + log K(0) = a trX^2 + b trX^4-ish ; return a
    y=np.array([-(fun(t)-fun(1e-4)) for t in ts]); x=np.array([trX2(t) for t in ts])
    A=np.vstack([x,x**2,x**3]).T; return np.linalg.lstsq(A,y,rcond=None)[0]
ts=np.linspace(0.02,0.25,12)
for tau in (0.05,0.1):
    a2=fit(lambda f:logK2(f,tau),lambda f:2*f*f,ts)
    chk(f"SU(2) HK tau={tau}: coeff of trX^2 = 1/(2tau) - N/24",abs(a2[0]-(1/(2*tau)-2/24))<1e-4,f"got {a2[0]:.8f} vs {1/(2*tau)-1/12:.8f}; (trX^2)^2 coeff {a2[1]:.2e} (expected tau-indep. O(1): -1/720 = {-1/720:.2e})")
ts3=np.linspace(0.05,0.35,8)
for tau in (0.06,0.12):
    a3=fit(lambda f:logK3(f,0.37*f,tau),lambda f:f*f+(0.37*f)**2+(1.37*f)**2,ts3)
    chk(f"SU(3) HK tau={tau}: coeff of trX^2 = 1/(2tau) - 3/24",abs(a3[0]-(1/(2*tau)-3/24))<1e-5,f"got {a3[0]:.8f} vs {1/(2*tau)-1/8:.8f}")
# (c) contractions symbolically: sum_a T^a M T^a = (tr M - M/N)/2 ; sum_a T^aT^a = C_F
N,d,g=S.symbols('N d g',positive=True)
w=2*g**2/d; CF=(N**2-1)/(2*N)
tr4_qq = 4*w*CF + 2*w*(-1/(2*N))          # coefficient of trB^2 in <tr(B+q)^4>_qq
cW = -S.Rational(1,12)                     # Wilson: -log w = g^-2[trX^2 - trX^4/12]
# matching: g_HK^-2 - N/24 = g_W^-2 + g^-2 cW <...>  => c = g_HK^-2 - g_W^-2
c = S.simplify(N/24 + cW*tr4_qq/g**2)
print("   c(d) =",S.factor(c),"; c(4) =",S.factor(c.subs(d,4)),"; c(2) =",S.factor(c.subs(d,2)))
chk("c(d) matches B12 claim",S.simplify(c-(N/24-(2/d)*(2*N**2-3)/(12*N)))==0)
chk("c(4)=(3-N^2)/(24N)",S.simplify(c.subs(d,4)-(3-N**2)/(24*N))==0)
chk("k=-2N c(2) = (N^2-2)/4",S.simplify(-2*N*c.subs(d,2)-(N**2-2)/4)==0)
for n in (2,3,4):
    b0=11*n/(48*math.pi**2); cc=float(c.subs({d:4,N:n})); R=math.exp(-cc/(2*b0))
    msw=38.853*math.exp(-3*math.pi**2/(11*n*n))
    print(f"   SU({n}): c={cc:.6f}, dbeta=2Nc={2*n*cc:.4f}, Lambda_HK/Lambda_W={R:.4f}, Lambda_MS/Lambda_W={msw:.3f}, Lambda_MS/Lambda_HK={msw/R:.3f}")
print("SUMMARY:", "ALL PASS" if not FAIL else FAIL)
