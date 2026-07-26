# Cycle 707 — BACKLOGGED as a theorem; erratum carved out

Branch: `physics-loop/confusability-floor-20260725`
Commits: `4a52949d69` (runner), `51f76bce45` (receipt + value gate)
Cluster-cap evaluator (codex `gpt-5.6-sol`, xhigh): **BACKLOG**.

## Confirmed, and kept

The evaluator independently verified the correction, including the part I
added mid-cycle:

> "P4 really pairs `S=L√(1−φ)` with `0.50`, while ACTION_UNIQUENESS tests
> `L(1−√f)`; these are distinct, and the former has linear depth
> `1−√(1−f)=f/2+O(f²)`. But canonical spent-delay is the third formula
> `L[1+f−√(2f+f²)] = L[1−√(2f)+O(f)]`, genuinely sublinear. Thus P4 misstated
> the formula, not the intended universality class."

This is carved out as an erratum (see below). It is confirmed twice over: by
the runner and by `scripts/action_universality_probe.py`, whose `action_value()`
defines the tested mode as `valley_sqrt -> L * (1.0 - np.sqrt(f))`.

## Error 1 (real) — Rellich needs analyticity, not just self-adjointness

I claimed the `p = 1/2` exclusion was **unconditional**, needing "only
self-adjointness". Wrong. Rellich requires the family to depend **analytically**
on the coupling. A self-adjoint but non-analytically parameterized family can
carry a half-power. And analytic dependence is close to assuming the linear
coupling that was to be explained.

Worse, row F's logic runs backwards as a necessity proof: it exhibits a
non-self-adjoint family *permitting* a square-root branch, which does not show
that every half-power *requires* non-self-adjointness. I asserted the converse
of what I demonstrated.

## Error 2 (real) — Theorem 4 was not a premise reduction

A2 is `L^{-1} = G_0`; the additive coupling `H(φ) = H + φ` is a *separate*
heuristic bullet in the same note; and neither implies the path-action rule
that admission (c) is actually about. With the propagator-to-action seam still
open, admission (c) was moved onto **two** unforced bridges, not collapsed into
one. The note's headline and the value gate both advertised a collapse.

## Error 3 (real, and the worst one) — row G sliced away its own counterexample

Row G listed `hill = [1+f, -f]` and then tested `all(... for g in hill[:1])`,
silently omitting `-Lf`. `g(f) = -f` has `g'(0) < 0`, which contradicts the
"hill ⟹ g'(0) > 0" classification the row asserts. (The real point is that
`-Lf` fails the `g(0) = 1` normalization and is outside the class — but the row
never said so; it just dropped the case.)

This is the same defect the campaign claims to guard against, committed in the
row whose job was to be a control. The `hill[:1]` slice should never have been
written, and grepping for always-true rows does not catch a test that quietly
narrows its own domain.

## Pattern

Sixth consecutive gate rejection, and the shape has not changed: the arithmetic
is correct every time, and the inference from it overreaches. Cycle 707 changed
target *selection* successfully — a named admission on a `critical` root row
with 773 descendants, which the evaluator did not dispute as a target — but did
not change the inference discipline. Choosing a better target does not fix
claiming more than was shown.

## Carve-out

Rows A, B and I are exact, confirmed, and independent of every objection above.
They are being reissued as a standalone erratum with all Rellich, premise-
reduction, and sign-classification content removed. See
`docs/ERRATUM_..._2026-07-26.md` and
`scripts/physical_weak_field_action_form_erratum_cycle707b_2026_07_26.py`.
