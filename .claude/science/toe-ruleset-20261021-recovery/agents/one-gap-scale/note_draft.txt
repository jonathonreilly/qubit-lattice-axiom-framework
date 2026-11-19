---
claim_id: one_running_cell_coupling_sets_the_colour_to_weak_rung_ratio_but_fits_the_weak_and_seesaw_ranks_and_fails_for_the_electroweak_factors_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the rule 'one cell coupling for every link factor, renormalised along the zoom ladder by the modes each factor acts on; a factor gaps at the first rung where its coupling reaches its critical value; cell-local quartics act at the cell rung only': (exact) crossing rungs n_X = 2 pi (1/a_cell - 1/a_cX)/(b_X ln2), so at equal critical values rung ratios are fixed by the beta coefficients; content coefficients for SM, Sp(2N) with 4 Weyl fundamentals (+6 antisymmetric) and Casimirs from explicit generators; the only neutral colourless B-L = 2 scalar bilinear of a 16 is n^c n^c, where every content factor is trivial or repulsive; a cell quartic's strength falls as 2^-2n, so it gaps at the cell or needs a tune (G - G_c)/G = m^2 ln((1+m^2)/m^2); a hidden B-L = 2 condensate reaches n^c through a dimension-6 term (M_R rung = 3 n_S); the vacuum standard subtracts every condensation energy. Estimates against measurement: SU(3) at the cell lies 1.6% from 1/a = 16 pi (chance 5%), SU(2)_L 4% and U(1)_Y 32% off; AX-6's Sp(2) gives f << v; Sp(4) with 4 Weyl fundamentals gives f ~ 7-10 TeV (xi ~ 1e-3); top partners push it to f << v; the seesaw needs a new factor of b ~ 90-120; the mirror gap sits at the cell; no Lambda is set. The rule FAILS the anti-smuggling gate."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/one_running_cell_coupling_sets_the_colour_to_weak_rung_ratio_but_fits_the_weak_and_seesaw_ranks_and_fails_for_the_electroweak_factors_2026_10_22.py
---

# One running cell coupling sets the colour-to-weak rung ratio, but fits the weak and seesaw ranks and fails for the electroweak factors

