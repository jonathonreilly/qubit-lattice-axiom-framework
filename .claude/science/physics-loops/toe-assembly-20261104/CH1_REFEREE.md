lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CH1 referee report (pass 3)

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort). It is pass 3, the referee, of part CH1 under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen. This session wrote neither pass 1 (`CH1_DRAFT.md`, `CH1_5_DRAFT.md`, `CG1_KILL_DRAFT.md`) nor pass 2 (`CH1.md`). This is one check: one whole-part, line-by-line read of `CH1.md`. It reviews no other review.

**What this file is.** A referee report. It grants no status, adopts no reading and changes no axiom or working-set entry. `CH1.md` is not edited; section 4 lists the edits for the lead. Verdicts: CORRECT; ERROR (a false line, quoted, with its fix); INCOMPLETE (a named missing step). A note under a CORRECT verdict marks a compressed step or a wording fix, not a defect in the claim. A referee closure is a complete short proof of a missing step, written out here. "[check]" marks a small scratch computation (`/tmp/toe-ch1ref/check_ch1ref.py`, output `out.txt`; about 4 s, 58 MB peak, floating point and exact rationals). A check guides and never proves.

**Source revisions read.** Local checkout of branch `claude/toe-assembly` at commit `beb68f037c` (the commit that adds `CH1.md`). No other branch was read.

| File | Last commit touching it | SHA-256 (first 12) |
|---|---|---|
| `CH1.md` (the text refereed) | `beb68f037c` | `c996e8856c01` |
| `CH1_DRAFT.md` | `b913d2d2e` | `745efe8aafa6` |
| `CH1_5_DRAFT.md` | `a8a208fdf` | `879002bdde3b` |
| `CG1_KILL_DRAFT.md` | `f67931a5e` | `46ce7c0695ef` |
| `TOE_ASSEMBLY.md` | `7d2b20d29` | `8027d9d44eb5` |
| `LW1.md` (frozen) | `da0ec1934` | `66d67e6609ee` |

Full SHA-256 of `CH1.md`: `c996e8856c01f13793d736a7dc7660d3446c98362a2933cb6cec1e1fe601675f`. The seven hashes `CH1.md` records at its line 13 equal the hashes of the files at this commit [check: `shasum -a 256`].

**Files read, by line.** `CH1.md` 1-173 (all). `CH1_DRAFT.md` 1-453 (all). `CH1_5_DRAFT.md` 1-311 (all). `CG1_KILL_DRAFT.md` 1-252 (all). `LW1.md`: full reads of lines 1-12, 312-336 (B10) and 361-375 (C1); grep hits at lines 16, 44-47, 113, 141, 150, 199, 205, 231-245, 391, 415, 492 and 502 (A2, B4, B5). `LW1_5U_DRAFT.md` 40-62 (the `L5-U` register and `Q_x`). `LW1_5_DRAFT.md` 252-258 (Theorem U). `TOE_ASSEMBLY.md`: grep hits at lines 86, 90, 146, 184, 399, 401, 410 and 599 (PS-8 row, PS-7r, CH1 (a), (b), (e)). `LW1_REFEREE.md` 1-80 and `Y2W_DRAFT.md` 1-40, for format only. `AGENTS.md` and `docs/ai_methodology/SCIENCE_WORKFLOW.md`. Not read: `LIT_SMG.md` and `LIT_HIGGS.md` (hashes only), `LW1_5O_DRAFT.md`, the B5B files, `docs/MINIMAL_AXIOMS_2026-06-29.md`.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws and the readings R-B, R-M, R-F are read plainly. No reading is proposed. One definition change (def 4′, section 2.1) is recorded with its four-test check and is not adopted.

**Working set used, by name.** PS-7r, only to check definition 2 against `TOE_ASSEMBLY.md` line 184. PS-1c, through `LW1.md` A2 (site transitivity), for C3. PS-6 and PS-6r (finite link registers), for GAP C2, Lemma U-T and Lemma U-T′. PS-5 (the five-mode fallback), through the law `L5-U`: `LW1_5_DRAFT.md` Theorem U and `LW1_5U_DRAFT.md` section 1.1. PS-8 only as the law to test, never as a premise. Results used, by name: `LW1.md` A2, B4, B5(a), GAP B5(b), B10 and C1; the results of `CH1.md` as checked below.

