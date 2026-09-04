# archive/ — the science record of the work-history

Status: process documentation, not a science claim surface.
Scope: the science done in work consolidated out of the open backlog.

## What this is

The secondary store of the two-track repo structure. The primary track is
`docs/` — full review-loop landing plus the independent audit lane. This
track is a record of SCIENCE, not of pull requests: what was computed,
shown, refuted, and left open, organized by physics question — enough to
find it, cite it, and if needed resurrect it, at light review cost and
with NO claim authority.

**Start at [`SCIENCE.md`](SCIENCE.md)** — the record organized by physics
question. A PR number in this store is never an identity, only an evidence
address: the closed PR's branch holds the raw diff, runner script, and
cache behind a recorded result, which is what a later promotion audit
needs. Results are the unit of the record; PR ids appear only as
citations.

Nothing under `archive/` is a claim surface, a carrier of live science, or
an authority of any kind. Entries quote historical PR titles and note text
verbatim, including status vocabulary those PRs used; quotation here grants
nothing. Every statement in this store is historical: it records what a
closed, never-independently-audited PR claimed and reported, and nothing
more. To rely on any of it, use the promotion lane below.

## Layout

- `SCIENCE.md` — the record: the science by question, citing evidence
  addresses. Read this first.
- `families/` — roll-up notes for probe families and campaign bands: the
  assembled record of what the member PRs' runners reported (tables of
  cells, reported verdicts, caveats, disputed rows) — cross-member
  bookkeeping no single member note carried. For a member not restated by
  any open PR, the roll-up is where its record is FOUND; being findable
  here confers no status.
- `chains/` — chain summaries for the numbered block lineages
  (`CHAINS_INDEX.md`) and cross-cutting methodology notes.
- `LEDGER.md` + `ledger/` — the provenance index: one entry per consolidated
  source, keyed by its evidence address (`pr-<N>` for the PR consolidation;
  the semantic note id for note demotions; `campaign-<slug>` for campaign
  packets). Plumbing, not the record: it exists for integrity checking and
  for following an old reference to what its source contained.
- `notes/` — demoted claim notes from the note-stratum densify (2026-09
  freeze), each at its full original path (`notes/docs/...`). A moved note
  remains the primary claim surface of its own result; the era memo in
  `chains/` is its carrier, never its replacement. `PATHMAP.tsv` maps every
  old path to its new one.
- `campaigns/` — whole working packets (campaign roll-ups, exercise packets,
  the opus-direct positive-path pack, the densify freeze evidence packet).
- `publication/` — deferred publication packages, moved whole as the
  snapshot at deferral (currently `ci3_z3/`, owner deferral 2026-09-03).

## Entry schema (`ledger/<xx>/pr-<N>.json`)

Required: `id` ("pr-<N>", equal to filename stem), `title`, `science`
(non-empty; the full-read one-paragraph record of what the PR claimed and
reported), `source` (`{pr: <int>, branch: <head branch>}`), `carried_by`
(a locator for the recorded science: an open PR that restates it, a family
roll-up in this store, or this ledger line itself — a finding aid, never an
authority), `review` (`{level: "light", process: ...}`),
`status` ("archived").
`science` must be a string of at least 40 characters; `source.pr` a strict
integer (not a boolean).
Optional: `forcing` (bool — a negative that forces direction),
`verdict_pair` (string; probe-cell verdicts), `promotion_candidate` (bool),
`disputed` (bool — the PR's published claim or bookkeeping failed
independent recomputation or reconciliation; details in the family
roll-up), `promoted_pr` (strict integer; set when promotion lands).

`scripts/check_archive_entry.py` validates all of this.

## Note-keyed and campaign entries (densify freeze 2026-09-04)

Entries whose filename stem is not `pr-<N>` are semantic: note demotions
(id = the note's claim id — its repo path lowercased with `/` as `.`,
`docs/` stripped) and campaign packets (`campaign-<slug>`), sharded by the
first two characters of the id. Required keys are the same, with `source`
exactly `{kind, path, consolidation}` plus `moved_to` when `kind` is
`docs-note` or `publication-package` (`kind` is `docs-note`,
`campaign-packet`, or `publication-package`). Optional extras:
`lane` (the densify lane whose `chains/` memo carries the entry) and
`follows_parent` (a FOLLOW-PARENT companion's archived parent id).
`carried_by` names the era memo and the decided carrier. The same
no-authority rule applies verbatim.

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
- **Demotion.** Superseded primary notes demote here under `notes/` with
  note-keyed ledger entries and a `PATHMAP.tsv` row (the 2026-09 densify
  freeze is the first such wave: 797 ARCHIVE-verdict notes + 2 follow-parent
  companions, released behind the 21 era memos in `chains/`). Their audit
  ledger rows retire natively: the citation graph is built from `docs/`, so
  a moved note leaves the graph and `seed_audit_ledger.py` drops its row at
  the next pipeline run ("dropped (note removed)"). `docs/work_history/`
  remains the in-docs lane for historical prose that stays on the primary
  surface.

## Boundaries (by construction)

- The citation graph is built from markdown beneath `docs/` (excluding
  `docs/audit/`) — see `docs/audit/scripts/build_citation_graph.py` — so
  `archive/` is outside it and outside every graph-derived audit surface —
  and the audit ledger is seeded FROM that graph
  (`docs/audit/scripts/run_pipeline.sh` run order;
  `seed_audit_ledger.py`), so `archive/` files cannot become audit rows.
  Do not link from `docs/` authority surfaces into `archive/`
  except from explicitly historical/work-history notes.
- `scripts/vocab_lint.py` skips `archive/` entirely (a code-level skip:
  quoted historical vocabulary must survive verbatim). The
  `excluded_paths` entry in `docs/repo/controlled_vocabulary.yaml` is
  rule-specific documentation of the same intent, not the enforcing
  mechanism.
- `archive_unlanded/` is a DIFFERENT, pre-existing lane (the canonical
  recovery surface for failed-narrative source notes, per the controlled
  vocabulary) and is not part of this store.

## Provenance of the note stratum (second population, 2026-09)

The 2026-09 densify freeze over the note stratum: 3,262 candidates read in
full; partition 2,418 FRONT / 797 ARCHIVE / 0 HOLD / 47 FOLLOW-PARENT; 21
lane memos, each attacked by an independent full-read adversarial seat and
the repair layer re-checked by a second pass (deltas D8/D8b). The complete
evidence packet is `campaigns/densify-freeze-20260904/`. Executed on the
owner's GO of 2026-09-05.

## Provenance of the initial population

The 2026-08 densify consolidation of the open-PR backlog: every candidate
PR read in full before bucketing; lists frozen and adversarially gated
(two independent gates) before execution. Closed PRs keep their branches
and carry the label `work-history`; each close comment names its ledger id.
List them with `is:pr is:closed label:work-history`.
