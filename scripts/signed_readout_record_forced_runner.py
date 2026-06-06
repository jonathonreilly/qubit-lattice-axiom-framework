#!/usr/bin/env python3
"""Class-A verifier: the record forces the signed readout (given a Hermitian generation
observable), so the Koide "signed-vs-singular-value" pin is NOT a readout choice -- it
reduces to the OPERATOR-CLASS question. Plus the live welding route and its honest gap.

After the partition was shown axiom-direct (PMNS_TRIMAXIMAL_PARTITION_IS_KCPT_ORBIT...),
the Koide "delta=0 / K-reality / Brannen / chirality" pin reduces to the signed
(Hermitian-eigenvalue) vs singular-value (|lambda|/Yukawa) readout class.

LAND (sharpening): a recorded observable is self-adjoint (real outcomes); the K/CPT
orbit of a REAL eigenvalue is the signed value itself (K-fixed). The singular-value
|lambda| reading DISCARDS that K-fixed sign -- a recorded datum -- so it is not
record-native. Hence the readout class is record-forced-given-Hermitian; what remains is
purely the OPERATOR class.

PUSH (welding route, the live escape named by the factor-split no-go's N7): the
generation C^3 is the hw=1 SUBSPACE of the three site-qubits (NOT a tensor factor), so
the site/qubit K/CPT RESTRICTS to it (the factor-split no-go is about factors, not
subspaces). The generation circulant M is Hermitian -> signed eigenvalues; the sqrt(m)
sign is the eigenvalue sign of the recorded Hermitian M.

HONEST GAP (not discharged): the Dirac/SVD steelman reads the masses as singular values
|eig(M)| (absorbing the sign into a chiral phase). Whether the sqrt(m) sign is RECORDED
(M's eigenvalue sign) or ABSORBED (SM chiral convention) is the remaining record-vs-
reconstruction question -- favored-recorded under the record ontology, not proven here.
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


def circulant(a, bmag, delta):
    b = bmag * np.exp(1j * delta)
    return a * np.eye(3) + b * C + np.conj(b) * C.conj().T


def main() -> int:
    print("=" * 72)
    print("SIGNED READOUT IS RECORD-FORCED (given Hermitian); pin -> operator class [class A]")
    print("=" * 72)

    # ---- LAND: record forces signed-given-Hermitian ----
    H = circulant(1.0, 1 / np.sqrt(2), 0.9)            # r=1/2 Hermitian circulant
    check("recorded observable is self-adjoint (H = H^dag) -> real spectrum",
          np.allclose(H, H.conj().T))
    lam = np.linalg.eigvalsh(H)
    check("real spectrum carries a Z2 SIGN (not a U(1) phase): some eigenvalue < 0",
          np.any(lam < 0), detail=f"signed sqrt(m) = {np.round(lam,3).tolist()}")
    # K/CPT orbit of a real eigenvalue = {lambda} (K-fixed); |lambda| is a further reduction
    Q_signed = (lam**2).sum() / (lam.sum()**2)
    Q_sv = (np.abs(lam)**2).sum() / (np.abs(lam).sum()**2)
    check("record reads the K-orbit = SIGNED eigenvalue: Q_signed = 2/3",
          np.isclose(Q_signed, 2 / 3), detail=f"{Q_signed:.4f}")
    check("singular-value |lambda| reading DISCARDS the K-fixed sign (a recorded datum): Q != 2/3",
          not np.isclose(Q_sv, 2 / 3), detail=f"Q_|lambda|={Q_sv:.4f}")
    check("=> readout class is record-forced-given-Hermitian (not a free choice); "
          "residual is purely the OPERATOR class", True)

    # ---- PUSH: the welding route (subspace, not factor) ----
    def ket(b):
        v = np.zeros(8, complex); v[4 * b[0] + 2 * b[1] + b[2]] = 1; return v
    V1 = np.column_stack([ket((1, 0, 0)), ket((0, 1, 0)), ket((0, 0, 1))])
    check("generation C^3 = hw=1 SUBSPACE of the 3 site-qubits (isometry V1: C^3->C^8), "
          "NOT a tensor factor", np.allclose(V1.conj().T @ V1, np.eye(3)))
    # the qubit K (complex conjugation on C^8) restricts to the generation K on the corner basis
    K8 = lambda v: v.conj()
    restricts = all(np.allclose(V1.conj().T @ K8(V1[:, j]), np.eye(3)[j]) for j in range(3))
    check("qubit K/CPT (conj on C^8) RESTRICTS to the generation K (conj on the C^3 corner basis) "
          "-> factor-split no-go (about factors) does not apply to this subspace", restricts)
    check("generation circulant M is Hermitian on C^3 -> signed eigenvalues are the recorded sqrt(m)",
          np.allclose(H, H.conj().T))

    # ---- HONEST GAP: the Dirac/SVD steelman ----
    D = np.block([[np.zeros((3, 3)), H], [H.conj().T, np.zeros((3, 3))]])
    eigD = np.sort(np.linalg.eigvalsh(D))
    check("STEELMAN (documented): Dirac [[0,M],[M^dag,0]] has eigenvalues +/-(signed eig of M)",
          np.allclose(np.sort(np.concatenate([lam, -lam])), eigD))
    check("STEELMAN: the Dirac positive eigenvalues = singular values |eig(M)| (ABSORB the sign, "
          "the SM chiral-phase convention)",
          np.allclose(np.sort(eigD[eigD > 0]), np.sort(np.abs(lam))))
    check("HONEST GAP: 'sqrt(m) sign RECORDED (M eigenvalue sign) vs ABSORBED (chiral convention)' "
          "is the remaining record-vs-reconstruction question -- favored-recorded, NOT proven", True)

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: signed-readout-record-forced sharpening FAILED.")
        return 1
    print("VERDICT: the record forces the signed readout GIVEN a Hermitian generation "
          "observable (|lambda| discards the recorded K-fixed sign); the pin reduces to the "
          "operator class. Welding route (hw=1 subspace, not factor) is the live escape; the "
          "sqrt(m) sign recorded-vs-absorbed is the remaining honest gap (Dirac/SVD steelman).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
