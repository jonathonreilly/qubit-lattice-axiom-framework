lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# ZM1-I1[a] referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max reasoning), as pass 3 (referee) under PR #10138's method. This session wrote neither pass 1 (`ZM1I1A_DRAFT.md`, Claude) nor pass 2 (`ZM1I1A.md`, Codex gpt-6.1-terra). This is one check: one whole-part, line-by-line read. It reviews no other review. It grants no status and adopts nothing; only the owner adopts.

**Text refereed.** `ZM1I1A.md` at commit `e5ad408dd` (branch `claude/toe-assembly`, head `e5ad408dd`). SHA-256 of the file read: `b6ca39f144ceb2b72e320672a1b49fe418b39eaaa959d0191a25416c1d1fdc5e`. Line numbers below refer to that file.

**Sources read, with commits.** `ZM1I1A_DRAFT.md` (last changed `f7933913b`); `ZM1.md` (last changed `36d5dd136`); further sources are listed in the section "Sources and prior work used" below as they are read.

**Working set used, by name.** PS-1c (through (Z-b) of Definition Z), PS-5 and PS-6r (through the five-mode laws of `LW1_5.md`). Owner decision ZM1-I1[a] (`TOE_ASSEMBLY.md` §3.8) is the text under test. No axiom, working-set entry or owner decision is changed.

**Method.** Every proof was re-derived by hand. A `[check]` is a small scratch computation in `/tmp/toe-ZM1I1Aref/`; it guides and proves nothing. Verdicts: CORRECT; ERROR (a false line, quoted, with the fix); INCOMPLETE (a named missing step). A "referee closure" (RC) is a short complete argument for a missing or reading-dependent step; RC-1 to RC-6 are in section 3.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". Definitions Z and G and the owner text of `TOE_ASSEMBLY.md` §3.8 are read plainly.

---

## 1. Verdict table

### 1A. Head, definitions, and the trace obstruction (lines 1-70)

| # | Item (ZM1I1A line) | Verdict | Note |
|---|---|---|---|
| 1 | Title (1) | CORRECT | |
| 2 | Status (3) | CORRECT | The obstruction uses no state and no update, so it holds for every vacuum and update. Exact hypotheses: section 4. |
| 3 | GAP summary (5) | CORRECT | Each GAP is assessed in section 2. The "reading question" it names is settled by RC-1. |
| 4 | Open (7) | CORRECT | |
| 5 | Provenance (9) | CORRECT | The referee checked with git: `31ef08a1e` and `59d3886d9` are commits of this repository. |
| 6 | Def. 1, fine and coarse systems (13) | CORRECT | `LW1_5.md` line 97 reads "\mathcal G_x^T=c_x^\dagger T c_x+\sum_{\ell\ni x}r_{\ell,x}^\dagger T r_{\ell,x}". Thus `Q_x=\mathcal G^1_x` exactly, with no constant shift. The draft cites line 96 (the display opens there). |
| 7 | Def. 2, coarse indexing and coarse-link assignment (14) | CORRECT | The assignment is not an added reading under (Z-b). By RC-1, any placement of coarse links in the coarse site algebras allowed by Definition Z, together with (Z-a) and (Z-b), gives the uniform bound that Theorem 3 needs. ZM1-I1[a] retains (Z-b). |
| 8 | Def. 3, R-form, four tests P P P P (15) | CORRECT | The four tests agree with draft §3.3. Extra coarse summands that do not enter the coarse Gauss generators change nothing, factors or not (RC-2). |
| 9 | Def. 4, `Cov_τ`, dark pair, finite range (16) | CORRECT | With `X=1` (empty support), darkness gives `ω(α^n(Y))=ω(Y)` for invariant `Y`. So truncated values of dark pairs vanish without a separate invariance hypothesis. |
| 10 | Def. 5, G1-eq (17) | CORRECT | Same as the draft §7.2 display. |
| 11 | Pointers (19) | CORRECT | §3.8 is `TOE_ASSEMBLY.md` lines 239-245. Definitions Z and G are `ZM1.md` lines 49-77. |
| 12 | Theorem 1, statement (23-28) | CORRECT | |
| 13 | Theorem 1 proof, trace transfer (30) | CORRECT | One step is implicit: `τ∘Φ` is a tracial state because `Φ` is a unital *-homomorphism. Draft Lemma T1(c) states it. |
| 14 | Theorem 1 proof, covariances (32-36) | CORRECT | Re-derived: `5(m/10)(1-m/10)=m(10-m)/20` and `20(m(m-1)/90-m²/100)=-m(10-m)/45`. Their sum is `m(10-m)/36`. This is the hypergeometric variance `m·½·½·(10-m)/9`. |
| 15 | Theorem 2 and proof (38-40) | CORRECT | |
| 16 | Theorem 3, statement (42) | CORRECT | The statement should name "(G1) at `T=1`" and (Z-a) explicitly. "Under the locality assignment in §1" carries (Z-a). |
| 17 | Theorem 3 proof, bounded displacement (44) | CORRECT | The fine star difference is `5+6\min(m,10-m)≥11`, using the fine `m`. The coarse norms `‖p_{ℓ,X}‖=\min(m_1,5)≤5` give the factor 35. Equality of the two basis states on the approximant is the standard fact that a CAR basis-vector state, restricted to a region, depends only on that region's occupations. |
| 18 | Theorem 3 proof, bijection and count (46) | CORRECT | Injective, edge-preserving, degree 6 on both sides: the image is closed under adjacency, hence all of `Z³`. The count gives `L³N³≤(N+2c)³`. |
| 19 | Remark after Theorem 3 (48) | CORRECT | "does not use (Z-b)" holds under the §1 assignment. Under RC-1, (Z-b) replaces that assignment. The Z0-indexing sentence is right: there the count gives `8L³≤1`, false for every `L≥1`. |
| 20 | Theorem 4, statement (50) | CORRECT | |
| 21 | Theorem 4 proof (52-56) | CORRECT | Internal links have zero-variance end sums. Each of the six extremal boundary edges is distinct. `Z³` is bipartite, so three sites span at most two edges. For two sites the parity argument is right. `[check]` C1 agrees (section 3). |
| 22 | Theorem 5, statement (58) | CORRECT | |
| 23 | Theorem 5 proof (60) | CORRECT | `e^{iH}=ζ·1`, so `u_x=ζ^{N_x}∏ζ^{p_{ℓ,x}}`. The shared link gives `E[ζ^{p}ζ^{m_1-p}]=ζ^{m_1}`, hence `μ²κ^{10}(ζ^{m_1}-κ²)`. Exact real parts, with `cos72°=(√5-1)/4` and `cos144°=-(√5+1)/4`: `120\,\mathrm{Re}\,κ_3=-(70+10√5)/4`, `210\,\mathrm{Re}\,κ_4=-(185+95√5)/4`, `252\,\mathrm{Re}\,κ_5=-(242+150√5)/4`. All are negative. `κ_m=\overline{κ_{10-m}}` because `P_m(p)=P_{10-m}(5-p)` and `ζ^5=1`. |
| 24 | Theorem 6, statement (64) | CORRECT | |
| 25 | Theorem 6 proof, adjacency (66) | CORRECT | `S_+` is the even total-rishon sector. `LW1_5.md` line 141 reads "On \(S_+\), the product of the ten commuting \(2T_{2j-1,2j}\) is chirality \(+1\)", and `∏(2n_j-1)=(-1)^{N_{tot}}`. The sums give `χ_e=-4e^{-5πi/4}`, `χ_o=-4ie^{-5πi/4}` and `(χ_e-χ_o)²=16(-i)(-2i)=-32`. Nonvanishing does not depend on the convention: the odd sector gives `+1/32`, and reversing one end's generator gives `+1/32`. |
| 26 | Theorem 6 proof, displacement (68) | CORRECT | `\mathcal G^{12}` on the star has spectrum `{-7/2,…,7/2}`. Both extremes occur in `S_+` after a parity fix at the far end of each link. |
| 27 | Remark on the O analogue (70) | CORRECT | |

