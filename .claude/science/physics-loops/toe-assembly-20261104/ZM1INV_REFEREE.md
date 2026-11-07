lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# ZM1-I1[INV] referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini as pass 3, the referee, under PR #10138's method. The object refereed is `ZM1INV.md` (pass 2, Codex distillation) at commit `cc209676e`. Its pass-1 source is `ZM1INV_DRAFT.md` at the same commit. This is one check of the proof. It reviews no other review. It edits no other file.

## Method

I read `ZM1INV.md` line by line, sections 0 to 5. I checked each cited result against its source file at commit `cc209676e`. I checked each pass-2 change against `ZM1INV_DRAFT.md`. Each statement and proof step gets one mark. CORRECT means the step holds as written. ERROR means the step is false or proves less than it says; the fix follows. INCOMPLETE means the step is true but a needed argument or hypothesis is missing; the missing part follows. Where a repair is short, I give it in full in the Repairs section. Every repair is a finite argument about finite-dimensional algebras, spectra or inequalities. No step rests on a computation. I adopt no reading.

## Text read

`ZM1INV.md` as of commit `cc209676e` (the last commit that touches it; unchanged at branch head `cc209676e`). SHA-256 of the file read: `899cf9706c64fa587a85d05de7b26cfc56f0efc99f2da847ab1a50130fad06b0`. Line numbers below refer to that file.

Pass-1 source: `ZM1INV_DRAFT.md` as of commit `64655facc`, SHA-256 `078d8fd390241eb8afb23d9e4e25c12676b815cf3b653180c9a3abd6cd599e7d`. `ZM1INV.md` line 13 records SHA-256 `078d8fd3...599e7d` for pass 1.

## Sources read and working set

**Source revision.** Branch `claude/toe-assembly` at `cc209676e` (local sparse checkout). No other branch was read; see section 8.

**Files read, by line.** `prior/ZM1INV.md` (all, 94 lines); `ZM1INV.md` (all, 130 lines); `ZM1INV_DRAFT.md` (all, 278 lines); `LW1_REFEREE.md` lines 1-80 and `Y2W_DRAFT.md` lines 1-20 (format only); `TOE_ASSEMBLY.md` lines 240-256 (sections 3.8-3.9); `VC1_5.md` lines 1-60 (status, definitions, section 2, Theorems 2.1-2.2), 84-92 (Theorem 4.2), 112-130 (Theorems 5.2-5.5), 198-202 (Proposition R2); `ZM1I1A.md` lines 15-27 (definitions, Theorem 1), 76-90 (Theorems 7-9), 126-131 (RC-4 to RC-6) and its theorem list; `ZM1_OBS.md` lines 66-72 (Theorems 3-4), 114-116 and 131-133 (Theorems 8′, 9′), 167-177 (section 5.1), 284-292 (Lemma ER); theorem lists of `GA1_5.md`, `LZ1I.md`, `VC1_5U_ODD.md`, `ZM1.md`, `GA2_Y2.md`, with the statement lines quoted in the table.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The owner texts ZM1-I1[a] and ZM1-INV are read plainly. Where they leave a choice open (which coarse law for an O fine law; any symmetry of `ω₁`), the choice is named and nothing is adopted.

**Working set used, by name.** PS-5, PS-6r and PS-7r only through the two five-mode laws and the VC1 witnesses as frozen in `VC1_5.md`; the owner decisions ZM1-I1[a] (section 3.8), ZM1-INV (section 3.9) and GA1-P-NN = NN-a (through `GA1_5.md` Amendment 1). No axiom and no working-set entry changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.

**Inputs from outside the working set.** Standard mathematics, rebuilt where used: Schur's lemma; the commutant of a compact group representation; joint spectra of commuting operators on tensor factors; the Jordan-Wigner order for even elements; the fact that a finite digraph with in-degree equal to out-degree at every vertex has a directed cycle if it has an edge. No literature is used.

## 1. Verdict table

Rows follow `ZM1INV.md` in file order. The section 0 summary lines 7, 9 and 11 depend on the whole body, so their rows come last (rows 50 to 52).

| # | Item (ZM1INV line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status line (5) | CORRECT | No mathematical claim. |
| 2 | §0 provenance (13) | CORRECT | The pass-1 hash `078d8fd3…599e7d` matches `ZM1INV_DRAFT.md` at `64655facc`. Pass 1 reports revision `b2690b690` (`ZM1INV_DRAFT.md` line 9). The pass-2 model identity is deferred to a run log; I cannot check it here. |

(Table continues below after the source checks; the comparison of passes is placed here because rows 3 onward refer to it.)

### Pass-1 to pass-2 changes that the rows check

- P1. Pass 1 states the `L5-O` case of Theorem R with "a coarse `L5-O` system" (`ZM1INV_DRAFT.md` line 153). Pass 2 makes it conditional on allowing an O coarse law (lines 9 and 46).
- P2. Pass 1 says the non-character tests force "exact tail matching" (draft line 35) and that a coarse law must reproduce "every nonzero invariant tail in the image of `Φ` exactly" (draft line 270). Pass 2 restricts this to envelopes with asymptotic forms, and to channels shown to lie in the image (lines 100-112).
- P3. Pass 1 states the shared-support consequence of Lemma F′ for "any finite-range solution" (draft line 217), but drops "finite-range" in its summaries (draft lines 35 and 228). Pass 2 limits it to exactly localized images (lines 9 and 98).
- P4. Pass 1 writes of Lemmas N, E and F: "Three distinct attacks failed, each at a named step" (draft line 223). Pass 2 keeps the theorems and says they do not exhaust K-INV (line 112).
- P5. Pass 1 Corollary C2 assumes updates that commute with every local gauge automorphism (draft line 123). Pass 2 Theorem 2.2 assumes only that the updates preserve the invariant algebras (line 40). The pass-2 hypothesis is weaker and suffices.
- P6. Pass 1 defines exponential locality (INV-3) and cell covariance with rotations (INV-2) in full (draft lines 46-47). Pass 2 item 3 compresses both (line 19). Row 5 checks that nothing used later depends on the dropped detail.
- P7. Pass 1 gives the Attack 3 geometry (`x_X=LX`, `L≥3` odd, straight paths; draft line 199). Pass 2 states Theorem 3.4 for any path and drops the geometry. The theorem does not need it.

### Table, continued: section 1 (definitions)

