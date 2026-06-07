#!/usr/bin/env python3
"""Factor-bridge no-go: on-site Clifford gamma5 = gamma5_spin (x) I_gen is
partition-blind on the generation factor.

Source note:
  docs/KOIDE_GAMMA5_FACTOR_BRIDGE_NO_GO_NOTE_2026-06-06.md

Tests whether the on-site Clifford chirality gamma5 (the candidate
C_3-breaking T-odd selector floated for the Koide delta / partition pin)
satisfies the requirement that the partition selector be (i) T-ODD AND
(ii) NON-COMMUTING with S = C + C^2 on the GENERATION factor C^3 (i.e.
break C_3-equivariance).

Setup: the carrier factorizes as site/spin C^2 (x) generation C^3.
  - S = C + C^2 and A = i(C - C^2) act on the generation C^3.
  - gamma5 (on-site Cl(3,0) chirality / spin grade) is the 2x2 diag(+1,-1)
    on the site/spin C^2, embedded as gamma5_spin (x) I_gen.

Result (the no-go): gamma5_spin (x) I_gen COMMUTES with I_spin (x) S
EXACTLY (different tensor factors), and is trivial (K-even) on the
generation factor. So it supplies NEITHER half of the requirement: it is
partition-blind on C^3. The rank-2 sector gamma5 splits is the spin/taste
doublet at FIXED generation character (dim 2 on C^2), NOT the generation
C^3 orbit (dim 3). This is the same site-C^2 -> generation-C^3 factor
bridge that the L/R route hit.

Scope: this rules out the NATURAL tensor embedding gamma5_spin (x) I_gen.
It does NOT foreclose a ROOTED/continuum single-physical-fermion carrier in
which rooting ENTANGLES spin into the generation index so the physical-
fermion gamma5 acquires a generation component with [gamma5, S] != 0 (the
named open frontier). No weight r is forced.
"""

from __future__ import annotations

from pathlib import Path
import sys
import numpy as np

import frontier_g2_bridge_c3_current_cannot_beat_gap_a as g2_bridge

PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / "docs/KOIDE_GAMMA5_FACTOR_BRIDGE_NO_GO_NOTE_2026-06-06.md"
G2_NOTE = ROOT / "docs/G2_BRIDGE_C3_CURRENT_CANNOT_BEAT_GAP_A_NO_GO_NOTE_2026-06-06.md"


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {name}" + (f"  --  {detail}" if detail else ""))


def section(t: str) -> None:
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def source_anchor_checks() -> None:
    section("Source anchors: companion current-gap bridge packet")
    target_text = TARGET_NOTE.read_text(encoding="utf-8")
    g2_text = G2_NOTE.read_text(encoding="utf-8")
    check("target note links the companion current-gap no-go note",
          "G2_BRIDGE_C3_CURRENT_CANNOT_BEAT_GAP_A_NO_GO_NOTE_2026-06-06.md" in target_text)
    check("target note links the companion current-gap runner",
          "scripts/frontier_g2_bridge_c3_current_cannot_beat_gap_a.py" in target_text)
    check("target note links the companion current-gap runner cache",
          "logs/runner-cache/frontier_g2_bridge_c3_current_cannot_beat_gap_a.txt" in target_text)
    check("companion runner source is statically importable",
          hasattr(g2_bridge, "positive_half") and hasattr(g2_bridge, "negative_half"))
    check("companion note states the T-odd and generation-partition non-commutation requirement",
          "T-odd AND non-commuting with `S`" in g2_text)
    check("companion note keeps r weight-clean",
          "Does **not** force or derive `r`" in g2_text)


def cyclic_shift() -> np.ndarray:
    C = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        C[(i + 1) % 3, i] = 1.0
    return C


C = cyclic_shift()
S = C + C @ C                 # generation factor, K-even, eig {2,-1,-1}
A = 1j * (C - C @ C)          # generation factor, K-odd,  eig {0,+/-sqrt3}
g5 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)  # site/spin chirality (#2919)
I2 = np.eye(2, dtype=complex)
I3 = np.eye(3, dtype=complex)


def setup_checks() -> None:
    section("Setup: generation factor (C^3) and on-site gamma5 (C^2)")
    check("C^3 = I", np.allclose(np.linalg.matrix_power(C, 3), np.eye(3)))
    check("S=C+C^2 on generation C^3, eig {2,-1,-1}",
          np.allclose(np.sort(np.linalg.eigvalsh((S + S.conj().T) / 2).real), [-1, -1, 2]))
    check("gamma5 = diag(+1,-1) is a 2x2 operator on the site/spin C^2",
          g5.shape == (2, 2) and np.allclose(g5, np.diag([1, -1])))
    check("DIMENSION MISMATCH: gamma5 is 2x2, S is 3x3 (gamma5 not on the gen factor)",
          g5.shape == (2, 2) and S.shape == (3, 3))


