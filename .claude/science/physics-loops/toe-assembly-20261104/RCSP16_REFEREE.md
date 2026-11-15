lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# RCS-P16 referee report. Straight-string spinor-class sectors

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini. This is pass 3, the referee, under PR #10138's method. The dispatch template calls the lane "pass 1"; the lane brief assigns pass 3. The report checks `RCSP16.md` (pass 2, Codex gpt-6.1-terra distillation) against its pass-1 source `RCSP16_DRAFT.md` (Claude, Mac mini) and the frozen inputs it cites. It edits no other file. It adopts nothing.

**Sources read** (branch `claude/toe-assembly`, commit `d45f92869` unless stated). Paths are relative to `.claude/science/physics-loops/toe-assembly-20261104/`.

- `RCSP16.md` (target; all 112 lines, line by line), `RCSP16_DRAFT.md` (pass 1; all 294 lines), `prior/RCSP16.md` (prior-work digest; all).
- Format models: `LW1_REFEREE.md` (lines 1-80), `Y2W_DRAFT.md` (head).
- Cited inputs, by line: `CG16B.md` 1-29, 39, 57-90, 116-186; `RCS1.md` 26-32, 68-129, 161-169, 207, 217-219; `LZ1.md` 14-46, 62; `TOE_ASSEMBLY.md` 201-203, 221-237; `LW1_5.md` 210-218, 266-276; `LW1.md` 72; `CG16S.md` 5, 9 and grep hits in 96-140, with 140 in full; `CG16S_REFEREE.md` (grep hits on RC-W and scope); `CG16D.md` 5-7, 69-81, 159; `ZM1_OBS.md` 5, 76-80 and its section heads.
- `origin/main` at `f5af11cd0` (read with `git show` after `git fetch -q origin main`): the two notes credited at `RCSP16.md:110`, lines 266-272 and 44-50.

**Working-set entries used.** NN-a (`TOE_ASSEMBLY.md` §3.7); R-CS^str with `χ_tot` (owner working candidate, not adopted); R-16^str′ (owner candidate, not adopted). Details in "Prior work used". Nothing is adopted. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.

**Referee.** Claude Opus 5.5 (model id `claude-opus-5-5`), headless, max effort, 2026-11-07. This session wrote neither pass 1 (`RCSP16_DRAFT.md`) nor pass 2 (`RCSP16.md`). This is one check: one whole-part, line-by-line read. No review of this review was commissioned.

**Text read.** `RCSP16.md` at commit `d45f92869` (the last commit that touches it, and the branch head when read). SHA-256 of the file read: `68d168a5050ffce60266e0f226304d7b8c7cb12b93d4163c299d6e6f1c5f0ff5`. Line numbers below refer to that file. The pass-1 source `RCSP16_DRAFT.md` (last touched at `11f25ee70`) has SHA-256 `bb76c7b17a3ef223ac9ce9051e14dd139e6f20dc92f627a96b217f0598030568`, and `prior/RCSP16.md` has `6ec6879ccada61d324d5a7907e69b5aac3e6328060dab5f7a49d034aefe34d5e`. Both equal the hashes that `RCSP16.md:13` records.

**Method.** Every proof was re-derived by hand. No `[check]` was run; every step below is a finite algebraic identity or a short operator-algebra argument. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix); INCOMPLETE (a named missing step). A "referee closure" is a short complete argument for a missing step. Quotations from cited files were compared with the files at `d45f92869`.

**Counts.** 49 items: 45 CORRECT, 2 ERROR, 2 INCOMPLETE. The six distiller definitions count as six items. No ERROR or INCOMPLETE item changes the content of a theorem. One ERROR (item 4) is a false correction of pass 1; the other (item 37) is a wrong pointer. Four referee closures (N2, N4, N6, N8) and one explicit example (N9) are in §3.

**Outcome in brief.** Every decision asked for comes out as `RCSP16.md` states it (§2). The distiller's correction 1 is real; correction 2 is not. Freeze after edits E1-E9 (§5, §7).

---

## 1. Verdict table