### 1B. First tests, general form, GAPs, boundaries and readings (lines 72-122)

| # | Item (ZM1I1A line) | Verdict | Note |
|---|---|---|---|
| 28 | Theorem 7, statement (74) | CORRECT | Under R-form it is vacuous for `L≥2` (Theorem 3). It matters only under a changed reading. |
| 29 | Theorem 7 proof (76) | CORRECT | For `1≤r≤r_*`: `|F_0^T-F_1^T|≤2M(r,t)≤2r_*^pr^{-p}M(r,t)`, because `M(r,t)` includes `β` itself. Darkness gives zero truncated values (item 9). The draft's constant is `r_*=2R_0+2⌈r_Φ/L⌉+3`. |
| 30 | Theorem 8, statement (78) | CORRECT | |
| 31 | Theorem 8 proof (80) | CORRECT | `GA1_5.md` line 150 states Theorem 6.1 (R) for D1 states with `ω(N_x)=0`. The conservation step can be written out. An invariant `X` commutes with `Σ_{z∈Λ}Q_z=N_Λ+m·I(Λ)+Σ_{\rm boundary}p_{ℓ,z}`. Choose `Λ` so that every link of `\mathrm{supp}\,X` is internal. Then `X` commutes with `N_Λ`, so it preserves the empty and the full sector. |
| 32 | Witness paragraph (82) | CORRECT | `VC1_5.md` Theorem 5.2 uses "the normalized trace on each link"; Theorem 5.5 puts end numbers `(k,k)` on every link, where `W_E` is scalar. Both meet Theorem 8's hypotheses. The Lemma ER sentence is right: if `ε(r)<1` and `M(r,t)>0`, then both `m_i(r)>0`. |
| 33 | Theorem 9, statement (84) | CORRECT | It extends to every nonzero cell translation, not only translations along `e_1` (RC-5). |
| 34 | Theorem 9 proof (86) | CORRECT | `VC1_5.md` R2 proof (1) reads "`W_E` is a function of the `p_{ℓ,src}`, which commute with the link densities". Proof (2) reads "In each `ψ_s` every `P_i` is sharp, at `1` if `s_1 = +1` and at `0` if `s_1 = −1`". `P` is invariant because end numbers commute with the Gauss generators (`LW1_5.md` line 145). |
| 35 | Lemma ER paragraph (88) | CORRECT | In the power form with `η=0`, Lemma ER forces `η_1=0` and `a_1=1/4` on a channel that contains `P`. |
| 36 | Theorem 10, statement (92) | ERROR (wording) | "connected degree-six cubic graphs": a cubic graph is 3-regular. Fix: "the simple cubic lattice `Z³` (every vertex of degree six), on both sides". The mathematics is right once the wording is fixed. |
| 37 | Theorem 10 proof (94) | CORRECT | Bounded displacement is a hypothesis here. RC-3 derives it. |
| 38 | GAP G (96) | CORRECT | The gap is real for the draft's Theorem G as stated. RC-3 gives the repaired theorem and the `L_cube` instance. |
| 39 | GAP swap-band inference (98) | CORRECT | The gap is real. RC-4 gives the repaired statement: an asymptotic ballistic channel under a stated hypothesis, not an exact glider. The unit remark is a caution, not an error: one fine cell per fine tick is one coarse cell per coarse tick. |
| 40 | GAP two-band inference (100) | CORRECT | The gap is real. `ZM1_OBS.md` Theorems 8 and 9 assume summable correlations, band forms and weights (lines 102, 106). The draft checks none of these for an image of a map. |
| 41 | GAP scope of R2′ (102) | CORRECT | The gap is real only as proof coverage. At `β=0`, `ψ_s(P^2)=ψ_s(P)` gives `1/4` as well. |
| 42 | §6 boundaries (106) | CORRECT | Relative commutant, verified: with `W=e^{-iθ\mathcal G_x}Φ(e^{iθ\mathcal G^{(1)}_X})`, (G1-eq) gives `WΦ(A)W^*=Φ(A)`. |
| 43 | §6 prior results (108) | CORRECT | The descriptions match the digest (`prior/ZM1I1A.md` lines 23-35). |
| 44 | §6 literature (110) | CORRECT | Pass 2 did not check the example. The referee checked it against Brothier-Stottmeister's own definition (RC-6). It holds for every finite group, abelian or not. |
| 45 | §7 opening (114) | CORRECT | |
| 46 | R-G1EQ, P P C P, and G1-EQ (116) | CORRECT | Section 5 confirms the tests. A useful restatement: (G1-eq) for all `θ` holds exactly when `Φ(\mathcal G^{(1),T}_X)-\mathcal G^T_{x_X}∈Φ(𝔄_1)'∩𝔄` for every `T` (section 5). |
| 47 | R-ISO, C C C C (117) | CORRECT | As written, test 2 is met only after the subspace rule is supplied. "C" must be read as "fails until then". |
| 48 | R-MEAS, P C C C (118) | CORRECT | |
| 49 | "Dropping (Z-a)…" paragraph (120) | CORRECT | Pass 2 rightly weakened the draft's "a relabelling of the fine law". Adjacency and injectivity give a bijection of site sets. They give no statement about the map or the dynamics. |
| 50 | Inherited open items (122) | ERROR | "GA1-5-Φ and GA1-5-O" is out of date. `GA1_5.md` Amendment 2 (line 9) reads "the open item GA1-5-Φ is answered yes in the proposed R-Φ reading for those m" (`m=2,…,8`). The remaining name is "R1-check (referee closure for m=1,9)". Fix: replace "GA1-5-Φ" by "R1-check (GA1-5-Φ at `m=1,9`)". The draft did not list GA1-5-Φ as open. |

