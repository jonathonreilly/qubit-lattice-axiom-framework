# N_F Trace-Space Bounded Obstruction: Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / Record-axiom invariance evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing obstruction-localization content in
[`N_F_TRACE_SPACE_BOUNDED_OBSTRUCTION_NOTE_2026-05-07_w2binary.md`](N_F_TRACE_SPACE_BOUNDED_OBSTRUCTION_NOTE_2026-05-07_w2binary.md)
is invariant under the 2026-06-04 Record-axiom adoption. It is not a
new theorem claim, not a status promotion, and not an attempt to
perform re-audit work. If the audit pipeline seeds this file, it is a
meta companion row; the audit lane still sets `audit_status`, and
pipeline-derived `effective_status` remains downstream of that
authority.
**Companion target:** `n_f_trace_space_bounded_obstruction_note_2026-05-07_w2binary`
(parent note
`docs/N_F_TRACE_SPACE_BOUNDED_OBSTRUCTION_NOTE_2026-05-07_w2binary.md`).
**Primary companion runner:**
[`scripts/audit_companion_n_f_trace_space_bounded_obstruction_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_n_f_trace_space_bounded_obstruction_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_n_f_trace_space_bounded_obstruction_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_n_f_trace_space_bounded_obstruction_record_axiom_invariance_2026_06_04.txt)

---

## Why this companion exists

The parent note `n_f_trace_space_bounded_obstruction_note_2026-05-07_w2binary`
is an `open_gate` claim documenting an obstruction-localization analysis
on the `N_F` trace-surface admission for the `g_bare` chain. The note's
substantive content is the enumeration of eight independent
attack vectors on the binary `N_F` admission `{1/2, 1}` (V_3 trace vs
V trace), with the conclusion that none of the tested Cl(3) + Z^3
routes unconditionally close the binary to `N_F = 1/2`, and a clean
localization of the load-bearing bridge step (V8: per-site Cl(3)
bivector SU(2) = SU(2) sub of color-SU(3) on V_3).

The parent was prior-audited on 2026-05-28 as `audited_clean` (claim
type `open_gate`) and was subsequently archived on 2026-05-29 with
`invalidation_reason = dep_weakened:cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02:retained->unaudited`.
That dep has since been re-promoted to `retained` (`audited_clean`,
`positive_theorem`).

The 2026-06-04 framework axiom adoption updated
`MINIMAL_AXIOMS_2026-05-20.md` to `MINIMAL_AXIOMS_2026-06-04.md`
(Lattice + Quantum + **Record**, explicit-owner-approved per
`docs/audit/AXIOM_MINIMALITY_POLICY.md` §6). This companion provides
machine-checkable evidence to the audit lane that the parent's
load-bearing obstruction content is independent of the Record axiom:
the parent's eight-vector enumeration, structural obstruction at V8,
and conditional-V_3 selection chain use only Cl(3) + Z^3 primitives
and standard finite-dimensional Lie/Clifford-algebra content, and
none of them invokes a scalar record functional `I(.)`, record
additivity, or any Record-axiom-only content.

This companion is therefore narrow Record-axiom-invariance evidence
for the parent's substantive obstruction content. It does not
re-establish the prior `audited_clean` verdict (which was invalidated
by a dep weakening, not by the axiom adoption); the audit lane decides
independently whether to honor or re-test the parent on the current
axiom-set premise hash and the now-re-promoted dep.

---

## Honest scoping: invalidation reason vs companion scope

This companion is narrower than the standard "Record-axiom-induced
re-audit cohort" companion (e.g.,
[`YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`](YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md)),
because the parent here was not invalidated by the Record-axiom
adoption. The invalidation reason on the latest archived audit is

```text
invalidation_reason = dep_weakened:cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02:retained->unaudited
```

(dep-weakened class), not

```text
invalidation_reason = axiom_premise_changed:minimal_axioms:<old>-><new>
```

(axiom-premise-changed class). Re-audit readiness on the new axiom-set
premise is therefore necessary but not sufficient for re-honoring the
prior verdict; the dep-weakened state has to be examined separately by
the audit lane. The dep
`cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` is now
`audited_clean` / `positive_theorem` / `effective_status=retained` on
`origin/main` (machine-readable in `docs/audit/data/audit_ledger.json`).

This companion's narrow contribution is the Record-axiom-invariance
observation on the parent's load-bearing obstruction content. The
audit lane is the authority for the parent's re-audit decision and
final status; this companion is read-only evidence for that decision.

---

## Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the parent's load-bearing
obstruction content.** The parent's load-bearing step
(eight-vector enumeration + V8 bridge-step obstruction localization +
conditional V_3 selection chain) depends only on:

1. the Cl(3) per-site local algebra (Quantum axiom in
   `MINIMAL_AXIOMS_2026-06-04.md`; equivalently A1 in the historical
   `MINIMAL_AXIOMS_2026-05-20.md` wording);
2. the `Z^3` lattice site set (Lattice axiom in
   `MINIMAL_AXIOMS_2026-06-04.md`; equivalently A2 in the historical
   wording);
3. standard finite-dimensional Lie-algebra identities (Gell-Mann
   generators, `Tr_R(T_a T_b)` canonical normalization on irreducible
   carriers, `d^abc` symbols, Killing rigidity);
4. standard tensor-product index counting (V_color = V_3 (x) V_fiber;
   V_lepton = V_antisym (x) V_fiber).

None of items 1-4 use the Record axiom's additive scalar
record-readout content. The parent contains no record functional
`I(.)`, no record additivity statement, no record collection, and no
Record-axiom citation. Adopting the Record axiom adds a strictly
additive non-overlapping statement (per
`MINIMAL_AXIOMS_2026-06-04.md` §"Record": "When a finite
record-readout surface is specified, its scalar record functional is
additive over disjoint record collections"). This statement is
neither used by nor consumed by the parent's obstruction-localization
analysis, the parent's eight-vector enumeration, or the parent's
conditional V_3 selection chain. The parent's eight numeric facts
(verified by `scripts/cl3_n_f_v3_trace_check_2026-05-07_w2binary.py`)
are unchanged.

**(C1) is the only auditable companion observation.** The
status-changing question of whether the dep-weakened re-promotion of
`cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` (now
`retained`) is sufficient to re-honor the prior `audited_clean`
verdict is explicitly out of scope here.

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs (the parent stays `open_gate`; this companion stays `meta`);
- assert anything about Record-axiom content or its downstream scope;
- close the binary admission `N_F in {1/2, 1}` to `N_F = 1/2`;
- re-audit `n_f_trace_space_bounded_obstruction_note_2026-05-07_w2binary`
  or any other ledger row;
- modify the audit ledger, the audit queue, or any status field.

The audit lane decides whether (C1), together with the now-re-promoted
dep, is sufficient evidence to re-honor the previous judicial verdict
or whether a fresh per-site audit is warranted on the new premise
hash plus the re-promoted dep.

---

## The Record axiom is not used by the parent's load-bearing step

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` §"Record") says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The parent's load-bearing step is the eight-vector enumeration with
the V8 bridge-step obstruction localization. None of those eight
vectors defines a record surface, asks a scalar record additivity
question, or writes a record functional `I(.)`. Each vector tests a
structural identification at the level of:

- `Tr_{V_3}(T_a T_b) = (1/2) δ_{ab}` on the irreducible color carrier
  V_3 (V1, V3, V8);
- `Tr_V(T_a^V T_b^V) = δ_{ab}` on the full 8-dim taste cube V (V1,
  V4);
- the fiber-multiplicity ratio `Tr_V / Tr_{V_3} = 2 = dim(V_fiber)`
  (V1, V4);
- anomaly cancellation as a matter-content question, not a
  trace-surface question (V2);
- per-site Cl(3) bivector half-Pauli `T_k = σ_k / 2` with
  `Tr_{C^2}(T_a T_b) = (1/2) δ_{ab}` (V8);
- anti-fundamental rep content (V5);
- holonomy on V_3 (V6);
- the `dim(Z^3) = N_c = 3` structural split (V7).

These eight checks use only group-theoretic, Clifford-algebraic, and
index-counting content. The Record axiom adds a scalar record
functional. It does not modify (and is not modified by) any of the
trace formulas, the Gell-Mann generators, the per-site Cl(3) bivector
half-Pauli normalization, or the V_3/V_color/V_lepton projector
algebra used in the parent. The eight-vector enumeration and the V8
bridge-step obstruction localization are invariant under the
axiom-set change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing arithmetic and structural fact from the parent
reproduces using only Lattice + Quantum content and standard
finite-dimensional algebra, a "Record-axiom counterfactual" block
confirms that the obstruction-localization conclusions are unchanged
whether or not a Record-axiom statement is appended, and a
static-source scan of the parent confirms zero Record-axiom usage
tokens in its load-bearing section.