| # | Item (ZM1INV line) | Verdict | Note |
|---|---|---|---|
| 3 | Def. 1, the laws (17) | CORRECT | Matches `VC1_5.md` section 2: "five rishon modes per end in the fixed total link number `m=1,...,9`; its local group is `U(5)`", and `S_+` with `Spin(10)`. Link factors commute with matter and each other (`VC1_5.md` section 1 item 1). |
| 4 | Def. 2, regions and `𝔄^G(R)` (18) | CORRECT | The gauge unitaries are even, so their parts outside `R` commute with `𝔄(R)`. Hence invariance of `A∈𝔄(R)` is commutation with the parts on `R`, as stated. Evenness is `ZM1_OBS.md` Theorem 3. For U it is also immediate: `-1∈U(5)_x` acts as the parity of the factors at `x`, and the product over the sites touching `R` is matter parity times the constant `(-1)^{m·#links}`. |
| 5 | Def. 3, coarse system and the owner's map (19) | CORRECT | Matches `TOE_ASSEMBLY.md` line 252 (owner text ZM1-INV) and line 253 (retained data). Pass 1's (INV-2) rotations and (INV-3) locality bound are compressed (P6). No later step uses the dropped detail: section 2 uses no locality and section 3 uses exact supports only. |
| 6 | Def. 4, K-INV, K-INV-O, character (20) | CORRECT | K-INV-O is a pass-1 label for the O-to-O question; the owner text names no O coarse law (see row 16). |
| 7 | Def. 5, truncated functions and class (a) (21-27) | CORRECT | Agrees with the owner text quoted at `TOE_ASSEMBLY.md` line 243 with `p=2`. The owner also fixes "Constants are independent of the variable data, except for the stated support-radius dependence" (line 243); item 5 omits it, but `C_{R_0}` carries it. |
| 8 | Def. 6, `P_m` and the locked vectors (28) | ERROR (wording) | `P_m` and its size are right: `s=max(0,m-5)<min(5,m)` for `1≤m≤9`. But "its gauge average is a VC1 witness" overstates. `VC1_5.md` Theorem 5.5 proves "(i)–(iii) and P", and P is a proposed reading (`VC1_5.md` section 1 item 5); that file says its statements "do not establish the full VC1 vacuum" (`VC1_5.md` line 5). Fix: "its gauge average is a P-witness of `VC1_5.md` Theorem 5.5". Same for the O witnesses ("dark P-witnesses", Theorem 4.2). |

### Table, continued: section 2 (character witnesses and reduction)

| # | Item (ZM1INV line) | Verdict | Note |
|---|---|---|---|
| 9 | Theorem 2.1, statement (32) | CORRECT | |
| 10 | Theorem 2.1, U proof (34) | CORRECT | The torus weight is the flavour count because matter and end rishons at `x` both carry the defining representation; this matches `Q_x=N_x+Σ_{ℓ∋x}p_{ℓ,x}` (`VC1_5.md` section 2). Empty case: no high flavour, at most `k` rishons per end, `2k` per link, so each end holds exactly `{1,…,k}` and the matter is empty. Full case: each low weight is the maximum `d_x+[x∈R]`, so every slot holds each low flavour; the link number then forbids high flavours on links; the high weights `1` force full matter. Outer endpoints have no matter in `R` and the same argument applies with maximum `d_x`. Each case leaves one basis vector. |
| 11 | Theorem 2.1, O proof (36) | CORRECT | The Cartan charges are those of `VC1_5.md` Theorem 4.2, `H_{x,j}=(n_{x,j}-1/2)+Σ_{ℓ∋x}(n^{ℓ,x}_j-1/2)`, restricted to the factors in `R`. Each summand is at least `-1/2` with equality only for an empty mode, so the empty vector is the unique joint minimum; full is the unique maximum. Both lie in `S_+`. Multiplicativity on local invariant elements, then density (`VC1_5.md` Theorem 2.1) and continuity, as stated. |
| 12 | Remark after 2.1 (38) | CORRECT | Purity is in `VC1_5.md` Theorems 4.2 and 5.5. A pure state of a noncommutative algebra need not be multiplicative, so 2.1 is stronger. |
| 13 | Theorem 2.2, statement and proof (40-42) | CORRECT | Preservation of the invariant algebras suffices (P5): `α^{Lt}(Φ(τ_βB))∈𝔄^G`, multiplicativity factors the two-point value, stationarity fixes the one-point value. Both truncated values vanish; `0≤C·0` for every `C≥0` and `p`. `‖π(A)Ω-ω(A)Ω‖^2=ω(A^*A)-|ω(A)|^2=0` gives `H_phys=CΩ`. The base tick preserves `𝔄^G` because `E` commutes with `α` (`VC1_5.md` Theorem 2.1). |
| 14 | Remark after 2.2 (44) | CORRECT | See row 35 for the hypotheses of `ZM1I1A.md` Theorem 7. |
| 15 | Theorem 2.3, U case, statement and proof (46-48) | CORRECT | The owner retains "a coarse law `α_1` of the stated form and an `α_1`-invariant state `ω_1`" (`TOE_ASSEMBLY.md` line 243); `ZM1.md` line 361 specifies "a coarse law `α_1` of the `L5-U` form". So the coarse locked witness with the coarse base tick is admissible as `ω_1`; no symmetry of `ω_1` is required. The theorem is conditional on the fine vacuum being a locked witness, as stated. The restriction to even `m₁` is removable (Repair R1). |
| 16 | Theorem 2.3, O case (46, 48) and GAP O (9) | CORRECT as conditional; GAP real but repairable | The owner text and `ZM1.md` line 361 fix a coarse law "of the `L5-U` form" and do not name an O coarse law, so pass 1's coarse `L5-O` is not in the stated target. Theorem 2.2 is indifferent to the laws on the two sides. Hence for a locked O fine witness and the base tick the target with a coarse `L5-U[m₁]` law is equivalent to the mixed kinematic statement K-INV(O; m₁, L): a map `𝔄₁^G[L5-U[m₁]]→𝔄^G[L5-O]` with the owner's covariance and locality. The O-to-O version is K-INV-O. The reduction holds under either reading; only the name of the kinematic lemma changes (Repair R2). |
| 17 | Remark on odd `m₁` (50) | ERROR | "For odd coarse `m₁` this proof supplies no coarse character witness ... its existence is open." A coarse character witness exists for every odd `m₁`: the oriented locked state of Repair R1 is base-tick stationary and restricts to a character. Fix: delete the open clause and cite R1. The plaquette sentence is correct. |

### Table, continued: section 3 (kinematic tests)

