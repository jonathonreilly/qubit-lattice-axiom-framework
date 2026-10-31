# lc55_2 — exact certifier (criteria: lc55_2_criteria.md). Plain python + fractions only. No floats in any verdict.
from fractions import Fraction as F
import sys, time, itertools
T0=time.time()
def log(*a):
    print(*a,flush=True)
# ---------------- polynomials in tau over Q ----------------
class Poly:
    __slots__=('c',)
    def __init__(self,c):
        c=list(c)
        while len(c)>1 and c[-1]==0: c.pop()
        self.c=c if c else [F(0)]
    @staticmethod
    def const(x): return Poly([F(x)])
    def __add__(s,o):
        o=o if isinstance(o,Poly) else Poly.const(o)
        n=max(len(s.c),len(o.c)); return Poly([(s.c[i] if i<len(s.c) else 0)+(o.c[i] if i<len(o.c) else 0) for i in range(n)])
    __radd__=__add__
    def __neg__(s): return Poly([-x for x in s.c])
    def __sub__(s,o): return s+(-(o if isinstance(o,Poly) else Poly.const(o)))
    def __rsub__(s,o): return (-s)+o
    def __mul__(s,o):
        if not isinstance(o,Poly): return Poly([x*o for x in s.c])
        r=[F(0)]*(len(s.c)+len(o.c)-1)
        for i,a in enumerate(s.c):
            if a==0: continue
            for j,b in enumerate(o.c):
                if b: r[i+j]+=a*b
        return Poly(r)
    __rmul__=__mul__
    def __eq__(s,o):
        o=o if isinstance(o,Poly) else Poly.const(o); return s.c==o.c
    def ev(s,t):
        r=F(0)
        for a in reversed(s.c): r=r*t+a
        return r
    def coef(s,j): return s.c[j] if j<len(s.c) else F(0)
# ---------------- quaternions a + i(b s1 + c s2 + d s3) over any ring ----------------
def qmul(p,q):
    a,b,c,d=p; e,f,g,h=q
    return (a*e-b*f-c*g-d*h, a*f+e*b-(c*h-d*g), a*g+e*c-(d*f-b*h), a*h+e*d-(b*g-c*f))
def qconj(p): return (p[0],-p[1],-p[2],-p[3])
def qadd(p,q): return tuple(p[i]+q[i] for i in range(4))
def qscal(p,x): return tuple(p[i]*x for i in range(4))
def vecq(w): return (w[0]*0,w[0],w[1],w[2])
def Adq(Gq,w,norm2=None):
    # vector part of Gq (0,w) conj(Gq) ; equals |Gq|^2 * Ad_G(w)
    r=qmul(qmul(Gq,vecq(w)),qconj(Gq)); return (r[1],r[2],r[3])
# ---------------- t-series (truncated at t^2) ----------------
def tmul(A,B):
    return [qmul(A[0],B[0]), qadd(qmul(A[0],B[1]),qmul(A[1],B[0])), qadd(qadd(qmul(A[0],B[2]),qmul(A[1],B[1])),qmul(A[2],B[0]))]
def link_series(Gq,w,zero,one):
    n2=w[0]*w[0]+w[1]*w[1]+w[2]*w[2]
    return [Gq, qmul(Gq,(zero,w[0],w[1],w[2])), qscal(Gq,(-n2)*F(1,2)) if not isinstance(n2,Poly) else qmul(Gq,(n2*F(-1,2),zero,zero,zero))]
def inv_series(S): return [qconj(x) for x in S]
def hess_t(plaqs,bg,var,zero,one):
    # plaqs: list of 4-tuples of (linkkey, inverse_flag); bg(linkkey)->quaternion; var(linkkey)->3-vector or None
    tot=zero
    for P in plaqs:
        prod=None
        for (lk,inv) in P:
            w=var(lk)
            Gq=bg(lk)
            if w is None: S=[Gq,(zero,zero,zero,zero),(zero,zero,zero,zero)]
            else: S=link_series(Gq,w,zero,one)
            if inv: S=inv_series(S)
            prod=S if prod is None else tmul(prod,S)
        tot=tot+prod[2][0]
    return tot*(-2)
