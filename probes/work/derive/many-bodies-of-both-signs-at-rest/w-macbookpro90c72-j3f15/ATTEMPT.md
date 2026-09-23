# Bodies of both signs at rest in the curvature member

Attempt 1 of 2. Worker `w-macbookpro90c72-j3f15`, model `claude-opus-5-5`. Script: `check.py` in this directory. It prints 11 checks, then a `SUMMARY` line and a `HIT` line.

**Provenance.** No earlier attempt at this problem exists, so the plan is my own. Two overlaps with earlier units:
- The capacity inequality in (e) uses the same potential theory as my unit `pinned-what-is-a-source:a3` (#8769).
- The `Z³` Green function code is reused from that unit.

**Sources:**
- block 60 (PR #8590): T4, the strong field of the curvature member; the premise that bonds are crossed at `√(w_x w_y)/(χ_x χ_y)`;
- block 71 (PR #8603): T3, a negative body at rest;
- block 75 (PR #8608): T1, the identity; T2, the closed-lattice no-go;
- block 59 (PR #8581): the generator and the hop energies.

## 1. Statement attempted

**Setting.** Bodies at rest sit at sites `x_i`, with `μ_i = m_i/(8K)` of either sign, in a box with held walls (`χ = N = 1` on the walls). The equations are:
- lengths: `χ = 1 + Σ Q_i g(·, x_i)`, with `Q_i χ(x_i) = μ_i`;
- rates: `N = 1 − Σ P_i g(·, x_i)`, where `N` solves `L N = 0` with `L = −Δ + Q/χ`;
- the rate itself is `w = N/χ`.

Positive static rates exist iff `L` is positive definite (block 71 T3(d)). For two bodies write `a = G_AA`, `b = G_BB`, `c = G_AB`, `D = ab − c²` and `v = Q/χ`.

**Claims:**
- **HIT case.** On the `5³` box with walls at 0 and 6 there is an exact configuration at rest with every rate positive:
  - a negative body at `(3,3,4)` with `μ_B = −1.5929`, beyond its single-body bound `−1/(4G_BB) = −1.1045`;
  - a positive body at `(3,3,3)` with `μ_A = 7.1650`;
  - rational charges `Q = (4, −2)`.
- **(a) A positive and a negative body.**
  - At a solution with positive lengths, `L` is positive definite iff `b/D + v_A > 0` and

        v_B > −(1 + a v_A)/(b + D v_A) = −1/b − c² v_A/(b(b + D v_A)).

  - The fold of the lengths' map `Q ↦ μ` is exactly where `L` loses definiteness.
  - The exact region is the image of the branch through `Q = 0`, up to that fold.
  - A positive neighbour (`v_A > 0`) extends the negative body's bound.
  - At the certificate's `(μ_A, μ_B)` the lengths' equations have 4 roots. 2 are real, both have positive lengths, and exactly one has `L > 0`.
  - Executed on `Z³`: the bound goes from `−0.989` to about `−1.86` next to `μ_A = 8` at distance 1.
- **(b) Two negative bodies.**
  - Each body satisfies `μ_i > −1/(4G_ii)` strictly: the joint region lies inside the single ones.
  - A symmetric pair folds at `μ* = −1/(4(g₀ + g_d))`.
- **(c) A pair with zero ledger** (`Q_A = −Q_B`).
  - It is static, with `L > 0` for a range of `Q`.
  - The lengths carry no monopole (a dipole only).
  - The rates carry the monopole `P_A + P_B < 0`, so clocks run fast far away.
- **(d) Content that moves.**
  - From block 60's bond form, stationarity gives

        (Δχ)_z = −e_z/(8K N_z),    (ΔN)_z = (e_z + 2τ_z)/(8K χ_z),

    with `τ_z` half the hop energy on `z`'s bonds. This re-derives the supervisor's relation.
  - With block 75 T1:
    - For block 54's walker, which has no on-site term, `e = τ`. A closed lattice is then at rest only if `e = 0` at every site, whatever the signs of the content's energies.
    - With rest energy present, the identity requires only `Σ e/(χN) < 0 < Σ τ/(χN)`. That is not excluded. A single pair of amplitudes of opposite sign, with a common rest energy, never meets it.
- **(e) A spread body.**
  - Exact: on any set `S` of body sites, `Σ μ_i ≥ −Cap(S)/4`.
  - Executed: spread evenly over balls, a negative body reaches `0.88–1.00 × (−Cap/4)`. So its bound grows with its capacity (linear size), not with its number of sites.

## 2. Steps

Each step is marked PROVED (argument given in full), CHECKED (verified by `check.py`, check named in brackets) or ASSUMED.

**S1 — CHECKED [B1]. The box.**
- The interior is `{1..5}³`, with walls at 0 and 6.
- The columns `g(·, A)` and `g(·, B)` of `(−Δ_D)^{-1}` are computed by exact banded elimination in Fractions.
- `−Δg = δ` is verified at all 125 sites.
- `G_AA = 68/297`, `G_AB = 37/594`, `G_BB = 34706593/153333180`.

**S2 — CHECKED [B2]. The HIT certificate.** Take `Q = (4, −2)`. Everything below is exact.
- `χ = 1 + 4g_A − 2g_B > 0` at every site; the minimum is `0.7965`, at `B`.
- `μ = (Q_A χ_A, Q_B χ_B) = (7.1650, −1.5929)`, and `μ_B < −1/(4G_BB)`.
- `L = −Δ_D + diag(v)` has all 125 pivots positive (Sylvester, by elimination), so it is positive definite.
- `P = (I + VG₂)^{-1}V1`, and `N = 1 − P_A g_A − P_B g_B` satisfies `LN = 0` at every interior site, with `N = 1` on the walls.
- `N ≥ 0.8724`, and the rates lie in `[0.487, 2.556]`.
- By block 71 T3(a), B alone at this `μ_B` has no real solution (`1 + 4G_BB μ_B < 0`).

**S3 — PROVED and CHECKED [S1]. The criterion and the fold.**
1. **Reduction.** For `V` supported on the two body sites, `−Δ + V > 0` iff `G₂^{-1} + V₂ > 0`, where `G₂` is the Green's function restricted to those sites. Proof: conjugate by `G^{1/2}`. The nonzero spectrum of `G^{1/2}VG^{1/2}` is that of `G₂^{1/2}V₂G₂^{1/2}`.
2. **Sylvester.** For the 2×2 matrix this is `b/D + v_A > 0` together with `det = (b/D + v_A)(a/D + v_B) − c²/D² > 0`. The latter is the threshold on `v_B` above, by algebra (sympy).
3. **The fold.** `det(∂μ/∂Q) = det(diag χ + diag(Q) G₂) = χ_Aχ_B det(I + VG₂)`, and `det(G₂^{-1} + V) = det(I + G₂V)/det G₂`. So along any path of solutions with positive lengths, an eigenvalue of `G₂^{-1} + V` crosses zero exactly at a fold. `L > 0` at `Q = 0`, so it holds on the branch through `Q = 0` up to the first fold. That branch, mapped to `μ`, is the exact region.
4. **Extension.** For `v_A > 0` the threshold on `v_B` lies below `−1/b` by `c²v_A/(b(b + Dv_A)) > 0`. So a positive neighbour extends the negative body's bound.

**S4 — CHECKED [B3]. The roots.**
- The resultant in `Q_A` of the two quadratics is an exact quartic in `Q_B`.
- Sturm counting gives 2 real roots.
- Both have `χ_A, χ_B > 0`.
- One, the certificate, has `L > 0`. The other (`Q ≈ (4.152, −3.613)`) has `det < 0`: it is the analogue of block 71's lower root.

**S5 — PROVED and CHECKED [S2, S3]. Two negative bodies.**
- *Signs.* `χ_i > 0` makes the sign of `Q_i` the sign of `μ_i`.
- *Each body tighter.* If both are negative, `χ_A = 1 + aQ_A + cQ_B < 1 + aQ_A`. Since `Q_A < 0`, `μ_A = Q_Aχ_A > Q_A(1 + aQ_A) = a(Q_A + 1/(2a))² − 1/(4a) ≥ −1/(4a)`. The same holds for `B`.
- *Symmetric pair.* `Q(1 + (g₀ + g_d)Q) = μ`, with the fold at `1 + 2Q(g₀ + g_d) = 0`, i.e. `μ* = −1/(4(g₀ + g_d))`.
- *On the box* (symmetric placement `(3,3,2)`, `(3,3,4)`):
  - `μ* = −1.0102`, against the single bound `−1.1045`;
  - at `0.99μ*` the symmetric solution has `L > 0`;
  - at `1.01μ*` it has no real solution.

**S6 — CHECKED [C1]. The zero-ledger pair.** Take `Q_A = −Q_B = 1` on the box.
- `μ = (1.1667, −0.8359)`.
- `L > 0`, `χ > 0` and `N > 0`, all exact.
- The ledger is `8K(Q_A + Q_B) = 0`, so `χ − 1 = Q(g_A − g_B)` carries no monopole.
- The rate monopole is `P_A + P_B = −0.77395`.

On `Z³` the pair is static for `0 < Q < Q_max(d)`, with `Q_max = 2.44, 2.17, 2.06` at `d = 1, 2, 4` (executed while exploring; not printed by `check.py`).

**S7 — PROVED and CHECKED [D1]. The field equations with moving content.**
- *Block 60's premises.* Lengths per site `ℓ = χ²`, bond lengths `χ_xχ_y`, and bonds crossed at `√(w_xw_y)/(χ_xχ_y) = √(N_xN_y)/(χ_xχ_y)^{3/2}`.
- *Block 59's ledger.* `⟨H⟩ = Σ_b c_b⟨h_b⟩ + Σ_x w_x⟨m_x⟩`.
- *Stationarity.* Take `F + ⟨H⟩` with `F = 8K Σ N(Δχ)`, holding the content's energies per tick fixed:
  - `∂/∂N_z = 8K(Δχ)_z + e_z/N_z`, with `e_z = w_z⟨m_z⟩ + τ_z`;
  - `∂/∂χ_z = 8K(ΔN)_z − (e_z + 2τ_z)/χ_z`, where the `2τ` comes from the power `3/2`.
- *Consistency.* Bodies at rest (`τ = 0`, `e = mw`) give back block 60 T4's equations.
- *Check.* Verified symbolically on a ring of 4 sites with symbolic `N`, `χ`, `⟨h_b⟩` and `⟨m_x⟩`. Block 75 T1 is also checked, on exact rationals.

**S8 — PROVED and CHECKED [D2]. A closed lattice with moving content.**
1. **The identities.** By block 75 T1 applied to `χ` and to `N`:

       Σ e/(χN) = −8K S_χ ≤ 0,    Σ (e + 2τ)/(χN) = 8K S_N ≥ 0,

   where `S` denotes block 75's sums of squares.
2. **Block 54's walker.** It has no on-site term, so `e_z = τ_z` exactly (block 59 T2). Then `3·(−8K S_χ) = 8K S_N`, so `S_N + 3S_χ = 0` and both vanish. `χ` and `N` are therefore uniform, `Δχ = 0`, and `e_z = 0` at every site. This holds whatever the signs of the amplitudes' energies.
3. **With rest energy.** The identities only require `Σ e/(χN) < 0 < Σ τ/(χN)`.
   - For eigen-amplitudes with anticommuting mass, `τ = E − m²/E`.
   - Weak-field example: one amplitude at `E = 2m` and three at rest at `−m` give `ΣE = −m < 0 < Στ = 3m/2`.
   - A single pair of opposite signs never meets it: `ΣE < 0` forces `|E₋| > E₊`, and `τ` is odd and increasing in `|E|`.
   - Existence of rest in this case is not decided.

**S9 — PROVED and CHECKED [S2]. The capacity bound.**
- Take any configuration on `S`, with `Q` real and `q = 1ᵀQ`.
- Then `Σμ_i = 1ᵀQ + QᵀGQ`.
- By Cauchy–Schwarz in the `G` inner product, `QᵀGQ ≥ q²/(1ᵀG_S^{-1}1) = q²/Cap(S)`.
- Also `q + q²/C = (q + C/2)²/C − C/4`.
- Hence `Σμ_i ≥ −Cap(S)/4`. It is tight for one site: `Cap = 1/g₀`, which is block 71's bound.

**S10 — executed [X1, X2], in floating point.**
- *X1.* On `Z³`, continuation along the branch with `L > 0` (a lower estimate of how far it reaches):

  | distance | `μ_A = 0.5` | `μ_A = 2` | `μ_A = 8` |
  |---|---|---|---|
  | `d = 1` | `−1.080` | `−1.288` | `−1.860` |
  | `d = 2` | `−1.031` | `−1.124` | `−1.370` |
  | `d = 4` | `−1.008` | `−1.050` | `−1.158` |

  The single bound is `−0.989`. For two equal negative bodies, the joint bound is `−0.738, −0.846, −0.916`.
- *X2.* A negative body spread evenly over balls reaches `−0.989, −2.706, −3.978, −4.878, −6.665, −7.755` for `N = 1, 7, 19, 33, 81, 123`. Each lies within `0.88–1.00` of `−Cap/4`.

## 3. Where the route stops

- (a)'s region is exact as a set: the image of the positive-definite branch up to the fold. Its boundary in `(μ_A, μ_B, d)` is given parametrically, not in closed form.
- (d) is decided for block 54's walker. For content with rest energy the identity gives necessary conditions only.
- (e) is an exact bound plus an executed scaling. The largest total for a given shape is not computed exactly.
- Bodies are pinned. Stability of the configurations at rest is not examined.

## 4. What would finish it

1. A closed form, or a monotone description, of the fold curve `μ_B*(μ_A, d)`. At first order in `c`, `μ_B* ≈ −(1 + cQ_A)²/(4b)`.
2. Rest on a closed lattice with rest-energy content: solve the two field equations of S7 for a pair of amplitudes of opposite signs, with the fast one positive, as S8 suggests.
3. Stability of the pair at rest, and the attraction or repulsion between the bodies (block 71's "chase" for mixed pairs).
