---
claim_id: curvature_member_closure_puts_a_lattice_weyl_field_and_a_lattice_maxwell_field_on_the_scalars_cone_and_rejects_anisotropic_cones_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Supplied models only, on the 2026-09-24 curvature-member clauses at flat strain and order eps (C = kin + s K R1, s = +-1, K > 0, alpha > 0, beta = -alpha, G_g[xi] = sum P.delta_xi h) as used in the companion scalar note (same PR). (1) Spin 1/2: the naive nearest-neighbour two-component Weyl field h_N = sum_b wbar_b (-iv/2)(sigma^j |x><x+e| - h.c.), wbar_b = wa N_x + wb N_(x+e), Grassmann bracket {psi, psibar} = -i, relabelling G_f[u] = psibar (i L_u) psi with L_u the Kosmann derivative (spin coefficient i/4 fixed by rotation invariance). Exact: at O(a^0), for every two-endpoint timing, [h_N, h_M] = -v^2 L_w, w = N grad M - M grad N, so the leading-order total algebra closes into one relabelling with common orientation iff v^2 = -sK/(4 alpha), the scalar's value; Hermitian h_N with real v gives v^2 > 0 (anti-Hermitian Clifford generators flip the sign), hence s = -1 given K, alpha > 0. All 8 species (k = 0 and the 7 doublers) have the same v^2, each with its own spin set tau; tau = sigma only at k = 0 and (pi,pi,pi), so an on-site-spin G_f fails at O(1) on the other 6. On the lattice the bracket carries range-2 collinear lapse pairs (coefficient -+wa wb v^2/4) and mixed diagonal pairs (~ wa^2 - wb^2), whose sum vanishes only at wa = wb = 0; with the exact gravity kernel (constant shifts) no linear G_f of any range, translation-covariant or not, closes the order-eps algebra exactly (exact rank 186 at L = 5). The deviation is O(a^2) at the endpoint mean and O(a) at the other timings tested (t = 1, 1/4), in each case not absorbable by any order-corrected translation-covariant G_f. Naive Dirac: the on-site mass drops out exactly iff t = 1/2 (cross terms ~ (2t - 1), Clifford-odd, blocking only Kosmann-class G_f); a Wilson term gives a Clifford-odd O(a) term that is kappa-linear (absorbable by a Clifford-odd O(a) correction) and an O(a^2) obstruction. (2) Spin 1: noncompact lattice U(1) field, H_EM(N) = sum_l Nlink (g^2/2) E^2 + sum_p Nplaq (cB/2g^2) F^2, Gauss_x = div E first class, G_A[xi] = sum xi_(y,i) E_(y+i,j) F_ij(y). Exact: among translation-invariant timings supported on link endpoints and plaquette corners, the bracket is bond-supported (also modulo Gauss with arbitrary multipliers) for exactly 8 classes, each axis timed at one endpoint and each plaquette at the matching corner; none is reflection-symmetric; a local rule covers position-dependent corner timings; a staggered reflection-symmetric timing that breaks unit translations also closes, with a caveat on its generator. With forward timing {H_EM(N), H_EM(M)} = G_A[-cB xi~] exactly; one total relabelling iff cB = -sK/(4 alpha), independent of g; scalar + Maxwell + gravity close iff c_phi = cB = K/(4 alpha). Every cone value is relative to the supplied generator normalisations (unit translations, ratio lambda_s/lambda_1 = 1 to gravity's linear shift); in the continuum, {G,G} closure with delta_xi h = L_xi g forces the scalar and Maxwell generators to one common structure constant, so their cones are equal (derived, continuum leading order), but leaves gravity's linear-shift weight lambda_1 free, so equality with K/(4 alpha) holds given the supplied ratio, or via the checked chain of campaign block B19 (gravity's own order-h {G,C} with a quadratic G2, giving every matter cone the TT-graviton cone K2/(4 alpha), and K1 = K2 when block 101's quadratic Hamiltonian is read as C(N = 1) of the lapse-smeared constraint), under B19's listed premises; the lattice {G,G} is not checked; for spin 1/2 the h-independent Kosmann relabellings close only up to an on-site rotation term, which an h-dependent connection term on the joint metric-spinor phase space absorbs (repository 2026-09-13 native-Weyl canonical-metric note; campaign C4b, checked). Continuum leading order: {G,C} over a 126-coefficient quadratic coupling selects the Maxwell metric stress plus lam tr h H_EM (mod Gauss); Gauss enters with field-dependent multipliers. Compact U(1): F -> sin F, same algebra. Exact uniform-shift identity {G_A[e0], H_EM(1)} = (g^2/2) sum (Delta E)^2 - (cB/2g^2) sum (Delta F)^2 + g^2 sum E Gauss, coupling-independent, caused by the one-sided action of G_A; O(a) by power count. (3) Anisotropic cones: a Weyl species with constant triad E has [h_N, h_M] = -(frame-E Kosmann derivative along g w), g = E^T E; it closes against the isotropic structure function iff g = kappa I; density improvements, anisotropic matter relabellings (excluded by {G,G}), lapse rescalings and an O-symmetric gravity sector do not evade this; {G,G} also closes with delta_xi h = L_xi g0 for any constant symmetric g0, which would give every species the shared cone metric kappa g0^-1, so it cannot rescue one anisotropic species among isotropic ones, but the isotropy (like the scale) of the structure function comes from the supplied G_g or from cubic covariance, not from {G,G} (gravity's h-linear {G,C} might fix g0; not computed); a lattice scalar with per-axis gradient coefficients closes iff they are equal. Not claimed: exact lattice closure, the lattice {G,G}, nonlinear strain, a triad or rotation constraint, any value of Newton's constant, the corner-step application, or any physical identification."
upstream_dependencies:
  - curvature_member_closure_with_matter_forces_one_common_cone_and_the_lorentzian_sign_and_has_an_order_a_squared_obstruction_bounded_theorem_note_2026-10-18
  - admissibility_rule_the_curvature_members_constraint_algebra_closes_on_the_lattice_only_at_beta_equals_minus_alpha_and_there_the_walkers_own_states_cannot_be_its_content_bounded_theorem_note_2026-09-24
runner: scripts/curvature_member_closure_spin_half_and_spin_one_common_cone_2026_10_18.py
---

# Curvature-member closure with a lattice Weyl field and a lattice Maxwell field: the scalar's cone, exact lattice obstructions, and no anisotropic cones

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact within the supplied models. Fresh-context checks of the same model family confirmed the core claims and corrected several scopes; those corrections are built in. This consolidation narrows two further statements: what `{G, G}` closure fixes about the cone (Result 2.3) and the spin-½ relabelling algebra (Result 4). Nothing is adopted.

## Question

The companion scalar note (same PR, not yet on main) adds a supplied real scalar to the 2026-09-24 curvature-member constraints. Requiring one lapse/relabelling algebra then ties the scalar's cone to `K/(4α)`, fixes the Lorentzian sign of the curvature term given `c > 0`, and leaves an `O(a²)` lattice obstruction in `{G, C}`.

This note asks the same questions for spin ½ and spin 1, and asks one more:

- Does a naive lattice Weyl or Dirac field close against the same constraints, and on which cone?
- Does a lattice U(1) Maxwell field close, with which lapse timing, on which cone, and how does the Gauss constraint enter?
- Does either close exactly on the lattice, and if not, at what order does it fail?
- Can a species whose cone is anisotropic close against the gravity sector's isotropic structure function?

## Result

Notation: `ξ̃_b = N_{x+e} M_x − N_x M_{x+e}` on bonds; `w = N∇M − M∇N` in the continuum, with `ξ̃/a → −w`; `κ = K/(4α)`. Gravity alone gives `{C_g(N), C_g(M)} = G_g[(sK/(4α)) ξ̃]` exactly on the lattice (09-24 T1, either sign), and `G_g[−(sK/(4α)) w]` in the continuum (W5). Every generator below moves its fields along `+ξ` ("common orientation").

### 1. Spin ½: a naive Weyl or Dirac field lands on the scalar's cone, and does not close exactly

The supplied field is `h_N = Σ_b w̄_b (−iv/2)(σ^j |x⟩⟨x+e_j| − h.c.)` with `w̄_b = w_a N_x + w_b N_{x+e}` and `w_a + w_b = 1` (the endpoint mean is `t = w_a = ½`). For `N = 1` this is `v σ·sin p`, doublers kept. `H_f(N) = ψ̄ h_N ψ` with `{ψ, ψ̄} = −i`, so that `{H_f(N), H_f(M)} = −i ψ̄ [h_N, h_M] ψ` (W0). The relabelling is `G_f[u] = ψ̄ (i L_u) ψ`, with `L_u = u·∇ + ½ div u + (i/4)(curl u)·σ`. The spin coefficient `i/4` is fixed by rotation invariance of `σ·∇` before any bracket is computed (W1, two paths).

1. **One cone.**
   - Continuum, exactly: `[h_N, h_M] = −v² L_w` (W2, two paths). The spin term comes out of the bracket.
   - Lattice, exactly at `O(a⁰)`: the same `−v² L_w`, for `t = ½, 1, ¼` (W6: exact symbols with symbolic relative momentum at two rational momentum points; `--full` adds a 3D Taylor-expansion path with symbolic `t` for all smooth fields, W26).
   - So at leading order `{H_f(N), H_f(M)} = G_f[v² w]`. One total relabelling `G_g[ξ] + G_f[ξ]` needs `v² = −sK/(4α)`, which is the scalar's `c` (W5). This value is relative to the supplied unit normalisation of `G_f` (Results 2.3 and 4).
2. **The sign.**
   - With anti-Hermitian Clifford generators `γ^j = iσ^j` the bracket is `+v² L_w` (W3). The sign of the coefficient is the Clifford signature.
   - The supplied `h_N` is Hermitian and `v` is real, so `v² > 0`. With the supplied `K, α > 0` and the common orientation, only `s = −1` closes, and then `v² = K/(4α)`.
   - The scalar needed `c > 0` as a premise; here positivity follows from the Hermitian form of the supplied operator, which is itself supplied.
3. **Doublers.**
   - All eight species have the same `v²`. Each obeys the leading-order bracket with its own proper spin set `τ` (W9, symbols; W23, position space; Y6, continuum).
   - **Caveat.** `τ = σ` only at `k = 0` and `(π,π,π)`. At the six doublers with one or two `π` components, a `G_f` with the on-site spin term `(i/4)(curl ξ)·σ` fails at `O(1)` (W10). A lattice `G_f` that closes on them needs momentum-dependent spin structure.
4. **No exact lattice closure.**
   - Besides nearest-neighbour lapse pairs, the exact bracket contains (W11, symbols; W16, position space):
     - the six collinear range-2 pairs `±2e_j`, coefficient `∓ w_a w_b v²/4`; at the endpoint mean the term is `−(v²/16)(N_x M_{x+2e} − N_{x+2e} M_x)(|x⟩⟨x+2e| − h.c.)`, spin-independent;
     - the six mixed diagonal pairs `±(e_j − e_k)`, coefficient `∝ (w_a² − w_b²)`;
     - no same-sign diagonal pairs, at any timing.
   - The non-nearest-neighbour part vanishes only at `w_a = w_b = 0` (W11, W17).
   - The gravity relabelling map has exactly the constant shifts as kernel (W18, `L = 3, 4, 5`). So a closing total `ξ` equals gravity's `(sK/(4α)) ξ̃` up to a constant.
   - Hence **no linear `G_f` of any range closes the order-ε algebra exactly**:
     - translation-covariant `G_f`: the range-2 symbol monomials lie outside the span `Σ_j (X_j − Y_j) g_j(XY, P)` of every such `G_f` (W12); and a localised bracket at `ξ̃ = 0` cannot equal a translation-invariant `G_f[constant]` (W20);
     - arbitrary linear `G_f`: at `L = 5`, the 186 lapse pairs with `ξ̃ = 0` give brackets whose off-site parts have exact rank 186, against `dim G_f[constants] ≤ 3` (W19), at the endpoint mean (`d = 2e_j`) and at `t = 1` (`d = e_j − e_k`).
   - Adding `C(λ)` does not help: `kin(λ)` is the only `P²` term at this order, so `λ = 0`. On-site internal constraints cannot touch off-site entries.
   - The scalar, by contrast, closes exactly at order ε (companion note).
5. **Order of the obstruction** (exact symbols, two rational `(K, p)` points, against the most general translation-covariant `G_f` order by order).
   - Endpoint mean: the `O(a)` part vanishes; the `O(a²)` part is not absorbable (W7). In 1D it is not absorbed by any `O(a²)`-corrected relabelling either, while a free bilinear shift would absorb it (W24).
   - `t = 1` and `t = ¼`: the `O(a)` part has a part cubic in the relative lapse momentum, so no `O(a)`-corrected translation-covariant `G_f` absorbs it (W8).
6. **Mass and Wilson term** (naive Dirac, `α^j = offdiag(σ^j)`, `β = diag(1, −1) ⊗ 1`).
   - On-site mass `m N_x β`: at the endpoint mean the mass drops out exactly, `[h_N, h_M] = 1₂ ⊗ [Weyl bracket]` (W13, W22). In the continuum an arbitrary position-dependent mass drops out (W4).
   - For `t ≠ ½` the mass cross terms are proportional to `(2t − 1)`, and are exactly `Σ_j ξ̃_j g_j` with Clifford-odd (`αβ`-type) `g_j` (W14, W21). They block only a Clifford-even (Kosmann-class) `G_f`. The endpoint mean is selected independently by the massless `O(a)` obstruction (item 5).
   - Wilson term (`r = 1`, endpoint mean): the `O(a)` term is nonzero and Clifford-odd, so it blocks a Kosmann-class `G_f`. It is linear in the relative momentum, so a `G_f` with a Clifford-odd `O(a)` correction absorbs it. Against a general translation-covariant `G_f` the obstruction is `O(a²)` (W15; 1D form W25).

### 2. Spin 1: a lattice Maxwell field needs one-sided timing and lands on the same cone

The supplied field has `A_l` and `E_l` on links and `F_p` on plaquettes, `F_ij(y) = A_{y+i,j} − A_{y,j} − A_{y+j,i} + A_{y,i}`. `H_EM(N) = Σ_l N_l (g²/2) E_l² + Σ_p N_p (c_B/(2g²)) F_p²`, with link lapse `u_tail N_x + u_head N_{x+j}` and plaquette lapse `Σ_c w_c N_c` over its corners. `Gauss_x = div E` is first class. The gauge relabelling is `G_A[ξ] = Σ_{y,i} ξ_{(y,i)} Σ_{j≠i} E_{(y+i,j)} F_ij(y)`. "Mod Gauss" means the identity is required only on `div E = 0`, implemented exactly as `E = curlᵀ b + h` (X0); this admits Gauss terms with arbitrary, even nonlocal, field-dependent multipliers.

1. **Timing.**
   - Among translation-invariant timings supported on link endpoints and plaquette corners (two weights per axis and four per plane, each normalised), `{H_EM(N), H_EM(M)}` depends on the lapses only through bond `ξ̃` for **exactly 8 classes**: each axis timed at its tail or its head, and each plaquette at the corner where its two axes' chosen endpoints meet. The same 8 hold mod Gauss. None is reflection-symmetric.
     - Three exact routes agree: the polynomial engine with symbolic lapses over 21 uniform timings plus the 8 orientations (X1, X2, `L = 3`); the hand-derived local equations (X4); and the classification generated from the computed incidence-formula bracket, exactly and mod Gauss (X5, `L = 4`).
     - The reflection-symmetric (mean, four-corner) timing leaves 162 non-bond lapse pairs at `L = 3` and 384 at `L = 4`, none removed mod Gauss (X1, X8). Gauss cannot be supported on one plaquette's links (X3).
   - **Local rule.** For corner-supported timings that may vary from place to place, the bracket is bond-supported iff each plaquette puts weight only on corners whose opposite corner is not covered by its links' timing supports. The proof is a short computation (below). Exact sampled confirmation: 12 random rule-obeying timings are bond-supported and 12 single-plaquette violations fail, even mod Gauss (X6). A two-sided axis covers all four corners of each of its plaquettes, which recovers the 8 classes (X7).
   - **Staggered counterexample (scope).** Reflection-symmetric closing timings exist if unit translations are broken. Links at their even endpoint and plaquettes at the mean of their two odd corners give an exactly bond-supported bracket, invariant under every axis reflection and the point reflection about an even site (X8). Relative to the generator it induces, it closes with gravity at `c_B = κ` (X13). This is automatic once the bracket is bond-supported, so the cone value has content only through that generator's normalisation. **Caveat:** that generator carries an `O(1)` staggered (doubler) component on smooth fields, and its `{G, C}` ratio drifts from 1.000 to 1.072 over `L = 16–56` in the campaign check (one configuration, floating point). The consolidation review finds that at uniform `ξ = e₀` its action on `F` is the forward generator's smooth part (within 4%, `L = 8–16`) plus a doubler-momentum part 1.5–2.0 times as large (floating point, one configuration). This suggests an `O(1)` defect; it is not proved.
   - The scalar closes with the symmetric endpoint mean; Maxwell does not, because both `E` and `B` live on extended cells. Forward timing is the common cubical cell-ownership convention, so "upwind" overstates it.
2. **The bracket and the cone.**
   - With forward timing, `{H_EM(N), H_EM(M)} = G_A[−c_B ξ̃]` exactly with symbolic lapses; `g` cancels (X9). The generator the bracket induces is `G_A` bond by bond (X10, second engine).
   - With gravity, the order-ε bracket closes into one `G_g[ξ] + G_A[ξ]` iff `c_B = −sK/(4α)`, for `g² = 1` and `9/4`. The Maxwell mode's speed² is `g²·(c_B/g²) = c_B` (X11).
   - Scalar + Maxwell + gravity (`s = −1`) close into one `G_g + G_m + G_A` iff `c_φ = c_B = K/(4α)` (X12b). **One cone for spin 0 and spin 1**, with the supplied unit normalisations (item 3).
   - The compact theory, `H_B = Σ N_p (c_B/g²)(1 − cos F_p)`, gives the same algebra with `F → sin F`, exactly to all orders in the field (X16).
3. **The cone value depends on the generator normalisation. Closure of `{G, G}` makes the matter cones equal, but does not fix them against gravity.**
   - Rescaling `G_A → 2G_A` moves closure to `c_B = 2κ` (X12). `G_A[e₀]` acts on `A` as the unit backward translation plus a gauge gradient, and `G_m[e₀]` acts on `φ` as the unit central translation (X12). These unit normalisations are supplied.
   - In the continuum, with the full `δ_ξ h = L_ξ g` at `O(h)`, the unit generators of gravity, the scalar and Maxwell (`G_Lie`) all obey `{G_s[ξ], G_s[η]} = G_s[[ξ, η]]`. Write gravity's generator as `λ₁ G₁ + G₂`, with `G₁` the linear shift `δh = 2∂ξ` and `G₂` its `O(h)` part, and give the matter sectors weights `λ_m`, `λ_A`. Closure of the total `{G, G}` forces `λ_m, λ_A ∈ {0, 1}`, the structure constant of `G₂`, and leaves `λ₁` free (N1).
   - So, at continuum leading order, **the matter cones equal each other (derived)**: each species' cone is `λ_s K₁/(4αλ₁)` (campaign block B19 and its check), and `λ_m = λ_A`.
   - **Their equality with `K/(4α)` is conditional.** It holds given the supplied ratio `λ_s/λ₁ = 1`, which is what identifying `h = g − δ` and normalising every generator as a unit translation does. Alternatively it follows from campaign block B19, now checked (fresh-context, same family, 19 PASS, with fully general ansätze: a 648-coefficient one-derivative `G₂`, 120/126-coefficient couplings, an 18-coefficient lapse rule). Including gravity's own `{G, C}` at linear order in `h`, which needs a quadratic generator `G₂`, gives in one solve `λ_m = λ_A = λ₁K₂/K₁`, so every matter cone equals the TT-graviton cone `K₂/(4α)`.
     - `K₁ = K₂` (hence `κ`) needs block 101's quadratic Hamiltonian to be read as `C(N = 1)` of a lapse-smeared constraint, with `R₂` inside `C`.
     - Further premises of that chain: one total `C` and one total `G`; a field-independent, local, first-order lapse rule; `G₂` local, `P`-linear and one-derivative; the Fierz–Pauli form of `R₂`.
     - The check also notes that the scalar-lapse rule `s₂ = 0` is a lapse/density-weight convention (only `s₁` enters the cone), that `λ_s` is invariant only under sector-preserving canonical maps (only ratios are meaningful), and that whether degree-2 brackets force `K₁ = K₂` by themselves is open.
     - This note does not reproduce the B19 computations.
   - The B16 check's argument that `{G, G}` closure fixes the matter normalisation against gravity, and hence the value `κ`, does not hold: `λ₁` is free (N1, agreeing with B19 and its check).
   - **Open:** the lattice `{G, G}`. Campaign block B19 and its check report that the lattice relabellings do not close among themselves (scalar `O(a²)`, one-sided Maxwell `O(a)`; slopes −2.3 and −0.89 after optimising over the comparison field), so a lattice normalisation is pinned at best asymptotically.
   - For spin ½ see Result 4.
4. **Continuum leading order** (exact jet calculus).
   - `{C(N), C(M)}` with `C = kin − K R1 + H_EM` equals `G_g[ξ₀] + P_A[ξ₀]`, `ξ₀ = κ(N∇M − M∇N)`, with no Gauss term, iff `c_B = K/(4α)`; `g` drops out (X21).
   - Over a coupling with a general quadratic form in `(E, F)` for each strain component (6 × 21 = 126 coefficients, no isotropy imposed), `{G[ξ], C(N)}` at `O(E², F²)` equals `H_EM(s₁ ξ·∇N + s₂ N div ξ)` mod Gauss exactly on a one-parameter family. That family is the metric-variational stress of `H_EM(g)` (`E` a vector density, `A` a one-form; X23) plus `λ tr h H_EM`, with `s₁ = 1`, `s₂ = −2λ` (X24).
   - With `--full`: `{C, C}` alone does not fix the coupling (X27); the scalar-lapse rule `s₂ = 0` makes it unique, with structure function `g^{ij} = δ^{ij} − h^{ij}` (X28); `r₂ = −s₂` (X29); scalar and Maxwell together close iff `c = c_B = κ` and share one `λ` (X30); an independent Function-based route reproduces X24, and shows that without Gauss `P_A` has no solution while `G_Lie` closes on the same family (X31, X32).
5. **Gauss enters with field-dependent multipliers.**
   - Lattice: with `G_A`, `{C, C}` closes with no Gauss term (X9, X11). With the pure-translation generator `G_L = G_A − Gauss[θ(ξ, A)]`, `{H_EM(N), H_EM(M)} = G_L[−c_B ξ̃] + Gauss[λ]` with `λ_w = −c_B Σ_i ξ̃_{(w−i,i)} A_{(w−i,i)}`; the total algebra then closes only on the Gauss surface, or once local terms `Gauss_w A_l` are allowed (X15). Gauss is first class (X14).
   - Continuum: with `G_Lie`, `{C, C}` needs `Gauss[ξ₀·A]` (X22). With the metric stress, `{P_A[ξ], C(N)} = H_EM(ξ·∇N) + Gauss[g² N ξ·E]`, while `{G_Lie[ξ], C(N)} = H_EM(ξ·∇N)` (X25). `{P_A[ξ], P_A[η]} = P_A[[ξ, η]] − Gauss[F_ij ξ^i η^j]`; Gauss is an ideal and `G_Lie` a subalgebra (X26).
6. **The lattice `{G, C}` obstruction is `O(a)` and comes from the one-sided generator.**
   - `G_g[uniform shift] = 0` identically, so at order (matter², h⁰) no coupling built from `h` or `P` enters `{G[e₀], C(N)}`.
   - Exact identity (X17 polynomial engine; X18 quadratic forms, `L = 3`, and `L = 4` with `--full`):

     `{G_A[e₀], H_EM(1)} = (g²/2) Σ_l (E_l − E_{l−e₀})² − (c_B/(2g²)) Σ_p (F_p − F_{p−e₀})² + g² Σ_w E_{(w−e₀,0)} Gauss_w`.
   - `{G_A[uniform], H_EM(N)}` is not `H_EM(N')` for any `N'`, even mod Gauss, at `N = 1` and at a random `N` (X19). The companion note's scalar has `{G_m[uniform], H_m(1)} = 0` but also fails for random `N`, so its `O(a²)` obstruction occurs where `G_g = 0` and does not depend on its coupling ansatz (X19).
   - **Cause.** `G_A` acts by one-sided differences: `{F_p, G_A[e₀]} = F_p − F_{p−e₀}` and `{E_l, G_L[e₀]} = E_{l+e₀} − E_l` (X20). The operator `D = 1 − T⁻¹` is not antisymmetric; `D + Dᵀ = 2 − T − T⁻¹` is exactly the sum of squares in the identity. The scalar's central `G_m` is antisymmetric. So the `O(a)` comes from the one-sided `G_A` that the timing forces, not from Maxwell as such.
   - **Order.** With `D ~ a∂`, the defect is `O(a)` relative to the leading `H(ξ·∇N)`; the scalar's residual is `O(a²)`. This is a power count. The campaign check measured slopes −1.03 (Maxwell, `L = 8–40`) and −2.06 (scalar) on one smooth configuration; `--diag` reproduces the Maxwell measurement on `L = 8–24` (not gating).

### 3. Anisotropic cones cannot close against the isotropic structure function

1. A Weyl species with a constant triad `E`, `h_N = ½ Σ E_aj {N, σ^a(−i∂_j)}`, has exactly `[h_N, h_M] = −(ξ·∇ + ½ div ξ + frame-E spin term)` with `ξ = g w`, `g = EᵀE`. Its derivative part is the scalar `−g^{kj} w_j ∂_k` (Y1: uniaxial, generic and reflected triads; Y2: a second component extraction for the uniaxial case).
2. `w` takes any value at a point, so this equals `−κ w·∇` for all lapses iff `g = κ I` (Y3). For a uniaxial cone the spin part independently forces `v_a = v_t` (Y4).
3. **Loopholes that do not rescue closure.**
   - Density improvements `∂_jN ψ†B^jψ` (any Hermitian `B^j`) add only a traceless derivative term and leave the scalar part `−g^{kj}w_j∂_k` (Y5).
   - A matter relabelling along `Aξ` with constant `A`: since `[Aξ, Aη] = A((Aξ)·∇η − (Aη)·∇ξ)` exactly, closing `{G, G}` with gravity's `[ξ, η]` forces `A = νI`, and gravity fixes `ν = 1` (Y8). One total constraint has one `ξ`.
   - Non-diagonal cone metrics are covered by Y1 and Y3.
   - Lapse rescaling of a sector multiplies its bracket by a scalar; it cannot produce direction dependence.
   - Another single-metric gravity sector with the octahedral symmetry: a cubic-invariant symmetric tensor is a multiple of `δ` (Y9), so its structure function is isotropic.
   - **Scope of the isotropy itself.** `{G, G}` also closes with `δ_ξ h = L_ξ g₀` for any constant symmetric `g₀`. Gravity's order-ε bracket is then matched by `ξ = κ g₀⁻¹ ξ̃`, so every species would share the cone metric `κ g₀⁻¹`. That cannot rescue one anisotropic species among isotropic ones. But the isotropy of the structure function, like its scale, comes from the supplied `G_g` or from cubic covariance (Y9), not from `{G, G}`. Gravity's `h`-linear `{G, C}` might fix `g₀`; that is not computed.
   - A constant coordinate change or background strain maps every metric `g_s → Aᵀ g_s A`. It can make all species isotropic at once only if their metrics are proportional.
   - Closure is an identity of the whole matter sector. A species cannot be dropped by restricting to part of momentum space if it shares the energy window.
4. **Lattice form for the scalar** (runner-added). With per-axis gradient coefficients `c_j`, `{H(N), H(M)} = G_m[−c_j ξ̃]` bond by bond exactly, and the total closes with gravity iff `c₀ = c₁ = c₂ = K/(4α)` (Y7).
5. This is the Hojman–Kuchař–Teitelboim statement that every species' cone metric must equal the structure function, made explicit for these supplied fields. Its application to the corner step's doublers lives in the scale-ladder note, not here.

### 4. A qualification for spin ½: Kosmann relabellings close only up to an on-site rotation

- Exactly (sympy Functions): `[L_ξ, L_η] = L_{[ξ,η]} − (i/2) ε_{kij} (S_ξ S_η)_{ij} σ_k`, where `S_ξ` is the symmetric part of `∇ξ` (N2). The remainder vanishes when `ξ` or `η` is a conformal Killing field (then `S` is a multiple of `δ`; checked for dilations and special conformal fields by the consolidation review), and not in general.
- So `{λ G_f[ξ], λ G_f[η]} = λ² (G_f[[ξ, η]] + rotation term)`. The transport part behaves like the other matter sectors in Result 2.3. But the remainder is a local spin rotation, which this flat, triad-free model does not carry as a constraint.
- So the campaign's statement that the normalisation argument "also holds for `G_f`" needs a further premise. A triad with a rotation constraint is one option, but it is not needed. On the joint metric–spinor phase space, an h-dependent connection term in `G_f`, from the symmetric-section (polar) lift, absorbs the remainder exactly.
  - This was already shown in the repository's 2026-09-13 native-Weyl canonical-metric note (`docs/NATIVE_WEYL_CANONICAL_METRIC_CONSTRAINTS_BOUNDED_THEOREM_NOTE_2026-09-13.md`, its P7/P13).
  - Campaign block C4b, checked independently with a constructed rather than fitted connection term, confirms it. With that term, `{G, G}` forces the spinor weight to equal the structure constant, as for the scalar and Maxwell.
  - So, in the continuum, the spin-½ cone equals the other matter cones under the same premises.
  - An earlier draft of this result said a triad with a rotation constraint was required. That was too strong, and it conflicted with the 09-13 note.

## How this bears on the gravity lane (interpretation, not a claim)

- **Which K sets the cone (campaign block B21, independently checked; continuum).** In the supplied member one K multiplies both the first- and second-order curvature terms. Invariantly, the cone is fixed by the second-order (TT) coefficient: the canonical rescaling (h, P) → (ρh, P/ρ) preserves every bracket while moving the ratio of the two coefficients. So "c = K/(4α)" here reads as "every matter cone equals the graviton's TT cone", given the member's single K.

- Within these supplied models and their unit generator normalisations, one lapse/relabelling algebra puts spin 0, spin ½ and spin 1 on the single cone `K/(4α)`. That the matter cones agree with each other is derived in the continuum for spin 0 and 1; that they equal `K/(4α)` rests on the supplied normalisation ratio, or on B19's checked gravity-sector chain under its listed premises (including the reading of block 101 that gives `K₁ = K₂`). For spin ½ the Lorentzian sign follows from the Hermitian form of the matter operator; for spin 0 and 1 it needs the supplied positivity of `c` or `c_B`.
- It also rejects anisotropic cones. Together with lattice doubling, that acts as a selection rule on step rules; the application is in the scale-ladder note.
- Exact lattice closure fails for every field beyond the scalar's order-ε bracket, with explicit monomials: `O(a²)` for the scalar and for the fermion at the endpoint mean, `O(a)` for Maxwell with its forced one-sided generator. A lattice version of "all matter shares one cone and sources gravity through its stress" therefore needs either modified discretisations or a statement up to controlled lattice terms. Neither is supplied here.
- Not shown: Newton's constant, nonlinear strain, a triad or rotation constraint, the lattice `{G, G}`, or whether any of the repository's own walks or steps realise these fields.

## Premises

- **Axioms used.** None beyond the lattice and its translations. `docs/MINIMAL_AXIOMS_2026-06-29.md` supplies no dynamics or time metric, so every clause below is supplied.
- **Supplied (gravity).** The 09-24 clauses as used in the companion note: block-62 placement, `R1`, kinetic Legendre form at `β = −α`, four-corner face timing, `G_g[ξ] = Σ P·δ_ξ h`, and `K, α > 0`. In N1 only, the full `δ_ξ h = L_ξ g` at `O(h)`.
- **Supplied (spin ½).** The naive operator `h_N` with two-endpoint bond timing; Hermitian `σ^j`; real `v`; the Grassmann bracket `{ψ, ψ̄} = −i`; `G_f[u] = ψ̄ (iL_u) ψ` with the Kosmann `L_u`, unit normalisation and the common orientation `{ψ, G_f[u]} = L_u ψ`. For Dirac: `α^j`, `β`, on-site mass, Wilson term `r Σ_b w̄_b β (…)`.
- **Supplied (spin 1).** `H_EM` with the stated field placement and timing family; `G_A` (its form is then derived from the bracket, X10); `Gauss_x = div E` as a first-class constraint; noncompact except in X16; `c_B > 0` for the sign statement.
- **Supplied (rules).** `δ_ξ h_ij = ∂_iξ_j + ∂_jξ_i` at order ε; the coupling ansatz of X24; in X28 only, the scalar-lapse rule `s₂ = 0`.
- **Convention.** `{q, p} = +1` for `(h, P)`, `(φ, π)`, `(A, E)`; one convention for all sectors.
- **Standard facts used.** Linear algebra over Q (exact ranks, Fredholm alternative), Laurent-polynomial symbols of translation-invariant lattice operators, Euler operators for local functionals, the Kosmann spinor Lie derivative.

## Proof sketches

- **Spin ½, the bracket.** `{ψ̄Aψ, ψ̄Bψ} = −iψ̄[A, B]ψ` reduces everything to the one-particle commutator `[h_N, h_M]`, bilinear and antisymmetric in `(N, M)`. In the continuum, `σ^jσ^k = δ^{jk} + iε^{jkl}σ^l` gives the transport term from `δ^{jk}` and the spin term from `ε^{jkl}`; this is a polynomial identity of plane-wave symbols. With anti-Hermitian generators `(iσ^j)(iσ^k) = −(δ + iεσ)` flips the sign.
- **Spin ½, absorbability.** A translation-covariant linear `G_f` acting on gravity's `ξ̃` has symbol `Σ_j (X_j − Y_j) g_j(XY, P)` with `X = e^{iak}`, `Y = e^{iaq}`. Writing `k = K/2 + κ`, `q = K/2 − κ`, its `a`-expansion is `Σ_j 2i e^{iaK_j/2} (sin(aκ_j)/a) g_j`. Order by order, `B₀` and `B₁` must be linear in `κ`, and `B₂ + Σ_j κ_j³ ∂_{κ_j} B₀/6` must be linear in `κ`. One exact rational point where this fails proves non-absorbability at that order, for every `g_j`.
- **Spin ½, arbitrary linear `G_f`.** For lapse pairs with `ξ̃ = 0`, the gravity `P`-part forces the total `ξ` to be constant (kernel of `G_g`), so the fermion bracket must lie in `{G_f[constant]}`, a space of dimension at most 3, whatever `G_f` is. Exact rank 186 excludes this.
- **Spin 1, the local rule.** By the incidence formula `{H(N), H(M)} = c_B Σ_{k,p} (∂F_p/∂A_k) E_k F_p [m_p(N) n_k(M) − n_k(N) m_p(M)]`, only corner pairs of one plaquette `p` occur. Nearest-neighbour pairs are bonds; a diagonal pair `(s, t)` lies in exactly one plaquette (`L ≥ 3`). Each link `l ∈ ∂p` touches exactly one of `s, t`, so its contribution `E_l F_p (w_ps u_lt − u_ls w_pt)` reduces to `u_ls w_pt` (or `u_lt w_ps`). Different `l` give independent monomials, and their `E`-combination is never a Gauss term (X3). So bond support holds iff `u_ls w_pt = 0` for every link timed at `s` and `t` opposite `s`.
- **Spin 1, the cone.** The `P`-linear part of the total bracket is gravity's, the `EA` part is `G_A[−c_B ξ̃]`. A common `ξ` must satisfy `G_g[ξ − (sK/(4α))ξ̃] = 0` and `G_A[ξ + c_B ξ̃] = 0`; the first forces `ξ = (sK/(4α))ξ̃ + const`, and the second then forces `c_B = −sK/(4α)` for generic lapses. X11 checks the full table.
- **Spin 1, the uniform-shift identity.** `G_A[e₀] = Eᵀ D A` up to gauge with `D` the backward difference, so `{G_A[e₀], H(1)}` is the symmetrised quadratic form of `D` in each sector, `½(D + Dᵀ) = −½ Δ_{e₀}`. The Gauss term is the gauge part of `G_A`.
- **Normalisation.** For a cotangent lift `G[ξ] = ∫ p L_ξ q`, `{G[ξ], G[η]} = ∫ p [L_ξ, L_η] q = G[[ξ, η]]`; with relative factors `λ_s`, the total bracket is `Σ λ_s² G_s[[ξ, η]]`, which is `Σ λ_s G_s[μ]` for one `μ` only if every nonzero `λ_s` is equal. Gravity's linear shift `G₁ = ∫ P·2∂ξ` is abelian on its own and enters the bracket only through `{G₁, G₂}`, which returns `λ₁ G₁[[ξ, η]]` for any `λ₁`; so its weight is unconstrained. N1 computes this for gravity, scalar and Maxwell; N2 computes the Kosmann commutator.
- **Anisotropic cones.** The frame-E Kosmann identity is the isotropic one transported by the linear map `x = Eᵀy`; the rest is linear algebra (Y3, Y8, Y9).

## Relation to prior work

- **Continuum content is known.**
  - Schwinger's energy-density commutator condition for spin 0, ½ and 1 (Schwinger 1962–63; in particular Phys. Rev. 130, 800 (1963)) already contains the continuum statement that the fields' energy densities close with a common structure function.
  - Teitelboim, Ann. Phys. 79, 542 (1973); Kuchař, J. Math. Phys. 15, 708 (1974) and 17 (1976); Hojman, Kuchař and Teitelboim, Ann. Phys. 96, 88 (1976): the surface-deformation algebra forces a common signature and a common light cone, and every species' cone metric must equal the structure function (Result 3 in continuum form).
  - Barbour, Foster and Ó Murchadha (2002) and Anderson and Barbour (2002), "relativity without relativity": a universal light cone from consistent propagation of the Hamiltonian constraint with matter (attribution from campaign block B19 and its check, not re-verified).
  - Nelson and Teitelboim (1978): the Dirac field in the Hamiltonian deformation algebra. Isham and Kuchař, Ann. Phys. 164, 288 and 316 (1985): representations of spacetime diffeomorphisms in canonical parametrised field theories and geometrodynamics (the campaign's attribution of a gauge-field/Gauss-constraint treatment is not verified). Deser, Gen. Rel. Grav. 1, 9 (1970): universal coupling to the stress (Result 2.4 in continuum form). Kosmann (1972): the spinor Lie derivative; the failure of Kosmann lifts to form a Lie algebra away from (conformal) Killing fields is standard (Result 4).
- **Lattice breaking of the algebra is expected.**
  - Koo and Saleur (1994): lattice Virasoro generators close only in the scaling limit.
  - Loll (1997, gr-qc/9708025): diffeomorphism commutators of lattice gravity. Bonzom and Dittrich (arXiv:1304.5983): discrete hypersurface-deformation algebras. arXiv:2305.10097 (cited by the B15/B16 checks; title not verified).
  - Renteln and Smolin, CQG 6, 275 (1989); Gambini and Pullin (consistent discretisations, e.g. PRL 90, 021301 (2003)); Bahr and Dittrich, CQG 26, 225011 (2009).
  - Cubical cell ownership, in which each cell is timed at its base corner, is a common lattice convention; the forward timing of Result 2.1 is that convention.
- **Repository.** The companion scalar note, same PR (one cone for spin 0, the sign, the `O(a²)` monomial); the 09-24 note (T1); the scale-ladder note (the corner-step application of Result 3).
- **New here, and narrow.**
  - The exact lattice realisation, in these discretisations, of the leading-order spin-½ and spin-1 closure on the scalar's cone.
  - The fermion obstruction: the explicit range-2 and mixed-diagonal monomials, the no-go for any linear `G_f`, and the order and timing classification, including mass and Wilson terms and the doubler spin caveat.
  - The Maxwell timing classification (exactly 8 one-sided classes; the local rule; the staggered counterexample), the exact uniform-shift defect identity and its cause.
  - The exact form of the Kosmann remainder as it bears on the normalisation argument (Result 4).
  - References follow the campaign checks' attribution. Henneaux (1983), cited in the campaign from memory, is not used.

## No-Go Discipline Gate

The negative sentences:
- no linear `G_f` of any range closes the order-ε spin-½ algebra exactly on the lattice;
- the spin-½ deviation is not absorbable at `O(a²)` (endpoint mean) or at `O(a)` (`t = 1, ¼`) by any order-corrected translation-covariant `G_f`;
- with Hermitian `h_N`, `s = +1` does not close;
- among translation-invariant corner-supported timings only the 8 one-sided classes close, also mod Gauss;
- `{G_A[uniform], H_EM(N)}` is not `H_EM(N')` for any `N'`;
- an anisotropic cone metric does not close against the isotropic structure function, and the listed loopholes do not rescue it.

- **N1 — routes by which they could fail or mislead.**
  - Non-naive fermion operators (improved hoppings, staggered or overlap fermions), geometric-mean or wider timings, field-dependent relabellings or nonlinear `G_f`.
  - Maxwell timings beyond link endpoints and plaquette corners; position-dependent timings beyond the local-rule class; generators not induced by the bracket.
  - A triad with a rotation constraint, which changes the spin-½ relabelling algebra (Result 4).
  - Higher strain orders; field-dependent structure functions beyond those found.
  - For anisotropic cones: gravity sectors with more than one metric, or with non-cubic symmetry.
- **N2/N3 — scope.**
  - Fermion: the symbol statements are exact identities of Laurent polynomials, evaluated at two rational `(K, p)` points for the order tests (a failure at one exact point suffices for non-absorbability); the position statements are exact at `L = 4, 5`; W19 covers every linear `G_f` at `L = 5`.
  - Maxwell: the classification is exact over the stated finite timing class at `L = 3` and `L = 4`; the local rule is proved, with 12 + 12 exact samples; X11 and X12b use one random integer lapse pair each.
  - Anisotropic cones: continuum leading order, constant triads; Y7 at `L = 3`.
- **N4 — inputs.** Exact rationals, Gaussian rationals or sympy throughout the gating tests. The staggered-generator and defect-order measurements are floating point, from the campaign check, reproduced in part by `--diag`, and not gating.
- **N5 — wording.** "Cone" means the equal coefficient `K/(4α)` of the transport term. "Lorentzian" names the sign of the deformation algebra. "`O(a)`, `O(a²)`" means the order of the first non-absorbable term. No physical identification is made.
- **N6/N7 — strongest objections.**
  - *"The fermion sign result only restates Hermiticity."* Yes; it says the sign follows from the supplied Hermitian form instead of a separate positivity premise.
  - *"The cone is fixed only up to the generator normalisation."* Yes. `{G, G}` closure in the continuum makes the scalar and Maxwell normalisations equal, so their cones agree, but it leaves gravity's linear-shift weight free (Result 2.3). The value `K/(4α)` is relative to the supplied ratio; for spin ½ even the equality is open (Result 4); the lattice `{G, G}` is open for all.
  - *"The Maxwell obstruction is an artefact of one-sided timing."* Yes; that is its stated cause. The staggered timing removes the uniform-shift defect but appears to have an `O(1)` problem of its own (not proved).
  - *"The no-gos are about one discretisation."* Yes; they are conditional on the supplied operators.
- **N8 — earlier claims.** The companion scalar note (same PR) is unchanged and is reused. The campaign B16 finding and its check say that `{G, G}` closure derives the normalisation, and that this "also holds for `G_f`". Result 2.3 (with N1 and the checked B19) restricts the first to matter–matter equality, with the value `K/(4α)` conditional as stated there, and Result 4 qualifies the second.

## Independent check

Three fresh-context agents of the same model family as the authors checked the campaign blocks this note consolidates. None is independent in model lineage. Each wrote its own code by a different route.

- **Spin ½ (B15 check).** Exact momentum-space symbol calculus (Laurent polynomials expanded in `a`), against the worker's position-space sparse operators and Taylor expansions.
  - Confirmed: the continuum bracket and `v² = −sK/(4α)`; the exact range-2 term; the no-go for any linear `G_f`; the orders; the doubler bracket; the mass cancellation at the endpoint mean.
  - Corrected, and adopted here: the sign needs `K, α > 0` and a common orientation; same-sign diagonal pairs cancel at every timing, only mixed ones survive; the `t ≠ ½` term is a genuine `O(a)` obstruction (the checker's own first expectation was wrong); the Wilson `O(a)` term is absorbable by a Clifford-odd correction; `τ = σ` at `(π,π,π)`, so the spin caveat concerns six doublers, not seven; prior-art additions.
- **Spin 1 (B16 check).** Its own lattice kernel with the closed incidence formula, and an independent continuum Function-based route.
  - Confirmed: the 8 one-sided classes (including mod Gauss); the cone and its `g`-independence; the stress family with Gauss imposed via `E = curl W`; the Gauss multipliers; the exact uniform-shift identity.
  - Corrected, and adopted here: reflection-symmetric closing timings exist once unit translations are broken (staggered), with an `O(1)` generator caveat; the `O(a)` is caused by the one-sided `G_A`; prior-art additions.
  - Not adopted: the check's conclusion that the normalisation, and with it the value `κ`, is derived from `{G, G}` closure and `δ_ξ h = L_ξ g`. N1 here and campaign block B19 (checked) find gravity's linear-shift weight free under `{G, G}`; only matter–matter equality follows from `{G, G}` (Result 2.3).
  - Not independently checked: the continuum structure function, the shared `λ` and `c_φ = c_B` (X27–X30); the scalar comparison at uniform shift was not rerun by the checker.
- **Anisotropic cones (B17 check).** Full-matrix symbols with a general constant triad, against the worker's single-component extraction. Confirmed the bracket and strengthened it; supplied the loophole list.
- **Campaign block B19** (generator normalisation; same model family) and **its check** (fresh context, same family, 19 PASS, more general ansätze, corrections listed in Result 2.3) are cited for the per-species cone formula, the single-lapse-rule argument, the gravity-sector order-`h` `{G, C}` chain and the lattice non-closure of the relabellings. Only the `{G, G}` part (λ₁ free, matter λ's equal) is reproduced here, by N1.
- **Consolidation review.** A reviewer of this note and runner, in fresh context and of the same model family (not independent in lineage), re-derived the tests written for this consolidation by different routes: N1 and N2 by field-space commutators of affine generators and polynomial vector fields with sign and conformal-Killing controls; the exact mod-Gauss restriction of X5 and X6 by a `ker(div)` nullspace and a separate sampler; X12b and X13 with a separate sparse Poisson engine; Y7, Y8 and Y9, the last by full `O_h` enumeration. All were confirmed; X13 is a consistency check. Result 4 and N1 disagree with sentences in the B16 check; the disagreements are recorded rather than resolved by majority.

This runner keeps two implementations wherever it was cheap (marked "two paths" or "path 2" in the output). Both are by the same model family, and both are adapted from the campaign and check scripts, so re-running this runner is not a further independent check.

## Verification

```bash
python3 scripts/curvature_member_closure_spin_half_and_spin_one_common_cone_2026_10_18.py
```

Expected: `TOTAL: PASS=65 FAIL=0`, in about 2.5 minutes (148 s measured) (Python 3, sympy; imports the companion scalar runner, same PR, for its exact polynomial Poisson engine). Parts:
- W: spin ½ (continuum, cone, lattice symbols, position space, 1D);
- N: what `{G, G}` closure fixes about normalisations;
- X: spin 1 (timing, local rule, bracket and cone, Gauss, compact U(1), uniform-shift identity, continuum);
- Y: anisotropic cones.

Optional:
- `--full` adds W26–W27, X27–X32 and the `L = 4` case of X18 (`TOTAL: PASS=73 FAIL=0`);
- `--diag` prints the floating-point Maxwell defect order (slope −1.04 on `L = 8–24`) and the staggered-generator ratio (not gating);
- `--full --diag` together took 504 s.

## Load-bearing sources

- [Companion scalar note (same PR)](CURVATURE_MEMBER_CLOSURE_WITH_MATTER_FORCES_ONE_COMMON_CONE_AND_THE_LORENTZIAN_SIGN_AND_HAS_AN_ORDER_A_SQUARED_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-10-18.md)
- [09-24 constraint-closure note](ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [Scale-ladder note (application of Result 3)](SCALE_LADDER_CROSS_RUNG_INVARIANTS_CORNER_FERMION_BOUNDED_THEOREM_NOTE_2026-10-18.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
