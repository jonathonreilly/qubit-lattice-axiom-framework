# Axiom Minimality Policy

> **Key terms used in this doc** are indexed A-Z at [docs/KEY_TERMINOLOGY.md](../KEY_TERMINOLOGY.md); each row points to the canonical source-of-truth doc.

**Status:** binding rule for the audit lane through completion of the full
repo audit.

`A_min` is fixed for ordinary audit work as the three named framework axioms
in `docs/MINIMAL_AXIOMS_2026-06-05.md`: Lattice, Quantum, and Record. Approved
framework primitives are tracked separately in
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
    `Lattice + Quantum + Record` + emergent-time + reflection positivity do not
    supply a value of `c_t/c_s`, the scale reference carries no dimensionless
    ratio, and since `c_t = c_s` is itself the emergent-Lorentz output, deriving
    it from those structures would be circular. The adjacent freedoms are not
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
  - **Scope.** The minimal framework baseline remains the three named axioms.
    This primitive does not re-axiomatize time: the emergent single-clock
    evolution remains derived, and only the one graining ratio `c_t/c_s` is
    fixed. It supplies no dynamics, no fourth spatial dimension, and no
    dimensionless observable.

- **2026-06-11 -- Record axiom individuation rewording.** The framework axiom
  set remains the three named axioms Lattice, Quantum, and Record, with source
  `docs/MINIMAL_AXIOMS_2026-06-11.md` and stable registry id `minimal_axioms`.
  - **Why it is admissible.** The Record axiom now states the realized outcome
    as the realized central sector individuated by the context's registered
    scalar surface. The prior `K`/CPT-orbit outcome clause is recovered exactly
    as the special case of a surface that is `K`/CPT-invariant and
    orbit-separating, and conversely a surface separating an orbit pair is
    inconsistent with the orbit clause -- a landed two-way equivalence
    (`KCPT_ORBIT_CLAUSE_KINVARIANT_SURFACE_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-06-10.md`).
    The rewording relocates where the same content sits (postulated quotient
    becomes a theorem of surface invariance); it neither strengthens nor
    weakens the premise.
  - **No laundering.** Record does not supply the readout context, central
    decomposition, registered surface, `K`/CPT structure, sector-generation
    rule, weighting, normalization, probability, measurement/decoherence
    dynamics, time metric, within-sector data, occupancy rule, P2/modulus,
    log-det, source/action, scale, or arbitrary observable identification.
    The `K`-reality of realized states remains the standing pin, exposed at
    sector resolution by the equivalence note and not discharged by this
    rewording.
  - **Scope.** Dependencies on the three framework axioms chain-satisfy without
    bounding downstream rows. This rewording invalidates prior direct
    `minimal_axioms` audits through the axiom-premise hash guard and must be
    re-audited by the independent audit lane where relevant. It does not itself
    promote any downstream theory surface or apply any audit verdict. Adoption
    is gated on the independent audit of the equivalence note and its sibling
    campaign rows before merge.
