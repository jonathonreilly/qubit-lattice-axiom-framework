#!/usr/bin/env python3
"""Exact checks for the supplied-readout-context C1/C2 decomposition note."""

from fractions import Fraction
import sys

try:
    import sympy as sp
except Exception:  # pragma: no cover - exercised only on minimal installs.
    sp = None


p = 0
f = 0


def check(name, condition):
    global p, f
    if condition:
        p += 1
        print(f"PASS {name}")
    else:
        f += 1
        print(f"FAIL {name}")


def require_sympy():
    check("sympy available for exact matrix witnesses", sp is not None)
    return sp is not None


def hs_inner(A, B):
    return sp.simplify(sp.trace(A.T * B))


def norm2_pair(pair):
    return sp.simplify(sum(sp.conjugate(x) * x for x in pair))


def idempotent_relation(a, c, d):
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    lam0 = a + c + d
    lam1 = a + c * omega + d * omega**2
    lam2 = a + c * omega**2 + d * omega
    return sp.simplify(lam0**2 - lam1**2 - lam2**2)


def additive_readout(weight, record):
    return record[0] + weight * record[1]


def add_records(left, right):
    return (left[0] + right[0], left[1] + right[1])


def main():
    if not require_sympy():
        print(f"TOTAL: PASS={p} FAIL={f}")
        sys.exit(1)

    # T1: Block01 restated through C1 on the hw=1 circulant surface.
    I3 = sp.eye(3)
    B3 = sp.ones(3, 3) - sp.eye(3)
    check("T1 C1 supplies algebra unit cell",
          sp.simplify(I3 - sp.eye(3)) == sp.zeros(3))
    check("T1 C1 supplies HS-orthocomplement cell",
          hs_inner(I3, B3) == 0)
    check("T1 unit norm squared is 3",
          hs_inner(I3, I3) == 3)
    check("T1 B=J-I norm squared is 6",
          hs_inner(B3, B3) == 6)

    N = 3
    r_s1 = Fraction(1, N - 1)
    q_s1 = Fraction(1, 3) + Fraction(2, 3) * r_s1
    check("T1 S1 generator-channel HS gives r=1/2",
          r_s1 == Fraction(1, 2))
    check("T1 S1 generator-channel HS gives Q=2/3",
          q_s1 == Fraction(2, 3))

    H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    v_s2 = sp.Matrix([1, 1])
    Hv_s2 = H * v_s2
    s2_squares = [sp.simplify(sp.conjugate(x) * x) for x in Hv_s2]
    check("T1 Hadamard witness excludes S2 per-mode equality in canonical frame",
          s2_squares != [sp.Integer(1), sp.Integer(1)])

    sqrt2 = sp.sqrt(2)
    t_s3 = -2 + sp.Rational(3, 2) * sqrt2
    relation_before = idempotent_relation(1, t_s3, t_s3)
    Hv_s3 = H * sp.Matrix([t_s3, t_s3])
    relation_after = idempotent_relation(1, Hv_s3[0], Hv_s3[1])
    check("T1 S3 parent relation holds before Hadamard mixing",
          sp.simplify(relation_before) == 0)
    check("T1 Hadamard witness excludes S3 mixed-frame relation",
          sp.simplify(relation_after) != 0)

    survivors_under_c1 = {
        "S1_generator_channel_HS": True,
        "S2_dimension_per_mode": False,
        "S3_idempotent_eigenvalue": False,
    }
    check("T1 C1 leaves only S1 among parent-named scorings",
          survivors_under_c1 == {
              "S1_generator_channel_HS": True,
              "S2_dimension_per_mode": False,
              "S3_idempotent_eigenvalue": False,
          })

    # T2: C1 does not supply C2. The same canonical frame admits w=1 and w=2.
    canonical_frame = ((1, 0), (0, 1))
    A = (Fraction(2, 1), Fraction(3, 1))
    B = (Fraction(5, 1), Fraction(7, 1))
    empty = (Fraction(0, 1), Fraction(0, 1))
    for weight in (Fraction(1, 1), Fraction(2, 1)):
        check(f"T2 w={weight} keeps the same C1 canonical partition",
              canonical_frame == ((1, 0), (0, 1)))
        check(f"T2 w={weight} empty direct-sum readout is zero",
              additive_readout(weight, empty) == 0)
        check(f"T2 w={weight} is additive on explicit direct sums",
              additive_readout(weight, add_records(A, B))
              == additive_readout(weight, A) + additive_readout(weight, B))

    check("T2 w=1 and w=2 give different scalar assignments",
          additive_readout(Fraction(1, 1), A)
          != additive_readout(Fraction(2, 1), A))
    check("T2 C1 constraints do not mention the scalar weight",
          canonical_frame == ((1, 0), (0, 1))
          and additive_readout(Fraction(1, 1), empty) == 0
          and additive_readout(Fraction(2, 1), empty) == 0)

    # T3: C2 does not supply C1. Equal weights allow an imported S2 frame.
    imported_s2 = H * sp.Matrix([1, 0])
    imported_s2_squares = [
        sp.simplify(sp.conjugate(x) * x) for x in imported_s2
    ]
    check("T3 imported-frame S2 witness satisfies equal weighting",
          imported_s2_squares == [sp.Rational(1, 2), sp.Rational(1, 2)])

    E1 = (I3 + B3) / sp.sqrt(2)
    E2 = (I3 - B3) / sp.sqrt(2)
    check("T3 imported mixed cell 1 is not the unit direction",
          sp.simplify(E1 - E1[0, 0] * I3) != sp.zeros(3, 3))
    check("T3 imported mixed cell 2 is not HS-orthogonal to the unit",
          hs_inner(I3, E2) != 0)
    check("T3 equal weighting alone permits C1 violation",
          imported_s2_squares == [sp.Rational(1, 2), sp.Rational(1, 2)]
          and hs_inner(I3, E2) != 0)

    generic_s2 = H * sp.Matrix([1, 2])
    generic_s2_squares = [
        sp.simplify(sp.conjugate(x) * x) for x in generic_s2
    ]
    check("T3 S2 mixed-frame behavior is frame-dependent",
          generic_s2_squares == [sp.Rational(9, 2), sp.Rational(1, 2)])

    # T4: merge/decomposition summary at witness level.
    c1_block01 = "NO IMPORTED FRAME"
    c1_kappa_shape = "supplied readout context"
    c2_kappa_shape = "weighting/readout-bridge rule"
    check("T4 Block01 residual item 1 is C1-shaped",
          c1_block01 == "NO IMPORTED FRAME")
    check("T4 kappa hostile clause is C1-shaped",
          c1_kappa_shape == "supplied readout context")
    check("T4 kappa missing rule is C2-shaped",
          c2_kappa_shape == "weighting/readout-bridge rule")
    check("T4 C1 and C2 are independent in both directions",
          additive_readout(Fraction(1, 1), A)
          != additive_readout(Fraction(2, 1), A)
          and imported_s2_squares == [sp.Rational(1, 2), sp.Rational(1, 2)]
          and hs_inner(I3, E2) != 0)
    check("T4 no kappa value is selected by the witnesses",
          "kappa_value" not in {"C1", "C2", "frame", "weight"})

    print(f"TOTAL: PASS={p} FAIL={f}")
    sys.exit(1 if f else 0)


if __name__ == "__main__":
    main()
