# GB1-QL. The quantum-link route of the lattice gauge bridge

## 0. Status

**FINISH: FROZEN 2026-11-07 after pass 3 (GB1QL_REFEREE.md); the referee's edits E1-E10 are applied, with closures R1 and R2.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment. The item enters `GB1.md` as its Amendment 2. The lead (Claude Opus 5.5, laptop) checked that the edits are in the text; that is a text check, not a second referee. 

On the definitions below, the harmonic identities, the finite `so(5)` quantum link, the bounded-flux coefficient and light-cone estimates, the single-time comparison and its energy and two-time extensions are conditional mathematical results. They compare a named family of finite registers with the cube-face, Trotterized SU(2) Hamiltonian model, for specified matched states and finite time. The five-mode model is a proposed rung test law, not either named working-set law. No continuum, vacuum, Euclidean measure, or retained audit status follows.

**GAP.** Pass 1 multiplies traversed link matrices in an order incompatible with its endpoint gauge transformation. The correction and failure are explicit in §1. Its T0 hand-off also conflates gauge-covariant dynamics with a gauge-invariant start measure; the corrected status appears in §3. (H-4D) is the first missing input in dependency order (Lemma H).

**Open by name.**

- **GB1-QL[`L5-O`]**: whether an `so(20)` register family realises `R_s` in an `SU(2)` block of `L5-O`, with a class on which that block evolves on its own.
- **GB1-QL[matter]**: the comparison with matter present.
- **GB1-QL[U(2)]**, with **U3a** (`U(2)` to `SU(2)`) and **U3b** (the electric layer), on any route that supplies a growing `U(2)` block register.
- **E-1, E-2, E-3** of `GB1.md`; **GB1-CF**; the time continuum; **GB1-SC**; **VC1**.
- **T0-start[SU(2)]**: (H-4D) first; then (H-GI), (H-Haar), (H-RP), (H-class).
- **T0-rate**; **T0-QLR[SU(2)]** beyond its finite-time Hamiltonian regulator part.
- **Y2-W** for the fixed register.

T0-start[SU(2)]: (H-4D) first; (H-GI), (H-Haar), (H-RP) and (H-class) as properties of the missing measure.

**Provenance.** Pass 1: Claude Opus 5.5, `GB1QL_DRAFT.md`, SHA-256 `4d06962b9bfc929079b504fe6458c10c16abd148394854f83f23085d8f5a6ac0`. Pass 2: Codex `gpt-6.1-terra`; reasoning effort and session id: see run log. Context: `prior/GB1QL.md`, `TOE_ASSEMBLY.md` §§3.4–3.6 and GB1 target, `GB1.md`, `GB1Z2L5.md`, `GA2_Y2.md`, `LW1_5.md`, `LW1.md`. Scratch numbers are pass-1 reports, not independently reproduced. Literature identifications and repository claims cited from the digest are contextual; they are not independently verified on a remote revision.

**Editing session provenance.** Codex `gpt-6.1-terra`, effort high, `codex-cli 0.165.0`; session id `01a1b7c7-5280-7133-a14f-3e948ae465fa`.

**Prior work.** The finite-box U(1) limit and its leak repair are already proved in `GB1.md` Theorem 5.2 and `GB1_REFEREE.md`; the frozen-spectator U(2) block and fixed-register limitation are in `GB1.md` Theorems 6.1 and 5U. `GA2_Y2.md` Theorem 2.1 and Corollary 2.2 give the finite-register obstruction and top-flux limitation. The digest `prior/GB1QL.md` identifies the already existing volume-uniform SU(3) local-observable approximation in `docs/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md`, an unaudited supplied-Hamiltonian Peter–Weyl result, and the energy-priced compression result in `docs/GAUGE_WILSON_PW_COMPRESSION_SHELL_AND_ENERGY_PATH_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md`. They do not identify this SU(2) regulator or prove this tick comparison. The digest also identifies the fixed five-state SU(2) truncation in `docs/MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md`, proposed and unaudited; its branch was not accessible to pass 1. Credit for the `so(5)` quantum-link construction goes to Chandrasekharan and Wiese; Tong et al. use the same truncated Hilbert space. These identifications are not used as proof.

## 1. Definitions inferred by the distiller

The following definitions fix the comparison. They are not adopted axioms.

Indices: `μ, ν, ρ, σ ∈ {1,2,3,4}`; `j, k, l ∈ {1,2,3}` when they label Pauli matrices; `a, b ∈ {1,2}` are matrix indices.

### 1.1 The Kogut-Susskind link

Let `S³ ⊂ R⁴` carry the normalized measure `σ` invariant under `SO(4)`, and put `𝒦 = L²(S³, σ)`. Put `e_4 = 1_2`, `e_j = iσ_j`, and `g(x) = Σ_μ x_μ e_μ = x_4 + i x·σ`. For `x ∈ S³`, `g(x) ∈ SU(2)`, and `g` is a bijection `S³ → SU(2)`. Left and right multiplication on `SU(2)` act on `x` by rotations, so `σ` is the Haar measure under `g` (the normalized measure invariant under both translations). So `𝒦` is the Kogut-Susskind link space `L²(SU(2))`.

- `𝓗_k` is the space of complex harmonic polynomials on `R⁴`, homogeneous of degree `k`. `H_k ⊂ 𝒦` is the space of their restrictions to `S³`. Restriction is injective on `𝓗_k` (a homogeneous polynomial that vanishes on `S³` vanishes). `k` is the **flux** of a link; `j = k/2` is its spin.
- `D_{μν} = x_μ∂_ν − x_ν∂_μ` and `L_{μν} = −i D_{μν}`, acting on polynomials. `J_l = ½Σ_{jk} ε_{jkl} L_{jk}`, `K_l = L_{l4}`, `N^±_l = ½(J_l ± K_l)`. A first-order computation shows that `N^+` generates left translations `g ↦ hg` and `N^-` right translations. These are the electric fields at the two ends of a link.
- `E² = ¼ Σ_{μ<ν} L_{μν}²` is the electric Casimir; Lemma 4.1(b) gives `E² = k(k+2)/4 = j(j+1)` on `H_k`.
- The link matrix is `U = Σ_μ x_μ ⊗ e_μ`: the 2 × 2 matrix of multiplication operators `U^{ab} = g(x)_{ab}`. It is unitary on `C² ⊗ 𝒦`, since `g(x)` is unitary at every point.

**Density, R2.** (referee closure, GB1QL_REFEREE.md) The algebraic sum `𝒫 = Σ_k H_k` is dense in `𝒦 = L²(S³, σ)`. Hence `𝒦 = ⊕̂_k H_k` (orthogonal by Lemma 4.1(c)), and `E² = Σ_k (k(k+2)/4)Π_k` is self-adjoint on its natural domain.

*Proof.* `H_0` holds the constants. By Lemma 4.1(a), `x_μ H_k ⊆ H_{k+1} + H_{k−1}` on `S³`, so `𝒫` is closed under multiplication by each `x_μ`. By induction on degree, `𝒫` contains the restriction of every complex polynomial. These restrictions form a unital algebra that separates points of `S³` and is closed under complex conjugation, so by Stone-Weierstrass they are dense in `C(S³)` in the sup norm. Sup-norm convergence implies `L²(σ)` convergence for the probability measure `σ`, and `C(S³)` is dense in `L²(σ)` for a finite Borel measure on a compact metric space. □

This fact is used to define `E²` as a self-adjoint operator on all of `𝒦`, so that the target model is the usual one. Only Corollary 4.9(a), for Kogut-Susskind states not supported on finite flux, uses it in a proof. Elsewhere every vector that enters a proof lies in a finite sum of `H_k`'s, or enters only through its norm.

### 1.2 The quantum-link family `R_s`

Fix an integer `s ≥ 1` and put `c_s = √(s(s+3))`.

- `R_s = H_0 ⊕ H_1 ⊕ … ⊕ H_s ⊂ 𝒦`, with `Π_k` the orthogonal projection onto `H_k` (orthogonality: Lemma 4.1(c)). `dim R_s = Σ_{k≤s}(k+1)² = (s+1)(s+2)(2s+3)/6`.
- For `h ∈ 𝓗_k`, put `x^+_μ h = x_μ h − |x|² ∂_μ h/(2k+2)` and `x^-_μ h = ∂_μ h/(2k+2)`, then restrict to `S³`. Lemma 4.1(a) shows `x^+_μ h ∈ 𝓗_{k+1}`, `x^-_μ h ∈ 𝓗_{k−1}`, and `x_μ h = x^+_μ h + x^-_μ h` on `S³`.
- `y_k = √((s−k)(s+k+3))/c_s` for `0 ≤ k ≤ s`, so `y_0 = 1`, `y_s = 0`, and `y_k² = 1 − k(k+3)/(s(s+3))`. `Y_s = Σ_{k≤s} y_k Π_k`.
- `P_μ = x^+_μ Y_s + Y_s x^-_μ` on `R_s`. It maps `R_s` into itself, since `y_s = 0`.
- `U_s = Σ_μ P_μ ⊗ e_μ = P_4 + i P·σ`, the link matrix of the family; `L_{μν}`, `N^±` and `E²` are restricted to `R_s` (each preserves every `H_k`).

Proposition 4.2 shows that `(L_{μν}, c_s P_μ)` is a representation of `so(5)` with Casimir `s(s+3)`. So `R_s` is the `SU(2)` quantum link model of Chandrasekharan-Wiese (section 2) in an `so(5)` representation of dimension `dim R_s`, with link `U = U⁰ + iU·σ`, `U⁰ ∝ P_4`, `U^j ∝ P_j`. The case `s = 1` is the five-state link.

### 1.3 The two ticks

Links of `Z³` are oriented, `ℓ = (x, x+e_i)`. As in `GB1.md` Definition 5, `𝒞` is the set of tiling cubes: every link lies in exactly one `C ∈ 𝒞`, and distinct cubes have disjoint link sets `ℓ(C)` (12 links each). For a face `p ⊂ C` with boundary links `ℓ_1, …, ℓ_4` in cyclic order, `ℓ_1, ℓ_2` traversed forward and `ℓ_3, ℓ_4` backward,

