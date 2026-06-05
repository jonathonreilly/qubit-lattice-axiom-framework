# Busch POVM Extension on the Qubit-Lattice Effect Algebra: deps-changed Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dep-edge restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing chain of the parent note
[`BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
(namely the application of Busch's 2003 POVM-additive extension of
Gleason's theorem to the qubit-lattice effect algebra
`E(H_Λ) = { E ∈ M_{2^|Λ|}(ℂ) : 0 ≤ E ≤ 𝟙 }`, concluding
`m(E) = Tr(σ·E)` for a unique density matrix `σ` on `H_Λ`) is invariant
under the 2026-06-04 `minimal_axioms` premise-node note-hash bump from
`1d36a556` to `b8848fc8` caused by Record-axiom adoption. It is not a new
theorem claim, not a status promotion, and not an attempt to perform
re-audit work. If the audit pipeline seeds this file, it is a meta
companion row; the audit lane still sets `audit_status`, and
pipeline-derived `effective_status` remains downstream of that authority.
**Companion target:** `busch_povm_extension_on_qubit_lattice_narrow_theorem_note_2026-05-20`
(parent note `docs/BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`).
**Primary companion runner:**
[`scripts/audit_companion_busch_povm_extension_deps_changed_hygiene_2026_06_04.py`](../scripts/audit_companion_busch_povm_extension_deps_changed_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_busch_povm_extension_deps_changed_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_busch_povm_extension_deps_changed_hygiene_2026_06_04.txt)

---

## Why this companion exists

The parent narrow theorem
`busch_povm_extension_on_qubit_lattice_narrow_theorem_note_2026-05-20`
was previously audit-loop-resolved on 2026-05-23 as `audited_clean`
(`positive_theorem`, criticality leaf) by a single per-site auditor verdict on
the narrowed scope:

> For every nonempty finite `Λ ⊂ Z³`, every countably additive
> POVM-additive probability measure `m: E(H_Λ) → [0, 1]` on the qubit-lattice
> effect algebra `E(H_Λ) = { E ∈ M_{2^|Λ|}(ℂ) : 0 ≤ E ≤ 𝟙 }` has the unique
> density-matrix representation `m(E) = Tr(σ · E)`, including the single-qubit
> `dim H_Λ = 2` case outside Gleason's projection-lattice theorem. This is
> Busch 2003 / CFMR 2004 standard mathematical-physics content applied to
> the framework's specific effect algebra.

The 2026-06-04 framework axiom update from `MINIMAL_AXIOMS_2026-05-20.md`
to `MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum + Record;
explicit-owner-approved per `docs/audit/AXIOM_MINIMALITY_POLICY.md`
section 6) changed the stable `minimal_axioms` premise-node note-hash
from `1d36a556` to `b8848fc8`. The audit pipeline correctly invalidated
the prior `audited_clean` snapshot via
`invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`,
returning the row to unaudited effective status. The parent's
`deps_changed:dep_added:minimal_axioms` edge is Record-bearing only
through the additive-scalar-record content the new memo adds; the
Lattice and Quantum content it inherits is unchanged from the
predecessor memo.

This companion records, for the audit lane, that the parent's
load-bearing chain is **independent of the Record axiom**: it uses only
the Lattice axiom content (`Z³` site set) and the Quantum axiom content
(per-site `M_2(ℂ)` qubit algebra) for the substrate identification
`H_Λ = ⊗_{x ∈ Λ} ℂ²`, `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ) ≅ M_{2^|Λ|}(ℂ)`, plus
the standard textbook POVM-additive-extension argument of Busch 2003 /
CFMR 2004 on a finite-dimensional complex Hilbert space of dimension
`≥ 2` (effect-algebra linear extension, finite-dim Riesz
representation, normalization). Adopting the Record axiom adds a
strictly additive scalar record-readout statement
`I(R_1 ⊔ R_2) = I(R_1) + I(R_2)`, which is neither used nor invoked
anywhere in the POVM-additive Born-form calculation. The numeric and
algebraic outputs `m(E) = Tr(σ · E)` for every density matrix `σ` and
every POVM element `E` are unchanged.

This companion is therefore audit-friendly evidence that the prior
clean verdict's substantive content survives the axiom-set change. It
is not a re-audit and does not promote status; it documents the
load-bearing-chain dependency surface in machine-checkable form so the
audit lane can decide whether to honor or re-test the prior verdict on
the new premise hash.

---

## Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the Busch POVM-extension chain.** The
parent's load-bearing chain (Claim and Steps 1-4 of
`BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`)
depends only on:

