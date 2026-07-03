#!/usr/bin/env python3
"""Audit companion runner: blocked-time-spacing normalization bridge for the
axiom-first spectrum condition (2026-06-05).

WHAT THIS RUNNER REPAIRS
------------------------
The spectrum-condition source note
(docs/AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md) imports its
load-bearing positivity input as T := T_hat^2, the TWO-STEP blocked staggered
transfer matrix, from the retained-bounded two-step positivity authority
(AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28). That
authority establishes

    T_hat^2 = exp(-2 a_tau H_hat),   H_hat = sum_p E(p) n_p >= 0,
    H_hat = -log(T_hat^2) / (2 a_tau),

i.e. the physical Hamiltonian uses the 1/(2 a_tau) normalization because the
two-step block advances the physical/Euclidean time by TWO lattice spacings.
The spectrum-condition note and its old runner instead wrote
H = -(1/a_tau) log(T_hat^2), a factor of two too large, and the old runner
side-stepped the issue by constructing its OWN single-step object
T = exp(-a_tau H_lat) rather than the cited two-step transfer matrix.

This runner supplies the missing blocked-time-spacing bridge and aligns the
exhibit with T_hat^2:

  (a) Identifies a_tau as the SINGLE lattice spacing and 2 a_tau as the
      physical two-step block spacing, by REPROVING that the staggered
      single-step transfer operator must be squared to advance one physical
      block (the canonical staggered phase eta_1(t) = (-1)^t alternates the
      single-step operator T_even / T_odd; the physical object is
      T_hat^2 = T_odd . T_even).
  (b) Shows T_hat (single step) is NOT positive while T_hat^2 IS positive
      Hermitian -> the spectrum condition H >= 0 holds for the blocked object.
  (c) REPROVES that ONLY the 1/(2 a_tau) normalization,
          H := -(1/(2 a_tau)) log(T_hat^2 / M_T),
      gives a self-adjoint H >= 0 whose single-particle dispersion equals the
      exact free staggered dispersion E(p) = arcsinh(sqrt(m^2 + sin^2 p)) and
      whose mass gap m_gap = -(1/(2 a_tau)) log(lambda_1 / M_T) matches the
      cited H_hat. The note's old 1/a_tau normalization gives exactly twice
      these values (the defect being repaired).

Everything is REPROVEN from the staggered action + finite-dimensional linear
algebra (numpy); the literature staggered dispersion is a comparator only.
The bridge bottoms out on the retained-bounded two-step positivity input, so
the supported re-audit target is the same bounded class; audit owns status.

NO forbidden inputs: no PDG / fitted / measured / lattice-MC / beta=6 / g_bare
values are consumed. The mass m and lattice spacing a_tau are free symbols /
scan parameters of the construction, not fitted constants.

Each check prints [PASS]/[FAIL]; the run ends with 'TOTAL: N PASS / 0 FAIL'.
"""
from __future__ import annotations

import math

import numpy as np

# --- construction parameters (NOT fitted; scanned to show robustness) --------
MASS_SCAN = [0.05, 0.1, 0.3, 0.5, 1.0, 2.0]
A_TAU_SCAN = [0.5, 1.0, 2.0]          # single lattice spacing values to scan
LS_SCAN = [2, 3, 4, 6]
N_BZ = 32
TOL = 1e-9
TOL_TIGHT = 1e-12


# =============================================================================
# Action-derived single-step classical transfer matrices and exact dispersion
# (reproduced from the staggered action, not imported)
# =============================================================================

def E_dispersion(p: float, m: float) -> float:
    """Exact free staggered 1+1d dispersion: sinh^2 E = m^2 + sin^2 p.

    LITERATURE COMPARATOR ONLY. The runner verifies the action-derived two-step
    eigenvalue reproduces this; it is not an input to any positivity claim.
    """
    return math.asinh(math.sqrt(m * m + math.sin(p) ** 2))


def classical_step(p: float, m: float, parity: int) -> np.ndarray:
    """Single-step classical transfer matrix T_s from the staggered action's
    banded-in-time mode equation

        alpha_t psi_t + (1/2) psi_{t+1} - (1/2) psi_{t-1} = 0,
        alpha_t = m + i eta_1(t) sin p = m + i (-1)^t sin p,

    rearranged to psi_{t+1} = -2 alpha_t psi_t + psi_{t-1} on V_t=(psi_t,psi_{t-1}):

        T_s = [[ -2 alpha_s, 1 ], [ 1, 0 ]].

    parity = 0 (even slice, eta_1=+1) or 1 (odd slice, eta_1=-1). Straight from
    the action; no convention supplied.
    """
    s = math.sin(p)
    alpha = m + (1j * s if parity == 0 else -1j * s)
    return np.array([[-2.0 * alpha, 1.0], [1.0, 0.0]], dtype=complex)