**Counts.** 50 items: 48 CORRECT, 2 ERROR, 0 INCOMPLETE. Neither ERROR changes the content of a theorem. All 27 items on lines 1-70 are CORRECT; they include every step of Theorems 1-6.

---

## 2. The distiller's GAPs

Pass 2 marks five gaps: one in the status block (line 5) and four in §5 (lines 96-102). Each is assessed below. Repairs are in section 3.

**GAP (line 5), "applicability of the inferred coarse-link assignment to Definition Z".** Not a gap for ZM1-I1[a]. Definition Z says the coarse site algebras include the coarse links ("one per coarse site, coarse links included where present", `ZM1.md` line 52). It does not say which site holds which link. RC-1 proves that (Z-a) and (Z-b) fix the needed bound for every placement. The owner text of §3.8 retains (Z-b) ("Retain … (Z-a), (Z-b), (G1), (G2), and singleton embedding sets"). So Theorem 3 holds under Definition Z as written. No reading of the assignment is needed.

**GAP G (line 96).** Real, for the draft's Theorem G as stated. The draft says "Let a law have finite-dimensional link registers, a compact local gauge group acting on the star of each site by local unitaries, and a coarse law of the same type". It names no lattice, no algebra shape and no step for bounded displacement. Theorem 10 of pass 2 states sufficient hypotheses, and it assumes bounded displacement. RC-3 removes that assumption: trace-correlation itself gives a non-scalar star generator, and translation covariance makes its spectral gap uniform. RC-3 also settles the `L_cube` clause from `LW1.md` line 55, "\mathcal G_x=n_x+\sum_{\ell\text{ out of }x}E_\ell-\sum_{\ell\text{ into }x}E_\ell", and line 49, "E_\ell|m\rangle=m|m\rangle" with `m=-S,…,S` (line 47). The draft's covariance `−S(S+1)/3` is right.

**GAP swap-band inference (line 98).** Real. The draft writes "at `r = t` the bound asks the coarse value at that `β` to equal the fine one up to `2C_{R_0}t^{−2}` times the envelope: an exact coarse glider". The bound gives agreement up to `2C_{R_0}t^{-2}M(t,t)`, not equality. And "a nonzero component along `u_0`" does not control the fine truncated value at the moving point: other spectral components of `Φ(A)Ω` add to it. RC-4 states what does follow, under an explicit hypothesis on the fine values.

**GAP two-band inference (line 100).** Real. `ZM1_OBS.md` Theorem 8 assumes "`Σ_β|C_i(β,0)|<∞`" and a band form with weights. Theorem 9 assumes "`p>0`, `Σ_β‖C_i(β,0)‖<∞`" and a branch form. The draft verifies none of these for the image data of a map. It also does not show that the `LZ1I.md` bands lie in such an image. The repaired statement is only the conditional one: if the image data meet the hypotheses of Theorem 8′ or 9′, those theorems apply. Under R-form no map exists (Theorem 3), so nothing further is owed here.

**GAP scope of R2′ (line 102).** Real as proof coverage only. The draft's claim "for every separation" is true: at `β=0`, `P^2=P` gives the same value `1/4`. Class (a) uses `r≥1` only. RC-5 also extends Theorem 9 from translations along `e_1` to every nonzero cell translation.

---

## 3. Referee closures and check

Each closure uses only finite-dimensional linear algebra and the hypotheses named. None uses a computation.

**RC-1 (coarse links are localized by (Z-a) and (Z-b)).** *Statement.* Let `Φ` be a block map of Definition Z: a unital injective graded *-homomorphism with (Z-a), constants `C, ξ`, and (Z-b). Let the coarse algebra be `L5-U[m_1]` or `L5-O[S_+]` on the coarse lattice of `ZM1.md` §1.1. Let each coarse link factor lie in some coarse site algebra, placed in any way. Then there is `K`, depending on `C, ξ, L`, with this property. For every coarse link `ℓ`, every `B` in its factor and every `R`, `Φ(B)` lies within `Ce^{-R/ξ}‖B‖` of an element supported within `R+K` of `β_{u(ℓ)}`. Here `u(ℓ)` is the cell of the lower endpoint of `ℓ`. So Theorem 3's proof runs with `K` in place of the §1 assignment.

*Step 1 (near-scalar lemma).* Let `A∈𝔄` be even. Let `R_1, R_2` be finite sets of fine factors with no common factor, and `A_i∈𝔄(R_i)` with `‖A-A_i‖≤ε`. Then `‖A-c‖≤3ε` for some scalar `c`. Proof. The parity automorphism preserves each `𝔄(R_i)` and fixes `A`, so we may replace `A_i` by its even part. Work in a finite region containing `R_1∪R_2`. There `𝔄(R_2)` is a full matrix algebra (Theorem 1). Let `E` be the trace-preserving conditional expectation onto `𝔄(R_2)`: the partial trace over its relative commutant. It has norm one and is an `𝔄(R_2)`-bimodule map. The even `A_1` commutes with `𝔄(R_2)`. So `bE(A_1)=E(bA_1)=E(A_1b)=E(A_1)b` for every `b∈𝔄(R_2)`. Thus `E(A_1)` is central in a full matrix algebra, a scalar `c`. Then `‖A_2-c‖=‖E(A_2-A_1)‖≤2ε` and `‖A-c‖≤3ε`. □

*Step 2.* Let `B` be even and self-adjoint in one coarse factor (link factors are even; on matter take, for example, a multiple of `N_X-5/2`), with `τ_1(B)=0` and `‖B‖=1`. A traceless self-adjoint matrix of norm one has eigenvalues of both signs, or `0` and `±1`, so `‖B-c‖≥1/2` for every scalar `c`. `Φ` is injective, hence isometric, and graded, so `Φ(B)` is even and `‖Φ(B)-c‖≥1/2`.

