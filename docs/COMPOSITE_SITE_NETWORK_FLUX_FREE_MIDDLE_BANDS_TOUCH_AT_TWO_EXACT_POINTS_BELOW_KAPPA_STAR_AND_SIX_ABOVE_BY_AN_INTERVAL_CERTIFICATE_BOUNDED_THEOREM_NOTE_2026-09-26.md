---
claim_id: composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, couplings J_x = J_y = 1, J_z = J, odd term kappa, four-site Bloch matrix H(f) = i M(f). Exact at real momenta where the displayed expressions are defined: det H, its gradient and the constant and linear characteristic-polynomial coefficients vanish on three families. (i) Two line points (x, 1 - x, 0), (1 - x, x, 0) with 4 kappa^2 c^2 - 2c + J^2 - 4 kappa^2 - 2 = 0, c = cos 2 pi x in (-1, 1) where such a root exists. (ii) Four points (x, 1 - x, +-f3), (1 - x, x, +-f3) with cos 2 pi x = 1 - J/(4 kappa^2), cos 2 pi f3 = (J + 2)/(4 kappa^2) - (4 + J - J^2)/J, real between the landed kappa_c^2 = J(J + 2)/[4(4 + 2J - J^2)] and kappa_h^2 = J/[4(2 - J)]. (iii) Four points (f3 + g, f3 - g, f3) with cos 2 pi f3 = [J + 2 - sqrt(5J^2 + 8J + J(J + 2)/kappa^2)]/2 and cos 2 pi g = -J - cos 2 pi f3, real from kappa_h. Computer-assisted count at thirteen couplings: J = 1 with kappa = 1/10, 3/10, 7/20 (two nodes) and 9/20, 12/25, 3/5, 4/5, 1 (six); J = 1/2 with kappa = 1/5 (two) and 2/5 (six); J = 3/2 with kappa = 2/5 (two) and 7/10, 1 (six). There det H vanishes at exactly these nodes; zero is a double level with the outer levels nonzero; each touching is conical with a certified chirality sign det V, summing to zero; and everywhere else H has two negative and two positive levels. At J = 5/2, kappa = 3/10 no family exists and the middle gap is certified open everywhere. Certificate: exact rational algebra plus interval arithmetic (outward-rounded IEEE float operations, mpmath interval functions) with the landed Lipschitz bound. No count between the sampled couplings, other anisotropies, spin-Hamiltonian equivalence, ground-sector selection, phase or physical identification."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_bands_with_the_odd_term_two_certified_touchings_of_opposite_charge_become_six_at_kappa_root_3_over_20_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_middle_band_touchings_two_below_kappa_star_and_six_above_interval_certificate_2026_09_26.py
---

# Certified middle-band touchings of a supplied comparator at thirteen couplings

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** exact node families on their defined real-momentum domains, and a computer-assisted count, conical form and chirality at thirteen couplings and a certified gap at a fourteenth, for a supplied comparator; unaudited.

## Supplied setting

Use the supplied comparator of the landed note
[COMPOSITE_SITE_NETWORK_FLUX_FREE_BANDS_WITH_THE_ODD_TERM_TWO_CERTIFIED_TOUCHINGS_OF_OPPOSITE_CHARGE_BECOME_SIX_AT_KAPPA_ROOT_3_OVER_20_BOUNDED_THEOREM_NOTE_2026-09-26](COMPOSITE_SITE_NETWORK_FLUX_FREE_BANDS_WITH_THE_ODD_TERM_TWO_CERTIFIED_TOUCHINGS_OF_OPPOSITE_CHARGE_BECOME_SIX_AT_KAPPA_ROOT_3_OVER_20_BOUNDED_THEOREM_NOTE_2026-09-26.md):
the colored network of
[THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24](THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md)
with the explicitly supplied real antisymmetric hopping matrix. Take `u = +1`,
one quadratic copy, the landed four-site reduction `H(f) = i M(f)` over the
fractional zone, and couplings `J_x = J_y = 1`, `J_z = J`, odd term `κ`.

That note found two numerical groups of touchings below the split and six
above. It gave the exact split `κ_c² = J(J + 2)/[4(4 + 2J − J²)]` and the
line identity `D = 16[J² + 4c²κ² − 2c − 4κ² − 2]²` on `f = (x, 1 − x, 0)`. It
left open:
- a certified exclusion of other zeros;
- an exact node count;
- where the groups sit;
- node charges;
- dispersion order.

It also retained the Lipschitz bound `‖H(f) − H(f′)‖ ≤ lip ‖f − f′‖∞`.

## Result

