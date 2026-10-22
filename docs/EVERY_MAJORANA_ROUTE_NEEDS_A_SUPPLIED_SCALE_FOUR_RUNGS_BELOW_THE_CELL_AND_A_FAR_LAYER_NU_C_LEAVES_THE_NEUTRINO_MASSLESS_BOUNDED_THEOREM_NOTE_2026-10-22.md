---
claim_id: every_majorana_route_needs_a_supplied_scale_four_rungs_below_the_cell_and_a_far_layer_nu_c_leaves_the_neutrino_massless_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For one chiral 16 per family with the register's supplied term list (Yukawa-type, uddn-class, (nu^c)^4) and its Z4 = i^(B-L): (A) every Majorana-type neutrino mass (nu^c nu^c, L L H H, a mirror N N or L H N) has Z4 charge 2, every Dirac-type term charge 0, and registers carry no B - L, so only a lepton-number-2 matter condensate or an explicit bilinear can break the Z4; a condensate leaves exactly two vacua; any number of heavy neutral states of mass >= M gives ||m_nu|| <= ||Y||^2 v^2/M, and a vector-like Dirac seesaw gives m_D mu/M; conjugate mirror singlets that mix with nu^c leave 3 - rank light massive neutrinos; in the register's square layer slab a far-layer (reversed) nu^c puts its mirror on the light layer and leaves the neutrino exactly massless, and at the smoothed-layer wall height M = 1 the far-layer overlap is zero at rest; a mirror-free index-1 slab for nu^c gives the Dirac mass y0 v sqrt(1-q^2) q^(Ls-1)/sqrt(1-q^(2Ls)) (finite diagnostic). (B) Estimates with measured inputs: inverted ordering excluded by Sigma < 0.064 eV; at every law-fixed scale even NDA strong coupling gives m3 <= 3e-3 eV (17x short), so a Majorana route needs a supplied scale at least 4.1 rungs below the cell (12.4 at y = 1); a spontaneous Z4 break there makes walls excluded without dilution; the far-layer slab restates y_nu by (q, Ls), cannot share one slab with the charged species, and a nu^c on the doublet's rung misses by >= 1e8 either way. No mechanism inside the laws gives m3; the replacement requirements are sharpened."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - supplied_chiral_terms_keep_a_z4_of_b_minus_l_and_leave_strong_cp_unfixed_bounded_theorem_note_2026-10-22
  - far_layers_reading_a_smoothed_field_decouple_the_mirror_from_field_strength_but_not_from_gauge_turns_topology_or_long_wavelengths_bounded_theorem_note_2026-10-22
runner: scripts/every_majorana_route_needs_a_supplied_scale_four_rungs_below_the_cell_and_a_far_layer_nu_c_leaves_the_neutrino_massless_2026_10_22.py
---

# Every Majorana route needs a supplied scale four rungs below the cell, and a far-layer nu^c leaves the neutrino massless

