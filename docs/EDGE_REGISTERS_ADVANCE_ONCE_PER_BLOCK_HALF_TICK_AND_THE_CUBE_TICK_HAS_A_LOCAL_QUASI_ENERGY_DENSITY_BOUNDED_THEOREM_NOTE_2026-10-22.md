---
claim_id: edge_registers_advance_once_per_block_half_tick_and_the_cube_tick_has_a_local_quasi_energy_density_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's lapse rule N = sin(eps0) / (sqrt3 sqrt(mean_i gamma^ii)), reading the same edges in block-rung units (gamma^ij / b_e^2) gives the block lapse N_B = b_e N exactly, so one block half-tick has the proper time of b_e cube half-ticks (checked for b_e = 2..12 on 20 seeded metrics each, max relative error 3.3e-16). In supplied toys with eps0 = 0.1: a block half-tick made of b_e cube half-ticks controlled on held edge registers and then one edge unitary is unitary (b_e = 3, 4; error up to 2e-15), its cube layers commute with every register projector, and register odds change only at the edge update (3e-17 between, 0.02 at it); in a 2D toy with register lengths l_x = 0.5..2 matter's proper cone speed is direction-independent to 2.5e-6 and Omega(K) = sqrt(m^2 + c^2 K^2) holds to 1.6e-4, so matter reads the block metric diag(-N^2, l_x^2, l_y^2); 37 edge-controlled ticks give each register branch the rest phase T m N_n to 9e-16 (kickback), so an edge tick that also applies the matter phase counts it twice, and the filled band's kickback grows with volume (6.0e-2 on 8 cells against 2.8e-2 for one rest particle); the strict cone of matter, held registers and brickwork edge hops is finite (1.53 and 1.52 sites per cube half-tick at b_e = 4, 8). A per-cube quasi-energy density q_c (own term plus equal shares of the third-order nested commutators of the cubes it touches) sums to the third-order Floquet generator to 3e-17 and lives on a cube and its neighbours; on an interacting 10-site chain order n misses the exact generator by eps^(n+1) and changes by eps^(n+2) per tick (fitted exponents 2.00, 3.00, 4.02 and 2.99, 4.01, 4.99); over 600 ticks the total oscillates by 1.3e-5 with drift 7.9e-7 while single cubes move by up to 0.10; a local current carries the change (continuity); the exact 8-site log is quasi-local and the free tick's one-particle log is local (decay rate 2.6 per site); the mean quasi-energy current equals the momentum c^2 K to 2.8e-6 at Ka = 0.05; a parent-to-child split passes proper quasi-energy with mismatch scaling as (pa)^3.8 (7.8e-7 at pa = 0.05); midpoint subdivision of a flat tetrahedron keeps its volume exactly. An estimate with cell = Planck length, an injection bound of 1e-5 of the critical density and vertex amplitude at most eps0 finds the heating bound met for eps0 = 0.0075 and 0.02 and missed at 0.0375. Supplied model, finite diagnostic: the toy step, the 2D plaquette hops, register lengths and edge unitary, masses, chain sizes, the interaction stand-in V = 1, the equal-share partition, the cone calibration, the cell size, the injection bound and the vertex-amplitude assumption."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/edge_registers_advance_once_per_block_half_tick_and_the_cube_tick_has_a_local_quasi_energy_density_2026_10_22.py
---

# Edge registers advance once per block half-tick, and the cube tick has a local quasi-energy density

