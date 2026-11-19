---
claim_id: transmutation_removes_the_weak_scale_tuning_but_only_colour_binds_a_doublet_pair_and_no_rule_vacuum_has_a_misalignment_angle_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the candidate laws' chiral content (one 16 per family, three families, read as SM or Pati-Salam multiplets) and the register's link, rishon and edge registers: (A) exact one-loop coefficients from the content; the colourless |Y| = 1/2 doublet pairs are exactly q u^c, q d^c, L e^c, L n^c, and the only non-abelian factor holding both members of any of them is colour; one-loop transmutation gives v/M = 2^-n with |d ln v/d ln alpha_cell| = n ln2 (37 for the measured hierarchy), and with the per-mode plaquette count as the cell coupling n = 8 pi^2 kappa T/(b0 ln2), whose readings miss the needed n = 53.1 by at least 10 rungs; (B) the SU(2)_L centre acts trivially on every link, edge and fixed-per-bond-number rishon configuration, so a Y = 1/2 doublet composite contains one of the (A) pairs; at mean field its scalar sits at twice the constituent mass; (C) every nonzero colour-singlet pair condensate (psi chi bilinear or pair-square 10) breaks SU(2)_L x U(1)_Y at its own scale with no misalignment angle (v = f), and a vacuum-standard subtraction leaves the scalar's cell-sized mass coefficient unchanged. Estimates against measurement (colour, top-pair, technicolor-like, bubble 125 GeV scalar) are separate. No weak-scale mechanism inside the content is established; the replacement-rule requirements are sharpened."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/transmutation_removes_the_weak_scale_tuning_but_only_colour_binds_a_doublet_pair_and_no_rule_vacuum_has_a_misalignment_angle_2026_10_22.py
---

# Transmutation removes the weak-scale tuning, but only colour binds a doublet pair and no rule vacuum has a misalignment angle