*Step 3.* Fix `R_0` with `3Ce^{-R_0/ξ}<1/2`. Let `c(ℓ)` be the cell of the site that holds `ℓ`. Let `b` be a coarse cell translation and `g` its lift from (Z-b). The lift acts on supports by a lattice isometry `σ_g`; the allowed global phase or parity is on-site and keeps supports. Apply (Z-a) to `B` and to `g_1(B)`, which lies in the factor of `ℓ+b`. Then `Φ(g_1B)=g(Φ(B))` is close to the algebras of both `σ_gN_{R_0}(β_{c(ℓ)})` and `N_{R_0}(β_{c(ℓ+b)})`. By Steps 1-2 these two regions share a factor. The same argument for a traceless coarse matter element in cell `c(ℓ)` shows that `σ_gN_{R_0}(β_{c(ℓ)})` meets `N_{R_0}(β_{c(ℓ)+b})`. Hence `|c(ℓ+b)-c(ℓ)-b|_∞≤K_1`, with `K_1` depending only on `R_0` and `L`. There are 24 orbits of coarse links under coarse cell translations. Choose one link `ℓ_0` of each orbit with lower endpoint in cell `0`. Then `|c(ℓ)-u(ℓ)|_∞≤K_1+\max_{ℓ_0}|c(ℓ_0)|_∞` for every `ℓ`. Put `K=2L(K_1+\max_{ℓ_0}|c(ℓ_0)|_∞+1)`. □

RC-1 uses (Z-b), injectivity and grading. Remark T.3 of the draft lists these three as unused, which is true only under the §1 assignment. All three are part of Definition Z, and §3.8 retains them.

**RC-2 (other coarse factors).** Suppose each coarse site algebra is `B^U_X⊗E_X`. Here `B^U_X` is the `L5-U[m_1]` site-and-link content, and `E_X` is any finite-dimensional C*-algebra, a factor or not. Suppose the coarse Gauss generators lie in `B^U_X⊗1`. Let `𝔅` be the unital C*-subalgebra generated by the `B^U_X`. Then `τ∘Φ` restricted to `𝔅` is a tracial state of `𝔅`. `𝔅` is a limit of full matrix algebras, so this state is `𝔅`'s normalized trace. Every quantity in Theorems 1-6 lies in `𝔅`, so their conclusions stand.

**RC-3 (Theorem G repaired; `L_cube`).** *Statement (G′).* Let the fine and the coarse law each have sites `Z³` with nearest-neighbour links, a CAR algebra of `n_0≥1` modes per site, a full matrix algebra `End(V)` per link, and translation-covariant Gauss generators `\mathcal G^T_x`, linear in `T`, each a sum of one-factor terms on the star of `x`. Use the coarse lattice of `ZM1.md` §1.1. Suppose that for some `T_0` the coarse `u_X=\exp(i\mathcal G^{(1),T_0}_X)` has nonzero trace on each star factor, and that its two end actions on a coarse link have nonzero trace covariance. Let `Φ` be a block map (Definition Z with (Z-a), (Z-b)) with (G1) at `T_0` on pairwise disjoint singletons. Then `L=1`.

*Proof.* Trace transfer is Theorem 1's argument. Coarse neighbours: the covariance of `u_X,u_Y` is the product of the unshared traces times the link covariance, which is nonzero. Fine sites that are distinct and not neighbours: the covariance is zero. Disjointness excludes equal representatives. So representatives of neighbours are neighbours. Bounded displacement: `\mathcal G^{(1),T_0}_X` is not a scalar, because a scalar has zero covariance with everything. `Φ` is injective, so `\mathcal G^{T_0}_{x_X}=Φ(\mathcal G^{(1),T_0}_X)` is not a scalar either. By translation covariance its spectral spread `δ>0` on the star is the same at every site. It is even, so extreme eigenvectors can be taken of definite parity. Tensor each with one fixed even product state off the star. The two states agree off the star and differ by `δ` on `\mathcal G^{T_0}_{x_X}`. Now run Theorem 3's proof, with RC-1 for the coarse links. □

*`L_cube`.* `LW1.md` lines 47-55 give spin-`S` links with `E_ℓ|m⟩=m|m⟩`, `m=-S,…,S`, and `\mathcal G_x=n_x+\sum_{\rm out}E_\ell-\sum_{\rm in}E_\ell`. Under the trace `E_ℓ` is uniform on `{-S,…,S}`. So neighbouring Gauss charges have covariance `\mathrm{Cov}(E,-E)=-S(S+1)/3`, and distinct non-neighbours have zero covariance. The linear form of Theorems 1-3 applies. A block map from coarse `L_cube` (spin `S_1≥1/2`) with (Z-a), (Z-b) and (G1) on disjoint singletons forces `L=1` and `S_1=S`.

**RC-4 (swap band, repaired).** *Statement.* Suppose a block map and a coarse pair satisfy class (a) with constant `C_{R_0}` and `p=2`. Suppose invariant coarse `A,B` (norm at most one, radius `R_0`) and coarse vectors `β_t` with `|β_t|_∞=t` satisfy `|F_0^T(A^*,τ_{β_t}B;t)|≥c>0` for all `t≥1`. Then `|F_1^T(A^*,τ_{β_t}B;t)|≥c-4C_{R_0}t^{-2}`. *Proof.* At `r=t` the budget is `C_{R_0}(t^{-2}+t·t^{-3})M=2C_{R_0}t^{-2}M`, and `M≤2` because every truncated value of norm-one elements is at most 2. □ So for `t≥(8C_{R_0}/c)^{1/2}` the coarse law has a truncated invariant correlation of size at least `c/2` at coarse distance `t` after `t` coarse ticks. The hypothesis holds, for example, if `Φ(A)=Φ(B)=A_0` of `GA1_5.md` Theorem 6.3, with `c=1` by orthonormality of the `u_b`. Whether any map has such images is not shown. Exactness at finite `t` does not follow.

**RC-5 (Theorem 9 for all translations).** In each `ψ_s`, every projection `Π[p_{ℓ',src}=a]` on a link `ℓ'` along `e_1` is sharp, with value `[s_1=+1]` (`VC1_5.md` R2, proof (2)). For any nonzero cell translation `β`, `τ_βP` is such a projection on a different link. So Theorem 9's proof applies unchanged and gives `1/4`. At `β=0`, `P^2=P` gives `ω(Pα^n(P))=1/2` and again `1/4`.