Claim type: bounded_theorem.
Primary runner: `scripts/edge_registers_advance_once_per_block_half_tick_and_the_cube_tick_has_a_local_quasi_energy_density_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law has block edge registers that advance once per block half-tick, while each cube's half-tick is the cube unitary controlled on its block's edge registers. Its response law reads a stationary total phase measured from the vacuum of the same edges. Two questions follow. First, what proper time does one block half-tick carry, and does matter on held registers see the block's metric without the edge tick re-applying the matter phase? Second, is there a per-cube quasi-energy whose mean can be set to zero cube by cube and kept so? This note answers both in supplied finite toys. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

The update law's lapse rule is N = sin(eps0) / (sqrt3 sqrt(mean_i gamma^ii)), with gamma^ij the inverse metric read by a cell. The toys use eps0 = 0.1, larger than the register's window 0.0075-0.0375, so that effects are visible.

A. Edge cadence.

1. Block lapse. Reading the same edges in block-rung units divides gamma^ij by b_e^2, so N_B = b_e N for every metric. One block half-tick therefore has the proper time of b_e cube half-ticks, the same fraction sin(eps0) of the block's light crossing.
2. Held registers. In a 2D toy on an 8 x 8 torus with five register values, take b_e cube half-ticks, each controlled on the held register, followed by one edge unitary (a supplied hop and phase on the register). The result is unitary. Every cube layer commutes with every register projector, so register odds are unchanged between edge updates and change only at them.
3. Block metric. In the same 2D toy (anticommuting plaquette hops, register lengths l_x = 2^((n-2)/2) for n = 0..4, so l_x = 0.5..2, l_y = 1, mass 0.3), matter's proper cone speed is the same along x, y and the diagonal, its proper rest energy is m, and Omega(K) = sqrt(m^2 + c^2 K^2). Matter's effective metric is diag(-N^2, l_x^2, l_y^2), the block's.
4. Kickback. On an 8-cell 1D chain with five register branches (l = 2^((n-2)/4), mass 0.4), T ticks of the edge-controlled cube tick give branch n the phase T m N_n relative to branch 0, the rest-phase part of the total phase. The controlled tick already applies the matter phase to the register, so an edge tick that also applies it counts it twice.
5. Vacuum share. The filled band's kickback differs across the register range by an amount per cell per tick, so on a chain it grows with volume and exceeds one rest particle's. The vacuum share therefore needs a counter-phase on the edges. This is a finite diagnostic.
6. Causality. The strict reachability cone of matter, held registers and brickwork edge hops advances a finite number of sites per cube half-tick, the same at b_e = 4 and 8. The dressed matter cone lies inside it.

B. Per-cube quasi-energy.

7. Local density (the runner's definition). For the two-layer tick U = exp(-i A_odd) exp(-i A_even), q_c is cube c's own term plus equal shares of the second- and third-order nested commutators among the cubes it touches. Then sum_c q_c is the third-order Floquet generator H^(3), and q_c lives on its cube and its neighbours, since non-touching cube terms commute.
8. Truncation scaling. On an interacting chain the order-n generator H^(n) misses the exact i log U by eps^(n+1) and changes by eps^(n+2) per tick.
9. Total kept, cubes move. Over many ticks of a local packet the total sum_c <q_c> oscillates without drift, while single cubes change by much more.
10. Continuity. The change in the summed density up to a cut, J = sum_(c <= cut) (U' q_c U - q_c), acts at the cut and not at the chain ends. So d<q_c>/tick is minus the face currents, and zero mean in every cube is kept iff the mean face currents vanish.
11. Quasi-locality. The exact i log U on an 8-site chain (full Fock space, dimension 256) has Pauli weight falling with span, faster at the smaller step. The free tick's one-particle log is exactly conserved (no heating) and exponentially local while the bands stay below pi (band maximum 2 eps0 < pi, stated).
12. Current is momentum. On the 1D walk with the step calibrated to the cone, the mean quasi-energy current E v_g equals c^2 K, the momentum, as Ka -> 0. Face currents are the momentum density, so the momentum constraint on the mean keeps zero mean per cube.
13. Split passing. A quantum passed from a parent rung to a child rung (lapse halved, both cone-calibrated) at fixed momentum keeps its proper quasi-energy up to a mismatch of order (pa)^4. Zero mean maps to zero mean only up to that order per passed quantum.
14. Volume additivity. A flat tetrahedron cut at its edge midpoints into 4 corner tetrahedra and 4 from the inner octahedron keeps its volume exactly. The runner states, and does not compute, that new hinges inside a flat parent or on a shared face have zero deficit and split hinges keep theirs, so that the Regge and Lambda terms map exactly.

C. Heating time (estimate).

15. The free tick never heats (item 11). Interacting wrap processes need ceil(pi / (2 eps0)) pairs. With vertex amplitude at most eps0, the bound that one cube's injected energy over the age stays below 1e-5 of the critical density is met for eps0 = 0.0075 and 0.02 and missed at 0.0375.

## Derivation

Item 1 is a scaling identity: gamma^ij -> gamma^ij / b_e^2 multiplies sqrt(mean gamma^ii) by 1/b_e. The runner checks it on 20 seeded random positive metrics for each b_e. Item 2 builds the block half-tick as a register-diagonal sum of cube ticks followed by a register unitary, and compares register populations before and after. Item 3 reads the dispersion from the eigenphases of the 2D Bloch tick. Item 4 evolves a k = 0, sublattice-symmetric state, an eigenvector of every branch, under the controlled tick and reads the relative branch phases. Item 5 integrates the lower band's quasi-energy over 400 momenta at the two register extremes. Item 6 propagates a reachability set through the combined circuit. Items 7-10 build the Floquet tick of a 10-site staggered-fermion chain with nearest-neighbour interaction in the 5-particle sector, its BCH truncations, and the density q_c. Item 11 takes a Schur-form log of the 8-site tick and decomposes it in Pauli strings. Items 12-13 differentiate the 1D walk's eigenphase. Item 14 subdivides a seeded random tetrahedron. Item 15 evaluates closed-form counts.

## Finite checks

Identity checks (the runner asserts each):
- Block lapse: N_B / (b_e N) - 1 at most 3.3e-16 over b_e = 2..12.
- Block half-tick, b_e = 3 and 4: unitarity error 4e-16 and 2e-15; commutator with register projectors 0; register odds change at most 3e-17 between edge updates and 0.02 at them.
- 2D block metric: cone-speed spread 2.5e-6 (asserted below 2e-3), rest-energy spread 1.0e-14, relative dispersion error 1.6e-4 at K up to 0.04 (asserted below 5e-3).
- Kickback after T = 37 ticks: branch phase error 9e-16.
- Density: |sum_c q_c - H^(3)| = 3e-17; non-touching commutators 0.
- Free one-particle log: |h(x, x+r)| ~ exp(-2.6 r) on 60 sites (asserted rate above 1).
- Tetrahedron volume: relative error 0.

Finite diagnostics (supplied model, finite diagnostic):
- Filled-band kickback difference across the register range: 7.5e-3 per cell per tick, 6.0e-2 on the 8-cell chain, against 2.8e-2 for one rest particle.
- Strict cone: 1.53 (b_e = 4) and 1.52 (b_e = 8) sites per cube half-tick; dressed cone about 0.100 at eps 0.1.
- Truncation exponents from eps = 0.05 and 0.1 (L = 10, N = 5, V = 1): |H_F - H^(n)| ~ eps^{2.00, 3.00, 4.02} and |U' H^(n) U - H^(n)| ~ eps^{2.99, 4.01, 4.99} for n = 1, 2, 3. The runner's "without accumulating" is a reading of the per-tick scaling, not a long-time measurement.
- 600 ticks: total oscillation 1.3e-5, drift 7.9e-7, largest single-cube change 0.10.
- Continuity: current commutator with the occupations 0.01 at the cut and 5.2e-6 at the chain ends.
- Exact 8-site log, Pauli weight at span 3..6 relative to span 2:

| eps | span 3 | span 4 | span 5 | span 6 |
|---|---|---|---|---|
| 0.1 | 3e-03 | 4e-06 | 1e-08 | 2e-11 |
| 0.25 | 2e-02 | 1e-04 | 2e-06 | 2e-08 |

- Diagonal-ensemble absorbed fraction of H^(2) (L = 10, N = 5) at eps 0.1 / 0.3 / 0.6 / 1.2: interacting (V = 1) 4.1e-06 / 4.7e-04 / 1.3e-02 / 7.6e-01; free 6.9e-07 / 7.0e-05 / 1.9e-03 / 7.8e-02. Small at small step; a finite chain cannot show the exponent.
- Current = momentum: uncalibrated c^2 is off by 6.2e-02 = (mu / 2 eps)^2; calibrated, E v_g / (c^2 K) - 1 is 2.8e-06 at Ka = 0.05 and 6.2e-03 at 0.2.
- Split mismatch: 7.8e-07, 5.9e-06 and 1.5e-04 at pa = 0.05, 0.1 and 0.2 (fitted slope 3.79).

The random metrics, the register state of item 2 and the tetrahedron use a fixed seed (7).

## Estimates against measurement

Planck units, with the cell length supplied as 1 l_P, the age 8.08e60, H0 = 1.18e-61 and an injection bound of 1e-5 of the critical density:

| eps0 | ticks in the age | needed ln(1/Gamma) | one cube outliving the age | wrap pairs | vertex amplitude <= eps0 gives | needed kappa in exp(-kappa/eps0) |
|---|---|---|---|---|---|---|
| 0.0075 | 1.9e+63 | 453 | 146 | 210 | 2055 | 3.4 |
| 0.02 | 7.0e+62 | 450 | 145 | 79 | 618 | 9.0 |
| 0.0375 | 3.7e+62 | 448 | 144 | 42 | 276 | 16.8 |

The bound holds at 0.0075 and 0.02 and fails at 0.0375. The runner's crossover "below about 0.026" is stated, not computed. The vertex-amplitude bound is an assumption, not derived.

## Boundary

Not claimed: any 3D register-level computation (the block metric of item 3 is a 2D toy with supplied plaquette hops); the edge unitary itself, which is supplied; the counter-phase on the edges that the vacuum share needs (item 5 shows it is needed, not what it is); that the equal-share partition of item 7 is the unique local density; convergence of the Floquet expansion or absence of heating in the interacting thermodynamic limit (items 8 and 11 are finite chains); the hinge-deficit statement of item 14 (stated); the heating crossover value and the vertex-amplitude bound (stated); any experimental exclusion.

## Supplied vs forced

Supplied: the toy step eps0 = 0.1 and the other step values; the 2D anticommuting plaquette hops; the register values, lengths and edge unitary (hop 0.3, phase 0.05 n); the masses 0.3, 0.4 and 0.5; the chain and torus sizes; the interaction stand-in V = 1 and mu = 0.3 eps; the packet's kick; the equal-share density partition; the cone-calibration form of the step; the cell size, the age, H0, the injection bound and the vertex-amplitude assumption. Forced, given those: N_B = b_e N; unitarity of the block half-tick and register odds that change only at edge updates; the block metric seen by matter in the toy; the kickback of the rest phase through the controlled tick, hence double counting if the edge tick re-applies it; the sum rule and locality of q_c; the eps^(n+1) and eps^(n+2) truncation scaling; continuity with a local current; current equal to momentum as Ka -> 0; exact volume additivity under subdivision.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's cube tick, lapse rule and block edge registers advancing once per block half-tick, and the response law's total phase measured from the vacuum of the same edges, with its Regge and Lambda terms. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/edge_registers_advance_once_per_block_half_tick_and_the_cube_tick_has_a_local_quasi_energy_density_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 3 s with about 190 MB resident, prints about 5.3 kB and ends with `TOTAL: PASS=18 FAIL=0`. Its random draws use a fixed seed; two runs gave identical output apart from the elapsed-time line.
