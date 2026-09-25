#!/usr/bin/env python3
"""Fresh PRE46 exact primitive controls. Standard library; no source imports.

The K(2,4) fixture checks the full original local algebra, not cubic dynamics.
All scientific coefficients are integers, including Gaussian integer pairs.
"""
from collections import Counter
from itertools import product
import json
import time

A = (0, 1)
B = (2, 3, 4, 5)
EDGES = tuple((a, b) for a in A for b in B)
EI = {edge: i for i, edge in enumerate(EDGES)}
INC = tuple(tuple((1 if x == a else -1 if x == b else 0) for a, b in EDGES) for x in range(6))
CYCLE = tuple({(0, 2): 1, (1, 2): -1, (1, 3): 1, (0, 3): -1}.get(e, 0) for e in EDGES)


def gauss(state, P=False):
    q, E = state
    assert len(q) == 6 and len(E) == 8 and all(s in (-1, 0, 1) for s in q)
    assert all(isinstance(v, int) for v in E)
    if P:
        assert all(q[a] for a in A)
    assert [sum(s*v for s, v in zip(row, E)) for row in INC] == [q[x]-int(x in A) for x in range(6)]


def changed(state, replacements, edge, shift):
    q, E = map(list, state)
    for x, value in replacements.items():
        q[x] = value
    E[EI[edge]] += shift
    out = tuple(q), tuple(E)
    gauss(out)
    return out


def outward(state, a):
    q, E = state
    if q[a] == 0:
        return {}
    sign = q[a]
    return {changed(state, {a: 0, b: sign}, (a, b), -sign): 1 for b in B if q[b] == 0}


def inward(state, a):
    q, E = state
    if q[a] != 0:
        return {}
    return {changed(state, {a: q[b], b: 0}, (a, b), q[b]): 1 for b in B if q[b] != 0}


def birth(state, a, b, sign, adjoint=False):
    q, E = state
    if adjoint:
        if q[a] != sign or q[b] != -sign:
            return {}
        return {changed(state, {a: 0, b: 0}, (a, b), -sign): 1}
    if q[a] != 0 or q[b] != 0:
        return {}
    return {changed(state, {a: sign, b: -sign}, (a, b), sign): 1}


def step(vector, action):
    out = Counter()
    for state, coefficient in vector.items():
        for target, amplitude in action(state).items():
            out[target] += coefficient*amplitude
    return {state: value for state, value in out.items() if value}


def jump(state, a, b, sign, adjoint=False):
    if not all(state[0][x] for x in A):
        return {}
    if sign is None:
        out = Counter()
        for sigma in (-1, 1):
            out.update(jump(state, a, b, sigma, adjoint))
        return dict(out)
    if adjoint:
        vector = birth(state, a, b, sign, True)
        vector = step(vector, lambda w: inward(w, a))
    else:
        vector = outward(state, a)
        vector = step(vector, lambda w: birth(w, a, b, sign))
    return {w: c for w, c in vector.items() if all(w[0][x] for x in A)}


def h4(state):
    # One overlapping A pair: -2 P F_0^* F_1^* F_1 F_0 P.
    vector = {state: 1}
    for a, adj in ((0, False), (1, False), (1, True), (0, True)):
        vector = step(vector, lambda w, a=a, adj=adj: inward(w, a) if adj else outward(w, a))
    return {w: -2*c for w, c in vector.items() if all(w[0][a] for a in A)}


def initial_field(q, multiplier=0):
    E = [0]*8
    E[EI[1, 2]] = q[1]-1
    E[EI[0, 2]] = -q[2]-E[EI[1, 2]]
    for b in (3, 4, 5):
        E[EI[0, b]] = -q[b]
    state = tuple(q), tuple(e+multiplier*c for e, c in zip(E, CYCLE))
    gauss(state, True)
    return state


def electric(state):
    q, E = state
    return sum(e*(e-q[a]) for (a, b), e in zip(EDGES, E) if q[b] == 0)


