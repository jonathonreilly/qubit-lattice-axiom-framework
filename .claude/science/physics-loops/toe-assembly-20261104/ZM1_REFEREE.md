lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# ZM1 referee report (pass 3)

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 3, the referee, of part ZM1 under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen. The lane is a Claude long-form lane run to closure.

**Referee.** Claude Opus 5.5 (model id `claude-opus-5-5`), max effort, headless, 2026-11-06. This session wrote neither pass 1 (`ZM1_DRAFT.md`) nor pass 2 (`ZM1.md`). This is one check: one line-by-line read of the whole part. It reads no other review.

**What this file is.** A referee report. It grants no status. It adopts no law, reading or definition, and it changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. A "referee closure" (R1–R6, §4) is a complete argument written here for a missing or disputed step. Each closure is itself unrefereed. "[check]" marks a small scratch computation (§5). A check guides and never proves.

**Text read.** `ZM1.md` at commit `064054508`, its last commit. SHA-256 `1a5c624fcada8c46ff2b92c644c04e72e644f3101809443667348744f2b0b7c7`. Line numbers below refer to that file. The branch head was `064054508` when the read began and `e9e8234c1` when this file was written. The two later commits touch only `EW1.md` and `EW1_DRAFT.md`.

**Source revisions read.**

| File (this folder unless stated) | Last commit | SHA-256, first 16 | Lines read |
|---|---|---|---|
| `ZM1.md` | `064054508` | `1a5c624fcada8c46` | 1–331 (all) |
| `ZM1_DRAFT.md` | `350be1b41` | `71a64958276dd35e` | 1–383 (all); this is the hash ZM1 records |
| `LW1.md` (frozen) | `4b65c608f` | `78280bd620800eac` | 1–75, 107, 180–250, 316–400 |
| `LW1_5.md` (frozen) | `271c868a4` | `7afb7ee2a52d91cd` | 1–140, 250–330 |
| `MT1.md` (frozen) | `9daf65234` | `232569f4b008ce8f` | 1–100; the pass-2 text at `dfe1706ec`, lines 38, 80–90, 124 |
| `GA2_Y2.md` (frozen) | `bf403a16a` | `25db8a18aff1d30f` | 15–34, 88, 169 |
| `TOE_ASSEMBLY.md` | `7d2b20d29` | `8027d9d44eb5fcaf` | 180–184, 200–278 |
| `LZ1.md` | `03709a6a0` | not taken | lines 11 and 146 (grep for "ZM1") |
| `LW1_REFEREE.md`, `Y2W_DRAFT.md` | not taken | not taken | 1–80 and section headings; 1–30 (format only) |
| YM branch `origin/claude/ym4d-hard-route` at `5b070b6421` (after `git fetch -q`), file `.claude/science/physics-loops/ym4d-hard-route-20261030/library/a1-balaban.md`, last changed `e205de8bb` | | | 15–25; line 21 also at `f8bb65831`, the commit pass 1 read |
| `AGENTS.md`, `CLAUDE.md`, `docs/ai_methodology/SCIENCE_WORKFLOW.md` | | | all |

Not read: `VC1_5.md` and `TM1.md`, which ZM1's provenance names but no proof step uses; the arXiv papers that pass 1 cites (Attack 3 cites one; it is not load-bearing); the audit ledger; any other referee report.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The working-set entries and both five-mode laws are read plainly. This report proposes no reading for adoption. Three items carry the four tests: the repaired words of Z0 (R2), the class `ℒ` of linear fields (R4) and the precise ZM1-I1 (R6). Each restates or extends text that ZM1 already contains.

**Working set used, by name.** PS-1c (cell covariance: Definition Z, Theorems Z0 and Z2, R1, R2). PS-5 (five modes per site: Corollaries Z1.1 and Z2.1, R3). PS-6r (finite link registers: Theorems Z3 and Z4, Attack 2, R4, R6). PS-7r (the free sea: Theorem Z2(4), R5). Both five-mode laws are live (`TOE_ASSEMBLY.md` §3.5, owner decision LW1-5-RQ). Not used: PS-2, PS-3 and its readings, PS-4, PS-11c, PS-Ar.

**Inputs from outside the working set.** Standard mathematics, rebuilt where used: Hadamard's determinant inequality, from the QR factorization (R5). Standard facts cited, not rebuilt: the C*-norm identity `‖a b‖ = ‖a‖ ‖b‖` for elements of two commuting tensor factors; the norm of a normal element equals its spectral radius. Wick's determinant rule enters as part of LW1's definition of a gauge-invariant quasi-free state (`LW1.md` line 107). The vanishing of gauge-charged correlators in a gauge-invariant state (R6) is elementary. It is in the spirit of S. Elitzur's 1975 theorem on local gauge symmetry, credited from memory and not used as a proof step.

**Method.** I re-derived each statement and proof step of `ZM1.md` by hand. I compared each quoted source line with the source file at the commit above. Verdicts: CORRECT; ERROR (a false line, quoted, with the fix); INCOMPLETE (a named missing step, with what is missing).

**Counts.** 103 items: 89 CORRECT, 10 ERROR, 4 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a theorem. The distiller marked seven GAPs (§0, line 9). One is not real (Z2-cov). Two are closed here (Z0-index; the infinite tails of Attack 1). One is closed in part (Z2-spatial, its Wick item). Three are real and stay (Attack 3; the reach of Attack 2; the massive dynamical limit).

---

## 1. Verdict table

