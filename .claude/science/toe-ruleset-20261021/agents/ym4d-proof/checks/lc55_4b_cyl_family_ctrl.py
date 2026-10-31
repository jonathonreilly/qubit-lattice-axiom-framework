# lc55_4b — lc55_4 rerun with the corrected horizontality-detector control (criteria: lc55_4b_criteria.md)
# lc55_4 — uniform family on a cylinder region with collar (criteria: lc55_4_criteria.md). Library part copied verbatim
# from lc55_2_certify.py (functions only); plain python + fractions.
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

RESULTS={}
def cyl_basis(n,P=3):
    a=pattern(P)
    one=Poly.const(1); zero=Poly.const(0); s=one+Poly([F(0),F(0),F(1)]); s2=s*s
    Gp=(Poly([F(1),F(0),F(-1)]),zero,zero,Poly([F(0),F(2)])); Gm=(Poly([F(1),F(0),F(-1)]),zero,zero,Poly([F(0),F(-2)]))
    Ghat=lambda x: Gp if a[x%P]==1 else (Gm if a[x%P]==-1 else (s,zero,zero,zero))
    Z3=(zero,zero,zero)
    def unit(i,sc): return tuple(sc if j==i else zero for j in range(3))
    basis=[]
    for i in range(3):
        w1=[unit(i,s2)]*n; w2=[None]+[Z3]*(n-1)+[None]
        basis.append((w1,w2))
    for x0 in range(1,n):
        for i in range(3):
            u=unit(i,one); g=Ghat(x0); y=Adq(g,u)
            D=tuple(y[j]-s2*u[j] for j in range(3))
            w2=[None]+[Z3]*(n-1)+[None]; w2[x0]=unit(i,s2)
            w1=[Z3 if x<x0 else tuple(-D[j] for j in range(3)) for x in range(n)]
            basis.append((w1,w2))
    return basis,Ghat
def cyl_combine(basis,coeffs,zero,n):
    w1=[tuple(sum((coeffs[k]*basis[k][0][x][j] for k in range(len(basis))),zero) for j in range(3)) for x in range(n)]
    w2=[None]+[tuple(sum((coeffs[k]*basis[k][1][x][j] for k in range(len(basis))),zero) for j in range(3)) for x in range(1,n)]+[None]
    return w1,w2
def cyl_Nhat(w1,w2,Ghat,n,zero,one):
    plaqs=reduced_plaqs(n,False)
    def bg(lk):
        kind,x=lk
        return Ghat(x) if kind=='2' else (one,zero,zero,zero)
    def var(lk):
        kind,x=lk
        if kind=='1': return w1[x]
        return w2[x] if 1<=x<=n-1 else None
    return hess_t(plaqs,bg,var,zero,one)
n=9; P=3
zero=Poly.const(0); one=Poly.const(1)
basis,Ghat=cyl_basis(n,P); nb=len(basis)
log('--- G4 cylinder n=%d, basis size %d (expected 3n = %d)'%(n,nb,3*n))
# exact horizontality of each basis vector at three rational tau values
for tv in (F(1,10),F(1,7),F(3,5)):
    Gf=lambda x: tuple(c.ev(tv) for c in Ghat(x))
    for (w1,w2) in basis:
        W1=[tuple(c.ev(tv) for c in v) for v in w1]; W2=[None]+[tuple(c.ev(tv) for c in w2[x]) for x in range(1,n)]+[None]
        for x in range(1,n):
            g=Gf(x); n2=sum(t*t for t in g); adw=tuple(t/n2 for t in Adq(g,W2[x]))
            assert all(W1[x][i]-W1[x-1][i]+adw[i]-W2[x][i]==0 for i in range(3)), 'not horizontal'
log('   every basis vector exactly horizontal at tau in {1/10,1/7,3/5}')
diag=[]
for k in range(nb):
    w1,w2=cyl_combine(basis,[one if i==k else zero for i in range(nb)],zero,n); diag.append(cyl_Nhat(w1,w2,Ghat,n,zero,one))
Q=[[None]*nb for _ in range(nb)]
for k in range(nb):
    Q[k][k]=diag[k]
    for l in range(k+1,nb):
        w1,w2=cyl_combine(basis,[one if i in (k,l) else zero for i in range(nb)],zero,n)
        v=cyl_Nhat(w1,w2,Ghat,n,zero,one); Q[k][l]=Q[l][k]=(v-diag[k]-diag[l])*F(1,2)
