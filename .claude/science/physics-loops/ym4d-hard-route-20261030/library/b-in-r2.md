lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T09:40Z

# b-in-r2: the three BLOCKs of gates/b-in-gate.md for library/b-in.md

FINISH row 399. Pinned at 99d2c3b3f. Finished 2026-11-06T22:18Z. The Result is at the end.

Started 2026-11-06T21:40Z on the Mac mini, worker 1. Proved by Claude, not yet checked by the other model, unless a line says otherwise.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (complete account CA-I, CA-II, CA-III and outline at upstream `31a47c543775`), for every statement, construction and bound cited with a line number. Tadeusz Balaban for the multiscale construction (CMP 89-122). Earlier work here: `library/b-in.md` (Claude, row 389), its check `gates/b-in-gate.md` (Codex gpt-6-astra xhigh, row 397), `library/ca-claude.md`, `library/ca-f.md`, `library/b102.md`.

## 1. Scope, duplicate check, sources

- **Item.** FINISH row 399. Moves: CA-BIN (`library/t0-tree.md` node CA-BIN, registry row CA-BIN, owner `b-in`), the input (B-in) of CA = clause (b) of `4.27:prf-room-dissolving` (CA-I 138348, unmarked) and the core step of `4.27:prf-ambient-inclusion` (CA-I 136490, marked incomplete). If the three BLOCKs close, CA-BIN becomes an implication from named Balaban-instance inputs; if one fails, the sealing package has a stated counterexample or a three-way-failed lemma.
- **Duplicate check (rule 0a).** `grep` of `library/open-core.md` and `library/l17c.md` for b-in, sealing, own-level, B_S, enlarged collar, Proposition Sh, partial product: no match. `library/open-registry.md` line 958: CA-BIN, owner `b-in` (this lane's lineage). FINISH rows naming the sealing package: 382, 383, 387 (digests), 389 (b-in), 397 (its check), 399 (this row). Row 404 (`fc-r2`) is the frame change of `library/fc.md`, a different object. No other row attacks these three BLOCKs. ca-f's (N1)-(N3) belong to other owners (stage-claude, B99b-T314) and are not attacked here.
- **Account label and status.** As in `library/b-in.md` section 1: clause (b) of `4.27:prf-room-dissolving` (CA-I 138348-138483, not marked incomplete) invokes the own-level bound of "the sealing construction" (CA-I 138438-138450); the construction is not stated in CA-I/II/III or the outline (gates/b-in-gate.md section 8, narrowed wording: no independent noncircular supplier located).
- **Sources.** CA-I, CA-II, CA-III and the outline fetched by URL into a scratch folder of this lane; SHA-256 agree with `library/arr.md` (outline d7f77d4d..., CA-I 4cb5cb5e..., CA-II 6a1f74b0..., CA-III 7e36523b...). Line numbers I:, II:, III:, SA: are of those raw files.
- **Rules.** No numerical run. No computer-assisted step.

## 2. Conventions kept from b-in.md, with the gate's renaming

- **Sets (gate section 3).** 𝖲 is the source band of the current localisation: the (2M_1+3 blocks)-neighbourhood of Ω''^{~2}_{h+1} in Λ (I:92468-92469). S := ∂(Ω''_{h+1})^~ is the cut of the room lemma (I:138358). They are different sets. b-in.md wrote S for 𝖲; here 𝖲 is written. G := (support of B_2) \ 𝖲, as in b-in.md section 3. o(y) := ℓ_{B''_k}(y), the level of y in B''_k read with precedence (I:132981-132989; I:136662-136665).
- **Geometry, from the law-site proof (I:91991-92031).** D_2 = (Z'_h)^{~2} ∩ Λ is Z'_h ⊇ Z_h with two layers of LMR_{h+1}-cubes of level h round it; the cut is its outer boundary; (Ω''_{h+1})^{~2} = ((Z'_h)^~)^c (Balaban, CMP 122a p. 195, as quoted at I:92010-92013). So 𝖲 contains the outer layer of D_2 and 2M_1+3 blocks of the inner one, and one full layer separates Z_h from 𝖲: d_sc(Z_h, 𝖲) >= Ř_k - 1 ((β) at I:92094-92096). Here Ř_k = k - h (I:77938-77954).
- **Corrected core (gate section 3).** K_0 := {cells y of D_2 ∩ G : d_sc(y, 𝖲) >= Ř_k/2}, K_+ := {y in K_0 : o(y) >= 1}, B_S := D_2 \ K_0.
- **Inputs kept as named in b-in.md**, with the gate's repairs: (LR) read-complete (gate section 2: every stencil, averaging and gauge read of a reset patch in N(y); B_3 >= 12; a separate boundary inequality at vertices without a patch); (I-A); (I-D) on the full test set, mixed-level transports included (gate section 3); (I-G) including the reading of d_sc as a path metric that counts M-cubes of the local scale (I:91727); (I-N0), (I-R), (I-T), (I-K); floor (M), read as (M*) below. Theorem G, Lemmas I, C, J, BCH, A_n, E' and Corollary B1 are used as the gate passed them (gate sections 2-7). B2(a) is used as the gate passed it: "ADVANCE as a conditional estimate".
- **Lemma C with read-complete patches (gate section 3, last sentence on Lemma C).** A reset patch at a block of level j now reads its box~ (within 4R_1M_1 L^j η of the block, CMP 102 (144)), the averaging contours inside it, the auxiliary gauge collar of total width at most 2W_aux L^j η (b102 1840-1846) and one-step stencils. So it reads within R_* L^j η of the block, R_* := 4R_1M_1 + 2W_aux + 1. In the proof of Lemma C the step bound becomes (R_* + L) L^l η <= 2 L R_* L^l η, as R_*, L >= 1. Read the floor (M) as **(M*)** M >= max{16 L s_0, 8 L^2} R_* (and M >= 4 W_aux). Then (C0) and (C1) hold with the same proofs, since M/(2L R_*) >= s_0 + 1. (C2) holds too: a step moves less than M L^{l-1} η, one cell of level l - 1, since M > L(R_* + L). B1 and B2(a) read Lemma C only through (C0)-(C2), so they hold under (M*). W_aux and R_1M_1 are fixed before M, so (M*) is an admissible floor.
- **Ceilings (gate section 4).** (Γ_1) has degree p_0 - q < 0 in t_γ; (Γ_3), (Γ_4), (Γ_0) have degree p_0 + 2r - q < 0; (Γ_2), (Γ_5), (Γ_Sh') have degree minus infinity. All are upper bounds on γ, fixed last. None is a cap in the sense of I:1246-1253.

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

Cases 2-4 use the closed form, which holds on the running class component X (I:133454-133460). A cube condition reads only □ ∩ X (I:148147-148148, "a gauge transformation u defined on □ ∩ X"), so only cubes meeting X matter. Let y ∈ □ \ X. The segment in □ from a point of □ ∩ X to y leaves X. Its first point outside X lies in Λ_k: X is a component of Z ⊂ Z_k = Λ^c_k (I:131963-131965), and a cell adjacent to X outside it is not in Λ^c_k. That point is within sup-distance 2ML^kη of y, since □ has side C L^λ M η <= 2ML^kη. The boundaries of Λ_k and Ω_k are at least 2MR_k L^k η apart (CMP 119, quoted at I:63572-63574), and R_k >= L > 2 (I:63570). So y ∈ Ω_k. There the level is k >= λ, in B_k and in every stage structure of the step (λ_n = min{μ'', max{k, j}} = k on Ω_k ∩ X'; live pieces miss Ω_k, since W_a ⊂ Ω^c_{k_a} ⊂ Ω^c_k). *Older live pieces inside X.* Let X_a ⊂ X be the component of an older live piece. By (T3) no later attempt re-levels a point of X_a (I:132108-132110), so on X_a the stage level, μ and μ'' all equal the frozen level; B''_k is "frozen on every piece then live" (I:133498). Cases 2 and 4 read Ω''_m and Ω_m as level regions of these sets, so they hold on □ ∩ X_a. Case 3 cannot meet X_a: W_a ⊂ Ω^c_{k_a}, and the collar X_a ∩ Ω_{k_a} keeps level k_a. Since k_a <= h (T2) and h < k_0 + 1 (2N_0 <= N_k, I:93415), X_a misses Ω_{k_0+1} ⊇ □. Off every running class component the structure is that of B_k, and case 1 applies. At a point of a live piece the structure is the frozen one of the innermost live piece (precedence, I:132981-132989). That is the stage structure of the piece's own attempt at its stage n^+ (I:121787-121790), read on its own nest, and cases 2-4 and this paragraph apply to it at its density k_a. If λ >= 1, each case gives □ ⊂ Ω_λ ⊂ Ω_1. QED.

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

So the account's sentence "A cube of a frozen family of a dissolved piece ... lies two LMR_{h+1}-layers inside S, hence whole in D_2 \ B_S" (I:136753-136756) holds with B_S := D_2 \ K_0, by (ii)-(iii). Raw cells of W_c are allowed (I:133037-133051): they lie in K_0, not K_+. A cube of family λ >= 1 contains no raw cell (Lemma F). A cube of family 0 has side at most 2Mη; it is the genuine index-zero case of B1 and Lemma A (gate section 4, last row).

### 3.4 Corollary B2(c'), the repaired cube clause

**Corollary B2(c').** Assume the inputs of B2(a), the floor (M') M >= 8 L W_aux, the ceilings (Γ_4) and (Γ_5) below, and Ř_k >= 64 L. Let □ be a cube of side n s, s := L^λ η, n <= CM, λ >= 1, such that
- (S1) o >= λ on □ (scale relation), and
- (S2) □ contains a point x with d_sc(x, 𝖲) >= Ř_k/2 and x in G.

Then there is a gauge u on □ with U_2^u = e^{iηA} and s|A|, s^2|∇^η A| <= (φ_flat/64) B C M α_{0,λ}.

By Lemma P2, (S1) and (S2) hold for every cube of Q_𝔅(x), x ∈ W_c, 𝔅 ≼ B''_k, of family λ >= 1, and for every cube of the frozen family of a dissolving piece. These are all the cubes that consumers R and A route to the base bound (section 3.1). The cube clause they read is F w_□ B C M α_{0,λ} with F >= φ_flat and w_□ >= 1. So B2(c') gives 1/64 of it.

*Proof.* *The read set.* b102 H14.1 (`library/b102.md` 1840-1866) encloses □ in an aligned cube of side M''s, M'' <= n + 2W_aux, and adds auxiliary collars of total width at most W_aux s/(1 - L^{-1}) <= 2W_aux s. It reads U only on these and on stencils of one lattice step; the further collar carries the identity and is not read. So every read lies in Q^+ := {z : dist_∞(z, □) <= 5 W_aux s}. W_aux is fixed before the separation floors (b102 order of constants, lines 1924-1933), hence before M.

*Scale relation on Q^+.* By (S1), □ ⊂ Ω_λ(B''_k). The zone of level λ - 1 has dist_∞(Ω^c_{λ-1}, Ω_λ) >= M L^{λ-1} η ((I-G)(a); (G) at I:137089-137092, "each stratum is at least one M-cube of its own scale wide"). By (M'), 5 W_aux s = 5 W_aux L^λ η < M L^{λ-1} η. Hence Q^+ ⊂ Ω_{λ-1}: every read has level at least λ - 1.

*Distance on Q^+.* Q^+ has sup-diameter at most (2M + 10 W_aux) L^λ η <= 3 M L^λ η, as M >= 16 W_aux. Q^+ is a cube, inside Ω_{λ-1}. Join x to any point of Q^+ by four axis-parallel segments inside Q^+. Each segment has length at most 3ML^λη and crosses at most 3L + 1 M-cubes of level >= λ - 1 (side >= ML^{λ-1}η). So d_sc(x, z) <= 4(3L + 1) <= 16 L for z in Q^+, by the path reading of d_sc in (I-G). Hence d_sc(z, 𝖲) >= Ř_k/2 - 16 L >= Ř_k/4. The path from x stays at positive d_sc from 𝖲. The support of B_2 ends at the cut, and 𝖲 contains the band of D_2 next to the cut (section 2). So the path stays in G, and Q^+ ⊂ G.

*Regularity on Q^+ at scale λ.* Let p be a plaquette (or b a bond) read on Q^+, attached to the block y' of level j := o(y') >= λ - 1. B2(a) gives ρ(y') <= 2 B_3 c_R ε^D_j, so (T1) gives |dU_2(p) - 1| <= 2 B_3 c_R ε^D_j L^{-2j} and the divergence test at L^{-3j}. Compare with scale λ:
- if j = λ - 1: ε^D_{λ-1} <= c_R ε^D_λ by (I-R), so the bounds are at most 2 L^2 B_3 c_R^2 ε^D_λ L^{-2λ} and 2 L^3 B_3 c_R^2 ε^D_λ L^{-3λ};
- if j >= λ: ε^D_j <= c_R (j - λ)^{1/2} ε^D_λ by (I-R), and (j - λ)^{1/2} L^{-2(j-λ)} <= 1, so the bounds are at most 2 B_3 c_R^2 ε^D_λ L^{-2λ} and the same with L^{-3λ}.

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
- (ii) Every cube of Q_𝔅(x), x ∈ W_c, 𝔅 ≼ B''_k, and every cube of the frozen family of c, lies in X_c ⊂ K_0 and satisfies (S1), (S2) of B2(c').
- (iii) Every block of level <= 1 within 20Mη of Col(C) lies in Z_1 ⊂ Z_h ⊂ K_0. Every index-zero cube meeting Col(C) has at most 10M sites per side (I:142775-142777).

*Proof.* (i) X_c ⊂ Z_{k_c} ⊂ Z_h by (T2), (T4) (I:138393-138398). Z_h ⊂ D_2 and d_sc(Z_h, 𝖲) >= Ř_k - 1 >= Ř_k/2 (section 2). The cells of Z_h are in the support of B_2 and off 𝖲, so in G. Hence Z_h ⊂ K_0. (ii) is Lemma P2. (iii) is the first paragraph of the proof of B1 (gate section 4: ADVANCE). QED.

This replaces b-in.md Lemma P (i). The false step there was "a cube meeting W_c meets a block of K", with K of positive level (gate section 6). Lemma P2 does not use it. A cube of family λ >= 1 has no raw cell (Lemma F), and every required cube lies in X_c.

### 4.2 The base bound at raw cells (B2 extended to level 0)

Consumer R reads clauses at every x ∈ W_c, raw cells included (I:138367: "Let x ∈ W_c"). At a raw cell the entries 1, 3, 5, 6, 7 are read on the pinned plaquettes, the current and A' (I:142600-142605). The base pair there is the raw datum: U_2 reads V'' off Ω''^{~2}_{h+1} (I:138407-138411), and every bond of a pinned plaquette is a level-0 block, fixed by the constraint.

**Corollary B2(b0).** Under the hypotheses of B2(a) and (Γ_3), entries 1, 3, 5 of (U_2, J(U_2)) at every raw block y of K_0 are at most (φ_flat/64) r_a(0), and entries 6, 7 vanish.

*Proof.* B2(a) is stated for every block y of G of level n >= 0 with d_sc(y, 𝖲) >= Ř_k/4, so it holds at n = 0: ρ(y) <= 2 B_3 c_R ε^D_0. The proof of B2(b), with the gate's repaired current step (gate section 5, B2(b): η^3|J(U)(b)| <= c_π ρ(y) L^{-3n}, c_π <= 2, B_3 >= 12), uses only this bound and (T1) at level n. At n = 0 it gives |dU_2(p) - 1| <= 2 B_3 c_R δ_D(t_γ) α_{0,0} and η^3|J| <= 4 B_3 c_R δ_D(t_γ) α_{0,0}. (Γ_3) is stronger than 256 B_3 c_R δ_D(t_γ) <= φ_flat (gate section 5). U_2 is real, so A' = 0. QED.

At a raw cell, U_2 = V'' on the pinned plaquettes. So B2(b0) there is the statement that the raw datum obeys the level-0 tests at 1/64 of the level-0 radius. Its input is (I-D) at level 0 (the account's data clause (γ), I:137012-137036). If (I-D) fails at a raw cell of W_c, then clause (b) of `4.27:prf-room-dissolving` fails there for every choice of B_S that W_c avoids. B2(a) does not repair a datum. The account's own ambient-inclusion lemma lists the presented pair at raw points of the core as not asserted (I:136398-136405, I:136553-136556).

Cube clause at family 0: an index-0 cube □ ∋ x, x ∈ W_c, has side at most 2Mη and lies in X_c (Lemma P2). Every plaquette in it is attached to a block of level j >= 0 in K_0, so |dU_2(p) - 1| <= 2 B_3 c_R ε^D_j L^{-2j} <= 2 B_3 c_R^2 ε^D_0 =: ε. The level-zero axial gauge (b102 H14.1, last paragraph, `library/b102.md` 1867-1869; the same bound is input (f) of `4.27:lem-real-point-collar`, I:142639-142646) gives η|A|, η^2|∇A| <= 50(d-1) M ε when 2(d-1)(2M)ε <= 1/10. The ceiling

  (Γ_0)  64 · 50 (d-1) M · 2 B_3 c_R^2 δ_D(t_γ) <= φ_flat B C M,  and  12 M · 2 B_3 c_R^2 δ_D(t_γ) sup α_0 <= 1/10,

gives 1/64 of the family-0 cube threshold BCMα_{0,0}. (Γ_0) has degree p_0 + 2r - q < 0, fixed last.

### 4.3 B_S: the account's descriptions, the choice made here, and every use

The account names B_S in three ways and fixes it nowhere:
- "the subset of S fixed by that construction which the pieces considered avoid" (I:138361-138363), S := ∂(Ω''_{h+1})^~;
- "the set near S that the base bound on the core excludes" (I:136725-136726);
- "the part of S avoided by the core D_2 \ B_S on which the pair is read", where "S denotes the region inside which the two layers forming D_2 below are placed" (I:142294-142297).

The construction is the supplier, so the choice is made here: **B_S := D_2 \ K_0.** It is the band of D_2 at d_sc < Ř_k/2 from the source band 𝖲, which sits next to the cut S. It is "near S" and inside the region holding D_2, as the second and third descriptions say. It is not a subset of the surface ∂(Ω''_{h+1})^~, as a literal reading of the first would ask. Under that literal reading the core D_2 \ B_S would contain the cells of D_2 inside 𝖲. These cells include the graded layer, where B_2 carries the cut datum of B_h, and cells a few reset steps from it. (I-A) admits that datum only at radius a_1, and Theorem G then bounds U_2 there only by about a_1, not by 1/64 of φ_flat r_a(o). No consumer reads a cell of D_2 \ K_0 for the base bound, as the table shows.

| Use of B_S in the account | What it asks | Status with B_S := D_2 \ K_0 |
|---|---|---|
| R, Place, I:138402-138404 | W_c "two layers of cubes of side LMR_{h+1} inside S" and "off B_S" | W_c ⊂ Z_h, two layers inside the cut (D_2 = (Z'_h)^{~2}); W_c ⊂ K_0 (P' (i)). Holds. |
| R (b), I:138383-138385, I:138438-138448 | base bound on cells of D_2 \ B_S, read at x ∈ W_c; cube clause with the base gauges | B2(b), B2(b0) on K_0; B2(c') and the family-0 gauge on the cubes of Q(x) (P' (ii)); entries 2, 4 by B2(d) under (Ref). Holds as an implication. |
| A core, I:136724-136745 | core "holds every piece dissolved at 𝔒"; 1/64 + 3/64 there | P' (i); base as above; increments by Sh' (section 5), one-sided for entries 2, 4. |
| A frozen cubes, I:136752-136756; interface (iv), I:139967-139971 | frozen-family cubes "whole in D_2 \ B_S", given the core's gauge | P' (ii) and B2(c'). Holds. |
| Collar displacement (f), I:142294-142313, I:142583-142586 | core contains the collar; base (U_2, J(U_2)) and layers H_3, H_4 there | Col(C) ⊂ Z_h ⊂ K_0 (P' (iii)). The base and layers on D_2 are the layer construction (section 5.1). |
| Current localisation (b), I:92444-92445 | deep-current identity on stencils meeting D_2 ∪ B_S | B_S ⊂ D_2, so the hypothesis reads on D_2 only. This weakens what is asked; no conclusion changes. |
| A's decomposition, I:139940-139979 | every re-presented cell lies in 𝖹, the core, or the list of the layer bound | **Open, and the account's own (∗) at I:139976-139979.** A cell of B_S is in D_2 ⊂ Z''_{h+1} ⊂ Z. That it lies in 𝖹 or in that list is not shown here. |

So the corrected sets are identified with every set the consumers name. The one remaining obligation is A's coverage of B_S. The account itself marks that step (∗) (I:139976-139979: "that Y' \ 𝖹 is exhausted by the list of the layer bound ... [is] not proved here"). Choosing B_S does not discharge it (gate section 10, item 6).

## 5. BLOCK 3: the layer kernels and Proposition Sh

The gate's blocking step (gate section 7) is the passage from the tuple bound at each layer's kernel (ca-f Proposition R) to the size N_{U_partial}(H_s) with the covariant derivative at the preceding partial product, which Lemma A_n reads. Two things close it: the kernel identity (K-id), read from the account's layer construction, and a comparison lemma (Lemma K) for the case the identity does not cover.

### 5.1 (K-id): the kernel of each layer is the configuration it multiplies

**(K-id).** At the completion site, on D_2, in the presentation gauge:
- (i) the pair at 𝔟_2 is (U_2, J_2), J_2 = 𝒥(U_2);
- (ii) for s ∈ {3, 4}, H_s is the response field of the layer theorem at the kernel (W_s, σ_s), where W_s is the pair at stage s: W_3 = U_2 and W_4 = e^{iηH_3} U_2;
- (iii) the presented chain at (t_3, t_4) is e^{iηt_4H_4} e^{iηt_3H_3} U_2 with current J_2 + Σ_s s^♯_{σ_s}[t_s H_s]; the consumers read b_2, b_3, b_4 and the two segments b_2b_3 (t_4 = 0) and b_3b_4 (t_3 = 1) (I:142334-142338, I:142563-142570).

*Where the account states it.* Each item below is part of the layer construction (Balaban's CMP 122b (1.50)-(1.55) as the account reads it). None is a conclusion of the arrest theorem.
- (i): "U_{1,2} = U_2" on D_2, CMP 122b (1.53), quoted at I:92022-92024; hypothesis (c) of `4.22:lem-current-localisation` (index PROVED), I:92446-92447.
- (ii): in the key containment theorem "(W_s, J_s) is the pair at stage s" (I:73071). Its proof is an induction in which stage s derives "(1) the layer theorem ... (3) the entries at 𝔟_s; (4) the induction hypothesis at stage s+1" from the pair at stage s (I:73123-73136). So the layer theorem at stage s is applied at the stage-s pair, and the pair at 𝔟_s is the next stage's pair. At the completion site: "Apply Lemma 4.27:lem-left-factor-algebra layer by layer, with 𝔥 = H_s and with 𝐔 replaced by W_s, the pair obtained after the layers preceding s. The size N_y(H_s) is taken with the covariant derivative ∇_{W_s}" (I:142473-142478). The substitution chain: each row "starts from a critical point P_0 ... (a) P_1 = e^{iη𝐇}P_0", the rows taken "in the order in which the corresponding substitutions are made in [CMP 122b]" (III:9174-9186), namely (1.63), (1.58)/(1.64), (1.57), (1.54), (1.51) (III:10186-10190). The layer s = 3 is (1.54) and s = 4 is (1.51) (I:73107-73111). So the H_4 row comes after the H_3 row and starts from its output. Balaban on (1.54): H''_k is a function of "the fields J_{1,2}", the current of U_{1,2} (quoted at I:92377-92384), so H_3 is built at U_2.
- (iii) and the single gauge: the chain display (I:142563-142570); "The rotation of the presentation is trivial on D_2" (I:142313-142314), supplied "by the layer construction" (I:142303); "The gauge frame is carried unchanged" (III:9192-9193).

*Reading, not rebuilt.* CMP 122b is not in `~/ym4d-papers`, so (K-id) is the account's description of Balaban's construction, read at five places that agree. Hypothesis (f) of the collar-displacement lemma attributes the base-and-layers fact on the core to "the arrest theorem together with the layer construction" (I:142302-142303). (K-id) uses only the layer-construction half, on D_2. The arrest-theorem half is the core D_2 \ B_S, which section 4 now supplies. So (K-id) does not import the arrest theorem (gate section 9).

*Compatibility with the cancellation datum.* ca-f Proposition R bounds E_{y'}(H_s) by (N1)(b) at whatever kernel the layer is built ("at any determining set", "for every kernel (W, σ) of the theorem's class"). The datum of H_3 is (f_1, arg_{3,2}) with f_1 = G''(σ)J^{𝔟_2} (ca-f (N4)), built from the current of the pair at 𝔟_2, which is W_3's pair. The datum of H_4 is g_k B, supported in 𝖲, and does not involve the kernel. So Proposition R's bounds hold at W_3 = U_2 and W_4 = e^{iηH_3}U_2, given (N7) (p(W_s) <= 1) at these kernels.

### 5.2 Lemma K (changing the connection by a left factor)

Write (∇_{W,μ} h)(x) := η^{-1}(Ad(W(x, x+ηe_μ)) h(x+ηe_μ) - h(x)); the proof is the same for the transport in the other direction. For a block y of level n put l := L^n η and N^W_y(h) := sup max{l|h|, l^2|∇_W h|} over the bonds read at y.

**Lemma K.** Let W = e^{iηA'}U on the bonds read at y, with U G-valued and η|A'| <= 1/80. Let X be a g^c-valued 1-form there with sup l|X| <= 1/100, and W' := e^{iηX}W bondwise. Then for every g^c-valued 1-form h,

  l^2 sup |(∇_{W'} - ∇_W) h| <= 2.1 (sup l|X|)(sup l|h|),   N^{W'}_y(h) <= (1 + 2.1 sup l|X|) N^W_y(h).

*Proof.* On a bond b, Ad(W'(b)) - Ad(W(b)) = (Ad(e^{iηX(b)}) - 1) Ad(e^{iηA'(b)}) Ad(U(b)). Ad(U) is an isometry for the operator norm. ‖e^{ad Z} - 1‖ <= e^{2|Z|} - 1 <= 2|Z| e^{2|Z|} and ‖e^{ad Z}‖ <= e^{2|Z|}. So l^2|(∇_{W'} - ∇_W)h(b)| <= l^2 η^{-1} · 2η|X(b)| e^{2η|X(b)|} e^{2η|A'(b)|} |h| <= 2 e^{0.02 + 0.025} (l|X|)(l|h|) <= 2.1 (l|X|)(l|h|), as η|X| <= l|X| <= 1/100. The second bound follows, since l|h| <= N^W_y(h). QED.

*Use.* Under (K-id), on the segment b_2b_3 the left factor e^{iηt_3H_3} acts on U_2 = W_3. On b_3b_4 the left factor e^{iηt_4H_4} acts on e^{iηH_3}U_2 = W_4. So N^{U_partial}_y(t_s H_s) = t_s N^{W_s}_y(H_s): Lemma K is not needed on the consumers' segments. It covers two other cases. (a) If W_4 = U_2 (the alternative the gate names), then U_partial = e^{iηt_3H_3}U_2 on the square, with X = t_3 H_3. (b) Inside the square (t_3 < 1, t_4 > 0) under (K-id), U_partial = e^{iη(t_3-1)H_3}W_4, with X = (t_3 - 1)H_3, |t_3 - 1| <= 1. In both cases N^{U_partial}(t_4H_4) <= (1 + 2.1F) N^{W_4}(H_4) <= 1.02 N^{W_4}(H_4) when l|H_3| <= F <= 1/200. This is the gate's conditional repair (gate section 7), proved.

### 5.3 Proposition Sh' (repaired)

**Proposition Sh'.** Assume (K-id); ca-f's (N1)-(N8), with (N7) read at the kernels W_3, W_4 at the blocks read from K_0, and (G-sep) extended to every block of K_0 (for z in K_0 and x in T, d_sc(z, x) >= d_sc(z, 𝖲) - 1); B2, B2(b0); Lemma E'; input 1(e) (I:131580-131586) with its premises below; α_0 <= 1/10 on [t_γ, ∞); and the ceiling (Γ_Sh') below. Then at every block y of K_0, of level n >= 0, at every point of the segments b_2b_3 and b_3b_4:
- (a) entries 1, 3, 5, 6, 7 differ from their values at b_2 by at most (3/64) φ_flat r_a(n);
- (b) entries 2 and 4 obey Q_e(chain)(y) <= Q_e(𝔟_2)(y) + (3/64) φ_flat r_e(n), e ∈ {2, 4} (one-sided);
- (c) the G-part, hence every cube gauge, is that of U_2.
By the radius ratio r_a(μ)/r_a(m) >= (1+β_0)^{-2} g^{-1/2} L^{e_a g} >= 1 for μ < m (I:131441-131446), the same bounds hold with r_a(n) replaced by r_a(n') for every finer birth index n' <= n. They hold a fortiori at every threshold F w c r_a with F >= φ_flat and w, c >= 1.

*Proof.* *Step 1, layer sizes.* Take δ_R <= w δ/2, so p_T = e^{-δ_R d_sc(., T)} lies in M^∧_{δ/2} (ca-f Step 1 with δ/2; gate section 7: "Taking δ_R <= wδ/2 is valid"). Proposition R (ca-f Step 3) gives E_{y'}(H_s) <= (C_D/K_u) ε_Q(k) p_T(y') at every block y', in its unit l_{y'}, at the kernel W_s. The left-factor lemma at y reads h on Δ~(y) and one step further (I:141270-141278). The blocks y' met have d_sc(y, y') <= 2 and level n - 1, n or n + 1 (Lemma C (C0)). Passing to l = L^nη costs at most L for |h| and L^2 for |∇h|. Hence

  N^{W_s}_y(H_s) <= μ(y) := L^2 e^{2δ_R} (C_D/K_u) ε_Q(k) p_T(y).

μ is a constant multiple of p_T, so μ ∈ M^∧_{δ/2}. By (G-sep) and Lemma E' (valid at n >= 0), d_sc(y, T) >= (1/2)[Ř_k/2 + (L-2)(h - n - 1)^+] - 1. By (N8) and (I-R), ε_Q(k) <= K_Q A^+ ρ_C max_i α_{i,k} and α_{i,k} <= c_R (k - n)^{1/2} α_{i,n}, with k - n = Ř_k + h - n. Hence

  μ(y) <= C_S (Ř_k^{1/2} + S_2) e^{-δ_R Ř_k/4} α_{*,n},  C_S := L^2 e^{3δ_R} (C_D/K_u) K_Q A^+ ρ_C^2 c_R,  S_2 := sup_{m>=0} m^{1/2} e^{-δ_R(L-2)(m-1)^+/2},

using (a + b)^{1/2} <= a^{1/2} + b^{1/2}. Put F(y) := μ(y). (Γ_Sh') gives F(y) <= α_{*,n}/200 <= 1/2000.

*Step 2, the kernel.* By (K-id) and Step 1, N^{U_partial}_y(t_s H_s) = t_s N^{W_s}_y(H_s) <= F(y) on both segments, since N is homogeneous of degree one in h.

*Step 3, entries 6 and 7.* On b_2b_3 the base has A' = 0, so A'(t_3) = t_3 H_3 exactly, and ∇_U = ∇_{U_2} = ∇_{W_3}. So l|A'| and l^2|∇_U A'| are at most F. On b_3b_4, Lemma A_n (ii_n), (iii_n) apply with base W_4, h = t_4 H_4, N <= F < 1/40 and a = sup l|H_3| <= F < 1/80. They move these entries by at most 1.06 F. In total, l|A'| <= 2.06 F and l^2|∇_U A'| <= 2.06 F, against α_{1,n} l^{-1} and α_{1,n} l^{-2}.

*Step 4, entries 1 and 5.* Entry 5 is the G-part; it does not move. Entry 1 on b_2b_3: Lemma A_n (i_n) with base U_2, θ <= (φ_flat/64) α_{0,n} L^{-2n} by B2(b), (b0). So 5.6 θ L^n <= 0.01 and the move is at most 2.91 L^{-2n} F. On b_3b_4 the base is W_4, and the first layer has moved its plaquettes by at most 2.91 L^{-2n} F. So θ_4 <= L^{-2n}[(φ_flat/64) α_{0,n} + 3F] (gate section 7, entries 1 and 5). Then 5.6 θ_4 L^n <= 5.6 (1/640 + 3/2000) < 0.02, and the move is at most 2.92 L^{-2n} F. In total at most 6 L^{-2n} F, against r_1(n) = α_{0,n} L^{-2n}.

*Step 5, entry 3.* Lemma S of ca-f at the kernel W_s, in the local unit l (gate section 7, row "Current": ADVANCE at the kernel of each layer, given (N6), (N7), the smallness bound and the segment-current identification). It gives l^3|s^♯_{σ_s}[t_s H_s](b)| <= t_s Kcur E_y(H_s) <= Kcur F. So η^3|𝒥| moves by at most 2 Kcur L^{-3n} F in total, against η^3 r_3(n) = α_{0,n} L^{-3n}.

*Step 6, entries 2 and 4.* Input 1(e) needs: a majorant in M^∧_{δ/2} of the layer's size, which μ is (Steps 1-2); admissible triples, which are those of the readings (Σ^♭), (Σ^*) at y; and the smallness C^b(a_♭ + κ_max) <= 1. Here κ_max = sup μ <= γ̄_0 by the second part of (Γ_Sh'). And a_♭ <= γ̄_0, because the direct entries of the chain stay below their radii α_{·,n} <= γ_0^{(k)} <= γ̄_0 (Steps 3-5; γ_0^{(k)} = 5 max_{j<=k} w_*(j) ᾱ_j, I:136509-136510, I:109946). The condition with both quantities at γ̄_0 is the ceiling (c4) of the arrest hypotheses, (Ce7) at I:131850-131862, and it persists when they decrease, as the account reads it at I:137279-137290. *Reading:* 1(e) is applied with N_· <= μ on the blocks read at x. Its constant K^b_S carries c_B = e^{2δL(ϱ_0+2L)}, the cost of a fixed neighbourhood (I:131585-131586), so its bound at x reads the layer only near x, where Steps 1-2 hold. Using that separately stated hypothesis on constants is not using the arrest theorem (gate section 9). The level in 1(e) is that of the point in its space: in the bracket of CMP 122a (1.65) the bound sits at the shell level m of the point, and p ranges over the triples (I:148158-148169). Here that level is n. So each layer gives Q_e^+ <= Q_e(1 + π_×) + π r_{e,n} with π_× <= π := K^b_S μ(y)/α~_{0,n} <= K^b_S F/(c~ α_{0,n}). Start from Q_e(𝔟_2) <= (φ_flat/64) r_{e,n} (B2(d) under (Ref)). While Q_e <= r_{e,n} each layer adds at most 2π r_{e,n}. Under (Γ_Sh'), 4π <= 3/64, so Q_e stays below r_{e,n} and the total increase is at most 4π r_{e,n}. This is an upper bound only, as the gate notes.

*Step 7, the ceiling.* With c_sh := max{2.06, 6, 2 Kcur, 4 K^b_S/c~} and γ_0-smallness folded in:

  (Γ_Sh')  sup_{R >= R_γ} c_sh C_S (R^{1/2} + S_2) e^{-δ_R R/4} <= min{(3/64) φ_flat, 1/200},  and  C_S (R^{1/2} + S_2) e^{-δ_R R/4} sup α_* <= γ̄_0 on the same range.

R_γ := inf_k Ř_k tends to infinity as γ tends to 0 (I:77940-77942). So (Γ_Sh') is a ceiling of degree minus infinity, fixed last. Steps 3-6 bound each move by c_sh F/α_{*,n} times the threshold at weight one. (Γ_Sh') makes this at most (3/64) φ_flat. Part (c) is `4.27:lem-left-factor-algebra`: a left factor keeps U and its gauges. QED.

*What changed from b-in.md Proposition Sh.* The norm passage at b-in.md lines 211-216 is replaced by Step 2, through (K-id). The second-layer curvature uses θ_4 (Step 4). Entries 2 and 4 are one-sided, with all premises of 1(e) listed (Step 6). The result holds on all of K_0, raw blocks included (Lemma E' and Lemma A_n hold at n = 0). The constants are those of the gate's repair, with F <= α_{*,n}/200 in place of 1/100 so that Step 4 closes at n = 0.

### 5.4 The account's three shares (REVISE of b-in.md line 226)

Consumer R (c) asks the increments to total at most 3θ/64 (I:138383-138387), and (d) adds 1/64. Consumer A adds the same (I:136726-136732). Sh' gives this total, with entries 2 and 4 one-sided, which is the direction spend reads. The account also names three separate shares (bend, source, map 𝐇'), a bend floor, an ownership floor, floors at a set Γ_♭ (I:138454-138464), and a use "at halved far factors" for the dissolved pieces at the t-disc of site (L) (II:1208-1212). These are not reconstructed. A total bound does not identify them. If "halved far factors" means the decay rate δ_R halved, then (Γ_Sh') with δ_R/2 in place of δ_R gives the same total; that reading is not checked here.

## 6. The gate's REVISE items, as applied here

b-in.md is not edited (row 399). Each REVISE of gates/b-in-gate.md is applied in this note as follows.

| Gate item | Applied here |
|---|---|
| §2 (LR): read-complete patches, B_3 >= 12, boundary inequality at vertices without a patch; Theorem G's cut term with the artificial datum retained | Section 2, kept as the form of (LR) and Theorem G that B2(a) uses. |
| §2 "ρ(y) = t(y)" on pinned blocks false for full (T1) | Replaced by the gate's stencil repair; used in B2(b0) (section 4.2). |
| §3 core definition; 𝖲 vs S | K_0, K_+, B_S as the gate defines them; 𝖲 and S kept apart (section 2). B_S identified with every consumer use (section 4.3). |
| §3 (I-D) attribution | (I-D) is required on the full test set, mixed-level transports included; it is an input, not the account's (γ) alone (section 2). |
| §3 Lemma C (C2): the last edge reaches the cut, and the cut region reached is the source band | Part of (I-G), as a geometric input (section 2). |
| §3 Lemma C: enlarged reset neighbourhoods need their step bound rechecked | Rechecked with reach R_* = 4R_1M_1 + 2W_aux + 1; floor (M*) replaces (M) (section 2). |
| §4 ceiling terminology | Section 2: degrees p_0 - q, p_0 + 2r - q, minus infinity; ceilings on γ, not caps. |
| §5 B2(b) current step | The gate's formula η^3 J(U) = π Im(η D^{η*}_U ∂U), c_π <= 2, used in B2(b0). |
| §5 B2 hypothesis list | (Γ_4) and the gauge smallness (Γ_5) are hypotheses of B2(c') (section 3.4). |
| §5 B2(c) BLOCK | Closed as an implication: Lemma F, Corollary F', Lemma P2, Corollary B2(c') (section 3). |
| §6 Lemma P BLOCK | Closed: Lemma P' (section 4.1); raw cells in K_0, base bound there by B2(b0) (section 4.2). |
| §7 Sh BLOCK; entries 1 and 5 at the second layer; derived entries; line 226 | Closed through (K-id) and Lemma K (sections 5.1-5.2); Proposition Sh' with θ_4, one-sided entries 2 and 4 with all premises of 1(e) (section 5.3); the share package stays unreconstructed (section 5.4). |
| §8 absence claim | Wording: "no independent, noncircular supplier located in the four supplied sources" (section 1). |
| §9 final claims, "new mathematics", "kind" | Result below: conditional conclusions only. Theorem G's local-profile idea has the outline predecessor SA 9678-9691 (Theorem 2, sketched); no priority is claimed. |

## 7. Tries to kill, and what survived

No numerical run. Each try is a hand argument.
- *A family cube whose scale exceeds its old level.* CMP 122a (1.67) cubes have scale j but sit in old shells Ω_m, m <= j. Lemma F case 3 shows the stage level there is j. Survives.
- *A cube that leaves its class component, or meets an older nested piece.* Lemma F, last two paragraphs: such points lie in Ω_k at level k, or in X_a where levels are frozen and case 3 cannot reach. Survives.
- *A frozen cube reaching outside X_c, into a finer region.* Lemma P2 (ii): the collar of width 2MR_{k_c} units of level k_c stops it. Survives, under the unit reading stated there.
- *The enlarged H14.1 region reaching finer zones.* Excluded by (M') M >= 8 L W_aux, which keeps every read within one level of the cube's scale. Some floor of this form is needed. The zones below level λ can have widths M L^{λ-1}η, M L^{λ-2}η, ..., which sum to less than 2 M L^{λ-1} η. If M < 2.5 L W_aux, a nest of minimal widths lets the read set (reach 5 W_aux L^λ η) touch every finer level j. There (T1) gives only L^{2(λ-j)} times the scale-λ bound, which is unbounded.
- *Raw cells of W_c.* The base pair there is the raw datum. Clause (b) at such a cell is exactly (I-D) at level 0, for every choice of B_S that W_c avoids (section 4.2). This is where the account's clause (b) can fail first, if the data clause fails at raw cells.
- *Finer birth indices for entries 2 and 4.* The radius ratio gives r_e(n') >= r_e(n) for n' < n. The level in 1(e) is the point's level in its space (reading of the CMP 122a (1.65) bracket, I:148158-148169). If 1(e)'s level were a predecessor level m < n, Step 6 would lose (n - m)^{1/2}, which no distance in the current structure pays. So that reading is load-bearing.
- *The second layer at level 0.* With F <= α_{*,n}/100 the Lemma A_n constant at n = 0 exceeds 3. F <= α_{*,n}/200 restores it (Step 4).

## 8. Named inputs and open items

**New inputs of this note.**
- (Q-pt): a cube of Q_𝔅(x) contains x. A weaker form suffices: each cube routed to the base bound contains a point of W_c.
- (K-id): the kernels W_3 = U_2, W_4 = e^{iηH_3}U_2 on D_2, in one gauge (section 5.1), read from the layer construction at five places.
- Floors (M*): M >= max{16 L s_0, 8 L^2} R_* with R_* = 4R_1M_1 + 2W_aux + 1 (section 2), and (M'): M >= 8 L W_aux. Ceilings, all fixed last: Ř_k >= 64 L, (Γ_4), (Γ_5), (Γ_0), (Γ_Sh'), sup_{t >= t_γ} α_0(t) <= 1/10.

**Inputs kept from b-in.md**, with the gate's repairs: (LR) read-complete; (I-A); (I-D) on the full test set, level 0 included; (I-G) with the path-metric reading; (I-N0), (I-R), (I-T), (I-K); (Q); (Ref); ca-f's (N1)-(N8), (N7) read at W_3 and W_4, (G-sep) extended to K_0; input 1(e) with its premises, including (c4)/(Ce7) of the arrest hypotheses.

**Open, ranked by what each breaks.**
1. **Coverage of B_S in consumer A.** That each re-presented cell of B_S = D_2 \ K_0 lies in the keystone region 𝖹 = Λ^♮ ∪ 𝔑^rec (I:131710) or in the list of the layer bound. The account marks this step (∗) at I:139976-139979. It belongs to `4.27:prf-ambient-inclusion` (registry O-ambient). Not attacked (rule 0a): it is consumer A's step, not the sealing construction's.
2. **(I-D) at raw cells of W_c, and (I-A).** Clause (b) at a raw cell is (I-D) at level 0 (section 4.2). (I-A) still needs the actual nest, mixed-level tests, minimal orbit and reset patches (gate section 10, item 1).
3. **(K-id) and (Q-pt) are readings.** CMP 122b and CMP 122a are not in `~/ym4d-papers`. If W_4 = U_2 instead, Lemma K gives Sh' with c_sh enlarged by 1.02. If W_4 is some other configuration, Sh' needs a new comparison.
4. ca-f's (N1)-(N3) (owners stage-claude and B99b-T314), (N7) at W_4, (Ref) and 1(e).
5. SU(N), N >= 3: (LR) is checked for SU(2) only (b102).
6. The account's three named shares, its floors at Γ_♭, and the use at halved far factors (II:1208-1212): not reconstructed (section 5.4).

## Result

**Kind (How we work, item 9).** Proof of steps the account assumes: the sealing construction that `4.27:prf-room-dissolving` (b), (c) and the core step of `4.27:prf-ambient-inclusion` invoke and that no supplied source states. This note repairs the three BLOCKs of gates/b-in-gate.md. Proved by Claude, not yet checked by the other model.

1. **BLOCK 1, B2(c), closed as an implication.** Lemma F: a cube of family λ lies where the level is at least λ, for every family of B_k, of the stage structures (CMP 122a (1.65), (1.67), (1.69) as quoted) and of the frozen structures. Levels never fall in time (Corollary F'). Every cube that consumers R and A route to the base bound lies in X_c ⊂ Z_h ⊂ K_0 (Lemma P2). Corollary B2(c'): on each such cube of family λ >= 1, U_2 has a gauge at 1/64 of φ_flat BCMα_{0,λ}. The proof bounds the whole H14.1 read set: it lies in the zone of level >= λ - 1 by the floor (M'), within d_sc 16L of the cube, so in G at d_sc >= Ř_k/4 from 𝖲. The family-0 case is the level-zero axial gauge.
2. **BLOCK 2, Lemma P, closed with one consumer obligation left.** W_c ⊂ K_0, positive-level cells in K_+, raw cells allowed. The base bound holds at raw cells too (B2(b0)), where it is exactly (I-D) at level 0. B_S := D_2 \ K_0 meets every use of B_S in the account (table, section 4.3). The exception is consumer A's coverage of B_S by the keystone region, which the account itself marks (∗) at I:139976-139979.
3. **BLOCK 3, Proposition Sh, closed as an implication from (K-id).** The account's layer construction builds each layer at the configuration it multiplies: W_3 = U_2, W_4 = e^{iηH_3}U_2, in one gauge on D_2. So on the consumers' segments the tuple bound at the kernel is the size Lemma A_n reads. Lemma K covers the full square and the alternative W_4 = U_2 (factor at most 1.02). Proposition Sh' then gives, at every block of K_0 of every level: entries 1, 3, 5, 6, 7 move by at most 3/64 of φ_flat r_a; entries 2 and 4 rise by at most that much; the G-part and cube gauges stay those of U_2. The gate's corrections are included: θ_4 at the second layer, one-sided 1(e) with all its premises, F <= α_{*,n}/200.

So clauses (b) and (c) of `4.27:prf-room-dissolving` get their inputs as implications, uniformly in the age, the cutoff, the history and the numbers of exclusions, blocks and strata. So does the core step of `4.27:prf-ambient-inclusion`, except its coverage of B_S. Neither those lemmas nor the arrest theorem's conclusions supply any step. The arrest hypotheses (c4)/(Ce7) on constants are used.

**Not shown.** Section 8, items 1-6. No counterexample to any of the account's statements was found. Clause (b) can fail first at raw cells of W_c, if (I-D) fails there.

**What changes for consumers.** No consumer statement changes. For the CA-BIN node the three BLOCKs of gates/b-in-gate.md are closed as implications, once checked; its named inputs become (I-A), (I-D), (LR), (K-id), (Q-pt), (Ref), 1(e) and ca-f's (N1)-(N3). O-ambient's (∗) now carries the coverage of the explicit band B_S = D_2 \ K_0. The tree and registry are not edited here (row 399); the lead updates them after a check.

**Suggested next step, for the lead.** One line-by-line check by Codex of sections 3-5, with attention to Lemma F case 3 and its nested-piece paragraph, Lemma P2 (ii) and its unit reading, the read set of B2(c'), and the five sources of (K-id). Nothing is posted.

**Provenance.** Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker 1, 2026-11-06, pinned at 99d2c3b3f. Account files fetched by URL into a scratch folder of this lane; SHA-256 as in `library/arr.md`. No Balaban page was read in this round; Balaban's statements are used as the account quotes them, and b102's as rebuilt in `library/b102.md`. No computer-assisted step; no numerical run.
