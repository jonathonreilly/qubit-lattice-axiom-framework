lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# LW1-5-X referee report (pass 3)

Written 2026-11-06 (UTC; the local clock read 2026-11-05) by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort). The lane ran under the pass-1 lane brief of the TOE assembly. Its task is pass 3, the referee of `LW1_5X.md`, under the method of open PR #10138: Claude drafts, Codex distils, a fresh Claude session referees, then the part is frozen. This session wrote neither pass 1 (`LW1_5X_DRAFT.md`) nor pass 2 (`LW1_5X.md`). This is one check: one line-by-line read of the whole distilled part. The only other review read is `LW1_REFEREE.md`, for its format, as the brief asks; no review was reviewed. No review of this review was commissioned. This report adopts no reading, law or status. It edits no other file.

**Text refereed.** `LW1_5X.md` at commit `a5ddff4b0` on branch `claude/toe-assembly`, the commit that adds it and the checkout's HEAD. SHA-256 `d6573e5ece1b6d7dba1f4d6002bef6eac96b390316b8c86b157b35d8639ebdd7`. Line numbers below refer to that file.

**Sources read, with commits.** All files are in `.claude/science/physics-loops/toe-assembly-20261104/` unless a path is given. No other branch was read.

| File | Last commit touching it | SHA-256 (prefix) | Lines read |
|---|---|---|---|
| `LW1_5X.md` | `a5ddff4b0` | `d6573e5ece1b6d7d` | 1-128 (all) |
| `LW1_5X_DRAFT.md` | `bf403a16a` | `e6c4b1b880e9ab61` | 1-280 (all) |
| `LW1_5.md` (frozen) | `4b65c608f` | `cbb2db58bfb6412e` | 1-140; 326 and 340 (grep hits) |
| `LW1_5U_DRAFT.md` | `c721a3507` | `b510f6f67eb47ced` | 160-195 (Lemma X1, Proposition X2), read because the draft quotes them |
| `LW1_REFEREE.md` | `5a2a0affe` | `f252954767393db5` | 1-80 (format); 80-140 in passing |
| `Y2W_DRAFT.md` | `92e03055c` | `f9d8db9c15b4b101` | 1-30 (head format) |
| `TOE_ASSEMBLY.md` | `7d2b20d29` | `8027d9d44eb5fcaf` | section headings; 214 (§3.5); 660 (§10); 552 in passing (a grep hit) |
| `AGENTS.md`, `CLAUDE.md` (repo root) | `a5ddff4b0` checkout | — | entry points |

The draft and `LW1_5.md` are unchanged between `bf403a16a` (the distiller's HEAD) and `a5ddff4b0` (`git diff --stat` shows only `CH1_5O.md`, `CH1_5U.md` and `LW1_5X.md` in this folder). `docs/MINIMAL_AXIOMS_2026-06-29.md` was not read and is unchanged.

**Working set used, by name.** PS-5, PS-6 and PS-6r, only through the two laws `L5-U[m]` and `L5-O[S_+]` as `LW1_5.md` §2 states them. Results of frozen `LW1_5.md` used: the §1 definitions (frame, register change, compatibility, `𝓔(H)`); C (each frame acts on its site as `Ad V`, `V` homogeneous); M and M.1; Q and G; U; the "Exceptional angles" paragraph (line 117). The owner decision LW1-5-RQ (`TOE_ASSEMBLY.md` line 214: "The owner chose: **keep both live.**") is noted and not used. PS-1, PS-2, PS-3, PS-4, PS-7 and PS-11 are not used.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws are read plainly, as `LW1_5.md` §2 states them. No hostile reading is made.

**Inputs from outside the working set.** Standard finite-dimensional mathematics, rebuilt where used: Lagrange interpolation; norms of orthogonal direct sums; commutants of `End(R)⊗1`; the centre and ideals of a finite-dimensional C*-algebra; the even Clifford algebra on `2n` Majoranas is `End(F_+)⊕End(F_−)`. Cited from frozen `LW1_5.md`, not rebuilt: linear independence of the 100 `U^{ab}` on every nontrivial register (§3, after M.1).

**Method.** Every proof was re-derived by hand. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix or counterexample); INCOMPLETE (a named missing step, with what is missing). A "referee closure" is a short complete argument for a missing step. A `[check]` is a scratch computation in `/tmp/toe-lw15xref/` (scripts `cube.py`, `check_blocks.py`, `check_link.py`, `check_onecolour.py`; each ran under 2 s and under 0.5 GB, started with 63 percent of memory free). A check guides or refutes; it never proves.

**Counts.** 103 items: 100 CORRECT (two of them open statements), 1 ERROR, 2 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a theorem. All three GAPs the distiller marked are real; §3 gives the repaired statements and one referee closure.

---

## 1. Verdict table

