# Taste-Scalar Fermion Coleman-Weinberg Isotropy: deps-restored Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dep-edge restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing algebraic chain of the parent note
[`TASTE_SCALAR_FERMION_CW_ISOTROPY_NARROW_THEOREM_NOTE_2026-05-02.md`](TASTE_SCALAR_FERMION_CW_ISOTROPY_NARROW_THEOREM_NOTE_2026-05-02.md)
(namely the binary orthogonality identity
`Σ_{s ∈ {0,1}^3} (-1)^{s_i} (-1)^{s_j} = 8 δ_{ij}` and its consequence
that the fermion Coleman-Weinberg Hessian
`∂²V_f / ∂φ_i ∂φ_j |_{φ=(v,0,0)}` is diagonal with common coefficient
`C(v)`) is intact and unchanged across the historical audit-state
transitions recorded in `docs/audit/data/audit_ledger.json` for the
claim row
`taste_scalar_fermion_cw_isotropy_narrow_theorem_note_2026-05-02`. It is
not a new theorem claim, not a status promotion, and not an attempt to
perform re-audit work. If the audit pipeline seeds this file, it is a
meta companion row; the audit lane still sets `audit_status`, and
pipeline-derived `effective_status` remains downstream of that
authority.
**Companion target:**
`taste_scalar_fermion_cw_isotropy_narrow_theorem_note_2026-05-02`
(parent note
`docs/TASTE_SCALAR_FERMION_CW_ISOTROPY_NARROW_THEOREM_NOTE_2026-05-02.md`).
**Primary runner:**
[`scripts/audit_companion_taste_scalar_fermion_cw_isotropy_hygiene_2026_06_04.py`](../scripts/audit_companion_taste_scalar_fermion_cw_isotropy_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_taste_scalar_fermion_cw_isotropy_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_taste_scalar_fermion_cw_isotropy_hygiene_2026_06_04.txt)

---

## Why this companion exists

The parent narrow theorem
`taste_scalar_fermion_cw_isotropy_narrow_theorem_note_2026-05-02` is
currently at `effective_status: unaudited`, with `load_bearing_score =
3.0` and `criticality = medium`. Its audit history in
`docs/audit/data/audit_ledger.json` (`rows[…].previous_audits`) records
two prior dispositions:

1. **2026-05-03 — `audited_clean` (`positive_theorem`),** by an
   independent codex-fresh-agent auditor; verdict rationale: "The claim
   is confined to a defined finite-dimensional binary taste block and
   the load-bearing Hessian isotropy follows by exact simultaneous
   diagonalization plus the binary orthogonality sum"; runner check
   breakdown reported `total_pass = 31`.
2. **2026-05-11 — `audited_conditional` (`bounded_theorem`),** by the
   codex-audit-loop; primary blocker
   `notes_for_re_audit_if_any = "missing_dependency_edge: add the
   admitted staggered-Dirac realization gate as a direct dependency, or
   split/update the note and runner so the audited row is only the
   abstract C^8 algebra identity."` Verdict rationale: "Issue: the
   source note's physical taste/fermion-CW framing names
   STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03 as the canonical
   open gate, but this audit row has no dependency edge to that gate;
   the current primary runner additionally fails two stale pre-retag
   scope assertions." Runner check breakdown at that audit reported
   `total_pass = 3`.

The 2026-05-11 audit identified two repair targets:

- **(R-dep)** Either split this into a purely abstract algebra note
  with an updated passing runner, **or** add the staggered-Dirac gate
  dependency and leave retained propagation blocked until that gate is
  closed.
- **(R-runner)** The registered primary runner is not current with the
  `bounded_theorem` retag — two stale `Type:** positive_theorem` and
  `target_claim_type: positive_theorem` string assertions in
  `scripts/frontier_taste_scalar_fermion_cw_isotropy_narrow.py`
  Part 1 fail against the post-retag note text.

The parent's current state on `main` shows that **(R-dep) has been
addressed**: the ledger row records
`deps = ["staggered_dirac_realization_gate_note_2026-05-03",
"minimal_axioms_2026-05-03"]`, `direct_in_degree = 2`, and the note
text explicitly records the dependency-restoration in the section
"Audit dependency repair links" and in the "Hypothesis set used
(axiom-reset 2026-05-03)" preamble. The
`effective_status_reason = "awaiting_audit"` indicates the row is
queued for fresh audit-lane handling under the
`bounded_theorem` retag.

