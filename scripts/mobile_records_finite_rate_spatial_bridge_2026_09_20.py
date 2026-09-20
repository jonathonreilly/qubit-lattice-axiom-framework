#!/usr/bin/env python3
"""Exact finite-rate, dilution and spatial-generator checks for mobile records.

The general inequalities are proved in the note. These computations check a
full killed generator, a certified gap, direct insertion sums and all local
states on named finite graphs. No interacting finite-density closure is used.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, cos, pi as PI

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/MOBILE_RECORDS_FINITE_RATE_CONTROL_AND_SPATIAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MOBILE_RECORDS_RARE_FORMATION_EVENT_LAW_AND_SIX_SITE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
LADDER = ((0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5))
AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
MUTATIONS = {
    "wrong_center": "resolvent", "oversized_gap": "gap",
    "omit_hazard_variance": "error", "omit_corrector": "poisson",
    "drop_wedges": "dilution", "drop_sink": "vacancy",
    "dense_closure": "orientation", "wrong_birth_sign": "spectrum",
}


class Checks:
    def __init__(self):
        self.passed = self.failed = 0
        self.families = set()

    def check(self, family, label, condition):
        if condition:
            self.passed += 1
        else:
            self.failed += 1
            self.families.add(family)
        print(f"{'PASS' if condition else 'FAIL'}: {family}: {label}")


def neighbors(n, edges):
    return tuple({v if u == x else u for u, v in edges if x in (u, v)} for x in range(n))


def pair_weight(a, b, j):
    return 1 + j if a == b else 1 - j if a == (b ^ 1) else F(1)


def weight(state, edges, j):
    out = F(1)
    for x, y in edges:
        if state[x] >= 0 and state[y] >= 0:
            out *= pair_weight(state[x], state[y], j)
    return out


def insertion(state, x, a, nb, j):
    out = F(1)
    for y in nb[x]:
        if state[y] >= 0:
            out *= pair_weight(a, state[y], j)
    return out


def pair_generator():
    states = tuple(frozenset(s) for s in combinations(range(6), 2))
    index = {s: i for i, s in enumerate(states)}
    nb = neighbors(6, LADDER)
    w = sp.Matrix([sp.Rational(3, 2) if tuple(sorted(s)) in LADDER else 1 for s in states])
    p = w / sum(w)
    Q = sp.zeros(15)
    for i, s in enumerate(states):
        for x in s:
            for y in nb[x] - s:
                k = index[s - {x} | {y}]
                Q[i, k] += w[k] / (w[i] + w[k])
        Q[i, i] = -sum(Q[i, k] for k in range(15) if k != i)
    success = sp.Matrix([sum(sp.Rational(3, 2) ** len(nb[x] & s) for x in range(6) if x not in s) for s in states])
    opposite = sp.Matrix([sum(sp.Rational(1, 2) ** len(nb[x] & s) for x in range(6) if x not in s) for s in states])
    return -Q, p, success + opposite + 16 * sp.ones(15, 1), success


def finite_rate_checks(checks, mutation):
    L, p, B, success = pair_generator()
    P, one = sp.diag(*p), sp.ones(15, 1)
    mean, low, high = (p.T * B)[0], min(B), max(B)
    gap = sp.Integer(1) if mutation == 'oversized_gap' else sp.Rational(2, 5)
    # Columns span the pi-mean-zero subspace. A positive exact LDL certificate
    # verifies the Poincare inequality without a floating eigenvalue estimate.
    basis = sp.zeros(15, 14)
    for i in range(14):
        basis[i, i], basis[14, i] = 1, -p[i] / p[14]
    gram = basis.T * P * (L - gap * sp.eye(15)) * basis
    try:
        lower, diag = gram.LDLdecomposition(hermitian=False)
        certified = lower * diag * lower.T == gram and all(x > 0 for x in diag.diagonal())
    except (ValueError, ZeroDivisionError):
        certified = False
    checks.check('gap', '14 exact positive pivots certify motion gap at least 2/5', certified)
    palm_density = B / mean
    entrances = (('stationary', one), ('point', sp.Matrix([1 / p[0]] + [0] * 14)), ('palm', palm_density))
    S = sp.diag(*B) - B * (p.T * sp.diag(*B)) / mean
    checks.check('resolvent', 'hazard Schur complement is symmetric in pi and kills constants', P * S == S.T * P and S * one == sp.zeros(15, 1))
    event_ok = reconstruction_ok = poisson_ok = time_ok = clock_ok = True
    rows = []
    derivative = None
    for name, entrance in entrances:
        forcing = entrance - palm_density
        phi = (L + one * p.T).inv() * forcing
        checks.check('poisson', f'zero-mean Poisson equation for {name} entrance', L * phi == forcing and (p.T * phi)[0] == 0)
        norm2 = (forcing.T * P * forcing)[0]
        for epsilon in (sp.Rational(1, 10000), sp.Rational(1, 1000), sp.Rational(1, 100), sp.Rational(1, 10), sp.Integer(1)):
            g = epsilon * (L + epsilon * sp.diag(*B)).inv() * entrance
            h = g - one * (p.T * g)[0]
            shift = 0 if mutation == 'wrong_center' else (p.T * sp.diag(*B) * h)[0] / mean
            reconstructed = one / mean + h - one * shift
            reconstruction_ok &= reconstructed == g and (L + epsilon * S) * h == epsilon * forcing
            observed = p.multiply_elementwise(B).multiply_elementwise(g)
            target = p.multiply_elementwise(palm_density)
            tv = sum(abs(x) for x in observed - target) / 2
            R = -sp.diag(*(1 / b for b in B)) * L
            clock_law = epsilon * (entrance.T * P) * (epsilon * sp.eye(15) - R).inv()
            clock_norm2 = mean * (forcing.T * P * sp.diag(*(1 / b for b in B)) * forcing)[0]
            clock_bound2 = epsilon**2 * clock_norm2 / (4 * (epsilon + gap / high)**2)
            clock_ok &= clock_law == observed.T and tv**2 <= clock_bound2
            use_norm2 = ((entrance - one).T * P * (entrance - one))[0] if mutation == 'omit_hazard_variance' else norm2
            bound2 = epsilon**2 * mean * high * use_norm2 / (4 * (gap + epsilon * low)**2)
            event_ok &= sum(observed) == 1 and tv**2 <= bound2
            cphi = phi - one * (p.T * sp.diag(*B) * phi)[0] / mean
            correction = sp.zeros(15, 1) if mutation == 'omit_corrector' else p.multiply_elementwise(B).multiply_elementwise(cphi)
            residual_tv = sum(abs(x) for x in observed - target - epsilon * correction) / 2
            remainder2 = epsilon**4 * mean * high**3 * norm2 / (4 * gap**2 * (gap + epsilon * low)**2)
            poisson_ok &= residual_tv**2 <= remainder2
            variance = ((B - mean * one).T * P * (B - mean * one))[0]
            time_error = abs((p.T * g)[0] - 1 / mean)
            time_bound2 = epsilon**2 * variance * norm2 / (mean**2 * (gap + epsilon * low)**2)
            time_ok &= time_error**2 <= time_bound2
            if name == 'stationary':
                rows.append((str(epsilon), str(tv), float(sp.sqrt(bound2)), str(residual_tv)))
                derivative = sp.Rational(37, 180) * (p.T * sp.diag(*success) * cphi)[0]
    checks.check('resolvent', 'direct absorption equals centered resolvent reconstruction at all 15 cases', reconstruction_ok)
    checks.check('error', 'exact pre-birth TV obeys the certified finite-rate bound for all entrances/rates', event_ok)
    checks.check('poisson', 'first-order corrected event law has the certified quadratic remainder', poisson_ok)
    checks.check('error', 'scaled mean waiting time obeys the same-gap bound', time_ok)
    checks.check('resolvent', 'hazard-clock resolvent and complementary gap bound agree with direct absorption', clock_ok)
    checks.check('poisson', 'third-birth derivative equals -16823/29030544', derivative == -sp.Rational(16823, 29030544))
    print(f'finite_rate: mean_hazard={mean} hazard_variance={variance} certified_gap={gap} third_birth_derivative={derivative}')
    for row in rows:
        print('stationary_entrance: epsilon=%s exact_TV=%s bound=%.12g corrected_TV=%s' % row)


def graph_cases():
    for n in (3, 4, 6, 8):
        yield f'path_{n}', n, tuple((x, x + 1) for x in range(n - 1))
    for n in (4, 5, 6, 10):
        yield f'cycle_{n}', n, tuple((x, x + 1) for x in range(n - 1)) + ((0, n - 1),)
    yield 'ladder_6', 6, LADDER
    yield 'ladder_12', 12, tuple((r * 6 + x, r * 6 + x + 1) for r in range(2) for x in range(5)) + tuple((x, x + 6) for x in range(6))
    yield 'star_8', 8, tuple((0, x) for x in range(1, 8))


def dilution_checks(checks, mutation):
    identities_ok = ratios_ok = static_ok = connected_ok = True
    count = 0
    for name, n, edges in graph_cases():
        nb = neighbors(n, edges)
        wedge = sum(comb(len(row), 2) for row in nb)
        assert not any(x in nb[y] and x in nb[z] and z in nb[y] for x, y, z in combinations(range(n), 3))
        pairs = set(frozenset(s) for s in combinations(range(n), 2))
        seen, todo = {next(iter(pairs))}, [next(iter(pairs))]
        while todo:
            s = todo.pop()
            for x in s:
                for y in nb[x] - s:
                    t = s - {x} | {y}
                    if t not in seen:
                        seen.add(t)
                        todo.append(t)
        connected_ok &= seen == pairs
        for j in (F(-1, 2), F(0), F(1, 2)):
            za = hazard_sum = success_sum = F(0)
            for occupied in pairs:
                state = tuple(0 if x in occupied else -1 for x in range(n))
                w = weight(state, edges, j)
                za += w
                for x in range(n):
                    if state[x] < 0:
                        row = [insertion(state, x, a, nb, j) for a in range(6)]
                        hazard_sum += w * sum(row)
                        success_sum += w * row[0]
            triple_same = sum((1 + j)**sum(x in occupied and y in occupied for x, y in edges) for occupied in map(set, combinations(range(n), 3)))
            dynamic = za / (6 * comb(n, 2)) * success_sum / hazard_sum
            static = triple_same / (36 * comb(n, 3))
            main = 6 * (n - 2) * za
            correction = 0 if mutation == 'drop_wedges' else 2 * j*j * wedge
            ratios_ok &= dynamic / static == main / (main + correction)
            identities_ok &= za == comb(n, 2) + j * len(edges) and hazard_sum == main + 2*j*j*wedge and success_sum == 3 * triple_same
            if n <= 6:
                total = F(0)
                for occupied in combinations(range(n), 3):
                    for contents in product(range(6), repeat=3):
                        state = [-1] * n
                        for x, a in zip(occupied, contents):
                            state[x] = a
                        total += weight(state, edges, j)
                static_ok &= total == 216 * comb(n, 3)
            count += 1
            if name == 'ladder_6' and j == F(1, 2):
                print(f'dilution: six_site_dynamic={dynamic} static={static} ratio={dynamic/static}')
    checks.check('dilution', 'identical-pair sectors connected on all 11 named graphs', connected_ok)
    checks.check('dilution', f'direct insertion sums verify pair/wedge/triple identities in {count} cases', identities_ok)
    checks.check('dilution', 'all-identical dynamic/static ratios match the graph formula', ratios_ok)
    checks.check('dilution', 'content-summed static triple partition independently enumerated for graphs up to six vertices', static_ok)
    for n in (10, 100, 1000):
        za = F(comb(n, 2)) + F(n, 2)
        ratio = 6 * (n - 2) * za / (6 * (n - 2) * za + F(n, 2))
        print(f'dilution: cycle_vertices={n} relative_deficit={1-ratio} volume_squared_deficit={float(n*n*(1-ratio)):.12g}')


def vacancy_checks(checks, mutation):
    epsilon, q = F(1, 7), 6
    good = True
    nstates = 0
    for n, edges in ((4, ((0, 1), (1, 2), (2, 3), (0, 3))), (6, LADDER)):
        nb = neighbors(n, edges)
        for occupied in product((0, 1), repeat=n):
            vacancy = [1 - v for v in occupied]
            for x in range(n):
                actual = F(0)
                for a, b in edges:
                    if occupied[a] != occupied[b] and x in (a, b):
                        other = b if x == a else a
                        actual += F(1, 2) * (vacancy[other] - vacancy[x])
                actual -= q * epsilon * vacancy[x]
                sink = 0 if mutation == 'drop_sink' else q * epsilon * vacancy[x]
                predicted = F(1, 2) * sum(vacancy[y] - vacancy[x] for y in nb[x]) - sink
                good &= actual == predicted
            nstates += 1
    checks.check('vacancy', f'full occupancy generators give diffusion plus formation sink on {nstates} configurations', good)
    r = sp.symbols('r', positive=True)
    kappa = (1-r)**2 / (2*r)
    amp = 2*r / (1-r*r)
    checks.check('vacancy', 'infinite-chain response recurrence, origin normalization and total mass',
                 sp.simplify((kappa+1)*amp*r - (amp+amp*r*r)/2) == 0 and
                 sp.simplify((kappa+1)*amp-amp*r) == 1 and
                 sp.simplify(amp*(1+r)/(1-r)-1/kappa) == 0)


def orientation_checks(checks, mutation):
    n, edges, j, epsilon = 4, ((0, 1), (1, 2), (2, 3), (0, 3)), F(1, 2), F(1, 7)
    nb = neighbors(n, edges)
    isolated_ok = residual_ok = True
    dense_witness = None
    tested = isolated = 0
    for state in product(range(-1, 6), repeat=n):
        w = weight(state, edges, j)
        for x in range(n):
            local = {x} | nb[x] | set().union(*(nb[y] for y in nb[x]))
            multiple = sum(state[y] >= 0 for y in local) >= 2
            actual = [F(0)] * 3
            for y in nb[x]:
                if (state[x] < 0) != (state[y] < 0):
                    child = list(state)
                    child[x], child[y] = child[y], child[x]
                    child_weight = weight(child, edges, j)
                    rate = child_weight / (w + child_weight)
                    for axis in range(3):
                        before = AXES[state[x]][axis] if state[x] >= 0 else 0
                        after = AXES[child[x]][axis] if child[x] >= 0 else 0
                        actual[axis] += rate * (after - before)
            if state[x] < 0:
                for a in range(6):
                    birth = epsilon * insertion(state, x, a, nb, j)
                    for axis in range(3):
                        actual[axis] += birth * AXES[a][axis]
            for axis in range(3):
                mx = AXES[state[x]][axis] if state[x] >= 0 else 0
                adjacent = sum(AXES[state[y]][axis] if state[y] >= 0 else 0 for y in nb[x])
                predicted = F(1, 2) * (adjacent - len(nb[x])*mx) + 2*j*epsilon*adjacent
                residual = actual[axis] - predicted
                if not multiple:
                    isolated_ok &= residual == 0
                    isolated += 1
                elif residual and dense_witness is None:
                    dense_witness = (state, x, axis, str(residual))
                bound = 2*len(nb[x]) + 2*epsilon*(1+abs(j))**max(map(len, nb)) + 2*abs(j)*epsilon*len(nb[x])
                if mutation == 'dense_closure':
                    bound = 0
                residual_ok &= abs(residual) <= bound * int(multiple)
                tested += 1
    checks.check('orientation', f'isolated-neighborhood generator identity on {isolated} site/component cases', isolated_ok)
    checks.check('orientation', f'local multiple-occupancy residual bound on all {tested} site/component cases', residual_ok)
    checks.check('orientation', 'an explicit interacting dense state has nonzero closure residual', dense_witness is not None)
    print(f'orientation: dense_closure_counterexample={dense_witness}')
    # Independent spatial-matrix action on every Fourier mode of a cycle.
    side, epsilon = 12, 0.01
    adjacency = np.zeros((side, side))
    for x in range(side):
        adjacency[x, (x+1) % side] = adjacency[x, (x-1) % side] = 1
    tangent = (adjacency - 2*np.eye(side))/2 + 2*float(j)*epsilon*adjacency
    vacancy = (adjacency - 2*np.eye(side))/2 - 6*epsilon*np.eye(side)
    good = True
    for mode in range(side):
        k = 2*PI*mode/side
        v = np.exp(1j*k*np.arange(side))
        birth_sign = -1 if mutation == 'wrong_birth_sign' else 1
        orient_rate = -(1-cos(k)) + birth_sign*4*float(j)*epsilon*cos(k)
        vacancy_rate = -(1-cos(k)) - 6*epsilon
        good &= np.max(abs(tangent@v-orient_rate*v)) < 1e-12 and np.max(abs(vacancy@v-vacancy_rate*v)) < 1e-12
    checks.check('spectrum', 'direct spatial matrices verify all twelve Fourier multipliers', good)
    print('orientation: cubic_d=3 j=1/2 uniform_tangent_growth=6*epsilon; this is not a finite-density growth theorem')
    neutral_ok = True
    modes = [sp.Matrix([a[i] for a in AXES]) for i in range(3)]
    modes += [sp.Matrix([1, 1, -1, -1, 0, 0]), sp.Matrix([0, 0, 1, 1, -1, -1])]
    for equal, opposite, orthogonal in ((3, 1, 2), (6, 1, 2), (12, 1, 2), (1, 3, 2), (1, 1, 4)):
        scale = sp.Rational(6, equal + opposite + 4*orthogonal)
        W = sp.Matrix([[scale*(equal if a == b else opposite if a == (b ^ 1) else orthogonal) for b in range(6)] for a in range(6)])
        theta_v = scale*(equal-opposite)
        theta_a = scale*(equal+opposite-2*orthogonal)
        for k, mode in enumerate(modes):
            theta = theta_v if k < 3 else theta_a
            neutral_ok &= sum(mode) == 0 and W*mode == theta*mode
        if equal in (3, 6, 12) and opposite == 1:
            print(f'neutral_modes: raw_weights=({equal},{opposite},{orthogonal}) theta_vector={theta_v} theta_axis_population={theta_a}')
    checks.check('orientation', 'five centered content modes diagonalize five neutral pair-weight matrices', neutral_ok)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list-mutations', action='store_true')
    parser.add_argument('--mutation', choices=tuple(MUTATIONS))
    args = parser.parse_args()
    if args.list_mutations:
        for key, value in MUTATIONS.items():
            print(key, value)
        return 0
    c = Checks()
    finite_rate_checks(c, args.mutation)
    dilution_checks(c, args.mutation)
    vacancy_checks(c, args.mutation)
    orientation_checks(c, args.mutation)
    print('per_element: executed — exact resolvents, Poisson equations, rational gap certificate and insertion sums')
    print('per_site: executed — every occupancy state on named four/six-site graphs and every six-axis state on the four-cycle')
    print('per_mode: executed — all twelve cycle Fourier modes; general torus multipliers and scaling are proved algebraically in the note')
    print('per_block: executed — finite-rate six-site witness and eleven named triangle-free graphs at three weights')
    print('lattice_wide: checked and not executed — uniform-weight response has an exact operator proof; no interacting bulk phase, relativistic field or gravity claim')
    if args.mutation:
        print(f'mutation_family_expected: {MUTATIONS[args.mutation]}')
        print(f'mutation_family_observed: {",".join(sorted(c.families)) or "none"}')
    print(f'TOTAL: PASS={c.passed} FAIL={c.failed}')
    return int(bool(c.failed))


if __name__ == '__main__':
    raise SystemExit(main())