| # | Item (LW1_5X line) | Verdict | Note |
|---|---|---|---|
| 1 | Title (1) | CORRECT | |
| 2 | §0 status: pass 2; laws are `LW1_5.md`'s conditional constructions (5) | CORRECT | |
| 3 | §0 Proved: `U(5)` in Theorem 5.1's small-angle range (7) | CORRECT | Theorem 5.1. |
| 4 | §0 Proved: `m=1,9`, every window point, by the even gate (7) | CORRECT | Corollary 5.2. |
| 5 | §0 Proved: `2≤m≤8` where the relevant sector gate determines its generator (7) | CORRECT | In the window, where `a_e<π/2<π√(3/5)`. |
| 6 | §0 Proved: scalar site commutant of the even gate in the window, every `m` (7) | CORRECT | Theorems 2.2 and 4.3. |
| 7 | §0 Proved: conditional `L5-O[S_+]` site commutant (7) | CORRECT | Theorem 6.1. |
| 8 | §0 GAP paragraph (9) | CORRECT | All three gaps are real (§3). |
| 9 | §0 Open by name (11) | INCOMPLETE | The amplitude hypothesis of Theorem 6.1 is open and has no name. |
| 10 | §0 Provenance (13) | CORRECT | Hashes and commits reproduced; label the second effort record (note). |
| 11 | Def. 1: frames and compatibility (17) | CORRECT | Matches `LW1_5.md` §1. |
| 12 | Def. 2: cube, registers, generator (18) | CORRECT | |
| 13 | Def. 3: `T_{u→v}` and `h_ℓ=T_{u→v}+T_{v→u}` (19-21) | CORRECT | `T_{v→u}=T_{u→v}^*` checked. |
| 14 | Def. 3: hop rule; blocking and open; `N_x`, `Π_k`, `Γ(u)` (23) | CORRECT | |
| 15 | Def. 4: exceptional angle; "precisely outside that set" (24) | ERROR | False at `a=0`; add `a≠0`. |
| 16 | Def. 4: extra registers in commutant statements (24) | CORRECT | |
| 17 | Def. 5: window and the two angles (25) | CORRECT | |
| 18 | Def. 6: "scalar on the cube registers"; "holds at a parameter point" (26) | CORRECT | |
| 19 | No new reading; four-test results; both laws live (28) | CORRECT | Matches `LW1_5.md` §2 and `TOE_ASSEMBLY.md` line 214. |
| 20 | Theorem 2.1, statement (32) | CORRECT | |
| 21 | Theorem 2.1, proof (34) | CORRECT | |
| 22 | Theorem 2.2, statement (36) | CORRECT | |
| 23 | Proof: the commutant is a unital *-algebra; its charge parts lie in it (38) | CORRECT | Name the charge `𝒢^1_x` (note). |
| 24 | First block: the configuration is consistent (40) | CORRECT | No triangles; five distinct links. |
| 25 | First block: `B_ξ`; orthogonal register labels; `‖B_ξ‖²=k‖ξ‖²` (40-43) | CORRECT | |
| 26 | First block: `HA_ξ=sB_ξ`, `HB_ξ=skA_ξ` (41-43) | CORRECT | [check] |
| 27 | First block: the `B` coefficient of `WA_ξ` (44) | CORRECT | |
| 28 | Second block: configuration; seven distinct links (46) | CORRECT | Wording "occupied endpoint" (note). |
| 29 | Second block: `HA_ξ`, `HB_ξ`, `HC_ξ` (47-49) | CORRECT | [check] |
| 30 | Second block: `H³=(k+1)H/3`; the `B` coefficient (50) | CORRECT | [check] |
| 31 | The two sines do not both vanish (50) | CORRECT | |
| 32 | Charge zero: `Dc_{x,j}=c_{x,j}D` on every `Λ^k` (52) | CORRECT | |
| 33 | Adjoint step; `D` is scalar (52) | CORRECT | |
| 34 | The charge parts `D_q`, `q≠0`, vanish (52) | CORRECT | |
| 35 | Corollary 2.3, statement (54) | CORRECT | |
| 36 | Corollary 2.3, proof (56) | CORRECT | Rebuilds `LW1_5U_DRAFT.md` Lemma X1. |
| 37 | Theorem 3.1, statement (60) | CORRECT | |
| 38 | Proof: one link hop has norm at most one (62) | CORRECT | |
| 39 | Proof: the direction sums give `‖H_1‖≤√3` (62) | INCOMPLETE | The orthogonal-sector step is missing. |
| 40 | Proof: injectivity on the spectrum; interpolation (64) | CORRECT | |
| 41 | Proof: matter matrix elements give `r^v_jr^{u†}_k` and adjoints (64) | CORRECT | |
| 42 | Proof: matrix units; commutant per link; all twelve links (64) | CORRECT | |
| 43 | Pass-1 one-colour report (66) | CORRECT | Referee [check] reproduces 1.3481. |
| 44 | Theorem 3.2, statement (68) | CORRECT | |
| 45 | Proof: the Gauss action gives every `Γ(u)` ("if") (70) | CORRECT | |
| 46 | Proof: Corollary 2.3; vacuum normalization; `V'=1` on `Λ^0⊕Λ^1` (70) | CORRECT | |
| 47 | Proof: Theorem 2.1 for the composed action (70) | CORRECT | |
| 48 | Proof: one-particle sector; Theorem 3.1 removes `L'` (70) | CORRECT | Invariance of the sector is implicit (note). |
| 49 | Proof: Theorem 2.2 and the normalization give `V'=1` (70) | CORRECT | |
| 50 | Proof: `a_e<π/2<π/√3` (70) | CORRECT | |
| 51 | Remark: odd gate; single-link example (72) | CORRECT | |
| 52 | Theorem 4.1, statement (76) | CORRECT | |
| 53 | Proof: `Θ(T_{u→v})=T_{v→u}` (78) | CORRECT | [check] |
| 54 | Proof: `m↦10−m`, `N_x↦5−N_x` (78) | CORRECT | |
| 55 | Proof: algebras, link unitaries and compatibility are carried over (78) | CORRECT | |
| 56 | Proof: `Γ(u)↦Γ(ū)` up to a scalar (78) | CORRECT | |
| 57 | Theorem 4.2: `ν_m²` and its nine values (80-84) | CORRECT | [check] |
| 58 | Theorem 4.2, statement (84) | CORRECT | |
| 59 | Proof: `T²=0`; `T^*T`, `TT^*` on orthogonal location spaces (86) | CORRECT | |
| 60 | Proof: `T^*T=p_vZ^*Z`, `ZZ^*=p_u`, block bound (86) | CORRECT | [check]: the single-link bound is attained. |
| 61 | Proof: the range of `p` (86) | CORRECT | |
| 62 | Proof: sum over the three directions (86) | CORRECT | Complete once item 39 is fixed; reword "disjoint directional layers". |
| 63 | Proof: interpolation; the products `n^v_j(1−n^u_k)`, `n^u_k(1−n^v_j)` (88) | CORRECT | |
| 64 | Proof: the products separate the `m`-subsets (88) | CORRECT | [check] |
| 65 | Proof: trades connect all `m`-subsets; the commutant is scalar (88) | CORRECT | [check] |
| 66 | Theorem 4.3, statement (90) | CORRECT | |
| 67 | Proof: reduction to `m≤5` by Theorem 4.1 (92) | CORRECT | |
| 68 | Proof: `𝒟_0` is a unital *-algebra invariant under `U(5)` (92) | CORRECT | |
| 69 | Proof: minimal central projections are fixed (92) | CORRECT | |
| 70 | Proof: the commutant of `Γ(U(5))` is `span{Π_0,…,Π_5}` (92) | CORRECT | |
| 71 | Proof: star-block configuration (94) | CORRECT | Uses `m≤5`, as assumed. |
| 72 | Proof: one departure, no second, return to the start (94) | CORRECT | Wording "sole hole" (note). |
| 73 | Proof: `n`, `H²A=(n/3)A`, `sin(a√(n/3))≠0` (94) | CORRECT | [check] |
| 74 | Proof: `f(k−1)=f(k)` for all `k` (94) | CORRECT | |
| 75 | Proof: the centre of `𝒟_0` is scalar (96) | CORRECT | |
| 76 | Proof: the vacuum-line homomorphism is injective (96) | CORRECT | Central support stated, not rebuilt (note). |
| 77 | Proof: the nonzero charge parts vanish (96) | CORRECT | |
| 78 | Theorem 5.1: the values of `ν'_m²` (100) | CORRECT | |
| 79 | Theorem 5.1: small-angle clause (100) | CORRECT | |
| 80 | Theorem 5.1: nonexceptional clause; one-hole sector for `m≥6` (100) | CORRECT | |
| 81 | Theorem 5.1, proof (102) | CORRECT | |
| 82 | Corollary 5.2: `m=1,9` (104) | CORRECT | |
| 83 | Corollary 5.2: sufficient conditions for `2≤m≤8` (104) | CORRECT | |
| 84 | Corollary 5.2: the four thresholds (104) | CORRECT | |
| 85 | Corollary 5.2: the two-gate residual is finite (104) | CORRECT | |
| 86 | Corollary 5.2, proof (106) | CORRECT | |
| 87 | GAP in the draft's finite-set wording (108) | CORRECT | Gap real (§3.1). |
| 88 | LW1-5-X-B_m, the question (110) | CORRECT (open) | |
| 89 | An affirmative LW1-5-X-B_m suffices (110) | CORRECT | |
| 90 | A non-`U(5)` frame needs a nonscalar register commutant (110) | CORRECT | |
| 91 | The draft's three searches (112) | CORRECT | Faithful to the draft; no no-go claimed. |
| 92 | Theorem 6.1, statement (116) | CORRECT | |
| 93 | Proof: `U(5)` in the `SO(10)` Gauss action; charges; centre (118) | CORRECT | |
| 94 | Proof: connectivity; vacuum line; charge parts (118) | CORRECT | |
| 95 | The hypothesis holds for small `a≠0` (120) | CORRECT | Referee rebuild in §4.F. |
| 96 | The hypothesis is unchecked at general window angles (120) | CORRECT | Needs a name (item 9). |
| 97 | LW1-5-X-O, the question (122) | CORRECT (open) | |
| 98 | U-law tools unavailable; proposed route; no counterexample (122) | CORRECT | |
| 99 | The parity-slice search (124) | CORRECT | |
| 100 | The limits of the Lie-algebra search (124) | CORRECT | |
| 101 | GAP: the module decomposition (124) | CORRECT | Gap real (§3.2). |
| 102 | GAP: "parity the only matter-only conserved quantity" (124) | CORRECT | Gap real at exceptional angles; closure off them (§3.3). |
| 103 | §7 scope and dependencies (128) | CORRECT | Add `LW1_5.md` C to the inputs (note). |

