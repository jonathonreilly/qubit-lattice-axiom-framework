# the-sixteen-branches-and-the-ledger-with-a-staggered-mass: attempt a1

Worker `w-macbookpro9927a-j17cc` (claude-opus-5-5). Every clause is supplied and nothing is adopted.

## Sources and provenance

**Notes, read as landed on `origin/main` `60c5f194d940`.** `check.py` pins each note's SHA256 in its `Q` family.
- Block 70: the exchange maps, `V_nHV_n = s_nH`.
- Block 71: twins `A_n = ΘV_n` for odd `n`, `e_x[A_nψ] = −e_x[ψ]`.
- Block 76: the filled sea `E_− = Σ_{λ<0}λ`; T1, a chessboard of clocks is invisible; the Hessian annihilates `ε`.
- Block 77: T3, `φ(K+mε)φ = φKφ + mwε` and `(K+mε)² = K² + m²`; T4, the paired energies.

**Narrowings that control this attempt.**
- Block 77 as landed says: *"Numerical packet and massive-sea experiments are deferred."*
- Block 76 as landed calls its `c = −1.193` and `κ = 0.095` *"inputs, not derived sea coefficients."*
- So the task's quoted W3 range (`κ = 0.076–0.090` for `m ≤ 1`) is a deferred historical number, and nothing here builds on it. The same holds for block 76's executed normalisation: this attempt defines `Π` and `κ` itself (§1).

**Related work, disclosed.**
- **The prior attempt a2** (`w-jonathonsmac4f50-ja540`, the same model family on another machine; not refereed). It found:
  - the maps and the no-on-site-twin statement;
  - the twin `τε` with density `−e_{z−e₁}`;
  - the exact chessboard energy `E_sea(a)`;
  - floating `κ(m)` on the `24³` torus, with the asymptote `1/(8m)` from second order in `1/m`.

  I formed my own plan before reading it. Parts (a), (b) and (d) below coincide with a2's and are re-derived independently here. The new content is:
  - the sea's exact energy density;
  - the exact second-order kernel of the massive free sea for all `m ≠ 0`;
  - the closed form of `κ(m)` with its exact consequences.

  The closed form reproduces a2's executed `24³` table to within `3·10⁻⁴` (`R6`).
- **My own earlier units.**
  - #8716 (held sea against free sea, massless): `κ_free = κ_held = I/12`, with the free−held kernel difference `O(q⁴ log q)`. This attempt extends that result to `m ≠ 0`.
  - #8697 (the rest energy density of a massive walker): the massive walker feels a chessboard of clocks.
  - #8721 (block 77's spectrum).

## 1. The statement attempted

**Objects.**
- The walk is `H = Σ_a σ_a S_a` with `S_a = (T_a − T_a⁻¹)/(2i)`, on an even torus or on `Z³`.
- `ε_x = (−1)^{x+y+z}` and `H_m = H + mε` with `m ≠ 0` real. The clocked walk is `H_w = φH_mφ = φHφ + mwε`, with `w = φ² = e^u` (block 77 T3).
- `E(k) = √(|s(k)|² + m²)`, where `s = (sin k₁, sin k₂, sin k₃)`, and `⟨·⟩` is the zone average.
- The energy density is `e_x[ψ] = Re ψ_x†(H_wψ)_x` (block 55).
- The filled sea is `E_sea[u] = Σ_{λ<0} λ(H_w)`, block 76's `E_−`. The held sea `E_fix[u] = tr(P₋H_w)` keeps the uniform-clock projector `P₋`.

**Normalisation.** For `u = a cos(q·x)` with `2q ≢ 0` and `2q ≢ Q = π(1,1,1)`:

`E(a) − E(0) = Π(q) a² N + O(a³)`, `Π(q) = c₀/4 + (κ/4)|q|²_lat + O(|q|⁴)`, `|q|²_lat = Σ_j 2(1 − cos q_j)`.

This is the normalisation of #8716. At `m = 0` it gives `c₀ = −I` and `κ = I/12`.

**Claims.**

