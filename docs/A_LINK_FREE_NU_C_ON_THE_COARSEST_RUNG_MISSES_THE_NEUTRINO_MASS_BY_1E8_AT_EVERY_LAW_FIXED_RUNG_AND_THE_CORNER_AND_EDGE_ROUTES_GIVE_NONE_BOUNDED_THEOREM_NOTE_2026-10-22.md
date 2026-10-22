---
claim_id: a_link_free_nu_c_on_the_coarsest_rung_misses_the_neutrino_mass_by_1e8_at_every_law_fixed_rung_and_the_corner_and_edge_routes_give_none_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Three candidate Dirac-neutrino mass rules under the register (nu^c Dirac by the Z4 of B - L). (a) nu^c, the only link-free mode, read on the coarsest rung available: exactly, nested block-uniform readings overlap by 2^(-3|a-b|/2) (to 2e-16), and a coarse nu^c's k = 0 Dirac coupling is 2^(-3n/2), 2^(+3n/2) or 1 for the one-contact, every-site and domain-normalised readings, so the suppression is a reading choice; with y0 = 1 the needed rung is n = 27.8 (one contact), 29.8 (covariant 8 sites) or 16.7 (coarse update owns the term), i.e. b_e = 2.3e8, 9.2e8 or 1.0e5; every law-available coarsest rung misses: b_e at its site-budget floor 32-45, the floor-to-split ratio 16 and the window top at Delta = 1 give m3 = 1e7-2e10 eV, the horizon (n = 200, measured H0) gives < 1e-78 eV; fitting b_e or Delta (bounded only below) is allowed and FITTED; with one rung for all three nu^c an O(1) matrix gives r within x1.5 in 0.8% and Sigma < 0.064 eV in 0.1% (conditional median Sigma 0.073 eV). (b) A light-mirror pairing mu acts as a Dirac seesaw, m_light m_heavy = y v mu exactly; a corner-only mu = lam f(K), f(0) = 0, gives exactly zero rest mass by crystal-momentum conservation, a cell-local mu gives no suppression, and the needed mu/Delta = 2.9e-13 is supplied. (c) Edge registers carry no Y or B - L and conserve nu^c number: with y_nu = 0 they never mix nu and nu^c, and with y_nu != 0 their flavour-blind dressing multiplies every Yukawa alike. All three rules FAIL the anti-smuggling gate; the parameter-free readings are EXCLUDED."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - every_majorana_route_needs_a_supplied_scale_four_rungs_below_the_cell_and_a_far_layer_nu_c_leaves_the_neutrino_massless_bounded_theorem_note_2026-10-22
  - the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_bounded_theorem_note_2026-10-22
runner: scripts/a_link_free_nu_c_on_the_coarsest_rung_misses_the_neutrino_mass_by_1e8_at_every_law_fixed_rung_and_the_corner_and_edge_routes_give_none_2026_10_22.py
---

# A link-free nu^c on the coarsest rung misses the neutrino mass by 1e8 at every law-fixed rung, and the corner and edge routes give none

