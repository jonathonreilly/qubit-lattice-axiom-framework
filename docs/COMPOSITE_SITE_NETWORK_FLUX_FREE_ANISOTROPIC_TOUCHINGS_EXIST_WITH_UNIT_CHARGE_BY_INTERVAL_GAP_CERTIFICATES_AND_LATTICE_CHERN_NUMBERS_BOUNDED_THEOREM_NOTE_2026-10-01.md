---
claim_id: composite_site_network_flux_free_anisotropic_touchings_exist_with_unit_charge_by_interval_gap_certificates_and_lattice_chern_numbers_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, four-site Bloch matrix H(f) = i M(f), couplings J = (J_x, J_y, J_z) and odd term kappa. At five anisotropic couplings, A (1, 0.8, 1; 0.45), B (1.2, 0.8, 1; 0.3), C (1, 0.8, 1; 0.8), D (1.2, 0.8, 1; 0.2), E (0.9, 1.1, 1.3; 0.4), and two isotropic controls (J = 1, kappa = 3/10 and 9/20): outward-rounded interval inertia clears the whole fractional zone of zeros of the middle gap except 6, 6, 6, 2, 2 (and 2, 6) small clusters; each cluster lies strictly inside a cube surface on which the middle gap is interval-certified (minimum 2.5e-3 to 1.9e-2); an admissibility lemma proved here (plaquette flux plus four edge transport mismatches below pi, bounded by interval-evaluated constants, at most 0.76) makes the Fukui-Hatsugai-Suzuki lattice Chern number of the two lowest bands equal to the Chern number of the occupied bundle on each surface; and that number is -1 or +1 on every cube, summing to zero at each coupling. So at each sampled anisotropic coupling every zero of the middle gap lies in the listed cubes and each cube contains zeros of net charge +-1; for J_x != J_y this includes cubes about off-plane points such as (0.222999, 0.686437, 0.250240) at A and (0.255057, 0.589947, 0.042639) at B, whose positions are not low-degree algebraic. The isotropic controls reproduce the landed exact family nodes and the landed chirality sign. The lattice integer is evaluated in floating point with a per-plaquette margin of at least 2.38 radians and recomputed at 30 digits on one surface. Not covered: that a cube holds a single conical node, couplings between the samples, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_anisotropic_touchings_certified_by_lattice_chern_numbers_2026_10_01.py
---

# Anisotropic touchings of the flux-free comparator exist with unit charge, by interval gap certificates and lattice Chern numbers

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** computer-assisted certificate at sampled couplings; unaudited.

## Supplied setting

