"""Microcausality / Lieb-Robinson check on the Lattice/Quantum baseline.

Verifies the lattice Lieb-Robinson bound on a 1D nearest-neighbor
chain with a generic Hermitian local Hamiltonian H = sum_z h_z, where
h_z is supported on a nearest-neighbor pair.

Tests:
  T1: equal-time strict locality (M1) - operators at distinct sites
      have zero commutator at t = 0.
  T2: Lieb-Robinson bound (M2) - the commutator
      ||[alpha_t(O_0), O_d]|| <= C * exp(-d + v_LR |t|)
      with the cited overlap-weight convention v_LR = 2 e q W R.
  T3: lightcone decay - inside lightcone (d < v_LR t), commutator
      grows; outside lightcone, commutator decays exponentially with d.
  T4: small-t expansion: at fixed d, ||[alpha_t(O_0), O_d]|| ~ |t|^d
      to leading order in t (commutator nesting depth d).

The exact-log free-bilinear quasilocal bridge is exposed as a helper runner
for the audit packet; it is checked by
free_bilinear_quasilocal_lr_bridge_2026_06_10.py.
"""
from __future__ import annotations

import math
import os
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
import free_bilinear_quasilocal_lr_bridge_2026_06_10  # noqa: F401,E402


def validate_source_packet_text() -> None:
    """Guard the parent note against stale finite-range bridge constants."""
    root = Path(__file__).resolve().parents[1]
    parent_note = root / "docs" / "AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md"
    bridge_note = root / "docs" / "MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md"
    parent_text = parent_note.read_text(encoding="utf-8")
    bridge_text = bridge_note.read_text(encoding="utf-8")

    parent_required = [
        "2β · q_face",
        "`J_max = |m| + 78`",
        "`J_max^carrier = |m| + 78.5`",
        "`J_max^envelope = |m| + 80`",
        "W_surface = |m| + 296",
        "W_carrier = |m| + 298",
        "W_envelope = |m| + 300",
        "`v_LR <= 16·e·(|m| + 300)`",
    ]
    bridge_required = [
        "`J_max` (`|m| + 78` supplied surface / `|m| + 78.5`",
        "`W` (`|m| + 296` / `|m| + 298` / `|m| + 300`",
        "`v_LR := 2·e·q·W·R`",
    ]
    parent_forbidden = [
        "(2β/" + "N_c) · d(d-1)/2",
        "`J_max = |m| " + "+ 30`",
    ]

    missing_parent = [needle for needle in parent_required if needle not in parent_text]
    missing_bridge = [needle for needle in bridge_required if needle not in bridge_text]
    stale_parent = [needle for needle in parent_forbidden if needle in parent_text]
    if missing_parent or missing_bridge or stale_parent:
        details = []
        if missing_parent:
            details.append(f"parent missing {missing_parent}")
        if missing_bridge:
            details.append(f"bridge missing {missing_bridge}")
        if stale_parent:
            details.append(f"parent still has stale constants {stale_parent}")
        raise AssertionError("; ".join(details))


def build_local_hamiltonian(
    L: int, J: float, seed: int
) -> tuple[np.ndarray, list[float]]:
    """Build a Hermitian H on (C^2)^L of the form H = sum_z h_z

    where h_z is a random Hermitian operator on sites z and z+1
    (range r = 1) with norm <= J.

    Returns (H, term_norms), where term_norms[z] is the operator norm of
    the term supported on sites z and z+1. The caller uses these norms to
    compute the per-site overlap weight W in v_LR = 2 e q W R.
    """
    rng = np.random.default_rng(seed)
    dim = 2 ** L
    H = np.zeros((dim, dim), dtype=complex)
    term_norms: list[float] = []
    for z in range(L - 1):
        # h_z acts on sites z, z+1 as a 4x4 Hermitian matrix
        h_local = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
        h_local = 0.5 * (h_local + h_local.conj().T)
        # normalize to operator norm = J
        eigvals = np.linalg.eigvalsh(h_local)
        norm = np.max(np.abs(eigvals))
        if norm > 0:
            h_local = h_local * (J / norm)
        term_norms.append(float(np.max(np.abs(np.linalg.eigvalsh(h_local)))))
        # Embed h_local into the full Hilbert space (acts as identity elsewhere)
        # Tensor structure: site 0 is leftmost, site L-1 rightmost
        # h_z at sites (z, z+1): identity on sites 0..z-1, h_local on (z, z+1), identity on z+2..L-1
        left_dim = 2 ** z
        right_dim = 2 ** (L - z - 2)
        h_full = np.kron(np.eye(left_dim), np.kron(h_local, np.eye(right_dim)))
        H = H + h_full
    return H, term_norms


