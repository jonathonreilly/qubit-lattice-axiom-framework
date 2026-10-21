#!/usr/bin/env python3
"""Conditional linear swap reduction; carrier closure alone is insufficient.

For a supplied real linear readout M with MP=M, its columns coincide and
rank(M)<=1. A swap-closed source family does not imply this premise.
The former source-token and literal-True checks are replaced by exact algebra
and a readout counterexample. No physical selector or audit status is derived.
"""
import sympy as sp

AUDIT_TIMEOUT_SEC = 120

def main():
    passed = 0
    def check(name, condition):
        nonlocal passed
        assert bool(condition), name
        passed += 1
        print('PASS:', name)
    P = sp.Matrix([[0, 1], [1, 0]])
    d, u, t = sp.symbols('d u t', real=True)
    carrier = sp.Matrix([1, d]) * sp.Matrix([[u, t]])
    check('carrier family is swap closed', carrier*P == sp.Matrix([1,d])*sp.Matrix([[t,u]]))
    check('identity readout disproves automatic swap invariance', sp.eye(2)*P != sp.eye(2))
    check('identity readout retains antisymmetric mode', sp.eye(2)*sp.Matrix([1,-1]) != sp.zeros(2,1))
    a,b,c,e = sp.symbols('a b c e', real=True)
    M = sp.Matrix([[a,b],[c,e]])
    check('invariance imposes exactly equal columns', sp.solve(list(M-M*P), [b,e]) == {b:a,e:c})
    v = sp.Matrix([a,c]); invariant = v*sp.Matrix([[1,1]])
    check('equal-column form satisfies invariance', invariant*P == invariant)
    check('invariant form kills antisymmetric source', invariant*sp.Matrix([1,-1]) == sp.zeros(2,1))
    check('factorization for every source', sp.simplify(invariant*sp.Matrix([u,t]) - v*(u+t)) == sp.zeros(2,1))
    check('rank at most one', invariant.det() == 0)
    check('zero map is allowed', invariant.subs({a:0,c:0}).rank() == 0)
    check('nonzero representative has rank one', invariant.subs({a:1,c:2}).rank() == 1)
    print(f'SUMMARY: PASS={passed} FAIL=0')

if __name__ == '__main__':
    main()
