# Full-History Science Census

**Date:** 2026-08-05
**Authority:** none
**Status:** orientation census. No claim authority. The audit ledger remains the
sole ruling surface for landed claims. Where this census and the ledger disagree
about a landed note, the ledger is right.

---

## What this is and why it exists

The owner directive of 2026-08-05 was to make sure there is a full ledger of all
meaningful science going back to the start of the project. This document answers
that by enumerating, rather than by ruling: it says what science exists, where it
physically lives, and which of it the audit ledger covers.

It is a **point-in-time enumeration**, dated 2026-08-05, built from a full-ref
git walk of the repository — 2,914 refs at the time of the walk [verified] — with
the results cross-checked against the ledger shards under
`docs/audit/data/ledger/`.

The companion file
[`science_census_unledgered_index_2026-08-05.json`](science_census_unledgered_index_2026-08-05.json)
**is the authority for the item lists.** It carries all 3,621 enumerated items
[verified] with their paths, refs, dates and pull request numbers. The prose below
names only representative examples. If a list here and the index disagree, the
index is right, and the index records its own coverage gaps.

Every count in this document is tagged. **[verified]** means it was recomputed
from the underlying data for this census. **[from-survey]** means it comes from
the earlier survey walks and could not be checked against the data available
here.

---

## The verdict

**The ledger is complete over the science it was built to cover, and five
strata of real science sit outside it.**

The covered part is in good order. At the 2026-08-03 tip the repository holds
4,686 markdown files under `docs/` [verified]. Those split exactly into 3,972
files carrying a ledger row and 714 files inside deliberately gated
infrastructure directories [verified] — 3,972 + 714 = 4,686, with nothing left
over. Every one of the 3,972 ledger rows points at a file that is present at the
tip [verified], and no row anywhere points at a note that has been deleted
[verified]. There are 3,972 shard files on disk, one per row [verified]. The
ledger is hash-exact over landed claim notes, with no drift.

The uncovered part is the point of this document. Five strata of science have
never had a ledger row, for five different and mostly deliberate reasons. They
total 3,621 enumerated items [verified]. Two of the five are working as designed
— open pull requests mint their rows when they land, and that is correct
behaviour, not a gap. The other three are genuine history sitting outside the
ledger's reach.

The single sharpest fact: **the registrar only ever looks inside `docs/`.** The
whole March 2026 era of the project, which predates the `docs/` note format
entirely, was never eligible for a row and never will be under the current
mechanism.

---

## The strata