**RC-6 (the Brothier-Stottmeister refinement).** The ar5iv text of arXiv:1901.04940, §2.1, defines (as returned by the fetch tool; the referee did not read the PDF) "R:M→M⊗M,R(b)=Ad(u)(b⊗id) where uξ(g,h):=ξ(gh,h)". It also states "R(a)=a∘μ_G, R(b)=b⊗id for any a∈C(G), b∈CG¯", with "μ_G is the group multiplication of G". The map and its eq. (2.2) are theirs. The computation below is the referee's; for abelian `G` it agrees with the draft. Take `G` finite, so `M=B(L^2(G))=M_{|G|}`. From the definition: `R(M_a)=M_{a(gh)}`, `R(λ_k)=λ_k⊗1`, and `R(ρ_b)ξ(g,h)=ξ(ghbh^{-1},h)`. Put coarse vertices `v_j` on a chain. Split each coarse link into `(v_j,w_j)`, with variable `g`, and `(w_j,v_{j+1})`, with variable `h`. Let a gauge element act by left translation on links that start at its vertex and by right translation on links that end there. Then:
(a) At the start of a link, `R(λ_k)=λ_k⊗1` is the fine transformation at `v_j`.
(b) At the end of a link, `Ad(1⊗ρ_b)(M_{a(gh)})=M_{a(ghb)}=R(\mathrm{Ad}(ρ_b)M_a)`, and both sides fix `λ_k⊗1`. Multiplications and left translations generate `M`, so `\mathrm{Ad}(1⊗ρ_b)∘R=R∘\mathrm{Ad}(ρ_b)`. But `R(ρ_b)≠1⊗ρ_b` for `b≠e`: one moves `g`, the other moves `h`.
(c) At a midpoint `w_j`, the map `ξ(g,h)↦ξ(gs,s^{-1}h)` fixes `a(gh)` and commutes with `λ_k⊗1`.
So the link-wise map on the chain is unital, injective, of finite range and translation covariant. It has (G1-eq) at coarse vertices, (G2) at midpoints and disjoint singletons, and it fails (G1). This holds for every finite `G`, abelian or not. The fetch tool reports that the paper's §2.5 states consistency of the gauge action across levels and calls the refinement "equivariant w.r.t. the gauge group action", but displays no identity of the form `R∘(\text{coarse gauge})=(\text{fine gauge})∘R`. So (a)-(c) are a computation, not a quotation. They are not load-bearing.

**Check C1.** `[check]` `/tmp/toe-ZM1I1Aref/check.py`, output `out.txt` (under one second, a few MB; `memory_pressure` reported 59 percent free). (1) The hypergeometric variances equal `m(10-m)/36` for `m=1,…,9`. `Re κ<0` for `m=3,…,7`, and `|μ²κ^{10}(ζ^m-κ²)|∈[3.1·10^{-4},5.0·10^{-3}]`. (2) In a `4³` box, `|∂S|∈{6}`, `{10,12}`, `{14,16,18}` for `|S|=1,2,3`. No `|S|∈{2,3}` solves `45(|S|-1)=6k_1-k|∂S|`. (3) Enumerating 512 `S_+` states gives `τ(g⊗1)=0.1767767=2^{-5/2}` and covariance `-0.03125`. (4) The uniform variance on `{-S,…,S}` equals `S(S+1)/3` for `S=1/2,…,3`. The check guides only.

---

## 4. Decision on the trace obstruction (Theorems T, T′, O; Propositions V, Z5)

**Verdict.** The obstruction is correct. Theorems 1-6 of `ZM1I1A.md` (draft Theorem T, Lemma T5, Theorem T′, Corollary T″, Propositions V and Z5, Lemma O1, Theorem O, Corollary O″) were re-derived step by step, and every step holds.

**Consolidated statement (all steps verified above).** Let the fine law be `L5-U[m]` for any `m∈{1,…,9}`, or `L5-O[S_+]`. Let the update and the state be arbitrary. Let the coarse system be the same construction on the coarse lattice of `ZM1.md` §1.1: `L5-U[m_1]` for any `m_1∈{1,…,9}`, or `End(S_+)` links for O. It may be tensored with further finite-dimensional algebras that do not enter the coarse Gauss generators (RC-2). Let `Φ:𝔄_1→𝔄` be a unital *-homomorphism. Assume:
1. (G1) on pairwise disjoint singleton sets, for at least one of these generator sets: `T=1` on U; all traceless `T` on U; the five Cartan generators on O;
2. (Z-a);
3. either the coarse-link assignment of `ZM1I1A.md` §1 item 2, or (Z-b) with `Φ` injective and graded (RC-1).

Then `L=1`.

**Exact reading of Definition Z used.**
- *Coarse algebra.* R-form is the only reading the result needs. It reads §3.8's "a coarse law \(\alpha_1\) of the stated form" with Definition G's "Let the coarse law be of the same type" (`ZM1.md` line 70). The value of `m_1` is free. Extra coarse tensor factors that do not enter the coarse Gauss generators are harmless (RC-2). For another finite coarse link register with trace-correlated ends, RC-3 gives the same conclusion.
- *Coarse-link assignment.* No reading is needed. Definition Z requires a "unital injective graded *-homomorphism" with (Z-a) and (Z-b) (`ZM1.md` lines 53-55), and RC-1 derives the bound from these. The coarse site of `(u,r)` is read as having block `β_u`, the block of its cell; this is the only block indexing `ZM1.md` §1.1 provides. Under the Z0 indexing (one coarse site per block of side `2L`) the count gives `8L³≤1`, false for every `L≥1`.
- *Embedding sets.* §3.8 requires singleton sets. Definition G requires "nonempty, pairwise disjoint finite sets" (`ZM1.md` line 70). On U, Theorem 4 shows that (G1) at `T=1` with any nonempty finite sets forces singletons. On O no analogue of Theorem 4 is proved; §3.8 does not need one.
- *The generator set.* Definition G asks (G1) "for every coarse site `u` and every `T`". On U the frame group is "exactly \(U(5)\)" (`LW1_5.md` line 143), so `T=1` is included. Theorem 5 shows that the traceless part already suffices.

**Not used.** No vacuum, no update, no coarse dynamics, no coarse state, no comparison class and no `p`. With the §1 assignment, (G2), (Z-b), injectivity and grading are not used either. So the conclusion holds for every VC1 vacuum (the witnesses of `VC1_5.md` included), for every admissible update (base tick, any GA1-P-5 member, any NN-a update), for every `m`, and on `L5-O[S_+]`.

**What it decides.** The owner text ZM1-I1[a] (§3.8), read with Definitions Z and G and R-form, has no instance for `L≥2` on either five-mode law. The same holds for every `p`, for each class of `ZM1_OBS.md` §5, and for the original ZM1-I1 of `ZM1.md` line 363: all retain the map conditions. The named failing step is (G1) at a coarse link whose two representatives are not fine neighbours. (Z-a) and `L≥2` force such a link. The cause is (G1) together with (Z-a) and the fixed-form coarse algebra; class (a) and `p=2` play no part. §3.8's line "It is not shown impossible or trivial" no longer holds under R-form.

