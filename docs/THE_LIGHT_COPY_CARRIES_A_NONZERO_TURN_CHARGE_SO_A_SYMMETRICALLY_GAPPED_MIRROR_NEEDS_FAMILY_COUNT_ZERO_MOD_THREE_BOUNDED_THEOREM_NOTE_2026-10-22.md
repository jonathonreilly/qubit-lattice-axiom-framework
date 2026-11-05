---
claim_id: the_light_copy_carries_a_nonzero_turn_charge_so_a_symmetrically_gapped_mirror_needs_family_count_zero_mod_three_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Conditional. Take 5 modes per site with Spin(10) on one 16 per family (why-five-modes), CL-1's cell and cube tick with the copy mass, and N families repeated by one uniform rule. Then the light copy the copy mass leaves carries a nonzero charge q under every three-fold cube turn (exact, q in {1, 2}, never 0). If the mirror 16bars are gapped keeping Spin(10) and at least one turn, the light vertex phase w^(4Nq) must be 1, so N = 0 mod 3, and the smallest N is 3. No twist by fermion number, Spin(10) or family rotations rescues any N != 0 mod 3. One family is obstructed under every copy-sign choice. N = 3 is necessary, not shown sufficient: symmetric mirror gapping (SMG) is cited, not established. Doubling counts and the cone-rule sums give no count."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_light_copy_carries_a_nonzero_turn_charge_so_a_symmetrically_gapped_mirror_needs_family_count_zero_mod_three_2026_10_22.py
---

# The light copy carries a nonzero turn charge, so a symmetrically gapped mirror needs a family count of 0 mod 3

Claim type: bounded_theorem (conditional). Runner: runner.py (PASS=29, FAIL=0, about 3 s, about 60 MB). Through
scripts/runner_cache.execute_runner it gave status ok, exit 0, 4.4 s and 4270 characters of stdout.

## Question

The minimal-toe ruleset's "shortest" selector predicts one family (row 15, falsified). why-five-modes says the
16 is per site and "families must repeat outside the site modes". This note looks for any non-fitted reason for
exactly three families with 5 modes per site and CL-1's cell and tick. It tests four candidates:
(a) lattice doubling multiplicity; (b) global or discrete anomalies; (c) the cone rule's "charges sum to zero";
(d) fitted counts, which are rejected.

## Repo context used

