---
claim_id: a_sharp_dark_constant_freezes_the_odds_and_per_cube_operator_constraints_have_no_common_solution_so_the_hamiltonian_constraint_holds_on_the_mean_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "In a supplied finite toy of the update law's tick (one cube = one edge register with lengths 1 + n/2S and a ghost-sign edge hop, plus one two-level matter mode read with a conformal lapse; half-ticks alternate edge hop and matter phase), and a two-cube version with shared terms counted half in each cube: odds with a sharp dark constant (an eigen-phase of the tick) are frozen for every value of that constant, not only zero, and the tick conserves every state's distribution over dark constants; a state annihilated by the constraint K read from the total phase leaves the kernel of K under alternating half-ticks at a rate linear in the step; on a finite register K has a discrete spectrum, so the operator constraint has no solution unless a supplied constant is tuned; for two cubes the two per-cube constraint operators do not commute and have no common solution for any value of the constant in the scanned range, while their sum gets one with one tuning; Gauss's law, by contrast, commutes with the tick. A tuned Page-Wootters state with a real generator gives a conditional atom state with no time direction (the forward and backward branches superposed), while its forward branch tracks proper time. Under the actuality law's transport (computed by entropic optimal transport), a packet with a spread of dark constants moves its actual edge value with the mean and the half-tick record count, while a sharp state's actual edge value does not move. A supplied estimate puts a Planck-energy global spread far below the dark-radiation bound. Supplied model, finite diagnostic: one or two cubes, supplied kinetic and matter terms, no lattice cube tick, no momentum constraint, no splits; reading the constraint as a condition on the mean is the interpretation these checks support, not a computed statement."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_sharp_dark_constant_freezes_the_odds_and_per_cube_operator_constraints_have_no_common_solution_so_the_hamiltonian_constraint_holds_on_the_mean_2026_10_22.py
---

# A sharp dark constant freezes the odds, and per-cube operator constraints have no common solution, so the Hamiltonian constraint holds on the mean

