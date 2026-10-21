# Complete corrected argument: Finite arc representations and lattice bracket constructions

This is inspectable mathematical source. The canonical claim is limited to: Arc representation algebra and explicit finite/SLAC/bandlimited/FFZ constructions.

**Deferred continuation:** Terminal arbitrary-range relabelling exclusions, with their full proofs and scope conditions retained pending packet. Complete arguments are retained below, but terminal negative conclusions are not promoted until the required residual-matched packet is supplied and reviewed. This does not make the exact identities uncertain. Historical verification statements below describe the original campaign, not a fresh capture or audit verdict.


# No translation-covariant lattice relabelling algebra of any range closes like the continuum, and the uniform-lapse bracket needs a non-local Leibniz rule

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact within the stated premises. A fresh-context check of the same model family confirmed Theorem B and sharpened it to the arc lemma stated here, tightened Theorem A, and corrected Theorem C and the sine-algebra order; those corrections are built in. Nothing is adopted.

## Question

The companion scalar note (same PR) finds that the curvature member's `{G, C}` bracket with a supplied scalar fails exact lattice closure at `O(a²)`. The spin-½/spin-1 companion finds the same for its fields, and campaign block B19 finds that the lattice matter relabellings do not close among themselves. All of these are local discretisations. This note asks:

- Is non-locality necessary for exact lattice closure?
- Is it sufficient: does some non-local, translation-covariant relabelling algebra close exactly like the continuum vector fields?
- What do the standard non-local constructions (SLAC derivative, band-limited products) actually give?

## Answer

- **Non-locality is necessary** for the two sub-brackets tested. On Z, every finite-range discretisation fails them, and so does every summable one whose transport symbol (Theorem A) or density-product kernel (Theorem C) is non-zero on a dense set (Theorems A and C). On every torus, Theorem C also excludes every `D` once the density product has full support.
- **It is not sufficient.** A relabelling algebra of any range, with one generator per momentum, that closes exactly with field-independent structure constants (P2) and matches the continuum at the longest wavelength ((S)) has `Λ_2/Λ_1 ≤ 0`, never the continuum value 2, and no `Λ_n = nΛ_1` with `n ∉ {0, ±1}`, on any torus with `L ≥ 4` or on Z (Theorem B, arc lemma). Such algebras exist abstractly (B4): what is lost is the continuum spectrum beyond `|n| = 1`, not closure itself.
- **What SLAC and band-limited constructions give:** exact sub-brackets; exact closure on band-limited windows, which is not an operator identity; and an exact uniform-lapse Leibniz rule, but with a fully non-local lapse–strain coupling once ξ is non-uniform (floating point, unchecked).
- **Boundary case.** The 2D sine algebra closes exactly and non-locally; it contains no uniform translation, so Theorem B does not apply.

## Setup

- A relabelling map `ξ ↦ G[ξ]` is linear, injective and translation-covariant. On the L-periodic sector, `X_n = G[e^{2πinx/L}]`, `n ∈ Z_L`, and `D = X_0 = G[1]` is the uniform relabelling.
- **Grading.** Translation covariance and closure within `span G` give `[X_a, X_b] = c(a,b) X_{a+b}` with `c` antisymmetric, one generator per momentum. Write `Λ_n = c(0,n)`, so `[D, X_n] = Λ_n X_n`.
- **Continuum values.** For vector fields, `[e^{ipx}∂, e^{iqx}∂] = i(q−p) e^{i(p+q)x}∂`, so `Λ_n ∝ n` and `[X_1, X_{−1}] ∝ D ≠ 0`.
- **SLAC no-wrap transport** (L odd, `m = L//2`, density weight `w`): `Y_p e_k = (k̄ + w p̄) e_{k+p}` if `|k̄ + p̄| ≤ m`, else 0, with `k̄ ∈ (−L/2, L/2]`. The physical generator is `X_p = i(2π/L) Y_p`, which rescales every identity uniformly.

## Theorem B (main result): the arc lemma

**Premises.**
- **(P1)** `G` is linear, injective and translation-covariant on an L-periodic sector.
- **(P2)** The sector closes within `span G` under a Lie bracket, with field-independent structure constants. This makes it an `L`-dimensional complex Lie algebra with one generator per momentum. Adding generators trivially closes, and is outside the statement.
- **(S)** `Λ_1 ≠ 0` and `[X_1, X_{−1}] ≠ 0`: the continuum values at the longest wavelength.
- **In d > 1:** the statement is about the e₁ sector `ξ = ξ(x₁) e₁`. It also needs covariance under `x_j → −x_j` for `j ≠ 1`, so that the bracket of two e₁-sector fields has no transverse component. B14's `G_m` (the companion note's) satisfies this reflection premise.
- **On Z:** the map must extend to periodic ξ with pointwise structure constants `c(k,q)`, so that each L-periodic sector is a subalgebra.
- **Not used:** locality, bilinearity of `G` in the fields, a particular lattice bracket, or the hypothesis (Z) `Λ_n ≠ 0`.