- Register, "Count, conditional" (families-mod-3, PR #9903). With one mode per site and the rung-1 (4,2), the
  turn's mixed anomaly with SU(2) is 4N(q + k) mod 3, where k is a twist. A supplied mirror term fixes k = 2
  (giving N = 0 mod 3), and k = 1 allows every N. This note transposes the mechanism to the 5-mode Spin(10)
  setting, and there the twist freedom disappears (D4-D6).
- families-from-tastes (PR #10016). The CL-1 cell's tastes are E + E. The copy mass leaves one light Dirac
  family. A 1 + 3 occurs only with two modes per site and a tuned triplet mass. This note uses its tick
  construction and reproduces A1-A3 and its E + E.
- why-five-modes: the 16, the Z4 centre, and nu^c.
- minimal-toe row 15: N_f = 1 from P0.
- Main: THREE_GENERATION_OBSERVABLE / STRUCTURE (the hw = 1 corner triplet). Narrowed by E2 below.

## Setting (supplied)

- One 16 of Spin(10) per family per site, with each component a CL-1 lattice mode. This is the Weyl-species
  reading of why-five-modes.
- CL-1's cell: face phase -1, the Margolus cube tick on both tilings, Bloch over 2Z^3, and the copy mass
  (M/4)(1 - s) Re.
- N families with the same tick and the same copy-sign convention ("one update acts the same way everywhere").
- The mirror 16bars are to be gapped by interactions that keep Spin(10) and at least one three-fold turn.
  Keeping a turn exact is needed for light-cone isotropy (families-mod-3 estimate: >= alpha/4pi against
  |c_jk| < 1e-18).

## Exact results (runner)

1. **Tick and rotations (A1-A3).**
   - All 24 cube-centred rotations are tick symmetries, with a site gauge that is unique up to sign.
   - The copy mass keeps exactly the 12 tetrahedral rotations, including all 8 three-fold turns.
   - The velocity matrices form Cl(3), and tr chi = 0.

2. **Turn charge of the light copy (B1-B7). This is the new exact fact.**
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
   - 2T(16)/T(10) = 2, so a unit instanton has 4 zero modes per 16. In explicit form, an SU(2) in Spin(4) sees
     4 doublets, and the zero-mode weights sum to 0 on every centraliser Cartan.
   - The centre acts on the 16 as Z4, so Spin(10)-invariant terms have Delta n = 0 mod 4.
   - A lone 16bar has U(1)_F x Spin(10)^2 = 4, so symmetric mirror gapping must break U(1)_F.

4. **Count condition (D1-D8).**
   - With the mirror gapped symmetrically, the light 't Hooft vertex (4N left-handed zero modes) must be
     invariant under the kept turn. Its phase is lambda^(4N) = w^(4Nq), and the spin parts cancel because the
     vertex is a Lorentz scalar.
   - So 4Nq = 0 mod 3, and with q != 0 this means **N = 0 mod 3: N in {3, 6, 9, ...}, smallest 3.**
   - The turn-gravity condition (16Nq) and the cubic condition (16Nq^3) give the same set; their normalisations
     are cited.
   - Twists cannot rescue N != 0 mod 3:
     - (i) Fermion number. A residual Z_m must be anomaly-free on the mirror, so m | 4N. Then a Z3 inside it
       exists only if 3 | N (D4).
     - (ii) Spin(10) elements leave the vertex phase at 1 (C2).
     - (iii) Family rotations. The copy-mass tick's exact commutant is dim 1 per mode (D6), so a family twist h
       acts alike on light and mirror. Mirror anomaly freedom needs det(h)^4 = 1, which then leaves the light
       phase unchanged (D5).
   - Loophole (D7): family-dependent copy-sign projectors (q_f = 1 for some families, 2 for others) allow every
     N >= 2. **N = 1 is obstructed under every choice.**
   - SU(N)_family gauged on chiral 16s is anomalous for N >= 3 (D8). That gives a constraint against gauging,
     not a count.

5. **(a) Doubling (E1-E3).**
   - Per family, the massless tick gives 2 light 16 + 2 light 16bar (E + E). The copy mass gives 1 + 1.
   - Any rotation-invariant mass gaps E whole. The counts are never 3, and n_16 = n_16bar always
     (Nielsen-Ninomiya, tr chi = 0).
   - The hw = 1 corner triplet carries turn charges {0, 1, 2}, which sum to 0. The anomaly is silent there, so
     that route gets no count from (b) (narrows the main THREE_GENERATION notes).

6. **(c) Cone rule (F1-F2).**
   - For family-blind copies every chirality-weighted charge sum is tr(chi) x tr(Q) = 0 for every N. Linear sums
     are N times the one-family sum, so they cannot select N.
   - The count enters only through the multiplicative vertex phase once the mirror is removed. The cone rule's
     q_L - q_R = 0 (B4) is what makes the light phase equal the mirror's inverse.

## Against measurement (estimate, not a check)

- LEP N_nu = 2.9840 +- 0.0082. N = 3 is at 2.0 sigma, N = 6 at 368 sigma, and N = 1 at 242 sigma.
- Among the allowed set, only 3 survives. This uses no fit: the rule outputs {3, 6, ...}, and measurement
  excludes N >= 6. It also predicts no isolated 4th sequential family.

## What each candidate gives

- (a) Doubling multiplicity: **nothing**. The counts are 2 or 1 per family, never 3.
- (b) Discrete anomaly of the kept turn: **N = 0 mod 3, smallest 3**. Conditional on SMG keeping Spin(10) and one
  turn, and on uniform copy-sign. One family is excluded unconditionally within the setting.
- (b') SU(3)_family anomaly freedom: **nothing** (it forbids gauging).
- (c) Cone-rule sums: **nothing alone**. They supply q_L = q_R.
- (d) Fitted counts: rejected.

## Theorems vs diagnostics vs cited

- Exact (runner): A1-A3, B1-B7, C1-C5, D4-D6 algebra, E2, F1.
- Cited, not rederived:
  - crystalline equivalence (Thorngren-Else: the turn as an internal Z3);
  - 't Hooft matching;
  - Ibanez-Ross and Dai-Freed normalisations for Z3 (Hsieh 2018);
  - SMG sufficiency in 3+1D (open; the register's chirality wall);
  - Garcia-Etxebarria-Montero, as precedent for "generations = 0 mod 3".
- Not tested: lattice-scale (LSM-type) crystalline data at the turn axis; turns about other centres composed
  with translations; interacting corrections to q (q is a discrete eigenvalue, so it is stable while the turn is
  exact and the light block stays gapped from the heavy one).

## Smuggling review / gate

1. Numbers chosen: none. q is computed, 4 = 2T(16) is computed, and 3 is the order of the cube turn. N_nu is used
   only in the estimate.
2. Observed structure by name: none added. The 16 and Spin(10) are inherited from why-five-modes, where they are
   selected (not named) but the per-site placement bends Qubit. Family replication with N free is an input; its
   value is an output. Uniform copy-sign is R1's "one update everywhere", not an observed fact. The borderline
   reading is the same Weyl-species reading why-five-modes uses.
3. Predictions it was not built for:
   - N_f = 1 is internally inconsistent with a symmetrically gapped mirror. This repairs minimal-toe row 15:
     "shortest consistent" is 3, not 1.
   - Families come in multiples of 3 (no 4th sequential family).
   - The massless tick (no copy mass) would allow every N.
   - The light family carries a nonzero crystalline Z3 charge.
   Tested: N = 3 is consistent with the Z width at 2.0 sigma.
4. Axioms bent: Qubit (5 modes per site, inherited), and Admissibility's rotation clause via the copy mass
   (inherited from the register). No new bend.
5. Gate result: **PASS as a conditional theorem**. It is not a derivation of three families. Sufficiency needs
   SMG of N = 3 mirror 16bars keeping Spin(10) and a turn, which no rule yet supplies.

## Used / narrowed / contradicted

- Used: families-from-tastes (tick, E + E, copy mass), why-five-modes (16, Z4), families-mod-3 (mechanism and
  isotropy estimate).
- Narrowed: families-mod-3's twist loophole k = 1. In the 5-mode Spin(10) setting there is no fermion-number Z3
  unless 3 | N, so no supplied mirror-term choice is needed. Also narrowed: the main hw = 1 triplet notes (the
  anomaly is silent there).
- Contradicted: minimal-toe row 15 (P0 + R4 on CL-1's cell gives smallest N = 3, not 1), conditional on SMG.