| # | Item (ZM1INV line) | Verdict | Note |
|---|---|---|---|
| 18 | Theorem 3.1, statement and proof (54-56) | CORRECT | `[p_{ℓ,x}=k]` commutes with both end groups, so it is invariant. `τ(P)=C(5,k)^2/C(10,2k)` equals `5/9, 10/21, 10/21, 5/9` for `k=1,…,4`. A character is a trace. |
| 19 | Lemma T conclusion (58) | INCOMPLETE | The step of `ZM1I1A.md` Theorem 1 is "A unital *-homomorphism `Φ:𝔄₁→𝔄` transfers the normalized trace: `τ∘Φ=τ₁`". It needs a unique trace on the *domain*. Theorem 3.1 is stated for the fine algebra; it covers the coarse domain only when `m₁` is even. Repair R3 covers every `m₁` and the O law. A second reason the old proof cannot start: its Theorems 2-6 use (G1), and the owner imposes "no map on charged fields or Gauss generators". With R3 the conclusion stands: the old trace obstruction does not carry over. The hedge "does not disprove every possible trace obstruction" is right. |
| 20 | Theorem 3.2 (N), statement and proof (60-62) | CORRECT | `A↦a` with `AΨ_R=aΨ_R` is a unital `*`-homomorphism to `C`. A unital `M_D→C` has a proper ideal of codimension one, impossible for `D≥2`. |
| 21 | Remarks after 3.2 (64) | ERROR | "It does not rule out ... exponentially localized registers; the latter would need a near-inclusion argument." Theorem 2.1 gives a character on all of `𝔄^G`, so the proof of 3.2 runs on `𝔄^G` itself: no unital `M_D→𝔄^G`, `D≥2`, exists with any localization. Fix: Repair R5. The rest of the paragraph is correct. |
| 22 | Theorem 3.3 (E, E1), statement (66) | CORRECT | On `End(K)` the two coarse actions coincide up to sign, since `p_X+p_Y=m₁`. "Independent" is true on the fine side only. The proof does not use independence on the coarse side. |
| 23 | Theorem 3.3, matrix units and charge splitting (68-71) | CORRECT | `ι(e^{-iθp_X})e^{iθp_x}` commutes with `ι(End K)`, so it is `W^*(1⊗c_θ)W`; `c_θ` is a continuous one-parameter group, so `c_θ=e^{iθk_x}`. Commutation of `k_x,k_y` follows from `[p_x,p_y]=0`. Pass 1 gives these steps (`ZM1INV_DRAFT.md` step (ii)); pass 2 compresses them correctly. |
| 24 | Theorem 3.3, joint spectra (72) | CORRECT | The joint spectrum of `(p_X⊗1+1⊗k_x, p_Y⊗1+1⊗k_y)` is the sum set `{(q+a,m₁-q+b)}`. `(s,s)` lies in `P_m×P_m`; moving `q` to a neighbour in the interval `P_{m₁}` puts one coordinate at `s-1`. |
| 25 | Theorem 3.3, one-link paths (74) | CORRECT | Coarse cell translation by `e_i` moves `X` by `2e_i` and the fine block by `2Le_i` (`ZM1I1A.md` section 1 item 2). Two fine unit steps have `ℓ¹` length at most 2, and `2L≥4`. |
| 26 | Remark after 3.3 (76) | CORRECT | Scope stated correctly; the O case is outside. |
| 27 | Theorem 3.4 (S), statement (78-82) | CORRECT | |
| 28 | Theorem 3.4, proof (84-86) | CORRECT | Rechecked: `U^{ab}r^{head†}_c|0⟩=r^{head}_ar^{tail†}_br^{head†}_c|0⟩=-δ_{ac}r^{tail†}_b|0⟩`. The `n` link factors give `(-1)^n`; interior colours are kept after the sum; the coarse `U^{jk}=-|X,k⟩⟨Y,j|` gives `(-1)^{n+1}`. Different links commute (even link factors). Schur's lemma applies because `⊗_iC^5_{z_i}` is irreducible for `∏_iU(5)_{z_i}`. |
| 29 | Remark after 3.4 (88) | CORRECT | |
| 30 | Theorem 3.5 (F) (90-92) | CORRECT | `2s≠m` for `1≤m≤9`. `Φ(f(p_X))=f(Φ(p_X))` for polynomials, and spectral projections are polynomials in `p_X` on the finite spectrum `P_m`. |
| 31 | Theorem 3.6 (F′) (94-96) | CORRECT | Even elements of disjoint regions act on disjoint Jordan-Wigner tensor factors; a tensor product of nonzero projections is nonzero; injectivity makes the images nonzero. |
| 32 | Remark after 3.6 (98) | CORRECT | Repair R6 gives the approximate form for exponentially localized images: the two distances to disjoint regions sum to at least `1/2`. |

### Table, continued: section 4 (tests, inherited results, limits)

| # | Item (ZM1INV line) | Verdict | Note |
|---|---|---|---|
| 33 | Lemma ER paragraph (102) | CORRECT | Matches `ZM1_OBS.md` Lemma ER, "`|m_0(r)-m_1(r)|\le\varepsilon(r)\,M(r,t)`", and its consequence for the two displayed asymptotic forms. |
| 34 | Locked witnesses paired with a coarse character (104) | CORRECT | Theorem 2.2. |
| 35 | Bullet on `VC1_5.md` Theorem 5.2 states (106) | INCOMPLETE | Non-character: the link trace gives `0<ω([p_{ℓ,x}=q])<1` because `|P_m|≥2`. Darkness: `ZM1I1A.md` Theorem 8 says it "applies to the empty/full product witnesses of `VC1_5.md` Theorems 5.2 at `t=±∞`". Missing: `ZM1I1A.md` Theorem 7 assumes "(G1)–(G2), singleton sets and finite range". Its proof uses (G1)-(G2) only to get `Φ(𝔄₁^G)⊆𝔄^G`, which holds here by definition, so it applies to a finite-range invariant-algebra map. Say so. The last sentence is right: if the coarse values vanish for `|β|_∞≥r_0`, then for `r≥r_0` Lemma ER gives `m_0(r)≤ε(r)m_0(r)`, so `m_0(r)=0` once `ε(r)<1`. |
| 36 | Bullet on the R2 mixture (107) | CORRECT | `ZM1I1A.md` Theorem 9 and RC-5 give `1/4` "for every nonzero cell translation and at `β=0`". The image caveat is right for a fine mixture. Repair R4 adds a map-independent statement for a coarse mixture. |
| 37 | Bullet on the swap band (108) | CORRECT | `GA1_5.md` Amendment 1: "The swap layers of Theorem 6.3 and Proposition S-odd are admissible" under NN-a. `ZM1I1A.md` RC-4 is conditional on `|F_0^T|≥c` and says "Whether any map has such images is not shown." |
| 38 | Bullet on the two bands (109) | CORRECT | `LZ1I.md` Theorems 6-8 construct `ω_Σ` and its mixture with "two exact bands" under their own conditions. Branch matching needs `ZM1_OBS.md` Theorems 8′-9′, whose weight and summability hypotheses are not checked for any image. |
| 39 | Bullet on the ice states (110) | CORRECT | `VC1_5U_ODD.md` Theorem 4.3: "`ω̂_ν` is pure on `A^gauge` if and only if `ν` is tail-trivial". The ice tails are not computed anywhere I read. |
| 40 | GAP, pass-1 scope (112) | CORRECT; GAP real | Pass 1's table conditions the R2 and band claims on the image (draft lines 142-143), but its summary drops the condition and the asymptotic-form hypothesis (P2). The ice row claims non-triviality with "tails not computed" (draft line 145); that claim is unproved. The last sentences on the three constructions are right. See the GAP rulings for the repaired statements. |
| 41 | Existing related work (114) | CORRECT | Spot checks: `ZM1.md` line 384, Attack 1 "fails at the step "`Psi_u` is a fermion field": Theorems Z3 and Z3′ force every coefficient with `x != x_u` to vanish"; `GA2_Y2.md` Theorem 3.4 gives "`\kappa\le1/2`" on L5-U. |
| 42 | Literature provenance (116) | CORRECT | Agrees with the pass-1 table (draft section 2). `ZM1I1A.md` RC-6 does "Take `G` finite". No citation is load-bearing. |

