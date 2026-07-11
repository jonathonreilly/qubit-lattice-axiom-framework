# Bounded Admission Backlog Registry -- Non-Authoritative Proposal

**Date:** 2026-06-15
**Claim type:** meta
**Status:** NON-AUTHORITATIVE PROPOSAL ONLY. Owner approved landing this file
as discussion/backlog material on 2026-06-16, not as a live registry. It is
NOT wired into the audit pipeline, NOT citable authority for audit verdicts,
NOT a replacement for `docs/audit/data/premise_decision_history.json`, and NOT a
mechanism for converting `audited_conditional` rows to `retained_bounded`.
This proposal is closed: no admission registry or migration path is live.
Current premise authority is limited to axioms and approved primitives.
**Proposed artifact:** [`docs/BOUNDED_ADMISSION_REGISTRY_PROPOSAL_2026-06-15.json`](BOUNDED_ADMISSION_REGISTRY_PROPOSAL_2026-06-15.json)
(first-pass populated draft; would eventually live at
`docs/audit/data/bounded_admissions.json` once approved and wired).

## The problem

Bounded admissions are currently scattered across **922 `retained_bounded`
rows**, each self-bound (`effective_status_reason: self`,
`claim_type: bounded_theorem`) on a residual named in **its own note**. There
is no atom-level index. Consequences:

- **Duplication.** The same underlying admission (beta=6, the Wilson relation,
  the Kogut-Susskind chirality import) is re-named and re-admitted note after
  note. A keyword scan of the 922 rows shows they collapse onto a *handful* of
  atom-families (approx: 369 imported-literature/empirical, 238 helper-module,
  112 color, 104 KS-chirality, 88 convention, 46 beta6) -- the same atoms,
  recorded dozens of times.
- **No leverage view.** Nobody can see that deriving *one* atom would retire
  *forty* rows, so derivation effort is not prioritized.
- **No chase/floor separation.** Genuinely irreducible floors (the Past
  Hypothesis) get chased forever while real targets sit unranked.

## Proposed future structure: one registry, `tier` as a field

This is a superseded historical proposal, not current repo machinery.
`docs/audit/data/premise_decision_history.json` preserves provenance only and
cannot supply or bound a dependency. The proposed catalog was never adopted;
the current foundation contains only axioms and approved primitives.

One entry per **deduplicated atom**:

| field | meaning |
| --- | --- |
| `admission_id` | stable slug for the atom |
| `statement` | the minimal atom, one line |
| `tier` | `A` \| `import` \| `convention` \| `floor` |
| `retirability` | `open_target` \| `no_go_proven` \| `non_retirable` \| `retired` |
| `leverage` | `{rows_bound, top_fanout}` -- the priority order |
| `bound_row_ids` | back-references (the dedup; the "go after these" list) |
| `derivation_state` | pointer to the campaign / no-go |
| `aliases` | so re-admissions COLLAPSE here, never duplicate |

### What distinguishes the tiers (be clear)

- **`tier: A`** -- a *confirmed genuine irreducible* framework derivation
  target (the project reduces to it). Retired only by a real derivation or a
  proven no-go. Kept tiny **by design**: something is promoted to `A` only
  *after* attempts to reprove it away have failed. Today: `AC_phi_lambda`,
  `theta`.
- **`tier: import`** -- the bulk. A value/relation used from *outside*
  (literature, hard-coded, helper module): a **debt**, retired by **reproving
  it from primitives** (forbidden-import discipline), after which it could
  retire from a future approved registry. Most "admissions" are really this --
  homework, not fundamental gaps.
- **`tier: convention`** -- vacuous rescaling/labeling (Y0, g_bare). Not an
  admission. Recorded for completeness.
- **`tier: floor`** -- non-retirable: the Past Hypothesis scope condition; an
  external empirical value the axioms cannot reach; a proven no-go. Recorded but
  **off the chase-list**.

### The lifecycle (entries flow; they are not static)

```
import --future approved reproof--> RETIRED (candidate for independent re-audit) <- best
       --confirmed irreducible-----> promoted to tier:A
       --proven non-retirable------> demoted to floor (e.g. Past Hypothesis)
```

## Three payoffs

1. **Dedup.** One atom, many rows pointing in via `bound_row_ids` + `aliases`.
   No re-admitting; no running the beta=6 campaign forty times.
2. **Leverage-ranked reproof/derivation backlog.** Sort by
   `rows_bound x top_fanout` -> the hit-list. `tier: A` atoms get
   **derivation campaigns**; `tier: import` atoms get **reproofs**
   (show the primitives reproduce the imported value, then retire it);
   `tier: floor` gets **left alone**.
3. **Possible future `audited_conditional -> retained_bounded` mechanics.** In
   a future approved registry, a row could cite a reviewed admission atom
   instead of repeating an import locally. This proposal does not enable that
   behavior. Auditors must not cite this proposal file as admission authority.

