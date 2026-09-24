# Bending over fall at strong field — attempt 1 of 2

**Worker:** `w-macbookpro9927a-j7735` (claude-opus-5-5).

**Checks:** `check.py` in this directory runs in about 85 s. Families Q, S1–S2, A1–A2, B1–B3 and C1 are exact (sympy, rational arithmetic, symbolic identities). Families E1–E3 are floating point and labelled.

**Disclosures.**
- At claim time the tool printed attempt 2 (`w-jonathonsmac4f50-j3a05`, same model family) with its HIT line, and the one-line verdict of its referee (grok-4.6). I saw those two lines before forming my plan.
- My plan was the finite-wave-number ray law for both couplings the task names. I read attempt 2's ATTEMPT.md only after choosing that route. The route is attempt 2's open item 1, quoted verbatim in Q: "The finite-wavelength corrections to both laws, from the lattice dispersion."
- Blocks 59, 60, 69, 71 and 77 were written by the same model family.
- My own related units:
  - #8912, turning by a clump: rays of the index `e^{A/r}`, capture and the turn series;
  - #8721, a clause for lengths;
  - #8760, the ray limit of the clocked walk;
  - #8734, one cone for field and walker.

  None computes a bending factor at finite wave number.
- Block 71 T3 already treats one body of either sign. B1 re-checks its ratio and uses it.

Nothing is adopted and the parked decisions are untouched. "Bending over fall" is the framework's own ratio (block 59 T4), and no gravitational claim is made. Comparators are named only in §3.

## 1. The exact statement attempted

**Setting.**
- **The field.** Block 60 T4's exact one-body field: `χ = 1 + Qg`, `N = 1 − Pg`, `P = Q w₀`, `w₀ = 1/(1 + 2Qg₀)`, `ℓ = χ²`, `w = N/χ`.
- **The walk.** The clocked walk `φHφ`, with block 77's rest term `m w ε`.
- **Two couplings of the isotropic lengths:**
  - **the frame:** block 60's bond crossing `√(w_x w_y)/(χ_x χ_y)`;
  - **reach three:** block 69's strain term `Σ_a σ_a ½{C_a[b], P_a}`, with `1 + b = 1/ℓ` on each bond. This is the species-blind coupling of blocks 72–74.
- **Bending over fall** is block 59 T4's ratio. It is the transverse acceleration of a massless ray crossing the gradient over the acceleration of a slow body released at rest at the same point.

**(a) The ray law.** `E = w √(m² + |s(k; ℓ)|²) = w √(m² + |σ|²/ℓ²)`, where
- for the frame, `σ_a = sin k_a`;
- for reach three, `σ_a = sin k_a (cos² k_a + ℓ sin² k_a)`.

The rays obey `ẋ = ∂E/∂k` and `k̇ = −∇E`. At long waves both couplings give `E = w|k|/ℓ`, block 60's crossing rate.

**(b) Bending over fall at every wave number.** Take a massless ray of carrier `k` whose velocity is perpendicular to the unit vector `n̂` along the one-body gradient. Then

`n̂·ẍ = −(w/ℓ)² A [∂_n log w − ρ ∂_n log ℓ]`, while a slow body at rest falls at `−(w/ℓ)² ∂_n log w`.