### Table, continued: section 5 (interfaces and readings)

| # | Item (ZM1INV line) | Verdict | Note |
|---|---|---|---|
| 43 | Domain and charged sectors (120) | CORRECT | `Q_x` is central in `A^{gauge}` (`VC1_5.md` Theorem 5.3 proof). Traceless generators carry the adjoint action, so they are not invariant. The owner text says these consumers "get no zoom from this map". |
| 44 | Reconstruction and consumers (122) | CORRECT | `ZM1_OBS.md` Theorem 4: truncated data "determine the unitary representation on `H_phys⊖CΩ`". Section 5.1 there: the rate "does not by itself prove speed transfer" and composition "requires a common dictionary and propagated errors". |
| 45 | Readings preamble (124) | CORRECT | The four tests are restated as in the lane rules. |
| 46 | R-V, marks P P P P (126) | CORRECT | The owner text already retains "the specified VC1 fine vacuum" (`TOE_ASSEMBLY.md` line 243). R-V restates it and selects nothing. It depends on a later VC1 decision; that is a dependence, not open-endedness. |
| 47 | R-NC, marks C P F P (127) | ERROR (proof step); marks stand | "Theorem 2.2 implies `H_phys≠CΩ` under this exclusion" reverses the implication. Theorem 2.2 gives character ⇒ `H_phys=CΩ`. The needed direction is its converse: if `H_phys=CΩ`, then `π(B)Ω=ω(B)Ω`, so `ω(AB)=⟨π(A^*)Ω,π(B)Ω⟩=ω(A)ω(B)`. Fix: state "a state is a character on `𝔄^G` if and only if `H_phys=CΩ`", with both directions. Then R-NC is exactly "the vacuum has a nonzero invariant vector orthogonal to `Ω`". Test 3 fails by premise on that weak part of VC1's excitation question; the marks are right. |
| 48 | R-ALL, marks P F P C (128) | CORRECT, with a note | Test 2 fails as stated: the list "every P-witness VC1 supplies" grows (`VC1_5U_ODD.md` adds ice witnesses under ICE-T). The closed variant "every state with (i)-(iii) and P" is not open-ended, but it imports reading P, which `VC1_5.md` leaves to the owner ("The choice among E, P and F is the owner's"); it then fails test 3 or test 4. Either way R-ALL does not pass all four. |
| 49 | Closing paragraph (130) | CORRECT | Conditional and hedged correctly. |

### Table, concluded: section 0 summaries

| # | Item (ZM1INV line) | Verdict | Note |
|---|---|---|---|
| 50 | §0 "Proved here" (7) | INCOMPLETE | Theorem 3.1 (T) is proved but not listed. "fail (Theorems 3.3–3.6)" includes 3.4, which is a positive result listed in the next sentence; write "3.3, 3.5, 3.6". The even-`m₁` and O qualifications become unnecessary or change name after Repairs R1 and R2. |
| 51 | §0 GAP (9) | CORRECT; all four parts real | (i) O coarse law: real; `ZM1.md` line 361 fixes "a coarse law `α_1` of the `L5-U` form"; Repair R2. (ii) Exact tail matching for the tests: real; pass 1's table conditions on the image, its summary does not (P2); Repair R4 and the GAP rulings. (iii) Shared support: real (P3); Repair R6. (iv) Good-sector global map: real, and pass 1 says the same ("The construction must therefore be extended to the defect sectors"). |
| 52 | §0 "Open by name" (11) | ERROR | "the coarse odd-register character-state question" is closed by Repair R1. Add the mixed lemma K-INV(O; m₁, L) of Repair R2. The other names are carried correctly. |

**Counts.** 52 rows: 44 CORRECT, 5 ERROR (rows 8, 17, 21, 47, 52), 3 INCOMPLETE (rows 19, 35, 50). Rows 16, 40 and 51 rule a distiller GAP real. No ERROR changes the truth of a numbered theorem. Rows 17, 21 and 52 understate what is proved; row 47 reverses an implication whose converse is true; row 8 is wording.

---

## 2. Rulings on the distiller's GAPs

**GAP-O (line 9, first part): real; repaired.** The owner text says "Coarse sites carry the same five-mode construction as the fine sites, with any allowed coarse m₁ (R-form)" (`TOE_ASSEMBLY.md` line 252). `ZM1.md` line 361 specifies "a coarse law `α_1` of the `L5-U` form". Neither names an O coarse law. Pass 1's coarse `L5-O` is therefore a variant, as pass 2 says. The reduction does not need it. Repair R2 proves the O-fine reduction with a coarse `L5-U[m₁]` law, to the mixed kinematic statement K-INV(O; m₁, L). If "the same construction" is read as O-to-O, the reduction is to K-INV-O. Neither reading is adopted here.

**GAP-TAIL (line 9, second part, and line 112): real; repaired where a proof exists.** Pass 1's table conditions the R2 and band claims on the image (`ZM1INV_DRAFT.md` lines 142-143). Its outcome paragraph and FINISH drop that condition (draft lines 35 and 270). Lemma ER gives agreement of envelopes to relative order `r^{-2}`; equality of decay length and amplitude needs one of its two displayed asymptotic forms. The repaired statements are:
- Locked witnesses: the comparison is empty (Theorem 2.2). Proved.
- Tracial-link dark states (`VC1_5.md` Theorem 5.2 at `t=±∞`) against a dark coarse pair: for a finite-range invariant-algebra map the comparison is automatic (row 35). For an exponentially local map the fine truncated values of every image pair must vanish exactly beyond a finite separation at each tick. Proved as a condition on `Φ`.
- R2 mixture as the *coarse* state: non-trivial for every `Φ` (Repair R4). Proved.
- R2 mixture, swap band, two bands as the *fine* state: a condition on `Φ` only through the image; non-triviality is not proved for an arbitrary `Φ`.
- Ice states: non-triviality is not proved; their tails are not computed.

