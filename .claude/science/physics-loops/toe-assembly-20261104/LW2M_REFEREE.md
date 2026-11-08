lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# LW2M referee report (pass 3)

Written 2026-11-08 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as pass 3 under PR #10138's method. Claude drafted pass 1 (`LW2M_DRAFT.md`). Codex gpt-6.1-terra distilled pass 2 (`LW2M.md`). This session wrote neither. This is one check: one whole-part, line-by-line read of `LW2M.md`. No review of this review was commissioned.

**Text read.** `LW2M.md` as of commit `ecdf9708b` (the last commit that touches it; branch `claude/toe-assembly` head). SHA-256 prefix of the file read: `b85d901eed63ba9c`. Line numbers below refer to that file.

**Sources read, with commits.**

| Ref | Commit |
|---|---|
| branch `claude/toe-assembly` (this checkout) | `ecdf9708b` |
| `LW2M.md` (pass 2, the text refereed) | `ecdf9708b`, SHA-256 prefix `b85d901eed63ba9c` |
| `prior/LW2M.md` (prior-work digest) | `0ec9a2b33`, SHA-256 prefix `3f17ca6865fdbeeb` |
| `LW2M_DRAFT.md` (pass 1) | `a6291aad1`, SHA-256 prefix `f11d35a648da7a24` |
| `origin/claude/ym4d-hard-route` (`git fetch -q`, then `git show` only) | `85d76598f` |

Files read, by line. This folder: `LW2M.md` lines 1-399 (all); `prior/LW2M.md` lines 1-77 (all); `LW2M_DRAFT.md` lines 1-16 and grep hits at 44, 205-213, 233, 288, 308, 326, 391, 396, 417-419, 434, 482, 487-488; `LW1_REFEREE.md` lines 1-80 and `Y2W_DRAFT.md` lines 1-30 (format only); `GA1_5.md` lines 5-13, 48-52, 65-90, 199-272; `LW1.md` lines 36-44, 399-402; `LW1_5.md` lines 18, 42, 86-101, 137, 264-276, 323; `GB1ISO.md` lines 38, 62, 91, 111, 161, 165, 167; `GB1ISO_REFEREE.md` lines 116-120; `GB1QL.md` lines 55-60, 137-146, 299; `GB1E.md` lines 27-37, 76-78, 145-150, 158, 180; `GB1E_REFEREE.md` line 143; `GB1.md` lines 11, 58; `GB1_GEN_OWNER_CHECK.md` lines 7-27, 77, 83. YM branch, `.claude/science/physics-loops/ym4d-hard-route-20261030/library/`: `o4-two-point.md` lines 5-75, 167-203 (last changed `0f018e1a4`); `lg1.md` lines 365-367 (`f9945a2b5`); `t0-tree.md` lines 164-168 (`79192bd78`); `ro1.md` grep hits for "H-L" at lines 64, 121, 630, 649 (`922ec0066`). `docs/MINIMAL_AXIOMS_2026-06-29.md` was not read and is unchanged.

**Working-set entries used.** PS-1c (cell covariance), through the NN-a clause "commutes with every cell lift"; PS-6 and PS-6r (gauge invariance, finite link registers); PS-5 (five-mode sites), only through the site algebras in Lemma U; the owner's NN-a decision (`GA1_5.md` line 7: "owner decision GA1-P-NN = NN-a"). The two live laws `L5-U[m]` and `L5-O[S_+]` (`LW1_5.md` §2). Proposed readings used as `LW2M.md` uses them, none adopted: R-SUM and R-IA (`GB1_GEN_OWNER_CHECK.md`), FS-ex, FS-sum, FS-1, R-COV_s. The test law `L5[SU(2),s]` of `GB1QL.md` is not a working-set law.

**Method.** Every proof step is re-derived by hand. A `[check]` is a tiny scratch computation in `/tmp/toe-LW2Mref/` (under a minute, a few MB, dense matrices at most `2^12 x 2^12`). It guides or refutes and never proves. Verdicts: CORRECT; ERROR (a false line, quoted, with the fix); INCOMPLETE (a named missing step). A "referee closure" is a short complete argument for a missing step. Owner guidance applied, verbatim: "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The axioms and readings are read plainly.

---

## 1. Verdict table

Verdicts are on the pass-2 text. "Re-derived" means the step was redone by hand in this session. Items 1-6 (section 0 of `LW2M.md`) are graded last, in section 1d, because they summarize later results.

### 1a. Definitions, section 1 (setting) and section 3 (NN-a check)

