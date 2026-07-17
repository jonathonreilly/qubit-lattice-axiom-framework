# PR body draft — block03 (final numbers synced before opening)

**Stacked PR**: base = `physics-loop/born-effect-menu-horn-block02-20260717`
(block02, PR #5476; itself stacked on #5472). Cluster-cap evaluation for
PR #3 in this family: OPEN (recorded in
`CLAIM_STATUS_CERTIFICATE_BLOCK03.md`).

## Summary

Block 03 completes the lane's menu-family map at session scale, taking both
remaining executable queue slices in one block:

- **T1/T2 — The outcome-count threshold is exactly three.** Two-outcome
  effect menus do not force the Born trace form: the smooth witness
  `w0 = f(Tr(sigma0 ·))`, `f(t) = t^3/(t^3+(1-t)^3)`, satisfies every
  binary normalization exactly and refutes every trace form (exact
  three-point non-affinity), while violating the ternary menu
  `{(1/4)1,(1/4)1,(1/2)1}` at exactly `4/7`. Adding three-outcome menus
  restores partial additivity (the block01 step-(A) elimination, whose
  only ternary input is now isolated) and with it the full effect-grade
  forcing chain. Sorkin's hierarchy cited as comparator analogy only;
  two-outcome insufficiency acknowledged as comparator folklore, witness
  native and gated.
- **T3 — Mixed-projective forcing (native mixture class).** Menus
  presentable as finite classical mixtures of binary projective
  measurements and coins with exact outcome splitting and merging force
  the Born form on their element domain, with no imported literature
  theorem. New mechanism: a merge/decomposition-invariance lemma — merged
  elements take decomposition-independent values — which turns the halved
  block02 axis-cancellation identity (two decompositions of `(1/2)1`) into
  the affinity equation. Closes block02's named open increment natively
  (Wright-Weigert 2019 stays comparator; no class identity claimed).
- **T4 — Incomparability: no unique minimal forcing family.** The merged
  element `(1/2)P(e_z)+(1/2)P(e_x)` (eigenvalues `(2±√2)/4`) lies outside
  the scaled-projector family; the coplanar three-element menu admits no
  mixture presentation (rank-1 elements force parallel pieces; the three
  directions are pairwise at `cos = −1/2`; coins fit inside no rank-1
  element). The witnessed forcing families form no chain, so no unique
  inclusion-minimal forcing family exists among them.
- **T5 — Scaled-grade consistency.** Binary scaled menus are exactly
  projective menus and coins (eigenvalue characterization) — inside the
  block02 paired subfamily, already twice-witnessed as non-forcing.

## Changes

- `docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md`
- `scripts/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.py` (44 gates)
- `logs/runner-cache/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.txt` (SHA-pinned)
- `docs/audit/data/citation_graph_manifest.json` (stage-18 refresh: 1 added node relative to block02)
- Loop pack block03 files under `.claude/science/physics-loops/born-effect-menu-horn-20260717/`

## Value gate, no-go gate, cluster cap

V1-V5 and the cluster-cap evaluation (verdict OPEN) in
`CLAIM_STATUS_CERTIFICATE_BLOCK03.md`; N1-N8 answered jointly for the T1
and T4 negatives inline in the note.

## Review rounds applied

Supervisor pre-battery (10/10) before authoring. Four-lens adversarial
panel: lens 1 clean (0/0/0, incl. flip-sign self-test); lens 3 found no
counterexample and contributed four adopted repairs (coin-primary T1
refutation gated on a generic normalized state; region-general
hypothesis restatement; separate-outcomes representation route for
trace>1 merged elements, gated at trace 7/5; sign(0) and c=0 endpoint
fixes); lens 4 governance corrections all applied (T4's own N4/N6/N7
including a PSD-parallelism steelman; "force nothing" narrowed;
dimension scoping; trace-gate target clarity; cluster-cap wording
de-collided); lens 5 convergent narrowings applied (iterated-pairwise
homogeneity wording; planned-slices completion instead of map
completion). Synthesis in REVIEW_HISTORY.md.

## Mutation checks

Twelve families (F, T1, T1f, T2, T3b, T3c, T3d, T3f, T4a, T4c-parallel,
T5, N), one load-bearing mutation each, all FAIL correctly — including
the T4c probe whose parallel degradation fails exactly per the
parallelism lemma. Table in REVIEW_HISTORY.md.

## Test plan

- [x] Runner `TOTAL: PASS=44 FAIL=0`; cache SHA-pinned and verified
- [x] Pipeline clean on stacked branch; derived churn restored to the
      block02 branch state; locally seeded shards dropped; only the
      manifest delta staged
- [x] audit_lint --strict OK; vocab_lint clean
- [x] Quotes machine-verified bidirectionally (both parents + axiom memo)

Independent audit remains required; landing is not ratification; retention
is the audit lane's decision alone.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
