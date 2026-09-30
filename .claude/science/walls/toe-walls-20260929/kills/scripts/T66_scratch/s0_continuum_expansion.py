# Continuum control: expand sqrt(g) R for the planar diagonal metric g=diag(1+hxx,1+hyy,1+hzz)(x)
# to second order and compare with the landed b62 symbols R1 = -d^2(hyy+hzz) and R2 = (1/2) hyy' hzz' (mod total derivatives).
import sympy as sp
x,t=sp.symbols('x t')
hxx,hyy,hzz=[sp.Function(n)(x) for n in ('hxx','hyy','hzz')]
g=sp.diag(1+t*hxx,1+t*hyy,1+t*hzz)
X=[x,sp.Symbol('y'),sp.Symbol('z')]
ginv=g.inv()
def Gam(a,b,c):
    return sum(ginv[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(3))/2
def Riem(a,b,c,d):  # R^a_{bcd}
    r=sp.diff(Gam(a,b,d),X[c])-sp.diff(Gam(a,b,c),X[d])
    r+=sum(Gam(a,c,e)*Gam(e,b,d)-Gam(a,d,e)*Gam(e,b,c) for e in range(3))
    return r
Ric=sp.Matrix(3,3,lambda b,d: sum(Riem(a,b,a,d) for a in range(3)))
R=sum(ginv[b,d]*Ric[b,d] for b in range(3) for d in range(3))
sg=sp.sqrt(g.det())
L=sp.simplify(sg*R)
ser=sp.series(L,t,0,3).removeO()
c1=sp.simplify(ser.coeff(t,1)); c2=sp.simplify(ser.coeff(t,2))
print("order1:",sp.expand(c1))
print("order2:",sp.expand(c2))
# reduce order2 mod total derivatives via Euler operator: compare Euler-Lagrange of c2 with that of 1/2 hyy' hzz'
from sympy.calculus.euler import euler_equations
cand=sp.Rational(1,2)*sp.diff(hyy,x)*sp.diff(hzz,x)
for f in (hxx,hyy,hzz):
    e1=sp.simplify(euler_equations(c2,[hxx,hyy,hzz],x)[[hxx,hyy,hzz].index(f)].lhs)
    e2=sp.simplify(euler_equations(cand,[hxx,hyy,hzz],x)[[hxx,hyy,hzz].index(f)].lhs)
    print(f, sp.simplify(e1-e2))
