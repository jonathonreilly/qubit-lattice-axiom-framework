lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CH1-5U-i on `L5-U`, pass 1: the anomalies of the mirror of the twisted family, and three new attacks on existence

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 of the open input CH1-5U-i of `CH1_5_DRAFT.md` section 5.1, under the method of open PR #10138 (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks one tiny scratch computation (`/tmp/toe-ch15u/check_ch15u.py`, output `out.txt`; exact integer and half-integer arithmetic, 0.05 s, 15 MB, run after `memory_pressure` showed 66 percent free). A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` (sparse) | `2d0adc0c0` |

No other branch was read. Files read at that commit, by line. This folder: `CH1_5_DRAFT.md` lines 1-311 (all; Theorem S2-5 at 97-104, Lemma C2-5 at 120-124, Lemma K2-5 at 136-141, Lemma V at 151-153, Lemma O-A at 159-161, Theorem U-A at 173-181, Lemma U-T at 185-190, AM-5 at 205-207, section 5.1 at 234-250); `CG1_KILL_DRAFT.md` lines 1-252 (all; Theorem U-M at 182-186, section 5 at 198); `LW1_5U_DRAFT.md` lines 1-309 (all; Lemma E at 68-75, Lemma Z-U at 115-122, Proposition D at 206-212, the mod-16 remark at 220); `VC1_5_DRAFT.md` lines 1-352 (all; Theorems U1-U4 at 222, 228, 240, 259); `CH1_DRAFT.md` lines 1-453 (all; Theorems F1-F4 at 139-206, Lemma AM at 301-303, literature at 102-108, section 8 at 394, section 9 at 398); `TOE_ASSEMBLY.md` lines 395-424 (CH1, CG1); `Y2W_DRAFT.md` lines 1-40 and 190-208 (format; Theorem W2 at 191); `GA2_Y2_DRAFT.md` lines 26-34 (by grep for "Wilson").

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The law `L5-U` and CH1-5U-i are read plainly. One word needs a meaning: "free of all `U(5)` anomalies". Section 1.3 fixes the structure group from the law's own Lemma Z-U and proves every claim for the larger structure, so no reading is chosen. Section 6 puts each new definition through the four tests. Nothing is adopted.

**Working set used, by name.** PS-5 (five modes per site) and PS-6 with PS-6r (finite link registers), only through the law `L5-U` of `LW1_5_DRAFT.md` section 8.1 as restated in `LW1_5U_DRAFT.md` section 1.1. PS-8, only as the kind of gate that CH1-5U-i (a) allows. PS-1c, only through CH1-5U-i's covariance clause. Results used, cited by name and quoted at the point of use: from `LW1_5U_DRAFT.md`, Lemma E and Lemma Z-U; from `CH1_5_DRAFT.md`, Theorem S2-5, Lemma C2-5, Lemma K2-5, Lemma V, Lemma O-A, Theorem U-A, Lemma U-T and Attack 1 of section 5.1; from `CG1_KILL_DRAFT.md`, Theorem U-M; from `Y2W_DRAFT.md`, Theorem W2; from `CH1_DRAFT.md`, the record of #10049. PS-2, PS-3, PS-4, PS-7, PS-9 to PS-11 are not used.

**Inputs from outside the working set.** *Standard mathematics, rebuilt in the text:* weights of torus representations, the trace identity for exterior powers, Schur's lemma for unitary representations, characters of finite abelian groups, integer linear algebra modulo `n`, associated bundles. *Standard mathematics cited, not rebuilt:* complete reducibility of compact-group representations; the maximal torus theorem; the Atiyah-Singer count of instanton zero modes; the Atiyah-Hirzebruch spectral sequence with the groups `Ω^{Spin^c}_{q}` and `Ω^{SO}_{q}` for `q ≤ 5` and the homology of `BSU(5)` and `BU(5)` in degrees `≤ 5`. *Physics framework cited, never load-bearing:* the anomaly of 4d Weyl fermions as an η-invariant on 5-manifolds, a bordism invariant once the perturbative anomaly vanishes (Dai and Freed 1994; Witten 2016; Freed and Hopkins 2016; Witten and Yonekura 2019); Witten's `SU(2)` anomaly (1982); the mod-16 anomaly of `Spin ×_{Z_2} Z_4` (Tachikawa and Yonekura 2018; García-Etxebarria and Montero 2018; Hsieh 2018); the "new `SU(2)` anomaly" (Wang, Wen and Witten 2018). *Literature context, credited from memory and never load-bearing:* Wang and Wen on symmetric mass generation of the `Spin(10)` 16 and a non-perturbative definition of the Standard Models (2018-2020); Razamat and Tong, "Gapped chiral fermions" (PRX 2021); Tong, "Comments on symmetric mass generation in 2d and 4d" (2021); Kikukawa on the gauge-invariant overlap measure for the 16 of `SO(10)` and on why mirror decoupling fails in 2d abelian models (2017-2019); Lüscher (1999); Golterman and Shamir (arXiv:2505.20436, as quoted in `CH1_DRAFT.md`); Eichten and Preskill (1986).

---

## 0. The question, quoted

`CH1_5_DRAFT.md` lines 236-239, **Lemma CH1-5U-i (open).** "There exist (a) an update `U` of `L5-U` form (the tick of `LW1_5_DRAFT.md` section 8.1 with rishon registers of some `m`, plus finitely many layers of gauge-invariant site or cell gates, the kind PS-8 names), covariant under `G_U`, and (b) a state `ω`, stationary under `U` and invariant under `G_U` and gauge transformations, such that hypothesis IR holds with light left-handed Weyl fields that are exactly `10 ⊕ 5bar ⊕ 1` of `SU(5)`, with `U(1)_N` charges `u(1, −3, 5)`, `u = 5k + 2`, `k` odd (case A, `Y ∈ su(5)`), or the flipped `B_k` assignment; with `U(5)` unbroken at long distance and every other fermion-odd excitation gapped."

Line 241: "The mirror of this set is anomaly free, so anomalies do not forbid its symmetric gapping." Line 244, *Not on file*: "A global-anomaly analysis for this content." Lines 246-248 give three attacks: free, PS-8 on the elementary content, one-site composites. Line 250: "False: a theorem that every light fermion of an invariant stationary state of an `L5-U` law has `|U(1)_N| ≤ 5`, or is carried at one site ... The next test to run, guidance only: exact diagonalisation of a small 1+1D five-mode chain with `U(5)`-invariant on-site interactions, to see which fermion-odd site composites are lightest."

`TOE_ASSEMBLY.md` line 399, CH1(a), asks for the mirrors "gapped at scale `~ 1/a` [**open input CH1-i**: symmetric mass generation for the mirrors without releasing light partners], no extra light charged state, gauge anomalies cancelling, the gauge field kept massless".

**The lane's target.** Decide exactly which `U(5)` anomalies, perturbative and global, the mirror of `R_u := 10_u ⊕ 5bar_{−3u} ⊕ 1_{5u}` carries (`u` odd, `u ≡ 2 mod 5`, `|u| ≥ 3`). A nonzero one refutes CH1-5U-i as stated. Zero removes the obstruction. Then attack existence with attacks that differ from the three on file.

## 0.1 Outcome in one paragraph

