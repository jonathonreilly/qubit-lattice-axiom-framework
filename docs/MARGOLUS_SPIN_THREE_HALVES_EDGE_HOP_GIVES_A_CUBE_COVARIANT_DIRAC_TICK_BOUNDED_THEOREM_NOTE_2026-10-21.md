---
claim_id: margolus_spin_three_halves_edge_hop_gives_a_cube_covariant_dirac_tick_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "In a supplied Margolus tick with one fermion mode per site and rotations acting on site modes as spin-3/2 coherent states along the body diagonals, the edge hop with overlap phases is unitary, exactly covariant under the 24 proper cubic rotations about every block centre, and has bands cos w = cos^2(mu/2)(cos Kx + cos Ky + cos Kz)/3 - sin^2(mu/2); no classification of all ticks, derivation from the axioms or physical identification is established."
upstream_dependencies:
  - minimal_axioms
runner: scripts/margolus_spin_three_halves_edge_hop_gives_a_cube_covariant_dirac_tick_2026_10_21.py
---

# A spin-3/2 edge hop gives a cube-covariant Dirac tick on one-mode sites

Claim type: bounded_theorem.
Primary runner: `scripts/margolus_spin_three_halves_edge_hop_gives_a_cube_covariant_dirac_tick_2026_10_21.py`.

This note studies a supplied two-partition unitary on one fermion mode per site. Its spin-3/2 rotation action and hop are model choices. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not select them; no physical identification is established.

## Setting

Sites of Z^3 carry one fermion mode each. The tick applies an 8x8 block unitary W on the even blocks {0,1}^3 + 2Z^3 and then on the odd blocks shifted by (1,1,1). Rotations act on site modes as corner permutations times phases, induced from a character of the corner stabiliser C3; the action used here is induced by spin-3/2 coherent states along the body diagonals. It is monomial and unitary, with the 2 pi rotation acting as -1.

## The spin-3/2 edge hop

Hop along each of the 12 cube edges with amplitude 1/sqrt3 and phase equal to that of the overlap of the two sites' spin-3/2 states, W = Wx + Wy + Wz. Transport around every cube face is -1 for j = 3/2. Hence hops along different axes anticommute, {Wa, Wb} = (2/3) delta_ab to 2.3e-15, and W is Hermitian with W^2 = 1. W commutes with the 24 spin-3/2 corner actions, and on a 6^3 lattice the tick commutes with all 24 rotations about both even and odd block centres to 2.1e-15.

With mass, W(mu) = cos(mu/2) W + i sin(mu/2) 1, all 8 bands obey

  cos w = cos^2(mu/2) (cos Kx + cos Ky + cos Kz)/3 - sin^2(mu/2)

to 1.3e-15 over 2000 K and three values of mu, away from w = 0 or pi, the two branches +-w are fourfold; coincident branches have the combined multiplicity. For the sampled mu = 0 and 0.1 and 200 directions, |w| agrees with sqrt(mu^2 + k^2/3) within 0.2% at |k| = 0.4, with direction spread below 0.5%. The massless limiting speed is 1/sqrt3 block per tick. For 0 <= mu <= pi, the principal quasienergy gap is mu, reached at K = 0. The finite-mesh Berry-flux diagnostic around the massless node agrees with zero; this is not a classification of chiral matter. For 0 <= mu < pi, the band formula puts quasienergy pi at K = pi(1,1,1); at mu = pi all branches coincide there in quasienergy throughout the zone.

## Algebra behind the band identity

The normalized axis hops square to I/3 and pairwise anticommute. The cube-face pi flux makes their connection gauge-equivalent to the Clifford representative Gamma_1 = X tensor I tensor I, Gamma_2 = Z tensor X tensor I, Gamma_3 = Z tensor Z tensor X. Write A = W and B = D(K)^dag W D(K). Then A^2 = B^2 = I and {A,B} = 2 S(K) I, where S(K) = (cos Kx + cos Ky + cos Kz)/3. With c = cos(mu/2), s = sin(mu/2), the tick is U = (c B + i s I)(c A + i s I). Adding U^dag cancels the linear imaginary term and gives (U + U^dag)/2 = (c^2 S(K) - s^2) I. The trace is real, so away from coincident branches their multiplicities are equal. This proves the displayed band identity for the supplied construction; the runner separately checks its coherent-state implementation.

The earlier comparison with other rotation actions is deferred. In particular, a universal vanishing-linear-term claim fails at coincident eigenspaces: with the untwisted corner inversion P on both half ticks, U(0) = I but R - P R P = 2R is nonzero. No such selection theorem is claimed here.

## Scope

Supplied: the partition geometry, the j = 3/2 action, the orientation convention and mu. Reading squared amplitudes as probabilities, interactions, the meaning of the two degenerate copies, the relay-source result for this tick, and a classification of all covariant ticks are not established. No derivation from the axioms or physical identification is claimed.
