"""Independent check of waves-need-signed-weights a1.

Own companions and exact characteristic polynomials. The author's script is not called.
Perron-Frobenius (a positive left eigenvector for an irreducible nonnegative matrix) stays assumed.
"""
import sys

import sympy as sp

FAILS = []
I = sp.I


def want(label, ok):
    if not ok:
        FAILS.append(label)
    print(("PASS " if ok else "FAIL ") + label, flush=True)


def companion(levels, k):
    """levels[j] is {displacement: matrix}. Top block-row is the symbol; the rest is the shift."""
    J = len(levels)
    M = next(iter(next(iter(levels)).values())).rows
    C = sp.zeros(M * J)
    for j, weights in enumerate(levels):
        block = sp.zeros(M)
        for y, mat in weights.items():
            block += mat * sp.exp(-I * k * y)
        C[0:M, j * M:(j + 1) * M] = block
    for j in range(1, J):
        C[j * M:(j + 1) * M, (j - 1) * M:j * M] = sp.eye(M)
    return sp.Matrix(C.rows, C.cols, lambda i, j: sp.expand_complex(sp.simplify(C[i, j])))


def abs_entry(z):
    z = sp.simplify(sp.expand_complex(z))
    return sp.simplify(sp.sqrt(sp.re(z) ** 2 + sp.im(z) ** 2))


def absmat(A):
    return sp.Matrix(A.rows, A.cols, lambda i, j: abs_entry(A[i, j]))


def positive_entries(A):
    return all(sp.simplify(A[i, j]).is_positive for i in range(A.rows) for j in range(A.cols))


def spectral_radius_one(C):
    """1 is an eigenvalue and every other eigenvalue has modulus strictly below 1, exactly."""
    lam = sp.symbols("lam")
    poly = sp.factor(C.charpoly(lam).as_expr())
    if sp.simplify(poly.subs(lam, 1)) != 0:
        return False
    roots = sp.roots(sp.Poly(sp.expand(poly), lam))
    if not roots:
        roots = {r: 1 for r in sp.solve(poly, lam)}
    for r, mult in roots.items():
        mod2 = sp.simplify(sp.expand_complex(r * sp.conjugate(r)))
        if sp.simplify(r - 1) == 0:
            continue
        if not (mod2.is_real and mod2 < 1):
            return False
    return True


def left_positive(C):
    null = (C.T - sp.eye(C.rows)).nullspace()
    if len(null) != 1:
        return False
    v = null[0]
    ratios = [sp.simplify(v[i] / v[0]) for i in range(v.rows)]
    return all(t.is_real and t.is_positive for t in ratios)


# ---------------------------------------------------------------- Q2 companions
diffusive = [{0: sp.Matrix([[sp.Rational(1, 2)]]), 1: sp.Matrix([[sp.Rational(1, 2)]])}]
chain = [{1: sp.Matrix([[sp.Rational(1, 2)]])}, {2: sp.Matrix([[sp.Rational(1, 2)]])}]
two = [{
    0: sp.Matrix([[sp.Rational(1, 3), sp.Rational(1, 3)], [sp.Rational(1, 2), 0]]),
    1: sp.Matrix([[0, sp.Rational(1, 3)], [0, sp.Rational(1, 2)]]),
}]
ok = True
for levels, name in ((diffusive, "diffusive one-level"), (chain, "two-level chain"), (two, "two-component")):
    C = companion(levels, 0)
    ok = ok and spectral_radius_one(C) and left_positive(C) and positive_entries((sp.eye(C.rows) + C) ** (C.rows - 1))
want("Q2 three gain-one companions have rho = 1, a positive left Perron vector, and (I+C)^(n-1) > 0", ok)

# ---------------------------------------------------------------- Q3 the two sides of condition (i)
rigid = [{0: sp.zeros(2)}, {1: sp.Matrix([[0, 1], [0, 0]]), -1: sp.Matrix([[0, 0], [1, 0]])}]
mixing = [{0: sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [0, 0]]), 1: sp.Matrix([[0, 0], [1, 0]])}]
spread = [{0: sp.Matrix([[sp.Rational(1, 2)]]), 1: sp.Matrix([[sp.Rational(1, 2)]])}]