| # | Item (`LW2M.md` line) | Verdict | Note |
|---|---|---|---|
| 7 | Definition 1, boxes and locality (19) | CORRECT | Even `N` is what makes the parity tilings well defined on the torus. |
| 8 | Definition 2, mixed plaquettes and `∂p` (20) | CORRECT | Same as `GA1_5.md` line 48: "A plaquette's type is the unordered pair of its two in-plane base parities". |
| 9 | Definition 3, ordering and covariance as equality of automorphisms (21) | CORRECT | |
| 10 | Definition 4, FS readings and the FS-1 family (22) | INCOMPLETE | The fixed-support, fixed-generator clause is not enough for the §4.5 proof as written (item 52). The referee closure of §2.1 makes the clause unnecessary. |
| 11 | Definition 5, the test family `R_s` (23) | CORRECT | |
| 12 | Definition 6, ISO-FP[W] and R-COV_s constants (24) | graded with §5 (item 58) | |
| 13 | §1.1 the two live laws (30) | CORRECT | Matches `LW1_5.md` line 89: "\(T_{ij}=i\eta_i\eta_j/2\), and \(U^{ab}=2T_{a,10+b}\), with \(\eta_a=\eta^y_a\) and \(\eta_{10+b}=\eta^x_b\)", and line 42: "Links commute with matter and are ordinary tensor factors." So `U^{ab}=iη^y_aη^x_b`, `a,b=1,…,10`. |
| 14 | §1.1 plaquettes, `B_C`, lift identity (32) | CORRECT | Quote of `GA1_5.md` line 50 is exact. `GA1_5.md` line 85 states "is carried by a cell lift to `W(gc)`"; with orientation independence of `B_p` this gives `α_g(B_C)=B_{gC}`. |
| 15 | §1.1 SU(2) family (34) | CORRECT | `GB1E.md` line 27: "put \(B_p=2\operatorname{Tr}X_p\)". |
| 16 | §1.2 the four tilings (38) | CORRECT | Wording: "the two site-disjoint families" means each of `𝒯_e+v`, `𝒯_o+v` is internally site-disjoint; the two families share sites with each other. `LW1.md` line 38 defines `𝒯_e,𝒯_o`; `GB1ISO.md` line 38 (Theorem 2.1): "Each link belongs to one cube in \(\mathcal C\)". |
| 17 | Lemma 1.1, memberships and table (40-48) | CORRECT | Re-derived: `p` is a face of the cube with base `b` iff `b_i=y_i`, `b_j=y_j`, `b_k∈{y_k,y_k-1}`; exactly one `b_k` has the parity `𝒞_v` needs iff `y_i-v_i≡y_j-v_j`. All six table entries checked. |
| 18 | `H_v`, `W_v(φ)`, the FP word (50) | CORRECT | `Σ_vH_v=2Σ_pB_p`, so the four factors at `θ/2` give angle `θ` per plaquette. `LW1.md` E1 is at line 401. |
| 19 | Lemma 1.2, the cell group permutes the shifted tilings by every permutation (56-58) | CORRECT | Re-derived with `c_0=𝟙/2` (`LW1.md` line 38). For `δ_i=-1` the interval `[b_i,b_i+1]` maps to `[-b_i,1-b_i]+2t`, so base parity is kept and only permuted. `det Q=sign(π)∏δ_i`, so every `π` has a proper lift. The quarter-turn `Qe_1=e_2`, `Qe_2=-e_1`, `Qe_3=e_3` gives `π=(12)`. |
| 20 | Referee quote and quarter-turn (60) | CORRECT | Quote matches `GB1ISO_REFEREE.md` line 119. |
| 21 | §1.4 components (64) | CORRECT | |
| 22 | Lemma 1.3 (66-68) | CORRECT | Notation: in (d), `tr(X⊗_{ℓ∈S}Z_ℓ)` must be read as `tr(X·⊗_{ℓ∈S}Z_ℓ)` (a product, not a tensor product). Edit E1. |
| 23 | Components of locally finite sums (70) | CORRECT | Uses that each link meets finitely many supports. |
| 24 | Lemma 1.4, nonzero component gives a nonzero derivation (72-74) | CORRECT | Re-derived. Maximality of `T` among `T'∋ℓ` kills the `T'⊋T` terms; `[K_T,A]=Σ_r[x_r,A]⊗y_r` is its own `T`-component and is nonzero by independence of the `y_r`. |
| 25 | §1.5 chains, pinned chains, straight rows (78) | CORRECT | Each link lies in at most two chain plaquettes, so `S_n` has `3n+1` links. |
| 26 | Lemma 1.5, rigidity (80-82) | CORRECT | Re-derived for the perpendicular case. Parallel non-coplanar plaquettes share no link, so the two cases are exhaustive. `N≥3` excludes wrap-around squares. |
| 27 | Lemma 1.6, structure of `Y_n` (86) | CORRECT | `[a_1⊗x,b_1⊗y]=a_1b_1⊗[x,y]` when `a_1,b_1` act on disjoint link sets and all link entries are even. |
| 28 | Lemma 1.6(a) on `L5-U[m]` (88-92) | CORRECT | Re-derived: `U^{ab}=-E_{xb,ya}`, `(U^†)^{cd}=-E_{yd,xc}`, `[E_{αβ},E_{γδ}]=δ_{βγ}E_{αδ}-δ_{αδ}E_{γβ}` gives line 90. `tr n_{xb}(1-n_{ya})=\binom{8}{m-1}>0` for `1≤m≤9`. Corner indices are per plaquette, so `a=d`, `b≠c` can be imposed at each shared link while the single links pin the rest. Exactly one term survives; pairing `±κ_m^{3n+1}`. |
| 29 | Lemma 1.6(b) on `L5-U[m]` (92) | CORRECT | `[U^{ab},n_{x,c}]=-δ_{bc}U^{ab}`, `[(U^†)^{ab},n_{x,c}]=δ_{ac}(U^†)^{ab}` checked. |
| 30 | Lemma 1.6(a),(b) on `L5-O[S_+]` (94) | CORRECT | Re-derived: an even product of `r` distinct generators, `0<r<20`, is traceless on `S_+`; `[iη^y_aη^x_d,iη^y_aη^x_b]=-2η^x_bη^x_d`. In (b) the `y`-corner index of `p_1` on `ℓ_0` must be chosen `1`; the text does this implicitly ("`[±iη^y_1η^x_b,A_0]`"). |
| 31 | Lemma 1.6(c) on `R_s` (96-100) | CORRECT | Conditional on `GB1QL.md` Proposition 4.2(a),(b) (line 143: "`[P_μ, P_ν] = i L_{μν}/c_s²`") and `P_μ1=x_μ`, which follows from line 57 (`P_μ = x^+_μ Y_s + Y_s x^-_μ`) and `y_0=1` (line 56). Pins `4,4,4` on `p` and `1,4,4` on `q` give `t_p∝δ_{μ4}`, `t_q∝δ_{ν1}`; with `(α,β)=(1,4)` the bracket is `±4≠0`. |
| 32 | Theorem 3.1, FP compiles into even nearest-neighbour gates of finite depth and is gauge invariant (106-118) | CORRECT | Conditional on `GA1_5.md` §8, Lemma U (line 236) and Proposition C(i) (lines 262-270), which that frozen file marks "unrefereed" (line 201); §0 states the condition. Lemma U's setting covers both laws (line 234: "`C(10,m)≥10` on `L5-U`; 512 on `L5-O[S_+]`"). Translating Proposition C(i)'s cube argument by `v` is valid: cubes of `𝒯_e+v` are `2Z^3`-translates with disjoint sites and links, and every corner of a cube is shared by three of its links, so Lemma U's `w` is a corner. Gauge invariance is required of the update, not of each gate (NN-a, `GA1_5.md` line 215). |
| 33 | Theorem 3.2, FP not cell covariant outside a closed discrete set (122-142) | CORRECT | Re-derived: `α_g∘β_θ∘α_g^{-1}=β'_θ`; the second-order defect is `-φ^2/2[K,·]` with `b_{uv}=ε_{uv}-ε_{πu,πv}`; on `S=∂p∪∂q` only `{p,q}` contribute (Lemma 1.5(i)); `c_{01}=c_{02}=-1`, `c_{12}=1`, others `0`; `K_S=2ε_{12}[B_p,B_q]_S≠0`. The zero set of one nonzero entire function bounds the covariant angles. The base-tick step uses `LW1_5.md` line 276 (item 34). |
| 34 | Base tick covariance and `α=α_0∘β_θ` (142) | ERROR (quotation only) | The logic is right: `U^*AU=α_0(β_θ(A))`; with `α_0` covariant, `α_gαα_g^{-1}=α` iff `α_gβ_θα_g^{-1}=β_θ`. But the quoted words "the tick automorphism commutes with each lift" do not occur in `LW1_5.md` (grep finds no "each lift"). Line 276 is inside the proof of B1-U. The statement is line 268: "The base \(L5\)-U tick is covariant under the cell group". Edit E3: quote line 270 and the corresponding `L5-O` covariance statement (item 37a). |
| 35 | Remarks (1)-(3) after Theorem 3.2 (144) | INCOMPLETE | Remark (1) proves the claim for `φ_0=λφ` with `λ` fixed, a joint expansion. For a fixed `φ_0≠0` with `𝒞_0` between shifted letters, the defect starts at first order in `φ`, as `iφ[D_1-D_2,e^{iφ_0D_0}]`, which the remark does not compute. Edit E2: replace "for any `φ_0`" by "for `φ_0=λφ`, any fixed real `λ`". Remarks (2) and (3) are correct under the same scaling. |
| 36 | §3.3 NN-a table and the sharpening of `GB1ISO.md` (148-155) | CORRECT | Follows from items 32-34. |

### 1b. Section 4 (GB1-CF at finite register)

