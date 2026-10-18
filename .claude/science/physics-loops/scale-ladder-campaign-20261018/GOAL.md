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

## Phase 2 (owner: "run for another 12 hours"; 2026-10-18T11:26Z to 23:26Z)

Phase 1 established three things:
- constraint closure ties every matter cone to the graviton's cone, in the continuum at leading order;
- closure rejects anisotropic cones;
- no tested parameter-free step passes that rule, because its D4 doublers are uniaxial.

Phase 2 attacks the open items that decide whether the information-minimal target survives.

- **C1. Gapping the doublers.** Can a symmetric pairing term, or an interaction that conserves number, gap the six D4 doublers while the isotropic ±k* species stay gapless? The low-energy content would then pass the selection rule. Pairing route: free-fermion BdG symmetry analysis. Interacting route: symmetric mass generation, with anomaly bookkeeping.
- **C2. Seagull from closure.** Does closure at the next order (h² · matter²) fix the seagull that the 06-08 induced bubble needs, and hence the induced 1/G?
- **C3. Exact lattice closure.** Is non-locality necessary? Either prove that no local lattice discretisation in a declared class closes {G, C} exactly, or construct a non-local one that does.
- **C4. Microscopic normalisation of h.** In the repo's qubit realisation, does the bounded spectrum or the operator content fix the scale of h? That would derive r = 1, equivalently K1 = K2.
- **C5. Checks and gaps.**
  - Checks of B23, B24 and B11.
  - A screen of the multifold (G3/2-mixed) k* levels.
- **C6 (stretch). Rung 0 → 1.** What map takes the formation rung to the corner model?

The contract is unchanged.

### Phase 2 follow-ups (added 17:15Z)

- **C8. Letters outside the phased-permutation class.** B26 shows that S^a and A0·S^a are the only O-covariant phased-permutation letters. Do momentum-shifting letters (translation-covariant only up to a character, i.e. a doubled cell) or antiunitary letters give new velocity sources or new tastes at ±k*? Can any of them make a step whose node quasi-energy is reached only at isotropic cones of one speed?
- **C9. Field-dependent structure functions and the arc lemma.** C3's arc lemma covers field-independent structure constants. Does a lattice relabelling algebra with field-dependent structure functions evade it? First test linearisation around the flat background: is the zeroth-order part a constant-structure algebra to which the lemma applies? Then test the first-order corrections.
- **C10 (added 17:55Z). Lattice Hamiltonian constraint with structure functions.** C9 shows that closure is automatic for generators linear in π. For a 1D lattice H constraint (scalar, optionally with an embedding pair), is there a local, translation-covariant, non-abelian, first-class lattice constraint algebra with the right continuum limit? Or is the naive one anomalous, and if so, why?
- **C11 (added 18:45Z). Generalised L1.** Prove by Schur's lemma and Wigner–Eckart that every product of O-covariant letters has an untilted isotropic cone at ±k*, with a speed that is additive over per-letter coefficients. Verify this on generic letters.
- **C12 (added 21:00Z). Winding letters.** Is there an O-covariant translation-invariant letter with 3D winding W₃ ≠ 0? Such a letter would escape the zero-net-chirality input to the doubling obstruction. The block has a hard 85-minute limit.
