---
claim_id: the_light_copy_carries_a_nonzero_turn_charge_so_a_symmetrically_gapped_mirror_needs_family_count_zero_mod_three_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Conditional arithmetic in a supplied mathematical model: 5 modes per site with Spin(10) on one 16 per family (why-five-modes), CL-1's cell and cube tick with the copy mass, and N families repeated by one uniform rule; the model is not an approved change to the current framework. Exact: the light copy the copy mass leaves carries a nonzero charge q under every three-fold cube turn (q in {1, 2}, never 0). Separately, impose the arithmetic condition A(N, q) = 4Nq = 0 mod 3 for an untwisted retained turn; then 3 divides N. If a fermion-number, Spin(10) or family twist is required to be anomaly-free on the mirror by itself, the tested twists leave that conclusion unchanged. This does not exclude a combined turn-twist symmetry: q + k = 0 mod 3 makes the combined polynomial 4N(q + k) vanish for every N, including N = 1. Whether 't Hooft matching, crystalline equivalence and the instanton, gravitational and cubic normalisations impose the chosen condition on an interacting mirror construction is supplied or argued, not checked here; no physical family-count theorem or mirror-gapping result is established. With family-dependent copy signs the untwisted polynomial vanishes for every N >= 2. Doubling counts and the cone-rule sums give no count."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_light_copy_carries_a_nonzero_turn_charge_so_a_symmetrically_gapped_mirror_needs_family_count_zero_mod_three_2026_10_22.py
---

# The supplied light copy has nonzero turn charge; the untwisted anomaly polynomial vanishes only for family count zero mod three

Claim type: bounded_theorem (conditional arithmetic in a supplied model).
Primary runner: `scripts/the_light_copy_carries_a_nonzero_turn_charge_so_a_symmetrically_gapped_mirror_needs_family_count_zero_mod_three_2026_10_22.py` (29 PASS / 0 FAIL, about 3 s, about 60 MB; exits nonzero on any failed check). The Z-width comparison G1 is computed from the supplied LEP value alone, so since 2026-11-14 it is printed as an estimate and not counted (the source version counted it). Check D9 was added on 2026-11-14.

**Repair 2026-11-14 (PR 10129 second hold, finding F1).** The source required every fermion-number, Spin(10) or family twist to be anomaly-free on the mirror by itself, and concluded that no twist rescues N != 0 mod 3. That implication is false at the level of the note's own arithmetic. Take N = 1, turn charge q = 1 and a twist k = 2 (or q = 2, k = 1): neither 4Nq nor 4Nk vanishes mod 3, but the combined exponent 4N(q + k) does (check D9). This is a counterexample to the exclusion inference, not a construction of a gapped mirror.
- Kept: the computed charges and weights, the modular arithmetic of the untwisted polynomial (D1-D3), and the statement that twists required to be anomaly-free by themselves leave it unchanged (D4, D5, which now name that premise).
- Relabelled: the unit-instanton normalisation, 't Hooft matching, crystalline equivalence and the gravitational and cubic normalisations are supplied or argued inputs, not checked physical consequences.
- Withdrawn, kept here as history: the physical family count of the source title ("a symmetrically gapped mirror needs a family count of 0 mod 3"); "no twist by fermion number, Spin(10) or family rotations rescues any N != 0 mod 3"; "one family is obstructed under every copy-sign choice" as a physical statement; "the rule outputs {3, 6, ...}", "no isolated 4th sequential family" and "shortest consistent is 3"; the claimed narrowing of the families-mod-3 twist loophole; the claimed contradiction of minimal-toe row 15; and the gate PASS.
- Five modes per site, the tick and Spin(10) are a mathematical model, not approved changes to the current framework. The source's wording that they "bend" Qubit and Admissibility is model history, not owner adoption.
The source title stays at the source head recorded in the consolidation map; the title above is narrowed to the arithmetic.