| # | Item (`LW2M.md` line) | Verdict | Note |
|---|---|---|---|
| 37 | §4.1 the readings FS-ex, FS-sum, FS-1 (161-165) | CORRECT | The FS-sum quote matches `GB1_GEN_OWNER_CHECK.md` line 27: "For GB1's specified layers \(e^{-i\tau_kK_k}\), set \(H=\sum_k\tau_kK_k\)". |
| 38 | "FS-sum implies FS-1 for every word in exponentials of the `K_k`" (167) | INCOMPLETE | True when every exponent is linear in the angle, `τ_k=θt_k`. A word with a fixed nonzero exponent, such as `V^{-1}e^{-iθK}V`, has first-order generator `V^*KV`, not `K`. Edit E4: add "with exponents linear in `θ`". |
| 39 | Four-test table for FS-ex, FS-sum, FS-1 (169-173) | CORRECT | Graded in section 4 of this report. The R-SUM test-3 grade C is quoted correctly (`GB1_GEN_OWNER_CHECK.md` line 77: "**C.** Supplies the energy reading and Euclidean correlations."). |
| 40 | "the update must also be NN-a admissible, so exactly cell covariant" (175) | CORRECT | |
| 41 | Theorem 4.2, statement (179) | CORRECT | |
| 42 | Theorem 4.2, steps (1)-(3) (181-185) | CORRECT | Re-derived. A link operator meets a gate only through the gate's own link; even gates keep supports local. A link-only element of a ball algebra lies in `B(H_B)⊗1`. A term of `ad^n_{H_N}A_0` with nonzero `S_n`-component has support exactly `S_n` (at most `1+3n` links), so its plaquettes are the row plaquettes (Lemma 1.5(ii)) in row order. Only the chain commutator survives, and Lemma 1.6(b) makes it nonzero. |
| 43 | Theorem 4.2, step (4) and the update (187) | CORRECT | `n=D+4` needs `N>2n+4=2D+12`, so even `N≥2D+14` works. A countable union of closed discrete sets is countable. For the update, `W_E` is one layer of single-link gates. The cube matter gates compile by `LW1_5.md` line 323 (finite edge factorization). |
| 44 | Remark after Theorem 4.2 (189) | CORRECT | |
| 45 | Class `𝒲`, `β_w`, `a_{uv}`, `A_{uv}` (193) | CORRECT | With `C_0=C_1`, `φΣ_vC_vH_v=2C_1φΣ_pB_p`. |
| 46 | Theorem 4.3 (195-199) | CORRECT | Re-derived. The quadratic part `½(Σx_k)^2` is relabelling-invariant exactly when `C_1=C_2=C_3`. `d_{uv}=A_{uv}-A_{π^{-1}u,π^{-1}v}`. Each pair of perpendicular planes realises all four membership combinations. `f_{01}+f_{02}+f_{03}-s=2e_0`, so `f_{01},f_{02},f_{03},s` is a basis of `R^4` and their six wedges span `Λ^2R^4`. |
| 47 | Corollary 4.3.1 (201) | CORRECT | Lie-Trotter: within-step pairs give `ε_{uv}/n`, cross-step pairs are symmetric. |
| 48 | Lemma 4.4.1, symmetric BCH (211-213) | CORRECT | Re-derived: coefficients `1/48-3/48-1/48+1/48=-1/24` for `[X,[X,Y]]` and `1/24+1/24=1/12` for `[Y,[Y,X]]`. Oddness of `log` removes the `t^4` term. |
| 49 | Theorem 4.4, palindromes and Strang products (215-242) | CORRECT | Re-derived by hand: the six-order evaluation `Y,-Y,0,0,-Y,Y`, `Γ_{uvw}=2a_us(v,w)`, the formula for `k(u,W)`, and all eight `κ` values of the table (`-1/3,-4/3`; `5/12,-4/3`; `2/3,-7/12`; `2/3,-1/3`). The reduction of 24 orders to the four positions of `0` is valid. |
| 50 | Class `𝒟` (246) | CORRECT | Matches `GA1_5.md` line 52 (GA1-P-5) restricted to disjoint supports. |
| 51 | Theorem 4.5, zero `∂p`-component and the FS-sum clause (248-250) | CORRECT | Re-derived. `GA1_5.md` line 77 (Theorem 2.2) is quoted exactly. At the corner `y` of a mixed plaquette, `(y,y+e_i)` and `(y,y+e_j)` have opposite parity, so no member contains `∂p`. Lemma 1.3(c) gives `(h_X)_{∂p}=0`. |
| 52 | Theorem 4.5, FS-1 clause (248, 250) | INCOMPLETE | Two missing steps. (i) "Differentiating a fixed-support, fixed-generator family at zero produces the sum of coefficient derivatives times these generators" holds only if every sublayer is a scalar at `θ=0`. If `φ_X(0)≠0` for some sublayers, the generator is `Σ_sV_s^*G_sV_s`, with `V_s` the product of the earlier sublayers at `θ=0`. Conjugation by `V_s` can enlarge supports. (ii) A zero component must be converted into a nonzero derivation (Lemma 1.4). Referee closure §2.1 proves a stronger FS-1 clause, with no fixed-support or fixed-generator condition, on both laws. |
| 53 | Remark after Theorem 4.5 (252) | CORRECT | Quote of `GA1_5.md` line 89 is exact. |
| 54 | Proposition 4.6(a) (260, 264) | CORRECT | Inputs quoted correctly: `GB1QL.md` line 299, Proposition 4.11(b),(c). Lemma 1.6(c) replaces Lemma 1.6(a). |
| 55 | Proposition 4.6(b), the `θ^2N^3/s` bounds (262, 266) | CORRECT | Re-derived: `‖P_μ‖≤1` from `Σ_μP_μ^2=(s(s+3)-k(k+2))/c_s^2≤1` (`GB1QL.md` line 145) and `c_s^2=s(s+3)`. The bracket has `4^8` terms with coefficients at most `16`, so `‖[B_p,B_q]‖≤2^{20}/s`. `3N^3` plaquettes, `12` neighbours each: `36N^3C_0/s`. Telescoping with `GB1.md` line 58 gives `(φ^2/2)·6·36N^3C_0/s=27θ^2N^3C_0/s`. The second bound uses `α_g(e^{-iθH_N})=e^{-iθH_N}`. |
| 56 | Paragraph after Proposition 4.6 (268) | CORRECT | |
| 57 | LW2M-WORD, statement, proved cases, uncovered words (272-274) | CORRECT | Statement is equivalent to: for every word of `𝒲`, the entire defect function is not identically zero for some `π`. The Suzuki relation and the invariance of the cell-averaged order matrix are re-derived. Referee closure §2.3 settles the cell-averaged product for most block orders. |
| 57a | The three failed attacks on LW2M-WORD (276-278) | CORRECT | They are distinct: a jet computation, a group-freeness argument, a finite-angle support argument. Each names its failing step accurately; for attack 3, a chain that turns a corner has a plaquette whose single sides are adjacent, so it is not pinned. |
| 57b | Corollary 4.8.1 (282-284) | CORRECT | A periodic commuting decomposition would give a depth independent of `N` through Lemma U and Proposition C(ii), contradicting Theorem 4.2. |
| 57c | Verdict on GB1-CF (286) | INCOMPLETE | Correct summary, except that the FS-1 clause for `𝒟` should be stated in the form of referee closure §2.1, and the cell-averaged product moves to the proved list (§2.3). Edit E5. |

### 1c. Sections 5-7 (ISO-FP, candidate texts, prior results)

YM files were read at `origin/claude/ym4d-hard-route` head `85d76598f`, with `git show` only. Last commits of the files read: `library/o4-two-point.md` `0f018e1a4`, `library/lg1.md` `f9945a2b5`, `library/t0-tree.md` `79192bd78`, `library/ro1.md` `922ec0066`. The draft read the branch at `8d48cdf80b`. Every quoted YM line was found at the cited line number at the newer head.