**(R-runner) is partially unresolved.** The parent runner's Part 1
("note structure and scope discipline") still contains two stale token
assertions written against the pre-retag wording of the note:
`Type:** positive_theorem` and `target_claim_type: positive_theorem`.
Because the parent note has been retagged to
`bounded_theorem (axiom-reset retag 2026-05-03; was positive_theorem)`
and `target_claim_type: bounded_theorem`, those two assertions now
fail. A third Part-7 assertion `has no declared dependency edges`
asserts `deps == []`, which also fails post-dep-edge-restoration since
the row now has the two correct deps. The parent runner therefore
exits nonzero with three Part-1/Part-7 wording FAILs while the
load-bearing Part-2 through Part-6 algebra checks all PASS.

This companion records, for the audit lane, that **the parent's
load-bearing algebraic chain (binary orthogonality identity plus
Hessian isotropy at `φ = (v, 0, 0)`) is intact** and is independently
re-verifiable in the companion runner without modifying the parent
note or the parent runner. It documents the invalidation reason
(`missing_dependency_edge` from the 2026-05-11 conditional audit) and
the current state of each repair target. It does not perform the
runner repair (R-runner): that is a separate scoped edit on the parent
runner that requires its own PR and falls outside this companion's
no-parent-edits discipline.

---

## Scope and boundary

This companion makes three narrow auditable observations:

**(C1) Load-bearing algebraic chain is unchanged.** The parent's
load-bearing chain (Parts 2-6 of the parent runner, plus the textual
Load-bearing step) consists entirely of:

1. The eigenvalue formula `λ_s(φ) = Σ_i φ_i (-1)^{s_i}` for
   `s = (s_1, s_2, s_3) ∈ {0, 1}^3` on the simultaneous σ_x
   eigenbasis of `ℂ^8 = (ℂ^2)^{⊗3}` (algebraic identity on a finite-
   dimensional complex Hilbert space; no external authority).
2. The pointwise evaluation `λ_s(v, 0, 0)^2 = v^2` for every
   `s ∈ {0, 1}^3` (direct substitution; no external authority).
3. The binary orthogonality sum
   `Σ_{s ∈ {0, 1}^3} (-1)^{s_i} (-1)^{s_j} = 8 δ_{ij}` for every
   `(i, j) ∈ {1, 2, 3}^2` (Fourier orthogonality on
   `(ℤ/2ℤ)^3`; no external authority).
4. The bilinear-then-sum recombination
   `∂²V_f / ∂φ_i ∂φ_j |_{φ=(v,0,0)} = (2 f'(v^2) + 4 v^2 f''(v^2)) ·
   Σ_s (-1)^{s_i}(-1)^{s_j}` (chain rule plus (1)-(2); no external
   authority).
5. The closure
   `∂²V_f / ∂φ_i ∂φ_j |_{φ=(v,0,0)} = δ_{ij} · C(v)` with
   `C(v) := 8 · (2 f'(v^2) + 4 v^2 f''(v^2))` (combining (3) and
   (4); no external authority).

None of items (1)-(5) depend on (a) the parent note's claim_type
tag wording, (b) the parent note's `target_claim_type` proposal
wording, (c) the parent note's `deps` field in the ledger, or (d) the
upstream `staggered_dirac_realization_gate_note_2026-05-03` open-gate
content. Items (a)-(b) are bookkeeping strings in the parent runner's
Part-1 scope-discipline assertions; item (c) is a ledger-pipeline
field maintained by the audit pipeline; item (d) is a physical-context
admission separately tracked in the note's "Hypothesis set used"
preamble and Audit-dependency-repair-links section. The algebraic
chain (1)-(5) is independent of all four.

**(C2) Dependency-edge restoration is recorded on main.** The
2026-05-11 audit blocker (R-dep) is addressed: the current ledger row
`deps = ["staggered_dirac_realization_gate_note_2026-05-03",
"minimal_axioms_2026-05-03"]` and `direct_in_degree = 2`. The parent
note records the dependency-edge restoration in the "Audit dependency
repair links" section and the "Hypothesis set used (axiom-reset
2026-05-03)" preamble. This companion verifies (a) the ledger row's
deps field contains both expected entries and (b) the parent note's
text contains both expected dependency-link markdown citations.

**(C3) Runner staleness is documented but not repaired here.** The
2026-05-11 audit also flagged (R-runner): the parent runner's
Part-1 scope-discipline assertions and Part-7 deps-bookkeeping
assertion are written against pre-retag, pre-dep-restoration wording
and now fail. This companion documents the exact assertion strings
that fail (`Type:** positive_theorem`, `target_claim_type:
positive_theorem`, `has no declared dependency edges`), confirms the
parent runner's load-bearing Part-2 through Part-6 algebra checks all
PASS in the current note state, and explicitly does **not** perform
the runner repair. That repair is a separate scoped edit on
`scripts/frontier_taste_scalar_fermion_cw_isotropy_narrow.py` that
requires its own PR. The current companion ships under the
no-parent-edits constraint and therefore only documents (R-runner)
without attempting to fix it.

