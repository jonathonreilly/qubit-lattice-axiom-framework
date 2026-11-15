lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# LW2M: a magnetic layer that couples cubes, pass 1

Written 2026-11-08 by a Claude Opus 5.5 headless lane on the Mac mini, as a pass-1 lane of the TOE assembly (part LW2, item 3, LW2M; owner 2026-11-08: "Yes, start it"). Method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status. It adopts no law, no reading and no class. It changes no axiom and no working-set entry; `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means that the argument is written out below and has not yet been distilled or refereed. "[check]" marks one tiny scratch computation (`/tmp/toe-LW2M/check_lw2m.py`, run with `python3 -I` at 55 percent free memory, 0.2 s, 20 MB peak; largest object a 4 x 4 matrix). A check guides and never proves. Every proof below is a finite algebraic argument or a one-variable analyticity argument, written for Lean formalization.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `claude/toe-assembly` (this checkout) | `0ec9a2b3325f43f51d2ee0df58cd0a6f914869df` |
| `origin/claude/ym4d-hard-route` (read with `git show` only, after `git fetch -q origin claude/ym4d-hard-route`) | `8d48cdf80bf9d92e449cbf6212f41876b5f76270` |

Files read at those commits, by line. This folder (`.claude/science/physics-loops/toe-assembly-20261104/`): `prior/LW2M.md` (all 77 lines); `TOE_ASSEMBLY.md` lines 13-23 (axioms), 201-270 (sections 3.4-3.11), 310-326 (part LW2), 464-475 (part GB1), 617-641 (section 6), 743-759 (section 11); `GB1ISO.md` (all 186 lines); `GB1ISO_REFEREE.md` lines 112-140 (FP, T0-start^an, ISO-FP) and 200-271 (checks, edits, open list, FINISH); `GB1.md` lines 1-75 (status with Amendments 1-4, definitions, Theorems 2.1-2.3) and 93-125 (section 4, Theorems 5.1-5.2); `GB1QL.md` lines 29-94 (definitions) and 137-150 (Proposition 4.2), plus grep hits at 68, 70, 259, 293-305, 347-357; `GB1E.md` lines 1-40 (status, definitions, the two lifts) and 140-182 (section 7), plus grep hits at 54, 78, 204, 222; `GB1E_REFEREE.md` lines 140-166 (decisions (a)-(e), start of the four-test table); `GB1_GEN_OWNER_CHECK.md` (all 96 lines); `LW1_5.md` lines 1-12 and 34-106 (definitions, the two laws), plus grep hits at 122-141, 187, 262, 276-278, 351-357; `GA1_5.md` lines 1-30 (status), 44-91 (definitions, Theorems 2.1, 2.2, 3.1) and 199-295 (the referee closures reproduced there: readings NN-a and NN-b, Lemma U, Proposition C, Lemma S1'); `LW1.md` lines 36-48 (sites, tilings, cell group) and lines 401 and 486 (Theorem E1, GA1-P). `GA1_5_REFEREE.md` was read only as reproduced in `GA1_5.md` section 8. YM branch, `.claude/science/physics-loops/ym4d-hard-route-20261030/`: `GOAL.md` lines 20-48; `library/ro1.md` (last changed `922ec0066`) lines 54-68 (H-U, H-L, H-C, H-T), 630-648 (Theorem 9) and 678-694 (Result); `library/o4-two-point.md` (last changed `0f018e1a4`) lines 1-7, 47-73 and 163-188 (Theorem O4-2 and its limits); `library/lg1.md` (last changed `f9945a2b5`) lines 365 and 431 (Theorems 10 and 13(5)); `library/t0-tree.md` (last changed `173667309`) by grep for anisotropy, O(4), diagonal mirrors and T0-rate (hits at lines 13, 15, 51-70, 150-166, 265, 394).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". NN-a (section 3.7), R-SUM and R-IA (section 3.11) are read plainly. Where a target needs a definition the sources do not fix ("full plaquette-sum form"), section 4.1 states candidate readings and four-tests them. Nothing is adopted.

**Working set used, by name.** PS-1 with PS-1c (cell covariance), PS-5 (five modes per site), PS-6 and PS-6r (finite link registers), through the two laws `L5-U[m]` and `L5-O[S_+]` of `LW1_5.md` section 2 and the owner decision GA1-P-NN = NN-a (`TOE_ASSEMBLY.md` section 3.7). The four generator readings stay live (section 3.11); only R-SUM and R-IA are used. Results used, cited by name and path, are listed in section 7. Inputs from outside the working set: standard finite-dimensional linear algebra (tensor products, partial traces, the spectral theorem); the Baker-Campbell-Hausdorff expansion to third order, rebuilt in section 4.4; zeros of a nonzero one-variable analytic function are isolated; modified Bessel functions `I_j` as power series, used only through `GB1E.md` Theorem 7.1. Literature is context only (section 2) and is never a proof step.

---

## 0. The questions, quoted

`TOE_ASSEMBLY.md` line 317, part LW2, item 3: "**LW2-M, a magnetic layer that couples cubes.** The four-tiling layer FP of `GB1ISO.md` §6, or another cube-coupling layer. Give the NN-a check. Prove or refute GB1-CF at finite register. Work ISO-FP."

`GB1ISO.md` line 156-159, the layer: "**FP, proposed, not adopted.** Replace the magnetic layer by \(W_B^{FP}=\prod_{v\in\{0,e_1,e_2,e_3\}}\prod_{C\in\mathcal C+v} e^{-i(\theta/2)B_C}\)." The text fixes no order of the four factors.

`GB1ISO.md` line 165: "At finite register, shared-link plaquette operators need not commute (`GB1.md` §4 and `LW1.md` GA1-P); the ordered product's covariance and exact full-sum form do not follow. **GB1-CF remains open** for an admissible finite-register update." The same line: "Neither pass made an NN-a check of FP."

`GB1ISO_REFEREE.md` line 235: "**GB1-CF** (carried from `GB1.md` line 109). An admissible finite-register update whose magnetic term is the full plaquette sum."

`GB1ISO.md` line 167: "**ISO-FP (OPEN).** There are parameter families under FP and either reading, with \(a\to0\), \(c>0\) and \(p>0\), whose volume-first action-density correlations converge to a non-trivial limit invariant under \(D_cSO(4)D_c^{-1}\), at rate \(O((a/r)^p)\)." The same line: "Finite-torus exchange invariance for R-SUM under FP is also open".

`TOE_ASSEMBLY.md` line 235, NN-a (owner 2026-11-06), the clauses used here: "A nearest-neighbour gate `g` is a unitary supported within `F_x`, `F_y` and `H_ℓ`, where `ℓ=(x,y)` and `y=x+e_i`." "Evenness means `[g,P_xP_y]=0`". "The update has a fixed finite number of such layers, independent of volume. Its automorphism `α` fixes every local gauge generator. It commutes with every cell lift `α_s`, for `s∈𝒢=2Z³⋊O_{c₀}`." "Gauge invariance and cell covariance are required of the complete update only."

`TOE_ASSEMBLY.md` line 269, the readings: the owner answered "cant we probe each of these? why do we need to pick?", so "no reading is adopted". The texts used are those of `GB1_GEN_OWNER_CHECK.md`: for R-SUM, "For GB1's specified layers \(e^{-i\tau_kK_k}\), set \(H=\sum_k\tau_kK_k\)" and "Use \(T(a_0)=e^{-a_0H}\)"; for R-IA, "\(T_{\rm loc}=\Phi(\lambda\theta,\lambda\tau_E)=e^{-\lambda\theta H_B/2}e^{-\lambda\tau_EA}e^{-\lambda\theta H_B/2}\)" with "one fixed \(\lambda>0\), in tick units, for each instantiated law".

The lane brief adds three tasks. (1) The NN-a check of FP on `L5-U[m]` and on `L5-O[S_+]`: gate decomposition, layer count, evenness, cell covariance, or the step where it fails. (2) GB1-CF at finite register, exactly or with an error bound in the register size, or a proof that none exists in a stated class; probe FP, a symmetrised ordering, a Trotter-Suzuki ordering and any other cube-coupling layer, and choose none. (3) ISO-FP under R-SUM and under R-IA: restoration with a rate, a weaker anisotropic form the YM4D side can accept, or a counterexample; at least the first failing step for each reading.

## 0.1 Outcome in one paragraph

**FP fails the NN-a check at cell covariance.** It compiles into even nearest-neighbour gates of finite depth and is gauge invariant (Theorem 3.1). But the cell group permutes the three shifted tilings by every permutation (Lemma 1.2), and on both live laws the shifted layers do not commute to second order, because shared-link plaquette commutators have nonzero top components (Lemma 1.6). So, in every order of the four factors, FP is not cell covariant for every `θ` outside a closed discrete set (Theorem 3.2). **GB1-CF at finite register is refuted in stated classes.** The exact full sum `e^{-iθΣB_p}` is not of finite depth for `θ` outside a countable set (Theorem 4.2). With the exact covariance NN-a requires, no admissible layer of full-sum form exists among: all words in the four tiling layers whose order matrix is not label-invariant, including every FP order and every Lie-Trotter product (Theorem 4.3); all 24 nested palindromes and their Strang products, which fail at third order (Theorem 4.4); and every covariant layer of disjoint gates, at every angle (Theorem 4.5). The remaining words are the open lemma LW2M-WORD, with three failed attacks named. On `GB1QL.md`'s growing family FP's defects are `O(θ^2N^3/s)`, but exact covariance still fails at each `s` (Proposition 4.6); a register-limit covariance reading R-COV_s would admit it and fails test 4. **ISO-FP.** Under R-SUM, the exact FP lift is time-space exchange invariant at most on a discrete set of `θ` (Theorem 5.1), so RO1's mirror hypothesis H-L fails generically; with GB1QL's electric term under R-IA it fails at every parameter (prior). Under R-IA with a Wilson-dual electric function `G_b`, the FP lift is exactly T0's isotropic Wilson measure (Theorem 5.2), so H-L holds and the YM branch's Theorem O4-2 gives two-point isotropy with `c=1`, conditional on its own inputs (Corollary 5.3). The first failing step there is T0 itself (non-triviality, higher points, rate). That electric function is calibrated to the Wilson weight and fails tests 1, 3 and 4. No reading, law or class is adopted.

## 1. Setting and notation

### 1.1 Laws, links and plaquettes

The two laws are those of `LW1_5.md` section 2. On `L5-U[m]`, `1 ≤ m ≤ 9`, a link `ℓ=(x,y)`, `y=x+e_i`, carries `Λ^m C^{10}`, with rishon modes `r^y_j`, `r^x_k` (`j,k=1,…,5`) and `U_ℓ^{jk}=r^y_jr^{x†}_k`. On `L5-O[S_+]` a link carries the 512-dimensional half-spin representation `S_+` of `Spin(20)`, with Clifford generators `η^y_a, η^x_b` and `U^{ab}=2T_{a,10+b}=iη^y_aη^x_b`. Links are ordinary tensor factors and commute with matter (`LW1_5.md` line 42). Every link entry is even in the rishons or in the `η`'s, so entries on distinct links commute.

Plaquettes follow `GA1_5.md` line 50: "For an oriented traversal `t`, put `𝒰(t)=U_ℓ` forward. Backward use `U_ℓ†`, meaning `(U_ℓ†)^{jk}=(U_ℓ^{kj})†`, for `L5-U`, and `-U_ℓᵀ` for `L5-O`. For a closed walk `c=(t₁,…,t_n)` define `W(c)=tr(𝒰(t_n)⋯𝒰(t₁))`; `B_p=W(∂p)+W(∂p)†`." For a cube, `B_C=Σ_{p⊂C}B_p` (six faces). `GA1_5.md` Theorem 3.1 (line 85) proves that each `W(c)` is gauge invariant and "is carried by a cell lift to `W(gc)`", and that `B_p` does not depend on the boundary orientation. So a cell lift `α_g` sends `B_C` to `B_{gC}`.

The SU(2) test family of `GB1QL.md` is used in sections 4.6 and 5. Its link is `R_s` (`GB1QL.md` section 1.2) or, on the infinite-register target, `L²(SU(2))`. There `B_p=2\,{\rm Tr}\,X_p` (`GB1E.md` line 27).

### 1.2 The four tilings and their memberships

Let `𝒞` be the unit cubes whose base `b` has `b_1≡b_2≡b_3 (mod 2)`; it is `𝒯_e∪𝒯_o` of `LW1.md` line 38. For `v∈{0,e_1,e_2,e_3}` put `𝒞_v=𝒞+v` and label it `0,1,2,3`. Each link lies in exactly one cube of each `𝒞_v`, and the cubes of `𝒞_v` have pairwise disjoint link sets (`GB1ISO.md` Theorem 2.1, translated by `v`). Each `𝒞_v` is the union of the two site-disjoint families `𝒯_e+v` and `𝒯_o+v` (translate `LW1.md` line 38). For a plaquette `p` put `n_v(p)=1` if `p` is a face of a cube of `𝒞_v`, else `0`.

**Lemma 1.1 (memberships; port of `GB1ISO.md` Theorem 6.1 and `GB1ISO_REFEREE.md` line 116).** Let `p` lie in the `(i,j)`-plane with base `y`. Then `n_v(p)=1` iff `y_i-v_i≡y_j-v_j (mod 2)`. So every plaquette has exactly two memberships, and

| plane | in-plane base parity equal | unequal |
|---|---|---|
| `(1,2)` | `{0,3}` | `{1,2}` |
| `(1,3)` | `{0,2}` | `{1,3}` |
| `(2,3)` | `{0,1}` | `{2,3}` |

*Proof.* The first sentence is the referee's counting (line 116), which is the proof of `GB1ISO.md` Theorem 6.1. Insert `v=0,e_1,e_2,e_3`. For the `(1,2)`-plane: `v=0` and `v=e_3` need `y_1≡y_2`; `v=e_1` and `v=e_2` need `y_1≢y_2`. The other planes are the same computation. □ [check: the script lists the six membership types of the table.]

Write `H_v=Σ_{C∈𝒞_v}B_C=Σ_p n_v(p)B_p` and `W_v(φ)=∏_{C∈𝒞_v}e^{-iφB_C}`. The second equality for `H_v` holds because each face of a `𝒞_v` cube lies in exactly one cube of `𝒞_v`. The factors of `W_v(φ)` act on disjoint links and commute. Both are formal infinite expressions; on a local observable only finitely many terms act (`LW1.md` E1, line 401). In this notation `W_B^{FP}=W_{v_4}(θ/2)W_{v_3}(θ/2)W_{v_2}(θ/2)W_{v_1}(θ/2)` for an order `(v_1,v_2,v_3,v_4)` of `{0,1,2,3}`. All 24 orders are treated.

### 1.3 The cell group permutes the shifted tilings

`LW1.md` line 43: "The group \(O\) consists of determinant-one signed coordinate permutations. Its action about \(c_0\) is \(x\mapsto Q(x-c_0)+c_0\). Write \(\mathscr G=2\mathbb Z^3\rtimes O_{c_0}\)".

**Lemma 1.2.** Let `g∈𝒢` have linear part `Q`, with `Qe_i=δ_ie_{π(i)}`, `δ_i=±1`. Then `g𝒞_0=𝒞_0` and `g𝒞_{e_i}=𝒞_{e_{π(i)}}`. Every permutation `π` of `{1,2,3}` occurs. Hence `α_g(W_v(φ))=W_{π_g(v)}(φ)`, where `π_g` fixes the label `0` and acts on `1,2,3` by `π`.

*Proof.* Let `x↦Q(x-c_0)+c_0+2t`. The unit interval `[b_i,b_i+1]` in coordinate `i` goes to coordinate `π(i)`. If `δ_i=1` its image is `[b_i+2t_{π(i)},b_i+1+2t_{π(i)}]`. If `δ_i=-1` it is `[-b_i+2t_{π(i)},1-b_i+2t_{π(i)}]`, since `1/2-(b_i+1-1/2)=-b_i`. In both cases the new base satisfies `b'_{π(i)}≡b_i (mod 2)`. So `g` permutes the coordinates of the base parity vector by `π`. Now `𝒞_0` is the set of cubes with parity vector `000` or `111`, and `𝒞_{e_i}` the set with `e_i` or `𝟙-e_i`. A coordinate permutation fixes the first set and sends the second to the class of `e_{π(i)}`. For a permutation `π`, choose signs with `sign(π)∏_iδ_i=1`; this gives an element of `O`. The last claim follows from `α_g(B_C)=B_{gC}` (section 1.1). □