| # | Item (`LW2M.md` line) | Verdict | Note |
|---|---|---|---|
| 58 | Definition 6 (24) | INCOMPLETE | Correct as far as it goes. It should name the hypotheses that "the cited conditional YM theorem" needs; see item 72. Edit E7. |
| 59 | §5.1 setting, the two transfers, the lift (292-297) | CORRECT | `GB1E.md` line 29 quote is exact; lines 33-37 give the local lift; two half-weights `e^{-λθ\,{\rm Tr}X_p}` give `β=-2λθ`. |
| 60 | Theorem 5.1, statement (303) | CORRECT | |
| 61 | Theorem 5.1, existence of the exact FP lift (305) | CORRECT | Port of `GB1E.md` Theorem 3.2. Its proof (line 78) uses `W=V_θ` through the smooth-multiplier commutator bound, `‖W‖`, and the nonnegative kernel of `e^{-sW}`. `θΣ_p2{\rm Tr}X_p` has all three properties and is gauge invariant. `GB1ISO.md` Theorem 2.4 (line 62) needs "a transfer with nonnegative gauge-covariant kernel"; `GB1E.md` line 76 supplies "a bounded nonnegative Haar density". |
| 62 | The function `Δ` and its trace formulas (307-312) | CORRECT | In temporal gauge `{\rm Tr}W=Σ_{ab}\overline{U'_{ab}}U_{ab}`. `Σ_{ab}M_{ab}^*TM_{ab}` is gauge invariant because unitarity of the site actions sums out the indices. |
| 63 | Analyticity (314) | CORRECT | Quote of `GB1E.md` line 158 is exact. The insertions are bounded multiplication operators. |
| 64 | `Δ(0)<0` (316-320) | CORRECT | Re-derived: `Σ_{ab}M_{ab}^*e^{-uE^2}M_{ab}` has kernel `k_u(gh^{-1})χ_{1/2}(gh^{-1})`. The coefficient of `χ_{k/2}` in `χ_{1/2}k_u` is `ke^{-u(k-1)(k+1)/4}+(k+2)e^{-u(k+1)(k+3)/4}`; divide by `k+1`. At `k=0` it is `2e^{-3u/4}>0`. `M` is odd for the flux parity of four links, so `𝔼_0{\rm Tr}X_{p_s}=0`. |
| 65 | Invariance forces `Δ=0` (322) | CORRECT | Spatial translations, spatial cubic symmetries and time translation make all spatial plaquettes, and all temporal plaquettes, equidistributed for `{\rm Tr}X`. |
| 66 | Remark on `ς` (324) | CORRECT | `GB1E_REFEREE.md` line 143: "The diagonal mirror `x_1 ↔ t` is the exchange `ς` itself". |
| 67 | Wilson multipliers (328) | CORRECT | Quotes of `GB1E.md` lines 145-150 and 180 are exact. Checked independently: `e^{2b\cos ψ}=Σ_k(k+1)b^{-1}I_{k+1}(2b)χ_{k/2}`. |
| 68 | Definition of `G_b` (330) | CORRECT | Four-tested inside L-FPW (section 4). |
| 69 | Theorem 5.2, FP with `G_b` under R-IA is the isotropic Wilson measure (332-339) | CORRECT | Re-derived: `c_k(w_b)=I_{k+1}(2b)/I_1(2b)=e^{-γ_k(b)}`; `λτ=1`, `-λθ/2=b/4`; each spatial plaquette gets `e^{\frac b2{\rm Tr}}` from two neighbouring kernels; the temporal factor is `w_b` at an argument conjugate to `W^{-1}`, and `{\rm Tr}W^{-1}={\rm Tr}W` on SU(2). The constant `(b/I_1(2b))^{\#\text{temporal plaquettes}}` drops out on normalization. |
| 70 | Creutz paragraph, finite-register remark (341) | CORRECT | `GB1.md` line 11: "at fixed `s` its lifts are signed for small `a₀`". The Creutz citation is context only. |
| 71 | Corollary 5.3(a) (343) | CORRECT | `lg1.md` line 365 (Theorem 10): "Every periodic Wilson DLR state at \(\beta>0\) is invariant and reflection positive at every admissible mirror". `ro1.md` line 64 states H-L for "Every periodic state used". Volume-first weak limits of the torus Wilson laws are periodic DLR states. `t0-tree.md` line 166: "No assertion of diagonal RP for a straight torus." |
| 72 | Corollary 5.3(b), two-point isotropy through O4-2 (343) | INCOMPLETE | The quote of `o4-two-point.md` line 188 is exact, and so is "proved as implications, with named outstanding items" (same line). Missing: (i) O4-2 has five inputs, not two: A = CA (iii-b), B = CA (iv), C = LG1 Theorem 10 (frozen), D = CL1 Lemmas 1-3, 5, 7, 8 at degree `≤1` with A in place of I3 (refereed conditional, one reading), E = unchanged RO1 text (frozen conditional) (`o4-two-point.md` lines 69-75). (ii) The standing hypotheses: "\(N=2\); CA's hypotheses for clauses (iii) and (iv)", `ϑ_*=1/12000`, `g≤γ_W^{\mathbb T}(ϑ_*)` (line 49). (iii) The class `𝔙`: `β_j=(g_0^{(j)})^{-2}`, cutoffs `K_j`, weak limit points of "the periodically lifted Wilson laws on \(\mathbb T_m\) at cutoff \(K_j\)", and CA's smeared action density (lines 51-56). So `b` must equal, at each `j`, the coefficient of `{\rm Tr}U_P` in CA's Wilson weight at `β_j` (convention of CA-I L128, not read here), and `N=N_t` must be the side of `𝕋_m` in lattice units. (iv) Nonemptiness of `𝔙` "has the same conditional standing as their first-passage construction" (line 201). With these named, the conclusion follows: by Theorem 5.2 the FP-`G_b` lifts are those torus Wilson laws. Edit E7. |
| 73 | Corollary 5.3(c) and proof (343-345) | CORRECT | |
| 74 | §5.4 table (349-354) | CORRECT | Row 1 carries the GAP (2) correction. Row 2 quote of `GB1E.md` line 180 is exact. |
| 75 | "What the YM side can accept" (356) | CORRECT | The `\log k_t` variant is recorded, not proved; the angle must be matched so that the two half-weights give `k_t(X_p)`. |
| 76 | "No counterexample to ISO-FP is claimed" (358) | CORRECT | A paraphrase of `GB1ISO.md` line 111, correctly not quoted. |
| 77 | §6 test definitions (362) | CORRECT | |
| 78 | L-FP (364) | CORRECT | Follows from Theorem 3.2. |
| 79 | L-FPW, text and grades (366-375) | CORRECT | Grades F P F F agreed in section 4. |
| 80 | R-COV_s text (377) | INCOMPLETE | "Exact covariance is required of the limit \(s\to\infty\)" does not say which limit: no common algebra or topology is named. See §2.4 and section 4. |
| 81 | GAP: admission of FP to R-COV_s (379) | CORRECT | The GAP is real. Referee closure §2.4 proves the finite-`s` estimate with `C_R` independent of `s`, volume and `g` (Proposition R3), and the limit clause under the specification LIM-s (Proposition R3′). |
| 82 | R-COV_s grades (381-388) | ERROR | Test 2 is graded P ("the limit \(s\to\infty\)" is "fixed"), but the limit notion is unspecified, so a later part can choose it: C. Edit E8. Tests 1, 3, 4 agreed. |
| 83 | "What no text here does" (390) | CORRECT | |
| 84 | §7 prior results and verification limits (393-399) | CORRECT | Update: the YM files were checked in this pass (header of this subsection). |

