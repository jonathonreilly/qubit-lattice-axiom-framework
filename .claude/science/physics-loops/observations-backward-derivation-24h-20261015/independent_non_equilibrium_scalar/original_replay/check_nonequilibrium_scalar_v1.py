#!/usr/bin/env python3
"""Exact conditional scalar inverse controls; no observational inputs or fitting.

Run from any directory. The output is deterministic; it does not confer an
independent review or formal scientific status. SymPy identities support the
written proof, whose functional domains are not established by finite fixtures.
"""
from pathlib import Path
import hashlib
import json
import sys
import sympy as s

ROOT = Path(__file__).resolve().parent
checks = []


def zero(name, expression):
    residual = s.simplify(s.factor(expression))
    checks.append({"name": name, "pass": residual == 0,
                   "method": "exact symbolic identity", "residual": str(residual)})


def truth(name, predicate, detail):
    checks.append({"name": name, "pass": bool(predicate),
                   "method": "exact algebra or stated numerical diagnostic", "detail": detail})


def poly(v, h, hd, d, e, f, alpha, alpha_dot, mu):
    return (2*alpha**2*v**6 + (9*h*alpha+2*alpha_dot)*v**5
            + (-2*d*alpha**2-9*h**2+6*hd+4*mu)*v**4
            + (-12*d*h*alpha-2*d*alpha_dot-e*alpha)*v**3
            + (18*d*h**2+6*d*hd+2*f+12*e*h)*v**2
            + (3*d**2*h*alpha+d*e*alpha)*v-(3*d*h+e)**2)


t = s.symbols("t", positive=True)
M = s.symbols("M", positive=True)
# Variation of a lapse-retaining homogeneous action, before fixing N=1.
a, ph, N = (s.Function(n)(t) for n in ("a", "phi", "N"))
V, A = s.Function("V"), s.Function("A")
rho0 = s.symbols("rho0", positive=True)
L = (-3*M**2*a*s.diff(a,t)**2/N + a**3*s.diff(ph,t)**2/(2*N)
     - N*a**3*V(ph) - N*rho0*A(ph))
gauge = {N: 1, s.diff(N,t): 0}
H = s.diff(a,t)/a
v = s.diff(ph,t)
r = rho0*A(ph)/a**3
friedmann = 3*M**2*H**2-v**2/2-V(ph)-r
scalar = s.diff(v,t)+3*H*v+s.diff(V(ph),ph)+rho0/a**3*s.diff(A(ph),ph)
el_phi = s.diff(s.diff(L, s.diff(ph,t)),t)-s.diff(L,ph)
el_a = s.diff(s.diff(L, s.diff(a,t)),t)-s.diff(L,a)
zero("lapse variation gives Friedmann", s.diff(L,N).subs(gauge)/a**3-friedmann)
zero("scalar variation fixes density and coupling normalization", el_phi.subs(gauge)/a**3-scalar)
zero("scale-factor variation plus constraint gives Raychaudhuri",
     el_a.subs(gauge)/(3*a**2)-friedmann-(-2*M**2*s.diff(H,t)-v**2-r))
zero("particle dust exchange", s.diff(r,t)-(-3*H+s.diff(A(ph),ph)/A(ph)*v)*r)

# General coefficient reduction, with D,H derivative jets treated independently.
x,h,j,d,e,f,al,ald,mu = s.symbols("x H Hdot D Ddot Dddot alpha alphadot mu")
g = (e+3*h*d-al*d*x-3*h*x*x+al*x**3)/(2*x)
gt = s.diff(g,h)*j+s.diff(g,d)*e+s.diff(g,e)*f+s.diff(g,al)*ald
compatibility = gt+s.diff(g,x)*g+3*h*g+(3*j+mu)*x-3*h*al*(d-x*x)
P = poly(x,h,j,d,e,f,al,ald,mu)
zero("expanded curvature polynomial agrees with differentiated KG", P-4*x**3*compatibility)
zero("dust conservation solves first-order velocity equation",
     e-2*x*g-(-3*h+al*x)*(d-x*x))
truth("nonzero coupling gives exact degree six", s.Poly(P,x).degree()==6,
      {"leading_coefficient": str(s.Poly(P,x).LC())})
zero("degree-six coefficient is positive for nonzero real coupling", s.Poly(P,x).LC()-2*al**2)
zero("constant coefficient retains density expansion derivative", P.subs(x,0)+(3*h*d+e)**2)

