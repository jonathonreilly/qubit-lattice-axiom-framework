# Axiom-Reconciliation Index — Fresh Scan And Triage Of Pre-Reset Surfaces (2026-07-12)

**Date:** 2026-07-12
**Type:** meta
**Status:** campaign index for the axiom-reconciliation campaign (started
2026-07-03). Detection and classification only: this note proposes repairs
and flags audit-lane items; it changes no claim, no status, and no axiom
content.
**Status authority:** sets no audit status; the independent audit lane owns
all row statuses.
**Primary tool:**
[`scripts/axiom_reconciliation_rescan_2026_07_12.py`](../scripts/axiom_reconciliation_rescan_2026_07_12.py)
(regenerable; writes
[`logs/runner-cache/axiom_reconciliation_rescan_2026_07_12.tsv`](../logs/runner-cache/axiom_reconciliation_rescan_2026_07_12.tsv))
**Triage evidence:** `logs/runner-cache/recon_triage/*.tsv` (30 batch files,
one row per classified file)

## Context

The 2026-06-29 foundation reset replaced the three-axiom set (Lattice,
Quantum, Record — Record read as durable realized-outcome registration with
a `K`/CPT-orbit reading in a supplied readout context) with the current four
axioms (Lattice, Qubit, Admissibility, Record) in
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), and the
2026-07-04 revision appended the formation sentence "Records form." The
campaign's first two blocks (PR #4908, PR #4910, and the guard re-keys landed
as commit `71cc2ec52`) restored the mechanical baseline: all axiom-live-guard
runners green as of 2026-07-03.

The campaign's working index from 2026-07-03 was a session artifact and was
never banked. This note replaces it with a REGENERABLE scan so the index can
never be lost again: needle categories are derived from the superseded memo
texts and from the phrase list in the PR #4887 repair record, and every hit
file is joined to its audit-ledger row by `note_path`.

## Scan result (at `7b9260b85`, 2026-07-12)

Scanned: 8,583 files (`docs/**/*.md` except `docs/audit/data/`, plus
`scripts/*.py`).

- **141 live hard-needle files** (98 notes, 43 scripts): superseded Record
  wording or legacy axiom-set naming outside marked-historical files.
  By ledger status: 85 unaudited, 2 audit_in_progress, 8 with retained
  audit status (see the audit-lane flag below), 46 with no ledger row
  (scripts and non-claim docs).
- **740 soft-only files**: only superseded-memo citations or generic
  legacy naming. Dated split: 607 pre-reset, 131 undated legacy-era, and
  2 post-reset scripts — both of which turned out to be deliberate
  absence-guards (they assert that superseded memo links are GONE from
  their notes), i.e. zero real post-reset drafting slips.
- 7 files intentionally excluded as historical authority (the
  `MINIMAL_AXIOMS_*` lineage and `docs/audit/AXIOM_MINIMALITY_POLICY.md`).

## Classification (triage of all 141 hard files)

Each hard file was classified by a bounded worker pass (rubric frozen in the
campaign pack; every row carries evidence line numbers, a representative
stale quote, and a proposed fix) and line-reviewed by the supervising agent.
Classes:

- **REKEY** — argument survives the landed text; mechanical
  quote/needle/citation refresh.
- **CONTENT-FLIP** — a load-bearing premise or the verdict itself uses
  deleted or changed axiom content; needs a refutation-seat re-derivation.
- **REOPENED-WALL** — a no-go whose blocking premise was the old wording;
  the wall may not survive the landed text.
- **HISTORICAL-OK** — old wording as marked historical context only.
- **DELIBERATE-OLD-TEXT** — runner references old wording by design (flip
  demonstrations, absence guards).

<!-- CLASSIFICATION-TABLE -->

## Files already owned by open PRs (skipped by the waves)

- `docs/POST_RECORD_SELECTOR_TANGENT_READOUT_WEIGHT_PROTOTYPE_2026-06-06.md`
  and its runner — PR #5208.
