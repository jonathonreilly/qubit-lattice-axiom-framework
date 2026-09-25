# The exchange sign at fourth order in the crowd — attempt 1 of 2

- **Worker:** `w-macbookpro9927a-je6b5` (claude-opus-5-5).
- **Unit:** `J-derive-the-exchange-sign-at-fourth-order-in-the-crowd-a1`.
- **Checks:** exact checks are in `check.py` in this directory. Family letters (Q, A, C, V, L, B, G) refer to it.
- **Runtime:** about 90 s.

**Disclosure.**
- The parent result, harvest issue #8642, is this machine's own earlier attempt: `the-exchange-sign-from-the-coin:a1`, worker `w-macbookpro90c72-j3430`. It was refereed as confirmed by a different model family (grok-4.6, `w-macbookpro90c72-je52e`).
- This unit builds on its refereed statements:
  - the two composition rules satisfy every axiom sentence;
  - under exclusion the sign first appears at order 4;
  - the difference is `−8` per plaquette.
- Nothing here re-derives those. The fourth-order coefficients, the fixed-filling transform, part (b) and the ground-energy comparison are new.

**Sources, as landed on main.** They are pinned by commit and SHA-256 in family Q.
- Block 54 (`…A_PHASE_TIMED_BY_THE_LOCAL_CLOCK…_2026-09-21.md`) supplies the one-record generator: "Define (T_e psi)(x)=psi(x-e), D_j=(i/2)(T_j-T_j^dagger), and H=sum_e A_e T_e". The member used here, as in #8642, is `H = Σ_j σ_j D_j`. Its symbol is `Σ_j σ_j sin k_j`, and a hop has amplitude `1/2`.
- Block 78 (`…ONE_RECORD_PER_SITE_IS_AN_INTERACTION…_2026-09-22.md`) supplies the compression: the "fixed position projector P removing configurations with equal sites; this compression, tensor-product space and exchange rule are supplied model choices".
- Block 85 (`…THE_CROWD_UNDER_EXCLUSION_ALSO_GAINS…_2026-09-22.md`) calls this the crowd, and gives bond amplitudes `1+δ(−1)^{x_j}` for its alternation.
- Nothing is adopted; both exchange rules are supplied.

**The landed narrowings control part (b).**
- Block 80 as landed keeps fixed-state source identities and projector symmetries. Its scope says "no interacting-sea stiffness claim is retained". The task's "clock stiffness (block 80)" is therefore withdrawn wording.
- Block 85 as landed keeps concave nonincrease, the jam and four-ring examples. It adds "No derivative or quadratic susceptibility follows from concavity, and a cusp is allowed." The task's "bond-rate alternation's coefficient (block 85)" is not a landed quantity.
- I do not build on either withdrawn statement. For (b) I compute the fourth-order cluster coefficients of an alternation and of a clock modulation. These are new, well-defined objects, labelled as such.

## 1. Statement attempted

**What "the fourth-order cluster expansion of the crowd's ground energy" can mean.**
- The crowd's generator is a pure hop under exclusion. It has no small parameter and no gapped reference state, so the ground energy has no expansion in hop order.
- The orders of #8642 are hop counts: moments `tr H^k`. The expansion whose order-`k` term is built from `k`-hop clusters is the linked-cluster (high-temperature) expansion of `log Z` at fixed filling.
- Its coefficients are the per-site cumulants of the generator in the infinite-temperature state of that filling.
- Its `β → ∞` end is the ground energy, but no finite truncation determines it.

I therefore attempt three things:

- **(a1)** The exact per-site coefficients through fourth order on `Z³`, for both composition signs, at fixed filling `ρ = N/V`. Also: which sign lowers the free energy and the energy at the first order where the sign appears.
- **(a2)** Separately, and exactly: which sign lowers the ground energy, where that can be decided. It turns out that the fourth-order verdict does not carry over to the ground state.
- **(b)** Whether the sign changes the fourth-order coefficient of a bond-rate alternation, or of a clock modulation (a gradient, or "stiffness", term).

