#!/usr/bin/env python3
"""Conditional parity non-identifiability; optional numerical diagnostics are separate."""
from __future__ import annotations
import argparse
import sys
import sympy as s

AUDIT_TIMEOUT_SEC = 600


def parity_checks():
    x1,x2,x3,y1,y2,y3,d = s.symbols('x1 x2 x3 y1 y2 y3 d', real=True)
    gamma = x1*y3*s.sin(d)
    e1 = ((x2**2+y2**2)-(x3**2+y3**2)+x2*y1-x1*y3*s.cos(d))/2
    e2 = x1**2+y1**2+(x2*y1+x1*y3*s.cos(d))/2
    cycle = s.Matrix([[0,1,0],[0,0,1],[1,0,0]])
    Y = s.diag(x1,x2,x3)+s.diag(y1,y2,y3*s.exp(s.I*d))*cycle
    H = Y*Y.conjugate().T
    identities = {
        'gamma is odd': gamma.subs(d,-d)+gamma,
        'E1 is even': e1.subs(d,-d)-e1,
        'E2 is even': e2.subs(d,-d)-e2,
        'cp1 is odd': (-2*gamma*e1/3).subs(d,-d)-2*gamma*e1/3,
        'cp2 is odd': (2*gamma*e2/3).subs(d,-d)+2*gamma*e2/3,
        'phase information cost is even': (1-s.cos(d)).subs(d,-d)-(1-s.cos(d)),
    }
    results = [s.simplify(v)==0 for v in identities.values()]
    for name,ok in zip(identities,results):
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    conjugation = all(s.simplify(v)==0 for v in H.subs(d,-d)-H.conjugate())
    results.append(conjugation)
    print(f"[{'PASS' if conjugation else 'FAIL'}] H(-d)=conjugate(H(d))")
    # A supplied algebraic control, not a native-surface or physical witness.
    values={x1:1,x2:2,x3:1,y1:1,y2:1,y3:1,d:s.pi/2}
    cp=s.Matrix([-2*gamma*e1/3,2*gamma*e2/3]).subs(values)
    control=cp==s.Matrix([-s.Rational(5,3),2])
    results.append(control)
    print(f"[{'PASS' if control else 'FAIL'}] even-data ambiguity does not imply target-sign impossibility")
    print('Scope: reflected domain/constraints must be supplied; nonzero odd data give distinct sign partners.')
    print('Eigenvector-modulus packets additionally require simple eigenvalues and consistent ordering.')
    print('No stationarity, branch count, physical admissibility or transport closure is proved here.')
    print(f'PASS={sum(results)} FAIL={len(results)-sum(results)}')
    return 0 if all(results) else 1


def numerical_diagnostic():
    import frontier_dm_leptogenesis_pmns_multistart_selector_support as m
    m.part1_enumerate_stationary_branches()
    return 1 if m.FAIL_COUNT else 0


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--numerical-diagnostic',action='store_true',help='Replay separate candidate diagnostic; failure stays nonzero.')
    args=parser.parse_args()
    if not args.numerical_diagnostic:
        return parity_checks()
    print('NUMERICAL DIAGNOSTIC: no exact/global/physical selection claim.')
    try:
        return numerical_diagnostic()
    except (RuntimeError,ValueError) as exc:
        print(f'FAIL: unresolved numerical diagnostic: {exc}')
        return 1


if __name__=='__main__':
    sys.exit(main())
