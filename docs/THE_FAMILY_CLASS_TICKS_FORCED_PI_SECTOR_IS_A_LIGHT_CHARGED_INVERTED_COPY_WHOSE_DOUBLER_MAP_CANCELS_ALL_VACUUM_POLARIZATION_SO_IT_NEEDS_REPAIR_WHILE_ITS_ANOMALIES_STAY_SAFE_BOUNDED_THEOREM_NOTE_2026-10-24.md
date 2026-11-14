---
claim_id: the_family_class_ticks_forced_pi_sector_is_a_light_charged_inverted_copy_whose_doubler_map_cancels_all_vacuum_polarization_so_it_needs_repair_while_its_anomalies_stay_safe_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Free bands of FREEZE (the family-class tick representative, W_F = (-2,1,1); a supplied model with zero premise weight) on CL-1's 2x2x2 cell (CL-1: the source label for the supplied cube tick), with CL-1's plain tick (eps 0.3) as control, and cell-charge potentials as gauge probes. Exact: (1) the doubler S (S U(K) S^-1 = -U(K+R)) maps each no-Fermi-surface half-filled vacuum to its complement, S rho(K) S^+ = 1 - rho(K+R); (2) hence, for every S-even one-body probe (any cell-charge potential, any strength, any number of ticks, any uniform vector potential), the induced cell charge of the supplied interval-filling vacuum equals the infinite-temperature value, zero: no response to those probes; (3) zero-quasi-energy, zero-momentum states made of a 0-sector pair and a pi-sector pair exist at every momentum scale (kinematics only: the free filled vacuum is stationary under the tick, so its transition amplitude into them is zero, and no decay or rate follows without a defined interaction); (4) F_pi = W in every turn sector, robust under turn-symmetric deformations, so no free term gaps pi; (5) the one-cube start is degenerate and every no-Fermi-surface filling has at least one inverted boundary; (6) with the pi copy (2 x 16 per family) every gauge anomaly stays zero and the turn-anomaly N_f set is unchanged. Conditional comparator estimates with supplied numbers, not exclusions: IF a gauged completion carried the S-even cancellation to the electron loop and coupled the pi copies to the Z as the 0 copies, the hydrogen 2S Uehling term would vanish and N_nu would be 0 or 6, against the measured values; neither bridge is defined here. Not covered: a gauged FREEZE (link gauging is not defined), the identification of the cell-charge response with an electromagnetic or electroweak observable, interacting gapping of the pi sector, other members of the family class, decay rates."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_family_class_ticks_pi_partners_are_same_hand_spacetime_doublers_not_cpt_mirrors_so_the_mirror_cannot_be_carried_in_time_bounded_theorem_note_2026-10-24
  - a_circuit_slab_puts_its_mirror_in_the_other_copy_only_through_a_nonzero_turn_graded_winding_which_forces_equal_flow_at_quasi_energy_pi_and_is_set_by_termination_bounded_theorem_note_2026-10-23
  - a_family_class_tick_keeps_a_96_element_magnetic_group_that_forbids_every_low_energy_rotation_or_lorentz_violating_dispersion_term_below_dimension_six_and_leaves_its_time_reversal_breaking_in_one_chirality_flip_term_bounded_theorem_note_2026-10-24
runner: scripts/the_family_class_ticks_forced_pi_sector_is_a_light_charged_inverted_copy_whose_doubler_map_cancels_all_vacuum_polarization_so_it_needs_repair_while_its_anomalies_stay_safe_2026_10_24.py
---

# The family-class tick's forced pi sector is a light, charged, inverted copy whose doubler map cancels the free vacuum's response to every S-even one-body probe, while its anomalies stay zero

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers, [S] reading.
Primary runner: `scripts/the_family_class_ticks_forced_pi_sector_is_a_light_charged_inverted_copy_whose_doubler_map_cancels_all_vacuum_polarization_so_it_needs_repair_while_its_anomalies_stay_safe_2026_10_24.py`; cache `logs/runner-cache/the_family_class_ticks_forced_pi_sector_is_a_light_charged_inverted_copy_whose_doubler_map_cancels_all_vacuum_polarization_so_it_needs_repair_while_its_anomalies_stay_safe_2026_10_24.txt`. Axioms unchanged. No rule proposed or adopted. Criteria were
written before any code ran (criteria_pre_run.txt, a source-session file not in this repository). Every criterion came out as predicted. One code-level control
failed on the first run and was replaced; no claim changed. The light-only filling (2 of 8) was meant as a
non-complementary control, but it gave zero response. That is correct: V and S both preserve the light block, so the
theorem applies block by block. It was replaced by the both-nodes-normal filling, which is S-invariant and does respond.

