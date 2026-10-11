#!/usr/bin/env python3
"""Finite controls for the supplied excluded walk's scattering-flux form.

The two embedded author programs are preserved verbatim. They use exact
finite algebra and non-certified shell quadrature; the proof note supplies
infinite-dimensional analysis. No analytic theorem or Lean run is inferred
from this Python exit code. Scientific inputs are literal fixtures; the
primary's own bytes are read for integrity, and the cache binds the declared
proof/premise files externally.
"""
from pathlib import Path
from hashlib import sha256
from time import perf_counter
import sys
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/EXCLUDED_WALK_SCATTERING_FLUX_TRANSPORT_FORM_BOUNDED_THEOREM_NOTE_2026-10-11.md',
    'docs/EXCLUDED_WALK_LOW_ENERGY_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md',
    'formalization/excluded_walk_rank_one/RankOneScattering.lean',
]
_started = perf_counter()
_source = Path(__file__).read_bytes()
print('Supplied excluded-walk flux/form finite controls; analytical and formal scopes remain separate.')
print('AUDIT_TIMEOUT_SEC='+str(AUDIT_TIMEOUT_SEC))

# BEGIN VERBATIM FLUX AUTHOR CONTROLS
"""Author controls for the excluded-walk flux bridge.

Exact finite-torus current identities, exact eight-channel unitarity, and
matrix-based lattice shell/parity controls. No repository runner imports.
The finite examples do not prove stationary phase, a limiting absorption
principle, or any uniform principal-value remainder.
"""
from fractions import Fraction as F
from itertools import product
from math import sin, cos, sqrt, pi


class Q:
    def __init__(self, x=0, y=0):
        if isinstance(x, Q): self.x, self.y = x.x, x.y
        else: self.x, self.y = F(x), F(y)
    def __add__(self, other):
        o=Q(other); return Q(self.x+o.x,self.y+o.y)
    __radd__=__add__
    def __neg__(self): return Q(-self.x,-self.y)
    def __sub__(self, o): return self+-Q(o)
    def __rsub__(self, o): return Q(o)+-self
    def __mul__(self, other):
        o=Q(other); return Q(self.x*o.x-self.y*o.y,self.x*o.y+self.y*o.x)
    __rmul__=__mul__
    def conj(self): return Q(self.x,-self.y)
    def abs2(self): return self.x*self.x+self.y*self.y
    def __truediv__(self, other):
        o=Q(other); z=self*o.conj(); return Q(z.x/o.abs2(),z.y/o.abs2())
    def __eq__(self, other):
        o=Q(other); return (self.x,self.y)==(o.x,o.y)


# K=0: in the orthonormal (c,sigma_1 c,sigma_2 c,sigma_3 c) basis,
# H(q) connects c to triplet j with matrix element 2 sin(q_j).
sites=list(product(range(4),repeat=3)); z=Q(F(3,5),F(2,7))
powers=[Q(1),Q(0,1),Q(-1),Q(0,-1)]; sins=[0,1,0,-1]
fourier={}
for k in sites:
    s=[sins[i] for i in k]; den=Q(4*sum(t*t for t in s))-z*z
    fourier[k]=[z/den]+[Q(2*t)/den for t in s]
psi={x:[sum((powers[sum(a*b for a,b in zip(k,x))%4]*fourier[k][j]
             for k in sites),Q())/64 for j in range(4)] for x in sites}


def shift(x,j,sign=1):
    y=list(x); y[j]=(y[j]+sign)%4; return tuple(y)


def bond(x,j):
    a,b=psi[x],psi[shift(x,j)]
    return 2*(a[0].conj()*b[j+1]+a[j+1].conj()*b[0]).x


G=psi[(0,0,0)][0]; total_norm=sum(sum(a.abs2() for a in v) for v in psi.values())
assert G.y==z.y*total_norm
for x in sites:
    div=sum(bond(x,j)-bond(shift(x,j,-1),j) for j in range(3))
    rhs=(2*G.y if x==(0,0,0) else F(0))-2*z.y*sum(a.abs2() for a in psi[x])
    assert div==rhs
    odd=[j for j in range(3) if x[j]%2]
    allowed=[0] if not odd else [odd[0]+1] if len(odd)==1 else []
    assert all(a==0 for j,a in enumerate(psi[x]) if j not in allowed)