**Conclusion.** Under (P1), (P2) and (S):
1. `[X_1, X_{−1}] = c(1,−1) D`, and `Λ_{−1} = −Λ_1` is forced. With `H = 2D/Λ_1`, `E = X_1` and `F = κ X_{−1}`, `κ = 2/(Λ_1 c(1,−1))`, the three span an `sl2`.
2. **Arc lemma.** `δ_n = w_n − 2n mod 2L`, with `w_n = 2Λ_n/Λ_1`, is a `Z_{2L}`-grading. Each δ-component is a single irreducible `sl2`-module, whose weight vectors are the `X_n` on an arc of consecutive momenta. `{−1, 0, 1}` is the adjoint arc, so for `L ≥ 4` the path `{2, …, L−2}` is cut into arcs `[n₀, n₀+m]`, and on each arc

   `Λ_n / Λ_1 = n − (n₀ + m/2)` (momentum minus arc centre).
3. **Corollaries.**
   - (i) `2Λ_n/Λ_1 ∈ Z`.
   - (ii) `Λ_n/Λ_1 ∉ n + LZ` for `n ∉ {0, ±1}`, so `Λ_n ≠ nΛ_1`.
   - `Λ_2/Λ_1 ∈ {0, −½, …, −(L−4)/2}`, so `Λ_2/Λ_1 ≤ 0`: the second mode moves opposite to the first.
   - The physical requirement is weaker than matching the continuum, and it still fails: `Λ(2k)/Λ(k) ≤ 0` at every `k = 2π/L` (L ≥ 4) at which (S) holds, so even `Λ(2k)/Λ(k) → 2` is excluded.
4. **L = 3 is a genuine exception:** the algebra is `sl2` itself, and no second mode exists.

**Reading.** A finite-dimensional translation-covariant algebra with one generator per momentum and constant structure can carry the Witt pattern only on its `sl2` core. Everything else is a sum of `sl2`-irreducibles whose `D`-eigenvalues are centred on their own arcs, not proportional to momentum.

**Proof sketch.**
- *The sl2.* `[X_1, X_{−1}] ∝ X_0 = D` by the grading, and it is non-zero by (S). Since `ad_D` is a derivation, `[D, [X_1, X_{−1}]] = (Λ_1 + Λ_{−1})[X_1, X_{−1}]`; the left side is `c(1,−1)[D, D] = 0`, so `Λ_{−1} = −Λ_1`. The `sl2` relations then follow by direct computation.
- *Integer weights.* `g` is a finite-dimensional `sl2`-module under `ad`; by Weyl's complete reducibility over C its `H`-weights are integers, and each `X_n` is a weight vector of weight `w_n`.
- *The grading δ.* `w` is additive on nonzero brackets because `ad_H` is a derivation, and `2n mod 2L` is additive by the momentum grading. So δ is additive. `ad_E` raises `(n, w)` by `(1, 2)` and `ad_F` lowers it by the same, so each δ-class is an `sl2`-submodule.
- *One irreducible per class.* Within a δ-class, `w ≡ 2n + δ mod 2L` fixes `n mod L` for each weight, so every weight has multiplicity ≤ 1 (one generator per momentum). All weights in a class have the parity of δ. Two irreducibles of equal parity would share weight 0 or weight ±1. Hence each class is a single irreducible `V_m`, and its weight vectors sit on consecutive momenta, since `E` raises the momentum by 1.
- *The arcs.* The class of `X_0` contains `E` and `F`, so it is the adjoint `V_2` on `{−1, 0, 1}`. The remaining classes are disjoint arcs in `{2, …, L−2}`. On an arc with top momentum `n₀+m` and highest weight `m`, `w_n = m − 2(n₀+m−n)`, which gives the formula.
- *Corollaries.* (i) holds because weights are integers. For (ii), `Λ_n/Λ_1 − n = −(arc centre)`, and the centre lies in `[2, L−2]`, so this difference is never in `LZ`. The `Λ_2` set follows because 2 is the bottom of an arc `[2, 2+m]` with `0 ≤ m ≤ L−4`.
- *The original route (worker).* `φ = τ ∘ exp(iπ ad_H/L)` is an automorphism. Here `τ(X_n) = e^{−2πin/L} X_n` is the grading automorphism, and `φ(X_n) = exp(iπ(w_n − 2n)/L) X_n`. The fixed algebra `g^φ` contains the `sl2`. Its weight-0 space is `C·D`: an `X_n` with `Λ_n = 0` and `n ≠ 0` has eigenvalue `e^{−2πin/L} ≠ 1`. It has only even weights, so it equals `sl2`, and every other `X_n` lies outside it. This gives (i) and (ii); the arc lemma refines it.

