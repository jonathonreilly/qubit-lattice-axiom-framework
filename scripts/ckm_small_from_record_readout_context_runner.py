#!/usr/bin/env python3
"""Class-A verifier: small-CKM-vs-large-PMNS as readout-context misalignment
(CONDITIONAL on an ungrounded posit) + the recorded failure of the detection grounding.

CONDITIONAL observation: the observed mixing is the misalignment between the two sectors'
mass eigenbases.
  - IF both quark mass operators are diagonal in the SAME (corner) basis, U_up=U_dn=I,
    while the neutrino mass is C3-structured, THEN CKM aligns (= identity + small
    registered Cabibbo, no trimaximal column) and PMNS is large (the recorded C3-singlet
    gives a trimaximal column).
This respects/refines the retained no-go (two shared-C3 circulants commute -> CKM is a
permutation): the aligned case is the IDENTITY element of that permutation set.

FAILED grounding (recorded so it is not repeated): the natural "detection/localization"
grounding -- that gauge-charged fermions are recorded in a LOCAL basis -- is REFUTED:
the framework's corner basis is the MOMENTUM (BZ) basis, and a LOCAL per-site observable
is GENERATION-BLIND (identical expectation across generations). So "corner = local
detection basis" is contradicted; the corner-vs-C3 asymmetry is an ungrounded posit.

Verifies:
  (1) both CIRCULANT on a shared C3 -> CKM is a permutation (the retained no-go);
  (2) aligned mass eigenbases (U_up=U_dn=I) -> CKM = identity (refines no-go to identity);
  (3) a small registered deviation -> small Cabibbo CKM, NO trimaximal column;
  (4) C3-structured neutrino vs corner-basis charged lepton -> large PMNS WITH a column;
  (5) FAILED-GROUNDING CONTROL: a local per-site observable is generation-blind (so the
      corner basis is NOT the local basis -> the detection grounding is refuted).
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
J = np.ones((3, 3))
P0 = J / 3                                          # C3-singlet projector (= |W><W|)


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

    # ---- (1) retained no-go: both circulant on a shared C3 -> permutation ----
    Hu = 2 * np.eye(3) + (0.3 + 0.1j) * C + (0.3 - 0.1j) * C.conj().T
    Hd = 1 * np.eye(3) + (0.5 - 0.2j) * C + (0.5 + 0.2j) * C.conj().T
    Vcirc = np.abs(eigb(Hu).conj().T @ eigb(Hd)) ** 2
    check("both CIRCULANT (shared C3) -> CKM is a PERMUTATION (|V| in {0,1}) [retained no-go]",
          is_permutation(Vcirc))

    # ---- (2) aligned mass eigenbases (U_up=U_dn=I) -> CKM = identity ----
    Uup = np.eye(3); Udn = np.eye(3)
    Vid = np.abs(Uup.conj().T @ Udn) ** 2
    check("aligned mass eigenbases (U_up=U_dn=I) -> CKM = IDENTITY permutation "
          "(refines the no-go to the identity)", np.allclose(Vid, np.eye(3)))

    # ---- (3) a small registered deviation -> small Cabibbo, NO trimaximal column ----
    th = 0.225
    R = np.array([[np.cos(th), np.sin(th), 0], [-np.sin(th), np.cos(th), 0], [0, 0, 1]])
    Vckm = np.abs((np.eye(3)).conj().T @ R) ** 2
    check("small registered deviation -> SMALL Cabibbo CKM (near identity)",
          Vckm[0, 0] > 0.9 and Vckm[0, 1] < 0.06, detail=f"|V_us|^2={Vckm[0,1]:.4f}")
    check("CKM has NO trimaximal column (structural opposite of PMNS)",
          len(trimax_cols(Vckm)) == 0)

    # ---- (4) C3-structured neutrino vs corner-basis charged lepton -> large + column ----
    rng = np.random.default_rng(1); A = rng.standard_normal((3, 3)); A = A + A.T
    Mnu = 2 * P0 + (np.eye(3) - P0) @ A @ (np.eye(3) - P0)   # C3-structured (W an eigenvector)
    Upmns = np.abs((np.eye(3)).conj().T @ eigb(Mnu)) ** 2
    check("C3-structured neutrino vs corner-basis charged lepton -> PMNS has a TRIMAXIMAL column",
          len(trimax_cols(Upmns)) >= 1, detail=f"col={trimax_cols(Upmns)}")
    check("PMNS is LARGE (off-diagonal O(1)), unlike CKM",
          Upmns.max(axis=1).min() < 0.8)

    # ---- (5) FAILED-GROUNDING CONTROL: a POSITION observable is generation-blind ----
    # The framework's generations are the MOMENTUM (BZ) corners, not position states. A
    # position eigenstate is a uniform superposition over momenta, so a position-local
    # observable has IDENTICAL expectation on each momentum generation -> local cannot
    # distinguish generations -> the corner (momentum) basis is NOT the local basis ->
    # the detection/localization grounding is refuted. (Cited: FLAVOR_CARRIER_FROM_AXIOMS
    # _MOMENTUM_FORCED, <P_site0> = 1/8 per generation.)
    Fm = np.array([[np.exp(2j * np.pi * x * k / 3) for x in range(3)] for k in range(3)]) / np.sqrt(3)
    gens = [Fm[k] for k in range(3)]                  # 3 MOMENTUM (DFT) modes = the generations
    Px0 = np.zeros((3, 3)); Px0[0, 0] = 1.0           # a position-site projector |0><0|
    exps = [np.real(g.conj() @ Px0 @ g) for g in gens]
    check("FAILED GROUNDING: a POSITION-local observable is GENERATION-BLIND "
          "(identical expectation on each MOMENTUM generation) -> corner(momentum) basis "
          "is NOT the local basis; the detection grounding is refuted",
          np.allclose(exps, exps[0]), detail=f"<P_pos> per momentum generation = {np.round(exps,3).tolist()}")

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: CKM readout-context conditional FAILED.")
        return 1
    print("VERDICT: small-CKM-vs-large-PMNS maps to readout-context misalignment "
          "(CONDITIONAL on the ungrounded posit: quark masses corner-diagonal, neutrino "
          "C3-structured). The detection/localization grounding is REFUTED -- the corner "
          "basis is momentum, and the local per-site observable is generation-blind.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
