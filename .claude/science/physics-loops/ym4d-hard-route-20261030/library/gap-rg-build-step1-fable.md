lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-23T14:08Z

# Row 1428: build step 1 of the computer-assisted tool in Lean

Started 2026-11-23T02:08Z (date -u), pinned at commit ac38ef61e. Research-stage working state; no status granted.

## Plan (save protocol)

1. Read row 1418 ('What to implement', 'First buildable component'), check 1420, row 1427 and `lean/glue/RECEIPT.md`.
2. (a) Lean: N = 1 four-dimensional link inventory (counts 1, 15, 30, 5; D_1 = 51) and the 12,910,079 slot count.
3. (b) Lean: one signed closed fundamental cube, b = 1/16, contribution 2^(-28).
4. (c) Lean: four failing acceptance fixtures, each corruption named exactly.
5. Report axioms, wall time, peak memory; state what stays outside Lean; next two rows.

Each step is appended below as it is done.

## Repo search and credit

- Row 1418 (`library/gap-rg-step-sizing-astra62.md`, gpt-6.2-astra): the inventory formula, the counts 1, 15, 30, 5, D_1 = 51, the 12,910,079 slots, the histogram, the cube value b^6/16 and the fixture list. All statements checked here are theirs; nothing below is a new mathematical statement.
- Check 1420 (`library/gap-rg-step-sizing-check-opus.md`, Claude Opus 5.5): independent C brute force over 2^24 corner subsets; defect 3 (fixture corruptions must be named exactly) and defect 4 (no kernel receipt) are what this row answers.
- Row 1427 (`lean/glue/GlueNamed.lean`, `RECEIPT.md`): the 2D gluing fixture, already kernel-checked; reused unchanged for fixture (c).
- Published sources behind the model: Oeckl and Pfeiffer hep-lat/0110034 (spin-foam form of lattice gauge theory); Sussman-Alpoge complete account GL3-GL4 (SA 2195-2243) for the character coefficients; Yosprakob arXiv 2311.02541 (site tensor without magnetic indices).
- `grep` of `library/open-core.md` for the cube, b^6/16 and the unbranched surface formula: no hit; the value is used as row 1418 states it (unbranched closed surface, b^F d^(V-E)).

## Design (written before any Lean run)

Lean 4.36.0, `import Init` only, no mathlib, no `native_decide`. Closing tactic: `decide` or `decide +kernel` (kernel definitional evaluation; proof term `of_decide_eq_true (Eq.refl true)`, no axiom expected; to be confirmed by `#print axioms`).

(a) Link inventory. Two independent definitions and one formula, all evaluated in the kernel:
  1. weight count: singlet multiplicity of k fundamentals = [z^0] - [z^2] of (z + 1/z)^k, by explicit polynomial product;
  2. C(6,k) Cat(k/2);
  3. D_1 = [z^6] of the row 1418 generating function at N = 1, by truncated integer power-series arithmetic.
  Slots: vertex figure K_{2,2,2,2}, nodes 0..7 with antipode i xor 1, 24 edges. Degree vector stored as one natural in base 8 (degree <= 6). (i) Definition: sum over ALL 2^24 edge subsets of prod_v w(deg v), w = 1, 0, 1, 0, 2, 0, 5 (so odd degree gives 0). (ii) Pruned: the same recursion, abandoning a branch when a node whose edges are all decided has odd degree. Attempt (i) in the kernel; if too slow, report it and keep (ii). Also the histogram by the pattern at node 0 and its two moments.

(b) Cube. Geometry given as data: 8 vertices, 6 faces as oriented 4-cycles. Trace indices: one two-valued index per (face, corner), 24 in all. Haar second moments in integer form (2 x integral): same direction 2 int U_ab U_cd = eps_ac eps_bd; opposite direction 2 int U_ab (U^-1)_cd = delta_ad delta_bc. Lean finds, for every link, its two faces and their relative direction, builds the 24 link-end factors, sums the product over all 2^24 index assignments (depth-first, a zero partial product is abandoned), and checks numerator / denominator = b^6 2^8 / 2^12 = 2^(-28) at b = 1/16. Checked for the outward orientation and for all 64 choices of face orientation (the sign must not depend on them because chi_(1/2) is real).

