# PRIOR_ART — Step 0 for the chirality / doubling wall on Z³

**Exercise:** a chiral fermion spectrum (SM chiral gauge content, no light mirror or doubler partners) on the framework's qubit lattice Z³.
**Mapper:** Claude Opus 5.5 (supervisor-run Step-0 mapper), 2026-10-14 12:58–13:25Z. Four read-only sub-readers, all Opus 5.5 at xhigh, so the same model family as the supervisor; they are not independent. Their raw maps are beside this file: `cluster_A_record_side.md`, `cluster_B_walks_weyl_domainwall.md`, `cluster_C_anomaly_generation.md`, `cluster_D_meta.md`. Every row I relied on for the wall statement and the open gates I re-read myself at the cited lines.
**Refresher surfaces read:** `docs/MINIMAL_AXIOMS_2026-06-29.md` (in full); `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`; `docs/audit/data/axiom_premise_nodes.json` (four nodes: minimal_axioms, scale_reference, kinetic_isotropy, realized_state; none touches chirality); `docs/audit/data/derivation_obligations.json` (three AC/theta obligations; none is about chirality or doubling); `docs/repo/DEFERRED_DECISIONS.md` (entries 2, 4, 5).
**Ledger note:** every main-branch row cited below has `audit_status = unaudited` in `docs/audit/data/ledger/` (checked for the 24 central rows). The status column gives the status *the note claims for itself*, not an audit grade.
**Labels:** [proved] = exact proof or exhaustive finite certificate in the note; [bounded] = bounded theorem on supplied objects; [conditional] = conditional on named premises; [no-go] = note's own negative claim; [open]; [retired/withdrawn]; [reading] = interpretation. "(branch)" = not on main.

---

## 1. Where the framework stands (plain summary)

The repo has met the doubling wall from every side it has tried and has not got past it. On the framework's own free carriers the count is always balanced. The two-component walker `H = Σ σ_a sin k_a` on the site qubit has eight Weyl nodes, four of each hand. One staggered field (one fermion mode per site) is two four-component Dirac "tastes", vector-like. Nothing covariant inside M₂(C) gaps a single corner. The staggered sign ε(x) labels the hands but does not unbalance them. A September proof extends the no-go to *ticking* (discrete-time, quantum-walk) dynamics: every finite-range free tick has zero 3D winding, and a one-handed tick needs infinite-range (exponential) tails and cannot come from any Hamiltonian flow. That note is unlanded, on a closed PR. Every escape tried so far has failed in a recorded way:
- domain walls in the staggered mass are vector-like in 3D;
- record-time and slab walls carry an opposite partner;
- vortex strings carry handedness only locally;
- the Spin(10) symmetric-gapping slab returns eight doublers in its strong-coupling limit;
- ultralocal Ginsparg–Wilson operators are excluded in the hypercube-range class;
- record-side handedness registers texture or direction, not fermion chirality.

The repo's own current position, in `THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE.md`, is that chirality is "not claimed on the purely spatial surface". It "enters only" through anomaly-forced time and a supplied one-generation completion, and the package "is not claiming a loophole in the usual no-go theorem". The live untested routes are:
- symmetric mass generation of a 16-Weyl mirror sector at finite coupling, in continuous time;
- overlap/Lüscher-type exponentially-local chiral measures;
- an extra dimension;
- the parked M₂(C)→M₄(C) enlargement;
- tails-ticks.

None has a first test run on this framework's lattice. TW-1/2/3 were registered at 12:58Z today and have not been run.

---

## 2. Table

Grouped by object. "Status" is the note's own claim type; "(branch)" means not on main.

### 2a. Foundations, the open gate, and what "chirality" means here

| Object | Note / path:line | Status | What it shows | What it does NOT show |
|---|---|---|---|---|
| Open gate AX:178 | `docs/MINIMAL_AXIOMS_2026-06-29.md:173-178` | axiom memo | Lists "the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`" as an open gate outside the axioms. Also :111: "No admission class exists". | Any chirality content. The axioms name no species count, no time direction and no dynamics (:114-130). |
| One-site γ5 | `docs/NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md:55-65, :140-143` | no-go [proved] | `σ1σ2σ3 = iI` is central, so no nonzero element of M₂(C) anticommutes with all three Paulis. There is no per-site chirality projector. | Multi-site, temporal, larger-Clifford or gauge chirality are explicitly out of scope (C2, :140-147). 1201 ledger descendants. |
| Clifford parity | `docs/CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md:5-23, :57-75` | bounded [proved] | γ5 exists iff the total Clifford dimension n is even. With d_s = 3, chirality needs an odd number of time directions (d_t = 1 is allowed). | That a time Clifford direction is supplied; it is a conditional parity count only. |
| Staggered-Dirac gate | `docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md:9-22, :88-116, :193-200, :341-390` | bounded_theorem (was open_gate) | Grassmann one-mode-per-site, KS phases unique as a Z₂ gauge class, 8 corners split 1+3+3+1 by Hamming weight, and an hw=1 triplet algebra M₃(C). The generation *labelling* is a no-go plus convention. | **Nothing about chirality.** The word appears nowhere in the gate's claims. Open residuals are the P-FLUX kinetic selector, spin-statistics support, the boundary-holonomy convention and AC_φλ labelling (:346-387). 974 descendants. |
| Earlier staggered-Dirac exercise | `docs/STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md:29-53, :76-93` (packet `.claude/science/exercises/staggered-dirac-gate/` is not on main) | bounded | Three hidden admissions beyond AC_φλ: fermionic statistics (a hard-core boson also has dim 2), a signature/time import inside `d−δ`, and the chirality field ε(x). Route rank 1 is the ε selector. Cites Nielsen–Ninomiya, Becher–Joos, Catterall. | Any chiral spectrum. |
| ε selector enumerator | `docs/STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR_NARROW_THEOREM_NOTE_2026-06-06.md:34-53, :57-65, :73-79` | bounded [proved, finite] | ε is a **free selector** on the bare surface, with two inequivalent classes (vector-like γ5 = ±I, or staggered). It is forced up to global sign iff `{D,γ5}=0` is required. "SM matter is chiral, so physics needs ε; but that need is the admission". | That `{D,γ5}=0` is derived. Calls this "the exact massless U(1)_ε" (:32); see Tension T3. |
| ε parity bridge | `docs/STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md:45-87, :115-126` | bounded [proved] | The edge-flip sign field is unique: `s(x) = s(0)(−1)^{Σx}`. It anticommutes with every nearest-neighbour odd stencil. | Statistics, the kinetic operator, species labels, and any chiral (unbalanced) spectrum. 797 descendants. |
| Chiral spectral pairing | `docs/STAGGERED_CHIRAL_SYMMETRY_SPECTRUM_THEOREM_NOTE_2026-05-02.md:46-67, :160-165` | positive_theorem [proved] | From `{C, H}=0`: σ(H) = −σ(H), with a C-graded zero-mode subspace (4³: 8 zero modes). | Species counting, index theory, interactions (:160-165). It is a pairing theorem, i.e. the doubling *mechanism*, not an escape. |
| ε vs ω vs Vandermonde | `docs/CHIRAL_CONTENT_IS_THE_EPSILON_D_CHIRALITY_IMPORT_DISTINCT_FROM_ORIENTATION_NARROW_THEOREM_NOTE_2026-06-08.md:16-26, :39-42` | bounded | The staggered ε, the qubit pseudoscalar ω and the generation handedness are three distinct objects. "The grading supplies a grading, not a chiral-gauging selection" (:41-42). | Any chiral gauging. |
| Two chirality gates | `docs/CHIRALITY_GATE_IS_TWO_INDEPENDENT_GATES_DIRAC_VS_GENERATION_SCOPING_NOTE_2026-06-08.md:12-19, :65-69` | bounded | Dirac/spinor γ5 (`I₃⊗σ₃`) and Koide/generation chirality (`{M_gen,Γ_χ}=0`) are independent. | The June "chirality gate" family is mostly the **Koide generation** sense, not gauge chirality (Tension T1). |
| Carrier attachment | `docs/CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md:11-19, :50-69, :128-139` | no-go | Operator-frame data do not force the j=½ state law (the trivial scalar lift survives). The spinful selector must come from the staggered/KS route, `{ε,D}=0`. | It does not discharge the chirality import (:130-132). |
| Dirac/Weyl DOF bridge | `docs/DIRAC_WEYL_FERMION_DOF_FROM_LORENTZ_AND_CHIRALITY_ADMISSION_BRIDGE_NOTE_2026-05-28.md:1-66, :400-460` | bounded | Weyl = 2 and Dirac = 4 DOF counting for thermal use. | The Dirac equation, chirality, Wick rotation. |
| Separate-factor Dirac | `docs/CHIRALITY_SEPARATE_FACTOR_DIRAC_MASS_ALGEBRA_SUPPORT_BOUNDED_NOTE_2026-06-08.md` (top) | bounded | A separate L/R factor gives a standard massive-Dirac algebra. | Derivation of that factor. |
| Frame-free chiral grading | `docs/CL3_FRAME_FREE_AMBIENT_CHIRAL_GRADING_NO_GO_NOTE_2026-06-02.md:1-10` | no-go | No frame-free Spin(3)-equivariant operation anticommutes with the Koide `Γ_χ`. | It is about the generation sense only. |

