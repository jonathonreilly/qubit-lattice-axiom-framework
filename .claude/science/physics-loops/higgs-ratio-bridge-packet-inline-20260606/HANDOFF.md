# Handoff

## What changed

This branch inlines the Higgs bridge packet into the parent ratio artifact. The
parent note now lists the bridge notes, runners, and caches. The parent runner
now verifies source markers and SHA-fresh cache evidence for both bridge
runners.

## Why it matters

The recent conditional blocker asks for a retained one-hop bridge deriving the
`d=4/Z^4` taste count `N_taste = 16` and the mean-field determinant `W(J)` form
used in the curvature calculation. This branch makes that packet explicit and
checkable from the parent artifact.

## Remaining blocker

Independent audit must decide whether the bridge packet is retained-grade. This
branch should be treated as `exact-support`, not as a self-applied status
promotion.

## Exact next action

Run review-loop/audit on the branch and, if accepted, re-audit
`higgs_lattice_eigenvalue_ratio_narrow_theorem_note_2026-05-02` against the now
explicit bridge packet.