- **(a) Maps.**
  - Every exchange map `V_n` commutes with `ε`, so `V_nH_mV_n = s_nH + mε`. The four even maps commute with `H_m`. For the four odd maps, `εV_n` commutes with `H_m`.
  - **No map that commutes with `ε` is a twin.** Such a map A may act site by site (unitary or antiunitary), or permute sites without mixing the two parities. The site-diagonal part of `A H_m A⁻¹` is `mε`, not `−mε`.
  - In particular, block 71's twin `ΘV_n` fails with a mass: `e[ΘV_nψ] + e[ψ] = 2m w ε|ψ|²`.
  - `εT`, the one-site translation followed by the site sign, is a twin: `(εT)H_m(εT)⁻¹ = −H_m`. In a clocked field, `εT` carries a solution in the field `φ` to a solution of opposite energy in the translated field `Tφ`.
- **(b) Twin densities and the sea.**
  - **The twin.** `e_x[εTψ; Tφ] = −e_{x−e₁}[ψ; φ]` at every site, exactly: minus the original's density, displaced by one site.
  - **The filled sea's density (new).** At uniform clocks, exactly: `e_x^sea = mε_x − ⟨E⟩`. Its alternating part is exactly `m`, whatever the band structure.
- **(c) The massive sea's stiffness (new).**
  - For every `m ≠ 0` the free sea's second-order kernel is, exactly:

    `Π(q) = −⟨E⟩/4 + (κ(m)/4)|q|²_lat − (1/16)⟨(1 − n·n′)(E − E′)²/(E + E′)⟩`.

    Here `n = (s, m)/E ∈ S³`, and primes denote evaluation at `k + q`.
  - The last term lies in `[−9|q|⁴/(64|m|³), 0]`.
  - Hence `c₀(m) = −⟨E⟩` and
    ```
    κ(m) = (1/12) ⟨ |s|² / √(|s|² + m²) ⟩ .
    ```
  - `κ(m) > 0` and strictly decreasing in `|m|` for all `m`.
  - `κ(m) → I/12 = 0.0995` as `m → 0`, matching #8716's massless value.
  - For `|m| > √3`: `κ(m) = 1/(8m) − 7/(64m³) + 81/(512m⁵) − …`, a convergent alternating series with rational coefficients.
  - The heavy sea decouples like `1/(8m)`.
  - **The task's HIT condition, a sign change of `κ`, is excluded exactly.**
- **(d) The chessboard.** A mass removes block 76's zero mode.
  - For `w = e^{aε}`: `φHφ = H` (block 76 T1), but `mwε = m cosh(a) ε + m sinh(a)`.
  - Therefore `E_sea(a) = N m sinh a − Σ_k √(|s|² + m² cosh² a)` for all `a`, since no level crosses zero.
  - The first variation along the chessboard is `N m`, the chessboard component of (b)'s source.
  - The second variation is `−N m² ⟨1/E⟩`.

## 2. Steps

**S1 (PROVED; CHECKED M1–M3, S1).**
- `H` has only odd-displacement entries, so `εHε = −H` and `(H + mε)² = H² + m²` (block 77 T3). In the `(k, k+Q)` block, `M(k) = [[s·σ, m], [m, −s·σ]]` and `M(k)² = E²`.
- `P₋ = (1 − H_m/Ê)/2` with `Ê = √(H² + m²)`. `Ê` has only even displacements, commutes with `ε` and is translation invariant.
- The one-site translation obeys `THT⁻¹ = H` and `TεT⁻¹ = −ε`.

**S2 (PROVED; CHECKED M4, M5, M7).**
- By block 70 T1(b) and site-locality, `V_nH_mV_n = s_nH + mε`.
- For odd `n`: `ε(−H + mε)ε = H + mε`.
- `Θ = σ₂K` commutes with `H` and with `ε`. Hence `ΘV_n` (odd `n`) maps `H_m` to `−H + mε`.

**S3 (PROVED; CHECKED M2, M6). No twin commutes with `ε`.** Let `A` commute with `ε`, so that `AεA⁻¹ = ε`. For `AH_mA⁻¹ = −H_m` one would need `AHA⁻¹ = −H − 2mε`.
- **Site-by-site maps.** Such an `A` keeps `AHA⁻¹` free of site-diagonal blocks, because `H` has none. But `−2mε` is site-diagonal and nonzero. Contradiction.
- **Parity-preserving site permutations.** The same argument applies: the permutation maps diagonal blocks to diagonal blocks.

`εT` flips `ε`, and `(εT)H_m(εT)⁻¹ = −H − mε`.

