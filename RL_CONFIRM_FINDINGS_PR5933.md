# PR #5933 Review-Loop Confirmation — Iteration 2

Scope: confirmation of local fix commit `1a3bcaa60cae9d22bc2dc80c0c06fea8a3669ff5` on `rl-fix-5933`, relative to the reviewed PR head `c28a1e42f7`, using `RL_FINDINGS_PR5933.md` and `RL_FIXDIFF_PR5933.txt`. This was a read-only confirmation round apart from this requested report; no source, science, audit-ledger, queue, or verdict artifact was edited.

## Finding dispositions

### F1 — FIXED

The arbitrary-dissection result is now stated consistently as a lower bound, not an attained minimum. The note explicitly says that `56` is not an attainment or disjointness-immunity claim (`docs/PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md`, lines 110–123 and 188–189), and the runner repeats that boundary (`scripts/physical_scale_free_adjacency_dissection_bracket_cycle724_2026_08_03.py`, lines 23–28 and 243–249). Remaining attainment language concerns either a genuinely attained per-cell floor/witness or explicitly records/negates the removed broad claim.

### F2 — FIXED

The supplied-model boundary and open bridges are explicit. `Lattice` supplies only spatial `Z^3` nearest-neighbor adjacency; the kinetic-isotropy primitive supplies only equal tick/edge graining; the simplex/dissection/refinement model is separately supplied. Physical tick–`Admissibility`, the identification of physical cells with those simplices, and nonsimplicial 1-skeleton routes remain open (`...CYCLE724_NOTE_2026-08-03.md`, lines 20–43 and 176–203; runner lines 3–31). The dependency discussion links the registered inputs without claiming that they close those bridges.

### F3 — FIXED

The citation edges are corrected and the tracked manifest is the exact repository-generator result. Independent regeneration at both endpoints found:

- base: 4,633 nodes, 15,425 edges;
- fix HEAD: 4,633 nodes, 15,424 edges;
- exactly one node record changed: Cycle 724 `out_degree` `3 -> 2` and `deps_hash` `bb5dc2c6f64d -> 0d988fd1ac07`;
- exact edge delta: removed Cycle 724 → Cycle 695 and Cycle 724 → Cycle 690, added Cycle 724 → `kinetic_isotropy_primitive`, while Cycle 724 → `minimal_axioms` remains.

The regenerated HEAD manifest is byte-identical to the tracked file (SHA-256 `0ad82746bb04feb73dae212b85124f60f7f641e62cc04caa30fd53a8ec7f72e9`). Thus the aggregate `edge_count` change is exactly `15425 -> 15424`, with no other node change.

### F4 — ACCEPTABLY_DEFERRED

The Cycle 721/722/723 lineage remains intentionally provenance-only rather than becoming a dependency or scientific premise. The identifiers are backticked and explicitly declared non-load-bearing (`...CYCLE724_NOTE_2026-08-03.md`, lines 249–262); the artifacts are absent from both HEAD and `origin/main`; the runner neither names nor reads them and reconstructs its tested domain internally; and the citation graph contains no lineage edges. This disclosure is acceptable and requires no science fix.

### F5 — FIXED

`disjoint_lp` is fail-closed. It returns disjoint only for `res.status == 2`; every other unsuccessful solver status raises instead of being classified as disjoint (runner lines 330–364), so the exception aborts before the 2,016-pair PASS gate. An isolated mock check confirmed status 2 returns true and statuses 1, 3, and 4 raise `RuntimeError`; successful optima retain the documented tolerance classification.

### F6 — FIXED

Determinants and rank decisions now use exact integer arithmetic: scalar and batched cofactor determinants plus fraction-free Python-integer rank (runner lines 85–136). All determinant/rank call sites use those routines; no `numpy.linalg` determinant/rank or other floating determinant/rank decision path remains. Independent checks matched a separate Leibniz determinant and rational RREF on thousands of random integer matrices, plus exhaustive small-matrix rank cases. Floating point remains only in display conversion and the explicitly disclosed LP comparator.

### F7 — FIXED

The theorem is correctly demoted and narrowed to the exact pairwise spatial-nearest-neighbor simplex model. The note defines that grading, proves the spatial clique/affine-rank ceiling, and draws only the resulting 3-/4-simplex conclusion (`...CYCLE724_NOTE_2026-08-03.md`, lines 63–83 and 178–187). It explicitly preserves nonsimplicial cells and the physical realization bridges as untested/open. The exact combinatorial core is closed; the overall claim remains conditional on the disclosed supplied simplex/dissection model. The Review record documents the demotion.

### F8 — FIXED

Vocabulary and scope are corrected. `Lattice` is capitalized and limited to the registered spatial-adjacency role; `Admissibility` appears only in the canonical open-bridge name. No all-caps `LATTICE` or “define the admissible set” conflation remains in the changed note, runner, output, or receipt. `scripts/vocab_lint.py --report-only` reported zero violations.

## Required confirmation checks

- Fresh cold runner: exit 0; `PASS=23`, `FAIL=0`; the emitted science receipt is byte-identical to the committed receipt. Removing the newly added `review_loop` provenance object leaves every pre-fix science key/value unchanged.
- Independent science census: reproduced 3,008 nondegenerate cases, per-cell floor 3, 64 floor cells, ratio 56 at `(7,3)`, floor-cell ratio 72, and unimodular profile `{3:64, 4:384, 5:1152, 6:768, 7:304}`.
- Fix-diff integrity: `RL_FIXDIFF_PR5933.txt` matches `git diff c28a1e42f7..HEAD`; Python compilation and `git diff --check` pass.
- Audit compatibility: the disposable validation pipeline, strict audit lint, and changed-audit-evidence gate all pass. Temporary materialization classifies Cycle 724 as `bounded_theorem`, `unaudited`, with dependencies `[minimal_axioms, kinetic_isotropy_primitive]`. The PR ships no ledger row, queue mutation, effective-status change, or audit verdict.
- Repository hygiene: portable-link and controlled-vocabulary checks pass; the only committed audit/control-plane delta is the required citation manifest.

## No-go and reviewer summary

N1–N8 pass for the narrowed claim. The exact target survives the clique/parity, repeated-site/multiple-tick rank, arbitrary-tick, refinement/rescaling, and non-corner/box checks. Supplied structure is not conflated with derived physics; all registered inputs are explicit; prior-cycle material is provenance-only; and the claim is per pairwise-adjacency simplex rather than lattice-wide or a physical-realization theorem. The cube/hypercube nonsimplicial counter-route is explicitly preserved, so it defeats only the former broad claim. The result is consistent with the active review queue and the repository's adjacency-as-hypothesis precedent.

| Review lens | Result |
|---|---|
| Code / runner | PASS |
| Physics claim boundary | BOUNDED |
| Proof obligations | CLOSED on exact core; CONDITIONAL on supplied model |
| Imports / support | DISCLOSED |
| Nature retention | BOUNDED |
| No-go discipline | PASS |
| Labeling convention | PASS |
| Repository governance | PASS |
| Audit compatibility | PASS |

No new blocking finding was identified. The fix is confirmation-ready as a bounded, explicitly conditional claim; this confirmation does not itself promote the claim to retained grade.

CONFIRMATION: PASS