Claim type: bounded_theorem.
Primary runner: `scripts/a_sharp_dark_constant_freezes_the_odds_and_per_cube_operator_constraints_have_no_common_solution_so_the_hamiltonian_constraint_holds_on_the_mean_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. With the lapse fixed by the update law (CL-1 in the three-law numbering), the response law (CL-3) has no lapse equation, and its integral survives as a dark constant per cube. In general relativity the Hamiltonian constraint is imposed on the state, H psi = 0, and the state then does not change: the problem of time. This note asks how the register's edges can obey a Hamiltonian constraint under a fixed tick, comparing an operator constraint on the odds with a constraint on the mean, in a finite toy. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

Toy: one cube = one edge register (n = 0..2S, length l = 1 + n/2S, ghost-sign edge hop w(V + V^dag)) plus one two-level matter mode with dust energy M and an atom splitting Omega read with the conformal lapse N = sigma l, minus a supplied constant E0. Half-tick A is the edge hop, half-tick B the matter phase on the edges. The dark constant c is the tick's quasi-energy, U_F = exp(-i K_F).

A. The constraint as an operator on the odds.

1. Odds with a sharp dark constant are frozen, for every value of c, not only c = 0; and the tick conserves the distribution over dark constants of every state. Restricting the odds to the c = 0 eigenspace is restricting them to the tick's fixed points.
2. A state with K psi = 0 for the constraint read from the total phase, K = K_kin + K_pot, leaves the kernel of K under the alternating half-ticks, at a rate linear in the step: the half-ticks keep i log U_F, not K.
3. On a finite register K has a discrete spectrum, so ker K = {0} for a generic supplied constant; a kernel needs E0 in a finite set.
4. Two cubes sharing one fermion and a hinge term (shared terms counted half in each cube): the per-cube constraint operators H1, H2 do not commute, and no odds obey both for any E0 in the scanned range; their sum H1 + H2 - 2 E0 gets a kernel with one tuning (one global condition).
5. Gauss's law on a link register between two sites commutes with the tick, has integer spectra and a sector on which the tick acts non-trivially: it is a symmetry, while the Hamiltonian constraint is the tick's own generator.

B. Relational time and the actual configuration.

6. On a finite register a non-degenerate sharp sector is one state; the atom is then in one stationary level, and nothing changes relative to anything.
7. With two supplied constants (E0, Omega) tuned so both atom levels meet c = 0, the conditional atom state at each edge value has <sigma_y> = 0 everywhere: the generator is real, so the forward and backward histories are superposed and there is no time direction. The forward branch alone (the analytic signal in n) has a relative phase that follows Omega times the proper time along the orbit, and its <sigma_y> swings fully.
8. Under the actuality law's transport (fewest changes, counting edge units, then greatest entropy), a packet with a spread of dark constants and mean near zero moves its actual edge value with the mean <n>_t, and the half-tick record count is a clock with something to time.
9. In the sharp state nearest that packet the actual edge value does not move over 300 ticks; with both half-ticks moving edges, the fewest-change transports act as monotone maps whose composition returns each edge value to itself.
10. The packet's spread dK is conserved with its whole distribution, and |<Phi|U^t Phi>| >= cos(dK t) (Mandelstam-Tamm); a history of T distinguishable ticks needs dK of order pi/(2T).

Reading. Items 1 to 4 and 6, 7, 9 say that an operator constraint on the odds either freezes the history or has no solution on finite registers; items 8 and 10 say a spread of dark constants is what lets the record count time anything. The register's reading, that the Hamiltonian constraint holds on the mean dark constant and not on the odds, is the interpretation these checks support; the runner does not compute it as a separate statement.

## Derivation

Item 1 diagonalises U_F by Schur decomposition (2S = 60, eps = 0.5) and evolves one eigenvector for 300 ticks and a random state for 137 ticks. Item 2 tunes the supplied constant so one eigenvector of K has K psi = 0 exactly and evolves it for 40 tick-units at three steps. Item 3 draws five random E0 in [1, 2]. Item 4 builds two cubes with 2S = 12 (338 states), scans E0 over [-4, 5] at 181 points, refines the minimum of the smallest singular value of [H1 - E0; H2 - E0], and reads the sum's kernel at half a level of H1 + H2. Item 5 builds one link register (spin 1) between two fermion sites. Items 6 and 7 use 2S = 200, solve for Omega by root finding, and fit the forward-branch phase. Items 8 and 9 compute the transport at each half-tick by entropic optimal transport (Sinkhorn, regularisation 0.05, 600 iterations) and sample 200 actual histories with a seeded generator. Item 10 checks the Mandelstam-Tamm bound tick by tick.

## Finite checks

Exact checks on the toy (the runner asserts each):
- Sharp dark constant: max |dP| over 300 ticks 5.2e-15; spectral weights of a random state conserved to 7.7e-15.
- Drift off ker K: max |K U^t psi| over 40 tick-units 5.12e-03, 2.56e-03, 1.28e-03 at eps = 0.2, 0.1, 0.05 (ratios 2.00, 2.00).
- Finite register (61 values): minimum level spacing 1.85e-04; distance from 0 to the spectrum of K for five random E0: 5.5e-03 to 4.7e-02.
- Two cubes (338 states): relative commutator ||[H1, H2]|| 0.23; minimum over the scanned E0 of sigma_min([H1 - E0; H2 - E0]) = 0.308 at E0 = -0.53; the sum has a kernel at E0 = 0.552.
- Gauss's law: [U, G_x] = 0 to print precision (asserted below 1e-12); sector (G1, G2) = (1, 0) of dimension 2, |U - phase| = 1.21 on it.
- Sharp sector, Omega = 0.2: atom weight 1.000 on one level, 1.1e-16 on the other.
- Tuned state (E0, Omega) = (1.5004, 0.20488): conditional <sigma_y> = 0 at every n (asserted below 1e-14); forward branch slope 0.9994 against Omega times proper time, maximum deviation 0.06 rad over 25 rad, <sigma_y> swinging to 1.00.
- Mandelstam-Tamm: the bound holds at every tick with dK t <= pi/2; overlap below 0.1 after 10 ticks.

Finite diagnostics (supplied model, finite diagnostic, no physical identification):
- Packet: mean dark constant +0.002, spread 0.204 per tick; actual edge value advances 29.6 units in 30 ticks, mean path within 0.42 of <n>_t, Sinkhorn marginal residual 7e-05, correlation of record count with actual n 1.000.
- Sharp state (overlap 0.06 with the packet): actual edge value changes in 0.000 of ticks, net drift +0.00 +- 0.00 units over 300 ticks, mean |corr(t, n)| 0.00.
- Both half-ticks moving edges: actual edge value changes between whole ticks in 0.000 of ticks.

## Estimates against measurement

With supplied inputs (Planck energy 1.22e19 GeV, a Hubble radius 1.37e28 cm, dark radiation allowed at about 4% of the radiation density with a neutrino factor 1.68): a global dark-constant spread of one Planck energy, enough to change the state every tick, against the dark-radiation room in a Hubble volume, 1.9e+74 GeV, gives a ratio of 6e-56: the spread is invisible while the mean is bounded by the dark-radiation measurement.

## Boundary

Supplied: the one-cube hop-form ghost kinetic term and the conformal-lapse dust and atom terms, the split of half-ticks into edges and matter (not the two tilings), the two-cube shared terms counted half, the link register for the Gauss's-law contrast, the tuned constants of item 7, the packet and its width, the transport by entropic optimal transport at regularisation 0.05 (the runner's closing summary line says 0.03; the code uses 0.05), edge units counted in the transport cost, and the measured inputs of the estimate. Forced, given those: frozen odds for every sharp dark constant and the conserved dark-constant distribution; the O(eps) drift off ker K; no operator solution on a finite register without tuning; no common solution of the two per-cube constraints in the scanned range; Gauss's law commuting with the tick; the absent time direction of the tuned real-generator state; packet and sharp-state behaviour of the actual edge value in the toy. Not claimed: any statement for the lattice cube tick; the momentum constraint as an operator; splits; a common-solution statement outside the scanned E0 range or for other two-cube couplings; that the mean-only constraint is derived rather than the reading these checks support; that the estimate is a prediction beyond its supplied inputs.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's tick and fixed lapse, the actuality law's transport and records, and the response law's total phase and dark constant. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/a_sharp_dark_constant_freezes_the_odds_and_per_cube_operator_constraints_have_no_common_solution_so_the_hamiltonian_constraint_holds_on_the_mean_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 12 s with about 130 MB resident, prints about 3.6 kB and ends with `TOTAL: PASS=12 FAIL=0`. Its random draws are seeded; two repeated runs gave identical output apart from the elapsed-time line.
