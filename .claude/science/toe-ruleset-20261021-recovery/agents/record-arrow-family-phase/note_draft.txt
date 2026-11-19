---
claim_id: the_record_arrow_the_tick_order_and_the_role_blocks_each_keep_an_inversion_or_a_mirror_time_reversal_so_no_family_term_is_odd_under_both_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's two-tiling cube tick as modelled here (one fermion mode per site, cube hop R a sum of three anticommuting real axis hops with R^2 = 1, copy sign s = i W1 W2 W3 R, the copy mass on even cubes before and after the half-tick, a gauge that puts the rest point at the zone centre, 6^3 sites, families the characters k_j = (2 pi/3) j (1,1,1) of the tick translations): exactly, up and down family terms sharing an inversion have a common eigenvector, so |V| has an entry 1, and terms sharing an antiunitary give J = 0 (200 seeded pairs each); the copy-massed tick commutes with the cube-centred inversion I = (-1)^y P(x -> 1 - x), and the antiunitary A = (-1)^(xy) sigma_d K maps its symmetric-frame tick to its inverse; a C3v polar term (the stand-in for the split's polarity) breaks I and keeps A, so the conjugate family pair stays degenerate (to 1e-15) with the copy mass, the polar term on one or both tilings and either half-tick order; U_odd U_even and U_even U_odd are similar, and the even-first generator's imaginary part (0.155 at the zone centre) is a frame effect absent in the symmetric frame; a T-odd polar current, the control, splits the pair at 3.29 rad per tick per unit weight. Under CL-2 the actual configuration and its growing record stack never enter the odds, so the arrow adds no family term at any order. Counterfactually, if records conditioned the odds (dephasing p per record set), I keeps the family pair's return curves equal in every cadence; with I broken and records once per half-tick, as CL-2 takes them, they stay equal to 2e-15 (finite diagnostic, 3 parameter sets, 60 ticks; reason not derived); a once-per-tick cadence gives a first-order dissipative asymmetry of 1.05e-3 p at polar weight 0.3. Blocks of whole even cubes have centres and corners at cube centres, every inversion-symmetric odd-period pattern (P = 3, 5, 7) has a cube-centred inversion centre, and nested blocks share one; covariant role layouts of period 3 sites and 6 sites both hop between families (norms 0.01-0.02 and 0.16-0.18), and the tick with both keeps I and A. Estimates: the needed inversion- and time-odd family weight is of order 1; split fronts give about 1e-61 per tick, and conditioning records would be bounded by matter-wave coherence to p < 5e-44. Supplied model, finite diagnostic: the real gauge and the rest-point gauge, the polar stand-in and its weights, the control current, the role tables and potentials, the step and mass angles, the dephasing model of conditioning records and its cadences, the 1 s coherence time, and the measured mixing values."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_record_arrow_the_tick_order_and_the_role_blocks_each_keep_an_inversion_or_a_mirror_time_reversal_so_no_family_term_is_odd_under_both_2026_10_22.py
---

# The record arrow, the tick's order and the role blocks each keep an inversion or a mirror time reversal, so no family term is odd under both

