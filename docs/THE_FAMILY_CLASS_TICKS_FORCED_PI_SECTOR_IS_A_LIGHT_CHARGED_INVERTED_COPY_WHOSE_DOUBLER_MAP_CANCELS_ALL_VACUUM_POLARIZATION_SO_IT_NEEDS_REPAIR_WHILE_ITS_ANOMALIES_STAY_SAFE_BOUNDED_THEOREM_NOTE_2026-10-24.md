---
claim_id: the_family_class_ticks_forced_pi_sector_is_a_light_charged_inverted_copy_whose_doubler_map_cancels_all_vacuum_polarization_so_it_needs_repair_while_its_anomalies_stay_safe_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Free bands of FREEZE (the family-class tick representative, W_F = (-2,1,1)) on CL-1's 2x2x2 cell, with CL-1's plain tick (eps 0.3) as control, and cell-charge potentials as gauge probes. Exact: (1) the doubler S (S U(K) S^-1 = -U(K+R)) maps each no-Fermi-surface half-filled vacuum to its complement, S rho(K) S^+ = 1 - rho(K+R); (2) hence, for every S-even one-body probe (any cell-charge potential, any strength, any number of ticks, any uniform vector potential), the vacuum's induced charge equals the infinite-temperature value, zero: no vacuum polarization; (3) zero-quasi-energy, zero-momentum states made of a 0-sector pair and a pi-sector pair exist at every momentum scale; (4) F_pi = W in every turn sector, robust under turn-symmetric deformations, so no free term gaps pi; (5) the one-cube start is degenerate and every no-Fermi-surface filling has at least one inverted boundary; (6) with the pi copy (2 x 16 per family) every gauge anomaly stays zero and the turn-anomaly N_f set is unchanged. Estimates with supplied numbers: Lamb shift (Uehling) and Z invisible width exclude the free pi sector. Not covered: interacting gapping of the pi sector, link-gauged FREEZE beyond cell-charge potentials, other members of the family class, decay rates."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_family_class_ticks_pi_partners_are_same_hand_spacetime_doublers_not_cpt_mirrors_so_the_mirror_cannot_be_carried_in_time_bounded_theorem_note_2026-10-24
  - a_circuit_slab_puts_its_mirror_in_the_other_copy_only_through_a_nonzero_turn_graded_winding_which_forces_equal_flow_at_quasi_energy_pi_and_is_set_by_termination_bounded_theorem_note_2026-10-23
  - a_family_class_tick_keeps_a_96_element_magnetic_group_that_forbids_every_low_energy_rotation_or_lorentz_violating_dispersion_term_below_dimension_six_and_leaves_its_time_reversal_breaking_in_one_chirality_flip_term_bounded_theorem_note_2026-10-24
runner: scripts/the_family_class_ticks_forced_pi_sector_is_a_light_charged_inverted_copy_whose_doubler_map_cancels_all_vacuum_polarization_so_it_needs_repair_while_its_anomalies_stay_safe_2026_10_24.py
---

# The family-class tick's forced pi sector is a light, charged, inverted copy whose doubler map cancels all vacuum polarization, so it needs repair while its anomalies stay safe

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers, [S] reading.
Runner: runner.py, TOTAL: PASS=11 FAIL=0, 1.7 s, 115 MB peak, 5.3 k characters, seeded, AUDIT_TIMEOUT_SEC = 120. It was
tested under a unique filename (scratch/pss_test_run.py). Axioms unchanged. No rule proposed or adopted. Criteria were
written before any code ran (criteria_pre_run.txt). Every criterion came out as predicted. One code-level control
failed on the first run and was replaced; no claim changed. The light-only filling (2 of 8) was meant as a
non-complementary control, but it gave zero response. That is correct: V and S both preserve the light block, so the
theorem applies block by block. It was replaced by the both-nodes-normal filling, which is S-invariant and does respond.

Question (urgent check on the adopted Family-class tick clause): mirror-in-time C4 read the forced pi sector as charged
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
  - The FREEZE vacuum has ZERO vacuum polarization at every q and every order in the probe.
- A3 [F]. Controls.
  - CL-1's vacuum (gap at pi) screens (|dN| up to 3.3).
  - An S-odd on-cell layer makes FREEZE respond (0.32).
  - The both-nodes-normal FREEZE filling responds (1.2). It is S-invariant, and it pays for that with an inverted Fermi
    surface at theta = pi/2.
