---
claim_id: composite_dispersion_flows_to_the_most_subluminal_constituent_and_closes_hadron_vacuum_emission_bounded_theorem_note_2026-10-26
claim_type: bounded_theorem
claim_scope: "For bound states whose constituents carry the rule-fixed dimension-six dispersion (c_g = -S/24, c_q = -S/6 + 1/24, E* = 1.22e18 GeV): (i) [T] at first order in the lattice correction the composite coefficient is exactly parton-additive, c_B = sum_i c_i <x_i^3> (Hellmann-Feynman); (ii) [T] Z^1 cos-band pair with on-site attraction: P^4/P^2 ratio = -1/12 + t^2/(U^2 + 16 t^2), additive (x 1/4) for binding << bandwidth, universal for binding >> bandwidth; Z^3 contact pairs (U_c = 7.91 ~ bandwidth) are all lattice-sized and universal with the S pattern; (iii) [F] in a supplied boost-covariant light-front two-body model the LIV enters the mass operator as lambda sum c_i x_i^3, lambda = 2P^4/E*^2, and the ground state's effective coefficient rises monotonically from the additive value to min_i c_i = c_q, half-way at P_x ~ 5 EeV, the same scale as the additive emission threshold; (iv) [F] p -> p gamma (ground state -> ground state + link-band photon) opens at 4.3-6.7 EeV with the frozen additive wavefunction and stays CLOSED to 1e20 eV on axis, sky-average and body rays with the full eigenstate, in 3 models and a 4-point binding scan. Not covered: transverse dynamics, >2-body light-front states, LIV inside the interaction kernel, nuclei, relaxation dynamics."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/composite_dispersion_flows_to_the_most_subluminal_constituent_and_closes_hadron_vacuum_emission_2026_10_26.py
---

# A composite's dimension-six coefficient flows to its most subluminal constituent, closing hadron vacuum emission

Runner: runner.py, TOTAL: PASS=9 FAIL=0, 6.8 s, seeded, AUDIT_TIMEOUT_SEC = 120, 3.4 k characters.
Criteria fixed before the run (criteria_pre_run.txt). Axioms unchanged; no CL edit; nothing adopted.
Labels: [T] exact, [F] finite diagnostic, [E] estimate, [S] reading.

## Builds on / narrows
- agents/liv-auger-confrontation (G1, G2) and agents/uhecr-vacuum-emission: both SUPPLIED parton additivity
  c_h = sum <x^3>_i c_i with rest-frame (2 GeV or E*) PDF moments. This note decides what the rules give.
- c_g, c_q and their S patterns from agents/assumed-inputs-model (A1/A2/B), inherited unchanged.
- No prior composite-dispersion note on origin/main (git grep).

## Results
- [T] A1 (Z^1, cos band, on-site -|U|). Closed form E(P) = -sqrt(U^2 + 16 t^2 cos^2(P/2)), checked against the
  Lippmann-Schwinger root to 4e-15. Ratio of the P^4 to P^2 coefficient = -1/12 + t^2/(U^2 + 16 t^2):
  U/t = 0.05, 1, 4, 20, 200 give 0.250, 0.294, 0.625, 0.971, 1.000 x the constituent ratio -1/12.
  Additive (x^2 = 1/4 at x = 1/2) when binding << bandwidth; universal when binding >> bandwidth.
- [F] A2 (Z^3, exact LS via the Bessel/Laplace reduction). U_c = 7.91 is of order the bandwidth 12, so every
  contact bound state is lattice-sized; at U/U_c = 3, 30, 300 the ratio is 0.98-1.07, 1.000, 1.000 x -S/12 on
  axis, face and body rays. The cubic S pattern is carried unchanged.
- Lesson of A: universality in the lattice frame needs a composite whose internal momenta are cell-scale.
  Hadrons are 1e19 cells across, so A alone would say ADDITIVE. But A uses a frame-fixed potential, which is
  not boost covariant; for UHECR the relevant regime is P >> M, handled in B.
- [T] B1. In light-front form the constituent energies are x_i P + (k_perp^2 + m^2)/2x_iP + c_i x_i^3 P^3/E*^2,
  so the LIV enters the mass operator as lambda(P) sum_i c_i x_i^3, lambda = 2P^4/E*^2. At first order the
  composite coefficient is <sum c_i x_i^3>_0 (Hellmann-Feynman, numerically 1.000005). This is the parent's
  additivity, and it is exact only while lambda |c| << M0^2.
