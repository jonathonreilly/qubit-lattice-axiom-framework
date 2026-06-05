# Lüders Rule from Compositional Bayesian Consistency:
# `deps_changed:dep_added:minimal_axioms` Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dep-resolution restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing derivation
`σ → (P σ P) / Tr(P σ P)` (Lüders rule from (U1)–(U4) consistency
requirements) of the parent note
[`LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md`](LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md)
is invariant under the 2026-06-04 framework citation-graph re-resolution
in which the parent's stable upstream dependency edge was migrated from
the date-stamped `minimal_axioms_2026-05-20` node to the canonical
`minimal_axioms` node. It is not a new theorem claim, not a status
promotion, and not an attempt to perform re-audit work. If the audit
pipeline seeds this file, it is a `meta` companion row; the audit lane
still sets `audit_status`, and pipeline-derived `effective_status`
remains downstream of that authority.
**Companion target:** `luders_rule_from_composition_consistency_note_2026-05-20`
(parent note `docs/LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md`).
**Primary runner:**
[`scripts/audit_companion_luders_rule_from_composition_consistency_deps_changed_2026_06_04.py`](../scripts/audit_companion_luders_rule_from_composition_consistency_deps_changed_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_luders_rule_from_composition_consistency_deps_changed_2026_06_04.txt`](../logs/runner-cache/audit_companion_luders_rule_from_composition_consistency_deps_changed_2026_06_04.txt)

---

## Why this companion exists

The parent narrow theorem
`luders_rule_from_composition_consistency_note_2026-05-20` was
previously had an archived clean bounded-theorem snapshot at
criticality `medium`, with load-bearing score `4.807`. Its narrowed
scope was the textbook operator-algebraic derivation of the Lüders
state-update rule
`σ → (PσP)/Tr(PσP)` from positivity, normalization, Bayes consistency,
and compositional consistency on the one-qubit operator algebra
`M_2(ℂ)` over the `Z^3` lattice, with standard sequential-effect
composition `M_{P,E} = P E P` as the named non-derivation import.

The 2026-06-04 axiom citation-graph re-resolution migrated the parent's
stable upstream-dependency edge from
`minimal_axioms_2026-05-20` to the canonical `minimal_axioms` node
(whose `note_path` is `docs/MINIMAL_AXIOMS_2026-06-04.md`,
explicit-owner-approved per `docs/audit/AXIOM_MINIMALITY_POLICY.md`
section 6). The audit pipeline archived the prior clean snapshot under
the deps-changed reason
`deps_changed:dep_added:minimal_axioms|dep_removed:minimal_axioms_2026-05-20`,
surfacing the row for independent audit-lane handling.

This companion records, for the audit lane, that the parent's
load-bearing chain is **independent of the Record axiom** (the only
axiom-set content present in the canonical `minimal_axioms` node that
is absent from the historical `minimal_axioms_2026-05-20` content): it
uses only the Quantum axiom content (per-site `M_2(ℂ)` local algebra)
plus standard textbook operator-algebraic identities (trace cyclicity,
positivity preservation under congruence, finite-dimensional duality
between density operators and effects). Adopting the canonical
`minimal_axioms` node introduces no new content used by the parent's
derivation; the Lattice axiom content is preserved verbatim across both
memos, and the Record axiom (additive scalar record-readout
functional `I(.)`) is neither used nor invoked anywhere in the
Lüders-rule derivation. The closed-form rule
`σ → (P σ P) / Tr(P σ P)`, its (U1) positivity and (U2) normalization
corollaries, the (U4) compositional consistency check
`(σ|_{P_1})|_{P_2} = σ|_{P_2 P_1}`, and the (U3) Bayes uniqueness
argument are unchanged.

This companion is therefore audit-friendly evidence that the prior
clean verdict's substantive content survives the citation-edge
re-resolution. It is not a re-audit and does not promote status; it
documents the load-bearing-step dependency surface in
machine-checkable form so the audit lane has clean context for its
independent handling of the new minimal-axioms premise hash.

---

## Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the Lüders-rule derivation.** The
parent's load-bearing chain (Step 1 Bayes-uniqueness argument; Step 2
(U1)/(U2) corollaries; Step 3 (U4) compositional consistency; Step 4
uniqueness summary of
`LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md`) depends
only on:

1. the per-site qubit operator algebra `A_x ~= M_2(C)` (Quantum axiom
   content);
2. composition over `Λ ⊂ Z^3` via standard C*-tensor product (Lattice
   axiom content for the site set; standard finite-dimensional
   C*-tensor-product machinery for the local-algebra composition);
3. the standard state/effect trace-pairing on `A_Λ` (textbook
   operator-algebraic probability);
4. trace cyclicity and positivity preservation under congruence
   `σ → P σ P` for projections `P` on a finite-dimensional Hilbert
   space (textbook linear algebra);
5. standard sequential-effect composition `M_{P,E} = P E P` (named
   non-derivation import, explicitly admitted in the parent's
   `## Admitted inputs` section);
6. Bayes consistency `p(P then E) = p(P) · p(E | P)` on the standard
   effect-algebra structure (textbook).

None of items 1–6 use the Record axiom's additive scalar record-readout
content `I(R_1 sqcup R_2) = I(R_1) + I(R_2)`. The Record axiom adds a
strictly additive scalar functional `I(.)` on disjoint record
collections; the parent's derivation neither defines a record-readout
surface nor invokes any additive scalar functional. The Lüders rule
the parent derives is a **state-update map** (CPTP-style measurement
update on a density operator), which is structurally orthogonal to a
record-readout functional.

**(C1) is the only auditable companion observation.** The bridge from
the Lüders rule to downstream Born-derivation routes
(`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` and
related notes) and to any persistent-record realization
(`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`) remains
explicitly out of scope, exactly as in the parent note
("What this can close after audit" and "What this does not close"
sections).

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs;
- assert anything about Record-axiom content or its scope;
- re-audit `luders_rule_from_composition_consistency_note_2026-05-20`
  or any other ledger row;
- modify the audit ledger, the audit queue, or any status field;
- edit the parent note's source text in any way.

The audit lane decides whether (C1) is sufficient evidence for its
handling of the archived clean snapshot or whether a fresh per-row
audit is warranted on the new premise hash.

---

## The Record axiom is not used by the load-bearing chain

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` §"Record") says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The parent's load-bearing chain defines no record surface, asks no
question about scalar record additivity, and writes no record
functional `I(.)`. It records four lattice/operator-algebra facts on
finite-dimensional matrix algebras:

- (T1) For a rank-`r` projection `P` on `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)` and
  state `σ` (density operator) with `Tr(σ P) > 0`, the linear map
  `σ → P σ P / Tr(P σ P)` returns a density operator (positive and
  unit-trace).
- (T2) (U3) Bayes consistency `p(P then E) = p(P) · p(E | P)`, together
  with the standard sequential-effect composition
  `M_{P, E} = P E P`, forces
  `Tr(σ|_P · E) = Tr(P σ P · E) / Tr(σ · P)` for every effect `E`,
  hence `σ|_P = (P σ P) / Tr(P σ P)`.
- (T3) (U4) compositional consistency
  `(σ|_{P_1})|_{P_2} = σ|_{(P_2 P_1)}` holds for the rule of (T2),
  by direct substitution.
- (T4) Any state-update rule `σ → f(σ, P)` satisfying (U1)–(U4) on the
  standard effect-algebra structure of `M_2(ℂ)`-based finite-region
  algebras coincides with the Lüders rule.

All four statements are fixed by:

- the per-site qubit operator algebra `A_x ~= M_2(C)` (Quantum axiom
  content);
- the `Z^3` site set with standard C*-tensor-product composition over
  finite regions (Lattice axiom content + standard finite-dimensional
  C*-tensor-product machinery);
- standard trace cyclicity `Tr(A B C) = Tr(B C A) = Tr(C A B)` on
  finite-dimensional matrix algebras (textbook linear algebra);
- positivity preservation under congruence `σ ≥ 0 ⇒ P σ P ≥ 0`
  (textbook linear algebra);
- standard sequential-effect composition `M_{P,E} = P E P` (named
  non-derivation import; identical in both axiom memos);
- Bayes consistency `p(P then E) = p(P) · p(E | P)` (textbook
  probability on the operator-algebraic effect structure).

The Record axiom adds an additive scalar record-readout functional
`I(.)`. It does not modify (and is not modified by) the state-update
map `σ → (P σ P) / Tr(P σ P)`, the trace-cyclicity identities used by
the Bayes argument, the positivity-preservation property used by the
(U1) corollary, or the operator-product composition `P_2 P_1` used by
the (U4) check. The closed-form rule, the Bayes-uniqueness argument,
the (U4) check identity
`(σ|_{P_1})|_{P_2} = σ|_{P_2 P_1}`, and all derivation steps are
invariant under the axiom-set change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing arithmetic / algebraic check passes using only the
Quantum and Lattice axiom content plus standard linear-algebra and
operator-algebra identities, and a "Record-axiom counterfactual" block
confirms the resulting density operators and Bayes identities are
unchanged whether or not a Record-axiom statement is appended.

---

## Companion runner block plan

`scripts/audit_companion_luders_rule_from_composition_consistency_deps_changed_2026_06_04.py`
verifies the Record-axiom invariance of the Lüders-rule load-bearing
chain. Each block runs as an independent algebraic/arithmetic check;
nothing is hard-coded against an expected target value beyond standard
linear algebra and operator-algebra identities. The runner reports
`PASS` / `FAIL` per check; the cached output records the run.

Block 1 — Projection structure on `M_2(C)`. Constructs rank-1 and
rank-2 projections on the single-qubit space and verifies idempotence
`P^2 = P`, self-adjointness `P† = P`, and unit-trace for rank-1.

Block 2 — Density operator construction on `M_2(C)` and
`M_2(C) ⊗ M_2(C)`. Constructs several test density operators (pure
states, maximally mixed, partial mixtures, two-qubit entangled) and
verifies `σ ≥ 0` (positive eigenvalues), `σ = σ†`, and `Tr(σ) = 1`.

Block 3 — Lüders sandwich positivity (parent step 2/U1). For each test
pair `(σ, P)` from Blocks 1-2, verifies `P σ P ≥ 0` and
`Tr(P σ P) ≥ 0`. This is the (U1) corollary.

Block 4 — Lüders sandwich normalization (parent step 2/U2). For each
test pair with `Tr(P σ P) > 0`, verifies the normalized post-update
state `σ|_P = (P σ P) / Tr(P σ P)` satisfies `Tr(σ|_P) = 1`. This is
the (U2) corollary.

Block 5 — Lüders sandwich self-adjointness. Verifies
`σ|_P = (σ|_P)†` for the same test pairs.

Block 6 — Trace cyclicity identity used in (U3) derivation
(parent step 1, equation (3)). For test triples `(σ, P, E)` with `σ`
density, `P` projection, `E` effect, verifies
`Tr(σ · P E P) = Tr(P σ P · E)` to machine precision.

Block 7 — Bayes consistency identity (parent step 1, equation (4)).
For test triples with `Tr(σ · P) > 0`, verifies the chain
`Tr(P σ P · E) = Tr(σ · P) · Tr(σ|_P · E)`
that turns the Bayes rule into the Lüders form.

Block 8 — (U4) compositional consistency
(parent step 3, equation (8)). For test triples `(σ, P_1, P_2)` with
non-zero relevant probabilities, verifies
`(σ|_{P_1})|_{P_2} = (P_2 P_1) σ (P_2 P_1)† / Tr((P_2 P_1) σ (P_2 P_1)†)`
to machine precision. This is exactly the parent's (U4) check.

Block 9 — Generalized Kraus form (parent step 1 generalization). For a
random rank-1 Kraus operator `K` (not necessarily a projection),
verifies `σ → (K σ K†) / Tr(K σ K†)` is a density operator (positive,
unit-trace, self-adjoint).

Block 10 — Uniqueness argument check (parent step 4). Verifies the
"linear functional equality over all effects forces operator equality"
step numerically: takes a candidate update `σ → ρ_1` and checks that
demanding `Tr(ρ_1 · E) = Tr(ρ_target · E)` for a basis of effects
forces `ρ_1 = ρ_target`. This is the textbook duality between density
operators and effects on a finite-dimensional space.

Block 11 — Static-source scan of parent note's load-bearing sections:
zero Record-axiom usage tokens. Enumerates the phrase set
`{"I(R_1", "I(R)", "scalar record", "record functional",
"record-readout", "additive record", "additive scalar record",
"MINIMAL_AXIOMS_2026-06-04"}` over the parent's `## Claim`,
`## Setup`, `## Step 1`, `## Step 2`, `## Step 3`, `## Step 4`,
`## What this can close after audit`, `## Admitted inputs`, and
`## Risk classification` sections and confirms zero matches.

