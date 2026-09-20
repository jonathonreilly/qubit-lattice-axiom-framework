# lightcone-uniqueness-region: derivation attempt 1 of 3

Worker `w-jonathonsmac4f50-j715c` (claude-opus-5), unit `J-derive-lightcone-uniqueness-region-a1`.

**Provenance, stated because it bears on independence.** The only prior attempt on this problem,
`a2` (`w-jonathonsmac4f50-j246a`), was written by the same model family, on the same machine, by
the same running worker. It is not an independent predecessor of this attempt. I formed the plan
below — bound the parallel influence by exhibiting a transport plan rather than by relaxing the
Lipschitz constraints — before reading `a2`, and the route, the closed form, the certificate and
the constant `8/135` are not in `a2`. What I take from `a2` is only the statement of its open
step (its S7, the directional lemma) and its numerical LP values, which I use once, as a
cross-check of my own cost function (S6). A referee should discount any agreement between this
attempt and `a2` accordingly.

**The object.** `probes/lib/formation_levelplane.py`, dim `3s`, sphere menu: the record at level
`t+1` and site `x ∈ Z³` is drawn from `μ_{βS_x}`, `S_x` the sum of the 7 records at `(t, x)` and
`(t, x ± e_j)`. `μ_V` has density `e^{V·s}/Z(|V|)` on `S²`; `A(κ) = coth κ − 1/κ`; `κ = |V|`.

**Metric.** `S²` carries the chordal metric `|s − s'|`; "Lip" is 1-Lipschitz for it. `W1` is the
dual form `sup_{f Lip}(E_μ f − E_ν f)`; no duality theorem is used — every upper bound below comes
from an explicit coupling, every lower bound from an explicit `f`.

**The influence.** For a unit `u`, `‖D_u(V)‖ := sup_{f Lip} Cov_V(f, u·s)`, the derivative of
`V ↦ E_V f`. The GIVEN of this unit is that this, and not the covariance `Cov(s_i, s_j)`, is the
Dobrushin influence; the perpendicular case is `A(κ)/κ` and the parallel case was open.

## 1. The statement attempted

**(a)** `‖D_u(V)‖` for `u ∥ V` — the case left open. I bound it by the cost of an explicit
transport plan and give that cost in closed form:

> `‖D_∥(κ)‖ ≤ Φ(κ) := c(κ) ∫_0^{ζ₁} |s(z_+(ζ)) − s(z_−(ζ))| e^ζ ζ dζ`,
> `c(κ) = e^{κA}/(2κ sinh κ)`, `ζ₁ = κ(1 − A)`, `z_± = A + ζ_±/κ`,
> and `ζ_−` is the partner of `ζ_+` under `ω(ζ_−) = ω(ζ_+)`, `ω(x) = e^x(x − 1) + 1`.

with `Φ(0) = 1/3`, `Φ(κ) = 1/3 − (8/135)κ² + O(κ⁴)`, and `Φ(κ) < A(κ)/κ` at 14 certified `κ`.

**(b)** The regions: W1 gives `β < 3/7 = 0.428571…` once the directional lemma is complete,
TV gives `β < √3/7 = 0.247436…`; W1 is the larger. (b) is answered in S7.

**(c)** The comparison with the executed onset, read out of this branch's own scan logs
rather than quoted: S8.

## 2. Steps

**S1 (PROVED). The influence in the parallel direction is a one-dimensional transport problem.**
- Take `V = κe₃`. For Lip `f` let `F(z)` be its average over the azimuth at height `z`. The law of
  `z = s₃` under `μ_V` has density `q(z) = κe^{κz}/(2 sinh κ)` on `[−1,1]`, and `μ_V` is invariant
  under rotations about `e₃`, so `Cov_V(f, s₃) = Cov(F, z)`.
- Two points at the same azimuth and heights `z, z'` are `chord(z,z') = |s(θ)−s(θ')|` apart, so
  averaging a Lip `f` over the azimuth gives `|F(z) − F(z')| ≤ chord(z,z')`.
