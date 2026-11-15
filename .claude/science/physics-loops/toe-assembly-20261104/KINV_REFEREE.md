lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# KINV referee report (pass 3)

Written 2026-11-08 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 3 (referee) of the TOE assembly under the method of open PR #10138 (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen). The Mac mini clock read 2026-11-07 19:04 EST when the lane started.

**Referee.** Claude Opus 5.5 (model id `claude-opus-5-5`), max effort, headless, Mac mini. This session wrote neither pass 1 (`KINV_DRAFT.md`) nor pass 2 (`KINV.md`). This is one check: one whole-part, line-by-line read. It reviews no other review. It edits no file other than this one.

**Text read.** `KINV.md` at commit `4ed6f62d4` (the last commit that touches it; branch `claude/toe-assembly` head). SHA-256 `f680f3f91e9ff3e07d49ac7cdbe1ddfabaaa3485c9544e2e55988f956626ad61`. Line numbers below refer to that file (105 lines).

**Source revisions read.** All files are in this folder at `4ed6f62d4`; last-change commits in brackets. No other branch was needed: every result `KINV.md` uses lives in this folder.

| File | Lines read | Use |
|---|---|---|
| `KINV.md` [`4ed6f62d4`] | 1-105, all | the text refereed |
| `KINV_DRAFT.md` [`dce446c0c`] | 1-60, 98-258, 278-302 | pass-1 source; SHA-256 `05eae300…162f91` equals the hash `KINV.md` line 13 records |
| `prior/KINV.md` | 1-92, all | prior-work digest |
| `TOE_ASSEMBLY.md` [`dd158e6a2`] | 180 (PS-1c), 243 (ZM1-I1[a], first 700 characters), 252-254 (ZM1-INV, scope, check) | owner texts |
| `ZM1.md` | 59 ((Z-b)) | the covariance being retained |
| `GB1Z2L5.md` [`3de4558ac`] | 37-53 and 75-83 in full; statement lines 33, 55, 59, 67-69, 85, 89, 111-119 | Theorems 2, 5, 6, 8 |
| `LW1_REFEREE.md`, `Y2W_DRAFT.md` | 1-80, 1-22 | file format only |

Further lines of `ZM1INV.md`, `VC1_5.md`, `ZM1INV_REFEREE.md` and the draft are listed in section 6. Of `ZM1I1A_OWNER_CHECK.md` only lines 13-16 were read, to confirm that the cited argument exists.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The owner texts ZM1-INV and PS-1c are read plainly. No hostile meaning is read into them. No reading is adopted; only the owner adopts.

**Working set used, by name.** PS-1c (cell covariance), PS-5, PS-6r and PS-7r only through the laws `L5-U[m]` and `L5-O[S_+]` of `VC1_5.md` section 2; the owner texts ZM1-I1[a] and ZM1-INV with the lead's scope note. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged and was not needed.

**Method.** Every proof was re-derived by hand. Verdicts: CORRECT; ERROR (a false line, quoted, with its fix); INCOMPLETE (a named missing step, with the step supplied where possible). A "referee closure" is a short complete argument for a missing step. A `[check]` is a scratch computation in `/tmp/toe-KINVref/`; it guides and never proves. No computation is load-bearing.

**Counts.** 39 items: 36 CORRECT, 1 ERROR, 2 INCOMPLETE. The ERROR is a wording slip in a definition. No ERROR or INCOMPLETE item changes the content of a theorem. Theorem 2 (P), Corollary 2.1 and Theorems 3, 4, 5 and 7 are correct as stated. Theorem 6 is correct once class J carries the two hypotheses of item 10.

---

## 1. Verdict table