(c) Failing fixtures, each naming the exact corruption: C1 missing 1/d on exactly one link; C2 spin-one channel dropped; C3 zero denominator; C4 twist sign (centre source on one face not applied / applied on a closed pair).

## Step 1 log: what the kernel can and cannot do in one evaluation (measured)

- First attempt: `pruned (wt 8) steps 0 = 12910079` as ONE `decide +kernel`, with the step list left as an unevaluated expression. Stopped after 10 minutes without an answer.
- With the step list as a literal: 65,536 leaves take 14 s and 3.27 GB peak; the full 131,072 leaves did not finish in 240 s. The time grows faster than the work, and memory is the cause (the kernel caches every intermediate term and the accumulated degree vector stays an unevaluated sum).
- With the accumulator forced to a literal at each step (a `match` on `d + c`): the same 65,536 leaves take 2.8 s and 1.1 GB.
- Consequence for the design: one kernel evaluation of the whole count is the wrong shape. The count is split by the six-bit pattern at node 0 into 64 separate theorems (each its own kernel run with fresh caches), joined by a lemma proved in Lean by induction. The all-subsets sum over 2^24 corner sets (the bare definition) is NOT attempted in the kernel: at the measured rate it would need about 128 times the work and a split into about a thousand theorems. It is instead tied to the pruned sum by a kernel check on the smaller figure K_{2,2,2} (4,096 subsets) and by check 1420's independent C brute force (outside Lean).
- The numeric lock is held (holder `gap-rg-build-step1-fable`) for the Lean runs; memory free was 68 percent at the first run.
- Two lapses, reported: (i) one full run of the inventory file was started when memory free read 32 percent, because my command printed the reading without testing it and two of my own timed-out test processes were still alive; I stopped that run, killed the two processes, and every later run was gated at 50 percent (readings 76 to 77 percent). (ii) While I held the numeric lock another session's Lean job was running on this machine (`sa-gap-rg-ring-lean-replay-astra62` by its scratch path); I left it alone. The times below may be slightly inflated by it.

## Step 2 result: (a) the N = 1 inventory is kernel-checked

*(Numbers of the first passing run. The final file replaces `omega` and `List.getD` by plain lemmas and helpers, so the axiom list shrank to `propext` only; final hash, time, memory and verbatim axioms are in the section "Final runs" below and in `lean/step1/RECEIPT.md`. The statements and the proof structure are unchanged.)*

Run finished 2026-11-23T03:00Z (date -u). File `lean/step1/Inventory.lean` (760 lines; sha256 06969f99ebd5d8d008748e8562c62e12c068eb9f008da98e76eb47a788c182e8), command `lean Inventory.lean`, Lean 4.36.0, `import Init` only, no `native_decide`. Exit 0, **60.9 s wall, peak resident 1,169,571,840 bytes (1.17 GB)**; memory free before the run 76 percent.

What is proved (theorem names in namespace `Step1`):

| Statement of row 1418 | Lean theorem | How |
|---|---|---|
| singlet multiplicities 1, 0, 1, 0, 2, 0, 5 for 0..6 fundamentals | `singlet_table`, `w_is_singlet` | weight count [z^0] - [z^2] of (z + 1/z)^k |
| link counts 1, 15, 30, 5 | `link_counts` | C(6,k) times the multiplicity |
| D_1 = 51 | `link_total_by_occupancy`, `link_total_by_patterns`, `D_one` | three routes: by occupancy, by the 64 patterns, and the generating function of row 1418 by truncated integer series |
| D_2 = 977 | `D_two` | same generating function |
| 24 corners, every node of degree 6 | `corners_card`, `corners_degree_six` | K_{2,2,2,2} built from the rule j != i xor 1 |
| 131,072 even subgraphs | `even_subgraphs` | pruned sum, 64 pieces |
| **12,910,079 slots** | `slots` | pruned sum of prod_v Cat(deg v / 2), 64 pieces |
| 413,122,528 bytes | `slot_bytes` | arithmetic |
| histogram 50,920 / 114,551 / 115,144 / 262,978 / 265,805 / 635,318 | `histogram` | for each of the 64 patterns at node 0 |
| label counts 1, 3, 12, 6, 24, 5 | `histogram_labels` | |
| first moment 12,910,079, second moment 4,329,800,859,159 | `first_moment`, `second_moment` | |