---

## 2. Details of the non-CORRECT items

### 2.1 ERROR

**Item 15 (line 24, definition 4).** LW1_5X: "An exceptional angle of a finite Hermitian `K` is an `a` for which `a(λ−λ')` is a nonzero multiple of `2π` for distinct eigenvalues. Thus `e^{iaK}` determines `K` by polynomial interpolation precisely outside that set."

Counterexample. Take `K=diag(0,1)` and `a=0`. Then `a(λ−λ')=0` is not a nonzero multiple of `2π`, so `0` lies outside the set. But `e^{i0K}=1`, and no polynomial in `1` equals `K`.

Fix: "For `a≠0`, `e^{iaK}` determines `K` by polynomial interpolation precisely when `a` lies outside that set."

Proof of the fixed line. Let `a≠0`. For distinct eigenvalues, `a(λ−λ')≠0`. So `e^{iaλ}=e^{iaλ'}` exactly when `a(λ−λ')∈2πℤ∖{0}`. Outside the set, `t↦e^{iat}` is injective on `spec K`, and Lagrange interpolation gives a polynomial `f` with `f(e^{iaK})=K`. Inside it, two distinct eigenvalues of `K` give one eigenvalue of `e^{iaK}`. Every polynomial in `e^{iaK}` is then scalar on the sum of their eigenspaces, while `K` is not. ∎

Every use in LW1_5X.md has `a≠0`: Theorems 3.1, 4.2 and 5.1 assume `0<|a|`, and Corollary 5.2 uses `a_e,a_o>0`. No result changes. The same caveat applies to frozen `LW1_5.md`. Its M.1 sentence "The same holds for a compatible gate `e^{iaH}` when `a∉𝓔(H)`" (line 111) covers `a=0`, since `0∉𝓔(H)` by the definition at line 33. At `a=0` the gate is `1` and every frame is compatible. No result there uses `a=0`, so this does not reopen `LW1_5.md`. The dated amendment can record "`a≠0`" once for both files.

### 2.2 INCOMPLETE

**Item 9 (line 11, Open by name).** LW1_5X: "The amplitude hypothesis in Theorem 6.1 is unchecked at general window angles." This is an open statement. The block lists it without a name, and line 120 repeats it without one.

Missing: a name and an exact statement. Proposed wording, a label for an existing hypothesis: "**LW1-5-X-OA (OPEN).** For an `L5-O[S_+]` cube gate `W` at a window angle (`a=−a_e` on the even cube, `a=a_o` on the odd cube), the pairs `{k,k'}`, `k≠k'`, with `Π_{k'}WΠ_k≠0` connect `{0,…,5}`." Theorem 6.1 assumes it. Any proof of LW1-5-X-O along the U-law lines would need it at the finitely many points of LW1-5-X-O. It holds for all small nonzero `|a|` (item 95, §4.F). Four-test check of the label: (1) it states or fixes no part's target; (2) it is a closed statement; (3) it settles no downstream physics question; (4) it adds no structure or constant. It passes all four.

**Item 39 (line 62, Theorem 3.1).** LW1_5X: "The four links in one direction are disjoint. On the one-particle sector a link hop exchanges the basis state with particle at one end and rishon at the other with the reversed state, up to sign; it kills the remaining states. Its norm is at most one. Thus the triangle inequality gives `||H_1||≤3/√3`."

Missing step. The triangle inequality over the twelve hops gives only `12/√3`. The bound `3/√3` needs each direction's sum to have norm at most one. The text names the premise (disjointness) but not the step.

Referee closure. Fix a direction. Its four links partition the eight sites. So `ℋ_1=⊕_ℓℋ_1^ℓ` over these four links, where `ℋ_1^ℓ` holds the one-particle states whose particle sits at an end of `ℓ`. The hop of `ℓ` maps `ℋ_1^ℓ` into itself and kills `ℋ_1^{ℓ'}` for `ℓ'≠ℓ`, since it needs a particle at an end of `ℓ`. So the direction's sum is the orthogonal direct sum of the four restricted hops. Its norm is their maximum, at most one. The triangle inequality over the three directions then gives `‖H_1‖≤3^{−1/2}·3=√3`. ∎

Fix: insert the closure before "Thus", and say "the triangle inequality over the three directions". Theorem 4.2's sentence "Sum the three disjoint directional layers as in Theorem 3.1" (line 86) is then complete. Reword it: "Sum over the three directions, each a set of four disjoint links, as in Theorem 3.1." The layers themselves are not disjoint from one another.

### 2.3 Notes on CORRECT items that bear on the freeze

