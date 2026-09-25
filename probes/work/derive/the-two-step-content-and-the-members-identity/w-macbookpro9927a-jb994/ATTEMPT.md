# The two-step content and the member's identity, attempt 1: exact up to the factor Π cos q_l, and exact for all eight species after a corner average

Worker `w-macbookpro9927a-jb994` (Claude Opus 5.5, `claude-opus-5-5`). The checks are in `check.py` in this directory. They run in about 4 seconds with a peak of about 110 MB.

The families are:
- **Q**: pinned sources.
- **F**: the symbolic chain, exact (sympy).
- **T**: a torus with every field built on the lattice, `[float]`.
- **X**: certificates from lattice fields, exact.

Family X uses Gaussian rationals for the axis beat and exact algebraic numbers (sympy) for the three-dimensional beat.

## Sources, provenance and overlap

**Sources.**
- **Block 55**, main at `60c5f194`. The energy density is `e_x = Re[χ_x† (H_w χ)_x]`.
- **Block 69/73**, main. `P_j = S_jC_j` has symbol `½ sin 2k_j` and commutes with `H`.
- **Block 120**, PR #9173 at head `2c7d2337`. It gives the bond currents `J_a^j`, and `K_a^j` "the same with `P_j`". Its T4(b) realisation is `B_i^j = −½ φ_j h_ij` with `φ_j = ½(1 + T_j⁻¹)Π_{l≠j} C_l`.
- **Block 134**, PR #9193 at head `52e320a4`.
  - T1: at `β = −α`, the member demands `ë = −(Kw̄²/(4α)) p·Θ·p`.
  - T2: for a beat, `e_q = ½w̄(l + l′)u′†u` and `ë_q = −w̄²(l − l′)²e_q`.
  - T4: the six partly reflected species cannot be such content with block 62's stress.
- **The task**, from `probes/TASKS.json` at `6ae1dbc2`.

Family Q checks the hashes and the quoted lines.

**Provenance.** The claim printed no prior attempts at this problem. It builds on two of my own earlier results, harvested into the blocks it cites:
- **Block 120's T4**, the transposed law and the φ-realisation, came from my `deferred-20260924-ledger` a1, issue #9060.
- **Block 112's exact failure** for block 62's one-step stress came from my `the-dewitt-ratio-and-local-conservation` a2, issue #8921.

What is new here is the two-step stress in the identity: the exact factor, the repair, and the result for every species. I re-derive everything I use, and nothing is taken from those units as authority.

## Setting

**The walk.**
- `H = Σ_a σ_a S_a`, with `(T_a f)(x) = f(x + e_a)`, `S_a = (T_a − T_a⁻¹)/(2i)` and `C_a = (T_a + T_a⁻¹)/2`.
- The rates are uniform, and `w̄ = 1` throughout. Rates multiply every energy, so they cancel from the identity.

**The fields.**
- The energy density is `e(x) = Re ψ(x)†(Hψ)(x)` (block 55).
- The two-step bond current on `x → x + e_a` is `K_a^j = ½Re[ψ(x+e_a)†σ_a(P_jψ)(x) + (P_jψ)(x+e_a)†σ_aψ(x)]` (block 120).

**The stress `Θ₂`.**
- The content's Lagrangian coupling through block 120's realisation is `−⟨K, B⟩` with `B_i^j = −½φ_j h_ij`.
- I write it as `½ Σ Θ₂_ij h_ij`, with `h` in block 62's staggered placement (`h_ij` at `x + (e_i + e_j)/2`). This defines `Θ₂`, normalised like block 62's `Θ`: both tend to `ŝ_i k_j` at long wavelength.
- Equivalently, in the site placement: `p·Θ₂·p = −Σ_ij (e^{−iq_i} − 1)(e^{−iq_j} − 1) Θ₂^{site}_ij`. This is because `p_j e^{−iq_j/2} = i(e^{−iq_j} − 1)`, so no half-angle ever appears.

