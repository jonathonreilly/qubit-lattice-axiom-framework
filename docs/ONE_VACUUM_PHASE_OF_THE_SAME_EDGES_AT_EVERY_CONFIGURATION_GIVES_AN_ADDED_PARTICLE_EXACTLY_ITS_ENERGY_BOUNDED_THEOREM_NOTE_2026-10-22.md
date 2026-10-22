---
claim_id: one_vacuum_phase_of_the_same_edges_at_every_configuration_gives_an_added_particle_exactly_its_energy_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For a vacuum eigenstate on fixed edges, the configuration-resolved phase-advance rate Re[(H psi)(c) / psi(c)] summed over sites equals E_vac(e) at every configuration on the vacuum's support (Born spread 1.3e-14 on a 12-site, 6-particle staggered chain; 1.2e-12 rad on an 8-site Floquet tick), while per-site shares fluctuate at order one (0.118). Number conservation gives the vacuum, and the vacuum carried along any edge history, zero amplitude on every configuration of the next charge sector, so a per-configuration vacuum subtraction is defined on none of them (stated). Subtracting the lowest state of the same charge sector makes an added particle at rest source zero (-1.4e-14). Subtracting one vacuum phase of the same edges, E_vac(e), at every configuration of every sector gives an added particle eigenstate exactly its departure E_(N+1)(e) - E_vac(e) at every configuration (Born spread 1.2e-14), which at V = 0 is sqrt((m N)^2 + (2 t cos k)^2) level by level (0.6250, 0.8004, 0.8004, 1.0680); the Born variance of the configuration-resolved source is bounded by the state's own energy variance (0.0927 <= 0.1566 for a 4-level packet), never the sea's. With E_ref = E_vac(e) of the same tick and edges, any displacement breaking cancels except the departure's own (stated): on a static 1D slice the sea's coarse source divergence (6.0e-3 at L = 200) is removed, leaving the departure's own (1.7e-8 moving, 2e-19 at rest), which relative to its pressure vanishes in the smooth limit (6.4e-4, 8.6e-5, 1.1e-5 at L = 100, 200, 400). With two quantum edge registers jointly evolved with an 8-site chain, the vacuum leaves the edges at rest (1.1e-4 against 1.357 raw) and an added particle moves them as its departure surface gives (-1.0738 against -1.0727). The sea's induced edge kinetic term (joint frequency shift -1.572e-5 against -1.565e-5 from the vacuum-overlap hop plus virtual mass) is not a diagonal phase and is not removed by the subtraction. Supplied model, finite diagnostic: 1D chains, the staggered mass, t, m, V, the read-lapse form N = l, the register size and spacing, the edge hop weight and the hinge stand-in, and the measured inputs of the estimates."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/one_vacuum_phase_of_the_same_edges_at_every_configuration_gives_an_added_particle_exactly_its_energy_2026_10_22.py
---

# One vacuum phase of the same edges at every configuration gives an added particle exactly its energy

