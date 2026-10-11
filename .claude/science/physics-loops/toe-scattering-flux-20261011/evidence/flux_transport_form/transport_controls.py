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