**Exact node families on their defined domains.** At every point below, `D = det H`, its
three momentum derivatives, and the constant and linear coefficients of
`det(H − λ)` vanish exactly.

| family | where real | points | condition |
|---|---|---|---|
| **(i) Line** | where the quadratic has a root in `(−1, 1)` | `(x, 1 − x, 0)`, `(1 − x, x, 0)` | `4κ²c² − 2c + J² − 4κ² − 2 = 0`, `c = cos 2πx` |
| **(ii) Plane `f₁ + f₂ = 1`** | `κ_c < κ ≤ κ_h` | `(x, 1 − x, ±f₃)`, `(1 − x, x, ±f₃)` | `cos 2πx = 1 − J/(4κ²)`, `cos 2πf₃ = (J + 2)/(4κ²) − (4 + J − J²)/J` |
| **(iii) Plane `f₁ + f₂ = 2f₃`** | `κ ≥ κ_h` | `(f₃ + g, f₃ − g, f₃)`, all four sign choices | `cos 2πf₃ = [J + 2 − √(5J² + 8J + J(J + 2)/κ²)]/2`, `cos 2πg = −J − cos 2πf₃` |

The table's birth and handover ranges assume `0 < J < 2` and `κ > 0`.
For other real couplings use the explicit cosine conditions only when defined
and in `[−1,1]`; the four sign choices may coincide at boundaries.
Here `κ_h² = J/[4(2 − J)]` for `0 < J < 2`. The families fit together exactly:
- **Birth at κ_c.** Family (ii) starts at `cos 2πf₃ = 1`, which reproduces
  the landed `κ_c`. There `cos 2πx = (J − 2)(J + 1)/(J + 2)`, the landed
  `c*`, so its four nodes are born from the line nodes.
- **Handover at κ_h.** Family (ii) reaches `cos 2πf₃ = −1`, where family
  (iii) starts. The two planes meet at `f₃ = 1/2`, and the nodes pass from
  one to the other. At `J = 1` this happens at `κ = 1/2` and the rational
  points `(1/4, 3/4, 1/2)`, where the landed rational-point polynomial
  vanishes.

**Theorem (computer-assisted).** At the thirteen couplings:
- `J = 1`: `κ = 1/10`, `3/10`, `7/20` (two nodes) and `9/20`, `12/25`,
  `3/5`, `4/5`, `1` (six);
- `J = 1/2`: `κ = 1/5` (two) and `2/5` (six, family iii);
- `J = 3/2`: `κ = 2/5` (two), `7/10` (six, family ii) and `1` (six,
  family iii).


At each of these couplings:
- `D` vanishes exactly at the family nodes and nowhere else in the zone;
- at each node zero is a double level and the outer two levels are nonzero;
- each touching is conical: on its box the middle gap lies between
  `c|f − f*|` and `2 lip |f − f*|∞`, with `c` from `0.009` (at `J = 1/2`,
  `κ = 1/5`) to `0.81` (at `J = 3/2`, `κ = 2/5`);
- each node has a certified chirality `sign det V`, and these sum to zero;
- everywhere else `H` has two negative and two positive levels.

So the middle bands touch exactly at these points, at zero energy, and the
middle gap is open everywhere else.

**A gapped coupling.** At `J = 5/2`, `κ = 3/10` the line quadratic has
negative discriminant (`−1001/2500`) and `κ² < κ_c²`, so no family exists.
The interval clearing leaves no cube, with every cube certified to have two
negative and two positive levels. So the middle gap is open everywhere. This
is the certified form of the landed note's numerical control at `J_z = 2.5`.

**Chirality through the split.** Take the side `x < 1/2`.
- Below `κ_c` its line node has `sign det V = +1`.
- Between `κ_c` and `κ_h` that line node has `−1`, and the two new family-(ii)
  nodes on the same side have `+1` each. The side total `+1` is conserved.
- The landed discrete sphere fluxes at `J = 1`, `κ = 0.3` equal
  `−sign det V`.

## Proof structure

1. **Exact algebra.** Determinants are computed in polynomial rings with
   rational amplitudes `2`, `2J` and `2κ`, where `κ` and `J` are symbolic.
   `D`, `∂D/∂f_j = 2πi z_j ∂D/∂z_j` and the two characteristic
   coefficients reduce to zero:
   - on the line, modulo `κ²z⁴ − z³ + (J² − 2κ² − 2)z² − z + κ²`;
   - on family (ii), modulo its two cosine quadratics;
   - on family (iii), with `z₁ = wy`, `z₂ = w/y`, modulo its two cosine
     quadratics and the equation defining `s`.

   All three derivatives are included, so each point is a critical point of
   `D` in the full zone. The same computation reproduces the landed line
   identity, and at `J = 1` the landed rational-point polynomial.
