# Hubble Lane 5 (C1) A2 Action-Unit Metrology Obstruction: deps-changed (dep-added) Audit-Readiness Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-readiness companion / deps-changed dep-added hygiene)
**Status:** companion-only — supplies audit-friendly evidence that the
parent note
[`HUBBLE_LANE5_C1_A2_ACTION_UNIT_METROLOGY_OBSTRUCTION_NOTE_2026-04-29.md`](HUBBLE_LANE5_C1_A2_ACTION_UNIT_METROLOGY_OBSTRUCTION_NOTE_2026-04-29.md)
is substantively unchanged from the prior `conditional` verdict
(2026-05-23) since the only structural change in the ledger row was a
`deps_changed:dep_added:staggered_dirac_realization_gate_note_2026-05-03`
edge addition that *was already named in the prior audit's verdict
reasoning* (`open_dependency_paths` and `notes_for_re_audit_if_any`)
and was already declared an "admitted context input" in the parent
note's prose at audit time. This is a graph-bookkeeping side-effect
of the citation extractor catching up to the parent's explicit
"Hypothesis set used (axiom-reset 2026-05-03)" section; it does not
reflect any new substantive dependency or any change to the
load-bearing chain.

This companion is not a re-audit, not a new theorem, and not a
status promotion. If the audit pipeline seeds this file, it is a
meta companion row. This companion writes no audit verdict and does not supply a direct
effective-status change.

**Companion target:** `hubble_lane5_c1_a2_action_unit_metrology_obstruction_note_2026-04-29`
(parent note `docs/HUBBLE_LANE5_C1_A2_ACTION_UNIT_METROLOGY_OBSTRUCTION_NOTE_2026-04-29.md`,
parent runner `scripts/frontier_hubble_lane5_c1_a2_action_unit_metrology_obstruction.py`).
**Primary runner:**
[`scripts/audit_companion_hubble_lane5_c1_a2_action_unit_metrology_obstruction_hygiene_2026_06_04.py`](../scripts/audit_companion_hubble_lane5_c1_a2_action_unit_metrology_obstruction_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_hubble_lane5_c1_a2_action_unit_metrology_obstruction_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_hubble_lane5_c1_a2_action_unit_metrology_obstruction_hygiene_2026_06_04.txt)

---

## 0. Why this companion exists

The parent obstruction note
`hubble_lane5_c1_a2_action_unit_metrology_obstruction_note_2026-04-29`
(prior-audit topology snapshot: load-bearing score `5.959`,
criticality `medium`) is a
*bounded_theorem* obstruction that records the algebraic invariance

```text
exp(i S_dim / kappa) = exp(i lambda S_dim / lambda kappa)
```

and concludes that retained dimensionless inputs (`g_bare = 1`,
`beta = 6`, plaquette `<P> = 0.5934`, `u_0 = <P>^(1/4)`,
`C_APBC = (7/8)^(1/4)`, `c_cell = 1/4`) do not pin an absolute
dimensional action quantum `kappa` on `P_A H_cell` — Lane 5 `(C1)`
needs an additional clock/source/action metrology theorem.

The parent's prior audit history records:

- `previous_audits[0]` — 2026-04-30 `clean`,
  `codex-ca82-second-slice-b-fresh`, `independence: fresh_context`,
  `auditor_confidence: high`, runner `PASS=8 FAIL=0`. Archived
  on 2026-05-03 by the axiom-reset retag that converted the row from
  `positive_theorem` to `bounded_theorem`.
- `previous_audits[1]` — 2026-05-23 `conditional`,
  `codex-cli-gpt-5.5-per-site-k1`, `independence: cross_family`,
  `auditor_confidence: high`, runner `PASS=8 FAIL=0`. Verdict:
  `chain_closes=false` with `notes_for_re_audit_if_any =
  "dependency_not_retained: close and re-audit the Staggered-Dirac
  realization gate and the g_bare parent repair chain, then re-run
  this obstruction audit on the retained dependency surface."`. The
  `open_dependency_paths` list at that audit explicitly named both
  gates: `["docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md",
  "docs/G_BARE_DERIVATION_NOTE.md"]`.