### 1d. Section 0 of `LW2M.md`

| # | Item (`LW2M.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | Status paragraph (5) | CORRECT | Lemma U and Proposition C are in `GA1_5.md` §8 (line 199 onward), marked unrefereed at line 201. |
| 2 | "Proved, subject to cited inputs" (7) | CORRECT | Subject to edits E5 (FS-1 clause in closure form) and E7 (O4-2 import list). |
| 3 | GAP list (9) | CORRECT | Each GAP is ruled on in section 3. |
| 4 | Open list (11) | INCOMPLETE | \"volume-uniform local register bounds and the register-limit identification\" is now closed for covariance (§2.4); keep only the volume-uniform full-sum bound (FP-FS-LOC, section 6). LW2M-WORD keeps its name, narrowed by §2.3. |
| 5 | Provenance (13) | CORRECT | `LW2M_DRAFT.md` lines 13-14 record `0ec9a2b3…` and `8d48cdf80b…`. SHA-256 prefix of the draft read here: `f11d35a648da7a24`, matching line 13. |
| 6 | Definitions preamble (17) | CORRECT | Editorial: the file has no section 2 (sections run 1, 3, 4). Edit E9. |

**Counts.** 87 numbered rows (items 1-84 and 57a-57c); row 12 points to row 58. Of the 86 graded rows: 75 CORRECT, 2 ERROR (items 34, 82), 9 INCOMPLETE (items 4, 10, 35, 38, 52, 57c, 58, 72, 80). No ERROR changes a theorem. The only INCOMPLETE item inside a theorem is item 52 (Theorem 4.5, FS-1 clause), closed by §2.1.

---

## 2. Referee closures

Each closure is a complete argument for a step the pass-2 text leaves open. They are unrefereed.

### 2.1 No family of disjoint-gate layers meets FS-1 (closes the FS-1 clause of Theorem 4.5)

**Proposition R1.** On `L5-U[m]` (any `m`) and `L5-O[S_+]`, let `θ↦W_B(θ)`, `θ` in an open interval `J∋0`, be any family of magnetic layers each of which is a member of `𝒟`. Supports, generators, the number of sublayers and the angles may depend on `θ` in any way. Then FS-1 fails. More precisely, there is a local `A` with `W_B(θ)^*AW_B(θ)=A` for all `θ∈J` and `[Σ_pB_p,A]≠0`.

*Proof.* *Step 1 (end charges).* `LW1_5.md` line 99 (`L5-U`): "\(\mathcal G_x^T=c_x^\dagger T c_x+\sum_{\ell\ni x}r_{\ell,x}^\dagger T r_{\ell,x}\)". Line 92 (`L5-O`): "\(\mathcal G_x^{cd}=M_x^{cd}+\sum_{\ell\ni x}L^{cd}_{\ell,x}\)". So each local gauge generator has the form `𝒢_v=M_v+Σ_{ℓ∋v}L_{ℓ,v}`, with `M_v` on the matter of `v` and `L_{ℓ,v}` on the register of `ℓ`. Put `q_v=Σ_{\text{even }ℓ∋v}L_{ℓ,v}`. On `L5-U` take `T=1`; then `L_{ℓ,v}=p_{ℓ,v}`, the end number, and `q_v` is the charge `q_v^e` of `GA1_5.md` line 77. On `L5-O` take one pair `c≠d`.

*Step 2 (every member of `𝒟` fixes `q_v`).* Let `h` be a link-only gauge-invariant operator on a member `X` of a cell-invariant family of pairwise disjoint finite link sets. `h` commutes with `𝒢_v` (gauge invariance), with `M_v` (`LW1_5.md` line 42: "Links commute with matter"), and with `L_{ℓ,v}` for `ℓ∉X` (other tensor factors). So `h` commutes with `Σ_{ℓ∈X∩{\rm star}(v)}L_{ℓ,v}`. By `GA1_5.md` Theorem 2.2 (line 77), `X∩{\rm star}(v)` is empty, one link, the even triple or the odd triple. In each case `q_v` is a sum of operators that commute with `h`. So `[h,q_v]=0`. This is the proof of the last sentence of `GA1_5.md` Theorem 2.2, read for every generator component. Every gate `e^{-iφ_Xh_X}` fixes `q_v`, so `W_B(θ)^*q_vW_B(θ)=q_v` for every `θ∈J`.

*Step 3 (`[Σ_pB_p,q_v]≠0`).* Let `p` be a mixed plaquette with corner `v`. Its links at `v` are an even link `ℓ_e` and an odd link `ℓ_o` (proof of Theorem 4.5). For a plaquette `p'∋v` with links `ℓ_1,ℓ_2` at `v`, the argument of Step 2 gives `[B_{p'},L_{ℓ_1,v}+L_{ℓ_2,v}]=0`. If `ℓ_1,ℓ_2` have equal parity, `[B_{p'},q_v]=0`. If `p'` is mixed with even link `ℓ_1`, then `[B_{p'},q_v]=[B_{p'},L_{ℓ_1,v}]`, supported on `∂p'`. By Lemma 1.3(e) its `∂p`-component vanishes unless `∂p⊆∂p'`, that is `p'=p`. So `([Σ_{p'}B_{p'},q_v])_{∂p}=([B_p,L_{ℓ_e,v}])_{∂p}`.

On `L5-U`, let `v` be the `x`-end of `ℓ_e` (the other case exchanges signs). Summing Lemma 1.6(b) over `c`: `[U^{ab},p_x]=-U^{ab}` and `[(U^†)^{ab},p_x]=(U^†)^{ab}`. All entries of `W(∂p)` on `ℓ_e` have one type, fixed by the traversal direction, and those of `W(∂p)^†` the other. So `[B_p,p_{ℓ_e,v}]=±(W(∂p)-W(∂p)^†)`. Every factor is traceless on its link, so the operator is its own `∂p`-component. Pair it with `⊗_{ℓ∈∂p}t_ℓ^†`, where the `t_ℓ` are the four entries of one term of `W(∂p)`. By the trace facts in the proof of Lemma 1.6, exactly that term survives and every `W(∂p)^†` term vanishes. The pairing is `±κ_m^4≠0`.

On `L5-O`, `B_p=2W(∂p)`. `LW1_5.md` line 137: "The local transformations implement \(SO(10)\) on site algebras and a representation of \(\operatorname{Spin}(10)\) on site and link-end state spaces", and every hop and cube gate commutes with every `𝒢_x^{cd}`. So `L^{cd}_{ℓ,v}` rotates the `v`-end index of each link entry in the `(c,d)`-plane and fixes the other index. In the normalization `L^{cd}=iη_cη_d/2` on the `v`-end generators, `[iη^y_aη^x_c,iη^x_cη^x_d/2]=i\,(iη^y_aη^x_d)`. Any nonzero normalization gives the same conclusion. Choose the corner indices of `p` with index `c` at `v`. Pair `[W(∂p),L^{cd}_{ℓ_e,v}]` with targets whose entry on `ℓ_e` has index `d` at `v`, whose entry on `ℓ_o` has index `c` at `v`, and whose other two entries are fixed by the other corner indices. Only the term with original index `c` on `ℓ_e` survives; the terms that start from index `d` end at index `c` on `ℓ_e` and are killed. The pairing is a nonzero multiple of `512^4`.

