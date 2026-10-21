---
claim_id: scale_ladder_gravity_front_clocks_spin_half_walk_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Finite plane-wave and packet comparisons of supplied front tick rates on a supplied spin-1/2 split-step walk in 3D against m^2/eps; no physical clock law, gravitational redshift, derivation of the flip rule or empirical identification."
upstream_dependencies:
  - minimal_axioms
runner: scripts/scale_ladder_gravity_front_clocks_spin_half_walk_2026_10_21.py
---

# Front clocks on a spin-1/2 walk in 3D

Claim type: bounded_theorem.
Primary runner: `scripts/scale_ladder_gravity_front_clocks_spin_half_walk_2026_10_21.py`.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the walk, coin or tick rules below. This note compares supplied tick rates with the rest frequency over gamma.

## Supplied walk and tick rates

The state has two chirality blocks of two components. Each tick a coin exp(-i th beta) mixes the blocks. Then shifts move each component one site along x, y and z according to the eigenvalue of alpha_i = diag(sigma_i, -sigma_i). For a positive-frequency eigenmode at momentum k with frequency eps, rest frequency m and group velocity v, the comparison target is m^2/eps. For a relativistic dispersion this equals m/gamma.

Four per-tick rates are compared:

- **product:** 4 eps pL pR;
- **geometric:** 2 th sqrt(pL pR);
- **coherent:** th psibar psi / psi^dag psi, evaluated at mid-coin, i.e. th times twice the real chirality overlap;
- **phase:** eps - k.v.

Here pL and pR are the chirality occupations. The first two count chirality flips by occupation; the third sets flips by the coherence between chiralities.

## Plane waves

Off the axes the two positive bands split. The runner evaluates each band separately at fixed k/th while th halves from .05 to .0125. Along (1,1,0) with k = th, (1,1,1) with k = 2 th and (2,1,0) with k = 2 th, the coherent rate's relative error roughly halves with each halving of th. The two bands carry errors of opposite sign. The phase rate's error is smaller still and falls faster on two of the three rays. These are finite convergence observations, not an error bound.

On the axes the bands are degenerate, so the spin state inside the degenerate pair is a free choice. The product and geometric rates change with that choice, while the coherent rate does not, to rounding. An occupation-counted flip clock therefore depends on spin orientation in this walk; the coherent rate does not.

## Packets

On a 48^3 torus with th = .1 the runner builds packets from the two positive bands with a Gaussian of momentum width .1. It does this for a packet at rest, one moving along (1,1,0), and two crossing head-on. It sums th psibar psi over sites and divides by the norm. Each signed total is within 3 percent of the packet's spectral average of m^2/eps. The overlap is negative on part of the moving and crossing packets' weight. Summing its absolute value overshoots where the packets cross. A counting rule that ticks at the absolute overlap must therefore give its ticks the overlap's sign for the expected count to equal the signed total. The phase rate has no sign issue.

## Scope

The walk, coin angle, mid-coin evaluation, band selection and packet construction are supplied. No clock law, gravitational redshift, derivation of the coherent flip rule or physical identification is established.
