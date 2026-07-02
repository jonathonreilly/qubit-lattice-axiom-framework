# Axiom Minimality Policy

> **Key terms used in this doc** are indexed A-Z at [docs/KEY_TERMINOLOGY.md](../KEY_TERMINOLOGY.md); each row points to the canonical source-of-truth doc.

**Status:** binding rule for the audit lane through completion of the full
repo audit.

`A_min` is fixed for ordinary audit work as the four named framework axioms
in `docs/MINIMAL_AXIOMS_2026-06-29.md`: Lattice, Qubit, Admissibility, and
Record. Approved framework primitives are tracked separately in
`docs/audit/data/axiom_premise_nodes.json`. Lane closure must close from the
current approved premise surface by derivation, identification, bounded
composition, or no-go boundary, not by amending that surface inside the lane.

## 1. Disallowed moves
- Adding `Axiom*` or an equivalent primitive, including a `Cl_4(C)`
  carrier on `P_A H_cell` or any irreducible module structure presented
  as a new axiom.
- Rewording an existing `A_min` axiom to be more permissive or more
  restrictive to close a lane, including PR #113's former axiom-3 reading
  question.
- Framing a result as "if we just accept X as primitive, lane Y closes"
  without recording X as an unmade science-level decision.

## 2. Allowed moves
- Identifying structures already present in `A_min` with Standard Model
  constructs. These are support-tier unless audited as class C; class E/F
  load-bearing identifications record `audited_renaming`.
- First-principles derivations from `A_min` that close without additional
  assumptions; these are the retained-tier path after class C audit.
- Bounded compositions with explicit named residuals.
- No-go boundary notes that state what is structurally unclosable from
  the current axiom set.

## 3. Precedents
- PR #186 / PR #196: `Axiom*` (`Cl_4(C)` on `P_A H_cell`) was declined as a
  forced extension; the proposed minimality theorem audit-failed at O2.
- PR #113: the former axiom-3 permissive-reading amendment is declined. The
  work lands only as bounded no-go inventory for `(C2-X)` and its attack
  frames.

## 4. Workflow
If a physics-loop or science worker reaches "we need an extra axiom to close
this", the correct action is:
1. Land the work as a bounded no-go boundary note documenting what would
   close under the proposed axiom.
2. Record the proposed axiom as an explicit science-level decision
   waiting on human input.
3. Move to a different lane or a different attack frame.
Do not add the axiom and proceed.

## 5. Scope
This policy applies until the full repo audit is complete. Owner-approved
axiom or primitive changes are recorded below and in the machine registry.
Until another explicit approval is recorded, the current premise surface is
fixed.

## 6. Explicit Owner Approval For Axioms And Primitives

Review-loop, physics-loop, audit-loop, and audit-pipeline consumers must not
add or amend repo-wide axioms, framework primitives, or equivalent
foundational premises without explicit owner approval. Approval must be
recorded in this policy and in the relevant machine registry before the new
premise can chain-satisfy downstream claims.

Framework primitives are distinct from Tier-A admitted derivation targets:

- **Axioms and approved primitives** are foundational framework premises. They
  are tracked in `docs/audit/data/axiom_premise_nodes.json`, chain-satisfy
  dependencies without bounding downstream status, and are guarded by
  `check_axiom_premise_clean.py`.
- **Tier-A admitted derivation targets** are non-axiom inputs with no-go
  portfolios. They are tracked in `docs/audit/data/tier_a_admissions.json` and
  chain-satisfy only at `retained_bounded` until retired by a retained
  derivation.

Recorded explicitly approved axiom updates:

- **2026-07-02 -- Record readout determination and rule totality.** Two
  wording updates to `docs/MINIMAL_AXIOMS_2026-06-29.md` (owner-approved,
  2026-07-02; source file edited in place, bundled same-day with the
  Admissibility clarification below so the premise-hash re-audit waves
  coincide). First, the Record axiom's readability clause gains one sentence
  closing the readout-function gap in place: "A readout value is determined
  by record content alone." (owner wording; additivity unchanged). Second,
  the Qubit axiom gains one individuation sentence generalizing the
  equivalent-presentation quotient beyond the named Cl(3,0) pair: "No
  presentation, and no basis or frame within one, is primitive; possibilities
  related by presentation equivalence are the same possibility." Third, one totality sentence
  is added to the Qualification section: "A rule offered as a law must be
  well-defined at every state admissible under Admissibility throughout its
  declared domain; the domain must be declared as registered structure, not
  by enumerating states, and a prescription defined only at particular states
  is pointwise content, not a law." Wording validated by three blind panel
  rounds (round 1: seven seats — operator algebras, quantum foundations,
  lattice gauge, philosophy of physics, GR/cosmology, condensed matter,
  experimental metrology — on the discipline clauses: S1 7x yes-with-caveat,
  S2 5x yes-with-caveat 2x contestable, 0 rejections; round 2: five seats on
  the owner's Record sentence in partial context: 4x works-with-qualifier, 1x
  fails via the descriptive-reporting seam; round 3: four seats on the same
  sentence in FULL four-axiom context, adjudicating whether the axiom set
  already individuates content structurally: 4x sufficient-but-ambiguous,
  unanimous that the exclusion of unregistered-frame readouts is JOINTLY
  entailed by the Record sentence, the Qubit presentation clause, and the
  Qualification supply paragraph — no readout-supply clause needed — with
  the single ambiguity being the Cl(3,0)-pair scoping of "adds no further
  primitive structure," closed by the Qubit individuation sentence above).
  Reading notes: supplied
  structure is pinned by the Qualification's first paragraph (the four
  axioms, approved primitives, explicit admissions, approved registrations),
  with the realized state entering through the registered pointwise-interface
  primitive and its records through the Record axiom; determination is over
  what varies — supplied structure is fixed background, so a readout built
  from registered structure has content-determined values, while a value that
  shifts with an imported basis, frame, or convention is not determined by
  record content and is excluded; explicitly admitting a choice defines a
  different fixed readout whose values are again content-determined; the
  admissible-state quantifier is fixed by the Admissibility axiom and prior
  registered structure, independent of the candidate rule (no gerrymandered
  domains — a declared domain must be a registered structural condition such
  as a gap or phase condition, never an enumeration of the states where the
  rule happens to hold); totality binds the rule's verdicts, not auxiliary
  presentations; conditional rules and pointwise evaluation under the
  realized-state primitive remain admissible. Panel-derived reading notes on
  content individuation: record content is the locked available possibility
  as framework-individuated (structurally, per the Qubit individuation
  sentence) — under it, readable quantities are exactly the invariants of
  supplied-plus-registered structure, and registering structure monotonically
  enlarges the readable class (scheme-relativity without per-readout
  registration); descriptive reporting outside premise-use is not policed by
  the axioms and binds at first premise-use via the supply paragraph; the
  additivity clause together with per-record content-determination excludes
  relational scalar readouts (invariant relational quantities remain derived
  objects); whether the internal orientation/pseudoscalar sign is supplied
  via proper-rotation covariance (chirality readouts) is the standing
  downstream chirality-import question and is explicitly NOT decided by this
  update. The clauses name
  no operator, basis, weighting, selector, kinetic class, or value; they add
  no axiom and no primitive; downstream consequences remain theorem content
  subject to independent audit. In the same update,
  `docs/C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md`
  is recorded as a labeling-convention ratification (the import-retirement
  path, not new structure): the singlet/doublet outcome cells and the
  unit/complement generator channels on the supplied `hw=1` circulant class
  are two namings of the same two cells of one canonical `C_3` generation
  readout context. The premise-hash guard invalidates prior direct
  `minimal_axioms` audits; the independent audit lane re-audits.

- **2026-07-02 -- Admissibility clarification: availability varies with the
  neighbors.** The Admissibility clause now reads: "For each site, the
  available possibilities are determined by, and vary with, the
  nearest-neighbor conditions" (owner-approved wording update, 2026-07-02;
  source file edited in place). "Vary with" is existential, not
  per-neighborhood: availability is not constant across nearest-neighbor
  conditions; under most conditions the full domain may remain available. It
  excludes the vacuous rule (full domain under every condition) and the
  neighbor-independent constant rule; it names no operator, kinetic class,
  selector, or carrier, and downstream consequences remain theorem content.
  The premise-hash guard invalidates prior direct `minimal_axioms` audits;
  the independent audit lane re-audits.

