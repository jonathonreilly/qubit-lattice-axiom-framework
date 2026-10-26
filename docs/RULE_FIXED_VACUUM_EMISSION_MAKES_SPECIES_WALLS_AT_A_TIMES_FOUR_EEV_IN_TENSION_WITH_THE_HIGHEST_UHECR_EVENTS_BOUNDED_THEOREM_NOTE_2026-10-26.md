---
claim_id: rule_fixed_vacuum_emission_makes_species_walls_at_a_times_four_eev_in_tension_with_the_highest_uhecr_events_bounded_theorem_note_2026-10-26
claim_type: bounded_theorem
claim_scope: "With the rule-fixed dimension-six dispersion (c_g = -S/24, c_q = -S/6 + 1/24, E* = hbar c/2L, L = sqrt(8 pi) l_P) and the supplied hadron-level parton additivity of agents/liv-auger-confrontation, the collinear golden-rule rate (normalisation checked against Frank-Tamm) for p -> p gamma, with the dipole form factor included, gives energy-loss lengths of 1-4e3 cm at 1.01 E_th and ~1 cm at 2 E_th. E_th = 3.24 (axis) to 4.44 EeV (body diagonal). Gamma_E ~ eps^1.2-1.5, so a 100 Mpc loss length sits within eps ~ 1e-19 of threshold: a sharp wall. p -> p pi0 (g^2/4pi = 13.7, axial dipole) opens later (6.7-21 EeV) and never sets the cutoff. For nuclei the coherent channel is kinematically open from ~sqrt(A) E_th but dead under a Gaussian charge form factor. The incoherent wall is A E_th/(1 + k_F/m) for a Fermi-gas core (Fe 144-188 EeV, N 36-47, He 10-13), and much lower (Fe 23-55 EeV) if the nucleon light-cone tail falls like e^{-s(alpha-1)}, s = 8-16.5 (supplied). Verdict: IN TENSION, not robustly excluded. Not covered: real nuclear large-momentum response, inelastic hadronic channels (they only shorten lengths), a spectrum/composition fit."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/rule_fixed_vacuum_emission_makes_species_walls_at_a_times_four_eev_in_tension_with_the_highest_uhecr_events_2026_10_26.py
---

# Rule-fixed vacuum emission builds per-species walls at about A x 4 EeV, in tension with the highest UHECR events

Runner: runner.py. TOTAL: PASS=9 FAIL=0, 4.6 s, seeded, AUDIT_TIMEOUT_SEC = 120, 3.9 k characters.
Criteria were fixed before the run (criteria_pre_run.txt). Axioms unchanged; no CL edit; nothing adopted.
Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers, [S] reading.

## Builds on
- agents/liv-auger-confrontation (same folder tree). It found kinematic openings (p -> p gamma from 3.2-4.4 EeV, p -> p pi0 from 7-21 EeV, nuclei at ~A x E_th) but computed no rates. This note supplies the rates.
- The c_g, c_q, W inputs are inherited unchanged.

## Rate formula [T/F]
- Collinear golden rule: Gamma = (1/16 pi P) int dy sum|M|^2 F^2.
  - k_perp^2 = y(1-y) D(y), where D = M_a^2(P) - M_b^2/(1-y) - mu^2/y.
  - The effective masses are M^2(K) = m^2 + 2 c K^4/E*^2.
