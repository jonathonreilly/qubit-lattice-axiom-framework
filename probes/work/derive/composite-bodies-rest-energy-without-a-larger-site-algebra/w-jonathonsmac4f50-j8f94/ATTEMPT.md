# composite-bodies-rest-energy-without-a-larger-site-algebra, attempt a3: binding gives a rest energy; the fall is not universal

**Provenance.** Written by Claude Opus 5.5 (`claude-opus-5-5`), worker `w-jonathonsmac4f50-j8f94`, task
`J:derive:composite-bodies-rest-energy-without-a-larger-site-algebra:a3`. There were no prior attempts at claim time. Blocks 53
and 54, which supply the setting, were supervisor-run in the same model family. This is not independent of them. Parked entry 4
of `docs/repo/DEFERRED_DECISIONS.md` is neither touched nor raised.

## 1. What is claimed

**Setting.** This is block 54 (open PR "ail54"; supplied clause, not adopted).
- `(T_eψ)(x) = ψ(x − e)`, and `D_j = (i/2)(T_j − T_j†)` has symbol `sin k_j`.
- One walker is `H₁ = σ_z D` on `Z`, or `Σ_j σ_j D_j` on `Z³`.
- Two distinguishable walkers have `H = H₁⊗1 + 1⊗H₁ + interaction`. The interaction is either contact, `V δ_{x₁x₂}`, or nearest
  neighbour, `V_n(δ_{x₁,x₂+1} + δ_{x₁,x₂−1})`.
- Under the clause each walker's term is `√W H₁ √W`.
  - **Timed interaction:** the interaction term is multiplied by a degree-one weight of the rate field at its sites: `w(x)` for
    contact, `√(w(x₁)w(x₂))` for a bond.
  - **Untimed interaction:** it is left as it is.

**(a) Bound states and their energy functions.**

*One dimension, contact.* `σ_z` is diagonal, so there are four spin sectors. For every `V < 0` there is exactly one bound state
per sector and `K`:
- co-moving walkers (`s₁ = s₂`): `E = −√(V² + 4 sin²(K/2))`. This gives `E² = V² + K² − K⁴/12 + …`, a rest energy
  **`M = |V|` and `c = 1`, the single walker's limiting speed**;
- counter-moving walkers: `E = −√(V² + 4 cos²(K/2))`. At `K = 0` this is `E² = (V² + 4) − K²`, a band **minimum**. It is
  relativistic, with `c = 1`, only about `K = π`.

*One dimension, nearest neighbour.* Co-moving walkers bind at `K = 0` in two channels at `E = V_n`:
- the even channel has `E² = V_n² + 6 sin²(K/2)`, so `c² = 3/2`;
- the odd channel has `E² = V_n² + 2 sin²(K/2)`, so `c² = 1/2`.

Both forms are relativistic, **neither with the walker's `c`**, and neither depends on `V_n`.

*Three dimensions, contact* (numerical). The ground pair lies below the two-walker continuum, whose edge is at `−2√3`. At
`K = 0` it has `E² = M² − c*²K²`, isotropic, with `c*² = 0.81` at `V = −5` and `0.90` at `V = −8`. This is a band
**minimum**: the inverted form.

**(b) The fall.**
- **Exact identity.** With the interaction timed, the two-walker generator satisfies `H_w T_a = λ_a T_a H_w` for the joint
  translation in a uniform gradient. So block 54's "force = −(energy) × grad u" holds exactly, binding energy included:
  `d⟨K⟩/dt = −g⟨H_w⟩`.
- **Fall at rest.** At the ray level, a composite at rest at a band extremum accelerates at
  **`a = −w² ∂²_K(ε²/2)|_rest ∇u`**. That gives:

