# Physics-loop GOAL — Dirac corner-coupling (the gated Koide derivation)

**Slug:** dirac-corner-coupling
**Launched:** 2026-06-04, 12h overnight campaign, Dirac-first with fan-out, --literature on (comparators only).
**Target status:** best-honest-status (close the corner coupling -> derive lepton Q=2/3 if possible; else sharpest obstruction / no-go).

## Core question

Derive the inter-generation hopping vs on-site ratio `|b|/a` of the C3-circulant
generation Yukawa `H = a I + b C + b-bar C^2` from the staggered-Dirac /
Kahler-Dirac realization on the three **hw=1** (Hamming-weight-1) corners of the
cubic Brillouin zone `{0,pi}^3` — the corners `(pi,0,0),(0,pi,0),(0,0,pi)` cycled
by the C3 axis-rotation — and test whether `|b|/a = 1/sqrt(2)`, i.e. whether the
dynamical corner coupling gives `r = |b|^2/a^2 = 1/2` (Koide `Q = 2/3`) for a
color-singlet (clean) fermion.

## Why this direction (the trace)

- Just-shipped no-go #2591 proved `r=1/2` is NOT protected by any unitary
  symmetry (S3 forces degeneracy; C3 leaves r free; singlet 1-dim vs doublet
  2-dim cannot be swapped). So `r=1/2` is a dynamical norm-balance
  (`3a^2 = 6|b|^2`, equal C3 singlet/doublet channel energy) and must come from
  the staggered-Dirac corner coupling, not symmetry.
- This is the SAME staggered-Dirac realization gate the 3-generation structure
  already rides on. Koide and the gate are the same problem now.

## Payoffs if `|b|/a = 1/sqrt(2)` derives

1. Derives charged-lepton Koide `Q = 2/3` from first principles (conditional on
   the staggered-Dirac gate).
2. Predicts neutrinos (color-singlet, like charged leptons) also at `r=1/2 ->
   Q=2/3` -> a specific relation among the 3 neutrino masses. The framework is
   currently neutrino-mass-blind, so this would be genuinely NEW and
   out-of-sample (testable at DUNE / cosmology / 0nubb).
3. Explains why quarks (color-triplet) DEVIATE (color adds to the coupling;
   empirically down r~0.60, up r~0.77). The complex phase delta that splits the
   doublet is the staggered eta-phase.

## Discipline (non-negotiable)

- Reprove every math fact from framework primitives in companion runners
  (exact/sympy). Literature (Kawamoto-Smit, staggered fermions) is comparator
  only, never a derivation input (forbidden-import rule).
- Match claim_type to verdict; narrowest honest status in branch-local notes
  (no bare `retained`/`promoted`). The staggered-Dirac realization is itself an
  open gate, so a clean corner result is CONDITIONAL on it.
- No new axioms. No audit-lane data in PRs. Science-only on dedicated branches;
  one review PR per coherent block.
