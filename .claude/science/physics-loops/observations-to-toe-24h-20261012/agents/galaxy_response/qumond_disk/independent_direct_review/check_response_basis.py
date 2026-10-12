#!/usr/bin/env python3
"""Independent solar log-ramp quadrature; no empirical input or author helpers."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import datetime
import hashlib
import json
import math
from pathlib import Path
import resource
import time
import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad

ROOT = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT = ROOT/'galaxy_response/qumond_disk/independent_direct_review'
HERE = Path(__file__).parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def guard():
    assert time.time() < json.loads((ROOT/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((ROOT/name).exists() for name in
                   ('STOP_REQUESTED.json', 'USER_STOP_REQUESTED', 'STOP_CAMPAIGN.json'))


def reference(lo, hi):
    """55-digit non-rationalized W; integrate in log acceleration."""
    mp.mp.dps = 55
    a, b = mp.mpf(str(lo)), mp.mpf(str(hi))
    def weight_log(u):
        s = mp.exp(u)
        plus = 4*s**4+2*s**3+3*s*s+2*s+4
        minus = 4*s**4-2*s**3+3*s*s-2*s+4
        return mp.mpf(8)/105*(minus*mp.sqrt(1+s)-plus*mp.sqrt(abs(1-s)))
    edges = [mp.log(a), mp.log(b)]
    if a < 1 < b:
        edges.insert(1, mp.mpf(0))
    value = mp.mpf(9)/(8*mp.log(b/a))*mp.quad(weight_log,edges)
    return value


def density_changed_order(lo, hi, order):
    """Hessian source integral in (log q, sqrt(w^2)), rather than (w,c).

    eta=1, s=q, t=w^2, c=(t^2+1-s^2)/(2t).
    dw dc = s/(2 t^(3/2)) ds dt, |1-s|<t<1+s.
    F = -3/(4 log(h/l)) integral ds/s integral dt/sqrt(t)
        P2(c) [s^2-3(t-c)^2].  Put t=z^2 and s=exp(u).
    The derivative support alone fixes both integrations; there is no
    author's knot splitter, response helper, kernel, or log-cell recurrence.
    """
    x, weight = leggauss(order)
    def at_log(u):
        s = math.exp(u)
        lower, upper = math.sqrt(abs(1-s)), math.sqrt(1+s)
        z = lower+(upper-lower)*(x+1)/2
        t = z*z
        c = (t*t+(1-s)*(1+s))/(2*t)
        integrand = (.5*(3*c*c-1))*(s*s-3*(t-c)**2)
        return (upper-lower)/2*float(np.dot(weight,integrand))
    edges = sorted(set([math.log(lo),math.log(hi)]+([0.] if lo<1<hi else [])))
    value, error = 0., 0.
    for a,b in zip(edges[:-1],edges[1:]):
        v,e = quad(at_log,a,b,epsabs=3e-14,epsrel=2e-11,limit=200)
        value += v;error += e
    scale = -3/(2*math.log(hi/lo))
    return scale*value,abs(scale)*error


def main():
    guard()
    started = time.time()
    authored = json.loads((ROOT/'gravity/direct_response_basis_v2.json').read_text())
    source = HERE/'followup_snapshot_direct_response_basis.py'
    assert sha(source) == authored['source_sha256']
    # The author's functions are subjects only, used after the independent
    # expectation and density integration for each row have been completed.
    subject = {'__name__':'basis_review_subject', '__file__':str(source)}
    exec(compile(source.read_text(),str(source),'exec'),subject)
    intervals = [(r['low_over_external'],r['high_over_external'])for r in authored['rows']]
    intervals += [(.37,1.63),(2.3,9.7)]
    rows = []
    for lo,hi in intervals:
        guard()
        ref = reference(lo,hi)
        expected = float(ref)
        estimates = []
        for order in (32,64,128):
            value,error = density_changed_order(lo,hi,order)
            estimates.append({'order':order,'F':value,'estimated_absolute_error':error,
                              'relative_to_reference':abs(value-expected)/expected})
        authored_positive = subject['positive_integral'](lo,hi)[0]
        authored_ibp = subject['poisson_integral'](lo,hi,1.,96,False)
        authored_density = subject['poisson_integral'](lo,hi,1.,96,True)
        row = {'lo_over_external':lo,'hi_over_external':hi,'reference_55_digit':mp.nstr(ref,45),
               'independent_density':estimates,
               'author_positive':authored_positive,'author_ibp':authored_ibp,
               'author_density':authored_density,
               'max_author_relative':max(abs(x-expected)/expected for x in
                                         [authored_positive,authored_ibp,authored_density])}
        assert expected > 0
        assert estimates[-1]['relative_to_reference'] < 2e-8
        assert row['max_author_relative'] < 2e-8
        rows.append(row)
    result = {'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'script_sha256':sha(Path(__file__)),'author_source_sha256':sha(source),
              'authored_receipt_sha256':sha(ROOT/'gravity/direct_response_basis_v2.json'),
              'rows':rows,'passed':True,'elapsed_seconds':time.time()-started,
              'max_rss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              'empirical_inputs':'none; only dimensionless synthetic transition intervals',
              'independent_methods':'55-digit square-root-difference primitive in log acceleration; independently transformed source Hessian density integral'}
    with (OUT/'response_basis_check.json').open('x') as stream:
        json.dump(result,stream,indent=2);stream.write('\n')
    for row in rows:
        print(row['lo_over_external'],row['hi_over_external'],row['reference_55_digit'],
              'independent_error',row['independent_density'][-1]['relative_to_reference'],
              'author_error',row['max_author_relative'])
    print('elapsed_seconds',result['elapsed_seconds'],'max_rss',result['max_rss'])


if __name__ == '__main__':
    main()
