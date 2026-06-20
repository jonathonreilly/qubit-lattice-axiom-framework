# Wall-to-Gate Map — Axiom-Update Proposals (block01, 2026-06-20)

**Lane:** axiom-update-proposals, branch
`physics-loop/axiom-update-proposals-block01-20260620`.
**Posture:** OWNER-authorized to go beyond the no-new-axiom rule and deliver
either no-new-axiom cracks OR candidate axiom-update PROPOSALS. This is a MAP
FOR the owner's governance decision; it adopts nothing.
**Status authority:** independent audit lane / owner only. Nothing here sets an
audit verdict or promotes an axiom.

**STATUS DISCIPLINE.** Every conditional derivation that maps consequences of an
UNADOPTED candidate axiom carries
`hypothetical_axiom_status: "conditional on accepted new axiom; not retained on
the actual current surface."` No bare `retained`/`promoted` appears. The
candidate is proposed for governance, never self-adopted.

**Verification runner:**
`logs/runner-cache/axiom_update_proposals_wall_to_gate_runner_2026_06_20.py`
(cache `...2026_06_20.txt`, **TOTAL: PASS=32 FAIL=0**). For each wall it
re-attacks the no_go (confirms it genuinely walls on the tested finite surface)
AND verifies the named minimal supplier shape discharges it.

**Policy conformance** (`docs/audit/AXIOM_MINIMALITY_POLICY.md`,
`docs/MINIMAL_AXIOMS_2026-06-05.md`). Current `A_min` = {Lattice, Quantum,
Record}; approved primitives = {scale_reference, kinetic_isotropy,
realized_state}. The minimal-axioms memo's OPEN GATES list is the target set:
*arrow / measurement / decoherence / record-production dynamics; readout
context / sector measure / objectivity / occupancy; gauge group / particle
content / species; P2 / modulus / log-det; source / action.* Every proposal
below lands in exactly one of those named open gates — i.e. each proposes
content the memo already declares is **outside** axiom content, not a reword of
an existing axiom (which §1 forbids). Each proposal is recorded as an "unmade
science-level decision" per §1/§4, not adopted.

---

## A. Sourcing note (read first)

The task prompt referenced 2026-06-20 campaign notes
(`SINGLE_CLOCK_BAXIS_..._NO_GO_NOTE`, `ANOMALY_FORCES_TIME_ABJ_..._NOTE`,
`KOIDE_RECORDS_OBJECTIVITY_DERIVATION_ATTEMPT_NOTE`, exercise packets
`baxis-wall-break` / `abj-walls-break`, OWNER_DECISION_PACKETs, FRONTIER_RAYS).
**Those exact filenames do not exist in this checkout** (verified by exhaustive
`find`). The prior-stage output was not produced under those names. This map is
therefore reconstructed directly from the LANDED campaign no_go / bounded-theorem
notes that DO exist and that already name the supplier shapes and gates verbatim.
The load-bearing sources used are listed per wall. Fanout magnitudes are
cross-checked against `docs/audit/data/load_bearing_summary.json`
(`transitive_descendants`): `minimal_axioms` 1564, `anomaly_forces_time_theorem`
1049, `observable_principle_from_axiom_note` 887,
`staggered_dirac_realization_gate` (=AC_phi_lambda) 927,
`native_gauge_closure_note` 1361. The task's headline fanouts (B-AXIS 959, ABJ
1105, observable 909, Koide 1) are consistent with these and are used as given.

---

## B. WALL MAP — each walled bridge -> exact minimal missing premise -> open gate -> fanout

Format: **WALL** | campaign no_go that walls it | exact minimal missing premise
(supplier shape) | open gate it sinks into | fanout. The "skeptical re-attack"
column records whether a genuine no-new-axiom crack exists FIRST (per posture).

### B-AXIS cluster (single-clock; total fanout ~959, gated via anomaly_forces_time 1049 + RP/continuum)

