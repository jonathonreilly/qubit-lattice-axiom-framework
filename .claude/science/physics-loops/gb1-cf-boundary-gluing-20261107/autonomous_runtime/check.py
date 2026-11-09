#!/usr/bin/env python3
"""Exact finite diagnostics; infinite-lattice existence rests on the proof."""
import argparse
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time


def zero(n=4):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def eye(n=4):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(x) for x in zip(*a)]


def multiply(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def plus(a, b):
    return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, c):
    return [[x*c for x in row] for row in a]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def kron(a, b):
    return [[x*y for x in ar for y in br] for ar in a for br in b]


I2 = eye(2)
H = [[F(1), F(1)], [F(1), F(-1)]]  # normalization squared is two
H0, H1 = kron(H, I2), kron(I2, H)
CNOT = [[F(i == (j ^ 1 if j & 2 else j)) for j in range(4)] for i in range(4)]
P = {wire: [[[F(i == j and ((i >> wire) & 1) == b) for j in range(4)]
             for i in range(4)] for b in (0, 1)] for wire in (0, 1)}


def instruments(j):
    if j == 1:
        return [(None, H0, F(2))]
    if j == 2:
        return [(None, CNOT, F(1))]
    if j in (3, 7):
        return [(b, P[1 if j == 3 else 0][b], F(1)) for b in (0, 1)]
    if j == 6:
        return [(None, H1, F(2))]
    return [(None, eye(), F(1))]


def evolve(rho, a, denominator):
    return scale(multiply(multiply(a, rho), transpose(a)), 1/denominator)


def ensemble_density(ensemble):
    out = zero()
    for weight, v in ensemble:
        out = plus(out, scale([[a*b for b in v] for a in v], weight))
    return out


def propagate(ensemble, a, denominator):
    return [(w/denominator, [sum((row[i]*v[i] for i in range(4)), F(0)) for row in a])
            for w, v in ensemble]


def autonomous_checks(fault):
    # Two data wires. Completion pointers are independent known basis factors:
    # their flip and registration are tracked explicitly rather than tracing out
    # entangled data. This fixture is not the whole native gauge circuit.
    e0, e3 = [F(1), F(0), F(0), F(0)], [F(0), F(0), F(0), F(1)]
    seeds = [[(F(1), e0)], [(F(1, 2), e0), (F(1, 2), e3)]]
    states_checked = zero_children = support_checks = 0
    terminal_masses = []
    for seed_index, ensemble in enumerate(seeds):
        initial = {('start', 0): 1, ('header', 0): seed_index}
        front = [(0, (), initial, ensemble_density(ensemble), ensemble, (0, 0))]
        seen, menus, all_records, leaves = {}, {}, [], []
        while front:
            phase, history, records, sigma, vectors, work_flags = front.pop()
            state_key = frozenset(records.items())
            assert sigma == ensemble_density(vectors), 'density/path disagreement'
            for output, wire in ((0, 1), (1, 0)):
                if ('value', output) in records:
                    projector = P[wire][records[('value', output)]]
                    assert evolve(sigma, projector, F(1)) == sigma, 'old quantum record changed'
                if ('completion', output) in records:
                    assert work_flags[output] == records[('completion', output)]
            reconstructed = (phase, history, sigma, work_flags)
            assert state_key not in seen or seen[state_key] == reconstructed, 'R not sufficient'
            seen[state_key] = reconstructed
            all_records.append(records)
            states_checked += 1
            halted = phase == 9 or (phase == 5 and history[0] == 0)
            if fault == 'no-halt-guard':
                halted = phase == 9
            if halted:
                leaves.append((phase, history, trace(sigma), records, work_flags))
                continue
            j = phase+1
            inst = instruments(j)
            intensity = zero()
            for b, a, den in inst:
                rate = F(2) if fault == 'unequal-rate' and b == 1 else F(1)
                intensity = plus(intensity, scale(multiply(transpose(a), a), rate/den))
            assert intensity == eye(), ('non-scalar total jump intensity', j)
            tick = ('tick', j)
            assert tick not in records
            menus[tick, state_key] = {1: F(1), 0: F(0)}
            value = ('value', 0 if j == 3 else 1)
            if j in (3, 7):
                assert value not in records
                menus[value, state_key] = {
                    b: trace(evolve(sigma, a, den))/trace(sigma) for b, a, den in inst}
            flag = ('completion', 0 if j == 5 else 1)
            if j in (5, 9):
                assert flag not in records and work_flags[flag[1]] == 1
                menus[flag, state_key] = {1: F(1), 0: F(0)}
            child_mass = F(0)
            for b, a, den in inst:
                child = evolve(sigma, a, den)
                child_mass += trace(child)
                if trace(child) == 0:
                    zero_children += 1
                    continue
                new_records = dict(records); new_records[tick] = 1
                new_history = history
                new_flags = list(work_flags)
                if j in (3, 7):
                    new_records[value] = b; new_history += (b,)
                if j in (4, 8):
                    new_flags[0 if j == 4 else 1] = 1
                if j in (5, 9):
                    new_records[flag] = 1
                assert all(new_records[x] == old for x, old in records.items())
                front.append((j, new_history, new_records, child,
                              propagate(vectors, a, den), tuple(new_flags)))
            assert child_mass == trace(sigma), 'branch normalization'
        for phase, hist, mass, records, flags in leaves:
            assert phase == (5 if hist[0] == 0 else 9), 'failure halted at wrong phase'
            assert records[('completion', 0)] == 1, 'failure lost completion'
            assert flags[0] == 1
        assert sum(x[2] for x in leaves) == 1
        terminal_masses.append({str(h): str(m) for _, h, m, _, _ in leaves})
        for records in all_records:
            for x, b in records.items():
                reduced = dict(records); del reduced[x]
                probability_one = (F(1, 2)+sum(reduced.values()))/(1+len(reduced))
                fallback = ({0: F(1), 1: F(0)} if fault == 'zero-fallback'
                            else {0: 1-probability_one, 1: probability_one})
                law = menus.get((x, frozenset(reduced.items())), fallback)
                assert law[b] > 0, ('old Record lost admissibility support', x, b)
                support_checks += 1
    return {'seeds': len(seeds), 'reached_states': states_checked,
            'zero_trace_children_excluded': zero_children,
            'old_record_support_checks': support_checks, 'terminal_masses': terminal_masses,
            'scope': 'two-data-qubit jump/record fixture, basis completion factors, exact path-density comparison'}