**The structure.** Every family on the line is one fixed representation pulled back along a covering. Let `Ũ(5) = {(g, z) ∈ U(5) × U(1) : z^2 = det g}`, the group that `Spin(10)` induces on `U(5)`, and `S = Λ^{even}(C^5) ⊗ z^{−1}`, the restriction of the 16. Then `R_u = φ_u^*S` for the surjection `φ_u(g) = (g·det(g)^{−(2u+1)/5}, det(g)^{−u})`, whose kernel is the scalar group `μ_{|u|}` and which sends `−1_5` to the element that acts as `−1` on `S` (Theorem Φ). The homomorphisms `U(5) → Ũ(5)` that fix `SU(5)` are exactly these, so the line is exactly the set of such pullbacks, and `u = ±1` would need an isomorphism that does not exist. **Anomalies.** Fermion parity is the gauge rotation `−1_5` (Lemma Z-U), so the structure is `Spin ×_{Z_2} U(5)`. Every anomaly of `R_u` is the pullback of the corresponding anomaly of `S` (Lemma N). Proved: every perturbative anomaly vanishes, `Tr_{R_u}X^3 = Tr_{R_u}X = 0` on all of `u(5)` (Theorem A1); Witten's type vanishes for every `SU(2) → U(5)`, since `R_u` has `4n(5)` instanton zero modes (Theorem A2); the mod-16 type vanishes for every `Z_4 ⊂ U(5)` whose square is fermion parity, with index `ν ∈ {0, ±16}` (Theorem A3); the new-`SU(2)` type has no structure map into `Spin ×_{Z_2} U(5)` (Lemma A4). With the cited bordism fact `Ω_5^{Spin ×_{Z_2} U(5)} = 0`, every global anomaly vanishes, so on this structure the perturbative conditions are the whole anomaly condition (Proposition A5). The mirror carries the negatives. **So the 't Hooft-anomaly obstruction to CH1-5U-i is absent.** No anomaly refutes it. **Existence.** Three new attacks fail. *Attack 4* imports a `Spin(10)`-symmetric gapping of the mirror 16 through `φ_u` (Wang-Wen; Tong; Razamat-Tong). It fails at its first step: no member of `R_u ⊕ \bar R_u` has `U(1)_N` charge `±1` (Lemma Q1), and every quasi-free point of the law has only charge-`±1` light fields, so the law has no weakly coupled point at which the imported flow could start. *Attack 5* pulls back an overlap measure for the 16 (Lüscher; Kikukawa). It fails at the link variables: the overlap needs c-number `U(5)` links, and an `L5-U` link operator `U^{jk}` squares to zero (Theorem W2 of `Y2W_DRAFT.md`). *Attack 6* tries to refute CH1-5U-i through a mirror symmetry that no interaction can break (in the spirit of Kikukawa's 2d argument) or through a Nielsen-Ninomiya theorem for the elementary propagator (Golterman-Shamir). It fails twice, at exact steps: two `U(5)`-invariant mirror quartics leave no symmetry beyond the gauged `U(1)_N` (Lemma K), and the elementary propagator couples only to charge `±1` (Lemma Q1). **What decides it.** The smallest statement that could refute CH1-5U-i outright, its anomaly, is decided: absent. The remaining question is dynamical. CH1-5U-i implies **CH1-5U-q**: a light fermion-odd excitation of `U(1)_N` charge `|q| ≥ 3` in an invariant stationary state of an `L5-U` law. Its negation refutes CH1-5U-i. Attack 4 stops exactly there. **No named failing step for `L5-U`.** CH1-5U-i stays open, with six failed attacks on file and its anomaly question decided.

---

## 1. Setting

### 1.1 The family and its mirror

The law is `L5-U` (`LW1_5U_DRAFT.md` section 1.1). `U(1)_N` is the centre of `U(5)`, and a matter operator's `U(1)_N` charge is the change of matter number it makes (`CH1_5_DRAFT.md` section 1).

Fix `u` on the line: `u` odd, `u ≡ 2 mod 5`, so `|u| ≥ 3` (`CH1_5_DRAFT.md` Theorem S2-5(iv)). Put `k = (u − 2)/5` (odd), `k' = −3k − 1` (even). As in `CG1_KILL_DRAFT.md` Theorem U-M (line 182), the **family** `R_u` is the `U(5)`-representation with weights
- `10_u`: the orbit of `(k+1, k+1, k, k, k)`, that is `Λ^2(C^5) ⊗ det^k`;
- `5bar_{−3u}`: the orbit of `(k', k', k', k', k' − 1)`, that is `5bar ⊗ det^{k'}`;
- `1_{5u}`: the weight `(u, u, u, u, u)`, that is `det^u`.

The `U(1)_N` charge of a weight `n` is `Σ_jn_j`: `5k + 2 = u`, `5k' − 1 = −3u`, `5u`. These are `CH1_5_DRAFT.md` line 100's line, "`(a, b, c) = u(1, −3, 5)`". The flipped assignment `B_k` has the same `U(5)`-representation. Line 100: "In case `B_k` it always holds, with `U(1)_N = uX'`." Only the embedding of the Standard Model group differs, and nothing below uses it.

The light family of CH1-5U-i is `R_u` as left-handed Weyl fields. Its **mirror** is the right-handed copy, which is the left-handed set `\bar R_u = R_u^* = 10bar_{−u} ⊕ 5_{3u} ⊕ 1_{−5u}`. Every anomaly is additive and changes sign under `R ↦ R^*`. So the mirror's anomalies are the negatives of the family's, and each vanishes exactly when the family's does. Below, statements are made for `R_u`.

### 1.2 The structure group

`LW1_5U_DRAFT.md` line 117, Lemma Z-U(ii): "The gauge transformation `−1_5 ∈ U(5)` at every site of a finite set `Λ` containing the sites and link ends of `O` acts on `O` as its fermion parity." So fermion parity is the gauge rotation `−1_5`. On `R_u` the element `−1_5` acts on weight `n` as `(−1)^{Σn_j}`, and every charge `u, −3u, 5u` is odd. So `−1_5` acts on `R_u` as `−1`.

For a spin group `Spin(d)` put
\[
K=\mathrm{Spin}(d)\times_{Z_2}U(5):=\big(\mathrm{Spin}(d)\times U(5)\big)\big/\langle(-1,-1_5)\rangle .
\]
A Weyl field in `R_u` is a representation of `K`: the pair `(−1, −1_5)` acts as `(−1)(−1) = 1`. The product structure maps to it, `Spin(d) × U(5) → K`, `(s, g) ↦ [s, g]`. By Lemma N below, an anomaly that vanishes for `K` vanishes for `Spin(d) × U(5)`. So every claim is proved for `K`, which covers both. No reading is chosen.

### 1.3 Words

The *perturbative anomaly* of a `K`-representation `R` is the degree-6 anomaly polynomial. For a compact connected group it vanishes exactly when `Tr_R(X^3) = 0` and `Tr_R(X) = 0` for all `X` in the Lie algebra (the cubic gauge anomaly and the mixed gravitational one). The *anomaly* of `R` is the anomaly theory of the Weyl field: the η-invariant of the twisted Dirac operator on closed 5-manifolds with `K`-structure (cited framework, head). A *type* of global anomaly is the anomaly pulled back along a structure map `f: K' → K` from a smaller structure: `Spin × SU(2)` (Witten's type), `Spin ×_{Z_2} Z_4` (the mod-16 type), `Spin ×_{Z_2} SU(2)` (the new-`SU(2)` type).