| # | Item (`RCSP16.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status line (5) | CORRECT | |
| 2 | §0 "Proved, subject to the cited inputs" (7) | CORRECT | Each clause is proved below: Theorems 1-2 (update, state), 3 (labels), 7 (band, node, `N`), 8 (no cone), 9 (flatness), 10 (RC-W). |
| 3 | §0 correction 1: endpoint condition in pass-1 Lemma A.3(a) (9) | CORRECT | The gap is real at the level of the statement; pass 1's proof already used the right condition. See note N1. |
| 4 | §0 correction 2: "a light cone of `B` contains every gate in `G_x`; that need not hold ..." (9) | ERROR | The containment holds for the cone that `α^{-1}(B)` uses. The draft's general vector form is true. Fix and proof in note N2. The narrower replacement at line 62 is also true. |
| 5 | §0 last two sentences of the correction paragraph (9) | CORRECT | |
| 6 | §0 Open (11) | CORRECT | |
| 7 | §0 Provenance (13) | CORRECT | Both recorded hashes match the files at `d45f92869`. |
| 8 | §1 preamble: witness, `E`, `p_{ℓ,x}`, `z_x` (17) | CORRECT | `z_x` matches `CG16B.md:151`. Link-purity is defined at `CG16B.md:26` and (F) at `CG16B.md:39`; §6 uses them. Pointer edit E5. |
| 9 | Def. 1: circuit, LZ1 class, NN-a, D1, band, node, `N_j` (19) | CORRECT | Matches `LZ1.md:34,40,42`, `RCS1.md:30` and `TOE_ASSEMBLY.md:235`. On the witness, "LZ1's class" means LZ1's template with the witness base tick `M_oM_e` (no electric layer, `CG16B.md:65`). |
| 10 | Def. 2: straight strings and string states (20) | CORRECT | Matches `CG16B.md:130-131` and `RCS1.md:84-89`. |
| 11 | Def. 3: `χ_tot`, boundary label, R-16^str′ (21) | CORRECT | R-16^str′ as quoted at `CG16B.md:179` also asks for a parity-sharp background sharp in every `z_x`; `ω'` and `ω_Φ` are both. Edit E6 adds the clause. |
| 12 | Def. 4: matter-activated gate (22) | CORRECT | Scope: with `S=∅`, `Π^-_∅=1`, so a matter-activated gate with no matter support is the identity. Nontrivial link-only layers (electric, plaquette, swap) are outside the class. See note N7. |
| 13 | Def. 5: background `ω'` and comparison state `ω_Φ` (23) | CORRECT | `ω_Φ` matches `CG16B.md:148`. |
| 14 | Def. 6: projected update `U=S_eS_o` (24) | CORRECT | |
| 15 | Theorem 1 statement (28) | CORRECT | |
| 16 | Theorem 1 proof (30) | CORRECT | Re-derived in note N3. |
| 17 | Theorem 2 statement (32) | CORRECT | |
| 18 | Theorem 2 proof, gate properties (34) | CORRECT | |
| 19 | Theorem 2 proof, cell lift (36) | CORRECT | Needs the per-edge sign identity; `LW1_5.md` B1-U states it per edge ("converts each transformed edge sign into the sign of the image edge, including reversed edges"). |
| 20 | Theorem 2 proof, exact NN compilation (38) | CORRECT | `CG16B.md:76` (NN-W(a) proof) uses only evenness, gauge invariance, edge-triple support and finite dimension of the twelve terms; the projected terms have all four. |
| 21 | Theorem 3 statement (42) | CORRECT | |
| 22 | Theorem 3 proof, norm and limit (44) | CORRECT | Uses the corrected endpoint condition (N1). |
| 23 | Theorem 3 proof, centre values and labels (46) | CORRECT | Hypotheses of `CG16B.md` Proposition L (lines 137-141) hold: (F), link-purity (`CG16B.md:69`, endpoint product `(−1)^{16}=1`), D1, `ω'(z_y)=1`, `ω'(P_Λ)=(−1)^{|Λ|}`, strings matter-odd and commuting with `z_y` off the far end (`CG16B.md:131`). "Every local `A∈𝔄^G` is even" is `CG16B.md:88` ("matter-even"). R2(a)'s proof (`RCS1.md:165`) uses only a norm-one net, so it transfers to `φ_Λπ(F_{∂Λ})`. |
| 24 | Theorem 3 proof, transverse disjointness (48) | CORRECT | `RCS1.md` Lemma 6 (line 93) needs each cyclic vector to be eventually an eigenvector of `X_t`; here `X_t=p_{ℓ_t,y_t}` has eigenvalue 1 at `Ω_x` for every `t≥1` and 0 at `Ω_{x'}`. |
| 25 | Theorem 4 statement (52) | CORRECT | |
| 26 | Theorem 4 proof (54) | CORRECT | Compressed. The sentence "inserting the remaining gates" is the right step; note N4 writes it out in four lines. |
| 27 | Theorem 5 statement (56) | CORRECT | |
| 28 | Theorem 5 proof, one link (58) | CORRECT | Re-derived, including operator order and the factor 16 (note N5). |
| 29 | Theorem 5 proof, two layers (60) | CORRECT | Tiling parity: "a direction-1 link belongs to the even or odd tiling according to the parity of its base coordinate \(x_1\)" (`LW1_5.md:218`; pass 1 cites line 216 of an earlier revision). The link `(x−e_1,x)` with `x_1` even has odd base coordinate, so it is in an odd cube, as stated. `exp(−iπ·4ησ_x/8)=−iησ_x` checked. |
| 30 | Vector form (62) | CORRECT | Valid as stated for `U`. Pass 1's general form is also valid (N2). |
| 31 | §5 set-up and three state identities (66-67) | CORRECT | "For even `x`" must mean `x∈2Z³`; the identities use `κ` constant on `2Z³` and Theorem 5's hypothesis `x_1` even at `x+2e_1`. Edit E7. |
| 32 | Theorem 6 statement (69-74) | CORRECT | Convention `Ũπ(A)Ũ*=π(αA)` matches `RCS1.md:30` (Definition 5). |
| 33 | Theorem 6 proof, isometries and range (76) | CORRECT | |
| 34 | Theorem 6 proof, commutation (78) | CORRECT | Re-derived: `π'(D)ψ̂_x=κ²ψ̂_{x+4e_1}−κ²ψ̂_{x+4e_1}=0`, using `Ûψ̂_y=κψ̂_{y−2e_1}` at `y=x+2e_1` and `y=x+4e_1`. |
| 35 | Theorem 7 statement (80) | CORRECT | Band, node and generator in the sense of `LZ1.md:42` and `RCS1.md:30`; the band "propagates" in LZ1's sense (`N_1≠0`). |
| 36 | Theorem 7 proof (82) | CORRECT | Orthogonality on one line: `P_{2b}` is sharply `+1` in `ω_{2b}` and sharply `−1` in `ω_{2b'}`, `b'_1≠b_1`, since every non-head site of a string state carries `|i_0⟩`. |
| 37 | Paragraph after Theorem 7: conventions (84) | ERROR | Content correct (rephasing `Ũ↦μŨ`, `T_{e_1}↦νT_{e_1}` gives `V=μν̄e^{iK_1}`; `N` unchanged). The pointer "(`ZM1_OBS.md` §0)" is wrong: the quoted point is `ZM1_OBS.md:80`, "GAP C-law" in §2; §0 has no such statement. Edit E3. |
| 38 | Theorem 8 (86-88) | CORRECT | `LZ1.md:42`: "A **Clifford cone** has `{N_i,N_j}=2v²δ_ij` for `v>0`." For `d=1`, `N_1²=N_2²=v²>0` contradicts `N_1N_2=0`. |
| 39 | Theorem 9 statement (92) | CORRECT | Ray limits for `ω'` along `+e_1` only; for `ω_Φ` along every `+e_j` (all links `(16,0)`). |
| 40 | Theorem 9 proof (94) | CORRECT | Port of `RCS1.md` Theorem 8(d) and Corollary 9 (lines 123-127); `CG16B.md:126` records that Corollary 9 "applies to covariantly chosen ray sectors when its disjointness and tick-equivalence hypotheses hold". The plane statement cites `CG16D.md` Lemma N, which `CG16D.md:71` marks "(unrefereed)"; note N6 rebuilds it from `RCS1.md` Lemma 5.1. |
| 41 | Paragraph after Theorem 9 (96) | CORRECT | It correctly weakens pass 1's "Any route to MT1-S must make the string's transverse position unobservable ... or act on the far ray" to "routes to test". |
| 42 | Theorem 10 statement (98) | CORRECT | |
| 43 | Theorem 10 proof (100) | CORRECT | `CG16S.md` is now frozen with RC-W inside it: Weyl point needs "`dim ker(V(K₀)−1)=2`" (`CG16S.md:96`); RC-W at `CG16S.md:120`; scope at `CG16S.md:140`: "This leaves open ... defects over a filled or entangled background, and node sets that are infinite or not all Weyl. Setting F has no links". Edit E8 cites the frozen file. |
| 44 | Remark on shifts and finite depth (102) | CORRECT | Not used in any proof. |
| 45 | §7 checks, first sentence: LZ1 Theorem 2.2 does not apply (106) | INCOMPLETE | The claim is true. The reason "(`RCS1.md` R2)" does not suffice: R2(b) gives `χ_tot=−1` also on `H_odd` of the background GNS (`RCS1.md:167`). The separating fact is the trivial centre pattern. Fix in note N8, edit E4. |
| 46 | §7 checks, other sentences (106) | CORRECT | `P_Λ` is not central in `𝔄^G`: a hop across `∂Λ` anticommutes with it. |
| 47 | §7 readings and four tests (108) | CORRECT | Recorded values match `RCS1.md:207` (R-CS^str: P, C, C, C) and `CG16B.md:178-179` (R-16^str: P, F, P, P; R-16^str′: P, C, P, P). The restriction's P, F, C, F is confirmed; note N9 gives an explicit test-2 example. |
| 48 | §7 prior work (110) | INCOMPLETE | Omits three inputs used in proofs: `CG16S.md` RC-W (Theorem 10), `CG16D.md` Lemma N (Theorem 9) and `LW1_5.md` B1-U (Theorem 2). Edit E9. |
| 49 | §7 named open routes (112) | CORRECT | |

