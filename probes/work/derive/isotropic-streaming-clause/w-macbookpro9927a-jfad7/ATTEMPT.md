# isotropic-streaming-clause, attempt a3: forward rules with a constant total rate, and the one number that decides isotropy

**Provenance.**
- Written by Claude Opus 5.5 (`claude-opus-5-5`), worker `w-macbookpro9927a-jfad7`, task `J:derive:isotropic-streaming-clause:a3`.
- **Prior attempts, from another machine:**
  - a1 (`w-jonathonsmac4f50-j8197`, `claude-opus-5-5`, the same model family as this worker). It was refereed by grok-4.6 (`referee_w-macbookpro90c72-je5f4`) and confirmed, with the flux-to-density step of its shadow flagged as its assumption.
  - a2 (`w-jonathonsmac4f50-j1e60`, `claude-opus-5`). It was refereed by grok-4.6 (`referee_w-macbookpro90c72-j2c8f`) and confirmed.
- This machine has no related units.
- **Plan before reading a1 and a2.** Write each content `s` as a convex combination of forward neighbours with mean `s` (a barycentre), and tune the fourth-rank moment by mixing two such rules.
- **After reading them.**
  - a1 solves (a) inside the shell-linear family `λ_{|d|²}(s·d̂)_+`. Its total rate is never constant, so its capture law and shadow stay anisotropic (15% and 33% spreads on its two minimal members).
  - a1 leaves open (its item 3) "whether any forward-only rule with constant κ has a constant total rate".
  - a2 gives pointwise witnesses and a two-way axis rule.
  - This attempt takes the barycentre route to a1's item 3, then builds (a) on top of it.
- **Landed first.**
  - Block 51's note is on main (PR #8563 is closed; its content landed as `docs/ADMISSIBILITY_RULE_THE_WIND_OF_A_CAPTURING_BODY_IS_NOT_ISOTROPIC_…_2026-09-21.md`). Its scope is narrowed: "conditional dilute independent streaming and first-harmonic local closure … historical direction-resolved simulations are author reports".
  - I use only its definitions and moments. The executed winds are not used.
  - Block 48 on main: "capture is weighted by `|s|_1`" for supplied forward axis hops; the shadow has "coordinate-plane multiplicity".
  - Block 44 on main (T2): "every record … has exactly one streaming preimage".
  - The paraphrases in the task agree with these landed statements where I use them.
- **A later landed block on the same question.** The task does not name it; I found it by listing the campaign's notes on main. It is block 52, `docs/ADMISSIBILITY_RULE_A_STREAMING_CLAUSE_WITH_AN_ISOTROPIC_SECOND_ORDER_TERM_CONTENT_AS_A_BIAS_ON_A_SYMMETRIC_WALK_UNBIASED_CAPTURE_AND_ITS_PRICE_…_2026-09-21.md`.
  - **Its clause.** Axis rates `(α + c s·e)/2` with `α ≥ c`, i.e. a2's two-way rule.
  - **Its results.**
    - `M = αI`.
    - T1: on the six axes the second moment along axis `k` is at least `c|s_k|`, "and only forward hops reach it".
    - T3: content-independent capture, for a single site and for balanced bodies, under a product-reservoir assumption.
    - T5: the price, a fifth to two thirds of the hops not following the content.
  - **Its No-Go gate leaves two routes open:**
    1. "*Hops to more neighbours* … a clause with less diffusion and an isotropic fourth-rank moment may exist there. Not worked."
    2. "`αδ_kl + β s_k s_l` … `β = 0` is forced with six neighbours."
  - **This attempt works both** (§1): route 1 positively, up to one float number; route 2 negatively, under a constant total rate. Nothing here re-derives block 52's results.

## 1. What is claimed

Take hop rates `a(s, d) ≥ 0` on the 26 neighbours with mean step `Σ_d a(s,d) d = r₀ s`. Here `r₀` is a constant; `r₀ = 1/√3` gives block 51's speed. Units below are `r₀ = 1`. As in a1, `M_kl(s) = Σ_d a(s,d) d_k d_l` and `T_ijkl = ⟨s_i s_j M_kl(s)⟩` over the uniform sphere.

