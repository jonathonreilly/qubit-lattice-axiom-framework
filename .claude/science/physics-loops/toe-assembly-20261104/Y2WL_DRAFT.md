lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# Y2-W-L: `U(1)`-blind cube loops of `L5-U` and SC-loop, pass 1

Written 2026-11-05 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 under PR #10138's method (part GA2, sub-lemma Y2-W-L of `Y2W_DRAFT.md` section 4). Method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation in `/tmp/toe-y2wl/` on the Mac mini (Python with numpy and scipy; each run under one minute and under 100 MB; floating point; started with 60 to 62 percent of memory free). A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` | `92e03055c` |

No other branch was read. Files read at that commit, by line, all in this folder: `Y2W_DRAFT.md` lines 1-208 (all; last changed `92e03055c`); `GA2_Y2_DRAFT.md` lines 1-215 (all; last changed `7d2b20d29`), in particular Theorem N (line 61), Corollary N5 (line 95) and T0-start[G] (line 211); `LW1_5_DRAFT.md` lines 1-70 and 140-360 (last changed `e648fa3e0`), in particular Theorem U (lines 252-264) and section 8 (lines 298-348); `TOE_ASSEMBLY.md` lines 13-23 (axioms), 169-222 (sections 3.2-3.5), 369-396 (GA1, GA2) and 538-562 (section 6) (last changed `7d2b20d29`).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The law `L5-U`, Definition SC and Definition SC-loop are read plainly. The phrase "`U(1)`-blind block cube products" allows several operators. Each is named (section 1.3), each gets the four tests, and none is adopted.

**Working set used, by name.** PS-5, PS-6 and PS-6r only through the law `L5-U` (`LW1_5_DRAFT.md` Theorem U and section 8.1). PS-7r only through its sentence "the vacuum is the state VC1 builds". Results used, by name: Definition SC, Definition SC-loop, Lemma 0, Theorem W1, Theorem W2 and Lemma W4 of `Y2W_DRAFT.md`; T0-start[G] of `GA2_Y2_DRAFT.md` (only as the source of the measure `μ` in Lemma 0); Theorem U of `LW1_5_DRAFT.md`.

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text: the canonical anticommutation relations; conjugation of a fermion Fock space by a product of Majorana operators; the central idempotents of the group algebra of the symmetric group `S_3`; `Λ^6(C^5) = 0`; telescoping norm bounds. Standard mathematics used only to guide the [check]s, never as a proof step: Schur-Weyl duality and Howe duality for `U(5) × U(3)` acting on `Λ(C^5 ⊗ C^3)` (Schur; Weyl; Howe). Literature context, credited from memory and never load-bearing: quantum link models and rishons (Horn; Orland-Rohrlich; Chandrasekharan-Wiese, Nucl. Phys. B 492 (1997); Brower-Chandrasekharan-Wiese, Phys. Rev. D 60 (1999)); Kogut-Susskind Hamiltonian lattice gauge theory.

---

## 0. The question, quoted

`Y2W_DRAFT.md` line 159: "**Y2-W-L (block loop window for `L5-U`).** Fix ZM1's block map and the class `𝒲_r` of `U(1)`-blind block cube products `Θ^{(r)}_c` at scale `r` (Attack 1). Let `ω` be the state VC1 supplies. Is there a choice of constants (`m`, `ε`, `μ`, `τ_E`, a plaquette class with its constant) and a scale `r = a_{k0}` such that SC-loop(`r`; `η_*`) holds for `𝒲_r`, with `η_* = 8ε_μ(g_*) + 6δ`?"

Line 161: "If Y2-W-L fails for every choice, then (A) holds: no window". Line 162: "If it holds, the plaquette-level necessary condition holds, and (B) then needs ZM1-G in full". So in this file (A) means "no window for `L5-U`" and (B) means "a window exists". Line 163: "**Y2-W-L0** is finite-dimensional and kinematic: is `inf_ω inf_c D_ω(cΘ_c) > η_*` on the twelve links of one cube? It is open."

Line 62: "**SC-loop(r; η)** holds in `ω` if there is `c ∈ C∖{0}` with `D_ω(cW) ≤ η` for every `W ∈ 𝒲_r`." Line 47 defines `D_ω(Y) := ω((Y−1)^†(Y−1)) + ω((Y−1)(Y−1)^†)`.

Line 141 (Attack 1) names the cube product: "The framework's `Θ_c = Π_f W_f` contains, on each of the twelve edges, one `𝐔_ℓ` and one `𝐔_ℓ^†`. So `[N^x_ℓ, Θ_c] = 0` for every `ℓ`". The order of the six factors is not fixed there. Section 2 shows that the order matters.

`LW1_5_DRAFT.md` line 254 (Theorem U): "ten complex rishon modes `r^{ℓ,y}_j`, `r^{ℓ,x}_k` (`j, k = 1, …, 5`), fermionic among themselves, in an ordinary tensor factor that commutes with matter, restricted to a sector of fixed total rishon number `m`, `1 ≤ m ≤ 9`. Put `U_ℓ^{jk} = r^{ℓ,y}_j r^{ℓ,x†}_k`". Line 318 makes `m` a free datum of `L5-U`.

`TOE_ASSEMBLY.md` line 214: "The owner chose: **keep both live.** MT1, GA1 and CG1 are developed on both laws until one fails at a named step."

## 0.1 Outcome in one paragraph

**The answer depends on which operator stands for the cube product, and this file decides each case.** The Wilson function `Θ = Π_f w_f` does not depend on the order of its six faces; the framework's products `Θ^σ_c` do. Three readings: one fixed order (F), the product averaged over all 720 orders (S), every order at once (B). F fails test 4. S passes all four tests. B passes tests 1-3 and passes test 4 only if one accepts its reason, Definition SC's own two-order clause. **Structure (proved, every `m`, every scale):** a cube product factorises into one operator per corner. At each corner one or two link ends are "particle ends", and the corner operator is a trace of three `5 × 5` matrices `E` or `1 − E` built from rishon bilinears (Lemmas C, K, T). **Y2-W-L0 (one cube, lattice scale), decided.** Under F and S, `D = 0` is attained for every `m`. Under B, `D = 0` is attained for every `m ∈ {2, …, 8}`, by corner states that are antisymmetric in three colours and carry the other colours as spectators. For `m ∈ {1, 9}` under B, the orders `σ` and reversed `σ` give `D + D ≥ 2` in every state. **General scale, one block cube:** the same results hold at every scale. **All cubes at once.** Under S, an explicit flux state meets SC-loop with `η = 0` at every scale and for every `m`: each `e_1`-link holds its rishons at its even end, each `e_2`- and `e_3`-link at its odd end (Theorem S∞). So under S no kinematic floor exists, and a proof that Y2-W-L fails needs the state VC1 supplies. Under B, floors hold at every scale for `m ∈ {1, 9}` (`max D ≥ 1`) and for `m ∈ {2, 8}` (a sum of 28 values of `D` is at least `1/16200`). Under B with `m ∈ {3, …, 7}`, the all-cube question is open after three named attacks (Y2-W-LB). **What the counterexamples are.** The states that meet SC-loop have link coherence `κ = 0`, and SC's own two-order clause on plaquettes excludes them. So SC-loop on `U(1)`-blind loops is met by states that SC excludes. **`L5-O`.** L5-O's register knob raises the coherence; the states that meet SC-loop here have none, so this test cannot separate the laws under S. Under B, L5-U's floors come from the small rishon register (an empty or full end; six one-rishon ends in five colours). **No named failing step for `L5-U` as a law.** Under B, the free datum `m` would be confined to `{3, …, 7}`, given the hypotheses of Lemma 0′ (section 6); recorded, not proposed.

---

## 1. Which loops count as `U(1)`-blind

### 1.1 Notation

`L5-U` as in section 0. A link is `ℓ = (x, y)` with `y = x + e_i`. Its rishons are `r^{ℓ,x}_a`, `r^{ℓ,y}_a`, `a = 1, …, 5` ("colours"). For an end `v ∈ {x, y}` put the end operators

\[
E^{\ell,v}_{ab} := r^{\ell,v\dagger}_a\, r^{\ell,v}_b ,\qquad N^{\ell,v} := \textstyle\sum_a E^{\ell,v}_{aa}.
\]

