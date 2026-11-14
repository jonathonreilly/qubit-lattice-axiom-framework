---
claim_id: edges_reading_the_actual_configuration_radiate_on_every_hop_and_edge_registers_keep_born_transport_no_signalling_and_the_vacuum_standard_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the edge source under the three-law register's laws, used as supplied conditional definitions: (local reading) conditioning one site's odds on the actual occupations of all other sites leaves a single occupation when number or parity is conserved, so a site-split conditional source is the same as reading the actual configuration; a sudden one-cell hop of a point source then releases exactly (1/6)(1 - 1/N^3) q^2/a into a definite edge field on an N^3 torus. (Smoothing) A source of width s that still jumps by a cell releases a^2 q^2/(48 pi^1.5 s^3), a power-law suppression. For the supplied 1D dispersion w = 2 asin(c sin(k/2)), 0 < c < 1, an ordinary (m = 0) resonance of a smoothly translated profile exists iff v_min <= v < c, with v_min = 2 asin(c)/pi the minimum phase speed (exact, by strict concavity of w); below v_min only lattice aliasing radiates, and with the supplied Gaussian form factor the tested case (c = 0.9, v = 0.5) is exponentially small in (s/a)^2 (finite diagnostic). The held 'no m = 0 root for every v < c' is withdrawn: c = 0.9, v = 0.8 has an m = 0 root at |k| = 2.66. (Coarse conditioning) In a two-qubit toy a conditional source coarser than a site lets a remote basis choice change the variance of a readable sourced field at fixed mean: signalling in principle. (Edge registers) An edge register built from fermion-mode sites (2S modes per end, S+ = sum c_L^dagger c_R) closes su(2) with lengths spanning the split window [l_rung, 2 l_rung]; same-type edges in that window always form triangles, mixed axis/face-diagonal triples need not. In a supplied harmonic toy of one quantum edge and one matter oscillator the per-configuration vacuum standard cancels the zero-point force, leaving an edge-motion residual close to 1/(8M), and one matter quantum pushes with force close to hbar omega. That the joint update with edge registers never reads the actual configuration, so that the Born-preserving transport, no signalling and zero hop radiation follow, is a structural reading of the supplied rules, argued and not computed; the runner prints it as NOT CHECKED. Comparisons with measurement (thermal nucleon radiation, interferometer phases, the proposed gravity-mediated entanglement test at 0.79 rad and concurrence 0.156, l_P/L corrections) are estimates with supplied inputs. No register edge dynamics with the originating register's edge hop is computed here."
upstream_dependencies:
  - minimal_axioms
runner: scripts/edges_reading_the_actual_configuration_radiate_on_every_hop_and_edge_registers_keep_born_transport_no_signalling_and_the_vacuum_standard_2026_10_22.py
---

# Edges reading the actual configuration radiate on every hop; edge registers keep the vacuum standard in a toy, and their Born transport and no signalling are argued

Claim type: bounded_theorem.
Primary runner: `scripts/edges_reading_the_actual_configuration_radiate_on_every_hop_and_edge_registers_keep_born_transport_no_signalling_and_the_vacuum_standard_2026_10_22.py`.

Model status (2026-11-14). The update, actuality and response laws (CL-1, CL-2, CL-3 in the three-law numbering of the originating register) are used here as supplied conditional model definitions with zero premise weight, stated where they are used. The originating register text is not in this repository, and these clauses are not the entries of the same number in [docs/CANDIDATE_LAWS.md](CANDIDATE_LAWS.md). No clause is adopted.

The response law (CL-3) sets the edges from departures from the vacuum of the same edges; its actuality law (CL-2) moves one actual configuration by the fewest-change, Born-preserving transport. If the edges are definite values sourced by the matter, something must say which matter: the odds, the actual configuration, or odds conditioned on part of the actual configuration. This note tests two replacements for a source read from the actual configuration: (A) a smooth source read from conditional odds, and (B) quantised edges, edge registers carrying odds like the link registers. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Smooth source from conditional odds.

