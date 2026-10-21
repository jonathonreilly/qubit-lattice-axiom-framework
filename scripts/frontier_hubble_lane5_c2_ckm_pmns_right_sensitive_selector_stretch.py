#!/usr/bin/env python3
"""Supplied two-world sign countermodel; no repository-wide absence theorem."""
from fractions import Fraction

AUDIT_TIMEOUT_SEC = 300


def even_data(delta, q, magnitude):
    return delta*delta + q*q, delta*delta*q*q, magnitude


def worlds(delta, q, magnitude, ckm_sign):
    return ((ckm_sign, even_data(delta,q,magnitude), magnitude),
            (ckm_sign, even_data(-delta,q,magnitude), -magnitude))


def main():
    passed = failed = 0
    def check(label, condition):
        nonlocal passed, failed
        passed += bool(condition)
        failed += not condition
        print(f"[{'PASS' if condition else 'FAIL'}] {label}")
    # Exact rational fixtures support the polynomial sign-symmetry argument.
    for d,q,a,k in [(Fraction(1),Fraction(2),Fraction(3),1),
                    (Fraction(2,3),Fraction(-5,7),Fraction(9,11),-1)]:
        plus,minus=worlds(d,q,a,k)
        check('Supplied worlds have identical CKM sign and even data',plus[:2]==minus[:2])
        check('Supplied worlds have distinct opposite target signs',plus[2]==-minus[2] and plus[2]!=minus[2])
        prediction=k*a
        check('Additional sign-matching rule chooses exactly one supplied world',sum(prediction==x[2] for x in (plus,minus))==1)
    print('per_element: polynomial even data and signed target are explicit')
    print('per_block: supplied independent-sign tuples, not physical matrix blocks')
    print('per_site: no site model or site sweep supplied')
    print('per_mode: both target signs checked at fixed input data')
    print('lattice_wide: no lattice embedding, admissibility or cross-sector absence proof')
    print(f'SUMMARY: PASS={passed} FAIL={failed}')
    print('Scope: no function of identical supplied inputs can recover both distinct targets; physical realization and coupling laws remain open.')
    return int(failed != 0)


if __name__ == '__main__':
    raise SystemExit(main())
