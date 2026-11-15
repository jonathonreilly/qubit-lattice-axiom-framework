# CG1 kill test on the five-mode laws, pass 1

Written 2026-11-05 by a Claude Opus 5.5 subagent, as a pass-1 lane under owner decision LW1-5-RQ ("keep both live ... until one fails at a named step"). It asks one question of each law: can local, gauge-covariant operators carry the representation content of one Standard Model family? Method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation (`check_cg1k.py`, output `out.txt`, in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-yalow-de8f06/bd9fd3c1-9024-4004-87d2-e8917bcfe6a3/scratchpad/cg1k/`; about 8 s, a few MB). A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `toe-assembly-local` (same commit as `claude/toe-assembly`) | `4b50cd57d8` |

Files read at that commit, by line: `TOE_ASSEMBLY.md` lines 71-219 (section 3 in full, with 3.4 and 3.5) and 397-427 (CH1, CG1); `LW1_5O_DRAFT.md` lines 1-329 (all); `LW1_5U_DRAFT.md` lines 1-78 (head, outcome, setting, Lemma E), 111-137 (section 3), 195-242 (sections 6-7), 260-309 (section 9, FINISH); `LW1_5_DRAFT.md` lines 47-61 (one site), 148-200 (section 4.1-4.2), 229-348 (sections 4.4-8), 422-445 (section 10); `CH1_DRAFT.md` lines 47-48 and 55 (statements of Lemma S1 and Theorem S2, by `grep`).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws and CG1 are read plainly. Where CG1's words allow two readings, both are named and treated, and neither is adopted (section 6).

**Working set used, by name.** PS-5 (fallback text, D1); PS-6 and PS-6r (frames and registers), only through the two laws of `LW1_5_DRAFT.md` section 8.1 (`L5-O`, and its variant `L5-U`). MT1's statistics enter as one reading (R-F, section 1). Results used, cited by name: from `LW1_5O_DRAFT.md`, Lemma K0, Lemma F, Theorem K, Proposition E, Theorem P, Proposition T; from `LW1_5_DRAFT.md`, Theorem G, Lemma Q4, Lemma Z, Theorem U; from `LW1_5U_DRAFT.md`, Lemma Z-U, Proposition D. PS-1 to PS-4, PS-7 and PS-11 are not used.

---

## 0. The question, quoted

`TOE_ASSEMBLY.md` line 214: "The owner chose: **keep both live.** MT1, GA1 and CG1 are developed on both laws until one fails at a named step."

CG1(a), line 414: "The light chiral content of one family is the Standard Model one-generation multiplet — `(3,2)_{1/6}`, `(3bar,1)_{-2/3}`, `(3bar,1)_{1/3}`, `(1,2)_{-1/2}`, `(1,1)_{1}`, and optionally `(1,1)_0` — equivalently the 16 of `Spin(10)` branched under `SU(3) x SU(2) x U(1)`".

The fact that motivates the kill test on `L5-O`. `LW1_5O_DRAFT.md` line 97, Theorem K (K1): "`Ad z_x` is the identity on the matter algebra. Every matter operator lies in a true `SO(10)` representation at every site, and fermion-odd matter operators are class 2 (Lemma F)." Its line 161 already notes: "CG1 read with "the Standard Model multiplet" is not excluded: `SU(5)` pieces of one family sit inside tensor-class representations of `Spin(10)`". This file turns that remark into theorems, for every embedding of the Standard Model group.

## 0.1 Outcome in one paragraph

**`L5-O` is not killed under the local-field reading.** Up to conjugacy, a Standard Model Lie algebra sits in `so(10)` in one of two ways (Lemma C). In Case I, `SU(3) x SU(2)` acts on `C^3 + C^2 = C^5`, every such embedding lies in a `U(5)`, and the hypercharge is `diag(a,a,a,b,b)` with a free ratio `α:β`. In Case II, `SU(2)` rotates three of the ten Majorana directions. Case II fails: `−1 ∈ SU(2)` maps to `−1 ∈ Spin(10)`, so no doublet sits in any tensor-class representation (Theorem O-II). Case I passes: for every ratio, the whole family with its hypercharge ratios sits in tensor-class representations. The members are all fermion odd exactly when `α` is even, that is, exactly when fermion parity is not a gauge transformation of the embedded group (Theorem O-I). The standard ratio `2:3` is even. At one site, `c`, `ccc` and `c^5` carry the six members with the right hypercharges, on both laws (Proposition F). **The kill holds only under a stronger reading,** R-M: "the family is a whole multiplet of the exact gauge group". On `L5-O`, every tensor-class `Spin(10)` multiplet that contains `(3,2)_y` has at least 40 components, under every embedding (Theorem O-M). So the family is never a whole `Spin(10)` multiplet of the law's operators. **`L5-U` passes both readings.** Its embeddings are Case I only (Lemma C-U). The criteria are the same as on `L5-O` (Theorem U-B). Under R-M, the family is `5bar_{−1} + 10_{−3} + 1_{−5}` with `Y ∈ su(5)`, which the standard assignment forces, or a flipped assignment with another ratio and a `U(1)_N` part in `Y` (Theorem U-M). On both laws the ratio `α:β` is free. The law does not fix it. It is CG1-i (P-HY), or the breaking pattern of EW1/VC1. **Representation content is not chirality.** Local operators always come with their adjoints. CH1 must still select the light chiral family and gap its mirrors and doublers. On `L5-O`, it must also gap the non-family partners of the parent multiplets, without #10014's protection of the 16. On `L5-U`, it must handle a gauged `U(1)_N` whose anomalies on one family are `(−40, −400, −5)` (section 5).

---

## 1. Readings and conventions

**Notation.** At a site, `c_{x,j} = (γ_{x,2j−1} + iγ_{x,2j})/2`, `j = 1, …, 5` (`LW1_5_DRAFT.md` line 49). Modes 1-3 are the colour block and modes 4-5 the doublet block. `G` is the exact local gauge group: `Spin(10)_y` on `L5-O` (Theorem G), `U(5)_y` on `L5-U` (Theorem U). An embedding is an injective Lie algebra map `ψ: 𝔤_SM = su(3) ⊕ su(2) ⊕ u(1) → 𝔤`. Its group `H ⊂ G` is generated by `exp ψ(𝔤_SM)`. The `U(1)` of `G_SM` maps onto a closed circle (any normalisation). `G̃ = SU(3) × SU(2) × R` is the simply connected group of `𝔤_SM`. The family with hypercharge unit `t ≠ 0` is the `𝔤_SM`-module
\[
F_t=(3,2)_{t}\oplus(\bar 3,1)_{-4t}\oplus(\bar 3,1)_{2t}\oplus(1,2)_{-3t}\oplus(1,1)_{6t}\;[\oplus(1,1)_0],
\]
where the subscript is the eigenvalue of `ψ(Y)`. `t = 1/6` is the usual normalisation. Any `t ≠ 0` is allowed.

**Definition (carried at a site).** A finite-dimensional space `𝒪` of local operators *carries* an `H`-representation `σ` at `y` if `Ad` of the local copy `H_y` maps `𝒪` to itself with `Ad|_𝒪 ≅ σ`, and every other local group `G_z`, `z ≠ y`, fixes `𝒪` pointwise. Link dressing is allowed. Every local operator spans a finite-dimensional `G_y`-representation, so `G`-covariance alone says nothing. The readings say which representation must be the family.

**The readings.** Each is a reading of words already in CG1, CH1 and MT1. None is adopted (section 6).
- **R-B (component reading).** Each member of `F_t` is carried at some site by a space of local operators, for one `t` and one embedding. This is the lead's local-field reading: light excitations created by local gauge-covariant operators, with charges read through `H`. It presupposes that at the scales where the family is light, the gauge group is `H`. That is EW1/VC1's question.
- **R-M (multiplet reading).** There is a space `𝒪` carried at `y`, invariant under the whole of `G_y`, whose restriction to `H_y` is `F_t`. Optionally it is `F_t` plus its adjoint `F_t^*`, to allow a `*`-closed space. This reads "equivalently the 16 of `Spin(10)`" with `G` in place of `Spin(10)`. It fits the case where `G` stays unbroken at those scales.
- **R-F (statistics).** In either reading, the members are created by fermion-odd operators. MT1 asks for fermions.

**Which operators.** On `L5-O` the statements use operators of the *law's algebra*: the algebra generated by matter, gates and gauge-invariant operators, as in Theorem P(ii). The fermion-parity statements also use one end-pure register class (Lemma Z's hypothesis, which `L5-O[S_+]` meets), or matter at one site. `LW1_5O_DRAFT.md` line 129 shows that this algebra commutes with every `z_x`: "`A` commutes with `z_x`: matter by (K1), gates by (K3), gauge-invariant operators by definition". So on it, `−1 ∈ Spin(10)_y` acts as the identity: every operator of the law's algebra is tensor class at every site. Operators outside it, such as `X` of Proposition E, are treated in section 3.6.

---

## 2. The embeddings

**Lemma C (embeddings into `so(10)`).** Up to conjugation by `Pin(10)`, up to the automorphism `3 ↔ 3bar` of `su(3)`, and up to `Y ↦ λY` (`λ ≠ 0`), every embedding `ψ: 𝔤_SM → so(10)` is one of these. Write `R^{10} = R^6 ⊕ R^4` and give `R^6` the complex structure of `C^3`.
- **Case I(α:β).** `su(3)` acts on `C^3` as the `3`. `su(2)` acts on `R^4 = C^2` as the `2` (it is `su(2)_L ⊂ so(4)`). `ψ(Y) = (ia·1_3) ⊕ (ib·1_2) ∈ u(3) ⊕ u(2) ⊂ u(5) ⊂ so(10)`, with `(a, b) = (α, β)` coprime integers, `(α, β) ≠ (0, 0)`, and `α:β` taken up to the signs of `α` and `β`. Every Case I embedding lies in a `U(5) ⊂ SO(10)`.
- **Case II.** `su(3)` acts on `C^3` as the `3`. `su(2)` acts as `so(3)` on three coordinates of `R^4` and trivially on the fourth. `ψ(Y) = ia·1_3` on `C^3`, `a ≠ 0`, and `0` on `R^4`.

Each `Pin(10)` class is at most two `Spin(10)` classes. Every statement below is unchanged by `Pin(10)` conjugation, by `3 ↔ 3bar` together with `Y ↦ −Y`, and by `Y ↦ λY`. The reason: `−1 ∈ Spin(10)` is central in `Pin(10)`, and the set of tensor-class representations is closed under conjugation.

*Proof.* (a) *The colour block.* `V = R^{10}` is a real `su(3)`-module and `V_C` is self-conjugate. The nontrivial complex irreducible `su(3)`-modules of dimension at most 10 are `3, 3bar, 6, 6bar, 8, 10, 10bar` (dimension `(p+1)(q+1)(p+q+2)/2` for highest weight `(p,q)`; cited, [check] (6)). Self-conjugacy gives `3` and `3bar` equal multiplicity, and likewise `6/6bar` and `10/10bar`. With 10 dimensions, the nontrivial part of `V_C` is `3 ⊕ 3bar` or `8`. If it is `8`, `su(2)` commutes with `su(3)`. On the trivial `R^2` it acts through the abelian `so(2)`, so trivially, because `su(2) = [su(2), su(2)]`. On the `8`, it acts by an element of the commutant of an absolutely irreducible module, which is `R·1`, and `R·1 ∩ so(8) = 0`. Then `su(2)` acts trivially, against injectivity. So `V = V_6 ⊕ V_4` with `(V_6)_C = 3 ⊕ 3bar` and `su(3)` trivial on `V_4`. The commutant `End_{su(3)}(V_6)` is a two-dimensional real algebra, because its complexification is `End(3 ⊕ 3bar)^{su(3)} = C ⊕ C`. It is not `R ⊕ R`, since that would split `V_6` into two real three-dimensional `su(3)`-modules, and `su(3)` (dimension 8) does not embed in `so(3)` (dimension 3). So it is `C = R[J]`. Replace `J` by its orthogonal polar part, which still commutes. Then `(V_6, J) ≅ C^3`, with `su(3)` acting as `3` (or `3bar`, which the automorphism exchanges). The commutant of `su(3)` in `so(6)` is `R·J`.
(b) *The doublet block.* `su(2)` commutes with `su(3)`, so on `V_6` it acts through the abelian `R·J`, hence trivially. On `V_4` it acts through `so(4) = su(2)_L ⊕ su(2)_R` (`LW1_5O_DRAFT.md` line 253 uses the same split). The image is isomorphic to `su(2)`. Each projection to a factor is `0` or an isomorphism, by simplicity. So the image is `su(2)_L`, `su(2)_R`, or a graph `{(X, θX)}` with `θ` an automorphism. Automorphisms of `su(2)` are inner, so a graph is conjugate to the diagonal, which is `so(3)` on three coordinates of `R^4`. `su(2)_L` and `su(2)_R` are exchanged by a reflection of `R^4`. This gives Case I and Case II.
(c) *The hypercharge.* `ψ(Y)` commutes with `su(3) ⊕ su(2)`. There is no equivariant map between `V_6` and `V_4`: as `su(3)`-modules they have no common constituent. In Case I, the commutant is `R·J ⊕ su(2)_R`. Conjugating by `SU(2)_R`, which commutes with `su(3) ⊕ su(2)_L`, puts the `su(2)_R` part on a fixed Cartan generator, the complex structure `J_2` of `C^2`. So `ψ(Y) = aJ ⊕ bJ_2`. In Case II, the commutant on `V_4 = R^3 ⊕ R` is `0` (`R^3` is absolutely irreducible under `so(3)`, and `so(1) = 0`), so `ψ(Y) = aJ`. Injectivity needs `(a, b) ≠ 0` in Case I and `a ≠ 0` in Case II. *Closed circle.* `exp(2πsψ(Y))` rotates three planes by `2πsa` and two by `2πsb`. It returns to `±1` only if `sa, sb ∈ Z`, so a closed circle needs `a/b ∈ Q ∪ {∞}`. Rescale to coprime integers. The signs of `α` and `β` change under `Y ↦ −Y`, under `3 ↔ 3bar` (complex conjugation of `C^3`), and under the Weyl element of `SU(2)_R`. ∎

**Lemma C-U (embeddings into `u(5)`).** Up to `U(5)` conjugation and `Y ↦ λY`, every embedding `ψ: 𝔤_SM → u(5)` makes `C^5 = (3,1) ⊕ (1,2)` (or `(3bar,1) ⊕ (1,2)`, the image under the outer automorphism `u ↦ ū`), with `ψ(Y) = i·diag(α,α,α,β,β)` and `(α, β)` coprime integers. There is no Case II.

*Proof.* A joint irreducible component with both factors nontrivial has dimension at least `3·2 = 6 > 5`. So `C^5` splits into an `su(3)` part and an `su(2)` part. The nontrivial `su(3)`-modules of dimension at most 5 are `3` and `3bar`, and `su(2)` needs at least 2 dimensions. So the split is `3 + 2`. The commutant in `u(5)` is `u(1) ⊕ u(1)`, the two block scalars. Closure gives a rational ratio, as in Lemma C(c). ∎

Lemma C's Case I and Lemma C-U are the same family of embeddings: on `L5-O`, Case I lies in the `U(5)` of the complex structure `J ⊕ J_2`.

---

## 3. `L5-O`

### 3.1 Weights

Use the maximal torus of `Spin(10)` that rotates the five coordinate planes `(γ_{2j−1}, γ_{2j})`. In Case I, plane `j` is the complex coordinate `j` of `C^5 = C^3 ⊕ C^2`. In Case II, planes 1-3 are `C^3`, plane 4 is the rotation plane of the `so(3)` Cartan generator, and plane 5 holds the remaining coordinate of `R^3` and the trivial `R^1`.

**Lemma W (tensor-class weights).**
(W1) Every representation of `Spin(10)` on which `−1` acts trivially has weights `n ∈ Z^5`. This holds in particular for `G_y` acting on any space of the law's algebra.
(W2) On a weight `n`, `−1_{SO(10)}` (rotation by `π` in every plane) acts as `(−1)^{Σ_j n_j}`.
(W3) Weight multiplicities are invariant under the signed permutations of the five coordinates with an even number of sign changes.
(W4) In Case I, a weight `n` restricts to: the `su(3)`-weight of `(n_1, n_2, n_3)` modulo `R(1,1,1)`; the `su(2)`-weight `(n_4 − n_5)/2`; and the hypercharge `Y(n) = a p + b q`, with `p = n_1 + n_2 + n_3` and `q = n_4 + n_5`. Triality is `p mod 3` and doublet parity is `q mod 2`. In Case II the `su(2)`-weight is `n_4 ∈ Z` and `Y(n) = a p`.

*Proof.* (W1) The representation factors through `SO(10)`. The torus of `SO(10)` is `(R/2πZ)^5`, and its characters are `e^{iΣn_jθ_j}` with `n ∈ Z^5`. The law's algebra commutes with `z_y` (`LW1_5O_DRAFT.md` line 129, quoted in section 1). (W2) Put `θ_j = π`. (W3) A permutation of the planes, or a reflection of two planes together, is an element of `SO(10)` that normalises the torus. It lifts to `Spin(10)`. Conjugation by it preserves the character. (W4) The Cartan elements of `ψ(𝔤_SM)` are block-diagonal rotations in these planes. A weight is evaluated plane by plane. The `su(3)` Cartan generators are the traceless diagonal elements on `C^3`. The weight `h ↦ Σ_{j≤3}n_jh_j` depends on `(n_1,n_2,n_3)` only modulo `(1,1,1)`. Its triality is `p mod 3`. The `su(2)` Cartan generator is `diag(1/2, −1/2)` on `C^2` in Case I, and the rotation generator with eigenvalues `±1, 0` on `R^3` in Case II. ∎

**Lemma Z6 (the family is one character raised to powers).** For each member of `F_t`, write `(τ, δ, y)` for its triality, its doublet parity and its hypercharge. Then `(τ, δ, y) = n·(1, 1, t)` modulo `(3, 2, ·)`, with `n = 1, −4, 2, −3, 6, 0` for `Q, u^c, d^c, L, e^c, ν^c`.

*Proof.* Read it off: `Q = (3,2)_t` has `(1, 1, t)`. `u^c = (3bar,1)_{−4t}`: `−4 ≡ 2 mod 3`, `−4` even. `d^c = (3bar,1)_{2t}`: `2 ≡ 2`, even. `L = (1,2)_{−3t}`: `−3 ≡ 0`, odd. `e^c = (1,1)_{6t}`: `6 ≡ 0`, even. `ν^c`: `0`. ∎

So a central element of `G̃` acts on member `n` as `χ^n`, where `χ` is its scalar on `Q`. This is the statement that one family is a representation of `G_SM/Z_6`.

**Lemma T (small tensor products).** In `3^{⊗A} ⊗ 3bar^{⊗B}`, the representation `3` occurs when `A − B ≡ 1 mod 3`, `3bar` when `A − B ≡ 2`, and `1` when `A − B ≡ 0`. In `2^{⊗N}`, `2` occurs when `N` is odd and `1` when `N` is even.

*Proof.* Induct, using `3 ⊗ 3 ⊃ Λ^2 3 ≅ 3bar`, `3bar ⊗ 3bar ⊃ 3`, `3 ⊗ 3bar ⊃ 1` (the trace pairing) and `2 ⊗ 2 ⊃ Λ^2 2 = 1`. ∎

### 3.2 Case II fails

**Theorem O-II.** In Case II, the element `k = (1, −1, 0) ∈ G̃` maps to `−1 ∈ Spin(10)`. So no `(3,2)_y` and no `(1,2)_y`, for any `y`, sits in any tensor-class representation of `Spin(10)`. On `L5-O`, no space of the law's algebra carries `Q` or `L` at any site, under any register choice.

*Proof.* Let `J_3 ∈ so(3)` rotate the plane `(7,8)` with eigenvalues `±i` on it. In `SU(2)` the same Lie algebra element acts on the doublet with eigenvalues `±i/2`, so `exp(2πJ_3) = −1_{SU(2)}`. In `Spin(10)`, `exp(2πJ_3)` is a full turn in one coordinate plane, which is `−1` (`LW1_5O_DRAFT.md` Lemma K0's proof: "a full turn in any coordinate plane ... the same central element `−1`"). The map `G̃ → Spin(10)` sends exponentials to exponentials, so `k ↦ −1`. On a tensor-class representation `−1` acts trivially. On any doublet `k` acts as `−1`. The last sentence follows by Theorem K's (K1) and Theorem P(ii). ∎

By Lemma W(W4) the same thing reads: in Case II all `su(2)`-weights are integers, so all spins are integers. Case II is the `SU(2) = Spin(3)` of `LW1_5O_DRAFT.md` line 249 ("the `SU(2) = Spin(3)` that rotates `γ_{x,1}, γ_{x,2}, γ_{x,3}` contains `exp(2πiM^{12}) = −1`"). So the `SU(2)` of CG1 on `L5-O` must be the `SU(2)_W` type of line 250, which is Case I.

### 3.3 Case I passes

**Theorem O-I (Case I).** Take Case I(α:β).
(i) *Criterion.* Let `σ = (σ_3, σ_2, y)` be irreducible with `σ_3 ∈ {1, 3, 3bar}` and `σ_2 ∈ {1, 2}`, and let `ε ∈ {0, 1}`. Then `σ` occurs in a tensor-class `Spin(10)`-representation on which `−1_{SO(10)}` acts as `(−1)^ε` exactly when there are `(p, q) ∈ Z^2` with
\[
ap+bq=y,\qquad p\equiv\tau(\sigma_3)\ (3),\qquad q\equiv\delta(\sigma_2)\ (2),\qquad p+q\equiv\varepsilon\ (2).
\]
When it occurs, it occurs in `V^{⊗N}` for some `N ≡ ε mod 2`.
(ii) *The family, any parities.* For every ratio and every `(p_1, q_1)` with `p_1 ≡ 1 (3)`, `q_1` odd and `t := ap_1 + bq_1 ≠ 0` (such a pair exists), the whole family `F_t` occurs in tensor-class representations. Member `n` occurs at `(np_1, nq_1)`.
(iii) *The family, all fermion odd.* All six members (and `ν^c`) occur with `−1_{SO(10)}` acting as `−1`, for one common `t`, exactly when `α` is even. That holds exactly when `−1_{SO(10)}` is not in the image of `H` in `SO(10)`.
(iv) On `L5-O`, under one end-pure register class or for matter at one site, `−1_{SO(10)}` at `y` acts on spaces carried at `y` as fermion parity. So (iii) is R-B with R-F: a fermion-odd family is carried exactly when `α` is even.

*Proof.* (i) *Only if.* Weights of such a representation lie in `Z^5` (W1), with `Σn_j ≡ ε` (W2). Any weight of `σ` gives `(p, q)` by (W4). *If.* Choose `n_3, n_{3bar}, n_+, n_− ≥ 0` with `n_3 − n_{3bar} = p` and `n_+ − n_− = q`. Over `C`, `V_C = 3_a ⊕ 3bar_{−a} ⊕ 2_b ⊕ 2_{−b}`. So `V_C^{⊗N}`, with `N = n_3 + n_{3bar} + n_+ + n_−`, contains `3^{⊗n_3} ⊗ 3bar^{⊗n_{3bar}} ⊗ 2_b^{⊗n_+} ⊗ 2_{−b}^{⊗n_−}`, of hypercharge `ap + bq`. By Lemma T it contains `σ_3 ⊗ σ_2`. Then `N ≡ p + q mod 2`, and `−1_{SO(10)}` acts on `V^{⊗N}` as `(−1)^N`. If `N = 0` is needed (`σ` trivial, `p = q = 0`), use `V ⊗ V ⊃ 1`.
(ii) A pair exists: `(1, 1)` and `(1, −1)` give `a + b` and `a − b`, and these are not both zero. `(np_1, nq_1)` satisfies (i)'s congruences for member `n` by Lemma Z6, and its hypercharge is `nt`.
(iii) *If `α` is even* (so `β` is odd). Choose `p_1 = 4` and `q_1 ∈ {1, 3}` with `t = 4α + βq_1 ≠ 0`. (Both values zero would force `β = 0`.) Then `p_1 + q_1` is odd. For member `n` take `(p_n, q_n) = n(p_1, q_1) + m_n(β, −α)`, with `m_n = 0` for odd `n` and `m_n = 3` for even `n`. The shift keeps `Y`. It keeps `p mod 3` because `3 | m_n`, and `q mod 2` because `α` is even. It changes `p + q` by `m_n(β − α)`, which is odd exactly when `m_n` is odd. So `p_n + q_n ≡ n + m_n ≡ 1`. By (i), every member occurs fermion odd.
*If `α` is odd.* Suppose the members occur fermion odd with a common `t = αp_1 + βq_1`, where `p_1 + q_1` is odd. For member `n`, `(p_n − np_1, q_n − nq_1)` solves `αu + βv = 0`, so it equals `m(β, −α)` (coprime). The congruence `q_n ≡ n ≡ nq_1 mod 2` forces `mα` even, so `m` is even. Then `p_n + q_n ≡ n(p_1 + q_1) ≡ n mod 2`. That is even for `u^c, d^c, e^c, ν^c`, a contradiction.
*Centre form.* `−1_{SO(10)}` is in the image of `H` exactly when some `g = (ζ^k1_3, (−1)^e1_2, s)` rotates every plane by an odd multiple of `π`. That means `k/3 + sα ≡ 1/2` and `e/2 + sβ ≡ 1/2 mod 1`. For `α` odd, `k = 0` and `s = 1/2` work, with `e = 0` if `β` is odd and `e = 1` if `β` is even. For `α` even, write `sα = 1/2 − k/3 + m` and `sβ = (1 − e)/2 + r`. Then `6β(sα) = 6α(sβ)` gives `3β − 2βk + 6βm = 3α(1 − e) + 6αr`. Mod 2, the left side is `1` (`β` odd) and the right side is `0` (`α` even). So there is no solution. By Lemma Z6, when such a `g` exists it acts on member `n` as `χ^n`. The value `χ = −1` would make the even members even, which is (iii)'s obstruction in centre form.
(iv) `LW1_5_DRAFT.md` line 239, Lemma Z(ii): "the element `−1_{10} ∈ SO(10)` applied at every site of a finite region `Λ` (with its link changes) acts as the fermion parity automorphism on every operator supported, with all its links, inside `Λ`". For a space carried at `y`, the factors at `z ≠ y` lie in `G_z`, which fixes the space pointwise. So only the factor at `y` acts. For matter at one site, Lemma F (`LW1_5O_DRAFT.md` line 88): `−I` acts on `Λ^k` as `(−1)^k`, and `Λ^{odd}` is the fermion-odd part. ∎

[check] (3): for all coprime `(α, β)` with `|α|, |β| ≤ 5`, a brute-force search of `(p, q)` finds a fermion-odd family exactly when `α` is even. No mismatches.

*Remark (examples).* `|α|:|β| = 2:3` is the standard hypercharge, `Y = diag(−1/3, −1/3, −1/3, 1/2, 1/2)`: even. `1:0` (`Y ∝ B − L`, acting on the colour block only) is odd. In that case a fermion-odd `Q` forces `u^c`, `d^c` and `e^c` to be bosonic. `0:1` (`Y` on the doublet block only) is even.

*Remark (local realization).* For the standard ratio, one site suffices (Proposition F). For other even ratios, (i) puts each member in `V^{⊗N}`. Local operators that carry it at `y` arise from fermions transported to `y`. `ψ_{y←x,a} = Σ_bU_ℓ^{ab}γ_{x,b}` (`ℓ = (x, y)`) is invariant under `Spin(10)_x` and a vector at `y`. That is the computation in Theorem G(i)'s proof together with (Q2). Products of the site's modes with transported fermions from the six neighbours are nonzero on the needed components. The reason is that the neighbours' links and sites are distinct tensor factors and the `U^{ab}` are independent (Lemma Q4). Larger `N`, with paths that share links, is not treated. No verdict below uses it.

### 3.4 The family at one site (both laws)

**Proposition F (one site carries one family).** Take the standard embedding: `su(3)` on modes 1-3, `su(2)` on modes 4-5, `Y_x = Σ_jY_j(n_{x,j} − 1/2)` with `Y = (−1/3, −1/3, −1/3, 1/2, 1/2)`. On `L5-O` it lies in `so(10)` and generates `H ⊂ Spin(10)_x` through the Gauss law. On `L5-U` the same `Y`, as `𝒢^T_x` with `T = diag(Y_j)`, lies in `su(5) ⊂ u(5)`. With `i < i' ≤ 3` and `α ∈ {4, 5}`, these spaces of single-site operators carry, at `x`:

| Member | Operators | Representation and `Y` | On `L5-O` inside | On `L5-U` inside |
|---|---|---|---|---|
| `d^c` | `c_{x,i}` | `(3bar,1)_{1/3}` | `Λ^1 = 10` | `5bar_{−1}` |
| `L` | `c_{x,α}` | `(1,2)_{−1/2}` | `Λ^1 = 10` | `5bar_{−1}` |
| `Q` | `c_{x,i}c_{x,i'}c_{x,α}` | `(3,2)_{1/6}` | `Λ^3 = 120` | `10_{−3}` |
| `u^c` | `c_{x,i}c_{x,4}c_{x,5}` | `(3bar,1)_{−2/3}` | `Λ^3 = 120` | `10_{−3}` |
| `e^c` | `c_{x,1}c_{x,2}c_{x,3}` | `(1,1)_{1}` | `Λ^3 = 120` | `10_{−3}` |
| `ν^c` | `c_{x,1}⋯c_{x,5}` | `(1,1)_0` | `Λ^5 = 252` | `1_{−5}` |

All are fermion odd. The hypercharges are in the family's ratios with `t = 1/6`.

*Proof.* *In the Lie algebra.* For `j ≠ k`, `c_j^†c_k + c_k^†c_j = M^{2j−1,2k} − M^{2j,2k−1}` and `i(c_j^†c_k − c_k^†c_j) = M^{2j−1,2k−1} + M^{2j,2k}` (expand with `LW1_5_DRAFT.md` line 49). Also `n_j − 1/2 = M^{2j−1,2j}`. So `u(5)` maps into `so(10) = span{M^{ab}}`, and `𝒢^T_x` with these `T` generates a closed subgroup of `Spin(10)_x`. It is exact, by Proposition T(i) (`LW1_5O_DRAFT.md` line 248). The link parts of the Gauss generators commute with matter, so on site operators only `Y_x` and the site parts of the `su(3)` and `su(2)` generators act. *Charges.* `[n_j, c_j] = −c_j`, so a product of annihilators on modes `S` has `[Y_x, O] = −(Σ_{j∈S}Y_j)O`. That gives: `d^c`: `1/3`. `L`: `−1/2`. `Q`: `−(−2/3 + 1/2) = 1/6`. `u^c`: `−(−1/3 + 1) = −2/3`. `e^c`: `1`. `ν^c`: `−ΣY_j = 0`. *Multiplets.* Annihilators of a block span the dual of the block's creators: `3bar` and `2bar ≅ 2`. Then `Λ^2(3bar) ≅ 3` (the wedge pairing with `Λ^3(3bar) = 1`), and `Λ^2(2) = 1`. So the products have the stated `su(3) × su(2)` types. *Parity.* The degrees are odd. *Containing multiplets.* On `L5-O`, Lemma F: a degree-`k` product of distinct `γ`-combinations lies in `Λ^k`. On `L5-U`, Lemma Z-U(iv). ∎

[check] (1): on the 32-dimensional site, each space has the stated `Y`, is closed under the `su(3)` and `su(2)` generators, and anticommutes with `P_x`.

So the operators that carry the family are *the same operators* on both laws. The laws differ only in which exact multiplet holds them.

### 3.5 Why the family is not one `Spin(10)` multiplet

**Theorem O-M (R-M fails on `L5-O`, every embedding).** Let `𝒪` be a space of the law's algebra carried at `y` and invariant under all of `Spin(10)_y`. For example, the `Spin(10)_y`-span of any operator that carries `Q`. If, for some embedding, `𝒪|_{H_y}` contains `(3,2)_y`, then `dim 𝒪 ≥ 40`. So no such `𝒪` restricts to `F_t` (15 or 16 dimensions) or to `F_t ⊕ F_t^*` (30 or 32), under any embedding and any register choice.

*Proof.* Case II has no `(3,2)` (Theorem O-II). In Case I, a weight of `(3,2)` has `(n_1, n_2, n_3) = e_i + k(1,1,1)`, with entries `{k+1, k, k}`, and `n_4 − n_5 = ±1` (W4). So `n` has a nonzero coordinate among planes 1-3 and another among planes 4-5. By (W3), the weights of `𝒪` include the orbit of `n` under even signed permutations. *Orbit sizes.* Let `κ ≥ 2` be the number of nonzero coordinates. If `κ ≤ 4`, a sign flip on a nonzero coordinate can be paired with one on a zero coordinate, so all `2^κ` sign patterns occur. The `C(5, κ)` supports also occur. So the orbit has at least `C(5,κ)2^κ ≥ min(40, 80, 80) = 40` elements. If `κ = 5` and the moduli are not all equal, at least 5 arrangements of the moduli times 16 sign patterns give at least 80. If `κ = 5` and all moduli equal `c ≥ 1`, the colour entries lie in `{c, −c}`. Two of them differ by `0` or `2c ≥ 2`, never by `1`, so `n` is not a `(3,2)` weight. Hence `𝒪` has at least 40 distinct weights. ∎

[check] (2): over `|n_j| ≤ 3`, the smallest orbit of a `(3,2)` weight has 40 elements. The orbit sizes seen are `1, 10, 16, 40, 80, …`, and the integer 16-orbit has colour differences `0, 2` only.

So on `L5-O`, `Q` sits in `Λ^2 = 45` (fermion even) and `Λ^3 = 120` (fermion odd), never in a smaller exact multiplet. The 16, which restricts to `F_t` under the standard embedding (the usual branching, cited and not used), is spinor class. Theorem O-M extends Theorem K's "never the 16" to "never any multiplet of one family, under any embedding".

### 3.6 What the `L5-O` results use and leave open

**Reading used.** R-B, with or without R-F, for the pass (Theorem O-I, Proposition F). R-M for the failing step (Theorem O-M). Case II fails under every reading (Theorem O-II).

**Left open by these results.**
- *Operators outside the law's algebra.* `LW1_5O_DRAFT.md` Proposition E(ii) gives, on a wider end-mixed register, "a fermion-odd gauge-covariant local operator that carries a half-spin representation at one site". Under the standard embedding, its `H`-content is one family. So R-M can be met by such an operator. But Theorem P says such charges are "never made, moved or screened by matter, by gates or by gauge-invariant operators". They are fixed Gauss sectors, not light excitations. Whether a family can live as a superselection sector rather than as an excitation is not treated here. It would need a reading of CG1 that counts sectors.
- *The 16 as site states.* `LW1_5O_DRAFT.md` E1: the site Fock space is `16 ⊕ 16bar`. That is a states statement, not a field one (its section 2.6).
- *Non-local composites.* Not treated. Theorem O-M and Theorem O-II are statements about local operators.
- *Breaking.* R-B presupposes that `Spin(10)` breaks to `H` at long distance. This is EW1/VC1's question. Whether the non-family partners in `10`, `120` and `252` are heavy is CH1's.

---

## 4. `L5-U`

**Theorem U-B (R-B on `L5-U`).** Take an embedding of Lemma C-U with ratio `α:β`. Then Theorem O-I (i)-(iii) hold word for word, with "tensor-class `Spin(10)`-representation" replaced by "`U(5)`-representation" and `−1_{SO(10)}` replaced by `−1_{U(5)}`. On `L5-U`, `−1_{U(5)}` at `y` acts as fermion parity on every space carried at `y`.

*Proof.* `U(5)`-representations have weights `n ∈ Z^5` on the diagonal torus, and `−1_{U(5)}` acts on weight `n` as `(−1)^{Σn_j}`. The restriction to `H` is (W4) with the same `p` and `q`. Lemma T and the tensor powers of `C^5 ⊕ C^{5*}` give the converse, as in Theorem O-I(i). Parity: `LW1_5U_DRAFT.md` line 116, Lemma Z-U(i): "A homogeneous local operator `O` has fermion parity `(−1)^{Σ_xq_x(O)}`". Its part (ii) shows that this is the action of `−1_5` at the sites of a region. For a space carried at `y`, only `y`'s factor acts. ∎

So on `L5-U`, as on `L5-O`'s Case I, a fermion-odd family is carried exactly when `α` is even. The standard ratio is realized at one site by `c`, `ccc` and `c^5` (Proposition F).

**Theorem U-M (R-M on `L5-U`).** Let `𝒪` be invariant under `U(5)_y`, with `𝒪|_{H_y} = F_t` (15 or 16 dimensions). Put `s = 3a + 2b`. Then `𝒪`'s weights are one orbit of `(k+1, k+1, k, k, k)` (a `Λ^2(5) ⊗ det^k`), one orbit of `(k', k', k', k', k'−1)` (a `5bar ⊗ det^{k'}`), and possibly one singlet `det^{k''}`. Exactly one of these holds:
(A) `s = 0`, so `Y ∈ su(5)` and `α:β = −2:3`. The `10` holds `Q, u^c, e^c`, the `5bar` holds `d^c, L`, and the singlet (if present) is `ν^c`. The twists `k, k', k''` are free. All three multiplets are fermion odd exactly when `k` is odd, `k'` is even and `k''` is odd. Example: `ccc` (`k = −1`), `c` (`k' = 0`), `c^5` (`k'' = −1`).
(B_k), `k ∈ Z`: the flipped assignment. The `10` holds `Q, d^c, ν^c`, the `5bar` holds `u^c, L`, and the singlet `det^{k''}` is `e^c`, so 16 dimensions. Here `a = s(1+k)/3`, `b = −ks/2`, `k' = −(1 + 3k)` and `k'' = 2 + 5k`, with ratio `α:β = 2(1+k):(−3k)`. All three are fermion odd exactly when `k` is odd.

*Proof.* *Orbits.* The Weyl group of `U(5)` is `S_5`, and an orbit has `5!/∏m_i!` elements: 1, 5, 10, 20, 30, 60 or 120. A `(3,2)` weight has entries `{k+1, k, k}` in the colour slots and `{m, m ± 1}` in the doublet slots. Its smallest orbit, 10, occurs exactly for `{m, m±1} = {k, k+1}`, the orbit of `(k+1, k+1, k, k, k)`. Any other choice gives at least 20. With `dim 𝒪 ≤ 16`, the rest is a union of orbits of size 5 and 1. A size-5 orbit `(l, l, l, l, l')` puts `l'` in a colour slot. So it needs `l' = l − 1` to be a `3bar` weight (`l' = l + 1` gives a `(3,1)`, which is not in the family), and then it is `(3bar,1)_{sl−a} + (1,2)_{sl−b}`. The family needs two `(3bar,1)`. So exactly one size-5 orbit occurs, plus at most one singlet. *Hypercharges of the 10-orbit.* `(3bar,1)_{sk+2a}`, `(3,2)_{sk+a+b}`, `(1,1)_{sk+2b}`. So `t = sk + a + b`. *Case A:* the `10`'s `(3bar,1)` is `u^c`. Then `sk + 2a = −4t` gives `s(5k + 2) = 0`, so `s = 0`. The other equations hold identically at `s = 0` (`2b = 6t`, `−a = 2t`, `−b = −3t`). *Case B:* it is `d^c`. Then `sk + 2a = 2t` gives `sk + 2b = 0`, so the `10`'s singlet is `ν^c` and `e^c` must be `det^{k''}`. The `5bar` equations `sk' − a = −4t` and `sk' − b = −3t` give `t = a − b`, `sk' = −3a + 4b` and `sk'' = 6(a − b)`. Here `s ≠ 0`, since `s = 0` with `sk + 2b = 0` gives `a = b = 0`. Solving gives the stated values, all integers for every `k`. *Parity* (`U(1)_N` charge `Σn_j`): `5k + 2`, `5k' − 1`, `5k''`. ∎

[check] (4): a grid search over `a, b ∈ {−2, …, 2}` in steps of `1/6` finds case A only at `a/b = −2/3`, and case B at `(a/b, k) = (−1/3, −2), (0, −1), (∞, 0), (−4/3, 1)`, as predicted. Other `k` lie outside the grid.

**What is fixed and what is free (smuggling check).** `L5-U` fixes `U(5)` and its local operator content (Lemma Z-U). It does not fix `H`. The `su(3) ⊕ su(2)` part is unique up to conjugacy and `u ↦ ū` (Lemma C-U), so it is not a choice. The ratio `α:β` is a free choice of one rational number. Under R-B, any even `α` works. Under R-M with the standard assignment, `Y ∈ su(5)` is *derived* (case A forces `s = 0`), and the flipped cases B_k give other ratios. So neither reading fixes the embedding uniquely. "The standard `SU(5)` embedding" is a choice. Choosing it because it yields CG1's content fails test 1 (section 6). It belongs to CG1-i (P-HY, already an open input of CG1) or to the vacuum of EW1/VC1. Proposition F uses only operators that `L5-U` already has, with no new structure. On `L5-O`, the same holds: Case I(α:β) is the same free ratio, and Case II is excluded by Theorem O-II, not by choice.

`CH1_DRAFT.md` line 48 (Theorem S2) is stated for "the exact `U(1)` of `L_cube`". `LW1_5_DRAFT.md` line 428 says that on `L5-U`, "S2 applies to `U(1)_N` and says it is not hypercharge". In cases B_k, `Y` has a `U(1)_N` part (`s ≠ 0`). Whether S2 bears on such a mixture was not checked here.

---

## 5. Representation content is not chirality: what CH1 still needs

CH1(a), `TOE_ASSEMBLY.md` line 399, asks for a light spectrum that "is exactly the chiral content of CG1 ... with every doubler and every mirror gapped ..., no extra light charged state, gauge anomalies cancelling". Representation content of local operators cannot give this. Every operator comes with its adjoint: `c` with `c^†` on `L5-U`, and on `L5-O` each `Λ^k` is spanned by `γ` monomials, which are Hermitian up to a phase, so `Λ^k` is closed under the adjoint. So the operator content is always vector-like. CH1 must show that the dynamics leaves light only the family as left-handed Weyl species, with mirrors and doublers gapped (CH1-i), with a local gauged measure (CH1-ii), and with the exact group broken to `H` (EW1/VC1). R-B presupposes that breaking on both laws. **On `L5-O`**, the family's members sit in parents with non-family partners: `Q` sits in the `120`, whose other components include `c^†cc`-type operators. So CH1 must also make those partners heavy. #10014's protection and anomaly steps for the 16 do not transfer, because they are field statements about a spinor (`LW1_5O_DRAFT.md` section 2.6). `Spin(10)` itself has no perturbative gauge anomaly, and the family's `H`-content is anomaly free. **On `L5-U`**, the exact group contains the gauged `U(1)_N`. The family `5bar_{−1} + 10_{−3} + 1_{−5}` has `U(1)_N` gravitational, cubic and mixed `SU(5)^2` anomalies `(−40, −400, −5)`. That is Proposition D(iii)'s `40 − 16c` (and its partners) at the integer shift `c = 5` ([check] (5)). So CH1's "gauge anomalies cancelling" needs `U(1)_N` broken at long distance, or other light `U(1)_N`-charged fields that cancel it. Both laws leave CH1-i and CH1-ii as they were.

---

## 6. Four-test check of every reading and choice

Tests: (1) states or fixes a part's target; (2) open-ended; (3) settles a downstream question by premise; (4) adds structure its reasons do not need. Nothing below is adopted.

| Reading or choice | (1) | (2) | (3) | (4) | Result |
|---|---|---|---|---|---|
| R-B. Family read through `H`-components of local operators | pass: it reads CG1's "the Standard Model one-generation multiplet" | pass: a fixed list of six representations | conditional: it presupposes `G → H` at long distance, which is EW1/VC1's question; disclosed | pass | passes 1, 2, 4; 3 conditional |
| R-M. Family is a whole multiplet of the exact `G` | pass: it reads "equivalently the 16 of `Spin(10)`" | pass | fails if adopted for CG1: it decides by premise that breaking cannot supply the family, which is EW1/VC1's question | pass | recorded; used only to state where `L5-O` fails |
| R-F. Members created by fermion-odd operators | pass: MT1's statistics, not CG1's target | pass | pass | pass | passes |
| E-std. Embedding with ratio `2:3` (`Y ∈ su(5)`) | fails if chosen because it yields the family; it is CG1-i (P-HY) | pass | as (1) | pass | recorded, not proposed |
| E-flip. Flipped `B_k` on `L5-U` | fails as E-std | pass | as (1) | conditional: it uses `U(1)_N` in `Y` | recorded, not proposed |
| Restricting the register to end-mixed classes to get a 16 (Proposition E) | fails: chosen for the 16 | fails unless given a range | fails: puts a family into a fixed sector by premise | fails | rejected, as `LW1_5O_DRAFT.md` c13-c14 |

---

## 7. Open statements

- **CG1K-H (OPEN, EW1/VC1).** Does `Spin(10)` (on `L5-O`) or `U(5)` (on `L5-U`) break at long distance to an image `H` of `G_SM`, and with which ratio `α:β`? This decides whether R-B or R-M applies, and fixes CG1-i. On `L5-O` it must be a Case I embedding with `α` even for a fermion-odd family. On `L5-U` it must also have `α` even.
- **CG1K-loc (not pursued).** Local realization of the family for even ratios whose construction needs more than the site and its six neighbours (section 3.3, remark). No verdict uses it.
- **Inherited, unchanged.** CG1-i, CG1-ii, CH1-i, CH1-ii, LW1-5-BG, LW1-5-X.

---

## FINISH

**Proved here (pass 1, not refereed).**
- Lemma C: up to `Pin(10)` conjugacy and relabeling, embeddings of `𝔤_SM` in `so(10)` are Case I(α:β) (inside a `U(5)`, `Y = diag(α,α,α,β,β)`) and Case II (`SU(2) = Spin(3)` on three Majorana directions).
- Lemma C-U: embeddings in `u(5)` are Case I only.
- Lemma W, Lemma Z6, Lemma T: tensor-class weights in `Z^5`, parity `(−1)^{Σn_j}`, Weyl invariance; the family's members are powers `n = 1, −4, 2, −3, 6, 0` of `Q`'s central character; small tensor products.
- Theorem O-II: in Case II, `(1, −1, 0) ↦ −1 ∈ Spin(10)`, so no doublet sits in any tensor-class representation.
- Theorem O-I: in Case I, the family sits in tensor-class representations for every ratio. All members are fermion odd exactly when `α` is even, that is, exactly when `−1_{SO(10)} ∉ p(H)`.
- Proposition F: on both laws, `c` (`d^c, L`), `ccc` (`Q, u^c, e^c`) and `c^5` (`ν^c`) at one site carry one family with hypercharges `1/3, −1/2, 1/6, −2/3, 1, 0`. On `L5-O` they sit in `10`, `120`, `252`; on `L5-U` in `5bar_{−1}`, `10_{−3}`, `1_{−5}`.
- Theorem O-M: on `L5-O`, every tensor-class `Spin(10)` multiplet containing `(3,2)_y` has at least 40 components, under every embedding and register choice. The family is never a whole exact multiplet.
- Theorem U-B: on `L5-U`, the same criteria as Theorem O-I.
- Theorem U-M: on `L5-U`, the family is a whole `U(5)` multiplet sum exactly in case A (`Y ∈ su(5)`, forced) or the flipped cases `B_k`.

**Counterexamples.**
- To "on `L5-O`, no local gauge-covariant operator carries the representation content of one family" (the kill test's hypothesis): Proposition F under the standard embedding.
- To "every embedding of `G_SM` in `Spin(10)` gives the family in some representation": Case II (Theorem O-II).
- To "any hypercharge ratio inside `U(5)` gives a fermion-odd family": `Y ∝ B − L` (`α:β = 1:0`, Theorem O-I(iii)).

**Open, by name.** CG1K-H (EW1/VC1). CG1K-loc (not pursued). Inherited: CG1-i, CG1-ii, CH1-i, CH1-ii, LW1-5-BG, LW1-5-X.

**What this means for keeping both laws live.**
- `L5-O` does **not** fail CG1 at a named step under the local-field reading R-B. The kill test as posed, "under some embedding", is answered yes by Proposition F. The family needs Case I with `α` even. Case II embeddings, including `LW1_5O_DRAFT.md`'s `Spin(3)` example, are excluded.
- `L5-O` **fails at a named step, Theorem O-M, under R-M**: the family is never a whole `Spin(10)` multiplet of the law's operators. R-M applies if `Spin(10)` is unbroken where the family is light. R-M fails test 3 as a reading of CG1 today, so this is a conditional failure, tied to CG1K-H.
- `L5-U` passes both readings, with the same one-site operators.
- The test does not separate the laws under R-B. It separates them under R-M. Both laws need breaking to `H` for the Standard Model gauge content anyway (GA2, EW1). So the reading that matches the rest of the skeleton is R-B, and under it both laws stay live. The difference that remains is for CH1: non-family partners and the lost 16-protection on `L5-O`, and an anomalous gauged `U(1)_N` on `L5-U`.
- This draft does not choose between `L5-O` and `L5-U`.

**Inputs from outside the working set.** The two laws of `LW1_5_DRAFT.md` section 8.1, and its Theorem G, Lemma Q4, Lemma Z, Theorem U. From `LW1_5O_DRAFT.md`: Lemma K0, Lemma F, Theorem K, Proposition E, Theorem P, Proposition T. From `LW1_5U_DRAFT.md`: Lemma Z-U, Proposition D. Standard mathematics, rebuilt in the text: characters of a torus, Weyl-group invariance of weights by conjugation, orbit counts, Schur's lemma and commutants of absolutely irreducible modules, simple ideals of `so(4)`, small tensor products of `su(3)` and `su(2)`, the wedge pairing. Standard mathematics cited, not rebuilt: the dimension formula for `su(3)` irreducibles ([check] (6)); complete reducibility; inner automorphisms of `su(2)`. Literature context, credited from memory and never load-bearing: the Georgi-Glashow `SU(5)` and the `SO(10)` assignment of one family; flipped `SU(5)` (Barr; Derendinger-Kim-Nanopoulos); the Pati-Salam decomposition, used only to name `B − L` and `T_{3R}` in a remark.
