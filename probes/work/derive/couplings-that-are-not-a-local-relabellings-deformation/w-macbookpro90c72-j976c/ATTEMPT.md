# J:derive:couplings-that-are-not-a-local-relabellings-deformation:a1 — worker w-macbookpro90c72-j976c

**Model:** claude-opus-5-5.

**Check:** `python3 probes/work/derive/couplings-that-are-not-a-local-relabellings-deformation/w-macbookpro90c72-j976c/check.py`
- sympy, mpmath and numpy; about 10 s.
- D1–D8 and D10 are exact. D9 reads the outputs of the executed search `search_exact_current.py` (driver `run_search_w2.py`, outputs `search_*.txt`).

**Provenance.**
- My plan was formed before I read attempt a2 (`w-jonathonsmac4f50-j0698`, same model family, another machine):
  - the division formula;
  - locality at the species momenta;
  - a no-go for reach two built on `U_(111)`'s reversal.
- I read a2's summary after D1–D9 were written.
- **Where a2 and I agree:**
  - a2 derived the same division formula (my S2).
  - On `Z³` it concluded that the generator is always local, with a real-algebraic step ASSUMED.
  - For (d) it gives a stronger route: the species average of the shear.
- **What this attempt adds:**
  - a proof of the locality step on `Z³` with nothing ASSUMED (S2(iv));
  - the torus reading made exact, with an explicit coupling whose current is exact on every torus of side `2q` but whose generator is not local (S3, S5). So the answer depends on which lattice "every stationary state" refers to;
  - the species momenta (S4);
  - an executed classification of nearest-neighbour couplings with an exact current (S6);
  - (d) by a separate route through `U_(111)`, which gives the exact geometry `D_n g D_n` (S8).
  - I also re-derive a2's species-average statement independently, in a few lines (D10), and credit it.
- **Overlap with my own earlier units:**
  - #8734 (a gradient relabelling symmetry in blocks 60–62);
  - #8815 (the walk in a frame, species signs).
  Nothing from either is reused.