`E^{ℓ,v}` denotes the `5 × 5` matrix of these operators. `N^{ℓ,x}` is Y2W's `N^x_ℓ`. Each `E^{ℓ,v}_{ab}` is even in the rishon modes. So end operators of different ends commute, also the two ends of one link. `(E^{ℓ,v}_{ab})^† = E^{ℓ,v}_{ba}`.

`𝐔_ℓ` has entries `U^{jk}_ℓ` (row `j` at `y`, column `k` at `x`). A step of a lattice path along `ℓ` in its direction uses `𝐔_ℓ`; a step against it uses `𝐔_ℓ^†`. For a closed path `C`, `W_C` is the trace of the ordered product, as in `Y2W_DRAFT.md` section 1.1. A step "starts" at its tail and "ends" at its head.

**Block scale and block faces.** `r = L^k a` with `n := L^k` fine links per block edge. For a block plaquette `f` of side `r`, the **boundary-loop block face** is `W^{(r)}_f := W_{∂f}`, the trace around the closed fine path `∂f`. A block cube `c` has six faces, oriented outward. An **order** `σ` lists the six faces; `Θ^σ_c := W^{(r)}_{σ(6)} ⋯ W^{(r)}_{σ(1)}`, so `σ(1)` acts first. At `r = a` this is the cube of Y2W line 141 in the order `σ`. `σ^{rev}` is the reversed list. The **skeleton** of `c` is the set of fine links on its twelve block edges; its points are the eight block corners and the `12(n − 1)` inner points of block edges.

### 1.2 The definition

**Definition UB (`U(1)`-blind loop product).** An ordered product `Θ = W_{C_k} ⋯ W_{C_1}` of loop traces is `U(1)`-blind if every link is traversed by the paths `C_1, …, C_k` as often along its direction as against it. Its Wilson image `ι(Θ) = Π_i w_{C_i}` is then unchanged under `U_ℓ ↦ e^{iθ_ℓ}U_ℓ` for every choice of the `θ_ℓ`.

**Lemma B0.** A `U(1)`-blind product commutes with every `N^{ℓ,x}`.

*Proof.* `[N^{ℓ,x}, U^{jk}_ℓ] = U^{jk}_ℓ`, since `U^{jk}_ℓ = r^y_j r^{x†}_k` adds one rishon at `x`. Taking adjoints, `[N^{ℓ,x}, (U^{jk}_ℓ)^†] = −(U^{jk}_ℓ)^†`. Operators of other links commute with `N^{ℓ,x}`. Expand `Θ` into products of entries. Each product shifts `N^{ℓ,x}` by the number of steps along `ℓ` minus the number against it, which is zero. ∎

Every block cube product `Θ^σ_c` is `U(1)`-blind: each fine link of the skeleton lies in exactly two block faces, which traverse it in opposite directions.

### 1.3 Three readings of "the cube product"

The Wilson function `Θ_c = Π_f w_f` is one function. Its framework images `Θ^σ_c` differ for different `σ` (Lemma K below). Three readings:

- **F (one fixed order).** `𝒲^F_r = {Θ^{σ_0(c)}_c}` for a rule `c ↦ σ_0(c)` fixed in advance.
- **S (symmetrised).** `𝒲^S_r = {Θ^S_c}` with `Θ^S_c := (1/720) Σ_σ Θ^σ_c`.
- **B (every order).** `𝒲^B_r = {Θ^σ_c : σ an order}`, 720 operators per cube.

Y2-W-L0 uses one unit cube. Y2-W-L uses all block cubes at scale `r`.

**Remark (how B and S relate).** Suppose one vector is an eigenvector of every `Θ^σ_c` and every `(Θ^σ_c)^†` with one eigenvalue `λ`, `λ̄`. Then every weighted sum `Σ_σ w_σ Θ^σ_c` has eigenvalue `λ Σ_σ w_σ`. So a state that meets B meets every ordering convention whose weights do not sum to zero. A failure of B does not imply a failure of S.

### 1.4 Four-test check

Tests (`LW1_5_DRAFT.md` line 328): "(1) states or fixes a part's target; (2) open-ended; (3) settles a downstream physics question by premise; (4) adds structure or constants its own reasons do not need."

| Item | (1) | (2) | (3) | (4) | Result |
|---|---|---|---|---|---|
| Definition UB | pass: names no target | pass: a closed condition on a given family of paths | pass | pass: it is the condition of Y2W line 141 | passes |
| boundary-loop block faces | pass | pass once `r` is pinned | conditional: ZM1 may use smeared block links; results below are claimed for boundary-loop faces only | pass: no constants | passes as a stand-in for ZM1's block map, conditional on ZM1 |
| F | pass | pass | pass as a question | fails: no reason supplies a fixed order; `ι` is order blind and the cube's rotations permute faces, so `σ_0` breaks a symmetry of the question | fails test 4; results recorded for comparison only |
| S | pass | pass: one operator per cube | pass as a question. Adopted as ZM1-G's convention by premise it would fail | pass: no constants; uniform weights are the only weights unchanged by every relabelling of the six time positions | passes |
| B | pass | pass: 720 operators per cube, a fixed list | pass as a question | conditional: it asks 720 conditions where ZM1-G may list one operator. Its reason is Definition SC's clause "both orders mapped to the same commuting product" (Y2W line 56), carried from products of two observables to products of six | passes if that reason is accepted |

The four tests do not choose between S and B. This draft decides Y2-W-L under each and adopts neither.

## 2. Exact structure of a cube product

### 2.1 One link carrying two factors

**Lemma C.** For a link `ℓ = (x, y)` and all colour indices,

