---
claim_id: a_fold_ladder_family_mass_rule_gives_rank_three_and_handed_cp_but_its_content_is_the_fitted_rungs_and_it_leaves_theta_bar_order_one_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For a candidate family mass rule in which each family multiplet is read on one rung of the zoom ladder, rungs bond to the newest three rungs, a contact spanning r rungs carries the nested block overlap 2^(-3r/2) and a handed phase exp(i h lam sin(r theta)) with theta = arccos(-2/3), and a mass term is the sum over monotone contact paths: exactly, nested block-uniform readings overlap by 2^(-3|a-b|/2) (to 2e-16); with singlets on rungs at or above the doublets the path-sum mass matrix has rank equal to the number of contact ranges (1, 2, 3; 40 seeded cases each); one range, or phases linear in r, are a rephasing and give J = 0 (2e-33); the sense flip h -> -h leaves masses and |V| unchanged and flips J; rung triples are on a half-line, so three distinct distances exist ((0,1,3)); at the example point no unitary other than the identity commutes with both sectors. Finite diagnostic: with 8 quark rung integers, lam and the sense bit all FITTED over 2.8e8 cells, the best point reaches rms log-deviation 0.27 on 4 mass ratios and 4 CKM numbers; the Boerdijk-Coxeter pitch fits worse than the median of 6 seeded random pitches (0.60 against 0.43), so the pitch is untested. With only the quark mass ratios fitted, the 601 fitting cells predict median |V_cb| 2.6 and |V_ub| 5.0 times the measured values, with all four CKM numbers within a factor 2 in 1.3% of cells; arg det(Mu Md) has median 1.59 rad and is never below 1e-3, against a measured |theta-bar| < 1e-10; Koide Q is within 1e-5 of 2/3 in none of 12648 lepton cells fitted to m_mu/m_tau; the pitch read as Brannen's phase gives m_e/m_tau twice the measured value. Supplied model, finite diagnostic: the rule itself, the multiplet-per-rung reading, the monotone path sum and its reversed-contact conjugation, lam, the sense bit, all rung integers, the scan ranges, the hit windows, the random pitches, and the measured running masses, CKM values and lepton pole masses."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_fold_ladder_family_mass_rule_gives_rank_three_and_handed_cp_but_its_content_is_the_fitted_rungs_and_it_leaves_theta_bar_order_one_2026_10_22.py
---

# A fold-ladder family mass rule gives rank three and handed CP, but its content is the fitted rungs and it leaves theta-bar of order one

