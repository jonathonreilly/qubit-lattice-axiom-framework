#!/usr/bin/env python3
"""Finite controls for the supplied excluded walk's low-energy current theorem.

Exact Gaussian-rational algebra tests the contact resolvent, rank-two
compression, stationary matrix reduction, current variance and canonical
placement commutator. Finite shell quadrature checks normalizations/scaling;
it does not prove limiting absorption, PV bounds or scattering existence.
The analytical note proves those estimates and the finite-time comparisons.
This author primary incorporates previously separate exact/shell and Laurent
controls; the preserved selective reviews record their original provenance.
No external data, repository science imports or stochastic sampling are used.
"""
from pathlib import Path
from hashlib import sha256
from time import perf_counter
import sys

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/EXCLUDED_WALK_LOW_ENERGY_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md',
    'docs/ADMISSIBILITY_RULE_UNDER_ONE_RECORD_PER_SITE_A_COLLISION_CHANGES_THE_RECORDS_TWO_STEP_MOMENTUM_ONLY_AT_THIRD_ORDER_IN_THEIR_OFFSETS_FROM_THE_CONES_BOUNDED_THEOREM_NOTE_2026-09-26.md',
]
started = perf_counter()
source = Path(__file__).read_bytes()
print('Supplied excluded-walk finite controls; no claim of infinite-volume certification')
print('AUDIT_TIMEOUT_SEC='+str(AUDIT_TIMEOUT_SEC))
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
    assert exact == scalar_formula(a,b,z), 'singlet resolvent from exact matrix inverse'
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
    assert fs == F(r,3), 'total-corner contact atom'
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
    assert actual == proposed, 'compressed resolvent including auxiliary contact eigenstate'
print('Exact finite compression: rank-two decoupling and extra -C/z resolvent term.')

# Direct finite auxiliary matrix reduction of the primary stationary formula.
G,E = Q(F(2,3),F(1,5)),Q(F(1,7))
B = [[G,1+E*G],[1+E*G,E+E*E*G]]
J = [[Q(),Q(-1)],[Q(-1),Q()]]
T = mul(J,inv(add(eye(2),mul(B,J))))
assert T == [[1/G+E,Q(-1)],[Q(-1),1/E]]
row = [[Q(1),E]]
assert mul(row,mul(T,star(row)))[0][0] == 1/G, 'stationary on-shell auxiliary-matrix reduction'
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
assert delta == expected, 'coherent current change adjoints'
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
    assert errors[-1] < 2e-6, 'eight-cone spectral-density normalization'

E = 1e-3
q = asin(E/sqrt(2))
a,b = sin(pi/4+q),sin(pi/4-q)
assert abs((a-b)-E) < 1e-14 and min(a,b) > .7
print('Mixed-channel counterexample: E=',E,'individual energies=',a,b,'contact weight=1/2.')
print('All finite controls completed; no PV quadrature or analytic theorem certification claimed.')

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

Hdiff={n:M for La in L for n,M in La.items()}

