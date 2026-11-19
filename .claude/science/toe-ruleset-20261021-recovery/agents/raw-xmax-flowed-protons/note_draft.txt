---
claim_id: raw_xmax_sigma_above_46_eev_puts_a_pure_flowed_proton_beam_in_tension_decided_by_the_flowed_hadron_air_cross_section_bounded_theorem_note_2026-10-26
claim_type: bounded_theorem
claim_scope: "Against Auger's raw Xmax moments above 46 EeV (SD-DNN calibrated to FD, arXiv:2406.06319 Table 4: lgE 19.74/19.85/20.00, <Xmax> 787.2/794.5/793.9, sigma 20.7/25.1/21.8 g/cm^2; FD cross-check lgE>=19.5, 779.8 +- 5.0, sigma 26.5 +- 4.8, arXiv:1409.4809) and post-LHC p/Fe moments (generalized-Gumbel parametrization, arXiv:1903.03174), a seeded generalized Heitler-Matthews toy, calibrated two-point on each model's p and Fe, gives for a pure beam of flowed protons (x_lead = 0.995-0.998 at 46 EeV, 0.9990-0.9997 at 1e20 eV, from the upstream residual r ~ P^-2): (i) [F] a transparent flowed hadron (elasticity 1 - (1-x_lead)/2) does not make normal showers (Xmax > 1500 g/cm^2 in > 50 % of events): excluded outright; (ii) [F] every corner with flowed cross-section factor f_sigma <= 1 is excluded (worst pull >= 4.2, sigma(Xmax) decides); (iii) [F] the best pre-registered corner (f_sigma = 2) misses sigma(Xmax) by 2.2 combined sigma: TENSION; f_sigma 4-8 (post-registration extension) fits both moments within 1.6 sigma; (iv) [F] in every fitting corner N_mu is proton-like (0.97-1.01 x standard proton, while toy Fe/p = 1.19). Verdict: TENSION, not EXCLUDED; the decisive unknown is the air cross section of the flowed hadron, which the rules have not yet computed (no transverse dynamics upstream)."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/raw_xmax_sigma_above_46_eev_flowed_proton_beam_tension_2026_10_26.py
---

# Raw Xmax above 46 EeV puts a pure flowed-proton beam in tension, decided by the flowed hadron's air cross section

Runner: runner.py. TOTAL: PASS=9 FAIL=0, 18.7 s, 69 MB, seeded (20261026), AUDIT_TIMEOUT_SEC = 120, 3.8 k chars.
Criteria fixed before any data fetch or run (criteria_pre_run.txt). Axioms unchanged; no CL edit; nothing adopted.
Labels: [T] exact, [F] finite diagnostic in a supplied model, [E] estimate vs measurement, [S] reading.

## Builds on / narrows
- agents/nuclear-vacuum-breakup: its verdict "EXCLUDED unless the rules also alter air-shower development
  (uncomputed)" is NARROWED to TENSION. Its stated caveat is real: the flowed state changes the first
  interactions, and through them the Xmax-based reading of lnA.
- agents/composite-dispersion and agents/liv-surviving-observables supply x_lead. The 3-body residual
  1 - c_B/c_q = 0.001-0.003 at 1e20 eV, scaled as P^-2, reproduces their 1e19 value (0.10-0.30 vs 0.10-0.28).
  With two equal soft constituents, 1 - x_lead = r/3.

## Raw data used (RAW = detector-level moments, corrected for acceptance and resolution only)
- Auger SD-DNN, arXiv:2406.06319 (PRD 111 companion), Table 4. This Xmax is SD-estimated but calibrated to the FD
  scale; the DNN is trained on simulated showers, which is a caveat for exotic showers.

  | lgE bin | <lgE> | <Xmax> (stat; sys) | sigma (stat; sys) | N |
  |---|---|---|---|---|
  | 19.7-19.8 | 19.74 | 787.2 +- 2.0 (-7.5, +11.6) | 20.7 +- 1.4 (-4.8, +6.8) | 113 |
  | 19.8-19.9 | 19.85 | 794.5 +- 3.6 (-7.8, +12.2) | 25.1 +- 3.9 (-4.8, +6.8) | 54 |
  | > 19.9 | 20.00 | 793.9 +- 4.5 (-8.3, +13.1) | 21.8 +- 5.4 (-4.8, +6.8) | 26 |

  The DNN event-count column for 19.7-19.8 was ambiguous in the fetched text.