---

## 2. The line is one representation pulled back

**Definition.** `Ũ(5) = {(g, z) ∈ U(5) × U(1) : z^2 = det g}`, a closed subgroup of `U(5) × U(1)`. Write `−1̃ = (1_5, −1)`. Let `S = (Λ^0 ⊕ Λ^2 ⊕ Λ^4)(C^5)`, with `(g, z)` acting as `z^{−1}Γ(g)`, where `Γ(g)` is the action on the exterior algebra (`LW1_5U_DRAFT.md` section 1.1). `−1̃` acts on `S` as `−1`.

*Naming only (standard; cited, not used in any proof).* `Ũ(5)` is the preimage in `Spin(10)` of `U(5) ⊂ SO(10)`, `−1̃` is the element `−1 ∈ Spin(10)`, and `S` is the restriction of a half-spin representation, the 16.

**Lemma Ũ.** `Ũ(5)` is connected. The map `σ: SU(5) × U(1) → Ũ(5)`, `σ(A, w) = (w^2A, w^5)`, is a surjective homomorphism with kernel `{(w^{−2}1_5, w) : w^5 = 1}`. The centre of `Ũ(5)` contains `C = {(w^21_5, w^5) : w ∈ U(1)}`, and `w ↦ (w^21_5, w^5)` is an isomorphism `U(1) → C`.

*Proof.* `det(w^2A) = w^{10} = (w^5)^2`, so `σ` lands in `Ũ(5)`. It is a homomorphism, because scalars are central. *Onto.* Given `(g, z)`, pick `λ` with `λ^5 = det g` and put `A = λ^{−1}g ∈ SU(5)`. Pick `w` with `w^2 = λ`. Then `(w^5)^2 = λ^5 = z^2`, so `w^5 = ±z`; if `w^5 = −z`, replace `w` by `−w`, which keeps `w^2` and changes the sign of `w^5`. Then `σ(A, w) = (g, z)`. `SU(5) × U(1)` is connected, so `Ũ(5)` is. *Kernel.* `w^5 = 1` and `w^2A = 1` give `A = w^{−2}1_5`, and conversely. *The circle `C`.* `(w^2, w^5) = (1, 1)` forces `w = w^{5−2·2} = 1`. ∎

**Theorem Φ (the line is the spinor pulled back).** Let `a, b` be integers with `2b = 1 + 5a`. Put `ψ_{a,b}(g) = (g·det(g)^a, det(g)^b)`.
(i) `ψ_{a,b}` is a homomorphism `U(5) → Ũ(5)` with `ψ_{a,b}(A) = (A, 1)` for `A ∈ SU(5)`. Every continuous homomorphism `ψ: U(5) → Ũ(5)` with `ψ(A) = (A, 1)` on `SU(5)` is some `ψ_{a,b}`. In it `a` is odd and `b ≡ 3 mod 5`.
(ii) `ψ_{a,b}` is surjective. Its kernel is the scalar group `μ_{|b|} = {λ1_5 : λ^b = 1}`.
(iii) `ψ_{a,b}^*S ≅ 10_{−b} ⊕ 5bar_{3b} ⊕ 1_{−5b} = R_{−b}`.
(iv) `ψ_{a,b}(−1_5) = (1_5, (−1)^b)`. It is `−1̃` exactly when `b` is odd.

So for `u` on the line put `φ_u = ψ_{a,b}` with `b = −u` and `a = −(2u + 1)/5`. Then `R_u = φ_u^*S`, `ker φ_u = μ_{|u|}`, and `φ_u(−1_5) = −1̃`.

*Proof.* (i) `g ↦ g·det(g)^a` is a homomorphism, since `det` is a character and scalars are central. `det(g·det(g)^a) = det(g)^{1+5a} = (det(g)^b)^2`, so `ψ_{a,b}` lands in `Ũ(5)`. On `SU(5)`, `det = 1`. *Converse.* Let `λ ∈ U(1)`. `ψ(λ1_5) = (h, z)` commutes with every `(A, 1)`, so `h` commutes with `SU(5)` on `C^5`. `C^5` is irreducible under `SU(5)` (Lemma E (E1) with `k = 1`), so `h = μ1_5` by Schur's lemma, and `z^2 = μ^5`. Pick `w` with `w^2 = μ`. Then `(w^5)^2 = μ^5 = z^2`, so `w^5 = ±z`, and replacing `w` by `−w` if needed gives `(μ1_5, z) = (w^21_5, w^5)`. So `(μ1_5, z) ∈ C`, and `λ ↦ ψ(λ1_5)` is a continuous homomorphism `U(1) → C ≅ U(1)`. It is `λ ↦ λ^c` for an integer `c` (characters of the circle; standard). So `ψ(λ1_5) = (λ^{2c}1_5, λ^{5c})`. On `ζ ∈ μ_5`, `ζ1_5 ∈ SU(5)`, so `(ζ^{2c}1_5, ζ^{5c}) = (ζ1_5, 1)`. Hence `2c ≡ 1 mod 5`. Write `g = λA` with `λ^5 = det g`, `A ∈ SU(5)`. Then `ψ(g) = (λ^{2c}A, λ^{5c})`. Put `b = c` and `a = (2c − 1)/5`. Then `g·det(g)^a = λ^{1+5a}A = λ^{2c}A` and `det(g)^b = λ^{5c}`, so `ψ = ψ_{a,b}`. `1 + 5a = 2b` is even, so `a` is odd; `2b ≡ 1 mod 5` gives `b ≡ 3`.
(ii) *Kernel.* `g·det(g)^a = 1` makes `g = μ1_5` scalar with `μ^{1+5a} = μ^{2b} = 1`. Then `det(g)^b = μ^{5b}`. So the kernel is `{μ : μ^{2b} = μ^{5b} = 1}`, and `gcd(2b, 5b) = |b|`. *Onto.* The kernel is finite, so the differential is injective. Both groups have dimension 25 (`Ũ(5) → U(5)`, `(g, z) ↦ g`, has fibres `{±z}`). So the differential is an isomorphism, the image is open, and it is closed because `U(5)` is compact. `Ũ(5)` is connected (Lemma Ũ), so the image is everything.
(iii) Take `g = diag(t_1, …, t_5)` and a basis vector `e_T ∈ Λ^r`, `|T| = r` even. `ψ(g)` acts on it as `det(g)^{−b}∏_{i∈T}(t_i det(g)^a)`. So its weight is `1_T + (ar − b)(1, 1, 1, 1, 1)`. For `r = 2` this is `Λ^2 ⊗ det^{2a−b}`, of `SU(5)` type 10 and charge `2 + 5(2a − b) = 2 + 2(2b − 1) − 5b = −b`. For `r = 4` it is `Λ^4 ⊗ det^{4a−b}`. The wedge pairing `Λ^4 ⊗ Λ^1 → Λ^5` is equivariant and nondegenerate, so `Λ^4 ≅ 5bar ⊗ det`. The type is `5bar` and the charge is `4 + 5(4a − b) = 4 + 4(2b − 1) − 5b = 3b`. For `r = 0` it is `det^{−b}`, of charge `−5b`. Each piece is irreducible (Lemma E (E1)). A `U(5)`-irreducible is fixed up to isomorphism by its `SU(5)` type and its charge: an `SU(5)` intertwiner between two copies is unique up to scale (Schur) and commutes with the scalars, which act by the same character. With `u = −b` the three pieces are `10_u`, `5bar_{−3u}`, `1_{5u}`. [check] (1): the 16 weights of `φ_u^*S` equal those of `R_u` for the eight line values with `|u| ≤ 40`.
(iv) `ψ(−1_5) = ((−1)^{1+5a}1_5, (−1)^{5b}) = (1_5, (−1)^b)`, since `a` is odd. ∎

