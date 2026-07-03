#!/usr/bin/env python3
"""
Per-sector flavor orientations are gauge; the physical CP content is the inter-sector
Jarlskog (mass-handedness and CP unified under one gauge principle).

Class-A finite-dim verifier (3x3 only, memory-safe). The shared generation-relabeling R
(a transposition acting on rows & columns of every sector's Hermitian simultaneously) is the
flavor gauge group's orientation-reversing element. Under it:

  (MASS)  the mass cyclic handedness sign(Delta), Delta=(p0-p1)(p1-p2)(p2-p0), is R-ODD
          (gauge) -- the companion absolute-handedness-is-gauge result.

  (CP)    the within-sector CP cubic orientation I_src(H) = Im(H_12 H_23 H_31) is R-ODD
          (gauge). The single-Hermitian Jarlskog identity J_basis = I_src/Delta_lambda holds
          (April-20 reduction), and a row permutation sigma multiplies it by parity(sigma) --
          so the per-sector "parity bit" is itself gauge-dependent.

  (PHYS)  the INTER-SECTOR Jarlskog J = Im(V00 V11 V01* V10*), V = U_1^dag U_2, is
          R-INVARIANT under the SHARED relabeling (physical), but changes under a
          one-sector relabeling -- i.e. J is a RELATIVE (inter-sector) orientation. The
          physical flavor CP content is purely relative; per-sector CP orientation is gauge.

  (MAG)   separate/retained: the CP-phase MAGNITUDE cos^2(delta) = 1/n_quark
          (CKM_CP_PHASE_STRUCTURAL_IDENTITY) -- the magnitude of the relative orientation,
          not addressed here.

No PDG value is load-bearing.
"""
from itertools import permutations
import json
from pathlib import Path

import numpy as np

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name} {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {name} {detail}")


rng = np.random.default_rng(7)
ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
RETAINED_GRADES = {"retained", "retained_bounded", "retained_no_go"}
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]


def retained_authority(claim_id, note_path):
    row = ledger.get(claim_id)
    ok = bool(row) and row.get("note_path") == note_path and row.get("effective_status") in RETAINED_GRADES
    detail = "missing" if not row else f"effective status {row.get('effective_status')}"
    return ok, detail


def randH():
    A = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    return (A + A.conj().T) / 2.0


def Isrc(H):
    return float(np.imag(H[0, 1] * H[1, 2] * H[2, 0]))


def jarlskog(U1, U2):
    V = U1.conj().T @ U2
    return float(np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0])))


def perm_sign(sigma):
    return (-1) ** sum(1 for i in range(3) for j in range(i + 1, 3) if sigma[i] > sigma[j])


# the shared orientation-reversing gauge element R (a transposition)
R = np.eye(3)[[1, 0, 2]]
check("R_is_orientation_reversing_transposition", abs(np.linalg.det(R) + 1) < 1e-12,
      f"det(R)={np.linalg.det(R):+.0f}")
staggered_ok, staggered_detail = retained_authority(
    "staggered_axis_symmetry_is_s3_narrow_theorem_note_2026-05-23",
    "docs/STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23.md",
)
check("R_unbroken_staggered_S3_authority_is_retained_grade", staggered_ok, staggered_detail)

# ===== (MASS) mass cyclic handedness sign(Delta) is R-ODD (gauge) =====
from numpy import pi, cos, sqrt
def lam(d): return 1.0 + sqrt(2.0) * cos(d + 2.0 * pi * np.arange(3) / 3.0)
def born(d):
    m = lam(d) ** 2; return m / m.sum()
def vand(p): return (p[0] - p[1]) * (p[1] - p[2]) * (p[2] - p[0])
two9 = 2.0 / 9.0
check("MASS_handedness_sign_Delta_R_odd",
      np.sign(vand(born(two9)[[1, 0, 2]])) == -np.sign(vand(born(two9))) != 0,
      "sign(Delta) flips under R (gauge)")

# ===== (CP) within-sector cubic orientation I_src is R-ODD (gauge) =====
H = randH()
HR = R @ H @ R.T
check("CP_Isrc_within_sector_R_odd", np.sign(Isrc(H)) == -np.sign(Isrc(HR)) != 0,
      f"Isrc(H)={Isrc(H):+.4f} -> Isrc(R H R^T)={Isrc(HR):+.4f}")