inside={x for x in sites if all(t in (0,1,3) for t in x)}
outflux=F(0)
for x in inside:
    for j in range(3):
        if shift(x,j) not in inside:outflux+=bond(x,j)
        if shift(x,j,-1) not in inside:outflux-=bond(shift(x,j,-1),j)
assert outflux==2*G.y-2*z.y*sum(sum(a.abs2() for a in psi[x]) for x in inside)
assert outflux>0
print('Exact 4^3 torus: 64 local continuity identities, resolvent absorption identity and all parity zeros verified.')
print('Exact finite-box outward flux:',outflux)

# Exact normalized eight-corner beam. These are genuine unit vectors in C^8,
# not delta-direction states normalized by decree.
phase=Q(F(3,5),F(-4,5)); shift_amp=(phase-1)/8
out=[(Q(1) if j==0 else Q())+shift_amp for j in range(8)]
assert sum(a.abs2() for a in out)==1
assert sum(a.abs2() for a in out[1:])==F(7,64)*(phase-1).abs2()
assert sum(a.abs2() for a in out[1:])==F(7,80)
print('Exact normalized corner beam: other-corner probability 7/80; total outgoing probability 1.')

# In the singlet/triplet basis the K=0 antisymmetric incident field is
# cos(q.x)c+i sin(q.x)t_n, of pointwise norm one and contact amplitude one.
n=(F(3,5),F(4,5),F(0)); cs,sn=F(5,13),F(12,13)
assert cs*cs+sum(sn*sn*t*t for t in n)==1
assert F(2)*F(1,2)==1  # paired contact intensity versus one unit ordered wave
print('Exact paired incident normalization: density 1 and contact intensity 1; ordered single-wave contact intensity 1/2.')

# Matrix controls below use the original tensor-product spin representation.
I=[[1.,0.],[0.,1.]]
pauli=[[[0.,1.],[1.,0.]],[[0.,-1j],[1j,0.]],[[1.,0.],[0.,-1.]]]


