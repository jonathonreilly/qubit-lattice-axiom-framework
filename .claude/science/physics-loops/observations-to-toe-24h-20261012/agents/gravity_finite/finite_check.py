#!/usr/bin/env python3
"""Independent finite positive-field construction; no parent code imports."""
import os

for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
              "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_name] = "1"

import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import expm
from scipy.special import beta, gammainc, gammaln, roots_genlaguerre

CAMPAIGN = Path("/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012")
DEFAULT_OUT = CAMPAIGN / "gravity_measurements" / "finite" / "finite_results.json"


def guard():
    stop_markers = list(CAMPAIGN.glob("*STOP_REQUESTED*"))
    if stop_markers:
        raise SystemExit(f"Stop marker present: {stop_markers[0].name}")
    deadline = json.loads((CAMPAIGN / "DEADLINE.json").read_text())
    if datetime.now(timezone.utc).timestamp() >= deadline["deadline_epoch"]:
        raise SystemExit("Campaign deadline reached")


def rule(s, n):
    x, raw = roots_genlaguerre(n, s - 1)
    w = raw * math.exp(-gammaln(s))
    assert np.all(x > 0) and np.all(w > 0)
    assert abs(float(w.sum()) - 1) < 3e-14
    return x, w


def responses(s, t, x, w):
    y = (1 + t) ** (-s)
    h = y * (1 + s * t / (1 + t))
    v = w * np.exp(-t * x)
    return y, h, float(v.sum()), float(np.dot(v, 1 + t * x))


def positive_exp(logv):
    return float(math.exp(logv)) if logv < 709 else float("inf")


def bounds(s, n, t):
    if t == 0:
        return {k: 0.0 for k in ("direct_y", "direct_h", "birth_y", "birth_h",
                                "relative_y", "relative_h")}
    logc = gammaln(n + 1) + gammaln(n + s) - gammaln(s) - gammaln(2*n + 1)
    loga = gammaln(n + s) - gammaln(s) - gammaln(n)
    d_y = positive_exp(logc + 2*n*math.log(t))
    d_h = positive_exp(logc + math.log(2*n-1) + 2*n*math.log(t))
    b_y = positive_exp(loga + math.log(t) + (2*n-2)*math.log(t/(t+2)))
    b_h = positive_exp(loga + math.log(t) + math.log1p(t*(n+s*t))
                       + (2*n-2)*math.log(t/(t+2)))
    y = (1+t)**(-s)
    h = y * (1+s*t/(1+t))
    return dict(direct_y=d_y, direct_h=d_h, birth_y=b_y, birth_h=b_h,
                relative_y=min(d_y, b_y)/y, relative_h=min(d_h, b_h)/h)


def cdf_delta(s, x, w):
    cumulative = np.cumsum(w)
    left = np.r_[0.0, cumulative[:-1]]
    f = gammainc(s, x)
    return float(max(np.max(abs(f-left)), np.max(abs(f-cumulative))))


def continuum_noise(s, u, b):
    # ell*j(omega), u=ell*omega, b=a/ell. QAWS integrates both endpoint powers.
    coefficient = u**(s+1)*math.exp(-gammaln(s))/(4*math.pi**2)
    value, error = quad(lambda z: math.sqrt(1+z)*math.exp(-u*z-b*b*u*u*(1-z*z)),
                        0, 1, weight="alg", wvar=(s-1, .5),
                        epsabs=2e-13, epsrel=2e-13, limit=200)
    return coefficient*value, coefficient*error


def finite_noise(u, b, x, w):
    keep = x < u
    k = np.sqrt(u*u-x[keep]**2)
    return float(np.dot(w[keep], k*np.exp(-b*b*k*k))/(4*math.pi**2))


def variation(u, b):
    if b == 0:
        return u
    g = u*math.exp(-b*b*u*u)
    return g if u <= 1/(math.sqrt(2)*b) else 2/(b*math.sqrt(2*math.e))-g


def cdf_noise_integral(s, u, b, x, w, absolute):
    cumulative = np.r_[0., np.cumsum(w)]
    points = sorted([0., u] + [math.sqrt(u*u-z*z) for z in x if z < u])
    if b > 0 and 1/(math.sqrt(2)*b) < u:
        points.append(1/(math.sqrt(2)*b))
        points.sort()

    def f(k):
        mass = math.sqrt(max(0., u*u-k*k))
        idx = int(np.searchsorted(x, mass, side="right"))
        difference = float(gammainc(s, mass))-float(cumulative[idx])
        slope = math.exp(-b*b*k*k)*(1-2*b*b*k*k)
        return abs(difference)*abs(slope) if absolute else difference*slope

    value = error = 0.
    for lo, hi in zip(points[:-1], points[1:]):
        q, e = quad(f, lo, hi, epsabs=1e-13, epsrel=1e-11, limit=200)
        value += q
        error += e
    return value/(4*math.pi**2), error/(4*math.pi**2)


