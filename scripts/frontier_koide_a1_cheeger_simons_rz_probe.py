#!/usr/bin/env python3
"""Finite character/phase corrections; no lattice simulation or physical no-go.

The former O13 construction is superseded. See the paired corrected note.
PASS/FAIL are ordinary computed predicates, not obstruction/closure labels.
"""
from __future__ import annotations
import sympy as sp

AUDIT_TIMEOUT_SEC = 120


def predicates():
    q = sp.Rational
    c = q(2, 9)
    omega = (-1 + sp.I * sp.sqrt(3)) / 2
    finite_sum = sp.simplify(sum(1 / ((omega**k - 1) * (omega**(2*k) - 1))
                                for k in (1, 2)) / 3)
    P = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    v = sp.ones(3, 1)
    n = sp.Symbol('n', integer=True)
    x = sp.Symbol('x', real=True)
    # On the cyclic wedge basis (dx^dy,dy^dz,dz^dx), P is the same cycle.
    return [
        ('exact finite sum equals 2/9', finite_sum == c),
        ('proposed order-three value violates domain relation', sp.Mod(3*c, 1) == q(2, 3)),
        ('all three permitted torsion values satisfy relation',
         all(sp.Mod(3*q(k, 3), 1) == 0 for k in range(3))),
        ('order-three values give cube roots of unity',
         all(sp.simplify(sp.exp(2*sp.pi*sp.I*q(k, 3))**3) == 1 for k in range(3))),
        ('standard exponential is invariant under integer shift',
         sp.simplify(sp.exp(2*sp.pi*sp.I*(x+n))/sp.exp(2*sp.pi*sp.I*x)) == 1),
        ('supplied 2/9 maps to angle 4pi/9', 2*sp.pi*c == 4*sp.pi/9),
        ('standard and literal phases differ', abs(complex(sp.N(sp.exp(2*sp.pi*sp.I*c)-sp.exp(sp.I*c), 40))) > .5),
        ('exp(i c) fails quotient representative consistency', abs(complex(sp.N(sp.exp(sp.I)-1, 40))) > .9),
        ('exp(pi i c) fails quotient representative consistency', sp.exp(sp.pi*sp.I) != 1),
        ('free-cycle supplied parameter yields literal target angle', sp.simplify(2*sp.pi/(9*sp.pi)-c) == 0),
        ('cyclic action has order three', P**3 == sp.eye(3)),
        ('one-form cyclic sum is nonzero and fixed', P*v == v and v != sp.zeros(3, 1)),
        ('one- and two-form cyclic fixed spaces have dimension one', 3-(P-sp.eye(3)).rank() == 1),
    ]


def main():
    results = predicates()
    for label, ok in results:
        print(f"[{'PASS' if bool(ok) else 'FAIL'}] {label}")
    failures = sum(not bool(ok) for _, ok in results)
    print('Scope: exact finite group/phase controls; no physical Koide selection.')
    print('per_element: finite permutation and scalar expressions evaluated.')
    print('per_site: no lattice sites, cocycle construction, or lattice simulation.')
    print('per_mode: no spectral eta or physical mode calculation.')
    print('per_block: one finite cyclic representation; no physical sector identification.')
    print('lattice_wide: quotient cohomology and physical closure remain unproved.')
    print(f'PASS={len(results)-failures} FAIL={failures}')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