| Wall | Walling no_go (landed) | Minimal missing premise (supplier shape) | Open gate | Fanout |
|---|---|---|---|---|
| **N2b — clock unit `tau`** | `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06` §"`T` alone does not fix the clock unit": `T` fixes only the product `tau·H`, not `H`. (runner W2: same `T` reconstructs for `tau`=1,2,0.7 with `H ∝ 1/tau`) | **ONE time-unit / blocked-time-spacing datum** `2a_tau` (a single dimensionful tick value). Supplying one `tau` value pins the Stone generator uniquely. | record-production / time-metric dynamics (a "tick" is record-stream timing) — but see skeptical flag: this is largely the already-approved `scale_reference_primitive` extended to the time edge. | ~959 (shared) |
| **N4 — axis label** | `SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11`: every retained anchor (OS/GNS, record/durability, CAP-K cone, anomaly/chirality) is EXACTLY transported by `W = P_{τ↔1}∘diag((-1)^{x_τ x_1})` (runner W1: periodic resid=0; durability = unitary-invariant operator-order monotonicity). | **ONE per-axis `Z_2` BC-asymmetry datum** (antiperiodic-`τ`/periodic-space breaks `W` exactly — runner W1 resid=8.0; symmetric BCs restore it, resid=0) **OR the record-shaped equivalent: a declared registration-direction bridge** "the realized record history's event order is parametrized by lattice axis `μ`". | **record-production dynamics** (the registration-direction form) — i.e. which lattice axis carries the record/event order. The BC form is a regulator convention; the *derivation* of the asymmetry is the open piece. | ~959 |
| **N5 — second clock** | `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06` §3: two commuting transfers `T_A⊗I`, `I⊗T_B` lift to a product whose Stone generator is the sum; the factor groups survive (runner W3: `H_sum=H_prod`, `[H_A,H_B]=0`). | **A single-factor (no independent commuting transfer-factor) transfer premise**: the physical transfer is irreducible / carries no tensor-factor clock. | record-production / measurement dynamics: whether tensor-factor "clocks" are physically excluded vs gauge/redundant (scope-boundary N6). | ~959 (shared) |

Skeptical re-attack (B-AXIS): the N4 no_go was ALREADY a correction of an
over-strong claim (RP-selects-axis was withdrawn). The residual is genuinely
walled — `W`-transport is exact and durability is provably unitary-invariant, so
no retained structure breaks it. **N4 does NOT crack without an added datum.**
N2b is mostly already covered by approved primitives (see flag SK-1).

### ABJ cluster (anomaly_forces_time; total fanout ~1105, node anomaly_forces_time_theorem=1049)

The master bridge `ANOMALY_FORCES_TIME_THEOREM.md` declares FIVE premises:
P-HY, P-COMP, P-REC, P-ABJ, plus B-AXIS (inherited). Each is a wall.

