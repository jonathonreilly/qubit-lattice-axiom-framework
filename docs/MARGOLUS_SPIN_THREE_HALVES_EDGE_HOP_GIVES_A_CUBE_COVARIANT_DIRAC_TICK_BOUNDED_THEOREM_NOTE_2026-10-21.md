---
claim_id: margolus_spin_three_halves_edge_hop_gives_a_cube_covariant_dirac_tick_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "In a supplied Margolus tick with one fermion mode per site and rotations acting on site modes as spin-3/2 coherent states along the body diagonals, the edge hop with overlap phases is unitary, exactly covariant under the 24 proper cubic rotations about every block centre, and has bands cos w = cos^2(mu/2)(cos Kx + cos Ky + cos Kz)/3 - sin^2(mu/2); no classification of all ticks, derivation from the axioms or physical identification is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/margolus_spin_three_halves_edge_hop_gives_a_cube_covariant_dirac_tick_2026_10_21.py
---

# A spin-3/2 edge hop gives a cube-covariant Dirac tick on one-mode sites

Claim type: bounded_theorem.
Primary runner: `scripts/margolus_spin_three_halves_edge_hop_gives_a_cube_covariant_dirac_tick_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its current block-of-eight tick candidate is exactly covariant under only 4 of the 24 rotations. This note gives a supplied tick on one-mode sites that is covariant under all 24. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the tick nor the rotation action.

## Setting

Sites of Z^3 carry one fermion mode each. The tick applies an 8x8 block unitary W on the even blocks {0,1}^3 + 2Z^3 and then on the odd blocks shifted by (1,1,1). Rotations act on site modes as corner permutations times phases, induced from a character of the corner stabiliser C3; the four cases are the spin-j coherent states along the body diagonals with j = 0, 1/2, 1, 3/2. Each action is monomial and unitary, and the 2 pi rotation acts as (-1)^(2j).

## The spin-3/2 edge hop

Hop along each of the 12 cube edges with amplitude 1/sqrt3 and phase equal to that of the overlap of the two sites' spin-3/2 states, W = Wx + Wy + Wz. Transport around every cube face is -1 for j = 3/2, against phases -pi/3 and -2 pi/3 for j = 1/2 and 1. Hence hops along different axes anticommute, {Wa, Wb} = (2/3) delta_ab to 2.3e-15, and W is Hermitian with W^2 = 1. W commutes with the 24 spin-3/2 corner actions, and on a 6^3 lattice the tick commutes with all 24 rotations about both even and odd block centres to 2.1e-15.

With mass, W(mu) = cos(mu/2) W + i sin(mu/2) 1, all 8 bands obey

  cos w = cos^2(mu/2) (cos Kx + cos Ky + cos Kz)/3 - sin^2(mu/2)

to 1.2e-15 over 2000 K and three values of mu, so the bands are +-w, each exactly fourfold. Near K = 0, |w| = sqrt(mu^2 + k^2/3) within 1.9e-3 at |k| = 0.4, with direction spread below 4.4e-3: two degenerate isotropic Dirac bands with speed 1/sqrt3 block per tick. The global gap is mu, reached at K = 0. The massless node has zero net Berry flux (-6.7e-16), so it is not net-chiral. The only other node is w = pi at K = pi(1,1,1), which mu does not gap.

## Comparison within the same runner

For multiplicity-free actions (j = 0, 1/2, 1) the linear K term vanishes inside every eigenspace of the K = 0 tick, to 4.6e-15. For j = 1/2 with E1/2 and G3/2 coupled, the massless cone has velocities +-sqrt(2/3), each twofold and isotropic to 1e-3, plus two zero-velocity states; with mass 0.1 the light bands follow sqrt(m^2 + (2/3)k^2) within 0.6% at |k| = 0.1. Along all four body-diagonal lines, however, a twofold level sits exactly at the G3/2 energy for random block unitaries, to 5.6e-16. The pure corner-inversion mover sends corner s to 1 - s, so each half-tick steps one block along a diagonal d in {+-1}^3.

## Scope

Supplied: the partition geometry, the j = 3/2 action, the orientation convention and mu. Reading squared amplitudes as probabilities, interactions, the meaning of the two degenerate copies, the relay-source result for this tick, and a classification of all covariant ticks are not established. No derivation from the axioms or physical identification is claimed.