- `Cov(F,z) = ∫F dμ⁺ − ∫F dμ⁻` where `μ^±` are the positive and negative parts of the signed
  density `(z − A)q(z)`. They have equal mass, because `A` is the mean of `z`.
- Hence for **every** coupling `π` of `μ⁺` with `μ⁻`, `Cov(F,z) ≤ ∫ chord dπ`. Any plan is an
  upper bound; no optimality claim is needed.

**S2 (PROVED; CHECKED `C1`). The mass function and the partner equation.**
- `M(z) := ∫_z^1 (t − A)q(t)dt = [e^κ(1−A−1/κ) − e^{κz}(z−A−1/κ)]/(2 sinh κ)`, verified by
  differentiating (`M' = −(z−A)q`) and by `M(1) = 0`.
- `M(−1) = 0` **forces** `A = coth κ − 1/κ` and nothing else: that is what makes `μ⁺`, `μ⁻` balance.
- The identity that organises everything:
  **`M(z) = M_max − c(κ) ω(κ(z − A))`, `ω(x) = e^x(x−1)+1`, `c = e^{κA}/(2κ sinh κ)`,**
  with `M_max = c ω(κ(1−A))`. Since `ω'(x) = x e^x`, `ω` decreases on `x<0` and increases on `x>0`,
  so each level of `M` is met exactly twice, at `z_− < A < z_+`.
- **The pairing is `κ`-free in `ζ = κ(z − A)`**: `z_−` is the partner of `z_+` iff
  `ω(ζ_−) = ω(ζ_+)`. All the `κ`-dependence of the plan sits in the two maps `z = A + ζ/κ` and in
  the weight.

**S3 (PROVED). The antitone plan, and `Φ`.**
- Pair each level of `M`: send the deficit below `z_−` to the excess above `z_+`. `M(z_−) = M(z_+)`
  says exactly that the two masses agree, so this is a coupling of `μ⁻` with `μ⁺`.
- Its cost is `∫_0^{M_max} chord dm`; with `m = M_max − cω(ζ)` this is the `Φ(κ)` of §1.
- By S1, `‖D_∥(κ)‖ ≤ Φ(κ)`.

**S4 (PROVED; CHECKED `C3`). `Φ(0) = 1/3`.**
- At `κ = 0`: `A = 0`, `M(z) = (1−z²)/4`, the partner of `z` is `−z`, `chord(z,−z) = 2z`, so
  `Φ(0) = ∫_0^{1/4} 2√(1−4m) dm = 1/3`, which is `A(κ)/κ` at `κ = 0`. The parallel and the
  perpendicular influence agree at `V = 0`, as they must by isotropy, and the plan is optimal there
  (`f = z` attains it).

**S5 (PROVED at the certified points; CHECKED `C4`). `Φ(κ) < A(κ)/κ`.**
- `chord` grows with `ζ_+`: as `z_+` rises its partner `z_−` falls, so the opening angle grows.
  Therefore taking the chord at a cell's upper end gives a Stieltjes **upper** sum, and cell masses
  are exact differences of `ω`. `check.py` evaluates that upper sum in rational interval arithmetic
  with outward rounding (`e^x` by a truncated series with an explicit tail, `ω` by Horner with an
  explicit tail, square roots by integer square roots), and compares it with a rational **lower**
  bound for `A(κ)/κ`.
- Result, with the margin `A/κ − Φ`:

  | κ | Φ ≤ | A/κ ≥ | margin |
  |---|---|---|---|
  | 1/10 | 0.33295205 | 0.33311132 | 1.59e-04 |
  | 1/4 | 0.33009063 | 0.33195266 | 1.86e-03 |
  | 1/2 | 0.31980793 | 0.32790683 | 8.10e-03 |
  | 1 | 0.28312758 | 0.31303529 | 2.99e-02 |
  | 2 | 0.19086395 | 0.26865736 | 7.78e-02 |
  | 3 | 0.12950809 | 0.22387883 | 9.44e-02 |

  (14 values of `κ` in `[1/10, 3]` in all; `κ ≤ 3` is the range that matters, since `κ ≤ 7β` and
  the target is `β < 3/7`.)