The 2026-05-23 audit's `audit_state_snapshot.deps` field, however,
recorded only one structured dependency: `["g_bare_derivation_note"]`.
This was a citation-graph snapshot of the parent's explicit
hyperlink/dependency edges at that moment. The parent's prose, in
its `## Hypothesis set used (axiom-reset 2026-05-03)` section, has
named *both* gates as admitted-context inputs since the axiom-reset
retag (commits `47e43c852` 2026-05-03, with later prose tidies in
the audit-pipeline-refresh and graph-hygiene sweeps).

When the citation-graph builder caught up to that explicit
"Hypothesis set used" section in the post-audit nightly run, the
`deps` field was repaired to include
`staggered_dirac_realization_gate_note_2026-05-03`. The audit
ledger's `detect_invalidation` (`docs/audit/scripts/invalidate_stale_audits.py`)
saw `current_deps != snap_deps` (`['g_bare_derivation_note',
'staggered_dirac_realization_gate_note_2026-05-03']` vs.
`['g_bare_derivation_note']`) and fired the invalidation reason
`deps_changed:dep_added:staggered_dirac_realization_gate_note_2026-05-03`,
archiving the prior `conditional` verdict and resetting
`generated audit status reset to unaudited`.

This invalidation is structurally distinct from a substance change:

- The parent's `note_hash` field on the current ledger row matches
  the on-disk file's SHA-256 to the byte (`5708b03f218f00e460f2f643af302db224173bbd2137587a67ab811d00859427`).
- The parent's runner SHA-256 matches the audit-time
  `audit_state_snapshot.runner_hash`
  (`51df6c191e8d2de45fe2be4997cf1a1751a4147ec8e98795358f8d4c0d355fbe`) to the byte.
- The parent runner produces `PASS=8 FAIL=0` on the current
  worktree, identical to both prior audits' runner check breakdowns
  (`A=7, B=1, C=0, D=0, total_pass=8`).
- Neither the prior verdict's `chain_closes=false` conclusion nor
  its `notes_for_re_audit_if_any` instructions are affected by the
  added dep edge: both gates were already named in the verdict
  reasoning surface and in the parent's prose.

This companion supplies audit-friendly evidence that the substance
the later independent audit handling will look at is the same substance the prior
`conditional` verdict already evaluated, modulo a citation-
graph repair on a dep edge the prior verdict already flagged as
unretained.

---

## 1. Parent recap

The parent note records a negative boundary on the Lane 5 `(C1)`
absolute-scale gate. Its substantive content:

**(P1) Inputs.** Retained dimensionless data: `g_bare = 1` (from the
two-Ward / structural-normalization `g_bare` packet), Wilson plaquette
`beta = 2 N_c / g_bare^2 = 6`, same-surface plaquette constant
`<P> = 0.5934` and `u_0 = <P>^(1/4)`, minimal APBC hierarchy block
factor `C_APBC = (7/8)^(1/4)`, `P_A H_cell` rank-four cell
coefficient `c_cell = 4/16 = 1/4`.

**(P2) Load-bearing step.** For any positive scale `lambda`, the
common replacement `S_dim -> lambda S_dim, kappa -> lambda kappa`
leaves all Hilbert phases and all Euclidean lattice weights
determined by the dimensionless action unchanged:

```text
exp(i S_dim / kappa) = exp(i lambda S_dim / lambda kappa).
```

The plaquette and APBC constants are dimensionless lattice
partition-function observables; `c_cell` is a primitive trace ratio.
None of `(P1)` selects a particular dimensional `kappa`.

**(P3) Bounded conclusion.** The action-unit input set admits a one-parameter
family of action-unit readings with identical dimensionless physics;
the parent's `(C1)` shortcut

```text
g_bare = 1 + plaquette/u_0 + APBC hierarchy + c_cell = 1/4
  => absolute action-unit metrology on P_A H_cell
```

is blocked by `(P2)`. The missing import is explicit: a physical
clock/source/action metrology map tying the canonical dimensionless
lattice action and the `P_A` boundary carrier to a particular
dimensional `kappa`.

**(P4) Honest status.** The note is `bounded_theorem` (axiom-reset
retag 2026-05-03; was `positive_theorem` before the retag). Its
`Hypothesis set used` section names two derivation-target gates that
must both close before the lane can upgrade:

1. Staggered-Dirac realization derivation target
   (`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`,
   `claim_type: open_gate`).
