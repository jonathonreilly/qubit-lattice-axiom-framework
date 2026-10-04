---
claim_id: composite_site_network_flux_free_every_touching_of_the_three_families_has_an_exact_charge_for_all_couplings_and_the_charges_sum_to_zero_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, J_x = J_y = 1, J_z = J with 0 < J < 2, odd term kappa > 0, four-site Bloch matrix H(f) = i M(f), and the three exact touching families of the landed certificate note: (i) line nodes (x, 1-x, 0), (1-x, x, 0), x in (0, 1/2), for every kappa; (ii) (x_o, 1-x_o, +-f3), (1-x_o, x_o, +-f3) for kappa_c < kappa < kappa_h; (iii) (+-F+G, +-F-G, +-F), (+-F-G, +-F+G, +-F) for kappa > kappa_h, with kappa_c^2 = J(J+2)/[4(4+2J-J^2)], kappa_h^2 = J/[4(2-J)]. Exact symbolic arithmetic in towers of quadratic extensions of Q(kappa, J), no floating point: at every node tr M = 0 and the kernel projector has rank two (a double zero level), and T = Im Tr(P d1H P d2H P d3H) = 2 det V (the landed chirality quantity) has the closed forms T(L+) = 32 pi^3 kappa d (J+2)(4 kappa^2 + 1) F2 sin(2 pi x)/(dU - V) on the line, T = -16 pi^3 (J+1) F1 F2 sin(2 pi x)/(kappa J (J+2)) on plane (ii), and T = -8 pi^3 b sin(2 pi g)/e2(M)^3 on plane (iii), where F1 = J - 4(2-J) kappa^2, F2 = J(J+2) - 4 kappa^2 (4+2J-J^2), d, U, V explicit, dU - V > 0, b > 0 and e2(M) > 0 on the domain. Hence on each family's open domain every node is a conical touching of charge +-1: the line nodes carry sign F2 and -sign F2 (they flip exactly at kappa_c), the plane (ii) nodes with x_o < 1/2 carry +1 and the others -1, the plane (iii) nodes carry -sign sin(2 pi g), g = (f1 - f2)/2; the charges sum to zero in each kappa range. The thirteen landed chirality strings are reproduced, and exact per-coupling arithmetic at 776 rational couplings agrees. Not covered: the transition couplings kappa_c and kappa_h (T = 0 there), completeness of the families away from the landed certified couplings, J outside (0, 2), J_x != J_y, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
  - composite_site_network_flux_free_handover_touchings_are_exact_charge_two_points_for_every_j_between_0_and_2_bounded_theorem_note_2026-09-28
runner: scripts/composite_site_network_flux_free_exact_charge_of_every_family_touching_for_all_couplings_2026_10_01.py
---

# Every touching of the flux-free comparator's three families has an exact charge for all couplings, and the charges sum to zero

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact symbolic algebra for a supplied comparator; unaudited.

## Supplied setting

Use the supplied comparator and the three exact touching families of the landed note
[current mathematical parent](COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md):
- `J_x = J_y = 1`, `J_z = J` with `0 < J < 2`, odd term `κ > 0`, and
  `H(f) = iM(f)`;
- `κ_c² = J(J+2)/[4(4+2J−J²)]` and `κ_h² = J/[4(2−J)]`.

That note certified the chirality signs at thirteen couplings. The landed
handover note
[current mathematical parent](COMPOSITE_SITE_NETWORK_FLUX_FREE_HANDOVER_TOUCHINGS_ARE_EXACT_CHARGE_TWO_POINTS_FOR_EVERY_J_BETWEEN_0_AND_2_BOUNDED_THEOREM_NOTE_2026-09-28.md)
treats the merged points at `κ_h`.

**Chirality.** The chirality is `sign T`, with
`T = Im Tr(P ∂₁H P ∂₂H P ∂₃H) = 2 det V`, the landed quantity. Here `P` is
the kernel projector and the derivatives are taken in the fractional
momenta.

## Method

**The algebra the nodes live in.** At a node, each `z_j = e^{2πif_j}` lies in
a tower of quadratic extensions of `Q(κ, J)`:
- a circle level `g² = p g − 1`, with `p = 2 cos 2πf`;
- for the line and plane (iii), a real radical level.

Complex conjugation of the node is the automorphism `z → 1/z`, so real and
imaginary parts are read off exactly.

**The kernel projector.** With `Pt = M² − tr(M) M + e₂(M) I`, the runner
checks `tr M = 0`, `M Pt = 0`, `Pt² = e₂ Pt` and `tr Pt = 2e₂` exactly at
every family node. So `P = Pt/e₂` is the rank-two kernel projector, and zero
is a double level. Also `e₂(M) = Σ|M_ij|²/2 > 0`.

**The chirality quantity.** `∂_jH = −2πN_j`, with `N_j = z_j ∂M/∂z_j`, so
`T = −8π³ Im Tr(Pt N₁ Pt N₂ Pt N₃)/e₂³`.

## Result

Write `u = κ²`, `F₁ = J − 4(2−J)u` (zero at `κ_h`) and
`F₂ = J(J+2) − 4u(4+2J−J²)` (zero at `κ_c`).

