lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# LZ1-i: one common speed for all propagating light species, pass 1

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft for the lead to check and commit. It grants no status. It adopts no law, no reading and no specification. It changes no axiom and no working-set entry; `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means that the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks one tiny floating-point computation (§8). It guides and never proves.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local `claude/toe-assembly` (this checkout, HEAD) | `4e574516aa` |
| `origin/main` (fetched 2026-11-06; read with `git show` only) | `f5af11cd01` |
| `origin/docs/consolidate-lorentz-dispersion` (PR #10125, which carries #9913; read with `git show` only) | `586d7c81d0` |

**Files read, by line.** This folder: `prior/LZ1I.md` lines 1–77 (all); `LZ1.md` lines 1–215 (all); `TOE_ASSEMBLY.md` lines 1–100, 169–420, 490–680; `MT1.md` lines 1–133; `ZM1_OBS.md` lines 1–200; `GA1_5.md` lines 1–62, 121–192, 197–291; `LW1_5.md` lines 1–130, 258–310; `LW1.md` lines 43, 209, 322–334; `Y2W_DRAFT.md` lines 1–40 (for the format only). Main: `docs/EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md` lines 1–266 (all); `docs/EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md` lines 1–142 (all); `docs/EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md` lines 1–113; `docs/CURVATURE_MEMBER_CLOSURE_WITH_MATTER_FORCES_ONE_COMMON_CONE_AND_THE_LORENTZIAN_SIGN_AND_HAS_AN_ORDER_A_SQUARED_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-10-18.md` lines 1–26 (all) and its full argument `outputs/scale_ladder_continuations_review_2026_10_18/curvature_member_closure_with_matter_common_cone_2026_10_18_full_argument.md` lines 1–80 and 110–175; `docs/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md` lines 1–60 and 380–500; `docs/SOFT_SPIN2_COLLISION_INVARIANTS_COMMON_CONES_AND_LATTICE_WARD_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md` lines 225–271 and 444–460, with its section headings; `docs/CROSS_SECTOR_FRONT_SPEED_B4_TWO_SURFACE_ALIGNMENT_BOUNDED_THEOREM_NOTE_2026-07-16.md` lines 19–40 and 76–96, with its section headings; `docs/EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md` section headings and line 65. PR #10125: `docs/LORENTZ_DISPERSION_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` lines 1–137 and 740–817. The structural note `docs/EMERGENT_LORENTZ_INVARIANCE_NOTE.md`, the taste-census note and the other consolidation PRs were not read; nothing below uses them.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws `L5-U[m]` and `L5-O[S_+]` are read plainly, as `LW1_5.md` §2 states them. Where a common-speed theorem would need more than the laws give, §6 states the extra specification and four-tests it. Nothing is adopted.

**Working set and owner decisions used, by name.** PS-1 as read by PS-1c (cell covariance); PS-5 (five modes per site); PS-6 and PS-6r (finite link registers); PS-7 only through the word "half-filled"; GA1-P-NN = NN-a (`TOE_ASSEMBLY.md` line 235); LZ1-SC (line 229). R-CS^str appears only in the lane target; no result below uses it. Proposed readings used and not adopted: LZ1's D1 states, bands, nodes and light species (`LZ1.md` lines 34–37) and R-loc (line 40).

**Results used, by name.** All are ported with credit in §1 and are not re-derived: `LZ1.md` Theorems 4.1–4.2 and RC3; `MT1.md` Theorems 1, 4, 7 and the remark at line 93; `LW1.md` Theorems A2 and B10; `LW1_5.md` §2 and B1-U; `GA1_5.md` class GA1-P-5, Theorem 6.1, Lemma U and Proposition C; `ZM1_OBS.md` Theorems 1, 3, 9 and 9′.

**Inputs from outside the working set.** Standard mathematics, rebuilt where it is used: Schur's lemma for finite-dimensional unitary representations; the character-norm test for irreducibility; the standard representation of `S_4`; induction along a free action; Fourier series on `Z³`; the explicit solution of a scalar linear ODE. Literature (§7) gives context only. No citation is load-bearing.

---

## 0. The question, quoted

The lane brief: "decide LZ1-i on L5-O[S_+] or L5-U. Either prove that the interacting law forces one common limiting speed for all propagating light species (bosons in H_phys, fermions in R-CS^str sectors), from the law plus a stated, four-tested condition, ... or build a counterexample: an admissible interacting law in the live class with two propagating light species of different speeds."

`TOE_ASSEMBLY.md` line 61, target T3: "All light species share one limiting speed `c`." Line 338, LZ1(a): "for every light species (fermions, gauge bosons, graviton), the low-momentum dispersion is `E = c|k|(1 + O((a|k|)^p))` with the same `c`; ... [**open input LZ1-i**: a mechanism that fixes one common `c` across species]".

`LZ1.md` line 159: "**LZ1-i.** One common speed for all relevant propagating species remains open". Line 12, Amendment 2: "Attacks A1 and A3 of section 7 are therefore not counted toward the three-attack rule until they are redone with these inputs."

The species notion. `LZ1.md` line 36: "A **band** is `(d,F,V)`, where `d≥1`, `F:L²(T³;C^d)→H` is an isometry, `V:T³→U(d)` is continuous, and `T_βF=FM_β`, `ŨF=FM_V`". The same line: "It **propagates** if some `N_j≠0` ... A **Clifford cone** has `{N_i,N_j}=2v²δ_ij` for `v>0`. A proposed **light species** is a band with a node, wholly in `H_even` or `H_odd`." `TOE_ASSEMBLY.md` line 229, LZ1-SC: "Its dispersion clause applies only to bands whose image lies in the orthogonal complement of the tick-fixed vectors, `ker(Ũ−1)^⊥`."

## 0.1 Outcome in one paragraph

**Refuted on `L5-U[m]` for every even `m`, by an exact counterexample.** Fix even `m`, any allowed `(ε, μ, τ_E)` and two angles `θ₁, θ₂ ∈ (0, π/2)`. Append to the base tick two link-only layers `L(θ₁, θ₂)` (§3.5). The result is an admissible update: it lies in LZ1 §1's class and in the proposed class GA1-P-5, it is cell covariant and gauge invariant, and NN-a compiles it into nearest-neighbour layers (Lemma 3.6). This law has a stationary, gauge-invariant, even-translation-invariant, half-filled state `ω_Σ`, a frozen layered state (§3.1, Lemma 3.7). Its physical sector carries two propagating light species. Each is a band in `H_phys ∩ H_even ∩ ker(Ũ−1)^⊥` with a node at `K = 0` and an exact Clifford cone. The speeds are `sin θ₁/√3` and `sin θ₂/√3` cells per tick (Theorem C). The average of `ω_Σ` over its six cell images is cell invariant, half filled at every site, and carries the same two species (Corollary C1). The speed ratio is therefore a free constant of the law (Corollary C2). A zoom that matches these correlators within ZM1-OBS's band-limited budget keeps both speeds (Corollary C3). **Mechanism.** The two species live in gauge-invariant multiplicity spaces of the link-end stars. In the frozen state the matter hop annihilates every configuration, so it never touches them. Nothing in the law couples the two species. This is the "neutral disconnected sector" exception that the spatial-lattice note and the soft spin-2 note record for their supplied models; here it is realized exactly inside the live class. **A1 and A3, redone with the repository inputs** (§5), fail at named steps, and Theorem C witnesses each failure. **What any proof must use** (Corollary 6.1): a restriction of the appended class beyond LZ1 §1, GA1-P-5 and NN-a, or a property of the vacuum beyond D1, gauge invariance, cell invariance and half filling, or a narrower species notion. Three candidate specifications are four-tested; none passes all four tests, and none is adopted. **Open by name:** LZ1-i[O] on `L5-O[S_+]`, LZ1-i[odd m], LZ1-i[cube], LZ1-i[VC1], and the fermion clause LZ1-i[R-CS^str].

---

## 1. Prior work used

Every item below is ported with its path. "Extended" means that this file proves more than the source, from the source.

**Frozen parts in this folder.**
- `LZ1.md` §1: the update class (line 29), D1 states (line 34), bands, nodes and light species (line 36), D5 symmetries (line 38). Theorem 4.1 (line 95): "A D5 symmetry sends a band to a band, takes a node to a node, and preserves its directional speed set and Clifford speed." Theorem 4.2 and RC3 (lines 98, 203–215): block scaling and copy mixing in a free node representation. **Extended:** Theorem C is an interacting-law version of Theorem 4.2's witness, which line 104 says "does not exhibit two bands in an admissible interacting law".
- `TOE_ASSEMBLY.md` lines 229 (LZ1-SC), 235 (NN-a), 338 (LZ1(a)).
- `MT1.md` Theorem 1 (line 58): "Each `Q∈O` has a cell-periodic sign lift. It is unique up to a constant phase." Theorem 4 (line 80): the cell fibres `R_e(K), R_o(K)`. Theorem 7 (line 103): the free node, with "`v=\sin\varepsilon/\sqrt3`" and Clifford generators `G_j`. Line 93: "For sign lifts, a face quarter-turn has fourth power −1." Used in §3.4 and Theorem C.
- `LW1.md` Theorem A2 (line 209): "The action on sites is transitive; a site's stabilizer has three elements." Theorem B10 (line 322): the eigenvalue formula, at `μ=0` the identity `1−cos w = sin²ε(1−χ(K))` quoted in `MT1.md` Theorem 7's proof. Used in Theorem C.
- `LW1_5.md` §2: the law `L5-U` (line 94) and "a plaquette class and its constants are **OPEN law data**, GA1-P-5" (line 102). B1-U: the cell lifts, whose link part reads "On each link send every rishon mode at its `z`-end to the same flavour at the `gz`-end of the image link. This is a permutation of ten rishon modes." Used throughout §3.
- `GA1_5.md` class GA1-P-5 (line 50); Theorem 6.1 (line 148), whose GNS computation §3.7 follows; Lemma U (line 234) and Proposition C (line 262), the nearest-neighbour compilation; Lemma S1′ (line 276), whose covariance argument Lemma 3.6 follows. **Extended:** Theorem 6.3 there gives the first exact neutral propagating band in the class, a one-way glider with no Clifford cone. Theorem C gives two Clifford cones with free speeds.
- `ZM1_OBS.md` Theorem 1 (Haar tools), Theorem 3 (`𝔄^G⊆𝔄_even`, credited there to `RCS1.md` Theorem 4), Theorems 9 and 9′ (lines 104–135, branch-speed transfer), and line 139: "Neither theorem establishes a common speed across different species." Used in Theorem C and Corollary C3.

**Main, at `f5af11cd01`** (each is `unaudited` in its ledger shard, as the digest records).
- Exchange-matrix note, Statement (lines 43–83). **Extended** in Lemma A3.1 to drag that depends on scale.
- Attractor note, status line 24 ("conditional-support / open gate") and part (A), lines 106–124.
- B4 radiative-stability note, Theorem, lines 48–72. Its hypothesis is the failing step A1.1.
- Spatial-lattice note, lines 31, 41–42, 455, 471–472, 487–488. Used in A3.
- Curvature-closure note, line 16, and Result 1 of its full argument. Used in A4.
- Soft spin-2 note, lines 247 and 268–270. Used in A4 and in §0.1.
- Cross-sector front-speed note, lines 34–36, 79 and 94. Used in A1.

**PR #10125, at `586d7c81d0`.** #9913, lines 83, 93, 101–104, 108, 112 and 132; the consolidation's line 790. Used in A1 and A3.

**Prior work the digest did not name as LZ1-i inputs.** `GA1_5.md` Theorem 6.1, Lemma U, Proposition C and Lemma S1′: they make a link-only decoupled sector admissible and compilable. `MT1.md` Theorems 1, 7 and line 93: the free node's speed and the sign lifts. `LW1.md` A2 and B10. `LW1_5.md` B1-U. The digest names `MT1.md` only through C4 and does not name `GA1_5.md`.

**Failed attempts on file, not repeated.** Kill attempt K (`LZ1.md` line 159) searched frozen stars, pinned strings and reduced link models, and "found no exactly solvable propagating sector". The new step here is different. The matter is frozen by an end-number pattern on the links (§3.1), not by frozen stars; `LZ1.md` Theorem 3.3 is not used. The propagating species live in the gauge-invariant multiplicity of the link-end stars, and appended link-only layers move them. That such layers are admissible is the content of NN-a (`TOE_ASSEMBLY.md` line 237: "GA1-5's swap layers are admissible"), which postdates attempt K.

---

## 2. The law, the class and the notation

**The law.** `LW1_5.md` line 94: "**L5-U.** Each link carries `Λ^m C^{10}`, `1≤m≤9`, with five rishon modes at each end. Put `U_ℓ^{jk}=r^y_j r^{x†}_k`, `h^U_ℓ=Σ_{jk}c†_{y,j}U_ℓ^{jk}c_{x,k}+h.c.`, ..., `W_E=Π_ℓ e^{−iτ_E(p_{ℓ,x}−m/2)²}`." Here `ℓ=(x,y)` with `y=x+e_i`, and `x` is the source. The base tick is `U₀=W_E M_o M_e`, with `M_e=Π_{C∈𝒯_e}e^{−ia_eH_C}`, `M_o=Π_{C∈𝒯_o}e^{ia_oH_C}` and `H_C=3^{−1/2}Σ_{ℓ=(x,x+e_i)⊂C}η_i(x)h_ℓ` (`LW1_5.md` §2). The cube tilings are `𝒯_e` with vertex sets `2b+{0,1}³` and `𝒯_o` with vertex sets `2b+(1,1,1)+{0,1}³` (`GA1_5.md` §1).

**The class.** `LZ1.md` line 29: "A **gauge-invariant update of the same form** appends finitely many layers. Each layer is a family of finite-support gates that is closed under the even translations and has finitely many gates per cell. The gates of a layer commute pairwise, and each gate commutes with every local gauge transformation (`LW1.md` E1)." `GA1_5.md` line 50, GA1-P-5: "Each `W_s=∏_{X∈ℱ_s}g_X` has finite link supports; `ℱ_s` is cell-group invariant and locally finite, each `g_X` is a link-only gauge-invariant unitary, gates in the sublayer commute pairwise, and each cell lift carries `g_X` to `g_{gX}`." NN-a (`TOE_ASSEMBLY.md` line 235): "A nearest-neighbour layer is a locally finite product on pairwise disjoint edge triples. The update has a fixed finite number of such layers, independent of volume. Its automorphism `α` fixes every local gauge generator. It commutes with every cell lift `α_s` ... Gauge invariance and cell covariance are required of the complete update only." In this file, **an admissible interacting law in the live class** is `L5-U[m]` with its required matter cube gates, its electric layer, and appended layers that meet all three of these texts. The matter–link hop is present in every such law, so the law is interacting.

**Notation.** `𝒢=2Z³⋊O_{c₀}`, `c₀=(1/2,1/2,1/2)`, acts by `(β,Q)x=Q(x−c₀)+c₀+2β`. `α_g` is the lift of `g` from B1-U. Directions are `D={±e₁,±e₂,±e₃}`. The end of a link at a site `x` is labelled `(x,d)`, where `d∈D` points from `x` along the link. The link part of B1-U sends the end `(x,d)` to the end `(gx,Qd)`. The star `S_x` is the joint space of the six ends at `x`. Bloch conventions are those of `MT1.md` line 39: `x=2b+r` with `r∈{0,1}³`, and `|K,r⟩=Σ_b e^{iK·b}|2b+r⟩`.

---

## 3. The counterexample

Throughout §3, `m ∈ {2,4,6,8}`. Put `n_F := min(m,5)` and `n_E := m − n_F`, so `(n_F, n_E)` is `(2,0)`, `(4,0)`, `(5,1)` or `(5,3)`.

### 3.1 The frozen layered sector

**Definition Σ.** Call `x` an F-site if `x₃` is even and an E-site if `x₃` is odd. A link in direction `e₁` or `e₂` is *in-plane*; a link in direction `e₃` is *vertical*. Every in-plane link joins two sites of one kind. Every vertical link joins an F-site and an E-site. The sector `Σ` is the assignment: `N_x = 5` at F-sites and `N_x = 0` at E-sites; end number `m/2` at both ends of every in-plane link; end number `n_F` at the F-end and `n_E` at the E-end of every vertical link. For a finite set `R` of sites and links, `P^Σ_R` projects onto the span of the occupation configurations that agree with `Σ` on `R`.

**Lemma 3.1 (frozen matter).** (a) Let `R` contain the sites and links of a cube `C` of either tiling. Then `H_C P^Σ_R = 0`, so `e^{−iaH_C}P^Σ_R = P^Σ_R` for every real `a`. (b) On `Ran P^Σ_R` each factor of `W_E` is a scalar: `1` on in-plane links and `e^{−iτ_E s}` on vertical links, with `s := (n_F − m/2)² = (n_E − m/2)²`.

*Proof.* (a) For `ℓ=(x,y)`, `h_ℓ` is the sum of `T = Σ_{jk} c†_{y,j} r^y_j r^{x†}_k c_{x,k}` and `T*`. A monomial of `T` is nonzero on an occupation basis vector only if `x` carries matter, `y` is not full, the `y`-end carries a rishon and the `x`-end has a hole. `T*` needs the same with `x` and `y` exchanged. On an in-plane link between two F-sites, the target of either term is full, so both terms vanish. Between two E-sites, the source of either term is empty. On a vertical link with F-end `f` and E-end `e`, the term that moves matter out of `e` vanishes, because `e` is empty. The term that moves matter from `f` to `e` needs a rishon at the `e`-end and a hole at the `f`-end. If `m ≤ 4` the `e`-end is empty (`n_E = 0`). If `m ≥ 6` the `f`-end is full (`n_F = 5`). So every monomial of every `h_ℓ` with `ℓ ⊂ C` annihilates every configuration of `Σ`, whatever its flavours. Hence `H_C P^Σ_R = 0`, and the exponential series gives the rest. (b) The source of a vertical link is its F-end or its E-end, and `(n_F − m/2)² = (m/2 − n_E)²` because `n_F + n_E = m`. In-plane ends carry `m/2`. □

### 3.2 Stars and the label space

**Lemma 3.2.** (a) Fix a link `(x,y)` and end numbers `(p,q)`. The map `e_A∧e_B ↦ e_A⊗e_B` (`A` a `p`-set of `x`-end flavours, `B` a `q`-set of `y`-end flavours, `x`-modes first) is a unitary from the `(p,q)` subspace of `Λ^mC^{10}` onto `Λ^pC⁵⊗Λ^qC⁵`. It carries every operator built from `x`-end modes that conserves the `x`-end number to `X⊗1`, and likewise at the `y`-end. Hence on `Ran P^Σ` the link space is the tensor product of the stars `S_x`, and the local gauge transformation at `x` acts only on `S_x` and on the matter at `x`.
(b) At every site the four in-plane ends give `W^{⊗4}` with `W := Λ^{m/2}C⁵`. The group `S(D_∥)` of permutations of `D_∥ = {±e₁,±e₂}` permutes the four factors and commutes with the gauge action.
(c) Let `B := {b : D_∥ → C, Σ_d b(d) = 0}`, with `S(D_∥)` permuting arguments. `B` is irreducible, of dimension 3.
(d) Let `A_x := Hom_{S(D_∥)}(B, W^{⊗4})` with `⟨f,f'⟩1_B := f*f'`. Then `ev_x : B⊗A_x → W^{⊗4}`, `b⊗f ↦ f(b)`, is an isometry. It intertwines `σ⊗1` with the permutation action of `σ`, and `1⊗(Γ∘·)` with the gauge action `Γ`. `A_x ≠ 0`.
(e) For `X ∈ End(B)` let `X̂_x` act on the in-plane ends at `x` by `ev_x(X⊗1)ev_x*`, by the identity on the vertical ends at `x`, and by `0` unless all six ends at `x` carry `Σ`'s end numbers. Then `X̂_x` is local, link-only and gauge invariant; `X ↦ X̂_x` is multiplicative and `*`-preserving; matter parity fixes `X̂_x`.

*Proof.* (a) The map is a bijection of orthonormal bases. On a fixed number sector, the `x`-end operators that conserve the `x`-end number are spanned by products of the bilinears `r†_{x,a}r_{x,b}`. The bilinears act by the `u(5)` action, which is irreducible on `Λ^pC⁵` (`LW1_5.md` line 118, the proof of C2: "For \(U(5)\), each \(\Lambda^k\mathbb C^5\) is irreducible"), so by Burnside's theorem they generate `End(Λ^pC⁵)`. Each bilinear is even, so it commutes with the `y`-end creators and acts as `X⊗1`. The gauge generator at `x` is built from the matter at `x` and from bilinears at the ends at `x`: `LW1_5.md` line 94, "`𝒢_x^T=c_x^†Tc_x+Σ_{ℓ∋x}r_{ℓ,x}^†Tr_{ℓ,x}`". (b) The gauge transformation acts on `W^{⊗4}` as `u^{⊗4}`, `u ∈ U(5)` acting on `W`; tensor powers commute with factor permutations. (c) `C^{D_∥} = B ⊕ C(1,1,1,1)` as `S(D_∥)`-modules, so `χ_B(σ) = fix(σ) − 1`. On the classes of `S₄` with sizes 1, 6, 3, 8, 6 (identity, transpositions, double transpositions, 3-cycles, 4-cycles), `χ_B` takes the values 3, 1, −1, 0, −1. So `(1/24)Σ_σ|χ_B(σ)|² = (9+6+3+0+6)/24 = 1`. For a unitary representation `V` of a finite group `G`, `(1/|G|)Σ_g|χ_V(g)|²` is the trace of the averaging projection on `End(V) ≅ V⊗V̄`, that is, `dim End_G(V)`. A proper invariant subspace would give a non-scalar invariant projection. So `End_G(B) = C1` and `B` is irreducible. (d) For `f, f' ∈ A_x`, `f*f'` commutes with `S(D_∥)` on `B`, so it is a scalar by Schur's lemma. `f*f = 0` forces `f = 0`, so `⟨·,·⟩` is an inner product. For an orthonormal basis `f_k` of `A_x`, `⟨ev(b⊗f_k), ev(b'⊗f_l)⟩ = ⟨b, f_k*f_lb'⟩ = ⟨b,b'⟩δ_{kl}`, so `ev_x` is isometric. Equivariance: `f(σb) = σf(b)`; and `Γ∘f ∈ A_x` because `Γ` commutes with `S(D_∥)`. Nonzero: take orthonormal `w₀, w₁ ∈ W` (`dim W ≥ 5`) and let `w_d` be the product vector with `w₁` in factor `d` and `w₀` elsewhere; `f₀(b) := Σ_d b(d)w_d` is injective and equivariant. (e) Locality and link-only: by construction. On the image of `ev_x`, `Γ` acts as `1⊗(Γ∘·)` and `X̂_x` as `X⊗1`; `Γ` preserves this image and its complement, where `X̂_x` is `0`; `Γ` preserves end numbers. Gauge transformations at other sites act on other ends, by (a). Multiplicativity holds because `ev_x*ev_x = 1`. Matter parity acts trivially on link operators. □

The image of `ev_x` is the `B`-isotypic part of `W^{⊗4}`; nothing below needs this.

### 3.3 The stabilizer of Σ and the lift on labels

**Lemma 3.3.** (a) `𝒢_Σ := {g ∈ 𝒢 : gΣ = Σ}` equals `2Z³ ⋊ ⟨r⟩`, where `r(x) = (1 − x₂, x₁, x₃)` is the quarter turn about the vertical axis through `c₀`. (b) `𝒢_Σ` acts freely on sites. Its two orbits are the F-sites and the E-sites, with representatives `x_F = 0` and `x_E = e₃`. (c) Let `g₁ = 1, g₂, …, g₆` represent the cosets of `𝒢/𝒢_Σ` and put `Σ_k := g_kΣ`. These are the six sectors of the same form with vertical axis `e₁`, `e₂` or `e₃` and full planes even or odd. At every site, two different `Σ_k` prescribe different end numbers on some end at that site. (d) For `g = (β,Q) ∈ 𝒢_Σ` and `X ∈ End(B)`, `α_g(X̂_x) = (Λ(Q)XΛ(Q)^{−1})^_{gx}`, where `Λ(Q)` is the permutation of `D_∥` by `Q`, acting on `B`. `Λ` is a homomorphism.

*Proof.* (a) Write `g = (β,Q)`. If `Qe₃ = ±e_i` with `i ≠ 3`, then `g` sends vertical links to in-plane links, and the end numbers `m/2` and `n_F, n_E` differ for every even `m`. If `Qe₃ = −e₃`, then `x₃ ↦ 1 − x₃ + 2β₃` exchanges F-sites and E-sites, and `N_x = 5` differs from `0`. So `Qe₃ = e₃`: `Q` is a power of the linear part of `r`. Every such `g`, and every even translation, preserves `Σ`. (b) `r^k(0)` is `(0,0,0)`, `(1,0,0)`, `(1,1,0)`, `(0,1,0)` for `k = 0,1,2,3`; only `k = 0` lies in `2Z³`, so `0` has trivial stabilizer. The same computation applies to `e₃`. The orbit of `0` is the set of all sites with `x₃` even, and the orbit of `e₃` is the set of all sites with `x₃` odd. (c) `|O/C₄| = 6`; `g_k` sends the vertical axis to `Q_ke₃` and the full planes to the corresponding parity. At one site, two sectors with different vertical axes give `m/2` on one sector and `n_F` or `n_E` on the other, for some direction. Two sectors with the same axis and opposite full parity give `n_F` against `n_E` on the vertical ends. Both differ for every even `m`. (d) By B1-U, `α_g` acts on the ends by the second-quantized mode permutation `(x,d) ↦ (gx,Qd)`. On `Ran P^Σ`, in the product form of Lemma 3.2(a), it maps `W^{⊗4}` at `x` to `W^{⊗4}` at `gx` as `P_Q∘J` times a sign from reordering fermionic modes. Here `J` identifies the factor with label `d` at `x` with the factor with label `d` at `gx`, and `P_Q` then moves factor `d` to factor `Qd`. The adjoint action removes the sign. `P_Q ev_x(b⊗f) = ev_x(Λ(Q)b⊗f)` by equivariance of `f`, and `J` carries `ev_x` to `ev_{gx}`. Vertical ends go to vertical ends because `Qe₃ = e₃`, and `X̂` is the identity there. □

**Frames.** Choose an orthonormal basis `|0⟩, |1⟩, |2⟩` of `B`. For `x = g x_a` with `g ∈ 𝒢_Σ` (unique by Lemma 3.3(b)), put `|j⟩_x := Λ(Q_g)|j⟩` and `E^x_{jk} := (|j⟩_x⟨k|_x)^_x`. For `h ∈ 𝒢_Σ`, `|j⟩_{hx} = Λ(Q_{hg})|j⟩ = Λ(Q_h)|j⟩_x`, so Lemma 3.3(d) gives

  `α_h(E^x_{jk}) = E^{hx}_{jk}` for every `h ∈ 𝒢_Σ`. (3.1)

Even translations have `Λ = 1`, so the frames are `2Z³`-periodic.

### 3.4 The one-body walk and a genuine lift on 𝒢_Σ

Let `R_C := 3^{−1/2}Σ_{ℓ=(x,x+e_i)⊂C}η_i(x)(|x+e_i⟩⟨x| + |x⟩⟨x+e_i|)` on `ℓ²(Z³)`. It is `H_C` with the link operators replaced by `δ^{jk}` and one flavour kept (`LW1_5.md` inferred definition 4; `MT1.md` line 37). Put `R_T := Σ_{C∈𝒯_T}R_C` and `V_θ := e^{iθR_o}e^{−iθR_e}`. Ported from `MT1.md`. Theorem 1 supplies, for every `Q ∈ O`, a cell-periodic sign lift `ρ(Q)`; line 46 reads "A lift is a site-permuting unitary with site phases, ... which commutes with both free half-step generators". It is unique up to a constant phase, and cell periodicity gives `ρ(Q)τ_βρ(Q)^{−1} = τ_{Qβ}`. Theorem 7, for an angle in the window `(0, π/2)` at `μ = 0`: "near `K=0`, `V(K)=exp(-ih(K))` with `h(K)=vΣ_jK_jG_j+O(|K|²)`, `v=sinε/√3`"; "The `G_j` are Clifford generators"; "The only `V=I` node is `K=0`." Its proof quotes `LW1.md` B10: "`1-cos w=sin²ε(1-χ(K))`". Here `χ(K) = (1/3)Σ_j cos K_j`, from B10's identity `R_eR_o + R_oR_e = (1/3)Σ_i(T_{2e_i}+T_{−2e_i})`. [check: §8 confirms this eigenvalue formula on an `8³` torus to `3×10⁻¹⁵`.]

**Lemma 3.4.** (a) For `g = (β,Q) ∈ 𝒢` put `ρ(g) := τ_βρ(Q)`. For every cube `C`, `ρ(g)R_Cρ(g)^{−1} = R_{gC}`. (b) `ρ(r)⁴ = λ1` with `λ ∈ {+1,−1}`. Fix a fourth root `λ^{1/4}` and put `ρ̃ := λ^{−1/4}ρ(r)`. Then `ρ'(β,r^k) := τ_βρ̃^k` is a unitary representation of `𝒢_Σ`, monomial in sites: `ρ'(g)|x⟩ = c_g(x)|gx⟩` with `|c_g(x)| = 1`. [check: `λ = −1`, as `MT1.md` line 93 states.]

*Proof.* (a) `ρ(g)` commutes with `R_e` and `R_o`: the sign lift does by Theorem 1, and even translations preserve the tilings and the signs `η_i`. Each `R_T` is block diagonal over the cubes of `T`. Conjugation by a site permutation with phases carries the block of `C` to the block of `gC`, and `g` permutes the cubes of each tiling (`LW1.md` A2, quoted in `GA1_5.md` Lemma S1′(a)). Comparing blocks gives the claim. (b) `ρ(r)⁴` is a sign lift of the identity, so Theorem 1's uniqueness makes it a constant phase; it is real, so it is `±1`. Then `ρ̃⁴ = 1` and `ρ̃τ_βρ̃^{−1} = τ_{rβ}`. The product `(β,r^k)(β',r^{k'}) = (β + r^kβ', r^{k+k'})` maps to `τ_βρ̃^kτ_{β'}ρ̃^{k'} = τ_{β+r^kβ'}ρ̃^{k+k'}`, and `ρ̃⁴ = 1` makes the exponent well defined mod 4. □

**Lemma 3.5 (induction along a free action).** Let `π` be the permutation representation of `𝒢_Σ` on `ℓ²(Z³)`, `π(g)|x⟩ = |gx⟩`. There is a `2Z³`-periodic diagonal unitary `Ψ = diag(ψ(x))` with `Ψπ(g) = ρ'(g)Ψ` for all `g ∈ 𝒢_Σ`.

*Proof.* Put `ψ(x_a) := 1` and `ψ(gx_a) := c_g(x_a)`; this is well defined by freeness. For `h ∈ 𝒢_Σ`, `Ψπ(h)|gx_a⟩ = c_{hg}(x_a)|hgx_a⟩` and `ρ'(h)Ψ|gx_a⟩ = c_g(x_a)c_h(gx_a)|hgx_a⟩`. They agree, because `ρ'(hg) = ρ'(h)ρ'(g)` gives `c_{hg}(x_a) = c_h(gx_a)c_g(x_a)`. Periodicity: `ρ'(τ_β) = τ_β` has `c ≡ 1`. □

Put `ĥ_C := Ψ*R_CΨ`, `ĥ_T := Ψ*R_TΨ` and `W_θ := e^{iθĥ_o}e^{−iθĥ_e} = Ψ*V_θΨ`. Lemmas 3.4(a) and 3.5 give `π(g)ĥ_Cπ(g)^{−1} = ĥ_{gC}` for `g ∈ 𝒢_Σ`. `Ψ` is periodic, so its Bloch fibre is a constant diagonal unitary `Ψ₀` on `C⁸`, and the fibre of `W_θ` at `K` is `Ψ₀*V_θ(K)Ψ₀`.

### 3.5 The appended layers

**Definition `L(θ₁,θ₂)`.** Let `θ₁, θ₂ ∈ (0, π/2)`, `s_e := −1` and `s_o := +1`. For a cube `C` let `B_C := ⊗_{x∈C}B`, written in the frames of §3.3 at the corners of `C`. Put `|vac_C⟩ := ⊗_{x∈C}|0⟩_x` and, for `j ∈ {1,2}` and `x ∈ C`, `|j;x⟩ := |j⟩_x ⊗ ⊗_{y∈C, y≠x}|0⟩_y`. Let `𝒱^j_C := span{|j;x⟩ : x ∈ C}`, a copy of `ℓ²(C)`. Define `g_C ∈ U(B_C)` by `g_C|vac_C⟩ = |vac_C⟩`, by `g_C = exp(is_Tθ_jĥ_C)` on `𝒱^j_C` (`ĥ_C` acting on the corner index), and by `g_C = 1` on the orthogonal complement of `C|vac_C⟩ ⊕ 𝒱¹_C ⊕ 𝒱²_C`.

Let `L′_C` be the 36 links with an end at a corner of `C`, and `Π_C` the projection onto the span of the configurations in which every end at a corner of `C` carries `Σ`'s end number. On `Ran Π_C` the in-plane ends at the corners form `⊗_{x∈C}W^{⊗4}`. Put

  `G^Σ_C := [ (⊗_xev_x)(g_C⊗1)(⊗_xev_x)* + (1 − (⊗_xev_x)(⊗_xev_x)*) ] ⊗ 1_vertical` on `Ran Π_C`, and `G^Σ_C := 0` on `Ran Π_C^⊥`.

For `k = 1,…,6` put `Π^{(k)}_C := α_{g_k}(Π_{g_k^{−1}C})` and `G^{(k)}_C := α_{g_k}(G^Σ_{g_k^{−1}C})`. Finally

  `G_C := Σ_k G^{(k)}_C + (1 − Σ_k Π^{(k)}_C)`, `L_T := ∏_{C∈𝒯_T}G_C`, `U(θ₁,θ₂) := L_oL_eU₀`.

**Lemma 3.6 (admissibility).** (a) `G_C` is well defined, unitary, link-only and gauge invariant, and it acts only on the registers of `L′_C`. (b) For distinct cubes `C, C′` of one tiling, `[G_C, G_{C′}] = 0`. (c) `α_h(G_C) = G_{hC}` for every `h ∈ 𝒢`. Hence `α_h(L_T) = L_T`, and `U(θ₁,θ₂)` is covariant under every cell lift. (d) `L_oL_e` is a member of GA1-P-5, and `U(θ₁,θ₂)` is a gauge-invariant update of LZ1 §1's form. (e) Under NN-a, `L_oL_e` is a composition of finitely many nearest-neighbour layers, each a product of pairwise disjoint edge-triple gates and invariant under `4Z³`. So `U(θ₁,θ₂)` is admissible in the sense of §2.

*Proof.* (a) *Well defined.* Replace `g_k` by `g_kh` with `h ∈ 𝒢_Σ`, and put `C₁ := g_k^{−1}C`. Lifts compose exactly on link operators, because they are second-quantized mode permutations and second quantization is a homomorphism. So `α_{g_kh}(G^Σ_{h^{−1}C₁}) = α_{g_k}(α_h(G^Σ_{h^{−1}C₁}))`. And `α_h(G^Σ_{h^{−1}C₁}) = G^Σ_{C₁}`, for four reasons: `α_h` preserves `Σ` and maps `Π_{h^{−1}C₁}` to `Π_{C₁}`; it maps the `ev`-images at the corners of `h^{−1}C₁` to those at the corners of `C₁`, acting by `Λ(Q_h)` on the `B`-factors (Lemma 3.3(d)); in the frames it maps `|vac⟩` to `|vac⟩` and `|j;x⟩` to `|j;hx⟩`, by (3.1); and `π(h)ĥ_{h^{−1}C₁}π(h)^{−1} = ĥ_{C₁}` (§3.4). The same facts make `Π^{(k)}_C` well defined. *Unitary.* The `Π^{(k)}_C` are mutually orthogonal, because two different sectors prescribe different end numbers at some end at each corner (Lemma 3.3(c)). Each `G^{(k)}_C` is unitary on `Ran Π^{(k)}_C`, because `g_C` is unitary and `ev` is isometric (Lemma 3.2(d)). *Support and link-only:* by construction; the projections are functions of the end numbers at the corners of `C`. *Gauge invariance:* end numbers are gauge invariant. On `Ran Π^{(k)}_C` the gauge transformations act on the `A`-factors and on the vertical ends, where `G_C` is the identity, and they preserve each `ev`-image and its complement (Lemma 3.2(d),(e)). (b) Distinct cubes of one tiling have disjoint corner sets. `G_C` acts only on the ends at the corners of `C` and conserves every end number. Operators on different ends that conserve end numbers commute, by Lemma 3.2(a). (c) For `h ∈ 𝒢`, `α_h(G^{(k)}_C) = α_{hg_k}(G^Σ_{g_k^{−1}C})`. Write `hg_k = g_{k′}h′` with `h′ ∈ 𝒢_Σ`; by well-definedness this is `G^{(k′)}_{hC}`. The same holds for the projections, and `h` permutes the six cosets, so `α_h(G_C) = G_{hC}`. `𝒢` permutes the cubes of each tiling (`LW1.md` A2), so `α_h(L_T) = L_T`. The base tick is covariant by B1-U: "It follows that the tick automorphism commutes with each lift." (d) GA1-P-5's conditions, quoted in §2: the supports `L′_C` are finite; the family `{L′_C : C ∈ 𝒯_T}` is cell-group invariant and locally finite; each `G_C` is a link-only gauge-invariant unitary, by (a); the gates of a sublayer commute, by (b); each cell lift carries `G_C` to `G_{gC}`, by (c). LZ1 §1's conditions follow: finite support, closure under even translations, finitely many gates per cell, pairwise commuting gates, and gauge invariance of each gate. (e) `L′_C` is connected, because each of its links has an end at a corner of `C` and the twelve edges of `C` join the corners. Lemma U (`GA1_5.md` line 234): "for every unitary `G` on `⊗_{ℓ∈L′}H_ℓ`, the operator `G⊗1` (identity on all matter and all other links) is a finite product of unitaries, each in some `𝒢_{w,ℓ}` with `ℓ∈L′`, `w∈S′∩ℓ`". Here `S′` is the corner set of `C`: a site outside `C` is adjacent to at most one corner. Each element of `𝒢_{w,ℓ} = 𝒜_w^+⊗B(H_ℓ)` is an even gate on one edge triple, a nearest-neighbour gate under NN-a. Choose the word for `C + 2β` as the translate of the word for `C`. Split each tiling into the eight classes of cubes whose index `b` is fixed mod 2. Corners of distinct cubes of one class are at sup-distance at least 3, so their sets `L′` and their corner sets are disjoint. Hence the `i`-th gates of the words of one class form one layer of pairwise disjoint edge triples, invariant under `4Z³`. The gates of `L_T` commute, so `L_T` is the product of its eight class products. This is the argument of Proposition C (`GA1_5.md` line 266), applied to `G_C`. The intermediate gates are not gauge invariant; NN-a allows this: "Gauge invariance and cell covariance are required of the complete update only." □

### 3.6 The state

**Definition `ω_Σ`.** `ω_Σ` is the product state whose factor at a site `x` is: `|full⟩⟨full|` on the matter at an F-site and `|empty⟩⟨empty|` at an E-site; `ev_x(|0⟩_x⟨0|_x ⊗ 1_{A_x}/dim A_x)ev_x*` on the in-plane ends at `x`; and the normalized identity on each vertical end space at `x`. By Lemma 3.2(a) these factors give, on every finite `R`, a density supported in `Ran P^Σ_R`, consistent under partial trace. So they define a state of the quasi-local algebra.

**Lemma 3.7.** `ω_Σ` is a D1 state for `U(θ₁,θ₂)`. It is stationary, invariant under `2Z³`, and invariant under every local gauge transformation, hence under each `Ad c_z`. `ω_Σ(N_x)` is `5` at F-sites and `0` at E-sites; its average over a cell is `5/2`.

*Proof.* *Gauge invariance.* The matter factor spans a one-dimensional gauge-invariant line. On the in-plane ends the gauge acts on `A_x` (Lemma 3.2(d)) and fixes `1_{A_x}`. The normalized identity is invariant. A gauge transformation at `x` acts only on the factor at `x` (Lemma 3.2(a)). `c_z = exp(iπQ_z)` is a local gauge transformation (`LZ1.md` line 32). *Translations.* The frames are `2Z³`-periodic. *Stationarity.* For local `A`, `α(A) = V*AV`, where `V` is the finite product of the gates of `U(θ₁,θ₂)` met by the backward cone of the support of `A` (`LW1.md` E1). Let `R` contain the supports of these gates, and let `P_R` be the support projection of the density `ρ_R` of `ω_Σ` on `R`. On `Ran P_R` every site carries `|0⟩` in its `B`-factor. There the matter gates act as the identity (Lemma 3.1(a)), each `W_E` factor as a scalar (Lemma 3.1(b)), and each `G_C` as the identity, because `g_C|vac_C⟩ = |vac_C⟩` and `G_C` is the identity on the `A`-factors and the vertical ends. So `VP_R = cP_R` and `P_RV* = c̄P_R` with `|c| = 1`. Then `Vρ_RV* = ρ_R`, and `ω_Σ(α(A)) = tr(ρ_RV*AV) = tr(Vρ_RV*A) = ω_Σ(A)`. *Filling.* Read it from the matter factors; a cell has four F-sites and four E-sites. □

### 3.7 The two species

For `j ∈ {1,2}` and a site `x` put `u^j_x := π(E^x_{j0})Ω`.

**Lemma 3.8.** (a) `⟨u^j_x, u^k_y⟩ = δ_{jk}δ_{xy}`. (b) `Ũu^j_x = Σ_y (W_{θ_j}*)_{yx}u^j_y`, a finite sum. (c) `u^j_x ∈ H_phys ∩ H_even`, and `T_βu^j_x = u^j_{x+2β}`.

*Proof.* (a) `⟨u^j_x,u^k_y⟩ = ω_Σ(E^x_{0j}E^y_{k0})`. For `x ≠ y` the factors act on different stars and the state is a product, so the value is `ω_Σ(E^x_{0j})ω_Σ(E^y_{k0}) = ⟨0|j⟩⟨k|0⟩ = 0`. For `x = y`, `E^x_{0j}E^x_{k0} = δ_{jk}E^x_{00}` by Lemma 3.2(e), and `ω_Σ(E^x_{00}) = 1`. (b) For local `Y, Y′` supported in a finite `R`, `‖π(Y−Y′)Ω‖² = tr(ρ_R(Y−Y′)*(Y−Y′))`, which vanishes if and only if `(Y−Y′)P_R = 0`. Take `A = E^x_{j0}` and `V, R, c` as in the proof of Lemma 3.7. Then `α(A)P_R = V*AVP_R = cV*AP_R`. `AP_R` maps `Ran P_R` into the subspace `𝒦^j_R` on which exactly one site `y` carries `|j⟩_y` in its `B`-factor, every other site carries `|0⟩`, and all other factors are as in `Ran P_R`. `𝒦^j_R` lies in `Ran P^Σ_R`. On it the matter gates act as the identity and the `W_E` factors as the same scalar `c`. A gate `G_C` with no excited corner acts as the identity; a gate with the excited corner `y ∈ C` acts by `exp(is_Tθ_jĥ_C)` on the corner index and leaves the `A`-factors alone. So `V` acts on `𝒦^j_R` as `c` times `W_{θ_j}` on the site of the excitation, and `V*` as `c̄W_{θ_j}*`. Hence `α(A)P_R = Σ_y(W_{θ_j}*)_{yx}E^y_{j0}P_R`, a finite sum since `W_θ` has finite range. (c) `E^x_{j0} ∈ 𝔄^G` by Lemma 3.2(e), so `u^j_x ∈ H_phys`; matter parity fixes `E^x_{j0}` and `Ω`, so `u^j_x` is even. `α_{τ_β}(E^x_{j0}) = E^{x+2β}_{j0}` by (3.1), and `T_β` implements `α_{τ_β}` and fixes `Ω`. □

**Theorem C (two light species with different Clifford speeds).** Let `m ∈ {2,4,6,8}`, let `(ε, μ, τ_E)` be allowed for `L5-U[m]`, and let `θ₁, θ₂ ∈ (0, π/2)`. In the GNS representation of `ω_Σ` for the update `U(θ₁,θ₂)`, for `j = 1, 2` there is a band `(8, F_j, V_j)` with

  `V_j(K) = Ψ₀* V_{θ_j}(−K)* Ψ₀`,

whose image lies in `H_phys ∩ H_even ∩ ker(Ũ−1)^⊥`. Each band has a node at `K = 0` with leading generator `N^{(j)}_i = v_jΨ₀*G_iΨ₀`, so that `{N^{(j)}_i, N^{(j)}_k} = 2v_j²δ_{ik}` with `v_j = sin θ_j/√3`. The two images are orthogonal. So both bands are propagating light species in the sense of `LZ1.md` line 36, LZ1-SC's dispersion clause applies to both, and their Clifford cones have speeds `v₁` and `v₂`. If `θ₁ ≠ θ₂`, then `v₁ ≠ v₂`.

*Proof.* For `f ∈ L²(T³;C⁸)` with components `f_s(K) = Σ_b f̂_s(b)e^{iK·b}`, put `F_jf := Σ_{b,s}f̂_s(b)u^j_{2b+s}`. Lemma 3.8(a) makes `F_j` an isometry. Lemma 3.8(c) gives `T_βF_jf = Σ_{b,s}f̂_s(b)u^j_{2(b+β)+s} = F_j(e^{iK·β}f)`, which is `T_βF = FM_β`. By Lemma 3.8(b), `Ũ` acts on the coefficients by the translation-invariant matrix of `W_{θ_j}*`. In this convention its symbol is the Bloch fibre of `W_{θ_j}*` at `−K`, namely `Ψ₀*V_{θ_j}(−K)*Ψ₀`, so `ŨF_j = F_jM_{V_j}`. `V_j` is a trigonometric polynomial, so it is continuous and smooth. *Node.* `V_{θ_j}(0) = 1`, so `V_j(0) = 1`. Near `0`, `V_{θ_j}(−K)* = exp(ih(−K))` with `h(K) = v_jΣ_iK_iG_i + O(|K|²)`. So `h_j(K) := i log V_j(K) = −Ψ₀*h(−K)Ψ₀ = v_jΣ_iK_iΨ₀*G_iΨ₀ + O(|K|²)`, and `N^{(j)}_i = ∂_ih_j(0) = v_jΨ₀*G_iΨ₀`. Unitary conjugation keeps the Clifford relations. *Orthogonality to `ker(Ũ−1)`.* The image `H_j` of `F_j` reduces `Ũ`, since `Ũ*F_j = F_jM_{V_j*}`. If `w` is `Ũ`-fixed, its components in `H_j` and in `H_j^⊥` are `Ũ`-fixed. A fixed vector `F_jf` in `H_j` has `V_j(K)f(K) = f(K)` for almost every `K`. By B10 at `μ = 0`, an eigenvalue of `V_{θ_j}(K)` equals `1` only if `1 − cos w = sin²θ_j(1 − χ(K)) = 0`, that is `χ(K) = 1`, that is `K ∈ 2πZ³`, because `sin θ_j ≠ 0`; `χ` is even, so the same holds at `−K`. So `f = 0` almost everywhere, and `H_j ⊥ ker(Ũ−1)`. *Rest.* The images are orthogonal by Lemma 3.8(a). Each band has a node and lies in `H_even`, so it is a proposed light species; it propagates, since `N^{(j)}_i ≠ 0`. `sin` is injective on `(0, π/2)`. □

**What Theorem C shows.** In one admissible interacting law, and in one D1 state that is half filled on average over a cell, two propagating light species carry exact isotropic Clifford cones with different speeds. Each speed is set by its own appended angle. Both species are neutral. Each `E^x_{j0}` commutes with every end number, so the bands are not flux-carrying in the sense of GA1-5's proposed R-Φ (`GA1_5.md` line 59: "A band in `H_phys` is flux-carrying if its image is orthogonal to `closure π(𝒩)Ω`"). They are not gauge bosons, fermions or gravitons. They are light species in `LZ1.md`'s sense and in T3's "All light species".

---

## 4. Corollaries

**Corollary C1 (a cell-invariant, half-filled state).** Put `ω_k := ω_Σ ∘ α_{g_k}^{−1}` and `ω̄ := (1/6)Σ_kω_k`. Then `ω̄` is a D1 state for `U(θ₁,θ₂)`, invariant under every cell lift, with `ω̄(N_x) = 5/2` at every site. Its GNS space carries two bands with the fibres `V₁, V₂` of Theorem C.

*Proof.* Each `α_{g_k}` commutes with the tick automorphism (Lemma 3.6(c) and B1-U), conjugates even translations to even translations, and maps local gauge transformations to local gauge transformations (B1-U: "the lifts send `𝒢_x^T,N_x,Q_x,p_{ℓ,z}` to their geometric counterparts"). So each `ω_k` is a D1 state. `𝒢` permutes the cosets and hence the `ω_k`, so `ω̄` is invariant under every lift. For each of the three axes, exactly one of its two parity sectors makes a given site full, so `ω̄(N_x) = (3·5 + 3·0)/6 = 5/2`. *Bands.* `E^x_{j0}` contains the projection onto `Σ`'s end numbers at `x` (Lemma 3.2(e)), and every `Σ_k` with `k ≠ 1` prescribes different end numbers at `x` (Lemma 3.3(c)). So `E^x_{j0}P^{(k)}_R = 0` for `k ≠ 1`, where `P^{(k)}_R` is the support projection of `ω_k` on `R`. The argument of Lemma 3.7 gives `VP^{(k)}_R = c_kP^{(k)}_R`, so also `α(E^x_{j0})P^{(k)}_R = 0`. Hence, for every local `Z` built from these operators, `ω̄(Z*Z) = (1/6)ω_Σ(Z*Z)`. The vectors `ū^j_x := √6 π̄(E^x_{j0})Ω̄` therefore satisfy Lemma 3.8(a)–(c), and the proof of Theorem C applies word for word. □

`ω̄` is site-transitive and half filled at every site. `LZ1.md` Theorem 3.2's last clause does not apply to it, because its Gauss-charge correlations do not cluster: `ω̄` is a mixture of six states with different sharp charge patterns.

**Corollary C2 (the speed ratio is a free constant).** Fix `m, ε, μ, τ_E`. The laws `U(θ₁,θ₂)`, `θ₁, θ₂ ∈ (0, π/2)`, all meet every condition of §2 and are covariant under the same cell lifts. In each, Theorem C gives two light species with Clifford speeds `sin θ₁/√3` and `sin θ₂/√3`. Their ratio `sin θ₂/sin θ₁` takes every value in `(0, ∞)`. If `θ₁ ≠ θ₂`, no D5 symmetry of the GNS representation maps the image of one band onto the image of the other.

*Proof.* The first two sentences restate Lemma 3.6 and Theorem C. `sin` maps `(0, π/2)` onto `(0, 1)`. For the last sentence: near the node, the restriction of `Ũ` to the image of band `j` has spectral values `e^{±iv_j|K|+o(|K|)}` (Theorem C), so the Clifford speed is a property of the image. `LZ1.md` Theorem 4.1 (line 95): "A D5 symmetry sends a band to a band, takes a node to a node, and preserves its directional speed set and Clifford speed." A D5 symmetry carrying one image onto the other would force `v₁ = v₂`. □

**Corollary C3 (a zoom keeps both speeds).** Fix `j`. The composite list `u^j_s`, `s ∈ {0,1}³`, meets the fine-side hypotheses of `ZM1_OBS.md` Theorem 9 (line 104). Indeed `C(β,0) = δ_{β,0}1₈`, so `Σ_β‖C(β,0)‖ = 1`. For `0 < |θ| < κ₀` with `κ₀` small, `c(θ,t) = V_j(θ)^t = W_+(θ)e^{−itw(θ)} + W_−(θ)e^{itw(θ)}`, where `W_±` are the spectral projections of `V_j(θ)`; they have norm 1, the phases `±w(θ)` are continuous with limit `0`, and the gap `2w(θ)` exceeds `v_j|θ|` near `0`. So suppose a coarse law and state reproduce the band-limited forms of these composites within Theorem 9's absolute budget, or Theorem 9′'s relative budget, with `p > 0`, and suppose their branch form meets the same hypotheses. Then each coarse branch lies within `O(|θ|^{p+1})` of `±w`, and the coarse directional speeds are `v_j`. No zoom in that comparison class brings `v₁` and `v₂` together.

*Proof.* Theorem 9's conclusion: "each branch on either side has a branch on the other within `O(|θ|^{p+1})` modulo `2π`. Along rays, existing branch-speed sets coincide." The fine-side facts are: orthonormality (Lemma 3.8(a)); the spectral decomposition of the unitary `V_j(θ)`, whose eigenvalues are `e^{±iw(θ)}`, each fourfold (`MT1.md` Theorem 7, `LW1.md` B10); continuity of `W_±` for small `θ ≠ 0`, since the two eigenvalues are separated; and `w(θ) = v_j|θ| + O(|θ|²)`. □

---

## 5. Attacks A1 and A3, redone with the repository inputs, and A4

Theorem C refutes the target, so these attacks are not the stopping point. They are redone because `LZ1.md` Amendment 2 asks for it, and because each failing step names a hypothesis that any restricted version of LZ1-i would have to supply.

### A1. Symmetry

*Claim attacked:* the law's symmetries force one common speed.

**Step A1.1 (the B4 route).** Input: the B4 note, Theorem, lines 61–68: "1. The `B4` invariant space of diagonal quadratic kinetic forms is one-dimensional, so `c_t = c_s` is forced. 2. A one-loop self-energy integral with a `B4`-invariant measure has `Sigma_t = Sigma_s` by finite relabeling of axes. ... 3. The statement is representation-blind: a gauge representation factor multiplies the same zero spacetime difference, so species differences also vanish at the marginal operator level." This step needs a symmetry that exchanges the time axis with a space axis. **Failing step: "the tick's Euclidean form is invariant under a signed permutation that moves the time axis."** A D5 symmetry commutes with `Ũ` by definition (`LZ1.md` line 38), so it maps the tick to itself and never to a translation. #9913 item 1 (consolidation line 101) says the same for the step set: "exactly 96 linear maps ... All fix the time axis." The cross-sector note says that off the `B4` surface "the time-fixing symmetry alone does not force equality of these marginal ratios" (lines 34–36), and that its alignment does not follow "On a **single-taste** object" (line 79). No reflection-positive Euclidean form of a five-mode tick is on file either (ST1-i is open). So A1.1 has no input in the live class.

**Step A1.2 (the orbit route).** Input: `LZ1.md` Theorem 4.1, and #9913 item 2 (consolidation line 102): "Any symmetry of a translation-invariant tick maps U to U or U^-1 and K to RK with R orthogonal. Such a map preserves w^2 = c^2 K^2 for every c, so it cannot fix c_e/c_gamma." A symmetry relates speeds only within one orbit. **Failing step: "all light species lie in one symmetry orbit."** It fails in the live class. Corollary C2 gives, in every law of a family with fixed symmetry requirements, two species in different orbits whose speed ratio is any positive number. This is the interacting-law form of `LZ1.md` Theorem 4.2, whose line 104 says the free witness "does not exhibit two bands in an admissible interacting law". The consolidation's line 790 already reads #9913's "two species" as "species that the tick symmetry does not exchange".

A1 fails at A1.1 (no time–space symmetry) and at A1.2 (no single orbit). Theorem C witnesses A1.2.

### A3. RG attraction

*Claim attacked:* interactions drive the speeds of all light species to one value.

**Step A3.1 (a controlled zoom).** Input: the attractor note, line 24, "conditional-support / open gate"; the spatial-lattice note, lines 41–42: its speeds "are not exact charged-particle pole speeds, microscopic signal-front speeds or a proved interacting spectral threshold." ZM1-i is open (`ZM1.md`). For Theorem C's species this step is moot: their speeds are exact at the lattice scale, and by Corollary C3 they survive every zoom in ZM1-OBS's band-limited class.

**Step A3.2 (drag between every pair).** Input: the exchange-matrix note, line 52, "3. each sector is dragged toward the other with positive coefficients `a,b > 0`", with conclusion (line 76) "the speed-difference mode is IR-attractive for every positive pair `a,b`". A running coupling needs the following native form.

**Lemma A3.1 (scale-dependent drag).** Let `a, b : [0,∞) → [0,∞)` be continuous, and let `v_F, v_B` solve `v_F′ = a(v_B − v_F)`, `v_B′ = b(v_F − v_B)`. Then `Δ := v_F − v_B` equals `Δ(0)exp(−∫₀^ℓ(a+b))`. So `Δ(ℓ) → 0` as `ℓ → ∞` if and only if `Δ(0) = 0` or `∫₀^∞(a+b) = ∞`.

*Proof.* Subtraction gives `Δ′ = −(a+b)Δ`. The function `Δ(ℓ)exp(∫₀^ℓ(a+b))` has derivative zero, so it is constant. The exponential factor tends to a positive limit if the integral converges and to `0` if it diverges. □

So positive drag is not enough; its integral must diverge. Drag carried only by an irrelevant coupling, or by a mediator that decouples below its mass, leaves a nonzero limiting difference. **Failing step: "every pair of light species has drag with divergent integral."** It fails in the live class. In Theorem C the exact tick leaves each species' one-excitation space invariant (Lemma 3.8(b)), so the two speeds do not run at all: the drag is identically zero. The repository already records this exception for its supplied models. Spatial-lattice note, line 31: "neutral disconnected sectors do not align by this mechanism"; lines 471–472: "If a species has q_a=0, its frame is a disconnected constant mode; no common metric for that sector follows from charged interactions." Soft spin-2 note, lines 268–270: "A photon shares the cone only if it belongs to the connected scattering sector. Decoupled sectors ... remain outside this proof."

**Step A3.3 (the rate).** LZ1(a) asks for `E = c|k|(1 + O((a|k|)^p))` with `p ≥ 2`.

**Lemma A3.2 (marginal drag gives a logarithmic rate).** In Lemma A3.1 let `a + b = λκ` with `κ(ℓ) = κ₀/(1 + Wκ₀ℓ)` and `λ, κ₀, W > 0`. Then `Δ(ℓ) = Δ(0)(1 + Wκ₀ℓ)^{−λ/W}`. With `ℓ = log(1/(a|k|))`, `Δ` is not `O((a|k|)^p)` as `|k| → 0`, for any `p > 0`, unless `Δ(0) = 0`.

*Proof.* `∫₀^ℓκ = W^{−1}log(1 + Wκ₀ℓ)`; insert it in Lemma A3.1. Put `t = a|k|`. Then `(1 + Wκ₀log(1/t))^{−λ/W}t^{−p} → ∞` as `t → 0`, because `t^{−p}` grows faster than any power of `log(1/t)`. □

This `κ` is the running charge of the spatial-lattice note's displayed flow. Its line 455 gives "powers `[1+W kappa_0 ell]^(-lambda_j/W)`", and lines 487–488 say the nonlinear statement is "not yet a theorem of the full quantum field theory". **Failing step for the rate clause: "the drag makes the speed difference decay as a power of `a|k|`."** It fails whenever the drag is marginal, even where the limiting speeds agree. Anber–Donoghue's Eq. (57) and Iengo–Russo–Serone's abstract report the same logarithmic running in continuum models (§7).

**Step A3.4 (matching at the cell scale).** #9913, consolidation line 112: "Because the tree cones are equal the logs cancel, so kappa is a finite lattice constant." Line 132: "The flow from the cell scale to the electron mass suppresses the offset only by a factor 0.88". These are #9913's numerical one-loop results for its supplied link law, not theorems here. They show that a flow acts on the running part and not on a finite offset generated at the cell scale.

A3 fails at A3.2 in the live class, with Theorem C as witness. It fails at A3.3 for the rate, even where it equalizes the limits.

### A4. Constraint closure (the gravity route)

Input: the curvature-closure note's full argument, Result 1: "Two species close iff `c₁ = c₂ = K/(4α)`. **Every species shares one matter cone.**" The mechanism needs a lapse-labelled family of constraints `C(N)` whose brackets close into one relabelling on every species. **Failing step: "the law carries a lapse-labelled family of constraints that closes on all light species."** The live class has one fixed update (PS-1) and no lapse family. The gravity response law PS-9 is a "Law to test" inside GR1/GR2, "Not a premise" (`TOE_ASSEMBLY.md` line 87). In Theorem C nothing of this kind reaches the two species. The soft spin-2 note's common cone starts from "Suppose a hard graviton belongs to the same connected rich-scattering domain" (line 227), which is the connectivity condition of A3.2 again.

---

## 6. What any proof must use

**Corollary 6.1.** Suppose a candidate theorem asserts, for a class of laws and states, that all propagating light species of the state have one Clifford speed. If the class contains `(U(θ₁,θ₂), ω_Σ)` or `(U(θ₁,θ₂), ω̄)` with `θ₁ ≠ θ₂`, the assertion is false. So every true version restricts at least one of: (i) the appended layers, below LZ1 §1, GA1-P-5 and NN-a; (ii) the state, below D1, local gauge invariance, cell invariance and half filling, all of which `ω̄` meets (Corollary C1); (iii) the species notion, below `LZ1.md`'s D4 with LZ1-SC, which Theorem C's bands meet.

*Proof.* Theorem C and Corollary C1. □

**Candidate specifications.** Each is proposed for the owner; none is adopted. Tests: (1) it states or fixes a part's target; (2) it is open-ended; (3) it settles a downstream physics question by premise; (4) it adds structure or constants its reasons do not need.

| Candidate | 1 | 2 | 3 | 4 | Effect |
|---|---|---|---|---|---|
| S-PL: the appended layers are exactly GA1-P-5's tiling-cube layer `W^cube`, with its two angles | pass | pass | fail, on file: `GA1_5.md` line 61, "For the cube member alone, pass 1 gives 1, 2, 4 as pass and 3 as fail if it is imposed as the only magnetic class" | pass | Excludes Theorem C's layers; LZ1-i[cube] is then open. |
| S-CONN: every light species couples to the charged sector with drag of divergent integral | fail: it states the mechanism LZ1-i asks for, as LZ1-C4 did (`LZ1.md` line 153, "Restates a common-speed mechanism") | conditional: "drag" needs a controlled zoom (ZM1-i) | fail: it decides by premise whether neutral light sectors exist | pass | Excludes Theorem C by premise, not by proof. |
| S-PHI: LZ1's species are only flux-carrying bands (R-Φ) and odd charged-sector bands | pass | pass | fail: T3 says "All light species share one limiting speed `c`"; S-PHI removes neutral species by fiat | pass | Excludes Theorem C's bands. |

None passes all four tests. No restriction of the appended class is on file that keeps GA1's magnetic question open, unlike S-PL, and still excludes link-only decoupled walks. The owner may specify; this file proposes no wording beyond the table.

---

## 7. Literature

Searched 2026-11-06 with WebSearch (standard mode). Searches: "Anber Donoghue emergence of a universal limiting speed"; "Bednik Pujolas Sibiryakov emergent Lorentz invariance from strong dynamics holographic"; "Liberati Visser Weinfurtner naturalness in emergent spacetime mono-metricity two-component BEC"; "Chadha Nielsen Lorentz invariance as a low energy phenomenon"; "Barbour Foster O Murchadha relativity without relativity universal light cone"; "Iengo Russo Serone renormalization group in Lifshitz-type theories"; "hidden sector Lorentz violation decoupled sector different limiting speed". Each abstract page below was fetched; the fetch tool returns summaries with short verbatim excerpts, and the quotes below are those excerpts. Nothing here is load-bearing.

- **Anber, Donoghue**, "The emergence of a universal limiting speed", arXiv:1102.0789, Phys. Rev. D 83, 105027 (2011). Abstract page and ar5iv text fetched. Speed differences obey RG equations of the form coupling times difference (Eqs. (18), (33), (53)–(54)); with a running coupling, Eq. (57), `η(μ) = η*[g²(μ)/g²(μ*)]^{2b/5}`, so "the difference in the speeds runs only logarithmically towards each other". Sec. V: "Gluon loops will not modify their own propagation speed." Sec. VIII: hidden fermions and gauge sectors "drop from the RG equations" once they are massive. Bears on A3.2 and A3.3.
- **Iengo, Russo, Serone**, "Renormalization group in Lifshitz-type theories", arXiv:0906.3477, JHEP 11 (2009) 020. ar5iv text fetched. Abstract: "a logarithmic running of c² persists also at low-energies, if δc²≠0 in the UV"; Lorentz symmetry is recovered only if the violating terms are "unnaturally fine-tuned". Bears on A3.3.
- **Bednik, Pujolàs, Sibiryakov**, "Emergent Lorentz invariance from Strong Dynamics: Holographic examples", arXiv:1305.0011; the arXiv page lists DOI 10.1007/JHEP11(2013)064. Abstract: deviations "are found to be power-law suppressed" in strongly coupled holographic models. Context for A3.3: a power law here needs strong coupling.
- **Giuliani, Mastropietro, Porta**, "Lattice quantum electrodynamics for graphene", arXiv:1107.4741, Ann. Phys. 327 (2012) 461. Abstract: "the Fermi velocity increases up to the speed of light". A rigorous connected-sector example.
- **Giudice, Raidal, Strumia**, "Lorentz Violation from the Higgs Portal", arXiv:1003.2364, Phys. Lett. B 690 (2010) 272. Abstract: "the strong coupling dynamically makes the speed-of-light equal for all colored particles". Connected-sector alignment.
- **Pospelov, Shang**, "On Lorentz violation in Horava-Lifshitz type theories", arXiv:1010.5249; the arXiv page lists DOI 10.1103/PhysRevD.85.105001. Abstract: the Standard Model can be coupled to "a Lorentz symmetry violating sector" if "the interaction between the two is mediated by higher-dimensional operators". This is the A3.2 failure mode, used there as protection.
- **Collins, Perez, Sudarsky, Urrutia, Vucetich**, "Lorentz invariance and quantum gravity: an additional fine-tuning problem?", arXiv:gr-qc/0403053, Phys. Rev. Lett. 93, 191301 (2004). Abstract: Lorentz violation "at the percent level" unless bare parameters are fine-tuned.
- **Polchinski**, comment on arXiv:1106.1417, arXiv:1106.6346. Abstract: the "only known exceptions" are "based on supersymmetry". The journal is not stated on the page (DOI prefix 10.1088/0264-9381): NOT VERIFIED as to journal.
- **Liberati, Visser, Weinfurtner**, "Naturalness in emergent spacetime", arXiv:gr-qc/0512139, Phys. Rev. Lett. 96, 151301 (2006). Abstract: a two-component BEC model "avoids" the naturalness problem. The mono-metric tuning statement attributed by a search snippet to gr-qc/0605121 was not fetched: NOT VERIFIED.
- **Barbour, Foster, Ó Murchadha**, "Relativity without relativity", arXiv:gr-qc/0012089. ar5iv Sec. VII: "the scalar field must respect the gravitational light cone"; the mechanism "will generate the universal metric–matter light cone – for bosons at least". Context for A4.
- **Kitaev**, "Anyons in an exactly solved model and beyond", arXiv:cond-mat/0506438, Ann. Phys. 321 (2006) 2. Abstract: "solved exactly by a reduction to free fermions in a static Z₂ gauge field". Theorem C uses the same pattern: an exactly free sector inside an interacting gauge model.
- **Bialynicki-Birula**, "Dirac and Weyl equations on a lattice as quantum cellular automata", arXiv:hep-th/9304070, Phys. Rev. D 49 (1994) 6920. Context for walk cones.
- **Farrelly**, "A review of Quantum Cellular Automata", arXiv:1904.13318, Quantum 4, 368 (2020). Abstract: QCAs arise if "we also demand a strict bound on the speed of information propagation". A strict causal bound is common to all species but does not equalize their speeds; in Theorem C both speeds lie below it.
- **NOT VERIFIED** (not fetched, or not fetchable): Chadha, Nielsen, "Lorentz invariance as a low energy phenomenon", Nucl. Phys. B 217 (1983) 125 (the DOI redirect could not be followed); Nielsen, Picek (1983); Teitelboim, Ann. Phys. 79 (1973) 542, and Hojman, Kuchař, Teitelboim, Ann. Phys. 96 (1976) 88, as cited by the curvature-closure note; arXiv:1112.4714, seen only as a search result. Barceló, Liberati, Visser, "Analogue Gravity", arXiv:gr-qc/0505065: its abstract was fetched and does not mention multi-metric structure, so it is not cited for that.

**Novelty, as far as this search reaches.** That a decoupled sector keeps its own limiting speed is known in continuum effective field theory (Anber–Donoghue Sec. VIII; Pospelov–Shang). This search found no exact construction of two Clifford cones with independent speeds inside a gauge-invariant, cell-covariant quantum cellular automaton class. The search was limited to the queries above.

---

## 8. [check]

`/tmp/toe-lz1i/check_lz1i.py`, run with `python3 -I` after `memory_pressure` showed 54% free; 0.9 s, 125 MB resident; output in `/tmp/toe-lz1i/out.txt`. It builds the one-flavour free walk `V_θ = e^{iθR_o}e^{−iθR_e}` on an `8³` torus (512 sites) with `LW1`/`MT1` sign conventions. Output:

```
Re^2 = 1: True  Ro^2 = 1: True
th=0.4: max |w - w_pred| = 3.44e-15;  speed check sin(th)/sqrt3 = 0.224831
th=1.1: max |w - w_pred| = 3.11e-15;  speed check sin(th)/sqrt3 = 0.514539
sign lift consistent: True  commutes with Re: True  with Ro: True
(P_r)^4 scalar: True  value: -1.0
some r^k maps 0 into 0+2Z^3 (nontrivial stabiliser)? False
```

It agrees with `cos w = 1 − sin²θ(1 − χ(K))` at every torus momentum, finds a sign lift of the quarter turn `r` commuting with both half-step generators, finds its fourth power `−1`, and finds no nontrivial stabilizer of site `0` in `⟨2Z³, r⟩`. It guides Lemma 3.3(b), Lemma 3.4(b) and the use of B10. It proves nothing.

---

## FINISH

**Proved** (here, pass 1; not yet distilled or refereed).
- Lemma 3.1 (the layered sector freezes the matter hop for every allowed constant), Lemma 3.2 (star factorization; the irreducible label space `B` of `S(D_∥)`; gauge-invariant label operators), Lemma 3.3 (`𝒢_Σ = 2Z³⋊⟨r⟩` acts freely; the lift acts on labels by permutation), Lemma 3.4 (cube-wise covariance of the sign lifts; a genuine rephased lift on `𝒢_Σ`), Lemma 3.5 (induction along a free action), Lemma 3.6 (the appended layers meet LZ1 §1, GA1-P-5, cell covariance and NN-a, the last through `GA1_5.md` Lemma U), Lemma 3.7 (`ω_Σ` is a half-filled D1 state), Lemma 3.8 (the one-excitation dynamics in the GNS space).
- **Theorem C.** On `L5-U[m]`, `m ∈ {2,4,6,8}`, for every allowed `(ε, μ, τ_E)` and all `θ₁, θ₂ ∈ (0, π/2)`, the update `U(θ₁,θ₂)` and the state `ω_Σ` have two propagating light species in `H_phys ∩ H_even ∩ ker(Ũ−1)^⊥`, with exact Clifford cones of speeds `sin θ₁/√3` and `sin θ₂/√3`.
- Corollary C1 (the same two species in a cell-invariant, site-transitive, half-filled D1 state), Corollary C2 (the ratio is a free constant; the species lie in different symmetry orbits), Corollary C3 (a ZM1-OBS comparison keeps both speeds; conditional on a comparison with a coarse branch form).
- Lemma A3.1 (scale-dependent exchange matrix: the speeds meet if and only if the integrated drag diverges), Lemma A3.2 (marginal drag gives a logarithmic rate, not a power of `a|k|`), Corollary 6.1 (what every true version must restrict).
- Ported, not re-derived: `MT1.md` Theorems 1, 4, 7; `LW1.md` A2, B10; `LW1_5.md` B1-U; `GA1_5.md` Lemma U and Proposition C; `LZ1.md` Theorem 4.1; `ZM1_OBS.md` Theorems 3, 9, 9′.

**Counterexamples.** Theorem C refutes LZ1-i in the lane's form, "the interacting law forces one common limiting speed for all propagating light species", on `L5-U[m]` for every even `m`. Corollary C1 extends it to a cell-invariant, half-filled D1 state. Redone with the repository inputs, A1 fails at A1.1 (no time–space symmetry) and A1.2 (no single orbit); A3 fails at A3.2 (drag between decoupled sectors) and, for the rate, at A3.3; A4 fails at the lapse-family step. Theorem C witnesses A1.2 and A3.2.

**Open by name.**
- LZ1-i[O]: the question on `L5-O[S_+]`. Its Majorana hop does not conserve matter number, so §3.1's freezing does not transfer; GA1-5-O is open.
- LZ1-i[odd m]: §3 needs `m/2` rishons on every in-plane end.
- LZ1-i[cube]: the base tick with at most GA1-P-5's tiling-cube layer (candidate S-PL).
- LZ1-i[VC1]: the VC1 vacuum, once VC1 constructs it. By Corollary 6.1(ii), it must differ from `ω̄` in some property beyond D1, gauge invariance, cell invariance and half filling.
- LZ1-i[R-CS^str]: the fermion clause; Theorem C uses no charged sector.
- Inherited and unchanged: the rate and one-loop coefficient clauses of LZ1(a); ZM1-i; MT1-S[R-CS]; R-CS; GA1-P-5 as law data.

**What changes downstream.**
- LZ1(a) cannot be proved for the live class as it stands. Every part that imports LZ1 (ST1, GR1, GR2, GA2) imports a restricted version, and the restriction must be named (Corollary 6.1).
- GA1-P-5 now carries LZ1-i. An appended class that admits link-only multiplicity walks admits independent light cones (Theorem C).
- GR2's "two tensor polarisations at speed `c`" needs a `c` fixed by a mechanism that reaches every light sector; the class does not supply one.
- ZM1 and ZM1-OBS: a zoom in ZM1-OBS's band-limited class transfers these speeds (Corollary C3), so it cannot repair LZ1-i.
- ST1's signature clause and MT1-S are unaffected: each species of Theorem C has its own `(3,1)` cone, and no fermion is involved.
- For the owner: whether to specify the appended class, a vacuum property or the species notion. The three candidates in §6 each fail at least one test; none is adopted.