- **2026-06-29 -- Foundation reset: site possibility and local admissibility.**
  The framework axiom set is updated to the four named axioms Lattice, Qubit,
  Admissibility, and Record, with source `docs/MINIMAL_AXIOMS_2026-06-29.md`
  and stable registry id `minimal_axioms`.
  - **Why it is admissible.** The 2026-06-05 Record wording already depended on
    realized-outcome registration, but it left arbitrary record mosaics
    underconstrained. This reset states the minimal ontology directly: Lattice
    carries physical locality; Qubit names the domain of local possibilities
    and its full one-site algebraic presentation; Admissibility names one fixed
    nearest-neighbor rule, covariant under lattice translations and proper
    cubic rotations, by which the available possibilities are determined by,
    and vary with, the nearest-neighbor conditions at each site; a site need
    not carry a record, and when present a record locks exactly one local
    possibility from the subset available at that site under Admissibility;
    only records are readable, and scalar readout is additive over finite
    pairwise-disjoint record collections.
  - **No laundering.** Admissibility does not choose the readout context, select
    a measurement basis, provide an occurrence rule, define probabilities,
    assign weights, normalize readouts, specify an update law, provide
    measurement/decoherence dynamics, define time metric or arrow, choose a
    Hamiltonian or transfer operator, select a kinetic branch, or identify
    physical observables. Record does not supply readout-context selection,
    central decomposition, `K`/CPT structure, sector-generation rule, weighting,
    normalization, probability, occurrence rule, update law,
    measurement/decoherence dynamics, time metric, within-sector data,
    occupancy rule, P2/modulus, log-det, source/action, scale, local
    observability, or arbitrary observable identification.
  - **Boundary language.** The new memo states that further physical structure
    remains compatible, but requires derivation, bridge, explicit admission, or
    approved primitive registration before use as load-bearing content.
  - **Scope.** Dependencies on the four framework axioms chain-satisfy without
    bounding downstream rows. This reset invalidates prior direct
    `minimal_axioms` audits through the axiom-premise hash guard and must be
    re-audited by the independent audit lane where relevant. It does not itself
    promote any downstream theory surface or apply any audit verdict.

- **2026-06-05 -- Record axiom refinement.** The framework axiom set remains
  the three named axioms Lattice, Quantum, and Record, with source
  `docs/MINIMAL_AXIOMS_2026-06-05.md` and stable registry id
  `minimal_axioms`.
  - **Why it is admissible.** The Record axiom now states durable
    realized-outcome registration in a supplied readout context: the realized
    outcome is the `K`/CPT orbit of the realized central sector, and scalar
    readout remains finitely additive over finite pairwise-disjoint record
    collections. This is a premise about what counts as a record once the
    readout context is supplied, not a mechanism that produces the context or
    the record.
  - **No laundering.** Record does not supply the readout context, central
    decomposition, `K`/CPT structure, sector-generation rule, weighting,
    normalization, probability, measurement/decoherence dynamics, time metric,
    within-sector data, occupancy rule, P2/modulus, log-det, source/action,
    scale, or arbitrary observable identification.
  - **Scope.** Dependencies on the three framework axioms chain-satisfy without
    bounding downstream rows. This refinement invalidates prior direct
    `minimal_axioms` audits through the axiom-premise hash guard and must be
    re-audited by the independent audit lane where relevant. It does not itself
    promote any downstream theory surface or apply any audit verdict.

- **2026-06-04 -- Record axiom.** The framework axiom set is updated to the
  three named axioms Lattice, Quantum, and Record, with source
  `docs/MINIMAL_AXIOMS_2026-06-04.md` and stable registry id
  `minimal_axioms`.
  - **Why it is admissible.** The Record axiom states only finite scalar
    record-readout additivity over disjoint record collections. It is a narrow
    premise about the readout surface, not a theorem about record production or
    a route to log-det structure.
  - **No laundering.** The older
    `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` remains a broader conditional
    parent and is not an axiom-premise node. Record does not import
    P2/modulus, log-det, source/action, measurement, Born weights, time arrow,
    normalization, scale, or arbitrary observable identification.
  - **Scope.** Dependencies on the three framework axioms chain-satisfy without
    bounding downstream rows. Record/P1 scalar additivity is retired from
    Tier-A; the remaining Tier-A derivation targets are non-axiom admissions
    and continue to bound dependents until retired by retained derivations.

Recorded explicitly approved primitive:

- **2026-06-04 -- scale-reference primitive.** The single dimensionful scale
  reference `a^{-1}` is accepted as a framework primitive and registered as
  `scale_reference_primitive` with source
  `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`.
  - **Why it is admissible.** The framework baseline carries no dimensionful
    number, so one scale reference is irreducible by dimensional analysis. This
    is a units conversion, not a physics axiom or a dimensionless import.
  - **No laundering.** The primitive carries no mass ratio, coupling, mixing
    angle, phase, selector, readout bridge, or empirical fit. Depending on this
    primitive cannot supply dimensionless physics, and the purity guard must
    keep the source note inside that boundary.
  - **Scope.** The minimal framework baseline remains fixed. This decision does
    not assert `a/l_P = 1`; the self-consistency that the natural unit equals
    the Planck length remains a separate open gravity derivation.

