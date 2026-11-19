---
claim_id: wall_local_electroweak_registers_are_realisable_on_a_confining_layer_bulk_but_chosen_and_leave_stable_fractional_charges_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Layered strong-coupling toys and exact group-theory checks for R1b/R4: can the rules realise X1 (wall-local electroweak link registers, shared colour, with a Gauss-law repair)? Exact: the strong-coupling strip identity (interior links of L mixed plaquettes give sum_n u_n^L e^{in theta}); the layer mass operator has one flat zero mode with ordered inter-layer links and exactly two wall-supported zero modes with disordered links and gapped bulk layers; in a gauge-dressed layer chain the near-wall charge rho_0 - E_0 commutes with the update (0 vs t for an undressed far-only register); per-wall anomalies of one 16 under its own SU(2) x U(1) with shared SU(3) all vanish; the 16 is vector-like under exactly {SU(3)} and {SU(2)} (two maximal shareable sets); no light-mirror quark bilinear is gauge invariant with H^a H'^b; mirror-quark hadrons carry our charge 1/3 mod 1 and are stable; QCD with 12 flavours has b0 = 3. Leading-order strong coupling: inter-wall stiffness K = 2u^(Ls-1) (U(1)), 4u^(Ls-1) (SU(2)) below mean-field ordering for bulk beta <= 1.16 / 2.45 at Ls = 4; kinetic mixing u^(4(Ls-1)). Finite: transverse unit-flux gap A-independent at strong coupling (1.758 at A = 4 and 10), falling with A at weak coupling (ratio 0.39). Estimates (supplied numbers): wall/bulk coupling ratio ~10-15x supplied; flat colour needs Ls <~ 5 for an isotropic 5D bulk value ~3; thermal mirror overcloses (Omega_e' h^2 >= 0.67) and leaves fractional charges; avoiding both needs supplied T_RH < m_u'/25, which removes the Delta N_eff signal. Not covered: Monte Carlo of the anisotropic 5D phase diagram, the CL-1 cell slab, interacting wall fermions with strings, a derivation of the couplings, v' or T_RH."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - face_swap_parity_gives_a_tree_level_zero_theta_only_with_wall_local_electroweak_registers_and_shared_colour_bounded_theorem_note_2026-10-24
  - the_adopted_link_rule_puts_one_gauge_field_on_both_slab_walls_so_a_separate_mirror_world_needs_a_new_link_rule_and_a_supplied_temperature_asymmetry_bounded_theorem_note_2026-10-24
runner: scripts/wall_local_electroweak_registers_are_realisable_on_a_confining_layer_bulk_but_chosen_and_leave_stable_fractional_charges_2026_10_24.py
---

# Wall-local electroweak registers are realisable on a confining layer bulk, but chosen, and leave stable fractional charges

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers, [S] reading.
Runner: runner.py, TOTAL: PASS=14 FAIL=0, 0.25 s, 79 MB peak, 2.6 k characters, seeded, AUDIT_TIMEOUT_SEC = 120.
Tested under a unique filename (wall_local_electroweak_test_run.py in the scratchpad, removed after the run).
Axioms and register unchanged; no rule adopted. Criteria were written before code (criteria_pre_run.txt).
Pre-set mismatches (recorded, not tuned away):
- P5 predicted the strong-coupling flux gap ~ g^2/2 within 10%. Measured 1.758 vs 2.0: the unit flux hops at
  first order (band bottom 2 x_p = 0.25), so the gap is g^2/2 - 2x_p = 1.75. The A-independence held exactly.
- P10 predicted the uniform-coupling confining order SU3 > SU2 > U1. The beta signs and Casimirs order that way, but
  at the cutoff 1/alpha_2 = 48.7 and 1/alpha_3 = 50.6 are nearly equal (SU(2) slightly stronger), and U(1) is the
  strongest. The conclusion (nothing singles out SU(2) x U(1) to confine) survives; the stated ordering did not.

