lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane
# VC1-5U-odd: referee report (pass 3)

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 3 (the referee) under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** A referee report on `VC1_5U_ODD.md`. It is one line-by-line read of the distilled text. It grants no status. It adopts no law, no reading and no definition. It changes no axiom and no working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. A "referee closure" (RC) is a complete short argument written in this file. No other session has checked the closures. This is one check of the proof. No review of this review was commissioned.

**Referee.** Claude Opus 5.5 (model id `claude-opus-5-5`), max effort, headless, Mac mini. A fresh session: it wrote neither pass 1 (`VC1_5U_ODD_DRAFT.md`) nor pass 2 (`VC1_5U_ODD.md`). Its session id is not visible to it.

**Text refereed.** `VC1_5U_ODD.md` at commit `3823d3b3e` (branch head; the last commit that touches the file). SHA-256 `c550d04b4f3be5f392b869ff394c02256eca9405ca08aea8e7a47aa3a4b2c7fe`, 176 lines. Line numbers below refer to this file.

**Source revisions read.**

| Ref | Commit |
|---|---|
| `claude/toe-assembly`, local sparse checkout, as named in the lane brief | `3823d3b3e` |

No other branch was read.

**Files read, by line, with the commit of their last change.** This folder: `VC1_5U_ODD.md` (`3823d3b3e`) lines 1-176 (all). `VC1_5U_ODD_DRAFT.md` (`f67ed2001`) lines 1-324 (all); its SHA-256 `ac69babc…989de7` equals the hash that `VC1_5U_ODD.md` line 13 records. `VC1_5.md` (`bf95fc909`, frozen) lines 1-228 (all); SHA-256 `7461113c…c83c56a8`, equal to the recorded hash. `LW1_5.md` (`271c868a4`, frozen) lines 25-100 (definitions, the two laws), 128-142 (Theorem U), 220-240 (Σ-U, Z-U, H-U), 255-272 (B1-U); SHA-256 `7afb7ee2…b20e`, equal. `LZ1.md` (`b3f266672`, frozen) lines 160-194 (RC1, RC2); SHA-256 `8dc59d4d…1fe`, equal. `TOE_ASSEMBLY.md` (`c5a9d29aa`) lines 160-168, 201-230 (sections 3.4-3.6), 484-497 (VC1), 670-672 (section 10). Routing: `AGENTS.md` and `docs/ai_methodology/SCIENCE_WORKFLOW.md` (`66962bfc2`), all. Format only: `LW1_REFEREE.md` (`5a2a0affe`) lines 1-100; `Y2W_DRAFT.md` (`92e03055c`) lines 1-40. `VC1_5_REFEREE.md` (`aa193b655`): section headings only, for layout; its content was not read or reviewed.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The law `L5-U[m]`, the cell group, the conditions (i)-(iii) and the readings E, P, F of `VC1_5.md` are read plainly. Nothing is specified or proposed for adoption.

**Working set used, by name.** PS-1c, PS-5, PS-6r and PS-7r, only through the frozen law `L5-U[m]` (`LW1_5.md` section 2) and `VC1_5.md`. PS-3c, PS-4 and proposed PS-3h5 appear only in the row on conditional records.

**Inputs from outside the working set.** Standard mathematics, used without a new proof: the spectral theorem for a representation of `C(K)` (`K` compact metrizable); the Riesz representation theorem; the Radon-Nikodym theorem and its chain rule; the π-λ theorem; both Borel-Cantelli lemmas; Stone-Weierstrass; Schur orthogonality; highest-weight theory of `U(5)`; perfectness of `SU(5)`. Literature, from one short targeted search on 2026-11-06 (context only, labelled `unchecked`, never load-bearing):

| Work | ID | Fetched | Use here |
|---|---|---|---|
| Bencs, Hrušková, Tóth, *Factor-of-iid Schreier decorations of lattices in Euclidean spaces* | arXiv:2101.12577 | abstract | confirms title, authors, and that `Z^d` (`d ≥ 3`) has finitary-factor-of-iid Schreier decorations; Theorem 1.2 was not re-read (row 74) |
| Galicza, Pete, *Sparse reconstruction in spin systems II: Ising and other factor of IID measures* | arXiv:2406.09232 | abstract; Proposition 4.3 from a search summary only, **NOT VERIFIED** | reported: a finitary iid coding whose coding radius `R` has `E\|B_{2R}\| < ∞` is tail-trivial; the published analogue of RC-A3b |
| Nahum, Chalker, Serna, Ortuño, Somoza, *3D loop models and the CP^{n-1} sigma model*; *Phase transitions in 3D loop models and the CP^{n-1} sigma model* | arXiv:1104.4096; arXiv:1308.0144 | search summary only, **NOT VERIFIED** | reported: completely packed loop models on 3D lattices have a finite-loop regime and an infinite-loop regime; context for A2-FIN |
| Serna, *3D Unoriented loop models and the RP^{n-1} sigma model* | arXiv:2107.13366 | abstract | a 3D completely packed loop model with crossings; context for A2-FIN |

**Method.** I re-derived every proof in `VC1_5U_ODD.md` by hand. I checked every citation of `VC1_5.md` against the line it quotes (section 5). A `[check]` is a small scratch computation in `/tmp/toe-vcoddref/`: `check_pairings.py` (output `out_pairings.txt`), `check_linksign.py` (`out_linksign.txt`), `check_a2.py` (`out_a2_16.txt`, `out_a2_32.txt`). Each ran in under 3 s and under 90 MB of memory (measured with `/usr/bin/time -l`), started at 54-56 percent free memory. A check guides and never proves. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix); INCOMPLETE (a named missing step, with what is missing).

**Counts.** 83 items: 78 CORRECT, 1 ERROR, 4 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a theorem. The two items the lane brief names are decided in section 3: the purity-tail equivalence (Theorems 4.3 and 5.3) is CORRECT; Proposition 6.2 is CORRECT, with two proof steps to fill.

---

## 1. Verdict table

"s" numbers count sentences inside the paragraph on that line.

