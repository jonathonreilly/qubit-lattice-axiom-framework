---
claim_id: chirality_doublers_consolidated_bounded_theorem_note_2026-10-30
claim_type: bounded_theorem
claim_scope: "Consolidation of 57 source notes on one question: Can the lattice support a consistently gauged chiral light sector while removing its mirror and doubler states? Each result carries its own scope below; nothing here is stronger than its source."
---

# Chirality, doublers and mirror removal: consolidated results

**Question.** Can the lattice support a consistently gauged chiral light sector while removing its mirror and doubler states?

**Status authority.** Independent audit lane only. These are author statements for review.

## What this theme found

# Synthesis: chirality, doublers and mirror removal

**Answer: not obtained.** No kept result constructs a consistently gauged chiral light sector in 3+1D with its mirror and doublers removed. What remains is supplied-model, finite, 1+1D or Euclidean-only.

**What failed.** For supplied two-component SU(2) walks on Z^3, net cone chirality at 0 and at pi equals minus W3, and products of coins and shifts have W3 = 0 (#9863). Record and feedback histories (#9895) and the zoom, pumping and mode-number-conserving mirror-gapping routes as written (#9896) give none. The octree ladder needs unbounded range (#9908); rung ladders give a charged tower or a charged mirror at a cut (#9971); smoothed far layers induce a cutoff-scale photon mass in 4D slab models at constant layer fields (#9985); a domain-wall tick puts the mirror on the far wall (#10056), and a strongly coupled far layer only relocates it in a free-slab check (#10060). Gapping the supplied block Hamiltonian's mirror releases vector-like doublers (#9911; toy Monte Carlo #9992). On FREEZE, Schur forbids light-light partner gapping under T and cell translations (#10030), and for free walk-invariant sectors the light W3 blocks the two-cell label escape (#10042). A Floquet slab reaches the other copy only with nonzero turn-graded winding, forcing equal flow at pi (#10064). A bulk tick with that winding has states at every quasi-energy (#10073); its free pi copy is excluded by estimates with supplied numbers (#10072).

**What survives.** The overlap of the cube walk's Euclidean kernel has exact Ginsparg-Wilson chirality without doublers; its chiral content is abelian, Euclidean and not a walk sector (#10049). 3^4 Standard Model anomaly tests are diagnostics (#10052). A toy slab puts the pi flow on the far wall (#10073). The 16-Weyl toy has Z16 index 0 under the unitary Z4s searched and an inconclusive mirror gap (#10004). In 1+1D, supplied unbounded rotors carry an exact chiral U(1) and Gauss law, with Gaussian-sector light content (#9927, logged); a chiral SU(2) x U(1) version cites its flow (#9939, logged).

**Open.** A local gauged measure: the U(1) four-field coefficient does not vanish like p^2 at L <= 24 (#10085). Persistence of the mirror gap (#10004). A forced termination and far-wall gapping of mirror plus pi pair (#10073). Whether partners surviving as propagator zeros are acceptable (#10030). Non-abelian existence and reflection positivity (#10049).

## Results carried with their runners

# Kept results: chirality, doublers and mirror removal

Theme question: can the lattice support a consistently gauged chiral light sector while removing its mirror and doubler states?

Twenty-one of the 57 PRs in this theme are kept below (37%, slightly over a third). Each section gives the note's own scope text verbatim, what kind of statement it is, its dependencies, and the note text verbatim with only the procedure sections (gate, smuggling-review, repo-check, mapping and next-step sections) omitted; the omitted sections are named in each section. Everything not kept is listed in the logged rows with its full scope text, and its note, runner and cache stay on its branch at the recorded commit. Statements here are author statements for independent review; none carries a review verdict.

Logged PRs named as upstream are context, definitions or earlier measurements. Where a statement takes something from one, its Dependencies line says what, and whether a carried runner rechecks it. The kept set is above a quarter because of dependencies, not because many results are exact: #9908 is relied on by #9971; #9993 and #9992 are relied on by #10004; #10041 defines the walk used by #10030, #10042, #10064 and #10073; #10049 is relied on by #10052 and #10056; #10064 and #10072 are relied on by #10073.

## Reading guide and glossary for the quoted note text

All quoted text is the source's own. Terms and labels that need a gloss:

- "cube tick", "register's cube tick": a supplied Margolus-type walk on 2^3 cubes with one fermion mode per site. The notes call it "CL-1" (and #10052 and #10056 also use "CL-1" for the history-level overlap weighting clause of matter) (as in "CL-1's cube tick", "CL-1's site gauges", "CL-1 content"). This is a label collision: in the current candidate-law register (`docs/CANDIDATE_LAWS.md`), "CL-1" is the historical alias of the lossless-influence clause, which does not specify an update rule, and "CL-2" and "CL-3" are the record-removal clause and a pending conservation proposal. Wherever a note says "CL-1" for a tick, read "the supplied cube tick"; wherever a note says "the register" for update, record, following, response or step-bound statements, read "as that note states the candidate-law register", which is not the current register text. See the section "Corrected or replaced claims".
- W3: the Floquet three-dimensional winding number of a tick unitary U(k) on the three-torus; K = 0 and R = pi(1,1,1) are the zone centre and zone corner of the cell; X and M are the other corners.
- Quasi-energy 0 and pi: the two quasi-energy values at which cones of a tick are counted.
- T: the 12 tetrahedral rotations of the cell; T3: the (111) three-fold turn; q: three-fold turn charge of a Weyl node; W_F = (-2, 1, 1): the turn-graded winding of FREEZE.
- CTWIST: the supplied composite twist walk of #10028, U(K) = f + i(h1 tau1 + h2 tau2 + tau3 g.sigma) on the 8 cell states, K the cell momentum, f = (cos K1 + cos K2 + cos K3)/3, h1 - i h2 = (sqrt2/3)(cos K1 + wbar cos K2 + w cos K3), g = sin K / sqrt3, sigma = 2S from the cube tick's velocity matrices, tau3 = (t - t^dag)/(i sqrt3) with t the turn's taste factor (#10028 B; #10041's runner). #10043's atomic form has w and wbar exchanged in its own basis. FREEZE: the supplied rule of #10041 (the sector where the cube tick's chirality disagrees with the walk's does not hop). FREEZE is called "twist-local-single" in some notes.
- "R10" and "R11": internal rule indices used in #10035 and #10043 (R10: the light copy carries a non-zero turn charge so a family count follows; R11: light and mirror sit at different exact momenta). Kept #10041 uses both labels.
- S: the doubler map of FREEZE, S U(K) S^-1 = -U(K + R) (stated in #10070, checked in #10072's runner).
- GW: Ginsparg-Wilson relation. SMG: symmetric mass generation. GK: Grabowska-Kaplan. P_hat: Luscher's projector built from sign(H). "3450": the charge pattern (3,4 | 5,0). "Pair square", "block-local quartic", "charge-4 term": four-fermion terms named in the notes.
- Tags [T], [F], [E], [S] in some notes mean exact, finite diagnostic, estimate and supplied; in #10056, #10058 and #10060 [T]/[F] can instead mean pass/fail of a pre-set criterion, as each note states. Letter-number items (A1, B2, ...) are the notes' own check indices.

## Kept sections

### #9863: winding fixes net cone chirality at quasi-energy 0 and pi

**Statement (the note's own `claim_scope`, verbatim).**

> For supplied two-component SU(2) walks on Z^3, the net chirality of the Weyl cones at quasi-energy 0 equals that at quasi-energy pi and equals minus the 3D winding W3; products of coins and coin-conditioned shifts have W3 = 0, and a supplied quasi-local walk with W3 = -1 has a single cone at quasi-energy 0 and an exponential tail; no matter content, physical chirality or adopted tick update is established.

**Kind of statement.** Exact finite/algebraic result (a degree theorem) for supplied two-component SU(2) walks on Z^3, with numerical diagnostics on the named walks. The walk with a single cone is a supplied quasi-local example, not finite range.

**Dependencies.** Uses the vanishing of SK1 of the Laurent ring C[Z^3] as an external input, cited and not rederived. Upstream: the minimal axioms and the candidate-law register (zero premise weight; neither fixes a tick). No other PR.

**Runner.** [`tick_update_winding_fixes_net_cone_chirality_at_quasi_energy_zero_and_pi_2026_10_21.py`](../scripts/tick_update_winding_fixes_net_cone_chirality_at_quasi_energy_zero_and_pi_2026_10_21.py); cached output [`tick_update_winding_fixes_net_cone_chirality_at_quasi_energy_zero_and_pi_2026_10_21.txt`](../logs/runner-cache/tick_update_winding_fixes_net_cone_chirality_at_quasi_energy_zero_and_pi_2026_10_21.txt); source note at head `6fe5fbe995` of branch `claude/toe-chirality-20261021`: `docs/TICK_UPDATE_WINDING_FIXES_NET_CONE_CHIRALITY_AT_QUASI_ENERGY_ZERO_AND_PI_BOUNDED_THEOREM_NOTE_2026-10-21.md`.

**Note text, verbatim** (title line dropped; no section omitted). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem.
Primary runner: `scripts/tick_update_winding_fixes_net_cone_chirality_at_quasi_energy_zero_and_pi_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight, and no law there fixes the tick update. This note asks how far a two-component tick on Z^3 can carry an unpaired Weyl cone. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the walks used.

##### The degree theorem

A cone at k0 with U(k0) = s I (s = +1 at quasi-energy 0, s = -1 at pi) has chirality sign det M, where U(k0 + q) = s(1 - i sum M_ij q_j sigma_i + O(q^2)). For U(k) in SU(2) the cones are the preimages of +I and -I of a map from the three-torus to the three-sphere. Each preimage count, weighted by sign, is the degree, so the net chirality at 0 equals that at pi and equals -W3.

A product of coins and coin-conditioned shifts is a product of one-variable loops, so its degree is 0. The runner finds W3 = -3.7e-16, -2.2e-17 and -1.8e-15 for the split-step walk S_z S_y S_x, a random-coin walk and a diagonal-shift walk, and -2.7e-17 for the eight-mode block candidate. The split-step walk has 8 cones at 0 and 8 at pi, four of each chirality in each set, and no others: off those 16 points, 1 - |cos w| is at least 5.48e-3 on a 60^3 grid. That every finite-range walk has W3 = 0 follows from the vanishing of SK1 of the Laurent ring C[Z^3]; this input is cited, not rederived.

##### A walk with one cone at quasi-energy 0

The quasi-local walk U = (n0 - i n.sigma)/|n| has net chirality -W3 at both 0 and pi for every mass parameter m, for example W3 = -1, +2, 0 and -1 at m = 2, 0.5, 4.5 and -2. At m = -2 it has exactly one cone at quasi-energy 0, at k = 0 with chirality +1, and all seven doublers at pi (four of +, three of -). It is covariant under all 24 cube rotations to 6.8e-16. Its weight beyond range R falls as exp(-1.66 R) (1.4e-2 at R = 1, 3.4e-11 at R = 12), so it is not finite range. By additivity, U_split^dag U_{m=2} has W3 = -1 and equals -I somewhere, so no W3 = 0 walk lies within operator distance 2 of it. Modes 0.05 from a pi cone have relay energy within 0.06 of pi, outside the domain of the switching law.

##### Scope

Supplied: the walks, the quasi-local walk, its parameter m and its exponential tail. The vanishing of SK1 is an external input. No matter content, physical chirality or adopted tick update is established.

---

### #9895: record and feedback histories of block ticks have zero flow index

**Statement (the note's own `claim_scope`, verbatim).**

> For supplied finite-range block ticks and frames on Z and Z^3, every history chosen by records, conditional odds, c-number link feedback or an adversary has flow index 0 (and W3 = 0 for periodic histories), so the record, following and response laws of the candidate laws register give no net chirality; a supplied conditioning variant keeps only an index-0 coherent part, and c-number feedback breaks the following law's Born tracking in a finite diagnostic; no matter content, chiral mechanism or adopted fix is established.

**Kind of statement.** Exact (index and algebra) argument for supplied finite-range block ticks and frames, with numerical diagnostics for the conditioning variant and for c-number feedback. For non-periodic histories the identification of chirality with the flow index is, in the note's words, a definition supported by controls, resting on a magnetic flow-index identity checked numerically only. Dependent on the record, following and response laws as the note states them.

**Dependencies.** Cited, not rederived: GNVW integrality, Avron-Seiler-Simon, Stinespring uniqueness. Uses the periodic-history winding result of #9863 (W3 = 0 for products of coins and shifts) and the same quasi-local control walk. The record, following and response laws are read as the note states them from the candidate-law register; they are not in the current register text (see the section "Corrected or replaced claims").

**Runner.** [`record_and_feedback_histories_of_block_ticks_have_zero_flow_index_2026_10_21.py`](../scripts/record_and_feedback_histories_of_block_ticks_have_zero_flow_index_2026_10_21.py); cached output [`record_and_feedback_histories_of_block_ticks_have_zero_flow_index_2026_10_21.txt`](../logs/runner-cache/record_and_feedback_histories_of_block_ticks_have_zero_flow_index_2026_10_21.txt); source note at head `607d10366c` of branch `claude/toe-records-chirality-20261021`: `docs/RECORD_AND_FEEDBACK_HISTORIES_OF_BLOCK_TICKS_HAVE_ZERO_FLOW_INDEX_BOUNDED_THEOREM_NOTE_2026-10-21.md`.

**Note text, verbatim** (title line dropped; no section omitted). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem.
Primary runner: `scripts/record_and_feedback_histories_of_block_ticks_have_zero_flow_index_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its record, following and response laws break the translation invariance, the fixed tick and the state-independent update that the free-circuit winding result assumes. This note asks whether that lets the layer carry net chirality. It does not. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used.

##### Statement

For a finite-range single-particle unitary V, the flow is the net probability crossing a cut from the uniform state. Every product of block layers of a fixed tiling and diagonal frames has flow 0, however each factor is chosen. Within the update, record, following and response laws of the register, every realised history is such a product, so the layer gives no net chirality in any history. Coherent chirality from extra registers needs registers that are coherent, blank and fermionic with the matter's charges, which records are not.

##### Derivation

Pathwise flow. The flow is additive under products, 0 on any block-diagonal layer (each block is a finite trace) and 0 on any frame. Its integrality is the cited GNVW index. So the flow of a product of block layers and frames is 0 whatever selects the factors: the actual configuration, the conditional odds, records or an adversary. For periodic histories the flow equals W1 = n_R(w) - n_L(w) at every quasi-energy w. In 3D every factor is contractible, so W3 = 0 for every periodic history. For non-periodic histories the note uses a magnetic flow index: thread flux N_phi through a transverse torus and take the flow along z. Block circuits give 0. For a translation-invariant walk it equals W3 N_phi; this identity is checked numerically, not proved in general.

Effective dynamics. The flow is affine in mixtures. The Born mean over the configuration process is a mixture of index-0 histories, so its flow is 0; its weights are quadratic in the state, so it is not a channel. The Born mean of the conditional odds is the one-body state, which evolves as gamma(t) = V_hist gamma(0) V_hist^dag.

Conditioning variant. The register forbids records that condition the odds. If they did, at rate kappa per half-tick with outcome-dependent index-0 feedback, the coherent part would be exactly (1 - kappa)^n times the free tick: a conditioning event leaves a configuration-diagonal state, which cannot regrow coherence beyond its light cone. Any chirality then sits in the decohered fraction. The argument does not depend on dimension.

Averages. Let K = sum_j p_j U_j with every U_j of index 0 and range at most r. If K is within delta of a unitary U of range at most r, then |ind U| <= 2n sqrt(2 delta) with n = 2rd. So ind U = 0 for delta < 1/(8n^2), and a K whose determinant has a point-gap winding is at least 1/(8n^2) from every range-r unitary. Two-term mixtures never wind. This bound is derived here and has not been compared with the literature.

Register bypass. If a finite-depth circuit on matter plus fresh registers induces a unitary chiral map on the matter, then by the cited Stinespring uniqueness the register output is independent of the matter, so the registers are not records. Fermion parity and charge rule out links and records as carriers of the compensating flow.

Covariance. The following law is label-equivariant and the source and link response transform covariantly, so the whole layer is inversion covariant. Inversion-symmetric initial odds give an inversion-symmetric law of histories. Chiral initial odds change which modes are occupied, not the index.

Born tracking. If links are c-numbers that follow the actual configuration, the update depends on that configuration, and the realised odds then carry information about it. This breaks the following law's statement that the configuration is distributed as its odds. With quantised links the joint update is a fixed unitary and the statement holds exactly; that fix is not adopted here.

##### Checks

The runner gives 21 PASS and 0 FAIL. These are finite diagnostics of supplied models.

- 1D free two-site tick: det U(k) is constant (max |W1| 4.3e-21), and crossings are balanced (1, 1) at every quasi-energy tested.
- Full layer on a ring of 40 sites with 2 fermion relays over 6 ticks: every realised history is a free block circuit to 1.1e-15, and every flow is 0 to 4e-16. That includes an adversary choosing bond phases to push right, which visibly moves the odds (Born mean position 39.00 against 54.05). Transport marginals are exact to 9.8e-15.
- Exact branching on a ring of 8 sites with 2 relays over 4 half-ticks: without feedback the law of the configuration equals the Born mean of the odds to 2.1e-15. With c-number feedback the total variation is 6.7e-3 at g^2 = 0.3 and 2.9e-2 at g^2 = 1, and 0.89 given the link history, over 237 histories. The layer is inversion covariant to 5.6e-17.
- Conditioning variant on a ring of 48 sites: the infinite-temperature drift is kappa/2 per half-tick, and long-range coherence is (1 - kappa)^6 times the free value (1, 0.941480, 0.531441, 0).
- 2,500 mixtures of depth-4 index-0 circuits: 145 wind, none with two terms. Every winding mixture is at least 0.871 from unitary, against the bound 0.0020.
- Register bypass: matter flow +1, register flow -1, registers left blank.
- 3D: the register's update on the 2^3 cell reproduces cos w = A S(k) - B to 9.0e-16. W3 is 4.6e-12 with random frames and 2.3e-12 over a 3-tick history with different frames, masses and steps. In a random frame field the magnetic flow winding is 6.3e-17 with crossings of w = 0 balanced at (2, 2). The quasi-local control walk gives W3 = -1, +2, 0 at m = -2, 0.5, 4.5, and windings -1, -2, +2, 0 matching W3 N_phi.

##### Against measurement (estimates)

Oscillation visibility of at least 0.9 over 180 km, with a lattice spacing of 5 l_P supplied, bounds a conditioning rate at kappa < 2.4e-41 per half-tick. Index 0 in every charge sector puts a light mirror partner beside each left-handed neutrino. That gives N_nu = 6 against the LEP value 2.9840 +- 0.0082, about 368 sigma away. Averaging can damp one chirality, but it removes no states, so the same count excludes chiral dephasing.

##### Boundary

Supplied: the 1D two-site analogue, the packets, the link reading of the response law with its current, the length response, the adversary's objective, the conditioning variant (which the register forbids), the mixture ensemble, the random frames and magnetic translations, and all measured inputs. Cited, not rederived: integrality of the flow (GNVW; Avron-Seiler-Simon), Stinespring uniqueness and the general magnetic flow identity. For non-periodic histories, identifying chirality with the flow index is a definition supported by the controls, not a derivation. The result is negative for chirality from the record layer under the current laws. No matter content, chiral mechanism or adopted fix is established.

---

### #9896: wall, pump and mirror-gapping routes under the candidate laws

**Statement (the note's own `claim_scope`, verbatim).**

> For the update of the candidate laws register and supplied wall models, the zoom ladder keeps W3 and is locked to momentum, the step pi/2 tick has index 0 at quasi-energy 0 and pi in every site-phase background, and exact mode number with the mirror reflection forbids gapping the mirror alone, so none of the three routes gives net chirality under the register as written; a supplied internal-index wall binds Weyl content at its ends; no chiral family, gapped mirror phase or adopted rule is established.

**Kind of statement.** Exact finite results and diagnostics on the update as the note states it and on supplied wall models; a no-go for three routes as written. The oriented internal-index wall is a supplied rule: chirality is accommodated by it, not derived. Cites the vanishing of SK1 and 't Hooft anomaly matching.

**Dependencies.** Uses the winding result of #9863 (zoom keeps W3). Same tick algebra as #9884 and #9905 (both logged); those notes are not named by this one. The register update is as the note states it.

**Runner.** [`wall_pump_and_mirror_gapping_routes_to_chirality_under_the_candidate_laws_2026_10_21.py`](../scripts/wall_pump_and_mirror_gapping_routes_to_chirality_under_the_candidate_laws_2026_10_21.py); cached output [`wall_pump_and_mirror_gapping_routes_to_chirality_under_the_candidate_laws_2026_10_21.txt`](../logs/runner-cache/wall_pump_and_mirror_gapping_routes_to_chirality_under_the_candidate_laws_2026_10_21.txt); source note at head `4663f78785` of branch `claude/toe-chiral-wall-20261021`: `docs/WALL_PUMP_AND_MIRROR_GAPPING_ROUTES_TO_CHIRALITY_UNDER_THE_CANDIDATE_LAWS_BOUNDED_THEOREM_NOTE_2026-10-21.md`.

**Note text, verbatim** (title line dropped; no section omitted). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem.
Primary runner: `scripts/wall_pump_and_mirror_gapping_routes_to_chirality_under_the_candidate_laws_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. This note tests three routes to net chirality against it: a domain wall along an internal or zoom coordinate, Floquet pumping between quasi-energy 0 and pi, and gapping the mirror through the response law. None works with the register as written. A wall along a supplied internal index does bind Weyl content at its ends, but only with rules the register does not contain. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used.

##### Statement

1. Zooming to the next rung keeps W3, and the zoom level is locked to momentum, so no rung holds a light field down to k = 0.
2. At step pi/2 the tick is a product of two traceless reflections, and its index at quasi-energy 0 and pi is 0 in every site-phase link background.
3. The register's laws conserve the total mode number N exactly. Every mass that keeps SU(2)_even x SU(2)_odd pairs the family with the mirror, and the exact mirror reflection maps one onto the other, so no history allowed by the register gaps the mirror alone.
4. A Wilson-Dirac chain along a supplied internal index, built from the tick's own algebra, binds left-handed content at one end and right-handed at the other.

##### Derivation

Finite circuits. A finite product of block-local unitaries has W3 = 0 and W1 = 0 at any depth, step, mass, link phases or rung, because each factor deforms to a constant in the connected group U(n). The same holds sector by sector for a symmetry carried through the factors. That finite-range non-circuit unitaries also have W3 = 0 is the cited vanishing of SK1(C[Z^3]).

Zoom. Folding a walk to the next rung leaves W3 unchanged. In the Haar multiresolution the weight of momentum k on level n is f_n(k) = sin^4(2^(n-2) k)/(4^(n-1) sin^2(k/2)), at most (pi^2/4) 4^(n-2) k^2, and the profile moves one level per octave of k. Carrying a 2^n-site cell's internal index unchanged to the next cell is a nearest-neighbour swap circuit of depth 2^(n+1) - 1, so the fine light cone is kept.

The tick's own chirality operator. At K = 0 the tick gives {A_a, A_b} = 2c^2 delta_ab and mass matrix beta = W. Then g5 = -i A1 A2 A3/c^3 is a traceless 8-site block operator, and the commutant is M_2, the copy factor.

Wall ends. For a Wilson-Dirac chain along an internal index built from (A_a, W), the near end holds the X = -1 space of X = i beta' G4', where X commutes with every A_a and anticommutes with beta'. With X = -g5 both copies bind left-handed at one end and right-handed at the other, and all 24 rotations survive. With a copy-mixing mass W s1 and X = -s3 one whole copy binds at step pi/2; there C3 turns the mass by 120 degrees, so rotations survive only at long wavelength. The end brings back doublers at X, M and R unless tau(2 - m0) stays below the tick's smallest doubler gap, about 1.15 eps.

Two reflections. For U = R1 R2, tr R1 on the U = +1 space is (tr R1 + tr R2)/2 and on U = -1 it is (tr R1 - tr R2)/2. At step pi/2 the tick is W_o W_e with W_o U W_o = U^dag, a Floquet Ginsparg-Wilson form, and both W stay traceless reflections under any site-phase links. So the index at 0 and pi is 0. The 2D overlap operator gets a nonzero index only because sign(H_W) is not ultralocal.

Mirror gapping. Every term of the register's update and response commutes with N. With c-number links every realised history is a free block circuit, so the response law has no four-fermion vertex. One family with a right-handed neutrino has N-Y^2 anomaly -2 and N-SU(2)^2 anomaly +2, with the mirror opposite. With N and Y exact on-site, the free case is ruled out sector by sector; the interacting case uses cited 't Hooft anomaly matching. An instanton vertex changes N by 4 per family, so a gapping term must break U(1)_N to at most Z_k with k dividing 4. The mirror reflection M = (odd rotation)(inversion) is exact at every step and mass and maps the family onto the mirror on the same cells. The register states that inversion swaps left and right; in fact inversion alone swaps SU(2)_even and SU(2)_odd and leaves the copy label fixed, and M is the symmetry that exchanges family and mirror.

Floquet pumping in the 3D bulk is forbidden by the finite-circuit result. An effective 3D unitary with W3 nonzero exists only at the end of a 4D bulk, so that route reduces to the wall.

##### Checks

The runner gives 18 PASS and 0 FAIL. These are finite diagnostics of supplied models.

- Zoom: a quasi-local W3 = -1 walk folded to 16 bands gives -0.999992 then -0.999995, and the register's tick gives 3.1e-20. The Haar formula holds to 2e-15, with mean levels 11.148, 10.148, 9.148, 8.149, 7.149 at successive octaves. Swap depths are 3, 7, 15.
- 1D wall at step 0.30: layer 0 holds one right-mover crossing w = 0 only at k = 0 and the last layer one left-mover, with leakage ratio 0.4000 per layer.
- Tick algebra at steps pi/2 and 0.04 (c = 0.5774, 0.0231); with X = -g5 the end Berry fluxes are +-2.000 at both steps and both orientations.
- Doublers: off K = 0 the ratio of end to bare |w| is 0.0004 at eps = 0.04, tau = 0.6 (doublers return) and 0.81 at tau = 0.02. The copy wall at step pi/2 gives sector fluxes +-1.0, doublers gapped at 0.85, and is symmetric under M with layer reversal to 8.9e-11.
- On the rung-1 cell, one (4,2), the plain end has SU(4)^3 anomaly 4. An end with an involution Xi on (4,2,1) + (4,1,2) is anomaly-free, but that content is not in the rung-1 cell.
- Two-reflection traces are exact integers. On a 4^3 torus at step pi/2 the free tick has dimensions (8, 8) at 0 and pi with W_o-traces 0, and random links give (0, 0). The 2D overlap gives index 0, -1, -2 in flux 0, 1, 2 with a far element 4.0e-3.
- N is exact; a four-mode term has [N, O] = -4 O. The 4 symmetric masses all anticommute with s3. The mirror reflection is exact to 4e-15.

##### Against measurement (estimates)

A Planck-suppressed term changing N by 4 gives a proton lifetime near 8e42 yr, against the bound of 2.4e34 yr. A massless mirror coupled through sphalerons would thermalise and add Delta N_eff of about 1.04, against N_eff = 2.99 +- 0.17, so it is excluded and the mirror must be gapped. A leakage mass below 0.05 eV at |1 - m0| = 0.4 and cutoff M_P/3 needs at least 73 layers; at m0 = r the chain dimerises and the end modes are exact for any length of at least 2. The copy wall needs step pi/2, which the register's bound eps < 0.04 excludes.

##### Boundary

Supplied: the internal index carried in parallel, the synthetic mass beta', m0, r, tau, the layer count, Xi, the four-mode term changing N by 4 and its symmetry, and the wall orientation, which is where handedness enters. Cited, not rederived: the vanishing of SK1(C[Z^3]), 't Hooft anomaly matching and the existence of a gapped symmetric mirror phase. No interacting test of the gapped mirror was run. Under the register as written all three routes give no net chirality. Chirality is accommodated by an oriented supplied rule, not derived. No chiral family, gapped mirror phase or adopted rule is established.

---

### #9908: octree ladder gives one fine chirality only by a swindle with unbounded range

**Statement (the note's own `claim_scope`, verbatim).**

> For a supplied octree ladder (coarse cells of the nested tilings as extra sites, every rung running the register's cube tick at the fine step, cells coupled to their eight children through X = W(1 - g5)/2), with a copy mass above the exchange one light Weyl field of one handedness sits on the fine lattice and its mirror on the top rung; with infinitely many rungs the ladder stays unitary and the mirror sits on no finite rung, but only by an Eilenberg swindle in which rung j acts across 2^(j+2) sites, and any bounded truncation restores it; the ladder supplies no tilt, its one exact charge is anomalous, and it gives 1 generation; the coarse sites, the coupling and any adopted rule are not established.

**Kind of statement.** Dependent on a supplied model: the octree ladder adds coarse cells as extra sites (a change to the lattice and qubit axioms in the note's words). Exact kernel/index statements and finite numerical checks; the swindle statement uses the cited GNVW index theorem.

**Dependencies.** Same zoom-ladder and wall-end setting as #9896 and same copy-mass tick algebra as #9906 (logged); neither is named by this note. Relied on by #9971 and by the logged #9912.

**Runner.** [`octree_ladder_of_cube_ticks_gives_one_fine_chirality_only_by_a_swindle_with_unbounded_range_2026_10_21.py`](../scripts/octree_ladder_of_cube_ticks_gives_one_fine_chirality_only_by_a_swindle_with_unbounded_range_2026_10_21.py); cached output [`octree_ladder_of_cube_ticks_gives_one_fine_chirality_only_by_a_swindle_with_unbounded_range_2026_10_21.txt`](../logs/runner-cache/octree_ladder_of_cube_ticks_gives_one_fine_chirality_only_by_a_swindle_with_unbounded_range_2026_10_21.txt); source note at head `e1d4b8d36b` of branch `claude/toe-octree-unify-20261021`: `docs/OCTREE_LADDER_OF_CUBE_TICKS_GIVES_ONE_FINE_CHIRALITY_ONLY_BY_A_SWINDLE_WITH_UNBOUNDED_RANGE_BOUNDED_THEOREM_NOTE_2026-10-21.md`.

**Note text, verbatim** (title line dropped; no section omitted). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem.
Primary runner: `scripts/octree_ladder_of_cube_ticks_gives_one_fine_chirality_only_by_a_swindle_with_unbounded_range_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight and says a finite-range update gives no net chirality at any rung. This note builds a ladder in which the coarse cells of the nested tilings are themselves sites, and asks whether it gives one chirality on the fine lattice, a spectral tilt, or gauge and generation content. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) contain no coarse sites; adding them changes the Lattice and Qubit axioms and breaks nearest-neighbour admissibility in physical distance.

##### Statement

Supplied: rung j's cells are the 2^(j+1) blocks of the nested tilings, one mode per corner; each rung runs the register's cube tick at the fine step st; each cell exchanges with the same corner of its 8 children (amplitude 1/sqrt8) through X = (W + iG4)/2 = W(1 - g5)/2, with exchange kappa = 0.5 and copy mass M = st > kappa st.

1. The tick supplies its own fifth matrix G4 = i W g5 and its own isotropic Wilson term (K^2/6) W, and the copy mass is a Dirac mass on copy 1.
2. The exchange is H5 = T + T^+ with T an isometry, so H5^3 = H5 and the kernel holds exactly 8 modes per fine cell for every number of rungs R. The ladder above rung 1 is the ladder on a lattice twice as coarse.
3. With the copy mass, the fine rung carries Weyl index +1 and the top rung -1; without it, +2 and -2.
4. With infinitely many rungs the ladder is unitary and the mirror sits on no finite rung, by an Eilenberg swindle; bounded range restores the mirror.
5. The only block-local operator commuting with every ladder block is the identity, so total mode number N is the one exact charge, and it sits on one Weyl field of one handedness (anomalous). The generation count is 1 (2 without the copy mass).

##### Derivation

Unitarity. |H5| = 1 gives exp(-i tau H5) = 1 - i sin(tau) H5 + (cos tau - 1) H5^2, and every rung tick is a block unitary, so the ladder is a quasi-free automorphism for any number of rungs.

Swindle. Three cell-child swap layers give Shift_j x Shift_(j+1)^-1 exactly, and the depth-6 circuit gives Shift on rung 0 and the identity on every other rung. Stopping the circuit at rung 2, which bounds its range, brings Shift_2^-1 back on the cut rung. So the ladder evades the conclusion of Nielsen-Ninomiya only by giving up bounded physical range: rung j acts across 2^(j+2) sites. With bounded range and bounded mode density the cited GNVW index puts the mirror back on the truncation rungs.

Mirror decoupling. At fixed physical momentum the mirror's energy is 2^R times the boundary's, so its light states fill a ball shrinking as 2^-R and its share of phase space falls as 8^-R. At zero momentum the light chain decouples exactly. A species mass mu pairs boundary and mirror into a residual mass falling by mu/(kappa st) per rung. The fine rate is what hides the mirror: at the zoom rate 2^-j it stays light on coarse rungs.

No tilt. A white start stays white, since an ensemble proportional to the identity is invariant. A rung-j cell is shared by 8^j fine sites, so correlations carried through the tree contribute at most |p|^3 in 3D (|p|^1 in 1D, so 1D toys would mislead).

##### Checks

The runner gives `TOTAL: PASS=20 FAIL=0` in 20.1 s.

- A1: the light algebra, G4 anticommuting with a_i and W, X^2 = 0, X X^+ = P+, X^+ X = P- (errors 2e-9, 2e-9, 3e-10).
- A2: K^2 Wilson coefficient 0.1665, spread 8e-8. A3: the copy projector commutes with W, a_i, g5; the copy mass is -M P1 W.
- B1: real space (576 modes) equals the momentum tree to 2e-15; kernel 512 = 8 x 64 at R = 1, 2. B2: self-similarity residual 0 at R = 2, 3.
- C1: Berry flux (2.0, -2.0) with no copy mass; (1.0, -1.0) at R = 1, 2; +1.0 on rung 0 at R = 3; (1.0, -1.0) for the discrete-time ladder.
- C2: bulk gap 0.416, 0.389 st; middle-rung weight below 0.25 st at most 1.6e-3; mirror over boundary energy 1.99 (R = 1), 3.94 (R = 2).
- D1: the boundary state's top-rung weight at |q_R| = 0.5 is 3.2e-4, 7.8e-9, 1.3e-14 (predicted 4.3e-4, 1.2e-8, 2.0e-14); the mirror's weight on the light rung-0 node 1e-2, 1e-5, 5e-8.
- D2: |E| < 4e-11 at mu = 0 for R = 1, 4, 16; at mu = 0.2 st the residual mass ratio per rung is 0.3995.
- D3: weight by rung at the zoom rate [2.0, 0.01, 0.68, 3.31] against [2.0, 0.0, 0.0, 0.0] at the fine rate.
- E1, E2: unitarity; shifts by rung [4095, 0, 0, 0] for the full circuit and [4095, 0, 1, 0] when stopped.
- E3: at st = 0.3, R = 3 on 32^3 sites the support grows 4 sites per tick against the fine cone's 2; probability beyond the fine cone is 8e-8, 3e-8, 5e-8 from a one-cell source and at most 1e-10 from a smooth source.
- F1: rung-1 admixture over q^4 is 0.1106 to 0.1108 (1/9) and the velocity shift over q^2 is -0.0416 (-0.0417), so dv/v = -(ka)^2/2.
- G1: on 40^3 sites the rung-0 density has a white floor of 2.4e-3 (index tends to 0), the all-rung density has index 1.92 (tends to 2).
- H1: commutant dimension 1. H3: generation count 1, never 3.
- F2, F3, H2: the estimates below.

Estimates (not checks). With a = sqrt(8 pi) Planck lengths, at 1.4 PeV the admixture is 2e-49 and dv/v = -1.7e-25 (subluminal, no vacuum Cherenkov), a quadratic scale of 3.4e18 GeV against the GRB 221009A bound above 7.3e11 GeV. If the photon kept the bare band, photons would decay to e+e- above about 71 PeV, an untested prediction. The beyond-cone signal is likewise an untested prediction for Planck-localized sources. A thermal slab mirror adds dN_eff < 0.02 for R >= 2. A link on N would drain fine-lattice charge at about 6e34 per m^3 per s in 1 MV/m parallel to 1 T, excluded by vector-like QED. The measured n_s = 0.965 is 230 and 246 sigma from the indices 0 and 2.

##### Boundary

Supplied: the coarse sites (axiom-level), the split, the fine rate, the dimerized coupling X with the sign of G4 that picks the handedness (G4 x s3 would make the content vector-like), kappa = 0.5 with M > kappa st (otherwise both copies bind), the steps 0.04 and 0.3, the Floquet ordering, the unit map and measured inputs. Cited: GNVW. Forced: G4, the Wilson term, the copy mass as wall height, the kernel count, self-similarity, the swindle and the small-momentum laws. Negative results: the single fine chirality needs unbounded range and loses the bounded light cone; the ladder gives no tilt; its one exact charge is anomalous and cannot carry a massless link; it gives 1 generation, never 3. No coarse sites, coupling or rule are established.

---

### #9911: gapping the mirror releases vector-like doublers

**Statement (the note's own `claim_scope`, verbatim).**

> For the supplied block Hamiltonian H' with a supplied copy-selective symmetric mirror term, the light-copy states at K = 0 and K = R are exact zero modes at any coupling and the second-order induced light mass vanishes at K = 0, but with the mirror gapped the light copy has 8 Weyl nodes per sublattice (4 left, 4 right), a vector-like spectrum; a 1+1D chain shows the same release; no chiral light spectrum is established.

**Kind of statement.** Exact finite results (4^3 torus and one block) for the supplied block Hamiltonian H' with a supplied copy-selective symmetric mirror term; the 1+1D chain is a supplied toy; extension away from the endpoint rests on Golterman-Shamir under assumptions the note did not check; the measurement lines are estimates.

**Dependencies.** H' = (i/2)[W_o, W_e], as in #9905 (logged), per this note's runner; the quoted text does not define it by a formula. The cell chains are those of #9910 (logged). Cites Nielsen-Ninomiya, anomaly matching and Golterman-Shamir (arXiv:2505.20436).

**Runner.** [`light_copy_exactly_massless_yet_mirror_gapping_releases_vector_like_doublers_2026_10_21.py`](../scripts/light_copy_exactly_massless_yet_mirror_gapping_releases_vector_like_doublers_2026_10_21.py); cached output [`light_copy_exactly_massless_yet_mirror_gapping_releases_vector_like_doublers_2026_10_21.txt`](../logs/runner-cache/light_copy_exactly_massless_yet_mirror_gapping_releases_vector_like_doublers_2026_10_21.txt); source note at head `314fa5e93d` of branch `claude/toe-light-protection-20261021`: `docs/LIGHT_COPY_EXACTLY_MASSLESS_YET_MIRROR_GAPPING_RELEASES_VECTOR_LIKE_DOUBLERS_BOUNDED_THEOREM_NOTE_2026-10-21.md`.

**Note text, verbatim** (title line dropped; no section omitted). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem.
Primary runner: `scripts/light_copy_exactly_massless_yet_mirror_gapping_releases_vector_like_doublers_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its chirality route gaps one copy (the mirror) symmetrically and keeps the other (the light copy). This note asks whether the light copy stays massless and whether it stays chiral. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither H' nor the mirror term.

##### Statement

1. At K = 0 and K = R the light copy is decoupled exactly: its states commute with every term built from mirror modes, for any coupling, so its Green function there is 1/z. The second-order induced light mass is zero at K = 0, and no mirror condensate can give the light copy a mass at K = 0.
2. Anomaly matching protects the light copy exactly for N = 1, 2, 4, 5, 7, 8 families, the N at which the rest cannot be gapped. At N = 0 mod 3 every listed anomaly vanishes and anomaly matching protects nothing.
3. Negative result. Once the mirror is frozen or gapped by a copy-selective term, the light copy has Weyl nodes at all 8 block-zone corners, 4 left-handed and 4 right-handed per sublattice. The spectrum is vector-like in each SU(2)_e sector. A 1+1D chain shows the same release at p = pi.

##### Derivation

H'(0) = H'(R) = 0, and s3 splits each sublattice 2 + 2 with [s3, H'(K)] = O(K^2). Near Gamma the light-mirror block has two equal singular values (sqrt2/6)|Kx^2 + w Ky^2 + w^2 Kz^2|, a d-wave form that vanishes on the body diagonals. On a 4^3 torus, in both tilings, the light states at K = 0 and K = R are killed by H' and orthogonal to the mirror combinations of all 16 cubes. By the canonical anticommutation relations they commute with every mirror term, so they are exact zero modes.

The mirror cell chains of the single-cell pair-square theorem give E0 = -2g sqrt(11088 + 48 sqrt 21081), gap 19.0715 g and fermion gap 33.5804 g. Reversal of the ground chain and particle-hole conjugation (16 <-> 16bar) give equal hole weights, so the isolated cell's mirror Green function is odd in z and vanishes at z = 0. The second-order self-energy h G_b h^dag is then a Z factor plus a static part from the mirror's own band of order K^5/Delta_f^2, which is zero at K = 0. Any mirror condensate reaches the light copy only through h(K) ~ K^2, so its induced light mass term goes as K^4/M and is zero at K = 0. Masses for the light copy therefore need fields coupled to it directly, as an explicit new term.

Per family, the light content carries twisted-Z3_k x SU(2)_e^2 = 4(q_a + k), which is 16 = 1 mod 3 at k = 2; the set still to be gapped (the mirror plus the light R-point partner) carries the opposite. The protection that holds at N = 0 mod 3 is crystalline: the copy label is exact at K = 0.

At the 8 corners the light-light and mirror-mirror blocks of H' vanish. The mixing is 0 at Gamma and R and 2sqrt2/3, the whole free gap, at the six X and M corners: H' gaps X and M only through copy mixing. With the mirror frozen, the light Hamiltonian P_l H' P_l is traceless with zeros only at the 8 corners, chirality (-1)^(r+1): Gamma and the three M points left-handed, the three X points and R right-handed, net zero. A gapped mirror with a propagator zero removes the partner that the X and M doublers were paired with. Any endpoint that freezes local light combinations leaves a finite-range free Hamiltonian, whose nodes have net chirality zero per sector by Nielsen-Ninomiya; with Gamma kept, a right-handed node survives. Golterman and Shamir (arXiv:2505.20436) extend this away from the endpoint under their assumptions; that is cited, not rederived.

##### Checks

The runner ends with `TOTAL: PASS=20 FAIL=0`. Among its lines:

- `[PASS] A1 [T] H'(0) = H'(R) = 0; s3 splits each sublattice 2+2; [s3,H'(K)] = O(K^2)`.
- `[PASS] A2 [T] near Gamma the light-mirror block has 2 equal singular values (sqrt2/6)|Kx^2 + w Ky^2 + w^2 Kz^2|`.
- `[PASS] A3 [T] at the 8 corners the light-light and mirror-mirror blocks vanish; the mixing is 0 at Gamma, R and 2sqrt2/3 = the whole free gap at the 6 X/M corners`.
- `[PASS] A4 [T] the light projected band P_l H' P_l is traceless with zeros only at the 8 corners, chirality (-1)^(r+1) (Gamma, 3M left; 3X, R right): net 0`.
- `[PASS] B1 [T] 4^3 torus, both tilings: light K=0 and K=R states are killed by H' and orthogonal to the mirror combos of all 16 cubes ... exact zero modes, G_l(z,0) = 1/z at any coupling`.
- `[PASS] B2 [T] one block, mirror top form: at Gamma and R the 16 light states stay exactly degenerate, mirror gap exactly g (g = .5, 4, 32) | splitting 5e-14`.
- `[PASS] C1 [T] cell chains: E0 = -2g sqrt(11088+48 sqrt21081), Delta = 19.0715 g, Delta_f = 33.5804 g`.
- `[PASS] C2 [T/F] second order Sigma = h G_b h^+ ... O(K^5), zero at K = 0, never a mass`. The one-block diagonalisation gives 0.170579652 against a predicted 0.170579724 at g = 2.
- `[PASS] D1 [T] ... anomaly protection holds exactly for the N at which S cannot be gapped | k=2: N [1, 2, 4, 5, 7, 8]`.
- `[PASS] D2 [T] at N = 0 mod 3 all listed light anomalies vanish ... anomaly matching gives no protection there`.
- `[PASS] E2 [T] endpoint (mirror frozen, P f P = 0): light H_eff = P_l H' P_l, 8 Weyl nodes per sublattice per family, 4L + 4R: vector-like in each SU(2)_e sector`.
- `[PASS] E3 [F] one block at X ... light weight 0.9991 = Z = g^2/(g^2+8/9): doublers released | gap 0.9428, 0.8093, 0.0329, 0.0005` at g = 0, 2, 8, 32.
- `[PASS] E5 [T] zoom repair of X/M: a light-copy term mu(1 - S(K)^2) linking K and K+R ... the 6 X/M doublers get gap mu 8/9, Gamma and R stay`.
- `[PASS] F1 [T]` to `[PASS] F5 [T]`: the 1+1D chain (16 modes on a twisted ring, copy mixing mu(1 - cos p), mu = 0.5). The light p = 0 mode commutes with the generator to 4e-17 and stays gapless and right-moving (+0.1494, weight 1.0000 at theta = 0.3, g = 16). The p = pi doubler is released as a left-mover (-1.006, -0.210, -0.1497 with weights 0.57, 0.90, 0.9961 for free, g = 4, g = 16), so the light copy becomes R + L. A pair hop on both copies instead moves the light Gamma quasiparticle to -22.35 (weight 0.32). Freezing the staggered light pair leaves H_eff = sin(K)/2, a new left-mover at K = pi.

Estimate lines: `[PASS] E1 [E]` (no light composites: odd cell levels >= 33.58 g, even >= 19.07 g, mirror-only composites carry twisted charge 0 against the light's 1) and `[PASS] E4 [E]` (condensation wins over hybridisation for g > 0.066, below the second-order bound g > 0.102 for the gapped mirror phase, so wherever the mirror is gapped the doublers are released).

Against measurement, as an estimate: at least 4 left- and 4 right-handed weak-doublet tastes per family gives N_nu >= 12 at N = 3, against 2.984 +- 0.008, plus full-strength right-handed charged currents. The induced change of the light velocity at 1 TeV is below 6e-64.

##### Repair candidate, not adopted

A light-copy term mu(1 - S(K)^2) linking K and K + R, staggered over blocks and so read one rung up, gaps exactly the six X and M doublers with gap mu 8/9 and keeps Gamma, R and the decoupling theorem. After it the light content is Gamma plus the R-point partner. Gapping that partner remains open; the anomaly-allowed N = 0 mod 3 is necessary but not sufficient for it.

##### Boundary

Supplied: H', which copy is the mirror, the mirror terms (the pair square and the stand-ins used here, the one-block top form and the 1+1D pair hop, all copy-selective with a unique symmetric ground state and no bilinear condensate), g and mu, the 1+1D Wilson-type mixing (chosen to mimic the block corners, not derived), the (4,2) content, SU(2)_e as the weak group, the twist k = 2 and a = 3 Planck lengths. Cited: Nielsen-Ninomiya, anomaly matching and Golterman-Shamir, whose assumptions were not checked for this candidate beyond the endpoint. Notes that assume two light tastes per family after mirror gapping are narrowed: without the repair term there are eight. The register's claims of exact chirality and V - A are not supported here. No chiral light spectrum is established.

---

### #9971: rung ladder is a domain-wall direction with exact inflow but bounded speed gives a charged tower

**Statement (the note's own `claim_scope`, verbatim).**

> For a supplied free tree ladder (1+1D toy: rung j has cells of 2^j fine cells, two modes per cell, a Wilson-type rung tick with copy mass m, each parent exchanging with its two children through the rank-one T = (s_z - i s_y)/2 at kap/sqrt2), (A) one chiral pair forms: a mover on the finest rung and the opposite mover on the top rung; at the tuned wall m = -kap the zero-momentum kernel is exact, and an offset mu pairs the ends into a residual mass falling by mu/kap per rung (fine rate) or mu/(sqrt2 kap) (zoom rate); (B) with Wilson-line dressing the ladder is gauge covariant, flux 2 pi moves q species units and q^2 gauge units from the top rung to rung 0 (inflow along the rungs), the inflow sums to zero for 3-4-5-0 and for the 16, and gauging only the light end either breaks gauge equivalence or, after Gauss projection, cuts the ladder and puts a charged mirror at the cut; (C) at the zoom rate the middle-rung band gaps are 0.707 x 2^-j exactly self-similar, and a Weyl bound gives gap <= 2 ||hop||, so bounded speed forces one charged vector-like band per factor 2 in energy; at the fine rate the gaps are rung-independent but rung j moves 2^j fine cells per tick; (D) estimates: at R = log2(c/(H0 a)) = 200 the zoom ladder puts 17.4 charged three-family copies between m_e and M_Z, about 38 units of extra 1/alpha running against 0.014 known; (E) a full-density layer coordinate inside a role block is the domain-wall slab: no tower, residual mass (mu/kap)^Ls, but the far mirror keeps the full charge, so it gives exact chiral symmetry of a vector-like theory only. Supplied model, finite diagnostic; no rule is adopted.

**Kind of statement.** Dependent on a supplied model; finite diagnostic. Exact on the 1+1D free toys, a 3D Wilson-band integral, and estimates against measurement; the note adopts no rule.

**Dependencies.** Builds on and narrows #9908. Cross-checks use notes on a hybrid wall, a ladder wall and the toy Monte Carlo (the latter is #9965, logged). Cites Callan-Harvey inflow, the Neuberger overlap and the Grabowska-Kaplan route (not tested).

**Runner.** [`the_rung_ladder_is_a_domain_wall_direction_with_exact_inflow_but_bounded_speed_makes_its_coarse_rungs_a_charged_tower_2026_10_22.py`](../scripts/the_rung_ladder_is_a_domain_wall_direction_with_exact_inflow_but_bounded_speed_makes_its_coarse_rungs_a_charged_tower_2026_10_22.py); cached output [`the_rung_ladder_is_a_domain_wall_direction_with_exact_inflow_but_bounded_speed_makes_its_coarse_rungs_a_charged_tower_2026_10_22.txt`](../logs/runner-cache/the_rung_ladder_is_a_domain_wall_direction_with_exact_inflow_but_bounded_speed_makes_its_coarse_rungs_a_charged_tower_2026_10_22.txt); source note at head `9a11d22c6a` of branch `claude/toe-rung-dimension-chirality-20261021`: `docs/THE_RUNG_LADDER_IS_A_DOMAIN_WALL_DIRECTION_WITH_EXACT_INFLOW_BUT_BOUNDED_SPEED_MAKES_ITS_COARSE_RUNGS_A_CHARGED_TOWER_BOUNDED_THEOREM_NOTE_2026-10-22.md`.

**Note text, verbatim** (title line dropped; sections omitted (gate, smuggling-review, repo-check and mapping sections, which describe the review procedure and not the result): Smuggling check). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem.
Primary runner: `scripts/the_rung_ladder_is_a_domain_wall_direction_with_exact_inflow_but_bounded_speed_makes_its_coarse_rungs_a_charged_tower_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its chirality item says no finite-range update gives net chirality at any rung, and that the update law's light content is vector-like. Domain-wall fermions get exact lattice chirality from an extra coordinate, with the light Weyl field on one boundary and its mirror on the other. This note asks whether a coordinate the framework already has can play that role without a literal Z^4. The candidates are the rung index of the nested blocks (the split cascade's levels) and the tick. Where the rung reading fails, the note tests one new rule, a layer coordinate inside a role block. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the model inputs.

Build on and narrow: the octree-ladder note (PR #9908) proved, for the 3D fine-rate ladder, the one fine chirality, the top-rung mirror, the per-rung residual-mass law and the unbounded range (an Eilenberg swindle). The campaign files hybrid-wall and ladder-wall cover the zoom-rate ladder, the top-rung pair square and the cut-rung flow. This note adds the following: the inflow along the rungs as an exact spectral-flow statement; anomaly-free versus anomalous content; the bounded-speed theorem behind the tower; the estimate at the rung count the horizon sets; and the full-density layer comparison.

##### Statement

A. Free ladder (1+1D toy).
1. Exact. H_zoom = S H_fine S with S = 2^(-j/2), so the two rates have equal inertia at every Bloch momentum, and the zero-momentum kernel has dimension 2 at both rates (A1).
2. One chiral pair. On rung 0 a mover has velocity -1. On the top rung the opposite mover has velocity 2^R (fine rate) or 1 (zoom rate) (A2).
3. The ends' residual mass is mu (mu/kap)^R at the fine rate, with a ratio of 0.1994 to 0.2000 at mu = 0.2 kap. At the zoom rate (in fine units) the ratio is mu/(sqrt2 kap). At the tuned wall the mass is exactly zero (A3). At fixed physical momentum, the light state's weight on the top rung falls from 2.5e-14 (R = 2) to 1.2e-27 (R = 6) (A4).

B. Gauge.
1. Exact. With Wilson-line dressing (every hop carries exp(i q A dx), and every parent is anchored at its first child), the ladder at flux theta is the twisted ladder at Bloch Q_n = (q theta + 2 pi n)/N_top, with a residual of 3e-15 (B1).
2. Index. Each Bloch turn has one zero crossing on the light end and the opposite one on the top rung, at both rates and for both handednesses. Flux 2 pi therefore moves q units of species number and q^2 units of gauge charge between the ends. This is Callan-Harvey inflow along the rung direction through the gapped middle rungs (B2).
3. For 3-4-5-0 the gauge inflow is sum chi q^2 = 9 + 16 - 25 - 0 = 0, while the species numbers (3, 4, -5, 0) still flow. For one family's 16, the coefficients Y^3, Y, SU(2)^2 Y and SU(3)^2 Y all vanish. So anomaly freedom makes the light end alone gauge-consistent, but it does not decouple the mirror (B3).
4. Gauging only the light end. If the cut is left undressed, the hops across it break gauge equivalence (the spectra of H(2 pi) and H(0) differ by 0.38). If Gauss's law projects those hops out, the ladder is cut. Crossings by rung are then [-1, 0, +1, -1, 0, +1]: the gauged piece carries its own charged mirror on rung J - 1 (B4).

C. Rates.
1. The middle-rung band gaps are 0.74 on every rung at the fine rate. At the zoom rate they are exactly 0.707 x 2^-j (C1).
2. Weyl bound (theorem). Suppose the smallest on-site |level| exceeds ||H_hop||. Then the path from the on-site Hamiltonian to H stays gapped, so the index is 0. A wall therefore needs bulk gap <= 2 ||H_hop||. In the scan, the largest ratio at indexed points is 0.52 (C2). By Lieb-Robinson, bounded speed v with hop range 2^j caps rung-j hops at about v 2^-j. So at bounded speed, gap_j <= 2 v 2^-j. Bounded speed makes the zoom rate the fastest rate allowed, and with it the tower of bands.

D. Estimates against measurement.
1. Diagnostic. A unit-charge 3D Wilson-Dirac band gives Delta(1/e^2) = chi(q)/q^2 = 0.035, 0.022 and 0.014 at m0 = 0.2, 0.354 and 0.6. These are within a factor 2 of the continuum value ln(Lambda^2/m^2)/(12 pi^2) (D1).
2. With a = sqrt(8 pi) l_P, the horizon sets R_H = log2(c/(H0 a)) = 200.1. At the zoom rate, a gauge-covariant ladder puts log2(M_Z/m_e) = 17.4 rungs between m_e and M_Z. Each is a vector-like three-family copy with sum Q^2 = 8. Together they add 17.4 x 4 pi x 0.022 x 8 = 38 to the running of 1/alpha, against an uncertainty of 0.014 (Delta alpha_had). This is excluded unless c1 < 2.4e-5 (D2).
3. At the fine rate there is no tower, and the mirror has essentially no states below 1 TeV per horizon volume. The residual mass is at most 1e-42 GeV for mu/kap = 1/2. The price is that rung j crosses 2^j sites per tick, the swindle of PR #9908, which goes against nearest-neighbour admissibility (D3).
4. Any cut, or any finite top rung with E_R above M_Z, leaves a massless charged mirror. The mirror e^c' alone adds 35.5 MeV per family to Gamma_Z (ladder-wall E3), against sigma = 2.3 MeV (D4).

E. A full-density layer coordinate, the rule proposed when the scope was widened.
1. Each matter cell holds 2 Ls one-mode sites (layer s, component). The layer hop T acts inside the cell, and the cell-to-cell hop K acts at equal layer. This is the domain-wall slab. The layer gap is the same on every layer (1.0, so no tower), the residual mass falls by (mu/kap) per layer (0.04 per two layers), and the flow is (-1 near, +1 far): the far mirror carries the full charge (E1).
2. Theorem (from B1 and B2). Any gauge-covariant reading of the far layers keeps their crossing under flux 2 pi. The mirror therefore couples to the holonomy with charge q. The slab gives exact chiral symmetry of a vector-like theory, not chiral gauge couplings.
3. Estimate of the cost. One family needs 16 Weyl x 4 components x Ls sites per cell. Three families at Ls = 8 use 1536 of the 1728 sites of a 12^3 role block. The cell-to-cell hops span the block, which gives a uniform slowdown and no tower.

F. The tick (counting theorem). A domain wall bounds a bulk with one more dimension, and its boundary is the whole 3+1 world, tick included. So the tick cannot be the wall direction. The B4 transfer matrix is the world's own time step: euclidean-b4 B4 shows it projects onto the vacuum and cannot carry CL-2. Neuberger's overlap sign(H_W) is the infinite-layer limit of a fifth-direction transfer matrix, that is, of E's layer coordinate.

##### Candidate law text (not adopted)

Rung reading, as tested here (fails measurement, D2/D4):
> "Each block's mode exchanges with the same mode of its children through T = W(1 - g5)/2, at the block's own rate, with the copy mass the wall height."

Layer rule, proposed (exact free chirality; vector-like as it stands):
> "Each matter cell is a role block whose matter sites, in a fixed order, are layers 0..Ls-1. Each half-tick hops every layer's modes to its neighbour layer through W(1 - g5)/2 and to the same layer of the neighbour cell through the cube tick; matter is read at layer 0."

To make the gauge couplings chiral, the layer rule needs one more clause. Either the far layers are gapped symmetrically (pair-square route; toy-qmc found pair order in the extended zone), or the far layers' hops read a smoothed field that keeps the holonomy (the Grabowska-Kaplan route, not tested here). The smoothed-field clause has an open risk: the holonomy and the topology stay coupled (E2).

##### Boundary

The toys are 1+1D, plus a 3D band integral. The 3+1D statements are cited (PR #9908, hybrid-wall) or argued by scaling (self-similarity, power counting). No interacting mirror, smoothed-field clause or adopted rule is established. Clause count: the rung reading adds one clause (the exchange) and gives one generation. The layer rule adds the layer clause plus a decoupling clause, and it removes none unless the decoupling clause can replace the register's mirror term.

---

### #9985: Grabowska-Kaplan far layers pass the Nielsen-Ninomiya count but induce a cutoff-scale photon mass

**Statement (the note's own `claim_scope`, verbatim).**

> For free Shamir domain-wall slabs (Wilson kernel, M = 1, Ls = 8 and 16, Pauli-Villars subtraction) in 2D and 4D momentum space, their overlap (infinite-Ls) form, an 8 x 8 2D SU(2) lattice and a 1+1D Chern-strip Hamiltonian slab (N = 32, Ls = 8): (A) the light-end chiral propagator element has its pole at p = 0 and zeros of opposite net chirality at the three doubler corners, the mirror element is its mirror image, and the boundary field is one vector-like pair, so the gauge-off slab meets the generalized Nielsen-Ninomiya theorem and is evaded only at gauging, through the mirror's range-r coupling; (B) when the far layers read A_* != A, the effective action gains c (A - A_*)^2, which is gauge invariant and protected by nothing: c = -0.0221 per q^2 in lattice units for the Shamir slab, independent of the cut position, the ramp width and Ls, and c = 2 <g_00> = 0.0997 in the overlap form, with g the quantum metric of the Wilson bands, positive whenever the bands carry the light chiral mode; in 4D this gives the photon a mass 0.2-0.4/a (4e17-9e17 GeV) for every k above 1/r, while in 2D the term is marginal (0.23 per q^2), which is why the 2D toy passed; (C) the slab is exactly gauge invariant at every r, and the mirror's residual field-strength coupling falls as 1/(kb) for block reading and as a gaussian for flow, but the induced mass grows to its full value; (D) 2D SU(2) block-flux spreading with comb-tree anchor transports is per-site covariant to 2e-15, spreads every block's flux evenly, and keeps block loops, boundary-line holonomies and the 't Hooft twist exactly; (E) a layer-blind fold quench fills the light and mirror edge modes equally (exact end-exchange symmetry), so a thermal mirror gives Delta N_eff = 2.25 (14 sigma). Supplied model, finite diagnostic; no rule is adopted.

**Kind of statement.** Dependent on supplied free Shamir domain-wall slabs and their overlap form; quadratic response at constant layer fields, exact covariance checks, finite diagnostic. Four-dimensional finite-k continuity is assumed. Not an adopted rule.

**Dependencies.** Builds on and narrows sections C and E of #9980 (logged). Consistent with #9944 (logged). Literature (Golterman-Shamir 2311.12790, 2603.15985, 2505.20436; Hamada-Kawai; Ago-Kikukawa) was read from abstracts or HTML only.

**Corrections and narrowings that apply to this statement.** The sign of the induced coefficient c is regulator dependent (negative for the Shamir slab, positive for the overlap form); only its non-vanishing is forced. The note reads #9980's ratio '0.26-0.33 rather than 1/2' as this induced term, and narrows #9980's sections C and E. The 2D toy of #9980 passed because the term is marginal in 2D.

**Runner.** [`grabowska_kaplan_far_layers_pass_the_nielsen_ninomiya_count_but_induce_a_gauge_invariant_cutoff_scale_photon_mass_above_the_smoothing_scale_2026_10_22.py`](../scripts/grabowska_kaplan_far_layers_pass_the_nielsen_ninomiya_count_but_induce_a_gauge_invariant_cutoff_scale_photon_mass_above_the_smoothing_scale_2026_10_22.py); cached output [`grabowska_kaplan_far_layers_pass_the_nielsen_ninomiya_count_but_induce_a_gauge_invariant_cutoff_scale_photon_mass_above_the_smoothing_scale_2026_10_22.txt`](../logs/runner-cache/grabowska_kaplan_far_layers_pass_the_nielsen_ninomiya_count_but_induce_a_gauge_invariant_cutoff_scale_photon_mass_above_the_smoothing_scale_2026_10_22.txt); source note at head `bb8ac3085b` of branch `claude/toe-gk-nogo-check-20261021`: `docs/GRABOWSKA_KAPLAN_FAR_LAYERS_PASS_THE_NIELSEN_NINOMIYA_COUNT_BUT_INDUCE_A_GAUGE_INVARIANT_CUTOFF_SCALE_PHOTON_MASS_ABOVE_THE_SMOOTHING_SCALE_BOUNDED_THEOREM_NOTE_2026-10-22.md`.

**Note text, verbatim** (title line dropped; sections omitted (gate, smuggling-review, repo-check and mapping sections, which describe the review procedure and not the result): Smuggling check). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem.
Primary runner: `scripts/grabowska_kaplan_far_layers_pass_the_nielsen_ninomiya_count_but_induce_a_gauge_invariant_cutoff_scale_photon_mass_above_the_smoothing_scale_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. The [smoothed far-layer note](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/27d877dc41e353268ce36cf4fe634916d8ba6f0d/docs/FAR_LAYERS_READING_A_SMOOTHED_FIELD_DECOUPLE_THE_MIRROR_FROM_FIELD_STRENGTH_BUT_NOT_FROM_GAUGE_TURNS_TOPOLOGY_OR_LONG_WAVELENGTHS_BOUNDED_THEOREM_NOTE_2026-10-22.md) (open PR #9980) proposed the leading chirality route: a layer slab inside each role block, where layer s hops on rung-s flux-smoothed links and the light end reads fine links. This note is a hostile check of that route against four known obstructions:
- the generalized Nielsen-Ninomiya theorem of Golterman and Shamir;
- the problems known for Grabowska-Kaplan (GK);
- the non-abelian extension;
- the requirement that the mirror starts empty.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

Repo check: origin/main contains no note on Grabowska-Kaplan or on smoothed far layers. The Golterman hits on main are corner-fermion and reflection-positivity notes and do not engage the generalized theorem. The Spin(10) atomic-gap note (2026-09-14) treats a frozen mirror boundary, which is a different mechanism. Open PRs: #9980 (the route under test) and #9944 (zeros-ghosts: propagator zeros sit on the partner's line). This note builds on #9980 and narrows its sections C and E. It is consistent with #9944: the zeros in A1 below are kinematical.

##### Statement

A. The spectrum count (gauge off).
1. Theorem (argument principle). On the zone torus, the windings of a chiral propagator element around its singular points sum to zero. In the free 2D slab, the light-end element (layer 0, P_-) has its pole at p = 0, with winding +1, and zeros at (pi,0), (0,pi) and (pi,pi), with windings -1, -1 and +1. The light end alone is therefore one Weyl pole plus kinematical zeros of opposite net chirality. The mirror element (layer Ls-1, P_+) is its mirror image, so the boundary field is one vector-like pair (A1).
2. Which assumption fails. None of them. The theorem's conditions in 2505.20436 are:
   - a finite-range, fermion-only Hamiltonian;
   - an unbroken compact symmetry G;
   - a free massless relativistic continuum;
   - a zero-free complete set of interpolating fields.

   The gauge-off slab meets all four, and its spectrum is vector-like, as the theorem demands: the mirror pole is present. GK evades only a corollary, "a vector-like spectrum gives a vector-like gauge theory". That corollary needs both ends to couple to the field through the local conserved current. In the slab the mirror reads A_*, a functional of range r whose form factor satisfies f(0) = 1 exactly, because flow and block reading keep the k = 0 mode. The gauge theory is therefore chiral only for 1/r << k << 1/a. Below 1/r it is vector-like, and the mirror's charge is visible in Gauss's law beyond r (A2).

B. The induced term (the decisive result).
1. Diagnostic (4D Shamir slab, DW minus PV, constant layer fields). The layer response Pi^{st}, the second derivative of -log det with respect to a constant A on layers s and t, has rows that sum to zero (the Ward identity; 7e-4 at N = 16, falling with N). Let the near layers read A and the far layers read A_* = 0, as in the window k >> 1/r. Then Gamma gains c A^2 per q^2 with c = -0.0221 (lattice units). This value is the same for:
   - every cut position j = 2..6 (-0.0219 to -0.0221);
   - ramp widths 1, 2 and 4 layers (-0.0221 to -0.0220);
   - Ls = 8 and Ls = 16 (-0.0218 and -0.0217 at N = 12).

   So it is an end term (the light Weyl and the mirror separated in field), not a bulk F_{s mu}^2 term, and spreading the transition over many layers does not remove it (B1).
2. Theorem (overlap form). For Ls -> infinity, |det| = |<v(A)|v(A_*)>|^2 at each momentum. For a constant A and A_* = 0, -log|<v(p+A)|v(p)>|^2 = g_00(p) A^2 + O(A^3), where g is the quantum (Fubini-Study) metric of the filled bands of H_W = g5 D_W(-M). Hence c = 2 <g_00>_BZ = 0.0997, equal to the direct second difference 0.09970. Since g >= 0, c vanishes only if the filled projector is momentum independent. Such bands are trivial and carry no light chiral mode. The band topology that makes the light end chiral therefore forces the mass (B2).
3. Why gauge invariance does not help. A and A_* turn alike, so A - A_* is gauge invariant, and c (A - A_*)^2 is allowed. It vanishes for k << 1/r, where A_* -> A, and takes its full value in the window. The exact gauge invariance of the smoothed slab (#9980 A1, C2) is real but irrelevant to this term.
4. Estimate. With e^2 = 4 pi/137 and sum Q^2 = 16 over three families, m_gamma a = 0.18 (Shamir, with m^2 < 0, tachyonic) or 0.38 (overlap), that is 4e17 to 9e17 GeV, for every k above 1/r. There would be no electromagnetism at distances below r, while r >> 1/m_e is needed (#9980 E2). A local A^2 counterterm is not gauge invariant. Only a supplied -c (A - A_*)^2 clause, tuned to about 1e-90 (the photon mass bound against 1/a, squared), cancels it (B3).
5. 2D. The same term is dimensionless there: c2 = 0.227 per q^2 in the overlap form, comparable to the Weyl Schwinger-type term (ratio 1.43). It is marginal, not a cutoff mass. This is why the 2D toy passed: #9980 C2 has smoothed/unsmoothed photon response 0.26-0.33 rather than 1/2, and that is this term (B4).

C. Scaling with the smoothing radius r (abelian). The slab is exactly gauge invariant at every r, so no gauge non-invariance appears that could fall with r. What does fall is the mirror's residual field-strength coupling at fixed k:
- block (box) reading: |sin(kb/2)/(b sin(k/2))| <= 2/(kb), a power law, 1/r in amplitude and 1/r^2 in the action (0.97, 0.53, 0.11, 0.024 for b = 16, 64, 256, 1024 at k = 2 pi 37/4096);
- flow: (1 - eps khat^2)^n, gaussian in r ~ sqrt(n).

The induced mass c (1 - f(kr))^2 grows to its full value as r grows. It does not fall (C1).

D. Non-abelian (SU(2), 8 x 8).
1. Theorem (covariant block-flux spreading). In each b x b block, take the comb tree from the anchor c: down the column, then along the bottom row. The tree-frame links phi(a)^dag U phi(b) turn only by g(c). The block loop W is read from the tree-frame top links. Every plaquette lasso is set to X = W^(1/b^2), the principal root, which is conjugation covariant. The explicit solution is:
   - interior row-k links X^(-k);
   - the top link of each interior column V_x, with V_(x+1) = X^b V_x T_x;
   - boundary links untouched.

   The closure V_(X+b) = 1 is exactly the statement X^(b^2) = W. Measured: covariance residual 1e-15 (b = 2) and 2e-15 (b = 4); closure 2e-15; within-block angle spread 2e-14; max plaquette angle 2.61 -> 0.67 (b = 2) and 0.12 (b = 4). Link averaging without transports gives 1.57 (D1).
2. Theorem (topology). Block loops and the torus holonomies along block-boundary lines are untouched. The 't Hooft twist (1/2 tr[P_x, P_y] = -0.926 with noise) is kept exactly while its thin plaquette (angle 3.03) is spread to 0.19. A vortex pair with commuting holonomies (twist +1) is spread likewise. The twist is never lost, unlike the abelian anchor reading's Q in #9980 A2. The principal root is undefined only at W = -1 exactly (D2).
3. So the non-abelian smoothing rule exists and is clean. It is not the obstruction.

E. Does any rule fill the far layers?
1. Theorem (end exchange). The Chern-strip slab has the symmetry (x, s) -> (-x, Ls-1-s) with sigma_z, which exchanges the ends. A fold-type order on every site (period 2), ending suddenly, respects it, so it fills light and mirror edge modes equally: 0.6606 each. The same fold on layer 0 alone gives 0.577 against 4.5e-4 (E1).
2. Estimate. Every CL rule that creates excitations is layer-blind:
   - the fold and its relaxation into misfolds (free sites on every layer of the role block, neighbourhood-roles, fold-inflaton E);
   - the split's ~0.04 K^2 flips.

   Reheating therefore gives the mirror the SM temperature: Delta N_eff = 48 (10.75/106.75)^(4/3) = 2.25 against Planck's 2.99 +- 0.17, excluded at 14 sigma. A safe mirror needs rho_mirror/rho_SM <~ 0.1 at reheating, which is a lopsided reheating that no rule supplies (E2).
3. Estimate. After reheating:
   - gravity gives Gamma/H ~ (T/M_P)^3 <= 1e-30;
   - sphalerons fill the mirror only with the net winding of each r-cell, ~sqrt(Gamma_sph r^3/H), a density ratio ~1e-45 at 130 GeV for r = R_Earth;
   - a massless mirror, charged for k < 1/r, is pair-produced without mass suppression by any smoothed field with E^2 > B^2 or E.B != 0, so r must exceed the coherence length of every such field. r ~ c/H0, the 200 layers of #9980 E1, is safe (E3).

##### Verdict

The route fails as stated in 3+1D. Its exact gauge invariance, its covariant non-abelian smoothing and its topology bookkeeping all hold. But reading a different field at the two ends induces a gauge-invariant (A - A_*)^2 term whose coefficient is forced nonzero by the same band topology that gives the light chiral mode, and in 4D that term is a Planck-scale photon mass for every momentum above 1/r. It can survive only at a stated cost: a supplied, fine-tuned gauge-invariant mismatch clause -c (A_fine - A_read)^2 (one tuned number per gauge factor and charge assignment, to ~1e-90), plus a new rule that reheats only the near layers. The 2D toy survives because there the term is marginal.

##### Candidate law text (not adopted; what the route would need)

> "Each layer's links enter the response with the mismatch term that cancels the slab's induced (A_s - A_*)^2, measured in the vacuum's own units at every rung."

This is a candidate reading of the CL-3 vacuum standard, applied per rung to the mass part of the link response but not to its F^2 part. It is untested, and as stated it is a tuned subtraction. Reheating would also need a clause that confines excitation creation to layer 0. No such clause is derived, and the fold acts on every site.

##### Boundary

These are free-fermion quadratic responses at constant layer fields, plus exact winding, covariance and symmetry checks. Not established:
- interacting (SMG-type) far ends;
- finite-k 4D responses;
- SU(2) x SU(3) fermion slabs;
- real-time far-layer dynamics.

The literature engaged at abstract level is Golterman-Shamir 2311.12790 and 2603.15985, Hamada-Kawai 1705.01317 and Ago-Kikukawa 1911.10925. The conditions of Golterman-Shamir 2505.20436 are taken from its HTML text. No rule is adopted.

---

### #9992: block-local quartic gaps the Dirac mirror symmetrically and releases the light partners

**Statement (the note's own `claim_scope`, verbatim).**

> For the block-local mirror term (on each matter role block, the unique singlet charge-4 term of the block's mirror modes; SU(4) toy with one mode per flavour per block, and its Spin(10) form with two orbitals per flavour) on a real pi-flux Dirac band of the block lattice: (exact) the term is unique (SU(4): 1 with one orbital, 5 with two; Spin(10) on the Weyl 16: 0 with one orbital, exactly 1 with two), is invariant under per-block SU(4) gauge rotations, commutes across blocks, maps to its conjugate under the sublattice particle-hole map, and alone has a unique ground state with gap g; with any real band, including a real light layer mixed to the mirror, the interaction expansion is sign-free (weights det(M)^4, M real). Finite diagnostics (sign-free CT-INT, L = 4, 6 block units, beta = 4, 8 in units 1/g): the Dirac mirror is massless for g/t <= 2, crosses over near g/t ~ 4, and is symmetric and gapped for g/t >= 8 (Dirac-point gap about 0.85-0.95 g, L-independent); no bilinear channel orders at any coupling (site and bond, charge 0 and 2, all Q). With a light layer whose modes are paired to the mirror by w eps_x, the light gap falls from w (g/t <= 4) to 0.54 w (g/t = 8) and 0.22 w (g/t = 16): the symmetric mirror gap releases every light mode the mirror was pairing (exact at the Dirac point once the mirror propagator has a zero). The toy is not Spin(10), the band is not the CL-1 cube tick, no Binder ratio, L <= 6.

**Kind of statement.** Exact statements (uniqueness of the charge-4 term, sign-freeness, gauge invariance) plus a numerical diagnostic (sign-free continuous-time interaction-expansion Monte Carlo, L = 4, 6, beta = 4, 8, some entries recorded rather than live) on a supplied SU(4) toy with a supplied real pi-flux band. The toy is not Spin(10) and the band is not the supplied cube tick. The note's own verdict is not to adopt the term.

**Dependencies.** Contrasts with #9983 (logged), whose band had no Dirac point; uses the toy Monte Carlo #9965 (logged) and the far-end atomic pair-square theorem of earlier work. Cites Ayyar-Chandrasekharan (not computed) and Golterman-Shamir. Relied on by #9993 and #10004.

**Runner.** [`the_block_local_quartic_gaps_the_dirac_mirror_symmetrically_and_releases_the_light_partners_2026_10_22.py`](../scripts/the_block_local_quartic_gaps_the_dirac_mirror_symmetrically_and_releases_the_light_partners_2026_10_22.py); cached output [`the_block_local_quartic_gaps_the_dirac_mirror_symmetrically_and_releases_the_light_partners_2026_10_22.txt`](../logs/runner-cache/the_block_local_quartic_gaps_the_dirac_mirror_symmetrically_and_releases_the_light_partners_2026_10_22.txt); source note at head `4572ca7d51` of branch `claude/toe-block-quartic-smg-20261021`: `docs/THE_BLOCK_LOCAL_QUARTIC_GAPS_THE_DIRAC_MIRROR_SYMMETRICALLY_AND_RELEASES_THE_LIGHT_PARTNERS_BOUNDED_THEOREM_NOTE_2026-10-22.md`.

**Note text, verbatim** (title line dropped; no section omitted). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem.
Primary runner: `scripts/the_block_local_quartic_gaps_the_dirac_mirror_symmetrically_and_releases_the_light_partners_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) leaves one chirality wall: a mirror term that gaps the mirror family symmetrically. The [face-gapped QMC note](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/6e45d558aeeb640e4d8e9e9694a895afb18a1f15/docs/THE_FILTERED_QUARTIC_TOY_WITH_A_FACE_GAPPED_BAND_IS_SYMMETRIC_AND_GAPPED_AT_MODERATE_COUPLING_AND_PAIRS_AT_STRONG_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-22.md) found two things in sign-free 3D QMC. The overlapping cube-filtered quartic pair-orders at strong coupling. The on-site SU(4) quartic is symmetric and gapped. That run had no Dirac point: its free band had only a quadratic touching. This note asks three questions. Does the non-overlapping, block-local version of the quartic fit the framework? Does it gap a mirror whose free band has a genuine Dirac point? And, the Golterman-Shamir question, does the light family keep its partners gapped while the mirror gaps? The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

##### Statement

1. (Framework fit and uniqueness.) CL-1 puts one fermion mode on each site. So a term that acts "on-site" in flavour must live on a non-overlapping block: the matter role block holding one family's modes. The block-local mirror term is the singlet charge-4 operator built from the block's mirror modes.
   - SU(4) toy, one mode per flavour per block: the singlet charge-4 operators span exactly one line, m1 m2 m3 m4. With two orbitals per flavour they span 5, so uniqueness needs one orbital.
   - Spin(10) on the Weyl 16: one orbital per flavour admits no singlet charge-4 operator. Two orbitals admit exactly one, the pair square.
   - In both cases the term is invariant under SU(4) (or Spin(10)) rotations of its own block alone, so it is gauge-invariant per block.
   - Terms on different blocks share no mode and are even, so they commute.
   - Every lattice map of the block tiling permutes the terms. A staggered sign gauge a -> -a multiplies each term by (-1)^4. The sublattice particle-hole map a_x -> eps_x a_x^+ sends the term to its conjugate, so -g sum (Q_b + Q_b^+) is invariant. Mode number is broken to Z4.
   - Alone, -g(Q_b + Q_b^+) has a unique ground state at -g with gap g.
2. (Sign.) Take any real free band, including a light layer mixed to the mirror by a real term, with vertices on the mirror block terms only. Every configuration of n terms and n conjugates has weight g^2n det(M)^4 with M real. A flux through a loop holding two vertex blocks makes the weights complex.
3. (Dirac band.) H = -t sum eta_mu(x)(a_x^+ a_x+mu + h.c.) is the real pi-flux (staggered) band on the block lattice. With periodic boundaries at L = 4 and antiperiodic at L = 6 it has exactly 8 zero modes per flavour (2 tastes x 4 components at k = (pi/2)^3), first levels 2t and sqrt3 t, and it anticommutes with eps_x. The mixing w eps_x (l_x^+ m_x + h.c.) gaps every light and mirror mode by exactly w, because (H +- w eps)^2 = H^2 + w^2. Every real period-2 site pattern tried is either this full mass or not a mass: (1 + eps)/2 leaves 8 zeros with a quadratic touching. So no real, sign-free taste-selective mixing was found.
4. (Mirror alone, finite diagnostics, g = 1.)
   - g/t = 0.5, 1, 2: massless. The Dirac-point midpoint gap is <= 0.02 and is 0.00-0.01 at L = 6.
   - g/t = 4: crossover. The Dirac gap shrinks with L at beta = 8 (cosh band [0.34,0.39] -> [0.27,0.30]), and pair xi/L falls 0.158 -> 0.101.
   - g/t = 8, 16: symmetric and gapped. The Dirac gap is L-independent, [0.87,0.91]; [0.85,0.90] and [0.92,0.99]; [0.87,0.98], approaching the exact g/t = infinity value g.
   - Across all couplings, S/N for each of the 7 bilinear channels falls from L = 4 to 6 by 2.6-3.7, against a volume ratio of 3.375. The channels are site pair (6, charge 2), site adjoint, site singlet density/staggered mass, bond pair (symmetric and antisymmetric), bond adjoint and bond singlet (VBS), each at its peak Q. No order is seen in any channel.
5. (Light release.) A light layer with the same band, paired to the mirror by w eps_x (t = 0.125, w = 0.25, beta = 8, L = 4). The light gap at the Dirac point is 0.249, 0.248, 0.239, 0.135, 0.054 at g/t = 1, 2, 4, 8, 16, against a free value of exactly w = 0.25. At L = 6 and g/t = 8 it is 0.141. Over the same range the mirror gap grows 0.25 -> 1.84. Exact form: at the Dirac point G_l = [i w - w_mix^2 G_m^0(i w)]^-1. Once the symmetric mirror's propagator has a zero (Sigma_m ~ Delta^2 / i w), the light has a pole at w = 0. Every light mode the mirror was gapping is released.

##### Derivation

Statement 1. A charge-4 operator on the block is a degree-4 element of the exterior algebra on (flavour x orbital). It is counted on the weight-zero subspace with the restricted Casimir sum_a (X_a P0)^+ (X_a P0), whose kernel is the singlets. The counts are SU(4): 1 (one orbital) and 5 (two). Spin(10), with the 16 as the even Fock space of 5 modes: 0 (one orbital) and 1 (two). The SU(4) result is Lambda^4 of the 4, times Sym^4 of the orbital space. The Spin(10) result is the register's "unique Spin(10) tensor times an algebraic-curvature tensor on the orbitals" (that space has dimension n^2(n^2 - 1)/12: 0, 1 for n = 1, 2). The symmetry and commutation statements are checked on two blocks (8 modes) to 1e-15.

Statement 2 is the toy-QMC sign argument. The light modes enter only the free propagator. The four flavours see the same real M, and vertex reordering gives +1.

Statement 3. {H, eps} = 0 because the hops join opposite sublattices. The zero modes are the 8 momenta with cos k_mu = 0 for all mu, since H^2 = 4t^2 sum cos^2 k_mu.

Statements 4-5 come from continuous-time interaction-expansion Monte Carlo. The moves are global and local pair insertions and removals and vertex shifts. The engine reuses the qmc-face-gapped engine with a translation-by-two table that carries the antiperiodic signs (checked to 1e-7). Observables come from the per-configuration propagator:
- bilinear correlators by Wick per flavour (pair G^2, adjoint (1 - G^T) G, bond forms with link phases);
- Dirac-point propagators Tr(P0 G(tau))/8 on the 8 zero modes, mirror and light;
- gaps from two estimators: the midpoint -(2/beta) ln(2 G(beta/2)/(G(0+) + G(beta-))), which is lower-bound style, and a one-level cosh fit at tau = beta/4, both as mean +- 2 sigma (jackknife, 16 bins).

The release formula follows from integrating out the mirror at quadratic order in the mixing. The light layer is free, so its exact propagator is the free one with self-energy w^2 eps G_m eps, where G_m is the full mirror propagator without the mixing self-energy.

##### Checks

- `[PASS] A1` real band with light-mirror mixing: trace = det(M)^4 (4e-16).
- `[PASS] A2` flux: complex weights (|Im w|/|w| up to 0.89).
- `[PASS] A3` uniqueness counts: SU(4) 1, 5; Spin(10) 0, 1.
- `[PASS] A4` per-block SU(4) invariance, commutation across blocks, particle-hole to the conjugate, unique block ground state -g with gap g.
- `[PASS] A5` 8 Dirac zeros at L = 4 (PBC) and 6 (APBC); {H, eps} = 0; the w eps mixing gaps by w; the half mixing gives a quadratic touching.
- `[PASS] A6` release algebra: |G_l(i 1e-3)| is 0.016 free and 941 with an SMG mirror.
- `[PASS] B1` engine vs exact diagonalisation of a mixed 3-orbital cluster: <H_int> and the light G_l(beta/2).
- `[PASS] C1` g/t = 1: Dirac gap 0.016.
- `[PASS] C2` g/t = 8: gap 0.63(6), xi/L 0.05.
- `[PASS] C3` g/t = 8, beta = 4: S/N ratio 3.30, cosh gap 0.684 vs 0.669 (L = 4, 6).
- `[PASS] C4` light gap 0.249 -> 0.144 while the mirror gap is 0.65.

Recorded production values (prod.py, 85 s segments, 171 to 48000 sweeps per point; printed by the runner as recorded, no PASS depends on them). Mirror alone, Dirac-point gap (cosh band, L = 4; L = 6), pair xi/L, and channel S/N ratio:

| beta = 8 | cosh gap | midpoint band | pair xi/L (4 -> 6) | S/N ratio min-max (7 channels) |
|---|---|---|---|---|
| g/t = 0.5 | [0.07,0.08]; [0.01,0.04] | <= 0.01 | 0.082 -> 0.053 | 3.06-3.38 |
| g/t = 1 | [0.07,0.09]; [0.00,0.05] | <= 0.01 | 0.085 -> 0.053 | 3.06-3.38 |
| g/t = 2 | [0.10,0.12]; [0.05,0.09] | <= 0.02 | 0.093 -> 0.058 | 3.05-3.35 |
| g/t = 4 | [0.34,0.39]; [0.27,0.30] | [0.16,0.20]; [0.11,0.13] | 0.158 -> 0.101 | 2.95-3.72 |
| g/t = 8 | [0.87,0.91]; [0.85,0.90] | [0.67,0.72]; [0.60,0.68] | 0.038 -> 0.037 | 2.80-3.41 |
| g/t = 16 | [0.92,0.99]; [0.87,0.98] | [0.75,0.80]; [0.63,0.77] | 0.021 -> 0.008 | 2.61-3.53 |
| g/t = inf | g (exact) | | 0 | |

At beta = 4 the cosh gaps are g/t = 2: [0.16,0.18]; [0.13,0.15], g/t = 4: [0.42,0.43]; [0.40,0.42], g/t = 8: [0.66,0.71]; [0.68,0.71], with S/N ratios 3.07-3.44. The cube-term susceptibility is at most 1.44 in every run and noisy at L = 6. The small nonzero cosh values at weak coupling come from incoherent self-energy decay; the midpoint gap stays at 0.

Light release (t = 0.125, w = 0.25, beta = 8, L = 4; cosh gaps):

| g/t | 1 | 2 | 4 | 8 | 16 |
|---|---|---|---|---|---|
| light | 0.249 | 0.248 | 0.239 | 0.135 (L = 6: 0.141) | 0.054 |
| mirror | 0.251 | 0.256 | 0.281 | 0.69 (L = 6: 0.66) | 1.84 |

##### Clause count and law text

Proposed replacement for the mirror clause of CL-1's chiral update (law text):

> "Mirror term. On each matter role block the mirror copy's modes carry the one Spin(10)-singlet charge-4 term they admit, the pair square of the block's two orbitals per flavour, with the same coupling on every block; terms of different blocks share no mode."

Effect on the register: one clause replaces one clause, and the cube filter (the supplied form factor prod cos^2(k_i/2)) is removed. That is a simplification. The term is forced by uniqueness once the block and the mirror copy are named.

Smuggling check:
- Supplied: the coupling g (a constant in proper units), the mirror bit, and the role block (already in CL-1).
- Forced: the form of the term (A3), its gauge and lattice covariance (A4), and the Z4.
- The toy evidence is SU(4), not Spin(10). Sign-freedom needs four identical flavours, and the Spin(10) pair square is not of that type, so the Spin(10) phase is unmeasured beyond the register's single-cell result (unique ground state, gap 19.1 g).

Verdict on the register: do NOT adopt this as the chirality fix. The block-local term is exactly the atomic pair square that the register's far-end theorem already excludes, and the QMC now confirms that exclusion in 3D. Gapping the mirror symmetrically is achieved, with no pair order, unlike the cube filter. But it releases every light partner that was gapped through light-mirror mixing, as Golterman and Shamir warn. Adopting it would trade the filter's pair-order failure for the far-end failure. The term is the better mirror-gapping term (unique, no filter, symmetric, gapped). If a separate rule removes the light copy's zone-corner partners WITHOUT routing through the mirror, this term is the natural mirror clause, and it should then replace the cube-filtered pair square.

##### Boundary

Supplied:
- the SU(4) toy (not Spin(10)), one mode per flavour per block;
- the real pi-flux Dirac band on the block lattice (a stand-in for the CL-1 cube tick's mirror band), with its boundary conditions;
- the w eps_x mixing as the stand-in for partner gapping through the mirror (no real taste-selective mass was found, so all light modes are paired in the test);
- sizes L = 4, 6, beta = 4, 8 (units 1/g), seeds, and g = 1.

Not computed:
- the Binder ratio, L > 6, and the T -> 0 limit near g/t ~ 4. A narrow intermediate bilinear phase, as Ayyar and Chandrasekharan found in 4E, is neither seen nor excluded.
- the Spin(10) pair square on the Dirac sea;
- a genuinely chiral light-versus-mirror split.

The unpaired-light question is trivial in this model: no light mode is unpaired. Statement 5 and A6 answer the Golterman-Shamir question for the paired ones.

---

### #9993: zone-corner partners are vector-like only through the sublattice charge

**Statement (the note's own `claim_scope`, verbatim).**

> Free-band census and removal tests for the light copy's zone-corner partners. Exact: on the CL-1 cube tick with copy mass (eps = 0.3, M = 0.2), the light copy's low content is one Dirac at K = 0 and the R = pi(1,1,1) partner sits at quasi-energy 2 eps, but the sublattice sign eps is not conserved and the copy mass is an eps-odd mass. On the step-pi/2 conserved generator H' = (i/2)[R_o, R_e], eps is conserved and there are 8 Weyl per flavour at K = 0 and R; each (eps, copy sign s) block at a node is one Weyl with chirality eps*s at K = 0 and -eps*s at R. The light copy (s = +1) holds, per eps sector, the zone-centre Weyl and one corner partner of the opposite chirality. Every eps-preserving mass at R pairs s = +1 with s = -1 (light with mirror). The only cell-local masses that anticommute with H' everywhere are eps-odd: with a 2-hop form factor (1 - B)/2 they gap the corner partners in light-light pairs and leave K = 0 untouched, but they break the charge that protects the light chirality. On one SU(4) block atom, the composite Phi = eps m^+m^+m^+/6 re-gaps a light level only through the anomalous G_(m,Phi), at 2 w lam/g; in a band that self-energy is a spin-blind node shift (Fermi pocket), not a mass. Composite spectra of extended mirrors, interacting 3D phases and Spin(10) are not computed.

**Kind of statement.** Exact on supplied free bands (the cube tick at one parameter point and its step-pi/2 generator) and a one-block exact diagonalisation for the composite pairing; dependent on a supplied model.

**Dependencies.** Uses #9992 (block-quartic mirror) and the generator H' of #9905 (logged). Relied on by #10004 and #9994. Note the symbol collision: eps is both the tick step and the sublattice sign; R is both the corner and the reflections R_o, R_e.

**Runner.** [`the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_2026_10_22.py`](../scripts/the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_2026_10_22.py); cached output [`the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_2026_10_22.txt`](../logs/runner-cache/the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_2026_10_22.txt); source note at head `2d3e5652c6` of branch `claude/toe-light-partner-gap-20261021`: `docs/THE_LIGHT_COPY_ZONE_CORNER_PARTNERS_ARE_VECTOR_LIKE_ONLY_THROUGH_THE_SUBLATTICE_CHARGE_BOUNDED_THEOREM_NOTE_2026-10-22.md`.

**Note text, verbatim** (title line dropped; no section omitted). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem.
Primary runner: `scripts/the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_2026_10_22.py`.

The [block-quartic note](THE_BLOCK_LOCAL_QUARTIC_GAPS_THE_DIRAC_MIRROR_SYMMETRICALLY_AND_RELEASES_THE_LIGHT_PARTNERS_BOUNDED_THEOREM_NOTE_2026-10-22.md) showed that a block-local quartic gaps a Dirac mirror symmetrically. The cost is that the symmetric gap releases every light mode that was gapped only by pairing with the mirror. The [candidate-law register](CANDIDATE_LAWS.md) therefore asks for a rule that removes the light copy's zone-corner partners without the mirror. This note counts those partners exactly and tests three removals:
- the copy mass;
- a light-only corner mass;
- pairing with the mirror's three-fermion composites.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

##### Statement

1. (CL-1 tick.) The tick has eps = 0.3, mu = 0 and copy mass M = 0.2. At K = 0, 4 modes are at zero: the light copy s = +1, one Dirac (1 L + 1 R per flavour). The other copy sits at +-M. At R = pi(1,1,1) the light copy is at +-2 eps and the heavy copy at +-(2 eps - M). The X point is at 0.198 and 0.398, the M point at 0.311 and 0.511. No zero lies off K = 0 (16^3 grid). The sublattice sign eps anticommutes with R_e, R_o and the copy-mass generator (1 - s)R_e = R_e - iR1R2R3, and it commutes with s. So the tick removes the corner partner by itself, with no mirror, and it conserves no chiral charge. The copy mass is an eps-odd Dirac mass on the s = -1 copy.
2. (Chiral generator.) H' = (i/2)[R_o, R_e] commutes with eps. Its only zeros are at K = 0 and R, with 8 modes each and Clifford velocities of speed 1/sqrt3. Its cell-local commutant is span{1, eps}, and tr(g5 X) = 0 on that commutant at both nodes. At the nodes the copy sign s commutes with the velocities. Each (eps, s) block is one Weyl, with chirality eps*s at K = 0 and -eps*s at R.
3. (Census.) Per flavour:
   - Light copy: G_L(eps+) and G_R(eps-) at K = 0, with corner partners R_R(eps+) and R_L(eps-) at pi(1,1,1).
   - Mirror: G_R(eps+), G_L(eps-), R_L(eps+), R_R(eps-).
   - When the mirror gaps, the released light modes are one Weyl per eps sector at pi(1,1,1), of the opposite chirality to that sector's light Weyl: 2 per flavour.
   - If instead every light mode is paired to the mirror, as in the block-quartic test, all 8 are released.
4. (Copy mass.) It gaps the mirror copy's Dirac at K = 0 and moves only the heavy copy at R. It gaps no light partner, and it is eps-odd. It is not enough.
5. (Light-only corner mass.) The eps-preserving masses at R span 4 dimensions, and every one of them pairs s = +1 with s = -1, so they are light-mirror pairings (Golterman-Shamir). The cell-local masses that anticommute with H' at every K span 2 dimensions, and all of them are eps-odd. One of them, X, has X^2 = 1 and [X, B] = 0, where B = (R_oR_e + R_eR_o)/2 is a 2-hop term with [B, H'] = 0. Then H' + lam (1 - B)/2 X squares exactly to H'^2 + lam^2 (1 - B)^2/4:
   - every R mode is gapped by lam, the light partners R_R(eps+) pairing with R_L(eps-), which is opposite chirality and light-light;
   - K = 0 keeps its 8 zeros.

   But the same X with no form factor gaps K = 0 by lam, pairing G_L(eps+) with G_R(eps-) of the light copy. The partners are vector-like among themselves only under the breaking of the charge that also makes the zone-centre pair vector-like. This is Nielsen-Ninomiya in exact form.
6. (Composites, one SU(4) block.) The block term is -g(Q + Q^+). At w = 0, G_m = G_Phi = 0 and |G_(m,Phi)| = 1/g. With a light l_a coupled by w l^+m + lam l^+Phi (exact diagonalisation, 256 states, w = lam = 0.05), the light level is:
   - with w alone: 1.2e-4 (released);
   - with lam alone: 9e-6 (released);
   - with both: 0.00498 g, against 2 w lam/g = 0.00500.

   In a band this self-energy is a number, not a matrix in spin. On a Weyl node it is a shift mu, with a zero of sigma.k + mu at |k| = mu: a Fermi pocket, not a gap. A Weyl gaps only with an opposite-chirality partner in its own eps sector (the mirror's R_L), or by a Majorana pair, and 16 x 16 has no Spin(10) singlet. Spin(10), Z4, eps and spin act alike on G_L and on its partner, so only momentum separates them.

##### Derivation

- (1) The tick is computed at the eight inversion-symmetric points and on a grid. The eps relations hold because each hop and the three-hop product join opposite sublattices, while s is a product of four hops.
- (2) The velocities are finite differences of H' at the node, and g5 = i a1 a2 a3 / v^3. The commutant is the null space of [., H'(K)] over five random K. The chirality per block is tr(g5 P_(eps,s))/2.
- (5) The masses at R are the null space of {., a_i} together with [., eps]. The global masses are the null space of {., H'(K)}. Because B is a function of U = R_oR_e that commutes with H' and with X, the square follows.
- (6) Lehmann sums on the 16-state atom, plus exact diagonalisation of the 8-mode block.

##### Checks

A1-A6 (census), B1-B4 (corner mass), C1-C4 (composites). TOTAL: PASS=14 FAIL=0.

##### Clause count and law text

Tested candidate (law text, NOT proposed for adoption):

> "Corner term. Each species' generator carries lam (1 - B)/2 X, with B the symmetrised product of the two tilings' reflections and X the cell-local term anticommuting with the generator at every momentum; lam is a constant in proper units."

Smuggling check:
- Supplied: lam, and the choice of X within its 2-dimensional space.
- Chosen, not forced: the form factor (1 - B)/2, a 2-hop function of U that is 0 at K = 0 and 1 at R; uniqueness is not checked. Forced: X is eps-odd (B2).
- Hidden cost: X breaks eps, the only cell-local conserved label (A5). That label is what makes the light copy chiral (A6). So the term reopens the K = 0 Dirac mass. It would trade the corner doubler for a vector-like light copy.

Verdict:
- (a) The copy mass is insufficient.
- (b) A light-only corner removal exists exactly, but it necessarily breaks the light chirality.
- (c) Composite pairing is spin-blind on a Weyl. It moves the partner to a Fermi pocket and does not gap it.

No rule is adopted. The requirement now has an exact form. The light corner partner R_R(eps+) can be gapped only by an L Weyl of the same eps sector at R. On these bands, the only such Weyl is the mirror's R_L(eps+). So the mirror term must gap the mirror symmetrically at K = 0 while it stays Dirac-paired with the light copy at R. That needs a mirror interaction whose symmetric zero vanishes at R, an intermediate, momentum-selective phase: the register's open SMG route, and not a cell-local term.

##### Boundary

- Free bands only: the CL-1 tick at one (eps, M) point and its step-pi/2 generator.
- The composite test is on one SU(4) block, with no dispersion. The spin-blindness argument assumes that G_(m,Phi) is spin-scalar at w = 0, as it is on the block.
- Not computed: the composite spectra of an extended symmetric mirror, any 3D interacting phase, Spin(10), twelve-turn covariance of X (the register states that no eps-preserving mass at R is turn-invariant), and links.

---

### #10004: zoomed filtered mirror term keeps the chiral Z4; the 16-Weyl toy is anomaly-free with an unresolved K gap

**Statement (the note's own `claim_scope`, verbatim).**

> Two parts. (I) CL-1 tick (step-pi/2 generator H'), exact: the fine cube-filtered mirror term keeps no Z4 inside U(1)_eps (only fermion parity); the same filter applied one rung up (over the 8 cells of a cell cube, on eps-pure mirror cell orbitals) keeps Z4_eps, vanishes at the cell corner R, and is orthogonal to the light copy at K; a corner pairing w (1 - B)/2 Y keeps eps, leaves the 8 K zero modes and gaps R with no new zero on a 12^3 grid; the K mirror carries Z16 index 2 per mode member under Z4_eps. (II) SU(4) MODEL (not a rule) with 16 Weyl at K: two tastes per flavour of a K/R Weyl band, taste-mixing spin-twisted cube-filtered rows on the mirror, light paired at R only. Exact: sign-free (det(M)^4, M real); light K and the whole R sector are decoupled by construction; an exhaustive search of the band commutant finds every Z4-type symmetry of H_int at Z16 index 0 mod 16 (taste-diagonal rows keep an index-8 symmetry). Correction to momentum-selective-mirror: the one-taste obstruction is Z4 of mode number, not Z4_J (the two J sectors are time-reversal partners of equal chirality). Finite diagnostics (sign-free CT-INT, beta = 4, L = 4, 6, g/t = 2, 4, 8, short L = 6 runs): g/t = 8 shows no order (S_pair/N falls 8-11x against volume 3.4) and a K-mirror gap 0.93-1.05 g at L = 6, 40x the zero-mode-atom baseline but half its L = 4 value (2.2(5)); g/t = 2 shows pair correlations that do not fall with volume; g/t = 4 is seed-dependent. Survival of the K gap as L -> infinity is not established: inconclusive.

**Kind of statement.** Part I exact on the supplied cube tick. Part II is an SU(4) model (the note says not a rule): exact statements plus a numerical diagnostic (sign-free interaction-expansion Monte Carlo, beta = 4, L = 4, 6). The outcome for the K-mirror gap is inconclusive.

**Dependencies.** Depends on #9994 (superseded and corrected here), #9993 and #9992. The Spin(10), 16-per-cell content is inherited from the supplied cube-tick mode content, not forced by this term. Cites the Z16 classification of Spin x_Z2 Z4 in 3+1D.

**Corrections and narrowings that apply to this statement.** Corrects #9994: the one-taste index-eight obstruction belongs to the Z4 of mode number (Z4_N), not to Z4_J; the two J sectors are time-reversal partners of equal chirality, so Z4_J is vector-like. See the section "Corrected or replaced claims".

**Runner.** [`the_zoomed_filtered_mirror_term_keeps_the_chiral_z4_and_the_16_weyl_toy_is_anomaly_free_with_an_unsettled_k_gap_2026_10_22.py`](../scripts/the_zoomed_filtered_mirror_term_keeps_the_chiral_z4_and_the_16_weyl_toy_is_anomaly_free_with_an_unsettled_k_gap_2026_10_22.py); cached output [`the_zoomed_filtered_mirror_term_keeps_the_chiral_z4_and_the_16_weyl_toy_is_anomaly_free_with_an_unsettled_k_gap_2026_10_22.txt`](../logs/runner-cache/the_zoomed_filtered_mirror_term_keeps_the_chiral_z4_and_the_16_weyl_toy_is_anomaly_free_with_an_unsettled_k_gap_2026_10_22.txt); source note at head `26fc2db5d1` of branch `claude/toe-ax7-chirality-16weyl-20261021`: `docs/THE_ZOOMED_FILTERED_MIRROR_TERM_KEEPS_THE_CHIRAL_Z4_AND_THE_16_WEYL_TOY_IS_ANOMALY_FREE_WITH_AN_UNSETTLED_K_GAP_BOUNDED_THEOREM_NOTE_2026-10-22.md`.

**Note text, verbatim** (title line dropped; no section omitted). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem.
Primary runner: `scripts/the_zoomed_filtered_mirror_term_keeps_the_chiral_z4_and_the_16_weyl_toy_is_anomaly_free_with_an_unsettled_k_gap_2026_10_22.py`.

The [light-partner note](THE_LIGHT_COPY_ZONE_CORNER_PARTNERS_ARE_VECTOR_LIKE_ONLY_THROUGH_THE_SUBLATTICE_CHARGE_BOUNDED_THEOREM_NOTE_2026-10-22.md) requires a mirror term that gaps the mirror symmetrically at K = 0 while the mirror stays Dirac-paired with the light copy at the corner R, and that keeps a Z4 inside U(1)_eps. The [momentum-selective note](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/d2a4f35a7dc8dffe8fe5926104be2a50d3510709/docs/THE_CUBE_FILTERED_MIRROR_TERM_IS_MOMENTUM_SELECTIVE_BUT_THE_SU4_TOY_K_MIRROR_IS_ANOMALOUS_BOUNDED_THEOREM_NOTE_2026-10-22.md) found its one-taste toy blocked by a Z16 index of 8. This note (I) checks the symmetry on the CL-1 tick and (II) runs the 16-Weyl toy. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

##### I. The CL-1 tick (exact)

Setting: H' = (i/2)[R_o, R_e] on 8-site cells, cell momentum K, sublattice sign eps, copy sign s (mirror s = -1), as in the light-partner runner.

1. (C1) Every fine 2x2x2 cube, in every alignment, holds 4 sites of each eps. So e^(i theta eps) maps the cube row r to e^(i theta) r_+ + e^(-i theta) r_-, which has the same support. That is a multiple of r only for theta = 0 or pi, and at theta = pi/2 the image is orthogonal to r (|<r, U r>| = 6e-17). **The fine cube-filtered term keeps no Z4 inside U(1)_eps, only fermion parity.** As written in the register, the term breaks the symmetry the light copy's chirality needs.
2. (C2) The fix is one rung up (zoom). Take the rows psi_(C,u) = 8^-1/2 sum over the 8 cells of the cell cube at C of u . c_cell, with u an eps-pure mirror cell orbital. The space s = -1, eps = +-1 has dimension 2 per sign per cell, and [eps, s] = 0.
   - Each row picks up the phase i^eps under Z4_eps, so a charge-4 product of one eps sign keeps Z4_eps. U(1)_eps is broken to Z4.
   - The cell form factor prod(1 + e^(iK_j)) is exactly 0 at R.
   - At K, H'(0) = 0 and s is exact there. The rows lie in s = -1, so they are orthogonal to the light copy (overlap 2e-16).
   So the light K modes and the whole R sector never enter the zoomed term, exactly as in the toy.
3. (C3) Corner pairing: w {(1 - B)/2, Y}/2. Here B = (R_oR_e + R_eR_o)/2 is a 2-hop term, (1 - B)/2 is 0 at K and 1 at R, and Y is taken from the 4-dimensional space of eps-even masses at R. Every element of that space pairs light with mirror.
   - At w = 0.3: eps is conserved (2e-16), K keeps its 8 zeros, the R gap is 0.283, and min |E| off K on a 12^3 grid is 0.283.
   - The free tick therefore realises the required corner structure. This is the light-mirror pairing at R that the toy supplies as w prod sin^2(k/2).
4. (C4) Under Z4_eps the K mirror is, per mode member, G_R(eps+) and G_L(eps-). The chiralities are +1 and -1 for charges +1 and -1, so both are left-handed with one charge. The index is 2 per member. A symmetric trivial gap of the K mirror under this term needs n = 0 mod 8 members per cell: the register's 16 passes, and 15 (no gauge-singlet member) fails.

##### II. The 16-Weyl SU(4) model (the SU(4) is a model, not a rule)

5. (Model, A1-A2) Two tastes per flavour of the realified K/R Weyl band of the momentum-selective note: mirror -h, light +h, pairing w prod sin^2(k_i/2) diagonal in taste.
   - Mirror rows are r_(alpha,+-) = (e_(alpha,1) +- e_(sigma alpha,2))/sqrt2 with sigma = spin flip. They are orthonormal and taste-mixing, and they entangle taste with spin, so no symmetry of the band rotates them to taste-diagonal rows.
   - H_int = -g sum over cubes and rows of (psi_1 psi_2 psi_3 psi_4 + h.c.), with psi = 8^-1/2 sum over the cube.
   - At L = 4 the only zeros are the 16 K modes per flavour. Every R mode sits at w.
   - The filter is exactly 0 at R, so light K and the whole R sector are decoupled. The light K gap is 0 and the R gap is the free paired value at every g, by construction.
6. (A3, symmetry and anomaly; theorem) The commutant of the mirror band has dimension 8. Searching it exhaustively for unitaries that map every row to i^k times a row gives:
   - Taste-mixing rows: a group of 32 elements with 16 elements of Z4 type (U^2 = (-1)^F), every one with Z16 index 0 mod 16.
   - Taste-diagonal rows: 128 elements, including an index-8 symmetry (the mode phase on one taste only).
   - The two J sectors are time-reversal partners. They have the same chirality and J-charges +-1, so Z4_J is vector-like (index 0). The chiral symmetry is Z4 of mode number: index 16 = 0 with two tastes, and 8 with one.

   Correction: the momentum-selective note's index-8 obstruction is real, but it belongs to Z4_N, not Z4_J. Its item 5 labels it wrong, and the conclusion stands.
7. (A4) Sign: the row tables are real (max |Im| = 0) and the 4 flavours see the same real M, so the weights are g^2n det(M)^4 >= 0.
8. (A5, exact ED) Zero-mode atom baseline. Projected to K, the quartic is -g(64/L^3) sum (Q + Q^+) on 4 identical 8-mode blocks. At beta = 4 its K midpoint gap is 0.465 g (L = 4) and 0.025 g (L = 6), with level gaps 1.000 and 0.296 g.
9. (Finite diagnostics; recorded production, prod3.py, 82 s segments, g = 1, w = t/2, beta = 4)

| | L = 4 | L = 6 seed 1 | L = 6 seed 2 |
|---|---|---|---|
| g/t = 2: K gap | 2.26(22) | 2.14(35) | 1.34(19) |
| S_pair/N (free) | 1.98 (0.169) | 1.69 (0.054) | 1.33 |
| xi/L | 0.71 | 0.89 | 0.82 |
| g/t = 4: K gap | unresolved (G(beta/2) 0.0006(33)) | 1.05(8) | 1.24(17) |
| S_pair/N | 2.02 (0.146) | 0.46 (0.044) | 0.90 |
| xi/L | 0.74 | 0.47 | 0.61 |
| g/t = 8: K gap | 2.20(51) | 1.05(3) | 0.93(5) |
| S_pair/N | 1.12 (0.122) | 0.141 (0.036) | 0.106 |
| xi/L | 0.54 | 0.24 | 0.18 |

The J-odd mass channels (all 20 K masses; every K mass is J-odd and every pair is Z4_N-odd) are below free in every run: S/N 404-476 against 532-547.

The L = 6 runs are short: 77-101 sweeps, 38-50 measurements, <2n> about 1850-2020. At g/t = 4 the spread between seeds exceeds the jackknife error.

Reading:
- g/t = 8: no order to L = 6. S_pair/N falls 7.9-10.6x against a volume ratio of 3.375, and xi/L falls. The K gap at L = 6 is about 1 g, 40x the zero-mode atom, so it is not the atom. But it is half its L = 4 value.
- g/t = 2: pair correlations do not fall with volume (ratio 1.2-1.5) and xi/L does not fall. This is consistent with pair order, or with MC that is too short.
- g/t = 4: undecided.

The trend is the reverse of the one-taste toy: symmetric at strong coupling, correlated at weak coupling, as for anomaly-free SMG.

##### Verdict

- Light K massless: exact (by construction in the model; on the tick, orthogonality at K plus Z4_eps).
- R paired: exact (decoupling; the tick's corner pairing realises it in the free band).
- Z16 index 0: yes (model, exhaustive within the band commutant; tick: 0 for n = 0 mod 8).
- Sign-free: yes.
- Z4 inside U(1)_eps: lost by the fine cube filter (C1). Kept by the zoomed filter (C2).
- Mirror K gap survives L -> 6 with no order: at g/t = 8 there is no order and a gap of about 1 g at L = 6, but the gap halves from L = 4 to 6. At g/t = 2 the pair correlations persist.

Overall: **INCONCLUSIVE.** The anomaly no longer forbids the momentum-selective symmetric phase, and the strong-coupling data are compatible with it, but no L-independent gap is shown.

##### Rule text (tested candidate, NOT adopted; for AX-7)

> "AX-7 (Mirror term, zoomed). The mirror term acts one rung above the site: on each cube of eight cells, for each sublattice sign, it is the charge-4 term of that sign's mirror cell modes, averaged over the eight cells, that is invariant under every mode rotation the update keeps, with one coupling everywhere. The light-mirror pairing at the cell corner is the cell-local sublattice-even light-mirror term weighted by (1 - B)/2, B the symmetrised product of the two tilings' reflections."

Smuggling check (anti-smuggling gate):
- (1) Measured numbers chosen: none. The values g and w are supplied constants. The toy's g/t, w = t/2, sizes, betas and seeds are model settings, not fitted.
- (2) Observed structure inserted by name: the rule names no gauge group or content. It selects the term by "invariant under every rotation the update keeps", but which group that is comes from the register's CL-1 mode content, where Spin(10) and the 16 per cell are register inputs. The uniqueness of the pair square was shown for Spin(10) in the block-quartic note, not derived here. So the content is inherited from CL-1, not forced by this rule. The SU(4) flavour group and the flavour and taste counts are a MODEL. The rule also chooses: the eps-pure split (forced by Z4_eps, C1-C2), the rung (forced by C1), the mirror copy (register), the form factor (1 - B)/2 and the choice of Y within its 4-dimensional space (not unique; supplied).
- (3) Prediction it was not built for: the symmetric K gap needs the member count per cell n = 0 mod 8 (C4). Fifteen fails and 16 passes, so the rule needs a gauge-singlet member per family (a right-handed neutrino). It is consistent with neutrino masses, but not a sharp test. The dynamical claim (a symmetric gapped K mirror) is UNTESTED beyond L = 6.
- (4) Axiom bent: nearest-neighbour admissibility (the term spans 4x4x4 fine sites, and the corner term is 2-hop in cells). It also uses the role-block layout of AX-2 (bends Lattice).

Gate result: the rule passes (1) and (4). It passes (2) only conditionally, since it inherits CL-1's content. Its prediction (3) is weak and its central dynamical claim is untested. It is NOT adopted.

##### Boundary

- The SU(4) model is not Spin(10), and the band is not the tick. The tick checks are free-band and symmetry-level only. The zoomed term on the tick was not simulated.
- Symmetry search: unitary symmetries inside the band commutant only. Antiunitary (Pin+) indices, lattice-symmetry combinations and mixed gauge anomalies are not computed.
- QMC: beta = 4 only, L <= 6, short L = 6 chains, a midpoint estimator (lower-bound style), no Binder ratio. The xi/L at L = 4 is contaminated by the K zero modes.
- No L = 8 and no beta = 8 at L = 6. These are the decisive next runs: g/t = 8 and 16 at L = 6 with longer chains, and L = 8.

---

### #10030: corner stabilizer forces a scalar light block at X and M

**Statement (the note's own `claim_scope`, verbatim).**

> Any cell walk covariant under the 12 tetrahedral rotations T (CL-1's site gauges), on the FREEZE cell content (light label tau3 = +1 on Pi+, a spinor doublet). Exact: X and M are fixed mod 2 pi by the D2 subgroup of T, whose lift Q8 acts irreducibly on the light doublet, so the light-labelled block of the walk (and of any T- and cell-translation-symmetric light Green's function) is a scalar at X and M. Consequence (exact, continuity): with a Weyl at K = 0 at quasienergy 0, the light-labelled sector is gapless at or around every X and M -- a node at quasienergy 0 or pi, a crossing surface, or a zero of the light block. No light-light partner mass exists. Finite diagnostics: 3 random T-covariant deformations; a designed light-light scalar layer; corner chirality bookkeeping of FREEZE (net +2 at 0 and at pi per family). Not covered: translation-breaking (zoomed) rules beyond the Schur remark in section D, and the infinite-lattice interacting phase.

**Kind of statement.** Exact (Schur lemma on the lift Q8 of the diagonal rotations D2, plus a continuity corollary) for any T-covariant, cell-translation-invariant cell walk on the FREEZE cell content; finite diagnostics on three random deformations and one designed layer; the zoom remark is a Schur argument derived but not run.

**Dependencies.** Uses FREEZE as defined in #10041. Lists #10031 (logged) as upstream: the note treats the release of the light partners found there as generic and does not recompute it. Floquet chiral-magnetic and Z16 inputs are cited and not used in the proof.

**Runner.** [`the_corner_stabilizer_forces_a_scalar_light_block_at_x_and_m_so_no_rotation_covariant_freeze_deformation_gaps_the_light_partners_light_light_2026_10_23.py`](../scripts/the_corner_stabilizer_forces_a_scalar_light_block_at_x_and_m_so_no_rotation_covariant_freeze_deformation_gaps_the_light_partners_light_light_2026_10_23.py); cached output [`the_corner_stabilizer_forces_a_scalar_light_block_at_x_and_m_so_no_rotation_covariant_freeze_deformation_gaps_the_light_partners_light_light_2026_10_23.txt`](../logs/runner-cache/the_corner_stabilizer_forces_a_scalar_light_block_at_x_and_m_so_no_rotation_covariant_freeze_deformation_gaps_the_light_partners_light_light_2026_10_23.txt); source note at head `0a4a61ee54` of branch `claude/toe-freeze-gapped-partners-20261021`: `docs/THE_CORNER_STABILIZER_FORCES_A_SCALAR_LIGHT_BLOCK_AT_X_AND_M_SO_NO_ROTATION_COVARIANT_FREEZE_DEFORMATION_GAPS_THE_LIGHT_PARTNERS_LIGHT_LIGHT_BOUNDED_THEOREM_NOTE_2026-10-23.md`.

**Note text, verbatim** (title line dropped; sections omitted (gate, smuggling-review, repo-check and mapping sections, which describe the review procedure and not the result): Gate (the candidate rule "add a T-covariant light-light layer that gaps the X/M light partners"); Smuggling review; Next). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem (one exact Schur statement plus an exact continuity corollary; numerics labelled).
Runner: runner.py, TOTAL: PASS=6 FAIL=0, 0.9 s, 84 MB peak, 2.4 k characters; run through
scripts/runner_cache.execute_runner under a unique filename (status ok, exit 0). Axioms unchanged.

##### Question

freeze-mirror-smg asked for a T-covariant, cube-local FREEZE variant whose light-labelled projection has no
nodes at X and M, so that the X/M light partners are gapped among light modes and a mirror-only charge-4
term could then gap the mirror without releasing them.

##### A. Theorem (exact)

- A1. X = (pi,0,0) and M = (pi,pi,0) (and their T-images) are fixed mod 2 pi by the four diagonal rotations
  D2 of T. The light label is V-invariant, and D2 lifts to Q8 on it, with a commutant of dimension 1
  (irreducible). For any T-covariant U, V_R U(X) V_R^+ = U(R X) = U(X), so P_L U(X) P_L is a scalar. The
  same holds at M.
  - The A4 characters w^q are trivial on D2, so this holds for either label and any family count.
  - It uses only T-covariance and cell-scale translation. It does not depend on depth, range, light-mirror
    mixing, or Pi+/Pi- mixing.
- A2 (corollary, continuity). Take the polar part of the light-labelled block, or the inverse light Green's
  function at zero frequency. Either one is a T-covariant 2x2 function on the torus with a Weyl at K = 0, and
  it is scalar at X. Its two eigenvalues are a band that rises from 0 and a band that falls from 0, and they
  coincide at X.
  - A band gapped away from isolated nodes stays on one side of 0 (and of pi). Two such bands can coincide
    only at 0 or pi.
  - So exactly one of three things happens: (i) X is a node at quasienergy 0 or pi; (ii) a band crosses 0 or pi
    along a surface (a light Fermi surface); (iii) the light block vanishes or the Green's function has a zero.
  - In case (iii) the local winding around X is preserved (it is topological), so the partner survives as a
    Golterman-Shamir zero with its old chirality.
  - The same argument holds at M relative to R at quasienergy pi.
- Therefore no deformation of FREEZE, free or interacting, T- and translation-symmetric, leaves the
  light-labelled sector with only the K = 0 and R Weyls. A light-light mass at X would be a 2x2 term that
  commutes with Q8, which is a scalar: it shifts the 2-fold X level and never splits it.

##### B. Finite diagnostics

- B1. 3 random T-covariant deformations U_F exp(i H_cov) (H_cov a rotation-twirled random Bloch Hamiltonian on
  all 8 modes). Covariance holds to 4e-15, and the light block at X, M is scalar to 2e-15. Its phase at X is
  generic (-1.38, -0.61, 1.32), not 0 or pi, so by A2 those cases have light crossing surfaces.
- B2. The designed light-light layer exp(i a phi(K) tau3 Pi+), with phi = 3 - sum cos K_i cos K_j, is
  T-invariant, vanishes at K = 0 and R, and equals 4 at X and M.
  - The node Weyls are untouched (U = U_F exactly there).
  - The X level stays 2-fold and moves to quasienergy 4a.
  - The lower light band crosses 0 on the line 0 -> X at s = 0.919 (a = 0.1) and at s = 0.691 (a = 0.25).
    That crossing is a light Fermi surface, which is the partner smeared rather than gapped.

##### C. Anomaly bookkeeping (light-labelled projection of FREEZE, polar part; matches freeze-mirror-smg C2)

- Light: K = 0 and R carry -1; the 3 X (quasienergy 0) and the 3 M (pi) carry +1. Net +2 at 0 and +2 at pi.
- Mirror: exactly opposite (-2, -2), and the total is 0, as a cube-local circuit requires (total winding 0).
- The target content of the light sector, the K = 0 and R Weyls only, would be net -1 at 0 and -1 at pi. That
  is a nonzero Floquet 3D winding.
  - It is not Nielsen-Ninomiya consistent as a stand-alone static sector.
  - It is allowed only as a Floquet-anomalous sector, which is a LITERATURE fact (Floquet chiral magnetic
    effect, Higashikawa-Nakagawa-Ueda 2019) and is not used here.
  - It would need the mirror to carry the opposite winding, so the mirror cannot then be gapped trivially by
    mirror-only terms.
- The Spin-Z4 count of the gapped mirror set is unchanged from freeze-mirror-smg: 2 N_f mod 16 (8 at
  N_f = 4).
- A1 forbids the target at the free level regardless of this bookkeeping.

##### D. Zoom remark (exact Schur, derived in this note, not run)

On a doubled superlattice (translation broken from 2 to 4 sites), the corners fold to the superlattice
centre, where the full binary tetrahedral group 2T acts. The irreps are:
- light at K = 0: s(x)w (-1);
- light X-triplet: s(x)w (x) {1, omega, omega-bar} = {s(x)w, s(x)w^2, s} (+1 each).

A light-light mass needs the same irrep with opposite chirality. That gives:
- Only s(x)w can pair, and that pairs the K = 0 light Weyl with an X combination, which kills the Weyl.
- s(x)w^2 and s have no light partner. Their only same-irrep, opposite-sign partners are mirror modes.

Zooming therefore does not give light-light partner gapping either (at the corner fixed point; nodes moved off
the fixed point are not covered).

##### Answers

1. A T-covariant FREEZE variant with light-labelled nodes only at K = 0 and R: does NOT EXIST. This is exact,
   for any depth or range and any mixing (A1-A2).
2. Mirror-only charge-4 gapping without releasing partners: impossible under T and translation, whatever the
   mirror term is. After any symmetric mirror gapping, the light Green's function block is still scalar at X
   and M (A1), so the partners come back as poles, a pole surface, or zeros (A2). The release found in
   freeze-mirror-smg (B4b) is therefore GENERIC; it is not a FREEZE accident. Not recomputed here.
3. Light-sector net chirality: +2 at 0 and +2 at pi per family on FREEZE. The target content would be a
   Floquet winding of -1 that a mirror-only gap cannot cancel.

Verdict: NO-GO (exact, bounded to T-covariant cell-translation-invariant rules). The obstruction is the Q8
stabilizer of the zone-boundary corners acting irreducibly on the light spinor, not the specific FREEZE gates.
Walls move: what escapes the theorem is a rule that breaks either (a) the D2 part of the corner stabilizer on
the light doublet, for example a light label that is not a spinor doublet, as in a composite multi-cell label,
or (b) the cell-scale translation in a way that moves the partners off fixed points. Neither is tested here.

---

### #10041: composite TWIST walk is a five-layer cube-local circuit; freezing one copy leaves one L and one R per node

**Statement (the note's own `claim_scope`, verbatim).**

> Free bands of composite TWIST (CTWIST) on CL-1's 2^3 cell (one mode per site, 8 cell states, the 12 tetrahedral rotations T with CL-1's site gauges). (A) CTWIST is not an even.odd.even product of cube-local layers (exact), but it is exactly a five-layer cube-local circuit even.odd.even.odd.even on CL-1's two tilings; no circuit whose layers each commute with the site rotations was found to depth 9 (finite search). (B) At the T-fixed nodes every level of any T-covariant cell walk is a 2-fold spinor irrep, and the two eta copies carry identical irreps (T acts trivially on the eta algebra), so no free T-keeping term removes the doubling. Rule FREEZE (the sector where CL-1's chirality disagrees with the walk's does not hop) is unitary, T-covariant, a five-layer cube-local circuit, and leaves exactly one L (q = 2) and one R (q = 1) per node. (C) A free label term exp(i phi (1 - tau3)/2) relocates the R Weyl but never gaps it. Not covered: interactions, the multi-family mirror term, measurement.

**Kind of statement.** Exact free-band statements, plus one finite search (no factorisation with every layer commuting with the site rotations found at depth 5, 7, 9; not a proof). Dependent on a supplied walk (CTWIST) and a supplied selector. FREEZE is a bounded candidate, which the note does not adopt; it admits that FREEZE removes the doubling by declaring half the cell inert.

**Dependencies.** CTWIST is the composite twist walk of #10028 (logged), built from the atomic twist of #10043 (logged). Relied on by #10030, #10042, #10064 and #10073, and by the logged #10031, #10065, #10070 and #10074 and the kept #10072.

**Corrections and narrowings that apply to this statement.** The question this note leaves open (whether some covariant layering exists, with the finite search finding none) is answered for gates commuting with the (111) turn by #10064 (FREEZE is not a product of T3-commuting cube-local gates at any depth) and #10065 (W(CTWIST) = W(U_A) = 2 W_F). See the section "Corrected or replaced claims".

**Runner.** [`the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_2026_10_23.py`](../scripts/the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_2026_10_23.py); cached output [`the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_2026_10_23.txt`](../logs/runner-cache/the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_2026_10_23.txt); source note at head `dd9464ccc1` of branch `claude/toe-twist-local-single-20261021`: `docs/THE_COMPOSITE_TWIST_WALK_IS_A_FIVE_LAYER_CUBE_LOCAL_CIRCUIT_AND_FREEZING_ONE_COPY_LEAVES_ONE_L_AND_ONE_R_PER_NODE_BOUNDED_THEOREM_NOTE_2026-10-23.md`.

**Note text, verbatim** (title line dropped; sections omitted (gate, smuggling-review, repo-check and mapping sections, which describe the review procedure and not the result): Smuggling review). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem (exact free-band statements, plus one finite search labelled as such).
Runner: runner.py, TOTAL: PASS=12 FAIL=0, 10.6 s, 90 MB peak, stdout 3.5 k characters; run through
scripts/runner_cache.execute_runner under a unique filename (status ok, exit 0). Axioms unchanged.

##### Question

composite-twist left three items open on CTWIST, U(K) = f + i(h1 tau1 + h2 tau2 + tau3 g.sigma):
(i) the light content is doubled by CL-1's chirality eta = chi acting as a spectator;
(ii) the hop spans up to 3 site steps -- is the walk a product of cube-local (2^3) layers on CL-1's two tilings?
(iii) after (i)-(ii), is the content one L (q = 2) and one R (q = 1) per node, and what does a label mirror
term (1 - tau3)/2 do?

##### A. Layers (item ii)

- A1 (exact no-go, depth 3). Any even.odd.even product C1 D C2 D^+ C3 (D = diag(e^{-iK.a}); this contains
  CL-1's own odd.even shape) needs the ranges of the z_i coefficients to cut the cell into 8 one-dimensional
  vertex spaces. CTWIST's three range projectors have rank 4 and commute, but their joint spaces have dims
  (2,2,2,2,0,0,0,0): two states on each vertex of one tetrahedron. So depth 3 is impossible.
- A2 (exact, depth 5). CTWIST = C1 . O(C2) . C3 . O(C4) . C5 with C1, C3, C5 even-cube gates and O(C) = D C D^+
  odd-cube gates. The product has degree <= 2 per direction, so the 5^3 momentum grid identifies it; the
  residual is 1e-14 on the grid and off it. The gates are found by block-coordinate (polar) ascent, so they are
  numerical, not closed form; the identity is exact to float precision. Conjugating by C5 gives two CL-1-shaped
  ticks (odd.even.odd.even) with different gates.
- A3 (finite diagnostic). With every layer commuting with the 12 site rotations (frames V; diagonal gauges are
  absorbed into the gates), no factorisation was found at depth 5, 7 or 9 (rms floors 1.59, 1.30, 1.25). The
  depth-5 gates found are not T-invariant. T-covariance holds for the full walk, not gate by gate. This is a
  search, not a proof.

Answer (ii): the walk splits into cube-local layers, so CTWIST does NOT bend nearest-neighbour admissibility.
Its status is the same as CL-1's tick, with five layers instead of two. Open: whether some covariant layering
exists (A3 found none).

##### B. The eta doubling (item i)

- B1 (exact). Every T-invariant on-cell operator commutes with sigma and tau3 (dim 8 = M2 + M2 on the eta
  copies). At the T-fixed nodes K = 0 and R, U(node) is such an operator for ANY T-covariant cell walk, so every
  level there is a 2-fold spinor irrep. A free T-keeping term can move node quasienergies; it can never gap a
  node Weyl.
- B2 (exact). The eta algebra (commutant of sigma and tau) is M2 = <chi, eta_x>, and T acts on it trivially. The
  two copies have identical irreps at both nodes, so no rotation tells them apart. Only a cell operator (chi) can.
  The doubling therefore cannot be removed by a free term built from T alone. A rule has to use chi.
- B3 (exact). Chirality agreement: the T-invariant cell relabelling Y = P_w + P_wbar eta_x gives U_A = Y U Y^+,
  whose taste flips are tau_1,2 eta_x. U_A conserves Pi+ = (1 + chi tau3)/2, the states where CL-1's chirality
  agrees with the walk's. eta_x is an exact symmetry of U_A that swaps Pi+ and Pi-, so choosing Pi+ is a
  convention, not a lopsided physics choice.
- Rule FREEZE: U_F = Pi+ U_A + Pi- (i tau3). The disagreeing sector does not hop; each cell ticks it by a
  quarter phase.
  - B4. U_F is unitary and T-covariant. On a 12^3 grid, quasienergy 0 occurs only at K = 0 and pi only at R
    (gap >= 0.30 elsewhere). The frozen states are flat at +-pi/2, the point equidistant from both node
    quasienergies.
  - B6. U_F is also exactly a five-layer cube-local circuit (residual 6e-15).

##### Answers

(iii) Light content. Under FREEZE, exactly one L Weyl (q = 2) and one R Weyl (q = 1) sit at each node (B5):
2 L + 2 R in all, half of CTWIST's 4 + 4. By Schur (B1, different characters), no T-invariant L-R mass exists.
R10 still holds (every light L at q = 2), now with n_L halved.

Label mirror term (C1-C2, exact plus one root-find):
- exp(i phi (1 - tau3)/2) on Pi+ never gaps the R Weyl. At phi = pi/2 it moves the K = 0 R Weyl to pi/2, still
  a 2-fold irrep, and opens a quasienergy-0 Fermi surface: sigma_min(U - 1) = 7e-9 at k = 2.22 on a generic line.
- At phi = pi, the R-labelled states at the R node land at quasienergy 0.
- The label is exact at the nodes and leaks O(K^2).

Any free label term therefore only relocates the mirror. Separating it needs an interacting term. As in
composite-twist, w^(4q) != 1 per family, so that term must be multi-family (the SMG route), which is not
computed here. R11 (light and mirror at different momenta) is still NOT MET.

Gate (rule FREEZE):
1. Numbers: none fitted. The +-pi/2 placement is the point equidistant from the two node quasienergies, and the
   +i versus -i assignment is fixed by tau3. Pass, with that convention flagged.
2. Named structure: none. It uses chi (CL-1's own chirality) and tau3 (cell geometry). Pass.
3. Prediction not built for: 4 cell-local, non-propagating modes per cell at quasienergy +-pi/2 (inert dark
   states in the vacuum); light content 2 L + 2 R with a pinned pi-node. Not compared with measurement. UNTESTED.
4. Axiom bent: none. One mode per site; a five-layer cube-local circuit (A2, B6). As with CTWIST, it replaces
   CL-1's O-covariant tick with a T-covariant walk.

Result: FREEZE passes items 1, 2 and 4 and is UNTESTED on item 3. It is a bounded candidate, not adopted.
Honest weakness: FREEZE removes the doubling by declaring half the cell inert. It uses a structural selector,
but its motive is the count. B1-B2 show this is the minimal kind of rule possible at the free level, because no
T-keeping free term can do it.

---

### #10042: light Floquet winding forces the mirror to carry the opposite chirality

**Statement (the note's own `claim_scope`, verbatim).**

> Free-band, symmetry-level test of escape 1 of the corner-stabilizer no-go. The light label is defined on a doubled cell (2x2x2 CL-1 cells = a 4^3 block) by folding FREEZE's composite light label. The rule keeps the 12 tetrahedral rotations about the block centre (and, as a control, about a cell centre) and the doubled translations. Exact (Schur, finite group): every doubled-zone corner stabilizer acts reducibly on the light space. At the zone centre, the Gamma light Weyl's 2T irrep appears exactly once more, in one X combination, and the other two X irreps are distinct with no light partner; the same holds at pi for R and M. Exact (topology, any cell size, any walk-invariant splitting): the Floquet 3D winding W3 is additive over sectors, vanishes on any sector gapped at one quasienergy, and equals minus the net node chirality at 0 and at pi. Finite diagnostic: W3(light) = -2 and W3(mirror) = +2 on FREEZE. Not covered: interacting gapping (the Floquet anomaly is cited, not proven), and labels that are not walk-invariant sectors.

**Kind of statement.** Exact (Schur on finite groups; Floquet-winding topology) plus a finite diagnostic on FREEZE; free-band, walk-invariant sectors only. The Floquet anomaly is cited, not proven.

**Dependencies.** Uses #10030 and #10041; additivity of W3 as in #9863. Cites Higashikawa-Nakagawa-Ueda (2019) and the Golterman-Shamir zero route, neither used in a proof.

**Runner.** [`the_composite_two_cell_light_label_makes_the_corner_stabilizers_reducible_but_the_light_floquet_winding_forces_the_mirror_to_carry_the_opposite_chirality_2026_10_23.py`](../scripts/the_composite_two_cell_light_label_makes_the_corner_stabilizers_reducible_but_the_light_floquet_winding_forces_the_mirror_to_carry_the_opposite_chirality_2026_10_23.py); cached output [`the_composite_two_cell_light_label_makes_the_corner_stabilizers_reducible_but_the_light_floquet_winding_forces_the_mirror_to_carry_the_opposite_chirality_2026_10_23.txt`](../logs/runner-cache/the_composite_two_cell_light_label_makes_the_corner_stabilizers_reducible_but_the_light_floquet_winding_forces_the_mirror_to_carry_the_opposite_chirality_2026_10_23.txt); source note at head `6c1f04d6b4` of branch `claude/toe-two-cell-light-label-20261021`: `docs/THE_COMPOSITE_TWO_CELL_LIGHT_LABEL_MAKES_THE_CORNER_STABILIZERS_REDUCIBLE_BUT_THE_LIGHT_FLOQUET_WINDING_FORCES_THE_MIRROR_TO_CARRY_THE_OPPOSITE_CHIRALITY_BOUNDED_THEOREM_NOTE_2026-10-23.md`.

**Note text, verbatim** (title line dropped; sections omitted (gate, smuggling-review, repo-check and mapping sections, which describe the review procedure and not the result): Gate (candidate rule: "light label = composite two-cell (4^3-block) label, with a T-covariant light-light layer gapping the partners"); Smuggling review). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem (two exact statements plus one finite diagnostic).
Runner: runner.py, TOTAL: PASS=4 FAIL=0, 1.2 s, 106 MB peak, 2.4 k characters of stdout. It was run through
scripts/runner_cache.execute_runner under a unique filename: status ok, exit 0. Axioms unchanged.

##### Question

freeze-gapped-partners proved a single-cell obstruction. D2 lifts to Q8, which acts irreducibly on the light
spinor doublet, so the light block at X and M is scalar and the light partners cannot be gapped among light
modes. Escape 1 asks whether a composite two-cell light label avoids this, and if so, whether a covariant
cube-local light-light term can gap the extra partners while keeping only the K = 0 (and R) light Weyls.

##### Construction

- Doubled cell = 2x2x2 CL-1 cells (a 4^3 block). Doubled translations only; the single-cell translation is now an
  internal symmetry that the label may break.
- Folding: the doubled-cell Bloch space at Q is the sum over the 8 cell momenta K = Q/2 + pi n, with n in {0,1}^3.
  It is 64-dimensional.
- Rotations act about the block centre c = (1/2,1/2,1/2) cells: x -> R x + (c - R c), with CL-1's site gauges V
  and the phase exp(-i K'.t_R). A cell-centre version is run as a control.
- The composite light label is the fold of FREEZE's tau3 = +1, Pi+ label (rank 16).

##### A. Escape 1 moves the Schur wall (exact)

- A0. The folded walk and the label are covariant under the 12 rotations (residual 1e-14).
- A1. Commutant dimensions of the stabilizer on the light space, with the single-cell value equal to 1 for
  comparison:

  | point | stabilizer | commutant |
  |---|---|---|
  | Gamma_D | 2T | 24 |
  | X_D | D2 | 64 |
  | M_D | D2 | 64 |
  | R_D | 2T | 24 |

  Every value is greater than 1, so every stabilizer acts reducibly. Both rotation centres give the same numbers.
  - General reason: Q8's only spinorial irrep is the 2-dimensional one. Any light space of dimension 2m is m copies
    of it, and the light block at a D2 point is 1_2 (x) (m x m). For m >= 2, levels can split pairwise. The
    single-cell obstruction was m = 1.
- A2. The zone centre is where all of FREEZE's light nodes fold. The quasienergy-0 light space is Gamma plus the
  X-triplet, 8 dimensions. Its 2T commutant has dimension 6 = 4 + 1 + 1:
  - the X-triplet is three distinct 2-dimensional irreps (commutant 3);
  - exactly one of them is isomorphic to Gamma's irrep (intertwiner dimension 1).
  The same holds at pi for R plus the M-triplet.
  - Consequence (Schur): a T-covariant light-light term at the zone centre is block-diagonal by irrep. It can pair
    Gamma's Weyl (chirality -1) only with one X combination, which destroys the protected Weyl. The other two X
    irreps (+1 each) have no light partner at all. They can only be shifted, which by the earlier note's A2
    trichotomy leaves a node, a light Fermi surface, or a zero.
  - This is the multiplicity form of the old wall. Reducibility is necessary but not sufficient.

##### B. What actually blocks: the light Floquet winding

These are exact statements, derived here, valid for any cell size and any walk-invariant light/rest splitting P.

- B-i (additivity). If [U, P] = 0, then U = (PUP + 1 - P)(P^perp U P^perp + P), a commuting product. W3 is additive
  under pointwise products, so W3(U) = W3(light) + W3(rest).
- B-ii (gap kills winding). If PUP has no eigenvalue exp(i e) anywhere on the torus, a branch cut at e gives a
  smooth Hermitian H with PUP = P exp(-iH) P. Then exp(-i t H) is a homotopy from the sector to 1, so the sector
  has W3 = 0.
  - Contrapositive: a sector with W3 != 0 is gapless at EVERY quasienergy at the free level.
- B-iii (node formula). Put the branch cut at 0, or at pi. The obstruction to a global log then localizes on the
  nodes at that quasienergy, which gives W3 = -n_0 = -n_pi in the runner's chirality convention.
  - The general node formula is derived as a localization argument; the runner checks it numerically.
  - Numerically: W3(light) = -2.0000 and W3(mirror) = +2.0000 on a 28^3 grid. The light block is never singular
    (smallest singular value 0.35). This matches the corner bookkeeping n_0 = n_pi = +2 (light) and -2 (mirror).
  - The total is 0, as a cube-local circuit requires.
- Consequences:
  - (a) Any light-light term (one that keeps the label invariant) conserves W3(light) = -2. The light sector
    therefore always keeps net chirality +2 at 0 and +2 at pi.
  - (b) The target light content is the Gamma Weyl at 0 and the R Weyl at pi, each -1, and nothing else. It has
    W3(light) = +1.
    - Light with only the Gamma Weyl (R absent) is impossible, because n_0 = n_pi is required.
  - (c) So any relabelling (on any doubled or larger cell) that reaches the target must move 3 units of winding.
    The complement then has W3 = -1. By B-ii it is gapless at every quasienergy and cannot be gapped by
    complement-only terms at the free level.
  - (d) Interacting level: a U(1) Floquet sector with nonzero W3 carries a quantized Floquet chiral-magnetic
    response. This is LITERATURE (Higashikawa-Nakagawa-Ueda 2019), cited and not used in a proof. It suggests
    that mirror-only SMG is anomalous. Not proven here.

##### Answers

1. Is the doubled-zone corner stabilizer action reducible? YES at every corner (commutants 24, 64, 64, 24 against
   1 before). Exact.
2. Is there a covariant cube-local light-light term that gaps the partners and keeps only Gamma and R? NO, at the
   free level.
   - With the folded composite label, Schur leaves two X irreps (and two M irreps) without a light partner. The
     only pairing channel consumes the Gamma (respectively R) Weyl.
   - With any label, light-light terms conserve W3(light) = -2, which is incompatible with the target's +1.
3. Bookkeeping: light net chirality is +2 at 0 and +2 at pi (W3 = -2). Mirror is the opposite. The target needs
   W3(light) = +1.
   - Escape 1 cannot evade Nielsen-Ninomiya through a stand-alone light Floquet winding with a gappable mirror.
   - It can do so only if the mirror carries the opposite winding (W3 = -1), and that mirror is then gapless at
     every quasienergy.
4. Gate: below.

Verdict: NO-GO for escape 1 as a partner-gapping route (exact, bounded to free, walk-invariant sectors under T
and translation at any zoom).
- The Schur wall does move, but the real obstruction is the conserved light winding, and no zoom changes it.
- Walls move. What escapes this note:
  - (i) accept a nonzero-W3 mirror, and test whether a Floquet-anomalous mirror (gapless at all quasienergies)
    is physically acceptable, for example as a hidden sector;
  - (ii) labels that are not walk-invariant sectors, for example interaction-defined composites, where W3 is not
    defined;
  - (iii) the Golterman-Shamir zero route from the earlier note.

---

### #10049: overlap of the cube walk's Euclidean kernel: exact Ginsparg-Wilson chirality without doublers, chiral projector not a walk sector

**Statement (the note's own `claim_scope`, verbatim).**

> Free and fixed-U(1)-background lattice Dirac operators built from the Euclidean (space x tick) form of the Wilson-type copy-mass cube walk, X = D_W - m0 on Z^4. Exact: for any g5-hermitian kernel, V = g5 sign(g5 X) is unitary and D = 1 + V obeys the Ginsparg-Wilson relation g5 D + D g5 = D g5 D; conversely GW plus g5-hermiticity forces V unitary. The 3+1 tick unitary U(K) itself is not such a V (g5 commutes with its hop). Finite diagnostics: on the 12^4 zone D vanishes only at k = 0 for 0 < m0 < 2 (one Dirac field; 15 doubler corners at |D| = 2; also with tick weight 0.5, m0 = 0.6); the count is 1, 5, 11, 15 for m0 = 1, 3, 5, 7; position-space decay rate 0.72 per taxicab step (free), 0.91 in a Q = 1 2D background; the Chebyshev form X P_n(X^+X) has strict range 2n+1 and error falling at rate >= ln rho = 0.29 per step; the Shamir domain-wall 5D operator (strictly nearest-neighbour) gives (1 + g5 tanh(Ls artanh H_T))/2 to 1e-15 with GW defect falling from 1e-2 (Ls = 4) to 3e-9 (Ls = 16). In U(1) backgrounds (2D 10^2, 4D 4^4) GW holds to 1e-14, zero modes are exactly chiral, |index| = |Q|; Luscher's P_hat = (1 - g5_hat)/2 has rank 100 at Q = 0 and 101 at Q = 1; the 2D 3-4-5-0 indices are -e and the anomaly sums to zero. Exact arithmetic: the 16 has sum Y = sum Y^3 = SU(3)^2 Y = SU(2)^2 Y = 0. Not covered: a chiral walk (tick) realisation, reflection positivity of the chiral theory, non-abelian chiral existence (open in the literature), the composite-cell turn charges inside the overlap, interacting dynamics.

**Kind of statement.** Exact algebra plus finite diagnostics (12^4 zone; 2D 10^2 and 4D 4^4 U(1) backgrounds), dependent on the supplied Euclidean (space x tick) form of the Wilson-type copy-mass cube walk. Chiral content is a Euclidean, history-level construction (range of P_hat), not a walk sector; abelian only; non-abelian chiral existence and reflection positivity are listed as open.

**Dependencies.** Uses #10042 (W3 obstruction), #10030 (corner stabilizer) and #10041 (FREEZE) for the tick-level wall that this note leaves unchanged; does not touch the chiral-gauging conclusions of #9971, #9985 and #10025. Cites Neuberger, Luscher 1998 and 1999, Kaplan 1992, Hernandez-Jansen-Luscher, Hasenfratz-Laliena-Niedermayer. Main-branch notes on the ABJ residual and on the lattice WZ/Fujikawa treatment are outside this theme.

**Corrections and narrowings that apply to this statement.** The abelian existence statement is the supplied Luscher 1999 theorem applied to the 16's charge sums (sum Y = sum Y^3 = 0); the measured locality test of the 16's four-field coefficient on this kernel is not met at L <= 24 and is not shown to be non-local (#10085). Status wording differs between notes: #10049 treats the overlap rule as a candidate for a decision, while #10051 and #10052 call it adopted. Here it is a supplied construction and nothing is adopted. See the section "Corrected or replaced claims".

**Runner.** [`the_overlap_of_the_cube_walk_euclidean_kernel_gives_exact_ginsparg_wilson_chirality_without_doublers_but_its_chiral_projector_is_not_a_walk_sector_2026_10_23.py`](../scripts/the_overlap_of_the_cube_walk_euclidean_kernel_gives_exact_ginsparg_wilson_chirality_without_doublers_but_its_chiral_projector_is_not_a_walk_sector_2026_10_23.py); cached output [`the_overlap_of_the_cube_walk_euclidean_kernel_gives_exact_ginsparg_wilson_chirality_without_doublers_but_its_chiral_projector_is_not_a_walk_sector_2026_10_23.txt`](../logs/runner-cache/the_overlap_of_the_cube_walk_euclidean_kernel_gives_exact_ginsparg_wilson_chirality_without_doublers_but_its_chiral_projector_is_not_a_walk_sector_2026_10_23.txt); source note at head `267389da31` of branch `claude/toe-overlap-from-walk-20261021`: `docs/THE_OVERLAP_OF_THE_CUBE_WALK_EUCLIDEAN_KERNEL_GIVES_EXACT_GINSPARG_WILSON_CHIRALITY_WITHOUT_DOUBLERS_BUT_ITS_CHIRAL_PROJECTOR_IS_NOT_A_WALK_SECTOR_BOUNDED_THEOREM_NOTE_2026-10-23.md`.

**Note text, verbatim** (title line dropped; sections omitted (gate, smuggling-review, repo-check and mapping sections, which describe the review procedure and not the result): Repo check; Anti-smuggling gate (candidate rule: "matter histories are weighted by the overlap of the cube walk's Euclidean kernel; chiral fields are the range of P_hat")). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem (exact algebra plus labelled finite diagnostics; literature results cited as supplied).
Runner: runner.py, TOTAL: PASS=19 FAIL=0, 2.2 s, 225 MB peak, 3.0 k characters of stdout; run through
scripts/runner_cache.execute_runner under a unique filename (status ok, exit 0). Axioms unchanged.

##### Question

Does the campaign's walk supply an overlap (Ginsparg-Wilson) Dirac operator with exact lattice chirality and
no doublers, is it local in the owner's sense (influence passed site to site), and does it get past the
FREEZE obstructions (corner Q8 Schur no-go; light Floquet winding W3(light) = -2)?

##### Which form, and why

4D Euclidean on space x tick. The GW relation, the index and the anomaly are properties of the Euclidean
fermion action over histories, and the tick is a lattice direction like space. The walk enters through its
Euclidean kernel: the Wilson form D_W - m0, whose copy mass is the walk's Wilson-type copy mass. This
identification (and isotropy between tick and space) is SUPPLIED; A2 shows the result survives tick weight 0.5.

##### A. Construction and zone count

- A1 (exact). For any g5-hermitian kernel X, V = g5 sign(g5 X) = X (X^+X)^(-1/2) is unitary with
  g5 V g5 = V^+, and D = 1 + V obeys GW exactly. Conversely GW for D = 1 + V means V g5 V = g5, which together
  with g5-hermiticity says V is unitary. So "an overlap operator" is the same thing as "a g5-hermitian unitary".
- A0 (exact). The 3+1 Wilson-Dirac tick U = exp(-i eps H) is not such a V: g5 commutes with the hop
  alpha.sin K, so g5 H g5 != -H (residual 0.99 at eps = pi/4). V must come from the Euclidean history kernel.
- A2-A5 (finite diagnostics, 12^4 zone). For 0 < m0 < 2, D vanishes only at k = 0; the 15 doubler corners
  have D = 2 (lifted to the cutoff); GW holds to 9e-16 at all momenta; near k = 0, D = i kslash/m0 + O(k^2).
  The light-corner count is the number of corners with 2n < m0: 1, 5, 11, 15 for m0 = 1, 3, 5, 7. So one
  light species needs the copy-mass window 0 < m0 < 2 (with tick weight c_t: 0 < m0 < 2 c_t).

##### B, C. Locality and the site-to-site reading

- B1. The free kernel decays as exp(-0.72 d) in taxicab distance d (12^4 and 10^4 agree to 0.01).
- C1 (exact structure, numerical rate). X^+X has taxicab range 2. A degree-n Chebyshev polynomial
  V_n = X P_n(X^+X) is therefore a sum of products of at most n neighbourhood steps, range 2n+1, and its error
  falls as rho^(-n), rho = (sqrt b + sqrt a)/(sqrt b - sqrt a) from the spectral range [a,b] of X^+X (measured
  rate 0.32 >= ln rho = 0.29). Hence |D(x)| <= C rho^(-d/2) (C2: bound 0.14 <= measured 0.72). This is the
  Hernandez-Jansen-Luscher locality mechanism (supplied for gauge fields; here checked free and in a background).
- C3 (exact match). The Shamir domain-wall operator (Kaplan 1992) is strictly nearest-neighbour in five
  dimensions. With the Pauli-Villars ratio, the boundary operator equals (1 + g5 tanh(Ls artanh H_T))/2,
  H_T = g5 D_W (2 + D_W)^(-1), to 6e-16. Its GW defect falls 1.2e-2, 7.8e-5, 3.0e-9 at Ls = 4, 8, 16: the
  overlap (Shamir kernel) is the Ls -> infinity limit.
- Reading for the owner's wording. Both realisations pass influence site to site: the polynomial form is n
  neighbourhood steps with weight falling geometrically in n, and the domain-wall form is a strict
  neighbour rule in a fifth direction whose bulk modes are gapped. The 4D tail comes from integrating out that
  gapped bulk, as a Yukawa tail comes from a massive field. No instantaneous long-range coupling enters.
  Whether the fifth direction is the zoom-rung ladder of #9971 is open; #9971 finds that bounded speed makes
  the coarse rungs a charged tower, which is a separate cost.

##### D. Exact chirality, index, Luscher projector, anomaly sums

- D1, D6. U(1) backgrounds with uniform flux: 2D 10^2 with Q = 1, and 4D 4^4 with fluxes (1,1) in the (12)
  and (34) planes, Q = 1. GW holds in the background to 5e-15 and 2e-14. Each has one zero mode with g5 = -1
  exactly, so |index| = |Q| (Hasenfratz-Laliena-Niedermayer 1998 index theorem, supplied and observed).
- D2 (exact integers). Luscher's g5_hat = g5(1 - D) squares to 1, and P_hat_L = (1 - g5_hat)/2 has rank 100
  at Q = 0 but 101 at Q = 1 (Tr g5_hat = 2 x index). The chiral split depends on the gauge field and changes
  rank between topological sectors.
- D3. Exponential locality persists in the Q = 1 background (rate 0.91).
- D4 (doubler control). With m0 = 3 in 2D, the two one-pi corners come back light with opposite chirality and
  the index becomes -1 + 2 = +1, so the doublers are exactly what the index counts.
- D5 (2D chiral U(1), 3-4-5-0). The measured indices for U^e are -e for e = 3, 4, 5. The left-minus-right
  sum of e x index is 0, and the anomaly density sum_f s_f e_f tr g5 D_f(x,x) sums to 0 to 2e-13. Pointwise it
  leaves a zero-sum remainder of 1e-3, which is the divergence term in Luscher's cohomology result (supplied).
- D7 (exact fractions). The 16 of one family, taken as left-handed Weyl fields, has sum Y = 0 and sum Y^3 = 0
  (Luscher 1999's abelian condition for an exactly gauge-invariant chiral measure on the lattice), and its
  SU(3)^2 Y and SU(2)^2 Y sums are also 0. So U(1)_Y is anomaly-free for the 16, and an abelian Luscher theory
  exists for it. Non-abelian nonperturbative existence is NOT claimed; it is open in the literature.
- D8 (arithmetic flag). FREEZE's light content per node is L with q = 2 and R with q = 1. As left-handed Z3
  labels that is {2, 2}, with sum q = sum q^3 = 1 mod 3 per family. This matters only if the turn were gauged;
  it is a global lattice rotation, and its 't Hooft anomaly is allowed. It cancels for N_fam = 0 mod 3. The plain
  Z^4 overlap does not carry these composite-cell turn charges (its light Weyl transforms spinorially under the
  3-fold turn), so combining the overlap with the composite cell is open.

##### Verdict

- YES, for a vector-like theory. The Euclidean form of the copy-mass cube walk gives an overlap operator with
  exact GW chirality, one light Dirac field and no doublers (for 0 < m0 < 2), and exponential locality. It is
  realised site to site, either as n neighbourhood steps or as the Ls -> infinity limit of a strictly
  nearest-neighbour fifth direction. Nielsen-Ninomiya (1981) is evaded in the standard way (Luscher 1998): the
  exact chiral symmetry is the GW-deformed one, not an on-site g5.
- CHIRAL: only as a Euclidean (history) theory. One left-handed Weyl per field with no mirror is obtained by
  restricting the field space to the range of P_hat (Luscher 1998/99), and this is consistent for anomaly-free
  U(1) content; the 16's U(1)_Y passes. This MEETS the measured comparator (one left-handed Weyl per field, no
  mirror at low energy) in the Euclidean sense for abelian gauge fields.
- It does not evade the walk obstructions; it steps outside their hypotheses. W3 and the corner Q8 theorem
  apply to walk-invariant sectors of a 3+1 tick with on-site rotation action. P_hat is not such a sector: it is
  a projector on histories, built from D (which contains the tick direction), and its rank changes with gauge
  topology (D2). A walk-invariant sector has a fixed rank. No 3+1 tick (positive transfer matrix) is known for
  the chiral overlap theory, and none is supplied here.
- Effect on the chirality wall. The wall MOVES from "no local lattice chirality" to a precise price. The light
  Weyl content is obtained if (i) the rule may be exponentially local (the owner's neighbourhood-of-influence
  reading, realised site to site) and (ii) the chiral selection may be a history-level, gauge-field-dependent
  projection rather than a sector of the tick. Item (ii) bends the update reading of the axioms (the rule is no
  longer only a tick), and that is an owner decision. The tick-level wall (W3, corner Q8) is unchanged.

##### Supplied (cited, not derived)

Neuberger 1998 (overlap operator); Luscher 1998 (exact lattice chiral symmetry from GW), Luscher 1999 (abelian
chiral gauge theories with anomaly-free charges); Kaplan 1992 (domain-wall fermions); Nielsen-Ninomiya 1981;
Hernandez-Jansen-Luscher 1999 (locality for smooth fields); Hasenfratz-Laliena-Niedermayer 1998 (index).

##### Not covered

A chiral tick or Hamiltonian realisation; reflection positivity of the chiral theory; non-abelian chiral
existence; the composite-cell turn charges inside the overlap; admissibility bounds for rough fields;
interacting dynamics; whether the zoom-rung ladder can serve as the fifth direction without #9971's tower.

---

### #10052: overlap chiral determinant in SU(3) x SU(2) x U(1) backgrounds, one generation

**Statement (the note's own `claim_scope`, verbatim).**

> The overlap D = 1 + V of the cube walk's Euclidean Wilson kernel (m0 = 1.6) with Luscher's P_hat_- = (1 + sign H)/2, in supplied SU(3) x SU(2) x U(1)_Y link backgrounds on the 3^4 torus (largest dense dimension 1944, the Q multiplet), for one generation of supplied left-handed content Q(3,2,1/6), u^c(3b,1,-2/3), d^c(3b,1,1/3), L(1,2,-1/2), e^c(1,1,1), nu^c(1,1,0). Exact to rounding: GW, g5-hermiticity and the P_hat split for an antitriplet; lattice charge conjugation (antitriplet SU(3) density = -triplet's, U(1) density equal) and hence exact site-by-site vanishing of the family's SU(3)^3 and SU(3)^2 Y densities in pure SU(3) backgrounds and of SU(2)^2 Y in pure SU(2) backgrounds. Integers: in a simply-connected Cartan SU(3) flux and in one Z6-twisted fractional flux, each with a random non-abelian SU(3) x SU(2) x U(1) perturbation, every measured index equals -sum f^2 and sum Y index = 0 for the family. Finite diagnostic: in generic backgrounds the family's covariant anomaly density falls as eps^4 (3.98, 4.07, 4.05 in U(1)_Y, SU(3), SU(2) directions), lone Q as eps^2; three contrast sets fail exactly in the directions their charge sums predict (15/15). Not covered: a non-perturbative existence proof (open), the gravitational Tr Y (no curved background), larger lattices, other Z6 bundles, the pi_4 / Witten anomaly, derivation of the content.

**Kind of statement.** Numerical diagnostic with exact lattice identities (lattice charge conjugation) and integer index sums, on the 3^4 torus only, in supplied backgrounds and for supplied one-generation content. Not a non-perturbative existence proof.

**Dependencies.** Uses #10049 and #10051 (logged; SU(2) x U(1) backgrounds). The content is taken from earlier five-mode and Spin(10) results outside this theme and is not derived here. Main-branch notes on Standard Model anomaly cancellation and colour realisation are outside this theme. Cites the all-orders perturbative construction of Luscher.

**Corrections and narrowings that apply to this statement.** The title says the one-generation anomaly cancels locally, but the exact site-by-site vanishing is only for the pure-SU(3) and pure-SU(2) densities named in the scope (lattice charge conjugation); in generic backgrounds the family's covariant anomaly density falls as eps^4 and is not zero. #10083 (logged) finds that on isotropic small tori the 16's single-mode density is Polyakov-loop dominated (a holonomy shift flips its sign on 8^4) and that m0 = 1.6 carries a slow scale; it flags #10051's 4^4 densities as unchecked and suggests a modest effect from their eps^4 scaling. #10052 uses the same kind of torus (3^4) and is not tested against this either, so the eps^4 exponents of #10051 and #10052 are unchecked against that artefact; their exact identities and integer index sums are unaffected. The note records an unexplained feature: the residual is order 4 although a d_abc-weighted order-3 charge sum (2/3) does not vanish; the cause is not proved. See the section "Corrected or replaced claims".

**Runner.** [`the_overlap_chiral_determinant_in_su3_x_su2_x_u1_backgrounds_cancels_the_one_generation_gauge_anomaly_locally_and_in_every_measured_index_including_a_z6_twisted_flux_but_anomalous_subsets_do_not_2026_10_23.py`](../scripts/the_overlap_chiral_determinant_in_su3_x_su2_x_u1_backgrounds_cancels_the_one_generation_gauge_anomaly_locally_and_in_every_measured_index_including_a_z6_twisted_flux_but_anomalous_subsets_do_not_2026_10_23.py); cached output [`the_overlap_chiral_determinant_in_su3_x_su2_x_u1_backgrounds_cancels_the_one_generation_gauge_anomaly_locally_and_in_every_measured_index_including_a_z6_twisted_flux_but_anomalous_subsets_do_not_2026_10_23.txt`](../logs/runner-cache/the_overlap_chiral_determinant_in_su3_x_su2_x_u1_backgrounds_cancels_the_one_generation_gauge_anomaly_locally_and_in_every_measured_index_including_a_z6_twisted_flux_but_anomalous_subsets_do_not_2026_10_23.txt); source note at head `d0a79c3a26` of branch `claude/toe-overlap-colour-20261021`: `docs/THE_OVERLAP_CHIRAL_DETERMINANT_IN_SU3_X_SU2_X_U1_BACKGROUNDS_CANCELS_THE_ONE_GENERATION_GAUGE_ANOMALY_LOCALLY_AND_IN_EVERY_MEASURED_INDEX_INCLUDING_A_Z6_TWISTED_FLUX_BUT_ANOMALOUS_SUBSETS_DO_NOT_BOUNDED_THEOREM_NOTE_2026-10-23.md`.

**Note text, verbatim** (title line dropped; sections omitted (gate, smuggling-review, repo-check and mapping sections, which describe the review procedure and not the result): Repo check; Anti-smuggling gate; Smuggling review). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem (exact lattice identities plus labelled finite diagnostics). Runner: runner.py,
TOTAL: PASS=10 FAIL=0, 39-46 s, peak RSS 313 MB, 3.6 k characters of stdout; tested under a unique filename
(exit 0), not yet through scripts/runner_cache. Axioms unchanged. No candidate law or axiom-level rule is
proposed or edited.

##### Question

CL-1 history-level matter weighting uses the overlap with Luscher's P_hat. The SU(2) x U(1) probe (PR #10051)
left SU(3) colour as a spectator multiplicity. With colour as a dynamical SU(3) link field, does the P_hat
determinant for one generation show the full SM anomaly cancellation (SU(3)^3, SU(3)^2 Y, SU(2)^2 Y, Y^3), and
fail for subsets that should fail?

##### Supplied

- Group SU(3) x SU(2) x U(1)_Y, one generation's content and hypercharges (from the earlier 5-mode / Spin(10)
  results; not derived here). Contrast field X(3,1,-1/3) (chosen to be a rep of the Z6 quotient).
- m0 = 1.6; seeded smooth random backgrounds (momenta in {-1,0,1}^4); lattice 3^4 only.
- The Z6 global form in A2: one twisted flux, SU(3) centre direction (1/3,1/3,-2/3), SU(2) (1/2,-1/2), U(1)
  1/6 per unit 6Y, in both the (12) and (34) planes.

##### Results (out.txt)

Exact charge coefficients (Tr Y^3, Tr_3 Y, Tr_2 Y, SU(3)^3 count, Tr Y): family 0,0,0,0,0; lone Q
1/36,1/3,1/2,2,1; no u^c 8/9,2/3,0,1,2; quarks only -3/4,0,1/2,0,0; family + X -1/9,-1/3,0,1,-1.
Note: quarks alone pass Tr Y (gravitational) and SU(3)^2 Y; they fail Tr Y^3 and SU(2)^2 Y.

A. Topology (3^4, random SU(3)xSU(2)xU(1) perturbation 0.15, H gap >= 0.50):
- A1 simply-connected SU(3) Cartan flux diag(1,-1,0): indices Q,u,d,L,e,nu,X = -4,-2,-2,0,0,0,-2, all = -sum f^2.
  sum Y index: family 0 (SU(3)^2 Y); lone Q -2/3; no u^c -4/3; quarks 0; +X 2/3 (each = charge prediction).
- A2 Z6-twisted fractional flux: indices -3,-2,-1,-1,-1,0,-1, all = -sum f^2. sum Y index: family 0 (probes
  Y^3, SU(3)^2 Y, SU(2)^2 Y together); lone Q -1/2; no u^c -4/3; quarks 1/2; +X 1/3.
- A3 abelian blocks (component index idx(f) = -f^2 measured for f = -1,0,1): colour diag(1,1,-2)-weighted
  integrated anomaly (SU(3)^3) and weak-T3-weighted (SU(2)^2 Y) are 0 for the family in A1 and A2; no u^c -2,
  +X -2/+2 (colour); quarks -1/2 (weak, A2). This step is charge algebra on measured component indices.
- A4: every 16 field (and X) has integer component fluxes in the twisted background; (3,1,0) and (1,2,0) do
  not; (3,1,2/3) does. Arithmetic, not a lattice measurement.

B. Single-factor backgrounds (3^4, eps = 0.3), exact:
- B1 pure SU(3): antitriplet tr(T g5 D(x,x)) = -triplet's and tr(g5 D) equal, to 1e-14 (lattice C). Family
  SU(3) density 1e-14 and Y-weighted density 5e-15 at every site; no u^c 2.2e-3 / 4.2e-3; +X 2.2e-3; lone Q 4.4e-3.
- B2 pure SU(2): family Y-weighted density 4e-15 (3 colours x Q + L); quarks only 1.1e-3.
- B3 pure U(1)_Y scan eps = 0.2, 0.1, 0.05: exponents family 3.95, lone Q 2.00, no u^c 1.98, quarks 1.99, +X 2.11.

C. Generic SU(3) x SU(2) x U(1) backgrounds (3^4, all three factors at strength eps = 0.2, 0.1, 0.05). Fitted
exponents of max_x |anomaly density| in U(1)_Y / SU(3) / SU(2) directions, pre-set prediction from the charge
sums (x anomalous: |s-2| < 0.3; o cancelled: s >= 2.7):
- family     o 3.98  o 4.07  o 4.05
- lone Q     x 2.00  x 1.99  x 1.97
- no u^c     x 1.96  x 2.01  o 4.05
- quarks     x 2.03  o 4.07  x 1.97
- family + X x 1.96  x 1.98  o 4.05
All 15 match. Family / lone Q at eps = 0.2: 0.19 (Y), 0.063 (SU(3)), 0.079 (SU(2)); at eps = 0.05: 1.2e-2,
3.5e-3, 4.4e-3.
Unexpected (observed, not explained here): the residual is order 4, not 3, even though a d_abc-weighted order-3
charge sum (sum_coloured Y x (+-1) x dim_w = 2/3) does not vanish for the family. A gauge-invariant order-3
covariant density (eps FFF type) evidently vanishes on this lattice/background class; the cause (hypercubic or
C x P structure) is not proved. The pre-set criterion was s >= 2.7, so this does not affect the pass.

D. GW, g5-hermiticity, P_hat projector and D P_hat_- = P_+ D for u^c in a generic SU(3) x U(1) background: 1e-14.

##### Verdict

Within these finite 3^4 backgrounds, the P_hat chiral determinant shows the full one-generation SM anomaly
structure: integrated U(1)_Y anomaly cancels exactly (integers) in a simply-connected and in a Z6-twisted
topological background; the local covariant anomaly cancels at the continuum (eps^2) order in all three gauge
directions, with an eps^4 remainder; and three subsets fail in exactly the predicted directions. This is a
finite numerical diagnostic, not a non-perturbative existence proof (open in the literature; Luscher's
non-abelian construction is all-orders perturbative).

Global form, honestly: tested is one twisted bundle of the Z6 quotient (n = 1, fractional fluxes 1/3, 1/2, 1/6
per factor, integer per component), in which all 16 fields are admissible and give integer indices; not tested
are other Z6 bundles, Z2/Z3-only quotients, or any statement that the lattice prefers the quotient. The other
sections use the simply-connected group.

---

### #10056: domain-wall tick with the layer as space: one Weyl cone per wall, mirror on the far wall

**Statement (the note's own `claim_scope`, verbatim).**

> Free-field test of three candidate tick (unitary, Hamiltonian/Floquet) forms of one-handed matter. (A) A 3+1+1 Wilson-type slab with Ls layers in an extra SPATIAL direction and the tick as time: the slab Hamiltonian H is strictly nearest-neighbour and tetrahedrally covariant; the layered circuit U = W_m W_1 W_2 W_3 W_odd W_even is unitary, range 1 in each space direction and range 2 in layers. Finite diagnostics at m = 0.6, theta = 0.2: 4D bulk gapped (0.067 at quasienergy 0, 1.66 at pi; H gap 0.60); exactly one two-component Weyl node per wall, at k = 0 and quasienergy 0, opposite chirality on the two walls, no other in-gap state on a 12^3 grid, and 4 in-gap states on the L = 6 torus; the mirror overlap falls as |1 - m|^Ls (exact zero-mode recursion; ratio 0.399 per layer, xi = 1.09 layers; exactly zero at m = 1); exp(-i H tau) is covariant and faster-than-exponentially local; no wall state at X, M, R. Exact: a circuit of gates exp(-i theta h) is homotopic to 1, so the slab's W3 = 0 for every step, mass and Ls; one wall has (n0, npi) = (-1, 0), which no walk-invariant sector of a 3D walk can have (n0 = npi = -W3, control on a degree-one family). (B) The slab's layer-sign charge is compact, quantised and on-site in 3D but not conserved; its commutator lives on the middle bond and falls as |1 - m|^Ls between wall modes; the cited 1+1D Onsager template's one-handed combination has levels |sin(k/2)|. (C) At larger steps the circuit's bulk gap closes between theta = 0.2 and 0.3; quasienergy-pi wall cones (-1, -3) appear at theta = 0.7 only with a gapless bulk. Not covered: gauging the light wall, gapping the far wall, interactions, identification with the CL-1 cube walk.

**Kind of statement.** Exact statements and finite diagnostics on a supplied free Wilson-type slab (3+1+1 dimensions, m = 0.6, theta = 0.2); free fields. The note discloses that two pre-set criteria needed revision or failed.

**Dependencies.** Tick form of the overlap construction of #10049; uses #10042 (W3 = -2 on FREEZE) and #10030; the far mirror's charge is from #9971 and the cutoff-scale photon mass from #9985; the note also names the chiral-wall route (#9896: exact mode number with the mirror reflection forbids gapping the mirror alone). A tick form for a history-level readable-Born-odds note outside this theme is needed. Literature (Kaplan, Creutz-Horvath, Rudner et al., Chatterjee-Pace-Shao, Gioia-Thorngren) is cited and not re-checked.

**Runner.** [`a_domain_wall_tick_with_the_layer_direction_as_space_puts_one_weyl_cone_on_each_wall_but_the_circuit_forces_the_mirror_onto_the_far_wall_2026_10_23.py`](../scripts/a_domain_wall_tick_with_the_layer_direction_as_space_puts_one_weyl_cone_on_each_wall_but_the_circuit_forces_the_mirror_onto_the_far_wall_2026_10_23.py); cached output [`a_domain_wall_tick_with_the_layer_direction_as_space_puts_one_weyl_cone_on_each_wall_but_the_circuit_forces_the_mirror_onto_the_far_wall_2026_10_23.txt`](../logs/runner-cache/a_domain_wall_tick_with_the_layer_direction_as_space_puts_one_weyl_cone_on_each_wall_but_the_circuit_forces_the_mirror_onto_the_far_wall_2026_10_23.txt); source note at head `7f404522a0` of branch `claude/toe-chiral-tick-form-20261021`: `docs/A_DOMAIN_WALL_TICK_WITH_THE_LAYER_DIRECTION_AS_SPACE_PUTS_ONE_WEYL_CONE_ON_EACH_WALL_BUT_THE_CIRCUIT_FORCES_THE_MIRROR_ONTO_THE_FAR_WALL_BOUNDED_THEOREM_NOTE_2026-10-23.md`.

**Note text, verbatim** (title line dropped; sections omitted (gate, smuggling-review, repo-check and mapping sections, which describe the review procedure and not the result): Gate (anti-smuggling); Smuggling review). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem (two exact statements, one exact recursion, labelled finite diagnostics; the domain-wall
construction and the Floquet/Nielsen-Ninomiya literature are supplied and cited).
Runner: runner.py, TOTAL: PASS=13 FAIL=0, 4.3 s, 76 MB peak, 4.9 k characters of stdout; run under a unique filename.
Axioms unchanged. No rule adopted.

##### Question

CL-1's history-level matter weighting (the overlap D = 1 + V with Luscher's P_hat) gives the right chiral content, but
its weight is complex, so it is an amplitude, not odds (history-actuality). CL-2 and records need a TICK form: a unitary
in the tick direction. Tick-level 3D walks are blocked by the corner-Q8 no-go (freeze-gapped-partners) and by the
conserved Floquet winding W3 = -2 of the light sector (two-cell-light-label). Which of (A) a domain wall with the extra
direction as space, (B) an exponentially local non-on-site chiral charge, (C) an anomalous Floquet bulk gives a unitary
tick of one-handed matter with the mirror removed?

Repo first. This builds on rung-dimension-chirality (PR #9971, part E: a full-density layer coordinate inside a role
block is the domain-wall slab, residual mass (mu/kap)^Ls, far mirror fully charged), gk-nogo-check (PR #9985:
far-layer smoothing gives a gauge-invariant cutoff-scale photon mass), chiral-wall (exact mode number with the mirror
reflection forbids gapping the mirror alone under the register as written), nononsite-chiral (T1: compact one-body
charges are vector-like; Chatterjee-Pace-Shao template; Gioia-Thorngren 2025 arXiv:2503.07708 as cited there), and
overlap-from-walk (PR #10049: Shamir 5D -> overlap). The commit "name the fifth direction a zero-action null
direction" (e45d53c96a) concerns a null strain direction of the Regge edge carrier in the gravity lane; it is not
a spatial layer coordinate, and nothing here ties to it.

##### Model (supplied)

Gammas G1..G3 = sx (x) s_i, G4 = sy (x) 1, G5 = sz (x) 1. Slab on Z^3 x {0..Ls-1}:
H(k) = sum_i [sin k_i G_i + cos k_i G5] + (m - 4) G5 + sum_bonds h_b, with h_b = A (x) |s+1><s| + h.c. and
A = (G5 + i G4)/2. Bulk mass M = m - 4 + sum cos k_i + cos p; window 0 < m < 2 (supplied, m = 0.6 used).
Tick: U = exp(-i th (m-4) G5) prod_i exp(-i th T_i) exp(-i th H_odd) exp(-i th H_even), T_i = sin k_i G_i + cos k_i G5,
T_i^2 = 1 and h_b^3 = h_b, so every factor is an exact range-1 gate.

##### A. Domain wall with the layer direction as space: YES for a unitary tick with one cone per wall; mirror on the far wall

Exact:
- A-T1 (zero-mode recursion). At k = 0, psi_s = (1-m)^s chi with i G5 G4 chi = -chi solves H psi = 0 on the s = 0 wall
  exactly (A chi = 0 kills the missing bond); the far end leaves amplitude |1-m|^Ls, so the mirror overlap is
  O(|1-m|^Ls). At m = 1 the wall mode is compact (one layer) and the overlap is exactly 0 (3e-17).
- A-T2 (homotopy). Every factor is exp(-i th h) with h local hermitian; th -> 0 contracts U to 1 through local
  unitaries, so the slab, viewed as a 3D walk with 4 Ls components per cell, has W3 = 0 for all th, m, Ls.
  With the sector relation n0 = npi = -W3 (K1), the slab total chirality is 0 at both quasienergies.
- A-T3 (rotations). H is covariant under the tetrahedral rotations with the spinor lift on G1..G3 (C2, C3 checked to
  1e-15).
Finite diagnostics (m = 0.6, th = 0.2, pre-set criteria in brackets):
- A1 unitarity 2e-16, no Fourier weight at |n| = 2 (cube-local), layer range <= 2 [< 1e-12, <= 2].
- A2 bulk gap 0.067 at 0 and 1.66 at pi (8^4 grid plus local minimisation); H gap 0.60 [> 0.05, > 0.5, > 0.3].
- A3 Ls = 12: one 2-dim wall space per wall at k = 0, chirality L = -1, R = +1 (walk and H agree; H |det v| = 1);
  none at the other 7 corners, none at pi [exactly this pattern].
- A4 in-gap states only within 0.8 of k = 0 on a 12^3 grid; 4 in-gap states on the L = 6 torus [0 stray, 4].
- A5 k = 0 splitting 5.4e-2, 2.2e-2, ..., 2.2e-4 for Ls = 3..9, ratio 0.400 (H), 0.399 (walk) [|ratio - 0.4| < 4e-3].
- A6 no wall state at X, M, R [none].
- A7 exp(-i H tau), tau = 1: hop weight 0.6, 0.3, 9e-2, 9e-3, 5e-4, ..., 7e-11 at r = 0..8 [monotone, < 1e-6 at 8].
Answer to "does W3 / the corner no-go apply?": not to one wall, yes to the slab. One wall has (n0, npi) = (-1, 0); a
walk-invariant sector of a 3D walk needs n0 = npi, so the wall is not such a sector (its leak is the |1-m|^Ls
overlap), and the corner premise (a walk-invariant light label at X and M) is void because the wall has no state
at X or M. But the slab as a whole is a circuit with W3 = 0, so the opposite cone is forced, and it sits on the far
wall. The light 3+1 Weyl lives on one wall; the mirror is exponentially separated, not removed.
Standard open step (unchanged): gauge only the light wall (rung-dimension-chirality B: breaks gauge equivalence or
cuts the ladder and puts a charged mirror at the cut; gk-nogo-check: smoothed far layers give a cutoff-scale photon
mass) or gap the far wall by symmetric interactions (symmetric mass generation; chiral-wall: forbidden under the
register as written by exact mode number with the mirror reflection). Not attempted here.

##### B. Exponentially local modified chiral charge in a 3D Hamiltonian: NO for one-handed matter

- B3 (theorem, rederived from the cited argument): if h(k) is analytic (exponential locality suffices) and commutes
  with a one-body, number-conserving q(k) of k-independent spectrum, the charge projectors are analytic (contour
  integral), each charge sector is a smooth bundle on T^3, and the slice Chern number is periodic in k3, so the net
  node chirality of every charge sector is 0. Non-on-site charges are covered. Escapes need non-compact charges
  (Gioia-Thorngren, as cited: single-Weyl charge non-compact) or pairing (non-number-conserving) charges.
- B1 [T]: the slab's layer-sign charge Q = sign(s - mid) is compact, quantised and on-site in 3D. [H, Q] is supported
  only on the middle bond, and its wall-mode element is 6.4e-3, 1.1e-3, 1.8e-4 at Ls = 6, 8, 10 (ratio per two layers
  0.171 -> 0.160 = 0.4^2). So the domain-wall "chiral charge" obeys B3 by not being conserved; its violation is the
  mirror leak. The pre-set criterion (both ratios within 0.01 of 0.16) failed on the first run at 0.171 because of
  finite size. It was revised to "asymptotic ratio within 0.005 and decreasing", and that change is disclosed here.
- B2 [T] recheck of the 1+1D template: the pairing axial charge has levels +-1, but (Q_V - Q_A)/2 has levels
  |sin(k/2)| in [0, 1], so there is no compact one-handed U(1) to gauge. This gives an exact chiral SYMMETRY of
  vector-like matter, not one-handed matter.

##### C. Anomalous Floquet bulk: NO in this family; W3 cannot be a resource for any circuit

- C1 [F]: the pre-set criterion (th = 0.3 gapped, no pi cones) FAILED. The circuit's bulk gap at 0 closes between
  th = 0.2 and 0.3, and the wall chirality flips to +1 there. The pattern (n0, npi) = (-1, -3), with pi cones at the
  three face corners (0,pi,pi), (pi,0,pi), (pi,pi,0), appears at th = 0.7 only with a gapless bulk (gaps 2e-12,
  5e-15). It is not a gapped anomalous phase.
- C2 [T] (= A-T2): any circuit of exponentiated local gates has slab W3 = 0, so the "obstruction as resource" reading
  needs an index-carrying, non-circuit element (for example a shift-like map along the layers). Whether such an
  element exists on an open or one-ended layer direction with a gapped bulk is OPEN. The control K1 shows what W3 != 0
  would give: n0 = npi = -W3, i.e. cones of the SAME hand at 0 and pi (no mirror but an anomalous pi partner).

##### Most promising: A, as the tick form of the existing overlap clause

The overlap is the Ls -> infinity limit of the domain wall (overlap-from-walk: Shamir 5D -> (1 + g5 tanh(Ls artanh H_T))/2).
A puts the same wall content on a Hamiltonian/Floquet tick: a positive transfer matrix in the tick direction is just
U itself, with records and CL-2 transport definable per tick. It inherits, unchanged, the open step of every
domain-wall route: the far-wall mirror.

Proposed CL wording (UNTESTED, not adopted; for the coordinator):
"Tick form of matter weighting (candidate). Each matter site carries a column of Ls layer modes (a role-block
coordinate, not a new spatial axis). The tick is the layered circuit of range-1 gates exp(-i eps h) with copy mass in
the window 0 < m < 2. Light matter is the finest-layer wall sector; its history weight at Ls -> infinity is the overlap
clause. The coarsest-layer wall carries the mirror, coupled to the light wall at O(|1-m|^Ls). Open: the far-wall rule
(gauging or symmetric gapping)."

---

### #10060: forced far-wall term: unique gapped three-site cell state, strong-coupling cell only moves the mirror

**Statement (the note's own `claim_scope`, verbatim).**

> Three parts. (1) 3-4-5-0 far-wall term (the two forced 6-fermion terms l1 = (1,-2,1,2), l2 = (2,1,-2,1), one coupling g) placed on cells: on one site it vanishes (Pauli); on a two-site cell the ground state is 8-fold at -g/2; on the three-site complete-graph cell it is unique, neutral (Q_A = Q_B = 0 from half filling, zero variance), E0 = -g, first excitation -(sqrt3/2) g, so Delta_0 = (1 - sqrt3/2) g = 0.134 g; the four-site cell is unique with Delta_0 = 0.026 g. Bond terms on overlapping bonds do not commute (norm 0.25 g^2) and the uniform open three-site chain has E0 = -0.75 g > -g (frustrated, 2-fold), so a uniform rule is not a sum of commuting cells; a non-overlapping cell tiling is needed. With a naive hop of norm 2t per bond, Yarotsky's theorem (classical in the cell eigenbasis, unique product ground state, 1D Jordan-Wigner-local) gives a persistent gap for t/g < kappa_0 Delta_0/(z ||h_b||) = kappa_0 / 44.8 (kappa_0 the theorem's constant, not computed); one cell with its own hops keeps its unique state until t/g = 0.237. This is SMG of the doubled (vector-like) chain content. In the domain-wall slab the gapped far-layer product does not gap the mirror: the far-wall branch keeps E = sin k and moves one layer in (free slab with the far layer gapped). 3-4-5-1 contrast: odd cells carry Q51 in Z + 1/2 at the particle-hole point, so the three-site cell ground state is an exact Q51 = +-1/2 doublet; the four-site cell is a Q51 = +-2 doublet (dynamical); a one-site-translation chain at half filling has Q51 filling 13/2 (LSM obstruction). The lattice sees the anomaly only mod 2 (sum q = q^T K q mod 2). (2) Bosonization: l1, l2 K-null, mutually null, neutral under (3,4,5,0) and (2,1,2,-1), primitive; free-point dimension 5 for both; in the equal-velocity Luttinger family V(x) both have dimension 5 sqrt((1-x)/(1+x)), relevant iff 21/29 < x < 1. (3) One site carrying the 16 (one orbital, 2^16 states): exactly two Spin(10) singlets, |0> and |F>; the Casimir is (3/4) N (16 - N); the 10 channel psi^T C Gamma^a psi vanishes identically and the 120 channel is N(N-1)/2; so no Spin(10)-invariant, particle-hole-symmetric site term of degree below 16 has a unique ground state. Under SU(3) x SU(2) x U(1)_Y x U(1)_B-L the one-orbital 16 has singlets 1, 6, 8, 6, 1 at N = 0, 4, 8, 12, 16, and its six singlet 4-fermion terms (equal real couplings) give a unique particle-hole-symmetric singlet ground state with gap 0.442 g. 15 modes (no nu^c): every level of a particle-hole-symmetric site is doubly degenerate (exact). 8 modes (Q + L, or (4,2)): singlets only at N = 0, 8. Not covered: gauge fields, the continuum limit, a cell lattice beyond one cell, the two-orbital Spin(10) cell (register value cited, not recomputed).

**Kind of statement.** Exact site statements and finite diagnostics on supplied models: the forced six-fermion terms on cells, the free slab with the far layer gapped, and the one-orbital 16 with spin dropped. The persistent-gap theorem (Yarotsky) is cited with its constant not computed.

**Dependencies.** The forced terms l1, l2 and the wall-mode chain come from #10058 (logged). Uses #9985 for the Grabowska-Kaplan check. The two-orbital Spin(10) atom value is cited from the register and not recomputed (see #10061, logged). The note adopts no rule.

**Runner.** [`the_forced_far_wall_term_has_a_unique_gapped_three_site_cell_state_but_a_strong_coupling_cell_only_moves_the_mirror_and_the_one_orbital_sixteen_site_has_only_two_spin10_singlets_2026_10_23.py`](../scripts/the_forced_far_wall_term_has_a_unique_gapped_three_site_cell_state_but_a_strong_coupling_cell_only_moves_the_mirror_and_the_one_orbital_sixteen_site_has_only_two_spin10_singlets_2026_10_23.py); cached output [`the_forced_far_wall_term_has_a_unique_gapped_three_site_cell_state_but_a_strong_coupling_cell_only_moves_the_mirror_and_the_one_orbital_sixteen_site_has_only_two_spin10_singlets_2026_10_23.txt`](../logs/runner-cache/the_forced_far_wall_term_has_a_unique_gapped_three_site_cell_state_but_a_strong_coupling_cell_only_moves_the_mirror_and_the_one_orbital_sixteen_site_has_only_two_spin10_singlets_2026_10_23.txt); source note at head `09a3f0258d` of branch `claude/toe-smg-strong-coupling-20261021`: `docs/THE_FORCED_FAR_WALL_TERM_HAS_A_UNIQUE_GAPPED_THREE_SITE_CELL_STATE_BUT_A_STRONG_COUPLING_CELL_ONLY_MOVES_THE_MIRROR_AND_THE_ONE_ORBITAL_SIXTEEN_SITE_HAS_ONLY_TWO_SPIN10_SINGLETS_BOUNDED_THEOREM_NOTE_2026-10-23.md`.

**Note text, verbatim** (title line dropped; sections omitted (gate, smuggling-review, repo-check and mapping sections, which describe the review procedure and not the result): Mapping to the rules (no rule adopted); Smuggling review). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem (exact statements; finite diagnostics labelled [F]; the stability theorems and the
Haldane criterion are supplied, not rederived). Runner: runner.py, TOTAL: PASS=21 FAIL=0, 2.5 s, 241 MB peak, 4.7 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120;
run under a unique filename (scratch/smg_strong_coupling_test_run.py).
Axioms unchanged. No rule adopted.

##### Question

far-wall-smg found that the two forced 6-fermion terms gap the 3-4-5-0 mirror in a wall-mode chain at L = 12, but no
size trend could be extracted. The owner asked for a cheaper route: a strong-coupling derivation, a bosonization check, and the
same site test for the 16 in 3+1D.
- (1) Is there a smallest cell on which the forced term has a unique symmetric gapped ground state, and does a
  stability theorem then give a size-independent gap?
- (2) Do the forced vectors pass Haldane's criterion, and when are they relevant?
- (3) Does one site carrying the 16 admit a local symmetric interaction with a unique symmetric ground state?

Repo first. This builds on:
- far-wall-smg (the forced terms, the Chern pump, the regulator-blind 3451 result);
- block-quartic-smg (Spin(10) on the one-orbital 16 admits no singlet charge-4 term, two orbitals admit one; the block
  mirror term releases light partners);
- the register's candidate unification law (one 32-mode cell under the Spin(10) pair square has a unique singlet
  ground state, gap 19.1 g, with survival under inter-cell hopping "estimated only");
- gk-nogo-check (Golterman-Shamir obstruction for mirror schemes);
- smg-literature.
New here:
- the cell search;
- the commuting/frustration analysis;
- the stability-theorem application and its failure mode in the slab (mirror relocation);
- the LSM mod-2 reading of the 3451 contrast;
- the bosonization threshold;
- the exact one-orbital Spin(10) singlet theorem;
- the SM-group site result.

##### Pass criteria (written before the runner's first run; scratch exploration in scratch/ preceded them, so the A, B
##### and D values were seen in scratch and the thresholds are diagnostics, not blind tests)

A1 one site: the forced-term operator on one site has norm 0.
A2 two-site cell: ground state degeneracy > 1.
A3 three-site complete-graph cell (pairs 01, 02, 12): unique ground state, |E0 + 1| < 1e-9, |E1 + sqrt3/2| < 1e-9;
   <Q_A>, <Q_A^2>, <Q_B>, <Q_B^2> all < 1e-9 (charges measured from half filling).
A4 four-site complete-graph cell: unique ground state with gap > 1e-2.
A5 overlapping bond terms: ||[h01, h12]|| > 0.1; open three-site chain E0 > -1 + 0.1 and ground state degenerate.
A6 naive hop norm per bond = 2 (to 1e-9); one cell with its two intra-cell hops keeps a unique ground state with gap
   >= Delta_0/2 for t/g <= 0.1, and the first crossing t_c/g lies in (0.1, 0.5).
A7 free slab Ls = 12, far layer gapped by m sz with m = 20: the far-wall branch at k = pi/8 has |E - sin k| < 1e-6,
   weight on the far layer < 0.01 and on the next layer > 0.9.
B1 arithmetic: Q51 per site at half filling = 13/2 (non-integer); Q_A, Q_B per site = 6, 2; sum q = q^T K q mod 2.
B2 3451 three-site cell: lowest energies in Q51 = +1/2 and -1/2 equal (to 1e-9) and lower than all other sectors.
B3 3451 two- and four-site cells: ground state degenerate (two-site: > 2 states; four-site: Q51 = +-2 doublet, the
   Q51 = 0 sector strictly higher).
C1 l1, l2: K-null, mutually null, neutral under both charges, gcd of 2x2 minors 1.
C2 free-point dimension 1/2 |l|^2 = 5 for both.
C3 sympy: V(x) eta V(x) = eta, Delta(x) = 5 sqrt((1-x)/(1+x)) for both, threshold Delta = 2 at x = 21/29; numerical
   O(2,2) diagonalisation at x = 0.3, 0.8 agrees to 1e-9.
D1 16 of Spin(10) from five oscillators: 45 Hermitian generators, Casimir 45/4 on the 16 (to 1e-12).
D2 Weyl-character count of Spin(10) singlets in Lambda^n(16): exactly [1 at n = 0, 1 at n = 16, 0 else].
D3 on random Fock vectors, || C2 v - (3/4) N (16 - N) v || < 1e-9.
D4 multiplicity of the 10 in Lambda^2(16) = 0, in Sym^2(16) = 1; Lambda^2(16) = 120 irreducible (multiplicity 1, dim 120).
D5 H = N(16 - N) - (Psi16 + h.c.) with Psi16 the product of all 16 annihilators: unique ground state at -1, gap 2,
   ground state (|0> + |F>)/sqrt2 up to sign.
D6 15 modes: the particle-hole operator prod_i (c_i + c_i^+) anticommutes with fermion parity (exact), so every level of a
   particle-hole-symmetric, parity-conserving site is at least 2-fold.
D7 Q + L (8 modes) under SU(3) x SU(2) x U(1)_Y x U(1)_B-L and (4,2) under SU(4) x SU(2): singlets only at n = 0, 8.
D8 16 under SU(3) x SU(2) x U(1)_Y x U(1)_B-L: singlet counts [1,6,8,6,1] at n = 0,4,8,12,16 (0 elsewhere); six
   singlet charge-4 terms; with equal real couplings H = -g sum_i (O_i + O_i^+) has a unique ground state, gap > 0.05 g,
   and the ground state is killed by all simple raising and lowering operators (< 1e-8) with weight zero.
   (Prediction written before the runner; the equal-coupling value was seen in scratch.)

##### A. Strong coupling for the forced 3450 term (part 1)

- A1 [T]. Both forced terms need two modes of one flavour (|l_f| = 2), so on one site they vanish: H_site = 0, and all
  16 states are degenerate.
- A2 [F]. Two-site cell: the terms connect only pairs of configurations, so the ground state is 8-fold at -g/2.
- A3 [F]. Three-site complete-graph cell (all three pairs; the pair terms are symmetric under exchange of the two sites
  because each term holds two pair factors, so the cell is S3-symmetric and no ordering is chosen):
  - the ground state is unique, E0 = -g, and the first excited level is -(sqrt3/2) g (4-fold), so Delta_0 = (1 - sqrt3/2) g = 0.134 g;
  - Q_A = Q_B = 0 from half filling, with zero variance;
  - a unique ground state carries a one-dimensional representation of every symmetry of the cell, so it is symmetric
    automatically.
  This is the smallest such cell.
- A4 [F]. The four-site cell is also unique, but with Delta_0 = 0.026 g.
- A5 [T]/[F]. The bond terms on (01) and (12) do not commute (||[h01, h12]|| = 0.25 g^2). The open three-site chain has
  E0 = -0.75 g, above 2 e_bond = -g, and is 2-fold.
  - So the uniform rule (one coupling on every bond) is NOT a sum of commuting or frustration-free blocks, and
    Bravyi-Hastings-Michalakis does not apply to it.
  - The block form the rule would need is a non-overlapping tiling by complete-graph cells of three sites, with the
    hops (and any inter-cell term) treated as the perturbation. That tiling breaks one-site translation to three-site
    translation: a lopsided choice that needs a reason (three equivalent tilings).
- A6 [F] Stability. Write H = g sum_cells h_c + t sum_bonds h_b, with naive hop h_b = sum_f s_f (i/2)(c^+_x c_x+1 - h.c.),
  where ||h_b|| = 2.
  - In each cell's eigenbasis, g sum h_c is classical with a unique product ground state and local gap Delta_0.
  - The hops are nearest-neighbour and bounded, and in 1D every hop is local after Jordan-Wigner.
  - So the hypotheses of Yarotsky 2006 hold: the ground state stays unique with gap >= Delta_0 - O(t) for
    t z ||h_b|| / Delta_0 < kappa_0, where z = 3 bonds touch each cell and kappa_0 is the theorem's constant (not
    computed). That is, t/g < kappa_0 / 44.8.
  - Kennedy-Tasaki 1992 is the cluster-expansion precedent; for fermions in d > 1 the analogue is De Roeck-Salmhofer
    2019 (CMP 365, 773; not on the supplied list).
  - Finite check: one cell with its own two hops stays unique until t_c/g = 0.237, which bounds the true constant from
    above at this cell.
  What this proves is SMG of the chain's full content, in which the naive hop gives each flavour both chiralities
  (3450 plus its mirror at k = pi): a vector-like statement.
- A7 [F] Relocation. In the domain-wall slab, the far layer in a unique cell product is gapped and decoupled, and the
  rest is a free Chern-1 slab per flavour. Its open face is now the next layer, so the mirror branch reappears there.
  - Free check: with the far layer gapped by m sz (m = 20), the far-wall branch keeps E = sin k exactly. Its weight on
    the far layer is 0.0025 and on the next layer 0.99.
  - Induced corrections are a bilinear self-energy O(T^2/g), which cannot gap a one-handed branch, and multi-fermion
    terms of order T^6/g^5 with free-point dimension 5 (part 2), which are irrelevant.
  So the g -> infinity limit of a far-layer term does NOT gap the mirror. The stability theorem's hypotheses fail for the
  coupled slab, because its unperturbed part (the free slab with the moved edge) is gapless.
  This is a route no-go for "strong coupling on the far layer" in this form. Escapes:
  - an intermediate-coupling phase (Zeng et al.'s regime), which no product-state theorem reaches;
  - a term acting on enough layers that the mirror modes themselves are cell-local, which turns it into the vector-like
    case, where the light copy must be protected by something the term does not see (momentum- or taste-selective
    forms: ax7, momentum-selective-mirror).

##### B. 3451 contrast (part 1)

- B1 [T].
  - At the particle-hole point, Q51 per site is 13/2. A one-site-translation chain therefore has fractional Q51 filling,
    and LSM (Oshikawa form) forbids a unique gapped symmetric ground state.
  - For 3450, Q_A and Q_B per site are 6 and 2 (integers): no obstruction.
  - Since q^2 = q mod 2, sum q = q^T K q mod 2. The lattice remnant of the anomaly is its parity only: 3451 has q^T K q = -1 (odd).
- B2 [T]+[F]. On odd cells, Q51 lies in Z + 1/2, so particle-hole pairs Q51 with -Q51. The three-site cell ground state
  is an exact doublet at Q51 = +-1/2.
- B3 [F] (recorded result). The two-site cell is many-fold. The four-site cell is a Q51 = +-2 doublet with the Q51 = 0
  sector higher. Even cells carry no kinematic obstruction, so this doublet is dynamical.
  So no cell up to four sites has a unique state for 3451, and only the odd-cell part is a theorem. The anomaly enters
  the cell test only mod 2.

##### C. Bosonization (part 2)

K = diag(1,1,-1,-1) (flavours 3, 4 one way, 5, 0 the other), t = (3,4,5,0), and the second charge (2,1,2,-1).
- C1 [T]. l1, l2 are K-null and mutually null, neutral under both charges, and primitive (the 2x2 minors have gcd 1).
  Haldane's criterion (supplied) then says cos(l1.phi) + cos(l2.phi) can gap all four modes. Primitivity gives a
  unique pinned minimum, so no discrete symmetry breaks.
- C2 [T]. At the free point, Delta(l) = 1/2 |l|^2 = 5 for both (> 2): both are irrelevant.
- C3 [T]. Write l = (a; b) with b = O a, where O = [[-3/5, -4/5], [4/5, -3/5]] is a rotation (possible because the
  Gram matrices of the a's and b's agree: both are null and mutually null).
  - The equal-velocity family V(x) = (1 - x^2)^(-1/2) [[1, x O^T], [x O, 1]] obeys V eta V = eta and
    Delta = 1/2 l^T V^-1 l = 5 sqrt((1-x)/(1+x)) for both.
  - Both are relevant iff 21/29 < x < 1: a strong forward-scattering helper, 0.72 of the velocity.
  - Unequal velocities and the general 10-parameter V are not scanned.
- Consistency with (1). Both routes say the forced terms gap only far from the free point: either at a large helper,
  or at g comparable to the bandwidth (far-wall-smg's level crossing near g ~ 40 in wall-mode units, and the cell regime
  g >> t here). Bosonization does not see A7's relocation, because it treats the mirror's own low-energy fields. The
  cell argument does not reach the bosonization regime.

##### D. The 16 on one site (part 3)

Modes: the 16 of Spin(10) as the even Fock space of five oscillators, one complex mode per weight (one orbital). The
Lorentz spin index is dropped.
- D1 [T]. There are 45 generators, with Casimir 45/4 on the 16.
- D2 [T] (Weyl character formula, |W(D5)| = 1920). Lambda^*(16) holds exactly two Spin(10) singlets: |0> (n = 0) and
  |F> (n = 16).
- D3 [T]. C2 = (3/4) N (16 - N) on the whole Fock space. Reason: Lambda^2(16) = 120 is irreducible, so the only
  invariant 2-in-2-out operator is sum_{i<j} n_i n_j, and C2 is fixed by n = 1 and n = 16.
  - Every number-conserving 4-fermion invariant is a function of N.
  - The 120-channel Phi^+ Phi is N(N-1)/2, a pure Hubbard term.
- D4 [T]. The 10 lies in Sym^2(16), not Lambda^2(16), so psi^T C Gamma^a psi = 0 identically on one orbital. The suggested
  H = g sum_a |psi C Gamma^a psi|^2 is zero.
- D5 [T]. A unique ground state of a Spin(10)-invariant site lies in span{|0>, |F>} (there is no nontrivial 1D
  representation).
  - Particle-hole symmetry C (with the outer automorphism) swaps |0> and |F>, and only the 16-fermion term mixes them.
  - So a C-symmetric Spin(10)-invariant site term of degree < 16 never has a unique ground state, and the fewest-change
    unique site term is Psi16 + h.c. (gap 2w with N(16-N) supplied).
  - Without C, the empty site (chemical potential, a bilinear) is trivially unique: no SMG content.
  - Two orbitals change this: the register's 32-mode pair square is unique, gap 19.1 g (cited, not recomputed).
- D6 [T]. 15 modes: prod_i (c_i + c_i^+) is fermion-odd, so a C-symmetric parity-conserving site has every level at least
  2-fold for ANY interaction. Exact failure.
- D7 [T]. 8 modes (Q + L under the SM group, or (4,2) under SU(4) x SU(2)): singlets only at n = 0, 8. So no term of
  degree < 8 is unique. This is the same pattern as the Spin(10) 16: at fixed symmetry the site test does not separate
  8 from 16.
- D8 [F]. Under SU(3) x SU(2) x U(1)_Y x U(1)_B-L, the one-orbital 16 has singlets 1, 6, 8, 6, 1 at n = 0, 4, 8, 12, 16.
  - Its six singlet charge-4 terms are the B-L-conserving four-fermion types: QQQL-type, u d d nu, u u d e,
    Q L d nu, Q L u e and Q Q u d contractions.
  - With equal real couplings they give a unique, C-symmetric, singlet ground state with gap 0.442 g.
  - Three seeded random coupling vectors (scratch) also gave unique states, with gaps 0.003, 0.65 and 0.30 g.
  - Spin(10) kills all six (D2), so this needs the Spin(10)-breaking pattern and six supplied couplings.

Answer to (3): for the Spin(10) one-orbital 16, NO at fewest change. Only the degree-16 cat term gives a unique
symmetric site state. The SM-group one-orbital 16 gives YES at degree 4. The 15 fails exactly (parity). The 8 fails
below degree 8. A unique symmetric site state with a gap would, by the fermionic stability theorem, give a gapped
symmetric product phase of a lattice of such sites in any dimension. But the site test sees only the 0+1D anomaly
(mode-count parity under C, and the degree thresholds), not Z16: 8 and 16 behave alike, and an on-site symmetry lattice
carries no 4D 't Hooft anomaly. And in a domain-wall geometry, A7's relocation applies unchanged. So this is NOT "the
Z16 statement made local". It is the vector-like (Butt-Catterall-Hasenfratz-type) strong-coupling statement, and a
necessary site condition for a strong-coupling route.

##### Answers

1. Strong coupling (3450): the smallest unique, symmetric, gapped cell is the three-site complete-graph cell,
   Delta_0 = (1 - sqrt3/2) g. The uniform rule is frustrated and non-commuting, so a cell tiling is required. Yarotsky
   gives a persistent gap for t/g < kappa_0/44.8 (ingredients: Delta_0 = 0.134 g, ||h_b|| = 2, z = 3), but for the
   vector-like content only. In the slab the mirror relocates (A7), so the far-wall strong-coupling route is a route
   no-go in this form. 3451: odd cells are exact doublets (LSM, mod 2), and the four-site cell is a dynamical doublet.
2. Bosonization: Haldane's criterion is met (null, mutually null, neutral, primitive). Delta = 5 at the free point.
   Both become relevant in the equal-velocity Luttinger family for x > 21/29.
3. The 16 site: Spin(10) one orbital: two singlets only. The 10 channel is identically zero and the 120 channel is
   Hubbard, so there is no unique state below degree 16. SM group: unique at degree 4 (gap 0.442 g). 15: exact
   doublets. 8: no unique state below degree 8. Not Z16.

---

### #10064: circuit slab puts its mirror in the other copy only through a nonzero turn-graded winding

**Statement (the note's own `claim_scope`, verbatim).**

> Free-field Floquet (circuit) slabs on CL-1's 2x2x2 cell with the site-gauged (111) turn T3 as a symmetry on the turn axis K = kappa (1,1,1). (T1) Sum rule: in each turn sector the eigenphase flow through every quasi-energy equals the winding W_a of det U_a(kappa), so F_0 = F_pi = W in Z[Z3] (augmentation 0). Every circuit of cube-local gates that each commute with T3 (and every exp(-i t H) with H turn-symmetric) has W = 0, so q_mirror = q_light holds in each gap separately. (T2) FREEZE (twist-local-single) has W = (-2, 1, 1); hence FREEZE is not a product of T3-commuting cube-local gates at any depth. (T3) A light q 2 Weyl at 0 with the q 1 mirror only at pi is impossible; light q 2 and mirror q 1 at 0 force flow (-2, 1, 1) at pi, i.e. at least two more Weyls at pi per family. (F) A coupled-layer circuit slab (layers alternating FREEZE and its inverse, turn-commuting tau3-label gates q 1 on even bonds and q 2 on odd bonds, g = 0.5) has its bulk gapped at 0 and pi (0.50 on a 12^4 grid). For odd Ls the near wall holds the light q 2 (hand +1) at (K = 0, 0) and (R, pi), and the far wall holds the mirror q 1 (hand -1) at both. For even Ls the far wall holds q 2. With the anomaly-family-count index and Omega twist, the odd slab allows N_f = 3, 6, 9. Not covered: interactions, gauge fields, the Omega gapping itself, a rule fixing the termination.

**Kind of statement.** Exact sum-rule results for free Floquet slabs with the (111) turn as a symmetry; the circuit slab is a finite diagnostic on a supplied construction (FREEZE layers and label gates). The termination is not forced.

**Dependencies.** Uses FREEZE (#10041). Re-derives the static-slab theorem of #10063 (logged) as the W = 0 case of its sum rule; takes the single-pair flow form f(q, h) from #10063 D2, which is not in #10063's scope, and checks it on its own slab walls. Uses the label-selective charge-4 result of #10031 (logged) for a tension it records, and the domain-wall tick of #10056. The family-count index form (N_f = 0 mod 3) and the Omega twist are supplied from notes outside this theme.

**Corrections and narrowings that apply to this statement.** Upgrades #10041's finite search (depths 5, 7, 9) to an exact statement for gates commuting with the (111) turn. The sentence of #10063 that the mod 3 is not recovered on any realised slab applies to static slabs without extra axis crossings; the Floquet slab here has a mirror in the other copy for odd Ls with a nonzero winding. See the section "Corrected or replaced claims".

**Runner.** [`a_circuit_slab_puts_its_mirror_in_the_other_copy_only_through_a_nonzero_turn_graded_winding_which_forces_equal_flow_at_quasi_energy_pi_and_is_set_by_termination_2026_10_23.py`](../scripts/a_circuit_slab_puts_its_mirror_in_the_other_copy_only_through_a_nonzero_turn_graded_winding_which_forces_equal_flow_at_quasi_energy_pi_and_is_set_by_termination_2026_10_23.py); cached output [`a_circuit_slab_puts_its_mirror_in_the_other_copy_only_through_a_nonzero_turn_graded_winding_which_forces_equal_flow_at_quasi_energy_pi_and_is_set_by_termination_2026_10_23.txt`](../logs/runner-cache/a_circuit_slab_puts_its_mirror_in_the_other_copy_only_through_a_nonzero_turn_graded_winding_which_forces_equal_flow_at_quasi_energy_pi_and_is_set_by_termination_2026_10_23.txt); source note at head `7759b4264b` of branch `claude/toe-floquet-pi-slab-20261021`: `docs/A_CIRCUIT_SLAB_PUTS_ITS_MIRROR_IN_THE_OTHER_COPY_ONLY_THROUGH_A_NONZERO_TURN_GRADED_WINDING_WHICH_FORCES_EQUAL_FLOW_AT_QUASI_ENERGY_PI_AND_IS_SET_BY_TERMINATION_BOUNDED_THEOREM_NOTE_2026-10-23.md`.

**Note text, verbatim** (title line dropped; sections omitted (gate, smuggling-review, repo-check and mapping sections, which describe the review procedure and not the result): Gate (anti-smuggling); Smuggling review). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem. Exact statements are labelled [T], finite diagnostics [F] and readings [S].
Runner: runner.py, TOTAL: PASS=12 FAIL=0, 7.7 s, 62 MB peak, 4.8 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120.
It was tested under a unique filename (scratch/floquet_pi_slab_test_run.py). Axioms unchanged. No rule adopted.

##### Question

copy-flip-slab proved that on any STATIC turn-symmetric slab whose only turn-axis crossings are the wall Weyls,
q_mirror = q_light, so the cube-turn anomaly gives no family-count constraint. It named the escape as a Floquet circuit with
a second gap at quasi-energy pi, as FREEZE has. This note builds the slab as a circuit: layers form the role-block
coordinate, and each tick is FREEZE's cube-local gate sequence per layer plus layer gates. Wall modes are allowed at 0 and
at pi. Questions:
- Can the near wall hold the light (q 2) at 0 and the far wall the mirror in the other copy (q 1), at 0 or at pi, with the
  bulk gapped at both?
- (1) What is the modified sum rule?
- (2) Does FREEZE's structure realise it without fitting?
- (3) Does the anomaly-family-count bookkeeping with Omega then give N_f = 0 mod 3?
- (4) Does the light keep one shared turn charge?

Repo first. A git grep of origin/main (docs, scripts) for "anomalous floquet", "turn-graded winding", "sector winding"
and "coupled-layer" found nothing. This note builds on and narrows:
- copy-flip-slab (D3 and its Floquet reading D4);
- twist-local-single (FREEZE; its A3 finite search);
- anomaly-family-count (the index and the Omega twist selection);
- freeze-mirror-smg (charge-4 terms on FREEZE's label);
- chiral-tick-form (W3 = 0 for exp(-i theta h) circuits).

##### Pass criteria

The criteria were written before any code ran (criteria_pre_run.txt). Afterwards, four short scratch scripts outside D
checked the FREEZE winding, the bulk gap against g, and the open slab.

PASS needed all five:
- P1: a bulk-gapped circuit slab with near light q 2 and far mirror q 1;
- P2: the sum rule;
- P3: the far copy forced by a rule;
- P4: allowed N_f = {3, 6, 9};
- P5: one shared light charge, with no light content beyond FREEZE's own pinned pi node.

Predicted: FAIL at P3 only. Every line matched its prediction.

##### A. FREEZE on its turn axis

- A1 [T]/[F]. The turn T3 (CL-1's site-gauged C3, T3^3 = 1) is a symmetry of U_F on the axis and keeps Pi+, tau3 and chi.
  - At K = 0, the tau3 = +1 pair (q 1, turn sectors {1, w^2}) and the tau3 = -1 pair (q 2, sectors {1, w}) sit at
    quasi-energy 0.
  - At R they sit at pi.
- A2 [T]/[F]. FREEZE's turn-graded winding is W_F = (-2, 1, 1) over sectors (1, w, w^2). Here W_a is the winding of
  det U_a(kappa) around the axis loop.
  - The axis flow through 0 (at K = 0) and through pi (at R) both equal W_F.
  - There is no other axis crossing.

##### B. Sum rule (answer to 1)

- B0 [T]. For a unitary family in one sector, the net number of eigenphases crossing any fixed eps upward equals the
  winding of the determinant. Hence F_0 = F_pi = W, with sum_a W_a = 0, because each gate's total det has zero winding.
  - Static Hamiltonian: W = 0 and there is no pi gap, so F_0 = 0. This is copy-flip-slab D3.
- B1 [T]. Lemma. A cube-local gate that commutes with T3 keeps every turn sector, and its sector det is constant in kappa.
  - On the even tiling the gate is C.
  - On the odd tiling it is D(K) C D(K)^+, and D(kappa) = diag(e^(-i kappa (a1+a2+a3))) commutes with T3 on the axis.
  - So any circuit of such gates has W = 0. So does exp(-i t H) with H turn-symmetric.
  - Checked: a depth-7 random covariant circuit has W = (0, 0, 0).
  - In such circuits each gap balances on its own, and q_mirror = q_light holds at 0 and at pi separately.
- B2 [T]. Corollary. W_F != 0, so FREEZE is not a product of cube-local gates that each commute with the (111) turn, at any
  depth. This upgrades twist-local-single A3 (a finite search at depths 5, 7 and 9 over all 12 rotations) to an exact
  statement, under a weaker covariance (one turn).
- B3 [T]. The single-pair flow is f(q, h) = h (e_(q+2) - e_(q+1)), as in copy-flip-slab D2.
  - (i) A light q 2 at 0 with the q 1 mirror only at pi is impossible: F_0 = (-1, 1, 0) differs from F_pi = (-1, 0, 1),
    whatever W is.
  - (ii) A light q 2 and a mirror q 1 both at 0 give F_0 = W = (-2, 1, 1). The pi gap must carry the same flow, and that is
    no single-pair flow, so there are at least two more Weyls at pi per family. This is a forced pi doubling.
  - Modified sum rule: sum over 0-crossings of f(q, h) = sum over pi-crossings of f(q, h) = W.
  - q_mirror != q_light is allowed exactly when W != 0. That needs gates that are not individually turn-commuting, and the
    pi content then copies the 0 content's flow.

##### C. The circuit slab (answer to 2)

Construction:
- Layers alternate F = U_F and F^+.
- Layer gates exp(-i g P (x) X_bond) use the turn-commuting label projectors P_q1 = Pi+ (1 + tau3)/2 and
  P_q2 = Pi+ (1 - tau3)/2.
- The tick is G_odd(q 2) G_even(q 1) (sum_l F_l), with g = 0.5.

Results:
- C1 [F]. The period-2 bulk is gapped at both 0 and pi. The gap is 0.50 at each on a 12^4 grid that contains K = 0 and R.
  - The min gap on 6^4 is 0.20, 0.43, 0.03 and 0.17 at g = 0.2, 0.8, 1.2 and 1.4: a window g < ~1.2, not a tuned value.
- C2 [T]/[F]. The alternation is forced by the bulk gap.
  - An all-F stack has W = Ls W_F, which is (-12, 6, 6) at Ls = 6.
  - Its bulk carries 2 W_F per two layers at every k_l, so an eigenphase passes through 0 and pi for every k_l: gapless.
  - The bulk period must have zero net W.
- C3 [T]/[F]. Odd Ls (7 and 13):
  - The near wall holds the light q 2 (hand +1) at (K = 0, 0) and at (R, pi).
  - The far wall holds the mirror q 1 (hand -1, the other copy) at both.
  - F_0 = F_pi = W = W_F, and the near-wall flow is f(2, +) = (-1, 1, 0).
  - The node states are exact single-layer eigenvectors, because the labels are exact at the nodes.
- C4 [T]/[F]. Even Ls (6 and 12), same bulk: the far wall holds q 2 (hand -1), so q_mirror = q_light, with
  W = F_0 = F_pi = 0.
- C5 [F]. With both labels on the even bonds and the same odd Ls, the whole FREEZE pair sits on the far wall, again with
  W = W_F.
- C6 [F]. The open Ls = 7 slab has no other state at 0 or pi off the nodes (gap 0.52 on a 6^3 wall grid).

Answer (2): yes, it is realised, with no measured number and g in a window. But two things are choices:
- the far copy is fixed by termination (the net number of F minus F^+ layers, i.e. Ls parity);
- the near/far split is fixed by the label bond pattern.

The bulk does not force either. P3 FAILS.

##### D. Bookkeeping (answers to 3 and 4)

- D1 [T]. The anomaly-family-count index is applied with the Omega twist k = -q_mirror, using the far-wall
  Z3-Spin(10)^2, Z3-gravity and Z3^3 coefficients.
  - Odd slab (lights {2 at 0, 2 at pi}, mirrors {1, 1}): allowed N_f = {3, 6, 9}.
  - The pi doubling keeps the mod 3, because the node count 2 is prime to 3.
  - The reflected slab (light 1, mirror 2) gives the same set.
  - Even slab: every N_f.
  - The smallest nonzero count is 3, but nothing in the rules prefers 3 over 6. Minimality is still supplied.
- D2 [T]. All light Weyls (both nodes, every stacked family) carry one turn charge, q 2.
  - The turn-CP lemma (J = 0 for turn-invariant masses on a turn-charged triplet) therefore does not force J = 0.
  - J != 0 is allowed, not supplied.
- D3 [S]. A tension with freeze-mirror-smg. On FREEZE's bare label doublet, a T-invariant charge-4 mirror term first exists
  at N_f = 4 (C(N_f, 4) such terms). The Omega in D1 is anomaly-family-count's per-family pairing inside a 16. At N_f = 3 the
  mirror gap therefore needs the 16's internal structure. It is not computed here.

##### Answer

1. Sum rule: F_0 = F_pi = W, where W is the turn-graded det winding.
   - q_mirror != q_light is allowed exactly when W != 0.
   - W != 0 is impossible for circuits of turn-commuting gates (B1). FREEZE has W = (-2, 1, 1), which proves that its
     layering cannot be turn-covariant.
   - The mirror cannot sit at pi alone. If it sits at 0 in the other copy, the pi gap must repeat the flow (at least two
     more Weyls per family).
2. FREEZE's structure realises the copy-flipped slab: alternate FREEZE and inverse layers, with label dimer gates. The bulk
   is gapped at 0 and pi. The near wall holds q 2 at 0 and pi, and the far wall holds q 1 at 0 and pi.
   - It is NOT forced: Ls parity and the bond pattern choose the far copy, and even Ls gives q_mirror = q_light.
3. On the odd slab the bookkeeping gives N_f = 0 mod 3 (3, 6, 9). Minimality is still supplied, and the gapping at N_f = 3
   needs the 16 pairing (D3).
4. Yes. One shared light charge, q 2, so J != 0 is allowed.

Synthesis: FAIL at P3 only, as predicted. P1, P2, P4 and P5 pass.

---

### #10072: free pi sector of FREEZE: the doubler map cancels all vacuum polarization

**Statement (the note's own `claim_scope`, verbatim).**

> Free bands of FREEZE (the family-class tick representative, W_F = (-2,1,1)) on CL-1's 2x2x2 cell, with CL-1's plain tick (eps 0.3) as control, and cell-charge potentials as gauge probes. Exact: (1) the doubler S (S U(K) S^-1 = -U(K+R)) maps each no-Fermi-surface half-filled vacuum to its complement, S rho(K) S^+ = 1 - rho(K+R); (2) hence, for every S-even one-body probe (any cell-charge potential, any strength, any number of ticks, any uniform vector potential), the vacuum's induced charge equals the infinite-temperature value, zero: no vacuum polarization; (3) zero-quasi-energy, zero-momentum states made of a 0-sector pair and a pi-sector pair exist at every momentum scale; (4) F_pi = W in every turn sector, robust under turn-symmetric deformations, so no free term gaps pi; (5) the one-cube start is degenerate and every no-Fermi-surface filling has at least one inverted boundary; (6) with the pi copy (2 x 16 per family) every gauge anomaly stays zero and the turn-anomaly N_f set is unchanged. Estimates with supplied numbers: Lamb shift (Uehling) and Z invisible width exclude the free pi sector. Not covered: interacting gapping of the pi sector, link-gauged FREEZE beyond cell-charge potentials, other members of the family class, decay rates.

**Kind of statement.** Exact statements for free bands of FREEZE with cell-charge potentials as gauge probes (link-gauged FREEZE is not defined), plus estimates against measurement with supplied numbers (Uehling term, Z width, N_nu). The note's word 'adopted' for the family-class tick is not carried (the section "Corrected or replaced claims" section 5). Its conclusion is that the free FREEZE bands are excluded as they stand and need repair, with its repair routes (a) and (b) untested.

**Dependencies.** Doubler map S and the alternation are first stated in #10070 (logged); S is rebuilt and checked in this note's own runner (S U(K) S^-1 = -U(K + R)). The F_pi = W sum rule is that of #10064. The Uehling formula, Lamb-shift agreement scale and N_nu are supplied literature numbers. Relied on by #10073, whose repair question and bulk conclusion rest on it.

**Runner.** [`the_family_class_ticks_forced_pi_sector_is_a_light_charged_inverted_copy_whose_doubler_map_cancels_all_vacuum_polarization_so_it_needs_repair_while_its_anomalies_stay_safe_2026_10_24.py`](../scripts/the_family_class_ticks_forced_pi_sector_is_a_light_charged_inverted_copy_whose_doubler_map_cancels_all_vacuum_polarization_so_it_needs_repair_while_its_anomalies_stay_safe_2026_10_24.py); cached output [`the_family_class_ticks_forced_pi_sector_is_a_light_charged_inverted_copy_whose_doubler_map_cancels_all_vacuum_polarization_so_it_needs_repair_while_its_anomalies_stay_safe_2026_10_24.txt`](../logs/runner-cache/the_family_class_ticks_forced_pi_sector_is_a_light_charged_inverted_copy_whose_doubler_map_cancels_all_vacuum_polarization_so_it_needs_repair_while_its_anomalies_stay_safe_2026_10_24.txt); source note at head `9a67d5379a` of branch `claude/toe-pi-sector-stability-20261021`: `docs/THE_FAMILY_CLASS_TICKS_FORCED_PI_SECTOR_IS_A_LIGHT_CHARGED_INVERTED_COPY_WHOSE_DOUBLER_MAP_CANCELS_ALL_VACUUM_POLARIZATION_SO_IT_NEEDS_REPAIR_WHILE_ITS_ANOMALIES_STAY_SAFE_BOUNDED_THEOREM_NOTE_2026-10-24.md`.

**Note text, verbatim** (title line dropped; sections omitted (gate, smuggling-review, repo-check and mapping sections, which describe the review procedure and not the result): Gate; Smuggling review). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers, [S] reading.
Runner: runner.py, TOTAL: PASS=11 FAIL=0, 1.7 s, 115 MB peak, 5.3 k characters, seeded, AUDIT_TIMEOUT_SEC = 120. It was
tested under a unique filename (scratch/pss_test_run.py). Axioms unchanged. No rule proposed or adopted. Criteria were
written before any code ran (criteria_pre_run.txt). Every criterion came out as predicted. One code-level control
failed on the first run and was replaced; no claim changed. The light-only filling (2 of 8) was meant as a
non-complementary control, but it gave zero response. That is correct: V and S both preserve the light block, so the
theorem applies block by block. It was replaced by the both-nodes-normal filling, which is S-invariant and does respond.

Question (urgent check on the adopted Family-class tick clause): mirror-in-time C4 read the forced pi sector as charged
and inverted, with possible vacuum instability. Is the pi sector a physical problem?

Repo first. A git grep of origin/main (docs, scripts) for "temporal doubler", "inverted sector", "quasi-energy pi" and
"Uehling" found nothing relevant. This note builds on and narrows:
- mirror-in-time (S, C1 alternation, C3 equal anomalies, C4 reading);
- floquet-pi-slab (F_0 = F_pi = W);
- t-breaking-tick-lowenergy (the kept group);
- the register's "cone partners at pi (charged, inverted inertia)" exclusion and the CL-2 text.

##### A. What the vacuum sees (Q1)

- A1 [T]/[F]. S sends the no-Fermi-surface half filling (light eigenphases in (-pi, 0), plus one frozen eigenspace) to
  its complement: S rho(K) S^+ = 1 - rho(K + R). The residual is 6e-15.
- A2 [T]/[F]. The theorem.
  - In real space S is a staggered cell sign times an on-cell unitary. It commutes with any cell-charge potential V and
    with a uniform vector potential (the twisted grid).
  - So S U_V S^-1 = -U_V for U_V = e^{-i lam V} U. Then tr(rho(t) O) = tr((1 - rho)(t) O) for every S-even O, so
    <O> = tr(O)/2. This is the infinite-temperature value.
  - Checked on 4^3 cells (512 modes) with lam = 0.5, a random V and 24 ticks: the induced cell charge of BOTH vacua is
    at most 6e-14.
  - The FREEZE vacuum has ZERO vacuum polarization at every q and every order in the probe.
- A3 [F]. Controls.
  - CL-1's vacuum (gap at pi) screens (|dN| up to 3.3).
  - An S-odd on-cell layer makes FREEZE respond (0.32).
  - The both-nodes-normal FREEZE filling responds (1.2). It is S-invariant, and it pays for that with an inverted Fermi
    surface at theta = pi/2.
- A4 [S]. The physical reading. The pi copy is a full second copy of every light Weyl: same hand, same charges, same
  dispersion. Pi-pi bilinears are slow and carry zero net momentum, so they couple to the low-energy photon and Z
  exactly as 0-sector bilinears do. Because the copy is inverted, it anti-screens exactly as much as the 0 copy screens.

##### B. Stability

- B1 [T]/[F]. The pi-sector dispersion equals the 0-sector dispersion (pi - theta(R + k) = theta(k), residual 2e-15).
  - States with exactly zero total quasi-energy and zero momentum (a 0 pair at +E and a pi pair at -E) exist at momentum
    scales 1e-1, 1e-2 and 1e-3.
  - So the vacuum -> pair + pair channel is open in the IR at every scale. It is not only a Planck-scale effect.
- B2 [T]/[F]. Control: CL-1's plain tick has w_max = 0.6, so any zero-quasi-energy vacuum transition needs at least
  6 particle-hole pairs, all at cell scale (prethermal). FREEZE needs 2.

##### C. Filling (Q2)

- C1 [T]/[F]. In every turn sector, the axis flow through pi equals the winding, (-2, 1, 1). This stays exact under
  random turn-symmetric deformations. So no free term opens a pi gap in any family-class tick (all components of W are
  nonzero).
- C2 [T]. The one-cube start is degenerate.
  - A single FREEZE cell puts its 4 light modes exactly at 0 (periodic) or exactly at pi (antiperiodic), and its frozen
    4 modes at +-pi/2.
  - So no quasi-energy ordering picks a filling, and no CL-2 clause does either.
- C3 [T]. Alternation (exhaustive over 4096 fillings on the axis loop). Rises equal drops, and there is at least one.
  Every no-Fermi-surface filling has at least one inverted light sector; the minimum is one.
- C4 [S]. What CL-2 does.
  - CL-2 defines no ground state. The actual configuration follows the odds, and a free Slater state of Floquet
    eigenvectors is stationary, so the transport stays.
  - The filling is the one the start and the splits carry.
  - CL-2 cannot choose a normal-normal vacuum, because none without a Fermi surface exists.
- The convention-independent statements are these: F_0 = F_pi = W; the complement map S; vacuum response = the
  infinite-temperature value; and the count of at least one inverted boundary. The branch-cut choice only decides WHICH
  sector is inverted.

##### D. Anomaly (Q3)

- D1 [T]. With the pi copy each family has 2 x 16 (counting the pi copy of the light near wall and of the far-wall
  mirror separately).
  - Y^3, Y-grav, SU2^2 Y, SU3^2 Y and SU3^3 are all 0. The doublet count is even, and the Weyl count is 0 mod 16.
  - The turn coefficients double. 2 is a unit mod 3 and mod 9, so the allowed N_f set is unchanged (N_f = 0 mod 3
    stays).
  - Anomaly: SAFE.
- D2 [S]. The far-wall gapping must also gap the mirror's pi copy, which is light, charged and S-related. An S-even
  far-wall term would do so at the same coupling. Not computed.

##### E. Against measurement

- E1 [E]. With S intact, the electron loop cancels against its inverted pi copy, so the hydrogen 2S Uehling term
  vanishes. Its size is -27.13 MHz, while theory and the measured Lamb shift agree at about 0.01 MHz (supplied).
  EXCLUDED by a factor of about 2700.
- E2 [E]. Z invisible width. Inverted pi neutrinos give N_nu -> 0, and normal-filled copies would give 6. The measured
  2.984 +- 0.008 excludes both (373 and 377 sigma).
- E3 [S]. Exothermic pi-pair production in every process, with phase space up to the cell scale. The free sector is
  excluded before any rate is computed.

##### Verdict: NEEDS REPAIR (not FATAL; anomaly SAFE)

The adopted family-class tick, taken with FREEZE's free bands, is excluded as it stands. Its forced pi sector is light,
charged and inverted, and the exact doubler S makes its gauge response cancel the light sector's. That contradicts the
Lamb shift and the Z width, and the vacuum is unstable in the IR.

It is not shown FATAL, because two repair routes remain open.
- (a) A family-class tick (W unchanged) that breaks S and leaves no light node at pi. F_pi = W forbids a free gap, but
  it does not forbid the band passing pi with constant occupation away from nodes. Whether any member of the class does
  this is untested, and so is C3's count outside FREEZE.
- (b) An interaction that gaps the pi copies (near wall and far wall) but not the 0 copies. It must be S-odd or act
  through the filling's own S-breaking. This is the same class of open problem as far-wall symmetric mass generation.

Required of any repair, testable with this runner's A2 probe: the vacuum must screen like CL-1's.

---

### #10073: family-class winding forces bulk pi states; a slab can put the pi flow on the far wall

**Statement (the note's own `claim_scope`, verbatim).**

> Free-field Floquet ticks with the (111) turn T3 as a symmetry on the turn axis; FREEZE (W_F = (-2, 1, 1)) rebuilt inline. (A1) In each turn sector the net eigenphase flow through every quasi-energy equals the det winding W_a, so W_a != 0 puts a BULK Bloch eigenstate at every quasi-energy (pi included) on the axis loop; checked for FREEZE and turn-symmetric deformations. (A2) Every interval filling has flow W at both cuts; intersection lemma: a band filling with no occupied-empty touching on the axis forces W = 0. (A3) An anomalous Floquet (RLBL) tick has gapped bulk at 0 and pi and zero det winding on every loop, walls F_0 = F_pi = +-1. (A4) On a slab, per wall F_0 - F_pi = C (band invariant of the bulk bands between 0 and pi); total pi flow = W_slab is forced but its wall is not: a sector-resolved class-A toy with a static-type domain-wall bulk (C = f(2,+), W = 0) and a W-carrying far termination layer has near wall (f(2,+), 0) and far wall (f(1,-), W_F). (B1) U0 O U0^-1 = (-1)^(n_pi) O, so any periodic drive resolves only the parity of the number of pi legs; tick-alternating terms cancel exactly on 0-0 and pi-pi terms. (B2) Separating pi-pi from 0-0 needs an S-odd term, which gives the light sector the reflected interaction; reduced two-flavour Spin(6) site: unique ground state for one sign, 2-fold for the reflected sign. (C) N_f = 0 mod 3 unchanged under the supplied anomaly-family-count index form. Not covered: the repaired slab built on FREEZE's 8-mode cell, the far-wall SMG of mirror + pi pair, interacting wall dynamics, gauge fields, the low-energy recheck of a W = 0 bulk.

**Kind of statement.** Exact flow statements for free Floquet ticks; slab placement is exhibited in a supplied sector-resolved class-A toy; the Spin(6) reduction is a supplied model. The slab reading is untested and not adopted.

**Dependencies.** Uses #10064 (sum rule) and #10072 (pi-sector exclusion; S is rebuilt and checked in #10072's runner, and was first stated in #10070, logged). Part B2 takes S from those notes; this note's runner does not build it. The Spin(6) reduction follows #10061 (logged) with a different normalisation; the one-16 site follows #10060. #10065 (logged) is used for the origin of the winding and for the T lemma behind the rechecks in its section C. The RLBL anomalous-Floquet model and the QWZ strip are supplied.

**Corrections and narrowings that apply to this statement.** #10074 (logged) narrows the slab reading: the termination is a chosen boundary bit, the near wall is pi-free and screening in the toy, and the far wall must gap all three families together, with that gapping not shown. The family-class tick is worded 'adopted' in #10072 and 'suspended' in #10073; nothing is adopted here. See the section "Corrected or replaced claims".

**Runner.** [`the_family_class_winding_forces_bulk_pi_states_but_a_slab_can_put_all_its_pi_flow_on_the_far_wall_while_no_tick_alternating_term_separates_pi_pi_from_zero_zero_2026_10_24.py`](../scripts/the_family_class_winding_forces_bulk_pi_states_but_a_slab_can_put_all_its_pi_flow_on_the_far_wall_while_no_tick_alternating_term_separates_pi_pi_from_zero_zero_2026_10_24.py); cached output [`the_family_class_winding_forces_bulk_pi_states_but_a_slab_can_put_all_its_pi_flow_on_the_far_wall_while_no_tick_alternating_term_separates_pi_pi_from_zero_zero_2026_10_24.txt`](../logs/runner-cache/the_family_class_winding_forces_bulk_pi_states_but_a_slab_can_put_all_its_pi_flow_on_the_far_wall_while_no_tick_alternating_term_separates_pi_pi_from_zero_zero_2026_10_24.txt); source note at head `498059c295` of branch `claude/toe-pi-repair-20261021`: `docs/THE_FAMILY_CLASS_WINDING_FORCES_BULK_PI_STATES_BUT_A_SLAB_CAN_PUT_ALL_ITS_PI_FLOW_ON_THE_FAR_WALL_WHILE_NO_TICK_ALTERNATING_TERM_SEPARATES_PI_PI_FROM_ZERO_ZERO_BOUNDED_THEOREM_NOTE_2026-10-24.md`.

**Note text, verbatim** (title line dropped; sections omitted (gate, smuggling-review, repo-check and mapping sections, which describe the review procedure and not the result): Gate (for the candidate termination clause, not adopted); Smuggling review). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [S] reading.
Runner: runner.py, TOTAL: PASS=7 FAIL=0, 2.7 s, 81 MB peak, about 4.0 k characters, seeded, AUDIT_TIMEOUT_SEC = 120.
It was tested under a unique filename (scratch/pi_repair_test_run.py). Axioms unchanged. No rule adopted. No CL edit.
Criteria were written before any code ran (criteria_pre_run.txt). Every criterion came out as predicted.

The first run had three code-level failures, and each was fixed without changing any claim:
- A4: the wall-flow counter missed crossings on the k-loop seam, because the crossing fell exactly on a grid point. The
  fix was a grid offset.
- A4: tau = 0.8 let the trivial-mass strip's bulk band cross pi. The fix was tau = 0.5, which gives a bandwidth below pi.
- B1: the sign convention for the alternating drive was wrong (H_eff = -O_odd for the order (+, -)).

Question (repair of the SUSPENDED family-class tick):
- (A) Is a light pi node forced by W != 0 in the bulk, or only on slab walls?
- (B) If bulk pi copies are forced, can they be gapped symmetrically, for example by a tick-alternating interaction?
- (C) Verdict.

Repo first. A git grep of origin/main (docs, scripts) for "anomalous floquet", "rudner" and "pi copy" found nothing. This
note builds on and narrows:
- pi-sector-stability: S, the zero vacuum polarization, and repair routes (a) and (b);
- floquet-pi-slab: the sum rule F_0 = F_pi = W, P3 (the termination is chosen), and the alternating F/F^+ bulk;
- tick-winding-origin: T forces a zero W component, and W is additive;
- spin10-two-flavour: the Spin(12) Casimir and the reduced Spin(6) analogue;
- smg-strong-coupling: one 16 per site has no unique low-degree singlet.

##### A. Bulk tick versus slab walls

- A1 [T]/[F]. Bulk theorem.
  - In turn sector a, U_a(kappa) is a unitary loop. The net upward crossing count of ANY fixed quasi-energy eps equals the
    winding of det U_a, which is W_a.
  - So W_a != 0 forces a bulk Bloch eigenstate at every eps, including pi, on the axis loop. This is the bulk tick's own
    spectrum, not a slab effect.
  - FREEZE: the flow is (-2, 1, 1) at eps = 0.37, 1.1, 1.77, 2.6 and pi. Two random turn-symmetric deformations give the
    same.
  - Every family-class tick has all components of W nonzero, so no family-class BULK tick is gapped at pi or anywhere else
    on the axis.
- A2 [T]. Fillings.
  - An interval filling (a, b) has flow W at both cuts. A light cut at 0 therefore always brings a second gapless cut. Its
    quasi-energy is a convention (pi in the standard vacuum), but its existence is forced.
  - Intersection lemma for band fillings with no occupied-empty touching on the axis (touchings across turn sectors are
    protected crossings, i.e. 3D nodes).
    - Occupied and empty curves are disjoint closed sets on the torus (kappa, theta). So every pair has zero algebraic
      intersection: N_o,a m_b - N_e,b n_a = 0.
    - All occupied and empty slopes are then equal. Since sum_a W_a = 0, the common slope is 0 and W = 0.
    - An exhaustive check over 676 disjoint configurations agrees.
  - Hence ANY bulk vacuum of a W != 0 tick has occupied-empty touchings beyond the single light cut. This answers (A) for a
    bulk world: forced.
- A3 [F]. Anomalous Floquet contrast.
  - The RLBL tick (4 full-transfer steps around a plaquette, plus an on-site step 0.8) has a bulk gap at 0 (0.80) and at
    pi, and det winding 0 on every loop.
  - Its strip walls carry F_0 = F_pi = (-1, +1).
  - So anomalous Floquet phases have gapped bulks only because their det windings vanish. Their invariant lives in the
    micromotion, not in W, and it cannot gap a W != 0 bulk.
  - It IS the structure of a slab whose bulk period has W = 0. That is floquet-pi-slab's F/F^+ bulk, whose net W sits in
    the unpaired layer, i.e. the termination.
- A4 [T]/[F]. Slab walls.
  - [T] For a slab bulk gapped at 0 and pi, each wall has F_0 - F_pi = C, the band invariant of the bulk bands between 0
    and pi on that side (sector resolved). The walls sum to W_slab at every eps.
  - So the total pi flow W_slab != 0 is forced (floquet-pi-slab B3), but WHICH wall carries it is set by C.
  - floquet-pi-slab's bulk has C = 0, which gives F_0 = F_pi on each wall. That is why its near wall holds the light q 2
    at both (0, 0) and (R, pi): the near-wall pi copy.
  - [F] Sector-resolved class-A toy. Per turn sector there is a QWZ strip (U = exp(-0.5 i H)) with C_a = f(2,+) =
    (-1, 1, 0). Its far termination carries a W_a chiral shift layer coupled at g = 0.3.
    - Near wall: (F_0, F_pi) = ((-1, 1, 0), (0, 0, 0)), i.e. the light q 2 at 0 only, with NO near-wall pi copy.
    - Far wall: F_0 = (-1, 0, 1) = f(1,-), the mirror q 1 in the other copy, and F_pi = W_F = (-2, 1, 1).
    - The slab's det winding is (-2, 1, 1).
  - [S] On the full cell this would be a static-type domain-wall bulk (W = 0, gap at pi, as in CL-1's tick) with one FREEZE
    layer at the far termination. At 0 the far wall then has: the static mirror q 2 (-), plus FREEZE's q 2 (+) and q 1 (-).
    The q 2 pair has zero net flow and is removable, leaving the mirror q 1. At pi it has FREEZE's (q 2, +) and (q 1, -).
    Not built on the 8-mode cell.

##### B. Gapping pi copies in a bulk world

- B1 [T]/[F]. Under the tick, a term with n_pi pi-legs obeys U0 O U0^-1 = (-1)^(n_pi) O.
  - So a drive of any period resolves only n_pi mod 2. The harmonics are multiples of 2 pi / n, and a pi-pi term carries
    total quasi-energy 0 mod 2 pi, exactly like a 0-0 term.
  - Constant terms give H_eff = O_even. Tick-alternating terms give H_eff = -O_odd. The errors are 1.5e-3 at g = 0.01.
  - Splittings: a 0-0 mass, a pi-pi mass and a 2+2 quartic each give 0.60 when constant and 0 (exact) when alternating.
    A 0-pi mixing term gives 0 when constant and 0.60 when alternating.
  - Answer: a tick-alternating interaction does NOT couple only pi-pi pairs. It cancels exactly on them, and on 0-0 terms.
    Allowed or not (it would make CL-1's tick period-2), it does not do the job.
- B2 [T]/[F]. Separating pi-pi from 0-0 needs an S-odd term (S exchanges the sectors).
  - In S-mapped frames an S-odd term gives the light sector the reflected interaction -O.
  - Reduced two-flavour Spin(6) site (2^8 states), with the term -(g/2) sum {B_a, B_a^+}:
    - the gapping sign has a unique half-filled ground state (gap 2.00 g in this runner's normalisation, which differs
      from spin10-two-flavour's);
    - the reflected sign has a 2-fold ground state.
  - So the light 16s would carry a cutoff-scale strongly coupled term. A reflected sign with a unique gapped state would
    gap the light, which is worse.
  - No S-odd route is shown benign.

##### C. Verdict

There are two readings.

Bulk-world reading (the light Weyls are FREEZE's bulk nodes): NOT REPAIRABLE by free terms (A1, A2) or by
tick-alternating interactions (B1). The S-odd route is not shown (B2).

Slab-world reading (the world is the near wall; this is the adopted clause's own setting): REPAIRABLE for the light wall at
the level of flows (A4). The rule costs are:
1. The family-class winding moves off the bulk tick into the far termination layer. The bulk tick becomes W = 0 (a
   static-type domain-wall circuit, gapped at pi). The clause would read: "the slab's far termination layer has all three
   turn-graded winding components nonzero; the bulk tick has W = 0".
   - floquet-pi-slab already found that the termination fixes the far copy (P3 FAIL). So this is no new choice in kind,
     but it is still a choice.
2. The far wall must gap, by SMG, the mirror at 0 plus the pi pair (q 2, +), (q 1, -). That is 3 x 16 = 48 Weyls per
   family (0 mod 16), with no turn-symmetric bilinear (the charge difference is 1). Not shown.
3. Rechecks are needed because the bulk is now W = 0 and T-symmetric (tick-winding-origin lemma): the 96-element kept group
   and the low-energy, CP and lapse results were derived for a FREEZE bulk.

Also: N_f = 0 mod 3 is unchanged (C1, under the supplied anomaly-family-count index form). The near wall has 1 light node
per family instead of 2, and both are units mod 3. The near wall has no pi states, so the S complement map of
pi-sector-stability has no near-wall instance. The vacuum polarization test (A2 probe of pi-sector-stability) on the
near wall is not run.

So the family-class mod-3 count is not lost. The suspension is narrowed: "family-class bulk tick" is excluded, and
"family-class far termination" is open, pending far-wall SMG and the rechecks.

---

### #10085: one-family U(1) anomaly: four-field coefficient in admissible backgrounds does not vanish like p^2

**Statement (the note's own `claim_scope`, verbatim).**

> Pre-registered rerun of the single-mode test of the one-family 16's four-field coefficient c4 in the U(1)_Y covariant anomaly density of the Wilson-kernel overlap (r = 1, m0 = 1.0), with every background inside the Hernandez-Jansen-Luscher admissibility bound ||1 - U_p|| < 1/30 (supplied): eps = 0.01, 0.02, 0.03 (max plaquette deviation 0.0300), axis-restricted factorised single-mode backgrounds, L x T x L x T with L = 12, 16, 24 and T = 24, 32, exact block sign(H). Exact: block = full 4D density, symmetry-reduced block sums = full sums, C-evenness, evr = eigh (all < 1e-12). Finite diagnostics, pre-set criteria: the joint fit R16/eps^2 = c4 + c6 eps^2 is clean (residual <= 1.1e-3 |c4|; eps exponent 3.97-4.01); the doublet's intercept is 0.989 gamma_L. NOT met: the headline (c4 vanishing like p^2 with T-agreement) and the copied P5, P5'. At L = 24, c4 = +1.13e-4, +6.7e-5, -3.60e-4 at |p_hat| = 0.26, 0.52, 0.77 (T = 32; T = 24 within 8%), so it changes sign and does not fall like p^2; the pooled intercept is +5.4e-4. Not covered: the measure, non-abelian locality, the gauge-field integral, non-axis backgrounds, L > 24, momenta below |p_hat| = 0.26.

**Kind of statement.** Numerical diagnostic with pre-registered criteria, in axis-restricted single-mode backgrounds inside the supplied Hernandez-Jansen-Luscher admissibility bound. The headline criterion is not met.

**Dependencies.** Builds on #10084 and #10083 (both logged) and the overlap construction of #10049. Hernandez-Jansen-Luscher and Luscher admissibility bound and theorems are supplied.

**Corrections and narrowings that apply to this statement.** Removes the caveats of #10084 (admissibility, T = 16 at L = 24, two-eps split); its not-met finding stands. The earlier L = 24 value 1.42e-4 (eps = 0.3/0.15 split) is about 26% above the admissible value 1.13e-4; equivalently the admissible value is about 20% below the earlier one. See the section "Corrected or replaced claims".

**Runner.** [`the_one_family_u1_anomaly_four_field_coefficient_in_admissible_backgrounds_at_wilson_mass_one_does_not_vanish_like_p_squared_2026_10_25.py`](../scripts/the_one_family_u1_anomaly_four_field_coefficient_in_admissible_backgrounds_at_wilson_mass_one_does_not_vanish_like_p_squared_2026_10_25.py); cached output [`the_one_family_u1_anomaly_four_field_coefficient_in_admissible_backgrounds_at_wilson_mass_one_does_not_vanish_like_p_squared_2026_10_25.txt`](../logs/runner-cache/the_one_family_u1_anomaly_four_field_coefficient_in_admissible_backgrounds_at_wilson_mass_one_does_not_vanish_like_p_squared_2026_10_25.txt); source note at head `b89d3a5426` of branch `claude/toe-luscher-admissible-20261021`: `docs/THE_ONE_FAMILY_U1_ANOMALY_FOUR_FIELD_COEFFICIENT_IN_ADMISSIBLE_BACKGROUNDS_AT_WILSON_MASS_ONE_DOES_NOT_VANISH_LIKE_P_SQUARED_BOUNDED_THEOREM_NOTE_2026-10-25.md`.

**Note text, verbatim** (title line dropped; sections omitted (gate, smuggling-review, repo-check and mapping sections, which describe the review procedure and not the result): Smuggling review). Headings are demoted to fifth level; the labels and check indices in it are the source's own (see the glossary above).

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [S] reading.

Runner facts:
- runner.py gives TOTAL: PASS=11 FAIL=0 in 6 s on the laptop, with 3.6 k characters of stdout.
- It is seeded, declares AUDIT_TIMEOUT_SEC = 120 and reads no data files: the Mac-mini results (243 jobs) are an embedded JSON literal.
- It was tested under a unique filename in the agent folder (exit 0).
- Each pre-set criterion prints MET or NOT MET. A PASS line certifies only that the recorded verdict reproduces from the data, so a PASS line can carry NOT MET.

Axioms unchanged; no rule proposed; no CL edit.

##### Pre-registration

- criteria_pre_run.txt was written before any computation of this probe. The only things run first were timing benchmarks on random matrices.
- It discloses that luscher-m0-1's eps = 0.3/0.15 numbers had been seen.
- Admissibility bound, as supplied: Hernandez, Jansen, Luscher, Nucl. Phys. B552 (1999) 363 prove overlap locality when every plaquette has ||1 - U_p|| < eps_adm with eps_adm < 1/30. Luscher, Nucl. Phys. B549 (1999) 295 builds the abelian anomaly-current locality on this class.
- For U(1), ||1 - U_p|| = 2|sin(F_p/2)| and max|Y| = 1, so the bound requires eps < 0.03334. The chosen values are eps = 0.01, 0.02, 0.03. G1 checks every job: the largest deviation is 0.03000 < 0.03333.
- One cost addendum (15:25, before any observable): one real L = 24 block takes 8.3 s, so all tiers were kept and no threshold changed.
- Mini run: 4 single-thread workers at nice 10, about 6.2 h wall. It ran longer than projected because another user's load on the mini reached 50-200.

##### Set-up

- The machinery is luscher-m0-1's (block construction unchanged), with three declared changes. Each is verified live (G0a, G0b).
  - (a) The background is th(x) = eps sin(p(x - 1/2)) / (2 sin(p/2)). This is luscher-m0-1's antiderivative minus the constant eps/2: the plaquettes are identical and only the holonomy constant changes. The odd profile makes the pi rotations in the (1,2) and (3,4) planes, and on the diagonal the (13)(24) swap, exact block symmetries. That gives a 4-8x reduction; reduced = full to 3e-14.
  - (b) q_Y[th] = q_1[Y th] (exact) together with C-evenness (8e-16). These build all five species from unit-charge runs at 9 amplitudes.
  - (c) The eigensolver is scipy evr (= numpy eigh to 2e-14). On the mini, the full 576-block numpy sum equals the reduced evr sum to 5e-15 on 12 x 24 x 12 x 24.
- The order-eps^2 density cancels exactly in R16 = sum m Y^3 r(|Y| eps). c4 comes from the joint fit R16/eps^2 = c4 + c6 eps^2 over the three eps (one dof).

##### Results against the pre-set criteria

| criterion | outcome | numbers |
|---|---|---|
| G0 exactness (a, b, c) | MET (PASS) | 4D 5e-15, GW 2e-15, reduced 3e-14, C 8e-16; laptop = mini 6e-11 |
| G1 admissibility < 1/30 | MET | max 0.03000 over 243 jobs |
| N joint-fit residual <= 5% abs(c4) | MET | max 1.1e-3 |
| A HEADLINE: c4 one sign, abs(p)-exponent >= 1.8 at T = 24 and 32, T-agreement 10% | NOT MET | c4 (T32) +1.127e-4, +6.72e-5, -3.599e-4; exponent 0.87 (T32), 0.95 (T24) with a sign change; T24/T32 differ 7.9%, 1.5%, 0.05% (T part met) |
| P5' L = 24 T = 32 one sign, exponent >= 1.8 | NOT MET | as above |
| P5 pooled intercept small; L16 diagonal exponent in [1.6, 2.4] | NOT MET | intercept +5.4e-4 (limits 1.3e-4, 7.5e-5); c4(16,1,1) +1.37e-4 and c4(16,2,2) -3.60e-4 have opposite signs |
| P5b eps exponent within 0.3 of 4 | MET | 3.971, 3.993, 4.003, 4.014 |
| D doublet intercept within 3% of gamma_L | MET | 0.9893 |

Reported, no criterion:
- Diagonal c4 at T = 24, in order of increasing s:

  | s | L | c4 |
  |---|---|---|
  | 0.038 | 16 | +1.37e-4 |
  | 0.067 | 12 | +5.5e-5 |
  | 0.146 | 16 | -3.60e-4 |
  | 0.25 | 12 | -8.7e-4 |
  | 0.31 | 16 | -1.07e-3 |
  | 0.5 | 12, 16 | -1.51e-3 |

- Admissible c4 against luscher-m0-1's eps = 0.3/0.15 split: (24,1) 1.13e-4 vs 1.42e-4; (16,1) 1.37e-4 vs 1.28e-4; (12,1) 5.5e-5 vs 4.8e-5; (16,2) -3.60e-4 vs -3.6e-4. The above-bound split was therefore qualitatively right; its L = 24 value carried a T = 16 / higher-order bias of about 25%.
- K3: the unit-charge 9-amplitude fit gives sum m Y^5 r4 = c4 to 1.6e-3.
- H1 [F, post-hoc]: at fixed momentum, c4 is L-converged at s = 0.146 (L16 -3.6018e-4 vs L24 -3.6012e-4). It is not converged at s = 0.067 (L12 +5.5e-5 vs L24 +6.6e-5, 20%).

##### Answer

- Inside Luscher's admissibility bound, with three eps, clean eps^4 scaling and T-convergence (T = 24 vs 32 within 8%), the 16's four-field coefficient does NOT vanish like p^2 on the three smallest L = 24 momenta.
  - It changes sign between |p_hat| = 0.52 and 0.77.
  - At |p_hat| = 0.26 it stays at +1.1e-4, about 0.9% of abs(gamma_L).
- This removes luscher-m0-1's caveats (i) admissibility, (ii) T = 16 at L = 24 and (iii) the two-eps split. Its NOT MET finding stands.
- [S] Remaining readings, from luscher-m0-1:
  - (a) A turnover below |p_hat| = 0.26. A sign change already sits near s ~ 0.1, and c4 would need a second zero or a curve to 0 below s = 0.017.
  - (b) A finite-L effect at small momentum. H1 shows a 20% L-dependence at s = 0.067 while s = 0.146 is converged, so this reading is live.
  - (c) A genuine non-local piece. Supplied perturbative locality argues against (c).
  - The next discriminating test is c4 at fixed s = 0.017 and 0.038 on L = 32 and 48, at T >= 24, inside the bound. The symmetry reduction makes L = 32 at T = 24 about 91 blocks of dim 4096 per amplitude.

---

## Corrected or replaced claims

# Corrections, withdrawals and conflicts: chirality, doublers and mirror removal

Each entry gives what was corrected or narrowed, by which PR, and the corrected form. A claim listed here as withdrawn is not a standing claim, even where it still appears in the quoted scope text of a logged PR.

## 1. #9994 is corrected by #10004 (disposition: superseded in the part below; the rest is given here)

**Withdrawn (by #10004):** the attribution of the index-eight obstruction to the symmetry Z4_J, and the sentence in #9994's scope "the quartic keeps Z4_J x Z4_N x SU(4), which forbids every bilinear mass and pair at K; the K mirror is 8 Weyl of one Z4_J charge (Z16 index 8)". #10004 finds that the two J sectors are time-reversal partners of equal chirality with J-charges +-1, so Z4_J is vector-like (index 0). The attribution of the index to Z4_J in #9994's item 5 and in its check A4 is not carried; its item 4 (exact decoupling) and the Z4_J oddness of K masses stand.

**Corrected form, as #10004 states it:** the one-taste obstruction is the Z4 of mode number (Z4_N): the chiral symmetry Z4 of mode number has index 16 = 0 with two tastes and 8 with one taste. #10004 says the conclusion of #9994 stands with that relabelling.

**#9994's statement in its corrected form (everything else is #9994's own text):** SU(4) toy of the momentum-selective mirror requirement. Band (supplied): a real band with Weyl nodes only at K = 0 and R = pi(1,1,1), of opposite chirality (Karsten-Wilczek form composed with a unimodular momentum map, realified with complex structure J); light h, mirror -h, light-mirror pairing w prod sin^2(k_i/2) (1 at R, 0 at K); cube-filtered SU(4) quartic (rows 8^-1/2 sum over the cube, form factor 8 prod cos^2(k_i/2)) on the mirror only. Exact: the toy is sign-free (weights det(M)^4, M real); the light K modes and the whole R sector never enter the interaction, so at every coupling and every finite size the light gap at K is 0 and the light-mirror gap at R is the free paired value (these are by construction, as the note says, not dynamical results); every mirror mass at K is odd under Z4_J and every pair is odd under the Z4 of mode number, so the quartic, which keeps both together with SU(4), forbids every bilinear mass and pair at K; under the Z4 of mode number the one-taste K mirror is 8 Weyl of one charge (Z16 index 8, the light K modes carrying +8), so a symmetric trivially gapped K mirror is anomaly-forbidden in this one-taste toy, assuming the standard Z16 classification applies to the on-site lattice symmetry (topological order was not tested). The note estimates that the same counting gives index 0 mod 16 for 16 Weyl per charge (the Spin(10) content), so the anomaly would not forbid the phase there; #10004 builds the 16-Weyl SU(4) model for this, which is a different model from the one-taste toy. Finite diagnostics (sign-free CT-INT, L = 4 at beta = 8 for g/t = 0.25, 2, 4, 6; L = 4, 6 at beta = 4 for g/t = 2): the L = 4 K-mirror gap is O(g) already at g/t = 0.25 (finite-size zero-mode atom), so it is not a bulk gap; at g/t = 2 and beta = 4 the gap falls 2.18(16) -> 1.53(5) from L = 4 to 6, S_pair/N 0.188 -> 0.039, xi/L 0.250 -> 0.116, with no pair or mass order; at beta = 8 and L = 4, xi/L is 0.175, 0.263, 0.382, 0.424 at g/t = 0.25, 2, 4, 6 (L = 6 at g/t = 4 and 6 was not run). No symmetric gapped window is established; at L <= 6 the K-mirror gap is inconclusive. Not Spin(10), not the supplied cube tick. Source: the #9994 note at head d2a4f35a7d; its runner and cache stay on the branch at the recorded commit.

## 2. Locality of the one-family U(1) anomaly: #10083, then #10084, then #10085

- **#10083, post-hoc reading withdrawn (by #10084):** at m0 = 1.0 the one-family coefficient "-9e-7 at |p| = 0.39 ... falls faster than p^2" is not a p^2 regime; #10084 shows it is a cancellation in the order of the background amplitude eps. #10084 also rejects the slow-scale reading min(m0, 2 - m0) for the kernel decay rate (its control criterion is not met; measured rates about 0.72-0.75 against 0.30). #10083's other results at m0 = 1.6 (exact integers on 6^4, the 16's flux integral 0, lone doublet -18, pre-set locality criteria P1, P2, P4, P4b, P5 not met for L <= 24, isotropic small tori Polyakov-loop dominated for the 16) are not replaced.
- **#10084's measurement of the four-field coefficient, narrowed (by #10085):** the value c4 = 1.3-1.4e-4 at s = 0.038 and 0.017 came from backgrounds with eps = 0.3 and 0.15, outside the admissibility bound ||1 - U_p|| < 1/30, and from T = 16 at L = 24. #10085 repeats the test with eps = 0.01, 0.02, 0.03 (admissible), L = 12, 16, 24, T = 24, 32: at L = 24, T = 32, c4 = +1.127e-4, +6.72e-5, -3.599e-4 at |p_hat| = 0.26, 0.52, 0.77. The old L = 24 value 1.42e-4 is about 26% above the admissible 1.13e-4, equivalently the admissible value is about 20% below the old one (the numerator and baseline matter: #10085's own text says "about 25%"). The not-met finding of #10084 stands; #10084's kernel-locality results (exponentially local with an L-independent length, zero-momentum value within 0.5% for L >= 10, doublet tail equal to |gamma_L|) are not replaced.
- Internal inconsistencies in the sources: #10083 reports a P5 exponent of 0.10 while its prose gives a local exponent rising from 0.30 to 0.69, not reconciled; its title says lattices to 24 while the per-charge zero-momentum value uses L <= 16. #10084's prose says P4 misses the 2% bound only on L = 6 and 8, while its table lists L = 8 at -1.83%.
- **Torus artefact, method finding of #10083.** On isotropic small tori the 16's single-mode density is Polyakov-loop dominated (a holonomy shift flips its sign on 8^4) and m0 = 1.6 carries a slow scale. #10083 flags #10051's 4^4 densities as unchecked and suggests a modest effect from their eps^4 scaling. #10052 uses the same kind of torus (3^4) and is not tested either. The eps^4 exponents of #10051 and #10052 are therefore unchecked against this artefact; their exact identities and integer index sums are unaffected.
- Standing statement: #10085 does not show that the one-family four-field coefficient is non-local; it reports that, at L <= 24 and |p_hat| >= 0.26, it does not vanish like p^2; supplied perturbative locality argues against a genuine non-local piece; the discriminating test at L = 32, 48 was not run.

## 3. #10041: open layering question answered for turn-commuting gates

#10041 says it is open whether some covariant layering of CTWIST exists (a finite search found none at depths 5, 7, 9). #10064 shows, for free Floquet slabs with the (111) turn as symmetry, that any circuit of cube-local gates each commuting with that turn has zero turn-graded winding, while FREEZE has W_F = (-2, 1, 1); hence FREEZE is not a product of such gates at any depth. #10065 gives W(CTWIST) = W(U_A) = (-4, 2, 2) = 2 W_F, and that FREEZE halves a winding already present in CTWIST. A gate commuting with all 12 site rotations commutes in particular with the site-gauged (111) turn, so this exact statement also excludes #10041's all-rotation layering, for FREEZE (W_F != 0) and for CTWIST (W = 2 W_F), at any depth. Covariance of the full walk is unaffected.

## 4. #10063 and #10064: static versus Floquet slabs

#10063 (logged) shows that on any static, turn-symmetric slab whose only turn-axis zero crossings are the K = 0 wall Weyls, the eigenvalue flow forces q_mirror = q_light, and concludes the mod 3 is not recovered on any realised slab. That conclusion is restricted to static slabs without extra axis crossings and excludes Floquet slabs; #10063 itself labels the Floquet reading as supplied, not checked. #10064 checks it: a Floquet circuit slab can put the mirror in the other copy only through a nonzero turn-graded winding, for odd Ls with a termination that is not forced (even Ls gives q_mirror = q_light). Tension recorded in #10064 and not resolved: a T-invariant charge-4 mirror term on FREEZE first exists at four families (#10031, logged), while the slab bookkeeping allows N_f = 3, 6, 9 with a supplied index form; for N_f = 3 the mirror gap would need the 16's internal structure, which is not computed.

#10031 also finds that its N_f = 4 term keeps Z4 and SU(4), so a symmetric trivial mirror gap is anomaly-forbidden there; Spin-Z4 anomaly freedom of the bare label term needs N_f = 0 mod 8, with SU(N_f) broken. The one-cell symmetric state needs a supplied mirror number bias; without it the cell ground state is 2-fold. The literature Z16 classification is an input. Its conclusion is that the term is not a chirality fix, because it frees the X and M partners.

## 5. The family-class tick: #10072, #10073, #10074

- The same supplied family-class tick is called "adopted" in #10072 and "suspended" in #10073. Neither status is carried; no rule is adopted here.
- #10073 narrows #10072: the bulk reading (free terms or tick-alternating interactions) is excluded; the far-termination reading is open pending far-wall symmetric gapping and rechecks; the 96-element group, low-energy, CP and lapse results derived for a FREEZE bulk need rechecking for the slab reading.
- #10074 narrows #10073's slab reading: the termination is a chosen boundary bit (both end placements are valid slabs with the same total winding, about three bits), no layer-preserving doubler map exists, the near wall is pi-free and screening in the toy (induced charge 0.42, against 1e-12 for an exactly S-doubled control), and the far wall (q1,-), (q2,+), (q1,-) times 16 has a turn Z3 anomaly of 6 mod 9 at k = 0 and can be symmetrically gapped only for the three families together under the supplied index form; the far-wall gapping itself is not shown; the criterion that the termination be forced fails.

## 6. #9980 narrowed by #9985

#9985 states that it builds on #9980 and narrows its sections C and E. #9980 (a 2D U(1) toy, 8 x 8 torus, Ls = 8) finds the smoothed slab's photon response equal to the light end's alone to below 3% with no gauge-variant term, and that the mirror is not removed (it sits in every 't Hooft vertex). #9985 reads #9980's smoothed/unsmoothed photon response of 0.26-0.33 rather than 1/2 as an induced gauge-invariant term c (A - A_*)^2, which is marginal in 2D (why the 2D toy passed) and is a cutoff-scale photon mass in its 4D slab models; and it shows by an exact end-exchange symmetry that a layer-blind fold quench fills the light and mirror edge modes equally (0.6606 each in the 1+1D Chern-strip slab), so a thermal mirror gives Delta N_eff = 2.25. #9980 gives the same Delta N_eff = 2.25 for a once-thermal mirror and about 0 for an unpopulated one. The tuned subtraction and the layer-0-only reheating that #9985 says a rescue would need are not supplied by any rule in these notes.

## 7. #9898 narrowed by #9907

#9898 states that the particle-hole-symmetric one-copy tick S has c = 0 with its zero "exact only in its form". #9907 shows that no symmetry of S forbids the additive mass: W U W = U^-1 holds for every mass and forbids none, and one-loop link dressing shifts the light level by about -0.142 e^2 per tick in supplied photon laws, with the same sign in every variant. The no-go that no tick has one particle-antiparticle-symmetric light copy with protected mass is stated as derived, not run, under the hypothesis that the gauge charges are block occupations and the charge commutes with the tick in every static electric background.

## 8. The filtered-quartic toy sequence: #9959, #9965, #9975, #9983, #9992

- #9975 narrows #9965's g/t = 4 result: in the half-filled 3D toy at mu = 0 the face planes carry free Fermi lines, so the toy is gapless at every g/t and "no order at g/t = 4" cannot be a fully gapped symmetric phase of that toy; comparisons should use the off-face sector. Nothing in #9975 decides the 3D question.
- #9983 notes that its symmetric window sits beside a free point whose only gapless mode is a quadratic touching at Gamma, so the window may be the trivially gapped side of that band rather than a gapped Dirac mirror. #9992 runs a genuine Dirac band with the block-local, non-overlapping quartic, not the cube-filtered one. #9983's statements on the filtered quartic (pair order at g/t >= 8, a window at g/t <= 2 beside a quadratic touching) are not replaced.
- Source inconsistencies: #9965 states a margin of "at least 0.25 per term" while its quoted energies give 0.246 (-0.614 against -0.368); it gives xi/L = 0.429 (live) in one place and 0.436(10) (recorded) in the table. #9975's prose says ratios to free "grow with L in every sector" while its table is not monotone. #9983's text gives pair-gap L-independence at g/t = 2 while its beta = 8 table has [0.50, 0.61] -> [0.33, 0.51].

## 9. The 3450 far-wall chain: #10058, #10076, #10078

#10076 weakens #10058's L = 12 result: the g = 200 gap 4.03 (neutral) and 4.84 (single-particle) at L = 12 become 3.36 / 4.31 (L = 14), 1.60 / 1.54 (L = 16), 1.44 / 1.42 (L = 18). Persistence ratio gap(18)/gap(12) = 0.358, below the pre-set 0.5, so the classification is inconclusive and persistence is not established. In #10076's prose "falls by 0.40" means the later gap is 0.40 of the earlier. #10078 says the decline is not generic to charge-4 terms, supported only on its supplied eight-Majorana proxy chain; neither result concerns the bulk or the light wall.

## 10. Narrowings of earlier register readings

- #9896: "The register states that inversion swaps left and right; in fact inversion alone swaps SU(2)_even and SU(2)_odd and leaves the copy label fixed, and M is the symmetry that exchanges family and mirror."
- #9909: the requirement that a term "must change mode number by four" should read that mode-number conservation must break, Z4 is the largest residual, and it survives exactly when every term has Delta N = 0 mod 4.
- #9911: notes that assume two light tastes per family after mirror gapping are narrowed; without the repair term there are eight tastes per family.
- #10035 says a glide-symmetric band that moves the q = 1 tastes off K = 0 is not excluded. #10033 excludes it for free one-mode ticks on the 2^3 cell that keep the glide and the three 2-fold rotations, at any range, by its glide-parity theorem. Its escapes (extra light doublets, one turn without the 2-fold rotations, composite cells, coarser rungs, breaking the glide) are not constructed.
- #10028 (logged): the massless tick's exact internal symmetry algebra has dimension 1, not 8. The dimension-8 value came from only three momenta, in the family-count note #10016 (outside this theme, A11); #10044 (outside this theme) checks saturation at 12 and 20 momenta. #10016's E+E taste decomposition and one-light-family result are not replaced by this.

## 11. Conflicts between notes in this theme

- **Label collision (CL-1).** The notes call a supplied cube tick "CL-1". In `docs/CANDIDATE_LAWS.md`, CL-1 is the lossless-influence clause, CL-2 the record-removal clause and CL-3 a pending conservation proposal; none specifies a tick, and the register states that admissibility does not specify time evolution. The record, following, response and step-bound laws that #9895-#9897 and #9905-#9909 attribute to "the register" are as those notes state them, not the current register text. Statements here that depend on them are conditional on those supplied rules.
- **Step bound.** #9897 gives the register step bound as below 0.04 with band maximum 0.08; #9906 gives eps < 0.037 with band maximum 0.0740. Both are as supplied by those notes.
- **Spin(10) pair-square gaps.** #9910 (one mirror 16 with two spin components, H = g(Omega + Omega^dag), gap 19.0715 g, fermion gap 33.5804 g) and #10061 (two 16s, particle-hole symmetric ordering, unique singlet ground state at -144 g, gap 4 g) concern different Hamiltonians; #10060 and #10061 cite the 19.1 g value from the register without recomputing it, and neither contradicts it. #10061's naive ordering has a two-fold charged ground state; only the particle-hole symmetric ordering gives the unique state.
- **Light and mirror labels on FREEZE.** #10030, #10031 and #10042 call tau3 = +1 (q = 1) light. #10041 calls q = 2 L and q = 1 R while its section C calls tau3 = -1 R, which #10031 notes clashes with its own sign rule. #10064, #10070, #10072, #10073 and #10074 call q 2 light, which by #10064 A1 is tau3 = -1. eta_x makes the choice of sector conventional and #10031 calls the naming a convention. #10030 A1 holds for either label, and #10064 D1 gives the same allowed N_f for the reflected slab. Read each note's labels within that note.
- **One copy on 2^3.** The 2^3 statements of #9892 and #9898 assume covariance under the cube rotation group (the note's 'rotation group'), with or without inversion. #9897, #10028 part A, #10035 part B and FREEZE reach reduced light content on the 2^3 cell by keeping only the 12 tetrahedral rotations, and they stay vector-like or keep a pinned pi node. These do not conflict.
- **Status of the overlap rule.** #10049 treats the overlap rule as a candidate for a decision; #10051 and #10052 call it adopted. Nothing is adopted here.
- **Title versus body, #10052 and #10051.** Both titles say the family anomaly cancels (locally, through cubic order). The body results are exact only for the lattice-charge-conjugation vanishing of the pure-SU(3) and pure-SU(2) densities and for the integer index sums; in generic backgrounds the family's covariant anomaly density is an eps^4 remainder, a finite diagnostic. #10051 gives the order-4 coefficients (sum Y^5 = 5/9, sum over doublets of Y^3 = -1/9) as non-zero; #10052 notes the unexplained absence of an order-3 residual. #10051 discloses that an earlier fixed 15% threshold on the 4^4 Y ratio failed (0.16) and was replaced by a predicted eps^2 fall criterion.
- **Frame of reference for pre-set criteria.** In #10056, #10058, #10060 and #10061 some pre-set thresholds were set after scratch exploration or revised after a first run, as each note discloses; the numbers are finite diagnostics.

## Source notes carried with this consolidation

Each kept result's own note, runner and cache are carried byte-for-byte from its source PR.

- #9863: [TICK_UPDATE_WINDING_FIXES_NET_CONE_CHIRALITY_AT_QUASI_ENERGY_ZERO_AND_PI_BOUNDED_THEOREM_NOTE_2026-10-21.md](TICK_UPDATE_WINDING_FIXES_NET_CONE_CHIRALITY_AT_QUASI_ENERGY_ZERO_AND_PI_BOUNDED_THEOREM_NOTE_2026-10-21.md)
- #9895: [RECORD_AND_FEEDBACK_HISTORIES_OF_BLOCK_TICKS_HAVE_ZERO_FLOW_INDEX_BOUNDED_THEOREM_NOTE_2026-10-21.md](RECORD_AND_FEEDBACK_HISTORIES_OF_BLOCK_TICKS_HAVE_ZERO_FLOW_INDEX_BOUNDED_THEOREM_NOTE_2026-10-21.md)
- #9896: [WALL_PUMP_AND_MIRROR_GAPPING_ROUTES_TO_CHIRALITY_UNDER_THE_CANDIDATE_LAWS_BOUNDED_THEOREM_NOTE_2026-10-21.md](WALL_PUMP_AND_MIRROR_GAPPING_ROUTES_TO_CHIRALITY_UNDER_THE_CANDIDATE_LAWS_BOUNDED_THEOREM_NOTE_2026-10-21.md)
- #9908: [OCTREE_LADDER_OF_CUBE_TICKS_GIVES_ONE_FINE_CHIRALITY_ONLY_BY_A_SWINDLE_WITH_UNBOUNDED_RANGE_BOUNDED_THEOREM_NOTE_2026-10-21.md](OCTREE_LADDER_OF_CUBE_TICKS_GIVES_ONE_FINE_CHIRALITY_ONLY_BY_A_SWINDLE_WITH_UNBOUNDED_RANGE_BOUNDED_THEOREM_NOTE_2026-10-21.md)
- #9911: [LIGHT_COPY_EXACTLY_MASSLESS_YET_MIRROR_GAPPING_RELEASES_VECTOR_LIKE_DOUBLERS_BOUNDED_THEOREM_NOTE_2026-10-21.md](LIGHT_COPY_EXACTLY_MASSLESS_YET_MIRROR_GAPPING_RELEASES_VECTOR_LIKE_DOUBLERS_BOUNDED_THEOREM_NOTE_2026-10-21.md)
- #9971: [THE_RUNG_LADDER_IS_A_DOMAIN_WALL_DIRECTION_WITH_EXACT_INFLOW_BUT_BOUNDED_SPEED_MAKES_ITS_COARSE_RUNGS_A_CHARGED_TOWER_BOUNDED_THEOREM_NOTE_2026-10-22.md](THE_RUNG_LADDER_IS_A_DOMAIN_WALL_DIRECTION_WITH_EXACT_INFLOW_BUT_BOUNDED_SPEED_MAKES_ITS_COARSE_RUNGS_A_CHARGED_TOWER_BOUNDED_THEOREM_NOTE_2026-10-22.md)
- #9985: [GRABOWSKA_KAPLAN_FAR_LAYERS_PASS_THE_NIELSEN_NINOMIYA_COUNT_BUT_INDUCE_A_GAUGE_INVARIANT_CUTOFF_SCALE_PHOTON_MASS_ABOVE_THE_SMOOTHING_SCALE_BOUNDED_THEOREM_NOTE_2026-10-22.md](GRABOWSKA_KAPLAN_FAR_LAYERS_PASS_THE_NIELSEN_NINOMIYA_COUNT_BUT_INDUCE_A_GAUGE_INVARIANT_CUTOFF_SCALE_PHOTON_MASS_ABOVE_THE_SMOOTHING_SCALE_BOUNDED_THEOREM_NOTE_2026-10-22.md)
- #9992: [THE_BLOCK_LOCAL_QUARTIC_GAPS_THE_DIRAC_MIRROR_SYMMETRICALLY_AND_RELEASES_THE_LIGHT_PARTNERS_BOUNDED_THEOREM_NOTE_2026-10-22.md](THE_BLOCK_LOCAL_QUARTIC_GAPS_THE_DIRAC_MIRROR_SYMMETRICALLY_AND_RELEASES_THE_LIGHT_PARTNERS_BOUNDED_THEOREM_NOTE_2026-10-22.md)
- #9993: [THE_LIGHT_COPY_ZONE_CORNER_PARTNERS_ARE_VECTOR_LIKE_ONLY_THROUGH_THE_SUBLATTICE_CHARGE_BOUNDED_THEOREM_NOTE_2026-10-22.md](THE_LIGHT_COPY_ZONE_CORNER_PARTNERS_ARE_VECTOR_LIKE_ONLY_THROUGH_THE_SUBLATTICE_CHARGE_BOUNDED_THEOREM_NOTE_2026-10-22.md)
- #10004: [THE_ZOOMED_FILTERED_MIRROR_TERM_KEEPS_THE_CHIRAL_Z4_AND_THE_16_WEYL_TOY_IS_ANOMALY_FREE_WITH_AN_UNSETTLED_K_GAP_BOUNDED_THEOREM_NOTE_2026-10-22.md](THE_ZOOMED_FILTERED_MIRROR_TERM_KEEPS_THE_CHIRAL_Z4_AND_THE_16_WEYL_TOY_IS_ANOMALY_FREE_WITH_AN_UNSETTLED_K_GAP_BOUNDED_THEOREM_NOTE_2026-10-22.md)
- #10030: [THE_CORNER_STABILIZER_FORCES_A_SCALAR_LIGHT_BLOCK_AT_X_AND_M_SO_NO_ROTATION_COVARIANT_FREEZE_DEFORMATION_GAPS_THE_LIGHT_PARTNERS_LIGHT_LIGHT_BOUNDED_THEOREM_NOTE_2026-10-23.md](THE_CORNER_STABILIZER_FORCES_A_SCALAR_LIGHT_BLOCK_AT_X_AND_M_SO_NO_ROTATION_COVARIANT_FREEZE_DEFORMATION_GAPS_THE_LIGHT_PARTNERS_LIGHT_LIGHT_BOUNDED_THEOREM_NOTE_2026-10-23.md)
- #10041: [THE_COMPOSITE_TWIST_WALK_IS_A_FIVE_LAYER_CUBE_LOCAL_CIRCUIT_AND_FREEZING_ONE_COPY_LEAVES_ONE_L_AND_ONE_R_PER_NODE_BOUNDED_THEOREM_NOTE_2026-10-23.md](THE_COMPOSITE_TWIST_WALK_IS_A_FIVE_LAYER_CUBE_LOCAL_CIRCUIT_AND_FREEZING_ONE_COPY_LEAVES_ONE_L_AND_ONE_R_PER_NODE_BOUNDED_THEOREM_NOTE_2026-10-23.md)
- #10042: [THE_COMPOSITE_TWO_CELL_LIGHT_LABEL_MAKES_THE_CORNER_STABILIZERS_REDUCIBLE_BUT_THE_LIGHT_FLOQUET_WINDING_FORCES_THE_MIRROR_TO_CARRY_THE_OPPOSITE_CHIRALITY_BOUNDED_THEOREM_NOTE_2026-10-23.md](THE_COMPOSITE_TWO_CELL_LIGHT_LABEL_MAKES_THE_CORNER_STABILIZERS_REDUCIBLE_BUT_THE_LIGHT_FLOQUET_WINDING_FORCES_THE_MIRROR_TO_CARRY_THE_OPPOSITE_CHIRALITY_BOUNDED_THEOREM_NOTE_2026-10-23.md)
- #10049: [THE_OVERLAP_OF_THE_CUBE_WALK_EUCLIDEAN_KERNEL_GIVES_EXACT_GINSPARG_WILSON_CHIRALITY_WITHOUT_DOUBLERS_BUT_ITS_CHIRAL_PROJECTOR_IS_NOT_A_WALK_SECTOR_BOUNDED_THEOREM_NOTE_2026-10-23.md](THE_OVERLAP_OF_THE_CUBE_WALK_EUCLIDEAN_KERNEL_GIVES_EXACT_GINSPARG_WILSON_CHIRALITY_WITHOUT_DOUBLERS_BUT_ITS_CHIRAL_PROJECTOR_IS_NOT_A_WALK_SECTOR_BOUNDED_THEOREM_NOTE_2026-10-23.md)
- #10052: [THE_OVERLAP_CHIRAL_DETERMINANT_IN_SU3_X_SU2_X_U1_BACKGROUNDS_CANCELS_THE_ONE_GENERATION_GAUGE_ANOMALY_LOCALLY_AND_IN_EVERY_MEASURED_INDEX_INCLUDING_A_Z6_TWISTED_FLUX_BUT_ANOMALOUS_SUBSETS_DO_NOT_BOUNDED_THEOREM_NOTE_2026-10-23.md](THE_OVERLAP_CHIRAL_DETERMINANT_IN_SU3_X_SU2_X_U1_BACKGROUNDS_CANCELS_THE_ONE_GENERATION_GAUGE_ANOMALY_LOCALLY_AND_IN_EVERY_MEASURED_INDEX_INCLUDING_A_Z6_TWISTED_FLUX_BUT_ANOMALOUS_SUBSETS_DO_NOT_BOUNDED_THEOREM_NOTE_2026-10-23.md)
- #10056: [A_DOMAIN_WALL_TICK_WITH_THE_LAYER_DIRECTION_AS_SPACE_PUTS_ONE_WEYL_CONE_ON_EACH_WALL_BUT_THE_CIRCUIT_FORCES_THE_MIRROR_ONTO_THE_FAR_WALL_BOUNDED_THEOREM_NOTE_2026-10-23.md](A_DOMAIN_WALL_TICK_WITH_THE_LAYER_DIRECTION_AS_SPACE_PUTS_ONE_WEYL_CONE_ON_EACH_WALL_BUT_THE_CIRCUIT_FORCES_THE_MIRROR_ONTO_THE_FAR_WALL_BOUNDED_THEOREM_NOTE_2026-10-23.md)
- #10060: [THE_FORCED_FAR_WALL_TERM_HAS_A_UNIQUE_GAPPED_THREE_SITE_CELL_STATE_BUT_A_STRONG_COUPLING_CELL_ONLY_MOVES_THE_MIRROR_AND_THE_ONE_ORBITAL_SIXTEEN_SITE_HAS_ONLY_TWO_SPIN10_SINGLETS_BOUNDED_THEOREM_NOTE_2026-10-23.md](THE_FORCED_FAR_WALL_TERM_HAS_A_UNIQUE_GAPPED_THREE_SITE_CELL_STATE_BUT_A_STRONG_COUPLING_CELL_ONLY_MOVES_THE_MIRROR_AND_THE_ONE_ORBITAL_SIXTEEN_SITE_HAS_ONLY_TWO_SPIN10_SINGLETS_BOUNDED_THEOREM_NOTE_2026-10-23.md)
- #10064: [A_CIRCUIT_SLAB_PUTS_ITS_MIRROR_IN_THE_OTHER_COPY_ONLY_THROUGH_A_NONZERO_TURN_GRADED_WINDING_WHICH_FORCES_EQUAL_FLOW_AT_QUASI_ENERGY_PI_AND_IS_SET_BY_TERMINATION_BOUNDED_THEOREM_NOTE_2026-10-23.md](A_CIRCUIT_SLAB_PUTS_ITS_MIRROR_IN_THE_OTHER_COPY_ONLY_THROUGH_A_NONZERO_TURN_GRADED_WINDING_WHICH_FORCES_EQUAL_FLOW_AT_QUASI_ENERGY_PI_AND_IS_SET_BY_TERMINATION_BOUNDED_THEOREM_NOTE_2026-10-23.md)
- #10072: [THE_FAMILY_CLASS_TICKS_FORCED_PI_SECTOR_IS_A_LIGHT_CHARGED_INVERTED_COPY_WHOSE_DOUBLER_MAP_CANCELS_ALL_VACUUM_POLARIZATION_SO_IT_NEEDS_REPAIR_WHILE_ITS_ANOMALIES_STAY_SAFE_BOUNDED_THEOREM_NOTE_2026-10-24.md](THE_FAMILY_CLASS_TICKS_FORCED_PI_SECTOR_IS_A_LIGHT_CHARGED_INVERTED_COPY_WHOSE_DOUBLER_MAP_CANCELS_ALL_VACUUM_POLARIZATION_SO_IT_NEEDS_REPAIR_WHILE_ITS_ANOMALIES_STAY_SAFE_BOUNDED_THEOREM_NOTE_2026-10-24.md)
- #10073: [THE_FAMILY_CLASS_WINDING_FORCES_BULK_PI_STATES_BUT_A_SLAB_CAN_PUT_ALL_ITS_PI_FLOW_ON_THE_FAR_WALL_WHILE_NO_TICK_ALTERNATING_TERM_SEPARATES_PI_PI_FROM_ZERO_ZERO_BOUNDED_THEOREM_NOTE_2026-10-24.md](THE_FAMILY_CLASS_WINDING_FORCES_BULK_PI_STATES_BUT_A_SLAB_CAN_PUT_ALL_ITS_PI_FLOW_ON_THE_FAR_WALL_WHILE_NO_TICK_ALTERNATING_TERM_SEPARATES_PI_PI_FROM_ZERO_ZERO_BOUNDED_THEOREM_NOTE_2026-10-24.md)
- #10085: [THE_ONE_FAMILY_U1_ANOMALY_FOUR_FIELD_COEFFICIENT_IN_ADMISSIBLE_BACKGROUNDS_AT_WILSON_MASS_ONE_DOES_NOT_VANISH_LIKE_P_SQUARED_BOUNDED_THEOREM_NOTE_2026-10-25.md](THE_ONE_FAMILY_U1_ANOMALY_FOUR_FIELD_COEFFICIENT_IN_ADMISSIBLE_BACKGROUNDS_AT_WILSON_MASS_ONE_DOES_NOT_VANISH_LIKE_P_SQUARED_BOUNDED_THEOREM_NOTE_2026-10-25.md)

## Other results

The scope text is copied verbatim from each source note. The full note, runner and cache stay on the listed branch at the listed commit.

| PR | Result | Disposition | Scope as stated in the source | Branch and commit |
|---|---|---|---|---|
| #9884 | The block tick has no exact copy SU(2), only a sublattice axial remnant | logged | For the supplied two-partition block tick with the spin-3/2 corner action: six anticommuting Hermitian involutions built from the tick generate all 8x8 matrices, so the K-independent block-local commutant is span{1, eps} at mu = 0 and the scalars for mu > 0; the long-wavelength Dirac algebra read from the tick gives C^8 = Dirac(4) x copy(2) with an emergent U(2) that the lattice breaks at O(k^2); the only exact remnant is the sublattice sign eps = gamma5 sigma3; a block-local inversion flips gamma5, so the content is vector-like; the copy doublet is the E irrep of the cube group; and the w = pi sector holds two massless copies at K = pi(1,1,1). No chirality, weak SU(2), copy symmetry or physical species is established. | `claude/toe-margolus-doublet-20261021` `d1a3d8eb8150` |
| #9892 | One light Dirac copy needs a tick written on cells larger than 2^3 | logged | For covariant partitioned ticks with one fermion mode per site of Z^3, two-partition L^3 Margolus ticks are cubic covariant only for offset (L/2)(1,1,1), so none exists for odd L; a spinorial site character exists only for stabilisers C1, C2, C3, C4, D3 (with parity only Cs, C3v, D3d), and at the 2^3 corner parity forces the j = 3/2 type; for the 2^3 rung no site action gives the representation content one Dirac copy at an invariant momentum needs, the smallest geometries with that content have 16 sites per cell (rotations) and 32 (with parity), integer-spin site actions force an even copy count, and reading the supplied 2^3 tick on 4^3 cells keeps two copies; a supplied 4^3 Margolus tick with exactly one light Dirac copy exists on the grids checked. Finite diagnostics; the 4^3 block rule, its mass tuning and the hop are supplied. No adopted cell rule, chirality or physical matter content is established. | `claude/toe-other-cells-20261021` `3b358f0a67d4` |
| #9897 | A copy-selective mass and a mirror pair square on the cube tick | logged | For the cube tick of the candidate laws register, a supplied copy-selective mass that keeps the 12 tetrahedral turns leaves one light Dirac copy without tuning but stays vector-like; the response law's link-mediated terms conserve mode number and cannot gap the mirror alone; a supplied anomaly-allowed mirror pair square needs the exact chiral SU(2)s that exist only at step pi/2 and mu = 0, outside the register's step bound; no chirality, gapped mirror phase or adopted rule is established. | `claude/toe-chiral-smg-20261021` `db19f82f9aa8` |
| #9898 | One light Dirac copy on 4^3 blocks and the protection versus particle-hole trade-off | logged | For covariant block unitaries with one mode per site, 2^3 cubes give a light Dirac only with two copies or a star of at least 3; on supplied 4^3 blocks with inversion a glide built from the register's reflection W makes the light pair massless without tuning, but a one-copy tick cannot have both that protection and an exact w -> -w symmetry; a supplied particle-hole-symmetric 4^3 tick has one light Dirac copy with c = 0 and its zero exact only in its form; no adopted tick, stability under link dressing or chirality is established. | `claude/toe-onecopy-verify-20261021` `1c69f8094dcd` |
| #9905 | The step-pi/2 cube tick has no continuous logarithm but conserves a local chiral generator | logged | For the cube tick of the candidate laws register, a wrap of quasi-energy to 2 pi needs at least ceil(pi/(2 eps)) particle-hole pairs, so step pi/2 fails the vacuum bound; at step pi/2 the tick has no continuous logarithm, but it conserves the strictly local generator H' = (i/2)[W_o, W_e], which keeps the sublattice sign exactly at every flow time and has isotropic cones at Gamma and R = pi(1,1,1), four Dirac tastes in all; on 2^3 cubes no small-band word of chirality-keeping layers gives an isotropic cone and no covariant chiral mass gaps the R doubler; no tick update, flow reading, chirality or matter content is established. | `claude/toe-chiral-step-20261021` `21f3c6534c93` |
| #9906 | The cube tick keeps a chiral weak SU(2) only at step pi/2 with no species mass | logged | For the cube tick of the candidate laws register, the sublattice sign commutes with the tick iff the step is pi/2 and the species mass is 0, so a chiral SU(2) exists only there, the copy factor breaks it at every step, and at small step the exact one-body group is a single vector-like U(8); with a supplied Spin(10) pair square as the mirror term the linked group would be su(4)+su(2)+su(2); given a chiral link, Yang-Mills forces one coupling, the contact limit gives m^5 rates and V-A Michel parameters, and fermion bilinears give rho = 1; no exact chiral weak SU(2) at the register's step, no breaking scale and no 125 GeV scalar are established. | `claude/toe-electroweak-20261021` `14230e5c213b` |
| #9907 | Link dressing gives the one-copy block tick an unprotected additive mass | logged | For the supplied one-copy 4^3 block tick S, its particle-antiparticle symmetry W U W = U^-1 and its Ginsparg-Wilson-type relation hold for every mass and forbid none; with W-compatible cube-phase links and the filled sea, one-loop dressing in supplied photon laws shifts the light level by about -0.142 e^2 per tick with the same sign in every variant, while a protected control tick gives zero; an overlap tick built from S is exactly chiral in magnetic backgrounds but quasi-local, and electric backgrounds and dynamical links give it a mass of the same order; no protected light copy, photon law or adopted tick is established. | `claude/toe-s-tick-dressing-20261021` `829e13737ac8` |
| #9909 | The tetrahedral four-mode term gaps both copies, and a pair across tetrahedra gaps one | logged | On the cube tick of the candidate laws register, each tetrahedron has one four-mode term (its top form, a Fidkowski-Kitaev term keeping a Z4 of mode number); the mirror map fixes it, so it gaps both light copies and cannot select one; the two copies are the eigenspaces of s3 = -S F at every step, and a supplied term pairing one F-pair from each tetrahedron is the only four-mode term on a single copy, leaving the other copy exactly free at zero momentum in one cube and on a 4x2x2 torus; the residual Z4 is anomaly-free per family only with n^c; light-copy gaplessness at nonzero momentum, the rung-1 gap, chiral gauge couplings and any adopted rule are not established. | `claude/toe-tetra-pairing-20261021` `80739e2cde91` |
| #9910 | The Spin(10) pair square alone gives a unique gapped symmetric ground state on one mirror cell | logged | On one cell carrying a supplied mirror 16 with two spin components (32 modes), the Spin(10) pair square H = g(Omega + Omega^dag) alone has a unique Spin(10)-singlet, spin-singlet, Z4-trivial ground state E0 = -2g sqrt(11088 + 48 sqrt 21081), a gap 19.0715 g and a fermion gap 33.5804 g, for every complex g != 0; the lattice phase at finite hopping, the masslessness of the light copy and chirality are not established. | `claude/toe-smg-verify-20261021` `839b6788c352` |
| #9912 | On the fine-rate octree ladder the charged coarse sea's magnetic response doubles per rung | logged | On the supplied octree ladder ticked at the fine rate and gauged by a U(1) that commutes with the ladder, coarse modes carry the fine charge, a rung-j plaquette carries 4^j times the fine flux, and the B^2 response per volume scales as 2^j per rung (E^2 as 2^-j); finite gapped tori give a positive bulk rung coefficient; estimated against measurement, the resulting magnetic running is excluded, so the gauged fine-rate octree route fails; no escape route is established. | `claude/toe-octree-field-20261021` `cc18d1d83c8b` |
| #9927 | One-mode free sites carry no exact 3450 charge, and rotor matter admits an exact depth-three chiral disentangler in 1+1D | logged | In 1+1D: on chains of one-mode fermion sites with the staggered hop, the vector charge and the Kitaev-pairing axial charge are exact, but the chiral 3450 combination has non-integer one-body and many-body spectra, so no circuit, free or interacting, on-site or not, makes it an exact U(1) (spectral obstruction). With non-slipping rotor matter (an angle per site and a winding integer per link), the rederived Thorngren-Preskill-Fidkowski disentangler (one on-site and two link layers) maps the 3450 symmetry exactly onto an on-site ancilla symmetry, checked in exact rational arithmetic; anomalous charge sets (sum q_V q_A != 0) fail by exactly the predicted phase and carry endpoint charge; the dressed charges are local integers; linking gives an exact Gauss law that eats the ancillas, a Schwinger term proportional to sum q_V q_A, and, in a Gaussian reading, one massless neutral mode plus a massive photon; the Trotterised Gaussian update has one zero per flavour (no doublers) and the zero modes carry the chiral charges L(3,4), R(5,0). With Z_5 clocks only Z_5 is exact. In 3+1D, the 16 Weyl fields of one family with the right-handed neutrino group into four blocks of the source construction with vanishing mixed anomalies, and the Kuhn triangulation count is stated. Source construction: arXiv:2601.04304. Supplied model, finite diagnostic; no chiral SU(2), no V - A structure and no derivation of rotor matter from the axioms. | `claude/toe-tpf-circuit-20261021` `e43a88e21c48` |
| #9939 | Fermion parity is the vector SU(2) centre, not the chiral half, and two singlet rotors give jointly chiral SU(2) x U(1) with on-site gluing | logged | For an SU(2) doublet carried on fermion modes in 1+1D: on a cell of two complex modes the SU(2) centre is the cell fermion parity and the commuting charge SU(2) has centre minus it, and a supplied non-on-site chiral SU(2) on 3 cells also has centre equal to fermion parity up to a phase; in the vertex-lattice description the centre of any on-site SU(2) flows to the vector centre z_L z_R, which on the doublet is the fermion parity (Z_8 index 0), while the gluing of charge parity to SU(2) centre needs the left-mover centre z_L, which on the doublet is the chiral fermion parity (twisted spin 1/4, Z_8 index 4) and is not on-site; a spin carrier whose gapless sector is one SU(2)_1 per chirality has no fermionic operator, and in the half-filled Hubbard ring (L = 4, 6, U = 4) the lowest triplet carries momentum pi relative to the singlet ground state, so with the charge gapped the infrared spin half is lattice translation. A construction on fermion modes plus two supplied SU(2)-singlet compact rotors (charges (2, 4) and (-2, 4)) with one null locking term per rotor leaves exactly free Weyl modes L = (2,3) + 2(1,1), R = (2,1) + 2(1,3) (the swap content), anomaly-free with no invariant bilinear mass; the gluing generator equals the on-site singlet fermion parity on all 531441 sampled carrier states; the TPF rotor disentangler is exact for the anomaly-free rotor pair and fails for anomalous sets; the locking vertex is marginal at the free point and relevant under a supplied forward-scattering term. Supplied model, finite diagnostic: rotor matter, charges, locking couplings and forward scattering supplied; the flow to the locked phase is cited, not computed; 1+1D only. | `claude/toe-fermion-spin-half-20261021` `26dfc7d9e3e4` |
| #9944 | Propagator zeros sit on the Dirac partner's line and give no ghosts on a positive-norm lattice | logged | For an elementary field b Dirac-paired (mass m) with a charged partner chi: the propagator G_bb = (z - h_chi)/((z - h_b)(z - h_chi) - m^2) has its zero exactly on the partner's bare line z = h_chi, the self-energy m^2/(z - h_chi) carries the partner's pole, and det(z - H) = (z - h_chi) G_bb^-1, so the inverse of the zero is the partner's determinant (symbolic). In a free toy (two-band Wilson pair, L = 400 antiperiodic, m0 = 0.5, r = 1) the full pair's stiffness is 0 and its current weight below the pair gap is 0, while the truncation that drops the partner (full minus partner) has stiffness -1/pi and a sign-flipped low-frequency current response equal to minus the partner's: the ghost-like response is the subtracted partner. On the interacting filtered 3450 Wilson ladder (L = 3 antiperiodic, sector dimension 64444) with an exact on-site U(1) twist on every hop, the twisted Hamiltonian is Hermitian to 2.8e-17, the Kohn decomposition matches the ground-energy curvature to 2.7e-3 (stiffness about 16.7), every current spectral weight is non-negative (minimum at roundoff) and the weights sum to the norm, at couplings g = 0, 8, 16; the stiffness ratio stays positive (1.0, 0.991, 0.959). An estimate compares the measured R ratio near 30-35 GeV (about 3.9) with three response classes. Supplied model, finite diagnostic: free toy masses, the 3450 charges, the six-fermion interaction vectors, the two-site filter, L = 3, the twist on one charge; L = 3 cannot separate light and mirror shares; the Golterman-Shamir argument is engaged at the level of its abstract only. | `claude/toe-zeros-ghosts-20261021` `4e9590ea62cc` |
| #9959 | The strong-coupling face composite has no atomic limit and stays gapped on sheared tori | logged | For the cube-filtered quartic interaction at g -> infinity (c_x = sqrt8 times the cube average of the site modes, one charge-4 quartic per cube): the filtered modes have {c_x, c_y^+} = prod_i (1, 1/2, 0)[\|x_i - y_i\|] and on L^3 span exactly the (L - 1)^3 off-face momenta (rank 27 at L = 4, 125 at L = 6), so face modes are free spectators; the sheared tori T_n = Z^3/Lambda_n (n = 1, 2, 3, det L) are legitimate 3D tori carrying only the lines (q,0,0), (q,q,0), (q,q,q), on which the cube filter is exactly ((1 + e^iq)/2)^n with the faces X, M, R at q = pi; overlapping filtered terms do not commute (toy norms 0.866, 0.484, 0.248 for overlaps 1/2, 1/4, 1/8), so the limit has no atomic form; [e_k, H_int] = sum_x conj(A_xk) D_x with a three-fermion D (identity error below 1e-12 on T_1, L = 4); for mode-product states <h(c_y)> = e_atom sum_m beta_m(y)^4 for any charge-4-only quartic. Toy diagnostics (4 flavour modes, one SU(4)-singlet quartic c1c2c3c4 + h.c. per cube, not Spin(10)): open clusters of up to 5 cubes have unique ground states; on T_1, T_2, T_3 at L = 4, 6 the face composite D(face)\|GS> has no weight below 0.5 and lowest pole 0.9-2.3 atom units, with and without a face-gapped free band; t = 0 is singular at the faces (near-face modes almost free); a two-cube linked-cluster expansion fails the 1D control (about 0 against the exact 1.01), so it does not decide 3D. The gapped face composite is a finite diagnostic on these tori; the 3D question stays undecided. Supplied model, finite diagnostic: the toy content and quartic, the cluster shapes, the torus sizes and shears, the free band, the atom units. | `claude/toe-composite-band-3d-20261021` `316a90060d53` |
| #9965 | The cube-filtered quartic toy is sign-free and pairs at strong coupling | logged | For the supplied one-quartic SU(4) toy (four modes per site, H = -t sum a^+ a - g sum_x (c1 c2 c3 c4 + h.c.) with c_x = sqrt8 times the cube average, any real free band): the interaction expansion has configuration weights g^2n det(M)^4 with M real, so the toy is sign-free at every g, L and beta (a complex hop restores the sign problem). Finite diagnostics on L^3 tori at g -> infinity: translations stay unbroken (the cube-term susceptibility stays below 1 and falls with beta), the energy per term lies below every translation-breaking mode-product state and below the uniform pair state (-1/2), and the charge-2 pair correlation has a plateau with a correlation length growing faster than L (L = 4, 6 live; L = 8 recorded), i.e. a pair condensate breaking SU(4) x Z4, not a symmetric phase; at g/t = 4 the pair order is weakened at L = 4 and absent at L = 6 at T = 1/8 (recorded). The toy is not Spin(10); no symmetric mass generation is established or excluded for the Weyl 16. | `claude/toe-toy-qmc-20261021` `5abd52b70e19` |
| #9975 | The filtered quartic chain is symmetric and gapped at intermediate coupling, and the half-filled 3D toy has free face Fermi lines | logged | For the cube-filtered SU(4)-singlet quartic toy (4 flavours, -g sum_x (c1c2c3c4 + h.c.) on the filtered modes, NN hopping t at mu = 0 as in the 3D toy QMC): (1) on any torus with two transverse sizes equal to 2 (L x 2 x 2) the cube vectors span exactly the L - 1 off-face modes of the transverse-symmetric sector and each equals the 1D two-site filter (a_x + a_{x+1})/sqrt2 four times, so the interaction is the 1D filtered chain with coupling 4g and all other modes are free face spectators; at mu = 0 that sector's band is -2t cos q - 4t <= -2t (a filled band, gapped at g = 0), so this ladder cannot test the massless-to-gapped question; (2) in the half-filled 3D toy the face planes k_i = pi carry the free Fermi lines cos k_j + cos k_l = 1, where the filter vanishes: those modes commute with H_int, are exact zero modes on the L = 4, 6, 8 tori, and make the toy gapless at every g/t; (3) on open chains the alternating mode (-1)^x is outside the filter span ([n_face, H_int] = 0). Finite diagnostics on the bare 1D chain (Dirac points at pi/2; L = 4 exact sector diagonalisation, L = 6, 8 two-site DMRG at chi <= 96; face mode lifted): for g/t >= 4 the charge-1, charge-2 pair (the 6 of SU(4)), adjoint and neutral gaps stay of order t (pair gap 1.40, 1.76, 1.83 t at L = 4, 6, 8 for g/t = 4) while the free gaps fall as 1/L, the pair structure factor stays at its free value 1/2 within 0.04, pair correlations fall more than 10x over four sites, and there is no density or bond dimerisation; for g/t <= 1 the gaps are within about 1.5x of free. So in 1D a symmetric gapped window exists from about g/t = 2 to the largest coupling computed (16), with no pair order; nothing here decides 3D, where the face Fermi lines (item 2) keep the toy gapless. Supplied model, finite diagnostic: the toy content and quartic, the hopping and mu = 0, open chains, sizes, chi, seeds, the face lift, the sector penalty. | `claude/toe-smg-ladder-20261021` `6e09f25e6f4d` |
| #9980 | Far layers that read a smoothed field decouple the mirror from field strength, but not from gauge turns, topology or long wavelengths | logged | For a supplied 2D euclidean U(1) toy (a 1+1D world) on an 8 x 8 antiperiodic torus times Ls = 8 layers (Shamir slab, wall height M = 1, Pauli-Villars subtraction), with layer s reading a smoothed copy of the links (gradient flow with flow time growing in s, or rung-s block-flux averaging): (A) flow, block-flux averaging and anchor transports are gauge covariant per site, so the whole slab is exactly gauge invariant; flow and block averaging keep the topological charge and the harmonic part of the holonomy, while coarse Wilson lines with anchor transports (the naive zoom reading) concentrate flux and lose the charge mod 2 pi; a nearest-neighbour smoothing step is stable only for eps <= 1/(2d) and grows the flux variance by at most one cell^2 per step, so n layer-local steps smooth over at most sqrt(n) cells, while reading rung-s blocks reaches 2^s; (B, C) the light end keeps the full photon coupling, the far mirror's photon coupling falls to ~1e-4, both ends keep the full pure-gauge coupling, the smoothed slab's photon response equals the light end's alone to < 3% with no gauge-variant term, and for 3-4-5-0 the anomalous terms of the light end alone cancel (sum chi q^2 = 0) while a real gauge-variant term remains; (D) the flowed far field keeps index q Q for q = 1, 3, 4, 5, and the Q = 1 slab keeps one near-zero mode whose left vector is the far mirror's (spread, not removed): the mirror sits in every 't Hooft vertex; (E) estimates: smoothing radius r needs (r/a)^2 layer-local steps but log2(r/a) zoom layers (136 for the Earth radius, 200 for the horizon); no added Gamma_Z or alpha running for r >> 1/m_e; a once-thermal mirror gives Delta N_eff = 2.25 (excluded), an unpopulated one ~0. Supplied model, finite diagnostic; no rule is adopted. | `claude/toe-gk-smoothed-layers-20261021` `27d877dc41e3` |
| #9983 | The filtered quartic toy with a face-gapped band is symmetric and gapped at moderate coupling, and pairs at strong coupling | logged | For the supplied cube-filtered SU(4)-singlet quartic toy with a real face-gapped free band eps_k = t sum_i (1 - cos k_i)/2 (Fermi set = Gamma only; X, M, R at t, 2t, 3t), and its interpolation lam (on-site quartic) + (1 - lam) (cube-filtered quartic): the interaction expansion stays sign-free (weights det(M)^4, M real, for any real band and any real mix of vertex orbitals). Finite diagnostics at L = 4, 6 and beta = 4, 8 (live at beta = 4, recorded at beta = 8): at g/t = 1 and 2 the filtered model has no pair, flavour or translation order (S_pair/L^3 falls about as 1/L^3, xi/L falls) and keeps L-independent pair and zone-centre gaps; at g/t = 4 xi/L is flat (crossover); at g/t >= 8 the strong-coupling pair order of the toy QMC survives (xi/L rises with L, pair gap closing); the on-site model (lam = 1) is symmetric and gapped at g/t = 8; lam = 0.5 at g/t = 8 is borderline. The symmetric window sits on the weak side of the pair phase, next to a free point whose only gapless mode is a quadratic touching at Gamma, not a Dirac cone. The Binder ratio, L > 6 and the Spin(10) content are not computed. | `claude/toe-qmc-face-gapped-20261021` `6e45d558aeeb` |
| #9994 | The cube-filtered mirror term is momentum-selective, but the SU(4) toy's K mirror is anomalous | corrected or replaced in part by #10004; see corrections | SU(4) toy of the momentum-selective mirror requirement. Band (supplied): a real band with Weyl nodes only at K = 0 and R = pi(1,1,1), of opposite chirality (Karsten-Wilczek form composed with a unimodular momentum map, realified with complex structure J); light h, mirror -h, light-mirror pairing w prod sin^2(k_i/2) (1 at R, 0 at K); cube-filtered SU(4) quartic (rows 8^-1/2 sum over the cube, form factor 8 prod cos^2(k_i/2)) on the mirror only. Exact: the toy is sign-free (weights det(M)^4, M real); the light K modes and the whole R sector never enter the interaction, so at every coupling and every finite size the light gap at K is 0 and the light-mirror gap at R is the free paired value; the quartic keeps Z4_J x Z4_N x SU(4), which forbids every bilinear mass and pair at K; the K mirror is 8 Weyl of one Z4_J charge (Z16 index 8), so a symmetric trivially gapped K mirror is anomaly-forbidden in this toy. Finite diagnostics (sign-free CT-INT, L = 4 at beta = 8 for g/t = 0.25, 2, 4, 6; L = 4, 6 at beta = 4 for g/t = 2): the L = 4 K-mirror gap is O(g) already at g/t = 0.25 (finite-size zero-mode atom), so it is not a bulk gap; at g/t = 2 the gap falls 2.18 -> 1.53 from L = 4 to 6 with no pair or mass order; at L = 4 pair correlations grow steadily with g/t (xi/L 0.18 -> 0.42). No symmetric gapped window is established; at L <= 6 the K-mirror gap is inconclusive. Not Spin(10), not the CL-1 tick. | `claude/toe-momentum-selective-mirror-20261021` `d2a4f35a7dc8` |
| #10025 | A rung-separated mirror protects the light cone, but a rung-local mirror gap releases the fine partner | logged | Free two-rung model (a fine Z^3 rung and one coarse rung on 2^3 blocks), each rung carrying the same cone-rule band (Karsten-Wilczek type, nodes 0 (+1) and R = pi(1,1,1) (-1), coarse hop 1/2 so the cone speeds agree), coupled by a nested block reading. Exact: on one rung the mirror cone sits on the same rung (charges sum to zero; a random 0.05 change keeps both); nested block rows overlap by 2^(-3/2) per rung and weight a fine plane wave by prod cos^2(q/2) (uniform rows) or prod sin^2(q/2) (staggered rows). With the same rule on both rungs the uniform reading couples same-chirality cones (zeros remain, no pair removed); the staggered reading Dirac-pairs the fine R cone with the coarse zone-centre cone A (gap w, coupling matrix fixed by the SU(2) lift of the polar rotation between the cone frames; the identity leaves a nodal ring) and leaves the fine zone-centre cone exactly decoupled (H psi_L = 0, vertex ~ q1 q2 q3). The two remaining zeros are the light cone on the fine rung (coarse weight 0) and the mirror B near the coarse corner (coarse weight 0.879), opposite chirality. Light-B bilinears are forbidden by coarse crystal momentum for every coarse-translation-invariant term (2e-16), while light-fine-partner and light-A bilinears are allowed by that symmetry. A momentum-blind (rung-local) symmetric gap of the coarse rung releases the fine partner with weight D^2/(D^2+w^2) (0.500, 0.889, 0.985 at w/D = 1, 2^-1.5, 2^-3): overlap suppression makes the release more complete (ED SU(4) atom: partner gap/w = 0.186, 0.0071, 0.0003). Only a quartic on rung-2 staggered rows leaves A untouched at the node; that layout is the momentum-selective-mirror route one rung up. Free bands and one atom only; no interacting 3D phase, no Spin(10), no links. | `claude/toe-rung-separated-mirror-20261021` `050717f54b11` |
| #10028 | The cell's taste doublet is a geometric tetrahedral twist: a one-qubit chiral-turn-charge walk | logged | Free bands on CL-1's 2^3 cell (one fermion mode per site, face phase -1, Bloch over 2Z^3, 8 cell states) under the 12 tetrahedral rotations T kept by the copy mass. (A) CL-1's own Margolus tick is vector-like in turn charge: each chirality's taste E splits into w + wbar, T allows an L-R mass per character pair, the copy-mass light family has q_L = q_R and the T-invariant mass mu gaps it; the massless tick's exact internal symmetry algebra is dim 1 (not 8), so no twisted turn is a symmetry of it. (B) New exact member (composite TWIST): U(K) = f + i(h1 tau1 + h2 tau2 + tau3 g.sigma) with sigma = cell spin, tau = cell taste doublet, CL-1 chirality eta a spectator, and the atomic TWIST functions of the cell momentum. It is unitary, a pure nearest-cell hop, exactly T-covariant under the plain site permutations (the twist is the cell's own geometric taste action, nothing supplied), not O-covariant. Nodes exactly K = 0 (quasienergy 0) and the cell corner R (quasienergy pi), 8-fold each; Weyl chirality = tau3 at both; every L has q = 2, every R q = 1; no T-invariant on-cell L-R term exists; on-cell filter leak O(K^2). Light content 4 L + 4 R. Not covered: interactions, links, walks outside this Clifford form, a cube-local circuit decomposition. | `claude/toe-composite-twist-20261021` `1cafd93c56f3` |
| #10031 | On the FREEZE walk, the mirror-only charge-4 term first exists at four families and frees the light partners | logged | On rule FREEZE (twist-local-single), a cell-local, charge-4 interaction of the mirror-labelled modes (tau3 = -1 on Pi+) only. Exact: (A) no T-invariant such term exists for N_f = 2 or 3 families; the T-invariant count is C(N_f, 4), so the first one is at N_f = 4, where it is unique and forced to be SU(4)-family symmetric. (B) One-cell exact diagonalisation at N_f = 4: the term alone has a 2-fold cell ground state, A (mirror occupation 2 of 8) and B (6 of 8), whose turn charges differ. A supplied T-, SU(4)- and Z4-invariant mirror number bias selects A: a unique symmetric cell state with a single-particle gap. G_R(0) is then finite (no pole and no zero at the node). The light Weyls at the nodes are untouched (G_L^-1 = -h_LL to 4e-5 at \|K\| = 0.1). At X the light-labelled modes, which the free walk gaps only by mixing with the mirror, are freed: their lowest pole goes 1.23 -> 0.35 -> 0.21 -> 0.06 as g = 0, 1, 4, 16 (cell-gap units). (C) The light-labelled projection of FREEZE has 6 opposite-sign nodes at X and M per family; at N_f = 4 the gapped set carries Spin-Z4 index 8 mod 16 and SU(4)^3 index 2. Not covered: the infinite-lattice phase diagram, Floquet (rather than Floquet-Hamiltonian) interaction, N_f = 8. | `claude/toe-freeze-mirror-smg-20261021` `4e7d492ae1b9` |
| #10033 | Glide-keeping cube ticks carry an even number of light Weyl doublets per glide label | logged | Free one-mode-per-site CL-1-type cube ticks on the 2^3 cell, any range. Exact: (i) a tick keeps the one-site (1,1,1) glide G = A^-1 D T exactly when its odd half-step is the glide image of its even half-step, U = (DT) A (DT)^-1 A, and then U = T^2 G^-2. (ii) The glide label Lam = e^{-i th.1/2} G U^{1/2} is an involution commuting with U that is antiperiodic in the cell Bloch angle, so it is balanced in every gapped quasienergy window. (iii) At K = 0 and at the zone corner pi(1,1,1) the 12 tetrahedral rotations (indeed the three 2-fold ones alone) commute with Lam and act spinorially, so each label sector there is a sum of doublets. Theorem: if such a tick keeps the glide and the three 2-fold rotations and has no quasienergy-0 or -pi states except Weyl doublets at K = 0, the number of light Weyl doublets carrying each glide label is even. Hence no glide-keeping, cube-covariant deformation leaves exactly L(q=2, glide +) + R(q=2, glide -) light: every placement of the q = 1 copy doublets is excluded, and they can never be mass-paired (they stay T-doublets at K = 0 with opposite glide labels). Finite diagnostics: the natural glide-symmetric copy terms (copy inversion, glide Dirac mass, copy shift) and a 12-start search over copy unitaries on both tilings all leave extra quasienergy-0 or -pi states, as the theorem requires; AX-3 evades only by breaking the glide; keeping a single turn without the 2-fold rotations lifts the doublet constraint. Not covered: composite or multi-mode cells, coarser rungs, interactions, links. | `claude/toe-glide-band-20261021` `e558491e0cce` |
| #10035 | No tested band carries both the light turn charge and the momentum-separated mirror | logged | Free-band consistency check of two conditional results that use different bands. The family count (N = 0 mod 3) needs the light copy to carry a nonzero three-fold-turn charge q; the mirror separation needs light and mirror at different exact momentum labels so a filtered charge-4 term vanishes on the light cone. Exact: (A) the massless CL-1 cube tick has an exact one-site (1,1,1) glide G, and at K = 0 G equals the chirality operator, so all left tastes carry G = +1 and all right tastes G = -1 (a Karsten-Wilczek-like split by the glide label); a glide-symmetric number-conserving bilinear therefore has no L-R block at K = 0, and the copy mass on both tilings gaps nothing there. (B) The AX-3 copy mass (even cubes) breaks the glide for every site gauge; its light copy (1 L + 1 R Weyl) has q in {1,2} but both sit at cell momentum 0 with weight 1/4 on every fine corner, and a term keeping cell translations and all 12 kept rotations opens a light-mirror Dirac gap linearly. (C) The glide-symmetric massless tick separates (the range-one filter (1 - G)/2 is exactly 0 on the light states, 1 on the mirror, leak linear in k) but its light content is E with q = 1 and 2, total turn phase 1, so every N is allowed. (D) The Karsten-Wilczek-type band keeps no three-fold cube turn; for any on-site-spinor band with cones at K and R the turn acts on both cones by one on-site phase, which the charge-4 term fixes to +-1, so q = 0. No tested band does both jobs. A glide-symmetric band reached by moving the q = 1 tastes off K = 0 and annihilating them is not excluded and not constructed. Free bands only; no interactions, links or Spin(10) dynamics. | `claude/toe-one-band-check-20261021` `0ae41e980752` |
| #10043 | The two-qubit-site Dirac walk is vector-like; a tetrahedral twist gives a chiral turn charge but a pinned pi doubler | logged | Free bands on a supplied two-qubit site C^2 (flavor tau) (x) C^2 (spin sigma), Clifford walks U = f + i(h1 tau1 + h2 tau2) + i tau3 (x) g.sigma. (A) The landed O-covariant doubler-free member (coin 1 (x) D(R), b*) does not resolve the R10/R11 clash: every band is doubly degenerate, its single light node at k = 0 is a vector-like Dirac point (one L and one R Weyl at the same momentum), an O-invariant mass is allowed, and both chiralities carry turn charge q = 0. (B) New exact member: twisting the flavor qubit by the Z3 character of the tetrahedral group T, rho = diag(wbar, w), gives the nearest-neighbour unitary T-covariant walk f = sum c/3, h1 - i h2 = (sqrt2/3)(c1 + w c2 + wbar c3), g = s/sqrt3. The turn then acts chirally: every L Weyl has q = 2 and every R Weyl q = 1 (relabel by the conjugate twist), so mass at k = 0 is forbidden, but h vanishes on the body diagonals and a second pinned Dirac node sits at R = pi(1,1,1) at quasienergy pi with the same per-chirality charges. Light content 2 L + 2 R; no momentum separation of light from mirror; label separation by an on-site filter with O(k^2) leak. Not covered: walks outside the Clifford class, interactions, links, composite realisations. | `claude/toe-two-qubit-cell-20261021` `089bf3df49a8` |
| #10051 | The overlap chiral determinant in SU(2) x U(1) backgrounds cancels the family gauge anomaly through cubic order and in every measured index, but a single doublet does not | logged | The overlap D = 1 + V of the cube walk's Euclidean Wilson kernel (m0 = 1.6) in supplied SU(2) x U(1)_Y link backgrounds on small Z^4 tori (3^4, 4^3x3, 4^4), with Luscher's projector P_hat_- = (1 + sign H)/2. Exact (algebra, checked to rounding): GW, g5-hermiticity and D P_hat_- = P_+ D in non-abelian backgrounds; lattice pseudo-reality makes the Y = 0 doublet's SU(2) covariant anomaly tr(T^a g5 D(x,x)) vanish at every site, tr(T^a g5 D) odd and tr(g5 D) even in Y; the fixed-psi-bar-basis, parallel-transported Weyl determinant phase changes under a gauge rotation by -(1/2) sum_x omega(x) tr(T g5 D(x,x)). Consequence (exact charge algebra plus those parities): for the 16 per colour-summed family every term of order 2 and 3 in the background in the covariant anomaly cancels identically on the lattice (sum Y = sum Y^3 = sum_doublets Y = 0); order-4 coefficients (sum Y^5 = 5/9, sum_doublets Y^3 = -1/9) do not. Finite diagnostics: (a) one doublet's anomaly scales as eps^2 (exponents 1.97, 2.01), (b) the family's as eps^4 (4.02, 4.03); on 4^3x3 at eps = 0.1, (b)/(a) = 0.060 (U(1)_Y) and 0.0065 (SU(2)). Indices in 4^4 non-abelian backgrounds with abelian flux equal -sum f^2 for every flavour, including the (SU(2) x U(1))/Z2 half-flux background (Q, L, u, d, e, nu = -1, -5, -4, -1, -9, 0), and sum_f Y index = 0 exactly for the family but not for one doublet. Mod-2: one Q doublet has odd index; the family's doublets give -8. Not covered: a non-perturbative existence proof (open in the literature); the removability of the order-4 remainder by a local measure term; the pi_4 Witten anomaly itself; Q = 1 SU(2) instantons; continuum limits; SU(3). | `claude/toe-overlap-nonabelian-20261021` `50bde09de24d` |
| #10058 | The fewest-change symmetric far-wall term is forced and gaps the 3450 mirror in a wall-mode chain, while the flux pump separates anomalous content | logged | 1+1D proxy of the domain-wall tick's open step: a 2D Wilson slab (m = 1, four flavours) whose near wall carries the 3-4-5-0 content L(3,4) R(5,0) and whose far wall carries its mirror, with U(1)_A x U(1)_B charges (3,4,5,0), (2,1,2,-1). Exact: the neutral occupation-change lattice is Z l1 + Z l2 with l1 = (1,-2,1,2), l2 = (2,1,-2,1); it is K-null (a gapping lattice); its fewest-change elements are exactly +-l1, +-l2 (six fermion operators), which need one nearest-neighbour bond; both coupling phases rotate away and a free-wall symmetry swaps the two terms, so one coupling g is forced. The bulk Chern number is 1 per flavour, so a flux quantum pumps s_f q_f particles per flavour onto the far wall; for 3450 both pumps lie in the neutral lattice, for 3451 the pump carries Q51 = -1, and no symmetric gapping set exists. Finite diagnostics on the far-wall chain (wall modes \|k\| < pi/2, bulk dropped, antiperiodic L = 8, 12): at L = 12, g = 200 a unique neutral P = 0 ground state, neutral gap 4.03 and single-particle gap 4.84 (free 0.52, 0.26), flat lowest branch; a level crossing near g = 40; L = 8 is mode-capped (quasi-doublet), so no finite-size trend is extracted. The near-wall flavour-3 level moves by 4e-5, 3e-7, 1e-9 at Ls = 2, 3, 4 (scaling as its own leak squared). The same chain also gaps 3451 with its fewest-change symmetric terms, so the chain regulator cannot see the anomaly; the flux pump separates the two. Not covered: a local (bulk-included) interacting computation, sizes beyond L = 14, 3+1D, gauging. | `claude/toe-far-wall-smg-20261021` `e9ba2aa82b75` |
| #10061 | The Spin(10) pair square on two 16s is a Spin(12) Casimir with a unique singlet ground state and gap 4 g, but a frozen far region still moves the mirror | logged | One site with two 16s of Spin(10) (32 complex modes c_{i alpha}, i = 1,2, Fock 2^32). With B_a = c_1^T M_a c_2 (M_a = (C Gamma^a)\|_16, symmetric), the operators {T_ab, B_a, B_a^+, J = (N-16)/2} close into so(12) (66 generators, exact), the flavour SU(2) commutes with them, and sum_a {B_a, B_a^+} = 2 [144 - 2 S(S+1) - C2_10 - J^2] exactly (checked on the N <= 2 sectors, which is complete for number-conserving degree-4 operators). So C2(so12) = 144 - 2 S(S+1), and H_sym = -(g/2) sum_a {B_a, B_a^+} = -g F with F = 144 - 2S(S+1) - C2_10 - J^2. Ground state: unique at -144 g, N = 16, Spin(10) singlet, flavour singlet, particle-hole even. Gap 4 g, to the Spin(10)-singlet flavour-singlet states at N = 16 +- 4. Pair level B^+\|GS> at 10 g, fermion level c^+\|GS> at 13 g (exact eigenstates). Within fixed N = 16 the gap is >= 16 g. The naive ordering -g sum B B^+ = H_sym + 5 g (N - 16) has a two-fold charged ground state (N = 4, 8) at -168 g, so the particle-hole symmetric ordering (or a tuned chemical potential) is required. The two flavours enter only through the epsilon pair: for the two spin components of one Weyl 16 this is the Lorentz-scalar 10 bilinear. Contrasts: 16 x 16bar contains no 10 (the channel vanishes; a quadratic Dirac pairing is allowed, vector-like); 15 + 15 (no nu^c) has no unique particle-hole symmetric level (exact). Reduced Spin(6) analogue (2^8, full diagonalisation): identity exact, unique GS, gap 4 g, fermion gap 5 g. Slab (free model): a two-layer far region holds > 0.99 of the wall mode at k <= pi/8, yet freezing r = 1..4 far layers into a gapped product moves the branch r layers in with E = sin k unchanged. Not covered: inter-site hopping at finite g, the interacting slab, gauge fields, the continuum limit. | `claude/toe-spin10-two-flavour-20261021` `bb1c64a23dcc` |
| #10063 | The cell slab cannot put its mirror in the other copy: turn-axis eigenvalue flow forces q_mirror = q_light on any static slab | logged | Free-field cell slab on CL-1's 2x2x2 cell (layer hop (B/2 + i eps)/2, copy mass (1 - s) R_e, Mc = 1, Ls = 32 or 40). (T1) At K = 0 the copy sign s commutes with every cell-built layer term, each copy is its own Shamir chain (r_+ = 1 - m, r_- = 1 + Mc - m), and the far boundary can hold copy s only with the hand opposite to that copy's near-wall hand: s+ with -1 or s- with +1, never s- with -1. (a) A layer mass stepping (sharp or tanh) from the (0, Mc) window [s+, q 2] to the (2, 2 + Mc) window [s-, q 1] puts s- (q 1) on the far wall with the light's hand +1, and both mirrors s+ (-1, q 2) and s- (-1, q 1) on the interior interface; it crosses the bulk gap closings m = Mc and m = 2 and is a chosen profile. (b) A hop s A keeps the wall content; a turn-commuting copy-flipping hop has rank <= 4 < 8, so no turn-covariant copy flip exists. (T2) On any static (Hamiltonian) turn-symmetric slab whose only E = 0 crossings on the turn axis are the K = 0 wall Weyls, the turn-sector eigenvalue flow forces q_mirror = q_light for every N_f. The families-mod-3 mod 3 is therefore not recovered on any realised slab. Not covered: interactions, gauge fields, Floquet (circuit) slabs, slabs with extra axis crossings, multi-Weyl nodes. | `claude/toe-copy-flip-slab-20261021` `eaf7c9495f86` |
| #10065 | No principle tested forces a nonzero turn-graded tick winding: chiral walls exist at zero winding, time reversal forbids the family class, and fewest changes selects zero | logged | Free-field Floquet ticks on CL-1's 2x2x2 cell on the (111) turn axis, with the site-gauged turn T3 as a symmetry; FREEZE, CTWIST and the F/F^+ slab (g = 0.5) rebuilt from twist-local-single / floquet-pi-slab / slab-parity. (0) Every copy-flip winding W = f(q_l,+) + f(q_m,-), q_m != q_l, has all three Z3 components nonzero. (a) A W = 0 slab (Ls = 6) has a one-handed light q 2 on one wall and its mirror on the other; gappable-mirror bookkeeping holds for every N_f at W = 0. (b) Lemma: a Floquet antiunitary T, a unitary chiral symmetry, or an axis-reversing unitary that normalises the turn group forces a zero component of W, so each forbids the family class; CL-1's tick has all three (and the C2' of its 24 rotations), FREEZE has no on-cell one; FREEZE plus its T partner has W = 0; a T-less turn-commuting circuit has W = 0. (c) W(CTWIST) = W(U_A) = 2 W_F, and FREEZE halves it; a fewest-changes cost (leave-site / leave-cell probability per tick) is 0 at the identity, -> 0 for CL-1's tick as eps -> 0, O(1) for every W != 0 tick tested, and invariant under U -> U^+ while W flips. (d) W is additive; the W = 0 class holds the identity and every turn-commuting circuit. Not covered: interactions, gauge fields, the copy-mass factor, K-dependent intertwiners in the numerical search (the lemma covers them), principles not listed. | `claude/toe-tick-winding-origin-20261021` `aac864716c98` |
| #10070 | The family-class tick's pi partners are same-hand spacetime doublers, not CPT mirrors, so the mirror cannot be carried in time | logged | Free light bands of FREEZE (twist-local-single; family-class tick W_F = (-2,1,1)) on CL-1's 2x2x2 cell, CL-1's plain cube tick (eps 0.3) as control, and the one-cube start tick (8 modes, Fock 256). Exact: (1) the kept CPT-type map (U(K) -> U(-K)^+) fixes K = 0, R and quasi-energies 0, pi, so it maps each node into itself; at K = 0 it sends the light q 2 pair onto the q 1 pair. (2) FREEZE has an on-cell spacetime-doubler map S U(K) S^-1 = -U(K + R); the pi partner at R is the light Weyl's doubler with the same hand, turn label, speed and on-cell charges (the commutant is scalar on Pi+). CL-1's plain tick has none. (3) Hand sum rule: net hand at quasi-energy 0 = net hand at pi = nu3, and nu3 = 0 for every circuit of cube-local gates (homotopy). So a mirror at pi alone is impossible for any charges, and the pi gap repeats the 0 gap. (4) Any half-filled vacuum that fills quasi-energy intervals and has no Fermi surface has boundaries at 0 and pi, and exactly one of the two sectors is inverted; no bilinear pairs a light Weyl with its pi partner; the anomaly coefficients of the two sectors are equal. (5) On the one-cube start, an antiunitary time reflection (a signed site permutation) fixes the half-filled vacuum, so a reflection-invariant start state has mirror-symmetric Born record odds. Register readings of the Boyle-Finn-Turok predictions are given as supplied-literature consistency checks. Not covered: interactions, the slab with links, the copy mass on FREEZE, inverted-sector decay rates, cosmological dynamics. | `claude/toe-mirror-in-time-20261021` `9a5bd14fd969` |
| #10074 | Far-termination winding keeps a pi-free, screening near wall, but the end is a chosen boundary bit and the far wall must gap all three families together | logged | Candidate clause (pi-repair A4 reading): CL-1's bulk tick has W = 0; the slab's far termination layer carries a family-class turn-graded winding. Supplied models: pi-repair's sector-resolved class-A toy (QWZ Floquet strip per turn sector + a chiral-shift layer standing in for the FREEZE layer) and a T-symmetric 3D Wilson domain-wall slab (m0 = 0.6, T = i sigma_y K). (G) Both end placements are valid slabs with the same bulk and total winding; U -> U^+ keeps the layer's end; given light q 2 and one far mirror Weyl the family-class W is one of two values: the clause carries ~3 bits of boundary information, none forced by an adopted rule. (N) Near wall: (F_0, F_pi) = (f(2,+), 0) over g and Lx; no layer-preserving doubler map can exist (exact lemma), and the near wall screens (induced charge 0.42) while an exactly S-doubled control gives 1e-12; a far-layer T-odd tetrahedral-covariant term leaks a reciprocity-odd dim-5 near-wall term falling as (1 - m0)^2 per layer (0.168 measured). (C) T kept by the bulk acts with X = 1 on copies: J = 0. (F) Far wall per family (q1,-), (q2,+), (q1,-) x 16: gauge and mod-16 anomalies vanish, the turn Z3 cubic is 6 mod 9 for k = 0 (nonzero for every twist), and vanishes for N_f = 0 mod 3 (supplied index form). Not covered: the slab on CL-1's 8-mode cell with a real FREEZE layer, the far-wall symmetric gapping itself, interactions, gauge fields. | `claude/toe-far-termination-winding-20261021` `3428d9458967` |
| #10076 | The 3450 far-wall term keeps a unique gapped wall-mode-chain state to L = 18, but its gap falls from six to eight modes per flavour | logged | Finite diagnostics on exactly the far-wall-smg wall-mode chain (far-wall modes \|k\| < pi/2, antiperiodic, the two forced 6-fermion bond terms l1 = (1,-2,1,2), l2 = (2,1,-2,1), one coupling g, sectors (Q_A, Q_B, P)) at L = 8, 10, 12, 14, 16, 18, i.e. n = 4, 4, 6, 6, 8, 8 modes per flavour; L = 16, 18 sectors have 2.1-2.3e6 states and were computed by sparse Lanczos on a separate machine (results committed as data). At g = 200 the ground state is unique, neutral and at P = 0 for every L = 12..18; the neutral gap is 4.03, 3.36, 1.60, 1.44 and the single-particle gap 4.84, 4.31, 1.54, 1.42 (free 2 sin(pi/L), sin(pi/L)). Within fixed n the gap tracks 1/L (gap*L = 48.4, 47.0 at n = 6; 25.6, 26.0 at n = 8); at equal window fraction n/L it falls by 0.40 (12 -> 16) and 0.43 (14 -> 18); at g = 1000 by 0.32 (12 -> 16). A fit gap = D_inf + c/L gives D_inf = -4.4 with residual 0.42, so the data do not support a finite large-L gap of that form; this is a trend over two mode numbers, not a limit. g = 5 is free-like (gap = 2 sin(pi/L) to 0.1%); g = 40 sits in the small-gap crossing region (0.06-0.11). Pre-set classification: INCONCLUSIVE (persistence ratio 0.36 < 0.5; closing criterion not met). Not covered: n = 10 (L = 20, 3.5e8 states per sector), the slab with the bulk, a mode-number-breaking far-wall term, 3+1D. | `claude/toe-far-wall-L16-20261021` `3eba0b274462` |
| #10078 | The Cayley completion of the charge-4 term halves the gapping coupling of the 8-Majorana proxy chain, but both forms persist at strong coupling | logged | (1) Exact on-site: on 8 Majoranas (4 complex modes) the 4-form Re Omega has so(8) stabiliser 15 (SU(4)) and operator spectrum -8 (1), 0 (14), +8 (1); (1/2) omega^omega has stabiliser 16 (U(4)) and spectrum -6 (2), 0 (8), +2 (6); their sum, the Cayley form, has stabiliser 21 (Spin(7)) and spectrum -14 (1), 0 (8, odd), +2 (7, even). The Cayley ground state is the Re Omega ground state, annihilated by all 21 commuting bilinears. (2) Finite diagnostics on a supplied 1+1D proxy: L sites with 4 complex modes each, SO(8)-invariant Majorana hopping (8 left + 8 right Majoranas), on-site g Phi^, flavour-twisted boundary (an SU(4) element), all momenta and the relative-charge sectors that can be lowest, L = 4..8 (L = 8 complete only for g <= 0.25). At g = 0.25 the Cayley gap is 2.719, 2.679, 2.702, 2.701, 2.702 (L = 4..8, OPEN) while Re Omega alone gives 1.130, 0.314, 0.917, 0.528, 0.824 (INCONCLUSIVE). At g = 0.5 and 1.0 both are OPEN and flat to 1%. At g = 0.125 Re Omega is free-like (Delta(8)/Delta(4) = 0.523 vs 0.510 free) and Cayley is not OPEN. At matched on-site gap (Re Omega at 0.5, Cayley at 0.25) both are OPEN. Pre-set outcome: PASS (Cayley advantage at g = 0.25), read as a lower gapping coupling, about a factor 2 consistent with the 7/4 on-site gap ratio, not a qualitative persistence difference. Not covered: the 3+1D 16, the slab with bulk and light wall, gauge fields, L > 8, a coupling scan finer than the grid. | `claude/toe-cayley-mirror-gap-20261021` `d2b189516809` |
| #10083 | The one-family U(1) anomaly passes Luscher's zero-momentum tests on lattices to 24, but its momentum-space locality test is scale-limited at m0 = 1.6 | logged | U(1)_Y covariant anomaly density of the Wilson-kernel overlap (r = 1) for the one-family 16 and a lone L doublet, in axis-restricted factorised backgrounds (U2 = exp(i th2(x1)), U4 = exp(i th4(x3))), on L x T x L x T lattices with L = 6..24 along x1, x3 and T = 24 (16 for L = 24) along x2, x4; exact block sign(H). Exact: block method = full 4D (6e-15), GW per block. Integers (6^4, full dense): indices -(6Y)^2 for 6Y = 1..6, all resolved; the 16's flux integral is 0 from measured integers; lone doublet -18. Finite diagnostics: isotropic small tori are Polyakov-loop dominated for the 16 (holonomy shift flips its sign); at m0 = 1.6 the per-charge kernel and the 16's single-mode coefficient carry a slow scale (finite-size rate ~0.3/site) and the pre-set momentum-space locality criteria P1, P2, P4, P4b, P5 are NOT met at L <= 24 (P3 partly, P6, P7 met); post-hoc at m0 = 1.0 the 16's coefficient is -9e-7 at \|p\| = 0.39 (7e-5 \|gamma_L\|) and falls faster than p^2 while the doublet tends to gamma_L. Not covered: the measure construction, non-abelian locality, the gauge-field integral, general (non-axis) backgrounds, momenta below \|p\| = 0.26. | `claude/toe-luscher-L8-20261021` `eacbca9d6149` |
| #10084 | The one-family U(1) anomaly at Wilson mass 1 passes Luscher's kernel locality tests, but its small-momentum four-field coefficient does not visibly vanish | logged | Pre-registered rerun at Wilson mass m0 = 1.0 (control m0 = 0.6) of the momentum-space Luscher locality test for the U(1)_Y covariant anomaly density of the Wilson-kernel overlap (r = 1): the one-family 16 and a lone L doublet, axis-restricted factorised backgrounds, L x T x L x T lattices with L = 6..24 along x1, x3 and T = 24 (16 for L = 24) along x2, x4, exact block sign(H). Exact: block = full 4D density on 4^4 (7e-15); GW per block. Finite diagnostics, pre-set criteria: per-charge order-2 kernel and its Luscher-split currents exponentially local with an L-independent length (xi 0.49-0.53; K1 0.53/0.57), zero-momentum value within 0.5% for L >= 10, doublet keeps a non-decaying current tail = \|gamma_L\| (within 10% on all L, 2% only for L >= 10) and its single-mode intercept 0.990 gamma_L. NOT met: the 16's single-mode coefficient criteria P5, P5', P5b and the T = 16 volume check; R16 is at most 1e-4 \|gamma_L\| for s <= 0.07 but changes sign, and the post-hoc two-eps split shows the leading (density order eps^4) coefficient c4 = 1.3-1.4e-4 at s = 0.038 and 0.017, flat rather than tending to zero. Control m0 = 0.6: the pre-set slow-scale reading min(m0, 2 - m0) is NOT met. Not covered: the measure, non-abelian locality, the gauge-field integral, non-axis backgrounds, momenta below \|p_hat\| = 0.26, T-convergence of the L = 24 points. | `claude/toe-luscher-m0-1-20261021` `60313b314a62` |

## Links in the carried notes to sources not carried

The carried notes are byte-identical, so three of them link to source notes that this consolidation records but does not carry. Those links resolve only on the source branches, at these commits:

- #9980: `docs/FAR_LAYERS_READING_A_SMOOTHED_FIELD_DECOUPLE_THE_MIRROR_FROM_FIELD_STRENGTH_BUT_NOT_FROM_GAUGE_TURNS_TOPOLOGY_OR_LONG_WAVELENGTHS_BOUNDED_THEOREM_NOTE_2026-10-22.md` at `27d877dc41e353268ce36cf4fe634916d8ba6f0d`
- #9983: `docs/THE_FILTERED_QUARTIC_TOY_WITH_A_FACE_GAPPED_BAND_IS_SYMMETRIC_AND_GAPPED_AT_MODERATE_COUPLING_AND_PAIRS_AT_STRONG_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-22.md` at `6e45d558aeeb640e4d8e9e9694a895afb18a1f15`
- #9994: `docs/THE_CUBE_FILTERED_MIRROR_TERM_IS_MOMENTUM_SELECTIVE_BUT_THE_SU4_TOY_K_MIRROR_IS_ANOMALOUS_BOUNDED_THEOREM_NOTE_2026-10-22.md` at `d2a4f35a7dc8dffe8fe5926104be2a50d3510709`
