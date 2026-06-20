# [physics-loop] single-clock-baxis-wall block05 — exercise reassessment + block02 no_go correction

**Honest status:** no_go reassessment / additive correction. No closure, no crack,
no new axiom. `proposal_allowed=false`; `bare_retained_allowed=false`;
`audit_required_before_effective_retained=true`. **Independent audit lane sole
authority.** Stacked on block04.

## Why this block exists

User directive: on hitting the B-AXIS wall, run the repo **exercise** skill from
first principles. The exercise (`.claude/science/exercises/baxis-wall-break/`,
5 max-reasoning slices) acted as a hostile reviewer and surfaced that the block02
unified no_go, while reaching the right verdict, was drawn **too strongly** in
specific checkable ways. This block VERIFIES the exercise's top routes with
runners and folds the corrections back additively.

## Verified routes (aggregate 143 PASS / 0 FAIL; no crack, no closure)

| route | clause | outcome | runner |
|---|---|---|---|
| R-FC-N5 | N5 | confirms_wall_sharper — block02's `span{I,Ĥ}` (linear) test is the **wrong algebra**; correct test is `{Ĥ}'' = {f(Ĥ)}` (dim = #distinct eigs, not 2). Wall **stands** only because the supplied many-body Ĥ is **degenerate** (2^Lₛ → 9/15/45 distinct eigs); genuine second-clock room = `2^Lₛ − #distinct` (7/49/211), not `(Lₛ−1)`. Right answer, wrong reason. | PASS=50 |
| R-COUNT-N4 | N4 | corrects_overclaim — the sole 959 consumer (ANOMALY_FORCES_TIME) reads only the **S₄-invariant count** `d_t ≤ 1`, never the axis label (verified verbatim). N4-as-label is **over-specified** for the cone; label-derivation stays walled (S₄-transitive). | PASS=16 |
| R-DICHOTOMY-N5 | N5 | shrinks_wall — the Lₛ-fold ⊗ₚ tower is the **free-fermion integrable** signature; a minimal A_min-admissible interaction collapses the commuting span 9→1. N5 holds **conditional on non-integrability** (one bit), not a `(Lₛ−1)`-param admission ray. | PASS=37 |
| R-KINFORM-N2b | N2b | confirms_wall_sharper — the form↔spacing identity `c_t/c_s == a_τ/a_s` is **false**; approved primitives grant only the form ratio, never the spacing ratio (registry rule 5). N2b stays open; **no crack**. | PASS=16 |
| R-DEFINABILITY | all | confirms_wall_sharper — Beth/Svenonius independence theorem; adding the four approved primitives does **not** fix a free quantity. **No crack.** | PASS=24 |

## Correction folded into block02 (additive, +119/−0, originals verbatim)

Appended a dated `## CORRECTION (2026-06-20, block05 exercise reassessment)` to
`docs/SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md`:
- **C-1** N5 linear-span → `{f(Ĥ)}` functional calculus (wall stands because Ĥ
  degenerate; room = `2^Lₛ−#distinct`, not `(Lₛ−1)`).
- **C-2** N5 Lₛ-fold tower is the free/integrable signature → one non-integrability bit.
- **C-3** N4-label over-specified for the sole consumer (reads only count `d_t≤1`).
- **C-4** scope hardened to A_min **+ the four approved primitives** (independence
  theorem; no crack); §5.2 sharpening (anisotropic `c_t≠c_s` form is the excluded
  one-axis enrichment, excluded only because kinetic_isotropy grants the isotropic
  S₄-transitive form).
- **C-5** net: verdict and direction **unchanged** — only the wall's shape/size/
  consumer-relevance amended; no boundary-flag flips.

Reassessment note: `docs/SINGLE_CLOCK_BAXIS_WALL_REASSESSMENT_NOTE_2026-06-20.md`;
consolidated runner `scripts/single_clock_baxis_reassessment_2026_06_20.py` (PASS=34/0).

## Net

B-AXIS is **not derivable** from A_min + the four approved primitives — verdict
unchanged, but the wall is **smaller, re-grounded, and consumer-scoped**: N4-label
dissolves *for the 959 cone* (count-only), N5 corrects to the Ĥ-degeneracy room +
one non-integrability bit, N2b stays open with the tempting kinetic-isotropy route
proven blocked. Every residual still funnels to the single emergent-dynamics open
gate. This is the loop self-correcting honestly via the exercise, not defending the
wall. Independent audit required before any retained-grade treatment.