| # | Item (`KINV.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status line (5) | CORRECT | |
| 2 | §0 "Proved" summary (7) | CORRECT | Its Theorem 5 clause omits "unital". The clause is still true: unitality is not needed (referee closure R-NGF, section 2.4). |
| 3 | §0 GAP and repair (9) | CORRECT | Both GAPs are real; both repairs are complete (section 2.5, section 3). |
| 4 | §0 Open by name (11) | INCOMPLETE | **K-INV-E** is named ("their existential version") but never defined. Insert the draft's definition (`KINV_DRAFT.md` line 229): for some even `m` or the O fine law, some even `m₁∈{2,4,6,8}` and some `L≥2`, a map with the three conditions of Definition 3 exists. |
| 5 | §0 provenance (13) | CORRECT | The four recorded SHA-256 values match the files at `4ed6f62d4` `[check: shasum]`. |
| 6 | Def. 1, laws and algebras (17) | CORRECT | Matches `VC1_5.md` section 2 as quoted in the draft. |
| 7 | Def. 2, cells and lifts (18) | CORRECT | The fine lift of a coarse rotation exists for every `L`; see section 2.1. |
| 8 | Def. 3, map conditions (19) | CORRECT | Matches (Z-b) (`ZM1.md` line 59) and PS-1c (`TOE_ASSEMBLY.md` line 180); both name the rotations. |
| 9 | Def. 4, characters and witnesses (20) | ERROR | "empty or full matter and link vacuum or full link vectors" also admits the two mixed products. `VC1_5.md` Theorem 4.2 has exactly two O witnesses: "`Φ_0` … empty matter sites and empty rishon links" and "`Φ_F` … full matter sites and full rishon links". Fix: "empty matter with empty links, or full matter with full links". A mixed product is not a character (section 2.2). No theorem uses a mixed product. |
| 10 | Def. 5, class J (21-25) | INCOMPLETE | Two hypotheses the proof uses are missing. (a) `Ψ` must be a unital `*`-homomorphism; "unital full-algebra map" does not say so. (b) `Q^F_x` must lie in the algebra of the star of `x`; "star operators" does not say so. Both are in the draft (`KINV_DRAFT.md` line 187). |
| 11 | Theorem 1, statement (29-33) | CORRECT | |
| 12 | Theorem 1, proof (35) | CORRECT | Vector-state invariance rebuilt in section 2.2. `det M=(−1)(−1)=1`, `M²=1` checked. |
| 13 | Theorem 2 (P), statement (37) | CORRECT | |
| 14 | Theorem 2, proof (39) | CORRECT | Pull-back is a character; covariance; integer spectrum. Section 2.3. |
| 15 | Corollary 2.1, statement (41) | CORRECT | |
| 16 | Corollary 2.1, proof (43) | CORRECT | Checked against `ZM1INV.md` Theorem 2.3 and R2 (section 2.3). |
| 17 | Theorem 3 (P4), statement (45) | CORRECT | `m₁/2∈P_{m₁}` for `m₁=2,4,6,8`. |
| 18 | Theorem 3, proof (47) | CORRECT | "Its lift is a composition" is loose: lifts compose only up to site matter-sign automorphisms. The proof needs only the composite of the two generator lifts; section 2.3. |
| 19 | Remark after Theorem 3 (49) | CORRECT | |
| 20 | Theorem 4 (T), statement (53) | CORRECT | |
| 21 | Theorem 4, proof (55) | CORRECT | Kernel membership uses `χ₁(p_{ℓ,X})=k=m₁/2` on the coarse locked configuration; the text gives only the reason for nonzeroness. One line; see section 2.4. |
| 22 | Attack A paragraph (57) | CORRECT | |
| 23 | Theorem 5 (NGF), statement (59-63) | CORRECT | The hypothesis "unital" can be dropped (R-NGF). |
| 24 | Theorem 5, proof (65-69) | CORRECT | `δ(1+δ)+δ=0.21<0.3`; `δ+3δ/(1−δ)=0.43<1`. |
| 25 | Corollary 5.1 (71-73) | CORRECT | |
| 26 | Attack B paragraph (75) | CORRECT | The draft's stronger claim is withdrawn correctly (section 3). |
| 27 | Theorem 6 (J), statement (77) | CORRECT | With item 10's two hypotheses. |
| 28 | Theorem 6, proof, commutation (79) | CORRECT | This is the repaired step. Section 2.5. |
| 29 | Theorem 6, proof, block and joint spectrum (81) | CORRECT | |
| 30 | Theorem 6, proof, corner and density (83) | CORRECT | `6s` uses the six links at a site of `Z³`. |
| 31 | Attack C paragraph (85) | CORRECT | `TOE_ASSEMBLY.md` line 254 calls the owner-check argument "unrefereed". |
| 32 | Theorem 7 (CF), statement (89) | CORRECT | |
| 33 | Theorem 7, proof (91) | CORRECT | `2t>m₁` for `1≤m₁≤9` `[check]`. |
| 34 | Constraint paragraph (93) | CORRECT | |
| 35 | Character and corner paragraph (95) | CORRECT | Quotes match `GB1Z2L5.md` Theorems 2, 5 and 8. |
| 36 | Existing work (99) | CORRECT | An isometry gives `Φ(1)=VV*`, unital only if `V` is unitary. |
| 37 | Literature (101) | CORRECT | Context only. |
| 38 | Readings (103) | CORRECT | `ZM1INV.md` §5 gives exactly "P, P, P, P", "C, P, F, P", "P, F, P, C". R-TR: section 4. |
| 39 | Scope of negative claims (105) | CORRECT | |

**`[check]` used above.** `/tmp/toe-KINVref/check_kinv.py`, 0.15 s, 154 MB peak, run after `memory_pressure` showed 56% free. It confirmed: `det M=1`, `M²=1`, `ρ` fixes the cell centre and swaps `X,Y`; for all 24 proper cubic rotations `R`, `(I−R)(1,1,1)∈{0,2}³`; for `m₁=1,…,9` the joint spectrum of `(Q_X,Q_Y)` at neighbours has both minima equal to `6s` but omits `(6s,6s)`, and `2t>m₁`; on `Λ^m(ℂ^{10})`, `m=1,…,9`, `‖[p_{ℓ,x},h_ℓ]‖=1` for the hop `h_ℓ` of section 2.5. Each fact is also proved by hand below. Largest space: `2^{10}`.

---

## 2. Decisions on the named items

### 2.1 Cell covariance includes the rotation `ρ`

The owner text ZM1-INV says "Retain cell covariance" (`TOE_ASSEMBLY.md` line 252). Two texts in the working set fix what "cell covariance" means, and both name the rotations.