1. Conditioning a site's odds on the actual occupations of all other sites leaves exactly one occupation of that site whenever particle number (or parity) is conserved. A conditional source split at the site is therefore the local reading of the actual configuration; smoothing needs a conditioning split coarser than a cell, which no clause of CL-1 to CL-3 supplies.
2. A sudden one-cell hop of a point source in a definite edge field on an N^3 torus (units with -Lap phi = rho) releases exactly (1/6)(1 - 1/N^3) q^2/a; for gravity q^2 -> 4 pi G m^2.
3. A Gaussian source of width s that still jumps by one cell releases a^2 q^2/(48 pi^1.5 s^3) at large s: a suppression (a/s)^3 times about 0.022 relative to the point hop, a power law.
4. A profile translated smoothly at speed v on a discrete-time lattice field with the supplied dispersion w(k) = 2 asin(c |sin(k/2)|), 0 < c < 1, has an ordinary (m = 0) resonance iff v_min <= v < c, where v_min = w(pi)/pi = 2 asin(c)/pi is the minimum phase speed. Below v_min it radiates only through lattice aliasing: every emitted mode has |kappa| = |k + 2 pi m| >= pi, and with the supplied Gaussian form factor the radiated power falls as exp(-kappa*^2 s^2), exponentially in (s/a)^2 (tested at c = 0.9, v = 0.5, v_min = 0.713). Negative result kept: the held "no m = 0 root for every v < c" is false; at c = 0.9, v = 0.8 there is an m = 0 root at |k| = 2.66, a resonance that is not an alias. A Gaussian still suppresses that resonance at large s, but by exp(-k^2 s^2) with |k| < pi, not by an alias-only factor.
5. A conditional source coarser than a site lets a remote setting change a readable distribution: in a two-qubit toy, B's conditional sourced dipole has the same mean but a different variance when A's basis changes, while B's own Born marginals do not change.

B. Edge registers.

6. An edge register can be built from fermion-mode sites like CL-1's rishons: 2S modes at each end, S+ = sum_a c_{L,a}^dagger c_{R,a} closes su(2), and the length l = l_rung (1 + n_L/2S) spans exactly CL-1's split window [l_rung, 2 l_rung], one hop moving one length quantum.
7. Three same-type edges with lengths in [L, 2L) always form a nondegenerate triangle (a + b >= 2L > c). Mixed axis/face-diagonal triples can fail, so the register needs a triangle constraint, as quantum Regge measures do; this is left open.
8. With a quantum edge the per-configuration vacuum standard cancels the matter zero-point force omega_0/2 exactly; what remains is the edge-motion (Born-Oppenheimer) term, near 1/(8M) for edge mass M, i.e. a force ratio R = 1/(4 M omega_0). For N matter modes on one collective (scale) mode of mass N M the total residual stays the same, so the residual per cell falls as 1/N. One matter quantum above the vacuum pushes the edge with force close to omega_0 (it sources hbar omega).
9. (Argued, not computed.) With edge registers the joint update never reads the actual configuration. CL-2 then has one target, the Born law, the transport stays exactly Born-preserving, nothing signals, and no hop of the actual configuration reaches the edges; the actual pointer, edge and test-mass values would then agree, and two masses would entangle through the edges as charges do through link registers. This item is a structural reading of the supplied rules. No update with edge registers, no Page-Geilker-generating dynamics and no mediator-side entanglement is computed: the runner's three-register state is correlated by construction, so it prints this item as NOT CHECKED and counts nothing for it.

## Derivation

Item 1. With N conserved, the site's occupation equals N minus the total of the other sites; with parity conserved it equals the parity minus that total mod 2. Every configuration with nonzero amplitude and the given occupations elsewhere therefore has the same value at the site.

Item 2. On the torus the hop changes the source by delta rho = rho - T rho, with |delta rho_k|^2 = 4 sin^2(k_x/2) for a point source. The field energy released is (1/2) N^-3 sum_{k != 0} |delta rho_k|^2 / w_k^2 with w_k^2 = sum_i 4 sin^2(k_i/2). Cubic symmetry makes the three terms 4 sin^2(k_i/2)/w_k^2 equal on average, and they sum to 1 at each k != 0, so each averages 1/3 over the N^3 - 1 nonzero momenta: (1/2)(1/3)(1 - 1/N^3) = (1/6)(1 - 1/N^3).

Item 3. For a smooth profile the jump energy is (1/2) int |rho_k|^2 k_x^2/k^2 d^3k/(2 pi)^3 at small k; for a normalised Gaussian of width s this is 1/(48 pi^1.5 s^3).

Item 4. A profile f(x - vt) sampled on a discrete-time lattice emits at the solutions of +-w(k) = (k + 2 pi m) v + 2 pi n. Write w(k) = 2 h(k/2) with h(s) = asin(c sin s); then h''(s) = -c sin s (1 - c^2)/(1 - c^2 sin^2 s)^(3/2) < 0 on (0, pi/2], so w is strictly concave on (0, pi] with w(0) = 0, and w(k)/k falls strictly from c (k -> 0) to v_min = 2 asin(c)/pi (k = pi). For m = 0, |w| < pi and |kv| < pi force n = 0, so an m = 0 root with k != 0 is a solution of w(k)/|k| = v: it exists iff v_min <= v < c. For v < v_min every root has m != 0, hence |kappa| = |k + 2 pi m| >= 2 pi - pi = pi, and the supplied Gaussian form factor gives the weight exp(-kappa^2 s^2). The runner checks the concavity formula against a numerical second difference, the witness v = 0.8, and a sweep of v.