- **2026-06-09 -- kinetic-isotropy primitive.** The space-time kinetic-form
  isotropy `c_t = c_s` (OS0 graining isotropy: the emergent tick is grained on
  the same footing as the spatial edge) is accepted as a framework primitive and
  registered as `kinetic_isotropy_primitive` with source
  `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`.
  - **Why it is admissible.** It is a dimensionless **structural** graining fact
    about the regulator, the time-direction analogue of the `LATTICE` axiom's
    spatial cubic adjacency `a_x = a_y = a_z` (a structural premise already
    accepted at axiom grade). It is irreducible for premise accounting:
    `Lattice + Qubit + Admissibility + Record` + emergent-time + reflection
    positivity do not supply a value of `c_t/c_s`, the scale reference carries
    no dimensionless ratio, and since `c_t = c_s` is itself the
    emergent-Lorentz output, deriving it from those structures would be
    circular. The adjacent freedoms are not
    supplied here: the absolute scale belongs to `scale_reference_primitive`,
    while any spacing-ratio/reachability claims remain in their own derivation
    rows.
  - **No laundering.** The primitive carries no mass ratio, coupling, mixing
    angle, phase, selector, readout bridge, or empirical fit. It supplies a
    dimensionless **structural/geometric** normalization (the regulator's
    space-time isotropy), of the same category as cubic adjacency, **not**
    dimensionless **dynamical** content. Depending on this primitive cannot
    supply a physical observable, and the purity guard must keep the source note
    inside that boundary.
  - **Scope.** The minimal framework baseline remains the four named axioms.
    This primitive does not re-axiomatize time: the emergent single-clock
    evolution remains derived, and only the one graining ratio `c_t/c_s` is
    fixed. It supplies no dynamics, no fourth spatial dimension, and no
    dimensionless observable.

Recorded Tier-A registry refinement (admissions remain Tier-A; nothing is
promoted to axiom or primitive class):

