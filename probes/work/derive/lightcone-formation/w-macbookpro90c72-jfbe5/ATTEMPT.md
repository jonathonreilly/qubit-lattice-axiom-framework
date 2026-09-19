# lightcone-formation, attempt 2 (worker w-macbookpro90c72-jfbe5, model grok-4.6)

Route: do not apply block 19 (PR #8153) to the marginal `π` as if it were a nearest-neighbour Heisenberg law. Represent `π` as the `s`-marginal of a Heisenberg ferromagnet on a doubled graph `Γ`, run the infrared / long-range-order / Bogoliubov chain on `Γ`, and keep the linear automaton as an exact identity. Independent of any other derive attempt.

Definitions are those of the task and of the block-19 note
`docs/ADMISSIBILITY_RULE_UNSOLDERED_SPHERE_STATIC_LAW_ORDERED_PHASE_TRANSVERSE_CHANNEL_CARRIES_THE_LATTICE_GREEN_FUNCTION_INFRARED_AND_BOGOLIUBOV_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md`
(PR #8153, branch `physics-loop/admissibility-induced-law-block19-sphere-static-law-goldstone-green-function-channel-20260915`). Finite claims are marked CHECKED with the label in `check.py`.

## (1) The statement attempted

**Objects.** Event lattice `Z^4` with records on the unit sphere `S²`. The record at `(t+1, x)`, `x ∈ T = (Z/L Z)^3` with `L` even, is drawn independently given level `t` from the covariant kernel

    K(s'_x | S_x(s)) ∝ exp(β s'_x · S_x(s)),    S_x(s) = ∑_{y ∈ N(x)} s_y,
    N(x) = {x} ∪ {x ± e_j : j = 1,2,3}

(seven predecessors; the symmetric light-cone neighbourhood of `formation_levelplane.py` with `dim=3s`). The one-site measure `dσ` is the uniform *probability* measure on `S²`. Write

    Z(h) = ∫_{S²} exp(β σ · h) dσ(σ) = sinh(β|h|)/(β|h|)   (h ≠ 0; Z(0)=1).

The synchronous kernel on configurations is `P(s → s') = ∏_x exp(β s'_x · S_x(s)) / Z(S_x(s))`. Put

    π(ds) ∝ ∏_x Z(S_x(s)) ∏_x dσ(s_x).

The static comparator of block 19 is `μ(ds) ∝ ∏_{⟨xy⟩ nn} exp(β s_x · s_y) ∏ dσ(s_x)`. The linear gain-one model is `θ_{t+1} = P θ_t + ξ_t` with `P` the 7-stencil average and `Var(ξ) = σ² = A(7β)/(7β)` per transverse component, `A(κ) = coth κ − 1/κ`.

**Statement.**
(a) On every finite torus, `P` is reversible with respect to `π`. The law `π` is the Gibbs measure of the finite-range Hamiltonian `H(s) = −∑_x log Z(S_x(s))`, equivalently the `s`-marginal of the Heisenberg ferromagnet on the bipartite graph `Γ` whose vertices are two copies of `T` and whose edges are `(x,σ)—(y,s)` for `y ∈ N(x)`.
(b) The joint law on `Γ` is reflection positive through spatial bond planes composed with a layer swap. Gaussian domination on `Γ` yields the infrared bound below. Long-range order of the even sector (hence of `π`) holds whenever `β > 3√3 π/16 + 3/4`.
(c) For the linear automaton, `φ(k) = 1 − E(k)/7` with `E(k) = ∑_{j=1}^3 2(1−cos k_j)`, and the stationary equal-time covariance of every nonzero mode is exactly `S_lin(k) = 7 σ² / (2 E(k) (1 − E(k)/14))`, hence `(7σ²/2)/E(k) ≤ S_lin(k) ≤ (49σ²/2)/E(k)`. For `π`, with unitary DFT `ŝ(k) = N^{−1/2} ∑_x e^{ik·x} s_x`, `N = L³`,

    ⟨|ŝ^e(k)|²⟩ ≤ (1/(2β)) (1/E(k) + 1/(14−E(k))) ≤ 7/(2β E(k))   (k ≠ 0, every component e).

In the ordered phase a zero-field Bogoliubov bound on the even sector of `Γ` gives a matching lower bound of order `M_+^4 / (β E(k))` on the transverse structure factor of `s`.
(d) The level automaton is a Dobrushin contraction in one-site total variation for `β < 1/7`: unique invariant law, exponential forgetting of the initial plane, uniformly in volume.
(e) The interaction `log Z(β|S|)` is not the nearest-neighbour `β s·s'`. Block 19's G1 (positive-definite *nearest-neighbour* crossing kernels) does not apply to `π` as a product over cubic bonds. G1–G5 *do* apply on `Γ`, with Laplacian spectrum `{E(k), 14−E(k)}` in place of `{E(k)}`.

## (2) Steps

**Step 1 — bilinear identity (PROVED; CHECKED E1).** `y ∈ N(x)` if and only if `x ∈ N(y)` (the 7-stencil is an undirected relation, including the diagonal `x ∈ N(x)`). Therefore

    ∑_x s'_x · S_x(s) = ∑_x ∑_{y ∈ N(x)} s'_x · s_y = ∑_y ∑_{x ∈ N(y)} s'_x · s_y = ∑_y s_y · S_y(s').

This is an identity of finite sums, for any assignment of vectors, on any torus (including the degenerate `L=2` case where `+e_j` and `−e_j` coincide). Checked on `Z/4Z`, `(Z/4Z)^3` and `(Z/2Z)^2` with integer 3-vectors.

**Step 2 — reversibility (PROVED; CHECKED E2).** On a finite torus

    π(s) P(s → s') = C ∏_x Z(S_x(s)) · ∏_x exp(β s'_x · S_x(s)) / Z(S_x(s))
                   = C exp(β ∑_x s'_x · S_x(s)),

and the right-hand side is symmetric in `(s,s')` by Step 1. So `π(s) P(s → s') = π(s') P(s' → s)`. In particular `π` is invariant. Checked: Ising menu `{±1}` on the 4-cycle (3-stencil), weights `t^{s S}` with rational `t = e^β ∈ {2,3}`: every row of `P` sums to 1, detailed balance holds on all `16²` pairs, and `π P = π`.

The same computation with the *backward* neighbourhood `{x, x−e_j}` fails: the relation is not symmetric, the bilinear identity fails on an explicit integer pair, and the product-form `∏_x Z(S^−_x)` fails detailed balance on an explicit Ising pair (CHECKED E3). Reversibility uses the symmetric past.

**Step 3 — Gibbs identification and the doubled graph (PROVED).** `π` is Gibbs for `H(s) = −∑_x log Z(S_x(s))`, finite range (each term depends on the 7-stencil of `x`; the interaction range is `√2`). Expanding the single-site partition function,

    ∏_x Z(S_x(s)) = ∫ ∏_x dσ(σ_x) exp(β ∑_x σ_x · S_x(s)) = ∫ ∏ dσ(σ) exp(β ∑_x ∑_{y ∈ N(x)} σ_x · s_y).

Let `Γ` have vertices `T × {0,1}`, spin `S_{(x,0)} = s_x`, `S_{(x,1)} = σ_x`, and an undirected edge between `(x,0)` and `(y,1)` precisely when `y ∈ N(x)`. Each vertex has degree 7, so `|E(Γ)| = 7N`. The exponent is `β ∑_{{u,v} ∈ E(Γ)} S_u · S_v`. Thus the joint law

    ν(ds, dσ) ∝ exp(β ∑_{E(Γ)} S_u · S_v) ∏ dσ(s_x) dσ(σ_x)

is the Heisenberg ferromagnet on `Γ` with coupling `β` on every edge (the same exponential overlap as block 19, on a different graph), and `π` is its `s`-marginal. The two copies are exchangeable because `y ∈ N(x)` iff `x ∈ N(y)`.

**Step 4 — spectrum of `Γ` (PROVED; CHECKED E4, E9).** The adjacency of `Γ` acts by `(A f)(x,0) = ∑_{y ∈ N(x)} f(y,1)` and `(A f)(x,1) = ∑_{y ∈ N(x)} f(y,0)`. The stencil multiplier is `μ(k) = ∑_{a ∈ N(0)} e^{ik·a} = 1 + 2 ∑_j cos k_j = 7 − E(k)` (real). On the even sector `f(x,0)=f(x,1)=ψ_k(x)` the Laplacian `Δ = 7I − A` has eigenvalue `E(k)`; on the odd sector `f(x,0)=−f(x,1)` it has eigenvalue `14 − E(k)`. Checked as identities and as eigenfunction identities for four wavevectors on the `4³` torus, including the gradient-sum `∑_{e ∈ E(Γ)} (ψ_u − ψ_v)² = 2 E(k) ∑_x ψ(x)²` on the even sector.

**Step 5 — why block 19 does not apply to `π` as a cubic nn law (PROVED; CHECKED E5, E6, E13).** Three obstructions, each exact.

(i) `log Z(β|S|) = log(sinh κ / κ)` with `κ = β|S|` has Taylor `κ²/6 − κ⁴/180 + ⋯` (CHECKED E13). The quadratic piece is `(β²/6) ∑_x |S_x|²`, whose pair kernel is `n_{yz} = |N(y) ∩ N(z)|`. Counts: `n_{xx}=7`, nearest neighbour `2`, axis next-nearest `1`, face-diagonal `2` (CHECKED E5). Face-diagonal partners of a site at `x_1=0` include `(1, ±e_2)`, which are *not* the spatial mirror `(1,0,0)` of a bond plane between `x_1=0` and `x_1=1`. So even the small-`β` pairwise approximation of `π` is not a nearest-neighbour cubic Heisenberg law.

(ii) Grouping `(s_x, σ_x) ∈ R^3 ⊕ R^3` and pairing a site to its *spatial* mirror, the two crossing `Γ`-edges contribute `s_x · σ_{θx} + σ_x · s_{θx}`, i.e. the `6×6` form `M = [[0, I], [I, 0]]` with eigenvalues `{+1}^3 ∪ {−1}^3`, not positive semidefinite (CHECKED E6). The FLS sufficient criterion of block 19 G1 (crossing weights `e^{β s_x · s_{θx}}` between spatial mirrors of the *same* cubic lattice) therefore does not apply to this grouping.

(iii) Direct spatial bond-plane RP of the *marginal* `π` is not given by G1. On the Ising 4-cycle the spatial Gram matrix of `π` happens to be positive semidefinite (CHECKED E11.2, min eig `0`); that is not a proof in 3d, and it is not G1.

What *does* apply is G1 on `Γ` after the pairing of Step 6.

**Step 6 — reflection on `Γ` (PROVED; CHECKED E11, E14).** Let `θ` be the spatial reflection through a pair of antipodal bond planes in direction `e_1` (torus of even side: `θ` is a fixed-point-free involution of `T` splitting `T` into `H^±` with no shared site, as in block 19 G1). Define `θ_Γ : V(Γ) → V(Γ)` by

    θ_Γ(x, 0) = (θx, 1),    θ_Γ(x, 1) = (θx, 0)

(spatial reflection and a layer swap). Then `θ_Γ` is an involution with no fixed vertex. It is a graph automorphism of `Γ` because `θ` preserves `N(·)`. Crossing `Γ`-edges of this involution are exactly the pairs `{v, θ_Γ(v)}` for `v` on the spatial boundary: for `x ∈ H^+` with `θx = x+e_1 ∈ N(x)`, the edges `(x,0)—(θx,1)` and `(x,1)—(θx,0)` each join a vertex to its `θ_Γ`-image. There are no other cross-plane `Γ`-edges (the stencil has range 1). Checked on the 1d 4-cycle: involution, automorphism, and the composition of the two distinct 1d `θ_Γ`'s restores layers (so the group generated by the `θ_Γ`'s contains the spatial reflections and the global layer swap composed with spatial isometries).

The crossing weight is therefore `∏_{v : {v,θ_Γ v} ∈ E} exp(β S_v · S_{θ_Γ v})`, a product of the same positive-definite kernels `e^{β t}` as block 19 G1. Legendre coefficients `a_ℓ(β) = (2ℓ+1)/2 ∫_{-1}^1 e^{β t} P_ℓ(t) dt` equal the Rodrigues form `(2ℓ+1)/2 · β^ℓ/(2^ℓ ℓ!) ∫ (1−t²)^ℓ e^{β t} dt` (CHECKED E14 for `ℓ ≤ 4`); the integrand is positive on `(−1,1)` for every `ℓ ≥ 0` and every `β > 0`, so `a_ℓ(β) > 0`. Expanding each crossing factor in spherical harmonics as in block 19 G1 gives, for any function `F` of the spins in one `θ_Γ`-half and any reflection-symmetric single-site factors,

    E_ν[F · (F ∘ θ_Γ)] ≥ 0.

(The joint Ising 4-cycle Gram matrix for this pairing is positive definite, min eig `> 0` at 40 decimals, CHECKED E11.4.)

**Step 7 — Gaussian domination on `Γ` (PROVED).** For `φ : V(Γ) → R` and a unit vector `e`, put

    Z_Γ(φ) = ∫ ∏_{{u,v} ∈ E(Γ)} exp(−(β/2) |S_u − S_v − (φ_u − φ_v) e|²) ∏_v dσ(S_v).

On unit spins this is the Heisenberg weight with a gradient twist, up to a `φ`-independent constant. Shifting `S̃_v = S_v − φ_v e` moves the twist into the site measures `dσ(S̃_v + φ_v e)`. For any `θ_Γ` as in Step 6, Step 6 applied to the *untwisted* crossing kernels in the `S̃` variables (single-site factors allowed) gives `Z_Γ(φ) ≤ Z_Γ(φ^+)^{1/2} Z_Γ(φ^-)^{1/2}`, where `φ^+` equals `φ` on one half and `φ ∘ θ_Γ` on the other. Iterating over the three spatial directions, each step replaces `φ` by a pair of its reflections; the group generated by the `θ_Γ`'s consists of spatial reflections (even words, layers restored) and spatial isometries composed with a global layer swap (odd words). A field invariant under the whole group is spatially constant *and* equal on the two layers, hence constant on `V(Γ)`. A global constant twist does not change differences, so `Z_Γ(constant) = Z_Γ(0)`. The geometric mean therefore yields `Z_Γ(φ) ≤ Z_Γ(0)`.

**Step 8 — infrared bound (PROVED; CHECKED E4, E9).** Expand `Z_Γ(λψ)/Z_Γ(0)` at small `λ` for a Laplacian eigenfunction `ψ` of `Γ` with eigenvalue `λ_Γ > 0`. The first-order term vanishes by `s ↦ −s`. Nonpositivity of the second-order coefficient is `β² ⟨X²⟩ ≤ β ∑_{edges} (ψ_u − ψ_v)²` with `X = ∑_{edges} (ψ_u − ψ_v)(S_u − S_v)·e = ∑_v S_v^e (Δψ)_v = λ_Γ ∑_v ψ_v S_v^e`, and `∑_{edges} (ψ_u−ψ_v)² = ∑_v ψ_v (Δψ)_v = λ_Γ ∑_v ψ_v²`. Thus `⟨(∑_v ψ_v S_v^e)²⟩ ≤ (∑_v ψ_v²)/(β λ_Γ)`.

Even sector, `ψ_{(x,ε)} = cos(k·x)`, `λ_Γ = E(k)`, `k ≠ 0`, `2k ≠ 0`: `∑_v ψ² = N` and `∑_v ψ S^e = ∑_x cos(k·x)(s_x^e + σ_x^e)`. With the copy-wise unitary DFT `ŝ_s(k) = N^{−1/2} ∑_x e^{ik·x} s_x` this is `⟨|ŝ_s^e(k) + ŝ_σ^e(k)|²⟩ ≤ 2/(β E(k))`. The odd sector with `ψ_{(x,0)} = −ψ_{(x,1)} = cos(k·x)` gives `⟨|ŝ_s^e − ŝ_σ^e|²⟩ ≤ 2/(β(14−E(k)))`. Adding,

    ⟨|ŝ_s^e(k)|²⟩ = (1/4) ⟨|ŝ_s^e + ŝ_σ^e|² + |ŝ_s^e − ŝ_σ^e|²⟩
                   ≤ (1/(2β)) (1/E(k) + 1/(14−E(k))).

On `(0,12]` one has `E/(14−E) ≤ 6` (CHECKED E4.13–E4.14), so `1/E + 1/(14−E) ≤ 7/E` and `⟨|ŝ_s^e(k)|²⟩ ≤ 7/(2β E(k))`. The case `2k = 0` only enlarges `∑ ψ²` and strengthens the bound, as in block 19 G2. Equivalently the even-sector unitary DFT on `Γ`,

    ŝ_+^e(k) := (2N)^{−1/2} ∑_x e^{ik·x} (s_x^e + σ_x^e) = (ŝ_s^e + ŝ_σ^e)/√2,

obeys `⟨|ŝ_+^e(k)|²⟩ ≤ 1/(β E(k))`, the exact analogue of block 19 G2 on `Γ`.

The identity `1/E + 1/(14−E) = 1/(E(1−E/14))` (CHECKED E4.12) rewrites the bound as `⟨|ŝ_s^e|²⟩ ≤ 1/(2β E (1−E/14))`. At large `β`, `σ² = A(7β)/(7β) → 1/(7β)`, and the linear kernel of Step 12 equals this upper bound exactly (CHECKED E4.16–E4.17).

**Step 9 — long-range order (PROVED; CHECKED E10).** Let `m_+ = (2N)^{−1} ∑_v S_v` and `M_{+,N}² = ⟨|m_+|²⟩`. Unitarity on `Γ` (`2N` vertices, `|S_v|=1`):

    ∑_k ∑_{e=1}^3 ( ⟨|ŝ_+^e(k)|²⟩ + ⟨|ŝ_-^e(k)|²⟩ ) = 2N.

The even zero mode is `⟨|ŝ_+(0)|²⟩ = 2N M_{+,N}²`. Dropping the odd zero mode (itself bounded by `3/(14β)`) and inserting Step 8,

    M_{+,N}² ≥ 1 − 3/(2N β 14) − (3/(2β)) N^{−1} ∑_{k≠0} (1/E(k) + 1/(14−E(k))).

As `L → ∞`, `N^{−1} ∑_{k≠0} 1/E(k) → G(0) := ∫_{[−π,π]³} d³k / ((2π)³ E(k))`. The bound `1−cos u ≥ 2u²/π²` on `[−π,π]` (the numerator `u sin u − 2(1−cos u)` has vanishing 0th and 1st derivatives at 0 and second derivative `−u sin u ≤ 0` on `[0,π]`; CHECKED E10.1–E10.4) gives `E(k) ≥ (4/π²)|k|²` and `G(0) ≤ √3 π/8`, as in block 19 G3. Also `14−E ≥ 2`, so `G_{14} := ∫ 1/(14−E) ≤ 1/2`. Hence

    M_+² := lim inf_L M_{+,N}² ≥ 1 − (3/(2β))(√3 π/8 + 1/2),

which is positive for `β > 3√3 π/16 + 3/4`. This threshold is strictly below `21/10` (CHECKED E10.5, using `π < 22/7`).

The odd zero mode is massive, and `s` and `σ` are exchangeable, so `⟨|m_s|²⟩ = M_+² + (1/4)⟨|m_s − m_σ|²⟩ ≥ M_+²`. Long-range order of the even sector of `Γ` is long-range order of `π`.

**Step 10 — Bogoliubov lower bound (PROVED; CHECKED E8).** On `Γ` run block 19 G4 with `N` replaced by `N_Γ = 2N` and with the even generator `L = ∑_v e^{−ik·x(v)} L_v`, `L_v F = (e_2 × S_v) · ∇_{S_v} F`. The local identities `L s^1 = s^3`, `L s^3 = −s^1`, `L(s·t) = e_2 · (s × t)`, and the single-bond second derivative

    −(c_u L_u + c_v L_v)(c̄_u L_u + c̄_v L_v)(S_u · S_v) = |c_u − c_v|² (S_u^1 S_v^1 + S_u^3 S_v^3)

are algebraic (CHECKED E8). Integration by parts on the sphere, `∫ L_v G dσ(S_v) = 0` for smooth `G`, is the same standard import as block 19 (iii); it is used here only through `⟨L G⟩ = −⟨G · L log w⟩` with `log w = β ∑_{E(Γ)} S_u · S_v`. Then `⟨|L log w|²⟩ = β ∑_{edges} |c_u − c_v|² ⟨S_u^1 S_v^1 + S_u^3 S_v^3⟩ ≤ β ∑_{edges} |c_u − c_v|²`. For the even plane wave, `∑_{edges} |c_u − c_v|² = E(k) · 2N`. With `F = ŝ_+^1(k) m̂_+` one gets the same quadratic as G4,

    ⟨|ŝ_+^1(k)|²⟩ ≥ (2 M_{+,N}² / 3)² / [ (β E)^{1/2} + (β E + 4 M_{+,N}² / (3 · 2N))^{1/2} ]².

As `N → ∞` at fixed `k ≠ 0` this tends to `(M_+² / 3)² / (β E(k))`. Because `⟨|ŝ_s^1(k)|²⟩ ≥ (1/2) ⟨|ŝ_+^1(k)|²⟩`,

    lim inf ⟨|ŝ_s^1(k)|²⟩ ≥ (M_+² / 3)² / (2 β E(k)).

The same holds for component `2`. Combined with Step 8, for every `β > 3√3 π/16 + 3/4` and every fixed `k ≠ 0`,

    (M_+² / 3)² / (2 β E(k)) ≤ lim inf ⟨|ŝ_s^1(k)|²⟩ ≤ lim sup ⟨|ŝ_s^e(k)|²⟩ ≤ (1/(2β))(1/E(k) + 1/(14−E(k))).

That is a two-sided Green-function sandwich for the transverse channel of `π`.

**Step 11 — uniqueness at small `β` (PROVED; CHECKED E7, E12).** The one-site kernel is von Mises–Fisher with field `β S_x`. Interpolating `h(t) = (1−t) S + t S'` between two predecessor fields,

    TV(r(·|S), r(·|S')) ≤ ∫_0^1 (1/2) ∫ |∂_t p_t| dσ dt = ∫_0^1 (1/2) E_{p_t} |β (s − m_t) · (S'−S)| dt
                        ≤ (β/2) |S'−S| ∫_0^1 E |s − m_t| dt.

`E|s−m|² = 1 − |m|² ≤ 1`, so `E|s−m| ≤ 1` and `TV ≤ (β/2) |ΔS|`. One predecessor changes `S` by at most 2, hence `TV ≤ β`. Seven predecessors: the Dobrushin matrix of the PCA has `sup_x ∑_y C_{xy} ≤ 7β`. For `β < 1/7` this is `< 1`. Coupling two copies sitewise (agree with probability `1−TV`, independent draws with probability `TV`) contracts the sum of one-site total variations by `7β`, uniformly in volume. Unique invariant law, exponential forgetting of any initial plane. (On a finite torus uniqueness of `π` is already true for every finite `β` by strict positivity of `P`; the content is the volume-uniform contraction.)

The Langevin function satisfies `A(κ) ≤ κ/3` because `u(κ) = (κ²+3) sinh κ − 3κ cosh κ` has `u(0)=0` and `u'(κ) = κ(κ cosh κ − sinh κ)` with `(κ cosh − sinh)' = κ sinh ≥ 0` (CHECKED E7.1–E7.3). Also `A'(κ) ≤ 1/3`: the function `p(κ) = κ² sinh²κ − 3 sinh²κ + 3κ²` has vanishing Taylor coefficients through order `κ^5` and nonnegative coefficients of `κ^{2m}` for `m ≥ 3`, given in closed form by `2^{2m−3}/(2m−2)! · (2m(2m−1)−12)/(2m(2m−1))` (CHECKED E7.4–E7.10). Thus `h ↦ A(β|h|) h/|h|` is `(β/3)`-Lipschitz (the `μ=±1` endpoints of the chordal comparison: parallel uses `|A'|≤1/3`, antiparallel uses `A(κ)≤κ/3`). Mean-field `r = A(7β r)` linearises at `β = 3/7`. The TV bound `1/7` is a fraction of mean-field and is not claimed to be sharp. Simulation memory at `β = 1` sits above `1/7` and below the FSS threshold, in the unproved gap.

Ising check of the TV derivative: `|d r(+1)/dS| = (β/2) sech²(β S) ≤ β/2` (CHECKED E12).

**Step 12 — linear automaton (PROVED; CHECKED E4).** `φ(k) = (1 + 2 ∑_j cos k_j)/7 = 1 − E(k)/7` identically. Then `1 − φ² = (2E/7)(1 − E/14)`, so `σ²/(1−φ²) = 7σ²/(2E(1−E/14))`. The prefactor `7/(2(1−E/14))` increases from `7/2` (`E → 0`) to `49/2` (`E = 12`, zone corner `φ = −5/7`, `1−φ² = 24/49`). Hence `(7σ²/2)/E ≤ S_lin ≤ (49σ²/2)/E` on every nonzero mode. This is the exact equal-time kernel of the linearised process, not of `π`; Step 8 shows it saturates the FSS upper bound as `β → ∞`.

**Step 13 — what of block 19 carries (PROVED, collecting (e)).**

| block 19 | static nn Heisenberg `μ` | formation Gibbs `π` / joint `ν` on `Γ` |
|---|---|---|
| interaction | `β ∑_{nn} s_x · s_y` | `∑_x log Z(β S_x)` / `β ∑_{E(Γ)} S_u · S_v` |
| graph | cubic lattice, degree 6 | `Γ`, bipartite, degree 7 |
| Laplacian symbols | `E(k)` | `{E(k), 14−E(k)}` |
| G1 RP through spatial bond planes | yes, nn crossing kernels | not as a cubic nn law (Step 5); yes on `Γ` with layer-swap `θ_Γ` (Step 6) |
| G2 IR bound | `⟨|ŝ^e(k)|²⟩ ≤ 1/(β E)` | `⟨|ŝ_+^e|²⟩ ≤ 1/(β E)` and `⟨|ŝ_s^e|²⟩ ≤ (1/(2β))(1/E + 1/(14−E))` |
| G3 LRO | `β > 3√3 π/8` | `β > 3√3 π/16 + 3/4` for `M_+` |
| G4–G5 Goldstone sandwich | `(M²/3)²/(β E) ≤ · ≤ 1/(β E)` | `(M_+²/3)²/(2β E) ≤ · ≤ (1/(2β))(1/E + 1/(14−E))` |
| linear automaton | not this object | exact `7σ²/(2E(1−E/14))` |

The formation law itself remains causal: records are written once. Reversibility is of the level-to-level kernel; `π` is its invariant equal-time law. That is the sense in which the Green-function kernel is a record statistic *of the stationary light-cone process*, not of a static nearest-neighbour reading.

## (3) Where the route stops

The FSS threshold `3√3 π/16 + 3/4 ≈ 1.770` and the Dobrushin threshold `1/7` leave a gap (the executed memory at `β = 1` lives in it). Constants are not sharp: G3 uses `G_{14} ≤ 1/2` and `G(0) ≤ √3 π/8`; the true integral `G_{14}` is smaller. Discrete menus have no rotation generator, so Steps 10's lower bound is sphere-only; Step 2's reversibility and Step 11's Dobrushin bound hold for any compact menu with the exponential overlap. Infinite-volume Gibbs measures are constructed as torus subsequential limits (compact spins); uniqueness in the gap is not claimed. Gaussian domination is written at the same granularity as block 19 G2 (the iteration over planes); a fully expanded chessboard inventory of every intermediate `φ` is not executed. The linear `σ² = A(7β)/(7β)` is the aligned-state transverse variance, a calibration of the linear model, not an identity for `π` at finite `β`.

## (4) What would finish it

A high-temperature expansion or two-step Dobrushin estimate pushing uniqueness up through `β = 1`; a chessboard / infrared improvement of `G_{14}` and of the `√3 π/8` bound to bring the FSS threshold below the executed memory; Peierls or chessboard LRO for finite menus; an identification of `π`'s structure factor with `S_lin` at finite `β` (fluctuation-dissipation for the reversible PCA, beyond the large-`β` saturation of Step 8).
