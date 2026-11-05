---
claim_id: the_family_copy_form_fixes_koide_q_in_every_sector_and_caps_the_mass_tower_at_one_step_so_the_quarks_exclude_it_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For a candidate family mass law that gives each charged sector's family mass term the form of the update law's copy mass, signed square-root masses = eigenvalues of c (1 - s) with s traceless of unit mean square (the cube hop's normalisation): exactly, Q = (3 + 2 S1 + S2)/(3 + S1)^2 equals 2/3 for every such s, with any eigenvectors (200 seeded random Hermitian s to 1e-12), and the same form on the update's two copies gives Q = 1; the admissible spectra are exactly 1 + sqrt2 cos(delta + 2 pi k/3), one free phase per sector; with only the update's translations and cube-centred inversion, delta is a multiple of pi/3 and two masses are equal; translation-invariant up and down operators share one eigenbasis, so the mixing matrix is a permutation (100 seeded pairs, 1e-13); m2/m3 >= 0.0147 for every phase, = 7 - 4 sqrt3 at m1 = 0, and > 0.035 whenever m1/m2 < 0.1, so no sector holds a two-step tower; a link-dressed family hop of weight kappa <= 1 gives Q = (1 + kappa^2)/3 <= 2/3. Also exact: the flat band's rest phase per tick is the mass angle, so with the dressed-cone clause a mode's rung does not change its mass; on a two-tiling cube tick (6^3 sites, random cube generators) the conjugate family characters stay degenerate unless the cube generator breaks cube-centred inversion and is complex. Estimates against measured masses: the charged-lepton Q and m_tau (1776.969 predicted, 1776.93 +- 0.09 MeV) agree; the lepton phase is no rational multiple of pi with denominator <= 48 (best misses m_e/m_tau by 3.1%); a uniform phase gives a lepton-sized hierarchy in 7.7% of cases; quark Q is 0.85-0.89 (up) and 0.73-0.75 (down), excluding the law by >= 12 sigma; with the signed readout neutrinos would be normally ordered with m1 = 0.36 meV and sum 0.059 eV. Supplied model, finite diagnostic: the law itself, the signed readout, the sector phases, the fixed-angle rung reading, the random cube generators, the measured masses, their running values and uncertainties, the neutrino splittings and the cosmology bound."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_family_copy_form_fixes_koide_q_in_every_sector_and_caps_the_mass_tower_at_one_step_so_the_quarks_exclude_it_2026_10_22.py
---

# The family copy form fixes Koide Q in every sector and caps the mass tower at one step, so the quarks exclude it

Claim type: bounded_theorem.
Primary runner: `scripts/the_family_copy_form_fixes_koide_q_in_every_sector_and_caps_the_mass_tower_at_one_step_so_the_quarks_exclude_it_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight, and none of its laws gives a hierarchical three-family spectrum. Recent no-gos map the wall. Zoom-3 family characters never give three distinct spurion distances. No zoom or point group gives an ordered charge with three light families. Cube-centred inversion ties families 1 and 2. Registers carry no family charge. An exact family charge forces zero mixing. This note tries the other direction: a law-level form for the family mass term, built from forms the update law already uses, tested against the measured masses. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here. The law gives the measured charged-lepton Koide value, but it gives the same value in every sector, and it allows only one step of hierarchy. The quarks exclude it. Every check passes. Several PASS lines record that the law fails against measurement.

## Candidate law (verbatim)

> "Family copy form. A charged sector's mass term on its three families has the form of the copy mass: the signed square roots of its masses are the eigenvalues of c(1 - s), where c is the sector's scale and s is a family-space operator built as the cube's hop is built, a sum of unitary family hops whose weights have squares summing to one, so that s is traceless with unit mean square."

Smuggling check. The text uses no measured number. The value 2/3 is not written into it. The equal weight of the identity and s is taken from the update law's copy-mass factor (1 - s), and the unit normalisation from its hop rule (R = sum of w_i W_i, with the w_i^2 summing to 1). Giving the family mass term this form is the law's own content, and that choice is the isotypic-weight choice. Main's Koide audits found that choice not forced (Gate 1 of `CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md`). The law moves the choice to a reuse of a form the register already has; it does not derive it. Two further choices sit outside the text: the signed readout (square roots may be negative), and the phase of s in each sector.

## Statement

A. The three suggested routes.

1. Rung span (exact). On flat edges CL-1's band is cos w = A S - (cos 2b - cos mu)/2, with A = (cos 2b + cos mu)/2. At K = 0, S = 1, so w = mu: the rest phase per tick equals the mass angle. The dressed-cone clause sets mu = m N per tick, so the proper rest energy is m on every rung. How many rungs a family's modes span does not change its mass. The reading that would suppress masses, a fixed angle per tick with masses 2^-n at rung n, needs supplied integers. The closest integer pair for leptons, (4, 13), gives Q = 0.6682 and m_e/m_tau = 1.2e-4 against 2.9e-4. This agrees with `generation-rungs`, item 3.
2. Record or actuality selection (structural). CL-2 moves the actual configuration by a transport that keeps its Born odds. The register states that records never condition the odds, because the only change the odds undergo is the joint update. Masses are quasi-energies of that update. No fewest-changes or entropy selection can split a mass unless actuality is allowed to condition the odds, and that breaks the Born distribution, as definite links did.
3. Polar nesting (exact, finite). On a two-tiling cube tick on 6^3 sites with random cube generators, the conjugate family characters (1,1,1) and (2,2,2) have identical spectra in two cases: when the generator keeps cube-centred inversion (even if complex), and when it is real (even with a polar C3v term). Only a generator that is both polar and complex splits them, by 1.16 rad here. This is the register's "axial vector plus time-reversal breaker". The split's nesting is real geometry, so it is time-reversal even. In a uniformly split bulk it is a pure translation, and every cube operation survives (register). It cannot split the pair in the bulk, and at split fronts its weight is about t_tick H, roughly 1e-61.

B. The family copy form (exact).

4. With sqrt(m) = 1 + x, Q = (3 + 2 S1 + S2)/(3 + S1)^2, where S1 = sum x and S2 = sum x^2. Traceless (S1 = 0) with unit mean square (S2 = 3) gives Q = 2/3 for every s and any eigenvectors. On the update's two copies the same form, 1 - s with s^2 = 1, gives roots 0 and 2, Q_2 = 1 and one massless copy, which is what the copy mass does.
5. The admissible spectra are exactly x_k = sqrt2 cos(delta + 2 pi k/3), so each sector has one free phase (Brannen's parametrisation at r = 1/2).
6. With only CL-1 to CL-3, s is diagonal in the zoom-3 translation characters, and cube-centred inversion sets x1 = x2. Then delta is a multiple of pi/3, and sqrt(m) is proportional to (1 + sqrt2, 1 - 1/sqrt2, 1 - 1/sqrt2) or the signed pi/3 pattern. There are only two distinct masses.
7. Translation-invariant s_u and s_d share the character eigenbasis, so |V| is a permutation for every pair of phases. This agrees with the family-flux and family-parity results.
8. One-step cap. For every phase, m2/m3 >= ((1 - 1/sqrt2)/(1 + sqrt2))^2 = 0.0147, with the bound reached at the degenerate point. At m1 = 0, m2/m3 = (2 - sqrt3)^2 = 0.0718. Whenever m1/m2 < 0.1, m2/m3 > 0.0357. So the form gives one step of hierarchy, never two. Koide's Q = 2/3 is the statement that a sector's tower is this one-step tower.
9. Dressing sign. If the family hop is dressed by link registers with domain-normalised raisers (norm at most 1), its weight kappa is at most 1. Then Q = (1 + kappa^2)/3 <= 2/3, so dressing can only lower Q.

## Estimates against measurement

- Charged leptons. With the measured masses Q = 0.6666645, and the form predicts m_tau = 1776.969 MeV from m_e and m_mu (measured 1776.93 +- 0.09). The fitted phase is 0.222239, which is 2/9 to within 2e-5 (main's Gate 2, not derived here). The best pi p/q with q <= 48 is pi 66/47, which misses m_e/m_tau by 3.1%. With 1424 such fractions, 95% of random targets are matched at least as well, so a lattice phase would not have been evidence even had one fit.
- Hierarchy is tuned. A phase uniform on (0, pi/3) gives m1/m3 at or below m_e/m_tau in 7.7% of cases.
- Quarks exclude the law. Q_u = 0.849 (PDG reference masses) and 0.888 (approximate running values at M_Z); Q_d = 0.731 and 0.748. The signed readout gives 0.82 to 0.90. The smallest pull from 2/3 is 12 sigma. Both quark sectors need kappa^2 = 3Q - 1 > 1 (1.55 to 1.66 up, 1.19 to 1.24 down), which item 9 forbids. Both also break the one-step cap: up has 1.7e-3 and 7.4e-3, down has 0.05 and 0.022. The second is below 0.0357 in both, and m_c/m_t is below the absolute floor 0.0147. This sharpens main's `FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND_CANNOT_DERIVE_THE_KOIDE_DIAL_NARROW_NO_GO_NOTE_2026-06-15.md`: any sector-blind form with this weight fails. The cap and the sign of the dressing say the failure is structural.
- Neutrinos, if the form were universal. No all-positive solution exists. With one negative root there is a normal-ordering solution, m1 = 0.364 meV and sum 0.0592 eV, inside the DESI DR2 plus CMB bound of 0.064 eV. The inverted solution has sum 0.102 eV and is excluded. This signed-root solution is known in the literature (Brannen). The sum sits 3e-4 eV above the normal-ordering minimum, beyond any planned sensitivity.
- Parameter count. Three scales and three phases for the 9 charged masses, and the phases are not in CL-1 to CL-3. That leaves three predicted Q values: leptons pass, up and down fail. The form predicts no mixing; mixing needs a supplied translation breaker and its four parameters. The Standard Model uses 9 + 4.

## The four criteria

(i) Three distinct masses: only with a phase that breaks inversion and time reversal in the family sector. CL-1 to CL-3 contain none in the bulk (items 3 and 6). (ii) Ordered hierarchy: one step at most (item 8), tuned at the 8% level for lepton size. (iii) Mixing: zero with the update's translations (item 7). (iv) Koide: exact by form for leptons, but in every sector, which the quarks exclude.

## What measured reality asks for instead

Two things, read off the failures. First, quark sectors are hop-dominated: their family-changing weight exceeds the diagonal weight (kappa^2 about 1.2 to 1.7), and no link dressing raises a weight. Second, the up and down towers need two hierarchy steps, so the family mass term must contain at least two distinct hop distances. That is the same three-distance requirement `family-charge-search` derived for spurion charges, here met from the mass-form side. A sector-dependent law with at least two hop ranges and a bulk inversion-and-time-reversal-odd family term would meet both. No structure in CL-1 to CL-3 supplies one yet.

## Boundary

This note does not derive Koide's Q, the Brannen phase, or any quark mass. It does not test non-Hermitian family terms, or forms with more than one hop range. The running quark masses at M_Z are approximate literature values used only to show that the scale doesn't matter. The neutrino statement applies only if the form were extended to neutrinos, which the register's separate-channel requirement does not imply.

## Supplied vs forced

Forced (exact, given the form): Q = 2/3 in every sector, one phase per sector, the degenerate pair without an inversion-and-time-reversal breaker, permutation mixing under translations, the one-step cap and the dressing sign. Supplied: the form itself (the isotypic weight), the signed readout, the phases, the scales, and every measured input. Not used: any measured number inside the law text.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Candidate-law register](CANDIDATE_LAWS.md)
- Context only: `CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md`, `FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND_CANNOT_DERIVE_THE_KOIDE_DIAL_NARROW_NO_GO_NOTE_2026-06-15.md`, and the open family PRs (#9883, #9922, #9954, #9958).

## How to run

```
python3 scripts/the_family_copy_form_fixes_koide_q_in_every_sector_and_caps_the_mass_tower_at_one_step_so_the_quarks_exclude_it_2026_10_22.py
```

Seeded (20261022), runtime about 1 s, peak memory about 120 MB, AUDIT_TIMEOUT_SEC = 120. Expected: TOTAL: PASS=15 FAIL=0.