| # | Item (ZM1 line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status paragraph (5) | CORRECT | |
| 2 | §0 "Proved within the stated scopes" (7) | CORRECT | Matches the body. Its two qualifiers ("indexing", "covariance") lapse with R2 and R1. |
| 3 | §0 GAP list (9) | ERROR | "Z2-cov: the kernel covariance proof uses the wrong rotation centre" is false (§2.2, R1). The infinite-tail clause is closed by R4. |
| 4 | §0 open-by-name list (11) | CORRECT | For the attack count on ZM1-I1 see #101. |
| 5 | §0 provenance (13) | CORRECT | Draft SHA-256 and source HEAD `350be1b4…` verified. |
| 6 | §1.1 notation (19–25) | CORRECT | Here a coarse cell is one block `β_u`, with eight coarse sites `(u, r)`. Section 4 uses this convention. |
| 7 | §1.2 B10 quotes (30) | CORRECT | Exact; `LW1.md` 324–326, 329, 335, 339–340. |
| 8 | §1.2 C1 quote (31) | CORRECT | Exact; `LW1.md` 372–375. |
| 9 | §1.2 factorization quotes (32) | CORRECT | `LW1.md` 196; `LW1_5.md` 314. |
| 10 | §1.2 A2 quotes (33) | CORRECT | `LW1.md` 209, 213. |
| 11 | §1.2 B4, G, U quotes (34) | CORRECT | `LW1.md` 241; `LW1_5.md` 128, 136. |
| 12 | §1.2 A2-5 quote and its reading (35) | CORRECT | `LW1_5.md` 257. |
| 13 | §1.2 MT1 Theorem 1 quote (36) | CORRECT | Pass-2 line 38; line 40 of the frozen file, same text. |
| 14 | §1.2 MT1 Theorems 7, 11 and `UΓ_jU* = Γ_j e^{-iεR_e}` (37) | CORRECT | Pass-2 lines 83–87 (cited as 82–86) and 124; frozen 85–89 and 126; same text. |
| 15 | §1.2 GA2_Y2 Theorem 3.4 quote (38) | CORRECT | `GA2_Y2.md` 88. |
| 16 | Definition Z (42–50) | CORRECT | `B_u` is indexed by coarse sites, `β_u` by blocks; R2 fixes the words. |
| 17 | Four-test check of Definition Z (52–57) | CORRECT | A recorded assessment. Test 4 is conditional, as the text says. |
| 18 | Definition G and the representative-site remark (61–65) | CORRECT | The first person "I" is pass 1's. The YM file credits the construction to Ethan Sussman and Levent Alpoge (edit E18). |
| 19 | Four tests of Definition G (67) | CORRECT | |
| 20 | Q-E, Q-F, Q-I (72–74) | CORRECT | |
| 21 | GAP Z0-index (82) | CORRECT | Real, as an indexing fault. No claim of Z0 depends on it (R2). |
| 22 | Theorem Z0 statement (84–89) | CORRECT | Holds on Z0's own coarse lattice (R2). |
| 23 | Z0 proof (1)–(2) (91) | CORRECT | Edge-triple factors are supported on one fine edge (`LW1.md` 205). |
| 24 | Z0 proof (3) (91) | ERROR | "A coarse cell translation is a fine translation by `2L` times an integer vector": with coarse cells of `2 x 2 x 2` blocks it is `4L`. The rest of (3) is correct. |
| 25 | Z0 proof (4)–(5) (91) | CORRECT | `D = 2^{2 n_s 8L^3} d_l^{48L^3}` recounted. |
| 26 | Plaquette-layer remark (93) | CORRECT | |
| 27 | "What Z0 says" (95) | CORRECT | Its last sentence lapses with R2. |
| 28 | §3.2 setup (99) | CORRECT | `a`, `b` agree with `LW1.md` line 107. |
| 29 | Lemma Z1a statement (101–104) | CORRECT | |
| 30 | Lemma Z1a proof, (i) and (ii) (106) | CORRECT | |
| 31 | Lemma Z1a proof, (iii) (106) | CORRECT | The step from "a subinterval" to "an open set" holds; see §3.2. |
| 32 | Theorem Z1 statement (108) | INCOMPLETE | For `L5-O`, Definition Z allows real Majorana maps (line 50). The theorem treats complex `J` only. Closed by R3. |
| 33 | Z1 Step 1 (110) | CORRECT | |
| 34 | Z1 Step 2 (112) | CORRECT | `V_1 = J*V^nJ` commutes with coarse translations, so it is fibred. |
| 35 | Z1 Step 3 (114) | CORRECT | |
| 36 | Z1 Step 4 (116) | CORRECT | |
| 37 | Z1 Step 5 (118) | CORRECT | |
| 38 | Corollary Z1.1 and proof (120–125) | CORRECT | For `L5-O` read "modes" as Majorana modes (R3); the conclusions are unchanged. |
| 39 | Scope paragraph (127) | CORRECT | |
| 40 | Named failing step (129) | ERROR | "So any zoom of the free tick with bounded content has a nonzero error" exceeds Z1's quasi-free scope, which line 127 states. |
| 41 | §4 setup (135) | CORRECT | |
| 42 | Lemma Z2.0(1) and proof (139–144) | CORRECT | |
| 43 | Lemma Z2.0(2) and proof | CORRECT | Odd-edge fibre re-derived. |
| 44 | Lemma Z2.0(3) and proof | CORRECT | |
| 45 | [check] (146) | CORRECT | A report; rerun with independent code (§5). |
| 46 | Generator and sea (150) | CORRECT | Matches `LW1.md` 107: eigenvalue `e^{-iw}`, `P = 1_{(-π,0)}`. |
| 47 | Lemma Z2.1(1) and proof (152–161) | CORRECT | |
| 48 | Lemma Z2.1(2) and proof (163) | CORRECT | Constants 0.0992, 0.448, 0.152 rechecked. |
| 49 | Lemma Z2.1(3) and proof (165) | CORRECT | |
| 50 | [check] (167) | CORRECT | Rerun: 0.0646. |
| 51 | Lemma Z2.2(1) and proof (171–176) | CORRECT | |
| 52 | Lemma Z2.2(2) | CORRECT | |
| 53 | Lemma Z2.2(3) and proof | CORRECT | |
| 54 | Remark after Z2.2 (178) | ERROR | "the cubic part of the spectrum, the anisotropy `-T_4(n) k^2/24`": the cubic part also contains the isotropic term `s^2/72` of C1. |
| 55 | GAP Z2-cov (182) | ERROR | Not real. In §4 a coarse cell is one block (§1.1 and the formula for `J_L`), so the rotation centre is right. R1 supplies the phase relation. |
| 56 | Lemma Z2.3 (1) and (5), with proof (184–198) | CORRECT | Constants 0.28, 0.078, 2.17, 27.7, 1.75 rechecked. |
| 57 | Lemma Z2.3 (2) (199) | CORRECT | |
| 58 | Lemma Z2.3 (3) (200) | CORRECT | Holds for both parities of `L` (§3.3). |
| 59 | Lemma Z2.3 (4) (201) | CORRECT | |
| 60 | Three dimensions: isometry, fibre formula, leakage (191, 202) | CORRECT | |
| 61 | Covariance claim and proof (191, 202) | CORRECT | For even `L` the fine lift is an even translation times the cell lift (R1). |
| 62 | [check] (204) | CORRECT | Rerun: 0.0054. |
| 63 | Lemma Z2.4 and proof (208–210) | CORRECT | |
| 64 | `W`, `J̃_L`, `Φ_L`, coarse law (214–218) | CORRECT | |
| 65 | Theorem Z2(1) and proof (1) (221, 233) | CORRECT | Drop "subject to GAP Z2-cov" (R1). |
| 66 | Theorem Z2(2) and proof (2) (222, 235) | CORRECT | |
| 67 | Theorem Z2(3) statement (223–226) | CORRECT | |
| 68 | Proof (3), the part `m ≠ 0` (237) | CORRECT | |
| 69 | Proof (3), the reduction at `m = 0` (237) | CORRECT | |
| 70 | Proof (3), the bound on `E_1` (239–241) | ERROR | With `v ≤ 0.578` and `e^{0.866} ≤ 2.38` the first two terms are 0.516 and 0.298, not 0.515 and 0.297. The sum is 0.988 ≤ 0.99, so the conclusion stands. |
| 71 | Proof (3), conclusion `1.49 \|θ\|^3` (243) | CORRECT | |
| 72 | Theorem Z2(4) statement (227–231) | CORRECT | The `1 - P` clause is true but weaker than Corollary Z2.1 needs; see #80. |
| 73 | Proof (4), alias sum and the `l^2` bound (245) | CORRECT | Uses `‖P(ξ_m) - P(ξ_0)‖ ≤ 1`, a difference of two projections. |
| 74 | Proof (4), the gap `g = 2v\|θ\|/π` (245) | CORRECT | |
| 75 | Proof (4), the constants after Lemma Z2.4 (245) | ERROR | "`≤ 1.42 δ/g ≤ (3.34/v)\|θ\|^2`": `1.42 · 3π/4 = 3.346`. With `2/(2 - 3π/16) = 1.4175` one gets 3.340. The final `3.5/v` stands. |
| 76 | Proof (4), the `1 - P` clause (245) | CORRECT | |
| 77 | "Every two-point function … is a matrix element" (231) | CORRECT | Negative time differences use the adjoint. |
| 78 | [check] (247) | CORRECT | Rerun: 0.035 and 0.0020. |
| 79 | GAP Z2-spatial (249) | CORRECT | Real, at the level of the ZM1 target. Its Wick item is closed by R5(b). |
| 80 | Corollary Z2.1 statement (251–255) | INCOMPLETE | For `c c*`-type correlations the stated constant needs one identity (R5(a)). The anisotropy wording repeats #54. |
| 81 | Corollary Z2.1 proof (257) | CORRECT | |
| 82 | Corollary Z2.2 and proof (259–261) | CORRECT | Drop "conditional on covariance" (R1). [check] agrees. |
| 83 | Remark, massive free tick (263) | CORRECT | "In coarse units the mass is `Lμ`" holds while `Lμ < π`. |
| 84 | §5 Gauss generators (269) | ERROR | "`T in u(5)`": `LW1_5.md` line 93 has `T` Hermitian. |
| 85 | §5.1 pointer (273) | CORRECT | |
| 86 | Theorem Z4 and proof (277–279) | CORRECT | `n_0 = 5` also holds for `L5-O`, with `T_0 = Σ_j M^{2j-1,2j}` (§3.6). |
| 87 | Remark after Z4 (281) | CORRECT | |
| 88 | Theorem Z3 statement (285–289) | CORRECT | Extended to norm limits by R4. |
| 89 | Z3 proof (a) (291) | CORRECT | |
| 90 | Z3 proof (b) (293) | CORRECT | |
| 91 | Z3 proof (c) (295–299) | CORRECT | |
| 92 | Z3 proof (d) (301) | CORRECT | |
| 93 | Remark on `GA2_Y2.md` Theorem 2.1 (303) | ERROR | That theorem says an invertible covariant link has `τ = 0`. "No nonzero normal operator carries a charge" is step (d) here, not Theorem 2.1. |
| 94 | Corollary Z3.1 (305) | CORRECT | Extends with R4. |
| 95 | Scope of Z3 and the dressed example (307) | CORRECT | (G1)–(G2) are properties of a map; the example has the matching gauge charges. |
| 96 | ZM1-I1 statement (311) | INCOMPLETE | The quantifiers on `κ`, `t`, `C` and the coarse state `ω_1` are missing. With locally gauge-invariant vacua its comparison reduces to same-site terms (R6). |
| 97 | Comment after ZM1-I1 (313) | CORRECT | Infinite tails are now covered (R4). |
| 98 | Attack 1 (315) | CORRECT | The failing step holds for finite sums. R4 closes the infinite-tail case. |
| 99 | Attack 2 (317) | ERROR | The named step fails, by `GA2_Y2.md` Theorem 3.4. But the setup "`w δ_{x_u} = J̃_L e_u`" cannot hold for a finite circuit: at `L = 2`, `J̃_L e_u` has infinite support (§3.8). Use a truncation. |
| 100 | GAP Attack 3 (319) | CORRECT | Real. |
| 101 | Attack 3 (321) | INCOMPLETE | Valid in its narrowed form for the subspace (tile-projection) notion it cites. That notion is not Definition Z, whose `Φ` is unital. So it is not an attack on ZM1-I1 as stated; the bridge is missing. |
| 102 | Closing line of §5.4 (323) | CORRECT | |
| 103 | §6 (327–331) | CORRECT | |

## 2. The distiller's GAPs

### 2.1 GAP Z0-index (line 82): real, harmless, repaired

