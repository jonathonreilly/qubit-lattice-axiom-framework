#!/usr/bin/env python3
"""Exact finite checks for the supplied mobile-record motion and birth model.

Enumerates all six-axis configurations through three births on a 2x3 graph,
checks communication classes, detailed balance and insertion counting, and
computes the formation-event content law. A symbolic killed-generator check
and an exact 15-state finite-rate solve use different calculations. No physical
rate selection, growing-volume limit, phase transition or TOE claim is made.
"""
from __future__ import annotations

import argparse
from collections import defaultdict, deque
from fractions import Fraction as F
from itertools import combinations, product

import sympy as sp

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/MOBILE_RECORDS_RARE_FORMATION_EVENT_LAW_AND_SIX_SITE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
EDGES = ((0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5))
NB = {x: {v if u == x else u for u, v in EDGES if x in (u, v)} for x in range(6)}
MUTATIONS = {
    "motion_flat": "motion", "birth_normalized": "insertion",
    "drop_multiplicity": "insertion", "merge_sectors": "content_law",
    "unbiased_events": "event_sampling", "killing_flat": "resolvent",
    "allow_removal": "vacancies",
}


class Checks:
    def __init__(self):
        self.passed = self.failed = 0
        self.failed_families = set()

    def check(self, family, label, condition):
        if condition:
            self.passed += 1
        else:
            self.failed += 1
            self.failed_families.add(family)
        print(f"{'PASS' if condition else 'FAIL'}: {family}: {label}")


def multiply(xs):
    out = F(1)
    for x in xs:
        out *= x
    return out


def weight(s, W):
    return multiply(W[s[x]][s[y]] for x, y in EDGES if s[x] >= 0 and s[y] >= 0)


def raw(s, x, a, W):
    return multiply(W[a][s[y]] for y in NB[x] if s[y] >= 0)


def count(s, q):
    return tuple(s.count(a) for a in range(q))


def inc(n, a):
    m = list(n)
    m[a] += 1
    return tuple(m)


def configurations(n, q):
    for sites in combinations(range(6), n):
        for contents in product(range(q), repeat=n):
            s = [-1] * 6
            for x, a in zip(sites, contents):
                s[x] = a
            yield tuple(s)


def hops(s, edges=EDGES):
    for x, y in edges:
        if (s[x] == -1) != (s[y] == -1):
            t = list(s)
            t[x], t[y] = t[y], t[x]
            yield tuple(t)


def components(ss, edges=EDGES):
    left, parts = set(ss), []
    while left:
        root = min(left)
        seen, queue = {root}, deque([root])
        while queue:
            for t in hops(queue.popleft(), edges):
                if t not in seen:
                    seen.add(t)
                    queue.append(t)
        parts.append(seen)
        left -= seen
    return parts


def enumerate_model(W, mutation):
    q = len(W)
    Z, sectors = defaultdict(F), defaultdict(list)
    for level in range(4):
        for s in configurations(level, q):
            n = count(s, q)
            sectors[n].append(s)
            Z[n] += weight(s, W)
    rates, hazards = {}, {}
    insertion_ok, balance_ok, connected_ok = True, True, True
    total_states = sector_count = 0
    for n, ss in sectors.items():
        if sum(n) > 2:
            continue
        total_states += len(ss)
        sector_count += 1
        connected_ok &= len(components(ss)) == 1
        r = [F(0)] * q
        for s in ss:
            ws = weight(s, W)
            for t in hops(s):
                wt = weight(t, W)
                forward = F(1, 2) if mutation == "motion_flat" else wt / (ws + wt)
                reverse = F(1, 2) if mutation == "motion_flat" else ws / (ws + wt)
                balance_ok &= ws * forward == wt * reverse
            b = F(0)
            for x in range(6):
                if s[x] != -1:
                    continue
                row = [raw(s, x, a, W) for a in range(q)]
                if mutation == "birth_normalized":
                    row = [v / sum(row) for v in row]
                b += sum(row)
                for a, value in enumerate(row):
                    r[a] += ws * value
            hazards[s] = b
        rates[n] = tuple(v / Z[n] for v in r)
        for a in range(q):
            multiplicity = 1 if mutation == "drop_multiplicity" else n[a] + 1
            insertion_ok &= rates[n][a] == multiplicity * Z[inc(n, a)] / Z[n]
    laws = [{(0,) * q: F(1)}]
    for level in range(3):
        nxt = defaultdict(F)
        average = sum(p * sum(rates[n]) for n, p in laws[-1].items())
        for n, p in laws[-1].items():
            denominator = average if mutation == "merge_sectors" else sum(rates[n])
            for a, r in enumerate(rates[n]):
                nxt[inc(n, a)] += p * r / denominator
        laws.append(dict(nxt))
    return Z, sectors, rates, hazards, laws, (insertion_ok, balance_ok, connected_ok, total_states, sector_count)