**What it does not decide.** Maps with (G1-eq) in place of (G1); non-unital isometries; measure-level maps; infinite group-valued registers. Under (G1-eq) the trace still transfers, but `Φ(Q^{(1)}_X)` may differ from `Q_{x_X}` by an element of the relative commutant, so Theorem 2 has no fine side to compare. RC-6 gives a one-dimensional pure-gauge map with (G1-eq), (G2), finite range and distant representatives. So (G1-eq) alone does not force adjacency.

---

## 5. The three readings and the Brothier-Stottmeister claim

The four tests: a reading fails if it (1) states or fixes a part's target, (2) is open-ended so a part can add to it, (3) settles a downstream physics question by premise, or (4) adds structure or constants its own reasons do not need. The verdicts below review pass 1's tests. They adopt nothing.

**R-G1EQ (P P C P): tested correctly.**
- *Equivalent form (proof).* (G1-eq) for all `θ` holds exactly when `D^T_X:=Φ(\mathcal G^{(1),T}_X)-\mathcal G^T_{x_X}` lies in `Φ(𝔄_1)'∩𝔄` for every `T`. Forward: differentiate at `θ=0`; this gives `[D^T_X,Φ(A)]=0`. Backward: `X(θ)=\mathrm{Ad}(e^{iθ\mathcal G^T_{x_X}})Φ(A)` and `Y(θ)=Φ(\mathrm{Ad}(e^{iθ\mathcal G^{(1),T}_X})A)` both solve `Z'=i[\mathcal G^T_{x_X},Z]` with `Z(0)=Φ(A)`. For `Y` this uses `[D^T_X,Y(θ)]=0`, since `Y(θ)∈Φ(𝔄_1)`. Bounded linear ODEs have unique solutions, so `X=Y`. □ The condition is closed (test 2).
- *Tests 1 and 4.* It is a condition on `Φ` only, and (G1) implies it. Pass.
- *Test 3.* The surviving conclusions were checked against their proofs. `ZM1_OBS.md` Theorem 3's proof uses (G1) only in "At a representative site, (G1) and Theorem 1 turn a fine gauge conjugation of `Φ(B)` into the image of the coarse conjugation", and (G1-eq) states exactly that. Theorem 2's proof uses "`Φ(g)` is the product of fine local gauge unitaries at `S_X`". Only the conjugation `Φ∘\mathrm{Ad}(g)=\mathrm{Ad}(\text{fine product})∘Φ` enters the data, so with singleton sets it survives. `ZM1.md` Lemma R-GI uses the sentence "conjugation by `e^{iθ G^1_x}` acts on `Φ(A_1)` as `Φ` of the coarse gauge transformation at `X`", which is (G1-eq). What is lost is the identification of coarse and fine Gauss charges. Charged-sector consumers (R-CS, MT1-S) would need their own bridge. This settles nothing by premise; it removes a premise that downstream parts may have used. "C" is the right flag.

**R-ISO (C C C C): tested correctly, with one sharpening.** As written ("an isometric embedding into a specified subspace"), the subspace rule is not given. So the text is open-ended now and fails test 2 until a rule is supplied; "C" must be read that way. Tests 1, 3 and 4 depend on that rule in the ways pass 1 states. The escape from the trace argument is real in general: the fine functional becomes `\mathrm{Tr}(P\,·)` with `P=VV^*`, which need not factorize. For a product `P` it might; that is not decided.

**R-MEAS (P C C C): tested correctly.** It needs a Euclidean form (Y1, open) and, for positive weights, reflection positivity for the chosen update (ST1). It adds the Euclidean structure. Measure-level maps lie outside Definition Z (`ZM1.md` line 65 and §5.3 Scope).

**Does Brothier-Stottmeister arXiv:1901.04940 satisfy R-G1EQ as claimed?** The draft makes three claims.
1. "The published refinement maps for lattice gauge fields are equivariant in this sense." Supported. The paper calls its refinement "equivariant w.r.t. the gauge group action" (introduction, as returned by the fetch tool), and RC-6 verifies the Ad-identity from the paper's own eq. (2.1).
2. "R satisfies (G1-eq) at the far end, and it does not satisfy the generator identity there" (finite abelian `G`). Correct. RC-6 proves it for every finite `G`, together with (G2) at midpoints and the exact identity at the near end.
3. "Brothier–Stottmeister's maps satisfy the analogue of (G1-eq) for group-valued links." Correct as an analogue. The setting is one dimension, pure gauge, registers `L^2(G)`, refinement factor 2.

The map does **not** satisfy R-G1EQ as a statement about `L5-U[m]` or `L5-O[S_+]`. Those laws live on `Z³` with five-mode matter and quantum-link registers `End(Λ^mC^{10})` or `End(S_+)`. So it is not an instance of G1-EQ and does not decide it. Its one use here: it shows that (G1-eq), unlike (G1), does not force adjacency of representatives in general. The draft's §8.1 sentence "Whether a finite-register analogue exists is not known to this lane" conflicts with its own §7.2 finite-`G` computation, unless "analogue" means a five-mode one. The distilled file does not carry that sentence, so no edit is needed there.

---

## 6. Required edits to `ZM1I1A.md` (for the lead; this report edits nothing)

None of these changes the content of a theorem.

1. **Line 3 (Status).** For "Under the explicit coarse-algebra and locality readings below", write "Under reading R-form below; the locality assignment follows from Definition Z (referee closure RC-1, `ZM1I1A_REFEREE.md`)".
2. **Line 5 (GAP).** Delete "The exact applicability of the inferred coarse-link assignment to Definition Z is a reading question, not an established owner decision." Add: "(Z-a) and (Z-b), with injectivity and grading, give the coarse-link localization for any placement of coarse links (referee closure RC-1)."
3. **Line 7 (Open).** At freeze, replace "No independent referee has checked this item" by a pointer to this report.
4. **Line 14 (Def. 2).** Append: "Under (Z-b), any placement allowed by Definition Z gives the same bound (referee closure RC-1)."
5. **Line 42 (Theorem 3).** State the hypotheses in full: "(Z-a), (G1) at `T=1` on disjoint singleton sets, and either the §1 assignment or (Z-b) (RC-1)".
6. **Line 48.** For "The proof does not use (Z-b), (G2), grading, dynamics, states, the envelope or `p`", write "With the §1 assignment the proof does not use (Z-b), (G2), injectivity, grading, dynamics, states, the envelope or `p`; without it, RC-1 uses (Z-b), injectivity and grading."
7. **Line 92 (Theorem 10).** For "connected degree-six cubic graphs", write "the simple cubic lattice `Z³` (every vertex of degree six) on both sides". Optionally replace the displacement hypothesis by (Z-a) and (Z-b) and cite RC-3.
8. **Line 96 (GAP G).** Add: "Repaired by referee closure RC-3, which also covers `L_cube` (`LW1.md` lines 47-55)."
9. **Line 98 (GAP swap-band).** Add RC-4 as the repaired statement: under a lower bound `c` on the fine values at the moving point, the coarse values are at least `c-4C_{R_0}t^{-2}`.
10. **Lines 84 and 102 (Theorem 9, GAP R2′).** Add: "The same value `1/4` holds for every nonzero cell translation and at `β=0` (referee closure RC-5)."
11. **Line 110.** For "the claimed finite-abelian equivariant refinement example relies on the stated conventions for the external refinement map and was not independently checked here", write "referee closure RC-6 checks the example from the paper's eq. (2.1): for every finite `G` the link-wise refinement has (G1-eq) at coarse vertices and (G2) at midpoints, and it fails (G1). It is a one-dimensional pure-gauge analogue, not an instance of G1-EQ."
12. **Line 116 (R-G1EQ).** Optional: add the equivalent form "(G1-eq) holds exactly when `Φ(\mathcal G^{(1),T}_X)-\mathcal G^T_{x_X}∈Φ(𝔄_1)'∩𝔄` for every `T`" (section 5).
13. **Line 117 (R-ISO).** Add: "As written, test 2 is met only once the subspace rule is stated."
14. **Line 122.** For "GA1-5-Φ and GA1-5-O", write "R1-check (GA1-5-Φ at `m=1,9`) and GA1-5-O" (`GA1_5.md` Amendment 2, line 9).
15. **Line 13 (optional).** Cite `LW1_5.md` line 97 for `\mathcal G^T_x`, so that `Q_x=\mathcal G^1_x` is quoted.