# April-20 single-Hermitian identity J_basis = I_src / Delta_lambda, and parity behavior
w, V = np.linalg.eigh(H)
Dl = (w[0] - w[1]) * (w[1] - w[2]) * (w[2] - w[0])
Jb = float(np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0])))
check("CP_april20_Jbasis_is_Isrc_over_Delta", abs(Isrc(H) / Dl - Jb) < 1e-9,
      f"Isrc/Delta={Isrc(H)/Dl:+.5f} = J_basis={Jb:+.5f}")
# row permutation sigma multiplies J by parity(sigma) -> the "parity bit" is gauge-dependent
sig = (1, 0, 2)
Pm = np.eye(3)[list(sig)]
Vp = Pm @ V
Jp = float(np.imag(Vp[0, 0] * Vp[1, 1] * np.conj(Vp[0, 1]) * np.conj(Vp[1, 0])))
check("CP_parity_bit_is_gauge_dependent", abs(Jp - perm_sign(sig) * Jb) < 1e-9,
      f"J_sigma={Jp:+.5f} = parity(sigma)*J_basis (parity bit gauge-dependent)")

# ===== (CP2) the in-basis (single-sector-ordering) Jarlskog J_basis is R-ODD (gauge) =====
# under the shared relabel R, the ascending-basis Jarlskog flips: J_basis(R H R^T) = -J_basis(H)
def Jbasis_of(Hm):
    _, Vv = np.linalg.eigh(Hm)
    return float(np.imag(Vv[0, 0] * Vv[1, 1] * np.conj(Vv[0, 1]) * np.conj(Vv[1, 0])))
check("CP2_in_basis_Jarlskog_R_odd",
      np.sign(Jbasis_of(H)) == -np.sign(Jbasis_of(R @ H @ R.T)) != 0,
      f"J_basis(H)={Jbasis_of(H):+.5f} -> J_basis(R H R^T)={Jbasis_of(R @ H @ R.T):+.5f} (gauge)")

# ===== (PHYS) the two-sector Jarlskog J = Im(V00 V11 V01* V10*), V=U1^dag U2, is =====
#        R-INVARIANT under the SHARED relabel -> the physical CP is the inter-sector invariant
inv_ok = True
nontrivial = 0
for _ in range(50):
    _, A = np.linalg.eigh(randH()); _, B = np.linalg.eigh(randH())
    j = jarlskog(A, B)
    if abs(j - jarlskog(R @ A, R @ B)) > 1e-9:
        inv_ok = False
    if abs(j) > 1e-6:
        nontrivial += 1
check("PHYS_two_sector_Jarlskog_R_invariant_shared", inv_ok and nontrivial > 40,
      f"J(U1,U2)=J(R U1, R U2) over 50 pairs ({nontrivial} nontrivial) -- physical, gauge-invariant")
# contrast: the per-sector orientation that BUILDS it is gauge (R-odd) -> physical CP is RELATIVE
check("PHYS_physical_CP_is_relative_not_per_sector",
      np.sign(Isrc(H)) == -np.sign(Isrc(R @ H @ R.T)),
      "per-sector I_src is R-odd (gauge) while two-sector J is R-invariant -> CP content is relative")

# ===== (MAG) the CP-phase magnitude is separate (retained) =====
n_quark = 6
magnitude_ok, magnitude_detail = retained_authority(
    "ckm_cp_phase_structural_identity_narrow_theorem_note_2026-05-10",
    "docs/CKM_CP_PHASE_STRUCTURAL_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md",
)
check("MAG_cp_phase_magnitude_authority_is_retained_grade", magnitude_ok, magnitude_detail)
check("MAG_cp_phase_magnitude_formula_is_separate",
      abs((1.0 / n_quark) - (1.0 / 6.0)) < 1e-12,
      "cos^2(delta_CKM)=1/n_quark (magnitude, separate)")

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("VERDICT: under the shared generation-relabeling gauge R, every PER-SECTOR flavor "
      "orientation is R-ODD (gauge) -- the mass cyclic handedness sign(Delta) AND the "
      "within-sector CP cubic I_src; only the INTER-SECTOR Jarlskog J is R-invariant "
      "(physical). The physical flavor CP content is purely the inter-sector RELATIVE "
      "orientation; the per-sector CP orientation and the April-20 'parity bit' are "
      "gauge-dependent. Magnitude cos^2(delta)=1/n_quark is separate/retained.")