2. `g_bare = 1` derivation target
   (`G_BARE_DERIVATION_NOTE.md`, `claim_type: positive_theorem`,
   `audit_status: conditional`).

The parent's runner verifies eight facts confirming `(P2)`:
dimensionless `beta`, dimensionless plaquette/u_0/alpha_LM/alpha_s,
dimensionless APBC factor, Hilbert-phase rescaling invariance,
Wilson plaquette weight using dimensionless action only, scale-
invariant `c_cell`, identical projected `P_A` phase across multiple
`kappa` readings, and the finite-rank canonical-commutator
obstruction.

Both prior audits' runner check breakdowns (`A=7, B=1, C=0, D=0,
total_pass=8`) are reproduced on the current repo state.

---

## 2. Invalidation cause: deps-changed (dep-added), not substance change

The audit ledger entry for this row records the following structured
audit history:

```text
previous_audits[1] = {
  audit_date:    "2026-05-23T19:48:27Z",
  audit_status:  "conditional",
  auditor_family:"codex-gpt-5.5",
  independence:  "cross_family",
  chain_closes:  false,
  audit_state_snapshot.deps:                  ["g_bare_derivation_note"],
  audit_state_snapshot.runner_hash:           "51df6c191e8d2de45fe2be4997cf1a1751a4147ec8e98795358f8d4c0d355fbe",
  audit_state_snapshot.criticality:           "medium",
  audit_state_snapshot.load_bearing_score:    5.959,
  audit_state_snapshot.transitive_descendants:21,
  open_dependency_paths: [
    "docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md",
    "docs/G_BARE_DERIVATION_NOTE.md"
  ],
  notes_for_re_audit_if_any:
    "dependency_not_retained: close and re-audit the Staggered-Dirac
     realization gate and the g_bare parent repair chain, then re-run
     this obstruction audit on the retained dependency surface."
}
```

The current ledger row records:

```text
note_hash:               "5708b03f218f00e460f2f643af302db224173bbd2137587a67ab811d00859427"
runner_path:             "scripts/frontier_hubble_lane5_c1_a2_action_unit_metrology_obstruction.py"
deps:                    ["g_bare_derivation_note",
                          "staggered_dirac_realization_gate_note_2026-05-03"]
criticality:             "medium"
topology counters:       queue-weight fields; they may increase after
                         this companion is seeded because the parent
                         gains a metadata descendant
intrinsic_status:        "unaudited"
effective_status:        "unaudited"
effective_status_reason: "awaiting_audit"
```

The diff between the audit-time snapshot and the current row is
exactly the dep addition:

```text
deps:
  added:    ["staggered_dirac_realization_gate_note_2026-05-03"]
  removed:  []
runner_hash:            unchanged (byte-identical SHA-256)
criticality:            remains medium
```

`load_bearing_score` and `transitive_descendants` are graph-derived
queue weights, not source-content invariants. The prior audit snapshot
recorded `load_bearing_score = 5.959` and `transitive_descendants = 21`;
after this companion is seeded, those counters may increase because the
parent gains a metadata descendant. That topology-weight increase is not
a parent substance change.

The `note_hash` differs from `audit_state_snapshot.archived_for_note_hash`
`54a6ed25...` because the parent prose received the standard
post-audit nightly maintenance edits (the `MINIMAL_AXIOMS_2026-05-03
-> MINIMAL_AXIOMS_2026-05-20` supersession sweep on 2026-05-21,
plus the citation-graph hygiene sweeps), but these edits are
non-substantive prose tidies that do not alter `(P1)`-`(P4)`. The
on-disk hash matches the current ledger row's `note_hash` field,
confirming the ledger and the file are in sync at the byte level
now.

Per the audit pipeline's `detect_invalidation` (lines 255-270 of
`docs/audit/scripts/invalidate_stale_audits.py`), the dep-set
difference fires the invalidation reason
`deps_changed:dep_added:staggered_dirac_realization_gate_note_2026-05-03`,
archives the prior verdict, and resets `generated audit status reset to unaudited`.

**Crucially**, the added dep `staggered_dirac_realization_gate_note_2026-05-03`
was already in scope for the prior verdict:

- it appears in the prior audit's `open_dependency_paths`
  (`docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`);
- the prior audit's `notes_for_re_audit_if_any` explicitly names
  it ("Staggered-Dirac realization gate");
- the parent's prose `## Hypothesis set used (axiom-reset 2026-05-03)`
  section names it as the first of two admitted-context inputs;