| # | Stratum | Count | Where it physically lives |
|---|---------|-------|---------------------------|
| 1 | March 2026 event-network era | **252** [verified] — 58 claim notes + 194 run logs | `.claude/science/**` and `logs/*.txt`, on history descending from the true root `7a5f1dca05` (2026-03-13). Not reachable from `origin/main`; reachable from archive refs such as `claude/yt-direct-lattice-correlator-2026-04-30`. |
| 2 | Pre-seeding mainline, deleted | **32** [verified] | `docs/*.md`, added to the mainline in April 2026 and deleted before the 2026-04-26 seeding run. Reachable only through archive refs, since `origin/main` has been rewritten. |
| 3 | Branch-only, never mainlined | **3,074** [verified] (2,510 of them [verified] pass the survey's science-note naming filter) | Branch and tag tips across the 2,914 refs. Named branch families include `physics-loop/*` (963 refs), `claude/*` (110), `codex/*` (101), `science/*` (96) [all verified]; plus 356 `archive/*` tags [verified], of which 51 are the `archive/ckm-*` closed-form wave [verified]. |
| 4 | Open pull requests, on origin branches | **228** [verified] | Head branches on origin, across 107 of the 110 open pull requests that carry science notes [verified]. **Correctly pending** — rows mint at landing. |
| 5 | Fork pull requests only | **14** [verified] | Inside fork-hosted pull request objects only, with no origin branch carrying them. PRs #5922, #5933, #5940, #5942, #5949, #5953, #5962, #5968, #5974, #5978, #5981, #5983, #5990, #5998. **Rescued by this census** into `archive_unlanded/fork_pr_rescue_2026_08_05/`. |
| 6 | Closed without merging, never landed | **21** [verified] | Closed pull request objects and branch tips, PRs #5620 through #5888 [verified]. 13 are still recoverable from `origin/main`'s own history; 8 exist only on branches [verified]. |

Strata 4 and 5 are two halves of the open-pull-request tier: 228 + 14 = 242
notes on open pull requests [verified], which is the full open set.

---

## How the registrar works

One pipeline owns every ledger row.
`docs/audit/scripts/build_citation_graph.py` walks `docs/**` for markdown files,
builds the citation graph, and `docs/audit/scripts/seed_audit_ledger.py` turns
that graph into one shard per claim under `docs/audit/data/ledger/`; both run
through `run_pipeline.sh`. Rows are enforced at three points — a pre-commit hook,
the nightly `.github/workflows/audit.yml` run, and the review-loop pipeline at
every landing — which is why the landed surface stays hash-exact. The mechanism's
reach is set by one line of code: the graph builder scans `DOCS_DIR.rglob("*.md")`
where `DOCS_DIR` is the repository's `docs/` directory. Anything outside `docs/`
is not gated, not excluded, not skipped — it is simply never seen.

---

## What is actually out there

Representative items per stratum. The index is the authority for the complete
lists.

### Stratum 1 — March 2026, the event-network era

Fifty-eight claim notes [verified], written before the `docs/` note format
existed, spread across `analyses` (29), `sanity` (12), `hypotheses` (6),
`write-ups` (4), `frontier` (3) and single notes under `derivations`,
`experiments`, `investigations` and `theory-reviews` [all verified]. Alongside
them sit 194 run logs first added in March [verified].

- `derivations/visibility-threshold-2026-03-30.md` — derives the visibility
  threshold R_c(y) for the discrete event-network model.
- `write-ups/interference-regime-2026-03-30.md` — characterises the interference
  regime of the discrete event-network toy model.
- `write-ups/decoherence-arc-2026-03-30.md` — surveys the decoherence mechanisms
  available in the model.
- `frontier/corrected-propagator-2026-03-31.md` — corrects the propagator, moving
  the mechanism from amplitude repulsion to gravitational attraction.
- `theory-reviews/interference-geometry-sensitivity-2026-03-30.md` — tests how
  sensitive the interference pattern is to geometry.

This era was pushed directly, without pull requests [owner-attested,
2026-08-05].

### Stratum 2 — the pre-seeding mainline deletions

Thirty-two notes [verified] that were on the mainline and were removed before the
ledger first existed. The survey judged roughly 24 of them substantive rather
than steering or index documents [from-survey]; that split is a judgement call and
was not recomputed here. Every flagship named in the survey was confirmed present
in the list of 32 [verified].

- `GW_ECHO_DERIVED_NOTE.md` — derives a zero-parameter gravitational-wave echo
  prediction for GW150914 from the lattice axioms: t_echo = 67.66 ms,
  f_echo = 14.8 Hz, testable against existing LIGO data.
- `CABIBBO_JARLSKOG_PREDICTION_2026-04-12.md` — predicts the Cabibbo angle with
  no free parameters, sin(θ_C) = 0.2236 against an observed 0.2243.
- `YT_ZERO_IMPORT_CLOSURE_NOTE.md` — closes the top-Yukawa gate with no imported
  Standard Model observables, reporting v, alpha_s(M_Z) and m_t from the single
  axiom.
- `YT_QFP_INSENSITIVITY_THEOREM.md` — answers a reviewer's blocker by arguing the
  Standard Model running above the electroweak scale is a valid framework-native
  interpolation.
- `DM_CLEAN_DERIVATION_NOTE.md` — derives the dark-matter to baryon ratio
  R = 5.48 through a thirteen-step chain with two bounded inputs.
- `DM_LEPTOGENESIS_NOTE.md` — routes the baryon asymmetry through thermal
  leptogenesis with right-handed neutrino masses set by the taste staircase.
- The three DM leptogenesis closure notes of 2026-04-16, including
  `DM_LEPTOGENESIS_FULL_THEOREM_CLOSURE_NOTE_2026-04-16.md`, which reports the
  transport side closing with no remaining non-axiom boundary.
- `GAUGE_VACUUM_PLAQUETTE_BRIDGE_THEOREM_NOTE.md` — closes the gauge-vacuum
  plaquette bridge on the scalar route.
- `BOUNDED_NATIVE_GAUGE_NOTE.md` — derives native cubic SU(2) gauge structure
  from lattice topology alone, with SU(3) left explicitly open.
- `HIGGS_VACUUM_PROMOTED_NOTE.md` — the standalone authority for the promoted
  Higgs and vacuum lane as it then stood.
- `PREDICTION_CARD.md` (2026-04-01) — the original falsification card, stating
  what would break the model.
- `CURRENT_FLAGSHIP_ENTRYPOINT_2026-04-14.md` — the April reading entry point.

### Stratum 3 — the branch-only tier

The largest stratum by a wide margin: 3,074 notes [verified] that were committed
on a branch or tag, never reached any mainline, and never held a row. By month of
first commit: April 1,525; May 378; June 311; July 759; August 101 [all verified].

Lane attribution is partial — 1,217 of the 3,074 carry a named branch in the
survey data [verified], so the following are **lower bounds**, not totals:
`physics-loop/*` at least 432, `science/*` at least 285, `causal-time/*` at
least 244, `codex/*` at least 184, `claude/*` at least 40 [all verified].

By subject, the heaviest name families are top-Yukawa (365), Koide (342),
physical-readout (337), zero-import (212), Planck (144), quark (113), PMNS (88),
dark matter (79) and CKM (71) [all verified]. The `QUARK_ROUTE2` no-go corpus
built on the block153–155 branches runs to 111 notes [verified].

### Stratum 4 — open pull requests on origin

228 notes [verified] across 107 pull requests [verified]. **This is not a gap.**
These notes are pending by design; the pipeline mints their rows the moment the
pull request lands. They are listed so the census total reconciles, not because
anything is wrong.

### Stratum 5 — fork pull requests only

Fourteen notes [verified] that existed nowhere except inside fork-hosted pull
request objects. No branch on origin carried them, so no walk of the repository's
own branches would ever find them, and nothing would have preserved them if the
forks went away. All fourteen are gravity-lane cycle notes — cycles 724 through
735, plus 873 and 883 [verified].

This census rescued all fourteen byte-for-byte into
`archive_unlanded/fork_pr_rescue_2026_08_05/`, with a manifest recording the
pull request number, head commit, original path, git blob id and SHA-256 of each.

### Stratum 6 — closed without merging, never landed

Twenty-one notes [verified] on pull requests that were closed unmerged and never
landed by any other route, spanning PRs #5620 to #5888 [verified]. Thirteen are
still recoverable from `origin/main`'s history; eight survive only on branch tips
[verified]. The set includes the physics-loop `inference-audit.md` methodology
document from PR #5652 [verified].

---

## The designed holes

Three mechanisms deliberately keep science out of the ledger. None of them is a
malfunction; all three are worth knowing about.

**Gated directories.** Certain directory families are listed in
`docs/audit/data/excluded_source_patterns.txt` as documentation or agent
infrastructure rather than auditable claims: `docs/repo/**`,
`docs/work_history/**`, `docs/lanes/**`, `docs/publication/**` and three
`docs/ai_methodology/` patterns [verified]. The file carries 45 pattern lines,
which match 711 of the markdown files present at the tip [verified]. At the tip
714 markdown files hold no row [verified], of which 499 are under
`docs/work_history/` [verified]; the two figures differ because 38 pattern-matched
files still hold grandfathered rows and 41 rowless files are gated by other means
[verified]. A further 200 files sit in `archive_unlanded/` [verified]. Note that
`archive_unlanded/` is **not** gated by a pattern line — it is outside `docs/`
entirely, so the registrar never scans it. Exclusion is also not retroactive
erasure: the seeder keeps any row that already carries a non-default audit
status, which is why 6 of the 505 markdown files under `docs/work_history/` still
hold grandfathered rows [verified].

**Notes created and deleted between pipeline runs are never seeded.** If a note
is added and withdrawn before the pipeline next runs, no row is ever minted for
it. The survey attributed roughly 24 such cases to July review churn; the data
shows 22, all dated July 2026, of which 19 are note-shaped and 1 has a row
[verified]. Successor notes were rowed normally.

**Rows are dropped when a note is deleted.** 4,247 distinct paths have held a
ledger row at some point; 3,972 hold one now; the difference of 275 paths have no
live row [all verified]. Of those 275, 241 are preserved elsewhere in the tree —
typically under `archive_unlanded/` — and 34 are gone from the working tree
entirely [verified]. Their audit history survives only in git history. Snapshots
of the old monolithic `docs/audit/data/audit_ledger.json` do survive on ref tips:
597 refs still carry the file, holding 2,234 distinct versions of it, spanning
2026-04-26 to 2026-07-13, and 44 of those refs are `archive/*` tags carrying 31
distinct versions [all verified].

---

## Flagged options for the audit lane

**None of the following was executed by this census.** They are options, listed
so the audit lane can price them. This document rules nothing.

1. **Backfill of pre-seeding-era rows.** Stratum 2 is 32 notes that were on the
   mainline and would have been rowed had the ledger existed a fortnight earlier.
   They are recoverable from archive refs. Backfilling them would bring the
   April flagships under the same audit discipline as everything since.

2. **An append-only row-retirement archive, instead of dropping rows.** Today a
   deleted note takes its row with it and the audit history is recoverable only
   by digging through git. A retirement archive would keep the row, marked
   retired, so 275 paths' worth of audit history stays queryable in place.

3. **A refresh cadence for `archive_unlanded/`.** The snapshot mechanism
   (`docs/audit/scripts/snapshot_unlanded_science.py`) last ran on 2026-04-27,
   covering 56 branches and preserving 138 files [verified from the archive
   manifest]. The directory has since grown to 200 files by other routes
   [verified], but the sweep itself has not been repeated. Everything in
   stratum 3 committed since then — the bulk of 3,074 notes — has never been
   snapshotted. A regular cadence would stop the branch-only tier from depending
   on branch tips surviving.

4. **Registration of the March stratum.** The 58 March claim notes and 194 run
   logs are outside `docs/`, so no change to the exclusion list reaches them.
   Registering them means either moving them under `docs/` or widening what the
   citation-graph builder scans. This is the only stratum that the current
   mechanism cannot reach at all.

---

## Known limits of this census

- Branch attribution is partial: 1,217 of the 3,074 branch-only notes carry a
  named branch [verified]. The rest carry the commit that first added them, but
  the branches holding that commit were not re-derived, because that needs
  another full-ref walk.
- The headline figure of 2,510 branch-only science notes is a **name-filtered
  subset** [verified]. The unfiltered count of `docs/*.md` that never reached a
  mainline and never held a row is 3,074 [verified]. The index carries all 3,074
  and flags which side of the filter each fell on, because the filter is not a
  clean split: 373 of the 564 filtered-out paths are treated as notes by the
  off-main sweep [verified].
- The March stratum is cut at the month boundary. The same `.claude/science/**`
  directory family accumulates 7,358 unique paths across the whole project
  [verified], and 84 further run logs first appear in April [verified]. Those are
  per-loop working scratch rather than era-defining science, and are not
  enumerated.
- Open and closed pull request items carry no creation date, because the survey
  read them from pull request objects rather than from commit history.
- Four ledger rows carry a claim identifier that does not match their note's
  filename — `kinetic_isotropy_primitive`, `minimal_axioms`,
  `realized_state_primitive` and `scale_reference_primitive`. All four point at
  notes that exist [verified]. These are naming mismatches, not orphans.
- No existing repository surface is a full census, and none claims to be.
  `RETAINED_BACKBONE.md` covers retained-grade claims only; `FRONT_DOOR_STATUS.md`
  projects ledger metrics; `STATE_OF_THE_THEORY_2026-07-16.md` is pinned to its
  date and defers to the ledger; `INTEREST_MAP` and the moonshot portfolio are
  April steering documents on the exclusion list. This census does not replace
  any of them, and does not outrank the ledger.
