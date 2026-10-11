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
