#!/usr/bin/env python3
"""Independent source-divergence Green controls; no author helper imports."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import datetime
import hashlib
import json
import math
from pathlib import Path
import time
from scipy.integrate import quad

ROOT = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT = ROOT/'galaxy_response/qumond_disk/independent_direct_review'


def guard():
    assert time.time() < json.loads((ROOT/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((ROOT/n).exists() for n in
                   ('STOP_REQUESTED.json', 'USER_STOP_REQUESTED', 'STOP_CAMPAIGN.json'))


def build():
    guard()
    radii = [0.2, 0.5, 1.0, 2.0, 5.0, 10.0]
    rows = []
    # A_r = alpha r^(ell-1) exp(-r) P_ell(c),
    # A_theta = beta r^(ell-1) exp(-r) partial_theta P_ell(c).
    # Differentiate the source analytically, then solve Poisson with its Green
    # function. This expectation does not use the author's S/T representation,
    # log recurrence, angular quadrature, special-function fixture or helpers.
    for ell, alpha, beta in [(2, 1., 0.), (2, 0., 1.), (4, 1., -0.2)]:
        expected, errors = [], []
        p_at_zero = (-1)**(ell//2)*math.comb(ell, ell//2)/2**ell
        def source(r):
            return (alpha*(ell+1-r)-ell*(ell+1)*beta)*r**(ell-2)*math.exp(-r)
        for radius in radii:
            inner, ei = quad(lambda t: t**(ell+2)*source(t), 0., radius,
                             epsabs=2e-13, epsrel=2e-13)
            outer, eo = quad(lambda t: t**(1-ell)*source(t), radius, math.inf,
                             epsabs=2e-13, epsrel=2e-13)
            # Derivative of -[r^(-ell-1) I + r^ell J]/(2ell+1).
            radial = ((ell+1)*radius**(-ell-2)*inner
                      -ell*radius**(ell-1)*outer)/(2*ell+1)
            expected.append(p_at_zero*radial)
            errors.append(abs(p_at_zero)*((ell+1)*radius**(-ell-2)*ei
                                         +ell*radius**(ell-1)*eo)/(2*ell+1))
        rows.append({'ell':ell, 'alpha':alpha, 'beta':beta, 'R':radii,
                     'expected_midplane':expected, 'quad_error_estimate':errors})
    # Independently integrate the vertical source, including the normal sign.
    vertical = []
    for h, k, z in [(.3, .2, 0.), (.3, 1/.3, .3), (.3, 1/.3*(1+1e-9), .9),
                    (1., 3., 2.), (1., .02, 10.), (.3, 100., 0.001)]:
        def integrand(v, derivative):
            value = math.exp(-abs(v)/h-k*abs(z-v))/(2*h)
            return value * (1 if z > v else -1) if derivative else value
        vals = [sum(quad(lambda v: integrand(v, derivative), a, b,
                         epsabs=1e-13, epsrel=1e-12)[0]
                    for a, b in [(-math.inf, 0.), (0., z), (z, math.inf)])
                for derivative in (False, True)]
        vertical.append({'h':h, 'k':k, 'z':z, 'Z':vals[0], 'V':vals[1]})
    return {'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'method':'Adaptive quadrature of analytic source H; derivative of Green solution',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'projection_controls':rows, 'vertical_controls':vertical}


if __name__ == '__main__':
    result = build()
    path = OUT/'independent_fixture_v1.json'
    with path.open('x') as file:
        json.dump(result, file, indent=2)
        file.write('\n')
    print(json.dumps(result, indent=2))