- the parent's header line `**Admitted context inputs:** (1)
  staggered-Dirac realization derivation target ...` names it.

The dep-add event is a citation-extractor catch-up to a fact the
prior audit already evaluated. It does not surface any *new* upstream
content. It is a graph-bookkeeping correction, not a substantive
dependency surface change.

This companion does not decide whether later independent audit handling should
reuse the prior conditional analysis at the corrected dep edge or run a fresh
per-row audit. It only records, in machine-checkable form, that the substance
later independent audit handling will inspect — the parent's `(P1)`-`(P4)`
content, the runner output, and the dependency surface including both gates —
is the same substance the prior `conditional` verdict already evaluated.

---

## 3. Substance-unchanged assertion

The parent note's load-bearing content is unchanged in five precise
senses:

**(S1) Runner hash matches audit-time snapshot.** The on-disk
SHA-256 of `scripts/frontier_hubble_lane5_c1_a2_action_unit_metrology_obstruction.py`
on `origin/main` is `51df6c191e8d2de45fe2be4997cf1a1751a4147ec8e98795358f8d4c0d355fbe`,
byte-identical to the audit-time `audit_state_snapshot.runner_hash`.

**(S2) Runner output matches audit-time check breakdown.** The
runner produces `PASS=8 FAIL=0` on the current worktree, matching
both prior audits' `runner_check_breakdown.A=7, B=1, C=0, D=0,
total_pass=8`. Per-check outputs are byte-stable per the cached
log `logs/runner-cache/frontier_hubble_lane5_c1_a2_action_unit_metrology_obstruction.txt`.

**(S3) Note hash on disk matches ledger.** The on-disk SHA-256 of
`docs/HUBBLE_LANE5_C1_A2_ACTION_UNIT_METROLOGY_OBSTRUCTION_NOTE_2026-04-29.md`
is `5708b03f218f00e460f2f643af302db224173bbd2137587a67ab811d00859427`,
byte-identical to the current ledger row's `note_hash` field.

**(S4) Load-bearing prose preserved.** The parent note's
load-bearing statements are present verbatim in the on-disk file:
the bridge identity `exp(i S_dim/kappa) = exp(i lambda S_dim /
lambda kappa)`, the dimensionless input table (`g_bare = 1`,
`beta = 6`, `u_0 = <P>^(1/4)`, `C_APBC = (7/8)^(1/4)`, `c_cell = 1/4`),
the "Result" section's rescaling family, the "Claim Boundary"
restatement (`g_bare = 1 + plaquette/u_0 + APBC hierarchy + c_cell
= 1/4 => absolute action-unit metrology on P_A H_cell`), the
"missing import" line (a physical clock/source/action metrology
map), the eight runner-witness fact list, and the
`Hypothesis set used (axiom-reset 2026-05-03)` section naming both
gates.

**(S5) Added dep was already named in prior verdict surface.** The
new structured dep `staggered_dirac_realization_gate_note_2026-05-03`
is named in: (a) the prior audit's `open_dependency_paths`; (b) the
prior audit's `notes_for_re_audit_if_any`; (c) the parent's header
`**Admitted context inputs:** (1) staggered-Dirac realization
derivation target ...`; (d) the parent's "Hypothesis set used"
section. So the prior `conditional` verdict was issued with
full awareness of this dependency; the citation-graph repair only
brings the structured `deps` field in line with what the prior
verdict already evaluated.

---

## 4. Runner-pass verification plan

The companion runner
`scripts/audit_companion_hubble_lane5_c1_a2_action_unit_metrology_obstruction_hygiene_2026_06_04.py`
performs the following classes of check:

- **(R1) Parent file presence.** The parent note file and the
  parent runner file exist on disk at their ledger-recorded paths.
- **(R2) Parent note-hash invariance.** SHA-256 of the parent note
  file matches the `note_hash` field on the current ledger row to
  the byte.
- **(R3) Parent runner-hash audit-time invariance.** SHA-256 of the
  parent runner file matches the prior audit's
  `audit_state_snapshot.runner_hash` to the byte.
- **(R4) Parent runner execution + pass-count match.** Invokes the
  parent runner, asserts exit status `0`, parses the tail
  `TOTAL: PASS=8, FAIL=0` line, and confirms the breakdown matches
  the prior audits' `A=7, B=1, C=0, D=0, total_pass=8`.
- **(R5) Parent prose load-bearing-content checks.** Static checks
  on the on-disk parent file: presence of the rescaling identity,
  the dimensionless input table, the result/claim-boundary
  paragraphs, the missing-import line, and the runner-witness fact
  list.
- **(R6) Hypothesis-set declaration.** The parent's
  `## Hypothesis set used (axiom-reset 2026-05-03)` section is
  present and names both gates: staggered-Dirac realization gate
  and `g_bare = 1` derivation target.
