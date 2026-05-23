# Lattice Gravity Resolution: 3D Dense Spent-Delay z = 2..5 Attractive Window

**Date:** 2026-04-04 (original); narrowed 2026-05-23
**Status:** bounded — the 3D dense spent-delay branch at ultra-weak field
`strength = 5e-5` retains an attractive same-family barrier card on the
runner-computed `z = 2, 3, 4, 5` window. Audit verdict and effective
status are the independent audit lane's decision.

## 3D dense spent-delay card (runner-supported window)

The retained surface of this note is the 3D dense spent-delay branch at
ultra-weak field with the supplied 10-property card. On the runner's
configured probe:

- Born `7.39e-16`
- `MI = 0.1414`
- decoherence `13.5%`
- centroid-side distance exponent `-1.62`, `R² = 0.976`

Under the gravity-observable hierarchy classifier, the runner-computed
`z = 2, 3, 4, 5` window is genuinely attractive on this retained tested
card.

So the safe 3D read here is:

- **the dense spent-delay branch retains a real attractive window on the
  current tested `z = 2..5` card**
- **this is not a clean all-distances attraction theorem**

Important correction (retained from the original note):

- the corrected `h = 1.0` vs `h = 0.5` refinement comparison does **not**
  preserve any older positive-refinement narrative
- the attractive 3D dense card is real at the retained reference point,
  but it is **not** a refinement theorem
- the new reconciliation note freezes that failure explicitly

## The mechanism (informational)

At ultra-weak field, the phase perturbation per edge is tiny.
The TOTAL perturbation over all paths is the coherent sum of
many small perturbations. In the LINEAR response regime, this
sum shifts the centroid TOWARD the mass (constructive interference
on the mass side from the phase valley).

At stronger field, the perturbation is large enough to cause
destructive interference at the beam center. The depletion
effect dominates, shifting the centroid AWAY.

The transition between TOWARD and AWAY happens at the field
strength where the per-edge phase perturbation exceeds ~1/k.
Below this, linear response → attraction.
Above this, nonlinear disruption → depletion.

## Open question

The next question for the 3D dense spent-delay branch is whether the
hierarchy-clean attractive window can be extended past `z = 5` while
keeping the same same-family barrier card. That extension is **not**
currently supported by the registered runner or the cited hierarchy
authority.

## Audit verdict acknowledgment (2026-05-23)

Audit verdict (`audited_failed`, leaf criticality, prior audit
2026-05-10):

> Issue: the note overclaims beyond both its supplied runner and its
> only cited authority, especially by retaining z = 6 and the 2D all-b
> distance-law table without supporting restricted evidence. Why this
> blocks: a bounded theorem cannot be audited clean when its stated
> retained window includes points the runner does not compute and the
> cited authority explicitly excludes from ratification. Repair target:
> split the runner-supported 3D z = 2..5 card from the broader
> narrative, add or cite audited artifacts for z = 6 and the 2D
> b-window, and align the hierarchy dependency scope. Claim boundary
> until fixed: only the raw supplied runner output for the h = 1.0,
> L = 12, W = 6, max_d = 3, strength 5e-5 3D card is locally evidenced.

This 2026-05-23 narrowing complies with the verdict's preferred repair
target by splitting the runner-supported 3D `z = 2..5` card from the
broader narrative. Concretely:

- **Dropped:** the 2D dense-lattice all-b distance-law table (b ∈ {4,
  5, 6, 7, 8, 10, 13, 16, 19}, distance law `b^(-0.94)`, `R² = 0.939`).
  The supplied runner does not compute the 2D card, and no one-hop
  audited authority closes it.
- **Dropped:** the 3D `z = 6` row. The registered runner
  `scripts/lattice_3d_dense_10prop.py` iterates `z_mass ∈ {2, 3, 4, 5}`
  only, and the cited hierarchy authority's retained scope is
  explicitly narrowed to dense `z = 3` and `z = 5`. The `z = 6` row had
  no in-packet executable verification.
- **Kept:** the 3D dense spent-delay attractive window on `z = 2..5`,
  the same-family barrier card (Born, MI, decoherence, centroid-side
  exponent on this card), the mechanism prose, and the refinement
  correction.

The hierarchy dependency scope is therefore aligned with the
runner-supported `z = 2..5` window of this note (the hierarchy
authority itself ratifies `z = 3` and `z = 5` directly; `z = 2` and
`z = 4` are part of the runner-computed iteration but extend past the
authority's explicit retained rows). The note does not claim a clean
all-distances attraction theorem.

## What this note does NOT claim

- The 2D ultra-weak spent-delay 9/9 attraction or its
  `b^(-0.94)` distance-law table (no supplied runner; no one-hop
  audited authority).
- Attraction at `z = 6` on the 3D dense spent-delay card (runner does
  not compute it; cited hierarchy authority excludes it from
  ratification).
- A refinement theorem at `h = 1.0` vs `h = 0.5` (the corrected
  comparison does not preserve the older positive-refinement
  narrative).
- An all-distances attraction theorem.

## Artifact chain

- [`scripts/lattice_3d_dense_10prop.py`](/Users/jonreilly/Projects/Physics/scripts/lattice_3d_dense_10prop.py)
- [`GRAVITY_OBSERVABLE_HIERARCHY_NOTE.md`](GRAVITY_OBSERVABLE_HIERARCHY_NOTE.md)
