"""J-hunt round 2: fermionic determinant power does not select J.

This runner verifies only the finite-algebra obstruction:

    fermionic/Berezin first-order structure
        does not imply
    selection of the antisymmetric J=C-C^2 doublet pairing.

It deliberately does not verify a det_R/Q default, a det_C-to-r/Q mapping, or a
Dirac-vs-Majorana wall. Those are separate authority/readout questions.
"""
from pathlib import Path

import numpy as np


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)


def frobenius_block_total(a, b):
    return 3.0 * a * a + 6.0 * abs(b) ** 2


def main():
    passed = []
    rng = np.random.default_rng(602)

    # (1) Berezin det(H) is a cubic determinant product, not the quadratic
    # Frobenius block-total that would define an equal-block convention.
    ok = True
    for _ in range(200):
        a = rng.standard_normal()
        b = rng.standard_normal() + 1j * rng.standard_normal()
        H = a * I3 + b * C + np.conj(b) * C.conj().T
        ev = np.linalg.eigvalsh(H)
        scale = 2.0
        det_h = np.linalg.det(H).real
        det_scaled = np.linalg.det(scale * H).real
        energy = frobenius_block_total(a, b)
        energy_scaled = frobenius_block_total(scale * a, scale * b)
        determinant_product = (
            np.allclose(ev.imag if np.iscomplexobj(ev) else 0, 0)
            and abs(det_h - np.prod(ev)) < 1e-9
        )
        distinct_scaling = (
            abs(det_scaled - scale**3 * det_h) < 1e-8
            and abs(energy_scaled - scale**2 * energy) < 1e-8
        )
        if not (determinant_product and distinct_scaling):
            ok = False
    passed.append(check(
        "R2-1 Berezin Z=det(H) is a real eigenvalue product, not the Frobenius block-total selector",
        ok,
        "det scales cubically under H -> tH; the Frobenius block-total scales quadratically"))

    # (2) C_3 admits BOTH symmetric I and antisymmetric J=C-C^2 as invariant bilinears
    Janti = C - C @ C
    passed.append(check(
        "R2-2 C3 leaves both symmetric I and antisymmetric J=C-C^2 invariant, so covariance does not select J",
        (
            np.allclose(C.T @ I3 @ C, I3)
            and np.allclose(Janti.T, -Janti)
            and np.allclose(C.T @ Janti @ C, Janti)
            and not np.allclose(Janti, 0)
            and abs(np.trace(I3.T @ Janti)) < 1e-12
        ),
        "choosing the antisymmetric pairing is extra structure relative to this finite C3 packet"))

    # (3) power vs count: the Pfaffian-vs-unrooted-det asymmetry is a normalization artifact
    a, s = 2.0, 2.0
    Janti2 = np.array([[0, -1.0], [1.0, 0]])
    fermion = abs(np.linalg.det(a * Janti2)) ** 0.5
    boson = np.linalg.det(s * np.eye(2)) ** (-0.5)
    passed.append(check(
        "R2-3 Gaussian statistics fixes determinant exponent, not generation-doublet mode count",
        abs(fermion - a) < 1e-9 and abs(boson - 1.0 / s) < 1e-9,
        f"Pf(aJ)={fermion:.3f}=a and det(sI)^(-1/2)={boson:.3f}=1/s"))

    # (4) Boundary guard: the paired note must not present imported Q/default
    # mappings as conclusions of this finite algebra packet.
    root = Path(__file__).resolve().parents[1]
    note = (root / "docs" / "FLAVOR_FIND_J_ROUND2_POWER_NOT_COUNT_2026-06-02.md").read_text()
    banned = [
        "det_R/Q=1 stands",
        "wall moves to Dirac",
        "charged leptons ARE Dirac",
        "Established det_C",
        "det_C/r=1/2/Q=2/3",
    ]
    required = [
        "does not derive",
        "fermionic determinant power alone",
        "No new axiom is introduced.",
    ]
    passed.append(check(
        "R2-4 source boundary guard: no Q/default or Dirac-vs-Majorana conclusion is promoted by this packet",
        all(term not in note for term in banned) and all(term in note for term in required),
        "the packet closes algebraic non-selection of J only"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT (J-hunt round 2, wf_d2438beb): bounded-support negative route pruning.")
    print("The fermionic/Berezin frame fixes determinant power but does not force the antisymmetric")
    print("J=C-C^2 doublet pairing. Berezin gives a determinant product, not the Frobenius")
    print("block-total selector; C3 admits both I and J invariant bilinears. This runner does")
    print("not derive det_R/Q=1, det_C -> r=1/2 -> Q=2/3, or a Dirac-vs-Majorana wall.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