Local labels (2026-11-14). "CL-1" is the source label for the supplied cube tick, "CL-2" the record rule as the source
notes state it, and "the register" those rules as the source notes state them; none is a clause of the current
[candidate-law register](CANDIDATE_LAWS.md), whose CL-1, CL-2 and CL-3 are historical aliases with zero premise weight.
The source notes called the family-class tick clause "adopted"; no owner adoption of it is recorded in the
repository, so it is treated here as a supplied candidate with zero premise weight. Short source names:
floquet-pi-slab is [#10064](A_CIRCUIT_SLAB_PUTS_ITS_MIRROR_IN_THE_OTHER_COPY_ONLY_THROUGH_A_NONZERO_TURN_GRADED_WINDING_WHICH_FORCES_EQUAL_FLOW_AT_QUASI_ENERGY_PI_AND_IS_SET_BY_TERMINATION_BOUNDED_THEOREM_NOTE_2026-10-23.md);
mirror-in-time (#10070) and t-breaking-tick-lowenergy are recorded only in the consolidation's source map
(historical reported results, unverified here).

Correction (2026-11-14, from the PR 10131 hold). The exact cancellation is for S-even one-body probes and the supplied
filling. A cell density response is not by itself an electromagnetic current-current tensor or an electroweak decay
observable, and link-gauged FREEZE is not defined. Section E is therefore a conditional comparator estimate, not an
exclusion, and B1 gives kinematics, not decay. This is not a claim that a completed gauged model would evade
measurement.

Question (check on the supplied family-class tick clause): mirror-in-time C4 read the forced pi sector as charged
and inverted, with possible vacuum instability. Is the pi sector a physical problem?

Repo first. A git grep of origin/main (docs, scripts) for "temporal doubler", "inverted sector", "quasi-energy pi" and
"Uehling" found nothing relevant. This note builds on and narrows:
- mirror-in-time (S, C1 alternation, C3 equal anomalies, C4 reading);
- floquet-pi-slab (F_0 = F_pi = W);
- t-breaking-tick-lowenergy (the kept group);
- the register's "cone partners at pi (charged, inverted inertia)" exclusion and the CL-2 text.

## A. What the vacuum sees (Q1)

- A1 [T]/[F]. S sends the no-Fermi-surface half filling (light eigenphases in (-pi, 0), plus one frozen eigenspace) to
  its complement: S rho(K) S^+ = 1 - rho(K + R). The residual is 6e-15.
- A2 [T]/[F]. The theorem.
  - In real space S is a staggered cell sign times an on-cell unitary. It commutes with any cell-charge potential V and
    with a uniform vector potential (the twisted grid).
  - So S U_V S^-1 = -U_V for U_V = e^{-i lam V} U. Then tr(rho(t) O) = tr((1 - rho)(t) O) for every S-even O, so
    <O> = tr(O)/2. This is the infinite-temperature value.
  - Checked on 4^3 cells (512 modes) with lam = 0.5, a random V and 24 ticks: the induced cell charge of BOTH vacua is
    at most 6e-14.
  - The FREEZE vacuum has ZERO response to cell-charge potentials and uniform vector potentials at every q and every
    order in the probe.
- A3 [F]. Controls.
  - CL-1's vacuum (gap at pi) screens (|dN| up to 3.3).
  - An S-odd on-cell layer makes FREEZE respond (0.32).
  - The both-nodes-normal FREEZE filling responds (1.2). It is S-invariant, and it pays for that with an inverted Fermi
    surface at theta = pi/2.
- A4 [S]. A reading, conditional on a gauged extension that is not defined here. The pi copy is a full second copy of
  every light Weyl: same hand, same cell charges, same dispersion. Pi-pi bilinears are slow and carry zero net
  momentum, so in a gauged extension they would couple to a low-energy photon and Z as 0-sector bilinears do. Because
  the copy is inverted, its response to S-even probes cancels the 0 copy's.

## B. Stability

- B1 [T]/[F]. The pi-sector dispersion equals the 0-sector dispersion (pi - theta(R + k) = theta(k), residual 2e-15).
  - States with exactly zero total quasi-energy and zero momentum (a 0 pair at +E and a pi pair at -E) exist at momentum
    scales 1e-1, 1e-2 and 1e-3.
  - So zero-quasi-energy multiparticle states are available in the IR at every scale. This is kinematics, not decay:
    the free filled vacuum is stationary under the tick (U rho U^+ = rho, B1b), so its amplitude into these states
    is zero. A rate needs an interaction that couples them, which is not defined here.
- B2 [T]/[F]. Control: CL-1's plain tick has w_max = 0.6, so any zero-quasi-energy vacuum transition needs at least
  6 particle-hole pairs, all at cell scale (prethermal). FREEZE needs 2.

## C. Filling (Q2)

- C1 [T]/[F]. In every turn sector, the axis flow through pi equals the winding, (-2, 1, 1). This stays exact under
  random turn-symmetric deformations. So no free term opens a pi gap in any family-class tick (all components of W are
  nonzero).
- C2 [T]. The one-cube start is degenerate.
  - A single FREEZE cell puts its 4 light modes exactly at 0 (periodic) or exactly at pi (antiperiodic), and its frozen
    4 modes at +-pi/2.
  - So no quasi-energy ordering picks a filling, and no CL-2 clause (as the source notes state CL-2) does either.
- C3 [T]. Alternation (exhaustive over 4096 fillings on the axis loop). Rises equal drops, and there is at least one.
  Every no-Fermi-surface filling has at least one inverted light sector; the minimum is one.
- C4 [S]. What CL-2 does.
  - CL-2 defines no ground state. The actual configuration follows the odds, and a free Slater state of Floquet
    eigenvectors is stationary, so the transport stays.
  - The filling is the one the start and the splits carry.
  - CL-2 cannot choose a normal-normal vacuum, because none without a Fermi surface exists.
- The convention-independent statements are these: F_0 = F_pi = W; the complement map S; vacuum response = the
  infinite-temperature value; and the count of at least one inverted boundary. The branch-cut choice only decides WHICH
  sector is inverted.

## D. Anomaly (Q3)

- D1 [T]. With the pi copy each family has 2 x 16 (counting the pi copy of the light near wall and of the far-wall
  mirror separately).
  - Y^3, Y-grav, SU2^2 Y, SU3^2 Y and SU3^3 are all 0. The doublet count is even, and the Weyl count is 0 mod 16.
  - The turn coefficients double. 2 is a unit mod 3 and mod 9, so the allowed N_f set is unchanged (N_f = 0 mod 3
    stays).
  - Anomaly: SAFE.
- D2 [S]. The far-wall gapping must also gap the mirror's pi copy, which is light, charged and S-related. An S-even
  far-wall term would do so at the same coupling. Not computed.

## E. Conditional comparator estimates (not exclusions)

Missing bridges: a gauged FREEZE, the identification of the cell-charge response with the photon vacuum
polarization, and of the pi copies with Z decay channels. The runner prints these lines as not counted.
- E1 [E]. IF the S-even cancellation carried over to the electron loop of a gauged completion, the hydrogen 2S Uehling
  term would vanish. Its size is -27.13 MHz, while theory and the measured Lamb shift agree at about 0.01 MHz
  (supplied), a factor of about 2700.
- E2 [E]. IF the pi neutrino copies coupled to the Z as the 0 copies do, inverted pi neutrinos would give N_nu -> 0 and
  normal-filled copies 6, against the measured 2.984 +- 0.008 (373 and 377 sigma).
- E3 [S]. With an interaction and a light photon, B1's states would be open final states with phase space up to the
  cell scale. Under the free tick nothing decays (B1b), and no rate is computed here.

## Verdict (narrowed 2026-11-14)

Exact, for the supplied family-class tick taken with FREEZE's free bands: its forced pi sector is light, carries the
same cell charges and is inverted, and the exact doubler S makes the vacuum's response to every S-even one-body
probe cancel (zero). Anomalies stay zero with the pi copy. Conditional: if a gauged completion carried this
cancellation to the photon and Z couplings, the comparator estimates of section E would conflict with the Lamb shift
and the Z width. No observable or rate conclusion is drawn here, and none is claimed for a completed gauged model.

If a repair is wanted, two routes remain open.
- (a) A family-class tick (W unchanged) that breaks S and leaves no light node at pi. F_pi = W forbids a free gap, but
  it does not forbid the band passing pi with constant occupation away from nodes. Whether any member of the class does
  this is untested, and so is C3's count outside FREEZE.
- (b) An interaction that gaps the pi copies (near wall and far wall) but not the 0 copies. It must be S-odd or act
  through the filling's own S-breaking. This is the same class of open problem as far-wall symmetric mass generation.

Test for any repair, with this runner's A2 probe: the vacuum should respond to S-even probes as CL-1's does.

## Gate

No rule is proposed. A repair rule would have to pass the anti-smuggling gate: choosing "gap the pi sector" by name
would insert structure, so it must come from site, neighbour or update conditions.

## Smuggling review

Supplied:
- FREEZE as the class representative;
- CL-1's tick at eps 0.3;
- the interval-filling vacuum class;
- cell-charge potentials as the probe (link-gauged FREEZE is not defined, and the probe is not an identified
  electromagnetic or electroweak observable);
- the 16's SM charges;
- the Uehling formula, the Lamb-shift agreement scale and N_nu (literature, labelled [E], used only in conditional
  estimates).

Forced:
- S and the complement map;
- zero response;
- the IR zero-quasi-energy states (kinematics) and the stationarity of the free vacuum;
- F_pi = W robustness;
- the degenerate start;
- alternation;
- the anomaly doubling.

Not shown:
- interacting pi gapping;
- other family-class ticks;
- decay rates and any interaction that would produce them;
- a gauged FREEZE and the observable identifications of section E;
- the far-wall pi copy gapping.