def symbolic_exit(checks, mutation):
    e, r, s, b0, b1, h = sp.symbols('e r s b0 b1 h', positive=True)
    Q = sp.Matrix([[-r, r], [s, -s]])
    alpha = sp.Matrix([[1, 0]])
    v = e * alpha * (e * sp.diag(b0 + h, b1 + h) - Q).inv()
    pi = sp.Matrix([[s / (r + s), r / (r + s)]])
    mean = (s * b0 + r * b1) / (r + s)
    want = pi / (mean + h)
    checks.check('resolvent', 'two-state marked waiting-time transform, arbitrary positive rates',
                 all(sp.simplify(sp.limit(v[i], e, 0) - want[i]) == 0 for i in range(2)))
    event = sp.Matrix([[sp.limit(v[i].subs(h, 0), e, 0) * b for i, b in enumerate((b0, b1))]])
    predicted = pi if mutation == 'unbiased_events' else sp.Matrix([[pi[i] * b / mean for i, b in enumerate((b0, b1))]])
    checks.check('event_sampling', 'event law tested against exact killed-generator limit',
                 all(sp.simplify(event[i] - predicted[i]) == 0 for i in range(2)))


def finite_rate(checks, mutation):
    # This calculation uses occupied pairs, global weights and a linear solve,
    # not the local-insertion averaged-count recursion above.
    ss = tuple(frozenset(c) for c in combinations(range(6), 2))
    index = {s: i for i, s in enumerate(ss)}
    edge_set = set(EDGES)
    w = sp.Matrix([sp.Rational(3, 2) if tuple(sorted(s)) in edge_set else sp.Integer(1) for s in ss])
    pi = w / sum(w)
    Q = sp.zeros(len(ss))
    for i, s in enumerate(ss):
        for x in s:
            for y in NB[x] - s:
                j = index[s - {x} | {y}]
                Q[i, j] = w[j] / (w[i] + w[j])
        Q[i, i] = -sum(Q[i, j] for j in range(len(ss)) if j != i)
    a = sp.Matrix([sum(sp.Rational(3, 2) ** len(NB[x] & s) for x in range(6) if x not in s) for s in ss])
    b = a + sp.Matrix([sum(sp.Rational(1, 2) ** len(NB[x] & s) for x in range(6) if x not in s) for s in ss]) + sp.ones(15, 1) * 16
    mean = (pi.T * b)[0]
    palm = sp.matrix_multiply_elementwise(pi, b) / mean
    checks.check('resolvent', '15-state invariant law and insertion intensity',
                 pi.T * Q == sp.zeros(1, 15) and mean == sp.Rational(898, 37))
    rows = []
    for epsilon in (sp.Rational(1, 10), sp.Rational(1, 100), sp.Rational(1, 1000)):
        diagonal = sp.eye(15) * mean if mutation == 'killing_flat' else sp.diag(*b)
        occupation = (epsilon * diagonal - Q).T.inv() * pi
        prebirth = epsilon * sp.matrix_multiply_elementwise(occupation, b)
        probability = sp.Rational(37, 180) * epsilon * (occupation.T * a)[0]
        rows.append((epsilon, probability, sum(abs(prebirth[i] - palm[i]) for i in range(15)) / 2))
        print(f'finite_rate: epsilon={epsilon} all_three_same={probability} event_distance_to_limit={rows[-1][2]}')
    checks.check('resolvent', 'nonzero-rate absorption witness at epsilon=1/1000',
                 rows[-1][1] == sp.Rational(2851401694918427, 56880888215238000))
    errors = [abs(p - sp.Rational(2701, 53880)) for _, p, _ in rows]
    checks.check('resolvent', 'three exact finite rates approach the proved limit; final error below 6e-7',
                 errors[2] < errors[1] < errors[0] and errors[2] < sp.Rational(6, 10**7))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list-mutations', action='store_true')
    parser.add_argument('--mutation', choices=tuple(MUTATIONS))
    args = parser.parse_args()
    if args.list_mutations:
        for name, family in MUTATIONS.items():
            print(name, family)
        return 0
    checks = Checks()
    W = [[F(3, 2) if a == b else F(1, 2) if a == (b ^ 1) else F(1) for b in range(6)] for a in range(6)]
    Z, sectors, rates, hazards, laws, evidence = enumerate_model(W, args.mutation)
    insertion_ok, balance_ok, connected_ok, ns, nc = evidence
    checks.check('motion', f'all {nc} source count sectors connected, {ns} configurations', connected_ok and nc == 28 and ns == 577)
    checks.check('motion', 'every source-class vacancy hop satisfies detailed balance', balance_ok)
    checks.check('insertion', 'all 168 averaged insertion rates agree with independent insertion/deletion counting', insertion_ok)
    checks.check('content_law', 'event laws normalize at all three births', all(sum(p.values()) == 1 for p in laws))
    totals = [sum(z for n, z in Z.items() if sum(n) == k) for k in (1, 2, 3)]
    checks.check('content_law', 'partition functions from enumeration: 36, 540, 4320', totals == [36, 540, 4320])
    same = sum(p for n, p in laws[3].items() if max(n) == 3)
    static_same = sum(z for n, z in Z.items() if sum(n) == 3 and max(n) == 3) / totals[2]
    tv = sum(abs(p - Z[n] / totals[2]) for n, p in laws[3].items()) / 2
    print(f'content_law: all_identical_growth={same} static={static_same} difference={same-static_same} count_TV={tv}')
    checks.check('content_law', 'third-birth witness matches the separate edge/wedge combinatorial derivation',
                 same == F(2701, 53880) and static_same == F(73, 1440) and same-static_same == -F(73, 129312) and tv == F(811, 387936))
    k = (2, 0, 0, 0, 0, 0)
    mean = sum(rates[k])
    event_tv = sum(abs(weight(s, W) / Z[k] * (hazards[s] / mean - 1)) for s in sectors[k]) / 2
    print(f'event_sampling: two_identical_mean_rate={mean} event_TV={event_tv}')
    checks.check('event_sampling', 'exact two-identical-record rate tilt', mean == F(898, 37) and event_tv == F(125, 16613))
    symbolic_exit(checks, args.mutation)
    finite_rate(checks, args.mutation)
    flat = [[F(1)] * 6 for _ in range(6)]
    _, _, _, _, flatlaws, _ = enumerate_model(flat, None)
    flat_same = sum(p for n, p in flatlaws[3].items() if max(n) == 3)
    checks.check('controls', 'constant weights give the uniform-content probability 1/36', flat_same == F(1, 36))
    path_states = {(0, 1, -1), (0, -1, 1), (-1, 0, 1), (1, 0, -1), (1, -1, 0), (-1, 1, 0)}
    checks.check('controls', 'three-site path has two distinct order-preserving motion classes',
                 sorted(len(c) for c in components(path_states, ((0, 1), (1, 2)))) == [3, 3])
    vacancy_ok = True
    for n, ss in sectors.items():
        if sum(n) > 2:
            continue
        for s in ss:
            before = s.count(-1)
            drift = F(0)
            for x in range(6):
                if s[x] == -1:
                    for a in range(6):
                        t = s[:x] + (a,) + s[x+1:]
                        drift += raw(s, x, a, W) * (t.count(-1) - before)
            for t in hops(s):
                drift += (t.count(-1) - before)
            if args.mutation == 'allow_removal':
                drift += sum(n)
            native_birth_rate = sum(raw(s, x, a, W) for x in range(6) if s[x] < 0 for a in range(6))
            vacancy_ok &= drift == -native_birth_rate
    checks.check('vacancies', 'explicit transitions give L V=-B at epsilon=1', vacancy_ok)
    print('per_element: executed — every insertion on the 577 source configurations; all 168 averaged rates checked by a different counting identity')
    print('per_site: executed — all six sites, all six contents and all vacancy hops on the declared source sectors')
    print('per_mode: checked and not executed — no Fourier-mode, hydrodynamic or field-response claim is made')
    print('per_block: executed — third-birth content law, rate-biased observation and a 15-state nonzero-rate resolvent on the stated 2x3 graph')
    print('lattice_wide: checked and not executed — the proof is finite-graph; no volume-uniform mixing or infinite-lattice correlation conclusion is asserted')
    if args.mutation:
        print(f'mutation_family_expected: {MUTATIONS[args.mutation]}')
        print(f'mutation_family_observed: {",".join(sorted(checks.failed_families)) or "none"}')
    print('scope: conditional finite motion-and-birth model; exact event-law witness; no physical parameter selection or TOE closure')
    print(f'TOTAL: PASS={checks.passed} FAIL={checks.failed}')
    return int(bool(checks.failed))


if __name__ == '__main__':
    raise SystemExit(main())