Item 5. For |0>_A |L>_B + |1>_A |R>_B, A's basis choice (Z or X) does not change B's reduced state, but it changes the set of conditional means of B's position given A's actual value: in Z they are -d/2 and +d/2 (variance d^2/4), in X both are 0. A source that reads that conditional mean then has a setting-dependent fluctuation at B.

Item 6. The 2S modes at each end obey the canonical anticommutators; S+ S- - S- S+ = 2 Sz follows from them, and on the sector with one fermion per flavour the top multiplet has dimension 2S + 1. n_L runs from 0 to 2S.

Item 8. With the edge coordinate q, the matter frequency w(q) and the subtraction w(q)/2 per configuration, the zero-point term no longer depends on q; the remaining q-dependence comes from the edge's own zero-point motion in the matter potential, of order 1/(8M) for a harmonic edge.

Item 9. With edges as registers the edge values are part of the joint odds; the half-tick acts on the joint odds alone, and CL-2's transport acts afterwards on a law equal to those odds. Nothing in the update takes the actual configuration as input.

## Checks

The runner ends with `TOTAL: PASS=16 FAIL=0` in about 1 s and exits nonzero if any counted check fails. Several passing lines are estimates; they are listed as such below. Item 9 is printed as NOT CHECKED and the entanglement phase as ESTIMATE; neither is counted.

Exact checks and identities (checked numerically):
- Conditional support of a site, chain of L = 8 sites with random amplitudes: maximum support 1 in the N = 3 sector and 1 in the parity-even sector.
- Point hop on 16^3 and 32^3 tori: maximum deviation from (1/6)(1 - 1/N^3) is 2.8e-17.
- Width-s hop on 64^3 against 1/(48 pi^1.5 s^3): s = 2: 4.67e-04 / 4.68e-04; s = 3: 1.38e-04 / 1.39e-04; s = 4: 5.78e-05 / 5.85e-05 (tolerance 5%).
- Two-qubit conditional source: B's dipole variance 0.25 d^2 in the Z basis against 0 in the X basis, equal means, equal Born marginals at B.
- Edge register with 2S = 4: anticommutator deviation 0, [S+, S-] - 2 Sz deviation 0, top multiplet dimension 5, lengths 1.00 to 2.00 l_rung.
- Triangles on a 40-point grid per edge type: same-type triples always nondegenerate; axis-axis-face-diagonal violating fraction 0.069.
- Minimum phase speed (A4a): the concavity formula for w'' matches a numerical second difference to 2e-7 on (0, pi); w(k)/k falls strictly; v_min = 0.7129 at c = 0.9.
- Held all-v statement rejected (A4b): at c = 0.9, v = 0.8 an m = 0 root at |k| = 2.657; over v = 0.3 to 0.89 an m = 0 root appears exactly when v >= v_min.

Finite diagnostics (supplied model, finite diagnostic, no physical identification):
- Smooth translation (1D lattice field with w = 2 asin(c |sin(k/2)|), c = 0.9, v = 0.5 < v_min, |m|, |n| <= 3): m = 0 roots 0; kappa* = 3.927 (>= pi); fitted log-slope of the radiated weight against s^2 is 15.42 against kappa*^2 = 15.42; W(2.5)/W(1) = 7e-36. The Gaussian form-factor weighting is supplied.
- Quantum edge toy (supplied harmonic edge kinetic term and stiffness K = M on 81 grid points in |q| <= 0.5, one matter oscillator with w(q) = omega_0/(1 + q), omega_0 = 2, 12 levels): ground-state edge force 0.9918 without the vacuum standard, 2.35e-03 with it; ratio R = 2.37e-03 against the Born-Oppenheimer estimate 2.49e-03 (tolerance 15%); at four times the edge mass R = 5.56e-04.
- Collective mode (two matter modes, 9 levels each, on one edge of mass 100, 61 grid points): R = 1.16e-03 against R(N = 1, M = 50)/2 = 1.19e-03 (tolerance 25%).
- One matter quantum (<n> = 1.005) above the vacuum: (F1 - F0)/omega_0 = 0.9552 (tolerance 5%).
- Vacuum of a free lattice field on 48^3 standing in for the edge registers' vacuum, averaged over L^3 cubes: Var L^2 = 0.178, 0.154, 0.141 at L = 2, 4, 8 (ratio of extremes below 1.35), consistent with delta l/l ~ l_P/L.
- Three-register toy (pointer, edge, test mass) correlated by construction: P(deflection disagrees with pointer) = 0 by construction. Printed as NOT CHECKED (item 9); it simulates no update and is not counted.