**GAP-SUPPORT (line 9, third part): real; repaired.** Theorem 3.6 needs exact supports. Pass 1 states the finite-range case (draft line 217) and then drops "finite-range" in its summaries (draft lines 35 and 228). Repair R6 gives the approximate form: for orthogonal nonzero projections the distances of their images to the algebras of two disjoint regions sum to at least `1/2`. That is the precise meaning "shared support" can have for exponentially localized images.

**GAP-GLOBAL (line 9, last part): real; not repaired.** Theorem 3.4 is a statement about one path. Pass 1 says the same: "The construction must therefore be extended to the defect sectors `1-P_γ`." No extension is constructed or refuted here.

**GAP-EXHAUST (line 112, last part): real.** Theorems 3.2, 3.3, 3.5 and 3.6 refute named constructions. None bounds an arbitrary invariant-only embedding. Pass 1's own FINISH agrees: "Lemmas N, E and F refute three specific constructions, not the statement."

## 3. Decisions on the questions put to this referee

**Lemma T (Theorem 3.1): the old trace obstruction does not carry over. Decided yes, with Repair R3.** The old proof starts from "A unital *-homomorphism `Φ:𝔄₁→𝔄` transfers the normalized trace: `τ∘Φ=τ₁`" (`ZM1I1A.md` Theorem 1). That step needs a unique tracial state on the domain. On the invariant domain `𝔄₁^G(R₁)` there are at least two, for every `m₁` and for the O law (R3). So `τ∘Φ` is some tracial state of `𝔄₁^G` and need not be `τ₁`. Independently, Theorems 2-6 there use (G1), and the owner removed every map condition on Gauss generators. Theorem 3.1 as written covers the domain only for even `m₁`; R3 covers the rest. Nothing here excludes a different trace argument, and the file says so.

**Theorem R (Theorem 2.3): decided correct, and stronger than stated.** In the locked even-`m` U witnesses with the base tick, the class-(a) comparison is empty for every unital `Φ` and every coarse pair that restricts to a character (Theorem 2.2). Such a coarse pair exists for every `m₁∈{1,…,9}`: Theorem 2.1 for even `m₁`, Repair R1 for odd `m₁`. So ZM1-I1[INV] in those vacua holds if and only if K-INV(m, m₁, L) holds for some `m₁` and `L≥2`, with no parity restriction on `m₁`. For the locked O witnesses the same holds with the mixed lemma K-INV(O; m₁, L) under the owner's `L5-U` coarse form (R2), or with K-INV-O if an O coarse law is allowed. Plaquette updates are outside both statements unless the witnesses are shown stationary for them.

**The three failed attacks on K-INV: decided valid as three distinct constructions, each failing at a proved step.**
1. *Neutral matrix registers* fail at Theorem 3.2 (N). Repair R5 removes the finite-region restriction: no unital `M_D`, `D≥2`, sits anywhere in `𝔄^G` for even `m` or O, whatever its localization.
2. *Decimation with equivariant links* fails at Theorem 3.3 (E) for paths of two or more links and at its covariance clause (E1) for one-link paths. Proof checked line by line (rows 22-25).
3. *Good-sector decimation with the star identification* fails at Theorem 3.5 (F): the identification sends both coarse end numbers of a link to end numbers of the first and last fine links, and no unital homomorphism does that. Theorem 3.4 (S), the good-sector isomorphism, is a correct positive result, not a failure.
Attacks 2 and 3 share one premise: coarse end data sit at fixed representatives. Theorem 3.6 (F′) and Repair R6 locate that premise as the common failure point. So the three attacks probe two ideas, registers and decimation. Under the lane rule this suffices to carry K-INV as "a lemma on which three distinct attacks failed", with those three names. It is not a proof that K-INV fails.

**Lemma F′ (Theorem 3.6): decided correct for exact supports; Repair R6 gives the exponentially local form.**

**First tests: non-trivial only where proved.** The locked witnesses are trivial (proved). The R2 mixture is non-trivial for every `Φ` when it is the coarse state (R4, proved). The tracial-link dark states impose an exact-vanishing condition on exponentially local maps (proved as a condition). The R2 mixture, the swap band and the two bands as fine states are non-trivial only for maps whose image contains the relevant channel; no such map is shown. The ice states are not shown non-trivial. Pass 1's blanket claim "not trivial: there the comparison forces exact tail matching" is therefore too strong; pass 2's corrected text is right.

**Readings: four-tested correctly, with one repaired proof step.** R-V: P P P P, correct. R-NC: C P F P, correct once "character if and only if `H_phys=CΩ`" is proved in both directions (row 47). R-ALL: P F P C, correct; its closed variant imports reading P and fails test 3 or 4 instead (row 48). R-V alone passes all four. No reading is needed for any proved statement.

## 4. Repairs (referee closures, proved here)

Each repair is a finite argument. None uses a computation. Each credits the result it extends.

**R1 (an oriented locked state for odd `m`).** Let `m=2k+1`, `0≤k≤4`, on `L5-U[m]`. Call `x` the lower end and `x+e_j` the upper end of the link `(x,x+e_j)`. Let `ψ` be the product state with empty matter at every site and, on every link, flavours `{1,…,k}` at the lower end and `{1,…,k+1}` at the upper end. Put `ω=ψ∘E`. Then (a) `ω` restricts to a character on `𝔄^G`; (b) `ω` is invariant under the base tick for every allowed constant; (c) `ω` is invariant under cell translations. It is not reversal invariant, and nothing here needs that.

*Proof of (a).* Fix a finite region `R`. Let `d_x` be the number of ends at `x` of links of `R`, and `u_x` the number of links of `R` whose upper end is `x`. The torus weight of `Ψ_R` is `h_{x,j}=d_x` for `j≤k`, `h_{x,k+1}=u_x`, and `h_{x,j}=0` for `j≥k+2`. Let `v` be an occupation-basis vector with this weight.
1. Sum the weight over all `x` and `j`: `kΣ_xd_x+Σ_xu_x=(2k+1)n_R`, with `n_R` the number of links of `R`. In `v` the same sum counts the `(2k+1)n_R` rishons of `R` plus the matter quanta at sites of `R`. So the matter of `v` is empty.
2. For `j≤k`, `h_{x,j}=d_x` with empty matter, so every end at `x` holds `j`. Every end holds `{1,…,k}`.
3. No end holds a flavour `≥k+2`. A link holds `2k+1` rishons and each end holds flavour `k+1` at most once, so exactly one end of each link also holds `k+1`. Orient each link toward that end. The in-degree of `x` is then `h_{x,k+1}=u_x`, the in-degree of `x` in the lower-to-upper orientation.
4. Two orientations of a finite graph with equal in-degrees, one of them acyclic, coincide. Let `S` be the set of links where they differ, oriented as in the acyclic one. At each vertex its in-degree in `S` equals its out-degree in `S`. A nonempty finite digraph with that property has a directed cycle: follow out-edges until a vertex repeats. The lower-to-upper orientation has none, since each step raises the coordinate sum. So `S` is empty and `v=±Ψ_R`.