The referee recorded the same fact in words (`GB1ISO_REFEREE.md` line 119): "Its coordinate permutations permute \(\mathcal C+e_1,\mathcal C+e_2,\mathcal C+e_3\)." In particular a quarter-turn about the `e_3`-axis through `c_0` exchanges the labels `1` and `2` and fixes `0` and `3`.

### 1.4 Components of link operators

Let `S` be a finite set of links and `X` an operator on `⊗_{ℓ∈S}H_ℓ`. For `ℓ∈S` let `E_ℓ(X)=d_ℓ^{-1}({\rm tr}_ℓX)⊗1_ℓ`, `d_ℓ=\dim H_ℓ`. The `E_ℓ` are commuting idempotent linear maps. For `T⊆S` put `X_T=∏_{ℓ∈T}(1-E_ℓ)∏_{ℓ∈S∖T}E_ℓ(X)`, the **`T`-component** of `X`.

**Lemma 1.3.** (a) `X=Σ_{T⊆S}X_T`. (b) `X_T` is a sum of products of operators that are traceless on each link of `T`, times the identity on `S∖T`. (c) If `X` acts as the identity on `ℓ`, then `X_T=0` for every `T∋ℓ`. (d) If product vectors `ψ=⊗ψ_ℓ`, `φ=⊗φ_ℓ` satisfy `ψ_ℓ⊥φ_ℓ` for every `ℓ∈S`, then `⟨ψ,Xφ⟩=⟨ψ,X_Sφ⟩`. If traceless `Z_ℓ` satisfy `{\rm tr}(X⊗_{ℓ∈S}Z_ℓ)≠0`, then `X_S≠0`. (e) For `R⊆S`, `X` lies in `B(H_R)⊗1` iff `X_T=0` for all `T⊄R`. (f) Components do not change when `S` is enlarged and `X` is tensored with the identity.

*Proof.* (a): expand `∏_ℓ(E_ℓ+(1-E_ℓ))=1`. (b): `1-E_ℓ` has range in the operators with zero partial trace on `ℓ`, and `E_ℓ` has range in `1_ℓ⊗(\cdot)`. (c): `(1-E_ℓ)X=0` and the maps commute. (d): for `T≠S` pick `ℓ∈S∖T`; then `X_T=Y⊗1_ℓ`, so `⟨ψ,X_Tφ⟩` carries the factor `⟨ψ_ℓ,φ_ℓ⟩=0`, and `{\rm tr}(X_T⊗Z)` carries `{\rm tr}Z_ℓ=0`. Use (a). (e): one direction is (c); for the other, `X=Σ_{T⊆R}X_T`. (f): `E_ℓ(1)=1`. □

For a formal locally finite sum `K=Σ_ik_i` of link operators with finite supports, put `K_T=Σ_i(k_i)_T`. For nonempty finite `T` only the finitely many `k_i` whose support contains `T` contribute, by (c).

**Lemma 1.4 (a nonzero component gives a nonzero derivation).** If `K_T≠0` for some nonempty finite `T`, then there is an operator `A` on one link with `[K,A]=Σ_i[k_i,A]≠0`.

*Proof.* Fix `ℓ∈T`. Among the finitely many `T'∋ℓ` with `K_{T'}≠0`, take `T` maximal for inclusion. Work on a finite `S` that contains every support meeting `ℓ`. A term `(k_i)_{T'}` with `ℓ∉T'` commutes with `A`, by (c). For `ℓ∈T'`, `[(k_i)_{T'},A]` lies in `B(H_{T'})⊗1`, so by (e) its `T`-component vanishes unless `T⊆T'`. By maximality, `[K,A]_T=[K_T,A]_T`. Write `K_T=Σ_rx_r⊗y_r`, with `x_r` traceless on `ℓ` and the `y_r` linearly independent products of traceless operators on `T∖{ℓ}` (or `y=1` if `T=\{ℓ\}`), and `x_1≠0`. A nonzero traceless `x_1` is not a scalar, so some `A` has `[x_1,A]≠0`. Each `[x_r,A]` is traceless, so `[K_T,A]=Σ_r[x_r,A]⊗y_r` equals its own `T`-component, and it is nonzero because the `y_r` are independent. □

### 1.5 Chains of plaquettes

A **simple chain** is a list of distinct plaquettes `p_1,…,p_n` with links `ℓ_1,…,ℓ_{n-1}` such that `∂p_{k+1}∩(∂p_1∪⋯∪∂p_k)=\{ℓ_k\}` and `ℓ_k∈∂p_k∖(∂p_1∪⋯∪∂p_{k-1})`. Put `S_n=∂p_1∪⋯∪∂p_n`; it has `3n+1` links. The links `ℓ_k` are **shared**; the others are **single**. The chain is **pinned** if every `p_k` has two opposite sides that are single. Two plaquettes sharing exactly one link form a pinned chain (`n=2`). A **straight row** (coplanar plaquettes with bases `y,y+e_i,…,y+(n-1)e_i`) is a pinned chain: its single links include the two sides of each plaquette parallel to `e_i`.

**Lemma 1.5 (rigidity).** (i) If `p≠q` share exactly one link, the only plaquettes with all four links in `∂p∪∂q` are `p` and `q`. (ii) The only plaquettes with all four links in `S_n` of a straight row are the plaquettes of the row.

*Proof.* (ii) and the coplanar case of (i): all links lie in one plane and form the edge set of a `1×n` strip; its only unit squares are its `n` cells. Perpendicular case of (i): say `p` in the `(1,2)`-plane with base `y` and `q` in the `(1,3)`-plane with base `y`, sharing `(y,y+e_1)`. The direction-1 links of `∂p∪∂q` start at `y,y+e_2,y+e_3`; the direction-2 links at `y,y+e_1`; the direction-3 links at `y,y+e_1`. A `(2,3)`-square needs a direction-2 link starting at `y+e_3` or a direction-3 link starting at `y+e_2`; there is none. A `(1,2)`-square needs direction-1 links at `z` and `z+e_2` and direction-2 links at `z` and `z+e_1`; only `z=y` works, giving `p`. Likewise only `q` among `(1,3)`-squares. The other relative positions are images of this one under lattice symmetries. □

**Lemma 1.6 (chain commutators do not vanish).** Let `p_1,…,p_n` be a pinned simple chain and `Y_n=[B_{p_n},[B_{p_{n-1}},…,[B_{p_2},B_{p_1}]…]]`. (a) On `L5-U[m]`, every `1≤m≤9`, and on `L5-O[S_+]`, `(Y_n)_{S_n}≠0`. (b) Let `ℓ_0` be a single link of `p_1` such that `p_1` keeps two opposite single sides other than `ℓ_0`. Let `A_0=n_{x,c}:=r^{x†}_cr^x_c` on `ℓ_0` for `L5-U`, and `A_0=iη^y_1η^x_1` on `ℓ_0` for `L5-O`. Then `[B_{p_n},…,[B_{p_1},A_0]…]` has nonzero `S_n`-component. (c) On the SU(2) register `R_s`, every `s≥1`, `[B_p,B_q]_{∂p∪∂q}≠0` for any `p≠q` sharing exactly one link.

*Proof.* *Structure.* Write `W(∂p)=Σ_{\bf i}⊗_{ℓ∈∂p}e_{p,ℓ}({\bf i})`: the trace sums one flavour index per corner, and each link carries the entry `𝒰^{ab}` whose indices sit at its two corners. Entries on distinct links commute. By induction on `n`, `Y_n` is a sum, over choices `σ_k∈\{W(∂p_k),W(∂p_k)^†\}` and corner indices, of tensor products whose factor on a single link is one entry and whose factor on `ℓ_k` is `[f_k,g_k]`, with `f_k` the entry of `p_{k+1}` and `g_k` that of `p_k` on `ℓ_k`. The reason: `p_{k+1}` meets the support `S_k` of the previous commutator only in `ℓ_k`, where the only factor is `g_k`.

*Case `L5-U`.* Write `E_{αβ}=f_α^†f_β` for rishon modes `α,β`. Then `U^{ab}=-E_{xb,ya}` and `(U^†)^{cd}=r^x_cr^{y†}_d=-E_{yd,xc}`, and
\[
[U^{ab},(U^\dagger)^{cd}]=\delta_{ad}E_{xb,xc}-\delta_{bc}E_{yd,ya},\qquad [U^{ab},U^{cd}]=0 .
\]
Trace facts on `Λ^mC^{10}`: `U^{ab}(U^{ab})^†=n_{xb}(1-n_{ya})` has trace `κ_m=\binom{8}{m-1}>0`; for `(a,b)≠(a',b')`, `U^{ab}(U^{a'b'})^†` maps each occupation basis vector to another one or to zero, so it has zero diagonal; and `U^{ab}((U^†)^{a'b'})^†=U^{ab}U^{b'a'}` changes the `x`-end number by two, so it is traceless. The same holds with `U` and `U^†` exchanged. Pair `Y_n` with `⊗_{ℓ∈S_n}Z_ℓ` as follows. On each single link choose a target entry `t_ℓ` and set `Z_ℓ=t_ℓ^†` (traceless). The pairing keeps only the terms whose entry on `ℓ` is `t_ℓ`. The type of `t_ℓ` (`U` or `U^†`) fixes `σ_k` for the plaquette containing `ℓ`, because `W^†` uses the adjoint entries. Its indices fix the two corner indices of `ℓ`. Two opposite single sides fix all four corner indices of `p_k`. So exactly one term survives, and on `ℓ_k` it carries `[f_k,g_k]` with determined `f_k,g_k`. Choose `σ_1` freely and then each `σ_{k+1}` so that `f_k,g_k` have opposite types. Choose the corner indices so that, writing the `U`-type entry as `U^{ab}` and the `U^†`-type entry as `(U^†)^{cd}`, we have `a=d` and `b≠c`. Then `[f_k,g_k]=±E_{xb,xc}`, which is traceless. Set `Z_{ℓ_k}=E_{xc,xb}`: `{\rm tr}(E_{xb,xc}E_{xc,xb})={\rm tr}\,n_{xb}(1-n_{xc})=κ_m`. The pairing equals `±κ_m^{|S_n|}≠0`, and Lemma 1.3(d) gives (a). For (b) the first step gives on `ℓ_0` the factor `[e,n_{x,c}]`, and `[U^{ab},n_{x,c}]=-δ_{bc}U^{ab}`, `[(U^†)^{ab},n_{x,c}]=δ_{ac}(U^†)^{ab}`. Choose the `x`-end corner index of `p_1` on `ℓ_0` equal to `c`, pair with `Z_{ℓ_0}=e^†`, and continue as in (a).