Claim type: bounded_theorem.
Primary runner: `scripts/the_record_arrow_the_tick_order_and_the_role_blocks_each_keep_an_inversion_or_a_mirror_time_reversal_so_no_family_term_is_odd_under_both_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Two of today's results map the family wall: the family copy form allows one hierarchy step, and the quarks exclude it (`mass-tower-law`); inversion-closed zoom charges give at most two spurion distances (`family-charge-search`). Both point to the same need. A family term must break cube-centred inversion and time reversal in the bulk. This note asks whether a structure already in the laws supplies one. It tests three candidates:

- the record arrow, the one built-in time asymmetry;
- the polar split together with the tick's even-odd order;
- the role-block sizes b, B_f and b_e as hop ranges.

None supplies it. Each candidate keeps either the cube-centred inversion I or the antiunitary A = sigma_d K, a diagonal mirror composed with time reversal. Either one ties the conjugate families. Every check passes. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Why both oddities are needed (exact).

1. Write the three families in the character basis, and let P swap the conjugate pair. If the up and down family terms commute with P, they share the eigenvector (0, 1, -1)/sqrt 2, so |V| has an entry equal to 1. If they commute with the antiunitary P K, then J = 0. The runner checks 200 seeded pairs of each kind. Measurement has no unit entry (|V_ub| = 0.0037, |V_cb| = 0.042) and J = 3.1e-5. So in both sectors the family term must break the inversion and every antiunitary that maps k to -k. With translations broken, three distinct masses alone do not need a time-odd term, but the mixing does.

B. The tick's order and the polar split (exact on the model).

2. Model tick. The cube hop is R = (W1 + W2 + W3)/sqrt 3, with anticommuting real axis hops (every face phase -1, R^2 = 1). The copy sign is s = i W1 W2 W3 R: Hermitian, s^2 = 1, [s, R] = 0, and purely imaginary, so it is odd under K. The copy mass exp(i (M/4)(1 - s) R) acts on even cubes before and after the half-tick. The odd cubes use a gauge that puts the rest point at the zone centre. There the rest phase is the mass angle, and with the copy mass the second copy sits at mu + M. The Bloch form matches the 216-site real-space tick.
3. Symmetries. I = (-1)^y P(x -> 1 - x) commutes with both half-ticks. A = (-1)^(xy) sigma_d K maps the symmetric-frame tick to its inverse. This is the register's "via the copy mass, K sigma_d". A C3v polar term, odd under I and real, stands in for the split's polarity. It breaks I and keeps A.
4. Order is a frame. U_odd U_even = U_even^-1 (U_even U_odd) U_even, so the two orders have the same quasi-energies (2e-15). Without the copy mass, the even-first Floquet generator has an imaginary part (0.155 at the zone centre). The symmetric-frame generator is real (1e-15), and the spectra agree. The chiral "screw" composition looks time-odd only in the even-first frame. The frame unitary removes it, so it never splits a conjugate pair.
5. The conjugate pair (1,1,1)/(2,2,2) stays degenerate (at most 8e-16) in every case tested: the copy mass alone; with the polar term on even cubes, or on both tilings; in either half-tick order; and without the copy mass. A survives all of them.
6. Control. A T-odd polar current along (1,1,1) breaks I, K and A. It splits the pair at first order, at 3.29 rad per tick per unit weight, so the test is sensitive.

C. The record arrow.

7. CL-2 (exact). The actual configuration moves by a coupling of successive Born odds. The runner checks the fewest-changes coupling exactly over 12 ticks, and the record stack only grows. The register says records never condition the odds, because the joint update is the odds' only change. The masses are quasi-energies of that update, so the arrow adds no family term at any order or weight. This narrows the earlier route no-go `ARROW_CPT_ORIENTATION_DO_NOT_SOURCE_CP_ODD_ACTION_COEFFICIENTS_NO_GO_NOTE_2026-06-08.md` (record formation gives an arrow only through boundary data) to the current register's family sector.
8. Counterfactual: records that do condition the odds, modelled as dephasing p per record set on matter sites.
   - With I kept, the return curves of the family pair are equal in every cadence (2e-15), because I is a site map with signs and commutes with the dephasing (exact).
   - With I broken by the polar term, and one record set per half-tick as CL-2 takes them, the curves still agree to 2e-15 over 60 ticks for three parameter sets. This is a finite diagnostic, and the reason is not derived.
   - A once-per-tick cadence, which is not CL-2's, gives a first-order asymmetry: 1.05e-3 p at polar weight 0.3, linear in p. This asymmetry sits in a decay rate, not in a quasi-energy. A maps the forward channel to the time-reversed one with the dephasing undone, which is not the same channel. This is how the arrow shows up as dissipation rather than as a mass.

D. Role blocks (exact lemma, finite check).

9. A block of B whole even cubes spans sites 2nB to 2nB + 2B - 1, so its centre and its corners sit at half-integer points, which are cube centres (checked for B = 1..40). Nested blocks share such a centre. An odd-period pattern symmetric about c is also symmetric about c + P/2, so it has a half-integer centre (all 3^P patterns for P = 3, 5, 7). Every covariant layout built from these blocks therefore keeps a cube-centred inversion of the whole tick.
10. Ranges exist, but they are even. O_h-covariant role layouts of period 3 sites (b = 3) and 6 sites (a block of three even cubes) both hop between families. The norms are 0.01-0.02 and 0.16-0.18, so two ranges are present. Additive layouts f(x) + f(y) + f(z) have no first-order family hop. Even with both layouts present, the tick keeps I (2e-16) and A (2e-14). By item 1, every such layout gives a unit mixing entry and J = 0. Edge registers enter only through their vacuum fluctuations on flat cells, because the flat metric is uniform. Link and edge vacua are real in their electric and length bases, so they keep A. This part is stated, not run.

## Estimates against measurement

- The needed weight is of order 1. The CKM J = 3.1e-5 comes with sines 0.22, 0.04 and 0.004, and the charged-lepton circulant phase sits 2/9 rad off the inversion values.
- Available in the bulk: exactly zero (items 4-10).
- At split fronts the polarity's weight is about t_tick H, or 1e-61 per tick (register).
- Conditioning records, if the law allowed them, would be bounded by matter-wave coherence. A coherence time of about 1 s gives p < t_P / 1 s = 5e-44 per tick. Combined with the front weight, the product is below 1e-104.
- No term exists, so the note predicts no mass ratio or mixing.

## What measured reality asks for instead

The family term must break, in the bulk and in both quark sectors, both I and A (equivalently every antiunitary taking k to -k). The tick, its order, the split's polarity, the records and every covariant whole-cube role layout keep at least one of them. A replacement rule needs a bulk structure that is polar and odd under sigma_d K, such as a time-odd current along the family axis (the control here), or a sigma_d-odd and time-even chiral texture together with a polar one. None of these is in CL-1 to CL-3.

## Boundary

Not claimed:
- the register's spin-3/2 overlap phases (a real gauge and a rest-point gauge are supplied; the spectra used are gauge invariant, but mixed even-odd loop fluxes follow the supplied gauge);
- the split's own geometry (a C3v polar term stands in for it);
- link or edge registers as quantum dynamics;
- non-covariant role layouts, or blocks not made of whole even cubes (a period-6 pattern centred on a site has no cube-centred inversion);
- a proof of the half-tick-cadence equality in item 8;
- interacting family terms;
- any family mass or mixing value.

## Supplied vs forced

Forced, given the model: item 1; the similarity of the two orders, and the frame origin of the even-first imaginary part; I and A on the copy-massed tick; that the polar term keeps A; the degeneracy of the conjugate pair; that CL-2's records never enter the quasi-energies; that I commutes with any site dephasing; the half-integer-centre lemma.

Supplied: the real hop gauge and the rest-point gauge, the polar stand-in and its weights, the control current, eps = 0.5, mu = 0.2, M = 0.6 (with two other sets), the role tables (seeded) and the potential strengths, the dephasing model and its cadences, the 1 s coherence time, and the measured mixing values.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Candidate-law register](CANDIDATE_LAWS.md): CL-1 tick, copy mass, split polarity, role blocks; CL-2 records never condition the odds.
- Context: `ARROW_CPT_ORIENTATION_DO_NOT_SOURCE_CP_ODD_ACTION_COEFFICIENTS_NO_GO_NOTE_2026-06-08.md` (main; narrowed here); open PRs #9873 (records never condition the odds), #9930 (no Zeno effect), #9922 (family-diagonal mixing under translations); today's `mass-tower-law` and `family-charge-search` drafts.

## How to run

```
python3 scripts/the_record_arrow_the_tick_order_and_the_role_blocks_each_keep_an_inversion_or_a_mirror_time_reversal_so_no_family_term_is_odd_under_both_2026_10_22.py
```

Seeded (20261022), runtime about 1 s, peak memory about 80 MB, AUDIT_TIMEOUT_SEC = 120, output about 4.2 kB. Expected: TOTAL: PASS=15 FAIL=0.