Structure of the slot proof. `pruned leaf steps d` is the sum over corner subsets in lexicographic order that returns 0 as soon as a node whose corners are all decided has odd degree. `prunedS` is the same function with the accumulator forced to a numeral; `prunedS_eq` proves them equal by induction. `split` (induction, no evaluation) rewrites the sum as a sum over the 64 start vectors of the six corners at node 0. Each start vector is one theorem `slot_k`, `even_k`, `hist_k` closed by `decide +kernel` (192 small kernel evaluations, about 0.6 s each for the 96 even ones). `total_of_pieces` joins them.

What is NOT proved in Lean here:

1. The sum over all 2^24 corner subsets (the bare definition `brute`) is not evaluated for K_{2,2,2,2}, and no Lean theorem states `brute = pruned` in general. The pruning only drops branches where a completed node has odd degree, where the leaf weight is 0; this is checked in the kernel on the octahedron K_{2,2,2} (`octahedron_slots_agree`: all 4,096 subsets against the pruned sum; `octahedron_even` = 128 = 2^(12-6+1)), and check 1420's C brute force gives 12,910,079 outside Lean. A general Lean lemma `brute = pruned` is a short induction on the step list (gap, not done).
2. That Cat(deg/2) is the number of structurally admissible entries (noncrossing pairings as a basis of invariants) is the representation-theory input of row 1418, not a Lean statement; Lean checks the weight count 1, 1, 2, 5 only.

The generator `gen_inventory.py` (with `inventory_head.lean.txt` and `values.txt`) writes the 192 piece theorems; the values come from Lean's `#eval` and are only right-hand sides that the kernel then checks.

`#print axioms`, verbatim:

```text
'Step1.singlet_table' depends on axioms: [propext]
'Step1.w_is_singlet' depends on axioms: [propext]
'Step1.link_counts' depends on axioms: [propext]
'Step1.link_total_by_occupancy' depends on axioms: [propext]
'Step1.link_total_by_patterns' depends on axioms: [propext]
'Step1.div_mul_sanity' does not depend on any axioms
'Step1.D_one' depends on axioms: [propext]
'Step1.D_two' depends on axioms: [propext]
'Step1.corners_card' depends on axioms: [propext]
'Step1.corners_degree_six' depends on axioms: [propext]
'Step1.prunedS_eq' does not depend on any axioms
'Step1.octahedron_even' depends on axioms: [propext]
'Step1.octahedron_even_pruned' depends on axioms: [propext]
'Step1.octahedron_slots_agree' depends on axioms: [propext]
'Step1.split' depends on axioms: [propext, Quot.sound]
'Step1.steps_eq' depends on axioms: [propext]
'Step1.stepsLit_split' does not depend on any axioms
'Step1.starts_eq' does not depend on any axioms
'Step1.starts_eq_masks' does not depend on any axioms
'Step1.slot_pieces' does not depend on any axioms
'Step1.even_pieces' does not depend on any axioms
'Step1.hist_pieces' does not depend on any axioms
'Step1.split0' depends on axioms: [propext, Quot.sound]
'Step1.total_of_pieces' depends on axioms: [propext, Quot.sound]
'Step1.even_subgraphs' depends on axioms: [propext, Quot.sound]
'Step1.slots' depends on axioms: [propext, Quot.sound]
'Step1.slot_bytes' does not depend on any axioms
'Step1.histogram' does not depend on any axioms
'Step1.histogram_labels' does not depend on any axioms
'Step1.first_moment' does not depend on any axioms
'Step1.second_moment' does not depend on any axioms
```

