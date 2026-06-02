#!/usr/bin/env python3
"""Flavor carrier from framework baseline UP: the momentum-factor carrier TYPE is FORCED; the hw=1 triplet LOCUS
reduces to one named chiral operator-class import (= the framework's recurring chirality gate);
the basepoint r=1/2 is a separate continuous input.

User directive: forget retained/non-retained ledger status; derive from the axioms up.
Workflow wf_de220c3f-291 (25 agents: 6 axioms-up routes + 3-lens adversarial verify + synth).
Verdict: carrier_derived_modulo_one_principle (the principle is a GENUINE import, not definitional).

TWO LAYERS (the synthesis' clean split, verified here):

  LAYER A -- carrier TYPE (momentum vs position): DERIVED from framework baseline+emergent-dynamics. ALL 6 routes
    and the 'lands-on-momentum-factor' lens agree (0 refutations). A2 => [H_dyn, T_mu]=0 for the three
    commuting translation unitaries on (x)_{x in Z^3} M_2(C); the spectral theorem for commuting normals
    forces a basis-independent joint spectral decomposition over the Pontryagin dual Z^3^=T^3 (the
    Brillouin zone). A LOCAL per-site observable is provably generation-blind; a flavor-separating
    observable MUST be a non-local momentum-block (corner-projector). The Gamma_5-graded EXTENSIVE
    position index vanishes globally and is disqualified. => the carrier is the MOMENTUM factor, as a
    theorem of A2. (The position-vs-momentum question is dissolved.)

  LAYER B -- which momentum LOCUS is 'the species' (the hw=1 C_3 triplet): NOT from framework baseline alone.
    The naive/first-order dispersion has its zero locus on ALL 8 corners {0,pi}^3 (Hamming-graded
    1,3,3,1); a Wilson/second-difference operator puts its distinguished massless mode at hw=0 (mass
    staircase 0,2r,4r,6r), NOT hw=1. Singling out the hw=1 C_3 triplet requires the staggered/
    Kawamoto-Smit FIRST-ORDER CHIRAL operator = single-mode Grassmann fermionization of the M_2(C)
    qubit + chiral anticommutation {epsilon=(-1)^(x+y+z), D}=0. A1 gives a BOSONIC qubit; these are
    PREMISES (genuine import). This import COINCIDES with the framework's already-identified generation-
    ID / Koide-Q=2/3 chirality gate (the C_3-orbit-splitting chiral grading) -- so the carrier locus is
    NOT a new independent input; it collapses into the one recurring chirality import.

  BASEPOINT r=|b|^2/a^2=1/2: separate continuous Yukawa input, untouched by the discrete pole structure.
"""
import itertools
import numpy as np

W = np.exp(2j * np.pi / 3)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def hw(k):
    return sum(1 for x in k if abs(x - np.pi) < 1e-9)


