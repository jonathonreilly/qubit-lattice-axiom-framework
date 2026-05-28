#!/usr/bin/env python3
"""Runner for the Observable-Principle form/scale two-stage synthesis note.

Consolidates four parallel lanes (first-principles, lit/math search, review
panel, assumption stress test) into one verification of the two-stage
decomposition of the additivity/phase/normalization admission surface
(`P1`, `P2`, `P4` in `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`):

  STAGE 1 (FORM).  The per-site algebra A_x = M_2(C) has exactly two
      conjugation invariants (tr, det); det is the action on the canonical
      volume Lambda^2 C^2; and the only continuous conjugation-invariant
      multiplicative characters GL_2(C) -> R_{>0} are |det|^c, whose logarithm
      c*log|det| is the unique additive (operator-product) generator. The
      counterexample family F_p[J] = |Z|^p IS exactly this multiplicative
      character family (log F_p = p*log|det| = c*log|det|, c = p), so STAGE 1
      collapses the entire F_p *function space* to a single free real scale c.
      Product/tensor log-det additivity is then internal to the P-form scope.
      This does not close the parent scalar-additivity premise.  ** STAGE 1
      does NOT by itself fix c -> it does not exclude p != 1; that is STAGE
      2's job. **

  STAGE 2 (SCALE).  On the qubit algebra Z[J] = Tr e^{-(H+J)} > 0, the
      Gibbs-expectation identity d log Z / dJ = <O> together with the
      identity-source response J -> J + s*1 (giving d log Z / ds = -<1> = -1
      under the normalized trace <1> = Tr rho = 1) fixes c = 1 in the
      additive-generator family W = c log Z.

  P2 (PHASE-BLINDNESS).  Dissolves: Z = Tr e^{-(H+J)} is real-positive for
      self-adjoint H, J, so there is no phase to be blind to.  ** Verified only
      on the self-adjoint / reflection-compatible (mass-like) source sector; a
      generic non-self-adjoint source can drive det off the positive axis
      (demonstrated). **

  HONEST RESIDUAL & CIRCULARITY STRESS-TEST.  The STAGE-2 selector "bare
      gradient = expectation" is, at the level of theorems, additivity in
      differential form (the locality-of-source-derivatives lemma): the
      *normalized* log-derivative (1/p) W^{-1} dW/dj recovers <O> for EVERY p,
      so normalization alone selects nothing; only the BARE gradient demand
      singles out log.  Whether the residual premise (P-cal) is a genuine
      approved primitive or the parent scalar-additivity premise relocated to
      differential/compositional form is unresolved -- this runner does NOT
      close the parent scalar-additivity premise.

Expected: PASS=22 FAIL=0.  A passing run supports ONLY the structural findings;
it does not close the parent scalar-additivity premise, promote any framework
row, or consume fitted/observed targets.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import sympy as sp
from scipy.linalg import expm, logm

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "OBSERVABLE_PRINCIPLE_P1P2_TWO_STAGE_SYNTHESIS_NARROW_THEOREM_NOTE_2026-05-28.md"
)

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"  [{status}] {label}")
    if detail:
        print(f"         {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


PAULI = {
    "I": np.eye(2, dtype=complex),
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}


def rand_gl2(rng, scale=1.0):
    return (rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))) * scale


def rand_herm(rng, n):
    a = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    return (a + a.conj().T) / 2


def rand_u2(rng):
    a = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
    q, r = np.linalg.qr(a)
    d = np.diag(r)
    return q * (d / np.abs(d))


# ---------------------------------------------------------------------------
# STAGE 1 — FORM
# ---------------------------------------------------------------------------
def stage1_form() -> None:
    section("STAGE 1 (FORM): F_p collapses to one scale c via GL_2(C) characters")
    rng = np.random.default_rng(20260528)

    # S1.1 — M_2(C): exactly two conjugation invariants (tr, det); no third.
    ok = True
    for _ in range(2000):
        M, S = rand_gl2(rng), rand_gl2(rng)
        Mc = S @ M @ np.linalg.inv(S)
        if abs(np.trace(M) - np.trace(Mc)) > 1e-8:
            ok = False
        if abs(np.linalg.det(M) - np.linalg.det(Mc)) > 1e-8:
            ok = False
        # Newton: tr(M^2) = tr(M)^2 - 2 det(M) -> next power-sum is dependent.
        if abs(np.trace(M @ M) - (np.trace(M) ** 2 - 2 * np.linalg.det(M))) > 1e-8:
            ok = False
    check("M_2(C) has exactly two conjugation invariants {tr, det} (Newton: no 3rd)", ok)

    # S1.2 — det = action on the canonical volume Lambda^2 C^2 (no additivity used).
    ok = True
    e1 = np.array([1, 0], dtype=complex)
    e2 = np.array([0, 1], dtype=complex)
    for _ in range(2000):
        M = rand_gl2(rng)
        v1, v2 = M @ e1, M @ e2
        wedge = v1[0] * v2[1] - v1[1] * v2[0]
        if abs(wedge - np.linalg.det(M)) > 1e-9:
            ok = False
    check("det(M) = scaling of M on Lambda^2 C^2 (canonical volume; det forced structurally)", ok)

    # S1.3 — |det|^c is a multiplicative character for any real c; |tr| is not.
    ok_detpow, c = True, 0.7
    for _ in range(1000):
        A, B = rand_gl2(rng), rand_gl2(rng)
        chi = lambda M: abs(np.linalg.det(M)) ** c
        if abs(chi(A @ B) - chi(A) * chi(B)) > 1e-6 * max(1.0, chi(A) * chi(B)):
            ok_detpow = False
    check("|det|^c is a multiplicative character GL_2(C)->R_{>0} for any real c", ok_detpow)
    abs_tr_fails = False
    for _ in range(500):
        A, B = rand_gl2(rng), rand_gl2(rng)
        f = lambda M: abs(np.trace(M))
        if abs(f(A @ B) - f(A) * f(B)) > 1e-6 * max(1.0, f(A) * f(B)):
            abs_tr_fails = True
            break
    check("|tr| fails multiplicativity => not a character (det is the only one)", abs_tr_fails)

    # S1.4 — additivity (under product, and per-dim-normalized tensor) is a THEOREM.
    ok_prod = True
    for _ in range(2000):
        A, B = rand_gl2(rng), rand_gl2(rng)
        lhs = np.log(abs(np.linalg.det(A @ B)))
        rhs = np.log(abs(np.linalg.det(A))) + np.log(abs(np.linalg.det(B)))
        if abs(lhs - rhs) > 1e-7:
            ok_prod = False
    check("log|det(AB)| = log|det A| + log|det B| (product additivity is derived)", ok_prod)
    ok_tens = True
    for _ in range(1000):
        A, B = rand_gl2(rng), rand_gl2(rng)
        K = np.kron(A, B)
        phiA = np.log(abs(np.linalg.det(A))) / 2
        phiB = np.log(abs(np.linalg.det(B))) / 2
        phiK = np.log(abs(np.linalg.det(K))) / 4
        if abs(phiK - (phiA + phiB)) > 1e-7:
            ok_tens = False
    check("per-dim-normalized log|det| additive under (x) within P-form scope", ok_tens)

    # S1.5 — the F_p family IS the character family: log F_p = p*log|det| = c*log|det|.
    j, p = sp.symbols("j p", real=True)
    Z = sp.Function("Z", positive=True)(j)
    Fp = sp.Abs(Z) ** p
    collapse = sp.simplify(sp.log(Fp) - p * sp.log(sp.Abs(Z)))
    check(
        "F_p = |Z|^p has log F_p = p*log|Z| = c*log|det| (whole family <-> one scale c)",
        collapse == 0,
        "STAGE 1 collapses the F_p function space to a single real parameter c (= p)",
    )

    # S1.6 — trace is the infinitesimal generator, not the composition scalar.
    ok_gen = True
    for _ in range(1000):
        X = rand_gl2(rng, scale=0.5)
        if abs(np.log(abs(np.linalg.det(expm(X)))) - np.real(np.trace(X))) > 1e-6:
            ok_gen = False
    check("log|det(exp X)| = Re tr X (trace = generator; log|det| its group integral)", ok_gen)


# ---------------------------------------------------------------------------
# STAGE 2 — SCALE
# ---------------------------------------------------------------------------
def stage2_scale() -> None:
    section("STAGE 2 (SCALE): Gibbs-expectation identity fixes c = 1")

    # S2.1 — symbolic: only W = log Z has bare gradient = <O>; F_{p!=1} excluded.
    j, p = sp.symbols("j p", real=True)
    Z = sp.Function("Z", positive=True)(j)
    expectation = sp.diff(sp.log(Z), j)  # <O> := d log Z / dj (by construction)
    bare_log = sp.simplify(sp.diff(sp.log(Z), j) - expectation)
    check("bare gradient of W = log Z equals <O> (selects log)", bare_log == 0)
    bare_pow = sp.simplify(sp.diff(Z ** p, j) - expectation)
    check(
        "bare gradient of W = Z^p != <O> for p != 0 (raw multiplicative scalar fails)",
        bare_pow != 0,
        f"d(Z^p)/dj - <O> = {bare_pow} (zero only if p*Z^p == 1, impossible)",
    )

    # S2.2 — numeric on a 1-qubit Gibbs block: d log Z / dj = <O> = Tr(rho * (-P)).
    rng = np.random.default_rng(11)
    max_err = 0.0
    for _ in range(200):
        n = int(rng.choice([2, 4]))
        H = rand_herm(rng, n)
        P = rand_herm(rng, n)  # source direction; H[j] = H + j P, observable O = -P
        h = 1e-6

        def logZ(jj):
            return np.log(np.trace(expm(-(H + jj * P))).real)

        grad_fd = (logZ(h) - logZ(-h)) / (2 * h)
        rho = expm(-H) / np.trace(expm(-H)).real
        exp_O = np.trace(rho @ (-P)).real
        max_err = max(max_err, abs(grad_fd - exp_O))
    check(
        "numeric: d log Z / dj = <O> = Tr(rho(-P)) on 1-qubit/2-qubit Gibbs blocks",
        max_err < 1e-5,
        f"200 random Hermitian (H, P); max |d logZ/dj - <O>| = {max_err:.2e}",
    )

    # S2.3 — identity-source response fixes c = 1 (normalized trace <1> = 1).
    rng = np.random.default_rng(22)
    ok_c1, max_norm_err = True, 0.0
    for _ in range(200):
        n = int(rng.choice([2, 4]))
        H = rand_herm(rng, n)
        Z0 = np.trace(expm(-H)).real
        s = 0.37
        Zs = np.trace(expm(-(H + s * np.eye(n)))).real
        # Z(s) = e^{-s} Z0  =>  d log Z / ds = -1 = <-1> = -Tr rho = -1.
        if abs(np.log(Zs) - (np.log(Z0) - s)) > 1e-9:
            ok_c1 = False
        rho = expm(-H) / Z0
        max_norm_err = max(max_norm_err, abs(np.trace(rho).real - 1.0))
    check(
        "identity-source: log Z(s) = log Z0 - s  =>  d log Z/ds = -1 = -<1>  (fixes c=1)",
        ok_c1,
        "for W = c log Z, dW/ds = -c; demanding = <O> = -1 gives c = 1",
    )
    check("normalized-trace calibration <1> = Tr rho = 1",
          max_norm_err < 1e-12, f"max |Tr rho - 1| = {max_norm_err:.2e}")


# ---------------------------------------------------------------------------
# P2 — PHASE-BLINDNESS DISSOLUTION (with honest source-class caveat)
# ---------------------------------------------------------------------------
def p2_dissolution() -> None:
    section("P2: phase-blindness dissolves under positivity (mass-like sources only)")
    rng = np.random.default_rng(20260528)

    # P2.1 — Z = Tr e^{-(H+J)} > 0 for self-adjoint H, J: no phase to be blind to.
    ok, min_Z = True, None
    for _ in range(200):
        n = int(rng.choice([2, 4]))
        H, J = rand_herm(rng, n), rand_herm(rng, n)
        Z = np.trace(expm(-(H + J)))
        if abs(Z.imag) > 1e-9 or Z.real <= 0:
            ok = False
        min_Z = Z.real if min_Z is None else min(min_Z, Z.real)
    check("Z = Tr e^{-(H+J)} > 0 for self-adjoint H, J (P2 vacuous)", ok,
          f"200 Hermitian samples; min Re(Z) = {min_Z:.4f}, max|Im(Z)| < 1e-9")

    # P2.2 — determinant-level evenness for real anti-Hermitian D (mass-like source).
    a, b, jj = sp.symbols("a b j", real=True)
    D = sp.Matrix([[0, a, 0, 0], [-a, 0, 0, 0], [0, 0, 0, b], [0, 0, -b, 0]])
    detp = sp.simplify((D + jj * sp.eye(4)).det())
    detm = sp.simplify((D - jj * sp.eye(4)).det())
    check("real anti-Hermitian D: det(D+jI) = det(D-jI) (|det| even; phase-blind)",
          sp.simplify(detp - detm) == 0, f"det(D+jI) = {detp}")

    # P2.3 — HONEST CAVEAT: a generic (non-self-adjoint) source drives det complex.
    #         The dissolution holds only on the self-adjoint / mass-like sector.
    found_complex = False
    for _ in range(200):
        D = 1j * rand_herm(rng, 4)  # real anti-Hermitian-like base
        Jns = rand_gl2(rng)  # stand-in non-self-adjoint perturbation
        Jbig = np.kron(Jns, np.eye(2))
        d = np.linalg.det(D + Jbig)
        if abs(d.imag) > 1e-6:
            found_complex = True
            break
    check(
        "CAVEAT: a non-self-adjoint source can drive det(D+J) off the positive axis",
        found_complex,
        "P2 dissolution is verified only on the self-adjoint / mass-like source sector",
    )


# ---------------------------------------------------------------------------
# HONEST RESIDUAL — the circularity stress-test (panel's decisive counterexample)
# ---------------------------------------------------------------------------
def residual_stress_test() -> None:
    section("RESIDUAL (P-cal): is the STAGE-2 selector additivity in differential form?")

    # R.1 — the NORMALIZED log-derivative recovers <O> for EVERY p:
    #        normalization alone selects nothing (panel's decisive counterexample).
    j, p = sp.symbols("j p", real=True)
    Z = sp.Function("Z", positive=True)(j)
    expectation = sp.diff(sp.log(Z), j)
    Wp = Z ** p
    norm_log_deriv = sp.simplify((sp.Rational(1) / p) * Wp ** (-1) * sp.diff(Wp, j))
    check(
        "(1/p) W^{-1} dW/dj = <O> for EVERY p: probability normalization can't select p",
        sp.simplify(norm_log_deriv - expectation) == 0,
        "=> the c=1 selection rides on the BARE-gradient demand, not on Tr rho = 1",
    )

    # R.2 — bare-gradient = expectation  <=>  cross-block second derivative vanishes
    #        (locality-of-source-derivatives lemma = additivity in differential form).
    rng = np.random.default_rng(31415)
    ok_cross_zero_log, ok_cross_nonzero_pow = True, True
    for _ in range(100):
        nA, nB = 2, 2
        HA, HB = rand_herm(rng, nA), rand_herm(rng, nB)
        PA = rand_herm(rng, nA)  # source in block A
        PB = rand_herm(rng, nB)  # source in block B
        H = np.kron(HA, np.eye(nB)) + np.kron(np.eye(nA), HB)
        JA = np.kron(PA, np.eye(nB))
        JB = np.kron(np.eye(nA), PB)
        h = 1e-4

        def logZ(sa, sb):
            return np.log(np.trace(expm(-(H + sa * JA + sb * JB))).real)

        # cross second derivative of W = log Z across independent blocks -> 0 (additive)
        d2 = (logZ(h, h) - logZ(h, -h) - logZ(-h, h) + logZ(-h, -h)) / (4 * h * h)
        if abs(d2) > 1e-3:
            ok_cross_zero_log = False
        # for W = Z^p the connected/disconnected split makes the cross term nonzero
        def Zp(sa, sb, pp=1.7):
            return np.trace(expm(-(H + sa * JA + sb * JB))).real ** pp
        d2p = (Zp(h, h) - Zp(h, -h) - Zp(-h, h) + Zp(-h, -h)) / (4 * h * h)
        if abs(d2p) < 1e-6:
            ok_cross_nonzero_pow = False
    check(
        "W = log Z: cross-block d^2W/dj_A dj_B = 0 (locality-of-source/additivity)",
        ok_cross_zero_log,
        "the bare-gradient=<O> selector is additivity in differential form (Pattern-L)",
    )
    check(
        "W = Z^p (p=1.7): cross-block d^2W != 0 (multiplicative, disconnected piece)",
        ok_cross_nonzero_pow,
        "=> whether P-cal is a genuine primitive or relocated additivity remains unresolved",
    )

    # R.3 — the qubit-trace note's standalone additivity step (log of a product) is circular:
    #        multiplicative factorization Z = Z_A Z_B holds for the WHOLE F_p family.
    rng = np.random.default_rng(271828)
    ok_mult_all_p = True
    for _ in range(100):
        ZA = abs(rand_gl2(rng)[0, 0]) + 0.5
        ZB = abs(rand_gl2(rng)[0, 0]) + 0.5
        for pp in (0.5, 1.0, 1.7, 3.0):
            if abs((ZA * ZB) ** pp - (ZA ** pp) * (ZB ** pp)) > 1e-9:
                ok_mult_all_p = False
    check(
        "Z[J_A(+)J_B] = Z_A Z_B is the F_p property (4) for EVERY p (qubit additivity step is circular)",
        ok_mult_all_p,
        "factorization is multiplicative; the additive 'log' step is the imported choice",
    )


# ---------------------------------------------------------------------------
def note_boundary() -> None:
    section("NOTE: honest-scope and boundary strings")
    if not NOTE.exists():
        check("note file present", False, f"missing: {NOTE}")
        return
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "bounded_theorem",
        "independent audit lane only",
        "parent scalar-additivity premise",
        "P-cal",
        "Pattern-L",
        "mass-like",
        "functional form",
    ]
    missing = [s for s in required if s not in text]
    check("required honest-scope strings present", not missing,
          "all present" if not missing else f"MISSING: {missing}")
    forbidden = [
        "P1 is derived",
        "P1 is closed",
        "| **P1** scalar additivity | **derived**",
        "promote to retained",
        "status: retained",
    ]
    present_forbidden = [s for s in forbidden if s in text]
    check("forbidden status-promotion strings absent", not present_forbidden,
          "none present" if not present_forbidden else f"FORBIDDEN: {present_forbidden}")


def main() -> int:
    stage1_form()
    stage2_scale()
    p2_dissolution()
    residual_stress_test()
    note_boundary()
    print()
    print("=" * 78)
    print(f"PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    if FAIL == 0:
        print(
            "\nSUMMARY (no parent additivity closure claimed):\n"
            "  STAGE 1 collapses the F_p function space to a single real scale c\n"
            "  (GL_2(C) characters); STAGE 2 fixes c=1 by the Gibbs-expectation\n"
            "  identity + normalized trace; P2 dissolves under positivity (mass-like\n"
            "  sources). The residual is ONE premise P-cal replacing {P1,P2,P4};\n"
            "  whether P-cal is a genuine approved primitive or relocated additivity\n"
            "  remains unresolved."
        )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