So nothing beyond `propext` and `Quot.sound`. They enter through `omega` (in `split`, `sum_map_add`) and through core library instances used by `decide`; no `Classical.choice`, no `Lean.ofReduceBool`, no `sorryAx`.

## Step 3 log: the cube evaluator, first measurements (file `Surface.lean`, not final yet)

- The evaluator builds the link-end factors from the face list and sums over the 24 corner indices. In the kernel: `cube_haarSum` (= 256 = 2^8), `cube_value` (2^(-28) accepted), the C1, C3, C4a fixtures each check in about 2.4 s and 1.13 GB when run alone.
- One theorem over all 64 face orientations did not finish in 30 s (same cache growth as in step 1); it is being split into 64 theorems. A check over all 4,096 link-sign assignments took 12 s and 3.9 GB, above the 2 GB rule; it is being replaced by a parity statement.
- **Finding (by `#eval`, compiled evaluator, guidance only until the kernel theorems below): the cube does not test the pairing sign.** With `eps` replaced by its absolute value, and also with `delta delta` used for every link whatever the directions, the cube gives 256 for all 64 orientations, the same as the correct rule. Reason: at each vertex three link ends form a triangle on three indices, an odd number of `eps` factors gives 0 and two give `sum eps_ab^2 = 2` in every arrangement that occurs. So on an orientable sheet a wrong sign in the same-direction rule is invisible, and "an incorrect twist sign must fail" needs either the centre twist on a face (C4a) or a non-orientable sheet.
- Repair of the fixture: the hemicube (the cube modulo the antipode: 4 vertices, the 6 links of K_4, the 3 Hamiltonian four-cycles as faces; a projective plane, V - E + F = 1). Hand value of the Haar integral, by fixing the three links at vertex 0 to the identity (A = U_12, B = U_23, C = U_13):
  int tr(AB) tr(C B^-1) tr(A^-1 C) = (1/2) int tr(AC) tr(A^-1 C) = (1/4) int tr(C^2) = (1/4) int (chi_1 - 1) = -1/4,
  using int U_ij (U^-1)_kl = delta_il delta_jk / 2 twice. So the integer sum must be -(1/4) 2^6 = -16: the Frobenius-Schur sign -1 of the fundamental representation times d^V. This is the fixture for the pairing sign.

## Step 4 result: (b) the signed closed cube and (c) the failing fixtures

Files `lean/step1/Surface.lean` (namespace `Step1Surface`) and `lean/step1/GlueFixtures.lean` (namespace `Step1Glue`).

**The evaluator.** A surface is a list of faces, each an oriented four-cycle of vertices. Lean itself derives the links, finds the two faces on each link and their relative direction, forms two integer end factors per link (`delta delta` for opposite directions, `eps eps` for the same direction, eps = [[0,1],[-1,0]]), and sums the product over all assignments of one two-valued index per face corner (24 for the cube). The certificate is numerator / denominator with the face coefficients and one factor 1/2 per link; `accept` is cross-multiplication with both denominators required nonzero.

**(b), kernel-checked.**

| Statement | Lean theorem |
|---|---|
| cube: 24 corners, 12 links, 6 faces; every link in two faces; outward orientation consistent | `cube_counts`, `cube_closed`, `cube_consistent` |
| integer sum 2^8 = 256 (one free index per vertex) | `cube_haarSum` |
| **value at b = 1/16 is 256 / (16^6 2^12) = 2^(-28) = b^6/16** | `cube_value`, `cube_value_cert` |
| the same sum for all 64 orientations of the six faces (62 of them use `eps`) | `cube_orient_0` ... `cube_orient_63` |

**(c), each fixture with its exact corruption.**