1. the `Z³` site set restricted to a finite `Λ` (Lattice axiom content);
2. the per-site qubit algebra `A_x ≅ M_2(ℂ)` and the standard tensor
   product `H_Λ = ⊗_x ℂ²`, `A_Λ = ⊗_x M_2(ℂ) ≅ M_{2^|Λ|}(ℂ)` (Quantum
   axiom content);
3. the POVM effect-algebra definition `E(H_Λ) = { E ∈ A_Λ : 0 ≤ E ≤ 𝟙 }`
   and POVM-partition condition `Σ_i E_i = 𝟙` (textbook
   POVM / effect-algebra structure);
4. Busch's 2003 POVM-additive extension theorem on `dim H ≥ 2`
   (cited textbook mathematical physics: linear extension on the
   effect algebra; finite-dim positive linear functional ↔ density
   matrix via Riesz representation; normalization `m(𝟙) = 1` fixes
   `Tr σ = 1`).

None of items 1-4 use the Record axiom's additive scalar
record-readout content `I(R_1 ⊔ R_2) = I(R_1) + I(R_2)`. POVM
σ-additivity over POVM partitions is a probabilistic axiom on the
effect algebra; it is strictly stronger than projection-lattice
σ-additivity, and structurally disjoint from scalar record additivity
on disjoint record collections. The two concepts have different
domains (POVM elements vs. record collections), different range types
(probability measure vs. additive scalar functional), and different
linear-extension targets (linear functional on `M_d(ℂ)_sa` vs.
additive functional on a measurable-set algebra). Both are "additivity"
statements in name only.

**(C1) is the only auditable companion observation.** The bridge from
the finite-region Born form `m(E) = Tr(σ · E)` to a quasi-local
inductive-limit normal state on the UHF algebra `A = ⊗_x M_2(ℂ)`, to
the identification of `σ` with the pre-record reference state, and to
the rest of the Born derivation chain remain explicitly out of scope,
exactly as in the parent note ("What this does not close" section).

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs (Busch 2003 cited as named non-derivation standard content;
  finite-dim Riesz representation and standard probability axioms);
- assert anything about Record-axiom content or its scope;
- re-audit
  `busch_povm_extension_on_qubit_lattice_narrow_theorem_note_2026-05-20`
  or any other ledger row;
- modify the audit ledger, the audit queue, or any status field.

The audit lane decides whether (C1) is sufficient evidence to re-honor
the previous verdict or whether a fresh per-site audit is warranted on
the new premise hash.

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
functional `I(.)`. It records the application of Busch's 2003
POVM-additive extension theorem to the qubit-lattice effect algebra:

- (B1) The finite-region Hilbert space is `H_Λ = ⊗_{x ∈ Λ} ℂ²` with
  `dim H_Λ = 2^|Λ| ≥ 2`, and the operator algebra is
  `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ) ≅ M_{2^|Λ|}(ℂ)` (Lattice + Quantum axiom
  content; standard tensor product of finite-dim Hilbert spaces /
  matrix algebras).
- (B2) The POVM effect algebra is
  `E(H_Λ) := { E ∈ A_Λ : 0 ≤ E ≤ 𝟙 }`, the set of positive operators
  bounded by the identity. A POVM is `{E_i} ⊂ E(H_Λ)` with
  `Σ_i E_i = 𝟙` (standard effect-algebra structure; textbook).
- (B3) A POVM-additive probability measure is `m: E(H_Λ) → [0, 1]`
  satisfying `m(0) = 0`, `m(𝟙) = 1`, and σ-additivity over countable
  POVM partitions (M1-M3; standard probability axioms on an effect
  algebra).
- (B4) Busch 2003 (refined by CFMR 2004): on any complex Hilbert space
  with `dim H ≥ 2`, every POVM-additive probability measure is of the
  form `m(E) = Tr(σ · E)` for a unique density matrix `σ` (cited
  textbook mathematical physics).
- (B5) Applying (B4) to (B1)-(B3): for any nonempty finite `Λ`,
  `m(E) = Tr(σ · E)` with unique `σ` on `H_Λ`.

All five items are fixed by:

- the `Z³` site set (Lattice axiom content);
- the per-site `M_2(ℂ)` qubit algebra and standard tensor product
  (Quantum axiom content);
- the standard POVM / effect-algebra definitions on a finite-dim
  Hilbert space (textbook quantum measurement theory);
- Busch 2003 / CFMR 2004 POVM-additive extension theorem (textbook
  mathematical physics; not re-derived in the parent);
