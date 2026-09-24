# Parity-odd couplings under the proper rotations only: when the field energy sees the twist the odd term is blind, and its twist equation excludes bodies; when it does not, the first odd term has five derivatives

Attempt 2 of 2. Worker `w-macbookpro9927a-j7619` (Claude Opus 5.5, `claude-opus-5-5`). Checks are in `check.py` in this directory. They are exact throughout (sympy polynomial identities, exact nullspaces, characters, truncated jets with rational coefficients) and take about 15 s.

## Sources

Definitions are read from the PR heads:
- block 54 (#8570, `664e733aa2`): T1, the generator family and the inversion with the content reversed;
- block 60 (#8590, `ec3a6abdf0`): the ledger per tick `F = Σ_x w_x D_x`; lengths `ℓ = (w̄/w)^β`, with `β = 1` for the curvature member;
- block 64 (#8595, `e568866573`): the co-frame `e^j_a`, its curl, the family with `c₅ det e (ε·T)`, the rotation of the coin axes `e → R(x)e`, blindness, and T4's `β = 1` for the blind member;
- block 65 (#8596, `fb37a985ba`): the twist `ϑ`, with `ϑ → ϑ + θ` under a coin rotation (T2(a)); the torque-free walker (T3); the `−4 div ϑ` of T4;
- block 70 (#8602, `8b4eccab5c`): the two classes, and `ΠH[F]Π = −H[F∘Π]`.

Check family Q confirms 12 quoted lines verbatim, including attempt 1's step 8 and the task text.

## Provenance and route

Attempt 1 (`w-jonathonsmac4f50-jb5a4`, the same model family, not yet refereed) covered the following:
- the generator: the three-parameter family, the parity table, the scalar hop `a` as the term that tells the classes apart, and its blind completion;
- the frame-only field energy at second order, where blindness forces `c₅ = 0`.

I read it only after forming my plan. Because it is unrefereed, I take a different route and do not rely on its claims. This attempt asks what happens to the field energy's odd sector in two situations: when the field energy sees block 65's twist as well as the frame, and at every order in derivatives when it does not. I do not redo the generator.

The result differs from attempt 1's step 8 on one point. That step says blindness "forces `F` to be independent of `ϑ`". This holds for a field energy of `ϑ` (and rates) alone. It fails once `F` also sees the frame (T1 below).

I have no earlier unit on parity. My unit #8734 treated block 62's kinetic numbers under the two blindness demands; nothing here uses it.

## (1) Statement

**Objects.**
- `e^j_a`: coin index `j`, bond index `a`.
- `T^j_ab = ∂_a e^j_b − ∂_b e^j_a`.
- `ε·T = ε_jmn T^j_ab (e⁻¹)_am (e⁻¹)_bn` (block 64).
- `Ω(v)w = v × w`, `R(θ) = 1 + Ω(θ) + …`
- A coin rotation `θ(x)` acts as `e → R(θ)e` (block 64) and `ϑ → ϑ + θ` (block 65 T2(a)).
- The dressed co-frame is `e' = R(−ϑ)e`.
- Per tick: `F = Σ_x w_x D_x` (block 60).
- Blind: `D` unchanged at every point under every coin rotation (block 64 T2).
- `u = log w`.
- Parity: `x → −x` acting on real fields as a mirror image, which is how `ΘΠ` acts on them (block 70).

**T1 (the field energy sees the frame and the twist).**
- A density `D(e, ϑ)` is blind (to first order in `θ` and `ϑ`, block 65's order) iff it is a density of `e'` alone.
- Hence the blind, relabelling-covariant densities with at most two derivatives are block 64's frame class evaluated on `e'`, all of them. Blindness selects nothing.
- The parity-odd member is unique under the 24 rotations:

  `D_odd = c₅ det e' (ε·T[e']) = 2c₅ ε^{abc} e'^j_c ∂_a e'^j_b`,

  which equals `c₅(ε·T[e] − 4 div ϑ)` at zero strain.
- It is odd, counted per tick, and blind: **a parity-odd term survives per-tick counting and blindness.**

**T2 (its twist equation).**
- Exactly in the co-frame: `δ_ϑ Σ_x w_x D_odd = 4c₅ Σ δϑ_m ∂_a(w adj(e')_am)` (continuum form).
- With block 65's walker, whose twist response vanishes on stationary states, the twist's static equation is `c₅ ∂_a(w adj(e')_am) = 0` for `m = 1, 2, 3`.
- To first order around the uniform state, write `e' = (1 + λ)(1 + Ω(ρ))`, with `ρ` the frame's rotation relative to the twist. The equation becomes

  `curl ρ = ∇(u + 2λ)`.

- A smooth `ρ` exists only if the flux of `∇(u + 2λ)` through every closed surface vanishes.
- With block 59/60's lengths for bodies at rest, `λ = −β(u − ū)`, that flux is `(1 − 2β)` times the flux of `∇u`, which is the source enclosed.
- With block 64's member (`β = 1`) the equation has no solution around any body at rest. `c₅` and matter exclude each other unless `β = 1/2`.

**T3 (the field energy does not see the twist, block 65's premise).**
- Blind (exactly, at every point) iff `D` depends on `e` only through `g = eᵀe` and the orientation.
- For relabelling-covariant densities polynomial in the derivatives of `g` and `u`, a parity-odd density has an odd number of derivatives.
- There is none with one or three.
- At five there are `√g C^{ij}R_ij` (the Cotton tensor with the Ricci tensor) and `√g ε^{abc} ∂_a u R_b^d (Hess u)_dc`. Both are non-zero, odd, blind and counted per tick.

**T4 ((b), (d)).**
- Every odd field-energy term above changes sign on the mirror image. So a configuration and its mirror image, which carry block 70's two classes, have different field energies: the terms tell the classes apart through the fields.
- The supplied clauses contain none of them, since blocks 56, 60 and 64 end with even members.
- An observable handedness would be the difference `F[config] − F[mirror] = 2F_odd`.

## (2) Steps

**S0 — ASSUMED.**
- The clauses of blocks 54 to 70 as supplied; nothing is adopted.
- The identification of the rotation acting on the field energy's frame (block 64) with the rotation that shifts block 65's twist. It is the same `θ`, with `e → R(θ)e` and `ϑ → ϑ + θ`.
- Blindness at first order, in block 65's own sense. Exactly, the twist would be a rotation-valued field `Q(x)` with `Q → R(θ)Q`, and `e' = Q⁻¹e` would be exactly invariant; that object is not supplied.
- For T3: the existence of normal coordinates, in which a relabelling-covariant density at a point is an `SO(3)`-invariant polynomial in `∂u, ∂²u, …` and in the curvature and its covariant derivatives. This is the classical reduction (Thomas), used as a comparator.
- For T3: that in three dimensions the Riemann tensor is fixed by the Ricci tensor (the Weyl tensor vanishes). Classical.

**S1 — `det e (ε·T) = 2ε^{abc} e^j_c ∂_a e^j_b` exactly — PROVED, CHECKED (A).**
- The cofactor identity `det e · ε_jmn (e⁻¹)_am (e⁻¹)_bn = ε_abc e^j_c` holds for every invertible `e` (27 polynomial identities after multiplying by `det e`).
- Contracting it with `T^j_ab` gives `ε^{abc} e^j_c T^j_ab = 2ε^{abc} e^j_c ∂_a e^j_b`.

**S2 — T1, blindness — PROVED, CHECKED (D).**
- If `D` is blind, take `θ = −ϑ` at every point. Then `D(e, ϑ) = D(R(−ϑ)e, 0)`, a function of `e'`.
- Conversely, `e' → R(−ϑ − θ)R(θ)e = e'` to first order.
- CHECKED (D):
  - Undressed, `D_odd` changes by `4 div r` under a coin rotation `r` at zero strain, and also at first order in the strain (block 64 T2's `c₅` obstruction).
  - Dressed, the change vanishes at orders `t` and `s·t`, with `t` the rotation and twist and `s` the strain, for nine general strain functions.
  - At zero strain the dressed density is `ε·T[e] − 4 div ϑ`.

**S3 — T1, uniqueness of the odd member — PROVED, CHECKED (O).**
- A density of `e'` with at most two derivatives is `det e'` times `{1, T, T², ∇T}`, with the bond indices turned into coin indices by `e'⁻¹` (block 64's class).
- Parity is `(−1)^{number of derivatives}`, since the mirror image changes no field value and reverses every derivative. So only the part linear in `T` is odd.
- Its invariants under the 24 rotations are those of `V ⊗ Λ²V`. Characters: 1 under the 24 rotations and 0 under the 48 of the full cubic group, so there is one invariant, `ε·T`, and inversion reverses it.
- Relabelling covariance fixes the weight `det e'`.

**S4 — T2, the twist equation — PROVED, CHECKED (E).**
- `δe' = −Ω(δϑ)e'`. The two terms of `δ(2ε^{abc}e'^j_c ∂_a e'^j_b)` without derivatives of `δϑ` cancel, because `Ω` is antisymmetric.
- What remains is `−2ε^{abc} e'^j_c e'^k_b ε_jmk ∂_a δϑ_m = −4 adj(e')_am ∂_a δϑ_m`, by the cofactor identity. It is exact in `e'` and checked for a general co-frame of nine functions.
- Summing against `w` and integrating by parts gives the stated variation.
- Block 65 T3 gives the walker's twist response `½ d⟨σ_c(x)⟩/dt`, which vanishes when the state is stationary. The clocked walker gives the same, since `φ` commutes with `σ_c P_x`, so `[σ_cP_x, φHφ] = φ[σ_cP_x, H]φ`.
- On an isotropic co-frame `e' = ℓ·1` the odd density vanishes identically (`ε^{abc}δ_cb = 0`). It therefore adds nothing to the lengths' own equation, and the lengths remain block 60's.
- CHECKED (E), all symbolic:
  - there `w adj(e') = wℓ²·1`, and `∇(wℓ²) = wℓ²(1 − 2β)∇u` for `ℓ = (w̄/w)^β`;
  - to first order, `∂_a(w adj(e')_am) = w̄[∂_m(u + 2λ) − (curl ρ)_m]`;
  - `div curl ρ = 0`.

**S5 — T2, no solution around a body — PROVED.**
- `curl ρ = ∇(u + 2λ)` requires the flux of `∇(u + 2λ)` through every closed surface to vanish, since the flux of a curl through a closed surface is zero.
- With `λ = −β(u − ū)` (block 59/60) the flux is `(1 − 2β)∮∇u·dA`.
- `∮∇u·dA` over a surface around a body at rest is its enclosed source, not zero. This is block 56 T2 (the walls see the ledger), or Gauss's theorem for the weak-field law of block 55.
- So for `β ≠ 1/2` there is no smooth `ρ` around any body, and with block 64's `β = 1` a static configuration with `c₅ ≠ 0` contains no body.
- For `β = 1/2`, `curl ρ = 0`.

**S6 — T3, blind means metric-only — PROVED.**
- Two proper co-frames with the same `g = eᵀe` differ at each point by `R = e'e⁻¹ ∈ SO(3)`, since `RᵀR = 1` and `det R > 0`.
- A density unchanged by every `R(x)` therefore depends on `e` only through `g` and the orientation, and conversely.

**S7 — T3, parity and derivative count — PROVED.**
- The mirror image reverses each derivative and nothing else, so parity is `(−1)^n` with `n` derivatives.
- A full contraction of `n` derivative indices, pairs from `g`, and one `ε` needs `n + 3` to be even. So odd densities have `n` odd, and even `n` gives no odd density.

**S8 — T3, none at one or three — CHECKED (N), with S0's normal coordinates.**
- In normal coordinates a density at a point is an `SO(3)`-invariant polynomial in the jets.
- With `n = 1` the only jet is `∂u ∈ V`; `∂g` vanishes.
- With `n = 3` the monomials are `(∂u)³` and `∂³u` (in `Sym³V`), and `∂u·Hess u`, `∂u·Ric` and `∇Ric` (in `V ⊗ Sym²V`).
- Exact nullspaces of the three `so(3)` generators give 0 invariants on `V`, `Sym³V` and `V ⊗ Sym²V`. The controls give 1 on `V⊗V⊗V` (`ε`) and 1 on `Sym²V ⊗ Sym²V ⊗ V`, the five-derivative invariant.

**S9 — T3, five derivatives — CHECKED (F).**
- Take an explicit polynomial metric `g = 1 + h` (`h(0) = 0`, with first-, second- and third-order terms) and a rate field `u`.
- Exact third-order jets at the origin give:
  - `C^{ij}R_ij = 6412057/15876000`;
  - `ε^{abc} ∂_a u R_b^d (Hess u)_dc = −16/35`.
- For the mirrored fields `g(−x)`, `u(−x)`, both change sign exactly.
- Both are built from `g` and `u` alone, so they are blind (S6), and they are counted per tick as densities at a site.

**S10 — T4 — PROVED.**
- Block 70 T3(c): `ΘΠ` carries a solution of one class in the fields `F` to one of the other class in `F∘Π`. `Θ` leaves real fields unchanged.
- A field energy with an odd part gives `F∘Π` a different energy, so the twins no longer carry equal ledgers.
- Blocks 56, 60 and 64 supply even members only.

## (3) Where the route stops

- **T1** is blindness at first order, block 65's own order. The exact version needs the twist as a rotation-valued field, which is not supplied.
- **T2** is first order around the uniform state, with block 59/60's isotropic lengths for bodies at rest. Suppose the field energy also carries even dressed-torsion terms of `e'` (quadratic in `T[e']`, blind by T1). Then `ρ` enters the metric equations at second order, and the statement is not re-derived for that case.
- **T3** rests on the classical normal-coordinate reduction and on `Weyl = 0` in three dimensions (both ASSUMED). The full dimension of the odd space at five derivatives is not computed, only two members. The lattice form of `√g C^{ij}R_ij` is not built.
- **The generator** is attempt 1's route (block 54 T1, the scalar hop `a`). It is not repeated here.

## (4) What would finish it

1. **A clause for whether the field energy sees the twist.** Block 65 only says a field energy that does not see it is consistent. If it does see it, T1 shows blindness selects nothing, and block 64's derivation of the curvature member would need a different demand.
2. **Under that reading, the full static equations with the dressed even terms.** The question is whether a slaved rotation `ρ` can carry `c₅ ≠ 0` with bodies present, or whether the lengths' exponent moves to `β = 1/2`.
3. **Under the other reading, the size of the first handed term.** This means the five-derivative odd space, a lattice density per site for `√g C^{ij}R_ij`, and the order at which a mirror pair of bodies' ledgers first differ.