# ---------------- second, independent path: 2x2 complex matrices over Q(i), assembled insertions ----------------
# complex number = (re, im) of Fractions
def cm(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def ca(a,b): return (a[0]+b[0],a[1]+b[1])
def mmul(A,B): return [[ca(cm(A[i][0],B[0][j]),cm(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
def madd(A,B): return [[ca(A[i][j],B[i][j]) for j in range(2)] for i in range(2)]
def mscal(A,x): return [[(A[i][j][0]*x,A[i][j][1]*x) for j in range(2)] for i in range(2)]
Z0=F(0)
def qtom(q):
    a,b,c,d=q  # a + i(b s1 + c s2 + d s3) = [[a+id, ib + c],[ib - c, a - id]]
    return [[(a,d),(c,b)],[(-c,b),(a,-d)]]
def mdag(A): return [[(A[j][i][0],-A[j][i][1]) for j in range(2)] for i in range(2)]
def ivs(w):  # i w.sigma as matrix
    return [[(Z0,w[2]),(w[1],w[0])],[(-w[1],w[0]),(Z0,-w[2])]]
def hess_assembled(plaqs,bg,var):
    tot=F(0)
    for P in plaqs:
        mats=[]; vs=[]; invs=[]
        for (lk,inv) in P:
            mats.append(qtom(bg(lk))); vs.append(var(lk)); invs.append(inv)
        def factor(k,mode):
            B=mats[k]
            if mode=='0': return mdag(B) if invs[k] else B
            w=vs[k]
            if mode=='1':
                X=ivs(w)
                return mscal(mmul(X,mdag(B)),F(-1)) if invs[k] else mmul(B,X)
            n2=w[0]*w[0]+w[1]*w[1]+w[2]*w[2]
            return mscal(mdag(B),-n2) if invs[k] else mscal(B,-n2)
        acc=F(0)
        for ka in range(4):
            if vs[ka] is None: continue
            for kb in range(4):
                if vs[kb] is None: continue
                M=[[(F(1),Z0),(Z0,Z0)],[(Z0,Z0),(F(1),Z0)]]
                for k in range(4):
                    mode='2' if (ka==kb==k) else ('1' if k in (ka,kb) else '0')
                    M=mmul(M,factor(k,mode))
                tr=M[0][0][0]+M[1][1][0]
                acc+= -F(1,2)*tr
        tot+=acc
    return tot
# ---------------- geometry: reduced 1D (torus or cylinder) ----------------
def Gq_of(tau,sgn):
    den=1+tau*tau; return ((1-tau*tau)/den,F(0),F(0),sgn*2*tau/den)
ONEQ=(F(1),F(0),F(0),F(0))
def pattern(P):
    h=(P-1)//2; a=[0]*P; a[h-1]=1; a[h+1]=-1; return a
def reduced_plaqs(P_or_n,periodic):
    pl=[]
    m=P_or_n
    for x in range(m):
        xp=(x+1)%m if periodic else x+1
        pl.append(((('1',x),False),(('2',xp),False),(('1',x),True),(('2',x),True)))
    return pl
def residual_reduced(w1,w2,Gfun,P,periodic,n=None):
    # R(x) = w1(x) - w1(x-1) + Ad_G(x) w2(x) - w2(x), x over interior sites
    res=[]
    rng=range(P) if periodic else range(1,n)
    for x in rng:
        xm=(x-1)%P if periodic else x-1
        g=Gfun(x)
        adw=Adq(g,w2[x]); n2=sum(t*t for t in g)
        adw=tuple(t/n2 for t in adw)
        res.append(tuple(w1[x][i]-w1[xm][i]+adw[i]-w2[x][i] for i in range(3)))
    return res
# ======================= G2a: reduced torus, exact perturbation theory in tau =======================
def poly_basis(P):
    # returns list of basis vectors e_k(tau) as (w1[x], w2[x]) with Poly entries, and helper data
    a=pattern(P); h=(P-1)//2; xp=h-1; xm=h+1
    one=Poly.const(1); zero=Poly.const(0); s=one+Poly([F(0),F(0),F(1)])  # 1+tau^2
    s2=s*s
    Gp=(Poly([F(1),F(0),F(-1)]),zero,zero,Poly([F(0),F(2)]))   # (1+tau^2) G(+beta)
    Gm=(Poly([F(1),F(0),F(-1)]),zero,zero,Poly([F(0),F(-2)]))
    Ghat=lambda x: Gp if a[x%P]==1 else (Gm if a[x%P]==-1 else (s,zero,zero,zero))
    Z3=(zero,zero,zero)
    basis=[]; names=[]
    def unit(i,scale): return tuple(scale if j==i else zero for j in range(3))
    def build(w1_0,w2):
        # D_y := (Ad_G(y)-1) w2(y) using the exact rules (pattern has inverse backgrounds at x+/x-)
        D=[Z3]*P
        for y in range(P):
            if a[y]==0: continue
        # caller supplies D via closure
        return None
    # (i) constant w1 units
    for i in range(3):
        w1=[unit(i,s2)]*P; w2=[Z3]*P
        basis.append((w1,w2)); names.append('w1(0)_%d'%(i+1))
    # (ii) charged u at x+ (components 1,2), tied at x-
    for i in (0,1):
        u=unit(i,one)
        y=Adq(Gp,u)               # = (1+tau^2)^2 Ad_{G+} u
        w2=[Z3]*P; w2[xp]=unit(i,s2); w2[xm]=y
        Dp=tuple(y[j]-s2*u[j] for j in range(3))     # (Ad_{G+}-1) w2(x+) scaled
        Dm=tuple(s2*u[j]-y[j] for j in range(3))     # (Ad_{G-}-1) w2(x-)
        D=[Z3]*P; D[xp]=Dp; D[xm]=Dm
        w1=[None]*P; w1[0]=Z3
        # recursion w1(x)=w1(x-1)-D(x), x=1..P-1 ; closure at 0 checked below
        for x in range(1,P): w1[x]=tuple(w1[x-1][j]-D[x][j] for j in range(3))
        clos=tuple(w1[P-1][j]-D[0][j]-w1[0][j] for j in range(3))
        assert all(c==0 for c in clos), 'closure failed'
        basis.append((w1,w2)); names.append('u_%d'%(i+1))
    # (iii) charged at a=0 sites
    for x in range(P):
        if a[x]!=0: continue
        for i in (0,1):
            w2=[Z3]*P; w2[x]=unit(i,s2); w1=[Z3]*P
            basis.append((w1,w2)); names.append('c%d_%d'%(x,i+1))
    # (iv) neutral at every site
    for x in range(P):
        w2=[Z3]*P; w2[x]=unit(2,s2); w1=[Z3]*P
        basis.append((w1,w2)); names.append('n%d'%x)
    return basis,names,Ghat,s
def combine(basis,coeffs,zero):
    P=len(basis[0][0])
    w1=[tuple(sum((coeffs[k]*basis[k][0][x][j] for k in range(len(basis))),zero) for j in range(3)) for x in range(P)]
    w2=[tuple(sum((coeffs[k]*basis[k][1][x][j] for k in range(len(basis))),zero) for j in range(3)) for x in range(P)]
    return w1,w2
def Nhat_torus(P,w1,w2,Ghat,zero,one):
    plaqs=reduced_plaqs(P,True)
    def bg(lk):
        kind,x=lk
        return Ghat(x) if kind=='2' else (Poly.const(1)+Poly([F(0),F(0),F(1)]) if isinstance(zero,Poly) else ONEQ, zero,zero,zero)
    # NOTE: direction-1 background is 1; to keep exactly two (1+tau^2) factors per plaquette we use the scaled Ghat
    # only on direction-2 links and the plain identity on direction-1 links:
    def bg2(lk):
        kind,x=lk
        if kind=='2': return Ghat(x)
        return (one,zero,zero,zero)
    def var(lk):
        kind,x=lk
        return w1[x] if kind=='1' else w2[x]
    return hess_t(plaqs,bg2,var,zero,one)
def norm2_vec(w1,w2,zero):
    t=zero
    for v in list(w1)+list(w2):
        for c in v: t=t+c*c
    return t
def solve_exact(A,b):
    # particular solution of A x = b over Q (A square, possibly singular); returns x or None
    n=len(A); M=[list(A[i])+[b[i]] for i in range(n)]
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,n):
            if M[i][c]!=0: p=i; break
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        inv=1/M[r][c]; M[r]=[x*inv for x in M[r]]
        for i in range(n):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[M[i][j]-f*M[r][j] for j in range(n+1)]
        piv.append(c); r+=1
    for i in range(r,n):
        if M[i][n]!=0: return None
    x=[F(0)]*n
    for i,c in enumerate(piv): x[c]=M[i][n]
    return x
def nullspace(A):
    n=len(A); m=len(A[0]); M=[list(r) for r in A]; piv=[]; r=0
    for c in range(m):
        p=None
        for i in range(r,n):
            if M[i][c]!=0: p=i; break
        if p is None: continue
        M[r],M[p]=M[p],M[r]; inv=1/M[r][c]; M[r]=[x*inv for x in M[r]]
        for i in range(n):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[M[i][j]-f*M[r][j] for j in range(m)]
        piv.append(c); r+=1
    free=[c for c in range(m) if c not in piv]; basis=[]
    for fc in free:
        v=[F(0)]*m; v[fc]=F(1)
        for i,c in enumerate(piv): v[c]=-M[i][fc]
        basis.append(v)
    return basis
def quad(Q,p,q=None):
    q=p if q is None else q
    return sum(p[i]*Q[i][j]*q[j] for i in range(len(p)) for j in range(len(q)) if Q[i][j]!=0)
RESULTS={}
def G2a(P):
    log('--- G2a P=%d'%P)
    zero=Poly.const(0); one=Poly.const(1)
    basis,names,Ghat,s=poly_basis(P)
    nb=len(basis); log('   horizontal basis size',nb,'(expected 3P+1 =',3*P+1,')')
    # exact horizontality of every basis vector as a polynomial identity: check at tau = 1/10, 1/7, 3/5 (rational values)
    for tv in (F(1,10),F(1,7),F(3,5)):
        Gfun=lambda x: tuple(c.ev(tv) for c in Ghat(x))
        for (w1,w2) in basis:
            W1=[tuple(c.ev(tv) for c in v) for v in w1]; W2=[tuple(c.ev(tv) for c in v) for v in w2]
            res=residual_reduced(W1,W2,Gfun,P,True)
            assert all(r==0 for v in res for r in v), 'basis vector not horizontal'
    log('   every basis vector exactly horizontal at tau in {1/10,1/7,3/5} (polynomial identity of degree <= 8 checked at 3 points + closure assertion)')
    # quadratic form Qhat(tau) by polarisation
    diag=[]
    for k in range(nb):
        w1,w2=combine(basis,[one if i==k else zero for i in range(nb)],zero)
        diag.append(Nhat_torus(P,w1,w2,Ghat,zero,one))
    Q=[[None]*nb for _ in range(nb)]
    for k in range(nb):
        Q[k][k]=diag[k]
        for l in range(k+1,nb):
            w1,w2=combine(basis,[one if i in (k,l) else zero for i in range(nb)],zero)
            v=Nhat_torus(P,w1,w2,Ghat,zero,one)
            Q[k][l]=Q[l][k]=(v-diag[k]-diag[l])*F(1,2)
    deg=max(len(Q[i][j].c) for i in range(nb) for j in range(nb))
    Qj=[[[Q[i][j].coef(d) for j in range(nb)] for i in range(nb)] for d in range(deg)]
    K=nullspace(Qj[0]); log('   dim ker Q_0 =',len(K),'(torons: expected 6)')
    first=[[quad(Qj[1],K[a],K[b]) for b in range(len(K))] for a in range(len(K))]
    first_zero=all(x==0 for r in first for x in r)
    log('   K^T Q_1 K == 0 :',first_zero)
    # effective second-order form on K
    P1=[]
    for kv in K:
        rhs=[-sum(Qj[1][i][j]*kv[j] for j in range(nb)) for i in range(nb)]
        sol=solve_exact(Qj[0],rhs); assert sol is not None, 'first-order equation not solvable'
        P1.append(sol)
    Qeff=[[quad(Qj[2],K[a],K[b])+quad(Qj[1],K[a],P1[b]) for b in range(len(K))] for a in range(len(K))]
    # choose a rational p0 in K with negative Qeff value: search small integer combinations
    best=None
    nk=len(K)
    for coeffs in itertools.product(range(-2,3),repeat=nk):
        if all(c==0 for c in coeffs): continue
        val=sum(coeffs[a]*Qeff[a][b]*coeffs[b] for a in range(nk) for b in range(nk))
        nrm=sum(c*c for c in coeffs)
        if best is None or val/nrm<best[0]: best=(val/nrm,coeffs,val)
    log('   most negative Qeff value per |coeff|^2 over integer coeffs in [-2,2]^%d:'%nk,best[0],'coeffs',best[1])
    co=best[1]
    p0=[sum(co[a]*K[a][i] for a in range(nk)) for i in range(nb)]
    p1=[sum(co[a]*P1[a][i] for a in range(nk)) for i in range(nb)]
    ptau=[Poly([p0[i],p1[i]]) for i in range(nb)]
    w1,w2=combine(basis,ptau,zero)
    N=Nhat_torus(P,w1,w2,Ghat,zero,one)          # direct t-expansion of the combined vector
    Nq=zero
    for i in range(nb):
        for j in range(nb):
            if p0[i]!=0 or p1[i]!=0:
                Nq=Nq+ptau[i]*Q[i][j]*ptau[j]
    consistent=(N==Nq)
    D=norm2_vec(w1,w2,zero)
    n0,n1,n2=N.coef(0),N.coef(1),N.coef(2)
    tail=sum(abs(N.coef(j))*F(1,10)**(j-2) for j in range(3,len(N.c)))
    ok=(n0==0 and n1==0 and n2<0 and tail<abs(n2) and consistent and first_zero)
    lead=n2/D.coef(0)
    log('   N(tau): deg',len(N.c)-1,'n0',n0,'n1',n1,'n2',n2,'; tail bound at tau0=1/10:',tail,'(< |n2| ?',tail<abs(n2),')')
    log('   direct expansion == p^T Q p :',consistent)
    log('   leading RQ coefficient: RQ = (n2/D0) tau^2 + ... with n2/D0 =',lead,'= approx',float(lead),'; in beta^2 (beta~2tau):',float(lead/4))
    log('   G2a P=%d:'%P,'PASS' if ok else 'FAIL')
    RESULTS['G2a_P%d'%P]=ok
    # G2-agree and controls at tau=1/10 (rational evaluation)
    tv=F(1,10)
    W1=[tuple(c.ev(tv) for c in v) for v in w1]; W2=[tuple(c.ev(tv) for c in v) for v in w2]
    Gfun=lambda x: Gq_of(tv,pattern(P)[x%P]) if pattern(P)[x%P]!=0 else ONEQ
    plaqs=reduced_plaqs(P,True)
    bg=lambda lk: Gfun(lk[1]) if lk[0]=='2' else ONEQ
    var=lambda lk: W1[lk[1]] if lk[0]=='1' else W2[lk[1]]
    h_t=hess_t(plaqs,bg,var,F(0),F(1)); h_a=hess_assembled(plaqs,bg,var)
    h_poly=N.ev(tv)/(1+tv*tv)**2
    agree=(h_t==h_a==h_poly)
    log('   G2-agree at tau=1/10: t-expansion == complex-matrix assembled == polynomial/(1+tau^2)^2 :',agree,' Hess =',float(h_t))
    RESULTS['G2agree_torus_P%d'%P]=agree
    res=residual_reduced(W1,W2,Gfun,P,True); hz=all(r==0 for v in res for r in v)
    # C2c detector: break the tie at x- (use the untied vector)
    W2b=[tuple(v) for v in W2]; xm=(P-1)//2+1; W2b[xm]=tuple(W2[xm][i]+(F(1,3) if i==0 else 0) for i in range(3))
    resb=residual_reduced(W1,W2b,Gfun,P,True); fired=any(r!=0 for v in resb for r in v)
    log('   C2c: certified vector residual zero:',hz,'; perturbed vector residual nonzero (detector fires):',fired)
    # C2a: tau=0
    W10=[tuple(c.ev(F(0)) for c in v) for v in w1]; W20=[tuple(c.ev(F(0)) for c in v) for v in w2]
    var0=lambda lk: W10[lk[1]] if lk[0]=='1' else W20[lk[1]]
    h0=hess_t(plaqs,lambda lk: ONEQ,var0,F(0),F(1))
    log('   C2a (tau=0, same p(0)): Hess =',h0,'>= 0 :',h0>=0)
    # C2b: neutral parts only at tau=1/10
    W1n=[(F(0),F(0),v[2]) for v in W1]; W2n=[(F(0),F(0),v[2]) for v in W2]
    varn=lambda lk: W1n[lk[1]] if lk[0]=='1' else W2n[lk[1]]
    hn=hess_t(plaqs,bg,varn,F(0),F(1))
    log('   C2b (neutral components only): Hess =',hn,'>= 0 :',hn>=0)
    RESULTS['ctrl_torus_P%d'%P]=(hz and fired and h0>=0 and hn>=0)
    return ok
for P in (3,5,7):
    G2a(P)
    log('   elapsed %.1fs'%(time.time()-T0))
# ======================= cylinder geometry =======================
def cyl_vector(params,n,tau,P=3):
    a=pattern(P)
    Gfun=lambda x: Gq_of(tau,a[x%P]) if a[x%P]!=0 else ONEQ
    w1=[None]*n; w2=[None]*(n+1)
    w1[0]=tuple(params[0:3]); w2[0]=None; w2[n]=None
    for x in range(1,n): w2[x]=tuple(params[3*x:3*x+3])
    for x in range(1,n):
        g=Gfun(x); n2=sum(t*t for t in g); adw=tuple(t/n2 for t in Adq(g,w2[x]))
        w1[x]=tuple(w1[x-1][i]-(adw[i]-w2[x][i]) for i in range(3))
    return w1,w2,Gfun
def cyl_hess(w1,w2,Gfun,n,path='t'):
    plaqs=reduced_plaqs(n,False)
    bg=lambda lk: Gfun(lk[1]) if lk[0]=='2' else ONEQ
    def var(lk):
        kind,x=lk
        if kind=='1': return w1[x]
        return w2[x] if 1<=x<=n-1 else None
    return hess_t(plaqs,bg,var,F(0),F(1)) if path=='t' else hess_assembled(plaqs,bg,var)
def cyl_norm(w1,w2,n):
    return sum(c*c for v in w1 for c in v)+sum(c*c for x in range(1,n) for c in w2[x])
def S01(nperp):
    f=[F(x*(nperp+1-x)) for x in range(nperp+2)]
    return sum(f[x]**2 for x in range(1,nperp+1)), sum((f[x+1]-f[x])**2 for x in range(nperp+1))
props=open('lc55_2_proposals.txt').read().splitlines()
cyl_props=[l for l in props if l.startswith('CYL')]
inst={(F(1,10),9):16,(F(1,10),60):12,(F(1,50),9):80,(F(1,50),240):80}
for line in cyl_props:
    head,par=line.split(' params ')
    tok=head.split(); tau=F(tok[1].split('=')[1]); n=int(tok[2].split('=')[1])
    params=[F(x) for x in par.split()]
    nperp=inst[(tau,n)]
    w1,w2,Gfun=cyl_vector(params,n,tau)
    res=residual_reduced(w1,[None]+[w2[x] for x in range(1,n)]+[None] if False else w2,Gfun,None,False,n) if False else None
    # residual at interior sites x=1..n-1: w1(x)-w1(x-1)+Ad w2(x)-w2(x)
    rz=[]
    for x in range(1,n):
        g=Gfun(x); n2=sum(t*t for t in g); adw=tuple(t/n2 for t in Adq(g,w2[x]))
        rz.append(all(w1[x][i]-w1[x-1][i]+adw[i]-w2[x][i]==0 for i in range(3)))
    hz=all(rz)
    H=cyl_hess(w1,w2,Gfun,n,'t'); Ha=cyl_hess(w1,w2,Gfun,n,'a'); Nn=cyl_norm(w1,w2,n)
    s0,s1=S01(nperp); lift=2*s1/s0
    rq=H/Nn; rq4=rq+lift
    ok=(hz and H==Ha and rq4<0)
    RESULTS['G2b_tau%s_n%d'%(tau,n)]=ok
    log('--- G2b cylinder tau=%s n=%d nperp=%d: horizontal(exact)=%s, agree(t vs assembled)=%s'%(tau,n,nperp,hz,H==Ha))
    log('   RQ_cyl = %s ~ %.6e ; 2S1/S0 = %s ~ %.6e ; RQ_4D ~ %.6e  ->  %s'%('(exact rational)',float(rq),s1*2/s0,float(lift),float(rq4),'PASS' if ok else 'FAIL'))
    # controls: tau=0 and neutral
    w1z,w2z,Gz=cyl_vector(params,n,F(0)); Hz=cyl_hess(w1z,w2z,Gz,n,'t')
    w1n=[(F(0),F(0),v[2]) for v in w1]; w2n=[None if v is None else (F(0),F(0),v[2]) for v in w2]
    Hn=cyl_hess(w1n,w2n,Gfun,n,'t')
    log('   C2a tau=0: Hess >= 0 :',Hz>=0,' | C2b neutral-only: Hess >= 0 :',Hn>=0)
    RESULTS['ctrl_cyl_tau%s_n%d'%(tau,n)]=(Hz>=0 and Hn>=0)
    log('   elapsed %.1fs'%(time.time()-T0))
# ======================= G2-sep: full 4D assembly vs lift formula =======================
def G2sep(n,T2,nperp,tau,params):
    P=3; a=pattern(P)
    Gfun=lambda x: Gq_of(tau,a[x%P]) if a[x%P]!=0 else ONEQ
    w1,w2,_=cyl_vector(params,n,tau)
    f=[F(x*(nperp+1-x)) for x in range(nperp+2)]
    NX=[n+1,T2,nperp+2,nperp+2]
    def collar(z): return z[0] in (0,n) or z[2] in (0,nperp+1) or z[3] in (0,nperp+1)
    def nb(z,mu):
        z2=list(z); z2[mu]+=1
        if mu==1: z2[1]%=T2
        elif z2[mu]>=NX[mu]: return None
        return tuple(z2)
    sites=list(itertools.product(range(NX[0]),range(NX[1]),range(NX[2]),range(NX[3])))
    def bgq(lk):
        z,mu=lk
        return Gfun(z[0]) if mu==1 else ONEQ
    def var(lk):
        z,mu=lk
        y=nb(z,mu)
        if collar(z) and collar(y): return None
        ff=f[z[2]]*f[z[3]]
        if mu==0: return tuple(c*ff for c in w1[z[0]])
        if mu==1: return tuple(c*ff for c in w2[z[0]]) if 1<=z[0]<=n-1 else (F(0),F(0),F(0))
        return (F(0),F(0),F(0))
    plaqs=[]
    for z in sites:
        for mu in range(4):
            for nu in range(mu+1,4):
                zm=nb(z,mu); zn=nb(z,nu)
                if zm is None or zn is None: continue
                if nb(zm,nu) is None: continue
                plaqs.append((((z,mu),False),((zm,nu),False),((zn,mu),True),((z,nu),True)))
    H4=hess_t(plaqs,bgq,var,F(0),F(1))
    # 4D norm and horizontality residual at non-collar sites: R(z)=sum_{l from z} Ad_{U_l} v_l - sum_{l into z} v_l
    N4=F(0); R={}
    for z in sites:
        for mu in range(4):
            y=nb(z,mu)
            if y is None: continue
            v=var((z,mu))
            if v is None: continue
            N4+=sum(c*c for c in v)
            g=bgq((z,mu)); n2=sum(t*t for t in g); adv=tuple(t/n2 for t in Adq(g,v))
            if not collar(z): R[z]=tuple((R.get(z,(F(0),)*3)[i]+adv[i]) for i in range(3))
            if not collar(y): R[y]=tuple((R.get(y,(F(0),)*3)[i]-v[i]) for i in range(3))
    hz=all(c==0 for v in R.values() for c in v)
    Hc=cyl_hess(w1,w2,Gfun,n,'t'); Nc=cyl_norm(w1,w2,n); s0,s1=S01(nperp)
    pred=T2*(s0*s0*Hc+2*s0*s1*Nc); predN=T2*s0*s0*Nc
    ok=(H4==pred and N4==predN and hz)
    log('--- G2-sep (n=%d, T2=%d, nperp=%d, tau=%s): Hess_4D == T2(S0^2 Hess_cyl + 2 S0 S1 |w|^2): %s ; |v|^2 identity: %s ; 4D horizontal: %s -> %s'%(n,T2,nperp,tau,H4==pred,N4==predN,hz,'PASS' if ok else 'FAIL'))
    return ok
import random
rnd=random.Random(20261029)
params=[F(rnd.randint(-9,9),rnd.randint(1,7)) for _ in range(3*4)]
RESULTS['G2sep_cyl']=G2sep(4,2,3,F(1,10),params)
log('   elapsed %.1fs'%(time.time()-T0))
# ======================= G2c: 2D box with exact horizontal projection =======================
def G2c():
    line=[l for l in props if l.startswith('BOX ')][0]
    vec=[l for l in props if l.startswith('BOXVEC')][0].split()[1:]
    tok=line.split(); tau=F(1,10); n=12; nperp=16
    links=[tuple(int(t) for t in s.split(',')) for s in line.split(' links ')[1].split()]
    links=[((l[0],l[1]),l[2]) for l in links]
    idx={l:i for i,l in enumerate(links)}
    a=pattern(3)
    Gfun=lambda x1: Gq_of(tau,a[x1%3]) if a[x1%3]!=0 else ONEQ
    bgq=lambda lk: Gfun(lk[0][0]) if lk[1]==2 else ONEQ
    v=[F(x) for x in vec]
    V=[tuple(v[3*i:3*i+3]) for i in range(len(links))]
    def end(lk):
        (x1,x2),mu=lk; return (x1+(mu==1),x2+(mu==2))
    interior=[(x1,x2) for x1 in range(1,n) for x2 in range(1,n)]
    sidx={z:i for i,z in enumerate(interior)}
    def residual(Vv):
        R={z:[F(0)]*3 for z in interior}
        for lk,i in idx.items():
            z=lk[0]; y=end(lk); w=Vv[i]
            if z in R:
                g=bgq(lk); n2=sum(t*t for t in g); adw=Adq(g,w)
                for c in range(3): R[z][c]+=adw[c]/n2
            if y in R:
                for c in range(3): R[y][c]-=w[c]
        return R
    def xi(lam):  # vertical vector of lam (dict site->3-vector)
        out=[(F(0),F(0),F(0))]*len(links)
        for lk,i in idx.items():
            z=lk[0]; y=end(lk); acc=[F(0)]*3
            if z in lam:
                g=bgq(lk); n2=sum(t*t for t in g); ad=Adq(qconj(g),lam[z])   # Ad_{U^{-1}} lam
                for c in range(3): acc[c]+=ad[c]/n2
            if y in lam:
                for c in range(3): acc[c]-=lam[y][c]
            out[i]=tuple(acc)
        return out
    # build the exact matrix A = (lambda -> residual(xi(lambda))) column by column (sparse)
    N=3*len(interior)
    cols={}
    for z in interior:
        for c in range(3):
            lam={z:tuple(F(1) if k==c else F(0) for k in range(3))}
            R=residual(xi(lam))
            col={}
            for zz,vals in R.items():
                for k in range(3):
                    if vals[k]!=0: col[3*sidx[zz]+k]=vals[k]
            cols[3*sidx[z]+c]=col
    rows=[dict() for _ in range(N)]
    for j,col in cols.items():
        for i,val in col.items(): rows[i][j]=val
    R0=residual(V); b=[F(0)]*N
    for z in interior:
        for k in range(3): b[3*sidx[z]+k]=R0[z][k]
    nz0=sum(1 for x in b if x!=0)
    # banded Gaussian elimination (SPD, no pivoting needed; checked: pivots nonzero)
    A=[dict(r) for r in rows]
    for p in range(N):
        piv=A[p].get(p,F(0)); assert piv!=0, 'zero pivot'
        for i in range(p+1,min(N,p+3*(n-1)+4)):
            if p in A[i]:
                f=A[i][p]/piv
                for j,val in A[p].items():
                    if j>=p:
                        nv=A[i].get(j,F(0))-f*val
                        if nv==0: A[i].pop(j,None)
                        else: A[i][j]=nv
                b[i]-=f*b[p]
    lamv=[F(0)]*N
    for p in range(N-1,-1,-1):
        s=b[p]-sum(val*lamv[j] for j,val in A[p].items() if j>p)
        lamv[p]=s/A[p][p]
    lam={z:tuple(lamv[3*sidx[z]+k] for k in range(3)) for z in interior}
    X=xi(lam)
    Vh=[tuple(V[i][k]-X[i][k] for k in range(3)) for i in range(len(links))]
    Rh=residual(Vh); hz=all(x==0 for vals in Rh.values() for x in vals)
    plaqs=[]
    for x1 in range(n):
        for x2 in range(n):
            plaqs.append(((((x1,x2),1),False),((((x1+1,x2)),2),False),((((x1,x2+1)),1),True),(((x1,x2),2),True)))
    def var(lk):
        i=idx.get(lk); return None if i is None else Vh[i]
    H=hess_t(plaqs,bgq,var,F(0),F(1)); Ha=hess_assembled(plaqs,bgq,var)
    Nn=sum(c*c for w in Vh for c in w)
    s0,s1=S01(nperp); rq=H/Nn; rq4=rq+2*s1/s0
    ok=(hz and H==Ha and rq4<0)
    log('--- G2c box n=%d tau=%s nperp=%d: initial residual nonzero entries %d (C2c detector fires: %s); projected residual zero: %s; agree: %s'%(n,tau,nperp,nz0,nz0>0,hz,H==Ha))
    log('   RQ_2D ~ %.6e ; 2S1/S0 ~ %.6e ; RQ_4D ~ %.6e -> %s'%(float(rq),float(2*s1/s0),float(rq4),'PASS' if ok else 'FAIL'))
    # controls
    bg0=lambda lk: ONEQ
    H0=hess_t(plaqs,bg0,var,F(0),F(1))
    Vn=[(F(0),F(0),w[2]) for w in Vh]
    varn=lambda lk: (None if idx.get(lk) is None else Vn[idx[lk]])
    Hn=hess_t(plaqs,bgq,varn,F(0),F(1))
    log('   C2a tau=0 (same vector, trivial background): Hess >= 0 :',H0>=0,' | C2b neutral-only: Hess >= 0 :',Hn>=0)
    RESULTS['G2c_box']=ok; RESULTS['ctrl_box']=(H0>=0 and Hn>=0 and nz0>0)
G2c()
log('   elapsed %.1fs'%(time.time()-T0))
log('=== SUMMARY ===')
for k,v in RESULTS.items(): log('  ',k,'PASS' if v else 'FAIL')
log('lc55_2 done %.1fs'%(time.time()-T0))