deg=max(len(Q[i][j].c) for i in range(nb) for j in range(nb))
Qj=[[[Q[i][j].coef(d) for j in range(nb)] for i in range(nb)] for d in range(deg)]
K=nullspace(Qj[0]); log('   dim ker Q_0 =',len(K),'(expected 3: wall-to-wall holonomy)')
nk=len(K)
first=[[quad(Qj[1],K[a],K[b]) for b in range(nk)] for a in range(nk)]
first_zero=all(x==0 for r in first for x in r)
log('   K^T Q_1 K == 0 :',first_zero)
order=None
if not first_zero:
    best=None
    for co in itertools.product(range(-2,3),repeat=nk):
        if all(c==0 for c in co): continue
        val=sum(co[a]*first[a][b]*co[b] for a in range(nk) for b in range(nk))
        if best is None or val<best[0]: best=(val,co)
    if best[0]<0:
        order=1; co=best[1]
        p0=[sum(co[a]*K[a][i] for a in range(nk)) for i in range(nb)]; ptau=[Poly([p0[i]]) for i in range(nb)]
if order is None:
    P1=[]
    for kv in K:
        rhs=[-sum(Qj[1][i][j]*kv[j] for j in range(nb)) for i in range(nb)]
        sol=solve_exact(Qj[0],rhs); assert sol is not None; P1.append(sol)
    Qeff=[[quad(Qj[2],K[a],K[b])+quad(Qj[1],K[a],P1[b]) for b in range(nk)] for a in range(nk)]
    best=None
    for co in itertools.product(range(-3,4),repeat=nk):
        if all(c==0 for c in co): continue
        val=sum(co[a]*Qeff[a][b]*co[b] for a in range(nk) for b in range(nk))
        if best is None or val<best[0]: best=(val,co)
    log('   Qeff (on K) =',[[str(x) for x in r] for r in Qeff],'; chosen coeffs',best[1],'value',best[0])
    order=2; co=best[1]
    p0=[sum(co[a]*K[a][i] for a in range(nk)) for i in range(nb)]
    p1=[sum(co[a]*P1[a][i] for a in range(nk)) for i in range(nb)]
    ptau=[Poly([p0[i],p1[i]]) for i in range(nb)]
w1,w2=cyl_combine(basis,ptau,zero,n)
N=cyl_Nhat(w1,w2,Ghat,n,zero,one)
Nq=zero
for i in range(nb):
    for j in range(nb):
        Nq=Nq+ptau[i]*Q[i][j]*ptau[j]
consistent=(N==Nq)
D=norm2_vec(w1,[w2[x] for x in range(1,n)],zero)
js=order
low_zero=all(N.coef(j)==0 for j in range(js))
nj=N.coef(js)
tail=sum(abs(N.coef(j))*F(1,10)**(j-js) for j in range(js+1,len(N.c)))
ok=(low_zero and nj<0 and tail<abs(nj) and consistent)
log('   certified order',js,'; coefficients below it zero:',low_zero,'; n_%d ='%js,nj,'; tail bound at 1/10:',float(tail),'< |n|:',tail<abs(nj),'; direct==pQp:',consistent)
kappa=abs(nj)-tail
Dmax=sum(abs(D.coef(j))*F(1,10)**j for j in range(len(D.c)))
cstar=kappa/((1+F(1,100))**2*Dmax)
log('   kappa =',float(kappa),' D_max =',float(Dmax),' c_* =',cstar,'~',float(cstar),'  => RQ_cyl(tau) <= -c_* tau^%d on (0,1/10]'%js)
log('   leading RQ coefficient n_%d/D(0) ='%js,nj/D.coef(0),'~',float(nj/D.coef(0)))
# exact identity 2S1/S0 = 20/((m+1)^2+1)
def S01(m):
    f=[F(x*(m+1-x)) for x in range(m+2)]
    return sum(f[x]**2 for x in range(1,m+1)), sum((f[x+1]-f[x])**2 for x in range(m+1))
