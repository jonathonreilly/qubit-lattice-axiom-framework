"""External author controls for the supplied hard-core walk; no repo imports.

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


vectors = [(F(1,3),F(-2,5),F(1,7)), (F(3,5),F(4,5),F(0)),
           (F(-1,2),F(1,4),F(2,3)), (F(0),F(0),F(1))]
zs = [Q(F(1,3),F(2,5)),Q(0,F(1,4)),Q(F(-3,2),F(1,7))]
for a,b,z in product(vectors,vectors,zs):
    exact = singlet_expect(inv(add(pair(a,b),scale(eye(4),-z))))
    assert exact == scalar_formula(a,b,z)
print('Exact 4x4 singlet resolvent: 48 Gaussian-rational cases agree.')

# An eight-point, coordinate/shift-symmetric rational sine/cosine measure.
for r in range(4):
    gs,fs,base = Q(),F(0),Q()
    z = Q(F(1,5),F(2,7))
    for sn in product((F(3,5),F(4,5)),repeat=3):
        cs = tuple(F(4,5) if t == F(3,5) else F(3,5) for t in sn)
        a = tuple(cs[j] if j < r else sn[j] for j in range(3))
        b = tuple(cs[j] if j < r else -sn[j] for j in range(3))
        eps2 = sum(t*t for t in a)
        fs += sum(cs[j]**2 for j in range(r))/eps2/8
        gs += scalar_formula(a,b,z)/8
        base += z/(4*sum(t*t for t in sn)-z*z)/8
    assert fs == F(r,3)
    assert gs == -F(r,3)/z+(1-F(r,3))*base
print('Exact total-corner atom: r/3 and full rational resolvent identity, r=0..3.')

# Compression identity in a finite two-node free model, normalized contact.
a,b = vectors[0],vectors[1]
blocks = [pair(a,b),pair(b,a)]
H = [[Q() for _ in range(8)] for _ in range(8)]
for k in range(2):
    for i in range(4):
        for j in range(4): H[4*k+i][4*k+j] = blocks[k][i][j]
u = [[Q(x)] for x in (0,1,-1,0,0,1,-1,0)]
C = scale(mul(u,star(u)),F(1,4))
P = add(eye(8),scale(C,-1))
assert mul(C,mul(H,C)) == scale(C,0)
Hext = mul(P,mul(H,P))
assert Hext == add(H,scale(add(mul(C,H),mul(H,C)),-1))
for z in zs:
    R0 = inv(add(H,scale(eye(8),-z)))
    G = mul(star(u),mul(R0,u))[0][0]/4
    actual = inv(add(Hext,scale(eye(8),-z)))
    proposed = add(add(R0,scale(mul(R0,mul(C,R0)),-1/G)),scale(C,-1/z))
    assert actual == proposed
print('Exact finite compression: rank-two decoupling and extra -C/z resolvent term.')

# Direct finite auxiliary matrix reduction of the primary stationary formula.
G,E = Q(F(2,3),F(1,5)),Q(F(1,7))
B = [[G,1+E*G],[1+E*G,E+E*E*G]]
J = [[Q(),Q(-1)],[Q(-1),Q()]]
T = mul(J,inv(add(eye(2),mul(B,J))))
assert T == [[1/G+E,Q(-1)],[Q(-1),1/E]]
row = [[Q(1),E]]
assert mul(row,mul(T,star(row)))[0][0] == 1/G
print('Exact stationary 2x2 reduction: shell T=1/G; no limiting-coupling argument.')

v = [[Q(F(3,5))],[Q(F(4,5))],[Q()]]
Pv = mul(v,star(v))
g = [[Q((1,3,7)[i] if i == j else 0) for j in range(3)] for i in range(3)]
s = Q(F(3,5),F(4,5))
S = add(eye(3),scale(Pv,s-1))
mu = mul(star(v),mul(g,v))[0][0]
w = add(mul(g,v),scale(v,-mu))
delta = add(mul(star(S),mul(g,S)),scale(g,-1))
expected = add(scale(mul(w,star(v)),s-1),scale(mul(v,star(w)),s.conj()-1))
assert delta == expected
variance = mul(star(w),w)[0][0]
sigma2 = (s-1).abs2()*variance
assert mul(delta,mul(delta,delta)) == scale(delta,sigma2)
assert sum(mul(delta,delta)[i][i] for i in range(3)) == 2*sigma2
assert sigma2.x > 0 and sigma2.y == 0
print('Exact rank-one current identity: squared norm = phase defect squared times variance =',sigma2.x)


def norm(v): return sqrt(sum(x*x for x in v))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def shell_data(K,E,n):
    k = tuple(x/2 for x in K)
    lo,hi = E/4,E
    def data(r):
        xp,xm = [r*n[i]+k[i] for i in range(3)],[r*n[i]-k[i] for i in range(3)]
        sp,sm = list(map(sin,xp)),list(map(sin,xm))
        A,B = norm(sp),norm(sm)
        slope = sum(n[i]*(sp[i]*cos(xp[i])/A+sm[i]*cos(xm[i])/B) for i in range(3))
        weight = (1+dot(sp,sm)/(A*B))/4
        return A+B,slope,weight
    assert data(lo)[0] < E < data(hi)[0]
    for _ in range(52):
        r = (lo+hi)/2
        if data(r)[0] < E: lo = r
        else: hi = r
    r = (lo+hi)/2
    _,slope,weight = data(r)
    assert .5 <= slope <= 2.000000000001 and .25 <= weight <= .500000000001
    return weight*r*r/slope


N = 2048
directions = []
for i in range(N):
    z = 1-2*(i+.5)/N
    a = 2*pi*i/((1+sqrt(5))/2)
    directions.append((sqrt(1-z*z)*cos(a),sqrt(1-z*z)*sin(a),z))
for kap in ((0.,0.,0.),(.2,.1,.05),(0.,0.,.25)):
    rho0 = (1-dot(kap,kap))/(4*pi*pi)
    last = None
    errors = []
    for lam in (1/8,1/16,1/32,1/64):
        K = tuple(lam*x for x in kap)
        rho = 4/pi**2*sum(shell_data(K,lam,n) for n in directions)/N
        assert lam*lam/(32*pi*pi) <= rho <= 4*lam*lam/(pi*pi)
        value = rho/(lam*lam)
        errors.append(abs(value-rho0))
        print('Shell quadrature',kap,'lambda',lam,'rho/lambda^2',format(value,'.12g'),
              'continuum',format(rho0,'.12g'),'absolute difference',format(abs(value-rho0),'.5g'))
        if last is not None:
            assert abs(value-last) < .02*lam*lam
        last = value
    # Finite comparison only: analytic proof does not rely on this tolerance.
    assert errors[-1] < 2e-6

E = 1e-3
q = asin(E/sqrt(2))
a,b = sin(pi/4+q),sin(pi/4-q)
assert abs((a-b)-E) < 1e-14 and min(a,b) > .7
print('Mixed-channel counterexample: E=',E,'individual energies=',a,b,'contact weight=1/2.')
print('All finite controls completed; no PV quadrature or analytic theorem certification claimed.')
