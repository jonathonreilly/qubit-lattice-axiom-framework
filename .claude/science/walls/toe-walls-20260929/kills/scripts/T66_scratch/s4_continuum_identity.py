# CONTROL 3: the degree-2 identity holds in the CONTINUUM ADM planar-diagonal sector with
#   T = (1/(4a)) (sum g_a^2 P_a^2 - 1/2 (sum g_a P_a)^2)/sqrt(g),  C[N] = int N (T + K sqrt(g) R),  g_a = 1 + h_a
#   G[xi] = int xi [ P_x h_x' - 2((1+h_x) P_x)' + P_y h_y' + P_z h_z' ],  xi = (K/4a) g^{xx}(N'M - N M')
# We check {C[N],C[M]} = G[xi] to total degree 2 (terms P*h) in fields, and record the pieces (T3, V2, xi1) used as the reference.
import sympy as sp
from sympy.calculus.euler import euler_equations
x,t,K,a=sp.symbols('x t K a',positive=True)
hx,hy,hz,Px,Py,Pz,N,M=[sp.Function(n)(x) for n in ('hx','hy','hz','Px','Py','Pz','N','M')]
H=[hx,hy,hz]; P=[Px,Py,Pz]
def D(f,n=1): return sp.diff(f,x,n)
# sqrt(g) R exact for diag planar metric (from s0), expanded to order 2
X=[x,sp.Symbol('y'),sp.Symbol('z')]
g=sp.diag(1+t*hx,1+t*hy,1+t*hz); ginv=g.inv()
def Gam(a_,b,c): return sum(ginv[a_,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(3))/2
def Riem(a_,b,c,d):
    r=sp.diff(Gam(a_,b,d),X[c])-sp.diff(Gam(a_,b,c),X[d])
    r+=sum(Gam(a_,c,e)*Gam(e,b,d)-Gam(a_,d,e)*Gam(e,b,c) for e in range(3)); return r
Ric=sp.Matrix(3,3,lambda b,d: sum(Riem(a_,b,a_,d) for a_ in range(3)))
Rs=sum(ginv[b,d]*Ric[b,d] for b in range(3) for d in range(3))
sgR=sp.series(sp.sqrt(g.det())*Rs,t,0,3).removeO()
sgR1=sp.expand(sgR.coeff(t,1)); sgR2=sp.expand(sgR.coeff(t,2))
# kinetic: rescale P by t as well? Degrees: track total degree with t on both h and P
gh=[1+t*h for h in H]
Tfull=(sum(gh[i]**2*(t*P[i])**2 for i in range(3))-sp.Rational(1,2)*sum(gh[i]*t*P[i] for i in range(3))**2)/sp.sqrt(gh[0]*gh[1]*gh[2])/(4*a)
Tser=sp.series(Tfull,t,0,4).removeO()
T2=sp.expand(Tser.coeff(t,2)); T3=sp.expand(Tser.coeff(t,3))
def var_deriv(L,f):
    # Euler operator: sum_n (-D)^n dL/d f^{(n)}
    res=0
    for n in range(0,4):
        fn=D(f,n) if n>0 else f
        res+= (-1)**n*D(sp.diff(L,fn),n)
    return sp.expand(res)
def PB(FN,FM):
    tot=0
    for hh,pp in zip(H,P):
        tot+= var_deriv(FN,hh)*var_deriv(FM,pp)-var_deriv(FN,pp)*var_deriv(FM,hh)
    return sp.expand(tot)
# lapse-weighted densities
def CN(L): return L*(T2+T3)+K*L*(sgR1+sgR2)   # up to cubic (T3, sgR2 deg 2 => V2). sgR3 not needed at this degree
CNn=CN(N); CMm=CN(M)
br=PB(CNn,CMm)
# keep terms of total degree exactly 2 in (h,P): degree counting via t is lost after PB; recount by scaling
scale=sp.Symbol('s')
def deg_part(expr,deg):
    sub={f:scale*f for f in H+P}
    e=expr.subs(sub,simultaneous=True).doit()
    return sp.expand(e).coeff(scale,deg)
br2=deg_part(br,2)
# the GR side: G[xi] density with xi = (K/4a) g^{xx}(N'M-NM'); degree-2: P h terms
xi_full=(K/(4*a))*(1-hx)*(D(N)*M-N*D(M))     # g^{xx}=1/(1+hx) -> 1-hx to first order
xi0=(K/(4*a))*(D(N)*M-N*D(M))
def Gdens(xi): return xi*(Px*D(hx)-2*D((1+hx)*Px)+Py*D(hy)+Pz*D(hz))
G_total=sp.expand(Gdens(xi_full))
G2=deg_part(G_total,2)
diff=sp.expand(br2-G2)
# diff must be a total derivative: all variational derivatives vanish
ok=True
for f in H+P:
    vd=sp.simplify(var_deriv(diff,f))
    print(f, 'EL of residual =', vd)
    ok = ok and vd==0
print("degree-2 continuum identity holds:", ok)

print("---- debug: degree 1 and sign of xi")
br1=deg_part(br,1)
G1=deg_part(sp.expand(Gdens(xi0)),1)
for sgn in (1,-1):
    d1=sp.expand(br1-sgn*G1)
    print("deg1 sign",sgn,[sp.simplify(var_deriv(d1,f)) for f in H+P])
for sgn in (1,-1):
    xi_s=sgn*xi_full
    G2s=deg_part(sp.expand(Gdens(xi_s)),2)
    d2=sp.expand(br2-G2s)
    print("deg2 sign",sgn,[sp.simplify(var_deriv(d2,f)) for f in H+P])

print("---- inspect")
def coeff_of(expr, *facs):
    e=sp.expand(expr)
    return sp.simplify(e.coeff(facs[0]).coeff(facs[1])) if False else None
# collect br2 terms containing hx*Px with no derivative of hx,Px
b2=sp.expand(br2)
terms=[tm for tm in sp.Add.make_args(b2) if tm.has(hx) and tm.has(Px) and not tm.has(sp.Derivative(hx,x)) and not tm.has(sp.Derivative(Px,x))]
print("br2 hx*Px terms (no field derivs):", sp.simplify(sp.Add(*terms)))
G2s=deg_part(sp.expand(Gdens(xi_full)),2)
g2=sp.expand(G2s)
terms=[tm for tm in sp.Add.make_args(g2) if tm.has(hx) and tm.has(Px) and not tm.has(sp.Derivative(hx,x)) and not tm.has(sp.Derivative(Px,x))]
print("G2 hx*Px terms (no field derivs):", sp.simplify(sp.Add(*terms)))
# also try integrating by parts to a canonical form: compare via EL on generic test