| Fixture | Corruption, exactly | Result | Lean theorems |
|---|---|---|---|
| C1 cube | the 1/2 of exactly one of the 12 link integrals replaced by 1 | value 2^(-27); target 2^(-28) rejected | `C1_one_link_missing_inv_d_is_twice`, `..._rejected` |
| C1 2D square | the 1/d (d = 2) of the fundamental channel omitted in exactly one of the three gluings (first, or last) | fundamental coefficient 1/1024 (b = 3456), rejected | `C1_one_missing_last_is_3456`, `..._rejected`, `C1_one_missing_first_...` |
| C1 labels of row 1418 | two gluings without 1/d give 1/512 (b = 6912, the Lean target of row 1418); all three give 1/256 (b = 13824, the Python target) | all three targets rejected against the correct square | `C1_two_missing_is_6912`, `C1_three_missing_is_13824`, `C1_targets_rejected` |
| C2 | the adjoint (spin-one) output of one gluing set to zero, vacuum kept (first, or last gluing) | result is (1, 1/2048, 0), rejected | `C2_drop_in_last_...`, `C2_drop_in_first_...` |
| C3 | a face coefficient 0/0 (cube), a link denominator 0, a target denominator 0, a plaquette denominator 0, the certificate 0/0 | all rejected; **cross-multiplication without the guard accepts 0/0** (so the guard is needed) | `C3_zero_over_zero_passes_unguarded`, `C3_zero_over_zero_rejected`, `C3_zero_link_denominator_rejected`, `C3_zero_target_denominator_rejected`, `C3_zero_input_denominator_rejected` |
| C4a | centre source on one face of the cube (coefficient -1/16) | value -2^(-28); +2^(-28) rejected | `C4a_one_face_centre_source_is_minus`, `..._plus_rejected` |
| C4b | closed twist: centre signs on links | the six link masks of the faces cancel mod 2, so no closed-cube value changes; checked directly for the 12 single-link twists and for all links | `C4b_face_masks`, `C4b_face_masks_cancel`, `C4b_closed_twist_trivial_generators`, `C4b_twist_is_nontrivial_on_faces` |
| C4c | pairing sign dropped: eps_10 = +1 instead of -1 | hemicube gives +16 instead of -16, rejected | `C4c_abs_eps_value`, `C4c_abs_eps_rejected` |
| C4d | direction ignored: `delta delta` on every link | hemicube gives +16, rejected | `C4d_no_eps_value`, `C4d_no_eps_rejected` |
| C4e | wrapping sheet (3 x 3 torus, 18 links, 9 faces) with one twisted face | untwisted 2^(-45) = b^9/2^9; twisted -2^(-45); +2^(-45) rejected | `torus_haarSum`, `torus_value`, `C4e_wrapping_sheet_odd_twist_is_minus`, `..._plus_rejected` |

**The cube is blind to the pairing sign (kernel-checked for one orientation, by `#eval` for all 64).** `cube_blind_to_abs_eps` and `cube_blind_to_no_eps`: with face 0 reversed, both corrupted rules still give 256. So row 1418's sentence "an incorrect normalization or twist sign must fail a corresponding fixture" cannot be met by the cube for the sign of the same-direction rule; the cube tests the centre twist only. The hemicube (projective plane; `hemicube_haarSum` = -16, all 8 orientations, value -2^(-14) at b = 1/16) is the fixture that does, and its value -1/4 was derived by hand in step 3 above, independently of the evaluator. I did not find this remark in row 1418 or check 1420 (`grep` for hemicube, projective, Frobenius, non-orientable in both files and in `library/open-core.md`: no hit).

Scope note on C4e: on the wrapping sheet the sign statement is only that a face coefficient multiplies the value; the pairing of a twist with a wrapping sheet in a four-dimensional torus (which faces a given twist surface meets) is geometry that this file does not model.

## Final runs (written 2026-11-23T03:24Z, date -u)

| File | wall | peak resident | exit |
|---|---:|---:|---:|
| `Inventory.lean` | 70.07 s | 1,177,108,480 bytes | 0 |
| `Surface.lean` | 47.12 s | 1,128,185,856 bytes | 0 |
| `GlueFixtures.lean` | 0.41 s | 415,744,000 bytes | 0 |

Memory free was 77 percent before the runs; the numeric lock was held during all Lean runs and is released. Hashes and the complete verbatim `#print axioms` output (31 + 41 + 19 lines) are in `lean/step1/RECEIPT.md`. Summary of that output: every theorem "does not depend on any axioms" or "depends on axioms: [propext]"; the headline lines are