Block 12 — Static-source scan of parent note for Quantum / Lattice
axiom content. Confirms the parent's load-bearing chain explicitly
cites `M_2(ℂ)`, `Z^3`, qubit, and the per-site/region operator-algebra
construction as its lattice/operator-algebra setting.

Block 13 — Record-axiom counterfactual: identical numeric output.
Re-runs Blocks 3-8 inside an explicit "Record axiom included" outer
scope and an explicit "Record axiom not included" outer scope;
verifies the post-Lüders density operators, the trace-cyclicity
identity, the Bayes consistency identity, and the (U4) compositional
identity are identical (component-wise, to machine precision) in both
runs. The counterfactual is a tautology at the calculation level (no
Record-axiom content enters the state-update / trace-cyclicity steps),
which is precisely the substantive content of (C1).

Block 14 — Quantum / Lattice content preservation across the
historical `MINIMAL_AXIOMS_2026-05-20.md` and current
`MINIMAL_AXIOMS_2026-06-04.md` memos. Confirms the per-site `M_2(ℂ)`
algebra and `Z^3` site set used by the parent are preserved under the
new wording, and confirms the new memo's Record axiom adds an
additive scalar functional whose scope statement explicitly excludes
load-bearing bridges the parent's Lüders derivation does not use.

Block 15 — Independent recomputation of the Lüders rule via three
routes. Computes the post-update state for a single test pair via:
(a) direct sandwich `P σ P / Tr(P σ P)`; (b) spectral construction
via the projection onto the supported `+1` eigenspace; and
(c) repeated post-selection on a purification (operational route).
Verifies all three agree to machine precision.

