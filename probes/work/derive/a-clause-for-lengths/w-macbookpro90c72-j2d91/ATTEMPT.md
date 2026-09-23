# J:derive:a-clause-for-lengths:a2 — the length exponent fixes the comparator's whole first-order law; one walker with a staggered rest energy reads it as a slope; block 62's frame can carry it

**Provenance.**
- Worker `w-macbookpro90c72-j2d91`, model `claude-opus-5-5`, one session.
- The claim printed one prior attempt: a1, `w-jonathonsmac4f50-jbfce`, `claude-opus-5-5`. It is the same model family, on another machine, and unrefereed.
- a1 cites block 59 (PR #8581: same family, unrefereed), which I read after forming my plan: Hamilton's equations for the family, the weak-field coefficients, scale covariance of bond rates, and a test with a rest energy.
- **Already there.**
  - a1:
    - the exact lattice ray law;
    - the two limits;
    - the exclusion, by scale covariance, of a factor 2 from bond rates built out of site rates;
    - an executed bending ratio of 1.934 for massless packets.
  - Block 59:
    - T1: a walker with no rest energy cannot tell site rates from lengths;
    - T4: the two limits;
    - T5: lengths need a law, with a free exponent `β`;
    - executed: 1.966 for massless packets, and 1.02 for a slow body on a line.
- **New here.**
  - (i) The full first-order law of the family, compared with the comparator's full law at every speed.
  - (ii) A single-walker, `κ`-free test, using block 77's staggered rest energy: the operator identity that makes it exact, and an execution.
  - (iii) Block 62's frame as the local object that can carry `b`.
  - (iv) The power-mean bond rate, as the exact form of the second-order candidate.
- Nothing is adopted and no gravitational claim is made; the comparator is a comparator.

## 1. The statement attempted

**Objects (supplied, blocks 53–54).** Site rates `w_x = e^{u_x}`, and block 54's walk `H = Σ_j σ_j D_j`, symbol `Σ_j σ_j sin k_j`.

**The family (task (a)).**
- **Continuum.** `E = a(x)√(m² + b(x)²|k|²)`.
- **Lattice.** `E² = a²m² + c²Σ_j sin²k_j`, with `c = ab`: `a` times the rest energy, `c` times the hops.
- **The weak field.** `a = w^α`, `b = w^β`, with `w = 1` at the point considered.

**Claims.**
- **(a) Exact.**
  - **The law at every speed and direction.** Hamilton's equations for the continuum family give

    `dv/dt = 2(v·∇log ab) v − a²b²∇log a − |v|²∇log b`.
  - **Slow bodies.** `−a²b²∇log a`, i.e. `−α∇u`.
  - **Transverse rays at the limiting speed** `|v| = ab`. `−(ab)²∇_⊥log(ab)`, i.e. `−(α + β)∇u`.
  - **The weak-field law.** `dv/dt = −α∇u − β|v|²∇u + 2(α + β)(v·∇u)v`.
  - **Against the comparator.** Its full first-order law is `−(1 + |v|²)∇u + 4(v·∇u)v`. The family's law equals it **for every `v`** iff `α = β = 1`. The exponent that doubles the bending (`β = 1`) also supplies the comparator's `|v|²` term and its longitudinal `4(v·∇u)v` term; nothing further is to be fixed.
- **(b) The candidates for `b`.**
  1. **A bond rate distinct from the site rate.** Allowed as a supplied field; not forced. This agrees with a1 and block 59.
  2. **Block 53's scale covariance applied to bond rates built from the endpoint site rates.** It forces degree-one homogeneity, hence `b = 1`: excluded as a source of the factor 2 (agrees with a1 and block 59 T5(a)).
  3. **The second-order term of block 53's law.** A bond rate set by that kind of rule is a power mean, `M_p(w_x, w_y) = √(w_x w_y)(1 + p d²/8 + O(d⁴))`, with `d = u_y − u_x`. It is degree one, and differs from the product form only at second order in the rate difference across the bond. Excluded at the order at which bending is measured. (Exact.)
  4. **Block 62's frame (new candidate).** `H[E] = ½Σ_j{E^j·σ, S_j}` with an isotropic frame `E^j = b e_j` gives `H[b·1] = bH`: an object in the framework's vocabulary that times hops and not sites. It is a pure number per bond direction, not a rate, so block 53's premise neither excludes it nor fixes it. Its isotropic part is the family's `b`. Whether the frame's own law (blocks 62–74) ties it to `w¹` is what would decide the factor 2.
- **(c) The executed test.**
  - **Why a massless walker is not enough.** By block 59 T1, a walker with no rest energy sees only bond rates. For it, hops timed by `w^{1+β}` are block 54's walk in the field `(1 + β)u`, and block 53 leaves `κ` free. Comparing massless packets under the two clauses therefore needs `u` known independently.
  - **The `κ`-free test.** Use one walker with block 77's staggered rest energy timed by the site rate.
    - Exact identity: `(w m ε + c H_hop)² = w²m² + c²H_hop²` for uniform rates, so `E² = a²m² + c²Σ sin²k`.
    - A packet crossing a uniform gradient `g` bends at `−c²g(1 + βh)`, where `h = c²S/E²` is its hop share.
    - Bending against `h` is a straight line: its intercept (the slow fall) measures the site-rate coupling, and its slope measures `β`.
  - **Executed in 2D.** At `m = 0.6`, width 12:
    - `β = 0`: intercept `0.993`, slope `−0.013`;
    - `β = 1`: intercept `1.003`, slope `0.929`;
    - the ray values are `(1, 0)` and `(1, 1)`.

## 2. Steps

**S1 (PROVED; CHECKED A.law). The continuum law.**
- **Set-up.** Write `E = aΓ` with `Γ = √(m² + b²|k|²)`. Then `v = ab²k/Γ` and `k̇ = −Γ∇a − ab|k|²∇b/Γ`.
- **Energy conservation.** Along a ray `Γ̇/Γ = −v·∇log a`.
- **Differentiating `v`.**

  `dv/dt = v[v·∇log(ab²) − Γ̇/Γ] + (ab²/Γ)k̇ = v(v·∇log(a²b²)) − ab²∇a − a²b³|k|²∇b/Γ²`.

  Since `|v|² = a²b⁴|k|²/Γ²`, the last term is `|v|²∇log b`.
- **CHECKED.** Exactly, from sympy derivatives of concrete `a(x), b(x)` (linear and quadratic, at the origin and off it), at four Pythagorean points (`Γ = 5, 13, 17, 29`) along the rational unit vectors `(1,2,2)/3` and `(2,3,6)/7`.

**S2 (PROVED; CHECKED A.comparator). The weak field and the comparator.**
- With `∇log a = α∇u`, `∇log b = β∇u` and `ab = 1` at the point, S1 gives `−α∇u − β|v|²∇u + 2(α + β)(v·∇u)v`.
- Equating it with `−(1 + |v|²)∇u + 4(v·∇u)v`:
  - the `v⁰` coefficient gives `α = 1`;
  - the `|v|²` coefficient gives `β = 1`;
  - then the longitudinal coefficient `2(α + β) = 4` holds.

  So `α = β = 1` is the unique solution. CHECKED with sympy.

**S3 (PROVED as in a1; CHECKED B.hopshare, independently). The lattice law.**
- For `E² = a²m² + c²S`, `S = Σ sin²k_j`:

  `dv_j/dt = −c²cos(2k_j)[a²m²∂_j log a + c²S∂_j log c]/E² + 2v_j(v·∇log c)`.
- CHECKED from sympy derivatives at three points with rational sines and cosines and rational `E` (`5/4, 5/4, 1`).
- **Crossing a gradient.** For motion across a gradient (`k_x = 0`, `v_x = 0`) with `a = w`, `c = w^{1+β}` and `w = 1` at the packet, `dv_x/dt = −g(m² + (1 + β)S)/E² = −g(1 + βh)`.

**S4 (PROVED; CHECKED B.rest). Block 77's staggered rest energy gives the lattice family exactly.**
- `ε = (−1)^{x+y+z}` anticommutes with every nearest-neighbour hop (a hop joins opposite sublattices), and `ε² = 1`.
- `H_hop² = Σ_j D_j²`, because the `D_j` commute and the `σ_j` anticommute.
- So, for uniform `a, c`, `(a m ε + c H_hop)² = a²m² + c²H_hop²`: the dispersion is `E² = a²m² + c²Σ sin²k`.
- CHECKED with integer matrices on the `4³` torus.
- **The rest states.** The rest states (`k = 0`) live on one sublattice. That is what a slow packet is, and it is why block 54's walk alone (which has no 2×2 mass matrix) cannot supply the slow side of the test.

**S5 (PROVED; CHECKED B.frame). Block 62's frame as `b`.**
- `(E^j·σ) = bσ_j` for `E^j = b e_j`, and `{bσ_j, S_j}/2 = bσ_jS_j`, so `H[b·1] = bH`.
- Clocked as in block 54, the hops then carry `b√(w_x w_y)`: `c = bw`, `a = w`.
- The frame is dimensionless (a length ratio per direction), so rescaling all rates leaves it unchanged. This is consistent with block 53's premise, and the premise does not fix it (compare block 59 T5(a), which concerns lengths built from rates).

**S6 (PROVED; CHECKED B.powermean). The second-order candidate.**
- Block 53's rule is a power mean of neighbour rates. Applied to a bond's two endpoints it gives `M_p = √(w_x w_y) cosh(pd/2)^{1/p} = √(w_x w_y)(1 + pd²/8 + O(d⁴))` (sympy series).
- It is homogeneous of degree one, so `b = 1 + O((Δu)²)`. It cannot change the first-order bending.

**S7 (executed; notes). The single-walker test in 2D.**
- **Set-up.**
  - Lattice `112 × 96`, open along the gradient and periodic across it.
  - Block 54's 2D walk (`σ₁D₁ + σ₂D₂`) with the staggered rest energy `m ε w_x`, `m = 0.6`, and hops `(w_x w_y)^{(1+β)/2}`.
  - `u = g(x − x_c)`, `g = ±0.004`.
  - Gaussian packets of width 12 in the positive band (the eigenvector of the doubled symbol), at `k_y = 0, 0.5, 1, π/2`.
  - Evolution with `expm_multiply` to `T = 30`, keeping the part of the displacement that is odd in `g`.
- **Bending over `gT²/2`:**

  | `h` | `β = 0` | `β = 1` | rays `(β = 0, β = 1)` |
  |---|---|---|---|
  | 0.000 | 0.9949 | 1.0011 | `1, 1` |
  | 0.390 | 0.9842 | 1.3690 | `1, 1.390` |
  | 0.663 | 0.9859 | 1.6216 | `1, 1.663` |
  | 0.735 | 0.9850 | 1.6816 | `1, 1.735` |

- **Fits.** `β = 0`: intercept `0.993`, slope `−0.013`. `β = 1`: intercept `1.003`, slope `0.929`.
- **Width matters.** At width 5 with `m = 0.3`, the slow packet falls only `0.81` of the ray value (the Compton length `1/m` is comparable to the width). The ratio approaches the ray value as the width grows: `0.927` at width 8, `0.988` at width 12.

**ASSUMED.**
- The ray (geometric-optics) description of packets, used only to interpret S7. The executed numbers show its accuracy at the stated widths.
- The comparator's first-order law in isotropic form, `−(1 + |v|²)∇Φ + 4(v·∇Φ)v`, quoted as the comparator (not derived).

## 3. The first failing step

None for (a) and (c) as posed. For (b), no candidate is forced:
- the factor 2 needs a supplied object whose law ties it to the depth of the rate: an independent bond field (block 59 T5(b)), or block 62's frame;
- scale covariance of bond rates built from site rates excludes it.

## 4. What would finish it

1. **Block 62's frame.** Do its field equations, as developed in blocks 62–74 (the relabelling identity balanced against `e∇u`, blocks 66 and 74), fix the frame's isotropic part as `w^β` for a definite `β`, and is `β = 1`? That is the one place where the framework's own vocabulary might force the factor 2.
2. **The test in three dimensions.** Run S7 in 3D, where block 54 found a sideways drift along `(gradient) × (motion)`. The bending lies in the plane of the gradient and the motion, so the drift does not enter it, but the geometry should be executed.
3. **A rigorous packet bound.** Bound the wave corrections to the ray law at finite width, i.e. the `0.81 → 0.99` convergence, to turn S7 into a proof at first order in `g`.

## 5. Running it

```
python3 probes/work/derive/a-clause-for-lengths/w-macbookpro90c72-j2d91/check.py
```

The run takes about 4 s. It makes six exact checks:
- sympy derivatives evaluated at Pythagorean points;
- integer matrices on a torus;
- sympy series.

The two `note` lines are the executed 2D test, in floating point.