`X_p = U_{ℓ_4}^* U_{ℓ_3}^* U_{ℓ_2} U_{ℓ_1}` (matrix product, operator entries), `B_p = tr X_p + (tr X_p)^*`, `B_C = Σ_{p ⊂ C} B_p` (six faces).

**GAP (draft plaquette ordering).** The draft instead writes `U_ℓ1 U_ℓ2 U_ℓ3^* U_ℓ4^*` in traversal order. Under its stated transformation `U_(x,y) ↦ h_y U_(x,y) h_x^{-1}`, adjacent gauge factors do not cancel in that product. For example, take `U_1=U_3=iσ_1`, `U_2=U_4=1`, and a gauge rotation `h=iσ_2` only at the vertex between the first two traversals. The draft trace changes from `2` to `−2`. The reversed product above transforms as `X_p ↦ h_{x0} X_p h_{x0}^{-1}`, so its trace is invariant. All subsequent claims use this corrected ordering; their norm and flux arguments depend only on four distinct links and apply unchanged.

The **Kogut-Susskind tick** is `U_KS = W_B W_E` with `W_B = ∏_{C∈𝒞} g_C`, `g_C = e^{−iθ B_C}`, and `W_E = ∏_ℓ e^{−iτ_E E²_ℓ}`. The **quantum-link tick** `U_{(s)}` is the same formula with `U_s` and `R_s` in place of `U` and `𝒦`; write `B^s_p, B^s_C, g^s_C`. Both use one magnetic angle `θ ∈ R` and one electric angle `τ_E ∈ R`. Their Heisenberg maps are `α(A) = U_KS^* A U_KS` and `α_s(A) = U_{(s)}^* A U_{(s)}`, as in `GB1.md` Definition 3. On `Z³` the products are locally finite; for a local `A` only finitely many gates act (Lemma 4.5). This is the pure-gauge Trotterized model, which is GB1's Hamiltonian target form (R-FORM in `GB1.md` §8) with the cube-face plaquettes; the continuous-time Hamiltonian and the full plaquette sum (GB1-CF) are not the target here.

### 1.4 The embedding and the classes of states

`ι : R_s → 𝒦` is the inclusion. For a finite link set `Λ`, `ι_Λ = ⊗_{ℓ∈Λ} ι`. It is an isometry and it commutes with every `L_{μν}`, `N^±_l` and `E²`. So it intertwines the gauge action exactly, and for every bounded `A` on `𝒦^{⊗X}` that commutes with the gauge action, the **framework observable** `ι_X^* A ι_X` commutes with the restricted gauge action.

For `M ≥ 0`, `F_M(Λ) = ⊗_{ℓ∈Λ}(H_0 ⊕ … ⊕ H_M)` is the space of vectors with flux at most `M` on every link of `Λ`, and `Π^Λ_M` is its projection. It commutes with the gauge action; it is not a projection onto local singlets.

- **Class `S_M(Λ)` (bounded flux).** A pair `(ω_s, ω)`, with `ω_s` a state of the quantum-link family and `ω` a state of the Kogut-Susskind model, is **matched at flux `M` on `Λ`** if `M ≤ s`, the restrictions are density matrices `ρ_s` on `R_s^{⊗Λ}` and `ρ` on `𝒦^{⊗Λ}` with `ρ = ι_Λ ρ_s ι_Λ^*`, and `ρ_s` is supported on `F_M(Λ)`. Every Kogut-Susskind density matrix supported on `F_M(Λ)` arises this way, and so does every framework density matrix supported on `F_M(Λ)`.
- **Class `E_e(Λ)` (bounded local electric energy).** A state with locally normal restrictions and `ω(E²_ℓ) ≤ e` for every `ℓ ∈ Λ`.

Neither class asks for gauge invariance of the state, a product form, or a vacuum. States of the Kogut-Susskind ground-state type at any coupling lie in `E_e(Λ)` for some `e` whenever their local electric energy is finite; no such state is identified here.


### 1.5 Flux-bounded observables and the proposed test law

Call a bounded `A` on `𝒦^{⊗X}` **`d`-flux-bounded** if it maps flux at most `M'` into flux at most `M'+d` on every link, for every `M'`. Examples: a Wilson loop `tr(F_1⋯F_r)` (each `F_i` a link matrix or its adjoint) in which each link occurs at most `d` times; every function of the `E²_ℓ` (`d = 0`); products of these.

**Definition (`L5[SU(2), s]`).** Data of `LW1.md` §2 and `GB1.md` Definition 5 except as follows.
1. Sites: `F_x = ΛC⁵`, modes `c_{x,j}`, `j = 1, …, 5`, `N_x = Σ_j n_{x,j}`. The doublet is `d_x = (c_{x,4}, c_{x,5})^T`; flavours 1-3 are spectators.
2. Links: the register `R_s` of section 1.2, link matrix `U_ℓ = U_s`.
3. Gauge group `SU(2)` at each site: `d_x ↦ h_x d_x`, spectators fixed, and on `ℓ = (x, y)`, `U_ℓ ↦ h_y U_ℓ h_x^{−1}`, implemented on `R_s` by the rotation of `S³` that corresponds to `g ↦ h_y g h_x^{−1}` (rotations preserve every `H_k`, and `x^±_μ`, `Y_s` are rotation-covariant, so `U_s` transforms like `U`).
4. Hop: `h_ℓ = d_y^† U_ℓ d_x + h.c. = Σ_{a,b∈{4,5}} c^†_{y,a} U_ℓ^{ab} c_{x,b} + h.c.`; matter cube layers `M_e, M_o` with `H_C = 3^{−1/2}Σ_{ℓ⊂C} η_i(x) h_ℓ`, angles `a_e = ε − μ/2`, `a_o = ε + μ/2`, `0 ≤ μ < 2ε < π`. Spectators do not hop.
5. Electric layer `W_E = ∏_ℓ e^{−iτ_E E²_ℓ}`; magnetic layer the cube-face layer of section 1.3 at one angle `θ`; tick `U = W_B W_E M_o M_e`.

## 2. Theorems and proofs

The numbering follows the draft. All results use the corrected plaquette ordering above.

### Lemma 4.1: harmonic calculus on `S³`

**Lemma 4.1.** Let `k ≥ 0` and `h ∈ 𝓗_k` (with `𝓗_{−1} = 0`).

(a) `x^+_μ h ∈ 𝓗_{k+1}`, `x^-_μ h ∈ 𝓗_{k−1}`, and `x_μ h = x^+_μ h + x^-_μ h` on `S³`.

(b) Each `L_{μν}` maps `𝓗_k` into itself, and `Σ_{μ<ν} L_{μν}² = k(k+2)` on `𝓗_k`. So `E² = k(k+2)/4` on `H_k`.

(c) For polynomials `f, h`, `⟨f, L_{μν} h⟩ = ⟨L_{μν} f, h⟩` in `𝒦`. Hence `H_k ⊥ H_{k'}` for `k ≠ k'`.

(d) `x^±_μ h = Π_{k±1}(x_μ h)`, and `⟨g, x^+_μ h⟩ = ⟨x^-_μ g, h⟩` for `g ∈ H_{k+1}`, `h ∈ H_k`.

(e) `Σ_μ x^-_μ x^+_μ h = a_k h` and `Σ_μ x^+_μ x^-_μ h = b_k h`, with `a_k = (k+2)/(2k+2)` and `b_k = k/(2k+2)`.

(f) `(x^-_μ x^+_ν − x^-_ν x^+_μ) h = −i L_{μν} h/(2k+2)`.

(g) `[L_{ρσ}, x^±_μ] = −i(δ_{σμ} x^±_ρ − δ_{ρμ} x^±_σ)` on `H_k`.

(h) `x^+_μ x^+_ν h = x^+_ν x^+_μ h`, `Σ_μ x^+_μ x^+_μ h = 0` on `S³`, and `(x^-_μ x^+_ν + x^+_μ x^-_ν) h` is symmetric in `(μ, ν)`.

*Proof.* (a) `Δ(x_μ h) = 2∂_μ h`. For harmonic `q` of degree `d`, `Δ(|x|² q) = 8q + 4(Σ_ρ x_ρ∂_ρ) q = (4d+8) q`. With `q = ∂_μ h` (harmonic, degree `k−1`): `Δ(|x|² ∂_μ h) = (4k+4) ∂_μ h`. So `Δ(x^+_μ h) = 2∂_μ h − (4k+4)∂_μ h/(2k+2) = 0`. The degrees are clear, and `|x|² = 1` on `S³`.

(b) `[Δ, x_μ∂_ν] = 2∂_μ∂_ν` is symmetric in `(μ, ν)`, so `D_{μν}` commutes with `Δ`; it also commutes with the Euler operator `𝔈 = Σ_ρ x_ρ∂_ρ`. So `D_{μν}` preserves `𝓗_k`. Using `∂_ν x_μ = x_μ ∂_ν + δ_{μν}`, one finds `Σ_{μ,ν} x_μ∂_ν x_μ∂_ν = |x|²Δ + 𝔈` and `Σ_{μ,ν} x_μ∂_ν x_ν∂_μ = 𝔈² + 3𝔈`, hence `Σ_{μ<ν} D_{μν}² = |x|²Δ − 𝔈(𝔈+2)`. On `𝓗_k` this is `−k(k+2)`, and `L² = −D²`.

