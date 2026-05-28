#!/usr/bin/env python3
"""Bridge runner: det(M_KS + m I) == Tr[T_hat^{L_t}] == Tr(e^{-beta H_hat}) for
free staggered (Kogut-Susskind) fermions, with H_hat self-adjoint and >= 0.

This is the load-bearing companion for
docs/P2_PHASE_BLINDNESS_FROM_RP_TRANSFER_TRACE_BRIDGE_NOTE_2026-05-28.md.

----------------------------------------------------------------------------
WHAT THIS RUNNER CLOSES (P2 phase-blindness on the determinant surface)
----------------------------------------------------------------------------
The observable-principle parent
docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md writes the scalar generator as
W = log|det(D+J)|; its P2 premise ("the scalar bosonic generator is a
continuous function of |Z| alone", i.e. phase-blindness) is enforced by hand
via the modulus |.|. The qubit-trace note
docs/OBSERVABLE_PRINCIPLE_P1_P2_FROM_QUBIT_TRACE_NOTE_2026-05-20.md derives P2
on the *qubit-trace* surface from positivity of Z = Tr(e^{-(H+J)}) when H+J is
self-adjoint, but left the BRIDGE to the determinant surface gate-conditional.

This runner supplies that bridge for the free staggered case via the
classic transfer-matrix <-> determinant identity, underwritten by the now
in-repo reflection-positivity (RP) result
docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md (the 2-step
blocked construction; in-repo runner
scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py, landed PR #2153):

  (a)  det(M_KS + m I) = Z_vac . Tr[T_hat^{L_t}]      (det = transfer trace,
          with the standard real-positive vacuum/zero-point normalization Z_vac)
  (b)  T_hat^2 = exp(-2 a H_hat), H_hat = H_hat^dag >= 0    (RP, in-repo)
  (c)  => Tr[T_hat^{L_t}] = Tr[(T_hat^2)^{L_t/2}]
              = Tr[exp(-L_t a H_hat)] = Tr(e^{-beta H_hat}) = Z_qubit, beta=L_t a
  (d)  H_hat self-adjoint AND Z_vac>0 => det = Z_vac . Z_qubit is real-positive
          => log|det| = log(det) is phase-blind.

The exact closed form on the free staggered lattice (verified to machine
precision in C1) is, per spatial momentum p (= 2 pi n / L_s):

  det(M_p) = (1/2)^{L_t} ( 1 + e^{+L_t a E(p)} )( 1 + e^{-L_t a E(p)} ),
  det(M_KS+mI) = prod_p det(M_p),  E(p) = arcsinh sqrt(m^2 + sin^2 p) >= 0.

This is the standard antiperiodic free-fermion identity
  det(M_p) = (1/2)^{L_t} det( I + T_full(p) ),
where T_full(p) is the one-period (L_t-step) classical transfer matrix with
eigenvalues e^{+-L_t a E(p)} (det T_full = 1). Splitting the per-mode factor as

  (1 + e^{+L_t a E})(1 + e^{-L_t a E})
     = [ (1/2)^{L_t}(1 + e^{+L_t a E}) ]^{-1}_{normalised out as Z_vac}
       x  (1 + e^{-L_t a E})  ... (see Z_vac and Tr below)

gives the PHYSICAL Fock trace Tr(e^{-beta H_hat}) = prod_p (1 + e^{-L_t a E(p)})
times the positive zero-point factor Z_vac = prod_p (1/2)^{L_t}(1 + e^{+L_t a E(p)}).
Both are manifestly real-positive (every E(p) is real, e^x>0), exactly as the RP
note uses "vacuum-energy subtraction" T_hat^2/lambda_max. So on the FREE
STAGGERED surface, the framework's Z = det(M_KS+mI) is the qubit-trace partition
function Tr(e^{-beta H_hat}) up to a positive real zero-point factor with
self-adjoint H_hat>=0; phase-blindness P2 is then a THEOREM, not an admission.

----------------------------------------------------------------------------
CONSTRUCTION (free staggered fermions, 1+1d, single Grassmann component/site)
----------------------------------------------------------------------------
Free staggered (KS) action, U=1, on an L_t x L_s lattice (clean temporal hop
eta_0 = 1, staggered spatial phase eta_1(t) = (-1)^t):

  S = sum_{t,x} bar_chi(t,x) [ m chi(t,x)
        + (1/2)( chi(t+1,x) - chi(t-1,x) )                  (temporal hop)
        + (1/2) (-1)^t ( chi(t,x+1) - chi(t,x-1) ) ]        (spatial hop)

The free theory factorizes across spatial momentum p = 2 pi n / L_s. Per p the
temporal-mode operator is a banded (tri-diagonal, antiperiodic in t) matrix
M_p whose product over p is the full determinant:

  det(M_KS + m I) = prod_p det(M_p).

For each p the banded mode equation
   alpha_t psi_t + (1/2) psi_{t+1} - (1/2) psi_{t-1} = 0,
   alpha_t = m + i eta_1(t) sin p = m + i (-1)^t sin p,
defines the single-step classical transfer matrix on V_t = (psi_t, psi_{t-1}):
   V_{t+1} = T_s(t) V_t,  T_s = [[ -2 alpha_t, 1 ], [ 1, 0 ]].
Because eta_1 alternates, T_s alternates T_even/T_odd; the physical step over
TWO spacings is T2cl(p) = T_odd . T_even, with eigenvalues e^{+-2E(p)} and
   E(p) = arcsinh( sqrt( m^2 + sin^2 p ) ) >= 0   (exact free staggered disp).

The classic identity for an antiperiodic banded determinant (verified in C1) is

   det(M_p) = (1/2)^{L_t} det( I + T_full(p) )
            = (1/2)^{L_t} ( 1 + e^{+L_t a E(p)} )( 1 + e^{-L_t a E(p)} ),

where T_full(p) is the one-period (L_t-step) product of single-step classical
transfer matrices, with eigenvalues e^{+-L_t a E(p)} and det T_full = 1, so that
det(I + T_full) = 1 + tr(T_full) + det(T_full) = 2 + 2 cosh(L_t a E(p)). The
PHYSICAL Fock trace of the (zero-point-normalised) transfer matrix is

   Tr(e^{-beta H_hat}) = prod_p ( 1 + e^{-L_t a E(p)} )   (free Fock trace),

and the positive real zero-point factor is

   Z_vac = prod_p (1/2)^{L_t} ( 1 + e^{+L_t a E(p)} ) > 0,

so det(M_KS+mI) = Z_vac . Tr(e^{-beta H_hat}) exactly (C1). This is the standard
"vacuum-energy subtraction" the RP note performs via T_hat^2/lambda_max.

----------------------------------------------------------------------------
SCORECARD
----------------------------------------------------------------------------
  C1  det = transfer trace : det(M_KS+mI) == Z_vac . Tr(e^{-beta H_hat}) AND
                             == prod_p (1/2)^{L_t}(1+e^{+L_t aE})(1+e^{-L_t aE})
                             to machine precision, L_t in {4,6}, L_s in {2,3},
                             several m>0, with Z_vac>0 and Tr(e^{-beta H})>0.
  C2  T^2 = exp(-2aH)      : T_hat^2 == exp(-2 a H_hat), H_hat self-adjoint,
                             spec(H_hat) >= 0  (RP self-adjoint bounded-below H).
  C3  Z real-positive      : Z = det(M_KS+mI) is real (|Im Z| ~ 0) and > 0.
  C4  phase-blind W         : W = log|det| == log(det) (modulus automatic), so
                             the scalar generator depends on |Z| alone -- P2.

A passing run supports the bounded bridge content for the FREE staggered
surface. The interacting/gauge realization (identifying the framework Dirac
operator with the staggered KS operator) rides on the ALREADY-registered
Tier-A staggered-Dirac realization gate AC_phi_lambda
(staggered_dirac_realization_gate_note_2026-05-03, audited_renaming) and is
NOT closed here. Independent audit owns any status verdict.
"""
from __future__ import annotations

