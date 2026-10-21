---
claim_id: candidate_laws
claim_type: meta
claim_scope: "Register of the current working candidate laws CL-1 to CL-5, what follows from them, untested predictions and where the rules are wrong or incomplete; zero premise weight. Several laws restate axiom clauses in the form the evidence needs; the axioms themselves are unchanged. Results that use a candidate law are conditional on it."
---

# Candidate laws

Claim type: meta.

Candidate laws are the current working rules adopted to build on. They are not axioms. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md), [policy section 6](audit/AXIOM_MINIMALITY_POLICY.md#6-explicit-owner-approval-for-axioms-and-primitives) and `docs/audit/data/axiom_premise_nodes.json` alone control premise admission, so this register has zero premise weight. A result that uses a candidate law is conditional on it.

The laws are judged against measured results, not against theoretical preference. Where a law restates an axiom clause, the note says so. The axioms are to be revisited once the laws account for the measured world.

## CL-1: sites and modes

> "Sites are the points of Z^3, tiled in two ways by 2x2x2 cubes offset by (1,1,1). Each site's qubit is one fermion mode, and modes at different sites anticommute."

This restates the Lattice axiom's symmetry clause in the form the update needs and makes explicit a cross-site product that the Qubit axiom leaves open. It is a theorem that every bond lies in exactly one cube of exactly one tiling, and that the symmetries preserving the pair of tilings are the translations by 2Z^3 and (1,1,1) + 2Z^3 and the 24 proper rotations about cube centres. Rotations about a site are not among them.

## CL-2: update

> "The odds, one amplitude per joint occupation of the modes, change only by half-ticks that alternate between the tilings. In each half-tick every cube of the tiling applies the same unitary to its sites. Let W pass each site's odds to its three edge neighbours equally, with the phase of their spin-3/2 overlap along the body diagonals. A species of mass mu applies exp(-i(eps - mu/2)W) on every even cube and exp(+i(eps + mu/2)W) on every odd cube, with one step eps for all species."

W is a unitary reflection exactly when every cube face carries phase -1. With one mode per site, that holds exactly when the site's rotation character makes spin 3/2, so the spin-3/2 phase is forced rather than chosen.

The bands obey cos w = A S - (cos 2b - cos mu)/2, with b = pi/2 - eps, A = (cos 2b + cos mu)/2 and S the cubic structure factor. The light band is an isotropic massive Dirac band of mass mu, with speed sin(eps)/sqrt(3) block per tick, and its partner cone at K = pi(1,1,1) is gapped. eps is a time step: eps -> 0 is the continuous-time limit. Because eps is shared, every species has the same limiting speed, which the absence of vacuum photon decay at 1.4 PeV and the SN1987A neutrino timing require. A species-dependent step is excluded by both. The light content is two degenerate Dirac copies, and no covariant term splits them.

Evidence:
- `docs/MARGOLUS_SPIN_THREE_HALVES_EDGE_HOP_GIVES_A_CUBE_COVARIANT_DIRAC_TICK_BOUNDED_THEOREM_NOTE_2026-10-21.md`;
- the independent re-check and gap results in the campaign files.

## CL-3: records

> "Each half-tick, each mode gets a permanent record of its occupation in the actual configuration. Only records are readable."

This restates the Record axiom's "one per site" as one per site per half-tick; with one mode per site the bound follows. Massive modes revisit sites, and a record locking a site's occupation outright would put Planck-scale noise into the gravitational source, which measurement excludes.

## CL-4: following

> "The actual configuration is distributed as its odds. Each half-tick it moves by a transport that keeps it so, uses only transitions (staying included) along nonzero elements of the half-tick, changes the fewest mode occupations on average, and of those is the one of greatest entropy."

Such a transport always exists: the half-tick maps the odds of any set of configurations into the odds of the set it connects to, and a supply-demand argument then gives the transport. Counting changed occupations rather than changed configurations keeps unentangled relays independent, and the greatest-entropy choice makes the transport unique and independent of labels. The mean drift of relays equals the group velocity exactly. Records never condition the odds, because the update of CL-2 is the only change they undergo.

The rule acts on the joint configuration of all modes. That is what makes two readers of one pointer agree and lets relays violate CHSH as measured. Number-changing transitions cover pair creation and annihilation.

Evidence:
- `docs/RECORDS_NEVER_CONDITION_THE_ODDS_FORMATION_LAW_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-10-21.md`;
- `docs/RELAY_NUMBER_CHANGE_BY_SWITCHING_CONFINED_TO_TICK_CONNECTED_CONFIGURATIONS_BOUNDED_THEOREM_NOTE_2026-10-21.md`.

## CL-5: response

> "Edge lengths, and links valued in the update's exactly conserved symmetries, take the values at which the total phase is stationary. The total phase has three parts:
> - the matter phase of each part's odds conditioned on the actual configuration of the rest, with each interaction term counted once and shared equally;
> - minus the sum over hinges of area times deficit, in units of the rung's cells, with rotation deficits around hinges that contain a tick direction and rapidity deficits around the others;
> - the links' plaquette phase.
>
> The flat background is the metric in which every massless source's stress is symmetric. A link's connection is a phase at each site; its holonomies sit on the bonds between neighbouring centres of each partition's cubes."

**Gravity.**
- The second variation is the linearised Einstein operator, with G = a^2/(8 pi) per cell.
- The field gives attraction and gamma = 1.
- Gravitational waves carry positive energy and travel at the matter light speed.
- Every part couples with the same strength, including binding energy and light.
- For a system that is its own pointer, the source follows the actual outcome (Page and Geilker 1981).

**Links.**
- A conserved value current gives Maxwell, and a self-coupled multiplet gives Yang-Mills with the Jacobi identity.
- The site phase and the centre-bond holonomies are one photon at two levels, related by an exact gauge-covariant map. On the centre lattices the photon has the fermion band at every momentum, and the symmetric-stress clause fixes its speed equal to the fermion speed without a tuned coupling.
- A magnetic term cannot act inside one cube, and a register hopped by W is fermionic, so the photon is not a mode of the update itself.
- Links attach only to currents the full update conserves exactly. On chiral content this leaves hypercharge, fixes the charge pattern and gives baryon and lepton number no massless field.

Evidence:
- `docs/RECORD_PROGRAM_THEOREMS_REDERIVED_BOUNDED_THEOREM_NOTE_2026-10-21.md`;
- `docs/LORENTZIAN_REGGE_CONTINUATION_AND_THE_ATTRACTIVE_GEOMETRY_PHASE_SIGN_BOUNDED_THEOREM_NOTE_2026-10-21.md`;
- `docs/REGGE_ACTION_PER_CELL_AND_THE_CONDITIONAL_GRAVITY_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-21.md`;
- `docs/CONDITIONAL_ODDS_CANONICAL_STRESS_AS_THE_RELAY_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-21.md`;
- `docs/VECTOR_RESPONSE_TO_LABELLED_RELAY_VALUES_FORCES_LIE_ALGEBRA_SELF_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-21.md`;
- `docs/RELAY_VALUE_CURRENT_AND_THE_VECTOR_FIELD_IT_SOURCES_BOUNDED_THEOREM_NOTE_2026-10-21.md`.

## What follows without a further law

- **Born reading.** CL-4 keeps the configuration distributed as its odds. For a mixing update, the squared magnitude is the only local, phase-blind reading that this preserves (`docs/RELAY_CONSERVATION_SELECTS_THE_SQUARED_MAGNITUDE_READING_OF_THE_ODDS_BOUNDED_THEOREM_NOTE_2026-10-21.md`).
- **Read once.** The transport depends only on the current configuration, so each half-tick's records are the input of exactly one step.
  - A fact many readers share needs many records.
  - Readable trails cannot give which-way knowledge together with fringes, which matches complementarity (`docs/CANDIDATE_LAW_CL3_READ_ONCE_RECORDS_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-10-19.md`).
- **Proper time.** A clock's odds advance in phase at m/gamma, so moving clocks run slow.
- **Magnetic moment.** In any coupling that keeps both half-tick hops reflections, mu and eps enter every level the same way, so no Pauli term arises and g = 2 at tree level. Lattice corrections to g - 2 and to the hydrogen 1S-2S line are below 1e-44, far under the measured precision.
- **Photons.** A link quantum is registered only by the record of a site whose odds it changes. That gives photon-counting statistics, bunching and antibunching, complementarity and non-demolition counting.
- **Expansion law.** On cubic slices the stationary total phase gives the Friedmann law H^2 = (8 pi G/3) rho (1 - rho/rho*), with rho* = 3/(4 pi G l^2) and growth never faster than sqrt(2) edges per light crossing. Dust grows as t^(2/3) and radiation as t^(1/2).
- **The arrow.** The record set only grows, while the update is reversible.
- **Information.** Between records nothing is lost. At a record the odds lose on average exactly the record's entropy (`docs/RECORD_INFORMATION_ACCOUNTING_LOSSLESS_ODDS_AND_READ_ONCE_RECORDS_BOUNDED_THEOREM_NOTE_2026-10-21.md`).

## Untested predictions

- **Gravity's event-level remote dependence.** The source's Born mean carries no signal, but its event-level distribution depends on a distant measurement setting. For atom-scale systems this is more than 20 orders below any measured source.
- **A single elementary system in superposition gravitates through its full odds.** Composite bodies follow their actual branch.
- **The lattice spacing is a few Planck lengths.**
- **Matter still relative to the lattice at nuclear density would exhaust its sites after about 1e8 years.** Moving matter does not.

## Where the rules are wrong or incomplete

- **Chirality.** A finite-range update gives no net chirality at any rung, and the tick has an exact inversion that swaps left and right, so parity violation is not reproduced. Records, the transport and the responses do not help: every half-tick stays a block unitary of a fixed tiling whatever chooses it, so the net flow of every history is zero, and coherent chirality from records would need coherent fermionic registers, which are mirror fermions under another name. Chirality therefore needs interactions that give the mirror family a large mass. The charge rule of CL-5 needs chiral content. Interactions that gap mirror fermions without breaking the gauge symmetry are under study.
- **The two copies.** No covariant term splits them, and Schur's lemma gives both the same value of every covariant charge. A second light electron copy would add 8.5e-8 to the electron's g - 2 at one loop, 6.5e5 times the measured precision. On 2^3 cubes two copies are forced for every site action. On 4^3 cells a covariant tick with one light copy exists, but its mass has to be tuned to a critical value.
- **Gauge groups and generations.** No law selects SU(3) x SU(2) x U(1) or three generations. Read one rung up with each 2x2x2 cell's modes carried together, a cell holds one lepton and three colours, each as an up and a down state, with the multiplet pattern of one measured generation. The cell factors uniquely as one (4,2) of SU(4) x SU(2), and B - L and T3 are the only charges rotations leave alone. Rotations can be taken to leave the cell index fixed, so every cell state is a spin-1/2 Dirac fermion. With the measured masses the tick keeps only colour-type U(3) x U(3) x U(1) x U(1), the second copy is a mirror family rather than a right-handed half, and no cell of 2^n sites per side holds three families.
- **Unobserved massless links.** On left-right symmetric content CL-5 allows massless links on T3, B - L and species number, which equivalence-principle tests exclude, so CL-5 needs a further selection rule.
- **Masses.** mu is given per species, and no law predicts a mass ratio or the step eps. If link quanta are quantised, partner-cone pairs at K = pi(1,1,1) can be made from the vacuum together with light quanta, since quasi-energy is conserved only mod 2pi; keeping that below the measured vacuum stability needs eps below about 0.04.
- **Vacuum energy and dark matter.** No law gives the cosmological constant or a dark sector. The second copy, the cone partners at quasi-energy pi (charged, with inverted inertia) and records are each excluded as dark matter. The remaining slot is a species with no link, whose mass and abundance only the initial odds would fix, and no law gives the initial odds. Counting records as 4-volume fails: a half-filled sea's configuration is frozen under CL-4, so its record count does not fluctuate as Poisson, and an imported Poisson count matches the size of the constant but its measured equation of state excludes the resulting drift.
- **Initial odds and cosmology.** No law gives the initial odds. Any odds the tick leaves unchanged, including the empty state and the half-filled sea, freeze the configuration under CL-4. Number conservation and the strict light cone fix the large-scale spectrum by the start: starting correlations that fall off faster than a power give an index of 0 or at least 2, never the measured 0.965. On a fixed lattice the update conserves lattice momentum, so growing edge lengths give no redshift and expansion is not observable. Splitting each cube into eight, with each corner mode shared evenly by that corner of the eight children, gives the exact factor-2 redshift and breaks the strict-cone premise, but it changes the Lattice axiom and heats a half-filled sea. A fixed number of ticks per split gives an index of exactly 1, and the measured 0.965 needs the ticks per split to grow by about 1% per split, which no law supplies. The baryon excess needs number- and CP-violating terms.
- **Relay paths.** In some plane waves the relays of CL-4 split into two sublattice streams that move at different speeds, while measured tracks move at one speed.
- **Supplied pieces.**
  - the rung that sets G and the radian-for-radian unit;
  - the positive/negative frequency branch;
  - quantised bosonic links. Measured antibunching forces them, and so does CL-4: a link that responds as a definite value to the actual configuration makes the realised odds carry information about it, which breaks the Born distribution of CL-4. The same holds for a definite geometry, though at gravitational strength the effect is far below measurement;
  - the site carrier of the link phase, which needs Z_N with N >= 5 or a U(1) rotor beyond the one qubit if the qubit stays the fermion mode. Read as flux instead, the qubits can carry an emergent Coulomb photon, but then a fermion is a neutral dipole rather than a charge. Zooming moves this cost into CL-2 as role-assigned sites but does not remove it.
