#!/usr/bin/env python3
"""Registered exact algebra only; no interacting Yang--Mills integration."""
from fractions import Fraction as F
from pathlib import Path
import datetime
import hashlib
import json
import os
import re
import resource
import subprocess
import sys

HERE = Path(__file__).resolve().parent
NAMES = ('h', 'b0', 'b1', 'b2', 'u', 'ell', 'a4', 'a2', 'z', 'r', 'c', 'd')
ZERO = (0,) * len(NAMES)
RECORDS = []
GUARDS = []
THREADS = ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
           'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')


class P:
    """Finite Laurent polynomials over Q; no symbolic-library assumptions."""
    def __init__(self, terms=0):
        if isinstance(terms, P):
            terms = terms.t
        elif not isinstance(terms, dict):
            terms = {ZERO: F(terms)}
        self.t = {e: F(a) for e, a in terms.items() if a}

    def __add__(self, other):
        out = dict(self.t)
        for e, a in P(other).t.items():
            out[e] = out.get(e, F(0)) + a
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -a for e, a in self.t.items()})

    def __sub__(self, other):
        return self + -P(other)

    def __rsub__(self, other):
        return P(other) + -self

    def __mul__(self, other):
        out = {}
        for e, a in self.t.items():
            for f, b in P(other).t.items():
                g = tuple(i+j for i, j in zip(e, f))
                out[g] = out.get(g, F(0)) + a*b
        return P(out)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = P(1)
        for _ in range(n):
            out = out*self
        return out

    def __eq__(self, other):
        return self.t == P(other).t

    def diff(self, name):
        j = NAMES.index(name)
        out = {}
        for e, a in self.t.items():
            if e[j]:
                f = list(e)
                f[j] -= 1
                out[tuple(f)] = a*e[j]
        return P(out)

    def truncate(self, max_h):
        return P({e: a for e, a in self.t.items() if e[0] <= max_h})

    def coeff_h(self, n):
        out = {}
        for e, a in self.t.items():
            if e[0] == n:
                out[(0,)+e[1:]] = a
        return P(out)

    def substitute(self, name, value):
        j = NAMES.index(name)
        out = P(0)
        for e, a in self.t.items():
            assert e[j] >= 0
            f = list(e)
            power, f[j] = f[j], 0
            out += P({tuple(f): a}) * P(value)**power
        return out


def mon(**powers):
    return P({tuple(powers.get(n, 0) for n in NAMES): F(1)})


def inverse(p, order):
    v = p-1
    assert v.coeff_h(0) == 0
    assert all(e[0] >= 1 for e in v.t)
    term, result = P(1), P(1)
    for _ in range(order):
        term = (-term*v).truncate(order)
        result += term
    return result.truncate(order)


def check(name, condition, **details):
    RECORDS.append(dict(name=name, passed=bool(condition), **details))
    if not condition:
        raise AssertionError(name)


def guard():
    data = subprocess.check_output(['/usr/bin/memory_pressure', '-Q'], text=True)
    free = int(re.search(r'free percentage:\s*(\d+)%', data).group(1))
    loads = os.getloadavg()
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        peak *= 1024
    g = dict(free_percent=free, loads=loads, peak_rss_bytes=peak)
    GUARDS.append(g)
    assert free >= 30 and max(loads) < 8 and peak < 800*1024**2, g