| # | Item (`VC1_5U_ODD.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status paragraph (5) | CORRECT | |
| 2 | §0 "Proved" list, claims 1-6: shadows, isotype, ice-measure states, purity ⇔ tail, ICE-T suffices, edge necessity (7) | CORRECT | Proved by Theorem 2.2, Lemma 2.1 and Theorems 4.2, 4.3, 5.1, 5.2. |
| 3 | §0 "Proved" list, "The R4 limit is pure on the invariant algebra exactly when its ice law is tail-trivial" (7) | ERROR | Presupposes one R4 limit. Theorem 5.3 treats each limit point. Fix in §2.1. |
| 4 | §0 "Proved" list, "The deterministic transition-system construction fails: all its paths are infinite" (7) | CORRECT | Proposition 6.2 concerns `G`-invariant systems; add "`G`-invariant" (edit E2). |
| 5 | §0 GAP paragraph (9) | CORRECT | The gaps are real (§4.1). Update its quasi-invariance sentence for A2 (RC-A2, edit E3). |
| 6 | §0 Open by name (11) | CORRECT | Add ICE-U(R4) and A2-FIN (§8). |
| 7 | §0 Provenance (13) | CORRECT | Draft, `VC1_5.md`, `LW1_5.md` and `LZ1.md` hashes recomputed: all equal. The pass-2 session id is not checkable here. |
| 8 | Definition 1 (17) | CORRECT | Matches `VC1_5.md` lines 19-26 (§5). |
| 9 | Definition 2 (18) | CORRECT | Matches `VC1_5.md` lines 31, 33 and `LW1_5.md` lines 87-93, 136. |
| 10 | Definition 3: shadow, outside σ-algebras, tail (19) | CORRECT | |
| 11 | Definition 4: `Ω_ice`, its `G`-action and tail (20) | CORRECT | `Ω_ice` does not depend on `m`. |
| 12 | Definition 5: replacements, quasi-invariance, flip-invariance (21) | CORRECT | `D(β,β')` is clopen; `S_{β→β'}^{-1}=S_{β'→β}`. |
| 13 | Definition 6: ICE-T, ICE-T⁻, ICE-U, ICE-QI and their implications (22) | CORRECT | Flip-invariance implies quasi-invariance. Four tests pass: each is a question used only as a hypothesis. |
| 14 | Definition 7: transition systems (23) | CORRECT | |
| 15 | Lemma 2.1, statement (27-31) | CORRECT | |
| 16 | Lemma 2.1 proof: charge sum, number conservation, evenness, locality (33) | CORRECT | |
| 17 | Lemma 2.1 proof: isotypic projection, centrality, one isotype, lifts, charge (35) | CORRECT | Sharpness on central projections is `VC1_5.md` Theorem 3.1(a) (line 49); lift covariance is Theorem 2.2 (line 39). Cite both (edit E11). |
| 18 | Theorem 2.2, statement (37) | CORRECT | Needs no tick, no gauge invariance, no plaquette data. |
| 19 | Theorem 2.2 proof: `C(K_m)` and the spectral measure (39, s1-3) | CORRECT | Every finite admissible pattern is a joint eigenvalue, so the cylinder calculus is isometric. |
| 20 | Theorem 2.2 proof: `P(T)` lies in the outside von Neumann algebra (39, s4-5) | CORRECT | |
| 21 | Theorem 2.2 proof: commutation, density, factor (39, s6-9) | CORRECT | Outside numbers are even, so they commute with odd local elements of `A` too. |
| 22 | Corollary 2.3, statement (41) | CORRECT | |
| 23 | Corollary 2.3 proof (43) | CORRECT | "The arrow and end-number tails coincide on this support" is compressed; RC-T writes it out. |
| 24 | §3 preamble (47) | INCOMPLETE | The end numbers of an arrow vector are not stated; `G_x^{E_{jk}}` needs the complex-linear extension of `T ↦ G_x^T`. §2.2. |
| 25 | Lemma 3.1, statement (49) | CORRECT | |
| 26 | Lemma 3.1 proof (51) | CORRECT | |
| 27 | Lemma 3.2, statement (53) | CORRECT | |
| 28 | Lemma 3.2 proof (55) | CORRECT | |
| 29 | Lemma 3.3, statement (57-62) | CORRECT | In fact `σ_C=+1` for every closed trail (RC-σ). |
| 30 | Lemma 3.3 proof: gauge invariance (64, s1-2) | CORRECT | |
| 31 | Lemma 3.3 proof: index forcing, action, sign (64, s3-6) | CORRECT | `[check]` `check_linksign.py`: the per-link sign is `(−1)^a` for both trail directions. |
| 32 | Lemma 3.4, statement (66) | CORRECT | |
| 33 | Lemma 3.4 proof (68) | CORRECT | |
| 34 | Quantum-link remark (70) | CORRECT | Context; no proof rests on it. |
| 35 | Definition of `R_S` and `V_S` (74-77) | CORRECT | |
| 36 | Lemma 4.1, statement (79-84) | CORRECT | |
| 37 | Lemma 4.1 proof (86) | CORRECT | Chain rule `R_{S_2S_1}=R_{S_2}·(R_{S_1}∘S_2^{-1})` checked. |
| 38 | Definition of `Θ` and its independence of `L` (88-92) | CORRECT | For admissible `β,β'` one has `D(β,β')=[β]`. |
| 39 | Theorem 4.2, statement (94) | CORRECT | |
| 40 | Theorem 4.2 proof: `*`-representation and extension (96) | CORRECT | Multiplicativity re-derived from Lemmas 3.2 and 4.1. |
| 41 | Theorem 4.2 proof: stationarity (98, s1-3) | CORRECT | Each hop term ends with a matter annihilator; on arrow vectors `(p_{ℓ,src}−m/2)^2=1/4`. |
| 42 | Theorem 4.2 proof: cell invariance (98, s4-6) | CORRECT | `(−1)^{a(a+1)}=+1` re-derived. |
| 43 | Theorem 4.2 proof: numbers, shadow, isotype (98, s7-8) | CORRECT | `Q_x=3(a+1)+3a=3m`; `w*` is dominant. |
| 44 | Theorem 4.2 proof: full matter (100) | CORRECT | |
| 45 | Theorem 4.3, statement (102) | CORRECT | Decided in §3.1. |
| 46 | Theorem 4.3 proof: GNS triple (104, s1-2) | CORRECT | |
| 47 | Theorem 4.3 proof: the commutant consists of multiplications (104, s3) | CORRECT | |
| 48 | Theorem 4.3 proof: invariance under loop reversals, then under all replacements (104, s4-5) | CORRECT | `Θ(O_C)=σ_CV_{S_C}` by refinement; quasi-invariance carries null sets along the chain of Lemma 3.4. |
| 49 | Theorem 4.3 proof: fibre averages and a tail-measurable version (106) | CORRECT | |
| 50 | Theorem 4.3 proof: the converse (108) | CORRECT | "preserves the outside-coordinate σ-algebras on its image, so `ν` is tail-trivial" needs one more line; RC-T supplies it. |
| 51 | Remark on stationarity and plaquette layers (110) | CORRECT | |
| 52 | Theorem 5.1, statement (114) | CORRECT | One ICE-T measure serves every odd `m`. |
| 53 | Theorem 5.1 proof (116) | CORRECT | |
| 54 | Theorem 5.2, statement (118) | CORRECT | |
| 55 | Theorem 5.2 proof (120) | CORRECT | `27=6·4+3`. The tail transfer is RC-T. |
| 56 | Remark on other odd `m` (122) | CORRECT | Divergence at `x` equals `Σ_{ℓ∋x}p_{ℓ,x}−3m=0`; `\|E_ℓ\|≤min(m,10−m)/2` checked. |
| 57 | Theorem 5.3, statement (124) | CORRECT | Decided in §3.1. |
| 58 | Theorem 5.3 proof: box replacements preserve the flux sector (126) | CORRECT | |
| 59 | Theorem 5.3 proof: the limit law is `G`- and flip-invariant (128, s1-2) | CORRECT | π-λ from cylinders to Borel sets. |
| 60 | Theorem 5.3 proof: the restriction identity (128, s3-5) | CORRECT | `ω̂_ν(B)=Σk_B(β',β)ν(D(β',β))` and `ω(B)=Σk_B(β',β)ν(D(β,β'))`; flip-invariance equates them. |
| 61 | Theorem 5.3 proof: purity and factor clauses (128, s6-7) | CORRECT | The factor clause uses RC-T. |
| 62 | Paragraph on ICE-U for an R4 limit (130) | CORRECT | Name the statement ICE-U(R4) (§8). |
| 63 | Conditional records (132) | CORRECT | The hypothesis ICE-T can be dropped (§2.3). |
| 64 | LZ1 consequence (134) | CORRECT | The hypothesis ICE-T can be dropped (§2.3). Quote `LZ1.md` line 172 checked. |
| 65 | Lemma 6.1, statement (138) | CORRECT | |
| 66 | Lemma 6.1 proof (140) | CORRECT | The last step is the π-λ theorem. |
| 67 | Proposition 6.2, statement (142) | CORRECT | Decided in §3.2. |
| 68 | Proposition 6.2 proof: invariant pairings (144, s1-3) | INCOMPLETE | "the 3-cycle moves every such pair" is not yet a contradiction. §2.2. |
| 69 | Proposition 6.2 proof: the walks (144, s4) | CORRECT | Import of `VC1_5.md` lines 129-136 checked; re-derived independently (RC-6.2); `[check]` `check_pairings.py` agrees. |
| 70 | Proposition 6.2 proof: "All trails are therefore infinite" (144, s5) | INCOMPLETE | The walk from one link does not cover all trails; the transitivity step is missing. §2.2. |
| 71 | Proposition 6.2 proof: `G`-invariance of the coin law; the tail event of probability 1/2 (144, s6-7) | CORRECT | |
| 72 | A2: the construction and its conditional claims (146, up to "GAP") | CORRECT | |
| 73 | A2 GAP (146) | CORRECT | The gap is real. Quasi-invariance is repaired given finiteness (RC-A2). The residual is A2-FIN (§4.2). |
| 74 | A3: the reported theorem and the `G`-invariance (148, up to "GAP") | CORRECT | Abstract fetched: `Z^d`, `d≥3`, has "finitary-factor-of-iid Schreier decorations". |
| 75 | A3 GAP (148) | CORRECT | The gap is real. "finitary coding alone does not imply it" is proved by RC-A3a. A sufficient criterion is RC-A3b (§4.3). |
| 76 | A4: uniform ice (150) | CORRECT | |
| 77 | Theorem 7.1, statement (154-164) | CORRECT | |
| 78 | Theorem 7.1 proof (a) (166) | CORRECT | |
| 79 | Theorem 7.1 proof (b) (166) | CORRECT | `5k−3m∈[0,5]` forces `k=1`, `2`, `3` or `4`, `5`, `6` for `m=1, 3, 5, 7, 9` respectively. |
| 80 | Theorem 7.1 proof (c)-(e) (168) | CORRECT | |
| 81 | Σc-odd paragraph (170) | CORRECT | At `m=5` the ice pattern has site space `(Λ^3)^{⊗3}⊗(Λ^2)^{⊗3}`, whose `SU(5)`-invariant space has dimension above one: `Λ^3≅(Λ^2)^*⊗det`, so the invariants form `End_{SU(5)}((Λ^2)^{⊗3})`, and `(Λ^2)^{⊗3}` is reducible. |
| 82 | §8, inputs (174) | INCOMPLETE | The π-λ theorem and Stone-Weierstrass are used but not listed; the frozen inputs are not named. §2.2. |
| 83 | §8, scope (176) | CORRECT | Both laws stay live (`TOE_ASSEMBLY.md` line 214). |