---

## 2. The decisions asked for

**D1. The update is in LZ1's class and meets NN-a, with the inverse layers. Yes.** `LZ1.md:34` asks only this of an appended layer: "a family of finite-support gates that is closed under the even translations and has finitely many gates per cell. The gates of a layer commute pairwise, and each gate commutes with every local gauge transformation". `M_o^{-1}`, `M_e^{-1}`, `S_o` and `S_e` each satisfy it. The quoted text does not forbid a layer equal to the inverse of a base layer. For NN-a (`TOE_ASSEMBLY.md:235`), each `t_C` is an exact finite word in even, gauge-invariant edge-triple unitaries: the proof of NN-W(a) (`CG16B.md:76`) uses only evenness, gauge invariance, edge-triple support and finite dimension of the twelve terms, and each `η_iQ_ℓh_ℓQ_ℓ` has all four. The complete update fixes every local generator. Cell covariance holds layer by layer: the lift sends each signed hop to the signed image hop (`CG16B.md:69`, with `LW1_5.md` B1-U per edge), it maps end numbers to image end numbers, `Q_ℓ`'s set `{(16,0),(15,1),(1,15),(0,16)}` is closed under exchanging the ends, and the lift preserves each tiling. NN-a is read with the witness register, as in `CG16B.md:74`; this reading is inherited, not new.

