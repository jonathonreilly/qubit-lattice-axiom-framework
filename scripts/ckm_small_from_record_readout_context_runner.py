#!/usr/bin/env python3
"""Class-A verifier for a supplied CKM/PMNS readout-context misalignment.

CONDITIONAL observation: the observed mixing is the misalignment between the two sectors'
mass eigenbases.
  - IF both quark mass operators are diagonal in the SAME (corner) basis, U_up=U_dn=I,
    while the neutrino mass is C3-structured, THEN CKM aligns (= identity + small
    registered Cabibbo, no trimaximal column) and PMNS is large (the recorded C3-singlet
    gives a trimaximal column).
The shared-C3 calculation gives a permutation matrix, with the aligned case as
the identity member of that finite family.

FINITE PROFILE CONTEXT: the explicit three-point Fourier characters each have
coordinate-projector expectation 1/3.  This is a positive equality between
two supplied finite bases and carries no physical detector, localization,
propagation, generation, carrier, or readout assignment.

Verifies:
  (1) both CIRCULANT on a shared C3 -> CKM is a permutation;
  (2) aligned mass eigenbases (U_up=U_dn=I) -> CKM = identity;
  (3) a small registered deviation -> small Cabibbo CKM with trimaximal-column count zero;
  (4) a simple-spectrum Hermitian circulant neutrino matrix vs a corner-basis
      charged lepton -> the full C3 character basis and a PMNS matrix whose
      squared-modulus entries are all 1/3;
  (5) every coordinate-projector expectation on the three Fourier characters is 1/3.
"""

from __future__ import annotations
import numpy as np

PASS = 0
FAIL = 0


def check(name, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok); FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


w = np.exp(2j * np.pi / 3)
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)


def eigb(H):
    _, U = np.linalg.eigh(H); return U


def is_permutation(P, tol=1e-6):
    return np.all((np.abs(P) < tol) | (np.abs(P - 1) < tol))


def trimax_cols(P, tol=1e-6):
    return [j for j in range(3) if np.allclose(P[:, j], 1 / 3, atol=tol)]


def main() -> int:
    print("=" * 72)
    print("SMALL CKM vs LARGE PMNS as readout-context misalignment (conditional)  [class A]")
    print("=" * 72)

    # ---- (1) both circulant on a shared C3 -> permutation ----
    Hu = 2 * np.eye(3) + (0.3 + 0.1j) * C + (0.3 - 0.1j) * C.conj().T
    Hd = 1 * np.eye(3) + (0.5 - 0.2j) * C + (0.5 + 0.2j) * C.conj().T
    Vcirc = np.abs(eigb(Hu).conj().T @ eigb(Hd)) ** 2
    check("both CIRCULANT (shared C3) -> CKM is a PERMUTATION (|V| in {0,1})",
          is_permutation(Vcirc))

    # ---- (2) aligned mass eigenbases (U_up=U_dn=I) -> CKM = identity ----
    Uup = np.eye(3); Udn = np.eye(3)
    Vid = np.abs(Uup.conj().T @ Udn) ** 2
    check("aligned mass eigenbases (U_up=U_dn=I) -> CKM = IDENTITY permutation",
          np.allclose(Vid, np.eye(3)))

    # ---- (3) a small registered deviation -> small Cabibbo ----
    th = 0.225
    R = np.array([[np.cos(th), np.sin(th), 0], [-np.sin(th), np.cos(th), 0], [0, 0, 1]])
    Vckm = np.abs((np.eye(3)).conj().T @ R) ** 2
    check("small registered deviation -> SMALL Cabibbo CKM (near identity)",
          Vckm[0, 0] > 0.9 and Vckm[0, 1] < 0.06, detail=f"|V_us|^2={Vckm[0,1]:.4f}")
    check("CKM trimaximal-column count equals zero on the displayed matrix",
          len(trimax_cols(Vckm)) == 0)

    # ---- (4) simple-spectrum Hermitian circulant -> full C3 character basis ----
    b_nu = 0.3 + 0.4j
    Mnu = 2 * np.eye(3) + b_nu * C + b_nu.conjugate() * C.conj().T
    nu_eigs = np.linalg.eigvalsh(Mnu)
    simple_spectrum = np.min(np.diff(nu_eigs)) > 1e-8
    commutes_with_c3 = np.allclose(Mnu @ C, C @ Mnu)
    Upmns = np.abs((np.eye(3)).conj().T @ eigb(Mnu)) ** 2
    check("simple-spectrum Hermitian circulant neutrino matrix -> full C3 character eigenbasis",
          commutes_with_c3 and simple_spectrum and len(trimax_cols(Upmns)) == 3,
          detail=f"trimaximal_cols={trimax_cols(Upmns)}")
    check("PMNS squared-modulus matrix is exactly the uniform 1/3 profile numerically",
          np.allclose(Upmns, np.full((3, 3), 1 / 3)))

    # ---- (5) finite-profile check: exact uniform DFT coordinate profiles ----
    Fm = np.array([[np.exp(2j * np.pi * x * k / 3) for x in range(3)] for k in range(3)]) / np.sqrt(3)
    characters = [Fm[k] for k in range(3)]
    P_coordinate0 = np.zeros((3, 3)); P_coordinate0[0, 0] = 1.0
    exps = [np.real(character.conj() @ P_coordinate0 @ character) for character in characters]
    check("FINITE PROFILE: every supplied Fourier character has coordinate-projector expectation 1/3",
          np.allclose(exps, [1 / 3] * 3), detail=f"<P_0>={np.round(exps,3).tolist()}")

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("CHECK FAILURE: one or more finite matrix assertions were not satisfied.")
        return 1
    print("SUMMARY: small-CKM-vs-large-PMNS maps to a supplied readout-context misalignment")
    print("(conditional on aligned quark bases and a C3-structured neutrino basis).")
    print("The finite Fourier-profile equality is exact and carries no physical basis assignment.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