Line 82: "The draft calls each block both a coarse site and a coarse cell." This is true. Section 1.1 (line 19) makes the block `β_u` a coarse cell with eight coarse sites `(u, r)`. Theorem Z0 makes `β_u` a coarse site (line 84: "the coarse site algebra `B_u` … of the `8L^3` sites of `β_u`"). Its proof (3) then uses both: "A coarse cell translation is a fine translation by `2L` times an integer vector" (block = cell) and "A coarse cell is `2 x 2 x 2` coarse sites; its centre has fine coordinates `4Lb_i + 2L - 1/2`" (block = site).

The fault is in words only. With one convention, every item of Z0 holds as stated (R2). Line 82 also says "the proof does not establish PS-1c for the eight-site coarse-cell structure used in Z2." Z0 needs no such claim. Z0 and Z2 use different coarse systems, and each satisfies PS-1c in its own convention (R2 for Z0, R1 for Z2).

### 2.2 GAP Z2-cov (line 182): not real

Line 182: "The covariance paragraph below rotates about the centre of a single block while calling it the centre of a coarse cell of eight blocks. These are different points." The paragraph (line 202) says: "The coarse rotation about the centre of coarse cell 0 … The fine rotation about the centre of block `β_0` (site point `(L - 1/2)(1,1,1)`, a cube centre)". In §4 the coarse cell `u` is the block `β_u`. Section 1.1 says so, and the kernel shows it: `J_L |u, r, f> = Σ_c ψ^(3)(c - Lu) |2c + r, f>` sends the eight coarse sites of coarse cell `u` to the eight residue classes of fine sites around `β_u`. So the centre of coarse cell 0 is the centre of `β_0`. The "coarse cell of eight blocks" exists only in Z0's convention.

Line 182 also says: "It also asserts the same sign lift without proving its phase relation at the correct centre." R1 proves the relation in four lines. It is the fact that the fine rotation about `β_0`'s centre is an even translation composed with the cell lift about `c_0`. The [check] in §5 confirms the intertwining for `L = 2, 3, 4`. It also shows that the "eight-block" centre fails, as R1 predicts. So Lemma Z2.3's covariance claim, Theorem Z2(1) and Corollary Z2.2 hold without qualification. The block map `Φ_L` satisfies (Z-b).

### 2.3 GAP Z2-spatial (line 249): real at the level of the target; one item closed

Line 249 lists five limits: (i) "physical separation `r` alone does not imply that support"; (ii) the bound concerns "normalized band-limited two-point functions, not arbitrary separated local block observables"; (iii) "It also only controls times `t <= 1/κ`"; (iv) "Wick's rule gives higher functions but requires observable-dependent error bounds"; (v) no fixed point, tower, gauge sector or bound on irrelevant terms. Each is a true statement about what Theorem Z2 and Corollary Z2.1 prove. None marks a false step.

Item (iv) is closed by R5(b). Every `2n`-point function of unit band-limited block fields differs between the fine and the coarse sea by at most `n^{(n+2)/2}` times the two-point bound. So `p = 2` holds for every fixed `n`. Items (i), (ii), (iii) and (v) stay. Section 7 carries them as **Z2-spatial (residual)**.

### 2.4 GAP Attack 3 (line 319): real

Line 319: "The draft has not classified conserved projections or proved that every tile-local function of Gauss generators must omit every boundary matter degree of freedom." This is true. Pass 1 wrote (draft line 357): "The exactly conserved local projections of the dressed law at hand are the spectral projections of the Gauss generators." No proof of that classification is given anywhere. The pass-2 text drops it and keeps a narrowed attack (line 321). That narrowed attack is valid for its own construction; see #101 and §3.9 for its scope.

### 2.5 Attack 1, infinite tails (line 9; line 315): closed

Line 315: "For finite-support sums, Theorem Z3 forces every coefficient with `x != x_u` to vanish. The exponentially supported kernel in Z2 needs an additional limiting argument." R4 supplies it. Theorem Z3 holds for every element in the norm closure of finite linear sums with link coefficients. The proof replaces "matter matrix elements" by averages over the phase of one mode. Any norm limit of partial sums of the Attack 1 series therefore has zero coefficients off `x_u`. This contradicts the nonzero kernel. If no grouping of the partial sums converges in norm, the series defines no element of the algebra. Either way the attack fails at its named step.

### 2.6 Attack 2, reach (line 9; line 317): real, and correctly stated

