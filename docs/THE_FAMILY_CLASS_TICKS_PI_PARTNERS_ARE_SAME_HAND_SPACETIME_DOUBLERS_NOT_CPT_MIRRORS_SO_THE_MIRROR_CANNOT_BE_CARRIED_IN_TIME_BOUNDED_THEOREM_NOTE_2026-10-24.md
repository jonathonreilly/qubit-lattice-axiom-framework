---
claim_id: the_family_class_ticks_pi_partners_are_same_hand_spacetime_doublers_not_cpt_mirrors_so_the_mirror_cannot_be_carried_in_time_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Free light bands of FREEZE (twist-local-single; family-class tick W_F = (-2,1,1)) on CL-1's 2x2x2 cell, CL-1's plain cube tick (eps 0.3) as control, and the one-cube start tick (8 modes, Fock 256). Exact: (1) the kept CPT-type map (U(K) -> U(-K)^+) fixes K = 0, R and quasi-energies 0, pi, so it maps each node into itself; at K = 0 it sends the light q 2 pair onto the q 1 pair. (2) FREEZE has an on-cell spacetime-doubler map S U(K) S^-1 = -U(K + R); the pi partner at R is the light Weyl's doubler with the same hand, turn label, speed and on-cell charges (the commutant is scalar on Pi+). CL-1's plain tick has none. (3) Hand sum rule: net hand at quasi-energy 0 = net hand at pi = nu3, and nu3 = 0 for every circuit of cube-local gates (homotopy). So a mirror at pi alone is impossible for any charges, and the pi gap repeats the 0 gap. (4) Any half-filled vacuum that fills quasi-energy intervals and has no Fermi surface has boundaries at 0 and pi, and exactly one of the two sectors is inverted; no bilinear pairs a light Weyl with its pi partner; the anomaly coefficients of the two sectors are equal. (5) On the one-cube start, an antiunitary time reflection (a signed site permutation) fixes the half-filled vacuum, so a reflection-invariant start state has mirror-symmetric Born record odds. Register readings of the Boyle-Finn-Turok predictions are given as supplied-literature consistency checks. Not covered: interactions, the slab with links, the copy mass on FREEZE, inverted-sector decay rates, cosmological dynamics."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - a_circuit_slab_puts_its_mirror_in_the_other_copy_only_through_a_nonzero_turn_graded_winding_which_forces_equal_flow_at_quasi_energy_pi_and_is_set_by_termination_bounded_theorem_note_2026-10-23
  - a_family_class_tick_keeps_a_96_element_magnetic_group_that_forbids_every_low_energy_rotation_or_lorentz_violating_dispersion_term_below_dimension_six_and_leaves_its_time_reversal_breaking_in_one_chirality_flip_term_bounded_theorem_note_2026-10-24
  - the_adopted_link_rule_puts_one_gauge_field_on_both_slab_walls_so_a_separate_mirror_world_needs_a_new_link_rule_and_a_supplied_temperature_asymmetry_bounded_theorem_note_2026-10-24
runner: scripts/the_family_class_ticks_pi_partners_are_same_hand_spacetime_doublers_not_cpt_mirrors_so_the_mirror_cannot_be_carried_in_time_2026_10_24.py
---

# The family-class tick's pi partners are same-hand spacetime doublers, not CPT mirrors, so the mirror cannot be carried in time

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers, [S] reading.
Runner: runner.py, TOTAL: PASS=16 FAIL=0, 4.2 s, 87 MB peak, 4.8 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120.
It was tested under a unique filename (scratch/mit_test_run.py). Axioms unchanged. No rule proposed or adopted.
The criteria were written before any code ran (criteria_pre_run.txt). Every verdict matched its prediction. Three
runner lines needed fixing before they passed, and none of the fixes changed a claim:
- A1 and A4 first compared node subspaces as vectors. Both nodes span Pi+, so the momentum label is what tells them apart.
- B1 had a normalisation bug in nu3.

## Question (owner, 2026-10-24): "what if the mirror is in time as well?"

There are three parts.
- (1) Are FREEZE's quasi-energy-pi partners the CPT images of the light Weyls? Are they time doublers, and how do they
  couple?