Claim type: bounded_theorem.
Primary runner: `scripts/a_fold_ladder_family_mass_rule_gives_rank_three_and_handed_cp_but_its_content_is_the_fitted_rungs_and_it_leaves_theta_bar_order_one_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Today's family results give five requirements for a family mass rule. It must break cube-centred inversion and sigma_d K. It must keep no translation, turn or screw that acts on the families, or else |V| has a unit entry or J = 0. It needs at least two hop ranges. It needs one handed sense across the observed universe. And it must have low symmetry. This note writes a Froggatt-Nielsen-type rule built to meet all five and tests it against the 13 flavour observables. It meets the five structurally. It fails the anti-smuggling gate, because its rung charges are fitted. Its unfitted predictions are either disfavoured or excluded. Every check passes. Several PASS lines record that the rule fails. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs.

## Candidate rule (verbatim; not adopted)

> "Fold ladder. Each family's doublet and each of its singlets is read on one rung of the zoom ladder, as the block-uniform mode of that rung's block. Rungs bond to the newest three rungs. A contact spanning r rungs carries the overlap of the nested block readings and the handed phase exp(i h lam sin(r theta)), where theta is the fold's turn per rung and h is the sense of the light sector's handedness. The mass term between a doublet on rung a and a singlet on rung b is the sum, over monotone contact paths from a to b, of the product of contact weights; a path run in reverse carries the conjugate weights."

## Statement

A. Exact structure.

1. Overlap. Nested block-uniform modes on rungs a and b overlap by 2^(-3|a-b|/2). The rule's suppression per rung is therefore eps = 2^(-3/2) = 0.354, read off the 2x2x2 split rather than chosen.
2. Rank = number of contact ranges. If every singlet sits at or above every doublet, the path sum is G(b - a) = sum over k of c_k rho_k^(b - a), with one root rho_k per contact range. So M = X^T C Y has rank at most the number of ranges, and the runner finds equality in 40 seeded cases each for 1, 2 and 3 ranges. Two ranges would leave one massless family in every sector. The newest-three contact rule (the Boerdijk-Coxeter rule of `chiral-texture-family`) gives three massive families.
3. CP needs two ranges with non-linear phases. With one range, or with phases linear in r, the phase is a rephasing of the rung fields and J = 0 (2e-33). The invariants are phi_2 - 2 phi_1 and phi_3 - 3 phi_1. The sin(r theta) phases of a Dzyaloshinskii-Moriya-type term are non-linear in r, and at the example point they give J = -2.87e-5.
4. Sense. h -> -h conjugates every contact, so it conjugates M. Masses and |V| are unchanged, and J flips sign exactly. One sense gives one sign of J. Measured J > 0 picks h = -1 in the runner's convention, and that bit is fitted.
5. Rungs are a half-line, not a cyclic group of characters. There is no k -> -k, so the ceiling of `family-charge-search` (at most two distances for negation-closed triples) does not apply; (0,1,3) has three.
6. No shared unitary. At the example point the commutant of {M_u M_u^dagger, M_d M_d^dagger} is one-dimensional, so the mixing lemma of `chiral-texture-family` is met.

B. Fit (all FITTED).

7. The rung integers are scanned over 0-14, ordered with the doublets' lowest rung at 0, with lam in {1, 1.5, 2, 2.5, 3}. That is 2.8e8 cells. The best point is lam = 1.5, Q-rungs (4,1,0), u-rungs (13,10,7), d-rungs (6,5,4). It gives m_u/m_t 7.5e-6 (7.3e-6), m_c/m_t 3.9e-3 (3.7e-3), m_d/m_b 1.2e-3 (0.94e-3), m_s/m_b 0.026 (0.019), |V_us| 0.126 (0.224), |V_cb| 0.050 (0.041), |V_ub| 0.0049 (0.0038) and |J| 2.9e-5 (3.1e-5). The rms log-deviation is 0.27.
8. Look-elsewhere. Six seeded random pitches have median best score 0.43 and minimum 0.23, while the Boerdijk-Coxeter pitch scores 0.60. The fit does not prefer the fold's pitch, so the pitch is untested by the data. Exploration also found that eps = 0.3 fits as well as 2^(-3/2), so the derived eps is not tested either.

C. Predictions not used in the fit.

9. CKM given masses. Fitting only the four quark mass ratios (each within a factor 1.5) leaves 601 cells. Their median predictions are |V_us| 0.174, |V_cb| 0.108, |V_ub| 0.019 and |J| 4.4e-5. All four CKM numbers fall within a factor 2 in 1.3% of cells (random pitches: 0.1-0.9%). The rule over-predicts V_cb by 2.6 and V_ub by 5. This is disfavoured, not excluded.
10. Strong CP. The rule's phases sit in the contact weights, so arg det(M_u M_d) is generic. Its median over the 601 cells is 1.59 rad, and none of them is below 1e-3. The measured |theta-bar| is below 1e-10. The rule therefore needs a separate theta mechanism, or a bare theta cancelling to 1e-10, which is a tuning. As written, this is a failed prediction.
11. Koide. Fitting m_mu/m_tau on the same chain leaves 12648 lepton cells. Of these, 2.0% have Q within 1e-3 of 2/3, and none has it within 1e-5 (measured Q = 0.666664). The rule does not predict Q. Reading the pitch as Brannen's phase (delta = theta - 2 pi/3 = 0.2061, against 0.2222) gives m_e/m_tau = 5.8e-4 against 2.9e-4.
12. Rank three. No massless quark or lepton is a structural prediction, consistent with m_u != 0. It is weak, because three ranges were taken from a fold rule chosen with families in mind.

## Gate result (owner's anti-smuggling gate): FAILS

1. Measured numbers chosen: the 8 quark rung integers, lam and the sense bit are fitted to the masses and the CKM matrix. The 5 lepton rung integers are fitted to the lepton masses. That makes 13 integers, one coupling and one bit against 13 observables, so the rule's content is the fit.
2. Structure inserted by name: the rule reads doublets and singlets per family, which is observed particle content. It also ties the sense to the weak handedness, which is an observed chirality not yet in the laws.
3. Unfitted predictions: CKM given masses is disfavoured (1.3%). theta-bar is of order one, which fails measurement. Koide Q is not predicted. Rank three is consistent but weak. PMNS and neutrinos are UNTESTED.
4. Axioms bent: Admissibility, through rung contacts of range 2 and 3 (non-nearest in the zoom direction). Lattice ("no site is privileged"), through the rung role reading, as AX-2 does. It would need an AX-n entry if pursued.

## What survives, and what a replacement must do

These items are fit-free and rule-level, and a later rule can reuse them:
- the overlap eps = 2^(-3/2);
- rank equals the number of contact ranges;
- CP needs two or more ranges with non-linear phases;
- a single sense bit gives a single sign of J;
- half-line charges escape the cyclic distance ceiling.

A replacement must make the rung assignments follow from site, neighbour or update constraints rather than from the fit. For example, it could make a multiplet's rung its first-split generation under CL-1's split, or the depth at which its copy-sign sector first gaps. It must also produce arg det(M_u M_d) = 0 in the same structure, for example by putting the handed phases only in a sector whose determinant is real (Nelson-Barr-type). Neither is done here.

## Boundary

Not claimed:
- any derivation of the rung integers, lam or the sense link to weak chirality;
- non-monotone paths or Hermitian-chain resolvents;
- lepton mixing or neutrino masses;
- running between scales (approximate M_Z running masses are used for quarks, pole masses for the lepton Q);
- a physical reading of the contact phases beyond the stated form.

## Supplied vs forced

Forced, given the rule: items 1-6.

Supplied:
- the rule itself and the per-rung multiplet reading;
- monotone paths and reversed-contact conjugation;
- the sin(r theta) phase form and lam;
- the sense bit;
- all rung integers and scan ranges;
- the factor-1.5 and factor-2 windows and the random pitches;
- the measured values: m_u 1.23 MeV, m_c 0.620 GeV, m_t 168.26 GeV, m_d 2.67 MeV, m_s 53.16 MeV and m_b 2.839 GeV at M_Z (approximate literature values); |V_us| 0.2243, |V_cb| 0.0411, |V_ub| 0.00382, J 3.08e-5; lepton pole masses.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Candidate-law register](CANDIDATE_LAWS.md): CL-1 split and zoom ladder, AX-2 role reading.
- Context: today's drafts `mass-tower-law` (one-step cap, quarks exclude the copy form), `record-arrow-family-phase` (I or sigma_d K kept), `chiral-texture-family` (mixing lemma, Boerdijk-Coxeter newest-three rule, DM sense term), and `family-charge-search` (cyclic ceiling). Open PRs #9951 (zoom ladder adds no family charge; the rung depth used here is not a character, so it does not contradict it) and #9960. Main's historic intake `HISTORIC_CABIBBO_JARLSKOG_PREDICTION_2026_04_12_INTAKE_NOTE_2026-08-05.md` (a Z3 Froggatt-Nielsen texture, unaudited) is context only.

## How to run

```
python3 scripts/a_fold_ladder_family_mass_rule_gives_rank_three_and_handed_cp_but_its_content_is_the_fitted_rungs_and_it_leaves_theta_bar_order_one_2026_10_22.py
```

Seeded (20261022), runtime about 13-17 s, peak memory about 36 MB, AUDIT_TIMEOUT_SEC = 120, output 2.5 kB. Expected: TOTAL: PASS=13 FAIL=0.