---

## 7. Open statements to carry by name

**No longer open as specified.** ZM1-I1[a] with `p=2`, read with Definitions Z and G and R-form, has no instance for `L≥2` on `L5-U[m]` (every `m`) or on `L5-O[S_+]` (section 4). The same holds for ZM1-I1[O] in every class of `ZM1_OBS.md` §5 and for the original ZM1-I1 (`ZM1.md` line 363). This is a proved negative under R-form, not an open item.

**Open, carried from `ZM1I1A.md`.**
- **G1-EQ.** On `L5-U[m]` or `L5-O[S_+]`, for some `L≥2`, is there a unital injective graded *-homomorphism from a coarse algebra of the same type with (Z-a), (Z-b), (G1-eq), (G2) and disjoint singleton sets? Nothing here decides it. RC-6 shows only that the trace route cannot decide it by itself: in one dimension, pure gauge, (G1-eq) maps with distant representatives exist.
- **The owner's reading of the zoom** after this result: R-G1EQ, R-ISO, R-MEAS, or another change. This is a decision, not a lemma.

**Inherited, unchanged (none worked here).** Odd-`m` ice-state tails and ICE-T; finite-`t` U and O witness tails; R-CS and MT1-S; R1-check (GA1-5-Φ at `m=1,9`) and GA1-5-O; LZ1-i[ZM1a]; Y1; ST1; ZM1-G; H-BLOCK; GA2's observable dictionary and propagated errors.

**New from this report.** None. An `L5-O` analogue of Theorem 4 (finite embedding sets) is not proved. It is not needed, because §3.8 requires singleton sets.

---

## 8. Freeze recommendation

**Freeze `ZM1I1A.md` after edits 1-14 of section 6** (edit 15 is optional). No edit changes a theorem.

- Theorems 1-6 freeze as stated. RC-1 is attached to Theorem 3 and to the displacement step of Theorem 6.
- Theorems 7-9 freeze. Under R-form they are vacuous for `L≥2`; they keep their use under any changed reading that retains class (a).
- Theorem 10 freezes with the wording fix and RC-3.
- GAP G is repaired (RC-3). GAP swap-band is repaired in the weaker form RC-4. GAP two-band stays as a conditional note. GAP R2′ is closed (RC-5). The status-line reading gap is closed (RC-1).

**Effect on the owner decision ZM1-I1[a] (`TOE_ASSEMBLY.md` §3.8).** The decision's text has no instance, for every vacuum and every update, on both five-mode laws, under one reading only: R-form, that "a coarse law \(\alpha_1\) of the stated form" has a coarse algebra of the same construction as the fine one. The cause is (G1) with (Z-a). Class (a) and `p=2` are not involved. The §3.8 sentence "It is not shown impossible or trivial" needs a dated amendment by the lead. Two owner questions follow, and this report settles neither:
1. Is R-form what §3.8 meant? If the owner meant a coarse algebra outside the same construction, RC-3 still applies to every finite register whose ends are trace-correlated.
2. Which change, if any? Of the three, R-G1EQ has the cleanest four-test profile (P P C P). It weakens (G1) and adds nothing, and the gauge-selection results it needs survive (section 5). Under it the question becomes G1-EQ. This is a fact about the tests, not a recommendation to adopt.

---

## Sources and prior work used