- (2) Can the far-wall mirror be traded for pi-modes within the 0/pi sum rule? Are pi-modes at cell-scale quasi-energy
  decoupled? Do the 0 and pi anomalies cancel?
- (3) Does the CPT-symmetric universe of Boyle-Finn-Turok (2018 PRL; 2022, cited as supplied) fit CL-2's arrow, and do
  the rules contradict its predictions?

Repo first. A git grep of origin/main (docs, scripts) for "CPT-symmetric universe", "time doubler" and "Higashikawa"
found nothing. "Boyle" hits only the older NCG notes, which are unrelated. This note builds on and narrows:
- floquet-pi-slab (the sum rule F_0 = F_pi = W; the pi doubling);
- t-breaking-tick-lowenergy (the 96-element group and its CPT-type map);
- mirror-world (one gauge field on both walls);
- freeze-gapped-partners (net hand bookkeeping at 0 and pi; it already cites Higashikawa-Nakagawa-Ueda 2019);
- light-partner-gap (CL-1's corner partner sits at 2 eps);
- the register lines "cone partners at pi (charged, inverted inertia)" (excluded as dark matter), the neutrino-mass lines,
  the one-cube start, and the tensor and inflaton lines.

## A. What the pi partner is (Q1)

- A1 [T]/[F]. The CPT-type map X (unitary, X U(K) X^-1 = U(-K)^+) sends K to -K and quasi-energy to its negative. It
  fixes K = 0, R, 0 and pi, so it maps each node INTO ITSELF; the node invariance residual is 5e-15.
  - The pi partner is therefore not the light Weyl's CPT image.
  - Inside the K = 0 node, X sends the light q 2 pair onto the q 1 pair, which is the other copy.
  - The CPT image of the light Weyl is the mirror. In the slab, that mirror sits on the far wall: the mirror lives in
    space, not in time.
- A2 [T]/[F]. FREEZE has an exact on-cell spacetime-doubler map, S U_F(K) S^-1 = -U_F(K + R), with residual 2e-14.
  - S shifts the momentum by R = pi(1,1,1) and the quasi-energy by pi.
  - So the pi partners are the light Weyls' doublers in space and time at once: modes that change sign every tick and
    stagger at the cell scale. This is the 4-momentum corner (pi, pi, pi, pi), which is why the hand is kept: there are
    four sign flips, an even number.
- A3 [T]/[F]. S keeps the hand, the turn label and the speed. The node content at K = 0 and at R is identical:
  (q 1, -, 1/sqrt3) and (q 2, +, 1/sqrt3). The pi partner is a COPY of the light Weyl, not a mirror, so there is no
  vector-like pairing.
- A4 [T]/[F]. The on-cell commutant of U_F has dimension 9: a scalar on the light block Pi+, plus 8 dimensions on the
  frozen Pi- block. The Links clause can gauge only update symmetries, so every register dresses the pi partner with the
  light Weyl's charges.
- A5 [T]/[F]. Control: CL-1's plain tick has no doubler map. Its corner partner sits at +-2 eps. The exact pi doubler
  is a property of the family-class tick.

## B. Sum rules: what the pi gap may hold (Q2, first part)

- B1 [T]/[F]. Hand sum rule: net hand at quasi-energy 0 = net hand at pi = nu3, the 3D winding of U(K). In the
  runner's orientation, hand = -nu3. This is the hand analogue of floquet-pi-slab's turn rule (cf. Higashikawa-Nakagawa-
  Ueda 2019, supplied).
  - FREEZE has nu3 = 0.0000, and its node hands sum to 0 at both 0 and pi.
  - Test map: a degree-1 SU(2) map has 1 Weyl at 0 and 7 at pi, with the same net hand (-1) at both.
- B2 [T]. Every circuit of cube-local gates has nu3 = 0. Each gate D(K) C D(K)^+ is homotopic to 1, because U(8) is
  connected. Checked: a random depth-5 circuit gives 0.0000. So for every CL-1-type tick, the net hand vanishes in each
  gap separately.
- B3 [T]. What is allowed. The content at 0 and at pi must each satisfy sum h = nu3 (= 0) and sum f(q, h) = W.
  - A mirror (hand -) at pi alone is impossible for ANY charges: the net hand would be +1 at 0 and -1 at pi. This is
    stronger than floquet-pi-slab B3, which used the turn rule.
  - The only single-Weyl pi content that matches the light (q 2, +) is that same (q 2, +), i.e. its doubler.
  - So the pi gap REPEATS the 0 gap. The mirror must be balanced within the 0 gap (the far wall), and likewise within
    the pi gap.
  - Precisely what is allowed: light (q 2, +) at 0 with its mirror (q 1, -) at 0 on the far wall, and the same pair
    again at pi. Where each pair sits (near or far wall) is a termination choice (floquet-pi-slab C4 and C5).

## C. Low energy (Q2, second part)

- C1 [T]/[F]. FREEZE's light band covers every quasi-energy, because cos theta = mean cos K exactly. Its level sets are
  2-surfaces, except at the points K = 0 (quasi-energy 0) and R (quasi-energy pi).
  - Take a half-filled vacuum that fills quasi-energy intervals and has no Fermi surface. Its filling boundaries must lie
    at 0 AND pi.
  - Boundary types alternate round the circle, so exactly one of the two sectors is INVERTED.
  - With (-pi, 0) filled, a small pair costs +0.070 at 0 and -0.070 at pi.
- C1' [T]. The pi modes are NOT decoupled by sitting at cell-scale quasi-energy. Only mixed 0-pi pairs cost about pi per
  tick. Pairs within the pi sector carry zero net momentum and small net quasi-energy, so they are as light as 0-sector
  pairs, with the opposite sign.
- C2 [T]. No bilinear pairs a light Weyl with its pi partner:
  - the hands are equal, so there is no Dirac mass;
  - q 2 + q 2 = 1 mod 3, and the number charge is a scalar on Pi+, so there is no Majorana term;
  - any such term would also have to carry momentum R and quasi-energy pi.
- C3 [T]. The anomaly coefficients (net hand, sum h q mod 3, sum h q^3 mod 9) are (0, 1, 7) in both sectors, so they are
  EQUAL. The 0 and pi sectors double each other's anomaly and never cancel it. Cancellation happens gap by gap, across
  the walls (B2).
- C4 [S]. Reading. A charged, inverted, light sector that couples identically to the light photon (A4) allows processes
  that conserve quasi-energy and momentum: from the vacuum, a positive-energy 0-sector excitation plus a negative-energy
  pi-sector pair. This is a ghost-type vacuum instability, or generic Floquet heating.
  - This is the register's "inverted inertia" exclusion, now located in the family-class tick, whose pi content is FORCED
    at the free level by F_pi = W != 0.
  - The family-class tick therefore needs its pi sector gapped by interactions, or by a term that breaks S and the axis
    turn. CL-1's plain tick does this, with its partner at 2 eps.
  - The rate is not computed.

## D. The CPT-mirror universe (Q3)

- D1 [T]/[F]. One-cube start tick G: CL-1's tick with every mode antiperiodic around each closed direction. It has
  8 modes, quasi-energies -0.6 (x4) and +0.6 (x4), and a unique half-filled vacuum.
  - 384 signed cube-site permutations reverse the tick.
  - The antiunitary time reflections (types K and K.PH, with det R = +-1) FIX the vacuum. The unitary ones do not: they
    map the sea onto the filled-(0, pi) state.
  - So BFT's boundary condition, a CPT-invariant state at the surface, is automatic for the register's start. It is not
    an extra datum.
- D2 [T]/[F]. Take a start state invariant under the time reflection. Its Born record odds at -t equal those at +t,
  relabelled (t = 1..5). So CL-2's arrow points away from the start surface on both sides, provided "the half-tick
  after" is counted outward from the surface.
- D3 [S]. Information. The two-sided picture keeps the same boundary datum and rewords one clause. It removes no supplied
  datum, so it is NOT less information than the one-sided start. It is also no more.
  - CL-1's split adds modes (an isometry), so the far half is a second history growing outward. It is not G^-1.
  - Nothing on our side can read the far half's records (read once). The two-sided reading makes no prediction from our
    side.
- E1 [T]/[S]. BFT's dark matter is a stable Majorana nu^c at about 4.8e8 GeV. The register CONTRADICTS it as written:
  - the Majorana mass carries Z4 (B - L) charge 2, and neutrinos are Dirac in the Z4 vacuum;
  - breaking Z4 spontaneously gives walls that exceed ZKO by 5e17;
  - stability needs a hand-added parity (owner decision 2, a gate failure) against the cross-copy (nu^c)^4 decay.
- E2 [E]. BFT's massless lightest neutrino is CONSISTENT.
  - The register's one-vertex and far-layer nu^c readings leave neutrinos massless.
  - Normal ordering with m1 = 0 gives sum m = 0.0587 eV (supplied splittings), just below the register's 0.059-0.060 eV
    and below the 0.064 eV bound.
  - It differs from BFT on 0nu-beta-beta: Dirac gives m_ee = 0 exactly, while BFT's Majorana seesaw gives about
    1.5-3.7 meV. That is untested; the bounds are about 30-120 meV.
- E3 [S]. BFT's r ~ 0 is CONSISTENT.
  - There is no inflaton, and one constant gives today's P_t ~5e-122.
  - The fold-inflaton candidate gives r ~1e-8 to 1e-6, below 0.036.
  - Shared gap: neither picture derives the scalar tilt.

## Verdicts (pre-set criteria)

1. Q1. The pi partners are NOT CPT images (FAIL as predicted). Each node is its own CPT image, and the light Weyl's CPT
   image is the q 1 mirror in the other copy. They ARE exact spacetime doublers (PASS): same hand, same charges, a copy,
   not vector-like (FAIL as predicted). They couple to every register exactly like the light Weyl.
2. Q2. The mirror cannot be traded for pi-modes. The hand rule (net hand at 0 = net hand at pi = nu3 = 0 for circuits)
   and the turn rule (F_0 = F_pi = W) both make the pi gap repeat the 0 gap. Pi-modes are not decoupled: they are light
   and, in any nodal half-filled vacuum, one sector is inverted. The 0 and pi anomalies are equal; they double and never
   cancel. FAIL x2, as predicted. New: the forced pi content of the family-class tick is a charged inverted sector, a
   stability problem to solve [S].
3. Q3. The CPT-mirror history fits CL-2 exactly on the one-cube start (PASS). The time reflection is antiunitary and
   fixes the vacuum. It is not less information (FAIL) and makes no new prediction from our side. Of BFT's predictions:
   - dark matter as a stable Majorana nu^c is contradicted (Z4, parity);
   - m1 = 0 and r ~ 0 are consistent;
   - 0nu-beta-beta distinguishes the two pictures.

Overall: "the mirror is in time" FAILS as a way to remove or carry the far-wall mirror. The owner's picture survives in
two weaker forms:
- the mirror is the CPT image, and it sits in space (the far wall);
- the cosmological CPT mirror is allowed but adds nothing.

## Gate

No rule is proposed. A rule that put the mirror at pi would violate the hand sum rule (B3), so it cannot be written
within cube-local circuits. A non-circuit tick with nu3 != 0 makes the 0 gap chiral, but the pi gap then repeats the
same hand, so it still gives no mirror.

## Smuggling review

Supplied:
- FREEZE and its labels;
- CL-1's tick at eps = 0.3;
- the one-cube spin structure;
- the interval-filling vacuum class;
- free fields;
- the BFT predictions;
- the Higashikawa-Nakagawa-Ueda and ghost-instability literature, as readings only;
- the neutrino splittings and the bounds 0.064 eV, r < 0.036 and 0nu-beta-beta.

Forced:
- the CPT node map;
- the doubler S and its kept hand and charges;
- the scalar Pi+ commutant;
- nu3 = 0 for circuits;
- the hand sum rule and the pi-repeats-0 table;
- the boundary alternation (one inverted sector);
- no 0-pi bilinear;
- equal anomalies;
- the antiunitary vacuum-fixing time reflection;
- the mirror-symmetric record odds.

Not shown:
- interacting gapping of the pi sector;
- the decay rate of the inverted sector;
- S with links and the copy mass;
- fillings not defined by quasi-energy (a per-K branch switch either moves the problem to Fermi surfaces at +-pi/2,
  which are again inverted, or is equivalent to the case treated) [S].