**D2. The D1 product state is locally gauge invariant. Yes.** The local transformation at `y` acts only on the star of `y`. It fixes each star factor: `|i_0⟩` (since `S_+⊕1` is trivial on `H_-`), the empty end, the full end (`det S_+(g)=1`), and each `σ`, because `W(Λ⁸g⊗Λ⁸g)=det(g)W`. Two facts make "product over stars" exact. (i) Every operator on a fixed-number link register is rishon-even, so operators on different links commute whatever the sign convention between links. (ii) Every matter factor is a parity eigenvector, so the infinite product of matter states is an even product state of the CAR algebra. The state is also invariant under all translations, has sharp `P_x=−1` and `z_x=+1` (end numbers `0,16,8,8,8,8`), and is fixed by every matter-activated gate. So it is D1 for every matter-activated update (`LZ1.md:40`).

**D3. The straight `+e_1` string sectors have `χ_tot=−1`, boundary label `−1`, and are spinor class under R-16^str′. Yes.** This is `CG16B.md` Proposition L(i)-(iii) with `ω=ω'`; its hypotheses hold (item 23). A direct check: take a finite string with far end outside a finite `Λ∋x`. The string crosses `∂Λ` an odd number of times. Each crossing link has end number 15 or 1 at its inner end, so `F_{∂Λ}=−1` on the string vector, against `+1` in `ω'`. R-16^str′ reads "Spinor class means the limit is `-1`" (`CG16B.md:179`). R-16^str′ is an owner candidate, not adopted. The label does not establish an irreducible 16 (`CG16B.md:182`).

**D4. The band. Correct.** `V(K)=e^{iK_1}`, with `d=1`. The node set is `{K:K_1∈2πZ}`, the plane `K_1=0` of `T³`. With `N_j=∂_j(i log V)(K₀)` (`LZ1.md:42`), `N=(−1,0,0)` at every node. The band propagates in LZ1's sense. Rephasing `Ũ` or `T_{e_1}` moves the node plane and leaves `N` unchanged. So the existence of a node and `N_1≠0` do not depend on the phase choice that `ZM1_OBS.md:80` leaves open.

**D5. Proposition B (Theorem 9) and its failing step. Correct.** The failing step for a Clifford cone is named correctly: a Clifford node needs a nonzero transverse generator, and in this class none exists. The far ray's transverse position is a sharp asymptotic label (target-end numbers far along the line). It separates sectors (`RCS1.md` Lemma 6), and every matter-activated update preserves it (Theorem 4). These are the two hypotheses of `RCS1.md` Corollary 9. Scope: the class contains no nontrivial link-only layer (note N7). Theorem 9 says nothing about updates with electric, plaquette or swap layers, which act on the far ray.

**D6. RC-W forces no mirror partner here. Correct, as a statement about RC-W.** RC-W (`CG16S.md:120`) proves `W₃=0` for a finite-depth translation-covariant walk on a single-particle space. Its pairing use (`CG16S.md:140`) needs a finite node set of Weyl points, and a Weyl point needs `dim ker(V(K₀)−1)=2` (`CG16S.md:96`). The band has a planar node set and one-dimensional kernels. So it has no Weyl point, and the pairing statement has nothing to pair; it neither asks for nor excludes a second band. The band's own `W₃` is zero. The string sector is also outside setting F (links, filled and entangled background). This is not a theorem that charged sectors carry no mirror constraint; line 100 says so.

**D7. The two distiller corrections.** Correction 1 is real at the level of the statement and does not affect the limit (N1). Correction 2 is not real: the containment it doubts holds (N2).

**D8. The four tests of the restriction "appended layers may not undo base layers". Correctly assessed: P, F, C, F.** Note N9 gives an update `U'` in which no layer is the inverse of a base layer, and which acts on every string sector exactly as `U`. A literal restriction therefore does not remove the witness. An effective one must decide case by case which sector-wise cancellations count. That is open-ended, so test 2 fails.

---

## 3. Notes and referee closures

**N1 (correction 1; items 3, 22).** Pass-1 Lemma A.3(a) reads: "`ω_r^{(x)}(A)` is constant in `r` once `y_{2r}` is outside the sites of `A`'s support". *Counterexample.* Take `A=p_{ℓ_{10},y_{10}}`, the target-end number of the tenth string link; it is gauge invariant with sites `y_9,y_{10}`. For `2r<10` the link is in its background `(16,0)` and `ω_r(A)=0`; for `2r≥10` it is a string link and `ω_r(A)=1`. The endpoints `y_8` (`r=4`) and `y_{12}` (`r=6`) both lie outside `{y_9,y_{10}}`, yet the values differ. Pass 1's proof already assumes the right condition: "a local `A` whose support lies in sites `y` with `y_1<x_1+k`, `k<2r`". Theorem 3 states the repaired version. The limit is unaffected.