1. **Line nodes, every κ.**
   - Write `d² = 1 + 8u + 16u² − 4uJ²`, `U = 8Ju + J + 8u + 2`, and `V` the
     explicit polynomial in the runner.
   - The trace is a real multiple of `z − c`, with `c = (1−d)/(4u)`, giving
     `T(x, 1−x, 0) = 32π³ κ d (J+2)(4u+1) F₂ sin(2πx)/(dU − V)`.
   - `dU − V > 0` on the whole domain: `d ≥ |4u−1|`, together with two
     polynomial identities with positive terms.
   - So the node with `x < 1/2` has charge `sign F₂`, and its mirror the
     opposite. The line charges flip exactly at `κ_c`.
2. **Plane (ii), κ_c < κ < κ_h.**
   - The trace has no part depending on the sign of `f₃`.
   - `T = −16π³ (J+1) F₁ F₂ sin(2πx)/(κJ(J+2))`.
   - The nodes are real and distinct exactly when `F₂ < 0 < F₁`, and there
     `T > 0` for `x_o < 1/2`.
   - Charges: `+1` for `(x_o, 1−x_o, ±f₃)` and `−1` for `(1−x_o, x_o, ±f₃)`.
3. **Plane (iii), κ > κ_h.**
   - The trace is `(r₀ + r₁s) + b·y`, with `y = e^{2πig}` and
     `s = √(5J² + 8J + J(J+2)/κ²)`. It has no part depending on the sign of
     `f₃`.
   - `b = r₄ + r₅s`, where `r₅ > 0` (a polynomial with positive
     coefficients).
   - The norm `r₄² − r₅²s²` factors as `F₁` times a product of positive or
     squared factors whose zeros lie outside the domain. So it is negative
     for `κ > κ_h`, which with `r₅ s > 0` forces `b > 0`.
   - `T = −8π³ b sin(2πg)/e₂³`, so the charge is `−sign sin 2πg`.
4. **Charge map and sum rule.**

   | κ range | line (x < 1/2, mirror) | plane (ii) | plane (iii) | total |
   |---|---|---|---|---|
   | `κ < κ_c` | `+1, −1` | none | none | 0 |
   | `κ_c < κ < κ_h` | `−1, +1` | `+1, +1, −1, −1` | none | 0 |
   | `κ > κ_h` | `−1, +1` | none | `−1` for `sin 2πg > 0`, `+1` otherwise | 0 |

   The sum is zero in each range because each family's trace depends on its
   nodes through a real multiple of `z − c` or `y` alone. The mirror nodes are
   Galois conjugates, so their `T` values cancel in pairs.
5. **Transitions.** The runner checks three exact identities:
   - at `κ_c`, the line cosine equals the plane (ii) cosine, with
     `cos 2πf₃ = 1`;
   - at `κ_h`, `cos 2πf₃ = −1`, `cos 2πx = J − 1` and `s = J + 4`;
   - `κ_h² − κ_c² = J²/(2(2−J)(4+2J−J²)) > 0`.

   Charge bookkeeping on the `x < 1/2` side:
   - at `κ_c` the line node's `+1` becomes `−1 + 1 + 1`;
   - at `κ_h` the plane (ii) pair (`+1` each) continues as the plane (iii)
     pair with `sin 2πg < 0` (`+1` each), giving the landed charge-two
     merged point.
6. **Cross-checks.**
   - Exact per-coupling tower arithmetic at 776 rational couplings, across
     all three regimes, gives the predicted charge strings.
   - The closed forms reproduce all thirteen landed chirality strings.

## What this settles and what it does not

- **Settled.** For every `0 < J < 2` and `κ > 0` away from `κ_c` and `κ_h`,
  each node of each family is conical with charge `±1`, as in the table, and
  the charges sum to zero. This replaces the thirteen sampled signs with
  exact all-coupling formulas.
- **Not settled here.**
  - At `κ_c` and `κ_h`, `T = 0` and the touchings are not conical. The
     merged points at `κ_h` are the landed charge-two points. The merged
     point at `κ_c` is not analysed.
  - That the three families are all the touchings is certified at the
     landed couplings, not between them.
  - `J ≥ 2`, `J_x ≠ J_y`, equality with the spin model, and any physical
     reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator with `J_x = J_y = 1`, `0 < J < 2`, `κ > 0`; the landed families.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed certificate and handover notes govern their scopes; their families and chirality convention are used as stated there.
- **N5:** exact symbolic identities; the rational-coupling and landed-string checks are exact.
- **N6:** the transition couplings and completeness between the landed couplings remain open.
- **N7:** other sectors, couplings and anisotropies remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_exact_charge_of_every_family_touching_for_all_couplings_2026_10_01.py
```

Twenty-seven checks; prints `TOTAL: PASS=27 FAIL=0` in about seventy seconds.

The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) sets the premise boundary. The supplied comparator is not a framework-law or physical-species selection. Original source and execution history remain recoverable at [PR #9417](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9417); this is provenance, not audit authority.

Network definition: [current supplied network](THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md).
