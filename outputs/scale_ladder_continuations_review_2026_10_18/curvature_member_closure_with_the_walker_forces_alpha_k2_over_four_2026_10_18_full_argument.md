# Complete corrected argument: Conditional walker normalization and constraint matching

This is inspectable mathematical source. The canonical claim is limited to: Result1–4 and complete canonical-rescaling/closure proof.

**Deferred continuation:** Universal uniqueness beyond the stated frame/jet family and physical identification of the supplied walker with gravitational matter. Complete arguments are retained below, but terminal negative conclusions are not promoted until the required residual-matched packet is supplied and reviewed. This does not make the exact identities uncertain. Historical verification statements below describe the original campaign, not a fresh capture or audit verdict.


# Curvature-member closure with the walker as matter: α = K₂/4 and one curvature coefficient in the walker's frame normalisation

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact within the supplied clauses at the orders computed (continuum, flat background, isotropic ansätze, the `k = 0` species). Fresh-context checks of the same model family confirmed the core claims and corrected several statements; those corrections are built in. Nothing is adopted.

## Question

The repository's curvature member (block 62, block 101's action, the 2026-09-24 constraint note) carries one coefficient `K` on both curvature terms: `K w̄ (u R₁ + R₂)`. The 09-25 one-light-cone notes then show that the walker's two-step content meets the member's lapse identity iff `α = K/4`. Block 62 T4 says that at `α = K/4` the member's disturbances move at the walker's top speed, and that "nothing here forces that value".

Write the two coefficients separately, `K₁` on the `u R₁` term and `K₂` on `R₂`. Three questions follow:

- Which combinations of `K₁`, `K₂`, `α` and the matter's coupling strength are meaningful at all, given that `h` can be rescaled?
- Which of them does the walker's own frame coupling fix?
- Does requiring one lapse/relabelling algebra with the walker as matter fix the rest, and in particular `α`?

## Result

### 1. Invariance: only the TT cone and `γ` are meaningful; `K₁ = K₂` is a normalisation statement

- **The map.** `Φ_ρ: (h, P) → (ρh, P/ρ)` is a linear symplectic map, so it preserves every Poisson bracket. Acting on a closing model it gives another closing model with
  `λ₁ → λ₁/ρ`, `K₁ → ρK₁`, `K₂ → ρ²K₂`, `α → ρ²α`, `a_s → ρa_s`, `β → ρβ`, `kin₁ → kin₁/ρ`.
  Here `a_s` is the matter coupling strength, defined by "the matter propagates on `δ + a_s h`", and `β` is the `h`-term of the structure function. The matter's own coefficients, `ν`, the lapse rule and `c₀` are unchanged.
- **Invariants.** `λ₁K₂/K₁`, the TT cone `K₂/(4α)`, `K₁a_s/α`, `c₀ = K₁/(4αλ₁)` and the static space-to-time curvature ratio `γ = a_s K₁/K₂` are invariant. `K₁/K₂`, `K₁/(4α)` and `a_s` are not.
- **The TT cone.** A transverse-traceless disturbance has `ω² = K₂ p²/(4α)`; `R₁` vanishes on TT, so `K₁` never enters. This is the invariant graviton cone.
- **Consequence (proof by the map).** No bracket, at any degree, can fix `K₁/K₂` in an ansatz that leaves every `Φ_ρ`-non-invariant normalisation free. Fixing any one of them (`a_s = 1`, `β = −1`, `λ₁ = ν`, a fixed nonpolynomial single-`K` form, or a microscopic scale for `h`) breaks the freedom.
- **The family (campaign block B21 and its check).** In B21's ansatz (degree ≤ 2, isotropic and parity-even, ultralocal `kin₁`, one constraint without `∂N` terms, a field-independent lapse rule):
  - `{G, G}` at order `P` and `{C, G}` at order `h` force `G₂ = ν∫P L_ξ h` uniquely, with `ν = λ₁K₂/K₁`, `s₁ = −ν`, `s₂ = 0`.
  - The closing set is one-parameter in `r = λ₁/ν`: `K₂/K₁ = 1/r`, `β = −1/r`, `kin₁` = DeWitt about `rδ`.
  - Witnesses close in all six sectors computed at `r = 2` (`K₁ = 3`, `K₂ = 3/2`), `r = 1` and `r = 1/3`. The negative control `r = 2` with `K₂ := K₁` fails `{C, G}` at order `h` and `{C, C}` at order `Ph`.
