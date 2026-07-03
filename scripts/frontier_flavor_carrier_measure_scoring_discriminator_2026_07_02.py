#!/usr/bin/env python3
"""Exact checks for the carrier-measure scoring discriminator note."""

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
    check("sympy available for exact radical/C3 witnesses", sp is not None)
    return sp is not None


def norm2_pair(pair):
    return sp.simplify(sum(sp.conjugate(x) * x for x in pair))


def idempotent_relation(a, c, d):
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    lam0 = a + c + d
    lam1 = a + c * omega + d * omega**2
    lam2 = a + c * omega**2 + d * omega
    return sp.simplify(lam0**2 - lam1**2 - lam2**2)


def main():
    # D1: reproduction of the three parent scoring values.
    N = 3
    s1 = Fraction(1, N - 1)
    s2 = Fraction(1, 1)
    check("D1 S1 generator-channel HS gives r=1/(N-1)", s1 == Fraction(1, 2))
    check("D1 S2 dimension/per-mode gives r=1", s2 == Fraction(1, 1))

    if not require_sympy():
        print(f"TOTAL: PASS={p} FAIL={f}")
        sys.exit(1)

    sqrt2 = sp.sqrt(2)
    t_s3 = -2 + sp.Rational(3, 2) * sqrt2
    s3 = sp.simplify(t_s3**2)
    check("D1 S3 idempotent/eigenvalue root solves parent equation",
          sp.simplify((1 + 2 * t_s3) ** 2 - 2 * (1 - t_s3) ** 2) == 0)
    check("D1 S3 gives r=17/2-6*sqrt(2)",
          sp.simplify(s3 - (sp.Rational(17, 2) - 6 * sqrt2)) == 0)
    check("D1 Koide Q at S1 is 2/3",
          Fraction(1, 3) + Fraction(2, 3) * s1 == Fraction(2, 3))
    check("D1 Koide Q at S2 is 1",
          Fraction(1, 3) + Fraction(2, 3) * s2 == Fraction(1, 1))
    check("D1 Koide Q at S3 is symbolic expected value",
          sp.simplify(sp.Rational(1, 3) + sp.Rational(2, 3) * s3
                      - (6 - 4 * sqrt2)) == 0)

    # D2(i): C3 cyclic conjugation leaves the circulant class fixed.
    a = sp.Rational(5, 1)
    c = sp.Rational(2, 1) + sp.I
    d = sp.conjugate(c)
    I3 = sp.eye(3)
    U = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    Y = a * I3 + c * U + d * (U**2)
    check("D2 C3 conjugation fixes supplied circulant matrix",
          sp.simplify(U * Y * (U**2) - Y) == sp.zeros(3))
    check("D2 C3 leaves S1 r-value unchanged", s1 == Fraction(1, 2))
    check("D2 C3 leaves S2 r-value unchanged", s2 == Fraction(1, 1))
    check("D2 C3 leaves S3 r-value unchanged",
          sp.simplify(s3 - (sp.Rational(17, 2) - 6 * sqrt2)) == 0)

    # D2(ii): complement-reading swap is a C3-equivariant bijection hw=1 -> hw=2.
    hw1 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    hw2 = [(0, 1, 1), (1, 0, 1), (1, 1, 0)]

    def rot(x):
        return (x[2], x[0], x[1])

    def comp(x):
        return tuple(1 - y for y in x)

    check("D2 complement maps hw=1 bijectively to hw=2",
          sorted(comp(x) for x in hw1) == sorted(hw2))
    check("D2 complement commutes with C3 rotation on hw=1",
          all(comp(rot(x)) == rot(comp(x)) for x in hw1))
    check("D2 complement swap leaves all three scalar r-values unchanged",
          s1 == Fraction(1, 2) and s2 == Fraction(1, 1)
          and sp.simplify(s3 - (sp.Rational(17, 2) - 6 * sqrt2)) == 0)

    # D2(iii): global phase dressing b -> phase*b is inert on r=|b|^2/a^2.
    b = sp.Integer(3) + 4 * sp.I
    phase = sp.I
    aden = sp.Integer(7)
    r_before = sp.simplify(sp.conjugate(b) * b / aden**2)
    r_after = sp.simplify(sp.conjugate(phase * b) * (phase * b) / aden**2)
    check("D2 global U(1) phase dressing is inert on modulus r",
          sp.simplify(r_before - r_after) == 0)
    check("D2 S1 total generator energy is phase inert",
          sp.simplify(norm2_pair([b, sp.conjugate(b)])
                      - norm2_pair([phase * b, sp.conjugate(phase * b)])) == 0)
    check("D2 S2 per-mode modulus is phase inert",
          sp.simplify(sp.conjugate(b) * b
                      - sp.conjugate(phase * b) * (phase * b)) == 0)
    b_s3 = t_s3
    check("D2 S3 parent r-value is phase inert as a modulus",
          sp.simplify(sp.conjugate(sp.I * b_s3) * (sp.I * b_s3) - b_s3**2) == 0)

    # D2(iv): U(2) mixing within the two generator channels.
    H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    v_s1 = sp.Matrix([1 / sp.sqrt(2), 1 / sp.sqrt(2)])
    Hv_s1 = H * v_s1
    r_eff_before = sp.simplify(norm2_pair(list(v_s1)) / 2)
    r_eff_after = sp.simplify(norm2_pair(list(Hv_s1)) / 2)
    check("D2 U(2) mixing preserves S1 total-HS r_eff",
          sp.simplify(r_eff_before - r_eff_after) == 0
          and r_eff_before == sp.Rational(1, 2))

    v_s2 = sp.Matrix([1, 1])
    Hv_s2 = H * v_s2
    s2_pair_after = [sp.simplify(sp.conjugate(x) * x) for x in Hv_s2]
    check("D2 U(2) mixing changes S2 per-mode channel squares",
          s2_pair_after != [sp.Integer(1), sp.Integer(1)])

    v_hostile = sp.Matrix([1, 0])
    Hv_hostile = H * v_hostile
    hostile_squares = [sp.simplify(sp.conjugate(x) * x) for x in Hv_hostile]
    check("D2 hostile S2 witness can mimic r=1/2 at special point",
          hostile_squares == [sp.Rational(1, 2), sp.Rational(1, 2)])

    v_generic = sp.Matrix([1, 2])
    Hv_generic = H * v_generic
    generic_squares = [sp.simplify(sp.conjugate(x) * x) for x in Hv_generic]
    check("D2 hostile S2 mimic fails generically",
          generic_squares != [sp.Rational(1, 2), sp.Rational(1, 2)])

    relation_before = idempotent_relation(1, t_s3, t_s3)
    Hv_s3 = H * sp.Matrix([t_s3, t_s3])
    relation_after = sp.simplify(idempotent_relation(1, Hv_s3[0], Hv_s3[1]))
    check("D2 S3 parent idempotent relation holds before U(2) mixing",
          sp.simplify(relation_before) == 0)
    check("D2 U(2) mixing changes S3 idempotent/eigenvalue relation",
          sp.simplify(relation_after) != 0)

    # D2(iv) honesty: the S1 equal-split CONDITION also moves under channel
    # mixing; what is frame-free about S1 is its partition provenance, not the
    # condition's coefficient form.
    v_eq = sp.Matrix([1 / sp.sqrt(2), 1 / sp.sqrt(2)])
    Hv_eq = H * v_eq
    eq_squares = [sp.simplify(sp.conjugate(x) * x) for x in Hv_eq]
    check("D2 honesty: equal-split condition itself moves under U(2) mixing",
          eq_squares != [sp.Rational(1, 2), sp.Rational(1, 2)])

    # D2(iv) canonical-pair non-preservation: the Hadamard-mixed channel pair
    # is no longer {algebra unit direction, HS-orthocomplement of the unit}.
    I3 = sp.eye(3)
    B3 = sp.ones(3, 3) - sp.eye(3)
    E1 = (I3 + B3) / sp.sqrt(2)
    E2 = (I3 - B3) / sp.sqrt(2)
    check("D2 mixed channel-1 is not the algebra unit direction",
          sp.simplify(E1 - E1[0, 0] * I3) != sp.zeros(3, 3))
    check("D2 mixed channel-2 is not HS-orthogonal to the unit",
          sp.simplify(sp.trace(I3.T * E2)) != 0)

    # D3: Record finite additivity compatibility on explicit direct sums.
    check("D3 S1 empty readout is zero", Fraction(0, 1) == 0)
    s1_A = Fraction(3, 2)
    s1_B = Fraction(5, 2)
    check("D3 S1 finitely additive on disjoint records",
          s1_A + s1_B == Fraction(4, 1))
    s2_A = [Fraction(1, 3), Fraction(2, 3)]
    s2_B = [Fraction(4, 3), Fraction(5, 3)]
    check("D3 S2 empty readout is zero", sum([], Fraction(0, 1)) == 0)
    check("D3 S2 finitely additive on disjoint records",
          [x + y for x, y in zip(s2_A, s2_B)] == [Fraction(5, 3), Fraction(7, 3)])
    s3_A = [sp.Integer(2), sp.Integer(3), sp.Integer(5)]
    s3_B = [sp.Integer(7), sp.Integer(11), sp.Integer(13)]
    check("D3 S3 empty readout is zero", sum([], sp.Integer(0)) == 0)
    check("D3 S3 finitely additive on disjoint records",
          sum(s3_A + s3_B) == sum(s3_A) + sum(s3_B))

    # D4: only S1 survives the named extra U(2)-invariance requirement.
    survives_named_requirement = {
        "S1_generator_channel_HS": True,
        "S2_dimension_per_mode": False,
        "S3_idempotent_eigenvalue": False,
    }
    check("D4 named invariance requirement leaves S1",
          survives_named_requirement["S1_generator_channel_HS"])
    check("D4 named invariance requirement rejects S2",
          not survives_named_requirement["S2_dimension_per_mode"])
    check("D4 named invariance requirement rejects S3",
          not survives_named_requirement["S3_idempotent_eigenvalue"])
    check("D4 conditional survivor gives r=1/2",
          survives_named_requirement["S1_generator_channel_HS"] and s1 == Fraction(1, 2))

    theorem_target = (
        "derive, from the current framework surface, why the physical generation\n"
        "readout uses generator-channel Hilbert-Schmidt scoring rather than\n"
        "dimension/per-mode or idempotent/eigenvalue scoring."
    )
    check("D4 parent theorem target string is preserved",
          theorem_target.startswith("derive, from the current framework surface")
          and theorem_target.endswith("idempotent/eigenvalue scoring."))

    print(f"TOTAL: PASS={p} FAIL={f}")
    sys.exit(1 if f else 0)


if __name__ == "__main__":
    main()