*Case `L5-O`.* Entries are `±iη^y_aη^x_b`; `W(∂p)` is Hermitian, so `B_p=2W(∂p)` and no `σ_k` occurs. A product of `r` distinct generators, `0<r<20`, is traceless on `S_+`: take `i` in the set and `k` outside; the even unitary `η_iη_k` anticommutes with the product. Hence `{\rm tr}((iη^y_aη^x_b)(iη^y_{a'}η^x_{b'})^†)=512\,δ_{aa'}δ_{bb'}`, and the single-link pairing fixes all corner indices as before. With `a=c`, `b≠d`: `[iη^y_aη^x_d,iη^y_aη^x_b]=-2η^x_bη^x_d`, traceless; pair with `Z=η^x_dη^x_b` to get `-2·512`. Corner indices take ten values, so the choices exist. For (b), `[±iη^y_1η^x_b,A_0]=±2η^x_bη^x_1` for `b≠1`; pair with its adjoint.

*Case `R_s`.* Here `U^{ab}=Σ_μP_μ(e_μ)_{ab}` (`GB1QL.md` line 58), the `P_μ` are Hermitian (Proposition 4.2(a)), and `[P_μ,P_ν]=iL_{μν}/c_s^2` (Proposition 4.2(b)). So `{\rm tr}X_p=Σ_{\boldsymbol\mu}t_p(\boldsymbol\mu)⊗_jP^{(j)}_{μ_j}` with real `t_p=` trace of a product of four unit quaternions, and `B_p=2{\rm tr}X_p`. Let `ℓ` be the shared link. On the six single links take `φ_ℓ=1∈H_0` and `ψ_ℓ=x_{ν_ℓ}∈H_1`; on `ℓ` take `φ_ℓ=x_α`, `ψ_ℓ=x_β`, `α≠β`. Then `ψ_ℓ⊥φ_ℓ` everywhere. Since `P_μ1=x_μ` and `⟨x_ν,x_μ⟩=δ_{μν}/4`, the single links pin the labels. With `L_{μν}=-i(x_μ∂_ν-x_ν∂_μ)`, `⟨x_β,iL_{μν}x_α⟩=\tfrac14(δ_{να}δ_{βμ}-δ_{μα}δ_{βν})`. Hence
\[
\langle\psi,[B_p,B_q]\phi\rangle=\frac{4}{4^{6}}\cdot\frac{1}{4c_s^2}\big(t_p(\beta)t_q(\alpha)-t_p(\alpha)t_q(\beta)\big),
\]
where `t_p(μ)` and `t_q(ν)` are the coefficients with the pinned labels and the free label on `ℓ`. As `μ` runs over `1,…,4`, `t_p(μ)=2⟨Q_p,e_μ⟩` for a unit quaternion `Q_p` fixed by the pins (up to conjugation of `e_μ`). Pinning all single labels of `p` to `4` and those of `q` to `(1,4,4)` makes `Q_p=±1` and `Q_q=±e_1` (up to conjugation), which are not parallel. Choose `(α,β)=(1,4)`. Lemma 1.3(d) gives (c). □

## 2. Literature read

Searches ran on 2026-11-08 (WebSearch, then WebFetch of each abstract page found) for: Trotter error with commutator scaling; anisotropic Wilson actions and the renormalized anisotropy (Karsch; Klassen; Burgers et al.); Creutz's transfer matrix and the Kogut-Susskind limit; heat-kernel actions (Menotti-Onofri; Drouffe); Balaban and the Sussman-Alpoge account; real-time lattice gauge actions; symmetry breaking by the ordering of Trotter factors. Nothing below is a proof step. Every result this file uses is proved in the file or ported from this repository with its path.

| Work | What was fetched | What it says, as fetched | Use here |
|---|---|---|---|
| A. M. Childs, Y. Su, M. C. Tran, N. Wiebe, S. Zhu, "A Theory of Trotter Error", arXiv:1912.08854 (Phys. Rev. X 11, 011020 (2021)) | arXiv abstract page; ar5iv text, characters 0-100000 | Abstract: "Our analysis directly exploits the commutativity of operator summands". Section 1.3 states, for anti-Hermitian summands, additive and multiplicative errors `O(α̃_comm t^{p+1})` with `α̃_comm` a sum of norms of nested commutators `[H_{γ_{p+1}},⋯[H_{γ_2},H_{γ_1}]]`; Section 3.1 states `‖ℳ_1(t)‖=𝒪(‖[B,A]‖t^2)` for `𝒮_1(t)=e^{tB}e^{tA}`. The numbered statement of the main theorem (Theorem 11, Section 3.4) was cut off in the fetch. | Context for section 4.6. The bound used there is rebuilt from `GB1.md` Theorem 2.2. |
| T. R. Klassen, "The Anisotropic Wilson Gauge Action", arXiv:hep-lat/9803010 (Nucl. Phys. B533 (1998) 557) | arXiv abstract page | The renormalized anisotropy `ξ` is determined as a function of the bare `ξ_0` and the coupling from spatial versus temporal static potentials, "to a fraction of 1% at weak coupling"; a parameterization covers `1≤ξ≤6`. Equation numbers not fetched. | Context: anisotropy is renormalized, so a fixed bare calibration does not fix the continuum speed (section 5). |
| F. Karsch, "SU(N) gauge theory couplings on asymmetric lattices", Nucl. Phys. B205 (1982) 285, doi 10.1016/0550-3213(82)90390-X | bibliographic records only | NOT VERIFIED beyond the record. | Credit for the one-loop anisotropic couplings. |
| G. Burgers, F. Karsch, A. Nakamura, I. O. Stamatescu, "QCD on anisotropic lattices", Nucl. Phys. B304 (1988) 587, doi 10.1016/0550-3213(88)90644-X | bibliographic record only | NOT VERIFIED. | Credit only. |
| M. Creutz, "Gauge fixing, the transfer matrix, and confinement on a lattice", Phys. Rev. D 15 (1977) 1128 | OSTI record 7118049, abstract | "We use the transfer-matrix formalism of statistical mechanics to relate Wilson's Lagrangian approach" "and the Kogut-Susskind Hamiltonian approach"; "Taking the timelike lattice spacing to zero, we extract the Kogut-Susskind Hamiltonian" "from the transfer matrix in the gauge A/sub 0/ = 0." Full text NOT VERIFIED. | Credit for the transfer-matrix form of the Wilson action, which Theorem 5.2 rebuilds natively. |
| J. Kogut, L. Susskind, Phys. Rev. D 11 (1975) 395 | not fetched | NOT VERIFIED. | Credit for the Hamiltonian lattice gauge theory that FP's infinite-register target reproduces. |
| P. Menotti, E. Onofri, "The action of SU(N) lattice gauge theory in terms of the heat kernel on the group manifold", Nucl. Phys. B190 (1981) 288; J.-M. Drouffe (1978) | catalogue records only | NOT VERIFIED. | Credit for the heat-kernel action (remark after Theorem 5.2). |
| G. Kanwar, M. L. Wagman, "Real-time lattice gauge theory actions: unitarity, convergence, and path integral contour deformations", arXiv:2103.02602 (Phys. Rev. D 104, 014513) | arXiv abstract page | The Wilson discretization of real-time gauge theory "does not lead to" a unitary real-time theory; a class of real-time actions is "based on analytic continuation of the Euclidean heat-kernel action". | Context for section 5: here the direction is reversed (a unitary tick is continued to a positive transfer). |
| J. Dimock, "The Renormalization Group According to Balaban - II. Large fields", arXiv:1212.5562 | arXiv abstract page | Expository; the fetched abstract treats the scalar `φ^4` model in `d=3`. | Context only. Balaban's Yang-Mills papers and the Sussman-Alpoge account were not fetched; the account is used only through the YM branch's own files (section 7). |
| M. C. Tran, Y. Su, D. Carney, J. M. Taylor, "Faster Digital Quantum Simulation by Symmetry Protection", arXiv:2006.16248 (PRX Quantum 2, 010323) | arXiv abstract page | Symmetry transformations inserted between Trotter steps make errors from different steps partly cancel. | Context: symmetry is restored there on average over steps, not exactly per step (section 4.7). |
| S. Lee, S. Choi, "Mitigating Trotter Errors via Post-Processed Symmetry Restoration", arXiv:2606.20242 | arXiv abstract page | "such Trotterized implementations generally fail to preserve the symmetries of the target Hamiltonian during compilation." | The one-dimensional analogue of Theorem 3.2, stated there without proof in the abstract. |

The prior-work digest records the repository's own one-dimensional warning example: in the two-bond `U(1)` model "the Lie product has `O(h^2)` one-tick summed-energy drift; the palindrome suppresses it to `O(h^3)`" (`prior/LW2M.md` line 26, citing `origin/main:docs/U1_QUANTUM_LINK_EXACT_LOCAL_BACKREACTION_AND_COLORED_FLOQUET_ENERGY_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md:100-105`, ledger "unaudited"). Theorems 4.3 and 4.4 below show the same order pattern for cell covariance: orderings fail at second order, palindromes at third.

## 3. Target 1: the NN-a check of FP

### 3.1 Decomposition, layer count, evenness, gauge invariance

**Theorem 3.1 (FP compiles under NN-a).** On `L5-U[m]`, every `1≤m≤9`, and on `L5-O[S_+]`, for every `θ∈R` and every order of the four factors:

(a) `W_B^{FP}` is the product of eight link-only layers `W_{v,e}=∏_{C∈𝒯_e+v}e^{-i(θ/2)B_C}` and `W_{v,o}=∏_{C∈𝒯_o+v}e^{-i(θ/2)B_C}`, `v∈\{0,e_1,e_2,e_3\}`. The two layers with the same `v` commute.

(b) Each of the eight layers is a composition of `d` layers of pairwise disjoint nearest-neighbour gates, each gate an even unitary in an algebra `𝒢_{w,ℓ}=𝒜_w^+⊗B(H_ℓ)` with `w` a corner of the cube. Each such layer is invariant under `2Z^3`. The number `d=d(\text{law},m,θ)` is the length of one Lemma U word for one cube gate. So FP has depth `8d`, independent of volume.

(c) Every gate is even, `[g,P_xP_y]=0`.

(d) The complete magnetic layer fixes every local gauge generator, and so does every update `W_B^{FP}W_EM_oM_e`.

*Proof.* (a) Section 1.2: `𝒞_v=(𝒯_e+v)∪(𝒯_o+v)`, and cubes of `𝒞_v` have disjoint links. (b) This is the `W^{cube}` part of Proposition C(i) (`GA1_5.md` lines 266-268), translated by `v` or `v+𝟙`: "the gate `e^{−iθB_C}` acts on the twelve links of `C`, a connected set; Lemma U uses sites of `C`; distinct cubes of one tiling have disjoint sites and links." Lemma U (`GA1_5.md` line 236) holds on both laws: its setting states "`dim H_ℓ≥2` (`C(10,m)≥10` on `L5-U`; 512 on `L5-O[S_+]`)". The cubes of `𝒯_e+v` are translates of one another, so one word, translated, serves all of them, and the `j`-th gates of all words form one layer of disjoint gates. (c) `𝒜_w^+` is the even part of the site algebra. (d) `B_C` is gauge invariant (`GA1_5.md` Theorem 3.1), so each cube gate commutes with every local gauge transformation; the base layers do too (`LW1_5.md` section 4). □

The word length `d` is finite but not explicit: Lemma U is an existence argument through the inverse function theorem (`GA1_5.md` Lemma U, Step 4). So the layer count is "eight times one cube word", not a number.

### 3.2 Cell covariance fails