- **Equivalent premises.** Given closure, `K₁ = K₂` is equivalent to each of: (a) `λ₁ = ν`; (b) structure function `δ − h` (`β = −1`); (c) DeWitt kinetic term about `δ`; (d) unit matter coupling `a_s = 1`; (e) a single `K` on `R₁` and `R₂`. Computed here: (b) forces `K₂ = K₁`, `λ₁ = ν`; (d) forces `K₂ = K₁` for a scalar and, in Result 3, for the walker. (a) and (c) are read off the family; (e) is the definition.
- For a scalar the `{C, G}` coupling is `(λ_s/λ₁)` times the unit metric stress of `δ + h`, plus only the covariant non-minimal direction `R₁φ²`, so `a_s = λ_s/λ₁`.

### 2. The walker's frame coupling fixes `a_s = 1`, by definition; the lapse identity fixes `K₁a_s = 4α`

- **The cone of a uniform frame.** For the walker of block 62, `H(k) = Σ_j (E^j·σ) s_j`, and `H(k)² = sᵀ(EᵀE)s · 1` exactly. So the walker's uniform cone is `g⁻¹ = EᵀE`.
- **Unit strength.** With block 62's identification `g^{ij} = Σ_a E_a^i E_a^j`, `g = δ + h`, define `h := (EᵀE)⁻¹ − δ`. For `E = 1 + tε`, `h = −(ε + εᵀ)t + O(t²)`: only the symmetric part of the tilt enters. Matching the walker's cone with matter on `δ + a h` for all `ε`, `s` gives `a = 1` uniquely, and the match persists at second order. Block 62's source `−½ΣΘ_(ij)h_ij` is the metric-variational stress at unit strength.
- **Placement and species.** Block 120 places the response with a bond strain `B = −½φ_j h_ij`, normalised by `ΛR(0) = 1`. Write the strength as `a_R`.
  - Two-step coupling (block 73's momentum): `H² = |s|² − a_R PᵀhP + O(h²)` at every wave vector, and at all eight species corners `H² = δkᵀ(1 − a_R h)δk`. So every species sees `δ + a_R h`.
  - Site frame (block 62's own placement): the corners see `ηhη` (mixed off-diagonals flip sign); 2 of 8 species see `δ + a_R h`.
  - One-step bond coupling (block 64): `sym(hη)`; 1 of 8 species.
  - `ΛR(0) = 1` is `a_R = 1`, so `a_s = 1`. It holds at `q = 0` only, as block 120 states.
- **Status of `a_s = 1`.** Block 120's compatibility condition is homogeneous of degree 1 in `R`, so `ΛR(0) = 1` is a normalisation clause, not a consequence. `a_s = 1` therefore defines what `h` means. It selects the `Φ_ρ` representative; it is not derived. The invariant content is that, in this representative, `K₁/K₂` equals the invariant `γ = a_sK₁/K₂` of the walker.
- **The lapse identity.** With separate coefficients and a source `(a_s/2)ΣΘh`, the member at `β = −α` demands
  `ë_u = −(K₁a_s/(4α)) p·Θ·p`,
  with no `K₂`, no `h` and no `u` dependence; for generic `β` trace terms survive. The walker's exact identity (09-25 notes) is `ë = −w̄² p·Θ·p`. With `w̄ = 1` the match is `K₁a_s = 4α`. So "`α = K/4`" in the source-link note (block 134) and the exact-lattice note means `K₁ = 4α` at `a_s = 1`.
- **Top speed.** After lapse matching the TT speed² is `K₂/(4α) = K₂/(K₁a_s)`. So the sentence "at `α = K/4` the disturbances move at the walker's top speed" (block 62 T4, block 134 T4, the 09-25 exact-lattice note T4) is equivalent to `γ = 1`. Those notes declare a single `K`, which supplies it.
- **Static pull.** With `K₁ ≠ K₂`, the static solution has `λ = e/(4K₁p²)` and `u = −(K₂/K₁)λ`, so the matter's ratio of space to time curvature is `γ = a_sK₁/K₂`. It is `Φ_ρ`-invariant, and equals 1 in block 62's member.
- **`R₁`, `R₂`.** They are the first- and second-order parts of `√g R[δ + h]` with unit coefficients: by the linearised Ricci tensor and the identity `R₂ = −½ h:G⁽¹⁾(h)` (default), and by a plane-wave expansion of `√g R` (`--full`). General relativity on `δ + h/r` gives B21's family, with `a_s = 1/r`.

### 3. Closure with the walker as matter forces `γ = 1`; with the walker's speed 1, `α = K₂/4`

Setup (campaign block C4b):
- **Matter.** `C_f[N] = ∫χ̄ ½{N E_a^j σ_a, p_j} χ`, with `χ` a two-component spinor half-density, `{χ, χ̄} = −i`. Frame on the symmetric section `E = (δ + a_s h)^{−1/2}` (metric route), or `E = 1 + ε` (triad route).
- **Gravity.** `C_g = N[kin₀ + kin_X − K₁R₁ − K₂R₂]`; `G = λ₁G₁ + νG₂ + λ_f K[ξ] + G_f⁽¹⁾`, with `G₁ = ∫P·(∂ξ + ∂ξᵀ)`, `G₂ = ∫P L_ξ h`, `K` the half-density Kosmann generator, and `G_f⁽¹⁾` an isotropic `h`-linear fermion relabelling (20 terms).
- **Rules.** One field-independent lapse rule `N' = s₁ξ·∇N + s₂N∇·ξ`; isotropic ansätze.

Results:
1. **`{C, G}` at order `χχ̄`.** Closes iff `a_sλ₁ = λ_f`, with `s₁ = −λ_f`, `s₂ = 0` and the Kosmann spin coefficient fixed. In the isotropic ansatz (5 + 5 terms, `ε` allowed) the solution space is exactly 3-dimensional: `λ_f` × (Kosmann + the walker's coupling), the density convention `s₂`, and the trivial phase `χ → e^{ik tr h}χ`. No other coupling closes. In a fully general ansatz (84 + 168 coefficients) the null space is 29-dimensional: 24 canonical field redefinitions, `λ_f`, `s₂`, and 3 phases by a constant vector, which are not rotation invariant (`--full`).
2. **`{G, G}` at order `χχ̄`.** With `G_f⁽¹⁾` free, `λ_f ∈ {0, ν}`; `λ_f = 0` would need `a_s = 0`, so `λ_f = ν`, the common structure constant. Without `G_f⁽¹⁾` the remainder is `½ν²∫ε_kij(S_ξS_η)_ij s_k`, the on-site rotation of the Weyl companion note's Result 4; `G_f⁽¹⁾` absorbs it. So the metric route closes `{G, G}` without a triad, in agreement with the 09-13 native-Weyl note's P7/P13. The checker's symmetric-gauge (Bourguignon–Gauduchon) lift, constructed rather than fitted, closes exactly (`--full`).
3. **The headline.** Fix the walker's `a_s = 1` (Result 2) and `λ_f = ν`. Gravity's `h`-linear `{C, G}` together with the walker's `{C, G}` has the unique solution
   `λ₁ = ν`, **`K₂ = K₁`**, `s₁ = −ν`, `s₂ = 0`.
   With `a_s` free the same brackets give `λ₁ = ν/a_s` and `K₂ = a_sK₁`. So closure forces `γ = a_sK₁/K₂ = 1` for every `a_s`; that is the invariant statement. In block-62 variables it reads `K₁ = K₂`. It is B21's equivalence (d), realised for the spinor walker. Two code paths compute this (Verification). The position-space path also shows:
   - `{G, G}` at order `P` forces `G₂`'s weight to equal the structure constant;
   - the common lapse rule `s₁ = −μ = −λ_f` forces `G₂`'s weight `μ = λ_f`, so the normalisation of `G₂` is not a hidden choice;
   - the half-density weight `½` is forced (`--full`).
4. **The cone and `α`.** `{C, C}` at orders `P` and `χχ̄` gives the DeWitt trace `b = −½`, `c₀ = K₁/(4αλ₁)` and the walker's speed² `v² = λ_fK₁/(4αλ₁) = a_sK₁/(4α)`. On the closure solution, `v² = K₂/(4α)`: the walker's cone is the TT cone, for every `a_s`. The walker's speed is 1 (block 62, `H² = g^{ij}s_is_j` at the identity frame), so closure forces
   **`α = K₂/4 = a_sK₁/4`**, and at `a_s = 1`, `α = K₁/4 = K₂/4`.
   This is block 62's `α = K/4` with a single `K`. Block 62 T4 said nothing there forces that value. Within these premises (continuum, leading orders, isotropic ansätze, the walker's speed 1), closure with the walker does.
5. **Forced connection terms.**
   - `{C, C}` at order `Pχχ̄` vanishes identically.
   - `{C, G}` at order `Pχχ̄` forces a kinetic cross term `kin_X ≠ 0`, a `P·h·s` term with coefficient `ν²/(32αλ₁²)`: the Darboux form of the symmetric-section connection (09-13 note, P1). A product-bracket kinetic term does not close.
   - `{C, C}` at order `hχχ̄`, with the full constraint, forces `a_s = ν/λ₁` and the structure function `δ + βh` with `β = −a_s`, `β' = 0`. This is a second route to `a_sλ₁ = ν`; at `a_s = 1` the structure function is `δ − h`.
6. **Triad route.** With `E = 1 + ε` relabelled by its own Lie shift and `χ` by the plain half-density Lie derivative plus a free spin term, closure at `χχ̄` holds iff `λ_E = λ_f` and the spin term vanishes; then `λ₁ = λ_E = λ_f`, so `a_s = 1` directly. This holds for the walker and for the covariant operator of Result 4.

### 4. The walker needs the totally antisymmetric spin-connection term at the next order

- **Rotation defect.** On `E = 1 + A`, `A_aj = ε_ajk θ_k`:
  `C_f[E] − C_f[1] = {C_f[1], ½∫θ·s} + ½∫N(∇·θ) n`,
  uniquely, and no spin rotation alone reproduces it. So the walker as written is not locally rotation covariant: an antisymmetric frame part acts as a spin rotation plus a scalar potential `½∇·θ`. A position-space operator identity on a test spinor gives the same result.
- **The completion.** With `T(E) = ε_abc E_a^j E_b^k ∂_j e_ck` (`e` the co-frame), `T⁽¹⁾(1 + A) = −2∇·θ`. Walker `+ c∫N T n` is rotation covariant at first order iff `c = ¼`.
- **Its identity.** Building the covariant half-density Weyl functional from the Levi-Civita spin connection, for a general first-order frame (9 free functions), gives walker `+ ¼∫N T n` uniquely; with the other connection sign no `c` works. At first order `ε_abc ω_abc = T`. So the term is the totally antisymmetric part of the Levi-Civita spin connection, the axial part of the anholonomy. It is not torsion; in Hehl–Datta's language it has the same algebraic form as the axial coupling.
- **Where it matters.** On the symmetric section `T⁽¹⁾ = 0` identically, so the walker equals the covariant operator at `O(h)` and Results 2–3 hold for both. `T⁽²⁾ ≠ 0`, and to second order the covariant functional equals walker `+ ¼∫N T⁽²⁾ n` (`--full`).
- **Next order (`--full`).** `{C, G}` at order `hχχ̄` needs the operator's second-order frame coupling. With the bare walker it has no solution for the remaining `G_f⁽¹⁾` directions, at `r = 1` (`a_s = 1`) or `r = 2` (`a_s = ½`). The completed operator closes at both, and the mismatched control (`λ₁ = ν`, `a_s = ½`) fails. The checker's route: the bare walker is inconsistent even with an arbitrary isotropic `h`-linear correction from a 33-term basis (rank 17 against augmented rank 18), while the completed operator closes with the constructed `G_f⁽¹⁾` and no free parameter.
- **Not new in the repository at first order.** Block 65, the blind-walk note, has the exact lattice version about the identity frame: a twist-weighted scalar hop, `½ div ϑ = −⅛ ε·T`. The 09-13 note uses the full covariant operator. What the walker lacks is the second-order symmetric-section term `¼∫N T⁽²⁾ n`, which has no lattice form in the repository.

## How this bears on the gravity lane (interpretation, not a claim)

- **The chain.** Block 62 identifies the walker's cone with `g⁻¹ = EᵀE`, and block 120 normalises the two-step placement at `q = 0`. Together they fix `a_s = 1`, which picks the meaning of `h`. The member's lapse identity then ties `K₁` to `α`. Closure with the walker ties `K₂` to `K₁`. With the walker's unit speed, everything is fixed: `α = K₁/4 = K₂/4`.
- **What is invariant.** Closure forces the walker's cone to equal the TT cone, `K₂/(4α)`, and `γ = 1`. That is independent of how `h` is normalised. "`K₁ = K₂`" and "`α = K/4`" are those invariant statements written in block 62's variables.
- **The companion notes.** The Weyl/Maxwell companion note cites this chain (campaign C4b) for its spin-½ normalisation. The value `K/(4α)` there reads as the TT coefficient `K₂/(4α)`, which this note shows equals `K₁/(4α)` in the walker's frame normalisation.
- **Not shown.**
  - Any lattice version. Exact continuum-spectrum closure on the lattice fails (campaign block C3; the companion notes' explicit obstructions). The walker is a step, and its frame coupling matches only at `q = 0`.
  - The doublers, which have their own spin sets.
  - Newton's constant.

## Premises

- **Axioms used.** None beyond those of the cited notes. `docs/MINIMAL_AXIOMS_2026-06-29.md` supplies no dynamics, frame or time metric, and block 62 N7 records that the qubit algebra does not supply a dynamical frame. Every clause below is supplied.
- **Supplied (member).** Block 62's member, written with separate coefficients `K₁` (on `u R₁`) and `K₂` (on `R₂`); block 101's kinetic form; `β = −α` where stated; `K₁, K₂, α > 0`. The continuum constraint with `kin₀`, `kin₁` (B21 ansatz) or `kin_X` (C4b), `G₁`, `G₂ = ν∫P L_ξ h`, and the stated isotropic relabelling ansätze.
- **Supplied (walker).** Block 54's walk with block 62's frame coupling, in its long-wavelength form `C_f[N]` on a spinor half-density; its speed 1; the `k = 0` species. The symmetric section `E = (δ + a_s h)^{−1/2}` (metric route) or `E = 1 + ε` (triad route).
- **Supplied (identification and placement).** `g^{ij} = Σ_a E_a^i E_a^j`, `g = δ + h`, i.e. `h = (EᵀE)⁻¹ − δ` (block 62); block 120's two-step realisation with `ΛR(0) = 1`, at `q = 0`.
- **Supplied (rules).** One field-independent lapse rule common to gravity and matter; one constraint, one relabelling; the bracket `{h, P} = +1`, `{χ, χ̄} = −i`.
- **Standard facts used.** Linearised and second-order `√g R`; Legendre transformation; the Kosmann spinor Lie derivative; the Levi-Civita spin connection; linear algebra over Q.
- **Solver conventions.** Parameters are declared positive in the C4b solves. Every `sympy.solve` solution is back-substituted into all of its equations (part Z of the runner), because `sympy.solve` can drop equations that involve only parameters.

## Proof sketches

- **Result 1.** `Φ_ρ` preserves `∫P ḣ`. The scaling of each functional block is checked by substitution, and the invariants follow. The family, witnesses and equivalences are exact Fourier-kernel brackets, solved as linear systems over the field of rational functions in the parameters.
- **Result 2.** The cone is a Clifford identity. The match `a = 1` is a coefficient identity in `ε` and `s`. The species statement comes from expanding the dispersion at each corner, or from the Jacobian of the coin vector at each corner (second route). The lapse identity solves the kinetic Euler–Lagrange equation for `ḧ`, by the component Hessian or by the closed-form DeWitt inverse, and applies `K₁R₁`; `K₂` drops by the transversality `p_i ∂R₂/∂h_ij = 0`.
- **Result 3.** Each bracket is computed exactly and projected onto a fixed field pattern, for example `N·ξ·χχ̄`. Closure means that the residual against the right-hand side vanishes as a local functional. In the kernel route that is the vanishing of its Fourier kernel; in the position-space route it is the vanishing of the Euler derivative in the lapse. The unknowns enter linearly or through the stated products, and the solution sets are found exactly and back-substituted.
- **Result 4.** The defect is a bracket identity at first order in `θ`. The covariant operator is built step by step: frame, co-frame, metric, Christoffel symbols, spin connection, then `−iσ^aE_a^j∇_j` on `√g`-scalar spinors conjugated to half-densities and symmetrised in the lapse. It is compared with walker `+ c∫N T n` term by term.

## Relation to prior work

- **Closure and universal coupling.**
  - Teitelboim, Ann. Phys. 79, 542 (1973); Kuchař, J. Math. Phys. 15, 708 (1974) and 17 (1976).
  - Hojman, Kuchař and Teitelboim, Ann. Phys. 96, 88 (1976), "geometrodynamics regained". HKT presuppose the structure function `g^{ij}` and the normalisation of the generators, i.e. premises (a)–(b) of Result 1.
  - Deser, Gen. Rel. Grav. 1, 9 (1970): universal coupling to the stress. Isham and Kuchař, Ann. Phys. 164, 288 and 316 (1985).
  - The common cone and the `γ = 1` statement are this known content specialised to the repository's member and walker.
- **Spinors in the deformation algebra.**
  - Nelson and Teitelboim, Ann. Phys. 116, 86 (1978): the Dirac field in the hypersurface-deformation algebra.
  - Kosmann (1972): the spinor Lie derivative.
  - Bourguignon and Gauduchon, Commun. Math. Phys. 144, 581 (1992): identifying spinors across metrics; the symmetric-gauge lift used by the checker.
  - The 2026-09-13 native-Weyl note (P7/P13) has the joint metric–spinor closure in this repository.
- **Axial coupling.**
  - Kibble, J. Math. Phys. 2, 212 (1961); Hehl and Datta, J. Math. Phys. 12, 1334 (1971): Dirac fields couple only to the totally antisymmetric (axial) part of torsion. Result 4's term has that algebraic form. Here there is no torsion: the term is the totally antisymmetric part of the Levi-Civita spin connection.
- **Bibliographic details** above are given from memory and from the campaign checks' attribution; volume and page numbers were not re-verified against the sources.
- **Campaign attributions not re-verified here.** Ashtekar, Romano and Tate (1989) and Barbero (1995) on triad constraint algebras; Henneaux (1983). They are not used.
- **Repository.** Block 62 (frame, member, T4); block 65 (the first-order lattice axial term); block 101 (the action); block 120 (the placement and its normalisation); the 09-24 constraint note; the 09-25 one-light-cone notes (block 134 and the exact-lattice note); the 09-13 native-Weyl note; the two companion closure notes of this date.
- **New here, and narrow.**
  - The normalisation chain for the repository's member and walker: `a_s = 1` from the frame identification and placement, `K₁a_s = 4α` from the lapse identity, and `K₂ = a_sK₁` from closure with the walker. Together they give `α = K₂/4 = K₁/4`.
  - The reading of block 62 T4's "nothing here forces that value": within these premises, closure does.
  - The species count of the three placements (2, 1 and 8 of 8).
  - The continuum form of the frame-coupled walker's rotation defect (block 65 T1(c) has the lattice form about the identity frame), and its next-order failure without the axial term.

## Historical packet proposal (promotion deferred)

The negative sentences:
- no bracket fixes `K₁/K₂` in an ansatz that leaves every `Φ_ρ`-non-invariant normalisation free;
- the site-frame and one-step placements do not give every species unit coupling;
- no other isotropic coupling closes `{C, G}` at order `χχ̄`;
- `λ_f ∉ {0, ν}` does not close `{G, G}` at order `χχ̄`;
- the walker as written is not locally rotation covariant;
- the bare walker does not close `{C, G}` at order `hχχ̄`.

- **N1 — routes by which they could fail or mislead.**
  - Ansätze that fix a non-invariant normalisation. This is the stated loophole, and Results 2–3 use it on purpose.
  - Non-isotropic, field-dependent or multi-derivative relabellings; more than one lapse rule; `∂N` terms in the constraint.
  - Placements other than the three compared; `q ≠ 0`.
  - Non-symmetric frames at the next order; the doublers.
  - Matter operators other than the walker and its completion.
- **N2/N3 — scope.**
  - Result 1's no-go is a proof for every ansatz closed under `Φ_ρ`. The family and the equivalences are computed in B21's degree-2 isotropic ansatz.
  - Results 2–3 hold at the orders stated, in the isotropic ansätze. Result 3.1 is also computed in a fully general ansatz.
  - The next-order statements of Result 4 are witnesses at `r = 1` and `r = 2`. The 33-term inconsistency is a rank certificate at `r = 1`.
- **N4 — inputs.**
  - Exact sympy throughout, over Q and rational functions of the parameters.
  - One floating-point cross-check (a `6³` torus build of the placements, `atol 1e-9`) corroborates the exact corner symbols; it is not the proof.
- **N5 — wording.**
  - "Cone" means the coefficient of the transport term, or `ω²/p²`.
  - "Top speed" means the walker's long-wavelength speed 1.
  - "Axial" names the algebraic form of the term, not torsion.
  - No physical identification is made.
- **N6/N7 — strongest objections.**
  - *"`K₁ = K₂` is put in by `a_s = 1`."*
    - Reply: yes, and the note says so. The derived, invariant content is `γ = 1`, together with equal walker and TT cones.
    - `a_s = 1` is the frame identification and block 120's normalisation, both supplied.
  - *"`α = K₂/4` only restates the walker's unit speed."*
    - Reply: it is the walker's speed together with the derived equality of the two cones.
    - Without closure the TT cone is unconstrained; that is block 62 T4's "nothing forces it".
  - *"Continuum results say nothing about the lattice walker."*
    - Reply: agreed. The lattice is listed as not shown.
- **N8 — earlier claims.**
  - Block 62 T4, block 134 T4 and the 09-25 exact-lattice T4 are unchanged; their single `K` is now read as `K₁ = K₂` in the walker's normalisation.
  - The Weyl companion note's Result 4 already carries the correction that the metric route needs no triad.
  - The C4 finding's open item ("the walker's own `{G, C}` with frame coupling has not been computed") is closed by Result 3.

## Historical checking narrative (not fresh evidence)

Workers and checkers were all of the same model family as the author. None is independent in model lineage. Each checker ran in fresh context and wrote its own code by a different route for the load-bearing step.

- **B21 (Result 1).**
  - The worker used position-space jets with an Euler operator. The checker wrote the Fourier-kernel engine used in this runner and its own `√g R`, DeWitt expansion and `G₂` bases.
  - Confirmed: all claims (17 PASS), with a scope qualifier adopted here (the no-go needs every `Φ_ρ`-non-invariant normalisation left free). It upgraded the uniqueness of `G₂` to the fully general 648-coefficient ansatz.
  - It also found the extra matter freedom `R₁φ²`, which does not change `a_s`, `s₁` or the cone.
- **C4 (Result 2).**
  - The checker took different routes: Jacobian corner couplings, a torus build, the closed-form DeWitt inverse, and `R₂ = −½h:G⁽¹⁾(h)` (12 PASS).
  - Corrected, and adopted: `ΛR(0) = 1` is stipulated, so `a_s = 1` is fixed by definition, not derived; the top-speed sentence relies on the declared single `K`, rather than assuming it silently; and the citations.
- **C4b (Results 3–4).**
  - The checker was proof-critical. It wrote a new position-space engine (Euler-operator brackets, `√g R` from Christoffel symbols), built the covariant Weyl operator from the Levi-Civita spin connection, and built `G_f⁽¹⁾` from the symmetric-gauge lift; neither was fitted. 23 PASS, 0 FAIL.
  - It audited C4b's runner by back-substitution: 21/21, no solution fails. It found that `sympy.solve` drops parameter-only equations; C4b is not affected.
  - Corrected, and adopted:
    - the only input that selects `K₁ = K₂` is `a_s = 1`, i.e. `h = (EᵀE)⁻¹ − δ`, so the invariant result is `γ = 1`;
    - "torsion" was wrong; use "totally antisymmetric Levi-Civita spin connection";
    - block 65 already has the first-order lattice term, so only `T⁽²⁾` is missing;
    - the scope wording for `α = K₂/4`.
  - It recorded the conflict with the spin-½ note's earlier "needs a triad", since corrected in that note.
  - Not independently checked: the null-space decompositions (Result 3.1), the `{C, C}` `Pχχ̄` sector, the forced `kin_X` and the order-`hχχ̄` structure function (3.5), and the triad route (3.6). They pass the solve audit.
  - The walker's cone `v² = a_sK₁/(4α)` (Result 3.4), on which `α = K₂/4` rests, was computed as one step by one engine (D1). Its ingredients are computed elsewhere: the flat walker bracket `{C_f[N], C_f[M]} = K[N∇M − M∇N]` (E.c4bchk.T4, E.c4bop.O1) and gravity's `c₀ = K₁/(4αλ₁)` (A.b21chk.T6b).
  - A fresh-context reviewer of the same model family recomputed the whole step, including D4, with its own code: operator commutators on a test spinor and explicit functional derivatives, with no shared engine. It found:
    - the flat walker bracket `+K[z]` with spin coefficient `i/4`, and `−K` against `−z`;
    - `b = −½` and `c₀λ₁ = K₁/(4α)`;
    - `a_sλ₁ = λ_f` and `s₁ = −λ_f`.
  - Hence `v² = a_sK₁/(4α)`. With B2's `K₂ = a_sK₁`, `v² = K₂/(4α)`, and `v = 1` gives `α = K₂/4` (9 PASS).
  - The lapse-identity route `K₁a_s = 4α` (Result 2; C4 and its check) and the scalar analogue (A.b21chk.T6b) agree.
- **Shared code.** C4b's kernel route uses the B21 checker's engine. So for Result 3 the independent second implementation is the C4b checker's position-space engine. The headline `K₂ = a_sK₁` is computed by both, and `a_sλ₁ = λ_f` also by a one-particle operator route.

This runner consolidates the campaign scripts and the check scripts, reused as written. Re-running it is not a further independent check. One consolidation step is new: D4, which inserts the closure solution into the cone and solves the unit-speed condition for `α`. It is a substitution of B2 into D1; the reviewer's independent check reproduces it. Its first version compared against the unsubstituted symbol `K₂`, an expectation bug of the consolidation that was fixed before the recorded run.

## Historical execution record (not a fresh capture)

```bash
python3 scripts/curvature_member_closure_with_the_walker_forces_alpha_k2_over_four_2026_10_18.py
```

Expected: `TOTAL: PASS=79 FAIL=0`, in about 3–4 minutes (185 s, 194 s and 232 s measured; Python 3.13, sympy 1.14, numpy). Parts:
- A: B21 check — `Φ_ρ`, invariants, TT cone, family, witnesses, equivalences;
- B: the C4 runner — frame coupling, species, lapse identity, `γ`;
- C: the C4 check — second routes for B;
- D: the C4b runner — Fourier-kernel closure with the walker, the cone and `α` (D4), connection terms, triad route, rotation defect;
- E: the C4b check and operator route — the headline `K₂ = a_sK₁` by the position-space engine;
- F: the C4b check — the Levi-Civita covariant operator and `c = ¼`;
- Z: the solve audit.

Each tag names its source script, for example `D.c4b.B1` or `E.c4bchk.B1`.

Optional:
- `--full` adds the slow checks: the 648-coefficient `G₂`, the plane-wave `√g R`, the generic-`β` control, the fully general null space, the half-density weight, the second-order covariant operator, the constructed `G_f⁽¹⁾`, and the next-order closure (F1/F2, F1′/F2′, F1″). Expected `TOTAL: PASS=96 FAIL=0`, in about 19–21 minutes (1125 s and 1225 s measured, alongside other jobs).
- `--parts A,D` runs selected parts.

## Load-bearing sources

- Block 62: the coin's frame (`docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md`)
- Block 65: the blind walk (`docs/ADMISSIBILITY_RULE_THE_BLIND_WALK_A_SCALAR_HOP_WEIGHTED_BY_THE_TWIST_OF_THE_COIN_ALONG_THE_BOND_MAKES_A_VARYING_ROTATION_OF_THE_COIN_AXES_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-21.md`)
- Block 101: the clock constraint (`docs/ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23.md`)
- Block 120: the two-step placement (`docs/ADMISSIBILITY_RULE_ONLY_THE_TWO_STEP_CURRENT_CAN_SOURCE_BLOCK_62S_SYMMETRIC_MEMBER_NO_LOCAL_PLACEMENT_OF_THE_FRAME_RESPONSE_OR_OF_THE_ONE_STEP_CURRENT_KEEPS_ITS_DIVERGENCE_CONDITION_BOUNDED_THEOREM_NOTE_2026-09-24.md`)
- 09-24 constraint-closure note (`docs/ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md`)
- 09-25 source-link note (block 134) (`docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_FROM_THE_SOURCE_LINK_THE_WALKERS_SMOOTH_STATES_MEET_THE_MEMBERS_IDENTITY_AT_LEADING_ORDER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md`)
- 09-25 exact-lattice note (`docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_EXACTLY_ON_THE_LATTICE_THE_TWO_STEP_CONTENT_MEETS_THE_MEMBERS_IDENTITY_FOR_EVERY_STATE_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md`)
- 09-13 native-Weyl canonical-metric note (`docs/NATIVE_WEYL_CANONICAL_METRIC_CONSTRAINTS_BOUNDED_THEOREM_NOTE_2026-09-13.md`)
- Companion scalar note (`outputs/scale_ladder_continuations_review_2026_10_18/curvature_member_closure_with_matter_common_cone_2026_10_18_full_argument.md`)
- Companion Weyl/Maxwell note (`outputs/scale_ladder_continuations_review_2026_10_18/curvature_member_closure_spin_half_and_spin_one_common_cone_2026_10_18_full_argument.md`)
- Axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md`)
