#!/usr/bin/env python3
"""Root's exact synthetic checks. No observations, fitted inputs or validation set."""
import hashlib
import json
from pathlib import Path
import sys

import sympy as s

HERE = Path(__file__).resolve().parent
checks = []


def zero(name, expression):
    residual = s.factor(s.cancel(expression))
    checks.append({"name": name, "pass": residual == 0, "residual": str(residual)})


def truth(name, condition, evidence):
    checks.append({"name": name, "pass": bool(condition), "evidence": str(evidence)})


h, hp, hpp, hppp = s.symbols("h hp hpp hppp", real=True)
b, bp, bpp, bppp = s.symbols("b bp bpp bppp", real=True)
k, kp = s.symbols("k kp", real=True)
x, y, z = s.symbols("x y z", real=True)
A = s.symbols("A", positive=True)
jets = {h: hp, hp: hpp, hpp: hppp, b: bp, bp: bpp, bpp: bppp, k: kp}


def partial_time(f):
    return sum(s.diff(f, symbol) * derivative for symbol, derivative in jets.items())


def dtau(f):
    return partial_time(f) + s.diff(f, x)*y + s.diff(f, y)*z + s.diff(f, A)*A*b*x


def deinstein(f):
    return A*dtau(f)


HE = A*(h-b*x)
v = A*x  # M=1, with all occurrences of density divided by M^2.
r0 = 2*bp*x-2*hp-2*b*h*x+(2*b*b-1)*x*x
R = 2*b*y+r0
rho_energy = A*A*R
dust = dtau(R)+(3*h-2*b*x)*R
kg = z+3*h*y+(3*hp+k-2*(bp*x+b*y)+6*h*b*x-4*b*b*x*x)*x-3*b*(h-b*x)*R

zero("Raychaudhuri transformed without supplied clock map", -2*deinstein(HE)/A**2-x*x-R)
zero("dust exchange transformed with A derivatives", (deinstein(rho_energy)+3*HE*rho_energy-b*v*rho_energy)/A**3-dust)
zero("differentiated KG transformed including dust and acceleration", (deinstein(deinstein(v))+3*HE*deinstein(v)+(3*deinstein(HE)+A*A*k)*v-3*HE*b*rho_energy)/A**3-kg)

B1 = 3*h-2*b*x-6*b*b*(h-b*x)
B0 = (3*hp+k-2*bp*x+6*h*b*x-4*b*b*x*x)*x-3*b*(h-b*x)*r0
C = -2*((6*b**4-2*b*b+1)*x+b*(1-6*b*b)*h-2*bp)
N = partial_time(r0)+(3*h-2*b*x)*r0-2*b*B0
zero("scalar equation has displayed linear x-prime coefficient", kg-z-B1*y-B0)
zero("eliminate x-double-prime between independently transformed equations", dust-2*b*kg-C*y-N)
truth("C affine", s.Poly(C, x).degree() == 1, s.Poly(C, x))
truth("N at most cubic", s.Poly(N, x).degree() <= 3, s.Poly(N, x).degree())
zero("strictly positive slope coefficient completed square", 6*b**4-2*b*b+1-(6*(b*b-s.Rational(1, 6))**2+s.Rational(5, 6)))

G = -N/C
Q = s.Poly(s.expand(-partial_time(N)*C*C+N*partial_time(C)*C+N*s.diff(N, x)*C-N*N*s.diff(C, x)-B1*N*C*C+B0*C**3), x)
zero("denominator clearing equals differentiated first-order flow", s.together(C**3*(partial_time(G)+s.diff(G, x)*G+B1*G+B0))-Q.as_expr())
truth("generic polynomial degree six", Q.degree() == 6, Q.degree())
zero("degree six coefficient", Q.coeff_monomial(x**6)-8*b*b*(6*b*b-1)*(12*b*b-7)*(6*b**4-2*b*b+1))
reflection = {x:-x, b:-b, bp:-bp, bpp:-bpp, bppp:-bppp}
zero("reflection C odd", C.xreplace(reflection)+C)
zero("reflection N even", N.xreplace(reflection)-N)
zero("reflection G odd", G.xreplace(reflection)+G)
zero("reflection Q even", Q.as_expr().xreplace(reflection)-Q.as_expr())

