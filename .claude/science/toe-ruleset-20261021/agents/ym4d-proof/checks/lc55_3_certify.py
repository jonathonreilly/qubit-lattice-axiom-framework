# lc55_3 — exponential chart at the stripe, rigorous rational intervals (criteria: lc55_3_criteria.md). Plain python + fractions.
from fractions import Fraction as F
from math import comb, factorial
import time
T0=time.time()
def log(*a): print(*a,flush=True)
class I:
    __slots__=('lo','hi')
    def __init__(s,lo,hi=None):
        s.lo=F(lo); s.hi=F(lo) if hi is None else F(hi)
        assert s.lo<=s.hi
    def __add__(s,o):
        o=o if isinstance(o,I) else I(o); return I(s.lo+o.lo,s.hi+o.hi)
    __radd__=__add__
    def __neg__(s): return I(-s.hi,-s.lo)
    def __sub__(s,o):
        o=o if isinstance(o,I) else I(o); return I(s.lo-o.hi,s.hi-o.lo)
    def __rsub__(s,o): return (-s)+o
    def __mul__(s,o):
        o=o if isinstance(o,I) else I(o)
        p=[s.lo*o.lo,s.lo*o.hi,s.hi*o.lo,s.hi*o.hi]; return I(min(p),max(p))
    __rmul__=__mul__
    def overlaps(s,o): return not (s.hi<o.lo or o.hi<s.lo)
    def __repr__(s): return '[%.12e, %.12e]'%(float(s.lo),float(s.hi))
def qmul(p,q):
    a,b,c,d=p; e,f,g,h=q
    return (a*e-b*f-c*g-d*h, a*f+e*b-(c*h-d*g), a*g+e*c-(d*f-b*h), a*h+e*d-(b*g-c*f))
def qconj(p): return (p[0],-p[1],-p[2],-p[3])
def qadd(p,q): return tuple(p[i]+q[i] for i in range(4))
def tmul(A,B):
    return [qmul(A[0],B[0]), qadd(qmul(A[0],B[1]),qmul(A[1],B[0])), qadd(qadd(qmul(A[0],B[2]),qmul(A[1],B[1])),qmul(A[2],B[0]))]
# ---- path 1: closed-form scalar functions F(s)=cos sqrt s, Gf(s)=sin sqrt s/ sqrt s, derivatives at s=a^2 ----
def series_enclosure(s,which,der,K=25):
    # which: 'F' (2k)! or 'G' (2k+1)!; der in {0,1,2}
    tot=F(0)
    def term(k):
        if k<der: return F(0)
        fac=factorial(2*k) if which=='F' else factorial(2*k+1)
        coef=F((-1)**k,fac)
        for m in range(der): coef*=(k-m)
        return coef*s**(k-der)
    for k in range(K+1): tot+=term(k)
    # tail: |term_k| <= k^2 s^(k-der)/(2k)!, consecutive ratio <= 1/2 for s<=1, k>=1  => tail <= 2|bound_{K+1}|
    k=K+1; b=F(k*k)*abs(s)**(k-der)/factorial(2*k); tail=2*b
    return I(tot-tail,tot+tail)
def link_series_p1(a,w):
    # E(t)=exp(i(a e3 + t w).sigma) to t^2 ; a rational, w rational 3-vector
    if a==0:
        n2=sum(x*x for x in w)
        return [(I(1),I(0),I(0),I(0)),(I(0),I(w[0]),I(w[1]),I(w[2])),(I(-n2/2),I(0),I(0),I(0))]
    s=a*a
    F0,F1,F2=(series_enclosure(s,'F',d) for d in (0,1,2))
    G0,G1,G2=(series_enclosure(s,'G',d) for d in (0,1,2))
    n2=sum(x*x for x in w); w3=w[2]
    Fd1=F1*(2*a*w3); Fd2=F1*n2+F2*(2*a*a*w3*w3)
    Gd1=G1*(2*a*w3); Gd2=G1*n2+G2*(2*a*a*w3*w3)
    E0=(F0,I(0),I(0),G0*a)
    E1=(Fd1,G0*w[0],G0*w[1],Gd1*a+G0*w3)
    E2=(Fd2,Gd1*w[0],Gd1*w[1],Gd2*a+Gd1*w3)
    return [E0,E1,E2]