---

## 2. Details of the non-CORRECT items

### 2.1 ERROR

**Item 3 (line 7, status wording).** The text: "The R4 limit is pure on the invariant algebra exactly when its ice law is tail-trivial." Nothing proves that the R4 states have one limit. Theorem 5.3 (line 124) is exact: "Let `ω` be a local weak-* limit point of the finite-volume states of `VC1_5.md` R4 along a subsequence". Different limit points may have different arrow laws. Fix: "For each local weak-* limit point `ω` of the R4 states, `ω∘E` is pure on `A^gauge` exactly when its ice law is tail-trivial." No proof changes.

### 2.2 INCOMPLETE

**Item 24 (line 47, §3 preamble).** The text: "At the end with number `p`, occupy flavours `1,…,p`." It never says which number each end of an arrow vector carries. Lemma 3.1 ("exactly three occupied in flavour `a+1`"), Theorem 4.2 ("the high/low end-number map") and line 70 need it. The draft states it (line 133): "put `p_h = a+1`, `p` of the other end `= a`". R4 uses the same vectors (`VC1_5.md` line 210). Missing clause: "On a link with high end `h`, the end `h` has number `a+1` and the other end has number `a`." A second clause is also missing. `LW1_5.md` line 93 defines `G_x^T` for Hermitian `T`; the preamble applies it to `E_{jk}`. Add: "`T ↦ G_x^T` is extended complex-linearly."

**Item 68 (line 144, Proposition 6.2 proof, first step).** The text: "An invariant pairing cannot pair two links in either triple: the 3-cycle moves every such pair." A moved pair is not yet a contradiction; an invariant pairing may contain a pair together with its image. The missing step: the image of a pair inside a 3-set is a different pair inside the same 3-set, and it shares one link with the original; a pairing has at most one pair inside a 3-set. The draft has it (line 264). Fix: "the 3-cycle maps such a pair to a different pair in the same triple, sharing a link with it; a pairing contains at most one pair inside a 3-set."

**Item 70 (line 144, "All trails are therefore infinite").** The walk of `VC1_5.md` Theorem 6.1 starts at one link, `(0,e_1)`. The missing step extends it to every trail. Every pair joins an even link to an odd link, so every trail contains an even link. `G` is transitive on even links: it is site-transitive, and the site stabilizer cycles the even triple (`VC1_5.md` Theorem 2.2, line 39). `G` permutes the trails of an invariant system. So every trail is the image of the trail through `(0,e_1)`. `VC1_5.md` line 136 says this: "Site transitivity and the site stabilizer take this component to every other component, so all are bi-infinite paths." Fix: cite that sentence and Theorem 2.2 (edit E7), or insert step 4 of RC-6.2.

**Item 82 (line 174, inputs).** Two standard inputs are used but not listed. The π-λ theorem: Lemma 6.1 ("hence of the full input σ-algebra") and Theorem 5.3 ("then from cylinders to Borel sets"). Stone-Weierstrass, or the density of cylinder functions in `C(Ω_ice)`: Theorem 4.3 (line 104). The sentence "The finite-volume and group-geometry results are cited frozen inputs" names none of them. Fix: list the two inputs, and name the frozen results used (`VC1_5.md` Theorems 2.1, 2.2, 3.1(a), 5.3, the proof of 6.1, Corollary 5.6, R1, R4; `LW1_5.md` Theorem U and B1-U; `LZ1.md` RC1(c)(iii)).

### 2.3 Notes on CORRECT items that bear on the freeze

1. **The tail transfer (items 23, 50, 55, 61).** Four steps move tail triviality between the arrow law `ν` on `Ω_ice` and the number shadow on `K_m`. Each step is true. The text compresses the one point that needs care: the trace of an intersection of σ-algebras on the subset `Ω_ice`. RC-T (section 6) writes it in four lines.
2. **The sign of a loop operator (item 29).** For both directions of a link, the bilinear on that link maps `|ℓ;x_{i+1}⟩` to `(−1)^a|ℓ;x_i⟩`. Every closed trail in `Z^3` has even length. So `σ_C=(−1)^{a|C|}=+1` (RC-σ). No proof needs the value.
3. **ICE-T is not needed at lines 132 and 134.** Both paragraphs use only that the state is gauge-invariant, stationary and cell-invariant, with `N_x` sharp and isotype `w*`. Theorem 4.2 gives this for `ω_ν` with any `G`-invariant quasi-invariant `ν`, tail-trivial or not. Theorem 5.3 gives such a `ν` with no hypothesis: the arrow law of any R4 limit point. So `LZ1.md` RC1(c)(iii) applies to `ω∘E` for every R4 limit point `ω`. The conditional record conclusion holds for these states under the same readings. The two paragraphs stay correct as written; dropping "Under ICE-T" is optional (edit O2).
4. **The status line states two results for P-witnesses.** Lemma 2.1 needs only P and (iii). Theorem 5.2 needs neither (i) nor (ii), as it says. The status line (7) is weaker than the two results, and true.

---

## 3. The two decisions the lane brief asks for

### 3.1 "Pure on the gauge-invariant algebra exactly when the arrow law is tail-trivial"

**Decision: CORRECT**, in the two forms the text proves. Theorem 4.3 (line 102): for every quasi-invariant Borel probability measure `ν` on `Ω_ice`, `ω̂_ν` is pure on `A^gauge` if and only if `ν` is tail-trivial. Theorem 5.3 (line 124): for each local weak-* limit point `ω` of the R4 states, its arrow law `ν` is `G`-invariant and flip-invariant, `ω|A^gauge=ω̂_ν`, and `ω∘E` is pure on `A^gauge` exactly when `ν` is tail-trivial. The status line (7) needs the wording fix of item 3.

**Scope, exactly.** Theorem 4.3 needs neither `G`-invariance of `ν` nor any value of the tick constants. Purity in this sector is kinematic. Theorem 5.3 is a statement about one limit point at a time. It says nothing about uniqueness of limit points, and nothing about whether any limit law is tail-trivial.

