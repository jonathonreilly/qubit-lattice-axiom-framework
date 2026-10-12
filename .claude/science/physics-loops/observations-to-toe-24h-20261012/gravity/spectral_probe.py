#!/usr/bin/env python3
"""Finite-source gravity response probe; benchmark, not experimental likelihood.

All variables called mu are inverse Compton lengths, in m^-1, not masses in eV.
The numerical light response uses the dimensionless z/b integral to resolve
the narrow central ray accurately even when endpoints are many AU away.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import k1, k1e

C = 299792458.0
PC = 3.085677581491367e16  # IAU parsec via exact AU and angular convention
AU = 149597870700.0
RS = 695700000.0  # nominal scale for this declared geometry


def sphere_scaled(x: float) -> float:
    """exp(-x)*3*(x*cosh(x)-sinh(x))/x^3, stable at zero and infinity."""
    if x < 0:
        raise ValueError("nonnegative inverse length required")
    if x < 1e-3:
        return math.exp(-x) * (1 + x*x/10 + x**4/280 + x**6/15120)
    return 1.5 * ((x-1) + (x+1)*math.exp(-2*x)) / x**3


def source_yukawa(mu: float, r: float, radius: float = 0.0) -> float:
    """Uniform-sphere exterior monopole, normalized to unit mass times 1/r."""
    if r < radius or radius < 0 or mu < 0:
        raise ValueError("requires r >= radius >= 0 and mu >= 0")
    return sphere_scaled(mu*radius) * math.exp(-mu*(r-radius))


def force_kernel(mu: float, r: float, radius: float = 0.0) -> float:
    return (1 + mu*r) * source_yukawa(mu, r, radius)


def ray_gradient(mu: float, b: float, z_left: float, z_right: float,
                 radius: float = 0.0) -> tuple[float, float]:
    """-b/2 times d/db integral F exp(-mu*r)/r dz at fixed z endpoints.

    Substitution z=b*sinh(t) gives an integrand exp(-mu*b*cosh(t))
    *(1+mu*b*cosh(t))/cosh(t)^2. F exp(-mu*radius) is evaluated separately.
    The massless infinite-ray value is 1. This is NOT the full orbital Doppler.
    """
    if b < radius:
        raise ValueError("ray must stay outside source")
    x = mu*b
    def f(t):
        ct = math.cosh(t)
        return math.exp(-mu*(b*ct-radius)) * (1+x*ct) / ct**2
    vals = [quad(f, 0, math.asinh(z/b), epsabs=2e-13, epsrel=2e-12)
            for z in (z_left, z_right)]
    scale = sphere_scaled(mu*radius)/2
    return scale*sum(v[0] for v in vals), scale*sum(v[1] for v in vals)


def infinite_ray(mu: float, b: float, radius: float = 0.0) -> float:
    if mu == 0:
        return 1.0
    x = mu*b
    return sphere_scaled(mu*radius)*math.exp(-mu*(b-radius))*x*k1e(x)


def group_delay(mu: float, hz: float, distance: float) -> float | None:
    q = (mu*C/(2*math.pi*hz))**2
    if q >= 1:
        return None
    # 1/sqrt(1-q)-1 evaluated without catastrophic cancellation.
    s = math.sqrt(1-q)
    return distance/C * q/(s*(1+s))


def run() -> dict:
    checks = []
    def check(name, condition, details):
        checks.append({"name": name, "pass": bool(condition), "details": details})
    for x in (0.0, 1e-7, 0.01, 1., 10., 100.):
        # Direct angular/radial integral, scaled by exp(-x), independent
        # of the closed sphere formula (angular kernel integrated analytically).
        if x == 0:
            radial = 1.
        else:
            radial = quad(lambda u: 1.5*u*(math.exp(-x*(1-u))-
                                            math.exp(-x*(1+u)))/x,
                          0, 1, epsabs=1e-13)[0]
        closed = sphere_scaled(x)
        check(f"sphere source quadrature x={x}", abs(radial-closed)<2e-10,
              {"quadrature": radial, "closed": closed})
    for x in (0., 1e-5, 0.1, 1., 20.):
        numerical, error = ray_gradient(x, 1., 1e7, 1e7)
        analytic = 1. if x == 0 else x*k1(x)
        check(f"ray Bessel limit x={x}", abs(numerical-analytic)<1e-10,
              {"quadrature": numerical, "bessel": analytic, "quad_error": error})
    z1, z2 = AU, 8.43*AU
    b0 = 1.6*RS
    l0 = ray_gradient(0., b0, z1, z2)[0]
    def mismatch(t):
        # t=mu*AU; source profile factor cancels exactly in this ratio.
        light = ray_gradient(t/AU, b0, z1, z2)[0]/l0
        force = force_kernel(t/AU, AU)
        return light - (4/3)*force
    root = brentq(mismatch, 0., 5., xtol=1e-14)
    mu = root/AU
    data = []
    for br in (1.6, 2., 4., 8., 16.):
        b = br*RS
        light = ray_gradient(mu,b,z1,z2)[0]/ray_gradient(0.,b,z1,z2)[0]
        gamma_eff = 2*light/((4/3)*force_kernel(mu,AU))-1
        data.append({"b_Rsun":br,"benchmark_gamma_eff":gamma_eff})
    accelerations = [{"r_AU": r,"relative_G_to_reference":
                     force_kernel(mu,r*AU)/force_kernel(mu,AU)}
                    for r in (.387,.723,1.,1.524)]
    delays = [{"f_Hz": f,"group_delay_s_at_26Mpc":group_delay(mu,f,26e6*PC)}
              for f in (30.,100.,300.,1000.)]
    check("G1 root residual",abs(mismatch(root))<1e-12, mismatch(root))
    check("positive sphere factor at root",source_yukawa(mu,AU,RS)>0,
          source_yukawa(mu,AU,RS))
    return {"schema":1,"status":"conditional geometry benchmark; no likelihood or audit status",
            "mu_AU":root,"mu_per_m":mu,"lambda_m":1/mu,
            "cutoff_f_Hz":mu*C/(2*math.pi),"light_shape":data,
            "force_shape":accelerations,"propagation":delays,"checks":checks,
            "total_pass":sum(c["pass"] for c in checks),
            "total_fail":sum(not c["pass"] for c in checks),
            "runner_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == '__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);a=p.parse_args()
    result=run();body=json.dumps(result,indent=2)+"\n"
    if a.output:
        a.output.write_text(body)
    print(body,end='')
    print(f"TOTAL: PASS={result['total_pass']} FAIL={result['total_fail']}")
    raise SystemExit(bool(result['total_fail']))