| composite | acceleration at rest |
|---|---|
| 1D co-moving contact pair | `−g`, for every `V` (the task's expectation) |
| 1D counter-moving contact pair | `+g`: falls **up**, away from slow clocks |
| 1D nearest-neighbour pairs | `−(3/2)g` (even channel) and `−(1/2)g` (odd channel) |
| 3D contact ground pair | `+0.81g` to `+0.90g`: falls up |

- **Untimed interaction.** The identity fails, and only the kinetic energy is pulled: `d⟨K⟩/dt = −g⟨H_kin⟩`. The 1D co-moving
  contact pair at `K = 0` has zero kinetic energy exactly, so at rest it **does not fall**.
- **Executed.** Propagations on a 130-site chain agree with ray clouds of each composite's own dispersion to within 0.02:

| composite | executed `a/g` |
|---|---|
| co-moving contact, timed | −1.0007 (`V = −1`), −0.9742 (`V = −3`) |
| co-moving contact, untimed | −0.0034 |
| counter-moving contact, timed | +1.0092 |
| nearest neighbour, even channel | −1.4384 |
| nearest neighbour, odd channel | −0.4928 |

**(c) What this does to "rest energy needs a larger site algebra".**
- **Rest energy.** Binding supplies a rest energy inside `M₂(ℂ)` per walker. The co-moving contact pair has `M = |V|` with the
  walker's `c`, and with a timed interaction it falls exactly like everything else. So the one-walker obstruction (nothing in
  `M₂(ℂ)` anticommutes with the content matrices) does not prevent composite bodies from having a rest energy.
- **What it costs.** Universal free fall of composites is **not** automatic:
  - it needs an interaction clause, which is not in the axioms;
  - it needs that interaction timed by the local clock, since an untimed binding energy does not gravitate;
  - even then it holds only for composites whose dispersion has `∂²(ε²/2) = 1` at rest. That holds for the co-moving contact
    pair in 1D; the counter-moving pair, the nearest-neighbour pairs and the 3D contact ground pair all fall at other
    accelerations, and some of them upward.

## 2. Steps

1. **ASSUMED — the setting.** Block 54's objects and clause, and the two interactions, are supplied. The walkers are
   distinguishable. Symmetrized pairs are the sectors' symmetric combinations and are not treated separately.

2. **PROVED / CHECKED (A1) — the four sectors.** `σ_z` commutes with everything in the 1D problem. In sector `(s₁, s₂)` the
   kinetic energy is `s₁ sin(K/2 + q) + s₂ sin(K/2 − q)`, which is `2 sin(K/2) cos q` or `2 cos(K/2) sin q` (checked with
   sympy).

3. **PROVED / CHECKED (A2) — contact bound states.**
   - A contact term couples all `q` equally, so a bound state is `φ(q) ∝ 1/(E − ε(q))` with
     `1 = V (1/2π)∫dq/(E − ε(q))`.
   - **Lemma.** For `a > 2|b|`, `(1/2π)∫₀^{2π} dq/(a − 2b cos q) = 1/√(a² − 4b²)`. Put `z = e^{iq}`: the integral becomes
     `(1/i)∮ −dz/(bz² − az + b)`, with one root `z₋ = (a − √(a² − 4b²))/(2b)` inside the unit circle. Its residue gives
     `2π/(b(z₊ − z₋)) = 2π/√(a² − 4b²)`. The
     case `a < −2|b|` follows by the sign. (checked with mpmath to `10⁻³⁰`)
   - Hence `E² = V² + 4b²`, with `b = sin(K/2)` (co-moving) or `cos(K/2)` (counter-moving), and the series in §1.

4. **CHECKED (A3) — exact diagonalization.**
   - On a 12-ring, the position-space generator's spectrum equals the union of the `K`-blocks to `10⁻¹⁴`.
   - On a 200-ring, the lowest state of every `K`-block matches the closed forms to `10⁻¹⁴` in both sectors.

5. **PROVED (to `O(b²)`) / CHECKED (A4) — nearest neighbour.**
   - The kernel `V_n·2cos(q − q')` is `V_n(2cos q cos q' + 2 sin q sin q')`, which is separable, with channels `cos q` and
     `sin q`.
   - Expanding `1/(E − 2b cos q)` to `b²` gives the channel conditions `1 = V_n(1 + 3b²/E²)/E` and `1 = V_n(1 + b²/E²)/E`
     (sympy).
   - Hence `E² = V_n² + 6b² + O(b⁴)` and `V_n² + 2b² + O(b⁴)`.
   - A 400-ring gives `c² = 1.4998` and `0.5000`, independent of `V_n`.

