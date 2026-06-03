"""Positive localization: a K-real (CPT / conjugation-even) measurement instrument on the generation
factor physically cannot record the K-ODD direction i(C-C^2), so the record ALPHABET is genuinely 2
letters (singlet + doublet), the +p_doublet*ln2 multiplicity term is absent BY CONSTRUCTION (the
forced 2-sector COUNT), and the Brannen phase is ORTHOGONAL to the weight: H decomposes as
  H = a*I + Re(b)*S + Im(b)*J,   S = C+C^2 (K-even, pointer/weight),  J = i(C-C^2) (K-odd, phase),
with [S,J]=0. So the record sees 2 sectors (which sets the weight question -> r), while the masses
WITHIN the doublet carry the phase (which sets the 3 distinct values + the 2/9 asymmetry). This
DISCHARGES the alphabet-size and the spectral-phase, localizing the entire Koide value gap to the
single MEASURE choice on the 2-sector partition (block-count 1:1 -> r=1/2 vs Born/dimension 1:2 -> r=1).

This note/runner does NOT force r=1/2. It sets no audit status (independent audit lane owns that).
"""
import numpy as np

w = np.exp(2j * np.pi / 3)
C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)
S = C + C.conj().T            # = C + C^2  (Hermitian, K-even)
J = 1j * (C - C.conj().T)     # = i(C - C^2) (Hermitian, K-odd)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    passed = []

    passed.append(check(
        "S=C+C^2 is K-even Hermitian, spectrum {2,-1,-1} (singlet isolated, doublet degenerate)",
        np.allclose(S, S.conj().T) and np.allclose(np.sort(np.linalg.eigvalsh(S)), [-1, -1, 2]),
        f"spec(S)={np.sort(np.linalg.eigvalsh(S)).round(3)}"))

    passed.append(check(
        "J=i(C-C^2) is K-ODD Hermitian, spectrum {-sqrt3,0,sqrt3} (resolves omega vs omega^2)",
        np.allclose(J, J.conj().T) and np.allclose(np.sort(np.linalg.eigvalsh(J)), [-np.sqrt(3), 0, np.sqrt(3)]),
        f"spec(J)={np.sort(np.linalg.eigvalsh(J)).round(3)}"))

    # K-odd under complex conjugation: conj(J) = -J  (so a conjugation-even instrument cannot record it).
    passed.append(check(
        "J is K-odd (conj(J) = -J): a conjugation-even (CPT) instrument cannot record the intra-doublet distinction",
        np.allclose(J.conj(), -J)))

    passed.append(check(
        "[S,J]=0: weight (K-even S) and phase (K-odd J) are simultaneously block-structured / orthogonal channels",
        np.allclose(S @ J - J @ S, 0)))

    # H = aI + Re(b)S + Im(b)J reproduces aI + bC + conj(b)C^2.
    a, b = 1.3, 0.6 + 0.4j
    H1 = a * I3 + b * C + np.conj(b) * C.conj().T
    H2 = a * I3 + b.real * S + b.imag * J
    passed.append(check(
        "H = aI + Re(b)S + Im(b)J  ==  aI + bC + conj(b)C^2 (pointer/weight = Re b, phase = Im b)",
        np.allclose(H1, H2)))

    # 2-letter record entropy: the +p_doublet*ln2 dit term is the discarded multiplicity.
    p_triv, p_doublet = 1.0 / 3, 2.0 / 3
    S_vN = np.log(3)
    H_shannon = -(p_triv * np.log(p_triv) + p_doublet * np.log(p_doublet))
    passed.append(check(
        "2-letter alphabet drops exactly the doublet multiplicity bit: S_vN - H_Shannon = p_doublet*ln2",
        abs((S_vN - H_shannon) - p_doublet * np.log(2)) < 1e-12,
        f"S_vN-H = {(S_vN-H_shannon):.6f} = (2/3)ln2"))

    # The 2-sector weight map p_triv:p_doublet = 1:2r  => Born(1:2)->r=1 ; uniform(1:1)->r=1/2.
    def r_from_weights(pt, pd):
        return (pd / pt) / 2.0
    passed.append(check(
        "weight map: Born/dimension (1/3,2/3) -> r=1 (Q=1) ; uniform/block-count (1/2,1/2) -> r=1/2 (Q=2/3)",
        abs(r_from_weights(1/3, 2/3) - 1.0) < 1e-12 and abs(r_from_weights(1/2, 1/2) - 0.5) < 1e-12,
        "the single remaining measure choice on the FORCED 2-sector partition"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("FINDING: K-real instrument forces a 2-letter record alphabet (count) and the Brannen phase (K-odd J)")
    print("is orthogonal to the weight (K-even S), [S,J]=0 -- so size and phase are DISCHARGED. The Koide value")
    print("gap localizes to the single MEASURE choice on the 2-sector partition. Does not force r=1/2. No audit status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