def birth_check(s, n, t):
    # Independent Markov generator, not a Laguerre-eigensystem implementation.
    generator = np.zeros((n, n))
    for k in range(n):
        generator[k, k] = -(2*k+s)
        if k+1 < n:
            generator[k, k+1] = k+s
        if k:
            generator[k, k-1] = k
    x, w = rule(s, n)
    y, h, yn, hn = responses(s, t, x, w)
    killed_return = float(expm(t*generator)[0, 0])
    a = math.exp(gammaln(s+n)-gammaln(s)-gammaln(n))

    def pn(v):
        return v**n/(1+v)**(n+s)

    def dpn(v):
        return v**(n-1)*(n-s*v)/(1+v)**(n+s+1)

    def hit(u):
        return (n-1+s)*float(expm(u*generator)[0, n-1])

    def hit_upper(u):
        return a*u**(n-1)/(1+u)**(n-1+s)

    ey_int = quad(lambda u: hit(u)*pn(t-u), 0, t, epsabs=1e-13)[0]
    eh_int = quad(lambda u: hit(u)*(pn(t-u)-t*dpn(t-u)),
                  0, t, epsabs=1e-13)[0]
    by = quad(lambda u: hit_upper(u)*pn(t-u), 0, t, epsabs=1e-13)[0]
    bh = quad(lambda u: hit_upper(u)*abs(pn(t-u)-t*dpn(t-u)),
              0, t, epsabs=1e-13, limit=200)[0]
    assert abs(killed_return-yn) < 2e-13
    assert abs(ey_int-(y-yn)) < 2e-13
    assert abs(eh_int-(h-hn)) < 2e-13
    assert ey_int <= by+2e-13 and abs(eh_int) <= bh+2e-13
    return dict(s=s, n=n, t=t, spectral_sum=yn, markov_return=killed_return,
                potential_error=y-yn, first_hit_potential_error=ey_int,
                force_error=h-hn, first_hit_force_error=eh_int,
                integral_bound_y=by, integral_bound_h=bh, bounds=bounds(s,n,t))


