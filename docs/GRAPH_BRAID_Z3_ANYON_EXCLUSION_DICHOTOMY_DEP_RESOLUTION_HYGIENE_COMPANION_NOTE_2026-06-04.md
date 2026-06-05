# Graph-Braid Z^3 Anyon-Exclusion Dichotomy: Dep-Resolution Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dep-resolution hygiene evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
parent
[`GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md`](GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md)
does not load-bear on the specific *audit grade* of the weakened dep
[`STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md`](STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md)
— a dep that is *explicitly named non-load-bearing* in the parent note's
own dependency-classification block and that contributes no proof input
to any of `(C1)`-`(C4)` in the parent. The parent's substantive
content is verified independently by the parent's own runner
[`scripts/graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.py`](../scripts/graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.py)
(SCORECARD: PASS=25 FAIL=0 on the current `origin/main` head) using
only exact integral linear algebra (Smith normal form over `Z`) plus
exact graph algorithms (networkx planarity / connectivity), with the
**single** retained framework dep
[`CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md`](CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md)
cited only inside `(C4)` (which combines the first-quantized dichotomy
with the retained per-site dim-2 to remove the free / infinite-tower
boson).
This is not a new theorem claim, not a status promotion, and not an
attempt to perform re-audit work. If the audit pipeline seeds this
file, it is a meta companion row; the audit lane still sets
`audit_status`, and the pipeline-derived `effective_status` remains
downstream of that authority.
**Companion target:** `graph_braid_z3_anyon_exclusion_dichotomy_narrow_theorem_note_2026-05-29`
(parent note
[`docs/GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md`](GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md)).
**Primary runner:**
[`scripts/audit_companion_graph_braid_z3_anyon_exclusion_dichotomy_dep_resolution_2026_06_04.py`](../scripts/audit_companion_graph_braid_z3_anyon_exclusion_dichotomy_dep_resolution_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_graph_braid_z3_anyon_exclusion_dichotomy_dep_resolution_2026_06_04.txt`](../logs/runner-cache/audit_companion_graph_braid_z3_anyon_exclusion_dichotomy_dep_resolution_2026_06_04.txt)

This is an audit-friendly meta companion: the parent's load-bearing
finite/integral graph-braid substance is independently re-verified by
the parent's own runner with no citation to the weakened dep's content
of any kind. The companion records that substance-vs-grade separation
as machine-checkable evidence for the audit lane; it does not re-audit
the parent and does not promote status.

---

## 0. Why this companion exists

The parent's prior audit snapshot (archived 2026-06-04) treated the row
as a clean bounded theorem, with verdict scope

> First-quantized unordered two-particle graph-braid exchange on the
> Z^3 site graph/finite cubes of side L >= 3: anyonic exchange phases
> are excluded, leaving boson or fermion exchange, and the retained
> dim_C H_x = 2 input excludes the free infinite-tower boson from the
> scoped combined statement.

That snapshot was invalidated with reason

```text
dep_weakened:staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25:retained_no_go->unaudited
```

The dep
[`STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md`](STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md)
later moved from the retained-no-go effective view to an `unaudited`
state in subsequent audit-lane activity (an upstream
`axiom_premise_changed` event).

The honest-stop question is then exactly:

> Does the parent's substantive claim load-bear on the dep's *audit
> grade* (which was weakened) or on the dep's *content* — or only on a
> set of *structural mathematical facts* (integer Smith normal forms of
> the Abrams `UD_2` boundary on the explicit `K_5` / `K_{3,3}`
> Kuratowski obstructions, plus exact networkx planarity/connectivity
> on `Z^3` cubes of side `L >= 3`) that the parent's own runner re-
> verifies block-for-block, independently of the weakened dep's grade
> *and* of the weakened dep's content?

This companion records that the third reading is the one supported by
the parent's runner and note text. The parent's runner contains zero
references to the weakened dep or its claims; the parent note
explicitly demotes the weakened dep to the **Non-Load-Bearing Context**
block (verbatim: *"it is `retained_no_go` on `origin/main` and nothing
here depends on its tier or claims to close it"*). The single
load-bearing framework dep is
[`CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md`](CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md),
which is `retained` on the current `origin/main` and is cited only
inside `(C4)` as the input that excludes the free / infinite-tower
boson.

This companion is therefore audit-friendly evidence that the prior
reading of the parent's substantive content survives the weakened
dep's audit grade change. It is not a re-audit and does not promote
status; it documents the load-bearing-step dependency surface in
machine-checkable form so the audit lane can decide how to treat the
parent in light of the dep weakening.

---

## 1. Parent recap and prior audit grade

The parent
[`GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md`](GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md)
addresses the following question:

> At the **first-quantized** level — two indistinguishable particles
> moving on the `Z^3` lattice site graph — are continuous-phase anyon
> statistics possible, or is the exchange phase forced to `+-1`
> (boson / fermion)?

The parent reaches the bounded conclusion (its claim block):

- `(C1)` `H_1(UD_2(Gamma)) = Z^{beta_1} (+) Z_2` for non-planar `Gamma`;
- `(C2)` `Z^3` cubes of side `L >= 3` are non-planar and 3-connected;
- `(C3)` `Hom(Z_2, U(1)) = {+1, -1}`, so the exchange phase is `+-1`
  only (anyons excluded);
- `(C4)` combination with the retained per-site dim-2 result excludes
  the free / infinite-tower boson, leaving `{hard-core boson, fermion}`
  as the surviving first-quantized matter statistics on `Z^3`.

The parent runner verifies all four blocks via 25 exact checks:

```text
SCORECARD: PASS=25 FAIL=0
VERDICT: At the FIRST-QUANTIZED configuration-space level, the Z^3 site
graph is non-planar and 3-connected, so its graph-braid group B_2
abelianizes with a Z_2 torsion summand carrying the two-particle
exchange; abelian statistics Hom(H_1, U(1)) sends the exchange to +-1
ONLY -> {boson, fermion}, continuous ANYONS EXCLUDED. Combined with the
retained per-site dim-2 result (free/infinite-tower boson excluded), the
surviving first-quantized matter statistics is {hard-core boson, fermion}.
This does NOT select boson vs fermion and does NOT settle the open
second-quantized gauge-coupled bridge.
```

The prior clean snapshot (codex-cli-gpt-5.5, medium confidence)
recorded a class-C load-bearing step (the homomorphism algebra
`Hom(Z_2, U(1)) = {+1, -1}` applied to the non-planar / 3-connected
`Z^3` site graph) and a 25-pass runner breakdown (`A=18, B=7, C=0,
D=0`), with chain_closure_explanation

> Within the first-quantized scope, the graph-theoretic inputs and the
> Z_2-to-{+1,-1} phase restriction close by exact graph/SNF computation
> plus the packet's quoted Ko-Park/HKRS theorem statements. The source
> explicitly does not claim the open second-quantized graded-locality
> bridge.

That explanation phrases the chain entirely in terms of *exact graph-
theoretic computation* and quoted *external* (Ko-Park, HKRS) theorem
statements — *not* in terms of any audit grade of either retained
framework dep. The present companion's narrow observation is that the
weakened dep is in fact *non-load-bearing* in both the runner and the
note: the parent's runner contains zero references to it, and the
parent note explicitly demotes it to the Non-Load-Bearing Context
block (see §3 below).

---

## 2. Invalidation cause

The audit ledger records the archived invalidation reason

```text
dep_weakened:staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25:retained_no_go->unaudited
```

This invalidation moves the parent from `audited_clean` back to
`unaudited` not because of any change in the parent's runner, note
text, prose, or computed outputs, and not because of any change in the
underlying mathematical content of the weakened dep. It is a
grade-propagation event in the audit graph: the dep's `effective_status`
was downgraded (the dep itself was re-opened via an upstream
`axiom_premise_changed` event), and the dep-weakening rule re-opens
the parent for fresh re-audit work.

At the time of this companion, the dep had *not* been restored to the
`retained_no_go` effective view on `origin/main`. This companion
therefore does *not* use the "dep restored" angle; it uses the
"parent does not load-bear on the weakened dep at all" angle. The
parent's own dependency-classification block confirms that reading
directly:

> [Non-Load-Bearing Context] —
> `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md`
> — the open second-quantized bridge this note does **not** resolve...
> Cited so the scope boundary is explicit; **it is `retained_no_go` on
> `origin/main` and nothing here depends on its tier or claims to
> close it.**

The parent's runner agrees, by static source-scan: it neither imports,
nor reads, nor cites the weakened dep's runner or note.

---

## 3. Substance-vs-grade separation

The narrow auditable observation in this companion is:

**(C1) The parent's load-bearing substantive content does not load-bear
on the *audit grade* of `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25`,
and does not load-bear on that dep's *content* at all.** The parent's
runner
[`scripts/graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.py`](../scripts/graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.py)
constructs the Abrams `UD_2` cube complex, computes the integral
boundary matrices `d1` and `d2`, runs Smith normal form over `Z` via
sympy, runs exact networkx planarity / Kuratowski / node-connectivity
checks on `Z^3` cubes of side `L in {3, 4}` plus the planar `Q_3`
contrast, and exhibits a dense 2048-point unit-circle sweep ruling out
any solution of `x^2 = 1` other than `+-1`. None of those checks
consult, import, or cite the weakened dep, the weakened dep's runner,
or the weakened dep's note. The single framework dep that *is*
load-bearing is
[`CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md`](CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md)
(currently `retained` on `origin/main`), and it is cited only in `(C4)`
as the input that excludes the free / infinite-tower boson.

The companion records this separation by:

1. Re-running the parent's runner on the current `origin/main` head and
   confirming the FINAL_TAG / scorecard is unchanged with PASS=25
   FAIL=0 (Block 1);
2. Re-verifying the integral Smith-normal-form torsion classification
   on the `K_5` and `K_{3,3}` Kuratowski obstructions directly with
   sympy (Block 2);
3. Confirming via static source-scan that
   [`scripts/graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.py`](../scripts/graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.py)
   contains zero references to audit-status fields (`audit_status`,
   `effective_status`, `intrinsic_status`, `retained_bounded`,
   `audited_clean`, `retained_no_go`, etc.) and zero references to the
   weakened dep's filename / stem / claim-id (Block 3);
4. Confirming via static source-scan that the parent note
   [`GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md`](GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md)
   classifies the weakened dep under **Non-Load-Bearing Context** with
   the explicit text *"nothing here depends on its tier or claims to
   close it"* (Block 4);
5. Counterfactual confirmation: re-executing the parent's runner
   without consulting the weakened dep's audit grade or content yields
   identical pass count and identical FINAL_TAG (Block 5);
6. `Hom(Z_2, U(1)) = {+1, -1}` homomorphism algebra self-check
   (independent of any dep), via a 4096-point dense unit-circle sweep
   on `x^2 = 1` (Block 6);
7. Exact `Z^3` planarity / Kuratowski / node-connectivity self-check on
   cubes of side `L in {3, 4}` plus the `Q_3` planar contrast,
   independent of the weakened dep (Block 7);
8. Boundary-square self-check `d1 . d2 = 0` for the `K_5` / `K_{3,3}`
   carriers, plus an independent re-derivation of the load-bearing
   `Z_2` torsion summand (Block 8);
9. Scope-preservation self-check: the parent's runner explicit "does
   NOT select boson vs fermion" / "does NOT settle the open
   second-quantized gauge-coupled bridge" sentences are still emitted
   verbatim, so the scope-boundary statement that touches the weakened
   dep is preserved as *scope language only* (Block 9).

These are static and dynamic facts about the parent's runner and note;
they do not depend on the weakened dep's audit-lane decisions or
content.

---

## 4. Substance-unchanged assertion

The parent's runner scorecard on the current `origin/main` head is

```text
SCORECARD: PASS=25 FAIL=0
```

with the FINAL_TAG/VERDICT text quoted in §1. This matches the
scorecard recorded in the parent note's header and the prior clean
snapshot's 25-pass breakdown.

The parent's note text, runner code, and runner outputs are unchanged
relative to the snapshot under which it was `audited_clean`. The
weakened dep's underlying mathematical content (the operator-algebra /
dimension-side no-go on field-algebra fermion-vs-hard-core-boson
selection) is also unchanged on `origin/main`; only the dep's
audit-lane grade has moved, and that dep is not used by the parent's
runner or load-bearing proof-walk.

The substantive bounded claim of the parent is therefore unchanged,
and the parent's runner continues to mechanically demonstrate it. The
audit lane retains exclusive authority to decide how the prior clean
treatment should be handled under the dep's current grade; the present
companion only provides the machine-checkable evidence above to
support that decision.

---

## 5. What this companion does NOT do

This companion explicitly does **not**:

- claim a new theorem;
- promote the parent's `effective_status` or `audit_status`;
- modify the parent note text, the parent's runner, or either of the
  parent's dep notes / runners (the retained dim-2 dep or the
  weakened statistics-agnostic dep);
- claim that the dep
  [`STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md`](STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md)
  has been restored to any prior grade (it has not);
- assert that the parent's bounded first-quantized scope is the only
  correct reading;
- close, sidestep, or reinterpret the parent's explicit open
  second-quantized gauge-coupled graded-locality gate (which is
  exactly the open question the weakened dep concerns);
- select boson vs fermion at the first-quantized level (which the
  parent explicitly leaves to the free 1D-rep choice);
- weigh in on dep-resolution policy beyond the parent / dep pair named
  here;
- back-fill or rebut any prior auditor verdict; the audit lane sets
  `audit_status` independently.

This companion's narrow auditable observation is exactly **(C1)** in §3:
*the weakened dep contributes neither content nor grade to any of the
parent's load-bearing checks `(C1)`-`(C4)`; it is named only in the
parent's scope-boundary text as the open second-quantized question the
first-quantized result does not close.*

---

## 6. Audit-lane handoff

The audit lane decides whether and how to re-audit the parent under
the dep's current `unaudited` grade. The present companion supplies:

- block-level static and dynamic evidence that the parent's substantive
  conclusion is mechanically demonstrated by the parent's own runner
  with no audit-status dependency on the weakened dep and no
  content-level dependency on the weakened dep;
- a verification that the parent's runner continues to PASS=25 FAIL=0
  at the current `origin/main` head with the weakened dep at
  `unaudited`;
- a static source scan that confirms zero audit-status references and
  zero weakened-dep-identifier references in the parent's runner;
- a static source scan that confirms the parent note explicitly
  classifies the weakened dep as Non-Load-Bearing Context;
- independent self-checks (`Hom(Z_2, U(1)) = {+1, -1}` algebra; `Z^3`
  planarity / Kuratowski / 3-connectivity; `d1 . d2 = 0` boundary
  square; integer Smith normal form on `K_5` / `K_{3,3}`) that
  exercise the entire substantive content of the parent independent of
  both deps.

If the audit lane chooses to treat the prior clean analysis of the
parent as reusable under the present dep grade, this companion records
the basis on which that decision can be made. If the audit lane chooses
to re-audit from scratch or to escalate the dep re-audit, this
companion does not block that path; it only documents the parent's
substance-vs-grade dependency surface.

This companion's type is meta, with audit-companion scope. It is not a
status change.
