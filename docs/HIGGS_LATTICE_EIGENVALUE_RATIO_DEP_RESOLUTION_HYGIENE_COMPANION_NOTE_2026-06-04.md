# Higgs Lattice Eigenvalue Ratio: Dep-Resolution Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dep-resolution hygiene evidence)
**Status:** companion-only — supplies audit-friendly evidence about the
parent
[`HIGGS_LATTICE_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`](HIGGS_LATTICE_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md)
in two narrow respects: (a) the historical `dep_weakened` event cited
the deprecated dep
[`G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md`](G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md),
which the parent **no longer declares** as a dependency (the 2026-05-28
parent repair replaced it with two retained-grade 2026-05-03 sister
theorems plus a retained one-hop authority for `u_0`); and (b) the
parent's load-bearing algebra (`R_lattice = 1/(4 u_0²)` at `N_taste=16`)
is mechanically demonstrated by the parent's own runner
[`scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py`](../scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py)
via exact `sympy.Rational`/symbolic computation and explicit Euclidean
Clifford matrix construction, **without** querying any dep's audit
grade. This is not a new theorem claim, not a status promotion, and
not an attempt to perform re-audit work. If the audit pipeline seeds
this file, it is a meta companion row; the audit lane still sets
`audit_status`, and the pipeline-derived `effective_status` remains
downstream of that authority.
**Companion target:** `higgs_lattice_eigenvalue_ratio_narrow_theorem_note_2026-05-02`
(parent note
[`docs/HIGGS_LATTICE_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`](HIGGS_LATTICE_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md)).
**Primary companion runner:**
[`scripts/audit_companion_higgs_lattice_eigenvalue_ratio_dep_resolution_2026_06_04.py`](../scripts/audit_companion_higgs_lattice_eigenvalue_ratio_dep_resolution_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_higgs_lattice_eigenvalue_ratio_dep_resolution_2026_06_04.txt`](../logs/runner-cache/audit_companion_higgs_lattice_eigenvalue_ratio_dep_resolution_2026_06_04.txt)

This is an audit-friendly meta companion: the parent's load-bearing
algebraic identity (per-taste curvature `W''(0)/N_tot = 1/(4 u_0²)`
matching `R_lattice = 4/(u_0² N_taste)` at `N_taste=16`) is exactly
re-verified by the parent's own runner over symbolic `sympy` and
exact `Fraction` arithmetic, with the Clifford identity
`D_taste² = d·I` **derived** by explicit Euclidean Cl(4) matrix
construction (4 gamma matrices, anticommutator verification, sum-of-
squares identity), and with `N_taste = 16 = 2^d` and `N_tot = 48`
derived as elementary structural counts. No audit-status field of any
declared dependency is queried by the parent's runner. The companion
records the substance-vs-grade separation as machine-checkable
evidence; it does not re-audit the parent and does not promote status.

---

## 0. Why this companion exists

The parent's prior audit history records the chain

```text
audited_clean (2026-05-02, codex-gpt-5 fresh-context)
    invalidated by dep_weakened:g_bare_canonical_convention_narrow_theorem_note_2026-05-02:retained_bounded->unaudited
  → audited_conditional (2026-05-11)
    invalidated by dep_weakened:g_bare_canonical_convention_narrow_theorem_note_2026-05-02:retained_bounded->unaudited
  → audited_conditional (2026-05-22)
  → audited_conditional (2026-05-25)
    invalidated by dep_weakened:g_bare_constraint_vs_convention_theorem_note_2026-05-03:retained_bounded->unaudited
  → audited_conditional (2026-05-27)
    invalidated by runner_hash_changed:7ced0fd6->91c94aab
  → audited_conditional (2026-05-28)
  → unaudited (current, awaiting re-audit)
```

The companion's two narrow observations are:

> **(N1)** The historical `dep_weakened` invalidations cite either
> `g_bare_canonical_convention_narrow_theorem_note_2026-05-02` (rounds
> 1-2) or `g_bare_constraint_vs_convention_theorem_note_2026-05-03`
> (round 3). The former is **no longer declared** as a dependency on
> the parent's current `origin/main` head: the 2026-05-28 parent
> repair replaced it with the two retained-grade 2026-05-03 sister
> theorems, wired a retained-bounded one-hop authority for `u_0`, and
> grounded the framework Clifford generator structure in a retained-
> pending-chain row. The latter (`g_bare_constraint_vs_convention_*`)
> is currently `retained_bounded` on `origin/main`.

> **(N2)** The parent's *runner* — which is what mechanically
> demonstrates the substantive `R_lattice = 1/(4 u_0²)` claim — does
> not query any dep's audit grade at all (see §3). The load-bearing
> algebra reduces, on the runner side, to exact `sympy.Rational`
> arithmetic and explicit Euclidean Cl(4) matrix construction, plus
> elementary structural counts (`N_taste = 2^d = 16`, `N_tot =
> N_c · N_sites = 48`).

The honest-stop question is then exactly:

> Does the parent's substantive claim load-bear on the *audit grade*
> of any current dep (which can be re-weakened by future audit-lane
> activity) — or only on the *algebraic substance* (exact symbolic
> identity plus derived Clifford matrix identity plus elementary
> counts) that the parent's own runner re-verifies block-for-block,
> independently of any dep grade?

This companion records that the second reading is the one supported by
the parent's runner and note text. The parent's runner constructs the
four Euclidean gamma matrices directly via `sympy.Matrix` /
`TensorProduct`, verifies the Clifford anticommutator algebra by
matrix arithmetic, builds the symmetric taste-Dirac element and
verifies `D_taste² = d·I` exactly, derives `N_taste = 2^d = 16` as
the spin⊗taste hypercube dimension, and computes the per-taste
generating-functional curvature `W''(0)/N_tot = 1/(4 u_0²)` and the
declared lattice ratio `R_lattice = 4/(u_0² · N_taste)` by exact
symbolic differentiation — all without referencing any dep's audit
field. The remaining ledger checks in Part 6 of the parent's runner
verify only that the *declared* dependency note rows exist as
graph-visible audit ledger entries, not that they hold any particular
audit grade.

This companion is therefore audit-friendly evidence that the
substantive content of the parent survives the prior dep-grade events,
and that the historical specific dep cited in the `dep_weakened`
invalidation that the task targeted (the deprecated 2026-05-02
canonical convention note) is no longer in the parent's current
declared dependency set. It is not a re-audit and does not promote
status; it documents the load-bearing-step dependency surface in
machine-checkable form so the audit lane can decide whether to honor
or re-test the prior treatment in light of the parent's repaired dep
surface.

---

## 1. Parent recap and prior audit grade

The parent
[`HIGGS_LATTICE_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`](HIGGS_LATTICE_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md)
asserts the bounded narrow-theorem claim

> Given the declared graph-first SU(3) gauge surface, the Wilson
> canonical convention `g_bare = 1` (retained via the two 2026-05-03
> sister theorems), the Cl(3) Clifford identity `D_taste² = d·I` at
> mean-field factorization with `N_taste = 16` taste eigenvalues, the
> dimensionless lattice generating-functional curvature ratio is
> `R_lattice ≡ 4 / (u_0² · N_taste) = 1 / (4 u_0²)` at `N_taste = 16`,
> where `u_0` is the mean-link parameter.

with explicit scope discipline: the narrow theorem **does not** claim
that `R_lattice` equals `(m_H/v)²`, **does not** fix the numerical
value of `u_0`, **does not** derive `m_H = v/(2 u_0)`, and **does not**
claim a Standard Model Higgs-mass prediction.

The parent's prior `audited_clean` snapshot (2026-05-02,
`codex-fresh-context`, `auditor_confidence=high`) recorded
`load_bearing_step_class = B`, `chain_closes = true`, and
`chain_closure_explanation`:

> The derivation closes as a narrow algebraic theorem from
> retained/admitted inputs: the structural counts, Clifford eigenvalue
> magnitude, mean-field scaling, generating-functional curvature, and
> `N_taste = 16` substitution are sufficient. No hidden physical
> Higgs-matching bridge is needed for the stated lattice-side ratio.

The most recent archived snapshot (2026-05-28,
`fresh-agent-Boyle-019e6ce4-...`, `auditor_confidence=high`) recorded
`audited_conditional` with `load_bearing_step_class = A` and
`runner_check_breakdown = {A: 33, B: 0, C: 0, D: 0, total_fail: 0,
total_pass: 33}`, and the closure explanation

> The displayed algebra and runner checks close exactly: `W''/N_tot`
> equals `1/(4 u_0²)`, matching `R_lattice`. The retained one-hop
> rows cover the scoped SU(3) and `g_bare` surfaces, but the
> Clifford/staggered identity `D_taste²=d I` and mean-field
> factorization `U_ab → u_0 δ_ab` are load-bearing admitted premises,
> not retained one-hop theorem rows or registered Tier-A admissions in
> this packet.

That snapshot's offered repair allowed retained one-hop coverage or
explicit-admission status for the Clifford and mean-field premises.
The parent's 2026-05-28 in-note repair already addresses this exact
remark by **deriving** the Clifford identity directly in the runner
(Part 3, explicit Euclidean Cl(4) construction) and by wiring `u_0`
to the retained-bounded
[`u0_plaquette_quartic_derivation_narrow_theorem_note_2026-05-17`](U0_PLAQUETTE_QUARTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17.md);
the mean-field factorization is named as the explicit defining
hypothesis of the truncation regime, not an admission of an exact
identity. This companion does not re-audit those repairs; it records
that the substantive algebra is mechanically demonstrated by the
parent's runner independently of any dep audit grade.

---

## 2. Invalidation cause and current state

The audit ledger records, on the most relevant earlier rounds, the
invalidation reason cited by the task

```text
previous_audits[*].invalidation_reason =
    dep_weakened:g_bare_canonical_convention_narrow_theorem_note_2026-05-02:retained_bounded->unaudited
```

and a later

```text
previous_audits[3].invalidation_reason =
    dep_weakened:g_bare_constraint_vs_convention_theorem_note_2026-05-03:retained_bounded->unaudited
```

plus

```text
previous_audits[4].invalidation_reason =
    runner_hash_changed:7ced0fd6->91c94aab
```

These invalidations moved the parent from `audited_clean` /
`audited_conditional` back down the status chain via dep-grade
propagation events (rounds 1-3) and a runner-hash refresh (round 4).
None of them changed the underlying mathematical content of the
parent's load-bearing algebra. The current ledger state is

| Field | Value |
|---|---|
| `claim_type` | `bounded_theorem` |
| `intrinsic_status` | `unaudited` |
| `effective_status` | `unaudited` |
| `effective_status_reason` | `awaiting_audit` |
| `load_bearing_score` | `3.807` |
| `criticality` | `medium` |
| `direct_in_degree` | `2` |
| `max_descendant_status` | `audit_in_progress` |
| `runner_check_breakdown` (last archived) | `{A: 33, B: 0, C: 0, D: 0, total_pass: 33}` |

The parent's *current* declared deps and their `origin/main` audit
grades:

| Dep | `intrinsic_status` | `effective_status` |
|---|---|---|
| `graph_first_su3_integration_note` | `retained` | `retained` |
| `g_bare_rescaling_freedom_removal_theorem_note_2026-05-03` | `retained_bounded` | `retained_bounded` |
| `g_bare_constraint_vs_convention_theorem_note_2026-05-03` | `retained_bounded` | `retained_bounded` |
| `u0_plaquette_quartic_derivation_narrow_theorem_note_2026-05-17` | `retained_bounded` | `retained_bounded` |
| `clifford_chirality_dimension_narrow_theorem_note_2026-05-10` | `retained_pending_chain` | `retained_pending_chain` |

The deprecated dep cited by the rounds 1-2 `dep_weakened` invalidations,
`g_bare_canonical_convention_narrow_theorem_note_2026-05-02`, is
**no longer in this list** — the parent's 2026-05-28 repair replaced
it with the two `2026-05-03` `g_bare_*` sister theorems plus the
retained-bounded `u_0` authority plus the retained-pending-chain
Clifford-chirality dimension row. All five current declared deps are
retained-grade on `origin/main`.

This companion therefore uses **both** standard hygiene-companion
angles. First (the "dep replaced" angle): the historical deprecated
dep is no longer declared, so the rounds 1-2 `dep_weakened` event
references a dep the parent does not currently depend on. Second (the
"parent does not load-bear on the dep grade" angle): the parent's
substantive `R_lattice = 1/(4 u_0²)` claim is mechanically demonstrated
by the parent's own runner via exact symbolic computation that never
queries any dep audit field. This companion does **not** assert the
deprecated dep has been restored; it has not.

---

## 3. Substance-vs-grade separation

The narrow auditable observations in this companion are:

**(C1) The deprecated dep cited by the historical rounds 1-2
`dep_weakened` invalidations is no longer declared by the parent.**
On `origin/main`, the parent's ledger row `deps` field is

```text
[
  "graph_first_su3_integration_note",
  "g_bare_rescaling_freedom_removal_theorem_note_2026-05-03",
  "g_bare_constraint_vs_convention_theorem_note_2026-05-03",
  "u0_plaquette_quartic_derivation_narrow_theorem_note_2026-05-17",
  "clifford_chirality_dimension_narrow_theorem_note_2026-05-10"
]
```

The deprecated id
`g_bare_canonical_convention_narrow_theorem_note_2026-05-02`
is not present. The parent note text (`docs/HIGGS_LATTICE_...`) does
cite the deprecated note **only** as a plain-text historical pointer
(under "Cross-references"), explicitly disclaimed as

> a plain-text reader pointer, not a markdown-link load-bearing
> dependency; the load-bearing `g_bare` content is now carried by the
> two retained 2026-05-03 sister theorems listed above.

Companion runner Block 3 verifies the deprecated id is absent from
the parent ledger row's `deps` field, and Block 4 verifies the
historical-pointer disclaimer is present in the parent note text.

**(C2) The parent's load-bearing substantive algebra does not
load-bear on the *audit grade* of any current dep.** The parent's
runner
[`scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py`](../scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py)
mechanically demonstrates the equality `R_lattice = 4/(u_0² · N_taste)
= 1/(4 u_0²)` at `N_taste = 16` via:

- Part 2: derive `N_c = 3`, `N_sites = 2^4 = 16`, `N_taste = N_sites`,
  `d = 4`, `N_tot = N_c · N_sites = 48` as elementary structural
  counts;
- Part 3: construct the four Euclidean `Cl(4)` gamma matrices as
  `σ_1 ⊗ σ_i` (`i = 1,2,3`) and `σ_2 ⊗ I_2`, verify the Clifford
  anticommutator algebra `{γ_μ, γ_ν} = 2 δ_μν · I` by exact
  `sympy.Matrix` arithmetic, verify `Σ_μ γ_μ² = d · I = 4 · I`, build
  `D_taste = Σ_μ γ_μ` and verify `D_taste² = d · I = 4 · I` exactly,
  and conclude `|λ_taste| = sqrt(d) = 2`;
- Part 4: at mean field `U_{ab} → u_0 · δ_{ab}` (the named truncation
  hypothesis), `|λ_full| = 2 u_0`, so `W(J) = (N_tot / 2) ·
  log(J² + 4 u_0²)` and `W''(0) = N_tot / (4 u_0²)` by exact symbolic
  differentiation;
- Part 5: `R_lattice = 4 / (u_0² · N_taste) = 1 / (4 u_0²)` at
  `N_taste = 16` and `W''(0) / N_tot = 1/(4 u_0²)` by exact symbolic
  simplification.

The runner's *only* ledger-side checks (Part 6) verify that the
declared dep note rows exist in the audit ledger as graph-visible
entries, plus that the parent row itself is not effective-retained
before independent audit. The runner does not query, cite, or consume
any dep's `audit_status`, `intrinsic_status`, `effective_status`, or
`effective_status_reason` field for use in any load-bearing algebraic
step.

The companion records this separation by:

1. Re-running the parent's runner on the current `origin/main` head
   and confirming all checks pass with the exact-symbolic identity
   `R_lattice = 1/(4 u_0²)` verified at the runner level (Block 1);
2. Re-deriving `N_taste = 2^d = 16`, `N_tot = N_c · N_sites = 48`,
   `R_lattice = 4 / (u_0² · 16) = 1/(4 u_0²)`, `W''(0) = N_tot /
   (4 u_0²) = 12/u_0²`, and `W''/N_tot = 1/(4 u_0²)` directly in
   this companion runner via exact `sympy` arithmetic (Block 2);
3. Confirming via static source-scan that
   [`scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py`](../scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py)
   contains **zero** references to dep audit-status fields used as
   load-bearing inputs to any algebraic step (the runner does read
   the ledger for dep-existence checks in Part 6 only) (Block 3);
4. Confirming via dep-set scan on the live `origin/main` audit ledger
   that the deprecated dep id
   `g_bare_canonical_convention_narrow_theorem_note_2026-05-02` is
   **not** in the parent row's `deps` field (Block 4);
5. Confirming via static source-scan that the parent note carries the
   historical-pointer disclaimer for the deprecated note (no
   load-bearing markdown link) (Block 5);
6. Counterfactual confirmation: re-executing the parent's runner on
   the current `origin/main` head (which is exactly the post-dep-
   weakening state, with all 5 current deps at retained-grade) and
   confirming identical pass count (Block 6);
7. Re-deriving the Clifford identity `D_taste² = d · I` at `d = 4`
   directly in this companion runner via an independent explicit
   Euclidean Cl(4) construction (Block 7);
8. Live-ledger check of current dep statuses: all 5 current deps are
   retained-grade on `origin/main`, and the deprecated dep cited by
   the historical rounds 1-2 `dep_weakened` event is not in the
   parent's current dep set (Block 8);
9. No-claim gate preservation: the companion declares
   `claim_type=meta`, disclaims status promotion, and disclaims any
   physical Higgs-mass / SM matching identification (Block 9).

These are static and dynamic facts about the parent's runner, the
parent's note, and the parent row's `deps` field in the live audit
ledger; they do not depend on the audit lane's grade decisions.

---

## 4. Substance-unchanged assertion

The parent's runner FINAL TOTAL on the current `origin/main` head is

```text
TOTAL: PASS=40, FAIL=0
```

with the load-bearing algebraic identities verified by exact symbolic
computation:

- `Σ_μ γ_μ² = d · I = 4 · I` (Part 3, derived);
- `D_taste² = d · I = 4 · I` and `|λ_taste| = sqrt(d) = 2` (Part 3,
  derived);
- `W''(0) = N_tot / (4 u_0²) = 12 / u_0²` (Part 4, exact symbolic
  differentiation);
- `R_lattice = 4 / (u_0² · N_taste) = 1 / (4 u_0²)` at `N_taste = 16`
  (Part 5, exact symbolic simplification);
- `W''(0) / N_tot = 1 / (4 u_0²)` matching `R_lattice` (Part 5).

This matches both prior `audited_clean` and prior `audited_conditional`
snapshots' recorded `load_bearing_step` text. The parent note text,
runner code, and runner outputs reflect the 2026-05-28 in-note repair
that knocks down the prior admissions (Clifford derived in runner,
`u_0` wired to retained one-hop authority). The mathematical content
of the parent's load-bearing chain is unchanged; only the audit
lane's grade has moved.

The substantive bounded claim of the parent is therefore unchanged,
and the parent's runner continues to mechanically demonstrate it. The
audit lane retains exclusive authority to decide whether the prior
audited treatment can be honored under the parent's current
five-retained-dep surface or must be re-audited from scratch; the
present companion only provides the machine-checkable evidence above
to support that decision.

---

## 5. What this companion does NOT do

This companion explicitly does **not**:

- claim a new theorem;
- promote the parent's `effective_status` or `audit_status`;
- modify the parent note text, the parent's runner, or any dep note or
  dep runner;
- claim that the deprecated dep
  [`G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md`](G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md)
  has been restored to any prior grade (it has not);
- assert that the parent's bounded scope is the only correct reading;
- close the parent's explicitly excluded physical-matching step
  `R_lattice = (m_H/v)²` (that remains in the lattice→physical
  matching cluster obstruction);
- derive the numerical value of `u_0` (its tadpole definition
  `u_0 = ⟨P⟩^{1/4}` is retained via the wired authority; the number
  requires the separate plaquette evaluation);
- derive `m_H = v/(2 u_0)` (separate full theorem);
- weigh in on dep-resolution policy beyond the parent / dep pair named
  here;
- back-fill or rebut any prior auditor verdict; the audit lane sets
  `audit_status` independently.

This companion's narrow auditable observations are exactly (C1) and
(C2) in §3.

---

## 6. Audit-lane handoff

The audit lane decides whether and how to re-audit the parent under
its current 5-retained-dep surface. The present companion supplies:

- block-level static and dynamic evidence that the historical
  deprecated dep cited by the rounds 1-2 `dep_weakened` invalidation
  is no longer in the parent's declared dependency set;
- block-level static and dynamic evidence that the parent's
  substantive `R_lattice = 1/(4 u_0²)` algebra is mechanically
  demonstrated by the parent's own runner with no audit-status
  dependency on any current dep;
- a verification that the parent's runner continues to pass with
  `PASS = 40, FAIL = 0` at the current `origin/main` head with all
  five current deps at retained-grade;
- a static source scan that confirms the parent's runner does not use
  any dep audit-status field as a load-bearing input to any algebraic
  step (Part 6's checks are dep-existence-only, not dep-grade);
- a static source scan that confirms the parent note carries the
  historical-pointer disclaimer for the deprecated note (no
  load-bearing markdown link);
- a live-ledger dep-set scan confirming the five current deps are
  retained-grade and the deprecated dep is not declared;
- a small set of self-checks (independent Clifford identity
  re-derivation, exact-symbolic ratio re-derivation, exact-symbolic
  curvature re-derivation, no-claim gate preservation) that exercise
  the substantive content of the parent independent of any dep
  audit-status field.

If the audit lane chooses to re-honor the prior audited treatment of
the parent under the present dep surface, this companion records the
basis on which that decision can be made. If the audit lane chooses
to re-audit from scratch, this companion does not block that path; it
only documents the parent's substance-vs-grade dependency surface.

This companion is `claim_type=meta`, scope `audit_companion`. It is
not a status change.