- PS-1c (`TOE_ASSEMBLY.md` line 180): "the update is covariant under the translations of the lattice of `2 x 2 x 2` cells and under the proper cubic rotations about each cell centre".
- (Z-b) (`ZM1.md` line 59): "each coarse cell translation and each proper cubic rotation about a coarse cell centre has a fine lift in the law's symmetry group … with `Phi o g_1 = g o Phi`, up to a global phase or global parity".

The lead's scope note (line 253) lists (Z-b) among the conditions that ZM1-INV replaces. The owner's own sentence then re-imposes cell covariance on the new map. Read plainly, the retained condition is (Z-b) for `Φ:𝔄₁^G→𝔄^G`. Pass 1 of ZM1INV wrote it so ("(INV-2) cell covariance: each coarse cell translation and each proper cubic rotation about a coarse cell centre", quoted at `KINV_DRAFT.md` line 33). `ZM1INV_REFEREE.md` line 47 records that pass 2 compressed it and that nothing later used the dropped detail.

`ρ(2u+(x,y,z))=2u+(1−x,z,y)` is such a rotation. Its linear part `M` is a signed permutation matrix with `det M=(−1)·(−1)=1` and `M²=1`. It fixes `c_u=2u+(½,½,½)`. It maps the cell `2u+{0,1}³` to itself. It maps the cell `u+w` to the cell `u+(−w₁,w₃,w₂)`, so it respects the cell structure. It sends `X=2u` to `Y=2u+e₁` and back. So (Z-b) includes `ρ`. **Decision: yes, cell covariance as the owner texts define it includes `ρ`.**

The fine lift exists for every `L` when the fine block is a union of fine cells. Take the block `2Lu+{0,…,2L−1}³`, with centre `c=2Lu+(L−½)(1,1,1)`. A fine cell centre is `c'=2Lu+(½)(1,1,1)`, and `c−c'=(L−1)(1,1,1)`. For any linear part `R`, the rotation about `c'+k(1,1,1)` equals the translation by `k(I−R)(1,1,1)` after the rotation about `c'`. The entries of `(I−R)(1,1,1)` are `1∓1∈{0,2}`, so that translation is a fine cell translation. Thus the fine rotation about the block centre lies in the fine cell group `𝒢`. `VC1_5.md` Theorem 2.2 states a related fact: "The stabilizer of either cube contains all 24 rotations about its centre". Theorem 2 does not need this: its proof works for every fine lift of the specified form, whatever its geometric part. If no fine lift existed, the covariance condition would fail outright and the theorem would hold trivially.

### 2.2 The locked characters (Theorem 1)

*Pull-back of a vector state.* Let `ψ` be a vector state on a finite CAR-and-link region with every occupation number sharp. Then `ψ` is the unique state with those occupations. A lift `β` maps each mode to a phase times an image mode, so `ψ∘β` has the image occupations. If the image pattern equals the pattern, `ψ∘β=ψ`. For U with even `m=2k`, the pattern "flavours `1,…,k` at both ends of every link, matter empty (or full)" is mapped to itself by every lattice symmetry, also when ends exchange. Global phase and parity have the locked vector as an eigenvector. For `b∈𝔄^G` the gauge average fixes `b`, so `χ₀(b)=ψ(b)`. This rebuilds the proof at line 35.

*The mixed O products are not characters (item 9).* Take empty matter and full links on `L5-O`. Fix a link `ℓ=(x,y)` and flavours `j,k`. The configuration with matter `j` at `x` and `k` at `y` occupied, and the rishon modes `(x,j)` and `(y,k)` of `ℓ` emptied, has the same Cartan weights `H_{x,·}, H_{y,·}` (`VC1_5.md` line 94: `H_{x,j}=(n_{x,j}−½)+Σ_{ℓ∋x}(n^{ℓ,x}_j−½)`). It stays in `S_+`, since two link modes change. The O hop contains "`4i d^y_k d^x_j`" with matter creation (`VC1_5.md` Theorem 4.2, proof), so it maps the mixed vector to a nonzero multiple of that configuration. A vector state that is a character on `𝔄^G` makes every invariant self-adjoint `A` satisfy `ψ(A²)=ψ(A)²`, so the vector is an eigenvector of `A`. The hop moves it, so the mixed product is not a character. Theorem 2 uses one locked character only, so nothing else changes.

### 2.3 Theorem 2 (P), Corollary 2.1 and Theorem 3 (P4)

*The pull-back is a character.* Let `Φ:𝔄₁^G→𝔄^G` be a unital `*`-homomorphism and `χ₀` a character of `𝔄^G`. Then `χ₁=χ₀∘Φ` is linear, multiplicative and `*`-preserving. Also `χ₁(1)=χ₀(Φ(1))=χ₀(1)=1`, so `χ₁≠0`. Hence `χ₁` is a character. Injectivity is not used. Unitality is used: without it `χ₀(Φ(1))` could be `0` and `χ₁` the zero functional. For K-INV maps unitality is a stated condition. `GB1Z2L5.md` Theorem 6 also derives it from uniform locality: a nonzero map "is unital, even if unitality is not assumed".