**The re-derivation, step by step.**
1. *GNS.* `Θ(Π_β)=M_{1_{[β]}}` for every cylinder `[β]`, because `Π_β` acts on arrow vectors by the indicator of `β`. Cylinder indicators span a dense subspace of `L²(ν)`. So `(L²(ν),Θ,1)` is the GNS triple of `ω̂_ν`, and purity is `Θ(A^gauge)'=C1`.
2. *Commutant.* An operator `T` in the commutant commutes with all `M_{1_{[β]}}`, hence with `M_f` for every `f∈C(Ω_ice)` (cylinder functions are dense, by Stone-Weierstrass on the totally disconnected compact `Ω_ice`). With `h=T1`, `Tf=fh` on `C(Ω_ice)`; the bound `∫_B|h|²dν≤‖T‖²ν(B)` gives `h∈L^∞` and `T=M_h`.
3. *Loop invariance.* For a directed closed trail `C`, `Θ(O_C)=σ_CV_{S_C}` (Lemma 3.3 and the refinement rule of Lemma 4.1). Applying `M_hV_{S_C}=V_{S_C}M_h` to `1_{dom S_C}` gives `hR^{1/2}=R^{1/2}(h∘S_C^{-1})` on `ran S_C`, and `R>0` there by quasi-invariance. So `h∘S_C=h` a.e. on `dom S_C`.
4. *All replacements.* A replacement `S_{β→β'}` changes a fixed finite link set `D_0`. Lemma 3.4 writes it on its whole domain as the composite of reversals of one fixed list of link-disjoint trails, each directed at its turn. Quasi-invariance carries null sets along the list. So `h∘S=h` a.e. on `dom S`, for every replacement.
5. *Tail version.* For finite `L`, a Borel version `h_0` is constant on every fibre `{c'' : c''=c off L}` outside a null set (finitely many replacements act on `L`). The fibre average `H_L` is Borel, depends only on the arrows off `L`, and equals `h_0` a.e. Along `L_n` (links with an endpoint in `Λ_n`), `limsup_n Re H_{L_n}` is measurable for the arrows off `L_k` for every `k`, so it is tail-measurable, and it equals `Re h` a.e. The same holds for `Im h`. Tail triviality makes `h` constant.
6. *Converse.* Purity of `ω̂_ν` makes the GNS representation of `ω_ν|A^gauge` irreducible, hence a factor. Theorem 2.2 makes the shadow tail-trivial. The shadow is `ι_*ν`, with `ι` the map "`n≡0`, `p=a+1` at high ends, `p=a` at low ends". RC-T transfers tail triviality back to `ν`.
7. *R4.* For large boxes, a local invariant `B` changes `c∈𝒞_L` only on directed closed trails inside a ball that does not wrap the box (Lemmas 3.2, 3.4). Their lifts to `Z^3` are closed walks, so they cross every coordinate plane as often in each direction, and the R4 flux sector is preserved. Hence each local replacement preserves the uniform law on `𝒞_L`, and in the limit `ν` is flip-invariant; `R4(d)` gives `G`-invariance. With `R_S≡1`, `ω̂_ν(B)=Σk_B(β',β)ν(D(β',β))`, while `ω(B)=lim ω_L(B)=Σk_B(β',β)ν(D(β,β'))`; flip-invariance equates the two. Steps 1-6 then apply. If `ν` is not tail-trivial, RC-T gives a nontrivial tail event of the shadow, and Theorem 2.2 rules out a factor restriction.

No step depends on the plaquette class, because every statement here concerns the base tick or no tick at all.

### 3.2 Proposition 6.2

**Decision: CORRECT.** Both claims hold. (a) Every `G`-invariant transition system consists of bi-infinite trails. There are exactly three such systems: the straight lines, and two systems whose trails drift by `(2,2,−2)`-type vectors every six steps. (b) Orienting the trails by independent fair coins gives a `G`-invariant ice law with a tail event of probability `1/2`.

The proof at line 144 is right in substance and has two short gaps: items 68 and 70. RC-6.2 (section 6) is an independent proof. It does not use the text of `VC1_5.md` Theorem 6.1. It computes the pairing at every site from the pairing at `0`, and it follows the walks. `[check]` `check_pairings.py` agrees: the stabilizer of `0` has order 3; exactly 3 of the 15 pairings are invariant; for the two non-straight ones the walk from `0` along `+e_1` returns after 6 steps translated by `(2,2,−2)`, respectively `(2,−2,2)`, as in `VC1_5.md` lines 132-133.

Part (b): `G` permutes the trails, so it preserves the product of fair coins. Fix a trail `γ`. The event "the arrows of `γ` agree with one fixed direction of `γ` on all but finitely many links" is determined by the arrows off `L_n` for every `n`, since `γ∩L_n` is finite. Under the coin law it has probability `1/2`. So the law is not tail-trivial. It is also not quasi-invariant: a plaquette reversal carries a set of positive measure to a null set, because each reversed link lies on an infinite trail whose other links keep their orientation. Nothing claims otherwise.

---

## 4. The GAPs marked by the distiller

### 4.1 GAP at line 9 (ICE-T and the R4 tail)

**Real.** Neither ICE-T nor tail triviality of any R4 limit law is proved, here or in the draft. Theorem 5.3 shows that the second is exactly the open core that `VC1_5.md` line 221 names ("Whether some `ω∘E` of R4 is pure on `A^{gauge}`"). Section 8 names it ICE-U(R4). One sentence of the paragraph needs an update. "Neither establishes quasi-invariance" stays true of the text, but RC-A2 now proves quasi-invariance for A2 whenever all its trails are finite. Repaired sentence (edit E3): "A3 does not address quasi-invariance. For A2, quasi-invariance and tail triviality follow from almost-sure finiteness of all trails (RC-A2); A2 is open exactly at A2-FIN."

### 4.2 GAP at line 146 (A2, independent random transitions)

The paragraph makes four claims. Verdicts:

1. "almost-sure finiteness of all trails is not proved": **real.** Nothing here proves it. I name the statement A2-FIN (section 8). `[check]` `check_a2.py`, tori `(Z/LZ)^3` with `L=16, 32`: pairings drawn i.i.d. from the uniform law on all 15 pairings, and from each of the four stabilizer orbits of size three (uniform on the orbit), transported by `G`. In every case at least 91 percent of the links lie on trails longer than `L²`, and at least 92 percent on trails that wind around the torus. This guides against A2-FIN for these five laws. It proves nothing, and it says nothing about other laws. It agrees in kind with the literature context above (`unchecked`): 3D completely packed loop models have regimes with infinite loops.
2. "The rule as written does not orient infinite trails": **real**, and it is a consequence of claim 1, not a separate gap. On the event A2-FIN the rule is defined.
3. "quasi-invariance is not checked": **real as a statement about the text; repaired here.** RC-A2 proves: if A2-FIN holds for a stabilizer-invariant full-support law, the A2 law is `G`-invariant, tail-trivial and quasi-invariant. So A2-FIN implies ICE-T, and by Theorem 5.1 it implies VC1-5U-odd at fillings 0 and 5 for every odd `m`.
4. "Near a deterministic pairing law is not a proof of infinite trails for a full-support law": **correct.** It retracts the draft's sentence (line 268) "A stabilizer-invariant law concentrated near one pairing concentrates near the patterns of Proposition 6.2, whose loops are infinite", which proves nothing.

**Repaired statement.** A2 now stands on one open statement, A2-FIN. The finite-change argument for tail triviality is already in the paragraph and is correct.

### 4.3 GAP at line 148 (A3, the Bencs-Hrušková-Tóth coding)

1. "the pass-1 source does not establish that finite input resampling changes only finitely many output arrows": **real.**
2. "finitary coding alone does not imply it": **true, and now proved.** RC-A3a is a finitary iid coding on `Z` in which resampling one input changes infinitely many outputs almost surely. So the implication fails in general. The example is not an ice configuration; it does not decide the BHT coding.
3. **Repaired criterion.** RC-A3b: if the coding radii `R_ℓ` of a finitary iid coding satisfy `Σ_ℓ P(R_ℓ ≥ d(ℓ,J)) < ∞` for every finite input set `J`, then the hypothesis of Lemma 6.1 holds and the law is tail-trivial. For a coding with finitely many `G`-orbits of links, `E[R^3]<∞` suffices on `Z^3`. Galicza and Pete report a published analogue (arXiv:2406.09232, Proposition 4.3, `E|B_{2R(o)}|<∞`; **NOT VERIFIED** here, not load-bearing). So A3 would give ICE-T⁻ if the BHT coding radius has a finite third moment. Neither that moment bound nor quasi-invariance is known here.
4. "Tail triviality and quasi-invariance are not established by this route" and "The literature statement is a pass-1 report": **correct.**

### 4.4 A4 at line 150 (uniform ice)

Not labelled GAP, but it states an unproved step: a decay-of-boundary-influence estimate for the uniform specification. **Real.** The sentence "A suitable decay-of-boundary-influence estimate ... would yield tail triviality" is correct as a sufficient condition and is not used. No repair is offered here.