Use the supplied comparator of the landed note
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`
with general couplings `J = (J_x, J_y, J_z)`. For `J_x = J_y` that note gives
exact touching families and certifies counts with a Hessian test. For
`J_x ≠ J_y` the extra touchings leave both symmetry planes, and their
positions are not low-degree algebraic. That certificate then needs exact
node positions it does not have. This block certifies existence and net
charge without exact positions.

## Certificate

1. **Zone clearing.**
   - A cube with dyadic centre `c` and half-width `h` is cleared when two
     outward-rounded interval `LDLᵀ` inertias of `H(c) − x₁` and `H(c) − x₂`
     each give exactly two negative pivots, and `x₂ − x₁ > 2r`.
   - `r = h·ρ(E_x + E_y + E_z)` bounds `‖H(f) − H(c)‖` by Weyl's inequality.
     Here `E_j` is the entrywise bound of `|∂H/∂f_j|` from the hopping terms,
     and `ρ` is a Collatz–Wielandt upper bound.
   - The cleared plus uncleared volume is exactly 1. Uncleared cubes form
     clusters, and each cluster must lie strictly inside a cube surface `Σ`
     around its float node.
2. **Gap on Σ.** On each of the `6m²` patches of `Σ`, the same interval
   inertia certifies a lower bound of the middle gap; `g` is the minimum.
3. **Admissibility lemma.** Let `P` be the projector on the two lowest
   bands, `Q = 1 − P` and `Y_j = Q ∂_jP P`. Let `Fro_j`, `Op_j`, `Op2_j` be
   outward-rounded bounds of `‖∂_jH‖_F`, `‖∂_jH‖_op` and `‖∂_j²H‖_op`.
   - (i) `Y_j` solves `H_Q Y − Y H_P = −(∂_jH)_{QP}`, so `‖Y_j‖_F ≤ Fro_j/g`.
     The Riesz integral along the mid-gap line gives `‖∂_jP‖ ≤ Op_j/g` and
     `‖∂_j²P‖ ≤ Op2_j/g + 8Op_j²/(πg²)`.
   - (ii) The curvature of the determinant bundle is
     `F_ab = 2i Im tr(Y_a†Y_b)`, so a plaquette of side `h` has flux
     `|Φ_p| ≤ 2h²Fro_aFro_b/g²`.
   - (iii) Compare the horizontal lift `ũ` along an edge with the endpoint
     frame. The overlap is `I − G` with `‖G‖_F ≤ x = α²h²/2`, where
     `α = Fro/g`. The first-order term vanishes, and the second-order trace
     is real. So the phase mismatch satisfies
     `|δ_e| ≤ α b₂ h³/6 + x²/(1 − x)`, where
     `b₂ = √2‖∂²P‖ + ‖∂P‖α`.
   - (iv) The principal plaquette phase of the Fukui link product is
     `Φ_p + Σ_e δ_e` whenever `|Φ_p| + Σ|δ_e| < π`. The edge terms cancel
     over a closed surface, so the lattice Chern number equals the Chern
     number of the occupied bundle on `Σ`.
4. **Conclusion per cube.** A nonzero Chern number on `Σ` means the middle
   gap vanishes inside the solid cube, with net charge equal to it. The
   clusters' Chern numbers sum to zero, because the occupied bundle exists on
   the complement. The convention is `C = −sign det V`, where `sign det V` is
   the landed chirality. The isotropic controls check this convention.

## Result

| coupling | cubes | min gap on Σ | admissibility bound | `C` per cube | off-plane point (float) |
|---|---|---|---|---|---|
| iso `J = 1`, `κ = 3/10` | 2 (= landed line nodes) | — | `0.094` | `−, +` | — |
| iso `J = 1`, `κ = 9/20` | 6 (= landed nodes) | — | `0.306` | `−,−,+,−,+,+` | — |
| A `(1, 0.8, 1)`, `0.45` | 6 | `7.6e-3` | `0.112` | `−,−,+,−,+,+` | `(0.222999, 0.686437, 0.250240)` |
| B `(1.2, 0.8, 1)`, `0.3` | 6 | `5.7e-3` | `0.134` | `−,+,−,+,−,+` | `(0.255057, 0.589947, 0.042639)` |
| C `(1, 0.8, 1)`, `0.8` | 6 | `1.9e-2` | `0.039` | `−,−,+,−,+,+` | `(0.035263, 0.687476, 0.340488)` |
| D `(1.2, 0.8, 1)`, `0.2` | 2 | `2.5e-3` | `0.624` | `−, +` | — (line nodes) |
| E `(0.9, 1.1, 1.3)`, `0.4` | 2 | `3.6e-3` | `0.76` | `−, +` | — (line nodes) |

Every cube has `|C| = 1`, `C = −sign det V`, and the sum over each coupling
is zero. At D the node has a nearly flat direction, so a larger cube and a
finer mesh were needed. A 30-digit recomputation of the lattice Chern number
on the A off-plane surface agrees, with a largest phase difference of `3e-14`
over 6144 plaquettes.

## What this settles and what it does not

- **Settled at the sampled couplings.**
  - Every zero of the middle gap lies in the listed cubes.
  - Each cube contains zeros of net charge `±1`.
  - For `J_x ≠ J_y` (A, B, C) this certifies off-plane touchings, with the
    same charge pattern as the isotropic families, where no exact positions
    are known.
- **Not settled.**
  - That a cube holds a single conical node: the charge is a net charge.
    Float Newton probes find one node per cluster.
  - The integer itself is evaluated in floating point. Its per-plaquette
    margin is at least `π − 0.76 = 2.38`, and it is recomputed at 30 digits
    on one surface, but it is not interval-verified.
  - Couplings between the samples, equality with the spin model, and any
    physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator at seven sampled couplings.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed certificate note's families and chirality convention are used for the controls.
- **N5:** interval-certified clearing, gaps and admissibility bounds; a float integer with a stated margin.
- **N6:** single-node counts and other couplings remain open.
- **N7:** other sectors, couplings and certificates remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_anisotropic_touchings_certified_by_lattice_chern_numbers_2026_10_01.py
```

Nine checks; prints `TOTAL: PASS=9 FAIL=0` in about eighty seconds.