Line 317: "The cited coherence bound excludes the stated near-coherent link criterion. It does not rule out every state-dependent approximation or every c-number reduction". This is an accurate statement of scope. `GA2_Y2.md` line 21 defines `κ = 2Σ|ω(U^{jk})|^2/ω(M)`. Near-c-number links have `κ` near 1, and Theorem 3.4 gives `κ ≤ 1/2` in every state. So the named step fails for every state. Other approximation schemes are not attacked. Attack 2 has a separate setup error (#99, §3.8).

### 2.7 Massive free tick (line 9; line 263): real, and correctly stated

Line 263 ends: "This proves exponential decay of these equal-time two-point functions, not absence of all long-distance dynamical content." The draft's sentence "The long-distance content of the massive free tick is empty" (draft line 295) had no proof. The distilled remark claims only what B10(4) gives. It is correct.

## 3. Details of the non-CORRECT items, and notes the verdicts rely on

### 3.1 The ten ERRORS, each with its fix

- **#3 (line 9).** "Z2-cov: the kernel covariance proof uses the wrong rotation centre." This is false (§2.2, R1). *Fix:* delete the clause. Replace "Attack 1 covers finite sums; an infinite-tail extension is unproved" by "Theorem Z3 also holds for norm limits of linear fields (R4)".
- **#24 (line 91, proof (3)).** "A coarse cell translation is a fine translation by `2L` times an integer vector, an even translation." In Z0 a coarse site is a block and a coarse cell is `2 x 2 x 2` blocks, as the next sentence of the proof uses. A coarse cell translation by `b` is then the fine translation by `4Lb`. *Fix:* write `4L`, and add: "translations by `2L` (one block) are also even translations, so `α_1` is covariant under them too." The rest of (3) is correct: the centre `4Lb + (2L - 1/2)(1,1,1)` is an odd-cube centre; LW1 A2 gives the lift; the reflection permutes blocks; the coarse group is transitive on coarse sites.
- **#40 (line 129).** "So any zoom of the free tick with bounded content has a nonzero error." Theorem Z1 concerns quasi-free maps, and line 127 says other maps are not decided. *Fix:* "So every quasi-free zoom of factor `L` with fewer than `L^3` modes per coarse cell has a nonzero error."
- **#54 (line 178), with the same words in #80 (line 255).** "The first term that a change of basis cannot remove is the cubic part of the spectrum, the anisotropy `-T_4(n) k^2/24` of `LW1.md` C1." LW1 C1 (lines 372–375) gives `w(k n) = (s k/√3)[1 + k^2(s^2/72 - T_4(n)/24) + O(k^4)]`. The cubic part `v k^3 (s^2/72 - T_4(n)/24)` contains an isotropic term. *Fix:* "…is the cubic part of the spectrum, `v k^3 (s^2/72 - T_4(n)/24)` by LW1 C1; its direction-dependent part is the anisotropy." At line 255, write "the first correction in the spectrum is the cubic term of LW1 C1, with relative size `(|θ|^2/L^2)(s^2/72 - T_4(n)/24)`; its direction-dependent part is the anisotropy".
- **#55 (line 182).** GAP Z2-cov. It is not real (§2.2). *Fix:* delete it, with the consequential edits of E7 (§6).
- **#70 (lines 239–241).** "Collecting, with `v <= 0.578` and `e^{0.866} <= 2.38`: … `‖E_1‖ <= (0.515 + 0.297 + 0.125 + 0.049)|θ|^3`". With those roundings, `(y^2/2)e^y ‖h_1‖ <= (3/8)(2.38)(0.578)|θ|^3 = 0.5159|θ|^3`, and `y e^y ‖h_2‖/L <= (0.866)(2.38)(0.578/2)(1/2)|θ|^3 = 0.2978|θ|^3`. With `v <= 1/√3` and `e^{√3/2}` exactly they are 0.5147 and 0.2972. *Fix:* "`(0.516 + 0.298 + 0.125 + 0.049)|θ|^3 = 0.988|θ|^3 <= 0.99|θ|^3`". The conclusion `‖A - h(θ)‖ <= 1.49|θ|^3` stands.
- **#75 (line 245).** "`<= 2δ/(2g - δ) <= 1.42 δ/g <= (3.34/v)|θ|^2`". With `δ/g = (3π/(4v))|θ|^2 <= 3π/16`, `1.42 δ/g` can reach `(3.346/v)|θ|^2`. *Fix:* `2δ/(2g - δ) <= (2/(2 - 3π/16)) δ/g <= 1.4175 δ/g <= (3.340/v)|θ|^2`. The final static bound `(3.5/v)|θ|^2` stands, since `3.340 + 0.15 < 3.5`.
- **#84 (line 269).** "`G^T_x = c_x^dag T c_x + sum_l r^dag_{l,x} T r_{l,x}` with `T in u(5)`". `LW1_5.md` line 93: "Here `T` is Hermitian". *Fix:* "with `T` a Hermitian `5 x 5` matrix".
- **#93 (line 303).** "The proof is the matter analogue of `GA2_Y2.md` Theorem 2.1: on a finite register no nonzero normal operator carries a charge." `GA2_Y2.md` line 30 reads: "If the operator link in Definition 1 is invertible and obeys either covariance equation, then `τ = 0`." Its Corollary 2.2 (line 34) reads: "`[E,U] = qU`, `E` Hermitian, `q ≠ 0`, has no invertible finite-dimensional solution." So GA2_Y2 proves non-invertibility. Step (d) here proves nilpotency, and step (c) supplies normality. *Fix:* "Step (d) strengthens `GA2_Y2.md` Theorem 2.1 and Corollary 2.2, which show that a charged operator on a finite register is not invertible: here it is nilpotent, so a normal one is zero."
- **#99 (line 317).** "chosen so that replacing every link operator `U^{jk}` by `δ^{jk}` turns `W` into `Γ(w)`, a one-body unitary with `w δ_{x_u} = J̃_L e_u`". A finite circuit of dressed hops reduces to a finite circuit of nearest-neighbour one-body gates. So `w` has finite range and `w δ_{x_u}` has finite support. At `L = 2`, `J̃_L e_u` has infinite support (§3.8), so no finite circuit meets the setup. *Fix:* "with `‖w δ_{x_u} - J̃_L e_u‖ <= C e^{-R/ξ}`, a truncation at radius `R`, using one `W` for all coarse modes". Theorem Z2 then applies to the reduced map up to that error. The named failing step is unchanged.

### 3.2 Lemma Z1a (iii): the open set (#31)

The proof differentiates `arccos x + arccos y = c` in `u = cos K_{i_0}`. That is legitimate at every point of the open set `U` where `x, y ∈ (-1, 1)`, so `x^2 = y^2` on `U`. Both `x - y = (2a/3) Σ_{i ∈ I_π} cos K_i` and `x + y = (2a/3) Σ_{i ∉ I_π} cos K_i - 2b` are real-analytic, and `x - y` vanishes on no open set. Off the zero set of `x - y`, which is closed with empty interior, `x + y = 0`. By continuity `x + y = 0` on `U`. This is the text's "on an open set". The rest follows as written.

### 3.3 Lemma Z2.3 (3) for both parities of `L` (#58)

Write `ψ̂(ξ) = e^{-i(L-1)ξ/2} ρ̃(ξ)` with `ρ̃` real and even. For odd `L` the phase is `2π`-periodic, and `ψ(n)` is the Fourier coefficient of `ρ̃` at `n - (L-1)/2`. For even `L` the phase is `2π`-antiperiodic, so `ρ̃` is antiperiodic. In both cases `ψ(n) = (1/2π) ∫_{-π}^{π} ρ̃(ξ) e^{i(n - (L-1)/2)ξ} dξ`. The substitution `ξ -> -ξ` shows that `ψ(n)` is real and that `ψ(L - 1 - n) = ψ(n)`. [check] agrees to `3·10^{-15}` at `L = 2, 3, 4`.

### 3.4 Theorem Z1 for `L5-O` (#32)

Line 50 defines the quasi-free block maps of `L5-O` by "its real Majorana form". Such a map may mix `c` and `c*`. Theorem Z1 (line 108) takes a complex isometry `J : l^2(Z^3) x C^d -> h`. Line 99 says the `L5-O` phase gauge "changes nothing below", which covers complex `J` only. R3 closes the real case. The conclusions of Corollary Z1.1 hold in Majorana units.

### 3.5 Corollary Z2.1 (#80)

Line 251: "every two-point correlation of `L` in its sea equals that of `L_k` in its sea up to `(3.5/v + 2.66 + 1.5)(2^k a/r)^2 ‖f‖ ‖g‖`". For correlations of type `c c*` the relevant operator has `1 - P`. Theorem Z2(4) (line 231) gives that case only "after adding the bound of (3)", which yields `(3.5/v + 8.32)κ^2` at `tκ <= 1`. The corollary's constant needs the identity of R5(a), which gives the `1 - P` case the same bound as the `P` case. With R5(a) the corollary holds as stated.

### 3.6 Theorem Z4 for `L5-O` (#86)

Take `T_0 = Σ_j M^{2j-1,2j}`. By `LW1_5.md` line 31 its matter part at `x` is `Σ_j (n_{x,j} - 1/2) = N_x - 5/2`. On `S_u` this takes `5|S_u| + 1` values. (G1) holds for this `T_0` by linearity of `Φ`. The proof of Z4 then gives `D_u >= 5|S_u| + 1` for `L5-O` as well. The stated `n_0 = 1` is true but weaker. This is an optional edit (E20).

### 3.7 ZM1-I1 (#96)

Line 311 states: "There are `L >= 2`, a block map `Φ` … and `p >= 1`, such that coarse fermion two-point functions smeared at coarse momenta `|θ| <= κ` have correlation error in `ω_0` at most `C (κ^p + t κ^{p+1})`." Three things are missing: the range of `κ` and `t`, the order of the quantifier on `C`, and the coarse state. Definition Z's correlation error uses "the coarse law's own state `ω_1`" (line 49). R6 gives the precise statement. R6 also proves a fact the lead needs before anyone works on ZM1-I1. If `ω_0` is invariant under every local gauge transformation, every charged two-point function between distinct coarse sites vanishes on the fine side. If `ω_1` is also locally gauge invariant and cell-translation invariant, the stated bound forces exact equality of the same-site terms for every `t`.

### 3.8 Attack 2: `J̃_2 e_u` has infinite support (#99)

The fibre is `J̃_L(θ) = Σ_m α_m(θ) ι_m(θ) W(θ)*`. So the fine Bloch transform of `J̃_L e_{u,r,f}` at the fine momentum `K = ξ_m(θ)` is a phase times `α_m(θ) W(θ)* e_{r,f}`. Since `W` is unitary, its norm is a fixed multiple of `|α_m(θ)| = L^{-3/2} |ψ̂^(3)(K)|`; the multiple depends only on the normalization of Bloch vectors. Each fine `K` arises from exactly one pair `(θ, m)`. A finitely supported vector has a trigonometric-polynomial Bloch transform. Its squared norm, a fixed multiple of `Π_i |ψ̂(K_i)|^2`, would then be a trigonometric polynomial. Since `ψ̂(0) ≠ 0`, setting `K_2 = K_3 = 0` would make `|ψ̂(k)|^2` one.

At `L = 2`, Lemma Z2.3's definitions give `B = 1 + e^{-ik}` and `G = 1 + cos k`. So `|â(k)|^2 = 2(1 + c)^3` with `c = cos k`. Then `g(θ) = (1 + cos(θ/2))^3 + (1 - cos(θ/2))^3 = 5 + 3 cos θ`, so `g(2k) = 2(1 + 3c^2)`. Hence `|ψ̂(k)|^2 = (1 + c)^3/(1 + 3c^2)`. An even trigonometric polynomial is a polynomial in `c`. This one is not, because `1 + 3c^2` has the roots `±i/√3`, where `(1 + c)^3` does not vanish. So `J̃_2 e_u` has infinite support. Whether `J̃_L e_u` has infinite support for every `L` is not needed and is not decided here.

### 3.9 Attack 3 (#101)

Line 321: "By arXiv:2511.23398 Theorem 1, an exact fermionic renormalisation needs a tile projection `Π_0` in the tile algebra with `[U_{T^N}, Π] = 0` for `Π` the product of its translates." Pass 1 records the cited notion (draft lines 48–49): "a subspace is selected in each tile". The coarse automaton then acts on `ran Π`. The operator map of such a renormalisation is a compression into `ΠAΠ`. It is unital in `A` only when `Π = 1`, and `Π = 1` is Theorem Z0's grouping. Definition Z asks for "a unital injective graded *-homomorphism `Φ : A_1 -> A`" (line 44). So a successful Attack 3 would not yet be a Definition-Z block map, and ZM1-I1 is stated with Definition Z. The bridge between the two notions is missing.

Within its own notion the narrowed attack is valid. A site on a lower face of a tile has an in-link owned by the neighbouring tile, so the joint Gauss projection of all sites of the tile is not in the tile algebra. The conditional rank bound is also correct. A function of the Gauss generators of the other sites acts as the identity on the matter of the lower-face sites, of which there are `3(2L)^2 - 6L + 1 >= (2L)^2`. So a nonzero such `Π_0` has rank at least `32^{(2L)^2}` on `L5-U`. *Fix:* state that Attack 3 attacks the subspace variant. ZM1-I1 as stated then has two failed attacks on file, Attacks 1 and 2.

## 4. Referee closures

Notation as in `ZM1.md` §1.1 and `MT1.md` line 28. `O` is the proper cubic rotation group, `Q e_j = σ_j e_{π(j)}`, `c_0 = (1/2)(1,1,1)`, `1 = (1,1,1)`. The cell lift about `c_0` is `ρ(Q)|2b + r> = s_Q(r) |2Qb + g_Q(r)>`, with `g_Q(r) = Q(r - c_0) + c_0`. MT1 Theorem 1 (frozen line 40): "Each `Q∈O` has a cell-periodic sign lift. It is unique up to a constant phase." MT1 line 28 defines a lift as "a site-permuting unitary with site phases … which commutes with both free half-step generators". The coarse lift `ρ_c(Q)` is the same formula on the coarse lattice.

### R1. Covariance of `J_L` and `J̃_L` (GAP Z2-cov is not real)

**Claim.** Fix `L >= 2` and `Q ∈ O`. Put `p = (L - 1/2) 1`, the centre of `β_0` and so of coarse cell 0. Put `t = p - c_0 = (L - 1) 1`, `p' = ((L-1)/2) 1`, and `F_Q = T_{(I-Q)t} ρ(Q)` (times `1_F`). Then:
1. `(I - Q)t ∈ 2Z^3`, so `F_Q` commutes with `R_e`, `R_o` and the free walk `V`;
2. `F_Q |2c + r> = s_Q(r) |2 Q̄(c) + g_Q(r)>` with `Q̄(c) = Q(c - p') + p'`;
3. `F_Q` moves sites by `x -> Q(x - p) + p`, the rotation about `p`;
4. every lift of that rotation equals `F_Q` times a constant phase;
5. `J_L ρ_c(Q) = F_Q J_L` and `J̃_L ρ_c(Q) = F_Q J̃_L`. For the centre of coarse cell `u_0` the same holds with `T^{(1)}_{u_0} ρ_c(Q) T^{(1)}_{-u_0}` and `T_{2L u_0} F_Q T_{-2L u_0}`.

*Proof.* (1) `Q1` has entries `±1`, so `1 - Q1` has entries `0` or `2`. Times `L - 1` it is even. `LW1.md` A2 proof, line 211: "Even translations preserve both tilings and every `η_i`." So the translation commutes with `R_e` and `R_o`. Line 213: "The signed permutation `D_dP_Q` consequently fixes both `R_e,R_o`". So `ρ(Q)` commutes with them too. (2) `ρ(Q)` sends `|2c + r>` to `s_Q(r)|2Qc + g_Q(r)>`. Adding `(I - Q)t = 2(I - Q)p'` gives the site `2(Qc + (I - Q)p') + g_Q(r) = 2Q̄(c) + g_Q(r)`. Note `(I - Q)p'` has entries `0` or `L - 1`, so `Q̄` maps `Z^3` to itself for both parities of `L`. (3) The site map is `x -> Q(x - c_0) + c_0 + (I - Q)(p - c_0) = Qx + (I - Q)p = Q(x - p) + p`. (4) Let `F'` be a lift of the same rotation. Then `F' F_Q^*` is diagonal with phases `d(x)` and commutes with `R_e` and `R_o`. Each edge `(x, y)` has a nonzero entry in one of them, so `d(x) = d(y)`. The lattice is connected, so `d` is constant. This is MT1 Theorem 1's uniqueness argument. (5) We have `J_L ρ_c(Q)|u, r> = s_Q(r) Σ_c ψ^(3)(c - LQu) |2c + g_Q(r)>`. By (2), `F_Q J_L |u, r> = s_Q(r) Σ_{c'} ψ^(3)(Q̄^{-1}(c') - Lu) |2c' + g_Q(r)>`. With `n = c' - LQu` one finds `Q̄^{-1}(c') - Lu = Q^{-1}(n - p') + p'`. All coordinates of `p'` are equal, so each coordinate of `Q^{-1}(n - p') + p'` is some `n_k` or `L - 1 - n_k`, each `k` once. By Lemma Z2.3(3) and the product form, `ψ^(3)(Q^{-1}(n - p') + p') = ψ^(3)(n)`. So the two sides agree. `𝒲` commutes with `ρ_c(Q)` by Lemma Z2.2(3), so `J̃_L = J_L 𝒲^*` intertwines too. The last sentence follows from `J_L T^{(1)}_u = T_{2Lu} J_L`. □