**Corollary Φ.1.**
(a) The families of the form `ψ^*S`, with `ψ` as in (i) and `ψ(−1_5) = −1̃`, are exactly the `R_u` with `u ≡ 2 mod 5` and `u` odd. This is `CH1_5_DRAFT.md` Theorem S2-5(iv) ("`u` is odd and `u ≡ 2 mod 5`") derived from the spinor. Composing with complex conjugation `g ↦ \bar g` gives `u ↦ −u`, the conjugate embedding's `u ≡ −2`.
(b) No `ψ` of (i) is an isomorphism, since `b ≡ 3 mod 5` forbids `|b| = 1`. That is the precise form of `CH1_5_DRAFT.md` line 106, "The `Spin(10)` spinor normalisation `u = 1` needs `det^{1/2}`": the value `u = 1` would need an isomorphism `U(5) ≅ Ũ(5)` that fixes `SU(5)`.
(c) The scalars `λ1_5` with `λ^u = 1` act trivially on `R_u`.

**Lemma Q1 (no family member has charge `±1`).** Every member of `R_u ⊕ \bar R_u` has `U(1)_N` charge in `{±u, ±3u, ±5u}`, so `|q| ≥ 3`. In particular the elementary fermion `c_{x,j}` (charge `−1`) and every operator of charge `±1` lie in a different charge sector from every family member.

*Proof.* `|u| ≥ 3` (Theorem S2-5(iv)). ∎

---

## 3. The anomalies of the mirror

### 3.1 Naturality

**Lemma N (anomalies pull back).** Let `f: K' → K` be a continuous homomorphism of structure groups that commutes with their maps to `SO(d)`. Let `R` be a `K`-representation. For a manifold `M` with `K'`-structure `P'`, put `P = P' ×_f K`. Then the twisted spinor bundles `P' ×_{K'} f^*R` and `P ×_K R` are canonically isomorphic, with their connections. So the twisted Dirac operators agree, and so do every quantity built from them: the anomaly polynomial, the index, the η-invariant. In particular, if the anomaly of `R` vanishes on `K`-manifolds, the anomaly of `f^*R` vanishes on `K'`-manifolds.

*Proof.* The map `[p', v] ↦ [[p', 1], v]` is well defined: `(p'k', v)` and `(p', f(k')v)` both go to `[[p', f(k')], v] = [[p', 1], f(k')v]`. On each fibre it is a linear bijection between copies of the space of `R`. A connection on `P'` pushes forward to `P`, and the map intertwines the induced covariant derivatives and the Clifford actions, since both come from the same frame bundle. ∎

Two structure maps are used. (1) `Spin(d) × U(5) → K`, `(s, g) ↦ [s, g]` (section 1.2). (2) `F_u: K → Spin(d) ×_{Z_2} Ũ(5) := (Spin(d) × Ũ(5))/⟨(−1, −1̃)⟩`, `[s, g] ↦ [s, φ_u(g)]`. It is well defined because `φ_u(−1_5) = −1̃` (Theorem Φ(iv)). By Theorem Φ(iii), `F_u^*S = R_u` as `K`-representations. So **every anomaly of `R_u` is the pullback along `F_u` of the corresponding anomaly of `S`**, for every `u` on the line.

### 3.2 Perturbative anomalies

**Theorem A1.** For every `X ∈ u(5)`, `Tr_{R_u}(X^3) = 0` and `Tr_{R_u}(X) = 0`. So every perturbative anomaly of `R_u` and of `\bar R_u` vanishes: `SU(5)^3`, `U(1)_N SU(5)^2`, `U(1)_N^2 SU(5)`, `U(1)_N^3` and `U(1)_N`-gravitational.

*First proof (through Φ).* Both sides are invariant under conjugation, and every `X ∈ u(5)` is unitarily diagonalizable (spectral theorem). So take `X = i·diag(x_1, …, x_5)`. Its image `dφ_u(X)` is the pair `(X', t)` with `t = Tr X'/2`, from `z^2 = det g`. On `e_T ⊗ z^{−1}` it acts as `i(Σ_{l∈T}x'_l − (1/2)Σ_lx'_l) = (i/2)Σ_lε_lx'_l`, with `ε_l = +1` for `l ∈ T` and `−1` otherwise. `|T|` is even exactly when the number of `+1`'s is even. Let `E ⊂ {±1}^5` be that set. A cubic monomial in `x'` has a variable `x'_p` of odd degree and involves at most three of the five variables; pick `m` outside them. Flipping `ε_p` and `ε_m` maps `E` onto itself and negates the monomial's coefficient `Σ_{ε∈E}∏ε^{e}`. So every cubic coefficient is zero, and `Σ_{ε∈E}(ε·x')^3 = 0`. The linear sum vanishes the same way. Hence `Tr_S(Y^3) = Tr_S(Y) = 0` for every `Y` in the Lie algebra of `Ũ(5)`, and `Tr_{R_u}(X^n) = Tr_S(dφ_u(X)^n)` finishes. This is `CH1_5_DRAFT.md` Lemma O-A's sign-flip argument (line 161), applied to `Ũ(5)`.
*Second proof (direct).* `CH1_5_DRAFT.md` line 174: "`SU(5)^3 = A(10) + A(5bar) = 1 − 1 = 0`". Line 177: "All three `U(1)_N` anomalies vanish exactly when `(a, b, c) = u(1, −3, 5)`". The remaining term, `U(1)_N^2SU(5)`, is `Σ q_i^2 Tr_{R_i}(A)` for `A ∈ su(5)`, and `Tr_{R_i}(A) = 0`. `X = A + iθ1_5` acts on the piece `R_i` of charge `q_i` as `A_{R_i} + iθq_i`, and expanding the cube gives exactly these four terms. ∎

[check] (2): the cubic and linear traces of the 16 weights vanish at 30 random integer points of `R^5`, for each of the eight line values with `|u| ≤ 40`.

### 3.3 Witten's type

For a representation `W` of `SU(2)` put `n(W) = 2Tr_W(J_3^2)`, where `J_3` has eigenvalues `±1/2` on the doublet. On spin `j`, `n = (2/3)j(j + 1)(2j + 1)`, the number of zero modes of the Weyl operator in one instanton (Atiyah-Singer; cited). Witten's anomaly of a `Spin × SU(2)` Weyl content `W` is `n(W) mod 2` (Witten 1982; cited).

