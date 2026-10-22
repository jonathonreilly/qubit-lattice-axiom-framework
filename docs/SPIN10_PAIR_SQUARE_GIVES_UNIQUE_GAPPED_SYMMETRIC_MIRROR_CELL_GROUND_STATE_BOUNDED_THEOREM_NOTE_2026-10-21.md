---
claim_id: spin10_pair_square_gives_unique_gapped_symmetric_mirror_cell_ground_state_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "On one cell carrying a supplied mirror 16 with two spin components (32 modes), the Spin(10) pair square H = g(Omega + Omega^dag) alone has a unique Spin(10)-singlet, spin-singlet, Z4-trivial ground state E0 = -2g sqrt(11088 + 48 sqrt 21081), a gap 19.0715 g and a fermion gap 33.5804 g, for every complex g != 0; the lattice phase at finite hopping, the masslessness of the light copy and chirality are not established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/spin10_pair_square_gives_unique_gapped_symmetric_mirror_cell_ground_state_2026_10_21.py
---

# The Spin(10) pair square alone gives a unique gapped symmetric ground state on one mirror cell

Claim type: bounded_theorem.
Primary runner: `scripts/spin10_pair_square_gives_unique_gapped_symmetric_mirror_cell_ground_state_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight and lists the existence of a gapped mirror phase as supplied. This note derives the single-cell part of that entry. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the mirror content nor the interaction used.

## Statement

On one cell carrying the mirror 16 with two spin components (32 fermion modes, 2^32 states), let B_a = sum M_a[A,B] c_{A up} c_{B down} with M_a = C gamma_a restricted to the 16, Omega = sum_a B_a B_a, and H = g(Omega + Omega^dag). For every complex g != 0, H has a unique ground state

E0 = -2g sqrt(11088 + 48 sqrt 21081) = -268.75463 g.

It is a Spin(10) singlet and a spin singlet, has N = 0 mod 4 and even fermion parity, and is gapped: the first excited level lies 19.0715 g above it and the first fermion-odd level 33.5804 g above it.

## Derivation

1. Algebra. M_a is symmetric and unitary and B_a is a Spin(10) vector and SU(2) singlet, with [B_a, B_a^dag] = 16 - N. Omega lowers N by 4, so the phase of g is removable and only Z4 of particle number survives. The number-conserving one-body stabiliser of Omega is so(10) + sl(2) (dimension 48), so there is no extra flavour symmetry and no U(1)_N. The B_a and their adjoints close on so(12), and H = g[J,[J,C_so(11)]] with J = (16 - N)/2: a difference of two so(11) Casimirs that do not commute, not a combination of Casimirs.
2. Decomposition. A particle-hole map on the spin-down modes turns the Fock space into the exterior algebra of the 32-dimensional spinor of so(12), with spin acting as quasi-spin. Under so(12) x SU(2) it splits into 63 irreducibles, each so(12) irrep occurring once and with one spin (exact integer character arithmetic). H therefore picks up no degeneracy from a repeated irrep. The empty and filled states lie in the irrep L* = (8,0,0,0,0,0) of dimension 63206. The so(12) singlets are the 17 fully spin-polarised states, at E = 0, so the ground state is not an so(12) singlet.
3. Localisation. On the Spin(10) block la of an irrep L, H/2g >= -(C_so(11)' - C_so(10)) >= -(max c11(mu) - c10(la)). This bound is at least -127 on every block except the Spin(10)-singlet block of L*, whose lowest value is -134.377.
4. Exact block. That block has 9 states (N = 0, 4, ..., 32) and is the Jacobi chain beta_k^2 = 16k(9-k)(k+4)(13-k). Its lowest eigenvalue is E0 above, a simple level. Steps 2 to 4 make the ground state unique.
5. Symmetry. In the ground state <N> = 16, <c^dag_a c_b> = d_ab/2, all pair and vector expectations vanish, and P(N = 0, 4, 8, 12, 16) = 0.0029, 0.0269, 0.1048, 0.2231, 0.2847, symmetric about N = 16.
6. Gap. The first excited level is a Spin(10) 10 with spin 0 (chain 16k(8-k)(k+5)(13-k)) at 19.0715 g; the first fermion-odd level is the 64 states of 16 + 16bar with spin 1/2 (chain 16k(8-k)(k+4)(13-k)) at 33.5804 g; the 54 follows at 42.330 g. Casimirs alone already bound the gap below by 14.75 g and the fermion gap by 25.75 g. The spectrum is symmetric under E -> -E.

## Checks

The runner ends with `TOTAL: PASS=14 FAIL=0`. Among its lines:

- `[PASS] A1 [T] M_a symmetric and unitary ... Omega lowers N by 4, so its phase is removable and only Z4 of N survives`.
- `[PASS] A2 [T] the one-body (number-conserving) stabiliser of Omega in gl(32) has dimension 48 = so(10) + sl(2)`.
- `[PASS] B1 [T] under so(12) x SU(2)_spin the 2^32 Fock space is a sum of 63 irreducibles, each so(12) irrep occurring once and with one spin`.
- `[PASS] B2 [T] |0> and |F> lie in L* = (8,0,0,0,0,0) (dim 63206, spin 0, once); the so(12) singlets are the 17 fully spin-polarised states`.
- `[PASS] C1 [T] Gelfand-Tsetlin coefficients: o_3..o_8 ... satisfy the consecutive-generator relations`: the Gelfand-Tsetlin formulas are cited and checked here.
- `[PASS] D0 [T] Casimir localisation ... over every block except the Spin(10) singlet of L* this bound is >= -127`.
- `[PASS] D1 [T] ground state unique ... E0 = -2g sqrt(11088 + 48 sqrt 21081)`.
- `[PASS] D2 [T] gap Delta = 19.0715 g to the Spin(10) 10 ... fermion gap 33.5804 g (64 states: 16 + 16bar, spin 1/2 ...)`.
- `[PASS] D3 [T] the so(12) chains are the Fock chains ... Fock 7680, 113541120, 6720, 85155840`: this fixes the normalisation of g.
- `[PASS] D4 [T] symmetric: Spin(10) singlet, spin singlet, N in {0,4,...,32} so Z4 = +1 and fermion parity even`.
- `[PASS] D5 [T] main-branch atom: its singlet ... overlap <= 2 P(N=0) = 5.7e-03 with this ground state; both carry trivial Spin(10) x SU(2) x Z4 charges`.

The non-singlet blocks are diagonalised in floating point, in blocks of at most 24 states, with margins far above rounding error.

The earlier Spin(10) symmetric atomic-gap construction on main reached an exact gap only by adding a 32-body cat projector, a Casimir term and number projections. The four-body pair square alone is enough, so that requirement is narrowed. Its singlet overlaps this ground state by at most 5.7e-3 but carries the same trivial charges, so the two lie in one 0D class by the cited classification by charges. Its Casimir term leaves E0 unchanged and raises the 10 by 9 lambda.

## Estimates

These lines are labelled [E] in the runner and are not part of the theorem.

- `[PASS] E1 [T/E]`: c^dag|GS> lies 99.98% in the lowest fermion level, so the site Green function is z/(z^2 - Delta_f^2) to within 2e-4, with a zero at z = 0.
- `[PASS] E2 [E]`: on the cubic lattice with hopping t on all 32 modes, the gapped symmetric phase persists below some t_* > 0 by cited stability theorems. The second-order bond energy 0.2382 t^2/g with z kappa t_c^2 = Delta gives t_c ~ 3.65 g; a first-order fermion-band criterion gives 5.6 g. A real value needs a many-site computation.
- `[PASS] F1 [E/M]`: with the mirror term applied once per tick and the tick hop t = eps/(sqrt3 tau), the window eps/(3.65 sqrt3) < g tau < 0.0117 is open for eps < 0.074, which contains the register bound eps < 0.04. The mirror fermion mass Delta_f = 33.6 g then exceeds 4.6/a, about 1e19 GeV for a lattice spacing of a few Planck lengths, against LHC limits near 1.5 TeV. This comparison is an estimate.

## Boundary

Supplied: the mirror content (one 16 x 2 per cell), the use of the pair square alone (it is the unique Spin(10) x SU(2)-invariant quartic that changes N by 4, but quartic order and the omission of number-conserving quartics are choices), g, the hopping model, the tick hop and the lattice spacing. Cited, not rederived: gap stability under weak hopping, the 0D classification by charges, the anomaly reason U(1)_N must break to Z4, and the LHC limits. Not established: that the light copy stays massless, the lattice phase at finite hopping, the zone-corner term, and chirality.