- **Item 10 (provenance).** Line 13 records the pass-2 effort twice: "reasoning effort high" (set by the lead from the run log) and "reasoning effort not visible" (the distiller's own line). They come from different vantage points, so neither is false. Label the second "the distiller's own record (historical)", as `LW1_5.md` §0 does for its prior provenance line. Reproduced here: the draft SHA-256 `e6c4b1b8…a720`, the frozen `LW1_5.md` SHA-256 `cbb2db58…5413`, and the HEAD `bf403a16a2bbb3bc0315a71f6cf1d791445cbb7f`. The draft's stated revision `92e03055c` is an ancestor of `bf403a16a`, and the draft's date (2026-11-06) is later than the distiller's (2026-11-05). So line 13's "an earlier source revision and a later date" is right.
- **Item 23.** "The local Gauss charge" should be named: `𝒢^1_x=N_x+Σ_{ℓ∋x}p_{ℓ,x}` (`T=1` in `LW1_5.md` U). Its link part acts on the six links at `x`; three lie outside the cube, where `W` acts trivially.
- **Item 24.** The text does not fix the seven links not incident on `x` or `y`. Any fixed state works, because no particle reaches them. One clause suffices.
- **Item 28.** "block every other link incident on `x,y,z` at its occupied endpoint" should read "at its endpoint in `{x,y,z}`". Each such link has exactly one endpoint there, since `x` and `z` are at distance two. In `A_ξ` the endpoint `z` is not occupied.
- **Item 48.** The step needs one clause: `ℋ_1⊗(\text{extra registers})` is invariant under `W` and under `V'⊗L'` (`V'` keeps `N_x`; `L'` fixes matter). Then `1⊗L'` commutes with `e^{iaH_1}`.
- **Item 72.** "fills the sole hole in the departure-end rishons": when `k≤m`, the `x`-end lacks `6−k` colours. The hole that matters is the one colour of `F` it lacks, `k_0`. Reword: "fills the only colour of `F` absent from the departure end".
- **Item 76.** "Its kernel, if nonzero, has a nonzero central support projection" is a standard fact about finite-dimensional C*-algebras. The draft's Step 5 (draft line 198) rebuilds it in three lines: the support projection `e` of `h=Σ_ix_i^*x_i` over a basis of the kernel `J` lies in `J`; operator Cauchy–Schwarz gives `x=xe=ex` for `x∈J`; so `e` is central. Restoring those lines meets the rule "rebuild any lemma you use".
- **Items 80 and 83.** For `m≥6`, Theorem 4.2 also holds on the one-particle sector of `L5-U[m]` itself, with `ν_m`. So either sector may be used. The text's one-hole choice is sufficient as stated.
- **Item 85.** The two-gate residual can be cut further. Theorem 5.1 at `a=a_o` also gives the bound when `a_o<π/(√3ν'_m)`, or when `a_o<π√(3/5)` and `a_o` is nonexceptional for the relevant sector. This is optional; the stated finite set is correct.
- **Item 103.** Theorem 2.1 and Corollary 2.3 also use `LW1_5.md` C: each frame acts on its site as `Ad V` with `V` homogeneous. Add C to the list of inputs.

---

## 3. The distiller's GAPs

### 3.1 GAP 1: the finite-set wording (lines 9 and 108). Real.

LW1_5X line 9: "The draft's assertion that the two-gate residual finite set also describes all exceptional *even-gate* parameter points is too broad: a fixed exceptional even angle leaves a continuum of parameter pairs. The finite-set statement needs compatibility with both gates." The draft, line 210: "For `2 ≤ m ≤ 8` the remaining points lie in Proposition X2's finite set, since an exceptional angle of `H_C|_{ℋ_1}` is an exceptional angle of `H_C`." The same claim appears at draft lines 31 ("The remaining points lie in Proposition X2's finite set") and 270 ("The open points lie inside Proposition X2's finite set").

The gap is real. The draft's corollary concerns the even gate alone. The points it leaves are those where `a_e` is an exceptional angle of the relevant sector. One such value `a*∈(0,π/2)` gives the whole segment `{(ε,μ): ε−μ/2=a*, 0≤μ<π−2a*}` of the window, a continuum. Proposition X2's finite set also needs `a_o` exceptional. The draft's reason supplies only the even half. For a frame compatible with both gates the draft's sentence is true, but its stated reason is incomplete.

**Repaired statement (referee closure).** Let `C` and `C'` be the even and odd cubes at `x`, and `2≤m≤8`. Let `𝓔^♯_m` be the exceptional set of `H_C` on the one-particle sector (`m≤5`) or on the one-hole sector (`m≥6`).
- (i) *Even gate alone.* The bound holds at every window point except possibly those with `a_e∈𝓔^♯_m∩[π/(√3ν'_m),π/2)`. That set of values is finite, so the exceptions lie on finitely many segments `ε−μ/2=a*`.
- (ii) *Both gates.* For a frame compatible with both gates, the exceptions lie in the finite set of window points with `a_e∈𝓔^♯_m∩[π/(√3ν'_m),π/2)` and `a_o∈𝓔(H_{C'})`.

*Proof.* (i) is Theorem 5.1 at `a=−a_e`, since `a_e<π/2<π√(3/5)`. An exceptional set meets a bounded interval in finitely many points, because `H_C` has finitely many eigenvalue differences `d≠0` and `|ad|≤|d|π/2` allows finitely many multiples of `2π`. (ii) If `a_o∉𝓔(H_{C'})`, `LW1_5.md` M.1 gives the bound through the odd gate. The values of `a_o` in `(0,π)` that remain are finitely many, and `(a_e,a_o)` determines `(ε,μ)=((a_e+a_o)/2,a_o−a_e)`. ∎

Lines 104 and 108 of LW1_5X.md already state (ii) and the reason for the gap. Statement (i), the segment description, is implicit there; Corollary 5.2 can add it in one sentence. Since the spectrum of `H_C` on a sector lies in `spec H_C`, `𝓔^♯_m⊂𝓔(H_C)`; so the set in (ii) lies inside Proposition X2's set, as the draft intended.

### 3.2 GAP 2: the module decomposition (lines 9 and 124). Real.

LW1_5X line 124: "**GAP:** the stated decomposition `45⊕45⊕210⊕210⊕1` does not by itself yield finitely many invariant subspaces, because equivalent copies can mix; no finite classification of candidate Lie algebras is proved." The draft, line 244: "Its Lie algebra is an `SO(10)`-submodule of the even part of `𝒜_x` modulo scalars, `45 ⊕ 45 ⊕ 210 ⊕ 210 ⊕ 1` (the even Clifford degrees `2, 8, 4, 6, 10`). So only finitely many candidate algebras exist."

The decomposition itself is right. The anti-Hermitian even site elements modulo `iℝ1` have Clifford degrees 2, 4, 6, 8, 10, of dimensions 45, 210, 210, 45, 1 (total 511, the dimension of `G_full`). As `SO(10)`-modules, degree 8 is isomorphic to degree 2 and degree 6 to degree 4.

The inference fails, and here is an explicit witness. For `(α:β)∈ℝP^1` put `V_{(α:β)}={αX+βXP_x : X∈span_ℝ\{iM^{cd}_x\}}`. Each `V_{(α:β)}` is `SO(10)`-invariant, because the site implementers are even and commute with `P_x`. On `H_±` the element `αX+βXP_x` acts as `(α±β)X|_{H_±}`. The maps `X↦X|_{H_±}` are injective on the span of the `M^{cd}_x`: if `X(1±P_x)/2=0` then `X=∓XP_x`, and the two sides have Clifford degrees 2 and 8. Comparing the two blocks, `V_{(α:β)}=V_{(α':β')}` forces `(α+β)(α'−β')=(α−β)(α'+β')`, that is `αβ'=α'β`. So the `V_{(α:β)}` are pairwise distinct, and the module has a continuum of 45-dimensional invariant subspaces.

This does not show infinitely many candidate algebras. For `β≠0`, `so(10)+V_{(α:β)}` is one and the same algebra, `so(10)_+⊕so(10)_−`: the pairs `(X|_{H_+},Y|_{H_−})` with `X,Y` in the span of the `iM^{cd}_x`. Neither finiteness nor its failure is proved. Repair: delete "So only finitely many candidate algebras exist", as line 124 does. No result uses it.

### 3.3 GAP 3: "parity is the only matter-only conserved quantity" (lines 9 and 124). Real at the angles that matter.

LW1_5X line 124: "The assertion that parity is the *only* conserved matter-only quantity is also unproved and is not needed to show that matter number fails to be conserved." The draft, line 242: "For `L5-O` the only matter-only conserved quantity is the parity `P_xP_𝔐`, and `φ(P_x) = ±P_x` holds for every frame."

The gap is real: the draft gives no proof. LW1-5-X-O lives where both cube angles are exceptional. The closure below holds off the exceptional set and does not reach those points.

**Lemma R1 (referee closure off the exceptional set).** Let `C` be a cube of `L5-O[S_+]` and `Q` an element of the matter algebra of `C`. (i) If `Q⊗1` commutes with `H_C`, then `Q∈span\{1,P_C\}`, where `P_C=∏_{z∈C}P_z`. (ii) The same holds if `Q⊗1` commutes with `e^{iaH_C}` for some `a≠0` with `a∉𝓔(H_C)`.

*Proof.* (i) Links commute with matter, so `h_ℓ=(i/2)Σ_{a,b}γ_{y,a}γ_{x,b}⊗U^{ab}_ℓ`. Hence
\[
[Q\otimes1,H_C]=3^{-1/2}\tfrac i2\sum_\ell\eta_\ell\sum_{a,b}[Q,\gamma_{y,a}\gamma_{x,b}]\otimes U^{ab}_\ell .
\]
The `1200` operators `U^{ab}_ℓ`, each tensored with the identity on the other links, are linearly independent. On one link the 100 `U^{ab}` are independent (`LW1_5.md` §3: "the 100 mixed generators are independent in every nontrivial representation"). Each is traceless: for `d∉\{a,10+b\}`, the bracket `[T_{ij},T_{jk}]=iT_{ik}` (from `T_{ij}=iη_iη_j/2` and the Clifford relations) gives `U^{ab}=2T_{a,10+b}=−2i[T_{ad},T_{d,10+b}]`, a commutator. Now suppose `Σ_ℓX_ℓ=0` with `X_ℓ` in the span of the `U^{ab}_ℓ`. The partial trace over all links but `ℓ_0` gives a nonzero multiple of `X_{ℓ_0}`; so `X_{ℓ_0}=0`. Independence makes every coefficient vanish: `[Q,γ_{y,a}γ_{x,b}]=0` for every cube link `(x,y)` and all `a,b`.

These bilinears generate every quadratic Majorana monomial of the cube. Along a path `x−y−z`, `(γ_{x,b}γ_{y,a})(γ_{y,a}γ_{z,c})=γ_{x,b}γ_{z,c}`, since `γ_{y,a}^2=1`; the cube graph is connected. At one site, `(γ_{x,b}γ_{y,a})(γ_{y,a}γ_{x,c})=γ_{x,b}γ_{x,c}`. The quadratic monomials generate the even part of the Clifford algebra on the cube's 80 Majoranas. On the Fock space `F_+⊕F_−` (`dim F_±=2^{39}`) the even part acts faithfully and keeps `F_±`. Its dimension `2^{79}=2·(2^{39})^2` equals that of `End(F_+)⊕End(F_−)`, so it is that algebra. Its commutant is `span\{1,P_C\}`. So `Q∈span\{1,P_C\}`.

(ii) By item 15's fixed form, `e^{iaH_C}` determines `H_C` by interpolation, so `Q⊗1` commutes with `H_C`. Apply (i). ∎

What R1 gives. Off `𝓔(H_C)`, the draft's sentence holds for the cube's matter algebra. In particular `N_C` does not commute with the gate there. At the points of LW1-5-X-O both angles are exceptional, R1(ii) does not apply, and the sentence stays unproved there. No proof needs it.

The last clause of line 124, "not needed to show that matter number fails to be conserved", is true for the generator: the pairing terms change `N_C` by `±2`. For the gate at an exceptional angle, non-conservation of `N_C` is not shown. Line 122 does not claim it; it says only that the U-law tools are unavailable, which is right.

---

## 4. Checks behind the verdicts, section by section

### 4.A Section 0 and section 1

- **Hashes.** `shasum -a 256` reproduces the two file hashes of line 13 (draft and frozen `LW1_5.md`, read at `bf403a16a` and at `a5ddff4b0`) and the hashes in this report's head [check: string comparison]. `git rev-parse bf403a16a` gives the full HEAD that line 13 records.
- **Definition 3.** Rishons commute with matter, so `(c^†_{y,j}r^y_jr^{x†}_kc_{x,k})^*=c^†_{x,k}r^x_kr^{y†}_jc_{y,j}`. Hence `h_ℓ=T_{x→y}+T_{y→x}` and `T_{y→x}=T_{x→y}^*`. The hop rule follows from the four factors: `c_{u,k}` removes the particle, `r^{u†}_k` needs a hole at the `u`-end, `r^v_j` needs a rishon at the `v`-end, `c^†_{v,j}` places the particle.
- **Definition 5.** `μ<2ε` gives `a_e>0`; `μ≥0` gives `a_e≤ε`; `2ε<π` gives `ε<π/2`; `a_o=ε+μ/2<2ε<π`; `a_o≥ε>0`.
- **Line 28.** `LW1_5.md` §2: "Four-test result for each: tests 1, 2 and 4 pass; test 3 is conditional". `TOE_ASSEMBLY.md` line 214: "The owner chose: **keep both live.**" Both match.

### 4.B Section 2

- **Theorem 2.1.** On `a∈𝒜_x` both sides give `VaV^*`. On outside matter `b` of parity `q`, `Ad(V⊗L)(P_x^q⊗b̂)=VP_x^qV^*⊗b̂=P_x^q⊗b̂=ψ(b)`, since an even `V` commutes with `P_x`. On links both give `Ad L`. Two automorphisms of the finite algebra that agree on generators are equal.
- **Charge parts (item 23).** `𝒢^1_x` commutes with every hop (`LW1_5.md` U). Its link factor commutes with `𝒜_x`. So `e^{itN_x}De^{−itN_x}` commutes with `W`, and `D_q=(2π)^{−1}∫_0^{2π}e^{−iqt}e^{itN_x}De^{−itN_x}dt` lies in the commutant; `D=Σ_{q=−5}^{5}D_q`.
- **First block, `m=1`.** With `λ_0` holding `|y;j'⟩` on `xy`: `r^y_{j'}r^{x†}_{k'}|y;j'⟩=−|x;k'⟩`, and `r^x_{k''}r^{y†}_{j'}(−|x;k'⟩)=δ_{k''k'}|y;j'⟩`. With `y` empty, `c_{y,j}c^†_{y,j'}c_{x,k'}|ξ;0⟩=δ_{jj'}c_{x,k'}|ξ;0⟩`. So `T_{y→x}B_ξ=Σ_{k'}n_{x,k'}A_ξ=kA_ξ`. On the span, `H^2=k/3`, so `e^{iaH}=\cos(aβ)+i(\sin(aβ)/β)H` with `β=√(k/3)`.
- **Second block.** `H^2B_ξ=(s^2k+t^2)B_ξ=((k+1)/3)B_ξ`, and `H^3=ω^2H` on the span with `ω^2=(k+1)/3`. So `e^{iaH}=1+i(\sin aω/ω)H+((\cos aω−1)/ω^2)H^2` there, and the `B` part of `WA_ξ` is `is(\sin aω/ω)B_ξ`. `T_{z→y}T_{y→z}` acts as `n_{y,j'}(1−n_{z,j''})` on the matter and as the identity on the `yz` register state; so `HC_ξ=tB_ξ` and `‖C_ξ‖=‖B_ξ‖`.
- **Sines.** If `a√(k/3)=pπ` and `a√((k+1)/3)=p'π` with `p,p'∈ℤ∖\{0\}`, then `k(k+1)=(kp'/p)^2`. A positive integer that is the square of a rational is the square of an integer. But `k^2<k(k+1)<(k+1)^2`.
- **Charge zero.** `D⊗1` keeps the `A`-, `B`- and `C`-type subspaces, which are mutually orthogonal (different matter on `𝔐` or different registers). An even `D` commutes with `c^†_{y,j'}`. So the `B` parts give `Σ_{k'}c^†_{y,j'}|(Dc_{x,k'}−c_{x,k'}D)ξ;0⟩⊗λ_{k'}=0`, and the `λ_{k'}` are orthonormal up to one sign.
- **Corollary 2.3.** `tr(φ(N_x)−N_x)=tr(VN_xV^*)−tr N_x=0`, so the scalar is zero.
- [check] `check_blocks.py`, full cube, five colours, `m=1`, `ξ=e_F`, `F=\{0,…,k−1\}`, `k=1,…,5`, the draft's signs: the set of basis states reachable from `A` under `H` has `1+k` elements (first block) and `1+2k` elements (second block). `H^2A=(k/3)A` and `H^3A=((k+1)/3)HA` hold to rounding. The extra states are the `k` components of `B_ξ` and `C_ξ`, as the proof says.

### 4.C Section 3

- **One link hop.** For one particle and `m=1`, `T(|u,k⟩⊗|v;j⟩⊗ρ')=−|v,j⟩⊗|u;k⟩⊗ρ'`, and `T` kills the other basis states. So `T^*T` and `TT^*` are projections onto orthogonal spans, `T^2=0`, and `(T+T^*)^2=T^*T+TT^*≤1`.
- **Direction sums.** See item 39.
- **Interpolation.** `|a(λ−λ')|≤2√3|a|<2π` for eigenvalues of `H_1`.
- **Matrix elements.** `⟨v,j|H|u,k⟩=3^{−1/2}η_ℓr^v_jr^{u†}_k`, as an operator on the registers. For `m=1` this is `−3^{−1/2}η_ℓ|u;k⟩⟨v;j|` on `ℂ^{10}_ℓ`. With the adjoints, the products give `|u;k⟩⟨u;k'|` and `|v;j⟩⟨v;j'|`. So the generated algebra is `End(ℂ^{10}_ℓ)`, and the commutant of `End(R_ℓ)⊗1` is `1⊗End(\text{rest})`.
- [check] `check_onecolour.py`: the one-colour analogue (cube one-particle sector, dimension `8·2^{12}=32768`, signs `η=(1,(−1)^{x_1},(−1)^{x_1+x_2})`) has largest eigenvalue `1.3481` and smallest `−1.3481`. This reproduces the pass-1 number. It is not the five-colour sector and bounds nothing there.
- **Theorem 3.2.** `Γ(e^{iT})` is the site factor of `e^{i𝒢^T_x}` (`LW1_5.md` U), and every `u∈U(5)` is some `e^{iT}`. `V'=Γ(u)^*V` is the identity on `Λ^0⊕Λ^1`. `V'⊗L'` commutes with `W` and keeps `ℋ_1⊗(\text{extra})`, where it acts as `1⊗L'`. Theorem 3.1 gives `L'=1⊗L''`. `W` acts trivially on the extra registers, so `(V'⊗1)W=W(V'⊗1)`. Theorem 2.2 gives `V'∈ℂ1`, and `V'|_{Λ^0}=1` gives `V'=1`.
- **Line 72.** `LW1_5.md` line 117: "including a two-mode `U` link at `m=2,a=π/\sqrt2`". It is a single link, two modes, `m=2`, at an angle above `π/√3`. The remark is right.

### 4.D Section 4

- **Theorem 4.1.** `c_{v,j}r^{v†}_jr^u_kc^†_{u,k}=(r^{v†}_jr^u_k)(c_{v,j}c^†_{u,k})=(−r^u_kr^{v†}_j)(−c^†_{u,k}c_{v,j})=c^†_{u,k}r^u_kr^{v†}_jc_{v,j}` for `u≠v`. Summing gives `T_{v→u}`. `Θ(c^†_jc_j)=1−c^†_jc_j` gives `N_x↦5−N_x` and `m↦10−m`. `Θ∘AdΓ(u)∘Θ^{−1}` sends `c_j` to `Σ_ku_{kj}c_k`, which is `AdΓ(ū)(c_j)`.
- [check] `check_link.py` part 3: three colours, one link, full matter and rishon Fock spaces (dimension 4096, sparse). The matrix of `Σ_{j,k}c_{v,j}r^{v†}_jr^u_kc^†_{u,k}` minus that of `T_{v→u}` is exactly zero.
- **Theorem 4.2.** `T^*T=Σ_{k,k'}|u,k'⟩⟨u,k|⊗r^u_{k'}p_vr^{u†}_k=(1⊗p_v)Z^*Z`, and `p_v` commutes with every `r^u_k`. On `p_u=p`, `‖Z^*Z‖=‖ZZ^*|_{p_u=p+1}‖=p+1` and `p_v=m−p`. The range: `p≤4` (room at `u`), `m−p≥1` (a rishon at `v`), `m−p≤5` (the register).
- [check] `check_link.py` part 1: one link, five colours, one particle at either end, sector `m`. The norm of `h_ℓ` equals `ν_m` for each `m=1,…,9` (`1, 1.414214, 2, 2.449490, 3, 3.464102, 4, 4.472136, 5`). So the single-link bound is attained.
- [check] `check_link.py` part 2: for each `m=1,…,9`, the 50 products `n^v_j(1−n^u_k)`, `n^u_k(1−n^v_j)` give distinct value vectors on the `C(10,m)` subsets, and the trade graph on the subsets is connected.
- **Theorem 4.3, star block.** A particle of colour `c` leaves `x` along `xy` only if `c∈F∖S` and `T≠∅`; it takes a colour `j∈T`. Case `k≥m`: `c∈F∖S` (`k−m+1` choices) and `j=j'`; then `T` is empty. Case `k≤m`: `c=k_0` and `j∈T` (`m−k+1` choices); then the `x`-end holds `F`. A return needs a colour the `x`-end holds and `x` lacks: `(S∖F)∪\{c\}=\{c\}`. Other links at `x` and `y` hold all `m` rishons at their `x` or `y` end, so they block. `|a|√(n/3)<π√(3/5)·√(5/3)=π`.
- [check] `check_blocks.py`: for every `m=1,…,5` and `k=1,…,5`, the set reachable from `A` in the full cube has `1+n` elements, with `n` as stated, and `H^2A=(n/3)A`.
- **Vacuum line.** `ρ_0:𝒟_0→ℂ` is a unital *-homomorphism. Its kernel is `𝒟_0e` for a central projection `e` (finite-dimensional C*-algebra; see the note on item 76). A scalar centre forces `e∈\{0,1\}`, and `ρ_0(1)=1` forces `e=0`.

### 4.E Section 5

- **`ν'_m`.** `min(1,25)`, `min(2,20)`, `min(4,16)`, `min(6,12)`, `9`, `min(12,6)`, `min(16,4)`, `min(20,2)`, `min(25,1)` give `1,2,4,6,9,6,4,2,1`.
- **Thresholds.** `π/√(3·2)=π/√6`, `π/√12=π/(2√3)`, `π/√18`, `π/√27=π/(3√3)`. For `m≤5`, `π/(√3ν_m)≤π/√3≈1.814<π√(3/5)≈2.433`. In the window `a_e<π/2≈1.571`.
- **Two gates.** `LW1_5.md` line 117: "If a frame is compatible with both cube gates, it satisfies the bound unless both angles are exceptional." With `(ε,μ)=((a_e+a_o)/2,a_o−a_e)`, the residual pairs are finite.
- **LW1-5-X-B_m.** At `a=−a_e` the site commutant is scalar (Theorem 4.3), `N_x` is kept (Corollary 2.3's argument), and the normalized `V'⊗L'` acts as `1⊗L'` on `ℋ_1`. An affirmative answer removes `L'` from the cube registers, and Theorem 4.3 gives `V'=1`. Conversely, if `L'` is scalar on the cube registers then `V'=1`. So a non-`U(5)` frame forces a nonscalar `L'` in the register commutant of `e^{iaH_1}`. Both claims of line 110 hold.

### 4.F Section 6

- **Charges for `L5-O`.** `Σ_j𝒢^{2j−1,2j}_x=Σ_jM^{2j−1,2j}_x+(\text{links})=N_x−5/2+(\text{links})`, by `n_j−1/2=M^{2j−1,2j}` (`LW1_5.md` §1). `LW1_5.md` Q and G: "Every hop and cube gate commutes with every `𝒢_x^{cd}`." So `Ad e^{itN_x}` keeps the site commutant, and the `U(5)` part of the `SO(10)` site action keeps `𝒟_0`. Theorem 4.3's centre and vacuum-line steps use only these facts.
- **Small angles (item 95), referee rebuild.** Faithful inflow (`LW1_5.md` M, which applies to `L5-O` by the independence sentence after M.1) gives `H=Σ_bγ_{x,b}B_b+H'`. With `γ_{2j−1}=c_j+c_j^†` and `γ_{2j}=i(c_j^†−c_j)`, `Π_{k+1}γ_{x,2j−1}Π_k=Π_{k+1}c^†_{x,j}Π_k` and `Π_{k+1}γ_{x,2j}Π_k=iΠ_{k+1}c^†_{x,j}Π_k`. So `Π_{k+1}HΠ_k=±Σ_jΠ_{k+1}c^†_{x,j}Π_k⊗(B_{2j−1}+iB_{2j})` in the Jordan–Wigner form. The five operators `B_{2j−1}+iB_{2j}` are independent, and `Π_{k+1}c^†_{x,j}Π_k≠0` for `k≤4`. So the block is nonzero for `k=0,…,4`. Then `Π_{k+1}WΠ_k=iaΠ_{k+1}HΠ_k+O(a^2)` is nonzero for small `|a|>0`, and the edges `\{k,k+1\}` connect `\{0,…,5\}`. Line 120 is right.

### 4.G Section 7

The inputs line 128 names are the ones used, with one omission: `LW1_5.md` C (item 103). "They do not independently re-audit the frozen source" is accurate; this report also does not, beyond the `a=0` remark in §2.1.

---

## 5. LW1_5X.md against LW1_5X_DRAFT.md

Each "(draft …)" citation in LW1_5X.md was compared with the draft text it names.

| LW1_5X item (line) | Draft item (draft line) | Result |
|---|---|---|
| Theorem 2.1 (32-34) | Lemma 1.1 (55-59) | Same statement and proof. |
| Theorem 2.2 (36-52) | Lemma A, Steps 1-6 (65-100) | Same statement. The proof compresses Steps 1-6 and keeps every computation. |
| Corollary 2.3 (54-56) | Corollary A.1 (104-108) | Same statement. LW1_5X rebuilds `LW1_5U_DRAFT.md` Lemma X1 instead of quoting it; the rebuild is right (§4.B). |
| Theorem 3.1 (60-64) | Lemmas N and B (114-132) | Same statements. LW1_5X drops the draft's orthogonal-sector step (draft line 116: the norm of each direction's sum is the maximum over its four links), which is item 39. |
| Line 66 | [check] (122) | Exact: one colour, `8·2^12`, `1.3481`. |
| Theorem 3.2 (68-70) | Theorem X (136-144) | Same. LW1_5X omits "Proposition X2's finite set of possible bad points is empty", which follows. |
| Line 72 | Remarks (1) and (4) (146) | Same. |
| Theorem 4.1 (76-78) | Lemma D (154-164) | Same. |
| Theorem 4.2 (80-88) | Lemmas N_m and B_m (168-178) | Same. |
| Theorem 4.3 (90-96) | Lemma A_m, Steps 1-6 (182-200) | Same. LW1_5X drops the rebuild of the central support projection in Step 5 (note on item 76). |
| Theorem 5.1 (100-102) | Theorem X_m (204-206) | Same; LW1_5X adds the explicit one-hole clause for `m≥6`, which the draft's proof implies. |
| Corollary 5.2 (104-106) | Corollary X_m.1 (208-210) | Same values. LW1_5X repairs the finite-set sentence (GAP 1). |
| LW1-5-X-B_m (110) | LW1-5-X-B_m (212-214) | Same content, posed as a question. LW1_5X adds "sufficient, not shown necessary", which is right. |
| Line 112 | Attacks 1-3 (215-217) | A faithful summary. LW1_5X adds "limitations of the routes, not no-go results", which is right. |
| Theorem 6.1 (116-118) | Lemma A_O (229-231) | Same. |
| Line 120 | Draft line 233 | Same claim; LW1_5X makes the derivative argument explicit. |
| LW1-5-X-O (122) | LW1-5-X-O (239-240) | Same question. |
| Line 124 | Attacks 1-3 (242-244) | GAPs 2 and 3 are real (§3). Attack 2 is hedged correctly ("can occur" for the draft's "they include"). |

One draft sentence is rightly not carried. Draft line 237: "The only conserved charges are the Gauss generators `𝒢^{cd}_z`, and every one of them has a link part, which `Ad L` moves." This is false as written: `P_C` commutes with every cube gate and has no link part, and the draft itself names `P_xP_𝔐` at line 242. LW1_5X line 122 replaces it with "the Majorana hop has pairing terms, so those particular tools are unavailable", which is right.

The draft's quotations of `LW1_5U_DRAFT.md` Proposition X2 (line 173) and Lemma X1 (line 179) match that file. Its other citations (`LW1_5_DRAFT.md`, `B5B_DRAFT.md` line numbers) were not re-checked. LW1_5X.md does not rely on them: it re-bases every dependency on frozen `LW1_5.md`, and the cited results are there (§1, C, C2, M and M.1, Q and G, U, line 117).

---

## 6. Edits

### 6.1 Required before the freeze

None of these changes a theorem.

1. **Line 24 (item 15).** Replace "Thus `e^{iaK}` determines `K` by polynomial interpolation precisely outside that set." with "For `a≠0`, `e^{iaK}` determines `K` by polynomial interpolation precisely when `a` lies outside that set." The amendment can note that `LW1_5.md`'s M.1 sentence needs the same `a≠0` (§2.1).
2. **Line 62 (item 39).** Before "Thus the triangle inequality", insert: "Each one-particle state has its particle at an end of exactly one link of a given direction, and a hop kills the states whose particle is not at its ends. So the four hops of one direction act on mutually orthogonal invariant subspaces, and their sum has norm at most one." Then write "the triangle inequality over the three directions". On line 86, write "Sum over the three directions, each a set of four disjoint links, as in Theorem 3.1."
3. **Lines 11 and 120 (item 9).** Name the amplitude hypothesis and list it under "Open by name", for example: "**LW1-5-X-OA (OPEN).** For an `L5-O[S_+]` cube gate `W` at a window angle, the pairs `{k,k'}`, `k≠k'`, with `Π_{k'}WΠ_k≠0` connect `{0,…,5}`." The name is for the lead to choose; §2.2 gives the four-test check of this one.
4. **Line 13 (item 10).** Label the second effort record: "Pass 2 (the distiller's own record, historical): … reasoning effort not visible …".

### 6.2 Recommended

5. **Line 38 (item 23).** Name the charge: "`𝒢^1_x=N_x+Σ_{ℓ∋x}p_{ℓ,x}` commutes with `W`".
6. **Line 40 (item 24).** Add: "the seven links not incident on `x` or `y` are in any fixed state".
7. **Line 46 (item 28).** Replace "at its occupied endpoint" with "at its endpoint in `{x,y,z}`".
8. **Line 70 (item 48).** Add: "`ℋ_1` tensored with the extra registers is invariant under `W` and under `V'⊗L'`".
9. **Line 94 (item 72).** Replace "fills the sole hole in the departure-end rishons" with "fills the only colour of `F` absent from the departure end".
10. **Line 96 (item 76).** Restore the draft's three-line rebuild of the central support projection (draft line 198).
11. **Line 104 (GAP 1).** Add statement (i) of §3.1: for the even gate alone the exceptions lie on finitely many segments `ε−μ/2=a*`.
12. **Line 124 (GAPs 2 and 3).** Optionally add the witness `V_{(α:β)}` of §3.2 and Lemma R1 of §3.3, so the two gaps read as settled off the points they concern.
13. **Line 128 (item 103).** Add `LW1_5.md` C to the inputs.
14. **Line 66 (item 43).** Optionally record that a referee [check] reproduced `1.3481` in the one-colour analogue; it still guides only.

---

## 7. Open statements to carry by name

- **LW1-5-X-B_m (OPEN), `2≤m≤8`.** For `2≤m≤5`, at an exceptional angle `a` of `H_1` with `π/(√3ν_m)≤|a|<π/2`: is every register unitary `L` with `[1⊗L,e^{iaH_1}]=0` the identity on the cube registers tensored with a unitary on the other registers? For `6≤m≤8`, the same question on the one-hole sector (equivalently, LW1-5-X-B_{10−m} through Theorem 4.1). An affirmative answer gives the even-gate frame bound at `a_e=|a|`. Three named attacks failed (line 112; draft lines 215-217): functional calculus, gauge covariance and the centre, register blocks. No counterexample is known.
- **LW1-5-X-O (OPEN), `L5-O[S_+]`.** At the finitely many window points where both cube angles are exceptional, is every frame compatible with both gates Bogoliubov? Three named attacks failed (draft lines 242-244): the U-law route, parity slices, the Lie algebra of the compatible group. No counterexample is known.
- **LW1-5-X-OA (OPEN), the amplitude hypothesis of Theorem 6.1.** Stated in §6.1, edit 3. It holds for small nonzero `|a|`. It is unchecked at general window angles.

The statement of GAP 3 at exceptional angles ("parity is the only matter-only conserved quantity") need not be carried: no proof uses it, and Lemma R1 settles it off the exceptional set.

---

## 8. Recommendation

LW1_5X.md can enter frozen `LW1_5.md` by a dated amendment once the four required edits of §6.1 are made. The proofs of Theorems 2.1-6.1 and Corollaries 2.3 and 5.2 are correct, with one sentence to add to Theorem 3.1's norm bound (edit 2). The one ERROR and the two INCOMPLETE items are textual: a missing `a≠0`, that missing sentence, and a missing name. Each GAP the distiller marked is real, is correctly kept out of the proofs, and has a repaired statement in §3.

The amendment should state the status change in `LW1_5.md`'s open list. **LW1-5-X**: proved for `L5-U[m]`, `m∈\{1,9\}`, gate-wise by the even gate at every window point. For `2≤m≤8` it is proved outside the residual set of §3.1(i) (even gate) and of §3.1(ii) (both gates). The residual is carried as LW1-5-X-B_m, a sufficient condition. For `L5-O[S_+]` it stays open as LW1-5-X-O, with Theorem 6.1 conditional on LW1-5-X-OA. The amendment should also say that these are results about the conditional laws of `LW1_5.md`. They fix no `m`, select no law and change no axiom.

---

## FINISH

**Proved here (pass 3, one check; the referee's own closures are themselves unrefereed).**
- Every statement and proof step of LW1_5X.md was re-derived (§1, §4). Theorems 2.1, 2.2, 3.1, 3.2, 4.1, 4.2, 4.3, 5.1 and 6.1 and Corollaries 2.3 and 5.2 hold as stated, given edit 2 for Theorem 3.1's norm bound. Definition 4 holds in its fixed form (`a≠0`).
- The repaired residual statement of GAP 1 (§3.1): for the even gate alone the exceptions lie on finitely many segments `ε−μ/2=a*`; for both gates they form a finite subset of Proposition X2's set.
- The witness for GAP 2 (§3.2): the pairwise distinct `SO(10)`-invariant subspaces `V_{(α:β)}`, `(α:β)∈ℝP^1`, of the even site algebra.
- **Lemma R1** (§3.3): for `L5-O[S_+]`, a cube matter element that commutes with `H_C`, or with the gate at a nonzero nonexceptional angle, lies in `span\{1,P_C\}`.
- The small-angle case of Theorem 6.1's hypothesis (§4.F), rebuilt from faithful inflow.

**Counterexamples.**
- Definition 4's "precisely outside that set" at `a=0`: `K=diag(0,1)` (§2.1). `LW1_5.md`'s M.1 sentence fails the same way at `a=0`; no result in either file uses `a=0`.
- The draft's sentence "For `2 ≤ m ≤ 8` the remaining points lie in Proposition X2's finite set" (draft line 210), read for the even gate alone: each exceptional `a*` leaves the segment `ε−μ/2=a*` (§3.1).
- The draft's inference "So only finitely many candidate algebras exist" (draft line 244) from the module decomposition: the continuum `V_{(α:β)}` (§3.2). This refutes the inference, not its conclusion.
- The draft's sentence "The only conserved charges are the Gauss generators" (draft line 237): `P_C` (§5). LW1_5X.md does not carry it.

**Open, by name.**
- **LW1-5-X-B_m** (`2≤m≤8`): the one-particle (one-hole for `m≥6`) register commutant at exceptional angles in `[π/(√3ν_m),π/2)`. Sufficient for the even-gate frame bound. Three attacks failed: functional calculus, gauge covariance and the centre, register blocks.
- **LW1-5-X-O** (`L5-O[S_+]`): the frame bound at the finitely many points where both cube angles are exceptional. Three attacks failed: the U-law route, parity slices, the Lie algebra of the compatible group.
- **LW1-5-X-OA** (label proposed here): the connectivity hypothesis of Theorem 6.1 at general window angles. It holds for small nonzero `|a|`.

**What changes downstream.**
- With the edits of §6.1, LW1_5X.md can enter frozen `LW1_5.md` by a dated amendment (§8). LW1-5-X then reads: proved for `L5-U[m]`, `m∈\{1,9\}`, at every window point by the even gate; proved for `2≤m≤8` outside the residual of §3.1, which is carried as LW1-5-X-B_m; open for `L5-O[S_+]` as LW1-5-X-O, with LW1-5-X-OA.
- The amendment can record `a≠0` in `LW1_5.md`'s M.1 sentence. No result there changes.
- Nothing here fixes `m`, selects a law, changes an axiom or a working-set entry, or decides a physics question. The owner's choice of both live laws stands.