**A beat.**
- `ψ = u e^{i(k·x − lt)} + u′ e^{i(k′·x − l′t)}`, with `(σ·s)u = lu` and `(σ·s′)u′ = l′u′`, where `s = sin k` and `l = ±|s|`. Any of the eight species and either branch is allowed.
- `q = k − k′`, `p_j = 2 sin(q_j/2)`, `K̄ = (k + k′)/2` and `M_i = u′†σ_i u`.

## (1) The statement attempted

**Theorem.** For every beat, the `e^{iq·x}` components satisfy
- `−ë_q = ½(l − l′)²(l + l′) u′†u`;
- `p·Θ₂,q·p = Π_l cos q_l · ½(l − l′)²(l + l′) u′†u`.

That is:

`p·Θ₂·p = Π_l cos q_l · (−ë)` exactly.

**(a) The identity fails.** The identity `ë = −p·Θ₂·p` fails exactly by the factor `Π_l cos q_l`, for every species and both branches.
- *Axis certificate.* `k = (a,0,0)` and `k′ = (a′,0,0)`, with `sin a = 5/13` and `sin a′ = 3/5`, both positive branches. Then `e_q = 192/845`, `−ë_q = 37632/3570125` and `p·Θ₂·p = 2370816/232058125`. The ratio is exactly `cos(a − a′) = 63/65`.
- *Three-dimensional certificate.* Sines `(3/5, 5/13, 8/17)` and `(−3/5, 7/25, 12/13)`, branches `(+, −)`. The ratio is exactly `2793/105625 = Π_l cos q_l`.

**(b) The order of failure, and a repair.**

*The order.* `Π_l cos q_l = 1 − |q|²/2 + O(q⁴)`. So the relative defect is `|q|²/2`, and it is isotropic at that order. For two waves of one species, `ë` is itself `O(q²)`, so the absolute defect is `O(q⁴)`.

*The repair.* Adding a total difference to the energy density does repair it:

`e′ = (Π_l C_l) e`,

the average of `e` over the eight body-diagonal neighbours `x + (±1, ±1, ±1)`.
- It differs from `e` by `(C₁ − 1)e + C₁(C₂ − 1)e + C₁C₂(C₃ − 1)e`, with `C_j − 1 = ½(T_j − 1)(1 − T_j⁻¹)`: a sum of forward differences of local fields.
- It meets `ë′ = −p·Θ₂·p` exactly on every beat.
- The identity is bilinear in `ψ`. The terms at `q = 0` give `0 = 0`, and the factor is even in `q`. So `e′` meets the identity on every state of every finite torus, and on every finite superposition of waves on `Z³`.

**(c) What it makes of α = K/4.** With `e′` as the rate field's source and `Θ₂` as the stress, block 134 T1's demand `ë′ = −(K/(4α)) p·Θ₂·p` is met by the walker's states exactly when `α = K/4`. This holds on the lattice, at every wave number, for all eight species, including the six partly reflected ones that block 134 T4 excludes for block 62's one-step stress.

Using `e′` is a supplied placement. It is equivalent to reading the rate field through the same corner average, since `Σ e′u = Σ e (Π C_l u)`. It mirrors the averaging `Π_{l≠j} C_l` already inside `φ_j`. Nothing is adopted.

## (2) Steps

**Step 1 (PROVED): the Fourier parts of the beat.**
- *The energy.* `Hψ` multiplies each wave by its own `l`. So the `e^{iq·x}` part of `Re ψ†Hψ` is `½(l + l′)u′†u`, as in block 134 T2. It oscillates as `e^{−i(l − l′)t}`.
- *The current.* `P_j` multiplies a wave by `π_j(k) = ½ sin 2k_j`. The two terms of `K_a^j` give the `e^{iq·x}` part

  `K_q = ¼(π_j(k) + π_j(k′)) M_a (e^{−ik′_a} + e^{ik_a}) = ½ e^{iq_a/2} cos K̄_a (π_j(k) + π_j(k′)) M_a`.