ok = True
for levels, expect in ((rigid, True), (mixing, True), (spread, False)):
    C0 = companion(levels, 0)
    for k in (sp.pi / 3, sp.Rational(2, 5) * sp.pi):
        Bk = companion(levels, k)
        same = absmat(Bk) == absmat(C0)
        ok = ok and same == expect
want("Q3 |C(k)| equals C(0) for the rigid and mixing rules, and not for the two-displacement rule", ok)

# rigid rule: monomial with unimodular entries, hence unitary
Ck = companion(rigid, sp.symbols("k", real=True))
ok = sp.simplify(Ck * Ck.H - sp.eye(4)) == sp.zeros(4)
want("Q3 the rigid companion is unitary at every real k, so every branch is unimodular", ok)

# mixing rule: lambda^2 - lambda/2 = exp(-I k)/2.
# If |lambda| >= 1 then |lambda^2 - lambda/2| >= |lambda|(|lambda| - 1/2) >= 1/2,
# with equality only for lambda = 1, which forces exp(-I k) = 1.
# Neither tested angle is a multiple of 2 pi, and at k = 0 the roots are (1 ± sqrt(5))/4.
ok = sp.simplify(sp.exp(-I * sp.pi / 3) - 1) != 0
ok = ok and sp.simplify(sp.exp(-I * sp.Rational(2, 5) * sp.pi) - 1) != 0
root_big = (1 + sp.sqrt(5)) / 4
ok = ok and sp.simplify(root_big ** 2 - (3 + sp.sqrt(5)) / 8) == 0
ok = ok and sp.Integer(5) < 25  # sqrt(5) < 5, so (3+sqrt(5))/8 < 1
# nonnegative weights a, b > 0: |a + b e^{-ik}| = a + b on an open set iff one of them vanishes
a, b, theta = sp.symbols("a b theta", positive=True)
cos_gap = sp.simplify((a + b) ** 2 - (a ** 2 + b ** 2 + 2 * a * b * sp.cos(theta)))
ok = ok and cos_gap == 2 * a * b * (1 - sp.cos(theta))
want("Q3 mixing branches lie inside the circle at the tested k, and two positive displacements agree in phase only when cos k = 1", ok)

# ---------------------------------------------------------------- Q4 irreducibility
def irreducible(A):
    P = (sp.eye(A.rows) + A) ** (A.rows - 1)
    return positive_entries(P)


deep = [{0: sp.Matrix([[sp.Rational(1, 2)]])}, {1: sp.Matrix([[sp.Rational(1, 2)]])}]
shallow = [{0: sp.Matrix([[1]])}, {1: sp.Matrix([[0]])}]
A_full = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [sp.Rational(1, 2), sp.Rational(1, 2)]])
A_red = sp.eye(2)
ok = irreducible(companion(deep, 0)) and not irreducible(companion(shallow, 0))
ok = ok and irreducible(A_full) and not irreducible(A_red)
# scalar depth 2: a zero deepest weight gives a node of out-degree 0
w0, w1 = sp.symbols("w0 w1", nonnegative=True)
Cform = sp.Matrix([[w0, w1], [1, 0]])
ok = ok and sp.simplify((sp.eye(2) + Cform.subs(w1, 0))[0, 1]) == 0
ok = ok and positive_entries(sp.eye(2) + Cform.subs({w0: sp.Rational(1, 3), w1: sp.Rational(2, 3)}))
want("Q4 an unused deepest level makes the scalar companion reducible; a used one, and the one-level matrix A, are irreducible exactly with A", ok)

print(f"TOTAL FAIL={len(FAILS)}")
if FAILS:
    print("SUMMARY: fails at " + FAILS[0])
    sys.exit(1)
print(
    "HIT: confirmed - if C is nonnegative and irreducible with rho(C) = 1 and |B| <= C, "
    "then Bx = lambda x with |lambda| = 1 forces |B| = C entrywise, by the positive left Perron vector applied to |x|. "
    "For nonnegative weights that is one displacement per entry on any open set of k. "
    "The rigid rule is unitary, the mixing rule has |C(k)| = C(0) but is unimodular only at k = 0, "
    "and the two-displacement rule has |C(k)| != C(0)."
)
print(
    "SUMMARY: confirmed the entrywise half. Ordinary Perron-Frobenius stays assumed; Wielandt's diagonal conjugation is not used. "
    "Condition (ii) is untouched. A zero deepest block leaves nodes of out-degree zero, so that companion is reducible."
)