### 2b. Doubling on the framework's free carriers

| Object | Note / path:line | Status | What it shows | What it does NOT show |
|---|---|---|---|---|
| Naive 2^d count | `docs/NAIVE_LATTICE_FERMION_TWO_POWER_D_SPECIES_COUNT_NARROW_THEOREM_NOTE_2026-05-10.md:30-35` | narrow [proved] | The zeros sit exactly at {0,π}^d. | Which regulator the framework uses. |
| Species count is regulator-dependent | `docs/HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md:8-26` | no-go | Wilson gives 1, twisted 2, staggered 4, domain wall 1, overlap 1. | Which one the substrate is. |
| Walker: 8 species, 4+4 | `docs/ADMISSIBILITY_RULE_EIGHT_SPECIES_OF_THE_WALK_…_2026-09-21.md:30` (block 68); `…THE_EIGHT_SPECIES_ARE_EXCHANGED_BY_SITE_SIGNS…:34` (block 70) | bounded-support | `H = Σσ_a sin k_a` on the site qubit has 8 Weyl nodes with chirality (−1)^{#π}: four of each hand. | Species selection (:78). |
| Scalar hop: 1:3:3:1, one sense per level | `docs/ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_OF_ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md:33, :44-54` (block 77) | bounded-support | The Wilson-like scalar hop splits the corners into levels 1:3:3:1. Each level has one hand, and the hands alternate, so **the hw=1 triplet is single-handed** for this walker. mε gaps by pairing k with k+π(1,1,1), i.e. opposite hands. | A gap from the hop alone. ε is not forced by rotations alone (:54). |
| What can gap the walk | `docs/ADMISSIBILITY_RULE_WHAT_CAN_GAP_THE_WALK_NO_INVARIANT_TERM_AT_ANY_REACH_CHESSBOARD_OR_AXIS_STRIPES_ON_SITES_ALTERNATING_LENGTHS_GIVE_ONE_REST_ENERGY_EXCLUSION_CAGES_BOUNDED_THEOREM_NOTE_2026-09-22.md:27-42` (block 82) | bounded-support | Corner stabilisers make every covariant symbol scalar at a corner. Anticommuting site fields are only `c0·ε + Σc_j(−1)^{x_j}σ_j`. | A complete classification (:4). |
| Species symmetry forces only doubling | `docs/ADMISSIBILITY_RULE_THE_SPECIES_SYMMETRY_FORCES_ONLY_DOUBLING_…_2026-09-24.md:31-36, :119, :151` (block 119) | bounded-support (Grok-refereed) | Only even multiplicity is forced. Every positive rate field keeps exactly 16 zero modes. | Twist fields, other sizes, infinite volume. |
| Only the staggered mass keeps the books | `…THE_BOOKS_ADMIT_ONE_REST_ENERGY…:42-47` (block 139) | bounded-support | Of {1, ε, σ_a, εσ_a}, only mε keeps the conservation laws. | — |
| Taste census | `docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:152-167, :243-251, :267` | bounded (corrected 09-08) | Coarse 2Z³ KS: 8 = spin 2 × chirality 2 × flavour 2, i.e. **N_f = 2 Dirac, vector-like**, "as Nielsen-Ninomiya requires". "No generations from tastes" (:248). "The chiral sector. Absent … a lane wanting chiral matter must break the pairing, and nothing here says how" (:267). | Fine-lattice (4,2,2) anisotropy; interactions; mass. |
| **Handedness no-go incl. ticks** | (branch `origin/claude/toe-viability-probes-20260927`, PR #9363 closed unmerged) `docs/LATTICE_HANDEDNESS_A_FINITE_RANGE_FREE_WALKER_IS_LEFT_RIGHT_BALANCED_…_2026-09-27.md:100-160, :203-281, :299-357` | bounded [T1, T2 proved]; sol referee: "stands with corrections mathematically; fails as an exhaustive framework claim" (cluster D) | **T1:** Hamiltonian two-band, chirality sum 0 (a degree argument). **T2:** every finite-range unitary tick, any N, has W3 = 0 (SK₁ of the Laurent ring is 0). For N=2 with det U constant, nodes balance at 0 and at π. **T3:** S_xS_yS_z has 16 nodes, 8+8. **T4:** a one-handed tick exists with exponential tails (W3 = 4), is not the Floquet operator of any Hamiltonian flow and not a positive transfer matrix, and has a time-doubler and heating cost. | Interacting or gauge-coupled walkers. Node balance for N > 2 bands is cited, not proved (:303-306). Many-body QCA. |
| Mixed Weyl quartet | `docs/LOCAL_HALL_FREE_MIXED_WEYL_QUARTET_AND_COMMON_METRIC_BOUNDED_THEOREM_NOTE_2026-09-13.md:400-407` | bounded | Net Weyl charge on the torus is 0 (Stokes). With T² = +1, at least 4 nodes. | A supplied carrier. |
| BCC Weyl walk on Z³ | `docs/work_history/repo/review_feedback/CUBIC_QUBIT_RELATIVISTIC_REDUCTION_CYCLE7_NOTE_2026-07-14.md:18-50, :319-345`; `archive/…/ISOTROPIC_WEYL_QCA_LATTICE_COMPATIBILITY_NOTE_2026-07-14.md:31-44, :101-103`; `archive/…/WEYL_PAIR_PHYSICAL_EQUIVALENCE_…_2026-07-14.md` | meta, no authority | The D'Ariano–Perinotti BCC Weyl QCA factors into three NN conditional shifts on Z³. The A⁺ and A⁻ walks differ by the character `(−i)^{x+y+z}`. | Its node count is completed by LATTICE_HANDEDNESS T3: 16 nodes, balanced. |
| Kitaev composite-site network | `docs/THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_…_2026-09-24.md`; `docs/COMPOSITE_SITE_NETWORK_FLUX_FREE_SLAB_SURFACE_ZERO_MODES_FORM_ARCS_BETWEEN_PROJECTED_TOUCHINGS_OF_OPPOSITE_CHARGE_…_2026-10-01.md:1-6`; `docs/DYNAMICS_CLAUSE_RECORDS_CARVE_EXACTLY_SOLVABLE_THREE_DIMENSIONAL_KITAEV_NETWORKS_…_2026-09-24.md` | bounded (supplied comparator) | Emergent Majorana fermions from qubits in a Z₂ gauge field. With the odd term κ, Weyl touchings come in opposite-charge pairs, with Fermi arcs. | Chirality escape: none is claimed; balance holds. This is the "emergent fermions from qubits" lane (my reading). |

### 2c. Escape attempts on record

| Object | Note / path:line | Status | What it shows | What it does NOT show |
|---|---|---|---|---|
| Domain-wall chiral edge (Kaplan, record-time wall) | `archive/notes/docs/DOMAIN_WALL_CHIRAL_EDGE_FROM_ACHIRAL_CL3_BULK_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-04.md:40-49, :65-68, :121-133` | bounded (archived) | An imposed record-time mass wall puts one Weyl on the wall and the opposite one on the anti-wall. Wilson lifts 7 corners by breaking `{γ5,D}=0`. | Gauge, anomaly, a dynamical wall; the embedding and regulator are supplied. |
| Edge content vs SM | `archive/notes/docs/DOMAIN_WALL_EDGE_CONTENT_VS_SM_CHIRAL_FERMIONS_MAP_BOUNDED_THEOREM_NOTE_2026-07-05.md:156-179, :203-205, :274-278, :323` | bounded map | The 6+2 hypercharge surface matches Q_L + L_L. u^c, d^c, e^c are missing. ΣY³ = −2/9. Edge ⊗ taste = 16 ≠ 15. | Any SM derivation; the edge-to-taste bridge is a named gap. |
| Anomaly inflow / record front as wall | `archive/notes/docs/DOMAIN_WALL_EDGE_ANOMALY_INFLOW_SPECTRAL_FLOW_…_2026-07-05.md:5-12`; `archive/notes/docs/RECORD_FORMATION_FRONT_IS_THE_DOMAIN_WALL_…_2026-07-05.md:5-11, :123-128` | bounded (archived) | Spectral flow in a background U(1); an occupancy front acts as the wall. | The inflow was later corrected to an avoided crossing (record-time note :90). The occupancy-to-mass map is not derived. |
| Record-time open interval | `docs/THE_RECORD_TIME_DOMAIN_WALL_ON_AN_OPEN_INTERVAL_WHERE_THE_PARTNER_WEYL_MODE_LIVES_BOUNDED_THEOREM_NOTE_2026-09-03.md:4, :69-71, :90, :100, :130` | bounded (corrected) | Supplied 4-component Wilson matrix on intervals. The partner mode lives at the end or pin. Balanced pairing gives tr(χP_cut) = 0. | Exact zeros, inflow and universal claims were withdrawn (:130). "Record time" is a supplied coordinate. |
| Record walls in the staggered mass | `docs/RECORD_WALLS_IN_THE_STAGGERED_MASS_CARRY_LOCALIZED_2P1D_DIRAC_MATTER_VECTOR_LIKE_BOUNDED_THEOREM_NOTE_2026-09-03.md:4, :93-99, :111-113`; original `.claude/science/review-fixes/walls-7896-7909/REVIEW_CORRIGENDUM_2026-09-08.md:234-243, :262-266` | bounded (corrected) | 3D mass-sign walls bind 2+1D Dirac bands, paired across walls. Two crossing walls give a line band with no movers. Original: "vector-like, as a lattice construction in three dimensions has to be … The standard route … is a wall in a fifth dimension". | The corrected note **withdrew** the wall-swap/anomaly proof: "no physical chiral/anomaly exclusion beyond these selected matrices" (:113). Three orthogonal walls and interactions on the wall were not computed. |
| 2D record-time vortex | `docs/A_VORTEX_IN_A_TWO_DIMENSIONAL_RECORD_TIME_CARRIES_A_SINGLE_WEYL_MODE_…_2026-09-04.md:4, :49-57, :103-121` | bounded (corrected) | Two supplied extra coordinates. Winding n gives 2\|n\| localized states. The global index is 0. | An exact Weyl cone; physical record time. |
| Taste-singlet vortex strings | `docs/THE_TASTE_SINGLET_SECOND_MASS_IS_A_BODY_DIAGONAL_IMAGINARY_HOP_AND_ITS_VORTEX_STRINGS_CARRY_2N_CO_MOVING_MODES_…_2026-09-03.md:4, :217, :232-235` | bounded | The only second mass is a length-3 body-diagonal hop. A winding-n string carries 2n modes and is paired with −2n. Handedness is −Γ₃ (Jackiw–Rossi), "local to a string and never net". | It needs a site U(1) phase register ("a charged scalar's phase by another name"). |
| **Spin(10) symmetric gapping (SMG) on a slab** | `docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md:1-12, :195-221, :373-410, :440-452` | proposed_retained / conditional | An exact Spin(10)-invariant atom has a unique gapped ground state. Freezing the whole last layer keeps the opposite boundary partner. **Freezing only the mirror slots restores 8 Weyl doublers, 4+4**: "The removed mirror has not yielded an isolated chiral species" (:220-221). This is the Golterman–Shamir endpoint. | Intermediate or finite coupling, non-product boundaries, extended interactions ("live", :449-452). "No interacting chiral phase … is established" (:7). |
| K2a mirror selector (continuous time) | HEAD `.claude/science/candidates/candidate-law-20261008/TEST_LOG.md:58-96`; `KILL_SHEET.md:75-83` | PASS-weak (supervisor-checked, no referee) | In 3D Hamiltonian KS, the body-diagonal shift `T₁T₂T₃ = −X` equals Weyl chirality on the zero modes (exact). This gives a 9-site mirror projector and a Spin(10)-singlet quartic, with content 2×16 ⊕ 2×16̄ per field. **In 4D hypercubic form there is no selector.** | The gap (K2b). Separation is in crystal momentum, so links leak (Eichten–Preskill). mε is forbidden. 16–32 bits per vertex. Generations come in pairs. |
| Ultralocal GW excluded | HEAD `.claude/science/exercises/gravity-current-state-20261009/TESTS.md:2562-2590, :2728-2736`; `agents/C5_R2-4_report.md`, `C5_R2-4_referee.md:44-63` | refereed, CONFIRMED WITH CORRECTIONS | There is no ultralocal Ginsparg–Wilson operator in the hypercube-range W(B_d) class (exact Gröbner, d = 2, 3, 4); overlap is only exponentially local. "Nielsen–Ninomiya covers only the free exact-chiral class" (:2733). Mirror-SMG is NN-compatible and open. | Reflection positivity of overlap/DW; any construction. |
| Opus-direct overlap & GW | `archive/campaigns/opus-direct-20260827/POSITIVE_PATH.md:3407-3530, :4032-4110, :4423-4500, :9172-9245` | archive, unlanded research log | An overlap operator was built (GW residual ≤ 5e-15, index −n), on the campaign's own carrier. R45/R46: the Kähler–Dirac operator "forbids ultralocal chiral matter", not chiral matter. R121: taste blocks split by `Γ₁Γ₂Γ₃` = Nielsen–Ninomiya. | A GW operator from the framework's own rule; the carrier correspondence with the repo was never audited (DEFERRED_DECISIONS.md:128-133). |
| M₂(C)→M₄(C) enlargement (opus R122–R134) | `…/POSITIVE_PATH.md:9247-9310, :10195-10360`; `archive/campaigns/opus-direct-20260827/LANDING_CORE.md:24-25, :158-176, :199` | archive; **PARKED** owner decision | "For odd d the chirality space is exactly {0}". M₄(C) is the unique minimal algebra with a γ5. R134 says the only blocked chirality is the flavoured `γ5⊗ξ5`, 8 at +1 and 8 at −1. | Its d is the *Euclidean* Clifford count; see Tension T2. Parked at `docs/repo/DEFERRED_DECISIONS.md:121-146`, with the standing default "M₂(ℂ) stands as postulated". |

### 2d. Record- and admissibility-side handedness (cluster A, summarized)

| Object | Note / path:line | Status | What it shows | What it does NOT show |
|---|---|---|---|---|
| Record typing | `docs/CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05.md:56, :70-78` | meta | Records consume chirality; they do not source it. | — |
| Registration | `docs/REGISTRATION_REINSTATES_CHIRALITY_NO_GO_NOTE_2026-06-07.md:25-36` | no-go | This is the Koide generation sense. | — |
| Rule achirality, covariance classification, empty-state bootstrap | `archive/notes/docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_…_2026-07-03.md:60-117`; `archive/notes/docs/EMPTY_STATE_BOOTSTRAP_…_DEGREE_NINE_CHIRALITY_WALL_…_2026-07-04.md:64-122, :231-233`; `archive/notes/docs/RULE_ACHIRALITY_FROM_MINIMALITY_…_2026-07-04.md:29-31, :100-107` | bounded (archived) | A chiral rule costs one orientation bit, detected by the degree-9 cubic harmonic Ψ9. A law can be achiral while a state is chiral. A mirror axiom is rejected because it "would forbid the observed weak-sector chirality". | No fermion-sector claim. |
| Mirror-asymmetric rule; time-directed sweep; winding phase | `docs/A_MIRROR_ASYMMETRIC_ADMISSIBILITY_RULE_…_2026-09-05.md:26-30, :97-115`; `docs/A_TIME_DIRECTED_FORMATION_SWEEP_…_2026-09-05.md:146-152`; correction `.claude/science/physics-loops/chirality-correction-20260909/CORRECTION_HISTORY.md:3-7` | bounded (corrected, conditional-support) | A handed rule registers its own parity-odd texture. A sweep registers direction of motion, not a screw sense. The original universal "no-rule" claim was false. | "not absence of all handed interface modes" (MIRROR :115). |
| Handed-rule pseudoscalar census | `docs/ADMISSIBILITY_HANDED_RULE_PSEUDOSCALAR_INVARIANT_CENSUS_AND_PARITY_ODD_RECORD_CORRELATORS_BOUNDED_THEOREM_NOTE_2026-09-13.md:32-70, :97, :531-532` | proposed_retained | Handed covariant rule terms exist under every reading; the lowest soldered one is a Dzyaloshinskii–Moriya curl. They leave parity-odd record correlators. | Which reading is realized. The fermion consistency test is named but not run (:97). |
| Moriya handedness | `docs/DYNAMICS_CLAUSE_MORIYA_HANDEDNESS_IS_A_TWIST_WITH_CURVATURE_…_2026-09-24.md` | bounded | Handedness is a twist that is gauge only on a line. | Fermion chirality. |
| Chiral-pair programme (10-09/10-10, ~70 notes, commit 516cb69d84) | e.g. `docs/CHIRAL_PAIR_BOND_FACTOR_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-10.md`; `docs/CHIRAL_PAIR_HEIGHT_LINE_ORDER_BLIND_CUT_…`; `docs/ACHIRAL_ZERO_ONE_TWO_ORBIT_ORDER_BLIND_FACTOR_…_2026-10-09.md` | proposed_retained / mostly open_gate | "Chiral pair" means the two proper orbits of the record alphabet point (1,2,3), 48 points. The bond-factor space is 300-dimensional. The partner kernels give exact ranks in restricted ansätze only. 168 of 240 single-orbit cases are eliminated and 72 are open. | **No fermion content at all** (name collision; cluster A, scope warning). |

### 2e. Anomaly, hypercharge and generations

Rows come from cluster C. I re-checked the key lines of `THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE.md`, `ANOMALY_FORCES_TIME_THEOREM.md` (:13-26, :105-116, :364-371), `SM_ANOMALY_CLOSURE_…`:84-86, `GAUGE_ALGEBRA_SUPPLIED_CARRIER_…`:50 and `scripts/frontier_right_handed_sector.py`:47-48, :515.

| Object | Note / path:line | Status | What it shows | What it does NOT show |
|---|---|---|---|---|
| Three-generation / chirality boundary | `docs/THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE.md:5, :19-30, :40-46, :58-62, :67-84` | proposed_retained support | The exact 8 = 1+1+3+3 orbit structure. Rooting is undefined in Hamiltonian Cl(3). Chirality "enters only in the full framework through anomaly-forced time and the resulting one-generation right-handed completion". "not claiming a loophole in the usual no-go theorem. It is claiming a different theory surface" (:83-84). Since 2026-10-02 the hw=1 species reading is an "open bridge" (:22-24, :40-46). | Not claimed: a purely spatial chiral regulator evading Nielsen–Ninomiya (:61-62). |
| Anomaly forces time (3+1) | `docs/ANOMALY_FORCES_TIME_THEOREM.md:13-26, :105-116, :364-375` | bounded, conditional | With premises P-HY, P-ABJ (external), P-COMP (opposite-chirality singlet completion, :111), P-REC (ε realized as the Dirac-factor chirality, i.e. taste reconstruction, :114) and B-AXIS, the result is d_t = 1 and signature (3,1). | **Assumes the chiral spectrum.** "Replacing the LH content by its vector-like doubling makes all six anomaly conditions vanish … no chirality operator is needed" (:366-370). 1180 descendants. |
| One-generation closure; RH runner | `docs/ONE_GENERATION_MATTER_CLOSURE_NOTE.md:44-74`; `scripts/frontier_right_handed_sector.py:47-48, :515` | bounded, conditional | C^16 = C^8_L ⊕ C^8_R. The runner says the taste commutant "commutes with gamma_5, so the same taste quantum numbers appear in both chirality sectors" (:47-48). | The RH half is made SU(2) singlets "by the chirality of weak interactions" (:515), i.e. by hand. |
| SM anomaly closure | `docs/SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08.md:35-54, :84-86`; `docs/AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03.md:15-58, :248-250`; component traces (LH catalog, SU(3)³, Witten, B−L, 3̄, singlet completion) | bounded/positive, arithmetic | Anomaly traces vanish on the *given* content; RH hypercharges are forced given a minimal singlet completion. | "Excluding vectorlike/mirror content is the separate chirality question, which reduces to the staggered-Dirac / spin-statistics import … not closed here" (:84-86). The completion is not unique (vectorlike or B−L also pass). |
| ABJ via staggered ε | `docs/ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md:33-61, :190-206`; historic `HISTORIC_ABJ_STAGGERED_EPSILON_NOT_SPACETIME_GAMMA5_…`:21, :47-49 | no-go | The ε index is identically 0 on equal-sublattice tori (doubler cancellation). ε is not the spacetime γ5. | A taste-singlet/Adams or overlap index; imbalanced or curved complexes. |
| Taste-singlet spin γ5 exists (blocked 2⁴) | `docs/ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md:17-26, :55-93, :107` | bounded | A genuine taste-singlet γ5 exists on the blocked 2⁴ hypercube, distinct from ε. | A single-taste selector, and a bridge from that γ5 to a chirally *gauged* representation. |
| Gauging selection | `docs/GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md:47-67`; `GAUGE_GAUGING_SELECTION_CONJUGATION_INDEPENDENCE_NO_GO_…`:59-76 | open_gate / no-go | su(3)⊕su(2)⊕u(1) is a supplied cut of u(6). Conjugation-invariant data cannot select it. | Chiral su(2)_L: it "does **not** derive chiral `su(2)_L`" (:50, :104). |
| Native gauge "left-handed" surface; Y on the "chiral cube" | `NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_…_2026-05-23.md:5-13, :21-24`; `docs/CL3_HYPERCHARGE_EIGENVALUE_SPECTRUM_ON_CHIRAL_CUBE_NARROW_THEOREM_NOTE_2026-05-27.md:63-93` | bounded | Y spectrum {+1/3 ×6, −1 ×2} on the taste C^8, the 6+2 = Q_L + L_L pattern. | "left-handed" is a label only; "chiral cube" is a name, not Weyl chirality. |
| hw=1 triplet as generations | `docs/THREE_GENERATION_STRUCTURE_NOTE.md:4-13`; `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md:23-60`; `THREE_GENERATION_ROOTING_UNDEFINED_…_2026-05-27.md:3-9`; `PARITY_VIOLATION_DOES_NOT_REACH_GENERATION_TRIPLET_…_2026-05-23.md:20-55` | bounded | Exact irreducible label algebra. Rooting is undefined. ε maps hw=1 ↔ hw=2 ("generations ↔ anti-generations"). | Physical generations: the hw labels are not symmetry sectors of the staggered operator (2026-10-02 narrowing). |
| Historic generation-anomaly routes | historic intakes GENERATION_ANOMALY_FORCES_THREE, GENERATION_PHYSICALITY_OBSTRUCTED, GENERATION_KTHEORY (cluster C) | historic, pre-reset | Continuous anomalies cannot tell 1×24 from 3×8. 11 physicality routes failed. | — |

### 2f. Most recent lane: C3–C5 candidate law and gravity exercise (HEAD branch `claude/candidate-law-20261008`, not on main)

| Object | Where | Status | What it shows | What it does NOT show |
|---|---|---|---|---|
| NF-1 staggered strain control | `.claude/science/exercises/gravity-current-state-20261009/TESTS.md:9448-9474` (pre-reg), `:9493-9511` (worker), `:9578-9590` (referee, codex gpt-5.6-sol) | refereed: **OPEN** (literal U(1)_ε not exact; physics confirmed) | In continuous time **U(1)_ε is not a symmetry**. Two discrete symmetries, Θ (sublattice with τ→−τ) and P_stag, force Σ(0,0) = 0 under strain. One staggered field gives 2 Dirac tastes. **Taste wall:** T1 (a twin per field) adds +84 MeV to Γ_Z (36σ, conditional); T2 (twins paired across generations) needs SM + 3ν_R + one vector-like family, untested. | A chiral spectrum. T2 is not computed. Taste splitting breaks Θ. |
| R9-1 doubler Z width | `TESTS.md:3839-3842` | refereed | Literal doublers add about 588 MeV to Γ_Z. | — |
| R6-5 law-level CPT | `TESTS.md:3181-3210, :3264-3268` | worker reading | A symmetry price that needs "a chiral lattice construction that has not been built". | — |
| C3 lane D | `.claude/science/exercises/gravity-current-state-20261009/PRICE_NOTE.md:168` (P6); `TESTS.md:538-571` | INCONCLUSIVE (refereed) | "order alone gives no … handedness". Price P6: an orientation and spin-transport primitive. | — |
| Walls campaign T22–T25 | commit `4bd42747e5:.claude/science/walls/toe-walls-20260929/WALLS.md:41-44` (PR #9395 closed unmerged; claims moved to the J queue) | T22 STANDS→WEAKENED; T24 PRICED→WEAKENED | T22: "A free local walker always has a mirror twin; a left-only weak force is the same theorem. Every exit needs the full anomaly-free 16-state family." Untried: overlap (Lüscher; Kikukawa for SO(10)) and SMG. T25: "the walker gives 8 Weyl species where 48 are needed". | — |
| Fork probe (09-22) | commit `7adeccb570`, `FORK_PROBE_source_link_20260922.md:10, :14` (PR #8572); memory `fork-probe-20260922.md:10` | panel, closed | "species kept 4+4 … NN theorem in-framework". Tension: "vector-like spectrum forced; SM is chiral; 8 ≠ 16". | Any exit tested. |
| Open probe issues (same family) | #8741 (nothing in M₂(C) gaps a species), #9106/#8668 (no filling gives one-handed content), #8867 (the only parity-odd term is the scalar hop) | open, unrefereed by another family | — | — |

---

## 3. Already tried and failed, with reasons

Each item cites the note that records the failure. "Failed" means the route did not give an unbalanced, gaugeable chiral spectrum.

1. **γ5 inside one site.** No element of M₂(C) anticommutes with all three Paulis (`NO_PER_SITE_CHIRALITY…:55-65`). [no-go, proved]
2. **The staggered ε as physical chirality.**
   - ε is a free selector, not forced (`STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR…:42-45`).
   - It is the taste-non-singlet γ5⊗ξ5, not the spacetime γ5 (`HISTORIC_ABJ_STAGGERED_EPSILON_NOT_SPACETIME_GAMMA5…`; `POSITIVE_PATH.md` R134 at :10292-10360).
   - Its index vanishes identically (`ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO…`).
   - It "supplies a grading, not a chiral-gauging selection" (`CHIRAL_CONTENT_IS_THE_EPSILON_D…:41-42`).
   - In continuous time U(1)_ε is not even a symmetry (NF-1 referee, `TESTS.md:9578`).
3. **Covariant terms inside M₂(C) to gap single corners.** Corner stabilisers force a scalar symbol at each corner, and no invariant term at any reach gaps the walk (block 82). The scalar hop splits 1:3:3:1 but leaves touchings (block 77). Rate fields keep exactly 16 zero modes (block 119). The only books-keeping mass is mε, and it pairs opposite hands (block 139).
4. **Ticking time (discrete-time walks) to escape Nielsen–Ninomiya.**
   - Every finite-range tick has W3 = 0 (`LATTICE_HANDEDNESS…:116-160`, branch).
   - The first "all eight corners right-handed" census missed eight left-handed nodes at (π/2)(±1,±1,±1) (:74-79).
   - A tails-tick exists but has no Hamiltonian, is not reflection positive, and has a time doubler and heating (:226-281; T22 kill).
5. **Domain walls without a fifth dimension.**
   - In 3D, staggered-mass walls carry 2+1D Dirac, vector-like matter (`RECORD_WALLS…`; corrigendum :234-243). The original wall-swap/anomaly proof was later withdrawn (:93-99, :113).
   - The record-time wall needs a supplied extra coordinate, and the partner sits on the anti-wall or end (`THE_RECORD_TIME_DOMAIN_WALL…:69-71, :100`). Its inflow claim was withdrawn as an avoided crossing (:90).
   - The edge content does not match the SM 15 (`DOMAIN_WALL_EDGE_CONTENT_VS_SM…:156-179`).
6. **Vortices and strings.** Handedness is local to the defect and never net. The string needs a site U(1) phase register; the 2D vortex needs two supplied coordinates (taste-singlet note :217, :232-235; vortex note).
7. **Symmetric mass generation in the atomic (strong-coupling) limit.** The Spin(10) atom gaps, but projecting the mirror slots restores eight doublers, 4+4: the Golterman–Shamir endpoint (`SPIN10…:195-221`). Finite coupling is untried.
8. **A mirror selector in hypercubic (Z⁴) time.** None exists: T₁T₂T₃ takes both values inside each chirality block (K2a, `TEST_LOG.md:73-74`).
9. **An ultralocal Ginsparg–Wilson operator.** Excluded in the hypercube-range W(B_d) class (R2-4, refereed). Overlap is only exponentially local.
10. **Record-side handedness.**
    - It registers texture or direction of motion, not fermion chirality (MIRROR, SWEEP; correction packet).
    - A mirror axiom is rejected (RULE_ACHIRALITY :29-31).
    - No NN rotation-equivariant chiral labelling exists on 4-occupied stars (`archive/families/toe-lphys-chirality-lightcone-arc.md:31-36`).
11. **Identifying the twins with SM content.**
    - A twin per field fails the Z width (NF-1 T1; R9-1).
    - "Generations from tastes" fails: the two tastes are identical copies (`EMERGENT_LORENTZ…TASTE_CENSUS:248`).
    - The hw=1 → {e, μ, τ} labelling is a no-go plus convention (`STAGGERED_DIRAC_REALIZATION_GATE…:113-116`).
12. **Getting chirality from the anomaly argument.** It is circular as a source: the chain assumes LH content plus P-COMP and P-REC, and goes inert on vector-like content (`ANOMALY_FORCES_TIME_THEOREM.md:364-370`).
13. **Transport of the generation-sector chirality** (Koide sense; not the target wall).
    - The emergent chirality × emergent time product factorizes (`FLAVOR_EMERGENT_CHIRALITY_NO_TRANSPORT…`).
    - Registration does not reinstate it (`REGISTRATION_REINSTATES_CHIRALITY_NO_GO…`).
14. **The opus-direct M₄(C) "forced" claim.** It rests on Euclidean d = 3 counting; see Tension T2. It is parked, not refuted.

## 4. Pre-registered or named, but not run

| Test | Where pre-registered | State |
|---|---|---|
| **TW-1** twin = antiparticle (Majorana/reduced-staggered halving), field by field; expectation HALVE-PARTIAL | HEAD `.claude/science/exercises/gravity-current-state-20261009/TESTS.md:9619-9631` (12:58Z today) | not run; no worker or referee files (cluster D) |
| **TW-2** twins as generations with realistic taste splitting, strain leak; expectation SPLIT-HAZARD | same, `:9633-9645` | not run |
| **TW-3** symmetric-gapping toy (8 Majoranas, SO(7) quartic) under strain; count for the 16; expectation SMG-PROTECTS. The 3+1D part "goes to the chirality exercise" (:9658) | same, `:9647-9658` | not run |
| **K2b** does the mirror gap with no symmetry breaking (Butt–Catterall–Hasenfratz-type SU(4) staggered SMG) | HEAD `.claude/science/candidates/candidate-law-20261008/KILL_SHEET.md:83` | not run ("expensive") |
| **K6** three light generations with a hierarchy, without supplied labels | `KILL_SHEET.md:104-113` | not run |
| NF-1 **T2** content (SM + 3ν_R + one vector-like family) | `TESTS.md:9506`; `agents/C5_NF1_report.md:218-229` | not computed |
| R2-4 open items: reflection positivity of overlap/DW fermions in physical time; a positive 4D pair model with emergent chiral fermions | `agents/C5_R2-4_report.md:204, :255, :273` | not run |
| T22 kill's "cheaper question": which inputs the Lüscher/Kikukawa overlap route needs on Z³×Z_τ, and whether any follow from the axioms | `4bd42747e5:.claude/science/walls/toe-walls-20260929/kills/T22.md` | not run |
| Viability probe 4: 1D symmetric-gapping analogue | branch VB `docs/TOE_VIABILITY_MAP_…:575-578` | not run |
| J-queue task `J:derive:review-20260929-interacting-cones-and-chiral-carriers:a1` | `origin/ai/probes:probes/tasks/review-science-20260929.json` | unclaimed as of ai/probes d61e03f1fe; the 09-30 prior-art worker died before reporting (memory `stadium-picture-20260930.md:43,47`) |
| Handed-rule census extension and fermion-parity consistency test | `docs/ADMISSIBILITY_HANDED_RULE_PSEUDOSCALAR_…_2026-09-13.md:97` | not run |
| Law-achiral/state-chiral weak sector ("Nielsen-Ninomiya / domain-wall chiral-from-achiral program") | `archive/notes/docs/RULE_ACHIRALITY_FROM_MINIMALITY_…_2026-07-04.md:321-325` (cluster A) | not run |
| SPIN10 finite-coupling chiral phase with its current spectrum; non-product boundaries | `docs/SPIN10_…_2026-09-14.md:396-397, :408-410, :449-452` | not run |
| Three orthogonal record walls (point defect); interactions on the wall; the fine lattice | `RECORD_WALLS…` corrigendum `:260-270` | not run |
| Taste-singlet strings on a periodic transverse torus; many-body sector | taste-singlet note `:259-263` | not run |
| Block 119: twist fields, other sizes; block 79: 3D wall count | block 119 `:132`; block 79 `:43` | not run |
| ABJ: a taste-singlet/Adams or overlap index as an allowed physical measure; a single-taste selector | `ABJ_EPSILON_INDEX…:195-202`; `ABJ_P_REC…:90-93` | not run |
| Weyl-QCA: reproduce BCC uniqueness by blocks on Z³ | `ISOTROPIC_WEYL_QCA…:101-108` | not run |

## 5. The current wall, as the repo states it

These are the repo's own statements. I have stitched them together but added nothing.

- **Where chirality currently comes from.** "chirality is not claimed on the purely spatial surface by itself; it enters only in the full framework through anomaly-forced time and the resulting one-generation right-handed completion" (`docs/THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE.md:28-30`). And: "the current package is not claiming a loophole in the usual no-go theorem. It is claiming a different theory surface" (:83-84).
- **That entry is by premise.** P-COMP "(no anomaly-free extension that avoids a second chirality class is admitted)" and P-REC (ε realized as the irreducible-Dirac chirality) are declared premises (`docs/ANOMALY_FORCES_TIME_THEOREM.md:111, :114`). With vector-like content "no chirality operator is needed" (:366-370).
- **The mirror question is open.** "Excluding vectorlike/mirror content is the separate chirality question, which reduces to the staggered-Dirac / spin-statistics import … not closed here" (`docs/SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08.md:84-86`).
- **What the native carrier gives.** Vector-like N_f = 2 per staggered field. "The chiral sector. Absent … a lane wanting chiral matter must break the pairing, and nothing here says how" (`docs/EMERGENT_LORENTZ_…TASTE_CENSUS…:245, :267`).
- **The ε admission.** "SM matter is chiral, so physics *needs* ε; but that need is the admission, not a derivation" (`docs/STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR…:73-75`).
- **The free no-go, including ticks** (branch). The chiral exits are named as: interactions that gap the mirrors (SMG with the 16, which in 3+1D is a literature conjecture); a tails-tick; or an extra dimension, which "the Lattice axiom supplies `Z^3` only" rules out (`LATTICE_HANDEDNESS…:299-345`).
- **The walls campaign** (closed PR, J queue). T22: "A free local walker always has a mirror twin; a left-only weak force is the same theorem. Every exit needs the full anomaly-free 16-state family." (`WALLS.md:41`)
- **The class boundary.** "Nielsen–Ninomiya covers only the free exact-chiral class" (`gravity-current-state-20261009/TESTS.md:2733`). The interacting class is *not* covered by any repo no-go.
- **The SMG endpoint.** "The removed mirror has not yielded an isolated chiral species: the projection restores momentum-space doublers" (`SPIN10…:220-221`). Finite coupling is live.
- **The timing tension.** "the grid can either tell left from right (continuous time) or keep one speed for every field by symmetry (hypercubic time), but not both … a tension, not a theorem" (`candidate-law-20261008/TEST_LOG.md:90-96`).

**Precise wall (my synthesis, checked against the cites above).** The following is proved or bounded on the framework's surfaces. Take any free (quadratic), translation-invariant, finite-range one-body carrier built on M₂(C) sites, with continuous or ticking time and no extra dimension. Its Weyl content is balanced:
- 4+4 for the walker;
- 2L+2R per staggered field;
- 8+8 for the ordered tick.

The SM chain gets its chirality only from declared premises: P-COMP and mirror exclusion, P-REC, P-HY, P-ABJ, and B-AXIS. No construction on Z³ gauges a chiral subset.

Every remaining exit lies outside that class, and each carries a named price:
- interactions (SMG at finite coupling);
- infinite-range dynamics (tails-tick, overlap);
- an extra coordinate (domain wall);
- a larger site algebra (the parked M₄(C) proposal);
- more matter per site (the 16 or 32 bits per vertex of K2a).

## 6. Open gates touching the wall

1. **AX:178.** The staggered-Dirac/finite-Grassmann realization and AC_φλ (`docs/MINIMAL_AXIOMS_2026-06-29.md:178`). Its hidden admissions include the chirality field ε, fermionic statistics, and a signature/time import (`STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT…:31-49`). The P-FLUX kinetic selector is also open (`STAGGERED_DIRAC_REALIZATION_GATE…:346-361`).
2. **Spin-statistics as the retirement target for `{D,γ5}=0`.** `AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md` is unaudited (`STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR…:59-65`).
3. **The anomaly-forces-time premises.** P-ABJ (external), P-HY, P-COMP (including mirror exclusion), P-REC and B-AXIS (`ANOMALY_FORCES_TIME_THEOREM.md:105-116`).
4. **Gauging selection.** Chiral su(2)_L is not derived (`GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md:50, :104`).
5. **The hw=1 species reading** is an open bridge (`THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE.md:22-24, :40-46`).
6. **Parked owner decisions** (`docs/repo/DEFERRED_DECISIONS.md`):
   - **#4, the M₄(ℂ) Qubit-domain enlargement** (:121-146). Its wake condition 1 is "the chirality/generation program resumes". **This exercise plausibly fires it.** Per the file's rule (:13-15), whoever observes a fired condition must say so to the owner.
   - **#2, the Ψ9 flip-invariance / orientation bit** (:50-79). Its wake condition 2 is "a weak-sector or handedness result needs the bit's status".
7. **The owner's range question.** Does Admissibility fix only the rule's range, so that the dynamics may be quasi-local or have tails? This comes from the T22 attack premise table and R2-4's "nearest-neighbor → quasi-local" price (`C5_R2-4_report.md:296`, SUGGESTED for chirality).
8. **Matter count per site.** The registered default "do not enlarge the Qubit domain by inference" makes the 8-vs-16-vs-48 Weyl count an owner-level question (`LATTICE_HANDEDNESS…:325-332`; VB map `:580`).
9. **The weak-force hand / orientation bit.** T23 is MISFRAMED→WEAKENED, and the weak hand stays a parked owner decision (`WALLS.md:42`).
10. **Law-level CPT price.** It needs a chiral lattice construction (R6-5).
11. **The J-queue chirality task** is unclaimed (§4).

## 7. Ten files a route agent must read

1. `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full. Note :111 ("No admission class"), :114-130 (no dynamics) and :178 (the gate).
2. Branch `origin/claude/toe-viability-probes-20260927`: `docs/LATTICE_HANDEDNESS_A_FINITE_RANGE_FREE_WALKER_IS_LEFT_RIGHT_BALANCED_WHETHER_TIME_FLOWS_OR_TICKS_A_CHIRAL_FREE_TICK_NEEDS_TAILS_BOUNDED_THEOREM_NOTE_2026-09-27.md`. This is the in-framework Nielsen–Ninomiya result including ticks, the tails construction and the three exits.
3. `docs/THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE.md` together with `docs/ANOMALY_FORCES_TIME_THEOREM.md`. Read the premise table :105-116 and the falsification legs :364-375. This is where chirality is currently supplied.
4. `docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md`. It gives the actual low-energy content: 2 Dirac tastes, vector-like.
5. `docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md`. This is the SMG attempt, its endpoint failure and its live finite-coupling gap.
6. HEAD `.claude/science/candidates/candidate-law-20261008/TEST_LOG.md:58-96` (K2a) and `KILL_SHEET.md:75-113` (K2a/K2b/K6). These give the 3D continuous-time mirror selector and the hypercubic loss.
7. HEAD `.claude/science/exercises/gravity-current-state-20261009/TESTS.md`: R2-4 (:2562-2590, :2726-2736), NF-1 (:9448-9511, :9578-9590) and TW-1/2/3 (:9611-9658), plus `agents/C5_R2-4_report.md` and `agents/C5_NF1_report.md`.
8. `docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`, `docs/STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md` and `docs/STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR_NARROW_THEOREM_NOTE_2026-06-06.md`. They cover the gate, the earlier exercise, and ε as an admission.
9. Blocks 77, 82 and 119 under `docs/`:
   - `ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_…_2026-09-22.md`
   - `ADMISSIBILITY_RULE_WHAT_CAN_GAP_THE_WALK_NO_INVARIANT_TERM_AT_ANY_REACH_…_2026-09-22.md`
   - `ADMISSIBILITY_RULE_THE_SPECIES_SYMMETRY_FORCES_ONLY_DOUBLING_…_2026-09-24.md`

   Together they say what M₂(C)-covariant terms can and cannot do to the eight corners.
10. `docs/repo/DEFERRED_DECISIONS.md` (#2, #4) with `archive/campaigns/opus-direct-20260827/LANDING_CORE.md` §7 and `POSITIVE_PATH.md` R121–R134 (:9172-9310, :10195-10360). These hold the parked M₄(C) proposal and the Euclidean-d argument it rests on.

Next in line:
- `4bd42747e5:.claude/science/walls/toe-walls-20260929/WALLS.md:41-44` and `kills/T22.md`;
- `docs/RECORD_WALLS_IN_THE_STAGGERED_MASS…` with its corrigendum;
- `archive/notes/docs/DOMAIN_WALL_EDGE_CONTENT_VS_SM_CHIRAL_FERMIONS_MAP_…_2026-07-05.md`;
- `docs/ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md`.

---

## Tensions and misframing flags found while mapping (readings; none is checked here)

- **T1. "Chirality" means six different things in the repo.** Title searches give many false positives. The six senses are:
  - (a) Weyl/gauge handedness, which is the target;
  - (b) Koide/generation chirality `Γ_χ = (2/3)J − I` (the June "chirality gate" family, `CL3_CHIRAL_*`, `REGISTRATION_…`, `FLAVOR_…`);
  - (c) the staggered sublattice grading ε, which is taste-non-singlet;
  - (d) record-alphabet orbit handedness (the CHIRAL_PAIR programme, Ψ9);
  - (e) the walk's direction components (`CHIRAL_3PLUS1D_*` and `CHIRAL_WALK_SYNTHESIS`, which are gravity-lane);
  - (f) the Clifford volume element.

  Only (a) is the wall. Route agents should not count (b), (d) or (e) as prior attacks on it.
- **T2. The parked M₄(C) premise looks like a Euclidean-counting artifact.** It is unchecked.
  - Opus R122/R133 conclude "Z³ has no chirality at all" from Cl(d) with d = 3 and no time direction (`POSITIVE_PATH.md:9254-9270, :10235-10262`).
  - In the Hamiltonian (continuous-time) reading, n = 3 + 1 is even (`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION…:18-19, :72-75`).
  - The repo has *exact* checks that Weyl handedness exists on M₂(C)-built carriers. K2a finds `e^{iφ}T₁T₂T₃ = −X` with X = ±1 (4,4) (`TEST_LOG.md:73`). The taste census finds `X = I⊗T` (:161-162, :172).
  - In the Hamiltonian form the chirality operator must commute with the velocity matrices and anticommute with the mass. It does not need to anticommute with the Γ's, which is the criterion R133 used.
  - So "odd d ⇒ no chirality" does not transfer to Z³ with continuous time. What M₂(C) lacks is a *net* chirality, not a chirality operator.
  - This should be checked before anyone treats M₄(C) as "forced". DEFERRED_DECISIONS :128-133 already says the opus carrier's correspondence to the repo carrier was never audited.
- **T3. "U(1)_ε" is misnamed in the Hamiltonian setting.** Several June notes call ε "the exact massless U(1)_ε" (`STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR…:32`). In continuous time it is a discrete sublattice (spectral) symmetry Θ, not a U(1): `{ε,H}=0`, so `e^{iθε}` does not commute with H. NF-1's referee confirmed that U(1)_ε is not exact (`TESTS.md:9578`). Route agents should not plan "gauge U(1)_ε" or "use the exact U(1)_ε" moves.
- **T4. The hw=1 triplet is read three incompatible ways.** No note reconciles them:
  - as three generations (staggered gate, generation lane);
  - as three Weyl nodes of *one hand* for the 2-component walker (block 77 T1: orientation signs (−1)^|n|, levels 1:3:3:1, so hw=1 is single-handed and hw=2 is the opposite hand);
  - as part of 2 identical Dirac tastes for one staggered field (taste census: "No generations from tastes").

  In addition, the taste C^8 is read as one generation's LH content Q_L + L_L, 6+2 (cluster C). For this wall, the second reading matters most. "Three generations" and "one-handed triplet" are the same corners, so any route that keeps hw=1 and lifts hw=2 is exactly a mirror-gapping problem, and its anomaly count must be done on that split.
- **T5. Continuous time against hypercubic time.** The chirality selector exists only in continuous time (K2a). The one-light-cone protection (`kinetic_isotropy_primitive`) and reflection positivity want hypercubic ticks. Tails-ticks are not reflection positive (`LATTICE_HANDEDNESS…:272-281`). Any route must say which time it uses.
- **T6. Several routes carry a site-count price.** K2a needs 16–32 bits per vertex. SPIN10 uses q = 64 per spatial site on a layered slab. The SM needs 48 Weyl against the walker's 8 (T25). The matter-count reading is an owner-level question (§6, item 8).
- **T7. Branch-only results the exercise must not miss:**
  - LATTICE_HANDEDNESS (PR #9363, closed);
  - WALLS T22–T25 (PR #9395, closed; J queue);
  - K2a, NF-1, R2-4 and TW-1/2/3 (HEAD branch, PR #9476);
  - the opus campaign (archive, unlanded log; only LANDING_CORE is "landed").

  None of these is on main's `docs/`.
