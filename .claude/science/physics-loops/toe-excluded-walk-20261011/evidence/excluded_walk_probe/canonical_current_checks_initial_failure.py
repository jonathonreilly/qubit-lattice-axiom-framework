"""External independent finite checks of the canonical-current draft.
Arithmetic helpers copied from the reviewer's own frozen exact checker;
no root runner, repo science module, or Fourier truncation is used.

Exact Gaussian-rational matrix calculations test algebra, not threshold analysis.
Deterministic angular quadrature checks finite shell normalizations and scaling;
it is not an interval proof or a proof of the principal-value estimate.
"""
from fractions import Fraction as F
from itertools import product
from math import sin, cos, sqrt, pi, asin


class Q:
    def __init__(self, x=0, y=0):
        if isinstance(x, Q):
            self.x, self.y = x.x, x.y
        else:
            self.x, self.y = F(x), F(y)
    def __add__(self, o):
        o = Q(o)
        return Q(self.x + o.x, self.y + o.y)
    __radd__ = __add__
    def __neg__(self):
        return Q(-self.x, -self.y)
    def __sub__(self, o):
        return self + -Q(o)
    def __rsub__(self, o):
        return Q(o) + -self
    def __mul__(self, o):
        o = Q(o)
        return Q(self.x*o.x-self.y*o.y, self.x*o.y+self.y*o.x)
    __rmul__ = __mul__
    def conj(self):
        return Q(self.x, -self.y)
    def abs2(self):
        return self.x*self.x + self.y*self.y
    def __truediv__(self, o):
        o = Q(o)
        t = self * o.conj()
        return Q(t.x/o.abs2(), t.y/o.abs2())
    def __rtruediv__(self, o):
        return Q(o) / self
    def __eq__(self, o):
        o = Q(o)
        return self.x == o.x and self.y == o.y
    def __repr__(self):
        return f"({self.x}+{self.y}i)"


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]
def add(a, b):
    return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(a, z):
    return [[Q(z)*x for x in row] for row in a]
def mul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), Q())
             for j in range(len(b[0]))] for i in range(len(a))]
def star(a):
    return [[Q(x).conj() for x in row] for row in zip(*a)]
def inv(a):
    n = len(a)
    x = [list(map(Q,a[i]))+eye(n)[i] for i in range(n)]
    for k in range(n):
        p = next(i for i in range(k,n) if x[i][k] != 0)
        x[k], x[p] = x[p], x[k]
        pivot = x[k][k]
        x[k] = [v/pivot for v in x[k]]
        for i in range(n):
            if i != k:
                t = x[i][k]
                x[i] = [a-t*b for a,b in zip(x[i],x[k])]
    return [row[n:] for row in x]
