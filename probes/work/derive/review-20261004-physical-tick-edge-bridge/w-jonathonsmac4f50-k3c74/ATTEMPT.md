# J:derive:review-20261004-physical-tick-edge-bridge:a1 -- the physical tick/record/edge bridge

Worker: Claude Sonnet 5.5, one session. Same-family, unrefereed. No HIT is claimed (see section 6).

## 0. Plain-language summary

- The axioms and the three registered primitives do not contain a physical tick, a physical light speed, or the ratio r = a_s/l_P. I could not supply them. I can state exactly which extra premises make "one tick = one edge, so a_tau = a_s/c" follow, and show where the 6-neighbour version of that story contradicts itself.
- Two separate questions were mixed in the Planck packet. (i) Is a tick one edge, a_tau = a_s/c? (ii) Is the edge one Planck length, r = 1? Question (ii) is the same as asking that the framework's Newton coupling, measured in lattice units, equals 1. Nothing registered says so.
- Most of this is already in the repo's earlier work (section 6). What I add is one consolidated premise table and a small exact classification (section 4), not a new physical result.

## 1. What I read (stated as required)

- Full axiom memo `docs/MINIMAL_AXIOMS_2026-06-29.md` (main_wt, a77a3449c9), lines 1-233. The Admissibility section says it does not choose a Hamiltonian or transfer operator, define a time metric, or supply a record-production process (lines 114-123); arrow, time metric and local observability are listed as open gates (185-187); the scale-reference primitive and "natural unit equals the Planck length" are listed as separate (189-190).
- Full `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (lines 1-130): three registered primitives, `scale_reference_primitive` (lines 31-56), `kinetic_isotropy_primitive` (58-96) and `realized_state_primitive` (98-129). Rule 5 (line 14-16): no dimensionless quantity, normalization or dynamics beyond what a primitive declares.
- All six pinned source objects; every sha256 matches at 94083c1bb4c89d746c8e4214b46a260efc16a433 (RECOVERY_STATUS.json). I also read `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` and the companion runner `scripts/min_time_step_tied_to_lattice_edge_by_locality_runner.py` (main_wt HEAD a77a3449c9; the pinned commit is an ancestor, the files I cite were not compared byte for byte past the six pinned ones).

## 2. Setting and premises

Setting: sites Z^3 with nearest-neighbour adjacency, edge length a_s; a tick of duration a_tau; SI constants c, hbar, G; l_P = sqrt(hbar G/c^3), t_P = l_P/c.

Supplied by the axioms: lattice and adjacency (`MINIMAL_AXIOMS_2026-06-29.md:35-41`), a per-site possibility domain, a nearest-neighbour probability rule, permanent records (lines 55-83). No dynamics, no clock.

Supplied by registered primitives: a ruler a^{-1} = M_Pl with no dimensionless content (`PRIMITIVE_REGISTRY_CHECK.md:31-56`); c_t = c_s as matter kinetic normalization of the Euclidean regulator, "one tick is one edge in form" (lines 58-96).

Supplied by lanes (not by axioms or primitives); each is named here so it can be tested:
- (T) a tick is one application of an update map of fixed duration a_tau, with a single clock. This is B-AXIS (`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`, B-AXIS.1-3; a_tau absolute value "supplied/open" at B-AXIS.1b).
- (U_N) strict locality: the one-tick map moves influence only by displacements in a set N of lattice vectors.
- (S) saturation: some signal moves one axis edge in every tick.
- (R) round cone: no physical signal exceeds speed c, and low-energy packets propagate with speed c in every direction.
- (P) physical-c bridge: this c is the SI value.
- (F) record synchrony: one record index = one tick.

## 3. Numbered steps

1. PROVED (algebra) and CHECKED (check.py A1-A2). If a_tau = a_s/c (the packet's supplied tie plus bridge), then a_tau/t_P = a_s/l_P = r, independent of c, hbar, G. This restates the packet and adds nothing.
2. PROVED and CHECKED (A3-A4). r^{-2} = G hbar c^{-3} a_s^{-2} =: G_lat, the Newton coupling in lattice units (hbar = c = a_s = 1), and it is the only dimensionless combination of (G, hbar, c, a_s). So r = 1 is exactly G_lat = 1. READING: this is the content of "the self-consistency question" in `SCALE_REFERENCE_PRIMITIVE_NOTE.md:39-41`.
3. CHECKED (A5-A6). "a^{-1} = kappa M_Pl" gives r = 1/kappa. With M_Pl = sqrt(hbar c/G) r = 1; with the reduced Planck mass r = sqrt(8 pi); with an h-based mass r = 1/sqrt(2 pi). The ruler note does not say which Planck mass is meant, so even the literal reading of the ruler does not fix r = 1 without a convention. READING: whether the ruler is a convention or has content is a choice the owner should state; I did not choose.
4. CHECKED (A7-A8), cross-check with repo. G_lat = 1/(4 pi) gives r = 2 sqrt(pi), the repo's own old mismatch (`PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md:60-62`). The 06-05 same-surface density c_cell/a^2 = 1/(4 l_P^2) gives r = 2 sqrt(c_cell), so r = 1 iff c_cell = 1/4. That premise (BP) is classed a genuine import, not derived, in `PLANCK_ANCHOR_BP_DERIVATION_PROBE_2026-06-05.md:171-190` (verdict "BP-IS-GENUINE-IMPORT"). So the first missing supplier for r = 1 is G_lat = 1 (equivalently c_cell = 1/4 with the BP identification). I did not try to derive it.
5. PROVED (support facts), CHECKED (B1-B3). For the six-neighbour set A the n-tick reach is exactly the l1 octahedron |x|+|y|+|z| <= n. Three axis layers per tick reach the cube max|x_i| <= n. Exact integer-weight updates confirm containment, and positive weights realise the whole octahedron.
6. PROVED (centroid lemma) for linear strictly local updates. If one tick moves content by displacements in N only, then after n ticks a packet started with compact support W has its mean position within W + n conv(N) (a mean of a distribution supported in a convex set lies in that set). For a packet of group velocity v (edges/tick) this gives v in conv(N). This is the argument of campaign8 A5 T1.5 (see section 6); I restate it, I do not claim it.
7. PROVED and CHECKED (B4-B7, D1-D4). For N = A: conv(N) is the octahedron, whose inscribed Euclidean radius is 1/sqrt3, because |v|_1 <= sqrt3 |v|_2 (B7). Hence under (U_A) a round cone of speed v has v <= 1/sqrt3 edge/tick. The packet's own A4 model E = asinh sqrt(sum sin^2 p) has |grad E|_2 <= 1 (what the runner tests) but |grad E|_1 = 3/sqrt7 at p = (pi/6)(1,1,1) and tends to sqrt3 in the infrared along the body diagonal (D1-D2), so it is not the one-tick map of any strictly six-neighbour update. This matches the packet's own disclaimer that the group velocity is a "separate model calculation", and explains why: the sinh model is a quasi-local Euclidean transfer-matrix dispersion, not an automaton tick.
8. PROVED (two inequalities) and CHECKED (C1-C5). Under (T), (U_N), (S), (R), (P), with x := c a_tau/a_s: (S) with "no signal exceeds c" gives x >= 1; (U_N) with (R) gives x <= rho(N), the inscribed radius of conv(N). So x in [1, rho(N)].
   - N = six neighbours: rho = 1/sqrt3, the interval is empty. So (U_A), (S), (R) are jointly inconsistent. The 6-NN BFS tie and a round light cone at speed a_s/a_tau cannot both hold.
   - N = 6 + face diagonals, 6 + body diagonals, all 26, or three axis layers: rho = 1, so x = 1 and a_tau = a_s/c is forced. This is a derived identification given the premises; the premise (U_N) with such N is then the missing supplier.
   - N = two six-neighbour layers: rho = 2/sqrt3, x in [1, 1.155]; a_tau = a_s/c is not forced.
   - If the strictly six-neighbour update is itself the clock, the round-cone tick obeys a_sigma <= a_s/(sqrt3 c) = r t_P/sqrt3. The "minimum step" would be below r t_P by a factor sqrt3, with r still open (C5).
9. CHECKED (E1). Locality does not give saturation: an exact gated six-neighbour update (shift only on odd ticks) satisfies the same reach bound with realised speed exactly 1/2, so a_tau = a_s/(2c) there.
10. CHECKED (E2). A record word has many integer tick embeddings (elapsed ticks 3, 6, 6, 35 for the same four records). Record index = tick number needs (F). This is the `POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md` no-go restated in tick units; nothing new.
11. CHECKED (E3-E5). The generator H = -(1/(2 a_tau)) log(T^2/M_T) rescales as 1/lambda under a_tau -> lambda a_tau (one-clock theorem is tau-relative); two species with speeds 1 and 1/3 give a_tau = a_s/c or a_s/(3c) depending on which is called light; sinh E = gamma |sin p| has infrared speed gamma while the six-neighbour reach set does not depend on gamma, so the tie a_tau = a_s/c needs gamma = 1, which is the kinetic-form clause and covers matter only (`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md:15-17`; photon not named).

## 4. Bounded identification statement (conditional)

Given (T), (U_N), (S), (R), (P) and rho(N) = 1 (for example N = three axis layers), a_tau = a_s/c exactly, hence a_tau = r t_P with r = G_lat^{-1/2}. Every premise other than (P) and the ruler is a lane supply, and none follows from the four axioms.

## 5. First unresolved step and what remains

First unresolved step: step 8's premise (U_N) with rho(N) = 1. The axioms give nearest-neighbour adjacency and no update map (`MINIMAL_AXIOMS_2026-06-29.md:114-123`), and a strictly six-neighbour tick gives an empty interval. A tick = edge identification therefore needs one of:
- a tick built from at least three axis sub-layers (cube reach), or a wider N, supplied as the update; or
- a quasi-local (non-strict) tick, in which case reachability is no bound and the tie rests only on the kinetic-form clause (matter sector).
Then also: (S), (R), (F), the photon/matter universality of c, and the supplier for r (G_lat = 1 or c_cell = 1/4). Work remaining: decide which tick realisation is meant, then test (S) and (R) on it.

## 6. What is new, what is not, prior art

- NOT new: the octahedron-versus-sphere factor 1/sqrt3 and the cube alternative (probes branch, `probes/work/campaign8-tick-moving-records-20261002/A5/REPORT.md` T1.5, lines 89-92; `TIME/T3.md` section 4.1 "Consistency with the night's own upper bound", which states the empty interval a/c <= tau <= a/(sqrt3 c)). The record-vs-clock no-go and tau-relativity (sources). G_lat, 2 sqrt(pi) and BP as the Planck-anchor import (`PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md`, `PLANCK_ANCHOR_BP_DERIVATION_PROBE_2026-06-05.md`). The packet's own r/t_P correction.
- Modest consolidation (my reading, not a HIT): the explicit classification of rho(N) over cubic-symmetric N (step 8) showing the tick = edge tie is forced exactly when rho(N) = 1; the m = 2 minimum of six-neighbour sub-steps; the l1-versus-l2 mismatch inside the companion runner's A4 test (step 7); the ruler-convention table (step 3). The A4 point is arguably new as a statement about that runner, but the packet already disclaims it, so I do not mark it a defect.
- Open PRs: `gh pr list` search shows several "cube tick"/"tick fraction" candidate-law PRs (#9872, #9899, #10020, #10024, #10048, #10053, #9955) that I did not read; any overlap is unchecked.
- claim.py, run_probe.py and commits were not used (no repository writes were permitted in this task).