- A4 [S]. The physical reading. The pi copy is a full second copy of every light Weyl: same hand, same charges, same
  dispersion. Pi-pi bilinears are slow and carry zero net momentum, so they couple to the low-energy photon and Z
  exactly as 0-sector bilinears do. Because the copy is inverted, it anti-screens exactly as much as the 0 copy screens.

## B. Stability

- B1 [T]/[F]. The pi-sector dispersion equals the 0-sector dispersion (pi - theta(R + k) = theta(k), residual 2e-15).
  - States with exactly zero total quasi-energy and zero momentum (a 0 pair at +E and a pi pair at -E) exist at momentum
    scales 1e-1, 1e-2 and 1e-3.
  - So the vacuum -> pair + pair channel is open in the IR at every scale. It is not only a Planck-scale effect.
- B2 [T]/[F]. Control: CL-1's plain tick has w_max = 0.6, so any zero-quasi-energy vacuum transition needs at least
  6 particle-hole pairs, all at cell scale (prethermal). FREEZE needs 2.

## C. Filling (Q2)

- C1 [T]/[F]. In every turn sector, the axis flow through pi equals the winding, (-2, 1, 1). This stays exact under
  random turn-symmetric deformations. So no free term opens a pi gap in any family-class tick (all components of W are
  nonzero).
- C2 [T]. The one-cube start is degenerate.
  - A single FREEZE cell puts its 4 light modes exactly at 0 (periodic) or exactly at pi (antiperiodic), and its frozen
    4 modes at +-pi/2.
  - So no quasi-energy ordering picks a filling, and no CL-2 clause does either.
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

## E. Against measurement

- E1 [E]. With S intact, the electron loop cancels against its inverted pi copy, so the hydrogen 2S Uehling term
  vanishes. Its size is -27.13 MHz, while theory and the measured Lamb shift agree at about 0.01 MHz (supplied).
  EXCLUDED by a factor of about 2700.
- E2 [E]. Z invisible width. Inverted pi neutrinos give N_nu -> 0, and normal-filled copies would give 6. The measured
  2.984 +- 0.008 excludes both (373 and 377 sigma).
- E3 [S]. Exothermic pi-pair production in every process, with phase space up to the cell scale. The free sector is
  excluded before any rate is computed.

## Verdict: NEEDS REPAIR (not FATAL; anomaly SAFE)

The adopted family-class tick, taken with FREEZE's free bands, is excluded as it stands. Its forced pi sector is light,
charged and inverted, and the exact doubler S makes its gauge response cancel the light sector's. That contradicts the
Lamb shift and the Z width, and the vacuum is unstable in the IR.

It is not shown FATAL, because two repair routes remain open.
- (a) A family-class tick (W unchanged) that breaks S and leaves no light node at pi. F_pi = W forbids a free gap, but
  it does not forbid the band passing pi with constant occupation away from nodes. Whether any member of the class does
  this is untested, and so is C3's count outside FREEZE.
- (b) An interaction that gaps the pi copies (near wall and far wall) but not the 0 copies. It must be S-odd or act
  through the filling's own S-breaking. This is the same class of open problem as far-wall symmetric mass generation.

Required of any repair, testable with this runner's A2 probe: the vacuum must screen like CL-1's.

## Gate

No rule is proposed. A repair rule would have to pass the anti-smuggling gate: choosing "gap the pi sector" by name
would insert structure, so it must come from site, neighbour or update conditions.

## Smuggling review

Supplied:
- FREEZE as the class representative;
- CL-1's tick at eps 0.3;
- the interval-filling vacuum class;
- cell-charge potentials as the gauge probe (link-gauged FREEZE is not defined);
- the 16's SM charges;
- the Uehling formula, the Lamb-shift agreement scale and N_nu (literature, labelled [E]).

Forced:
- S and the complement map;
- zero response;
- the IR zero-quasi-energy states;
- F_pi = W robustness;
- the degenerate start;
- alternation;
- the anomaly doubling.

Not shown:
- interacting pi gapping;
- other family-class ticks;
- decay rates;
- the far-wall pi copy gapping.