---

## Companion runner block plan

`scripts/audit_companion_n_f_trace_space_bounded_obstruction_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the parent's obstruction
content. Each block runs as an independent numeric/algebraic check;
nothing is hard-coded against an expected target value beyond standard
finite-dimensional algebra. The runner reports `PASS` / `FAIL` per
check; the cached output records the run.

Block 1 — V_3 canonical Gell-Mann trace. Verifies
`Tr_{V_3}(T_a T_b) = (1/2) δ_{ab}` for all (a,b) pairs using explicit
Gell-Mann matrices `T_a = lambda_a / 2`. Uses only Quantum-axiom
content (Cl(3)/M_2(C) local algebra applied at the V_3 = 3D
irreducible color carrier level via the cited
`CL3_COLOR_AUTOMORPHISM_THEOREM`).

Block 2 — V full-taste trace. Verifies
`Tr_V(T_a^V T_b^V) = δ_{ab}` on V = C^8 with `T_a^V = T_a (x) I_2`
extended by zero on the antisym lepton block. Index counting only;
no Record-axiom content appears.

Block 3 — Fiber-multiplicity ratio. Verifies
`Tr_V / Tr_{V_3} = 2 = dim(V_fiber)` exactly. Confirms the parent's
"binary admission" structural fact.

Block 4 — Projector algebra. Builds the projectors `P_3`, `P_antisym`,
`P_color = P_3 (x) I_2`, `P_lepton = P_antisym (x) I_2`, and verifies
the parent's "T_a^V vanishes on V_lepton" structural identity:
`T_a^V . P_lepton = 0` and `P_lepton . T_a^V = 0` for all eight a.

Block 5 — Anti-fundamental distinguishability. Verifies that the
3-bar generators `-T_a^*` are not equal to the 3 generators `T_a`
(SU(3) is complex, V_3 is not self-dual). Confirms V5 structural
content from the parent.

Block 6 — d-symbol fiber inflation. Computes `d^abc` on V_3 and on V,
verifies the parent's `d_V = 2 . d_{V_3}` ratio fact (V2 structural
content). Famous `d_{118} = 1/sqrt(3)` reproduced on V_3.

Block 7 — Per-site Cl(3) bivector trace. Verifies the V8 input
`Tr_{C^2}(T_a T_b) = (1/2) δ_{ab}` for `T_k = sigma_k / 2`
(Pauli halves) using the explicit Cl(3) bivector half-Pauli matrices.
This is the per-site Cl(3) side of the V8 bridge step.

Block 8 — SU(2) sub of SU(3) on V_3 trace. Verifies that the SU(2)
subalgebra of color-SU(3) generated by `(T_1, T_2, T_3)` on V_3 has
`Tr_{V_3 sub}(T_a T_b) = (1/2) δ_{ab}`, matching the per-site
bivector trace numerically. This is the V8 bridge target.

Block 9 — V8 bridge-step obstruction localization. Records the
structural fact that Blocks 7 and 8 produce numerically matching
half-trace values but on algebraically distinct C^2 spaces (per-site
Cl(3) irrep vs SU(2)-sub-of-color V_3 block). The structural
identification "per-site C^2 = (1,2)-block C^2" is not derived by
this block; the parent explicitly leaves it as the open structural
bridge.

Block 10 — Static-source scan: zero Record-axiom usage tokens in
parent's load-bearing section. Reads the parent note's load-bearing
sections (eight attack vectors + structural obstruction + verification
table) and verifies zero matches of Record-axiom usage tokens
(`I(R_1`, `I(R)`, `scalar record`, `record functional`,
`record-readout`, `additive record`, `additive scalar record`,
`MINIMAL_AXIOMS_2026-06-04`). Confirms that the parent's load-bearing
content does not invoke the Record axiom.

Block 11 — Record-axiom counterfactual on numeric outputs. Re-runs
Blocks 1-3 and 7-8 inside an explicit "Record axiom is asserted"
outer scope and an explicit "Record axiom is not asserted" outer
scope; verifies that the eight load-bearing numeric values are
identical in both runs. The counterfactual is a tautology at the
calculation level (no Record-axiom content enters the trace, index,
or Pauli steps), which is precisely the substantive content of (C1).

Block 12 — Quantum and Lattice axiom-content preservation across
memos. Verifies that the historical 2026-05-20 memo (qubit /
`M_2(C)` / Cl(3,0) wording for A1; `Z^3` lattice wording for A2) and
the current 2026-06-04 memo (named Quantum + Lattice axioms) preserve
the local-algebra and lattice-site content the parent uses. Verifies
that the 2026-06-04 memo's Record-axiom scope statement explicitly
excludes the load-bearing bridges the parent would have needed if it
were using Record content (log-det, source/action, observable bridges,
etc.) — i.e., the new memo's own scope statement is consistent with
the (C1) invariance observation.

Total: 12 blocks, with the exact PASS/FAIL count recorded in the
SHA-pinned cached runner output. All checks PASS to machine precision.

---

## Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline
derives `effective_status`), no status field changes are implied by
this PR. The audit lane decides whether to re-honor the prior
judicial verdict (now that the dep is re-promoted and the new
axiom-set premise hash applies) or whether a fresh per-site audit is
warranted; this companion only supplies machine-checkable evidence
on whether the new Record axiom disturbs the parent's load-bearing
content.

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the parent's
output. Each downstream claim must be examined independently against
the new axiom-set premise hash. Since the parent here was invalidated
by `dep_weakened` rather than `axiom_premise_changed`, the parent is
not part of the 32-row axiom-premise-changed cohort listed in the
audit queue; the dep-weakened resolution is a separate audit-lane
question.

---

## Audit-ordering and integration

This companion does not migrate the parent's
`MINIMAL_AXIOMS_2026-05-03.md` citation to
`MINIMAL_AXIOMS_2026-06-04.md`. The 2026-05-03 axiom memo is the
parent's historical authority; the 2026-06-04 memo is the current
authority. The local-algebra and lattice-site content the parent
uses (Cl(3)/M_2(C); Z^3) is preserved across all three memo versions
2026-05-03 -> 2026-05-20 -> 2026-06-04. A separate citation-migration
PR (if desired) can refresh the parent note's references; this
companion is independent of that text update and is content-only.

This companion's load-bearing-step invariance observation depends
only on the Quantum and Lattice content being preserved across the
memos — verified in Block 12 — and on the Record axiom adding a
strictly additive non-overlapping statement, confirmed by direct
reading of `MINIMAL_AXIOMS_2026-06-04.md` §"Record".

---

## References

- Parent note:
  [`N_F_TRACE_SPACE_BOUNDED_OBSTRUCTION_NOTE_2026-05-07_w2binary.md`](N_F_TRACE_SPACE_BOUNDED_OBSTRUCTION_NOTE_2026-05-07_w2binary.md)
- Parent runner:
  `scripts/cl3_n_f_v3_trace_check_2026-05-07_w2binary.py`
- Prior judicial verdict snapshot:
  `docs/audit/data/audit_ledger.json` row
  `n_f_trace_space_bounded_obstruction_note_2026-05-07_w2binary`,
  `previous_audits[-1]` (`audited_clean`, `open_gate`, 2026-05-28,
  archived 2026-05-29 with
  `invalidation_reason=dep_weakened:cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02:retained->unaudited`)
- Re-promoted dep:
  [`CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md`](CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md)
  (currently `audited_clean`, `positive_theorem`,
  `effective_status=retained`)
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for local-algebra
  content): [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Sister Record-axiom-invariance companion (axiom-premise-changed
  cohort example):
  [`YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`](YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md)
