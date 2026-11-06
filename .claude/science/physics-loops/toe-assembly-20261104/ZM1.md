# ZM1. The zoom: block maps from the cell law to coarse cells

## 0. Status

**FINISH: FROZEN 2026-11-06 after pass 3 (ZM1_REFEREE.md); the referee's edits E1-E20 are applied (E20's optional Z4 strengthening is not).** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment. ZM1-i and ZM1-I1 stay open. The statements below are conditional on the named laws and readings; Definitions Z and G are proposed, not adopted. The lead (Claude Opus 5.5, laptop) checked that the required edits are present and the replaced text is gone; that is a text check, not a second referee. The results are conditional on the cited source laws and the hypotheses stated below. A free tick replaces links by c-numbers; it is not the interacting law or its vacuum. Both five-mode laws remain live. No axiom or owner reading is adopted here.

**Amendment 1, 2026-11-06 (prior work in the repository; digest `prior/ZM1.md`).** No proved result of this file changes. ZM1 was drafted before the prior-work gate (SCIENCE_WORKFLOW rule 9, PR #10138). Its digest (Codex `gpt-6.1-sol`, read-only, over main, the open science PRs, the YM branch and this folder) records:
- Z2.0's Clifford relations duplicate `MT1.md` Theorem 4 (credit there). Z0 and Z2 extend `LW1.md` gate factorization and `MT1.md`'s free-node expansion. Z1, Z3 and Z4 are new in the searched material; none is contradicted.
- Inputs that the open statements should use: `docs/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md` (compatible algebra embeddings, a Cauchy-section criterion, and counterexamples to exact state and flow compatibility) for ZM1-ii and the tower; the `docs/WILSON_STAGGERED_CONSTRAINED_FIBER_*_BOUNDED_THEOREM_NOTE_2026-07-12.md` series (raw-integration unit directions, a two-layer complex-source polymer region) for ZM1-i; the level-matched gauge split named in the digest for any nonlinear ZM1-I1 candidate; and `ZM1_OBS_DRAFT.md` for the observable class.
- Open statements are unchanged.

**Proved within the stated scopes.** Exact identity regrouping, finite range and fine gauge conservation (Z0); the exact quasi-free folded-mode count (Z1); the Clifford identities, generator expansion, second-order rotation, tent-kernel isometry and leakage, and spectral projection bound (Z2.0–Z2.4); the displayed low-momentum free dynamics and sea two-point estimates (Z2, conditional on the source formulas); the Gauss-sum dimension bound (Z4); and the finite-support linear-fermion obstruction (Z3). These proofs use the cited earlier results as inputs; they are not independent audit status.

**GAP.** Z2-spatial: band limitation and a time bound do not establish the target for general observables at spatial separation, nor a compatible fixed-point tower. Attack 3: the conserved-projection classification and rank inference are unproved. Theorem Z3 also holds for norm limits of linear fields (Theorem Z3′). Attack 2 does not exclude every approximate c-number route. The massive equal-time decay does not establish an empty dynamical limit.

**Open by name.** ZM1-I1 (in R6's precise form); Z2-spatial (residual); ZM1-i, ZM1-ii, ZM1-G, Y1, VC1, GA1-P, GA1-P-5; and the rule that selects the rung `n` or the exact fixed point. Exact block maps of the free tick that are not quasi-free are not decided and are not asked by Q-F. ZM1-I1 has two failed attacks on file as stated; Attack 3 concerns the subspace variant. The observable class is for the lead or the owner. No counterexample is known.

**Provenance.** Distilled from `ZM1_DRAFT.md`, SHA-256 `71a64958276dd35e767c041af743c926d08bccae60201b9b0cc83e9aea51af97`. Source HEAD `350be1b410eb7d92dfd7df3b85684bbec9ae7c00`. Context: `TOE_ASSEMBLY.md` §§3.4–3.5 and ZM1; `LW1.md`, `LW1_5.md`, `VC1_5.md`, `MT1.md`, `TM1.md`. Pass 1 was Claude Opus 5.5. Pass 2 is Codex CLI `gpt-6.1-terra`, reasoning effort high (from the launch command), session `01a1afd3-b0fa-7e72-80b7-859c5c0f9165`. Draft numerical checks are reports, not independently rerun or proofs. The literature and YM-branch source reports in the draft are not independently verified here; Balaban's group-valued block RG is context, not a premise of the proofs below.

**Editing-session provenance.** Codex gpt-6.1-terra, effort high, codex-cli 0.165.0, session `01a1b005-fbfc-72e3-8017-c48d547720c7`. Referee closures imported below are unrefereed.

## 1. Definitions inferred by the distiller

### 1.1 Notation

Laws and free walks are those of `LW1.md` section 1 and `LW1_5.md` section 2. Sites `x = 2b + r`, cell index `b`, residue `r in {0,1}^3`. Cell Bloch vectors `|K, r> = sum_b e^{iK.b} |2b+r>`, `K in T^3`. `F` is the number of complex flavours (`F = 1` for `L_cube`, `5` for `L5-U`); `L5-O` is handled by a phase gauge and a reality condition (Corollary Z2.2). For an integer `L >= 1`, the **coarse lattice of factor `L`** has coarse cell `u in Z^3` equal to the block `beta_u` of fine cells `{Lu + c' : c' in {0,...,L-1}^3}`, that is, `8L^3` fine sites. A coarse cell has 8 coarse sites `(u, r)`. Coarse momentum is `theta in T^3`. The fine one-body space at coarse momentum `theta` is the direct sum over `m in (Z/LZ)^3` of the fine fibres at the fine momenta

\[
 \xi_m(\theta) = (\theta + 2\pi m)/L .
\]

One coarse tick is `L` fine ticks (graining `c_t = c_s`: a tick moves one cell side, `LW1.md` A3).

### 1.2 Inputs used

Each input below is quoted before it is used.
- `LW1.md` B10(1) (lines 324-326): "The Bloch eigenvalues are \(e^{\pm iw(K)}\), with \(\cos w(K)=a_{\rm band}\chi(K)-b_{\rm band}\) and \(\mu\leq w(K)\leq2\varepsilon\). Each sign has multiplicity four away from a coincident eigenvalue." B10 proof (lines 339-340): "\(V(K)+V(K)^*=2\cos a_e\cos a_o\,I+\sin a_e\sin a_o\{R_e(K),R_o(K)\}\)", with (line 335) "\(\{R_e(K),R_o(K)\}=2\chi(K)I\)". So `V + V^*` is a scalar multiple of the identity. B10(4) (line 329): "If \(\mu>0\), \(|P_{xy}|\leq C e^{-\kappa_{\rm dec}|x-y|}\) for some \(C,\kappa_{\rm dec}>0\)."
- `LW1.md` C1 (lines 372-375): "\(w(k\widehat n)=\frac{s_\varepsilon k}{\sqrt3}\left[1+k^2\left(\frac{s_\varepsilon^2}{72}-\frac{T_4(\widehat n)}{24}\right)+O(k^4)\right]\)" for `mu = 0`.
- `LW1.md`, dressed factorization (line 196): "Each dressed cube gate is an exact finite product of even gates on individual edge triples. These factors can be chosen gauge invariant." `LW1_5.md` section 7.1 (line 314): "Each cube exponential is therefore a finite word of even gauge-invariant edge exponentials."
- `LW1.md` A2 (lines 209, 213): "Every proper cube-centred rotation preserves each half-tick up to a common site sign gauge." "Rotations about other even or odd cube centres differ from these by even translations."
- `LW1.md` B4 (line 241): "Every dressed edge term, dressed cube gate and electric gate commutes with every \(\mathcal G_x\)." `LW1_5.md` G (line 128): "Every hop and cube gate commutes with every \(\mathcal G_x^{cd}\)." U (line 136): "For \(L5\)-U, every \(\mathcal G_x^T\) commutes with every hop and electric gate."
- `LW1_5.md` A2-5 proof (line 257): "Direct substitution gives \(h^{O,\rm free}_{xy}=i\sum_j(c^\dagger_{y,j}c_{x,j}-c^\dagger_{x,j}c_{y,j})\)". So the `L5-O` one-body hop is `i` times a real antisymmetric matrix.
- `MT1.md` Theorem 1 (pass 2, line 38; frozen, line 40): "Each `Q∈O` has a cell-periodic sign lift. It is unique up to a constant phase." "Its fibre matrix `ρ̂(Q)` obeys `ρ̂(Q)R_T(K)ρ̂(Q)*=R_T(QK)`."
- `MT1.md` Theorem 7 (pass 2, lines 82-86; frozen, lines 85-89): "At `μ=0`, near `K=0`, `V(K)=exp(-ih(K))` with h(K)=v\sum_jK_jG_j+O(|K|^2), v=\sin\varepsilon/\sqrt3, G_j=U\Gamma_jU^*, U=e^{i\varepsilon R_e/2}." Since `Gamma_j` anticommutes with `R_e`, `U Gamma_j U^* = Gamma_j e^{-i eps R_e}`, the `G_j` of Lemma Z2.1. Theorem 11 (pass 2, line 124; frozen, line 126): "At the massless free node each five-mode law has 20 two-component Weyl fields per cell"; "`L_cube` has four Weyl fields."
- `GA2_Y2.md` Theorem 3.4 (line 88): "On L5-U, \((U^{jk})^2=0\), \(M=5m-2N^xN^y\ge m(10-m)/2>0\), and \(\kappa\le1/2\)." and "On the L5-O half-spinor, \((U^{ab})^2=1\) and \(\kappa\le1/10\)".

### 1.3 Definition Z (block map, effective law, error)

**Definition Z.** Fix a law with quasi-local algebra `A` and tick automorphism `alpha` (`LW1.md` E1), and `L >= 1`.
- A **coarse system** is a quasi-local algebra `A_1` over the coarse lattice, a graded tensor product of finite-dimensional algebras `B_u` (one per coarse site, coarse links included where present). Its **content** is `D = dim B_u`.
- A **block map of factor `L`** is a unital injective graded *-homomorphism `Phi : A_1 -> A` with:
  - (Z-a) *locality*: for `B in B_u`, `Phi(B)` is a norm limit of elements supported within distance `R` of the block `beta_u`, with error at most `C e^{-R/xi} ||B||` for constants `C, xi`;
  - (Z-b) *cell covariance*: each coarse cell translation and each proper cubic rotation about a coarse cell centre has a fine lift in the law's symmetry group (`LW1.md` A2, `MT1.md` Theorem 1) with `Phi o g_1 = g o Phi`, up to a global phase or global parity;
  - (Z-c) *exact symmetry*: for a free tick, `Phi` commutes with the global group (`U(1)` for `L_cube`, `U(5)` for `L5-U`, `SO(10)` for `L5-O`); for a dressed law, Definition G in §1.4.
- An **effective law at the next scale** is an automorphism `alpha_1` of `A_1` that is local and covariant in the sense of PS-1c (and gauge invariant for dressed laws).
- The **error** of `(Phi, alpha_1)` on `B in A_1` after `t` coarse ticks is `e_t(B) = ||alpha^{Lt}(Phi(B)) - Phi(alpha_1^t(B))||`. The pair is **exact** if `e_t = 0` for all `B` and `t`. For a fine state `omega` and the coarse law's own state `omega_1`, the **correlation error** is `|omega(Phi(A) alpha^{Lt}(Phi(B))) - omega_1(A alpha_1^t(B))|`.
- For a quasi-free (free-tick) law, a **quasi-free block map** is `Phi = Gamma(J)`: `c_1(f) -> c(Jf)` for a one-body isometry `J` that commutes with coarse translations (for `L5-O`, its real Majorana form). Locality (Z-a) holds when `J` has an exponentially decaying kernel.

**Four-test check (pass-1 assessment; proposed reading, not adopted).** The homomorphism, quasi-free scope and embedding choices add restrictions beyond the working-set wording; the assessment of test 4 below is conditional on accepting them.

1. *States a part's target?* No. It names what a candidate must satisfy and the quantities to be bounded. It asserts no existence, no `p` and no fixed point.
2. *Open-ended?* No. The list of conditions is closed.
3. *Settles downstream physics by premise?* It restricts block maps to *-homomorphisms, so block fields obey the same algebra as the law's fields (CAR, Gauss law). This excludes measure-level (Euclidean) block maps, whose block fields are integration variables. Those stay open under Y1 and ZM1-G; nothing here decides them. With that scope stated, it passes.
4. *Adds structure or constants?* No. Locality and covariance are PS-1c's own requirements. Content `D` is the quantity studied, not fixed. The quasi-free restriction for free ticks has a reason of its own: the free tick is a quasi-free automorphism, and ZM1(a)2 asks its long-distance content to be "free massless fields". It passes, with the scope stated in Theorem Z1.

### 1.4 Definition G: gauge embedding

**Definition G (proposed reading, not adopted).** Let the coarse law be of the same type, with coarse Gauss generators `G^{(1),T}_u`. A block map `Phi` is **gauge covariant with embedding sets** `S_u` (nonempty, pairwise disjoint finite sets of fine sites) if:
- (G1) *Gauss law to Gauss law:* `Phi(G^{(1),T}_u) = sum_{x in S_u} G^T_x` for every coarse site `u` and every `T`;
- (G2) *no hidden charge:* every element of `Phi(A_1)` is fixed by each fine gauge transformation at a site outside the union of the `S_u`.

`|S_u| = 1` is the **representative-site** embedding. It is the operator analogue of averaging toward a block centre; the YM branch's `library/a1-balaban.md`, line 21, credits the "centred contour-average construction" to Ethan Sussman and Levent Alpoge; pass 1 read no more of its definition, so the analogy is pass 1's. `S_u = beta_u` is the **block-constant** embedding.

*Four tests.* (1) It states no target: it says what "preserves the exact gauge symmetry" means for a block map, not that one exists. (2) It is closed. (3) It settles no downstream physics: the coarse gauge group is the fine group, embedded diagonally; Gauss's law of the coarse law is a sum of fine Gauss laws. (4) It adds the sets `S_u`, which are data of the block map, not of the law, and no constants. Passes, as a reading of the lane brief's phrase "preserving ... the exact gauge symmetry".


### 1.5 The three questions

- **Q-E (exact zoom).** For which `L` and content `D` is there an exact pair `(Phi, alpha_1)`?
- **Q-F (free tick with error control).** For the free tick, is there a quasi-free block map of bounded content and an effective law with correlation error `O((La/r)^p)`, `p >= 2`, for block observables smeared at scale `r`? (Smearing at scale `r` means coarse momentum support `|theta| <= La/r`.)
- **Q-I (first interacting step).** The same for the dressed base tick, with exact gauge symmetry (Definition G).

---

## 3. Exact block maps (question Q-E)

### 3.1 Exact grouping always works

**Z0 indexing.** In Theorem Z0 use these words. A *coarse site* is a block `β_u`, `u ∈ Z^3`, of side `2L` fine sites. A *coarse cell* is a group `{β_{2b + r'} : r' ∈ {0,1}^3}` of `2 x 2 x 2` blocks. A *coarse cell translation* by `b` is the fine translation by `4Lb`. The *centre* of coarse cell `b` is the fine point `4Lb + (2L - 1/2) 1`. With these words, items (1)–(5) of Theorem Z0 hold as stated, and the coarse system satisfies PS-1c. This coarse lattice differs from §1.1, where a block is a coarse cell. (referee closure, ZM1_REFEREE.md)

**Theorem Z0 (exact grouping, per block).** Take `L_cube`, `L5-U` or `L5-O` with its base tick `U_0` (any `tau_E`, no plaquette layer; GA1-P and GA1-P-5 are open). Fix `L >= 1`. Let the coarse site algebra `B_u` be the algebra of the matter on the `8L^3` sites of `beta_u` together with the fine links whose lower endpoint lies in `beta_u`. Let `Phi` be the identity of `A`, regrouped, and `alpha_1 = alpha^L`. Then:
1. the pair is exact;
2. `alpha_1` maps `B_u` into the algebra of the 27 coarse sites within coarse distance 1 (sup norm) of `u`, and it is a finite product of layers of commuting gauge-invariant gates, each supported on two face-adjacent coarse sites;
3. `alpha_1` is covariant under coarse cell translations and under the proper cubic rotations about coarse cell centres, with lifts in the fine symmetry group; the coarse group acts transitively on coarse sites;
4. `alpha_1` commutes with every fine local gauge transformation; the coarse gauge group at `u` is the product of the fine site gauge groups over `beta_u`;
5. `D = dim B_u = 2^{2 n_s 8L^3} d_l^{48 L^3}`, where `n_s` is the number of modes per site (1 or 5) and `d_l` the link dimension (`2S+1`, `C(10,m)` or 512). So `D` grows like `exp(c L^3)`.

*Proof.* (1) Trivial. (2) Locate each link at its lower endpoint. Say an operator *touches* the sites of its matter and the locations of its links; `B_u` touches exactly `beta_u`. A layer of commuting even gates, each supported in one fine unit cube with its links, maps an operator touching a set `X` to one touching `X^{+1}`, the sites within sup distance 1 of `X`: a gate that shares a site or a link with the operator contains a point of `X` and so lies in `X^{+1}`; the others commute with the operator and cancel (LW1 E1). A link touched in `X^{+1}` is owned by the block of its location. The base tick has two cube layers and one electric layer of single-link gates, so one tick enlarges touched sets by at most 2 in each coordinate. `L` ticks enlarge them by at most `2L`, one block side. For the gate form: each fine cube gate is a finite word of gauge-invariant even edge-triple gates (`LW1.md`, "Dressed factorization"; `LW1_5.md` section 7.1, "finite edge factorization"). A fine edge changes one coordinate by one, so it lies in one block or joins two face-adjacent blocks. Gates of one fine layer on different cubes commute, so the layer equals the product over `k` of the `k`-th letters on all cubes at once; each such product is a layer of commuting gates. Electric gates act on single links. (3) A coarse cell translation is a fine translation by `4L` times an integer vector, an even translation. Translations by `2L` (one block) are also even translations, so `alpha_1` is covariant under them too. A coarse cell is `2 x 2 x 2` coarse sites; its centre has fine coordinates `4Lb_i + 2L - 1/2`, whose integer part is odd in all three coordinates, so it is an odd-cube centre. `LW1.md` A2: rotations about any even or odd cube centre are rotations about `c_0` followed by even translations, so they lie in the fine symmetry group with their sign lifts; the dressed ticks are covariant under these lifts (`LW1.md`, gauged covariance after B4; `LW1_5.md` B1-5 and B1-U). The reflection `x_i -> 2p_i - x_i` about such a centre maps the block boundaries `{2Lk - 1/2}` to `{2L(4b_i + 2 - k) - 1/2}`, so the rotations permute blocks. Coarse cell translations together with rotations act transitively on coarse sites; translations by whole coarse cells alone do not. (4) `LW1.md` B4 for `L_cube`; `LW1_5.md` G and U for the five-mode laws. (5) Count factors. □

A covariant plaquette layer of `l_P` sublayers, each of commuting gates inside single fine cubes, adds `l_P` to the per-tick enlargement; then `alpha_1` has range `ceil((2 + l_P)/2)` blocks instead of 1. Everything else stands.

**What Z0 says.** Identity regrouping has zero error and retains the fine gauge transformations. Its block content grows exponentially in `L^3`.

### 3.2 Exact quasi-free zooms keep a multiple of `L^3` modes

Fix a free tick: the one-body walk `V` on `h = l^2(Z^3) x C^F`, with fibre `V(K) x 1_F` and `0 <= mu < 2 eps < pi`. By `LW1.md` B10(1), `V(K)` has eigenvalues `e^{+-i w(K)}`, each of multiplicity `4F`, with `cos w = a chi - b`, `a = (cos mu - cos 2eps)/2 > 0`, `b = (-cos 2eps - cos mu)/2`, `chi(K) = (1/3) sum_i cos K_i`, and `mu <= w <= 2 eps`. The value `w = pi` never occurs; `w = 0` occurs only at the node (`mu = 0`, `K = 0`). Write `Q_{+-}(K)` for the band projections and `Pi = (pi, pi, pi)`. For `L5-O` the walk is conjugated by the site phases `W_x = i^{x_1+x_2+x_3}`, which shifts the node to `Pi` and changes nothing below.

**Lemma Z1a (no identical crossings except one).** Let `delta in R^3 \ 2 pi Z^3`.
- (i) `w` is not constant on any nonempty open set.
- (ii) `K -> w(K) - w(K + delta)` is not constant on any nonempty open set.
- (iii) `K -> w(K) + w(K + delta)` is not constant on any nonempty open set, unless `delta = Pi mod 2 pi` and `2 eps + mu = pi`. In that case `w(K) + w(K + Pi) = pi` for all `K`.

*Proof.* The function `a chi - b` takes values in `[cos 2eps, cos mu]`, and `cos 2eps > -1`. So `w = arccos(a chi - b)` is real-analytic on the torus minus the node, a connected open set. By the identity theorem, a function in (i)-(iii) that is constant on a nonempty open set is constant on that whole set. (i) `w(0) = mu < 2 eps = w(Pi)`. (ii) Suppose `w(K) - w(K + delta) = c` for all `K`. Then `w(K) - w(K + q delta) = qc` for every integer `q`; `w` is bounded, so `c = 0`. Since `arccos` is injective, `chi(K) = chi(K + delta)` for all `K`. Vary one coordinate `K_i`: `cos(K_i + delta_i) - cos K_i = -2 sin(K_i + delta_i/2) sin(delta_i/2)` must be constant, so `sin(delta_i/2) = 0` for each `i`, and `delta in 2 pi Z^3`. Contradiction. (iii) Suppose `w(K) + w(K + delta) = c`. Then `w(K) = c - w(K + delta) = w(K + 2 delta)`, and (ii) gives `2 delta in 2 pi Z^3`. So each `delta_i` is `0` or `pi` mod `2 pi`, not all `0`. Let `I_pi` be the coordinates with `delta_i = pi`. Put `x = a chi(K) - b` and `y = a chi(K + delta) - b`, so `arccos x + arccos y = c`. Fix `i_0 in I_pi` and vary `u = cos K_{i_0}` near a point where `x, y in (-1,1)`, all other coordinates fixed. Then `x = x_0 + au/3` and `y = y_0 - au/3`. Differentiating, `(1 - x^2)^{-1/2} = (1 - y^2)^{-1/2}`, so `x = y` or `x = -y` on a subinterval. The first gives `x_0 - y_0 + 2au/3 = 0` on an interval, impossible since `a > 0`. So `a(chi(K) + chi(K + delta)) = 2b` on an open set, hence everywhere. Here `chi(K) + chi(K + delta) = (2/3) sum_{i not in I_pi} cos K_i`. If some `i` is not in `I_pi`, varying `K_i` gives a contradiction. So `delta = Pi` and `b = 0`, which is `cos mu = cos(pi - 2 eps)`, that is `mu = pi - 2 eps`. Conversely, if `b = 0` then `cos w(K + Pi) = -a chi(K) = -cos w(K)`, so `w(K + Pi) = pi - w(K)`. □

**Theorem Z1 (exact quasi-free zooms: Bloch monodromy).** Let `L >= 2`, `n >= 1` and `d >= 1`. Let `J : l^2(Z^3) x C^d -> h` be an isometry that commutes with coarse translations (`J T^{(1)}_u = T_{2Lu} J`) and has a summable kernel (`sum_x ||<x|J|(0,i)>|| < infinity` for each `i`; an exponentially decaying kernel qualifies). If `V^n J = J V_1` for a bounded operator `V_1`, then `d = L^3 r` for an integer `1 <= r <= 8F`. More precisely, there are integers `0 <= d_+, d_- <= 4F` with `d = L^3 (d_+ + d_-)`, except when `2 eps + mu = pi` and `L` and `n` are both even; then `d = L^3 d'` with `0 <= d' <= 8F`.

*Proof.* *Step 1 (fibres).* Index the fine one-body space over a coarse cell by `(c', r, f)`: position `c'` of the fine cell in the block, residue `r`, flavour `f`. Coarse Bloch transform turns `J` into a matrix function `theta -> J(theta)` from `C^d` to `C^{8L^3F}`. The summable kernel makes it continuous; isometry gives `J(theta)^* J(theta) = 1` almost everywhere, hence everywhere. So `P(theta) = J(theta) J(theta)^*` is a continuous rank-`d` projection, `2 pi`-periodic in each `theta_j`. For `m in Z^3` (only `m mod L` matters) and `theta in R^3`, the vectors `e_{m,r,f}(theta) = L^{-3/2} sum_{c'} e^{i xi_m(theta).c'} |c', r, f>` are orthonormal, depend continuously on `theta`, and satisfy `e_{m,r,f}(theta + 2 pi e_j) = e_{m + e_j, r, f}(theta)`. With `c = Lu + c'`, `e^{i xi_m . c} = e^{i theta . u} e^{i xi_m . c'}`, so `e_{m,r,f}(theta)` is the coarse Bloch component of the fine Bloch vector `|xi_m(theta), r> x |f>`. Hence `V^n` acts on the span of `{e_{m,.,.}(theta)}` as `V(xi_m(theta))^n x 1_F`. Let `Q_{m,s}(theta)` be the band-`s` projection there. It is continuous off the discrete set `N` of `theta` with some `xi_m(theta)` at the node (empty if `mu > 0`), and `Q_{m,s}(theta + 2 pi e_j) = Q_{m + e_j, s}(theta)`.

*Step 2 (invariance).* `V^n J = J V_1` gives `V^n(theta) P(theta) = P(theta) V^n(theta) P(theta)` almost everywhere, hence everywhere by continuity. `V^n(theta)` is unitary on a finite-dimensional space and maps `ran P(theta)` into itself, hence onto it. So `ran P(theta)` is also invariant under `V^n(theta)^*`, and `P(theta)` commutes with `V^n(theta)`.

*Step 3 (generic separation).* For a label `lambda = (m, s)` put `e_lambda(theta) = e^{i s n w(xi_m(theta))}` on `R^3 \ N`. Write `lambda ~ lambda'` if `e_lambda = e_{lambda'}` identically. For `lambda` not `~ lambda'`, the coincidence set `{e_lambda = e_{lambda'}}` is closed in `R^3 \ N`. It has empty interior: if it contained an open ball, the real-analytic function `f = n(s w(xi_m) - s' w(xi_{m'}))` would take values in `2 pi Z` on the ball, hence be constant there, hence constant on the connected set `R^3 \ N`; then `e_lambda / e_{lambda'} = e^{if}` would equal 1 identically, that is `lambda ~ lambda'`. There are finitely many labels, so the set `G` where all non-equivalent labels have distinct eigenvalues is open and dense in `R^3 \ N`. By Lemma Z1a, with `K = xi_m(theta)` and `delta = 2 pi (m' - m)/L`: for `m = m'` and `s != s'`, `2 n w` is not constant (part (i)); for `m != m'` and `s = s'`, part (ii); for `m != m'` and `s = -s'`, part (iii). The only possible identity is `w(K) + w(K + Pi) = pi` with `2 eps + mu = pi`, which needs `2 pi (m' - m)/L = Pi mod 2 pi`, that is `L` even and `m' = m + h`, `h = (L/2)(1,1,1)`. Then `e_{(m,s)}/e_{(m+h,-s)} = e^{i s n pi} = (-1)^n`, so the identity holds exactly when `n` is even. Hence the classes are singletons, except in the case `2 eps + mu = pi`, `L` even, `n` even, where they are the pairs `C_m = {(m,+), (m+h,-)}`; every label lies in exactly one such pair because `2h = 0 mod L`.

*Step 4 (commutation).* For a class `C` put `Q_C = sum_{lambda in C} Q_lambda`. On `G`, the `Q_C(theta)` are the spectral projections of `V^n(theta)`, so `P(theta)` commutes with them. By continuity this holds on `R^3 \ N`.

*Step 5 (count).* `d_C(theta) = rank(P Q_C) = tr(P Q_C)` is continuous and integer-valued on the connected set `R^3 \ N` (a discrete set removed from `R^3`), hence constant. Periodicity of `P` and Step 1 give `d_C = d_{C + e_j}`, where `C + e_j` shifts the `m`-labels; the relation `~` is shift-equivariant. Since `sum_C Q_C = 1` and `P` commutes with each, `d = sum_C d_C`. The shifts act transitively on `{(m,+)}`, on `{(m,-)}`, and on the pairs `C_m`. So `d = L^3 (d_+ + d_-)` with `d_s <= 4F`, or `d = L^3 d'` with `d' <= 8F` in the exceptional case. As `d >= 1`, `r = d/L^3 >= 1`. □

**Theorem Z1 for real Majorana maps** (referee closure, ZM1_REFEREE.md)

**Claim.** Let `O` be the real orthogonal one-body walk of the `L5-O` free tick on the Majorana space `l^2(Z^3; R^{10})`. Let `J_R : l^2(Z^3; R^d) -> l^2(Z^3; R^{10})` be a real isometry that commutes with coarse translations and has a summable kernel. If `O^n J_R = J_R O_1` for a bounded real `O_1`, then `d = L^3 r_M` with `1 <= r_M <= 80`. More precisely, `d = L^3 (d_+ + d_-)` with `0 <= d_± <= 40`, except when `2ε + μ = π` and `L`, `n` are both even; then `d = L^3 d'` with `d' <= 80`. In Majorana units Corollary Z1.1 holds unchanged. PS-5 content, 80 Majorana modes per coarse cell, forces `L = 2` and `r_M = 10`. No two-step exact tower exists.

*Proof.* Complexify: `J = J_R ⊗ 1_C`, `O_C = O ⊗ 1_C`. Then `J` is a complex isometry that commutes with coarse translations, has a summable kernel, and satisfies `O_C^n J = J O_{1,C}`. The free `L5-O` hop conserves number. `LW1_5.md` line 257: "Direct substitution gives `h^{O,free}_{xy} = i Σ_j (c^†_{y,j} c_{x,j} - c^†_{x,j} c_{y,j})`". So `O` preserves the complex structure of the Majoranas, and `l^2(Z^3; C^{10})` splits into an annihilator part and a creator part. On them `O_C` acts as `V' ⊗ 1_5` and `V̄' ⊗ 1_5`, with `V' = W V W^*` (`LW1_5.md` line 255) and the bar denoting complex conjugation in the site basis. The fibre of `V̄'` at `K` is `conj(V'(-K))`. `V'(K)` has eigenvalues `e^{±i w'(K)}` with `w'(K) = w(K - Π)`. Since `χ` is even, `w'` is even, so `conj(V'(-K))` has eigenvalues `e^{∓i w'(K)}`. Hence the fibre of `O_C` at `K` has the two eigenvalues `e^{±i w'(K)}`, each of multiplicity 40, with band projections continuous off the node `Π`. Steps 1–5 of Theorem Z1 use only these facts, the label shift `ξ_m(θ + 2πe_j) = ξ_{m+e_j}(θ)` and continuity. So they apply with `4F` replaced by 40. For the corollary: `L^3 r_M = 80` with `L >= 2` forces `L = 2`, since 27 and 64 do not divide 80. A two-step tower would need `(L_1 L_2)^3 >= 64` to divide 80. □

**Corollary Z1.1 (no exact tower; Majorana modes for `L5-O`).**
1. An exact quasi-free zoom of factor `L` keeps at least `L^3` modes per coarse cell, at least `L^3/8` per coarse site.
2. To keep the PS-5 content of five complex modes per coarse site (40 per coarse cell) requires `L^3 r = 40`, so `L = 2` and `r = 5`.
3. Two exact quasi-free zooms compose: if `V^{n_1} J_1 = J_1 V_1` and `V_1^{n_2} J_2 = J_2 V_2`, then `V^{n_1 n_2} J_1 J_2 = J_1 J_2 V_2`, and `J_1 J_2` is an isometry with summable kernel commuting with translations by `2 L_1 L_2`. So a tower of `k` exact quasi-free zooms of factor `L_i >= 2` with fixed content `d` per coarse cell needs `(L_1 ... L_k)^3` to divide `d`. That fails for large `k`. With PS-5 content no two-step exact tower exists.

*Proof.* (1)-(2) are Theorem Z1. (3) is the displayed identity and Theorem Z1 for the composite. □

**Scope.** Theorem Z1 concerns quasi-free block maps (§1.3). The grouping of Theorem Z0 is quasi-free with `r = 8F`, the largest value. Whether a block map that is not quasi-free can be exact with bounded content for the free tick is not asked by Q-F and is not decided here.

**Named failing step for exact bounded zooms.** "A local subspace invariant under `V^n` can keep only the low-momentum states." Step 5 shows it must keep the same number of states at every one of the `L^3` folded fine momenta, including those at the lattice scale. So every quasi-free zoom of factor `L` with fewer than `L^3` modes per coarse cell has a nonzero error. Section 4 bounds that error.

---

## 4. The free tick with error control (question Q-F)

Throughout this section `mu = 0` and `0 < eps < pi/2`. Write `s = sin eps`, `c = cos eps`, `v = s/sqrt3`, and `R = R_e`.

### 4.1 The cell algebra and the one-tick formula

**Lemma Z2.0 (rebuild of `MT1.md` Theorem 4, and an exact formula).** On the cell fibre `C^8` (residues `r`), let `A_j = sum_{r_j = 0} eta_j(r)(|r + e_j><r| + |r><r + e_j|)`, `Z_j |r> = (-1)^{r_j} |r>` and `Gamma_j = i Z_j A_j`. Then:
1. the six matrices `A_j, Gamma_j` are Hermitian involutions and anticommute pairwise; so for real `a_j, b_j`, `(sum_j a_j A_j + b_j Gamma_j)^2 = sum_j (a_j^2 + b_j^2) 1`;
2. `R_e(K) = R = (1/sqrt3) sum_j A_j` and `R_o(K) = (1/sqrt3) sum_j (cos K_j A_j - sin K_j Gamma_j)`;
3. with `D(K) = R_o(K) - R`, `V(K) = 1 + i s D(K) e^{-i eps R}`, and `||D(K)|| = (2/sqrt3) (sum_j sin^2(K_j/2))^{1/2} <= |K|/sqrt3`.

*Proof.* (1) `A_j` is a signed perfect matching, so `A_j^2 = 1`. Two matchings `A_i, A_j` anticommute because each face has sign product `-1` (`LW1.md` A1). `Z_j` is diagonal; `A_j` flips `r_j`, so `Z_j A_j = -A_j Z_j`; `A_k` for `k != j` keeps `r_j`, so `Z_j A_k = A_k Z_j`. Then `Gamma_j^* = -i A_j Z_j = i Z_j A_j = Gamma_j`, `Gamma_j^2 = -Z_j A_j Z_j A_j = 1`, `Gamma_j A_j = i Z_j = -A_j Gamma_j`, `Gamma_j A_k = -A_k Gamma_j` for `k != j`, and `Gamma_j Gamma_k = -Z_j Z_k A_j A_k = -Gamma_k Gamma_j`. Squares of real combinations follow. (2) Even edges join residues `r` (with `r_j = 0`) and `r + e_j` in one cell, with sign `eta_j(r)` (cell-periodic, since `eta_j(2b + r) = eta_j(r)`). Odd edges in direction `j` join `2b + r` (with `r_j = 1`) to `2(b + e_j) + (r - e_j)`. On `|K, r>` they give `e^{-iK_j} |K, r - e_j>` for `r_j = 1` and `e^{iK_j} |K, r + e_j>` for `r_j = 0`, with sign `eta_j`. Summing, the direction-`j` part is `(1/sqrt3)(cos K_j A_j + i sin K_j sum_{r_j=0} eta_j(r)(|r+e_j><r| - |r><r+e_j|))`, and the last sum equals `-Z_j A_j`, so the term is `-sin K_j Gamma_j`. (3) Since `R^2 = R_o^2 = 1`, `e^{i a R} = cos a + i sin a R`. Then `V = (c + i s R + i s D)(c - i s R) = 1 + i s D e^{-i eps R}`. By (1), `D^2 = (1/3) sum_j ((cos K_j - 1)^2 + sin^2 K_j) = (4/3) sum_j sin^2(K_j/2)`, a scalar. □

[check] `check_h2.py`: the six relations hold to machine precision.

### 4.2 The generator to second order

Let `h(K) = i Log V(K)` with the principal logarithm. Since `V(K) = e^{-i h(K)}` and the quasi-energies lie in `(-pi, pi)`, the free sea is `P(K) = 1_{(-infinity, 0)}(h(K))` (PS-7r, `LW1.md` B10).

**Lemma Z2.1 (expansion).** Put `G_j = Gamma_j e^{-i eps R}` and
\[
 C_j = \frac{s}{2\sqrt3}\Big(c\,A_j - \frac{i s}{\sqrt3}\sum_{k\ne j} A_jA_k\Big).
\]
Then:
1. the `G_j` are Hermitian and pairwise anticommuting involutions; the `C_j` are Hermitian with `||C_j|| = (s/(2 sqrt3))(c^2 + 2s^2/3)^{1/2} <= v/2`;
2. `h(K) = h_1(K) + h_2(K) + r_3(K)` with `h_1(K) = v sum_j K_j G_j`, `h_2(K) = sum_j K_j^2 C_j`, and `||r_3(K)|| <= |K|^3/2` for `|K| <= 1`;
3. `{G_j, C_k} = 0` for all `j, k`.

*Proof.* (1) `Gamma_j` anticommutes with `R`, so `e^{i eps R} Gamma_j = Gamma_j e^{-i eps R}`. Hence `G_j^* = e^{i eps R} Gamma_j = G_j`, `G_j^2 = Gamma_j^2 = 1` and `{G_j, G_k} = {Gamma_j, Gamma_k} = 0`. For `j != k`, `(A_j A_k)^* = -A_j A_k`, so `C_j` is Hermitian. Write `C_j = (s/(2 sqrt3)) A_j (c - (i s/sqrt3)(A_k + A_l))` with `{k, l} = {1,2,3} \ {j}`. `Y_0 = A_k + A_l` has `Y_0^2 = 2`, so `c - (is/sqrt3) Y_0` is normal with eigenvalue moduli `(c^2 + 2s^2/3)^{1/2} <= 1`, and `A_j` is unitary.

(2) Put `X = V - 1 = i s D e^{-i eps R}`; then `||X|| <= v|K| <= 1/sqrt3 < 1` for `|K| <= 1`, and `h = i sum_{k >= 1} (-1)^{k+1} X^k / k`. Split `D = D_1 + D_2 + D_3` with `D_1 = -(1/sqrt3) sum_j K_j Gamma_j`, `D_2 = -(1/(2 sqrt3)) sum_j K_j^2 A_j` and `D_3 = (1/sqrt3) sum_j ((cos K_j - 1 + K_j^2/2) A_j - (sin K_j - K_j) Gamma_j)`, and `X_i = i s D_i e^{-i eps R}`. By Lemma Z2.0(1), `||D_1|| = |K|/sqrt3`, `||D_2|| <= |K|^2/(2 sqrt3)`, and, using `|cos x - 1 + x^2/2| <= x^4/24` and `|sin x - x| <= |x|^3/6`, `||D_3|| <= (1/sqrt3)(|K|^6/36 + |K|^8/576)^{1/2} <= 0.0992 |K|^3`. First order: `i X_1 = -s D_1 e^{-i eps R} = v sum_j K_j G_j = h_1`. Second order: `D_1` anticommutes with `R`, so `X_1^2 = -s^2 D_1^2 = -s^2 |K|^2/3`, and `-i X_1^2/2 = i s^2 |K|^2/6`. Next `i X_2 = (s/(2 sqrt3)) sum_j K_j^2 A_j (c - i s R)`, and `A_j R = (1/sqrt3)(1 + sum_{k != j} A_j A_k)`; so `i X_2 = sum_j K_j^2 C_j - i s^2 |K|^2/6`. The two scalar terms cancel: `i(X_2 - X_1^2/2) = h_2`. The remainder is `r_3 = i(X_3 - (X^2 - X_1^2)/2 + sum_{k>=3} (-1)^{k+1} X^k/k)`. Here `||X_3|| <= 0.0992|K|^3`; `X^2 - X_1^2 = X_1(X - X_1) + (X - X_1)X` has norm at most `s(||D_2|| + ||D_3||) 2v|K| <= 0.448 |K|^3`; and `sum_{k>=3} ||X||^k/k <= (v|K|)^3/(3(1 - v|K|)) <= 0.152 |K|^3`. Total `||r_3|| <= (0.0992 + 0.224 + 0.152)|K|^3 <= |K|^3/2`.

(3) From `V + V^* = 2 cos w(K) 1` (`LW1.md` B10 proof) and `V = e^{-ih}`, every eigenvalue `lambda` of `h` has `cos lambda = cos w`, so `h^2 = w^2 1`. With `mu = 0`, `cos w = 1 - s^2 (1 - chi)` and `1 - chi = |K|^2/6 + O(|K|^4)`, so `w^2 = v^2 |K|^2 + O(|K|^4)`. By (2), `h^2 = h_1^2 + {h_1, h_2} + O(|K|^4)`, and `h_1^2 = v^2 |K|^2`. So the cubic polynomial `{h_1, h_2} = v sum_{j,k} K_j K_k^2 {G_j, C_k}` is `O(|K|^4)`, hence zero. Its monomials `K_j K_k^2` are distinct for distinct `(j,k)`, so each `{G_j, C_k} = 0`. □

[check] `check_h2.py` (`eps = 0.7`) confirms `h_1`, the absence of `K_j K_k` cross terms, the formula for `C_j` (error `3e-8`), its norm, and `{G_j, C_k} = 0`. `check_z2.py` gives `max ||r_3(K)||/|K|^3 = 0.065` over `eps in {0.05, 0.3, 0.7, 1.2, 1.5}` and `|K| <= 1`, below the proved `1/2`.

### 4.3 The second-order term is a basis rotation

**Lemma Z2.2 (twist).** Put `Y(K) = (i/(2v)) sum_j K_j G_j C_j` and its periodic version `Y^tr(theta) = (i/(2v)) sum_j sin(theta_j) G_j C_j`. Then:
1. `Y` and `Y^tr` are Hermitian, `i[Y(K), h_1(K)] = h_2(K)`, and `i[Y^tr(theta), h_1(theta)] = sum_j theta_j sin(theta_j) C_j`;
2. `||Y^tr(theta)|| <= (1/4) sum_j |sin theta_j| <= (sqrt3/4)|theta|`;
3. `Y^tr` is covariant: for every proper cubic rotation `Q` with cell lift `rho(Q)` (`MT1.md` Theorem 1), `rho(Q) Y^tr(theta) rho(Q)^* = Y^tr(Q theta)`.

*Proof.* (1) `(G_j C_j)^* = C_j G_j = -G_j C_j`, so `i G_j C_j` is Hermitian. For `k != j`, `[G_j C_j, G_k] = -G_j G_k C_j - G_k G_j C_j = -{G_j, G_k} C_j = 0`; and `[G_j C_j, G_j] = -C_j - C_j = -2 C_j`. Hence `i [Y, h_1] = i (i/(2v)) v sum_j K_j K_j (-2 C_j) = h_2`, and the same computation with `sin theta_j` in place of the first `K_j` gives the trig form. (2) `||G_j C_j|| = ||C_j|| <= v/2`, then Cauchy-Schwarz. (3) The fibre lift satisfies `rho(Q) V(K) rho(Q)^* = V(QK)` (`MT1.md` Theorem 1 with Theorem 4), and the principal logarithm commutes with unitary conjugation, so `rho(Q) h(K) rho(Q)^* = h(QK)`. Write `Q e_j = sigma_j e_{pi(j)}`. Comparing the linear and quadratic Taylor terms, which are unique, gives `rho(Q) G_j rho(Q)^* = sigma_j G_{pi(j)}` and `rho(Q) C_j rho(Q)^* = C_{pi(j)}`. Since `sin((Q theta)_{pi(j)}) = sigma_j sin theta_j`, the claim follows. □

So to second order the walk at low momentum is `e^{iY} h_1 e^{-iY}`: the term `h_2`, of order `|K|^2`, changes no eigenvalue at that order and is removed by an analytic, covariant change of basis. The first term that a change of basis cannot remove is the cubic part of the spectrum, `v k^3 (s^2/72 - T_4(n)/24)` by `LW1.md` C1; its direction-dependent part is the anisotropy.

### 4.4 The block kernel

**Lemma Z2.3 (an orthonormal symmetric tent kernel).** Fix `L >= 2`. On `Z` let `B(xi) = sum_{n=0}^{L-1} e^{-in xi}`, let `G(xi) = sum_{|n| <= (L-1)/2} e^{-in xi}` for odd `L` and `G(xi) = sum_{|n| < L/2} e^{-in xi} + cos(L xi/2)` for even `L`, and let `a` be the finitely supported sequence with `hat a = B G`. Put `g(theta) = (1/L) sum_{m=0}^{L-1} |hat a((theta + 2 pi m)/L)|^2` and `hat psi(xi) = hat a(xi) g(L xi)^{-1/2}`. Let `alpha_m(theta) = L^{-1/2} hat psi((theta + 2 pi m)/L)`. Then:
1. `g` is a trigonometric polynomial with `g(theta) >= 0.078 L^3` on `[-pi, pi]`;
2. `sum_m |alpha_m(theta)|^2 = 1`, so the translates `psi(. - Lb)`, `b in Z`, are orthonormal;
3. `psi` is real and symmetric about `(L-1)/2`: `psi(n) = psi(L - 1 - n)`;
4. there are `C_psi, eta > 0` with `|psi(n)| <= C_psi e^{-eta |n|/L}`;
5. for `|theta| <= pi`, `sum_{m != 0} |alpha_m(theta)|^2 <= 1.75 theta^4`.

In three dimensions put `psi^(3)(c) = psi(c_1) psi(c_2) psi(c_3)` and `J_L |u, r, f> = sum_c psi^(3)(c - Lu) |2c + r, f>`. Then `J_L` is an isometry with exponentially decaying kernel that commutes with coarse translations and flavour. Its fibre is `J_L(theta) = sum_m alpha_m(theta) iota_m(theta)` with `alpha_m(theta) = prod_i alpha_{m_i}(theta_i)` and `iota_m(theta) : e_{r,f} -> e_{m,r,f}(theta)` (Theorem Z1, Step 1). For `theta in [-pi, pi]^3` the leakage `l(theta) = (sum_{m != 0} |alpha_m(theta)|^2)^{1/2}` obeys `l(theta) <= 1.33 |theta|^2`. Finally `J_L` intertwines the coarse sign lift of each rotation about a coarse cell centre with the fine sign lift of the same rotation about the corresponding block centre.

*Proof.* `B(xi) = e^{-i(L-1)xi/2} sin(L xi/2)/sin(xi/2)`. For odd `L`, `G(xi) = sin(L xi/2)/sin(xi/2)`; for even `L`, using `cos(L xi/2) sin(xi/2) = (sin((L+1)xi/2) - sin((L-1)xi/2))/2`, `G(xi) = sin(L xi/2) cot(xi/2)`. Both `G` are real and even, with `G(0) = L`.

*(5) and (1).* Put `xi_m = (theta + 2 pi m)/L`. Then `|sin(L xi_m/2)| = |sin(theta/2)|` for every `m`. So for `m != 0`, `|hat a(xi_m)| <= sin^2(theta/2)/sin^2(xi_m/2)` (equality for odd `L`; for even `L` use `|cos| <= 1`). For `m = 0` and `|theta| <= pi`: `|sin(theta/2)| >= |theta|/pi` and `|sin(theta/(2L))| <= |theta|/(2L)`, so `|B(xi_0)| >= 2L/pi`, and `|G(xi_0)| >= (2L/pi) cos(pi/4)` (even `L`) or `>= 2L/pi` (odd `L`). Hence `|hat a(xi_0)| >= (4 cos(pi/4)/pi^2) L^2 >= 0.28 L^2`, which gives (1): `g >= (1/L)|hat a(xi_0)|^2 >= 0.078 L^3`. For `1 <= m <= L-1` and `|theta| <= pi`, `xi_m/2` lies in `[(2m-1)pi/(2L), (2m+1)pi/(2L)]`, inside `(0, pi)`. With `j = min(m, L - m)` and `sin x >= (2/pi) min(x, pi - x)` on `[0, pi]`, `sin(xi_m/2) >= j/L`. Each `j` occurs at most twice, so `sum_{m != 0} sin^{-4}(xi_m/2) <= 2 L^4 sum_{j>=1} j^{-4} = 2 L^4 pi^4/90 <= 2.17 L^4`. Since `|alpha_m|^2 = |hat a(xi_m)|^2 / sum_{m'} |hat a(xi_{m'})|^2`,
\[
 \sum_{m\ne0}|\alpha_m|^2 \le \frac{\sin^4(\theta/2)\, 2.17 L^4}{(0.28 L^2)^2} \le 27.7\,\sin^4(\theta/2) \le 1.75\,\theta^4 .
\]
*(2).* `L g(theta) = sum_m |hat a(xi_m)|^2`, and `g(L xi_m) = g(theta + 2 pi m) = g(theta)`, so `sum_m |alpha_m|^2 = sum_m |hat a(xi_m)|^2/(L g(theta)) = 1`. Folding the Fourier integral over the `L` aliases gives `<psi(. - Lb), psi(. - Lb')> = (1/2 pi) int_{-pi}^{pi} (sum_m |alpha_m(theta)|^2) e^{i(b - b')theta} d theta = delta_{bb'}`.
*(3).* `hat a(xi) = e^{-i(L-1)xi/2} rho(xi)` with `rho` real and even; `g` is real, even and positive. So `hat psi(xi) = e^{-i(L-1)xi/2} times` a real even function, which is the Fourier transform of a real sequence symmetric about `(L-1)/2`.
*(4).* `g` has finitely many Fourier coefficients, so it extends to an entire, `2 pi`-periodic function. By uniform continuity on `[-pi, pi] x [-1, 1]`, there is `eta_0 > 0` with `Re g(theta + iy) >= g(theta)/2 > 0` for `|y| <= eta_0`. So `g^{-1/2}` (principal branch) is holomorphic and periodic on that strip, and shifting the contour gives Fourier coefficients `|gamma_b| <= M e^{-eta |b|}` for any `eta < eta_0`. Since `g(L xi)^{-1/2} = sum_b gamma_b e^{-iLb xi}`, `psi(n) = sum_b gamma_b a(n - Lb)`, and `a` has finite support, the bound follows.
*Three dimensions.* Orthonormality, decay and reality tensorize. The fibre formula: the coarse Bloch component of `J_L |u, r, f>` along `e_{m,r,f}(theta)` is `L^{-3/2} sum_n psi^(3)(n) e^{-i xi_m . n} = alpha_m(theta)`, because `e^{i xi_m . Lv} e^{-i theta . v} = 1`. For `p_i in [0,1]`, `1 - prod p_i <= sum (1 - p_i)`, so `l(theta)^2 <= sum_i 1.75 theta_i^4 <= 1.75 |theta|^4`, and `sqrt(1.75) < 1.33`. *Covariance.* (referee closure, ZM1_REFEREE.md) Let `O` be the proper cubic rotation group, `c_0 = (1/2)(1,1,1)`, `1 = (1,1,1)`, and `g_Q(r) = Q(r - c_0) + c_0`. The cell lift is `ρ(Q)|2b + r> = s_Q(r)|2Qb + g_Q(r)>`, and `ρ_c(Q)` is the same lift on the coarse lattice. The twisted map `J̃_L` is defined in §4.6.

**Claim.** Fix `L >= 2` and `Q ∈ O`. Put `p = (L - 1/2) 1`, the centre of `β_0` and so of coarse cell 0. Put `t = p - c_0 = (L - 1) 1`, `p' = ((L-1)/2) 1`, and `F_Q = T_{(I-Q)t} ρ(Q)` (times `1_F`). Then:
1. `(I - Q)t ∈ 2Z^3`, so `F_Q` commutes with `R_e`, `R_o` and the free walk `V`;
2. `F_Q |2c + r> = s_Q(r) |2 Q̄(c) + g_Q(r)>` with `Q̄(c) = Q(c - p') + p'`;
3. `F_Q` moves sites by `x -> Q(x - p) + p`, the rotation about `p`;
4. every lift of that rotation equals `F_Q` times a constant phase;
5. `J_L ρ_c(Q) = F_Q J_L` and `J̃_L ρ_c(Q) = F_Q J̃_L`. For the centre of coarse cell `u_0` the same holds with `T^{(1)}_{u_0} ρ_c(Q) T^{(1)}_{-u_0}` and `T_{2L u_0} F_Q T_{-2L u_0}`.

*Proof.* (1) `Q1` has entries `±1`, so `1 - Q1` has entries `0` or `2`. Times `L - 1` it is even. `LW1.md` A2 proof, line 211: "Even translations preserve both tilings and every `η_i`." So the translation commutes with `R_e` and `R_o`. Line 213: "The signed permutation `D_dP_Q` consequently fixes both `R_e,R_o`". So `ρ(Q)` commutes with them too. (2) `ρ(Q)` sends `|2c + r>` to `s_Q(r)|2Qc + g_Q(r)>`. Adding `(I - Q)t = 2(I - Q)p'` gives the site `2(Qc + (I - Q)p') + g_Q(r) = 2Q̄(c) + g_Q(r)`. Note `(I - Q)p'` has entries `0` or `L - 1`, so `Q̄` maps `Z^3` to itself for both parities of `L`. (3) The site map is `x -> Q(x - c_0) + c_0 + (I - Q)(p - c_0) = Qx + (I - Q)p = Q(x - p) + p`. (4) Let `F'` be a lift of the same rotation. Then `F' F_Q^*` is diagonal with phases `d(x)` and commutes with `R_e` and `R_o`. Each edge `(x, y)` has a nonzero entry in one of them, so `d(x) = d(y)`. The lattice is connected, so `d` is constant. This is MT1 Theorem 1's uniqueness argument. (5) We have `J_L ρ_c(Q)|u, r> = s_Q(r) Σ_c ψ^(3)(c - LQu) |2c + g_Q(r)>`. By (2), `F_Q J_L |u, r> = s_Q(r) Σ_{c'} ψ^(3)(Q̄^{-1}(c') - Lu) |2c' + g_Q(r)>`. With `n = c' - LQu` one finds `Q̄^{-1}(c') - Lu = Q^{-1}(n - p') + p'`. All coordinates of `p'` are equal, so each coordinate of `Q^{-1}(n - p') + p'` is some `n_k` or `L - 1 - n_k`, each `k` once. By Lemma Z2.3(3) and the product form, `ψ^(3)(Q^{-1}(n - p') + p') = ψ^(3)(n)`. So the two sides agree. `𝒲` commutes with `ρ_c(Q)` by Lemma Z2.2(3), so `J̃_L = J_L 𝒲^*` intertwines too. The last sentence follows from `J_L T^{(1)}_u = T_{2Lu} J_L`. □

[check] `check_z2.py`: over `L in {2, 3, 4, 5, 8}` and `theta in [-pi, pi]`, `max sum_{m != 0}|alpha_m|^2 / theta^4 = 0.0054`, below the proved `1.75`; the symmetry (3) holds for `L = 2, ..., 5`.

### 4.5 Spectral projections

**Lemma Z2.4.** Let `A, B` be Hermitian matrices, let `B` have no eigenvalue in `(-g, g)` with `g > 0`, and let `||A - B|| = delta < g`. Then `||1_{(-infinity,0)}(A) - 1_{(-infinity,0)}(B)|| <= 2 delta/(2g - delta)`.

*Proof.* By Weyl's inequality, `A` has no eigenvalue in `(-(g - delta), g - delta)`. Let `E = 1_{(-infinity,0)}(B)`, `F = 1_{(-infinity,0)}(A)`, `E' = 1 - E`, `F' = 1 - F`, and `X = F' E`. Since `A` commutes with `F` and `B` with `E`, `F'(A - B)E = A' X - X B'` with `A' = F' A F' >= g - delta` on `ran F'` and `B' = E B E <= -g` on `ran E`. For such `A', B'`, `X = int_0^infinity e^{-tA'} (A'X - XB') e^{tB'} dt` (differentiate `t -> e^{-tA'} X e^{tB'}`, which tends to 0), so `||X|| <= delta/((g - delta) + g)`. The same bound holds for `F E'`, using `-FAF >= g - delta` and `-E'BE' <= -g`. Finally `F - E = F E' - F' E`. □

### 4.6 The theorem

Let `W(theta) = exp(i beta Y^tr(theta)) x 1_F` with `beta = 1 - 1/L`, let `cal W` be the coarse one-body unitary with this fibre, and put
\[
 \tilde J_L = J_L\, \mathcal W^{*}, \qquad \Phi_L = \Gamma(\tilde J_L).
\]
The **coarse law** is the free walk itself, with the same `eps` and `mu = 0`, on the coarse lattice: fibre `V(theta)`, generator `h(theta)`, sea `P(theta) = 1_{(-infinity,0)}(h(theta))`.

**Theorem Z2 (massless free wave-packet estimates).** Let `F = 1` (`L_cube`) or `F = 5` (`L5-U`), `0 < eps < pi/2`, `mu = 0` and `L >= 2`.
1. `tilde J_L` is an isometry with exponentially decaying kernel. It commutes with coarse translations and with `U(F)`, and intertwines the coarse sign lifts of rotations about coarse cell centres with fine sign lifts. `Phi_L` is a block map in Definition Z; its coarse law has `F` modes per coarse site.
2. The coarse law is the fine free walk: a finite-depth nearest-neighbour unitary, covariant under PS-1c.
3. (*Dynamics.*) For every coarse one-body vector `f` with momentum support in `|theta| <= kappa <= 1`, and every `t in N`,
\[
 \|V^{Lt}\tilde J_L f - \tilde J_L V^t f\| \le (2.66\,\kappa^2 + 1.5\,t\,\kappa^3)\,\|f\| .
\]
4. (*Sea correlations.*) If moreover `kappa <= sqrt(v)/2`, then for every `g` with the same support,
\[
 |\langle f, (\tilde J_L^{*} P V^{Lt} \tilde J_L - P V^t) g\rangle| \le \Big(\frac{3.5}{v}\kappa^2 + 2.66\,\kappa^2 + 1.5\,t\,\kappa^3\Big)\|f\|\,\|g\| ,
\]
and the same bound holds with `1 - P` in place of `P` (referee closure, ZM1_REFEREE.md). Here the first `P` is the fine sea and the second the coarse sea; each is `1_{(-infinity,0)}(h)` of its own walk. Every two-point function of smeared block fields in the free sea is a matrix element of one of these operators, and Wick's rule gives all higher correlations from them.

*Proof.* (1) `J_L` has the stated properties by Lemma Z2.3. `cal W` has fibre `exp(i beta Y^tr(theta))`; `Y^tr` has range one coarse cell, so `cal W` is an entire function of a finite-range operator and its kernel decays faster than exponentially. It commutes with coarse lifts by Lemma Z2.2(3), and acts as `1_F` on flavour. Compositions keep each property. `Gamma` of an isometry is an injective *-homomorphism of CAR algebras.

(2) This is `LW1.md` (A1a, A2) and `LW1_5.md` (A2-5).

(3) At coarse momentum `theta`, `V^{Lt}(theta) iota_m(theta) = iota_m(theta) V(xi_m(theta))^{Lt}` (Theorem Z1, Step 1), and `tilde J_L(theta) = sum_m alpha_m(theta) iota_m(theta) W(theta)^*`. Split the difference `Delta(theta) = V^{Lt} tilde J_L - tilde J_L V^t` at `theta` into the `m = 0` part and the rest. The rest is `sum_{m != 0} alpha_m iota_m (V(xi_m)^{Lt} W^* - W^* V(theta)^t)`. The `iota_m` have orthogonal ranges and the bracket is a difference of two unitaries, so this part has norm at most `2 l(theta) <= 2.66 |theta|^2` by Lemma Z2.3. The `m = 0` part is `alpha_0 iota_0 W^* ((W V(theta/L)^L W^*)^t - V(theta)^t)`. Now `W V(theta/L)^L W^* = exp(-i A)` with `A = W (L h(theta/L)) W^*`, and `V(theta) = exp(-i h(theta))`. For Hermitian `A, B`, `||e^{-iA} - e^{-iB}|| <= ||A - B||` (Duhamel), and `||U_1^t - U_2^t|| <= t ||U_1 - U_2||` for unitaries. It remains to show `||A - h(theta)|| <= 1.5 |theta|^3` for `|theta| <= 1`.

By Lemma Z2.1(2) at `K = theta/L` (`|K| <= 1/2`), using that `h_1` is linear and `h_2` quadratic: `L h(theta/L) = h_1(theta) + h_2(theta)/L + rho_f` with `||rho_f|| <= L |theta/L|^3/2 <= |theta|^3/(2L^2) <= 0.125 |theta|^3`. Put `Y = Y^tr(theta)` and `y = 2 beta ||Y|| <= (sqrt3/2)|theta| <= 0.866`. For any matrix `M`, `W M W^* = e^{i beta ad_Y} M`, so `||W M W^* - M|| <= (e^y - 1)||M|| <= y e^y ||M||` and `||W M W^* - M - i beta [Y, M]|| <= (e^y - 1 - y)||M|| <= (y^2/2) e^y ||M||`. Apply these to `M = h_1(theta)` (`||h_1|| = v|theta|`), `M = h_2(theta)/L` (`||h_2|| <= (v/2)|theta|^2`) and `M = rho_f` (norm kept). With Lemma Z2.2(1), `i beta [Y, h_1] = beta h_2(theta) + beta sum_j theta_j (sin theta_j - theta_j) C_j`, whose last term has norm at most `(v/12)|theta|^4`. Collecting, with `v <= 0.578` and `e^{0.866} <= 2.38`:
\[
 A = h_1 + (\beta + 1/L)\, h_2 + E_1,\qquad \|E_1\| \le (0.516 + 0.298 + 0.125 + 0.049)|\theta|^3 = 0.988|\theta|^3 \le 0.99\,|\theta|^3 .
\]
Since `beta + 1/L = 1` and, by Lemma Z2.1(2) at `K = theta`, `h(theta) = h_1 + h_2 + r_3` with `||r_3|| <= |theta|^3/2`, we get `||A - h(theta)|| <= 1.49 |theta|^3`. Summing the two parts pointwise in `theta` and integrating over the support (Plancherel) gives (3).

(4) Write `tilde J^* P V^{Lt} tilde J - P V^t = tilde J^* P (V^{Lt} tilde J - tilde J V^t) + (tilde J^* P tilde J - P) V^t`. The first term is bounded by (3). The fine sea `P` commutes with fine cell translations, so it is diagonal in `m`, and `tilde J(theta)^* P tilde J(theta) = W (sum_m |alpha_m|^2 P(xi_m)) W^*`. This differs from `W P(theta/L) W^*` by at most `l(theta)^2 <= 1.75 |theta|^4`. Next, `W P(theta/L) W^* = 1_{(-infinity,0)}(A)` with `A` as in (3), because scaling by `L > 0` and conjugating by `W` keep the negative spectral projection; and the coarse sea is `1_{(-infinity,0)}(h(theta))`. The eigenvalues of `h(theta)` are `+-w(theta)`. From `1 - cos w = s^2 (1 - chi)`, `1 - chi = (2/3) sum_j sin^2(theta_j/2) >= 2|theta|^2/(3 pi^2)` and `1 - cos w <= w^2/2`, we get `w(theta) >= 2v|theta|/pi =: g`. With `delta = 1.5|theta|^3` and `|theta| <= sqrt(v)/2`, `delta/g <= (3 pi/(4v))|theta|^2 <= 3pi/16 < 0.59`. Lemma Z2.4 gives `||1_{(-inf,0)}(A) - P(theta)|| <= 2 delta/(2g - delta) <= (2/(2 - 3pi/16)) delta/g <= 1.4175 delta/g <= (3.340/v)|theta|^2`. Adding `1.75|theta|^4 <= 0.44 v |theta|^2 <= (0.15/v)|theta|^2` (since `v^2 <= 1/3`) gives the static bound `(3.5/v)|theta|^2`. The `V^t` factor keeps the momentum support. For `1 - P` (referee closure, ZM1_REFEREE.md): For `t ∈ N`, expand and use `J̃^* J̃ = 1`:
\[
 \tilde J^*(1-P)V^{Lt}\tilde J-(1-P_c)V^t=\tilde J^*(1-P)\big(V^{Lt}\tilde J-\tilde JV^t\big)-\big(\tilde J^*P\tilde J-P_c\big)V^t .
\]
The first term is bounded by Theorem Z2(3). The second is bounded by the static bound `(3.5/v)κ^2` of the proof of (4), since `V^t` keeps the momentum support. So the `1 - P` operator obeys the same bound as the `P` operator, `((3.5/v + 2.66)κ^2 + 1.5 t κ^3)‖f‖‖g‖`. With `tκ <= 1` this gives Corollary Z2.1's constant for every two-point function. □

[check] `check_z2.py`: over `eps in {0.05, 0.3, 0.7, 1.2, 1.5}`, `L in {2, 3, 4, 7}` and 60 random `theta` with `|theta| <= 1`, `max ||W L h(theta/L) W^* - h(theta)|| / |theta|^3 = 0.039`, below the proved `1.5`; `max ||Y^tr(theta)||/|theta| = 0.430 <= sqrt3/4 = 0.433`. `check_static.py`: over `eps in {0.1, 0.4, 0.8, 1.3}`, `L in {2, 3, 5}` and 40 random `theta` with `|theta| <= sqrt(v)/2`, the static mismatch `||tilde J(theta)^* P tilde J(theta) - P(theta)||` is at most `0.0018` times the proved bound `(3.5/v)|theta|^2`.

**GAP Z2-spatial.** The proof assumes momentum support `|theta| <= La/r`; physical separation `r` alone does not imply that support. The displayed bound concerns normalized band-limited two-point functions, not arbitrary separated local block observables. It also only controls times `t <= 1/kappa`. The estimates do not prove the full ZM1(a)1–3, an exact fixed point, the interacting gauge sector, or bounds on every irrelevant term. The family `Phi_{2^k}` is not shown to compose into a tower.

**Higher correlations** (referee closure, ZM1_REFEREE.md)

**Normally ordered `2n`-point functions.** Write `P_c` for the coarse sea projection. Let `n >= 1`, `T ∈ N`, `κ <= √v/2`, and `β = (3.5/v + 2.66)κ^2 + 1.5 T κ^3`. Let `u_1, …, u_n, w_1, …, w_n` be unit coarse one-body vectors with momentum support in `|θ| <= κ`, and let `s_i, s'_i ∈ {0, …, T}`. Let `F` be the fine sea expectation of `Π_i α^{L s_i}(Φ_L(c_1(u_i)))^* · Π_i α^{L s'_i}(Φ_L(c_1(w_i)))`, with the annihilators in reverse order. Let `F_c` be the coarse sea expectation of the same product with `α_1^{s}` in place of `α^{Ls}`. Then `|F - F_c| <= n^{(n+2)/2} β`.

*Proof.* `Φ_L(c_1(h)) = c(J̃h)`, and `α^{Ls}` sends `c(h')` to `c(V^{-Ls} h')`. Both seas are gauge-invariant quasi-free states. `LW1.md` line 107 defines them by "`ω_G(c_y^† c_x) = G_{xy}`, vanishing unequal-creation/annihilation moments, and Wick's determinant rule for the remaining moments". So `F = det M` with `M_{ik} = <w_i, J̃^* P V^{L(s'_i - s_k)} J̃ u_k>`, and `F_c = det N` with `N_{ik} = <w_i, P_c V^{s'_i - s_k} u_k>`. Here `P` commutes with `V`. Every entry has modulus at most 1. By Theorem Z2(4), and by its adjoint when `s'_i < s_k`, `|M_{ik} - N_{ik}| <= β`. Write `det M - det N = Σ_{k=1}^n det C_k`, where `C_k` has the columns `N_1, …, N_{k-1}, M_k - N_k, M_{k+1}, …, M_n`. Hadamard's inequality `|det C| <= Π_k ‖C e_k‖` follows from `C = QR`: `|det C| = Π_k |R_{kk}| <= Π_k ‖R e_k‖ = Π_k ‖C e_k‖`. The columns of `M` and `N` have norm at most `√n`, and `M_k - N_k` has norm at most `√n β`. So `|det C_k| <= n^{n/2} β`, and the sum is at most `n^{(n+2)/2} β`. □

Together with the CAR, the normally ordered functions determine all correlation functions of the block fields. So `p = 2` holds for every fixed number of band-limited fields. This closes the higher-correlation item identified in `ZM1_REFEREE.md` §2.3 and nothing more.

**Corollary Z2.1 (band-limited free comparison).** For every `k >= 1`, take `L = 2^k`, `B_k = Phi_{2^k}` and `L_k` = the free walk at spacing `2^k a`. Take block fields whose momentum support satisfies `|theta| <= kappa = 2^k a/r`. For `kappa <= sqrt(v)/2` and times `t <= r/(2^k a)` coarse ticks, every two-point correlation of `L` in its sea equals that of `L_k` in its sea up to
\[
 \Big(\frac{3.5}{v} + 2.66 + 1.5\Big)\Big(\frac{2^k a}{r}\Big)^2 \|f\|\,\|g\| ,
\]
with constants independent of `k`. Thus this restricted comparison has `p = 2`. The chosen effective walks are identical, though an exact fixed point or compatible tower is not proved; its long-distance content is the Clifford cone `v sum_j K_j G_j` of `MT1.md` Theorem 7, four Weyl fields per cell for `L_cube` and twenty for `L5-U` (`MT1.md` Theorem 11). The zoomed generator is `h_1 + h_2/L + O(|theta|^3/L^2)`; `h_2/L` is a basis rotation (Lemma Z2.2), and the first correction in the spectrum is the cubic term of `LW1.md` C1, with relative size `(|theta|^2/L^2)(s^2/72 - T_4(n)/24)`; its direction-dependent part is the anisotropy. `L_k` has the fine site content, PS-5 for the five-mode law; this alone does not settle ZM1-ii.

*Proof.* Theorem Z2 at `L = 2^k`, with `t kappa <= 1`. The spectral scaling: the eigenvalues of `W L h(theta/L) W^*` are `L w(theta/L)`, and `LW1.md` C1 gives `L w(theta/L) = v|theta|(1 + (|theta|^2/L^2)(s^2/72 - T_4(n)/24) + O(|theta|^4/L^4))`. □

**Corollary Z2.2 (`L5-O`).** Let `W_f` and `W_c` be the site-phase gauges `i^{x_1+x_2+x_3}` on fine and coarse sites. Then `tilde J^O = W_f tilde J_L W_c^*` (with `F = 5`) carries the `L5-O` free walk `W_f (V x 1_5) W_f^*` to the coarse `L5-O` free walk with the same bounds (3)-(4), coarse momenta now measured from the coarse node `Pi`. In the real (Majorana) frame of `L5-O` its kernel is real, so `Gamma(tilde J^O)` commutes with the global `SO(10)`. Coarse translations are intertwined up to the global parity `(-1)^{N}` when `L` is even.

*Proof.* Conjugation by the two gauges carries every identity in Theorem Z2 to the `O` frame and keeps all norms. Reality of `W_f J_L W_c^*`: its entry between coarse site `2u + r` and fine site `2c + r` is `(-1)^{sum c_i + sum u_i} psi^(3)(c - Lu)`, since the residue phases `i^{sum r_i}` cancel; it is real. Reality of the twist: the `O` walk is real orthogonal on each Majorana flavour (`LW1_5.md` A2-5: the one-body hop is `i` times a real antisymmetric matrix), so its principal logarithm is `i` times a real antisymmetric matrix. Position-space reality of a matrix `X` means `conj(hat X(theta)) = hat X(-theta)`. Write coarse momenta as `Pi + k`; since `-Pi = Pi` mod `2 pi`, reality reads `conj(hat X(Pi + k)) = hat X(Pi - k)`, and for the generator `h^O` (imaginary in position space) `conj(hat h^O(Pi + k)) = -hat h^O(Pi - k)`. Comparing Taylor terms in `k` gives `conj(G^O_j) = G^O_j` and `conj(C^O_j) = -C^O_j`; hence `conj(Y^O(k)) = Y^O(k) = -Y^O(-k)`, and `conj(exp(i beta Y^O(k))) = exp(i beta Y^O(-k))`, which is reality of `W_c cal W W_c^*`. A real one-body map acting as the identity on the ten Majorana flavours commutes with `SO(10)`. For even `L`, the entry carries the extra factor `(-1)^{(L+1) sum u_i} = (-1)^{sum u_i}` relative to a translation-invariant kernel, which is the global parity on odd coarse translates. □

**Remark (massive free tick).** For `mu > 0`, `V(0) = e^{i a_o R} e^{-i a_e R} = e^{i mu R}` (Lemma Z2.0(2) at `K = 0`), so `V(0)^L = e^{i L mu R}`: in coarse units the mass is `L mu` (while `L mu < pi`), a relevant parameter. `LW1.md` B10(4) gives `|P_xy| <= C e^{-kappa_dec |x - y|}` for the free sea. Hence equal-time sea correlations of block fields with exponentially local kernels and supports at distance `r` decay like `e^{-kappa' r}`. This proves exponential decay of these equal-time two-point functions, not absence of all long-distance dynamical content.

---

## 5. The first interacting step (question Q-I)

The dressed base tick replaces the c-number links of the free tick by the finite registers of PS-6r. Its Gauss generators are `G_x = n_x + sum_out E - sum_in E` (`L_cube`), `G^T_x = c_x^dag T c_x + sum_l r^dag_{l,x} T r_{l,x}` with `T` a Hermitian `5 x 5` matrix (`L5-U`), and `G^{cd}_x = M^{cd}_x + sum_l L^{cd}_{l,x}` (`L5-O`). Each commutes with the tick (`LW1.md` B4; `LW1_5.md` G, U).

### 5.1 Gauge covariance of a block map

Definition G and its proposed four-test assessment are in §1.4.

### 5.2 Content forced by the embedding

**Theorem Z4.** Let `Phi` satisfy (G1). Let `D_u` be the dimension of the finite-dimensional coarse algebra generated by the coarse site `u` and the ends of its coarse links (it contains `G^{(1),T}_u`). Then `D_u >= n_0 |S_u| + 1`, with `n_0 = 5` for `L5-U` and `n_0 = 1` for `L_cube` and `L5-O`. For the block-constant embedding, `D_u >= 40 L^3 + 1` (`L5-U`) or `8L^3 + 1`: unbounded.

*Proof.* Take `T_0 = 1` for `L5-U` and `L_cube`, and `T_0 = M^{12}` for `L5-O`. An injective homomorphism preserves polynomial identities in both directions: `p(G^{(1),T_0}_u) = 0` if and only if `p(Phi(G^{(1),T_0}_u)) = 0`. So `G^{(1),T_0}_u` and `H = sum_{x in S_u} G^{T_0}_x` have the same minimal polynomial and the same number of distinct eigenvalues. A Hermitian element of an algebra of dimension `D_u` has a minimal polynomial of degree at most `D_u`, so at most `D_u` distinct eigenvalues. `H` is the sum of a matter part (`sum_{x in S_u} N_x`, `sum n_x`, or `sum (n_{x,1} - 1/2)`) and a link part, acting on different tensor factors and commuting. Its eigenvalues include the matter values plus one fixed link eigenvalue: at least `5|S_u| + 1`, `|S_u| + 1` and `|S_u| + 1` values. □

So bounded content needs `|S_u|` bounded independently of `L`: the coarse gauge group must act on a bounded number of fine sites per block.

### 5.3 No linear block fermion on finite links

**Theorem Z3.** Let `Phi` satisfy (G1) and (G2). Let `psi` be a coarse fermion mode at coarse site `u` (`psi^2 = 0`, `{psi, psi^*} = 1`, fixed by coarse gauge transformations at every `u' != u`), or a coarse Majorana mode. Suppose `Psi = Phi(psi)` is linear in fine matter:
\[
 \Psi = \sum_\alpha \big(T_\alpha c_\alpha + T'_\alpha c^\dagger_\alpha\big),
\]
a finite sum over fine matter modes `alpha = (x, j)`, with `T_alpha, T'_alpha` in the finite-dimensional algebra of finitely many links. Then `T_alpha = T'_alpha = 0` for every mode `alpha` at a site `x` outside `S_u`.

*Proof.* *(a) Invariance.* Let `x` be outside `S_u`. If `x` lies in no `S_{u'}`, (G2) makes `Psi` fixed by all fine gauge transformations at `x`; put `S' = {x}`. If `x in S_{u'}` with `u' != u`, then `psi` is fixed by `exp(i theta G^{(1),T}_{u'})`, and since `Phi` is a *-homomorphism with (G1), `Psi` commutes with `sum_{y in S_{u'}} G^T_y`; put `S' = S_{u'}`. In both cases `Psi` commutes with `H_T = sum_{y in S'} G^T_y` for every `T`.

*(b) Majorana reduction.* Put `Psi_1 = Psi + Psi^*` and `Psi_2 = -i(Psi - Psi^*)`. Both are Hermitian, linear in matter, commute with every `H_T` (which is Hermitian), and satisfy `Psi_k^2 = 1` (expand, using `Psi^2 = 0` and `{Psi, Psi^*} = 1`). If `psi` is Majorana, take `Psi_1 = Psi`. It suffices to prove the claim for a Hermitian `Psi_k = sum_alpha (T_alpha c_alpha + T_alpha^* c_alpha^dag)`; Hermiticity forces this form.

*(c) Normality.* Link operators commute with matter (`LW1.md` §1; `LW1_5.md` §1). Expanding,
\[
 \Psi_k^2 = \sum_\alpha \big(T_\alpha T_\alpha^*(1 - n_\alpha) + T_\alpha^* T_\alpha n_\alpha\big) + (\text{terms with } c_\alpha c_\beta,\ c_\alpha c^\dagger_\beta,\ c^\dagger_\alpha c_\beta,\ c^\dagger_\alpha c^\dagger_\beta,\ \alpha\ne\beta).
\]
Take matter matrix elements between equal occupation basis vectors: the second group has none. So for every occupation pattern `sigma`, `sum_alpha (T_alpha T_alpha^* (1 - sigma_alpha) + T_alpha^* T_alpha sigma_alpha) = 1`. Comparing the empty pattern with the pattern occupied only at `alpha_0` gives `T_{alpha_0}^* T_{alpha_0} = T_{alpha_0} T_{alpha_0}^*`: each `T_alpha` is normal.

*(d) Grading.* Fix a mode `alpha = (x, j)` with `x` in `S'`. Choose `T` with matter part `n_{x,j}` up to a constant: `T = 1` (`L_cube`), `T = E_{jj}` (`L5-U`), `T = M^{2j-1,2j}` (`L5-O`). Then `H_T = sum_{y in S'} n_{y,j} + const + Lambda`, where the link part `Lambda` is a finite sum of end generators: Hermitian, with finitely many eigenvalues on the finite-dimensional link algebra involved. Now `[H_T, T_beta c_beta] = ([Lambda, T_beta] - q_beta T_beta) c_beta` with `q_beta = 1` if `beta = (y, j)`, `y in S'`, and `0` otherwise; similarly with `+q_beta` for `c^dag_beta`. The elements `c_beta, c^dag_beta` are independent over the link algebra (take matrix elements between occupation patterns differing at `beta`). So `[H_T, Psi_k] = 0` gives `[Lambda, T_alpha] = T_alpha`. Then `T_alpha` maps the `lambda`-eigenspace of `Lambda` into the `(lambda + 1)`-eigenspace, so it is nilpotent. A normal nilpotent matrix is zero: its norm equals its spectral radius. □

Step (d) strengthens `GA2_Y2.md` Theorem 2.1 and Corollary 2.2, which show that a charged operator on a finite register is not invertible: here it is nilpotent, so a normal one is zero.

**Theorem Z3′: norm limits of linear fields** (referee closure, ZM1_REFEREE.md)

**Definitions.** `𝔏` is the C*-algebra generated by all link operators. It commutes with matter (`LW1.md` line 52; `LW1_5.md` line 33). `ℒ` is the norm closure of the set of finite sums `Σ_α (T_α c_α + T'_α c^†_α)` with `T_α, T'_α ∈ 𝔏`. For a mode `α` and `φ ∈ R`, `θ^φ_α` is conjugation by `e^{iφ n_α}`. It sends `c_α` to `e^{-iφ} c_α` and fixes every other mode and `𝔏`. Put `Π^{(1)}_α(X) = (1/2π) ∫_0^{2π} e^{iφ} θ^φ_α(X) dφ` and `Π^{(2)}_α(X) = (1/2π) ∫_0^{2π} e^{-iφ} θ^φ_α(X) dφ`.

*Four tests* (for reading "linear in fine matter" as membership in `ℒ`). (1) It states no target. (2) It is closed. (3) It settles no physics; it only extends Z3's class to norm limits. (4) It adds no structure or constant.

**Coefficients.** `Π^{(1)}_α` and `Π^{(2)}_α` are contractions. On a finite sum they return `T_α c_α` and `T'_α c^†_α`. The map `T -> T c_α` is isometric on `𝔏`: `(T c_α)^*(T c_α) = T^*T n_α`, and `‖T^*T n_α‖ = ‖T^*T‖` because the two factors lie in commuting tensor factors. Its image is therefore closed. So each `X ∈ ℒ` has unique coefficients `T_α(X), T'_α(X) ∈ 𝔏` with `Π^{(1)}_α(X) = T_α(X) c_α` and `Π^{(2)}_α(X) = T'_α(X) c^†_α`. They depend continuously on `X`.

**Theorem Z3′.** Let `Φ` satisfy (G1) and (G2), and let `ψ` be as in Theorem Z3. If `Ψ = Φ(ψ) ∈ ℒ`, then `T_α(Ψ) = T'_α(Ψ) = 0` for every mode `α` at a site outside `S_u`.

*Proof.* (a) As in Z3, `Ψ` commutes with `H_T = Σ_{y ∈ S'} G^T_y` for every `T`; this step does not use finiteness. (b) `Ψ_1 = Ψ + Ψ^*` and `Ψ_2 = -i(Ψ - Ψ^*)` lie in `ℒ`, are Hermitian, square to 1 and commute with every `H_T`. By continuity `T_α(Ψ_1) = T_α + T'^*_α` and `T_α(Ψ_2) = -i(T_α - T'^*_α)`, and `T'_α(Ψ_k) = T_α(Ψ_k)^*`. So it suffices to show `S_α := T_α(Ψ_k) = 0` for `α` outside `S_u`.

(c) *Normality.* Fix `α_0` and write `c = c_{α_0}`, `n = n_{α_0}`, `S = S_{α_0}`, `A = S c + S^* c^†` and `R = Ψ_k - A`. Subtract the continuous `α_0`-parts from finite approximants of `Ψ_k`. This shows that `R` is a norm limit of odd finite sums over modes `β ≠ α_0`. So `R` is odd and lies in the C*-algebra `𝔅` generated by `𝔏` and the modes `β ≠ α_0`. Hence `R^2` is even in `𝔅`, commutes with `c` and `c^†`, and is fixed by `θ^φ_{α_0}`. Let `E_0(X) = (1/2π) ∫ θ^φ_{α_0}(X) dφ`. Then `E_0(AR + RA) = 0`, `E_0(A^2) = A^2 = SS^*(1 - n) + S^*S n` and `E_0(R^2) = R^2`. So `1 = E_0(Ψ_k^2) = SS^*(1 - n) + S^*S n + R^2`. Multiplying by `1 - n` and by `n` gives `(1 - n) Y_1 = 0` and `n Y_2 = 0`, with `Y_1 = SS^* + R^2 - 1` and `Y_2 = S^*S + R^2 - 1`. Both commute with `c` and `c^†`. Then `n Y_1 = c^†(1 - n) c Y_1 = c^†((1 - n)Y_1) c = 0`, so `Y_1 = 0`. Likewise `(1 - n) Y_2 = c (n Y_2) c^† = 0`, so `Y_2 = 0`. Hence `SS^* = 1 - R^2 = S^*S`.

(d) *Grading.* Fix `α = (x, j)` with `x ∈ S'`, and choose `T` as in Z3(d). Then `H_T = Σ_{y ∈ S'} n_{y,j} + const + Λ`, with `Λ ∈ 𝔏` Hermitian of finite spectrum `λ_1 < … < λ_N`. `θ^φ_α` fixes `H_T`, so `0 = Π^{(1)}_α([H_T, Ψ_k]) = [H_T, S_α c_α] = ([Λ, S_α] - S_α) c_α`. Injectivity of `T -> T c_α` gives `[Λ, S_α] = S_α`. With the spectral projections `P_i ∈ 𝔏` of `Λ`, this reads `(λ_i - λ_k - 1) P_i S_α P_k = 0`. So `S_α` maps each eigenspace into the next one up, and `S_α^N = 0`. `S_α` is normal by (c), and a normal element has norm equal to its spectral radius. So `S_α = 0`. □

**Consequence for Attack 1.** Let `Ψ_u` be the Attack 1 series in §5.4. Suppose some grouping of its partial sums converges in norm. Then the limit lies in `ℒ`, and its coefficient at `(x, k)` is `J̃_{x,u} T^{jk}_{x -> x_u}`, because the coefficient maps are eventually constant on the partial sums. For `L5-U` the operators `r^y_j r^{x†}_k` on one link are linearly independent (`LW1_5.md` line 117). So along a path with distinct links the contracted product `T_{x -> x_u}` is nonzero. `J̃_L e_u` is not supported on one site, for every `L >= 2`. The norm of its fine Bloch transform is proportional to `|ψ̂^(3)(K)|` (`ZM1_REFEREE.md` §3.8). This is nonzero at `K = 0`, and zero at `K = 2πm/L` with `m ≢ 0 mod L`, because `B(2πm_i/L) = 0` when `m_i ≢ 0`. A one-site vector has a Bloch transform of constant norm. So `J̃_{x,u} ≠ 0` for some `x ≠ x_u`. Theorem Z3′ forbids this, so `Ψ_u` is not a fermion field. If no grouping converges, the series defines no element of the algebra. Corollary Z3.1 holds for `ℒ` with the same proof.

**Corollary Z3.1 (finite operator-level transported averages).** Let `Phi` satisfy (G1)-(G2) and have bounded content `D_u <= D`. Then every coarse fermion field of the finite purely linear form in Z3 has coefficients on at most `(D - 1)/n_0` fine sites, a number independent of `L` (Theorems Z3, Z4). The same conclusion holds for the norm-closed class `ℒ` by Theorem Z3′. In particular, a linear transported block average `psi_B = sum_{x in beta_u} (transport from x to the centre) psi_x` with nonzero weight at each site of the block, is never a coarse fermion field on PS-6r links once `8L^3 > (D - 1)/n_0`. **Named failing step:** "the transport coefficients at sites other than the block centre can be nonzero." They are normal (step (c), from the anticommutation relations) and raise a bounded grading (step (d), from the finite registers), hence they vanish.

**Scope.** Theorem Z3 concerns operator-level block maps (Definition Z). It does not touch measure-level block maps of a Euclidean form of the law, where block fields are Grassmann integration variables and need no anticommutation relations; that route needs Y1 and ZM1-G (`GA2_Y2.md`), both open. It does not touch nonlinear block fields either. For example, `Psi = W c_{x_u} W^*` with a gauge-invariant local unitary `W` (a finite circuit of dressed hops) obeys the anticommutation relations, (G1) with `S_u = {x_u}`, and (G2), and can spread over a block. Thus this example allows a nonlinear spread field; extending it to a covariant, translation-consistent block map with a coarse law is a separate obligation.

### 5.4 The open lemma, two attacks, and a subspace attack

**ZM1-I1 (open; precise statement)** (referee closure, ZM1_REFEREE.md) Let `ω_0` be a vacuum that VC1 supplies for `L5-U[m]` (base tick, or with a plaquette class that GA1-P-5 supplies). There exist `L >= 2`, `p >= 1`, `C, κ_0 > 0`, a block map `Φ` of factor `L` (Definition Z) satisfying (Z-a), (Z-b) and (G1)–(G2) with `|S_X| = 1` for every coarse site `X`, a coarse law `α_1` of the `L5-U` form, and an `α_1`-invariant state `ω_1` of `A_1`, with the following property. For all `κ ∈ (0, κ_0]`, all `t ∈ N` and all unit coarse one-body vectors `f, g` with momentum support in `|θ| <= κ`,
\[
 \big|\omega_0\big(\Phi(c_1(f))^*\,\alpha^{Lt}(\Phi(c_1(g)))\big)-\omega_1\big(c_1(f)^*\,\alpha_1^{t}(c_1(g))\big)\big|\le C(\kappa^p+t\kappa^{p+1}).
\]

(referee closure, ZM1_REFEREE.md)

**Lemma R-GI.** Let `Φ` satisfy (G1)–(G2) with `S_X = {x_X}` for every coarse site `X`. Let `ψ_X` be a coarse matter annihilator at `X` with `[G^{(1),1}_X, ψ_X] = -ψ_X`, fixed by coarse gauge transformations at every `X' ≠ X`. Put `Ψ_X = Φ(ψ_X)`. Suppose `ω_0` is invariant under conjugation by `e^{iθ G^1_x}` for every site `x` and every `θ ∈ R`. Then `ω_0(Ψ_X^* α^n(Ψ_Y)) = 0` for all `X ≠ Y` and all `n ∈ Z`. The same holds for a coarse state invariant under every coarse gauge transformation `e^{iθ G^{(1),1}_X}`.

*Proof.* Let `x = x_X`. The sets `S` are disjoint, so `x ∉ S_Y`. By (G1), `Φ(e^{iθ G^{(1),1}_X}) = e^{iθ G^1_x}`, so conjugation by `e^{iθ G^1_x}` acts on `Φ(A_1)` as `Φ` of the coarse gauge transformation at `X`. It fixes `Ψ_Y` and multiplies `Ψ_X` by `e^{-iθ}`. The base tick commutes with `e^{iθ G^1_x}` (`LW1_5.md` line 136, U), and so does any gauge-invariant plaquette layer. So `α^n(Ψ_Y)` is fixed as well. Hence `ω_0(Ψ_X^* α^n(Ψ_Y)) = e^{iθ} ω_0(Ψ_X^* α^n(Ψ_Y))` for every `θ`, and it vanishes. The coarse case is the same computation. □

**Consequence.** Suppose, besides Lemma R-GI's hypothesis on `ω_0`, that `ω_1` is invariant under every coarse gauge transformation, and that `ω_0` and `ω_1` are invariant under the coarse cell translations. Then the bound in the precise statement holds only if `ω_0(Ψ_{X,j}^* α^{Lt}(Ψ_{X,k})) = ω_1(ψ_{X,j}^* α_1^t(ψ_{X,k}))` for every coarse site `X`, all flavours `j, k` and every `t ∈ N`.

*Proof.* Each side is a bounded sesquilinear form in `(f, g)`. For finitely supported `f, g` Lemma R-GI reduces it to the same-site sum `Σ_X Σ_{j,k} conj(f_{X,j}) g_{X,k} (…)`. That sum converges absolutely for `f, g ∈ l^2` and is continuous, so the reduction holds for all `f, g`. Let `D_{X,jk}(t)` be the difference of the same-site terms. By translation invariance it depends on `X` only through its residue `r`. Take a unit coarse-cell profile `φ` with momentum support in `|θ| <= κ`. Let `f` be `φ` on residue `r` and flavour `j`, and `g` be `φ` on residue `r` and flavour `k`. Then the difference equals `D_{r,jk}(t)`, so `|D_{r,jk}(t)| <= C(κ^p + tκ^{p+1})` for every `κ ∈ (0, κ_0]`. Letting `κ -> 0` gives `D_{r,jk}(t) = 0`. □

The choice of observable class for ZM1-I1 is for the lead or the owner.

By Theorems Z3 and Z3′, linear fields in the stated finite and norm-closed classes with nonzero coefficients outside the representative site are excluded; these theorems do not classify general nonlinear fields. ZM1-I1 is the first interacting form of ZM1(a)1; ZM1-G (`GA2_Y2.md`) is its gauge-sector companion.

**Attack 1: minimal coupling of Theorem Z2.** Take `Psi_u = sum_x tilde J_{x,u} T_{x -> x_u} c_x`, with `T_{x -> x_u}` the ordered product of link operators along a fixed path. It fails at the step "`Psi_u` is a fermion field": Theorems Z3 and Z3′ force every coefficient with `x != x_u` to vanish for finite sums and norm-convergent limits; the consequence of Z3′ above covers the kernel of Z2.

**Attack 2: dressing that reduces to Theorem Z2 when links are c-numbers.** Take `Psi_u = W c_{x_u} W^*`, with `W` a finite gauge-invariant circuit of dressed hops chosen so that replacing every link operator `U^{jk}` by `delta^{jk}` turns `W` into `Gamma(w)`, a one-body unitary with `||w delta_{x_u} - tilde J_L e_u|| <= C e^{-R/xi}`, a truncation at radius `R`, using one `W` for all coarse modes. Then Theorem Z2 applies to the reduced map up to that error. It fails at the step "in some state the link operators act as c-numbers, so the dressed circuit is close to its reduction". `GA2_Y2.md` Theorem 3.4: every `L5-U` link has coherence `kappa <= 1/2` in every state, for every value of the free constants (`kappa <= 1/10` for `L5-O[S_+]`). The cited coherence bound excludes the stated near-coherent link criterion. It does not rule out every state-dependent approximation or every c-number reduction; the error bounds of Theorem Z2 have not been transferred.

**GAP Attack 3.** The draft has not classified conserved projections or proved that every tile-local function of Gauss generators must omit every boundary matter degree of freedom. Boundary charges or functions can cancel link dependence. The cited necessary condition also does not prove that a projection rank is the coarse observable content in this setting. The argument therefore does not establish the claimed rank bound or failure of the whole projection route. The following is the proposed attack, not a proof of that conclusion.

**Attack 3: exact renormalisation through conserved projections.** Attack 3 concerns the subspace notion of the cited work. Definition Z needs a unital map, so Attack 3 is not an attack on ZM1-I1 as stated. ZM1-I1 has two failed attacks on file.  By arXiv:2511.23398 Theorem 1, an exact fermionic renormalisation needs a tile projection `Pi_0` in the tile algebra with `[U_{T^N}, Pi] = 0` for `Pi` the product of its translates. Spectral projections of the Gauss generators are examples of exactly conserved local projections. No exhaustive classification is shown. Take tiles as in Theorem Z0 (whole links assigned to the block of their lower endpoint). It fails at the step "the Gauss projection of every site of the tile lies in the tile algebra". At a site on the tile boundary, the Gauss generator involves the end of a link owned by the neighbouring tile. The draft infers that `Pi_0` can only be a function of the Gauss generators of sites whose links all lie in the tile; that inference is not established (GAP Attack 3). Under that extra, unproved restriction, `Pi_0` acts as the identity on the matter of sites on lower faces, at least `(2L)^2` sites, so `rank Pi_0 >= 32^{(2L)^2}`. No general conclusion on bounded content follows.

These are scoped obstructions and unclosed attacks in their respective formulations, not a proof that ZM1-I1 is false. No counterexample is known.



## 6. Scope and remaining decisions

The block maps and Gauss embedding in Definitions Z and G are proposed readings, not working-set changes. Their four-test outcomes above are the draft author's assessments. In particular, homomorphic blocking and the diagonal Gauss embedding add substantive restrictions; passing the tests does not derive them from PS-1c or settle the measure-level alternative.

Z1 excludes a bounded **exact quasi-free** tower, not every nonlinear tower. Z2 gives a bounded-content free comparison for specified band-limited fields and times; it does not close ZM1-ii. Z3 and Z3′ exclude linear transported fields in their stated finite and norm-closed classes under G1–G2, not nonlinear dressed fields. ZM1-I1 depends on an actual VC1 vacuum and a compatible block law. ZM1-G and Y1 remain open. Nothing here proves the GA2 interacting sector or the assembly target.