idok=all(2*S01(m)[1]/S01(m)[0]==F(20,(m+1)**2+1) for m in range(1,201))
log('   identity 2S1/S0 = 20/((n_perp+1)^2+1) for n_perp=1..200:',idok)
import math
def nperp_of(tau):
    # criteria formula: n_perp := ceil( sqrt( 40/(c_* tau^js) ) )  (exact integer arithmetic)
    X=F(40)/(cstar*tau**js)
    c=-((-X.numerator)//X.denominator)        # ceil(X)
    r=math.isqrt(c)
    return r if r*r>=c else r+1
for tv in (F(1,10),F(1,50),F(1,1000),F(1,10**44)):
    m=nperp_of(tv)
    assert F(20,(m+1)**2+1)<=cstar*tv**js/2
    log('   tau=%s: n_perp(tau) = %d (region x1-width 9, x2 periodic, x3,x4 extent %d+2): RQ_4D <= -c_* tau^%d/2 < 0'%(tv if tv.denominator<10**6 else '1e-44',m,m,js))
RESULTS['G4']=ok and idok
# agreement and controls
ag=True; hz=True
for tv in (F(1,10),F(1,50),F(1,1000)):
    W1=[tuple(c.ev(tv) for c in v) for v in w1]; W2=[None]+[tuple(c.ev(tv) for c in w2[x]) for x in range(1,n)]+[None]
    Gf=lambda x: Gq_of(tv,pattern(P)[x%P]) if pattern(P)[x%P]!=0 else ONEQ
    ht=cyl_hess(W1,W2,Gf,n,'t'); ha=cyl_hess(W1,W2,Gf,n,'a'); hp=N.ev(tv)/(1+tv*tv)**2
    ag=ag and (ht==ha==hp)
    for x in range(1,n):
        g=Gf(x); n2=sum(t*t for t in g); adw=tuple(t/n2 for t in Adq(g,W2[x]))
        hz=hz and all(W1[x][i]-W1[x-1][i]+adw[i]-W2[x][i]==0 for i in range(3))
    if tv==F(1,10):
        W2b=list(W2); W2b[4]=tuple(W2[4][i]+(F(1,7) if i==1 else 0) for i in range(3))
        fired=any(not all(W1[x][i]-W1[x-1][i]+tuple(t/sum(q*q for q in Gf(x)) for t in Adq(Gf(x),W2b[x]))[i]-W2b[x][i]==0 for i in range(3)) for x in range(1,n))
        W1n=[(F(0),F(0),v[2]) for v in W1]; W2n=[None]+[(F(0),F(0),W2[x][2]) for x in range(1,n)]+[None]
        hn=cyl_hess(W1n,W2n,Gf,n,'t')
log('   G4-agree (t-expansion == assembled == polynomial at tau in {1/10,1/50,1/1000}):',ag,'; certified residual zero:',hz,'; C4c detector fires:',fired)
W10=[tuple(c.ev(F(0)) for c in v) for v in w1]; W20=[None]+[tuple(c.ev(F(0)) for c in w2[x]) for x in range(1,n)]+[None]
h0=cyl_hess(W10,W20,lambda x: ONEQ,n,'t')
log('   C4a (tau=0): Hess =',h0,'>= 0:',h0>=0,' | C4b (sigma_3 parts, tau=1/10): Hess =',hn,'>= 0:',hn>=0)
RESULTS['G4agree']=ag and hz
RESULTS['ctrl4']=fired and h0>=0 and hn>=0

# ---- corrected controls C4c' and C4c'' (lc55_4b_criteria.md) ----
tv=F(1,10)
W1=[tuple(c.ev(tv) for c in v) for v in w1]; W2=[None]+[tuple(c.ev(tv) for c in w2[x]) for x in range(1,n)]+[None]
Gf=lambda x: Gq_of(tv,pattern(P)[x%P]) if pattern(P)[x%P]!=0 else ONEQ
def resid(W1,W2):
    out=[]
    for x in range(1,n):
        g=Gf(x); n2=sum(t*t for t in g); adw=tuple(t/n2 for t in Adq(g,W2[x]))
        out.append(tuple(W1[x][i]-W1[x-1][i]+adw[i]-W2[x][i] for i in range(3)))
    return out
W1p=list(W1); W1p[4]=(W1[4][0]+F(1,7),W1[4][1],W1[4][2])
r1=resid(W1p,W2); fired1=any(c!=0 for v in r1 for c in v)
W2p=list(W2); W2p[3]=(W2[3][0]+F(1,7),W2[3][1],W2[3][2])
r2=resid(W1,W2p); fired2=any(c!=0 for v in r2 for c in v)
log("   C4c' (w_1(4) perturbed): residual nonzero:",fired1,"; C4c'' (w_2(3), a=+beta site): residual nonzero:",fired2)
log("   corrected control:", "FIRED" if (fired1 and fired2) else "DID NOT FIRE")
for k,v in RESULTS.items(): log('  ',k,'PASS' if v else 'FAIL')
log('lc55_4 done %.1fs'%(time.time()-T0))