**S4 (PROVED; CHECKED M8 exactly with rational `φ`, `m = 7/5` and a Gaussian-rational `ψ` on `4³`).**
- `T(φH_mφ)T⁻¹ = φ′Hφ′ − mw′ε` with `φ′ = Tφ`. Conjugating by `ε` gives `−H_w[φ′]`.
- For `χ = εTψ`: `χ_x = ε_xψ_{x−e₁}` and `(H_w[φ′]χ)_x = −ε_x(H_w[φ]ψ)_{x−e₁}`. So `e_x[χ] = −e_{x−e₁}[ψ]`.
- An eigenstate of energy `E` in the field `φ` becomes one of energy `−E` in the field `Tφ`.

**S5 (PROVED; CHECKED M9).** `ΘV_111 = Θε`. It reverses the hop part of `e_x` (block 71 T1(a)) and keeps the rest term `m w_x ε_x |ψ_x|²`, since `|Θεψ|² = |ψ|²` site by site. Hence `e[Θεψ] + e[ψ] = 2m w ε |ψ|²`.

**S6 (PROVED; CHECKED S2–S4). The sea's density.** `P₋H_m = (H_m − Ê)/2`, from `H_m² = Ê²`. So

`e_x^sea = tr_coin⟨x|P₋H_m|x⟩ = ½ tr_coin(mε_x I₂) − ½ tr_coin⟨x|Ê|x⟩ = mε_x − ⟨E⟩`.

The diagonal of `Ê` is uniform, since `Ê` is translation invariant. FLOAT check against the eigenvectors on `4³`: `< 10⁻¹²`.

**S7 (PROVED; CHECKED by K5 FLOAT). The held sea, exactly and to all orders in `u`.**

`E_fix[u] = β Σ_bonds e^{(u_x+u_y)/2} + Σ_x e^{u_x}(mε_x − m²J)`,

with `β = −⟨|s|²/E⟩/3` and `J = ⟨1/E⟩`.
- **Bonds.** The bond value `⟨x+e_j|P₋|x⟩` equals `−½⟨x+e_j|HÊ⁻¹|x⟩`: the term `mεÊ⁻¹` has no odd-displacement entries. It is the same on every bond.
- **Sites.** `tr_coin⟨x|P₋|x⟩ = 1 − mε_xJ`.
- **The kernel.** Expanding to second order gives

  `Π_fix(q) = 3β/4 − m²J/4 − (β/16)|q|²_lat`,

  because the site sum `Σ_x ε_x cos²(q·x)` vanishes for `2q ≢ Q`.
- **The same kernel perturbatively.** Its perturbative form `(1/8)⟨−½(E+E′)(1 + n·n′)⟩` reduces to this closed form by `⟨s(k)·s(k+q)/E(k)⟩ = ⅓⟨|s|²/E⟩ Σ_j cos q_j`.

**S8 (PROVED; CHECKED K1–K3, K5). The free sea at second order.** The gap `2|m|` makes the filled projector analytic in `a`, as does the second-order formula for the sum of the occupied levels.

- **Expansion.** `φH_mφ = H_m + V₁ + V₂ + O(u³)` with `V₁ = ½{u, H_m}` and `V₂ = ⅛{u², H_m} + ¼uH_mu`.
- **Matrix elements.** `⟨j|V₁|i⟩ = ½(λ_i + λ_j)⟨j|u|i⟩`.
- **Second-order energy.** Summing,

  `E₂ = −¼ Σ_{i,j occ}(E_i + E_j)|u_ij|² + ½ Σ_{i occ, j unocc} E_i(E_j − E_i)/(E_i + E_j)|u_ji|²`.

- **Projector traces.** `u = a cos(q·x)` couples block `k` to `k ± q` with amplitude `a/2`, and `tr[P_a(k)P_b(k′)] = 1 + ab(s·s′ + m²)/(EE′) = 1 + ab n·n′`.
- **Symmetrized.**

  `Π(q) = (1/8)⟨G⟩`, `G = −½[(E+E′)(1 + n·n′) + (1 − n·n′)(E − E′)²/(E + E′)]`.

  The first part is `Π_fix`. The second is the free sea's extra term.
- **FLOAT check.** Brute-force diagonalization of `φH_mφ` on the `4³` torus (`m = 0.7`, `q = (π/2,0,0)`) and the `6³` torus (`m = 1.3`, `q = (π/3,π/3,0)`) agrees with `(1/8)⟨G⟩` to `< 10⁻⁸`, including `E_sea/N = −⟨E⟩`.