So the weight space of `Ψ_R` is `CΨ_R`. The rest is the proof of Theorem 2.1: invariant elements preserve torus weight spaces, `ω=ψ` on `𝔄^G`, multiplicativity on local elements, density.

*Proof of (b).* `VC1_5.md` Proposition R2, proof (1): "Each hop term has a matter annihilator on its right, so every cube generator kills every vector with empty matter on its cube, and each cube gate acts as the identity there." The electric factor is `exp[-iτ_E(p_{ℓ,src}-m/2)^2]` (`VC1_5.md` section 2). On `ψ`, `p_{ℓ,src}∈{k,k+1}`, so `(p_{ℓ,src}-m/2)^2=1/4` and the factor is a phase on each link, for either choice of source end. Each gate maps the local product vector to a phase multiple of itself, so `ψ∘α=ψ` on local elements, as in the proof of `VC1_5.md` Theorem 4.2. `E` commutes with `α` (`VC1_5.md` Theorem 2.1), so `ω∘α=ω`. *Proof of (c).* Translations preserve the configuration. □

*Consequence.* With `ω₁` this state on a coarse `L5-U[m₁]` system, `m₁` odd, Theorem 2.3 holds for every `m₁∈{1,…,9}`. The owner text requires of `ω₁` only "an `α_1`-invariant state". If a later reading also demanded cell-lift invariance of `ω₁`, (c) would not suffice and the odd-`m₁` case would reopen. The construction follows `VC1_5.md` Theorem 5.5 and Proposition R2.

**R2 (the O fine witnesses with an `L5-U` coarse law).** Let `ω₀` be a locked witness of `VC1_5.md` Theorem 4.2 and `α` the base tick. With a coarse law of the `L5-U[m₁]` form, the target holds for `(ω₀,α)` if and only if, for some `m₁∈{1,…,9}` and `L≥2`, there is a cell-covariant, exponentially local, unital injective `*`-homomorphism `𝔄₁^G[L5-U[m₁]]→𝔄^G[L5-O]`. Call this K-INV(O; m₁, L).

*Proof.* The target contains the map. Conversely take the coarse base tick and, as `ω₁`, the locked witness (even `m₁`, Theorem 2.1) or the state of R1 (odd `m₁`). The fine witness is a stationary character (Theorem 2.1, `VC1_5.md` Theorem 4.2). Theorem 2.2 uses no relation between the two laws. □ With a coarse `L5-O` law the same proof gives the K-INV-O form.

**R3 (Lemma T on the domain, every `m₁`, both laws).** For every `m₁∈{1,…,9}` and every finite coarse region `R₁` containing a link `ℓ=(X,Y)`, `𝔄₁^G(R₁)` has at least two tracial states. The same holds on `L5-O`.

*Proof.* U: let `ω₁` be the character of Theorem 2.1 or R1, and `q` the sharp value of `p_{ℓ,X}` in it. Then `ω₁([p_{ℓ,X}=q])=1`, while `τ₁([p_{ℓ,X}=q])=C(5,q)C(5,m₁-q)/C(10,m₁)<1` because `P_{m₁}` has another element. O: the even-parity projection of the `X` end commutes with `Spin(10)_X`, whose elements are products of exponentials of even quadratic elements (the group is connected), and with every other site group. It has value 1 in the empty witness. Under `τ₁` it has value `1/2`, because `S_+=(even⊗even)⊕(odd⊗odd)` with two summands of dimension `16·16`. A character is tracial. □

**R4 (the R2 mixture as the coarse state is a test for every map).** Fix `m₁` and the coarse base tick. Let `ω₁` be the mixture of `VC1_5.md` Proposition R2 for `L5-U[m₁]`, and `P₁=[p_{ℓ,src}=a]` on a coarse link `ℓ` along `e_1`. Let a unital `*`-homomorphism `Φ`, a fine pair and `C_{R₀}` (with `R₀` at least the support radius of `P₁`) satisfy class (a) with `p=2`. Then for every `t≥0` and every cell translation `β` with `|β|_∞=r≥1`,
\[
|F_0^T(P_1,\tau_\beta P_1;t)-\tfrac14|\le 2C_{R_0}(r^{-2}+tr^{-3}).
\]
So `F_0^T→1/4` as `r→∞` at fixed `t`. In particular no fine character pair (Theorem 2.2) can be paired with this coarse state.

*Proof.* `P₁` is invariant, self-adjoint and of norm one. `ZM1I1A.md` Theorem 9 with RC-5, applied to the coarse law, gives `F_1^T(P_1,τ_βP_1;t)=1/4` for all `β≠0` and all `t`. Every truncated value of norm-at-most-one elements has modulus at most 2, so `M(r,t)≤2`. Insert both facts into the bound at `β`. □

**R5 (no unital matrix register anywhere in `𝔄^G`).** Let `𝔅` be a unital C*-algebra with no character, for example `M_D` with `D≥2`. On `L5-U[m]` with even `m`, and on `L5-O`, there is no unital `*`-homomorphism `𝔅→𝔄^G`.

*Proof.* Compose with the character of Theorem 2.1. □ For these fine laws every K-INV map makes `ω₀∘Φ` a character of `𝔄₁^G`. Such characters exist for every `m₁` (Theorem 2.1, R1) and for O, so R5 gives no obstruction to K-INV.

