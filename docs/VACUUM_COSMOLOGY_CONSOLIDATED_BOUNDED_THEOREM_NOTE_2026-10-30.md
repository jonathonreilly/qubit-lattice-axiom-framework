---
claim_id: vacuum_cosmology_consolidated_bounded_theorem_note_2026-10-30
claim_type: bounded_theorem
claim_scope: "Consolidation of 28 source notes on one question: Can the proposed vacuum and split rules produce a viable cosmological history with inflation, dark matter and a small cosmological constant? Each result carries its own scope below; nothing here is stronger than its source."
---

# Vacuum, cosmology and dark matter: consolidated results

**Question.** Can the proposed vacuum and split rules produce a viable cosmological history with inflation, dark matter and a small cosmological constant?

**Status authority.** Independent audit lane only. These are author statements for review.

## What this theme found

# Synthesis: vacuum, cosmology and dark matter

Within the supplied models tested, no. Every result is conditional on the update, actuality and response laws as each note supplies them; none is a result about the register in `ref/`.

**Cosmological constant.** The supplied half-filled sea sources zero, a Planck-scale value, or a mass-dominated value, never the measured density (#9880). A fixed 4-volume per record cancels every vacuum term proportional to 4-volume on the supplied frustum carrier but leaves Lambda to initial data, lost matter energy and split kicks (#9900). A first-slab rule gives a closed-top minimum 1e117 to 1e119 above the measured value and, with a transparent top, a free size; record-multiplier rules give the wrong sign or a drift (#10002). Records on change are frozen in the tested half-filled seas (#9876, #10018), and Sorkin-type histories fail early bounds (#10018).

**Inflation and perturbations.** Exponential plateaus give n_s = 1 - 2/N (power plateaus differ), and supplied curvature-squared inflation with the rules' reheating gives 0.9617, an estimated 4.1 sigma below ACT (#9918). A supplied 2D toy's cascade is self-similar, and under the stationary-shift read lapse the trigger gives no linear split-time fluctuation (#9961). The update's own Dirac sea gives a fast fold (#9979). An unsplit block cannot inflate; a nested-sea plateau needs order-carrying splits, gives n_s = 0.957 at a self-consistent N* with a fitted rung and supplied repulsion, and the passing seeds nothing (#10000). Born split times are white inherited offsets and supply no seed (#10007).

**Dark matter.** A census stated, not computed, leaves only a supplied label parity and magnetic charge (not dark) as stabilisers of a massive relic (#9946); none of the four places searched in the update's existing structure protects a dark species (#10005, with the mirror group input from #9988). No abundance is set by the rules.

**Open.** Records for the copy-massed tick (a patch computation finds motion, #9923, logged); a rule that supplies dephasing or a horizon-correlated seed; a conserved number for a dark species; the size of Lambda.

## Results carried with their runners

# Kept results: vacuum, cosmology and dark matter

Each section below carries the source note's own text at the recorded INDEX head. The claim scope is copied exactly from the note. The statement and supporting text are copied line for line from the note; omitted line ranges are listed in each section (derivation prose, run instructions, and in some sections a note's own pass/fail checklist for candidate rules, which is replaced by a plain description). Headings in copied text are demoted two levels. In the copied text, CL-1, CL-2 and CL-3 are the notes' shorthand for an update law, an actuality law and a response law; they are not the aliases defined in `docs/CANDIDATE_LAWS.md` (see CORRECTIONS). All statements are about supplied models, not about the physical vacuum or measured Lambda.

Count: 13 of the theme's 28 PRs are kept, above a third (9). The ones beyond that are #9876 and #9988, which kept results rely on for a computation they do not rerun (the 3D antiunitary instance for #10018; the mirror group input for #10005); #9946, the only source of the label-parity survivor; #10007, which corrects #10000; and #9979, the stiffness theorem the fold chain imports. Their loss would remove an input that another kept result takes from the branch, not a routine negative.

### #9876: Time reversal freezes half-filled-sea records, and a record-count Lambda needs Poisson input

- Branch `claude/toe-records-causal-set-20261021`, head `9d4172159e`; note `docs/TIME_REVERSAL_FREEZES_HALF_FILLED_SEA_RECORDS_AND_RECORD_COUNT_LAMBDA_NEEDS_POISSON_INPUT_BOUNDED_THEOREM_NOTE_2026-10-21.md`.
- Runner: [`scripts/time_reversal_freezes_half_filled_sea_records_and_record_count_lambda_needs_poisson_input_2026_10_21.py`](../scripts/time_reversal_freezes_half_filled_sea_records_and_record_count_lambda_needs_poisson_input_2026_10_21.py); cache `logs/runner-cache/time_reversal_freezes_half_filled_sea_records_and_record_count_lambda_needs_poisson_input_2026_10_21.txt`.
- Kind of statement: Mixed. An exact antiunitary statement checked on a 12-site 1D pair walk (924 configurations) and on the supplied 3D block tick on an 8^3 torus; finite diagnostics for the Fano factors, area-law variance and past-cone counts; estimates against the measured Lambda, including a Sorkin-type comparison; all for supplied models.
- Dependencies: Supplied pair walk, 3D spin-3/2 block tick at (mu, b) = (0.4, 0.3), half-filled sea, volume = record count, unit map and LambdaCDM. PR 10018 relies on its 3D block-tick instance of the antiunitary (8^3 torus, entry error 1.9e-14) and on its statement that a Poisson count must be imported; PR 10002 builds on it. PR 10018 computes the prefactor under a different convention, so the magnitude statements differ (CORRECTIONS item 2). The tick has no copy mass (CORRECTIONS item 3).

Claim scope (verbatim):

> For a supplied half-filled Floquet sea of the supplied 1D pair walk and the supplied 3D spin-3/2 block tick, a site-diagonal antiunitary that reverses both half-ticks makes the odds equal at both half-ticks, so the record-formation rule moves nothing and vacuum records are frozen; in these models record counts are not Poisson (window-dependent Fano factor, area-law variance, past-cone variance growing as R^3). Under the supplied identification volume = record count, the unimodular estimate of Lambda depends on the Fano factor; Poisson counting at the rule density gives an estimate within a factor 10 of measured, the frozen sea does not, and a Sorkin-type Lambda is compared with measured w as an estimate. No vacuum, volume rule, causal-set structure or value of Lambda is established.

Statement and supporting text (copied from the note):

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. This note asks whether reading 4-volume as the number of records, as in causal-set estimates of the cosmological constant, works with the register's record-formation rule. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used, and main chooses no vacuum, so the half-filled sea is supplied.

#### The unimodular estimate and the Fano factor

The vacuum energy density rho_L is conjugate to the 4-volume V, and a minimum-uncertainty packet has delta rho_L delta V = hbar/2 (runner value 0.50000000). Write V = v0 N with Var N = F <N>, where F is the Fano factor. The uncertainty reading gives rho_L ~ hbar / sqrt(F v0 V). The classical-sum reading Lambda = S/V gives rho_L ~ hbar sqrt(F) / sqrt(v0 V). The two agree only at F = 1 and move apart by the factor F otherwise. With the rules' element v0 = a^3 tau = 729.4 Planck 4-volumes per record, rho_L/rho_P = 1/sqrt(F kappa V_P) with kappa = 729.4. Counting cells instead overestimates by the factor kappa.

#### Theorem: the half-filled sea is frozen

Suppose a site-diagonal antiunitary reverses both half-ticks. Then the Floquet sea has the same odds at both half-ticks, and the rule that the record set changes as little as possible moves nothing, whatever the tie-break. Every vacuum record is then frozen.

- 1D pair walk (L = 12, 924 configurations): the pair unitaries are symmetric, so U_e U_o = (U_o U_e)^T. The odds at the two half-ticks differ in total variation by 1.1e-15, the stay probability is 1, and the autocorrelation at 256 half-ticks is 1.000. Each pair's occupation is conserved, so the rule splits into independent groups, and both tie-breaks keep the odds.
- Control: a ring flux breaks the antiunitary. The odds then change (total variation 0.074, stay 0.926) and the autocorrelation at 256 half-ticks falls to 0.24.
- 3D spin-3/2 block tick with a gapped half-filled sea (mu = 0.4, b = 0.3, 4 of 8 bands filled): all hop holonomies are real with faces -1, and the antiunitary is solved to a maximum entry error of 1.9e-14 on the 8^3 torus. The |C|^2 differ by 1.1e-16 and the 4x4 minors by 8.3e-17, so the 3D vacuum records are frozen too.

#### Records are not Poisson in these models

- 1D Fano factors depend on the window: 1.00 (2x2), 0.36 (6x2), 256.75 (2x512), 91.47 (6x512) for the frozen sea, and similarly for the moving control.
- 1+1D past-cone diamond: Var grows as T^1.036 while the mean grows as T^2; the Fano factor at T = 128 is 0.0179.
- 3D equal-time cube of side l: Var = 0.50 l^2, an area law (8.00 at l = 4 against 16 for independent sites, 50.32 at l = 10 against 250).
- 3D past cone: Var ~ R^3.10 with Var/R^3 = 1.063 while the mean grows as R^4, so delta N ~ V^(3/8). The Fano factor falls from 0.159 to 0.085.

#### Estimates against measured Lambda

Measured rho_L = 1.133e-123 rho_P. The past light-cone 4-volume today is 0.1230 H0^-4 = 6.39e242 Planck units.

- If records were Poisson (F = 1) at the rule density, rho_L = 1.46e-123 rho_P, 1.29 times measured. The factor depends on conventions and spans roughly 0.2 to 10.
- For the frozen sea, delta N = 1.0e90 against sqrt(N) = 9.4e119. The uncertainty reading gives 1.3e-93 rho_P, about 1e31 too large, and the classical-sum reading gives 1.6e-153 rho_P, about 1e-31 too small.
- Counting matter relays per half-tick gives N = 3.6e148 in the past cone and rho_L = 3.0e-169 rho_P.
- In an empty vacuum there are no records, so the volume-count rule would give voids no volume.

A Sorkin-type Lambda (S/V random walk over nested past cones, Poisson reading) tracks the critical density, with standard deviation of Omega_L 2.54 at BBN, 1.94 at recombination and 0.88 today. At coefficient 1, histories matching today give w_eff(z = 0.5) = -0.28 [-1.22, +0.28], and the sampled fraction with w within 2 sigma of the measured -1.03 +- 0.03 is 0.000. Adding BBN and recombination, the best factorised probability over coefficients 0.1 to 3 is 2.0e-11. These are estimates against approximate bounds.

#### Checks

The runner prints `TOTAL: PASS=19 FAIL=0`. Its PASS lines cover the conjugacy bound, the Fano dependence of the two readings, the element normalisation, the 1D and 3D antiunitary theorems and frozen odds, the flux control, the non-Poisson window, diamond, cube and past-cone counts, the three normalisations of the Lambda estimate, and the three measured-constraint comparisons.

#### Supplied and boundary

Supplied: the 1D pair walk and its masses, mu and b, the half-filled sea, the tie-breaks (shown not to matter), the unit map a = sqrt(8 pi) l_P with tau = 2a/(sqrt(3) c), the volume-count identification, the S/V dynamics, the LCDM background and the bounds used. A Poisson sprinkling would be imported from causal-set theory, not derived from the odds, and the uncertainty reading needs V in superposition while records are definite. No vacuum, volume rule, causal-set structure or value of Lambda is established.

[end of lines 16-54 of the note]

(Omitted from the note: lines 1-15 and lines 55-55.)

### #9880: Floquet-sea vacuum source: zero, Planckian or mass-dominated, not the measured Lambda

- Branch `claude/toe-lambda-20261021`, head `5dee2371d5`; note `docs/FLOQUET_SEA_VACUUM_SOURCE_IS_ZERO_PLANCKIAN_OR_MASS_DOMINATED_NOT_MEASURED_LAMBDA_BOUNDED_THEOREM_NOTE_2026-10-21.md`.
- Runner: [`scripts/floquet_sea_vacuum_source_is_zero_planckian_or_mass_dominated_not_measured_lambda_2026_10_21.py`](../scripts/floquet_sea_vacuum_source_is_zero_planckian_or_mass_dominated_not_measured_lambda_2026_10_21.py); cache `logs/runner-cache/floquet_sea_vacuum_source_is_zero_planckian_or_mass_dominated_not_measured_lambda_2026_10_21.txt`.
- Kind of statement: Mixed. Exact identities and sum rules for the supplied block tick (determinant, sea phase at mu = 0, spectral symmetry); finite numerical diagnostics (Hellmann-Feynman residual, zone-dependent pressure, toy-model shifts); results that hold only inside supplied rules (the Hartree condensate rule, the one-block model, the counter-rotating variant); unit-mapped comparisons with the measured vacuum density are estimates. Everything depends on the supplied block tick and the supplied half-filled sea.
- Dependencies: Supplied block tick and half-filled sea. The note says its source law (a geometry law sourcing curvature by the generator i log U of the tick) is taken from the candidate-law register it cites; that law is not stated in `docs/CANDIDATE_LAWS.md`, so the result is conditional on it as the note supplies it. No other PR is cited. Later notes in this theme (9900, 9962, 10002, 10018) treat the vacuum sea as supplied in the same way.

Claim scope (verbatim):

> For the supplied block tick and supplied half-filled sea: det U(K) = 1 so the 8 quasi-energies sum to 0; at mu = 0 the sea phase is exactly -2 pi per block per tick, which is 0 mod 2 pi but -pi/4 per site under the generator reading; mass leaves a residual -I0 mu^2 per block, a supplied Hartree condensate rule leaves -(a/16) mu^4 ln(1/mu) per site, a supplied one-block model's vacuum is undressed, a supplied counter-rotating variant shifts it by -(g^2/2) cot(Delta/2) with a balanced-channel sum rule, and the sea's pressure depends on the zone cut. Unit-mapped values and record-noise wander are compared with measured rho_Lambda as estimates. No vacuum, log branch, unimodular reading or value of Lambda is established.

Statement and supporting text (copied from the note):

#### Sum rules and the sea phase

Write the block hop as W(mu) = e^{i mu/2} exp(i(pi - mu) P_-) with rank P_- = 4. Then det U(K) = 1 at every K, so the 8 quasi-energies sum to 0. This cancels only the all-empty and all-full fillings. The spectrum is symmetric under w -> -w with 4 bands of each sign at every K (checked at mu = 0.37).

At mu = 0 the shift K -> K + pi(1,1,1) maps |w| to pi - |w|, so the filled bands of each such pair sum to -4 pi (maximum deviation 5.3e-15). The sea phase is -2 pi per block per tick (runner value -6.283185307180). Read mod 2 pi it is 0, and the vacuum odds return each tick. Read through the generator it is -pi/4 per site per tick. The register does not choose between these readings.

#### Mass, condensate and dressing

- Floquet Hellmann-Feynman: dE_sea/dmu = -<B> per block per tick, to 2.2e-9. The residual is E_sea(mu) + 2 pi = -I0 mu^2 (1 + O(mu^2 ln mu)) with I0 = 1.1567154153; at mu = 0.05, 0.1 and 0.2 the residuals are -2.8865e-3, -1.1517e-2 and -4.5680e-2 against -I0 mu^2 = -2.8918e-3, -1.1567e-2 and -4.6269e-2.
- Supplied Hartree condensate rule: at the gap root the mu^2 term cancels and leaves -(a/16) mu^4 ln(1/mu) + O(mu^4) per site, with a = 3 sqrt(3)/(2 pi^2). The integration-by-parts check gives -2.500315e-4.
- Supplied one-block model with coupling a+ b+ c + h.c.: it conserves a number, so the empty state is an exact Floquet eigenstate with phase 0. The dressed vacuum is the bare vacuum and its Born-mean source is exactly 0.
- Supplied counter-rotating variant a+ b+ c+ + h.c.: the dressed vacuum's quasi-energy is -(g^2/2) cot(Delta/2) + O(g^4), with Delta the quasi-energy of the state it couples to. With the rotating coupling off the formula matches to 2.5e-4. It vanishes at Delta = pi and flips sign above.
- Floquet sum rule: channels at Delta and 2 pi - Delta cancel the shift. In the balanced toy the shift is -2.2e-16 at g = 0.02 and -1.4e-16 at g = 0.3, against -2.9227e-4 for one channel.

#### The vacuum equation of state is not fixed

At mu = 0 the sea's kinetic stress depends on where the momentum zone is cut. The zones [-pi, pi) and [0, 2 pi) give p = -1.4936 and +1.4936 per block with rho = -6.2832, so w = p/rho = +0.2377 or -0.2377. Neither gives w = -1.

#### Estimates against measured Lambda

With a = sqrt(8 pi) l_P and tau = 2a/(sqrt(3) c), the measured value (Planck 2018, Omega_L = 0.6847 +- 0.0073, H0 = 67.4 +- 0.5) is rho_L = 5.251e-10 J/m^3 = 1.133e-123 rho_P, nonzero at more than 90 sigma.

| source | rho / rho_P | ratio to measured |
|---|---|---|
| massless sea, generator reading | 1.08e-3 | 9.5e119 |
| massless sea, phase mod 2 pi | 0 | excluded |
| relays counted relative to the sea | 0 | excluded |
| fixed mass, electron | 1.16e-47 | 1.0e76 |
| fixed mass, top | 1.33e-36 | 1.2e87 |
| condensate, electron | 3.87e-90 | 3.4e33 |
| condensate, top | 3.76e-68 | 3.3e55 |
| condensate, 50 meV neutrino | 4.70e-118 | 4.1e5 |

If gravity is unimodular and each relay forms one record per half-tick with independent zero-mean jumps, the rms wander over the Hubble volume after 13.8 Gyr (2.8e60 half-ticks) is 1.6e-139, 4.2e-137 and 8.2e-134 rho_P for relic neutrinos, electrons and baryons. Only Planck-size jumps reach the measured scale, and they overshoot at 2.1e-110. A Sorkin-type scaling rho_P/sqrt(N) over the Hubble 4-volume, which is not in the register, gives 1.9e-121 rho_P counted in cells and 6.9e-123 counted in Planck 4-volumes. It needs cell-count fluctuations that a regular lattice lacks.

[end of lines 18-51 of the note]

#### Supplied and boundary

Supplied: the block hop and mass parameter, the sea filling, the log branch, the one-block couplings (the counter-rotating term is a variant), the condensate rule and Hartree approximation, the unit map, the unimodular reading, the jump sizes and the particle densities. Counting relays relative to the sea sets the vacuum to zero by construction. Measured comparisons are estimates. No vacuum, log branch, unimodular reading or value of Lambda is established.

[end of lines 57-59 of the note]

(Omitted from the note: lines 52-56, 60-60 and lines 1-17, i.e. front matter, derivation prose, run instructions and any candidate-rule checklist.)

### #9900: Fixed 4-volume per record cancels vacuum energy and leaves Lambda as history

- Branch `claude/toe-lambda-split-20261021`, head `880e28d1a8`; note `docs/FIXED_FOUR_VOLUME_PER_RECORD_CANCELS_VACUUM_ENERGY_AND_LEAVES_LAMBDA_AS_HISTORY_BOUNDED_THEOREM_NOTE_2026-10-21.md`.
- Runner: [`scripts/fixed_four_volume_per_record_cancels_vacuum_energy_and_leaves_lambda_as_history_2026_10_21.py`](../scripts/fixed_four_volume_per_record_cancels_vacuum_energy_and_leaves_lambda_as_history_2026_10_21.py); cache `logs/runner-cache/fixed_four_volume_per_record_cancels_vacuum_energy_and_leaves_lambda_as_history_2026_10_21.txt`.
- Kind of statement: Finite numerical diagnostics (19 checks) of supplied models on a cubic-frustum Regge expansion carrier, with short derivations; comparisons with measurement are estimates; the negative statement is about the tested rules only.
- Dependencies: Supplied cubic-frustum carrier, split construction, corner-preserving split map and the fixed-4-volume-per-record rule. Later notes in this theme (9962, 9990, 10002) describe the fixed-4-volume-per-record clause as dropped from the laws; this result is therefore a statement about that clause on that carrier. PR 9902 (assigned to gravity-edge-registers) corrects the carrier: its cubic-frustum Friedmann law matches Friedmann only to first order in rho/rho* and has no bounce (see CORRECTIONS). Cited by 9962 and 10002.

Claim scope (verbatim):

> On a supplied cubic-frustum Regge expansion carrier, varying edge lengths at fixed 4-volume per record cancels every vacuum term proportional to 4-volume and conserves a constant Lambda set only by initial data, lost matter energy and a kick rho^2/rho* per synchronous 2^3 split; supplied per-new-cell phase and split-trigger self-tuning rules either track the critical density, freeze the start or need the size by hand; no rule fixing the size of Lambda is established.

Statement and supporting text (copied from the note):

#### Statement

1. On the supplied cubic-frustum Regge carrier, the fixed-4-volume rule cancels every vacuum term -rho_v V from the edge equation exactly.
2. Under that rule a constant Lambda is conserved with no secular drift, and the late expansion obeys Friedmann with it, so w = -1.
3. Its value is Lambda_0 plus the matter energy lost along the way plus rho^2/rho* for each synchronous 2^3 split of dust, with rho* = 3/(4 pi G a^2) the lattice's maximal density. Lambda_0 is set by the first slab, so the size is history, not a consequence of the rules.
4. A phase per new cell gives a constant of unfixed size plus a zero-mean term that tracks the critical density. Self-tuning through the split trigger tracks, freezes the starting value, or needs the measured size put in by hand.

[end of lines 18-23 of the note]

Fixed 4-volume. At fixed V_n the variation of rho_v V vanishes, so a vacuum term proportional to 4-volume drops out of the edge equation. This removes the 4-volume parts of the vacuum sea and of any constant residual. It does not remove the sea's shear response. The integration constant of the remaining equations is a conserved Lambda, fixed by the first slab's mismatch. Matter non-conservation enters as Lambda = Lambda_0 + int Q dt. The split junction's one-slab residual of order (H l)^2 becomes a permanent kick rho^2/rho* per split. Fixing only the cell count is not enough: through the split trigger the record count follows the expansion, so on large scales a per-record phase still acts as a gravitating Lambda.

[end of lines 27-27 of the note]

#### Checks

The runner gives 19 PASS and 0 FAIL. These are finite diagnostics of supplied models.

- Vacuum cancellation to 3e-16 relative, for rho_v from 1e4 to 1e7 Lambda_0.
- No drift: |Lbar_n - Lambda_0| <= 4.2 c^2 rho_c(n) at every slab (3.92, 4.06, 4.13 at relative steps c = 0.02, 0.01, 0.005), though rho_c starts at 1e4 Lambda_0. Late (3H^2 - rho_r)/Lbar is 1.00008, 1.00001, 0.99999.
- Initial data: a 1e-7 change of the second edge length moves Lambda by 20% (1.2030 at the first slab, 1.2034 late).
- Lost energy: radiation losing 1% at one slab raises Lambda by the lost density (ratios 1.00078, 1.00017, 1.00004), with later drift at most 0.14 c^2.
- Split kick: ratio to rho^2/rho* from 0.9974 to 0.9991 in five setups, independent of step.
- Per-new-cell phases: slope -0.490 and mean 0.2980 against m = 0.3. Independent split phases have Fano factor 35.3 times the ticks per split (35.17 to 35.28 against 35.29 analytic).
- Self-tuning: lam = 0 gives Omega at BBN of 3.42; lam = 1 gives a ratio of 1.0667 between today's and the first value. Fixed points lie in [3.9e-3, 2.6e2]. Cancelling the junction residual with a vacuum term needs rho_v/rho_c of -1.014, -1.013, -1.027 at H l = 0.091, 0.046, 0.023, so no small positive constant.
- A corner-preserving split changes the energy of massless light states of the register's update by -c(eps) K^2 E per split, with c from 3.142e-2 at eps = 1.271 to 4.622e-5 at eps = 0.041 (c/eps^2 tending to about 0.0275).
- A supplied frozen sea has number variance 0.502 to 0.503 l^2 in sharp cubes and exponent 1.12 in smooth windows.

#### Against measurement (estimates)

Measured inputs: rho_L = 1.13e-123 rho_P, w = -1.03 +- 0.03, Omega_L(BBN) < 0.05, early dark energy below 2% at recombination.

- Fixed 4-volume with splits: the measured value needs the first such split at T near 1.2 TeV. A supplied inflation by splits (539 ticks per split, 60 e-folds) overshoots by 3e110, and a Planck start gives about rho_P. The 1.2 TeV value sits at sqrt(M_L M_P), so reading it as the electroweak scale would be numerology.
- Fixed 4-volume with split losses in an empty vacuum and a thermal plasma: rho_L = 598 c g T_max^6/M_P^2, which needs T_max from 16 MeV (eps 1.27) to 48 MeV (eps 0.04), with w + 1 = -5e-66 today. This is a conditional relation only.
- Per-new-cell phase: Poisson counting lands within a factor of 2 but tracks, with the spread of Omega_L 3.59 at BBN, 2.74 at recombination and 1.25 today. Split noise is off by about 1e31 either way and correlated noise by about 1e116. Excluded.
- Self-tuning: a steady split rate makes the expansion at 1 MeV too slow by 3.7e17, and the measured H tau = 5.6e-61 needs alpha = 8.3e-121 by hand. Excluded.
- Sea number noise in a sharp Hubble window is 0.16 to 0.47 of the measured value, but it tracks, and the same noise on 1 m would be 5e25 kg/m^3 (sharp) or 4e7 kg/m^3 (smooth). Excluded.
- Capacity: 2^407.5 qubits per horizon would have to be supplied.

#### Boundary

Supplied: the frustum carrier, its central tick, the matter phase -E T, kappa = 1, the split construction and threshold, the corner-preserving split map, the update at the chosen mu and b, the empty vacuum and thermal plasma for the split-loss estimate, independent split phases, the self-tuning families, the unit map, LambdaCDM and all measured numbers. The empty-vacuum input conflicts with the sea-induced running of alpha in the register. The result is negative for the size of Lambda: no tested rule fixes it, and the fixed-4-volume rule turns the vacuum-energy problem into a requirement that every refinement be adiabatic to about 1e-123 of rho_P. No rule fixing the size of Lambda is established.

[end of lines 35-62 of the note]

(Omitted from the note: lines 1-17 and lines 24-26, 28-34 and 63-63.)

### #9918: Curvature-squared inflation misses the ACT tilt, and no rule lifts it

- Branch `claude/toe-act-tilt-20261021`, head `4a56f8a8cc`; note `docs/CURVATURE_SQUARED_INFLATION_MISSES_THE_ACT_TILT_AND_NO_RULE_LIFTS_IT_BOUNDED_THEOREM_NOTE_2026-10-21.md`.
- Runner: [`scripts/curvature_squared_inflation_misses_the_act_tilt_and_no_rule_lifts_it_2026_10_21.py`](../scripts/curvature_squared_inflation_misses_the_act_tilt_and_no_rule_lifts_it_2026_10_21.py); cache `logs/runner-cache/curvature_squared_inflation_misses_the_act_tilt_and_no_rule_lifts_it_2026_10_21.txt`.
- Kind of statement: Exact leading-order theorems (symbolic) for supplied single-field families and for the e-fold and gravitational-wave relation of a constant-w phase; numerical second-order Hubble-flow solves; sigma pulls against Planck, ACT and DR2 are estimates. No inflaton is derived.
- Dependencies: Supplied curvature-squared and cubic coefficients, shape families, pivot, g*, colour running and top mass for reheating, transfer prefactors, BBN limit, heat-kernel bound, running-tilt constant. Earlier campaign results on the inflaton background, running tilt and split schedule are cited by the note without PR numbers and not rerun. Cited by 9979 and 10000.

Claim scope (verbatim):

> For supplied single-field slow-roll models with second-order Hubble-flow tilts, exponential plateaus give n_s = 1 - 2/N for every steepness and power plateaus 1 - c phi^-k give 1 - 2(k+1)/((k+2)N); supplied curvature-squared inflation with the rules' colour-anomaly reheating gives n_s = 0.9617, estimated at -0.8, -4.1 and -4.5 sigma against Planck, ACT and DR2, and none of the rules' own terms estimated here shifts n_s by more than about 1e-10; no inflaton is derived.

Statement and supporting text (copied from the note):

#### Statement

1. A phase of constant w from rho_end to rho_rh adds dN = (3w - 1) ln(rho_end/rho_rh)/(12(1 + w)) e-folds and boosts the gravitational-wave background of the modes entering during it by E, with ln E = 4 dN for every w.
2. At leading order in 1/N, V = 1 - c e^(-kappa phi) gives n_s = 1 - 2/N for every kappa, and V = 1 - c phi^-k gives n_s = 1 - 2(k+1)/((k+2)N).
3. With V = M^2 v(phi), eps, eta, n_s and r are M-free, so in pure curvature-squared inflation n_s depends on N* alone and no curvature-squared-type term can lift it.
4. Supplied curvature-squared inflation with the rules' colour-anomaly reheating gives N* = 50.3 and n_s = 0.9617. Against measurement this is estimated at -0.8 sigma (Planck), -4.1 sigma (ACT) and -4.5 sigma (DR2). None of the rules' own terms estimated here moves n_s by the +0.012 needed.

#### Derivation

The stiff-phase relation follows from matching e-folds at the pivot k = 0.05/Mpc with rho scaling as a^(-3(1+w)) during the phase; the gravitational-wave boost follows from the same scaling of the modes entering during it. For the plateau families the slow-roll integrals give N in terms of phi at leading order, and substituting into n_s - 1 = 2 eta - 6 eps gives the two closed forms. ACT therefore asks for a power-law plateau with k = 0.88 at N* = 50.3 or 1.63 at N* = 55.7, while Planck was met by k of about 43, effectively exponential.

The runner's background solver and second-order Hubble-flow code reproduce 0.96489 at N* = 55. The N* that gives each measured n_s is 55.02, 74.84 and 78.55 for Planck, ACT and DR2 (leading order 57.0, 76.9, 80.6), with r = 0.0035, 0.0020 and 0.0018 there. Instant reheating gives N* = 55.7 and n_s = 0.9653; plain curvature-squared inflation reheats through its quadratic minimum (w = 0), so instant is its ceiling.

The rules' own forms:
- The hinge-sum plateau has eps_H = 3(1+w)(pi rho*/rho)^2 and n_s - 1 = -6(1+w). It needs w = -0.99415, -0.99567 or -0.99587, a fluid no rule supplies, and its tensor amplitude is at least 0.41, so it is excluded on every dataset regardless of n_s.
- A running coupling with n_s - 1 = gamma/N needs 57.0, 76.9 or 80.6 e-folds to the pole; on the ladder length L* = 133.28 the needed |gamma| is 4.68, 3.47 or 3.31, and gamma is supplied.
- A constant transfer per split gives n_s = 1 - q/(2N_e) with r = 8/N_e; ACT with q = 4 needs N_e = 76.9 and r = 0.104. Its Jordan-frame reading is curvature-squared inflation.
- A lattice curvature-squared remainder changes the coefficient c = 5.7e8 by about 2e-10 and n_s not at all (item 3).
- Hinge corrections to the Friedmann law have rho/rho* <= 7.2e-11, so |dn_s| is about 1e-10 at most.
- A cell-scale cubic curvature term with an O(1) coefficient gives lambda = 2.3e-18, against the needed -1.8e-4.
- Promoting the copy mass to a field puts it in the natural-inflation class, which never reaches 1 - 2/N at r < 0.036.

#### Checks

The runner ends with `TOTAL: PASS=16 FAIL=0`. Among its lines:

- `[PASS] B1 N* that gives each n_s (2nd-order flow): Planck 55.02, ACT 74.84, DR2 78.55 (leading 2/(1-n_s): 57.0, 76.9, 80.6); r there 0.0035, 0.0020, 0.0018`.
- `[PASS] B2 reheating histories (e-fold matching at k = 0.05/Mpc): colour-anomaly decay (w = 0, T_rh = 1.5e+08 GeV) N* = 50.3, n_s = 0.9617 [Pl-0.8 ACT-4.1 DR2-4.5]; instant N* = 55.7, n_s = 0.9653 [Pl+0.1 ACT-2.9 DR2-3.3]`.
- `[PASS] B3 THEOREM (sympy): a phase of constant w from rho_end to rho_rh adds dN = (3w-1) ln(rho_end/rho_rh)/(12(1+w)) e-folds and boosts the GW background ... with ln E = 4 dN for every w`; kination to BBN gives N* = 69.6 and n_s = 0.9721.
- `[PASS] B4 ESTIMATE: ... caps any stiff phase at dN <= 6.6: N* <= 62.4, n_s <= 0.9689 [Pl+1.0 ACT-1.7 DR2-2.1]; ACT needs dN = 19.1, a GW boost e^77`.
- `[PASS] C1 hinge plateau ...: needs w = -0.99415 (Planck), -0.99567 (ACT), -0.99587 (DR2), a fluid no rule supplies; P_t >= 4/pi^2 = 0.41`.
- `[PASS] C2 N to the pole needed: 57.0 (Planck), 76.9 (ACT), 80.6 (DR2); on the ladder (N >= L* = 133.28) |gamma| = 4.68, 3.47, 3.31`.
- `[PASS] C3 constant transfer per split ...: ACT with q = 4 needs N_e = 76.9, r = 0.104 (excluded); r < 0.036 needs N_e > 222 and q = 11.6`.
- `[PASS] C4 legacy graph-growth notes on main ...: n_s = 1 - 2/N_e at N_e = 60 is 0.9667 [Pl+0.4 ACT-2.4 DR2-2.8]`.
- `[PASS] D1 THEOREM (leading order in 1/N, sympy): V = 1 - c e^(-kappa phi) gives n_s = 1 - 2/N for every kappa ...; V = 1 - c phi^-k gives n_s = 1 - 2(k+1)/((k+2)N)`.
- `[PASS] D2 at r < 0.036 the exponential plateaus (E/T alpha-attractors, any alpha) and natural inflation stay > 2 sigma below ACT at N* <= 55.7`, while power plateaus with k = 1, 2 and curvature-squared plus a cubic term reach it.
- `[PASS] E1 THEOREM: V = M^2 v(phi) makes eps, eta, n_s and r M-free ...: no R^2-type term can lift the tilt`.
- `[PASS] E2 ESTIMATE hinge Friedmann law ...: |dn_s| <~ 2 rho/rho* = 1e-10 vs the needed +0.012`.
- `[PASS] E3 cubic: a cell-scale c3 R^3 with c3 = O(1) a^4 gives lam = 72 M^4 c3 = 2.3e-18 c3 vs the needed -1.8e-04`; a loop of any field heavy enough to act locally gives |lambda| <= 4e-15 (estimate).
- `[PASS] E4 copy-mass promotion is the natural-inflation class ...: it never reaches 1 - 2/N at r < 0.036`; the SU(2) condensate hilltop would sit 5e11 times above the tensor bound.
- `[PASS] F1 11 campaign readings (all with a supplied piece) within 2 sigma: Planck 6, ACT 1, DR2 0 vs 4.6, 3.3, 3.3 by chance`.
- `[PASS] F2 shape grid (76 points, N* = 55.7): 32% fit ACT at 2 sigma with r < 0.036, 55% fit Planck; every fit spends >= 1 supplied shape parameter`.

#### Estimates against measurement

All pulls are estimates. The Planck and ACT n_s values differ by 0.0091, about 1.8 sigma, a lower bound on their tension since P-ACT-LB includes Planck data; all three values are reported and no candidate was tuned to any one. Supplied curvature-squared inflation plus any post-inflation history allowed by the BBN bound on extra radiation stays at least 1.7 sigma below ACT, and 4.1 sigma below with the rules' own reheating. The legacy main-branch claim that n_s = 1 - 2/N_e at N_e = 60 matches Planck within 0.4 sigma is narrowed: it is -2.4 sigma against ACT. Meeting ACT needs a second supplied deformation (a power-law plateau with k of about 1 to 2, or a cubic curvature coefficient of about -1.2e-4 to -1.9e-4) or about 19 extra e-folds, which the BBN bound excludes. Because fits on the shape grid are common and each spends a supplied parameter, a fit is not evidence.

#### Boundary

Supplied: the curvature-squared and cubic coefficients and the shape families; the pivot, g*, the colour running and top mass used for reheating; the gravitational-wave transfer prefactors, the BBN limit and a heat-kernel coefficient bound of 1e-2; the running-tilt constant C = 4.891 and the one-loop beta coefficients; and the measured n_s, r and A_s. Earlier campaign results on the inflaton background, the running tilt and the split schedule are cited, not rerun. No inflaton and no tilt are derived.

[end of lines 18-67 of the note]

(Omitted from the note: lines 68-68 and lines 1-17, i.e. front matter, derivation prose, run instructions and any candidate-rule checklist.)

### #9946: Label copies carry linked families; only a supplied label parity or magnetic charge stabilises a massive relic

- Branch `claude/toe-dm-revisit-20261021`, head `955073bc44`; note `docs/LABEL_COPIES_CARRY_LINKED_FAMILIES_AND_ONLY_A_SUPPLIED_LABEL_PARITY_OR_MAGNETIC_CHARGE_STABILISES_A_MASSIVE_RELIC_BOUNDED_THEOREM_NOTE_2026-10-22.md`.
- Runner: [`scripts/label_copies_carry_linked_families_and_only_a_supplied_label_parity_or_magnetic_charge_stabilises_a_massive_relic_2026_10_22.py`](../scripts/label_copies_carry_linked_families_and_only_a_supplied_label_parity_or_magnetic_charge_stabilises_a_massive_relic_2026_10_22.py); cache `logs/runner-cache/label_copies_carry_linked_families_and_only_a_supplied_label_parity_or_magnetic_charge_stabilises_a_massive_relic_2026_10_22.txt`.
- Kind of statement: Exact or closed-form checks on small registers (a statement about the registers examined, with label terms and label parity supplied) and finite diagnostics; estimates of label relics, monopoles and edge quanta against measurement use supplied inputs. Several decay times and the conserved-number census are stated, not computed.
- Dependencies: Supplied label terms and label parity, effective couplings, production yield, splittings, cell unit, cubic compact-link lattice, sync slab. Companion edge-register census note (named in the note; not in this theme's PR list) supplies the slab construction, which is inlined from its runner; a hidden-sector commutant result is cited, not recomputed. Cited by 9963, 9991 and 9996 (logged).

Claim scope (verbatim):

> For the update law's parallel-carriage circuit at zoom b, whose b^3 label copies of each block fermion are rotated by an exact U(b^3): gauge generators act as T x 1 and commute with all of U(b^3), so every label copy carries one whole linked family (checked at b = 2); on one chiral family the only link-free Weyl state is nu^c and the only gauge-invariant bilinear is the Majorana nu^c nu^c (hand-entered charge table), so a chiral label copy takes no label mass and heavy labels are vector-like; any quadratic label term keeps one exact U(1) per label-mass eigenspace (commutator 2e-15), which the links make a long-range force on matter; terms even in each label break label number but keep label parity (-1)^N_k, and one mixing bilinear breaks it (Fock toy, 2 labels x 3 modes), so label parity is a supplied choice. For the links: the spin-3/2 register's charge conjugation maps E to -E and U to U^dag (checked), the extra mode is stated C-odd with no selection rule against three-photon decay; the register raiser conserves each bond's rishon number (other link-spin sectors are superselected); on compact cubic links every cube's magnetic charge is an integer, the total is zero and 312 continuous-evolution events changed charges in +- pairs (monopole number locally conserved); on the six-edge block triangulation 48 registers per 8 block sites give two light roots at |K| = 0.05 and every other real root at least 1.49 per block tick, and the one-register hop conserves no edge number or parity. Estimates of label relics and monopoles against measurement use supplied inputs. Supplied model, finite diagnostic: label terms and label parity, effective couplings, the gravitational production yield, splittings, the cell unit, a cubic link lattice for the monopole count, the sync slab; many decay times and the conserved-number census are stated, not computed.

Statement and supporting text (copied from the note):

#### Statement

A. Label copies at zoom b (label terms supplied).

1. The links read per coarse cube alike for every label: gauge generators act as T x 1 and commute with all of U(b^3). Every label copy carries one whole linked family.
2. In one chiral family the only link-free Weyl state is nu^c, and the only gauge-invariant bilinear is nu^c nu^c, a Majorana term that the Z4 of B - L forbids (stated from the register). A chiral label copy takes no label mass; heavy labels are vector-like.
3. Any quadratic label term keeps one exact U(1) per label-mass eigenspace. The update law links these numbers to the gauge fields, so the light label's number would be a massless long-range force on matter. The runner states the MICROSCOPE bound (below about 1e-25) against which this is excluded; it does not compute the force.
4. Terms even in each label break label number (no dark link) but keep label parity (-1)^N_k; one mixing bilinear breaks it. The fine tick has trivial cell commutant (cited from an earlier hidden-sector computation), so label parity is not in the fine tick: it is a supplied choice. With parity supplied, the lightest odd state N' (label nu^c) is exactly stable and link-free; the runner states, without computing, a lifetime of about 1e-39 s if parity is broken by mixing.

B. Link registers.

5. For the spin-3/2 register, charge conjugation C (m -> -m) maps E -> -E and U -> U^dag and keeps ring exchange, so n photons have C = (-1)^n. The extra d1 d2 d3 mode is stated to be C-odd and trivial under the kept turns, so three-photon decay is allowed and no selection rule protects it. Its lifetime at the cell scale, about 1e-41 s, is stated, not computed: not dark matter.
6. The register raiser (the rishon hop between a bond's two ends, 2S = 2) conserves the bond's total rishon number while changing each end's. Other link-spin sectors are superselected and never occur; they are not a relic.
7. On compact link angles (a cubic lattice, supplied) every cube's magnetic charge, the reduced plaquette flux divided by 2 pi, is an integer and the total is zero. Continuous evolution changes charges only in +- pairs: monopole number is locally conserved and a lone monopole is stable. Monopoles are magnetically charged, so they are not dark.

C. Edge registers on the six-edge block triangulation (sync slab, fixed lapse, zero shift).

8. There are 48 registers per 8 block sites, 6 per site, the metric count, so no non-metric light strain exists. At |K| = 0.05 the light roots are the two tensor polarisations on the edge cone, and every other real root is at the cell scale.
9. The one-register hop V_e + V_e^dag changes every edge value by +-1 and anticommutes with (-1)^n: no edge-register number or parity is conserved. With crystal momentum alone, and threshold zero at K = 0 (back-to-back massless pairs), massive edge quanta near K = 0 are open to decay. Near-zero transfer roots at generic K are ill-conditioned (Jordan blocks of the gauge zeros), so a kinematically closed band minimum near the zone edge is not excluded here.

D. Conserved numbers as stabilisers (a census stated, not computed).

10. Exact U(b^3) must be broken (LEP), and quadratic terms leave linked U(1)s. Label parity is not in the fine tick. The Z4 of B - L makes the light neutrino the lightest carrier, which is hot and below 1% of dark matter (sum m_nu below 0.07 eV). Rishon number is superselected. Only zero static charge occurs in the Gauss sectors. Magnetic charge is exact but not dark. Edge value, copy sign and turn charges are not conserved; crystal momentum and pattern are not particle charges. The dark constant has zero mean in every cube under the response law, so it has no carrier. Only label parity (supplied) and magnetic charge (not dark) stabilise a massive relic.

#### Derivation

Item 1 checks [T x 1, 1 x U] = 0 for a random 3 x 3 Hermitian T and a random U(8) at b = 2. Item 2 scans a hand-entered table of one family's SU(3), SU(2) and hypercharge assignments for neutral states and singlet bilinears. Item 3 checks that the projectors onto each eigenvector of a random 8 x 8 label mass commute with H = H_c x 1 + 1 x M. Item 4 builds six Jordan-Wigner modes, adds intra-label hops, intra-label pair terms and a cross-label term even in each label, and tests commutation with label parity and label number, then adds a mixing bilinear. Item 5 checks C Sz C = -Sz and C S+ C = S+^T for S = 3/2. Item 6 checks commutation of the rishon hop with total and one-end rishon number. Item 7 draws random compact angles on a 5^3 lattice, computes the cube charges, and follows 400 random small steps (width 0.02), counting charge-changing events. Items 8-9 build the sync slab's quadratic form on the six-edge triangulation (inlined from an earlier edge-register computation) and find its roots at |K| = 0.05 by a polynomial eigenproblem; the edge hop is checked on a four-level register.

#### Finite checks

Exact or closed-form checks (the runner asserts each):
- [T x 1, 1 x U] below 1e-12 (b = 2, 8 labels).
- Link-free state ['nu^c']; singlet bilinear [('nu^c', 'nu^c')].
- Label-mass eigenspace commutator 2e-15 (8 eigenspaces).
- Fock toy: label parity conserved below 1e-12 by even terms; label number broken (above 0.1); mixing at 1e-3 breaks parity (above 1e-4).
- Spin-3/2 C relations below 1e-12; rishon hop conserves the total, changes one end's (above 0.5).
- Compact links: integer charges to 1e-9, total 0, 312 events all in +- pairs; G(0) = 0.2498 on a 48^3 midpoint grid against Watson's 0.2527 (asserted within 3%).
- Edge hop anticommutes with (-1)^n below 1e-12.

Finite diagnostics (supplied model, finite diagnostic):
- Six-edge slab: 48 registers; light roots [0.05 0.05] at |K| = 0.05; every other real root at least 1.49 per block tick.

#### Estimates against measurement

Estimates with supplied inputs (M_P = 1.221e19 GeV, reduced 2.435e18 GeV, the cell scale Lambda = M_P/sqrt(8 pi) for a = sqrt(8 pi) l_P, a cell-contact decay width with splittings dm = (1.4-5)e-3 m, alpha_eff = 0.03-0.3 with a coannihilation factor 0.1-10, a gravitational production yield Y = 1e-3 (T/M_P)^3 e^(-2m/T), r < 0.036, MACRO's 1.4e-16 /cm^2/s/sr at beta 1e-3):
- Coloured or charged label states reach N' only through cell-scale contacts: lifetime 4e+44 s at m = 10 TeV, far beyond the age; decay before BBN (1 s) needs m above 8.5e+12 to 3.0e+13 GeV.
- A thermal coannihilating label family gives Omega h^2 = 0.12 at m about 0.4 to 39 TeV; its stable coloured relics would then exceed heavy-isotope bounds by more than 1e16 (the abundances n/n_B above about 1e-12 against bounds below about 1e-28 are stated, not computed): excluded.
- Non-thermal window: the reheating temperature needed is T_reh/m = 0.42, 0.18, 0.11 at m = 1e13, 1e14, 1e15 GeV; T_reh < 5.8e+15 GeV (from r < 0.036) caps m below 1.0e+17 GeV; dlnY/dlnT = 8, 14, 22, so the abundance is tuned.
- N' couples by contact only: sigma_SI about m_n^2/(pi Lambda^4) = 3e-102 cm^2, no direct-detection signal; label masses at the cell scale give e^(-2 Lambda/T_max) = e^-842, so none are made after the start.
- Monopoles: M = (pi/2 alpha) G(0) Lambda = 1.3e+19 GeV at alpha = 0.071 (the S = 3/2 natural coupling), allowed dark-matter fraction below 3.6e-03; 1.9e+21 GeV at alpha = 5.0e-4 (a hypercharge-unit target), fraction below 5.1e-01. MACRO excludes monopoles as all of the dark matter at the natural coupling.
- Edge quanta: b_e = 6 gives m about 6.1e+17 GeV and lifetime about 2e-41 to 2e-39 s; b_e = 38 gives 9.6e+16 GeV and 4e-39 to 4e-37 s (universal coupling, N = 1 to 100 channels). Any closed band minimum would be cell-scale and made only at T about m/20 > T_max = 6e+15 GeV, or by splits, which carry vacuum to vacuum: no abundance from the rules.
- Conditional survivor: N' with a supplied label parity, m about 3e+13 to 1e+17 GeV, produced non-thermally; Omega is not set by the rules.

#### Boundary

Not claimed: a derivation of label parity from the register (it is supplied); the dark-matter abundance; the extra link mode's lifetime, the mixing lifetime and the census of section D (stated, not computed); a closed band minimum of the edge registers near the zone edge (not excluded); monopole production; the hidden-sector commutant result (cited). The monopole count uses a cubic compact-link lattice, not the register's bcc link geometry.

#### Supplied vs forced

Supplied: the label terms and label parity, alpha_eff, the production yield, the splittings, the cell unit a = sqrt(8 pi) l_P, the cubic link lattice, the sync slab with fixed lapse and zero shift, and the measured inputs. Forced, given those: the linked family per label; no label mass for a chiral copy; the linked U(1) per label-mass eigenspace; label parity under even terms and its breaking by mixing; the C action on the spin-3/2 register; rishon-number superselection; integer, locally conserved magnetic charge; six registers per site and the two light roots; no conserved edge number or parity.

#### Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's parallel-carriage circuit and label copies, the site-bond link registers and their raiser, the edge registers on block edges, the response law's zero-mean dark constant. Zero premise weight; results using it are conditional on it.
- Companion computation: EDGE_REGISTER_SET_CENSUS_CUBE_EDGES_ALONE_GIVE_NO_HINGE_SUM_AND_SIX_EDGES_PER_SITE_GIVE_TWO_TENSOR_POLARISATIONS_ON_THE_EDGE_CONE_BOUNDED_THEOREM_NOTE_2026-10-22 (the slab construction is inlined from its runner).

[end of lines 18-83 of the note]

(Omitted from the note: lines 84-92 and lines 1-17, i.e. front matter, derivation prose, run instructions and any candidate-rule checklist.)

### #9961: Split-time cascade is self-similar, so its delta-N spectrum is flat and the trigger reads no linear scalar

- Branch `claude/toe-spectral-tilt-20261021`, head `8cdd1d8ba1`; note `docs/THE_SPLIT_TIME_CASCADE_IS_SELF_SIMILAR_SO_ITS_DELTA_N_SPECTRUM_IS_FLAT_AND_THE_TRIGGER_READS_NO_LINEAR_SCALAR_BOUNDED_THEOREM_NOTE_2026-10-22.md`.
- Runner: [`scripts/the_split_time_cascade_is_self_similar_so_its_delta_n_spectrum_is_flat_and_the_trigger_reads_no_linear_scalar_2026_10_22.py`](../scripts/the_split_time_cascade_is_self_similar_so_its_delta_n_spectrum_is_flat_and_the_trigger_reads_no_linear_scalar_2026_10_22.py); cache `logs/runner-cache/the_split_time_cascade_is_self_similar_so_its_delta_n_spectrum_is_flat_and_the_trigger_reads_no_linear_scalar_2026_10_22.txt`.
- Kind of statement: Mixed. Exact register arithmetic (A); a conditional theorem on cascades with level-independent shape (B1); finite seeded diagnostics in a supplied 2D block-tree toy with supplied Poisson stepping of each register (B2 to B5, C2); exact toy arithmetic (D); estimates against measurement.
- Dependencies: Uses the read-lapse note with a stationary shift (PR 9933, assigned to gravity-edge-registers), the cascade theorem and 3.81e-5 per-level spread from the register's cosmology work, the one-cell-start reset and the Born split-time spread (cited by name only). PR 10007 narrows part B: split-time offsets are inherited rather than redrawn under the laws' quantile transport, and the Poisson toy assumed redraws (see CORRECTIONS). Relied on by 9966, 9979, 10000 and 10007.

Claim scope (verbatim):

> For the update law's glued split (a block splits when the mean of its cube's edge registers reaches 4s, its children's edges along parent edges take the parent's value minus s, held edges block a child, and the trigger needs each unsplit +x, +y, +z face neighbour's shared edges full): (A) exact register arithmetic: a generation is s register steps, ln 2 of log-length, for every s; over the 18 edges of a five-tetrahedron block cube the trigger's mean log-length is tr h/6 at first order, so no traceless strain moves it, and on a tensor wave along z it is -(9 h+^2 + 2 hx^2)/72 at second order. (B) A cascade whose level-l split-time spread has a level-independent shape and variance sig^2 lam^l has Delta^2(2k) = lam Delta^2(k), so n_s - 1 = log2 lam. In a 2D block-tree toy that keeps the trigger rule, with Poisson stepping of each register supplied to give the trigger a timing spread, the mean wait per generation stays ln 2 e-folds, the coupled (max-plus) trigger raises the wait variance by 1.8 and correlates waits (neighbours +0.32, parent-child -0.14), and the deep levels are stationary (deepest per-level ratio 0.9994 against the 0.976 that n_s = 0.965 needs); the per-level spread (ln 2)^2/(m s) contains only register numbers, so s and the window set the amplitude, never the tilt. (C) With the stationary-shift reading of the read lapse (zeta = 0 at k != 0), the laws give no linear split-time fluctuation; the tensors reach it at second order, blue and at most about 2e-21 at r < 0.036. (D) If every rule component is a function of local edge length, the uniform-length slice is the uniform-density slice and split-time spread carries zeta = 0; it becomes zeta = H delta T only through a supplied exit that reads ticks. Not computed: the 3D trigger with all 18 registers, the quantum volume-mode width per block, the second-order constraint that sources the trace from tensors.

Statement and supporting text (copied from the note):

#### Statement

A. Register arithmetic and what the trigger reads (exact).

1. An edge register's length is its flat length times 2^(n/s - 3). The trigger mean 4s is twice the flat length; the children's value 4s - s = 3s is their own flat length, and two children span the parent edge. A generation is therefore s register steps, ln 2 of log-length, for every s, and the window [0, (4 + Delta)s] holds the whole cycle for every Delta >= 0.
2. Over the 18 edges of a block cube (12 axis edges and the 6 face diagonals of the even corners, the five-tetrahedron cube), the mean log-length is tr h/6 at first order in a strain h. No traceless strain moves the trigger, since the 18 directions have mean e e^T = 1/3.
3. At second order, on a tensor wave along z, the mean log-length moves by -(9 h+^2 + 2 hx^2)/72. The trigger reads tensors quadratically, with a weight that depends on the polarisation.

B. Split cascades.

1. Theorem. If the split-time spread contributed at level l has a level-independent spatial shape (in units of the level's block) and variance sig^2 lam^l, then Delta^2(2k) = lam Delta^2(k), so n_s - 1 = log2 lam exactly. Self-similar levels give n_s = 1. This rederives the cascade item in the register's cosmology work.
2. Toy with the trigger rule (2D block tree, 512^2 finest blocks, block-mean registers), with Poisson stepping of each register supplied to give the trigger a timing spread. In the free trigger (mean reaches 4s, children start at the parent's value minus s), the mean wait is ln 2 e-folds, the wait variance is (ln 2)^2/(m s), and the per-level variance does not depend on the level.
3. In the coupled trigger (+x and +y unsplit neighbours full, held edges block, 2:1 balance), the max-plus coupling raises the wait variance by 1.8. Neighbour waits correlate at +0.32. Parent and child waits anticorrelate at -0.14, because a delayed parent's registers keep rising and the excess passes to its children. The mean wait stays ln 2, since the geometry and not the split sets it. The deep levels are stationary: the effective per-level variance at levels 8 and 9 agrees to 0.9994, against the 0.976 that n_s = 0.965 needs. Held edges bind rarely (0.3% of the ready block-steps); the neighbour-full condition binds 90%.
4. The split-time field is made of sharp blocks. At fixed |k| the power along the axes exceeds the power along the diagonals by about 1.5, a statistical anisotropy on top of n_s = 1.
5. The e-fold wait Gamma(m s) ln 2/(m s) contains only register numbers (s, and m, the registers the trigger averages). Neither H, eps0 nor the window size enters, so rule-constant s and m give lam = 1 for every expansion history. s = 64 gives the same result.

C. The laws' own channel.

1. At linear order the trigger reads only tr h/6 (A2). With the stationary-shift reading of the read lapse, the scalar sector has zeta = 0 at every k != 0. So the laws give no linear split-time fluctuation at k != 0.
2. The quadratic readout of a flat Gaussian field is blue (n - 1 of about +0.3 on a 64^3 grid, from the infrared logarithm) and of size about 9 Delta_h^4.

D. When the split-time record is a curvature perturbation.

1. Suppose every rule component is a function of the local edge length: the constant, the sea carried from vacuum to vacuum, and injection at the fixed-length trigger. Then rho = F(a) in every patch, the uniform-length slice is the uniform-density slice, and zeta = delta N(flat to uniform rho) = 0 for any split-time spread.
2. Only a tick-integrating quantity separates the patches, for example the record count, which no law reads. An exit law that read it would give zeta = H delta T per level, that is, the cascade spectrum of B.

[end of lines 18-42 of the note]

#### Estimates against measurement

- Index. Every split-time channel with rule-constant numbers gives n_s = 1: 8.4 sigma from Planck and further from ACT. The measured index needs lam = 2^(n_s - 1) = 0.976 per split. In the Poisson model that means the product m s of the registers read and the steps per octave must grow by 2.46% per split, which no rule supplies.
- Amplitude. A_s needs a per-level spread of 3.8e-5 e-folds. In the Poisson model that is m s = ln 2/A_s = 3.3e8, against at most 18 x 113 = 2034 for the rules, so the supplied Poisson model overshoots the amplitude by about 1.6e5. The laws' own channel is zero at linear order. At second order it is at most about 2e-21 at r < 0.036, and blue. CL-3's only de Sitter phase is today's (P_t of about 5e-122), so in the rules it is zero in practice.
- Isotropy. Sharp blocks give axis-aligned excess power of order 1.5 in the toy.

#### Boundary

Supplied: Poisson stepping of each register, used only in B to give the trigger a timing spread (a stochastic model, not a law); one mean register per block, averaging m = 3 in the toy; the 2D block tree; "full" read as a neighbour mean >= 4s; interior child edges at the parent mean minus s; a scalar stand-in for one tensor polarisation in C2; the injection fraction in D1, any value.

Forced, given those: the register arithmetic; the first-order trace readout and the second-order tensor form; Delta^2(2k) = lam Delta^2(k); a mean wait of ln 2 per generation; stationarity of the coupled cascade in the toy; zeta = 0 when rho = F(a).

Not computed: the 3D trigger on all 18 registers with the three neighbour faces; the quantum volume-mode width per block; the second-order constraint that sources the trace from tensors, which could change the coefficient in A3 but not the order; any exit law.

Not claimed: that a tilt is impossible. A tilt needs a rule number that changes from one generation to the next (lam = 0.976 to 0.982), or a clock, and that is a named supplied number, not a gap the cascade fills.

#### Dependencies

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [candidate_laws](CANDIDATE_LAWS.md)
- Used: the read-lapse note (zeta = 0 at k != 0 with a stationary shift, inhomog-volume #9933); the cascade theorem and the 3.81e-5 per-level spread (cosmology); the reset at fixed local e-fold number (one-cell-start C3); the Born spread of split time (split-creation B5).

[end of lines 54-74 of the note]

(Omitted from the note: lines 43-53, 75-81 and lines 1-17, i.e. front matter, derivation prose, run instructions and any candidate-rule checklist.)

### #9979: A fold is a slow scalar clock only when the unfolded sea is critical on a surface; the update's Dirac sea makes it fast

- Branch `claude/toe-fold-inflaton-20261021`, head `3d98c3bd3d`; note `docs/A_FOLD_IS_A_SLOW_SCALAR_CLOCK_ONLY_WHEN_THE_UNFOLDED_SEA_IS_CRITICAL_ON_A_SURFACE_AND_THE_UPDATES_DIRAC_SEA_MAKES_IT_FAST_BOUNDED_THEOREM_NOTE_2026-10-22.md`.
- Runner: [`scripts/a_fold_is_a_slow_scalar_clock_only_when_the_unfolded_sea_is_critical_on_a_surface_and_the_updates_dirac_sea_makes_it_fast_2026_10_22.py`](../scripts/a_fold_is_a_slow_scalar_clock_only_when_the_unfolded_sea_is_critical_on_a_surface_and_the_updates_dirac_sea_makes_it_fast_2026_10_22.py); cache `logs/runner-cache/a_fold_is_a_slow_scalar_clock_only_when_the_unfolded_sea_is_critical_on_a_surface_and_the_updates_dirac_sea_makes_it_fast_2026_10_22.txt`.
- Kind of statement: Mixed. Exact small-ring diagonalisation (A); a stiffness theorem with lattice ratio checks (B); a 1D toy with supplied one-loop stiffness and slow-roll dictionary (C); a supplied continuum-cutoff model of the Dirac band (D); an energy bound (E); estimates against measurement. All slow-roll numbers depend on the supplied star rule, J a = sqrt 3, M_P a = 1 at the flat rung, N* = 55 and semiclassical expansion with Hubble friction.
- Dependencies: Uses the neighbourhood-roles note (star rule, bound-pair folds), the split-time cascade note (PR 9961), the record-clock note (PR 9966), PR 9918, and inflaton-design B1/C1 and inflaton A1 (cited by name). PR 10000 recomputes the self-consistent N* for the nested-sea plateau and obtains about 47, so the N* = 55 index values here are conditional on that supplied N* (see CORRECTIONS). The pole theorem is imported by 9982 and 9986; 10000 uses its re-seeding and misfold statements.

Claim scope (verbatim):

> For a fold order parameter m that opens a gap in a half-filled sea, with the one-loop (adiabatic) stiffness Z(m) = sum |<n|dH|0>|^2 / (E_n - E_0)^3 and the semiclassical slow-roll dictionary: (A) exact on rings N = 8, 10, 12: the star rule sum P_3/2 is the Majumdar-Ghosh form, with two gapped zero-phase folds; uniform odds (equal amplitudes on every half-filled configuration) are its top, an exact eigenstate at energy 1 per site, which the update's hop moves off within about one tick; the sea's weight on the fold manifold is conserved under the fold rule's unitary and falls with N (0.786, 0.660, 0.541). (B) Theorem: Z = c_d m^(d-3), with d the codimension of the sea's gapless set (c_1 = 1/3, c_2 = 2/3, d = 3 logarithmic), so the unfolded point is at infinite field distance only for d = 1. Lattice ratio check: 1D dimer chain 4.04, 3D nested cubic sea 4.00, 3D Dirac sea 0.91 (4 means pole, 1 means log). (C) 1D toy with the pole (dimer path, exact infinite-chain Wick): V_star falls monotonically from 0.07559 to 0 and z = 1/(24 pi delta^2); slow roll gives n_s = 0.9631-0.9634 at N* = 55 for rungs 0, 2, 4, r = 7e-6 to 2.5e-8, exit at delta = 0.01-0.05; lam = 2^(-2/N) = 0.975; A_s fixes the fold rung near 20 for coupling 1; children born unfolded give q = 1/8 + 7x/8, never a clock. (D) The update's isotropic Dirac band (d = 3, continuum ball cutoff): eta at N* = 55 is -0.88 (flat rung) and -14 (rung 4); n_s = 0.965 needs zeta ~ 50 against zeta <= 1 from the unit map. (E) Plateau energy that leaves the coherent mode sits in misfolds: at most 0.36 walls per site at full conversion. Supplied: the star rule, the dimer path and one-loop stiffness, J a = sqrt 3, M_P a = 1 at the flat rung, the fold rung, coupling gamma = 1, N* = 55, the Dirac cutoff, m_f = 1, semiclassical FRW with Hubble friction, the split carrying the fold order.

Statement and supporting text (copied from the note):

#### Statement

A. The funnel's ends (exact, rings N = 8, 10, 12, half-filled sector).

1. Each P_3/2 on a three-site star is a rank-4 projector. The star rule sum_x P_3/2(x-1, x, x+1) equals N/2 + (4/3) sum S.S(x, x+1) + (2/3) sum S.S(x, x+2), which is the Majumdar-Ghosh chain (literature, 1969). It has two zero-phase folds, the bound-pair coverings, with gaps 0.539, 0.467 and 0.426.
2. Uniform odds (equal amplitudes on every half-filled configuration) are the funnel's top:
   - every star is spin 3/2, so the energy is 1 per site, the maximum;
   - the state is an exact eigenstate of the star rule and of every SU(2)-blind rule, so a fold never starts from it;
   - the update's hop breaks SU(2) and moves it off the top within about a tick (fidelity 0.83, 0.51, 0.20 at t = 0.25, 0.5, 1).
3. The update's sea (the XX ground state) sits low on the funnel: star energy 0.0645, 0.0685 and 0.0707 per site, tending to 0.0756. The fold manifold's projector commutes with the fold rule, so under that rule's unitary the sea's fold weight (0.786, 0.660, 0.541, about 0.91 per site) never changes. Unitary odds never complete a fold, so an energy sink is needed. Records cannot be the sink, because they never condition the odds (CL-2).

B. What sets the fold's speed (theorem and lattice check).

1. Theorem. Let a fold order parameter m open a gap in a sea of two-band (or Clifford) type. Its adiabatic (one-loop) stiffness is Z(m) = int rho(e) e^2 / (4 (e^2 + m^2)^(5/2)) de. If the gapless set has codimension d, then rho ~ e^(d-1), and Z = c_d m^(d-3):
   - d = 1 (a surface of gapless modes, or a 1D sea): a pole m^-2, with c_1 = 1/3;
   - d = 2: m^-1, with c_2 = 2/3;
   - d = 3 (Dirac points): log(1/m) only, with constant log 2 - 4/3.

   The canonical distance to the unfolded point, int sqrt(Z) dm, diverges only for d = 1.
2. Lattice check, using the ratio [Z(0.1) - Z(0.2)] / [Z(0.2) - Z(0.4)], which is 4 for a pole and 1 for a log:
   - 1D dimer chain: 4.04;
   - 3D half-filled nearest-neighbour cubic sea (a nested Fermi surface; the fold is the staggered gap): 4.00;
   - 3D lattice Dirac sea: 0.91.

C. A 1D toy where the pole exists: the star rule on the dimer path (hops 1 +- delta, with delta = 0 the sea and delta = 1 the fold).

1. Exact infinite-chain values:
   - The Wick reduction gives V_star = 1/2 + (2/3)[(g_s - g_s^2) + (g_w - g_w^2)] + (4/3) g_s g_w from the strong- and weak-bond correlators. It is checked against a 10-site Slater state (1e-12) and a 400-site chain.
   - V_star falls monotonically from V0 = 0.07559 to 0, with V0 - V ~ delta^2 ln^2(1/delta).
   - The stiffness is z = 1/(24 pi delta^2) (0.013263 at delta = 1e-9).
2. Slow roll. Take chi = zeta int sqrt(z) d delta in Planck units, with zeta = (J a)^(-1/2) / (M_P a_r) and M_P a = 1 at the flat rung (unit map). The pole makes V(chi) an exponential plateau: the fold is critically slowed near the sea.
   - n_s at N* = 55 is 0.9631, 0.9633 and 0.9634 at rungs 0, 2 and 4, against 1 - 2/55 = 0.9636. It does not depend on the coupling or the rung.
   - r is 7.0e-6, 4.1e-7 and 2.5e-8, which is about 2 zeta^2 z0 / N^2.
   - eps reaches 1 at delta = 0.05 to 0.01, before the fold completes. This is the graceful exit.
3. Per-split factor: lam = 2^(-2/N), which is 0.9751 at N = 55, inside Planck's range. It is not constant (running -2/N^2 = -6.6e-4). ACT's 0.974 needs N* = 77, as for every exponential plateau (act-tilt).
4. Amplitude. A_s = gamma V0 N^2 2^(-2r) / (pi^2 z0), so A_s fixes the fold rung: r = 19.8 + log2(gamma)/2. Then H/M_P = 2.5e-13 and r = 6e-18.
5. Split re-seeding. If children are born unfolded with share x, the per-split energy factor is q = 1/8 + 7x/8.
   - x = 1 is exact de Sitter with no exit.
   - Constant x < 1 is power-law inflation, with r = 16 eps = 0.28 at q = 0.976 (inflaton-design B1).

   The clock therefore needs the split to carry the fold order to the children.

D. The update's sea.

1. The update's light band is an isotropic Dirac band, a point node, so d = 3 (continuum, ball cutoff of one mode per cell, fold gap m_f = 1). The stiffness is only logarithmic, so eta ~ -sqrt(c2 / (V0 zeta^2 z1 N)) on the log asymptotics:
   - at N* = 55, eta = -0.88 at the flat rung (n_s far below 0.9);
   - eta = -14 at rung 4;
   - n_s = 0.965 would need zeta ~ 50, a cell far below the Planck length, against zeta <= 1 from the unit map.
2. Fold speed. Without the pole, a gapped local fold relaxes in about 1/gap ticks, while a split takes at least ln2/(H a) = 3.6e4 cell times. The fold finishes about 2e4 times within one split. This is the lattice eta problem of inflaton-design C1. In field form eta = M_P^2 V''/V, so the fold coupling cancels and only the stiffness and the cell in Planck units remain.

E. Reheating. The fold rule is >= 0 and vanishes only on folds. Every bit of plateau energy that leaves the coherent mode therefore sits in misfolds: domain walls, whose sites are free, so they are matter in the neighbourhood reading. Full conversion gives at most 2 V0 / gap_pair = 0.36 walls per site, a dense gas at the fold scale, which splits then dilute as matter.

[end of lines 26-76 of the note]

#### Estimates against measurement

- Index. In the pole case n_s = 1 - 2/N*: 0.963 at N* = 55, -0.4 sigma from Planck and about -3.5 sigma from ACT with DESI, unless N* is about 77. With the update's Dirac sea (no pole), eta is about -0.9 or worse: excluded by orders of magnitude.
- Tensors. r = 2 zeta^2 z0 / N^2 is below 1e-5 at every rung, far under 0.036.
- Amplitude. It needs the fold at about rung 20 (blocks of about 1e6 cells) for coupling 1. That is a supplied number.
- Running. -6.6e-4, against the measured -0.0045 +- 0.0067.

#### Boundary

Supplied:
- the star rule (not CL-1's cube tick);
- the dimer path and its one-loop stiffness as the fold's slow manifold and kinetic term;
- J a = sqrt 3;
- M_P a = 1 at the flat rung (unit map);
- the fold rung and the coupling gamma;
- N* = 55;
- the Dirac ball cutoff and m_f = 1;
- semiclassical FRW with Hubble friction acting on the fold mean field (no lattice mechanism for that friction is derived; the split's carriage map would have to provide it);
- the split carrying the parent's fold order.

Forced, given those:
- the Majumdar-Ghosh identity;
- the uniform-odds top as an exact eigenstate;
- conservation of the fold weight;
- Z ~ m^(d-3);
- the pole in 1D and on a nested surface, and its absence at Dirac points;
- n_s = 1 - 2/N with r ~ 2 zeta^2 z0/N^2 in the pole case;
- q = 1/8 + 7x/8;
- the fast roll with the update's Dirac sea.

Not computed:
- a 3D star rule's own potential;
- fold selection among the many 3D coverings;
- quantum diffusion near the top;
- the CL-3 vacuum standard's reading of the plateau (it gravitates only as a departure from the folded vacuum, and between splits it scales like the cell, l^-4, so a log-periodic ripple of period ln 2 is expected);
- reheating dynamics beyond the energy bound.

Not claimed: that a fold cannot be the clock. It can, but only if the sea it folds has a gapless surface. CL-1's sea has only Dirac points.

#### Candidate law text (tested, not adopted)

> CL-F (fold). "The first odds are the unfolded sea. Roles are read from the zero-phase states of a uniform star rule acting with coupling gamma on the blocks of rung r_f, and a split carries its parent's fold order to its children."


[end of lines 100-142 of the note]


Smuggling check:
- The pole comes from the sea's gapless surface, which is not CL-1's band, so a working version needs a new rule that makes the pre-fold sea nested (for example, a pre-role tick with only axis hops, whose half-filled sea is the nested cubic sea of B2). That rule is untested here and is not law text.
- gamma and r_f are fitted to A_s.
- N* is supplied.

#### Dependencies

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [candidate_laws](CANDIDATE_LAWS.md)
- Used:
  - the neighbourhood-roles note (star rule, bound-pair folds, misfolds as free sites);
  - the split-time cascade note (lam = 2^(n_s - 1), self-similar cascades);
  - the record-clock note (records give no clock);
  - inflaton-design B1 and C1 (power law from a fixed per-split fraction; the lattice eta problem);
  - act-tilt, PR #9918 (every exponential plateau gives 1 - 2/N);
  - inflaton A1 (H a < 1.93e-5);
  - the register's unit map (M_P L = 1) and its Dirac light band.
- Narrowed: the owner's fold-as-inflaton idea, to a sea that is critical on a surface.

[end of lines 144-162 of the note]

(Omitted from the note: lines 77-99, 143-143, 163-169 and lines 1-25, i.e. front matter, derivation prose, run instructions and any candidate-rule checklist.)

### #9988: The gapped mirror keeps only a number shared with light matter, and its lightest state is charged, so it gives no dark matter

- Branch `claude/toe-mirror-dark-matter-20261021`, head `16032e5f1e`; note `docs/THE_GAPPED_MIRROR_KEEPS_ONLY_A_NUMBER_SHARED_WITH_LIGHT_MATTER_AND_ITS_LIGHTEST_STATE_IS_CHARGED_SO_IT_GIVES_NO_DARK_MATTER_BOUNDED_THEOREM_NOTE_2026-10-22.md`.
- Runner: [`scripts/the_gapped_mirror_keeps_only_a_number_shared_with_light_matter_and_its_lightest_state_is_charged_so_it_gives_no_dark_matter_2026_10_22.py`](../scripts/the_gapped_mirror_keeps_only_a_number_shared_with_light_matter_and_its_lightest_state_is_charged_so_it_gives_no_dark_matter_2026_10_22.py); cache `logs/runner-cache/the_gapped_mirror_keeps_only_a_number_shared_with_light_matter_and_its_lightest_state_is_charged_so_it_gives_no_dark_matter_2026_10_22.txt`.
- Kind of statement: Mixed. Exact representation-theory, lattice (Smith normal form) and anomaly results for the mirror 16 with the Spin(10) pair square (A, C); a finite diagnostic of the cube tick's commutant and a theorem in a sector with a 1D witness (B); an atomic-limit level ordering using so(12) chain values cited from PR 9910 (D); estimates against measurement. All are for the supplied mirror cell and SM gauging.
- Dependencies: Depends on PR 9910 (one-cell pair-square spectrum; chirality-doublers), PR 9974 (mirror condensate; families-flavour) and PR 9985 (far-layer N_eff; chirality-doublers), on the named Spin(10) pair-square note, and on PR 9963 (copy-sign vertex, A5 rederived). PR 10005 takes this note's group U(1)_Y x U(1)_X, X = (1, 1, -3, -3, 1, 5), as an input to its own Smith-form computation, so its conclusion that no charge is absent from light states rests on it. Relied on also by 9991 and 9996 (logged). The note narrows PR 9985 to a massless mirror.

Claim scope (verbatim):

> For one mirror 16 (two spin components per cell) with the Spin(10) pair square, species-diagonal hops and SM gauging: (A) the species phases that keep every pair-square monomial form exactly U(1)_Y x U(1)_X, with X = 5(B-L) - 4Y = (1,1,-3,-3,1,5) on (Q,u^c,d^c,L,e^c,nu^c) and no discrete remnant (Smith normal form); mode number changes only by 4, and its Z4 = i^N equals exp(i pi X/2), the Spin(10) centre inside U(1)_X; mirror B' and L' are broken, B'-L' is kept; X has no anomaly with SM gauge fields, itself or gravity; with any species-diagonal light-mirror bilinear only U(1)_Y x U(1)_X(total) survives, so the mirror's number is shared with light B-L. (B) The CL-1 cube tick's one-body commutant is 16-dimensional at K = 0 and the identity at three random K: no mirror, copy or turn number exists for moving states; an exact one-body mirror number would leave the light sector a lattice theory by itself, vector-like by Nielsen-Ninomiya (1D witness: 20 random bands, net chirality 0). (C) SM singlets: none in the 10, one in the 16 (nu'^c, X = 5), two in the 45, one in the 54 (X = 0); 16 x 16bar = 1 + 45 + 210 and 10 x 10 = 1 + 45 + 54, so in the Spin(10)-symmetric phase nu'^c has zero photon and Z couplings to all orders in the mirror dynamics, while the 10's neutral members have T3 = +-1/2. (D) From the cited one-cell chains: the 10 (spin 0, X = +-2) at 19.07 g lies below the 16 (33.58 g), so the lightest mirror state is SM-charged and nu'^c (Delta_f) is the lightest SM singlet. Estimates against measurement use supplied inputs. Supplied model, finite diagnostic.

Statement and supporting text (copied from the note):

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its lead chirality route gaps the mirror family symmetrically (SMG) with a cell-local Spin(10)-singlet quartic, the pair square. Measured Higgs data already require that phase rather than the pair-condensed one (mirror-condensate-ew, PR #9974). This note asks whether that one mechanism also gives the dark matter: in an SMG phase every mirror excitation is a gapped composite, and the mirror might carry its own conserved number. The copy-sign note (dark-matter-candidate) found no stable link-free species in CL-1 to CL-3, because the copy sign is exact only at rest and copies share link charges. The question is whether SMG changes that. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

Repo check: origin/main has no note on mirror or SMG dark matter. The SMG hits are the Spin(10) atomic-gap note (2026-09-14) and the chirality endpoint-algebra note. Open PRs used: #9910 (one-cell pair-square spectrum, whose chains are cited here), #9974 (mirror condensate), #9877 and the copy-sign note (dark-matter slot), and #9985 (far-layer N_eff).

#### Statement

A. Symmetries of the mirror 16 with the pair square, species-diagonal hops and SM gauging.

1. Exact. Build Spin(10) on 2^5 modes and take M_a = C Gamma_a on the 16. M_a is symmetric, and sum_a M_a x M_a is Spin(10) invariant. The diagonal phases of the 16 weight states that keep all 40 pair-square monomials form U(1)^5, the Spin(10) torus, with no torsion.
2. Exact. SM gauging and species-diagonal hops commute with the six species numbers, U(1)^6. Of these, the pair square keeps exactly U(1)_Y x U(1)_X, with X = 5(B-L) - 4Y taking the values (1, 1, -3, -3, 1, 5) on (Q, u^c, d^c, L, e^c, nu^c). The Smith normal form has no torsion, so no discrete remnant exists beyond these two U(1)s. This answers "which U(1)s survive": one exact mirror number survives, U(1)_X, which at fixed Y is the mirror's B-L.
3. Exact. Mode number changes by 4 only, so Z4 = i^N survives. Every mode has X = 1 mod 4, so i^N = exp(i pi X/2): the Z4 is the Spin(10) centre and lies inside U(1)_X. It is not an independent protection. Mirror B' and L' are broken separately: L' fully, and 3B' only down to the Z3 that colour already contains. B'-L' is exact.
4. Exact. On one 16, the anomalies SU(3)^2 X, SU(2)^2 X, Y^2 X, Y X^2, X^3 and gravity-X all vanish. The mirror's X therefore also survives electroweak instantons.
5. Exact. Add the light family (a left 16) to the mirror (a right 16). Without mixing, the symmetry is U(1)^6 (light species) x U(1)_Y x U(1)_X(mirror), 8 dimensions. With any species-diagonal light-mirror bilinear, only U(1)_Y x U(1)_X(total) survives, 2 dimensions. The mirror's number is then the same symmetry as light B-L.

B. The update shares the mirror's number with light matter.

1. Finite diagnostic (rederives the copy-sign note's A5). Take the CL-1 cube tick at (b, mu, M) = (0.3, 0.4, 0.5). The one-body operators commuting with both half-ticks span 16 dimensions at K = 0: copy sign and turn labels are exact at rest. At three random K they span only the identity. No cell-local mirror, copy or turn number exists for moving states. The labels that pick out "the mirror" (the copy the three-fold turn rotates by e^(4 pi i/3), or the copy sign) are rest labels, so the tick is a light-mirror bilinear at nonzero momentum, and A5 applies.
2. Theorem (Nielsen-Ninomiya in a sector; 1D witness checked). Suppose an exact one-body mirror number existed. The light sector would then be a local lattice theory by itself, with exact charges, so it would be vector-like. The register also records that the mirror's zone-corner partners are gapped by the chiral generator only through light-mirror mixing. A separately conserved mirror number and a chiral light family therefore exclude each other in the present content.

C. Quantum numbers of the gapped spectrum.

1. Exact. SM-singlet content (colour, SU(2)_L and Y all zero):
   - 10: none.
   - 16: one, nu'^c, with X = 5 and B-L = 1.
   - 45: two, the Y and X generators.
   - 54: one, with X = 0.
2. Exact. 16 x 16bar = 1 + 45 + 210 and 10 x 10 = 1 + 45 + 54 (Casimir multiplicities). The 45 occurs once in each. In the Spin(10)-symmetric phase the hops and the pair square commute with Spin(10), so each band is a whole 16 or 10. By Wigner-Eckart, every gauge-current matrix element inside a band is one form factor times the generator's own eigenvalue.
3. Exact, then. nu'^c has T3 = Q = Y = 0. It therefore has zero photon and Z couplings to all orders in the mirror dynamics: no charge radius, magnetic moment or anapole in the Spin(10) limit. These are induced only at O(alpha/4 pi) by the gauge couplings breaking Spin(10). The 10's two neutral members have T3 = +-1/2, which is a vector Z coupling.

D. Which mirror state is lightest (atomic limit; chains cited from #9910).

1. The chains reproduce E0 = -2 sqrt(11088 + 48 sqrt 21081) g. The levels above it are:
   - the 10 (spin 0, X = +-2) at Delta_b = 19.07 g;
   - 16 + 16bar (spin 1/2) at Delta_f = 33.58 g;
   - the 54 at 42.33 g.
2. Finite. Delta_b/Delta_f = 0.568, and 2 Delta_b = 1.136 Delta_f. The lightest mirror excitation is therefore the 10, which is SM-charged (a Y = +-1/2 doublet pair and colour triplets, with no singlet). The lightest SM singlet is nu'^c at Delta_f. It lies below the two-cell 10 x 10 singlets (2 Delta_b, X = 0) and the 54 singlet, both of which carry no conserved number.
3. Finite. Suppose X were exact. Then each (X, mirror fermion parity, SM charge) sector's lightest state is stable. nu'^c cannot reach another 16 member, because Delta X = 4 costs at least 2 Delta_b, and the 10 is the absolute lightest mirror state. A Casimir term lambda C_Spin(10) raises the 16 faster than the 10 (C(16)/C(10) = 1.25), so it cannot lift the 10 above the 16. The 10 also softens toward the pair condensate as hopping grows (toy-qmc, qmc-face-gapped), which keeps it lightest.

#### Estimates against measurement

Supplied inputs: the unit map (1 rad/tick = 2.1e18 GeV); the Kolb-Turner freeze-out formula with sigma v = 4 pi kappa/m^2; the copy-changing vertex g >= 0.30 at recoil (from the copy-sign note) times a quasi-particle weight 1/sqrt2 (#9910 E1); the Z cross-section with xenon N/A; the bounds (approximate).

- Mass scale. With the pair square once per tick, #9910's window puts Delta_f near the cell scale. Mirror-condensate-ew needs at least about 1.5 TeV (symmetric phase, decoupled). The mass of nu'^c is Delta_f(1 + O(alpha/4 pi)), and the 10 lies at 0.57 Delta_f.
- With the laws as written (light-mirror mixing, B1), nu'^c -> nu^c + graviton gives tau ~ 3e6 s at 1.5 TeV, 50 s at 56 TeV and 1e-38 s at 1e18 GeV. Even the invisible bound (8e18 s) needs m < 0.1 GeV. Excluded at every gap. Every other mirror state decays to light states carrying the same total X (light B-L) at the cell rate.
- Thermal relic if the mirror number were exact. Strong annihilation gives Omega h^2 = 0.12 at m = 56 TeV (kappa = 1) or 18 TeV (kappa = 0.1). nu' nubar' -> 10 10bar is open, since 2 Delta_b < 2 Delta_f, so the relic is dominated by the stable 10s:
  - charged members (Q = +-1 and colour triplets) are stable CHAMPs or heavy hadrons, excluded;
  - the neutral complex doublet member has sigma_n ~ 6e-40 cm^2 through the Z, against about 1e-46 (m/TeV) cm^2. U(1)_X forbids the real/imaginary splitting that would remove this, so it is excluded below about 6e9 GeV.
  At the law-fixed cell-scale gap, a thermal mirror overcloses (Omega h^2 >~ 4e25 at 1e18 GeV, unitarity-limited).
- nu'^c itself would be a good WIMP-like state: its Z and photon couplings vanish (C3), and its self-interaction is 4 pi/m^3, about 2e-17 cm^2/g at 56 TeV. But it is never the lightest stable mirror state.
- N_eff. A gapped mirror has no massless state, so Delta N_eff = 0 below Delta, unlike the massless far layers (2.25, #9985). The empty-start condition becomes T_RH << Delta if the mirror is stable, and nothing if it decays.

[end of lines 19-68 of the note]

SMG does not change the copy-sign verdict. In isolation it does supply one exact, anomaly-free mirror number, U(1)_X, which contains the Z4 of the quartic. But:
- (i) the tick shares X with light B-L, because the mirror label is a rest label (B1), so every mirror state decays at the cell rate;
- (ii) keeping a separate mirror number would make the light sector vector-like (B2) and undo the doubler gapping, so it conflicts with the chirality route that the SMG mirror exists for;
- (iii) even with a supplied mirror number, the lightest stable mirror states are the SM-charged 10, not the neutral nu'^c.

Chirality and dark matter do not unify through the SMG mirror in the present content. What SMG does give for free is a neutral composite with exactly zero gauge couplings in the Spin(10) limit (C3).

[end of lines 72-77 of the note]

#### Notes used or contradicted

- smg-verify (#9910): its chains and spectrum are cited, and D1 rechecks them. Its Z4 is identified here as the Spin(10) centre inside U(1)_X (A3), and its E1 weight is used.
- dark-matter-candidate (copy sign): A5 is rederived (B1) and its vertex g is cited. Its verdict is extended to the SMG mirror, not contradicted.
- mirror-condensate-ew (#9974): the symmetric-phase requirement and the 1.5 TeV floor are used.
- gk-nogo-check (#9985): narrowed. Its Delta N_eff = 2.25 applies to a massless mirror; a gapped SMG mirror adds nothing below Delta.
- Register lines on the Z4 of mode number ("Z4 is the most that survives") and on the light-mirror mixing that gaps the corner partners: both are consistent. The Z4 sits inside the exact U(1)_X of the mirror alone.

#### Boundary

Exact: the representation theory, the lattice and Smith form of the species phases, the anomalies, and Wigner-Eckart.

Finite: the tick commutant at (0.3, 0.4, 0.5) and three K, and the atomic-limit ordering.

Cited: the so(12) chains and the copy vertex.

Not computed:
- the lattice SMG phase and its band minima (the 10's further softening is cited from the toy QMC);
- the sign of the gauge self-energy splittings inside the 16;
- three-family and cross-family mirror terms (these could reduce per-family X to the diagonal X);
- light Yukawa terms;
- graviton-coupling normalisation.

Literature: Spin(10) branching rules and the GUT X charge are standard. The freeze-out formula and the unitarity scale are standard approximations.

[end of lines 89-112 of the note]

(Omitted from the note: lines 1-18 and lines 69-71, 78-88, 113-121.)

### #10000: An unsplit block cannot inflate; the fold plateau needs order-carrying splits and dephased split phases to seed perturbations

- Branch `claude/toe-inflation-rule-20261021`, head `236819094e`; note `docs/AN_UNSPLIT_BLOCK_CANNOT_INFLATE_SO_THE_FOLD_PLATEAU_NEEDS_SPLITS_THAT_CARRY_ITS_ORDER_AND_DEPHASED_SPLIT_PHASES_TO_SEED_PERTURBATIONS_BOUNDED_THEOREM_NOTE_2026-10-22.md`.
- Runner: [`scripts/an_unsplit_block_cannot_inflate_so_the_fold_plateau_needs_splits_that_carry_its_order_and_dephased_split_phases_to_seed_perturbations_2026_10_22.py`](../scripts/an_unsplit_block_cannot_inflate_so_the_fold_plateau_needs_splits_that_carry_its_order_and_dephased_split_phases_to_seed_perturbations_2026_10_22.py); cache `logs/runner-cache/an_unsplit_block_cannot_inflate_so_the_fold_plateau_needs_splits_that_carry_its_order_and_dephased_split_phases_to_seed_perturbations_2026_10_22.txt`.
- Kind of statement: Mixed. Exact or closed-form statements (window arithmetic, dilation gauge, fixed-site bound, re-seeding, friction-blindness, adiabatic no-seed result, E2); finite diagnostics (computed potential and stiffness, synchronised-split heating, dephasing scan); estimates against measurement. Depends on a supplied nested-sea Hartree model with repulsion g, a rung fitted to A_s, instant reheating and a scanned dephasing spread.
- Dependencies: Uses PR 9979 (re-seeding, misfolds), PR 9982 (potential, friction, momentum-overlap statement; its potential and friction numbers are rederived here), PR 9986 (face phases stay fixed), PR 9918, the split-time cascade note (PR 9961), the record-clock note (PR 9966), inflaton A1 (cited by name). PR 10007 narrows the dephasing estimate D4 (see CORRECTIONS). The proposed clauses (order carriage, vacuum standard, dephasing) are the note's tests, not adopted laws.

Claim scope (verbatim):

> For the update law's tied lapse, edge-register window [L/8, 2^(1+Delta) L], 4s split trigger and passing (vacuum to vacuum, each excitation to the same), with the bare-axis-hop nested sea's Hartree density-wave fold (spinless NN repulsion g) as the plateau: (A) exact: an unsplit block's edges span (4+Delta) ln2 e-folds, so 60 e-folds need Delta >= 82.6; but with the tied lapse the plateau is V0 per site per tick, and read in the vacuum's own units aH stays constant (zero horizon exits for any stretch); with G fixed in proper units rho ~ a^-4. Generally a fixed site set with per-site energy ~ l^p (p <= 0) has w = -p/3 >= 0, so e-folds need new sites: 86.6 split generations during the plateau. (B) Without order carriage a split gives children zero overlap with the fold coordinate (x = 1): no exit, and no folded vacuum survives any later split. Carrying each order with its total momentum makes friction impulsive (mean drift 27 ln2/14), and the plateau attractor is friction-blind: P(N) = V0 N^2/(12 pi^2 mu^2) for any friction factor. (C) Computed V and cranking mass give n_s = 1 - 2/N; with the rung FITTED to A_s (18.4 at g = 0.5, 20.2 at g = 1), the matching condition gives N* = 46.8-47.4, so n_s = 0.957 (-1.8 sigma Planck, -5.6 sigma ACT+DESI), r = 5e-18, running -9e-4. (D) The register's passing is adiabatic for every mode and the tick is static in cell units, so the vacuum seeds no perturbation (superhorizon variance x1/4 per split; A_s = 0). Carrying the order field's configuration through synchronized splits gives |beta|^2 = 9/16 per sub-horizon mode per split and a ln2-periodic spectrum (first harmonic 1.3). With split phases dephased by sigma, the modulation is 0.81, 0.30 and 0.007 at sigma = 0.1, 0.2 and 0.35 e-folds, with mean power 1.2-1.3 times Bunch-Davies; the laws' Poisson estimate gives sigma = 0.07-0.10. (E) The amplitude mode at D* sits 1.19 times above the pair edge 2D*; the folded-vacuum standard gives the plateau departure V0. (F) The 4s trigger is untouched: H a = 2.3e-13. Supplied: g, the fold rung (FITTED to A_s), J a = sqrt3, M_P a = 1, Hartree, instant reheating, g_* = 106.75, mode speed 1, the dephasing sigma (scanned).

Statement and supporting text (copied from the note):

#### Where this starts

The fold-inflaton and nested-prefold-sea notes found three things:
- The density-wave fold of the bare-axis-hop (nested) sea is a Starobinsky-class plateau.
- A split cannot pass the fold, so the children are born unfolded.
- The friction needs CL-3's vacuum standard to be read from the folded vacuum.

The candidate tested first is: "the universe begins as one block with the pre-role nested sea, and no block splits until its fold completes", so that inflation happens inside one unsplit block and the passing problem never comes up. Measured values: n_s = 0.9649 +- 0.0042 (Planck), 0.974 +- 0.003 (ACT with DESI), A_s = 2.1e-9, r < 0.036.

#### A. The candidate fails for every Delta

**A1 [T]. Window.**
- An unsplit block's edges run from the floor to the top of the window, which is (4 + Delta) ln2 e-folds; from birth at flat length to the top it is (1 + Delta) ln2.
- At Delta = 0 that is only 2.77 e-folds. 60 e-folds would need Delta >= 82.6 (from the floor) or 85.6 (from birth), plus a new clause holding the 4s trigger.
- When the hold is released, children start at the parent's value minus s, which is still at least 4s, so 86 generations split in a burst.

**A2 [T]. Dilation gauge.**
- Under the tied lapse the tick's proper time scales with the cell, so the plateau is V0 per site per tick and rho ~ V0/l^4.
- Read in the vacuum's own units (CL-3, with M_P l = 1), G ~ l^2 and H l is constant. So aH is constant, and there are zero horizon-exit e-folds however far the edges stretch. Uniform stretching is the register's "uniform dilation is a common whole shift": pure relabelling.
- With G held fixed in proper units instead, rho ~ a^-4 (radiation), and aH falls by e^-60.

**A3 [T]. General no-go.**
- Take a fixed set of sites whose per-site energy scales as l^p, with p <= 0 for bounded energy per tick (p = -1 under the tied lapse). Then w = -p/3 >= 0, and acceleration needs w < -1/3.
- So e-folds need new sites: 60 e-folds are 86.6 split generations, and they must happen during the plateau.

Verdict: the unsplit-block rule cannot inflate. Bending the window or Delta does not help, so the passing problem cannot be avoided.

#### B. The split must carry the order

**B1 [T]. What happens without carriage.**
- Site-zone passing gives a parent staggered order zero overlap with the child's fold coordinate (integer overlap 0; nested-prefold E1). So x = 1, and q = 1/8 + 7x/8 = 1: de Sitter with no exit.
- After reheating, every later split would re-seed V0. So no folded vacuum, which is the vacuum CL-3 needs, survives even one split.
- Order carriage is therefore needed for the fold to exist at all as a lasting vacuum, not just for inflation.

**B2 [T+D]. Impulsive friction.**
- In cell units the tick is static between splits.
- If the split carries the order's total momentum, it divides the order's velocity by 8 at each split. The mean drift is then 3 ln2 (f/(1-f) + 1/2) with f = 1/8, which is 27 ln2/14 = 1.337 times -V'/3H (stepped check 1.338). This rederives nested-prefold D1.

**B3 [T]. The plateau is friction-blind.**
- With friction factor c, N = N_std/c and P = (dN/dchi)^2 H^2/4pi^2 = V0 N^2/(12 pi^2 mu^2) (sympy). This does not depend on c.
- So n_s(N), r(N) and A_s(N) are the same for impulsive and continuous friction, at leading slow-roll order.

#### C. Numbers from the computed potential

**C1 [T+D].** Rederived: the gap equation 1 = 3g int rho/E has a solution at every g > 0, the cranking pole is M -> rho0/(12 D^2) (rho0 = 0.14267), and W ~ D^2 ln^2(1/D). D* = 0.641 at g = 0.5 and 2.300 at g = 1.

**C2 [D]. Slow roll at N* = 55.** n_s = 0.9636 = 1 - 2/N. eps reaches 1 long before D*, which is the graceful exit.

**C3 [T+E]. Self-consistent N*.**
- Setup: instant reheating, k* = 0.05/Mpc, g_* = 106.75, the Planck-2018 matching formula.
- Results: N* = 47.4 (g = 0.5) and 46.8 (g = 1).
- The rung is FITTED to A_s: 18.4 and 20.2. Then H/M_P = 7.6e-13 and 2.3e-13.
- The low plateau shortens N*, and 55 is not available.

**C4 [E]. Predictions the rule was not built for** (at the self-consistent N*, g = 1):

| Quantity | Rule | Measured | Pull |
|---|---|---|---|
| n_s | 0.9572 | Planck 0.9649 +- 0.0042 | -1.8 sigma |
| n_s | 0.9572 | ACT+DESI 0.974 +- 0.003 | -5.6 sigma (excluded) |
| r | 5e-18 | < 0.036 | passes; prediction: no observable tensors |
| running | -9.1e-4 | -0.0045 +- 0.0067 | consistent |

Delayed or stiff reheating could add up to about 11 e-folds, which still falls short of ACT's N ~ 77.

#### D. Perturbations: a new wall and its rule

**D1 [T]. The register's passing seeds nothing.**
- The passing (vacuum to vacuum, each excitation to the children's lowest excitation of the same) maps every mode adiabatically: u -> u/2 and pi -> 2 pi in the instantaneous basis.
- Between splits the tick is static in cell units, so occupations never change. This is a conformally coupled field.
- Superhorizon variance therefore falls by 1/4 per split (2.3e-10 of Bunch-Davies after 16 splits), and A_s = 0 from the vacuum.
- This holds for the inflaton fluctuation under the register as written. It is the mechanism behind the predictions sheet's "scalar seed absent".

**D2 [D]. Order carriage with synchronized splits.**
- The continuum check (smooth a^3 weight) reproduces Bunch-Davies, R = 0.9999.
- Carrying the order field's configuration and total momentum through synchronized splits is sudden. It gives |beta|^2 = 9/16 per sub-horizon mode per split, which heats.
- The frozen spectrum is then 17 times Bunch-Davies on average and saw-toothed with period ln2 in ln k (first harmonic 1.30). That is excluded.

**D3 [D+E]. Dephased splits restore the continuum.** If block split phases are spread by sigma e-folds, a long mode sees the summed cell count:

| Phase spread | Mean power / Bunch-Davies | ln2-periodic modulation |
|---|---|---|
| sigma = 0.1 | 1.78 | 0.81 |
| sigma = 0.2 | 1.17 | 0.30 |
| sigma = 0.35 | 1.27 | 0.007 |
| uniform within one generation | 1.24 | 0.32 |

A modulation below the few-percent log-oscillation bound needs sigma of about 0.35 e-folds or more. The bound is approximate, from the Planck feature search; check it before citing. The rung shift log2(R)/2 is 0.17 or less.

**D4 [E]. The laws do not supply enough dephasing.** The Poisson register estimate (spectral-tilt, m s <= 2034) over the 22-42 levels since a Hubble patch's common ancestor gives sigma = 0.07-0.10, so a dephasing source is still needed.

#### E. Exit, reheating, vacuum standard

**E1 [E].** After exit the order oscillates about D*. The amplitude mode's frequency is 5.47, which is 1.19 times the pair edge 2D* = 4.60, so it can decay into the fold sea's quasiparticle pairs (fold-sea matter). Misfolds are at most 0.36 walls per site (fold-inflaton E). Rates are not computed.

**E2 [T].** With CL-3's vacuum read as the lowest state over orders (the folded vacuum), the plateau's departure is V0 (0.1673 per site at g = 1), and it is zero after exit. Lambda stays a separate supplied constant.

#### F. Trigger consistency (F1)

Under IN-1 the plateau rides the ordinary 4s trigger: one generation is s steps, which is ln2.
- H a = 2.3e-13 per finest tick, far below the edge-rate cap and inflaton A1's 1.93e-5.
- That is about 3e12 ticks per split, with 68 generations within N*.
- The window and Delta are unchanged.

[end of lines 15-117 of the note]

#### Rule text (proposed, tested)

> IN-1 (order carriage; amends CL-1's passing). "An update's vacuum is its lowest state at its block's orders: the orders are the site averages of the odds that the update's interaction makes nonzero, and the vacuum at given orders has every negative-quasi-energy mode of the tick, with the mean fields at those orders, filled. The passing carries a block's vacuum at its orders, and each order's total momentum, onto the children's vacuum at the same orders, read in the children's own cells."

> IN-2 (vacuum standard; CL-3 reading). "The vacuum CL-3 measures departures from is the update's lowest state over all orders."

> Pre-role sea (nested-prefold clause, kept). "While a block of rung r_f is unfolded, its role sites tick with the bare axis hop and nearest-neighbour repulsion g."

> IN-3 (dephasing). Needed, not supplied: split phases must be spread by at least about 0.35 e-folds within a Hubble patch. A candidate source is "the first odds spread each block's edge registers over one register octave". It is UNTESTED: a spread of one generation alone gives modulation 0.32 (D3), not enough, and whether the coupled trigger keeps or erases an initial spread is not computed.

[end of lines 119-127 of the note]

#### Smuggling review

Supplied:
- g, the fold rung (FITTED);
- J a = sqrt3;
- M_P a = 1;
- the Hartree reading;
- instant reheating and g_* = 106.75 (for N*);
- mode speed 1;
- the dephasing sigma (scanned; mean-field summed cell count as the long mode's inertia);
- the Poisson register model (D4 only).

Forced, given those:
- the window arithmetic;
- the dilation gauge and the fixed-site no-go;
- the B1 re-seeding;
- the 27 ln2/14 drift;
- friction-blindness;
- n_s = 1 - 2/N;
- N* of about 47;
- the adiabatic no-seed theorem;
- 9/16 heating per synchronized split;
- the D3 modulation numbers.

Not computed:
- the 3D star or fold selection;
- the coupling of the rung-r_f fold sea to finest-rung matter, and reheating rates;
- whether the coupled trigger keeps an initial phase spread;
- quantum diffusion near the top;
- the face-phase switch from the nested to the Dirac sea (nested-prefold B; not needed here, because the fold sea is a separate rung-r_f sea).

#### Dependencies

- Used: fold-inflaton (#9979; C5 re-seeding, E misfolds); nested-prefold-sea (#9982; C potential, D1 friction, E1 overlap); pi-flux-fold (#9986; face phases stay fixed, no Stokes issue); spectral-tilt (Poisson spread, n_s - 1 = log2 lam); record-clock-tilt (no record clock); act-tilt (#9918; every exponential plateau gives 1 - 2/N); inflaton A1.
- Narrows: the owner's candidate that inflation happens in one unsplit block (refuted, A), and the nested-prefold claim that the passing must "write the clock" (IN-1 is the vacuum clause completed, B1).

[end of lines 151-185 of the note]

(Omitted from the note: lines 118-118, 128-150, 186-192 and lines 1-14, i.e. front matter, derivation prose, run instructions and any candidate-rule checklist.)

### #10002: First slab fixes Lambda only at the Planck scale; a record-count multiplier gives a wrong sign or a drifting Lambda

- Branch `claude/toe-lambda-rule-2-20261021`, head `26a6cb069a`; note `docs/FIRST_SLAB_FIXES_LAMBDA_ONLY_AT_THE_PLANCK_SCALE_AND_A_RECORD_COUNT_MULTIPLIER_GIVES_A_WRONG_SIGN_OR_A_DRIFTING_LAMBDA_BOUNDED_THEOREM_NOTE_2026-10-22.md`.
- Runner: [`scripts/first_slab_fixes_lambda_only_at_the_planck_scale_and_a_record_count_multiplier_gives_a_wrong_sign_or_a_drifting_lambda_2026_10_22.py`](../scripts/first_slab_fixes_lambda_only_at_the_planck_scale_and_a_record_count_multiplier_gives_a_wrong_sign_or_a_drifting_lambda_2026_10_22.py); cache `logs/runner-cache/first_slab_fixes_lambda_only_at_the_planck_scale_and_a_record_count_multiplier_gives_a_wrong_sign_or_a_drifting_lambda_2026_10_22.txt`.
- Kind of statement: Mixed. Exact symbolic and counting results; finite diagnostics of a supplied minisuperspace window and hop kinetic; estimates against measured Lambda and DESI central values (a sign comparison only).
- Dependencies: Rebuilds the construction of PR 9947 (fixed lapse, one-cube sign; logged) and builds on PRs 9962 (logged), 9900 and 9876. Cited by 10018. Supplied window, hop kinetic, v_r = sig/2, Q = 4, power q and LambdaCDM numbers.

Claim scope (verbatim):

> Two size rules for the response law's constant Lambda per proper 4-volume, tested against Lambda L^2 = 7.15e-121 (L = sqrt(8 pi) l_P) and w = -1. (a) First-slab charge. Conserved totals of the laws (fermion number, Gauss charges) dilute as a^-3 (w = 0), and the tick's conserved quasi-energy has w = n/3 under lapse a^n, so 1/3 under the fixed lapse (symbolic). Only a quantity copied per cell at splits and carried per proper 4-volume is Lambda-like: the per-4-volume phase over a split is exactly conserved (8 x 2 x 2^-4 = 1), and a per-cell energy copied at splits is w = -1 only on average, with a factor-8 sawtooth (cascade, 10 cycles). Fixing Lambda by the one-cube start's mean-zero dark constant, Lambda = <K>/<v> (rebuilt construction of PR #9947), is split-stable and predicts Lambda > 0, w0 = -1 and wa = 0. With a closed window top the allowed set is Lambda L^2 >= 1.3e-3 to 9.6e-2, so the measured value is excluded, by 1e117 to 1e119. With a transparent top Lambda_min falls as (top)^-6 (slope -6.00), so the size is free; it would need a top near 1e20 L. A matter-filled first cube needs a cancellation to 9e-120 (fitted). (b) Fixed 4-volume per record. Record counts are exact (Fano 0), so no Sorkin fluctuation arises. A sharp integer count makes Lambda L^2 defined only modulo 4 pi/sig (581 to 2902), a Planck-sized circle with the point on it free. A fixed total count of the history needs a finite 4-volume, which forces Lambda <= 0 (wrong sign). A to-date count N gives N^-1/2 = 0.011 to 0.14 times the measured value and N^-1 ~ 1e-122 times it, with w0 from -0.58 to +0.32 and wa from +0.51 to +1.63. (c) A first-slab integer (Q = 4) per 4-volume to date gives 4e-240 and tracks. No rule fixes the size; the gate result is FAILURE. Supplied model, finite diagnostic: LambdaCDM (Planck 2018), the eps0 range, the window and hop kinetic, v_r = sig/2, Q = 4, and DESI DR2 central values for a sign comparison.

Statement and supporting text (copied from the note):

#### Statement

A. Which conserved quantity is Lambda-like.

1. The laws' conserved totals (fermion number, Gauss charges, and any total carried at a fixed energy per unit) dilute as a^-3, so w = 0. The tick's conserved quasi-energy under lapse a^n has w = n/3, so under the fixed lapse (n = 1) the dark constant is dark radiation (rederives PR #9947 item 1). The edge-pair totals n1 + n2 = 1 are labels, carrying no phase.
2. A quantity behaves as a cosmological constant only if it is copied per cell at splits and carried per proper 4-volume. Over a split, 8 children x 2 child ticks x 2^-4 of the 4-volume gives exactly 1, so the per-4-volume phase is conserved. A per-cell energy copied at splits but fixed per cell is w = -1 only on average: over a 10-cycle cascade the fitted w is -0.990, with a factor-8 sawtooth in each cycle. The laws' one carrier of this kind is CL-3's constant itself, and in each cube it is tied to the edge zero-point by the mean-zero dark constant, <K> = Lambda <v>. Edge terms are not subtracted.

B. The first-slab rule: Lambda is fixed by the one-cube start's mean-zero dark constant.

3. On the rebuilt construction of PR #9947 (window l/L = 2^(n/s - 3), hop kinetic, Dirichlet walls), the closed-top minimum is Lambda_min L^2 = 8.35e-2, 9.14e-2 and 9.56e-2 at s = 23, 50 and 113 (Delta = 0), and 1.30e-3, 1.42e-3 and 1.49e-3 at Delta = 1. The mean form admits every Lambda >= Lambda_min. The measured value lies below the allowed set by a factor of 1.8e117 to 1.3e119, so the rule EXCLUDES the measured size. It does not merely miss it.
4. With a transparent top, Lambda_min falls as (top length)^-6 (fitted slope -6.00 over tops of 2, 8 and 32 L). The start then fixes only the sign. The measured value would need a top of 1.1e20 L (8.5e-15 m), a length no law contains.
5. With matter in the first cube, Lambda <v> = <K> - <E_m>. Reaching the measured value needs <E_m>/<K> = 1 - 8.6e-120, which is initial-data tuning (FITTED).
6. The rule is split-stable. Every newborn cube is born at the flat length on the same register, so its constraint has the same Lambda_min, and nothing is kicked at splits. It predicts Lambda > 0, w0 = -1 and wa = 0.

C. Fixed 4-volume per record: Lambda as the multiplier of the record count.

7. Under CL-2 every site records once per half-tick, and splits go 1 -> 8, so the count is exact (Fano 0; one-cube start, 3 splits x 5 ticks: 46800 records, variance 0; seeded Poisson control Fano 0.999). A Sorkin-type dV4 ~ sqrt(N) has no source. Conjugacy with a sharp count leaves Lambda's value unconstrained; it does not give 1/sqrt(N).
8. With V4 = N v_r exactly, and v_r = (sig/2) L^4, the Lambda phase is (Lambda L^2) v_r N with N an integer. So Lambda L^2 is defined only modulo 4 pi/sig, which is 581 to 2902 over the eps0 range: a Planck-sized circle. The measured value is 1.2e-123 of a turn, and nothing picks a point on the circle. PR #9947 found no such circle when the 4-volume per record varies with the edges. It exists only under the dropped fixed-4-volume clause.
9. A fixed total record count for the whole history needs a finite total 4-volume. For Lambda > 0 the cascade's future 4-volume diverges, because splits never stop while H > 0 and the integral of e^(3Ht) dt diverges. A finite total therefore forces Lambda <= 0 and recollapse. The sign is wrong.
10. A to-date count, taken as records in the past cone or as the Hubble volume times the age, is horizon-tied and not conserved, so it is no first-slab charge. Today N is 9.4e241 to 4.7e242 (past cone) or 3.0e243 to 1.5e244 (Hubble volume x age). The rule Lambda L^2 = N^-q gives:
   - past cone, q = 1/2: 0.065 to 0.14 times the measured value; w0 = -0.34, wa = +0.51;
   - past cone, q = 1: about 1e-122 times it; w0 = +0.32, wa = +1.01;
   - Hubble volume x age, q = 1/2: 0.011 to 0.025 times it; w0 = -0.58, wa = +0.81;
   - Hubble volume x age, q = 1: about 1e-124 times it; w0 = -0.17, wa = +1.63.
   Every form drifts with wa > 0, opposite in sign to the DESI DR2 hint (about -0.75, -0.86).

D. Other.

11. A first-slab integer charge Q (Q = 4, the fermion number of a half-filled cube) spread over the 4-volume to date gives 3.9e-240, about 1e-119 of the measured value, and tracks as V4^-1.

#### Candidate rule tested (not adopted)

> "First-slab constant. Lambda is the value at which the one-cube start's mean dark constant vanishes; each newborn cube inherits it per proper 4-volume."

[end of lines 20-52 of the note]

#### Boundary

Not claimed: that no first-slab or unimodular rule exists. These are not computed: inhomogeneous edge modes, coherent many-cell edge states for the first slab (the block form gives b^-6, PR #9947), a self-consistent everpresent history, and closed recollapsing histories in detail. The DESI comparison is a sign test. Open: a law that picks a point on the Planck circle of item 8, or a transparent-top start whose top is fixed by a rule.

#### Supplied vs forced

Supplied: LambdaCDM and the measured values; the eps0 range; the window [L/8, 2^(1+Delta) L] and the hop kinetic; v_r = sig/2; Q = 4; the power q; and DESI central values.

Forced, given the laws:
- the a^-3 and n/3 laws;
- per-4-volume conservation at splits;
- Lambda_min > 0 and the (top)^-6 scaling;
- exact counts;
- the circle period;
- Lambda <= 0 for a finite global total;
- drift of every horizon-tied count.

#### Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records.
- [Candidate-law register](CANDIDATE_LAWS.md): CL-1's fixed lapse, window and split; CL-2's record per site per half-tick; CL-3's constant per proper 4-volume and mean-zero dark constant. Zero premise weight.
- Builds on the open PRs #9947, #9962, #9900 and #9876.

[end of lines 74-95 of the note]

(Omitted from the note: lines 53-73, 96-104 and lines 1-19, i.e. front matter, derivation prose, run instructions and any candidate-rule checklist.)

### #10005: No structure of the update protects a dark species

- Branch `claude/toe-dm-from-structure-20261021`, head `e6d1d55aeb`; note `docs/NO_STRUCTURE_OF_THE_UPDATE_PROTECTS_A_DARK_SPECIES_BECAUSE_THE_MIRROR_NUMBER_IS_SHARED_AT_EVERY_MOMENTUM_THE_BLOCK_PERIOD_BLOCKS_NO_COPY_DECAY_AND_THE_WINDOW_FLOOR_HOLDS_NO_ATOM_OR_REMNANT_BOUNDED_THEOREM_NOTE_2026-10-22.md`.
- Runner: [`scripts/no_structure_of_the_update_protects_a_dark_species_because_the_mirror_number_is_shared_at_every_momentum_the_block_period_blocks_no_copy_decay_and_the_window_floor_holds_no_atom_or_remnant_2026_10_22.py`](../scripts/no_structure_of_the_update_protects_a_dark_species_because_the_mirror_number_is_shared_at_every_momentum_the_block_period_blocks_no_copy_decay_and_the_window_floor_holds_no_atom_or_remnant_2026_10_22.py); cache `logs/runner-cache/no_structure_of_the_update_protects_a_dark_species_because_the_mirror_number_is_shared_at_every_momentum_the_block_period_blocks_no_copy_decay_and_the_window_floor_holds_no_atom_or_remnant_2026_10_22.txt`.
- Kind of statement: Exact or finite diagnostics (commutant dimensions at chosen momenta, Smith normal form on an integer phase lattice, connectivity scans of one tetrahedron's register) and estimates against measurement; the mirror pair-square group is cited, not recomputed. Depends on supplied (b, mu, M), s, Delta, b_e, the stiffness scan and the unit map.
- Dependencies: Cites PR 9988 (mirror pair-square group U(1)_Y x U(1)_X, which in turn depends on PR 9910 in chirality-doublers and PR 9974 in families-flavour), PR 9963 (copy-sign vertex, recomputed here), PR 9991 and PR 9996; all four are in this theme and logged. Names PR 9847 as an open dark-matter PR (not assigned to any theme).

Claim scope (verbatim):

> Searches the structure CL-1 to CL-3 already have, with no added parity, for a protected dark species. (a) The cube tick's one-body commutant is 16 at K = 0 and at the zone corner pi(1,1,1), 8 on the diagonal 0.7(1,1,1), 4 at a random K, and 1 jointly over these and three random K: no number beyond species number is kept for moving states. On the integer species-phase lattice of a light 16 plus a mirror 16 (the mirror's pair-square group U(1)_Y x U(1)_X cited), the dark subgroup (trivial on every light mode) is U(1)^2 without a light-mirror pairing and trivial with the species-diagonal pairing in either form (Smith normal form, no torsion); every light mode has X = 1 mod 4, so U(1)_X and its Z4 are carried by light states. (b) The copy sign commutes with the tick at K = 0 only (7e-16 against 0.524); the traceless strain vertex is 0 at q = 0 and 0.297 at q = 0.87 M; a block half-tick is b_e cube half-ticks and edges repeat every b_e cells, so quasienergy and momentum are kept only mod 2 pi/b_e, and the light band (width 1.642 on 8^3 at (b, mu, M) = (0.3, 0.4, 0.5)) and M exceed 2 pi/b_e for b_e >= 40: no kinematic block on the heavy copy's decay. (c) On a regular tetrahedron's edge register (s = 2, Delta = 0, 8849 positive-volume states, one component) the all-floor state is connected to the flat state; under the register hop it leaves the floor (mean return 0.018); a quadratic departure bowl traps it in continuous time (0.45) but not in the per-tick form (at most 0.278 over six stiffnesses, below 0.1 at stiffness >= 2); splits start children at flat. (d) A floor remnant would weigh (b_e sqrt(8 pi)/16) M_Pl (12.5 M_Pl at b_e = 40), carries no number, and from the measured A_s has collapse fraction exp(-2.4e8) against the 1e-27 needed. The anti-smuggling gate result for the one rule considered (a floor lock) is FAIL. Supplied model, finite diagnostic: (b, mu, M), s, Delta, b_e, the stiffness scan, the mirror group, the unit map, the graviton-width coefficient, A_s, n_s, delta_c, g*, T_eq.

Statement and supporting text (copied from the note):

#### Question

The dark-parity note (AX-5) failed the anti-smuggling gate: its abundance was fitted and its one-family form names nu^c. This note looks for a dark species protected by structure the laws already have, with no added parity, and an abundance the laws fix. It tests four places:
- (a) a conserved charge of the update that no light state carries: the mirror's X = 5(B-L) - 4Y together with the light-mirror pairing, at every momentum;
- (b) copy-sign states at rest, whose decay needs momentum transfer: is that transfer suppressed by the block or window structure?
- (c) a minimum-size atom of geometry held by the window floor, and gravitational bound states;
- (d) black-hole remnants that the floor stops from evaporating.

Repo check: origin/main has no note on remnants, maximons or floor-stabilised relics. The open dark-matter PRs are #9877 (link-free slot), #9963 (copy sign), #9988 (mirror), #9991 (fold defects) and #9847. The register's dark-matter line already gives the primordial-hole collapse fraction exp(-2.4e8) from the measured amplitude; this note uses it for remnants.

#### Results

##### A. A charge carried by no light state

**A1 [F].** Take the cube tick at (b, mu, M) = (0.3, 0.4, 0.5). Its one-body commutant has dimension:
- 16 at K = 0;
- 16 at the zone corner pi(1,1,1);
- 8 on the diagonal at 0.7(1,1,1);
- 4 at a random K;
- 1 jointly over all of these and three random K.

A charge kept by moving states must commute at every K. So the corner pairing does not leave a mirror-number combination conserved. The corner commutant is as large as the rest commutant, but the two do not survive together with any generic K. This rederives and extends the mirror note's B1.

**A2 [T].** Take the integer lattice of species phases for a light 16 plus a mirror 16. The mirror's own pair-square group, U(1)_Y x U(1)_X with no torsion, is cited from the mirror note.
- Without a light-mirror pairing, the dark subgroup (the part acting trivially on every light mode) is U(1)^2: the mirror's own Y' and X'.
- With the species-diagonal pairing, in the form psi^dag psi' or psi psi', the dark subgroup is trivial, and the whole group is U(1)^2 = Y and X(total). Smith normal form; no torsion.

A1 says the tick supplies that pairing at nonzero K.

**A3 [T].** Every light mode has X = 1 mod 4, and i^N = exp(i pi X/2). So U(1)_X and its Z4 are carried by light states; the lightest carrier is the neutrino, with X = -3. CL-1's species mode numbers are carried by each species' light copy at rest.

Therefore no charge of the update is absent from the light states, and (a) gives no dark species.

##### B. Copy-sign states at rest

**B1 [F].** The copy sign commutes with the tick at K = 0 (7e-16) and not at a random K (0.524). The rest phases are mu + M for s = -1 and mu for s = +1.

**B2 [F].** The traceless one-cube strain vertex, heavy copy at rest to light copy at recoil q, is 6e-10 at q = 0, 0.038 at 0.1 M and 0.297 at 0.87 M. This recomputes the copy-sign note's A6.

**B3 [T+F].** This item is new: the block period gives no kinematic protection.
- A block half-tick is b_e cube half-ticks (CL-3 text), and the edge lattice repeats every b_e cells. So the full update keeps quasienergy only mod 2 pi/b_e per cube tick, and crystal momentum only mod 2 pi/b_e per cell.
- The light copy's positive band spans [0.400, 2.042] on the 8^3 grid, a width of 1.642. Both this width and M = 0.5 exceed 2 pi/b_e (0.157, 0.063 and 0.006 at b_e = 40, 100 and 1000).
- The folded light band therefore covers the whole quasienergy circle. For any edge-quantum energy and momentum, some light final state is resonant through umklapp.

Both energy and recoil can be absorbed by the block structure. Exactness at rest suppresses no decay.

**B4 [E].** With the graviton width g^2 M^3/(32 pi Mbar^2) at the O(1) vertex:
- at the law's M (one constant for every species, about 1.1e18 GeV) the heavy copy lives 4e-39 s;
- tau = 4e6 s at 1 TeV;
- tau > 8e18 s needs M < 82 MeV, which a heavy electron copy excludes.

Result: (b) gives no dark species.

##### C. A geometry atom at the window floor

**C1 [F].** Take a regular tetrahedron's six edge registers (s = 2, Delta = 0, values 0 to 8, length 2^(n/s - 3) of flat). They have 8849 of 531441 positive-volume states in one component. The all-floor state, every edge at 1/8 of flat, lies in that component, so no floor geometry is frozen.

**C2 [F].** Under the register hop, the floor state leaves the floor. Over t = 50 to 200 its mean return probability is 0.018, and the weight on the floor shell (sum n <= 2) is 0.038.

**C3 [F].** A stiff departure cost, here a quadratic bowl lambda sum((n - 3s)/s)^2 standing in for CL-3's departure phase, can trap the floor state by energy isolation. That is a doublon-like effect, not a conserved number.
- In continuous time at lambda = 1 the return is 0.45.
- In the update's own per-tick form (hop, then phase lambda V per block tick) the phase folds mod 2 pi. The return is 0.065, 0.145, 0.278, 0.085, 0.085 and 0.034 at lambda = 0.25, 0.5, 1, 2, 3 and 2 pi.

The trap is therefore at most partial, depends on a supplied stiffness, and fails at large stiffness. No robust floor atom exists in one tetrahedron. Decay into neighbouring cells, which can only add channels, was not computed.

**C4 [T].** A split fires at mean edge value 4s, twice the flat length, and each child edge takes the parent value minus s, exactly half the length (checked to 1e-15). Children therefore start at flat, and the split cascade makes no floored cells: the law-fixed abundance of floor atoms from splits is zero.

**C5 [T+E].** A two-body gravitational atom has Bohr radius r_B = 2 l_P (M_Pl/m)^3. It is resolved above the floor edge b_e a/8 (25 l_P at b_e = 40) only for m < 0.43 M_Pl (b_e = 40), 0.32 M_Pl (100) or 0.15 M_Pl (1000). Its constituents must already be stable and dark, and a particle-antiparticle pair annihilates. So a bound state adds no protection.

##### D. Remnants stopped by the floor

**D1 [T+E].** A horizon fits a floor edge when r_s = 2GM = l_floor = b_e a/8 with a = sqrt(8 pi) l_P. That gives M_rem = (b_e sqrt(8 pi)/16) M_Pl:
- 12.5 M_Pl (2.7e-4 g) at b_e = 40;
- 31 M_Pl at b_e = 100;
- 313 M_Pl at b_e = 1000.

b_e is only bounded below (about 40 or more), so this mass is supplied, not fixed. At M_rem the Hawking temperature (4e16 GeV at b_e = 40) lies below the block band top pi/b_e (2e17 GeV). Emission is therefore not band-cut before the floor is reached.

**D2 [T].** An edge register keeps nothing: the commutant of {hop, value} is 1. The floor state is connected to flat (C1). A floor-size lump therefore carries no number. The floor removes the horizon (r_s < l_floor) rather than stopping the loss of mass, and the lump's energy can leave as edge and matter quanta.

**D3 [E].** Holes with M_i ~ M_rem form at T_f = 5.9e17 GeV, from the horizon mass in the radiation era (b_e = 40). For their remnants to be all the dark matter, the collapse fraction must be beta ~ (T_eq/T_f)(M_i/M_rem) = 1.1e-27. The measured A_s gives:
- with the tilt set to n_s = 1, sigma^2 = (16/81) A_s and delta_c = 0.45, so ln beta = -2.44e8;
- with the measured tilt carried over the 62 e-folds of scale, ln beta = -2.1e9.

The power needed is P_R = 8.3e-3, about 4e6 A_s. The abundance is supplied, not fixed.


[end of lines 22-107 of the note]


None of (a) to (d) gives a dark species from structure the laws already have:
- (a) every conserved charge is carried by light states;
- (b) the block period gives no kinematic suppression;
- (c) the floor holds no robust atom, and splits make none;
- (d) a floor remnant has a supplied mass, no protecting number and a negligible abundance under the measured spectrum.

This extends the copy-sign, mirror and fold-defect notes and agrees with the AX-5 conclusion: a stable dark species still needs a conserved number the laws do not contain. Dark matter stays open (owner decision 2).

[end of lines 109-116 of the note]

#### Smuggling review

Supplied:
- (b, mu, M) = (0.3, 0.4, 0.5);
- s = 2 and Delta = 0 for the tetrahedron (the register needs s >= ~135);
- the bowl stiffness scan, which stands in for CL-3's departure phase and is not derived from the Regge part;
- b_e = 40, 100 and 1000;
- the mirror pair-square group (cited);
- the unit map;
- the graviton-width coefficient;
- A_s, n_s, delta_c = 0.45, g* = 106.75 and T_eq = 0.8 eV.

Forced, given these:
- the trivial joint commutant;
- the trivial dark subgroup under the pairing;
- the light carriers of X and Z4;
- rest-only copy exactness and the O(1) vertex at recoil;
- quasienergy and momentum kept only mod 2 pi/b_e (from the block-tick clause);
- connectivity of the floor to flat;
- children at flat;
- M_rem proportional to b_e;
- no register number.

Not derived:
- the lattice (many-cell) decay rate of a stiff floor configuration;
- the true CL-3 stiffness per register step;
- Hawking emission on the register lattice itself;
- production of floor states at reheating, which is Boltzmann-suppressed by the cell-scale energy against a supplied T_RH.

#### Notes used or contradicted

- Copy-sign note (dark-matter-candidate): A5 and A6 are recomputed (A1, B1, B2). B3 adds the block-period umklapp.
- Mirror note (PR #9988): its pair-square group is cited; its B1 is extended to the zone corner and joint K (A1); its "shared with light B-L" is made exact on the phase lattice (A2).
- Fold-defect note (PR #9991): its zero-Kibble-Zurek passing argument is paralleled for floored cells (C4).
- AX-5 note: its gate failure stands. This note finds no structure-based replacement.
- Floor-horizon and window-fix: the floor 1/8 and the window are used as written.
- Register dark-matter line: the primordial-hole fraction exp(-2.4e8) is reproduced and applied to remnants (D3).

[end of lines 128-164 of the note]

(Omitted from the note: lines 108-108, 117-127, 165-173 and lines 1-21, i.e. front matter, derivation prose, run instructions and any candidate-rule checklist.)

### #10007: Born split times are white inherited offsets and the passing leaves no remainder, so no law seeds curvature

- Branch `claude/toe-seed-rule-20261021`, head `a2e45add26`; note `docs/BORN_SPLIT_TIMES_ARE_WHITE_INHERITED_OFFSETS_AND_THE_PASSING_LEAVES_NO_REMAINDER_SO_NO_LAW_SEEDS_CURVATURE_BOUNDED_THEOREM_NOTE_2026-10-22.md`.
- Runner: [`scripts/born_split_times_are_white_inherited_offsets_and_the_passing_leaves_no_remainder_so_no_law_seeds_curvature_2026_10_22.py`](../scripts/born_split_times_are_white_inherited_offsets_and_the_passing_leaves_no_remainder_so_no_law_seeds_curvature_2026_10_22.py); cache `logs/runner-cache/born_split_times_are_white_inherited_offsets_and_the_passing_leaves_no_remainder_so_no_law_seeds_curvature_2026_10_22.txt`.
- Kind of statement: Mixed. Exact statements (A1, B1 to B3, the odds statement in C1); finite diagnostics in supplied toys (1D raw-passing toy, 32^3 coupled-trigger lattice, 10^3 staggered sea); estimates against measurement. Depends on supplied register-odds readings, Gaussian offsets and the numbers N* = 46.8, H l_c = 2.3e-13 and the dephasing requirement from PR 10000.
- Dependencies: Uses PR 10000, PR 9961 (cascade theorem, Poisson model, trigger edges), PR 9966 (records never condition the odds; quantile transport) and the register's split, passing and junction text, which the note cites as a document (CANDIDATE_LAWS_v3) not present in `ref/`. It narrows part B of PR 9961 and estimate D4 of PR 10000 (see CORRECTIONS). The proposed rules SE-1 and SE-2 are tests, not adopted laws; the note reports that neither produces A_s near 2.1e-9 with n_s between 0.965 and 0.974.

Claim scope (verbatim):

> For the update law's split and passing (eight children; edges along parent edges take the parent's value minus s, other registers start as in the children's vacuum; the nearest unitary carrying the update's vacuum onto the children's vacuum and each excitation onto the children's lowest excitation of the same charges, flux and momentum; the trigger on the cube's 18-edge mean at 4s with each unsplit +x, +y, +z face neighbour's shared-face edges full) and the actuality law (fewest-change transport, records never conditioning the odds): (A) the clause's remainder is zero for every mode, edge registers included, so A_s = 0 and P_t = 0 at linear order; the raw passing before the clause is no small squeezing: in a 1D free-fermion toy it leaves 0.62 excitations per parent site, fidelity e^(-1.27 per site), and a white density structure factor (1/16 at Q -> 0); a mode carried by its configuration gets |beta|^2 = 9/16. (B) The quantile transport keeps each register's Born quantile, and value-minus-s keeps it through the passing, so split-time offsets are inherited, never redrawn (1/4 of a child's trigger edges inherited: 6 on even, 3 on odd children); the block-mean offset is stationary at sigma_r/sqrt18 over 40 generations, the field is white (coarse variance ~8^-j), and as a curvature seed it gives Delta^2 ~ (k l)^3, about 1e-99 at the pivot. The coupled trigger DAMPS the spread (x0.43 on a 32^3 lattice with shared edges; always waiting for the face would amplify x2.4). Split phases spread by 0.35 e-folds would need Gaussian register odds of sd >= 4.9 s steps, more than half the (4+Delta)s window; the pair vacuum, the one-step floor and the own-hop window vacuum give 0.0002-0.065 e-folds, leaving the ln2 sawtooth (modulation 0.94-0.96). (C) Record picks seed nothing through odds; read through actual occupations they carry the vacuum's own density correlator, S(Q) -> Q^2 on a gapped staggered sea, so n_s - 1 = +4. (D) A mode-resolving passing threshold keeps the sawtooth (0.34-0.77) and its power depends on the chosen threshold; even with a supplied 0.35 dephasing and the inflation-rule's order carriage, A_s needs the FITTED rung, n_s = 0.957 (-5.6 sigma ACT+DESI) and r = 0. Supplied: Delta = 1, s = 23 and 135, the three register-odds readings, Gaussian offsets, the 1D raw-passing toy, a 10^3 staggered sea with mass 0.5, the inflation-rule's N* = 46.8 and H l_c = 2.3e-13, its mode model and dephasing requirement.

Statement and supporting text (copied from the note):

#### Where this starts

The inflation-rule note found a new wall, D1: the passing carries vacuum to vacuum, so it seeds no perturbation and A_s = 0. Synchronised splits under order carriage (IN-1) give an excluded ln2 sawtooth, and removing it needs split phases dephased by about 0.35 e-folds or more. The laws were estimated to give 0.07-0.10, but only through a supplied Poisson register model. The spectral-tilt note showed that a self-similar split-time cascade gives n_s = 1, and the record-clock-tilt note showed that a record clock gives no tilt. This note tests three candidate seeds that the laws might already contain:
- (a) the passing's quantum remainder;
- (b) Born randomness of split times, computed from the registers' own odds;
- (c) Born picks of new sites' first records.

The goal is near-scale-invariant curvature with A_s ~ 2.1e-9 and n_s ~ 0.965-0.974, from a rule in site, possibility, record and update terms only.

#### A. The passing's remainder (candidate a)

**A1 [T].**
- A mode carried by its configuration through a split (M -> 8M, w -> w/2, so M w x4) gets |beta|^2 = ((2 - 1/2)/2)^2 = 9/16.
- The clause as written takes the unitary nearest the raw passing that carries the vacuum onto the children's vacuum and each excitation onto the children's lowest excitation with the same charges, flux and momentum. That unitary has remainder 0 for every mode by construction, edge registers included.

**A2 [D]. 1D free-fermion toy of the raw passing.** Each corner mode is shared evenly over two children, and the other modes start as in the children's vacuum (reduced state). For N_p = 16 to 128:
- fidelity with the children's vacuum is e^(-1.27 N_p);
- there are 0.618 excitations per parent site;
- the density structure factor tends to 1/16 as Q -> 0 (white), where the children's vacuum has S ~ Q/2pi.

So the nearest-unitary step is load-bearing, not a small correction. The register's own junction note already says a local passing that falls short lowers transmission rather than heating.

**A3 [T+E].** Candidate (a) therefore gives one of two things:
- nothing, with the clause as written: A_s = 0 and P_t = 0 at linear order;
- without the clause, white UV heating of O(1) quanta per site per split: Delta^2 ~ (k l)^3, n_s - 1 = +3, and (k l)^3 is about 1e-99 at the pivot (k l ~ H l_c e^-N*).

It never gives a small, scale-invariant squeezing.

#### B. Born split times from the registers' own odds (candidate b)

**B1 [T]. Offsets are inherited.**
- On a register line, the fewest-change transport keeps the actual value at a fixed Born quantile u. On a translating packet the offset from the mean is constant (0.023 steps of binning drift over 37 steps).
- The passing's "value minus s" shifts the odds rigidly, so it keeps every quantile.
- So a split-time offset is inherited, never redrawn. Spectral-tilt's Poisson model redrew every step; the laws' transport does not.

**B2 [T]. Three readings of a register's odds.** The per-register spread is sigma_r = ln2 sigma_n / s e-folds.

| Reading | sigma_n | s = 23 | s = 135 |
|---|---|---|---|
| R0, one-step floor | 1/sqrt12 | 0.0087 | 0.0015 |
| R1, pair vacuum (each partner pair bonding, n binomial) | sqrt((4+Delta)s)/2 | 0.162 | 0.067 |
| R2, own-hop vacuum on the window | 0.1808 (4+Delta)s | 0.637 | 0.628 |

**B3 [T]. Inheritance geometry.** Of a child cube's 18 trigger edges (12 axis edges and the 6 even-corner face diagonals), the ones along parent edges number 6 on even children and 3 on odd ones, a mean of 4.5 (1/4). The rest start fresh.

**B4 [D]. No accumulation.**
- Over 40 generations of one lineage, the block-mean offset stays at sigma_r/sqrt18 (0.237 at generation 1, 0.231 at generation 40). The parent-child correlation is 1/4.
- A redraw-per-generation model random-walks (x6.3 over the same 40 generations).

**B5 [D]. The coupled trigger damps the spread.** The test lattice is 32^3 blocks with shared edges. A block splits when its own 18-edge mean reaches 4s and, for each UNSPLIT +x, +y, +z neighbour, the five shared-face edges are all full (the least fixed point of T = max(own, max_n min(T_n, F_n))).
- Coupled spread: 0.102 sigma_r, against 0.236 for the own mean alone (x0.43; mean delay 0.93 sigma_r). A neighbour that has already split lifts its condition, so late faces are skipped.
- A variant that always waits for the face would amplify the spread (x2.42).
- Coarse-grained over 2^j blocks, the variance falls as 8^-j: the field is white.

**B6 [D+E]. Dephasing is not supplied.**
- IN-3 needs split phases spread by about 0.35 e-folds or more (inflation-rule D3). The coupled spread is linear in sigma_r, so this needs Gaussian register odds with sd >= 4.94 s steps. That is more than half the 5s window (at Delta = 1), which no odds on the window reach.
- The readings give sigma_split = 0.0002-0.065 e-folds.
- With the inflation-rule's mode model, the ln2-periodic modulation is 0.94 (R2) and 0.96 (R1), with mean power 2.6 and 6.8 times Bunch-Davies. The sawtooth stays.

**B7 [T+E]. The offsets can dephase, but they never seed.** As a curvature seed the white offset field gives Delta^2 ~ (k l)^3, n_s - 1 = +3, negligible at the pivot. The Poisson cascade's n_s = 1 assumed redraws that the quantile transport does not make.

#### C. Born picks of new sites' first records (candidate c)

**C1 [T+D].**
- Records never condition the odds, so a response that reads odds sees no record seed (exact).
- If a source read the recorded occupations instead, the Born picks would carry the vacuum's own density correlator. On a gapped staggered sea (10^3, mass 0.5), S(Q) -> Q^2 (local power 1.75 at the two smallest Q). So Delta^2 ~ Q^5 and n_s - 1 = +4.
- A gapless 1D sea gives S ~ Q.

#### D. Seed rules against the gate

**D1 [D]. SE-2 (mode-resolving passing).** Proposed text: "the passing carries a mode vacuum to vacuum when the children's tick turns it by more than th per generation, and by its configuration otherwise." With synchronised splits, the power is 0.87, 0.96 and 1.84 times Bunch-Davies at th = 1, pi and 2pi, with ln2 modulation 0.34, 0.59 and 0.77. The power depends on the chosen threshold, and the sawtooth stays. SE-2 still needs dephasing, so it adds a clause and solves nothing.

**D2 [E]. Even with dephasing supplied.** Grant a supplied dephasing of 0.35 or more (IN-3), together with IN-1 order carriage. The seed is then Bunch-Davies times 1.2-1.3 (inflation-rule D3), and:
- A_s = R V/(24 pi^2 eps M_P^4), with the rung FITTED;
- n_s = 1 - 2/N* = 0.9573 (-1.8 sigma Planck, -5.6 sigma ACT+DESI); a constant dephasing adds no tilt;
- edge registers pass vacuum to vacuum, so r = 0.

#### Rule text tested

> SE-1 (Born dephasing; a reading of CL-2 and the split, with no new text). "A block's split time is read from the actual values of its edge registers, each a Born quantile of its odds; the passing keeps the quantile of every edge along a parent edge, and fresh registers take fresh quantiles."

> SE-2 (mode-resolving passing; new CL-level text). "The passing carries a mode vacuum to vacuum when the children's tick turns it by more than th per generation, and carries its configuration and momentum otherwise."

[end of lines 15-96 of the note]

#### What the measurement now demands (not claimed derived)

- A horizon-correlated seed. Every Born or record source the laws contain is local and kept (white). Only the modes themselves carry correlations at the horizon scale, and the vacuum clause removes their squeezing.
- A route that remains open (UNTESTED): smooth expansion inside a block. If the edge stretching between splits were not a pure dilation in cell units (the tied lapse makes it one), then a mode carried by its configuration would be pumped continuously, and no dephasing would be needed. That requires a rule under which the tick is not static in cell units between splits. This bends the dilation-gauge result of inflation-rule A2.
- A_s still needs the plateau height in Planck units from a rule for the fold rung, and n_s >= 0.965 needs N* > 57 or a non-exponential plateau.

[end of lines 117-121 of the note]

#### Smuggling review

Supplied:
- Delta = 1 (the AX-4 value, FITTED there);
- s = 23 and 135;
- the three register-odds readings and Gaussian offsets;
- the 1D raw-passing toy and its reduced-state reading of "start half filled as in the children's vacuum";
- the 10^3 staggered sea with mass 0.5;
- from the inflation-rule note: N* = 46.8, H l_c = 2.3e-13, the mode model (summed cell count) and the 0.35 dephasing requirement (approximate).

Forced, given those:
- the zero remainder of the clause and 9/16 for configuration carriage;
- the O(1) raw remainder;
- quantile inheritance and 1/4 inheritance;
- stationarity and whiteness;
- damping by the coupled trigger;
- the impossibility of 0.35 dephasing on the window for Gaussian odds;
- the record correlator ~Q^2.

Not computed:
- the edge register's odds under the CL-3 response during stretching (the true sigma_n);
- held edges and positive-volume restrictions in the coupled trigger;
- the correlated pair of child edges along one parent edge, in the lattice test;
- non-Gaussian odds;
- the 3D raw passing;
- the second-order tensor readout.

#### Dependencies

- Used:
  - inflation-rule (#10000): D1-D3, the mode model, N*, IN-1;
  - spectral-tilt: cascade theorem, Poisson model, trigger edges;
  - record-clock-tilt: records never condition the odds; quantile register transport;
  - the register's split, passing and junction text (CANDIDATE_LAWS_v3).
- Narrowed:
  - spectral-tilt B (its Poisson redraws are not the laws' transport; the laws make split-time offsets white);
  - inflation-rule D4 (the laws' dephasing is 0.0002-0.065, not 0.07-0.10, and the coupled trigger damps it).

[end of lines 123-159 of the note]

(Omitted from the note: lines 97-116, 122-122, 160-166 and lines 1-14, i.e. front matter, derivation prose, run instructions and any candidate-rule checklist.)

### #10018: Records on change are frozen in the half-filled sea; everpresent histories fail the early bounds

- Branch `claude/toe-everpresent-lambda-20261021`, head `73447fee15`; note `docs/RECORDS_ON_CHANGE_ARE_FROZEN_IN_THE_HALF_FILLED_SEA_SO_A_RECORD_COUNT_LAMBDA_HAS_NO_POISSON_SOURCE_AND_EVERPRESENT_HISTORIES_FAIL_THE_EARLY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-10-22.md`.
- Runner: [`scripts/records_on_change_are_frozen_in_the_half_filled_sea_so_a_record_count_lambda_has_no_poisson_source_and_everpresent_histories_fail_the_early_bounds_2026_10_22.py`](../scripts/records_on_change_are_frozen_in_the_half_filled_sea_so_a_record_count_lambda_has_no_poisson_source_and_everpresent_histories_fail_the_early_bounds_2026_10_22.py); cache `logs/runner-cache/records_on_change_are_frozen_in_the_half_filled_sea_so_a_record_count_lambda_has_no_poisson_source_and_everpresent_histories_fail_the_early_bounds_2026_10_22.txt`.
- Kind of statement: Mixed. An exact theorem conditional on a site-diagonal antiunitary reversing each half-tick (A1) with finite checks on 1D rings N = 8, 10, 12; finite diagnostics for the collective counts; a computed prefactor under supplied conjugacy and unit conventions (B); history ensembles of a supplied S/V dynamics with approximate BBN and CMB bounds (C); estimates against measurement.
- Dependencies: Uses PR 9876 (the 3D block-tick instance of the antiunitary, 8^3 torus, on which this note relies; magnitudes compared in CORRECTIONS item 2), PR 10002 (exact counts, Planck circle, drift), PR 9962 (Sorkin variant overshoots and tracks; logged), and the neighbourhood-roles probe (not in this theme). The candidate rules it tests (record on change, a Born coin per site and half-tick, random records at splits) are not adopted; per the note, the first gives no vacuum records and the Lambda from counts is at most 5e-31 of measured, and the second overshoots by 6.7 to 14.9 and makes every history crunch at coin odds 1/2. The frozen-vacuum statement is for the ticks checked, without a copy mass; the copy-massed tick moves in the patch computation of PR 9923 (CORRECTIONS items 2 and 3).

Claim scope (verbatim):

> Tests record-count rules meant to give the Poisson counts an everpresent (Sorkin-type) Lambda needs. (a) Record on change, where a site records only when its actual occupation changes. If a site-diagonal antiunitary reverses both half-ticks, the half-filled sea has equal odds at both half-ticks. The fewest-change transport is then the identity, so record-on-change makes zero vacuum records (count 0, variance 0). Checked on a 1D pair-walk ring, N = 8, 10, 12, CL-1 gate form: TV <= 7.8e-16. In 1D the only breaking is the ring holonomy mod 2 pi; 2 pi is an exact gauge (frozen). At holonomy pi + 1 the rate per site falls with N (3.4e-2, 1.7e-2, 8.9e-3 at N = 6, 8, 10). Those counts are collective: the Fano factor grows in proportion to the window (0.80, 1.61, 4.02 for 2, 4, 10 sites), so there is no sqrt(N) law. A drifting mass angle gives local single hops: rate 0.142 per site per unit drift, Fano 2.00. (b) Prefactor. Lambda/L^2 is conjugate to V4, and a minimum-uncertainty packet gives Lambda_rms L^2 = L^4/(2 sigma_V) with sigma_V^2 = (F/r) v_c V4, where r is records per site per half-tick. With the past cone today (0.1229 H0^-4): imported Poisson per half-tick, or a fair Born coin per site per half-tick, overshoots by 6.7 to 14.9. Expansion-driven changes (through mass angles) give about 2e-40 of the measured value, and split-driven changes at most 5e-31. (c) History. Under S/V dynamics on the past light cone (ADGS model 1, amplitude A = (1/2) sqrt(2 r/(F sig))), rms Omega_L = A/(3 sqrt(V H^4)): 2.73 A in the radiation era, 1.81 A in the matter era, 0.95 A today, so Lambda tracks H^2. Histories from a = 1e-20 survive (H^2 > 0) only for A <~ 0.15. Today's Omega_L = 0.685 is then a >= 7 sigma fluctuation, and the best factorised joint probability with BBN and recombination bounds is about 8e-18. A late-window diagnostic (switched on at z = 3, conditioned on today) gives w0 = +0.17 [-0.97, +0.89] and wa = -0.86 [-3.03, +1.50]; 0 of 82 histories fall in a DESI DR2 box or a LambdaCDM box. Gate result: FAILURE. Supplied model, finite diagnostic: toy gate parameters, LambdaCDM (Planck 2018), the eps0 range, the S/V dynamics, approximate BBN and CMB bounds, and DESI central values.

Statement and supporting text (copied from the note):

#### Statement

A. Records on change in the half-filled sea.

1. Theorem (frozen vacuum). Suppose a site-diagonal antiunitary K reverses each half-tick, K U K = U^dag. Then K maps the Floquet sea at one half-tick onto the sea at the other, so the configuration odds are equal at both. The fewest-change transport between equal odds is the identity, and it is unique, since every other plan has positive expected change. Under record-on-change the vacuum therefore makes no records: the count is 0 and its variance is 0, at every window. In the 1D pair walk (CL-1 gate form: exp(-i(eps - mu/2)R) on even pairs, exp(+i(eps + mu/2)R) on odd pairs) |KUK - U^dag| = 2e-16 and TV(p_A, p_B) <= 7.8e-16 for N = 8, 10 and 12, both at (eps, mu) = (0.6, 0.3) and at (0.0375, 0.01). PR #9876 solved the same antiunitary for the 3D block tick (8^3 torus, max error 1.9e-14). The pi-flux face phases that the sea's energy selects are T-even (+pi and -pi are one holonomy), so the laws' vacuum has this symmetry.
2. Breaking the antiunitary does not give Poisson counts.
   - A gauge-real 1D chain is broken only by its ring holonomy mod 2 pi. Holonomy 2 pi is an exact gauge, and its TV is 5e-16.
   - At holonomy pi + 1 the sea moves. The eps -> 0 entropic plan reaches the LP fewest-change minimum (N = 8: 0.136365 changes per half-tick, both ways).
   - The rate per site falls with N: 3.4e-2, 1.7e-2 and 8.9e-3 at N = 6, 8 and 10. A filled band is invariant under a uniform vector potential, so the bulk stays frozen.
   - The counts that do occur are collective. The long-time Fano factor (tilted Perron root) is 0.80, 1.61 and 4.02 for windows of 2, 4 and 10 sites, so Var ~ w^2: one global mode moves, and a 4-volume count has no sqrt(N) law.
3. The one structural Poisson-like source is a changing odds. If the mass angle drifts by d per half-tick, the plan makes independent single hops. The rate is c d per site with c = 0.142, the one-step Fano factor is 2.00 for the whole ring and for a single pair (two site changes per hop), and the fresh entropy H(Y|X) lies within the Fano-inequality bound h(P_move) + P_move ln(M - 1). Fresh randomness per half-tick is bounded by how much the odds change. A stationary vacuum supplies none.

B. Lambda magnitude, prefactor computed.

4. The phase of Lambda is (Lambda/L^2) V4, so Lambda/L^2 and V4 are conjugate. A minimum-uncertainty packet has sigma_V sigma_(Lambda/L^2) = 1/2 (Gaussian check: 0.50000000), so Lambda_rms L^2 = L^4/(2 sigma_V). With r records per site per half-tick and Fano factor F, the count-volume has sigma_V^2 = (F/r) v_c V4, so Lambda_rms L^2 = (1/2) sqrt(r/(F sig/2)) / sqrt(V4/L^4). Fewer or noisier-per-record counts give a smaller Lambda.
5. The past light cone today is V4 = 0.1229 H0^-4 = 1.01e240 L^4.
   - Imported Poisson per site per half-tick (r = F = 1), or a fair Born coin per site per half-tick (r = F = 1/2): Lambda_rms is 6.7 to 14.9 times the measured value over the eps0 range. This agrees with the register's 'overshoots 6-13x'.
   - Record on change under the laws: zero from the vacuum (item 1). Expansion reads edges only through mass angles mN, so r_exp = c mu_top H sig L/2 <= 1.4e-81, giving 2e-40 of the measured value. Splits give at most one random change per site per split, r_split <= 9.2e-63, giving <= 5e-31 of it. Every structural source misses by 30 orders or more.
   - Matching today's rms needs r/F of about 2 sig A^2, with A as in item 6: about 4e-3 to 2e-2 at A ~ 0.7. No rule supplies it. A Born coin at that rate is FITTED.

C. History and (w0, wa).

6. S/V dynamics (Ahmed-Dodelson-Greene-Sorkin model 1, supplied): Lambda L^2 = A B(u)/u, with B a standard Brownian motion in u = V4/L^4 over the past light cone and A = (1/2) sqrt(2 r/(F sig)) from item 4. ADGS's alpha is A/(8 pi). Theorem (tracking): rms Omega_L = A/(3 sqrt(V H^4)). Here V H^4 is 4 pi/840 in the radiation era and 0.0338 in the matter era (beta functions), and 0.1229 today, so rms/A is 2.73, 1.81 and 0.95. Lambda ~ H^2 at every epoch, and early fluctuations are about 2.9 times today's.
7. Self-consistent Friedmann histories from a = 1e-20, 12000 each, start analytic in the radiation era; a crunch is H^2 <= 0.

   | A | alive | P(BBN) | P(rec) | rms Omega_L0 | P(today) |
   |---|---|---|---|---|---|
   | 0.05 | 1.000 | 0.380 | 0.229 | 0.027 | 2e-140 |
   | 0.10 | 0.991 | 0.195 | 0.117 | 0.055 | 1e-34 |
   | 0.15 | 0.314 | 0.044 | 0.024 | 0.086 | 2e-15 |
   | 0.20 | 0.001 | 0 | 0 | — | — |

   Survival needs A <~ 0.15. Today's Omega_L = 0.685 is then at least a 7 sigma fluctuation. The best factorised joint probability (alive x BBN x recombination x today) is about 8e-18, with bounds |Omega_L(BBN)| < 0.065, |Omega_L(z = 1100)| < 0.03 and |Omega_L0 - 0.685| < 0.02. Per half-tick Poisson (A = 4.8 to 10.7) crunches at once. PR #9876 found the same kind of tracking (Omega_L std 2.54 at BBN at coefficient 1, against 2.73 here).
8. Late-window diagnostic, a lower bound on the trouble (early bounds ignored): switch on at z = 3, A = 0.5, condition on today's Omega_L, and fit CPL to rho_L over z <= 2. The result is w0 = +0.17 [-0.97, +0.89] and wa = -0.86 [-3.03, +1.50] (16-84%). None of the 82 histories falls in a DESI DR2 box (|w0 + 0.75| < 0.12, |wa + 0.86| < 0.5) or a LambdaCDM box. Everpresent Lambda changes by O(1) per Hubble time, so |w + 1| ~ O(1). DESI's departure is about 0.25 in w0, and the hinge law keeps |dw| < 6e-4. The model matches neither.


[end of lines 27-61 of the note]

#### Boundary

Not claimed: that no record rule gives everpresent Lambda.
- The CL-1 cube tick with copy mass was not rebuilt here. The record-arrow probe reports the laws keep sigma_d K, a site-permuting antiunitary, which does not by itself force equal odds. If the copy mass breaks the site-diagonal antiunitary, the 3D vacuum may move. That is the open test, with r and F to be computed as in items 2 and 3.
- Not computed: 2D/3D plaquette-flux T-breaking, the S/V model's alternative 4-volumes (Hubble cylinder), ADGS model 2, and inhomogeneous Lambda (Barrow 2007 constrains it).
- ADGS (2004) and later analyses (Zwane, Afshordi and Sorkin 2018; Das, Nasiri and Yazdi 2023) report viable histories near alpha ~ 0.01 to 0.02 (A ~ 0.25 to 0.5). Here A >= 0.2 does not survive from a = 1e-20. The difference (crunch handling, the 4-volume, the start time) is not resolved.
- The DESI comparison is a box test on a CPL fit to rho_L, not a likelihood.

#### Supplied vs forced

Supplied:
- the toy gate parameters and ring sizes;
- the half-filled sea;
- the eps0 range and v_c = (sig/2) L^4;
- LambdaCDM and the measured values;
- the S/V dynamics and the past-cone 4-volume;
- the BBN and CMB bounds (approximate);
- the start a = 1e-20;
- the DESI and LambdaCDM boxes;
- the m_top value.

Forced, given the laws:
- the frozen vacuum (equal odds, identity plan);
- the 2 pi gauge;
- collective (Var ~ w^2) counts under holonomy breaking;
- Fano 2 under drift, with randomness bounded by the odds change;
- the prefactor 1/2 and the sqrt(r/F) scaling;
- the tracking constants;
- the survival bound on A.

#### Conflicts

- (i) CL-3 (vacuum standard: Lambda a constant per proper 4-volume, w = -1; hinge bound |dw| < 6e-4). Everpresent Lambda gives |w + 1| ~ O(1), so the two cannot both hold.
- (ii) The register's criterion "a size law must not drift with the horizon". Everpresent Lambda violates it by construction (item 6).
- (iii) Record-reading (every site every half-tick, adopted 2026-10-22) gives Fano 0 (PR #10002). Record on change gives no vacuum records. Neither supplies Sorkin noise.
- (iv) The info-min-law and minimal-toe-b R5(a) lead (Lambda ~ N^-1/2 within a factor 2). It has a prefactor convention of order 1. With the computed 1/2 and v_c, it overshoots 6.7 to 14.9 times and fails the history test.

[end of lines 93-128 of the note]

(Omitted from the note: lines 62-92, 129-143 and lines 1-26, i.e. front matter, derivation prose, run instructions and any candidate-rule checklist.)

## Corrected or replaced claims

# Corrections and conflicts: vacuum, cosmology and dark matter

Each item gives the corrected form of a claim and the PR that corrects it. A claim listed here as withdrawn or narrowed should not be read from the earlier note alone.

## 1. Law names in the notes versus `docs/CANDIDATE_LAWS.md`

Most notes in this theme write CL-1, CL-2 and CL-3 for an update law, an actuality law (record formation and fewest-change transport) and a response law (Lambda a constant per proper 4-volume, departures from the vacuum of the same edges). In `docs/CANDIDATE_LAWS.md` the aliases are different: CL-1 is the lossless-influence clause, CL-2 the record-removal clause, CL-3 a pending conservation proposal, and that register has zero premise weight. It does not define the update, actuality or response laws used here (cube tick, fixed lapse, edge registers, window, glued split, passing). Corrected reading: every kept result is conditional on those laws exactly as the note states them as supplied models; none is a consequence of the register in `ref/`. Where a copied sentence says "CL-n", read it as the note's own shorthand. Note 10007 also cites a document called CANDIDATE_LAWS_v3 that is not in `ref/`.

## 2. #9876 and #10018: two conventions for a Poisson record-count Lambda

#9876 states that Poisson counting at the rule density gives an estimate within a factor 10 of the measured Lambda (1.46e-123 rho_P, 1.29 times measured), with a stated convention range of roughly 0.2 to 10. It uses one record per volume element v0 = a^3 tau = 729.4 Planck 4-volumes.

#10018 computes the prefactor from the conjugacy bound with the 4-volume per site per half-tick v_c = (sig/2) L^4, sig = sin(eps0)/sqrt 3, eps0 from 0.0075 to 0.0375. Under those conventions an imported Poisson count per site per half-tick, or a fair Born coin per site per half-tick, gives 6.7 to 14.9 times the measured Lambda, tracking H^2, and histories survive only for A of at most about 0.15.

Comparison made in this consolidation, not stated by either note: the "within a factor 10" statement of #9876 depends on its element-size convention (its own stated range is roughly 0.2 to 10), and under #10018's convention the computed overshoot is 6.7 to 14.9. Neither fixes Lambda. Other Sorkin-type numbers carried in this theme (1.9e-121 and 6.9e-123 rho_P in #9880, "within a factor of 2" in #9900, 0.065 to 0.14 times measured in #10002, 0.09 to 0.20 in #9962) are literal or order-one-prefactor forms; only #10018's uses the computed prefactor 1/2.

Standing only in #9876: the 3D spin-3/2 block-tick instance of the antiunitary and frozen odds (8^3 torus, entry error 1.9e-14, absolute differences 1.1e-16 and 8.3e-17); the window-dependent Fano factors (1.00, 0.36, 256.75, 91.47), the 1+1D past-cone variance growth T^1.036, the 3D area law Var = 0.50 l^2 and past-cone Var ~ R^3.10; the unimodular estimate's dependence on the Fano factor; the uncertainty-reading and classical-sum readings for the frozen sea (about 1e31 too large or small); the matter-relay count (3.0e-169 rho_P); its own S/V history numbers (standard deviation of Omega_L 2.54, 1.94 and 0.88 at BBN, recombination and today at coefficient 1; best factorised probability 2.0e-11; w_eff(z = 0.5) = -0.28 [-1.22, +0.28]). These are a different parametrisation from #10018's, so the two sets of numbers should not be merged. #10018 notes that published S/V analyses report viable histories at A of about 0.25 to 0.5 whereas its ensembles do not survive from a = 1e-20 at A of 0.2 or more; that difference is unresolved.

## 3. Frozen-vacuum theorem versus the copy-massed tick (#9876, #9889, #10018 versus #9923)

#9876 and #10018 show that a site-diagonal antiunitary reversing each half-tick gives equal odds at both half-ticks, so a fewest-change record rule moves nothing. Their checks are the 1D pair walk and, in #9876, the 3D block tick at (mu, b) = (0.4, 0.3); the 3D statement names no copy mass. #10018's boundary section says the copy-massed cube tick was not rebuilt and that, if the copy mass breaks the antiunitary, the 3D vacuum may move.

#9923 (logged) computes exactly that case on 12-site 3x2x2 patches at (b, mu, M) = (0.3, 0.4, 0.5): the sea's odds at the two half-tick stages differ (total variation 2.99e-3, zero at M = 0), related by particle-hole exchange, so the forced configuration motion is a period-2 shuttle of at least 2.5e-4 flips per site per half-tick. Its even-order density statistics and turn-symmetric counts are unchanged and its C-odd part averages to zero over a tick.

Corrected form: the frozen-vacuum statement holds for the ticks that #9876 and #10018 check, which do not include a copy mass. For the copy-massed tick the patch computation in #9923 finds motion. Whether record-on-change counts for that tick could supply a Lambda source was not computed in either note. #10018's estimate of the records-on-change contribution (zero, from the vacuum) is therefore for the ticks it checks, without copy mass. #9889's frozen half-filled sea ("the empty start, the half-filled sea and any tick-eigenstate start give no moving records", ticks at (mu, b) = (0.4, 0.3) and (0, 0.3)) is likewise for a tick without copy mass. #10018's sentence that "the laws' vacuum has this symmetry" concerns the face phases and is not established for the copy-massed tick; #10018's own Boundary and #9923 limit it. #9978 E1's statement that the half-tick odds are stationary only at the two fold limits is stated for #9978's tick and uses a different quantity from the configuration odds of #9876 and #9923 (an independent check of its runner finds a correlation-matrix change); do not read it as confirming or contradicting this item.

## 4. #9900 and the status of the fixed-4-volume clause and its carrier

#9900 tests a response law that varies edge lengths with each record's 4-volume held fixed. Notes #9962, #9990 and #10002 refer to the fixed-4-volume-per-record clause as dropped from the laws, and #10002 states that the Planck-sized circle for Lambda exists only under that dropped clause. Corrected form: #9900's cancellation of every vacuum term proportional to 4-volume, and its conserved Lambda set by initial data, are statements about that clause on the supplied cubic-frustum carrier, not about the laws as later written.

PR 9902 (assigned to gravity-edge-registers) corrects the carrier itself: the cubic-frustum expansion law matches Friedmann only to first order in rho/rho*, saturates at H l = sqrt 2, and has no bounce. #9900's statement that late expansion obeys Friedmann with a constant Lambda (w = -1) is therefore a late-time, first-order statement. #9900's kick rho^2/rho* per split and #9990's "does not jump" vacuum energy at a split look opposed but hold under different clauses; #9990 says "the dropped fixed-4-volume-per-record clause gave a kick at each split". The same carrier underlies the hinge-series results #9919 and #9990 (logged).

## 5. #10007 narrows #9961 (part B) and #10000 (estimate D4)

#9961 (B2 to B5) uses a supplied Poisson stepping of each register to give the trigger a timing spread, redrawn each step, and finds a level-independent per-level spread and n_s = 1. #10007 shows that under the laws' fewest-change (quantile) transport, with "value minus s" in the passing, a register keeps its Born quantile, so split-time offsets are inherited (about 1/4 of a child's trigger edges inherited: 6 on even children, 3 on odd), not redrawn. The block-mean offset is stationary at sigma_r/sqrt 18 over 40 generations, the field is white, and as a curvature seed it gives Delta^2 proportional to (k l)^3, about 1e-99 at the pivot. Corrected form: the n_s = 1 of the Poisson cascade holds for the Poisson toy of #9961; for the laws' transport the offsets are white inherited offsets and are not a scale-invariant seed. The register arithmetic, the cascade theorem Delta^2(2k) = lam Delta^2(k) and the statement that the trigger reads only tr h/6 at first order in #9961 are not changed.

#10000 (D4) estimates the dephasing the laws supply at 0.07 to 0.10 e-folds from the Poisson register model. #10007 replaces this: the three register-odds readings give 0.0002 to 0.065 e-folds, the coupled trigger damps the spread (by a factor 0.43 on a 32^3 lattice with shared edges), and the 0.35 e-folds that #10000 requires would need Gaussian register odds of standard deviation at least 4.94 s steps, more than half the 5 s window at Delta = 1. #10000's no-seed result (A_s = 0 from the vacuum under the register as written) and its synchronised-split heating (|beta|^2 = 9/16 per mode per split, ln 2-periodic modulation) are not changed. #10000's named candidate (first odds spreading each block's registers over one octave) was not run by name. #10007 B5 answers the question #10000 left open ("whether the coupled trigger keeps or erases an initial spread is not computed") for the inherited Gaussian offsets of its model: the coupled trigger damps the spread by 0.43. Its B6 requirement of sd >= 4.94 s steps applies to Gaussian odds; non-Gaussian odds were not computed.

#9961's factor 1.8 rise in wait variance (redrawn Poisson steps, 2D tree) and #10007's factor 0.43 fall in split-time spread (inherited offsets, 3D lattice, "unsplit neighbour" condition) use different models and quantities. Neither note reconciles them; the 1.8 holds only for the toy.

## 6. Index values at N* = 55 for fold plateaus (#9979, #9982, #9986) corrected by #10000

#9979 (C2) reports n_s = 0.9631 to 0.9634 at N* = 55 for the 1D pole toy, and #9982 (C4) reports the same for the nested-sea density-wave fold; #9986 reports n_s = 0.948 at N* = 55 for the flux-fold quartic hilltop. In each the value N* = 55 is supplied. #10000 (C3) computes N* self-consistently for the nested-sea Hartree plateau with instant reheating, k* = 0.05/Mpc and g* = 106.75, with the fold rung fitted to A_s: N* = 47.4 (g = 0.5) and 46.8 (g = 1), giving n_s = 0.957 (1.8 sigma below Planck, 5.6 sigma below ACT with DESI), r about 5e-18 and running about -9e-4. Corrected form: for the nested-sea plateau the supplied-N* values 0.963 are not self-consistent; the number to use under the note's own matching assumptions is 0.957. For any exponential plateau n_s = 1 - 2/N, and ACT's value needs N* about 77 (#9918, #9979). #9982's rungs 18.6 and 20.4, H/M_P and r are likewise for the supplied N* = 55; at the self-consistent N*, #10000 gives rungs 18.4 and 20.2, H/M_P 7.6e-13 and 2.3e-13, and r = 5e-18 at g = 1. The #9986 value and its amplitude failure were not recomputed in #10000.

## 7. #9991 narrows #9978 (wall misfolds), and fold language that should not be conflated

#9978 (logged) says a wall where the sign of mu flips carries gapless 2+1 fermions and in-gap states growing with wall area. #9991 (logged) shows that the update has one sign of mu per species in every cube (mu = mN with N > 0), so no law produces such a wall; the wall configurations are those of a supplied mass profile, not states of the update. Corrected form: #9978's wall misfold statement holds only for a supplied mu-sign profile.

Four different things are called a fold and must not be conflated. The two-tiling cube fold selected by the sign of mu (#9978, #9991; fold strength about 9 |mu| in variance imbalance, about 4e-22 for an electron mass, so unfolded at the cell scale); the staggered density-wave fold of the bare axis hop's nested sea under a supplied nearest-neighbour repulsion (#9982, #10000), which #9982 shows is not the mass angle, selects no tiling and leaves every site free; the star-rule dimer-path fold of #9979's 1D toy; and the face-flux fold (#9986). Only #9979's 1D dimer-path toy and the 3D density-wave fold (#9982, #10000) reached an index near 0.96; the flux fold (#9986) reached 0.948. These computations rest on supplied choices (the stiffness, the repulsion g, a rung fitted to A_s, instant reheating).

## 8. Earlier main-branch statements narrowed by kept or logged notes in this theme

- #9918: the earlier statement that n_s = 1 - 2/N_e at N_e = 60 matches Planck within 0.4 sigma is narrowed to 0.4 sigma for Planck and -2.4 sigma against ACT (-2.8 sigma against DR2).
- #9919 (logged): the earlier dark-energy claim of a constant shift with no time dependence does not hold on the hinge carrier, where the correction changes with time at about 1e-121.
- #9990 (logged): the "log-periodic ripple of period ln 2" in the tensor spectrum is second order in its fundamental (at most 1.1 (H l_c)^2) in the discrete-tick toy; the first-order structure is a fast lattice oscillation.

## 9. What counts as a "record count" in #9876 versus the later record notes

#9876's Fano factors and area-law variance are for site occupation number in windows of a frozen sea. #10002 (and #9962) use a record per site per half-tick, for which cell, split and record counts are exact (Fano 0). #10018 uses record on change, for which the vacuum makes no records. Corrected form: "record counts are not Poisson" in #9876 and "record counts are exact" in #10002 refer to different counted quantities and different record-formation rules; neither supplies the Poisson noise a Sorkin-type Lambda needs.

## 10. Conflict between the everpresent-Lambda route and the response law

#10018 notes that an everpresent Lambda (w + 1 of order 1) cannot hold together with the response law's constant Lambda per proper 4-volume (w = -1, hinge bound |dw| below 6e-4 in #9919). Neither is derived from the axioms; each is a supplied model.

## 11. Narrowings along the fold chain and elsewhere, as stated by the notes

#9982 narrows #9979's pre-role tick suggestion (it works for the roll, not for the identification with mu or for the passing). #10000 narrows #9982's "the passing must write the clock" by proposing order carriage IN-1, a tested clause that is not adopted. #9987 (logged) narrows #9986's suggestion that a face clause derives the pi phases to a kinematic statement. #9988 narrows #9985 (chirality-doublers) to a massless mirror.

## Source notes carried with this consolidation

Each kept result's own note, runner and cache are carried byte-for-byte from its source PR.

- #9876: [TIME_REVERSAL_FREEZES_HALF_FILLED_SEA_RECORDS_AND_RECORD_COUNT_LAMBDA_NEEDS_POISSON_INPUT_BOUNDED_THEOREM_NOTE_2026-10-21.md](TIME_REVERSAL_FREEZES_HALF_FILLED_SEA_RECORDS_AND_RECORD_COUNT_LAMBDA_NEEDS_POISSON_INPUT_BOUNDED_THEOREM_NOTE_2026-10-21.md)
- #9880: [FLOQUET_SEA_VACUUM_SOURCE_IS_ZERO_PLANCKIAN_OR_MASS_DOMINATED_NOT_MEASURED_LAMBDA_BOUNDED_THEOREM_NOTE_2026-10-21.md](FLOQUET_SEA_VACUUM_SOURCE_IS_ZERO_PLANCKIAN_OR_MASS_DOMINATED_NOT_MEASURED_LAMBDA_BOUNDED_THEOREM_NOTE_2026-10-21.md)
- #9900: [FIXED_FOUR_VOLUME_PER_RECORD_CANCELS_VACUUM_ENERGY_AND_LEAVES_LAMBDA_AS_HISTORY_BOUNDED_THEOREM_NOTE_2026-10-21.md](FIXED_FOUR_VOLUME_PER_RECORD_CANCELS_VACUUM_ENERGY_AND_LEAVES_LAMBDA_AS_HISTORY_BOUNDED_THEOREM_NOTE_2026-10-21.md)
- #9918: [CURVATURE_SQUARED_INFLATION_MISSES_THE_ACT_TILT_AND_NO_RULE_LIFTS_IT_BOUNDED_THEOREM_NOTE_2026-10-21.md](CURVATURE_SQUARED_INFLATION_MISSES_THE_ACT_TILT_AND_NO_RULE_LIFTS_IT_BOUNDED_THEOREM_NOTE_2026-10-21.md)
- #9946: [LABEL_COPIES_CARRY_LINKED_FAMILIES_AND_ONLY_A_SUPPLIED_LABEL_PARITY_OR_MAGNETIC_CHARGE_STABILISES_A_MASSIVE_RELIC_BOUNDED_THEOREM_NOTE_2026-10-22.md](LABEL_COPIES_CARRY_LINKED_FAMILIES_AND_ONLY_A_SUPPLIED_LABEL_PARITY_OR_MAGNETIC_CHARGE_STABILISES_A_MASSIVE_RELIC_BOUNDED_THEOREM_NOTE_2026-10-22.md)
- #9961: [THE_SPLIT_TIME_CASCADE_IS_SELF_SIMILAR_SO_ITS_DELTA_N_SPECTRUM_IS_FLAT_AND_THE_TRIGGER_READS_NO_LINEAR_SCALAR_BOUNDED_THEOREM_NOTE_2026-10-22.md](THE_SPLIT_TIME_CASCADE_IS_SELF_SIMILAR_SO_ITS_DELTA_N_SPECTRUM_IS_FLAT_AND_THE_TRIGGER_READS_NO_LINEAR_SCALAR_BOUNDED_THEOREM_NOTE_2026-10-22.md)
- #9979: [A_FOLD_IS_A_SLOW_SCALAR_CLOCK_ONLY_WHEN_THE_UNFOLDED_SEA_IS_CRITICAL_ON_A_SURFACE_AND_THE_UPDATES_DIRAC_SEA_MAKES_IT_FAST_BOUNDED_THEOREM_NOTE_2026-10-22.md](A_FOLD_IS_A_SLOW_SCALAR_CLOCK_ONLY_WHEN_THE_UNFOLDED_SEA_IS_CRITICAL_ON_A_SURFACE_AND_THE_UPDATES_DIRAC_SEA_MAKES_IT_FAST_BOUNDED_THEOREM_NOTE_2026-10-22.md)
- #9988: [THE_GAPPED_MIRROR_KEEPS_ONLY_A_NUMBER_SHARED_WITH_LIGHT_MATTER_AND_ITS_LIGHTEST_STATE_IS_CHARGED_SO_IT_GIVES_NO_DARK_MATTER_BOUNDED_THEOREM_NOTE_2026-10-22.md](THE_GAPPED_MIRROR_KEEPS_ONLY_A_NUMBER_SHARED_WITH_LIGHT_MATTER_AND_ITS_LIGHTEST_STATE_IS_CHARGED_SO_IT_GIVES_NO_DARK_MATTER_BOUNDED_THEOREM_NOTE_2026-10-22.md)
- #10000: [AN_UNSPLIT_BLOCK_CANNOT_INFLATE_SO_THE_FOLD_PLATEAU_NEEDS_SPLITS_THAT_CARRY_ITS_ORDER_AND_DEPHASED_SPLIT_PHASES_TO_SEED_PERTURBATIONS_BOUNDED_THEOREM_NOTE_2026-10-22.md](AN_UNSPLIT_BLOCK_CANNOT_INFLATE_SO_THE_FOLD_PLATEAU_NEEDS_SPLITS_THAT_CARRY_ITS_ORDER_AND_DEPHASED_SPLIT_PHASES_TO_SEED_PERTURBATIONS_BOUNDED_THEOREM_NOTE_2026-10-22.md)
- #10002: [FIRST_SLAB_FIXES_LAMBDA_ONLY_AT_THE_PLANCK_SCALE_AND_A_RECORD_COUNT_MULTIPLIER_GIVES_A_WRONG_SIGN_OR_A_DRIFTING_LAMBDA_BOUNDED_THEOREM_NOTE_2026-10-22.md](FIRST_SLAB_FIXES_LAMBDA_ONLY_AT_THE_PLANCK_SCALE_AND_A_RECORD_COUNT_MULTIPLIER_GIVES_A_WRONG_SIGN_OR_A_DRIFTING_LAMBDA_BOUNDED_THEOREM_NOTE_2026-10-22.md)
- #10005: [NO_STRUCTURE_OF_THE_UPDATE_PROTECTS_A_DARK_SPECIES_BECAUSE_THE_MIRROR_NUMBER_IS_SHARED_AT_EVERY_MOMENTUM_THE_BLOCK_PERIOD_BLOCKS_NO_COPY_DECAY_AND_THE_WINDOW_FLOOR_HOLDS_NO_ATOM_OR_REMNANT_BOUNDED_THEOREM_NOTE_2026-10-22.md](NO_STRUCTURE_OF_THE_UPDATE_PROTECTS_A_DARK_SPECIES_BECAUSE_THE_MIRROR_NUMBER_IS_SHARED_AT_EVERY_MOMENTUM_THE_BLOCK_PERIOD_BLOCKS_NO_COPY_DECAY_AND_THE_WINDOW_FLOOR_HOLDS_NO_ATOM_OR_REMNANT_BOUNDED_THEOREM_NOTE_2026-10-22.md)
- #10007: [BORN_SPLIT_TIMES_ARE_WHITE_INHERITED_OFFSETS_AND_THE_PASSING_LEAVES_NO_REMAINDER_SO_NO_LAW_SEEDS_CURVATURE_BOUNDED_THEOREM_NOTE_2026-10-22.md](BORN_SPLIT_TIMES_ARE_WHITE_INHERITED_OFFSETS_AND_THE_PASSING_LEAVES_NO_REMAINDER_SO_NO_LAW_SEEDS_CURVATURE_BOUNDED_THEOREM_NOTE_2026-10-22.md)
- #10018: [RECORDS_ON_CHANGE_ARE_FROZEN_IN_THE_HALF_FILLED_SEA_SO_A_RECORD_COUNT_LAMBDA_HAS_NO_POISSON_SOURCE_AND_EVERPRESENT_HISTORIES_FAIL_THE_EARLY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-10-22.md](RECORDS_ON_CHANGE_ARE_FROZEN_IN_THE_HALF_FILLED_SEA_SO_A_RECORD_COUNT_LAMBDA_HAS_NO_POISSON_SOURCE_AND_EVERPRESENT_HISTORIES_FAIL_THE_EARLY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-10-22.md)

## Other results

The scope text is copied verbatim from each source note. The full note, runner and cache stay on the listed branch at the listed commit.

| PR | Result | Disposition | Scope as stated in the source | Branch and commit |
|---|---|---|---|---|
| #9877 | The candidate laws leave only a link-free species as a dark-matter slot | logged | For the supplied staggered block tick and supplied (mu, b) settings: the two copies at one frequency carry equal values of any rotation-covariant charge at rungs 1 to 3; pi-cone states carry their species number, sit at the global band top and, in finite numerical searches, have no lower two- or three-body state; the record set has no source term; and a number-conserving species with no link is exactly stable. Measured-data comparisons (halo dynamics, CMB consistency, thermalisation, self-scattering, sterile-neutrino lifetime) are estimates. No dark-matter species, mass or relic abundance is established. | `claude/toe-dark-matter-20261021` `1ac4d9af669f` |
| #9889 | A definite start gives the record arrow, but no initial odds tested give the spectral tilt | logged | For the supplied staggered Margolus tick on small tori, odds stationary under a half-tick freeze the register's transport rule, so the empty start, the half-filled sea and any tick-eigenstate start give no moving records; a Haar-typical start has near-maximal odds entropy and no growth; a definite start (odds on one configuration) has zero odds entropy and rises to a volume law, giving an arrow; the only definite starts that favour no site are all-empty and all-full, both frozen; the support of a local operator grows exactly one site per half-tick in L-infinity distance; finite-range starts give an analytic structure factor with small-q index 0 or 2, and a doped Fermi sea gives index near 1. Comparisons with the measured tilt, baryon asymmetry and dark-matter ratio are estimates. No initial-odds law beyond the arrow, and no value of n_s, eta or the dark-matter ratio, is established. | `claude/toe-initial-odds-20261021` `93909643e475` |
| #9919 | The hinge response law keeps w at -1, far below the DESI departure | logged | Under the register's response law with Lambda a constant per proper 4-volume, the hinge Friedmann law H^2 = X - X^2 l^2/2 + O(l^4) gives \|w + 1\| of order 1e-121, a uniform rescaling of H projects onto (w0, wa) = (-1, 0) exactly, and every rule effect estimated here projects to \|dw\| below about 1e-18 for known content and 6e-4 for the heaviest allowed species, against the roughly 0.1 of the DESI fits; the projections are linearised fits to supplied toy BAO errors, and the comparison with DESI is an estimate. | `claude/toe-desi-de-20261021` `1a985cfacee0` |
| #9923 | No configuration or record rule sources the response, and the copy-mass sea motion is a particle-hole shuttle | logged | Under the register's update, actuality and response laws: the actuality law never changes the odds and the vacuum odds return every tick, while the response law subtracts the vacuum odds at the same configuration, so the matter source is zero at every configuration and no rule acting only on the configuration or the records (any rate, record reading or cost) sources the response; the half-ticks are one-body unitaries, so number is conserved exactly. Finite diagnostic on 12-site 3x2x2 patches of the supplied copy-massed tick at (b, mu, M) = (0.3, 0.4, 0.5): the sea's odds at the two half-tick stages are exchanged by particle-hole conjugation (equally the fourfold turn or a mirror), so the forced configuration motion is a period-2 particle-hole shuttle of at least 2.5e-4 flips per site per half-tick that leaves every even-order density statistic and every turn-symmetric count unchanged and whose C-odd part averages to zero over each tick. Escapes are estimates. No source of matter, baryon excess or clock is found. | `claude/toe-departure-law-20261021` `5c99f9982500` |
| #9947 | Fixed lapse keeps Lambda independent of the dark constant, and an empty mean-zero start forces Lambda positive | logged | For the update law's fixed-lapse clause on isotropic edges (N = sin(eps0) l/sqrt3, so lapse a^n with n = 1) and the response law's constant per proper 4-volume Lambda: a read lapse a^n makes the tick's conserved value (the dark constant D) a fluid of w = n/3, so D is dark radiation (symbolic); Lambda enters the fixed-lapse generator as Lambda a^4 and D as a^0, so no shift of D absorbs Lambda (the unimodular degeneracy would need n = -3), and two readings of a(eta) separate them (det J = -4.124). For the homogeneous volume mode of an empty one-cube start on the finite log window l/L in [1/8, 2] (Dirichlet walls, hop kinetic matched to the classical Regge form): a mean-zero dark constant needs Lambda = <K>/<v> with K positive semidefinite, so Lambda >= 0, and Lambda > 0 strictly on the finite window (Lambda_min L^2 = 0.083 to 0.096 for 23 to 113 values per octave); with a transparent top Lambda_min falls as (top length)^-6 and as b^-6 for blocks, so the size is free; the mean form admits every Lambda >= Lambda_min. The tick has no Lambda period mod 2 pi because consecutive window ratios 2^(4/s) are irrational. Estimates and look-elsewhere statements: a least-kinetic start with a closed top gives a Planck-scale value, about 1e119 times the measured one; tick-count and split-count forms are dimensional coincidences. Supplied model, finite diagnostic: the unit map, the window, the minisuperspace mode, the hop kinetic, the least-kinetic start, the eps0 range and the measured Lambda; one radiation-like-spread statement is stated, not computed. | `claude/toe-lambda-quantum-20261021` `3eb8e362ec03` |
| #9962 | No count, spread or window power in the laws sizes Lambda without tuning or horizon drift | logged | Three size rules for the response law's constant Lambda per proper 4-volume, built from structures of the candidate laws, tested against Lambda L^2 = 7.15e-121 (L = sqrt(8 pi) l_P) and w = -1. (a) Inverse counts: under the actuality law cell, split and record counts are fixed by the geometry (Fano 0); the split trigger never stops while H > 0, so no count freezes; the de Sitter past-cone 4-volume grows as (4 pi/3) H^-3 (t - 11/(6H)) (exact); a rule Lambda L^2 = C N^-p with N = k (HL)^-d has the de Sitter fixed point (Lambda L^2)^(1-pd/2) = C k^-p 3^(pd/2), rung-sized for order-one C and scale-free at pd = 2. (b) The dark constant's zero-mean spread: with lapse a^n its density goes as a^-(n+3), w = n/3, so under the fixed lapse every spread is dark radiation of either sign (exact enumeration of skewed zero-mean cells: mean 0, variance N sigma^2, P(negative) -> 1/2); w = -1 needs n = -3. A Sorkin-type variant (Lambda conjugate to 4-volume, not in the current laws) with exact counts and a least-kinetic edge vacuum gives 6 to 13 times the measured size but tracks H^2. (c) The window ratio 2^(4+Delta) per rung to the horizon gives about 1e-241 and tracks H^(4+Delta); a frozen variant 2^-(4+Delta)s hits at s = 99.8 only as a fit of s (chance 2/(4+Delta)). Every horizon-tied form has w0 > -0.7 and wa > 0, opposite in sign to DESI's wa. Supplied model, finite diagnostic: LambdaCDM (Planck 2018), the eps0 range, the edge vacua, the unimodular coupling of the Sorkin variant, and DESI DR2 (w0, wa) for a sign comparison. | `claude/toe-lambda-size-rule-20261021` `d93ba5806449` |
| #9963 | The copy sign is exact only at rest, and no copy, edge or split structure of the candidate laws gives a stable, cold, link-free species | logged | For CL-1's cube tick with the copy mass, read on diagonal metrics: R_i = sqrt3 W_i are Clifford generators and G = i R1 R2 R3 is central, so the copy sign s = G R commutes with the even half-tick and the copy mass at every metric; on Bloch states the odd half-tick keeps s exactly at K = 0 (flat and a random metric, 7e-16) and not at random K (0.52); at K = 0 the s = -1 copy has rest phase mu + M; cell-local operators commuting with the tick at three random K (and three metrics) are only the identity; a one-cube traceless strain vertex taking the heavy copy at rest to the light copy at recoil q vanishes at q = 0, grows as q/M, and is O(1) (0.30 to 0.93) at a real decay's recoil q = 0.87 M for M = 0.5 and 0.05, while conformal strain gives zero; the second-quantised copy sign commutes with mode number, so each copy carries its species' link charges. For one chiral family (hand-entered table) nu^c is the only link-free Weyl state and nu^c nu^c the only singlet bilinear, Z4 = i^(B-L)-odd. An edge register's hop and value have trivial commutant and the hop anticommutes with (-1)^n. Squared edge lengths are a linear bijection of a tetrahedron's Gram matrix, so the positive-volume set is convex and the flat vacuum manifold contractible; exhaustive scans of one tetrahedron (s = 2, Delta = 0, 1) find every positive-volume state connected to the flat one by single steps; a child edge at the parent value minus s is exactly half the parent length. Estimates against measurement use supplied inputs. Supplied model, finite diagnostic: (b, mu, M), metric weights, the charge table, s and Delta, the unit map, the graviton-coupling normalisation, y, measured bounds; the label-parity survivor N' and the edge-register root are cited, not recomputed. | `claude/toe-dark-matter-candidate-20261021` `e9b9b3e38125` |
| #9966 | The record-count clock is self-similar, so it gives no tilt, and a tick-read exit is blue and too large | logged | For the actuality law's records (one permanent record per matter site per half-tick, a new site's first record at the half-tick after it appears, records never conditioning the odds, a past record read only through a pointer) and the update law's split (eight children per block, children's edges along parent edges at the parent's value minus s, tied lapse): (A) exact counting: a block has unrecorded sites only on its 7/8 new sites, and only for the one half-tick after its split, so the unrecorded share per generation is (7/8)/T_gen, the same at every level; the share of a region's records laid in the latest generation is 8^l / sum_j 8^j, which tends to 7/8 with per-split ratio 1 + O(8^-l), a start transient and not a constant factor; the tied lapse gives 1/(2 k l_c H) ticks per generation, equal at every level of a de Sitter cascade; records never condition the odds, so no vacuum-energy share belongs to unrecorded modes; a pointer's occupation odds never change, so a pointer holds no tick count. (B) With a supplied exit that reads ticks, an exact tight-binding edge register with the fewest-change (quantile) transport gives a Born split-time spread delta N = ln2 sigma_T/T_gen per level that does not depend on H; its minimum over Gaussian packets is 0.023 to 0.22 e-folds for s = 23 to 113 and register speed x = v/2J = 0.5 to 0.9999, at least 600 times the 3.8e-5 that A_s needs; in de Sitter the levels repeat, so lam = 1; when H falls the register slows and spreads more, so n_s - 1 = p eps with p = +1.0 to +5.4 (blue). (C) The record clock adds no tensor channel; r is set by a supplied plateau H. Supplied model, finite diagnostic: the octree with S, T_gen and a Born spread; an 8-mode ring; a random controlled unitary; a one-dimensional tight-binding register with J = 1, Gaussian packets and quantile transport; eps; the plateau H. Measured numbers enter only the estimates. | `claude/toe-record-clock-tilt-20261021` `d2443c9003b8` |
| #9978 | The sign of the mass angle picks one cube fold of the two-tiling tick, and its misfolds are the matter fermions; dimer resonance and symmetric window rules leave the 3D fold unselected | logged | Finite exact diagnostics. Pair (dimer) coverings enumerated on 4x4, 6x6, 8x8 and 4x4x4 tori. Quantum dimer resonance H = -t sum flip + v sum flippable: exact extreme ends (v -> -inf, v > t), the RK point's tiling balance, the one-cube problem, product-crystal energies, and an exact 6x6 control. The CL-1 cube hop R (edge hops with spin-3/2 overlap phases) on one cube (256-state Fock space) and the two-tiling tick, even step eps - mu/2 and odd step eps + mu/2, on the 8^3 torus and 16xLxL slabs (L = 4, 6), single-particle, eps = 0.3, copy mass M = 0.2 in one check. Tile-level window rules on 8x8, 12x12 and 4^3 tilings by 2^d tiles. Results: the 3D landscape of any partner-in-star rule has >= 9^(N/8) folds; dimer resonance picks the columnar states at v -> -inf (3 axes x 2 offsets, each inside one CL-1 tiling), a highly degenerate no-resonance set for v > t, and no fold at the RK point; the cube crystal is the best product crystal for -0.802 < v/t < 0.671, but the exact 2D control shows product energies do not decide the phase; the cube's four-unit vacuum is 91% in the span of its nine pair coverings, and the cube tick is not a plaquette flip; the two-tiling tick's quasi-energy gap is exactly \|mu\|, so every mu < 0 vacuum is continuously the even-cube fold and every mu > 0 vacuum the odd-cube fold, with every site bound by the face-mirror condition at the limits; point misfolds are odd cubes, which are fermions in a 4-state level split 2 + 2 by the copy sign, costing \|mu\|; wall misfolds carry gapless 2+1 fermions; a symmetric 3^d window rule leaves 2^O(L^(d-1)) sliding folds, and a 2x5 anti-slide window leaves only the aligned 2D crystals; the fewest-change transport cannot select. Toy and finite: the fold has no free sites, its strength at physical masses is ~1e-22, and the nested role-block layout is not produced. | `claude/toe-fold-selection-3d-20261021` `f9c3ec8bbed9` |
| #9982 | The bare axis hop's sea folds slowly by a staggered density wave, but the fold is not the mass angle, the Dirac sea needs the face phases, and the split cannot pass the fold | logged | Single-particle two-tiling ticks in Bloch form (2^3 cell; eps = 0.3; k grids 6^3 to 24^3), the cube's 4096 sign fields, Hartree mean field for spinless fermions with nearest-neighbour repulsion g on the simple-cubic half-filled sea (elliptic density of states), slow roll on the computed potential and cranking mass, a discrete stationary-phase check of friction, and a 4^3-supercell child sea. Results: (A) every bond lies in exactly one cube of one tiling, so the bare axis hop's two-tiling tick is a split of the 6-NN hop. Its gapless set stays a nested surface (box count 4.5; 4.2 at mu = 0.1), while CL-1's spin-3/2 tick has Dirac points and the same quasi-energies as the Kogut-Susskind pi-flux tick (1e-15). R^2 = 1 holds for exactly the all-minus-face class (128 of 4096 fields). The Dirac sea comes from the face phases, not from the folding; pi flux lowers the half-filled energy from -1.00244 to -1.19380 per site. (B) The staggered density wave at (pi,pi,pi) gaps the nested sea at every g > 0 (ln D* slope -1.168 = -1/(6 rho0)); the Dirac sea needs g > 0.732. It is a Dirac mass of CL-1's tick, but it adds to mu in quadrature (0.1383 = sqrt(0.1^2 + 0.0955^2)), selects no tiling (\|Var N_even - Var N_odd\| < 1e-14) and leaves every site free. (C) Cranking mass M -> rho0/(12 D^2) and released energy W ~ D^2 ln^2(1/D) give n_s = 0.9631-0.9634 at N* = 55 for g = 0.5 and 1 at rungs 0, 2, 4, with r = 6e-6 to 2e-8 and exit before D*. A_s fixes the rung at 18.6 (g = 0.5) or 20.4 (g = 1). (D) A phase per proper 4-volume gives friction 3H exactly (1.0015 at H tau = 1e-3); a phase per cell gives 27 ln2/14 = 1.34 off. CL-3's 'update's vacuum' (negative quasi-energies filled) is the unfolded sea, so the plateau has zero departure. (E) The parent nesting vector never lifts to the child's, and a passed density wave has zero overlap with the child's fold coordinate and leaves the child gapless: children are born unfolded. Supplied: eps, g, the Hartree reading, J a = sqrt3, M_P a = 1, N* = 55, semiclassical FRW. | `claude/toe-nested-prefold-sea-20261021` `bdf301cb2b2e` |
| #9986 | The nested sea orders its face flux to pi, but the flux fold is a scale-free quartic hilltop and a split cannot pass pi flux | logged | Spinless half-filled nearest-neighbour cubic sea (hop 1) with link phases A whose every face carries flux of magnitude Phi (0 <= Phi <= pi); Bloch form on the 2^3 cell (k grids 6^3 to 48^3), a q-site magnetic cell for the uniform field, 8^3 and 12^3 tori; Inglis cranking mass M = 2 sum \|<b\|dH/dPhi\|a>\|^2/(E_b - E_a)^3 in the zero-mean gauge; semiclassical slow roll. Results: (A) all 288 divergence-free separable face-sign patterns on the 2^3 cell end in the one pi-flux class (E = -1.19380 against -1.00243 at zero flux); E(Phi) falls monotonically on the scaled Kogut-Susskind path S and on the lowest path N (which carries the nesting vector (pi,pi,pi)); the uniform field is highest. Phi = 0 is a maximum: V = V0 - 0.0278 Phi^2 on S, E - E0 ~ -0.029 Phi^2 ln(1/Phi) on N. Random face flux already sits 29% down. (B) No flux pattern gaps the whole nested surface (m(k+Q) = -m(k)); S keeps a surface, N leaves zero-energy lines, and Dirac points appear only at Phi = pi. Z_S = [1/(32 pi) + (ln(16/Phi) - 1)/(32 pi^2)]/Phi + O(1), matched by the lattice to 0.3% at Phi = 0.05 pi: a finite field distance, not the plateau's 1/Phi^2. On N the stiffness grows with L (0.14, 0.34, 0.59 at L = 16, 32, 48), so the roll is damped into the sea. (C) On S with its own stiffness the roll is a log-corrected quartic hilltop: n_s = 0.948-0.949 at N* = 55 (rungs 0-4), 3.8 sigma below Planck, r < 1e-7, exit at Phi_end = 0.04-0.2 pi. The quartic coupling is rung-free, so P = 2.4e5 at rung 0 and ln(P/A_s) stays above 25 to rung 200: A_s cannot be met. (D) The parent face holonomy is the product of its four child faces, so children at pi read 0 at the parent; a faithful split gives children Phi/4 (x = 0.953 of the Lieb drop still to release) or, as a Z2 lift, x = 0.299; per-face flux is kept only at 0, 2pi/3 and 4pi/3. (E) pi flux is a stable minimum on S and N. (F) E(Phi) = E(-Phi), and +pi = -pi: no selector. Supplied: hop 1 and half filling, the face flux as a dynamical register, the adiabatic stiffness as the kinetic term, J a = sqrt3, M_P a = 1 at the flat rung, N* = 55, semiclassical FRW. | `claude/toe-pi-flux-fold-20261021` `2bd3b7b7a403` |
| #9987 | The link registers cannot supply the cube tick's pi faces, and the hop phases reduce to "minus one around every unit face" | logged | Spinless half-filled nearest-neighbour cubic sea (hop 1) and the CL-1 two-tiling cube tick (eps = 0.3, 0.8, 1.2; Floquet vacuum = negative quasi-energies filled, proper units = quasi-energy per tick / N), Bloch supercells up to 16x8x1 and 8^3, classical (static) link values, CL-3 magnetic term (1/g^2)(1 - cos Phi) l/S per loop. (A) With CL-1's fixed hop phases removed, registers laid out by the Links clause (B_f-block faces, crossing odd hops dressed) put flux only on the fine faces at block-edge segments (1/B_f^2 per orientation); every even-cube and inter-cube face reads 0 at every register value, so R_even is the bare hop and the pi-flux sector is unreachable at any g^2, B_f. What they can reach (pi on every block-edge loop) lowers the sea by 0.0351 (B_f = 2) and 0.0049 (B_f = 4) per site; an isolated pi flux line binds 0.018 per unit length, so the zero-flux photon vacuum fails at n_m g^2 > ~2/(0.018 B_f^2) (10.7 and 4.8 computed at B_f = 2, 4; 0.15 at B_f = 27). With the fixed phases the same flux costs energy (0.049, 0.016 per site), so the current law keeps a zero-flux register vacuum at every g^2, B_f. (B) A register on every matter edge: R^2 = 1 fixes only the cube faces; among all 128 R^2 = 1 odd-cube fields on the 2^3 cell the energy falls with every inter-cube pi face and is least at pi on every face (static and eps = 0.8). Against the CL-3 term read from 1, zero flux wins until n_m g^2 = 31.4 (static; 32.1, 39.3, 56.7 at eps = 0.3, 0.8, 1.2), then pi on every face; no partial pattern ever wins. (C) The sea's own magnetic response about pi is diamagnetic and log-growing (c = 0.042 to 0.078 per delta^2 for delta = 2 pi/8 to 2 pi/48), paramagnetic about 0 (about -0.005): the matter's magnetic minimum is at pi. CL-3's term read from 1 gives the photon about pi stiffness n_m c - 1/(2g^2); read from the vacuum holonomy it gives 1/(2g^2) + n_m c > 0 at every g. No element of SU(3) x SU(2) x U(1)_Y acts as -1 on every measured multiplet, so pi can sit only in a factor acting alike on all modes (fermion parity). (D) 'Phase -1 around every unit face' is equivalent to {W_i, W_j} = 0 on every cube, hence R^2 = sum w_i^2 for any positive weights; CL-1's spin-3/2 field is gauge-equivalent to it on every face; the tick with mass angle and copy mass, the copy-sign spectrum, the Dirac point, the dressed tick and the rotation covariance (half-turns anticommute: the double cover) are identical. (E) A dynamical face register cannot be passed at pi per face (Stokes); a flipped link costs 0.37. Supplied: hop 1, half filling, eps, classical link values, n_m. | `claude/toe-face-clause-unification-20261021` `7538d511b1f4` |
| #9990 | The split-epoch step in H is geometric, of order (H L)^2, with zero vacuum jump | logged | Under the candidate laws' split (children's edges at the parent's value minus s register steps, so the edge halves for every s) and the response law (Lambda a constant per proper 4-volume, vacuum standard on the same edges), the vacuum energy density does not jump at a split (exact 4-volume count). On the supplied cubic-frustum hinge carrier, with a triggered split keeping 8 pi G rho/3 continuous, ln H jumps by +(3/4)(H L)^2 per split (L the post-split edge), a sawtooth of period ln 2 in ln(1+z), exactly two steps in 0 < z <= 3 for any phase; the phase is not fixed by any law. Splits fire at a fixed local edge, so a spread of split times does not smear the step in 1+z; in a finite diagnostic with independent Born edge offsets at the register's wall-margin bound the fundamental keeps 0.988 of its size. With L = sqrt(8 pi) l_P the step is 2.6e-121 today and 5.4e-120 at z = 3; CPL fits give \|dw\| <= 5e-118 (rho_DE on z < 3) and <= 1e-112 (toy BAO + theta*), with the DESI sign pattern but some 1e110 below a 0.01 sensitivity. In the tensor spectrum of the discrete-tick toy, the period-ln 2 fundamental is second order (<= 1.1 (H l)^2), and the first-order structure is a fast lattice oscillation. Supplied: the carrier, the unit map, LambdaCDM numbers, the toy BAO errors, the Gaussian edge-offset model and the 1D tensor toy. | `claude/toe-split-step-hz-20261021` `67bda4c45526` |
| #9991 | Fold defects of the two-tiling tick are no dark matter, because the mass sign selects one gapped fold and a supplied fold-sign register is excluded by the domain-wall bound | logged | Single-particle two-tiling ticks of CL-1 (cube hop with face phases -1, even step eps - mu/2, odd step eps + mu/2, eps = 0.3, copy mass M, diagonal metric weights) in Bloch form on the 2^3 cell (k grids 6^3, 8^3), on Lx x 2 x 2 slabs with transverse twists (Lx = 32, 48; 8^2 twists) and on the 10^3 torus. Results: (A) law text: mu = mN with m >= 0 and lapse N > 0, so every species' mass angle has one sign in every cube; mu -> -mu is the (1,1,1) image (spectra equal to 8e-16); at fixed sign the vacuum is unique with gap exactly mu, including with M in [0, 0.25] and random diagonal metrics (gap/mu = 1.000 on 8 samples); the parameter space is contractible, so no fold wall, string or point is topological; the other fold costs ~1.3-1.5 mu^2 per site; a fold offset on the fixed Z^3 has no Burgers charge, and the two tilings admit no three-domain junction. (B) With a supplied mu-sign profile: a sharp wall binds 4 zero modes at zero transverse momentum (2+1D cones of the two copies); a staggered on-site phase D, a second mass direction adding in quadrature (gap 0.13826 at mu = D = 0.1), lets the wall unwind with gap >= 0.11; a closed cubic bubble (side 4) has no zero mode (lowest 0.097); the sharp-wall tension is sigma = c mu^2 per site^2, c = 0.40-0.69; the Fermi-ball binding ratio (12 pi sigma/g)^(1/3)/mu is 2.7-6.4 > 1 at every mu. (C) Estimates: with the supplied unit map, sigma^(1/3) = 8e3 GeV (electron), 0.17 GeV (0.05 eV neutrino), against the domain-wall bound (1 MeV); the passing re-seeds the same fold, so splits make no Kibble-Zurek defects. No dark-matter species from fold defects. | `claude/toe-fold-defect-dm-20261021` `7813a2f16076` |
| #9996 | A dark parity is kept exactly by the cube tick, but its abundance is fitted and its name-free form makes every Dirac neutrino massless | logged | Tests the candidate rule AX-5 (dark parity): one link-free species D is odd, and every term of the update other than the tick holds an even number of D modes. Exact checks on CL-1's tick (anticommuting face-phase -1 hops, copy sign, copy mass, both tilings): the copy sign s commutes with the tick at K = 0 only (5e-16; 0.235 at a random K), and the one-cube traceless strain vertex takes the heavy copy at rest to the light copy at recoil 0.87 M with amplitude 0.30 (M = 0.5) and 0.36 (M = 0.05), so no copy parity that equals s at rest survives CL-1's edge reading. On a real-space 4^3 torus with a random metric per cube and random links on a second species E, the update commutes exactly with the D projector, and D's block does not depend on E's links. In Fock space (4 + 4 modes, dim 256) the tick keeps (-1)^N_D, a one-D-mode term breaks it, and a pair term keeps it. The lightest D-odd state is D's light copy at rest (phase mu_D, 8^3 grid). With D taken as one family's nu^c, the Dirac neutrino matrix has rank 2. In the name-free form, where every zero-charge mode enters only in pairs, it has rank 0. The anti-smuggling gate FAILS: the abundance is fitted, the one-family form names nu^c, and the name-free form makes every neutrino massless under Z4, which the measured splittings contradict. Supplied model, finite diagnostic: (b, mu, M), the metric weights, the link phases, the charge table, the unit map, the graviton-exchange rate coefficient, g*, A_s, r, the measured Omega h^2 and the neutrino splittings. | `claude/toe-ax5-dark-matter-20261021` `873876f538f4` |