**Consequence.** Lemma Z2.3's final claim holds. `Φ_L = Γ(J̃_L)` satisfies (Z-b) with the fine lifts `Γ(F_Q)` and `Γ(T_{2Lu})`. Theorem Z2(1) and Corollary Z2.2 hold without qualification. For Corollary Z2.2 the `L5-O` lifts are the `W`-conjugates (`LW1_5.md` line 255). [check] `cov_check.py` agrees to `9·10^{-16}` for `L = 2, 3, 4` and all 24 rotations, with a nontrivial twist. Two controls fail as expected: a wrong residue sign (deviation 1.15), and the centre `(2L - 1/2)1` of a group of eight blocks (deviation 0.37).

### R2. Theorem Z0 on its own coarse lattice (GAP Z0-index repaired)

**Repaired statement.** In Theorem Z0 use these words. A *coarse site* is a block `β_u`, `u ∈ Z^3`, of side `2L` fine sites. A *coarse cell* is a group `{β_{2b + r'} : r' ∈ {0,1}^3}` of `2 x 2 x 2` blocks. A *coarse cell translation* by `b` is the fine translation by `4Lb`. The *centre* of coarse cell `b` is the fine point `4Lb + (2L - 1/2) 1`. With these words, items (1)–(5) of Theorem Z0 hold as stated, and the coarse system satisfies PS-1c.

*Proof.* Items (1), (2), (4) and (5) do not use the word "cell", and they hold as proved at line 91. For (3): `4Lb` is an even translation, and the dressed ticks commute with even translations (`LW1.md` 245–247; `LW1_5.md` 255, 259–267). The centre has integer part `4Lb + (2L - 1) 1`, odd in every coordinate, so it is an odd-cube centre. `LW1.md` A2 (line 213), "Rotations about other even or odd cube centres differ from these by even translations", gives the lift, and the same lines give the dressed covariance. The reflection `x_i -> 2p_i - x_i` maps the block boundaries `{2Lk - 1/2}` to `{2L(4b_i + 2 - k) - 1/2}`, so the rotations permute blocks. They act on the eight blocks of coarse cell `b` as the cube's rotation group acts on its vertices, which is transitive. With the cell translations the group is transitive on coarse sites. Translations by `2L` (one block) are also even, so `α_1` is covariant under them as well. □

This coarse lattice is not §1.1's lattice of factor `L`, where a block is a coarse cell. Z0 makes no claim about Z2's coarse system. A version in §1.1's words also holds. Let the coarse site `(u, r)` be the residue-`r` sites of `β_u`, with the links whose lower endpoint they are. Then the rotation step is R1(2)–(3). The range in (2) becomes "the coarse sites of the 27 coarse cells around `u`", and (5) reads `D = 2^{2 n_s L^3} d_l^{6L^3}`.

*Four tests.* R2 chooses one of the two meanings the text already uses. (1) It states no target. (2) It is closed. (3) It settles no physics; it names coarse sites and cells. (4) It adds no structure and no constant.

### R3. Theorem Z1 for the real Majorana block maps of `L5-O`

**Claim.** Let `O` be the real orthogonal one-body walk of the `L5-O` free tick on the Majorana space `l^2(Z^3; R^{10})`. Let `J_R : l^2(Z^3; R^d) -> l^2(Z^3; R^{10})` be a real isometry that commutes with coarse translations and has a summable kernel. If `O^n J_R = J_R O_1` for a bounded real `O_1`, then `d = L^3 r_M` with `1 <= r_M <= 80`. More precisely, `d = L^3 (d_+ + d_-)` with `0 <= d_± <= 40`, except when `2ε + μ = π` and `L`, `n` are both even; then `d = L^3 d'` with `d' <= 80`. In Majorana units Corollary Z1.1 holds unchanged. PS-5 content, 80 Majorana modes per coarse cell, forces `L = 2` and `r_M = 10`. No two-step exact tower exists.

*Proof.* Complexify: `J = J_R ⊗ 1_C`, `O_C = O ⊗ 1_C`. Then `J` is a complex isometry that commutes with coarse translations, has a summable kernel, and satisfies `O_C^n J = J O_{1,C}`. The free `L5-O` hop conserves number. `LW1_5.md` line 257: "Direct substitution gives `h^{O,free}_{xy} = i Σ_j (c^†_{y,j} c_{x,j} - c^†_{x,j} c_{y,j})`". So `O` preserves the complex structure of the Majoranas, and `l^2(Z^3; C^{10})` splits into an annihilator part and a creator part. On them `O_C` acts as `V' ⊗ 1_5` and `V̄' ⊗ 1_5`, with `V' = W V W^*` (`LW1_5.md` line 255) and the bar denoting complex conjugation in the site basis. The fibre of `V̄'` at `K` is `conj(V'(-K))`. `V'(K)` has eigenvalues `e^{±i w'(K)}` with `w'(K) = w(K - Π)`. Since `χ` is even, `w'` is even, so `conj(V'(-K))` has eigenvalues `e^{∓i w'(K)}`. Hence the fibre of `O_C` at `K` has the two eigenvalues `e^{±i w'(K)}`, each of multiplicity 40, with band projections continuous off the node `Π`. Steps 1–5 of Theorem Z1 use only these facts, the label shift `ξ_m(θ + 2πe_j) = ξ_{m+e_j}(θ)` and continuity. So they apply with `4F` replaced by 40. For the corollary: `L^3 r_M = 80` with `L >= 2` forces `L = 2`, since 27 and 64 do not divide 80. A two-step tower would need `(L_1 L_2)^3 >= 64` to divide 80. □