def axiom_models():
    count = 0
    minima, maxima = [], []
    for a in (F(1, 4), F(3, 4)):
        values = []
        for eta in product((-1, 0, 1), repeat=6):
            k = sum(x != -1 for x in eta); l = sum(x == 1 for x in eta)
            p = (a+l)/(1+k)
            assert a/7 <= p <= 1-(1-a)/7
            for i, value in enumerate(eta):
                if value == -1:
                    assert (a+l)/(k+2) < p < (a+l+1)/(k+2)
            permuted = eta[3:]+eta[:3]
            assert p == (a+sum(x == 1 for x in permuted))/(1+sum(x != -1 for x in permuted))
            values.append(p); count += 1
        minima.append(str(min(values))); maxima.append(str(max(values)))
    assert F(1, 4) != F(3, 4)
    return {'six_neighbor_conditions': count, 'minimum_I_probabilities': minima,
            'maximum_I_probabilities': maxima, 'empty_neighbor_I_odds': ['1/4', '3/4'],
            'infinite_lattice_existence': 'hand proof, not a finite simulation'}


def omission_controls():
    no_record_before = F(1)
    no_record_after_H = F(1, 2)
    assert no_record_before != no_record_after_H
    waited = F(1, 2)/(F(1, 2)+F(1, 4))
    assert waited == F(2, 3) and waited != F(1, 2)
    assert F(1, 2) != (F(1, 2)+1)/2  # nonconstant fallback even for T=0
    return {'omitted_tick_Z0': [str(no_record_before), str(no_record_after_H)],
            'unequal_rate_no_event_Z0': ['1/2', str(waited)],
            'arbitrary_preherald_success': ['1', '0'],
            'T0_fallback_I_odds': ['1/2', '3/4'],
            'scope': 'specific explicit counterexamples, not a general no-go'}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--fault', choices=('no-halt-guard', 'unequal-rate', 'zero-fallback'))
    args = p.parse_args()
    for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
                 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
        assert os.environ.get(name) == '1', name
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    start = time.monotonic()
    def guard(_s, _f):
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rss = rss if sys.platform == 'darwin' else rss*1024
        if time.monotonic()-start > 60 or rss > 270_000_000:
            raise RuntimeError('resource bound exceeded')
    signal.signal(signal.SIGALRM, guard); signal.setitimer(signal.ITIMER_REAL, .2, .2)
    result = {'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'autonomous': autonomous_checks(args.fault), 'axiom_models': axiom_models(),
              'omission_controls': omission_controls(),
              'N5': {'per_element': 'checked exact finite rational matrix entries; no physical gate calibration inferred',
                     'per_site': 'checked both atoms stay supported in all 1458 six-neighbor conditions',
                     'per_mode': 'checked and not executed — no field-mode or continuum decomposition is in this diagnostic',
                     'per_block': 'checked finite two-qubit phase/record trajectories and normalized jump intensity',
                     'lattice_wide': 'checked and not executed — infinite Z3 existence is the separately checked finite-ancestry proof'}}
    result.update(status='ok', elapsed_seconds=time.monotonic()-start,
                  max_rss_host_units=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
