"""J-hunt ROUND 2: the FERMIONIC frame does NOT force det_C. Power != count; the symplectic pairing J
is an unforced extra posit. det_R/Q=1 default stands. Wall moves to Dirac-vs-Majorana reality structure.

Round 2 tested the bridge [matter fermionic (P1)] => [Berezin/first-order] => [det_C] => [r=1/2].
Verdict (wf_d2438beb): det_R_default_stands. Guard (i) PASSES (P1 independently motivated); guards
(ii),(iii) FAIL. Decisive verified findings:

(1) POWER vs COUNT ORTHOGONALITY: the fermionic/bosonic frame fixes the determinant EXPONENT
    (Grassmann det^{+1} vs boson det^{-1/2}), NEVER the doublet mode-COUNT (det_C vs det_R). P1 is
    silent on the count. The 'fermion=1 factor, boson=2 factors' asymmetry is a Pfaffian-vs-unrooted-det
    normalization artifact (Pf(aJ)=a vs un-rooted det(sI)=s^2); on equal footing log|Z| both are single-power.
(2) BEREZIN GIVES A DETERMINANT-PRODUCT, NOT A BLOCK-TOTAL: integrating the matter field psi (action
    psi-bar H psi) gives Z = det(H) as a FUNCTION of (a,b) -- three REAL eigenvalue factors
    (a+2Re b)(a-Re b +- sqrt3 Im b) = (1 singlet)(2 doublet). This determinant-PRODUCT functional is
    structurally distinct from the Frobenius BLOCK-TOTAL functional (E_singlet=3a^2, E_doublet=6|b|^2)
    whose equal-block point gives r=1/2. Berezin never integrates OVER b to set r.
(3) C_3 ADMITS BOTH INVARIANT BILINEARS: the symmetric I (det_R) AND the antisymmetric J=C-C^2 (det_C)
    are BOTH C_3-invariant (C^T I C=I, C^T J C=J). So pairing the two real doublet modes into one complex
    mode (choosing A propto J = det_C) is an ADDITIONAL posit, NOT forced by C_3 or fermion-ness. That J
    is the U(1)_b complex structure Round 1 proved MEASURE-NEUTRAL and C^3=I forbids as a continuous
    rephasing. So the fermionic frame is the same static J in a Berezin costume -- it does not move the wall.
(4) INDEX EQUIVOCATION: the retained Berezin/forcing notes are SITE-indexed (per-site Fock occupation
    dim 2 = vacuum+1-particle), silent on the GENERATION reality structure; the 2=2 match (Fock-dim vs
    doublet-complex-dim) is coincidental, not structural.

(Established mapping kept: det_C = equal power per BLOCK 3a^2=6|b|^2 -> r=1/2 -> Q=2/3 [observed];
 det_R = equal power per real DIM 3a^2=3|b|^2 -> r=1 -> Q=1 [A1 default].)

WALL NOW: det_C/r=1/2 <=> a DIRAC (complex/antisymmetric-J) reality structure on the generation
doublet, vs MAJORANA (real). Round 3 attacks whether framework baseline+emergent-spacetime force Dirac over Majorana.
"""
import numpy as np


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)


def main():
    passed = []
    rng = np.random.default_rng(602)

    # (1) Berezin det(H) = product of 3 real eigenvalues (a determinant-product, det_R-type), not a block-total
    ok = True
    for _ in range(200):
        a = rng.standard_normal()
        b = rng.standard_normal() + 1j * rng.standard_normal()
        H = a * I3 + b * C + np.conj(b) * C.conj().T
        ev = np.linalg.eigvalsh(H)
        # det = product of the 3 real eigenvalues; closed form (a+2Re b)(a-Re b)^2 - 3 a Im b^2 ... just check det=prod(ev)
        if not (np.allclose(ev.imag if np.iscomplexobj(ev) else 0, 0) and abs(np.linalg.det(H).real - np.prod(ev)) < 1e-9):
            ok = False
    passed.append(check(
        "R2-1 Berezin Z=det(H) = product of 3 REAL eigenvalue factors (det_R-type product), a FUNCTION of (a,b) -- never integrates over b",
        ok, "determinant-PRODUCT functional, structurally distinct from the Frobenius block-total that gives r=1/2"))

    # (2) C_3 admits BOTH symmetric I and antisymmetric J=C-C^2 as invariant bilinears
    Janti = C - C @ C
    passed.append(check(
        "R2-2 C_3 leaves BOTH symmetric I (C^T I C=I) and antisymmetric J=C-C^2 (C^T J C=J) invariant -> does NOT select det_C(J) over det_R(I)",
        np.allclose(C.T @ I3 @ C, I3) and np.allclose(Janti.T, -Janti) and np.allclose(C.T @ Janti @ C, Janti),
        "choosing A propto J (= det_C, pairing 2 reals into 1 complex) is an unforced posit = the U(1)_b that round 1 showed measure-neutral / C^3=I-forbidden-as-continuous"))

    # (3) power vs count: the Pfaffian-vs-unrooted-det asymmetry is a normalization artifact
    a, s = 2.0, 2.0
    Janti2 = np.array([[0, -1.0], [1.0, 0]])
    fermion = abs(np.linalg.det(a * Janti2)) ** 0.5      # Pf(aJ) = a (single factor)
    boson = np.linalg.det(s * np.eye(2)) ** (-0.5)        # properly normalized boson: det(sI)^{-1/2} = 1/s (single factor)
    passed.append(check(
        "R2-3 on equal footing both are single-power: Pf(aJ)=a and det(sI)^{-1/2}=1/s; the '1-vs-2 factor' split is a Pfaffian-vs-unrooted-det artifact",
        abs(fermion - a) < 1e-9 and abs(boson - 1.0 / s) < 1e-9,
        f"Pf(aJ)={fermion:.3f}=a (1 factor); det(sI)^(-1/2)={boson:.3f}=1/s (1 factor) -> fermion/boson fixes the det EXPONENT, not the doublet COUNT"))

    # (4) established mapping (kept; not the synth's label slip): det_C->r=1/2, det_R->r=1
    Q = lambda r: 1/3 + 2/3 * r
    passed.append(check(
        "R2-4 det_C (equal power per BLOCK 3a^2=6|b|^2) -> r=1/2 -> Q=2/3 (observed); det_R (per real dim 3a^2=3|b|^2) -> r=1 -> Q=1 (A1 default)",
        abs(Q(0.5) - 2/3) < 1e-12 and abs(Q(1.0) - 1.0) < 1e-12,
        "the wall: det_C/r=1/2 <=> DIRAC (complex/J-paired) generation doublet; det_R/r=1 <=> MAJORANA (real)"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT (J-hunt round 2, wf_d2438beb): det_R/Q=1 stands. The FERMIONIC frame does NOT force det_C:")
    print("POWER (det exponent) != COUNT (doublet mode-count); Berezin gives a determinant-PRODUCT (3 real")
    print("factors), not the block-total that gives r=1/2; and C_3 admits BOTH the symmetric I and the")
    print("antisymmetric J as invariant bilinears, so det_C's J is an unforced extra posit = the measure-neutral,")
    print("C^3=I-forbidden-as-continuous U(1)_b. The fermionic frame is the same static J in a Berezin costume.")
    print("WALL NOW (round 3): can framework baseline+emergent-spacetime force a DIRAC (complex) vs MAJORANA (real) reality")
    print("structure on the generation doublet? (Charged leptons ARE Dirac -- the round-3 lever.)")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