# Sufficiency uses the ORIGINAL scalar force, before its derivative is used.
V = A*A*(3*(h-b*x)**2-x*x/2-R)
force = deinstein(v)+3*HE*v+deinstein(V)/v+b*rho_energy
zero("Friedmann derivative recovers original scalar force given dust", force+A*A*dust/x)

t = s.symbols("t", positive=True)
p, c = s.symbols("p c", positive=True)
rbar = 2*p-c*c
exponent = 3*p-2
AE = rbar*t**exponent
VE = (3*p*p-2*p+c*c/2)/t**2
rho_bare = t**(-3*p)
vE = c/t
HEf = p/t


def dphi(f):
    return s.diff(f, t)/vE


muE = s.factor(dphi(dphi(VE))+rho_bare*dphi(dphi(AE)))
zero("forward power family Friedmann from specified action", 3*HEf**2-vE*vE/2-VE-AE*rho_bare)
zero("forward power family Raychaudhuri from specified action", -2*s.diff(HEf,t)-vE*vE-AE*rho_bare)
zero("forward power family original KG off minimum", s.diff(vE,t)+3*HEf*vE+dphi(VE)+rho_bare*dphi(AE))
zero("forward power family fixed-bare-density curvature", muE-(-2+6*p+3*p*exponent*rbar/c**2)/t**2)

tau = s.symbols("tau", positive=True)
n = 3*p-1
hf = (4*p-2)/(n*tau)
xf = c/(n*tau)
bf = exponent/c
kf = (-2+6*p+3*p*exponent*rbar/c**2)/(n*n*tau*tau)
Rf = rbar/(n*n*tau*tau)


def history_subs(hf, bf, kf, xf, derivative):
    return {h:hf, hp:derivative(hf), hpp:derivative(derivative(hf)),
            hppp:derivative(derivative(derivative(hf))), b:bf, bp:derivative(bf),
            bpp:derivative(derivative(bf)), bppp:derivative(derivative(derivative(bf))),
            k:kf, kp:derivative(kf), x:xf, y:derivative(xf), z:derivative(derivative(xf))}


power_subs = history_subs(hf,bf,kf,xf,lambda f:s.diff(f,tau))
zero("general power history physical R", R.xreplace(power_subs)-Rf)
zero("general power history matter dust", dust.xreplace(power_subs))
zero("general power history matter scalar", kg.xreplace(power_subs))
zero("general power history polynomial", Q.as_expr().xreplace(power_subs))

fixtures = [(s.Rational(1),s.Rational(1)), (s.Rational(4,5),s.Rational(1,2)),
            (s.Rational(3,2),s.Rational(1)), (s.Rational(2,3),s.Rational(1,2))]
fixture_evidence = []
for j,(pv,cv) in enumerate(fixtures):
    sub = {p:pv,c:cv}
    rs = s.factor(Rf.subs(sub)); cs = s.factor(C.xreplace(power_subs).subs(sub))
    truth(f"power fixture {j} positive dust", (2*pv-cv*cv)>0, rs)
    truth(f"power fixture {j} regular eliminated chart", cs != 0, cs)
    fixture_evidence.append({"p":str(pv),"c":str(cv),"R":str(rs),"C":str(cs),"b":str(bf.subs(sub))})

simple = {h:1/tau,hp:-1/tau**2,hpp:2/tau**3,hppp:-6/tau**4,b:1,bp:0,bpp:0,bppp:0,k:7/(4*tau**2),kp:-7/(2*tau**3)}
simpleQ = s.factor(Q.as_expr().xreplace(simple))
zero("simple forward fixture x=1/(2 tau)", simpleQ.subs(x,1/(2*tau)))
zero("simple fixture R", R.xreplace(simple).subs({x:1/(2*tau), y:-1/(2*tau*tau)})-1/(4*tau*tau))