**(C1)-(C3) are the only auditable companion observations.** The
bridge from the abstract `ℂ^8 = (ℂ^2)^{⊗3}` taste-block algebraic
identity to a physical staggered-Dirac realization on a `Z^3` lattice,
to the identification of `φ_i` with physical scalar-taste shift
parameters, and to the downstream Higgs-sector / electroweak / gauge /
scalar-loop consequences remain explicitly out of scope, exactly as in
the parent note ("What this theorem does NOT close" section).

This companion does **not**:

- introduce a new minimal-axiom statement;
- change the parent's claim scope, claim type, or admitted-context
  inputs;
- re-audit
  `taste_scalar_fermion_cw_isotropy_narrow_theorem_note_2026-05-02` or
  any other ledger row;
- modify the audit ledger, the audit queue, or any status field;
- modify the parent note or the parent runner;
- promote the parent row or remove the staggered-Dirac realization
  gate's open status.

The audit lane decides whether (C1)-(C3) are sufficient evidence for
its handling of the row's `unaudited` state, or whether a fresh per-
note audit and a separate (R-runner) repair PR are warranted before
re-handling.

---

## The algebraic chain is independent of bookkeeping wording

The parent's load-bearing identity is the binary Fourier orthogonality
on `(ℤ/2ℤ)^3`:

> For every `(i, j) ∈ {1, 2, 3}^2`,
>
>     Σ_{s = (s_1, s_2, s_3) ∈ {0, 1}^3} (-1)^{s_i} (-1)^{s_j}
>       = 8 δ_{ij}.

This is the orthogonality relation for the rank-1 Walsh-Hadamard
characters `χ_i: {0, 1}^3 → {±1}`, `χ_i(s) := (-1)^{s_i}`, on the
abelian group `(ℤ/2ℤ)^3`. It is a standard discrete-Fourier identity:

- the only `i = j` contribution gives
  `Σ_s (-1)^{2 s_i} = Σ_s 1 = 8`;
- the off-diagonal `i ≠ j` contribution factorizes as
  `(Σ_{s_i ∈ {0, 1}} (-1)^{s_i}) · (Σ_{s_j ∈ {0, 1}} (-1)^{s_j}) ·
  (Σ_{s_k ∈ {0, 1}} 1) = 0 · 0 · 2 = 0`.

The Hessian isotropy

>     ∂²V_f / ∂φ_i ∂φ_j |_{φ=(v,0,0)} = δ_{ij} · C(v)

follows immediately from this orthogonality combined with the chain
rule on `V_f(φ) = Σ_s f(λ_s(φ)^2)` with
`λ_s(φ) = Σ_k φ_k (-1)^{s_k}`. None of these steps reference:

- the parent note's `claim_type` wording (`bounded_theorem` /
  `positive_theorem`);
- the parent note's `target_claim_type` proposal;
- the parent note's `deps` list in the audit ledger;
- the parent note's "Hypothesis set used" axiom-reset wording.

This independence is precisely what makes the algebra checks
auditable in this companion under the no-parent-edits constraint:
the companion runner re-derives (1)-(5) from first principles on
its own copies of the same finite-dim state vectors, never reading
the parent note's claim_type / target_claim_type / deps wording for
load-bearing input.

The companion runner's verification blocks are designed to be
independent of any future repair of the parent runner's Part-1 and
Part-7 stale wording: even if those three FAILs are fixed in a
separate PR, the companion's blocks 1-6 (algebraic) continue to PASS
on the unchanged algebraic chain, and the companion's blocks 7-12
(dependency-edge / ledger / note-text / runner-staleness observation)
continue to record the audit-state evidence as observable facts on
the current parent files.

---

## Companion runner block plan

`scripts/audit_companion_taste_scalar_fermion_cw_isotropy_hygiene_2026_06_04.py`
verifies the deps-restored hygiene observations for the parent
narrow theorem. Each block runs as an independent
numeric/algebraic/textual check; nothing is hard-coded against an
expected target value beyond standard finite-dim linear algebra and
the explicit bookkeeping facts being recorded. The runner reports
`PASS` / `FAIL` per check; the cached output records the run.

**Algebraic chain blocks (independent re-derivation, no parent-runner
re-import):**

