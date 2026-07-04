# Four-Axiom Narrative Scrub — Plan And Attack (2026-07-04)

**Claim type:** meta (process plan; `docs/repo/**` is outside the audit ledger
per `docs/audit/data/excluded_source_patterns.txt`)
**Status:** plan only. This PR executes no scrub edits except the front-door
rewrite (`README.md`) shipped alongside it. Every other change described here
lands in later waves, each through its own PR and the owner-operated
review-loop.
**Owner landing:** review-loop special landing, per owner instruction
2026-07-04.
**Retirement:** this plan is transient coordination, not registry content
(`docs/repo/**` is outside the audit ledger). Each wave that lands strikes
its section here; when Wave 5 lands, delete this file — anything still worth
keeping by then must already live in machinery, policy, or lint.

## 1. Trigger And Ground Truth

The 2026-06-29 foundation reset (PR #4747) replaced the three-axiom base
(Lattice, Quantum, Record; memo `docs/MINIMAL_AXIOMS_2026-06-05.md`) with the
four-axiom base (Lattice, Qubit, Admissibility, Record; memo
`docs/MINIMAL_AXIOMS_2026-06-29.md`). The memo has since been edited in place
under recorded owner approvals through 2026-07-04 (distinction clauses,
admissibility nonvacuity, readout discipline, record permanence and
one-record-per-site restoration, reading-note retirement, and the 2026-07-04
formation sentence "Records form." — occurrence at axiom strength, every
formation rule downstream; landed as PR #4915 with a certification note and
consistency sweep). The approval history and current premise-surface rules
live in `docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6.

The complete current foundation surface is:

- **Axioms (4):** Lattice, Qubit, Admissibility, Record
  (`docs/MINIMAL_AXIOMS_2026-06-29.md`).
- **Approved primitives (3):** `scale_reference_primitive`,
  `kinetic_isotropy_primitive`, `realized_state_primitive`
  (`docs/audit/data/axiom_premise_nodes.json`).
- **Tier-A admitted derivation targets (2):** `AC_phi_lambda`, `theta`
  (`docs/audit/data/tier_a_admissions.json`).
- **Scope condition (not a premise):** the past-hypothesis low-entropy
  magnitude (2026-06-16 classification).

## 2. What The Audit Machinery Already Handles (Do Not Duplicate)

A 2026-07-04 machinery review confirmed the ledger side has absorbed the
reset:

- The premise-hash guard (`invalidate_stale_audits.py`,
  `dep_axiom_premise_note_hash`) detected every axiom-text edit between
  2026-06-29 and 2026-07-03; each was followed by a pipeline or nightly
  refresh; the 2026-07-04 08:22 run reached fixed point with zero pending
  invalidations. No row was found audited against mid-flux axiom text.
- Reset fallout is queued, not lost: rows reset to `unaudited` are draining
  through the audit lane at roughly ten clean rows per day.
- Generated views (ledger, queue, publication effective-status mirrors,
  divergence report, `docs/repo/FRONT_DOOR_STATUS.md`) regenerate from
  sources via `bash docs/audit/scripts/run_pipeline.sh`.

Therefore the scrub covers only what the pipeline does not scan: narrative
and prose surfaces, currency-claiming pointers, and non-ledger governance
text. Hard boundaries for every wave:

- No hand edits to `docs/audit/data/**` or any generated file.
- No audit verdicts, effective-status changes, promotions, or retirements
  applied by scrub PRs. Status is set only by the audit lane; no-go
  retirement in particular flows only through that lane.
- No new axioms, primitives, or Tier-A admissions.

## 3. Scope Inventory (Survey Of 2026-07-04)

Reproducible detection greps are listed in Appendix A. Approximate counts,
by surface class:

| Class | Surface | Files | Fix character |
|---|---|---:|---|
| 1 | Front door: `README.md`, `docs/START_HERE.md` | 2 | mechanical, high care |
| 2 | Governance: `docs/repo/CONTROLLED_VOCABULARY.md`, `docs/KEY_TERMINOLOGY.md` axiom rows | ~2 | mechanical |
| 3 | Publication package `docs/publication/ci3_z3/` (README backbone list, `FALSIFIABLE_PREDICTIONS_2026-06-08.md` axiom-set phrase, source tables citing old memos) | ~5 source files + regenerated mirrors | mechanical + regenerate |
| 4 | Lane docs citing "the three axioms" as current | ~1–3 | mechanical |
| 5 | Superseded axiom memos still claiming currency (`2026-06-05` header says "Status: current") | 5 | header banner only |
| 6 | Science notes citing an old memo as the current baseline | ~400 | mechanical pointer/name/count |
| 7 | Science notes whose claim content touches the record-availability boundary Admissibility changed | ~213 | substantive — triage, not scrub |
| 8 | Scripts with stale axiom docstrings/filenames (e.g. `audit_companion_three_axiom_*` shim) | ~125 | mechanical docstrings; keep shims |

Counts are grep-derived estimates; each wave re-derives its own file list at
execution time rather than trusting this table. One verified anchor: 245
Markdown files cite `MINIMAL_AXIOMS_2026-06-05` as of 2026-07-04 (many
legitimately historical under R0 — the per-file R0 check, not the raw count,
sets each wave's work list).

## 4. Fix Rules

**R0 — Historical-record rule (binding, checked first).** A document that
describes the axiom set *as of its own date* is a record, not a stale claim.
Do not edit: dated session/closeout/synthesis notes, audit verdict records,
`AXIOM_MINIMALITY_POLICY.md` section 6 approval entries (the "three named
axioms" wording in the 2026-06-04/06-05 entries is correct history), the body
text of superseded memos, and quotations of older wording inside newer notes.
Only currency claims are fixed: a header still saying "current public
framework axiom memo", or prose presenting the three-axiom set as the present
baseline.

**R1 — Currency-pointer rule.** Any surface presenting the axiom set as
current must name the four axioms and cite `docs/MINIMAL_AXIOMS_2026-06-29.md`
(plus, where relevant, the policy section 6 approval history).

**R2 — Name rule.** `Quantum` → `Qubit` only where the token names the axiom.
Never touch "quantum" as a physics adjective (quantum field, quantum link,
qubit algebra prose). New surfaces use Lattice, Qubit, Admissibility, Record;
`A1`/`A2`/`A3` and the `Quantum` axiom name remain historical vocabulary.

**R3 — Count rule.** "three-axiom"/"three axioms" → four only in
currency-claiming text (per R0, historical descriptions keep their count).

**R4 — Supersession banners.** Each superseded memo
(`MINIMAL_AXIOMS_2026-04-11/2026-05-03/2026-05-20/2026-06-04/2026-06-05`)
gets a header-only edit: `Status:` flipped to superseded-historical plus a
one-line "Superseded by: `MINIMAL_AXIOMS_2026-06-29.md`" forward pointer.
Bodies untouched. No file is moved or renamed — 600+ inbound links and the
premise-registry path aliases depend on current paths; archival relocation is
explicitly deferred (section 7, item 10).

**R5 — Substantive notes are triaged, never silently rewritten.** Notes whose
claims concern record-formation freedom, record mosaics, availability
constraints, or "the axioms do/don't supply X" boundaries get no content edit
from the scrub. They are enumerated into a triage queue (Wave 3) with a
proposed disposition each — *invalidated / narrowed / intact* — for owner
adjudication and audit-lane re-audit. Initial survey assessments to seed the
queue (proposals, not verdicts):

- **Formation slice — pre-triaged; consume, don't re-derive.** The 2026-07-04
  formation sentence shipped with
  `docs/RECORD_FORMATION_APPEND_CONSISTENCY_SWEEP_2026-07-04.md`, which
  classifies 182 formation-adjacent files + 27 ledger rows into
  FLIPS-VERDICT (17), RE-KEY (10), DISCLAIMER-TRUE (136), HISTORICAL (9),
  UNAFFECTED (10). Wave 3 imports those buckets as the formation slice of
  the triage queue and adds only what the sweep did not cover. In
  particular
  `RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md`
  is FLIPS-VERDICT: occurrence is now axiom-forced, and the no-go's residue
  must narrow to formation rule/process/site/weight/rate.
- `REDUNDANCY_NOT_FORCED_BY_PND_LOCALITY_NO_GO_NOTE_2026-06-08.md` — likely
  intact (no observability/redundancy mechanism added).
- `RECORD_BLANK_BOUNDARY_RESET_NO_GO_2026-06-05.md` — likely intact.
- `AXIOM_STACK_MINIMALITY_CL4C_NO_GO_THEOREM_NOTE_2026-04-29.md` — proved
  against the 2026-04-11 base; needs re-audit for implicit record-freedom
  assumptions.
- "Arbitrary record mosaic" claims — the one family Admissibility *directly*
  targets; strongest candidates for narrowing or retirement.

Coordination with the formation-semantics channels: PR #4915 (landed axiom
append + certification + sweep) is the owning channel for formation
dispositions; PR #4916 (Born-form bridge note) and PR #4914 (program memo,
explicitly zero premise weight) are adjacent but share no files with this
plan, the front-door rewrite, or the PR #4918 mechanisms (verified
2026-07-04). Scrub waves cite those channels instead of restating their
content.

**R6 — Scripts.** Docstring/comment updates only. Wrapper shims (e.g.
`audit_companion_three_axiom_clean_base_exact.py`) stay in place; no renames
of runners referenced by cached results (runner-cache hash stability).

**R7 — Generated files are never hand-edited.** Fix sources, then run
`bash docs/audit/scripts/run_pipeline.sh` and commit the refresh as
mechanical fallout.

**R8 — No mass file moves during the scrub.** Directory reorganization,
`archive_unlanded/` build-out, and dated-series consolidation are deferred
until after the audit backlog drains (they churn paths and hashes mid-drain).

## 5. Wave Plan

Each wave is one bounded PR, prepared under the workhorse split (supervisor
specs and line-reviews; codex worker executes), landed by the owner through
review-loop.

- **Wave 0 (this PR):** this plan + the rewritten front door (`README.md`).
- **Wave 1 — front-door chain remainder (~15 files, hand-reviewed):**
  `docs/START_HERE.md`; `docs/publication/ci3_z3/README.md` backbone list and
  memo pointers; `FALSIFIABLE_PREDICTIONS_2026-06-08.md` axiom-set phrase;
  `docs/repo/CONTROLLED_VOCABULARY.md` and `docs/KEY_TERMINOLOGY.md` axiom
  rows; R4 supersession banners on the five old memos; lane-doc currency
  fixes; pipeline refresh commit.
- **Wave 2 — mechanical science-note cohort (~400 files):** scripted R1–R3
  edits in batches of ~75, each batch grep-verified (Appendix A patterns,
  zero-hit target on currency-claiming forms), line-reviewed, and followed by
  a pipeline refresh. Batch PRs assert "axiom-surface phrases only; no claim
  content touched."
- **Wave 3 — substantive triage (~213 files):** produce
  `docs/repo/AXIOM_SCRUB_SUBSTANTIVE_TRIAGE_2026-07.md`: one row per note —
  claim summary, axiom base cited, Admissibility-impact proposal
  (invalidated/narrowed/intact), suggested route (repair PR / narrowing
  repair / audit-lane retirement). No content edits in this wave. Repairs
  then flow as ordinary science PRs; verdicts stay with the audit lane.
- **Wave 4 — scripts and protocol surfaces (~125 files):** docstrings,
  comments, `.claude`/AUTOPILOT protocol text, per R6.
- **Wave 5 — regression guard:** add a warning-level stale-axiom-narrative
  lint (Appendix A patterns; allowlist for historical records per R0) to
  `audit_lint.py` or a standalone check wired into `run_pipeline.sh`/CI, so
  the next foundation change cannot silently strand the narrative layer
  again.

## 6. Verification Gates (Every Wave)

1. Detection greps: zero hits for currency-claiming stale patterns on the
   wave's surface class (allowlisted historical records excluded).
2. `bash docs/audit/scripts/run_pipeline.sh` then
   `python3 docs/audit/scripts/audit_lint.py --strict`: clean (modulo the
   pre-existing notice set); `git diff --check` clean.
3. Diff audit: no `docs/audit/data/**` hand edits; no generated-file hand
   edits; no status/verdict strings changed anywhere.
4. Reviewer instruction: mechanical waves are reviewed as fallout (spot-check
   against R0 false positives — the known failure mode is "fixing" a
   historical record); Wave 3 is reviewed as a triage queue, not as science.

## 7. Audit-Of-The-Audit Findings And Process Recommendations

Machinery is sound (section 2). Items 1, 2, and 6 of the original list are
EXECUTED as standing machinery in PR #4918 (2026-07-04); they remain here as
pointers only, not open attention items:

1. **Terminal-verdict rule — executed (PR #4918).**
   `compute_audit_queue.py` re-queues `audited_conditional` and
   `audited_failed` rows as non-terminal (`non_terminal_conditional` /
   `non_terminal_failed`), encoding the owner rule of 2026-06-15 (terminal
   verdicts are bound/unbound/nogo only). The 26 affected rows drain through
   the normal audit lane.
2. **Type-header debt — executed (PR #4918).** 210 of the 212 defaulted
   notes (all verified unaudited) now carry vocabulary `Claim type:`
   headers; the 2 undeterminable notes remain lint-visible; the existing
   pre-commit guard keeps the class at zero for new notes.
3. **137 legacy rows carry seeder-default `claim_scope`** rather than
   auditor-recorded scope; schedule re-audit or record acceptance.
4. **19 `audited_conditional` rows have non-standard repair-note prefixes**,
   breaking structured dispatch; normalize during their re-audits (all are
   queue-visible via item 1's mechanism).
5. **2 decoration rows sit under non-retained parents**; re-audit or demote
   the parents.
6. **Front-door currency — executed (PR #4918).**
   `render_front_door_status.py` emits a registry-derived Foundation Surface
   block, and `audit_lint.py` warns (`front_door_axiom_pointer`) when any
   surface listed in `docs/audit/data/front_door_surfaces.txt` cites a
   superseded axiom memo or omits the current one. Escalate the warning to
   error-level once the front-door chain is clean after Wave 1.
7. **Publication catalog refresh.** `FALSIFIABLE_PREDICTIONS_2026-06-08.md`
   predates the reset; after Wave 1 and the relevant re-audits, re-issue the
   catalog under a current date with conditionality statements checked
   against the four-axiom base.
8. **Citation discipline for new notes.** New notes should cite the current
   memo path; the Wave 5 lint should warn on new citations of superseded
   memos outside quoted/historical context.
9. **Sequencing with the drain.** Ready-queue drain is ~10 rows/day with 157
   ready; run Waves 1–2 promptly (they do not touch ledger rows) but hold
   Wave 3 dispositions loosely where re-audits are already queued — the
   audit lane may resolve some rows before triage adjudication.
10. **Deferred structural hygiene.** `docs/` root sprawl (3,600+ files),
    missing `archive_unlanded/`, and dated-series consolidation are real
    debt but wrong to fix mid-drain (R8); revisit after the reset backlog
    clears.

## Appendix A — Detection Patterns

Currency-claiming stale forms (fix under R1–R3):

- `\b(three|3)[- ]axioms?\b` near "current"/"the framework"/"this repository"
- Axiom lists naming `Lattice`+`Quantum`+`Record` without
  `Qubit`/`Admissibility`
- `MINIMAL_AXIOMS_2026-06-05` (and `-06-04`, `-05-20`, `-05-03`, `-04-11`)
  cited as canonical/current; every hit re-checked against R0
- `Status: current` headers on superseded memos
- `audit_companion_three_axiom`, `three_axiom` in script names/docstrings

Substantive-flag forms (route to Wave 3, never auto-fix):

- "arbitrary record", "record mosaic", "records are free"
- "record formation … not forced", "axioms do not supply", "not derivable
  from the (minimal )?axioms"
- no-go/insufficiency notes whose premise sections cite a pre-06-29 memo

Already-correct (inverse check): `MINIMAL_AXIOMS_2026-06-29`,
`Admissibility`, four-axiom lists.
