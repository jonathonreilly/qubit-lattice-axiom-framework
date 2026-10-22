---
claim_id: no_configuration_or_record_rule_sources_the_response_and_the_copy_mass_sea_motion_is_a_particle_hole_shuttle_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Under the register's update, actuality and response laws: the actuality law never changes the odds and the vacuum odds return every tick, while the response law subtracts the vacuum odds at the same configuration, so the matter source is zero at every configuration and no rule acting only on the configuration or the records (any rate, record reading or cost) sources the response; the half-ticks are one-body unitaries, so number is conserved exactly. Finite diagnostic on 12-site 3x2x2 patches of the supplied copy-massed tick at (b, mu, M) = (0.3, 0.4, 0.5): the sea's odds at the two half-tick stages are exchanged by particle-hole conjugation (equally the fourfold turn or a mirror), so the forced configuration motion is a period-2 particle-hole shuttle of at least 2.5e-4 flips per site per half-tick that leaves every even-order density statistic and every turn-symmetric count unchanged and whose C-odd part averages to zero over each tick. Escapes are estimates. No source of matter, baryon excess or clock is found."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/no_configuration_or_record_rule_sources_the_response_and_the_copy_mass_sea_motion_is_a_particle_hole_shuttle_2026_10_22.py
---

# No configuration or record rule sources the response, and the copy-mass sea motion is a particle-hole shuttle