- **What this does not do:** it certifies the 14 points, not the intervals between them. See §3.

**S6 (CHECKED `C5`, numerical and labelled as such). The behaviour at the origin.**
- `Φ(κ) = 1/3 − (8/135)κ² + O(κ⁴)`, from mpmath quadrature at `κ = 1/20, 1/10` at 40 digits; the
  fitted coefficient is `0.0592592274` against `8/135 = 0.0592592593`.
- `A(κ)/κ = 1/3 − κ²/45 + O(κ⁴)`, and `8/135 − 1/45 = 1/27` exactly, so
  **`A(κ)/κ − Φ(κ) = κ²/27 + O(κ⁴)`**: the margin opens quadratically, and the inequality is
  strict on a punctured neighbourhood of `0`. Both sides are `1/3` at `κ = 0`, so no inequality
  with room can hold there; `κ²/27` is the whole of it.
- Cross-check against `a2`'s grid LPs (its N1, the only number I take from it): `a2` reports
  parallel optima `0.3297, 0.2825, 0.1896` at `κ = 0.25, 1, 2`. My `Φ` at those `κ` is
  `0.329665, 0.282117, 0.189619`. The plan's cost and `a2`'s LP optimum agree to 4 decimals, from
  two unrelated computations — `a2` also observed that its LP optimum is realised by a decreasing
  matching along meridians, which is this plan.

**S7 (PROVED; CHECKED `C6`, `C7`). What the parallel case buys, and the two regions.**
- `A(κ)/κ` is strictly decreasing, re-proved here rather than cited: `κA' − A < 0` reduces to
  `cosh x − 1 − x²/4 − (x/4)sinh x ≤ 0` at `x = 2κ`, whose Taylor coefficients are
  `(2−m)/(4m(2m−1)!)` — zero at `m = 1, 2` and negative after. With `A(κ)/κ → 1/3`, `A(κ)/κ ≤ 1/3`.
- **W1 region.** With the directional lemma complete, `L = sup_{|V|≤7β,|u|=1}‖D_u(V)‖ = 1/3`,
  attained at `V = 0`, and the sitewise Dobrushin sum is `7β/3 < 1`, i.e. `β < 3/7 = 0.428571…`.
- **TV region.** Block 27's `TV(μ_V, μ_{V'}) ≤ |V−V'|/(2√3)` is a distance, not a derivative, so
  the Dobrushin coefficient pays the full chordal diameter `2`: `c_j ≤ 2β/(2√3) = β/√3` and
  `7β/√3 < 1`, i.e. `β < √3/7 = 0.247436…`.
- **Which is larger: W1**, by the factor `3/√3 = √3 = 1.73`. The reason is structural and worth
  stating plainly: the W1 coefficient is a Lipschitz constant, so it is charged for the *arclength*
  a predecessor moves; the TV coefficient is charged for the *diameter* whatever the move.

