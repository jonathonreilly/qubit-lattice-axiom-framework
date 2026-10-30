---
claim_id: rule_fixed_dimension_six_liv_survives_time_of_flight_by_seven_orders_and_is_testable_in_uhecr_composition_and_photon_cutoff_bounded_theorem_note_2026-10-26
claim_type: bounded_theorem
claim_scope: "With the rule-fixed dimension-six dispersion (c_g = -S/24, c_q = -S/6 + 1/24 for quarks, leptons and neutrinos, E* = 1.217e18 GeV): (i) [F] composite universality holds for a 3-body light-front proton (Q1 FEM, converged to 3e-3, checked against an independent simplex discretisation): c_B/c_q = 0.214 (additive, HF-exact) -> 0.72-0.90 (1e19 eV) -> 0.997-0.999 (1e20 eV), with residual 1 - c_B/c_q ~ u^-1/2; gluon dressing (two Fock sectors, supplied) changes c_B by 6-8 % and the gluon is pushed to small x; (ii) [F] p -> p gamma and p -> p pi0 stay closed to 1e21 eV on axis and sky rays, but the u^-1/2 residual opens p -> p gamma at 5.3-6.0 EeV inside cones around the 8 body diagonals where |c_q| - |c_g| < ~1e-3 (1.8 % of the sky); (iii) [E] bound nuclei cannot follow the flow (the flowed state is their continuum): frozen at the nucleon level, spontaneous vacuum dissociation A -> N + (A-1) opens kinematically at d 3.5-6, He 5-9, N 9-17, Fe 19-32 EeV and reaches the Fermi core (k <= 0.25 GeV, supplied) at d 3.5-6, He 7-13, N 25-40, Fe 100-160 EeV (~1.8 A EeV); (iv) [T/F] e -> e gamma and gamma splitting are closed exactly; gamma -> e+e- opens at 8.0e16 (axis) to 1.1e17 eV (sky) and never on body diagonals; the gamma gamma_bg pair threshold shift is ray-independent (coefficient 1/96) and 5e-8 at 1.4 PeV; (v) [E] photon E_QG,2 = 4.2-7.3e18 GeV, 6.8-7.5 orders above the GRB 090510 and GRB 221009A subluminal quadratic bounds. Verdict: time of flight SURVIVES (>= 6.8 orders); UHECR composition and the photon cutoff are TESTABLE SOON."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/rule_fixed_dimension_six_liv_survives_time_of_flight_by_seven_orders_and_is_testable_in_uhecr_composition_and_photon_cutoff_2026_10_26.py
---

# The rule-fixed dimension-six LIV survives time of flight by seven orders; its sharp tests are UHECR composition and a 1e17 eV photon cutoff

Runner: runner.py. TOTAL: PASS=10 FAIL=0, 36 s, seeded, AUDIT_TIMEOUT_SEC = 120, 4.8 k characters, < 200 MB.
Criteria fixed before the run (criteria_pre_run.txt). Axioms unchanged; no CL edit; nothing adopted.
Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers, [S] reading.

## Builds on / narrows
- agents/composite-dispersion (2-body light-front flow to the most subluminal constituent). Extended here to
  3 bodies, gluon dressing, pion, and nuclei. It is confirmed for hadrons and NARROWED in two places: the body
  cone (ii) and nuclei (iii). Its line "nuclei inherit the same flow [S]" is contradicted.
- agents/uhecr-vacuum-emission and agents/liv-auger-confrontation: their proton walls (3.2-4.4 EeV) are removed
  off the body cones. Their nuclear walls are replaced by a dissociation channel that is stronger, not weaker.
- c_g, c_q, the S pattern and E* are inherited unchanged.

## Sources (fetched 2026-10-26)
- Vasileiou et al., PRD 87, 122001 (2013), arXiv:1305.3463: GRB 090510, E_QG,2 > 1.3e11 GeV (95 % CL, subluminal).
- LHAASO, PRL 133, 071501 (2024): GRB 221009A, E_QG,2 > 6e-8 E_Pl = 7.3e11 GeV (95 % CL, subluminal).
  Piran-Ofengeim, PRD 109, L081501 (2024), arXiv:2308.03031, give 5.8(4.6)e-8 E_Pl.
- LHAASO, PRL 128, 051102 (2022), arXiv:2106.12350: superluminal photon decay, E_QG,2 > 1e-3 M_Pl. The rules'
  photon is subluminal, so this bound does not apply; its analogue is the gamma -> e+e- threshold below.
  Highest photon about 1.4 PeV (LHAASO J2032+4102).
