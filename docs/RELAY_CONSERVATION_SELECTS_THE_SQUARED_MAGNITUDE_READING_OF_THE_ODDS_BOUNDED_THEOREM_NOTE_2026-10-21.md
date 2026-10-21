---
claim_id: relay_conservation_selects_the_squared_magnitude_reading_of_the_odds_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Conditional on CL-4, CL-6, a tick of the form direction shift after block-local unitary mixing, and a local, additive, phase-blind, continuous reading of the odds. Under these, the reading is c|a|^2. Exact two-mode step and Lie-closure step; finite numerics in a supplied 1D two-direction walk. The note does not derive linearity or unitarity of the tick, the locality of the reading, phase blindness, or an identification of block-direction odds with the axioms' per-site distribution."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/relay_conservation_selects_the_squared_magnitude_reading_of_the_odds_2026_10_21.py
---

# Relay conservation selects the squared-magnitude reading of the odds

Claim type: bounded_theorem.
Primary runner: `scripts/relay_conservation_selects_the_squared_magnitude_reading_of_the_odds_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight; the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the hypotheses below.

## Hypotheses (all supplied)

- **H1. Tick form.** Each tick, the amplitudes a(b, d) of a block b are mixed by a block-local unitary C, and each then moves one block along d. Unitarity is CL-1 as the candidate laws read it. The tick update itself remains an open dependency.
- **H2. Local additive reading.** The odds of (b, d) are f(a(b, d)), with one continuous f : C -> [0, inf) for all blocks and directions, and f(0) = 0. Using one f everywhere follows from "a law privileges no site". That the odds of a component depend on that component's amplitude alone is assumed.
- **H3. Phase blindness.** f(e^{i alpha} z) = f(z).
- **H4. Mixing.** C is not monomial: it does not just relabel directions and attach phases. A coin that never mixes directions never turns a relay, so a massive species needs H4.

## What CL-4 and CL-6 add

By CL-4 every relay moves one block per tick and none is created or lost. CL-6 switches relays between directions inside a block only. So the number of relays in a block is unchanged by the mixing step. If relays are to stay distributed as the odds, the block's total odds must be unchanged by C, for every block state phi:

    sum_d f((C phi)_d) = sum_d f(phi_d).          (B)

Global normalisation only probes block states of total odds at most 1. The argument below runs unchanged on that range.

## Theorem

Under H1 to H4 and (B), f(z) = c |z|^2 with c > 0 on every amplitude a state can reach. Normalisation fixes c, so the odds are |a|^2 / sum |a|^2.

**Step 1 (invariance group).** The unitaries that satisfy (B) on the compact set {W <= 1} form a closed semigroup of U(n). A closed subsemigroup of a compact group is a group, call it K. By H3 every diagonal phase matrix lies in K, so K contains the diagonal torus T. It also contains C T C^dagger. That is a different torus, because C T C^dagger = T exactly when C is monomial, which H4 excludes. The Lie algebra k of K therefore contains the diagonal algebra t and a non-diagonal element. Under the adjoint action of T, u(n) is t plus irreducible two-dimensional root planes r_jk, one for each pair j < k, with distinct weights. A t-invariant subspace containing t is therefore t plus some of the r_jk, here at least one. Exponentiating r_jk gives every two-mode rotation of modes j and k, in particular the balanced one.

**Step 2 (Jensen).** Feed the balanced rotation of modes j and k with |x|^2 = |y|^2 = s and relative phase theta. The two outputs have |.|^2 = s(1 + cos theta) and s(1 - cos theta). Write G(u) = f(sqrt u), which is well defined by H3. Then (B) gives

    G(S) + G(2s - S) = 2 G(s)   for every S in [0, 2s].

Here the relative phase sweeps S over the whole interval, so this step uses complex amplitudes. A continuous solution of Jensen's equation is affine, and G(0) = 0, so G(u) = c u. Positivity gives c > 0.

The argument needs only two modes. It does not use Gleason's theorem, which needs dimension 3 because it constrains measures on all bases without any dynamics. On a qubit, (1 + u_z^3)/2 is a non-Born frame function on every basis (control in the runner). Here the basis is fixed by H2 and the constraint comes from the tick, which is why dimension 2 suffices.

**Corollary (normalised nonlocal readings).** Consider the reading odds = |a|^p / sum |a|^p, which is normalised automatically. It still violates (B) for p != 2: pair any block with a block in an eigenvector of C, whose weight is unchanged, and the ratio of their block weights must be kept fixed.

## Numerics (supplied model)

The supplied 1D walk has two directions per block, coin cos m - i sin m sigma_x with m = 0.3, L = 32 blocks, a random state and 60 ticks. The runner reports the largest per-tick fraction of relays that would have to change block to keep CL-6:

| p | additive | normalised |
|---|---|---|
| 1 | 3.3e-2 | 3.3e-2 |
| 1.5 | 2.1e-2 | 2.0e-2 |
| 2 | 1.6e-16 | 1.6e-16 |
| 2.5 | 2.8e-2 | 2.4e-2 |
| 3 | 6.1e-2 | 5.1e-2 |
| 4 | 1.3e-1 | 1.1e-1 |

Take the block-of-eight mass mixing, with t1 = 0.05 and t2 = 0.5. Its closure with the diagonal phases has dimension 32 and contains the root planes of 12 mode pairs, so Step 1 applies to it.

**Control.** A real orthogonal coin conserves the phase-sensitive weight Re^2 + 3 Im^2. H3 or a complex coin is therefore needed. The complex mass coin breaks that weight (deviation 8.96).

## What is supplied, plainly

Linearity and unitarity of the tick (H1), the locality and additivity of the reading (H2), and phase blindness (H3). H3 is motivated by the fact that a common phase acts trivially on M_2(C) by conjugation, but it is not derived. The note also does not identify the block-direction odds with the per-site distribution of the Admissibility axiom. The open dependency is narrowed, from "read |a|^2 as probability" to "the odds are a local, phase-blind function of the amplitudes". It is not removed.