### 4.5 The route-3 GAP of `VC1_5.md` (line 146 there)

`VC1_5.md` line 146: "**GAP:** finite-volume purity need not survive a weak-* limit; no proof of invariant-algebra purity is supplied." Theorem 5.3 states this GAP exactly: purity of `ω∘E` at an R4 limit point is equivalent to tail triviality of its arrow law. The GAP stays open as ICE-U(R4).

---

## 5. Imports, checked by line

The item enters frozen `VC1_5.md` by amendment. I compared every import from `VC1_5.md` with the line it reads. "Applies" means the quoted statement is what the frozen text proves and its hypotheses hold where it is used.

| `VC1_5.md` line | Imported content (quoted or named) | Used at (`VC1_5U_ODD.md` line) | Result |
|---|---|---|---|
| 19-23 (definitions 1-5) | `A`, `A^{gauge}`, `G = 2 Z^3 ⋊ O_c0`; "(i) stationarity under the tick `α`; (ii) local gauge invariance; (iii) invariance under all the stated cell lifts"; "**P** means purity of the restriction to `A^{gauge}`" | 17 | matches |
| 24 (definition 6) | "E passes all four, but is weak and does not imply F ... P passes 1, 2 and 4; check 3 is conditional because P forbids half filling" | 17 | matches; "E need not imply F" is weaker than the frozen "does not imply F" and true |
| 25-26 (definitions 7-8) | PS-7(h) "unadopted"; PS-3h5 "1, 2 and 4 pass; 3 is conditional" | 17 | matches |
| 31 | `L5-U[m]`, `p_{ℓ,x}`, `N_x`, `Q_x`; "`p_{ℓ,x}+p_{ℓ,y}=m`" | 18 | matches |
| 33 | base tick `U_0=W_EM_oM_e`; "`0≤μ<2ε<π`; `τ_E` is real. The plaquette class is not specified." | 18 | matches |
| 35 (Theorem 2.1) | "Local invariant observables are dense in `A^{gauge}`"; the affine bijection "with inverse `φ↦φ∘E`"; "The map `E` commutes with `α` and the cell lifts"; "P is equivalent to extremality among all gauge-invariant states" | 39, 96, 98, 166 | applies |
| 39 (Theorem 2.2) | lifts "`c_{x,j}↦d_g(gx)c_{gx,j}` and `r^{ℓ,z}_j↦r^{gℓ,gz}_j`"; they "carry Gauss generators and end numbers to their images"; "a site stabilizer is cyclic of order 3 and cycles the three even-cube edges and the three odd-cube edges separately" | 35, 43, 98, 144 | applies; not cited at 35 and 144 (edits E7, E11) |
| 49 (Theorem 3.1(a)) | "A self-adjoint central element `z` is sharp in every pure state `ψ` of `B`." | 35 | applies; not cited (edit E11) |
| 103 (Theorem 5.3) | "`q_x∈Z` and `ω(N_x)=q_x-3m`"; "Every state pure on `A^{gauge}` is sharp in every `Q_x`" | 43, 120, 166 | applies; (iii) supplies the reversal invariance it needs |
| 115-117 (Corollary 5.6) | records of value 0 and 5; proof "Their site numbers are sharp and equal at every tick" | 132 | applies |
| 129-136 (Theorem 6.1, pair case) | "Either `k=0` everywhere, giving straight lines, or the two sublattices alternate between `1` and `2`"; the two six-step paths; "`T=(2,2,-2)` or `(2,-2,2)`"; "all are bi-infinite paths" | 144 | applies. A `G`-invariant transition system is the pair case with blocks the trails. Re-derived in RC-6.2 |
| 164 (R1) | "If `ω\|A^{gauge}` is pure, then `π_ω(A)''` is a factor", for `ω` invariant under local gauge unitaries | 108, 114 | applies: `ω_ν=ω̂_ν∘E` is gauge-invariant |
| 210-219 (R4) | `𝒞_L` with zero plane flux; `Ψ_L`; (c) box covariance; (d) "every local weak-* limit point `ω` of `(ω_L)` satisfies (i) and (iii)" | 124-128 | applies |
| 221 | "Whether some `ω∘E` of R4 is pure on `A^{gauge}`. That is the open core of VC1-5U-odd." | 130 | Theorem 5.3 restates it as ICE-U(R4) |

Imports from the other frozen parts:

| Source line | Imported content | Used at | Result |
|---|---|---|---|
| `LW1_5.md` 33 | "Links commute with matter and are ordinary tensor factors." | 33, 47 | applies |
| `LW1_5.md` 78 | "Cube gates in a layer have disjoint matter and links. Infinite products mean local automorphisms as in LW1 E1." | 98 (implicit) | applies |
| `LW1_5.md` 87-91 | `U_ℓ^{jk}=r^y_jr^{x†}_k`; `h^U_ℓ`; `G_x^T`; `W_E` | 18, 47, 98 | applies; each hop term ends with a matter annihilator |
| `LW1_5.md` 136-138 (Theorem U) | "every `G_x^T` commutes with every hop and electric gate"; "End numbers commute with the Gauss generators" | 18, 98, 104 | applies |
| `LW1_5.md` 259-267 (B1-U) | the lifts send "`G_x^T,N_x,Q_x,p_{ℓ,z}` to their geometric counterparts" | 43, 98 | applies |
| `LZ1.md` 172 (RC1(c)(iii)) | "On `L5-U[m]`, the conclusion of (ii) holds for every locally gauge-invariant, stationary, cell-invariant state in which some `𝒢^T_x` with traceless `T` has `ω((𝒢^T_x)²)>0`." | 134 | applies; see §2.3 note 3 |

No import is misquoted. No import is used outside its hypotheses. Nothing here gives a `wrong` signal for `VC1_5.md`, `LW1_5.md` or `LZ1.md`.

I compared the draft with the distillation item by item. The distillation drops no proved statement. It weakens two draft claims, correctly: A2's unconditional "the law is `G`-invariant" becomes "Conditional on every trail being finite" (the rule orients only finite trails), and the draft's "the GAP of route 3 is exactly ICE-U for the limit `ν`" (draft line 246) becomes the sharper line 130. It omits three draft clauses that items 24, 68 and 82 restore.

---

## 6. Referee closures

Each closure is a complete argument from stated premises. Each is Lean-formalizable: finite combinatorics, countable products of finite or standard Borel spaces, and the standard theorems listed in the head. No `[check]` is a step of any closure.

### RC-T. Tail triviality across the shadow map

**Lemma.** Let `Π=∏_{i∈I}X_i` be a countable product of finite sets. Let `I_1⊂I_2⊂…` be finite, and let `F_n` be the σ-algebra of the coordinates outside `I_n`. Let `Ω⊂Π` be Borel and write `F|_Ω={Ω∩E : E∈F}`. Then `(∩_nF_n)|_Ω=∩_n(F_n|_Ω)`.

*Proof.* The inclusion `⊂` is immediate. Let `T∈∩_n(F_n|_Ω)` and choose `T_n∈F_n` with `T=Ω∩T_n`. Put `T^*=∩_k∪_{n≥k}T_n`. For each `k`, `∪_{n≥k}T_n∈F_k`, because `F_n⊂F_k` for `n≥k`. So `T^*∈∩_kF_k`. Also `Ω∩T^*=∩_k∪_{n≥k}(Ω∩T_n)=T`. ∎

**Application.** Let `A:K_m→{0,1}^{links}` record on each link whether its source end is high (`p_{ℓ,src}>m/2`). Write `F^{arr}_n` for the σ-algebra of arrows on links with no endpoint in `Λ_n`. The arrow of such a link is a function of its own end numbers, so `A^{-1}(F^{arr}_n)⊂F^{out}_n`.
- (i) Let `κ` be a probability measure on `K_m` with `κ(A^{-1}(Ω_ice))=1`, and `ν=A_*κ`. If `κ` is tail-trivial, so is `ν`. Indeed, by the lemma a tail event of `Ω_ice` is `T=Ω_ice∩T^*` with `T^*∈∩_nF^{arr}_n`. Then `A^{-1}(T^*)` is a tail event of `K_m`, and `ν(T)=κ(A^{-1}(T^*))∈{0,1}`.
- (ii) Let `ι:Ω_ice→K_m` be the injective map of Theorem 4.2 (`n≡0`, `p=a+1` at high ends, `p=a` at low ends) and `κ=ι_*ν`. Then `A∘ι` is the identity of `Ω_ice`, so (i) applies. Conversely `ι^{-1}(F^{out}_n)⊂F^{arr}_n|_{Ω_ice}`, because `n_x∘ι` is constant. So for a tail event `U` of `K_m`, `ι^{-1}(U)` is a tail event of `Ω_ice` and `κ(U)=ν(ι^{-1}(U))`. Hence `ν` is tail-trivial exactly when `κ` is.