- **(R7) Admitted-context-input header.** The parent's
  `**Admitted context inputs:**` header line names both gates in
  numbered form.
- **(R8) Ledger-state self-consistency.** The current ledger row's
  `deps` field contains exactly
  `{g_bare_derivation_note, staggered_dirac_realization_gate_note_2026-05-03}`;
  `criticality = medium`; `load_bearing_score` is not below the
  prior-audit topology floor `5.959`; `transitive_descendants` is not
  below the prior-audit topology floor `21`;
  `generated effective status reset to unaudited`;
  `effective_status_reason = awaiting_audit`;
  `claim_type = bounded_theorem`;
  `generated audit status reset to unaudited`.
- **(R9) Prior-audit history shape.** The ledger row records exactly
  two prior audits: `[clean (2026-04-30), conditional
  (2026-05-23)]`. The most recent prior audit (`previous_audits[1]`)
  recorded `audit_state_snapshot.deps == ['g_bare_derivation_note']`
  (a single-element list) and `open_dependency_paths` listing both
  gate notes.
- **(R10) Dep-add detection self-check.** The companion runner
  computes the dep-set difference
  `current_deps - prior_audit_snap_deps` and verifies it equals
  `{staggered_dirac_realization_gate_note_2026-05-03}`. Confirms
  the invalidation reason
  `deps_changed:dep_added:staggered_dirac_realization_gate_note_2026-05-03`
  is the exact structural difference.