**Setting.**
- There are `N` records on the torus `(Z/L)³` (the limit `L → ∞` is `Z³`). Each record has a two-state coin, and there is at most one record per site.
- The generator is `P(Σ_i H_i)P` restricted to the symmetric sector `K₊` (`ε = +1`) or the antisymmetric sector `K₋` (`ε = −1`).
- Every configuration of distinct sites with coin labels gives exactly one state in each sector. So `dim K_{±,N} = C(V,N)·2^N` for both signs.
- In second quantization, `K₊` is two-component hard-core bosons and `K₋` is two-component fermions with at most one fermion per site. Hops onto occupied sites are removed (S1).

## 2. Steps

**S1 (PROVED). Second quantization.**
- The map from `Π_ε` (the (anti)symmetrizer on distinct-site, coin-labelled configurations) to the bosonic or fermionic Fock space is the standard one. `P H P` becomes `Ĥ = Σ_{x,j} [c†_x (−iσ_j/2) c_{x+e_j} + h.c.]`, restricted to occupations 0 or 1.
- Grand-canonical traces are `Ξ(z,β) = Σ_N z^N tr_{ε,N} e^{−βĤ}`, and `Ξ(z,0) = (1+2z)^V`.
- Locally, the fermion sign is a Jordan–Wigner string over the sites of a finite region. The trace of a closed product of number-conserving bilinears does not depend on the ordering chosen.

**S2 (PROVED; CHECKED A, C). The linked-cluster coefficients.**
- *The state.* At `β = 0` the state is a product over sites, with weights `1−ρ` (empty) and `ρ/2` for each coin, where `ρ = 2z/(1+2z)`.
- *Cumulants.* Write `Ĥ = Σ_b h_b` over bonds. Then `log⟨e^{−βĤ}⟩ = Σ_k (−β)^k κ_k / k!` with `κ_1 = ⟨Ĥ⟩ = 0`.
- *Odd orders.* `κ_3 = 0`: every hop changes the total coordinate parity of the records, and an exchange preserves it, so no closed 3-hop process exists (CHECKED A).
- *Second order.* `κ_2 = Σ_{b1,b2}⟨h1h2⟩`.
- *Fourth order.* `κ_4 = Σ_{b1..b4} K(b1,b2,b3,b4)`, with

  `K = ⟨h1h2h3h4⟩ − ⟨h1h2⟩⟨h3h4⟩ − ⟨h1h3⟩⟨h2h4⟩ − ⟨h1h4⟩⟨h2h3⟩`.
- *Only connected bond sets contribute.* Suppose the bonds of a sequence split into two site-disjoint groups. Their bilinears commute, and the product state factorizes. A group entered once or three times has zero expectation (odd hops). Two groups entered twice each are cancelled exactly by the matching pairing, and the other two pairings vanish.
- *Per site.* Anchor `b1` at the origin: `c_k = κ_k/V` is a sum over sequences whose first bond is anchored and whose bond set is connected.
- *Degree.* Every connected set of four bonds with five sites is a tree used once per bond, so it gives `K = 0` (CHECKED C). Hence `c_4` has degree at most 4 in `ρ`.

**S3 (CHECKED C). The coefficients on Z³.** The enumeration covers all connected sets of up to four bonds, 1,014 per anchor direction. Only 165 anchored four-bond sequences give `K ≠ 0`.
- `c_2 = (3/2) ρ(1−ρ)` for both signs.
- `c_4^{(+)} = ρ(1−ρ)(21 − 198ρ + 207ρ²)/8`.
- `c_4^{(−)} = ρ(1−ρ)(21 − 150ρ + 159ρ²)/8`.

Structural checks:
- `c_4(1) = 0` (the jam: every hop is blocked).
- The `O(ρ)` coefficient is `21/8`, the single-record fourth moment (CHECKED A: `H(k)² = Σ sin²k_j`, `m_4 = 3·3/8 + 6·1/4`).
- **`c_4^{(+)} − c_4^{(−)} = −6 ρ²(1−ρ)²`.** It comes from plaquettes only. Every non-plaquette sequence has the same `K` for both signs (CHECKED C).

