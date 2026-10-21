---
claim_id: candidate_laws
claim_type: meta
claim_scope: "Register of the current working candidate laws CL-1 to CL-6, what follows from them, untested predictions and where the rules are wrong or incomplete; zero premise weight. Several laws restate axiom clauses in the form the evidence needs; the axioms themselves are unchanged. Results that use a candidate law are conditional on it."
---

# Candidate laws

Claim type: meta.

Candidate laws are the current working rules adopted to build on. They are not axioms. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md), [policy section 6](audit/AXIOM_MINIMALITY_POLICY.md#6-explicit-owner-approval-for-axioms-and-primitives) and `docs/audit/data/axiom_premise_nodes.json` alone control premise admission, so this register has zero premise weight. A result that uses a candidate law is conditional on it.

The laws are judged against measured results, not against theoretical preference. Where a law restates an axiom clause, the note says so. The axioms are to be revisited once the laws account for the measured world.

## CL-1: lattice

> "Sites are the points of Z^3. Every nearest-neighbour bond is an edge of exactly one 2x2x2 cube in one of two cube partitions offset by (1,1,1). The symmetries are the translations and proper rotations that preserve the pair of partitions."

This restates the Lattice axiom's symmetry clause. The covariant update of CL-3 is invariant under the 24 proper rotations about cube centres and the translations between them. It is not invariant under rotations about a site.

## CL-2: modes

> "Each site's qubit is one fermion mode, and modes at different sites anticommute."

This makes explicit a cross-site product that the Qubit axiom leaves open.

## CL-3: update

> "The odds, one amplitude per joint occupation of the modes, change only by half-ticks, and the half-ticks alternate between the partitions. In each half-tick every cube of the partition applies the same unitary to its sites. Each site's odds pass to its three edge neighbours equally, with the phase of their spin-3/2 overlap along the body diagonals. A species applies cos(a) W + i sin(a) in place of W, with a = mu/2 + b on even cubes and a = mu/2 - b on odd cubes."

Unitarity of the edge hop W holds exactly when every cube face carries phase -1. With one mode per site, that holds exactly when the site's rotation character makes spin 3/2 (j ≡ 3/2 mod 3), so the spin-3/2 phase is forced rather than chosen.

The light band is an isotropic massive Dirac band of mass mu, with light speed 1/sqrt(3) block per tick. The staggered term b gaps the cone at K = pi(1,1,1). It names a partition only through the sign of mu times b. The light content is two degenerate Dirac copies, and no covariant term splits them.

Evidence:
- `docs/MARGOLUS_SPIN_THREE_HALVES_EDGE_HOP_GIVES_A_CUBE_COVARIANT_DIRAC_TICK_BOUNDED_THEOREM_NOTE_2026-10-21.md`;
- the independent re-check and gap results in the campaign files.

## CL-4: records

> "Each half-tick a record forms at each mode of the actual configuration and locks its occupation. Records are permanent, a site carries at most one record per half-tick, and only records are readable."

This restates the Record axiom's "one per site" as one per site per half-tick. Massive modes revisit sites, and a record locking a site's occupation outright would put Planck-scale noise into the gravitational source, which measurement excludes.

## CL-5: following

> "The actual configuration is distributed as its odds. Each half-tick it moves by a transport that keeps it so, uses only transitions the half-tick connects (staying included), and leaves the most in place."

Such a transport always exists: the half-tick maps the odds of any set of configurations into the odds of the set it connects to, and a supply-demand argument then gives the transport. Records never condition the odds, because the update of CL-3 is the only change they undergo.

The rule acts on the joint configuration of all modes. That is what makes two readers of one pointer agree and lets relays violate CHSH as measured. Number-changing transitions cover pair creation and annihilation.

Evidence:
- `docs/RECORDS_NEVER_CONDITION_THE_ODDS_FORMATION_LAW_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-10-21.md`;
- `docs/RELAY_NUMBER_CHANGE_BY_SWITCHING_CONFINED_TO_TICK_CONNECTED_CONFIGURATIONS_BOUNDED_THEOREM_NOTE_2026-10-21.md`.

## CL-6: response

> "Edge lengths, and links valued in the update's exactly conserved symmetries, take the values at which the total phase is stationary. The total phase has three parts:
> - the matter phase of each part's odds conditioned on the actual configuration of the rest, with each interaction term counted once and shared equally;
> - minus the sum over hinges of area times deficit, in units of the rung's cells, with rotation deficits around hinges that contain a tick direction and rapidity deficits around the others;
> - the links' plaquette phase.
>
> The flat background is the metric in which every source's stress is symmetric. A link's connection is a phase at each site; its holonomies sit on the bonds between neighbouring centres of each partition's cubes."

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

- **Born reading.** CL-5 keeps the configuration distributed as its odds. For a mixing update, the squared magnitude is the only local, phase-blind reading that this preserves (`docs/RELAY_CONSERVATION_SELECTS_THE_SQUARED_MAGNITUDE_READING_OF_THE_ODDS_BOUNDED_THEOREM_NOTE_2026-10-21.md`).
- **Read once.** The transport depends only on the current configuration, so each half-tick's records are the input of exactly one step.
  - A fact many readers share needs many records.
  - Readable trails cannot give which-way knowledge together with fringes, which matches complementarity (`docs/CANDIDATE_LAW_CL3_READ_ONCE_RECORDS_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-10-19.md`).
- **Proper time.** A clock's odds advance in phase at m/gamma, so moving clocks run slow.
- **Magnetic moment.** In any coupling that keeps both half-tick hops reflections, mu and b enter every level the same way, so no Pauli term arises and g = 2 at tree level. Lattice corrections to g - 2 and to the hydrogen 1S-2S line are below 1e-44, far under the measured precision.
- **Photons.** A link quantum is registered only by the record of a site whose odds it changes. That gives photon-counting statistics, bunching and antibunching, complementarity and non-demolition counting.
- **The arrow.** The record set only grows, while the update is reversible.
- **Information.** Between records nothing is lost. At a record the odds lose on average exactly the record's entropy (`docs/RECORD_INFORMATION_ACCOUNTING_LOSSLESS_ODDS_AND_READ_ONCE_RECORDS_BOUNDED_THEOREM_NOTE_2026-10-21.md`).

## Untested predictions

- **Gravity's event-level remote dependence.** The source's Born mean carries no signal, but its event-level distribution depends on a distant measurement setting. For atom-scale systems this is more than 20 orders below any measured source.
- **A single elementary system in superposition gravitates through its full odds.** Composite bodies follow their actual branch.
- **The lattice spacing is a few Planck lengths.**
- **Matter still relative to the lattice at nuclear density would exhaust its sites after about 1e8 years.** Moving matter does not.

## Where the rules are wrong or incomplete

- **Chirality.** A finite-range update gives no net chirality, so parity violation is not reproduced. The charge rule of CL-6 needs chiral content. Interactions that gap mirror fermions without breaking the gauge symmetry are under study.
- **The two copies.** No covariant term splits them, and Schur's lemma gives both the same value of every covariant charge. A second light electron copy would add 8.5e-8 to the electron's g - 2 at one loop, 6.5e5 times the measured precision. On 2^3 cubes two copies are forced for every site action. On 4^3 cells a covariant tick with one light copy exists, but its mass has to be tuned to a critical value.
- **Gauge groups and generations.** No law selects SU(3) x SU(2) x U(1) or three generations.
- **Masses.** mu and b are given per species, and no law predicts a mass ratio. A species' limiting speed is cos(b)/sqrt(3), so the absence of photon decay at 1.4 PeV requires b < 7e-10 for the electron.
- **Vacuum energy and dark matter.** No law gives the cosmological constant or a dark sector. The second copy, the cone partners at quasi-energy pi (charged, with inverted inertia) and records are each excluded as dark matter. The remaining slot is a species with no link, whose mass and abundance only the initial odds would fix, and no law gives the initial odds. Counting records as 4-volume fails: a half-filled sea's configuration is frozen under CL-5, so its record count does not fluctuate as Poisson, and an imported Poisson count matches the size of the constant but its measured equation of state excludes the resulting drift.
- **Supplied pieces.**
  - the rung that sets G and the radian-for-radian unit;
  - the positive/negative frequency branch;
  - the tie-break inside CL-5;
  - quantised bosonic links, which are forced by measured antibunching but not by the laws;
  - the site carrier of the link phase, which needs Z_N with N >= 5 or a U(1) rotor beyond the one qubit. Zooming moves this cost into CL-3 as role-assigned sites but does not remove it.