- Ellis et al., arXiv:1807.05155: TXS 0506+056 neutrino, M_1 >~ 3e16 GeV. The abstract gives no quadratic number.
  The n = 2 bound used here is computed from their ~10-day window, so it is mine, not theirs.

## Results
- [F] A1, 3-body proton. Setup:
  - Light-front longitudinal model, LMV pair confinement (m = 0.3, kappa = 0.6 GeV, supplied).
  - Q1 FEM in the Jacobi chart, graded to x ~ 1e-7.
  - Checks: the two grids agree to 2e-3; a 1/N-extrapolated uniform-simplex graph Laplacian agrees to <= 7e-3;
    Hellmann-Feynman holds to 1e-6.

  c_B/c_q by ray:
  | Ray | 1e18 eV | 1e19 eV | 1e20 eV |
  |---|---|---|---|
  | Axis | 0.214 | 0.901 | 0.9990 |
  | Sky | 0.214 | 0.857 | 0.9985 |
  | Body | 0.214 | 0.719 | 0.9969 |

  The residual 1 - c_B/c_q falls as u^-1/2 (slope 0.500, u = lam|c_q|), set by the spectators' m^2/x cost.
  So universality is ROBUST for 3 bodies.
- [F] A2, gluon dressing. Setup: |qqq> + |qqqg>, contact q -> qg (supplied g, m_g = 0.5 GeV), P_g(0) = 0.17.
  - The dressed/undressed c_B ratio is 0.924 -> 0.939 for u = 0.5 -> 20 GeV^2.
  - P_g falls 0.17 -> 0.04, and P_g <x_g^3> falls 6e-3 -> 2e-3.
  - So the less-subluminal gluon is expelled to small x, and the dressing does not leave a growing residual.
  - Limits: uniform grids, u <= 20 only, and the large-u value is not computed.
- [F] A3, emission with the full eigenstate dispersion (physical masses shifted in; supplied).

  Opening energy:
  | Model | Axis | Sky | Body |
  |---|---|---|---|
  | Frozen-additive control | 6.3 EeV | 6.0 EeV | 5.0 EeV |
  | Full eigenstate | closed to 1e21 eV | closed to 1e21 eV | 5.3 EeV |

  - The frozen control reproduces the parent wall.
  - p -> p pi0 with the full eigenstate is closed on all rays.
  - Body cone: opens for S <= 0.340 and is closed at S >= 0.350. That is a sky fraction of 0.018 around the
    8 body-diagonal directions. Scanning (m, kappa) = (0.2, 0.5) and (0.4, 0.8) gives 6.0 and 5.3 EeV.
  - Mechanism: on the body diagonal c_q = c_g = -1/72 exactly. The u^-1/2 residual adds a term linear in P to
    the composite energy, i.e. a speed offset of order M sqrt(2|c|)/E*. That makes the proton marginally faster
    than the photon there.
  - This is the one non-universal residual that opens a hadron channel.
- [F] A3d, GZK. The required head-on target energy for p gamma -> p pi0 is never below 0.03-0.05 eV (minimum at
  2-3 EeV) and grows to 2-14 eV at 1e20 eV. So photopion on the CMB is closed at all energies.
  - The photopion GZK horizon is absent [T-level kinematics, F-level dispersion].
- [E] A3c, nuclei.
  - A bound nucleus cannot follow the flow, because the flowed configuration (one nucleon carrying x ~ 1) has
    GeV relative momentum and IS the nucleon continuum. So nuclei are additive at the nucleon level, while each
    nucleon flows internally.
  - Spontaneous vacuum dissociation A -> N + (A-1) (S_n supplied) therefore opens kinematically:

  | Nucleus | Kinematic opening (EeV) | Reaches Fermi core, k_min <= 0.25 GeV (EeV) |
  |---|---|---|
  | d | 3.5-6.0 | 3.5-6.3 |
  | He | 5.3-8.9 | 7.1-13 |
  | N | 9.4-17 | 25-40 |
  | Fe | 19-32 | 100-160 |

  - For Fe, k_min = 10 GeV at 1.2 E_open (rate negligible) and 0.40 GeV at 1e20 eV (short-range-correlation
    tail). So the effective Fe wall is about 50-160 EeV, depending on the unsupplied nuclear tail.
  - Coherent A -> A gamma also opens kinematically (Fe 25-32 EeV), but the parent found it form-factor dead.
  - Near threshold the products are nucleons with about E/A each.