2. **Rigorous clearing.** Cubes `[c − h, c + h]³` with exact dyadic centres
   start from `32³` and are split eight ways, thirteen times. For each cube:
   - `H(c)` is enclosed entrywise with `mpmath` interval phases and
     outward-rounded float arithmetic, including outward conversion of high-precision
     interval endpoints and the Lipschitz bound;
   - interval `LDL*` inertia of `H(c) ∓ rI` is computed, with `r` rounded
     up from `lip·h`;
   - equal certified negative counts at `±r` show that no level vanishes in
     the cube (by Weyl's inequality) and that the count holds throughout.

   Every cleared cube has count exactly 2. The uncleared cubes form exactly
   as many groups as there are family nodes.
3. **Boxes.**
   - **Node.** Each group's bounding box contains exactly one family node,
     enclosed to `1e-12` by a certified sign change of its cosine equation.
   - **Double level.** Interval evaluation of the quadratic characteristic
     coefficient at the node excludes zero, so the outer levels are nonzero
     there.
   - **Uniqueness.** The Hessian of `D` is positive definite on the box
     (centred interval forms, bisection, interval Cholesky). With `D = 0`
     and `∇D = 0` at the node, Taylor's theorem gives `D > 0` on the box
     except at the node.
   - **Conical bound.** If `Hess D − mI` is also certified positive definite
     on the box, then `D ≥ (m/2)|δ|²`. Since `|λ₁λ₄| ≤ ‖H‖²`, AM–GM on
     `λ₂ ≤ 0 ≤ λ₃` gives a middle gap of at least `√(2m)|δ|/‖H‖`. The upper
     bound `2 lip |δ|∞` is Weyl's inequality.
   - **Chirality.** At the node the kernel projector is
     `P = (H² − tr(H) H + qI)/q`, where `q` is the sum of principal 2×2
     minors (nonzero, because the outer levels are nonzero). With
     `P ∂ᵢH P = aᵢ + vᵢ·σ`, the identity
     `Im Tr(P∂₁H P∂₂H P∂₃H) = 2 det[v₁, v₂, v₃]` holds in any basis of the
     kernel. Evaluated in interval arithmetic on the node enclosure, it
     excludes zero.
4. **Conclusion.**
   - `D ≠ 0` off the nodes.
   - The negative count is locally constant where `D ≠ 0`, equals 2 on the
     cleared cubes, and equals 2 on each punctured box, which is connected
     and meets the cleared cubes.
   - So `λ₂ < 0 < λ₃` off the nodes. At the nodes, `λ₂ = λ₃ = 0` with
     `λ₁ < 0 < λ₄`.

A sanity check also passes: at dyadic points the interval matrices contain
40-digit evaluations of the entries, and the interval inertia agrees with
floating eigenvalue counts.

## What this settles and what it does not

- **Settled at the thirteen couplings.**
  - The landed note's numerical groups each contain exactly one touching,
    at an exact point, and there is no other zero in the zone.
  - The touchings are conical, with certified chiralities.
  - Read through the families, the landed "two become six" is a birth from
    the line nodes at `κ_c` followed by a handover between two planes at
    `κ_h`.
- **Not certified here.**
  - The exact count at couplings between the samples. Near `κ_c` and `κ_h`
    the Hessian softens: at `J = 1`, `κ = 2/5` and at `J = 1/2`,
    `κ = 27/100` (inside the narrow family-(ii) window) the
    positive-definiteness step did not succeed within the bisection depth
    used, so those couplings are not included.
  - Anisotropies other than `J_x = J_y`.
  - Equality with the spin model.

## Arithmetic boundary

The certificate assumes:
- IEEE 754 double precision with round-to-nearest for `+ − × ÷`, so one
  outward `nextafter` step encloses each exact result;
- the correctness of `mpmath`'s interval elementary functions;
- `sympy`'s exact rational polynomial arithmetic.

Floating eigenvalues enter the sanity check and nothing in the certificate.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator with `J_x = J_y = 1`; exact families on their defined real-momentum domains, certificates at thirteen rational couplings and a certified gap at a fourteenth.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed parent's reduction, identities and Lipschitz bound are used as stated there.
- **N5:** exact positions, counts, conical form and chiralities; nothing is claimed between the sampled couplings.
- **N6:** a coupling interval and other anisotropies remain open.
- **N7:** other sectors, couplings and certificates remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_middle_band_touchings_two_below_kappa_star_and_six_above_interval_certificate_2026_09_26.py
```

Eighteen checks; prints `TOTAL: PASS=18 FAIL=0` in about five minutes.

## Premise authority

[Current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).
