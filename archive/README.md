# archive/ — the work-history consolidation store

Status: process documentation, not a science claim surface.
Scope: work-history for pull requests consolidated out of the open backlog.

## What this is

The secondary store of the two-track repo structure. The primary track is
`docs/` — full review-loop landing plus the independent audit lane. This
track holds the recorded science of closed work-history pull requests:
enough to find, cite, and if needed resurrect any of it, at light review
cost and with NO claim authority.

Nothing under `archive/` is a claim surface. Entries quote historical PR
titles and note text verbatim, including status vocabulary those PRs used;
quotation here grants nothing. A result in this store is exactly as strong
as its closed PR's own evidence, which was never independently audited.

## Layout

- `LEDGER.md` — human index, one line per archived PR.
- `ledger/<xx>/pr-<N>.json` — one machine-readable entry per archived PR,
  sharded by `N % 100` (zero-padded two digits).
- `families/` — roll-up notes for probe families and campaign bands: the
  synthesis their member PRs never carried (tables of cells, verdicts,
  caveats, disputed rows). A family roll-up is the carrier for members whose
  science is not restated by any open PR.
- `chains/` — chain summaries for the numbered block lineages
  (`CHAINS_INDEX.md`) and cross-cutting methodology notes.

## Entry schema (`ledger/<xx>/pr-<N>.json`)

Required: `id` ("pr-<N>", equal to filename stem), `title`, `science`
(non-empty; the full-read one-paragraph record of what the PR established),
`source` (`{pr: <int>, branch: <head branch>}`), `carried_by` (where the
science lives on a live surface: an open PR, a family roll-up, or this
ledger line itself), `review` (`{level: "light", process: ...}`),
`status` ("archived").
Optional: `forcing` (bool — a negative that forces direction),
`verdict_pair` (probe-cell verdicts), `promotion_candidate` (bool),
`disputed` (bool — the PR's published claim failed independent
recomputation; details in the family roll-up), `promoted_pr` (set when
promotion lands).

`scripts/check_archive_entry.py` validates all of this.

## Lanes

- **Entry (light review).** A PR that only adds/edits files under
  `archive/` needs: the checker green, honest quotation (no new claim
  language), and a normal review-loop pass — no audit, no citation-graph
  membership, no runner requirements. The review bar is index integrity,
  not scientific verdict.
- **Promotion (full review + audit).** To use archived science on the
  primary track, re-state it in a `docs/` note through the ordinary
  review-loop + audit lanes (external-idea policy applies: re-prove
  in-framework). Then set `promoted_pr` on the archive entry. The archive
  entry itself never becomes an authority.
- **Demotion.** Superseded `docs/` prose goes to `docs/work_history/`
  (existing lane), not here. This store is for unlanded PR work-history.

## Boundaries (by construction)

- The audit pipeline and citation graph ingest `docs/**` only; `archive/`
  is outside both. Do not link from `docs/` authority surfaces into
  `archive/` except from explicitly historical/work-history notes.
- `scripts/vocab_lint.py` skips `archive/` (quoted historical vocabulary
  must survive verbatim); the exclusion is mirrored in
  `docs/repo/controlled_vocabulary.yaml`.
- `archive_unlanded/` is a DIFFERENT, pre-existing lane (the canonical
  recovery surface for failed-narrative source notes, per the controlled
  vocabulary) and is not part of this store.

## Provenance of the initial population

The 2026-08 densify consolidation of the open-PR backlog: every candidate
PR read in full before bucketing; lists frozen and adversarially gated
(two independent gates) before execution. Closed PRs keep their branches
and carry the label `work-history`; each close comment names its ledger id.
List them with `is:pr is:closed label:work-history`.