### R4. Theorem Z3′: linear block fermions, finite or infinite (closes the infinite tails of Attack 1)

**Definitions.** `𝔏` is the C*-algebra generated by all link operators. It commutes with matter (`LW1.md` line 52; `LW1_5.md` line 33). `ℒ` is the norm closure of the set of finite sums `Σ_α (T_α c_α + T'_α c^†_α)` with `T_α, T'_α ∈ 𝔏`. For a mode `α` and `φ ∈ R`, `θ^φ_α` is conjugation by `e^{iφ n_α}`. It sends `c_α` to `e^{-iφ} c_α` and fixes every other mode and `𝔏`. Put `Π^{(1)}_α(X) = (1/2π) ∫_0^{2π} e^{iφ} θ^φ_α(X) dφ` and `Π^{(2)}_α(X) = (1/2π) ∫_0^{2π} e^{-iφ} θ^φ_α(X) dφ`.

*Four tests* (for reading "linear in fine matter" as membership in `ℒ`). (1) It states no target. (2) It is closed. (3) It settles no physics; it only extends Z3's class to norm limits. (4) It adds no structure or constant.

**Coefficients.** `Π^{(1)}_α` and `Π^{(2)}_α` are contractions. On a finite sum they return `T_α c_α` and `T'_α c^†_α`. The map `T -> T c_α` is isometric on `𝔏`: `(T c_α)^*(T c_α) = T^*T n_α`, and `‖T^*T n_α‖ = ‖T^*T‖` because the two factors lie in commuting tensor factors. Its image is therefore closed. So each `X ∈ ℒ` has unique coefficients `T_α(X), T'_α(X) ∈ 𝔏` with `Π^{(1)}_α(X) = T_α(X) c_α` and `Π^{(2)}_α(X) = T'_α(X) c^†_α`. They depend continuously on `X`.

**Theorem Z3′.** Let `Φ` satisfy (G1) and (G2), and let `ψ` be as in Theorem Z3. If `Ψ = Φ(ψ) ∈ ℒ`, then `T_α(Ψ) = T'_α(Ψ) = 0` for every mode `α` at a site outside `S_u`.

*Proof.* (a) As in Z3, `Ψ` commutes with `H_T = Σ_{y ∈ S'} G^T_y` for every `T`; this step does not use finiteness. (b) `Ψ_1 = Ψ + Ψ^*` and `Ψ_2 = -i(Ψ - Ψ^*)` lie in `ℒ`, are Hermitian, square to 1 and commute with every `H_T`. By continuity `T_α(Ψ_1) = T_α + T'^*_α` and `T_α(Ψ_2) = -i(T_α - T'^*_α)`, and `T'_α(Ψ_k) = T_α(Ψ_k)^*`. So it suffices to show `S_α := T_α(Ψ_k) = 0` for `α` outside `S_u`.

(c) *Normality.* Fix `α_0` and write `c = c_{α_0}`, `n = n_{α_0}`, `S = S_{α_0}`, `A = S c + S^* c^†` and `R = Ψ_k - A`. Subtract the continuous `α_0`-parts from finite approximants of `Ψ_k`. This shows that `R` is a norm limit of odd finite sums over modes `β ≠ α_0`. So `R` is odd and lies in the C*-algebra `𝔅` generated by `𝔏` and the modes `β ≠ α_0`. Hence `R^2` is even in `𝔅`, commutes with `c` and `c^†`, and is fixed by `θ^φ_{α_0}`. Let `E_0(X) = (1/2π) ∫ θ^φ_{α_0}(X) dφ`. Then `E_0(AR + RA) = 0`, `E_0(A^2) = A^2 = SS^*(1 - n) + S^*S n` and `E_0(R^2) = R^2`. So `1 = E_0(Ψ_k^2) = SS^*(1 - n) + S^*S n + R^2`. Multiplying by `1 - n` and by `n` gives `(1 - n) Y_1 = 0` and `n Y_2 = 0`, with `Y_1 = SS^* + R^2 - 1` and `Y_2 = S^*S + R^2 - 1`. Both commute with `c` and `c^†`. Then `n Y_1 = c^†(1 - n) c Y_1 = c^†((1 - n)Y_1) c = 0`, so `Y_1 = 0`. Likewise `(1 - n) Y_2 = c (n Y_2) c^† = 0`, so `Y_2 = 0`. Hence `SS^* = 1 - R^2 = S^*S`.

(d) *Grading.* Fix `α = (x, j)` with `x ∈ S'`, and choose `T` as in Z3(d). Then `H_T = Σ_{y ∈ S'} n_{y,j} + const + Λ`, with `Λ ∈ 𝔏` Hermitian of finite spectrum `λ_1 < … < λ_N`. `θ^φ_α` fixes `H_T`, so `0 = Π^{(1)}_α([H_T, Ψ_k]) = [H_T, S_α c_α] = ([Λ, S_α] - S_α) c_α`. Injectivity of `T -> T c_α` gives `[Λ, S_α] = S_α`. With the spectral projections `P_i ∈ 𝔏` of `Λ`, this reads `(λ_i - λ_k - 1) P_i S_α P_k = 0`. So `S_α` maps each eigenspace into the next one up, and `S_α^N = 0`. `S_α` is normal by (c), and a normal element has norm equal to its spectral radius. So `S_α = 0`. □

**Consequence for Attack 1.** Let `Ψ_u` be the Attack 1 series (line 315). Suppose some grouping of its partial sums converges in norm. Then the limit lies in `ℒ`, and its coefficient at `(x, k)` is `J̃_{x,u} T^{jk}_{x -> x_u}`, because the coefficient maps are eventually constant on the partial sums. For `L5-U` the operators `r^y_j r^{x†}_k` on one link are linearly independent (`LW1_5.md` line 117). So along a path with distinct links the contracted product `T_{x -> x_u}` is nonzero. `J̃_L e_u` is not supported on one site, for every `L >= 2`. The norm of its fine Bloch transform is proportional to `|ψ̂^(3)(K)|` (§3.8). This is nonzero at `K = 0`, and zero at `K = 2πm/L` with `m ≢ 0 mod L`, because `B(2πm_i/L) = 0` when `m_i ≢ 0`. A one-site vector has a Bloch transform of constant norm. So `J̃_{x,u} ≠ 0` for some `x ≠ x_u`. Theorem Z3′ forbids this, so `Ψ_u` is not a fermion field. If no grouping converges, the series defines no element of the algebra. Corollary Z3.1 holds for `ℒ` with the same proof.

### R5. Corollary Z2.1 for every two-point function, and higher correlations

**(a) The `1 - P` case.** For `t ∈ N`, expand and use `J̃^* J̃ = 1`:
\[
 \tilde J^*(1-P)V^{Lt}\tilde J-(1-P_c)V^t=\tilde J^*(1-P)\big(V^{Lt}\tilde J-\tilde JV^t\big)-\big(\tilde J^*P\tilde J-P_c\big)V^t .
\]
The first term is bounded by Theorem Z2(3). The second is bounded by the static bound `(3.5/v)κ^2` of the proof of (4), since `V^t` keeps the momentum support. So the `1 - P` operator obeys the same bound as the `P` operator, `((3.5/v + 2.66)κ^2 + 1.5 t κ^3)‖f‖‖g‖`. With `tκ <= 1` this gives Corollary Z2.1's constant for every two-point function.

**(b) Normally ordered `2n`-point functions.** Let `n >= 1`, `T ∈ N`, `κ <= √v/2`, and `β = (3.5/v + 2.66)κ^2 + 1.5 T κ^3`. Let `u_1, …, u_n, w_1, …, w_n` be unit coarse one-body vectors with momentum support in `|θ| <= κ`, and let `s_i, s'_i ∈ {0, …, T}`. Let `F` be the fine sea expectation of `Π_i α^{L s_i}(Φ_L(c_1(u_i)))^* · Π_i α^{L s'_i}(Φ_L(c_1(w_i)))`, with the annihilators in reverse order. Let `F_c` be the coarse sea expectation of the same product with `α_1^{s}` in place of `α^{Ls}`. Then `|F - F_c| <= n^{(n+2)/2} β`.