**Exact certificates (runner Part B).**
- **B0** (checker's generator): `Λ_{−1} + Λ_1` lies in the Jacobi ideal under (S), for L = 4–7.
- **B1** (checker's generator, no (Z)): over a 20-point rational grid, the consistent `Λ_2/Λ_1` values equal the arc prediction for L = 4–7 (L = 8 with `--slow`).
- **B2** (checker's generator): the lex-elimination projection of the variety onto `(Λ_2, …, Λ_{L−2})` is finite and equals the set of arc partitions, for L = 4–7. This is the full necessity statement at those sizes, without a grid.
- **B3** (worker's generator):
  - (S) with `Λ_2 = 2` is inconsistent (Gröbner basis `[1]`) for L = 4–9, both with (Z) and without it. With `--slow`, L = 10 with (Z) is added.
  - The SLAC spectrum `Λ_n = n̄` on the whole zone is inconsistent for L = 5, 7, 9.
  - At L = 5 with (Z), the elimination ideal in `Λ_2` is `Λ_2 + ½`.
- **Controls** (consistent): L = 3 (`sl2`, the exception); `sl2 ⋉ C²` (special affine) at L = 5 with `Λ_{±2} = ∓½`, which shows that (i) is sharp; and L = 4 with `Λ_2 = 0`.
- **B4** (sufficiency; new path written for this consolidation):
  - Every arc partition, for L = 3–12, is realised exactly as `sl2 ⋉ (⊕ V_m)` with abelian radical: one irreducible per arc, rational structure constants, and cyclic Jacobi checked over all triples.
  - On each, `Λ_n` = momentum minus arc centre, the φ-fixed momenta are exactly `{0, ±1}`, and δ is additive.
  - So the arc set is attained, not merely an upper bound.
  - These are abstract graded algebras. Whether any is realised by relabellings of a lattice field is not claimed.
- **Scope of the certificates.** The campaign's "L = 4–9" certificate used (Z); this runner adds no-(Z) certificates for L = 4–9 (B3_noZ). In the campaign, the no-(Z) checks covered L = 4–8 (checker) and L = 5–8 (worker). The general statement rests on the proof.

## Scope: structure functions and enlarged generator sets (campaign evidence, not certified by this runner)

Source: campaign block C9 and its same-family fresh-context check (`.claude/science/physics-loops/scale-ladder-campaign-20261018/C9_structure_functions_arc_lemma/ (unavailable historical pointer; not a proof premise)` and `C9_check/`, exact sympy and Gröbner certificates, PASS=79 and PASS=66). This note's runner does not certify these statements.

Theorem B uses (P2) in full: field-independent structure constants, and one generator per momentum. Without either, its conclusion fails.

- **Structure functions.** Weaken (P2) to closure with field-dependent structure functions C_ab^e(Φ) on a translation-invariant open set. At a translation-invariant background Φ̄ that the relabellings move, the arc lemma then no longer constrains the zeroth-order constants c̄(a,b) = C_ab^{a+b}(Φ̄), Λ_n = c̄(0,n). These fail Jacobi only through first-order structure functions contracted with the background velocities.
  - *Example.* The 1D model δu = ξ(1 + Δu) of φ = x + u about the ruler u = 0 closes exactly with rational structure functions for every translation-invariant Δ with Δ1 = 0, and has Λ_n = −λ_n, where λ is the symbol of Δ. The SLAC derivative gives Λ_n = n̄Λ_1; the central difference gives Λ_2/Λ_1 = 2cos(2π/L).
  - On Z_L the ruler is not periodic, so this is an affine field-space model satisfying (P1) formally, not a relabelling of a periodic field.
  - The closure is automatic: L pointwise-independent generators on an L-dimensional configuration space form a frame. It is not automatic for the d > 1 e₁ sector, where the same model fails to close even with structure functions (exact, 3×3 torus).
- **Common zero.** If every generator vanishes at the background and the structure functions are continuous there, the linearised generators form a graded Lie algebra on their momentum support S. The arc lemma holds on it in gap form: arcs are runs of consecutive momenta inside S, and Λ_2/Λ_1 ≤ 0 whenever 0, ±1, 2 ∈ S and (S) holds at linear order.
  - For generators linear in the fields, and for quadratic Poisson generators such as G_m, continuous structure functions at the vacuum reduce to constants, so B19's non-closure and Theorem B stand for them.
  - The same relabellings do close on {Δφ_x ≠ 0 for all x}, with degree-0 homogeneous structure functions that are discontinuous at the vacuum.
- **Enlarged generator sets.**
  - If [X_1, X_{−1}] ∝ D, then 2Λ_n/Λ_1 ∈ Z survives, and Λ_n = nΛ_1 for some |n| ≥ 2 forces at least two generators at each of the momenta 0 and ±1.
  - sl2 ⋉ V_{L−1} (L odd) attains Λ_n = n̄Λ_1 for every n, with exactly two generators at each of those momenta.
  - Under the literal (S), one central extra generator at momentum 0 removes even 2Λ_n/Λ_1 ∈ Z.
- **Not claimed.** These constructions are abstract graded algebras or affine field-space models. Not claimed: their realisation by periodic lattice relabellings; mixed backgrounds; {G, C} and {C, C} with structure functions. None of this contradicts Theorems A–C; it bounds their scope.

## Theorem A: the uniform–non-uniform sub-bracket

Write `X_p e_{k'} = f(k'+p, k') e_{k'+p}` in the momentum basis and `D e_k = d(k) e_k`, with `d(k) = f(k, k)`. Then `[D, X_p] ∈ span X_p`, with `[D, X_p] = C(p) X_p`, holds iff

`f(k'+p, k') [d(k'+p) − d(k') − C(p)] = 0` for all `k'`.

- **On Z.** Suppose the sub-bracket closes for every `p`, `d` is continuous, which holds for any summable kernel, and each `f(·+p, ·)` is non-zero on a dense set. Then `d(k+p) − d(k) = C(p)` everywhere, `C` is a continuous additive function on the circle, so `C = 0` and `d` is constant. The density condition is per `p`. It is automatic for finite range, where `f` is a non-zero trigonometric polynomial. A non-constant `d` therefore needs a discontinuous symbol, that is a non-summable kernel such as SLAC.
- *Reviewer's remark (consolidation review; unchecked).* For summable transports, the density premise may be unnecessary: `f(k, k) = d(k)` gives closure locally near `(0, k)` wherever `d(k) ≠ 0`, so `d` is locally affine and hence constant.
- **On Z_L.** The jumps of `d`, the `k'` where `d(k'+p) − d(k') ≠ C(p)`, must sit on zeros of `f`.
- **SLAC.** With `d = i k̄`, the jump is the wrap (Umklapp) set `|k̄' + p̄| > L/2`. SLAC closes this sub-bracket iff `f` vanishes on the wrap set. This assumes `f` is not identically zero on the non-wrap set, so that `C(p) = ip̄` is fixed. For even L, `p = L/2` needs a convention; the runner uses odd L.
- **Runner.**
  - **A1:** exact Laurent-polynomial certificates on Z for three finite-range transports: B14's central `G_m`, a fourth-order improved one, and a random rational range-3 one. For each, the gcd of the non-constant z-coefficients is `y − 1`.
  - **A2:** SLAC no-wrap `[Y_0, Y_p] = p̄ Y_p` exactly, for L = 5, 7, 9 and `w = 0, ½, −1`.
  - **A3:** the aliased SLAC, with `f` kept on the wrap set, fails for every `p ≠ 0`.

## Band-limited window and the SLAC full bracket (exact sub-cases)

- **Window (A4).** For `|a|, |b| ≤ n_L` and `|k̄| ≤ m − 2n_L`, `[Y_a, Y_b] e_k = (b − a) Y_{a+b} e_k` exactly. This is the continuum identity `[ξ∂ + wξ′, η∂ + wη′] = ζ∂ + wζ′`, `ζ = ξη′ − ηξ′`, restricted to plane waves with no wrap anywhere. It fails for some band-edge `k`, and the window is not invariant: some `Y_a` maps a window vector outside it. So band-limited closure is a statement about sampled vectors, not an operator identity. The runner covers `(L, n_L) = (9,1), (13,2), (17,3), (25,4)` with `w = 0, ½, −1`, using exact integers. The campaign's floating-point version agreed to 1e−16.
- **SLAC full bracket (A5).** The no-wrap transport satisfies (S), with `Λ_1 = 1`, `Λ_2 = 2` and `[Y_1, Y_{−1}] ≠ 0` exactly, so by Theorem B it cannot close. Exactly, 12, 26 and 48 ordered pairs `(p, q)` have `[Y_p, Y_q] ∉ span Y_{p+q}` at L = 5, 7, 9.
- **L = 3.** With `w = −1` it closes exactly with `[Y_1, Y_{−1}] ≠ 0`: the `sl2` exception. With `w = 0` it closes only degenerately, with `[Y_1, Y_{−1}] = 0`, so (S) fails.

## Theorem C (corrected): the uniform part of (b) is a lattice Leibniz rule

"(b)" is exact closure of `{G[ξ], C(N)}` at order φ² into `H(N′)` plus coupling terms, as in the companion scalar note.

- **Reduction.** At uniform ξ the gravity relabelling `G_g` vanishes, because it is built from differences of ξ. Every lapse–strain coupling also drops out, since `δ_ξ h = 0`. So (b) requires `{P, H(N)} = H(N′)`, with `P = G[1] = πᵀDφ` and `H(N) = Σ N_x h_x`. The density `h` is built with a bilinear product of kernel `a(k₁, k₂)`.
- **The condition.** In momentum space: `a(k₁, k₂) · [λ(k₁) + λ(k₂) − λ′(k₁+k₂)] = 0`. Here `λ` is the symbol of `D` on φ and `λ′` the symbol of the lapse map `N′ = D′N`. The symbol entering the π–π sector is `−λ(−k)`, which equals `λ(k)` only for real antisymmetric `D`. The conclusions below are unchanged, because the argument applies to whichever symbol enters.
- **Full-support kernel** (for example any ultralocal product). Setting `k₂ = 0` gives `λ′ = λ + λ(0)`, so `λ − λ(0)` is a homomorphism `Z_L → C` and hence zero. `λ(0) = 0` because `D` annihilates constants. So `λ = 0` for every `D`, SLAC included, and (b) fails at uniform ξ. On Z, a continuous `λ` with a finite-range kernel `a` (more generally, any `a` non-zero on a dense set) gives the same. A summable `D` with a band-limited product is not excluded. Take `λ = λ′ = i g(k)`, with `g` smooth, odd and equal to `k` on `|k| < 2π/3`, and a smooth `a` supported in `|k₁|, |k₂|, |k₁+k₂| < π/3`. This solves the condition, although `H(1)` then misses the high modes.
  - Correction adopted from the check: the earlier wording "λ is a homomorphism" is replaced by "λ − λ(0) is the zero homomorphism, and λ(0) = 0".
  - Exact nullspace (C1): the solution space is `span{λ = 1, λ′ = 2}` for L = 4–9.
- **The exact case.** Take SLAC with the anti-aliased (no-wrap) product, `a = 1` iff `|k̄₁|, |k̄₂|, |k̄₁ + k̄₂| ≤ m`. Then `λ = λ′ = k̄` solves the condition, with `N′ = +D_SLAC N`. Exactly (C2), the no-wrap solution space is `span{const, k̄}` for L = 5, 7, 9. The sign follows from `{P, F} = −𝒟F`, where `𝒟` is the induced derivation, together with summation by parts. Floating point (F_C4) confirms `N′ = +D_SLAC N` to 1e−14. The first campaign run expected the opposite sign; its log is kept as a bug record.
- **Non-uniform ξ (factorisation lemma; floating point, not checked).** With SLAC transport and the anti-aliased `H`, the residual is absorbed only by a lapse–strain coupling `Σ_x N_x Σ_{|r|≤R} (Dξ)_{x+r} T^{(r)}_x` of full range `R = L//2`. This is least squares over sampled configurations at L = 7, 9, 11, in the campaign script `c3_gc_leibniz.py`, not in this runner. `{C, C}` at order hφπ was not tested with this coupling. So "exact (b)" holds only with a fully non-local lapse–strain coupling, and only as far as these numerics go.

## Boundary case: the 2D sine algebra

The area-preserving relabellings of a lattice scalar on `Z_N²` are realised through the clock-and-shift matrices `g`, `h`, with `hg = ωgh`. They form the Fairlie–Fletcher–Zachos algebra, `[X_p, X_r] = κ c(p,r) X_{p+r}`, with `c(p,q) = ω^{p₂q₁} − ω^{p₁q₂}` and `κ = N/(2πi)`.

- **Exact closure** (S0, S1; N = 5, 7). `J_pJ_q = ω^{p₂q₁} J_{p+q}` is checked with exact monomial matrices. The cyclic Jacobi identity is checked in `Z[ω]` over all `N⁶` triples.
- **Translation-covariant and non-local.** A site-localised stream function generates a relabelling that reaches torus distance `N//2` (F_S5, floating point).
- **O(a²), not O(a)** (S2, S3). In the Weyl-ordered basis `J′_m = e^{iπm₁m₂/N} J_m`, `J′_pJ′_q = e^{iπs/N} J′_{p+q}` with `s = p₂q₁ − p₁q₂` (exact, exponents mod 2N). So the structure constants are `(N/π) sin(πs/N) = s − π²s³/(6N²) + …`. The raw basis has an `O(1/N)` term. The earlier "O(a)" was a basis artefact, since the Weyl rescaling is a change of basis.
- **No uniform translation** (S4; N = 5, 7). Adjoin a `D` acting diagonally with weights `Λ(p)`. Jacobi gives `(Λ(p) + Λ(q) − Λ(p+q)) c(p,q) = 0`, and the system has full rank, so `Λ = 0`. This strengthens the check's observation that an additive `Λ` on `Z_N²` vanishes. Adjoining a translation therefore breaks closure; the campaign's floating-point check gave relative residual 1 for both SLAC and naive `D₁`.
- **Reading.** Exact closure with translation covariance is possible here only because the algebra avoids Theorem B's premises: it contains no uniform translation, and, being area-preserving, no compressions. It is non-local.

## Relation to earlier blocks (interpretation where marked)

- **B19 (lattice non-closure of the relabellings).** B19 certified exactly, at L = 3 and 4, that the lattice `G_m` does not close.
  - Theorem A shows that on Z no finite-range `G_m` closes even the uniform sub-bracket. On small tori, Theorem A alone does not decide; B19's certificates do.
  - Theorem B shows that no translation-covariant replacement of any range closes while keeping (S) and the continuum ratio `Λ_2 = 2Λ_1` (or any `Λ_n = nΛ_1`, `n ∉ {0, ±1}`). Interpretation: B19's non-closure is not an artefact of range.
  - The 09-24 gravity relabelling `G_g` is linear on the lattice, hence abelian, so it fails (S). Theorem B concerns the matter relabellings and any relabelling meant to close like vector fields.
- **B14 E5 / companion note Result 3, and B16 T6d (interpretation, partly supported here).**
  - The companion note's obstruction monomial `ob = −¼ ξ_b (N_{x+e} − N_x)(π_{x+e} − π_x)²` survives at `ξ ≡ 1`. There `G_g` and every coupling vanish.
  - Its π–π sector has an ultralocal, full-support product and the central `D ≠ 0`, so it is the full-support case of Theorem C.
  - Runner C3 checks the 1D reduction exactly: `{G_m[1], ½ Σ N π²} = ½ Σ (N_{x+1} − N_x) π_x π_{x+1}`, whose off-diagonal part is that of `ob`.
  - B16 T6d reported the B14 obstruction at uniform shift. That B14 E5 and B16 T6d are instances of Theorem C was not independently verified by the campaign check. C3 is a same-family consolidation check in 1D; the consolidation review re-derived it in 2D (same family).
- **B15.** B15's fermion no-go (range-2 and mixed-diagonal lapse pairs) is a separate mechanism and is not derived from Theorems A–C.

## Premises

- **Axioms used.** None beyond the lattice and its translations. `docs/MINIMAL_AXIOMS_2026-06-29.md` supplies no dynamics, so every generator below is supplied.
- **Supplied (Theorem B).** (P1), (P2) and (S) as stated, with the d > 1 reflection premise and, on Z, the periodic-ξ extension.
- **Supplied (Theorems A, C).**
  - Translation-covariant transports `X_p` with symbol `f`.
  - Uniform relabelling `D` with symbol `d`.
  - Density products with kernel `a`.
  - The uniform-ξ reduction of (b), which uses that `G_g` and the couplings vanish at uniform ξ, as in the companion note.
  - `{q, p} = +1` for `(φ, π)`.
- **Supplied (sine algebra).** The clock–shift realisation and the stream-function relabelling `δΦ = κ[F, Φ]`.
- **Standard facts used.**
  - Weyl's complete reducibility and the weight theory of finite-dimensional `sl2`-modules over C.
  - Gröbner bases over Q (`[1]` certifies inconsistency over C).
  - Exact linear algebra over Q.
  - Laurent polynomials as symbols of finite-range translation-invariant operators.
  - For prime N, `Z[ω] ≅ Z^N / Z(1, …, 1)`.

## Relation to prior work

- **Confirmed by the campaign worker.**
  - Kato, Sakamoto and So, arXiv:0803.3121 and arXiv:0810.2360: a no-go for a lattice Leibniz rule with local difference operators, and the role of SLAC-type non-locality. Theorem C is the relabelling-algebra version of this mechanism.
  - Loll, gr-qc/9708025: diffeomorphism commutators of lattice gravity.
- **Cited from memory by the campaign; not verified.**
  - Drell, Weinstein and Yankielowicz (1976): the SLAC derivative.
  - Karsten and Smit; Nielsen and Ninomiya: locality versus symmetry on the lattice.
  - Bahr and Dittrich; Dittrich; Gambini and Pullin; Renteln and Smolin: broken diffeomorphisms and the constraint algebra in discrete gravity. The companion notes give citation details, also by attribution.
  - Kempf: band-limited fields and sampling.
  - Fairlie, Fletcher and Zachos (1989); Hoppe: the sine algebra and `gl(N)` approximations of area-preserving diffeomorphisms.
  - Koo and Saleur: lattice Virasoro generators close only in the scaling limit.
- **Theorem B.** This is elementary `sl2` weight theory and plausibly folklore. Related results:
  - the simplicity of the Witt algebra;
  - the Witt–Zassenhaus algebra `W(1;1)` in characteristic p;
  - classifications of graded Lie algebras with one-dimensional homogeneous pieces (Mathieu; Iohara; Su, Zhang and Zhao).

  It is presented as a new-to-us elementary lemma, not as a new mathematical theorem.
- **New here, and narrow.**
  - The arc-lemma form, with exact certificates and explicit realisations.
  - Its application to lattice relabelling maps under the stated premises.
  - The exact sub-case statements for SLAC and band-limited windows.
  - The reduction of the uniform-ξ obstruction of the companion note to Theorem C.

## Historical packet proposal (promotion deferred)

The negative sentences:
- no translation-covariant relabelling algebra of any range satisfying (P1), (P2) and (S) has `Λ_2 = 2Λ_1`, or any `Λ_n = nΛ_1` with `n ∉ {0, ±1}`, on a torus with `L ≥ 4` or on Z;
- no summable `D` with continuous symbol closes the uniform sub-bracket on Z (Theorem A);
- no `D` closes the uniform part of (b) with a full-support product (Theorem C);
- no uniform translation can be adjoined to the sine algebra.

- **N1 — routes by which they could fail or mislead.**
  - Enlarged generator sets, with more than one generator per momentum. Adding generators trivially closes; what enlargement buys is the spectrum, which needs at least two generators at each of 0 and ±1 (see the scope section).
  - Field-dependent structure functions, which (P2) excludes. The continuum hypersurface-deformation algebra itself has them in `{C, C}`. At a background the relabellings move they evade Theorem B (see the scope section).
  - Algebras without a uniform translation, or with `[X_1, X_{−1}] = 0` (the sine algebra; the abelian lattice `G_g`).
  - In d > 1, maps without the reflection covariance.
  - Infinite-dimensional sectors, which are not covered.
  - Statements up to controlled `O(a^k)` terms, which these theorems do not touch.
- **N2/N3 — scope.**
  - Theorem B is proved for every `L ≥ 4` and for Z under the periodic extension. The Gröbner certificates cover L = 4–9 (L = 10 with `--slow`), and the exact projection L = 4–7.
  - Theorem A on Z needs `f` non-zero on a dense set, which is automatic for finite range.
  - Theorem C: C1 covers full support at L = 4–9; the homomorphism argument covers every L.
  - The window and SLAC sub-cases are exact on the listed odd tori.
  - The factorisation lemma is floating point on sampled configurations, and unchecked.
- **N4 — inputs.**
  - Exact throughout the gating tests: sympy over QQ, Fractions, and integer exponent arithmetic in `Z[ω]` and `Z[ζ_{2N}]`.
  - The checks prefixed `F_` are floating point: the Leibniz bracket with SLAC, and sine-algebra non-locality.
  - The campaign's Levenberg–Marquardt runs (400 starts, L = 5–8) are corroboration only.
- **N5 — wording.**
  - "Closes like the continuum" means (P2) together with (S) and the continuum spectrum at some `n ∉ {0, ±1}` (in particular `Λ_2 = 2Λ_1`). (P2) with (S) alone is attainable (B4).
  - "Range" means the real-space support of the kernel.
  - "Non-local" means not absolutely summable, or full-torus support.
  - "O(a²)" means the order of the first deviation of the structure constants at fixed integer momenta.
  - No physical identification is made.
- **N6/N7 — strongest objections.**
  - *"Theorem B is folklore."*
    - Reply: plausibly yes, and it is presented as such.
    - Its content here is the application, under explicit premises, to lattice relabelling maps.
  - *"(P2) is too strong; physical lattices need not close within span G."*
    - Reply: yes, this is the premise.
    - The theorem says a lattice relabelling algebra must give up one of (P2), (S), one generator per momentum, the uniform translation, or the continuum ratio `Λ_2 = 2Λ_1`. Keeping all but the last, exact closure is attainable (B4).
  - *"The window is exact."*
    - Reply: only on vectors that stay inside it, and it is not invariant.
  - *"The SLAC Leibniz case shows exact (b)."*
    - Reply: only the uniform part is exact.
    - The non-uniform part needs a full-range coupling, and this was found by unchecked floating-point numerics.
- **N8 — earlier claims.**
  - The companion notes' `O(a²)` and `O(a)` obstructions are unchanged.
  - This note says that the uniform-ξ part of the scalar one cannot be removed by any `D` while the π product has full support, nor on Z by a summable `D` with a local product. It also says that no relabelling of any range satisfying (P1) and (S) removes the `{G, G}` defect, that is achieves (P2), while keeping `Λ_2 = 2Λ_1`.
  - The campaign C3 statements "affine sl2", "|Λ_2/Λ_1 − 2| ≥ ½", "O(a)" for the sine algebra, and "λ is a homomorphism" are superseded by the corrected forms above.

## Historical checking narrative (not fresh evidence)

The campaign worker (block C3) and its checker are both of the same model family as each other and as this consolidation's author; none is independent in model lineage. The checker worked in fresh context and wrote new code that imports nothing from C3 (49 PASS, 0 FAIL). Its code differs from the worker's in three ways:
- its own Jacobi generator ("ad is a representation" rather than the cyclic form);
- Gröbner grid and lex-elimination routes;
- Levenberg–Marquardt numerics from random starts.

- **Confirmed.**
  - Theorem B, with the derivation of `Λ_{−1} = −Λ_1` (Gröbner R0).
  - The `sl2` relations, integer weights, and the weight-0 argument for `g^φ`.
  - The L = 3 exception.
- **Sharpened.** The arc lemma: proved, then verified by Gröbner (the grid for L = 4–8, the projection for L = 4–7) and by numerics (every converged solution obeys the arcs; with `Λ_2 = 2` pinned, the best residual was 2.0).
- **Corrected, and adopted here.**
  - Define τ, and state that `Λ_{−1} = −Λ_1` is derived.
  - Replace `|Λ_2/Λ_1 − 2| ≥ ½` with the arc result.
  - The "L = 4–9" certificate used (Z).
  - "sl2 ⋉ C² (special affine)", not "affine sl2".
  - The d > 1 and Z premises are stated as above.
  - Theorem A: the density condition is per p; the SLAC "iff" needs f non-zero off the wrap set; even L needs a convention.
  - Theorem C: λ − λ(0) is the zero homomorphism, and the π symbol is `−λ(−k)`.
  - The sine algebra is `O(a²)` in the Weyl basis (slope −1.97).
- **Not checked.** The factorisation lemma, and B14 E5 and B16 T6d as instances of Theorem C.

This runner keeps both Gröbner generators: B0–B2 are the checker's, B3 the worker's. It adds checks written for this consolidation by the same model family:
- B4, the explicit realisations;
- exact rewrites of the SLAC, window, Leibniz and sine-algebra checks (A1–A5, C3, S0–S4).

- **Consolidation review.** A fresh-context reviewer of the same model family, not independent in lineage, gave the verdict "needs changes". Its corrections are applied here:
  - Theorem B forbids the continuum spectrum, not closure (F1).
  - The Z-side scope of Theorems A and C needs the density premise, and a band-limited summable Leibniz pair exists (F2).
  - The `Λ(2k)/Λ(k)` wording and the certificate scope are corrected (F3).
  - The B3_Q_L5 test is tightened.

  By different paths, the reviewer also re-derived:
  - B4, as affine-matrix realisations for L = 3–9;
  - necessity at L = 5 and 6, by `sympy.solve`;
  - A1's `y ≠ 1` claim (the gcd of the non-constant z-coefficients is `y − 1` for all three families);
  - C3 in 2D (a 3×3 torus with `ξ = e₁`).

  Its scripts are in `.claude/science/physics-loops/scale-ladder-campaign-20261018/NOTE_C3_review/ (unavailable historical pointer; not a proof premise)`.

Re-running this runner is not a further independent check.

## Historical execution record (not a fresh capture)

```bash
python3 scripts/lattice_relabelling_algebra_no_go_arc_lemma_and_non_local_leibniz_2026_10_18.py
```

Expected: `TOTAL: PASS=103 FAIL=0`, in about 80 s (63–78 s measured; Python 3, sympy 1.14, numpy). Parts:
- B: Theorem B and the arc lemma (Gröbner, realisations);
- A: Theorem A, SLAC, window, SLAC full bracket;
- C: Theorem C and the B14 instance;
- S: the sine algebra.

Optional: `--slow` adds the checker's L = 8 grid and the worker's L = 10 (Z) certificate (`TOTAL: PASS=105 FAIL=0`, about 4 min; 241 s measured). The campaign scripts in `.claude/science/physics-loops/scale-ladder-campaign-20261018/C3_exact_closure_nonlocality/ (unavailable historical pointer; not a proof premise)` and `C3_check/` hold the floating-point evidence not repeated here: the factorisation scan, the Levenberg–Marquardt runs, and the local-family torus residuals.

## Load-bearing sources

- Companion scalar note (same PR) (`outputs/scale_ladder_continuations_review_2026_10_18/curvature_member_closure_with_matter_common_cone_2026_10_18_full_argument.md`)
- Spin-½ and spin-1 companion (same PR) (`outputs/scale_ladder_continuations_review_2026_10_18/curvature_member_closure_spin_half_and_spin_one_common_cone_2026_10_18_full_argument.md`)
- 09-24 constraint-closure note (`docs/ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md`)
- Axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md`)