*Invariance.* Covariance gives `Φ∘β¹_ρ=g∘Φ` with `g` a fine lift, possibly composed with global phase or parity. `g` maps `𝔄^G` into itself and `χ₀∘g=χ₀` there (section 2.2). So `χ₁∘β¹_ρ=χ₀∘g∘Φ=χ₁`.

*Contradiction.* The coarse lift sends `r^{ℓ,X}_j` to `r^{ℓ,Y}_j`, so `β¹_ρ(p_{ℓ,X})=p_{ℓ,Y}`. Then `χ₁(p_{ℓ,X})=χ₁(p_{ℓ,Y})`. The sum is `χ₁(m₁·1)=m₁`. So `χ₁(p_{ℓ,X})=m₁/2`. The spectral projections of `p_{ℓ,X}` are polynomials in it, so they lie in `𝔄₁^G`; `χ₁` takes each to `0` or `1` with total `1`. So `χ₁(p_{ℓ,X})∈P_{m₁}⊂ℤ`. For odd `m₁` this is false. **Decision: Theorem 2 is correct as stated, for every `L≥1`, with no injectivity and no locality.**

*Corollary 2.1.* `ZM1INV.md` Theorem 2.3 states: "Any instance of the target implies its kinematic map conditions, for every fine state and update." Its converse uses "a coarse locked witness for even `m₁`" with `VC1_5.md` Theorem 5.5 and `ZM1INV.md` Theorem 2.2. R2 does the same for the O fine witnesses. So, for a locked fine witness and its base tick: an instance gives a K-INV map with some `m₁`, which Theorem 2 forces to be even; a K-INV map with even `m₁` gives an instance through the even coarse locked witness. **Decision: the consequence holds. In locked U (even `m`) and locked O vacua with the base tick, ZM1-I1[INV] with a U coarse law holds exactly when K-INV holds for some even `m₁∈{2,4,6,8}` and some `L≥2`.** The statement is conditional on the fine state being a locked witness; it selects no VC1 vacuum.

*Theorem 3, the composite.* A link `(2u+e₁, 2u+2e₁)` between two cells has no end-exchanging rotation about a cell centre, since such a rotation maps its own cell to itself. `T_{2e₁}∘ρ` exchanges its ends `[check]`. Covariance applied twice gives `Φ∘β¹_T∘β¹_ρ=g_T∘g_ρ∘Φ`. Both fine lifts fix `χ₀` on `𝔄^G`, so `χ₀Φ` is invariant under `β¹_T∘β¹_ρ`. This composite sends `p_{ℓ,X}` to `p_{ℓ,Y}`, since each factor carries end numbers to the image ends. Site matter-sign automorphisms fix end numbers, so the choice of lift does not matter. With `m₁` even the value is `m₁/2∈P_{m₁}`, and the spectral argument gives `χ₀Φ([p_{ℓ,X}=m₁/2])=1`. The proof at line 47 says this in one sentence; it is correct.

### 2.4 Theorem 4 (T) and Theorem 5 (NGF)

*Theorem 4, kernel line.* The coarse locked configuration has flavours `1,…,k` at each end, so `χ₁(p_{ℓ,X})=k=m₁/2`. The spectral argument of Theorem 1 then gives `χ₁([p_{ℓ,X}=m₁/2])=1`, so `1−[p_{ℓ,X}=m₁/2]` is in the kernel. It is nonzero because `P_{m₁}` has at least three elements for even `m₁`. Covariance holds with every fine automorphism, since fine automorphisms fix scalars. Locality holds with zero error. So Theorem 4 is correct, for every fine law, odd fine `m` included.

**R-NGF (referee closure): Theorem 5 without unitality.** *Let `Φ:𝔄₁^G→𝔄^G` be an injective `*`-homomorphism with the uniform exponential locality of Definition 3. Let `E` be a nonzero projection in `𝔄^G` and `P∈𝔄₁^G` a local projection with `P∉{0,1}`. Then `Φ(τ_βP)E∉{0,E}` for all sufficiently distant coarse cell translates.*

*Proof.* The proof at lines 65-69 reaches `‖Φ(τ_βP)−c1‖<1` without unitality. It uses only that `Φ(τ_βP)` is a projection, so `‖Φ(τ_βP)−c‖≤1` for `c∈{0,1}`. A projection at distance below 1 from `c1` equals `c1`. If `c=0`, injectivity gives `τ_βP=0`. If `c=1`, then `Φ(1)−Φ(τ_βP)=Φ(1−τ_βP)≥0` and `Φ(1)≤1`, so `Φ(1)=1=Φ(τ_βP)`; injectivity gives `τ_βP=1`. Either way `P∈{0,1}`, a contradiction. □

So the summary at line 7 is true as written. Theorem 5 as stated is also correct; its hypothesis "unital" is harmless. The proof needs `E` only to be even; every element of `𝔄^G` is even by `GB1Z2L5.md` Theorem 6 ("Every invariant element is even under matter parity"). The product-norm step is the one in `ZM1INV.md` R6: even elements of disjoint regions act as `A⊗1` and `1⊗B` in a Jordan-Wigner order, so `‖AB‖=‖A‖‖B‖`.

### 2.5 Theorem 6 (J): the distiller's GAP in Step 1

