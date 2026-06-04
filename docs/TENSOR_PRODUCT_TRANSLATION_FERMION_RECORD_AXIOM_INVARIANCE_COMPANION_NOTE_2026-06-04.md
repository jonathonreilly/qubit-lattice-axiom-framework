# Tensor-Product Translation / Fermion Operator Bridge: Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing operator-algebra identities (T1)-(T4) of
[`TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md`](TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md)
are invariant under the 2026-06-04 Record-axiom adoption. It is not a new
theorem claim, not a status promotion, and not an attempt to perform
re-audit work. If the audit pipeline seeds this file, it is a meta
companion row; the audit lane still sets `audit_status`, and
pipeline-derived `effective_status` remains downstream of that authority.
**Companion target:** `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`
(parent note
`docs/TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md`).
**Primary companion runner:**
[`scripts/audit_companion_tensor_product_translation_fermion_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_tensor_product_translation_fermion_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_tensor_product_translation_fermion_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_tensor_product_translation_fermion_record_axiom_invariance_2026_06_04.txt)

---

## Why this companion exists

The parent narrow theorem
`tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`
was previously audit-loop-resolved on 2026-05-26 as `audited_clean`
(positive_theorem, load-bearing-step class A) under cross-family
confirmation (two independent codex-gpt-5.5 audit sessions, one
`fresh_context`, one `cross_family`-style follow-up). The narrowed claim
scope was:

> Tensor-permutation translations on finite periodic tensor-product
> qubit blocks are unitary, obey the translation group law, translate
> the per-site ladder operators by conjugation, and commute with
> `Q_total = sum_x a_x^† a_x`.

The 2026-06-04 framework axiom update from `MINIMAL_AXIOMS_2026-05-20.md`
to `MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum + Record;
explicit-owner-approved per
[`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
section 6) changed the stable `minimal_axioms` premise-node note-hash
from `1d36a556` to `b8848fc8`. The audit pipeline correctly invalidated
the prior `audited_clean` snapshot, returning the row to unaudited
effective status.

This companion records, for the audit lane, that the parent's load-bearing
chain is **independent of the Record axiom**: it uses only the Lattice
(`Z^3` cubic site set + translation structure) and Quantum (per-site
one-qubit operator algebra, `M_2(C)` / `Cl(3,0)`) axiom content, plus
standard tensor-product Fock-space and single-mode per-site Pauli fermion
constructions. Adopting the Record axiom adds a strictly additive scalar
record-readout statement, which is neither used nor invoked anywhere in
the four operator-algebra identity proofs. The matrix entries verifying
`T_a T_a^† = I`, `T_a T_b = T_{a+b}`, `T_a a_x T_a^† = a_{x+a}`, and
`[T_a, Q_total] = 0` are unchanged.

This companion is therefore audit-friendly evidence that the prior
clean cross-confirmed verdict's substantive content survives the
axiom-set change. It is not a re-audit and does not promote status; it
documents the load-bearing-step dependency surface in machine-checkable
form so the audit lane can decide whether to honor or re-test the prior
judicial verdict on the new premise hash.

---

## Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of identities (T1)-(T4).** The parent's
four load-bearing identities depend only on:

1. the per-site dim-two complex factor `C²_x` supplied by the Quantum
   axiom (one-qubit operator algebra `A_x ≅ M_2(C)` / equivalently
   `Cl(3,0)` real algebra);
2. the standard ladder matrices `σ_+`, `σ_-` on `C²_x`;
3. the cyclic-shift / translation structure on the finite block
   `Λ ⊂ Z^3` supplied by the Lattice axiom (cubic adjacency, periodic
   identification on `Λ`);
4. the standard finite tensor-product Fock-space construction
   `H_Λ = ⊗_{x ∈ Λ} C²_x`;
5. the standard single-mode per-site Pauli realization
   `a_x = I_{Λ \ {x}} ⊗ σ_-^{(x)}`;
6. elementary linear algebra (basis permutation, Kronecker product,
   adjoint).

None of items 1-6 invoke a record functional `I(·)`, a record collection,
a record additivity statement, or any Record-axiom content. The Record
axiom (`MINIMAL_AXIOMS_2026-06-04.md` §"Record") adds a separate,
non-overlapping additive scalar functional over disjoint record
collections; that statement is silent about local operator-algebra
identities on the tensor-product Fock space.

**(C1) is the only auditable companion observation.** The downstream
consumer notes that cite the parent bridge for translation covariance of
fermion bilinears (notably `HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md`,
which cites identities (T3) and (T4)) remain in scope of their own
independent ledger rows; this companion does not assert anything about
their Record-axiom dependence.

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs (tensor-product Fock space; single-mode per-site Pauli fermion
  construction; periodic identification on `Λ`);
- assert anything about Record-axiom content or its scope;
- re-audit `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`
  or any other ledger row;
- modify the audit ledger, the audit queue, or any status field.

The audit lane decides whether (C1) is sufficient evidence to re-honor
the previous judicial verdict or whether a fresh per-site audit is
warranted on the new premise hash.

---

## The Record axiom is not used by the load-bearing identities

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` §"Record") says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The parent's load-bearing identities (T1)-(T4) define no record surface,
ask no question about scalar record additivity, and write no record
functional `I(·)`. They are matrix identities on the explicit
finite-dimensional tensor-product Fock space `H_Λ = ⊗_{x ∈ Λ} C²_x`:

- **(T1) Unitarity** — proved by showing the basis-permutation rule
  (eq. 2 of the parent) preserves the orthonormal basis inner product:
  `⟨T_a b | T_a b'⟩ = ⟨b | b'⟩` by the bijection of label-shifts on `Λ`.
- **(T2) Group law** — proved by composing two cyclic-shift label
  bijections on `Λ`: `(x − a) − b = x − (a + b)`.
- **(T3) Fermion-operator covariance** — proved by tracking
  `σ_-^{(x)}` action through the basis-permutation `T_a`, with the
  selection content `δ_{b_{x+a},1}` matching on the two sides.
- **(T4) Charge conservation** — proved by applying (T3) to each
  summand of `Q_total = Σ_x a_x^† a_x` and relabeling the finite-sum
  index by the bijection `y := x + a` on `Λ`.

The operator content (`a_x` ladder matrices, `T_a` permutation, `Q_total`
finite sum), the basis-state action (`σ_-|1⟩=|0⟩`, `σ_-|0⟩=0`), and the
finite-sum relabeling are fixed by:

- finite-dimensional linear algebra on the explicit basis
  `{⊗_x |b_x⟩_x}` (Quantum-axiom-supplied per-site `C²_x`);
- the bijection of cyclic shifts on `Λ` (Lattice-axiom-supplied `Z^3`
  translation structure, with the standard finite-volume periodic
  identification on `Λ`);
- the standard tensor-product Fock-space construction (definitional
  mathematical infrastructure, no admitted physics convention).

The Record axiom adds an additive scalar record functional over
disjoint record collections. It does not modify (and is not modified
by) the per-site complex Hilbert structure, the cyclic-shift label
bijection on `Λ`, or the elementary linear algebra of the tensor-
product Fock space. So the matrix entries verifying (T1)-(T4) are
invariant under the axiom-set change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing matrix equality holds at exact precision using only
Lattice + Quantum content and standard tensor-product Fock algebra, and
a "Record-axiom counterfactual" block confirms that the matrix entries
are unchanged whether or not a Record-axiom statement is appended to
the framework axiom set.

---

## Companion runner block plan

`scripts/audit_companion_tensor_product_translation_fermion_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the parent's load-bearing
identities (T1)-(T4). Each block runs as an independent exact-symbolic
check on a small finite block; nothing is hard-coded against an expected
target value beyond standard tensor-product linear algebra. The runner
reports `PASS` / `FAIL` per check; the cached output records the run.

Block 1 — Quantum-axiom-only construction of `H_Λ` for `N = 2`. Builds
`H_Λ = C² ⊗ C²` as an exact sympy `Matrix`, constructs `a_0`, `a_1` as
single-mode per-site Pauli realizations, and verifies the per-site
adjoint relation `(a_x)^† = a_x^†` (eq. 1 of the parent). Uses only
Quantum-axiom content; no Record functional invoked.

Block 2 — Lattice-axiom-only construction of `T_1` for `N = 2`. Builds
the tensor-permutation cyclic shift `T_1` as an exact permutation
matrix from the basis-relabeling rule (eq. 2 of the parent) on the
length-2 periodic block. Uses only Lattice-axiom content (cubic
adjacency / periodic identification on `Λ`); no Record functional
invoked.

Block 3 — (T1) Unitarity at `N = 2`. Verifies `T_1 T_1^† = I_4` and
`T_1^† T_1 = I_4` at exact precision. Pure Lattice + Quantum content.

Block 4 — (T2) Group law at `N = 2`. Verifies `T_1 T_1 = T_2 = I_4`
(period-2 cyclic group). Pure Lattice content.

Block 5 — (T3) Fermion covariance at `N = 2`. Verifies
`T_1 a_0 T_1^† = a_1`, `T_1 a_1 T_1^† = a_0`, and the corresponding
adjoint identities, at exact precision. Pure Lattice + Quantum content.

Block 6 — (T4) Charge conservation at `N = 2`. Builds
`Q_total = a_0^† a_0 + a_1^† a_1` and verifies `T_1 Q_total T_1^† = Q_total`
(equivalently `[T_1, Q_total] = 0`). Pure Lattice + Quantum content.

Block 7 — (T1)-(T4) at `N = 3`. Reproduces unitarity, group law, fermion
covariance, and charge conservation for every cyclic-shift `T_a`,
`a ∈ {0, 1, 2}` on the 8-dimensional space. Confirms that the
identities are not artifacts of the smallest block.

Block 8 — (T2) full group law at `N = 4`. Verifies `T_a T_b = T_{(a+b) mod 4}`
for every `(a, b) ∈ {0, 1, 2, 3}²` on the 16-dimensional space.

Block 9 — (T3) on the 2D `2 × 2` block. Verifies fermion covariance
for both independent lattice generators (axis-1 shift and axis-2 shift),
confirming the bridge applies to higher-dimensional `Z^d` translations.

Block 10 — Record-axiom counterfactual. Wraps Blocks 3-6 (the four
load-bearing identities at `N = 2`) inside two outer scopes:
"Record axiom is asserted" and "Record axiom is not asserted". Verifies
that the matrix entries (and therefore the identity verdicts) are
bitwise identical in both runs. The counterfactual is a tautology at
the matrix-arithmetic level (no Record-axiom content enters basis
permutation, Kronecker product, adjoint, or finite-sum relabeling),
which is precisely the substantive content of (C1).

Block 11 — Static-source scan of parent note's structural calculation.
Verifies that the auditable core of the parent note does not invoke a
record functional `I(·)`, a record additivity statement, a record
collection, or a Record-axiom citation. The check enumerates the
phrase set `{"I(R_1", "I(R)", "scalar record", "record functional",
"record-readout", "additive record", "additive scalar record",
"MINIMAL_AXIOMS_2026-06-04"}` over the load-bearing section of the
parent note and confirms zero matches inside the auditable core.

Block 12 — Quantum/Lattice content preservation across the historical
2026-05-20 and current 2026-06-04 minimal-axioms memos. Verifies that
the parent note's load-bearing premises (per-site one-qubit operator
algebra on `C²_x`, and the `Z^3` cubic-lattice translation structure)
are preserved in the new memo, and that the Record axiom is a third,
additive, non-overlapping statement.

Total: 12 blocks, with the exact PASS/FAIL count recorded in the
SHA-pinned cached runner output.

---

## Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline derives
`effective_status`), no status field changes are implied by this PR.
The audit lane decides whether to re-honor the prior judicial verdict
on the new premise hash; this companion only supplies machine-checkable
evidence on whether the new Record axiom disturbs the load-bearing
identities (T1)-(T4).

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the parent's
output. Each downstream claim (e.g., the hopping-bilinear hermiticity
theorem) must be examined independently against the new axiom-set
premise hash. Those rows are out of scope of this companion.

---

## Audit-ordering and integration

This companion does not migrate the parent's
`MINIMAL_AXIOMS_2026-05-20.md` citations to `MINIMAL_AXIOMS_2026-06-04.md`.
Both are valid framework axiom memos; the 2026-06-04 memo cites the
2026-05-20 memo as the "local-algebra authority and historical source
for the prior two-axiom wording." A separate citation-migration PR (if
desired) can refresh the parent note's `Cited authorities` block; this
companion is independent of that text update and is content-only.

This companion's load-bearing-identity invariance observation depends
only on the Quantum and Lattice content being preserved across the two
memos — verified in Block 12 — and on the Record axiom adding a strictly
additive non-overlapping statement — confirmed by direct reading of
`MINIMAL_AXIOMS_2026-06-04.md` §"Record".

---

## References

- Parent note:
  [`TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md`](TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md)
- Parent runner:
  `scripts/tensor_product_translation_fermion_operator_bridge_check_2026_05_25.py`
- Prior judicial verdict snapshot:
  `docs/audit/data/audit_ledger.json` row
  `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`,
  `previous_audits[-1]`
  (`audited_clean`, positive_theorem, load-bearing-step class A,
  cross-confirmed by two independent codex-gpt-5.5 sessions on
  2026-05-25 and 2026-05-26, archived 2026-06-04 with
  `invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`)
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for local-algebra
  content): [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)

```yaml
claim_type_author_hint: meta
claim_scope: "Audit-companion evidence: the load-bearing operator-algebra identities (T1) unitarity, (T2) group law, (T3) fermion-operator covariance, and (T4) charge conservation of `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25` use only Lattice + Quantum axiom content (per-site one-qubit C^2_x factor and Z^3 cyclic-shift translation) plus standard tensor-product Fock-space and single-mode per-site Pauli fermion constructions; they invoke no Record functional, no record collection, and no Record-axiom content. Matrix entries verifying (T1)-(T4) are identical under both 'Record axiom asserted' and 'Record axiom not asserted' outer scopes. This is audit-friendly evidence, not a re-audit or status promotion."
upstream_dependencies:
  - minimal_axioms
admitted_context_inputs:
  - tensor-product Fock space H_Lambda = otimes_x C^2_x (definitional)
  - single-mode per-site Pauli fermion construction a_x = I otimes sigma_-^{(x)} (definitional)
  - periodic identification on finite block Lambda (standard finite-volume lattice convention)
```