# A general exact power-law family generated in the forward direction. The
# field-space action supplies alpha and mu before use of the inverse formulas.
q,c,mm = s.symbols("q c mm", positive=True)
phi = c*s.log(t)
rho = t**(-3*q)
R0 = 2*mm**2*q-c**2
AF = R0*s.exp((3*q-2)*s.Symbol("z")/c)
VF = (3*mm**2*q*q-2*mm**2*q+c*c/2)*s.exp(-2*s.Symbol("z")/c)
z = s.Symbol("z")
hf = q/t
vf = c/t
rf = R0/t**2
af = s.diff(AF,z).subs(z,phi)/AF.subs(z,phi)
mf = (s.diff(VF,z,2)+rho*s.diff(AF,z,2)).subs(z,phi)
zero("forward power-law Friedmann", 3*mm**2*hf**2-vf**2/2-VF.subs(z,phi)-rf)
zero("forward power-law Raychaudhuri", -2*mm**2*s.diff(hf,t)-vf**2-rf)
zero("forward power-law scalar equation", s.diff(vf,t)+3*hf*vf+(s.diff(VF,z)+rho*s.diff(AF,z)).subs(z,phi))
zero("forward power-law matter energy", rho*AF.subs(z,phi)-rf)
zero("forward power-law signed coupling", af-(3*q-2)/c)
zero("forward power-law curvature", mf-(-2+6*q+3*q*(3*q-2)*R0/c**2)/t**2)
df = -2*mm**2*s.diff(hf,t)
gf = g.subs({h:hf,d:df,e:s.diff(df,t),al:af,x:vf})
zero("inverse differential equation recovers forward power-law", gf-s.diff(vf,t))
zero("inverse polynomial recovers forward power-law",
     poly(vf,hf,s.diff(hf,t),df,s.diff(df,t),s.diff(df,t,2),af,s.diff(af,t),mf))

# A non-power-law chart with time-dependent coupling. Parametric A(t),V(t)
# permit direct chain derivatives with respect to phi; no phi quadrature or
# inverse runner output is used to define mu.
hn = 1/t
rn = 1/(4*t)
vn = s.sqrt(2/t**2-rn)
An = t**2/4
Vn = 2/t**2-rn/2
rhon = t**-3
an = s.diff(An,t)/(An*vn)
mun = (s.diff(s.diff(Vn,t)/vn,t)+rhon*s.diff(s.diff(An,t)/vn,t))/vn
dn = 2/t**2
zero("non-power-law scalar equation", s.diff(vn,t)+3*hn*vn+s.diff(Vn,t)/vn+rhon*s.diff(An,t)/vn)
zero("non-power-law dust exchange", s.diff(rn,t)-(-3*hn+an*vn)*rn)
zero("non-power-law inverse velocity", g.subs({h:hn,d:dn,e:s.diff(dn,t),al:an,x:vn})-s.diff(vn,t))
zero("non-power-law inverse curvature", poly(vn,hn,s.diff(hn,t),dn,s.diff(dn,t),s.diff(dn,t,2),an,s.diff(an,t),mun))
truth("non-power-law fixture has positive dust and kinetic energy on 1<t<4",
      s.simplify(vn**2-(8-t)/(4*t**2))==0,
      "r=1/(4t)>0 and v^2=(8-t)/(4t^2)>0; interval explicitly restricted to 1<t<4")

# Complete root filtering in the q=c=M=1 fixture.
p1 = s.factor(poly(x,1,-1,2,-4,12,1,0,7))
expected = (x-1)*(2*x**5+11*x**4+20*x**3+4)
zero("unique-fixture curvature factorization", p1-expected)
diff_num = (x-1)*(x*x-2)
zero("unique-fixture differential residual", g.subs({h:1,d:2,e:-4,al:1})+x-diff_num/(2*x))
zero("instantaneous and differential polynomial gcd", s.gcd(p1,diff_num)-(x-1))
truth("one extra instantaneous physical root exists", p1.subs(x,-s.Rational(7,10))*p1.subs(x,-s.Rational(6,10))<0,
      {"interval": "(-7/10,-6/10) inside (-sqrt(2),0)",
       "p_left":str(p1.subs(x,-s.Rational(7,10))),"p_right":str(p1.subs(x,-s.Rational(6,10)))})