(c) Let `R_t = exp(t(𝔢_{μν} − 𝔢_{νμ})) ∈ SO(4)`, with `𝔢_{μν}` the 4 × 4 matrix units. Invariance of `σ` gives `∫ \bar f(R_t x) h(R_t x) dσ = ∫ \bar f h dσ` for all `t`. Polynomials are smooth on compact `S³`, so the derivative at `t = 0` may be taken inside the integral. Since `(d/dt) f(R_t x)|_{t=0} = −D_{μν} f` and `D_{μν}` has real coefficients, `⟨D_{μν} f, h⟩ = −⟨f, D_{μν} h⟩`. Multiply by `−i`. Then `C_4 = Σ_{μ<ν} L_{μν}²` is symmetric on polynomials, with eigenvalue `k(k+2)` on `H_k` by (b); distinct eigenvalues give orthogonality.

(d) By (a) and (c), `x_μ h` has components `x^+_μ h ∈ H_{k+1}` and `x^-_μ h ∈ H_{k−1}` only. Multiplication by the real function `x_μ` is symmetric, so `⟨g, x^+_μ h⟩ = ⟨g, x_μ h⟩ = ⟨x_μ g, h⟩ = ⟨x^-_μ g, h⟩`, because `x^+_μ g ∈ H_{k+2} ⊥ h`.

(e) The denominator for `x^-_μ` on `𝓗_{k+1}` is `2k+4`. `Σ_μ ∂_μ(x_μ h) = (k+4) h` and `Σ_μ ∂_μ(|x|² ∂_μ h) = 2k h`. So `Σ_μ x^-_μ x^+_μ h = [(k+4) − 2k/(2k+2)] h/(2k+4) = (k+2)² h/((k+1)(2k+4)) = a_k h`. For the other order, `x^+_μ` on `𝓗_{k−1}` has denominator `2k`, so `Σ_μ x^+_μ (∂_μ h)/(2k+2) = [𝔈h − |x|² Δh/(2k)]/(2k+2) = b_k h` (both sides vanish at `k = 0`).

(f) `x^-_μ x^+_ν h = [δ_{μν} h + x_ν∂_μ h − (2x_μ∂_ν h + |x|²∂_μ∂_ν h)/(2k+2)]/(2k+4)`. Antisymmetrize in `(μ, ν)`: the `δ` and `∂_μ∂_ν` terms cancel, leaving `−D_{μν} h [1 + 2/(2k+2)]/(2k+4) = −D_{μν} h/(2k+2)`. Use `D = iL`.

(g) `[D_{ρσ}, x_μ] = δ_{σμ} x_ρ − δ_{ρμ} x_σ`. `L_{ρσ}` preserves every `H_k` by (b) and (c), so it commutes with each `Π_k` on polynomials; take the `H_{k±1}` components and use (d).

(h) By (d) and (a), `x^+_μ x^+_ν h = Π_{k+2}(x_μ x_ν h)`, because the `H_{k−1}` part of `x_ν h` is mapped by `x_μ` into `H_k ⊕ H_{k−2}`. This is symmetric, and `Σ_μ x_μ x_μ = 1` on `S³` gives `Π_{k+2} h = 0`. Likewise `(x^-_μ x^+_ν + x^+_μ x^-_ν) h = Π_k(x_μ x_ν h)`. □

`[pass-1 check, not reproduced]` (a), (d), (e), (f) at `k ≤ 4` to `10^{−15}` (section 7).

### Proposition 4.2: the family is an `so(5)` quantum link, and its link is a contraction

**Proposition 4.2.** On `R_s`:

(a) Each `P_μ` is Hermitian.

(b) `[L_{ρσ}, P_μ] = −i(δ_{σμ} P_ρ − δ_{ρμ} P_σ)` and `[P_μ, P_ν] = i L_{μν}/c_s²`. So the ten operators `L_{μν}` and `L_{μ5} := c_s P_μ` obey `[L_{ab}, L_{cd}] = −i(δ_{bc}L_{ad} − δ_{ac}L_{bd} − δ_{bd}L_{ac} + δ_{ad}L_{bc})`, `a, b, c, d ∈ {1, …, 5}`: the relations of `−i(x_a∂_b − x_b∂_a)` on `R⁵`, that is, of `so(5)`.

(c) `Σ_{a<b≤5} L_{ab}² = s(s+3)` on `R_s`, and `Σ_μ P_μ² = (s(s+3) − k(k+2))/c_s²` on `H_k`.

(d) `U_s^* U_s = (Σ_μ P_μ²) ⊗ 1 − (2/c_s²) Σ_l N^-_l ⊗ σ_l`, and `‖U_s‖ ≤ 1` on `C² ⊗ R_s`.

*Proof.* (a) For `u, v ∈ R_s`, Lemma 4.1(d) gives `⟨u, x^+_μ Y_s v⟩ = ⟨Y_s x^-_μ u, v⟩`; the term that would leave `R_s` is killed by `y_s = 0`. So `(x^+_μ Y_s)^* = Y_s x^-_μ` on `R_s`, and `P_μ^* = P_μ`.

(b) `Y_s` commutes with every `L_{ρσ}`, so the first relation is Lemma 4.1(g). Split `[P_μ, P_ν]` by the change of flux. The part `H_k → H_{k+2}` is `y_{k+1} y_k (x^+_μ x^+_ν − x^+_ν x^+_μ) = 0`, by Lemma 4.1(h); the part `H_k → H_{k−2}` is its adjoint up to relabelling, and vanishes too. The part `H_k → H_k` is `y_k²(x^-_μ x^+_ν − x^-_ν x^+_μ) + y_{k−1}²(x^+_μ x^-_ν − x^+_ν x^-_μ)`. By Lemma 4.1(h) the second bracket is minus the first, and by Lemma 4.1(f) the first is `−i L_{μν}/(2k+2)`. Since `y_k² − y_{k−1}² = (−k(k+3) + (k−1)(k+2))/c_s² = −(2k+2)/c_s²`, the part is `i L_{μν}/c_s²`. At `k = 0` both terms vanish, as does `L_{μν}`; at `k = s` the formula holds with `y_s = 0`. The relations among the `L_{μν}` are those of the differential operators, and the displayed `so(5)` relations with an index 5 reduce to the two relations just proved.

(c) The flux-changing parts of `Σ_μ P_μ²` vanish by Lemma 4.1(h). On `H_k` the rest is `y_k² a_k + y_{k−1}² b_k`. Its numerator over `c_s²(2k+2)` is `(k+2)(s(s+3) − k² − 3k) + k(s(s+3) + 2 − k − k²) = (2k+2)(s(s+3) − k(k+2))`. Add `Σ_{μ<ν} L_{μν}² = k(k+2)` (Lemma 4.1(b)).

(d) With `e_4^* e_j = iσ_j`, `e_j^* e_4 = −iσ_j` and `e_j^* e_k = δ_{jk} + iε_{jkl} σ_l`, `U_s^* U_s = Σ_μ P_μ² + i Σ_j [P_4, P_j] σ_j + (i/2) Σ ε_{jkl}[P_j, P_k] σ_l`. Insert (b): this is `Σ_μ P_μ² − c_s^{−2} Σ_l (L_{4l} + ½Σ_{jk}ε_{jkl}L_{jk}) σ_l = Σ_μ P_μ² − (2/c_s²) N^-·σ`, since `L_{4l} = −K_l`. From (b), `[J_a, J_b] = iε_{abc}J_c`, `[J_a, K_b] = iε_{abc}K_c`, `[K_a, K_b] = iε_{abc}J_c`, so `[N^-_a, N^-_b] = iε_{abc} N^-_c`. Also `Σ_l J_l K_l = 0` on polynomials: written with `D`'s, every term contracts `ε_{jkl}` with a symmetric pair (`x_j x_l`, or `δ_{kl}`). So `(N^-)² = ¼(J² + K²) = C_4/4 = k(k+2)/4` on `H_k`. Put `T = N^-·σ`. Then `T² = (N^-)² + (i/2)Σε_{abc}[N^-_a, N^-_b]σ_c = (N^-)² − T`, so every eigenvalue `t` of `T` on `C² ⊗ H_k` solves `t² + t − k(k+2)/4 = 0`: `t ∈ {k/2, −(k+2)/2}`. Both `Σ_μ P_μ²` and `T` preserve each `C² ⊗ H_k`. So the eigenvalues of `U_s^* U_s` there are at most `(s(s+3) − k(k+2) + k + 2)/c_s² ≤ 1` for `k ≥ 1` (as `k² + k ≥ 2`), and equal `1` at `k = 0` (where `N^- = 0`). □

So `R_s` with `(L_{μν}, c_s P_μ)` is a representation of `so(5)` with Casimir `s(s+3)`, the value of the symmetric representation `[s, 0]` (Lemma 4.1(b) on `R⁵`), and of that representation's dimension `(s+1)(s+2)(2s+3)/6`. Irreducibility is not used and not claimed. The Chandrasekharan-Wiese link `U = U⁰ + iU·σ` is `U_s` up to a scalar normalization (`U⁰ ∝ P_4`, `U^j ∝ P_j`). `[pass-1 check, not reproduced]` (b), (c), (d) and `‖U_s‖² = 1` at `s = 1, 2, 3` (section 7).

### Lemma 4.3, Remarks 4.4 and 4.6: the coefficient bound and its limits

Write `ιU_sι^* = Σ_μ ιP_μι^* ⊗ e_μ` on `C² ⊗ 𝒦`, tensored with the identity on all other links. Put

`δ_s(M') = 2M'(M'+3)/(s(s+3))`.

**Lemma 4.3.** Let `0 ≤ M' ≤ s`, and let `v` be a vector whose component on one link lies in `H_0 ⊕ … ⊕ H_{M'}` (any state on the other links and on `C²`). Then `‖(ιU_sι^* − U) v‖ ≤ δ_s(M') ‖v‖` and `‖(ιU_sι^* − U)^* v‖ ≤ δ_s(M') ‖v‖`.

*Proof.* On vectors of finite flux put `U^± = Σ_μ x^±_μ ⊗ e_μ`, so `U = U^+ + U^-` there (Lemma 4.1(a)).