# Non-power forward model: aE=t, A=t^2/4, rho=t^-3, phi-dot=sqrt(8-t)/(2t).
an = t*t/4
vn = s.sqrt(8-t)/(2*t)
hnE = 1/t
rnE = 1/(4*t)
Vn = 2/t**2-1/(8*t)
bn = s.diff(an,t)/(an*vn)
mun = s.factor((s.diff(s.diff(Vn,t)/vn,t)+t**-3*s.diff(s.diff(an,t)/vn,t))/vn)
zero("non-power original Friedmann", 3*hnE*hnE-vn*vn/2-Vn-rnE)
zero("non-power original Raychaudhuri", -2*s.diff(hnE,t)-vn*vn-rnE)
zero("non-power original KG", s.diff(vn,t)+3*hnE*vn+s.diff(Vn,t)/vn+t**-3*s.diff(an,t)/vn)
dn = lambda f:s.diff(f,t)/an
nonpower = history_subs((hnE+s.diff(an,t)/an)/an,bn,mun/an**2,vn/an,dn)
zero("non-power R from energy density", R.xreplace(nonpower)-rnE/an**2)
zero("non-power matter dust", dust.xreplace(nonpower))
zero("non-power matter scalar", kg.xreplace(nonpower))
# Avoid claiming a global C-domain from sampled points; the DAE checks above are interval identities.
for tv in [s.Rational(1),s.Rational(2),s.Rational(4)]:
    row={u:s.simplify(f.subs(t,tv)) for u,f in nonpower.items()}
    zero(f"non-power polynomial at t={tv}", Q.as_expr().xreplace(row))
    truth(f"non-power C nonzero at t={tv}", s.simplify(C.xreplace(row)) != 0, s.simplify(C.xreplace(row)))

# A whole uncoupled ambiguity family, not a degree-six inference at b=0.
uncoupled = {h:2/(3*tau),hp:-2/(3*tau*tau),hpp:4/(3*tau**3),hppp:-4/tau**4,b:0,bp:0,bpp:0,bppp:0,k:2/tau**2,kp:-4/tau**3}
zero("uncoupled continuum has identically zero polynomial", Q.as_expr().xreplace(uncoupled))
zero("uncoupled flow retains free x normalization", G.xreplace(uncoupled)+x/tau)

# Explicit scaling of a forward action at fixed phi and same matter time.
ell, phi = s.symbols("ell phi", positive=True)
As = ell*s.exp(phi)
Vs = ell**2*s.Rational(3,2)*s.exp(-2*phi)
rhob = ell*s.exp(-3*phi)
mus = s.diff(Vs,phi,2)+rhob*s.diff(As,phi,2)
zero("A-normalization rescaling leaves canonical b unchanged", s.diff(As,phi)/As-1)
zero("A-normalization rescaling leaves matter curvature unchanged", mus/As**2-7*s.exp(-4*phi))
zero("physical density over F invariant under A0 rescaling", (rhob/As**3)/(1/As**2)-s.exp(-4*phi))

# Mutation checks ensure key missing terms are distinguished by forward histories.
mutations = {
    "omit conformal q in Raychaudhuri": ((-2*hp-x*x)-R).xreplace(power_subs).subs({p:1,c:1,tau:1}),
    "omit dust source in scalar equation": (3*b*(h-b*x)*R).xreplace(power_subs).subs({p:1,c:1,tau:1}),
    "wrong scalar acceleration sign": (-2*z).xreplace(power_subs).subs({p:1,c:1,tau:1}),
    "curvature read as mu instead of mu/A^2": (mun-mun/an**2).subs(t,1),
}
for name,residual in mutations.items():
    truth("detect mutation: "+name,s.simplify(residual)!=0,s.simplify(residual))

sources={f:hashlib.sha256((HERE/f).read_bytes()).hexdigest() for f in
         [Path(__file__).name,"MATTER_CLOCK_DERIVATION_v1.md","MATTER_CLOCK_NEUTRAL_CONTRACT_v1.json"]}
output={"author":"/root", "kind":"exact mathematical and synthetic controls only", "sympy":s.__version__,
        "source_sha256":sources, "checks":checks, "passed":sum(c["pass"] for c in checks),
        "failed":sum(not c["pass"] for c in checks),"generic_polynomial_degree":Q.degree(),
        "leading_coefficient":str(s.factor(Q.LC())),"simple_fixture_polynomial":str(simpleQ),
        "power_fixtures":fixture_evidence,
        "limitations":["No empirical data or independently registered b,kappa", "C=0 histories unclassified",
                       "General identically-zero Q unclassified", "No scale, action or preferred history selected"]}
print(json.dumps(output,indent=2,sort_keys=True))
sys.exit(int(output["failed"]>0))