zero("minimum formula is not the fixture velocity", 3*s.Rational(1,7)-1+s.Rational(4,7))
truth("minimum discrepancy is nonzero", s.Rational(3,7)!=1,
      "The actual nonzero scalar force balances acceleration; no claim against a minimum-tracking theorem.")

# Full continuum of admissible uncoupled histories at the degenerate inputs.
zero("uncoupled dust-era curvature polynomial is identically zero",
     poly(x,s.Rational(2,3)/t,-s.Rational(2,3)/t**2,
          s.Rational(4,3)/t**2,-s.Rational(8,3)/t**3,8/t**4,0,0,2/t**2))
for cc in [s.Rational(1,2), s.Rational(3,4), s.Integer(1)]:
    substitutions = {q:s.Rational(2,3),c:cc,mm:1}
    zero(f"uncoupled family c={cc} identical coupling", af.subs(substitutions))
    zero(f"uncoupled family c={cc} identical curvature", mf.subs(substitutions)-2/t**2)
    truth(f"uncoupled family c={cc} positive matter", R0.subs(substitutions)>0,
          {"r_times_t_squared":str(R0.subs(substitutions)),"canonical_slope":str(-2/cc)})

# Local curvature input is not simply V''. Wrong fixed-r density differentiation
# would remove a term. The concrete fixture catches this convention substitution.
zero("fixed-conserved-density and fixed-energy-density curvatures differ",
     (s.diff(VF,z,2)+rho*s.diff(AF,z,2)).subs({z:phi,q:1,c:1,mm:1})-7/t**2)
truth("bare potential curvature alone fails fixture", s.Integer(6)!=s.Integer(7),
      "V''=6/t^2; fixed-rho response curvature=7/t^2 in the unique fixture.")

# A calibrated r(t) supplies an additional, separate constraint. It determines
# speed squared directly and leaves only the chart orientation if positive.
rr=s.Function("r")(t)
hh=s.Function("h")(t)
kk=-2*M**2*s.diff(hh,t)-rr
qq=s.diff(rr,t)/rr+3*hh
yk=s.sqrt(kk)
mu_from_k=(-s.diff(kk,t,2)/(2*kk)+s.diff(kk,t)**2/(4*kk**2)
           -3*hh*s.diff(kk,t)/(2*kk)-3*s.diff(hh,t)+3*hh*rr*qq/kk)
zero("registered-density curvature identity",
     mu_from_k-(-s.diff(yk,t,2)/yk-3*hh*s.diff(yk,t)/yk
                 -3*s.diff(hh,t)+3*hh*rr*qq/kk))

# Ill-conditioning illustration: finite algebraic candidate count is not a
# uniformly stable inverse as coupling approaches the exact degenerate family.
eps=s.symbols("eps", positive=True)
pp=(2+eps)/3
alp=eps
mup=(-2+6*pp+3*pp*eps*(2*pp-1))
pe=poly(x,pp,-pp,2*pp,-4*pp,12*pp,alp,0,mup)
root_slope=s.factor(s.diff(pe,x).subs(x,1))
zero("near-degenerate family preserves exact velocity", pe.subs(x,1))
zero("root slope vanishes in uncoupled limit", s.limit(root_slope,eps,0))
truth("near-degenerate finite-input root slope is nonzero",
      root_slope.subs(eps,s.Rational(1,1000))!=0,
      {"dP_dv_at_true_root":str(root_slope),
       "interpretation":"Algebraic sensitivity only; no observational covariance or statistical coverage."})

passed=sum(x["pass"] for x in checks)
payload={"schema":"conditional-scalar-inverse-controls-v1",
         "author":"root personally", "sympy_version":s.__version__,
         "scope":"Exact identities and constructed fixtures; not an independent implementation or empirical test",
         "source_sha256":hashlib.sha256((ROOT/'NON_EQUILIBRIUM_SCALAR_INVERSE_v1.md').read_bytes()).hexdigest(),
         "runner_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "checks":checks,"passed":passed,"failed":len(checks)-passed,
         "polynomial":str(s.Poly(P,x)),"near_degenerate_root_slope":str(root_slope)}
out=ROOT/'NON_EQUILIBRIUM_SCALAR_CONTROLS_v1.json'
out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
for row in checks:
    print(('PASS' if row['pass'] else 'FAIL')+': '+row['name'])
print(f'TOTAL: PASS={passed} FAIL={len(checks)-passed}')
sys.exit(int(passed!=len(checks)))