def high_precision_example():
    # A fresh 70-digit symmetric Jacobi diagonalization, independent of SciPy roots.
    mp.mp.dps = 70
    n, s, t = 16, mp.mpf(1), mp.mpf(1)
    jacobi = mp.matrix(n)
    for k in range(n):
        jacobi[k, k] = 2*k+s
        if k+1 < n:
            jacobi[k, k+1] = jacobi[k+1, k] = -mp.sqrt((k+1)*(k+s))
    nodes, vectors = mp.eigsy(jacobi)
    weights = [vectors[0, k]**2 for k in range(n)]
    yn = mp.fsum(weights[k]*mp.exp(-t*nodes[k]) for k in range(n))
    hn = mp.fsum(weights[k]*(1+t*nodes[k])*mp.exp(-t*nodes[k]) for k in range(n))
    y = (1+t)**(-s)
    h = y*(1+s*t/(1+t))
    return dict(s=1, n=n, t=1, digits=70,
                minimum_node=mp.nstr(nodes[0], 55),
                potential_error=mp.nstr(y-yn, 55),
                potential_relative_error=mp.nstr((y-yn)/y, 55),
                force_error=mp.nstr(h-hn, 55),
                force_relative_error=mp.nstr((h-hn)/h, 55),
                weights_sum=mp.nstr(mp.fsum(weights), 55),
                bounds=bounds(1,n,1))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    guard()
    output = dict(
        generated_utc=datetime.now(timezone.utc).isoformat(),
        method="independent Laguerre quadrature + killed Markov chain + CDF integration",
        dimensionless_convention="t=r/ell; u=ell*omega; b=a/ell; noise columns are ell*j",
        versions=dict(numpy=np.__version__, scipy=scipy.__version__, mpmath=mp.__version__),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        birth_checks=[birth_check(.6,4,2.), birth_check(2.5,6,4.), birth_check(1.,1,.1)],
        high_precision=high_precision_example(),
        windows=[], noise=[], refined_noise=[], moment_checks=[], cdf_convergence=[])

    for s in (.3, 1., 2.5):
        for n in (4, 8, 16, 32, 64, 128):
            guard()
            x, w = rule(s,n)
            delta = cdf_delta(s,x,w)
            moment_errors = [abs(float(np.dot(w,x**k))*math.exp(gammaln(s)-gammaln(s+k))-1)
                             for k in range(min(2*n,21))]
            output["moment_checks"].append(dict(s=s,n=n,max_relative_error=max(moment_errors),
                                                degrees_checked=len(moment_errors)-1))
            output["cdf_convergence"].append(dict(s=s,n=n,delta=delta,minimum_node=float(x[0]),
                                                 maximum_weight=float(w.max())))
            for tmax in (1.,10.):
                points = np.r_[0., np.geomspace(1e-5,tmax,350)]
                errors_y, errors_h = [], []
                for t in points:
                    y,h,yn,hn = responses(s,float(t),x,w)
                    errors_y.append(abs(y-yn)/y)
                    errors_h.append(abs(h-hn)/h)
                certificate = bounds(s,n,tmax)
                assert max(errors_y) <= certificate["relative_y"]+2e-12
                assert max(errors_h) <= certificate["relative_h"]+2e-12
                output["windows"].append(dict(s=s,n=n,tmax=tmax,
                    sampled_max_relative_y=max(errors_y), sampled_max_relative_h=max(errors_h),
                    sampled_points=len(points), certificate=certificate,
                    floating_point_floor="errors around 1e-14 are not resolved by this scan"))
            for u in (.01,.1,.3,1.,3.):
                b=.7
                j, err = continuum_noise(s,u,b)
                jn = finite_noise(u,b,x,w)
                bj = delta*variation(u,b)/(4*math.pi**2)
                assert abs(j-jn) <= bj+2e-13
                output["noise"].append(dict(s=s,n=n,u=u,b=b,continuum=j,
                    continuum_quad_error=err,finite=jn,relative_error=abs(j-jn)/j,
                    absolute_bound=bj,below_first_threshold=bool(u<=x[0])))

    x,w = rule(1.,16)
    for u in (.01,.1,.3,1.,3.):
        j,_=continuum_noise(1.,u,.7)
        jn=finite_noise(u,.7,x,w)
        signed,err=cdf_noise_integral(1.,u,.7,x,w,False)
        refined,berr=cdf_noise_integral(1.,u,.7,x,w,True)
        assert abs(signed-(j-jn)) < 2e-12
        assert abs(j-jn) <= refined+2e-12
        output["refined_noise"].append(dict(s=1.,n=16,u=u,b=.7,actual_error=j-jn,
            signed_cdf_integral=signed,signed_quad_error=err,refined_bound=refined,
            refined_quad_error=berr,relative_error=abs(j-jn)/j,
            relative_refined_bound=refined/j,
            relative_global_bound=cdf_delta(1.,x,w)*variation(u,.7)/(4*math.pi**2*j)))

    output["low_frequency_check"] = []
    for s in (.3,1.,2.5):
        u=1e-5
        j,_=continuum_noise(s,u,.7)
        leading=u**(s+1)*beta(s/2,1.5)*math.exp(-gammaln(s))/(8*math.pi**2)
        output["low_frequency_check"].append(dict(s=s,u=u,ratio=j/leading))
    # An explicit simultaneous window certificate, not a fitted physical scale.
    s,n,b,ulo,umax,tmax=1.,128,.1,4.,5.,10.
    x,w=rule(s,n)
    delta=cdf_delta(s,x,w)
    noise_relative_certificate=(2*delta*variation(umax,b)*math.exp(b*b*umax*umax)
                                /(math.sqrt(3)*ulo*float(gammainc(s,ulo/2))))
    output["joint_example"]=dict(s=s,n=n,b=b,frequency_band_u=[ulo,umax],
        radial_window_t=[0.,tmax],minimum_node=float(x[0]),cdf_delta=delta,
        uniform_relative_noise_certificate=noise_relative_certificate,
        uniform_static_certificates=bounds(s,n,tmax),
        interpretation="analytic formulas evaluated in floating point; no empirical parameter selection")
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,indent=2,allow_nan=False)+"\n")
    print(json.dumps(dict(output=str(args.output),birth_checks=len(output["birth_checks"]),
                         window_checks=len(output["windows"]),noise_checks=len(output["noise"]),
                         high_precision=output["high_precision"]),indent=2))


if __name__ == "__main__":
    main()