- finite-dimensional Riesz representation of positive linear
  functionals on `M_d(ℂ)` as `Tr(σ · )` for positive `σ` (textbook
  C*-algebra theory).

The Record axiom adds an additive scalar record functional `I(.)`. It
does not modify (and is not modified by) the POVM effect algebra
`E(H_Λ)`, the POVM-additivity condition on probability measures, the
Busch / CFMR extension theorem, or the finite-dim Riesz
representation. So the conclusion `m(E) = Tr(σ · E)` is invariant
under the axiom-set change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing arithmetic / linear-algebra check passes using only
Lattice + Quantum axiom content plus standard textbook POVM /
effect-algebra / Riesz-representation identities, and a "Record-axiom
counterfactual" block confirms that the conclusion `m(E) = Tr(σ · E)`
holds identically under both "Record axiom asserted" and "Record axiom
not asserted" outer scopes.

---

## Companion runner block plan

`scripts/audit_companion_busch_povm_extension_deps_changed_hygiene_2026_06_04.py`
verifies the Record-axiom invariance of the Busch POVM-extension
load-bearing chain. Each block runs as an independent
numeric/algebraic check; nothing is hard-coded against an expected
target value beyond standard finite-dim linear algebra and the cited
textbook POVM / effect-algebra structure. The runner reports `PASS` /
`FAIL` per check; the cached output records the run.

Block 1 — Substrate dimensions. For every `|Λ| ∈ {1, 2, 3}` verifies
`dim H_Λ = 2^|Λ|` (parent's substrate identification, Quantum + Lattice
axiom content only). Confirms in particular the load-bearing
single-site `dim H_Λ = 2` case that Gleason's projection-lattice
theorem cannot supply.

Block 2 — POVM effect-algebra membership. Constructs random Hermitian
operators on `H_Λ` for `|Λ| = 1, 2`, projects each onto
`E(H_Λ) = { E : 0 ≤ E ≤ 𝟙 }`, and verifies the resulting `E` satisfies
`0 ≤ E ≤ 𝟙` (eigenvalue bounds), `E = E*`, and `E ∈ M_{2^|Λ|}(ℂ)`.

Block 3 — POVM partition closure. Constructs explicit POVMs (Pauli-X,
Pauli-Z eigenprojector pairs; tetrahedron / SIC-POVM on dim 2; uniform
projective POVMs on dim 4) and verifies `Σ_i E_i = 𝟙` exactly. Confirms
the POVM-partition axiom is satisfiable on the parent's substrate.

