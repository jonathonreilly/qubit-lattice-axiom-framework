#!/usr/bin/env python3
"""
abj_residual_gw_not_necessary_runner.py
---------------------------------------

Runner paired with
    ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28.md

Source-only proposal. Status authority: independent audit lane only.

Verifies, on the FREE (U = 1) staggered Dirac operator on the same
Z^4 = Z_4 x Z_2^3 substrate used by the U(1)_Y Jacobian note
(L_t = 4, L_s = 2; plus a symmetric L = 4 robustness lattice), the two
framework-internal facts that correct the (P1') residual justification
("robust non-zero indices on staggered Dirac generally require the
overlap-Dirac construction (Adams 2002)"):

  (G1) eps-GAP. With {eps, D} = 0 and K = eps D (Hermitian, {eps, K} = 0),
       the massive family H(m) = eps(D - m) = K - m eps satisfies the
       EXACT operator identity
           H(m)^2 = K^2 + m^2 I ,   with  K^2 = -D^2 = D^dag D >= 0.
       Since min spec(K^2) = 0 (the massless free operator has a zero
       mode), min|spec H(m)| = |m|. For m != 0 no eigenvalue of H(m)
       crosses zero, so the spectral flow / K^1 index is identically 0.
       The eps-grading that would carry internal chirality is exactly
       what gaps H(m)^2 and forbids the flow.

  (G2) chi = 0. A[1, 1] = Tr[eps exp(-t D^dag D)] = 0 and t-independent on
       the free/flat background, by the eps D eps = -D spectral +/-
       pairing ([eps, D^dag D] = 0; D spectrum symmetric lambda -> -lambda).

These are exact finite-dimensional linear-algebra facts. The
Ginsparg-Wilson relation is NOT used anywhere, and no external result is
invoked numerically: the runner demonstrates that "no GW => must import
overlap" mis-states the obstruction. The obstruction is the eps-gap +
chi = 0 on the flat/free background, and the open residual (P1') is the
existence of a chi != 0 / Q != 0 background.

PASS/FAIL counted per-check; exits 0 iff PASS_COUNT > 0 and FAIL_COUNT == 0.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import sys
from itertools import product

try:
    import numpy as np
except Exception as exc:  # pragma: no cover
    print(f"FAIL: numpy not available: {exc}")
    sys.exit(1)


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"[{status}] {name}"
    if detail:
        msg += f"  {detail}"
    print(msg)


# ---------------------------------------------------------------------------
# Free staggered Dirac operator and site-parity grading.
# Same construction (Kogut-Susskind phases, eps = (-1)^{sum x}) as the
# U(1)_Y Jacobian note's runner, specialized to the free background U = 1.
# ---------------------------------------------------------------------------

def site_index(x, L):
    return (
        (x[0] % L[0]) * (L[1] * L[2] * L[3])
        + (x[1] % L[1]) * (L[2] * L[3])
        + (x[2] % L[2]) * L[3]
        + (x[3] % L[3])
    )


def epsilon_diagonal(L) -> np.ndarray:
    """eps(x) = (-1)^{x_0 + x_1 + x_2 + x_3}, site-diagonal."""
    N = L[0] * L[1] * L[2] * L[3]
    eps = np.zeros(N, dtype=np.float64)
    for x in product(range(L[0]), range(L[1]), range(L[2]), range(L[3])):
        eps[site_index(x, L)] = (-1.0) ** (x[0] + x[1] + x[2] + x[3])
    return eps


def ks_phase(mu: int, x) -> float:
    """Standard Kogut-Susskind staggered phases.

    eta_0 = 1, eta_1 = (-1)^{x_0}, eta_2 = (-1)^{x_0+x_1},
    eta_3 = (-1)^{x_0+x_1+x_2}.
    """
    if mu == 0:
        return 1.0
    if mu == 1:
        return (-1.0) ** (x[0])
    if mu == 2:
        return (-1.0) ** (x[0] + x[1])
    if mu == 3:
        return (-1.0) ** (x[0] + x[1] + x[2])
    raise ValueError(mu)


def free_staggered_D(L) -> np.ndarray:
    """Massless free (U = 1) staggered Dirac operator on the periodic lattice L."""
    N = L[0] * L[1] * L[2] * L[3]
    D = np.zeros((N, N), dtype=np.complex128)
    for x in product(range(L[0]), range(L[1]), range(L[2]), range(L[3])):
        i = site_index(x, L)
        for mu in range(4):
            eta = ks_phase(mu, x)
            xp = list(x)
            xp[mu] = (xp[mu] + 1) % L[mu]
            xm = list(x)
            xm[mu] = (xm[mu] - 1) % L[mu]
            D[i, site_index(tuple(xp), L)] += 0.5 * eta
            D[i, site_index(tuple(xm), L)] -= 0.5 * eta
    return D


def run_lattice(L, label: str) -> None:
    N = L[0] * L[1] * L[2] * L[3]
    D = free_staggered_D(L)
    eps = epsilon_diagonal(L)
    E = np.diag(eps)
    eye = np.eye(N)

    # ---- G1.a: {eps, D} = 0 (eps D eps = -D) and D anti-Hermitian ----
    err_ac = float(np.max(np.abs(E @ D @ E + D)))
    check(
        f"[{label}] G1.a {{eps,D}}=0  (eps D eps = -D)",
        err_ac < 1e-12,
        f"max|eps D eps + D| = {err_ac:.2e}",
    )
    err_ah = float(np.max(np.abs(D + D.conj().T)))
    check(
        f"[{label}] G1.a D anti-Hermitian (D = -D^dag)",
        err_ah < 1e-12,
        f"max|D + D^dag| = {err_ah:.2e}",
    )

    # ---- G1.b: K = eps D Hermitian, {eps, K} = 0 ----
    K = E @ D
    err_kh = float(np.max(np.abs(K - K.conj().T)))
    check(
        f"[{label}] G1.b K = eps D is Hermitian",
        err_kh < 1e-12,
        f"max|K - K^dag| = {err_kh:.2e}",
    )
    err_ek = float(np.max(np.abs(E @ K + K @ E)))
    check(
        f"[{label}] G1.b {{eps, K}} = 0",
        err_ek < 1e-12,
        f"max|eps K + K eps| = {err_ek:.2e}",
    )

    # ---- G1.c: K^2 = -D^2 = D^dag D ; H(m)^2 = K^2 + m^2 I ----
    K2 = K @ K
    DdD = D.conj().T @ D
    err_k2 = float(np.max(np.abs(K2 - DdD)))
    check(
        f"[{label}] G1.c K^2 = D^dag D  (= -D^2 >= 0)",
        err_k2 < 1e-12,
        f"max|K^2 - D^dag D| = {err_k2:.2e}",
    )
    for m in (0.1, 0.37, 1.0):
        H = E @ (D - m * eye)  # H(m) = eps(D - m) = K - m eps
        H2 = H @ H
        err_id = float(np.max(np.abs(H2 - (K2 + (m ** 2) * eye))))
        check(
            f"[{label}] G1.c H(m)^2 = K^2 + m^2 I  (m={m})",
            err_id < 1e-10,
            f"max|H^2 - (K^2 + m^2)| = {err_id:.2e}",
        )

    # ---- G1.d: zero mode of K, then min|spec H(m)| = |m| => no crossing ----
    kmin = float(np.min(np.abs(np.linalg.eigvalsh(K))))
    check(
        f"[{label}] G1.d massless K has a zero mode (min|spec K| ~ 0)",
        kmin < 1e-8,
        f"min|spec K| = {kmin:.2e}",
    )
    for m in (0.1, 0.37, 1.0):
        H = E @ (D - m * eye)
        ev = np.linalg.eigvalsh(H)  # H Hermitian
        mn = float(np.min(np.abs(ev)))
        # Lower bound (exact, from H^2 = K^2 + m^2 >= m^2): min|spec H| >= |m|.
        check(
            f"[{label}] G1.d min|spec H(m)| >= |m|  (no zero crossing, m={m})",
            mn >= abs(m) - 1e-9,
            f"min|spec H| = {mn:.8f}, |m| = {abs(m)}",
        )
        # Saturation (since min spec(K^2) = 0): min|spec H| = |m|.
        check(
            f"[{label}] G1.d min|spec H(m)| = |m|  (saturation, m={m})",
            abs(mn - abs(m)) < 1e-6,
            f"||min|spec H| - |m|| = {abs(mn - abs(m)):.2e}",
        )

    # ---- G2: A[1,1] = Tr[eps exp(-t D^dag D)] = 0, t-independent; +/- pairing ----
    w, V = np.linalg.eigh(DdD)
    diag_eps = np.diag(V.conj().T @ E @ V).real
    A_vals = [float(np.sum(diag_eps * np.exp(-t * w))) for t in (0.1, 0.5, 1.0, 2.0)]
    spread = max(A_vals) - min(A_vals)
    check(
        f"[{label}] G2 A[1,1] t-independent across t in {{0.1,0.5,1,2}}",
        spread < 1e-8,
        f"spread = {spread:.2e}, A = {[round(a, 8) for a in A_vals]}",
    )
    check(
        f"[{label}] G2 A[1,1] = 0  (chi = 0 / +/- pairing)",
        abs(A_vals[0]) < 1e-8,
        f"A[1,1] = {A_vals[0]:.2e}",
    )
    # D spectrum symmetric under lambda -> -lambda (iD Hermitian, real spectrum).
    s = np.sort(np.linalg.eigvalsh(1j * D))
    sym_err = float(np.max(np.abs(s + s[::-1])))
    check(
        f"[{label}] G2 D spectrum is +/- symmetric (lambda -> -lambda)",
        sym_err < 1e-8,
        f"max|sorted(s) + reversed| = {sym_err:.2e}",
    )


def main() -> int:
    print("=" * 72)
    print("ABJ residual correction: GW NOT necessary; obstruction = eps-gap + chi=0")
    print("Note: ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28.md")
    print("Free (U = 1) staggered operator; Ginsparg-Wilson relation NOT used.")
    print("=" * 72)

    run_lattice([4, 2, 2, 2], "Z4xZ2^3  L_t=4,L_s=2")
    run_lattice([4, 4, 4, 4], "L=4 symmetric (robustness)")

    print("=" * 72)
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print(
            "VERDICT: GW is not necessary for a lattice index; the demonstrable "
            "internal obstruction on the free/flat staggered background is the "
            "eps-gap (H(m)^2 = K^2 + m^2 => spectral flow 0) and chi = 0 "
            "(A[1,1] = 0), so the open residual (P1') is 'exhibit a chi != 0 / "
            "Q != 0 background', not 'import overlap because no GW'."
        )
        print("=" * 72)
        return 0
    print("VERDICT: failures encountered; see above.")
    print("=" * 72)
    return 1


if __name__ == "__main__":
    sys.exit(main())