The count behind the plaquette term:
- `tr(Π_ε X) = (1/N!) Σ_π ε^π tr(U_π X)`.
- At order 4 only transpositions contribute a sign. Three-cycles on a plaquette are even.
- The pair must sit on a plaquette whose other two corners are empty; this has weight `ρ²(1−ρ)²`.
- #8642's coin-summed ordered-pair amplitudes are `−1/2` per plaquette for an edge pair and `−1` for a diagonal pair. They total `−8` per plaquette.
- With the coin weights `1/4`, a factor `1/2` because each unordered pair appears as two ordered placements, and three plaquettes per site, the sign part of `c_4` is `ε·(1/2)·3·(1/4)·(−8)·ρ²(1−ρ)² = −3ε ρ²(1−ρ)²`.

**S4 (CHECKED V). Independent validation by brute force.**
- *Why the torus of side 5 is exact.* On it, no connected cluster of at most four bonds wraps. So `log Ξ = V[log(1+2z) + β²c_2/2 + β⁴c_4/24] + O(β⁶)` holds exactly there. It predicts `tr_{ε,N}((2H)²)` and `tr_{ε,N}((2H)⁴)` for every `N`.
- *What was compared.* Exact sparse traces over Gaussian integers match the predictions for both signs:
  - on the `5×5` torus for `N = 1, 2, 3, 4` (the same code in 2D; `N = 4` fixes all four coefficients);
  - on the `5³` torus for `N = 1, 2`;
  - on `5³` for `N = 3`, using translation orbits: `(V/N)` times the sum over states with a record at the origin.
- *Consistency with #8642.* The `5³`, `N = 2` fourth traces are `9135000` and `9183000`. These are #8642's `9135/496` and `9183/496` per state.
- *The 3D coefficients are fixed.* The degree bound plus `c_4(1) = 0` pin all of them from `N ≤ 3`.

**S5 (PROVED; CHECKED L). Fixed filling, and which sign lowers the energy.**
- *Legendre transform.*
  - The canonical `log Z_N/V` is the Legendre transform of `g(β,t) = log(1+2e^t) + β²c_2/2 + β⁴c_4/24`, with `t = log z`, taken at `∂_t g = ρ`.
  - Expanding the minimizer `t* = t₀ + β²τ` gives `log Z_N/V = s(ρ) + β²C_2/2 + β⁴C_4/24 + O(β⁶)`, with `C_2 = c_2` and

    `C_4 = c_4 − 3(∂_t c_2)²/∂_t ρ = c_4 − (27/4)ρ(1−ρ)(1−2ρ)²`.
  - Here `s(ρ) = −ρ log ρ − (1−ρ) log(1−ρ) + ρ log 2`.
  - CHECKED: the exact canonical `κ_4/V`, extracted from the validated series at `V = 400, 800, 1600` (`ρ = 1/4`), approaches `C_4` with the error halving each time.
- *The coefficients at fixed filling:*
  - **`C_4^{(+)} = −(3/8) ρ(1−ρ)(11 − 6ρ + 3ρ²)`**
  - **`C_4^{(−)} = −(3/8) ρ(1−ρ)(11 − 22ρ + 19ρ²)`**
  - Their low-density limit is `−33/8` per record, the single-record cumulant.
  - The correction is sign-blind, so `C_4^{(+)} − C_4^{(−)} = −6ρ²(1−ρ)²` as before.
- *Which sign lowers it.*
  - With `f = −β⁻¹ log Z_N / V` and `u = −∂_β log Z_N / V`:
    - `f_− − f_+ = −(β³/4) ρ²(1−ρ)² + O(β⁵)`;
    - `u_− − u_+ = −β³ ρ²(1−ρ)² + O(β⁵)`.
  - At the first order where the sign appears, the antisymmetric rule has the lower free energy and the lower energy, at every filling `0 < ρ < 1`.
  - Units: one hop has amplitude `1/2`, and `β` is in inverse units.

**S6 (PROVED; CHECKED B). Part (b): alternation and clock modulation.**

A bond factor `t_b` multiplies `h_b`, so each `K` scales by the product of its four bonds' factors. The pairings carry the same product.

