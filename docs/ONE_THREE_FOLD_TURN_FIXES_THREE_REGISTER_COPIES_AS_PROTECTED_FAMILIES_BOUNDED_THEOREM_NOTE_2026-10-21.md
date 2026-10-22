---
claim_id: one_three_fold_turn_fixes_three_register_copies_as_protected_families_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "If the coarse tick carries its block positions as a supplied family register and every turn-allowed term on it is present, a generic turn-invariant Dirac mass leaves exactly F3 protected families, F3 being the number of register copies one three-fold turn fixes; on the site's 3^3 block F3 = 3 and the other 24 copies are vector-like; the mirror partners gap at twist k = 2 iff 3 divides F3; no mass hierarchy or mixing is predicted, and the register reading is not in the current laws."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/one_three_fold_turn_fixes_three_register_copies_as_protected_families_2026_10_21.py
---

# One three-fold turn fixes three register copies, and those are the protected families

Claim type: bounded_theorem.
Primary runner: `scripts/one_three_fold_turn_fixes_three_register_copies_as_protected_families_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight and contains no family law. This note asks which family copies survive a generic symmetric mass when the coarse tick carries the positions of its block as an internal index. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither that reading nor the terms on it.

## Statement

Grant two supplied rules: the coarse tick carries the positions of its block as an internal register index, and every term on that index that the twisted turns allow is present. Let F3 be the number of register copies that one three-fold turn maps to themselves. Then:

1. A generic turn-invariant Dirac mass leaves exactly 8 F3 massless states, carrying F3 copies of one family's representation.
2. On the site's 3^3 block (27 copies), the turn fixes 3: the site and the far corners of its even and odd cube. The other 24 form 8 three-cycles, each of which allows an ordinary turn-invariant Dirac mass pairing its light copy with its mirror copy, so those 24 families are vector-like.
3. At twist k = 2 the mirror and zone-corner partners of the protected families can be gapped iff 3 divides F3.
4. On the protected space the allowed family operators are (cube commutant) x M_3, so any hierarchy and any mixing are allowed and none is predicted.

## Derivation

A (2m)^3 cell has F3 = m fixed copies and (m^3 - m)/3 three-cycles, and every register X has |X| = F3 mod 3. Blocks of a factor-2 rung have F3 = 2^n, never 0 mod 3, so no factor-2 rung carries three protected families. Every site lies on one body diagonal d shared by its even and odd cube; the rotations about the site that keep both tilings are the three turns about d, and in the site's 3^3 block they fix exactly {x - d, x, x + d}. Axes give F3 = 0, body diagonals 1 and aligned tilings 2.

The sublattice-keeping Dirac masses at Gamma span 4 dimensions; each pairs the light copy with the mirror copy, the turn gives them charges w and w^2 (twice each), and none is invariant under the 12 turns. On a three-cycle the turn permutes copies, so a combination of these masses over the cycle is invariant; on a fixed copy no such combination exists. By Schur's lemma and the count of turn characters, a generic invariant mass leaves exactly 8 F3 massless states.

On a register the turn permutes, the Z3_k x SU(2)_e^2 anomaly of the gapped set S is -4(|X|(q_a + k) + n_1 + 2n_2) = -4 F3 (q_a + k) mod 3. For the 27-copy register this is -528 in total, -60 per three-cycle, -16 per fixed copy and -48 for the three fixed copies. A twisted Haldane criterion (a turn-invariant Lagrangian gaps symmetrically iff z.l = 0 mod 3 on its turn-fixed part) gives the same condition. Negative result: each three-cycle has a turn sector that is anomaly-free on its own, so the anomaly alone does not force families to be removed in threes, and the minimal anomaly-free set could be a single family.

The protected left and right families factor as spinor x register. A vacuum that ignores the register therefore gives every sector the same mass matrix: equal mass ratios in all sectors and no mixing.

## Checks

The runner ends with `TOTAL: PASS=13 FAIL=0`. Among its lines:

- `[PASS] A1 theorem: in a (2m)^3 cell one three-fold turn fixes m of the m^3 copies ... and moves the rest in (m^3-m)/3 three-cycles (m = 1..9); |X| = F3 mod 3 for every register; blocks of a factor-2 rung have F3 = 2^n, never 0 mod 3`.
- `[PASS] A2 theorem: every site lies on one body diagonal d shared by its even and odd cube; the rotations about the site that keep both tilings are the three turns about d`.
- `[PASS] A3 fixed copies of one turn: axes 0, body diagonals 1, aligned tilings 2, shells 3, site block 3, 6^3 cell 3`.
- `[PASS] A4 theorem: on a permuting register Z3_k x SU(2)_e^2 of S is ... = -4 F3 (q_a+k) mod 3; at k = 2 the doublers gap iff 3 | F3`.
- `[PASS] B1 theorem ...: eps-keeping Dirac masses at Gamma span 4 dims, every one pairs the light copy with the mirror copy, the turn gives them charges w, w^2 (twice each), none is invariant under the 12 turns`.
- `[PASS] B2 theorem (Lefschetz count; finite check on 12 registers, with and without P and PW): a generic turn-invariant Dirac mass leaves exactly 8 F3 massless states`.
- `[PASS] B3 6^3 register (27 copies) with an invariant mass, 7^3 grid: 24 massless states at Gamma and at R, gapped at every other point | min gap off the windows 0.504`.
- `[PASS] C1 theorem (twisted Haldane criterion ...): light-mirror backscattering on the 8 three-cycles is null, neutral, primitive and twisted-neutral`; on a fixed copy the same term has z.l = 1 and is forbidden.
- `[PASS] C2 theorem + finite`: over m = 1..4, at k = 0 and k = 2 only m = 3 gaps.
- `[PASS] C3 the three protected families are removable together ...: the anomaly does not protect them; only bilinears are excluded`. In 3D a term built from light-copy modes alone has turn charge equal to its mode change, so with Z4 it must change mode number by 12.
- `[PASS] D1 theorem: on the protected space the turns act as 3 copies of the cube, so the allowed family operators are (cube commutant) x M_3 ... | dim 72 = 8 x 9`.
- `[PASS] D2 diagnostic (supplied random textures)`: with a register-diagonal mass the light families are exactly the fixed copies (weight 1.000); off-diagonal parts d tilt them inside the 11-dimensional turn-invariant sector (0.916, 0.393, 0.322 at d = 0.05, 0.2, 1.0).
- `[PASS] D3 theorem + [M]`: a register-blind vacuum gives ratios (1, 0.415, 0.118) in both sectors with |V_12| = 3e-16, against |V_12| = 0.34 for a register-dependent vacuum.

## Estimates against measurement

N_nu = 3 against 2.9963 +- 0.0074 is 0.5 sigma. The next anomaly-allowed counts, 6 and 9, are about 406 and 811 sigma off. Counts 1, 2, 4 and 5 are anomaly-forbidden on every register, so there is no fourth chiral family. The 24 vector-like families have mass of order the copy-mixing coefficient times the cell scale; vector-like quark limits near 1.5 TeV need that coefficient above about 1e-16 for a Planck-scale cell. Each light family keeps one right-handed neutrino with Dirac mass only; the estimated Delta N_eff of 0.14 to 0.29 is a mild tension against Planck. The measured mass log-ratios (1.889, 1.299, 0.787 for leptons, up and down) and |V_us| = 0.2243 exclude a register-blind vacuum.

## Boundary

Supplied: H' as the generator, the mirror term that fixes k = 2, the zone-corner term and the sufficiency of symmetric mass generation, all from the unadopted unification candidate; the register reading (under the fine tick itself the 27 copies are folded momenta and only fine Gamma is light); a term that sees the block geometry (if every term ignores the register, an extra turn stays exact, forbids every copy-mixing mass, and all 27 copies stay light); and the zoom factor 3 (the smallest zoom that maps the sites and both tilings to themselves). None of these is in the current laws. Antiunitary symmetries were not checked; if exact they could only raise the count. Axes or tilings as the family index fail: a triplet the turn cycles has F3 = 0, and aligned tilings have F3 = 2 and are anomaly-forbidden. No hierarchy, mixing or vacuum clause is derived.
