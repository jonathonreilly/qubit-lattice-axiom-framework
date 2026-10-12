#!/usr/bin/env python3
"""Fixed prospective error budgets; exact rational propagation, no measured data."""
import argparse
import hashlib
import json
import math
import time
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
RT = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT = RT/'quantum'/'angular_robustness'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read_rat(d):
    return F(int(d['numerator']), int(d['denominator']))


def rat(x):
    with localcontext() as ctx:
        ctx.prec = 38
        value = str(Decimal(x.numerator)/Decimal(x.denominator))
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator), 'decimal': value}


def atan_interval(x, n):
    a = sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(n)), F(0))
    b = a+(-1)**n*x**(2*n+1)/F(2*n+1)
    return min(a, b), max(a, b)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--freeze', action='store_true')
    args = parser.parse_args()
    deadline = json.loads((RT/'DEADLINE.json').read_text())
    assert time.time() < deadline['packaging_epoch']
    assert not any((RT/p).exists() for p in ('STOP_REQUESTED.json', 'USER_STOP_REQUESTED.json', 'STOP_REQUESTED', 'USER_STOP_REQUESTED'))
    names = ['DIRECT_ANGULAR_ROBUSTNESS.md', 'direct_angular_robustness_check.py',
             'DIRECT_REFLECTION_WITNESS_V2.md', 'DIRECT_REFLECTION_RESULT.json']
    sources = {p: sha(HERE/p) for p in names}
    OUT.mkdir(parents=True, exist_ok=True)
    freeze_path = OUT/'FREEZE.json'
    if args.freeze:
        with freeze_path.open('x') as f:
            json.dump({'at': datetime.now(timezone.utc).isoformat(), 'sources': sources,
                       'equal_angle_radians': ['0', '1/2000', '1/1000', '1/500', '1/250'],
                       'candidate_absolute_correlation_error': ['0', '1/1000'],
                       'visibility': '19/20', 'data_fit': None}, f, indent=2)
        print(freeze_path)
        return
    frozen = json.loads(freeze_path.read_text())
    assert frozen['sources'] == sources
    d = json.loads((HERE/'DIRECT_REFLECTION_RESULT.json').read_text())
    v = F(frozen['visibility'])
    row = next(r for r in d['witnesses'] if read_rat(r['V']) == v)
    ideal_gap = read_rat(row['B_interval'][0])-1
    k_hi = read_rat(d['k_exact_interval'][1])
    lo5, hi5 = atan_interval(F(1, 5), 50)
    lo239, hi239 = atan_interval(F(1, 239), 12)
    pi_lo, pi_hi = 16*lo5-4*hi239, 16*hi5-4*lo239
    assert 3 < pi_lo < pi_hi < F(22, 7)
    exact_upper = 2/pi_lo+k_hi
    scaled = exact_upper*10**30
    L = F(-(-scaled.numerator//scaled.denominator), 10**30)
    assert L >= exact_upper and L-exact_upper < F(1, 10**30)
    j = read_rat(d['total_absolute_weight'])
    assert j == F(111, 20)
    rows = []
    for delta_text in frozen['equal_angle_radians']:
        delta = F(delta_text)
        for eps_text in frozen['candidate_absolute_correlation_error']:
            eps = F(eps_text)
            allowance = j*(2*v*L*delta+eps)
            gap = ideal_gap-allowance
            count = None
            if gap > 0:
                required = 40*j*j/(gap*gap)
                count = -(-required.numerator//required.denominator)
                assert count-1 < required <= count
            rows.append({'angle_per_side_rad': delta_text, 'extra_candidate_error': eps_text,
                         'B_allowance_upper': rat(allowance), 'effective_gap_lower': rat(gap),
                         'N_for_each_error_at_most_1_percent': count})
    assert rows[0]['N_for_each_error_at_most_1_percent'] == 469373
    assert all(read_rat(r['B_allowance_upper']) >= 0 for r in rows)
    limit = ideal_gap/(2*j*v*L)
    result = {'at': datetime.now(timezone.utc).isoformat(), 'sources': sources,
              'freeze_sha256': sha(freeze_path), 'L_certified_upper': rat(L),
              'ideal_gap_lower': rat(ideal_gap), 'strict_pure_angle_tolerance_rad': rat(limit),
              'rows': rows,
              'scope': 'Stipulated error examples, conditional on common local quantum maps and per-trial alternative mean. No measured calibration, apparatus performance, or empirical exclusion.'}
    assert sources == {p: sha(HERE/p) for p in names}
    with (OUT/'RESULTS_v1.json').open('x') as f:
        json.dump(result, f, indent=2)
    print('L upper', rat(L)['decimal'], 'pure angle strict threshold radians', rat(limit)['decimal'])
    for r in rows:
        print(r['angle_per_side_rad'], r['extra_candidate_error'], r['effective_gap_lower']['decimal'], r['N_for_each_error_at_most_1_percent'])


if __name__ == '__main__':
    main()
