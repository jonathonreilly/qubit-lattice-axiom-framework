---
claim_id: graph_braid_z3_anyon_exclusion_dichotomy_dep_resolution_hygiene_companion_note_2026-06-04
claim_type_author_hint: meta
---

# Graph-Braid Z3 Anyon-Exclusion Dep-Resolution Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dependency-surface hygiene evidence)
**Status:** companion-only. This records that the parent
[`GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md`](GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md)
keeps the statistics-agnostic note as plain-text non-load-bearing context,
while the parent runner's cached artifact still verifies the graph-braid
calculation. It is not a new no-go claim, not a direct status change, and not
independent audit work.
**Companion target:** `graph_braid_z3_anyon_exclusion_dichotomy_narrow_theorem_note_2026-05-29`
**Primary runner:**
[`scripts/audit_companion_graph_braid_z3_anyon_exclusion_dichotomy_dep_resolution_2026_06_04.py`](../scripts/audit_companion_graph_braid_z3_anyon_exclusion_dichotomy_dep_resolution_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_graph_braid_z3_anyon_exclusion_dichotomy_dep_resolution_2026_06_04.txt`](../logs/runner-cache/audit_companion_graph_braid_z3_anyon_exclusion_dichotomy_dep_resolution_2026_06_04.txt)

## Claim Boundary

The parent theorem's load-bearing framework input is the per-site Hilbert
dimension note. The statistics-agnostic note is context for the open
second-quantized bridge; the parent says nothing depends on that note's tier.
This companion makes that boundary graph-visible by keeping the
statistics-agnostic reference as plain text rather than a Markdown citation.

The parent runner itself is unchanged. Its current cache records
`SCORECARD: PASS=25 FAIL=0`, with exact Smith-normal-form / graph-planarity
checks for the first-quantized graph-braid calculation. Because the local
default Python in this review environment lacks `networkx`, this companion
verifies the parent cache against the current parent-runner hash rather than
re-executing the parent runner directly.

## What This Does Not Claim

- It does not add a new no-go or strengthen the parent.
- It does not select boson vs fermion.
- It does not close the second-quantized gauge-coupled bridge.
- It does not promote the parent or this companion.
- It does not edit audit verdicts or generated status files.

The safe downstream use is only this meta evidence: the parent no longer uses
a Markdown citation for its non-load-bearing statistics-agnostic context, and
the parent runner artifact still matches the current parent runner.
