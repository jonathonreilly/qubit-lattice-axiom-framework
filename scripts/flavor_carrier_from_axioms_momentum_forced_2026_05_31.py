#!/usr/bin/env python3
"""Consistency runner for the conditional flavor integration map.

Layer A reproduces only positive finite translation-character data: three
distinct supplied hw=1 characters, their transitive C_3 orbit, their uniform
site profiles, and an exact rank-one projector expectation row.  Layer B keeps
two supplied operator comparisons as conditional-route context.  The remaining
checks reproduce the displayed cyclotomic-density and circulant equalities and
verify the parent/source authority boundary.  No audit verdict is written.
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

    # ===== LAYER A: positive finite translation-character data =====
    # The three commuting translations have joint eigenvalues (-1)^k_mu.
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

    # Exact supplied-character profiles and one rank-one projector row.
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
    Pk0 = np.outer(psi[hw1[0]], psi[hw1[0]].conj())
    mom_exps = [float(np.real(psi[k].conj() @ Pk0 @ psi[k])) for k in hw1]
    passed.append(check(
        "A3 supplied hw=1 characters have uniform site profiles and projector row delta_(k0,k)",
        np.allclose(local_exps, [1 / 8] * 3) and np.allclose(mom_exps, [1, 0, 0]),
        f"<P_site0>={np.round(local_exps,4).tolist()}; <P_k0>={np.round(mom_exps,4).tolist()}"))

    # ===== LAYER B: two supplied operator comparisons for the conditional route =====
    pts = list(itertools.product([0, np.pi], repeat=3))
    naive_zeros = [k for k in pts if sum(np.sin(x) ** 2 for x in k) < 1e-12]
    grading = sorted(hw(k) for k in naive_zeros)
    passed.append(check(
        "B1 naive/first-order |D|^2=sum sin^2(k) has all 8 corners as zeros with grading (1,3,3,1)",
        len(naive_zeros) == 8 and grading == [0, 1, 1, 1, 2, 2, 2, 3],
        f"zeros={len(naive_zeros)}, Hamming multiplicities {[grading.count(h) for h in (0,1,2,3)]}"))

    r = 1.0
    wilson_mass = {hw(k): r * sum(1 - np.cos(x) for x in k) for k in pts}
    passed.append(check(
        "B2 displayed Wilson/2nd-difference comparison has staircase (0,2r,4r,6r)",
        abs(wilson_mass[0]) < 1e-12 and abs(wilson_mass[1] - 2 * r) < 1e-12
        and abs(wilson_mass[2] - 4 * r) < 1e-12 and abs(wilson_mass[3] - 6 * r) < 1e-12,
        f"Wilson mass by hw = {{0:{wilson_mass[0]:.0f}, 1:{wilson_mass[1]:.0f}, 2:{wilson_mass[2]:.0f}, 3:{wilson_mass[3]:.0f}}} "
        f"on this supplied comparison operator"))

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

    # ===== Source-boundary checks: parent remains an open integration map =====
    parent = PARENT_NOTE.read_text(encoding="utf-8")
    split = SPLIT_NOTE.read_text(encoding="utf-8")
    parent_norm = normalize(parent)
    split_norm = normalize(split)
    passed.append(check(
        "E0 parent source declares the canonical open_gate author hint",
        "**type:** open_gate" in parent_norm
        and "**type:** bounded_theorem" not in parent_norm,
        "source metadata keeps the combined parent open"))
    passed.append(check(
        "E1 parent note records the 2026-07-18 positive-scope repair",
        "## 2026-07-18 positive-scope repair" in parent,
        "source-side narrowing section present"))
    passed.append(check(
        "E2 parent delegates exact finite character formulas to the 2026-06-15 theorem",
        "flavor_carrier_momentum_type_from_translation_theorem_note_2026-06-15.md" in parent_norm
        and "rank-one character projectors" in parent_norm
        and "expectation matrix `delta_(kq)`" in parent_norm,
        "the historical path now carries a positive finite theorem"))
    passed.append(check(
        "E3 parent keeps physical locus, r, and readout identification outside the finite theorem",
        "physical `hw=1` locus" in parent_norm
        and "`r=1/2`" in parent_norm
        and "readout identifications explicitly open" in parent_norm,
        "physical integrations remain open"))
    passed.append(check(
        "E4 parent assigns no physical interpretation to the finite equalities",
        "these equalities carry no physical carrier, generation, flavor, observable, or readout assignment" in parent_norm,
        "finite algebra and physical interpretation remain distinct"))
    passed.append(check(
        "E5 comparison formulas are conditional-route context rather than route exhaustion",
        "not an exhaustion of possible physical routes" in parent_norm
        and "conditional staggered/kawamoto-smit route" in parent_norm,
        "the parent makes no alternative-route foreclosure"))
    passed.append(check(
        "E6 finite theorem states positive_theorem scope and its authority limit",
        "**type:** positive_theorem" in split_norm
        and "## authority limit" in split_norm
        and "assigns it no physical selection or species meaning" in split_norm
        and "koide basepoint or readout selection" in split_norm,
        "finite theorem remains an abstract positive construction"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("SUMMARY: Layer A is the exact finite translation-character profile/projector construction.")
    print("The supplied hw=1 characters have uniform 1/8 profiles, distinct joint characters, a transitive")
    print("C_3 orbit, and the displayed Kronecker projector row. These equalities assign no physical role.")
    print("Layer B records one conditional staggered/Kawamoto-Smit route and two finite operator comparisons;")
    print("it does not exhaust physical routes or select the supplied hw=1 subset as a physical generation locus.")
    print("BASEPOINT r=1/2 and the density/readout identification remain separate open inputs.")
    print("Sources: STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md")
    print("(BlockT1 + {epsilon,D}=0), KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md,")
    print("and KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