| Wall | Walling no_go / boundary | Minimal missing premise (supplier shape) | Open gate | Fanout |
|---|---|---|---|---|
| **P-ABJ — internal index** | `ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30`: on equal-sublattice even `Z^4` tori the staggered `ε`-index `A_t[U]=Tr(ε e^{-tD†D})=0` for ALL U(1) backgrounds (square bipartite block) (runner W4: vanishes for q∈{-2..2}). | EITHER **(a) the standard ABJ anomaly-to-inconsistency implication as a declared physics premise** (P-ABJ as written), OR **(b) a framework-internal taste-singlet / Adams / overlap (Ginsparg-Wilson) chiral measure that is a valid physical chiral readout**, OR **(c) an imbalanced/curved emergent complex (`χ≠0`)** on which the signed heat trace is nonzero (runner W4: 3×3 unequal-sublattice gives A_t=0.838). | gauge content / particle content (whether the framework's chiral sector is anomalous as a *consistency* fact) — and, for route (c), it is partly **geometry not axiom** (see flag SK-2). | ~1105 |
| **P-HY — `Y_like` is-gauged** | `ANOMALY_FORCES_TIME_THEOREM` HY-surface row: the cited abelian note `NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23` supplies the traceless eigen-direction with spectrum `{+1/3×6,-1×2}` but DELIBERATELY does not claim anomaly-complete `U(1)_Y`. | **A "the `Y_like` eigen-direction is a GAUGED `U(1)` of the emergent theory" premise** — i.e. the traceless abelian direction is dynamical/gauged, not a global label. | **gauge group / gauge content** (which abelian factors are gauged). | ~1105 (shared) |
| **P-COMP — RH-template existence** | `ANOMALY_FORCES_TIME_THEOREM` P-COMP row: no anomaly-free extension avoiding a second chirality class is admitted; the SM branch `(4/3,-2/3,-2,0)` is only a computed EXISTENCE witness, not forced. | **A "the anomaly-cancelling completion is the opposite-chirality SU(2)-singlet RH template" premise** — i.e. the particle-content completion shape exists and is of that class. | **particle content / species** (the right-handed multiplet template). | ~1105 (shared) |
| **P-REC — single-taste selector** | `ANOMALY_FORCES_TIME_THEOREM` P-REC row + `NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02` (per-site `γ_5` impossible in `M_2(C)`); staggered grading lives on taste-reconstructed lattice. | **A taste-reconstruction selector**: the staggered `ε` is realized as the Clifford chirality on the *irreducible* emergent Dirac factor (anticommuting with every spacetime `γ`, incl. temporal). I.e. a rule selecting one taste/Dirac factor from the 16-fold staggered multiplet. | **species / particle content** (taste→generation/Dirac reconstruction). Adjacent to the AC_phi_lambda realization gate (fanout 927). | ~1105 (shared) |
| **(B-AXIS inherited)** | imported from single-clock; supplies the `d_t≤1` cap. | (the B-AXIS cluster above) | record-production dynamics | counted under B-AXIS |

Skeptical re-attack (ABJ): P-ABJ route (c) is a GENUINE no-new-axiom crack
candidate (flag SK-2) — `χ≠0` is geometry. P-HY/P-COMP/P-REC are each genuine
walls: the cited notes explicitly decline to supply them, and they are
particle/gauge-content selectors that Quantum's axiom text explicitly excludes
("no species identification, gauge group, particle content"). They do NOT crack
from the current surface.

### Koide cluster (r=1/2; fanout ~1, near-leaf; measure/objectivity shared with koide cone 327 / AC gate 927)

| Wall | Walling no_go | Minimal missing premise (supplier shape) | Open gate | Fanout |
|---|---|---|---|---|
| **r=1/2 — equal-block measure** | `KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31`: general capacity max is `r* = w_p/(2 w_s)` (runner W5); the two-block pointer fixes the NUMBER of blocks, not the weight ratio. | **An equal-block `(1,1)` sector measure** (atom/share weighting over the singlet/doublet K-real sectors), as opposed to rank/Born `(1,2)`. Equal-block ⇒ `r*=1/2` ⇒ `Q=2/3` (runner W5). | **sector measure** (the singlet/doublet block weighting). | ~1 (but the *measure axiom* is shared with the whole Koide/flavor stack) |
| **r=1/2 — objectivity selector** | `FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02`: QD objectivity fixes the pointer BASIS, not the weight; tracial `I/3` pushes to `(1/3,2/3)` ⇒ r=1 (runner W6); `I/3` is the U(3)-invariant reference. | **A maximum-objective-information / indifference selector** over the objective alphabet (count objective LABELS, not Born weight) — picks uniform `(1/2,1/2)` (runner W6: H(unif)>H(rank)). This is the "objectivity functional as physical readout criterion" the conditional note names. | **objectivity / readout-context** (which functional is the physical readout criterion). | ~1 (shared with objectivity-readout stack) |

Skeptical re-attack (Koide): the conditional note ALREADY checked 5 routes; the
measure is genuinely a free reference-state/measure choice (basis≠weight is a
clean computed separation). Does NOT crack. The two inputs are independent (the
note's N2), so they need a measure premise AND an objectivity-selector premise —
both in the readout-context/sector-measure gate.

### observable_principle cluster (T1-d det-readout; fanout ~909, node observable_principle_from_axiom_note=887)

| Wall | Walling boundary | Minimal missing premise (supplier shape) | Open gate | Fanout |
|---|---|---|---|---|
| **T1-d — det-readout identification** | `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` Boundary T1-d (declared bridge premise): "the scalar record readout `W` is a continuous function of `Z=det(D+J)` alone on all of `R_{>0}`, and disjoint independent source blocks register as disjoint records (Cauchy additivity)". | **A record-readout-IDENTIFICATION bridge**: continuity of `W` in `Z=det` on `R_{>0}` + disjoint-block additivity ⇒ `W = c·log det` (`c=1`). NOTE the FORM (det vs trace) is NOT the wall — it is a theorem (runner C1/W7: det multiplicative over independent blocks, trace not). | **readout context / P2-log-det** (the identification of Record's abstract additivity with the determinant readout). | ~909 |
| **FS — det realization (statistics frame)** | `OBSERVABLE_PRINCIPLE_P2_DET_REALIZATION_BRIDGE_CONDITIONAL_ON_FERMIONIC_FRAME_NARROW_THEOREM_NOTE_2026-05-28` + `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25`: fermion and hard-core boson share per-site dim 2; JW is an invertible change of generators on the same `M_{2^|Λ|}(C)` — statistics frame NOT forced (runner W8). | **A fermion-parity superselection / graded-locality (spin-statistics) premise** that disallows the hard-core-boson frame and keeps the CAR frame (runner W8: CAR ladders anticommute across sites). Discharges `FS`, making `Z_matter[J]=det(D+J)` the framework generator. | **source / action** (the matter-sector statistics frame underlying the partition function). Adjacent to AC realization gate 927. | ~909 (shared; gates the realization half of P2) |

Skeptical re-attack (observable): the FORM half of P2 (det) is ALREADY a
no-new-axiom theorem (multiplicative-character) — flag SK-3. So the 909 fanout
does NOT all need an axiom: the genuine residuals are (i) the T1-d
*identification* bridge (arguably already inside Record's additivity once the
det form is granted — a candidate crack), and (ii) `FS` (a real spin-statistics
premise). This SHRINKS the observable wall substantially.

### record-formation (the dynamics floor under B-AXIS-N4 and Koide and observable)

| Wall | Walling no_go | Minimal missing premise | Open gate | Fanout |
|---|---|---|---|---|
| **record formation not forced** | `RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06`: `H=0`, decoupled `H`, and energy eigenstates are baseline-consistent NO-record witnesses (runner W9). | **A record-production / decoherence-dynamics premise** (a system-environment coupling that drives einselection; runner W9: coupling+env-superposition ⇒ coherence→0, and |coh|→0 monotonically in #env copies). | **arrow / measurement / decoherence / record-production dynamics** — the single biggest open gate. | floor under B-AXIS-N4, Koide objectivity, T1-d (transitively large) |

Skeptical re-attack (record-formation): exact witnesses (`H=0`, decoupled,
eigenstate) defeat unconditional forcing; the Record axiom VERBATIM excludes
measurement/decoherence dynamics. Cannot crack — this is the genuine dynamics
floor.

---

## C. GATE CLUSTERS — the smallest set of candidate axiom additions

The walls above cluster into **THREE** candidate axiom additions (matching the
expected shape), each in exactly one open gate. Each is the WEAKEST sufficient
addition for its cluster, recorded as an unmade science-level decision.

### CLUSTER 1 — Record-Production / Decoherence-Dynamics Axiom  [GATE: arrow / measurement / decoherence / record-production dynamics]

`hypothetical_axiom_status: "conditional on accepted new axiom; not retained on
the actual current surface."`

- **Weakest sufficient statement (candidate):** "There is a system–environment
  coupling such that, for the realized state, off-diagonal coherence in a
  pointer basis is monotonically suppressed (einselection), producing a durable
  record." (Pure-dephasing form; runner W9 exhibits |coh|→0.) The
  registration-direction (which lattice axis carries the event order) is the
  same object, supplying B-AXIS-N4's record-shaped pin.
- **Walls discharged:**
  - record-formation no_go (the dynamics floor);
  - **B-AXIS N4** via the registration-direction-bridge form (PIN-REG) — the
    record event order is parametrized by lattice axis `μ`;
  - (downstream) the arrow-of-time / past-hypothesis residual stack feeds from
    here.
- **Gate:** record-production dynamics (the memo's largest open gate).
- **Total fanout unlocked:** the record-formation floor + **~959** (B-AXIS via
  the registration-direction route, which then unlocks the anomaly cap path
  ~1049). High.
- **Minimality note:** strictly weaker than a "past hypothesis" (which the
  realized_state_primitive note explicitly classifies as a STRONGER
  atypicality input and forbids). Proposes only that record-producing dynamics
  EXIST, not a specific kernel/weight (those stay supplied per
  `POST_RECORD_DYNAMICS_AUTHORITY_STACK_MAP_2026-06-06`).

### CLUSTER 2 — Readout-Context / Objectivity / Sector-Measure Axiom  [GATE: readout context / sector measure / objectivity / occupancy]

`hypothetical_axiom_status: "conditional on accepted new axiom; not retained on
the actual current surface."`

- **Weakest sufficient statement (candidate):** "The physical readout criterion
  is maximum objective information over the objective alphabet (count objective
  K-real sector LABELS / atom-share, not Born/rank weight); equivalently the
  central-sector measure is the equal-block `(1,1)` measure." This is exactly
  the pair of inputs the Koide conditional note isolates.
- **Walls discharged:**
  - **Koide r=1/2 equal-block measure** ⇒ `r*=1/2`, `Q=2/3` (runner W5);
  - **Koide r=1/2 objectivity selector** ⇒ uniform `(1/2,1/2)` (runner W6);
  - **T1-d det-readout identification** (the "readout context" that ties
    Record's additivity to `Z=det`, the Cauchy/disjoint-block clause) — same
    gate;
  - (downstream) the flavor/CKM-vs-PMNS readout-context rows
    (`CKM_SMALL_VS_PMNS_LARGE_FROM_RECORD_READOUT_CONTEXT_...`) and the
    occupancy/orbit-count decision feed from here.
- **Gate:** readout context / sector measure / objectivity.
- **Total fanout unlocked:** Koide r=1/2 (~1 direct) + the shared
  objectivity/measure stack (koide cone 327, flavor readout rows) + **~909** of
  the observable T1-d identification half (after the FORM theorem and FS are
  accounted — see SK-3). Medium–high once shared fanout is counted.
- **Minimality note:** supplies the *criterion/measure* only; does NOT supply
  weights/probabilities/normalization (those stay outside per Record's text).
  The objectivity selector and the equal-block measure are the SAME choice
  expressed two ways (atom-share = label-count), so this is ONE addition, not
  two (the conditional note's N2 lists them as independent inputs, but a single
  "objective-label / atom-share readout criterion" axiom supplies both).

### CLUSTER 3 — Gauge-Content / Particle-Content / Statistics Axiom  [GATE: gauge group / particle content / species; source/action]

`hypothetical_axiom_status: "conditional on accepted new axiom; not retained on
the actual current surface."`

- **Weakest sufficient statement (candidate):** "The emergent matter sector is a
  GAUGED chiral gauge theory with the framework's `Y_like` abelian factor gauged
  (P-HY), fermionic statistics (graded locality / fermion-parity
  superselection, discharging FS), and the staggered grading realized as the
  Clifford chirality on the irreducible Dirac factor (P-REC taste selector);
  anomaly cancellation is required for consistency (P-ABJ)." This is the union
  of the four declared ABJ premises minus the parts that crack (see SK-2) plus
  the FS spin-statistics premise.
- **Walls discharged:**
  - **ABJ P-HY** (`Y_like` is gauged);
  - **ABJ P-COMP** (RH-singlet completion template exists);
  - **ABJ P-REC** (taste/single-Dirac-factor selector);
  - **ABJ P-ABJ** routes (a)/(b) (anomaly-to-inconsistency as physics, or a
    valid internal chiral index) — route (c) may crack without this (SK-2);
  - **observable FS** (fermion-parity superselection) — same "graded
    locality/statistics" content;
  - (downstream) the entire anomaly_forces_time chain (`d_t=1`, signature
    (3,1)), the staggered-Dirac realization gate (AC_phi_lambda, 927), and the
    SM gauge-content rows.
- **Gate:** gauge group / particle content / species (+ source/action for FS).
- **Total fanout unlocked:** **~1105** (ABJ chain) + ~909-shared (FS half of
  observable P2) + the AC realization gate (927, overlapping). HIGHEST.
- **Minimality note:** this is the heaviest addition (it asserts gauge content +
  statistics, which Quantum's axiom text explicitly leaves out). It can be
  SPLIT into sub-clauses (P-HY gauging; FS statistics; P-COMP/P-REC content) if
  the owner wants finer granularity; but they all sink into the same
  "particle/gauge content" gate and are naturally one science-level decision
  ("the emergent matter content is the chiral SM-shaped gauged fermionic
  sector"). The B-AXIS `d_t≤1` cap is consumed by this chain but is supplied by
  Cluster 1, not here.

**Why three (not more):** the nine walls collapse onto three OPEN GATES from the
memo. N2b (clock unit) is NOT a fourth cluster — it is flagged (SK-1) as already
covered by the approved `scale_reference_primitive`/`kinetic_isotropy_primitive`
extended to the time edge, i.e. a candidate no-new-axiom crack, not a proposal.

---

## D. COVERAGE TABLE — candidate axiom -> total downstream fanout unlocked

| Candidate axiom (cluster) | Gate | Walls discharged | Total fanout unlocked (approx) | Strength |
|---|---|---|---|---|
| **C1 Record-Production/Decoherence Dynamics** | record-production dynamics | record-formation floor; B-AXIS-N4 (registration-direction form); arrow stack | record floor + ~959 (B-AXIS→anomaly path) | weak (existence of einselecting dynamics; weaker than past-hypothesis) |
| **C2 Readout-Context/Objectivity/Sector-Measure** | readout context / sector measure / objectivity | Koide r=1/2 measure; Koide r=1/2 objectivity; T1-d det-readout identification; flavor readout-context stack | ~1 (Koide direct) + ~887–909 (observable identification half) + koide/flavor shared (≥327) | weak–medium (a readout criterion; supplies no weights/probabilities) |
| **C3 Gauge-Content/Particle-Content/Statistics** | gauge group / particle content / species; source/action | ABJ P-HY, P-COMP, P-REC, P-ABJ(a/b); observable FS | ~1105 (anomaly chain) + ~909-shared (FS) + 927 (AC gate, overlapping) | heavy (asserts gauge + statistics; splittable) |

Fanout-per-unit-strength ranking (maximize unlocked per unit axiom strength):
**C2 ≈ C1 > C3.** C1 and C2 are weak additions with large transitive reach; C3
unlocks the most but is the strongest addition. Recommended owner sequencing:
adopt the WEAKEST high-leverage first (C1, then C2), and treat C3 as the heavy
content decision — after first attempting the SK-2 crack that may remove part of
P-ABJ without any axiom.

---

## E. SKEPTICAL FLAGS — no_gos that look over-strong on re-read (candidates for a no-new-axiom CRACK, not a proposal)

These are flagged per the OWNER posture "don't believe the no-gos." Each is a
place to spend a no-new-axiom re-attack BEFORE proposing an axiom.

- **SK-1 — B-AXIS N2b (clock unit `tau`) may already be covered by approved
  primitives.** The scope-boundary no_go says `T` fixes only `tau·H`. But
  `scale_reference_primitive` (the single dimensionful `a^{-1}`, owner-approved
  2026-06-04) and `kinetic_isotropy_primitive` (`c_t=c_s`, owner-approved
  2026-06-09) TOGETHER fix the time-edge spacing relative to the spatial edge.
  So N2b's `2a_tau` may be *derivable* from the already-approved primitive
  surface — a no-new-axiom crack, NOT a new axiom. **Action: attempt to derive
  `2a_tau` from `scale_reference × kinetic_isotropy` before proposing anything.**

- **SK-2 — ABJ P-ABJ "irreducibly external" may be over-strong.** The
  square-block no_go is narrow (its own N1/N5/N7): it kills only the standard
  `ε`-index on EQUAL-sublattice EVEN tori. The runner confirms an
  imbalanced/curved complex (`χ≠0`, e.g. 3×3) gives a NONZERO signed heat trace
  (W4: A_t=0.838). If the framework's ACTUAL emergent complex is imbalanced or
  curved (geometry, not an axiom), P-ABJ route (c) closes with NO new axiom. The
  no_go itself names this as an open positive-retention route. **Action: check
  whether the emergent complex is forced to be balanced-even; if not, P-ABJ may
  crack and Cluster 3 shrinks.**

- **SK-3 — observable T1-d fanout (909) is over-attributed to a missing axiom.**
  The FORM half of P2 (det vs trace) is ALREADY a no-new-axiom theorem: a
  generator additive on independent subsystems AND a multiplicative character of
  the block operator IS the determinant (runner C1: det multiplicative, trace
  not). And the T1-d *identification* clause (continuity in `Z` + disjoint-block
  additivity) is arguably ALREADY inside the Record axiom's finite additivity
  once the determinant form is granted. So the genuine new-axiom residual in the
  observable cluster is ONLY `FS` (spin-statistics), which lives in Cluster 3 —
  not a standalone observable axiom. **Action: try to discharge T1-d from
  Record-additivity + the multiplicative-character theorem with NO new axiom;
  if it lands, the 909 fanout is unlocked by Cluster 3 alone (via FS), and C2's
  observable share is smaller than tabulated.**

- **SK-4 — Koide objectivity-selector vs equal-block-measure "independence"
  (N2) may be over-counted.** The conditional note lists them as two independent
  inputs, but atom-share weighting and label-counting objectivity are the SAME
  physical choice. A single "objective-label readout criterion" supplies both,
  so this is ONE addition (Cluster 2), not two — a minor minimality crack on the
  no_go's wall-count, already folded into Cluster 2 above.

---

## F. ONE-PARAGRAPH SUMMARY

The nine walled high/medium-fanout bridges from the single-clock (B-AXIS
N2b/N4/N5, ~959), anomaly (ABJ P-HY/P-COMP/P-REC/P-ABJ, ~1105), Koide
(r=1/2 measure + objectivity, ~1 direct but stack-shared), and
observable-principle (T1-d det-readout + FS, ~909) campaigns collapse onto
exactly THREE open gates from `MINIMAL_AXIOMS_2026-06-05.md`, hence three
candidate axiom additions, each carrying
`hypothetical_axiom_status: conditional`: **(C1)** a weak record-production /
decoherence-dynamics axiom (existence of einselecting system–environment
dynamics) that discharges the record-formation floor and B-AXIS-N4 via the
registration-direction bridge; **(C2)** a weak readout-context / objectivity /
sector-measure axiom (the physical readout criterion is maximum objective
information = equal-block atom-share) that discharges both Koide r=1/2 inputs and
the T1-d det-readout identification; and **(C3)** a heavy gauge-content /
particle-content / statistics axiom (gauged chiral fermionic SM-shaped matter
with anomaly cancellation) that discharges the four ABJ premises and the
observable `FS` frame. A 32/32-passing runner verifies, for every wall, that the
no_go genuinely walls AND that the named minimal supplier shape discharges it.
Per the "don't believe the no-gos" posture, four skeptical flags mark
no-new-axiom CRACKS to attempt first: B-AXIS N2b is likely already covered by the
approved scale/kinetic-isotropy primitives (SK-1); ABJ P-ABJ may crack on an
imbalanced/curved emergent complex with no axiom (SK-2); the observable T1-d
fanout is over-attributed because the determinant FORM is already a theorem and
the identification clause is arguably inside Record-additivity (SK-3); and the
Koide measure/objectivity "two inputs" are one physical choice (SK-4). Fanout per
unit of axiom strength ranks C2 ≈ C1 > C3, so the recommended governance
sequence is C1 then C2 (weak, high-leverage), with C3 deferred until the SK-2
crack is attempted. This is a MAP for the owner's governance decision; it adopts
nothing and sets no audit verdict.