Corollary 2.3 (line 43) and Theorem 5.2 (line 120) use (i). Theorem 4.3 (line 108) and the factor clause of Theorem 5.3 (line 128) use (ii) in the direction "`κ` tail-trivial implies `ν` tail-trivial", the second by contraposition. The other direction of (ii) is recorded for completeness. ∎

### RC-σ. The sign of a loop operator

Let `ℓ` have source end `s` and target end `t`, and let the trail of Lemma 3.3 run from `x_i` to `x_{i+1}` along `ℓ`, with high end `x_{i+1}`. Order creators source end first, as in the text.
- If `x_i=s`: the vector is `r^{s†}_1⋯r^{s†}_a r^{t†}_1⋯r^{t†}_{a+1}|0⟩`. The annihilator `r^t_{a+1}` passes `2a` creators (sign `+1`). The creator `r^{s†}_{a+1}` then passes `a` creators to its place (sign `(−1)^a`).
- If `x_i=t`: the vector is `r^{s†}_1⋯r^{s†}_{a+1} r^{t†}_1⋯r^{t†}_a|0⟩`. The annihilator `r^s_{a+1}` passes `a` creators (sign `(−1)^a`). The creator `r^{t†}_{a+1}` passes `2a` creators (sign `+1`).

Either way the bilinear on `ℓ` maps `|ℓ;x_{i+1}⟩` to `(−1)^a|ℓ;x_i⟩`. Operators on different links commute and act on separate tensor components, so no other sign arises. `Z^3` is bipartite, so `|C|` is even and `σ_C=(−1)^{a|C|}=+1`. `[check]` `check_linksign.py` agrees for `a=0,…,4`. ∎

### RC-6.2. Every `G`-invariant transition system, explicitly

*Tilings.* The even cubes are `[0,1]^3+2n` (centres `c_0+2Z^3`), the odd cubes `[1,2]^3+2n`. The link `(x,x+e_j)` is an even-cube edge exactly when `x_j` is even. So at `x`, with `s_j(x)=(−1)^{x_j}`, the even link along axis `j` points in direction `s_j(x)e_j` and the odd link along axis `j` points in direction `−s_j(x)e_j`.

*Step 1 (group elements).* For `Q∈O` and `t∈Z^3`, `y↦Q(y−c_0)+c_0+2t` equals `y↦Qy+(c_0−Qc_0)+2t`. The vector `c_0−Qc_0` has entry 1 where `Q(1,1,1)` has entry `−1`, and entry 0 elsewhere. So `g_x(y)=Q_xy+x` lies in `G` whenever `Q_x(1,1,1)=s(x)`. The stabilizer of `0` is `{Q∈O : Q(1,1,1)=(1,1,1)}={1,h,h^2}`, with `h(y_1,y_2,y_3)=(y_2,y_3,y_1)`. `h` permutes the axes cyclically and fixes all signs, so it cycles `{+e_j}` (the even triple at `0`) and `{−e_j}` (the odd triple) separately.

*Step 2 (pairing at `0`).* Let a pairing at `0` be `h`-invariant. Suppose it contains a pair inside one triple. Its `h`-image is a different pair inside the same triple, and the two pairs share a vector. A pairing contains at most one pair inside a 3-set. This is a contradiction. So every pair is `{+e_j,−e_{σ(j)}}` for a permutation `σ`, and invariance makes `σ` commute with the 3-cycle of axes. Hence `σ(j)=j+k mod 3`, `k∈{0,1,2}`.

*Step 3 (pairing at `x`).* `G`-invariance makes the pairing at `x` the image under `Q_x` of the pairing at `0`. Write `Q_xe_j=s_{π(j)}(x)e_{π(j)}`. Then `1=det Q_x=sgn(π)s_1s_2s_3`, so `sgn π=ε(x):=(−1)^{x_1+x_2+x_3}`. The pair `{+e_j,−e_{j+k}}` goes to the even link along axis `π(j)` and the odd link along axis `π(j+k)`. Conjugating the shift `j↦j+k` by `π` gives `j↦j+ε(x)k`. So at `x` the even link along axis `i` is paired with the odd link along axis `i+ε(x)k`. This rule does not depend on the choice of `Q_x`. Each `k` gives one `G`-invariant system, and there are no others.

*Step 4 (trails).* `k=0`: at every site the two links along each axis are paired, so the trails are straight lines. `k=1`: start at `0` and leave along `+e_1`. The rule of step 3 gives the sites

| step | site | `ε` | arrived along | its type at the site | leaves along |
|---|---|---|---|---|---|
| 0 | `(0,0,0)` | `+1` | `+e_2`, from `(0,−1,0)` | odd, axis 2 | `+e_1` (even, axis 1) |
| 1 | `(1,0,0)` | `−1` | `+e_1` | even, axis 1 | `−e_3` (odd, axis 3) |
| 2 | `(1,0,−1)` | `+1` | `−e_3` | odd, axis 3 | `+e_2` (even, axis 2) |
| 3 | `(1,1,−1)` | `−1` | `+e_2` | even, axis 2 | `+e_1` (odd, axis 1) |
| 4 | `(2,1,−1)` | `+1` | `+e_1` | odd, axis 1 | `−e_3` (even, axis 3) |
| 5 | `(2,1,−2)` | `−1` | `−e_3` | even, axis 3 | `+e_2` (odd, axis 2) |
| 6 | `(2,2,−2)` | `+1` | `+e_2` | odd, axis 2 | `+e_1` (even, axis 1) |

At step 6 the walk enters `(2,2,−2)` through the translate of the link `((0,−1,0),0)` and leaves along the translate of `(0,e_1)`. Translation by `T=(2,2,−2)∈2Z^3` lies in `G` and preserves the system. The walk is deterministic and reversible, so its sites obey `x_{i+6}=x_i+T` for all `i∈Z`. If the trail were closed, the sequence of (site, incoming link) pairs would be periodic, which `x_{i+6n}=x_i+nT≠x_i` forbids. So the trail is bi-infinite. For `k=2` the rule of step 3 gives, in the same way, the sites `0,(1,0,0),(1,−1,0),(1,−1,1),(2,−1,1),(2,−2,1),(2,−2,2)` and `T=(2,−2,2)`; this is the `k=1` table with axes 2 and 3 exchanged. These are the two paths of `VC1_5.md` lines 132-133.

*All trails.* For every `k`, every pair joins an even link to an odd link, so every trail contains an even link. `G` is transitive on even links: it is site-transitive, and the stabilizer cycles the even triple. `G` permutes the trails. So every trail is the image under some `g∈G` of the trail through `(0,e_1)`, and is bi-infinite. ∎

`[check]` `check_pairings.py` confirms steps 1-4: stabilizer of order 3; 3 invariant pairings among 15; the pairing at `x` independent of the choice of `Q_x` on `[−3,3]^3`; drifts `(2,0,0)`-type for `k=0` (period 2) and `(±2,±2,±2)`-type for `k=1,2` (period 6) from all six directions at `0`.

### RC-A2. A2 gives ICE-T whenever all its trails are finite

**Setting.** Let `ρ_0` be a probability law on the 15 pairings at `0`. Let it be invariant under the stabilizer `{1,h,h^2}` and have full support. Put `ρ_x=g_*ρ_0` for any `g∈G` with `g0=x`; stabilizer invariance makes this well defined. Let `τ_x∼ρ_x` (sites), `d_ℓ` uniform on the two ends of `ℓ`, and `u_ℓ` uniform on `[0,1]` (links), all independent. Write `ξ` for the whole input and `P` for its law.