**Theorem A2.** For every continuous homomorphism `σ: SU(2) → U(5)`, `n(σ^*R_u) = 4n(σ^*5)`, an integer divisible by 4. The map `(s, h) ↦ [s, σ(h)]` is a structure map `Spin × SU(2) → K`, and it pulls `R_u` back to `σ^*R_u`. So the Witten-type anomaly of `R_u` and of `\bar R_u` vanishes for every `SU(2)` in `U(5)`.

*Proof.* `det∘σ` is a continuous character of `SU(2)`. Its differential is `Tr∘dσ`, which vanishes on `[su(2), su(2)] = su(2)`, and `SU(2)` is connected. So `σ` lands in `SU(5)`, and `Y = dσ(J_3)` is traceless, with eigenvalues `y_1, …, y_5`, `Σy_l = 0`. On `10_u = Λ^2 ⊗ det^k` the eigenvalues are `y_i + y_j`, and `Σ_{i<j}(y_i + y_j)^2 = (5 − 2)Σy_l^2 + (Σy_l)^2 = 3Σy_l^2`. On `5bar ⊗ det^{k'}` they are `−y_l`, with sum of squares `Σy_l^2`. On the singlet the eigenvalue is `0`. So `Tr_{R_u}(Y^2) = 4Tr_5(Y^2)`. `σ^*5` is a sum of spins `j` with `Σ(2j + 1) = 5`, and `n(j) ∈ {1, 4, 10, 20}` for `j ∈ {1/2, 1, 3/2, 2}`, so `n(σ^*5)` is an integer. ∎

[check] (4) and (8): `Tr_{R_u}(Y^2) = 4Tr_5(Y^2)` at random traceless integer `Y`; for the seven ways to split the 5 into `SU(2)` blocks, `n(5) ∈ {20, 10, 5, 4, 2, 1, 0}` and `n(R_u) = 4n(5)`. For the weak `SU(2)` on modes 4 and 5, `n(5) = 1` and `R_u` has four doublets, as in `CH1_5_DRAFT.md` line 116 ("There are four doublets").

### 3.4 The mod-16 type

Let `g ∈ U(5)` with `g^2 = −1_5`. Then `⟨g⟩ ≅ Z_4`, its square is fermion parity (section 1.2), and `[s, g^j] ↦ [s, g^j]` is a structure map `Spin ×_{Z_2} Z_4 → K`. On a Weyl content on which `g` acts with eigenvalues `±i`, put `ν(g) = #(+i) − #(−i)`, counted with multiplicity. The anomaly of `Spin ×_{Z_2} Z_4` is `ν mod 16` (Tachikawa-Yonekura; García-Etxebarria-Montero; Hsieh; cited).

**Theorem A3.** For every `g ∈ U(5)` with `g^2 = −1_5`, `ν(g) ∈ {16, 0, −16}` on `R_u`. So every mod-16-type anomaly of `R_u` and of `\bar R_u` vanishes.

*Proof.* `g` is unitary with `g^2 = −1`, so it is conjugate to `i·h_T` with `h_T = diag(s_1, …, s_5)`, `s_l = −1` for `l ∈ T` and `+1` otherwise; put `r = |T|`. `ν` is invariant under conjugation. On a weight `n`, `i·h_T` acts as `i^{Σn_l}∏_ls_l^{n_l} = i^q(−1)^{n_T}`, with `q` the charge and `n_T = Σ_{l∈T}n_l`. The charges `u, −3u, 5u` are all `≡ u mod 4`, because `−3 ≡ 5 ≡ 1 mod 4`. So the eigenvalue is `ε·i·(−1)^{n_T}` with `ε = +1` if `u ≡ 1 mod 4` and `−1` if `u ≡ 3 mod 4`. Hence `ν = ε·χ_{R_u}(h_T)`, with `χ` the character. With `k` odd, `k'` even and `u` odd,
\[
\chi_{R_u}(h_T)=(-1)^{r}e_2(s)+e_1(s)+(-1)^{r},\qquad e_1=5-2r,\quad e_2=\tfrac12\big(e_1^2-5\big).
\]
Put `t = 5 − 2r`. Then `χ = (−1)^r(t^2 − 3)/2 + t`, which is `16, 0, 0, 0, 0, −16` for `r = 0, …, 5`. ∎

[check] (3): the characters `16, 0, 0, 0, 0, −16` from the weights, at `u = −33, −23, −13`.

*Remark A3.1.* `r = 0` is the centre element `i·1_5`, which acts on `R_u` as the uniform scalar `i^u`. `LW1_5U_DRAFT.md` line 220 found the mod-16 criterion of #10014 inapplicable to `S_+` under genuine `U(5)`: "It is not uniform, so the criterion as written does not apply." On the line it applies, and gives `ν = ±16`. Without the singlet, `ν(i·1_5) = ±15`: the 15-member family is mod-16 anomalous, on top of `CH1_5_DRAFT.md` Theorem U-A(vi).

### 3.5 The new-`SU(2)` type

**Lemma A4.** No continuous homomorphism `σ: SU(2) → U(5)` has `σ(−1) = −1_5`. So no structure map `Spin ×_{Z_2} SU(2) → K`, `[s, h] ↦ [s, σ(h)]`, exists, and the new-`SU(2)` type of Wang, Wen and Witten has nothing to pull back.

*Proof.* `σ` lands in `SU(5)` (proof of Theorem A2), and `det(−1_5) = −1`. ∎

### 3.6 All global types

**Proposition A5 (rests on cited inputs; not used in sections 2, 4, 5).**
(i) `K ≅ (Spin^c(d) × SU(5))/μ_5`, with `Spin^c(d) = (Spin(d) × U(1))/⟨(−1, −1)⟩` and `μ_5` embedded as `(ζ^{−1} ∈ U(1), ζ1_5)`.
(ii) *Cited:* `Ω_5^K = 0`.
(iii) *Cited framework:* when the perturbative anomaly vanishes, the anomaly of a `K`-content is a homomorphism `Ω_5^K → U(1)`.
(iv) Granted (ii) and (iii), every anomaly of `R_u` and of `\bar R_u` on `K`-manifolds vanishes. On `K`, the perturbative conditions are then the whole anomaly condition. By `CH1_5_DRAFT.md` Theorem U-A(iv), a one-family `U(5)` content is anomaly free exactly on the line.

*Proof of (i).* Write `U(5) = (SU(5) × U(1))/⟨(ζ1_5, ζ^{−1})⟩` by `(A, λ) ↦ λA`; then `−1_5` is the image of `(1_5, −1)`. So `K = (Spin × SU(5) × U(1))/⟨(1, ζ1_5, ζ^{−1}), (−1, 1_5, −1)⟩`. Divide first by the second generator, then by the image of the first. ∎

*Sketch of (ii), cited, not rebuilt.* At the prime 2, dividing by the odd-order `μ_5` does not change bordism, so it is `Ω_5^{Spin^c}(BSU(5))`. In the Atiyah-Hirzebruch spectral sequence every term on the line `p + q = 5` is zero: `Ω^{Spin^c}_q = Z, 0, Z, 0, Z^2, 0` and `H_p(BSU(5); Z) = Z, 0, 0, 0, Z, 0` for `p, q = 0, …, 5`. After localizing at an odd prime, `K`-bordism becomes oriented bordism of `BU(5)`, and the line `p + q = 5` is again zero: `H_{odd}(BU(5); Z) = 0`, `H_1 = 0`, and `Ω^{SO}_q ⊗ Z_{(p)} = 0` for `q = 1, 2, 3, 5`.

