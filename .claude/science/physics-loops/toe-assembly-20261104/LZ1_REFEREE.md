lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# LZ1 referee report (pass 3)

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 3 (the referee) of part LZ1 (with MT1-S) under the method of open PR #10138. In that method Claude drafts at length and runs to closure, Codex distils, a fresh session referees, and then the part is frozen.

**Referee.** Claude Opus 5.5 (model id `claude-opus-5-5`), max reasoning effort, headless lane `mac-mini-toe-lane`. This session wrote neither pass 1 (`LZ1_DRAFT.md`) nor pass 2 (`LZ1.md`). It ran no subagents. This is one check: one whole-part, line-by-line read of `LZ1.md`. It read no other review of LZ1. No review of this review was commissioned.

**What this file is.** A referee report. It grants no status. It adopts no law, reading, definition or specification. It changes no axiom and no working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. A "referee closure" (RC) is a complete argument written here. Referee closures are themselves unrefereed. A "[check]" is a small scratch computation. It guides or refutes; it never proves.

**Text read.** `LZ1.md` at commit `03709a6a0`, the last commit that touches it. The branch head when read was `e9e8234c1`. The two later commits add only `EW1_DRAFT.md`, `EW1.md` and `ZM1.md` [check: `git diff --stat 03709a6a0 e9e8234c1`]. SHA-256 of the file read: `bb6b7db755c82321b3bdf5487e8594acabbe3133090e36184d4e57c83a4b8579`. Line numbers below refer to that file.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` (sparse) | `e9e8234c1` (head when read); `LZ1.md` last changed at `03709a6a0` |
| `MT1.md` at the revision the draft quoted, read with `git show c2bfcd143:<path>` on the same branch | `c2bfcd143` |

No other branch was read.

**Files read, by line.** In this folder at `e9e8234c1`: `LZ1.md` lines 1-150 (all); `LZ1_DRAFT.md` lines 1-430 (all); `MT1.md` lines 1-246 (all; the frozen text); `MT1_REFEREE.md` lines 1-36 and 270-340, and lines 189-215 (C4) by string comparison with frozen `MT1.md` lines 180-205; `LW1_5.md` lines 1-352 (all); `LW1.md` lines 14-100, 205-215 and 389-410; `CH1_5UQ.md` lines 1-70 and 205-236; `TOE_ASSEMBLY.md` lines 214, 316-334 and 354. At `c2bfcd143`: `MT1.md` lines 17-24, 32, 60-67, 75-77, 83-92, 116-120 and 134-140, each compared with its frozen counterpart. For format only: `LW1_REFEREE.md` lines 1-100 and its section headers, the section headers of `MT1_REFEREE.md`, and `Y2W_DRAFT.md` lines 1-40 and its section headers. Rules: `AGENTS.md` and `docs/ai_methodology/SCIENCE_WORKFLOW.md`.

**Hashes.** `LZ1.md` line 13 records the draft's SHA-256 and says the draft's context hashes agree except for `MT1.md`. Recomputed [check: `shasum -a 256`]: the draft is `ef73317c22e37d163508de838c7f68c017cac8dd99f3c656e0297b71b074f124`, as recorded. `TOE_ASSEMBLY.md` `8027d9d44eb5fcaf`, `MT1_REFEREE.md` `51acc331b9709faa`, `LW1.md` `78280bd620800eac`, `LW1_5.md` `7afb7ee2a52d91cd`, `CH1_5UQ.md` `674c2ef458aac936` and `TM1.md` `24e183db90eb5ab9` equal the draft's prefixes. `MT1.md` is now `232569f4b008ce8f`. At `c2bfcd143` it is `c8263124f7df9bea`, the draft's value.

**Working-set entries used, by name.** PS-1 read by PS-1c, only through the cell lifts (Theorem 3.2, RC2). PS-5 (five fermion modes per site). PS-6 and PS-6r, only through the link registers of `L5-U[m]` and `L5-O[S_+]`. PS-7r, only for its sentence "For the gauged law, the vacuum is the state VC1 builds from this sea" (`LW1_5.md` line 65; used in G8 and RC2). The owner decision LW1-5-RQ (both laws live). Nothing else from the working set is used.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws, the working set and the proposed readings are read plainly. Where a reading needs a specification, this report says so and proposes none.

**Method.** I re-derived every proof in `LZ1.md` by hand. I compared each item with its pass-1 source in `LZ1_DRAFT.md` and with each cited source. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix or counterexample); INCOMPLETE (a named missing step, with what is missing). The checks are three scripts in `/tmp/toe-lz1ref/`: `check_c4.py`, `check_theta_o.py` and `check_rc3.py`, with outputs `out_c4.txt`, `out_theta_o.txt` and `out_rc3.txt`. They use floating point on 8 by 8 and 16 by 16 matrices and on sparse 1024 by 1024 matrices. They ran in 13.6 s, 0.4 s and 0.1 s, under 530 MB each, after `memory_pressure` showed 68 percent free.

**Counts.** 58 items: 53 CORRECT, 3 ERROR, 2 INCOMPLETE. The nine distiller GAPs count as nine items. No ERROR or INCOMPLETE item changes the content of a proved theorem. All nine GAPs are real. Section 4 gives three referee closures. RC1 bears on the proposed band reading: as written, it counts static flat bands, including bands outside the physical sector, as light species.

**Credits.** Pass 1: `LZ1_DRAFT.md` (Claude Opus 5.5). Pass 2: `LZ1.md` (Codex `gpt-6.1-terra`). Used here with credit: closures C3 and C4 of the MT1 referee, now in frozen `MT1.md` §7; `CH1_5UQ.md` Theorem 3.1 (frozen stars) and RC7, with their draft, distiller and referee; `LW1_5.md` H, Σ, SC.1, B1-U, E2b-5 and step 2 of S′ ("a matrix commuting with every \(E_{ab}-E_{ba}\) is scalar"). The literature named in `LZ1.md` §6 is not used. No citation is a proof step here.

---

## 1. Verdict table

| # | Item (LZ1 line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status paragraph (5) | CORRECT | |
| 2 | §0 "Proved" list (7) | ERROR | Cites "Theorems 4.1–4.3"; there is no Theorem 4.3. The half-filling clause drops site transitivity. The multiplicity-one phrase inherits item 42. |
| 3 | GAP G1 (9) | CORRECT | Real. |
| 4 | GAP G2 (9) | CORRECT | Real as a missing step. RC1(a): in the exponential case the band reading itself excludes the static vectors. |
| 5 | GAP G3 (9) | CORRECT | Real. "Multiplicity one" must mean equivalence of the whole fibre (item 42). |
| 6 | GAP G4 (9) | CORRECT | Real as a missing hypothesis in the draft's summary sentence. |
| 7 | GAP G5 (9) | CORRECT | Real. RC3 adds a symmetric copy-mixing term. |
| 8 | GAP G6 (9) | CORRECT | Real. |
| 9 | GAP G7 (9) | CORRECT | Real. The repair also needs commuting gates (item 14). |
| 10 | GAP G8 (9) | CORRECT | Real for the word "counterexample". RC2: the class is not empty. |
| 11 | GAP G9 (9) | CORRECT | Real. RC1(b) makes the full-space obstruction hold in every gauge-invariant `L5-O` state, with no clustering hypothesis. |
| 12 | §0 "Open by name" (11) | CORRECT | |
| 13 | §0 provenance (13) | CORRECT | Hashes recomputed; all as stated. |
| 14 | §1 update class (17) | INCOMPLETE | Each layer's gates must commute pairwise, with finitely many per cell (`LW1.md` E1). "finite-support ... layers" should read "layers of finite-support gates". |
| 15 | §1 translations and tick (19) | CORRECT | |
| 16 | §1 centre implementers (21) | CORRECT | `ω_z²=−1` on `S_+`; "involutive as adjoint actions" is the right wording. |
| 17 | §1 D1 states and GNS (23) | CORRECT | |
| 18 | §1 bands, nodes, light species (25) | CORRECT | Flat bands and bands outside `H_phys` qualify as light species; see RC1 and item 52. |
| 19 | §1 D5 symmetries (27) | CORRECT | |
| 20 | §1 proposed readings (29) | CORRECT | The coverage sentence is right for R-SC in general; RC1(a) covers the exponential case. |
| 21 | Theorem 2.1, statement (33-37) | CORRECT | |
| 22 | Theorem 2.1, proof (39-43) | CORRECT | |
| 23 | Theorem 2.2, statement (45) | CORRECT | |
| 24 | Theorem 2.2, proof (47) | CORRECT | The `C¹` hypothesis is used: a Cantor-type continuous function takes countably many values almost everywhere. |
| 25 | Corollary 2.3 (49) | ERROR | The second sentence reverses the logic of Theorem 2.2. |
| 26 | Theorem 3.1, statement (53-55) | CORRECT | |
| 27 | Theorem 3.1, proof (57) | CORRECT | |
| 28 | Theorem 3.2, statement (59-63) | CORRECT | |
| 29 | Theorem 3.2, proof (65) | CORRECT | |
| 30 | Remark after Theorem 3.2 (67) | CORRECT | RC1(a) and RC2 sharpen it. |
| 31 | Theorem 3.3, statement (69) | CORRECT | |
| 32 | Theorem 3.3, proof (71) | CORRECT | |
| 33 | Remark (73) | CORRECT | |
| 34 | Theorem 3.4, statement (75) | CORRECT | |
| 35 | Theorem 3.4, proof (77) | CORRECT | |
| 36 | Casimir paragraph (79) | CORRECT | In a locally gauge-invariant state its clustering hypothesis holds automatically (RC1(b)). |
| 37 | Theorem 4.1, statement (83) | CORRECT | Both fibre formulas re-derived. |
| 38 | Theorem 4.1, proof (85) | CORRECT | |
| 39 | Theorem 4.2, statement (87) | CORRECT | A sufficiency claim. The full two-copy family has one more term (RC3). |
| 40 | Theorem 4.2, proof (89) | CORRECT | |
| 41 | Remark (91) | CORRECT | |
| 42 | Theorem 5.1, statement (95) | ERROR | "exactly one copy" admits a counterexample. Restore the draft's unitary `T`. |
| 43 | Theorem 5.1, proof (97-103) | CORRECT | Complete under the restored hypothesis. `[check]` agrees. |
| 44 | Remark (105) | CORRECT | |
| 45 | Theorem 5.2, statement (107-112) | CORRECT | |
| 46 | Theorem 5.2, proof (114-116) | CORRECT | `[check]` agrees on the link identities. |
| 47 | Remark (118) | CORRECT | A sharper citation is recommended (R1). |
| 48 | Theorem 6.1, statement (122) | CORRECT | Read on a finite region, or on vectors with empty matter. |
| 49 | Theorem 6.1, proof (124) | CORRECT | |
| 50 | Remark (126) | CORRECT | |
| 51 | §6 lead-in to the four tests (128) | CORRECT | |
| 52 | Four-test row D2–D4 (132) | INCOMPLETE | Its scope note misses RC1. |
| 53 | Four-test rows D5, R-loc, R-CS, R-SC (133-136) | CORRECT | They match the draft's judgments. R-loc reads species through D2–D4, so item 52 bears on it. |
| 54 | Four-test rows LZ1-C1 to LZ1-C4 (137-140) | CORRECT | They match the draft's judgments. |
| 55 | Literature paragraph (142) | CORRECT | |
| 56 | §7 LZ1-i and the attacks (146) | CORRECT | |
| 57 | §7 MT1-S[R-CS] (148) | CORRECT | Its reconciliation request is answered in §5: no import changed in content. |
| 58 | §7 VC1, PS-7 and GA1-P-5 (150) | CORRECT | |

---

## 2. Details of the non-CORRECT items

### 2.1 ERRORS

**Item 2 (line 7).** Three fixes.

- (a) `LZ1.md`: "The symmetry and empty-matter results are in Theorems 4.1–4.3 and 6.1." Section 4 contains Theorems 4.1 and 4.2 only. Fix: "Theorems 4.1, 4.2 and 6.1".
- (b) `LZ1.md`: "half filling plus exponential Gauss-charge clustering produces static physical-sector spectral weight arbitrarily close to zero momentum (Theorem 3.2)". Theorem 3.2 proves this for "a stationary, site-transitive state" (line 63). Its proof uses site transitivity: transitivity forces every `ω(N_x)` to equal `q−3m`. Without it the clause is not proved. A cell-invariant half-filled state with every `Q_x` sharp is not excluded, since its eight charges per cell need only sum to `20+24m` (line 67). In such a state no `Q_x` has positive variance, and Theorem 3.1 has no input. Fix: "a stationary, site-transitive, half-filled state with exponential Gauss-charge clustering has static physical-sector spectral weight arbitrarily close to zero momentum".
- (c) `LZ1.md`: "A specified multiplicity-one node representation forces a Clifford triple up to a real scalar, which may be zero (Theorem 5.1)." Fix as for item 42: "A node fibre carried by a unitary, up to phases, onto the free node representation forces a Clifford triple up to a real scalar, which may be zero (Theorem 5.1)."

**Item 25 (line 49).** `LZ1.md`: "The fermion clause of LZ1 is incompatible with a propagating odd band in this reading; if there are no odd bands it may be vacuous." The fermion clause asks every fermionic light species to have `E=c|k|(1+O((a|k|)^p))` with `c>0`. A propagating odd band with a Clifford cone of the common speed would satisfy that clause. So the clause and such a band are compatible. Theorem 2.2 proves a different fact: no odd light species of a D1 state propagates. Fix: "Under R-loc every odd light species of a D1 state is flat. So the fermion clause of LZ1 fails in every D1 state that has an odd light species, and holds only vacuously in a D1 state that has none." This is the draft's Corollary P.7 (draft line 201).

**Item 42 (line 95).** `LZ1.md`: "assume a finite-dimensional node fibre `E` has, up to phases, exactly one copy of the free `L5-U` node representation `C⁸⊗C⁵`". Read as multiplicity one inside a larger fibre, the theorem is false.

*Counterexample.* Let `E=(C⁸⊗C⁵)⊕(C⁸⊗C⁵)`. On both summands let the rotations act by `ρ̂(Q)⊗1`, inversion by `ρ̂_I⊗1`, the antiunitary `t` by `(D_rK)⊗K₅` and `σ` by `cχ_G⊗1`. Let `U(5)` act by `w(u)=1⊗u` on the first summand and by `w(u)=1⊗ū` on the second. The relation `t w(u) t⁻¹=w(ū)` holds on both summands. The second summand is not the free node representation up to phases. Restricted to `SU(5)`, the representations `u` and `ū` are inequivalent, and a phase (a character of `U(5)`) is trivial on `SU(5)`. So `E` contains exactly one copy. Put `N_j=aG_j⊗1₅ ⊕ a′G_j⊗1₅` with real `a,a′`. Each summand satisfies every listed condition: the converse at line 103 gives the rotation, inversion, antiunitary and `σ` conditions, and `G_j⊗1₅` commutes with `1⊗ū`. So `N` satisfies them on `E`. For `a²≠a′²`, `{N_i,N_j}=2δ_ij(a²1⊕a′²1)` is not a scalar. So `N` is not `aG_j⊗1₅` on `E`, and it has no single cone. Its speeds are `|a|` and `|a′|`.

The proof uses `E=C⁸⊗C⁵` in its first step: "The `U(5)` commutant makes each transformed triple `M_j⊗1₅`" (line 97). Fix: restore the hypothesis of the draft's Theorem M (draft line 304). "Let `T:E→C⁸⊗C⁵` be a unitary that carries the fibre's rotations, inversion, antiunitary, `σ` and `U(5)` action, up to phases, to `ρ̂(Q)⊗1`, `ρ̂_I⊗1`, `(D_rK)⊗K₅`, `cχ_G⊗1` and `1⊗u`." With it the proof is complete. The same change applies at line 7 and in G3.

### 2.2 INCOMPLETE

**Item 14 (line 17).** `LZ1.md`: "A **gauge-invariant update of the same form** appends finitely many finite-support, gatewise gauge-invariant layers, each covariant under the even translations." Two points are missing.

- (a) An infinite layer defines an automorphism only if its gates commute and each local operator meets finitely many of them. `LW1.md` E1 (line 401) states this proviso: "provided each of its sublayers consists of pairwise commuting gates". Its proof (line 403) starts from "a layer of locally finite, commuting, even gates". The draft points to E1 (draft line 85: "extended as in `LW1.md` E1"); `LZ1.md` drops the pointer. Every theorem of `LZ1.md` uses `α` as an automorphism of the quasi-local algebra.
- (b) A nonempty layer with finite support is not covariant under the even translations. The intended object is a layer of finite-support gates (draft line 85: "layers of finite-support gates").

Fix: "A gauge-invariant update of the same form appends finitely many layers. Each layer is a family of finite-support gates that is closed under the even translations and has finitely many gates per cell. The gates of a layer commute pairwise. Each gate commutes with every local gauge transformation." Each gate is then even: by §1 the product of the centre actions over its sites equals `θ` on the gate, and that product fixes the gate. No theorem changes under this fix.

**Item 52 (line 132).** `LZ1.md`: "| D2–D4 bands and species | pass | pass | conditional | pass | Finite fibres and `C¹` nodes omit possible infraparticles. |". The note misses a larger effect. D4 counts flat bands, and it counts bands outside `H_phys`. RC1(c) proves the following. Under R-loc with D2–D4 as written, LZ1(a) fails on `L5-O[S_+]` in every locally gauge-invariant, stationary, cell-invariant state, for every update in §1 and all constants. The flat species comes from the Gauss generators, that is, from the static background LW1-5-BG, not from light propagation. On `L5-U` the same holds in every such state in which some `SU(5)` Gauss generator has positive variance. Fix: add to the note "D4 counts flat bands and bands outside `H_phys`. With R-loc this decides LZ1(a) negatively on `L5-O[S_+]` in every locally gauge-invariant, stationary, cell-invariant state (`LZ1_REFEREE.md` RC1)." Whether a light species must propagate, or must lie in `H_phys`, is a specification the owner may give. This report proposes neither.

### 2.3 Notes on CORRECT items that bear on the freeze

- **Item 16.** On `L5-O[S_+]`, `ω_z²=z_z=−1` (`LW1_5.md` line 162 and SC.1). So `c_z` is not an involution there, but `Ad c_z` is. `LZ1.md` says exactly "involutive as adjoint actions", and `U_z²=1` follows in the GNS space.
- **Item 24.** The step "Such a function is constant on a connected open set" needs `C¹`. The Cantor function is continuous and nonconstant, and it takes dyadic values off a null set. The band definition requires `C¹` near a node, so the proof is complete.
- **Item 37.** Re-derived. For unitary `S`, `(Rf)(K)=f(Q⁻¹K)` gives `RM_βR⁻¹=M_{Qβ}`, and the band `SFR⁻¹` has fibre `V(Q⁻¹K)`. For antiunitary `S`, with componentwise conjugation `C` and `(R′f)(K)=f(−Q⁻¹K)`, the band `SFCR′⁻¹` has fibre `\overline{V(−Q⁻¹K)}` and leading generator `N′_j=Σ_iQ_{ji}\bar N_i`. Since `\bar N_i=N_i^T`, the spectra and the anticommutators are preserved.
- **Item 47.** `LZ1.md`: "Theorem 5.2 addresses the missing dressed-tick antiunitary named in MT1 referee C6". C6 itself says only "The argument does not apply to L5-O". Frozen `MT1.md` line 138 names the missing step: "On L5-O two more steps fail: no antiunitary symmetry of the dressed tick is known, and the dressed lifts act on bare matter in the exchanged form of C7." Recommended edit R1.
- **Item 53.** The R-loc row reports "pass" on all four tests. R-loc reads species through D2–D4, so RC1 reaches it through item 52.

### 2.4 Checks behind the main verdicts

- **Theorem 2.1.** The character projections `A_ε` have the support of `A`, because each `Ad c_z` acts on generators by signs. For `z∉Λ`, `c_z` is even and acts on modes outside the support of `A`, so it fixes `A_ε`. Oddness of `A` gives `∏_{z∈Λ}ε_z=−1` through `θ(A_ε)=Ad(∏_{z∈Λ}c_z)(A_ε)`. Patterns of different vectors differ at some `z`, and the `±1` eigenspaces of the self-adjoint unitary `U_z` are orthogonal. A finite nonempty `D⊂Z³` with `D+2β=D` has `|D|·2β=Σ_{d∈D}(d+2β)−Σ_{d∈D}d=0`, so `β=0`. The map `(u_β)↦Σ_βT_βu_β` from `ℓ²(Z³;K)` is unitary onto `H_nt`, because the pairs (orbit, `β`) label distinct patterns.
- **Theorem 2.2.** `⟨g_i(K),g_j(K)⟩−δ_ij` is integrable with all Fourier coefficients zero, hence zero almost everywhere. `W f(K)=f(K)V(K)` holds almost everywhere. So every eigenvalue of `V(K)` is an eigenvalue of `W` for almost every `K`. The point spectrum of a unitary on a separable space is countable. Newton's identities give the characteristic polynomial from `tr V^r`, `r≤d`.
- **Theorem 3.1.** `C(−β)=\overline{C(β)}` by translation invariance, so the density is real. With `|C(β)|≤Ae^{−κ|β|}`, the series converges on the complex strip `|Im K|<κ/2`, so the density is real-analytic. `τ_β` maps `A^G` onto itself, so `H_phys` reduces every `T_β`.
- **Theorem 3.2.** For each direction `i`, cell invariance moves the end `(x−e_i,x)` at `x` to the end `(x′,x′+e_i)` at `x′+e_i`, with `x′≡x−e_i` mod `2Z³`. The map `x↦x′` is a bijection of `{0,1}³`. So each direction contributes `8m`, and the total is `24m`. Sharpness gives `π(Q_x)Ω=q_xΩ`, and `q_x` lies in the integer spectrum of `Q_x`.
- **Theorem 3.3.** `[φ_{ℓ,x},φ_{ℓ,y}^*]=0` uses three facts: matter modes at different sites anticommute, matter commutes with rishons, and the two ends' rishons anticommute. Then `h_ℓv=φ_{ℓ,y}^*φ_{ℓ,x}v+φ_{ℓ,y}φ_{ℓ,x}^*v=0` on the kernel. The kernel vector exists for `a=max(0,m−5)≤4` with `y`-end number `m−a≤5`. The non-identity witness moves flavour 1 into an empty `x`-end mode.
- **Theorem 3.4 and line 79.** On `L5-O[S_+]` the star space is a product of seven spinor modules of `Spin(10)_x` (matter, and the `x`-end factor of each of six links). So `−1∈Spin(10)_x` acts as `−1` there, and no singlet exists. On each irreducible summand `C_x=Σ(𝒢^{ab}_x)²` is a scalar, zero only on the trivial one. So `C_x≥c_*>0`.
- **Theorem 5.1.** Re-derived through `M_1=Γ_1(a+bA_1(A_2+A_3))`. The three-fold turn and the quarter turn give `b_12=b_13` and `b_23=−b_23`. The antiunitary acts on `cΓ^SA^R` as `c↦c̄` times `(−1)^{|R|}`. `[check: check_c4.py]` finds real solution dimensions 8, 4, 3, 1, 2, 2 for the condition sets (R), (R,I), (R,I,Θ), (R,I,Θ,σ′), (R,I,σ′), (R,Θ,σ′), the numbers MT1's C4 reports, and the one-dimensional solution is `aΓ_j` with real `a`.
- **Theorem 5.2.** `Mη_{2k−1}M⁻¹=−η_{2k−1}` (nine anticommuting factors) and `Mη_{2k}M⁻¹=η_{2k}` (ten), while `K` fixes `X,Z` and negates `Y`. So `Jη_iJ⁻¹=−η_i` for all `i`. `J²=M²=(−1)^{10·9/2}=−1`. On the hop, the explicit `i`, the sign of `U^{ab}` and the two site signs give `(−1)(−1)(−1)=−1`. `[check: check_theta_o.py]` confirms `Jη_iJ⁻¹=−η_i` for all 20, `J²=−1` on the module and on `S_+`, `[J,Γ]=0`, `JΓ^xJ⁻¹=−Γ^x` and `JU^{ab}J⁻¹=−U^{ab}` for all 100 pairs.

---

## 3. The distiller's GAPs: real or not, and the repairs

All nine are in `LZ1.md` line 9. Each is real. Repairs follow where a repair exists.

**G1.** "A finite-fibre band is a proposed reading, not a definition supplied by MT1-S; flatness in it does not settle charged sectors or infraparticles." Real. Frozen `MT1.md` line 142: "The leading generator of the light fermion-odd excitations of an interacting state is not yet defined". So Corollary 2.3 is a theorem under the proposed reading R-loc. It is not a counterexample to MT1-S as frozen. No repair is needed.

**G2.** "The LZ1 dispersion statement alone does not imply R-SC: it constrains listed light species, not necessarily every fixed vector." Real as a missing step in the draft's inference. The draft names the needed reading in its own four-test note (draft line 344: "under the reading 'every low-energy excitation of the vacuum lies in some light species'"). The image of a band has translation spectral measures absolutely continuous with respect to Lebesgue measure: `⟨Ff,E(Δ)Ff⟩=∫_Δ|f|²dK`. So a `Ũ`-fixed vector with singular translation spectrum is orthogonal to every band, and the dispersion clause does not see it. Whether a state of the law has such vectors is not shown. So the non-implication holds at the level of the argument, not as a theorem about the law.

*Repair (RC1(a)).* When the connected correlation of a conserved local observable decays exponentially, its static vector generates a flat band. Under R-loc with D2–D4, the dispersion clause then excludes it with no coverage premise. So the exponential clause of Theorem 3.1 and the last clause of Theorem 3.2 hold with "R-SC" replaced by "R-loc with D2–D4 and the dispersion clause of LZ1(a)". The coverage premise stays needed for the first clause of Theorem 3.1, where `C(β)` only tends to zero.

**G3.** "Multiplicity one and the stated symmetries are sufficient for a Clifford cone only when the scalar is nonzero; they are not necessary, and MT1-S is not equivalent to that representation condition." Real. The draft wrote "MT1-S on `L5-U` at `μ = 0 = τ_E` is equivalent to one statement: the light charged band's node fibre carries the free node representation once" (draft line 310). Both directions fail. With `a=0` the fibre condition gives no cone. Two copies with `M=λ1₂` give `N_j=λG_j⊗1₅⊗1₂`, a cone without multiplicity one. One correction: "multiplicity one" must mean that the whole fibre is the free node representation; item 42 gives a counterexample otherwise.

*Repaired statement.* "If a unitary carries the node fibre, up to phases, onto the free node representation, the stated symmetries give `N_j=aG_j⊗1₅`. This is one Clifford cone exactly when `a≠0`. The fibre condition is not necessary for a cone, and MT1-S[R-CS] is not equivalent to it."

**G4.** "Theorem 3.1 needs its stated clustering hypothesis for each observable: R-SC alone does not make all conserved operators sharp." Real as a missing hypothesis in the draft's summary (draft line 223: "In words: under R-SC, every conserved local gauge-invariant operator is dispersion-free in the vacuum"). Theorem Z of the draft states a clustering hypothesis in each case. The non-implication is again a statement about the argument. A mixture of two states with different values of a conserved `Y` puts its extra variance at `K=0`, where R-SC says nothing. Whether the law has such a mixture satisfying R-SC is not shown. *Repair:* keep the clustering hypothesis in every statement, as Theorem 3.1 does.

**G5.** "The algebraic two-speed witness in Theorem 4.2 is not an interacting-law counterexample. Blockwise symmetry covariance alone does not exclude additional dynamical relations." Real. The draft wrote "The speeds of different orbits are independent (S.2, S.3)" (draft line 284). Theorem 4.2 shows only that the symmetries impose no relation. RC3 sharpens the witness: on two copies the node symmetries also allow a copy-mixing term, which splits even equal diagonal speeds.

**G6.** "The draft's deduction that B12 forces every D5 symmetry to commute with the tick does not follow from preservation of the time axis alone; D5 makes commutation a definition." Real. `LW1.md` line 391 (B12): "A symmetry of an ordered PS-1 update that maps each time slice to a time slice cannot move the time root off its line." This constrains the geometric action on the event lattice. It does not give `SŨS⁻¹=Ũ`. For example, a map with `SŨS⁻¹=Ũ⁻¹` keeps the time line and reverses its orientation. B12 excludes it only "For an oriented forward time direction". D5 restricts the class by definition. No result of `LZ1.md` uses more than the definition.

**G7.** "The proposed update class contains a plaquette layer only if that layer actually has the specified gatewise gauge invariance, finite support and cell covariance." Real. The draft wrote "This class contains every plaquette class that GA1-P-5 may supply" (draft line 85). *Repaired statement:* "The proposed update class contains a plaquette update if it is a finite product of layers, each a family of finite-support gates that commute pairwise, commute with every local gauge transformation, and are closed under the even translations with finitely many gates per cell (`LW1.md` E1)."

**G8.** "The draft calls the conditional class in Theorem 3.2 a counterexample without proving a state in that class exists; it is an incompatibility theorem." Real for the word "counterexample". The draft wrote "This is a counterexample to LZ1's first statement on `L5-U`, on the stated class of candidate vacua" (draft line 252). LZ1 concerns the vacuum: PS-7r says "For the gauged law, the vacuum is the state VC1 builds from this sea". Theorem 3.2 does not place that vacuum in its class. *Repair of the existence part (RC2):* the tracial state lies in the class. So the last clause of Theorem 3.2 is a nonvacuous incompatibility theorem. The tracial state is not offered as the vacuum.

**G9.** "The draft's statement that R-SC can be posed *only* on the physical sector is too strong: static charged vectors obstruct an analogous exclusion on the full GNS space under the stated clustering conditions, but other readings remain possible." Real. The draft wrote "So on `L5-O[S_+]` the spectral reading can be posed on `H_phys` only" (draft line 260). Nothing proves that every reading on the full space fails. *Sharpening (RC1(b)):* in every locally gauge-invariant, stationary, cell-invariant state of `L5-O[S_+]`, the vectors `π(𝒢^{ab}_x)Ω`, at least one of them nonzero, generate flat bands in `H_even⊖H_phys`, with no clustering hypothesis. So R-SC posed on all of `H` fails in every such state.

---

## 4. Referee closures

Notation is that of `LZ1.md` §1, with the update class repaired as in item 14. `m` denotes normalized Haar measure on `T³`. For a vector `w`, `μ_w(·)=⟨w,E(·)w⟩` is its translation spectral measure.

### RC1. Static flat bands

**Statement.** Let `ω` be stationary and cell invariant. Let `Y` be local with `α(Y)=Y`. Put `Y′=Y−ω(Y)`, `v=π(Y′)Ω`, `C(β)=ω(Y′^*τ_β(Y′))`, and let `H_v` be the closed span of `{T_βv:β∈Z³}`. Suppose `C(0)>0`.

- (a) If `|C(β)|≤Ae^{−κ|β|}` for some `A,κ>0`, there is an isometry `F:L²(T³,m)→H` with image `H_v` such that `(1,F,1)` is a band. Every `K` is a node, and the leading generator is zero.
- (b) Let `ω` be invariant under every local gauge transformation at `x`. Let `Y` lie in the span `𝔤_x` of the non-abelian Gauss generators at `x`: `𝔤_x=span{𝒢^{ab}_x}` on `L5-O[S_+]`, or `𝔤_x=span{𝒢^T_x: T traceless}` on `L5-U[m]`. Then `ω(Y)=0` and `C(β)=0` for every `β≠0`, so `μ_v=C(0)m`. If `ω` is locally gauge invariant, then `H_v⊥H_phys`.
- (c) Consequences.
  - (i) Under R-loc with D2–D4, every state in (a) with `Y` even has a flat bosonic light species with image `H_v`. So the dispersion clause of LZ1(a), read that way, fails in it. In particular, every stationary, site-transitive, half-filled `L5-U` state whose Gauss-charge correlations decay exponentially has a flat bosonic light species in `H_phys`.
  - (ii) On `L5-O[S_+]`, for every update in §1 and all constants, every locally gauge-invariant, stationary, cell-invariant state has a flat bosonic light species in `H_even⊖H_phys`. Under R-loc with D2–D4 as written, the dispersion clause of LZ1(a) fails in every such state.
  - (iii) On `L5-U[m]`, the conclusion of (ii) holds for every locally gauge-invariant, stationary, cell-invariant state in which some `𝒢^T_x` with traceless `T` has `ω((𝒢^T_x)²)>0`. The tracial state is one (RC2).

**Lemma RC1.0 (zero sets of real-analytic functions).** If `f:Rⁿ→R` is real-analytic and not identically zero, then `{f=0}` has Lebesgue measure zero.

*Proof.* Induction on `n`. Case `n=1`. The set of points where every derivative of `f` vanishes is closed. It is open, because `f` equals its Taylor series near each point. It is not all of `R`, since `f≢0`, so it is empty because `R` is connected. At a zero `s_0`, let `k` be the least order with `f^{(k)}(s_0)≠0`. Then `f(s)=(s−s_0)^kg(s)` near `s_0`, with `g` continuous and `g(s_0)≠0`. So `s_0` is an isolated zero. Hence the zeros are countable, and so null. Case `n≥2`. Write points as `(s,t)` with `s∈R`, `t∈R^{n−1}`. Put `g_k(t)=∂_s^kf(0,t)`, real-analytic on `R^{n−1}`, and `B={t: g_k(t)=0 for all k}`. Suppose `B` had positive measure. Then every `g_k` vanishes on a set of positive measure, so `g_k≡0` by induction. Then for every `t` the function `s↦f(s,t)` has all derivatives zero at `s=0`, so it vanishes identically by the case `n=1`. So `f≡0`, a contradiction. Hence `B` is null. For `t∉B`, `s↦f(s,t)` is not identically zero, and its zero set is null by the case `n=1`. The set `{f=0}` is closed, and Tonelli's theorem gives `|{f=0}|=∫|{s:f(s,t)=0}|dt=0`. ∎

*Proof of (a).* Cell invariance gives `C(−β)=ω(τ_β(Y′^*)Y′)=\overline{C(β)}`. Put `c(K)=Σ_βC(β)e^{−iK·β}`. For complex `K` with `|Im K|<κ` the terms are bounded by `Ae^{−(κ−|Im K|)|β|}`. So the series converges uniformly on compact subsets of that strip, and `c` is holomorphic there. Hence `c` is real-analytic on `R³`, periodic and real. Its Fourier coefficients against `m` are `C(β)`, the Fourier coefficients of `μ_v`. Uniqueness of Fourier coefficients gives `μ_v=c·m`. So `c≥0` almost everywhere, hence everywhere by continuity, and `∫c dm=C(0)>0`. By Lemma RC1.0 the set `{c=0}` is null. By the spectral theorem for the commuting unitaries `T_{e_j}`, there is a unitary `ι:L²(T³,μ_v)→H_v` with `ι(e^{iK·β})=T_βv`, and `ι` intertwines multiplication by `e^{iK·β}` with `T_β`. Define `F(f)=ι(c^{−1/2}f)`. Then `‖Ff‖²=∫|f|²c^{−1}c dm=‖f‖²`. `F` is onto `H_v`: for `g∈L²(T³,μ_v)` take `f=c^{1/2}g`. `F` commutes with multiplications, so `T_βF=FM_β`. `Ũv=π(α(Y′))Ω=v`, and `Ũ` commutes with every `T_β`, so `Ũ` fixes `H_v` pointwise and `ŨF=F`. So `(1,F,1)` is a band. Its fibre `V≡1` is `C¹`, every `K` is a node, `h≡0` and `N_j=0`. ∎

*Proof of (b).* Let `G_x` be the local gauge group at `x`: `U(5)_x` on `L5-U`, and the image of `Spin(10)_x` on `L5-O`. Its elements are local unitaries, and `G_x` is compact. Let `dg` be its normalized Haar measure, and put `E_x(A)=∫Ad g(A)dg` for local `A`. The map `S↦𝒢^S_x` is a Lie algebra homomorphism from `su(5)` (traceless `T`) or `so(10)` into the local algebra. It is injective, because its matter part `c^†Sc` or `M^S` is. It is equivariant: `Ad g(𝒢^S_x)=𝒢^{Ad(g)S}_x`. So `E_x` maps `𝔤_x` onto its `G_x`-invariant elements. These correspond to central elements of `su(5)` or `so(10)`. Both centres are zero. An element commuting with all of `su(5)` is a scalar matrix, hence zero when traceless. An element commuting with every `E_{ab}−E_{ba}` is a scalar matrix (`LW1_5.md` S′, step 2), hence zero when skew. So `E_x(Y)=0` on `𝔤_x`. Invariance of `ω` under each `Ad g` gives `ω(A)=ω(E_x(A))` for local `A`. So `ω(Y)=0` and `Y′=Y`. For `β≠0` the site `x+2β` is neither `x` nor a neighbour of `x`. So `τ_β(Y)` acts on matter and link ends that `G_x` does not move, and `τ_β(Y)` is even. Hence `Ad g(τ_β(Y))=τ_β(Y)`, and `C(β)=ω(E_x(Y^*)τ_β(Y))=0`, since `Y^*∈𝔤_x`. So `μ_v` has Fourier coefficients `C(0)δ_{β,0}`, and `μ_v=C(0)m`. Its density is the positive constant `C(0)`, so the construction in (a) applies without Lemma RC1.0. Now let `ω` be locally gauge invariant and `B∈A^G`. Then `⟨π(B)Ω,v⟩=ω(B^*Y)=ω(E_x(B^*Y))=ω(B^*E_x(Y))=0`. So `v⊥H_phys`. `H_phys` reduces every `T_β` (`LZ1.md` line 57), so `H_v⊥H_phys`. ∎

*Proof of (c).* (i) If `Y` is even, so are `v` and every `T_βv`, so `H_v⊂H_even`. By (a), `(1,F,1)` is then a light species in the sense of `LZ1.md` line 25. Its dispersion is `E≡0`, which is not `c|k|(1+O((a|k|)^p))` with `c>0`. For the `L5-U` statement take `Y=Q_x`. The proof of Theorem 3.2 gives `C(0)>0`. `Q_x∈A^G` is even, and `H_v⊂H_phys` because `H_phys` reduces every `T_β`. (ii) `LZ1.md` line 79 gives `C_x≥c_*>0` on the end-pure `S_+` star. In a locally gauge-invariant state `ω(𝒢^{ab}_x)=0` by (b). So `Σ_{a<b}ω((𝒢^{ab}_x)²)=ω(C_x)≥c_*>0`, and some `𝒢^{ab}_x` has `C(0)>0`. It is local and even, and `α` fixes it because every gate commutes with it. Apply (b), the construction of (a), and (i). The image lies in `H_even⊖H_phys`. (iii) The same argument with `𝒢^T_x`. In the tracial state `ω((𝒢^T_x)²)` is the normalized trace of the square of a nonzero Hermitian operator, so it is positive. ∎

**What RC1 means.** The flat species in (ii) is the static Gauss background LW1-5-BG, seen through D4. It does not propagate, and it lies outside `H_phys`. So D4 as written counts static modes, including unphysical ones, as light species. Under R-loc it decides LZ1(a) negatively on `L5-O[S_+]` in every locally gauge-invariant, stationary, cell-invariant state. A reading that leaves LZ1(a) undecided there must exclude these bands, for example by requiring propagation or by requiring even species to lie in `H_phys`. The owner may specify; this report proposes neither. Part (a) also shows that, in the exponential case, R-loc with D2–D4 already does the work of R-SC (G2).

### RC2. The tracial state lies in the class of Theorem 3.2

**Statement.** Let `τ` be the tracial state of the quasi-local algebra of `L5-U[m]`. Then `τ` is stationary for every update in §1. It is invariant under every lift of the cell group and under every local gauge transformation. It is half filled. For every `x` and `β≠0`, `τ(Q′_xτ_β(Q′_x))=0`, while `τ((Q′_x)²)>0`. So `τ` lies in the class of the last clause of Theorem 3.2, and that clause applies to it.

*Proof.* The quasi-local algebra is the norm closure of the increasing union of the finite-dimensional full matrix algebras `𝔄_Λ`: the matter CAR algebra on `Λ`, tensored with the registers of the links in `Λ`. On a full matrix algebra the normalized trace is the only tracial state: `τ(E_{ij})=τ(E_{ij}E_{jj})=τ(E_{jj}E_{ij})=0` for `i≠j`, and `τ(E_{ii})=τ(E_{ij}E_{ji})=τ(E_{ji}E_{ij})=τ(E_{jj})`. These traces are compatible with the inclusions, so they define one tracial state `τ`, and it is the only one. For a `*`-automorphism `φ`, `τ∘φ` is tracial, so `τ∘φ=τ`. This gives stationarity and invariance under the lifts and the local gauge transformations. Each matter mode has `τ(n_{x,k})=1/2`, so `τ(N_x)=5/2`. For `β≠0`, `x` and `x+2β` are not neighbours, so `Q_x` and `Q_{x+2β}` are even elements with disjoint supports. Order the matter modes with those at `x` first. A Jordan–Wigner map then sends an even element of the other modes to an operator on the other tensor factors only, because its strings cancel in pairs. So `Q_x` and `Q_{x+2β}` act on different tensor factors, and the normalized trace factorizes: `τ(Q′_xQ′_{x+2β})=τ(Q′_x)τ(Q′_{x+2β})=0`. Finally `Q_x` is not a scalar, since `N_x` takes the values `0,…,5`, so `τ((Q′_x)²)>0`. ∎

**What RC2 means.** The last clause of Theorem 3.2 has a nonempty class. The tracial state is the infinite-temperature state. Nobody offers it as VC1's vacuum. So the clause stays an incompatibility theorem about candidate vacua, as G8 says.

### RC3. Two copies: all covariant triples

**Statement.** Let `E=C⁸⊗C⁵⊗C²`. Let the rotations, inversion, `σ` and `U(5)` act on `C⁸⊗C⁵` as in Theorem 4.2 and as the identity on `C²`. Let the antiunitary act as `(D_rK)⊗K₅⊗K₂`. Write `{j,k,l}={1,2,3}` and `σ_y=[[0,−i],[i,0]]`. The Hermitian triples with the covariance of Theorem 5.1 are exactly

\[
 N_j=G_j\otimes1_5\otimes M+b\,UZ_j(A_k+A_l)U^*\otimes1_5\otimes\sigma_y,
\]

with `M` real symmetric `2×2` and `b` real. For `M=m₀1₂` with `m₀b≠0`, the speeds along `e₁` are `|m₀+√2b|` and `|m₀−√2b|`, so the triple is not one cone.

*Proof.* The commutant of `1⊗U(5)⊗1` is `M₈⊗1₅⊗M₂`, so `N_j` acts as `1₅` on the middle factor. Write `N′_j` for its action on `C⁸⊗C²`, and put `M_j=(U^*⊗1₂)N′_j(U⊗1₂)`. As in the proof of Theorem 5.1, `M_j` satisfies (R), (I) and (σ′) of MT1's C4, and `(D_r⊗1₂)\bar M_j(D_r⊗1₂)=M_j`. Expand `M_j=Σ_αB^α_j⊗σ_α` in the Hermitian basis `σ_0=1₂,σ_x,σ_y,σ_z`. The `σ_α` are linearly independent, and the symmetries act trivially on `C²`. So each `B^α_j` is Hermitian and satisfies (R), (I) and (σ′). Since `\bar σ_α=σ_α` for `α≠y` and `\bar σ_y=−σ_y`, the antiunitary condition reads `D_r\bar B^α_jD_r=B^α_j` for `α≠y` and `D_r\bar B^y_jD_r=−B^y_j`. Frozen `MT1.md` lines 197-201 (C4) show that (R), (I), (σ′) and Hermiticity leave `B_j=aΓ_j+b′Z_j(A_k+A_l)` with real `a,b′`; here `Γ_jA_j=iZ_j` converts C4's `Γ_j(a+bA_j(A_k+A_l))`. The map `X↦D_r\bar XD_r` fixes `Γ_j` and negates `Z_j(A_k+A_l)`; C4: "(Θ) sends `Z_jA_k` to `−Z_jA_k`". So `B^α_j=a_αΓ_j` for `α≠y`, and `B^y_j=bZ_j(A_k+A_l)`. Hence `M_j=Γ_j⊗M+bZ_j(A_k+A_l)⊗σ_y` with `M=Σ_{α≠y}a_ασ_α` real symmetric. Conjugating back gives the displayed form. Each term satisfies the conditions by the same computation, read backwards.

For the speeds, conjugation by `U⊗1` preserves spectra, so use `M_1=m₀Γ_1⊗1₂+bZ_1(A_2+A_3)⊗σ_y`. `Γ_1` anticommutes with `Z_1`, `A_2` and `A_3`, so it commutes with `Z_1A_2` and `Z_1A_3`. `Z_1` commutes with `A_2,A_3`, so `(Z_1(A_2+A_3))²=(A_2+A_3)²=2`. Also `Γ_1Z_1=−iA_1`. So `M_1²=(m₀²+2b²)+2m₀bW` with `W=−iA_1(A_2+A_3)⊗σ_y`. `W` is Hermitian and `W²=2`. So the eigenvalues of `M_1²` are `(m₀±√2b)²`. ∎ [check: `check_c4.py` finds a four-dimensional real solution space for the two-copy problem; `check_rc3.py` confirms the four conditions for the `b` term, with the rotation condition tested on the three-fold turn, and the speeds `0.858579` and `1.141421` at `m₀=1`, `b=0.1`.]

**What RC3 means.** On two copies the antiunitary loses its force on copy-mixing terms. C4's second witness, which (Θ) excludes on one copy, returns when it is paired with the imaginary `σ_y`. So two copies with equal diagonal speeds need not share one cone. Theorem 4.2 stays correct as a sufficiency statement.

---

## 5. MT1 imports: the draft's revision against the frozen `MT1.md`

The draft read `MT1.md` at `c2bfcd143` (SHA-256 prefix `c8263124f7df9bea`, 140 lines). The folder now holds the frozen `MT1.md` from `9daf65234` (prefix `232569f4b008ce8f`, 246 lines). `LZ1.md` line 148 asks for a reconciliation. Each import that the draft or `LZ1.md` uses was compared line by line [check: Python string comparison of the two revisions].

| Import | Old lines | Frozen lines | Change | Effect on LZ1 |
|---|---|---|---|---|
| Setting paragraph | 17 | 19 | One sentence added on the `L5-O` free node at `K+(π,π,π)` (MT1 referee edit E4). | None. LZ1 uses no `L5-O` free-node formula. |
| Cell matrices `A_j`, `Z_j`, `Γ_j=iZ_jA_j` | 19-24 | 21-26 | None. | None. |
| ER and the Clifford condition | 32 | 34 | None. | None. |
| Theorem 4 (six generators, 64-monomial basis, rotation rules) | 60-67 | 62-69 | None. | None. |
| Theorem 6 (centre and matter parity) | 75, 77 | 77, 79 | The frozen text names the centre elements, "`e^{iπ𝒢_x}` on `L_cube`, `Γ_x(−1)` on U, and `ω_x` on O[S_+]", and states that on every even torus the product of all centres equals `(−1)^N` (edits E7, E10). | None. LZ1 uses only the local identity `θ=Ad∏_{z∈Λ}c_z`, which is unchanged. `Γ_x(−1)=e^{iπQ_x}`, as in `LZ1.md` line 21. |
| Theorem 7 (free node, `G_j=UΓ_jU^*`, `v=sin ε/√3`) | 83-90 | 85-92 | None. | None. |
| Correction `χ_G=UχU^*` | 92 | 94 | "for generic `ε`" becomes "for every `ε` in the window". | None. |
| Theorem 10 and its proof (inversion lift `±A_1A_2A_3`, `D_r`) | 116, 118 | 118, 120 | Statement: "It is the leading term" becomes "The added term is the leading term". Proof unchanged. | None. |
| `σ=M_e^{−1}τ` and its node form | 120 | 122 | The old line had "**GAP:** those scripts are unavailable, and no proof of this classification is supplied here." The frozen line cites C3 (`σ̂(0)=cχ_G`) and C4 (the classification). | The draft took both from `MT1_REFEREE.md`. They are now in `MT1.md` itself. |
| MT1-S | 134 | 136 | None. | None. |
| Attack A1 | 136 | 138 | The frozen text adds "On L5-O two more steps fail: no antiunitary symmetry of the dressed tick is known, and the dressed lifts act on bare matter in the exchanged form of C7." | Theorem 5.2 supplies an antiunitary symmetry of the dressed `L5-O[S_+]` tick, so the first step, as worded, no longer fails. The charged-node form of `Θ` stays open (`LZ1.md` line 118; recommended edit R1). |
| Counterexample sentence | 140 | 142 | "No counterexample to MT1-S is supplied." becomes "No counterexample to MT1-S is known. The leading generator of the light fermion-odd excitations of an interacting state is not yet defined; on L5-O their gauge dressing also needs specification." | Consistent with LZ1. Corollary 2.3 holds under the proposed reading R-loc, which supplies a definition of the leading generator (G1). |
| C4 (Proposition C) | `MT1_REFEREE.md` 189-215 | `MT1.md` 180-205 | Identical apart from the closure tag. | None. Theorem 5.1 and RC3 use it. |

**Result.** No import that `LZ1.md` uses changed in content between the two revisions. Line numbers moved by two. The request at `LZ1.md` line 148 is answered (recommended edit R2).

---

## 6. Required edits

Each edit fixes one ERROR or INCOMPLETE item. None changes the content of a proved theorem.

- **E1 (item 2, line 7).** (a) Replace "Theorems 4.1–4.3 and 6.1" by "Theorems 4.1, 4.2 and 6.1". (b) Replace "half filling plus exponential Gauss-charge clustering produces static physical-sector spectral weight arbitrarily close to zero momentum" by "a stationary, site-transitive, half-filled state with exponential Gauss-charge clustering has static physical-sector spectral weight arbitrarily close to zero momentum". (c) Replace "A specified multiplicity-one node representation forces" by "A node fibre carried by a unitary, up to phases, onto the free node representation forces".
- **E2 (item 14, line 17).** Replace the sentence that defines the update class by: "A **gauge-invariant update of the same form** appends finitely many layers. Each layer is a family of finite-support gates that is closed under the even translations and has finitely many gates per cell. The gates of a layer commute pairwise, and each gate commutes with every local gauge transformation (`LW1.md` E1)." In G7, add "and pairwise commuting gates" to the list of properties.
- **E3 (item 25, line 49).** Replace "The fermion clause of LZ1 is incompatible with a propagating odd band in this reading; if there are no odd bands it may be vacuous." by "Under R-loc every odd light species of a D1 state is flat. So the fermion clause of LZ1 fails in every D1 state that has an odd light species, and holds only vacuously in a D1 state that has none."
- **E4 (item 42, line 95).** Replace "assume a finite-dimensional node fibre `E` has, up to phases, exactly one copy of the free `L5-U` node representation `C⁸⊗C⁵`: rotations ..., and the fundamental `1⊗U(5)`" by "let `E` be a finite-dimensional node fibre, and let a unitary `T:E→C⁸⊗C⁵` carry its rotations, inversion, antiunitary, `σ` and `U(5)` action, up to phases, to `ρ̂(Q)⊗1`, `ρ̂_I⊗1`, `(D_rK)⊗K₅`, `σ=cχ_G⊗1` and the fundamental `1⊗U(5)`". In G3 (line 9), replace "Multiplicity one" by "Unitary equivalence of the node fibre with the free node representation".
- **E5 (item 52, line 132).** Add to the scope note of the D2–D4 row: "D4 counts flat bands and bands outside `H_phys`. With R-loc this decides LZ1(a) negatively on `L5-O[S_+]` in every locally gauge-invariant, stationary, cell-invariant state (`LZ1_REFEREE.md` RC1)."

**Recommended, not required.**

- R1. Line 118: cite frozen `MT1.md` line 138 for the missing `L5-O` antiunitary ("On L5-O two more steps fail: no antiunitary symmetry of the dressed tick is known, ..."). C6 says only that its argument "does not apply to L5-O".
- R2. Line 148: replace "The `MT1.md` source revision differs from the draft's reported input and must be reconciled before relying on its precise imports." by "`LZ1_REFEREE.md` §5 compares the imports; none changed in content."
- R3. Lines 63, 67 and G2: add RC1(a) and (c)(i). In the exponential case the last clause of Theorem 3.2 holds under R-loc with D2–D4, without R-SC.
- R4. Line 67 and G8: add RC2. The tracial state lies in the class; it is not offered as the vacuum.
- R5. Line 79 and G9: add RC1(b) and (c)(ii). In a locally gauge-invariant state the clustering hypothesis holds automatically, and the static vectors form flat bands outside `H_phys`.
- R6. After Theorem 4.2 and in G5: add RC3, the copy-mixing term.
- R7. G2 and G4: state each as a missing step in the draft's inference, not as a proved non-implication about the law.

## 7. Open statements to carry by name

- **LZ1-i** (`LZ1.md` line 146): one common speed for all propagating light species, with the dispersion correction, the leading Lorentz-violating operator and its one-loop coefficient. Three attacks failed at named steps. A1 (symmetry) fails at "the node symmetries relate the speeds of different blocks": Theorem 4.2 and RC3 give covariant multi-speed triples. This is a representation-level failure, not a dynamical no-go. A2 (continuity from the free node) fails at "the free node continues to a propagating odd band of the vacuum representation": Theorem 2.2 excludes it under R-loc, and a charged-sector continuation needs R-CS. A3 (renormalization) fails at "a controlled flow exists" (ZM1-i) and at "the approach is a power law". The kill attempt K is a failed search, not a no-go.
- **MT1-S[R-CS]**: needs R-CS. On `L5-U` at `μ=τ_E=0`, Theorem 5.1 (with E4) gives a sufficient route if the node fibre is the free node representation and `a≠0`. On `L5-O`, C7 and the charged-node action of `Θ_O` remain.
- **R-CS**: the charged-sector prescription, an owner question shared with CH1's charged-correlator prescription.
- **D4 scope** (from RC1): whether a light species must propagate, or an even species must lie in `H_phys`. A specification question for the owner. This report proposes none.
- **Carried unchanged from `LZ1.md` line 11:** ZM1-i; the `L5-O` lift ambiguity C7 and the charged-node action of `Θ`; GA1-P-5; VC1 and LW1-5U-PS7; the rate and one-loop coefficient clauses of LZ1(a).

## 8. Freeze recommendation

Freeze `LZ1.md` after edits E1-E5. None of them changes a proved theorem. The three ERRORs are a summary line with a wrong theorem range and a dropped hypothesis, a reversed sentence, and a hypothesis whose wording admits a counterexample. E4 restores the draft's hypothesis, under which the proof of Theorem 5.1 is complete. E2 states the condition under which the tick automorphism exists; every theorem holds under it. The two INCOMPLETE items need one or two sentences each. All nine GAPs are real, and `LZ1.md` states each one correctly. Record RC1-RC3 as referee closures; they are unrefereed. Pass RC1(c) to the owner with the freeze: with D4 as written, R-loc decides LZ1(a) negatively on `L5-O[S_+]` in every locally gauge-invariant, stationary, cell-invariant state, through the static Gauss background. LZ1 stays open, with LZ1-i and MT1-S[R-CS] carried by name. R-loc, R-CS, R-SC, R-SC\* and D2-D5 stay proposals; nothing here adopts them.

---

## FINISH

**Proved** (in this file; written out in §§2-4; unrefereed).

- Every theorem of `LZ1.md`, re-derived by hand: Theorems 2.1, 2.2, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2, 5.1 (with the hypothesis of E4), 5.2 and 6.1, and Corollary 2.3 (with the wording of E3).
- RC1(a): in a stationary cell-invariant state, a conserved local observable with positive variance and exponentially decaying connected correlation generates a flat band (`d=1`, `V≡1`) on its cyclic translation subspace. Lemma RC1.0 (the zero set of a nonzero real-analytic function is null) is rebuilt.
- RC1(b): in a locally gauge-invariant state, the non-abelian Gauss generators at a site have zero mean and zero connected correlation at every `β≠0`. Their vectors generate flat bands with constant spectral density, orthogonal to `H_phys`.
- RC1(c): under R-loc with D2–D4 as written, LZ1(a) fails on `L5-O[S_+]` in every locally gauge-invariant, stationary, cell-invariant state of every update in §1, for all constants. It fails on `L5-U` in every such state with a non-sharp `SU(5)` Gauss generator. Without R-SC, it fails in every stationary, site-transitive, half-filled `L5-U` state with exponential Gauss-charge clustering.
- RC2: the tracial state of `L5-U[m]` lies in the class of the last clause of Theorem 3.2.
- RC3: on two copies of the free node representation, the covariant Hermitian triples are exactly `G_j⊗1₅⊗M+b·UZ_j(A_k+A_l)U^*⊗1₅⊗σ_y`, with `M` real symmetric and `b` real.
- §5: no MT1 import of LZ1 changed in content between `MT1.md` `c8263124f7df9bea` and the frozen `232569f4b008ce8f`.

**Counterexamples.**

- To Theorem 5.1 read with "exactly one copy" as multiplicity one inside a larger fibre: `E=(C⁸⊗C⁵)⊕(C⁸⊗C⁵)`, with `U(5)` acting by `u` on the first summand and by `ū` on the second, and `N_j=aG_j⊗1₅⊕a′G_j⊗1₅` with `a²≠a′²` (item 42).
- To "on two copies, equal diagonal speeds and the node symmetries give one cone": `m₀G_j⊗1₅⊗1₂+b·UZ_j(A_k+A_l)U^*⊗1₅⊗σ_y` with `m₀b≠0`, whose speeds along `e₁` are `|m₀±√2b|` (RC3).
- To LZ1(a) read by R-loc with D2–D4 as written, on `L5-O[S_+]`: every locally gauge-invariant, stationary, cell-invariant state (RC1(c)). The tracial state is one (`LW1_5.md` E2b-5: "the tracial state supplies one").
- To "the class of the last clause of Theorem 3.2 may be empty": the tracial state of `L5-U[m]` (RC2).

**Open by name.** LZ1-i, after three failed attacks: A1 (symmetry) at "the node symmetries relate the speeds of different blocks", A2 (continuity) at "the free node continues to a propagating odd band of the vacuum representation", A3 (renormalization) at "a controlled flow exists"; the kill attempt K is a failed search. MT1-S[R-CS]. R-CS. The D4 scope specification. ZM1-i. C7 and the charged-node action of `Θ_O`. GA1-P-5. VC1 and LW1-5U-PS7. The rate and one-loop coefficient clauses of LZ1(a).

**What changes downstream.**

- `LZ1.md`: edits E1-E5, then freeze. LZ1 stays open.
- Any part that reads LZ1 or MT1-S through R-loc: D4 as written counts static flat bands, including unphysical ones, as light species (RC1). With it, LZ1(a) is false on `L5-O[S_+]` in every locally gauge-invariant, stationary, cell-invariant state. Before R-loc can carry LZ1 on `L5-O`, light species need a specification (for example: propagating, or in `H_phys`). That is the owner's call.
- `L5-U`, VC1 and PS-7 (LW1-5U-PS7): the tension of Theorem 3.2 holds under R-loc with D2–D4 alone in the exponential case (RC1(c)), and its class is not empty (RC2). Which escape VC1's vacuum takes stays open.
- MT1: no change. The frozen `MT1.md` supplies the same imports (§5). Corollary 2.3 stays a result under R-loc, consistent with `MT1.md` line 142.
- MT1-S[R-CS] on `L5-U`: Theorem 5.1 needs the whole node fibre to be the free node representation. A fibre that also carries the antifundamental, or two copies, admits several speeds (item 42, RC3).
- No working-set entry, axiom, law or reading changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
