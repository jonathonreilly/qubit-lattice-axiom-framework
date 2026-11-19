---
claim_id: link_quanta_registered_by_site_records_reproduce_photon_counting_statistics_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "In supplied tiny models where configurations are site occupations only and link modes carry quantised odds but no records, shortfall switching restricted to tick-connected classes reproduces Born record statistics without rewriting earlier records; complete absorption gives the port photon-number distribution, with thermal, coherent and Fock bunching values; classical link mixtures cannot give g2 < 1; which-way visibility and distinguishability satisfy V^2 + D^2 = 1 with an eraser; dispersive marker sites register link number without absorption; composite site-pair bosons deviate from Bose statistics by prod(1 - k/N) and have no single frequency; with the link field obeying Maxwell the conserved quadratic link tensor is the Maxwell tensor. Quantised link odds, detectors, couplings and the response forms are supplied. No registration law, link deposit rule or physical photon identification is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/link_quanta_registered_by_site_records_reproduce_photon_counting_statistics_2026_10_21.py
---

# Link quanta registered by site records reproduce photon-counting statistics

Claim type: bounded_theorem.
Primary runner: `scripts/link_quanta_registered_by_site_records_reproduce_photon_counting_statistics_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. It gives a link field but no rule for how link quanta are registered. This note asks whether a minimal construction fits the standard photon experiments. In that construction, records are made of site occupations only, and link modes carry odds but no configuration and no records. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply the Record axiom. Quantised link odds and every detector model are supplied. Detection need not be absorption: a link quantum can be registered by the record of any site whose odds it changed, either by absorption or by a phase.

## Statement

1. Born records. With site-only configurations, shortfall switching kept within the classes that the tick connects reproduces the Born record statistics, and earlier records never change. Without the class restriction, earlier records are rewritten. Giving link occupations a configuration leaves the record statistics unchanged.
2. Counting. Under complete absorption the record counts equal the photon-number distribution at each port. Mandel Q is 0 for coherent light, +0.5 for thermal light with mean 0.5, and -1 for one- and two-quantum Fock states. The HBT g2 is 2 (thermal), 1 (coherent), 0 (one quantum) and 0.5 (two quanta).
3. Quantised link odds are needed. Any mixture of classical (coherent) link fields has g2 >= 1 by Cauchy-Schwarz. A measured g2 below 1 therefore needs odds on link occupations. That is supplied; it is not in the axioms or in the register.
4. Which way. In a Mach-Zehnder with a which-way marker site, visibility is |cos beta| and distinguishability is |sin beta|, so V^2 + D^2 = 1. Reading the marker in the rotated basis restores visibility 1 in each record class.
5. Non-demolition. Dispersive marker sites, with Kraus operators diagonal in link number, collapse the number without absorbing it. A later absorption count agrees with the collapsed value.
6. Composite photons. For B = N^(-1/2) sum a_l^dag a_u, the norm of B^dag^n acting on the ground state, divided by n!, is prod_(k<n)(1 - k/N), and [B, B^dag] = 1 - 2 N_exc/N. Thermal composite light falls short of g2 = 2 by about 6/N. A free site-pair composite at fixed momentum has no single frequency, so composites would need a supplied binding interaction.
7. Gravity of link energy. If relays and links exchange energy at rate Gamma, a conserved source requires the link coupling to equal the relay coupling. With the link field obeying Maxwell's equations, the unique quadratic tensor whose divergence is minus the force on the value current is the Maxwell tensor. Its energy (E^2 + B^2)/2 is non-negative and it is traceless, so a link-quantum gas has p = rho/3. A plane wave deposits (energy) u u with u = (1, k/|k|), the same null form the register gives a relay at the top speed.

## Derivation

For item 1, the configuration space is site occupations. The tick conserves link-plus-detector excitation per port, and shortfall switching moves weight only between configurations the tick connects. So the class odds are conserved and records already formed are not revisited. Item 3 follows because a mixture of coherent states has <n(n-1)> = <|alpha|^4> >= <|alpha|^2>^2. Item 6 is direct Fock-space algebra for one fermion per site pair. Item 7 uses the vanishing divergence of the linearised Einstein operator: the total source must be conserved, and the relay and link pieces exchange energy, so the divergence (kappa_R - kappa_L) Gamma must vanish.

## Checks

The runner prints 16 PASS lines, and its output ends `TOTAL: PASS=16 FAIL=0` (1.2 s).

- `A0` detector raisings of different site pairs commute exactly.
- `A1`:
  - the tick conserves excitation per port;
  - 20000 sampled record patterns over 256 patterns match the Born site marginal within 2.0, 1.8 and 1.6 sigma for Fock 1, Fock 2 and coherent input;
  - the controls: 2238 record rewrites without the class restriction, and 2.3 sigma with 0 excitation-breaking jumps when link occupations get a configuration.
- `A2`:
  - leftover link quanta are below 1e-12;
  - the printed g2 and Q values are 1.0000 and -0.000 (coherent, mean 1), 1.9999 and +0.500 (thermal, mean 0.5), 0.0000 and -1.000 (Fock 1), and 0.5000 and -1.000 (Fock 2);
  - the lowest g2 over 200 random classical mixtures is 1.0569.
- `A3` V = 1.000, 0.866, 0.707 and 0.000 at beta = 0, pi/6, pi/4 and pi/2, with eraser V = 1.000 in both classes.
- `A4` after 120 markers, agreement 1.0000 with later absorption and Born agreement within 1.4 sigma. The collapse in A2 to A4 is an effective one; only the tiny model of A1 tests it.
- `B1` the product formula and the commutator on N = 4 to 1e-12.
- `B2` 2 - g2 = 0.590, 0.0926, 0.0117 and 0.00146 for N = 8, 64, 512 and 4096, scaling as 1/N.
- `B3` at q = 2 pi/24 the link frequency is 0.2611, while pair energies span 0.2588 to 3.445.
- `C1` only solves (kappa_R - kappa_L) Gamma = 0 for kappa_L symbolically. The vanishing divergence of the Einstein operator is an input, not computed.
- `C2` the symbolic solution alpha = 1, beta = -1/4 for the quadratic ansatz.
- `C3` the plane-wave null form.
- `C4` the bookkeeping of odds-weighted link deposits with site-only configurations:
  - Fock light keeps every trajectory's deposit total exactly;
  - coherent light with mean 2 gives zero-mean registration noise Omega(n_counted - <n>), with a mean jump of +0.918 Omega per click, a total change of mean +0.006 and standard deviation 1.427 Omega, against sqrt 2 = 1.414.

The runner also prints a cosmology estimate. If photons did not gravitate, the radiation density would read as N_eff = -1.36, against the measured 2.99 +- 0.17 (about 26 sigma), and the nucleosynthesis-era shift would be -1.14. This enters no check.

## What is supplied and the boundary

Supplied: quantised bosonic link modes; the detector site pairs and their coupling; beam splitters, phases and markers; the input states; the shortfall rule with tick-connected classes; and, in section C, the linearised-Einstein response and the quadratic, gauge-invariant ansatz for the link tensor.

Not established:
- an adopted registration law;
- the rule by which link energy enters the record source. Two variants remain open. In one, links deposit the Maxwell stress weighted by their odds given the records, which gives the zero-mean registration noise of C4. In the other, link occupations get a configuration that forms no record, which conserves energy jump by jump but adds a new item;
- any physical identification of link quanta with photons.

The experimental figures are quoted as estimates and were not checked against sources.