**A2-FIN for `ρ_0`.** `P`(every `τ`-trail is finite) `=1`.

**Proposition RC-A2.** Assume A2-FIN for `ρ_0`. On the event that all trails are finite, let `F(ξ)` orient each `τ`-trail `γ` so that its link `ℓ^*(γ)` of largest label `u` points to `d_{ℓ^*}`. (Labels are distinct almost surely.) Then the law `ν` of `F(ξ)` is a `G`-invariant, tail-trivial, quasi-invariant Borel probability measure on `Ω_ice`. Hence ICE-T holds, and by Theorem 5.1 each odd `m` has P-witnesses at fillings 0 and 5.

*Proof.* (0) *Ice.* Each pair of `τ_x` joins two consecutive links of one consistently oriented trail, so it has one link with high end `x` and one without. Three pairs give three high ends at `x`. The trail through a link is determined by finitely many coordinates when it is finite, so `F` is Borel on the full-measure event.

(1) *`G`-invariance.* `G` acts on inputs by `(gξ)`: `τ'_{gx}=g(τ_x)`, `d'_{gℓ}=g(d_ℓ)`, `u'_{gℓ}=u_ℓ`. The input law is `G`-invariant, and `F(gξ)=gF(ξ)`. So `ν` is `G`-invariant.

(2) *Tail triviality.* Resample a finite set `J` of inputs. A `τ`-trail that visits no site of `J` and contains no link of `J` is also a trail after resampling, with the same `d` and `u` on it, so it keeps its orientation. Only the trails before or after resampling that visit a site of `J` or contain a link of `J` can change. There are finitely many, each finite almost surely (the resampled input has law `P`). Lemma 6.1 gives tail triviality.

(3) *Quasi-invariance.* Fix a replacement `S=S_{β→β'}`. Let `D_0` be the links where `β≠β'` and `V_0` their endpoints. Fix, for each pattern of three high and three low ends at a site, one pairing that matches each high end with a low end. For `ξ` with all trails finite and `c=F(ξ)∈dom S`, define `ξ'=Φ(ξ)`:
- `τ'_x` is the fixed pairing for the pattern of `S(c)` at `x`, for `x∈V_0`; `τ'_x=τ_x` otherwise;
- `u'=u`;
- `d'=d`, except on the largest-label link `ℓ^*` of each `τ'`-trail that visits `V_0`, where `d'_{ℓ^*}` is the high end of `ℓ^*` in `S(c)`.

(a) Every `τ'`-pair joins a high end and a low end of `S(c)`. At `x∈V_0` this holds by choice. At `x∉V_0` no link at `x` lies in `D_0`, so `S(c)=c` on the links at `x` and `τ'_x=τ_x`. So `S(c)` orients every `τ'`-trail consistently.
(b) Every `τ'`-trail is finite. A `τ'`-trail that avoids `V_0` is a `τ`-trail. A `τ'`-trail that visits `V_0` is a concatenation of segments; each segment starts with a link at `V_0` and follows pairings equal to those of `τ` until it returns to `V_0`. Each segment is part of one of the finitely many `τ`-trails through `V_0`, all finite. So there are finitely many segments, each finite.
(c) `F(ξ')=S(c)`. The `τ'`-trails through `V_0` are oriented by `d'` at their `ℓ^*`, which agrees with `S(c)`. The other `τ'`-trails are `τ`-trails avoiding `V_0`, with unchanged `d` and `u`; `F` orients them as `c` does, and `c=S(c)` on them.

Split the domain of `Φ` into countably many Borel pieces `Ξ_k`. On `Ξ_k`, fix the old and new values of `τ` on `V_0`, the set `M` of links where `d` is modified, and the old and new values of `d` on `M`. On `Ξ_k`, `Φ` is the restriction of the bijection `Ψ_k` that replaces these finitely many coordinates. `Ψ_k` multiplies `P` by `c_k=∏_{x∈V_0}ρ_x(τ'_x)/ρ_x(τ_x)`, which lies in `(0,∞)` by full support. Let `B⊂dom S` be Borel with `ν(B)>0`. Some `Ξ_k∩F^{-1}(B)` has positive probability. Its image under `Ψ_k` has positive probability and lies in `F^{-1}(S(B))` by (b) and (c). So `ν(S(B))>0`. The same argument for `S^{-1}` gives the converse. ∎

### RC-A3a. Finitary coding does not imply finite change

Let `(ξ_n,η_n)_{n∈Z}` be i.i.d., `ξ_n` a fair bit, `η_n∈{1,2,…}` independent of it with `P(η_n≥k)=1/k`. Put `X_n=ξ_{n−1}⊕⋯⊕ξ_{n−η_n}`. Then `X_n` is determined by the inputs at the sites `n−η_n,…,n`, a finite window almost surely, so `X` is a finitary iid coding. Resample the input at `0`. With probability `1/2` the bit `ξ_0` changes. Then `X_n` changes for every `n≥1` with `η_n≥n`. These events are independent and `Σ_n1/n=∞`, so by the second Borel-Cantelli lemma infinitely many occur almost surely. So with probability `1/2` infinitely many outputs change. ∎

### RC-A3b. A coding-radius criterion for Lemma 6.1

Let `ξ=(ξ_v)_{v∈V}` be independent, with `V` countable and `d` a graph distance. Let `Y=(Y_ℓ)` take values in `Ω_ice`. Suppose there are Borel `R_ℓ` with the following property: for almost every `ξ`, `R_ℓ(ξ)<∞`, and `Y_ℓ(ξ'')=Y_ℓ(ξ)` for every `ξ''` that agrees with `ξ` at all `v` with `d(v,ℓ)≤R_ℓ(ξ)`. If `Σ_ℓP(R_ℓ≥d(ℓ,J))<∞` for every finite `J⊂V`, then resampling `J` changes finitely many arrows almost surely, and the law of `Y` is tail-trivial.

*Proof.* Let `ξ'` agree with `ξ` off `J`. If `R_ℓ(ξ)<d(ℓ,J)`, then `ξ'` agrees with `ξ` within distance `R_ℓ(ξ)` of `ℓ`, so `Y_ℓ(ξ')=Y_ℓ(ξ)`. By the first Borel-Cantelli lemma, almost surely only finitely many `ℓ` have `R_ℓ(ξ)≥d(ℓ,J)`. Lemma 6.1 applies. ∎

If the `R_ℓ` have one law on each of finitely many link orbits, `#{ℓ : d(ℓ,J)≤r}=O(r^3)` makes `E[R^3]<∞` sufficient on `Z^3`.

### Four-test check of the statements named here

These are questions and closures, not readings. None is proposed for adoption.

| Statement | (1) fixes a target | (2) open-ended | (3) settles physics by premise | (4) unneeded structure or constant | Result |
|---|---|---|---|---|---|
| ICE-U(R4) | no: restates the open core of `VC1_5.md` line 221 | no: a fixed statement | no: used only as a hypothesis | no | pass |
| A2-FIN | no: a lemma toward ICE-T | no: `ρ_0` is quantified, not fixed | no: used only as a hypothesis | no: no constant is chosen | pass |
| RC-T, RC-σ, RC-6.2, RC-A2, RC-A3a, RC-A3b | no | no | no: mathematics from stated premises | no | pass |

---

## 7. Required edits

Required (E1-E11). None changes a theorem's content.

