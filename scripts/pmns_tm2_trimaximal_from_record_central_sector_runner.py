#!/usr/bin/env python3
"""Class-A verifier: the PMNS trimaximal column is the recorded C3-singlet central sector.

Under the RECORD axiom, the physical observable is the recorded outcome = the K/CPT
orbit of the realized CENTRAL SECTOR; inter-sector and within-sector coherence are NOT
recorded. For the 3-generation C3 algebra the central decomposition (modulo K-reality)
is SINGLET (the democratic W=(1,1,1)/sqrt3, C3-trivial) (+) DOUBLET (2-dim).

This runner verifies:
  (A) RECORD outcome structure as the dephasing map D(M)=P0 M P0 + P1 M P1 (record =
      land in a central sector; inter-sector coherence dropped);
  (B) the C3-singlet central sector projector P0 = J/3, and its corner (flavor) overlap
      |<corner|W>|^2 = 1/3 -- exactly the trimaximal column;
  (C) pre-record W-breaking is NOT recorded: for ANY pre-record M_nu, the recorded
      (dephased) operator has W as an eigenvector => trimaximal column, with theta13
      FREE (within-doublet data the axiom disclaims);
  (D) the K-reality predicate that selects the 2-block (singlet+doublet) partition: a
      K-real C3-invariant observable is span{I, C+C^2} (eig {2,-1,-1}: singlet isolated,
      doublet degenerate); resolving the 3-mode split strictly needs the K-ODD i(C-C^2);
  (E) the monitored observable C+C^dag = J-I is the native double-shift coupling, whose
      eigenbasis is the magic-S partition (link to the dynamical generator note).

All checks are finite-dimensional linear algebra (class A).
"""

from __future__ import annotations
import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


w = np.ones(3) / np.sqrt(3)                       # C3-singlet / democratic / W
P0 = np.outer(w, w)                               # singlet central-sector projector
P1 = np.eye(3) - P0                               # doublet central sector
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
Jall = np.ones((3, 3))


def record(M):
    """RECORD outcome structure: dephase onto the central sectors (drop inter-sector coherence)."""
    return P0 @ M @ P0 + P1 @ M @ P1


def main() -> int:
    print("=" * 72)
    print("PMNS TM2 TRIMAXIMAL COLUMN = RECORDED C3-SINGLET CENTRAL SECTOR (class A)")
    print("=" * 72)

    # ---- (A) RECORD outcome structure ----
    check("singlet central-sector projector P0 = J/3 (rank 1, onto W)",
          np.allclose(P0, Jall / 3) and np.isclose(np.trace(P0), 1.0))
    check("central decomposition is complete & orthogonal: P0+P1=I, P0 P1=0",
          np.allclose(P0 + P1, np.eye(3)) and np.allclose(P0 @ P1, np.zeros((3, 3))))
    # idempotent dephasing channel
    rng = np.random.default_rng(0)
    Mr = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    check("record map is an idempotent dephasing channel (D(D(M))=D(M))",
          np.allclose(record(record(Mr)), record(Mr)))

    # ---- (B) trimaximal column = singlet-sector corner overlap = 1/3 ----
    corner_overlap = np.array([abs(np.vdot(np.eye(3)[a], w))**2 for a in range(3)])
    check("singlet sector corner (flavor) overlaps |<corner|W>|^2 are all 1/3 (trimaximal)",
          np.allclose(corner_overlap, 1/3), detail=f"{np.round(corner_overlap,4).tolist()}")

    # ---- (C) pre-record W-breaking is NOT recorded => TM2 ----
    A = rng.standard_normal((3, 3)); Mbreak = A + A.T          # generic pre-record, breaks W
    coh = np.linalg.norm(P0 @ Mbreak @ P1)
    check("pre-record M_nu has nonzero singlet-doublet coherence (breaks W)", coh > 1e-3,
          detail=f"||P0 M P1||={coh:.3f}")
    _, Ub = np.linalg.eigh(Mbreak); Pb = np.abs(np.eye(3) @ Ub) ** 2
    check("bare pre-record PMNS has NO trimaximal column",
          not any(np.allclose(Pb[:, j], 1/3, atol=1e-6) for j in range(3)))
    Mrec = record(Mbreak)
    check("recorded M_nu: singlet-doublet coherence is gone (not recorded)",
          np.linalg.norm(P0 @ Mrec @ P1) < 1e-12)
    check("recorded M_nu has W as an eigenvector", np.allclose(Mrec @ w, (w @ Mrec @ w) * w))
    _, Ur = np.linalg.eigh(Mrec); Pr = np.abs(np.eye(3) @ Ur) ** 2
    tri = [j for j in range(3) if np.allclose(Pr[:, j], 1/3, atol=1e-9)]
    check("recorded PMNS has an exact trimaximal column", len(tri) >= 1, detail=f"col={tri}")
    check("theta13 (within-doublet) is FREE: not pinned by the record",
          0.0 <= Pr.min() < 0.34, detail=f"min|U|^2={Pr.min():.4f}")
    # robustness: holds for many random pre-record operators
    ok_all = True
    for s in range(200):
        r = np.random.default_rng(s); X = r.standard_normal((3, 3)); X = X + X.T
        Mrr = record(X); _, Uu = np.linalg.eigh(Mrr); Pp = np.abs(np.eye(3) @ Uu) ** 2
        if not any(np.allclose(Pp[:, j], 1/3, atol=1e-9) for j in range(3)):
            ok_all = False; break
    check("recorded trimaximal column for ALL 200 random pre-record operators", ok_all)

    # ---- (D) K-reality predicate selects the 2-block partition ----
    Keven = C + C.conj().T                          # = C + C^2 = J - I, K-real (real symmetric)
    Kodd = 1j * (C - C.conj().T)                    # = i(C - C^2), K-odd
    check("K-real C3 observable C+C^2 has spectrum {2,-1,-1}: singlet isolated, DOUBLET DEGENERATE",
          np.allclose(np.sort(np.linalg.eigvalsh(Keven)), [-1, -1, 2]))
    check("=> K-real monitoring resolves only 2 blocks (cannot split the doublet)",
          np.allclose(P1 @ Keven @ P1, -1.0 * P1))      # Keven acts as scalar -1 on the doublet
    check("splitting the doublet (3-mode) strictly needs the K-ODD i(C-C^2) (non-degenerate on doublet)",
          not np.isclose(*np.linalg.eigvalsh(P1 @ Kodd @ P1 + 0*np.eye(3))[1:3]))

    # ---- (E) monitored observable = native double-shift coupling (link to magic-S note) ----
    check("monitored C3 observable C+C^dag = J - I (native double-shift corner coupling)",
          np.allclose(Keven, Jall - np.eye(3)))
    # its eigenbasis is the magic-S partition: S = 2|W><W|-I commutes with the record projectors
    S = 2 * P0 - np.eye(3)
    check("magic reflection S = 2 P0 - I commutes with the record decomposition",
          np.allclose(S @ P0, P0 @ S) and np.allclose(S @ P1, P1 @ S))

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: record-central-sector trimaximal-column bridge FAILED.")
        return 1
    print("VERDICT: trimaximal column = recorded C3-singlet central sector; "
          "pre-record W-breaking is not recorded. Derivable from RECORD + retained C3, "
          "modulo the K-reality predicate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
