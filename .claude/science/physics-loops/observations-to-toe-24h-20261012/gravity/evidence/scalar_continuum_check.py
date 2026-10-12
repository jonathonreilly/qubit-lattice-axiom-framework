"""Checks for the independently derived scalar continuum, hbar=c=1.

No parent equations or implementation are imported. Oscillator overlap,
frequency-spectrum and positive Schwinger-parameter integrals are compared.
"""
from pathlib import Path
import datetime
import json
import math
import os
import time

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import scipy
from scipy.integrate import quad
from scipy.special import beta, erfcx, gamma, hyp2f1, j1, k1

ROOT=Path("/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012")
HERE=ROOT/"gravity_measurements"
assert not any(ROOT.glob("*STOP_REQUESTED*"))
assert time.time()<json.loads((ROOT/"DEADLINE.json").read_text())["deadline_epoch"]
ell=1.3
a=0.7
d=1.2
g=0.8
pi=math.pi


def rho(mu,s):
    if mu==0:
        return ell if s==1 else 0.0
    return ell**s*mu**(s-1)*math.exp(-ell*mu)/gamma(s)


def one_minus_sinc(x):
    if abs(x)<0.02:
        return x*x*(1/6-x*x/120+x**4/5040-x**6/362880)
    return 1-math.sin(x)/x


def sdiff(w,s=1.0):
    if w==0:
        return 0.0
    def integrand(u):
        kval=w*math.sqrt(max(0.0,1-u*u))
        return rho(w*u,s)*kval*math.exp(-a*a*kval*kval)*one_minus_sinc(kval*d)*w/pi
    return quad(integrand,0,1,epsabs=2e-14,epsrel=2e-10,limit=160)[0]


def slocal(w,s):
    def integrand(u):
        kval=w*math.sqrt(max(0.0,1-u*u))
        return rho(w*u,s)*kval*math.exp(-a*a*kval*kval)*w/(2*pi)
    return quad(integrand,0,1,epsabs=1e-18,epsrel=2e-10,limit=160)[0]


def frequency_density(w):
    return g*g*sdiff(w)/(2*pi*w*w) if w else 0.0


def gamma_oscillator(T):
    def by_mass(mu):
        def by_k(k):
            w=math.hypot(k,mu)
            if w==0:
                return 0.0
            return k*k*math.exp(-a*a*k*k)*one_minus_sinc(k*d)*2*math.sin(w*T/2)**2/w**3
        return rho(mu,1)*quad(by_k,0,math.inf,epsabs=2e-11,epsrel=2e-9,limit=150)[0]
    return g*g/(2*pi*pi)*quad(by_mass,0,math.inf,epsabs=2e-10,epsrel=2e-8,limit=150)[0]


def gamma_schwinger():
    def f(u):
        if u==0:
            return 0.0
        # Exact M_nu for s=1, evaluated without overflow via erfcx.
        M=ell*math.sqrt(pi)/(2*math.sqrt(u))*erfcx(ell/(2*math.sqrt(u)))
        return math.sqrt(u)/(a*a+u)**1.5*(-math.expm1(-d*d/(4*(a*a+u))))*M
    return g*g/(4*pi*pi)*quad(f,0,math.inf,epsabs=2e-12,epsrel=2e-10,limit=160)[0]


out={"created_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
     "scipy_version":scipy.__version__,
     "parameters":{"s_for_decoherence":1,"ell":ell,"a":a,"d":d,"g":g},
     "static":[],"retarded_tail":[],"low_frequency":[],"decoherence":[],"long_time":[]}
for s in (.4,1.,2.7):
    for r in (.3,2.):
        val=quad(lambda mu:rho(mu,s)*math.exp(-r*mu),0,math.inf,epsabs=2e-12,epsrel=2e-10)[0]
        expected=(ell/(ell+r))**s
        out["static"].append(dict(s=s,r=r,laplace_quadrature=val,closed=expected,relative_error=abs(val/expected-1)))
    for tau in (.2,2.):
        val=quad(lambda mu:rho(mu,s)*mu*j1(mu*tau),0,math.inf,epsabs=2e-12,epsrel=2e-10,limit=160)[0]/(4*pi*tau)
        expected=s*(s+1)/(8*pi*ell*ell)*hyp2f1((s+2)/2,(s+3)/2,2,-(tau/ell)**2)
        out["retarded_tail"].append(dict(s=s,tau=tau,mass_quadrature=val,hypergeometric=expected,relative_error=abs(val/expected-1)))
    w=.001
    A=ell**s*beta(s/2,1.5)/(4*pi*gamma(s))
    out["low_frequency"].append(dict(s=s,omega=w,local_ratio=slocal(w,s)/(A*w**(s+1)),difference_ratio=sdiff(w,s)/(A*d*d/(s+3)*w**(s+3))))

# A separate spacelike Wightman integral whose expected value was derived
# by K1's cosh integral and a rational substitution, not curve fitted.
wval=quad(lambda mu:rho(mu,1)*mu*k1(mu*ell)/(4*pi*pi*ell),0,math.inf,epsabs=2e-13,epsrel=2e-10)[0]
out["wightman_s1_at_r_equal_ell"]={"mass_integral":wval,"analytic":1/(6*pi*pi*ell*ell)}
plateau=quad(frequency_density,0,math.inf,epsabs=3e-12,epsrel=2e-9,limit=160)[0]
out["plateau"]={"frequency_route":plateau,"schwinger_route":gamma_schwinger(),"all_T_polynomial_bound":g*g*d*d/(12*pi*pi*a*a)}
for T in (2.,5.):
    first=gamma_oscillator(T)
    second=quad(lambda w:frequency_density(w)*2*math.sin(w*T/2)**2,0,math.inf,epsabs=3e-11,epsrel=2e-8,limit=250)[0]
    out["decoherence"].append(dict(T=T,oscillator_route=first,frequency_route=second,relative_difference=abs(first/second-1)))
for T in (10.,20.,40.):
    approach=quad(frequency_density,0,math.inf,weight="cos",wvar=T,epsabs=1e-12,limlst=160,limit=200)[0]
    predicted=-g*g*ell*ell*d*d/(10*pi*pi*T**4)
    out["long_time"].append(dict(T=T,plateau_minus_exponent=approach,leading_asymptotic=predicted,ratio=approach/predicted))
out["scope"]="Self-checks of the independent conditional construction, not empirical validation or independent review of parent code."
(HERE/"scalar_continuum_check_results.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
assert max(x["relative_error"] for x in out["static"]+out["retarded_tail"])<1e-7
assert abs(wval/(1/(6*pi*pi*ell*ell))-1)<1e-7
assert abs(plateau/out["plateau"]["schwinger_route"]-1)<1e-7
assert max(x["relative_difference"] for x in out["decoherence"])<1e-6
assert all(0<x["local_ratio"]<1.002 and abs(x["local_ratio"]-1)<.01 for x in out["low_frequency"])
assert all(abs(x["difference_ratio"]-1)<.01 for x in out["low_frequency"])
assert abs(out["long_time"][-1]["ratio"]-1)<.03
print("Scalar normalization and independent integration-route checks passed.")