Total: 15 blocks. The exact PASS/FAIL count is recorded in the
SHA-pinned cached runner output.

---

## Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline derives
`effective_status`), no status field changes are implied by this PR.
The audit lane decides how to handle the new premise hash; this
companion only supplies machine-checkable evidence on whether the
current minimal-axioms node (and in particular the Record axiom)
disturbs the load-bearing chain.

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the parent's
output (e.g.
`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`,
`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`, or any
specific record-formation dynamics analysis). Each downstream claim
must be examined independently against the new axiom-set premise
hash. The other rows recently invalidated under the same edge-rewrite
(notably `kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20`)
are out of scope of this companion; they are listed in the audit
queue's `deps_changed` cohort and should be examined separately as the
audit lane reaches them.

---

## Audit-ordering and integration

This companion does not migrate the parent's
`MINIMAL_AXIOMS_2026-05-20.md` source-text citation to
`MINIMAL_AXIOMS_2026-06-04.md`. Both are valid framework axiom memos;
the 2026-06-04 memo cites the 2026-05-20 memo as the "local-algebra
authority and historical source for the prior two-axiom wording." A
separate citation-migration PR (if desired) can refresh the parent
note's load-bearing-dependencies column; this companion is independent
of that text update and is content-only.

This companion's load-bearing-chain invariance observation depends only
on the Quantum and Lattice content being preserved across the two
memos — verified in Block 14 — and on the Record axiom adding a
strictly additive non-overlapping statement — confirmed by direct
reading of `MINIMAL_AXIOMS_2026-06-04.md` §"Record".

---

## References

- Parent note:
  [`LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md`](LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md)
- Archived clean snapshot:
  `docs/audit/data/audit_ledger.json` row
  `luders_rule_from_composition_consistency_note_2026-05-20`, archived
  clean bounded-theorem snapshot invalidated on 2026-06-04 by
  `deps_changed:dep_added:minimal_axioms|dep_removed:minimal_axioms_2026-05-20`
- Current framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axiom memo (still authoritative for
  local-algebra content):
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)