**Step 2 (PROVED): the staggered stress.**
1. The coupling is `−⟨K, B⟩ = ½ Σ_x K_i^j (φ_j h^{site}_ij)`, with `h^{site}_ij(x) = h^{st}_ij(x + (e_i + e_j)/2)`.
2. On the mode `e^{−iq·y}`, `φ_j` has symbol `½(1 + e^{iq_j})Π_{l≠j} cos q_l`, and the staggered offset gives the phase `e^{−iq·(e_i + e_j)/2}`.
3. So `Θ₂^{st}_ij(q) = K_q^{ij} cos(q_j/2) Π_{l≠j} cos q_l e^{−iq_i/2}`.
4. The bond midpoint's phase `e^{iq_i/2}` in `K_q` cancels the offset.

**Step 3 (PROVED; CHECKED, family F): the factorisation.**
1. `p·Θ₂·p = ½ (Σ_i p_i cos K̄_i M_i)(Σ_j p_j cos(q_j/2) Π_{l≠j} cos q_l (π_j + π′_j))`.
2. *The first factor.* `p_i cos K̄_i = 2 sin(q_i/2) cos K̄_i = s_i − s′_i`. So the first sum is `u′†σ·(s − s′)u = (l − l′)u′†u`, because `u′†(σ·s′) = l′u′†`.
3. *The second factor.* `p_j cos(q_j/2) = sin q_j`, and `sin q_j(π_j(k) + π_j(k′)) = cos q_j (s_j² − s′_j²)`, the identity used in block 120's proof. So the second sum is `Π_l cos q_l (|s|² − |s′|²) = Π_l cos q_l (l² − l′²)`.
4. Together these give the theorem.

**Step 4 (PROVED; CHECKED, family F): the order and the repair.**
- The series of `Π_l cos q_l`.
- The symbol of `Π_l C_l` is `Π_l cos q_l`, so `e′_q = Π_l cos q_l · e_q`.
- The total-difference decomposition, as an identity of symbols.

**Step 5 (PROVED): (c).**
- Block 134 T1 derives the demand from block 101's action at `β = −α`: the `u`-equation is the constraint `2Kw̄p²φ = e`, and the relabelling equation is `−8αφ̈/w̄ =` the stress projected on `p`.
- The same derivation applies with `(e′, Θ₂)` in place of `(e, Θ)`, because it uses only the source's projection on the relabelling direction and the energy source.
- By Step 4, the walker's pair `(e′, Θ₂)` satisfies `ë′ = −w̄² p·Θ₂·p` exactly.

**Step 6 (CHECKED): families T and X.**
- *T `[float]`.* On the `12³` torus, 40 random beats of both branches at all corners are built from lattice fields, with the aliased beats `2q ≡ 0` excluded. They reproduce `e_q`, `K_q` and the ratio `Π cos q_l`. The staggered and site test fields agree, and `e′` gives ratio 1. The maximum deviation is `7.6·10⁻¹⁴`.
- *X, exact.* The `e^{iq·x}` parts of `e` and of `K` are extracted from lattice values at three sites, by an exact Vandermonde solve. They give the two certificates in (a) and the repaired identity.

## (3) Where the route stops

1. **Beyond finite superpositions.** The theorem is stated per beat, so it covers every state of every finite torus and every finite superposition on `Z³`. Wave packets on `Z³` would follow by continuity, which is not written out here.
2. **The repair is a placement.** It uses `e′ = (Π C_l)e` as the source of the rate field. That is a supplied placement, equivalent to reading the rates through the corner average. Block 55's `e` itself fails by `Π cos q_l`.
3. **The coupling is assumed.** Block 120's realisation is assumed to enter the member's action in place of block 62's frame coupling, which is what block 120 proposes. The member's demand is block 134 T1's, at `β = −α`.
4. **Uniform rates.** Only `w̄ = 1` is treated. Nonuniform rates are not.

## (4) What would finish it

1. A clause that puts the rate field's source through the same local average as the strain's `φ_j`, so that `e′` is forced rather than chosen.
2. Block 112's constraint algebra with the two-step content `(e′, Θ₂)`.
3. Nonuniform rates, with `φ`-weighted clocks.