*An independent cited route.* `F_u` composed with `Ũ(5) ⊂ Spin(10)` is a structure map `K → Spin ×_{Z_2} Spin(10)` that pulls the 16 back to `R_u` (Theorem Φ, Lemma N). The literature reports the 16 free of every anomaly on that structure: Wang, Wen and Witten for the new-`SU(2)` type; García-Etxebarria and Montero for the bordism groups; Wang and Wen for the whole list. That also gives (iv).

### 3.7 Verdict on the anomaly obstruction

**The 't Hooft-anomaly obstruction to CH1-5U-i is absent.** The mirror `\bar R_u` carries no perturbative `U(5)` anomaly (Theorem A1), no Witten-type anomaly for any `SU(2) ⊂ U(5)` (Theorem A2), no mod-16-type anomaly for any `Z_4 ⊂ U(5)` whose square is fermion parity (Theorem A3), and no new-`SU(2)`-type anomaly (Lemma A4). With the cited bordism fact, it carries none at all (Proposition A5). These hold for `K` and so for `Spin × U(5)`. So no anomaly theorem refutes CH1-5U-i, and CH1-5U-i does not fail at an anomaly step. Off the line the perturbative anomaly is nonzero (Theorem U-A(iv)), so there the obstruction is present: for example `(−40, −400, −5)` for the one-site family. Anomalies that involve the space group `G_U` are not `U(5)` anomalies, and this section does not treat them.

---

## 4. Existence: three new attacks

The attacks on file are (`CH1_5_DRAFT.md` lines 246-248): Attack 1, free (fails at Lemma V); Attack 2, PS-8 on the elementary content (fails at K1-5, and at K2-5 with AM-5); Attack 3, one-site composites `c`, `ccc`, `c^5` (fails at Theorem U-A(iii) with AM-5). The three below differ from them. Attacks 4 and 5 try to prove CH1-5U-i. Attack 6 tries to refute it.

### 4.1 Two lemmas used by the attacks

**Lemma Q1′ (quasi-free points have only charge-`±1` light fields).** Let the tick be quasi-free and number conserving, at a c-number `U(5)` background, with any sea (`CH1_DRAFT.md` C4). Its light excitations are one-body modes near the cuts (`CH1_DRAFT.md` C5): particles, created by combinations of the `c^†_{x,j}` (charge `+1`), and holes, created by combinations of the `c_{x,j}` (charge `−1`). By Lemma Q1 none of them is a member of `R_u ⊕ \bar R_u`.

*Proof.* The one-body space is spanned by the five modes per site, each of charge 1 (`LW1_5U_DRAFT.md` line 48: "Matter creators and `x`-end rishon creators both transform as `5`"). A pocket is a set of one-body modes. ∎

This is the pocket form of `CH1_5_DRAFT.md` line 246: "by K2-5 there is no light 10 or singlet at all."

**Lemma K (the mirror keeps no extra symmetry).** Let `ψ_A, ψ_B, ψ_C` be left-handed Weyl fields in `10bar_{−u}`, `5_{3u}`, `1_{−5u}`, with components `ψ_{A,jk} = −ψ_{A,kj}`, `ψ_B^j`, `ψ_C`. Write `(χη) = ε^{αβ}χ_αη_β` for the Lorentz-invariant pairing of two left-handed spinors, and `\bar χ` for the conjugate right-handed field.
(i) The unitary transformations of the mirror fields that commute with `U(5)` are `U(1)_A × U(1)_B × U(1)_C`, acting by `(e^{iα}, e^{iβ}, e^{iγ})`.
(ii) `O_2 = Σ_{j,k}(ψ_{A,jk}ψ_B^k)(ψ_B^jψ_C)` and `O_3 = Σ ε^{ijklm}(ψ_{A,jk}ψ_{A,lm})(\bar ψ_{B,i}\bar ψ_C)` are Lorentz invariant, `U(5)` invariant and nonzero.
(iii) The subgroup of `U(1)_A × U(1)_B × U(1)_C` that fixes `O_2` and `O_3` is exactly the image of `U(1)_N`, `{(e^{iα}, e^{−3iα}, e^{5iα})}`. So no further symmetry, continuous or finite, commutes with `U(5)` and survives these two interactions.

*Proof.* (i) The three pieces are irreducible (Lemma E (E1)) and of different `SU(5)` types, so Schur's lemma makes every commuting unitary a scalar on each piece. (ii) The index contractions are `SU(5)` invariant. The `U(1)_N` charges add up to `−u + 3u + 3u − 5u = 0` for `O_2` and `−2u − 3u + 5u = 0` for `O_3`. So both are `U(5)` invariant. *Nonzero.* In `O_3` the two brackets involve disjoint fields. For `i = 1` the first contains `8ε^{12345}(ψ_{A,23}ψ_{A,45})`: the eight orderings of the two index pairs contribute with the same sign, because `ψ_{A,kj} = −ψ_{A,jk}` compensates each sign of `ε`, and `(χη) = (ηχ)` for anticommuting fields. That is a nonzero pairing of two independent fields, and the second bracket is one too. In `O_2`, the monomial `ψ_{A,12;1}ψ^2_{B;2}ψ^1_{B;1}ψ_{C;2}` (spinor components after the semicolon) comes only from the term `(j, k) = (1, 2)`, with coefficient `±1`: the term `(2, 1)` pairs `ψ_{A,21}` with `ψ_B^1`, which puts the spinor index 2 on `ψ_B^1`. (iii) `O_2` has charge `α + 2β + γ` and `O_3` has `2α − β − γ`. Both phases are 1 exactly when `e^{i(3α + β)} = 1` (their product) and `e^{i(α + 2β + γ)} = 1`, that is `e^{iβ} = e^{−3iα}` and `e^{iγ} = e^{−iα − 2iβ} = e^{5iα}`. On the mirror, `e^{iθ} ∈ U(1)_N` acts as `(e^{−iuθ}, e^{3iuθ}, e^{−5iuθ})`, and `α = −uθ` runs over the whole circle. ∎

[check] (6): for `n = 2, …, 30`, the solutions of `3α + β ≡ 0` and `α + 2β + γ ≡ 0 mod n` are exactly the multiples of `(1, −3, 5)`. `O_2` and `O_3` are the `U(5)` pieces of the `Spin(10)` quartic `(16bar 16bar)_{10}(16bar 16bar)_{10}` and its conjugate partner under Theorem Φ; that naming is not used.

### 4.2 Attack 4: import a `Spin(10)`-symmetric gapping of the mirror

*The plan.* (1) Find a point of an `L5-U` law at which the light fermions are `R_u ⊕ \bar R_u`, weakly coupled. (2) Add `U(5)`-invariant mirror interactions. By Theorem Φ every `Spin(10)`-invariant, indeed every `Ũ(5)`-invariant, interaction of the mirror 16 pulls back through `φ_u` to a `U(5)`-invariant one; `O_2` and `O_3` are examples. On the lattice they are gauge-invariant multi-fermion operators of the composite carriers of Lemma U-T. (3) Use the continuum expectation that the mirror 16 of `Spin(10)` gaps symmetrically (Wang and Wen; Tong; Razamat and Tong; from memory). Then the mirror flows to a symmetric gapped phase and `R_u` stays light.