## The reproof-worker campaign this could enable after future approval

If separately approved and wired, a registry like this could become the
**backlog** for an import-reproof worker (codex / workhorse under
supervision). The loop would be:

1. Take the top `tier: import`, `retirability: open_target` atom by leverage
   (e.g. `helper_frontier_module_surface` ~238 rows, or
   `imported_literature_series` ~369 rows).
2. Reprove the imported value/relation **from framework primitives** (Haar /
   the three axioms), per the reprove-and-cite discipline (reprove in the
   runner, cite the literature only as comparator).
3. On a clean reproof, every row in that atom's `bound_row_ids` could become
   a candidate for independent re-audit; only the audit lane changes status.
4. The worker ships PRs; the independent auditor re-lands the rows. No verdict
   is written from a session.

That future workflow could convert large import clusters from *bounded* to
*retained clean* in cluster-sized chunks instead of one row at a time. This
proposal does not perform that conversion.

## Verification update (2026-06-15)

The per-atom operational test (cited-as-dep bound-check + retirability) was run
on the 10 `first_pass` atoms (see the JSON `_verification` field). It earned its
keep -- **two atoms flipped**:

- **`beta6_wilson_coupling` `import -> floor`.** The atom conflated the Wilson
  matching *relation* (already a bounded theorem) with the *number* beta=6, an
  external lattice-QCD empirical value that bounds nothing load-bearing. There
  was never a primitives-reproof to win there -- it is **off the chase-list**.
- **`koide_so2_quotient` `floor(no_go) -> import(open_target)`.** The block-total
  Frobenius route is *retained* (PASS=16) and reaches kappa=2 *without* the
  withheld quotient -- a tractable structural choice, not a wall.

No atom was an axiom-citation-gap; **no genuine new tier:A** (Tier-A stays the
canonical 2). Verified reproof backlog (all `hard`), by leverage:
`imported_literature_series` (~369) > `helper_frontier_module_surface` (~238) >
`staggered_ks_chirality_import` (~104) > `readout_determinant_identification` >
`koide_so2_quotient`. **Top reproof target: `imported_literature_series`** (a
framework-native 1-loop BZ integral for I_S, no no-go blocking it). A reproof
worker is dispatched on it.

## Careful line-by-line review population (2026-06-16)

All 921 `retained_bounded` rows were read one at a time and assigned to their
canonical atom (the `bound_row_ids` map in
[`BOUNDED_ADMISSION_BOUND_ROW_IDS_MAP_2026-06-16.json`](BOUNDED_ADMISSION_BOUND_ROW_IDS_MAP_2026-06-16.json)).
This **corrected the keyword-scan estimates and the 67->11 minimize optimism**:

- **`imported_literature_series` collapsed 369 -> 19** -- the "import/literature"
  keyword hits were almost all *specific* physics atoms (beta6, color, KS,
  empirical), not a generic literature pile.
- **`helper_frontier_module_surface` is the top cluster (254)**; its science core
  (the shell-localization identity) is now DERIVED in PR #4123. It needs a
  **shell-vs-GR split** -- the shell-bounded subset retargets to #4123 (separate
  retarget PR), the GR/tensor + Maradudin-lattice-Green rows stay bounded.
- **A new atom surfaced: `bounded_runner_gate_b_certificate` (22 rows)** -- the
  one coherent cluster the first-pass registry was missing (added here).
- **A large diverse tail: ~315 rows do not map to a canonical atom**, ~268 of
  them effectively-unique one-offs (gravity/DM/network/teleportation probes). The
  bounded register does **not** cleanly reduce to a few atoms; a third is a
  diverse long tail that will not cluster-drain. This is the honest correction
  the careful-review gate was protecting against.

This updates per-atom leverage to the reviewed counts but edits NO row notes and
asserts NO audit status -- it only records the back-reference map.

## Honesty / scope of this draft

- **First pass.** `rows_bound` marked `_estimate` are approximate keyword-scan
  counts; `bound_row_ids` are exact only for the conditional-bridge atoms.
  The full dedup of all 922 rows is the reproof-worker's first job.
- **Triage, not gospel.** Entries marked `classification_status: first_pass`
  come from the agent-sort, which demonstrably mis-shelved **B-AXIS** (called it
  a scope condition when it is a bounding admission gating 925 descendants -- now
  corrected to `verified`) and labeled the **SM-color** bridge `tier:A` while
  also calling it "non-retirable" (a contradiction). Every `first_pass` atom
  needs the per-atom operational test (does it bound? is it retirable?) before
  its tier is recorded.
- **No live change.** This PR adds proposal files in `docs/`; it does not
  touch `docs/audit/data/`, any live registry, the pipeline, or any audit
  verdict. It is not citable admission authority.