- Blocks 63–75, a2 and this attempt are all from the Claude family. This needs a referee of another family.
- Definitions come from the notes of blocks 63, 64, 66, 69, 72, 73 and 74, read on their PR branches (#8593, #8595, #8597, #8601, #8605, #8606, #8607).

## 1. The exact statements attempted

**Conventions.** Block 63 has `(T_aψ)(x) = ψ(x + e_a)`, `S_a` with symbol `sin k_a`, and `C_a` with symbol `cos k_a`. The walk is `H(k) = σ·s(k)`, `s_a = sin k_a`, with energies `±|s(k)|`. It has eight zeros `πn`, and `D_n = diag((−1)^{n_a})`.

**Couplings.** A coupling `dH[B]` is hermitian, linear in a bond field `B_a^j`, translation-covariant and of finite reach.
- On gradients, `X = dH[dξ]`.
- For `ξ` a plane wave of wave vector `p`, `X` carries `k` to `k + p` through a 2×2 trigonometric polynomial `X_p(k)`.
- Write `H' = H(k+p)`, `Φ(X) = H'X + XH` and `Δ_p(k) = |s(k+p)|² − |s(k)|²`.

**(a) The generator.**
- The response is divergence-free on every stationary state ⟺ `X` has no block between equal energies ⟹ `X = i[H, G]`.
- For a plane wave, `G = −iΦ(X)/Δ`, with
  `Δ_p(k) = Σ_a sin p_a sin(2k_a + p_a) = (E(k+p) − E(k))(E(k+p) + E(k))`.
  This is the division by energy differences.
- `G` can be chosen local ⟺ `Δ` divides `Φ(X)`.
- **On `Z³`** (stationary states in block 63's sense: plane-wave pairs of equal energy), `Φ(X)` vanishes on the whole shell. Then `Δ | Φ(X)` jointly in `(k, p)`, and `G` is local.
- **On tori the hypothesis is weaker.**
  - On every torus of side `2q` (`q` prime ≥ 13), equal energies occur only for pairs related by the 384 symmetries of `|s|²`.
  - Locality is still forced at the eight species momenta and along the axes, but not at generic `p`.

**(b) Example.** The coupling on gradients `X = i[F̂, ξ]`, with `F̂ = e₂(cos 2k₁, cos 2k₂, cos 2k₃)`, has reach four.
- Its current is exact on every `2q` torus.
- It has no local generator.
- Its current is not conserved on `24³`.
- It fails demands 2 and 3.
- Among couplings of the form `i[Q, ξ]` with `Q` conserved, it has the least reach.
- Every nearest-neighbour coupling with an exact current is `i[H, ζ(ξ)]`, with `ζ` an on-site coin field. That is a local generator, and it makes no lengths.

**(c) Curls.** A coupling through the curls alone:
- vanishes on gradients;
- has a response that is divergence-free in every state;
- makes no lengths for uniform strains;
- leaves block 72's requirement unchanged.

**(d) Theorem.** No coupling of reach ≤ 2, of any kind, meets demands 2 and 3.
- The energy reversal by `U_(111)` forces odd hops, hence one-step hops.
- Species `n` then sees, for a uniform strain, `D_n(1 + b)ᵀ(1 + b)D_n`, with shear of the wrong sign for six species.
- Block 69's coupling meets both at reach three. So three is the least reach among **all** couplings, not only among relabellings.
- (a2's species average, re-derived in D10, removes demand 3 from the hypotheses.)
- **The task's HIT condition** (a reach-two coupling meeting all four demands) is refuted, so no HIT line is printed.

## 2. Steps

**S1. Conservation means no blocks between equal energies. PROVED.**
- On a torus the space is finite-dimensional.
- `∂⟨H[B]⟩/∂B` is divergence-free for the state `ρ` ⟺ `Σ_x ξ·div R = 0` for all `ξ` ⟺ `tr(ρ X) = 0` for every `ξ` (summation by parts).
- For all `ρ` commuting with `H`, this says `P_E X P_E = 0` for every eigenvalue `E`: X has no diagonal blocks.
- Then `G = Σ_{E≠E'} P_E X P_{E'}/(i(E − E'))` solves `X = i[H, G]`. It is unique up to operators commuting with `H`.

**S2. The division. PROVED; D1, D2.**
- (i) **The identity.** With `L(G) = H'G − GH`: `L∘Φ = Φ∘L = Δ·id`, because `H² = |s|²` (D1, symbolic).
  - So `X = iL(G)` forces `Δ G = −iΦ(X)`, i.e. `G = −iΦ(X)/Δ` wherever `Δ ≠ 0`.
  - Conversely, if `Δ | Φ(X)`, then `G := −iΦ(X)/Δ` satisfies `iL(G) = X` identically.
  - For `p ∉ πZ³` a polynomial `K` with `H'K = KH` vanishes. So `G` is local ⟺ `Δ | Φ(X)`.
- (ii) **The identity for `Δ`** (D1): `Δ_p(k) = Σ_a sin p_a sin(2k_a + p_a) = ½Σ_a [cos 2k_a − cos 2(k_a + p_a)]`.
- (iii) **On the shell** (`|s'| = |s| = r > 0`): `Φ(X)` has no cross-band blocks, and `P'_σ Φ(X) P_σ = 2σr P'_σ X P_σ` (D2). So "no block between equal energies at the pair" ⟺ `Φ(X) = 0` there.
- (iv) **Locality on `Z³`.**
  - *At fixed `p` with `sin p₃ ≠ 0`:* in `z₃ = e^{ik₃}`, `Δ` has constant leading and trailing coefficients `∓(1/4)(w₃² − 1)w₃^{…}`, which are units.
  - For `(k₁, k₂)` near `(−p₁/2, −p₂/2)`, its four roots in `z₃` are distinct and lie on the unit circle: `sin(2k₃ + p₃) = −R/sin p₃` with `|R| < |sin p₃|`.
  - `Φ(X)` vanishes at all four, because they are real points of the shell. So the remainder of dividing `Φ(X)` by `Δ` in `z₃` vanishes on an open set, and hence identically.
  - *Jointly in `(k, p)`:* the remainder over `C(w, z₁, z₂)` vanishes on an open real set of `p`, so it is zero.
  - `Δ` is primitive in `z₃` over `C[z₁^±, z₂^±, w^±]`: its `z₃²` coefficient `(w₃² − 1)` and its `z₃⁰` coefficient, which is free of `w₃`, have no common factor.
  - By Gauss's lemma, `Δ | Φ(X)` in the Laurent ring. So `G` is local, and of reach one less than the coupling.
  - This replaces a2's ASSUMED real-algebraic step. Nothing is assumed.

**S3. Which pairs are degenerate on a torus. PROVED; D3.**
- On a torus of side `2q` with `q` prime, `u_a = e^{2ik_a}` are `q`-th roots of unity. `|s(k)|² = |s(k')|²` says `Σ(u_a + u_a⁻¹) − Σ(u'_a + u'_a⁻¹) = 0`, a sum of 12 signed `q`-th roots of unity.
- Group the terms as `Σ_j c_j ζ^j` with integers `c_j`, `Σ|c_j| ≤ 12`. Since the minimal polynomial of `ζ` is `1 + x + … + x^{q−1}`, all `c_j` are equal. For `q ≥ 13` they are all zero, so the terms cancel in pairs.
- So the multisets `{u_a^{±1}}` and `{u'_a^{±1}}` agree. Since `−1` is not a `q`-th root, the inverse-pairs are recovered, and `k'_a ≡ ±k_{π(a)}` (mod `π`): `k' = g(k)` for one of the 384 symmetries (signed permutations and `π`-shifts).
- D3 confirms this at `q = 13` to 40 digits.
- **Consequences** for the torus reading of (a):
  - The conditions are `Φ(X)(k, g(k) − k) ≡ 0` for all 384 `g` (dense grid points, so polynomial identities), plus `X = 0` between zeros.
  - For `p` along an axis, the shell is a union of symmetry planes. Locality is forced there (S2(iv) with the planes).
  - For generic `p`, `g(k) = k + p` has solutions only for the `g` with `P − 1` invertible: finitely many points. Nothing forces `Δ | Φ(X)`.
- **Other tori.** On `24³` the pair `(π/3, 0, 0)`, `(π/6, π/4, 0)` is degenerate (`Σ cos 2k = 3/2` for both) but related by no symmetry (D3, exact). Rational coincidences of this kind (vanishing sums of 3rd, 4th, … roots of unity) add conditions on such tori.

**S4. The species momenta `p = πn`: locality is forced. PROVED; D4.**
- `sin(k + πn) = D_n sin k`, and `σ·(D_n s) = s_n R(σ·s)R†` with `R` the coin's half turn (D4, all seven `n`). So `X = iL(G)` becomes `X̃ = i(s_n HG̃ − G̃H)` at one wave vector.
- **`s_n = +1`.**
  - No same-energy blocks means `X̃ = σ·x` with `x·s = 0`.
  - `(sin k₁, sin k₂, sin k₃)` are, up to units, `z_a² − 1` in separate variables: a regular sequence. So Koszul's complex is exact, and `x = s × w` with `w` polynomial.
  - Direct proof for three elements: modulo `t₁` the relation gives `(x₂, x₃) ≡ c(t₃, −t₂)`, and then `x₁ = −(u₂t₂ + u₃t₃)`.
  - Then `G̃ = −σ·w/2` is local.
- **`s_n = −1`.**
  - The condition gives `X̃ = α + βσ·s`, with `β` polynomial (block 73 T1's divisibility).
  - The conditions at the zeros give `α(πm) = 0`, so `α` lies in `(s₁, s₂, s₃)`, which is the radical ideal of the eight zeros.
  - Then `G̃ = iβ/2 + σ·g` with `s·g = iα/2` is local.
- So the division by the inter-band gap `2|s|`, which vanishes at the zeros, is **not** an obstruction.

**S5. The example. PROVED; D5.**
- **The coupling.** `F(k) = e₂(cos 2k)` is unchanged by all 384 symmetries (D5 checks generators), and it is not a function of `|s|²`: at the `24³` pair, `e₁` agrees and `F` differs by `1/2`.
- `X = i[F̂, ξ]` has the kernel `i(F(k+p) − F(k))`, with hops of four steps (D5: the Fourier support has `|m|₁ = 4`).
- As a coupling, write each `F̂`-hop's `[T_m, ξ]` as a path sum of bond differences along a fixed axis order. That is local, hermitian (with the `i`) and translation-covariant.
- **Exact current on every `2q` torus.** By S3, the eigenspaces there are symmetry orbits, one band each, plus the zeros, where `F = 3`. So `F̂` is a function of `H`, `[ρ, F̂] = 0` for every stationary `ρ`, and `tr(ρX) = i tr([ρ, F̂]ξ) = 0`.
- **No local generator.** A local `G` would give `Φ(X) = iΔΓ` as polynomials. But at the `24³` pair `Δ = 0` while `Φ(X) = i f (H' + H) ≠ 0` (D5, exact).
- **Not conserved on `24³`:** the same-band block there is nonzero (D5).
- **Least reach within commutators.** Among `i[Q, ξ]` with `Q = a + cH` conserved (block 73 T1), conservation on `2q` tori needs `a` and `c` invariant.
  - The invariants are the symmetric polynomials in `cos 2k_a`.
  - A non-local generator needs `a` or `c` not a polynomial in `e₁` (otherwise `Q` is a polynomial in `H`).
  - The least reach is then `e₂`'s four, or five for `e₂H`.
- **The four demands.**
  - (1) Exact on `2q` tori; not on `24³`.
  - (2) A uniform strain adds `B·∇F` times the identity: no lengths.
  - (3) `F(k + π(1,1,1)) = F(k)`, so `U_(111)` does not reverse it.
  - (4) Its response is the flux of the scalar `F̂`, not a stress, so the requirement "stress gradient = weight" has nothing to hold.
  - It fails 2 and 3, and does not bear on (d).

**S6. Nearest-neighbour couplings with an exact current. Executed; D9.**
- **The search.** `search_exact_current.py` solves (C0) `X(k,0) = 0`, (C1) `Φ(X)(k, g(k) − k) ≡ 0` for all 384 `g`, and (C2) `X = 0` between zeros. The unknowns are the one-step kernels anchored in a window, and the solution uses singular values.
- **Window `{−1,0,1}³`:** dimension 1, with and without on-site terms. The solution is `i[H, ξ]`, the U(1) coupling.
- **Window `{−2,…,2}³`:** dimension 105, which equals the rank of the family `i[H, ζ]` with `ζ(x) = Σ_y Q_y ξ(x − y)` an on-site coin field and `Σ_y Q_y` scalar. That is 27 × 4 − 3. The family lies inside to `10⁻¹⁴`.
- So within these windows every nearest-neighbour coupling with an exact current has an on-site, local generator.
- **Covariance.** For a strain coupling, covariance forces `Σ_y Q_y = c_j` to be a vector, hence zero (block 73 T2(c)). A uniform strain then only turns the coin (`i[σ·s, σ·z] = −2σ·(s × z)`), with no lengths at first order.
- This is floating point; the windows are finite.

**S7. Curls. PROVED; D8.**
- `curl ∘ d = 0` (`d_ad_bξ = d_bd_aξ`), and the curl of a uniform field is 0 (D8, exact on `3³`). So a coupling through the curls vanishes on every gradient and on every uniform strain: no lengths.
- **Its response.** The response is `R = curlᵀ⟨V⟩`, so `div R = (curl ∘ d)ᵀ⟨V⟩ = 0` in every state.
- **Block 72's requirement.**
  - The requirement is the relabelling Ward identity: the pairing of the response with gradients, i.e. the stress gradient against the weight.
  - Adding a curl coupling adds nothing to `dH[dξ]`, so the requirement is unchanged.
  - (Block 66's corrigendum concerns curl-built *field* energies, not couplings to the content.)

**S8. (d): the theorem. PROVED; D6, D7, D10.**
1. **Odd hops.** `U_(111) = (−1)^{x₁+x₂+x₃}` multiplies a hop of `m` steps by `(−1)^m`. So `U(H + dH[B])U = −(H + dH[B])` for uniform `B` needs every hop of the uniform-strain symbol to be odd, and at reach ≤ 2 to be one step.
   - A two-step term such as `cos(k₁ + k₂)σ₃` is not reversed (D6).
2. **The species metric.** A one-step hermitian symbol is `Σ_b (α_b cos k_b + β_b sin k_b)`. Near `πn` its `σ` part is `(1 + εb̃)D_n q`, where `b̃_ab` is the `σ_a` part of `β_b` (D6, symbolic, all eight `n`).
   - The `α` terms move the node by `O(B)` and do not change the linear part at first order.
   - So species `n` sees `D_n(1 + b̃)ᵀ(1 + b̃)D_n`.
   - Its entry `(a, c)` changes sign for a species reflected along exactly one of `a`, `c`.
3. **Conclusion.** `(1 + B)ᵀ(1 + B)` for all eight species is impossible for any strain with shear. If only "the same for all" is asked, the coupling must be blind to shear: no angles.
4. **The ladder** (D7, exact symbols):
   - block 63's coupling (hops of 0 and 2 steps) is not reversed and shows `(1 + BD)ᵀ(1 + BD)`;
   - block 69's (hops of 1 and 3) is reversed and shows `(1 + B)ᵀ(1 + B)` to all eight.
   - So reach three is least for demands 2 and 3 among all couplings.
5. **Second route (a2's statement, derived here).** For any symbol of reach ≤ 2, the first-order shear metric averaged over the eight species vanishes.
   - The average keeps only the monomials `m ≡ e_a` (mod 2) with `|m|₁ ≤ 2`, i.e. `m = ±e_a`, which have no component along `e_c` (D10).
   - So equal shear for all species forces zero shear even without demand 3. At reach three `σ₁ cos k₁ ½ sin 2k₂` gives all eight the same shear (D10).
6. **Demand 1 does not rescue reach two.** By S6, the nearest-neighbour couplings with an exact current are `i[H, ζ]`, which make no lengths.

**ASSUMED:** nothing beyond standard algebra: Gauss's lemma, the exactness of Koszul's complex for a regular sequence (proved directly for three elements in S4), and the minimal polynomial of a root of unity of prime order.

## 3. Where the route stops

- **For the HIT question, nothing stops.** No reach-two coupling meets demands 2 and 3 (S8), and with S6 none meets demands 1 and 3 while making lengths.
- **What stays open.**
  - S6 is an executed classification in two finite windows, not a proof for all anchor spreads.
  - The "smallest example" of (b) is proved smallest only among commutators `i[Q, ξ]`. A smaller one of another form, or one exact on **all** tori and still non-local, is not excluded. It would need the Zariski closure of all rational degeneracies, from vanishing sums of 12 roots of unity.
- **Which lattice is meant.** The two readings of "every stationary state" give different answers.
  - With block 63's plane-wave pairs on `Z³`, the generator is always local (S2(iv)).
  - Along tori of side `2q` it is not (S5).
  - Block 64 T1's use presumably intends the former.

## 4. What would finish it

1. **A proof of S6 for every anchor spread.** Nearest-neighbour hops with an exact current would imply an on-site generator, perhaps via the conditions at `p = πn` and the reflection families.
2. **The Zariski closure of the degenerate pairs over all tori.** Does conservation on every torus force `Δ | Φ(X)`?
3. **A referee of another model family** for S2(iv), S3, S4 and S8.