*Proof.* `Φ_L(c_1(h)) = c(J̃h)`, and `α^{Ls}` sends `c(h')` to `c(V^{-Ls} h')`. Both seas are gauge-invariant quasi-free states. `LW1.md` line 107 defines them by "`ω_G(c_y^† c_x) = G_{xy}`, vanishing unequal-creation/annihilation moments, and Wick's determinant rule for the remaining moments". So `F = det M` with `M_{ik} = <w_i, J̃^* P V^{L(s'_i - s_k)} J̃ u_k>`, and `F_c = det N` with `N_{ik} = <w_i, P_c V^{s'_i - s_k} u_k>`. Here `P` commutes with `V`. Every entry has modulus at most 1. By Theorem Z2(4), and by its adjoint when `s'_i < s_k`, `|M_{ik} - N_{ik}| <= β`. Write `det M - det N = Σ_{k=1}^n det C_k`, where `C_k` has the columns `N_1, …, N_{k-1}, M_k - N_k, M_{k+1}, …, M_n`. Hadamard's inequality `|det C| <= Π_k ‖C e_k‖` follows from `C = QR`: `|det C| = Π_k |R_{kk}| <= Π_k ‖R e_k‖ = Π_k ‖C e_k‖`. The columns of `M` and `N` have norm at most `√n`, and `M_k - N_k` has norm at most `√n β`. So `|det C_k| <= n^{n/2} β`, and the sum is at most `n^{(n+2)/2} β`. □

Together with the CAR, the normally ordered functions determine all correlation functions of the block fields. So `p = 2` holds for every fixed number of band-limited fields. This closes item (iv) of GAP Z2-spatial and nothing more.

### R6. ZM1-I1: a precise statement, and what local gauge invariance does to it

**Precise statement (repair of line 311).** Let `ω_0` be a vacuum that VC1 supplies for `L5-U[m]` (base tick, or with a plaquette class that GA1-P-5 supplies). There exist `L >= 2`, `p >= 1`, `C, κ_0 > 0`, a block map `Φ` of factor `L` (Definition Z) satisfying (Z-a), (Z-b) and (G1)–(G2) with `|S_X| = 1` for every coarse site `X`, a coarse law `α_1` of the `L5-U` form, and an `α_1`-invariant state `ω_1` of `A_1`, with the following property. For all `κ ∈ (0, κ_0]`, all `t ∈ N` and all unit coarse one-body vectors `f, g` with momentum support in `|θ| <= κ`,
\[
 \big|\omega_0\big(\Phi(c_1(f))^*\,\alpha^{Lt}(\Phi(c_1(g)))\big)-\omega_1\big(c_1(f)^*\,\alpha_1^{t}(c_1(g))\big)\big|\le C(\kappa^p+t\kappa^{p+1}).
\]
*Four tests.* (1) It restates ZM1-I1 with its quantifiers; it fixes no target beyond line 311. (2) It is closed. (3) It settles no physics; the observable class is left as line 311 has it. (4) It adds the coarse state `ω_1`, which Definition Z's correlation error already uses (line 49), and no constant.

**Lemma R-GI.** Let `Φ` satisfy (G1)–(G2) with `S_X = {x_X}` for every coarse site `X`. Let `ψ_X` be a coarse matter annihilator at `X` with `[G^{(1),1}_X, ψ_X] = -ψ_X`, fixed by coarse gauge transformations at every `X' ≠ X`. Put `Ψ_X = Φ(ψ_X)`. Suppose `ω_0` is invariant under conjugation by `e^{iθ G^1_x}` for every site `x` and every `θ ∈ R`. Then `ω_0(Ψ_X^* α^n(Ψ_Y)) = 0` for all `X ≠ Y` and all `n ∈ Z`. The same holds for a coarse state invariant under every coarse gauge transformation `e^{iθ G^{(1),1}_X}`.

*Proof.* Let `x = x_X`. The sets `S` are disjoint, so `x ∉ S_Y`. By (G1), `Φ(e^{iθ G^{(1),1}_X}) = e^{iθ G^1_x}`, so conjugation by `e^{iθ G^1_x}` acts on `Φ(A_1)` as `Φ` of the coarse gauge transformation at `X`. It fixes `Ψ_Y` and multiplies `Ψ_X` by `e^{-iθ}`. The base tick commutes with `e^{iθ G^1_x}` (`LW1_5.md` line 136, U), and so does any gauge-invariant plaquette layer. So `α^n(Ψ_Y)` is fixed as well. Hence `ω_0(Ψ_X^* α^n(Ψ_Y)) = e^{iθ} ω_0(Ψ_X^* α^n(Ψ_Y))` for every `θ`, and it vanishes. The coarse case is the same computation. □

**Consequence.** Suppose, besides Lemma R-GI's hypothesis on `ω_0`, that `ω_1` is invariant under every coarse gauge transformation, and that `ω_0` and `ω_1` are invariant under the coarse cell translations. Then the bound in the precise statement holds only if `ω_0(Ψ_{X,j}^* α^{Lt}(Ψ_{X,k})) = ω_1(ψ_{X,j}^* α_1^t(ψ_{X,k}))` for every coarse site `X`, all flavours `j, k` and every `t ∈ N`.

*Proof.* Each side is a bounded sesquilinear form in `(f, g)`. For finitely supported `f, g` Lemma R-GI reduces it to the same-site sum `Σ_X Σ_{j,k} conj(f_{X,j}) g_{X,k} (…)`. That sum converges absolutely for `f, g ∈ l^2` and is continuous, so the reduction holds for all `f, g`. Let `D_{X,jk}(t)` be the difference of the same-site terms. By translation invariance it depends on `X` only through its residue `r`. Take a unit coarse-cell profile `φ` with momentum support in `|θ| <= κ`. Let `f` be `φ` on residue `r` and flavour `j`, and `g` be `φ` on residue `r` and flavour `k`. Then the difference equals `D_{r,jk}(t)`, so `|D_{r,jk}(t)| <= C(κ^p + tκ^{p+1})` for every `κ ∈ (0, κ_0]`. Letting `κ -> 0` gives `D_{r,jk}(t) = 0`. □

So, if both vacua are locally gauge invariant, ZM1-I1's two-point comparison carries no information about propagation between coarse sites. It then asks for exact equality of on-site return amplitudes. Whether ZM1-I1 should compare gauge-invariant observables instead, as ZM1-G does for the gauge sector, is for the lead or the owner. This report proposes no observable class.

## 5. Checks behind the verdicts

All checks ran in `/tmp/toe-zm1ref/` on the Mac mini, with `memory_pressure` showing 68 percent free before each run. They use floating point. Each run took under 15 s with peak memory under 0.5 GB. The code is independent of pass 1's scripts, which this session did not read. The checks guide; none proves.