*Step 4.* `q_v` is local. FS-1 would give `q_v=q_v+iθ[Σ_pB_p,q_v]+O(θ^2)`, so `[Σ_pB_p,q_v]=0`. This contradicts Step 3. □

The same charge gives a second proof of the FS-sum clause: every written sum `Σφ_Xh_X` commutes with `q_v`, and `θΣ_pB_p` does not for `θ≠0`. Proposition R1 uses only `GA1_5.md` Theorem 2.2 and gauge invariance. It says nothing about overlapping commuting supports.

### 2.2 Repaired statement of Theorem 4.5

"**Theorem 4.5.** On `L5-U[m]` (any `m`) and `L5-O[S_+]`: (a) for every member of `𝒟` and every choice of angles, the written sum `Σ_sΣ_{X∈ℱ_s}φ_Xh_X` has zero `∂p`-component for every mixed plaquette `p`, so no written sum meets FS-sum at `θ≠0`; (b) no one-parameter family of members of `𝒟` meets FS-1 (Proposition R1 of `LW2M_REFEREE.md`)." The fixed-support, fixed-generator clause of Definition 4 is then unnecessary.

### 2.3 The cell-averaged product at third order (narrows LW2M-WORD)

Let `σ=(σ_1,…,σ_6)` list the six orders of `\{1,2,3\}`. Let `w_σ` be the word whose letters, in the order in which their derivations appear in `β_w` (§4.3), are the blocks `(0,σ_k(1),σ_k(2),σ_k(3))`, `k=1,…,6`, every letter with `c=1/6`. All `C_v=1`, so `w_σ` meets FS-sum with `θ=2φ`. Its order matrix is invariant (`LW2M.md` line 274). Put `ε^{(k)}_{uv}=+1` if `u` precedes `v` in block `k`, else `-1`, and
\[
(A_σ,B_σ,C_σ)=\sum_{k=1}^6(2k-7)\big(ε^{(k)}_{12},\,ε^{(k)}_{13},\,ε^{(k)}_{23}\big).
\]

**Proposition R2.** On `L5-U[m]` (any `m`) and `L5-O[S_+]`, if `(A_σ,B_σ,C_σ)` is not a multiple of `(1,-1,1)`, there is a closed discrete set of `φ` outside which `w_σ` is not cell covariant. For the lexicographic sequence `(123,132,213,231,312,321)`, `(A,B,C)=(-10,-18,-10)`.

*Proof.* *Block logarithms.* By BCH to second order (the commutator part of the expansion in Theorem 3.2), block `k` has logarithm `Y_k=X+Q_k+R_k+O(φ^4)`. Here `X=\frac{iφ}6Σ_vD_v`, `Q_k=\frac12(\frac{iφ}6)^2Σ_{u<v}ε^{(k)}_{uv}[D_u,D_v]`, and `R_k` is cubic. *Six blocks.* Iterating the two-factor formula of Lemma 4.4.1's proof gives `\log(e^{Y_1}⋯e^{Y_6})=Σ_kY_k+\frac12Σ_{j<k}[Y_j,Y_k]+T+O(φ^4)`. Every term of `T` is a bracket of three `Y`'s, so at order three it is a bracket of three copies of `X` and vanishes. The cubic part is therefore `Σ_kR_k+\frac12Σ_k(2k-7)[X,Q_k]`. *Relabelling.* For `π` of `\{1,2,3\}`, `πw_σ` has the blocks `πσ_k` in the same positions. `Σ_kQ_k` and `Σ_kR_k` depend only on the set `\{σ_k\}=S_3`, which `π` permutes, so they agree. Hence
\[
\log β_{w_σ}-\log β_{πw_σ}=\tfrac14\big(\tfrac{iφ}6\big)^3\Big[\textstyle\sum_wD_w,\sum_{u<v}E^π_{uv}[D_u,D_v]\Big]+O(φ^4),\qquad E^π_{uv}=\sum_k(2k-7)\big(ε^{(k)}_{uv}-ε^{(πσ_k)}_{uv}\big),
\]
and the automorphisms differ by the same cubic derivation plus `O(φ^4)`. *Row component.* On the row `p,q,r` of Theorem 4.4 (`(1,2)`-plane, `y_1≢y_2`), the `S`-coefficient of `[H_w,[H_u,H_v]]` is `2a_ws(u,v)` and `Σ_wa_w=2`. So the cubic defect has `S`-coefficient `4Σ_{u<v}E^π_{uv}s(u,v)=-4(E^π_{13}+E^π_{23})`. Here `E^π_{0v}=0` because `0` is first in every block, `s(1,2)=0` and `s(1,3)=s(2,3)=-1`. Using `ε^{(πσ)}_{uv}=ε^{(σ)}_{π^{-1}u,π^{-1}v}`: for `π=(13)`, `E_{13}+E_{23}=2B+A+C`; for `π=(23)`, `E_{13}+E_{23}=B-A+2C`. Both vanish iff `(A,B,C)∈R(1,-1,1)`. Otherwise `Y_S≠0` (Lemma 1.6(a)), and Lemma 1.4 gives `A'` with a nonzero cubic defect. The defect is then a nonzero entire function of `φ`. Both transpositions are realized by cell rotations (Lemma 1.2), and the base tick is covariant. For the lexicographic sequence: `2B+A+C=-56`. □

[check] `/tmp/toe-LW2Mref/check_blocks.py`, run with `python3 -I` at 51 percent free memory, under one second, a few MB. Of the 720 sequences, 24 have `(A,B,C)∈R(1,-1,1)` and none has `(A,B,C)=0`. It reproduces the lexicographic `(-10,-18,-10)` and `2B+A+C=-56`. A guide only; the proposition is proved for each sequence by the displayed hand computation.

### 2.4 FP and R-COV_s on the SU(2) family (closes the finite-`s` estimate of GAP (3))

**Proposition R3.** On `L5[SU(2),s]` with FP at angle `θ` (any order), let `A` be supported in a ball `b` of graph radius `R`, and let `P_R` be the number of plaquettes on faces of cubes meeting the concentric ball of radius `R+12`. Then for every `g∈𝒢`, every even box with `N≥2R+28`, and in infinite volume,
\[
\|α_g(α(α_g^{-1}(A)))-α(A)\|\le 36\cdot2^{20}\,θ^2P_R\,\|A\|/s .
\]
The constant is independent of `s`, the volume and `g`.

*Proof.* A cube has graph diameter `3`. So under any word in the four letters, each letter enlarges the support by at most `3`, and every cube that acts lies in the set `Ω` of cubes meeting the ball of radius `R+12`. Let `u_Ω` be the word with each letter restricted to its cubes in `Ω`. Then `u^*Au=u_Ω^*Au_Ω`. Proof by induction from the innermost letter: a cube of the current letter that misses the current support commutes with the current operator and with the other cubes of its letter (disjoint links). So it can be dropped, or added. By Lemma 1.2 and `α_g(B_C)=B_{gC}` on `R_s` (`GB1QL.md` Proposition 4.11(b),(c)), `α_g(β_θ(α_g^{-1}A))=u'^*Au'`, with `u'` the relabelled word. Both words restrict to the same `Ω`. So the difference is at most `2‖A‖‖u'_Ω-u_Ω‖`. Two orders of four letters differ by at most six adjacent transpositions. Each transposition costs at most `‖[φH^Ω_u,φH^Ω_v]‖` (`GB1.md` line 58, applied twice). And `‖[H^Ω_u,H^Ω_v]‖≤12P_R2^{20}/s` by the bound of Proposition 4.6(b). With `φ=θ/2` this gives the display for `β_θ`. The base tick is covariant (`GB1QL.md` Proposition 4.11(c)), so the bound passes to `α=α_0∘β_θ`. □