def classical_2step(p: float, m: float) -> np.ndarray:
    """Two-step (blocked) classical transfer matrix T2cl = T_odd . T_even."""
    return classical_step(p, m, 1) @ classical_step(p, m, 0)


def decaying_eig(mat: np.ndarray) -> complex:
    ev = np.linalg.eigvals(mat)
    return ev[int(np.argmin(np.abs(ev)))]


# =============================================================================
# Jordan-Wigner Fock-space operators (for the many-body T_hat^2 exhibit)
# =============================================================================

def jw_annihilation(mode: int, Ls: int) -> np.ndarray:
    I2 = np.eye(2)
    Z = np.array([[1.0, 0.0], [0.0, -1.0]])
    a = np.array([[0.0, 1.0], [0.0, 0.0]])
    ops = []
    for k in range(Ls):
        if k < mode:
            ops.append(Z)
        elif k == mode:
            ops.append(a)
        else:
            ops.append(I2)
    out = ops[0]
    for o in ops[1:]:
        out = np.kron(out, o)
    return out.astype(complex)


def build_T_hat2(Ls: int, m: float) -> np.ndarray:
    """Many-body two-step blocked transfer matrix T_hat^2 = Gamma(t1^(2)),
    t1^(2)(p) = decaying eigenvalue of the action-derived T_odd.T_even.

    T_hat^2 = tensor_p diag(1, t1^(2)(p)) on Fock space H = tensor_p {|0>,|1>}.
    Built from the ACTION-DERIVED kernel, not posited.
    """
    ps = [2.0 * math.pi * k / Ls for k in range(Ls)]
    kernels = [decaying_eig(classical_2step(p, m)).real for p in ps]
    T2 = np.array([[1.0]], dtype=complex)
    for val in kernels:
        T2 = np.kron(T2, np.diag([1.0, val]))
    return T2


def build_H_hat_lattice(Ls: int, m: float) -> np.ndarray:
    """Second-quantized H_hat = sum_p E(p) n_p from Jordan-Wigner number ops,
    using the exact dispersion E(p). This is the operator whose blocked
    evolution is T_hat^2 = exp(-2 a_tau H_hat); we use it to cross-check that
    the reconstructed H equals H_hat under the 1/(2 a_tau) normalization."""
    ps = [2.0 * math.pi * k / Ls for k in range(Ls)]
    Es = [E_dispersion(p, m) for p in ps]
    dim = 2 ** Ls
    A = [jw_annihilation(k, Ls) for k in range(Ls)]
    H = np.zeros((dim, dim), dtype=complex)
    for k in range(Ls):
        H += Es[k] * (A[k].conj().T @ A[k])
    return H


# =============================================================================
# Reconstructed Hamiltonian under a chosen normalization 1/(c * a_tau)
# =============================================================================

def reconstruct_H(T2: np.ndarray, a_tau: float, c: float) -> tuple[np.ndarray, float]:
    """H = -(1/(c a_tau)) log(T2 / M_T), via the diagonal spectrum of T2.

    Returns (H, M_T). c = 2 is the CORRECT blocked-time normalization;
    c = 1 is the note's old (defective) normalization.

    The action-derived block kernel diag entry is t1^(2)(p) = e^{-2 E(p)} in
    lattice units (a_tau = 1 per single step). To exhibit the a_tau dependence
    we identify e^{-2 E(p)} = e^{-2 a_tau E_phys(p)} with E_phys(p) = E(p)/a_tau,
    so reconstruct_H(.,a_tau,c=2) returns E_phys = E(p)/a_tau on the occupied
    modes, matching H_hat/a_tau. We therefore compare H(c=2) to H_hat/a_tau.
    """
    diag = np.real(np.diag(T2))
    M_T = float(diag.max())
    H_diag = -(1.0 / (c * a_tau)) * np.log(diag / M_T)
    return np.diag(H_diag).astype(complex), M_T


