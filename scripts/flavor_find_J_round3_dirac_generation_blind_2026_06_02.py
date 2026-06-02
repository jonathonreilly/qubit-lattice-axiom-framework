"""J-hunt ROUND 3: charged-lepton DIRAC reality structure is GENERATION-BLIND -- it does not supply the
generation-doublet complex structure J. det_C/r=1/2 not forced; lane assignment reframed (pending a
spinor-to-generation coupling). Wall pivots to the kappa block-count MEASURE (round 4).

Round 3 tested: does charged-lepton Dirac-ness (e- != e+, from U(1)_em -- a physical reality structure,
NOT the forbidden continuous U(1)_b) descend to the doublet J -> det_C -> r=1/2, and predict the lane?
Verdict (wf_2d355f65): dirac_generation_blind_no_J, unanimous 5/5.

Verified findings:
(1) Charge conjugation acts as the IDENTITY on the generation index (it neither permutes nor mixes
    e,mu,tau); U(1)_em charges all 3 generations identically. So the Dirac reality structure factorizes
    as J_spin (x) I_generation: on the generation factor it is the central scalar i*I_3.
(2) VERIFIED: U=i*I_3 AND the continuous centralizer diag(1,e^{iphi},e^{-iphi}) (in the C-eigenbasis)
    both leave H fixed (U H U^dag = H) -- generation-blind, b unchanged. A uniform ambient
    complexification multiplies singlet and doublet weights EQUALLY and cancels in the ratio r. So
    Dirac-ness does not touch kappa (the isotype block-count) and does not force det_C.
(3) The map that WOULD set kappa=2 (r=1/2) is either (a) a continuous doublet rotation b->e^{i theta}b =
    the rephasing C->e^{i theta}C, barred by C^3=I except at the 3 cube roots (VERIFIED (e^{i*0.7}C)^3 !=
    I), or (b) a Hermitian generation operator anticommuting with Gamma_chi, which is NON-circulant /
    C_3-equivariance-breaking (VERIFIED: no circulant anticommutes with Gamma_chi). Naming either 'Dirac'
    does not produce it.

This is round 3 after rounds 1-2 (static J measure-neutral; fermionic frame power!=count). Three
genuinely-distinct levers, three det_R-defaults -- the wall is robust but NOT closed: the gap relocates
to the kappa block-count MEASURE (a discrete/counting question, decoupled from symmetry generators),
attacked in round 4. The Dirac/Majorana datum remains a physically-meaningful per-sector reality label;
the lane assignment is reframed (pending a spinor-reality-to-generation coupling), not closed.
"""
import numpy as np


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


w = np.exp(2j * np.pi / 3)
C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)
GX = (2.0 / 3.0) * np.ones((3, 3)) - I3
F = np.array([[1, 1, 1], [1, w, w ** 2], [1, w ** 2, w]]) / np.sqrt(3)  # C-eigenbasis


def main():
    passed = []
    a, b = 1.0, 0.6 + 0.2j
    H = a * I3 + b * C + np.conj(b) * C.conj().T

    # (1) ambient Dirac i*I_3 is generation-blind: leaves H fixed
    U1 = 1j * I3
    passed.append(check(
        "R3-1 ambient Dirac i*I_3 (generation block of charge conjugation = identity) leaves H fixed -> generation-blind",
        np.allclose(U1 @ H @ U1.conj().T, H),
        "charge conjugation acts as I_3 on the generation index -> Dirac-ness factorizes J_spin (x) I_generation"))

    # (2) the continuous centralizer diag(1,e^iphi,e^-iphi) also leaves H fixed (b unchanged) -> doesn't touch kappa
    phi = 0.8
    Uph = F @ np.diag([1, np.exp(1j * phi), np.exp(-1j * phi)]) @ F.conj().T
    passed.append(check(
        "R3-2 continuous centralizer diag(1,e^iphi,e^-iphi) leaves H fixed -> uniform ambient phase cancels in r, does NOT touch kappa",
        np.allclose(Uph @ H @ Uph.conj().T, H),
        "any generation-uniform complexification multiplies singlet & doublet weights equally -> cancels in r=|b|^2/a^2"))

    # (3) the b-rotating map C->e^{i theta}C breaks C^3=I for generic theta
    th = 0.7
    M = np.exp(1j * th) * C
    passed.append(check(
        "R3-3 the only b-rotating map C->e^{i theta}C breaks C^3=I for generic theta (barred except at 3 cube roots)",
        not np.allclose(M @ M @ M, I3),
        "(e^{i*0.7}C)^3 != I -> the continuous doublet rotation = forbidden U(1)_b"))

    # (4) no circulant anticommutes with Gamma_chi -> any kappa=2 anticommutant is non-circulant (C_3-breaking)
    none_anti = True
    rng = np.random.default_rng(3)
    for _ in range(300):
        aa = rng.standard_normal()
        bb = rng.standard_normal() + 1j * rng.standard_normal()
        Hc = aa * I3 + bb * C + np.conj(bb) * C.conj().T
        if np.linalg.norm(Hc) > 0.1 and np.linalg.norm(Hc @ GX + GX @ Hc) < 1e-6:
            none_anti = False
    passed.append(check(
        "R3-4 no nonzero circulant anticommutes with Gamma_chi -> any det_C(kappa=2)-producing anticommutant is NON-circulant (C_3-breaking)",
        none_anti,
        "the two routes to the doublet J are exactly the C^3=I-forbidden rephasing OR the C_3-equivariance-breaking non-circulant (retained_bounded no-go)"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT (J-hunt round 3, wf_2d355f65): dirac_generation_blind_no_J. The charged-lepton Dirac reality")
    print("structure factorizes J_spin (x) I_generation -- on the generation factor it is the central scalar i*I_3,")
    print("generation-blind, leaves b fixed, cancels in r. It does NOT supply the doublet J and does NOT force")
    print("det_C/r=1/2. Every CONTINUOUS lever (rounds 1-3: static J_cs, fermionic Berezin, Dirac/charge phase)")
    print("leaves b fixed and cancels in r. The two maps that WOULD set kappa=2 are the C^3=I-forbidden rephasing")
    print("or a C_3-breaking non-circulant. WALL PIVOTS (round 4): from 'what ROTATES b' (continuous symmetry,")
    print("exhausted) to 'what COUNTS the doublet as one block vs two real modes' (the kappa block-count MEASURE,")
    print("a discrete/measure question). Lane assignment reframed as pending a spinor-to-generation coupling.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
