# Axiom Minimality Policy

> **Key terms used in this doc** are indexed A-Z at [docs/KEY_TERMINOLOGY.md](../KEY_TERMINOLOGY.md); each row points to the canonical source-of-truth doc.

**Status:** binding rule for the audit lane through completion of the full
repo audit.

`A_min` is fixed for ordinary audit work as the three named framework axioms
in `docs/MINIMAL_AXIOMS_2026-06-04.md`: Lattice, Quantum, and Record. Approved
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

Recorded explicitly approved axiom update:

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

- **2026-06-05 -- Record axiom v0.4 update.** The Record axiom is updated from
  the 2026-06-04 additivity-only form to v0.4: *a record is the irreversible
  registration of which real (CPT-even) superselection sector is realized*, with
  unchanged additivity. Source `docs/MINIMAL_AXIOMS_2026-06-05.md` (supersedes
  `docs/MINIMAL_AXIOMS_2026-06-04.md`); logic
  `docs/RECORD_AXIOM_V04_UPDATE_LOGIC_NOTE_2026-06-05.md`; stable registry id
  remains `minimal_axioms`.
  - **Why it is admissible.** The update introduces exactly one new assumption,
    the reality (CPT-even) adjective (= the already-named K-reality stance); the
    other added clauses (irreversibility, registration of *which* sector) are
    constitutive of recordhood, and "sector = center" is derived
    (`center(M_n)=scalars`). This is an explicit owner-approved Section 6
    amendment, not a lane-internal rewording of the kind Section 1 forbids.
  - **What it adds.** The classical/quantum cut as derived content (the recorded
    structure is the real Wedderburn center; reality fixes 2 generation blocks)
    and the measure dial `r(s)=2^(s-1)` with its two symmetry-distinguished
    settings `r=1/2` (block-count) and `r=1` (Born/dimension).
  - **No laundering, and the binding non-overreach frame.** The update does NOT
    supply within-sector/Born weights, per-sector dial occupancy, a time metric,
    measurement/decoherence dynamics, log-det/modulus, source/action,
    `AC_phi_lambda` value, theta, or arbitrary observable identification. It does
    **not** force any generation modulus: in particular `r=1/2` is a stable
    symmetry-distinguished *setting* the charged-lepton sector occupies, not a
    forced or exclusive value (the framework default is `r=1`; a universal-`s`
    rule is falsified by the inter-sector Koide spread).
  - **Scope.** The audit lane updates the `minimal_axioms` source pointer to the
    2026-06-05 memo only after independent review of the v0.4 language and logic.
    No downstream row is promoted, bounded, or re-statused by this approval.

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
