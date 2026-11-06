lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T09:40Z

# b-in-r2: the three BLOCKs of gates/b-in-gate.md for library/b-in.md

FINISH row 399. Pinned at 99d2c3b3f. Finished 2026-11-06T22:18Z. The Result is at the end.

Started 2026-11-06T21:40Z on the Mac mini, worker 1. Original arguments by Claude; checked line by line by Codex in `gates/b-in-r2-gate.md`, with the repairs and retained premises recorded below. FINISH row 405 applies that written check at checkout `3710994a7`; this is research text, not an audit and no status grant.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (complete account CA-I, CA-II, CA-III and outline at upstream `31a47c543775`), for every statement, construction and bound cited with a line number. Tadeusz Balaban for the multiscale construction (CMP 89-122). Earlier work here: `library/b-in.md` (Claude, row 389), its check `gates/b-in-gate.md` (Codex gpt-6-astra xhigh, row 397), `library/ca-claude.md`, `library/ca-f.md`, `library/b102.md`.

## 1. Scope, duplicate check, sources

- **Item.** FINISH row 399. Moves: CA-BIN (`library/t0-tree.md` node CA-BIN, registry row CA-BIN, owner `b-in`), the input (B-in) of CA = clause (b) of `4.27:prf-room-dissolving` (CA-I 138348, unmarked) and the core step of `4.27:prf-ambient-inclusion` (CA-I 136490, marked incomplete). The three old local obstructions have conditional repairs. Full sealing requires the complete input and consumer-obligation lists below; CA-BIN remains OPEN.
- **Duplicate check (rule 0a).** `grep` of `library/open-core.md` and `library/l17c.md` for b-in, sealing, own-level, B_S, enlarged collar, Proposition Sh, partial product: no match. `library/open-registry.md` line 958: CA-BIN, owner `b-in` (this lane's lineage). FINISH rows naming the sealing package: 382, 383, 387 (digests), 389 (b-in), 397 (its check), 399 (this row). Row 404 (`fc-r2`) is the frame change of `library/fc.md`, a different object. No other row attacks these three BLOCKs. ca-f's (N1)-(N3) belong to other owners (stage-claude, B99b-T314) and are not attacked here.
- **Account label and status.** As in `library/b-in.md` section 1: clause (b) of `4.27:prf-room-dissolving` (CA-I 138348-138483, not marked incomplete) invokes the own-level bound of "the sealing construction" (CA-I 138438-138450); the earlier bounded search located no independent, noncircular supplier in the four supplied sources (gates/b-in-gate.md section 8). The account does state and invoke the desired conclusions; this is not an absence claim about their statements.
- **Sources.** CA-I, CA-II, CA-III and the outline fetched by URL into a scratch folder of this lane; SHA-256 agree with `library/arr.md` (outline d7f77d4d..., CA-I 4cb5cb5e..., CA-II 6a1f74b0..., CA-III 7e36523b...). Line numbers I:, II:, III:, SA: are of those raw files.
- **Rules.** No numerical run. No computer-assisted step.

## 2. Conventions kept from b-in.md, with the gate's renaming

- **Sets (gate section 3).** 𝖲 is the source band of the current localisation: the (2M_1+3 blocks)-neighbourhood of Ω''^{~2}_{h+1} in Λ (I:92468-92469). S := ∂(Ω''_{h+1})^~ is the cut of the room lemma (I:138358). They are different sets. b-in.md wrote S for 𝖲; here 𝖲 is written. G := (support of B_2) \ 𝖲, as in b-in.md section 3. o(y) := ℓ_{B''_k}(y), the level of y in B''_k read with precedence (I:132981-132989; I:136662-136665).
- **Geometry, from the law-site proof (I:91991-92031).** D_2 = (Z'_h)^{~2} ∩ Λ is Z'_h ⊇ Z_h with two layers of LMR_{h+1}-cubes of level h round it; the cut is its outer boundary; (Ω''_{h+1})^{~2} = ((Z'_h)^~)^c (Balaban, CMP 122a p. 195, as quoted at I:92010-92013). So 𝖲 contains the outer layer of D_2 and 2M_1+3 blocks of the inner one, and one full layer separates Z_h from 𝖲: d_sc(Z_h, 𝖲) >= Ř_k - 1 ((β) at I:92094-92096). Here Ř_k = k - h (I:77938-77954).
- **Corrected core (gate section 3).** K_0 := {cells y of D_2 ∩ G : d_sc(y, 𝖲) >= Ř_k/2}, K_+ := {y in K_0 : o(y) >= 1}, B_S^{new} := D_2 \ K_0, written B_S below. This replaces the literal surface description by “the excluded band near the cut”; section 4.3 retains the consumer matching obligations.
- **Inputs kept as named in b-in.md**, with the gate's repairs: (LR) read-complete (gate section 2: every stencil, averaging and gauge read of a reset patch in N(y); B_3 >= 12; a separate boundary inequality at vertices without a patch); (I-A); (I-D) on the full test set, mixed-level transports included (gate section 3); (I-G) including the reading of d_sc as a path metric that counts M-cubes of the local scale (I:91727); (I-N0), (I-R), (I-T), (I-K); floor (M), read as (M*) below. Theorem G, Lemmas I, C, J, BCH, A_n, E' and Corollary B1 are used as the gate passed them (gate sections 2-7). B2(a) is used as the gate passed it: "ADVANCE as a conditional estimate".
- **Lemma C with read-complete patches (gate section 3, last sentence on Lemma C).** A reset patch at a block of level j now reads its box~ (within 4R_1M_1 L^j η of the block, CMP 102 (144)), the averaging contours inside it, the auxiliary gauge collar of total width at most 2W_aux L^j η (b102 1840-1846) and one-step stencils. So it reads within R_* L^j η of the block, R_* := 4R_1M_1 + 2W_aux + 1. In the proof of Lemma C the step bound becomes max{R_* + L, LR_* + 1} L^l η <= 2 L R_* L^l η, including a reverse crossing beginning at level l + 1, as R_*, L >= 1. Read the floor (M) as **(M*)** M >= max{16 L s_0, 8 L^2} R_* (and M >= 4 W_aux). Then (C0) and (C1) hold with the same proofs, since M/(2L R_*) >= s_0 + 1. (C2) holds too: a step moves less than M L^{l-1} η, one cell of level l - 1, since (M*) gives M > 2 L^2 R_*. B1 and B2(a) read Lemma C only through (C0)-(C2), so they hold under (M*). W_aux and R_1M_1 are fixed before M, so (M*) is an admissible floor.
- **Ceilings (gate section 4).** (Γ_1) has degree p_0 - q < 0 in t_γ; (Γ_3), (Γ_4) and the first part of (Γ_0) have degree p_0 + 2r - q < 0; (Γ_2), (Γ_5), the second part of (Γ_0) and the local (Γ_Sh') decay exponentially. (G-global) below has degree −r. All are upper bounds on γ, fixed last. None is a cap in the sense of I:1246-1253.

## 3. BLOCK 1: B2(c) on the actual cube families

### 3.1 The cubes the consumers route to the base bound

- **Consumer R** (`4.27:prf-room-dissolving` (b), I:138448-138450): "On cubes, the cube clause of the same own-level bound is met with the gauges of its first clause". The clause is that of a term τ read at x in W_c. Its cubes are those of Q(x), at the family's weight (I:132543-132544; I:122284-122286).
- **Consumer A** (`4.27:prf-ambient-inclusion`, I:136752-136756 and the interface I:139967-139971): "A cube of a frozen family of a dissolved piece ... is controlled by the base bound on the core with its gauges". The other cubes go to other bounds: a cube with a point in 𝖹 to the consumer's gauge, every other cube to the kept gauge of the layer bound. "No cube is assembled from two bounds."
- **The frozen family** of a piece c is the cube family that 𝔖^{(k_c)}_{n^+} assigns at the points x of W_c (I:132454-132456). A clause at x reads Q(x), "the frozen cube clauses read at x" (I:125321-125323).

**Reading (Q-pt).** A cube of Q_𝔅(x) contains x. The account attaches cube clauses "pointwise" (I:136749) and does not state the rule. If another rule is meant, the proofs below need only that each such cube contains a point of W_c.

### 3.2 Lemma F (family form: a family-λ cube lies where the level is at least λ)

**Lemma F.** Let 𝔅 be the set of a date of the time order (I:133424-133460) and let □ be a cube of Q_𝔅 of family (λ, w). Then ℓ_𝔅 >= λ at every point of □ ∩ Ω_1(𝔅). If λ >= 1, then □ ⊂ Ω_1(𝔅): the cube has no raw point.

*Proof.* Every family has the one-sided form "□ ⊂ (level region >= m), □ meets the complement of the next region" (I:48472-48474, I:134557, I:148146-148186). The families are of four kinds.

1. *Families of B_k* (CMP 119 (2.38), quoted at I:148146-148152; the top family, I:134608-134613). Here □ ⊂ Ω_n with scale n, or □ ⊂ Ω_j (top) with scale j. Ω_n is the region of level >= n of the nest. So ℓ >= λ on □.
2. *Stage family (1.65) of CMP 122a, m <= j* (I:148171-148176). □ ⊂ Ω''_m, scale m. By the closed form (4.27:eq-determining-set-order-a), I:133459, the stage level at y in X ∩ Ω_1 is λ_n(y) = min{μ''(y), max{μ(y), j}}, with μ the level in B_k, μ'' the level in B''_k and j = h + n. On Ω''_m = Ω_m(B''_k), μ'' >= m; and max{μ, j} >= j >= m. So λ_n >= m on □.
3. *Stage family (1.67), k_0 + 1 <= m <= j* (I:148183-148188). Here □ ⊂ Ω_m and its scale is j, not m. On Ω_m, μ >= m. Also Ω_m ⊂ Ω_{k_0+1}, which misses Z''_k = (Ω^{~5}_{k_0+1})^c ∩ Z (I:121784). So μ'' >= k there. Hence λ_n >= min{k, j} = j on □. This is the case where the scale exceeds the old level m; the stage level j still dominates.
4. *Stage family (1.69), m >= j + 1* (I:148194-148201; one-sided form "Q ⊂ Ω_m and Q ∩ Ω^c_{m+1} ≠ ∅", I:48495-48497). □ lies in the region of level >= m and has scale m. There μ >= m, and μ'' >= m because Ω_m misses Z''_m (for m <= k_0, by Z''_m = (Ω^{~5}_m)^c ∩ Z) or μ'' >= k >= m (for m > k_0, as in case 3). So λ_n >= m.

Cases 2-4 use the closed form, which holds on the running class component X (I:133454-133460). A cube condition reads only □ ∩ X (I:148147-148148, "a gauge transformation u defined on □ ∩ X"), so only cubes meeting X matter. Let y ∈ □ \ X. The segment in □ from a point of □ ∩ X to y leaves X. Its first point outside X lies in Λ_k: X is a component of Z ⊂ Z_k = Λ^c_k (I:131963-131965), and a cell adjacent to X outside it is not in Λ^c_k. That point is within sup-distance 2ML^kη of y, since □ has side C L^λ M η <= 2ML^kη. The boundaries of Λ_k and Ω_k are at least 2MR_k L^k η apart (CMP 119, quoted at I:63572-63574), and R_k >= L > 2 (I:63570). So y ∈ Ω_k. There the level is k >= λ, in B_k and in every stage structure of the step (λ_n = min{μ'', max{k, j}} = k on Ω_k ∩ X'; live pieces miss Ω_k, since W_a ⊂ Ω^c_{k_a} ⊂ Ω^c_k). *Older live pieces inside X.* On an older component X_a, use the frozen determining set. For the current attempt, X_a ⊂ Z_h ⊂ (Ω''_{h+1})^c (I:134451-134458), and Z_h ⊂ Ω_{h+1}^c (I:63575-63576). Thus families with lower containment index above h, including case 3, do not meet it. At indices at most h, the current preparation leaves the level regions unchanged (I:92002). Apply the family argument at the date that owns the cube, with the innermost-piece precedence of I:132981-132989. Recursion is through strictly smaller arrest densities (T1), hence terminates. A later attempt does not apply its running formula afresh to an older frozen component. Off every running class component the structure is that of B_k, and case 1 applies. If λ >= 1, each case gives □ ⊂ Ω_λ ⊂ Ω_1. QED.

*What is read and not rebuilt.* The family definitions are Balaban's CMP 122a pp. 190-191 and CMP 119 (2.38) as the account quotes them; CMP 122a is not in `~/ym4d-papers`. The closed form is the account's (unmarked lemma 4.27:lem-determining-set-order). In case 3 the account's quotation of (1.67) writes the side CML^jη: so the scale is j.

**Corollary F' (levels at the completion date).** Let 𝔅 ≼ B''_k and □ ∈ Q_𝔅 of family (λ, w). Then o >= λ on □ ∩ Ω_1(𝔅).

*Proof.* Lemma F gives ℓ_𝔅 >= λ there. Levels never fall along the time order: each elementary move (t1)-(t4) has ℓ' >= ℓ (I:133466-133480). The check is short. (t1) raises Ω_{k+1} from k to k+1. (t2) changes λ_n to λ_{n+1}, and max{μ, j} grows with j. (t3) changes nothing. (t4) puts level k, at least the level in force. So o = ℓ_{B''_k} >= ℓ_𝔅 >= λ. QED.

### 3.3 Lemma P2 (the frozen cubes lie in X_c, at points of level at least λ)

**Lemma P2.** Let c be a piece dissolving at the completion step. Let x ∈ W_c, let 𝔅 ≼ B''_k, and let □ ∈ Q_𝔅(x) be of family (λ, w). Then:
- (i) λ <= o(x) <= k_c <= h;
- (ii) □ ⊂ X_c ⊂ Z_h ⊂ D_2;
- (iii) d_sc(y, 𝖲) >= Ř_k - 1 for every y in □, so □ ⊂ K_0;
- (iv) o >= λ on □ ∩ Ω_1(𝔅).

*Proof.* (i) By (Q-pt), x ∈ □. Corollary F' gives λ <= o(x) when x ∈ Ω_1(𝔅). If x is raw at 𝔅, Lemma F gives λ = 0. The frozen level is the actual level at x (I:132484-132486: no later attempt re-levels a point of X_c, clause (T3), I:132108-132110). So o(x) = ℓ_c(x) <= k_c by (T2), and k_c <= h by (T2) for the completing attempt (I:132100).

(ii) □ has side C L^λ M η <= 2ML^{k_c}η, and it contains x ∈ W_c = X_c ∩ Ω^c_{k_c} (I:131972). X_c is a component of the class Z ⊂ Z_{k_c} = Λ^c_{k_c} (I:131963-131965). A point outside X_c is in Λ_{k_c} or in another component of Z_{k_c}, and a path to it from x leaves X_c into Λ_{k_c} ⊂ Ω_{k_c}. The boundaries of Ω_{k_c} and Λ_{k_c} are at least 2MR_{k_c} units of level k_c apart (CMP 119, quoted at I:63572-63574). The account says the same of the piece: the collar X_c ∩ Ω_{k_c} "consists of two layers of cubes of side MR_{k_c}" (I:131977-131978), lengths in units of level k_c as for the blocks of Z_k (I:134666-134667). *Reading:* the unit is that of level k_c, not η. So dist_∞(x, X_c^c) >= 2MR_{k_c}L^{k_c}η - η >= 2ML·L^{k_c}η - η > 2ML^{k_c}η, using R_{k_c} >= L (I:63570) and L > 2. Hence □ ⊂ X_c. Then X_c ⊂ Z_{k_c} ⊂ Z_h (I:138393-138398, from (T2), (T4)) and Z_h ⊂ D_2 (I:91991-92031).

(iii) d_sc(Z_h, 𝖲) >= Ř_k - 1 ((β), I:92094-92096). And Ř_k - 1 >= Ř_k/2 once Ř_k >= 2. Every cell of □ lies in Z_h ⊂ D_2 and outside 𝖲, so in D_2 ∩ G; hence □ ⊂ K_0.

(iv) Corollary F'. QED.

So the account's sentence "A cube of a frozen family of a dissolved piece ... lies two LMR_{h+1}-layers inside S, hence whole in D_2 \ B_S" (I:136753-136756) holds with B_S := D_2 \ K_0, by (ii)-(iii). Raw cells of W_c are allowed (I:133037-133051): they lie in K_0, not K_+. A cube of family λ >= 1 contains no raw cell (Lemma F). A cube of family 0 has side at most 2Mη and uses the zero-level gauge in section 4.2. It is not by definition every raw (3.35)_0 cube: the account allows side 10Mη (I:142771-142783). B1 covers its own collar read set; full raw-core matching stays open.

### 3.4 Corollary B2(c'), the repaired cube clause

**Corollary B2(c').** Retain (LR), (I-A), full (I-D), (I-G), (I-N0), (I-R), (I-T), (I-K), (Q), the effective frozen-family definitions/time order, (Q-pt), H14.1 on its admitted local cube and boundary class, (M*), and the inherited base ceilings. Neither (K-id) nor ca-f's layer inputs supply these hypotheses. Assume also the floor (M') M >= 8 L W_aux, the ceilings (Γ_4) and (Γ_5) below, and Ř_k >= 64 L. Let □ be a cube of side n s, s := L^λ η, n <= CM, λ >= 1, such that
- (S1) o >= λ on □ (scale relation), and
- (S2) □ contains a point x with d_sc(x, 𝖲) >= Ř_k/2 and x in G.

Then there is a gauge u on □ with U_2^u = e^{iηA} and s|A|, s^2|∇^η A| <= (φ_flat/64) B C M α_{0,λ}.

By Lemma P2, (S1) and (S2) hold for every cube of Q_𝔅(x), x ∈ W_c, 𝔅 ≼ B''_k, of family λ >= 1, and for every cube of the frozen family of a dissolving piece. These are all the cubes that consumers R and A route to the base bound (section 3.1). The cube clause they read is F w_□ B C M α_{0,λ} with F >= φ_flat and w_□ >= 1. So B2(c') gives 1/64 of it.

*Proof.* *The read set.* b102 H14.1 (`library/b102.md` 1840-1866) encloses □ in an aligned cube of side M''s, M'' <= n + 2W_aux, and adds auxiliary collars of total width at most W_aux s/(1 - L^{-1}) <= 2W_aux s. It reads U only on these and on stencils of one lattice step; the further collar carries the identity and is not read. So every read lies in Q^+ := {z : dist_∞(z, □) <= 5 W_aux s}. W_aux is fixed before the separation floors (b102 order of constants, lines 1924-1933), hence before M.

*Scale relation on Q^+.* By (S1), □ ⊂ Ω_λ(B''_k), read in the effective frozen nest of (I-G), not an unmodified nest through an older piece. The zone of level λ - 1 has dist_∞(Ω^c_{λ-1}, Ω_λ) >= M L^{λ-1} η ((I-G)(a); (G) at I:137089-137092, "each stratum is at least one M-cube of its own scale wide"). By (M'), 5 W_aux s = 5 W_aux L^λ η < M L^{λ-1} η. Hence Q^+ ⊂ Ω_{λ-1}: every read has level at least λ - 1.

*Distance on Q^+.* Q^+ has sup-diameter at most (2M + 10 W_aux) L^λ η <= 3 M L^λ η, as M >= 16 W_aux. Q^+ is a cube inside Ω_{λ-1}. Join x to any point z of Q^+ by four axis-parallel segments inside Q^+. Follow this path until any first exit from G. Before that exit, each segment has length at most 3ML^λη and crosses at most 3L + 1 M-cubes of level >= λ - 1, of side >= ML^{λ-1}η. Its accumulated scaled distance is at most 4(3L + 1) <= 16L by (I-G). Reaching the source band would contradict d_sc(x, 𝖲) >= Ř_k/2 > 16L. The cut is inside that band, so the path cannot leave G across the support boundary either. Hence Q^+ ⊂ G, and d_sc(z, 𝖲) >= Ř_k/2 - 16L >= Ř_k/4.

*Regularity on Q^+ at scale λ.* Let p be a plaquette (or b a bond) read on Q^+, attached by the read-complete incidence convention to a block y' of level j := o(y') >= λ - 1, with the inherited range 0 <= j <= h of B2(a). B2(a) gives ρ(y') <= 2 B_3 c_R ε^D_j, so (T1) gives |dU_2(p) - 1| <= 2 B_3 c_R ε^D_j L^{-2j} and the divergence test at L^{-3j}. Compare with scale λ:
- if j = λ - 1: ε^D_{λ-1} <= c_R ε^D_λ by (I-R), so the bounds are at most 2 L^2 B_3 c_R^2 ε^D_λ L^{-2λ} and 2 L^3 B_3 c_R^2 ε^D_λ L^{-3λ};
- if j >= λ: ε^D_j <= c_R max{1, j - λ}^{1/2} ε^D_λ, using the identical radius at j = λ and (I-R) at a positive difference. Since max{1, j - λ}^{1/2} L^{-2(j-λ)} <= 1 (and likewise with exponent −3(j−λ)), the bounds are at most 2 B_3 c_R^2 ε^D_λ L^{-2λ} and the same with L^{-3λ}.

So U_2 obeys (T1) read at scale λ on Q^+ at radius ε' := 2 L^3 B_3 c_R^2 ε^D_λ <= 2 L^3 B_3 c_R^2 δ_D(t_γ) α_{0,λ}. This is the hypothesis the gate states for H14.1 (gate section 5, B2(c)).

*Gauge.* H14.1 gives s|A| + s^2|∇A| <= C_L M'' ε' on □, provided C_L M'' ε' is below H12's fixed ceiling c_12 (b102 lines 1882-1885). The ceilings

  (Γ_4)  128 C_L (CM + 2 W_aux) L^3 B_3 c_R^2 δ_D(t_γ) <= φ_flat B C M,
  (Γ_5)  B C M sup_{t >= t_γ} α_0(t) <= c_12,

give C_L M'' ε' <= (φ_flat/64) B C M α_{0,λ} <= c_12. (Γ_4) has degree p_0 + 2r - q < 0 under (Q); (Γ_5) has degree minus infinity; both are fixed last. QED.

*Not covered.* (a) A cube that meets K_0 but violates (S1) is not covered; no consumer routes one to the base bound. (b) b-in.md's "every cube of side at most CML^λη meeting K" is withdrawn. (c) The floor (M') is new; it is of the kind b102's order of constants allows ("Choose the original block and separation floors large ... for ... the independent auxiliary gauge family", b102 lines 1927-1929). M is fixed at Stage 6 of the account's order (I:1537), after d, L and the local constants.

## 4. BLOCK 2: placement with raw points, and the sets the consumers use

### 4.1 Lemma P' (placement, repaired)

**Lemma P'.** Let c be a piece dissolving at the completion step, and C a completing component.
- (i) W_c ⊂ X_c ⊂ Z_h ⊂ K_0, and W_c ∩ {o >= 1} ⊂ K_+. Raw cells of W_c lie in K_0 \ K_+.
- (ii) Every cube of Q_𝔅(x), x ∈ W_c, 𝔅 ≼ B''_k, and every cube of the frozen family of c, lies in X_c ⊂ K_0 and satisfies (S1), (S2), with B2(c') used when λ >= 1; a family-zero cube goes to section 4.2.
- (iii) Every block of level <= 1 within 20Mη of Col(C) lies in Z_1 ⊂ Z_h ⊂ K_0. Every index-zero cube meeting Col(C) has at most 10M sites per side (I:142775-142777).

*Proof.* (i) X_c ⊂ Z_{k_c} ⊂ Z_h by (T2), (T4) (I:138393-138398). Z_h ⊂ D_2 and d_sc(Z_h, 𝖲) >= Ř_k - 1 >= Ř_k/2 (section 2). The cells of Z_h are in the support of B_2 and off 𝖲, so in G. Hence Z_h ⊂ K_0. (ii) is Lemma P2. (iii) is the first paragraph of the proof of B1 (gate section 4: ADVANCE). QED.

This replaces b-in.md Lemma P (i). The false step there was "a cube meeting W_c meets a block of K", with K of positive level (gate section 6). Lemma P2 does not use it. A cube of family λ >= 1 has no raw cell (Lemma F), and every required cube lies in X_c.

### 4.2 The base bound at raw cells (B2 extended to level 0)

Consumer R reads clauses at every x ∈ W_c, raw cells included (I:138367: "Let x ∈ W_c"). At a raw cell the entries 1, 3, 5, 6, 7 are read on the pinned plaquettes, the current and A' (I:142600-142605). The base pair there is the raw datum: U_2 reads V'' off Ω''^{~2}_{h+1} (I:138407-138411), and every bond of a pinned plaquette is a level-0 block, fixed by the constraint.

**Corollary B2(b0).** Under the hypotheses of B2(a) and (Γ_3), entries 1, 3, 5 of (U_2, J(U_2)) at every raw block y of K_0 are at most (φ_flat/64) r_a(0), and entries 6, 7 vanish.

*Proof.* B2(a) is stated for every block y of G of level n >= 0 with d_sc(y, 𝖲) >= Ř_k/4, so it holds at n = 0: ρ(y) <= 2 B_3 c_R ε^D_0. The proof of B2(b), with the gate's repaired current step (gate section 5, B2(b): η^3|J(U)(b)| <= c_π ρ(y) L^{-3n}, c_π <= 2, B_3 >= 12), uses only this bound and (T1) at level n. At n = 0 it gives |dU_2(p) - 1| <= 2 B_3 c_R δ_D(t_γ) α_{0,0} and η^3|J| <= 4 B_3 c_R δ_D(t_γ) α_{0,0}. (Γ_3) is stronger than 256 B_3 c_R δ_D(t_γ) <= φ_flat (gate section 5). U_2 is real, so A' = 0. QED.

At a pinned raw plaquette, the base equals the datum. A datum plaquette exceeding the required φ_flat α_{0,0}/64 violates that base clause. Failure merely of the stronger (I-D) bound leaves the clause undecided. A full current stencil still needs its own test. B2(b0) uses full (I-D), (LR) and B2(a), including the repaired real-current identity on the complete stencil; the current is not determined by one pinned plaquette. The account's own ambient-inclusion lemma lists the presented pair at raw points of the core as not asserted (I:136398-136405, I:136553-136556).

Cube clause at family 0: an index-0 cube □ ∋ x, x ∈ W_c, has side at most 2Mη and lies in X_c (Lemma P2). Every plaquette in it is attached to a block of level j >= 0 in K_0, so |dU_2(p) - 1| <= 2 B_3 c_R ε^D_j L^{-2j} <= 2 B_3 c_R^2 ε^D_0 =: ε. Here ε^D_j <= c_R max{1, j}^{1/2} ε^D_0: use the identical radius at j = 0 and (I-R) otherwise, then max{1, j}^{1/2} L^{-2j} <= 1. The level-zero axial gauge (b102 H14.1, last paragraph, `library/b102.md` 1867-1869; the same bound is input (f) of `4.27:lem-real-point-collar`, I:142639-142646) gives η|A|, η^2|∇A| <= 50(d-1) M ε when 2(d-1)(2M)ε <= 1/10. The ceiling

  (Γ_0)  64 · 50 (d-1) M · 2 B_3 c_R^2 δ_D(t_γ) <= φ_flat B C M,  and  12 M · 2 B_3 c_R^2 δ_D(t_γ) sup α_0 <= 1/10,

gives 1/64 of the family-0 cube threshold BCMα_{0,0}. The first inequality of (Γ_0) has degree p_0 + 2r - q < 0; the second decays exponentially. Both are fixed last.

### 4.3 B_S: replacement band and retained consumer obligations

The account describes B_S as a subset of the cut surface (I:138358-138363), as the excluded set near the cut (I:136725-136726), and in the region holding the two layers D_2 (I:142294-142297). Here **B_S^{new} := D_2 \ K_0**, written B_S, is the excluded band near the cut. This explicitly replaces the literal surface description. An interior band is not a subset of ∂(Ω''_{h+1})^~. Placement does not establish equality with every description or verify every consumer use.

| Use of B_S in the account | Status with B_S^{new} := D_2 \ K_0 |
|---|---|
| R: placement and base, I:138402-138404, 138438-138450 | Conditional on P', repaired B2/B2(b0), family-zero gauges, and (Ref) for the derived base entries. W_c ⊂ X_c ⊂ Z_h ⊂ K_0. |
| A: positive-level core and frozen cubes, I:136724-136756 | Conditional on P', repaired B2 and the qualified Sh' of section 5. Frozen cubes have whole-cube gauges. This does not supply the full raw-core rider below. |
| Completion collar, I:142294-142314, 142583-142586 | Placement follows from the inherited collar geometry and P'(iii). Base-and-layer identification remains (K-id), not a consequence of placement. |
| Deep-current identity, I:92444-92447, 92490-92497 | B_S^{new} ⊂ D_2 reduces the required set to stencils meeting D_2. Retain the actual identity there as (N4), including equality of configurations on the whole current stencil. Changing a set in an assumption does not prove the assumption. |
| Literal B_S ⊂ ∂(Ω''_{h+1})^~, I:138358-138363 | Replaced by “the excluded band near the cut.” The literal consumer description changes. |
| Interface coverage and units, I:139940-139979 | Retained consumer obligation. The marked step asks both for exhaustion by the off-zone list and for the units of its increments. It is not a proved reduction to keystone coverage of B_S. Neither fact is discharged for the newly excluded cells. |
| Raw core rider, I:140758-140766 | Retained consumer obligation: actual raw thresholds, or disjointness from Γ_0. Numbered-entry bounds and family-zero gauges must be matched to the full raw (3.35)_0 and (3.37)_0 clauses. I:136553-136556 expressly withholds this completion-site conclusion. |

At a held point, T^B(y) = γ_0^(k_c) >= 5α_{0,0} (I:132488-132502, 132884-132914). Thus an established φ_flat α_{0,0}/16 current bound is more than sufficient for that source threshold. This comparison does not replace raw-core matching. A family-zero cube of side 2Mη is not every (3.35)_0 cube; I:142771-142783 permits side 10Mη. B1 covers its own collar read set. Matching every raw point of the enlarged core remains the account's existing raw-core obligation.

For the restricted positive-level numerical core calculation, coverage of the discarded band is the remaining regional issue. For every consumer use, interface units and raw-core matching also remain. These obligations are neither solved nor reassigned here.

## 5. BLOCK 3: the layer kernels and Proposition Sh

The gate's blocking step (gate section 7) is the passage from the tuple bound at each layer's kernel (ca-f Proposition R) to the size N_{U_partial}(H_s) with the covariant derivative at the preceding partial product, which Lemma A_n reads. The conditional repair uses read-complete (K-id) as a named matching input and Lemma K for the specified alternative/full square. The cited passages do not independently establish all of (K-id).

### 5.1 (K-id): the kernel of each layer is the configuration it multiplies

**(K-id), retained matching input.** At the completion site, on D_2 and every complete local read set used below, in the same presentation gauge:
- (i) the pair at 𝔟_2 is (U_2, J_2), J_2 = 𝒥(U_2);
- (ii) for s ∈ {3, 4}, H_s is the response field of the layer theorem at the kernel (W_s, σ_s), where W_s is the pair at stage s: W_3 = U_2 and W_4 = e^{iηH_3} U_2;
- (iii) the presented chain at (t_3, t_4) is e^{iηt_4H_4} e^{iηt_3H_3} U_2 with current J_2 + Σ_s s^♯_{σ_s}[t_s H_s]; the consumers read b_2, b_3, b_4 and the two segments b_2b_3 (t_4 = 0) and b_3b_4 (t_3 = 1) (I:142334-142338, I:142563-142570).

*What the five source groups supply.* These are the account's readings of Balaban's construction, with the following qualifications.

| Source | Contribution and retained matching |
|---|---|
| I:92022-92024; 92401-92447 | The real minimiser and field equality on D_2. The presentation-current identity is separate hypothesis (b). Retain (N4) and complete stencils; equality at one point does not prove it. |
| I:73068-73136 | Key containment uses the stage pair as kernel and assumes that pair belongs to its regularity class. Sequential identification is conditional on the actual stage construction and admission. |
| I:142473-142480 | Local algebra reads the derivative at the preceding partial product. This identifies the needed norm; it does not separately identify the cancellation-based response tuple's kernel. |
| III:9174-9193; 10186-10194 | The rows put (1.54) before (1.51), carrying the frame within each row. Each row also re-minimises, Ξ = e^{iηH_2}P_1. Row order alone does not prove that the next row starts exactly at P_1. No contradictory kernel is exhibited; matching remains. |
| I:92377-92391; 142292-142314; 142563-142570 | H_3 uses the current of U_{1,2}; the displayed chain and currents have the stated form; rotation is trivial on D_2. The core base-and-layer fact is attributed jointly to the arrest theorem and layer construction. The text does not separate a proved construction half from a purely geometric half. |

Keep (K-id) on every local read set as an explicit input. Using it as an input is acyclic; claiming these citations independently supply it would overstate the check. No arrest-theorem conclusion is used to discharge it.

*Compatibility with the cancellation datum.* Given (K-id), apply ca-f's (N1) to those same kernels, actual admissible data, norms and gauge. (N2)-(N4) must use the same field-datum operator. The H_3 datum is (f_1, arg_{3,2}), with f_1 = G''(σ)J^{𝔟_2} under (N4); H_4's datum is g_k B, supported in 𝖲. Retain (N7), p(W_s) <= 1, at each actual kernel and every required read block. Merely changing the kernel symbol in a weighted estimate does not supply these admissions.

### 5.2 Lemma K (changing the connection by a left factor)

Write (∇_{W,μ} h)(x) := η^{-1}(Ad(W(x, x+ηe_μ)) h(x+ηe_μ) - h(x)); the proof is the same for the transport in the other direction. For a block y of level n put l := L^n η and N^W_y(h) := sup max{l|h|, l^2|∇_W h|} over the bonds read at y, including the endpoint values of h required by each transport.

**Lemma K.** Let W = e^{iηA'}U on the bonds read at y, with U G-valued and η|A'| <= 1/80. Let X be a g^c-valued 1-form there with sup l|X| <= 1/100, and W' := e^{iηX}W bondwise. Then for every g^c-valued 1-form h,

  l^2 sup |(∇_{W'} - ∇_W) h| <= 2.1 (sup l|X|)(sup l|h|),   N^{W'}_y(h) <= (1 + 2.1 sup l|X|) N^W_y(h).

*Proof.* On a bond b, Ad(W'(b)) - Ad(W(b)) = (Ad(e^{iηX(b)}) - 1) Ad(e^{iηA'(b)}) Ad(U(b)). Ad(U) is an isometry for the operator norm. ‖e^{ad Z} - 1‖ <= e^{2|Z|} - 1 <= 2|Z| e^{2|Z|} and ‖e^{ad Z}‖ <= e^{2|Z|}. So l^2|(∇_{W'} - ∇_W)h(b)| <= l^2 η^{-1} · 2η|X(b)| e^{2η|X(b)|} e^{2η|A'(b)|} |h| <= 2 e^{0.02 + 0.025} (l|X|)(l|h|) <= 2.1 (l|X|)(l|h|), since 2e^{9/200} <= 400/191 < 2.1 and η|X| <= l|X| <= 1/100. The second bound follows, since l|h| <= N^W_y(h). QED.

*Use.* Under (K-id), on the segment b_2b_3 the left factor e^{iηt_3H_3} acts on U_2 = W_3. On b_3b_4 the left factor e^{iηt_4H_4} acts on e^{iηH_3}U_2 = W_4. So N^{U_partial}_y(t_s H_s) = t_s N^{W_s}_y(H_s): Lemma K is not needed on the consumers' segments. It covers two other cases. (a) If W_4 = U_2 (the alternative the gate names), then U_partial = e^{iηt_3H_3}U_2 on the square, with X = t_3 H_3. (b) Inside the square (t_3 < 1, t_4 > 0) under (K-id), U_partial = e^{iη(t_3-1)H_3}W_4, with X = (t_3 - 1)H_3, |t_3 - 1| <= 1. In both cases N^{U_partial}(t_4H_4) <= (1 + 2.1F) N^{W_4}(H_4) <= 1.02 N^{W_4}(H_4) when l|H_3| <= F <= 1/200. This proves the specified conditional comparison. Lemma K does not identify an otherwise unspecified actual W_4.

### 5.3 Proposition Sh' (repaired)

**Proposition Sh'.** Retain all of the following premises.

- Read-complete (K-id) in the presentation gauge, with the matching of section 5.1.
- ca-f's (N1)-(N8), including actual-kernel (N7) at W_3, W_4 and every required kernel/read block. Retain the actual segment-current identification and the same field-datum operator in (N2)-(N4).
- (G-sep) extended to every block of K_0: for z ∈ K_0 and x ∈ T, d_sc(z, x) >= d_sc(z, 𝖲) − 1. Retain Lemma E' (including n = 0), B2, B2(b0), the inherited flow/radius inputs, and δ_R <= min{δ_br, wδ/2}.
- (Ref) for the derived base entries, and **full global 1(e) admission** (I:131580-131586). Each actual global stage kernel, in its required presentation, has a_♭ <= γ̄_0(t_k). Its layer obeys N_·(H_s) <= μ in precisely the norm and on the determining set of 1(e). The triples are admitted there, refer to the same derived object, and satisfy α~_{0,m} >= c~ α_{0,m}. These global facts must come from the admitted stage construction without ambient inclusion's conclusion. They do not follow from bounds on K_0.
- For that admission, use the later frozen shell n = o(x), not automatically the finer predecessor level λ_s(x). Retain the structure/shell/reference-level distinction and matching of I:119564-119584, 122290-122325, 125599-125646, 148158-148169. Do not change a shell denominator silently; birth radii use I:131441-131446 only after this matching.
- (c4)/(Ce7) as hypotheses on constants, evaluated with both smallness quantities at γ̄_0(t_k); (G-global) and (Γ_Sh') below; and α_0(t) <= 1/10 for t >= t_γ. All coupling-dependent quantities in a comparison are evaluated at the same t under one supremum.

Then at every block y ∈ K_0 of level n >= 0, on the segments b_2b_3 and b_3b_4:

- (a) entries 1, 3, 5, 6, 7 differ from their values at b_2 by at most (3/64) φ_flat r_a(n);
- (b) entries 2 and 4 obey Q_e(chain)(y) <= Q_e(𝔟_2)(y) + (3/64) φ_flat r_e(n), e ∈ {2, 4}, one-sided;
- (c) the G-part, hence every cube gauge, is that of U_2.

After the stated triple/radius matching, the radius ratio r_a(μ)/r_a(m) >= (1+β_0)^{-2} g^{-1/2} L^{e_a g} >= 1 for μ < m (I:131441-131446) gives the same bounds with r_a(n) replaced by r_a(n') at a finer birth index n' <= n. They hold a fortiori at thresholds F w c r_a with F >= φ_flat and w, c >= 1. Direct entries and unchanged gauges use the local premises. Derived entries additionally require the full global admission just stated.

*Proof.* *Step 1, layer sizes.* Take δ_R <= min{δ_br, w δ/2}, so p_T = e^{-δ_R d_sc(., T)} lies in M^∧_{δ/2} (ca-f Step 1 with δ/2; gate section 7: "Taking δ_R <= wδ/2 is valid"). Proposition R (ca-f Step 3) gives E_{y'}(H_s) <= (C_D/K_u) ε_Q(k) p_T(y') at every block y', in its unit l_{y'}, at the kernel W_s. The left-factor lemma at y reads h on Δ~(y) and one step further (I:141270-141278). The blocks y' met have d_sc(y, y') <= 2 and level n - 1, n or n + 1 (Lemma C (C0)). Passing to l = L^nη costs at most L for |h| and L^2 for |∇h|. Hence

  N^{W_s}_y(H_s) <= μ(y) := L^2 e^{2δ_R} (C_D/K_u) ε_Q(k) p_T(y).

μ is a constant multiple of p_T, so μ ∈ M^∧_{δ/2}. By extended (G-sep) and Lemma E' (valid also at n = 0, since the same disjoint zone crossings start at level 1), d_sc(y, T) >= (1/2)[Ř_k/2 + (L-2)(h - n - 1)^+] - 1. By (N8) and (I-R), ε_Q(k) <= K_Q A^+ ρ_C max_i α_{i,k} and α_{i,k} <= c_R (k - n)^{1/2} α_{i,n}, with k - n = Ř_k + h - n. Hence

  μ(y) <= C_S (Ř_k^{1/2} + S_2) e^{-δ_R Ř_k/4} α_{*,n},  C_S := L^2 e^{3δ_R} (C_D/K_u) K_Q A^+ ρ_C^2 c_R,  S_2 := sup_{m>=0} m^{1/2} e^{-δ_R(L-2)(m-1)^+/2},

using (a + b)^{1/2} <= a^{1/2} + b^{1/2}. Put F(y) := μ(y). (Γ_Sh') gives F(y) <= α_{*,n}/200 <= 1/2000.

*Step 2, the kernel.* By (K-id) and Step 1, N^{U_partial}_y(t_s H_s) = t_s N^{W_s}_y(H_s) <= F(y) on both segments, since N is homogeneous of degree one in h.

*Step 3, entries 6 and 7.* On b_2b_3 the base has A' = 0, so A'(t_3) = t_3 H_3 exactly, and ∇_U = ∇_{U_2} = ∇_{W_3}. So l|A'| and l^2|∇_U A'| are at most F. On b_3b_4, Lemma A_n (ii_n), (iii_n) apply with base W_4, h = t_4 H_4, N <= F < 1/40 and a = sup l|H_3| <= F < 1/80. They move these entries by at most 1.06 F. In total, l|A'| <= 2.06 F and l^2|∇_U A'| <= 2.06 F, against α_{1,n} l^{-1} and α_{1,n} l^{-2}.

*Step 4, entries 1 and 5.* Entry 5 is the G-part; it does not move. Entry 1 on b_2b_3: Lemma A_n (i_n) with base U_2, θ <= (φ_flat/64) α_{0,n} L^{-2n} by B2(b), (b0). So 5.6 θ L^n <= 0.01 and the move is at most 2.91 L^{-2n} F. On b_3b_4 the base is W_4, and the first layer has moved its plaquettes by at most 2.91 L^{-2n} F. So θ_4 <= L^{-2n}[(φ_flat/64) α_{0,n} + 3F] (gate section 7, entries 1 and 5). Then 5.6 θ_4 L^n <= 5.6 (1/640 + 3/2000) < 0.02, and the move is at most 2.92 L^{-2n} F. In total at most 6 L^{-2n} F, against r_1(n) = α_{0,n} L^{-2n}.

*Step 5, entry 3.* Lemma S of ca-f at the kernel W_s, in the local unit l (gate section 7, row "Current": ADVANCE at the kernel of each layer, given (N6), (N7), the smallness bound and the segment-current identification). It gives l^3|s^♯_{σ_s}[t_s H_s](b)| <= t_s Kcur E_y(H_s) <= Kcur F. So η^3|𝒥| moves by at most 2 Kcur L^{-3n} F in total, against η^3 r_3(n) = α_{0,n} L^{-3n}.

*Step 6, entries 2 and 4: admission and numerical spend.* Put D := L^2 e^{2δ_R} C_D/K_u, so μ(z) = D ε_Q(k)e^{−δ_R d_sc(z,T)}. For nonempty T its global supremum is D ε_Q(k). The exponentially smaller estimate of Step 1 holds on K_0 only. Separation of K_0 from T changes neither this supremum nor a field's size on T. Steps 3-5 likewise do not prove a global a_♭ bound. The factor c_B in 1(e) supplies no compact-support or extension theorem.

First retain full 1(e) admission as a premise: the actual global stage kernels have a_♭ <= γ̄_0(t_k), their layers satisfy its norm bound on its determining set, and the triples and α~_{0,m} >= c~ α_{0,m} match as in the statement. These facts cannot be inferred from this note's core estimates.

Second impose the global ceiling

\[
 \sup_{t\ge t_\gamma}
 \frac{D K_Q A^+\rho_C\,C^{\rm rad}e^{-t/2}t^q}
 {5(1+\beta_0)^2L^2(L+1)C^{\rm rad}e^{-t/2}t^{q+r}}
 \le1. \tag{G-global}
\]

Here ε_Q(k) <= K_Q A^+ρ_C max_i α_{i,k} is the inherited conservative budget. The ratio is a fixed constant times t^{−r}, tending to zero. Thus this is an admissible final ceiling. It gives κ_max = sup μ <= γ̄_0(t_k) on the whole determining set. With the admitted a_♭ bound, (c4)/(Ce7) at both quantities equal to γ̄_0(t_k) implies C^b(a_♭ + κ_max) <= 1 by monotonicity (I:131850-131862, 137279-137290). This uses a hypothesis on constants, not ambient inclusion's conclusion.

Apply 1(e) to the same derived object with the matched later frozen shell n = o(x). Each layer gives Q_e^+ <= Q_e(1 + π_×) + π r_{e,n}, with π_× <= π := K^b_S μ(y)/α~_{0,n} <= K^b_S F/(c~ α_{0,n}). The local exponential estimate now bounds the increment at the core point. Start from Q_e(𝔟_2) <= (φ_flat/64) r_{e,n}, supplied by B2(d) under (Ref). While Q_e <= r_{e,n}, each move adds at most 2π r_{e,n}. Two moves add at most 4π r_{e,n}; (Γ_Sh') gives **4π <= 3φ_flat/64**. Hence the iteration stays below r_{e,n} and yields the stated one-sided increase. The numerical consequence is conditional on global admission, which remains an input.

*Step 7, local absorption and order.* Put c_sh := max{2.06, 6, 2 Kcur, 4 K^b_S/c~}. Retain the local ceiling

  (Γ_Sh')  sup_{R >= R_γ} c_sh C_S (R^{1/2} + S_2) e^{−δ_R R/4} <= min{(3/64) φ_flat, 1/200}.

R_γ := inf_k Ř_k tends to infinity as γ tends to zero (I:77940-77942), so (Γ_Sh') is an exponentially decaying final ceiling. Steps 3-6 then bound the spend by (3/64)φ_flat of the threshold at weight one. Part (c) follows from the left-factor algebra: it keeps U and its gauges. This local absorption does not supply global admission. QED.

The floors (M*) and (M') follow the early local and auxiliary constants; round M upward to its required power of L. The radius exponents precede the final coupling ceiling. Here p_1 < p_0 < q (I:1351-1364), so A^+ is finite; no alternative polynomial correction is needed. Impose (G-global), of degree −r, and (Γ_Sh') last. Read γ̄_0(t), the budget and all coupling-dependent quantities at the same t under one supremum (I:131815-131826, 132934-132941). A free supremum of α_* cannot replace comparison with the dated γ̄_0(t_k).

*What changed from b-in.md Proposition Sh.* The norm passage at b-in.md lines 211-216 is replaced by Step 2, through (K-id). The second-layer curvature uses θ_4 (Step 4). Entries 2 and 4 are one-sided, conditional on full global 1(e) admission, its norm/triple/radius matching, (c4)/(Ce7), and (G-global) (Step 6). The result holds on all of K_0, raw blocks included (Lemma E' and Lemma A_n hold at n = 0). The constants are those of the gate's repair, with F <= α_{*,n}/200 in place of 1/100 so that Step 4 closes at n = 0.

### 5.4 The account's three shares (REVISE of b-in.md line 226)

Consumer R (c) asks the increments to total at most 3θ/64 (I:138383-138387), and (d) adds 1/64. Consumer A adds the same (I:136726-136732). Under all its stated premises, Sh' gives this total, with entries 2 and 4 one-sided, which is the direction spend reads. The account also names three separate shares (bend, source, map 𝐇'), a bend floor, an ownership floor, floors at a set Γ_♭ (I:138454-138464), and a use "at halved far factors" for the dissolved pieces at the t-disc of site (L) (II:1208-1212). These are not reconstructed. A total bound does not identify them. If "halved far factors" means the decay rate δ_R halved, then (Γ_Sh') with δ_R/2 in place of δ_R gives the same total; that reading is unverified and must not be used to close the analytic-disc application. “Halved far factors” does not state “halve the decay rate.”

## 6. The gate's REVISE items, as applied here

b-in.md is not edited (row 399). Each REVISE of gates/b-in-gate.md is applied in this note as follows.

| Gate item | Applied here |
|---|---|
| §2 (LR): read-complete patches, B_3 >= 12, boundary inequality at vertices without a patch; Theorem G's cut term with the artificial datum retained | Section 2, kept as the form of (LR) and Theorem G that B2(a) uses. |
| §2 "ρ(y) = t(y)" on pinned blocks false for full (T1) | Replaced by the gate's stencil repair; used in B2(b0) (section 4.2). |
| §3 core definition; 𝖲 vs S | K_0, K_+, B_S as the gate defines them; 𝖲 and S kept apart (section 2). The literal surface description is replaced; interface coverage/units and raw-core matching remain consumer obligations (section 4.3). |
| §3 (I-D) attribution | (I-D) is required on the full test set, mixed-level transports included; it is an input, not the account's (γ) alone (section 2). |
| §3 Lemma C (C2): the last edge reaches the cut, and the cut region reached is the source band | Part of (I-G), as a geometric input (section 2). |
| §3 Lemma C: enlarged reset neighbourhoods need their step bound rechecked | Rechecked with reach R_* = 4R_1M_1 + 2W_aux + 1; floor (M*) replaces (M) (section 2). |
| §4 ceiling terminology | Section 2: degrees p_0 - q, p_0 + 2r - q, minus infinity; ceilings on γ, not caps. |
| §5 B2(b) current step | The gate's formula η^3 J(U) = π Im(η D^{η*}_U ∂U), c_π <= 2, used in B2(b0). |
| §5 B2 hypothesis list | The full retained list is explicit in B2(c') (section 3.4), including H14.1's admitted class, the geometry, (Q-pt), floors and ceilings; (Γ_0) treats family zero. |
| §5 B2(c) BLOCK | Conditionally repaired by F/F', P2 and B2(c') with the equality case and full inputs (section 3). |
| §6 Lemma P BLOCK | Placement repaired by P'; raw bounds require full base inputs. Identification with every B_S use is not established (sections 4.1-4.3). |
| §7 Sh BLOCK; entries 1 and 5 at the second layer; derived entries; line 226 | Connection comparison conditional on read-complete (K-id) and Lemma K. Sh' retains ca-f (N1)-(N8), actual-kernel admission, extended (G-sep), E', flow/radius inputs, full global 1(e) admission with matching, (Ref), (c4)/(Ce7), (G-global) and (Γ_Sh'). The share/disc package remains open. |
| §8 absence claim | Wording: "no independent, noncircular supplier located in the four supplied sources" (section 1). |
| §9 final claims, "new mathematics", "kind" | Result below: conditional conclusions only. Theorem G's local-profile idea has the outline predecessor SA 9678-9691 (Theorem 2, sketched); no priority is claimed. |

## 7. Tries to kill, and what survived

No numerical run. Each try is a hand argument.
- *A family cube whose scale exceeds its old level.* CMP 122a (1.67) cubes have scale j but sit in old shells Ω_m, m <= j. Lemma F case 3 shows the stage level there is j. Survives.
- *A cube that leaves its class component, or meets an older nested piece.* Lemma F, last two paragraphs: such points lie in Ω_k at level k, or in X_a where levels are frozen and case 3 cannot reach. Survives.
- *A frozen cube reaching outside X_c, into a finer region.* Lemma P2 (ii): the collar of width 2MR_{k_c} units of level k_c stops it. Survives, under the unit reading stated there.
- *The enlarged H14.1 region reaching finer zones.* (M') keeps the envelope Q^+ within one level of the cube's scale. Without a suitable floor, this envelope argument does not guarantee a minimum read level. Q^+ is an upper envelope of the reads; its reaching finer zones does not show that H14.1 actually reads every such point.
- *Raw cells of W_c.* A pinned datum plaquette exceeding φ_flat α_{0,0}/64 violates the base clause. Failure only of the stronger (I-D) allowance leaves the clause undecided. The current needs the whole stencil (section 4.2).
- *Finer birth indices for entries 2 and 4.* After shell/triple matching, the radius ratio gives r_e(n') >= r_e(n) for n' < n. The shell of the later space is the frozen shell n = o(x), not automatically the predecessor's finer λ_s(x). Replacing the denominator by that of a different shell is not justified by the ordinary radius ratio; retain the matching of section 5.3.
- *The second layer at level 0.* With F <= α_{*,n}/100 the Lemma A_n constant at n = 0 exceeds 3. F <= α_{*,n}/200 restores it (Step 4).

## 8. Named inputs and open items

**New inputs of this note.**

- (Q-pt): a cube of Q_𝔅(x) contains x. The weaker requirement is that each cube routed to the base bound contains a point of W_c.
- (K-id): W_3 = U_2 and W_4 = e^{iηH_3}U_2 in one presentation gauge, on D_2 and every complete local read set. Section 5.1 retains this as matching input, not as independently proved by its five source groups.
- Floors (M*): M >= max{16 L s_0, 8 L^2} R_*, R_* = 4R_1M_1 + 2W_aux + 1; (M'): M >= 8 L W_aux. Round M to its required power of L. Retain Ř_k >= 64 L, (Γ_4), (Γ_5), (Γ_0), (Γ_Sh'), (G-global), and sup_{t >= t_γ} α_0(t) <= 1/10, with the final-ceiling order of section 5.3.
- Full global 1(e) admission, including its actual stage kernels, norm and determining set, admitted triples, later frozen-shell/reference/birth-radius matching and α~_{0,m} >= c~ α_{0,m}. The core estimates do not supply this admission.

**Inputs kept from b-in.md**, with the repairs: read-complete (LR), its actual patches/boundaries and B_3 >= 12; (I-A); full (I-D), including level zero and mixed-level transports; (I-G) with its path metric and effective frozen nests; (I-N0), (I-R), (I-T), (I-K); (Q); effective frozen-family definitions/time order; H14.1 on its admitted class; the inherited base ceilings; (Ref); ca-f's (N1)-(N8), including (N4)'s whole-stencil identity and actual-kernel (N7) at every required read block; extended (G-sep); E'; the flow/radius inputs; and (c4)/(Ce7) with full global 1(e) admission. Local smallness, matching and ceilings are hypotheses, not consequences of placement.

**Open, ranked by what each breaks.**

1. **Interface coverage and units in consumer A.** I:139976-139979 retains both exhaustion of Y' \ 𝖹 by the off-zone list (including rings) and the units of its increments. For B_S = D_2 \ K_0, this note establishes neither fact for the newly excluded cells. The marked step is not a proved reduction to keystone coverage of B_S. It remains consumer A's existing O-ambient obligation, not reassigned here.
2. **Full raw-core matching.** I:140758-140766 requires raw (3.35)_0 and (3.37)_0 thresholds, or disjointness from Γ_0. The source-threshold comparison and genuine index-zero cube convention in section 4.3 must be matched at every required raw core point. The family-zero gauge at side 2Mη and B1's own collar read set do not establish all side-10Mη readings. The account withholds this completion-site conclusion at I:136553-136556.
3. **(I-A), full (I-D), and (LR)'s actual patches/boundaries.** Keep the actual nest, mixed-level tests, minimal orbit, reset patches, complete current stencils and boundary inequalities. At a raw plaquette, failure of the stronger (I-D) allowance alone does not refute the target base clause.
4. **(Q-pt) and read-complete (K-id).** Both remain inputs. The source groups identify intended constructions but do not independently establish all matching. If the specified alternative W_4 = U_2 applies, Lemma K supplies the comparison with a factor at most 1.02. An otherwise unspecified W_4 needs matching or a further comparison, not a symbol substitution.
5. **ca-f's (N1)-(N3), actual-kernel admission/(N7), (Ref), and global 1(e) matching.** (N1)-(N3) retain their owners, stage-claude and B99b-T314. (N7) must hold at every actual kernel/read block. The stage construction must supply global admission, including its norm, determining set, triples and radii, without ambient inclusion's conclusion. Do not drop (N4)-(N8), extended (G-sep), E', geometry, flow/radius inputs, floors or the new ceilings from the conditional input list.
6. **SU(N), N >= 3.** The checked (LR) reset is for SU(2) only. No conclusion for larger N follows here.
7. **Separate shares and the analytic-disc package.** The three named shares, bend/ownership floors, floors at Γ_♭, and the halved-far-factor use at the t-disc (II:1208-1212) remain unreconstructed. The unverified δ_R/2 reading does not close this application.

## Result

**Kind.** Conditional repairs of the three old local failing inferences in `gates/b-in-gate.md`. The account states and invokes the desired sealing conclusions. The earlier bounded search located no independent, noncircular supplier in the four supplied sources; it did not establish absence of a statement. Original arguments by Claude; `gates/b-in-r2-gate.md` records Codex's line-by-line check and qualifications. This revision applies its written repairs, adds no mathematics, and grants no status.

1. **B2(c), enlarged-cube regularity: conditional repair after the equality case.** F/F', P2 and B2(c') supply the routed-cube geometry and whole-read-set bound. Retain (LR), (I-A), full (I-D), (I-G), (I-N0), (I-R), (I-T), (I-K), (Q), effective frozen-family definitions/time order, (Q-pt), H14.1 on its admitted class, (M*), (M'), inherited base ceilings and (Γ_4), (Γ_5); use (Γ_0) for family zero. Neither (K-id) nor ca-f's layer inputs prove this part.
2. **P, raw points and actual frozen cubes: geometric placement repaired conditionally.** (Q-pt), F/F', arrest timing and law-site separation give P2/P': W_c and its routed frozen cubes lie in X_c ⊂ Z_h ⊂ K_0, with raw cells allowed. Raw estimates additionally require the full base inputs. Identification with every use of the account's B_S is not established. The surface description is replaced by the excluded band near the cut; interface coverage/units and raw-core matching remain consumer obligations.
3. **Sh, kernel-to-partial-product norm comparison: conditional repair from read-complete (K-id).** Lemma K handles the specified alternative/full square. The direct spend estimate also uses ca-f's (N1)-(N8), including actual-kernel (N7), extended (G-sep), E', B2/B2(b0), the flow/radius inputs and (Γ_Sh'). Derived entries additionally require (Ref) for the base, full global 1(e) admission with its norm/triple/radius matching, (c4)/(Ce7), and (G-global). Under these premises Sh' gives the stated total 3/64 spend, one-sided for entries 2 and 4, with unchanged G-part and cube gauges. It does not derive global admission from core bounds.

The three original local obstructions therefore have conditional repairs. The full advertised sealing conclusion is not established from the shortened input list. Clauses (b), (c) of room-dissolving and the numerical core calculation may consume the repaired implications only with the complete premises above. The full consumer conclusions still require section 8's interface, raw-core and share/disc obligations. If global 1(e) admission is assumed, repaired Sh' is an implication; if it is supposed to follow from this note, Step 6 remains BLOCK. No arrest-theorem ambient-inclusion conclusion supplies that admission, and no counterexample to the actual completion construction is claimed.

**Not shown.** Every open item in section 8 remains. In particular, failure of (I-D) alone is not a counterexample to the target base clause. No numerical or computer-assisted step discharges any obligation.

**What changes for consumers.** The literal surface description of B_S is replaced by “the excluded band near the cut.” The useful repairs are routed-cube geometry, the whole-read-set bound and conditional connection comparison, with the full Result input lists. Consumer A's interface coverage/units and raw-core obligations are neither solved nor reassigned. The separate share/disc package remains open. CA-BIN remains OPEN; no registry, tree, source note or editable prompt file is changed. Only this note is revised for row 405.

**Next decision.** Consumers must retain the complete premises and their existing open obligations; this edit supplies no new proof lane or status change. Nothing is posted.

**Provenance.** Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker 1, 2026-11-06, pinned at 99d2c3b3f. Account files fetched by URL into a scratch folder of this lane; SHA-256 as in `library/arr.md`. No Balaban page was read in this round; Balaban's statements are used as the account quotes them, and b102's as rebuilt in `library/b102.md`. No computer-assisted step; no numerical run.

## Change log: FINISH row 405

Applied the written repairs of `gates/b-in-r2-gate.md` at checkout `3710994a7da125ce8ea1c07ad1014a6e4fe8b4ff`. Gate line numbers below refer to that pinned revision, Git blob `7dce73cfd493024eb244a6bc4466443efd29d901`. The pre-edit note is blob `55b46f5bb32c449dda4fa06ac876a8baabd693a1` at the same commit. The historical row-399 provenance above is retained. This is an editorial application of the check, not another scientific check, audit or status grant.

| Repair applied | Gate line(s) |
|---|---|
| Retained (Q-pt) as an input; the account does not supply an explicit incidence rule. | 15, 182-183 |
| Replaced the older-component paragraph with the frozen determining-set reading, date ownership, precedence and terminating recursion. | 19-23 |
| Repaired B2(c') at j = λ with the identical radius and max{1,j−λ}^{1/2}. | 31 |
| Retained H14.1's admitted local cube/boundary conventions, effective frozen nest, and read-complete B2(a) incidence with 0 <= j <= h. | 37-40 |
| Rewrote Q^+ containment as a first-exit argument rather than presupposing Q^+ ⊂ G. | 39 |
| Made B2(c') and Result 1 retain the full base/family input list, floors and ceilings, with (Γ_0) for family zero. | 44, 182 |
| Qualified P'(ii): B2(c') is used only for λ >= 1; family zero goes to section 4.2. | 48 |
| Retained full (I-D), (LR), B2(a) and the complete current stencil in B2(b0). | 50 |
| Applied max{1,j}^{1/2} to family-zero radii and distinguished the polynomial and exponential parts of (Γ_0). | 52 |
| Replaced every inference from failure of (I-D) to failure of the base clause with the written pinned-plaquette repair and separate current test. | 54-58, 172 |
| Restricted B_S identification to conditional placement/base uses; collar base-and-layer identification remains (K-id). | 60-65 |
| Retained (N4)'s actual deep-current identity on complete stencils meeting D_2. Set reduction does not prove it. | 66 |
| Explicitly replaced the literal surface description by “the excluded band near the cut.” | 67 |
| Retained both interface exhaustion and increment units as consumer obligations; removed the keystone-only reduction. | 68, 73 |
| Added the raw-core rider, raw thresholds/disjointness, held-point radius comparison and 2Mη versus 10Mη cube distinction; B1 retains its own read set. | 69-71 |
| Recast the five (K-id) source groups by their actual contributions, including row re-minimisation and the joint arrest/construction attribution. | 79-87 |
| Kept read-complete (K-id) and same-kernel/data/norm/gauge/operator matching explicit; no independent supply is inferred from citations. | 89 |
| Included endpoint values in Lemma K's supremum and the hand bound 2e^{9/200} <= 400/191 < 2.1. | 93 |
| Limited Lemma K to its specified alternative/full square; it does not identify an unspecified W_4. | 95 |
| Preserved δ_R <= δ_br as well as δ_R <= wδ/2; recorded E' at n = 0. | 101 |
| Retained ca-f's (N1)-(N8), actual-kernel (N7), segment-current identification, extended (G-sep), E', base and flow/radius inputs in Sh'. | 89, 101-105, 184 |
| Separated global 1(e) admission from local bounds: actual global kernels, a_♭, norm/determining set, admissible triples and radius matching remain premises. | 107-123 |
| Replaced the second (Γ_Sh') inequality with (G-global), its conservative budget and degree −r; applied (c4)/(Ce7) only with admitted global data. | 124-133 |
| Made later frozen-shell, structure/reference-level and same-derived-object matching explicit before birth-radius comparison. | 135, 173 |
| Corrected the two-move numerical spend to 4π <= 3φ_flat/64, conditional on full admission. | 106, 133, 137 |
| Retained the separate-share/floor/disc limitation; the δ_R/2 interpretation of “halved far factors” is unverified and cannot close it. | 141 |
| Narrowed source-absence claims, retained outline credit, and distinguished stated conclusions from an independently located supplier. | 145 |
| Corrected Lemma C's reverse-crossing intermediate bound to max{R_*+L, LR_*+1}L^lη; retained its final bound and floors. | 149-156 |
| Stated rounding of M, exponent order, finite A^+, final ceilings, and same-t comparisons; excluded deriving global admission from ambient inclusion. | 158-160 |
| Repaired section 6's cube, placement and Sh rows to state conditional scope and the complete premises. | 162 |
| Replaced the below-floor H14.1 “counterexample” by loss of the envelope containment guarantee. | 171 |
| Retained and expanded the full section 8 open list, including raw-core/interface obligations, (N4)-(N8), geometry, ceilings and the SU(2)-only scope. | 188 |
| Rewrote Result items 1-3 to the gate's implication table, retaining all inputs. | 180-186, 190 |
| Rewrote former lines 285 and 289: no unconditional consumer delivery, no unchanged-surface claim, no reassignment of consumer A's obligations; CA-BIN remains OPEN. | 186-190 |