- [F] B2/B3. With a supplied Li-Maris-Vary longitudinal confinement the ground state at fixed P rearranges as
  lambda grows: momentum flows to the most subluminal constituent, because c < 0 rewards large x^3.
  - c_B/c_q (sky ray): qq 0.400 -> 0.928 (1e19 eV) -> 1.000; quark + Lorentz-invariant spectator
    0.074 -> 0.894 -> 1.000; quark + gluonic spectator 0.211 -> 0.894 -> 1.000.
  - Half-way at P_x ~ 5e18 eV, i.e. P_x ~ (M0^2 E*^2 / 2|c|)^(1/4). This is the SAME scale as the additive
    threshold, because both are set by lambda |c| ~ M0^2. So the frozen-PDF assumption fails exactly where the
    parent's tension lives.
- [F] B4. p -> p gamma (collinear, ground state -> ground state + photon with c_g):
  | model | frozen additive (axis/sky/body) | full eigenstate |
  |---|---|---|
  | qq | closed / 1.6e19 / 5.6e18 eV | closed / closed / closed |
  | q + LI spectator | 4.3e18 / 4.7e18 / 5.0e18 | closed / closed / closed |
  | q + gluonic spectator | 6.0e18 / 6.3e18 / 6.7e18 | closed / closed / closed |
  The frozen rows reproduce the parent's 3.2-4.4 EeV walls at the same scale. The full rows stay closed to
  1e20 eV, and also for (m1, m2, kappa) = (.1,.5,.4), (.3,.9,.8), (.4,.6,.5), (.2,.7,.6) GeV.

## Verdict (pre-registered rules): UNIVERSAL, in this precise form
- The law: c_B(P) = min over the bound state's wavefunction at fixed P of the mass operator; it equals
  sum c_i <x_i^3>_0 for P << P_x and tends to min_i c_i (here c_q, the copy-shifted fermion band) for P >> P_x,
  with P_x ~ (M0^2 E*^2/2|c|)^(1/4) ~ EeV for hadrons.
- Additivity is the correct FIRST-ORDER statement and is what an EFT matrix element gives at low P. It is not
  valid at UHECR energies, where the LIV term exceeds the binding scale in the mass operator.
- Consequence: the parent walls (protons above 3.2-4.4 EeV, Fe at 144-188 EeV) are artifacts of the frozen
  wavefunction; the ruleset survives the highest-event confrontation. The tension note should be narrowed.
- Side consequences [E/S], not computed here:
  - Photopion: with p and pi both at c_B ~ c_q, the final state costs 3|c_q| x(1-x) P^3/E*^2 extra (~2e-5 GeV
    at 1e20 eV, sky), so GZK stays closed (as in the parent F1); the observed suppression must be a source
    or propagation effect of nuclei.
  - Nuclei inherit the same flow (momentum to the most subluminal nucleon, then quark), so incoherent walls also
    close [S].
  - Hadronic delta_had,2 = 2 c_q/E*^2 at UHECR energies (sky -7.9e-56 eV^-2) is about 18x the additive 2 GeV value (-4.3e-57),
    still of the sign Auger does not scan; magnitude-only comparison now exceeds 1e-57 by ~80x. This must be
    rechecked against any n = 2 analysis that does treat negative coefficients.

## Smuggling review
- Forced (upstream [F]/[T] here): c_g, c_q with S patterns; light-front kinematics putting the LIV into the mass
  operator as lambda sum c_i x_i^3 (requires only |k_i| << E* and interactions smooth on the cell scale);
  Hellmann-Feynman additivity at first order; the direction of the flow (c < 0 -> toward max x^3).
- Supplied: the binding (on-site U in A; Li-Maris-Vary longitudinal confinement with m, m_s, kappa in B);
  2-body truncation, no transverse motion; the spectator's coefficient (0 or c_g); neglect of LIV inside the
  exchange kernel (it enters at the same order lambda and could shift P_x); the assumption that the fixed-P
  eigenstate is reached (light-front energy scale M0^2/2P ~ 1e-10 GeV at P_x, i.e. a ~1e-4 cm formation length,
  shorter than the parent's cm emission lengths, but not computed dynamically).
- No rule proposed, so no gate. Nothing fitted.

## Open
- A 3-body light-front proton with gluons, a transverse check, and the exchange-kernel LIV.
- Recheck agents/liv-auger-confrontation E/H and uhecr-vacuum-emission with c_B(P) instead of frozen weights.