def tensor(a,b):
    return [[a[i//2][j//2]*b[i%2][j%2] for j in range(4)] for i in range(4)]


s1=[tensor(s,I) for s in pauli]; s2=[tensor(I,s) for s in pauli]
c=[0.,1/sqrt(2),-1/sqrt(2),0.]


def matvec(a,b): return [sum(x*y for x,y in zip(row,b)) for row in a]
def inner(a,b): return sum(complex(x).conjugate()*y for x,y in zip(a,b))
def norm(a): return sqrt(sum(abs(x)**2 for x in a))
def dot(a,b): return sum(x*y for x,y in zip(a,b))


def projector(s):
    e=norm(s)
    return [[((1 if i==j else 0)+sum(s[k]*pauli[k][i][j]/e for k in range(3)))/2
             for j in range(2)] for i in range(2)]


def adjugate(a):
    result=[]
    for i in range(3):
        row=[]
        for j in range(3):
            rr=[k for k in range(3) if k!=j];cc=[k for k in range(3) if k!=i]
            row.append((-1)**(i+j)*(a[rr[0]][cc[0]]*a[rr[1]][cc[1]]-a[rr[0]][cc[1]]*a[rr[1]][cc[0]]))
        result.append(row)
    return result


def shell(K,E,radial):
    lo,hi=E/4,E
    def details(r):
        q=[r*t for t in radial]
        ap=[K[j]/2+q[j] for j in range(3)]; am=[K[j]/2-q[j] for j in range(3)]
        sp,sm=list(map(sin,ap)),list(map(sin,am));ep,em=norm(sp),norm(sm)
        return q,ap,am,sp,sm,ep,em
    for _ in range(55):
        mid=(lo+hi)/2;*_,ep,em=details(mid)
        if ep+em<E:lo=mid
        else:hi=mid
    q,ap,am,sp,sm,ep,em=details((lo+hi)/2)
    vp=[sp[j]*cos(ap[j])/ep-sm[j]*cos(am[j])/em for j in range(3)]
    Hess=[[(cos(2*ap[i])/ep+cos(2*am[i])/em if i==j else 0)
            -sp[i]*cos(ap[i])*sp[j]*cos(ap[j])/ep**3
            -sm[i]*cos(am[i])*sm[j]*cos(am[j])/em**3 for j in range(3)] for i in range(3)]
    speed=norm(vp);normal=[x/speed for x in vp]
    curvature=dot(vp,matvec(adjugate(Hess),vp))/speed**4
    assert curvature>0
    return q,sp,sm,speed,normal,curvature


corners=list(product((0,1),repeat=3)); worst_matrix=0.; worst_limit=0.
radials=[(1.,0.,0.),(0.,1.,0.),(1/sqrt(3),)*3,(3/5,4/5,0.)]
for kap in ((0.,0.,0.),(.125,.015625,.015625)):
    e=1.5;D=e*e-dot(kap,kap)
    for lam in (1/16,1/32,1/64):
        max_low_error=0.
        for radial in radials:
            K=[lam*x for x in kap];E=lam*e
            q,sp,sm,speed,normal,curv=shell(K,E,radial)
            amp=[]
            for C in corners:
                signs=[(-1)**t for t in C]
                Pc=matvec(tensor(projector([a*b for a,b in zip(signs,sp)]),
                                      projector([a*b for a,b in zip(signs,sm)])),c)
                amp.append([x/(2*pi*speed*sqrt(curv)) for x in Pc])
            fields=[[sum((-1)**dot(C,p)*amp[i][j] for i,C in enumerate(corners))
                     for j in range(4)] for p in corners]
            bonds=[]
            for a in range(3):
                hopping=[[(sin(K[a]/2)*(s1[a][i][j]+s2[a][i][j])
                            -1j*cos(K[a]/2)*(s1[a][i][j]-s2[a][i][j]))/2
                           for j in range(4)] for i in range(4)]
                total=0.
                for ix,p in enumerate(corners):
                    pp=list(p);pp[a]^=1;iy=corners.index(tuple(pp))
                    phase=complex(cos(q[a]),sin(q[a]))
                    total+=-2*inner(fields[ix],matvec(hopping,[phase*x for x in fields[iy]])).imag/8
                bonds.append(total)
            expected=[normal[a]*speed*sum(norm(x)**2 for x in amp) for a in range(3)]
            error=norm([a-b for a,b in zip(bonds,expected)])/max(norm(expected),1e-30)
            worst_matrix=max(worst_matrix,error);assert error<2e-13
            w=(1-dot(sp,sm)/(norm(sp)*norm(sm)))/4
            Factual=2*w/(pi*pi*speed*curv)
            assert abs(norm(expected)-Factual)<1e-12*Factual
            gamma=D+dot(kap,normal)**2
            Flimit=D*D*e/(8*pi*pi*gamma**1.5)
            lowerror=abs(Factual/lam**2-Flimit)
            max_low_error=max(max_low_error,lowerror)
            assert lowerror<.2*lam**2
            if not any(kap):
                for p,field in zip(corners,fields):
                    if sum(p)>=2:assert norm(field)<1e-13
        worst_limit=max(worst_limit,max_low_error)
        print('Actual lattice shell/parity current:',kap,'lambda',lam,
              'max scaled angular-flux error',format(max_low_error,'.9g'))
print('Eight-corner matrix current relative error:',format(worst_matrix,'.6g'))

# Analytic limiting angular-flux normalization checked by a separate radial
# one-dimensional Simpson quadrature, with its axis aligned with kappa.
for e,k in ((1.5,0.),(1.5,.2),(1.25,.25)):
    D=e*e-k*k;N=4096;dt=2/N
    values=[(D+k*k*(-1+i*dt)**2)**(-1.5) for i in range(N+1)]
    integ=dt/3*(values[0]+values[-1]+4*sum(values[1:-1:2])+2*sum(values[2:-1:2]))
    assert abs(integ-2/(D*e))<2e-12
    flux=D*D*e/(8*pi*pi)*(2*pi*integ)
    assert abs(flux-D/(2*pi))<2e-12
print('Limiting ellipsoid angular-flux integral equals 2pi r0 for three parameter pairs.')
print('Controls complete. Fixed finite identities and non-certified floating geometry; no PV or stationary-phase proof by numerics.')
# END VERBATIM FLUX AUTHOR CONTROLS

# BEGIN VERBATIM TRANSPORT FORM AUTHOR CONTROLS
"""Author controls for the excluded-walk scattering-flux transport form.

Exact weighted finite-space algebra and exact uniform-sphere polynomial moments,
then non-certified quadrature of the actual lattice coarea measure. These are
finite controls, not an independent review or a proof of the threshold input.
Only the Python standard library is used; no repository runner is imported.
"""
from fractions import Fraction as F
from itertools import combinations
from math import sin, cos, sqrt, pi


class Q:
    def __init__(self, a=0, b=0):
        if isinstance(a, Q): self.a,self.b=a.a,a.b
        else: self.a,self.b=F(a),F(b)
    def __add__(self, x):
        x=Q(x);return Q(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return Q(-self.a,-self.b)
    def __sub__(self,x):return self+-Q(x)
    def __rsub__(self,x):return Q(x)+-self
    def __mul__(self,x):
        x=Q(x);return Q(self.a*x.a-self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def conj(self):return Q(self.a,-self.b)
    def abs2(self):return self.a*self.a+self.b*self.b
    def __eq__(self,x):
        x=Q(x);return self.a==x.a and self.b==x.b


def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def adj(a):return [[Q(a[j][i]).conj() for j in range(len(a))] for i in range(len(a[0]))]
def mv(a,x):return [sum(y*z for y,z in zip(row,x)) for row in a]
def inner(x,y):return sum(Q(a).conj()*b for a,b in zip(x,y))


# A deliberately nonuniform finite measure: nu_j=v_j^2 but mu_j=rho*nu_j/w_j.
# The atoms are exchange orbits, not a claim of unequal corner masses.
v=[F(1,6),F(1,6),F(1,3),F(1,3),F(1,3),F(1,3),F(1,2),F(1,2)]
w=[F(1,4),F(2,7),F(1,3),F(3,8),F(2,5),F(3,7),F(4,9),F(1,2)]
rho=F(7,10);nu=[x*x for x in v];mu=[rho*p/a for p,a in zip(nu,w)]
assert sum(nu)==1 and sum(a*b for a,b in zip(mu,w))==rho
s=Q(F(3,5),F(-4,5));phase2=(s-1).abs2();N=len(v)
S=[[Q(i==j)+(s-1)*v[i]*v[j] for j in range(N)] for i in range(N)]
assert mm(adj(S),S)==[[Q(i==j) for j in range(N)] for i in range(N)]
f=[F(0),F(1),F(-1),F(2),F(3,2),F(-2,3),F(5,7),F(3)]
g=[F(1),F(1),F(0),F(-2),F(1,5),F(1,3),F(-3,4),F(2)]


def covariance(a,b):
    return sum(p*x*y for p,x,y in zip(nu,a,b))-sum(p*x for p,x in zip(nu,a))*sum(p*y for p,y in zip(nu,b))


def delta(a):
    M=[[Q(a[i]) if i==j else Q() for j in range(N)] for i in range(N)]
    T=mm(mm(adj(S),M),S)
    return [[T[i][j]-M[i][j] for j in range(N)] for i in range(N)]


# Absorb the sole irrational constant: pi*Q = |s-1|^2 Var_nu.
# This corresponds to G=pi*rho*(2+i), so Im(G)=pi*rho exactly.
qpi=sum(mu[i]*mu[j]*phase2*w[i]*w[j]/rho**2*(f[j]-f[i])**2
        for i in range(N) for j in range(N))/2
assert qpi==phase2*covariance(f,f)>0
Df,Dg=delta(f),delta(g);Df2=mm(Df,Df);Df3=mm(Df2,Df)
assert Df3==[[qpi*x for x in row] for row in Df]
assert sum(Df2[i][i] for i in range(N))==2*qpi
assert sum(mm(Df,Dg)[i][i] for i in range(N))==2*phase2*covariance(f,g)
mean_mu=sum(a*b for a,b in zip(mu,f))/sum(mu)
distance=sum(a*(b-mean_mu)**2 for a,b in zip(mu,f))
assert phase2*min(w)/rho*distance<=qpi<=phase2*max(w)/rho*distance
# Positive form does not imply a change for every coherent state.
dark=[v[1],-v[0]]+[F(0)]*(N-2)
assert inner(v,dark)==0 and mv(S,dark)==[Q(x) for x in dark]
assert inner(dark,mv(Df,dark))==0 and inner(v,mv(Df,v))==0
# Halving the paired incident contact intensity halves the resulting form.
assert qpi/2!=qpi and qpi==F(2)*(qpi/2)
print('Exact nonuniform eight-atom form: pi Q = operator norm squared; HS polarization and coercivity verified.')
print('pi Q witness:',qpi,'; dark and pure-contact states both have zero expectation change.')


# Direct exact polynomial integration over a uniform unit sphere, rather than
# evaluating the covariance formula under test. Monomials have multi-indices.
def mulpoly(a,b):
    out={}
    for x,c in a.items():
        for y,d in b.items():
            z=tuple(i+j for i,j in zip(x,y));out[z]=out.get(z,F(0))+c*d
    return out


def odd_factorial(n):
    x=1
    for j in range(1,n+1,2):x*=j
    return x


def sphere(poly):
    total=F(0)
    for powers,c in poly.items():
        if any(x%2 for x in powers):continue
        total+=c*F(odd_factorial(powers[0]-1)*odd_factorial(powers[1]-1)*odd_factorial(powers[2]-1),odd_factorial(sum(powers)+1))
    return total


def matrix_rank(a):
    a=[row[:] for row in a];r=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][col]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];p=a[r][col];a[r]=[x/p for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                p=a[i][col];a[i]=[x-p*y for x,y in zip(a[i],a[r])]
        r+=1
    return r


def det(a):
    if len(a)==1:return a[0][0]
    return sum((-1)**j*a[0][j]*det([[a[i][k] for k in range(len(a)) if k!=j] for i in range(1,len(a))]) for j in range(len(a)))


def covariance_formula(k,e):
    D=e*e-sum(x*x for x in k);B=[[(D*(i==j)+k[i]*k[j])/4 for j in range(3)] for i in range(3)]
    return [[F(8,45)*k[i]*k[j]*(3*B[i][j]**2-B[i][i]*B[j][j]) for j in range(3)] for i in range(3)]


e=F(65,64);d=F(63,64)
ks=[(F(0),)*3,(F(1,4),F(0),F(0)),(F(3,20),F(1,5),F(0)),(F(1,12),F(1,6),F(1,6)),(F(-1,12),F(1,6),F(-1,6))]
for k in ks:
    kk=sum(x*x for x in k);dd=e if not kk else d
    assert dd*dd==e*e-kk
    T=[[(dd*(i==j)+(e-dd)*k[i]*k[j]/kk if kk else e*(i==j))/2 for j in range(3)] for i in range(3)]
    gamma=[]
    for i in range(3):
        row={tuple(int(j==a) for j in range(3)):T[i][a] for a in range(3)}
        gamma.append({p:-2*k[i]*c for p,c in mulpoly(row,row).items()})
    exact=[[sphere(mulpoly(gamma[i],gamma[j]))-sphere(gamma[i])*sphere(gamma[j]) for j in range(3)] for i in range(3)]
    wanted=covariance_formula(k,e)
    assert exact==wanted
    active=[i for i,x in enumerate(k) if x]
    assert matrix_rank(exact)==len(active)
    for n in (1,2,3):
        for indices in combinations(range(3),n):assert det([[exact[i][j] for j in indices] for i in indices])>=0
    if active:
        D=dd*dd
        Binv=[[(F(4)/D)*((i==j)-k[i]*k[j]/e**2) for j in range(3)] for i in range(3)]
        Bnorm=sum(x*x for row in Binv for x in row)
        eta=1-sum(Binv[i][i]**2 for i in active)/Bnorm
        assert eta>0
        lower=[[exact[i][j]-(D*D*eta/F(30)*k[i]**2 if i==j else 0) for j in range(3)] for i in range(3)]
        upper=[[(e**4/F(30)*k[i]**2 if i==j else 0)-exact[i][j] for j in range(3)] for i in range(3)]
        for mat in (lower,upper):
            for n in (1,2,3):
                for indices in combinations(range(3),n):assert det([[mat[i][j] for j in indices] for i in indices])>=0
    print('Exact sphere polynomial covariance: kappa',tuple(map(str,k)),'rank',matrix_rank(exact))
print('Exact tensor off-diagonal moments, active rank and explicit quadratic bounds verified in five rational geometries.')


# Actual lattice coarea moments, using radial shell coordinates, quadrature,
# and the original sine dispersion. This does not approximate a principal value.
def gauss_legendre(n):
    out=[]
    for i in range(1,n+1):
        x=cos(pi*(i-.25)/(n+.5))
        for _ in range(30):
            p0,p1=1.,x
            for j in range(2,n+1):p0,p1=p1,((2*j-1)*x*p1-(j-1)*p0)/j
            derivative=n*(x*p1-p0)/(x*x-1)
            step=p1/derivative;x-=step
            if abs(step)<1e-15:break
        out.append((x,2/((1-x*x)*derivative**2)))
    return out


def lattice_moments(k,e,lam,order):
    mu_mass=rho_mass=0.;first=[0.]*3;second=[[0.]*3 for _ in range(3)]
    nphi=2*order
    for z,weight in gauss_legendre(order):
        rr=sqrt(1-z*z)
        for j in range(nphi):
            phi=2*pi*(j+.5)/nphi;n=(rr*cos(phi),rr*sin(phi),z)
            lo,hi=e/4,e
            for _ in range(50):
                R=(lo+hi)/2
                sp=[sin(lam*(k[i]/2+R*n[i])) for i in range(3)]
                sm=[sin(lam*(k[i]/2-R*n[i])) for i in range(3)]
                ep=sqrt(sum(x*x for x in sp));em=sqrt(sum(x*x for x in sm))
                if (ep+em)/lam<e:lo=R
                else:hi=R
            R=(lo+hi)/2;q=[lam*R*x for x in n]
            ap=[lam*k[i]/2+q[i] for i in range(3)];am=[lam*k[i]/2-q[i] for i in range(3)]
            sp,sm=list(map(sin,ap)),list(map(sin,am));ep=sqrt(sum(x*x for x in sp));em=sqrt(sum(x*x for x in sm))
            derivative=sum(n[i]*(sp[i]*cos(ap[i])/ep-sm[i]*cos(am[i])/em) for i in range(3))
            assert derivative>.5
            w=(1-sum(a*b for a,b in zip(sp,sm))/(ep*em))/4
            assert .25<w<.500000000001
            # All eight equal corner masses retained here. Divide by lambda^2
            # before accumulation so the threshold moment limit is stable.
            dm=8*R*R/derivative*weight*(2*pi/nphi)/(2*pi)**3
            mu_mass+=dm;rho_mass+=w*dm
            gam=[-2*(sin(lam*k[i])/lam)*(sin(q[i])/lam)**2 for i in range(3)]
            for a in range(3):
                first[a]+=w*dm*gam[a]
                for b in range(3):second[a][b]+=w*dm*gam[a]*gam[b]
    cov=[[second[a][b]/rho_mass-first[a]*first[b]/rho_mass**2 for b in range(3)] for a in range(3)]
    return mu_mass,rho_mass,cov


cases=[((.25,0.,0.),65/64),((1/12,1/6,1/6),65/64),((0.,0.,0.),1.5)]
for k,e in cases:
    D=e*e-sum(x*x for x in k);r0=D/(4*pi*pi);m0=(e*e-sum(x*x for x in k)/3)/(2*pi*pi)
    target=covariance_formula(k,e)
    for lam in (1/16,1/32,1/64):
        coarse=lattice_moments(k,e,lam,12);fine=lattice_moments(k,e,lam,24)
        quad=max([abs(coarse[0]-fine[0]),abs(coarse[1]-fine[1])]+[abs(coarse[2][i][j]-fine[2][i][j]) for i in range(3) for j in range(3)])
        error=max([abs(fine[0]-m0),abs(fine[1]-r0)]+[abs(fine[2][i][j]-float(target[i][j])) for i in range(3) for j in range(3)])
        assert quad<2e-10
        assert error<.15*lam*lam
        if not any(k):assert all(x==0 for row in fine[2] for x in row)
        print('Actual lattice moments:',k,'lambda',lam,'limit error',format(error,'.9g'),'quadrature difference',format(quad,'.4g'))
print('Controls complete: exact algebra and moments; floating lattice quadrature is not interval certified and does not prove the uniform threshold theorem.')
# END VERBATIM TRANSPORT FORM AUTHOR CONTROLS

assert _source == Path(__file__).read_bytes()
print('All finite controls completed; no continuum or kinetic conclusion follows from the finite checks alone.')
print('runtime_seconds=%.6f'%(perf_counter()-_started))
print('python='+sys.version.split()[0]+'; dependencies=Python standard library only')
print('script_sha256='+sha256(_source).hexdigest())