**N2 (correction 2; items 4, 30). Referee closure: the containment holds.** Write the update as `L_k⋯L_1`, with `L_1` first in time, so `α^{-1}(B)=UBU^*`. Put `D_0=supp B`. Let `Y_j` be the gates of `L_j` that meet `D_{j−1}`, and `D_j=D_{j−1}∪supp Y_j`. Gates of `L_j` outside `Y_j` commute with the partly conjugated `B` and cancel, so `α^{-1}(B)=YBY^*` with `Y=Y_k⋯Y_1`. Claim: `R_j⊆D_j`. Indeed `R_0={x}⊆D_0`, since `B` contains `E_{x,ai_0}`. If `R_{j−1}⊆D_{j−1}`, a gate of `L_j` that meets `R_{j−1}` meets `D_{j−1}`; so it lies in `Y_j`, and its sites lie in `D_j`. Hence every gate of `G_x` lies in `Y`, as pass 1 says. The other gates of `Y_j` miss `R_{j−1}` and fix the current vector. So `Û_𝒱ψ=π'(G_x)ψ` for every matter-activated `𝒱`. The distiller's worry is valid for the backward cone of `α(B)=U^*BU`, which is built from `L_k` down; the vector form does not use that cone.

**N3 (Theorem 1; item 16).** `W≠0`, so `σ` is defined. For unitary `g` with `det g=1`, `W∘(Λ⁸g⊗Λ⁸g)=W` gives `(Λ⁸g⊗Λ⁸g)^{-1}W^*=W^*`, hence `(Λ⁸g⊗Λ⁸g)σ=σ`. `det S_+(g)=1` holds because `Spin(10)` is connected and semisimple; `CG16B.md:150` gives a trace proof. On a fixed-number link sector the endpoint action at `y` is even in the `y`-end modes, so it commutes with the other end's modes and acts as `1⊗Λ^p S_+(g)` on the ordered product. The hop terms end in `E^†_{x,βi}` or `E^†_{y,αi}`, each zero on `H_-`, so every base gate and its inverse fixes the all-`H_-` subspace for any link state.

**N4 (Theorem 4; item 26). The four-line form.** Fix local `A` and its backward cone `Y=Y_k⋯Y_1` for `α_𝒱`, so `α_𝒱(A)=Y^*AY`. Let `g_j` be the gates of `L_j` that meet `R_{j−1}`, so `G_x=g_k⋯g_1`. Put `Z_j=Y_j∪g_j` and `Z=Z_k⋯Z_1`. (a) `Z^*AZ=Y^*AY`: a gate of `Z_j` outside `Y_j` misses the cone region at its stage, so it commutes with the partly conjugated `A` and cancels. (b) `Zψ=G_xψ`: a gate of `Z_j` outside `g_j` misses `R_{j−1}`, and all its sites carry `P=−1` in the current vector, so it acts as the identity. Hence `⟨ψ,α_𝒱(A)ψ⟩=⟨G_xψ,AG_xψ⟩`. Sum over `b` and let `r→∞`.

**N5 (Theorem 5; item 28).** In the adjoint hop term `E_{w,βi}r^w_βr^{v†}_αE^†_{v,αi}`, the product `E^†_{v,αi}E_{v,ai_0}=δ_{αa}|i⟩⟨i_0|_v` is matter-even, so moving `E_{w,βi}` past it costs no sign, and `E_{w,βi}|i_0⟩=δ_{ii_0}|β⟩`. The link pair `r^{ℓ,w}_βr^{ℓ,v†}_a` lands in the string's own order. In reverse, `r^v_αr^{w†}_βr^w_βr^{v†}_a=n^w_β r^v_αr^{v†}_a`, which equals `δ_{αa}` on (full, empty); the sum over `β` gives 16.

**N6 (Theorem 9, plane statement; item 40). Rebuild from `RCS1.md` Lemma 5.1.** Let `B` be a ball around a node on which `V` is `C¹` and `h=i log V` has spectrum in `(−π/2,π/2)`. Lemma 5.1's proof shows that no `tr(h^p)` has a nonzero `n`-derivative on any open subset of `B`, else separability fails. The derivative is continuous, so it vanishes on all of `B`. Apply this with `n=e_2` (label `q=c_2/2`) and `n=e_3` (label `q=c_3/2`). Then each `tr(h^p)` is constant on the convex set `B∩(K₀+span{e_2,e_3})`, with value 0 at `K₀`. Newton's identities give characteristic polynomial `λ^d`, so the Hermitian `h` vanishes and `V=1` there. This is the content of `CG16D.md` Lemma N (line 71, marked unrefereed); the rebuild uses only frozen `RCS1.md`.

**N7 (scope of "matter-activated"; items 12, 39).** If a gate has no matter support, `Π^-_∅=1`, and `gΠ^-_∅=Π^-_∅` forces `g=1`. In general a matter-activated gate fixes every vector whose support sites carry `P=−1`, whatever the links hold. So the class excludes every layer that acts nontrivially on links over an all-`H_-` region: an electric layer, a plaquette layer, GA1-5's swap layers. The witness has "no electric layer" (`CG16B.md:65`), so its base tick is in the class. Updates that act on the far ray lie outside Theorem 9. This is a scope remark, not an error. Optional edit E10.