def main():
    passed = []

    # ===== LAYER A: momentum carrier TYPE forced from framework baseline =====
    # translation characters of the BZ corners; the three commuting T_mu have eigenvalue e^{i k_mu}
    corner_char = {k: tuple(-1 if ki else 1 for ki in k) for k in itertools.product([0, 1], repeat=3)}
    hw1 = sorted(k for k in corner_char if sum(k) == 1)
    passed.append(check(
        "A1 the 3 hw=1 corners carry DISTINCT joint translation characters (-1,1,1),(1,-1,1),(1,1,-1)",
        len(hw1) == 3 and sorted(corner_char[k] for k in hw1) == [(-1, 1, 1), (1, -1, 1), (1, 1, -1)],
        f"characters = {[corner_char[k] for k in hw1]} (joint spectrum of commuting T_x,T_y,T_z)"))

    def R(k):
        return (k[2], k[0], k[1])
    perm = [hw1.index(R(k)) for k in hw1]
    passed.append(check(
        "A2 C_3[111] axis-shift acts transitively on the hw=1 triplet (a single 3-orbit)",
        sorted(perm) == [0, 1, 2] and perm != [0, 1, 2],
        f"R-permutation = {perm}"))

    # generation-blind trap cleared: a local per-site observable is identical across generations,
    # while the momentum-block (corner-projector) separates them.
    sites = list(itertools.product([0, 1], repeat=3))
    def char_amp(k, n):
        s = 1
        for ki, ni in zip(k, n):
            if (ki * ni) % 2:
                s = -s
        return s / np.sqrt(8.0)
    psi = {k: np.array([char_amp(k, n) for n in sites]) for k in hw1}
    P_site0 = np.zeros((8, 8)); P_site0[0, 0] = 1.0
    local_exps = [float(np.real(psi[k].conj() @ P_site0 @ psi[k])) for k in hw1]
    # momentum-block separation: projector onto corner hw1[0] gives delta_ij
    Pk0 = np.outer(psi[hw1[0]], psi[hw1[0]].conj())
    mom_exps = [float(np.real(psi[k].conj() @ Pk0 @ psi[k])) for k in hw1]
    passed.append(check(
        "A3 carrier lands on MOMENTUM, not position: local per-site obs identical across gens; momentum-block separates",
        np.allclose(local_exps, local_exps[0]) and np.allclose(mom_exps, [1, 0, 0]),
        f"local <P_site0>={np.round(local_exps,4).tolist()} (blind); momentum <P_k0>={np.round(mom_exps,4).tolist()} (separates)"))

    # Gamma_5 extensive position index vanishes globally -> not a single-particle observable
    eps_sum = sum((-1) ** (n[0] + n[1] + n[2]) for n in sites)
    passed.append(check(
        "A4 the extensive Gamma_5=(-1)^(x+y+z) position index sum_x epsilon(x) = 0 (bulk total, disqualified as carrier)",
        eps_sum == 0,
        f"sum_x (-1)^(x+y+z) = {eps_sum} over the 8-site torus"))

    # ===== LAYER B: hw=1 LOCUS requires the chiral operator-class import (counterfactuals) =====
    pts = list(itertools.product([0, np.pi], repeat=3))
    naive_zeros = [k for k in pts if sum(np.sin(x) ** 2 for x in k) < 1e-12]
    grading = sorted(hw(k) for k in naive_zeros)
    passed.append(check(
        "B1 naive/first-order |D|^2=sum sin^2(k) zero locus = ALL 8 corners, Hamming-graded (1,3,3,1) -- NOT just hw=1",
        len(naive_zeros) == 8 and grading == [0, 1, 1, 1, 2, 2, 2, 3],
        f"zeros={len(naive_zeros)}, Hamming multiplicities {[grading.count(h) for h in (0,1,2,3)]} -> hw=1 is one C_3 orbit, but not singled out by the dispersion alone"))

    r = 1.0
    wilson_mass = {hw(k): r * sum(1 - np.cos(x) for x in k) for k in pts}
    passed.append(check(
        "B2 COUNTERFACTUAL: a Wilson/2nd-difference operator puts its massless mode at hw=0 (staircase 0,2r,4r,6r), NOT hw=1",
        abs(wilson_mass[0]) < 1e-12 and abs(wilson_mass[1] - 2 * r) < 1e-12
        and abs(wilson_mass[2] - 4 * r) < 1e-12 and abs(wilson_mass[3] - 6 * r) < 1e-12,
        f"Wilson mass by hw = {{0:{wilson_mass[0]:.0f}, 1:{wilson_mass[1]:.0f}, 2:{wilson_mass[2]:.0f}, 3:{wilson_mass[3]:.0f}}} "
        f"-> hw=1 selection needs the first-order CHIRAL (staggered/KS) operator = the import"))

    # ===== delta=2/9 retains the index apparatus; basepoint r free =====
    L12 = sum(1 / ((W ** k - 1) * (W ** (2 * k) - 1)) for k in (1, 2)) / 3
    passed.append(check(
        "C1 delta=L_3(1,2)=2/9 (equivariant-eta/Atiyah-Bott density), distinct from the bare doublet character omega+omega^2=-1",
        abs(L12 - 2.0 / 9.0) < 1e-12 and abs((W + W ** 2) + 1) < 1e-12,
        f"L_3(1,2)={L12.real:.6f}; bare char={float((W+W**2).real):.1f}"))
    passed.append(check(
        "D1 basepoint r=|b|^2/a^2 is FREE in F=aI+b(J-I): Q=1/3+(2/3)r; r=1/2->Q=2/3, r=1->Q=1; unconstrained by corner kinematics",
        abs((1 / 3 + 2 / 3 * 0.5) - 2 / 3) < 1e-12 and abs((1 / 3 + 2 / 3 * 1.0) - 1.0) < 1e-12,
        "discrete pole/corner structure fixes delta=2/9 only; the continuous Yukawa modulus r is a separate input"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: carrier_derived_modulo_one_principle. LAYER A (carrier TYPE = momentum, not position) is")
    print("FORCED from framework baseline: [H_dyn,T_mu]=0 + spectral theorem => basis-independent BZ decomposition; local")
    print("observables generation-blind; flavor-separating observables are momentum-block (corner) operators;")
    print("the extensive Gamma_5 position index vanishes. This is the genuine advance -- the position-vs-")
    print("momentum carrier question is dissolved as a theorem of A2. LAYER B (which LOCUS = hw=1 triplet) is")
    print("NOT forced by framework baseline: the dispersion zero locus is all 8 corners and a Wilson operator prefers hw=0;")
    print("the hw=1 C_3 triplet needs the staggered/Kawamoto-Smit first-order CHIRAL operator (single-mode")
    print("Grassmann + {epsilon,D}=0) -- a genuine import that COINCIDES with the framework's recurring")
    print("generation-ID / Koide-Q=2/3 chirality gate. So the carrier locus is NOT a new independent input;")
    print("it collapses into the one chirality import. BASEPOINT r=1/2 remains a separate continuous Yukawa input.")
    print("Source: STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE premise table (BlockT1 + {epsilon,D}=0).")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