**Files read, with last-change commits** (branch `claude/toe-assembly`, head `e5ad408dd`; read in this checkout, no other branch needed):
- `ZM1I1A.md` (`e5ad408dd`), all 122 lines. `prior/ZM1I1A.md` (`a97593f4e`, SHA-256 prefix `ecaf9d607feaff57`, which matches the draft's record), all 106 lines.
- `ZM1I1A_DRAFT.md` (`f7933913b`, prefix `0304ab37f7ad1ed1`): lines 1-27, 76-135 and 154-381, so every theorem, the literature table, §§7-8 and FINISH.
- `ZM1.md` (`36d5dd136`): lines 24-80, 89-105 and 65, plus grep hits 311-390 (Z4, Z3, Z3′, ZM1-I1, R-GI, Attack 3).
- `ZM1_OBS.md` (`36d5dd136`): lines 56-68 (Theorems 1-3 with proofs), statement lines 102, 106, 114, 131 (Theorems 8, 9, 8′, 9′), lines 284-292 (Lemma ER).
- `TOE_ASSEMBLY.md` (`36d5dd136`): lines 239-245 (§3.8).
- `LW1_5.md` (`727ad9884`): lines 87-97, 135-147, 169, plus grep hits. `LW1.md` (`4b65c608f`): lines 40-56.
- `VC1_5.md` (`727ad9884`): lines 112-114, 124-126, 196-206. `GA1_5.md` (`913ef70a5`): lines 7-15, 150-151, 166-180. `LZ1I.md` (`7da1a4174`): line 99 and theorem heads 47-103.
- Format only: `LW1_REFEREE.md` (`5a2a0affe`) lines 1-80; `Y2W_DRAFT.md` (`92e03055c`) lines 1-20.
- Outside the repo, not load-bearing: the ar5iv text of arXiv:1901.04940 (Brothier-Stottmeister), through two fetch-tool calls that return extracted quotes. The referee did not read the PDF.

**Working set used, by name.** PS-1c, through Definition Z's (Z-b). PS-5 and PS-6r, through the five-mode laws of `LW1_5.md`. No axiom, working-set entry or owner decision is changed. `docs/MINIMAL_AXIOMS_2026-06-29.md` was not read and is unchanged.

**Prior results used or extended, with paths.**
- `ZM1.md` §§1.3-1.4, Definitions Z and G (lines 49-77): the hypotheses under review. §3.1, the Z0 indexing (line 91). Line 363, the precise ZM1-I1. Lemma R-GI (lines 370-372): checked to survive (G1-eq).
- `ZM1_OBS.md` Theorem 1 (exponentials), used by Theorems 5-6. Theorems 2-3: proofs checked to survive (G1-eq). Theorems 8, 9, 8′, 9′: hypotheses checked for the two-band GAP. Lemma ER: used for items 32 and 35.
- `TOE_ASSEMBLY.md` §3.8: the owner text.
- `LW1_5.md` lines 97, 141, 143, 145; `LW1.md` lines 47-55: the Gauss generators and registers that all covariances use.
- `VC1_5.md` Theorems 5.2, 5.5 and Proposition R2: extended by RC-5.
- `GA1_5.md` Theorem 6.1 (R), Theorem 6.3, Proposition S-odd and Amendment 2: used for items 31, 39 and 50, and for RC-4.
- `LZ1I.md` Theorems 6-8: GAP two-band.
- `ZM1I1A_DRAFT.md` (pass 1, Claude Opus 5.5): every theorem refereed here originates there. Its §7.2 abelian computation is extended to all finite groups by RC-6.

**Prior work the digest missed** (it bears on this target and is in this folder): `ZM1_OBS.md` Theorem 1 and the proofs of Theorems 2-3; `GA1_5.md` Theorem 6.1 (R), Theorem 6.3 and Proposition S-odd, and Amendment 2 (the status of GA1-5-Φ); `GA15PHI.md`; `VC1_5.md` Theorems 5.2, 5.5 and Proposition R2; `LZ1I.md` Theorems 6-8; `LW1_5.md` line 97 and `LW1.md` line 55 (the Gauss generators themselves); `GA2_Y2.md` Theorem 2.1 (the finite-register obstruction N, cited by the draft's §7.5). The digest's "Overlap with this lane's results" reads "not run".

**Credits.** The trace obstruction, Propositions V and Z5, the O analogue and Theorem G are pass 1's (Claude Opus 5.5, `ZM1I1A_DRAFT.md`). The distillation and its GAPs are pass 2's (Codex gpt-6.1-terra). The refinement map of RC-6 is A. Brothier and A. Stottmeister's (arXiv:1901.04940). Standard facts rebuilt in the text: uniqueness of the trace on full matrix algebras, Jordan-Wigner, conditional expectations onto full matrix subalgebras, and the hypergeometric variance.

---

## FINISH

**Proved** (by this referee; each is a finite-dimensional argument written out above).
- Theorems 1-9 of `ZM1I1A.md` are correct as stated, and Theorem 10 is correct after a wording fix. In particular the trace obstruction holds: Theorems T, T′ and O, and Propositions V and Z5.
- RC-1: (Z-a), (Z-b), injectivity and grading localize every coarse link factor near its own block, for any placement of links in the coarse site algebras. So Theorem 3 holds under Definition Z as written, with R-form as the only reading.
- RC-2: further coarse tensor factors that stay out of the Gauss generators change nothing, whether or not they are factors.
- RC-3: the general form G′ for any finite registers with trace-correlated link ends, bounded displacement included. On `L_cube` it gives `L=1` and `S_1=S`.
- RC-4: under the swap band, a lower bound `c` on the fine values at the moving point forces coarse values at least `c-4C_{R_0}t^{-2}` (not an exact glider).
- RC-5: Theorem 9's value `1/4` holds for every nonzero cell translation and at `β=0`.
- RC-6: for every finite group `G`, the link-wise Brothier-Stottmeister refinement has (G1-eq) at coarse vertices and (G2) at midpoints, and it fails (G1).
- Section 5: (G1-eq) holds exactly when `Φ(\mathcal G^{(1),T}_X)-\mathcal G^T_{x_X}∈Φ(𝔄_1)'∩𝔄` for every `T`.

**Counterexamples.**
- ZM1-I1[a] with `p=2`, read with Definitions Z and G and R-form, has no instance for `L≥2` on `L5-U[m]` (every `m`) or on `L5-O[S_+]`, for every vacuum and every update. This is pass 1's result, verified here; RC-1 removes its coarse-link reading. The same holds for every `p`, for every class of `ZM1_OBS.md` §5, and for the original ZM1-I1.
- RC-6 refutes "(G1-eq) forces adjacency of representatives" in general (one dimension, pure gauge, any finite `G≠1`).
- `ZM1I1A.md` has two small errors: line 92 ("degree-six cubic graphs") and line 122 (GA1-5-Φ listed as open).

**Open by name.** G1-EQ. The owner's reading of the zoom (R-G1EQ, R-ISO, R-MEAS or another change). Inherited and unchanged: odd-`m` ice tails and ICE-T; finite-`t` witness tails; R-CS; MT1-S; R1-check; GA1-5-O; LZ1-i[ZM1a]; Y1; ST1; ZM1-G; H-BLOCK; GA2's dictionary and propagated errors. No three-attack lemma is claimed.

**What changes downstream.**
- `ZM1I1A.md`: freeze after edits 1-14 of section 6.
- `TOE_ASSEMBLY.md` §3.8 (owner decision ZM1-I1[a]): under R-form the decision's text has no instance. The line "It is not shown impossible or trivial" needs a dated amendment by the lead. The owner decides whether R-form is meant and which change, if any, to make.
- `ZM1.md`: ZM1-I1 (line 363) is false as stated under R-form. No frozen proof changes.
- `ZM1_OBS.md`: the existence statements ZM1-I1[O] are false as stated under R-form. Its theorems and Lemma ER stand. Theorems 2-3 and `ZM1.md` Lemma R-GI survive under R-G1EQ.
- Consumers of ZM1(a)1 (GA2's operator interface, LZ1-i[ZM1a], H-BLOCK, ZM1-G): no homomorphic zoom of the specified kind supplies them. Under R-G1EQ their question becomes G1-EQ; under R-MEAS it moves to Y1 and ZM1-G.
- Not changed: `docs/MINIMAL_AXIOMS_2026-06-29.md`, the working set, every frozen part, and `ZM1I1A.md` itself.