Block 4 — POVM-additive probability measure: random density matrices.
Generates random density matrices `σ` on `H_Λ` for `|Λ| = 1, 2` and
verifies `m(E) := Tr(σ · E)` satisfies `m(E) ∈ [0, 1]` for every random
POVM element `E ∈ E(H_Λ)`. Spot-checks the parent's
density-matrix → probability-measure direction (the easy direction in
Busch's theorem).

Block 5 — Probability normalization `m(𝟙) = 1`. For every random
density matrix `σ` on `H_Λ` verifies `Tr(σ · 𝟙) = Tr(σ) = 1`.
Reproduces (M2) for the density-matrix induced measure.

Block 6 — Probability of zero effect `m(0) = 0`. For every random `σ`
verifies `Tr(σ · 0) = 0`. Reproduces (M1).

Block 7 — POVM-additivity over partitions. Generates random POVMs
`{E_i}_{i=1}^n ⊂ E(H_Λ)` (multiple `n ∈ {2, 3, 4}`) for `|Λ| = 1, 2`
and verifies `Σ_i Tr(σ · E_i) = Tr(σ · 𝟙) = 1` to machine precision.
Reproduces (M3) for the density-matrix induced measure on every
POVM partition.

Block 8 — Riesz representation on finite-dim `M_d(ℂ)`. For random
positive linear functionals `φ` on the self-adjoint sector of
`M_d(ℂ)` with `d ∈ {2, 4, 8}` (built by `φ(X) := Tr(σ · X)` for
random positive trace-1 `σ`), verifies uniqueness of `σ` reconstruction
via the Hilbert-Schmidt inner product:
`σ = Σ_a φ(B_a) · B_a` where `{B_a}` is the orthonormal Hermitian
Pauli-string basis of `M_d(ℂ)`. Reproduces the inverse direction of
Busch's theorem on the parent's substrate.

Block 9 — Static-source scan of parent note: zero Record-axiom usage
tokens in the load-bearing sections. Enumerates the phrase set
`{"I(R_1", "I(R)", "scalar record", "record functional",
"record-readout", "additive record", "additive scalar record",
"MINIMAL_AXIOMS_2026-06-04"}` over the parent's load-bearing
sections ("Setup", "Step 1", "Step 2", "Step 3", "Step 4",
"Claim") and confirms zero matches. Additionally confirms that the
load-bearing sections explicitly cite Lattice / Quantum content
(`Z^3`, `M_2(ℂ)`, `ℂ²`, `dim H_Λ = 2^|Λ|`).

Block 10 — Record-axiom counterfactual: identical numeric output.
Re-runs Blocks 4-7 inside an explicit "Record axiom asserted" outer
scope and an explicit "Record axiom not asserted" outer scope; verifies
the load-bearing arithmetic outputs (`Tr(σ · E)` values, partition
sums, normalization) are identical in both runs. The counterfactual is
a tautology at the calculation level (no Record-axiom content enters
the POVM / linear-algebra / trace steps), which is precisely the
substantive content of (C1).

Block 11 — Lattice + Quantum content preservation across the
historical 2026-05-20 and current 2026-06-04 minimal-axioms memos.
Confirms the parent's load-bearing substrate identification
(`Z^3` site set, per-site `M_2(ℂ)` qubit algebra) is preserved word-
for-word under the new memo wording, and that the Record axiom is a
separate non-overlapping additive scalar statement that does not
disturb the substrate.

Block 12 — Four-route cross-check on `m(E) = Tr(σ · E)`. For a fixed
test density matrix `σ` and a fixed test POVM element `E` on
`dim H_Λ = 4` (`|Λ| = 2`), computes `m(E)` four ways: (i) direct
`Tr(σ · E)`; (ii) eigenexpansion `Σ_a p_a ⟨a|E|a⟩` for `σ = Σ_a p_a |a⟩⟨a|`;
(iii) Pauli-string basis expansion `(1/d) Σ_α c_α(σ) c_α(E)` with
real Pauli-string coefficients; (iv) POVM partition `m(E) + m(𝟙 - E) = 1`.
Verifies all four routes agree to machine precision.

Total: 12 blocks. The exact PASS/FAIL count is recorded in the
SHA-pinned cached runner output.

---

## Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline derives
`effective_status`), no status field changes are implied by this PR.
The audit lane decides whether to re-honor the prior verdict on the new
premise hash; this companion only supplies machine-checkable evidence
on whether the new Record axiom disturbs the load-bearing chain.

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the parent's
output (e.g. the Born-rule-from-Gleason-Busch derivation chain, the
persistent-record-as-Kraus identification, the pre-record reference
state identification, the Lüders sequential-product bridge). Each
downstream claim must be examined independently against the new
axiom-set premise hash. The other rows recently axiom-invalidated
under the same hash change are out of scope of this companion; they
are listed in the audit queue's `axiom_premise_changed` cohort and
should be examined separately as the audit lane reaches them.

---

## Audit-ordering and integration

This companion does not migrate the parent's
`MINIMAL_AXIOMS_2026-05-20.md` citations to
`MINIMAL_AXIOMS_2026-06-04.md`. Both are valid framework axiom memos;
the 2026-06-04 memo cites the 2026-05-20 memo as the "local-algebra
authority and historical source for the prior two-axiom wording." A
separate citation-migration PR (if desired) can refresh the parent
note's load-bearing-dependencies section; this companion is
independent of that text update and is content-only.

This companion's load-bearing-chain invariance observation depends
only on the Lattice and Quantum content being preserved across the
two memos — verified in Block 11 — and on the Record axiom adding a
strictly additive non-overlapping statement — confirmed by direct
reading of `MINIMAL_AXIOMS_2026-06-04.md` §"Record".

---

## References

- Parent note:
  [`BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
- Prior verdict snapshot:
  `docs/audit/data/audit_ledger.json` row
  `busch_povm_extension_on_qubit_lattice_narrow_theorem_note_2026-05-20`,
  `previous_audits[-1]` (`audited_clean`, `positive_theorem`, leaf,
  single per-site auditor verdict, 2026-05-23, archived 2026-06-04 with
  `invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`)
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for local-algebra
  content): [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Cited textbook upstream (named non-derivation, parent's "Admitted
  inputs"): Busch 2003 *Phys. Rev. Lett.* 91, 120403; Caves-Fuchs-
  Manne-Renes 2004 *Found. Phys.* 34, 193; finite-dim C*-algebra
  Riesz-representation theorem