**Scope note (2026-11-14, updated after the second hold).** Later notes outside this PR (#10063, #10064, #10065, #10035, recorded only in the consolidation map) apply a twist k = -q_mirror under which every N_f is allowed when the mirror carries the light copy's turn charge. The first repair recorded that as unreconciled with this note. The difference came from this note's premise that each twist is anomaly-free by itself: without it, the combined polynomial vanishes for every N (D9), which is the arithmetic those notes use. Whether an interacting mirror construction realises or forbids such a combined turn-twist is not settled here.

**Local labels (2026-11-14).** CL-1 here names the source's supplied cube-tick update law (cell, tilings, copy mass), not entry CL-1 of [`CANDIDATE_LAWS.md`](CANDIDATE_LAWS.md); "the register", R1 and the minimal-toe ruleset (its rows 15 and P0) are source-branch texts that are not in this repository. None carries premise weight. families-from-tastes is [#10016](THE_CUBE_TASTES_ARE_TWO_DOUBLETS_AND_NO_SYMMETRY_PROTECTS_A_FAMILY_TRIPLET_BOUNDED_THEOREM_NOTE_2026-10-22.md), carried in this PR. why-five-modes (the five-mode Spin(10) content, outside this theme) and families-mod-3 (#9903, logged in the consolidation map) are not in this repository; what this note takes from them is a supplied input and a historical reported result, unverified here. The main-branch notes meant by THREE_GENERATION_OBSERVABLE / STRUCTURE are [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) and [`THREE_GENERATION_STRUCTURE_NOTE.md`](THREE_GENERATION_STRUCTURE_NOTE.md).

## Question

The minimal-toe ruleset's "shortest" selector predicts one family (row 15, falsified). why-five-modes says the
16 is per site and "families must repeat outside the site modes". This note looks for any non-fitted reason for
exactly three families with 5 modes per site and CL-1's cell and tick. It tests four candidates:
(a) lattice doubling multiplicity; (b) global or discrete anomalies; (c) the cone rule's "charges sum to zero";
(d) fitted counts, which are rejected. The answer below is conditional arithmetic, not such a reason.

## Repo context used

- Register, "Count, conditional" (families-mod-3, PR #9903). With one mode per site and the rung-1 (4,2), the
  turn's mixed anomaly with SU(2) is 4N(q + k) mod 3, where k is a twist. A supplied mirror term fixes k = 2
  (giving N = 0 mod 3), and k = 1 allows every N. This note transposes the mechanism to the 5-mode Spin(10)
  setting. The source said the twist freedom disappears there (D4-D6). That holds only for twists required to be
  anomaly-free by themselves; a combined turn-twist is not excluded (D9).
- families-from-tastes (PR #10016). The CL-1 cell's tastes are E + E. The copy mass leaves one light Dirac
  family. A 1 + 3 occurs only with two modes per site and a tuned triplet mass. This note uses its tick
  construction and reproduces A1-A3 and its E + E.
- why-five-modes: the 16, the Z4 centre, and nu^c (supplied).
- minimal-toe row 15: N_f = 1 from P0.
- Main: THREE_GENERATION_OBSERVABLE / STRUCTURE (the hw = 1 corner triplet). Narrowed by E2 below.

## Setting (supplied mathematical model)

- One 16 of Spin(10) per family per site, with each component a CL-1 lattice mode. This is the Weyl-species
  reading of why-five-modes.
- CL-1's cell: face phase -1, the Margolus cube tick on both tilings, Bloch over 2Z^3, and the copy mass
  (M/4)(1 - s) Re.
- N families with the same tick and the same copy-sign convention ("one update acts the same way everywhere").
- The model is not an approved change to the current framework. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
  select none of five modes per site, this tick, the copy mass or Spin(10).
- The question asked of the model: the mirror 16bars are to be gapped by interactions that keep Spin(10) and at least
  one three-fold turn. The source motivates keeping a turn exact by light-cone isotropy (a families-mod-3 estimate,
  >= alpha/4pi against |c_jk| < 1e-18; a historical reported result, unverified here).

## Exact results (runner)

1. **Tick and rotations (A1-A3).**
   - All 24 cube-centred rotations are tick symmetries, with a site gauge that is unique up to sign.
   - The copy mass keeps exactly the 12 tetrahedral rotations, including all 8 three-fold turns.
   - The velocity matrices form Cl(3), and tr chi = 0.

2. **Turn charge of the light copy (B1-B7).**
   - On each light chirality block (2 spin states) the turn factorises as a spin-1/2 rotation (det 1) times a
     scalar taste phase lambda. So det(V_turn | block) = lambda^2 is invariant under the site-gauge sign, and
     it defines q mod 3.
   - For all 8 turns, both chiralities, both copy-mass signs and eps = 0.3 and 0.5: q is in {1, 2} and never 0.
     q_L = q_R, q(turn^-1) = -q(turn), and q is independent of eps.
   - The copy-sign projector (1 - s) versus (1 + s) picks which E taste stays light (q -> -q). Neither gives 0.
   - Reason: per chirality the taste rep is E of O, whose three-fold-turn character is -1. Its eigenvalues are
     w and w-bar, with no trivial one, and the copy mass keeps the turn, so the light taste is one of them.
   - Without the copy mass both tastes are light, with q = {1, 2}, which sum to 0.

3. **Spin(10) data from weights (C1-C5).**
   - 2T(16)/T(10) = 2 (computed). With the supplied unit-instanton normalisation (argued, not checked) a unit
     instanton has 4 zero modes per 16. In explicit form, an SU(2) in Spin(4) sees 4 doublets, and the zero-mode
     weights sum to 0 on every centraliser Cartan (computed).
   - The centre acts on the 16 as Z4, so Spin(10)-invariant terms have Delta n = 0 mod 4.
   - A lone 16bar has U(1)_F x Spin(10)^2 coefficient 4 (computed). By the cited matching argument, not checked here,
     symmetric gapping of the mirror would have to break U(1)_F.

4. **Anomaly arithmetic (D1-D9).**
   - Supplied step (argued, not checked): if the mirror is gapped keeping Spin(10) and the turn, matching would ask the
     light 't Hooft vertex (4N left-handed zero modes) to be invariant under the kept turn. Its phase is
     lambda^(4N) = w^(4Nq), and the spin parts cancel because the vertex is a Lorentz scalar.
   - Arithmetic (computed): with q != 0, the untwisted condition A(N, q) = 4Nq = 0 mod 3 holds only for
     **N = 0 mod 3: N in {3, 6, 9, ...}, smallest 3** (D1, N <= 12). With the supplied turn-gravity (16Nq) and cubic
     (16Nq^3) normalisations the same set results (D2).
   - Twists required to be anomaly-free on the mirror by themselves leave this unchanged:
     - (i) Fermion number. Such a residual Z_m has m | 4N, and a Z3 inside it exists only if 3 | N (D4).
     - (ii) Spin(10) elements leave the vertex phase at 1 (C2).
     - (iii) Family rotations. The copy-mass tick's exact commutant is dim 1 per mode (D6), so a family twist h
       acts alike on light and mirror. Requiring det(h)^4 = 1 on the mirror leaves the light phase unchanged (D5).
   - **Combined twists are not excluded (D9, 2026-11-14).** With twist charge k, the combined polynomial 4N(q + k)
     vanishes for every N when q + k = 0 mod 3, including N = 1, although at N = 1 neither 4Nq nor 4Nk vanishes on
     its own. So D1's conclusion needs the separately-anomaly-free premise of D4 and D5.
   - Family-dependent copy-sign projectors (q_f = 1 for some families, 2 for others) make the untwisted polynomial
     vanish for every N >= 2; for N = 1 no copy-sign choice does (D7).
   - SU(N)_family gauged on chiral 16s is anomalous for N >= 3 (D8). That gives a constraint against gauging,
     not a count.

5. **(a) Doubling (E1-E3).**
   - Per family, the massless tick gives 2 light 16 + 2 light 16bar (E + E). The copy mass gives 1 + 1.
   - Any rotation-invariant mass gaps E whole. The counts are never 3, and n_16 = n_16bar always
     (Nielsen-Ninomiya, tr chi = 0).
   - The hw = 1 corner triplet carries turn charges {0, 1, 2}, which sum to 0. The polynomial is silent there, so
     that route gets no count from (b) (narrows the main THREE_GENERATION notes).

6. **(c) Cone rule (F1-F2).**
   - For family-blind copies every chirality-weighted charge sum is tr(chi) x tr(Q) = 0 for every N. Linear sums
     are N times the one-family sum, so they cannot select N.
   - N enters only through the multiplicative polynomial of item 4. The cone rule's q_L - q_R = 0 (B4) is what
     makes the light phase equal the mirror's inverse.

## Against measurement (estimate, not a check; printed, not counted)

- LEP N_nu = 2.9840 +- 0.0082. N = 3 is at 2.0 sigma, N = 6 at 368 sigma, and N = 1 at 242 sigma.
- This compares the arithmetic set {3, 6, 9, ...} of D1 with a measured number. It is not a prediction: D1's
  condition is supplied, and a combined twist removes it (D9). The source's "the rule outputs {3, 6, ...}" and
  "it predicts no isolated 4th sequential family" are withdrawn (2026-11-14).

## What each candidate gives

- (a) Doubling multiplicity: **nothing**. The counts are 2 or 1 per family, never 3.
- (b) Discrete anomaly of the kept turn: the untwisted polynomial vanishes only for N = 0 mod 3, with uniform
  copy-sign; twists required to be anomaly-free by themselves leave that unchanged; a combined turn-twist removes it
  (D9). Whether matching imposes the untwisted condition on an interacting mirror is not checked. No physical count.
- (b') SU(3)_family anomaly freedom: **nothing** (it forbids gauging).
- (c) Cone-rule sums: **nothing alone**. They supply q_L = q_R.
- (d) Fitted counts: rejected.

## Theorems vs diagnostics vs supplied inputs

- Exact (runner): A1-A3, B1-B7, C1-C5 (weights and indices), D1-D9 (finite algebra and modular arithmetic), E2, F1.
- Supplied or argued, not checked here; none is a checked physical consequence:
  - crystalline equivalence (Thorngren-Else: the turn as an internal Z3);
  - 't Hooft matching, and whether it imposes the untwisted condition rather than a combined one;
  - the unit-instanton normalisation, and the Ibanez-Ross and Dai-Freed normalisations for Z3 (Hsieh 2018) behind
    the gravitational and cubic conditions;
  - SMG sufficiency in 3+1D (open; the register's chirality wall);
  - Garcia-Etxebarria-Montero, as precedent for "generations = 0 mod 3" (a literature comparison, not used).
- Not tested: lattice-scale (LSM-type) crystalline data at the turn axis; turns about other centres composed
  with translations; interacting corrections to q (q is a discrete eigenvalue, so it is stable while the turn is
  exact and the light block stays gapped from the heavy one); any interacting mirror construction.

## Smuggling review (narrowed 2026-11-14)

1. Numbers chosen: none. q is computed, 4 = 2T(16) is computed from weights with a supplied instanton
   normalisation, and 3 is the order of the cube turn. N_nu is used only in the estimate.
2. Observed structure by name: the 16 and Spin(10) are inputs from why-five-modes (outside this repository). Five
   modes per site, the tick and Spin(10) are a supplied mathematical model, not approved changes to the current
   framework. Family replication with N free is an input. Uniform copy-sign is the source's "one update
   everywhere" (R1), also an input.
3. Predictions: none is claimed. The source listed "N_f = 1 is internally inconsistent with a symmetrically gapped
   mirror", "'shortest consistent' is 3, not 1" and "families come in multiples of 3 (no 4th sequential family)";
   these are withdrawn, because they rest on the separately-anomaly-free premise and on unchecked matching inputs.
   "The light family carries a nonzero crystalline Z3 charge" is the computed turn charge of the supplied model (B3).
   The massless tick (no copy mass) makes the untwisted polynomial vanish for every N (D3).
4. Axioms: none is changed or adopted. The source's "Axioms bent: Qubit (5 modes per site, inherited), and
   Admissibility's rotation clause via the copy mass" describes its model, not an approved change. The minimal
   axioms' Qualification reads: "A choice not fixed by the supplied structure remains a named conditional or open
   dependency."
5. Gate: no gate PASS is claimed (the source's "PASS as a conditional theorem" is withdrawn). The result is
   conditional arithmetic in a supplied model; it is not a derivation of three families, and mirror gapping is not
   supplied by any rule.

## Used / narrowed / withdrawn

- Used: families-from-tastes (tick, E + E, copy mass), why-five-modes (16, Z4; supplied), families-mod-3 (the
  mechanism; its isotropy estimate is historical and unverified here).
- Narrowed: the main hw = 1 triplet notes (the polynomial is silent there, E2).
- Withdrawn (2026-11-14): the source's narrowing of families-mod-3's twist loophole (a combined twist is not
  excluded, D9), and its contradiction of minimal-toe row 15 (no physical count is established here).