- **2026-06-11 -- realized-state primitive.** The realized-state interface --
  the axioms select no state; a physical history fixes one law-admissible
  realized state; derivations may evaluate at it pointwise only -- is accepted
  as a framework primitive and registered as `realized_state_primitive` with
  source `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`. Explicit owner
  approval recorded 2026-06-11, conditional on best-physics-judgment affirmation
  (necessary, unavoidable, clean) -- affirmed; wording passed a two-round
  ten-persona adversarial physics panel (round 1: 9 reservations + 1 objection;
  round 2: 10/10 pass, no objections).
  - **Why it is admissible.** It is the laws-versus-initial-conditions floor
    made explicit: the framework axioms fix the carrier, adjacency,
    local admissibility interface, and registration
    structure, and a state is an additional datum no state-blind structure can
    supply. Irreducibility is exhibited case by case on exact instances
    (state-blind dynamics with state-contingent registered outcomes; no derived
    selector on degenerate invariant manifolds; invariant-state continua --
    support runner
    `scripts/realized_state_primitive_irreducibility_support_2026_06_11.py`,
    PASS=8). A registered slot with fixed policing clauses replaces per-note
    ad-hoc conditioning prose, which is where measures, typicality assumptions,
    and representative choices get smuggled.
  - **No laundering.** The primitive supplies the slot, never the content: no
    state, state-selection rule, measure, typicality/genericity assumption,
    weighting, normalization, probability rule, preferred or default state
    (the maximal-symmetry reference is never "the natural input"), or any
    state-contingent value. Its counterfactual test makes the boundary
    mechanical: a quoted number that would differ had another permitted state
    been realized is registered data, not derivation output.
  - **Past-hypothesis classification.** The past hypothesis is explicitly NOT
    housed by this primitive: it is a strictly stronger input (a specialness /
    atypicality claim about the realized history, exactly the class the
    primitive's clauses forbid it from supplying), and remains the named
    residual of
    `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`.
  - **Scope.** Effective statuses are unchanged and remain audit-lane-only.
    Dependencies on this primitive chain-satisfy without bounding downstream
    rows; rows quoting data of a particular realized state remain conditional
    on that supplied data exactly as supplied inputs always are -- nothing here
    lifts state-contingent content into the unconditional column.
- **2026-06-11 -- Tier-A minimum-statement refinement.** The two admitted
  derivation targets (`AC_phi_lambda`, `theta`) are restated at their
  sharpest landed decomposition in
  `docs/ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md` (minimum-statement
  section) and `docs/audit/data/tier_a_admissions.json`:
  `AC_phi_lambda` = the doublet reading/occupancy selection + the R-eta delta
  readout identification + the species bridge; `theta` = the gauge-side
  winding account + the mass-side orientation localized onto the
  determinant-readout bridge, with the mass-side K-real structure identified
  as the same `C_3` object as the `AC_phi_lambda` reading selection.
  - **Why it is admissible.** A restatement-to-minimum is governance hygiene:
    it removes derived/conditional content from the admission statements so
    elimination campaigns target the true residual atoms. No admission is
    added, removed, adopted, or re-graded; the genuine admitted-input count
    stays at two; dependents continue to chain-satisfy only at
    `retained_bounded`.
  - **No laundering.** The named premise candidates for the reading
    selection (orbit-occupancy; the R-D durability bridge) remain
    **unadopted** proposals: the reading selection is and stays Tier-A
    admitted content. It is a selector for dimensionless physics content
    and is therefore **not** primitive-eligible under the kinetic-isotropy
    admissibility boundary above; this entry exists precisely to record that
    classification decision.
  - **Scope.** Effective statuses are unchanged and remain audit-lane-only.
    The `no_go_portfolio` lists are unchanged (verified rows only); the new
    `sharpening_sources` fields list landed source notes whose audit status
    is set only by the audit lane.

Approved scope classification (no axiom, primitive, or Tier-A change; nothing
added to or removed from any premise registry):

- **2026-06-16 -- past-hypothesis magnitude is a scope condition, not a
  premise.** Owner approval recorded 2026-06-16. The thermodynamic past
  hypothesis -- the low-entropy *magnitude* of the initial
  boundary ("why the boundary was so atypically special"; Penrose
  ~1-in-10^(10^123)) -- is classified as the framework's
  **scope / domain-of-applicability condition**, not as a premise in any of the
  three categories (axiom, primitive, Tier-A). It is the residual named in
  `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`
  and the input carved out of the realized-state primitive (2026-06-11 entry
  above, "Past-hypothesis classification").
  - **Rationale (physics/logic, not an audit finding).** The arrow's
    *direction* (record formation), the boundary's *existence* (record
    durability = append-only well-foundedness), and the *time-axis* are derived
    separately; the only residual is the low-entropy magnitude, which is
    (i) *content* -- a measure-relative atypicality value, not a units
    convention (scale-reference) or a structural graining ratio
    (kinetic-isotropy), so not a primitive; (ii) *contingent* -- the
    time-symmetric microdynamics is equally consistent with a high-entropy past
    (Loschmidt), so not an axiom/law; (iii) *provably non-retirable* -- needed
    identically by every time-symmetric theory (CM/QM/QFT/GR) and underivable
    from time-symmetric microdynamics, so not a Tier-A derivation target (which
    must be retirable). An input that can never be discharged is not a premise
    the chain rests *on*; it is the antecedent the relevant claims are scoped
    *by* -- results that use it are honest conditionals ("given a low-entropy
    past, X"), in the standard laws-versus-initial-conditions sense. A scope
    condition creates no derivation debt (Tier-A's bounding mechanism), so it
    does not bound dependents.
  - **Guardrails.** The low-entropy magnitude must remain absent from both
    premise registries (`axiom_premise_nodes.json`, `tier_a_admissions.json`)
    and must not be cited by retained/shipped rows as a dependency. The scope
    classification is bound to the magnitude *alone*: the derived direction,
    boundary existence, and time-axis stay unconditional and acquire no
    conditional tag. No typicality, measure, or specialness assumption is
    laundered under the "scope" label; the realized-state primitive's
    counterfactual test continues to police that boundary.
  - **Machinery.** The three premise categories are unchanged and the
    past hypothesis is outside all three by construction (this generalizes the
    realized-state primitive's existing carve-out). No registry row, no
    `canonical_id`, no `premise_nodes.py` / `compute_effective_status` / schema
    change; the audited source notes (arrow, existence reduction, realized-state)
    and the machine registries are left byte-unchanged by this classification.
    Optional future hardening (separate, not in this change): a one-line audit
    lint warning if any retained row ever cites the low-entropy magnitude as an
    upstream dependency.