\[
(U^{j'k'})^\dagger U^{jk} = E^{y}_{j'j}\,\big(\delta_{kk'} - E^{x}_{kk'}\big),\qquad
U^{jk}\,(U^{j'k'})^\dagger = E^{x}_{kk'}\,\big(\delta_{jj'} - E^{y}_{j'j}\big). \tag{2.1}
\]

*Proof.* `(U^{j'k'})^† = r^x_{k'} r^{y†}_{j'}`. In `r^x_{k'} r^{y†}_{j'} r^y_j r^{x†}_k` the middle pair `r^{y†}_{j'} r^y_j` is even and contains no `x`-mode, so it commutes with `r^x_{k'}`. This gives `E^y_{j'j} r^x_{k'} r^{x†}_k = E^y_{j'j}(δ_{kk'} − r^{x†}_k r^x_{k'})`. For the second identity, move the even pair `r^{x†}_k r^x_{k'}` in `r^y_j r^{x†}_k r^x_{k'} r^{y†}_{j'}` to the front, and use `r^y_j r^{y†}_{j'} = δ_{jj'} − r^{y†}_{j'} r^y_j`. ∎

*Reading.* A step along `ℓ` with `𝐔_ℓ` removes a rishon at `y` and adds one at `x`. A step against `ℓ` with `𝐔_ℓ^†` removes one at `x` and adds one at `y`. In both cases the step removes a rishon at its head and adds one at its tail. In `Θ^σ_c` each fine link `ℓ` of the skeleton meets two factors, one from each of its two faces. **Definition.** For an order `σ`, the **particle end** of `ℓ` is the head of the step of the face that acts first (the earlier face). The other end is the **hole end**. By (2.1), the two factors on `ℓ` compose to

\[
E^{p}_{\alpha_{\rm later}\,\alpha_{\rm earlier}}\;\big(\mathbb 1 - E^{h}\big)_{\beta_{\rm earlier}\,\beta_{\rm later}}, \tag{2.2}
\]

where `p` is the particle end, `h` the hole end, `α` are the two faces' matrix indices at `p` and `β` their indices at `h`.

### 2.2 Corner factorisation

At a skeleton point `v`, each face through `v` has one summed matrix index `α_f(v)`, shared by its two steps at `v`. For a link end `e` at `v`, let `prev(e)` be the face whose step along `e` ends at `v`, and `next(e)` the face whose step along `e` starts at `v`. The end `e` is a particle end exactly when `prev(e)` acts before `next(e)`.

**Lemma K (corner factorisation).** Let `c` be a block cube at scale `r` and `σ` an order. Put `X^e := E^e` if `e` is a particle end and `X^e := 1 − E^e` if `e` is a hole end. Then

\[
\Theta^\sigma_c=\prod_{v}O_v,\qquad O_v:=\sum_{(\alpha_f)_{f\ni v}}\ \prod_{e\ \text{at}\ v}X^{e}_{\alpha_{{\rm next}(e)}\,\alpha_{{\rm prev}(e)}}, \tag{2.3}
\]

the product over all skeleton points `v` of `c`. The factors `O_v` act on disjoint sets of link ends and commute.

*Proof.* Expand each of the six traces into a sum over its matrix indices. Each term of `Θ^σ_c` is then an ordered product of entries, two on each skeleton link. Entries on different links commute (they are even operators in different tensor factors). Collect the two entries on each link and apply (2.2). At a particle end the indices are (later, earlier) = (`next(e)`, `prev(e)`). At a hole end they are (earlier, later), which is again (`next(e)`, `prev(e)`). Each index `α_f(v)` occurs only in end operators at `v`. So the sum over all indices splits into a product over points. End operators at different points commute. ∎

At a block corner three faces and three ends meet. Each face enters `v` along one end and leaves along another, and each end is entered by one face and left by the other. So `prev` and `next` arrange the three ends in a cycle. Label them `e_1, e_2, e_3` with `next(e_i) = prev(e_{i+1})` (indices mod 3). Then (2.3) reads

\[
O_v=\operatorname{tr}\big(X^{e_3}X^{e_2}X^{e_1}\big), \tag{2.4}
\]

a trace of a product of `5 × 5` matrices whose entries commute. At an inner point of a block edge two faces and two ends meet, and `O_v = tr(X^{e_2}X^{e_1})`.

**Lemma T (corner types).** At each block corner, one or two of the three ends are particle ends. Exactly four corners have one and four have two. At each inner point exactly one end is a particle end.

*Proof.* At a block corner with faces `f_i := prev(e_i)`, the end `e_i` is a particle end exactly when `f_i` acts before `f_{i+1}`. Among the three statements "`f_1` before `f_2`", "`f_2` before `f_3`", "`f_3` before `f_1`", not all hold and not all fail. Each skeleton link has exactly one particle end. Along a block edge the earlier face steps the same way on all `n` fine links. So every inner point is the particle end of exactly one of its two links, and exactly one of the two block corners receives a particle end from that block edge. Hence the eight corners receive twelve particle ends: `t_1 + 2t_2 = 12` with `t_1 + t_2 = 8`, so `t_2 = 4`. ∎

[check] (5) `tetra.py`: on a closed surface of four triangles (abstract links, the same three-face corners), Lemma K holds exactly for all 24 orders, with `N = 2` colours at `m = 1, 2, 3` and `N = 3` at `m = 1` (largest entry of the difference: 0; the products are nonzero).

### 2.3 Spectator colours

**Lemma S (spectators).** Let `a_1, …, a_q` be distinct link ends and `T := tr(E^{a_q} ⋯ E^{a_1})`, `q ≥ 1`. Fix a colour `μ` and let `T^{(μ̂)}` be the same sum with every index restricted to colours `≠ μ`.
(i) On the subspace where `μ` is occupied at every `a_i`, `T = T^{(μ̂)} + 1`.
(ii) On the subspace where `μ` is empty at every `a_i`, `T = T^{(μ̂)}`.
(iii) Let `O_v` be a corner operator (2.3) at a block corner or an inner point. On either subspace, taken at all ends of `v`, `O_v` equals the operator `O_v^{(μ̂)}` built by the same rule from the colours `≠ μ`.

*Proof.* A term of `T` is `Π_j E^{a_j}_{ν_{j+1}ν_j}` with indices read cyclically. No two factors act on the same end. (i) If `ν_{j+1} = μ ≠ ν_j`, the factor `r^{a_j†}_μ r^{a_j}_{ν_j}` must create `μ` at `a_j`, where `μ` is present; the term vanishes. So in a nonzero term `ν_{j+1} = μ` forces `ν_j = μ`; going round the cycle, either all indices equal `μ` or none does. The all-`μ` term is `Π_j n^{a_j}_μ = 1` on the subspace. Terms with no index `μ` form `T^{(μ̂)}`, which preserves the subspace. (ii) Every index occurs as the right index of some factor. If it is `μ`, that factor removes `μ` at an end where it is absent, and the term vanishes. (iii) By (2.3), `O_v = Σ_{H' ⊆ H} (−1)^{|H'|} T_{P ∪ H'}`, where `P` and `H` are the particle and hole ends at `v` and `T_{P∪H'}` is the trace (2.4) with `E` at the ends of `P ∪ H'` and `1` elsewhere. Every term has at least one `E`, since `P ≠ ∅` (Lemma T). Under (i) the constants add up to `Σ_{H'⊆H}(−1)^{|H'|} = 0`, since `H ≠ ∅` (Lemma T). Under (ii) there are none. The remaining parts reassemble into `O_v^{(μ̂)}`. ∎

### 2.4 Particle-hole conjugation

**Lemma P.** On each link let `C_ℓ := γ_1 ⋯ γ_{10}`, with `γ_μ := r_μ + r_μ^†` over the ten rishon modes of `ℓ`. Put `C := ⊗_ℓ C_ℓ`. Then `C` is unitary, `C r_μ C^† = −r_μ^†` for every rishon mode, `C` maps the sector `m` of every link to the sector `10 − m`, and for every loop trace and every order

\[
C\,W_C\,C^\dagger = W_C^\dagger,\qquad C\,\Theta^\sigma_c\,C^\dagger = \big(\Theta^{\sigma^{\rm rev}}_c\big)^\dagger . \tag{2.5}
\]

*Proof.* Each `γ_μ` is Hermitian with `γ_μ^2 = 1`, so `C_ℓ` is unitary. `γ_μ r_μ γ_μ = r_μ^† r_μ r_μ^† = r_μ^†`, and `γ_μ r_ν γ_μ = −r_ν` for `ν ≠ μ` (anticommutation). Conjugating by the ten factors gives `C r_ν C^† = (−1)^9 r_ν^†`. Then `C n_μ C^† = r_μ r_μ^† = 1 − n_μ`, so the rishon number `N ↦ 10 − N`. Next, `C U^{jk} C^† = (−r^{y†}_j)(−r^x_k) = −(U^{jk})^†`, and `C (U^{jk})^† C^† = −U^{jk}`. So each step matrix `𝐌` of a loop goes to `−(𝐌^†)^T`, with `T` the transpose of matrix indices. For a loop of `q` steps the signs give `(−1)^q`, and `q` is even on the cubic lattice. Entries of different steps' matrices commute, so `tr(A^T B^T ⋯) = tr(⋯ B A)`. Hence `W_C ↦ tr(𝐌_1^† 𝐌_2^† ⋯ 𝐌_q^†) = W_C^†`. Finally `C W_{σ(6)} ⋯ W_{σ(1)} C^† = W_{σ(6)}^† ⋯ W_{σ(1)}^† = (W_{σ(1)} ⋯ W_{σ(6)})^†`. ∎

`D_ω(Y) = D_ω(Y^†)`. So `C` carries every statement about `D` for the classes S and B in the sector `m` to the same statement in the sector `10 − m`.

### 2.5 One rishon per end

**Lemma R.** Consider a block corner whose three ends hold exactly one rishon each. On their colours, `E^{e}_{ab}` acts as `|a⟩⟨b|`. So `tr E^{e_i} = 1`, `tr(E^{e_i}E^{e_j}) = S_{ij}` (the exchange of the colours of `e_i` and `e_j`), and `Z := tr(E^{e_3}E^{e_2}E^{e_1})` is a cyclic permutation of the three colours. The six corner operators (2.4) are

\[
\text{one particle end } e_i:\ \ 1-S_{ij}-S_{ik}+Z;\qquad \text{two particle ends } e_i,e_j \text{ (hole } e_k):\ \ S_{ij}-Z,
\]

with `{i, j, k} = {1, 2, 3}`. Let `e_+`, `e_−` be the projections onto the colour states symmetric, respectively antisymmetric, under all permutations of the three ends, and `e_0 := 1 − e_+ − e_−`.
(i) On `ran e_+` all six operators vanish.
(ii) On `ran e_−` the three one-particle operators equal `4` and the three two-particle operators equal `−2`. Their adjoints take the same values.
(iii) On `ran e_0`, `1 + Z + Z^2 = 0`, `S_{12} + S_{13} + S_{23} = 0`, and each `A := S_{ij} − Z` satisfies `A^2 = A`.
(iv) At an inner point with one rishon on each of its two ends, both corner operators equal `1 − S_{12}`: `0` on symmetric and `2` on antisymmetric colour states.

*Proof.* On a one-rishon end `r^†_a r_b r^†_c|0⟩ = δ_{bc} r^†_a|0⟩`, which gives `|a⟩⟨b|`. The trace formulas follow by summing indices: `tr(E^{e_i}E^{e_j})` sends `|α⟩_i|β⟩_j` to `|β⟩_i|α⟩_j`, and `Z` sends `|α⟩_1|β⟩_2|γ⟩_3` to `|β⟩_1|γ⟩_2|α⟩_3`. Expanding (2.4) with `X = E` or `1 − E` gives the six operators. Write `P_π` for the permutation operators of `S_3` on the three colours; they are unitary. `e_± = (1/6) Σ_π (±1)^{π} P_π` are self-adjoint idempotents with `e_+e_− = 0`, commuting with every `P_π`, and `P_π e_± = (±1)^π e_±`. (i) `S = Z = 1`, so `1 − 1 − 1 + 1 = 0` and `1 − 1 = 0`. (ii) `S = −1` and `Z = +1` (a 3-cycle is even), so `1 + 1 + 1 + 1 = 4` and `−1 − 1 = −2`. Adjoints replace `Z` by `Z^{−1}`, also `+1` there. (iii) `1 + Z + Z^2 = Σ_{π even} P_π = 3(e_+ + e_−)` and `S_{12} + S_{13} + S_{23} = Σ_{π odd} P_π = 3(e_+ − e_−)`; both vanish on `ran e_0`. For `A = S − Z`: `A^2 = 1 − (SZ + ZS) + Z^2`. In `S_3`, `SZ` and `ZS` are the two transpositions other than `S` (they are odd, differ from `S` since `Z ≠ 1`, and differ from each other since `SZS = Z^{-1} ≠ Z`). So on `ran e_0`, `SZ + ZS = −S` and `Z^2 = −1 − Z`, and `A^2 = 1 + S − 1 − Z = A`. (iv) `tr((1 − E^{e_2})E^{e_1}) = 1 − S_{12}` and `tr(E^{e_2}(1 − E^{e_1})) = 1 − S_{12}`. ∎

[check] (1) `corner.py`: on `Λ^1 ⊗ Λ^1 ⊗ Λ^1` the `U(5)` highest-weight space of weight `(1,1,1,0,0)` (the antisymmetric states) gives `4, 4, 4, −2, −2, −2`; weight `(3,0,0,0,0)` gives zeros; weight `(2,1,0,0,0)` (multiplicity 2) gives eigenvalues `{0, 1}` for each operator and no common eigenvector with all six nonzero. On `Λ^2 ⊗ Λ^2 ⊗ Λ^2` the weights `(3,1,1,1,0)` and `(2,2,2,0,0)` give `(4, −2)` and `(−2, 4)`.

## 3. One cube at the lattice scale (Y2-W-L0), every `m`, every state

**Theorem L0.** Fix `m ∈ {1, …, 9}` and one unit cube `c`. Put `m̄ := min(m, 10 − m)`.
(i) (reading F) For every order `σ` there is a vector `Ψ_σ` in the sector `m` with `Θ^σ_c Ψ_σ = m̄^8 Ψ_σ` and `(Θ^σ_c)^† Ψ_σ = m̄^8 Ψ_σ`. Hence `D_{Ψ_σ}(m̄^{−8} Θ^σ_c) = 0`.
(ii) (reading S) The same `Ψ_σ` satisfies `Θ^S_c Ψ_σ = λ Ψ_σ` and `(Θ^S_c)^† Ψ_σ = λ Ψ_σ` with `λ = (n_σ/720) m̄^8 > 0`, where `n_σ ≥ 1` is the number of orders with the same particle ends as `σ`. Hence `D_{Ψ_σ}(λ^{−1} Θ^S_c) = 0`.
(iii) (reading B) If `2 ≤ m ≤ 8`, there is a vector `Φ` in the sector `m` with `Θ^σ_c Φ = 4096 Φ` and `(Θ^σ_c)^† Φ = 4096 Φ` for all 720 orders at once. If `m ∈ {1, 9}`, then for every state `ω`, every order `σ` and all `c, c' ∈ C`,

\[
D_\omega(c\,\Theta^\sigma_c)+D_\omega(c'\,\Theta^{\sigma^{\rm rev}}_c)\ \ge\ 2 . \tag{3.1}
\]

**What this decides.** Y2-W-L0 asks whether `inf_ω inf_c D_ω(cΘ_c) > η_*`. Under F and under S the answer is no, for every `m`: the infimum is `0` and it is attained. Under B the quantity is `inf_ω inf_c max_σ D_ω(cΘ^σ_c)`. It is `0`, attained, for `m ∈ {2, …, 8}`. It is at least `1` for `m ∈ {1, 9}`, so there Y2-W-L0 holds whenever `η_* < 1`.

*Proof of (i).* First let `m ≤ 5`. Let `Ψ_σ` put, on each of the twelve edges, all `m` rishons at the `σ`-particle end, in colours `1, …, m`, and leave the hole end empty. Use Lemma K. At a hole end `E = 0`, so `X = 1 − E` acts as the identity matrix. A corner with one particle end `p` gives `O_v = tr E^p = N^p = m`. A corner with two particle ends `p, p'` gives `O_v = tr(E^{p'}E^p)`. Apply Lemma S(i) to each colour `μ ≤ m`, present at `p` and `p'`, and Lemma S(ii) to each `μ > m`, absent at both. What remains is a sum over no colours, which is zero; so `tr(E^{p'}E^p) = m` on this vector. By Lemma T there are eight corners, so `Θ^σ_c Ψ_σ = m^8 Ψ_σ`. Next, `(Θ^σ_c)^† = Π_v O_v^†`, and `O_v^†` is (2.3) with `prev` and `next` exchanged. On `Ψ_σ` it is the same trace of one or two matrices, with the same value. For `m ≥ 6`, let `Ψ'` be the vector just built for the sector `10 − m` and the order `σ^{rev}`, and put `Ψ_σ := CΨ'`. By (2.5), `Θ^σ_c CΨ' = C (Θ^{σ^{rev}}_c)^† Ψ' = (10 − m)^8 CΨ'`, and likewise for the adjoint. ∎

*Proof of (ii).* Let `m ≤ 5` and let `τ` be an order whose particle ends differ from those of `σ` on some edge. On that edge the `τ`-particle end is the `σ`-hole end, which is empty in `Ψ_σ`. Every term of the `τ`-corner operator there contains a factor `E` of that empty end, so `Θ^τ_c Ψ_σ = 0`. The same holds for `(Θ^τ_c)^†`. Orders with the same particle ends as `σ` act as in (i). Averaging over the 720 orders gives `λ`. For `m ≥ 6` use (2.5): `τ ↦ τ^{rev}` is a bijection of the orders, and `τ` has the particle ends of `σ` exactly when `τ^{rev}` has those of `σ^{rev}`. ∎

*Proof of (iii), first part.* Give each corner `v` of `c` a number `s_v ∈ {0, 1, 2}` with `s_v + s_w = m − 2` on every edge `vw`. For `m = 2, 4, 6` take `s_v = m/2 − 1` everywhere. For `m = 3` take `0` at the corners with even coordinate sum and `1` at the others; for `m = 5` take `1` and `2`. (Each edge joins corners of opposite parity.) At each corner choose disjoint colour sets `S_v`, with `|S_v| = s_v`, and `A_v = {α_1, α_2, α_3}`; this needs `s_v + 3 ≤ 5`. At an end put `|S; α⟩ := r^†_α Π_{μ ∈ S} r^†_μ |0⟩` (product in a fixed order). Define

\[
\chi_v:=\sum_{\pi\in S_3}\operatorname{sgn}(\pi)\ \bigotimes_{i=1}^{3}\big|S_v;\alpha_{\pi(i)}\big\rangle_{e_i},\qquad \Phi:=\bigotimes_v\chi_v . \tag{3.2}
\]

Each end at `v` holds `s_v + 1` rishons, so each edge `vw` holds `s_v + s_w + 2 = m`. Each colour of `S_v` is present at all three ends of `v`. Each colour outside `S_v ∪ A_v` is absent at all three. By Lemma S(iii), applied colour by colour, `O_v` acts on `χ_v` as the corner operator built from the three active colours. For active colours `a, b`, `E_{ab} |S; α⟩ = δ_{bα} |S; a⟩`, because `r_b r^†_α |S⟩ = δ_{bα} |S⟩` when `b ∉ S`. So the reduced problem is the one-rishon problem of Lemma R, and `χ_v` is antisymmetric in it. By Lemma R(ii), `O_v χ_v = 4χ_v` at a corner with one particle end and `−2χ_v` at a corner with two. By Lemma T, `Θ^σ_c Φ = 4^4 (−2)^4 Φ = 4096 Φ` for every `σ`, and Lemma R(ii) gives the same for the adjoints. For `m ∈ {7, 8}` put `Φ := CΦ'` with `Φ'` built for `10 − m ∈ {3, 2}`; (2.5) gives `Θ^σ_c Φ = C(Θ^{σ^{rev}}_c)^† Φ' = 4096 Φ`. ∎

*Proof of (iii), second part.* Let `m = 1`, so each edge holds one rishon. Let `P_σ` project onto the configurations in which every edge's rishon sits at its `σ`-particle end. If some edge's rishon sits at its `σ`-hole end, its `σ`-particle end is empty and `Θ^σ_c` vanishes there, as in (ii). `Θ^σ_c` preserves every `N^{ℓ,x}` (Lemma B0), so `Θ^σ_c = P_σ Θ^σ_c P_σ`. For every vector `ψ`, `(cΘ^σ_c − 1)ψ = (cΘ^σ_c − 1)P_σψ − (1 − P_σ)ψ`, and the two terms are orthogonal. So `‖(cΘ^σ_c − 1)ψ‖^2 ≥ ⟨ψ, (1 − P_σ)ψ⟩`, and the same holds for the adjoint. As operator inequalities, `(cΘ − 1)^†(cΘ − 1) ≥ 1 − P_σ` and `(cΘ − 1)(cΘ − 1)^† ≥ 1 − P_σ`. Hence `D_ω(cΘ^σ_c) ≥ 2(1 − ω(P_σ))` for every state. Reversing the order makes every earlier face the later one, so every `σ`-particle end is a `σ^{rev}`-hole end. Thus `P_σ P_{σ^{rev}} = 0` and `ω(P_σ) + ω(P_{σ^{rev}}) ≤ 1`. Adding the two bounds gives (3.1). For `m = 9`, conjugate by `C`: by (2.5), with `C^†` acting the same way, the pair `(σ, σ^{rev})` goes to `(σ^{rev}, σ)`, and `D_ω(Y) = D_ω(Y^†)`. ∎

**Which corner states serve all orders.** [check] (2) `ratios.py`, `ratios2.py`: on the corner sectors `1 ≤ n_1 ≤ n_2 ≤ n_3 ≤ 4`, restricted to multiplicity-one `U(5)` highest-weight spaces, 14 joint eigenvectors of the six corner operators have all six eigenvalues nonzero. Each is a spectator state of the kind in (3.2) with `N` active rishons antisymmetrised (for example `Λ^4` on ends holding `1, 1, 2`), or its particle-hole image. For each, the six eigenvalues have the product form `λ(P) = Π_{ends} g(end ∈ P)`, checked through `λ({1})λ({2,3}) = λ({2})λ({1,3}) = λ({3})λ({1,2})`. On `Λ^N` states the per-end ratio `g(particle)/g(hole)` is `−a/(1 + a)` for an end with `a` active rishons; on particle-hole images it is the inverse. The search used a random linear combination of the six operators on each weight space; it is a guide, not a classification.

## 4. The general scale

### 4.1 One block cube

**Theorem L0-r.** Theorem L0 holds for one block cube at every scale `r = L^k a` with boundary-loop faces. In (i) and (ii) replace `m̄^8` by `m̄^{8 + 12(n−1)}`; in (iii) replace `4096` by `4096 · 2^{12(n−1)}`; (3.1) holds unchanged.

*Proof.* Lemmas K, T, S and P hold on the skeleton. (i) and (ii): for `m ≤ 5` put all `m` rishons of every skeleton link at its `σ`-particle end, in colours `1, …, m`. An inner point has one particle end `p` and one hole end `h` (Lemma T). Its operator is `tr((1 − E^h)E^p)` or `tr(E^p(1 − E^h))`, depending on the labels, and both equal `N^p − tr(E^h E^p) = m − 0 = m`. Block corners give `m` as before, and orders with other particle ends give `0` as before. For `m ≥ 6` use (2.5). (iii), first part: choose `s_v` at every skeleton point with `s_v + s_w = m − 2` along every skeleton link, `s_v ≤ 2` at block corners and `s_v ≤ 3` at inner points. For `m = 2, 4, 6` take `s_v = m/2 − 1` everywhere. For `m = 3` and `m = 5` let `s_v` alternate between `0` and `1`, or `1` and `2`, by the parity of the coordinate sum (the skeleton is a subgraph of `Z^3`). Block corners carry `χ_v` of (3.2). An inner point with spectator set `S_v` and active colours `β_1, β_2` carries `Σ_{π ∈ S_2} sgn(π) |S_v; β_{π(1)}⟩ ⊗ |S_v; β_{π(2)}⟩`. By Lemma S and Lemma R(iv) its operator equals `2` whichever end is the particle end. For `m ∈ {7, 8}` use (2.5). (iii), second part: the support argument of Theorem L0 applies to every skeleton link. ∎

### 4.2 All block cubes at once

SC-loop asks one `c` to serve every `W ∈ 𝒲_r`, so Y2-W-L concerns all block cubes at scale `r` together. Block cubes share block edges, and the states of Theorem L0-r disagree on shared edges. Two facts guide the search. [check] (3) `lattice_aligned.py`: no translation-invariant state with colours `1, …, n` on an end of `n` rishons gives a nonzero product for any order, for any `m`. [check] (4) `orient.py`: no translation-invariant choice of occupied ends makes every cube compatible with some order; with period 2 many choices do. The parity rule below is one of the 138 rules of the form `ε_i (−1)^{a_i · x}` that the check accepts (`orient_rules.py`, `rule_check.py`).

**Face steps on a block edge.** The boundary of a face runs counterclockwise as seen from outside the cube: at a point of an edge it steps along `ν × n̂`, where `n̂` is the outward normal and `ν` points from the edge into the face. For a block cube with lowest corner at the origin (block units), faces named by outward normal, this gives:

| block edge (lower endpoint) | face stepping along `+e_i` | face stepping along `−e_i` |
|---|---|---|
| `e_1`, `(0,0,0)` | `−e_2` | `−e_3` |
| `e_1`, `(0,1,0)` | `−e_3` | `+e_2` |
| `e_1`, `(0,0,1)` | `+e_3` | `−e_2` |
| `e_1`, `(0,1,1)` | `+e_2` | `+e_3` |
| `e_2`, `(0,0,0)` | `−e_3` | `−e_1` |
| `e_2`, `(0,0,1)` | `−e_1` | `+e_3` |
| `e_2`, `(1,0,0)` | `+e_1` | `−e_3` |
| `e_2`, `(1,0,1)` | `+e_3` | `+e_1` |
| `e_3`, `(0,0,0)` | `−e_1` | `−e_2` |
| `e_3`, `(1,0,0)` | `−e_2` | `+e_1` |
| `e_3`, `(0,1,0)` | `+e_2` | `−e_1` |
| `e_3`, `(1,1,0)` | `+e_1` | `+e_2` |

Each entry is one cross product. For example, the `e_1`-edge at `(0,0,0)` lies in the face `−e_3` with `ν = e_2`, and `e_2 × (−e_3) = −e_1`.

**Theorem S∞ (reading S; all block cubes; every scale; every `m`).** Fix `m` and `k ≥ 0`; `r = L^k a`, `n = L^k`. Call a block site even or odd by the parity of the sum of its block coordinates. Let `m ≤ 5` first. Let `Ψ_k` be the vector state that, on every fine link of a block edge parallel to `e_1`, puts all `m` rishons, in colours `1, …, m`, at the end of that fine link nearer the even endpoint of the block edge; on block edges parallel to `e_2` or `e_3`, at the end nearer the odd endpoint. Other links carry any fixed vector. Then for every block cube `c` at scale `r`,

\[
\Theta^S_c\Psi_k=\lambda\,\Psi_k,\qquad (\Theta^S_c)^\dagger\Psi_k=\lambda\,\Psi_k,\qquad \lambda=\tfrac{8}{720}\,m^{\,8+12(n-1)} . \tag{4.1}
\]

For `m ≥ 6`, `CΨ'_k`, with `Ψ'_k` built for `10 − m`, satisfies (4.1) with `λ = (8/720)(10 − m)^{8 + 12(n−1)}`. So SC-loop(`r`; 0) holds for `𝒲^S_r`, with `c = 1/λ`, in this state. It also holds in the state averaged over the gauge transformations of the sites involved, because each `Θ^S_c` commutes with them.

*Proof.* (a) Fix a block cube `c` and an order `σ`. Call `σ` compatible if, on every block edge of `c`, the `σ`-particle ends of its fine links are the occupied ends. The proof of Theorem L0-r gives `Θ^σ_c Ψ_k = m^{8 + 12(n−1)} Ψ_k` for compatible `σ`, and `Θ^σ_c Ψ_k = 0` otherwise; the same holds for the adjoints. (b) The particle end of a fine link is the head of the earlier face's step. So `σ` is compatible exactly when, on each block edge, the face stepping toward the occupied endpoint acts first. Let the lowest corner of `c` be even. An `e_1`-edge with lower endpoint `(0, t_2, t_3)` has its occupied (even) endpoint below when `t_2 + t_3` is even and above when it is odd. Reading the table: `−e_3` before `−e_2`; `−e_3` before `+e_2`; `+e_3` before `−e_2`; `+e_3` before `+e_2`. So both `e_3`-faces precede both `e_2`-faces. The `e_2`-edges, occupied at the odd endpoint, give the same way: both `e_3`-faces precede both `e_1`-faces. The `e_3`-edges give: both `e_1`-faces precede both `e_2`-faces. The compatible orders are therefore exactly those listing the two `e_3`-faces, then the two `e_1`-faces, then the two `e_2`-faces: `2 · 2 · 2 = 8` orders. If the lowest corner of `c` is odd, every parity flips and every relation reverses; again 8 orders. (c) Averaging over 720 orders gives (4.1) for every block cube. For `m ≥ 6` use (2.5). The gauge average: for a unitary `g` commuting with `Θ`, `D_{ω(g^†·g)}(cΘ) = D_ω(cΘ)`, and `D` is affine in the state. ∎

**Theorem B1 (reading B; `m ∈ {1, 9}`; all block cubes; every scale).** For every block cube `c`, every state `ω`, every order `σ` and all `c, c'`, (3.1) holds. So SC-loop(`r`; `η`) fails for `𝒲^B_r` in every state when `η < 1`.

*Proof.* Theorem L0-r, (iii), second part. ∎

**Theorem B2 (reading B; `m ∈ {2, 8}`; all block cubes; every scale).** Let `x` be a block site at scale `r`. There is a family `F_x` of 28 pairs (block cube with corner `x`, order) such that for every state `ω` and every `c ∈ C`,

\[
\sum_{(c',\sigma)\in F_x} D_\omega\big(c\,\Theta^\sigma_{c'}\big)\ \ge\ \frac{1}{16200} . \tag{4.2}
\]

So SC-loop(`r`; `η`) fails for `𝒲^B_r` in every state when `η < 1/453600`.

*Proof.* By (2.5) it suffices to take `m = 2`. Let `ℓ_1, …, ℓ_6` be the fine links at `x` along the six block edges at `x`. The eight block cubes with corner `x` correspond to the eight octants at `x`. It suffices to prove the operator inequality `Σ_{F_x} (cΘ − 1)^†(cΘ − 1) ≥ 1/16200`; (4.2) follows by taking expectations, since `D_ω(Y) ≥ ω(Y^†Y)` for `Y = cΘ − 1`.

*Step 0 (sectors).* Every `Θ^σ_{c'}` preserves every end number: by (2.2), each link carries `E` at one end and `1 − E` at the other. Split a vector as `ψ = Σ_s ψ_s` by the end numbers of `ℓ_1, …, ℓ_6`. Then `‖(cΘ − 1)ψ‖^2 = Σ_s ‖(cΘ − 1)ψ_s‖^2`. So it suffices to bound each `ψ_s`.

*Step 1 (an empty end).* Suppose in the sector `s` some `ℓ_j` holds no rishon at `x`. Choose a block cube containing `ℓ_j` with corner `x`, and an order making the end of `ℓ_j` at `x` a particle end. Every term of the corner operator at `x` contains `E` of an empty end, so `Θ ψ_s = 0` and `‖(cΘ − 1)ψ_s‖^2 = ‖ψ_s‖^2`. If `ℓ_j` holds two rishons at `x`, its far end is empty; an order making the far end a particle end gives the same. These are 12 pairs of `F_x`.

*Step 2 (one octant).* Now let each `ℓ_j` hold one rishon at `x`. Fix an octant `O` with block cube `c_O` and ends `e_1, e_2, e_3` at `x` labelled as in (2.4). Choose two orders `σ_1, σ_2` of `c_O` whose local orders at `x` make two different pairs of ends the particle ends (every local order at `x` extends to an order). These are 16 pairs of `F_x`. Let `e^O_+, e^O_−, e^O_0` be the projections of Lemma R for the colours of `e_1, e_2, e_3`. By Lemma K and Lemma R, `Θ^{σ_i}_{c_O} = A_i R_i`, where `A_i` is a polynomial in the permutations of these three colours and `R_i` acts on other ends. So `Θ^{σ_i}_{c_O}` commutes with `e^O_±` and `e^O_0`. Write `ψ = ψ_+ + ψ_− + ψ_0` (orthogonal) and `S_O := Σ_{i=1,2} ‖(cΘ^{σ_i}_{c_O} − 1)ψ‖^2`. On `ran e^O_+`, `A_i = 0` (Lemma R(i)), so `‖(cΘ^{σ_i}_{c_O} − 1)ψ‖^2 ≥ ‖ψ_+‖^2`. On `ran e^O_0`, `A_i = S^{(i)} − Z` with two different exchanges `S^{(1)}, S^{(2)}` and one 3-cycle `Z`, and `A_i^2 = A_i` (Lemma R(iii)). Since `A_i` commutes with `R_i`, `(1 − A_i)Θ^{σ_i}_{c_O} = 0` there, so `(1 − A_i)(cΘ^{σ_i}_{c_O} − 1)ψ_0 = −(1 − A_i)ψ_0` and `‖(1 − A_i)ψ_0‖ ≤ 3‖(cΘ^{σ_i}_{c_O} − 1)ψ_0‖`. Put `Y := S^{(2)} S^{(1)}`, a 3-cycle. Then `(Y − 1)ψ_0 = S^{(2)}((1 − A_2) − (1 − A_1))ψ_0`. On `ran e^O_0`, `1 + Y + Y^2 = 0` (Lemma R(iii) holds for both 3-cycles). With `d := (Y − 1)ψ_0`, this gives `0 = 3ψ_0 + 2d + Yd`, so `‖ψ_0‖ ≤ ‖d‖ ≤ 3(‖(cΘ^{σ_1}_{c_O} − 1)ψ_0‖ + ‖(cΘ^{σ_2}_{c_O} − 1)ψ_0‖)`, and `‖ψ_0‖^2 ≤ 18 Σ_i ‖(cΘ^{σ_i}_{c_O} − 1)ψ_0‖^2`. Together, `‖(1 − e^O_−)ψ‖^2 = ‖ψ_+‖^2 + ‖ψ_0‖^2 ≤ 18 S_O`.

*Step 3 (the six ends at `x`).* Let `τ_{ab}` exchange the colours of two ends `a, b` at `x` on different axes. Some octant `O` contains both, and `τ_{ab} = −1` on `ran e^O_−`. So `‖(1 + τ_{ab})ψ‖ = ‖(1 + τ_{ab})(1 − e^O_−)ψ‖ ≤ 2(18 S_O)^{1/2}`. Let `ε` be the largest of these twelve norms. The twelve exchanges generate all permutations of the six colours: an exchange on one axis is `τ_{ac}τ_{bc}τ_{ac}` with `c` on another axis, and every permutation of six objects is a product of at most five exchanges. So every permutation `π` is a product of at most 15 of the `τ_{ab}`, and telescoping gives `‖πψ − sgn(π)ψ‖ ≤ 15ε`. The total antisymmetriser `(1/720)Σ_π sgn(π)π` over six one-rishon ends in five colours is zero, since `Λ^6(C^5) = 0`. Hence `ψ = (1/720) Σ_π (ψ − sgn(π)πψ)` and `‖ψ‖ ≤ 15ε`. So `max_O S_O ≥ ‖ψ‖^2/(225 · 4 · 18) = ‖ψ‖^2/16200`.

*Step 4.* Steps 1 and 3 give `Σ_{F_x} ‖(cΘ − 1)ψ_s‖^2 ≥ ‖ψ_s‖^2/16200` in every sector. Step 0 sums the sectors. If SC-loop(`r`; `η`) held, each of the 28 terms of (4.2) would be at most `η`. ∎

[check] (6) `b2site.py`: the 16 terms of Step 2 with every `R_i` replaced by `1`, on the six one-rishon ends at a site (dimension `5^6`). Over ten values of `c` (real and complex), the lowest eigenvalue of `Σ (cA − 1)^†(cA − 1)` lies between `7.68` (at `c = −0.4`) and `16`. The constant `1/16200` is not optimised.

**Remark F (reading F on all cubes).** Let `σ_0` give every unit cube the same order of the six face types. At `m = 1`, an `e_1`-link is the `e_1`-edge with lower endpoint `(0,0,0)`, `(0,1,0)`, `(0,0,1)`, `(0,1,1)` of four cubes. By the table, these cubes put its particle end at its `+e_1` end exactly when, respectively, `−e_2` precedes `−e_3`, `−e_3` precedes `+e_2`, `+e_3` precedes `−e_2`, `+e_2` precedes `+e_3` in `σ_0`. The four cannot all hold (they would close the cycle `−e_2, −e_3, +e_2, +e_3`) and cannot all fail. So two of these cubes have orthogonal supports, and the argument of (3.1) gives `D + D ≥ 2` for them in every state. So reading F with a covariant order fails on all cubes for `m ∈ {1, 9}`, with floor 1.

### 4.3 Reading B on all cubes for `m ∈ {3, …, 7}`: open

**Y2-W-LB(m), `m ∈ {3, …, 7}`.** Under reading B, with boundary-loop block faces at a scale `r`: is there `δ_m > 0` such that, in every state, the sum of `D_ω(cΘ^σ_{c'})` over the block cubes `c'` with a common corner and their orders is at least `δ_m`? Theorem L0-r gives `D = 0` for each single block cube, so a floor, if it exists, comes from several cubes together, as in Theorem B2. Three attacks failed.

- *Attack 1, toward "no floor": extend the states (3.2) to all cubes at a corner.* Named failing step: "the eight octants at `x` keep antisymmetric active parts". In the family (3.2), an end holds its spectator colours with certainty and one of three active colours with probability `1/3` each. An end lies in four octants, so all eight octants at `x` share one spectator set and one active set of three colours. Their active rishons are then antisymmetric under every exchange of two ends on different axes, hence totally antisymmetric over six ends in three colours, which is zero. This is the mechanism of Theorem B2. It excludes the family, not every state.
- *Attack 2, toward a floor: the support argument of (3.1).* Named failing step: "in every sector some end is empty or full". For `m ∈ {3, …, 7}` the sectors in which every end holds between 1 and 4 rishons exist, and Theorem L0(iii) shows that the corner operators have nonzero joint eigenvalues there.
- *Attack 3, toward a floor: the `S_3` argument of Theorem B2.* Named failing step: "the corner operators are polynomials in the permutations of three one-rishon ends". With two or more rishons on an end they lie in the larger algebra of `U(5)`-invariant operators on `Λ^{n_1} ⊗ Λ^{n_2} ⊗ Λ^{n_3}`. Step 2 of Theorem B2 would need every joint eigenspace of the six corner operators with all eigenvalues nonzero. [check] (2) finds only states of the kind (3.2) and their particle-hole images, on multiplicity-one weight spaces; no classification is proved, and weight spaces of higher multiplicity are not covered.

## 5. What the states that meet SC-loop are

**Coherence zero.** In every state of Theorems L0, L0-r and S∞ each end holds a definite number of rishons. `U^{jk}_ℓ` changes `N^{ℓ,x}` by one, so `ω(U^{jk}_ℓ) = 0` on every link. Y2W's coherence `κ(ω) = 2Σ_{jk}|ω(U^{jk})|^2/ω(M)` (Y2W line 110) is therefore `0` on every link. These states are flux states, the opposite of the aligned coherent states of Y2W's Attack 3.

**SC's own two-order clause excludes the states of Theorem S∞.** Take a block plaquette `p` in the `(e_1, e_2)`-plane whose lowest corner is an even block site, and let `W^{(r)}_p` run `(0,0) → (1,0) → (1,1) → (0,1) → (0,0)` (block units). Its `e_1`-edges hold their rishons toward their even endpoints and its `e_2`-edges toward their odd endpoints. Going round `p` in this direction, every fine link's occupied end is then the tail of its step. Every step removes a rishon at its head, so `W^{(r)}_p Ψ_k = 0` (for `m ≤ 5`). The reverse loop `W^{(r)†}_p` removes rishons at those tails, and `W^{(r)†}_p Ψ_k ≠ 0`: its index sum yields distinct basis vectors with coefficients `±1`. Suppose `Λ_r` contains `Ŵ_p = c_ι W^{(r)}_p` with `ι(Ŵ_p) = w_p`, and SC(`r`; `δ`) holds with a `μ` satisfying `E_μ(1 − Re w_p) ≤ ε_μ`. Definition SC maps both `Ŵ_p^†Ŵ_p` and `Ŵ_pŴ_p^†` to `|w_p|^2`, and `E_μ|w_p|^2 ≥ (E_μ Re w_p)^2 ≥ (1 − ε_μ)^2`. But `ω(Ŵ_p^†Ŵ_p) = |c_ι|^2 ‖W^{(r)}_p Ψ_k‖^2 = 0`. So SC fails in `Ψ_k` whenever `(1 − ε_μ)^2 > δ`. For `m ≥ 6` the same holds with the two products exchanged. So SC itself excludes these states; SC-loop on `U(1)`-blind cube loops does not.

## 6. What follows for (A)

**Lemma 0′ (Lemma 0 for a cube product; rebuilt).** Let `Θ'` be one of the operators `Θ^σ_c` or `Θ^S_c`. Suppose `Λ_r` contains `Θ̂ := c_ι Θ'` with `ι(Θ̂) = Θ_c := Π_f w_f`, each `w_f` a normalised trace, so `|Θ_c| ≤ 1`. Suppose `μ` satisfies `E_μ(1 − Re Θ_c) ≤ ε_Θ`. If SC(`r`; `δ`) holds with this `μ`, then `D_ω(Θ̂) ≤ 8ε_Θ + 6δ`.

*Proof.* `D_ω(Θ̂) = ω(Θ̂^†Θ̂) + ω(Θ̂Θ̂^†) − 2ω(Θ̂) − 2ω(Θ̂^†) + 2`. Definition SC puts each of the four expectations within `δ` of `E_μ|Θ_c|^2`, `E_μ|Θ_c|^2`, `E_μΘ_c`, `E_μΘ̄_c`. The `μ`-side value is `2E_μ|Θ_c − 1|^2`, and the error is at most `2δ + 4δ`. Since `|Θ_c| ≤ 1`, `|Θ_c − 1|^2 = (1 − Re Θ_c)^2 + (Im Θ_c)^2 ≤ 4(1 − Re Θ_c)`, as in Y2W line 66. ∎

**Under reading B.** Let ZM1-G list all 720 orders of the boundary-loop block cube products at each scale, with one normalisation `c_ι`. By Theorem B1, SC-loop fails at every scale for `m ∈ {1, 9}` once `8ε_Θ + 6δ < 1`. By Theorem B2 it fails at every scale for `m ∈ {2, 8}` once `8ε_Θ + 6δ < 1/453600`. With Lemma 0′, these sectors then have no window, for every value of `ε`, `μ`, `τ_E` and every plaquette class. This is (A) restricted to those values of `m`. It rests on `ε_Θ` for T0-start's class, to be confirmed on the YM branch as Y2W line 161 says of `ε_μ`.

**Under reading S.** Theorem S∞ meets SC-loop with `η = 0` at every scale, for every `m` and every value of the other constants. So Lemma 0′ yields nothing there. A proof of (A) through Y2-W-L would have to use properties of the state VC1 supplies.

## 7. Comparison with `L5-O`'s register knob

`Y2W_DRAFT.md` line 175: "In `φ^{⊗k}`, with `φ` the state of W2(iii) taken in `S_+`, the link variables `Σ_iU^{ab}_{(i)}` have coherence `k/(k + 9)` (Lemma W4)". Line 113 (Theorem W2(i)): on the `L5-U` register "`κ(ω) ≤ 1/2` for every state".

1. The states that meet SC-loop in this file have `κ = 0` (section 5). So SC-loop on `U(1)`-blind cube loops is met with no coherence at all. `L5-O`'s knob raises the coherence toward `1`; `L5-U`'s fixed register caps it at `1/2`. Under reading S this difference is invisible to Y2-W-L, since `L5-U` meets it at every scale (Theorem S∞). So Y2-W-L under S cannot separate the laws in `L5-O`'s favour.
2. Under reading B, `L5-U`'s floors come from the size of its rishon register. In Theorem B1 an end space `Λ^0` or `Λ^5` is one-dimensional, so `E` or `1 − E` vanishes on it. In Theorem B2 six one-rishon ends cannot be antisymmetric in five colours. These are finiteness facts of the same kind as `K_m` in Theorem W1 and the bound `1/2` in Theorem W2. On `L5-O[S_+]` the link variables satisfy `(U^{ab})^2 = 1` (Theorem W2(iii)), so no factor of a loop product vanishes on a whole sector, and an end carries no rishon number. Neither mechanism transfers as it stands. Whether `L5-O[S_+^{⊗k}]` meets reading B on all cubes, for some or all `k`, is not analysed here.
3. So the coherence that the knob controls is not tested by SC-loop on `U(1)`-blind loops under S. Section 5 shows that SC's own two-order clause does see the flux states. Under B the fixed register of `L5-U` costs the sectors `m ∈ {1, 2, 8, 9}`.

## 8. Scratch checks (guides only)

All in `/tmp/toe-y2wl/` on the Mac mini; numpy 2.4.1, scipy 1.17.0; floating point.

| Check | Script | What it showed |
|---|---|---|
| (1) | `corner.py` | corner operators on `Λ^{n_1} ⊗ Λ^{n_2} ⊗ Λ^{n_3}` per `U(5)` highest weight: values `4, −2` on the antisymmetric states of three one-rishon ends; `0` on symmetric ones; `(4, −2)` and `(−2, 4)` on two spectator-type weights at `(2,2,2)` (9 s) |
| (2) | `joint.py`, `ratios.py`, `ratios2.py` | 14 joint eigenvectors with all six eigenvalues nonzero on sectors `1 ≤ n_i ≤ 4`, all of spectator-`Λ^N` type or particle-hole images; product form of the eigenvalues holds for all 14 (46 s) |
| (3) | `lattice_aligned.py` | no translation-invariant colour-aligned state gives a nonzero cube product for any order and any `m` |
| (4) | `orient.py`, `orient_rules.py`, `rule_check.py` | occupied-end patterns compatible with some order in every cube: none of period 1; many of period 2; 138 parity rules; the rule of Theorem S∞ gives 8 compatible orders in both cube types, with the precedences of its proof |
| (5) | `tetra.py` | Lemma K exact on a closed four-triangle surface, all 24 orders, `N = 2` at `m = 1, 2, 3` and `N = 3` at `m = 1` |
| (6) | `b2site.py` | the site sum of Theorem B2, Step 2, with the other corner factors set to `1`: lowest eigenvalue at least `7.68` on a grid of ten values of `c`, against the proved bound `1/16200` |

---

## FINISH

**Proved here (pass 1, not distilled or refereed).**
- Definition UB and Lemma B0: a loop product that crosses every link equally often both ways commutes with every `N^{ℓ,x}`. The three readings F, S, B of the cube product, with the four-test check: F fails test 4; S passes; B passes, with test 4 conditional on Definition SC's two-order clause.
- Lemma C: the two factors on a link compose to `E` at the particle end times `1 − E` at the hole end. Lemma K: a block cube product is a product of commuting corner operators, each a trace of `E`'s and `1 − E`'s. Lemma T: one or two particle ends at each block corner, four corners of each kind; one at each inner point. Lemma S: colours present at all ends of a corner, or absent at all, drop out of its operator. Lemma P: the particle-hole map sends the sector `m` to `10 − m` and `Θ^σ_c` to `(Θ^{σ^{rev}}_c)^†`. Lemma R: with one rishon per end the corner operators lie in the group algebra of `S_3`; they vanish on symmetric colour states, equal `4` and `−2` on antisymmetric ones, and are idempotent on the two-dimensional part.
- Theorem L0 (Y2-W-L0, one unit cube, every state): for every `m`, `D = 0` is attained under F and under S. Under B, `D = 0` is attained for `m ∈ {2, …, 8}` for all 720 orders at once; for `m ∈ {1, 9}`, `D(σ) + D(σ^{rev}) ≥ 2` in every state.
- Theorem L0-r: the same for one block cube at every scale, with boundary-loop block faces.
- Theorem S∞: under S, the parity flux state (`e_1`-links occupied at the even end, `e_2`- and `e_3`-links at the odd end) meets SC-loop(`r`; 0) for all block cubes at every scale, for every `m`.
- Theorems B1 and B2: under B, SC-loop fails in every state at every scale for `m ∈ {1, 9}` when `η < 1`, and for `m ∈ {2, 8}` when `η < 1/453600`.
- Remark F: a fixed order covariant under translations fails on all cubes for `m ∈ {1, 9}`.
- Section 5: the states that meet SC-loop have coherence `κ = 0`; SC's own two-order clause on plaquettes excludes the states of Theorem S∞ when `(1 − ε_μ)^2 > δ`.
- Lemma 0′ (section 6): SC gives `D_ω(Θ̂) ≤ 8ε_Θ + 6δ` for a listed cube product.

**Counterexamples.**
- To Y2-W-L0 as a kinematic floor on one cube: it fails under F and S for every `m`, and under B for `m ∈ {2, …, 8}` (Theorem L0, explicit states).
- To the (A)-route of `Y2W_DRAFT.md` section 4 under reading S: the states of Theorem S∞ meet SC-loop at every scale, for every `m` and every value of the other constants. So no kinematic proof that "Y2-W-L fails for every choice" exists under S.
- None of these is a counterexample to (A) itself. The states violate SC (section 5); they are not windows.

**Open, by name.**
- **Y2-W-LB(m), `m ∈ {3, …, 7}`** (section 4.3): reading B on all block cubes at one corner. Attack 1 (extend the states (3.2)) fails at "the eight octants at `x` keep antisymmetric active parts". Attack 2 (support argument) fails at "in every sector some end is empty or full". Attack 3 (the `S_3` argument of Theorem B2) fails at "the corner operators are polynomials in the permutations of three one-rishon ends".
- **Y2-W for `L5-U`** (Y2W's item) stays open. Under S its decision needs the state VC1 supplies. Under B it fails for `m ∈ {1, 2, 8, 9}` given Lemma 0′'s hypotheses, and is open for `m ∈ {3, …, 7}`.
- `ε_Θ = E_μ(1 − Re Θ_c)` for T0-start's class, from the YM branch, as Y2W asks for `ε_μ`.

**What changes downstream.**
1. `Y2W_DRAFT.md` FINISH item 4 ("attack Y2-W-L0, then Y2-W-L"): Y2-W-L0 is decided (Theorem L0). Y2-W-L is decided under S (met, Theorem S∞) and under B for `m ∈ {1, 2, 8, 9}` (fails, Theorems B1-B2). Y2-W-LB remains. The condition in `Y2W_DRAFT.md` line 201, "and for every loop if Y2-W-L0 holds", is met only under B and only for `m ∈ {1, 9}`.
2. GA2: SC-loop on `U(1)`-blind loops is met by flux states of coherence `0` that SC itself excludes (section 5), so by itself it cannot detect small coupling. The `U(1)`-blind part of SC that excludes them is SC's own two-order clause on plaquettes, a first-moment condition with ZM1-G's normalisation. A sub-lemma built on that clause is not attacked here.
3. `L5-U`: no named failing step for the law. Under B, given Lemma 0′'s hypotheses, its free datum `m` would be confined to `{3, …, 7}`. Recorded, not proposed. Both laws stay live under `TOE_ASSEMBLY.md` section 3.5.
4. `L5-O`: nothing about `L5-O` is proved here; section 7 compares only. The register knob acts on coherence, which SC-loop on `U(1)`-blind loops does not see under S.
5. Owner decision, if wanted: reading S or reading B for the cube observable, or leave the choice to ZM1-G. Nothing is adopted here.