Block 1 — Eigenvalue formula on the `(ℂ^2)^{⊗3}` σ_x eigenbasis.
For every `φ = (φ_1, φ_2, φ_3) ∈ {(1, 2, 3), (2, 0, 0), (-1/3, 7/11, 0),
(5/7, -3/13, 11/17)}` and every `s = (s_1, s_2, s_3) ∈ {0, 1}^3`,
verifies `λ_s(φ) = Σ_i φ_i (-1)^{s_i}` matches the exact
rational-arithmetic computation of the operator `H(φ) = Σ_i φ_i S_i`
acting on the explicit Walsh-Hadamard eigenvector `|s⟩` with
`S_i|s⟩ = (-1)^{s_i}|s⟩`. Confirms the parent's eigenvalue formula
on multiple test points without re-importing the parent runner's code.

Block 2 — Binary Fourier orthogonality
`Σ_s (-1)^{s_i} (-1)^{s_j} = 8 δ_{ij}`. For every
`(i, j) ∈ {1, 2, 3}^2`, computes the sum at exact integer precision
and verifies it equals `8` if `i = j` and `0` otherwise. This is the
parent's binary-orthogonality identity, re-derived independently.

Block 3 — Squared eigenvalue uniformity at `φ = (v, 0, 0)`. For
`v ∈ {1, 2, -3, 7/11, -5/13, 11/19}`, verifies
`λ_s(v, 0, 0)^2 = v^2` exactly for every `s ∈ {0, 1}^3` using rational
arithmetic. Confirms the pointwise uniformity that drives the
Hessian's common-coefficient factorization.

Block 4 — Fermion Coleman-Weinberg Hessian diagonality. For
`f ∈ {f₁(x) = x, f₂(x) = x^2, f₃(x) = x^3, f₄(x) = x + x^2 / 3}`
and `v ∈ {1, 2, 3}`, computes
`H_{ij}(v) := ∂²V_f / ∂φ_i ∂φ_j |_{φ=(v,0,0)}` at exact rational
precision using the explicit chain-rule expression
`H_{ij} = Σ_s [2 f'(λ_s^2) (-1)^{s_i + s_j} + 4 f''(λ_s^2) λ_s^2
(-1)^{s_i + s_j}]` and verifies `H_{ij}(v) = 0` for `i ≠ j` and
`H_{ii}(v) = H_{11}(v)` for every `i ∈ {1, 2, 3}`. Reproduces the
parent's Part-5 diagonality observation without re-importing.

Block 5 — Hessian common-coefficient formula `C(v) = 8 (2 f'(v^2)
+ 4 v^2 f''(v^2))`. For `f, v` as in Block 4, verifies
`H_{11}(v) = 8 (2 f'(v^2) + 4 v^2 f''(v^2))` at exact rational
precision. Reproduces the parent's Part-6 closure-factor observation.

Block 6 — Off-diagonal vanishing on a denser scan. For `f(x) = x`,
`v ∈ {1, 2, 3, 4, 5}`, and every `(i, j) ∈ {1, 2, 3}^2`, verifies the
exact rational-precision value `H_{ij}(v) = 16 δ_{ij}`. Provides a
denser numeric scan than the parent's Part-5 (which scans a single
`v = 2` only). Demonstrates the algebraic chain is robust under
parameter perturbation.

**Bookkeeping / audit-hygiene blocks:**

Block 7 — Dependency-edge restoration recorded on main. Loads
`docs/audit/data/audit_ledger.json` and verifies the row
`taste_scalar_fermion_cw_isotropy_narrow_theorem_note_2026-05-02`
has `deps` containing both
`staggered_dirac_realization_gate_note_2026-05-03` and
`minimal_axioms_2026-05-03`, and `direct_in_degree >= 2`.
Reproduces the (R-dep) restoration observation.

Block 8 — Parent note text contains both expected
dependency-link citations. Loads the parent note and verifies it
contains both markdown links
`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` and
`MINIMAL_AXIOMS_2026-05-03.md`. Reproduces the note-text-side
dependency-restoration observation.

Block 9 — Parent note explicitly records the axiom-reset retag.
Verifies the parent note's claim_type wording contains
`bounded_theorem (axiom-reset retag 2026-05-03; was positive_theorem)`
and `target_claim_type: bounded_theorem`. Reproduces the 2026-05-03
axiom-reset retag observation that underlies the (R-runner) staleness.

Block 10 — Parent runner Part-1 stale assertions are still present.
Loads the parent runner and verifies its Part-1 `required` list
literally contains the two stale strings `Type:** positive_theorem`
and `target_claim_type: positive_theorem`. Reproduces the
(R-runner) staleness observation without modifying the parent runner.

