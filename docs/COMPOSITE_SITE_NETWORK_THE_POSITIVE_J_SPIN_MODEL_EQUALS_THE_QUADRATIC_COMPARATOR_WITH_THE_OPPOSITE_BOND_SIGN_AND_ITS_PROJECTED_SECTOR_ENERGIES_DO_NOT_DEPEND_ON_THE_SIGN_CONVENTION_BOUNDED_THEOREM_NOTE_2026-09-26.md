---
claim_id: composite_site_network_the_positive_j_spin_model_equals_the_quadratic_comparator_with_the_opposite_bond_sign_and_its_projected_sector_energies_do_not_depend_on_the_sign_convention_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Supplied spin model of the landed composite-site network notes (bonds J_l (tau^l tau^l)(sigma . sigma), odd paths kappa tau_q1^l tau_p^nu tau_q2^m (sigma_q1 . sigma_q2) for cyclic (l, m, nu)) and the supplied quadratic Majorana comparator with the six-Majorana representation and constraints D_i = 1. Exact local operator identities, checked as matrices on the constrained Clifford spaces of two and three sites: sigma^a tau^l = +i b^l c^a; the positive-J spin bond equals the comparator bond with hopping -2J u_ij (the opposite of the comparator's convention); each odd path equals the comparator's odd hop with hopping -2 kappa u u, for every colour pair and either sublattice of the middle site. Exact spectral statements: a sublattice sign flip of the c Majoranas and the reversal A -> -A change the ground parity by (-1)^(N/2), so on every admissible torus (N = 8abc) the four sign conventions give the same projected sector energies (checked on random sectors of the 32-, 64- and 128-site tori). So the landed notes' projected sector energies are those of the positive-J spin model on the same tori, while band-flux signs refer to the comparator's odd-term sign. No phase, thermodynamic statement or physical identification."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_sites_give_the_carved_majoranas_an_exact_charge_one_qubit_per_site_cannot_two_can_bounded_theorem_note_2026-09-24
  - composite_site_network_spin_model_ground_state_is_locally_flux_free_on_the_clusters_searched_with_the_projection_exact_bounded_theorem_note_2026-09-25
runner: scripts/composite_site_network_spin_model_to_comparator_operator_identities_and_sign_conventions_2026_09_26.py
---

# The composite-site network: the positive-J spin model equals the quadratic comparator with the opposite bond sign, and its projected sector energies do not depend on the sign convention

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** exact local operator identities and exact spectral relations, checked numerically; unaudited.

## Why

The landed flux-sector note
`COMPOSITE_SITE_NETWORK_SPIN_MODEL_GROUND_STATE_IS_LOCALLY_FLUX_FREE_ON_THE_CLUSTERS_SEARCHED_WITH_THE_PROJECTION_EXACT_BOUNDED_THEOREM_NOTE_2026-09-25.md`
records, from its review, that equality between the positive-J spin model
and the quadratic Majorana comparator is not established in the
comparator's sign convention. With the usual bilinear representation, the
positive-J spin bond corresponds to the opposite hopping sign. Spectra alone
do not settle this, because the comparator's spectra are even in the
hopping signs. This block settles it with operator identities, and shows
which comparator statements carry over.

## Result

- **The local algebra.** On the constrained Clifford space of one site
  (`D = −i bˣ bʸ bᶻ cˣ cʸ cᶻ = 1`, dimension four), `σᵃ = −(i/2) ε^{abc} cᵇ cᶜ` and
  `τˡ = −(i/2) ε^{lmn} bᵐ bⁿ` obey the two-qubit Pauli algebra and
  `σᵃ τˡ = +i bˡ cᵃ`. These are checked as matrices on the constrained space
  of three sites (rank 64 of 512).
- **The bond.** For each flavour `l`, the positive-J spin bond
  `J (τᵢˡ τⱼˡ)(σᵢ·σⱼ)` equals `(i/2)(−2J uᵢⱼ) Σₐ cᵢᵃ cⱼᵃ` on the constrained
  space, with `uᵢⱼ = i bᵢˡ bⱼˡ` and `i` on sublattice A. The difference with the
  other sign has norm 4. So the comparator's `+2J u` bond is the positive-J
  model with the bond sign reversed, as the landed review stated.
- **The odd path.** For each colour pair `(l, m)` with third colour `ν`, the
  spin term `κ τ_{q₁}ˡ τ_pᵛ τ_{q₂}ᵐ (σ_{q₁}·σ_{q₂})` equals
  `(i/2)(−2κ u(p,q₁) u(p,q₂)) Σₐ c_{q₁}ᵃ c_{q₂}ᵃ` on the constrained space. The
  sign is the same for every colour pair and for the middle site `p` on
  either sublattice, so it is uniform, not staggered.
- **The positive-J spin model is the comparator with A reversed.** Both signs
  are reversed, so on the constrained space the spin model's quadratic form
  is `−A` for the comparator's `A` at the same `κ`. Term by term this is an
  operator identity. It extends to the network because the constrained space
  is the product of the local ones and every term commutes with every
  constraint.
- **Projected sector energies do not depend on the convention.** Reversing
  the bond sign alone is the sublattice flip `S` (`c → −c` on sublattice B),
  with `det S = (−1)^{N/2}`. Reversing all of `A` sends `Pf(A)` to
  `(−1)^{N/2} Pf(A)` and leaves the single-particle levels unchanged. Either
  way, the parity entering the projection rule changes by `(−1)^{N/2}`.
  Admissible tori have `N = Lx Ly Lz / 2` with `Lx`, `Ly` even and `Lz` a
  multiple of four, so `N = 8abc` and `N/2` is even. On random bond sectors of
  the 32-, 64- and 128-site tori at `κ = 0.3`, the four conventions
  (bond ±, odd ±) give the same projected sector energy to `1.1 × 10⁻¹³`.
- **What carries over.** The projected sector energies in the landed
  composite-network notes (flux sectors, winding classes, pair excitations,
  repeated flux candidates) are those of the positive-J spin model on the
  same tori. Signs of band fluxes and group charges refer to the comparator's
  `A`. The spin model's `−A` has its band structure negated, so those signs
  reverse, as they do under `κ → −κ`.

## Boundary

- The identities are local and finite: they hold term by term on the
  constrained Clifford spaces. The global statement follows because the
  constrained space of the network is the product of the local ones and
  every term commutes with every constraint.
- Energy statements carry over; statements about signs of band fluxes or
  group charges refer to the comparator's odd-term sign and reverse under
  `κ → −κ`.
- No phase, thermodynamic statement or physical identification.

## Reproduction

```bash
python3 scripts/composite_site_network_spin_model_to_comparator_operator_identities_and_sign_conventions_2026_09_26.py
```

Four checks; prints `TOTAL: PASS=4 FAIL=0` in about 2 s.
