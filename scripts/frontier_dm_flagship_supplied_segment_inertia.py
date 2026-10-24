#!/usr/bin/env python3
"""Exact certificate for one supplied rounded affine Hermitian segment.

Owns the segment proof only. The PMNS fit is a separately bound conditional
dependency; no full-chamber connectivity or physical branch selection follows.
All sign decisions below use exact rational interval arithmetic, not float
roundoff. Decimal output is a display of proven enclosures.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    'docs/DM_FLAGSHIP_CLOSURE_REVIEW_NOTE_2026-04-17.md',
    'docs/PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md',
    'scripts/frontier_pmns_from_dm_neutrino_source_h_diagonalization_closure_theorem.py',
    'scripts/data/pr9844_supplied_segment_reference.json',
)

import json
import math
from pathlib import Path
from fractions import Fraction as F
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def plus(a, b):
    return (a[0] + b[0], a[1] + b[1])


def times(a, b):
    products = [x*y for x in a for y in b]
    return (min(products), max(products))


def enclosure(expr):
    """Enclose rational/radical polynomial coefficients by exact fractions."""
    if expr.is_Rational:
        value = F(int(expr.p), int(expr.q))
        return (value, value)
    if expr.is_Add:
        result = (F(0), F(0))
        for term in expr.args:
            result = plus(result, enclosure(term))
        return result
    if expr.is_Mul:
        result = (F(1), F(1))
        for term in expr.args:
            result = times(result, enclosure(term))
        return result
    if expr.is_Pow and expr.exp == sp.Rational(1, 2) and expr.base.is_Integer:
        n, scale = int(expr.base), 10**40
        lower = math.isqrt(n * scale**2)
        assert lower**2 <= n * scale**2 < (lower+1)**2
        return (F(lower, scale), F(lower+1, scale))
    raise ValueError(f'Unsupported exact expression: {expr}')


def evaluate(poly, interval):
    result = (F(0), F(0))
    for coefficient in poly.all_coeffs():
        result = plus(times(result, interval), enclosure(coefficient))
    return result


def main():
    t = sp.Symbol('t', real=True)
    E1, E2, gamma = sp.sqrt(sp.Rational(8, 3)), sp.sqrt(8)/3, sp.Rational(1, 2)
    base = sp.Matrix([[0,E1,-E1-sp.I*gamma],[E1,0,-E2],[-E1+sp.I*gamma,-E2,0]])
    Tm = sp.Matrix([[1,0,0],[0,0,1],[0,1,0]])
    Td = sp.Matrix([[0,-1,1],[-1,1,0],[1,0,-1]])
    Tq = sp.Matrix([[0,1,1],[1,0,1],[1,1,0]])
    endpoint = tuple(sp.Rational(x) for x in ('0.657061','0.933806','0.715042'))
    path = base + t*sum((c*M for c,M in zip(endpoint,(Tm,Td,Tq))), sp.zeros(3))
    assert path == path.conjugate().T
    determinant = sp.Poly(sp.expand(path.det()), t)
    reference = json.loads((ROOT/AUDIT_INPUT_PATHS[3]).read_text())
    expected = sp.sympify(reference['determinant_polynomial'], locals={'t':t})
    assert sp.expand(determinant.as_expr()-expected) == 0
    assert determinant.degree() == 3
    derivative = determinant.diff()
    assert derivative.degree() == 2

    # Rational brackets from independently reported decimal locations; exact
    # derivative signs, not those decimal observations, certify the roots.
    inside = (F('0.775569801340639'), F('0.775569801340641'))
    outside = (F('1.127365661486394'), F('1.127365661486397'))
    assert evaluate(derivative,(inside[0],inside[0]))[1] < 0
    assert evaluate(derivative,(inside[1],inside[1]))[0] > 0
    assert evaluate(derivative,(outside[0],outside[0]))[0] > 0
    assert evaluate(derivative,(outside[1],outside[1]))[1] < 0
    assert 0 < inside[0] < inside[1] < 1 < outside[0] < outside[1]
    # A degree-two polynomial with sign changes in two disjoint intervals
    # has exactly one real root in each and no other roots.
    values = [evaluate(determinant,(F(0),F(0))),
              evaluate(determinant,(F(1),F(1))),
              evaluate(determinant,inside)]
    assert all(low > 0 for low,high in values)
    assert values[2][1] < min(values[0][0],values[1][0])
    assert F('0.8783091593') < values[2][0] < values[2][1] < F('0.8783091594')
    # Continuous cubic on [0,1] attains a minimum at endpoints or an interior
    # derivative zero. The complete candidate set above certifies positivity.
    assert sp.trace(base) == 0
    assert sp.simplify(base.det()-32*sp.sqrt(2)/9) == 0
    assert enclosure(sp.simplify(base.det()))[0] > 0
    # Hermitian + nonzero determinant gives three nonzero real eigenvalues.
    # Positive product permits 0 or 2 negative values; trace zero excludes 0.
    # Nonsingularity along the continuous Hermitian path preserves (2,0,1).
    assert enclosure(E1)[0] > 0  # baseline delta=q=0 is outside active chamber
    note = (ROOT/AUDIT_INPUT_PATHS[0]).read_text()
    assert 'baseline itself is outside' in note and 'physical sheet remains an open' in note
    print('Exact supplied segment: endpoint =', endpoint)
    print('determinant polynomial =', determinant.as_expr())
    print('Complete derivative-root brackets:', inside, outside)
    for label,(lo,hi) in zip(('t=0','t=1','interior stationary value'),values):
        print(label, 'exact interval =', str(lo), str(hi))
        print(label, 'decimal display =', float(lo), float(hi))
    print('Certified global minimum on this supplied segment lies in (0.8783091593, 0.8783091594).')
    print('Baseline and entire segment inertia (negative,zero,positive) = (2,0,1).')
    print('The baseline is outside the imposed active chamber; no chamber path or physical-sheet selection follows.')
    print('Supplied PMNS fit dependency is bound, not recomputed or promoted.')
    print('PASS: exact matrix polynomial, complete quadratic root brackets, positive segment determinant, inertia implication.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