def magnetic_column(state):
    q, E = state
    rows = []
    for target, coefficient in sorted(h4(state).items()):
        tq, tE = target
        shift = tuple(y-x for x, y in zip(E, tE))
        M = [d*coefficient for d in shift]
        Q = [(x-y)*coefficient for x, y in zip(q, tq)]
        assert [Q[x]+sum(s*v for s, v in zip(INC[x], M)) for x in range(6)] == [0]*6
        rows.append(dict(q=tq, shift=shift, h4_coefficient=coefficient,
                         current_without_i_delta=M, charge_generator_without_i_delta=Q))
    return rows


def dissipative_column(state, coherent):
    q, E = state
    out = {}
    signs = (None,) if coherent else (-1, 1)
    for a, b in EDGES:
        for sign in signs:
            for middle, first in jump(state, a, b, sign).items():
                mq, mE = middle
                for target, second in jump(middle, a, b, sign, True).items():
                    tq, tE = target
                    values = out.setdefault(target, [0]*14)
                    for x in range(6):
                        values[x] += first*second*(2*mq[x]-q[x]-tq[x])
                    for e in range(8):
                        values[6+e] += first*second*(2*mE[e]-E[e]-tE[e])
    rows = []
    for (tq, tE), values in sorted(out.items()):
        Q, M = values[:6], values[6:]
        assert Q == [sum(s*v for s, v in zip(row, M)) for row in INC]
        if any(values):
            rows.append(dict(q=tq, shift=tuple(y-x for x, y in zip(E, tE)),
                             twice_charge_generator_over_kappa=Q,
                             minus_twice_current_over_kappa=M))
    return rows


def gadd(a, b): return a[0]+b[0], a[1]+b[1]
def gscale(n, a): return n*a[0], n*a[1]
def gconj(a): return a[0], -a[1]
def gmul(a, b): return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]
def charge_test(f, q):
    out = (0, 0)
    for x, fx in enumerate(f):
        out = gadd(out, gscale(q[x]-int(x in A), fx))
    return out


def initial_kernels():
    q = (1, 1, 0, 0, 0, 0)
    f = [(x-2, (x*x)%5-2) for x in range(6)]
    g = [((2*x)%7-3, 1-x) for x in range(6)]
    states = {m: initial_field(q, m) for m in (-1, 0, 1)}
    rows = []
    for coherent in (False, True):
        signs = (None,) if coherent else (-1, 1)
        images = {(m, a, b, sign): jump(w, a, b, sign) for m, w in states.items()
                  for a, b in EDGES for sign in signs}
        for m in states:
            for n in states:
                loss = 0
                mean_f = mean_g = covariance = (0, 0)
                for a, b in EDGES:
                    for sign in signs:
                        left, right = images[m, a, b, sign], images[n, a, b, sign]
                        for u in left.keys() & right.keys():
                            weight = left[u]*right[u]
                            rf, rg = charge_test(f, u[0]), charge_test(g, u[0])
                            loss += weight
                            mean_f = gadd(mean_f, gscale(weight, rf))
                            mean_g = gadd(mean_g, gscale(weight, rg))
                            covariance = gadd(covariance, gscale(weight, gmul(gconj(rf), rg)))
                rows.append(dict(coherent=coherent, left_cycle=m, right_cycle=n, loss=loss,
                                 mean_f=mean_f, mean_g=mean_g, covariance_fg=covariance))
    diagonals = [r for r in rows if r['left_cycle'] == r['right_cycle']]
    reference = {k: diagonals[0][k] for k in ('loss', 'mean_f', 'mean_g', 'covariance_fg')}
    assert reference['loss'] == 48
    for row in rows:
        for key in reference:
            expected = reference[key] if row['left_cycle'] == row['right_cycle'] else (0 if key == 'loss' else (0, 0))
            assert row[key] == expected
    expected_mean_f = expected_mean_g = expected_covariance = (0, 0)
    for a, b in EDGES:
        df = gadd(f[b], gscale(-1, f[a]))
        dg = gadd(g[b], gscale(-1, g[a]))
        expected_mean_f = gadd(expected_mean_f, gscale(6, df))
        expected_mean_g = gadd(expected_mean_g, gscale(6, dg))
        expected_covariance = gadd(expected_covariance, gscale(12, gmul(gconj(df), dg)))
    assert (reference['mean_f'], reference['mean_g'], reference['covariance_fg']) == (expected_mean_f, expected_mean_g, expected_covariance)
    return dict(f=f, g=g, rows=rows, formula_values=reference)