- **(R11) Added-dep prose presence.** The added dep's canonical
  filename `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
  appears in the parent's prose (both header and "Hypothesis set
  used" section), confirming the added dep was prose-declared at
  audit time and is not a new dependency surface element.
- **(R12) Other-dep stability.** The unchanged dep
  `g_bare_derivation_note` remains in the `deps` field and is
  prose-declared in both the parent's `**Admitted context inputs:**`
  header line and the "Hypothesis set used" section.
- **(R13) Open-gate file presence.** The two gate files
  (`docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`,
  `docs/G_BARE_DERIVATION_NOTE.md`) exist on disk so the later independent audit handling
  can re-fetch their content if needed.
- **(R14) Cached-log alignment.** The cached log
  `logs/runner-cache/frontier_hubble_lane5_c1_a2_action_unit_metrology_obstruction.txt`
  exists on disk and contains the `TOTAL: PASS=8, FAIL=0` line and
  the eight per-check `[PASS]` lines.
- **(R15) Bounded-theorem invariance under dep-add.** The parent's
  `claim_type` declaration (header line `**Type:** bounded_theorem
  (axiom-reset retag 2026-05-03; was positive_theorem)`) names
  the retag and is consistent with the bounded status under both
  open gates — adding the second gate as a structured dep cannot
  weaken a bounded-on-both-gates status.
- **(R16) Helper-runner stability.** The helper runner
  `scripts/canonical_plaquette_surface.py` (listed in the ledger
  row's `helper_runner_paths`) exists on disk.
- **(R17) Sister-row cross-link.** The sister Lane 5 row
  `hubble_lane5_two_gate_dependency_firewall_note_2026-04-27` is
  present on disk (the sister hygiene companion
  `HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_CRITICALITY_BUMP_HYGIENE_COMPANION_NOTE_2026-06-04.md`
  was filed 2026-06-04; this companion follows the same
  "audit-readiness, substance-unchanged" pattern for the C1 action-unit
  obstruction sibling row).
- **(R18) Companion note self-presence.** This companion note's
  on-disk filename matches the canonical path advertised in the
  PR title.
- **(R19) Claim-type-meta self-declaration.** The companion's
  `**Type:**` header line contains the literal token `meta`,
  confirming `claim_type=meta` per the precedent of
  `CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md` and
  `RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md`.
- **(R20) No-parent-edit assertion self-check.** The companion
  runner re-asserts that the parent note's on-disk SHA-256 matches
  the current ledger row's `note_hash` (i.e., this PR adds no
  parent edits).

Each (R*) block above expands into several PASS/FAIL line items in the
runner output, so the total PASS count is in the low-50s rather than
literally 20 (one PASS per check; some (R*) blocks chain three to six
individually-verifiable sub-checks). The exact PASS count and the
absence of any FAIL is what matters; the cached log records the
current breakdown. The runner is purely a hygiene verifier: it does
no new physics, claims no derivation, performs no re-audit of the
parent, and writes/modifies no ledger field.

---

## 5. What this companion does not do

For audit-lane clarity, this companion explicitly does not:

- modify the parent note in any way;
- modify the parent runner in any way;
- change the parent's `audit_status`, `effective_status`,
  `criticality`, `load_bearing_score`, `claim_type`, `claim_scope`,
  or any other ledger field;
- assert that later independent audit handling should reuse the prior
  conditional analysis at the corrected dep edge;
- claim that either open gate (staggered-Dirac realization,
  `g_bare = 1` derivation) has been closed, audited, or moved;
- claim progress toward `(C1)` closure or numerical `H_0`
  derivation;
- introduce a new minimal-axiom statement or accepted-premise;
- assert anything about the Record axiom adopted in
  `MINIMAL_AXIOMS_2026-06-04.md` (the parent note predates the
  Record-axiom adoption and the load-bearing chain is independent
  of it — the rescaling invariance is a finite-dimensional algebraic
  identity);
- assert that the `Δb_3` pure-gauge-vs-full-SM piece or any other
  recent QCD/lane progress is relevant to this row (none of the
  load-bearing inputs in `(P1)` depend on those results).

This companion is **claim_type=meta** by design: it ratifies no
new content, only records the substance-unchanged invariant in a
form the later independent audit handling can verify with one runner invocation.

---

## 6. Audit Handoff

When the later independent audit handling next picks up
`hubble_lane5_c1_a2_action_unit_metrology_obstruction_note_2026-04-29`
from the queue, this companion offers the auditor a one-shot
precondition check:

1. Run
   `scripts/audit_companion_hubble_lane5_c1_a2_action_unit_metrology_obstruction_hygiene_2026_06_04.py`
   on the current repo state.
2. If every check returns `PASS` with `FAIL=0` in the trailing
   summary, the parent's substance, runner output, and dependency
   surface are provably identical to what the prior
   `conditional` verdict evaluated (modulo the single
   dep-add `staggered_dirac_realization_gate_note_2026-05-03`
   which the prior verdict already named in
   `open_dependency_paths` and `notes_for_re_audit_if_any`).
3. The auditor can then choose to:
    - reuse the prior conditional analysis at the
      corrected dep edge, since both gates were already known to
      the prior verdict and the dep-set repair simply makes the
      citation graph match the prose;
    - or perform a fresh per-row audit with the knowledge that the
      load-bearing content, runner output, and (full) dependency
      surface are exactly the artifacts the prior verdict assessed.
4. If the companion runner returns any FAIL, then the on-disk
   parent or runner has drifted since this companion was filed,
   and the auditor should treat this companion as stale.

Later independent audit handling retains the provenance boundary for any new verdict at the
corrected dep edge. This companion does not anticipate a particular
verdict outcome. It only narrows what the next auditor must
investigate: the substance is the same, the runner is the same, the
upstream gates were already known to the prior verdict, and only
the structured `deps` field caught up to the parent's prose.

---

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links the
audit citation graph can track for this companion. It does not
promote this note or change the audited claim scope.

- [hubble_lane5_c1_a2_action_unit_metrology_obstruction_note_2026-04-29](HUBBLE_LANE5_C1_A2_ACTION_UNIT_METROLOGY_OBSTRUCTION_NOTE_2026-04-29.md)
- [staggered_dirac_realization_gate_note_2026-05-03](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
- [g_bare_derivation_note](G_BARE_DERIVATION_NOTE.md)