**Theorem 3.2 (FP is not cell covariant at finite register).** Fix `L5-U[m]` (any `m`) or `L5-O[S_+]`, and fix an order `(v_1,v_2,v_3,v_4)` of the labels `0,1,2,3`. There is a closed discrete set `Θ⊂R`, with `0∈Θ`, such that for every `θ∉Θ` the automorphism `β_θ(A)=W_B^{FP*}AW_B^{FP}` does not commute with the lift `α_g` of the quarter-turn `g` about the `e_3`-axis through `c_0`. For `θ∉Θ`, no update `W_B^{FP}W_EM_oM_e` is NN-a admissible. It fails at the clause "It commutes with every cell lift `α_s`".

*Proof.* Put `φ=θ/2`. By Lemma 1.2, `α_g(W_v(φ))=W_{π(v)}(φ)` with `π` exchanging `1` and `2`. So `α_g∘β_θ∘α_g^{-1}=β'_θ`, where `β'` is built from the same order with labels `1` and `2` exchanged. (For a local `A`, `α_g(β_θ(α_g^{-1}A))=α_g(W)^*Aα_g(W)`, and only finitely many gates act.) Covariance at `θ` therefore requires `β_θ(A)=β'_θ(A)` for every local `A`.

*Expansion.* `β_θ=e^{iφD_{v_1}}∘e^{iφD_{v_2}}∘e^{iφD_{v_3}}∘e^{iφD_{v_4}}` with `D_v=[H_v,\,\cdot\,]`, because `W^*AW=W_{v_1}^*⋯W_{v_4}^*AW_{v_4}⋯W_{v_1}`. On a fixed local `A`, every `H_v` may be replaced by the finite sum over the cubes that reach `A` through the four layers. So `Δ_A(φ)=β_θ(A)-β'_θ(A)` is an entire function of `φ` with values in one finite-dimensional algebra. The second-order term of a product of exponentials `∏_ke^{x_k}` is `\tfrac12(Σ_kx_k)^2+\tfrac12Σ_{j<k}[x_j,x_k]`. The first part is the same for both orders. Since `[D_u,D_v]=[[H_u,H_v],\,\cdot\,]`,
\[
\Delta_A(\varphi)=-\frac{\varphi^2}{2}\,[K,A]+O(\varphi^3),\qquad K=\sum_{u<v}b_{uv}[H_u,H_v],\qquad b_{uv}=\epsilon_{uv}-\epsilon_{\pi u,\pi v},
\]
where `ε_{uv}=+1` if `u` comes before `v` in `(v_1,…,v_4)` and `-1` otherwise. With `π=(12)`: `b_{12}=2ε_{12}`, `b_{01}=-b_{02}=ε_{01}-ε_{02}`, `b_{13}=-b_{23}=ε_{13}-ε_{23}`, `b_{03}=0`.