*Step 1: `‖U^± w‖ ≤ ‖w‖` for every finite-flux `w`.* For `w_k ∈ C² ⊗ H_k`, `U^+ w_k ∈ C² ⊗ H_{k+1}` and `U^- w_k ∈ C² ⊗ H_{k−1}` are orthogonal (Lemma 4.1(c)), and `U` is unitary; so `‖U^+ w_k‖² + ‖U^- w_k‖² = ‖w_k‖²`. For `w = Σ_k w_k` the vectors `U^+ w_k` lie in mutually orthogonal spaces, so `‖U^+ w‖² = Σ_k ‖U^+ w_k‖² ≤ ‖w‖²`; the same for `U^-`. Other tensor factors change nothing.

*Step 2: the difference.* `Y_s x^-_μ = x^-_μ Y'_s` with `Y'_s = Σ_{1≤k≤s} y_{k−1} Π_k`. So on flux at most `M' ≤ s`, `ιU_sι^* = U^+ Y_s + U^- Y'_s`, and `(ιU_sι^* − U) v = U^+(Y_s − 1)v + U^-(Y'_s − 1)v`. By Step 1 its norm is at most (using `U^-Π_0 = 0`) `max_{k≤M'}(1 − y_k) + max_{1≤k≤M'}(1 − y_{k−1})`, times `‖v‖`. Since `0 ≤ y_k ≤ 1`, `1 − y_k ≤ 1 − y_k² = k(k+3)/(s(s+3))`, which increases in `k`. Each maximum is at most `M'(M'+3)/(s(s+3))`.

*Step 3: the adjoint.* `(ιU_sι^* − U)^* = (Y_s − 1)(U^+)^* + (Y'_s − 1)(U^-)^*` on finite flux. `(U^+)^*` lowers the flux by one and `(U^-)^*` raises it by one, and both have norm at most one by Step 1. So the weights met are `1 − y_k` with `k ≤ M' − 1` and `1 − y_{k−1}` with `k ≤ M' + 1`, each at most `M'(M'+3)/(s(s+3))` (for `M' = s` the claim is trivial, as `δ_s(s) = 2` and both operators have norm at most one). □

**Remark 4.4 (the first member and the truncated space).** (i) At `s = 1`, `y_0 = 1` and `y_1 = 0`, so `ιU_1ι^* = Π_{≤1} U Π_{≤1}` exactly, with `Π_{≤1}` the projection onto `H_0 ⊕ H_1`. The five-state `SU(2)` link of Ludwig-Jakobs-Urbach (the `so(5)` vector representation) and the `j_max = 1/2` truncation of the MDTN note ("dim H_ℓ = 1 + 4 = 5") are therefore the same regulator, up to the choice of basis. (ii) For every `s`, `R_s` is the space Tong et al. keep at `Λ = s` (total angular momentum at most `s/2`; their dimension `(Λ+1)(Λ+2)(2Λ+3)/6`). For `s ≥ 2` the links differ: `y_1² = 1 − 4/(s(s+3)) < 1`, so `ιU_sι^* ≠ Π_{≤s} U Π_{≤s}`. For `s ≥ 2` the projected link is not an `so(5)` link with these `L_{μν}`: its components `Q_μ = Π_{≤s} x_μ Π_{≤s}` have weights 1 on `H_k → H_{k+1}` for `k < s`, so the computation in the proof of Proposition 4.2(b) gives `[Q_μ, Q_ν] = 0` on `H_1`, while `L_{μν} ≠ 0` there; no `c > 0` gives `[cQ_μ, cQ_ν] = iL_{μν}`.

**Remark 4.6 (the flux restriction cannot be removed).** Let `h ∈ H_s`, `h ≠ 0`, and let `u_1, u_2` be the basis of `C²`. The `H_{s+1}` component of `(ιU_sι^* − U)(u_a ⊗ h)` is `−U^+(u_a ⊗ h)`, since `ιU_sι^*` has none. With `tr(e_μ^* e_ν) = 2δ_{μν}` and Lemma 4.1(e), `Σ_a ‖U^+(u_a ⊗ h)‖² = 2Σ_μ ‖x^+_μ h‖² = 2a_s ‖h‖²`. So for some `a`, `‖(ιU_sι^* − U)(u_a ⊗ h)‖ ≥ √(a_s) ‖h‖ > ‖h‖/√2`. No bound of Lemma 4.3's form that tends to zero as `s → ∞` holds uniformly on `R_s`. This is the `SU(2)` form of the top-flux defect in the paragraph after `GA2_Y2.md` Corollary 2.2. On natural observables: `tr(U_s^* U_s) = 2Σ_μ P_μ² = 2/(s+3)` on `H_s`, by Proposition 4.2(c,d) (the trace of `σ_l` vanishes), while `tr(U^* U) = 2`.

**Correlator-level top-flux counterexample, R1.** (referee closure, GB1QL_REFEREE.md) Fix `s ≥ 1`, any `τ_E`, and `0 < |θ| ≤ 1/300`. Let `ℓ` be a link, `C` its tiling cube, `X = {ℓ}`, and `A = 1 − Π^ℓ_{≤s}`, the projection onto flux above `s` on `ℓ`. `A` is a function of `E²_ℓ`, so it is gauge invariant, `0`-flux-bounded, and `‖A‖ = 1`. Let `ψ_s` be the product vector with a unit `h ∈ H_s` on `ℓ` and the constant `1 ∈ H_0` on every other link of `Λ_1`, and let `ω_s`, `ω` be the vector states of `ψ_s` and `ψ = ι_Λψ_s`. They are matched at flux `s`. Then

`ω_s(α_s(ι_X^*Aι_X)) = 0` and `ω(α(A)) ≥ 0.9 θ²`.

So the error of Theorem 4.8(b) at `n = 1`, `M = s` is at least `0.9θ²`, for every `s`.

*Proof.*
1. `A` vanishes on `ran ι`, so `ι_X^*Aι_X = 0`.
2. `ψ` is an eigenvector of every `E²_{ℓ'}`, so `W_E ψ` is a phase times `ψ`. Gates of cubes other than `C` are unitary and commute with `A`. So `ω(α(A)) = ‖A g_C ψ‖²`.
3. Write `g_C = 1 − iθB_C + R`. With `‖B_C‖ ≤ 24` and `x = 24|θ| ≤ 0.08`, `‖R‖ ≤ e^x − 1 − x ≤ (x²/2)e^x ≤ 312θ²`. Since `Aψ = 0`, `‖Ag_Cψ‖ ≥ |θ|‖AB_Cψ‖ − 312θ²`.
4. A face of `C` that misses `ℓ` does not change the flux on `ℓ`, so it contributes nothing to `AB_Cψ`. The link `ℓ` lies in exactly two faces `p, p'` of `C`, which share no other link.
5. For `SU(2)` links, `tr X_p` is multiplication by a real function, so `B_p = 2 tr X_p` on `𝒦`. Move the factor of `ℓ` to the right end by cyclicity of the trace. Then `A tr X_p ψ = F_p := tr(Â G)`, where `Â` is the product of the other three link matrices or their adjoints (each a function of one link, of flux exactly one there), and `G = Σ_μ x^+_μh ⊗ e_μ` or `Σ_μ x^+_μh ⊗ e_μ^*` by the orientation of `ℓ` in `p`.
6. Haar orthogonality, rebuilt: on `S³`, `∫x_μx_ν dσ = δ_{μν}/4` (reflection and permutation symmetry, `Σx_μ² = 1`). With `Σ_μ (e_μ)_{cd}\overline{(e_μ)_{ab}} = 2δ_{ac}δ_{bd}` (the `e_μ/√2` are an orthonormal basis of `M_2(C)` up to phases), `∫\overline{g_{ab}}g_{cd} dσ = δ_{ac}δ_{bd}/2`, and the same for `g^*`. Write `Â = B_1 g B_2` with `g` (or `g^*`) one of its three factors and `B_1, B_2` the unitary products of the others. Integrating over that one link gives `∫\overline{Â_{ba}}Â_{dc} = (B_1B_1^*)_{db}(B_2^*B_2)_{ac}/2 = δ_{bd}δ_{ac}/2` pointwise in the other two links; Fubini applies because all entries are bounded. This gives `‖F_p‖² = ½ Σ_{ab}‖G_{ab}‖² = ½ Σ_{μν}⟨x^+_μh, x^+_νh⟩ tr(e_μ^*e_ν) = Σ_μ‖x^+_μh‖² = a_s`, by Lemma 4.1(d), (e).
7. `F_p` has flux one on the links of `p` other than `ℓ` and flux zero on those of `p'`; `F_{p'}` the reverse. So they are orthogonal, and `‖AB_Cψ‖² = 4a_s + 4a_s = 8a_s > 4`.
8. Hence `‖Ag_Cψ‖ ≥ 2|θ| − 312θ² ≥ 0.96|θ|` for `|θ| ≤ 1/300`, and `ω(α(A)) ≥ 0.92θ²`. □

### Lemmas 4.5 and 4.7: the light cone, one gate, one layer

**Lemma 4.5 (light cone).** Let `X` be a finite set of links whose endpoints lie in a box `Q_0 = [a, a+R]³ ∩ Z³`, `R ≥ 1`. Put `X^{(0)} = X`, `𝒞_i = {C ∈ 𝒞 : ℓ(C) ∩ X^{(i)} ≠ ∅}` and `X^{(i+1)} = ∪_{C∈𝒞_i} ℓ(C)`.

(a) `X^{(i)} ⊆ X^{(i+1)}`; the endpoints of `X^{(i)}` lie in `Q_i = [a−i, a+R+i]³`; and `|𝒞_i| ≤ |X^{(i)}| ≤ 3(R+2i+1)³`.

(b) For every bounded `A` on `𝒦^{⊗X}` and `n ≥ 1`, `α^n(A) = W_n^* A W_n` with `W_n = V_0 V_1 ⋯ V_{n−1}` and `V_i = (∏_{C∈𝒞_i} g_C)(∏_{ℓ∈X^{(i+1)}} e^{−iτ_E E²_ℓ})`. The same holds for `α_s`, with `g^s_C` and the same index sets. `W_n` acts on `Λ_n := X^{(n)}`.