**R6 (shared support for exponentially localized images).** Let `Φ:𝔄₁^G→𝔄^G` be an injective unital `*`-homomorphism. Let `P,P'∈𝔄₁^G` be nonzero projections with `PP'=0`, and `R₁,R₂` disjoint finite fine regions. Then
\[
\operatorname{dist}(\Phi(P),\mathfrak A(R_1))+\operatorname{dist}(\Phi(P'),\mathfrak A(R_2))\ge\tfrac12 .
\]
*Proof.* Let the distances be `δ₁,δ₂`; they are attained in finite dimension. If either is at least `1/2` there is nothing to prove, so let both be below `1/2`. Take `a∈𝔄(R₁)` with `‖Φ(P)-a‖=δ₁`. Replace `a` by its even part `(a+θ(a))/2`, with `θ` the parity automorphism. `θ` fixes the even element `Φ(P)` (`ZM1_OBS.md` Theorem 3), preserves `𝔄(R₁)` and is isometric, so the distance does not grow. Do the same for `b∈𝔄(R₂)`. Even elements of disjoint regions act as `A⊗1` and `1⊗B` in a Jordan-Wigner order with `R₁` first, as in Theorem 3.6. So `‖ab‖=‖a‖‖b‖≥(1-δ₁)(1-δ₂)`, since `‖Φ(P)‖=‖Φ(P')‖=1` by injectivity. Also `Φ(P)Φ(P')=Φ(PP')=0`, so
\[
\|ab\|\le\|(a-\Phi(P))b\|+\|\Phi(P)(b-\Phi(P'))\|\le\delta_1(1+\delta_2)+\delta_2 .
\]
Hence `1-δ₁-δ₂+δ₁δ₂≤δ₁+δ₂+δ₁δ₂`, that is `δ₁+δ₂≥1/2`. □ Theorem 3.6 is the case `δ₁=δ₂=0`. For any injective map, two incompatible end-number projections of one coarse link cannot both be approximated to better than `1/4` on disjoint fine regions. Under exponential locality this is the usable form of "shared support".

## 5. Required edits to `ZM1INV.md` (for the lead; this referee edits nothing)

- E1 (row 8). Line 28: "its gauge average is a VC1 witness" → "its gauge average is a P-witness of `VC1_5.md` Theorem 5.5". Call the O witnesses "dark P-witnesses (`VC1_5.md` Theorem 4.2)".
- E2 (rows 15, 17; R1). Theorem 2.3: drop "even" before the coarse `m₁`; cite R1 as the coarse witness for odd `m₁`. Line 50: replace its first two sentences by a pointer to R1 and the cell-lift caveat of R1.
- E3 (row 16; R2). Theorem 2.3, O sentence: replace "if an O coarse law is allowed" by R2 (coarse `L5-U` law: K-INV(O; m₁, L); coarse `L5-O` law: K-INV-O). Add K-INV(O; m₁, L) to definition 4.
- E4 (row 19; R3). After Theorem 3.1 add R3 and one sentence: the old Theorems 2-6 also use (G1), which the owner removed.
- E5 (row 21; R5). Line 64: replace "or exponentially localized registers; the latter would need a near-inclusion argument" by R5.
- E6 (row 32; R6). After Theorem 3.6 add R6.
- E7 (row 35). Line 106: add that `ZM1I1A.md` Theorem 7 uses (G1)-(G2) only to obtain `Φ(𝔄₁^G)⊆𝔄^G`, which holds here by definition.
- E8 (row 36; R4). Line 107: add R4.
- E9 (row 47). Line 127: replace "Theorem 2.2 implies `H_phys≠CΩ` under this exclusion" by "a state is a character on `𝔄^G` if and only if `H_phys=CΩ`" with both directions proved.
- E10 (row 48). Line 128, optional: note that the closed variant of R-ALL imports reading P.
- E11 (row 50). Line 7: add Theorem 3.1; write "fail (Theorems 3.3, 3.5, 3.6)"; reflect R1, R2 and R5.
- E12 (row 52). Line 11: delete "the coarse odd-register character-state question"; add K-INV(O; m₁, L).
- E13 (section 2 of this report). Line 9 and line 112: mark GAP-O, GAP-TAIL and GAP-SUPPORT repaired by R2, R4 and R6 where proved; GAP-GLOBAL and GAP-EXHAUST stay open.
- E14 (row 2). Line 13: the lead records the pass-2 model, effort and session from the run log.

## 6. Open statements to carry, by name

- **K-INV(m, m₁, L)**, `m` even, any `m₁∈{1,…,9}`, `L≥2`. Open. Three named attacks failed: neutral matrix registers (Theorem 3.2, R5); decimation with equivariant links (Theorem 3.3 with E1); good-sector decimation with the star identification (Theorem 3.5). By Theorem 2.3 with R1 it is equivalent to ZM1-I1[INV] in the locked U witnesses with the base tick.
- **K-INV(O; m₁, L)** (R2) and **K-INV-O**. Open. Theorem 3.3 does not apply on O; Theorem 3.2 and R5 do.
- **ZM1-I1[INV] in non-character vacua.** Open. R4 is a proved necessary condition when the coarse state is the R2 mixture.
- **Good-sector extension.** A unital, globally compatible extension of Theorem 3.4 to defect sectors. Open.
- **Fine-side test non-triviality.** Whether any K-INV map has the R2, swap-band or two-band channels in its image; the ice tails. Open.
- **Coarse-state symmetry.** If a reading ever requires cell-lift invariance of `ω₁`, the odd-`m₁` coarse character question reopens (R1, remark).
- Inherited, unchanged: VC1 and its vacuum choice (with the E, P, F reading); ICE-T and ICE-U(R4); LZ1-i[ZM1a]; ZM1-G; Y1; H-BLOCK; R-CS, including R-CS^str; MT1-S; ZM1(a)1 and full ZM1.

## 7. Freeze recommendation

Freeze `ZM1INV.md` after edits E1-E14. No edit changes the truth of a numbered theorem. E2, E3 and E5 strengthen stated results; E9 repairs a proof step whose conclusion stands. The status line should keep "author-side mathematics", with Repairs R1-R6 marked "referee closure, unrefereed". No `[check]` is needed for any proof: every step is finite-dimensional algebra, a spectral argument, a finite-graph lemma or an inequality. The one `[check]` in section 9 only guided R1.

## 8. Prior work used

All paths are in this folder at `cc209676e` unless stated. Each result is quoted where it is used above.

| Result | Path | Use here |
|---|---|---|
| Laws, base tick `U_0=W_EM_oM_e`, electric factor, `Q_x` | `VC1_5.md` section 2 | Rows 3, 10; R1(b). |
| Gauge average, density, `E` commutes with `α` | `VC1_5.md` Theorem 2.1 | Rows 3, 13; R1, R2. |
| Locked O witnesses and their stationarity proof | `VC1_5.md` Theorem 4.2 | Rows 11, 16; R2, R3. |
| Tracial-link states | `VC1_5.md` Theorem 5.2 | Row 35. |
| `Q_x` central in `A^{gauge}` | `VC1_5.md` Theorem 5.3, proof | Row 43. |
| Locked U witnesses | `VC1_5.md` Theorem 5.5 | Rows 8, 10, 15; R1 follows its pattern. |
| Empty-matter stationarity; the R2 mixture | `VC1_5.md` Proposition R2 | R1(b) (extended to a pure oriented state); R4. |
| Coarse indexing and block size | `ZM1I1A.md` section 1, items 1-2 | Rows 5, 25. |
| Trace transfer `τ∘Φ=τ₁` | `ZM1I1A.md` Theorem 1 | Row 19; R3 shows the step is unavailable on the invariant domain. |
| Dark pairs; dark kinematics | `ZM1I1A.md` Theorems 7, 8 | Rows 14, 35. |
| The `1/4` tail | `ZM1I1A.md` Theorem 9, RC-5 | Row 36; R4 (extended to a map-independent coarse-side bound). |
| Moving-point lower bound; refinement check | `ZM1I1A.md` RC-4, RC-6 | Rows 37, 42. |
| Evenness of `𝔄^G` | `ZM1_OBS.md` Theorem 3 | Rows 4, 31; R6. |
| Reconstruction from truncated data | `ZM1_OBS.md` Theorem 4 | Row 44. |
| Branch transfer hypotheses | `ZM1_OBS.md` Theorems 8′, 9′ | Row 38. |
| Lemma ER | `ZM1_OBS.md` appendix | Rows 33, 35, 40. |
| Class (a) scope remarks | `ZM1_OBS.md` section 5.1 | Row 44. |
| Swap layers admissible under NN-a | `GA1_5.md` Amendment 1 (Theorem 6.3, Proposition S-odd) | Row 37. |
| Two exact bands | `LZ1I.md` Theorems 6-8 | Row 38. |
| Ice purity iff tail triviality | `VC1_5U_ODD.md` Theorems 4.2, 4.3 | Row 39. |
| Coarse law "of the `L5-U` form" | `ZM1.md` line 361 | Rows 15, 16; GAP-O. |
| Attack 1 and Theorems Z3, Z3′ | `ZM1.md` line 384 and Theorems Z3, Z3′ | Row 41. |
| Link coherence `κ≤1/2` | `GA2_Y2.md` Theorem 3.4 | Row 41. |
| Owner texts ZM1-I1[a] and ZM1-INV | `TOE_ASSEMBLY.md` lines 243, 252-255 | Rows 5, 7, 15, 16, 46. |
| Prior-work digest | `prior/ZM1INV.md` | Read first, in full. |

**Prior work the digest missed.** Two inputs decide points here and are not in `prior/ZM1INV.md`. `ZM1.md` line 361 fixes the coarse law as "of the `L5-U` form", which decides GAP-O. `VC1_5.md` Proposition R2, proof (1), gives the empty-matter stationarity argument that R1 reuses. No other branch was read: every result used lives in this folder, and the digest quotes main and the open PRs where they bear on the target.

## 9. Check

`[check]` One scratch computation, `/tmp/toe-ZM1INVref/check_r1.py`, run with `python3 -I` after `memory_pressure` reported 55 percent free; 0.03 s, about 6 MB. It guides only and proves nothing. On one plaquette (four sites with matter, four links) it counts the occupation-basis vectors whose torus weight equals that of the reference product vector. Output:

```
odd m=1 plaquette: acyclic ref -> 1, cyclic ref -> 2
odd m=3 plaquette: acyclic ref -> 1, cyclic ref -> 2
odd m=5 plaquette: acyclic ref -> 1, cyclic ref -> 2
odd m=7 plaquette: acyclic ref -> 1, cyclic ref -> 2
odd m=9 plaquette: acyclic ref -> 1, cyclic ref -> 2
even m=2 plaquette locked -> 1
even m=4 plaquette locked -> 1
```

The lower-to-upper orientation leaves one vector, as R1 step 4 says. A directed 4-cycle as reference leaves two: reversing the cycle keeps every weight. So acyclicity is the needed hypothesis, not a convenience. The even locked count agrees with Theorem 2.1.

---

## FINISH

**Proved (pass 3, referee closures, unrefereed).**
- Theorems 2.1, 2.2, 2.3 and 3.1-3.6 of `ZM1INV.md` are correct as stated. Row 47's step is repaired: a state is a character on `𝔄^G` if and only if `H_phys=CΩ`.
- R1: for every odd `m`, the oriented locked state (empty matter; flavours `{1,…,k}` at the lower end and `{1,…,k+1}` at the upper end of every link) is base-tick stationary, translation invariant, and a character on `𝔄^G`. So Theorem R holds for every coarse `m₁∈{1,…,9}`.
- R2: for the locked O witnesses with the base tick and an `L5-U` coarse law, the target is equivalent to K-INV(O; m₁, L) for some `m₁` and `L≥2`.
- R3: the invariant domain has at least two tracial states for every `m₁` and for O, so the trace-transfer step `τ∘Φ=τ₁` of `ZM1I1A.md` Theorem 1 is unavailable.
- R4: with the R2 mixture as coarse state, every map satisfying class (a) has `|F_0^T(P_1,τ_βP_1;t)-1/4|≤2C_{R_0}(r^{-2}+tr^{-3})`; no fine character pair can match it.
- R5: for even `m` and for O, no unital `*`-homomorphism from a character-free algebra, such as `M_D` with `D≥2`, into `𝔄^G` exists, with any localization.
- R6: for orthogonal nonzero projections `P,P'` and disjoint fine regions, `dist(Φ(P),𝔄(R₁))+dist(Φ(P'),𝔄(R₂))≥1/2`.

**Counterexamples.** None to ZM1-I1[INV] or to K-INV. Two statements of `ZM1INV.md` are refuted as understatements: the open clause of line 50 and line 11 (a coarse odd-register character witness exists, R1), and the near-inclusion clause of line 64 (R5 needs none).

**Open by name.**
- K-INV(m, m₁, L), `m` even. Three distinct attacks failed: neutral matrix registers (Theorem 3.2, R5); decimation with equivariant links (Theorem 3.3 with E1); good-sector decimation with the star identification (Theorem 3.5). Attacks 2 and 3 share the premise that coarse end data sit at fixed representatives.
- K-INV(O; m₁, L) and K-INV-O.
- ZM1-I1[INV] in non-character vacua; the extension of Theorem 3.4 to defect sectors; whether any K-INV map carries the R2, swap-band or two-band channels; the ice-state tails.
- The odd-`m₁` coarse character question, only if a reading ever requires cell-lift invariance of `ω₁`.
- Inherited: VC1 and its vacuum choice, ICE-T, ICE-U(R4), LZ1-i[ZM1a], ZM1-G, Y1, H-BLOCK, R-CS (with R-CS^str), MT1-S, ZM1(a)1, full ZM1.

**What changes downstream.**
- ZM1: in the locked U witnesses with the base tick, ZM1-I1[INV] is exactly K-INV for some `m₁∈{1,…,9}`, with no parity restriction. Lanes on ZM1-I1[INV] should work K-INV.
- K-INV lanes: a solution contains no unital matrix register anywhere (R5); incompatible end-number images cannot both lie closer than `1/4` to the algebras of disjoint regions (R6); end data cannot stay at the representatives (Theorem 3.5).
- Coarse-state choices: the R2 mixture cannot be paired with a locked fine vacuum (R4).
- O-law lanes: no O coarse law is needed for the reduction (R2).
- VC1 lanes: a state is a character on `𝔄^G` exactly when `H_phys=CΩ`, so a locked witness has no invariant excitation vector. Whether VC1 requires one is VC1's question; nothing here decides it.
- Charged sectors and Gauss generators: unchanged; they get no zoom from this map.
- No axiom, working-set entry, reading or frozen file changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. `ZM1INV.md` is not edited.