- **E1** (line 7). Replace "The R4 limit is pure on the invariant algebra exactly when its ice law is tail-trivial." by "For each R4 limit point `ω`, `ω∘E` is pure on the invariant algebra exactly when its ice law is tail-trivial."
- **E2** (line 7). Replace "The deterministic transition-system construction fails" by "The `G`-invariant deterministic transition-system construction (A1) fails".
- **E3** (line 9). Replace "Neither establishes quasi-invariance." by "A3 does not address quasi-invariance. For A2, quasi-invariance and tail triviality follow from almost-sure finiteness of all trails (referee closure RC-A2); A2 is open exactly at A2-FIN."
- **E4** (line 11). Add ICE-U(R4) and A2-FIN to "Open by name", with the statements of section 8.
- **E5** (line 47). After "occupy flavours `1,…,p`" add: "On a link with high end `h`, the end `h` has number `a+1` and the other end has number `a`." After the definition of `E_x^{jk}` add: "`T↦G_x^T` is extended complex-linearly."
- **E6** (lines 43, 108, 120, 128). At each tail transfer add: "By referee closure RC-T, `ν` is tail-trivial exactly when its shadow is." At line 108 this replaces "The shadow map is injective and preserves the outside-coordinate σ-algebras on its image, so `ν` is tail-trivial."
- **E7** (line 144). Replace "the 3-cycle moves every such pair" by "the 3-cycle maps such a pair to a different pair in the same triple, sharing a link with it, and a pairing contains at most one pair inside a 3-set". Replace "All trails are therefore infinite." by "Every pair joins an even and an odd link, so every trail contains an even link. `G` is transitive on even links and permutes the trails, so all trails are infinite (`VC1_5.md` line 136)." Cite `VC1_5.md` Theorem 2.2 for the stabilizer in the first sentence.
- **E8** (line 146). Replace "and quasi-invariance is not checked" by "Given A2-FIN, the law is quasi-invariant and ICE-T follows (referee closure RC-A2). The GAP is exactly A2-FIN." The `[check]` sentence of §4.2 may be added, marked `[check]`.
- **E9** (line 148). After "finitary coding alone does not imply it" add "(referee closure RC-A3a)". Add: "If the coding radius `R` satisfies `Σ_ℓP(R_ℓ≥d(ℓ,J))<∞` for every finite `J`, for instance `E[R^3]<∞`, Lemma 6.1 gives tail triviality (referee closure RC-A3b; compare Galicza-Pete, arXiv:2406.09232, Proposition 4.3, `unchecked`)."
- **E10** (line 174). Add the π-λ theorem, Stone-Weierstrass and the Borel-Cantelli lemmas to the inputs. Replace "The finite-volume and group-geometry results are cited frozen inputs" by the list: `VC1_5.md` Theorems 2.1, 2.2, 3.1(a), 5.3, the proof of 6.1, Corollary 5.6, R1, R4; `LW1_5.md` Theorem U and B1-U; `LZ1.md` RC1(c)(iii).
- **E11** (line 35). After "A pure state is sharp on central projections" add "(`VC1_5.md` Theorem 3.1(a))". After "The lifts carry `P_λ(x)` to `P_λ(gx)`" add "(`VC1_5.md` Theorem 2.2)".

Optional (O1-O3).

- **O1** (line 62). Add: "In fact `σ_C=+1` (referee closure RC-σ)."
- **O2** (lines 132, 134). Replace "Under ICE-T" by "For `ω_ν` with any `G`-invariant quasi-invariant `ν`, in particular `ω∘E` for every R4 limit point `ω` (Theorem 5.3)". §2.3 note 3 gives the reason.
- **O3** (line 130). Name the statement ICE-U(R4) there.

For the lead, outside this file's scope. When the dated amendment enters `VC1_5.md`, its lines 9 and 146 (the route-3 GAP), 148 (LW1-5U-Σc-odd) and 221 ("What remains of route 3") can point to Theorems 4.3, 5.3 and 7.1. This report edits no file but itself.

---

## 8. Open statements to carry, by name

- **VC1-5U-odd.** Open. It follows from ICE-T at fillings 0 and 5 for every odd `m` (Theorem 5.1). At `m∈{1,9}` and fillings 0 or 5 it implies ICE-T⁻ (Theorem 5.2). Fillings 1-4 are not reduced.
- **ICE-T, ICE-T⁻, ICE-U, ICE-QI.** Open, as defined at line 22.
- **ICE-U(R4)** (name given here). "Some local weak-* limit point of the R4 states of `VC1_5.md` has a tail-trivial arrow law." By Theorem 5.3 it is equivalent to: some R4 limit point `ω` has `ω∘E` pure on `A^gauge`, which is the open core named at `VC1_5.md` line 221. It implies ICE-U.
- **A2-FIN** (name given here). "For some stabilizer-invariant full-support law `ρ_0` on the 15 pairings at a site, the i.i.d. `G`-transported random transition system has only finite trails almost surely." By RC-A2 it implies ICE-T. `[check]` guides against it for the uniform law and the four orbit-uniform laws (§4.2).
- **LW1-5U-Σc-odd.** Open. Theorem 7.1 gives necessary conditions.
- Unchanged: P-existence with a plaquette class, on both laws; the PS-7r sea continuation of VC1; VC1-i; TM1-i; LW1-5U-PS7 (owner); LW1-5-BG; LW1-5-X; GA1-P-5; LW1-5-RQ (owner); stability, excitations and energy density of full VC1.

---

## 9. Freeze recommendation

**Freeze `VC1_5U_ODD.md` after edits E1-E11.** The edits are one wording fix, citations and four short inserted closures. No theorem's statement or content changes. The two items the lane brief names are decided: the purity-tail equivalence is CORRECT (Theorems 4.3 and 5.3, §3.1), and Proposition 6.2 is CORRECT (§3.2, RC-6.2). Every import from `VC1_5.md`, `LW1_5.md` and `LZ1.md` applies as quoted (§5); no frozen input gets a `wrong` signal. The item may then enter `VC1_5.md` by a dated amendment. The referee closures RC-T, RC-σ, RC-6.2, RC-A2, RC-A3a and RC-A3b have had only this check.

---

## FINISH

**Proved (this session; each closure has had only this check).**
- Verdicts on all 83 items of `VC1_5U_ODD.md`: 78 CORRECT, 1 ERROR (item 3, status wording), 4 INCOMPLETE (items 24, 68, 70, 82), each with its fix.
- The purity-tail equivalence holds as Theorems 4.3 and 5.3 state it: for every quasi-invariant `ν`, and for each R4 limit point separately (§3.1).
- Proposition 6.2 holds: exactly three `G`-invariant transition systems exist, all their trails are bi-infinite, and the fair-coin law is `G`-invariant and not tail-trivial (§3.2, RC-6.2).
- RC-T: tail triviality passes between `Ω_ice` and the number shadow in both directions, via `(∩_nF_n)|_Ω=∩_n(F_n|_Ω)`.
- RC-σ: every loop operator acts with sign `σ_C=+1`.
- RC-A2: if A2-FIN holds, the A2 law is `G`-invariant, tail-trivial and quasi-invariant; so A2-FIN implies ICE-T.
- RC-A3b: a summable coding-radius tail (`E[R^3]<∞` suffices on `Z^3`) gives the hypothesis of Lemma 6.1.
- Every import from `VC1_5.md`, `LW1_5.md` and `LZ1.md` was checked by line and applies (§5).

**Counterexamples.**
- RC-A3a: a finitary iid coding on `Z` in which resampling one input changes infinitely many outputs with probability `1/2`. So finitary coding does not imply the finite-change property of Lemma 6.1.
- Proposition 6.2 (re-verified): the fair-coin law of any `G`-invariant transition system is a `G`-invariant ice law that is not tail-trivial.
- No frozen claim is contradicted.

**Open by name.** VC1-5U-odd; ICE-T; ICE-T⁻; ICE-U; ICE-QI; ICE-U(R4) (named here; the open core of `VC1_5.md` line 221); A2-FIN (named here); LW1-5U-Σc-odd; P-existence with a plaquette class on both laws; the PS-7r sea continuation of VC1; VC1-i; TM1-i; LW1-5U-PS7 (owner); LW1-5-BG; LW1-5-X; GA1-P-5; LW1-5-RQ (owner); stability, excitations and energy density of full VC1.

**What changes downstream.**
- `VC1_5U_ODD.md` can freeze after E1-E11 and enter `VC1_5.md` by a dated amendment.
- The route-3 GAP of `VC1_5.md` is now an exact classical statement, ICE-U(R4).
- ICE-T has one more sufficient condition, A2-FIN, a statement about random loops on `Z^3` alone. `[check]` runs guide against it for five natural laws.
- `LZ1.md` RC1(c)(iii) applies, without ICE-T, to `ω∘E` for every R4 limit point `ω` (§2.3 note 3). Under PS-3c, PS-4, proposed PS-3h5 and the joint Born identification, each of these states, taken as the initial state, forms records of value 0 at every site at tick 1.
- No law, reading, axiom or working-set entry changes. Both five-mode laws stay live. Nothing is adopted.