Claim type: bounded_theorem.
Primary runner: `scripts/one_running_cell_coupling_sets_the_colour_to_weak_rung_ratio_but_fits_the_weak_and_seesaw_ranks_and_fails_for_the_electroweak_factors_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. It leaves four scales supplied: v/M = 1.0e-16 (rung 53.1 below M = hbar c/L = 2.44e18 GeV), a Z4-breaking seesaw scale at rungs 11-15, a mirror gap above 1.5 TeV (rung <= 50.5) and Lambda L^2 = 7.15e-121 (2^-399). This note writes one rule meant to set all of them from one cell coupling and tests it. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

## Rule tested (not adopted)

> "One running coupling. Every link factor has the same cell coupling. At rung n a factor reads that coupling renormalised over blocks of 2^n cells by the modes it acts on that are light at that rung. A factor's condensate forms, and its modes gap, at the first rung where its coupling reaches the factor's critical value. Cell-local terms that are not link factors act at the cell rung only."

Axiom bent: none by the clause itself (it is a CL-level reading of the zoom ladder). Its weak and seesaw parts need new modes per cell (the light-Higgs factor of AX-6 and a new seesaw factor), which bends Lattice through the role layout (AX-2) and is owner decision 3.

## Statement

A. Exact.

1. Crossing law. At one loop 1/a(n) = 1/a_cell - b n ln2/(2 pi), so n_X = 2 pi (1/a_cell - 1/a_cX)/(b_X ln2) and dn/d(1/a_cell) = 2 pi/(b ln2). The product n_X b_X is the same for all factors with the same critical value, so the coupling fixes rung ratios, n_s/n_w = b_w/b_s, and content fixes the rest.
2. Coefficients. SM: (U(1)_Y GUT, SU(2)_L, SU(3)) = (-41/10, 19/6, 7). Sp(2N) with 4 Weyl fundamentals (the SU(4)/Sp(4) coset that a light doublet needs, weak-scale C3): b = 11(N+1)/3 - 4/3, giving 6, 29/3, 40/3, 17 for N = 1 to 4. Adding the 6 Weyl antisymmetric top partners subtracts 4(N-1): 17/3 at N = 2.
3. Casimirs from explicit generators: Sp(2N) C2(F) = (2N+1)/4 and C_A = N+1; SU(4) 15/8, 9/2 (10), 5/2 (6); SU(2) 3/4 and 2 (3). The ladder critical value is a_c = pi/(3 C2(F)).
4. The Z4 channel. The colourless B-L = 2 Lorentz-scalar bilinears of one 16 are e^c e^c (Q = 2), e^c n^c (Q = 1) and n^c n^c (Q = 0). The only neutral one is n^c n^c, which is SM-trivial and Pati-Salam (10,1,3). There 2C2(F) - C2(R) is -3/4 for SU(4) and -1/2 for SU(2)_R, so both repel. No content factor binds a Z4-breaking pair.
5. Dimension counting. A cell quartic has strength g 2^-2n at rung n, so it gaps at the cell or not at all. n^c cannot carry a binder's charge, because L H n^c must stay invariant. A hidden B-L = 2 condensate therefore reaches n^c only through (n^c n^c)(chi chi)/M^2, which puts the M_R rung at 3 n_S.
6. Tuning law. For a mean-field cell quartic, (G - G_c)/G = m^2 ln((1+m^2)/m^2) in cutoff units (checked by quadrature to 1e-6). A 1.5 TeV mirror gap made by a quartic needs 2.6e-29, and a rung-12 condensate needs 1e-6. Only the running of a marginal coupling gives scales below the cell without a tune.
7. Lambda. The vacuum standard (CL-3) subtracts every condensation energy (toy pairing: condensation energy -0.28 and -0.74, response 0 to 1e-16). The rule therefore sets no Lambda.

B. Estimates against measurement (one loop unless stated).

1. Cell couplings from MZ: 1/a = (34.3, 48.6, 50.6) at one loop and (34.1, 48.3, 51.1) at two loops. SU(3) lies within 1.6% of the per-mode plaquette reading kappa T = 4 (1/a = 16 pi = 50.27). For a reading set spaced by factor 2 the chance of a hit this close is 5%, so this is look-elsewhere, not evidence. SU(2)_L is 4% off and U(1)_Y 32% off. The one-coupling clause fails for the electroweak factors.
2. Colour calibration. From 16 pi, colour reaches a_c at rung 62.2 (one loop) or 60.9 (two loops). f_pi lies 2.3 to 3.6 rungs lower, and that offset is used to convert any factor's crossing to its decay constant.
3. Light-Higgs factor at 16 pi, f rung at one/two loops. Sp(2) (AX-6's 8 Weyl modes): 77.2/76.2, so f << v and it fails. Sp(4) with 4 F: 48.3/47.6, so f ~ 7-10 TeV and v = f sin theta needs xi = v^2/f^2 ~ 1e-3 (5e-4 to 1.3e-3). Sp(6): xi ~ 1e-11. Sp(8): xi ~ 1e-15. Sp(4) + 6A (top partners): f << v. So the top Yukawa cannot come from partial compositeness inside this window, and with 4 F alone a cell-suppressed four-fermion term gives a negligible m_t.
4. The Sp(4) modes are SU(2)_L doublets. Above Lambda_HC = 3.4e4 GeV they lower 1/a_2 at the cell from 48.6 to 41.9, 17% from 16 pi.
5. Seesaw. A new factor is required (A4). Through the k = 3 transfer its b must be 89-117 (pure SU(24-32)) for M_R at rungs 14.9 to 11.4. k = 1 would need b = 30-39, but it is forbidden (A5). Its rank is a fit of M_R. Its spontaneous Z4 break keeps the two-vacuum walls that are excluded without dilution (neutrino-mass B4).
6. Mirror. With g/t >= 8 (block-quartic-smg) the symmetric gap is about 0.9 g at the cell, 50 rungs above the bound. This is an inequality, not a fit. The light-partner release (block-quartic-smg 5) is untouched.
7. Stability. f_HC rung = f_pi rung - (n_q - n_HC) changes by less than 0.1 rung over 1/a_cell = 50.27 to 51.07. That ratio is the one piece the coupling genuinely sets.
8. Lambda. Lambda^(1/4) is at rung 99.8. v^2/M (106.3) misses by 6.5 rungs (2^26 in Lambda), m3 (95.3) by 4.5 rungs (2^18), and m2 (97.8) by 1.9 rungs (about 200). Of 125 two-scale integer monomials of the rule's scales none lands within half a rung; the best is v f_HC/M (101.5). Lambda ~ m_nu^4 is a coincidence at about 1e2 to 1e5 and is not derived. An unmeasured m1 = 2.2 meV would be untestable numerology.

## Anti-smuggling gate (owner 2026-10-22): FAIL

1. Measured numbers chosen (FITTED): the cell coupling reading kappa T = 4, picked because it lands on alpha_s; the Sp(4) rank, picked from Sp(2N) N = 1-4 because it lands on v (with xi ~ 1e-3 still a continuous choice); the seesaw factor's rank, picked to land on M_R.
2. Observed structure inserted by name: the Sp(2N) hypercolour with its SU(4)/Sp(4) coset, a new SU(N_S), and the n^c n^c channel. Each was named because a measured structure needs it.
3. Unfitted predictions: (a) the common cell coupling for SU(2)_L and U(1)_Y. It FAILS: 4% and 32% off, or 17% for SU(2)_L once the Sp(4) doublets run. (b) The mirror gap at the cell passes, but only as an inequality that any g/t >= 8 meets. (c) The colour-to-weak rung ratio is a test only once the rank is fixed by something other than v, and nothing fixes it. Lambda: UNTESTED (the rule sets none).
4. Axiom bent: none by the clause. Its content needs new modes per cell (AX-2/Lattice, owner decision 3).
Verdict: reported as a failure, not adopted.

## Notes used or contradicted

- weak-scale (PR #9969): A1/A3 extend its transmutation algebra with critical values. It found the Sp(2) misses (n = 38 or 76); B3 sharpens this: Sp(2) fails at any reading consistent with colour, and Sp(4) is the only rank in the xi window. That contradicts AX-6's "8 new Weyl modes": the window needs 16, and then the top partners close it.
- neutrino-mass: its M_R rungs, k-type caps and wall exclusion are used. A4-A5 add that no content factor binds the Z4 channel and that the transfer triples the rung.
- block-quartic-smg: its g/t >= 8 symmetric gap is used. A5-A6 show it must sit at the cell rung.
- lambda-size-rule and register-size-s: A7 repeats their vacuum-share cancellation for condensates. B8 adds the power-law misses.
- main HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10 (alpha_LM^16 map): this note uses neither its map nor its coupling.

## Boundary

Running is one or two loops in the perturbative region, up to the ladder critical value. The decay constant comes from the colour offset, which is a one-parameter calibration. The xi window [1e-4, 0.1] is supplied. Not computed: the misalignment potential, m_H, threshold effects of the new factors on colour, and the lattice reading of a per-factor cell coupling. Not excluded: a rule that fixes ranks or the cell coupling from sites and updates alone.