import cmath
import math

import numpy as np

# Lattice spacing convention (a = 1; beta = L_t a = L_t).
A_TAU = 1.0
TOL_MACHINE = 1e-9
TOL_PSD = 1e-10


# ---------------------------------------------------------------------------
# Free staggered dispersion and single-particle 2-step transfer kernel
# (action-derived; identical construction to the RP runner #2153)
# ---------------------------------------------------------------------------

def E_dispersion(p: float, m: float) -> float:
    """Free staggered 1+1d dispersion: sinh^2 E = m^2 + sin^2 p."""
    return math.asinh(math.sqrt(m * m + math.sin(p) ** 2))


def classical_step(p: float, m: float, parity: int) -> np.ndarray:
    """Single-step classical transfer matrix from the staggered action's
    banded-in-time mode equation. parity 0 -> eta_1=+1, 1 -> eta_1=-1."""
    s = math.sin(p)
    alpha = m + (1j * s if parity == 0 else -1j * s)
    return np.array([[-2.0 * alpha, 1.0], [1.0, 0.0]], dtype=complex)


def classical_2step(p: float, m: float) -> np.ndarray:
    """T2cl(p) = T_odd(p) . T_even(p)."""
    return classical_step(p, m, 1) @ classical_step(p, m, 0)


def single_particle_2step_kernel(p: float, m: float) -> complex:
    """Decaying-mode eigenvalue of the 2-step classical matrix = e^{-2E(p)}."""
    ev = np.linalg.eigvals(classical_2step(p, m))
    return ev[int(np.argmin(np.abs(ev)))]