def tensor(a, b):
    return [[Q(a[i//len(b)][j//len(b[0])])*b[i%len(b)][j%len(b[0])]
             for j in range(len(a[0])*len(b[0]))]
            for i in range(len(a)*len(b))]
def h(a):
    x,y,z = a
    return [[Q(z),Q(x,-y)],[Q(x,y),Q(-z)]]
def pair(a,b):
    return add(tensor(h(a),eye(2)),tensor(eye(2),h(b)))
def singlet_expect(a):
    return (a[1][1]+a[2][2]-a[1][2]-a[2][1])/2
def scalar_formula(a,b,z):
    aa,bb = sum(x*x for x in a),sum(x*x for x in b)
    uu = sum((x+y)**2 for x,y in zip(a,b))
    return z*(uu-z*z)/((aa+bb-z*z)*(aa+bb-z*z)-4*aa*bb)



# Exact Laurent fields in q, with arbitrary first K-derivative jets.
ZERO=(0,0,0)
I=Q(0,1)
cs=(F(3,5),F(5,13),F(15,17))
sn=(F(4,5),F(12,13),F(8,17))
sig=[h((1,0,0)),h((0,1,0)),h((0,0,1))]
sig1=[tensor(s,eye(2)) for s in sig]
sig2=[tensor(eye(2),s) for s in sig]
c0={ZERO:[Q(0),Q(1),Q(-1),Q(0)]}  # normalized c=c0/sqrt(2)

def vadd(a,b): return [x+y for x,y in zip(a,b)]
def vscale(a,z): return [Q(z)*x for x in a]
def vzero(v): return all(x==0 for x in v)
def trim(f): return {n:v for n,v in f.items() if not vzero(v)}
def plus(*fields):
    out={}
    for f in fields:
        for n,v in f.items(): out[n]=vadd(out.get(n,[Q()]*4),v)
    return trim(out)
def times(f,z): return trim({n:vscale(v,z) for n,v in f.items()})
def shifted(n,m): return tuple(x+y for x,y in zip(n,m))
def action(M,f):
    out={}
    for m,A in M.items():
        for n,v in f.items():
            w=[sum((A[i][j]*v[j] for j in range(4)),Q()) for i in range(4)]
            z=shifted(n,m)
            out[z]=vadd(out.get(z,[Q()]*4),w)
    return trim(out)
def inner(a,b):
    return sum((sum((x.conj()*y for x,y in zip(v,b.get(n,[Q()]*4))),Q())
                for n,v in a.items()),Q())
def norm2(a): return inner(a,a)
def project(f): return plus(f,times(c0,-inner(c0,f)/2))
def dq(f,a): return times({n:vscale(v,n[a]) for n,v in f.items()},I)
def basis(a,sign=1):
    n=[0,0,0];n[a]=sign;return tuple(n)

H,L,Hp={},[],[]
for a in range(3):
    La,Ha={},{}
    for sign in (-1,1):
        n=basis(a,sign)
        coscoef=Q(F(1,2));sincoef=Q(0,F(-sign,2))
        ac=sn[a]*coscoef+cs[a]*sincoef
        bc=sn[a]*coscoef-cs[a]*sincoef
        H[n]=add(scale(sig1[a],ac),scale(sig2[a],bc))
        La[n]=add(scale(sig1[a],ac),scale(sig2[a],-bc))
        ap=(cs[a]*coscoef-sn[a]*sincoef)/2
        bp=(cs[a]*coscoef+sn[a]*sincoef)/2
        Ha[n]=add(scale(sig1[a],ap),scale(sig2[a],bp))
    L.append(La);Hp.append(Ha)

def D0(f,jet,a):
    return times(plus(action(H,jet),times(action(L[a],dq(f,a)),F(1,2)),
                      action(Hp[a],f)),I)
def HD(f): return project(action(H,project(f)))
def dHD(f,jet,a): return project(plus(action(Hp[a],project(f)),action(H,project(jet))))
def DD(f,jet,a): return project(D0(project(f),project(jet),a))
def antisym(f):
    swap=(0,2,1,3)
    reflected={tuple(-x for x in n):[v[swap[i]] for i in range(4)] for n,v in f.items()}
    return times(plus(f,times(reflected,-1)),F(1,2))
def current_poly(a):
    return {basis(a,sign*2):scale(eye(4),sn[a]*cs[a]) for sign in (-1,1)}
def Fcurrent(f,a):
    hh=action(H,c0);ha=action(Hp[a],c0)
    return times(plus(times(ha,inner(hh,f)),times(hh,inner(ha,f))),F(-1,2))

seeds=[]
for n in (ZERO,(1,0,0),(0,1,-1),(2,-1,0)):
    for j in range(4):
        v=[Q() for _ in range(4)];v[j]=Q(F(j+1,3),F(j-1,5))
        seeds.append(antisym({n:v}))
count=0;witness=None
for a in range(3):
    hh=action(H,c0);ha=action(Hp[a],c0)
    assert inner(c0,hh)==0 and inner(c0,ha)==0
    assert norm2(hh)/2==2*sum(t*t for t in cs)
    assert norm2(ha)/2==sn[a]*sn[a]/2
    for i,f in enumerate(seeds):
        jet=seeds[(i+5)%len(seeds)]
        free=times(plus(action(H,D0(f,jet,a)),times(D0(action(H,f),plus(action(Hp[a],f),action(H,jet)),a),-1)),I)
        assert free==action(current_poly(a),f)
        pp=project(f);jp=project(jet)
        exact=times(plus(HD(DD(pp,jp,a)),times(DD(HD(pp),dHD(pp,jp,a),a),-1)),I)
        compressed=project(action(current_poly(a),pp))
        proposed=plus(compressed,Fcurrent(pp,a))
        assert exact==proposed
        # The K-derivative jet must cancel from the final commutator.
        nojet=times(plus(HD(DD(pp,{},a)),times(DD(HD(pp),dHD(pp,{},a),a),-1)),I)
        assert exact==nojet
        defect=norm2(plus(exact,times(compressed,-1)))
        if defect.x>0 and witness is None: witness=(a,i,defect.x)
        count+=1
assert witness is not None
print('Exact full Laurent convolution and K-jets:',count,'axis/antisymmetric-field cases.')
print('Free original-position commutator equals sin(K_a) cos(2q_a).')
print('Compressed commutator equals PgP - |h_a_prime><h| - |h><h_a_prime|.')
print('All arbitrary K-derivative jets cancel; no Fourier aliasing/truncation used.')
print('Exact omitted-correction witness (axis,seed,squared field norm):',witness)
print('Exact Parseval norms agree with ||h||^2 and ||h_a_prime||^2 in all axes.')
print('Scope: these finite controls test J2-J6; band estimates and time inequalities are analytic checks.')