Block 11 — Parent runner Part-7 deps-bookkeeping assertion is still
present. Verifies the parent runner contains the literal assertion
`{CLAIM_ID} has no declared dependency edges` against `not
claim_deps`. Reproduces the deps-bookkeeping side of the (R-runner)
staleness without modifying the parent runner.

Block 12 — Audit ledger row records the historical audit
dispositions. Verifies the ledger row's `previous_audits` list
contains exactly two entries with `audit_status ∈ {audited_clean,
audited_conditional}`, with the `audited_conditional` entry's
`notes_for_re_audit_if_any` literally beginning with
`missing_dependency_edge:`. Confirms the audit-history evidence for
the (R-dep) blocker.

Total: 12 blocks. The exact PASS/FAIL count is recorded in the
SHA-pinned cached runner output.

---

## Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline derives
`effective_status`), no status field changes are implied by this PR.
The audit lane decides how to handle the current `unaudited` state
under the dep-edge-restored ledger row; this companion only supplies
machine-checkable evidence on (a) the load-bearing algebraic chain's
intactness, (b) the (R-dep) restoration's current ledger and
note-text state, and (c) the (R-runner) staleness as an observable
fact pending a separate runner-repair PR.

The hygiene observations here are structurally narrow: they do not
extend to any downstream claim that consumes the parent's output
(e.g. taste-scalar isotropy in the gauge-loop or scalar-loop sectors,
electroweak minimum selection, Higgs-mass splitting, Standard-Model
phenomenology). Each downstream claim must be examined independently.

---

## Audit-ordering and integration

This companion does not migrate the parent's
`MINIMAL_AXIOMS_2026-05-03.md` citations to any successor memo. The
parent note explicitly cites `MINIMAL_AXIOMS_2026-05-03.md` as its
hypothesis-set authority, and that citation is preserved unchanged.
The companion is independent of any future axiom-set memo update.

The companion's load-bearing observation depends only on:

- the binary Fourier orthogonality `Σ_s (-1)^{s_i}(-1)^{s_j} = 8 δ_{ij}`
  on `(ℤ/2ℤ)^3` — verified in Blocks 1-2;
- the chain-rule expansion of the second derivative of
  `V_f(φ) = Σ_s f(λ_s(φ)^2)` — verified in Blocks 3-5;
- the current `audit_ledger.json` row's `deps` field — verified in
  Block 7;
- the current parent note's textual content — verified in Blocks 8-9;
- the current parent runner's textual content — verified in Blocks
  10-11.

The companion's runner does not import the parent runner and does not
share state with it. The companion's algebraic blocks (1-6) are
self-contained re-derivations from first-principles linear algebra on
`(ℂ^2)^{⊗3}`. The companion's bookkeeping blocks (7-12) read the
parent note and parent runner as static text files via path-only
reads; they do not execute the parent runner.

---

## References

- Parent note:
  [`TASTE_SCALAR_FERMION_CW_ISOTROPY_NARROW_THEOREM_NOTE_2026-05-02.md`](TASTE_SCALAR_FERMION_CW_ISOTROPY_NARROW_THEOREM_NOTE_2026-05-02.md)
- Parent runner:
  [`scripts/frontier_taste_scalar_fermion_cw_isotropy_narrow.py`](../scripts/frontier_taste_scalar_fermion_cw_isotropy_narrow.py)
- Audit-history record:
  `docs/audit/data/audit_ledger.json` row
  `taste_scalar_fermion_cw_isotropy_narrow_theorem_note_2026-05-02`,
  fields `previous_audits[0]` (audited_clean, 2026-05-03) and
  `previous_audits[1]` (audited_conditional, 2026-05-11, blocker
  `missing_dependency_edge`).
- Dependency-restoration target:
  [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
- Axiom-set authority:
  [`MINIMAL_AXIOMS_2026-05-03.md`](MINIMAL_AXIOMS_2026-05-03.md)
- Audit pipeline contract:
  [`docs/audit/README.md`](audit/README.md)
- Companion shape precedent:
  [`BUSCH_POVM_EXTENSION_DEPS_CHANGED_HYGIENE_COMPANION_NOTE_2026-06-04.md`](BUSCH_POVM_EXTENSION_DEPS_CHANGED_HYGIENE_COMPANION_NOTE_2026-06-04.md)
  (sibling 2026-06-04 deps-changed / Record-axiom-invariance hygiene
  companion; this companion follows the same `claim_type=meta` /
  companion-only / no-parent-edits / SHA-pinned-runner-cache shape).
