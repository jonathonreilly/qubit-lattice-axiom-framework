"""Finite controls for the coherent-packet author draft.
Exact arithmetic reused from the same author's earlier independent checker;
this is not an independent review of the new packet theorem.

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



# Exact sign and normalization for an actual coherent vector in a 2D block.
# Use unnormalized (1,+i), divide its quadratic form by its norm squared 2.
A,B,D=F(7,5),F(3,11),F(2,7)
for lam in (F(1,8),F(1,16),F(1,32),F(1,64)):
    G=Q(lam*A,lam*lam*B);s=G.conj()/G;sig=lam**3*D
    g=[[Q(F(2,3)),Q(sig)],[Q(sig),Q(F(5,4))]]
    S=[[s,Q()],[Q(),Q(1)]]
    difference=add(mul(star(S),mul(g,S)),scale(g,-1))
    for sign in (-1,1):
        chi=[[Q(1)],[Q(0,sign)]]
        change=mul(star(chi),mul(difference,chi))[0][0]/2
        assert change==sign*sig*s.y
        assert change.y==0 and sign*change.x<0
    assert difference[0][0]==0  # pure contact channel has zero change
    leading=F(2)*B*D/A
    scaled= -sig*s.y/lam**4
    assert 0 < scaled <= leading
    assert leading-scaled <= leading*lam*lam*B*B/(A*A)
print('Exact coherent phase sign and unit normalization: +i gives sigma Im(s)<0; -i reverses it.')
print('Pure v is an exact zero-change control; no dissipation inference.')

# Sphere fourth moments by monomial expansion, independently of the
# one-coordinate prolate calculation used in the analytic draft.
L=(F(3,5),F(4,5),F(0))
second=sum(x*x for x in L)/3
fourth=sum(x**4 for x in L)/5
fourth+=sum(F(6,15)*L[i]**2*L[j]**2 for i in range(3) for j in range(i))
assert second==F(1,3) and fourth==F(1,5)
assert fourth-second*second==F(4,45)
Dmin=F(1575,1024)
assert Dmin==F(5,4)**2-F(5,32)**2
print('Exact sphere moment control: Var((L dot n)^2)=4/45 for |L|=1.')
print('Selected domain positive variance lower input D_min=',Dmin)

# Direct radial lattice shells, weighted by their actual coarea/contact mass.
def norm(v): return sqrt(sum(x*x for x in v))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def point(K,E,n,lam):
    k=tuple(x/2 for x in K);lo,hi=E/4,E
    def energy(r):
        return norm([sin(r*n[j]+k[j]) for j in range(3)])+norm([sin(r*n[j]-k[j]) for j in range(3)])
    assert energy(lo)<E<energy(hi)
    for _ in range(50):
        r=(lo+hi)/2
        if energy(r)<E:lo=r
        else:hi=r
    r=(lo+hi)/2
    xp=[r*n[j]+k[j] for j in range(3)];xm=[r*n[j]-k[j] for j in range(3)]
    sp=list(map(sin,xp));sm=list(map(sin,xm));p,m=norm(sp),norm(sm)
    slope=sum(n[j]*(sp[j]*cos(xp[j])/p+sm[j]*cos(xm[j])/m) for j in range(3))
    w=(1+dot(sp,sm)/(p*m))/4
    mass=w*r*r/slope
    y=r*n[0]/lam
    # Stable exact identity for (g-sin K_1)/lambda^3.
    centered=-2*(sin(K[0])/lam)*(sin(r*n[0])/lam)**2
    return mass,y,centered
N=3072
directions=[]
for i in range(N):
    z=1-2*(i+.5)/N;t=2*pi*i/((1+sqrt(5))/2)
    directions.append((sqrt(1-z*z)*cos(t),sqrt(1-z*z)*sin(t),z))
for kap,e in (((.125,0.,0.),1.5),((.125,.015625,.015625),1.5)):
    beta=e*e-dot(kap,kap)+kap[0]**2
    d0=kap[0]*beta/(3*sqrt(5))
    for lam in (1/16,1/32,1/64,1/128):
        rows=[point(tuple(lam*x for x in kap),lam*e,n,lam) for n in directions]
        mass=sum(x[0] for x in rows)
        mean=sum(m*z for m,y,z in rows)/mass
        var=sum(m*(z-mean)**2 for m,y,z in rows)/mass
        d=sqrt(var)
        y2=sum(m*y*y for m,y,z in rows)/mass
        y4=sum(m*y**4 for m,y,z in rows)/mass
        assert d>0 and abs(d-d0)<.08*lam*lam+2e-7
        assert abs(y2-beta/12)<lam*lam
        assert abs(y4-beta*beta/80)<lam*lam
        print('Actual lattice coarea:',kap,'e',e,'lambda',lam,
              'sigma/lambda^3',format(d,'.12g'),'limit',format(d0,'.12g'),
              'mean(y_a^2)',format(y2,'.10g'),'limit',format(beta/12,'.10g'))
# Change-of-variable exponents derived separately as rational arithmetic.
for r in (6,7):
    Aex=F(3,2)-r
    tail=Aex+F(3,2)*(r-1)
    observable=tail+1
    proj=Aex+F(3,2)*r
    Fh=5-2*r+3*r
    Fhp=7-2*r+3*r
    assert tail==F(r,2) and proj==F(r+3,2)
    print('Cook powers r=',r,': contact seminorm',Aex,'state tail',tail,
          'current comparison',observable,'projection',proj,
          'canonical C9 powers',Fh,Fhp)
print('Finite controls completed. Angular quadrature is not interval certified; no PV quadrature used.')