- **Alternation.** Bond factors `1 + δ(−1)^{x_a}` on every axis, averaged over the 2×2×2 cell:
  - `c_2 = (3/2)ρ(1−ρ)(1+δ²)`;
  - `c_4^{(+)} = (3ρ(1−ρ)/8)[(69ρ² − 66ρ + 7)(1+δ⁴) + (114ρ² − 108ρ + 10)δ²]`;
  - **`c_4^{(+)} − c_4^{(−)} = −6ρ²(1−ρ)²(1+δ²)²`**. The plaquette's four bonds give `(1+δs_i)²(1+δs_j)²`, which averages to `(1+δ²)²`.
  - The `δ²` coefficients are:
    - `(3/4)ρ(1−ρ)(57ρ² − 54ρ + 5)` for `ε = +1`;
    - `(3/4)ρ(1−ρ)(41ρ² − 38ρ + 5)` for `ε = −1`.
  - The sign moves the fourth-order alternation coefficient by `−12ρ²(1−ρ)²`: the antisymmetric crowd gains more.
  - With one axis alternated, the sign part is `−2ρ²(1−ρ)²(3 + 2δ²)`.
- **Clock modulation.** Block 80's rates: bond factor `e^{(u_x+u_y)/2}`, with `u = η cos(k·x)`, at order `η²`, averaged over position.
  - A sequence contributes `(1/4)|Σ_s A_s e^{ik·s}|²`, where `A_s` is half the number of its bond endpoints at `s`.
  - `χ_2(k) = ρ(1−ρ)(12 − |k|²)/8`.
  - `χ_4^{(+)}(k) = (3ρ(1−ρ)/8)[(276ρ² − 264ρ + 28) − (36ρ² − 34ρ + 3)|k|²] + O(k⁴)`.
  - **`χ_4^{(+)} − χ_4^{(−)} = 4ρ²(1−ρ)²(|k|² − 6) + O(k⁴)`**. Per plaquette the factor is `|(1+e^{ik_i})(1+e^{ik_j})|²`.
  - The gradient ("stiffness") coefficient therefore also changes with the sign at fourth order.
- These are high-temperature cluster coefficients, not the ground-state response that blocks 80 and 85 no longer claim.

**S7 (PROVED; CHECKED G). The ground energy: the fourth-order verdict does not carry over.**

(i) *Two records are sign-blind.*
- On `Z³` the lowest one-record level is `−√3`, at the 8 points `k = (±π/2)³`.
- Compression cannot go below the free minimum. So both sectors have two-record infimum `≥ −2√3`.
- Two separated wave packets reach it in either sector, since (anti)symmetrizing disjoint supports changes nothing. So the infimum is exactly `−2√3` for both signs.

(ii) *An upper bound for the symmetric rule.* Take `L` divisible by 4. The hard-core boson state `Φ_N = Σ_{|X|=N} Π_{x∈X} e^{ik₀·x} |X; χ…χ⟩`, with `k₀ = (π/2)³`, has energy exactly

  `⟨Φ_N|H|Φ_N⟩/⟨Φ_N|Φ_N⟩ = [N(V−N)/(V−1)] · χ†(σ₁+σ₂+σ₃)χ / χ†χ`.

- Proof: a hop from `y` to an empty neighbour `x` maps `X` to `X − y + x`, with phase ratio `e^{ik₀·(y−x)}` and coin overlap `χ†σ_jχ`. Each bond is crossed by `C(V−2, N−1)` configurations, and `C(V−2,N−1)/C(V,N) = N(V−N)/(V(V−1))`.
- CHECKED exactly on `4³` for `N = 2, 3` with three rational spinors.
- The lowest eigenvalue of `σ₁+σ₂+σ₃` is `−√3`. Hence **`E₀^{(+)}(N) ≤ −√3·N(V−N)/(V−1)`**.

(iii) *A lower bound for the antisymmetric rule.*
- `K₋` compressed is a subspace of the free antisymmetric space. So **`E₀^{(−)}(N) ≥ E_FF(N)`**, the sum of the `N` lowest one-record levels `−|d(k)|`, with `|d|² = Σ sin²k_j`.