**(a) and a1's item 3: forward rules with a constant total rate exist.** Every unit `s` is the barycentre of its forward neighbours.

Order `|s|` as `a ≥ b ≥ c ≥ 0` on axes `i, j, k`, and write `u_m = sign(s_m) e_m`. Then `s` is the convex combination

```
(1 - t)[(a-b) u_i + (b-c)(u_i+u_j) + c(u_i+u_j+u_k)] + t[a u_i + b u_j + c u_k],     t = (1 - a)/(b + c).
```

This is the **staircase rule**. It has:
- non-negative weights summing to 1, and mean exactly `s`;
- at most five targets, each with `s·d > 0`;
- continuity on the sphere and covariance under the 48 cubic symmetries.

So the total rate is `r(s) ≡ r₀`, the same for every content. Records keep "content = direction of travel". Each step is **sign-compatible**: it never moves against any component of `s`. A second valid rule uses only axes and face diagonals: a maximal merge, scaled to total weight 1 (§2 step 4).

**(b) With a constant total rate:**
- **Stationarity** is kept. a1 proves the uniform product measure stationary for **every** rate function on any hop set, with the exchange rule. With reflecting solids it also needs `a(−s,d) = a(s,−d)`, which both rules satisfy. With the rate constant, block 44's bookkeeping holds literally: each record has one event clock of rate `r₀`.
- **The capture law of a site is isotropic.** At first order in the density, content `s` is captured at rate `ρ r(s) = ρ r₀` for every `s`. Block 48 has `|s|_1` for axis hops; a1's members are anisotropic.
- **The far collisionless shadow (flux form) is isotropic:** `r(n̂)/(4π⟨r⟩) = 1/(4π)` per unit capture in every direction. This is a1's step 8 with `r` constant. The density form is ASSUMED, as in a1.

**(a) itself: one number decides isotropy, and a mixture meets it.**
- **Block 52 T1's least-diffusion bound is unchanged on the 26 neighbours.** For any rule with mean `s`, `M_mm = Σ_d a d_m² ≥ Σ_d a|d_m| ≥ |s_m|`. Equality holds exactly when every weighted target has `d_m ∈ {0, sign(s_m)}`: the rule is **sign-compatible**, the 26-neighbour form of "only forward hops reach it".
- **The diagonal is universal.** Every sign-compatible rule with mean `s` has `M_mm(s) = |s_m|` exactly, at every `s` and for any total rate. Hence `T₁₁₁₁ = ⟨|s_1|³⟩ = 1/4` and `T₁₁₂₂ = ⟨s_1²|s_2|⟩ = 1/8`, the axis rule's values. So
  ```
  T = (1/8) δ_ij δ_kl + β (δ_ik δ_jl + δ_il δ_jk) + (1/8 − 2β) δ_ijkl,     β = T₁₂₁₂ = ⟨|s_1 s_2| W_12(s)⟩,
  ```
  with `W_12` the rate of steps that move in both coordinates 1 and 2. **(a)'s isotropy is the single condition β = 1/16.** Axis hops have `β = 0`.
- **The streaming equations.** At block 51's speed, a1's local-equilibrium form of the momentum term becomes
  ```
  ν_lat [∇²g_i + 16β ∂_i(∇·g) + (1 − 16β) ∂_i² g_i],     ν_lat = √3/16,
  ```
  and the number term is `D_lat ∇²n`, `D_lat = 1/(4√3)`. These are block 51's own coefficients. `β` only moves weight from block 51's cubic term `∂_i²g_i` to the isotropic `∂_i(∇·g)`.
- **The two rules' values (float, converged quadrature):**

  | rule | `β` | block 51's `η = 1 − 16β` |
  |---|---|---|
  | staircase | `0.06489844` | `−0.038` |
  | axes-and-faces | `0.05612879` | `+0.102` |
  | block 51's axis clause | `0` | `1` |