(c) The number of cube gates in `W_n` is `G_n := Σ_{i<n} |𝒞_i| ≤ 3n(R+2n)³`, for every lattice volume.

*Proof.* (a) Every link lies in exactly one tiling cube, so each link of `X^{(i)}` contributes at most one cube, and its own cube puts it in `X^{(i+1)}`. A unit cube with a link whose endpoints lie in `Q_i` has its eight vertices in `Q_{i+1}`. A box of side `R'` has `3R'(R'+1)² ≤ 3(R'+1)³` links. (b) Let `B` be supported in a finite `Y`. In `α(B) = W_E^* W_B^* B W_B W_E`, a cube gate whose links miss `Y` commutes with `B` and with every other cube gate (disjoint supports), so it cancels. The rest is supported in `Y' = ∪_{ℓ(C)∩Y≠∅} ℓ(C)`, and electric gates off `Y'` cancel in the same way. Adding gates that commute with `B` does not change the result, so `α(B) = V_Y^* B V_Y` for the `V_Y` built from any `Y ⊇ supp B`. Induction: `α^n(A) = α(W_{n−1}^* A W_{n−1}) = V_{n−1}^* W_{n−1}^* A W_{n−1} V_{n−1}`. (c) Sum (a) over `i ≤ n−1`. □

So for a local observable only the gates of a finite backward light cone act, on the infinite lattice and on every periodic box that carries the cube tiling and is large enough that `Λ_n` does not wrap. No Lieb-Robinson bound is needed: the tick is a finite-depth circuit.

**Embedded framework gates.** On the links of a cube `C` put `B̃_C = ι B^s_C ι^*` and `g̃_C = e^{−iθ B̃_C}`. Since `ιι^*` is the projection onto `ι(R_s^{⊗ℓ(C)})` and `B̃_C` vanishes on its complement, `g̃_C` equals `ι g^s_C ι^*` on the embedded space and the identity on its complement; it is unitary. By Proposition 4.2(d), `‖tr X^s_p‖ ≤ 2`, so `‖B̃_C‖ ≤ 24`; also `‖B_C‖ ≤ 24`. Put `β = 24`, `t_K = e^{β|θ|}(β|θ|)^{K+1}/(K+1)!`.

**Lemma 4.7 (one gate, one layer).** Let `K ≥ 0` and `M' + K ≤ s`. For a cube `C` let `P_C` and `Q_C` project onto flux at most `M'` and at most `M'+K` on the 12 links of `C`.

(a) `‖(g̃_C − g_C) P_C‖ ≤ 96|θ| e^{β|θ|} δ_s(M'+K) + 2t_K`.

(b) For `g = g_C` and for `g = g̃_C`, `‖(1 − Q_C) g P_C‖ ≤ t_K`. For a finite set `𝒞'` of cubes, `P = ∏_{C∈𝒞'} P_C` and `Q = ∏_{C∈𝒞'} Q_C`: `‖(1 − Q)(∏_{C∈𝒞'} g) P‖ ≤ |𝒞'| t_K`, for both kinds of gate.

(c) `‖(∏_{C∈𝒞'} g̃_C − ∏_{C∈𝒞'} g_C) P‖ ≤ |𝒞'| [96|θ| e^{β|θ|} δ_s(M'+K) + 2t_K]`.

*Proof.* *Plaquettes.* Let `v` have flux at most `M'' ≤ s` on the four links of a face `p`. Write `X_p = F_1F_2F_3F_4` and `X̃_p = ιX^s_pι^* = F̃_1F̃_2F̃_3F̃_4`, where `F̃_i` is `ιU_sι^*` or its adjoint on link `ℓ_i`. Telescope: `X̃_p − X_p = Σ_i F_1⋯F_{i−1}(F̃_i − F_i)F̃_{i+1}⋯F̃_4`. Apply it to `u_a ⊗ v`. The factors right of position `i` act on other links, so link `ℓ_i` still has flux at most `M''`; Lemma 4.3 bounds the middle factor by `δ_s(M'')`, and the other factors have norm at most one (`U` unitary, Proposition 4.2(d)). So `‖(X̃_p − X_p)(u_a ⊗ v)‖ ≤ 4δ_s(M'')‖v‖` and `‖(tr X̃_p − tr X_p)v‖ ≤ Σ_a ‖(X̃_p − X_p)(u_a ⊗ v)‖ ≤ 8δ_s(M'')‖v‖`. The adjoint `(tr X_p)^* = tr(X_p^*)` is the reversed product, with the same bound. So `‖(B̃_p − B_p)v‖ ≤ 16δ_s(M'')‖v‖`, and over the six faces `‖(B̃_C − B_C)v‖ ≤ 96δ_s(M'')‖v‖`.

(a) Write `e^{−iθB} = T_K(B) + R_K(B)` with `T_K(B) = Σ_{j≤K}(−iθB)^j/j!`; then `‖R_K(B)‖ ≤ Σ_{j>K}(β|θ|)^j/j! ≤ t_K` for `‖B‖ ≤ β`. Each `B̃_p` and `B_p` changes the flux of each of its links by at most one, so `B̃_C^i v` has flux at most `M'+i` on `ℓ(C)` for `v ∈ ran P_C`. Telescoping `B̃_C^j − B_C^j = Σ_{i<j} B_C^{j−1−i}(B̃_C − B_C)B̃_C^i` gives `‖(B̃_C^j − B_C^j)v‖ ≤ jβ^{j−1}·96δ_s(M'+K)‖v‖` for `j ≤ K`. Summing, `Σ_{j=1}^K |θ|^j jβ^{j−1}/j! ≤ |θ|e^{β|θ|}`. The two remainders add `2t_K`.

