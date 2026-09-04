# Key science — the front-of-house index

This file is the canonical entry point to the primary (audited) track.
It is an index only: it names where the key science lives and grants no
status by listing. The repo runs two tracks — this primary track
(`docs/` + the audit lane), and the archive track (`archive/`, record
without authority; start at `archive/README.md` → `archive/SCIENCE.md`).

## The foundation

- **Axioms:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
  — the four named axioms (Lattice, Qubit, Admissibility, Record), revised
  in place (the file records its own revision history, including the
  2026-08-05 Admissibility distribution sentence and the 2026-08-13
  Record scalar-functional removal). Read it in full before foundations
  work; earlier `MINIMAL_AXIOMS_*.md` files are historical epochs.
- **Approved primitives:** [`audit/data/axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json)
  with their source notes
  ([scale reference](SCALE_REFERENCE_PRIMITIVE_NOTE.md),
  [kinetic isotropy](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md),
  [realized state](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)) — each
  grants exactly what its note declares, nothing more.
- **Vocabulary and policy:**
  [`repo/CONTROLLED_VOCABULARY.md`](repo/CONTROLLED_VOCABULARY.md),
  [`KEY_TERMINOLOGY.md`](KEY_TERMINOLOGY.md), the axiom-minimality policy,
  and `audit/data/premise_decision_history.json` (governance record).

## The audited claim surface

- **Ledger:** the sharded machine ledger
  `audit/data/ledger/<xx>/<claim_id>.json` (the rendered `AUDIT_LEDGER.md`
  is materialized locally by the pipeline, not tracked);
  pipeline: `audit/scripts/run_pipeline.sh` (mechanical; verdicts come only
  from the independent audit lane).
- **Standing derivation obligations (open gates):**
  [`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md),
  [`AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md`](AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md),
  [`THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md`](THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md).

## What stays front-of-house

The 2026-09 densify freeze partitioned the note stratum (3,262 candidates,
all read in full): 2,418 FRONT claims stay on this track; 797 archived
notes moved to `archive/notes/` behind 21 era memos (`archive/chains/`),
with `archive/PATHMAP.tsv` mapping every moved path. The freeze evidence
(partition lists, gates, adversarial attack + checker passes) is
`archive/campaigns/densify-freeze-20260904/`. Consolidated-PR history:
closed PRs labeled `work-history`, indexed in `archive/LEDGER.md`.

## Live work

Live campaign records and AI planning surfaces live on the standing
`ai/execution` branch and in working trees, not on `main`
(see the repository `CLAUDE.md`). Open FRONT terminals and the live
mainline stack remain open PRs.