**Inputs from outside the working set.** The `L5-U` register and Gauss generator (`LW1_5U_DRAFT.md` section 1.1: register `Λ^m(C^{10})`, `Q_x = N_x + Σ_{ℓ∋x} p_{ℓ,x}`, end rishon creators transforming as `5`). They are provisional pass-1 inputs, as `CH1.md` line 11 says. Standard mathematics rebuilt in the text: Weyl's eigenvalue inequality for Hermitian `2 × 2` matrices, connectedness of a punctured ball in `R^3`, the transformation of an `ε`-contraction under `U(5)`, Jordan-Wigner signs, row reduction. Cited, not rebuilt: nothing beyond what `CH1.md` line 11 already names. Literature, from memory and never load-bearing: the anomaly-free `U(1)'` charges of one family with `ν^c` are combinations of `Y` and `B − L` when the Standard Model group is unbroken (a standard computation; for example Appelquist, Dobrescu and Hopper, Phys. Rev. D 68 (2003) 035012). Proposition AN (section 3.2) rebuilds it.

**Method.** Every proof in `CH1.md` was re-derived by hand. Where `CH1.md` cites or corrects a pass-1 source, the cited source text was read at the line given in the table notes. Each GAP gets a verdict (real or not) and, where possible, a repaired statement with its proof.

**Counts.** 80 items: 76 CORRECT, 2 ERROR, 2 INCOMPLETE. Neither ERROR is in a theorem's statement or proof: one is a false remark about a source (item 75), one a false reason inside an open target (item 79). Three referee closures: Lemma ST (closes GAP F3a/F4, critical tilt included), Lemma U-T′ with Corollary U-T″ (closes GAP U-T), Proposition AN (repairs item 79). One sharpening, Lemma B (GAP CG1K-loc). Two GAPs are real and need no repair (C2, O-M). One stays open by name (CG1K-loc).

---

## 1. Verdict table

Line numbers refer to `CH1.md` at SHA-256 `c996e8856c01…`. Each theorem's statement and its proof are separate items. The nine distiller definitions are nine items.

| # | Item (CH1 line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status paragraph (5) | CORRECT | |
| 2 | §0 "Proved below" list (7) | INCOMPLETE | K2, Lemma V and Lemma U-T are proved in the text and missing from the list. Theorem F, O-M and U-M are covered only by "Representation results from CG1". Edit R5. |
| 3 | §0 "Open" list (9) | CORRECT | B5(b) of `LW1.md` also bears on line 73; it is carried as inherited (section 5). |
| 4 | §0 outside inputs (11) | CORRECT | |
| 5 | §0 provenance (13) | CORRECT | The seven hashes match [check]. |
| 6 | Def 1, periodic free update (17) | CORRECT | |
| 7 | Def 2, quasienergy, cuts, sea (18) | CORRECT | Matches PS-7r, `TOE_ASSEMBLY.md` line 184: "It is defined when `pi` lies in a gap." |
| 8 | Def 3, pocket decomposition and charge (19) | CORRECT | `c` is the first Chern number of `ran P` on the sphere. |
| 9 | Def 4, regular Weyl node (20) | INCOMPLETE | Two specifications are missing. `t` must be a linear form. The link between `h` and `U` must be stated: on the pair, `e^{ia}U(k_0+q) = exp(−ih(q))` up to second order in `q`. "Lower band", and so the sign in F3a, depend on it. The tilt bound is sufficient, not necessary (section 2.1). Edit R6. |
| 10 | Def 5, charge and weight sectors (21) | CORRECT | |
| 11 | Def 6, definite charge, parity (22) | CORRECT | |
| 12 | Def 7, carried at `y`; R-F, R-B, R-M (23) | CORRECT | Matches `CG1_KILL_DRAFT.md` lines 43-48. |
| 13 | Def 8, IR (24) | CORRECT | |
| 14 | Def 9, `G_∞` (25) | CORRECT | |
| 15 | `W_1`, `W_3` normalization (29) | CORRECT | |
| 16 | Theorem F1 (31) | CORRECT | |
| 17 | F1 proof (33) | CORRECT | |
| 18 | Theorem F2 (35) | CORRECT | |
| 19 | F2 proof (37) | CORRECT | Note: compactness keeps the spectrum a fixed distance from the omitted point. That makes the logarithm continuous. |
| 20 | Theorem F3 (39) | CORRECT | |
| 21 | F3 proof (41) | CORRECT | The smoothing sentence repairs a step the draft skipped: `dΩ` needs `P` in `C^2`. |
| 22 | Lemma F3a, Corollary F3b (43) | CORRECT | Under def 4. |
| 23 | F3a and F3b proof (45) | CORRECT | Chern additivity is credited at line 11. |
| 24 | GAP F3a/F4, tilt (47) | CORRECT | GAP real as a missing step. Lemma ST closes it, critical tilt included (section 2.1). |
| 25 | Theorem F4 (49) | CORRECT | |
| 26 | F4 proof (51) | CORRECT | |
| 27 | Theorem K1 (53) | CORRECT | Note: by def 5 a charge block is invariant under `P_l` as well. The proof's "preserve the blocks" uses this; K1 should say it. |
| 28 | K1 proof (55) | CORRECT | Any `c > 0` works. |
| 29 | Limits paragraph (57) | CORRECT | Particle-hole sign rederived: `C P(k) C^{-1} = 1 − P(−k)` gives `c_{−k_0} = −c_{k_0}`. |
| 30 | §3 setting (61) | CORRECT | `LW1.md` A2 (line 199: "The action on sites is transitive") and the Gauss law with charge 1 (line 45). |
| 31 | Lemma S1 (63) | CORRECT | |
| 32 | S1 proof (65) | CORRECT | |
| 33 | 3-4-5-0 and normalization remarks (67) | CORRECT | |
| 34 | Theorem S2 (69) | CORRECT | |
| 35 | S2 proof (71) | CORRECT | |
| 36 | Consequences of S2 (73) | CORRECT | Note: the draft's S3 was conditional ("read with `G` the exact gauge group of `L_cube`", `CH1_DRAFT.md` line 261) and rested on B5 for cell frames. "Unconditional ... for every possible reading" overstates it. The conclusion stands: frozen `LW1.md` keeps B5(b) open (line 492). |
| 37 | Lemma C2 (75) | CORRECT | |
| 38 | C2 proof (77) | CORRECT | |
| 39 | GAP C2 (79) | CORRECT | GAP real. The draft's sentence is false (section 2.2). |
| 40 | Lemma C3 (81) | CORRECT | |
| 41 | C3 proof (83) | CORRECT | Note: write the class count. A cluster's `s` sites lie in distinct classes, since otherwise a translate of the cluster meets it and so equals it. Different orbits use disjoint classes. Transitivity is not needed once the sizes are equal. |
| 42 | K2 (85) | CORRECT | |
| 43 | Elementary content paragraph (87) | CORRECT | Note: the import comes from `CH1_DRAFT.md` line 281, which quotes `LW1_DRAFT.md` 7.2 (#10016). Frozen `LW1.md` proves only B10 and C1: at `μ = 0` the cut-0 set is `K = 0`, where `V(0) = I` (line 336), an eightfold point. The regular-node results do not apply there; F3 does. Edit R7. |
| 44 | CH1-C1 and CH1-C3 (89) | CORRECT | Open; three attacks named. |
| 45 | AM (91) | CORRECT | Outside input. |
| 46 | §4 setting (95) | CORRECT | |
| 47 | Lemma S1-5 (97) | CORRECT | Note: define "homogeneous" (a definite charge at each site), as `CH1_5_DRAFT.md` line 41 does. |
| 48 | S1-5 proof (99) | CORRECT | On the provisional LW1-5 inputs that line 11 names. |
| 49 | Lemma C2-5 (101) | CORRECT | |
| 50 | C2-5 proof (103) | CORRECT | |
| 51 | Lemma V (105) | CORRECT | |
| 52 | V proof (107) | CORRECT | |
| 53 | `F_t` and the standard embedding (111-115) | CORRECT | Note: bracket `(1,1)_0` as optional, as `CG1_KILL_DRAFT.md` line 40 does. U-M and O-M speak of 15 or 16 dimensions. Edit R8. |
| 54 | Theorem F (117) | CORRECT | Hypercharges `1/3, −1/2, 1/6, −2/3, 1, 0` rederived. |
| 55 | Theorem F proof (119) | CORRECT | |
| 56 | Theorem O-M (121) | CORRECT | |
| 57 | O-M proof (123) | CORRECT | [check] The smallest `W(D_5)` orbit of a `(3,2)` weight has 40 elements. |
| 58 | GAP O-M, scope (125) | CORRECT | GAP real as a scope statement (section 2.3). |
| 59 | Case I criterion (127, first three sentences) | CORRECT | Note: "requires and abstract tensor powers supply integers" should read "occurs, in an abstract tensor-class representation of parity `(−1)^ε`, if and only if there are integers". |
| 60 | Fermion-odd family exactly when `α` is even (127) | CORRECT | The shift `3(β, −α)` checked member by member. |
| 61 | GAP CG1K-loc (127) | CORRECT | GAP real. Lemma B sharpens it; it stays open (section 2.4). |
| 62 | Theorem U-M (129-133) | CORRECT | [check] Case B formulas at `k = −3, …, 3`. |
| 63 | U-M proof (135) | CORRECT | Note: two one-line reasons to write. The second `(3bar,1)` of `F_t` needs a five-weight orbit, because singlets cannot supply it. The orbit of `(l,l,l,l,l+1)` gives a `(3,1)`, which `F_t` lacks. |
| 64 | Embedding facts (137) | CORRECT | Summary of `CG1_KILL_DRAFT.md` Lemma C and Lemma C-U. |
| 65 | Lemma O-A (141) | CORRECT | |
| 66 | O-A proof (143) | CORRECT | |
| 67 | Elementary content ledger (145) | CORRECT | |
| 68 | Theorem U-A (147-151) | CORRECT | [check] `(−40, −400, −5)`. Note: here `a, b` are `U(1)_N` charges; in U-M they are hypercharge block values. |
| 69 | U-A proof (153) | CORRECT | |
| 70 | The line as `uX` and `u[4Y+(B−L)]` (155) | CORRECT | Note: `α, β` here are the coefficients of `Y` and `B − L`, not S2's and not Case I's. |
| 71 | Subgroup ledger of `F_t` (157) | CORRECT | The five sums rederived. |
| 72 | Lemma U-T (159) | CORRECT | |
| 73 | U-T proof (161) | CORRECT | [check] The `5bar ⊗ det^2` operator is nonzero for `m = 1, …, 9`. |
| 74 | GAP U-T, first four sentences (163) | CORRECT | GAP real. Lemma U-T′ and Corollary U-T″ close it (section 2.5). |
| 75 | GAP U-T, last sentence (163) | ERROR | Section 3.1. |
| 76 | AM-5 (165) | CORRECT | Outside input. |
| 77 | CH1-5U-i (169) | CORRECT | Open; three attacks named. |
| 78 | CH1-5O-i, all but one clause (171) | CORRECT | Open. |
| 79 | CH1-5O-i: "the mixed `SU(5)^2U(1)` condition also needs the relevant unbroken `SU(5)` and multiplet assumption" (171) | ERROR | Section 3.2. |
| 80 | Closing paragraph (173) | CORRECT | |

---

## 2. The distiller's GAPs

### 2.1 GAP F3a/F4 (tilt), line 47

`CH1.md`: "The draft's definition allows arbitrary \(t\), but its proof assumes the two eigenvalues straddle the cut. ... The regular-node condition above repairs the proof. Critical tilt is not resolved by that argument."

**Verdict: real, as a missing step. No draft statement is false.** The draft's proofs use straddling without deriving it. `CH1_DRAFT.md` line 175: "If `a = 0`, the filled member (quasi-energy in `(-pi, 0)`) is `e < 0`, the lower band of `h`". Line 200: "the upper eigenvalue gives `H = a + O(eps)`, and the lower one gives `H = a + 2pi - O(eps)`". The distiller's example `h(q) = 2q_3 I + q·σ` is right about straddling. But it meets none of the draft's hypotheses, because each one forces the node to be isolated. F3a (line 173): "Take `B_j` so small that `B_j` meets no other point of `N_0 ∪ N_pi`". F3b (line 177): "If the cut-`0` and cut-`pi` points are all linear Weyl nodes". F4 (line 195): "Let the cut `a` have finitely many points, all linear Weyl nodes". The example has a cone of cut points through the node. No ball meets only the node; the cone points are simple crossings, not nodes; the cut set is infinite. The missing step is that isolation forces straddling. Lemma ST proves it.

**Setting.** `U : T^3 → U(n)` is `C^2` and `a ∈ {0, π}`. A *linear Weyl node* at the cut `a` is a point `k_0` where `e^{−ia}` is an eigenvalue of `U(k_0)` of multiplicity exactly two and, in a `C^2` orthonormal frame of the two-dimensional Riesz subspace near `k_0`, `e^{ia}U(k_0+q) = exp(−ih(q))` with `h` Hermitian, `h(q) = t(q)·1 + (Mq)·σ + R(q)`, `t` linear, `det M ≠ 0` and `‖R(q)‖ ≤ C|q|^2` for `|q| < r_0`. Then the pair's quasienergies are `a + e_±(q)`, with `e_−(q) ≤ e_+(q)` the eigenvalues of `h(q)`.

**Lemma ST (an isolated node straddles its cut).** If `k_0` is an isolated point of `N_a`, there is `r > 0` with `e_−(q) < 0 < e_+(q)` for `0 < |q| < r`.

*Proof.* (1) Take `r ≤ r_0` so small that the other `n − 2` eigenvalues stay away from `e^{−ia}` on `B_r(k_0)`, the pair satisfies `|e_±| < 1` there, and `B_r(k_0) ∩ N_a = {k_0}`. For `0 < |q| < r`, `e_±(q) = 0` would make `e^{−ia}` an eigenvalue of `U(k_0+q)`. So neither `e_−` nor `e_+` vanishes on the punctured ball. (2) Weyl's inequality for Hermitian `2 × 2` matrices, `|e_±(h) − e_±(h')| ≤ ‖h − h'‖`, makes `e_±` continuous. (3) The punctured ball is connected. A continuous function with no zero on a connected set has one sign. So `e_−` has one sign there, and so has `e_+`. (4) The eigenvalues of `t(q)·1 + (Mq)·σ` are `t(q) ± |Mq|`. Weyl's inequality gives `|e_±(q) − t(q) ∓ |Mq|| ≤ C|q|^2`. (5) Fix a unit vector `n` and put `μ = |Mn| > 0`. Take `0 < ρ < min(r, μ/(2C))`. Linearity gives `t(ρn) + t(−ρn) = 0`. So `e_−(ρn) + e_−(−ρn) ≤ −2ρμ + 2Cρ^2 < 0`, and `e_−` is negative at `ρn` or at `−ρn`. By (3) it is negative on the whole punctured ball. Likewise `e_+(ρn) + e_+(−ρn) ≥ 2ρμ − 2Cρ^2 > 0`, so `e_+ > 0` throughout. ∎

**What it gives.**
- Lemma F3a holds at every linear Weyl node isolated in `N_0 ∪ N_π`, at any tilt. On a small sphere the filled member of the pair is `e_−` at the cut `0` and `e_+` at the cut `π`, which is what the proof uses. The lower eigenprojection there converges to that of `(Mn)·σ`, because the pair splits by at least `2|Mq| − 2C|q|^2`, whatever `t` is.
- Corollary F3b holds whenever every point of `N_0 ∪ N_π` is a linear Weyl node. Each such node is isolated in `N_0 ∪ N_π`. Near a node `k_0` at the cut `a` the pair's eigenvalues differ, so a nearby cut-`a` point would be a simple crossing, not a node. `N_{a+π}` is closed, so its points accumulate at `k_0` only if `k_0 ∈ N_{a+π}`. Then `k_0` is a node at `a + π` as well, and the same splitting isolates it there. Compactness then makes the cut set finite.
- Theorem F4 holds when the chosen cut has finitely many points, all linear Weyl nodes of any tilt. Step 2 of its proof needs exactly the straddling of Lemma ST on each small sphere.

**Critical tilt is resolved.** An isolated node with critical tilt straddles. A local example shows that the case occurs. Take `h(q) = (q_3 − q_3^3/2)·1 + q·σ`. Its linear tilt is `t(q) = q_3` and `M = 1`, so `|t(q)| = |Mq|` on the `q_3`-axis: it is not regular under def 4. For `0 < |q| < 2`: if `q_3 ≥ 0`, then `e_− = (q_3 − |q|) − q_3^3/2` is a sum of two non-positive terms that are not both zero; if `q_3 < 0`, then `e_− ≤ 2q_3 − q_3^3/2 = q_3(2 − q_3^2/2) < 0`. The case of `e_+` is symmetric. So the node is isolated and straddles. [check] On spheres of radius 0.2, 0.05 and 0.01 it straddles, and the filled-band Chern number on a sphere of radius 0.05 equals that of a regular node with tilt `q_3/2`. (A scalar term never moves the eigenprojections, so this is expected.) A node that is not isolated (over-tilted, or critical with a crossing cone) is not a single-node pocket. F3 still applies to any pocket ball that contains its whole cut set.

**Repaired statement (def 4′; recorded, not adopted).** "An *isolated linear Weyl node* is a linear Weyl node, with `t` linear and `e^{ia}U(k_0+q) = exp(−ih(q))` on the pair, that is an isolated point of `N_0 ∪ N_π`." With def 4′ in place of def 4, Lemma F3a, Corollary F3b and Theorem F4 hold as `CH1.md` states them, with its proofs plus Lemma ST. Four-test check: (1) it states no part's target; (2) it is closed, a fixed condition at one point; (3) it settles no physics question; (4) it adds no structure, since it drops the tilt bound and keeps the isolation that the proofs use. It passes all four.

### 2.2 GAP C2 (free embedding), line 79

`CH1.md`: "The draft infers that every free cluster walk embeds exactly with finite quantum links. ... finite link raising operators are not unitary and can annihilate boundary-flux states."

**Verdict: real. The draft's sentence is false.** `CH1_DRAFT.md` line 341: "Every free walk of odd-charge modes on a layout embeds exactly in the update of one-mode sites, inside the invariant subspace `H_𝒞`, with exact Gauss laws." A concrete counterexample follows the distiller's mechanism. Take clusters `S = {x}` and `S' = {y}` (size 1 is odd), adjacent and joined by one link with a spin-1/2 register: `E ∈ {−1/2, +1/2}` and `J = S^+`, so `[E, J] = J` as `LW1.md` B4 needs. Let `ψ` have `x` full, `y` empty and `E = +1/2`. The dressed hop `O = c_y^† J c_x` gives `Oψ = 0`, because `J` annihilates the top state. Also `O^†ψ = 0`, because `y` is empty. So `exp(−iτ(O + O^†))ψ = ψ`. The free hop `exp(−iτ(c_y^†c_x + c_x^†c_y))` sends the matter part to `cos τ |x⟩ − i sin τ |y⟩`. The two differ whenever `sin τ ≠ 0`. The same happens for any odd size whose dressing path runs through this link. `ψ` is a legitimate state: `LW1.md` line 47 reads gauge invariance as invariance under conjugation, not as a Gauss sector.

**Repaired statement.** C2 as `CH1.md` states it (lines 75-77): the dressed gates are gauge invariant and keep `H_𝒞 ⊗ (links)`, and their matter action depends on the link state. An exact free embedding holds for unitary c-number link factors, which PS-6r excludes. No result of `CH1.md` uses the embedding. Nothing is carried.

### 2.3 GAP O-M (scope), line 125

`CH1.md`: "This is an operator-space result under R-M, not a proof that every possible infrared one-family spectrum must break the microscopic local gauge symmetry."

**Verdict: real, as a scope statement. O-M itself is correct (items 56-57).** The scope matters for one pass-1 sentence. `CH1_5_DRAFT.md` line 259: "So on `L5-O`, CH1 cannot be posed without breaking." That holds under R-M and for operator spaces of the law's algebra only. **Repaired statement:** "Under R-M, for operator spaces of the law's algebra, CH1(a) with `Spin(10)` unbroken fails at O-M, and its 'one Weyl 16' clause at Theorem K." Nothing needs closing. The end-mixed spinor sectors stay fixed Gauss sectors, never made or moved by the law's operators (`CG1_KILL_DRAFT.md` line 167, quoting `LW1_5O_DRAFT.md` Theorem P). Whether a family can live in such a sector stays a question inside CH1-5O-i.

### 2.4 GAP CG1K-loc, line 127

`CH1.md`: "abstract tensor occurrence does not by itself establish a nonzero finite-register local operator for arbitrary tensor degree."

**Verdict: real; it stays open.** Pass 1 names it "not pursued" (`CG1_KILL_DRAFT.md` line 220). `CH1.md` line 127 states its family claim for abstract tensor representations and says so; that claim is correct (item 60). One sharpening is proved here.

**Lemma B (weight box on `L5-U`).** At a site `y` of `L5-U`, with any `m`, every `U(5)_y`-weight `w ∈ Z^5` of an operator space carried at `y` lies in `[−7, 7]^5`.

*Proof.* The diagonal generator `𝒢^{E_{jj}}_y = c_{y,j}^†c_{y,j} + Σ_{ℓ∋y} r^{ℓ,y†}_j r^{ℓ,y}_j` (`LW1_5_DRAFT.md` Theorem U) is a sum of seven commuting number operators. So its spectrum lies in `{0, …, 7}`. A nonzero `O` with `[𝒢^{E_{jj}}_y, O] = w_jO` maps the eigenspace of `λ` into that of `λ + w_j`. Both values lie in `{0, …, 7}`, so `|w_j| ≤ 7`. ∎

So `Sym^8(C^5)`, with weight `(8, 0, 0, 0, 0)`, occurs in tensor powers of `C^5` but is never carried at one site. Abstract occurrence and one-site realization differ, as the GAP says. **Open as CG1K-loc:** for each even ratio `α:β`, whether every member of `F_t` has a solution `(p_n, q_n)` of the Case I criterion whose weight lies in the box and is carried by a nonzero operator; and the `L5-O` analogue, whose register spectrum was not read here.

### 2.5 GAP U-T (singlet), line 163

`CH1.md`: "The cited construction proves the charge-9 multiplet and a total-charge singlet, not a complete \(10_{-3}\oplus\bar5_9\oplus1_{-15}\) carried at one site."

**Verdict: real for what the source proves.** `CH1_5_DRAFT.md` line 188 gives the singlet only as "The total-charge composite `D_x^†D_y^†D_z^†`", charged at three sites. Its FINISH (line 299) leaves the middle registers open: "For `m ∈ {2, …, 8}`, and for carriers spread over several sites at every `m`, the line realization is open". Lemma U-T′ settles the one-site case for those registers; Lemma U-T already settles it for `m ∈ {1, 9}`. The GAP's last sentence is an ERROR (section 3.1).

**Setting** (`LW1_5U_DRAFT.md` section 1.1 and `LW1_5_DRAFT.md` Theorem U; provisional inputs). Each link carries ten rishon modes, fermionic among themselves, in an ordinary tensor factor that commutes with matter and with other links. The register is `Λ^m(C^{10})`, so `p_{ℓ,x} + p_{ℓ,y} = m`. `Γ(u)` acts on the matter creators of a site and on the rishon creators at each incident link end by `Γ(u)c_j^†Γ(u)^* = Σ_k u_{kj}c_k^†`. `Q_x = N_x + Σ_{ℓ∋x} p_{ℓ,x}`.

**Lemma U-T′ (a one-site singlet on the line).** Let `2 ≤ m ≤ 8`. Let `y` be a site, `x_1, …, x_6` its neighbours and `ℓ_i` the link from `y` to `x_i`. Put
\[
A_i=\sum_{k=1}^5 c_{x_i,k}\,r^{\ell_i,x_i\dagger}_k,\qquad W_{i,j}=A_i\,r^{\ell_i,y}_j,
\]
\[
F_1=\sum_{\sigma\in S_5}\operatorname{sgn}\sigma\;W_{1,\sigma(1)}W_{2,\sigma(2)}W_{3,\sigma(3)}W_{4,\sigma(4)}W_{5,\sigma(5)},\qquad
F_2=\sum_{\tau\in S_5}\operatorname{sgn}\tau\;W_{2,\tau(1)}W_{3,\tau(2)}W_{4,\tau(3)}W_{5,\tau(4)}W_{6,\tau(5)},
\]
`D_y = c_{y,1}^† ⋯ c_{y,5}^†` and `O = D_y^† F_1 F_2`. Then:
(i) `Ad Γ_{x_i}(v)` fixes `O` for every `v ∈ U(5)` and `i = 1, …, 6`; the groups of all other sites `z ≠ y` fix `O`; and `Ad Γ_y(u) O = det(u)^{−3} O`.
(ii) `O` is fermion odd and lowers the total matter number by 15.
(iii) `O ≠ 0` on the Hilbert space of the law, every link in `Λ^m(C^{10})`.
So `span{O}` is carried at `y` in `det^{−3}`: the `U(5)` singlet of `U(1)_N` charge `−15`.

*Proof.* (i) At `x_i`, `c_{x_i,k} ↦ Σ_{k'} \bar v_{k'k} c_{x_i,k'}` and `r^{ℓ_i,x_i†}_k ↦ Σ_{k''} v_{k''k} r^{ℓ_i,x_i†}_{k''}`. So `A_i ↦ Σ_{k',k''} (vv^*)_{k''k'} c_{x_i,k'} r^{ℓ_i,x_i†}_{k''} = A_i`. The `y`-end rishons do not see `v`. At `y`, `r^{ℓ,y}_j ↦ Σ_{j'} \bar u_{j'j} r^{ℓ,y}_{j'}`. So `F_1 ↦ Σ_{j'_1,…,j'_5} [Σ_σ sgn σ ∏_i \bar u_{j'_i σ(i)}] ∏_i W_{i,j'_i}`. The bracket is the determinant of the matrix with rows `\bar u_{j'_i,·}`. It is zero when two `j'_i` agree, and `sgn(κ) det \bar u` when `i ↦ j'_i` is a permutation `κ`. So `F_1 ↦ det(\bar u) F_1 = det(u)^{−1}F_1`, and the same holds for `F_2`. `D_y ↦ det(u) D_y`, so `D_y^† ↦ det(u)^{−1}D_y^†`. Conjugation is an automorphism, so `O ↦ det(u)^{−3}O`. No factor of `O` sits at another site.
(ii) Each `W_{i,j}` has one matter factor and an even rishon factor, so it is odd. `F_1` and `F_2` are products of five `W`'s, so they are odd. `D_y^†` is odd. A product of three odd operators is odd. The ten `W`'s remove ten matter fermions and `D_y^†` removes five.
(iii) Choose a basis vector `ψ`. All five modes at `y` are occupied. At `x_1` and `x_6` only matter flavour 1 is occupied; at `x_i`, `i = 2, …, 5`, only flavours 1 and 2. On `ℓ_1` the `y`-end holds flavour 1 and the `x`-end lacks flavour 1. On `ℓ_6` the `y`-end holds flavour 5 and the `x`-end lacks flavour 1. On `ℓ_i`, `i = 2, …, 5`, the `y`-end holds flavours `i − 1` and `i`, and the `x`-end lacks flavours 1 and 2. Fill each register to total `m`. On `ℓ_1` and `ℓ_6` put `p_y = max(1, m − 4)` and `p_x = min(m − 1, 4)`, with `x`-end flavours from `{2, …, 5}`. On `ℓ_2, …, ℓ_5` put `p_y = max(2, m − 3)` and `p_x = min(m − 2, 3)`, with `x`-end flavours from `{3, 4, 5}`. These counts are consistent for every `2 ≤ m ≤ 8`. Let `φ` be the basis vector obtained from `ψ` by emptying the matter at `y`, emptying the occupied far-end flavours, adding `x`-end flavour 1 on `ℓ_1` and `ℓ_6` and flavours 1, 2 on `ℓ_2, …, ℓ_5`, and removing `y`-end flavour 1 from `ℓ_1`, flavours `i − 1, i` from `ℓ_i` (`i = 2, …, 5`) and flavour 5 from `ℓ_6`. Expand `Oψ` over `σ`, `τ` and the far-end sums. Each term is `±` a basis vector or zero. A term reaches `φ` only if it removes exactly the listed `y`-end flavours. On `ℓ_1` this forces `σ(1) = 1`. On `ℓ_2` it forces `{σ(2), τ(1)} = {1, 2}`, and `σ(2) ≠ σ(1)` gives `σ(2) = 2`, `τ(1) = 1`. Inductively `σ(i) = i` and `τ(i − 1) = i − 1` for `i ≤ 5`, and `ℓ_6` gives `τ(5) = 5`. So only `σ = τ = id` reaches `φ`. At `x_1` and `x_6` one far-end term survives, `k = 1`. At `x_i`, `i = 2, …, 5`, the two copies of `A_i` act. The operators between them act on other sites, on other links, or on the `y`-end of `ℓ_i`; moving one copy next to the other gives a sign that does not depend on the flavours. And `A_i^2 = 2Σ_{k<k'} c_{x_i,k}c_{x_i,k'} r^{ℓ_i,x_i†}_k r^{ℓ_i,x_i†}_{k'}`, whose `(1, 2)` term has coefficient 2. Hence `⟨φ, Oψ⟩ = ±2^4 ≠ 0`. ∎

[check] A fermionic simulation of `O` on this `ψ` gives `|Oψ| = 16`, with a single output term, for `m = 2, …, 5`. For `m = 6, 7, 8` the norm is nonzero; the extra `y`-end flavours give further outputs. For `m = 1, 9` no admissible `ψ` exists.

**Corollary U-T″ (the whole line family at one site).** Let `2 ≤ m ≤ 8` and let `y` be a site. The 16-dimensional space
\[
\mathcal O_y=\operatorname{span}\{c_{y,i}c_{y,j}c_{y,k}\}\;\oplus\;M_y\;\oplus\;\operatorname{span}\{O\},
\]
with `M_y` the `5bar ⊗ det^2` space of Lemma U-T at `y`, is carried at `y`, invariant under `U(5)_y` and fermion odd. Its `U(1)_N` charges are `(−3, 9, −15) = −3·(1, −3, 5)`, the line point `u = −3`. So by U-A every perturbative `U(5)` anomaly of this content vanishes. Under the standard embedding (case A of U-M, `Y ∈ su(5)`) its restriction to `H_y` is `F_{1/6}`. For `m ∈ {1, 9}` no space carried at one site realizes any point of the line: Lemma U-T bounds the charge of such a space by 11, and every line point has `|c| = 5|u| ≥ 15`. **So an anomaly-free `U(5)` family is carried at one site exactly when `2 ≤ m ≤ 8`.**

*Proof.* Each summand is carried at `y`: the triples by Theorem F, `M_y` by Lemma U-T, the singlet by Lemma U-T′. Invariance and oddness hold summand by summand. The charges: `Λ^3(5bar) ≅ Λ^2(5) ⊗ det^{−1}` has `5k + 2 = −3` at `k = −1`; `5bar ⊗ det^2` has `5·2 − 1 = 9`; `det^{−3}` has `−15`. Restriction: in case A, `det` is trivial on `SU(3) × SU(2)` and `Y ∈ su(5)` sees no `det`, so each summand restricts as its `SU(5)` part: the 10 gives `Q ⊕ u^c ⊕ e^c` (Theorem F), the `5bar` gives `d^c ⊕ L`, and the singlet gives `ν^c`. ∎

**Repaired statement.** Replace GAP U-T by: "Closed. For `2 ≤ m ≤ 8` the line family at `u = −3` is carried at one site (Corollary U-T″). For `m ∈ {1, 9}` no line point is (U-T)." This is operator content only. Whether these composites are light and chiral, and whether their mirrors gap, is CH1-5U-i, unchanged.

---

## 3. The two errors

### 3.1 Item 75: the last sentence of GAP U-T

`CH1.md` line 163: "The source's last sentence also reverses the sign of \(D^\dagger\) after defining \(D\) as a product of creators; the charge \(-15\) belongs to \(D^\dagger D^\dagger D^\dagger\)."

The source does not reverse a sign. `CH1_5_DRAFT.md` line 188: "The total-charge composite `D_x^†D_y^†D_z^†`, with `D_x = c^†_{x,1}⋯c^†_{x,5}`, is a gauge-covariant `SU(5)` singlet of total charge −15 for every `m`." Its proof, line 190: "The last sentence: each `D^†` is `det^{−1}` at its site." `D_x` is a product of five creators. It raises `N_x` by 5 and transforms as `det`. So `D_x^†` lowers `N_x` by 5 and transforms as `det^{−1}`, and the product of three has total charge `−15`. The source's operator, charge and representation agree. **Fix:** delete the sentence.

### 3.2 Item 79: the reason given for correcting clause (c)

`CH1.md` line 171: "Mere inclusion of \(U(1)_N\) alone does **not** impose that full line: the mixed \(SU(5)^2U(1)\) condition also needs the relevant unbroken \(SU(5)\) and multiplet assumption. This corrects clause (c) of the draft."

The first clause is true. The draft's clause (c) is false as worded, as `CH1.md` says. `CH1_5_DRAFT.md` line 257: "(c) if `U(1)_N ⊂ G_∞`, the family's `U(1)_N` charges are on the line of S2-5(iii) (forced under AM-5)." **The reason is false: unbroken `SU(5)` is not needed.** CH1-5O-i already assumes `H ⊆ G_∞` (line 171), and `SU(3) ⊂ H`. Give `U(1)_N` the constant values `a` on the members of the 10, `b` on the `5bar` and `c` on the singlet. Then the `U(1)_N SU(3)^2` coefficient is `(1/2)(2a + a + b) = (3a + b)/2`: two triplets in `Q`, one antitriplet each in `u^c` and `d^c`. That is the mixed `SU(5)^2` coefficient of U-A. The `U(1)_N SU(2)^2` coefficient is `(1/2)(3a + b)` as well: three doublets in `Q`, one in `L`. What the line needs, beyond `U(1)_N ⊂ G_∞`, is the multiplet constancy alone. Proposition AN states the correct clause.

**Proposition AN.** Give each member `f` of `F_t` (with `ν^c`, all left-handed) one `U(1)_N` charge `N_f`. Normalize `Y` by `Y(Q) = 1/6`, and write `B − L = (1/3, −1/3, −1/3, −1, 1, 1)` on `(Q, u^c, d^c, L, e^c, ν^c)`.
(i) The four coefficients `U(1)_N SU(3)^2`, `U(1)_N SU(2)^2`, `U(1)_N U(1)_Y^2` and `U(1)_N`-gravitational vanish if and only if `N = λY + μ(B − L)` on the family, for some real `λ, μ`. The other two, `U(1)_N^2 U(1)_Y` and `U(1)_N^3`, then vanish too.
(ii) Suppose `N` is constant on the members of the `U(5)` multiplets of U-M, with values `(a, b, c)`: pattern A, `{Q, u^c, e^c}`, `{d^c, L}`, `{ν^c}`; or pattern B, `{Q, d^c, ν^c}`, `{u^c, L}`, `{e^c}`. Then the four coefficients of (i) vanish if and only if `(a, b, c) ∈ R·(1, −3, 5)`.
(iii) Under AM-5 with `H·U(1)_N ⊆ G_∞` and light content exactly `F_t`, `N ∈ span{Y, B − L}` on the family. With R-F and S1-5 every `N_f` is odd, and S2 (with `q = 1`) gives `N = 2α'Y + β'(B − L)` with `α'` even, `β'` odd and `α' + β' ≡ 0 mod 3`.

*Proof.* (i) In the order `(N_ν, N_e, N_L, N_u, N_d, N_Q)` the four coefficients are
gravitational: `N_ν + N_e + 2N_L + 3N_u + 3N_d + 6N_Q`;
`U(1)_Y^2`: `N_e + (1/2)N_L + (4/3)N_u + (1/3)N_d + (1/6)N_Q`;
`SU(2)^2`: `(1/2)(N_L + 3N_Q)`;
`SU(3)^2`: `(1/2)(N_u + N_d + 2N_Q)`.
Only the first contains `N_ν`. Of the other three, only the second contains `N_e`. Of the last two, only the third contains `N_L`. The fourth contains `N_u`. So the system is in echelon form with four pivots. Its rank is 4 and its kernel has dimension 2. `Y = (1/6)(1, −4, 2, −3, 6, 0)` and `B − L` lie in the kernel (direct sums; [check]). They are independent, since their `ν^c` entries are 0 and 1 and `Y ≠ 0`. So the kernel is their span. On the span, `U(1)_N^2 U(1)_Y` and `U(1)_N^3` expand into the dimension-weighted family sums of `Y^3`, `Y^2(B−L)`, `Y(B−L)^2` and `(B−L)^3`. Each is zero. For example, `Σ dim·Y^2(B−L) = 6·(1/36)(1/3) + 3·(4/9)(−1/3) + 3·(1/9)(−1/3) + 2·(1/4)(−1) + 1 = (1 − 8 − 2 − 9 + 18)/18 = 0` [check: the other three].
(ii) Pattern A: substitute. The `SU(3)^2` coefficient is `(3a + b)/2` and the gravitational one is `10a + 5b + c`. So `b = −3a` and `c = 5a`. Then `SU(2)^2` gives `(3a + b)/2 = 0`, and `U(1)_Y^2` gives `(15a + 5b)/6 = 0`. Pattern B: `SU(3)^2` is `(3a + b)/2`, `SU(2)^2` is `(3a + b)/2`, gravitational is `10a + 5b + c`, so again `b = −3a` and `c = 5a`; then `U(1)_Y^2 = c + (11/6)b + a/2 = 5a − 11a/2 + a/2 = 0`. Conversely the line satisfies all four in both patterns [check].
(iii) AM-5 (line 165) asserts that every perturbative anomaly coefficient of `G_∞` vanishes on the light fields. The four coefficients of (i) are values of `G_∞`'s invariant cubic form and of its gravitational trace on `su(3) ⊕ su(3) ⊕ u(1)_N`, `su(2) ⊕ su(2) ⊕ u(1)_N`, `u(1)_Y ⊕ u(1)_Y ⊕ u(1)_N` and `u(1)_N`. They are restrictions of `G_∞`'s coefficients to the subalgebra `h ⊕ u(1)_N`, so they vanish. `U(1)_N` commutes with `H`, and the six members of `F_t` are pairwise non-isomorphic `H`-representations (`t ≠ 0`), each of multiplicity one. By Schur's lemma `U(1)_N` acts on each member by one charge `N_f`. Then (i) applies, and S2 gives the lattice. ∎

**Witness against the draft's clause (c).** `N = 12Y + 15(B − L)` gives `(N_Q, N_u, N_d, N_L, N_e, N_ν) = (7, −13, −1, −21, 27, 15)`. All six charges are odd, and all six coefficients of (i) vanish [check]. It is off the line: in pattern A the members `Q, u^c, e^c` carry `7, −13, 27`, and in pattern B the members `Q, d^c, ν^c` carry `7, −1, 15`. It also meets the Case I lattice conditions at the standard ratio. There `Y = (−2p + 3q)/6` with `p = n_1 + n_2 + n_3`, `q = n_4 + n_5` and `N = p + q`. The members sit at `(p, q) = (4, 3), (−7, −6), (−1, 0), (−12, −9), (15, 12), (9, 6)`, and each pair has the triality `p ≡ n (mod 3)`, the doublet parity `q ≡ n (mod 2)` and the odd `p + q` that line 127 requires [check]. Whether nonzero local operators carry these weights is CG1K-loc.

**Fix.** Replace the sentence by: "Mere inclusion of \(U(1)_N\) does not impose that line. With \(H\cdot U(1)_N\subseteq G_\infty\), AM-5 forces \(U(1)_N\) on the family into \(\mathrm{span}\{Y,B-L\}\), and with R-F into the odd lattice of S2 (Proposition AN of `CH1_REFEREE.md`). The line follows when, in addition, the charges are constant on the members of \(U(5)\) multiplets. Unbroken \(SU(5)\) is not needed: \(SU(3)\subset H\) gives the same mixed coefficient \((3a+b)/2\). Example off the line: \(N=12Y+15(B-L)\)."

---

## 4. Required edits

Each edit names its item and the `CH1.md` line.

- **R1** (item 75, line 163). Delete the last sentence of GAP U-T (section 3.1).
- **R2** (item 79, line 171). Replace the reason as in section 3.2. State clause (c) as Proposition AN (iii).
- **R3** (items 72-74, lines 159-163). Add Lemma U-T′ and Corollary U-T″ (section 2.5). Replace GAP U-T by the closed statement of section 2.5.
- **R4** (items 22-26, lines 43-51). Add Lemma ST (section 2.1). Replace GAP F3a/F4 by: "Closed by Lemma ST: a linear Weyl node isolated in \(N_0\cup N_\pi\) straddles its cut, at any tilt." Def 4 may stay; with def 4′ instead, F3a, F3b and F4 hold as stated for isolated nodes of any tilt.
- **R5** (item 2, line 7). Add K2, Lemma V and Lemma U-T to the "proved" list, and name Theorem F, O-M and U-M.
- **R6** (item 9, line 20). State that `t` is a linear form and that, on the pair, \(e^{ia}U(k_0+q)=\exp(-ih(q))+O(|q|^2)\).
- **R7** (item 43, line 87). Name the import's source: `CH1_DRAFT.md` line 281, quoting `LW1_DRAFT.md` 7.2 (#10016). Add that frozen `LW1.md` gives at \(\mu=0\) only an eightfold point, \(V(0)=I\) (B10, C1), where the regular-node results do not apply and F3 does.
- **R8** (item 53, line 113). Bracket \((1,1)_0\) as optional.

Wording and notation, recommended, with no change of content:
- **W1** (items 68, 70). Rename U-A's charges `(a, b, c)`, for example to `(n_10, n_5̄, n_1)`, since U-M uses `a, b` for hypercharge block values. Rename line 155's `α, β`, the coefficients of `Y` and `B − L`, since S2 and Case I use `α, β` in two other senses.
- **W2** (item 59, line 127). Replace "requires and abstract tensor powers supply integers" by "occurs, in an abstract tensor-class representation of parity \((-1)^\epsilon\), if and only if there are integers".
- **W3** (item 27, line 53). Say in K1 that \(P_l\) preserves each block.
- **W4** (item 47, line 97). Define "homogeneous": a definite charge at each site.
- **W5** (item 63, line 135). Add U-M's two one-line reasons.
- **W6** (item 19, line 37). Add the compactness clause to F2's proof.
- **W7** (item 41, line 83). Write C3's class count.
- **W8** (item 36, line 73). Say that the draft's S3 was conditional on reading `G` as the exact group and on B5 for cell frames.

## 5. Open statements to carry, by name

**Unchanged by this report.** CH1-i (mirror gapping). CH1-ii (a local gauged measure). Reflection positivity of the measure. The propagator-zero question (`TOE_ASSEMBLY.md` line 410, #10030: whether partners surviving as propagator zeros are acceptable). CH1-C1 and CH1-C3 on `L_cube`. CG1K-H and CG1K-loc. CG1-i and CG1-ii. LW1-5-BG and LW1-5-X. VC1. The outside inputs AM and AM-5. Inherited from frozen `LW1.md`: B5(b), which bears on line 73.

**Changed by this report.**
- CH1-5U-i keeps its name. Its representation step, an anomaly-free `U(5)` family of local operators carried at one site, is closed for `2 ≤ m ≤ 8` (Corollary U-T″). For `m ∈ {1, 9}` such a family must spread over several sites. Binding, chirality and the mirror gap stay open.
- CH1-5O-i keeps its name. Its clause (c) becomes Proposition AN (iii).
- GAP F3a/F4 is closed (Lemma ST). GAP U-T is closed (Lemma U-T′, Corollary U-T″). GAP C2 is settled by a counterexample and carries nothing. GAP O-M is a scope statement and carries nothing new.

---

## FINISH

**Proved here** (referee closures; pass 3, not themselves refereed).
- The verdict table: 80 items, 76 CORRECT, 2 ERROR, 2 INCOMPLETE. No ERROR sits in a theorem's statement or proof.
- **Lemma ST.** A linear Weyl node isolated in its cut set straddles the cut on a punctured ball, at any tilt. With it, Lemma F3a, Corollary F3b and Theorem F4 hold for every isolated linear node, critical tilt included.
- **Lemma U-T′.** On `L5-U` with `2 ≤ m ≤ 8`, `O = D_y^†F_1F_2` is a nonzero, fermion-odd operator carried at `y` in `det^{−3}`, of `U(1)_N` charge `−15`. It rests on the provisional `L5-U` definitions of `LW1_5U_DRAFT.md` section 1.1.
- **Corollary U-T″.** For `2 ≤ m ≤ 8` the whole line family `10_{−3} ⊕ 5bar_9 ⊕ 1_{−15}` is carried at one site, is anomaly free under `U(5)`, and restricts to `F_{1/6}` under the standard embedding. For `m ∈ {1, 9}` no line point is carried at one site. So an anomaly-free `U(5)` family is carried at one site exactly when `2 ≤ m ≤ 8`.
- **Proposition AN.** The four linear `H·U(1)_N` anomaly coefficients of one family vanish exactly on `span{Y, B − L}`; with `U(5)`-multiplet constancy, exactly on the line `u(1, −3, 5)`. Under AM-5 with `H·U(1)_N ⊆ G_∞`, the family's `U(1)_N` charges lie in S2's odd lattice. Unbroken `SU(5)` is not needed for the line.
- **Lemma B.** On `L5-U` every weight of an operator space carried at one site lies in `[−7, 7]^5`.

**Counterexamples.**
- To `CH1.md` line 163, last sentence: the source's `D_x^†D_y^†D_z^†`, with `D_x` a product of creators, has charge `−15`. No sign is reversed.
- To the reason at `CH1.md` line 171: on `U(5)`-constant charges the `U(1)_N SU(3)^2` coefficient equals the mixed `SU(5)^2` one, `(3a + b)/2`.
- To the draft's clause (c) (`CH1_5_DRAFT.md` line 257), confirming `CH1.md`: `N = 12Y + 15(B − L) = (7, −13, −1, −21, 27, 15)` is odd, anomaly free under `H·U(1)_N`, meets the Case I lattice conditions at the standard ratio, and lies off the line.
- To the draft's free-embedding sentence (`CH1_DRAFT.md` line 341), confirming GAP C2: on a spin-1/2 link at `E = +1/2` the dressed hop acts as the identity, while the free hop moves the fermion.
- To the necessity of def 4's strict tilt bound: `h(q) = (q_3 − q_3^3/2)·1 + q·σ` is critically tilted, isolated, and straddles, so F3a's conclusion holds for it.

**Open, by name.** CH1-i, CH1-ii, reflection positivity, the propagator-zero question, CH1-C1, CH1-C3, CH1-5U-i (its dynamical steps), CH1-5O-i, AM, AM-5, CG1K-H, CG1K-loc, CG1-i, CG1-ii, LW1-5-BG, LW1-5-X, VC1; inherited from `LW1.md`, B5(b).

**What changes downstream.**
- `CH1.md`: required edits R1-R8, and W1-W8 if the lead wants them. With them applied, this check finds no ERROR or INCOMPLETE item.
- CH1-5U-i: its target content exists as local operators carried at one site for every `m` from 2 to 8. For `m = 1` or `9` an anomaly-free family must spread over several sites. This answers, for one-site carriers, the case that `CH1_5_DRAFT.md` line 299 leaves open.
- CH1-5O-i: clause (c) is Proposition AN (iii). A long-distance `U(1)_N` with `H` unbroken confines the family's `U(1)_N` charges to `span{Y, B − L}`, not to the `U(5)` line.
- Parts that cite F3a, F3b or F4 may cite them for isolated linear nodes of any tilt.
- No law fails at a named step here. Both five-mode laws stay live.