- [T/F] A4, leptons and photons (elementary, no flow).
  - |c_g| <= |c_q| on every ray, so the photon is the faster particle.
  - e -> e gamma is closed (exact: |c_e|(1 - (1-y)^3) >= |c_g| y^3).
  - gamma -> 2, 3 gamma is closed (exact concavity).
  - gamma -> e+e- opens at 8.0e16 eV (axis) and 1.1e17 eV (sky), and NEVER on body diagonals (c_q = c_g).
  - [T] The gamma gamma_bg -> e+e- threshold coefficient |c_g| - |c_q|/4 = 1/96 on every ray. Its shift is
    +5.2e-8 at 1.4 PeV: unobservable.
  - Crab 2 PeV electrons: the LIV/mass ratio in 1 - v is 3e-5.
- [E] B, time of flight. E_QG,2 = E*/sqrt(2|c|):
  - photon 4.22e18 (axis), 5.44e18 (sky), 7.30e18 (body) GeV;
  - lepton or neutrino 2.43e18, 3.56e18, 7.30e18 GeV.

  | Source | Axis delay | Margin in E_QG,2 |
  |---|---|---|
  | GRB 090510, 31 GeV | 5e-17 s | 10^7.5 |
  | GRB 221009A, 13 TeV | 1e-12 s | 10^6.8 |
  | TXS 0506 neutrino, 290 TeV | 4e-9 s | 10^7.2 |

  - A 1 s delay from z = 1 needs a 3.9e18 eV photon, which is impossible (gamma -> e+e- and background absorption).
  - Direction pattern: cubic l = 4 in S. Delay(body)/delay(axis) = 1/3, and neutrinos arrive after photons.
    The lattice orientation relative to the sky is NOT supplied by the rules, so it is 3 free angles in any test.

## Verdict (pre-registered rules)
- Time of flight (GRB, blazar, neutrino): SURVIVES, with a margin of >= 6.8 orders in E_QG,2 (>= 13.5 in delay).
  The quadratic delay can never be measured by time of flight.
- Photon sector: TESTABLE SOON.
  - The sharp prediction is a gamma -> e+e- cutoff at 0.8-1.1e17 eV, only 57x above the highest LHAASO photon.
  - It is absent within the body-diagonal cones.
  - One photon above ~1.2e17 eV from an off-body direction would falsify it. Running and planned tests: Auger/TA
    UHE photon searches, LHAASO-KM2A at its upper end, GRAND.
- UHECR sector: TESTABLE SOON. Nothing observed is excluded under the strict criterion, because protons survive to
  1e21 eV off the cones and no species-resolved flux above its dissociation energy is established. Predictions:
  - no photopion GZK horizon;
  - a mass-ordered breakup cutoff E ~ 1.8 A EeV (core) per species, with nucleons released at E/A;
  - an 8-fold set of 1.8 %-sky proton-depleted cones above ~5 EeV;
  - events above 1.6e20 eV (Amaterasu 2.44e20) must be protons, or nuclei above Fe.
  - Confronting Auger SD-DNN's heavy <lnA> ~ 3 at 50-100 EeV: N is broken up by 25-40 EeV, so survivors there
    are Si-Fe plus protons. This is IN TENSION if Auger's "no large light fraction" holds, and AugerPrime decides it.
- Overall: SURVIVES all current bounds. Sharpest LIV prediction: the composition and photon-cutoff pattern.
- [S] Coincidence, no claim: the core breakup scale of ~1.8 A EeV resembles Auger's fitted Peters-cycle cutoff
  Z x R_cut. With no GZK horizon, a 244 EeV proton from a void direction needs no nearby source.

## Smuggling review
- Forced (upstream [F], or exact here):
  - c_g, c_q and the S pattern;
  - light-front placement of the LIV in the mass operator;
  - Hellmann-Feynman additivity;
  - the flow direction;
  - the lepton and photon inequalities;
  - the 1/96 ray-independence;
  - the body-diagonal degeneracy c_q = c_g.
- Supplied:
  - all binding models (m, kappa, g, m_g);
  - the physical masses that are shifted in;
  - S_n, k_F = 0.25 GeV, and the frozen-nucleon-level nucleus;
  - LCDM (H0 = 67.4, Om = 0.315);
  - source energies and redshifts, and all bound values;
  - the 10-day neutrino window;
  - the lattice orientation (unsupplied, so a free parameter).
- No rule is proposed, so there is no gate. Nothing is fitted.

## Open
- Rates for vacuum dissociation and for the body-cone p -> p gamma; transverse dynamics; LIV inside the
  interaction kernel; the large-u value for gluon dressing; whether air-shower hadronic physics at 1e20 eV is
  altered (it would bias Xmax-based composition).