(b) `T_K(B)` raises the flux on `ℓ(C)` by at most `K`, so `(1 − Q_C)T_K P_C = 0` and `(1 − Q_C)gP_C = (1 − Q_C)R_K P_C`. For a layer (this is the referee's leak closure of `GB1.md` line 113, ported): gates of distinct cubes act on disjoint links and commute with the other cubes' projections, so `(∏g)P = ∏(gP_C)`. Write `gP_C = A_C + D_C` with `A_C = Q_C g P_C` and `D_C = (1 − Q_C) g P_C`. Then `‖A_C‖ ≤ 1`, `‖A_C + D_C‖ ≤ 1` and `‖D_C‖ ≤ t_K`, and telescoping gives `‖∏(A_C + D_C) − ∏A_C‖ ≤ |𝒞'|t_K`. The range of `∏A_C` lies in `ran Q`.

(c) Telescope over the cubes of `𝒞'` in a fixed order. In each term the gates to the right act on other links, so they keep flux at most `M'` on `ℓ(C)`; apply (a). The gates to the left are unitary. □

### Theorem 4.8: the main theorem

**Theorem 4.8 (GB1-QL for the `so(5)` family, bounded flux).** Fix `s ≥ 1`, angles `θ, τ_E ∈ R`, a finite link set `X` with endpoints in a box of side `R ≥ 1`, and integers `n ≥ 1`, `M ≥ 0`, `K ≥ 0` with `M + nK ≤ s`. Let `Λ = Λ_n = X^{(n)}` (so `|Λ| ≤ 3(R+2n+1)³`) and `G_n ≤ 3n(R+2n)³` as in Lemma 4.5, and put

`ε_n = G_n [96|θ| e^{24|θ|} δ_s(M+nK) + 2t_K] + 2nG_n t_K`, with `δ_s(M') = 2M'(M'+3)/(s(s+3))` and `t_K = e^{24|θ|}(24|θ|)^{K+1}/(K+1)!`.

(a) For every unit vector `ψ_s ∈ R_s^{⊗Λ}` of flux at most `M` on every link of `Λ`: `‖ι_Λ W^{(s)}_n ψ_s − W_n ι_Λ ψ_s‖ ≤ ε_n`.

(b) For every pair `(ω_s, ω)` matched at flux `M` on `Λ` and every bounded `A` on `𝒦^{⊗X}`:

`|ω_s(α_s^n(ι_X^* A ι_X)) − ω(α^n(A))| ≤ 2‖A‖ ε_n`.

If `A` is gauge invariant, so is the framework observable `ι_X^* A ι_X`. The bound depends on the lattice only through `R` and `n`: it is the same on `Z³` and on every periodic box in which `Λ_n` does not wrap. It does not depend on `τ_E`. It increases in `n`, so for a stated time `T` it holds for all `n ≤ T` with `ε_T`, provided `M + TK ≤ s`.

(c) (Rate.) Take `K = ⌈(log s)²⌉`. If `K + 1 ≥ 24e³|θ|` and `M + nK ≤ s`, then `t_K ≤ e^{24|θ|} s^{−2 log s}`, and

`ε_n ≤ 3n(R+2n)³ [192|θ| e^{24|θ|} (M + n(log s)² + n + 3)²/s² + (2n+2) e^{24|θ|} s^{−2 log s}]`.

For fixed `θ`, `R`, `n` and `M` this is `O((log s)⁴/s²)`, the rate of `GB1.md` Theorem 5.2.

*Proof.* (a) Let `Ṽ_i` be `V_i` with each `g_C` replaced by `g̃_C`. Every factor of `Ṽ_i` preserves `ι_Λ(R_s^{⊗Λ})` and acts there as the matching framework gate (the electric gates commute with `ι`, since `ι` intertwines `E²`). So `ι_Λ W^{(s)}_n ψ_s = Ṽ_0 ⋯ Ṽ_{n−1} ψ` with `ψ = ι_Λ ψ_s`. Telescope:

`Ṽ_0⋯Ṽ_{n−1} − V_0⋯V_{n−1} = Σ_{i=0}^{n−1} V_0⋯V_{i−1}(Ṽ_i − V_i)Ṽ_{i+1}⋯Ṽ_{n−1}`.

Let `φ_i = Ṽ_{i+1}⋯Ṽ_{n−1} ψ`, the vector after `n−1−i` framework ticks, and `M_i = M + (n−1−i)K`. *Leak.* Claim: `‖(1 − Π^Λ_{M_i}) φ_i‖ ≤ Σ_{j>i} |𝒞_j| t_K ≤ G_n t_K`. It holds for `i = n−1`. If `φ = Π^Λ_{M'} φ + r`, then the electric layer of `Ṽ_j` preserves `Π^Λ_{M'}`; by Lemma 4.7(b) the magnetic layer sends `Π^Λ_{M'}φ` to a vector whose part above flux `M'+K` on the links of `𝒞_j` has norm at most `|𝒞_j|t_K`; and links of `Λ` outside those cubes keep their flux. So `‖(1 − Π^Λ_{M'+K}) Ṽ_j φ‖ ≤ |𝒞_j| t_K + ‖r‖`. *One tick.* The electric parts of `Ṽ_i` and `V_i` are equal and preserve `Π^Λ_{M_i}`. Lemma 4.7(c), with `M' = M_i` and `M_i + K ≤ M + nK ≤ s`, gives `‖(Ṽ_i − V_i)Π^Λ_{M_i} φ_i‖ ≤ |𝒞_i| [96|θ|e^{24|θ|}δ_s(M+nK) + 2t_K]`. The remaining part costs at most `2‖(1 − Π^Λ_{M_i})φ_i‖ ≤ 2G_n t_K`. The left factors `V_0⋯V_{i−1}` are unitary. Sum over `i`.

(b) By Lemma 4.5(b), `α^n(A) = W_n^*(A ⊗ 1)W_n` and `α_s^n(ι_X^*Aι_X) = W_n^{(s)*}(ι_X^*Aι_X ⊗ 1)W^{(s)}_n` on `Λ`, so both sides depend only on the restrictions `ρ_s` and `ρ = ι_Λρ_sι_Λ^*`. For a unit `ψ_s` in the support of `ρ_s`, put `a = ι_Λ W^{(s)}_n ψ_s` and `b = W_n ι_Λ ψ_s`. Then `⟨W^{(s)}_nψ_s, (ι_X^*Aι_X ⊗ 1)W^{(s)}_nψ_s⟩ = ⟨a, (A ⊗ 1)a⟩`, and `|⟨a, Aa⟩ − ⟨b, Ab⟩| ≤ ‖A‖(‖a‖ + ‖b‖)‖a − b‖ ≤ 2‖A‖ε_n` by (a). Decompose `ρ_s` into its eigenvectors, which lie in `F_M(Λ)`, and average. Gauge invariance passes to `ι_X^*Aι_X` because `ι` intertwines the gauge action (section 1.4). The volume statement is Lemma 4.5(c). Monotonicity in `n`: `G_n`, `δ_s(M+nK)` and `nG_n` increase in `n`.

(c) Stirling's bound `(K+1)! ≥ ((K+1)/e)^{K+1}` gives `t_K ≤ e^{24|θ|}(24e|θ|/(K+1))^{K+1} ≤ e^{24|θ|}e^{−2(K+1)} ≤ e^{24|θ|}e^{−2(log s)²}` when `K + 1 ≥ 24e³|θ|`. Also `δ_s(M') ≤ 2(M'+3)²/s²` and `nK ≤ n(log s)² + n`. □

`[pass-1 check, not reproduced]` one plaquette at `s = 1, 2`, flux `M ≤ 1`, `θ ∈ {0.05, 0.2}`: the gate difference lies between `3 × 10^{−3}` and `0.4`, far below the one-plaquette form of Lemma 4.7(a)'s first term, `16|θ|e^{4|θ|}δ_s(M+1)` (section 7). The check compares with a truncated Kogut-Susskind register and guides only.

**What Theorem 4.8 does not say.** The order of limits is: fix `X`, `n`, `M`, then let `s` grow. Remark 4.6 shows the flux bound cannot be dropped, and `ε_n` grows like `n⁴ (M + n(log s)²)²/s²` in `n`. So the theorem gives no statement uniform in all ticks, and none for states with unbounded flux; Corollary 4.9 treats states with bounded local electric energy. It concerns the Trotterized model with the cube-face layer, as fixed in section 1.3, at any angles; it does not choose angles, a vacuum or a continuum limit.

### Corollaries 4.9 and 4.10: bounded local electric energy, and two-time correlators

**Corollary 4.9 (bounded local electric energy).** Keep the data of Theorem 4.8, and let `0 ≤ M ≤ s` with `η := 4|Λ| e/((M+1)(M+3)) < 1`.

(a) Let `ω` be a Kogut-Susskind state whose restriction `ρ` to `Λ` is a density matrix with `ω(E²_ℓ) ≤ e` for all `ℓ ∈ Λ`. Put `ρ' = Π^Λ_M ρ Π^Λ_M / tr(Π^Λ_M ρ)` and `ρ'_s = ι_Λ^* ρ' ι_Λ`. Then `(ρ'_s, ρ')` is matched at flux `M`, and for every bounded `A` on `𝒦^{⊗X}`:

`|ω'_s(α_s^n(ι_X^*Aι_X)) − ω(α^n(A))| ≤ ‖A‖ (2ε_n + 2√η + η)`.

(b) Let `ω_s` be a framework state with `ω_s(E²_ℓ) ≤ e` for all `ℓ ∈ Λ`, and `ω` its image (`ρ = ι_Λ ρ_s ι_Λ^*`). Then `|ω_s(α_s^n(ι_X^*Aι_X)) − ω(α^n(A))| ≤ ‖A‖ (2ε_n + 4√η + 2η)`.

(c) (Rate.) Take `M = ⌊s^{2/3}⌋` and `K = ⌈(log s)²⌉`. For `s` large enough that `M + nK ≤ s`, `η < 1` and `K + 1 ≥ 24e³|θ|`, the bounds of (a) and (b) are `O(s^{−2/3})`, with constants depending only on `θ`, `R`, `n` and `e`.

*Proof.* `E² = k(k+2)/4 ≥ (M+1)(M+3)/4` on `H_k` for `k > M`. So for one link, `tr(ρ(1 − Π^ℓ_M)) ≤ 4ω(E²_ℓ)/((M+1)(M+3))` (Markov's inequality for the spectral measure of `E²_ℓ` in `ρ`). For commuting projections, `1 − ∏_ℓ Π^ℓ_M ≤ Σ_ℓ (1 − Π^ℓ_M)`, so `η' := tr(ρ(1 − Π^Λ_M)) ≤ η`. For a unit vector `ψ`, `‖|ψ⟩⟨ψ| − |Πψ⟩⟨Πψ|‖_1 ≤ ‖ψ − Πψ‖(‖ψ‖ + ‖Πψ‖) ≤ 2‖(1−Π)ψ‖`, because `|a⟩⟨a| − |b⟩⟨b| = |a−b⟩⟨a| + |b⟩⟨a−b|` and a rank-one operator `|u⟩⟨v|` has trace norm `‖u‖‖v‖`. Average over the eigenvectors of `ρ` and use concavity of the square root: `‖ρ − ΠρΠ‖_1 ≤ 2√η'`. Normalizing costs `‖ΠρΠ − ρ'‖_1 = 1 − tr(Πρ) = η'`. So `‖ρ − ρ'‖_1 ≤ 2√η + η`, and `|ω(B) − ω'(B)| ≤ ‖B‖‖ρ − ρ'‖_1` for `B = α^n(A)`, `‖B‖ = ‖A‖`. Add Theorem 4.8(b) for the matched pair. In (b), compress on both sides; `ι_Λ` is isometric and intertwines `E²`, so the same `η` bounds both compressions. (c) `δ_s(M + nK) = O(s^{−2/3})` and `√η = O(s^{−2/3})`. □

For states supported on finite flux, as every framework state is, the proof uses only finite sums. For a general Kogut-Susskind state in (a) it uses the spectral decomposition `E² = Σ_k (k(k+2)/4) Π_k`, that is, the density of `⊕_k H_k` (section 1.1).



**Corollary 4.10 (two-time correlators, and the natural loops).** Let `A_1, A_2` be bounded on `𝒦^{⊗X_1}`, `𝒦^{⊗X_2}`, with `A_2` `d`-flux-bounded, and `X_1 ∪ X_2` in a box of side `R`. Let `n_1, n_2 ≥ 0`, `n̂ = max(n_1, n_2)`, `Λ = (X_1 ∪ X_2)^{(n̂)}`, `G = 3n̂(R+2n̂)³`, and `M̂ = M + (n_1 + 2n_2)K + d ≤ s`. Let `ε̂ = G[96|θ|e^{24|θ|}δ_s(M̂) + 2t_K] + 2n̂ G t_K`.

(a) For every pair `(ω_s, ω)` matched at flux `M` on `Λ`:

`|ω_s(α_s^{n_1}(ι^*A_1ι) α_s^{n_2}(ι^*A_2ι)) − ω(α^{n_1}(A_1) α^{n_2}(A_2))| ≤ ‖A_1‖‖A_2‖ (4ε̂ + 7G t_K)`.

(b) Let `γ` be a closed path of `r` links, each used once, with `W_γ = tr(F_1⋯F_r)` and `W^s_γ` its framework version built from `U_s`. If `M + nK + 1 ≤ s`, then for every pair matched at flux `M` on `Λ_n`: `|ω_s(α_s^n(W^s_γ)) − ω(α^n(W_γ))| ≤ 2rδ_s(M+nK) + 4ε_n + 6G_n t_K`.

*Proof.* Two facts from the proof of Theorem 4.8, for any product `W̃` of embedded framework ticks or of their inverses (Lemma 4.7 holds for `−θ`), with Kogut-Susskind counterpart `W` and `n` factors: (R1) for every embedded `φ` and `M' + nK ≤ s`, `‖(W̃ − W)φ‖ ≤ ε_n(M')‖φ‖ + 2‖(1 − Π_{M'})φ‖`, where `ε_n(M')` is `ε_n` with `M'` in place of `M`; (R2) `‖(1 − Π_{M'+nK})W̃φ‖ ≤ ‖(1 − Π_{M'})φ‖ + G_n t_K‖φ‖`, and the same for `W`. Here `Π_{M'} = Π^Λ_{M'}`. For (R1), apply Theorem 4.8(a) to `Π_{M'}φ`, and bound `(W̃ − W)(1 − Π_{M'})φ` by `2‖(1 − Π_{M'})φ‖`.

(a) Take a unit `ψ` in the support, embedded, of flux at most `M`. Write `W, Z` for the Kogut-Susskind words of `n_2, n_1` ticks, `W̃, Z̃` for the embedded framework words, and `Π_s = ιι^*`. The framework correlator is `⟨Z̃ψ, Π_sA_1Π_s Z̃W̃^*Π_sA_2Π_sW̃ψ⟩ = ⟨Z̃ψ, A_1 ṽ_4⟩`, with `ṽ_1 = W̃ψ`, `ṽ_2 = Π_sA_2ṽ_1`, `ṽ_3 = W̃^*ṽ_2`, `ṽ_4 = Z̃ṽ_3`; all these are embedded, so the outer `Π_s` drop. The Kogut-Susskind correlator is `⟨Zψ, A_1v_4⟩` with `v_1 = Wψ`, `v_2 = A_2v_1`, `v_3 = W^*v_2`, `v_4 = Zv_3`. By (R2), `ṽ_1` has flux at most `M_1 = M + n_2K` up to `r_1 ≤ Gt_K`; `ṽ_2` has flux at most `M_1 + d` up to `‖A_2‖r_1`; `ṽ_3` has flux at most `M_1 + d + n_2K` up to `r_3 ≤ 2‖A_2‖Gt_K`. Now: `‖ṽ_1 − v_1‖ ≤ ε̂`. `‖ṽ_2 − v_2‖ ≤ ‖A_2‖ε̂ + ‖(1 − Π_s)A_2v_1‖ ≤ ‖A_2‖(ε̂ + Gt_K)`, since `v_1` has flux at most `M_1` up to `Gt_K` and `M_1 + d ≤ s`. `‖ṽ_3 − v_3‖ ≤ ‖(W̃^* − W^*)ṽ_2‖ + ‖ṽ_2 − v_2‖ ≤ ‖A_2‖(2ε̂ + 3Gt_K)`, by (R1). `‖ṽ_4 − v_4‖ ≤ ‖(Z̃ − Z)ṽ_3‖ + ‖ṽ_3 − v_3‖ ≤ ‖A_2‖(3ε̂ + 7Gt_K)`. Finally `|⟨Z̃ψ, A_1ṽ_4⟩ − ⟨Zψ, A_1v_4⟩| ≤ ‖Z̃ψ − Zψ‖‖A_1‖‖A_2‖ + ‖A_1‖‖ṽ_4 − v_4‖`. All cutoffs used are at most `M̂`. Average over `ρ_s`.

(b) `ιW^s_γι^* − W_γ` telescopes as in Lemma 4.7: on vectors of flux at most `M'` (`M' + 1 ≤ s`) its norm is at most `2rδ_s(M')`. Then `|⟨ṽ, ιW^s_γι^*ṽ⟩ − ⟨ṽ, W_γṽ⟩| ≤ 2rδ_s(M+nK) + 2·2·G_nt_K` for `ṽ = W̃ψ` (flux at most `M+nK` up to `G_nt_K`, `‖W_γ‖ ≤ 2`, `‖ιW^s_γι^*‖ ≤ 2`), and `|⟨ṽ, W_γṽ⟩ − ⟨Wψ, W_γWψ⟩| ≤ 4ε_n`. Two leak terms of size `G_nt_K` are absorbed in `6G_nt_K`. □

### 4.11 (Proposition 4.11): a five-mode realisation, the rung test law `L5[SU(2), s]`

This names the "other five-mode realisation" the brief allows. It is a rung test law in the sense of `GB1.md` Theorem 5M, proposed and not adopted; its four tests are in section 4.



**Proposition 4.11.** (a) Every gate of `L5[SU(2), s]` commutes with the `SU(2)` gauge action at every site. (b) Orientation reversal `U_ℓ ↦ U_ℓ^*` is implemented on `R_s` by a unitary. (c) Finite depth under NN-a, and cell covariance, hold as in `GB1.md` Theorem 5M(1). (d) For every state with `ω(N_x) = 0` at every site, every bounded link observable `B` and every `n ≥ 0`, `ω(α^n(B))` equals the expectation under the pure-gauge framework tick of section 1.3. So Theorem 4.8 and Corollaries 4.9-4.10 hold for `L5[SU(2), s]` on states with empty matter.

*Proof.* (a) `d_y^† U_ℓ d_x ↦ d_y^† h_y^{−1} h_y U_ℓ h_x^{−1} h_x d_x`. `E²` is a Casimir. `tr X_p` is invariant by cyclicity, and each matter gate is an exponential of invariant terms. (b) Inversion `g ↦ g^{−1}` is `x ↦ (−x_1, −x_2, −x_3, x_4)`, an orthogonal map. It preserves every `H_k`. Multiplication by `x_μ`, `∂_μ` and `|x|²` transform covariantly under orthogonal maps, so the induced unitary `J` maps `P_j ↦ −P_j`, `P_4 ↦ P_4`, that is, `U_s ↦ U_s^*` entrywise as a matrix. (c) Ported from `GB1.md` Theorem 5M(1), with its citation of `GA1_5.md` Lemma U ("holds for five-mode sites and any finite registers") and Proposition C. Its proof uses only that each hop term is even, lies in one edge triple, and that the cell lifts act on all flavours alike, together with an orientation-reversal unitary on the link, which (b) supplies. (d) This is the proof of `GB1.md` Theorem 3.3, ported: positivity of `Σ_x N_x` on each finite region forces the reduced density matrix onto the matter vacuum; every term of `h_ℓ` annihilates the matter vacuum; so the matter layers act as the identity there, and the link layers do not touch matter. □

So, for this named five-mode realisation, the framework's gauge-invariant correlators on states with empty matter approach those of Trotterized Kogut-Susskind `SU(2)` on `Z³` as `s → ∞`, at the rates of Theorem 4.8 (bounded flux, `O((log s)⁴/s²)`) and Corollary 4.9 (bounded local electric energy, `O(s^{−2/3})`), uniformly in the volume and in `n ≤ T`. Matter is not compared: with matter present the hop layers act, and the matter-coupled Kogut-Susskind comparison is not attempted here.

### 4.12 (Proposition 4.12): the `L5-U` route and its first failing step

The route the brief names first has these steps.

- **(U1) Sector reduction.** Holds: `GB1.md` Theorem 6.1 (SU2-C). On the frozen-spectator, empty-matter class `𝒮_J`, the block flavours `{4, 5}` evolve as the Trotterized `U(2)` rishon quantum link model with `m' = m − 2k ∈ {1, 2, 3}` block rishons per link, on the register `Λ^{m'}C⁴`.
- **(U2) A family of block registers whose size grows, inside the law.** **Fails.** `L5-U[m]` has one register, `Λ^m C^{10}` with `m` fixed. `LW1_5_DRAFT.md` line 316 lists the free data: "`ε, μ` with `0 ≤ μ < 2ε < π`; the register `R`; `τ_E` (zero allowed); the plaquette class (open); `ω_0`". Line 318 replaces the register for `L5-U`: "items 2-3 replaced by the rishon register of Theorem U (free datum `m`, `1 ≤ m ≤ 9`)". The block register then has dimension `C(4, m') ≤ 6`, and no other free datum changes it. Under ZM1-INV, "Coarse sites carry the same five-mode construction as the fine sites, with any allowed coarse m₁ (R-form)" (`TOE_ASSEMBLY.md` 3.9), so zoom rungs carry the same bound (`GB1.md` line 165: "rung n≥1 supplies no C² or spin-S coarse register"). So "as the register size grows" has no instance inside `L5-U`. This is the failed attempt recorded in the digest (`GB1.md` line 182); the step named here is the same one, and it comes first.

Two further steps would follow (U2) on any route that supplied a growing `U(2)` block register, such as the recorded alternative `L5-U[ρ]` (`GA2_Y2.md` line 166, not adopted). They are named, not attempted. **(U3a) `U(2)` to `SU(2)`:** the block plaquette is a `U(2)` trace and carries the `U(1)` phase; the determinant mechanism "changes the gauge symmetry" (`LIT_QLM.md` line 23). **(U3b) The electric layer:** `L5-U`'s item 6 is a function of end numbers. Proposition 4.12 shows what this gives in the block now; for a register with two rishon flavours per colour, the end number 2 already contains spin 0 and spin 1 (`Λ²(C²⊗C²) = Sym²C²⊗Λ²C² ⊕ Λ²C²⊗Sym²C²`), so a function of end numbers is not then the `SU(2)` Casimir.

**Proposition 4.12 (the electric layer of the `SU(2)` block of `L5-U`).** On the class `𝒮_J` of `GB1.md` Theorem 6.1, with `m' = m − 2k`, the block electric term there, `H_E^{(2)} = Σ_ℓ (N^B_{ℓ,x} + k − m/2)² = Σ_ℓ (N^B_{ℓ,x} − m'/2)²`, satisfies:
(i) for `m' ∈ {1, 3}`, `(N^B_{ℓ,x} − m'/2)² = 1/4` on the class, so the electric layer acts there as a scalar phase on every finite region;
(ii) for `m' = 2`, `(N^B_{ℓ,x} − 1)² = 1 − (4/3)E²_{ℓ,x}`, where `E²_{ℓ,x}` is the `SU(2)` Casimir of the two block modes at the `x`-end.

*Proof.* Each end has two block modes, and `N^B_{ℓ,x} + N^B_{ℓ,y} = m'`. For `m' = 1`, `N^B_{ℓ,x} ∈ {0, 1}`; for `m' = 3`, `N^B_{ℓ,x} ∈ {1, 2}`; in both cases `(N^B_{ℓ,x} − m'/2)² = 1/4`. For `m' = 2`, `N^B_{ℓ,x} ∈ {0, 1, 2}`. Zero or two fermions in a doublet of modes form an `SU(2)` singlet; one fermion forms the doublet. So `E²_{ℓ,x} = (3/4)·[N^B_{ℓ,x} = 1]`, while `(N^B_{ℓ,x} − 1)² = 1 − [N^B_{ℓ,x} = 1]`. □

So inside `L5-U`, the `SU(2)` block has no electric dynamics at odd `m'`, and at `m' = 2` its electric coefficient is `−(4/3)τ_E` with a constant. This is a fact about the fixed register; it neither helps nor blocks (U2).

**`L5-O`.** Its register is free data (`LW1_5_DRAFT.md` line 305: "a finite-dimensional unitary representation of `𝔨 = so(20)` (Lemma Q). Free datum."), so a growing family exists among its laws. One law still has one register (`GA2_Y2_DRAFT.md` (a1): "one law has one register"), and the frozen `SU(2)` route on `L5-O` fails first at the matter layer (`GB1.md` Lemma O2). Whether some `so(20)` representation family realises the family `R_s` of section 1.2 in an `SU(2)` block of `L5-O`, with a class on which that block evolves on its own, is not attempted: **GB1-QL[`L5-O`]**.

## 3. The hand-off to T0-start

T0-start[G] (`GA2_Y2_DRAFT.md` line 211) puts these hypotheses on the start: "every gauge-invariant, reflection-positive probability measure `μ` on `G`-valued links of `a_{k_0}Z^4`, with Haar reference measure and density in `𝒜_{k_0}(g)` for some `g ≤ g_*`". Each row says what Theorem 4.8 with Proposition 4.11 delivers. "Delivered" means proved here or in a frozen item cited; "approximately" means with an error that tends to zero only in the stated order of limits.

**Lemma H (dependency order).** (referee closure, GB1QL_REFEREE.md) In this sentence, (H-GI), (H-RP), (H-Haar) and (H-class) are properties of one object, the measure `μ` that (H-4D) asks for. (H-G) fixes the group. So a hand-off that supplies no `μ` supplies none of the four properties, and the first input it lacks, after (H-G), is (H-4D).

*Proof.* Read the quoted noun phrase. "gauge-invariant" and "reflection-positive" modify "probability measure `μ`"; "with Haar reference measure" and "density in `𝒜_{k_0}(g)`" are attached to `μ`; "on `G`-valued links of `a_{k_0}Z^4`" names its configuration space. A property of `μ` is decided only once `μ` is given. □

| Hypothesis of T0-start[SU(2)] | Decision | Reason |
|---|---|---|
| (H-G) `G = SU(2)`, acting locally | Delivered in the test law | It is an exact local gauge group of `L5[SU(2), s]` (Proposition 4.11(a)); no classification excluding additional symmetries is proved. In `L5-U` and `L5-O` it is an exact subgroup (`GB1.md` §8, row H1a), but the route of section 4.12 stops at (U2). |
| (H-4D) a probability measure `μ` on `G`-valued links of `a_{k_0}Z⁴` | **Not delivered. The first missing input (Lemma H).** | Theorem 4.8 is a real-time statement for a unitary tick on `Z³`. `GB1.md` Theorem 2.1 (F1-F2): a unitary tick is not a positive transfer, and the tick does not fix a Hermitian logarithm. A Euclidean measure needs GB1's inputs E-1 (a quasi-energy lift), E-2 (the state's relation to it) and E-3 (a time-continuum family joined to a Euclidean limit). None is supplied here. |
| (H-GI) `μ` gauge invariant | Not delivered; a property of the missing `μ` | Proved instead, at slice level: both ticks commute with the gauge action, `ι` intertwines it, and `ι^*Aι` is gauge invariant when `A` is. The classes `S_M`, `E_e` admit non-invariant states. |
| (H-Haar) `μ` has Haar reference measure | Not delivered; a property of the missing `μ` | Slice analogue proved: each target link space is `L²(SU(2), Haar)`, and over one time slice their tensor product is T0's `H_W = ⊗_b L²(SU(2))` (`GA2_Y2.md` line 63, Corollary Y2-0(ii)). Correlators approach it at `O((log s)⁴/s²)` on `S_M` and `O(s^{−2/3})` on `E_e`, at fixed support, ticks and bound. Remark 4.6 and R1 exclude a flux-uniform version. |
| (H-RP) reflection positivity | Not delivered; a property of the missing `μ` | Needs E-1 and E-2 (`GB1.md` §8, row H3). |
| (H-class) density in `𝒜_{k_0}(g)`, `g ≤ g_*` | Not delivered; a property of the missing `μ` | Theorem 4.8 compares states and dynamics at the bare scale; it says nothing about effective actions, block maps or small-field and large-field structure. Small `g` in Kogut-Susskind units is a choice of angles, not a consequence. |
| Uniformity in `a`, `L` | Not a hypothesis on `μ` | It sits in T0-start's conclusion (i). Independence of the lattice volume (`L`) holds for local observables (Lemma 4.5(c)). There is no `a → 0` statement, and the error grows with `n` and with the flux or energy bound. |
| T0-rate | Not delivered | No running coupling or continuum rate is addressed. |

**The answer, exactly.** GB1-QL delivers (H-G) in the named test law. The hand-off fails first at (H-4D): no probability measure on links of a four-dimensional lattice is constructed. (H-GI), (H-Haar), (H-RP) and (H-class) are properties of that measure and are not delivered. GB1-QL delivers slice-level analogues of two of them: gauge-covariant ticks with an equivariant comparison map, and the approach of framework correlators to the Kogut-Susskind slice space `L²(SU(2), Haar)`, with rates, for local observables, uniformly in volume and in ticks up to a stated time, on states of bounded flux or bounded local electric energy. The `a`-uniformity and T0-rate are not delivered.

**Relation to the other requests.** `GA2_Y2.md` line 178 records T0-QLR[G]: "a controlled joint quantum-link/register limit" with T0's conclusions. Theorem 4.8 is the TOE-side regulator-error part of such a limit for `SU(2)`, in Hamiltonian form and for finite time: it controls `s → ∞` at fixed `X`, `n` and `M`. It supplies none of T0's conclusions. In `GB1.md` §8, row H1b says Haar links "Cannot be delivered through a ZM1-INV readout ... Correlator-level and Euclidean-variable routes are not excluded." Theorem 4.8 is a correlator-level route of that kind, for the test-law family; it uses no readout, so it does not conflict with Corollary R1.

## 4. Candidate readings for the owner, four-tested

The four tests (`LW1_5_DRAFT.md` line 328, as quoted in `GA2_Y2_DRAFT.md` §4.3): "(1) states or fixes a part's target; (2) open-ended; (3) settles a downstream physics question by premise; (4) adds structure or constants its own reasons do not need." P = pass, C = conditional, F = fail. Nothing below is adopted; only the owner adopts.

| Reading | Text | Tests | Reasons |
|---|---|---|---|
| **R-QL5** (test law) | "For the `SU(2)` rung of GB1, `L5[SU(2), s]` of section 4.11 is a rung test law for each named `s ≥ 1`; it is not a working-set law." | 1 C, 2 P, 3 P, 4 C | (1) As a framework law it would fix GA1's group by premise; as a rung test law the group is the ladder's premise, as for `GB1.md` Theorem 5M. (2) Each `s` gives one closed law; `s` is a named datum, like LW1's spin `S`. (3) It settles no vacuum, continuum or matter question; Theorem 4.8 is proved, not assumed. (4) A finite register with an exact `SU(2) × SU(2)` action and a covariant link has an independent reason (PS-6r); the particular family `[s, 0]` and the Casimir electric term are chosen because they approach Kogut-Susskind, and the inert spectators exist only because PS-5 fixes five modes. |
| **R-QLC** (meaning of "approach") | "The framework's gauge-invariant correlators approach those of Kogut-Susskind `SU(2)` means: for pairs of states matched as in section 1.4, and for framework observables `ι^*Aι` or the natural loops `W^s_γ`, the differences of `ω(α^n(·))` and of two-time correlators tend to zero as `s → ∞`, at fixed support, tick number and flux or energy bound, with a stated rate." | 1 P, 2 P, 3 P, 4 P | (1) It says how to compare, not what the comparison yields; the brief hands the class of states to the lane ("in a class of states you state"). (2) The classes, observables and order of limits are fixed. (3) It does not place the VC1 vacuum in either class, and it claims no Euclidean or continuum statement. (4) It uses only the inclusion `ι`, which the registers already carry. |
| R-FORM with the cube-face layer | `GB1.md` §8: R-FORM (C P P P) and `L_{cube}^{cf}` (P P C P). | as recorded there | Used unchanged in section 1.3; not a new reading. |

Under R-QL5 and R-QLC, Theorem 4.8 answers GB1-QL for the `SU(2)` rung on states with empty matter. Without them, Theorem 4.8 and Corollaries 4.9-4.10 remain theorems about the `so(5)` quantum-link family and the Kogut-Susskind model, independent of any framework reading.


## 5. Check record and scope

Pass 1 reports floating-point harmonic and commutator checks for `s=1,2,3`, with errors at most `1.2e-15`; the Casimir values were 4, 10, 18 and the squared link norm was 1. Its one-plaquette test used a truncated Kogut–Susskind register, so it is not a proof of the infinite-register bound. The scratch path was `/tmp/toe-GB1QL/check_ql.py`; no check is claimed to have been rerun in this pass. The corrected plaquette order is fixed by the displayed endpoint covariance, not by those numerical checks.

The estimated time window is finite and the constants depend on support, tick bound, flux or energy bound, and magnetic angle. The comparison does not establish a Wilson action, reflection positivity, an RG-class start, or the selected physical vacuum.