def stars():
    out = []
    for d in range(7):
        branches = []
        mean = [0]*(d+1)
        C = [[0]*(d+1) for _ in range(d+1)]
        for b in range(1, d+1):
            for c in range(1, d+1):
                if b == c:
                    continue
                for sign in (-1, 1):
                    dq = [0]*(d+1)
                    dq[0], dq[b], dq[c] = sign-1, -sign, 1
                    de = [0]*d
                    de[b-1], de[c-1] = sign, -1
                    assert dq[0] == sum(de) and dq[1:] == [-e for e in de]
                    for x in range(d+1):
                        mean[x] += dq[x]
                        for y in range(d+1):
                            C[x][y] += dq[x]*dq[y]
                    branches.append(dict(mark=b, hop=c, sign_at_A=sign, charge_change=dq, electric_shift=de))
        assert len(branches) == 2*d*(d-1)
        expected_mean = [-2*d*(d-1)]+[2*(d-1)]*d
        expected_C = [[0]*(d+1) for _ in range(d+1)]
        for b in range(1, d+1):
            for x, y, sign in ((0, 0, 1), (b, b, 1), (0, b, -1), (b, 0, -1)):
                expected_C[x][y] += 4*(d-1)*sign
        assert mean == expected_mean and C == expected_C
        out.append(dict(degree=d, branches=branches, intensity_over_kappa=len(branches),
                        mean_derivative_over_kappa=mean, covariance_derivative_over_kappa=C))
    return out


def magnetic_coherence():
    q = (1, 1, 0, 0, 0, 0)
    coeffs = {initial_field(q, 0): (1, 0), initial_field(q, 1): (0, -1)}
    numerator = [(0, 0)]*8
    for source, alpha in coeffs.items():
        for target, h in h4(source).items():
            if target not in coeffs:
                continue
            weight = gmul(gconj(coeffs[target]), alpha)
            for e in range(8):
                value = (target[1][e]-source[1][e])*h
                numerator[e] = gadd(numerator[e], gmul(weight, (0, value)))
    assert numerator == [(4*c, 0) for c in CYCLE]
    assert [sum(s*v[0] for s, v in zip(row, numerator)) for row in INC] == [0]*6
    return dict(unnormalized_amplitudes=[[0, [1, 0]], [1, [0, -1]]], norm_squared=2,
                mean_current_numerator_over_delta=numerator, cycle=CYCLE,
                meaning='Nonzero Hamiltonian circulation current with zero charge divergence')


def main():
    started = time.perf_counter()
    columns = []
    matter_words = [q for q in product((-1, 0, 1), repeat=6)
                    if all(q[a] for a in A) and sum(q) == 2]
    assert len(matter_words) == 40
    for q in matter_words:
        magnetic = dissipative = None
        energies = []
        for m in (0, -1000, 1001):
            state = initial_field(q, m)
            H = magnetic_column(state)
            R = dissipative_column(state, False)
            C = dissipative_column(state, True)
            assert R == C
            if magnetic is None:
                magnetic, dissipative = H, R
            else:
                assert H == magnetic and R == dissipative
            energies.append(dict(circulation=m, D=electric(state)))
        columns.append(dict(q=q, N=sum(abs(v) for v in q), energies=energies,
                            magnetic_terms=magnetic, dissipative_terms=dissipative,
                            both_instruments_equal=True, current_flux_offset_independent=True))
    result = dict(status='All exact primitive continuity and initial-noise controls passed',
                  fixture=dict(A=A, B=B, edges=EDGES, incidence=INC, cycle=CYCLE),
                  current_columns=columns, matter_columns=len(columns), shifted_columns=3*len(columns),
                  star_initial=stars(), normal_field_initial_kernels=initial_kernels(),
                  coherent_field_magnetic_current=magnetic_coherence(),
                  scope='Finite exact algebra controls; analytic PRE supplies unbounded domains and all normal states',
                  prior_or_author_code_imported=False, elapsed_seconds=time.perf_counter()-started)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