- `docs/PWC_DERIVATION_FROM_CUMULANT_GENERATING_FUNCTIONAL_NARROW_THEOREM_NOTE_2026-05-22.md`
  and `docs/publication/ci3_z3/FALSIFIABLE_PREDICTIONS_2026-06-08.md` — PR #5156.
- `docs/RECORD_PRODUCTION_INTERFACE_PRINCIPLE_2026-06-06.md` and its runner —
  PR #5222.
- `docs/SINGLE_CLOCK_ANTIPERIODIC_AXIS_DATUM_S4_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-06-17.md`
  — PR #5216.

## Live-guard drift measured on today's main

Re-running the five runners repaired in Blocks 1–2 found two have drifted
back to failing since 2026-07-03 — both needle drift, not science
regressions:

- `scripts/acphilambda_ambient_equivariant_heat_trace_face_2026_07_02.py`
  (PASS=79 FAIL=2): PR #5184 rewrote the C3 fixed-locus supplier note and
  dropped the two exact sentences this runner pins. The rewritten supplier
  still derives the `2/9` density and still states the readout exclusion
  ("No physical single-summand readout is derived."), so the repair is a
  re-pin of both needles plus the consumer note's quote. Queued for Wave 1.
- `scripts/frontier_post_record_selector_tangent_readout_weight_prototype_2026_06_06.py`
  (PASS=79 FAIL=2): the premise-node disclaimer sentence moved again and
  the "current snapshot" row-count pin is stale (17 → 22). The file is
  owned by open PR #5208; left to that PR, with this drift noted for its
  reviewer.

## Audit-lane flag (no action taken here)

Eight hard-needle files carry retained audit status (4 `audited_clean`,
4 `audited_conditional`). This is a structural gap, now precisely locatable:
`docs/audit/scripts/invalidate_stale_audits.py` triggers on changes to the
audited artifact (note hash, runner hash, classifier class, no-go packets) —
it has no trigger for "the axiom authority this note quotes was superseded."
Rows audited before 2026-06-29 against pre-reset axiom text therefore retain
status even though their quoted axiom surface no longer exists. The eight
files are listed in the scan TSV (`RETAINED_STATUS_HARD` block of the runner
output). Handing to the audit lane: either a reset-boundary invalidation
trigger, or targeted re-audit of the eight rows.

## Soft-only policy (740 files)

No mechanical mass-edit. The pre-reset and undated files cite the memo that
was current when they were written; their reconciliation burden is already
carried by their ledger rows (overwhelmingly unaudited), and a 738-file
citation swap would churn history, invalidate runner needles, and change no
live claim. The two post-reset hits are deliberate absence-guards needing
nothing. Fresh surfaces are already covered by the guard pattern those two
scripts implement. Soft-only files re-enter scope one at a time when their
rows are audited or their content is next touched.

## Wave plan (Blocks 4+)

1. **Wave 1 — live-guard and retained-status re-keys**: the drifted
   heat-trace runner re-pin plus the REKEY-classed members of the
   retained-status eight (highest-leverage: these carry live audit status).
2. **Waves 2+ — mechanical re-keys per lane** (REKEY class), one PR per
   lane wave, stacked on this branch, every wave re-running the affected
   runners plus `vocab_lint` before commit.
3. **Content flips**: each CONTENT-FLIP file gets a refutation-seat
   re-derivation under the landed text (worker seats draft, supervising
   agent decides) before any edit; verdict changes become their own repair
   notes, never silent edits.
4. **Reopened walls last**: each REOPENED-WALL file gets its no-go proof
   re-read against the landed text; a wall that no longer blocks is
   reported as an opened route, not repaired in place.

## Boundaries

Textual needle detection only; a file with no needle hit but a silently
stale argument is out of scope for this index. Classification is triage,
not audit. No ledger, queue, registry, or publication effective-status
file is touched by this campaign. Sets no audit status.