(iv) *A finite certificate.*
- On `8³` the shells are `|d|² = 3, 5/2, 2`, with 8, 48 and 120 states.
- Interval arithmetic certifies `E_FF(N) > −√3·N(V−N)/(V−1)` exactly for **`N = 11, …, 35`** (`ρ` from 0.021 to 0.068). There, **`E₀^{(+)} < E₀^{(−)}`**: the symmetric rule has the lower ground energy.
- For `N = 11` the margin is `0.07988…`.

(v) *The thermodynamic limit (L ∈ 4Z).*
- *Measure bound.* `|d(k)| ≥ √3 − ε` forces `Σ cos²k_j ≤ 2√3 ε`. By Jordan's inequality `|sin q| ≥ 2|q|/π`, this confines `k` to 8 balls of radius `(π/2)(2√3ε)^{1/2}`. So the fraction of lower-band levels within `ε` of the bottom is at most `A ε^{3/2}`, with `A = (π/6)(2√3)^{3/2}`.
- *Free-fermion bound.* The bathtub principle then gives `e_FF(ρ) ≥ −√3ρ + (3/5)A^{−2/3} ρ^{5/3}`. Finite-`L` lattice-point counts add `O(1/L)` at fixed `ε`.
- *Conclusion.* `limsup E₀^{(+)}/V ≤ −√3ρ(1−ρ) < liminf E₀^{(−)}/V` for **`0 < ρ < ρ* = ((3/5)A^{−2/3}/√3)³ = 0.00365…`**.

So at low filling the ground state prefers the symmetric rule, the opposite of the fourth-order high-temperature verdict. The mechanism: bosons pay an exclusion cost of order `ρ²`, fermions a Fermi cost of order `ρ^{5/3}`.

## 3. Where the route stops

1. **No ground energy per site is obtained at any filling.**
   - The ordering is decided only at low filling: `ρ < 0.00365` in the limit, and `11 ≤ N ≤ 35` on `8³`.
   - Between these and the jam it is open.
   - The fourth-order cluster coefficients cannot decide it, and neither can any finite truncation.
2. **Part (b) concerns high-temperature cluster coefficients.**
   - The ground-state alternation response and the interacting-sea stiffness are not landed (blocks 80 and 85).
   - They are not computed here.
3. **Jordan's inequality and the bathtub principle are standard.**
   - I use them as stated, on `|q| ≤ π/2` and on finite sums of levels respectively.

## 4. What would finish it

- **The sixth-order coefficients.** These are the next sign-sensitive terms: six-hop exchanges, including transpositions around 2×1 rectangles and odd cycles. The same enumeration extends.
- **A sharper low-density comparison, to push `ρ*` up.**
  - A Jastrow trial state for the symmetric rule.
  - A lower bound for the antisymmetric rule that includes the exclusion.
- **The hole side near the jam.** A single hole permutes coins as it moves. The one-hole ground state of each rule is a Nagaoka-type problem with this coin.
- **The ground-state versions of (b).** They need an interacting ground state, and the landed notes keep none.

## Answers

- **(a)** In the linked-cluster expansion at fixed filling, through fourth order, on `Z³`, with hop amplitude `1/2`:
  - `log Z/V = s(ρ) + β²C_2/2 + β⁴C_4/24 + O(β⁶)`;
  - `C_2 = (3/2)ρ(1−ρ)`;
  - `C_4^{(±)} = −(3/8)ρ(1−ρ)(11 − 14ρ + 11ρ² ± 8ρ(1−ρ))`.

  The sign first enters here, through plaquette exchanges: `C_4^{(+)} − C_4^{(−)} = −6ρ²(1−ρ)²`. The antisymmetric rule lowers the free energy by `(β³/4)ρ²(1−ρ)²` and the energy by `β³ρ²(1−ρ)²` per site.

  The ground energy is a different matter. At low filling it is strictly lower for the symmetric rule: certified on `8³` for `N = 11…35`, and in the limit for `ρ < 0.00365`.
- **(b)** The sign changes both fourth-order coefficients:
  - the alternation's `δ²` coefficient, by `−12ρ²(1−ρ)²` with all axes alternated;
  - the clock-modulation gradient coefficient, by `+4ρ²(1−ρ)²|k|²`.

  The landed blocks 80 and 85 keep no ground-state version of either quantity.