```text
'Step1Glue.C1_one_missing_last_rejected' does not depend on any axioms
'Step1Glue.C2_drop_in_last_rejected' does not depend on any axioms
'Step1Glue.C3_zero_over_zero_rejected' does not depend on any axioms
'Step1.D_one' does not depend on any axioms
'Step1.slots' depends on axioms: [propext]
'Step1.histogram' does not depend on any axioms
'Step1.second_moment' does not depend on any axioms
'Step1Surface.cube_value' depends on axioms: [propext]
'Step1Surface.C3_zero_over_zero_rejected' depends on axioms: [propext]
'Step1Surface.hemicube_haarSum' depends on axioms: [propext]
'Step1Surface.hemicube_value' depends on axioms: [propext]
'Step1Surface.C4c_abs_eps_rejected' depends on axioms: [propext]
```

`propext` enters through core-library definitions that `decide` evaluates; I did not trace which ones (measured: `List.getD` brings `propext`, and `==` on `Int` brings `propext`, `Classical.choice` and `Quot.sound`, so both were replaced by plain helpers). It is one of Lean's three standard axioms. Three negative controls (false claims) were refused by Lean.

Trusted base: the Lean 4.36.0 kernel, with its built-in GMP arithmetic on natural-number literals (`Nat.add`, `Nat.mul`, `Nat.pow`, `Nat.div`, `Nat.mod`, `Nat.beq`), which `decide +kernel` relies on; no compiled evaluator is trusted.

## What remains outside Lean

1. **Haar second and fourth moments.** The rules the integer models encode: E x^2 = 1/4, E xy = u/4, E x^2 y^2 = (1 + 2u^2)/24 for a Haar unit quaternion (2D gluing), and 2 int U_ab U_cd = eps_ac eps_bd, 2 int U_ab (U^-1)_cd = delta_ad delta_bc (surfaces). They are comments in the Lean files, not theorems.
2. **Schur orthogonality** chi_i * chi_j = delta_ij chi_j / d_j and the character coefficients of the plaquette weight.
3. **The representation-theory reading of the inventory**: that the singlet multiplicity counts the bond states and that prod_v Cat(deg/2) counts the structurally admissible entries.
4. `brute = pruned` for K_{2,2,2,2} (step 2, item 1): a short induction, not written.
5. The four-dimensional site tensor itself (recoupled values, magnetic contractions): not started; this row builds fixtures and an inventory, no physics inequality.

**Is a small Lean proof of the sphere moments in reach?** In core Lean, no: there is no measure or integral. The algebra, however, is small and is done here.

*Lemma SM (hand proof; arithmetic kernel-checked as `SM_relations`).* Let mu be a probability measure on the unit sphere of R^4 that is invariant under the sign change of each coordinate, under permutations of the coordinates, and under the rotation x_1 -> (3x_1 + 4x_2)/5, x_2 -> (-4x_1 + 3x_2)/5. Then every odd moment vanishes, E x_i^2 = 1/4, E x_i^4 = 1/8 and E x_i^2 x_j^2 = 1/24 for i != j.

*Proof.* A monomial with an odd exponent changes sign under one sign flip, so its mean is 0. By permutations m2 = E x_i^2, m4 = E x_i^4 and m22 = E x_i^2 x_j^2 do not depend on the indices. From sum x_i^2 = 1: 4 m2 = 1, and squaring, 4 m4 + 12 m22 = 1. By the rotation, 625 m4 = E (3x_1 + 4x_2)^4 = 81 m4 + 256 m4 + 6 (9)(16) m22, the terms x_1^3 x_2 and x_1 x_2^3 being odd; so 288 m4 = 864 m22, m4 = 3 m22. Hence 24 m22 = 1. QED.

Then, for y = u x_1 + sqrt(1 - u^2) x_2 (the scalar part of q v for a fixed unit quaternion v with scalar part u, after a rotation fixing the first axis; this uses invariance under the rotations fixing e_1, which the three listed symmetries do not give, so the hypothesis for the gluing rule is full O(4) invariance): E x y = u m2 = u/4 and E x^2 y^2 = u^2 m4 + (1 - u^2) m22 = (1 + 2u^2)/24, the numbers of `sew` (`SM_x2y2`, `SM_sew_coefficients`).