*One nonzero component.* Take a `(1,2)`-plaquette `p` with base `y`, `y_1≢y_2`, so its memberships are `\{1,2\}` (Lemma 1.1). Let `q` be the `(1,3)`-plaquette that contains the link `(y,y+e_1)` and has base `z∈\{y,y-e_3\}` with `z_1≡z_3`; its memberships are `\{0,2\}`. Put `S=∂p∪∂q` (seven links). Since `H_v=Σ_rn_v(r)B_r`,
\[
[H_u,H_v]=\sum_{r,r'}n_u(r)n_v(r')[B_r,B_{r'}].
\]
A term `[B_r,B_{r'}]` is zero unless `r,r'` share a link. Its support has at most seven links, so by Lemma 1.3(e) its `S`-component vanishes unless `∂r∪∂r'=S`, and by Lemma 1.5(i) that forces `\{r,r'\}=\{p,q\}`. Hence `[H_u,H_v]_S=c_{uv}[B_p,B_q]_S` with `c_{uv}=n_u(p)n_v(q)-n_u(q)n_v(p)`. With `n(p)=1_{\{1,2\}}` and `n(q)=1_{\{0,2\}}`: `c_{01}=c_{02}=-1`, `c_{12}=1`, `c_{03}=c_{13}=c_{23}=0`. So
\[
K_S=(-b_{01}-b_{02}+b_{12})[B_p,B_q]_S=2\epsilon_{12}[B_p,B_q]_S .
\]
`ε_{12}=±1` for every order, and `[B_p,B_q]_S≠0` by Lemma 1.6(a). [check: all 24 orders give a nonzero coefficient.]

*Conclusion.* Lemma 1.4 gives a one-link `A` with `[K,A]≠0`. So `Δ_A` is a nonzero entire function, and its real zeros form a closed discrete set `Θ`; `0∈Θ`. For `θ∉Θ`, `β_θ(A)≠β'_θ(A)`. The base tick `U_0=W_EM_oM_e` is covariant (`LW1_5.md` line 276: "the tick automorphism commutes with each lift"). The update's automorphism is `α=α_0∘β_θ` with `α_0` covariant, so `α` is covariant iff `β_θ` is. □

**Remarks.** (1) The angle on `𝒞_0` plays no role: with angle `φ_0` on `𝒞_0` and `φ` on the shifted tilings, the `S`-coefficient is `φ_0φ(-b_{01}-b_{02})+2ε_{12}φ^2=2ε_{12}φ^2`. So the conclusion also holds for the three shifted tilings alone, and for any `φ_0`. (2) Unequal angles `φ_1,φ_2,φ_3` on the shifted tilings already fail at first order: `α_g` exchanges `H_1` and `H_2`, which have different components (a `\{1,3\}`-plaquette `r` has `(H_1)_{∂r}=B_r` and `(H_2)_{∂r}=0`), so `[φ_1H_1+φ_2H_2,\,\cdot\,]` is not invariant unless `φ_1=φ_2`. (3) `Θ` depends on the law, on `m`, on the order and on the chosen `A`. It contains every angle at which all cube gates are scalars, if any. Its full structure is not determined here.

### 3.3 The NN-a check, in one table

| Clause of NN-a (`TOE_ASSEMBLY.md` line 235) | FP on `L5-U[m]` and on `L5-O[S_+]` |
|---|---|
| gates on one edge triple, even | yes (Theorem 3.1(b),(c)) |
| fixed finite number of layers, independent of volume | yes, `8d` (Theorem 3.1(b)) |
| automorphism fixes every local gauge generator | yes (Theorem 3.1(d)) |
| commutes with every cell lift | **no**, for every order and every `θ` outside a closed discrete set (Theorem 3.2) |

So FP is not an admissible magnetic layer of either live law, except possibly at the angles of `Θ`. The prior statement "the ordered product's covariance and exact full-sum form do not follow" (`GB1ISO.md` line 165) is now sharpened for covariance: it fails. `GB1ISO_REFEREE.md` line 119 noted that "cell covariance does not force any shifted tiling. It forces all three once one of them is used". Theorem 3.2 shows that, at finite register, using them in an ordered product breaks cell covariance.

## 4. Target 2: GB1-CF at finite register

### 4.1 What "full plaquette-sum form" can mean

The sources do not fix the phrase. `GB1ISO.md` line 161 uses it on the infinite-register target, where it means `W_B^{FP}=\exp(-iθΣ_pB_p)`. At finite register three readings are natural. Each is a proposed specification, four-tested, not adopted.

- **FS-ex (exact).** On every large even periodic box `Λ_N`, the magnetic layer equals `e^{-iθH_N}`, `H_N=Σ_{p⊂Λ_N}B_p`, up to a phase.
- **FS-sum (written sum).** The law writes the magnetic layer as a product of layers `e^{-iτ_kK_k}` with `Σ_kτ_kK_k=θΣ_pB_p`. This is what R-SUM reads ("For GB1's specified layers \(e^{-i\tau_kK_k}\), set \(H=\sum_k\tau_kK_k\)", `GB1_GEN_OWNER_CHECK.md`).
- **FS-1 (first order).** In the law's one-parameter family of magnetic layers, `W_B(θ)^*AW_B(θ)=A+iθ[Σ_pB_p,A]+O(θ^2)` for every local `A`.

FS-sum implies FS-1 for every word in exponentials of the `K_k`. Four tests (fail = the condition holds): (1) does it state or fix a part's target? (2) is it open-ended? (3) does it settle a downstream question by premise? (4) does it add structure its reasons do not need?

| Reading | 1 | 2 | 3 | 4 | Reason |
|---|---|---|---|---|---|
| FS-ex | P | P | P | P | It restates GB1-CF's comparison target as a question; boxes, operator and phase are fixed; no physics follows from it. |
| FS-sum | P | P | C | P | It reads only written data. Under R-SUM it fixes the Euclidean generator, the same C that R-SUM itself carries (`GB1_GEN_OWNER_CHECK.md` table, row R-SUM, test 3). |
| FS-1 | P | P | P | P | It fixes only the linear term; it is weaker than the other two. |

In every reading the update must also be NN-a admissible, so exactly cell covariant. Sections 4.2-4.5 decide GB1-CF in stated classes. Section 4.6 treats the register size.

### 4.2 The exact form is not of finite depth

**Theorem 4.2 (FS-ex fails).** On `L5-U[m]` (any `m`) and on `L5-O[S_+]` there is a countable set `Θ_X⊂R`, with `0∈Θ_X`, with this property. For `θ∉Θ_X` and every depth `D` there is `N_D` such that, for every even `N≥N_D`, no product `V` of `D` layers of disjoint nearest-neighbour gates on `Λ_N` satisfies `V^*AV=e^{iθH_N}Ae^{-iθH_N}` for every link operator `A`. Hence no NN-a update `W_BW_EM_oM_e` has a magnetic layer of form FS-ex at such `θ`.

*Proof.* (1) *Light cone.* A gate on the triple `(F_x,F_y,H_ℓ)` enlarges the support of an operator by at most that triple. After `D` layers, a link operator on `ℓ_0=(y,y+e_2)` is supported on sites and links within graph distance `D+1` of `y`. Let `B` be the set of links in that ball. A link-only operator in the algebra of the ball lies in `B(H_B)⊗1`.

(2) *An entire function.* Let `E_B` be the normalized partial trace over the links of `Λ_N` outside `B`, and put `f_N(θ)=(1-E_B)(e^{iθH_N}A_0e^{-iθH_N})`, with `A_0` as in Lemma 1.6(b). Then `f_N` is entire, and `f_N(θ)=0` iff the evolved operator lies in `B(H_B)⊗1` (Lemma 1.3(e)). Its Taylor coefficients are `(i^n/n!)(1-E_B)(ad_{H_N}^nA_0)`.

(3) *One coefficient is nonzero.* Let `p_1,…,p_n` be the straight row in the `(1,2)`-plane with bases `y+(k-1)e_1`, so `ℓ_0` is a single side of `p_1`. Take `N>2n+4`, so the row does not wrap. `ad_{H_N}^nA_0` is the sum, over sequences `(q_1,…,q_n)` of plaquettes, of `[B_{q_n},…,[B_{q_1},A_0]…]`. A nonzero term needs `q_1∋ℓ_0` and each `q_{k+1}` to meet the earlier support, so its support has at most `1+3n=|S_n|` links. If its `S_n`-component is nonzero, its support contains `S_n` (Lemma 1.3(e)), hence equals it, so every `q_k` lies in `S_n` and the `q_k` are distinct. By Lemma 1.5(ii) they are the row plaquettes. `ℓ_0` lies only in `p_1`, so `q_1=p_1`; inductively `q_{k+1}` meets `∂p_1∪⋯∪∂p_k` and is new, so `q_{k+1}=p_{k+1}`. So the `S_n`-component of `ad_{H_N}^nA_0` is that of the chain commutator, nonzero by Lemma 1.6(b). Choose `n` with `S_n⊄B` (`n=D+4` works). Since `E_B(X)=Σ_{T⊆B}X_T`, the `n`-th coefficient of `f_N` is nonzero.

(4) *Countable exceptions.* So the real zeros `Z_{N,D}` of `f_N` form a closed discrete set. Put `N_D=2D+14` and `Θ_X=⋃_D⋃_{N≥N_D}Z_{N,D}`, a countable union of countable sets. For `θ∉Θ_X`, `D` and even `N≥N_D`, `f_N(θ)≠0`, so `e^{iθH_N}A_0e^{-iθH_N}` is not supported in `B`, and no depth-`D` circuit reproduces it. For the update: `W_EM_oM_e` has finite depth `D_0` (single-link electric gates; cube matter gates compile by `LW1_5.md` section 7.1, line 323), so an update of depth `D_U` gives `W_B=U(W_EM_oM_e)^{-1}` of depth at most `D_U+D_0`. □

The theorem does not decide the countably many angles in `Θ_X`. It uses only boxes, so it needs no infinite-volume dynamics.

### 4.3 Words in the four tiling layers: a second-order criterion

Let `𝒲` be the class of words `w=W_{i_K}(c_Kφ)⋯W_{i_1}(c_1φ)`, `i_k∈\{0,1,2,3\}`, `c_k∈R`, with total weights `C_v=Σ_{k:i_k=v}c_k` and `C_1=C_2=C_3≠0`. When also `C_0=C_1`, the word satisfies FS-sum and FS-1 with `θ=2C_1φ`, since `Σ_vH_v=2Σ_pB_p` (Lemma 1.1). Every word of `𝒲` is gauge invariant and compiles under NN-a (Theorem 3.1, applied letter by letter); the theorem below does not need `C_0=C_1`. Its automorphism is `β_w=e^{iφc_1D_{i_1}}∘⋯∘e^{iφc_KD_{i_K}}`. Put `a_{uv}=Σ_{j<k,\,i_j=u,\,i_k=v}c_jc_k` and `A_{uv}=a_{uv}-a_{vu}`.

**Theorem 4.3.** On `L5-U[m]` (any `m`) and `L5-O[S_+]`: (a) if `A` is not invariant under the permutations of the labels `1,2,3`, that is, unless `A_{12}=A_{13}=A_{23}=0` and `A_{01}=A_{02}=A_{03}`, then there is a closed discrete set `Θ_w∋0` such that for `φ∉Θ_w` the word is not cell covariant. (b) If `A` is invariant, the covariance defect `β_w(A')-β_{π w}(A')` is `O(φ^3)` for every local `A'` and every `π`.

*Proof.* As in Theorem 3.2, `α_g(w)=π_g w` (letters relabelled), and the second-order term of `∏e^{x_k}`, `x_k=iφc_kD_{i_k}`, is `\tfrac12(Σ_kx_k)^2+\tfrac12Σ_{j<k}[x_j,x_k]`, and `\tfrac12(Σ_kx_k)^2=-\tfrac{φ^2}{2}(Σ_vC_vD_v)^2`. This first part is the same for `w` and `πw` because `C_1=C_2=C_3`. The second part is `-\tfrac{φ^2}2[Σ_{u<v}A_{uv}[H_u,H_v],\,\cdot\,]`. So the defect for `π` is `-\tfrac{φ^2}{2}[K_π,\,\cdot\,]+O(φ^3)` with `K_π=Σ_{u<v}d_{uv}[H_u,H_v]`, `d_{uv}=A_{uv}-A_{π^{-1}u,π^{-1}v}`. This proves (b).

For (a), let `d≠0`. For two plaquettes `r,r'` sharing one link, with membership pairs `P,Q`, the argument of Theorem 3.2 gives `(K_π)_{∂r∪∂r'}=⟨d,f_P∧f_Q⟩[B_r,B_{r'}]_{∂r∪∂r'}`, where `f_P=Σ_{u∈P}e_u∈R^4`, `(x∧y)_{uv}=x_uy_v-x_vy_u`, and `⟨d,c⟩=Σ_{u<v}d_{uv}c_{uv}`. Which pairs `(P,Q)` occur? Two perpendicular plaquettes in the `(1,2)`- and `(1,3)`-planes sharing a direction-1 link occur with all four combinations `P∈\{03,12\}`, `Q∈\{02,13\}`: vary the base `y` and the side `z∈\{y,y-e_3\}` (Lemma 1.1). Likewise `(1,2)`/`(2,3)` give `\{03,12\}×\{01,23\}` and `(1,3)`/`(2,3)` give `\{02,13\}×\{01,23\}`. With `s=(1,1,1,1)` and `f_{12}=s-f_{03}`, `f_{13}=s-f_{02}`, `f_{23}=s-f_{01}`, the four wedges of the first family span `\{f_{03}∧f_{02},f_{03}∧s,s∧f_{02}\}`; the other families add `f_{03}∧f_{01}`, `s∧f_{01}`, `f_{02}∧f_{01}`. These are the six wedges of `f_{01},f_{02},f_{03},s`, a basis of `R^4` (`f_{01}+f_{02}+f_{03}-s=2e_0`). So they span `Λ^2R^4`, and some occurring pair has `⟨d,f_P∧f_Q⟩≠0`. Lemma 1.6(a) and Lemma 1.4 give a one-link `A'` with `[K_π,A']≠0`, and the defect is a nonzero entire function of `φ`. Finally `d=0` for all `π` iff `A` is invariant: the transposition `(12)` forces `A_{12}=-A_{12}=0` and `A_{01}=A_{02}`, and the others likewise. □

**Corollary 4.3.1.** (i) All 24 orders of FP fail (here `A_{uv}=ε_{uv}`), as in Theorem 3.2. (ii) The Lie-Trotter product `(W_{v_4}(φ/n)⋯W_{v_1}(φ/n))^n` fails for every `n≥1` and every order: cross-step pairs add the same amount to `a_{uv}` and `a_{vu}`, so `A_{uv}=ε_{uv}/n`.

### 4.4 Symmetrised orderings: the palindromes fail at third order

Palindromic words have `A=0` and pass Theorem 4.3(b). The natural symmetrised orderings are the nested palindromes
\[
P(i_1,i_2,i_3,i_4)=W_{i_1}(\tfrac\varphi2)W_{i_2}(\tfrac\varphi2)W_{i_3}(\tfrac\varphi2)W_{i_4}(\varphi)W_{i_3}(\tfrac\varphi2)W_{i_2}(\tfrac\varphi2)W_{i_1}(\tfrac\varphi2),
\]
with `(i_1,…,i_4)` an order of `0,1,2,3`. They satisfy FS-sum. The second-order Trotter-Suzuki products are `P(φ/n)^n`.

**Lemma 4.4.1 (symmetric BCH to third order).** For formal power series in `t` over an associative algebra, `\log(e^{tX/2}e^{tY}e^{tX/2})=t(X+Y)+t^3c(X,Y)+O(t^5)`, with `c(X,Y)=-\tfrac1{24}[X,[X,Y]]-\tfrac1{12}[Y,[X,Y]]`. If `\log M(t)=tY+t^3R+O(t^5)` and `M(-t)=M(t)^{-1}`, then `\log(e^{tX/2}M(t)e^{tX/2})=t(X+Y)+t^3(R+c(X,Y))+O(t^5)`.

*Proof.* Expanding `e^ae^b` to third order and using `\log(1+z)=z-z^2/2+z^3/3` gives `\log(e^ae^b)=a+b+\tfrac12[a,b]+\tfrac1{12}([a,[a,b]]+[b,[b,a]])+O(4)`. With `a=tX/2`, `b=tY`: `W:=\log(e^{tX/2}e^{tY})=\tfrac{tX}2+tY+\tfrac{t^2}4[X,Y]+t^3(\tfrac1{48}[X,[X,Y]]+\tfrac1{24}[Y,[Y,X]])+O(4)`. Apply the formula again to `\log(e^We^{tX/2})`. The cross terms are `\tfrac t4[W,X]=-\tfrac{t^2}4[X,Y]-\tfrac{t^3}{16}[X,[X,Y]]`, `\tfrac{t}{24}[W,[W,X]]=-\tfrac{t^3}{48}[X,[X,Y]]+\tfrac{t^3}{24}[Y,[Y,X]]` and `\tfrac{t}{48}[X,[X,W]]=\tfrac{t^3}{48}[X,[X,Y]]`, up to `O(4)`. Summing, the `t^2` terms cancel; the coefficient of `t^3[X,[X,Y]]` is `\tfrac1{48}-\tfrac1{16}=-\tfrac1{24}`, and that of `t^3[Y,[Y,X]]` is `\tfrac1{24}+\tfrac1{24}=\tfrac1{12}`. The product `Q(t)` satisfies `Q(-t)=Q(t)^{-1}`, so its logarithm is odd and the `t^4` term vanishes. For the second claim, replace `tY` by `\log M(t)`; `R` enters linearly at order `t^3`, and the cubic cross terms involve only the linear parts. □ [check: for random `4×4` matrices the remainder divided by `t^5` is constant, `0.264` at `t=0.1` and `0.05`.]

**Theorem 4.4 (palindromes and Strang products).** On `L5-U[m]` (any `m`) and `L5-O[S_+]`, for each of the 24 nested palindromes and each `n≥1`, there is a closed discrete set `Θ∋0` such that for `φ∉Θ` the layer `P(φ/n)^n` is not cell covariant.

*Proof.* *Logarithm.* On a fixed local operator all series are finite-dimensional, and `D_v=[H_v,\,\cdot\,]` generates a Lie algebra in which `[D_u,[D_v,D_w]]=[[H_u,[H_v,H_w]],\,\cdot\,]`. By Lemma 4.4.1 applied three times (innermost first), `\log β_P=iφΣ_vD_v+(iφ)^3L_3+O(φ^5)`, with
\[
L_3=c(D_{i_3},D_{i_4})+c(D_{i_2},D_{i_3}+D_{i_4})+c(D_{i_1},D_{i_2}+D_{i_3}+D_{i_4}).
\]
For `P(φ/n)^n` the cubic term is `(iφ)^3L_3/n^2`. For a label permutation `π`, `β_P` and `β_{πP}` agree to second order, so their difference on a local `A'` is `(iφ)^3n^{-2}[K_3,A']+O(φ^4)`, where `K_3` is the degree-3 Lie polynomial in the `H_v` that gives `L_3-πL_3`.

*Component on a row.* Let `p,q,r` be the straight row in the `(1,2)`-plane with bases `y,y+e_1,y+2e_1`, `y_1≢y_2`. By Lemma 1.1, `n(p)=n(r)=a:=1_{\{1,2\}}` and `n(q)=b:=1_{\{0,3\}}`. Let `S=∂p∪∂q∪∂r` and `Y=[B_p,[B_q,B_r]]`. In `[H_u,[H_v,H_w]]=Σn_u(r_1)n_v(r_2)n_w(r_3)[B_{r_1},[B_{r_2},B_{r_3}]]`, a term with nonzero `S`-component has support `S`, because a nonzero triple commutator of plaquettes has at most ten links and `S` has ten, so `\{r_1,r_2,r_3\}=\{p,q,r\}` by Lemma 1.5(ii). Using `[B_p,B_r]=0` and the Jacobi identity, the six orders give `Y,-Y,0,0,-Y,Y`, so
\[
[H_u,[H_v,H_w]]_S=\Gamma_{uvw}Y_S,\qquad \Gamma_{uvw}=n_u(p)\big(n_v(q)n_w(r)-n_v(r)n_w(q)\big)-n_u(r)\big(n_v(p)n_w(q)-n_v(q)n_w(p)\big)=2a_u\,s(v,w),
\]
with `s(v,w)=b_va_w-a_vb_w`: `+1` if `v∈\{0,3\}`, `w∈\{1,2\}`; `-1` if `v∈\{1,2\}`, `w∈\{0,3\}`; `0` otherwise. `Y_S≠0` by Lemma 1.6(a) (the chain `r,q,p`). For `W⊆\{0,1,2,3\}`, the `S`-coefficient of `c(H_u,Σ_{w∈W}H_w)` is therefore
\[
k(u,W)=-\tfrac1{12}\Big(a_u+2\sum_{w\in W}a_w\Big)\sum_{w\in W}s(u,w),
\]
and `L_3` has coefficient `κ(i_1,i_2,i_3,i_4)=k(i_3,\{i_4\})+k(i_2,\{i_3,i_4\})+k(i_1,\{i_2,i_3,i_4\})`.

*Four cases.* Take `π=(13)`. Direct evaluation of `k`:

| order | `κ(order)` | `κ(π·order)` | difference |
|---|---|---|---|
| `(0,1,2,3)` | `-2/3+1/4+1/12=-1/3` | `(0,3,2,1)`: `-2/3-2/3+0=-4/3` | `1` |
| `(1,0,2,3)` | `1/2-1/6+1/12=5/12` | `(3,0,2,1)`: `-2/3-2/3+0=-4/3` | `7/4` |
| `(1,2,0,3)` | `1/2+1/6+0=2/3` | `(3,2,0,1)`: `-2/3+1/4-1/6=-7/12` | `5/4` |
| `(1,2,3,0)` | `1/2+1/6+0=2/3` | `(3,2,1,0)`: `-2/3+1/4+1/12=-1/3` | `1` |

So `(K_3)_S≠0` in each case, Lemma 1.4 gives `A'` with `[K_3,A']≠0`, and the defect is a nonzero entire function of `φ`. *All 24 orders.* Two orders with `0` in the same position differ by a permutation `ρ` of the labels `1,2,3`, realized by a cell rotation `g_ρ` (Lemma 1.2), and `P_{ρ\cdot o}=α_{g_ρ}(P_o)`. If `Ad(P_{ρ·o})` commuted with every lift, so would `Ad(P_o)=α_{g_ρ}^{-1}Ad(P_{ρ·o})α_{g_ρ}`; on link operators the lifts compose as a group action, because the site-sign automorphisms of `LW1_5.md` line 276 act only on matter. The table covers the four positions of `0`. □ [check: the script reproduces the table and confirms that every one of the 24 orders is detected by this row and some transposition.]

### 4.5 Covariant layers of disjoint gates miss the mixed plaquettes

Let `𝒟` be the class of magnetic layers `W_r⋯W_1`, `W_s=∏_{X∈ℱ_s}e^{-iφ_Xh_X}`, where each `ℱ_s` is a cell-invariant, locally finite family of pairwise disjoint finite link sets, each `h_X` is a Hermitian gauge-invariant link operator supported on `X`, `α_g(h_X)=h_{gX}` and `φ_{gX}=φ_X`. This is the part of the proposed class GA1-P-5 (`GA1_5.md` line 52) with disjoint supports and exponential gates. It contains the cube-face layer `W^{cube}`. Every member is gauge invariant, cell covariant (each `W_s` is), and compiles under NN-a (`GA1_5.md` Proposition C(ii)).

**Theorem 4.5.** On `L5-U[m]` (any `m`) and `L5-O[S_+]`, for every member of `𝒟` and every choice of angles, the written sum `Σ_sΣ_{X∈ℱ_s}φ_Xh_X` has zero `∂p`-component for every mixed plaquette `p`. Since `(θΣ_{p'}B_{p'})_{∂p}=θB_p≠0`, no member of `𝒟` meets FS-sum or FS-1 at any `θ≠0`.

*Proof.* `GA1_5.md` Theorem 2.2 (line 77): "Let `ℱ` be a cell-invariant family of pairwise disjoint finite link sets. At any site, a nonempty intersection of a member with the six-link star is a single link, the even triple or the odd triple." A mixed plaquette (`GA1_5.md` line 48: a plaquette's type is "the unordered pair of its two in-plane base parities") in the `(i,j)`-plane with base `y` has `y_i≢y_j`. At its corner `y` its links `(y,y+e_i)` and `(y,y+e_j)` are an even and an odd link ("An `i`-link is even or odd according to `x_i mod 2`", line 48). So no member of `ℱ_s` contains `∂p`. By Lemma 1.3(c), `(h_X)_{∂p}=0` for every `X`. For the last claim: every entry of `B_p` is traceless on its link (it changes an end number, or it is a product of two distinct `η`'s), so `(B_p)_{∂p}=B_p`, and the pairing of Lemma 1.6 shows `B_p≠0`. □

The result needs no condition on the angles and no exceptional set. It does not cover sublayers whose gates overlap and commute, which GA1-P-5 allows (`GA1_5.md` line 89: "Overlapping supports with commuting gates are not ruled out").

### 4.6 Error bounds in the register size

The live registers are fixed, so a register-size bound needs a register family. The one on file is `GB1QL.md`'s SU(2) family `R_s` in the rung test law `L5[SU(2),s]` (`GB1QL.md` section 4.11; a test law, not a working-set law).

**Proposition 4.6.** On `L5[SU(2),s]` with FP at angle `θ` (any order):

(a) For every `s≥1` there is a closed discrete set `Θ_s∋0` such that FP is not cell covariant for `θ∉Θ_s`.

(b) On the even box `Λ_N`, `‖W_B^{FP}-e^{-iθH_N}‖≤27C_0θ^2N^3/s` and `‖α_g(W_B^{FP})-W_B^{FP}‖≤54C_0θ^2N^3/s` for every `g∈𝒢`, with `C_0=2^{20}`.

*Proof.* (a) The proof of Theorem 3.2 uses three inputs: Lemma 1.2, the identity `α_g(B_C)=B_{gC}`, and the nonvanishing of `[B_p,B_q]_S`. The first is geometric. The second is the cube-face covariance of `GB1QL.md` Proposition 4.11(b)-(c) ("Orientation reversal `U_ℓ ↦ U_ℓ^*` is implemented on `R_s` by a unitary"; "cell covariance, hold as in `GB1.md` Theorem 5M(1)"), applied to the translated tilings. The third is Lemma 1.6(c). Lemmas 1.3 and 1.4 hold for any finite registers.

(b) `B_p=2{\rm tr}X_p=2Σ_{\boldsymbol μ}t_p(\boldsymbol μ)⊗_jP_{μ_j}` has `4^4` terms with `|t_p|≤2` (the trace of a unit quaternion), and `‖P_μ‖≤1` because `Σ_μP_μ^2≤1` (`GB1QL.md` Proposition 4.2(c)). For `p,q` sharing one link, `[B_p,B_q]` has `4^8` terms, each the product of single-link factors of norm at most one and one factor `[P_μ,P_ν]=iL_{μν}/c_s^2`. On `H_k`, `L_{μν}` acts on degree-`k` harmonic polynomials; in the variable `z=x_μ+ix_ν` it acts as `z∂_z-\bar z∂_{\bar z}` up to sign, whose eigenvalues lie in `[-k,k]`. So `‖[P_μ,P_ν]‖≤s/(s(s+3))<1/s`, and `‖[B_p,B_q]‖≤4·4^8·2·2/s=2^{20}/s`. A plaquette shares a link with at most 12 others, and `Λ_N` has `3N^3` plaquettes, so `‖[H_u,H_v]‖≤36N^3C_0/s`. `GB1.md` Theorem 2.2 (line 58): "\(\|e^Ae^B-e^{A+B}\|\le\tfrac12\|[A,B]\|\)" for skew-Hermitian `A,B`. Combining the four factors one at a time gives `‖∏_ke^{-iφH_{v_k}}-e^{-iφΣ_vH_v}‖≤\tfrac{φ^2}2Σ_{u<v}‖[H_u,H_v]‖`. Here `Σ_vH_v=2H_N` (each plaquette has two memberships) and `φ=θ/2`, which gives the first bound. `e^{-iθH_N}` is cell covariant, so the second bound follows from the first by the triangle inequality. □

So on this family FP's covariance defect and its full-sum defect both vanish like `1/s` on each fixed box. Exact covariance, which NN-a requires of each law, still fails at every finite `s` (part (a)). FP therefore meets GB1-CF "with an error bound in the register size" only under a relaxed covariance clause. That clause is a reading change; section 6 states it (R-COV_s) and four-tests it. The volume factor `N^3` comes from operator norms on the whole box. A volume-uniform local bound would need a light-cone bound for `e^{-iθH_N}`, which is not proved here.

### 4.7 The remaining words: an open lemma

**LW2M-WORD (open).** For every word of `𝒲` (section 4.3), on `L5-U[m]` and `L5-O[S_+]`, there is a closed discrete set of `φ` outside which the word is not cell covariant.

Proved cases: every word whose order matrix `A` is not invariant (Theorem 4.3), all 24 nested palindromes and their Strang products (Theorem 4.4). Two natural words are not covered: Suzuki's fourth-order product `S_4(φ)=P(s_1φ)^2P((1-4s_1)φ)P(s_1φ)^2` with `4s_1^3+(1-4s_1)^3=0`, and the cell-averaged product of the six FP orders that put `0` first, each at angle `φ/6` (its order matrix is invariant: within the six blocks each pair of labels from `1,2,3` occurs in both orders, and cross-block pairs cancel). Three attacks failed.

1. *Order-by-order BCH with chain components* (the method of Theorems 3.2, 4.3, 4.4). For a fixed word it works at the first order where the logarithms of `w` and `πw` differ, provided the difference has a nonzero chain component. It fails as a general argument at the step "the first differing order is bounded". For `S_4` the cubic term is `(Σ_ks_k^3)L_3=0` and the quartic term vanishes because the word is a palindrome, so the first possible defect is at order five. It needs the degree-five Lie polynomial of `S_4` and a degree-five chain component, which this file does not compute. Higher Suzuki orders push the first possible defect to order `2k+1`.
2. *Reduced words in a free product.* In the free product of the four one-parameter groups, a reduced word with a letter from `\{1,2,3\}` is never fixed by a nontrivial label permutation, because relabelling changes that letter. Transferring this to automorphisms needs the map from the free product into automorphisms of the link algebra to separate the word from its relabelled copy. That is a freeness property of the derivations `D_0,…,D_3`. This file proves the needed separation only through the chain functionals of degrees two and three. The attack fails at freeness in degrees four and above.
3. *Light-cone shapes at finite angle.* A word has a combinatorial light cone from each link: grow by the cubes of each letter's tiling, in order. Covariance forces the actual light cones to be covariant. If the actual support equals the combinatorial one, a non-covariant combinatorial shape refutes covariance, by the analytic argument of Theorem 4.2. The attack fails at the step "actual support equals combinatorial support": that needs nonvanishing of components along the boundary chains of the light cone, and those chains turn corners, so they are not pinned. Lemma 1.6 covers only pinned chains.

### 4.8 Verdict on GB1-CF at finite register

**Corollary 4.8.1.** On `L5-U[m]` and `L5-O[S_+]`, `H_B=Σ_pB_p` is not a sum of pairwise commuting gauge-invariant terms with bounded supports, periodic under `2Z^3`.

*Proof.* If it were, `e^{-iθH_N}` would be a product of commuting gates of finitely many types, each compiled by Lemma U into a word of bounded length, and Proposition C(ii)'s scheduling would give a depth independent of `N`, for every `θ`. This contradicts Theorem 4.2 at any `θ∉Θ_X`. □

**Verdict.** In reading FS-ex, GB1-CF is refuted on both live laws for every `θ` outside a countable set (Theorem 4.2). In readings FS-sum and FS-1, with the exact cell covariance NN-a requires, no admissible magnetic layer exists in these stated classes: FP in all 24 orders, Lie-Trotter products, every word with a non-invariant order matrix, all nested palindromes and their Strang products (each outside a closed discrete angle set; Theorems 3.2, 4.3, 4.4), and every covariant layer of disjoint gates (at every angle; Theorem 4.5). The remaining words form the open lemma LW2M-WORD. General NN-a circuits outside these classes are not decided. With an error bound in the register size, FP works on `GB1QL.md`'s family only if exact covariance is relaxed (Proposition 4.6).

## 5. Target 3: ISO-FP under R-SUM and R-IA

### 5.1 The lifts under FP

ISO-FP lives where GB1ISO's lifts live: the infinite-register target of `GB1QL.md`'s SU(2) family, on even tori `(Z/NZ)^3×Z/N_tZ`. There all `B_C` commute and `W_B^{FP}=e^{-iθH_B}`, `H_B=Σ_pB_p` over all spatial plaquettes (`GB1ISO.md` Theorem 6.1). An electric layer is `∏_ℓe^{-iτG_ℓ}` with `G=Σ_kg_kΠ_k` a real function of the flux; GB1QL's layer is `G=E^2` (`g_k=k(k+2)/4`), `τ=τ_E`. The readings give
\[
\text{R-SUM: } T=e^{-a_0H},\ H=\tau\textstyle\sum_\ell G_\ell+\theta H_B;\qquad
\text{R-IA: } T_{\rm loc}=e^{-\lambda\theta H_B/2}e^{-\lambda\tau\sum_\ell G_\ell}e^{-\lambda\theta H_B/2}.
\]
The lift is the transfer-kernel lift of `GB1E.md` line 29: "the normalized product of \(\kappa(U_t,V_t\cdot U_{t+1})\) against Haar measure on all spatial links \(U_t\) and temporal links \(V_{x,t}\)", with `(h·U)_{xy}=h_y^{-1}U_{xy}h_x`. For `G=E^2` the R-IA lift has heat-kernel weights on temporal plaquettes and Wilson weights `e^{βTr X_p}` on every spatial plaquette, `β=-2λθ` (`GB1E.md` lines 33-37 with `CF` replaced by all plaquettes).

### 5.2 R-SUM: the exact lift under FP is not exchange invariant

GB1ISO left this open (`GB1ISO.md` line 167: "Finite-torus exchange invariance for R-SUM under FP is also open; Theorem 4.1 relied on the non-translation-invariant cube-face set and does not apply").

**Theorem 5.1.** Let `G=E^2`, `τ_E,a_0>0`, and `N=N_t≥4` even. The exact R-SUM lift under FP is invariant under a lattice isometry exchanging time with a spatial axis for at most a discrete set of `θ∈R∖\{0\}`.

*Proof.* *Lift and expectations.* `GB1E.md` Theorem 3.2 builds the exact lift for `V_θ=θH_B^{CF}` as a limit of local lifts. Its proof (line 78) uses `V_θ` only as a bounded, real, smooth, gauge-invariant multiplication operator: "The product rule for \(A=-\frac14\sum D_i^2\) gives \(\|[A,f]z\|\le C_f(\|z\|+\|Az\|)\) for smooth \(f\)." `θH_B^{FP}` has the same properties, so the exact lift exists for FP, and its transfer is `T=e^{-a_0H}`. `GB1ISO.md` Theorem 2.4 then gives, for a window observable, `𝔼F={\rm Tr}(𝔉T^{N_t-w}P_0)/{\rm Tr}(T^{N_t}P_0)`.

*The function `Δ`.* Let `p_s` be a spatial `(1,2)`-plaquette at slice `0`, and `p_t` the temporal plaquette over the link `ℓ=(x,x+e_2)` between slices `0` and `1`. Put `Δ(θ)=𝔼_θ{\rm Tr}X_{p_s}-𝔼_θ{\rm Tr}X_{p_t}`. In temporal gauge, `{\rm Tr}W_{ℓ,0}=Σ_{ab}\overline{U'_{ab}}U_{ab}` for the two slice values `U,U'` of the link `ℓ`. So
\[
\mathbb E_\theta{\rm Tr}X_{p_s}=\frac{{\rm Tr}(M T^{N_t}P_0)}{Z},\qquad
\mathbb E_\theta{\rm Tr}X_{p_t}=\frac{{\rm Tr}\big((\sum_{ab}M_{ab}^*TM_{ab})T^{N_t-1}P_0\big)}{Z},\qquad Z={\rm Tr}(T^{N_t}P_0)>0,
\]
with `M` the multiplication by `{\rm Tr}X_{p_s}` and `M_{ab}` the multiplication by the matrix entry `(U_ℓ)_{ab}`.

*Analyticity.* `GB1E.md` Theorem 7.2's proof (line 158): "The Duhamel series for the finite-box Gibbs trace is entire in θ: in the m-th term one heat segment has length at least \(N_ta_0/(m+1)\), and \(\Theta(u)=O(1+u^{-3/2})\), which leaves a summable factorial bound." The same bound applies to each trace above, with `H_B^{FP}` bounded. So numerators and `Z` are entire, `Z>0` on `R`, and `Δ` is real-analytic on `R`.

*`Δ(0)<0`.* At `θ=0`, `T=⊗_ℓe^{-a_0τ_EE_ℓ^2}` preserves every flux sector, and so does `P_0` (gauge transformations act on each link by translations, which preserve each `H_k`). Multiplication by an entry of `U` maps `H_k` into `H_{k-1}⊕H_{k+1}` (`GB1QL.md` Lemma 4.1(a)). So `M` changes the flux parity of four links, and `{\rm Tr}(MT^{N_t}P_0)=0`. On the link `ℓ`, `Σ_{ab}M_{ab}^*e^{-uE^2}M_{ab}` (`u=a_0τ_E`) is convolution by `f=χ_{1/2}k_u`, where `k_u=Σ_j(j+1)e^{-uj(j+2)/4}χ_{j/2}` is the heat kernel. By `χ_{1/2}χ_{j/2}=χ_{(j+1)/2}+χ_{(j-1)/2}`, `f` acts on `H_k` by
\[
\frac{k\,e^{-u(k-1)(k+1)/4}+(k+2)\,e^{-u(k+1)(k+3)/4}}{k+1}>0 .
\]
So `X=(Σ_{ab}M_{ab}^*TM_{ab})T^{N_t-1}` is a positive definite trace-class operator that commutes with `P_0`, and `{\rm Tr}(XP_0)={\rm Tr}(P_0XP_0)>0` because `P_0≠0`. Hence `Δ(0)<0`.

*Invariance forces `Δ=0`.* Let `ι` be a lattice isometry of the torus that maps the time axis to a spatial axis `j_0`. Then `ι^{-1}` maps `j_0` to time and maps the other two spatial axes to spatial axes. So `ι^{-1}` maps a spatial `(j_0,j_1)`-plaquette to a temporal plaquette. `{\rm Tr}` is invariant under orientation reversal of the plaquette, so invariance gives equal expectations. Under FP, `H` is invariant under the spatial translations and cubic rotations, so all spatial plaquettes have one expectation and all temporal plaquettes have another. So invariance at `θ` gives `Δ(θ)=0`. A nonzero real-analytic function has isolated zeros. □

So the time-space exchange `ς`, which is also RO1's diagonal mirror (`GB1E_REFEREE.md` line 143: "The diagonal mirror `x_1 ↔ t` is the exchange `ς` itself"), fails for the FP R-SUM lift at every `θ` outside a discrete set.

### 5.3 R-IA with a Wilson-dual electric function: the lift is T0's measure

`GB1E.md` Theorem 7.1 (lines 145-150) gives the Wilson multipliers: "convolution by a class function \(f\) acts on \(H_k\) by \(c_k(f)=(k+1)^{-2}\int fz_k\,dU\)", and "\(c_k(e^{b\operatorname{Tr}})=\frac{I_{k+1}(2b)}b\quad(b\ne0)\)". Line 180 records "The normalized Wilson temporal multipliers are \(I_{k+1}(x_0)/I_1(x_0)\)". This fixes an electric function whose Euclidean partner is a Wilson weight.

**Definition (Wilson-dual electric function).** For `b>0` let `G_b=Σ_kγ_k(b)Π_k` with `γ_k(b)=-\log\big(I_{k+1}(2b)/I_1(2b)\big)`. All `I_j(2b)>0` (power series with positive terms), so `G_b` is a real function of the flux, and `e^{-iτG_b}` is a gauge-invariant single-link unitary.

**Theorem 5.2.** On the infinite-register target take the magnetic layer FP at angle `θ` and the electric layer `∏_ℓe^{-iτG_{b,ℓ}}`, `τ>0`. Under R-IA with `λ=1/τ` and `θ=-bτ/2`, the local lift on `(Z/NZ)^3×Z/N_tZ` (`N≥4`, `N_t≥2` even) has density proportional to `∏_Pe^{b{\rm Tr}U_P}` against Haar measure, the product running over all spatial and temporal plaquettes. It is the isotropic Wilson SU(2) measure with T0's weight `e^{(x_0/2){\rm Tr}W}` at `x_0=2b`. For `N=N_t` it is invariant under every lattice isometry of the four-torus.

*Proof.* `e^{-G_b}` acts on `H_k` by `I_{k+1}(2b)/I_1(2b)=c_k(w_b)` with `w_b=(b/I_1(2b))e^{b{\rm Tr}}`, so it is convolution by the positive continuous class function `w_b` (both operators are diagonal on `⊕̂_kH_k`, which is dense by `GB1QL.md` R2). With `λτ=1` and `-λθ/2=b/4`, and `H_B=Σ_p2{\rm Tr}X_p`,
\[
T_{\rm loc}=e^{\frac b4H_B}e^{-G_b}e^{\frac b4H_B},\qquad
\kappa(U,U')=\prod_pe^{\frac b2{\rm Tr}X_p(U')}\prod_\ell w_b\big(U'_\ell U_\ell^{-1}\big)\prod_pe^{\frac b2{\rm Tr}X_p(U)} .
\]
In the product of `κ(U_r,V_r·U_{r+1})` over slices, each spatial plaquette at slice `r` collects `e^{\frac b2{\rm Tr}X_p(U_r)}` from two neighbouring factors (a gauge transformation does not change plaquette traces), so `e^{b{\rm Tr}X_p(U_r)}`. The factor for `(ℓ,r)` is `w_b(V_{y,r}^{-1}U_{ℓ,r+1}V_{x,r}U_{ℓ,r}^{-1})`, whose trace argument is cyclically equal to `W_{ℓ,r}^{-1}`, with `W_{xy,r}=V_{x,r}^{-1}U_{xy,r+1}^{-1}V_{y,r}U_{xy,r}` (`GB1E.md` line 36), and `{\rm Tr}W^{-1}={\rm Tr}W` on SU(2). Each temporal plaquette is one pair `(ℓ,r)`. So the density is `∏_Pe^{b{\rm Tr}U_P}` up to a positive constant. A lattice isometry permutes the plaquettes and preserves Haar measure. □

This is Creutz's transfer-matrix form of the Wilson action (credited in section 2), read backwards: the law's tick is the unitary member of the family whose R-IA continuation is Creutz's transfer. The construction needs the infinite-register target. At finite register the lifts are signed for small Euclidean step (`GB1.md` line 11, Amendment 3: "at fixed `s` its lifts are signed for small `a₀`"), and FP is not covariant (Proposition 4.6(a)).

**Corollary 5.3 (ISO-FP for the Wilson-dual family is T0's question).** Call ISO-FP[W] the statement ISO-FP for FP with the electric layer `G_b` under R-IA (`λ=1/τ`, `θ=-bτ/2`, `b` along a trajectory). (a) Its lifts are finite-torus Wilson measures, invariant under every lattice isometry when `N=N_t` (Theorem 5.2). LG1 Theorem 10 (YM `library/lg1.md` line 365) gives, for every periodic Wilson DLR state at `β>0`, invariance and reflection positivity "at every admissible mirror", including diagonal mirrors. RO1's H-L is stated for such periodic states, so it holds for the volume-first limits of these lifts; for the finite straight torus itself the YM branch makes "No assertion of diagonal RP" (`library/t0-tree.md` line 166). With `G=E^2`, H-L failed for every FP lift. (b) Theorem O4-2 (YM `library/o4-two-point.md` line 188) applies verbatim: "for every volume-first limit \(S_2\in\mathfrak V\) through torus-limit Wilson DLR states at CA's first-passage data, the connected plaquette-action-density two-point function is O(4)-invariant on real compact \(C^1\) tests with disjoint supports." Its inputs are CA (iii-b) and CA (iv), which the YM branch records as "proved as implications, with named outstanding items". So the two-point part of ISO-FP[W] holds with `c=1`, conditional on exactly those inputs. (c) The rest of ISO-FP[W] (non-triviality, higher points, the rate `O((a/r)^p)`) is T0's own content with T0-rate; no anisotropic request is needed.

*Proof.* (a) and (b) follow from Theorem 5.2: the lifts are the measures those theorems treat, and volume-first limits of them are the states those theorems quantify over. (c) is a restatement. □

### 5.4 First failing steps, per reading

| Reading and electric layer | Lattice measure under FP | Exchange and diagonal mirrors (RO1 H-L) | First failing step for ISO-FP |
|---|---|---|---|
| R-IA, `G=E^2` (GB1QL's layer) | heat-kernel in time, Wilson on all spatial plaquettes | fail at every `(β,t)` (`GB1ISO.md` Theorem 6.1) | H-L. Any route must then pass through the anisotropic request T0-start^an (Y-a to Y-d of `GB1ISO.md` §6), which is not available. |
| R-SUM, `G=E^2` | exact semigroup lift | fail for `θ` outside a discrete set (Theorem 5.1) | H-L, generically. The exact lift "need not have a finite plaquette-product action" (`GB1E.md` line 180), so the action-class step (Y2) is also unaddressed. |
| R-IA, `G=G_b`, `λ=1/τ`, `θ=-bτ/2` | isotropic Wilson (Theorem 5.2) | hold (LG1 Theorem 10) | Two-point isotropy holds conditionally (Corollary 5.3(b)). The first failing step is T0 itself: non-triviality NT1-NT2, higher points (H-U) and T0-rate are open on the YM branch. |
| R-SUM, `G=G_b` | exact semigroup lift of `τG_b+θH_B` | not decided here | Theorem 5.1's existence step uses the commutator bound for `A` (`GB1E.md` line 78); that bound is not checked for `G_b`, so existence of this exact lift is not settled here. |

**What the YM side can accept.** The anisotropic request T0-start^an is not needed for the third row: its lifts are exactly T0's Wilson measures. The price is the electric function `G_b`, which is calibrated to the Wilson weight. Section 6 four-tests it. A variant keeps GB1QL's electric term and replaces the magnetic function `{\rm Tr}X_p` by `\log k_t(X_p)` (well defined because `k_t>0`, `GB1ISO.md` Theorem 2.2). With `λθ` and `t=λτ_E` matched, its R-IA lift is `∏_Pk_t(U_P)`, the isotropic heat-kernel action (Menotti-Onofri, Drouffe; section 2), by the same proof. It is exchange invariant, but the YM branch's CA statements are for the Wilson action, so its first failing step is the action class (Y2). It is recorded, not developed.

**No counterexample to ISO-FP is claimed.** Theorems 5.1 and `GB1ISO.md` 6.1 are fixed-lattice statements. As `GB1ISO.md` line 111 says, a finite-lattice anisotropy does not decide continuum restoration.

## 6. Candidate law texts and the four tests

Each text below is a candidate for the owner. None is adopted. The tests: a text fails test (1) if it states or fixes a part's target, (2) if it is open-ended so a part can add to it, (3) if it settles a downstream physics question by premise, (4) if it adds structure or constants its own reasons do not need. P = pass, C = conditional, F = fail. The three readings of "full plaquette-sum form" are tested in section 4.1.

**L-FP (GB1ISO's layer, as finite-register law data).** "Replace the magnetic layer by \(W_B^{FP}=\prod_{v\in\{0,e_1,e_2,e_3\}}\prod_{C\in\mathcal C+v}e^{-i(\theta/2)B_C}\), in a fixed order of the four factors, with one free angle \(\theta\)." Verdict: not admissible under NN-a on either live law for `θ` outside a closed discrete set, in every order (Theorem 3.2). The pass-1 grades C P P P of `GB1ISO.md` line 165 stand as judgments about the text; they do not repair the failed premise.

**L-FPW (FP with a Wilson-dual electric layer; a probe for the SU(2) test family's infinite-register target).** "Magnetic layer: FP at angle \(\theta\). Electric layer: \(\prod_\ell e^{-i\tau G_b(\ell)}\), where \(G_b\) acts on flux \(k\) by \(-\log(I_{k+1}(2b)/I_1(2b))\). Free data: \(b>0\), \(\tau>0\); \(\theta=-b\tau/2\). Under R-IA the Euclidean step is \(\lambda=1/\tau\)."

| Test | Grade | Reason |
|---|---|---|
| 1 | F | By construction its R-IA lift is T0's Wilson measure (Theorem 5.2), so it fixes the bridge's target. |
| 2 | P | The function, the relation `θ=-bτ/2` and the step are fixed. |
| 3 | F | It settles Y3 (exchange and diagonal mirrors) and Y2 (action class) for the R-IA branch by the choice of data. |
| 4 | F | The Bessel-ratio function and the angle relation have no reason except the match; GB1QL's `E^2` has an independent reason (the Casimir). |

Its value is diagnostic. It shows that the anisotropy and the action-class mismatch of the R-IA lift come from the shape of the electric function (`GB1E.md` Theorem 7.1), not from the cube coupling or from R-IA itself. If the owner wants ISO handed to T0 without an anisotropic request, this is the price; the owner's guidance allows such a specification ("we can specify if needed"). The heat-kernel variant of section 5.4 has the same grades for the same reasons.

**R-COV_s (covariance in the register limit; a reading change for register families).** "For a register family \(L[s]\), \(s\in\mathbb N\), each \(L[s]\) meets NN-a except that cell covariance of the complete update is required only approximately: for every \(R\) there is \(C_R\), independent of \(s\) and of the volume, such that \(\|\alpha_g(\alpha(\alpha_g^{-1}(A)))-\alpha(A)\|\le C_R\|A\|/s\) for every \(g\in\mathcal G\) and every \(A\) supported in a ball of radius \(R\). Exact covariance is required of the limit \(s\to\infty\)."

FP on `GB1QL.md`'s family satisfies it. For a local `A` only the gates in a bounded region `Ω_R` act, and the two words `W` and `α_g(W)` differ by a permutation of the shifted letters; each transposition costs a commutator of two layers restricted to `Ω_R`, of norm at most `φ^2‖[H_u^{Ω_R},H_v^{Ω_R}]‖≤φ^2|Ω_R|C_0/s` (the bound `‖[e^{iX},e^{iY}]‖≤‖[X,Y]‖` for Hermitian `X,Y`, by Duhamel twice, and the commutator count of Proposition 4.6(b)).

| Test | Grade | Reason |
|---|---|---|
| 1 | P | It names no part's target. |
| 2 | P | The quantifiers, the rate `1/s` and the limit are fixed. |
| 3 | C | It admits FP on register families, so GB1-CF "with an error bound" becomes provable (Proposition 4.6); it settles no vacuum, dispersion or continuum question. |
| 4 | F | It weakens the owner's exact covariance (PS-1c, NN-a) for the sole reason of admitting FP. PS-1c's own reason, a lattice symmetry of each law, does not need an approximate clause. |

It also changes the working-set reading of PS-1c for register families, which is the owner's decision.

**What no text here does.** None makes FP admissible on the live laws `L5-U[m]` or `L5-O[S_+]`, whose registers are fixed. On those laws the classes of section 4 contain no admissible cube-coupling magnetic layer of full-sum form, and the open lemma LW2M-WORD and general NN-a circuits remain.

## 7. Prior work used

Paths are relative to `.claude/science/physics-loops/toe-assembly-20261104/` unless marked YM (`.claude/science/physics-loops/ym4d-hard-route-20261030/` on `origin/claude/ym4d-hard-route` at `8d48cdf80b`) or main.

| Prior result | Path | How it is used here |
|---|---|---|
| Cube tiling, link partition, temporal gauge and cycle lemma, strict heat-kernel positivity | `GB1ISO.md` Theorems 2.1, 2.2, 2.4 | Ported: section 1.2; the trace formula and positivity in Theorem 5.1; `\log k_t` in section 5.4. |
| FP counting, full sum on the target, local R-IA lift never exchange invariant | `GB1ISO.md` Theorem 6.1; `GB1ISO_REFEREE.md` §2.3 (line 116 counting, line 119 covariance) | Ported: Lemma 1.1, Lemma 1.2, section 5.1, table of section 5.4. Extended: Theorem 3.2 decides the finite-register covariance left open at `GB1ISO.md` line 165. |
| ISO-FP and its three failed attacks (RO1 at H-L; tree-level plus perturbative renormalization; the Sussman-Alpoge Ward route) | `GB1ISO.md` line 167; `GB1ISO_REFEREE.md` §2.5 | Not repeated. Theorem 5.1 closes the R-SUM finite-torus exchange sub-question named there; Theorem 5.2 and Corollary 5.3 open a route that avoids H-L by changing the electric function. |
| Plaquette definitions, loop gauge invariance and covariance, disjoint covariant families meet stars in a link or a parity triple | `GA1_5.md` §1, Theorems 2.1, 2.2, 3.1 | Ported: section 1.1; Theorem 4.5 is Theorem 2.2 applied to mixed plaquettes. |
| Lemma U, Proposition C (finite NN-a depth), Lemma S1' | `GA1_5.md` §8 (referee closures of `GA1_5_REFEREE.md`, unrefereed) | Ported: Theorem 3.1. Their unrefereed status is inherited. |
| The two five-mode laws; base-tick covariance; cube matter gates compile | `LW1_5.md` §2, line 276, line 323 | Ported: section 1.1, Theorem 3.2, Theorem 4.2. |
| Cell group, tilings, local automorphisms, GA1-P | `LW1.md` lines 38-43, E1 (line 401), GA1-P (line 486) | Ported: sections 1.2-1.3. |
| `‖e^Ae^B-e^{A+B}‖≤\tfrac12‖[A,B]‖`; finite-register lifts are signed at fixed `s` | `GB1.md` Theorem 2.2, Amendment 3 | Ported: Proposition 4.6(b); remark after Theorem 5.2. |
| The `so(5)` quantum link `R_s`, harmonic calculus, rung test law | `GB1QL.md` §1.2-1.3, Lemma 4.1(a), Proposition 4.2, Proposition 4.11 | Ported: Lemma 1.6(c), Proposition 4.6, Theorem 5.1. |
| Lift definitions; exact lift for R-SUM; Wilson multipliers; analyticity of `Δ` in `θ` | `GB1E.md` §1, Theorem 3.2, Theorem 7.1, Theorem 7.2, line 180 | Ported: section 5.1; Theorem 5.1 reuses Theorem 7.2's method; Theorem 5.2 rests on Theorem 7.1. |
| The diagonal mirror is the exchange | `GB1E_REFEREE.md` line 143 | Used to read Theorem 5.1 as a failure of H-L. |
| Reading texts R-SUM and R-IA | `GB1_GEN_OWNER_CHECK.md` | Used verbatim (sections 0, 4.1, 5.1). |
| NN-a text | `TOE_ASSEMBLY.md` line 235 (section 3.7) | The check of section 3. |
| All mirrors for periodic Wilson states | YM `library/lg1.md` Theorems 10 and 13(5) (lines 365, 431; frozen per `library/t0-tree.md` line 150) | Cited for Corollary 5.3(a); not rebuilt here. |
| RO1 hypotheses and Theorem 9 | YM `library/ro1.md` lines 54-68, 630 | Names H-L in section 5.4. |
| Two-point O(4) without H-U | YM `library/o4-two-point.md` Theorem O4-2 (line 188) | Cited for Corollary 5.3(b), conditional on its own inputs. |
| Two-bond Lie product versus palindrome | main `docs/U1_QUANTUM_LINK_EXACT_LOCAL_BACKREACTION_AND_COLORED_FLOQUET_ENERGY_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md` lines 100-105 (ledger: unaudited), via `prior/LW2M.md` | Context for the order pattern of Theorems 4.3-4.4; not used in a proof. |

**Prior work the digest missed.** (1) `GB1E.md` Theorem 7.1 and line 180 ("The normalized Wilson temporal multipliers are \(I_{k+1}(x_0)/I_1(x_0)\)"): with Creutz's transfer form, this is the whole content of Theorem 5.2. The digest lists GB1E only for its lifts and the heat-kernel mismatch. (2) `GA1_5.md` Theorem 2.2 is a direct no-go for the full plaquette sum in covariant layers of disjoint gates (Theorem 4.5); the digest lists it only as a support obstruction for parity-split charges. (3) `GB1E.md` Theorem 7.2's analyticity argument for the exact lift, which Theorem 5.1 reuses. (4) `GB1.md` Theorem 2.2 (F3'), the commutator bound behind Proposition 4.6.

**Overlap with this lane's results.** No file in the folder, on the YM branch or in the digest's main and PR material states Theorems 3.2, 4.2-4.5, 5.1 or 5.2. The closest are `GB1ISO.md` line 165 (non-commutation noted, consequences not drawn), `GB1E.md` line 180 (the Wilson multipliers, not turned into an electric layer) and the main-branch two-bond example above.

## FINISH

**Proved here** (pass 1; not distilled, not refereed).
- Lemmas 1.1-1.6: tiling memberships; the cell group fixes `𝒞` and permutes the three shifted tilings by every permutation; components of link operators; a nonzero component gives a nonzero derivation; rigidity of plaquette chains; chain commutators have nonzero top components on `L5-U[m]` (all `m`), on `L5-O[S_+]`, and (pairs) on `R_s` (all `s`).
- Theorem 3.1: FP compiles under NN-a into eight cube layers of one Lemma U word each, even gates, gauge invariant.
- Theorem 3.2: in every order, FP is not cell covariant on either live law for `θ` outside a closed discrete set. So FP fails NN-a at "It commutes with every cell lift". The angle on `𝒞` plays no role.
- Theorem 4.2 and Corollary 4.8.1: the exact full sum `e^{-iθH_N}` is not of bounded depth for `θ` outside a countable set; `H_B` is not a periodic sum of commuting bounded terms.
- Theorem 4.3 and Corollary 4.3.1: a word in the four tiling layers is covariant to second order iff its order matrix is label-invariant; otherwise it fails off a discrete set. All FP orders and all Lie-Trotter products fail.
- Lemma 4.4.1 and Theorem 4.4: all 24 nested palindromes and all Strang products fail at third order, off a discrete set.
- Theorem 4.5: every covariant layer of disjoint gates misses every mixed plaquette, at every angle.
- Proposition 4.6: on `GB1QL.md`'s family, FP's covariance and full-sum defects are `O(θ^2N^3/s)` per box, and exact covariance fails at every `s`.
- Theorem 5.1: the exact R-SUM lift under FP is time-space exchange invariant at most on a discrete set of `θ≠0`.
- Theorem 5.2 and Corollary 5.3: with the Wilson-dual electric function `G_b`, the R-IA lift under FP is exactly the isotropic Wilson measure; LG1's mirrors and Theorem O4-2 then apply, so the two-point part of ISO-FP[W] holds with `c=1`, conditional on O4-2's own inputs.

**Counterexamples.**
- To "FP is an admissible finite-register update" (the NN-a check `GB1ISO.md` line 165 asked for): Theorem 3.2, both live laws, every order, generic `θ`.
- To GB1-CF in reading FS-ex on both live laws: Theorem 4.2, generic `θ`.
- To "the exact R-SUM lift under FP might be exchange invariant" at generic `θ`: Theorem 5.1.

**Open by name.**
- LW2M-WORD (section 4.7): the remaining words in the four tiling layers, for example Suzuki's fourth-order product and the cell-averaged product of FP orders. Three attacks failed: order-by-order BCH (no bound on the first differing order), reduced words in a free product (freeness of the layer derivations in degree five and above), light-cone shapes (nonvanishing along unpinned boundary chains).
- GB1-CF outside the stated classes: general NN-a circuits with gauge-variant intermediate gates, and GA1-P-5 sublayers with overlapping commuting gates.
- ISO-FP for GB1QL's electric term `E^2`, under either reading: H-L fails (`GB1ISO.md` Theorem 6.1; Theorem 5.1), so it needs T0-start^an.
- ISO-FP[W]: non-triviality, higher points and the rate, which are T0 and T0-rate on the YM side; the inputs CA (iii-b) and (iv) of Theorem O4-2.
- The exact R-SUM lift for `G_b`; the structure of the exceptional sets `Θ`, `Θ_X`, `Θ_s`; volume-uniform register bounds for FP.

**What changes downstream.**
- `GB1ISO.md` / GB1-CF: FP is not admissible on `L5-U[m]` or `L5-O[S_+]` (generic `θ`). The natural ordered and symmetrised variants also fail. On fixed registers, a cube-coupling magnetic layer of full-sum form must lie outside the classes of section 4, or the owner must relax exact covariance (R-COV_s, test 4 F).
- GB1QL and LW2-G (growing registers): FP's register-limit comparison needs R-COV_s or another construction; Proposition 4.6 gives the `1/s` rate if R-COV_s is chosen.
- ISO-FP under R-SUM: the finite-torus exchange question is decided, negatively, at generic `θ`. Under R-IA, changing the electric function to `G_b` hands isotropy to T0 itself, with no anisotropic request (L-FPW, tests F P F F). Under R-IA with `E^2`, nothing changes: H-L fails at every parameter.
- W3 (rung 2) inherits the same choice: a framework gauge layer that couples cubes must either give up exact cell covariance at finite register or come from outside the classes proved empty here.
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, the working set and every owner decision are unchanged. Nothing is adopted.