*The draft's line.* `KINV_DRAFT.md` Theorem J, Step 1: "`[Q^F_x,Q^F_y]=0` (star generators at distinct sites commute)". Step 1 is stated for any two coarse neighbours, before Step 5 supposes that `x,y` are not neighbours.

*The GAP is real.* Class J (`KINV_DRAFT.md` line 187) allows any "self-adjoint `Q^F_x` in the algebra of the star of `x`, even, with finite spectrum, translation covariant". Here is a family that meets every clause and fails the commutation. Let `h_ℓ=r^{ℓ,−†}_1r^{ℓ,+}_1+r^{ℓ,+†}_1r^{ℓ,−}_1`, the hop of flavour 1 between the lower end `−` and the upper end `+` of `ℓ`. Put
\[
Q^F_x=p_{(x,x+e_1),x}+h_{(x-e_1,x)} .
\]
Both terms act on links in the star of `x`. Both are even link operators with finite spectrum, and the family is translation covariant. For `y=x+e₁` the stars share `ℓ=(x,y)`. The only non-commuting pair is `p_{ℓ,x}` against `h_ℓ`, and `[p_{ℓ,x},h_ℓ]=r^{ℓ,−†}_1r^{ℓ,+}_1−r^{ℓ,+†}_1r^{ℓ,−}_1`. On `Λ^m(ℂ^{10})` this is nonzero for every `1≤m≤9`: some basis vector has flavour 1 at the upper end only. Its norm is 1 `[check]`. So "star generators at distinct sites commute" is false for adjacent sites in class J. It is true for the two examples the draft names (`Q_x` on U, a Cartan generator on O), which are commuting number operators.

*The repair is complete.* `KINV.md` line 79 assumes first that `x,y` are not neighbours. Then the stars share no site and no link: a shared link would join `x` and `y`. I re-derived each step under that assumption.

1. Even operators on disjoint stars commute. Their spectral projections `[Q^F_x=a]`, `[Q^F_y=b]` act as `A⊗1`, `1⊗B`, so every product is nonzero and the joint spectrum is `σ_x×σ_y`.
2. (J) at `X` with `a=Q_X` gives `[Ψ(Q_X),Q^F_x]=0`. Then `e^{iθk_X}=e^{−iθQ^F_x}e^{iθΨ(Q_X)}`, and (J) gives `Ad(e^{iθk_X})Ψ(a)=Ψ(a)`. Differentiating, `k_X∈Ψ(𝔄₁)'`. The same holds at `Y`.
3. (J) at `Y` with `a=Q_X` (which commutes with `Q_Y`) gives `[Ψ(Q_X),Q^F_y]=0`. With step 1 this gives `[k_X,k_Y]=−[k_X,Q^F_y]=−[Ψ(Q_X),Q^F_y]+[Q^F_x,Q^F_y]=0`. So `Ψ(Q_X),Ψ(Q_Y),k_X,k_Y` commute, with finite spectra.
4. `F`, the algebra of a finite coarse region containing both stars, is a full matrix algebra; `Ψ|_F` is injective. For `0≠π∈Ψ(F)` and `0≠κ∈Ψ(F)'`: if `e₁₁κ=0` then `κ=Σ_ie_{i1}e₁₁κe_{1i}=0`; and `e_{1a}πκe_{b1}=π_{ab}e₁₁κ≠0` for a nonzero coefficient `π_{ab}`. So `πκ≠0`.
5. The products `Ψ(E_q)K_κ` are nonzero for `q∈J₁`, `κ∈K`; they are orthogonal and sum to 1. So the joint spectrum of `(Q^F_x,Q^F_y)` is `J₁−K`.
6. Both coarse minima equal `6s`, `s=max(0,m₁−5)`, but `(6s,6s)∉J₁`: on the shared link `p_{ℓ,X}=s` forces `p_{ℓ,Y}=m₁−s`, and `m₁−2s=min(m₁,10−m₁)≥1` `[check]`. The product set `σ_x×σ_y` has a least point `q*−κ*`. For each `q∈J₁`, `q−κ*` lies in it, so `q≥q*`. Then `q*` is a least point of `J₁`, which is false.
7. So `x,y` are neighbours (`x≠y` by injectivity). The class-J clause `x_{X+2b}=x_X+2Lb` and two neighbour steps give `2L≤2`.

**Decision: the GAP is real; the repaired Theorem 6 is correct; its conclusion is unchanged.** Item 10's two missing hypotheses must be restored; the proof uses both (step 2 uses multiplicativity of `Ψ`, step 1 uses star support).

### 2.6 Theorem 7 (CF)

`Q_X` generates the central `U(1)` of `U(5)_X`. Invariant elements commute with it and with its spectral projections. `Q_X` is itself invariant. So `Π_X` is a central projection of `𝔄₁^G` and `a↦Π_Xa` is a `*`-homomorphism onto the corner (not unital on `𝔄₁^G`). The maximum `5+6t` needs `N_X=5` and all six ends at `t=min(5,m₁)`. On a shared link both ends at `t` need `2t=m₁`, but `2t>m₁` for `1≤m₁≤9`. Correct.

---

## 3. The GAPs the distiller marked