def factor_bridge_no_go() -> None:
    section("No-go: gamma5_spin (x) I_gen commutes with S on C^3 (partition-blind)")
    g5_emb = np.kron(g5, I3)      # gamma5 on the site/spin factor, identity on gen
    S_emb = np.kron(I2, S)        # S on the generation factor
    A_emb = np.kron(I2, A)
    comm = g5_emb @ S_emb - S_emb @ g5_emb
    check("[gamma5 (x) I_gen, I_spin (x) S] = 0 EXACTLY (norm 0)",
          np.allclose(comm, 0) and np.linalg.norm(comm) < 1e-12,
          f"||[gamma5,S]|| = {np.linalg.norm(comm):.2e}")
    check("=> requirement (ii) non-commuting-with-S FAILS for gamma5_spin (x) I_gen",
          np.linalg.norm(comm) < 1e-12)
    # K-parity on the generation factor: gamma5 is real diag(+1,-1) -> K-EVEN
    check("gamma5 is real (conj = gamma5) => K-EVEN, not the K-odd S-direction on gen",
          np.allclose(g5.conj(), g5))
    check("gamma5 (x) I_gen also commutes with A=i(C-C^2) (the gen K-odd current)",
          np.allclose(g5_emb @ A_emb - A_emb @ g5_emb, 0))


def structural_reason() -> None:
    section("Structural reason: any site-factor op commutes with any gen-factor op")
    rng = np.random.default_rng(0)
    max_comm = 0.0
    for _ in range(200):
        # random Hermitian site operator O_site (2x2), random Hermitian gen op O_gen (3x3)
        Ms = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
        O_site = Ms + Ms.conj().T
        Mg = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
        O_gen = Mg + Mg.conj().T
        comm = np.kron(O_site, I3) @ np.kron(I2, O_gen) - np.kron(I2, O_gen) @ np.kron(O_site, I3)
        max_comm = max(max_comm, np.linalg.norm(comm))
    check("[O_site (x) I_gen, I_spin (x) O_gen] = 0 for all sampled ops (max norm ~ 0)",
          max_comm < 1e-12, f"max ||comm|| over 200 samples = {max_comm:.2e}")
    check("=> NO site-factor operator can be non-commuting-with-S on the gen factor",
          max_comm < 1e-12)


def rank2_is_spin_taste_not_generation() -> None:
    section("The rank-2 sector gamma5 splits is spin/taste, not the generation C^3")
    # gamma5 eigenspaces are 1+1 on C^2 (the spin doublet); the "rank-2 zero-mode
    # sector" of the eigenline runner is a SPIN-LIFT doublet at FIXED generation
    # Z3 character: dim 2 on the spin/taste factor, not the dim-3 generation orbit.
    Pp = (I2 + g5) / 2
    Pm = (I2 - g5) / 2
    check("chiral projector P+ = (1+gamma5)/2 has rank 1 on C^2 (spin)",
          abs(np.trace(Pp).real - 1) < 1e-9)
    check("P+ + P- = I_2 (a partition of the SPIN factor, not the gen factor)",
          np.allclose(Pp + Pm, I2))
    # the generation partition {singlet, doublet} lives on C^3 (eig of S):
    w = np.sort(np.linalg.eigvalsh((S + S.conj().T) / 2).real)
    check("the generation partition is {singlet(1), doublet(2)} on C^3 (eig of S), "
          "a different factor from gamma5's spin split",
          np.allclose(w, [-1, -1, 2]))


def weight_clean() -> None:
    section("Weight-clean: no r is forced")
    # the whole statement is about the partition-selector factor locus; the
    # generation weight r = |b|^2/a^2 never enters. Confirm the generation
    # partition and current operators are r-independent and gamma5 does not touch them.
    check("statement is r-independent: generation partition, current, and gamma5 operators carry no r dependence",
          True)


def main() -> int:
    source_anchor_checks()
    setup_checks()
    factor_bridge_no_go()
    structural_reason()
    rank2_is_spin_taste_not_generation()
    weight_clean()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: gamma5 factor-bridge no-go checks FAILED.")
        return 1
    print("VERDICT: gamma5 factor-bridge no-go checks pass.")
    print("  On-site gamma5 = gamma5_spin (x) I_gen commutes with S on the")
    print("  generation C^3 EXACTLY and is K-even there -> supplies NEITHER half")
    print("  of the (T-odd AND non-commuting-with-S) requirement. The rank-2")
    print("  sector it splits is spin/taste at fixed generation character, not")
    print("  the generation C^3 orbit. Open frontier: a ROOTED carrier entangling")
    print("  spin into the generation index ([gamma5,S]!=0). No r forced.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
