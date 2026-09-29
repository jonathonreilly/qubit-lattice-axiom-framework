# Work History

This directory is the historical lane for the repo’s older programs, partial
bridges, and exploratory branches.

The repo's front door is the key-science index:
[`docs/KEY_SCIENCE.md`](../KEY_SCIENCE.md). The former flagship paper
package is deferred (owner decision 2026-09-03) and lives on the archive
tier at `archive/publication/ci3_z3/` (record, not a claim surface).

## Purpose

Use work history for:

- earlier architecture families
- historical retained bridges that are no longer the repo headline
- exploratory or negative-result lanes worth preserving
- scratch-era chronology that still matters for provenance

## Rule

Old files remain part of the scientific record, but they are not the public
claim surface unless they are explicitly promoted through the ordinary
review-loop + audit lanes.

## Current split

- `archive/publication/ci3_z3/`
  - the deferred paper package (archive tier; snapshot at deferral)
- `docs/work_history/`
  - explicit historical bucket
- `docs/work_history/atomic/`
  - bounded atomic companions and salvage packets
- `docs/work_history/repo/review_feedback/`
  - archived operational review packets and resolved audit histories
- `docs/work_history/repo/backlog/`
  - archived planning/backlog notes
- `docs/work_history/pf/`
  - salvaged PF route history from the rejected closure packet
- the live review surface should point here only for optional historical
  context, not as part of the primary read path

## Stored payloads kept in git, not in the working tree

The review drain of 2026-09-15 to 2026-09-23 stored byte-exact copies of the original PR files in hash-named folders (`_objects/`, `scientific-recovery/objects/`, `review_loop/pr*/objects/`). On 2026-09-27 those 33,660 files (158 MB compressed) were removed from the working tree. The science they record is unchanged: no current note, runner or ledger row reads them, and the manifests, READMEs and `kept/` files beside them stay checked out. Git keeps every payload byte for byte at tag `archive/work-history-payloads-20260927` (main commit `7d2dc1a8b5`). Each affected folder's README gives the command that reads or restores its payloads. Two payloads that a current runner reads stay checked out in `repo/review_feedback/pr8061-proof-sources/_objects/`.