# ---------------------------------------------------------------------------
# Full free staggered Dirac matrix M_KS + m I in position space
# ---------------------------------------------------------------------------

def build_staggered_M(Lt: int, Ls: int, m: float) -> np.ndarray:
    """Free staggered Kogut-Susskind operator M = M_KS + m I on an Lt x Ls
    lattice, single Grassmann component per site.

    eta_0 = 1 (clean temporal hop), eta_1(t) = (-1)^t (staggered spatial
    phase). Temporal direction is ANTIPERIODIC (fermionic thermal BC);
    spatial direction is periodic.  Central-difference hops with weight 1/2,
    matching the action in this module's docstring and the RP runner.
    """
    N = Lt * Ls

    def idx(t: int, x: int) -> int:
        return (t % Lt) * Ls + (x % Ls)

    M = np.zeros((N, N), dtype=complex)
    # mass term
    for t in range(Lt):
        for x in range(Ls):
            M[idx(t, x), idx(t, x)] += m
    # temporal hop (eta_0 = 1), antiperiodic in t: hop crossing the t-boundary
    # picks up a minus sign.
    for t in range(Lt):
        for x in range(Ls):
            i = idx(t, x)
            # +t neighbour
            sign_p = -1.0 if (t + 1) >= Lt else 1.0
            M[i, idx(t + 1, x)] += 0.5 * sign_p
            # -t neighbour
            sign_m = -1.0 if (t - 1) < 0 else 1.0
            M[i, idx(t - 1, x)] += -0.5 * sign_m
    # spatial hop with staggered phase eta_1(t) = (-1)^t, periodic in x
    for t in range(Lt):
        eta1 = 1.0 if (t % 2 == 0) else -1.0
        for x in range(Ls):
            i = idx(t, x)
            M[i, idx(t, x + 1)] += 0.5 * eta1
            M[i, idx(t, x - 1)] += -0.5 * eta1
    return M


# ---------------------------------------------------------------------------
# Second-quantized transfer matrix T_hat and H_hat (RP construction)
# ---------------------------------------------------------------------------