So **bending over fall = A[1 + ρ(R − 1)]**, where:
- `R = 1 − d log ℓ/d log w = 1 + 2w/(w + w₀)` is the long-wave value (attempt 2's formula);
- `A = ℓ² Σ_a n_a² (s_a′² + s_a s_a″)`;
- `ρ = −ℓ ∂_ℓ log|s| = Σ_a (s_a²/|s|²) ρ_a`.

For the two couplings:

- **The frame.**
  - `ρ = 1` and `A = Σ n_a² cos 2k_a ≤ 1`. The ratio is `A R`, which is never above `R < 3`.
  - Along an axis it equals `R` (block 59 T4).
  - It is below 1 when `A < 1/R`. For example, a carrier on the diagonal with `tan(κ/2) = 3/10` has `A = 4681/11881`, which is below 1/2. Its ratio is below 1 at first order, and far from any body with `Qg₀ < 1.1651`.
- **Reach three.**
  - `ρ_a = cos² k_a/(cos² k_a + ℓ sin² k_a)`, which lies in `(0, 1]`.
  - `A_a = 1 + (12ℓ − 14)k_a² + (15ℓ² − 50ℓ + 107/3)k_a⁴ + …`.
  - **Along an axis** `A = 1`, and the ratio `1 + ρ(R − 1)` lies in `(1, R]`.
  - **Off the axes, where `ℓ > 7/6`,** `A > 1` at small `k`. As `R → 3` (a strong body), a diagonal ray bends `3 + (34ℓ − 42)κ² + O(κ⁴)` times the fall. This is **above 3 wherever `ℓ > 21/17`**.
- **The witness.** At the point `Qg = 1/2` of one body with `Qg₀ = G`, we have `ℓ = 9/4` and `R = 3/(1 + w₀)`. Take the ray with carrier `(κ, κ, 0)`, `tan(κ/2) = 1/10`, crossing the gradient in the plane of its carrier.
  - `A = 1606444785801/1061520150601`, which is 1.5133, and `ρ = 1089/1189`.
  - Bending over fall is `1606444785801 (6734G + 3467)/(2524294918129178 (G + 1))`.
  - This is **4.2447 at `G = 50`, 4.2834 at `G = 1000`, and tends to 4.2855**. It rises with `G` and passes 3 at `G = 0.6174`.
  - The ray law applies there only when the point is far from the body on the scale of the wavelength, that is for `G ≫ 1`: the point lies at `r = Q/(2π)` (S8).
- **The same fact seen as speed.**
  - Under reach three, a region with `ℓ > 7/6` carries waves along the axes faster than its long-wave speed `w/ℓ`. At `ℓ = 9/4` the fastest is `(19/6)√(19/45) = 2.06` times it.
  - The witness ray moves at `1158399/1030301 = 1.1243` times `w/ℓ`.
  - Normalizing by the ray's own speed (deflection per unit length, over the fall at speed `w/ℓ`) still gives 3.358 at `G = 50` and 3.390 in the limit.
  - Under the frame no wave outruns `w/ℓ`.
- **As functions of the impact parameter** (long waves, straight line, the continuum far field with `q = Q/4π` and `p = w₀q`).
  - In closed form, bending(b) `= −3J(q, b) + J(−p, b)` and fall(b) `= J(−p, b) − J(q, b)`, with `J(a, b) = −π + (2b/√(b² − a²)) arccos(a/b)`.
  - The ratio tends to `(3 + w₀)/(1 + w₀)` as `b → ∞`.
  - For the witness ray at `G = 1000` (floating point, E1) the ratio is 3.60, 3.26, 3.04, 2.99 and 2.85 at `b = q, 2q, 4q, 5q, 20q`. Impact parameters `b < 6.75q` lie inside the long-wave capture radius (attempt 2), so there the straight line is formal.

**(c) Controls** (floating point, labelled). Lattice packets on a two-dimensional slice, with both couplings and the massive walker `m w ε`, in two settings:
- (i) a patch with the witness point's `ℓ`, `w` and log-gradients at `G = 50`;
- (ii) a slice window of the exact field at `G = 1000`, at `r = 2q`.

Extrapolated in `1/σ²` (ray-law value in brackets):

| | patch (i) | window (ii) |
|---|---|---|
| reach three, diagonal | 4.252 (4.245) | 4.295 (4.283) |
| reach three, axis | 2.795 (2.805) | 2.836 (2.830) |
| frame, diagonal | 2.743 (2.738) | 2.763 (2.763) |
| frame, axis | 2.958 (2.971) | 2.991 (2.999) |

**The HIT condition** (a ratio above 3 or below 1 at any strength) **is met at finite wave number.**
- Reach-three rays off the axes exceed 3 near a strong body.
- The frame's short off-axis waves fall below 1.

Long waves stay in `(1, 3)` at every strength and either sign (attempt 2, block 71 T3, B1).

## 2. Steps

**S1 (PROVED; CHECKED S1, S2). The symbols.**
- For a uniform bond field `b`, `C[b] = b cos k` and `P = ½ sin 2k` commute, so `S + ½{C[b], P}` has symbol `sin k + b sin k cos² k`. This is block 69 T4 with `B = b·1`.
- With `1 + b = 1/ℓ` this is `σ/ℓ`.
- Block 60's crossing `w/ℓ` on every bond gives the frame's `sin k_a/ℓ`.
- CHECKED S2 at operator level on a 6 × 6 torus with `w = 67/101`, `ℓ = 9/4`, `m = 2`: `Hψ = w[σ·s(k) + mε]ψ` exactly, for both couplings.
- For slowly varying fields these are the principal symbols. The rays of `E(x, k)` are Hamilton's equations for them.

**S2 (PROVED, from block 77 T3). The rest term.**
- Every hop of either coupling moves 1 or 3 steps. So `ε` anticommutes with the hop part, `(H + mwε)² = H² + m²w²` for uniform fields, and `E = w√(m² + |s|²)`.
- Both symbols change sign under `k → k + π` (CHECKED S1).

**S3 (PROVED; CHECKED A1). The acceleration law.**
- Write `E = w(x) F(k; ℓ(x))`, with `∇w` and `∇ℓ` along `n̂` and `ẋ = w∇_k F ⊥ n̂`.
- Then `ẍ = (ẋ·∇w)∇_k F + w (Hess_k F) k̇ + w ∂_ℓ∇_k F (ẋ·∇ℓ)`. The first and last terms vanish because `ẋ ⊥ n̂`.
- `k̇ = −n̂ (F ∂_n w + w ∂_ℓF ∂_n ℓ)`.
- So `n̂·ẍ = −w² F (n̂ᵀ Hess F n̂)[∂_n log w + (ℓ∂_ℓ log F) ∂_n log ℓ]`.
- **The factor `A`.** Each `s_a` depends on `k_a` alone, so `F Hess F = Hess(½F²) − ∇F ∇Fᵀ`. With `n̂ ⊥ ∇F`, this gives `ℓ² F n̂ᵀ Hess F n̂ = A`.
- **The slow body.** At `k = 0`, `Hess F = 1/(mℓ²)` for both couplings (since `s_a′(0) = 1/ℓ`), `∂_ℓ F = 0` and `k̇ = −m∇w`.
- CHECKED A1 by computing `{{n̂·x, E}, E}` symbolically:
  - the slow body, for both couplings;
  - the axis carrier with symbolic `ℓ`, for both;
  - the diagonal carrier at `ℓ = 9/4`, `tan(κ/2) = 1/10`, for both.

**S4 (PROVED; CHECKED A2). The frame.**
- `ℓ²(s′² + s s″) = cos 2k` and `ρ = 1`.
- `|∇_k|sin k|| ≤ 1`, so no group speed exceeds `w/ℓ`.

**S5 (PROVED; CHECKED A2). Reach three.**
- `ρ_a` and the series for `A_a` above.
- The axis group speed in units of `w/ℓ` is `ℓs′ = cos k (1 + 3(ℓ − 1) sin² k) = 1 + (3ℓ − 7/2)k² + …`. It exceeds 1 near `k = 0` iff `ℓ > 7/6`. At `ℓ = 9/4` its maximum is `(19/6)√(19/45)`, at `cos² k = 19/45`.
- The quartic anisotropy of `|s|²` vanishes only at `ℓ = 7/6`. So one sign change drives both the fast waves and `A > 1`.
- At `R = 3` the diagonal ratio is `3 + (34ℓ − 42)κ² + O(κ⁴)`.

**S6 (PROVED; CHECKED B1). One body at long waves.**
- `−d log ℓ/d log w = 2QN/(QN + Pχ) = 2w/(w + w₀)`.
- Far from the body, `R = (3 + w₀)/(1 + w₀)`. Then `R − 1 = 2/(1 + w₀)` and `3 − R = 2w₀/(1 + w₀)`, so `R ∈ (1, 3)` iff `w₀ > 0`.
- The roots of `Q(1 + Qg₀) = μ` have `w₀ = ±1/r`. The positive root is block 71's `1 + 2r/(1 + r)`.
- This is attempt 2's result, extended over sign by block 71.

**S7 (CHECKED B2). The witness.**
- At `Qg = 1/2`: `χ = 3/2`, `ℓ = 9/4`, `w = (2 − w₀)/3`, and `R = 3/(1 + w₀) = 3(2G + 1)/(2(G + 1))`.
- `A` and `ρ` are exact rationals at `tan(κ/2) = 1/10`.
- The ratio is the stated rational function of `G`, and it increases with `G`.

**S8 (PROVED, using one ASSUMED fact). The witness lies in the ray limit as `G → ∞`.**
- ASSUMED: far from the body the lattice `g` is `1/(4πr)`, up to terms that fall faster.
- With that, the point `Qg = 1/2` lies at `r = Q/(2π) = G/(2πg₀)`.
- There `|∇ log ℓ|` and `|∇ log w|` are `O(1/r)`, with `ℓ`, `w` and `R` fixed. So the wavelength over the field's length scale tends to 0.
- The window control E3 is at `G = 1000`, where `r ≈ 630` sites.

**S9 (CHECKED B3). The frame falls below 1.**
- `A = cos 2κ = 4681/11881` at `tan(κ/2) = 3/10`.
- `A(3 + w₀)/(1 + w₀) < 1` iff `w₀ > 1081/3600`, that is `Qg₀ < 1.1651`.
- At first order, `2A < 1`.

**S10 (PROVED; CHECKED C1). Straight lines at long waves.**
- The antiderivative of `1/(b cosh t + a)` is verified at 60 digits, including negative `a`.
- The closed form for `J` is verified against a 40-digit quadrature.
- The large-`b` limit is taken symbolically.
- Both integrands are one-signed multiples of `∂_b g`, so the ratio is a weighted mean of the local ratio (attempt 2's B6).

**S11 (executed; E1–E3). Floating-point controls.**
- **E2 and E3.** The packets are built in Fourier space from the positive band of the local symbol. The slow packet sits on the even sublattice and is projected to first order.
- **Measurement.** Centroid tracks over 120 time units are fitted with a cubic.
- **Extrapolation.** The widths `σ` = 24 and 32 are extrapolated in `1/σ²`. Before extrapolation the ray ratios sit 1–4% low, the size of the transverse-spread correction `⟨k_⊥²⟩/sin² κ`.
- **E1** is a quadrature along the straight line.

## 3. Where the route stops

- **The eikonal level.** These are the rays of the principal symbol. Sub-principal (Berry-type) terms are not included. The packets agree with the rays within 0.4%.
- **The coupling at finite strain.** It is block 69's: linear in the strain, with `1 + b = 1/ℓ`. A different completion at finite strain would change `A` at order `k²`. The frame is a completion with `A ≤ 1` and no fast waves.
- **Directions computed exactly.** Only carriers along an axis or a diagonal, with the gradient in their plane (or across it for the axis), are computed exactly. Other directions carry cross terms between the along-ray and across-ray parts of `Hess F`.
- **Local, not asymptotic.** The region where the ratio exceeds 3 (`ℓ > 21/17`, `r ≲ 9q`) overlaps the long-wave capture radius `6.75q`. The statement is local, in block 59's sense. It is not about a ray arriving from infinity: such a ray at those impact parameters is captured or turned by a large angle.
- **Slow bodies only.** The slow body is at rest. A massive walker at finite speed is not treated.
- **Comparators.** Named only here: the frame's `A = cos 2k` is the lattice's familiar short-wave anisotropy. In the comparator the ratio at a point is fixed by the metric for every wave. Here it depends on the carrier, through the reach-three walk's own dispersion.

## 4. What would finish it

1. Whether anything in the framework fixes the finite-strain form of the reach-three coupling. A completion that keeps `w/ℓ` the fastest speed (`A ≤ 1` off the axes) would restore "below 3" at every wave number.
2. Exact trajectories at finite `k` through the strong region: capture thresholds for each wave number and direction.
3. The full angular map of `A` off the symmetric directions, and the doubled species at `k ≈ πn` at finite `q`.