# =============================================================================
# Checks
# =============================================================================

def main() -> int:
    passes: list[str] = []
    fails: list[str] = []

    def check(label: str, ok: bool, detail: str = "") -> None:
        tag = "[PASS]" if ok else "[FAIL]"
        (passes if ok else fails).append(label)
        print(f"  {tag} {label}" + (f"  ::  {detail}" if detail else ""))

    print("=" * 78)
    print("BLOCKED-TIME-SPACING NORMALIZATION BRIDGE for the SPECTRUM CONDITION")
    print("Repairs H = -(1/a_tau) log T_hat^2  ->  H = -(1/(2 a_tau)) log T_hat^2")
    print("Aligns the exhibit with the imported two-step object T := T_hat^2.")
    print("=" * 78)

    # ------------------------------------------------------------------
    # B1. Two lattice steps per block: single-step alternates, must be squared.
    # ------------------------------------------------------------------
    print("\n--- B1: a_tau is ONE lattice step; T_hat^2 advances TWO (one block) ---")
    print("    Canonical staggered phase eta_1(t)=(-1)^t alternates the single-step")
    print("    operator T_even/T_odd; the physical (period-2) object is T_odd.T_even.")
    b1_ok = True
    detail_b1 = []
    for m in MASS_SCAN:
        # T_even != T_odd whenever sin(p) != 0  =>  single-step is NOT
        # time-translation invariant by one step; period is two steps.
        worst_diff = 0.0
        for k in range(1, N_BZ):
            p = 2.0 * math.pi * k / N_BZ
            if abs(math.sin(p)) < 1e-12:
                continue
            d = float(np.max(np.abs(classical_step(p, m, 0) - classical_step(p, m, 1))))
            worst_diff = max(worst_diff, d)
        b1_ok = b1_ok and (worst_diff > 1e-3)
        detail_b1.append(f"m={m}: max|T_even-T_odd|={worst_diff:.3f}")
    check(
        "single-step transfer alternates (T_even != T_odd) => block spacing = 2 a_tau",
        b1_ok,
        "; ".join(detail_b1[:3]) + " ...",
    )

    # ------------------------------------------------------------------
    # B2. Faithfulness: decaying eigenvalue of T_hat^2 == e^{-2 E(p)}.
    #     The factor 2 in the exponent IS the two-step block spacing.
    # ------------------------------------------------------------------
    print("\n--- B2: action-derived T_hat^2 decaying eigenvalue == e^{-2 E(p)} ---")
    print("    (the exponent carries the factor 2 = two lattice steps per block)")
    b2_ok = True
    detail_b2 = []
    for m in MASS_SCAN:
        max_res = 0.0
        max_im = 0.0
        for k in range(N_BZ):
            p = 2.0 * math.pi * k / N_BZ
            lam = decaying_eig(classical_2step(p, m))
            target = math.exp(-2.0 * E_dispersion(p, m))
            max_res = max(max_res, abs(lam - target))
            max_im = max(max_im, abs(lam.imag))
        b2_ok = b2_ok and (max_res < TOL) and (max_im < TOL)
        detail_b2.append(f"m={m}: max|lam - e^-2E|={max_res:.1e}")
    check(
        "T_hat^2 decaying eigenvalue == e^{-2 E(p)} over the BZ (factor-2 exponent)",
        b2_ok,
        "; ".join(detail_b2[:3]) + " ...",
    )

    # ------------------------------------------------------------------
    # B3. Single-step T_hat is NOT positive (spectrum condition needs the block).
    # ------------------------------------------------------------------
    print("\n--- B3: single-step T_hat is NON-positive (so the block is required) ---")
    b3_ok = True
    detail_b3 = []
    for m in MASS_SCAN:
        min_im = float("inf")
        exceptional_neg = True
        for k in range(N_BZ):
            p = 2.0 * math.pi * k / N_BZ
            s = math.sin(p)
            for par in (0, 1):
                ev = np.linalg.eigvals(classical_step(p, m, par))
                if abs(s) > 1e-12:
                    min_im = min(min_im, float(np.max(np.abs(ev.imag))))
                else:
                    ev_real = sorted(float(x.real) for x in ev)
                    exceptional_neg = exceptional_neg and (ev_real[0] < -1e-10)
        if min_im == float("inf"):
            min_im = 0.0
        b3_ok = b3_ok and (min_im > 1e-3) and exceptional_neg
        detail_b3.append(f"m={m}: min|Im eig|={min_im:.3f}, sin(p)=0 neg mode={exceptional_neg}")
    check(
        "single-step T_even/T_odd non-positive (complex off sin(p)=0; negative at sin(p)=0)",
        b3_ok,
        "; ".join(detail_b3[:3]) + " ...",
    )

    # ------------------------------------------------------------------
    # B4. T_hat^2 IS positive Hermitian  =>  spectrum condition H >= 0.
    #     (built from the action-derived two-step kernel; aligned with T_hat^2)
    # ------------------------------------------------------------------
    print("\n--- B4: T_hat^2 positive Hermitian (=> spectrum condition H>=0 holds) ---")
    b4_ok = True
    detail_b4 = []
    for Ls in LS_SCAN:
        for m in (0.3, 0.5):
            T2 = build_T_hat2(Ls, m)
            herm = float(np.max(np.abs(T2 - T2.conj().T)))
            eig = np.linalg.eigvalsh(0.5 * (T2 + T2.conj().T))
            ok = (eig.min() > 0.0) and (herm < TOL_TIGHT) and (eig.max() <= 1.0 + 1e-12)
            b4_ok = b4_ok and ok
            if Ls in (3, 4) and m == 0.5:
                detail_b4.append(f"Ls={Ls}: min eig={eig.min():.2e}, max={eig.max():.4f}")
    check(
        "T_hat^2 positive Hermitian with spec in (0, M_T], M_T=1 (vacuum)",
        b4_ok,
        "; ".join(detail_b4),
    )

    # ------------------------------------------------------------------
    # B5. CORE BRIDGE: ONLY 1/(2 a_tau) reconstructs the physical H = H_hat.
    #     Show H(c=2) = H_hat/a_tau (matches cited authority) and H(c=2) >= 0;
    #     show H(c=1) = 2 H_hat/a_tau (the note's old, defective value).
    # ------------------------------------------------------------------
    print("\n--- B5: H = -(1/(2 a_tau)) log(T_hat^2/M_T) == H_hat (CORE BRIDGE) ---")
    print("    c=2 (correct): single-particle dispersion = E(p) and H matches H_hat.")
    print("    c=1 (old note): gives exactly 2 H_hat (the factor-of-2 defect).")
    b5_ok = True
    detail_b5 = []
    for Ls in LS_SCAN:
        for m in (0.3, 0.5):
            for a_tau in A_TAU_SCAN:
                T2 = build_T_hat2(Ls, m)
                H_hat = build_H_hat_lattice(Ls, m)
                # H_hat is diagonal in occupation basis; the physical H_hat carries
                # the per-step lattice units. The reconstructed H(c=2) returns
                # E(p)/a_tau on occupied modes, so compare to H_hat/a_tau.
                H_hat_diag = np.real(np.diag(H_hat)) / a_tau

                H_c2, M_T = reconstruct_H(T2, a_tau, c=2.0)
                H_c1, _ = reconstruct_H(T2, a_tau, c=1.0)
                H_c2_diag = np.real(np.diag(H_c2))
                H_c1_diag = np.real(np.diag(H_c1))

                err_c2 = float(np.max(np.abs(H_c2_diag - H_hat_diag)))      # -> 0
                err_c1 = float(np.max(np.abs(H_c1_diag - 2.0 * H_hat_diag)))  # -> 0
                nonneg_c2 = H_c2_diag.min() > -1e-10
                # the two normalizations differ by exactly factor 2 (away from vacuum)
                nz = np.abs(H_c2_diag) > 1e-12
                ratio_ok = True
                if np.any(nz):
                    ratios = H_c1_diag[nz] / H_c2_diag[nz]
                    ratio_ok = bool(np.all(np.abs(ratios - 2.0) < 1e-9))

                ok = (err_c2 < TOL) and (err_c1 < TOL) and nonneg_c2 and ratio_ok
                b5_ok = b5_ok and ok
                if Ls == 4 and m == 0.5 and a_tau == 1.0:
                    detail_b5.append(
                        f"Ls={Ls},m={m},a_tau={a_tau}: ||H(c=2)-H_hat||={err_c2:.1e}, "
                        f"||H(c=1)-2H_hat||={err_c1:.1e}, H(c=2)>=0:{nonneg_c2}, ratio==2:{ratio_ok}"
                    )
    check(
        "H(c=2)=H_hat (>=0); H(c=1)=2 H_hat; the two normalizations differ by exactly 2",
        b5_ok,
        "; ".join(detail_b5),
    )

    # ------------------------------------------------------------------
    # B6. Single-particle dispersion under c=2 equals E(p); under c=1 equals 2E(p).
    # ------------------------------------------------------------------
    print("\n--- B6: single-particle energy -(1/(2 a_tau)) log(lambda_dec) == E(p)/a_tau ---")
    b6_ok = True
    detail_b6 = []
    for m in MASS_SCAN:
        for a_tau in A_TAU_SCAN:
            max_err_c2 = 0.0
            max_err_c1 = 0.0
            for k in range(N_BZ):
                p = 2.0 * math.pi * k / N_BZ
                lam = decaying_eig(classical_2step(p, m)).real
                # block kernel lam = e^{-2 E(p)} (lattice units). Physical
                # single-particle energy under c=2 is -log(lam)/(2 a_tau)=E(p)/a_tau.
                E_c2 = -math.log(lam) / (2.0 * a_tau)
                E_c1 = -math.log(lam) / (1.0 * a_tau)
                E_ref = E_dispersion(p, m) / a_tau
                max_err_c2 = max(max_err_c2, abs(E_c2 - E_ref))
                max_err_c1 = max(max_err_c1, abs(E_c1 - 2.0 * E_ref))
            ok = (max_err_c2 < TOL) and (max_err_c1 < TOL)
            b6_ok = b6_ok and ok
            if m == 0.5 and a_tau == 1.0:
                detail_b6.append(
                    f"m={m},a_tau={a_tau}: max|E(c=2)-E_ref|={max_err_c2:.1e}, "
                    f"max|E(c=1)-2E_ref|={max_err_c1:.1e}"
                )
    check(
        "1/(2 a_tau): single-particle energy == E(p)/a_tau; 1/a_tau gives twice that",
        b6_ok,
        "; ".join(detail_b6),
    )

    # ------------------------------------------------------------------
    # B7. Mass gap under the corrected normalization (SC3) and forward cone.
    #     m_gap = -(1/(2 a_tau)) log(lambda_1 / M_T) > 0 on the finite carrier;
    #     all energies non-negative (spectrum in the forward cone E >= 0).
    # ------------------------------------------------------------------
    print("\n--- B7: corrected gap m_gap=-(1/(2 a_tau)) log(lambda_1/M_T); forward cone ---")
    b7_ok = True
    detail_b7 = []
    for Ls in LS_SCAN:
        for a_tau in A_TAU_SCAN:
            m = 0.5
            T2 = build_T_hat2(Ls, m)
            diag = np.sort(np.real(np.diag(T2)))[::-1]  # descending eigenvalues
            M_T = diag[0]
            lam1 = diag[1]
            gap_c2 = -(1.0 / (2.0 * a_tau)) * math.log(lam1 / M_T)
            gap_c1 = -(1.0 / (1.0 * a_tau)) * math.log(lam1 / M_T)
            H_c2, _ = reconstruct_H(T2, a_tau, c=2.0)
            E = np.sort(np.real(np.diag(H_c2)))
            forward_cone = E.min() > -1e-10               # all E_n >= 0
            ground_zero = abs(E[0]) < 1e-12               # E_0 = 0 (vacuum)
            gap_pos = gap_c2 > 1e-9
            gap_half = abs(gap_c1 - 2.0 * gap_c2) < 1e-9  # old gap = 2 * corrected
            gap_matches_spectrum = abs((E[1] - E[0]) - gap_c2) < 1e-9
            ok = forward_cone and ground_zero and gap_pos and gap_half and gap_matches_spectrum
            b7_ok = b7_ok and ok
            if Ls == 4 and a_tau == 1.0:
                detail_b7.append(
                    f"Ls={Ls},a_tau={a_tau}: E_0={E[0]:.1e}, m_gap(c=2)={gap_c2:.4f}, "
                    f"m_gap(c=1)={gap_c1:.4f}, cone(E>=0)={forward_cone}"
                )
    check(
        "corrected m_gap>0, E_0=0, spectrum in forward cone (E_n>=0); old gap=2*corrected",
        b7_ok,
        "; ".join(detail_b7),
    )

    # ------------------------------------------------------------------
    # B8. Operator-picture self-adjointness of the reconstructed H (SC1).
    #     Build H on the full Fock space from the functional calculus of the
    #     (Hermitian PSD) T_hat^2 and confirm H self-adjoint, spec >= 0, c=2.
    # ------------------------------------------------------------------
    print("\n--- B8: reconstructed H self-adjoint & H>=0 on full Fock space (SC1+SC2) ---")
    b8_ok = True
    detail_b8 = []
    for Ls in (2, 3, 4):
        for a_tau in (1.0, 2.0):
            m = 0.5
            T2 = build_T_hat2(Ls, m)
            T2h = 0.5 * (T2 + T2.conj().T)
            w, V = np.linalg.eigh(T2h)
            M_T = float(w.max())
            logTn = (V * np.log(w / M_T)) @ V.conj().T
            H = -(1.0 / (2.0 * a_tau)) * logTn
            herm_err = float(np.max(np.abs(H - H.conj().T)))
            evH = np.linalg.eigvalsh(0.5 * (H + H.conj().T))
            ok = (herm_err < TOL) and (evH.min() > -1e-10)
            b8_ok = b8_ok and ok
            if Ls == 4 and a_tau == 1.0:
                detail_b8.append(
                    f"Ls={Ls},a_tau={a_tau}: ||H-H^dag||={herm_err:.1e}, "
                    f"min spec(H)={evH.min():.1e}, max={evH.max():.4f}"
                )
    check(
        "H=-(1/(2 a_tau)) logm(T_hat^2/M_T) self-adjoint, spec(H) >= 0",
        b8_ok,
        "; ".join(detail_b8),
    )

    # ------------------------------------------------------------------
    # B9. Forbidden-input guard: positivity uses the action only.
    #     Build T_hat^2 from classical_2step (action) alone and confirm
    #     positivity without invoking the E(p) dispersion comparator.
    # ------------------------------------------------------------------
    print("\n--- B9: no forbidden inputs (m, a_tau are free; E(p) is comparator only) ---")
    indep_ok = True
    for Ls in (3, 4):
        for m in (0.2, 0.7):
            T2 = build_T_hat2(Ls, m)  # uses ONLY classical_2step (action), no E()
            eig = np.linalg.eigvalsh(0.5 * (T2 + T2.conj().T))
            indep_ok = indep_ok and (eig.min() > 0.0)
    check(
        "positivity built from action only (independent of the E(p) comparator)",
        indep_ok,
        "T_hat^2 positive Hermitian without invoking the dispersion formula",
    )

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    n_pass = len(passes)
    n_fail = len(fails)
    labels = [
        ("B1 two lattice steps per block",
         "single-step transfer alternates (T_even != T_odd) => block spacing = 2 a_tau"),
        ("B2 faithfulness (e^-2E factor-2 exponent)",
         "T_hat^2 decaying eigenvalue == e^{-2 E(p)} over the BZ (factor-2 exponent)"),
        ("B3 single-step non-positive",
         "single-step T_even/T_odd non-positive (complex off sin(p)=0; negative at sin(p)=0)"),
        ("B4 T_hat^2 positive Hermitian",
         "T_hat^2 positive Hermitian with spec in (0, M_T], M_T=1 (vacuum)"),
        ("B5 CORE BRIDGE H(c=2)=H_hat",
         "H(c=2)=H_hat (>=0); H(c=1)=2 H_hat; the two normalizations differ by exactly 2"),
        ("B6 single-particle dispersion",
         "1/(2 a_tau): single-particle energy == E(p)/a_tau; 1/a_tau gives twice that"),
        ("B7 corrected gap + forward cone",
         "corrected m_gap>0, E_0=0, spectrum in forward cone (E_n>=0); old gap=2*corrected"),
        ("B8 self-adjoint H>=0 (Fock space)",
         "H=-(1/(2 a_tau)) logm(T_hat^2/M_T) self-adjoint, spec(H) >= 0"),
        ("B9 no forbidden inputs",
         "positivity built from action only (independent of the E(p) comparator)"),
    ]
    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    for short, key in labels:
        print(f"  {short:<44} {'PASS' if key in passes else 'FAIL'}")
    print()
    if n_fail:
        print("Failures:")
        for f in fails:
            print(f"  - {f}")
    print(f"TOTAL: {n_pass} PASS / {n_fail} FAIL")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