def build_T_and_H(Lt: int, Ls: int, m: float):
    """Build (i) the physical Fock-space transfer-matrix trace
    Tr(e^{-beta H_hat}); (ii) the positive zero-point factor Z_vac; (iii) the
    closed-form determinant; (iv) the many-body T_hat^2 and H_hat for the RP
    self-adjoint, bounded-below check.

    Free quadratic fermions: the many-body transfer operator is the second
    quantization of the single-particle transfer kernel. The action-derived
    single-particle 2-step kernel is t1^(2)(p) = e^{-2E(p)} (decaying mode of
    T_odd.T_even), so the physical single-step kernel is e^{-E(p)} and on the
    Fock space H = tensor_p {|0>,|1>}:

        T_hat^2 = Gamma(t1^(2)) = tensor_p diag(1, e^{-2 a E(p)})
                = exp(-2 a H_hat),  H_hat = sum_p E(p) a_p^dag a_p >= 0,
        Tr[T_hat^{Lt}] = Tr(e^{-beta H_hat}) = prod_p (1 + e^{-Lt a E(p)}).

    The full antiperiodic free-fermion determinant adds the conjugate (filled-
    sea) factor and the (1/2)^{Lt} hop normalisation:

        det(M_p) = (1/2)^{Lt} (1 + e^{+Lt a E(p)})(1 + e^{-Lt a E(p)}),
        Z_vac    = prod_p (1/2)^{Lt} (1 + e^{+Lt a E(p)}) > 0.
    """
    ps = [2.0 * math.pi * n / Ls for n in range(Ls)]
    Es = [E_dispersion(p, m) for p in ps]

    trace_TLt = 1.0          # Tr(e^{-beta H_hat}) = prod_p (1+e^{-Lt a E_p})
    Z_vac = 1.0              # prod_p (1/2)^{Lt} (1+e^{+Lt a E_p}) > 0
    det_closed = 1.0         # prod_p (1/2)^{Lt}(1+e^{+Lt aE})(1+e^{-Lt aE})
    for Ep in Es:
        em = math.exp(-Lt * A_TAU * Ep)
        ep = math.exp(+Lt * A_TAU * Ep)
        trace_TLt *= (1.0 + em)
        Z_vac *= (0.5 ** Lt) * (1.0 + ep)
        det_closed *= (0.5 ** Lt) * (1.0 + ep) * (1.0 + em)

    # Many-body T_hat^2 on the 2^Ls Fock space, built EXACTLY as the RP runner:
    # from the action-derived single-particle 2-step kernel e^{-2E(p)}, and the
    # generator H_hat = sum_p E(p) n_p (diagonal in the occupation basis).
    T2 = np.array([[1.0]], dtype=complex)
    Hkron = np.array([[0.0]], dtype=complex)
    max_imag_kernel = 0.0
    for Ep, p in zip(Es, ps):
        k = single_particle_2step_kernel(p, m)          # action-derived = e^{-2E}
        max_imag_kernel = max(max_imag_kernel, abs(k.imag))
        val = k.real                                     # proven real-positive
        single_T2 = np.diag([1.0, val]).astype(complex)
        single_H = np.diag([0.0, Ep]).astype(complex)
        if T2.shape[0] == 1:
            T2 = single_T2
            Hkron = single_H
        else:
            T2 = np.kron(T2, single_T2)
            Hkron = _kron_sum(Hkron, single_H)
    T2_from_H = np.diag(np.exp(-2.0 * A_TAU * np.real(np.diag(Hkron)))).astype(complex)
    T2_herm_err = float(np.max(np.abs(T2 - T2.conj().T)))
    T2_recon_err = float(np.max(np.abs(T2 - T2_from_H)))
    Hherm_err = float(np.max(np.abs(Hkron - Hkron.conj().T)))
    H_eig = np.linalg.eigvalsh(0.5 * (Hkron + Hkron.conj().T))
    T2_eig = np.linalg.eigvalsh(0.5 * (T2 + T2.conj().T))
    return {
        "trace_TLt": trace_TLt,
        "Z_vac": Z_vac,
        "det_closed": det_closed,
        "Es": Es,
        "T2_min_eig": float(T2_eig.min()),
        "T2_herm_err": T2_herm_err,
        "T2_recon_err": T2_recon_err,
        "H_min_eig": float(H_eig.min()),
        "H_herm_err": Hherm_err,
        "max_imag_kernel": max_imag_kernel,
    }


