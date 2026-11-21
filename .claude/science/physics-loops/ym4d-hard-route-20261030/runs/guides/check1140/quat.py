# Guide only: quaternion identities used in S1, S2, S8.
import math, random
def mul(p,q):
    a1,b1,c1,d1=p; a2,b2,c2,d2=q
    return (a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2, a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2)
def conj(q): return (q[0],-q[1],-q[2],-q[3])
def dot(p,q): return sum(x*y for x,y in zip(p,q))
def Ad(g,q): return mul(mul(g,q),conj(g))
s=1/math.sqrt(2)
gA=(s,s,0,0); gB=(s,0,s,0)
I=(0,1,0,0); J=(0,0,1,0); K=(0,0,0,1); one=(1,0,0,0)
A=lambda q: Ad(gA,q); B=lambda q: Ad(gB,q)
print("A(i),A(j),A(k)", A(I),A(J),A(K))
print("B(i),B(j),B(k)", B(I),B(J),B(K))
print("AB(i)", A(B(I)), " BA(i)", B(A(I)))
# S1: Re(conj(qx) u qy v^-1) == qx . (u qy v^-1)
def rq():
    v=[random.gauss(0,1) for _ in range(4)]; n=math.sqrt(dot(v,v)); return tuple(x/n for x in v)
err=0
for _ in range(1000):
    qx,qy,u,v=rq(),rq(),rq(),rq()
    lhs=mul(mul(mul(conj(qx),u),qy),conj(v))[0]
    rhs=dot(qx, mul(mul(u,qy),conj(v)))
    # plaquette u qy v^-1 qx^-1
    pl=mul(mul(mul(u,qy),conj(v)),conj(qx))[0]
    err=max(err,abs(lhs-rhs),abs(lhs-pl))
print("S1 max error", err)
# S8: |(1-A)n|^2+|(1-B)n|^2 = 2(ni^2+nj^2+2nk^2)
err=0
for _ in range(1000):
    v=[random.gauss(0,1) for _ in range(3)]; nn=math.sqrt(sum(x*x for x in v)); n=(0,)+tuple(x/nn for x in v)
    da=[a-b for a,b in zip(n,A(n))]; db=[a-b for a,b in zip(n,B(n))]
    lhs=dot(da,da)+dot(db,db); rhs=2*(n[1]**2+n[2]**2+2*n[3]**2)
    err=max(err,abs(lhs-rhs))
print("S8 identity max error", err)
# H = Ad_i : u.Hu
gH=(0,1,0,0)
err=0
for _ in range(1000):
    u=rq(); Hu=Ad(gH,u)
    err=max(err,abs(dot(u,Hu)-(u[0]**2+u[1]**2-u[2]**2-u[3]**2)))
print("u.Hu formula max error", err, " H(1),H(j):", Ad(gH,one), Ad(gH,J))