`KINV.md` line 9 marks two GAPs against the draft and carries one inherited open item.

| GAP | Draft text (quoted) | Real? | Repair |
|---|---|---|---|
| **J-Step 1** | `KINV_DRAFT.md` line 197: "`[Q^F_x,Q^F_y]=0` (star generators at distinct sites commute)" | Yes. The family `Q^F_x=p_{(x,x+e₁),x}+h_{(x−e₁,x)}` of section 2.5 meets every clause of class J and has `‖[Q^F_x,Q^F_{x+e₁}]‖=1`. | `KINV.md` Theorem 6 assumes non-adjacency before it uses commutation. The repaired proof is complete (section 2.5, steps 1-7). The conclusion `L≤1` stands. Class J must keep the star-support clause (item 10). |
| **Local defects** | `KINV_DRAFT.md` line 181: "defects must be handled by a local modification of the map near each defect, never by one character on a defect projection"; line 240: "defects must be absorbed locally" | Yes. Lemma NGF proves only `Φ(τ_βP)E∉{0,E}` for distant `β`, hence no character filler. It says nothing about other actions on `E`, local or not. "A K-INV map is unital on every local sector separately" (line 181) has no definition and no proof. | `KINV.md` lines 9, 75 and 93 state only what Theorem 5 proves. Repaired statement: *for every nonzero projection `E∈𝔄^G` and every local coarse projection `P∉{0,1}`, `Φ(τ_βP)E∉{0,E}` for all sufficiently distant `β`; hence no character `χ` has `Φ(a)E=χ(a)E` for all `a`.* By R-NGF this needs injectivity and uniform locality, not unitality. |
| **GAP-GLOBAL** (inherited) | `ZM1INV.md` line 124: "Compatibility across local supports and defect sectors remains to be constructed." | Open; not a defect of `KINV.md`. | None here. Theorem 5 removes one completion mechanism only, as line 75 says. |

No other step of `KINV.md` needs a GAP mark. The two INCOMPLETE items (4 and 10) are omissions of definitions, not gaps in proofs.

---

## 4. The recorded readings

**R-TR (translations only).** `KINV.md` line 103 records it, "not proposed", with the draft's tests `P P C P`. My four-test check, on the same wording ("cell covariance" in ZM1-INV means coarse cell translations only):

1. It states or fixes no target: it removes a premise and decides nothing. **P.**
2. It is closed: one named group. **P.**
3. It settles no downstream question, but it moves one. A map covariant under translations only need not carry the cubic rotations to the coarse scale, so LZ1's rotation recovery would need another source. **C.**
4. It adds no structure or constant; it removes some. **P.**

I agree with `P P C P`. One fact the record should carry: R-TR is not a reading of an ambiguity. PS-1c, the working-set entry named "cell covariance", and (Z-b) both include the rotations (section 2.1). Adopting R-TR would change an owner-confirmed definition. Under the owner's guidance ("we can specify if needed") no specification is needed here: the plain text is clear. Theorem 2 rests on it. Under R-TR, Theorem 2 would be empty and K-INV with odd `m₁` would be open again, since R1's odd coarse character "is invariant under cell translations" (`ZM1INV.md` line 56).

**The coarse rotation composed with rishon particle-hole at `m₁=5`.** Recorded, not proposed, test 4 F. I agree: the composite fixes `p_{ℓ,X}`, so Theorem 2 gives nothing, and the extra internal map is not needed by (Z-b)'s reasons. (Z-b) names the rotation, and the coarse law's lift is the action the law supplies.

**Fine lifts that move every locked character.** Line 49 says Theorem 2 "does not decide that reading". Correct. (Z-b) asks for a lift "in the law's symmetry group (`LW1.md` A2, `MT1.md` Theorem 1)", that is, lattice symmetries with sign lifts. One further fact narrows this: a global flavour rotation is a product of local gauge transformations, so it acts trivially on `𝔄^G` and cannot move `χ₀` there. Only a non-gauge internal symmetry, such as an empty-full exchange on `L5-O`, could. Definition 2 already excludes such maps by name. No reading is adopted here.

---

## 5. Required edits

Required before freeze (all wording-level; no theorem changes):

- **E1 (line 20, item 9).** Replace "A locked O witness has empty or full matter and link vacuum or full link vectors as in `VC1_5.md` Theorem 4.2" by "A locked O witness is one of the two product states of `VC1_5.md` Theorem 4.2: empty matter with empty links, or full matter with full links."
- **E2 (lines 21-25, item 10).** Replace "A unital full-algebra map `Ψ:𝔄₁→𝔄`" by "A unital `*`-homomorphism `Ψ:𝔄₁→𝔄`", and "even finite-spectrum self-adjoint fine star operators `Q^F_x`" by "even finite-spectrum self-adjoint `Q^F_x` in the algebra of the star of `x` (matter at `x` and the links at `x`)".
- **E3 (line 11, item 4).** Define the name at first use: "**K-INV-E**: for some even `m` or the O fine law, some even `m₁∈{2,4,6,8}` and some `L≥2`, a map with the conditions of Definition 3 exists (`KINV_DRAFT.md` section 6)."

Recommended, not required:

- **R1 (line 47).** Replace "Its lift is a composition of the generators in the covariance condition" by "It is a cell translation composed with a rotation about a cell centre; covariance applied to both makes `χ₀Φ` invariant under the composite of the two coarse lifts, which carries `p_{ℓ,X}` to `p_{ℓ,Y}`."
- **R2 (line 55).** Add before the kernel sentence: "The coarse locked configuration has `p_{ℓ,X}=m₁/2`, so `χ₁([p_{ℓ,X}=m₁/2])=1`."
- **R3 (line 59 or after line 69).** Note that "unital" is not needed in Theorem 5, citing R-NGF of this report.
- **R4 (line 103).** Add: "PS-1c and (Z-b) both include the rotations, so R-TR would change a defined condition rather than read an ambiguous one."
- **R5 (line 79).** Optionally note the counterexample of section 2.5, so that a later reader does not restore the draft's general commutation claim.

---

## 6. Prior work used

All paths are in `.claude/science/physics-loops/toe-assembly-20261104/` at `4ed6f62d4`. Each result was read at the lines given and checked where `KINV.md` uses it.

| Result | Path and lines | Use here |
|---|---|---|
| Locked witnesses are characters on `𝔄^G` (Theorem 2.1) | `ZM1INV.md` 42-46 | Theorems 1, 2, 4 |
| Character pairs give class (a) for any unital `Φ` (Theorem 2.2) | `ZM1INV.md` 50-54 | Corollary 2.1 |
| Odd-`m` oriented character; translation invariant, "not reversal invariant" (R1) | `ZM1INV.md` 56-68 | line 49; R-TR (section 4) |
| Reductions to K-INV and K-INV(O) in locked vacua (Theorem 2.3, R2) | `ZM1INV.md` 70-78 | Corollary 2.1 (section 2.3) |
| Neutral registers (R5); path obstruction (Theorem 3.3); good sector "not unital" (Theorem 3.4 remark); Theorem 3.5; R6 shared support | `ZM1INV.md` 96-144 | lines 75, 85, 93, 95, 105 |
| Reading tests of R-V, R-NC, R-ALL | `ZM1INV.md` 179-183 | item 38 |
| Characters of every named law (Theorem 2); no `ab=λba` pair (Theorem 5); evenness and forced unitality (Theorem 6); `M₂` corners (Theorem 8) | `GB1Z2L5.md` 37-53, 67, 75-81, 89 | Theorem 5; lines 95; section 2.3 |
| Lifts, end-exchanging reversals, cube stabilizers (Theorem 2.2); O witnesses (Theorem 4.2); even-`m` U witnesses (Theorem 5.5); target conditions (section 1 item 5) | `VC1_5.md` 52, 84-94, 124, 36 | Theorem 1; section 2.1; section 2.2; item 9 |
| PS-1c, the working-set definition of cell covariance | `TOE_ASSEMBLY.md` 180 | section 2.1 |
| ZM1-INV owner text, lead's scope note, check record | `TOE_ASSEMBLY.md` 252-254 | section 2.1; item 31 |
| (Z-b) cell covariance of Definition Z | `ZM1.md` 59 | section 2.1 |
| Pass-2 compression of (INV-2)'s rotations (P6) | `ZM1INV_REFEREE.md` 47 | section 2.1 |
| Pass-1 text of K-INV-E, class J, Theorem J, Lemma NGF remarks | `KINV_DRAFT.md` 181, 187-209, 229, 240 | sections 2.5, 3; items 4, 10 |

**Extended here.** R-NGF (section 2.4) extends `KINV.md` Theorem 5 to non-unital injective maps. Section 2.1 extends `VC1_5.md` Theorem 2.2's cube-stabilizer clause to the fine block centre for every `L`. Section 2.5 gives a counterexample to the draft's general Step 1 claim.

**Prior work the digest missed.** `prior/KINV.md` cites neither `VC1_5.md` nor PS-1c nor `ZM1INV_REFEREE.md` P6 (`grep` counts 0, 0, 0).
- PS-1c (`TOE_ASSEMBLY.md` line 180) is the working-set definition of "cell covariance". It decides that Theorem 2's rotation premise is the plain reading.
- `VC1_5.md` Theorem 2.2 supplies the lifts, "carry Gauss generators and end numbers to their images", and "Every link has an end-exchanging reversal in `G`". Theorems 1-3 rest on it. The draft found it; the digest did not list it.
- `ZM1INV_REFEREE.md` line 47 records that ZM1INV's pass 2 compressed pass 1's "(INV-2) rotations". This is why `ZM1INV.md` line 29 says only "cell covariance".

---

## 7. Open statements to carry by name