Claim type: bounded_theorem.
Primary runner: `scripts/one_vacuum_phase_of_the_same_edges_at_every_configuration_gives_an_added_particle_exactly_its_energy_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its response law has edges and links respond only to departures from the vacuum of the same edges. Read per configuration, that is each site's share of the phase by which the update advances the odds, minus the same share for the vacuum odds at the same configuration and edges. Off the vacuum's charge sector the vacuum odds vanish, so this subtraction is undefined exactly where a charged particle lives. This note compares the candidate subtractions in supplied finite toys: the lowest state of the same charge sector, one vacuum phase of the same edges at every configuration, a fixed density, and the carried vacuum. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

Supplied model: a periodic 1D staggered-fermion chain with hop t, staggered mass m and nearest-neighbour interaction V, on two edges (sites x < L/2 read edge 0, the rest edge 1). The update law's 1D read lapse is N = l: the hop amplitude N / l stays t, the mass is m N_x and the interaction V N_b. The configuration-resolved phase-advance rate of a state psi is Re[(H psi)(c) / psi(c)].

A. Which subtraction is defined everywhere.

1. Vacuum. For a vacuum eigenstate on fixed edges, the configuration-resolved rate summed over sites equals E_vac(e) at every configuration on its support. The subtraction for the vacuum is therefore the constant E_vac(e), while the per-site shares fluctuate at order one. The same holds on the two-layer Floquet tick.
2. Off-sector. Number is conserved, so the vacuum, and the vacuum carried along any edge history, has zero amplitude on every configuration with one more particle. A per-configuration vacuum subtraction is defined on none of them. This is a structural statement; the runner records it as a stated check and prints the count of such configurations.
3. Same-sector lowest state. Subtracting the lowest state of the particle's own charge sector makes an added particle at rest source zero at every configuration, and a moving one only its kinetic excess. The particle's rest energy then sources nothing.
4. One vacuum phase of the same edges. Subtracting E_vac(e) at every configuration of every sector gives an added-particle eigenstate exactly its departure E_(N+1)(e) - E_vac(e) at every configuration. At V = 0 and uniform edges each departure is the single-particle level sqrt((m N)^2 + (2 t cos k)^2): rest energy m N at the band bottom plus kinetic.
5. Noise bound. The Born mean of Re[(H psi)/psi] is <H> and the Born mean of |(H psi)/psi|^2 is <H^2>. The configuration-resolved total source of any state therefore has Born spread at most the state's own energy spread, never the sea's.
6. Sea force. Subtracting E_vac(e) removes the sea's force on the edges at every edge configuration (by construction). An edge-blind per-site constant leaves all of it, and a flat density per proper length leaves its nonlinear part.
7. Carried vacuum. Ramping the edges smoothly from rest at rate omega, the carried vacuum's configuration-resolved rate is one number up to O(omega^2). The O(omega) part is imaginary (probability flow), and its Born mean exceeds E_vac at O(omega^2). The carried vacuum equals item 4's reference plus the kinetic half.

B. Conservation.

8. Noether. The edge equation's consistency needs d_xi (E_psi - E_ref)(e) = 0 for every displacement xi. With E_ref = E_vac(e) of the same tick and edges, any breaking cancels except the departure's own, and the subtraction commutes with the momentum constraint iff the raw tick does. The runner states this and does not compute it.
9. Static slice. On a static 1D slice (one particle, hop 1/(2 l_b), m = 0.2, l_b = 1 + 0.2 cos(4 pi b / L)), the sea's coarse edge source has a divergence of first order in the gradient. Subtracting the vacuum of the same edges cancels it, leaving the departure's own. Relative to its own pressure the moving particle's coarse divergence is a lattice term vanishing in the smooth limit; per bond it is order one (a staggered cell-internal oscillation), so conservation holds at the block rung. A fixed density keeps the sea's violation (stated).

C. Quantum edges.

10. Joint odds. Evolving two edge registers (n = -4..4, l = 1 + 0.1 n, edge hop w = 0.05, a supplied hinge stand-in 0.05 n^2 / 2) jointly with an 8-site chain: with E_vac(e) subtracted the vacuum leaves the edges at rest, and an added particle moves them as its departure surface E_(N+1)(e) - E_vac(e) gives (Born-Oppenheimer). Raw, the sea moves them by cell sizes; the same-sector subtraction hides the particle.
11. No extra edge noise. The edge spread changes exactly as the departure surface gives, with no contribution from the particle's order-one per-configuration stress.
12. Kinetic part not a phase. The subtraction leaves the sea's induced edge kinetic term: the edge hop becomes w <vac_e | vac_e'> (the quantum metric) plus a virtual mass 2 sum_k |<k|dH|0>|^2 / dE^3. A diagonal phase cannot change a hop.
13. Dressed weight. A dressed edge hop weight w' absorbs the induced term exactly, so the carried reference is item 4's phase plus dressed weights.

## Derivation

Items 1, 3, 4 and 10 build the chain Hamiltonians in fixed-number sectors with fermionic signs and diagonalise them; item 1 also shares each term equally among its sites. The Floquet tick of item 1 applies even bonds, odd bonds and the mass term in sequence at eps = 0.6. Item 4's free check compares many-body departures with the single-particle spectrum and the closed-form dispersion. Item 5 uses a 4-level packet with seeded random coefficients. Item 6 differentiates E_vac by central differences in each edge. Item 7 integrates the Schrödinger equation through the ramp 1 + 0.1 (1 - cos omega t)^2 / 4, which starts with zero rate and acceleration. Item 9 differentiates single-particle levels in each bond length and smooths with a Gaussian of width 4 bonds. Items 10-13 build the joint chain-register Hamiltonian, diagonalise it with a sparse solver, compare with the Born-Oppenheimer problem on the departure surface, and fit the dressed weight by secant iteration.

## Finite checks

Exact checks (the runner asserts each):
- Vacuum (L = 12, N = 6, 924 configurations, t = m = 0.5, V = 0.3, edges l = (1.00, 1.25)): Born spread of the total 1.3e-14; largest per-site share spread 0.118; sum of Born-mean shares minus E_vac 5.3e-15.
- Floquet tick (L = 8, 70 configurations): phase spread 1.2e-12 rad.
- Off-sector: 792 configurations with N = 7, subtraction defined on 0 (stated).
- Same-sector subtraction: source at rest -1.4e-14, moving 0.2884.
- One vacuum phase of the same edges: source 1.0848 and 1.3731 (levels 1 and 3); edge forces dE_dep / dl = 0.8898 and 0.1766; largest Born spread over three particle levels 1.2e-14.
- Free check (V = 0, l = 1.25): departures 0.6250, 0.8004, 0.8004, 1.0680 against the dispersion 0.6250, 0.8004, 0.8004, 1.0680.
- Packet: Born spread 0.0927 <= energy spread 0.1566.

Finite diagnostics (supplied model, finite diagnostic):
- Sea force on the two edges: raw or edge-blind -0.9580, -1.0556; per proper length +1.4276, +1.3300; with E_vac(e) subtracted 0 by construction.
- Carried vacuum at omega = 0.02 / 0.04: real spread 4.1e-06 / 1.6e-05 (slope 2.00), imaginary spread 4.2e-04 / 8.4e-04 (slope 1.00), mean minus E_vac 9.0e-08 / 3.6e-07 (slope 2.00).
- Static slice, rms divergence of the coarse edge source (mean |T_sea| per bond 0.323 at L = 200):

| L | sea | sea x L | at rest, subtracted | moving, subtracted | moving, div / pressure |
|---|---|---|---|---|---|
| 100 | 1.1e-02 | 1.07 | 4e-19 | 8.2e-07 | 6.4e-04 |
| 200 | 6.0e-03 | 1.20 | 2e-19 | 1.7e-08 | 8.6e-05 |
| 400 | 3.1e-03 | 1.23 | 1e-19 | 3.0e-10 | 1.1e-05 |

  Per bond at L = 200 the moving particle's divergence over its pressure is 15.4.
- Joint odds, mean of register 1: vacuum raw +1.357, vacuum subtracted +1.1e-04; particle shift (subtracted) -1.0738 against -1.0727 from the departure surface; same-sector shift -1.1e-03; raw particle +0.193.
- Variance of register 1: vacuum 0.6383, particle 0.7024, departure surface 0.7045.
- Induced edge kinetic term: bare frequency 0.063859; joint shift -1.572e-05 against -1.382e-05 (vacuum-overlap hop) plus -1.84e-06 (virtual mass) = -1.565e-05; 1 - <vac_0 | vac_1> = 3.72e-04 against half the quantum metric 4.02e-04.
- Dressed weight: w' / w - 1 = 4.46e-04 (estimate 3.72e-04), residual at roundoff.

The packet coefficients use a fixed seed (7).

## Estimates against measurement

- Same-sector subtraction removes every body's rest energy from its source, so the gravitating mass would be at most about 1e-3 of the inertial mass (binding differences only), against their equality to about 1e-15 (MICROSCOPE, lunar laser ranging). Stated, not computed.
- With one vacuum phase of the same edges the source is the tick's own departure energy, so gravitating and inertial energy agree identically at tree level. Stated.
- Without the subtraction the sea's non-conservation is a pressure hbar c / L^4 = 7.3e+110 Pa (L = sqrt(8 pi) l_P) times the fractional edge variation; with it only the departure's own remains, about (p L / hbar)^2 = 4e-51 relative for a 300 K electron. The numbers are computed from supplied constants; the scaling is stated.

## Boundary

Not claimed: any 3D or register-level computation (all toys are 1D chains with two edges or two edge registers); the read-lapse form N = l, the hinge stand-in or the edge hop weight as derived; that the Noether cancellation of item 8 holds beyond the stated argument; the form of the dressed-weight clause beyond the fit of item 13; that the induced edge kinetic term is small in general; the estimates' equivalence-principle statements (stated); any experimental exclusion.

## Supplied vs forced

Supplied: the 1D chains, the staggered mass, t = m = 0.5, V = 0.3, the step eps = 0.6, the read-lapse form N = l, the slice profile and m = 0.2, the Gaussian smoothing width, the register size, spacing 0.1, hop weight w = 0.05 and hinge stand-in 0.05 n^2 / 2, the ramp profile and rates, the packet, and the measured or physical constants of the estimates. Forced, given those: a vacuum eigenstate's configuration-resolved total rate is E_vac(e) on its support; no per-configuration vacuum subtraction exists off its sector; the same-sector subtraction zeroes the rest source; one vacuum phase of the same edges at every configuration gives an added particle exactly its departure energy at every configuration; the Born-variance bound; removal of the sea's coarse divergence; edge motion as the departure surface gives; an induced edge kinetic term that no diagonal phase removes.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's read lapse and staggered mass, and the response law's vacuum standard (edges and links respond only to departures from the vacuum of the same edges) with its dressed weights. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/one_vacuum_phase_of_the_same_edges_at_every_configuration_gives_an_added_particle_exactly_its_energy_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 3 s with about 170 MB resident, prints about 5.9 kB and ends with `TOTAL: PASS=18 FAIL=0`. Its random draw uses a fixed seed. Two runs gave identical output apart from the elapsed-time line and the dressed-weight residual, which is at roundoff (2.2e-16 and 0.0e+00) because the sparse eigensolver starts from an unseeded vector.
