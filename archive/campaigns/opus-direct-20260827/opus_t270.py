"""
T270 - general-d symbolic derivation of the a1 slope, as a second route.

For g = e^{2w} delta in d dims,  R = e^{-2w}[-2(d-1) lap w - (d-1)(d-2)|grad w|^2].
With f = 1+eps*cos(kappa x), w = (1/2)ln f, expand sqrt(g)R = f^{d/2-1}[...] to
O(eps^2) and average over a period.  The slope of R(s)=1+b1*s*kappa^2 is
   b1*kappa^2 = <sqrt(g) R>_2 / (6 * <sqrt(g)>_2).
This MUST give 1/4 at d=4 -- a value measured independently in R132 -- and
2/9 at d=3.  One formula, two checks, one of them against a measurement.
"""
import sympy as sp
eps,kap,x,d = sp.symbols('epsilon kappa x d', positive=True)
f = 1 + eps*sp.cos(kap*x)
w = sp.Rational(1,2)*sp.log(f)
lap  = sp.diff(w,x,2)
grad2= sp.diff(w,x)**2
sgR  = f**(d/2-1) * (-2*(d-1)*lap - (d-1)*(d-2)*grad2)
sg   = f**(d/2)

def eps2_avg(expr):
    c = sp.simplify(sp.series(expr, eps, 0, 3).removeO().coeff(eps,2))
    return sp.simplify(sp.integrate(c,(x,0,2*sp.pi/kap))/(2*sp.pi/kap))

num, den = eps2_avg(sgR), eps2_avg(sg)
b1k2 = sp.simplify(num/(6*den))
print("  <sqrt(g) R>_2  =", sp.simplify(num))
print("  <sqrt(g)>_2    =", sp.simplify(den))
print("  b1*kappa^2     =", b1k2, "   ->  b1 =", sp.simplify(b1k2/kap**2))
print()
for dv,name,ref in ((3,"d=3","2/9 target"),(4,"d=4","1/4 MEASURED in R132")):
    val=sp.simplify(b1k2.subs(d,dv)/kap**2)
    print(f"  {name}:  b1 = {val} = {float(val):.6f}     [{ref}]")
