---
claim_id: composite_site_network_flux_free_anisotropic_touchings_exist_with_unit_charge_by_interval_gap_certificates_and_lattice_chern_numbers_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator, one copy and supplied hopping convention, at five stated anisotropic decimal couplings and two isotropic controls. Outward-rounded whole-zone clearing confines all middle-gap zeros to the recorded small cubes; their surfaces have certified positive gaps and transport/admissibility bounds. The analytic admissibility lemma equates the exact lattice integer with the occupied-bundle Chern number. The recorded integers, node locations and chirality signs are floating-point diagnostics; a 30-digit repeat on one surface is not a rounding-error enclosure. Therefore net unit charge and existence of off-plane zeros are conditional on authenticating the nonzero integers, not certified conclusions here. Exact line-node existence and signs at general positive couplings are owned by the linked general-line theorem. No unique off-plane node, all-coupling census, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_anisotropic_touchings_certified_by_lattice_chern_numbers_2026_10_01.py
---

# Anisotropic touching candidates have interval gap certificates and numerical lattice Chern values

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** interval gap and admissibility certificates with numerical charge diagnostics; unaudited.

## Supplied setting

Use the supplied comparator of the landed note
[current mathematical parent](COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md)
with general couplings `J = (J_x, J_y, J_z)`. For `J_x = J_y` that note gives
exact touching families and certifies counts with a Hessian test. For `J_x ≠ J_y`, floating probes locate candidate extra touchings off both
symmetry planes. Their exact algebraic degrees are not established here.
This block certifies gap bounds around those candidates; existence and net
charge require authentication of the computed lattice integers.

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

The floating calculation gives `|C| = 1`, `C = −sign det V`, and zero sum
at each coupling. These are reported numerical values. At D the node has a nearly flat direction, so a larger cube and a
finer mesh were needed. A 30-digit recomputation of the lattice Chern number
on the A off-plane surface agrees, with a largest phase difference of `3e-14`
over 6144 plaquettes.

## What this settles and what it does not

- **Settled at the sampled couplings.**
  - Every zero of the middle gap lies in the listed cubes.
  - Surface gaps and analytic admissibility bounds are certified.
  - If the nonzero lattice integers are authenticated, the lemma would
    imply zeros of net charge `±1` in each cube, including off-plane cubes.
    That integer authentication remains open here; the numerical values
    and 30-digit comparison do not supply a rigorous rounding bound.
- **Not settled.**
  - Authentication of the nonzero integer, and a single conical node per cube.
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
- **N6:** integer authentication, single-node counts and other couplings remain open.
- **N7:** other sectors, couplings and certificates remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_anisotropic_touchings_certified_by_lattice_chern_numbers_2026_10_01.py
```

Nine checks; prints `TOTAL: PASS=9 FAIL=0` in about eighty seconds.

The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) sets the premise boundary. The supplied comparator is not a framework-law or physical-species selection. Original source and execution history remain recoverable at [PR #9419](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9419); this is provenance, not audit authority.

Network definition: [current supplied network](THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md).
Exact line-node existence and conical signs: [general-line theorem](COMPOSITE_SITE_NETWORK_FLUX_FREE_THE_LINE_TOUCHINGS_AND_THEIR_CHARGES_ARE_EXACT_FOR_GENERAL_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-10-01.md).