*Where it fails.* At step (1), exactly. The points of the law at which the light content is proved are the quasi-free ones (Lemma V, Lemma K2-5). By Lemma Q1′ every quasi-free point has light fields of charge `±1` only, and by Lemma Q1 no member of `R_u ⊕ \bar R_u` has charge `±1`. So the law supplies no weakly coupled point at which the imported flow could start. A starting point would itself need a light fermion of charge `|q| ≥ 3`, which is CH1-5U-q (section 5). Step (3) is, in addition, an expectation in the literature, not a theorem.

*A variant, rejected.* Razamat and Tong gap chiral fermions with an extra strongly coupled gauge group. `L5-U` has one gauge group, `U(5)`. Adding a second one changes the law, and it fails tests 1 and 4 (section 6, row c).

### 4.3 Attack 5: pull back an overlap measure for the 16

*The plan.* The overlap (Ginsparg-Wilson) construction gives Euclidean lattice Weyl fermions with exact gauge invariance when the anomalies cancel: Lüscher for abelian theories (1999), and Kikukawa for the 16 of `SO(10)` (both from memory). Link variables in `Ũ(5)` are a special case of `Spin(10)` links. By Theorem Φ and Lemma N, coupling the 16 to `φ_u(U_ℓ)` for `U(5)` links `U_ℓ` gives a lattice Weyl field whose content is exactly `R_u`. So a lattice chiral `U(5)` gauge theory with content `R_u` would follow.

*Where it fails.* At the link variables, exactly. The overlap operator is a function of c-number unitary link matrices. An `L5-U` link has no such evaluation. `Y2W_DRAFT.md` line 191, Theorem W2: "`L5-U` links have `(U^{jk})^2 = 0`". Suppose a state `ω` of one link were multiplicative on the `U^{jk}`, with values `u_{jk}`. Then `u_{jk}^2 = ω((U^{jk})^2) = 0` for every `j, k`, so the matrix `(u_{jk})` is zero and not unitary. So no state of an `L5-U` link makes `(U^{jk})` a c-number unitary matrix, and the overlap operator cannot be formed from the law's links. Two further steps fail as well. The overlap is a Euclidean kernel, not an update: `CH1_DRAFT.md` line 96 quotes #10049, "The 3+1 tick unitary U(K) itself is not such a V", while CH1-5U-i (a) asks for an update of `L5-U` form. And its fields are elementary CAR multiplets valued in `R_u`; at one site, the ten operators of `ccc` are not ten CAR modes on any invariant subspace (`CH1_5_DRAFT.md` Lemma C2-5(ii)). Replacing the finite registers by c-number `U(5)` links changes PS-6r and fails tests 1 and 4 (section 6, row d).

### 4.4 Attack 6: refute CH1-5U-i through a protected symmetry or the elementary propagator