Claim type: bounded_theorem.
Primary runner: `scripts/a_link_free_nu_c_on_the_coarsest_rung_misses_the_neutrino_mass_by_1e8_at_every_law_fixed_rung_and_the_corner_and_edge_routes_give_none_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. It makes nu^c the Dirac partner of nu (the Z4 of B - L forbids nu^c nu^c and L L H H) and supplies y_nu ~ 3e-13. Seesaws at law-fixed scales cap m3 at ~3e-3 eV (neutrino-mass). Measured: sqrt(dm^2_31) = 0.050 eV, sqrt(dm^2_21) = 0.0087 eV, Sigma < 0.064 eV. This note tests three rules meant to give m3 without a fit. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

Repo check: origin/main has legacy (2026-04) Dirac-neutrino notes (NEUTRINO_MASS_REDUCTION_TO_DIRAC_NOTE, NEUTRINO_DIRAC_Z3_SUPPORT_TRICHOTOMY_NOTE, NEUTRINO_LANE4_DIRAC_SEESAW_FORK_NO_GO_NOTE_2026-04-27). None uses the current register's link-free nu^c, edge block or window. Open PR #9981 (neutrino-mass) and PR #9877 (the link-free slot) are the inputs used here. No open PR reads nu^c on the edge block.

## Candidate rules tested (not adopted)

> (a) "Coarsest reading. A mode that carries no link charge is read only as the block-uniform mode of the coarsest rung available to it, and each of its contact terms joins one fine site per coarse site."

> (b) "Corner Dirac. nu^c's Dirac mass is the light-mirror pairing at the zone corner, passed to the light copy through the mirror's gap."

> (c) "Edge Dirac. nu^c's Dirac mass is mediated by the edge registers."

## Statement

A. Exact.

1. Overlap. Nested block-uniform readings on rungs a and b overlap by 2^(-3|a-b|/2). This is checked on 16^3 for rungs 0-4, to 2e-16.
2. Reading dependence. A coarse nu^c on rung n couples to the fine k = 0 mode with weight:
   - 2^(-3n/2) when each coarse site has one contact;
   - 2^(+3n/2) when every fine site is a contact with weight 1;
   - 1 when the contacts are domain-normalised.
   So the suppression comes from the contact reading, not from the overlap theorem alone. The one contact spreads its weight evenly over the 2^(3n) folded fine momenta, with shares summing to 1. Only 2^(-3n) of it reaches the light band, and the rest pairs with heavy fine bands. The exact torus spectra of nu-rung A2 confirm this.
3. Mirror seesaw (b). Take rows (nu, N) and columns (nu^c, N^c), with mass matrix [[0, y v], [mu, Delta]]. Then m_light m_heavy = y v mu exactly (200 random cases, 2e-13). For three families the light masses are the singular values of Y mu/Delta (2e-7 at Delta = 1e4).
4. Corner-only pairing. Suppose mu(K) = lam f(K) with f(0) = 0 and f(R) = 1. The update conserves crystal momentum, so the K = 0 Dirac mass is exactly 0 and grows as k^2. There is no rest mass. This is the momentum form of the light-partner-gap result that a corner term which spares K = 0 cannot reach it. A symmetric (SMG) mirror has no bilinear pole at K = 0 to mix through at all.
5. Edge routes (c). Edge registers carry no Y and no B - L, and their terms are flavour-blind.
   - With y_nu = 0 the edge-coupled evolution never mixes nu and nu^c. In a 128-dimensional toy the leak is exactly 0.
   - With y_nu != 0 the induced coupling is y_nu <F>, with F the universal dressing. It multiplies every Yukawa alike.
   - CL-3 measures from the vacuum, so F departs from 1 only by the local departure, (H0 L)^2 = 3.5e-121 today.

B. Estimates against measurement.

1. Needed Yukawa: y3 = sqrt2 m3/v = 2.88e-13 = 2^-41.66 (normal ordering, m1 -> 0).
2. Needed rung at y0 = 1:

| Reading | Needed n | Needed b_e = 2^n |
|---|---|---|
| one contact (p = 3/2) | 27.8 | 2.3e8 |
| covariant 8 sites (2^(3 - 3n/2)) | 29.8 | 9.2e8 |
| coarse update owns the term (p = 5/2) | 16.7 | 1.0e5 |

3. Law-available rungs, m3 at y0 = 1 for the three readings:

| Rung | m3 (eV) | Verdict |
|---|---|---|
| b_e = 32-45 (site-budget floor, register-size-s) | 1.3e7 - 7.7e9 | excluded by KATRIN (0.45 eV) and Sigma |
| floor-to-split 16 (n = 4) | 1.7e8 - 2.2e10 | excluded |
| window top 4 + Delta at Delta = 1 (n = 5) | 3.0e7 - 7.7e9 | excluded |
| horizon c/H0 over L (n = 200.1, measured H0) | 5e-140 - 6e-79 | excluded (two splittings) |

   The closest miss is 10^8.4. No reading gives the needed exponent per horizon octave, 41.66/200 = 0.21.
4. Fitting. b_e and Delta are bounded only below, so b_e = 1e5-1e9 or Delta = 12.7-25.8 is allowed. But it is FITTED, because the value is chosen to hit m3. The consequences are untestable:
   - the gravity block scale 1/(b_e L) is 2.7e9-2.4e13 GeV;
   - the pinning bound s >= 26.3 b_e (edge-block D1) becomes s >= 3e6-2e10.
5. Look-elsewhere. With an integer rung the target lies within x2 with P = 1 (p = 3/2) or 0.80 (p = 5/2), and b_e is continuous anyway.
6. One coarsest rung for all three nu^c (rule (a) as written). Rule (a) puts all three on the same rung, so the masses are one scale times the singular values of an O(1) matrix (200000 complex-Gaussian draws). This is the rule's unfitted prediction, and it is disfavoured:
   - r = dm21/dm31 falls within x1.5 of 0.030 in 0.81% of draws (normal ordering), against 0.003% for an inverted-type assignment;
   - adding Sigma < 0.064 eV leaves 0.10%, so P(Sigma ok | r ok) = 12%;
   - the conditional median Sigma is 0.073 eV, above the bound, with m1 = 0.009 eV.
7. Mirror route (b). The needed mu/Delta is 2.9e-13.
   - A cell-local mu with the cell-scale mirror gap (one-gap-scale B6) gives O(1).
   - A singlet mu cannot carry v (hypercharge).
   - mu ~ v^2/M gives 1.8e-5 eV, 2800x short.
   - A corner-only mu gives 0 at rest (A4).
8. Any Dirac route gives m_ee = 0 exactly. At m1 = 0, normal ordering gives m = (0, 0.0087, 0.0501) eV, Sigma = 0.0588 eV and m_beta = 0.0088 eV.

## Anti-smuggling gate (owner 2026-10-22)

(a) Coarsest reading: FAIL.
1. Number chosen: the rung (b_e, Delta or n) is FITTED to m3, and the contact reading (p and which sites) is also supplied (A2). The parameter-free choices, the budget-floor b_e, the window top, the floor-to-split ratio and the horizon, are EXCLUDED by 10^8.4 or more (B3).
2. Structure inserted: none by name. "Link-free" is a register property, not observed content.
3. Unfitted prediction: the one-rung anarchy of B6, at 0.10%, is disfavoured.
4. Axiom bent: Lattice ("no site privileged") through the one-contact-per-coarse-site reading (A3 of nu-rung: a b = 2^n block has no centre site). It would need an AX-n entry.

(b) Corner Dirac: FAIL. mu/Delta is supplied. The corner-only form gives no rest mass (exact), so the measured splittings exclude it as the source. Axiom bent: none.

(c) Edge Dirac: FAIL. It is exactly blind to nu^c number (A5) and gives no neutrino-specific suppression. Axiom bent: none. No rule is adopted.

## What survives, and what a replacement must do

These items are fit-free and reusable:
- the overlap theorem;
- the reading dependence: suppression needs one contact per coarse site;
- the exact mirror-seesaw identity;
- the zero rest mass of any corner-only pairing;
- the edge selection rule.

A replacement must fix a rung exponent of 16.7-29.8, or a scale ratio of 2.9e-13 between nu^c's pairing and its gap, from a law that is not tuned on neutrino data. One example is a law that fixes b_e from the gravity sector (b_e = 1e5 under the p = 5/2 reading). It must also give the three nu^c distinct rungs, or else accept the B6 tension. The neutrino-mass requirements still hold: Z4, normal ordering, Sigma < 0.064 eV and no rank-saturating mixing.

## Relation to existing work

- nu-rung: A2 reproduces its reading dependence, and B2 its needed n. New here: the law-available rungs, b_e, the window and the horizon (B3), and the one-rung anarchy test (B6).
- neutrino-mass (PR #9981): its cap and requirements are used. This note adds that the Dirac route also fails at every law-fixed rung.
- light-partner-gap: A4 is the momentum-conservation form of its "corner term cannot reach K = 0" result. It gives no rest mass.
- register-size-s and edge-block: these give b_e >= 32-45 with no upper bound and s >= 26.3 b_e.
- flavour-rule: its overlap theorem is A1. Its look-elsewhere lesson (eps not tested) carries over.

## Boundary

Free-band and toy statements only. Not computed: an interacting SMG mirror's Green's-function zeros near K = 0, non-perturbative gravity (topology change, splits) breaking nu^c number, and a gravity-sector law for b_e. The toy edge dressing is random, not CL-1's edge tick. The anarchy measure is complex Gaussian.

## Supplied vs forced

Forced: A1-A5, given the stated readings.
Supplied:
- the contact readings (p, which sites, which update), y0 = 1, the rungs, mu, Delta and the form factor f;
- the measured inputs: splittings (NuFIT-6-like), Sigma bound (DESI DR2 + CMB), v = 246.22 GeV, H0 = 67.4 km/s/Mpc, hbar c/L = 2.44e18 GeV, mixing |U_e2|^2, |U_e3|^2 for m_beta.

## How to run

```
python3 scripts/a_link_free_nu_c_on_the_coarsest_rung_misses_the_neutrino_mass_by_1e8_at_every_law_fixed_rung_and_the_corner_and_edge_routes_give_none_2026_10_22.py
```

Seeded (20261022), about 0.7 s, peak memory about 110 MB, AUDIT_TIMEOUT_SEC = 60, output 4.1 kB. Expected: TOTAL: PASS=11 FAIL=0.