**S8 (CHECKED `C7`, from the branch's own logs). The executed onset.**
- `check.py` parses `logs/probes/X:lightcone-threshold-fine/` and
  `logs/probes/X:formation-lightcone-sphere/` for the `dim=3` sphere runs and prints the plateau of
  `|m|`: `β = 0.3, 0.4, 0.5 → 0.0023, 0.0029, 0.0163 (L=32), 0.0078 (L=48), 0.0050 (L=64)`, then
  `β = 0.6 → 0.4146`, `0.65 → 0.5276 (L=32), 0.5214 (L=48)`, `0.7 → 0.5938`, rising to `0.9669` at
  `β = 6`. At `β = 0.5` the plateau falls as `L` grows; from `β = 0.65` it does not.
- So the onset lies between `β = 0.5` and `β = 0.6` in these logs — tighter than, and consistent
  with, the `0.6`–`0.75` window the unit's statement quotes.
- `3/7 = 0.4286` is a factor **1.17 to 1.40** below that onset. `a2`'s unconditional `3/10` is a
  factor 1.67 to 2.0 below; the TV region `√3/7` is a factor 2.0 to 2.4 below.

## 3. Where the route stops

The first thing that is not proved is **the interval statement in S5**. The certificate is a finite
set of points. Two ranges are open, for different reasons:

1. **Between the certified `κ`.** This needs a modulus of continuity for `Φ` in `κ` (or the
   monotonicity of `Φ`, which the values support and which I did not prove). Neither is in the
   attempt. A Lipschitz bound on `Φ` would close it mechanically, since the margins in S5 are
   3 to 5 orders of magnitude above the grid spacing's effect.
2. **`κ < 1/10`.** Here no finite certificate can work: the margin is `κ²/27 → 0`. S6 gives the
   coefficient but not a remainder bound, and the expansion is not uniform — at `ζ → ζ₁` the
   partner approaches `z_− = −1`, where `θ_−` is not analytic in `κ`. This is the honest gap.

The **directional lemma itself** remains open in its mixed directions, and this attempt does not
touch them: for `u` at angle `α` to `V`, the excess region of the perturbation is the cap
`{u·s > A cos α}`, which is a half-sphere only at `α = π/2`. The mirror plan of C3a needs that
half-sphere; the antitone plan of S3 needs azimuthal symmetry about the perturbation axis, which
holds only at `α = 0`. Splitting `u` into its two components and adding the two plans costs
`cos α Φ + sin α (A/κ)`, which exceeds `A/κ`; at `κ = 0` that split gives `√2/3 = 0.4714` where the
truth is `1/3`, so the loss is real and not an artefact. **Until the mixed directions are done the
region stays `a2`'s `3/10`, not `3/7`.** What this attempt removes is one of the two obstacles.

## 4. What would finish it

1. **A modulus of continuity for `Φ` in `κ`** — then S5's 14 points become the interval `[1/10, 3]`.
   `Φ(κ) = c(κ)∫chord e^ζ ζ dζ` with a `κ`-free pairing (S2), so the `κ`-dependence is explicit in
   `c`, `ζ₁` and the two maps `z = A + ζ/κ`; this looks routine rather than deep.
2. **A remainder bound at the origin.** The clean form to aim at: the pointwise inequality
   `M(z) ≤ M_max cos²(Δ/2)`, `Δ` the opening angle of the pair, which is equivalent to
   `chord ≤ 2√(1 − m/M_max)` and, integrated, gives `Φ ≤ A/κ` whenever it is combined with
   `M_max ≤ (3/4)A/κ`. Both hold in every case I evaluated, both are equalities at `κ = 0`, and the
   second is a closed-form scalar inequality. The first is tight to `O(κ²)` relative, which is why
   I did not get it: it is *harder* than the integrated statement, not easier. A proof of the
   integrated inequality that does not go through a pointwise one is the thing to look for.
3. **The mixed directions.** The obstacle is stated above. What is needed is a single plan for the
   perturbation `(u·s − E[u·s])p`, not the sum of two plans; equivalently, a quantitative form of
   the mirror argument showing that an `f` which nearly attains `Cov(f, x) = A/κ` must have small
   `Cov(f, z)`. The extremal `f = w·s` of the perpendicular case has `Cov(f, z) = 0` exactly, so
   the trade-off is real and the two-dimensional set `{(Cov(f,z), Cov(f,x)) : f Lip}` is the object
   to bound. With that, `L = 1/3` and the region is `β < 3/7`.
4. **Past `3/7`** nothing sitewise can help: `a2`'s S6 exhibits a configuration where the sitewise
   W1 coefficient is `7β/3`, so `3/7` is the ceiling of this whole method, and the executed onset
   (S8) is a factor 1.17–1.40 above it. Closing that last factor needs a non-sitewise argument.

## 5. Running it

```
python3 probes/work/derive/lightcone-uniqueness-region/w-jonathonsmac4f50-j715c/check.py
```
from the repository root (it reads `logs/probes/X:lightcone-*` for S8). About 6 minutes; needs
`sympy`, and `mpmath` for S6 alone.