What a mathlib proof would need: Haar measure on SU(2) as a probability measure invariant under left and right translation, the identification of SU(2) with the unit quaternions so that these translations act by SO(4), and Lemma SM as above with integrability of polynomials on a compact group. All of these exist or are short in mathlib (`MeasureTheory.Measure.haar`, `Matrix.specialUnitaryGroup`); my estimate is a few hundred lines, one row, unchecked. The surface rules follow from the same moments: U = x_0 + i x.sigma has entries linear in x, so int U_ab U_cd is a quadratic moment, equal to (1/4) sum_k (s_k)_ab (s_k)_cd over the four basis matrices, which is eps_ac eps_bd / 2 (a 16-entry identity that the kernel can check once the moment is given).

## Next two rows

1. **Haar bridge in Lean with mathlib (gap-rg-build-haar-lean).** State and prove, with mathlib, Lemma SM for the Haar probability measure of SU(2) and derive the three gluing moments and the two link rules; then restate `sew`, `linkFactors` and `haarSum` as theorems about integrals for the 2D square, the cube and the hemicube. Decisive outcome: either `#print axioms` shows only the three standard axioms and the cube theorem reads "the Haar integral of the product of the six plaquette traces equals 1/16", or the first missing mathlib fact is named (candidates: invariance of Haar measure under inversion on a compact group, the SO(4) action on the unit quaternions) with its size. This removes items 1 and 2 of "outside Lean" for the fundamental channel; the adjoint channel needs the fourth moment only.
2. **The half-spin site tensor as a kernel-checked sparse table (gap-rg-build-site-tensor).** Using noncrossing pairings as the basis at each of the eight link ends (Gram matrices of sizes 1, 1, 2, 5: the Temperley-Lieb Gram matrices at loop value -2 or +2, the sign convention to be fixed by the hemicube fixture), generate the entries of the N = 1 site tensor on the 12,910,079 slots as signed powers of two times b^(k/4), in pieces indexed by the 64 patterns at one leg exactly as `Inventory.lean` splits the count, and check in the kernel (i) the entry count per histogram class against `histogram`, (ii) the closed cube, the hemicube and the 2D square recomputed from site tensors instead of link rules, (iii) the four fixtures of this row failing. Decisive outcome: the measured kernel time and memory per piece (this row: 0.6 s and under 1.2 GB per piece for counting) decide whether the kernel can hold the N = 1 table at all or whether a certificate checked by a compiled verified checker is needed; a mismatch with any of the three known values rejects the recoupling conventions before anything is built on them. Also write the `brute = pruned` induction (item 4).

Neither row is a step toward an intermediate-coupling inequality by itself; as row 1418 says of its next row 1, this builds a reusable verified component.

RESULT: (a) kernel-checked: counts 1, 15, 30, 5, D_1 = 51 (three routes) and D_2 = 977, 131,072 even subgraphs, 12,910,079 slots, the histogram with label counts 1, 3, 12, 6, 24, 5 and both moments (70 s, 1.18 GB, split into 192 kernel pieces because one evaluation did not finish); (b) kernel-checked: the closed cube at b = 1/16 is 2^(-28) for all 64 face orientations; (c) fixtures C1 (one missing 1/d, on the cube and in the 2D square, b = 3456), C2 (spin-one dropped), C3 (zero denominators; unguarded cross-multiplication accepts 0/0) and C4 (centre twist, pairing sign) all fail as required, axioms none or propext only; new finding: the cube cannot detect a wrong pairing sign, the hemicube (hand value -1/4) does. Open: the Haar moment, link-rule and Schur identities and the reading of the counts are not in Lean (Lemma SM gives the algebra by hand; a mathlib proof is estimated at one row, unchecked); the all-subsets sum for K_{2,2,2,2} is tied to the pruned sum only on the octahedron and by check 1420's C run; no site tensor and no inequality is built.