def run_checks():
    h, b0, b1, b2, u, ell, a4, a2, z, r, c, d = (mon(**{n: 1}) for n in NAMES)
    # Exact coefficients, with N and pi factors kept symbolic outside Q.
    check('coupling_conversion', 2*F(11, 48) == F(11, 24))
    check('inverse_coupling_slope', 2*F(11, 24) == F(11, 12))
    check('mutation_missing_factor_two', F(11, 24) != F(11, 12))

    beta = -b0*h**3-b1*h**5-b2*h**7
    gamma = beta.diff('h')-3*beta*mon(h=-1)
    check('clover_gamma_no_h2', gamma.coeff_h(2) == 0)
    check('clover_gamma_h4', gamma.coeff_h(4) == -2*b1)
    check('clover_gamma_h6', gamma.coeff_h(6) == -4*b2)
    beta_u = 2*b0+2*b1*mon(u=-1)+2*b2*mon(u=-2)
    gamma_u = beta_u.diff('u')
    changed = {}
    for e, a in gamma_u.t.items():
        f = list(e)
        f[0] += -2*f[4]
        f[4] = 0
        changed[tuple(f)] = a
    check('independent_u_derivative', P(changed) == gamma)
    gamma_can = beta.diff('h')-beta*mon(h=-1)
    check('canonical_gamma', gamma_can == -2*b0*h**2-4*b1*h**4-6*b2*h**6)
    check('canonical_rescaling_route', gamma_can == gamma+2*beta*mon(h=-1))
    check('mutation_canonical_used_for_clover', gamma_can != gamma)
    ward = -beta*mon(b0=-1, h=-3)
    check('ward_differential_identity', beta*ward.diff('h') == gamma*ward)
    check('ward_first_coefficient', ward.coeff_h(2) == b1*mon(b0=-1))

    for n, a in ((2, a2), (4, a4)):
        correlator = h**(2*n)*(1+h**2*(a+2*n*b0*ell))
        rg = correlator.diff('ell')+beta*correlator.diff('h')+n*gamma*correlator
        check(f'rg_log_order_{n}', rg.coeff_h(2*n+2) == 0)
        wrong = h**(2*n)*(1+h**2*(a-2*n*b0*ell))
        wrong_rg = wrong.diff('ell')+beta*wrong.diff('h')+n*gamma*wrong
        check(f'mutation_log_sign_{n}', wrong_rg.coeff_h(2*n+2) != 0)

    p = 1+h**2*(a4+8*b0*ell)
    q = 1+h**2*(a2+4*b0*ell)
    ratio = (p*inverse(q, 4)**2).truncate(4)
    check('ratio_first_coefficient', ratio.coeff_h(2) == a4-2*a2)
    check('ratio_common_log_zero', ratio.coeff_h(2).diff('ell') == 0)
    wrong_ratio = (p*inverse(q, 4)).truncate(4)
    check('mutation_missing_denominator_square', wrong_ratio.coeff_h(2).diff('ell') != 0)

    common = 1+z*h**2+r*h**4
    p_common = (p*common**4).truncate(4)
    q_common = (q*common**2).truncate(4)
    ratio_common = (p_common*inverse(q_common, 4)**2).truncate(4)
    check('finite_factor_cancels_through_h4', ratio_common == ratio)
    p_ward = (p*ward**4).truncate(4)
    q_ward = (q*ward**2).truncate(4)
    check('ward_factor_cancels_through_h4', (p_ward*inverse(q_ward, 4)**2).truncate(4) == ratio)
    wrong_q_ward = (q*ward).truncate(4)
    check('mutation_single_ward_denominator',
          (p_ward*inverse(wrong_q_ward, 4)**2).truncate(2) != ratio.truncate(2))
    base_ratio = 1+c*h**2+d*h**4
    transformed = base_ratio.substitute('h', h+r*h**3).truncate(4)
    check('coupling_scheme_first_invariant', transformed.coeff_h(2) == c)
    check('coupling_scheme_next_shift', transformed.coeff_h(4) == d+2*r*c)
    next_ratio = base_ratio+2*b0*c*ell*h**4
    check('ratio_next_log', (next_ratio.diff('ell')+beta*next_ratio.diff('h')).truncate(4) == 0)

    check('smooth_A_enclosure', F(3, 2) < F(9971, 6480) < F(10309, 6480) < F(5, 3))
    check('smooth_B_enclosure', 11 < 12*F(2500, 2501)**8 < 12*F(2500, 2499)**8 < 13)
    check('smooth_ratio_lower', F(3, 2)/13**2 == F(3, 338))
    check('smooth_ratio_upper', F(5, 3)/11**2 == F(5, 363))
    factors = [(1+x)/(1+y)**2 for x in (F(-1, 4), F(1, 4))
               for y in (F(-1, 4), F(1, 4))]
    check('positivity_rectangle', min(factors) == F(12, 25) and max(factors) == F(20, 9))
    check('witness_lower_margin', F(12, 25)*F(3, 338) == F(18, 4225))
    check('error_budget', F(1, 16)+F(1, 16)+F(1, 8) == F(1, 4))
    for sign in (-1, 1):
        delta = sign*F(1, 16)-F(1, 16)-F(1, 8)
        check(f'correction_sign_{sign}', 1+delta >= F(3, 4))
    cutoff, x = 10**8, F(1, 100)
    counterexample = 1-2*cutoff*x*x/(1+cutoff*x*x)
    check('mutation_no_uniform_remainder', counterexample < 0,
          example=str(counterexample), scope='scalar logical counterexample, not a YM law')

    for j, scale in enumerate((F(1), F(2), F(7, 3))):
        for k, fraction in enumerate((F(0), F(1, 4), F(1, 2))):
            E = scale*fraction
            for sign in (-1, 1):
                v = sign*E
                error = abs(1/(scale+v)-1/scale)
                check(f'reciprocal_{j}_{k}_{sign}', error <= 2*E/(scale*scale))
    check('mutation_drop_reciprocal_two', abs(1/(F(1)-F(1, 2))-1) > F(1, 2))


def main():
    report = dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  scope='exact algebra only; actual YM coefficient and remainder OPEN',
                  passed=False, checks=RECORDS, guards=GUARDS)
    try:
        assert os.environ.get('K4CORR_WATCHDOG') == '1'
        assert all(os.environ.get(t) == '1' for t in THREADS)
        nice = os.getpriority(os.PRIO_PROCESS, 0)
        assert nice >= 10
        report.update(nice=nice, threads={t: os.environ[t] for t in THREADS})
        criteria = HERE/'k4corr_criteria.md'
        assert criteria.stat().st_mtime_ns < Path(__file__).stat().st_mtime_ns
        report['criteria_sha256'] = hashlib.sha256(criteria.read_bytes()).hexdigest()
        guard()
        run_checks()
        guard()
        report['passed'] = True
    except BaseException as exc:
        report['failure'] = repr(exc)
    report['assertion_count'] = len(RECORDS)
    print(json.dumps(report, indent=2))
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
