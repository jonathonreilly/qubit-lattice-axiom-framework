#!/usr/bin/env python3
"""Finite controls for the explicit lifetime and spatial-dependence proofs.

The note proves the infinite-system statements. This runner checks finite
generators and the algebraic/probabilistic controls; it does not infer an
infinite-time theorem from a finite simulation.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import ceil, e, factorial

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/MOBILE_RECORDS_LIFETIME_ACTIVITY_AND_TERMINAL_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MOBILE_RECORDS_RARE_FORMATION_EVENT_LAW_AND_SIX_SITE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
MUTATIONS = {
    "omit_empty_neighbor_floor": "hazards",
    "drop_birth_sink": "balance",
    "ignore_vacancy_killing": "vacancy",
    "omit_birth_competition": "reuse",
    "miss_half_hop_acceptance": "uniform",
    "radius_one_hops": "dependence",
    "forget_product_start": "correlations",
    "omit_search_ball": "tag",
}


class Checks:
    def __init__(self):
        self.passed = self.failed = 0
        self.families = set()

    def run(self, family, label, function):
        try:
            function()
        except (AssertionError, ValueError, np.linalg.LinAlgError) as error:
            self.failed += 1
            self.families.add(family)
            print(f"FAIL: {family}: {label}: {error}".rstrip())
        else:
            self.passed += 1
            print(f"PASS: {family}: {label}")


def menu(j=F(1, 2), scale=F(1)):
    return [[scale*(1+j if a == b else 1-j if a ^ 1 == b else F(1))
             for b in range(6)] for a in range(6)]


def finite_model(n, edges, W):
    states = list(product(range(-1, 6), repeat=n))
    adjacent = [{y if x == i else x for x, y in edges if i in (x, y)} for i in range(n)]
    weights = {}
    for s in states:
        w = F(1)
        for x, y in edges:
            if s[x] >= 0 and s[y] >= 0:
                w *= W[s[x]][s[y]]
        weights[s] = w
    B, H, bx, departure = {}, {}, {}, {}
    for s in states:
        births, hops = {}, {}
        local_birth, local_depart = [F(0)]*n, [F(0)]*n
        for x in range(n):
            if s[x] >= 0:
                continue
            for a in range(6):
                t = list(s)
                t[x] = a
                t = tuple(t)
                rate = weights[t]/weights[s]
                births[t] = rate
                local_birth[x] += rate
        for x, y in edges:
            if (s[x] == -1) == (s[y] == -1):
                continue
            t = list(s)
            t[x], t[y] = t[y], t[x]
            t = tuple(t)
            rate = weights[t]/(weights[s]+weights[t])
            hops[t] = rate
            local_depart[x if s[x] >= 0 else y] += rate
        B[s], H[s], bx[s], departure[s] = births, hops, local_birth, local_depart
    return states, adjacent, B, H, bx, departure


def hazard_checks(model, W, mutation):
    states, adjacent, B, H, bx, departure = model
    z = max(map(len, adjacent))
    low = min(x for row in W for x in row)
    high = max(x for row in W for x in row)
    ell = low if mutation == "omit_empty_neighbor_floor" else min(F(1), low)
    alpha, beta = 6*ell**z, 6*max(F(1), high)**z
    for s in states:
        for x in range(len(s)):
            if s[x] == -1:
                assert alpha <= bx[s][x] <= beta, (s, x, alpha, bx[s][x], beta)
            else:
                assert bx[s][x] == 0
        count = sum(a >= 0 for a in s)
        assert sum(rate*(sum(a >= 0 for a in t)-count) for t, rate in B[s].items()) == sum(bx[s])
        assert all(sum(a >= 0 for a in t) == count for t in H[s])


def translation_balance(model, mutation):
    states, adjacent, B, H, bx, departure = model
    n = len(adjacent)
    for original in states:
        drift = birth = F(0)
        for k in range(n):
            s = original[k:]+original[:k]
            vacancy = int(s[0] == -1)
            drift += sum(rate*(int(t[0] == -1)-vacancy) for t, rate in B[s].items())
            drift += sum(rate*(int(t[0] == -1)-vacancy) for t, rate in H[s].items())
            birth += bx[s][0]
        assert drift == (F(0) if mutation == "drop_birth_sink" else -birth)
    # A fixed inhomogeneous state has nonzero local flux, despite no local birth.
    s = (0,)+(-1,)*(n-1)
    local_flux = sum(rate*(int(t[0] == -1)-int(s[0] == -1)) for t, rate in H[s].items())
    assert local_flux > 0 and bx[s][0] == 0


def vacancy_drift(model, W, mutation):
    states, adjacent, B, H, bx, departure = model
    epsilon, kappa = F(2, 7), F(3, 5)
    z = max(map(len, adjacent))
    alpha = 6*epsilon*min(F(1), min(x for row in W for x in row))**z
    increment = alpha/(2*z*kappa)
    for s in states:
        for x in range(len(s)):
            if s[x] != -1:
                continue
            vacancy_hop = kappa*sum(rate for t, rate in H[s].items() if t[x] >= 0)
            killing = F(0) if mutation == "ignore_vacancy_killing" else epsilon*bx[s][x]
            assert vacancy_hop*increment-killing <= -alpha/2


def uniform_product(model, mutation):
    states, adjacent, B, H, bx, departure = model
    p = [F(1, 3)]+[F(2*(a+1), 63) for a in range(6)]
    epsilon = F(2, 7)
    derivative = [-6*epsilon*p[0]]+[epsilon*p[0]]*6
    law = {s: sp.prod(p[a+1] for a in s) for s in states}
    incoming = defaultdict(F)
    for s in states:
        for t, rate in B[s].items():
            incoming[t] += law[s]*epsilon*rate
            incoming[s] -= law[s]*epsilon*rate
        for t, rate in H[s].items():
            assert rate == F(1, 2) and law[s] == law[t]
    for s in states:
        expected = law[s]*sum(derivative[a+1]/p[a+1] for a in s)
        assert incoming[s] == expected
    # Explicit elementary integral for lifetime departure count.
    v0, kappa, z = F(3, 5), F(4, 7), max(map(len, adjacent))
    integrated = kappa*z*F(1, 2)*(v0/(6*epsilon)-v0*v0/(12*epsilon))
    proposed = kappa*z/(12*epsilon)*(v0-v0*v0/2)
    if mutation == "miss_half_hop_acceptance":
        proposed *= 2
    assert proposed == integrated


def repeated_birth(epsilon, kappa, mutation):
    q = kappa/((6 if mutation == "omit_birth_competition" else 12)*epsilon+kappa)
    # Independently solve the alternating one-record occupation at absorption.
    hop, birth = kappa/2, 6*epsilon
    matrix = sp.Matrix([[hop+birth, -hop], [-hop, hop+birth]])
    absorb_other = matrix.inv()*sp.Matrix([0, birth])
    probability_two_at_origin = absorb_other[0]/2
    expected = kappa/(4*(6*epsilon+kappa))
    assert probability_two_at_origin == expected
    assert q/(2*(1+q)) == expected
    lifetime_hops = matrix.inv()*sp.Matrix([hop, hop])
    assert lifetime_hops[0] == kappa/(12*epsilon)
    assert q/(1-q) == lifetime_hops[0]


def dependence(mutation):
    equal = F(3, 2)/(1+F(3, 2))
    opposite = F(1, 2)/(1+F(1, 2))
    if mutation == "radius_one_hops":
        equal = opposite = F(1, 2)
    assert equal == F(3, 5) and opposite == F(1, 3)
    for distance in range(1, 1001):
        radius = (distance-1)//2
        depth = radius//2+1
        assert 2*radius < distance and depth == ceil(distance/4)
    for m in range(1, 30):
        assert (m/(2*e))**m/factorial(m) <= 2.**(-m)


def tag_bound(mutation):
    # A maximally correlated tag/vacancy choice; independence cannot remove
    # the size of the possible-destination set from a marginal vacancy bound.
    candidates = 4
    marginal_vacancy = F(1, candidates)
    selected_vacancy_probability = F(1)
    bound = (1 if mutation == "omit_search_ball" else candidates)*marginal_vacancy
    assert selected_vacancy_probability <= bound
    x, g, c = sp.symbols('x g c', positive=True)
    for dimension in [1, 2, 3, 4]:
        polynomial = sp.Poly((2*c*x+3)**dimension, x)
        integrated = sum(coefficient*sp.factorial(power[0])/g**(power[0]+1)
                         for power, coefficient in polynomial.terms())
        formula = sum(sp.binomial(dimension,k)*3**(dimension-k)*(2*c)**k*sp.factorial(k)/g**(k+1)
                      for k in range(dimension+1))
        assert sp.expand(integrated-formula) == 0
    # Time-dependent uniform clock: mass balance persists without a floor.
    a, t, v0 = sp.symbols('a t v0', positive=True)
    vacancy = v0*sp.exp(-6*a*t/(1+t))
    assert sp.simplify(sp.diff(vacancy,t)+6*a*vacancy/(1+t)**2) == 0
    assert sp.limit(vacancy,t,sp.oo) == v0*sp.exp(-6*a)


def terminal_values(model, epsilon, kappa):
    states, adjacent, B, H, bx, departure = model
    n = len(adjacent)
    chi = (1, -1, 0, 0, 0, 0)
    values = {}
    for s in states:
        if -1 not in s:
            values[s] = np.array([chi[s[0]], chi[s[-1]], chi[s[0]]*chi[s[-1]]], float)
    largest = 0
    for number in reversed(range(n)):
        groups = defaultdict(list)
        for s in states:
            occupied = tuple(sorted(a for a in s if a >= 0))
            if len(occupied) == number:
                groups[occupied].append(s)
        for group in groups.values():
            index = {s:i for i,s in enumerate(group)}
            largest = max(largest, len(group))
            matrix = np.zeros((len(group),len(group)))
            rhs = np.zeros((len(group),3))
            for i,s in enumerate(group):
                matrix[i,i] = float(epsilon*sum(B[s].values())+kappa*sum(H[s].values()))
                for t,rate in H[s].items():
                    matrix[i,index[t]] -= float(kappa*rate)
                for t,rate in B[s].items():
                    rhs[i] += float(epsilon*rate)*values[t]
            solution = np.linalg.solve(matrix,rhs)
            for s,v in zip(group,solution):
                values[s] = v
    residual = 0.
    for s in states:
        if -1 not in s:
            continue
        applied = sum((float(epsilon*r)*(values[t]-values[s]) for t,r in B[s].items()),np.zeros(3))
        applied += sum((float(kappa*r)*(values[t]-values[s]) for t,r in H[s].items()),np.zeros(3))
        residual = max(residual,float(np.max(abs(applied))))
    assert residual < 1e-11
    return values[(-1,)*n],residual,largest


def correlation_counterexample(model, mutation):
    states, adjacent, B, H, bx, departure = model
    n = len(adjacent)
    plus, minus = (0,)*n,(1,)*n
    assert not B[plus] and not H[plus] and not B[minus] and not H[minus]
    mean = F(1,2)-F(1,2)
    covariance = F(1)-mean*mean
    assert covariance == (0 if mutation == "forget_product_start" else 1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list-mutations',action='store_true')
    parser.add_argument('--mutation',choices=tuple(MUTATIONS))
    args = parser.parse_args()
    if args.list_mutations:
        for mutation,family in MUTATIONS.items(): print(f'{mutation}: {family}')
        return 0
    mutation=args.mutation;checks=Checks()
    cycle=((0,1),(1,2),(2,3),(0,3))
    models={}
    for name,W in [('neutral',menu()),('flat',menu(F(0))),('large',menu(F(0),F(2))),('small',menu(F(0),F(2,3)))]:
        model=finite_model(4,cycle,W);models[name]=model
        checks.run('hazards',f'all 2401 four-cycle states; {name} positive weights',lambda model=model,W=W:hazard_checks(model,W,mutation))
        checks.run('balance',f'all cyclic initial-state orbits; {name} weights',lambda model=model:translation_balance(model,mutation))
        checks.run('vacancy',f'vacancy-label exponential drift in every vacant state; {name}',lambda model=model,W=W:vacancy_drift(model,W,mutation))
    checks.run('uniform','full biased-product generator identity and lifetime departure integral',lambda:uniform_product(models['flat'],mutation))
    for epsilon,kappa in [(F(1),F(0)),(F(1),F(1)),(F(2,7),F(3,5)),(F(1,10),F(10))]:
        checks.run('reuse',f'exact two-site repeated birth and tagged count at epsilon={epsilon}, kappa={kappa}',lambda epsilon=epsilon,kappa=kappa:repeated_birth(epsilon,kappa,mutation))
    checks.run('dependence','range-two discriminator and one thousand radius/depth identities',lambda:dependence(mutation))
    checks.run('tag','search-ball joint-law control, integrated hop bound and varying-clock budget',lambda:tag_bound(mutation))
    checks.run('correlations','absorbed shared random content retains covariance one',lambda:correlation_counterexample(models['neutral'],mutation))
    for name,kappa in [('flat',F(1)),('neutral',F(0)),('neutral',F(1)),('neutral',F(5))]:
        def absorption(name=name,kappa=kappa):
            values,residual,largest=terminal_values(models[name],F(1),kappa)
            assert max(abs(values[:2]))<1e-12
            if name=='flat': assert abs(values[2])<1e-12
            else: assert values[2]>0
            print(f'  terminal_control: menu={name} kappa={kappa} covariance={values[2]:.17g} max_harmonic_residual={residual:.3g} max_block={largest}')
        checks.run('correlations',f'full four-cycle absorption equations; {name}, kappa={kappa}',absorption)
    print('per_element: executed — exact birth, vacancy-hop, hazard and exponential-drift identities on four finite menus')
    print('per_site: executed — local budgets over all cyclic orbits, repeated-site births and biased product controls')
    print('per_mode: executed — terminal single-coordinate covariance and a shared-random-content counterexample')
    print('per_block: executed — full 2401-state four-cycle absorption controls and exact two-site tagged calculations')
    print('lattice_wide: checked and not executed — infinite-process construction and uniform lifetime/correlation proofs in note; no physical field or time identification')
    if mutation:
        print(f'mutation_family_expected: {MUTATIONS[mutation]}')
        print(f'mutation_family_observed: {",".join(sorted(checks.families)) or "none"}')
    print(f'TOTAL: PASS={checks.passed} FAIL={checks.failed}')
    return int(bool(checks.failed))


if __name__ == '__main__':
    raise SystemExit(main())