- **The mixture.** The two values of `β` lie on opposite sides of `1/16`, and `T` is linear in the rule. So the mixture `(1 − λ)·staircase + λ·(axes-and-faces)`, with `λ = 0.27349352` (float), has `β = 1/16` and `T = (1/8)[δ_ijδ_kl + (δ_ikδ_jl + δ_ilδ_jk)/2]`. It is:
  - forward, sign-compatible, with constant total rate;
  - at most 7 targets per content.

  Its streaming term is `ν_lat[∇²g_i + ∂_i(∇·g)]`, which vanishes on a potential inflow. So block 51 T3's obstruction is absent at the level of the streaming term.
- **No pointwise route.** No forward rule with constant speed and constant total rate has `M(s) ∈ span{I, s sᵀ}` on the arcs `(a, b, 0)`, `0 < b < a`. That includes a2's reduction `M ∝ I` and block 52's route 2. Isotropy has to come from the sphere average. (The argument needs `r(s) < (1 + ab)/(a + b)` on the arc, which holds at `r = 1` since `(1 − a)(1 − b) > 0`. A larger total rate escapes it, so the lemma is specific to a constant rate.)
- **Against block 52.** Block 52's clause reaches `M = αI` with `α ≥ c` and pays with hops against or across the content. The mixture here keeps every hop forward and sign-compatible, at the least diffusion `M_mm = |s_m|`, which is block 44's forward rule's value. It pays with diagonal steps and one float number `λ`.
- **The capture argument needs no reservoir assumption.** For forward rules the density upstream of a site is exactly unperturbed at first order in the density. Block 52 T3 assumes "the same product-reservoir content law and density beside every exposed face".