1. `cov_check.py`. It builds `R_e` and `R_o` on even tori of sides `2L N_c` and `2N_c`, with `N_c = 3`, from `LW1.md` §1. It finds the cell sign lifts about `c_0` by solving `d(gx)d(gy) = R_T(gx, gy)/R_T(x, y)` along edges. It builds `ψ` by exact periodization (DFT of Lemma Z2.3's `ψ̂`), then `J_L`, then `Y^tr` from Lemma Z2.1's `G_j`, `C_j` at `ε = 0.7`, and `W = exp(iβ Y^tr)`. For `L = 2, 3, 4` and all 24 rotations: the signs are cell-periodic; `F_Q` of R1 commutes with the fine `R_e`, `R_o` exactly; `max|J_L ρ_c - F_Q J_L| <= 8.3·10^{-16}`; `max|J̃_L ρ_c - F_Q J̃_L| <= 9.0·10^{-16}`. The twist is not trivial: `max|Y| = 0.108`, and `max|W - 1|` reaches 0.083. `ψ` is symmetric to `2.6·10^{-15}`, and `J_L` is isometric to `3.1·10^{-15}`.
2. `cov_controls.py` (`L = 2`). Flipping the sign of one residue breaks the fine symmetry, with deviation 1.15. Using the centre `(2L - 1/2)1` of a group of eight blocks breaks the intertwining, with deviation 0.37.
3. `z2_bounds.py`. Over `ε ∈ {0.05, 0.3, 0.7, 1.2, 1.5}` and 200 random `K` each with `|K| <= 1`: `max ‖r_3‖/|K|^3 = 0.0646`, against the proved 1/2; `max ‖{G_j, C_k}‖ = 2.8·10^{-16}`; `max ‖i[Y, h_1] - h_2‖ = 2.0·10^{-16}`. For `L ∈ {2, …, 8, 16}`: `min g/L^3 >= 0.25`, against the proved 0.078; `max Σ_{m≠0}|α_m|^2/θ^4 = 0.0054`, against 1.75. For `L ∈ {2, 3, 5}` and 30 random `θ` per pair `(ε, L)`: `max ‖A - h(θ)‖/|θ|^3 = 0.035`, against 1.5; the static mismatch is at most 0.0020 times `(3.5/v)|θ|^2`. Arithmetic: with exact constants the four terms of `E_1` are 0.5147, 0.2972, 0.125 and 0.0481, sum 0.985; with the stated roundings the first two are 0.5159 and 0.2978. Also `2/(2 - 3π/16) = 1.4175`, and times `3π/4` this is 3.3399.
4. `o_check.py` (`L = 2, 3`; `N_c = 4`, so that `i^{x_1+x_2+x_3}` is periodic). `W_c Y W_c^*` is purely imaginary, with largest real part 0. `W_f J̃_L W_c^*` is real, with largest imaginary part 0. A coarse cell translation is intertwined with the sign `(-1)^{L+1}`, with deviation at most `3.3·10^{-16}`. The opposite sign gives deviations 0.68 and 0.72.

## 6. Required edits

The lead applies these to `ZM1.md`. Each names the table item it settles. None changes the content of a theorem.

- **E1** (#3). Line 9: delete the Z2-cov clause. Replace "Attack 1 covers finite sums; an infinite-tail extension is unproved" by "Theorem Z3 also holds for norm limits of linear fields (Theorem Z3′)". Keep the other clauses.
- **E2** (#2). Line 7: delete "subject to its indexing qualification" and "except the covariance qualification".
- **E3** (#21, #24, #27). Replace GAP Z0-index (line 82) by R2's statement of the words. Delete "covariance subject to GAP Z0-index" from Z0's title (line 84). In proof (3) write `4L` and add R2's sentence on translations by `2L`. Delete the last sentence of line 95.
- **E4** (#32, #38). Add R3 after Theorem Z1, and add "(Majorana modes for `L5-O`)" to Corollary Z1.1.
- **E5** (#40). Line 129: "So every quasi-free zoom of factor `L` with fewer than `L^3` modes per coarse cell has a nonzero error."
- **E6** (#54, #80). Lines 178 and 255: the cubic-term wording of §3.1.
- **E7** (#55, #61, #65, #82). Delete GAP Z2-cov (line 182). Delete "covariance conditional" from the titles of Lemma Z2.3 (line 184) and Theorem Z2 (line 220), and "conditional on covariance" from that of Corollary Z2.2 (line 259). In Theorem Z2(1) (line 221) delete "and, subject to GAP Z2-cov," and "Subject to that gap,". In proof (1) (line 233) delete "The covariance assertion is conditional on GAP Z2-cov." Insert R1 (1)–(3) into the covariance part of the proof of Lemma Z2.3 (line 202).
- **E8** (#70). Line 241: "`(0.516 + 0.298 + 0.125 + 0.049)|θ|^3 = 0.988|θ|^3 <= 0.99|θ|^3`".
- **E9** (#75). Line 245: "`<= (2/(2 - 3π/16)) δ/g <= 1.4175 δ/g <= (3.340/v)|θ|^2`".
- **E10** (#72, #80). Lines 231 and 245: replace the `1 - P` clause by R5(a), which gives it the same bound as `P`.
- **E11** (#79). After line 249: add R5(b), and delete "Wick's rule gives higher functions but requires observable-dependent error bounds."
- **E12** (#83). Line 263: "in coarse units the mass is `Lμ` (while `Lμ < π`)".
- **E13** (#84). Line 269: "with `T` a Hermitian `5 x 5` matrix".
- **E14** (#93). Line 303: the GA2_Y2 wording of §3.1.
- **E15** (#96). Line 311: replace ZM1-I1 by R6's precise statement. Add Lemma R-GI and its consequence, with one sentence: "The choice of observable class for ZM1-I1 is for the lead or the owner."
- **E16** (#97, #98). Lines 313 and 315: cite Theorem Z3′ (R4) for norm limits. Delete "The exponentially supported kernel in Z2 needs an additional limiting argument."
- **E17** (#99). Line 317: the truncation wording of §3.1 for Attack 2.
- **E18** (#18). Line 65: "pass 1 read no more of its definition, so the analogy is pass 1's". Credit the centred contour-average construction to Ethan Sussman and Levent Alpoge, as the YM file's line 21 does.
- **E19** (#101). Line 321 and the heading of §5.4: add "Attack 3 concerns the subspace notion of the cited work. Definition Z needs a unital map, so Attack 3 is not an attack on ZM1-I1 as stated. ZM1-I1 has two failed attacks on file."
- **E20** (optional; #13, #14, #86). In Theorem Z4, `n_0 = 5` holds for `L5-O` as well (§3.6). In §1.2 give the frozen MT1 lines (40, 85–89, 126) beside the pass-2 ones. The file has no §2 heading, so numbering jumps from §1 to §3.

## 7. Open statements to carry by name

- **ZM1-I1**, in R6's precise form. Two attacks are on file against it as stated. Attack 1 (minimal coupling) fails at "`Ψ_u` is a fermion field", by Theorems Z3 and Z3′. Attack 2 (c-number dressing) fails at "in some state the link operators act as c-numbers", by `GA2_Y2.md` Theorem 3.4. Attack 3 (Gauss-projection tiles) fails at its named step, but it attacks the subspace variant. Lemma R-GI bears on the formulation: if both vacua are locally gauge invariant, the comparison reduces to exact on-site agreement. The observable class is for the lead or the owner. No counterexample is known.
- **Z2-spatial (residual).** ZM1(a)1 for local block observables at separation `r`, which are not band-limited; times beyond `1/κ`; a compatible tower of the maps `Φ_{2^k}`.
- **ZM1-i, ZM1-ii, ZM1-G, Y1, VC1, GA1-P, GA1-P-5**, and the rule that selects the rung `n` or the exact fixed point, as `ZM1.md` line 11 lists them.
- Not decided, and not asked by Q-F (line 127): exact block maps of the free tick that are not quasi-free.

## 8. Freeze recommendation

Freeze ZM1 after E1–E19; E20 is optional. No edit changes a theorem. Theorems Z0, Z1, Z2, Z3 and Z4, Lemmas Z1a and Z2.0–Z2.4, and Corollaries Z1.1, Z2.1, Z2.2 and Z3.1 are correct as stated once the edits are in. The closures R1–R6 are unrefereed, and the lead may gate them before downstream use. R1 reverses the distiller's GAP Z2-cov. Its proof is four lines and can be checked by hand: the fine rotation about the block centre is `T_{(L-1)(1 - Q1)} ρ(Q)`, an even translation times the cell lift. ZM1 stays open as a part. Under the lane brief's three-attack rule, ZM1-I1 needs one more attack on it as stated; the lead may assign it.

---

## FINISH

**Proved (this file; referee closures, unrefereed).**
- **R1.** `J_L` and `J̃_L` intertwine the coarse lift of every rotation about a coarse cell centre with the fine lift `T_{(I-Q)t} ρ(Q)` about the block centre. So `Φ_L` satisfies (Z-b), and GAP Z2-cov is not real.
- **R2.** Theorem Z0 holds on its own coarse lattice: blocks are coarse sites, `2 x 2 x 2` blocks are coarse cells, and a coarse cell translation is the fine translation by `4L`.
- **R3.** Theorem Z1 and Corollary Z1.1 hold for the real Majorana block maps of `L5-O`, in Majorana units: `d = L^3 r_M` with `r_M <= 80`, and PS-5 content forces `L = 2`.
- **R4.** Theorem Z3′: a coarse fermion field in the norm closure of linear fields has no coefficient outside `S_u`. This closes the infinite tails of Attack 1, and Corollary Z3.1 extends to that class.
- **R5.** The `1 - P` two-point functions obey the `P` bound, so Corollary Z2.1 holds for every two-point function. Normally ordered `2n`-point functions differ by at most `n^{(n+2)/2} β`.
- **R6.** A precise statement of ZM1-I1. Lemma R-GI: in locally gauge-invariant states, charged two-point functions between distinct coarse sites vanish. With both vacua locally gauge invariant and translation invariant, ZM1-I1's bound forces exact on-site agreement.
- **Verdicts.** 103 items: 89 CORRECT, 10 ERROR, 4 INCOMPLETE. With the edits, every theorem, lemma and corollary of `ZM1.md` is correct as stated.

**Counterexamples.**
- To GAP Z2-cov's claim that the covariance proof uses the wrong rotation centre: R1, with the [check] and its controls.
- To Attack 2's setup "`w δ_{x_u} = J̃_L e_u`" for a finite circuit: at `L = 2`, `J̃_L e_u` has infinite support (§3.8).
- None to any theorem, lemma or corollary of `ZM1.md`.

**Open by name.** ZM1-I1, in R6's precise form: Attacks 1 and 2 fail on it, Attack 3 fails on its subspace variant, and the observable class is for the lead or the owner. Z2-spatial (residual). ZM1-i. ZM1-ii. ZM1-G. Y1. VC1. GA1-P. GA1-P-5. The rule that selects the rung `n` or the exact fixed point.

**What changes downstream.**
- **ZM1.** After E1–E19, Theorem Z2 gives a Definition-Z block map without qualification, for `L_cube`, `L5-U` and (Corollary Z2.2) `L5-O`. The free-tick comparison has `p = 2` for every two-point function and for every fixed number of band-limited fields.
- **LZ1 and MT1-S.** They may cite Theorem Z2 and Corollary Z2.1 without the covariance qualifier.
- **GA2.** Corollary Z3.1 now covers norm limits of linear transported averages on PS-6r links. The linear operator-level block average is excluded in that whole class.
- **ZM1-I1.** If VC1's vacuum is locally gauge invariant, the lead or the owner must choose an observable class before ZM1-I1 is worked. A gauge-invariant class would sit beside ZM1-G.
- **The working set.** No entry changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. Nothing is adopted.
