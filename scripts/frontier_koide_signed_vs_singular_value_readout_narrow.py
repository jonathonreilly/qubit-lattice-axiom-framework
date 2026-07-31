#!/usr/bin/env python3
"""Exact algebra checks for the paired signed-eigenvalue/modulus-vector note.

For ``H = a I + b C + conjugate(b) C^2`` with ``a > 0``, this runner checks
the C3 character spectrum, the phase-independent signed-vector functional,
the shared component-square sum, exact phase witnesses at ``r = 1/2``, the
zero-component endpoints, and the displayed arbitrary-r counterexample.

The note supplies the analytic proof of the universal triangle-inequality and
centered phase-cell statements. Finite phase evaluations here are exact
witnesses and regression checks, not an exhaustive continuous-domain proof.
"""

import sys

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md",
)

try:
    import sympy as sp
    from sympy import (
        Rational, sqrt, cos, pi, simplify, trigsimp, symbols, Abs, N,
        exp, I, conjugate, expand,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    # Keep successful output compact enough for legacy restricted packets;
    # failed checks retain their diagnostic detail.
    suffix = f"  ({detail})" if detail and not ok else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print(f"\n== {title} ==")


# ---------------------------------------------------------------------------
# Shared symbolic ingredients
# ---------------------------------------------------------------------------
a = symbols("a", positive=True)          # I-coefficient (real, > 0 WLOG by scale)
bmod = symbols("bmod", positive=True)    # |b|
theta = symbols("theta", real=True)      # arg(b)


def signed_eigs(a_val, bmod_val, th):
    """lambda_k = a + 2|b| cos(theta + 2 pi k / 3), k = 0,1,2 (real, signed)."""
    return [a_val + 2 * bmod_val * cos(th + 2 * pi * k / 3) for k in (0, 1, 2)]


def koide_Q(w):
    """Q(w) = (sum w^2)/(sum w)^2 for a 3-vector w."""
    return sum(wi**2 for wi in w) / (sum(w)) ** 2


def main() -> int:
    print("KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29")
    print("Exact signed-eigenvalue and modulus-vector functional checks at r=1/2")

    # =====================================================================
    section("Part 0: circulant -> real spectrum sanity (lambda_k real, theta = arg b)")
    # =====================================================================
    # H = a I + b C + bbar C^2 with the standard 3x3 cyclic permutation C.
    C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    bre, bim = symbols("bre bim", real=True)
    b = bre + I * bim
    H = a * sp.eye(3) + b * C + conjugate(b) * (C * C)
    check(
        "H = aI + bC + bbar C^2 is Hermitian (H^dagger = H)",
        simplify(H - H.conjugate().T) == sp.zeros(3, 3),
        detail="circulant Hermitian family",
    )
    # The C_3 character vectors v_k = (1, w^k, w^{2k})^T are eigenvectors of the
    # circulant H, with eigenvalue lambda_k = a + b w^k + bbar w^{-k}. Verify the
    # eigenpair relation symbolically (exp form, no trig) to pin down the spectrum.
    w = exp(2 * pi * I / 3)
    eig_char = [a + b * w**k + conjugate(b) * w ** (-k) for k in (0, 1, 2)]
    eigvec_ok = True
    for k in (0, 1, 2):
        vk = sp.Matrix([1, w**k, w ** (2 * k)])
        eigvec_ok = eigvec_ok and simplify(H * vk - eig_char[k] * vk) == sp.zeros(3, 1)
    check(
        "character vectors v_k = (1, w^k, w^{2k}) are eigenvectors, eigenvalue a + b w^k + bbar w^{-k}",
        eigvec_ok,
        detail="C_3 circulant spectrum",
    )
    # Polar form: with b = |b| e^{i theta}, lambda_k = a + 2 Re(b w^k)
    #   = a + 2 |b| cos(theta + 2 pi k / 3)  (real spectrum, theta = arg b).
    polar = {bre: bmod * cos(theta), bim: bmod * sp.sin(theta)}
    target = signed_eigs(a, bmod, theta)
    ok_polar = all(
        simplify(sp.expand_complex(e.subs(polar)) - t) == 0
        for e, t in zip(eig_char, target)
    )
    check(
        "lambda_k = a + 2|b| cos(theta + 2 pi k/3) with theta = arg(b) (real spectrum)",
        ok_polar,
        detail="polar form of the C_3 character eigenvalues",
    )

    # =====================================================================
    section("Part 1: signed-vector functional Q_S = (1 + 2 r)/3")
    # =====================================================================
    lam = signed_eigs(a, bmod, theta)

    sum_lam = simplify(trigsimp(sum(lam)))
    check(
        "sum_k lambda_k = 3 a  (theta-independent; uses sum_k cos = 0)",
        simplify(sum_lam - 3 * a) == 0,
        detail=f"sum lambda = {sum_lam}",
    )

    sum_lam_sq = simplify(trigsimp(sum(l**2 for l in lam)))
    check(
        "sum_k lambda_k^2 = 3 a^2 + 6 |b|^2  (theta-independent; uses sum cos^2 = 3/2)",
        simplify(sum_lam_sq - (3 * a**2 + 6 * bmod**2)) == 0,
        detail=f"sum lambda^2 = {sum_lam_sq}",
    )

    Q_signed = simplify(trigsimp(koide_Q(lam)))
    Q_signed_target = (a**2 + 2 * bmod**2) / (3 * a**2)
    check(
        "Q_signed = (a^2 + 2|b|^2)/(3 a^2) = (1 + 2 r)/3, exact & theta-independent",
        simplify(Q_signed - Q_signed_target) == 0,
        detail=f"Q_signed = {Q_signed}",
    )
    # theta-independence made explicit: derivative w.r.t. theta is identically 0.
    dQ_dtheta = simplify(trigsimp(sp.diff(koide_Q(lam), theta)))
    check(
        "d Q_signed / d theta == 0 identically (no theta dependence)",
        simplify(dQ_dtheta) == 0,
        detail=f"dQ_signed/dtheta = {dQ_dtheta}",
    )
    # Specialize the explicit hypothesis r = |b|^2/a^2 = 1/2.
    Q_signed_at_half = simplify(Q_signed.subs(bmod, a / sqrt(2)))
    check(
        "at r = 1/2 (|b| = a/sqrt 2): Q_signed = 2/3 EXACTLY, theta-independent",
        simplify(Q_signed_at_half - Rational(2, 3)) == 0,
        detail=f"Q_signed(r=1/2) = {Q_signed_at_half}",
    )

    # =====================================================================
    section("Part 2: component-square sum invariance")
    # =====================================================================
    # |lambda_k|^2 = lambda_k^2 because each lambda_k is real.
    num_signed = sum(l**2 for l in lam)
    num_sv = sum(Abs(l) ** 2 for l in lam)
    check(
        "sum_k |lambda_k|^2 = sum_k lambda_k^2",
        simplify(trigsimp(num_sv - num_signed)) == 0,
        detail="component squares agree term by term",
    )

    # =====================================================================
    section("Part 3: exact equality and strict-inequality witnesses")
    # =====================================================================
    # Triangle inequality: sum_k |lambda_k| >= |sum_k lambda_k| = |3a| = 3a (a>0),
    # Since sum lambda_k = 3a > 0, equality holds iff all lambda_k are
    # nonnegative. Hence (sum|lambda|)^2 >=
    # (sum lambda)^2, so Q_sv = N/(sum|lambda|)^2 <= N/(sum lambda)^2 = Q_signed,
    # The universal statement is proved in the note; exact equality and strict
    # witnesses are checked here at r = 1/2.
    a0, b0 = Rational(1), 1 / sqrt(2)

    def Q_sv_exact(th):
        L = signed_eigs(a0, b0, th)
        return simplify(sum(l**2 for l in L) / (sum(Abs(l) for l in L)) ** 2)

    def Q_signed_exact(th):
        L = signed_eigs(a0, b0, th)
        return simplify(sum(l**2 for l in L) / (sum(L)) ** 2)

    # same-sign sample: theta = 0 -> lambda = (1+sqrt2, 1-sqrt2/2, 1-sqrt2/2), all > 0.
    L0 = [simplify(x) for x in signed_eigs(a0, b0, Rational(0))]
    same_sign = all(N(x) > 0 for x in L0)
    check(
        "theta = 0: all lambda_k > 0 and Q_V = Q_S = 2/3",
        same_sign
        and simplify(Q_sv_exact(Rational(0)) - Rational(2, 3)) == 0
        and simplify(Q_signed_exact(Rational(0)) - Rational(2, 3)) == 0,
        detail=f"lambda(0) = {L0}",
    )

    # opposite-sign sample: theta = pi/3 -> lambda_1 = 1 - sqrt2 < 0.
    Lp3 = [simplify(x) for x in signed_eigs(a0, b0, pi / 3)]
    has_flip = any(N(x) < 0 for x in Lp3)
    qsv_p3 = Q_sv_exact(pi / 3)
    check(
        "theta = pi/3: one lambda_k < 0 and Q_V < Q_S",
        has_flip
        and simplify(qsv_p3 - Rational(2, 3)) != 0
        and N(qsv_p3) < N(Rational(2, 3)),
        detail=f"lambda(pi/3) = {Lp3},  Q_sv = {qsv_p3} = {N(qsv_p3, 8)}",
    )

    # =====================================================================
    section("Part 4 (non-constancy): three DISTINCT exact-radical Q_sv values at r = 1/2")
    # =====================================================================
    qsv_0 = Q_sv_exact(Rational(0))           # = 2/3
    qsv_pi3 = Q_sv_exact(pi / 3)              # = 6/(9 + 4 sqrt 2)
    qsv_pi2 = Q_sv_exact(pi / 2)              # = 6/(7 + 2 sqrt 6)
    print(f"  Q_sv(0)    = {qsv_0}            = {N(qsv_0, 8)}")
    print(f"  Q_sv(pi/3) = {qsv_pi3}  = {N(qsv_pi3, 8)}")
    print(f"  Q_sv(pi/2) = {qsv_pi2}  = {N(qsv_pi2, 8)}")
    check(
        "Q_sv(pi/3) = 6/(9 + 4 sqrt 2) exactly",
        simplify(qsv_pi3 - 6 / (9 + 4 * sqrt(2))) == 0,
        detail=f"Q_sv(pi/3) = {qsv_pi3}",
    )
    check(
        "Q_sv(pi/2) = 6/(7 + 2 sqrt 6) exactly",
        simplify(qsv_pi2 - 6 / (7 + 2 * sqrt(6))) == 0,
        detail=f"Q_sv(pi/2) = {qsv_pi2}",
    )
    check(
        "Q_sv takes >= 3 DISTINCT exact values over theta -> Q_sv is NON-CONSTANT in theta",
        simplify(qsv_0 - qsv_pi3) != 0
        and simplify(qsv_pi3 - qsv_pi2) != 0
        and simplify(qsv_0 - qsv_pi2) != 0,
        detail="{2/3, 6/(9+4 sqrt2), 6/(7+2 sqrt6)} pairwise distinct",
    )
    # By contrast Q_signed is constant 2/3 at all three angles.
    check(
        "Q_S = 2/3 at all three angles while Q_V varies",
        all(
            simplify(Q_signed_exact(th) - Rational(2, 3)) == 0
            for th in (Rational(0), pi / 3, pi / 2)
        ),
        detail="Q_signed constant while Q_sv varies",
    )

    # =====================================================================
    section("Part 5: note's stated float samples theta = 0.4 -> 0.566, 0.9 -> 0.416")
    # =====================================================================
    for th_val, stated in [(Rational(4, 10), 0.566), (Rational(9, 10), 0.416)]:
        L = signed_eigs(a0, b0, th_val)
        qsv = sum(l**2 for l in L) / (sum(Abs(l) for l in L)) ** 2
        qsv_f = float(N(qsv, 12))
        qsg_f = float(N(Q_signed_exact(th_val), 12))
        signs = [int(sp.sign(N(x))) for x in L]
        print(
            f"  theta = {float(th_val):.1f}: signs = {signs}  "
            f"Q_signed = {qsg_f:.6f}  Q_sv = {qsv_f:.6f}  (stated ~{stated})"
        )
        check(
            f"theta = {float(th_val):.1f}: Q_sv = {qsv_f:.3f} matches stated ~{stated} and != 2/3",
            abs(qsv_f - stated) < 5e-3 and abs(qsv_f - 2 / 3) > 1e-3,
            detail=f"Q_sv = {qsv_f:.6f}",
        )
        check(
            f"theta = {float(th_val):.1f}: Q_signed = 2/3 (unchanged by the sign flip)",
            abs(qsg_f - 2 / 3) < 1e-12,
            detail=f"Q_signed = {qsg_f:.6f}",
        )

    # =====================================================================
    section("Part 6: sign-flip boundary at theta = pi/12 (one eigenvalue exactly 0)")
    # =====================================================================
    # Equality Q_V = Q_S holds exactly when every eigenvalue is nonnegative.
    # At r = 1/2 the boundary is where an
    # eigenvalue crosses 0:
    #   lambda_k = a(1 + sqrt2 cos(...)) = 0  <=>  cos(...) = -1/sqrt2  <=>  angle = 3 pi/4.
    # The note defines centered distance d(theta) = min_n |theta - 2 pi n/3|.
    # The strict-positive cell is d(theta) < pi/12, while equality holds on
    # d(theta) <= pi/12, including both zero-component endpoints.
    L_b = [simplify(x) for x in signed_eigs(a0, b0, pi / 12)]
    check(
        "theta = pi/12: lambda spectrum contains an EXACT zero (sign-flip boundary)",
        any(simplify(x) == 0 for x in L_b),
        detail=f"lambda(pi/12) = {L_b}",
    )
    # At theta = pi/12 one eigenvalue vanishes and the other two are positive.
    n_zero_b = sum(1 for x in L_b if simplify(x) == 0)
    n_neg_b = sum(1 for x in L_b if N(x) < 0)
    check(
        "theta = pi/12 (boundary): Q_sv = 2/3 EQUALITY still holds (one zero eigenvalue, none negative)",
        simplify(Q_sv_exact(pi / 12) - Rational(2, 3)) == 0
        and simplify(Q_signed_exact(pi / 12) - Rational(2, 3)) == 0
        and n_zero_b == 1
        and n_neg_b == 0,
        detail=f"Q_sv(pi/12) = {Q_sv_exact(pi / 12)} (= 2/3); zeros={n_zero_b}, negatives={n_neg_b} -> sum|lambda| = sum lambda = 3a",
    )
    # Just inside the window (theta = pi/20 < pi/12): all positive, Q_sv = 2/3.
    L_in = signed_eigs(a0, b0, pi / 20)
    inside_ok = all(N(x) > 0 for x in L_in) and simplify(
        Q_sv_exact(pi / 20) - Rational(2, 3)
    ) == 0
    check(
        "theta = pi/20 (inside window): all lambda > 0 and Q_sv = 2/3 exactly",
        inside_ok,
        detail="exact interior witness",
    )
    # Just outside the window (theta = pi/8 > pi/12): a flip, Q_sv < 2/3.
    L_out = signed_eigs(a0, b0, pi / 8)
    outside_ok = any(N(x) < 0 for x in L_out) and N(Q_sv_exact(pi / 8)) < N(Rational(2, 3))
    check(
        "theta = pi/8 (outside window): a sign flip occurs and Q_sv < 2/3",
        outside_ok,
        detail=f"Q_sv(pi/8) = {N(Q_sv_exact(pi/8), 8)}",
    )

    # The second centered endpoint and a representative just below the right
    # edge of an ordinary [0, 2pi/3) remainder catch one-sided modulo mistakes.
    L_b_neg = [simplify(x) for x in signed_eigs(a0, b0, -pi / 12)]
    check(
        "theta = -pi/12: one exact zero and Q_V = 2/3",
        sum(1 for x in L_b_neg if simplify(x) == 0) == 1
        and all(N(x) >= 0 for x in L_b_neg)
        and simplify(Q_sv_exact(-pi / 12) - Rational(2, 3)) == 0,
        detail=f"lambda(-pi/12) = {L_b_neg}",
    )
    translated_inside = 2 * pi / 3 - pi / 20
    L_translated = signed_eigs(a0, b0, translated_inside)
    check(
        "theta = 2pi/3 - pi/20: centered-period interior has Q_V = 2/3",
        all(N(x) > 0 for x in L_translated)
        and simplify(Q_sv_exact(translated_inside) - Rational(2, 3)) == 0,
        detail="periodic centered-distance witness",
    )

    # =====================================================================
    section("Part 7: component-square vector at theta = 0.9")
    # =====================================================================
    # Demonstrate at theta = 0.9 that componentwise squaring commutes with
    # taking absolute values, while the original vectors differ.
    th = Rational(9, 10)
    L = signed_eigs(a0, b0, th)
    squares_signed = sorted(simplify(l**2) for l in L)
    squares_modulus = sorted(simplify(Abs(l) ** 2) for l in L)
    check(
        "theta = 0.9: signed and modulus vectors have identical component squares",
        all(simplify(x - y) == 0 for x, y in zip(squares_signed, squares_modulus)),
        detail="component-square vectors agree",
    )
    signed_components = [simplify(l) for l in L]
    modulus_components = [simplify(Abs(l)) for l in L]
    check(
        "theta = 0.9: signed and modulus vectors differ",
        any(simplify(x - y) != 0 for x, y in zip(signed_components, modulus_components)),
        detail="the signed vector has a negative component",
    )

    # =====================================================================
    section("Part 8 (corollary): one-negative closed form Q_sv = N / (3a - 2 lambda_min)^2")
    # =====================================================================
    # On the region with exactly one negative eigenvalue lambda_min < 0:
    #   sum|lambda| = sum lambda - 2 lambda_min = 3a - 2 lambda_min,
    # so Q_sv = (3 a^2 + 6|b|^2) / (3a - 2 lambda_min)^2. The larger
    # denominator gives the general strict bound Q_sv < Q_signed; it gives
    # Q_sv < 2/3 only after the r = 1/2 specialization.
    for th_val in (pi / 3, pi / 2):
        L = signed_eigs(a0, b0, th_val)
        negs = [x for x in L if N(x) < 0]
        lam_min = simplify(negs[0])
        closed = simplify((3 * a0**2 + 6 * b0**2) / (3 * a0 - 2 * lam_min) ** 2)
        direct = Q_sv_exact(th_val)
        check(
            f"theta = {sp.nsimplify(th_val)}: Q_sv = (3a^2+6|b|^2)/(3a - 2 lambda_min)^2 (one-flip form)",
            simplify(closed - direct) == 0 and len(negs) == 1,
            detail=f"closed = {closed}, direct = {direct}",
        )
    # The spectrum below is realized by the same C_3 Hermitian family with
    # a = 1 and b = 19/20 - i sqrt(3)/20. It has exactly one negative eigenvalue
    # and still obeys Q_sv < Q_signed, but Q_sv is above 2/3 because r != 1/2.
    b_counter = Rational(19, 20) - I * sqrt(3) / 20
    counter_eigs = [Rational(29, 10), Rational(1, 5), -Rational(1, 10)]
    counter_from_c3 = [
        simplify(sp.expand_complex(1 + b_counter * w**k + conjugate(b_counter) * w ** (-k)))
        for k in (0, 1, 2)
    ]
    counter_num = simplify(sum(x**2 for x in counter_eigs))
    qsv_counter = simplify(counter_num / (sum(abs(x) for x in counter_eigs)) ** 2)
    qsigned_counter = simplify(counter_num / (sum(counter_eigs)) ** 2)
    check(
        "general one-negative counterexample: Q_sv can exceed 2/3 while still below Q_signed",
        all(simplify(x - y) == 0 for x, y in zip(counter_from_c3, counter_eigs))
        and sum(1 for x in counter_eigs if x < 0) == 1
        and simplify(qsv_counter - Rational(423, 512)) == 0
        and simplify(qsigned_counter - Rational(47, 50)) == 0
        and qsv_counter > Rational(2, 3)
        and qsv_counter < qsigned_counter,
        detail=f"spectrum={counter_eigs}, Q_sv={qsv_counter}, Q_signed={qsigned_counter}",
    )

    # =====================================================================
    section("Summary")
    # =====================================================================
    print("  Symbolic identities and exact finite witnesses completed.")
    print("  Universal inequality and centered phase-cell proofs remain source-level algebra.")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