**The limit clause.** The R-COV_s text says "Exact covariance is required of the limit \(s\to\infty\)" but names no common space or topology. One specification, proposed here and not adopted:

> **LIM-s.** On a finite box, embed `R_s=⊕_{k≤s}H_k⊂L^2(SU(2))` on every link. The register limit of updates `U_s` is `U_∞` if `Ũ_s→U_∞` strongly on `𝓜⊗⊗_ℓL^2(SU(2))`, where `𝓜` is the unchanged matter space and `Ũ_s` is `U_s` on `𝓜⊗⊗_ℓR_s` and the identity on its orthogonal complement.

Four tests: (1) P, it names no part's target; (2) P, the embedding and topology are fixed; (3) P, it settles no physics question; (4) P, a limit clause needs a common space and a topology, and nothing else is added.

**Proposition R3′.** Under LIM-s, the FP update of `L5[SU(2),s]` has register limit the infinite-register update, whose magnetic layer is `e^{-iθH_B}`. That limit is exactly cell covariant.

*Proof.* For `h∈H_k` and `s>k`, `P^{(s)}_μh=y_kx^+_μh+y_{k-1}x^-_μh` (`GB1QL.md` line 57), and `y_k\to1` as `s\to∞` (line 56). So `P^{(s)}_μh\to x_μh` (line 55: "`x_μ h = x^+_μ h + x^-_μ h` on `S³`"). Each `B^{(s)}_p` maps flux at most `j` per link to flux at most `j+1` and converges on finite-flux vectors. `‖B^{(s)}_p‖\le 2^{11}` uniformly in `s`, since `|t_p|\le2` and `‖P_μ‖\le1`. So the exponential series converges uniformly in `s`, and `e^{-iφB^{(s)}_C}\to e^{-iφB^{(∞)}_C}` on finite-flux vectors. Uniformly bounded operators that converge on a dense set converge strongly. Extend each gate by the identity off `𝓜⊗⊗_ℓR_s`; the product of the extended gates is `Ũ_s`. Strong limits of products of uniformly bounded operators are products of the limits. The base layers converge the same way: `E^2` acts identically on each `H_k`, `k\le s`, and the hops are linear in the `P_μ`. The limit magnetic layer is `e^{-iθH_B}` (`GB1ISO.md` Theorem 6.1), which `α_g` fixes. □

So GAP (3) is closed: Proposition R3 proves the estimate, and R3′ proves the limit clause under LIM-s. If the owner adopts R-COV_s with a different limit notion, the second half must be rechecked.

---

## 3. The distiller's GAPs

| GAP (`LW2M.md` line 9) | Real? | Ruling |
|---|---|---|
| (1) Theorem 4.5, FS-1 | Real | The draft (`LW2M_DRAFT.md` line 288) says "no member of `𝒟` meets FS-sum or FS-1 at any `θ≠0`". It argues only from the written sum at one angle, but FS-1 concerns the derivative of a family. The distiller's restriction to fixed supports and generators is still not enough (item 52): with sublayers that are not scalars at `θ=0`, the derivative is `Σ_sV_s^*G_sV_s`. **Closed** by Proposition R1 (§2.1), which needs nothing beyond membership in `𝒟`. Repaired statement: §2.2. |
| (2) "every route must pass through T0-start^an" | Real | Draft line 391: "Any route must then pass through the anisotropic request T0-start^an". A fixed-lattice failure of H-L excludes only routes that need exact exchange symmetry or diagonal reflection positivity at fixed spacing. The distilled row (line 351) states the correct, weaker claim. Nothing more to repair. |
| (3) FP and R-COV_s | Real | Draft line 419 gives the right idea (a bounded causal region and letter swaps) without a common region, uniformity or a limit notion. **Closed**: Proposition R3 (§2.4) proves the estimate with `C_R` independent of `s`, volume and `g`; Proposition R3′ proves the limit clause under the proposed specification LIM-s. |
| (4) YM inputs not checked | Real for pass 2 | Checked here at YM head `85d76598f`: every quoted line exists at its cited number. The application is a conditional implication whose hypotheses are listed in item 72 (edit E7). This makes Corollary 5.3(b) exact as a conditional; it closes no part of T0. |
| (5) N1-N8 landing packet | Real as a process item | It is not a gap in any proof and is outside this report. |

## 4. Four-test grades

The tests: a text fails if it (1) states or fixes a part's target, (2) is open-ended so a part can add to it, (3) settles a downstream physics question by premise, or (4) adds structure or constants its own reasons do not need.

| Text | Pass-2 grades | Referee grades | Reason |
|---|---|---|---|
| FS-ex (§4.1) | P P P P | P P P P | It is a reading of GB1-CF's own phrase and is used as the question: Theorem 4.2 refutes it, so it fixes no answer as a premise. |
| FS-sum (§4.1) | P P C P | P P C P | Test 3 C is inherited from R-SUM (`GB1_GEN_OWNER_CHECK.md` line 77). |
| FS-1 (§4.1) | P P P P | P P P P | |
| L-FP (§6) | C P P P (pass 1, `GB1ISO.md` line 165) | unchanged | The grades judge the text. The law is inadmissible on both live laws by Theorem 3.2. |
| L-FPW with `G_b` (§6) | F P F F | F P F F | Agreed. Theorem 5.2 shows that by construction the R-IA lift is T0's Wilson measure (tests 1 and 3). The Bessel ratios have no reason except the match (test 4). The `\log k_t` variant has the same grades. |
| R-COV_s (§6) | P P C F | P C C F | Test 2: "the limit \(s\to\infty\)" names no space or topology, so a later part can choose one; with LIM-s attached it is P. Test 3: if adopted it decides GB1-CF's admissibility question for register families by changing the rule (Propositions R3, R3′ show FP then passes). Test 4 F agreed. |
| LIM-s (this report, §2.4) | none | P P P P | It fixes the embedding and the topology a limit clause needs, and nothing else. |

ISO-FP[W] (Corollary 5.3) is the name of a statement, not a law text, so it has no grade. Definition 4's FS-1 family clause is a scope condition and is superseded by Proposition R1.

## 5. Required edits to `LW2M.md`

| Edit | Where | Change |
|---|---|---|
| E1 | Lemma 1.3(d), line 66 | Write `tr(X·⊗_{ℓ∈S}Z_ℓ)`: a product, not a tensor product. |
| E2 | Remark (1) after Theorem 3.2, line 144 | Replace "for any `φ_0`" by "for `φ_0=λφ`, any fixed real `λ`". |
| E3 | Line 142 | Replace the unfound quote by `LW1_5.md` line 268, "The base \(L5\)-U tick is covariant under the cell group", and line 18, "the two specified dressed ticks have cell-covariant lifts (§7)". |
| E4 | Line 167 | "FS-sum implies FS-1 for every word in exponentials of the `K_k` whose exponents are linear in `θ`." |
| E5 | Definition 4, Theorem 4.5, §4.8 verdict, §0 GAP (1) | Replace the FS-1 clause by the statement in §2.2 of this report, cite Proposition R1, drop the fixed-support, fixed-generator restriction, and mark GAP (1) closed by the referee. |
| E6 | §4.7, line 274 | Add Proposition R2 to the proved cases. The uncovered words become: Suzuki's `S_4` and higher Suzuki orders, the cell-averaged products whose block sequences have `(A,B,C)∈R(1,-1,1)` (24 of 720 by [check]), and other words with an invariant order matrix. |
| E7 | Definition 6; Corollary 5.3(b); line 343 first sentence; line 397 | List O4-2's five inputs with their standing, its standing hypotheses, the class `𝔙`, the identification of `b` with CA's Wilson coefficient at `β_j`, `N=N_t` equal to the side of `𝕋_m`, and the conditional nonemptiness of `𝔙` (item 72). Replace "their source texts were not independently checked in this pass" with this report's check record (YM head `85d76598f`). |
| E8 | §6, R-COV_s; §0 open list | Test 2 becomes C (P if LIM-s is attached). Replace the GAP paragraph (line 379) by Propositions R3 and R3′. In §0 replace "volume-uniform local register bounds and the register-limit identification" by FP-FS-LOC. |
| E9 | Editorial | Number the sections consecutively (there is no section 2). In §1.2 write "two families, each of pairwise site-disjoint cubes". |

