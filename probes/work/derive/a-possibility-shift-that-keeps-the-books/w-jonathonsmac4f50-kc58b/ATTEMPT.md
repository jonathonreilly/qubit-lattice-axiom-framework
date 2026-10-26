# Attempt: a-possibility-shift-that-keeps-the-books (a1)

Worker: Claude Sonnet 5.5. Same family as the supervisor's blocks; unrefereed. Nothing here is adopted.

## Plain-language summary

The question was whether a short-range extra term between neighbouring records can repair the energy-current books that "one record per site" breaks on the plane and in space. Main already answers it, twice: no fixed-position coin term does (block 141), and no bounded finite-range interaction does (the 2026-09-26 note). So part (a) is not open, and parts (b) and (c) have nothing to act on in 2D/3D. I did not find a V. I added one small exact structural fact about pair-moving terms, which block 141 did not treat, and one exact fact about the line.

## Read before concluding

- `docs/MINIMAL_AXIOMS_2026-06-29.md` read in full (233 lines) on main_wt (a77a3449). Used: Admissibility is not a dynamics axiom; no possibility or site is privileged; one record per site; walk, exclusion, currents, placements are supplied clauses, not axiom content.
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` read in full (130 lines). The approved primitives are scale_reference, kinetic_isotropy and realized_state; none is used here.
- Sources, as landed on main (origin/main moved to 3e1a2dd during the work; none of the notes below changed between a77a3449 and 3e1a2dd):
  - block 137: `docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_KEEPS_THE_BOOKS_ONLY_AT_LEADING_ORDER_..._2026-09-25.md:60-80` (T1, T2), `:84-96` (T3).
  - block 141: `docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_NO_POSSIBILITY_SHIFT_AMONG_NEIGHBOURS_RESTORES_THE_BOOKS_..._2026-09-25.md:62-80` (three-hop support proof), `:142-145` (N1: correlated hops, other placements, longer reach not treated).
  - 2026-09-26 note: `docs/ADMISSIBILITY_RULE_NO_FINITE_RANGE_INTERACTION_KEEPS_TWO_EXCLUDED_RECORDS_TOTAL_ENERGY_CURRENT_..._2026-09-26.md:77-118` (theorem, S0-S7), `:120-129` (any number of records), `:204` (scope left open).

## Source mismatch the supervisor must know

The task text says blocks 137-139 are open hand-off PRs and that (a) is unsettled. On main, block 137 and block 141 are landed. The 2026-09-26 note (landed) proves, in its stated class, that `[H', J'] != 0` for every bounded hermitian translation-invariant interaction of finite relative range, hopping terms included, with placements of the form free current + one-body change + finite-rank remainder. That is the answer to (a) for nearest-neighbour reach. The task's own HIT ("(a) settled with exact checks") is therefore already met on main for its stated class. No RECOVERY_STATUS.json is written because the brief names no source branch.

## 1. The exact statement attempted

(a) On the Z^2 and Z^3 two-record walk of block 54 under block 78's compression, find V, acting only on neighbouring records and covariant, such that the total energy current of H2 + V is kept; or prove none exists.

Because main already settles this in a stated class, I attempted the sub-obligation that block 141 flagged as untreated and the 2026-09-26 note treats only analytically: an elementary, finite-algebra account for V that moves records (pair-translating or rotating terms), with an arbitrary dipole placement.

## 2. Steps

Notation. v = records at (0,0) and e1, both coins up. w = records at (-1,-1) up and (0,0) down. The witness entry is `<w|[H2+V, J]|v>` with `J = i[H2+V, D2+V_D]`. A "bond configuration" is a pair of records on adjacent sites. "Bond-supported" means V = P_b V P_b and V_D = P_b V_D P_b, with P_b the projector onto bond configurations, V and V_D Hermitian and otherwise arbitrary (any translation of the pair, any rotation, any coin matrix, no translation invariance).

1. ASSUMED (supplied, from main): the walk, block 78's exclusion, `D2` with weight `(x_t+x_s)/2` on the moving record, `J = i[H2, D2]`.
2. CHECKED (A1, A2): with V = 0 the witness entry is `-i/16` for both exchange signs on Z^2 and Z^3. This reproduces the landed number with an independent implementation; it is retrieval, not new.
3. PROVED (parity lemma). Let `s` be the sum of all coordinates of both records. Every bond configuration has odd `s`, because `s = 2*(sum of the lower record's coordinates) + 1`. A free hop (from H0 or D0) changes `s` by one. A bond-supported operator takes odd `s` to odd `s`. Here v has `s = 1` and w has `s = -2`, so w is not a bond configuration and a monomial must contain an odd number of free hops. Expand `[H,[H,D]] = H^2 D - 2 H D H + D H^2` with `H = H0 + V`, `D = D0 + V_D`. A monomial with a V-type factor X acts on a bond configuration, so the state just before X must have odd `s`.
   - One V-type and two free factors: two free hops give even parity change, but the net change must be odd. Vanishes.
   - Three V-type factors: no free hop, net change even. Vanishes.
   - Two V-type and one free factor: the only order that survives is both V-type factors acting first and the free hop last. A free hop acting before a V-type factor would leave an even-`s` state, which is not a bond configuration, so that V-type factor gives zero.
   So `entry = -i/16 + B`, with `B = i <w| H0 (V V_D - 2 V_D V) + D0 V V |v>`, bilinear in (V, V_D). There is no term linear or cubic in V. The same argument holds on Z^3 (coordinate sum over all axes) and for either exchange sign.
4. CHECKED (B1, B2, B3, B4): the type census of step 3; and on dense random exact Hermitian V and V_D (Gaussian rationals; Z^2 window [-2,2]^2 with 160 states, both signs; Z^3 window [-1,1]^3 with 216 states), `entry(t)` for V -> tV, V_D -> tV_D is exactly `-i/16 + c t^2`, and the coefficients of t, t^3, t^4, t^5 are zero. With V_D the midpoint-weighted copy of V, c is still nonzero (B3).
5. PROVED + CHECKED (size bound; C1-C3). `<w|H0` restricted to bond configurations has four entries and squared norm 1. `<w|D0` (x component) restricted likewise has squared norm 3/8. Hence `|B| <= (3 + sqrt(6)/4) N^2` with `N = max(||V||, ||V_D||)`, using `||X1 X2 X3 v|| <= r ||X2|| ||X3||`. If the witness entry vanishes then `|B| = 1/16`, so `N^2 >= 1/(16(3 + sqrt(6)/4)) = 0.0173`. This only says a repairing bond-supported V cannot be weak. It is one entry, and the bound is not sharp.
6. CHECKED (D1, D2): the step-3 argument does not make `B` vanish in general, so block 141's support argument does not extend to pair-moving V. For V = mu*(1 on bonds) + lam*(translate the pair one site along its axis) with midpoint-weighted dipole, `B = 0` for symbolic lam and mu (the witness is untouched). For a generic random bond-supported V, `B` is a nonzero complex number, so this one entry can in principle be cancelled by a large V.
7. SUGGESTED (not proved here): nothing in steps 3-6 decides the other entries. In the odd-parity sector the equations read `F0 + Q(V, V_D) = 0` with `F0` the free exclusion defect. In the even-parity sector they read `L(V, V_D) + C(V, V, V_D) = 0`, homogeneous, satisfied by V = 0. A complete elementary no-go would have to combine the two sectors; I did not find the combination.
8. PROVED on main, not by me: for every bounded translation-invariant hermitian V of finite relative range and every placement in the stated class, `[H', J'] != 0` on Z^2 and Z^3, any number of records (2026-09-26 note `:77-129`). By this, parts (b) and (c) have no 2D/3D content: there is no V whose momentum law or line reduction needs deciding.
9. CHECKED (Ea, Eb), line only, relevant to part (c): on Z with V = U (identity on neighbouring pairs), energy at the bond midpoint, the defect of J is nonzero at order U^2 on 8 of 16 test pairs (separation 1 to 4, all coin pairs, both signs). Adding a one-body piece `-U X` to the dipole (X = total position; equivalently an energy `-U` per record) makes all 16 defects vanish, for symbolic U. So on the line V = 0 is not the only kept case, and the reduction to block 121's free chain pair is the U = 0 member of a family. This is a finite fact on test pairs. I did not prove it for all states; the expected mechanism is the integrable (XXZ) structure after block 121's site unitary (ASSUMED, standard, not re-proved). The `-U X` piece is a placement change of zero range, which the 2026-09-26 note's step S1 excludes in 2D/3D (a one-body placement change must vanish there).

## 3. First step that fails

The route "extend block 141's minimum-hop support proof to nearest-neighbour V that moves records" fails at step 3-6: the proof needs every V-containing monomial to have fewer hops than the witness distance (3). A pair-translating V has two-hop displacement, so V-containing monomials do reach the witness. The parity lemma removes all linear terms but leaves the quadratic form `B`, which is not zero in general (step 6). The elementary route stops there. The unconditional answer comes from the analytic 2026-09-26 theorem, not from this attempt.

## 4. What is new, and what is not

Not new: the −i/16 witness (step 2), the coin-term no-go (block 141), the finite-range no-go (2026-09-26 note), the line result for V = 0 (block 137 T2).

New, scoped (same-family, unrefereed):
- the parity lemma (step 3) and the exact "no linear, no cubic term" structure for all bond-supported V and V_D, including pair-moving terms and arbitrary dipole weights; it holds without translation invariance or rotation covariance;
- the explicit size bound (step 5);
- the exact line fact (step 9): naive density-density term fails at U^2, with the one-body placement piece it passes on the 16 test pairs.

None of these decides part (a); the landed theorem does.

## 5. What would finish an elementary route

Combine the odd-sector quadratic equations with the even-sector homogeneous equations for the covariant bond-supported class on Z^2 (a finite polynomial system once translation and rotation covariance are imposed), and show it has no solution. That is a Groebner or resultant computation, which I did not run (sympy only). Separately, an other-family referee should read the 2026-09-26 proof (S3 density step and S5 volume bounds are the steps the note itself says no runner checks).

## Files

- `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-poison-ivy-oak-treatment-90452e/a67d71b1-0c50-4041-92e4-07c78ad7ebea/scratchpad/attempts/a-possibility-shift-that-keeps-the-books/check.py` (`TOTAL: PASS=15 FAIL=0`, about 75 to 115 s, one process, sympy only)
- exploration scripts left in the same folder (`explore.py`, `explore2.py`, `line.py`, `line2.py`, `line3.py`, `shiftV.py`, `weighted.py`, `xxz.py`): scratch, not part of the deliverable.
