# Goal: scale-ladder campaign 20261018

- **Budget:** 12 h, 2026-10-18T02:14Z to 14:14Z.
- **Branch:** `claude/scale-ladder-campaign-20261018`, stacked on PR #9702.

## Direction

The owner asked for a 12-hour goal on the scale ladder and delegated its design. The working picture comes from the scale-ladder note (PR #9702) and from the owner's own correction, "the speed limit is related to the base grid; prefer information-minimal". The finest rung is a one-qubit-per-site grid. Higher rungs are coarse-grained neighbourhoods. The ladder unifies lanes when some data provably survives the climb.

## Campaign question

Can one parameter-free local step rule on the base grid serve as the common origin of the low rungs, fixing the speed from the grid alone? And can the strongest lane-probe reframings be turned into theorems or decisive computations?

## Blocks

Ranked by expected evidence value; the live order is in OPPORTUNITY_QUEUE.md.

- **B1. Parameter-free corner fermion.** Find a step rule with no continuous parameters that has all of the following:
  - built from canonical corner-model operators;
  - commutes with the gauge-dressed site rotations and the translations;
  - a Weyl or Dirac node at k* carrying the spin-½ class;
  - a speed fixed by geometry;
  - anisotropy of order (a/w)²;
  - no flat bands at the node.

  Or prove the obstruction inside a declared class.
- **B2. Common origin.** Do composite excitations of the same rule (pairs, and particle–hole bosons) inherit the constituent speed? Does a gauge-like field built from the rule share it?
- **B3. Formation coding-radius theorem.** iid-priority, finite-range formation is a finitary factor of iid noise with a super-exponential coding-radius tail. Covariances therefore decay super-exponentially, which excludes long-range order and pinch points from an empty start. Write the proof and check it numerically.
- **B4. Gravity g3.** Extract the cubic electric invariant g3 and the full long-wavelength symbol from the repo's curvature-member stencil and from the Regge Hessian. Is graviton birefringence present or protected?
- **B5. Record clock hypothesis.** On the campaign's reduced one-excitation device, do the bond tolerances scale as 1/M only under the phase-including metric? That would locate the fine-tuning in a phase reference.
- **B6. Maxwell winding sectors.** Measure ΔE(W)·L and K_T(2π/L) against χ_L for L > 2 where computable.
- **B7. LSM-type constraint for the corner model.** Does the projective symmetry group plus the filling forbid a trivial symmetric gapped state at the node filling?
- **B8. Ergodicity route to frequency consistency (Born lane).** For order-blind 1-dependent fields, state and check the theorem.

## Contract

- Each block delivers one of: an exact classification or construction inside a declared model class, a proved obstruction, or a decisive computation. Models are supplied premises.
- No new axioms.
- No physical identification in theorem text.
- Independent checks are run by fresh-context same-model-family agents, and reported as such.

## Delivery

- Milestone PRs.
- PR #9702 is revised first, with the parameter-free step-rule material, as the owner requested.