- Vertices:
  - Spin 1/2 photon vertex: sum|M|^2 = 2 e^2 D (1+(1-y)^2)/y. The helicity-flip mass term is dropped, an O(m^2/D) correction.
  - Spin 0: 2 e^2 Z^2 D 2(1-y)/y.
  - pi0: g^2 (2 p.p' - 2 m^2).
- The form factor is evaluated at Q^2 = -mu^2 = 2|c_X| y^4 P^4/E*^2, which is exact (t = k^2).
- R1 check: in the constant-index, LI-fermion limit the formula reproduces Frank-Tamm to 1e-5.
- The same structure as the standard LIV vacuum-Cherenkov treatment (Jacobson-Liberati-Mattingly; Klinkhamer-Risse PRD 77, 016002 (2008), arXiv:0709.2502). Their bounds also take "threshold = cutoff" because the radiation length is tiny.

## Results
- [E] A1/A2: p -> p gamma (elastic; G_D^2 lower bracket, mu_p^2 G_D^2 = 7.8x upper).

| Ray | E_th (EeV) | l at 1.01 E_th | l at 2 E_th |
|---|---|---|---|
| Axis | 3.24 | 150 cm | 2 cm |
| Sky average | 3.67 | 160 cm | 2 cm |
| Body diagonal | 4.24 | 160 cm | 1 cm |

  - These rows use W at E*. With W at 2 GeV the thresholds are up to 4.44 EeV and the worst length is 3.7e3 cm.
  - A 100 Mpc loss length is reached at eps <= 7e-19 above threshold. The wall is sharp: no proton above E_th(n) reaches us from any source, galactic included.
- [E] B1: p -> p pi0 thresholds are 6.7-21.3 EeV, with l(1.01 E_th) < 2e2 cm. This channel is always above the photon wall.
- [E] C1: coherent nuclear emission is kinematically open from ~sqrt(A) E_th (Fe 24-31 EeV). Under a Gaussian charge form factor (supplied r_rms) the rate is negligible at all energies. A real large-q tail could matter, which is open.
- [E] C2: incoherent emission. The model is Z x nucleon elastic rate, with the nucleon at light-cone fraction alpha/A, a Fermi-gas core (k_F = 250 MeV, weight 0.8) and a tail 0.2 s e^{-s(alpha-1)}. E_cut is taken at l = 100 Mpc.

| Nucleus | Core only (EeV) | s = 16.5 (EeV) | s = 8 (EeV) |
|---|---|---|---|
| He | 10-13 | 3-4 | 2 |
| N | 36-47 | 10-14 | 6-7 |
| Si | 72-94 | 21-27 | 11-15 |
| Fe | 144-188 | 42-55 | 23-30 |

  - The tail slopes are a proxy from F2(x > 1) data and are supplied. Extrapolating them to the ~1e-25 probabilities needed here is unsupported, so the tail rows are a bracket, not a prediction.
- [E] D3: E_cut(body)/E_cut(axis) = 1.31 for every species. This is a cubic (l = 4) pattern in the maximum energy across the sky.

## Confrontation with data
- Protons:
  - Prediction: no protons above 3.2-4.4 EeV on any ray.
  - Auger Xmax fits give a proton fraction above ~5 EeV that depends on the hadronic model. ICRC17 (arXiv:1710.09478) says a small proton fraction "may persist" to the highest energies.
  - TA reads a lighter composition.
  - So this is TENSION: not established, and AugerPrime is projected to see a 10% proton fraction above 10 EeV.
- Composition floor:
  - lnA_min = ln(E/E_th) is 2.0-2.3 at 10^19.5 eV, 2.7-3.0 at 10^19.8 and 3.2-3.4 at 10^20.
  - Auger SD-DNN (PRL/PRD 2025) finds <lnA> ~ 3 with small spread at the top. It calls the data "incompatible with a large fraction of light nuclei between 50 and 100 EeV".
  - So the floor is CONSISTENT, but marginal at 10^20.
- Highest events:
  - Amaterasu: 2.44 (+-0.29 stat, +0.51/-0.76 syst) e20 eV.
  - The Fe wall (core only) is 144 (axis) to 188 (body) EeV, below the central value on every ray. It is consistent only for a body-like arrival ray with the low-side energy systematic, or for A > ~70 nuclei.
  - Fly's Eye ~3.2e20 eV (recalled, not fetched) is above every Fe wall.
  - With any exponential nucleon tail, the Fe wall falls below 1e20 eV, against the observed flux above 1e20 eV from Auger and TA. That case would be EXCLUDED.
- Verdict (pre-registered): IN TENSION.
  - The exclusion of the observed > 1e20 eV flux follows only under the supplied nuclear-tail model. Under the Fermi-core model it rests on the central Amaterasu energy, which the criteria do not allow as a basis for exclusion.
  - The deciding unknowns are the nuclear response at large momentum transfer and the proton fraction above 4 EeV.
- [S] Coincidence, reading only. The nucleon-level walls are p 3.2-4.4, He 13-17 and N 46-60 EeV. Auger's spectral features (arXiv:2008.06488) are the ankle 5.0, instep 13 and suppression 46 EeV.
  - The instep and suppression are softenings, as a He or CNO drop-out would give.
  - The ankle is a hardening, which does not fit a proton drop-out.
  - No claim is made.

## Model caveat (load-bearing)
- Hadron-level additivity (eigenstate dispersion c_h = sum <x^3> c_i) opens emission.
- A quark-level impulse accounting closes free-quark emission exactly, because |c_q| >= |c_g| on every ray and [x^3 - (x-y)^3] >= y^3.
- So whether protons radiate at all depends on how a composite's dispersion is assigned (the soccer-ball question). Rescue (ii) of the parent note removes every wall here.

## Smuggling review
- Supplied: PDFs and alpha_s (inherited); the form factors (G_D with 0.71 GeV^2, mu_p, M_A = 1.03 GeV, Gaussian r_rms); g^2/4pi = 13.7; k_F, S_n = 8 MeV and the nuclear tail s; the event energies and literature numbers; kappa = 1.
- Forced (upstream [F]): c_g, c_q and their angular forms.
- No rule proposed, so there is no gate.
