---
claim_id: the_margolus_tick_at_the_next_rung_keeps_its_speed_two_copies_and_zero_chirality_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied spin-3/2 Margolus tick read at rung 1 (4^3 cells of 64 one-mode sites, zoom x2 in space and time), the 64-band tick is exactly the fold of the 8 fine bands; the composite is not a two-partition Margolus circuit at rung 1 for any alignment; under the light-sector flow c is rung-invariant, the mass doubles and the cubic anisotropy falls by 4 per rung; under the stroboscopic zoom the pi-cone aliases onto the coarse zone centre; the rung-1 nodes carry zero Berry flux and every level stays fourfold, while the rung-0 cube cannot hold a single Dirac copy; a supplied covariant rung-1 block unitary with exactly one Dirac copy exists. Finite diagnostics of supplied models. The zoom convention, light projection and the rung-1 unitary are supplied; no rung-1 law, chirality, single-copy matter content or internal gauge group is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_margolus_tick_at_the_next_rung_keeps_its_speed_two_copies_and_zero_chirality_2026_10_21.py
---

# The Margolus tick at the next rung keeps its speed, its two copies and zero chirality

Claim type: bounded_theorem.
Primary runner: `scripts/the_margolus_tick_at_the_next_rung_keeps_its_speed_two_copies_and_zero_chirality_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its supplied spin-3/2 Margolus tick is read here at rung 1: 4^3 cells of 64 one-mode sites. The zoom convention is supplied: one rung-1 tick is two fine ticks, and space is coarsened by a factor of 2, which keeps the causal cone at one block per tick. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the tick nor the zoom.

The result is mostly negative. Read at rung 1, the tick is not a Margolus circuit, so it is not a fixed point of zooming. The light speed, the two copies and the zero chirality carry over unchanged to every rung. The one new feature is that rung 1 is the first rung whose cell can hold a single Dirac copy, and a supplied rung-1 unitary with exactly one copy is shown to exist.

## Statement

1. Folding. The 64-band rung-1 tick is the direct sum of the 8 fine bands at K = (Q + 2 pi n)/2. At Q = 0 the bands split into the momentum stars Gamma, R, X (x3) and M (x3), with dimensions 8, 8, 24 and 24. As rotation content the cell is 4 E_(1/2) + 4 E_(5/2) + 12 G_(3/2). Gamma and R are each 2 G_(3/2), while X and M are each 2 E_(1/2) + 2 E_(5/2) + 4 G_(3/2). The rung-0 cube is 2 G_(3/2) only.
2. Not a Margolus circuit. Neither one nor two fine ticks factor as a layer on even 4^3 blocks followed by a layer on odd blocks offset by (2,2,2), for any alignment.
3. Light-sector flow. Project onto the light states, then compose two ticks:
   - c^2 = A mu / (3 sin mu) is the same at every rung;
   - the mass in tick units doubles;
   - the cubic anisotropy w^2(q x) - w^2(q n_111) = -c^2 q^4 / (18 x 4^n) falls by 4 per rung, so isotropy emerges.

   A member (2 mu, b') of the same tick family with the same c exists exactly when 2b >= mu, with cos 2b' = cos 2b cos mu + sin^2 mu. At rung n this needs 3c^2 <= (mu_n/2) cot(mu_n/2). The condition fails at the first rung for b = 0. For the register's value of b it holds up to mu_n = 3.0617.
4. Pi-cone under the exact zoom. Read stroboscopically, the fine R states land on the coarse zone centre at |w| = |2(pi - 2b)| mod 2 pi. They form a Dirac pair of mass 4b per rung-1 tick, with c_D^2 = (A/3)(2b/sin 2b), which equals the light c^2 only if 2b = mu. Under repeated stroboscopic zoom every band eventually aliases onto quasi-energy 0; for the register's b this happens at rung 4. Light content is therefore preserved only by projecting first and then composing.
5. Chirality. The rung-1 light node and the aliased doubler node carry zero Berry flux. At any rung U(Q) = Phi(Q)^dag W_o Phi(Q) W_e, with Phi(Q) a diagonal matrix of Bloch phases. Since U(N) is connected, the block unitaries deform to the identity and the 3-winding vanishes.
6. Copies. Every rung-1 level stays fourfold at generic Q, so the two light copies persist at every rung. The rung-0 cube contains no E_(1/2) or E_(5/2), so no covariant rung-0 tick has a two-dimensional rest level, which a single Dirac copy would need.
7. Supplied single-copy unitary. W1 = P_a - P_b + i exp(0.3 i h_rest) on the remaining 60 states. Here P_a and P_b project onto two E_(1/2) copies, and h is the in-cell edge hop with the spin-3/2 overlap phases (pi flux per face). W1 is unitary and covariant, with exactly 4 light states at Q = 0 carrying E_(1/2) + E_(1/2), and one isotropic Dirac cone of speed c1 = 0.5745 rung-1 blocks per tick. It has no other light states, a mass term and zero Berry flux.

## Derivation

Item 1 is Bloch folding: a 2x2x2 coarsening maps each coarse momentum Q to eight fine momenta, and the rotation content follows from the characters of the 24 spin-3/2 rotations on the 64-site cell. Item 3 expands the light band of two composed ticks to fourth order in q: the q^2 coefficient is unchanged in rung units, and the quartic anisotropy carries the factor 1/4 from the zoom. Item 5 is a homotopy argument: W3 of a product of block unitaries conjugated by Bloch phases equals W3 at any point of a path in U(N) to the identity, and W3 of the identity is 0. Item 6 follows from Schur's lemma on the rotation content in item 1.

## Checks

The runner prints 26 PASS lines, and its output ends `TOTAL: PASS=26 FAIL=0`.

- Section 1:
  - the fold matches to 2.6e-15;
  - the printed Q = 0 levels are 0.13, 1.206086, 1.852721 and 2.721593 for Gamma, X, M and R;
  - the 1+1+3+3 split;
  - the rotation content;
  - the fine tick commutes with the rotations about the rung-1 cell centre.
- Section 2: at best 16 of 64 dimensions factor for one fine tick, and 0 of 64 for two.
- Section 3:
  - c^2 = 0.303896 at both rungs for (mu, b) = (0.1, 0.3), and 0.020203 at both rungs for (0.05, 1.321);
  - the anisotropy ratios 1.0000, 0.2500, 0.0625 and 0.0156;
  - the condition for the family member;
  - the rung-n matching bound.
- Section 4:
  - 8 states at |w| = 0.2000 and 1.0000 for two settings;
  - doubler c_D^2 = 0.32560 against light c^2 = 0.32998;
  - at rung 4, states with |K| >= 0.5 alias to quasi-energy 0 (minimum 1.5e-5, against 0.087 at rung 0).
- Section 5: Berry fluxes -1.1e-16 and -1.0e-15. The vanishing of the 3-winding at every rung is the argument above; the runner checks the flux only at rung 1.
- Section 6: fourfold levels to 3.6e-15, and no E_(1/2) or E_(5/2) in the rung-0 cube.
- Section 7, an existence check for the supplied W1:
  - unitarity and covariance;
  - 4 states at w = 0, with the other 60 at |w| >= 1.460;
  - the cone speed 0.5745;
  - no other light states (minimum 0.1714 over |Q| >= 0.3, against the cone's 0.1713 at |Q| = 0.3);
  - the fifth level is at least 1 rad over the zone, and the in-cell hop reduces the mean number of states within 0.2 of pi from 56.1 to 1.0;
  - the massive dispersion (0.100736 at |Q| = 0.02);
  - zero Berry flux (+1.4e-16);
  - covariance about both partitions' block centres on an 8^3 lattice (1.3e-15).

## What is supplied and the boundary

Supplied:
- the zoom convention and the light-state projection;
- the alignment of the rung-1 cells;
- the dense 64-mode block W1, which is not of the register's "edge neighbours equally" form, together with its speed-maximising pair (e_max +- e_min)/sqrt 2, its free relative phase, the rest phase i, the value 0.3 and the x mod 4 labels.

Not established:
- a rung-1 law;
- net chirality at any rung for these free Margolus ticks;
- single-copy matter content beyond the existence of W1;
- any internal gauge group.

The 3s in the 1+1+3+3 split are momentum stars that rotate with space, so reading them as colour or as generations would be unwarranted. Because c is the same at every rung, a per-species b would have to be shared by all species; supernova timing ties neutrino and light speeds to about 2e-9, an estimate.