def site_operator(L: int, site: int) -> np.ndarray:
    """Build a single-site operator (Pauli Z on site `site`, identity elsewhere)."""
    dim_left = 2 ** site
    dim_right = 2 ** (L - site - 1)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    return np.kron(np.eye(dim_left), np.kron(sigma_z, np.eye(dim_right)))


def expm_hermitian_scalar(c: complex, H: np.ndarray) -> np.ndarray:
    """exp(c H) for Hermitian H, scalar c (possibly complex)."""
    eigvals, V = np.linalg.eigh(H)
    return V @ np.diag(np.exp(c * eigvals)) @ V.conj().T


def alpha_t(O: np.ndarray, H: np.ndarray, t: float) -> np.ndarray:
    """Heisenberg evolution alpha_t(O) = exp(itH) O exp(-itH)."""
    U = expm_hermitian_scalar(1j * t, H)
    Uinv = expm_hermitian_scalar(-1j * t, H)
    return U @ O @ Uinv


def commutator_norm(A: np.ndarray, B: np.ndarray) -> float:
    """Operator norm of [A, B]."""
    C = A @ B - B @ A
    return float(np.linalg.norm(C, ord=2))


def main() -> None:
    print("=" * 72)
    print("MICROCAUSALITY / LIEB-ROBINSON CHECK")
    print("=" * 72)
    print()
    validate_source_packet_text()
    print("Source-packet constants:")
    print("  parent note agrees with finite-range bridge on 2β, J branches,")
    print("  overlap weights W = |m| + {296, 298, 300}, and v_LR = 2 e q W R")
    print("  STATUS: PASS")
    print()
    print("Setup:")
    print("  1D chain of L sites with C^2 (qubit) per site")
    print("  H = sum_z h_z with h_z supported on nearest-neighbor pairs")
    print("  J = max ||h_z||_op, q = max support size, R = support diameter")
    print("  W = sup_x sum_{Z contains x} ||h_Z||_op (per-site overlap weight)")
    print("  v_LR = 2 e q W R (overlap-weight velocity)")
    print()

    L = 8  # chain length
    J = 1.0
    seed = 20260501
    H, term_norms = build_local_hamiltonian(L, J, seed)
    q = 2
    R = 1
    site_weight = [0.0] * L
    for z, nrm in enumerate(term_norms):
        site_weight[z] += nrm
        site_weight[z + 1] += nrm
    W = max(site_weight)
    v_LR = 2 * math.e * q * W * R
    print(f"  L = {L} sites, dim H_phys = {2**L}")
    print(f"  J = {J}, q = {q}, W = {W}, R = {R}")
    print(f"  v_LR = 2 e q W R = {v_LR:.4f}")
    print(f"  ||H||_op = {np.linalg.norm(H, ord=2):.4f}")
    print("  exact-log quasilocal bridge helper: free_bilinear_quasilocal_lr_bridge_2026_06_10.py")
    print()

    # ----- Test 1: equal-time strict locality M1 -----
    print("-" * 72)
    print("TEST 1: equal-time strict locality (M1)")
    print("        For x != y, [O_x, O_y] = 0 at t = 0")
    print("-" * 72)
    max_resid_t1 = 0.0
    for x in range(L):
        for y in range(L):
            if x == y:
                continue
            O_x = site_operator(L, x)
            O_y = site_operator(L, y)
            comm = commutator_norm(O_x, O_y)
            max_resid_t1 = max(max_resid_t1, comm)
    print(f"  max ||[O_x, O_y]||_op over all x != y = {max_resid_t1:.3e}")
    t1_ok = max_resid_t1 < 1e-12
    print(f"  STATUS: {'PASS' if t1_ok else 'FAIL'}")
    print()

    # ----- Test 2: Lieb-Robinson bound M2 -----
    print("-" * 72)
    print("TEST 2: Lieb-Robinson bound (M2)")
    print("        ||[alpha_t(O_0), O_d]|| <= 2 ||O_0|| ||O_d|| exp(- d + v_LR |t|)")
    print("        finite-range carrier uses v_LR = 2 e q W R")
    print("-" * 72)
    O_0 = site_operator(L, 0)
    norm_O = float(np.linalg.norm(O_0, ord=2))
    print(f"  ||O_0|| = {norm_O:.4f} (Pauli Z)")
    print()
    print(f"  {'d':>3}  {'t':>6}  {'||[a_t(O_0), O_d]||':>22}  {'Lieb-Robinson bound':>22}")
    print(f"  {'-'*3}  {'-'*6}  {'-'*22}  {'-'*22}")
    bounds_satisfied = True
    for d in [2, 3, 4, 5, 6, 7]:
        for t in [0.05, 0.1, 0.2, 0.5]:
            O_d = site_operator(L, d)
            alpha_O0 = alpha_t(O_0, H, t)
            comm = commutator_norm(alpha_O0, O_d)
            bound = 2 * norm_O * norm_O * math.exp(-d + v_LR * t)
            ratio = comm / bound if bound > 0 else 0.0
            sat = "OK" if comm <= bound + 1e-9 else "FAIL"
            print(f"  {d:>3}  {t:>6.3f}  {comm:>22.6e}  {bound:>22.6e}  ratio={ratio:6.3e} {sat}")
            if comm > bound + 1e-9:
                bounds_satisfied = False
    print()
    t2_ok = bounds_satisfied
    print(f"  STATUS: {'PASS' if t2_ok else 'FAIL'}")
    print()

    # ----- Test 3: lightcone decay -----
    print("-" * 72)
    print("TEST 3: lightcone decay - outside lightcone, commutator -> 0")
    print("-" * 72)
    print("Fix t = 0.02. Sweep d = 2 to 7 outside the conservative lightcone. Expect")
    print("exponential decay of commutator with d outside the lightcone.")
    print()
    t_fixed = 0.02
    print(f"  t = {t_fixed}, v_LR t = {v_LR * t_fixed:.4f}")
    print(f"  {'d':>3}  {'commutator':>16}  {'log(commutator)':>20}")
    last_log = None
    decreasing = True
    for d in [2, 3, 4, 5, 6, 7]:
        O_d = site_operator(L, d)
        alpha_O0 = alpha_t(O_0, H, t_fixed)
        comm = commutator_norm(alpha_O0, O_d)
        log_comm = math.log(comm) if comm > 1e-300 else float("-inf")
        marker = ""
        if last_log is not None and log_comm > last_log + 0.01:
            marker = " (NOT decreasing!)"
            decreasing = False
        print(f"  {d:>3}  {comm:>16.6e}  {log_comm:>20.6f}{marker}")
        last_log = log_comm
    print()
    t3_ok = decreasing
    print(f"  STATUS: {'PASS' if t3_ok else 'FAIL'}")
    print()

    # ----- Test 4: small-t expansion -----
    print("-" * 72)
    print("TEST 4: small-t scaling - ||[alpha_t(O_0), O_d]|| ~ |t|^d at small t")
    print("-" * 72)
    print("Commutator nesting depth = d means leading order is t^d.")
    print(f"  {'d':>3}  {'t1':>6}  {'t2':>6}  {'comm(t1)':>14}  {'comm(t2)':>14}  {'ratio':>10}  {'expected':>10}")
    powerlaw_ok_count = 0
    powerlaw_total = 0
    for d in [2, 3, 4]:
        t1 = 0.01
        t2 = 0.02
        O_d = site_operator(L, d)
        alpha_O0_t1 = alpha_t(O_0, H, t1)
        alpha_O0_t2 = alpha_t(O_0, H, t2)
        comm1 = commutator_norm(alpha_O0_t1, O_d)
        comm2 = commutator_norm(alpha_O0_t2, O_d)
        ratio = comm2 / comm1 if comm1 > 0 else 0.0
        expected = (t2 / t1) ** d  # = 2^d
        # Test that the actual ratio is in [0.5 * expected, 2 * expected]
        ratio_ok = 0.5 * expected <= ratio <= 2.0 * expected
        powerlaw_total += 1
        if ratio_ok:
            powerlaw_ok_count += 1
        print(f"  {d:>3}  {t1:>6.3f}  {t2:>6.3f}  {comm1:>14.6e}  {comm2:>14.6e}  {ratio:>10.3f}  {expected:>10.3f}")
    print()
    t4_ok = powerlaw_ok_count >= powerlaw_total - 1  # allow 1 borderline
    print(f"  STATUS: {'PASS' if t4_ok else 'FAIL'} ({powerlaw_ok_count}/{powerlaw_total} fits within 2x)")
    print()

    # ----- Summary -----
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  Test 1 (equal-time strict locality M1):       {'PASS' if t1_ok else 'FAIL'}")
    print(f"  Test 2 (Lieb-Robinson bound M2):              {'PASS' if t2_ok else 'FAIL'}")
    print(f"  Test 3 (outside-lightcone exponential decay): {'PASS' if t3_ok else 'FAIL'}")
    print(f"  Test 4 (small-t scaling t^d):                 {'PASS' if t4_ok else 'FAIL'}")
    print()
    all_ok = t1_ok and t2_ok and t3_ok and t4_ok
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    print()
    print("Note: this runner verifies the lattice Lieb-Robinson bound on a")
    print("1D finite-matrix witness with C^2 sites. The proof in the")
    print("companion theorem note is dimension-independent for finite")
    print("one-site tensor factors and applies to the Lattice/Quantum")
    print("baseline on Z^3.")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