**(c) The cost.**
- Records step to face-diagonal (`√2`) and body-diagonal (`√3`) neighbours. That needs:
  - exchange with a diagonal target;
  - reflection at solids as content reversal (a1's point);
  - a rule that reads the ordering of `|s_k|`. It is piecewise rational and continuous, not block 51's single formula `|s_k|/√3`.
- In return, every step is sign-compatible and forward, every record keeps one clock of rate `r₀`, and its mean step is exactly `r₀ s`.
- `D_lat` and `ν_lat` are block 51's values.
- Isotropy of `T` needs the mixing weight `λ`. This attempt gives it only as a float.
- Alone, the staircase rule already cuts the cubic coefficient of `T` (`T₁₁₁₁ − T₁₁₂₂ − 2T₁₂₁₂`) from block 51's `1/8` (at unit speed) to `−0.0048`, a factor of 26.

## 2. Steps

1. **ASSUMED — the setting.**
   - These are supplied hypotheses, and none is adopted:
     - block 44's clause (S) (exchange at occupied targets, the re-draw at bonds), with the hop set enlarged to the 26 neighbours;
     - block 51's streaming expansion (exact on fields of degree two, block 51 T1);
     - bodies that capture.
   - Everything second-order is inside block 51's landed scope: "conditional dilute independent streaming and first-harmonic local closure".

2. **PROVED / CHECKED (H1) — the barycentre theorem.**
   - Let `a ≥ b ≥ c ≥ 0` be the sorted `|s_m|` on axes `i, j, k`, with `a² + b² + c² = 1`.
   - **The axis form** `X = (a on u_i, b on u_j, c on u_k)` has mean `s` and total `a + b + c`. The total is `≥ 1`, because `(a + b + c)² ≥ a² + b² + c² = 1`.
   - **The staircase form** `Y = (a − b on u_i, b − c on u_i+u_j, c on u_i+u_j+u_k)` has:
     - mean `(a − b + b − c + c)u_i + (b − c + c)u_j + c u_k = s`;
     - total `a ≤ 1`.
   - **The mixture** `tX + (1 − t)Y` has mean `s` and total `a + t(b + c)`. That total is 1 at `t = (1 − a)/(b + c)`, and `t ∈ [0, 1]` because `a ≤ 1 ≤ a + b + c`.
   - **The weights** `(1 − t)(a − b) + ta`, `(1 − t)(b − c)`, `(1 − t)c`, `tb` and `tc` are all `≥ 0`.
   - **Forwardness.** `s·u_i = a > 0`, `s·(u_i+u_j) = a + b` and `s·(u_i+u_j+u_k) = a + b + c` are positive. `u_j` and `u_k` carry weight `tb` and `tc`, which are zero whenever `b` or `c` is.
   - **The axis.** At `b + c = 0` (`s = ±e_m`), put `t = 0`: weight 1 on `u_i`.
   - **Checked exactly:** weights `≥ 0`, sum 1, mean exactly `s`, every weighted target with `s·d > 0`. This holds at 3174 rational points of the sphere (stereographic images plus special points, all 48 cubic images of each).

3. **PROVED / CHECKED (H2) — continuity.**
   - `t` depends only on `a` and `b + c`.
   - **Tie `a = b`.** Both orders give weight `ta` on each of `u_i` and `u_j`, `(1−t)(a−c)` on `u_i+u_j`, `(1−t)c` on the body, and `tc` on `u_k`.
   - **Tie `b = c`.** Both orders give `(1−t)(a−b)+ta`, `(1−t)b` on the body, `tb` on each of `u_j` and `u_k`, and `0` on the face.
   - So the formulas agree on the sector walls.
   - **A zero component.** It is the smallest, `c = 0`. Its targets carry `(1−t)c = tc = 0`, so the arbitrary sign of `u_k` does not matter.
   - **Near an axis.** `1 − a = (b² + c²)/(1 + a) ≤ (b + c)²`, so `t ≤ b + c → 0`, and the weights tend to 1 on `u_i`.
   - Inside a sector the weights are rational with non-vanishing denominators.
   - **Checked exactly:** the aggregated weights are independent of the tie-break at all 510 tied points, for both rules, and `t ≤ b + c` holds everywhere.

4. **PROVED / CHECKED (H3) — the axes-and-faces rule.**
   - **Merges.** Merging weight `z` from `u_m` and `u_n` into `u_m + u_n` keeps the mean and lowers the total by `z`. So merges `z_ij, z_ik, z_jk ≥ 0` with budgets `z_ij + z_ik ≤ a`, `z_ij + z_jk ≤ b` and `z_ik + z_jk ≤ c` give total `a + b + c − Σz`.
   - **The maximal merge `z*`:**
     - `(b, c, 0)` if `a ≥ b + c`, with `Σz* = b + c`;
     - otherwise `((a+b−c)/2, (a−b+c)/2, (−a+b+c)/2)`, with `Σz* = (a+b+c)/2` and every budget tight.
   - **The scaling.** Scale by `θ = (a + b + c − 1)/Σz*`. Then `θ ∈ [0, 1]`, because `a ≤ 1` in the first case and `a + b + c ≤ √3 < 2` in the second.
   - **Validity.** The weights are non-negative, the total is 1, the mean is `s`, and `u_j + u_k` is weighted only when `b + c > a`, where `s·(u_j+u_k) > 0`.
   - **Continuity.** The two forms of `z*` agree at `a = b + c`.
   - **Checked exactly:** at all 3174 points, including tie-independence.

5. **PROVED / CHECKED (H4) — the capture law.**
   - This is a1's step 7, used as argued there. Along a forward walk `s·x` increases strictly. So the content-`s` density at the upstream neighbours `y = −d` (`s·d > 0`) of a capturing site is untouched by it at first order in the density.
   - The capture rate is therefore `Σ_d ρ a(s,d) = ρ r(s)`, and here `r(s) ≡ r₀`, checked exactly at every point for both rules.
   - A fully exposed site in a homogeneous reservoir thus captures the reservoir's own content law.
   - Extended bodies (mutual shadowing) are not addressed.

6. **PROVED / CHECKED (H5) — stationarity.**
   - a1's step 6 proves the balance for every rate function. Its argument: one predecessor per record and per hop vector, whether by hop, exchange or reflection. The grok referee confirmed it on three `3³` censuses.
   - The rules are covariant under `s → −s`, so `a(−s,d) = a(s,−d)` (checked exactly). a1's reflecting-solid case applies.
   - With the total rate constant, block 44 T2's statement ("each record, at rate 1, tries to step") holds with the target drawn from the rule.

7. **PROVED given the strong law (flux form); ASSUMED (density form) — the far shadow.**
   - a1's step 8 gives the missing outgoing flux per unit capture as `r(n̂)/(4π⟨r⟩)`, which is `1/(4π)` here. Each missed record continues as a walk with i.i.d. steps of mean `s`, so its exit direction tends to `ŝ`.
   - The density form needs a local limit, as in a1.
   - Near the coordinate planes it also needs block 48's care. A sign-compatible walk with `s_m = 0` never moves along `m`, which is block 48's "coordinate-plane multiplicity".

8. **PROVED / CHECKED (H7) — the universal diagonal and the reduction.**
   - **The bound.** For `d_m ∈ {−1, 0, 1}`, `d_m² = |d_m|`. So for any rule with mean `s`, `M_mm = Σ a|d_m| ≥ |Σ a d_m| = |s_m|`, with equality iff no weighted target has `d_m = −sign(s_m)`. This is block 52 T1's bound, and it is unchanged by diagonal hops.
   - If every target has `d_m ∈ {0, sign(s_m)}`, then `d_m² = sign(s_m) d_m`. So `M_mm = sign(s_m) Σ_d a d_m = sign(s_m) s_m = |s_m|`.
   - Then `T₁₁₁₁ = ⟨|s_1|³⟩ = 1/4` and `T₁₁₂₂ = ⟨s_1²|s_2|⟩ = 1/8`, by sympy integration. These are block 51's moments at unit speed, which a2 also checked.
   - **Cubic invariance.** For a cubic-covariant rule, `T` is cubic-invariant with symmetric pairs `(ij)` and `(kl)`. Its only possibly non-zero components are then `T₁₁₁₁`, `T₁₁₂₂ = T₂₂₁₁` and `T₁₂₁₂`. Any component with an odd count of an index vanishes under a sign flip, and permutations relate the rest.
   - **Isotropy.** The isotropic tensors of this symmetry are `αδ_ijδ_kl + β(δ_ikδ_jl + δ_ilδ_jk)`. So isotropy is `T₁₁₁₁ = T₁₁₂₂ + 2T₁₂₁₂`, i.e. `β = 1/16`.
   - **The joint-step rate.** `s_1 s_2 M_12 = |s_1 s_2| W_12`, because every target has `d_1 d_2 = sign(s_1 s_2)` or 0.
   - **The equations.** a1's step 5 (local equilibrium `(n/4π)(1 + 3u·s)`; `M` is even in `s` by inversion covariance) turns `T` into the momentum term `(3/2)∂_k∂_l T_ijkl g_j`. That is `(3/16)[∇²g_i + 16β∂_i∇·g + (1 − 16β)∂_i²g_i]` at unit speed, and `ν_lat[…]` with `ν_lat = √3/16` at speed `1/√3`.
   - The number term `(1/2)⟨M_kl⟩∂_k∂_l n` has `⟨M_mm⟩ = ⟨|s_m|⟩ = 1/2`. That gives `D_lat = 1/(4√3)` at block 51's speed.
   - **Checked exactly:** `M_mm = |s_m|` and sign-compatibility at every point, for both rules. The quadrature also reproduces `1/4` and `1/8` to `1e-12`.

9. **PROVED / CHECKED (H6) — no pointwise route.** Let `s = (a, b, 0)` with `0 < b < a`, and take a rule with total 1 and mean `s`.
   - **The forward set.** It is `{d_1 = 1} ∪ {(0, 1, *)}`: `d_1 = −1` would need `b d_2 > a`.
   - **The forced entries.**
     - `Σ w d_1 = a` puts weight `1 − a` on `d_1 = 0`, where every target has `d_2 = 1`. Hence `M11 = a` and `M12 = b − (1 − a) = a + b − 1`.
     - `M22 = Σ w d_2² ≥ Σ w d_2 = b`.
   - **The contradiction.** If `M = αI + β s sᵀ`, then `β = (a + b − 1)/(ab)` and `M22 = a − β(a² − b²)`. Using `(a + b)² = 1 + 2ab`, `M22 − b = −(a − b)(1 − a)(1 − b)/(ab) < 0`, which is impossible.
   - **Checked exactly:** the forward set and the identity at 8 rational arc points, with both rules as instances of the forced `M11` and `M12`.

10. **CHECKED (float) (N0, N2, N1) — the values of `β` and the mixture.**
    - **N0.** The float builders of `M` equal the exact rules' `M` at all 82 rational sector points (deviation `2e-16`).
    - **N2.** Gauss–Legendre on the sector `a ≥ b ≥ c ≥ 0` in `(ψ, ρ)` coordinates of `(b, c)`.
      - The range of `ρ` is split at the kink `a = b + c` of the axes-and-faces rule, so every piece is analytic.
      - `n = 16` and `n = 32` differ by `7e-16`.
      - The sector area matches `π/12`.
      - Results: `β = 0.06489844` (staircase) and `0.05612879` (axes-and-faces).
    - **N1.** An independent route: the full sphere as 48 images, with the tensor assembled in the lab frame. It agrees to `1e-8`.
    - **The mixture.** `λ = (β_st − 1/16)/(β_st − β_af) = 0.27349352`. The mixture has `α = 0.125000` and `β = 0.062500`.
    - A variance-reduced Monte Carlo in the scratchpad (not part of check.py) gave `−0.00478 ± 0.00007` and `+0.01276 ± 0.00006` for `1/8 − 2β`.
    - **Status.** The existence of `λ ∈ (0, 1)` is exact **given** the two signs, and the signs are float. The margins are 3.8% and 10% of `1/16`.

11. **The cost (c).** See §1(c).

## 3. Where the route stops

- **The first non-exact step is step 10.** The exact values of `β` for the two rules are not computed.
  - The sector integrands are rational: `(σ − 1)(ab² + ac² + bc²)/(3(b + c))` for the staircase, with `σ = a + b + c`, and two rational pieces for the axes-and-faces rule.
  - Their sector integrals were not evaluated in closed form.
- **One exact route was tried and fails as stated.**
  - The idea: vary the mixing weight pointwise so that `Σ_{m<n}|s_m s_n|W_mn` equals a polynomial `P` in `|s_m|`. The sphere average would then be exact (Beta integrals).
  - On the coordinate planes, `P` is forced to `|s_1 s_2|(|s_1| + |s_2| − 1)`.
  - `P = Σ_{m<n}|s_m s_n|(|s_m| + |s_n| − 1) + (8 − 9π/4)|s_1 s_2 s_3|` has `⟨P⟩ = 3/16` exactly. But a float scan shows it leaves the band between the two rules: the minimum of `(P − lower)/(abc)` is `−0.31`.
  - A richer `P`, or a third rule that widens the band, is open.
- **Not claimed:**
  - an exact value of `λ`;
  - the shadow at moderate distances, or its density form;
  - the collisional viscosity (block 51 marks its isotropy as not proved);
  - the two-body force off the axes;
  - any simulator run of the new clauses;
  - which clause is right, which is a decision for the owner.

## 4. What would finish it

1. **Exact `β` for the staircase and axes-and-faces rules.** Closed-form sector integrals, or a certified enclosure. Or a valid constant-rate rule whose joint-step weights make `⟨|s_1s_2|W_12⟩` exactly computable, then mix exactly.
2. **The shadow at moderate distances.** The exact first-order shadow of the staircase clause, by dynamic programming over forward paths. Then a run of `inertial_wind_by_direction.py` modified to diagonal hops.
3. **The collisional part** of the viscosity.
4. **A referee of another model family.**

## 5. Running it

```
python3 probes/work/derive/isotropic-streaming-clause/w-macbookpro9927a-jfad7/check.py
```

- **Dependencies:** `numpy`, `sympy` and the standard library.
- **Checks.** Seven exact families (H1–H7, `Fraction` and sympy) and three float families (N0, N2, N1).
- **Runtime:** about 3 s.
- **Mutation census: 9 of 9 caught.**
  - a wrong `t`;
  - a mixed-sign body target;
  - a wrong merge scale;
  - swapped merges;
  - a same-sign partner;
  - a wrong sphere moment;
  - the arc identity with the sign flipped;
  - no kink split;
  - a wrong off-diagonal in the float axes-and-faces `M`.