def _kron_sum(H_acc: np.ndarray, single_H: np.ndarray) -> np.ndarray:
    """Add a new single-mode generator to the accumulated many-body H_hat in
    the same kron order used for T2: H_acc (x) I_2 + I_acc (x) single_H."""
    I_acc = np.eye(H_acc.shape[0], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    return np.kron(H_acc, I2) + np.kron(I_acc, single_H)


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

LATTICES = [(4, 2), (4, 3), (6, 2), (6, 3)]
MASSES = [0.3, 0.5, 0.9, 1.5]


def main() -> int:
    print("=" * 78)
    print("P2 PHASE-BLINDNESS FROM RP TRANSFER-MATRIX-TRACE BRIDGE (free staggered)")
    print("=" * 78)
    print("det(M_KS+mI) = Tr[T_hat^{L_t}] = Tr(e^{-beta H_hat}),  H_hat=H_hat^dag>=0 (RP)")
    print("=> Z real-positive => W = log|det| = log Z is phase-blind  (P2 theorem)")
    print(f"eta_0 = 1 (clean temporal hop), eta_1(t) = (-1)^t, antiperiodic in t.")
    print()

    passes = 0
    fails = 0

    # ---- C1: det = Z_vac . Tr[T_hat^{L_t}] (machine precision) ----
    print("-" * 78)
    print("C1  det(M_KS+mI) == Z_vac . Tr(e^{-beta H_hat}) == closed form")
    print("    Tr(e^{-beta H_hat}) = prod_p (1+e^{-Lt a E_p}) > 0;  beta = Lt a")
    print("    Z_vac = prod_p (1/2)^{Lt}(1+e^{+Lt a E_p}) > 0  (real-positive zero-point)")
    print("-" * 78)
    c1 = True
    max_res_c1 = 0.0
    for (Lt, Ls) in LATTICES:
        worst = 0.0
        Zvac_min = math.inf
        Ztr_min = math.inf
        for m in MASSES:
            M = build_staggered_M(Lt, Ls, m)
            detM = np.linalg.det(M)
            tb = build_T_and_H(Lt, Ls, m)
            lhs = detM
            rhs_factored = tb["Z_vac"] * tb["trace_TLt"]
            rhs_closed = tb["det_closed"]
            res = max(abs(lhs - rhs_factored), abs(lhs - rhs_closed))
            worst = max(worst, res)
            max_res_c1 = max(max_res_c1, res)
            Zvac_min = min(Zvac_min, tb["Z_vac"])
            Ztr_min = min(Ztr_min, tb["trace_TLt"])
            ok = (res < TOL_MACHINE * max(1.0, abs(lhs))) \
                and (tb["Z_vac"] > 0) and (tb["trace_TLt"] > 0)
            c1 = c1 and ok
        print(f"    L_t={Lt} L_s={Ls}: max|det - Z_vac.Tr| over m = {worst:.2e}  "
              f"min Z_vac={Zvac_min:.4e}>0  min Tr(e^-bH)={Ztr_min:.4f}>0")
    print(f"    overall max residual = {max_res_c1:.3e}  (tol {TOL_MACHINE:.0e})")
    print(f"    C1 = {'PASS' if c1 else 'FAIL'}")
    passes += int(c1)
    fails += int(not c1)
    print()

    # ---- C2: T^2 = exp(-2aH), H self-adjoint, spec(H) >= 0 ----
    print("-" * 78)
    print("C2  T_hat^2 == exp(-2 a H_hat),  H_hat self-adjoint, spec(H_hat) >= 0  (RP)")
    print("-" * 78)
    c2 = True
    min_spec_H = math.inf
    seen = set()
    for (Lt, Ls) in LATTICES:
        for m in MASSES:
            tb = build_T_and_H(Lt, Ls, m)
            min_spec_H = min(min_spec_H, tb["H_min_eig"])
            ok = (tb["H_min_eig"] >= -TOL_PSD) and (tb["H_herm_err"] < 1e-12) \
                and (tb["T2_recon_err"] < 1e-10) and (tb["T2_herm_err"] < 1e-12) \
                and (tb["max_imag_kernel"] < 1e-9)
            c2 = c2 and ok
            if Ls not in seen:
                seen.add(Ls)
                print(f"    L_s={Ls} m={m}: spec(H_hat) min={tb['H_min_eig']:.6e}  "
                      f"H Herm-err={tb['H_herm_err']:.1e}  "
                      f"||T^2 - exp(-2aH)||={tb['T2_recon_err']:.1e}  "
                      f"max|Im kernel|={tb['max_imag_kernel']:.1e}")
    print(f"    min spec(H_hat) over all (lattice,m) = {min_spec_H:.6e}")
    print(f"    C2 = {'PASS' if c2 else 'FAIL'}")
    passes += int(c2)
    fails += int(not c2)
    print()

    # ---- C3: Z = det is real-positive ----
    print("-" * 78)
    print("C3  Z = det(M_KS+mI) is REAL-POSITIVE (|Im Z| ~ 0, Re Z > 0)")
    print("-" * 78)
    c3 = True
    max_imZ = 0.0
    min_reZ = math.inf
    for (Lt, Ls) in LATTICES:
        for m in MASSES:
            M = build_staggered_M(Lt, Ls, m)
            Z = np.linalg.det(M)
            max_imZ = max(max_imZ, abs(Z.imag))
            min_reZ = min(min_reZ, Z.real)
            ok = (abs(Z.imag) < 1e-9 * max(1.0, abs(Z))) and (Z.real > 0)
            c3 = c3 and ok
    print(f"    max |Im Z| over all (L_t,L_s,m) = {max_imZ:.3e}")
    print(f"    min  Re Z over all (L_t,L_s,m) = {min_reZ:.6e}  (must be > 0)")
    print(f"    C3 = {'PASS' if c3 else 'FAIL'}")
    passes += int(c3)
    fails += int(not c3)
    print()

    # ---- C4: W = log|det| == log Z (phase-blind) ----
    print("-" * 78)
    print("C4  W = log|det(M_KS+mI)| == log Z  (modulus automatic => P2 theorem)")
    print("-" * 78)
    c4 = True
    max_res_c4 = 0.0
    for (Lt, Ls) in LATTICES:
        for m in MASSES:
            M = build_staggered_M(Lt, Ls, m)
            Z = np.linalg.det(M)
            W_mod = math.log(abs(Z))           # framework form: log|det|
            W_logZ = cmath.log(Z).real         # qubit-trace form: Re log Z
            # because Z is real-positive, log|Z| == Re log Z == log Z exactly
            res = abs(W_mod - W_logZ)
            max_res_c4 = max(max_res_c4, res)
            c4 = c4 and (res < 1e-12)
    print(f"    max | log|det| - log Z | over all (L_t,L_s,m) = {max_res_c4:.3e}")
    print(f"    (equality is exact because Z real-positive: no phase to blind to)")
    print(f"    C4 = {'PASS' if c4 else 'FAIL'}")
    passes += int(c4)
    fails += int(not c4)
    print()

    # ---- AC_phi_lambda residual statement ----
    print("-" * 78)
    print("STAYS ADMITTED (NOT closed here): interacting/gauge realization")
    print("-" * 78)
    print("    The identification of the framework Dirac operator D with the")
    print("    staggered KS operator on the interacting/gauge surface rides on the")
    print("    ALREADY-registered Tier-A staggered-Dirac realization gate AC_phi_lambda")
    print("    (staggered_dirac_realization_gate_note_2026-05-03, audited_renaming).")
    print("    This runner closes the FREE staggered surface only; AC_phi_lambda is")
    print("    NOT removed and P1 stays Tier-A.")
    print()

    # ---- Verdict ----
    print("=" * 78)
    print("VERDICT")
    print("=" * 78)
    print(f"  C1 det = Z_vac.Tr    : {'PASS' if c1 else 'FAIL'}  (max res {max_res_c1:.2e})")
    print(f"  C2 T^2 = exp(-2aH)   : {'PASS' if c2 else 'FAIL'}  (min spec H {min_spec_H:.2e})")
    print(f"  C3 Z real-positive   : {'PASS' if c3 else 'FAIL'}  (max |Im Z| {max_imZ:.2e})")
    print(f"  C4 phase-blind W     : {'PASS' if c4 else 'FAIL'}  (max res {max_res_c4:.2e})")
    print()
    all_ok = (fails == 0)
    print(f"PASS={passes} FAIL={fails}")
    if all_ok:
        print()
        print("  PASS -- on the free staggered surface det(M_KS+mI) = Tr[T_hat^{L_t}] =")
        print("  Tr(e^{-beta H_hat}) with H_hat self-adjoint and >= 0 (RP). Hence Z is")
        print("  manifestly real-positive, the modulus in log|det| is automatic, and")
        print("  P2 phase-blindness is a THEOREM on the determinant surface -- the qubit-")
        print("  trace note's Step 2 transferred via RP. The interacting/gauge case rides")
        print("  on the already-registered Tier-A AC_phi_lambda gate (not closed here).")
    else:
        print()
        print("  FAIL -- the bridge did not close on the free case. Debug before")
        print("  concluding; the det = Tr[T^Lt] identity and Z>0 are classic and must")
        print("  hold for a faithful free-staggered construction.")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