**S9 (PROVED; CHECKED K4). The remainder is `O(|q|⁴)`.**
- **Gradient bounds.** `|∂_j n|² = cos²k_j(E² − sin²k_j)/E⁴ ≤ 1/m²` and `|∂_jE| = |sin k_j cos k_j|/E ≤ 1`.
- **Consequences.** So `1 − n·n′ = |n − n′|²/2 ≤ (3/(2m²))|q|²` and `(E − E′)² ≤ 3|q|²`, with `E + E′ ≥ 2|m|`.
- **The bound.** The extra term therefore lies in `[−9|q|⁴/(64|m|³), 0]`.

  So `κ = −β/4 = (1/12)⟨|s|²/E⟩` and `c₀ = 3β − m²J = −⟨E⟩`.

**S10 (PROVED; CHECKED R1–R3). Properties of `κ(m)`.**
- The integrand `|s|²/√(|s|²+m²)` is nonnegative, positive almost everywhere and strictly decreasing in `|m|`.
- Dominated convergence gives `κ(0+) = ⟨|s|⟩/12 = I/12`.
- **Series.** For `|m| > √3`, let `x = |s|²/m² ≤ 3/m² < 1`. Then `(1+x)^{−1/2} = Σ_j c_j x^j`, with `c_j = (−1)^j C(2j,j)/4^j`, alternating with decreasing terms. So the partial sums bracket the value at every point, and averaging with the weight `|s|²/(12m) ≥ 0` keeps the brackets.
- **Moments.** The moments are exact rationals: `⟨|s|²⟩ = 3/2`, `⟨|s|⁴⟩ = 21/8`, `⟨|s|⁶⟩ = 81/16`, …. This gives `1/(8m) − 7/(64m³) + 81/(512m⁵)`.
- **Enclosures.** The exact rational enclosures (width `< 10⁻¹⁰`) are `κ(2) = 0.0523181086715…` and `κ(4) = 0.0296806233061…`.

**S11 (FLOAT, labelled; R4–R6). Values.** Torus averages converge exponentially for `m > 0` (`32³` against `48³`: `< 10⁻⁹`).

| `m` | 0.25 | 0.5 | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| `κ(m)` | 0.09725 | 0.09160 | 0.07667 | 0.06298 | 0.05232 | 0.03816 | 0.02968 | 0.02035 | 0.01542 |

`c₀(m) = −⟨E⟩` is `−1.1938`, `−1.5687`, `−2.3415`, `−4.1827` at `m = 0, 1, 2, 4`. a2's brute-force free-sea values on `24³` agree within `3·10⁻⁴`. The small residual at `m = 0.25` is the torus's `O(q⁴/m³)` term at `q = 2π/24`.

**S12 (PROVED; CHECKED M10, D1). The chessboard.**
- For `φ_x = c^{ε_x}`, `φ_xφ_y = 1` on every bond, and `m w_x ε_x = m cosh(a)ε_x + m sinh(a)` with `a = 2 log c`.
- The levels are `±√(|s|² + m²cosh²a) + m sinh a`. Since `|m sinh a| < |m| cosh a`, no level crosses zero.
- Hence the closed form for `E_sea(a)`, whose first variation `Nm` and second variation `−Nm²⟨1/E⟩` (D1) follow by differentiation.
- The first variation equals `Σ_x ε_x e_x^sea` (S6), which is block 55's source reading.
- Block 76's parenthetical expected the zero mode to survive, because `ε` commutes with the chessboard rates. It does commute, but the rest term scales with `w`, so it is not invariant.

## 3. Where the route stops

No step of claims (a)–(d) fails. Not done:
1. the `|q|⁴` coefficient of `Π`;
2. the kernel at the chessboard momentum `q = Q`, where `2q ≡ 0` and the linear source of (d) enters;
3. the interacting (projected) sea of block 78;
4. whether any supplied ledger clause uses `κ(m)`.

With a mass, block 76's T4 comparator (`c + κL`, checkerboard denominator `c + 12κ`) is no longer ruled out by T1 at `q = Q`: the exact functional has a nonzero gradient there (d).

## 4. What would finish it

For the task as posed, nothing further is needed. The sign question is settled exactly, and the values at `m = 2, 4` are enclosed exactly. A next step would be the exact kernel at `q = Q`, together with the response of the rate field to the sea's chessboard source `mε`.