Claim type: bounded_theorem.
Primary runner: `scripts/no_configuration_or_record_rule_sources_the_response_and_the_copy_mass_sea_motion_is_a_particle_hole_shuttle_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its initial-odds entry records that with the update law's copy mass (CL-1 in the three-law numbering) the sea's odds differ between the two half-ticks, so the actuality law (CL-2) moves the vacuum configuration. Its response law (CL-3) is the vacuum-standard principle: edges and links respond only to departures from the vacuum of the same edges. This note asks whether that forced motion creates departures the response law can see, whether it carries a clock or a baryon excess, and what any rule acting on the configuration or the records could add. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the tick, the angles or the vacuum branch.

## Statement

1. The actuality law never changes the odds, and the vacuum odds return every tick. The response law's matter phase subtracts, at the actual configuration, the same share for the vacuum odds at that configuration on the same edges. So the odds' departure from the vacuum is zero at every tick and the matter source is zero at every configuration: no rule that acts only on the configuration or the records, whatever its rate, record reading or cost, sources the response.
2. The half-ticks are one-body unitaries, so the actuality law's transitions conserve the mode number exactly.
3. Supplied model, finite diagnostic: on the copy-massed tick at (b, mu, M) = (0.3, 0.4, 0.5), the sea's odds on a 12-site 3x2x2 patch differ between the half-tick stages (zero at M = 0). Stage 1 equals stage 0 under particle-hole exchange, equally under the fourfold turn about x or the yz mirror; particle-hole exchange composed with the fourfold turn, and the half turn, each keep a stage. So the forced configuration motion is a period-2 shuttle P -> P o PH -> P.
4. Consequences of 3 (exact once 3 holds): every even-order density statistic (|C_ij|, four-site loops) is the same at both stages, while odd orders, such as the third cumulant of three sites, flip sign. A region mapped to itself by the fourfold turn has the same count distribution at both stages, since P1(N) = P0(n - N) = P0(N), so the shuttle is invisible to every coarse cube count. The only C-odd part, the odd cumulants, averages to zero over each tick, so there is no CP-odd bias.
5. Supplied model, finite diagnostic: the shuttle starts at two cubes across (nothing moves on a one-cube start, where the tick is mass-blind), its rate is set to within 5% by four cubes, and it depends only on the per-tick angles: a one-split transient, not a clock.

## Derivation

Item 1 uses only the rule texts: the update law's half-ticks map the vacuum, the state with every negative-quasi-energy mode filled, to itself over a whole tick, and the actuality law selects configurations without acting on the odds. The response law's matter phase is then the actual share minus the vacuum share on the same edges at the same configuration, and these coincide whatever the configuration is. Item 2 is that a product of exponentials of one-body hops is number-conserving. Item 4 follows from item 3: particle-hole exchange maps the density-fluctuation operators d_i = n_i - 1/2 to -d_i, which keeps even moments and flips odd ones, and the count argument uses the turn symmetry of stage 0 under PH o R4.

## Checks

The runner ends with `TOTAL: PASS=10 FAIL=0` in about 2 s and under 150 MB.

Finite diagnostics (Gaussian pattern odds on the 3x2x2 patch; Bloch construction on 8^3 cubes, antiperiodic, unless stated):
- Total variation between the two stages: 4e-16 at M = 0 and 2.99e-3 at M = 0.5, so at least 2.5e-4 flips per site per half-tick; the real-space construction on a 4^3-cube torus agrees with the Bloch one to 1e-12.
- Total variation to stage 0 and to stage 1: particle-hole exchange, the fourfold turn and the yz mirror give 3e-3 and 6e-16; particle-hole times fourfold turn gives 4e-16 and 3e-3, the half turn 5e-16 and 3e-3.
- Even and odd statistics: d|C| = 2e-16, four-loop difference 1e-19; the third cumulant reaches 1.24e-4 in magnitude and its sum over the two stages is 6e-18.
- Counts: total variation 4e-16 for the 3x2x2 and 2x2x2 count distributions, against 3.0e-3 for the patterns.
- The density structure factor is the same at both stages and goes as q^2 (S = 3.01e-3, 1.18e-2, 4.33e-2 at q = pi/16, pi/8 and pi/4, log slope 1.97); max |C| falls from 2e-1 at one cell to 2e-4 at four cells.
- Size dependence: 1e-15 on the one-cube start; 5.22e-3, 3.58e-3, 3.12e-3, 2.99e-3 at 2, 3, 4 and 8 cubes across.
- Angle dependence: 5.88e-4 and 1.10e-3 at M = 0.05 and 0.1; 2.42e-3 and 1.23e-3 at eps = 0.3 and 0.15 with fixed ratios; 5.94e-3 at the halved birth angles (mu, M)/2.

Exact checks: the vacuum correlation matrix returns to itself after three ticks to 3e-15; the half-ticks are unitary within the runner's 1e-9 tolerance.

Stated, not computed: that every split cycle repeats the same N(t), so every level gets the same rate.

## Estimates against measurement

These are estimates with a supplied unit map (a = sqrt(8 pi) l_P, tau = 2a/(sqrt3 c)) and measured numbers, not theorems.
- The shuttle creates no modes, against at least about 1e80 measured, and gives baryon excess 0 against 6.1e-10.
- First escape, records conditioning the odds at the shuttle rate at about hbar/tau each: today's critical density allows at most 8e-181 such events per site-tick, 3e176 times below the forced rate, and no rule variable switches it off.
- Second escape, the response law reading the configuration itself: coarse cubes see nothing (item 4), the static q^2 noise gives a spectrum Delta^2 ~ q^5 (index n - 1 = 4), and the cell-scale noise is 1/4 per site today.

## Boundary

Supplied: the tick and its angles (b, mu, M) = (0.3, 0.4, 0.5) and the variants above, which are large-step model values; the negative-quasi-energy vacuum branch; antiperiodic and periodic tori; the 12-site patches and Gaussian pattern odds; the unit map and the measured numbers. Forced by the rule texts: zero response source from any configuration-only or record-only rule, and exact number conservation. Diagnostic only: the particle-hole shuttle structure, its rate and its size and angle dependence, on the patches and tori computed. Not claimed: a source of matter, of a baryon excess or of a clock; any statement at the register's small step eps0 beyond the linear scaling seen; the initial odds. Both escapes that would let the shuttle matter change a register law, and each misses a measured fact as estimated.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): unchanged.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's copy-massed tick and vacuum, the actuality law's transport, and the response law's vacuum standard. Zero premise weight; results are conditional on them.

## How to run

```
python3 scripts/no_configuration_or_record_rule_sources_the_response_and_the_copy_mass_sea_motion_is_a_particle_hole_shuttle_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120` with an internal alarm, runs in about 2 s, prints about 3.7 kB and ends with `TOTAL: PASS=10 FAIL=0`.
