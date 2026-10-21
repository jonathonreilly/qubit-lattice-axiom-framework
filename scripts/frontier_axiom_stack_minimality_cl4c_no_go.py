"""Exact countermodel to the withdrawn weight-preserving permutation inference.

Supplied finite CAR algebra only; no physical selector or audit verdict.
"""
from itertools import product
import sys
import sympy as sp

AUDIT_TIMEOUT_SEC = 120


def main():
    checks = []
    def check(label, value):
        ok = bool(value)
        checks.append(ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label}")

    # Bit i denotes occupation of mode i; preceding bits give the CAR sign.
    annihilators = []
    for i in range(4):
        a = sp.zeros(16)
        for state in range(16):
            if state & (1 << i):
                sign = (-1) ** ((state & ((1 << i) - 1)).bit_count())
                a[state ^ (1 << i), state] = sign
        annihilators.append(a)
    for i, j in product(range(4), repeat=2):
        a, b = annihilators[i], annihilators[j]
        check(f"CAR {i},{j}", a*b.H+b.H*a == (sp.eye(16) if i == j else sp.zeros(16)))
    inclusion = sp.zeros(16, 4)
    for i in range(4):
        inclusion[1 << i, i] = 1
    units = {}
    for i, j in product(range(4), repeat=2):
        units[i,j] = inclusion.H * annihilators[i].H * annihilators[j] * inclusion
        expected = sp.zeros(4)
        expected[i,j] = 1
        check(f"matrix unit {i},{j}", units[i,j] == expected)
    check("bilinear span rank sixteen", sp.Matrix.hstack(*(m.reshape(16,1) for m in units.values())).rank() == 16)
    check("all matrix-unit products", all(units[i,j]*units[k,l] == (units[i,l] if j == k else sp.zeros(4)) for i,j,k,l in product(range(4), repeat=4)))
    check("odd compression vanishes", all(inclusion.H*a*inclusion == sp.zeros(4) for a in annihilators))
    check("product compression nonzero", units[0,0] != sp.zeros(4))
    X = sp.Matrix([[0,1],[1,0]])
    Y = sp.Matrix([[0,-sp.I],[sp.I,0]])
    Z = sp.diag(1,-1)
    gammas = [sp.kronecker_product(X,sp.eye(2)), sp.kronecker_product(Y,sp.eye(2)), sp.kronecker_product(Z,X), sp.kronecker_product(Z,Y)]
    check("Hermitian Clifford generators", all(g.H == g for g in gammas))
    check("all Clifford anticommutators", all(a*b+b*a == (2*sp.eye(4) if i == j else sp.zeros(4)) for i,a in enumerate(gammas) for j,b in enumerate(gammas)))
    print(f"SUMMARY: PASS={sum(checks)} FAIL={len(checks)-sum(checks)}")
    print("Scope: supplied CAR countermodel; physical selection remains unproved.")
    print("Resolution scope and limits (not physical bridge certificates):")
    print("per_element: checked all sixteen supplied matrix units and their products.")
    print("per_block: checked only the supplied four-dimensional one-particle block.")
    print("per_mode: checked the algebra of four supplied CAR modes; their physical selection is unproved.")
    print("per_site: no physical site assignment or local realization is proved here.")
    print("lattice_wide: no lattice embedding, physical selector, or global construction is proved here.")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