Repo first. git grep of origin/main for Dvali-Shifman, "layered phase", Fu-Nielsen and fractionally charged hadrons:
nothing. Builds on face-swap-parity (PR #10079: X1 statement, BCS shape, v' window, Delta N_eff) and mirror-world
(PR #10069: flat zero mode A1, uniform commutant A2, Gauss leak A2g/h). Literature cited as supplied: Dvali-Shifman
1997; Fu-Nielsen 1984 layered phase; Barr-Chang-Senjanovic 1991; deconstruction (Arkani-Hamed-Cohen-Georgi).

## A. Confining bulk between Coulomb walls (Q1)

Setup: layers are a physical extra direction with their own inter-layer link registers (owner decision 5). Wall layers
have weak-coupling 4D plaquettes; bulk plaquettes (4D and mixed) are at strong coupling beta_b.
- A1 [T]. A strip of L mixed plaquettes with its interior links integrated gives exactly
  (2 pi)^(L-1) sum_n I_n(beta)^L e^{i n theta} (rel. err 1e-15). So the near-far wall link chain
  Phi = prod U_5 has, at leading order, stiffness K = 2 u^(Ls-1) (U(1), u = I1/I0) and 4 u^(Ls-1) (SU(2),
  u = I2/I1, O(4) normalisation).
- A2 [T/E]. K lies below the mean-field ordering value (0.25, 0.5; mean field underestimates the true value, so
  this is conservative) for bulk beta <= 1.16 (U(1)) and <= 2.45 (SU(2)) at Ls = 4, and up to 4.2 / 11.3 at Ls = 16.
  Phi is disordered: <Phi> = 0, so A_near - A_far gets no Higgs mass.
- A3 [T]. Layer mass operator: ordered links (Coulomb bulk) give 1 flat zero mode (mirror-world A1). Disordered links
  plus gapped (confined) bulk layers give exactly 2 zero modes, each supported on ONE wall (cross weight 0).
  This is the deconstruction reading of Dvali-Shifman: two massless wall gauge sectors G_near x G_far.
- A4 [T, leading order]. The inter-wall kinetic mixing is the 4-strip tube, eps ~ u^(4(Ls-1)): 4e-8 at Ls = 4,
  1e-37 at Ls = 16 (beta_b = 0.5).
- A5 [F]. Unit flux through a bulk bond layer, on a transverse ring of A sites (|E| <= 1). At strong coupling
  (g^2 = 4) the gap is 1.758 at both A = 4 and 10: flux is quantised and costs a fixed amount per bond, so moving
  charge between walls costs a string ~ sigma Ls. At weak coupling (g^2 = 0.5) the gap falls 0.341 -> 0.133
  (Coulomb: flux spreads, which is mirror-world's flat mode).

Answer to Q1: YES at the toy level. Each wall carries its own massless gauge mode, and inter-wall charge transfer is
gapped by the flux string, not leaked.

## B. Gauss-law repair (Q2)

- B1 [T]. Dressed layer chain (Lc = 5, links |E| <= 1, Kogut-Susskind hop dressed by the bond link):
  ||[H, rho_0 - E_0]|| = 0 and every bulk Gauss operator commutes. The undressed far-only register of mirror-world
  gives ||[H, Q_far]|| = t = 1. So the repair is: keep the inter-layer EW link registers (exact 5D Gauss law), and
  let the bulk be confining. The near-wall charge seen by the near photon is rho_0 - E_0, and the bulk flux E_0 is
  gapped. In this sense the bulk fermion modes' EW charge is carried only by neutral (string-closed) composites.
- B2 [F]. A near-wall bound state (|1-m| = 0.4 tail) in its own charge sector: the string sigma*s makes the tail
  super-exponential (Ls = 16: 9e-7 at sigma = 0, 1e-12 at 0.5, 7e-19 at 2; log-slope -1.67 -> -2.25). The charge it
  shows the far photon is 0 exactly (sector label), not |1 - m|^(2 Ls).
- B3 [T]. Each wall's 16 is anomaly-free under its own SU(2) x U(1) with shared SU(3): Y^3, Y-grav, SU(2)^2 Y,
  SU(3)^2 Y, SU(3)^3 = 0, and the doublet count is 4 (Witten). No inflow (Chern-Simons) term is needed per wall.

Answer to Q2: YES. The half-slab charge is exactly conserved as rho_left - flux; the flux is gapped at strong coupling.

## C. What decides which factors are wall-local (Q3)

- C1 [T]. Subsets of {SU3, SU2, U1} under which one 16 is vector-like: exactly {SU3} and {SU2}. These are two maximal
  shareable sets, and neither contains the other. "Share every factor the wall content is vector-like under" is
  inconsistent, because {SU3, SU2} jointly is chiral. Sharing SU(2) instead of SU(3) puts the mirror in OUR doublets,
  and that is face-swap B4 (N_nu = 6, excluded). So X1's "colour shared" is a CHOICE between two rule-equal maxima.
  The tiebreak (e.g. by dimension, 8 > 3) is untested and post hoc.
- C2 [E]. Beta signs b = (41/10, -19/6, -7) and Casimirs (3 vs 2) make colour the most confining in the IR. At the
  cutoff (1-loop SM) 1/alpha = (34.3, 48.7, 50.6), and the wall lattice betas are SU(2) 15.5 and U(1)_Y 4.6. A
  confining EW bulk needs beta_b <~ 1, i.e. bulk couplings ~10-15x the wall couplings for EW factors only, while colour
  stays weak in the bulk. The rules fix register sizes and flavours per factor by supply. Nothing forces this split:
  SUPPLIED.
- [S] Expressibility. The Links clause already reads each factor at its own rung B_f. X1 maps onto it: colour's B_f
  block contains all layers (hops undressed, one shared register), while each EW factor's B_f block is one layer
  (dressed inter-layer registers at strong coupling). That needs the layers to be a physical direction (owner decision
  5) and per-role (wall vs bulk) register strengths.

## D. Consequences (Q4)

- D1 [T]. Shared colour with 6 light + 6 mirror flavours: b0 = 11 - 8 = 3 > 0, so QCD stays asymptotically free.
  (b1 = -50: massless 12 flavours would sit near the conformal window, but the mirror is heavy at v'.)
- D2 [E]. 1/alpha3(cutoff) is 31.2 (v' = 1e8) and 35.6 (v' = 1e11), vs 50.6 (SM); no Landau pole. Tension: flat
  colour across Ls layers has per-layer beta3 = 14.9/Ls. Staying above an isotropic 5D bulk value ~3 (supplied,
  uncertain) needs Ls <~ 5, against the Ls ~ 16 used for wall overlaps. Anisotropy may relax this (not computed).
- D3 [T]. Mirror quarks have zero OUR hypercharge. A light-mirror bilinear would need 6Y_q in 3Z, which is impossible,
  so no H^a H'^b dressing ever mixes them. Mirror-quark number mod 3 is conserved (colour triality), and a colour
  singlet containing one u' has our charge 1/3 mod 1. The lightest (u' qbar, u' q q) is an ABSOLUTELY STABLE
  FRACTIONALLY CHARGED hadron. Proton / mirror-baryon conversion needs (udd)(u'd'd')^dagger at dim 9, so it is
  negligible, and the proton is stable.
- D4 [E, supplied]. If T_RH > m_q' the mirror thermalises through shared gluons (T' = T):
  - mirror electrons (alpha' = alpha by P_slab) give Omega h^2 = 0.67 at v' = 1e8 and 7e5 at v' = 1e11;
  - stable coloured relics, n/n_B >~ 1e-12, face fractional-charge searches at <~ 1e-20 per nucleon.
  Both are EXCLUDED. A supplied T_RH < m_u'/25 (35 GeV at v' = 1e8, 3.5e4 GeV at 1e11) avoids them. But the mirror then
  never thermalises, so face-swap's Delta N_eff 0.19-0.64 prediction goes to ~0.

## Verdict

- X1 REALISABLE: yes, consistently, on a confining-layer bulk.
  - It keeps an exact Gauss law.
  - Each wall has its own massless gauge sector, and the walls connect only through a string gap and eps ~ u^(4(Ls-1)).
  - Each wall is chiral and anomaly-free.
- But CHOSEN, not forced:
  - a physical layer direction (owner decision 5; bends the Lattice axiom);
  - per-role register strengths (EW bulk strong, colour bulk weak; ~10-15x, supplied);
  - a tiebreak between two maximal shareable sets;
  - Ls <~ 5 tension for flat colour (estimate).
- New exact consequence: stable fractionally charged mirror-quark hadrons. With a thermal mirror they are excluded,
  along with mirror-electron overclosure. That forces a supplied low T_RH, which kills the route's one unbuilt
  prediction (Delta N_eff).
- Walls move. Next tests:
  - an anisotropic 5D Monte Carlo of the layered phase (colour Coulomb, EW confined);
  - a principled share rule (does a fermion-number-conserving mass criterion pick {SU3} uniquely?);
  - a route that lets u' decay, e.g. a field charged under both walls' hypercharges. That needs a bifundamental
    register, which is a new rule.

## Gate (for X1 with the confining-bulk repair)

1. Measured numbers: none chosen to pass. The coupling ratio and T_RH are supplied, and T_RH is set by bounds, so it
   is FITTED-type.
2. Named structure: the rule names no group. But the choice between {SU3} and {SU2} is made to match BCS, so it is a
   smuggling RISK until a tiebreak is derived.
3. Prediction: stable fractional charges (excluded unless T_RH is low), Delta N_eff (lost at low T_RH), and
   eps ~ u^(4(Ls-1)). Net status: UNTESTED, with a measured tension.
4. Bends: the Links clause (per-role strengths, per-factor rungs) and the Lattice axiom (physical layers, decision 5).

## Smuggling review

- Supplied:
  - the strong-coupling regime and the mean-field ordering values;
  - the |E| <= 1 truncation;
  - the 0.4 tail;
  - the SM inputs: 1/alpha at MZ, b coefficients, PDG quark masses, 246 GeV, 2.4e18 GeV cutoff;
  - the 5D bulk value ~3;
  - the relic and search numbers;
  - the content of the 16;
  - the literature mechanisms.
- Forced:
  - the strip identity;
  - the zero-mode counts;
  - Gauss commutation;
  - per-wall anomaly cancellation;
  - the two-maxima enumeration;
  - b0 = 3;
  - the no-mixing/triality theorem.
- No measured number was chosen to pass anything.