def D0(f,jet,a):
    return times(plus(action(H,jet),times(action(Hdiff,dq(f,a)),F(1,2)),
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
        assert free==action(current_poly(a),f), 'original-position free-current identity'
        pp=project(f);jp=project(jet)
        exact=times(plus(HD(DD(pp,jp,a)),times(DD(HD(pp),dHD(pp,jp,a),a),-1)),I)
        compressed=project(action(current_poly(a),pp))
        proposed=plus(compressed,Fcurrent(pp,a))
        assert exact==proposed, 'canonical finite-rank correction sign and coefficient'
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


# Nonzero coherent-current discriminator: choose an actual orthogonal channel.
# The omitted 1/sqrt(2) in chi is accounted for in its quadratic form below.
v = [[Q(F(3,5))],[Q(F(4,5))],[Q()]]
u = [[Q(F(-4,5))],[Q(F(3,5))],[Q()]]
g = [[Q((1,3,7)[i] if i == j else 0) for j in range(3)] for i in range(3)]
s = Q(F(3,5),F(4,5))
Sc = add(eye(3),scale(mul(v,star(v)),s-1))
mu = mul(star(v),mul(g,v))[0][0]
w = add(mul(g,v),scale(v,-mu))
sigma = F(24,25)
assert w == scale(u,sigma)
chi = add(v,scale(u,Q(0,1)))
delta_g = add(mul(star(Sc),mul(g,Sc)),scale(g,-1))
change = mul(star(chi),mul(delta_g,chi))[0][0]/2
assert change == sigma*s.y and change == F(96,125), 'nonzero coherent packet current change'
chi_opposite = add(v,scale(u,Q(0,-1)))
assert mul(star(chi_opposite),mul(delta_g,chi_opposite))[0][0]/2 == -change
assert mul(star(v),mul(delta_g,v))[0][0] == 0
print('Exact coherent packet: opposite phases reverse the nonzero current change; contact-aligned change is zero.')

# Independent monomial integration of the continuum ellipsoid moments.
# Uniform sphere moments are integrated from their elementary factorial rule;
# no value from the note's target variance is used to build the polynomials.
def odd_double_factorial(n):
    answer=1
    for k in range(1,n+1,2): answer*=k
    return answer

def sphere_moment(indices):
    if any(k%2 for k in indices): return F(0)
    value=F(1,odd_double_factorial(sum(indices)+1))
    for k in indices: value*=odd_double_factorial(k-1)
    return value

def linear_power_moment(row,power):
    result=F(0)
    for indices in product(range(3),repeat=power):
        monomial=[0,0,0];coefficient=F(1)
        for j in indices:monomial[j]+=1;coefficient*=row[j]
        result+=coefficient*sphere_moment(monomial)
    return result

for row in [(F(1,2),F(0),F(0)),(F(3,5),F(4,5),F(0)),(F(2,7),F(-4,9),F(8,11))]:
    squared=sum(x*x for x in row)
    mean=linear_power_moment(row,2)
    variance=linear_power_moment(row,4)-mean*mean
    assert mean==squared/3 and variance==4*squared*squared/45, 'continuum angular second and fourth moments'
    # For a row of T, squared=(e^2-|kappa|^2+kappa_a^2)/4.
    axis_parameter=4*squared
    assert variance==axis_parameter*axis_parameter/180
print('Exact continuum angular second/fourth moments give the nonzero coherent-current coefficient.')

# Whole-line integration-by-parts tails and joint scales. These exact powers
# are finite controls only; packet smoothness and both outgoing form-factor
# premises must be established by the analytical proof.
for r in (2,3,7):
    for T in (F(1,2),F(2),F(7,3)):
        tail=1/(F(r-1)*T**(r-1))
        assert -F(r-1)*tail/T==-T**(-r), 'integrated Cook tail denominator'
        assert tail>0
r=7;time_power=F(3,2)
contact_density_L1_derivative=F(3,2)-r
state_error_power=contact_density_L1_derivative+time_power*(r-1)
preparation_power=contact_density_L1_derivative+time_power*r
current_error_power=1+state_error_power
form_factor_power=min(2*(F(5,2)-r),2*(F(7,2)-r))+2*r*time_power
assert state_error_power==F(7,2) and preparation_power==F(5), 'finite-time coherent packet separation powers'
assert current_error_power==F(9,2) and current_error_power>4
assert form_factor_power==12
assert 1+(F(3,2)-6)+time_power*5==4  # r=6 does not separate the leading coefficient
print('Exact tail and scale controls: r=7, T=lambda^(-3/2) give state O(lambda^(7/2)), current O(lambda^(9/2)), correction O(lambda^12).')

assert source == Path(__file__).read_bytes()
print('All finite controls completed; analytic proof and scoped review supply the infinite-dimensional conclusions.')
print('runtime_seconds=%.6f'%(perf_counter()-started))
print('python='+sys.version.split()[0]+'; dependencies=Python standard library only; inputs=literal fixtures and own provenance bytes')
print('script_sha256='+sha256(source).hexdigest())