- Auger FD direct fluorescence, arXiv:1409.4809 (PRD 90, 122005), Table 4. The last bin is lgE >= 19.5 (<lgE> 19.62,
  N = 37): <Xmax> 779.8 +- 5.0 (+9.4/-6.9), sigma 26.5 +- 4.8 (+1.5/-1.6). The ICRC 2023 FD update
  (PoS(ICRC2023)319, 75210 events) gives its values in figures only, so it is not tabulated here.
- Model p/Fe moments: Arbeletche & de Souza, arXiv:1903.03174, Table 6 (generalized Gumbel; moments are mu + s(ln
  lam - psi(lam)) and s sqrt(psi'(lam))). As a check, the parametrization reproduces the ICRC 2013 Auger anchors
  (EPOS-LHC 806.1, QGSJetII-04 790.4 at 1e19 eV) within 1 g/cm^2.
  - At 10^19.74 the proton prediction is ~831 / 847 / 861 (QGSJetII-04 / EPOS-LHC / Sibyll2.3c), with
    sigma ~ 57-60. Iron is 736-760, with sigma 16.5-21.8.
- Muons: Auger hybrid 6-16 EeV (PRL 117, 192001; arXiv:1610.08509) found the hadronic signal 1.33 +- 0.16
  (1.61 +- 0.21) x EPOS-LHC (QGSJetII-04). There is no published muon number above 46 EeV.
- Auger arXiv:2401.10740 (10^18.5-10^19, 2239 hybrid events) prefers model Xmax shifted DEEPER (> 5 sigma). Any
  such shift only pushes every proton-like prediction further from the data, so it is not used to help the rules.
- TA hybrid above 10^19.5 is statistics-limited (parent note). It does not decide.

## Results
- [F] A, model check: proton/iron moments as above.
- [F] C, toy calibration.
  - The toy proton has sigma 53.4.
  - The variance mapping sigma^2 = sigma_p,model^2 + (toy^2 - toy_p^2) gives Fe sigma 26.5/21.8/28.6 against the
    model 21.8/16.5/21.3. So the toy OVER-estimates sigma for multi-subshower showers by about 5-7 g/cm^2.
    This bias works AGAINST the rules.
  - The mean is mapped two-point per model (p and Fe).
- [F] D, flowed corners. Values are (f_sigma, kappa, f_N): prediction at 19.74 for <X> and sigma | worst pull
  over the three bins:
  - f_sigma = 1/3: 1018-1079, 150-185 | 5.6-6.6, 13.9-16.0. Excluded (a single-quark cross section).
  - f_sigma = 1: 823-893, 53-58 | 4.2-4.9 on sigma. Excluded (a flowed proton is still a single-particle shower).
  - kappa = 1 - (1-x_lead)/2 (transparent): Xmax 2400-3300, every shower lost. Excluded outright.
  - f_sigma = 2, standard kappa: 771-830, 32-34 | 0.4-1.7 on X, 2.2-2.5 on sigma. TENSION.
  - Extended (post-registration, stated): f_sigma = 4 gives 743-799, 27-28 | <= 1.8; f_sigma = 8 gives 731-789,
    26 | <= 2.4. Low elasticity U(0, 0.4) changes little.
  - N_mu/N_mu,p = 0.97-1.01 in every non-transparent corner, against toy Fe/p 1.19 (the toy understates the
    model value of ~1.3-1.4).
- [F] E: pure standard protons give worst pulls of 2.0 on <X> and 4.9 on sigma. <Xmax> alone does NOT exclude
  protons once the three-model spread (~30 g/cm^2) is included; sigma(Xmax) does.
- [F] G, FD cross-check (lgE >= 19.5).
  - Best pre-registered corner: 830 / 36, pulls 1.6 / 1.2.
  - Standard proton: 840 / 59, pull 5.2 on sigma.
  - The direct-fluorescence bin agrees with the DNN.

## Verdict (pre-registered rule: the most favourable pre-registered corner decides)
TENSION (2.2 combined sigma). The deciding measurement is sigma(Xmax) in the SD-DNN 19.7-19.8 bin (20.7 +- 1.4, +6.8
sys, 113 events), backed by FD lgE >= 19.5 (26.5 +- 4.8).
- With the toy's known +5-7 g/cm^2 sigma over-estimate removed, or with f_sigma >= 4, it becomes CONSISTENT.
- With f_sigma <= 1 it is EXCLUDED at >= 4.2 sigma.
- So the parent's EXCLUDED rests on an assumption, not a measurement: the flowed hadron interacting like a standard
  proton.

The question becomes whether the flowed hadron's inelastic air cross section is >= ~2 x sigma_p-air (>= ~1.1 b at
1e19.7 eV), with standard (string-breaking) elasticity.
- [S] This is not implausible in rule terms. In a light-front picture with confinement in the boost-invariant
  variable zeta^2 = x(1-x) b^2, the soft constituent at x_s ~ (1-x_lead)/2 ~ 1e-3 sits at b ~ b0/sqrt(x_s), about
  30 b0. A color string from the leading quark across 10-20 fm would be broken by most passing air nuclei, which
  gives a large sigma, and each break re-fragments the leading quark (kappa ~ standard).
- If instead the cloud is stripped without disturbing the leading quark, the shower never develops (corner i),
  which is excluded.
- Neither transverse picture is derived. Upstream has longitudinal dynamics only.

## What AugerPrime adds
SSD + WCD (+ radio) give a per-event muon/EM split above 46 EeV. A flowed-proton beam that mimics heavy Xmax keeps
a PROTON-like muon number: in the toy, N_mu is about 1.0 x proton against about 1.2-1.4 for Fe. So the falsifier is a
joint (Xmax-like-heavy, N_mu-like-proton) signature. Given the existing 6-16 EeV muon excess (1.33-1.61 x models),
a proton-like N_mu above 46 EeV would deepen the muon deficit sharply. If AugerPrime finds N_mu rising toward
heavy values with energy, the flowed-proton escape closes. A second test is the shape of the Xmax distribution: for
f_sigma = 2 the deep tail is exponential with slope ~ lambda_p/2 ~ 20 g/cm^2, which is distinguishable from a
Gaussian-like heavy peak only with >~ 1e3 events.

## Smuggling review
- Forced or upstream: x_lead (r ~ P^-2 from the 3-body FEM); the flow threshold 5e18 eV (half-way scale); the
  breakup wall <= 46 EeV.
- Supplied:
  - the whole toy (lambda_p from Auger's 505 mb at 10^18.24 with E^0.045, N_ch = 41.2 (E/PeV)^0.2, kappa ~ U(0.1, 0.8),
    1/3 to pi0, Greisen profiles, pion decay at 20 GeV);
  - the bracket f_sigma, kappa, f_N, which is NOT derived from the rules;
  - the two-point calibration to model p/Fe;
  - the data and parametrizations.
- Nothing is fitted to the >46 EeV data. No rule is proposed, so there is no gate.
- Deviation from the pre-registration: the f_sigma >= 4 and kappa-low corners were added after the run and are
  labelled extended; the verdict uses the pre-registered grid only.

## Open
- Derive the flowed hadron's transverse size and its air cross section from the rules (3-body light-front with
  transverse dynamics, kernel LIV).
- The muon number above 46 EeV (AugerPrime).
- The Xmax tail slope.
- A full Monte Carlo (CONEX with a modified first-interaction generator) to replace the toy.