*The plan, first form (in the spirit of Kikukawa's 2d argument; from memory, not load-bearing).* Kikukawa argued that mirror decoupling fails in 2d abelian models because an exact symmetry of the mirror sector, under which the 't Hooft vertices are charged, survives every allowed interaction. Here: find a global symmetry of the mirror that commutes with `U(5)`, survives every `U(5)`-invariant mirror interaction, and is anomalous. Anomaly matching for it would forbid a symmetric gap, and CH1-5U-i would fail.

*Where it fails.* At Lemma K, exactly. The candidate symmetries are `U(1)_A × U(1)_B × U(1)_C` (Lemma K(i)), and the two interactions `O_2`, `O_3` leave only the image of `U(1)_N`, with no finite remnant (Lemma K(iii)). `U(1)_N` is gauged, and its anomalies on the mirror vanish (Theorem A1). Fermion parity is `−1_5` (section 1.2), inside `U(5)`. So no surviving symmetry has an anomaly to match.

*The plan, second form (Golterman and Shamir).* `CH1_DRAFT.md` line 105 records their result: using "a one-particle lattice Hamiltonian, the authors derive conditions under which the Nielsen-Ninomiya theorem applies. When those conditions hold, the massless fermion spectrum must be vector-like, regardless of interaction strength". Apply it to the propagator of the elementary fermion `c_{x,j}`, dressed with links so that it is gauge invariant.

*Where it fails.* At Lemma Q1, exactly. `U(1)_N` is exact, so the dressed propagator `ω(c_{x,j}(t)W c^†_{y,k})`, with `W` a link product, decomposes over intermediate states of total charge `±1` relative to `ω`. No family member has charge `±1` (Lemma Q1). So no pole or zero of the elementary propagator is a family member, and a vector-like theorem for that propagator says nothing about the light family. It would apply to the light fields of charge `±1`, which CH1-5U-i requires to be gapped anyway.

### 4.5 What the six attacks leave

CH1-5U-i as stated stays open. The anomaly question is decided (section 3.7): no anomaly of the named types, and none at all given the cited bordism fact. Attacks 1-3 fail at Lemma V, K1-5 with K2-5, and Theorem U-A(iii). Attacks 4-6 fail at Lemma Q1′ with Lemma Q1, at Theorem W2 of `Y2W_DRAFT.md`, and at Lemma K and Lemma Q1. Every failure is a proved fact of the law or of the representation, and none is a failure of the law.

---

## 5. The open sub-lemma, and the 1+1D guide

**Lemma CH1-5U-q (open).** There exist an update `U` of `L5-U` form (as in CH1-5U-i (a)), a state `ω` stationary under `U` and invariant under `G_U` and gauge transformations, and a quasi-local fermion-odd operator `ψ` of `U(1)_N` charge `q` with `|q| ≥ 3`, whose large-separation correlations in `ω` agree with those of a free Weyl field.

*Relation to CH1-5U-i.* CH1-5U-i implies CH1-5U-q: its hypothesis IR supplies a light field in `10_u`, of charge `u` with `|u| ≥ 3` (Lemma Q1). So a proof that every light fermion of such a state has charge `±1` refutes CH1-5U-i. That is a sharper form of `CH1_5_DRAFT.md` line 250's "False" option, which asked for `|U(1)_N| ≤ 5`. The family forces more: charges `u`, `−3u`, `5u`, so light fields of charge at least 3, 9 and 15 in modulus. CH1-5U-q is where Attack 4 stops (section 4.2), and no attack on file reaches it. This draft does not attack it.

*Why this sub-lemma.* Attack 4 starts from the law's quasi-free points and stops before any light field of charge `|q| ≥ 3` exists. Representation content does not settle CH1-5U-q: carriers of every line charge exist as local operators (`CH1_5_DRAFT.md` Lemma U-T). Anomalies do not settle it (section 3.7). What remains is dynamical.

**Lemma Q3 (one-site `U(5)`-invariant matter operators).** An operator on one site's matter `Λ(C^5)` commutes with every `Γ(g)`, `g ∈ U(5)`, exactly when it is a function of `N_x`.

*Proof.* The pieces `Λ^k`, `k = 0, …, 5`, are irreducible (Lemma E (E1)) and pairwise inequivalent, because the centre acts on `Λ^k` by `e^{ikθ}`. By Schur's lemma the commutant is spanned by the projections onto the `Λ^k`. ∎

*The 1+1D guide of `CH1_5_DRAFT.md` line 250 is not run.* By Lemma Q3, a `U(5)`-invariant on-site interaction is a function `V(N_x)`. The site cost of a fermion-odd composite that takes `N_x` from `n` to `n + q` is `V(n + q) − V(n)`. So the order of the one-site composites is the chosen `V`, and the guide would print its own input. The informative version needs hopping and the many-site spectrum: that is CH1-5U-q in 1+1D, where the anomaly conditions are quadratic, not cubic. A chain short enough for the machine rules (four five-mode sites, dimension `2^{20}`) cannot separate a light composite from a finite-size level.

---

## 6. Four-test check

Tests: (1) states or fixes a part's target; (2) open-ended, so a part can add to it; (3) settles a downstream physics question by premise; (4) adds structure or constants its own reasons do not need. Nothing is adopted.

| Item | (1) | (2) | (3) | (4) | Result |
|---|---|---|---|---|---|
| a. The structure group `K = Spin ×_{Z_2} U(5)` (section 1.2) | pass: forced by Lemma Z-U(ii); every claim is also proved for `Spin × U(5)` by Lemma N | pass: one group | pass: it decides no physics question; the anomaly results hold on both structures | pass | not a choice; used |
| b. "Type of global anomaly" = pullback along a structure map (section 1.3) | pass | pass: three named types, and Proposition A5 covers all types at once | pass | pass | a definition of words already in the target; used |
| c. A second, strongly coupled gauge group on the mirror (Razamat-Tong variant of Attack 4) | fails: chosen to meet CH1(a)'s mirror gapping | fails unless its group and content are fixed | fails: it settles CH1-i by premise | fails: `L5-U` has one gauge group | rejected |
| d. c-number `U(5)` links in place of finite registers (Attack 5) | fails: chosen to make the overlap available | pass | fails: it settles GA2's bridge Y2 by premise (`GA2_Y2_DRAFT.md` line 26 quotes `TOE_ASSEMBLY.md` line 552: "Their link registers are finite quantum links (PS-6r), not group-valued Wilson links. Whether that sector is in T0's class is bridge Y2.") | fails: it changes PS-6r | rejected |
| e. CH1-5U-q (section 5) | pass: a consequence of CH1-5U-i, posed as a question | pass: one statement | pass: not a premise of any part | pass | recorded as an open sub-lemma |

No change to `L5-U`, to CH1-5U-i or to any working-set entry is proposed.

---

## FINISH

**Proved here (pass 1, not distilled or refereed).**
- Lemma Ũ and Theorem Φ: every family on the line is `R_u = φ_u^*S`, the restriction `S` of the 16 to `Ũ(5) = {(g, z) : z^2 = det g}` pulled back along the surjection `φ_u(g) = (g·det(g)^{−(2u+1)/5}, det(g)^{−u})`, with kernel `μ_{|u|}` and `φ_u(−1_5) = −1̃`. The homomorphisms `U(5) → Ũ(5)` that fix `SU(5)` are exactly the `ψ_{a,b}`, `2b = 1 + 5a`, `b ≡ 3 mod 5`. So the line is exactly the set of such pullbacks with odd `b`, and `u = ±1` is impossible (Corollary Φ.1).
- Lemma N: anomalies pull back along structure maps; every anomaly of `R_u` is the pullback of the corresponding anomaly of `S`.
- Theorem A1: every perturbative `U(5)` anomaly of `R_u` and `\bar R_u` vanishes, `Tr X^3 = Tr X = 0` on all of `u(5)` (two proofs).
- Theorem A2: Witten's type vanishes for every `SU(2) → U(5)`; `R_u` has `4n(5)` instanton zero modes.
- Theorem A3: the mod-16 type vanishes for every `Z_4 ⊂ U(5)` whose square is fermion parity; `ν ∈ {16, 0, −16}`. Remark A3.1: the 15-member family has `ν = ±15`.
- Lemma A4: the new-`SU(2)` type has no structure map into `Spin ×_{Z_2} U(5)`.
- Proposition A5(i): `Spin ×_{Z_2} U(5) ≅ (Spin^c × SU(5))/μ_5`.
- Lemma Q1 and Lemma Q1′: no family or mirror member has charge `±1`; every quasi-free point has only charge-`±1` light fields.
- Lemma K: two `U(5)`-invariant mirror quartics leave exactly the image of `U(1)_N` of the mirror's flavour symmetry, with no finite remnant.
- Lemma Q3: one-site `U(5)`-invariant matter operators are functions of `N_x`.
- The failing steps of Attacks 4-6 (section 4).

**Counterexamples.** None to a stated claim. The candidate refutations of CH1-5U-i by anomalies (section 3), by a protected mirror symmetry and by the elementary propagator (Attack 6) are refuted as routes.

**Open, by name.**
- **CH1-5U-i** (`CH1_5_DRAFT.md` 5.1), anomaly obstruction absent (section 3.7). Six attacks failed: free (Lemma V); PS-8 on the elementary content (K1-5, K2-5 with AM-5); one-site composites (Theorem U-A(iii) with AM-5); `Spin(10)` import (Lemma Q1′ with Lemma Q1); overlap pullback (Theorem W2 of `Y2W_DRAFT.md`: `(U^{jk})^2 = 0`); protected symmetry or elementary propagator (Lemma K, Lemma Q1).
- **CH1-5U-q** (section 5): a light fermion of charge `|q| ≥ 3` in an invariant stationary state of an `L5-U` law. CH1-5U-i implies it; its negation refutes CH1-5U-i. Not attacked here.
- The word "all" in section 3.7 rests on Proposition A5(ii)-(iii), cited, not rebuilt.
- Inherited, unchanged: AM-5, CH1-ii, CH1-5O-i, reflection positivity, CG1K-H, LW1-5-X, VC1-5U-odd.

**What changes downstream.**
- `CH1_5_DRAFT.md` line 244, "A global-anomaly analysis for this content", is now on file: no `U(5)` anomaly of the named types, and none at all given the cited bordism fact. Line 241's "anomalies do not forbid its symmetric gapping" now holds for global anomalies too.
- CH1 on `L5-U` does not fail at an anomaly step. **No named failing step for `L5-U`.** The law stays live under `TOE_ASSEMBLY.md` section 3.5.
- Every twisted family is the 16 of `Spin(10)` restricted to `Ũ(5)` and pulled back along a covering of `U(5)` (Theorem Φ). So `Spin(10)` anomaly and gapping results transfer to `L5-U` as statements about the light fields, without a `Spin(10)` acting on the lattice; the lattice's own `U(5)` action does not factor through `φ_u`, since `c_{x,j}` has charge 1.
- `LW1_5U_DRAFT.md` line 220 (the mod-16 criterion "does not apply" to `S_+` under genuine `U(5)`): on the line the centre acts uniformly, and the criterion gives `ν = ±16`, which is zero mod 16.
- For CH1-5U-i the next question is dynamical and is CH1-5U-q. Its natural first test is whether any `L5-U` law, with finitely many gauge-invariant gates, has a light fermion of charge `|q| ≥ 3` at all.
- For GA2 and Y2: Attack 5 adds a second reason that `L5-U`'s links are not group valued at the lattice scale, namely that no link state evaluates `(U^{jk})` to a unitary matrix.
