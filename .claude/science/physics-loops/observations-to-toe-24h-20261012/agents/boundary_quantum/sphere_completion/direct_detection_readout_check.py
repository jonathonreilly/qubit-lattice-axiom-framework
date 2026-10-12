#!/usr/bin/env python3
"""Exact prospective all-trial loss budgets; fixed inputs, no observed efficiency."""
import hashlib
import json
import math
import time
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
RT = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT = RT/'quantum'/'detection_readout'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_rat(d):
    return F(int(d['numerator']), int(d['denominator']))


def rat(x):
    with localcontext() as c:
        c.prec = 35
        value = str(Decimal(x.numerator)/Decimal(x.denominator))
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator), 'decimal': value}


def root_interval(x):
    scale = 10**30
    r = math.isqrt(x.numerator*scale*scale//x.denominator)
    low, high = F(r, scale), F(r+1, scale)
    assert low*low <= x < high*high
    return low, high


def main():
    assert time.time() < json.loads((RT/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((RT/n).exists() for n in ('STOP_REQUESTED.json', 'USER_STOP_REQUESTED.json', 'STOP_REQUESTED', 'USER_STOP_REQUESTED'))
    frozen = json.loads((OUT/'FREEZE.json').read_text())
    for name, digest in frozen['sources'].items():
        path = Path(name)
        if not path.is_absolute():
            path = HERE/path
        assert sha(path) == digest
    execution = {'script_sha256': sha(Path(__file__)), 'freeze_sha256': sha(OUT/'FREEZE.json')}
    with (OUT/'EXECUTION_SOURCE_v1.json').open('x') as f:
        json.dump(execution, f, indent=2)
    reflection = json.loads((HERE/'DIRECT_REFLECTION_RESULT.json').read_text())
    ideal = next(r for r in reflection['witnesses'] if read_rat(r['V']) == F(19, 20))
    ideal_gap = read_rat(ideal['B_interval'][0])-1
    angular = json.loads((RT/'quantum/angular_robustness/RESULTS_v1.json').read_text())
    perturbed = next(r for r in angular['rows'] if r['angle_per_side_rad'] == '1/1000' and r['extra_candidate_error'] == '1/1000')
    budgets = [('ideal', ideal_gap), ('angle_and_candidate_error', read_rat(perturbed['effective_gap_lower']))]
    j = F(111, 20)
    rows, thresholds = [], []
    for label, gap in budgets:
        blo = 1+gap
        random_threshold = root_interval(1/blo)
        rl, rh = root_interval(1+2*gap)
        constant_threshold = (2/(1+rh), 2/(1+rl))
        thresholds.append({'budget': label, 'random_assignment_eta_threshold': [rat(x) for x in random_threshold],
                           'constant_plus_eta_threshold': [rat(x) for x in constant_threshold]})
        for eta_text in frozen['equal_efficiencies']:
            eta = F(eta_text)
            for assignment in frozen['assignments']:
                loss_offset = (1-eta)**2 if assignment == 'constant_plus_one_fair_candidate' else F(0)
                effective = eta*eta*blo-loss_offset-1
                n = None
                if effective > 0:
                    bound = 40*j*j/(effective*effective)
                    n = -(-bound.numerator//bound.denominator)
                    assert n-1 < bound <= n
                rows.append({'budget': label, 'eta_per_side': eta_text, 'assignment': assignment,
                             'gap_lower': rat(effective), 'N_for_each_error_at_most_1_percent': n})
    assert rows[0]['N_for_each_error_at_most_1_percent'] == 469373
    result = {**execution, 'thresholds': thresholds, 'rows': rows,
              'scope': 'Stipulated independent-loss candidate model; all heralded trials included. No experimental data. Deterministic assignment additionally requires fair candidate marginals.'}
    with (OUT/'RESULTS_v1.json').open('x') as f:
        json.dump(result, f, indent=2)
    for t in thresholds:
        print(t['budget'], 'random eta threshold <=', t['random_assignment_eta_threshold'][1]['decimal'],
              'constant-plus eta threshold <=', t['constant_plus_eta_threshold'][1]['decimal'])
    for r in rows:
        print(r['budget'], r['eta_per_side'], r['assignment'], r['gap_lower']['decimal'], r['N_for_each_error_at_most_1_percent'])


if __name__ == '__main__':
    main()
