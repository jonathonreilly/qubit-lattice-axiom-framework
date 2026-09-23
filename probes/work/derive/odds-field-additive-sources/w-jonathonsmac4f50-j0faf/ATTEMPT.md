# odds-field-additive-sources, attempt a2: the massless case, computed

**Provenance.** Written by Claude Opus 5.5 (`claude-opus-5-5`), worker `w-jonathonsmac4f50-j0faf`, task
`J:derive:odds-field-additive-sources:a2`.

The prior attempt a3 (`w-jonathonsmac4f50-j38d3`) was written by Claude Opus 5 (`claude-opus-5`). That is
the same model family as this worker, and a3 is unrefereed. Block 42 was supervisor-run in the same family.

**Plan before reading a3.** My plan was to reduce (b) to the exact two-record formula and to compute the arrays and `D*` from
the lattice Green function.

a3 had done the screened case on tori of side 5 to 7 with exact Fractions. It listed as open:
- the massless case, the one the gravity lane needs, where the torus operator is singular;
- the constant `κ` of `D*`.

It also asserted that on the massless surface the 10 percent criterion "is not met at any separation a lattice body offers".
This attempt computes the massless case on the infinite lattice and tests that sentence. Part (a) is not redone here: I did
not reread the axioms memo for this unit and make no claim about it.

## 1. What is claimed

**Setting.** The setting is block 42's linear odds field, with a record as a boundary value (open PR "ail42"; supplied
reading, not adopted).
- The lean of a set `A` of records is `v(x) = P_x(`the walk hits `A` before it is killed`)`. The walk steps to a uniform
  neighbour and survives each step with probability `θ = 6l₁`.
- Its Green function is `G = (I − θP)⁻¹ = (1/l₁)(−Δ + m²)⁻¹`, with `m² = (1 − 6l₁)/l₁`.
- Capacity is `cap(A) = 1ᵀG_A⁻¹1`. Far from `A`, `v ≈ cap(A)·G(x)`.
- Numbers are given in the massless walk's normalization (`θ = 1`, as at `(3,1,2)`). There `c₁ = 1/G(0) = 0.65946267`.

**(b1) Two records.**
- The exact identity is `cap₂/(2c₁) = G(0)/(G(0) + G(r))`. So two records add to within 10 percent iff `G(r)/G(0) ≤ 1/9`.
- **In the massless case this holds at every separation with `|r|² ≥ 8`, and at none with `|r|² ≤ 6`.** The failing set is
  exactly `(1,0,0), (1,1,0), (1,1,1), (2,0,0), (2,1,0), (2,1,1)` and their images.
- At the boundary, `G(2,2,0)/G(0) = 0.1110080 < 1/9 < 0.1264794 = G(2,1,1)/G(0)`.
- a3's "not met at any separation" is therefore false.
- The threshold shrinks with the range `1/m` of the lean:

| range | threshold |
|---|---|
| ∞ (massless) | `√8` |
| 10 | `√6` |
| 4.5 | `√5` |
| 3.2 | `√3` |
| 1.4 | `√2` |
| 0.45 (a3's `(2,1,2)`) | adjacent sites |

**(b2) Arrays of `N³` records at spacing `d`, massless.** Many records do not add even when every pair does.
- 8 records reach 90 percent of `8c₁` only at spacing `d ≥ 17`.
- The ratio `cap/(N³c₁)` follows `1/(1 + (N/N*)²)`, with `N* = √(κd/c₁)`, to within 0.04 for `N = 2..8` and `d = 2, 4, 8`.
- It is bracketed by two proved bounds: `N⁶/Σ_ij G_ij ≤ cap ≤ N³c₁`. The lower bound has the same shape.

**(c) The crossover and κ.**
- The capacity of a solid lattice cube grows linearly in its side, with `κ = 1.381`. The continuum cube's `0.6607·4π/6 = 1.3838`
  is the expected limit; it is not used.
- A dilute body therefore shields itself beyond **`D* = √(κ/c₁) d^{3/2} = 1.447 d^{3/2}`**, which is the unit's expected form,
  now with its constant.
- Past `D*` a body's strength is `κ ×` its side, not `c₁ ×` its record count. The mutual lean of two large bodies at distance
  `R` goes as `cap₁cap₂G(R) ≈ κ²D₁D₂·3/(2πR)`: a one-over-distance law whose coefficient is a product of linear sizes, not of
  record counts.
- **With any screening** the charge of a record deep inside an infinite array converges to `c₁/(1 + S)`, with
  `S = Σ_j G(dj)/G(0)`. So a screened body's strength stays proportional to its record count, with a finite factor, and has
  no crossover size. For example, at `m² = 1` the factor is 0.17, 0.68 and 0.92 at spacings 1, 2 and 3. The capacity law
  that defeats additivity belongs to the massless lean.

## 2. Steps

1. **ASSUMED — the setting.** Block 42's linear odds field with records as boundary values, as supplied (not adopted).

2. **PROVED / CHECKED (E1) — two records.**
   - By symmetry, the 2×2 system `[[G(0), G(r)], [G(r), G(0)]] e = 1` has `e = 1/(G(0) + G(r))` per record.
   - Hence `cap₂ = 2/(G(0) + G(r))` and `cap₂/(2c₁) = G(0)/(G(0) + G(r))`, which is `≥ 9/10` iff `G(r)/G(0) ≤ 1/9`.
   - The identity is also in a3, from its own derivation.

3. **CHECKED (E2) — exact anchor.** On the 7-torus at `m² = 5`, the exact rational `G(e₁)/G(0) = 0.09895102` from an
   orbit-reduced Fraction solve is a3's value. The infinite-lattice quadrature gives `0.09894893`. The two methods agree
   where both apply.

4. **NUMERICAL (N1) — validation of the quadrature.** `G(x) = ∫₀^∞ e^{−m²t} Π_i ive(|x_i|, 2t) dt`, with an erf tail term in
   the massless case, satisfies:
   - `G_SRW(0) = 1.5163860510`, against Watson's closed form `1.5163860592` (ASSUMED, used only as a check);
   - the exact identity `G(e₁) = G(0) − 1`, to `6·10⁻⁹`;
   - the lattice equation at `0` and at `e₁` for `m² = 0, 0.1, 5`, to `10⁻⁸`.

   Every margin used below is larger than `10⁻⁶`.

5. **NUMERICAL (N2) — the massless two-record threshold.** Every separation vector with `|coordinates| ≤ 12` is checked. The
   smallest margins are `1.5·10⁻²` on the failing side and `1.0·10⁻⁴` on the passing side, the latter at `(2,2,0)`. Beyond
   `12`, `G(r)/G(0) ≤ 0.03` by the asymptotic form `G ≈ 3/(2π|r|)` (ASSUMED, standard).

6. **NUMERICAL (N3) — the threshold versus the range.** This is the table in §1(b1).

7. **NUMERICAL (N4) and PROVED (N4b) — arrays.**
   - **Upper bound.** `cap(A) = Σ_{y∈A} e_A(y)`, and escaping `A` implies escaping `{y}`, so `e_A(y) ≤ c₁` and `cap(A) ≤ |A|c₁`.
   - **Lower bound.** For positive definite `G_A`, `1/cap = min{μᵀG_Aμ : 1ᵀμ = 1}` by Lagrange multipliers. The uniform
     measure gives `cap ≥ |A|²/Σ_ij G_ij = 1/(G(0)/N³ + ⟨G⟩_off)`, and massless `⟨G⟩_off` is of order `1/(Nd)`.
   - check.py confirms both bounds on all computed arrays. The lower bound is attained at `N = 2`, where every record is
     equivalent.

8. **NUMERICAL (N5) — κ.**
   - `cap(solid cube of side D)` for `D = 1..12` has increments rising monotonically to `1.3765`.
   - The fit `κD + b + c/D` on `D = 8..12` gives `κ = 1.3812`.

9. **NUMERICAL (N6) — `D*`.** `1/(1 + (N/N*)²)` with `N* = √(κd/c₁)` matches the array ratios to 0.021, 0.029 and 0.037 at
   `d = 2, 4, 8`. It is the series combination of the additive strength `N³c₁` and the conductor strength `κNd`, which
   cross at `N*`.

10. **NUMERICAL (N7) — screened arrays.** The lattice sums `S(d, m)` are truncated at 20 ranges, and the omitted terms are
    below `10⁻⁶` of `S`. The bulk equilibrium charge of an infinite periodic array is `1/(G(0)(1 + S))`: a finite
    renormalization, with no growth of the shielding with size.

## 3. Where the route stops

- **The infinite-lattice values are floating point.** They are validated to about `10⁻⁸` against three independent exact
  facts, and every claimed inequality clears that margin by at least `10⁻⁴`. They are not Fraction-exact, which is impossible
  for the massless lattice, since `G(0)` is Watson's transcendental constant. The only Fraction computation is the torus
  anchor (E2).
- **κ is an extrapolation** from `D ≤ 12`. Its agreement with the continuum `1.3838` is a consistency check, not a proof.
- **The `D*` law is a fit**, bracketed by the proved bounds of step 7. The lower bound's constant, from a uniform charge, is
  smaller than the one the true equilibrium gives, so it proves the shape, not the constant.
- **(a) is not addressed.**

## 4. What would finish it

1. **An exact lower bound on the capacity of the massless array** by a better test measure (charge raised on the surface).
   This would prove `D*` with a constant.
2. **κ to more digits**, by larger cubes or Richardson extrapolation, and a proof of linear growth. The upper bound
   `cap(cube) ≤ cap(ball)`, with a Dirichlet test function, would do it.
3. **The gravity lane's question**, sharpened by this attempt: an additive source needs either a screened lean, which has no
   `1/r` field, or bodies smaller than `D* = 1.447 d^{3/2}`. A register decision is not a derivation.
4. **A referee from another model family.**

## 5. Running it

```
python3 probes/work/derive/odds-field-additive-sources/w-jonathonsmac4f50-j0faf/check.py
```

It needs `numpy`, `scipy` and `sympy`. It runs 10 checks (E1, E2, N1–N7, N4b) in about 30 seconds.