## 6. Open statements to carry, by name

- **LW2M-WORD**, narrowed by Proposition R2. Its three failed attacks (lines 276-278) stand as recorded.
- **GB1-CF for general NN-a circuits**, including sublayers with overlapping commuting supports (`GA1_5.md` line 89).
- **ISO-FP** under R-SUM and R-IA with `E^2` (`GB1ISO.md` line 167).
- **ISO-FP[W] remainder**: NT1-NT2, higher points (H-U), T0-rate; and, beneath Corollary 5.3(b), the outstanding items of CA (iii-b) and CA (iv) on the YM branch.
- **T0-start^an** with Y-a to Y-d; **Y2**; **Y3**.
- **R-SUM-`G_b`**: existence of the exact R-SUM lift for `G_b`.
- **The exceptional sets** `Θ`, `Θ_X`, `Θ_w`, `Θ_s`: their structure.
- **FP-FS-LOC**: a volume-uniform local bound for FP's full-sum defect on `R_s`. It needs a light-cone bound for `e^{-iθH_N}`. The covariance defect needs none (Proposition R3).

## 7. Freeze recommendation

**Freeze `LW2M.md` after edits E1-E9.** No theorem of `LW2M.md` is false. The two ERRORs are a misquotation (item 34) and one grade (item 82). The one INCOMPLETE proof step inside a theorem (Theorem 4.5, FS-1) is closed by Proposition R1 in a stronger form. Propositions R1, R2, R3, R3′ and the specification LIM-s should enter as "referee closures, unrefereed", as `GA1_5.md` §8 does. R-COV_s and LIM-s are proposals for the owner; nothing here adopts them.

---

## Prior work used

Ported with credit, not re-derived beyond the checks named in section 1:

- `GA1_5.md` Theorem 2.2 (line 77) and its parity-split-charge sentence: the classification of star intersections. Used in Proposition R1, extended from `L5-U` end numbers to every generator component, so it also covers `L5-O`. Listed in `prior/LW2M.md`.
- `GA1_5.md` §8, Lemma U (line 236) and Proposition C (lines 262-270): the compilation behind Theorem 3.1.
- `GB1ISO.md` Theorems 2.1, 2.4 (line 62) and 6.1 (line 161); `GB1ISO_REFEREE.md` lines 116-120: tilings, temporal-gauge window formula, infinite-register FP.
- `GB1E.md` Theorem 3.2 (lines 76-78), Theorem 7.1 (lines 145-150), Theorem 7.2's analyticity step (line 158), lines 29-37 and 180: the exact lift, Wilson multipliers and transfer-kernel lifts behind Theorems 5.1 and 5.2.
- `GB1QL.md` lines 55-58, Proposition 4.2 (lines 139-146), Proposition 4.11 (line 299): the family `R_s`, used in Lemma 1.6(c), Proposition 4.6 and Propositions R3, R3′.
- `GB1.md` line 58 (Theorem 2.2): the product-formula bound used in Proposition 4.6 and Proposition R3.
- `LW1.md` line 38 (tilings, `c_0`) and E1 (line 401); `LW1_5.md` lines 18, 42, 89-99, 137, 268 and 323: the laws, their gauge generators, tick covariance, cube-gate compilation.
- `GB1_GEN_OWNER_CHECK.md` lines 27 and 77: R-SUM and its test-3 grade.
- YM branch at `85d76598f`, `library/`: `o4-two-point.md` lines 49-75, 188, 201 (Theorem O4-2 and its inputs); `lg1.md` line 365 (Theorem 10); `ro1.md` line 64 (H-L); `t0-tree.md` line 166.

Prior work the digest missed: `GB1E_REFEREE.md` line 143 ("The diagonal mirror `x_1 ↔ t` is the exchange `ς` itself"); `GB1.md` line 11 (finite-register lifts "are signed for small `a₀`"); `LW1_5.md` line 137 (`Spin(10)` on link ends, needed for the `L5-O` half of Proposition R1).

---

## FINISH

**Proved.** Confirmed in `LW2M.md` on re-derivation: Lemma 1.2 (the cell group realizes every permutation of the three shifted tilings); Lemma 1.6 (nonzero top components of pinned chain commutators on both live laws and on `R_s`); Theorem 3.1 (FP compiles into even nearest-neighbour gates of depth `8d` and is gauge invariant, conditional on `GA1_5.md` §8); Theorem 3.2 (FP not cell covariant outside a closed discrete set of `θ`, every order); Theorem 4.2 (the exact full sum has no bounded-depth circuit outside a countable set); Theorems 4.3, 4.4 and 4.5(a); Proposition 4.6; Theorem 5.1; Theorem 5.2; Corollary 5.3 as a conditional implication with the O4-2 hypotheses of item 72. New referee closures (unrefereed): Proposition R1 (no family of members of `𝒟` meets FS-1, on both laws); Proposition R2 (the cell-averaged product fails cell covariance at third order whenever `(A,B,C)∉R(1,-1,1)`, for example in lexicographic block order); Proposition R3 (FP meets R-COV_s's finite-`s` estimate on the SU(2) family, with constant independent of `s`, volume and `g`); Proposition R3′ (its register limit, under LIM-s, is the exactly covariant infinite-register update).

**Counterexamples.** None to a stated theorem. One to a proof step: with a constant non-scalar sublayer `V`, the family `V^{-1}W(θ)V` has first-order generator `V^*KV`, so "the derivative is the sum of coefficient derivatives times the generators" (line 250) fails in general.

**Open by name.** LW2M-WORD (narrowed); GB1-CF for general NN-a circuits and overlapping commuting supports; ISO-FP with `E^2`; ISO-FP[W] remainder (NT1-NT2, H-U, T0-rate; CA (iii-b), CA (iv) outstanding items); T0-start^an, Y-a to Y-d, Y2, Y3; R-SUM-`G_b`; the exceptional sets; FP-FS-LOC.

**What changes downstream.** GB1-CF: the disjoint-gate class `𝒟` is excluded under FS-1 for every family, not only fixed-generator ones. LW2M-WORD loses one of its two named uncovered words, except for 24 block orders. GB1QL and LW2-G: if the owner adopts R-COV_s with LIM-s, FP is admissible on the SU(2) register family with error `O(θ^2/s)` per fixed ball. ISO-FP and T0: Corollary 5.3(b) now carries O4-2's exact hypotheses. Freeze `LW2M.md` after E1-E9.
