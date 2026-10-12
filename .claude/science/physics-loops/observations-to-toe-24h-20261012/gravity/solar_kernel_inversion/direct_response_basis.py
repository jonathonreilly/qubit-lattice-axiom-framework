#!/usr/bin/env python3
"""Three solar-response calculations for a fixed monotone log-ramp basis."""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.integrate import quad
from scipy.special import roots_legendre

RUNTIME = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')


def guard():
    clock = json.loads((RUNTIME/'DEADLINE.json').read_text())
    if time.time() >= clock['packaging_epoch'] or any((RUNTIME/p).exists() for p in
        ['STOP_REQUESTED.json', 'USER_STOP_REQUESTED', 'STOP_CAMPAIGN.json']):
        raise RuntimeError('Campaign discovery window or stop marker')


def kernel(s):
    p = 4*s**4 + 2*s**3 + 3*s*s + 2*s + 4
    r = 4*s**4 - 2*s**3 + 3*s*s - 2*s + 4
    numerator = s**5*(16*s**4+12*s*s+21) if s <= 1 else 21*s**4+12*s*s+16
    return (16/105)*numerator/(r*np.sqrt(1+s)+p*np.sqrt(abs(1-s)))


def positive_integral(lo, hi):
    edges = sorted(set([lo, hi]+([1.] if lo < 1 < hi else [])))
    value, error = 0., 0.
    for left, right in zip(edges[:-1], edges[1:]):
        a, b = quad(lambda s: kernel(s)/s, left, right, epsabs=2e-13, epsrel=2e-13)
        value += a
        error += b
    return 9*value/(8*np.log(hi/lo)), 9*error/(8*np.log(hi/lo))


def poisson_integral(lo, hi, eta=1., order=64, density=False):
    """Direct w,c Green/Hessian integral, splitting at both response knots."""
    x, weight = roots_legendre(order)
    cutoff = np.sqrt(eta*(hi+1))
    edges = sorted(set([0., cutoff] +
        [np.sqrt(eta*abs(1+sign*edge)) for sign in [-1, 1] for edge in [lo, hi]] +
        [np.sqrt(eta)]))
    edges = [e for e in edges if e <= cutoff]
    total = 0.
    for a, b in zip(edges[:-1], edges[1:]):
        wnodes = (a+b)/2+(b-a)*x/2
        wweights = (b-a)*weight/2
        for w, ww in zip(wnodes, wweights):
            cedges = sorted(set([-1., 1.] +
                [float(np.clip((w**4+eta**2-(eta*edge)**2)/(2*eta*w*w), -1, 1))
                 for edge in [lo, hi]]))
            for left, right in zip(cedges[:-1], cedges[1:]):
                c = (left+right)/2+(right-left)*x/2
                cw = (right-left)*weight/2
                q = np.hypot(w*w-eta, np.sqrt(2*eta*(1-c))*w)
                if density:
                    derivative = np.zeros_like(q)
                    mask = (q > eta*lo) & (q < eta*hi)
                    derivative[mask] = -1/(q[mask]*np.log(hi/lo))
                    value = (3/2)*((3*c*c-1)/2)*derivative*(q*q-3*(w*w-eta*c)**2)*w*w/q
                else:
                    enhancement = np.clip(np.log(eta*hi/q)/np.log(hi/lo), 0, 1)
                    baseline = np.clip(np.log(eta*hi/np.hypot(w*w, eta))/np.log(hi/lo), 0, 1)
                    polynomial = w*w*(3*c*c-1)+eta*(3*c-5*c**3)
                    value = (9/4)*(enhancement-baseline)*polynomial
                total += ww*float(cw@value)
    return total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    guard()
    if args.output.exists():
        raise RuntimeError('Refusing to overwrite a computation receipt')
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    rows = []
    for lo, hi in [(.02, .2), (.5, 2.), (2., 5.), (10., 100.)]:
        positive, estimated_error = positive_integral(lo, hi)
        row = {'low_over_external': lo, 'high_over_external': hi,
               'positive_F_at_eta1': positive, 'adaptive_error_estimate': estimated_error,
               'direct_forms': []}
        for eta, order in [(1., 48), (1., 96), (.5, 96), (2., 96)]:
            guard()
            ibp = poisson_integral(lo, hi, eta, order, False)
            density = poisson_integral(lo, hi, eta, order, True)
            norm = eta**1.5
            row['direct_forms'].append({'eta': eta, 'order': order,
                'ibp_scaled': ibp/norm, 'density_scaled': density/norm,
                'largest_relative_discrepancy': max(abs(ibp/norm-positive),
                                                    abs(density/norm-positive))/positive})
        rows.append(row)
        print(json.dumps(row), flush=True)
    result = {'at': dt.datetime.now(dt.timezone.utc).isoformat(), 'source_sha256': source_hash,
              'author': 'direct work in user chat',
              'scope': 'Synthetic monotone responses; no empirical fit or uncertainty inference',
              'basis': 'N(A)=1+clip(log(A_hi/A)/log(A_hi/A_lo),0,1)', 'rows': rows}
    result['passed'] = all(z['largest_relative_discrepancy'] < 2e-8 for r in rows for z in r['direct_forms'])
    if hashlib.sha256(Path(__file__).read_bytes()).hexdigest() != source_hash:
        raise RuntimeError('Source changed during calculation')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('TOTAL:', 'PASS' if result['passed'] else 'FAIL')
    if not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
