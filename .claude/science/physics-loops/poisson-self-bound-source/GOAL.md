# Goal — poisson-self-bound-source (cycle 713)

## Exact target contract

PR #5693 (cycle 712) closed with: *"any future self-consistency claim in this
lane needs a source term that is not the normalized propagator density."*

This cycle asks the question that successor poses, and asks it of the whole
operator family rather than of Poisson alone:

> Does the self-consistent construction in
> `self_consistency_forces_poisson_note` admit **any** source whose spatial
> extent is set by the physics rather than by the box; and if so, does the
> operator family separate on that criterion?

## What counts as an answer

A source is **self-bound** on this surface when, at fixed coupling `g` and with
the box `N` increasing:

1. the RMS extent of `rho` converges to a finite limit, and
2. the depth of the self-consistent well `|min V|` converges to a finite limit.

Condition 2 is the load-bearing half. A state whose extent stops growing can
still be held by a well that deepens without bound as the box grows — that is
box-squeezing by an operator with no decaying far field, not self-binding. The
landed `FROZEN_STARS_RIGOROUS_NOTE.md` reports condition 1 only, and reports it
in 1D; its own 3D table shows the width still growing at the largest box it ran.

## Non-goals

- No claim about the continuum limit of the lattice theory.
- No claim that the tested operator family is exhaustive among local operators.
- No restoration of the parent note's `beta` diagnostic as evidence; PR #5693
  showed that diagnostic is inverted under the parent's own window.
- No new axiom and no new framework primitive. The construction uses only the
  lattice Laplacian already present in the parent runner, its own operator
  family, and the eigenvalue problem for the lowest state.
