# Handoff

## What changed

This branch adds a periodic plane-wave density-kernel bridge and wires it into
the generation localization parent row. The bridge derives the finite torus
Laplacian eigenbasis, mediator eigenvalue `Vq(q)`, and Hartree-Fock
`1/N` normalization used by the corner calculation.

## Why it matters

The latest audit blocker was dependency scope. The parent arithmetic already
passed; this branch supplies the missing source-side bridge from the
retained-bounded mediator family to the periodic plane-wave kernel.

## Remaining blockers

Independent audit must certify the bridge. The physical magnitude remains
open: this PR does not derive `G`, `mu^2`, effective `N`, or any flavor value.

## Exact next action

Run review-loop/audit on this branch. If accepted, re-audit
`generation_localization_momentum_corner_delta_ji_protected_narrow_theorem_note_2026-06-06`
against the bridge packet.