Claim type: bounded_theorem.
Primary runner: `scripts/transmutation_removes_the_weak_scale_tuning_but_only_colour_binds_a_doublet_pair_and_no_rule_vacuum_has_a_misalignment_angle_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its weak-interaction entry is conditional on a supplied Y = 1/2 doublet register and a fitted v. Measured: v = 246.22 GeV, a narrow scalar at 125.1 GeV, and v/M = 1.0e-16 with M = hbar c/L = 2.44e18 GeV, the register's cell rung (the register's "about 1e-17" uses a Planck-size M). The register's four-mode route needs (G - G_c)/G_c of order 1e-34 (2.3e-34 on the lattice cone; 4e-34 on the sphere |k| < pi/a for m a = 1e-17) or a top above 235 GeV. This note asks whether the scale can be generated rather than tuned, in three ways: (a) a fermion-pair condensate whose binding coupling runs to criticality after n rungs; (b) the scalar as a bound configuration of neighbouring registers; (c) a symmetry, or the vacuum standard of the response law, that keeps a scalar light. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the content, couplings or the doublet.

## Statement

A. Dynamical breaking.

1. Exact. The one-loop coefficients follow from the content (b > 0 means asymptotically free). They are b = (-41/10, 19/6, 7) for U(1)_Y (GUT normalisation), SU(2)_L and SU(3) with three families and one doublet scalar. In the Pati-Salam reading they are (40/3, 6) for SU(4) and SU(2)_L with one family, and (32/3, 10/3) with three. An Sp(2) factor on four Weyl doublets has b = 6.
2. Exact. Take a pair of one family's left-handed multiplets that is a colour singlet, an SU(2)_L doublet and has |Y| = 1/2. The only such pairs are q u^c, q d^c, L e^c and L n^c. In every one of them exactly one member is an SU(2)_L doublet, so SU(2)_L never holds both members. Colour holds both members of the two quark pairs. No non-abelian factor holds both members of the lepton pairs. So in the present content, colour is the only factor that can bind a doublet-channel pair.
3. Exact. At one loop the binding scale is Lambda = M exp(-2 pi/(b0 alpha_cell)), so v/M = 2^-n with n = 2 pi/(b0 alpha_cell ln 2). For any b0 the sensitivity is |d ln v/d ln alpha_cell| = n ln 2, which is 36.8 for the measured hierarchy (n = 53.1). Transmutation therefore replaces the four-mode route's 1e-34 tuning with an ordinary sensitivity of 37. The price is that 1/alpha_cell must be fixed to about 1 part in 70: a factor 2 in v corresponds to d(1/alpha_cell) = b0 ln2/(2 pi), which is 1.18 for three-family Pati-Salam and 0.66 for Sp(2).
4. Exact, then estimate. If the cell coupling is the per-mode plaquette count, 1/alpha_cell = 4 pi kappa T, then n = 8 pi^2 kappa T/(b0 ln 2) is fixed by the content once a reading is chosen. The readings kappa T = 1/2 to 16 give:

   | factor | n over the readings |
   |---|---|
   | PS SU(4), 3 families | 5.3, 10.7, 21.4, 42.7, 85.4, 170.9 |
   | PS SU(4), 1 family | 4.3, 8.5, 17.1, 34.2, 68.3, 136.7 |
   | Sp(2), 4 doublets | 9.5, 19.0, 38.0, 75.9, 151.9, 303.8 |

   The readings double n at each step. The closest misses 53.1 by 10.4 rungs, a factor of about 1e3 in v. With 18 readings spaced by a factor 2, a hit would be look-elsewhere, not evidence.

B. The scalar as a neighbourhood composite.

1. Exact. Global SU(2)_L transformations are a symmetry. The centre element -1 acts as Ad(-g) = Ad(g) on every link register. It acts trivially on edges, which are singlets. A rishon string that keeps each bond's rishon number fixed (the register's exact per-bond U(F)) has even length, so the centre acts trivially on it too. Products of adjoints carry integer spin only (checked up to adj^4). The doublet has centre charge -1. So no configuration of links, rishons and edges, at any zoom, is a doublet. Links and edges carry Y = 0. A Y = 1/2 doublet therefore needs an odd number of doublet fermion modes, and a boson needs a singlet fermion as well. The lowest such composite is one of the A2 pairs, possibly dressed by links (split across a bond by a link, for example), and the dressing does not change its charges. The neighbourhood route therefore reduces to route (a), with colour as the only binder (A2).
2. Finite diagnostic. Take mean-field four-mode binding on a 20^3 single-cone lattice at G = 1.3 G_c (m = 1.656/a). The pseudoscalar pole is at q0 = 0, the three eaten modes (1 - Pi_P(0) = 2e-16). The scalar sits at the threshold 2m (1 - Pi_S(2m) = 2e-9), and there is no scalar zero below 2m. Both locations are identities of the gap equation at any coupling above critical. A bubble composite's scalar is therefore at 2 m_f, not lighter.

C. Protection.

1. Exact. Let Sigma = <psi chi> be a colour-singlet condensate, with psi in 2_L x N families and chi in 2_R x N, transforming as Sigma -> g_L Sigma g_R^T. Every real combination of SU(2)_L generators is invertible, so a nonzero Sigma leaves at most one U(1) of SU(2)_L x U(1)_Y unbroken (the maximum over 62 sampled vacua is 1, and Sigma = 1 leaves T3L - T3R). SU(2)_L acts on one index only, so the charged-W mass is sum_(a=1,2) |T_a Sigma|^2 = |Sigma|^2/2 for every Sigma. It depends only on the condensate's size: v = f, with no vacuum angle. No vacuum keeps SU(2)_L x U(1)_Y and then misaligns slightly, so there is no pseudo-Goldstone doublet with v << f.
2. Exact. Consider the pair square's 10 = (6,1,1) + (1,2,2). Colour fixes only the 4-dimensional (1,2,2) block, and colour together with SU(2)_L fixes no direction. A colour-safe pair condensate n therefore breaks the weak group at its own scale. Its 9 Goldstones are a colour triplet (6 real, colour Casimir 4/3, Y = -+1/3 from the (6,1,1)) plus 3 eaten modes. This answers the walls-table question for the pair-condensed phase: its light composites are colour-triplet scalars, not a light doublet.
3. Exact contrast. Four Weyl doublets of a pseudoreal factor give the SU(4)/Sp(4) vacuum manifold, Sigma_theta = cos theta Sigma_B + sin theta Sigma_H. There m_W^2(theta)/m_W^2(pi/2) = sin^2 theta exactly, so v = f sin theta, and theta = 0 keeps SU(2) x U(1). This is the structure a light pseudo-Goldstone doublet needs. By A2, no pseudoreal factor of the content holds a doublet pair (SU(2)_L and SU(2)_R pairs are colour or charge breakers). rung-higgs's SU(4) x SO(5) bulk is the same kind of supplied coset.
4. Exact. The vacuum standard (CL-3: edges and links respond only to departures from the vacuum, in the vacuum's own units) subtracts the vacuum's value. That value is a constant in the condensate, so the cell-sized m^2 coefficient of the sea energy is unchanged: dE/d(m^2) = -2 I0 = -0.910/a^2, the same before and after subtraction. A subtraction that moved with the condensate would make the potential identically flat and would fix no v. A shift symmetry of a linear doublet has the same consequence, since a shift-invariant gauge-invariant potential is constant. The dressed-cone clause constrains the kinetic term only. H^dagger H is a Lorentz scalar invariant under every kept symmetry (centre, SU(2)_L, Y, colour, rotations, inversion, the antiunitaries), so no clause of the laws forbids the scalar's mass term.

## Estimates against measurement

These are estimates, not theorems. The inputs are alpha_s(MZ) = 0.1180, f_pi = 92.1 MeV, g = 0.6517, gauge couplings at m_t, y_t(m_t) = 0.936, and S = -0.05 +- 0.07 (U = 0).

| route | v/M obtained | scalar | what is supplied | measured comparison |
|---|---|---|---|---|
| colour condensate (the only binder in the content) | 6.5e-20 (v = sqrt3 f_pi) | broad sigma at the QCD scale | nothing new | alpha_s(v) = 0.104 vs alpha_c = pi/(3 C_F) = 0.785 (x7.6 short); m_W = 52 MeV vs 80.4 GeV |
| top-pair condensation (four-mode, cutoff up to the cell) | any, with a 1e-31 to 1e-34 tune | bubble 2 m_t = 345 GeV (RG-improved >= 244, composite-doublet) | four-mode coefficient near critical | y_t(m_t) = 1.281 at the cell, 1.480 at 1e10, 2.368 at 1e4 GeV vs 0.936 |
| PS SU(4) technicolor-like (A4 readings) | 2^-42.7 = 1.4e-13 or 2^-85.4 = 2e-26 vs 1.0e-16 | heavy and broad (several f) | SU(4) unbroken down to v (it confines leptons; excluded) | S = 0.21 (1 doublet, 3.7 sigma), 0.64 (3 doublets); T = 0 (custodial) |
| bubble composite at 125 GeV | — | 2 m_f, so m_f = 62.6 GeV | K degenerate coloured chiral states | with K = 3: ln(Lambda/m) = 102 vs 38.2 to the cell; at the cell K >= 8.01, so 10 states: S = 0.27 (4.5 sigma) |
| pseudo-Goldstone doublet (C3 contrast) | f sin theta; f from transmutation | set by the explicit breaking; not fixed by the laws | a new pseudoreal factor, four new Weyl doublets per cell, top couplings to them | the Sp(2) readings give n = 38.0 or 75.9 vs about 53 (f near 1 TeV) |

## Candidate law text (tested, not adopted)

> "Weak scale. Each cell carries four further fermion modes forming the doublet of a further link factor Sp(2), with SU(2)_L x U(1)_Y charges (2, 0) + (1, +1/2) + (1, -1/2); the factor's cell coupling is the per-mode plaquette count; the weak doublet is the Goldstone of their Sp(4)-preserving pair condensate, and its vacuum angle is the stationary point of the response law's total phase including the top's Yukawa-type term."

Smuggling check. The four modes are not in CL-1's update, which gives one 16 per family, so they are new content and need the owner. Once the modes exist and the update commutes with Sp(2), the Sp(2) link follows from the link rule rather than being supplied. The count reading is a choice, and it fails: n = 38.0 or 75.9 against about 53. The top's coupling to the condensate needs a further four-mode or partial-compositeness term, which is supplied. The vacuum angle and m_H are not computed. The text therefore turns the 1e-34 tuning into a list of supplied structures plus a sin^2 theta of order 0.1, and with the count rule it misses v by a factor of about 2^15. It is recorded as a tested candidate, not a working law.

## Notes used or contradicted

- ew-transmutation (probe runner): A1 rederives its coefficients and A2 rederives its binder statement (B4). The rung count n = 8 pi^2 kappa T/(b0 ln 2) and the sensitivity statement are new. Its C2 look-elsewhere warning applies to A4.
- composite-doublet (probe runner): its 2.3e-34, m_t >= 235 GeV and m_H >= 244 GeV are used. The one-loop y_t(m_t) = 1.281 at the cell matches its 1.283. C1 to C2 here extend its D1 (no light state "without a further symmetry"): within the content no vacuum supplies that symmetry.
- rung-higgs (C3): the depth N of about 49 to 52 is unfixed, consistent with the count misses here. Its SU(4) x SO(5) bulk is the supplied coset of C3.
- PR #9920 (masses read from a response-set field force a Y = 1/2 doublet): consistent. B1 adds that this field cannot be any configuration of links, rishons or edges.
- main: COMPOSITE_HIGGS_MECHANISM_NOTE_2026-05-03 (a Z3 multi-channel scalar with 1/3 suppression): its suppression is already contradicted by composite-doublet C2, and C1 adds that whatever the channel weights, v = f.
- main: HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10 (v_cand = M_Pl (7/8)^(1/4) alpha_LM^16, a declared candidate map): like transmutation it has an ordinary sensitivity (-4 per ln <P>), but it has no condensate, no scalar and no m_t, and its magnitude is supplied by alpha_bare^16. Not used, not contradicted.
- PR #9906 (the cube tick keeps a chiral weak SU(2) only at step pi/2) was not read in detail.

## What a weak-scale law must now do (replacement requirements)

1. Supply an asymptotically free binder that holds both members of a colourless |Y| = 1/2 doublet pair (A2: colour is the only one in the content, and it is 7.6 times too weak at v).
2. Fix that binder's cell coupling to about 1.5% (A3). The plaquette count's readings are a factor 2 apart in n (A4).
3. For a 125 GeV narrow scalar, give a vacuum manifold with a misalignment angle, that is a pseudoreal binder with an Sp-type coset (C1 to C3). A bubble scalar sits at 2 m_f (B2), and a 125 GeV bubble is excluded by S (B3).
4. Give species-dependent Yukawa-type weights coupling the families to the composite (unchanged).

Zoom check: a coarser rung does not change gauge representations, so B1 and A2 hold at every zoom. The rung count enters only through n, which is where the hierarchy could be generated if requirement 2 were met.

## Boundary

The theorems are exact algebra or identities on the stated content. B2 is a mean-field diagnostic on a supplied band. The estimates use measured inputs and one-loop running. Nothing here derives the doublet, v, m_H or the Yukawa-type weights, and nothing excludes a weak-scale law built from new content.