- **K-INV-E.** K-INV(m, m₁, L) with `m,m₁` even and `L≥2`; K-INV(O; m₁, L) with `m₁` even and `L≥2`. It is a lemma on which three distinct attacks failed, each at a proved step:
  - **A, covariant characters**: fails at Theorem 4. The constant locked map meets every map condition except injectivity, so any refutation must use injectivity.
  - **B, good sector completed by a character**: fails at Theorem 5 and Corollary 5.1. No injective uniformly local map acts as a character on a nonzero invariant projection.
  - **C, charge-equivariant decimation**: fails at Theorem 6. Representatives of coarse neighbours must be fine neighbours, so `L≤1`.

  They are distinct: A uses the character and covariance, B uses injectivity and locality, C uses a joint spectrum and density. The three earlier failed attacks stand with their own scopes: neutral matrix registers (`ZM1INV.md` R5), end-equivariant link decimation (Theorem 3.3), good-sector decimation with representative end data (Theorem 3.5). Proved constraints on any K-INV-E map: Theorem 3, Theorem 5 (with R-NGF), `ZM1INV.md` R6, and exclusion from class J.
- **K-INV-O** (O coarse law). Theorem 2 does not reach it: on `S_+` the two end parities of a link are equal, so an end exchange gives no contradiction.
- **K-INV with odd fine `m`.** Outside the even-`m` question. Theorem 2's route gives nothing: no odd-`m` character is reversal invariant.
- **GAP-GLOBAL.** A unital, globally compatible extension of the good-sector map to defect sectors (`ZM1INV.md` line 124).
- **ZM1-I1[INV] in non-character vacua; fine-side test non-triviality; coarse-state symmetry under readings imposing it.** Unchanged from `ZM1INV.md`. For odd `m₁` the coarse-state question no longer matters, since the map cannot exist.
- **Inherited, unchanged.** VC1 and its vacuum choice; ICE-T and ICE-U(R4); LZ1-i[ZM1a]; ZM1-G; Y1; H-BLOCK; R-CS and R-CS^str; MT1-S; ZM1(a)1 and full ZM1.

---

## 8. Freeze recommendation

**Freeze `KINV.md` after E1-E3.** The three edits are wording-level and change no theorem. Recommended edits R1-R5 may be made at the same time.

What the frozen file then holds, as author-side mathematics with this one referee check:
- Theorem 2 (P) and Corollary 2.1, under the plain reading that cell covariance includes the rotations about cell centres (PS-1c, (Z-b)). The dependence is already recorded at lines 49 and 103.
- Theorems 3-7, with Theorem 6 in its repaired form and class J as corrected by E2.
- K-INV-E carried open by name, with attacks A, B, C named.

No owner decision is needed for the freeze. R-TR stays recorded and not proposed.

---

## FINISH

**Proved (referee-side, this report).**
- The pull-back `χ₀∘Φ` of a character through a unital `*`-homomorphism is a character. Injectivity is not used; unitality is (section 2.3).
- Cell covariance, as PS-1c and (Z-b) define it, includes `ρ(2u+(x,y,z))=2u+(1−x,z,y)`: a proper cubic rotation by `π` about the cell centre that exchanges the ends of a link in the cell. Its fine lift exists for every `L` (section 2.1).
- Theorem 2 (P) is correct: for odd `m₁`, every `L≥1`, fine `L5-U[m]` with `m` even or `L5-O[S_+]`, no unital `*`-homomorphism `𝔄₁^G→𝔄^G` intertwines `ρ` with a specified fine lift.
- Corollary 2.1 is correct: in locked U (even `m`) and locked O vacua with the base tick, ZM1-I1[INV] with a U coarse law holds exactly when K-INV holds for some even `m₁∈{2,4,6,8}` and `L≥2`.
- Theorems 3, 4, 5, 7 are correct. Theorem 6 is correct in `KINV.md`'s repaired form.
- R-NGF: Theorem 5 holds without unitality (section 2.4).
- The mixed O product states are not characters on `𝔄^G` (section 2.2).

**Counterexamples.**
- To the draft's Theorem J Step 1 claim "star generators at distinct sites commute": the class-J family `Q^F_x=p_{(x,x+e₁),x}+h_{(x−e₁,x)}` has `‖[Q^F_x,Q^F_{x+e₁}]‖=1` (section 2.5).
- To the literal wording of `KINV.md` Definition 4: a mixed O product is not a character (section 2.2; fix E1).
- Confirmed from `KINV.md`: Theorem 2 refutes K-INV(m, m₁, L) for every even `m`, odd `m₁` and `L`, and K-INV(O; m₁, L) for every odd `m₁` and `L`.

**Open by name.** K-INV-E (three failed attacks: A covariant characters, Theorem 4; B good sector completed by a character, Theorem 5; C charge-equivariant decimation, Theorem 6); K-INV-O; K-INV with odd fine `m`; GAP-GLOBAL; ZM1-I1[INV] in non-character vacua; fine-side test non-triviality; coarse-state symmetry under readings imposing it; the inherited list of section 7.

**What changes downstream.**
- `KINV.md` can freeze after E1-E3. Its Theorem 2 and Corollary 2.1 then stand as refereed author-side results.
- ZM1-I1[INV] in locked vacua: odd coarse registers are excluded on these fine laws; the target reduces to K-INV-E.
- K-INV lanes: work K-INV-E within the proved constraints (Theorems 3, 5, 6 and `ZM1INV.md` R6). Do not use the draft's unproved "defects must be absorbed locally".
- Owner: no decision is needed. Theorem 2 uses the rotations that PS-1c and (Z-b) already name; R-TR would change that definition.
- No axiom, working-set entry, reading or frozen file changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. No file other than this one was edited.
