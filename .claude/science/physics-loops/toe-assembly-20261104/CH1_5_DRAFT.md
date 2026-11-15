# CH1 on the five-mode laws, pass 1

Written 2026-11-05 by a Claude Opus 5.5 subagent, as a pass-1 lane under owner decision LW1-5-RQ ("keep both live ... until one fails at a named step"). It restates the proved results of `CH1_DRAFT.md` for the two five-mode laws `L5-O` and `L5-U`, and it settles the anomaly question for one family on each law. Method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation (`check_ch15.py`, output `out.txt`, in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-yalow-de8f06/bd9fd3c1-9024-4004-87d2-e8917bcfe6a3/scratchpad/ch15/`; under 1 s, a few MB, exact rational arithmetic). A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `toe-assembly-local` (same commit as `claude/toe-assembly`) | `f67931a5ec` |

Files read at that commit, by line: `TOE_ASSEMBLY.md` lines 71-235 (section 3 in full, with 3.4 and 3.5) and 397-427 (CH1, CG1); `CH1_DRAFT.md` lines 1-454 (all); `CG1_KILL_DRAFT.md` lines 1-253 (all); `LW1_5_DRAFT.md` lines 1-22, 39-62, 229-445 (head, one site, sections 4.4-10); `LW1_5O_DRAFT.md` lines 37-135 (outcome, section 1, sections 2.1-2.4 with Theorem K); `LW1_5U_DRAFT.md` lines 32-78 (outcome, setting, Lemma E), 111-137 (section 3, Lemma Z-U), 195-242 (sections 6-7, Proposition D).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws, CH1 and CG1 are read plainly. Where a word allows two readings, both are named (CG1K's R-B and R-M, section 1). Nothing is adopted.

**Working set used, by name.** PS-5 (fallback text, D1). PS-6 and PS-6r, only through the two laws of `LW1_5_DRAFT.md` section 8.1. PS-1c (covariance, for Lemma C3). PS-7r (the sea, for F2a). PS-8 (law to test, for K1-5). PS-2, PS-3 and its refinements, PS-4, PS-9 to PS-11 are not used. Results used, cited by name: from `CH1_DRAFT.md`, F1-F4, F3a, F3b, F3', S1, S2, S3, C2, C3, K1, K2, Lemma AM; from `LW1_5_DRAFT.md`, Lemma Z, A2-5, B1-5, section 8.1 item 10, section 10; from `LW1_5O_DRAFT.md`, Lemma K0, Lemma F, Theorem K; from `LW1_5U_DRAFT.md`, Lemma Z-U, Lemma E, Proposition D; from `CG1_KILL_DRAFT.md`, Lemma C, Lemma C-U, Lemma W, Theorem O-I, Theorem O-M, Proposition F, Theorem U-B, Theorem U-M.

**Input from outside the working set, named once.** **AM-5**, anomaly matching for an unbroken exact subgroup (section 4.5). It is a standard continuum principle. It is not proved here and no result below treats it as proved. Every conclusion that uses it says so.

---

## 0. The question, quoted

`TOE_ASSEMBLY.md` line 214: "The owner chose: **keep both live.** MT1, GA1 and CG1 are developed on both laws until one fails at a named step."

CH1(a), line 399: "Within `L` there is a local lattice theory, invariant under `G`, whose light spectrum at scales `>> a` is exactly the chiral content of CG1 (one Weyl 16, or the Standard Model multiplet, per family), with every doubler and every mirror gapped at scale `~ 1/a` [**open input CH1-i** ...], no extra light charged state, gauge anomalies cancelling, the gauge field kept massless [**open input CH1-ii** ...], and the measure reflection positive."

The fact that sets the anomaly question. `CG1_KILL_DRAFT.md` line 198: "The family `5bar_{−1} + 10_{−3} + 1_{−5}` has `U(1)_N` gravitational, cubic and mixed `SU(5)^2` anomalies `(−40, −400, −5)`. ... So CH1's "gauge anomalies cancelling" needs `U(1)_N` broken at long distance, or other light `U(1)_N`-charged fields that cancel it."

## 0.1 Outcome in one paragraph

**Carry-over.** F1-F4 hold unchanged on both laws. They are one-body statements for any number of modes per site, and both free ticks are five copies of LW1's. On `L5-O` they also hold for Majorana gates in Nambu form, with "charge sector" read as a weight sector of a preserved torus (Remark F-N). S1, S2, S3, C2, K1 and K2 are restated and proved (section 3). C3 holds unchanged but has no role: one family's carriers sit at one site. **The lattice fact.** Every free gauge-covariant tick of either law, at any locality, has light content with zero net chirality in every weight sector, so every perturbative anomaly of its light content vanishes (Lemma V). That is all this draft proves about the total anomaly. **`L5-O`.** `so(10)` has no invariant cubic form, so `Spin(10)` has no perturbative anomaly in any representation (Lemma O-A). An unbroken `Spin(10)` asks nothing of the light spectrum through anomalies. CH1(a) with `Spin(10)` unbroken still fails, at CG1K's Theorem O-M (under R-M): one family is never a `Spin(10)` multiplet. **`L5-U`.** For a family carried as `U(5)` multiplets, `SU(5)^3` always cancels. The three `U(1)_N` anomalies vanish exactly when `U(1)_N` acts on the family as `u X`, with `X` the charge `(1, −3, 5)` on `(10, 5bar, 1)`. That holds exactly when `U(1)_N` restricted to the family lies in the span of `Y` and `B − L` (Theorem U-A, Theorem S2-5). `U(5)` integrality forces `u ≡ ±2 mod 5`, so `|u| ≥ 3`, and the `Spin(10)` normalisation `u = 1` is excluded. The one-site carriers `c`, `ccc`, `c^5` are off this line: `(−40, −400, −5)`. Twisted carriers on the line exist as local operators (Lemma U-T). **Verdict under AM-5.** `L5-U` with unbroken `U(1)_N` and a one-family light spectrum is **not excluded**. It is excluded for every realization off the line, the one-site one included. On the line every member is a composite, with matter-number change at least 3, 9 and 15. Light singlets cannot cancel the one-site anomaly, because the mixed `U(1)_N SU(5)^2` term needs `SU(5)`-charged states, which CH1(a) forbids. **No change to the law is needed, and none is proposed** (section 4.6). **No law fails at a named step here.** CH1's first open inputs are **CH1-5U-i** (symmetric gapping of the mirror of an anomaly-free twisted `U(5)` family, `U(5)` unbroken) and **CH1-5O-i** (a light family under `H` with `Spin(10)` broken, which contains CG1K-H). Each has three attacks written out, and each attack fails for a stated reason (section 5).

---

## 1. Conventions

**Laws.** `L5-O[R]` and `L5-U` as in `LW1_5_DRAFT.md` section 8.1. Item 10 (line 313): "**Free tick.** Replace every `U_ℓ^{ab}` by `δ^{ab}`. ... Its one-body tick is `(W V W^*) ⊗ 1_5`, with `V` LW1's free tick". The variant `L5-U` has "the same" free tick. Statements for `L5-O` assume irreducible `so(20)` registers (as `L5-O[S_+]`), which is Lemma Z's hypothesis, unless marked.

**`U(1)_N`.** On `L5-U` it is the `U(1)` factor of `U(5)`, with Gauss generator `Q_x = 𝒢^1_x` (`LW1_5U_DRAFT.md` section 1.1). On `L5-O` it is the circle of `Spin(10)` generated by `Q^O_x = Σ_j 𝒢_x^{2j−1,2j}`. On matter, `Σ_j M_x^{2j−1,2j} = N_x − 5/2` (`LW1_5_DRAFT.md` section 1.1), so on both laws a matter operator's `U(1)_N` charge is the change of matter number it makes. A *homogeneous* local operator `O` has charges `q_x` with `e^{iθQ_x}Oe^{−iθQ_x} = e^{iθq_x}O`.

**Embedding and family.** `H` is the image of `G_SM` under a Case I embedding (CG1K Lemma C, Lemma C-U). `F_t` is the family of CG1K section 1, with hypercharges `t·(1, −4, 2, −3, 6, 0)` on `(Q, u^c, d^c, L, e^c, ν^c)`. Twists `(k, k', k'')` are those of CG1K Theorem U-M, line 182: weights "one orbit of `(k+1, k+1, k, k, k)` (a `Λ^2(5) ⊗ det^k`), one orbit of `(k', k', k', k', k'−1)` (a `5bar ⊗ det^{k'}`), and possibly one singlet `det^{k''}`". Their `U(1)_N` charges are `a = 5k + 2`, `b = 5k' − 1`, `c = 5k''`.

**Readings.** R-B, R-M and R-F of CG1K section 1, unchanged and not adopted. R-M for a subgroup `G_∞`: the family is a sum of `G_∞`-multiplets of local operators.

**Charges.** `X := 5(B − L) − 4Y` (CH1 S2's "`SO(10)` charge"), which is `(1, −3, 5)` on the members of `(10, 5bar, 1)` in case A. `X' := 4Y + (B − L)` (also listed in S2). [check] (6): `X` on `(Q, u^c, e^c | L, d^c | ν^c)` is `(1, 1, 1 | −3, −3 | 5)`.

**Hypothesis IR.** As in CH1 Lemma AM (line 301): quasi-local fermion-odd operators `ψ_i` whose large-separation correlations in `ω` agree with free Weyl fields of chiralities `χ_i`, all other connected correlations decaying exponentially. Here `ψ_i` spans an irreducible representation `R_i` of the group named.

---

## 2. Carry-over table

| `CH1_DRAFT.md` result | On `L5-O` | On `L5-U` | Where |
|---|---|---|---|
| F1 (circuits null-homotopic) | unchanged; also for Majorana gates | unchanged | `LW1_5_DRAFT.md` line 432; Remark F-N |
| F2, F2a, F2b (gap at one cut) | unchanged; also Nambu | unchanged | same |
| F3, F3a, F3b, F3' (Floquet NN) | unchanged per weight sector of a preserved torus; Nambu total is automatic | unchanged; sectors `U(1)_N` or torus weights | Remark F-N |
| F4 (`W3` counts chirality) | unchanged | unchanged | line 432 |
| S1 (charge parity) | restated, S1-5, for `U(1)_N ⊂ Spin(10)` | restated, S1-5 (Lemma Z-U(i)) | 3.2 |
| S2 (exact `U(1)` is not `Y`) | hypothesis does not arise (no abelian factor); restated for `U(1)_N` | restated, S2-5 | 3.3 |
| S3 (CH1(a) needs) | (i) false as stated (`G` non-abelian); restated, S3-5 | same | 3.4 |
| C2 (cluster modes) | restated, C2-5 | restated, C2-5 | 3.5 |
| C3 (no odd layout) | unchanged; no role | unchanged; no role | 3.5 |
| K1 (endpoints release partners) | restated, K1-5 (weight sectors, Nambu) | restated, K1-5 | 3.6 |
| K2 (elementary set anomalous) | **false as stated**: the elementary set is the real 10, anomaly free; replaced by K2-5(O) | restated, K2-5(U): anomalous | 3.6 |
| Lemma AM (not proved) | restated as input AM-5 | same | 4.5 |
| CH1-C1, CH1-C3 (odd-charge bound states on `L_cube`) | superseded by CH1-5O-i | superseded by CH1-5U-i | 5 |

---

## 3. Restatements, with proofs

### 3.1 The free theorems

`LW1_5_DRAFT.md` line 432: "**CH1, Theorems F1-F4.** Unchanged: they are one-body statements for any number of components per cell, and the free tick of both laws is number conserving." That is correct as quoted. F1's hypothesis allows any `r`; F2-F4 use only a `C^1` (or `C^3`) map `T^3 → U(n)`. The free tick of item 10 is number conserving and commutes with `1 ⊗ u` for every `u ∈ U(5)`, so F3(iii) applies per weight of the diagonal torus: five flavour sectors.

**Remark F-N (Majorana gates on `L5-O`).** At a c-number background `U_ℓ^{ab} ∈ SO(10)`, a gate of `L5-O` is quasi-free but not number conserving. Its one-body action on `span{γ}` is real orthogonal. Complexified and Bloch transformed, it is a continuous map `U : T^3 → U(n)` with a particle-hole map `C` (antiunitary, `C U(k) C^{-1} = U(−k)`).
(i) F1 and F2 hold for this `U`, with the same proofs: they use only that `U` is a continuous unitary-valued map and, for F1, a layer structure.
(ii) For the sea projector `P` (C4), the pocket charges at `k_0` and `−k_0` are opposite. So F3's total sum is zero for every such `U`, and it carries no information.
(iii) If the gate commutes with a torus `T` of `Spin(10)`, F3 holds in each `T`-weight sector, and `C` maps sector `w` to sector `−w`. Then F3 in sector `w ≠ 0` is a real constraint.
*Proof of (ii).* Off the pockets, `CP(k)C^{-1}` is the projector onto quasi-energies in `(0, π)` of `U(−k)`, which is `1 − P(−k)`. Let `ι(k) = −k`, which maps the ball `B` around `k_0` onto the ball `B'` around `−k_0` with determinant `−1`, so it reverses the boundary orientation. Put `Ω_P = tr(P dP ∧ dP)`. Then `ι^*Ω_P = Ω_{1−CPC^{-1}} = −Ω_{CPC^{-1}}`, because `tr(dQ ∧ dQ) = 0`. And `Ω_{CPC^{-1}} = \overline{Ω_P}` componentwise, because `tr(CAC^{-1}) = \overline{tr A}`. So `∫_{∂B'}Ω_P = −∫_{∂B}ι^*Ω_P = \overline{∫_{∂B}Ω_P}`. With `c = (i/2π)∫Ω`, and `∫_{∂B}Ω_P = −2πi c_B`, this gives `c_{B'} = (i/2π)(2πi c_B) = −c_B`. (iii) is F3(iii) applied to the blocks of `T`. ∎

### 3.2 Charge parity

**Lemma S1-5.** On `L5-U`, and on `L5-O` with irreducible registers: every homogeneous local operator `O` has `Σ_x q_x(O) ∈ Z`, and its fermion parity is `(−1)^{Σ_x q_x(O)}`. So every fermionic excitation has odd `U(1)_N` charge, every bosonic one even, and every `U(1)_N`-neutral excitation is a boson.

*Proof.* `L5-U`: `LW1_5U_DRAFT.md` line 116, Lemma Z-U(i): "A homogeneous local operator `O` has fermion parity `(−1)^{Σ_xq_x(O)}`." `L5-O`: take a finite `Λ` that contains `O`'s sites and both ends of its links. `exp(iπQ^O_x)` is `ω_x` of `LW1_5O_DRAFT.md` section 1.2, and its site factor is rotation by `π` in all five planes, which is a lift of `−1_{10}`. `LW1_5_DRAFT.md` line 239, Lemma Z(ii): "the element `−1_{10} ∈ SO(10)` applied at every site of a finite region `Λ` (with its link changes) acts as the fermion parity automorphism on every operator supported, with all its links, inside `Λ`". So `Ad ∏_{x∈Λ}ω_x(O)` is the parity of `O` times `O`. It is also `e^{iπΣq_x}O`. Integrality: `exp(2πiQ^O_x) = ω_x^2 = z_x` (Lemma K0(ii)), and `Ad z_x` is the identity on the quasi-local algebra (Lemma Z(i)), so `e^{2πiΣq_x} = 1`. ∎

S1(i) ("`|q_x| = q` is the same for all sites") is automatic on both laws: the frame group acts on every site by the same representation.

### 3.3 Which charges the exact `U(1)_N` can carry

`LW1_5_DRAFT.md` line 428: "On `L5-U`, S2 applies to `U(1)_N` and says it is not hypercharge; hypercharge lies in `su(5)`, where S2 says nothing." This theorem says what else the parity rule excludes.

**Theorem S2-5.** Take R-F. On `L5-U`, or on `L5-O` for the circle `U(1)_N ⊂ Spin(10)`:
(i) `U(1)_N` restricted to the family is not a multiple of `Y` and not a multiple of `Q_em`.
(ii) Let the family be a sum of `U(5)`-multiplets (R-M for `U(5)`; on `L5-O`, for the `U(5)` of a Case I embedding). In case A the charges are `(a, b, c) = (5k+2, 5k'−1, 5k'')` with `k` odd, `k'` even and `k''` odd. In case `B_k` they are the same with `k' = −(1+3k)` and `k'' = 2+5k`.
(iii) `U(1)_N` restricted to the family lies in `span{Y, B − L}` exactly when `(a, b, c) = u(1, −3, 5)`. In case A that is `U(1)_N = uX` and `(k', k'') = (−3k−1, 5k+2)`. In case `B_k` it always holds, with `U(1)_N = uX'`. Here `u = 5k + 2`.
(iv) On that line `u` is odd and `u ≡ 2 mod 5` (`u ≡ −2` for the conjugate embedding of Lemma C-U). So `|u| ≥ 3`, and `u = ±1` is excluded. In S2's parametrization `uX` is `(α, β) = (−2u, 5u)`, which S2 allows.
(v) The parity rule of (ii) excludes no point of the line of (iii).

*Proof.* (i) By S1-5 and R-F every member has an odd charge. `Y(u^c)/Y(Q) = −4` is not a ratio of two odd integers. `Q_em(ν) = 0` is even. (ii) CG1K line 186, *Parity*: "`U(1)_N` charge `Σn_j`: `5k + 2`, `5k' − 1`, `5k''`", and line 183 for the parity conditions; line 184 for `B_k`. On `L5-O`, tensor-class weights are in `Z^5` (CG1K Lemma W(W1)), so the same weight arithmetic applies. (iii) In case A, `U(1)_N` commutes with `SU(5)`, so it is constant on each `SU(5)` multiplet. An element `αY + β(B − L)` that is constant on the 10 (`Q, u^c, e^c`) satisfies `α/6 + β/3 = α + β`, so `β = −5α/4`, and then it is `−(α/4)X`. Conversely `X` is constant on the multiplets ([check] (6)). So `(a, b, c) ∝ (1, −3, 5)`. With `a = 5k+2`, `b = −3a` gives `k' = −3k − 1` and `c = 5a` gives `k'' = 5k + 2`. In case `B_k`, substitute `k' = −(1+3k)`, `k'' = 2+5k`: then `b = −15k − 6 = −3a` and `c = 5a`. On the flipped members, `Q, d^c, ν^c` carry `u`, `u^c, L` carry `−3u` and `e^c` carries `5u`; solving `ν^c: β = u`, `Q: α/6 + β/3 = u` gives `α = 4u`, and `u^c, L, e^c` then check. (iv) `5k + 2` with `k` odd is odd and `≡ 2 mod 5`. The smallest modulus is `|−3| = 3` at `k = −1` ([check] (1)). The conjugate embedding sends the 10-orbit to `(k−1, k−1, k, k, k)`, with charge `5k − 2`. (v) On the line, `k` odd gives `k' = −3k − 1` even and `k'' = 5k + 2` odd. ∎

*Reading.* The `U(5)` centre explains (iv). `U(5) = (SU(5) × U(1))/Z_5`, so a `U(5)` representation has `U(1)_N` charge `≡` its `SU(5)` 5-ality mod 5. The 10 has 5-ality 2. The `Spin(10)` spinor normalisation `u = 1` needs `det^{1/2}`. That is `LW1_5U_DRAFT.md` Remark D.1's shift `c = 5/2`, which "is not a representation of `U(5)`".

### 3.4 What CH1(a) needs on each law

**Theorem S3-5.** With `G` the exact group:
(i) `G = Spin(10)` (`SO(10)` on the algebra) on `L5-O[S_+]`, and `U(5)` on `L5-U` (`LW1_5_DRAFT.md` line 430). S3(i), "`G = U(1)`", is false on both.
(ii) `H ⊂ G` for every Case I embedding. A fermion-odd family is carried exactly when `α` is even (CG1K Theorems O-I(iii), U-B).
(iii) CH1(a) with `G` unbroken at long distance, read with R-M. On `L5-O` it fails at CG1K Theorem O-M: every `Spin(10)` multiplet containing `(3, 2)` has at least 40 components. Its "one Weyl 16" clause fails at Theorem K (no fermion-odd local operator is a 16). On `L5-U` representation content allows it (Theorem U-M). Under AM-5 it then needs the line of S2-5(iii) (section 4.5).
(iv) CH1(a) with `G` broken to some `G_∞ ⊇ H` (R-B): nothing here excludes it on either law. The `H` anomalies of `F_t` vanish for every `t` ([check] (5)).

*Proof.* (i) is quoted. (ii) is quoted. (iii) CG1K line 154 gives O-M; `LW1_5O_DRAFT.md` line 97, (K1): "Every matter operator lies in a true `SO(10)` representation at every site, and fermion-odd matter operators are class 2". Under R-M a light spectrum invariant under unbroken `G` is a sum of `G`-multiplets of local operators. (iv) The five `H` conditions are one-line sums. In units of `t`: gravitational `6 − 12 + 6 − 6 + 6 = 0`; `Y^3`: `6 − 192 + 24 − 54 + 216 = 0`; `SU(3)^2 Y`: `(1/2)(2 − 4 + 2) = 0`; `SU(2)^2 Y`: `(1/2)(3 − 3) = 0`; `SU(3)^3`: `2 − 1 − 1 = 0`. There are four doublets. ∎

### 3.5 Cluster modes and layouts

**Lemma C2-5.**
(i) For any set `S` of three or five distinct modes at one site, `C_S = ∏_{j∈S}c_{x,j}` is an exact fermion mode on the subspace where `S` is empty or full. Its `U(1)_N` charge is `−|S|`.
(ii) The ten operators `c_S`, `|S| = 3`, at one site do not satisfy the CAR of ten modes on any nonzero subspace that they and their adjoints leave invariant.

*Proof.* (i) C2(i)-(iv)'s proof (line 339) uses only that the `c`'s are distinct CAR modes. Five modes at one site are such modes. (ii) Such a subspace `W` would carry a representation of the CAR algebra of ten modes. That algebra is `M_{2^{10}}(C)` (Jordan-Wigner; standard, credited), which is simple. So `dim W` is a multiple of 1024. But `dim W ≤ 32`. ∎

So a light 10 is a multiplet of composite operators, not ten exact modes at a site. It must be built from operators on growing regions, as any composite is.

**C3 on five-mode laws.** The statement and proof are geometry and the covariance group. `LW1_5_DRAFT.md` A2-5, line 382: "Its symmetries are those of A2", and B1-5, line 392, gives the same transitivity. So C3 holds unchanged. It has no role here. The carriers `c`, `ccc`, `c^5` sit at one site (CG1K Proposition F), and size 1 is allowed. So CH1's Attack 2(i), the layout obstruction, does not arise on five-mode sites. The twisted carriers of Lemma U-T span several sites, but they are operators (bound states), not a layout fixed by the law.

### 3.6 The kill test at the endpoints

**Theorem K1-5.** K1 (line 287) holds on both laws with "charge sector" read as a weight sector of a torus `T` of the exact group that the endpoint's light generator preserves. On `L5-O` the generator may be in Nambu form, and the sectors are the `T`-weight spaces of Remark F-N(iii). If the light sector keeps Weyl nodes of net chirality `χ ≠ 0` in sector `w`, it has light pockets of total charge `−χ` in sector `w`.

*Proof.* K1's proof builds `H~ = H_l + cP_m` (or `U~ = U_l ⊕ e^{−iπ/2}P_m`) and applies F3. If `H_l` and `P_m` commute with `T`, so does `H~`, and F3(iii) applies per block. In Nambu form use Remark F-N(iii). ∎

**Lemma K2-5.**
(U) On `L5-U` the elementary light content of the free tick is two left-handed and two right-handed Weyl 5's, all of `U(1)_N` charge 1 (CH1 line 281, five copies). Every subset of net chirality `χ ≠ 0` (counted in 5's) has `SU(5)^3 = χ`, `U(1)_N SU(5)^2 = χ/2`, `U(1)_N^3 = 5χ` and `U(1)_N`-gravitational `5χ`. All are nonzero.
(O) On `L5-O` the same content is two left-handed Weyl fields in the real 10 (a Dirac 5 is a left-handed `5 ⊕ 5bar`). Every set of such fields has zero `Spin(10)` anomaly (Lemma O-A) and admits the invariant symmetric bilinear `δ_{ab}`, a Majorana mass. K2's conclusion, "both nonzero", is false on `L5-O`.
(both) Under every Case I embedding the 10 restricts to `(3,1) ⊕ (3bar,1) ⊕ (1,2) ⊕ (1,2)`, which contains no `(3, 2)`. So `Q` is never elementary. Nor are `u^c` and `e^c`: under `SU(5)` they lie in the 10, not the 5bar.

*Proof.* (U) `A(5) = 1`, `T(5) = 1/2`, five components of charge 1. (O) `ψ_aψ_b δ_{ab}` is `SO(10)`-invariant and symmetric. (both) `C^5 = (3,1) ⊕ (1,2)` (Lemma C-U), and `R^{10} ⊗ C = C^5 ⊕ \overline{C^5}`. ∎

*Kill-test verdict on five-mode sites.* PS-8 acting on the elementary content cannot give one family on either law. On `L5-U` the reason is K1-5 at quasi-free endpoints (proved) and K2-5(U) with AM-5 in general. On `L5-O` the reason is representation content (K2-5, proved): the target has members that are not in the 10. On both laws `Q`, `u^c`, `e^c` and `ν^c` must be composites.

---

## 4. The anomaly ledger

### 4.1 The lattice fact

**Lemma V (free light content is vector-like in every weight sector).** Let `V` be a free tick of `L5-O` or `L5-U` at a c-number background that commutes with a torus `T` of the exact group `G` (for example item 10's free tick, which commutes with the whole global `U(5)`). Take any sea filled between the cuts `0` and `π` (C4), at any locality. Then for every polynomial `f` on `Lie(T)`, `Σ_j c_j f(w_j) = 0`, the sum running over the light pockets, with `w_j` the weight of the pocket's sector. If the pockets are linear Weyl nodes of fields `ψ_i` in representations `R_i` of `G` with chiralities `χ_i`, and `T` is maximal, then every perturbative anomaly coefficient of `G` on the light content vanishes: `Σ_iχ_i Tr_{R_i}(X^3) = 0` for all `X ∈ 𝔤`, and `Σ_iχ_i Tr_{R_i}(X) = 0`.

*Proof.* Group the pockets by sector: `Σ_jc_jf(w_j) = Σ_wf(w)Σ_{j∈w}c_j`. Each inner sum is zero by F3(iii) (Remark F-N(iii) on `L5-O`). With linear Weyl nodes, F3a gives `Σ_{j∈w}c_j = Σ_iχ_i·mult_w(R_i)` up to the cut-`π` sign, so `Σ_iχ_iΣ_{w∈wt(R_i)}w(X)^3 = 0` for `X ∈ Lie(T)`. That is `Σ_iχ_iTr_{R_i}(X^3)` on `Lie(T)`. This function of `X` is `Ad`-invariant, and every `X ∈ 𝔤` is `Ad`-conjugate into `Lie(T)` (maximal torus theorem; standard, credited). So it vanishes on `𝔤`. The symmetric `d`-symbol is its polarization, so it vanishes too. The same argument with `f(w) = w(X)` gives the linear traces. ∎

*Scope.* This is the lattice-level fact: the elementary content of an exact gauge-covariant law, read through any free tick, has zero total anomaly. It does not reach interacting updates. There "the anomaly of the lattice content" is defined only through long-distance correlations, and that step is AM-5.

### 4.2 `L5-O`

**Lemma O-A (`Spin(10)` has no perturbative anomaly).** For every finite-dimensional representation `R` of `Spin(10)`, `Tr_R(X^3) = 0` and `Tr_R(X) = 0` for all `X ∈ so(10)`.

*Proof.* `Tr_R(X)`: `so(10)` is spanned by commutators (it is simple; cited, as in `LW1_5O_DRAFT.md` Lemma B10), and traces of commutators vanish. `Tr_R(X^3)`: on `Lie(T) ≅ R^5` it is a cubic polynomial `p`, invariant under the Weyl group (the multiset of weights of `R` is). That group contains every sign change of an even number of coordinates. Each cubic monomial has a variable `x_i` of odd degree and involves at most three variables. Pick `m` outside them (five coordinates). Flipping the signs of `x_i` and `x_m` is an even sign change, and it negates the monomial. So averaging over the even sign changes kills every cubic monomial, and the invariant `p` is zero. Conjugacy into `Lie(T)` finishes, as in Lemma V. ∎

[check] (4): `Σ_w (w·x)^3 = 0` for the weights of the 10, 16, 45, 120 and 210 at 20 random `x`; every cubic monomial averages to zero over the 16 even sign changes.

**Ledger on `L5-O`.**
- `G_∞ = Spin(10)` unbroken: no perturbative condition. CH1(a) fails there by S3-5(iii) (Theorem O-M under R-M), not by anomalies.
- `G_∞ = U(5)` of a Case I embedding: the `L5-U` ledger of 4.3 applies word for word, because tensor-class weights lie in `Z^5` (Lemma W(W1)) and the analysis is weight arithmetic. Local realization of the twisted carriers on `L5-O` needs nine or more vector factors. That is CG1K-loc, which CG1K did not treat, and it is not treated here.
- `G_∞ = SU(5)` or `H`: the one-site family of Proposition F has `SU(5)^3 = 0` and `H` anomalies zero (S3-5(iv)).
- Global anomalies are not treated.

### 4.3 `L5-U`

**Theorem U-A (`U(5)` ledger of one family).** Let one family be carried as `U(5)`-multiplets (Theorem U-M), with `U(1)_N` charges `(a, b, c)` on `(10, 5bar, 1)` as in section 1. Then:
(i) `SU(5)^3 = A(10) + A(5bar) = 1 − 1 = 0`, and the `SU(5)`-gravitational trace is zero.
(ii) In the order of CG1K (gravitational, cubic, mixed): `U(1)_N`-gravitational `10a + 5b + c`, `U(1)_N^3 = 10a^3 + 5b^3 + c^3`, and `U(1)_N SU(5)^2 = (3/2)a + (1/2)b`.
(iii) The one-site carriers `ccc`, `c`, `c^5` (`k = −1`, `k' = 0`, `k'' = −1`, so `(a, b, c) = (−3, −1, −5)`) give `(−40, −400, −5)`.
(iv) All three `U(1)_N` anomalies vanish exactly when `(a, b, c) = u(1, −3, 5)`, that is on the line of S2-5(iii). The mixed and gravitational conditions fix the line, and the cubic one then holds.
(v) Every flipped family `B_k` is on the line, so all its `U(5)` anomalies vanish.
(vi) Without `ν^c`, no twist gives zero `U(1)_N` anomaly.

*Proof.* (i) `A(5) = 1` and `A(Λ^2 5) = (N − 4)A(5) = 1` at `N = 5` (`LW1_5U_DRAFT.md` Proposition D(i)'s proof: "On `Λ^2`: ... `(N−4)p_3`"); `A(5bar) = −1`; twisting by `det^k` does not change `SU(5)` content. The `SU(5)` generators are traceless. (ii) Dimensions 10, 5, 1 and indices `T(10) = 3/2`, `T(5bar) = 1/2`, as in Proposition D(iii)'s proof. (iii) `−30 − 5 − 5 = −40`; `10(−27) + 5(−1) + (−125) = −400`; `(3/2)(−3) + (1/2)(−1) = −5`. (iv) Mixed zero: `b = −3a`. Then gravitational zero: `c = 5a`. Then cubic: `10a^3 − 135a^3 + 125a^3 = 0`. Conversely the line gives zero for all three. (v) S2-5(iii). (vi) Without the singlet, mixed zero gives `b = −3a`, and gravitational `10a + 5b = −5a = 0` forces `a = 0`. But `a = 5k + 2 ≠ 0`. ∎

[check] (1)-(3): over `|k|, |k'|, |k''| ≤ 12` the anomaly-free twists are exactly the five points of the line in the box; the one-site value is `(−40, −400, −5)` as (gravitational, cubic, mixed); `B_k` at `k = −3, −1, 1, 3` gives zero; without `ν^c` there is no solution for `|k|, |k'| ≤ 30`.

**Lemma U-T (twisted carriers).** On `L5-U`, for every `m ∈ {1, …, 9}`:
(i) There is a nonzero, fermion-odd space of local operators carried at `y` that is the `U(5)_y` representation `5bar ⊗ det^2` (`U(1)_N` charge 9). With `ccc` (charge −3) it gives the 10 and the 5bar of the line at `u = −3`.
(ii) An operator of total `U(1)_N` charge `q` changes the matter number by `q`, so it acts on the matter of at least `⌈|q|/5⌉` sites. On the line, the 5bar and singlet carriers have `|q| ≥ 9` and `|q| ≥ 15`, so they act on at least two and three sites.
(iii) An operator carried at one site `y` has `|q_y| ≤ 5 + 6w(m)`, with `w(m) = min(m, 10 − m, 5)`. For `m ∈ {1, 9}` this bound is 11. So for `m ∈ {1, 9}` no space carried at one site realizes the line's singlet, and R-M at one site (CG1K's definition) cannot give an anomaly-free family. The total-charge composite `D_x^†D_y^†D_z^†`, with `D_x = c^†_{x,1}⋯c^†_{x,5}`, is a gauge-covariant `SU(5)` singlet of total charge −15 for every `m`.

*Proof.* (i) For a link `ℓ = (x, y)` put `V_{ℓ,j} = (Σ_k c^†_{x,k}r^{ℓ,x}_k) r^{ℓ,y†}_j`. `LW1_5U_DRAFT.md` line 48: "Matter creators and `x`-end rishon creators both transform as `5`." So the bracket is `U(5)_x`-invariant with `q_x = 0`, and `r^{ℓ,y†}_j` makes `V_{ℓ,·}` a 5 at `y` with `q_y = 1`. It is fermion odd: one matter factor, and the rishon bilinear is in the link algebra. It is nonzero: take `p_{ℓ,x} = max(1, m − 4)`, which lies in `[1, min(5, m)]` and makes `p_{ℓ,y} ≤ 4`; on a basis state with rishon flavour 1 present at the `x`-end, flavour `j` absent at the `y`-end and matter flavour 1 empty at `x`, the `k = 1` term is nonzero and the other terms give orthogonal vectors. Take four links `ℓ_1, …, ℓ_4` at `y` with distinct far ends. For a 4-subset `J` let `A_J` be the antisymmetrized product `Σ_σ sgn σ ∏_iV_{ℓ_i, j_{σ(i)}}`. The terms act on distinct tensor factors with distinct flavour labels, so they are linearly independent and `A_J ≠ 0`. The `A_J` span `Λ^4(5) ≅ 5bar ⊗ det` at `y` (wedge pairing with `Λ^1`; Lemma E). Multiply by `D_y`, which is `det` at `y` (`Γ(u)D_yΓ(u)^* = det(u)D_y`) and acts on `y`'s matter, a separate factor. The result is `5bar ⊗ det^2`, charge `5 + 4 = 9`. Parity: `D_y` is odd and the four `V`'s are even together. (ii) Lemma Z-U(i): "`Σ_xq_x(O)` is the change of total matter number that `O` makes". Each site's `N_x` lies in `{0, …, 5}`. On the line `|b| = 3|u| ≥ 9` and `|c| = 5|u| ≥ 15` (S2-5(iv)). (iii) `Q_y = N_y + Σ_{ℓ∋y}p_{ℓ,y}`. `N_y` ranges over an interval of width 5, and each `p_{ℓ,y}` over `[max(0, m−5), min(5, m)]`, of width `w(m)`. A nonzero `O` with `[Q_y, O] = q_yO` maps one eigenvalue to another, so `|q_y|` is at most the total width. Carried at `y` means `q_z = 0` for `z ≠ y`, so `q_y = q`. The last sentence: each `D^†` is `det^{−1}` at its site. ∎

[check] (8): `5 + 6w(m)` is `11, 17, 23, 29, 35, 29, 23, 17, 11` for `m = 1, …, 9`.

### 4.4 Which anomalies the light spectrum must cancel

If the group `G_∞` stays unbroken at long distance, the conditions are the perturbative anomaly coefficients of `G_∞` on the light Weyl content:
- `G_∞ = Spin(10)` (`L5-O`): none (Lemma O-A).
- `G_∞ = U(5)` (`L5-U`, or `L5-O` broken to a Case I `U(5)`): `SU(5)^3`, `U(1)_N SU(5)^2`, `U(1)_N^3`, `U(1)_N`-gravitational. On one family the first is automatic and the other three hold exactly on the line (Theorem U-A).
- `G_∞ = SU(5)`: `SU(5)^3`, automatic.
- `G_∞ = H`: the five conditions of S3-5(iv), automatic for `F_t`.
Global anomalies are not treated for any `G_∞`.

### 4.5 The outside input and the verdicts

**AM-5 (anomaly matching for an unbroken exact subgroup; outside the working set; not proved).** Let `U` be an update of `L5-O` or `L5-U` form, possibly with further gauge-invariant gates. Let `ω` be stationary and invariant under `G_U` and gauge transformations. Let `G_∞ ⊂ G` be closed and connected, with its gauge field massless at long distance (a continuum notion; not defined on the lattice here). Suppose hypothesis IR holds with fields `ψ_i` in irreducible `G_∞`-representations `R_i`. Then every perturbative anomaly coefficient of `G_∞` vanishes on `{(R_i, χ_i)}`.

*Status.* For quasi-free `U` and `ω` with a preserved maximal torus it is Lemma V, proved. For interacting updates it is the standard principle (an exactly gauge-invariant regularization has zero total anomaly; symmetrically gapped sets carry none). It fails as a lattice theorem at the same step as CH1's Lemma AM: step (c), the adiabatic flux insertion, line 303: "Step (c) fails as a lattice theorem." It says nothing about broken generators.

**Verdict on `L5-O`.** Under AM-5 with `G_∞ = Spin(10)`: no anomaly condition. With `G_∞ ⊊ Spin(10)`: the `G_∞` ledger of 4.4. Anomalies exclude nothing on `L5-O` beyond what the `L5-U` ledger excludes for a `U(5)`-type `G_∞`.

**Verdict on `L5-U`.** Under AM-5 with `U(1)_N ⊂ G_∞ = U(5)` unbroken:
- Every realization of one family off the line is excluded. That includes the one-site realization `c`, `ccc`, `c^5` (`(−40, −400, −5)`). This is a named step: **Theorem U-A(iii) with AM-5.**
- Realizations on the line are not excluded. They exist as local operators (Lemma U-T(i), and the total-charge singlet of (iii)). Every member is then a composite: the 10 changes matter number by `|u| ≥ 3`, the 5bar by `≥ 9`, the singlet by `≥ 15`. For `m ∈ {1, 9}` the singlet cannot be carried at one site.
- So **`L5-U` with unbroken `U(1)_N` and a one-family light spectrum is not excluded under AM-5.** What AM-5 fixes is the realization: the light family's `U(1)_N` charges must be `u(1, −3, 5)`, `|u| ≥ 3`.
With `U(1)_N` broken at long distance, AM-5 does not apply to `U(1)_N`. The `SU(5)` and `H` conditions hold for the one-site family. Whether an anomalous light set under a broken generator is consistent needs a further continuum input (Wess-Zumino terms; D'Hoker and Farhi, from memory, not load-bearing), which this draft does not use.

**Extra light states cannot cancel the one-site anomaly within CH1(a).** The mixed coefficient `−5` gets contributions only from `SU(5)` non-singlets. A nontrivial `SU(5)` representation is nontrivial on `su(3) ⊕ su(2)`: `su(5)` is simple, so the representation is faithful on it. So the cancelling states carry Standard Model charges, and CH1(a)'s "no extra light charged state" fails.

### 4.6 Changes considered, and the four-test check

Tests: (1) states or fixes a part's target; (2) open-ended; (3) settles a downstream question by premise; (4) adds structure its reasons do not need. Nothing is adopted. **No change is proposed:** the law already allows anomaly-free realizations (Lemma U-T), so every law change below would add structure its reason does not need.

| Option | (1) | (2) | (3) | (4) | Result |
|---|---|---|---|---|---|
| (a) Break `U(1)_N` at long distance, as a premise | fails: it is EW1/VC1's target (CG1K-H) | pass | fails: it settles the breaking pattern by premise | pass | rejected as a premise; it remains a possible outcome of VC1 |
| (b) Add light states that cancel the anomaly | fails: CH1(a) says "no extra light charged state", and the mixed term forces charged ones (4.5) | fails unless their content is fixed | fails | fails | rejected |
| (c) Register or link change so that only `SU(5)` is exact (for example a `det`-type rishon term) | fails: it fixes GA1's answer to meet CH1's "gauge anomalies cancelling" | pass | fails: it settles CH1's anomaly by premise | fails: the line realization exists without it | rejected |
| (d) The light family is carried on the line of S2-5(iii) | not a choice: under AM-5 it is a consequence of CH1(a)'s own words with `U(1)_N` unbroken | — | — | — | recorded as a condition on CH1-5U-i |

---

## 5. CH1's first open input on each law

### 5.1 `L5-U`: CH1-5U-i

**Lemma CH1-5U-i (open).** There exist
(a) an update `U` of `L5-U` form (the tick of `LW1_5_DRAFT.md` section 8.1 with rishon registers of some `m`, plus finitely many layers of gauge-invariant site or cell gates, the kind PS-8 names), covariant under `G_U`, and
(b) a state `ω`, stationary under `U` and invariant under `G_U` and gauge transformations,
such that hypothesis IR holds with light left-handed Weyl fields that are exactly `10 ⊕ 5bar ⊕ 1` of `SU(5)`, with `U(1)_N` charges `u(1, −3, 5)`, `u = 5k + 2`, `k` odd (case A, `Y ∈ su(5)`), or the flipped `B_k` assignment; with `U(5)` unbroken at long distance and every other fermion-odd excitation gapped.

*Why this one.* It is CH1(a) as worded, "invariant under `G`" with "the gauge field kept massless", for `G = U(5)`. Under AM-5 the charges are forced (Theorem U-A(iv)). The mirror of this set is anomaly free, so anomalies do not forbid its symmetric gapping.

*On file.* Proposition F (one-site carriers `c`, `ccc`, `c^5`). Theorem U-M (the `U(5)` multiplet structure). Lemma U-T (line carriers exist; their sizes). F3 and K1-5 (free and quasi-free exclusions). #10004 (a 16-Weyl `Spin(10)` toy, "Survival of the K gap as L -> infinity is not established: inconclusive"; it is not `U(5)` and not on the cube tick). #9992 (release in a sign-free toy).
*Not on file.* Any lattice or numerical evidence that a `U(5)`-invariant interaction gaps the mirror of `10_u ⊕ 5bar_{−3u} ⊕ 1_{5u}`. Any evidence that composites of 9 and 15 elementary fermions can be light. A global-anomaly analysis for this content. A proof of AM-5.

*Attack 1, free.* Take `U` quasi-free and `ω` a quasi-free sea. *Fails:* Lemma V. The light content is vector-like in every weight sector. Also, by K2-5 there is no light 10 or singlet at all.
*Attack 2, PS-8 on the elementary content.* Keep the left-handed elementary 5's light and gap the right-handed ones. *Fails:* at every quasi-free endpoint by K1-5 (partners released in each flavour sector; proved). In general the kept set is anomalous by K2-5(U), and AM-5 excludes it. The target needs the 10 and the singlet, which are not elementary.
*Attack 3, one-site composites.* Use `ccc`, `c`, `c^5` at each site as the family. Gap the mirror symmetrically with `U(5)`-invariant multi-fermion site gates (the Eichten-Preskill route, now with no layout problem, by C3-5). *Fails:* the set is off the line. Its `U(1)_N` anomalies are `(−40, −400, −5)` (Theorem U-A(iii)), so under AM-5 it cannot be the light content with `U(5)` unbroken.

*What would settle it.* True: a mechanism that binds the twisted carriers into light chiral states and gaps the mirror, with a proof of IR. False: a theorem that every light fermion of an invariant stationary state of an `L5-U` law has `|U(1)_N| ≤ 5`, or is carried at one site; under AM-5 that would rule out the line. The next test to run, guidance only: exact diagonalisation of a small 1+1D five-mode chain with `U(5)`-invariant on-site interactions, to see which fermion-odd site composites are lightest.

### 5.2 `L5-O`: CH1-5O-i

**Lemma CH1-5O-i (open).** There exist an update `U` of `L5-O[S_+]` form, plus finitely many layers of gauge-invariant gates, covariant under `G_U`, and a stationary state `ω` invariant under `G_U` and gauge transformations, such that, for one Case I embedding with `α` even:
(a) `Spin(10)` is broken at long distance to a closed `G_∞` with `H ⊆ G_∞ ⊊ Spin(10)` (this is CG1K-H);
(b) hypothesis IR holds with light left-handed Weyl fields whose `H`-content is exactly `F_t`, with every other fermion-odd excitation gapped, including the non-family components of the parents `10`, `120`, `252`;
(c) if `U(1)_N ⊂ G_∞`, the family's `U(1)_N` charges are on the line of S2-5(iii) (forced under AM-5).

*Why this one.* CH1(a) as worded with `G = Spin(10)` unbroken fails at S3-5(iii) (Theorem O-M under R-M; Theorem K for the 16). So on `L5-O`, CH1 cannot be posed without breaking. Clause (a) is CG1K-H, and it comes first.

*On file.* Theorem K and Lemma F (matter is tensor class). Theorem O-M. Theorem O-I and Proposition F (the family's members as one-site operators, with `α` even). Lemma O-A (no anomaly condition from `Spin(10)`).
*Not on file.* Any breaking mechanism `Spin(10) → G_∞` in a gauge-invariant state of `L5-O` (VC1). Any `H`-symmetric gapping of the non-family partners. Any substitute for #10014's protection of the 16, which does not transfer (`LW1_5O_DRAFT.md` section 2.6).

*Attack 1, free.* *Fails:* Lemma V and Remark F-N. Free content is vector-like per weight sector, and without a preserved torus F3 says nothing.
*Attack 2, PS-8 on the elementary content.* *Fails:* K2-5. The elementary content is the real 10. It takes a `Spin(10)`-invariant Majorana mass and contains no `(3, 2)`.
*Attack 3, `Spin(10)`-symmetric gapping of `16 ⊕ 16bar`.* This is the classic route (Wang and Wen; Razamat and Tong; from memory, not load-bearing). *Fails:* Theorem K. No fermion-odd local operator of `L5-O` is a 16, so the route's light field does not exist on this law.

*What would settle it.* First CG1K-H: a gauge-invariant stationary state of `L5-O` whose long-distance gauge group is a proper subgroup `G_∞ ⊇ H`. Without it, CH1 on `L5-O` has no well-posed target under R-M.

---

## FINISH

**Proved here (pass 1, not refereed).**
- Remark F-N: F1, F2 hold for Majorana quasi-free gates; under particle-hole symmetry the pockets at `k_0` and `−k_0` have opposite charges, so F3's Nambu total is automatic and F3 has content only per weight sector of a preserved torus.
- Lemma S1-5: on `L5-U`, and on `L5-O` with irreducible registers, fermion parity is `(−1)^{U(1)_N}`; every neutral excitation is a boson.
- Theorem S2-5: `U(1)_N` is not `Y` or `Q_em`; on a `U(5)`-multiplet family, `U(1)_N ∈ span{Y, B−L}` exactly on the line `u(1, −3, 5)` (`uX` in case A, `uX'` in `B_k`); `u` odd, `u ≡ ±2 mod 5`, `|u| ≥ 3`; parity excludes no point of the line.
- Theorem S3-5: the exact group is non-abelian; CH1(a) with `G` unbroken fails on `L5-O` (O-M under R-M; K for the 16) and is open on `L5-U`; the `H` ledger of `F_t` vanishes.
- Lemma C2-5: one-site triples are exact modes on their invariant subspace; the ten triples are never ten CAR modes at a site.
- Theorem K1-5 and Lemma K2-5: endpoints release partners per weight sector; on `L5-U` an elementary chiral set is anomalous; on `L5-O` it is the real 10, anomaly free and massable, and on both `Q`, `u^c`, `e^c`, `ν^c` are composites.
- Lemma V: free light content of either law is vector-like in every weight sector, so all its perturbative anomalies vanish.
- Lemma O-A: `Spin(10)` has no perturbative anomaly in any representation.
- Theorem U-A: the `U(5)` ledger of one family; `(−40, −400, −5)` for the one-site carriers; all zero exactly on the line; `B_k` always on it; no anomaly-free family without `ν^c`.
- Lemma U-T: twisted carriers exist (`5bar ⊗ det^2` at one site for every `m`); line carriers act on at least 1, 2, 3 sites; for `m ∈ {1, 9}` the line's singlet is not carried at one site.

**Counterexamples.**
- To K2 on `L5-O` ("both nonzero"): two left-handed Weyl 10's, anomaly free under `Spin(10)` (Lemma O-A).
- To "a one-family `L5-U` spectrum with unbroken `U(1)_N` needs `U(1)_N` broken or extra light fields" (CG1K line 198): the line realization at `u = −3`, with charges `(−3, 9, −15)` on `(10, 5bar, 1)`, is anomaly free and is carried by local operators (Theorem U-A(iv), Lemma U-T).
- To "light `U(1)_N`-charged fields can cancel the one-site anomaly within CH1(a)": the mixed term needs `SU(5)`-charged, hence Standard Model-charged, states (4.5).

**Open, by name.**
- **CH1-5U-i** (5.1), three attacks failed: free (Lemma V), PS-8 on the elementary content (K1-5, K2-5 with AM-5), one-site composites (Theorem U-A(iii) with AM-5).
- **CH1-5O-i** (5.2), three attacks failed: free (Lemma V, Remark F-N), PS-8 on the elementary content (K2-5), `Spin(10)` gapping of `16 ⊕ 16bar` (Theorem K). Its clause (a) is CG1K-H.
- **AM-5**, the outside input. Proved for quasi-free updates (Lemma V); the interacting case fails at CH1 Lemma AM's step (c).
- Inherited, unchanged: CH1-ii, reflection positivity, CG1-i, CG1-ii, CG1K-H, CG1K-loc, LW1-5-BG, LW1-5-X.

**Named failing steps for `L5-O` or `L5-U`.** None for either law. Two routes fail at named steps, and neither is a failure of the law:
- `L5-O`: CH1(a) read with `Spin(10)` unbroken fails at Theorem O-M (under R-M) and, for "one Weyl 16", at Theorem K. Under R-B the law stays live.
- `L5-U`: the one-site family with `U(1)_N` unbroken fails at Theorem U-A(iii) under AM-5. For the register data `m ∈ {1, 9}`, the line realization read with R-M at one site also fails, at Lemma U-T(iii). For `m ∈ {2, …, 8}`, and for carriers spread over several sites at every `m`, the line realization is open, so the law stays live.

**What CH1 needs next.**
1. On `L5-U`: whether light chiral states can carry the line charges `u(1, −3, 5)`, `|u| ≥ 3`, or whether VC1 breaks `U(1)_N`. Either answer changes CH1-5U-i's target. The cheapest guide is the small 1+1D five-mode exact diagonalisation of 5.1.
2. On `L5-O`: CG1K-H first. CH1-5O-i has no target until `Spin(10)` breaks to some `G_∞ ⊇ H`.
3. AM-5 for interacting Floquet updates, if a step is to rest on it as a theorem.

**Corrections to carry into other parts.**
- CG1K section 5 (line 198): the alternatives "`U(1)_N` broken at long distance, or other light `U(1)_N`-charged fields" omit the line realization. The second alternative needs Standard Model-charged states, which CH1(a) forbids.
- `LW1_5_DRAFT.md` line 430: "`U(1)_N` charges proportional to `(1, 3, 5)`" holds for the one-site carriers only. Twists change it, and the anomaly-free values are `u(1, −3, 5)` on `(10, 5bar, 1)` (up to the operator-versus-adjoint sign).
- CH1 section 4.4 lists the 16 with its `X` charges at `u = 1` as an anomaly-free target. On `L5-U` (and `L5-O` broken to `U(5)`), `u = 1` is excluded by `U(5)` integrality; the smallest is `|u| = 3`.

**Inputs from outside the working set.** AM-5 (named, not proved). The two laws of `LW1_5_DRAFT.md` section 8.1 and the results cited by name in the head. Standard mathematics rebuilt in the text: Chern-number sign rules under conjugation, complement and reflection; weight-sector grouping; even-sign-change averaging of cubics; anomaly arithmetic; the rishon transport operator. Cited, not rebuilt: the maximal torus theorem (conjugacy into a Cartan subalgebra), simplicity of `so(10)` and `su(5)`, simplicity of the CAR algebra of ten modes. Literature credited from memory, never load-bearing: Eichten and Preskill; Wang and Wen; Razamat and Tong; D'Hoker and Farhi; Georgi-Glashow and flipped `SU(5)` (only to name assignments).