## Estimates against measurement

All of these are estimates with supplied inputs (G, hbar, c, l_P, a = sqrt(8 pi) l_P per cell, nucleon mass, experiment geometries):
- Thermal (300 K) nucleon with the local reading: about 5e+07 W radiated into the edges, against a budget of about 3e-31 W (1e-3 m_p c^2 per Hubble time). An fm-wide conditional source still jumping a cell per partner hop: about 6e-52 W. A block split of size l_s would need l_s > 1e-15 m; the runner's statement that Page-Geilker then needs l_s below about 1e-2 m is stated, not computed.
- Coarse conditioning at the scale of the proposed tabletop test (1e-14 kg, 250 um splitting, at 1 mm): a field split of about 2e-19 m/s^2 per run.
- A lone particle sourcing from its full odds (Schrodinger-Newton self-term): the Fein et al. (2019) molecule phase about 4e-17 rad and a 54 cm rubidium arm attraction phase about 1e-25 rad; self-collapse at 1 um needs about 3e+09 amu. Every interferometer so far is far inside the null region.
- Gravity-mediated entanglement (1e-14 kg masses, d = 200 um, splitting 250 um, 2.5 s): phase G m^2 t/(hbar d) = 0.79 rad and concurrence |sin(Delta phi/2)| = 0.156, from the Newtonian phase formula with that supplied geometry. That edge registers would mediate it is item 9 (argued, not computed); a definite edge gives concurrence 0 (stated). Printed as an uncounted ESTIMATE line.
- Corrections (l_P/L)^2 to results derived with definite edges: Gravity Probe B (7e6 m) 5e-84, light bending (7e8 m) 5e-88, Hulse-Taylor timing (1e9 m) 3e-88, Friedmann law (H0 t_P)^2 1e-122. The (l_P/L)^2 scaling is assumed from the vacuum diagnostic above. The LIGO figure (4 km, about 4e-39 against 1e-23 strain) is stated in the runner, not computed. Results at Planck curvature (crush and split epochs) are not controlled.
- The runner also prints hbar/tau = 4e+08 J against a hop energy of 5e-31 J, with no check.

## Boundary

Supplied: the conditioning toys and their sizes, the Gaussian profiles, the 1D dispersion and speeds of the aliasing diagnostic, the two-qubit signalling toy, 2S = 4 for the edge register, the length grids, the harmonic edge kinetic term, mass and stiffness of the vacuum-standard toy and its matter frequency w(q), the free-field stand-in for the edge vacuum, the constructed pointer/edge/test-mass state, and every input of the estimates. Forced, given those: that a site-split conditional source is the local reading; the exact 1/6 hop release; power-law suppression for jumping sources and exponential suppression for smooth motion below v_min (tested at one speed); the minimum-phase-speed condition; setting dependence of a readable variance under coarse conditioning; the su(2) closure and length window of the fermion-mode edge register; the triangle statements; cancellation of the zero-point force by the vacuum standard in the toy and the size of its residual. Not claimed: an alias-only radiation mechanism at any v >= v_min (withdrawn; item 4); any result with the originating register's edge hop (S+ + S- normalised on its domain, sign opposite to matter's), since the toy here uses a supplied harmonic edge kinetic term and should be re-checked with that hop; the triangle constraint for mixed edges; stability of the edge vacuum; any computed update with edge registers (item 9 is argued, not simulated), and so no computed Born transport, no-signalling or entanglement statement for edge registers; that the estimates are predictions beyond their supplied inputs; any statement at Planck curvature.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- Supplied model (originating three-law register, not in this repository; stated here as conditional definitions with zero premise weight): the split window and fermion-mode sites of the update law, the Born-preserving transport of the actuality law, and the vacuum standard of the response law. [docs/CANDIDATE_LAWS.md](CANDIDATE_LAWS.md) does not contain these clauses.

## How to run

```
python3 scripts/edges_reading_the_actual_configuration_radiate_on_every_hop_and_edge_registers_keep_born_transport_no_signalling_and_the_vacuum_standard_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s with about 110 MB resident, prints about 5.5 kB and ends with `TOTAL: PASS=16 FAIL=0`; it exits nonzero if any counted check fails. Its random amplitudes are seeded; the sparse eigensolver in the vacuum-standard toy has no fixed start vector, but repeated runs gave identical printed output apart from the elapsed-time line.
