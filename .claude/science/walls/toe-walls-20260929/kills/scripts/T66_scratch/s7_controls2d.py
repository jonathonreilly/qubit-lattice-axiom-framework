import random
from model2 import *
# CONTROL 1 (2D): degree-1 bracket equals G1[xi0]
def deg1(c=CC, timing_ok=True):
    return fadd(bracket(C1('N'), T2('M', c=c)), bracket(T2('N', c=c), C1('M')))
xx, yy = xi0_xy()
g = G1_of_xi(xx, yy)
for c in (F(1,2), F(0), F(1,3)):
    d = fadd(deg1(c), g, F(-1))
    print("2D degree-1: c=",c,"residual monomials:",len(d))
# CONTROL 2: gauge invariance of the assembled real-space R2 (linear gauge variation A(xi)) on a torus
L=6
random.seed(5)
def rnd(): return F(random.randint(-5,5), random.randint(1,4))
h={ (c,i,j): rnd() for c in (XX,YY,ZZ,XY) for i in range(L) for j in range(L)}
xi={ (d,i,j): rnd() for d in ('x','y') for i in range(L) for j in range(L)}
def Afield(xi):
    def g_(d,i,j): return xi[(d,i%L,j%L)]
    out={}
    for i in range(L):
        for j in range(L):
            out[(XX,i,j)]=2*(g_('x',i,j)-g_('x',i-1,j))
            out[(YY,i,j)]=2*(g_('y',i,j)-g_('y',i,j-1))
            out[(ZZ,i,j)]=F(0)
            out[(XY,i,j)]=g_('y',i+1,j)-g_('y',i,j)+g_('x',i,j+1)-g_('x',i,j)
    return out
def cell_of(v):
    c,p=v[1],v[2]
    if c==XY: return (c,((p[0]-1)//2)%L,((p[1]-1)//2)%L)
    return (c,(p[0]//2)%L,(p[1]//2)%L)
def evalfun(fun, field):
    tot=F(0)
    for mono,cf in fun.items():
        for si in range(L):
            for sj in range(L):
                val=cf
                for v in mono:
                    c,p=v[1],v[2]
                    key=cell_of((v[0],c,(p[0]+2*si,p[1]+2*sj)))
                    val*=field[key]
                tot+=val
    return tot
R2=R2_2D()
A=Afield(xi)
hA={k:h[k]+A[k] for k in h}
print("R2(h)      =",evalfun(R2,h))
print("R2(h+A xi) =",evalfun(R2,hA))
print("R2 gauge-invariant:",evalfun(R2,h)==evalfun(R2,hA))
# also check: R2 is not trivially zero and not invariant under a random non-gauge shift
h2={k:h[k]+rnd() for k in h}
print("R2(random shift) =",evalfun(R2,h2))

# CONTROL 2b: planar reduction of the 2D R2 equals the 1D S1 formula (1/2) sum (D h_yy)(D h_zz)
hx1={(c,i,j): (rnd() if False else None) for c in (XX,YY,ZZ,XY) for i in range(L) for j in range(L)}
prof={c:[rnd() for _ in range(L)] for c in (XX,YY,ZZ,XY)}
hp={(c,i,j):(prof[c][i] if c!=XY else F(0)) for c in (XX,YY,ZZ,XY) for i in range(L) for j in range(L)}
v2d=evalfun(R2,hp)/L   # divide by L (translations in y)
v1d=sum(F(1,2)*(prof[YY][(i+1)%L]-prof[YY][i])*(prof[ZZ][(i+1)%L]-prof[ZZ][i]) for i in range(L))
print("planar reduction: 2D R2 / L =",v2d," 1D formula =",v1d," equal:",v2d==v1d)
