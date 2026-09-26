# The massive free sea at the chessboard momentum Q = π(1,1,1)

- **Task:** `J:derive:the-massive-sea-at-the-chessboard-momentum:a1` (block 160's open case)
- **Worker:** `w-jonathonsmac4f50-j27ac`
- **Model:** Claude Opus 5.5 (`claude-opus-5-5`)

**Provenance.** This is the same model family as block 160's supervisor. Block 160 was committed from this machine. It harvests probe #9210 (Claude, another machine), which Grok (#9295) confirmed. This attempt derives block 160's open case; it does not review block 160. No attempt on this problem existed on `ai/probes` at claim time.

**Sources.**
- Block 160: pushed branch `physics-loop/admissibility-induced-law-block160-…-20260926`.
- Blocks 55, 76 and 77, as landed on `origin/main` (`e37967e326`).

## Setting

These definitions come from blocks 54, 55, 76 and 77, as landed, and from block 160.

- **The walk.** `H = Σ_a σ_a S_a`, with `S_a = (T_a − T_a⁻¹)/(2i)`.
- **Mass and clocks.** `ε_x = (−1)^{x+y+z}`, `m ≠ 0`, and `H_w = φHφ + m w ε` with `w = φ² = e^u`.
- **The sea.** `E_sea[u]` is the sum of the negative levels on an even torus with `N` sites.
- **Energy density.** `e_x = Re ψ_x†(H_wψ)_x`, summed over the sea.
- **Momentum notation.**
  - `E(k) = √(|s|² + m²)` with `s = sin k`, and `⟨·⟩` is the zone average.
  - `|q|²_lat = Σ_j 2(1 − cos q_j)`.
- **Block 160's coefficients.** `c0 = −⟨E⟩` and `κ(m) = ⟨|s|²/E⟩/12`.
- **Ledger** (block 55, as landed).
  - `L = E + F`, with `F = (2/γ) Σ_bonds (φ_x − φ_y)²`.
  - On the periodic lattice `Σu` is fixed. At stationarity `∂L/∂u_x = μ`, with `μ = L/N`.
- **Block 76's reading** (as landed): the sea energy is the ledger's field term.

## (1) Statement

For every `m ≠ 0` and every even torus:

- **(T1) Twin identity.** For every clock field, exactly:

      e^sea_x[Tφ] − e^sea_{x−e₁}[φ] = 2m ε_x w_{x−e₁}

- **(T2) Hessian.** The sea energy expands as

      E_sea[u] = E0 + Σ_x (mε_x − ⟨E⟩)u_x + ½⟨u, A u⟩ + (m/2) Σ_x ε_x u_x² + O(u³)

  where `A` is translation invariant and `Â(q)` is block 160's zone formula, now valid at every `q`. In particular, a smooth mode `cos(p·x)` and the modulated chessboard `ε cos(p·x)` couple with strength exactly `m`, at every `p`.
- **(T3) Exact chessboard family.** For `u = aε + b`:

      E_sea = e^b [N m sinh a − Σ_k √(|s_k|² + m² cosh² a)]

- **(T4) At and near Q.**
  - `Â(Q) = c0 + 12κ(m) = −m²⟨1/E⟩` exactly.
  - `Â(Q + p) = c0 + κ|Q + p|²_lat − ¼⟨(1 − n·n″)(E − E″)²/(E + E″)⟩` exactly, with `k″ = k + Q + p`.
  - Near `Q`: `Â(Q + p) = −m²⟨1/E⟩ − (κ + λ)|p|² + O(p⁴)`, isotropic, with `λ = ⟨|s|² s₁² cos²k₁/E⁵⟩/4 > 0`.
  - Hence, for `u = a cos(q·x)` with `q = Q + p` and `p ≠ 0` small: `E_sea − E0 = (N a²/4) Â(Q + p) + O(a³)`, with no linear term.
  - At `p = 0` the linear source is `N m a`, and the quadratic term is `−(N/2) m²⟨1/E⟩ a²`.
- **(T5) Static response under block 55's ledger.**
  - The chessboard's total curvature is `B0 = 12/γ − m²⟨1/E⟩`.
  - The static chessboard solves `m + (12/γ) tanh a = m² sinh a ⟨1/E(a)⟩`, with `E(a) = √(|s|² + m² cosh² a)`.
  - Its amplitude is `a* = −m/B0 + O(m³)`.
  - It is locally stable along the chessboard iff `γ m²⟨1/E⟩ < 12`. This holds whenever `|m|γ < 12`.
  - The ledger is bounded below along the chessboard iff `|m|γ ≤ 6`.
- **(T6) Block 76's sea-only reading.** `E_sea` is strictly monotone along the chessboard, so there is no static chessboard: the chessboard runs away towards `a → −sign(m)·∞`.

## (2) Steps

### Step 1 — T1 (PROVED; CHECKED F1)

*The twin map* (block 160 T1c, re-proved). Let `Θ = εT`, with `(Tψ)_x = ψ_{x−e₁}`.
- `THT⁻¹ = H`, `TεT⁻¹ = −ε` and `εHε = −H`, so `ΘH_mΘ⁻¹ = −H_m`.
- `Θ` carries diagonal clocks to `Tφ`, so `ΘH_w(φ)Θ⁻¹ = −H_w(Tφ)`.
- So `Θ` maps the sea of `φ` onto the positive levels of `Tφ`. The gap `2|m|·min φ² > 0` means no level sits at zero.
- Also `e_x[Θψ; Tφ] = −e_{x−e₁}[ψ; φ]`.

*The sum rule.* Summed over all levels, `Σ_all e_x = Re tr_spin(H_w)_xx = 2m w_x ε_x`, because `φHφ` has no on-site block.

*Combining.* `e^sea_x[Tφ] = 2mε_x w^{(Tφ)}_x − e^pos_x[Tφ] = 2mε_x w_{x−e₁} + e^sea_{x−e₁}[φ]`. ∎

F1 checks this for a random field (`|u| ~ 0.5`) on the `6³` torus, to 10⁻¹⁴.

### Step 2 — T2 (PROVED; CHECKED F2)

*Linearising T1.* The Hessian `R` (`δe = R δu`, with `e0 = mε − ⟨E⟩`) satisfies `[R, T] = 2m εT`.
- The uniform-clock sea is invariant under even translations. So `R = A + εB`, with `A` and `B` translation invariant (they keep `q`, and shift `q` by `Q`, respectively).
- Then `[A, T] = 0` and `[εB, T] = 2εBT`. Hence `B = m·Id`.

*Consequence.* `K(u, v) = ⟨u, Av⟩ + m Σ_x ε_x u_x v_x`, and `Â(q) = (K(cos, cos) + K(sin, sin))/N`.

F2 checks, on the `6³` torus (m = 0.7), to 10⁻¹⁰:
- `Â(q)` equals block 160's T2(b) zone formula at every momentum, including `2q ≡ 0` and `2q ≡ Q`;
- the decomposition holds for random `u` and `v`;
- the cross-coupling `K(cos(p·x), ε cos(p·x))/(N/2) = m` at three momenta.

*The formula for `Â`.* It is block 160's T2(b), a harvest refereed by #9295. It is ASSUMED as that input and verified here at every torus momentum (the scratch also covered `8³`).

### Step 3 — T3 (PROVED; CHECKED E1)

*Proof.*
- With `φ = e^{(b + aε)/2}`, `φ_xφ_y = e^b` on every bond, because neighbours have opposite `ε`.
- `w = e^b(cosh a + ε sinh a)`. So `H_w = e^b(H + m cosh a ε + m sinh a)`.
- `{H, ε} = 0` and `H²` is the momentum multiplier `|s|²`, spin-trivial. So `(H_w − e^b m sinh a)² = e^{2b}(|s|² + m² cosh² a)`.
- Exactly `N` levels are negative, because `|m sinh a| < |m| cosh a`.

*Check.* E1 verifies the matrix identities exactly (Gaussian integers, `4³` torus, `m = 1`, `e^b = 3`, `e^{a/2} = 2`), including building `H_w` from `φ`.

### Step 4 — `u = aε + v`, `v` smooth (PROVED from Steps 2–3)

*Second-order energy.*

    E_sea = E0 + Nma + Σ_x(mε_x − ⟨E⟩)v_x
          + ½[−N m²⟨1/E⟩ a² + 2am Σ_x v_x + ⟨v, Av⟩ + m Σ_x ε_x v_x²] + O(3).

- The chessboard couples at second order only to the mean of `v`, with strength `m`. This agrees with T3's factor `e^b`.
- A smooth mean-zero `v` is untouched by the chessboard at this order.
- With `Σu` fixed (block 55), the chessboard decouples from every smooth mode.

### Step 5 — T4 (PROVED; CHECKED E2, E6, E7, F3)

*`Â(Q)`.* At `k″ = k + Q`, `E″ = E`, so the non-held term of block 160's formula vanishes. The held part is `c0 + κ|q|²_lat` exactly, so `Â(Q) = c0 + 12κ`. Pointwise, `−E + |s|²/E = −m²/E` (E2).

*Near `Q`.* Pointwise, `held(Q+p) − held(p) = ½(E + E′) s·s′/(EE′)` (E6). Its zone average is `4κΣ_j cos p_j = 12κ − 2κ|p|²_lat`.

*The non-held term.* `1 − n·n″ → 2|s|²/E²` stays nonzero, so this term is `O(p²)` near `Q`, not `O(p⁴)`. Its `t²` coefficient (`p = t e₁`) is exactly `−|s|² s₁² cos²k₁/(4E⁵)` pointwise (E7).

*Isotropy.* Cross terms `s_i cos k_i s_j cos k_j` (`i ≠ j`) average to zero, and cubic symmetry gives equal diagonals. So the `p²` term is isotropic.

*Check.* F3 (quadrature, m = 0.7) gives `κ = 0.085813`, `λ = 0.009033`. The slopes approach `−0.09485` in three directions.

*The modes.* For `u = a cos(q·x)`, `q = Q + p`: the linear term `Σ(mε − ⟨E⟩)u = a m Σ cos(p·x) = 0` when `p ≠ 0`. The quadratic term is `(N a²/4)Â(Q+p)`, because the `mε` part gives `(m/2)Σ_x ε_x cos²(q·x) = 0` unless `2q ≡ Q`.

### Step 6 — T5 under block 55's ledger (PROVED; CHECKED E3, E5, F4)

*The field energy along the chessboard.*
- `F = (24N/γ) sinh²(a/2)`: every one of the `3N` bonds has `|φ_x − φ_y| = 2 sinh(|a|/2)`.
- `F`'s quadratic kernel is `|q|²_lat/γ`, which is `12/γ` at `Q`.

*Symmetric criticality.*
- `L` and the constraint `Σu = const` are invariant under even translations, which act transitively on each parity.
- So the constrained gradient at `aε` is `g_± = ∂L/∂u_x` on the two parities, and stationarity is `g₊ = g₋`, which is `dL(aε)/da = 0`. The multiplier is `μ = (g₊ + g₋)/2 = L/N` (block 55's homogeneity).

*The chessboard.*
- `dL/da = N cosh a [m − m² sinh a ⟨1/E(a)⟩ + (12/γ) tanh a]` (E3).
- Linearising: `a* = −m/B0`.
- `B0 = 12/γ − m²⟨1/E⟩`, and `m²⟨1/E⟩ ≤ |m|` increases strictly with `|m|` (E2). So `B0 > 0` whenever `|m|γ < 12`, and there is a unique threshold beyond which `B0 < 0`.

*Global behaviour along the chessboard.*
- As `a → −sign(m)·∞`, `e^{−|a|} L/N → 6/γ − |m|`. E5 checks this from both sandwich bounds `|m| cosh a ≤ E(a) ≤ |m| cosh a + |s|²/(2|m| cosh a)`.
- In the other direction `F` dominates.
- So the ledger is bounded below along the chessboard iff `|m|γ ≤ 6`. At equality the limit is finite, `−12/γ`.

*Examples* (F4, `γ = 1`). For `m = 0.7`, `3` and `5.9`, each static equation has exactly one root, of sign `−sign(m)`: `−0.0602`, `−0.339` and `−2.03`. The linear values are `−0.0602`, `−0.325` and `−0.948`.

*Modulated chessboards.* On the pair (`cos p·x`, `ε cos p·x`) the total Hessian is

    [[Â(p) + |p|²_lat/γ,  m], [m,  Â(Q+p) + (12 − |p|²_lat)/γ]].

The chessboard entry is `B0 − (κ + λ + 1/γ)|p|² + O(p⁴)`. So `Q` is where the chessboard entry peaks: modulated chessboards are softer.

### Step 7 — T6 under block 76's sea-only reading (PROVED; CHECKED E4)

- `dE_sea/da = N m cosh a [1 − m sinh a ⟨1/E(a)⟩]`.
- Pointwise, `(m sinh a)²/E(a)² ≤ tanh² a < 1`, with difference `|s|² sinh²a/(cosh²a E(a)²) ≥ 0`.
- So `E_sea` is strictly monotone along the chessboard, with sign `sign(m)`. No static chessboard exists, and `E_sea → −∞` as `a → −sign(m)·∞`.
- The sea-only curvature at `Q` is `−m²⟨1/E⟩ < 0`.

## (3) Where it stops

- **The smooth sector.** At fixed `Σu`, the smooth diagonal `Â(p) + |p|²/γ → c0 = −⟨E⟩ < 0` as `p → 0`. This is the volume term of blocks 147 and 160, and it is present with or without the chessboard. So the closed-lattice static state is a saddle of the ledger in long-wavelength smooth directions.
- **Scope of "stable".** T5's stability is stated along the chessboard, the only direction the sea's source drives, and for the modulated chessboard entry. It is not a statement about the whole Hessian.
- **The `O(p⁴)` terms near `Q`.** They are not computed. The quadrature shows a small anisotropy at order `p⁴`.
- **The chessboard at nonzero `a*`.** The Hessian there is computed only to leading order in `m`.
- **The projected sea** (block 78) is not treated.

## (4) What would finish it

- **(i)** The full constrained Hessian at the static chessboard `a*`, with the smooth sector's negative volume mode resolved by whatever clause fixes the zero of energy (block 147).
- **(ii)** The `p⁴` term near `Q`.
- **(iii)** The same analysis for block 78's projected sea.

## ASSUMED

- The supplied clauses: the walk, mass, clocks, sea and the ledger `F`.
- Block 160's T2(b) formula for the translation-invariant kernel. It is refereed (#9295) and verified numerically here at every torus momentum.
- Standard second-order perturbation theory for a gapped finite matrix. The gap is `2|m|` at uniform clocks.

## Reproduce

```bash
python3 probes/work/derive/the-massive-sea-at-the-chessboard-momentum/w-jonathonsmac4f50-j27ac/check.py
```

The run takes about 12 s.