# ---- path 2: matrix power series of exp(M0 + t M1), M0 = i a s3, M1 = i w.s (exact Gaussian-rational 2x2), tail bound ----
def cm(x,y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def ca(x,y): return (x[0]+y[0],x[1]+y[1])
def mmul(A,B): return [[ca(cm(A[i][0],B[0][j]),cm(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
def madd(A,B): return [[ca(A[i][j],B[i][j]) for j in range(2)] for i in range(2)]
def mscal(A,x): return [[(A[i][j][0]*x,A[i][j][1]*x) for j in range(2)] for i in range(2)]
Zc=(F(0),F(0)); IDm=[[(F(1),F(0)),Zc],[Zc,(F(1),F(0))]]; ZM=[[Zc,Zc],[Zc,Zc]]
def ivs(w): return [[(F(0),w[2]),(w[1],w[0])],[(-w[1],w[0]),(F(0),-w[2])]]
def mtoq(M):
    al=(M[0][0][0]+M[1][1][0])/2; b3=(M[0][0][1]-M[1][1][1])/2; b1=(M[0][1][1]+M[1][0][1])/2; b2=(M[0][1][0]-M[1][0][0])/2
    return (al,b1,b2,b3)
def link_series_p2(a,w,K=30):
    M0=ivs((F(0),F(0),a)); M1=ivs(w)
    # powers of M0
    P=[IDm]
    for k in range(K+1): P.append(mmul(P[-1],M0))
    c0=ZM; c1=ZM; c2=ZM
    for k in range(0,K+1):
        inv=F(1,factorial(k))
        c0=madd(c0,mscal(P[k],inv))
        if k>=1:
            s1=ZM
            for j in range(k): s1=madd(s1,mmul(mmul(P[j],M1),P[k-1-j]))
            c1=madd(c1,mscal(s1,inv))
        if k>=2:
            s2=ZM
            for j1 in range(k):
                for j2 in range(j1+1,k):
                    s2=madd(s2,mmul(mmul(mmul(mmul(P[j1],M1),P[j2-j1-1]),M1),P[k-1-j2]))
            c2=madd(c2,mscal(s2,inv))
    na=abs(a); nw2=sum(x*x for x in w)
    # crude rational upper bound for |w| : use nw2+1 >= |w| when |w|<=..., safer: |w| <= nw2 if nw2>=1 else 1
    nw=max(nw2,F(1))
    tails=[]
    for d in range(3):
        t=F(0)
        for k in range(K+1,K+60):
            t+=F(comb(k,d))*na**(k-d)*nw**d/factorial(k)
        t*=2  # generous: the remaining terms beyond K+60 are dominated (ratio < 1/2)
        tails.append(t)
    out=[]
    for c,t in zip((c0,c1,c2),tails):
        q=mtoq(c); out.append(tuple(I(x-t,x+t) for x in q))
    return out
def S01(nperp):
    f=[F(x*(nperp+1-x)) for x in range(nperp+2)]
    return sum(f[x]**2 for x in range(1,nperp+1)), sum((f[x+1]-f[x])**2 for x in range(nperp+1))
props=open('lc55_3_proposals.txt').read().splitlines()
heads=[l for l in props if l.startswith('EXPBOX')]; vecs=[l for l in props if l.startswith('EXPVEC')]
inst={F(1,5):12,F(1,20):24}
ALL=True
for head,vline in zip(heads,vecs):
    tok=head.split(); beta=F(tok[1].split('=')[1]); n=int(tok[2].split('=')[1]); nperp=inst[beta]
    links=[tuple(int(t) for t in s.split(',')) for s in head.split(' links ')[1].split()]
    links=[((l[0],l[1]),l[2]) for l in links]; idx={l:i for i,l in enumerate(links)}
    v=[F(x) for x in vline.split()[1:]]; W=[tuple(v[3*i:3*i+3]) for i in range(len(links))]
    pat=[beta,F(0),-beta]
    def A_of(lk): return pat[lk[0][0]%3] if lk[1]==2 else F(0)
    def run(beta_scale, path):
        cache={}
        def series(lk,inv):
            a=A_of(lk)*beta_scale
            i=idx.get(lk); w=W[i] if i is not None else (F(0),F(0),F(0))
            key=(a,w)
            if key not in cache:
                cache[key]=link_series_p1(a,w) if path==1 else link_series_p2(a,w)
            S=cache[key]
            if i is None: S=[S[0],(I(0),I(0),I(0),I(0)),(I(0),I(0),I(0),I(0))]
            return [qconj(x) for x in S] if inv else S
        tot=I(0)
        for x1 in range(n):
            for x2 in range(n):
                fac=[(((x1,x2),1),False),(((x1+1,x2),2),False),(((x1,x2+1),1),True),(((x1,x2),2),True)]
                prod=None
                for (lk,inv) in fac:
                    S=series(lk,inv); prod=S if prod is None else tmul(prod,S)
                tot=tot+prod[2][0]
        return tot*(-2)
    H1=run(F(1),1); H2=run(F(1),2)
    N2=sum(c*c for w in W for c in w)
    s0,s1=S01(nperp); lift=2*s1/s0
    rq1=I(H1.lo/N2,H1.hi/N2)+lift; rq2=I(H2.lo/N2,H2.hi/N2)+lift
    agree=H1.overlaps(H2)
    ok=(rq1.hi<0 and rq2.hi<0 and agree)
    ALL=ALL and ok
    log('--- G3 beta=%s n=%d nperp=%d: Hess path1 %s ; path2 %s ; overlap %s'%(beta,n,nperp,H1,H2,agree))
    log('    |w|^2 = %s ; RQ_2D path1 %s ; 2S1/S0 = %s ; RQ_4D upper ends: path1 %.6e, path2 %.6e -> %s'%(float(N2),I(H1.lo/N2,H1.hi/N2),s1*2/s0,float(rq1.hi),float(rq2.hi),'PASS' if ok else 'FAIL'))
    # Control C3a: beta=0
    H0=run(F(0),1)
    log('    C3a (beta=0, same vector): Hess interval %s ; >= 0 : %s'%(H0,H0.lo>=0))
    ALL=ALL and (H0.lo>=0)
    log('    elapsed %.1fs'%(time.time()-T0))
log('G3 overall:','PASS' if ALL else 'FAIL')
