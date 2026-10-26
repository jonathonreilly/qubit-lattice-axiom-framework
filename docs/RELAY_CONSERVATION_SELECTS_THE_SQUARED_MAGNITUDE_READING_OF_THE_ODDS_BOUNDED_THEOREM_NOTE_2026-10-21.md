---
claim_id: relay_conservation_selects_the_squared_magnitude_reading_of_the_odds_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
conditional_surface_status: "Quadratic reading under the explicitly supplied full-space hypotheses"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Conditional finite-dimensional characterization; physical reading and dynamics remain supplied"
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_scope: "Conditional on full-space additive block-weight conservation, a tick of the form direction shift after block-local unitary mixing, and a local, additive, phase-blind, continuous reading of the odds. Under these, the reading is c|a|^2. Exact two-mode step and Lie-closure step; finite numerics in a supplied 1D two-direction walk. The note does not derive linearity or unitarity of the tick, the locality of the reading, phase blindness, or an identification of block-direction odds with the axioms' per-site distribution."
upstream_dependencies:
  - minimal_axioms
runner: scripts/relay_conservation_selects_the_squared_magnitude_reading_of_the_odds_2026_10_21.py
---

# Relay conservation selects the squared-magnitude reading of the odds

Claim type: bounded_theorem.
Primary runner: `scripts/relay_conservation_selects_the_squared_magnitude_reading_of_the_odds_2026_10_21.py`.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not supply the hypotheses below. This is a self-contained conditional finite-dimensional result, with a supplied walk as a numerical example.

## Hypotheses (all supplied)

- **H1. Tick form.** Each tick, the amplitudes a(b, d) of a block b are mixed by a block-local unitary C, and each then moves one block along d. The linear unitary tick is supplied; no candidate-law register is used as a premise.
- **H2. Local additive reading.** The odds of (b, d) are f(a(b, d)), with one continuous f : C -> [0, inf) for all blocks and directions, and f(0) = 0. Both use of one common f and dependence on the component amplitude alone are supplied assumptions.
- **H3. Phase blindness.** f(e^{i alpha} z) = f(z).
- **H4. Mixing.** C is not monomial: it does not just relabel directions and attach phases. This is an algebraic condition on the supplied coin, with no physical mass identification.

## Supplied block-weight conservation

For n >= 2 define W(phi) = sum_d f(phi_d). Assume, for every phi in C^n,

    W(C phi) = W(phi).                           (B)

This full-space identity is supplied. It is motivated by a model whose mixing
preserves block relay counts, together with an additional correspondence between
counts and the reading W. Neither that correspondence nor (B) is derived here
from the framework axioms. Conservation only on a normalized subset is not the
hypothesis of this theorem.

## Theorem

Under H1 to H4 and full-space (B), f(z) = c |z|^2 for every z in C, with c >= 0. If additionally f is not identically zero (in particular, some state has positive total weight), then c > 0. Normalizing any nonzero state gives odds |a|^2 / sum |a|^2; the identically zero reading cannot be normalized.

**Step 1 (invariance group).** Let K = {U in U(n): W(U phi) = W(phi) for every phi in C^n}. Continuity of W makes K closed. It is closed under composition; substituting phi = U^dagger psi proves inverse invariance. Thus K is a closed subgroup of the compact group U(n). By H3 every diagonal phase matrix lies in K, so K contains the diagonal torus T. It also contains C T C^dagger. That is a different torus, because C T C^dagger = T exactly when C is monomial, which H4 excludes. The Lie algebra k of K therefore contains the diagonal algebra t and a non-diagonal element. Under the adjoint action of T, u(n) is t plus irreducible two-dimensional root planes r_jk, one for each pair j < k, with distinct weights. A t-invariant subspace containing t is therefore t plus some of the r_jk, here at least one. Exponentiating r_jk gives every two-mode rotation of modes j and k, in particular the balanced one.

**Step 2 (Jensen).** Feed the balanced rotation of modes j and k with |x|^2 = |y|^2 = s and relative phase theta. The two outputs have |.|^2 = s(1 + cos theta) and s(1 - cos theta). Write G(u) = f(sqrt u), which is well defined by H3. Then (B) gives

    G(S) + G(2s - S) = 2 G(s)   for every S in [0, 2s].

Here the relative phase sweeps S over the whole interval, so this step uses complex amplitudes. A continuous solution of Jensen's equation is affine, and G(0) = 0, so G(u) = c u. Nonnegativity gives c >= 0; the separately supplied nonzero-reading condition gives c > 0.

The argument needs only two modes. It does not use Gleason's theorem, which needs dimension 3 because it constrains measures on all bases without any dynamics. On a qubit, (1 + u_z^3)/2 is a non-Born frame function on every basis (control in the runner). Here the basis is fixed by H2 and the constraint comes from the tick, which is why dimension 2 suffices.

## Numerics (supplied model)

The supplied 1D walk has two directions per block, coin cos m - i sin m sigma_x with m = 0.3, L = 32 blocks, a random state and 60 ticks. For the six sampled powers listed below, the runner reports the maximum half-L1 block-weight defect using a fixed initial normalization, and the maximum half-L1 distance between separately normalized block distributions. Only the latter has a minimum transported-fraction interpretation. When total weight drifts, the former is a defect diagnostic, not a conserved-relay transport fraction:

| p | fixed-normalization defect | normalized transport distance |
|---|---|---|
| 1 | 3.14e-2 | 3.09e-2 |
| 1.5 | 2.02e-2 | 2.01e-2 |
| 2 | 1.24e-16 | 1.51e-16 |
| 2.5 | 2.58e-2 | 2.54e-2 |
| 3 | 5.54e-2 | 5.33e-2 |
| 4 | 1.21e-1 | 1.13e-1 |

Take the block-of-eight mass mixing, with t1 = 0.05 and t2 = 0.5. Its closure with the diagonal phases has dimension 32 and contains the root planes of 12 mode pairs, so Step 1 applies to it.

**Control.** A real orthogonal coin conserves the phase-sensitive weight Re^2 + 3 Im^2. H3 or a complex coin is therefore needed. The complex mass coin breaks that weight (deviation 8.96).

## What is supplied, plainly

Linearity and unitarity of the tick (H1), the common local additive reading (H2), phase blindness (H3), non-monomial mixing (H4), and conservation on all C^n (B). Strict positivity additionally uses a nonzero reading. H3 is motivated by the fact that a common phase acts trivially on M_2(C) by conjugation, but it is not derived. The note also does not identify the block-direction odds with the per-site distribution of the Admissibility axiom. Conditional on the supplied unitary mixing and full-space block conservation (B), the reading question reduces to the supplied common local, phase-blind continuous function of amplitudes. These hypotheses and the physical identification remain supplied; this theorem does not derive them.

## Review record

The corrected statement assumes conservation on all of C^n. It withdraws the
unproved extension from normalized sublevel sets and includes the zero reading;
strict positivity requires a nonzero reading. The candidate-law attributions
are replaced by explicit supplied assumptions. The standalone universal power
exclusion is withdrawn; the numerical comparisons cover the listed samples.
The table is corrected to the reproduced outputs, and unnormalized weight
defect is distinguished from normalized transport distance. The runner now
checks the stated eight-mode dimension/root pairs and the transport factor.