Claim type: bounded_theorem.
Primary runner: `scripts/every_majorana_route_needs_a_supplied_scale_four_rungs_below_the_cell_and_a_far_layer_nu_c_leaves_the_neutrino_massless_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its neutrino entry is conditional: nu^c is the Dirac partner of nu (the Z4 of B - L forbids nu^c nu^c and L L H H), y_nu ~ 3e-13 is supplied, any seesaw at a rule scale gives at most 3e-4 eV, and a coarse-rung nu^c restates the hierarchy. Measured: sqrt(dm^2_31) = 0.050 eV, sqrt(dm^2_21) = 0.0087 eV, Sigma < 0.064 eV (DESI DR2 + CMB). This note asks for a mechanism inside or just beyond the laws that gives m3 ~ 0.05 eV without a supplied number, along four routes: (a) a Weinberg term at a law-fixed scale; (b) a spontaneous Z4 break giving a Majorana nu^c mass; (c) a nu^c localised on the far layer of the layer slab (a split-fermion overlap); (d) mirror-family mixing with nu^c. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

Repo check: origin/main holds a legacy (2026-04, pre-reset) lane, DM_NEUTRINO_ATMOSPHERIC_SCALE_THEOREM_NOTE_2026-04-15 (m3 = y^2 v^2/M_1 with M_1 = M_Pl alpha_LM^8 (1 - alpha_LM/2), y = g^2/64, unaudited), and many NEUTRINO_MAJORANA_* and NEUTRINO_LANE4_* notes from the same period; none uses the current register's content, Z4 or layer slab. Open PR #9925 (the Z4 of B - L) is the symmetry input used here. No open PR or main note covers split fermions, a far-layer nu^c or the seesaw cap at the register's scales.

## Statement

A. Exact.

1. Z4 charges. Z4 = i^(B-L) on colour-singlet operators. L H nu^c and nu^c N carry 0; nu^c nu^c, L L H H, N N and L H N carry 2 (N is a conjugate mirror singlet with B - L = -1). Edge, link, rishon and doublet registers carry no B - L, so no register, fold or edge configuration can break the Z4. Only a matter condensate of lepton number 2, or an explicit bilinear, can do it. A Weinberg term (a) and a Majorana nu^c (b) both need the break.
2. Vacua. A charge-2 condensate breaks Z4 to Z2 and leaves |Z4/Z2| = 2 degenerate vacua, phi and -phi. The spontaneous route makes domain walls.
3. Seesaw cap. For any number of heavy neutral states with mass matrix M_h (all singular values >= M) and couplings Y to L H, ||Y M_h^-1 Y^T|| <= ||Y||^2/M. The runner checks this on 300 random instances with 1 to 30 heavy states. A vector-like singlet pair (the Dirac seesaw) gives the light Dirac mass m_D mu/M. With v as the only light scale, every route is capped by (coupling)^2 v^2/M.
4. Mirror mixing (d). Z4 allows nu^c N and forbids N N, nu N and L H N. The rows nu and N then share the three nu^c columns, so the number of light massive neutrinos is 3 - rank of the nu^c-N block (checked for ranks 0 to 3). Two measured splittings need rank <= 1. Mirror mixing removes masses and never makes one.
5. Finite diagnostic (mirror-free slab). Read nu^c on Ls layers with Shamir kernel xi_s (chi_(s-1) - q chi_s), q = |1 - M|, and one more chi layer than xi (index 1, no mirror; allowed because nu^c carries no link charge). Then the chi zero mode is exactly proportional to q^(Ls-1-s), on the far layer. A Yukawa-type term on layer 0 gives the Dirac mass y0 v sqrt(1-q^2) q^(Ls-1)/sqrt(1-q^(2Ls)). The SVD agrees to 1e-4 (Ls = 10, q = 1/2).
6. The register's square slab. In the register's layer coordinate each mode has its mirror at the other end. A reversed (far-layer) nu^c therefore puts its mirror xi on layer 0, with charge -1 like nu. The rows (nu, xi) outnumber the columns by one, so one state is exactly massless. The light block is [eps chi0; sigma], with sigma ~ q^Ls/a the slab's own leak. Since eps chi0/sigma ~ y0 v a/q ~ 1e-16, the massless state is the neutrino. The runner's numbers match the two-state prediction: share 0.999996 against 0.999995, and the lightest massive state equals hypot(sigma, eps chi0).
7. Wall height M = 1. This is the height of the smoothed-layer slab (gk-smoothed-layers). There q(p) = sum(1 - cos p_i) vanishes at rest, so the far-layer overlap is exactly 0 at p = 0 and grows as p^(2(Ls-1)) away from it. No neutrino mass results.

B. Estimates against measurement.

1. Spectrum. With NuFIT-6-like inputs, normal ordering at m1 = 0 gives m = (0, 0.0087, 0.0501) eV and Sigma = 0.0588 eV. Inverted ordering gives Sigma_min = 0.099 eV, excluded by Sigma < 0.064. Normal ordering needs m1 < 0.0041 eV. A Majorana route then gives m_bb between 0.0015 and 0.0068 eV, below the ~0.01 eV reach of LEGEND-1000 or nEXO. A Dirac route gives m_ee = 0 exactly.
2. Scales. One-loop SM running gives y_t(M) = 0.414 and a Weinberg-coefficient running factor of 0.755. The scale needed for m3 = 0.0501 eV, with its rung count below M = 2.44e18 GeV, is:

| Route | Scale (GeV) | Rungs below the cell |
|---|---|---|
| type I, y = y_t(M) | 7.8e13 | 14.9 |
| type I, y = 1 | 4.6e14 | 12.4 |
| Weinberg, c = 1 with v = 246 GeV (the brief's 1.2e15 without running) | 9.1e14 | 11.4 |
| type I, y^2 = 4 pi | 5.7e15 | 8.7 |
| NDA, c = 16 pi^2 | 1.4e17 | 4.1 |

The law-fixed scales are the cell 1/L, 1/l_P and the floor 8/L. At these, y = 1 gives m3 <= 9.4e-6 eV and NDA gives m3 <= 3.0e-3 eV, 17x short. Only scales that carry a supplied size get there. The window top at Delta = 1 gives 1.2e-2 eV (NDA). The nested block /24 gives 7.1e-2 eV (NDA). The edge block /b_e at b_e = 40 gives 0.12 eV (NDA). Delta, the block sizes and b_e are only bounded below. Edge blocks are geometry and carry no B - L, so they cannot host the Z4 break (A1) in any case.
3. Look-elsewhere. With a free integer rung 2^-n, the target always lies within x2 for steps <= 4 (P = 0.67 for step 8). A hit at n ~ 11-12 is no evidence unless a law fixes n. No law does.
4. Spontaneous break (b). At M_R ~ 4.6e14 GeV, walls of tension ~M_R^3 dominate at T ~ 2e12 GeV. They exceed the Zel'dovich-Kobzarev-Okun bound sigma^(1/3) < ~1 MeV by 5e17. The route is excluded unless a dilution phase follows the break or a supplied Z4-breaking bias removes the walls. An explicit bilinear nu^c nu^c (the register's other option, U(1)_Y x Z2) has no walls but still needs the supplied scale of B2.
5. Far-layer slab (c), mirror-free. It trades y_nu = 2.88e-13 for (q, Ls). Examples: Ls - 1 = 12.5 at q = 0.1, 20.8 at q = 1/4, 41.5 at q = 1/2, and 127 at q = 0.8 (y0 = 1). For q >= 1/4 some integer Ls always hits within x2, so the match is no evidence. Consequences if adopted:
   - Exponential spacing makes m1 << m2 << m3 natural (normal ordering).
   - Inverted ordering needs two equal Ls with singular values equal to 1.5% (0 of 40000 anarchic draws).
   - The masses are Dirac, so m_ee = 0.
   - Sigma = 0.0588-0.0604 eV (for m1 = 0 to q m2), just under the 0.064 bound and testable.
6. Shared slab. One slab for every species fails. In the free-slab reading the leak q^Ls M pairs each light fermion with its far mirror, so q^Ls M < m_e is required. Together with q^(Ls-1) = y_nu this forces q < 7.3e-10 and Ls = 2, i.e. a wall height tuned to 1 - 3e-13. The nu^c slab must therefore be its own supplied slab.
7. nu^c on the doublet register's rung, N ~ 49-52 (weak-scale, rung-higgs). Every nu-rung contact reading gives a Dirac m3 of at most 1e-10 eV (one-site, 8-site or lapse-owned) or 2e11 eV (domain-normalised). The needed exponent, 41.7/N = 0.80-0.85, matches no reading.

## Candidate law text tested (not adopted)

> "Link-free slab. A mode that carries no link charge is read on every layer of its role block's layer coordinate, with one more layer of its own handedness than of the other, its zero mode at the far layer; its Yukawa-type terms act on the light layer."

Smuggling check. The following are supplied:
- the far orientation (a sign choice; the near orientation gives y_nu = y0, no suppression);
- q, meaning the wall height of nu^c's own slab (B6 rules out sharing the light species' slab, and at the shared height M = 1 the mass is zero by A7);
- Ls and y0.

The "one more layer" is not new content: it is nu^c's existing net chirality, and it carries no anomaly because nu^c is link-free. Gained: the Z4 and Dirac nature are kept, and the 13-decade number becomes an integer. Lost: nothing measured. Verdict: the clause restates y_nu with two supplied numbers (B5), so it is not adopted. Its falsifiable tail (normal ordering, m_ee = 0, Sigma 0.059-0.060 eV, no 0nubb) is shared with any hierarchical Dirac texture.

Majorana variant (register option T2, explicit nu^c nu^c on rung n): it needs n >= 4.1 below the cell at NDA coupling or 12.4 at y = 1 (B2). No law fixes n (B3). Not adopted.

## Relation to existing work

- Register, Neutrino masses item: confirmed and narrowed. The "at most 3e-4 eV" becomes the general cap A3 (any number of heavy states, Dirac seesaw included), with a strong-coupling (NDA) ceiling of 3e-3 eV at the cell.
- Prior neutrino-mass run (agents/neutrino-mass/prev_run_out_0202.txt): its C1, C3 and C4 agree. This run reproduces M_R(y = 1) = 4.6e14 GeV, the running factor 0.76 and y_t(M) = 0.414. A1 to A4 here are new. Its A5 (a nu^c nu^c vacuum breaks Z4) is extended by A2 and B4 (walls).
- nu-rung: its contact readings are used in B7. Its "rung restates the hierarchy" is extended to the doublet's own rung, which misses by 1e8 or more.
- dark-matter-candidate B: consistent (nu^c is Dirac only in a Z4 vacuum).
- gk-smoothed-layers, rung-dimension-chirality: the layer coordinate and the wall height M = 1 are used in A6 and A7. A6 is new: in the square slab a far-layer singlet's mirror captures the partner.
- PR #9925: its Z4 is the input to A1 and A2.
- main, DM_NEUTRINO_ATMOSPHERIC_SCALE_THEOREM_NOTE_2026-04-15 (legacy, unaudited): its M_1 = M_Pl alpha_LM^8 is a staircase exponent on a plaquette coupling. No current register clause fixes that coupling, and the B3 look-elsewhere applies to integer exponents. Not used, not contradicted.

## What a neutrino-mass law must now do (replacement requirements)

1. Majorana route. It must break the Z4 through a lepton-number-2 matter term (A1). It needs a scale fixed by a law at most 1.4e17 GeV even at strong coupling, and 4.6e14 y^2 GeV perturbatively (B2). If the break is spontaneous, it must also supply dilution or a bias (B4).
2. Dirac route. It must give y_nu ~ 3e-13 from a law. A rule must fix the exponent (layer count, rung or overlap). The integer must not be free (B3, B5).
3. Either route must keep at least two massive states: no rank-saturating mirror mixing (A4), and no far-layer singlet in the square slab (A6).
4. Normal ordering with Sigma < 0.064 eV (B1).

Zoom check: a coarser rung moves no Z4 or hypercharge (nu-rung A6), so A1 to A4 hold at every zoom. Zoom enters only through the scale or exponent, which is where a law would have to act.

## Boundary

The A items are exact algebra, plus the stated numerical checks of exact identities. A5 is a finite diagnostic on a supplied free slab. The B items use measured inputs, one-loop running and NDA counting. Nothing here derives y_nu, M_R, the slab parameters or the ordering. Nothing excludes a neutrino-mass law built from new content with a law-fixed scale or exponent.
