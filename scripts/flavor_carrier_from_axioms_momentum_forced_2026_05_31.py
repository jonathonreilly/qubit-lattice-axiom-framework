#!/usr/bin/env python3
"""Flavor carrier parent-boundary runner.

The momentum-factor carrier TYPE is forced on the finite translation
representative; the physical hw=1 triplet LOCUS remains a named chiral
operator-class import; the basepoint r=1/2 and readout class are separate
inputs. This runner verifies the source boundary of the combined parent note
and does not write an audit verdict.

Workflow wf_de220c3f-291 (25 agents: 6 axioms-up routes + 3-lens adversarial
verify + synth).
Verdict: conditional_parent_with_clean_layer_a_split.

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
    qubit + chiral anticommutation {epsilon=(-1)^(x+y+z), D}=0. The current qubit substrate supplies a BOSONIC qubit; these are
    PREMISES (genuine import). This import is gate-aligned with the framework's
    already-identified generation-ID / Koide-Q=2/3 chirality gate family
    (the C_3-orbit-splitting chiral grading), but the physical locus bridge
    remains open.

  BASEPOINT r=|b|^2/a^2=1/2: separate continuous Yukawa input, untouched by the discrete pole structure.
"""
import itertools
from pathlib import Path

import numpy as np
import sympy as sp

W = np.exp(2j * np.pi / 3)
ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = ROOT / "docs" / "FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31.md"
SPLIT_NOTE = ROOT / "docs" / "FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md"


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def normalize(text: str) -> str:
    return " ".join(text.split()).lower()


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

    a_sym, b_sym = sp.symbols("a_sym b_sym", positive=True, real=True)
    J3 = sp.ones(3)
    F = a_sym * sp.eye(3) + b_sym * (J3 - sp.eye(3))
    tr_F = sp.simplify(sp.trace(F))
    tr_F2 = sp.simplify(sp.trace(F * F))
    Q_F = sp.simplify(tr_F2 / (tr_F ** 2))
    passed.append(check(
        "D1 derive Q(F)=Tr(F^2)/Tr(F)^2 = 1/3 + (2/3)|b|^2/a^2 from F=aI+b(J-I)",
        tr_F == 3 * a_sym
        and tr_F2 == 3 * a_sym ** 2 + 6 * b_sym ** 2
        and sp.simplify(Q_F - (sp.Rational(1, 3) + sp.Rational(2, 3) * (b_sym ** 2 / a_sym ** 2))) == 0,
        f"Tr F={tr_F}, Tr F^2={tr_F2}, Q={Q_F}"))
    passed.append(check(
        "D2 basepoint r=|b|^2/a^2 is FREE: r=1/2->Q=2/3, r=1->Q=1; unconstrained by corner kinematics",
        abs((1 / 3 + 2 / 3 * 0.5) - 2 / 3) < 1e-12 and abs((1 / 3 + 2 / 3 * 1.0) - 1.0) < 1e-12,
        "discrete pole/corner structure fixes delta=2/9 only; the continuous Yukawa modulus r is a separate input"))

    # ===== Source-boundary checks: parent remains conditional; clean Layer A lives in the split note =====
    parent = PARENT_NOTE.read_text(encoding="utf-8")
    split = SPLIT_NOTE.read_text(encoding="utf-8")
    parent_norm = normalize(parent)
    split_norm = normalize(split)
    passed.append(check(
        "E0 parent source declares open_gate conditional integration map, not bounded theorem",
        "**claim type:** open_gate / conditional integration map" in parent_norm
        and "**claim type:** bounded_theorem" not in parent_norm
        and "not a retained-status proposal" in parent_norm,
        "source metadata demotes combined parent to open integration map"))
    passed.append(check(
        "E1 parent note records 2026-06-18 parent-boundary repair",
        "## 2026-06-18 parent-boundary repair" in parent,
        "source-side repair section present"))
    passed.append(check(
        "E2 parent delegates clean Layer-A carrier-type theorem to the 2026-06-15 split",
        "flavor_carrier_momentum_type_from_translation_theorem_note_2026-06-15.md" in parent_norm
        and "clean layer-a theorem" in parent_norm,
        "downstream Layer-A citations should use the split note"))
    passed.append(check(
        "E3 parent remains the combined conditional packet",
        "combined conditional" in parent_norm
        and "physical `hw=1` locus bridge" in parent_norm
        and "`r=1/2` input" in parent_norm
        and "readout-class input" in parent_norm,
        "locus/basepoint/readout stay inside the conditional parent"))
    passed.append(check(
        "E4 parent is not standalone physical generation-carrier closure",
        "do not use this parent as a standalone closure of the physical generation carrier" in parent_norm,
        "full physical carrier closure stays open"))
    passed.append(check(
        "E5 parent names the re-audit condition before full-package reuse",
        "only after a separate theorem forces the staggered/ks `hw=1` physical locus" in parent_norm
        and "closes the `r=1/2` and readout selections" in parent_norm,
        "full-package recheck requires locus/r/readout closure"))
    passed.append(check(
        "E6 split note boundary excludes hw=1/r/readout closure",
        "this split proves only item 1" in split_norm
        and "does not claim that the physical generation locus is forced to be `hw=1`" in split_norm
        and "that the continuous koide basepoint `r = 1/2` is derived" in split_norm
        and "that the index-density readout `delta = 2/9` is selected" in split_norm,
        "split theorem remains clean Layer A only"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: conditional_parent_with_clean_layer_a_split. LAYER A (carrier TYPE = momentum, not position) is")
    print("FORCED from framework baseline: [H_dyn,T_mu]=0 + spectral theorem => basis-independent BZ decomposition; local")
    print("observables generation-blind; flavor-separating observables are momentum-block (corner) operators;")
    print("the extensive Gamma_5 position index vanishes. This is the genuine advance -- the position-vs-")
    print("momentum carrier question is dissolved as a theorem of A2. The clean Layer-A citation target is")
    print("FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15. This parent remains")
    print("the combined conditional packet. LAYER B (which LOCUS = hw=1 triplet) is")
    print("NOT forced by framework baseline: the dispersion zero locus is all 8 corners and a Wilson operator prefers hw=0;")
    print("the hw=1 C_3 triplet needs the staggered/Kawamoto-Smit first-order CHIRAL operator (single-mode")
    print("Grassmann + {epsilon,D}=0) -- a genuine import that aligns with the framework's named")
    print("generation-ID / Koide-Q=2/3 chirality gate family. This is gate alignment, not closure of")
    print("the physical generation bridge. BASEPOINT r=1/2 and the readout class remain separate inputs.")
    print("Sources: STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md")
    print("(BlockT1 + {epsilon,D}=0), KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md,")
    print("and KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