**N8 (item 45). Repaired reason.** `CG16B.md:90` splits the background GNS space into centre patterns, and under (F) and link-purity `H_odd⊂H_nt`. LZ1 Theorem 2.2 concerns bands with image in `H_nt`. Each `π_x` has trivial pattern: `π_x(z_y)=1` for all `y` (Proposition L(i)). With `π₀` the background GNS representation, every `π₀(𝔄^G)`-invariant subspace of `H_nt` is a sum of pieces on which some central `z_y` equals `−1`. An intertwiner from `π_x` to such a piece would carry the scalar 1 to `−1`, so it is zero. The trivial-pattern part `H(1)` lies in `H_even`, where `χ_tot=+1` (`RCS1.md:167`), against `χ_tot(π_x)=−1`. So `π_x` is disjoint from every subrepresentation of the background GNS representation restricted to `𝔄^G`. LZ1 Theorem 2.2 does not reach the band.

**N9 (item 47; decision D8). An explicit test-2 example.** Put `X'_C=Σ_{ℓ=(x,y)⊂C}(1+P_x)(1+P_y)/4`. Each term is an even, gauge-invariant element of one edge-triple algebra, so NN-W's argument compiles `e^{iθX'_C}` exactly. Replace each appended inverse gate `b_C^{-1}`, the inverse of a base cube gate `b_C`, by `g_C=e^{iθX'_C}b_C^{-1}`, with `θ∉2πZ`. Each new layer is in LZ1's class and is cell covariant, since the lift fixes each `P_x` up to relabelling and preserves the tilings. It is matter-activated, since `X'_CΠ^-=0`. No new layer is the inverse of a base layer. Every hop term moves the `H_+` content of one site to another, so it preserves the number of `H_+` sites. Hence every vector reached from a string vector has exactly one `H_+` site, and `X'_C` vanishes on it. On string vectors, `g_C` acts as `b_C^{-1}`, so the new update `U'` acts as `U` at every stage. Theorems 4-7 then hold for `U'` with the same `G_x`, implementers and band. A literal restriction does not remove the witness; an effective one must judge sector-wise cancellation case by case.

---

## 4. The GAPs the distiller marked

`RCSP16.md` marks one GAP paragraph (line 9). It has two corrections and two status sentences.

- **Correction 1, endpoint condition in pass-1 Lemma A.3(a). Real.** The pass-1 statement is false as written (counterexample in N1). The pass-1 proof is right, because it assumes the stronger condition. Repaired statement, as in Theorem 3: for a local `A`, `ω_r^{(x)}(A)` is constant for all `r` with `y_{2r}` beyond every site and link of `A`'s support along the ray. The limiting state, and everything after it, is unchanged.
- **Correction 2, light-cone containment in pass 1's vector form. Not real.** The containment holds for the cone of `α^{-1}(B)`, which is the cone the vector form uses (N2). The distiller's replacement, restricted to `U`, is also true, so no theorem changes. Line 9's sentence "that need not hold for a gate whose support meets the recursively enlarged active region but not the light cone of `B`" should be replaced (edit E1).
- **"The claimed construction is author-checked here, not independently refereed."** A status sentence. This report is the referee pass.
- **"The compilation result imported from `CG16B.md` is a referee closure that has not itself received a second independent review."** True: `CG16B.md:71` labels NN-W "(referee closure, CG16B_REFEREE.md)". `CG16B.md` is frozen with it.

No other line of `RCSP16.md` is marked GAP. Item 45 (a reason that does not separate the string sectors from `H_odd`) is a gap the distiller did not mark; N8 closes it.

---

## 5. Required edits

Required (E1-E9). None changes a theorem's content.

- **E1** (line 9, item 4). Replace the sentences from "The draft's general “vector form” also asserts" to "no such containment is needed." by: "Pass 1's general vector form is correct. The cone of `α^{-1}(B)` is built from the first layer upward and contains each active region `R_j`, so it contains every gate of `G_x` (`RCSP16_REFEREE.md` N2). Line 62 states the case used below."
- **E2** (line 62, item 30). Optional with E1: state the general form "for every matter-activated LZ1-class update `𝒱`, `Û_𝒱ψ=π'(G_x)ψ` on finite string vectors", with N2 as its proof. If E2 is not applied, keep line 62 as is; it is true.
- **E3** (line 84, item 37). Replace "(`ZM1_OBS.md` §0)" by "(`ZM1_OBS.md` §2, GAP C-law, line 80)".
- **E4** (line 106, item 45). Replace the first sentence by: "LZ1 Theorem 2.2 concerns bands with image in the nontrivial-pattern subspace of the D1 background GNS representation (`CG16B.md` Theorem 4.1(c)). The present representation has trivial centre pattern, `π(z_y)=1` (`CG16B.md` Proposition L(i)), so it is disjoint from that subspace. Its `χ_tot=−1` also makes it disjoint from the trivial-pattern part, which lies in `H_even` where `χ_tot=+1` (`RCS1.md` R2(b))."
- **E5** (line 17, item 8). Replace "Link purity and condition (F) are as in `CG16B.md` §6" by "Link-purity is `CG16B.md` §1 item 4 and condition (F) is `CG16B.md` Theorem 2.2(a); §6 uses both."
- **E6** (line 21, item 11). After "calls boundary label `−1` spinor class", add: "over a parity-sharp background sharp in every `z_x`, as its quoted text requires (`CG16B.md` §7); `ω'` and `ω_Φ` are both."
- **E7** (line 66, item 31). Replace "For even `x`" by "For `x∈2Z³`".
- **E8** (lines 98-100, item 43). Cite the frozen `CG16S.md`: Weyl point at line 96, Lemma RC-W at line 120, scope at line 140 ("defects over a filled or entangled background, and node sets that are infinite or not all Weyl. Setting F has no links"). Keep `CG16S_REFEREE.md` §3.1 as the origin of RC-W.
- **E9** (line 110, item 48). Add credits: `CG16S.md` RC-W (Theorem 10); `CG16D.md` Lemma N, marked unrefereed at its line 71 (Theorem 9's plane statement; rebuilt in `RCSP16_REFEREE.md` N6 from `RCS1.md` Lemma 5.1); `LW1_5.md` B1-U (Theorem 2's per-edge lift); `ZM1_OBS.md` line 80 (phase convention).

Optional (E10-E12).

- **E10** (after line 22, item 12). Add: "A matter-activated gate with no matter support is the identity. Layers acting nontrivially on links over an all-`H_-` region (electric, plaquette, swap) are outside the class."
- **E11** (line 54, item 26). Insert N4's four lines after "Gates within one layer commute."
- **E12** (line 94, item 40). After "see `CG16D.md` Lemma N", add "(rebuilt from `RCS1.md` Lemma 5.1 in `RCSP16_REFEREE.md` N6)".

---

## 6. Open statements to carry by name

- **RCS-P, Clifford form** (inherited, `RCS1.md` §8). Narrowed here: over `ω'` and `ω_Φ`, no matter-activated update gives a Clifford node (Theorem 9). Still open: updates with layers that act on the far ray (N7), other backgrounds such as fluctuating strings, and other laws.
- **MT1-S[R-CS^str] in the VC1 vacuum** (inherited).
- **R-CS and R-16^str′.** Owner candidates, not adopted. Theorem 7's spinor-class label holds under R-16^str′ only.
- **CG16D-NLP** (inherited; not worked in RCS-P16).
- **RCSP16-BT** (name proposed here for line 11's sentence "The base tick's own ray motion and a band retaining that motion are not decided"). Does the witness base tick alone, or an update that keeps it uncancelled, carry a band with a node and `N≠0` on these string sectors?
- **Owner question on LZ1's update class.** Should appended layers that undo base layers be excluded? Not proposed. Tests P, F, C, F (D8, N9).

## 7. Freeze recommendation

**Freeze after edits E1-E9.** No theorem of `RCSP16.md` is false in content. The two ERRORs are one false correction of pass 1 (item 4) and one wrong pointer (item 37). The two INCOMPLETEs are a reason that needs one more fact (item 45, closed by N8) and three missing credits (item 48). Correction 1 is a real repair of a pass-1 statement. The six decisions asked for (D1-D6) all come out as `RCSP16.md` states them. The four tests of the restriction are right (D8).

Inputs that remain referee closures inside frozen files: `CG16B.md` NN-W, Proposition L and Example S, and `CG16S.md` RC-W. N6 rebuilds the one unrefereed import, `CG16D.md` Lemma N, from frozen `RCS1.md` Lemma 5.1. This report is one check. No second independent review was run.

---

## Prior work used

Paths are in this folder at `d45f92869` unless marked `main`. Each result was re-derived or its hypotheses checked where used.

| Prior result | Path | Used for |
|---|---|---|
| Pass-1 draft; prior digest | `RCSP16_DRAFT.md`; `prior/RCSP16.md` | Source comparison; credits |
| Rishon witness, with per-edge cell lift in its proof | `CG16B.md:57-69` | Items 8, 19; D1 |
| Lemma NN-W (referee closure) | `CG16B.md:71-76` | Item 20; D1; N9 |
| Theorem 4.1(b),(c): `𝔄^G` matter-even; `H_odd⊂H_nt` | `CG16B.md:88-90` | Items 23, 45; N8 |
| Theorem 6.1 (flux identity; Corollary 9 applies on (F)-laws) | `CG16B.md:120-128` | Items 23, 40 |
| Theorem 6.2 (finite strings) | `CG16B.md:130-133` | Items 10, 23 |
| Proposition L, Example S (referee closures) | `CG16B.md:137-154` | Items 13, 23, 39; D3 |
| R-16^str, R-16^str′ tests | `CG16B.md:178-182` | Items 11, 47 |
| Definition 5 (covariant representation, band) | `RCS1.md:30` | Items 9, 32 |
| Lemma 5.1 and Theorem 5 (boost, directional flatness) | `RCS1.md:70-78` | Item 40; N6 |
| Straight strings, R-CS^str(e), Lemma 6 | `RCS1.md:84-95` | Items 10, 24 |
| Theorem 8(c),(d), Corollary 9 | `RCS1.md:101-127` | Item 40; D5 |
| R2(a),(b) | `RCS1.md:161-169` | Items 23, 45; N8 |
| Four tests; RCS-P | `RCS1.md:207,219` | Item 47; §6 |
| Update class, D1 state, band, node, Clifford cone | `LZ1.md:34-42` | Items 9, 35, 38; D1, D2, D4 |
| Theorem 2.2 (flat nodes) | `LZ1.md:62` | Item 45 |
| NN-a; R-CS owner candidate | `TOE_ASSEMBLY.md:235,225` | D1; §6 |
| Tiling parity; B1-U per-edge lift | `LW1_5.md:218,268-276` | Items 19, 29 |
| Base tick and E1 products | `LW1.md:72` | Items 9, 20 |
| Weyl point; Lemma RC-W; its scope | `CG16S.md:96,120,140` | Item 43; D6 |
| Lemma N (marked unrefereed) | `CG16D.md:71,81` | Item 40; N6 |
| GAP C-law (phase convention) | `ZM1_OBS.md:80` | Item 37; D4 |
| Charge motion without a sharp band | main `f5af11cd0`: `docs/NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md:270-271` | Item 48; quote "It does not identify a single eigenvalue, a sharp particle pole, or a nonzero curvature of the lowest band" matches |
| Mobile bosonic toric-code charges | main `f5af11cd0`: `docs/THREE_AXIS_QUBIT_SITE_STABILIZER_RULES_UNSOLDERED_TORIC_CODES_MOVE_SOLDERED_MAXIMAL_RULES_DO_NOT_BOUNDED_THEOREM_NOTE_2026-10-17.md:46-48` | Item 48; quote "The charges are bosons, those of the 3D toric code" matches |

**Prior work the digest missed, or that changed after it was written.**
1. `CG16S.md` is frozen ("FROZEN 2026-11-07 after pass 3", line 5) with RC-W at line 120 and its scope at line 140. The digest describes RC-W as a referee closure in `CG16S_REFEREE.md` awaiting freeze checks.
2. `CG16D.md` is frozen (line 5, 2026-11-07) and contains Lemma N at line 71, marked "(unrefereed)". The digest says its header "still says 'Pass 2; not refereed or frozen'".
3. `CG16B.md:126` records that `RCS1.md` Corollary 9 "applies to covariantly chosen ray sectors when its disjointness and tick-equivalence hypotheses hold" on (F)-laws. This is the bridge Theorem 9 uses.
4. `LW1_5.md:218` states the tiling parity rule that Theorem 5 uses.

The other main-branch and consolidation-PR notes the digest names bear on context, not on any proof step of `RCSP16.md`; they were not reread.

**Working-set entries used.** NN-a (`TOE_ASSEMBLY.md` §3.7, owner 2026-11-06), read with the witness register as in `CG16B.md:74`. R-CS^str with `χ_tot` over parity-sharp backgrounds (owner working candidate, not adopted, §3.6). R-16^str′ (owner candidate, not adopted, `CG16B.md` §7). "D1 state" means `LZ1.md:40`'s definition; it is not the owner decision named D1 in `TOE_ASSEMBLY.md` §3.4, which concerns PS-5. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.

---

## FINISH

**Proved (referee side; one check, not independently reviewed).**
- Every theorem of `RCSP16.md` (Theorems 1-10) is correct as stated, subject to its cited frozen inputs. In particular: the update `U=S_eS_o` is in LZ1's class and meets NN-a read with the witness register, including the appended layers that undo the base tick (D1). The product state `ω'` is locally gauge invariant and D1 for every matter-activated update (D2). The straight `+e_1` string sectors have `χ_tot=−1` and boundary label `−1`, and are spinor class under R-16^str′ (D3). The band is `V(K)=e^{iK_1}`, with node plane `K_1=0` and `N=(−1,0,0)` (D4). Theorem 9 forces transverse flatness for matter-activated updates over `ω'` and `ω_Φ` (D5). RC-W forces no mirror partner for this band (D6).
- Referee closures: N2 (pass 1's vector-form containment holds), N4 (Theorem 4 in four lines), N6 (plane flatness rebuilt from `RCS1.md` Lemma 5.1, replacing reliance on the unrefereed `CG16D.md` Lemma N), N8 (the string sectors are disjoint from every subrepresentation of the background GNS representation, so LZ1 Theorem 2.2 does not reach them).

**Counterexamples.**
- To pass-1 Lemma A.3(a) as worded: `A=p_{ℓ_{10},y_{10}}` (N1). The distiller's correction 1 stands.
- To the distiller's correction 2: none exists; N2 proves the doubted containment.
- To "a literal ban on appended inverse base layers removes the witness": the update `U'` of N9.

**Open by name.** RCS-P in its Clifford form (inherited; narrowed by Theorem 9). MT1-S[R-CS^str] in the VC1 vacuum. R-CS and R-16^str′ (owner candidates, not adopted). CG16D-NLP. RCSP16-BT (does an update keeping the base tick's motion carry a band on these sectors?). The owner question on excluding layers that undo base layers (tests P, F, C, F).

**What changes downstream.**
- *RCS-P16.* After E1-E9 it can freeze. A propagating band with a node and `N≠0` exists on straight-string sectors of spinor class (under R-16^str′) on the U(16)-rishon witness. It is one-dimensional and not a Clifford cone.
- *RCS-P.* The remaining question is the cone, not motion. Over these backgrounds a Clifford node needs layers that act on the far ray (outside the matter-activated class, N7), or a background in which the far ray's transverse position is not sharp.
- *LZ1's update class.* N9 shows that a literal ban on inverse base layers would not remove this band. Any restriction aimed at it must judge sector-wise cancellation, which fails test 2.
- *RC-W.* Its pairing statement does not reach charged-sector bands of this kind; a chirality claim about them needs its own argument.
- Nothing is adopted. No law, reading, axiom or working-set entry changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