6. **NUMERICAL (A5) — three dimensions.**
   - **Method.** A bound state solves `det(1 − V G(E,K)) = 0`, where `G = N⁻³Σ_k (E − A(k))⁻¹` and
     `A = h(k)·σ⊗1 + 1⊗h(K − k)·σ`. `G` is assembled from the projectors `(1 ± n̂·σ)/2`.
   - **Cross-checks.** The solver agrees with full diagonalization of `K`-blocks on `6³` to `5·10⁻¹⁵`. The `24³` and `32³`
     grids agree to all digits shown.
   - **Result.** The curvature of `E²` at `K = 0` is the same along axes, face diagonals and body diagonals, to `0.002`.

7. **PROVED / CHECKED (B1) — the exact identity.**
   - In a uniform gradient `w = e^{gx}`, `√W T_a = λ_a^{1/2} T_a √W` (block 54), and the joint translation commutes with each
     `D` and with `δ`.
   - Each timed term is a degree-one weight times a translation-invariant operator, so `H_w T_a = λ_a T_a H_w`.
   - Then block 54's argument gives `T_a(t) = T_a exp(i(λ_a − 1)H_w t)`, i.e. `d⟨K⟩/dt = −g⟨H_w⟩`.
   - Untimed, `H T_a = T_a(λ_a H_kin + V δ)`.
   - Checked entrywise on the interior of a 14-chain: `4·10⁻¹⁶` timed, `0.35` untimed.

8. **PROVED at ray level (ASSUMED: the ray limit, as in block 54) / EXECUTED (B2) — the fall at rest.**
   - With `E(X,K) = w(X)ε(K)`:
     - `dK/dt = −g w ε`;
     - `dX/dt = w ε'`;
     - so `d²X/dt² = −g w² εε'' + g w² ε'²`.
   - At a band extremum `ε' = 0`, so `a = −g w² ∂²_K(ε²/2)`.
   - Untimed, `E = −√(V² + 4w² sin²(K/2))`, and at `K = 0` it has no `X` dependence.
   - The executed runs are in §1(b). The ray clouds integrate the ray equations over the packet's `K` spread
     (Gauss–Hermite, 21 nodes) and are fitted like the propagations.

## 3. Where the route stops

- **3D is numerical and contact-only.** The 3D statement rests on the secular equation, which is cross-checked against full
  diagonalization. The 3D nearest-neighbour case is not done. The 3D excited bound bands are not mapped beyond the
  high-symmetry points (0 and M are minima; X and R are saddles).
- **The ray limit is ASSUMED**, as in block 54. Only the stated executed numbers are claimed.
- **Timing weights.** "Timed" is any degree-one weight. Different weights (`√(w₁w₂)` or `(w₁ + w₂)/2`) differ at `O(g²)` and
  do not change the at-rest law.
- **Identical walkers** (symmetrized sectors) are not treated separately.

## 4. What would finish it

1. **Which composites fall like everything else.** Characterize the composites with `∂²_K(ε²/2) = 1` at rest. A plausible
   route is a two-body analogue of the single walker's ray matrix: the co-moving contact pair is the walker's own dispersion
   lifted to the pair.
2. **3D beyond contact.** Do nearest-neighbour binding in 3D, and search for a 3D bound band with a relativistic maximum with
   `c = 1`.
3. **What the three findings do to the gravity lane.** The owner, or the lane, should read them together:
   - a composite's fall depends on its internal state;
   - counter-moving pairs fall up;
   - untimed binding energy does not gravitate.
4. **A referee from another model family.**

## 5. Running it

```
python3 probes/work/derive/composite-bodies-rest-energy-without-a-larger-site-algebra/w-jonathonsmac4f50-j8f94/check.py
```

It needs `numpy`, `scipy`, `sympy` and `mpmath`. It runs 7 checks (A1–A5, B1, B2) in about 15 seconds.
