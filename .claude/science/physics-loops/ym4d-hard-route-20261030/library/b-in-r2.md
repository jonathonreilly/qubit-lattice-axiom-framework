lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T09:40Z

# b-in-r2: the three BLOCKs of gates/b-in-gate.md for library/b-in.md

FINISH row 399. Pinned at 99d2c3b3f. Work in progress; sections are added as they are written.

Started 2026-11-06T21:40Z on the Mac mini, worker 1. Proved by Claude, not yet checked by the other model, unless a line says otherwise.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (complete account CA-I, CA-II, CA-III and outline at upstream `31a47c543775`), for every statement, construction and bound cited with a line number. Tadeusz Balaban for the multiscale construction (CMP 89-122). Earlier work here: `library/b-in.md` (Claude, row 389), its check `gates/b-in-gate.md` (Codex gpt-6-astra xhigh, row 397), `library/ca-claude.md`, `library/ca-f.md`, `library/b102.md`.

## 1. Scope, duplicate check, sources

- **Item.** FINISH row 399. Moves: CA-BIN (`library/t0-tree.md` node CA-BIN, registry row CA-BIN, owner `b-in`), the input (B-in) of CA = clause (b) of `4.27:prf-room-dissolving` (CA-I 138348, unmarked) and the core step of `4.27:prf-ambient-inclusion` (CA-I 136490, marked incomplete). If the three BLOCKs close, CA-BIN becomes an implication from named Balaban-instance inputs; if one fails, the sealing package has a stated counterexample or a three-way-failed lemma.
- **Duplicate check (rule 0a).** `grep` of `library/open-core.md` and `library/l17c.md` for b-in, sealing, own-level, B_S, enlarged collar, Proposition Sh, partial product: no match. `library/open-registry.md` line 958: CA-BIN, owner `b-in` (this lane's lineage). FINISH rows naming the sealing package: 382, 383, 387 (digests), 389 (b-in), 397 (its check), 399 (this row). Row 404 (`fc-r2`) is the frame change of `library/fc.md`, a different object. No other row attacks these three BLOCKs. ca-f's (N1)-(N3) belong to other owners (stage-claude, B99b-T314) and are not attacked here.
- **Account label and status.** As in `library/b-in.md` section 1: clause (b) of `4.27:prf-room-dissolving` (CA-I 138348-138483, not marked incomplete) invokes the own-level bound of "the sealing construction" (CA-I 138438-138450); the construction is not stated in CA-I/II/III or the outline (gates/b-in-gate.md section 8, narrowed wording: no independent noncircular supplier located).
- **Sources.** CA-I, CA-II, CA-III and the outline fetched by URL into a scratch folder of this lane; SHA-256 agree with `library/arr.md` (outline d7f77d4d..., CA-I 4cb5cb5e..., CA-II 6a1f74b0..., CA-III 7e36523b...). Line numbers I:, II:, III:, SA: are of those raw files.
- **Rules.** No numerical run. No computer-assisted step.

## 2. Conventions kept from b-in.md, with the gate's renaming

- **Sets (gate section 3).** 𝖲 is the source band of the current localisation: the (2M_1+3 blocks)-neighbourhood of Ω''^{~2}_{h+1} in Λ (I:92468-92469). S := ∂(Ω''_{h+1})^~ is the cut of the room lemma (I:138358). They are different sets. b-in.md wrote S for 𝖲; here 𝖲 is written. G := (support of B_2) \ 𝖲, as in b-in.md section 3. o(y) := ℓ_{B''_k}(y), the level of y in B''_k read with precedence (I:132977-132985; I:136637-136640).
- **Geometry, from the law-site proof (I:91991-92031).** D_2 = (Z'_h)^{~2} ∩ Λ is Z'_h ⊇ Z_h with two layers of LMR_{h+1}-cubes of level h round it; the cut is its outer boundary; (Ω''_{h+1})^{~2} = ((Z'_h)^~)^c (Balaban, CMP 122a p. 195, as quoted at I:92010-92013). So 𝖲 contains the outer layer of D_2 and 2M_1+3 blocks of the inner one, and one full layer separates Z_h from 𝖲: d_sc(Z_h, 𝖲) >= Ř_k - 1 ((β) at I:92094-92096). Here Ř_k = k - h (I:77938-77954).
- **Corrected core (gate section 3).** K_0 := {cells y of D_2 ∩ G : d_sc(y, 𝖲) >= Ř_k/2}, K_+ := {y in K_0 : o(y) >= 1}, B_S := D_2 \ K_0.
- **Inputs kept as named in b-in.md**, with the gate's repairs: (LR) read-complete (gate section 2: every stencil, averaging and gauge read of a reset patch in N(y); B_3 >= 12; a separate boundary inequality at vertices without a patch); (I-A); (I-D) on the full test set, mixed-level transports included (gate section 3); (I-G) including the reading of d_sc as a path metric that counts M-cubes of the local scale (I:91727); (I-N0), (I-R), (I-T), (I-K); floor (M). Theorem G, Lemmas I, C, J, BCH, A_n, E' and Corollary B1 are used as the gate passed them (gate sections 2-7). B2(a) is used as the gate passed it: "ADVANCE as a conditional estimate".
- **Ceilings (gate section 4).** (Γ_1) has degree p_0 - q < 0 in t_γ; (Γ_3), (Γ_4) have degree p_0 + 2r - q < 0; (Γ_2), (Γ_5), (Γ_Sh) have degree minus infinity. All are upper bounds on γ, fixed last. None is a cap in the sense of I:1246-1253.

## 3. BLOCK 1: B2(c) on the actual cube families

### 3.1 The cubes the consumers route to the base bound

- **Consumer R** (`4.27:prf-room-dissolving` (b), I:138446-138448): "On cubes, the cube clause of the same own-level bound is met with the gauges of its first clause". The clause is that of a term τ read at x in W_c. Its cubes are those of Q(x), at the family's weight (I:132543-132544; I:122284-122286).
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

Cases 2-4 use the closed form, which holds on the running class component X (I:133454-133460). A cube condition reads only □ ∩ X (I:148147-148148, "a gauge transformation u defined on □ ∩ X"), so only cubes meeting X matter. Let y ∈ □ \ X. The segment in □ from a point of □ ∩ X to y leaves X. Its first point outside X lies in Λ_k: X is a component of Z ⊂ Z_k = Λ^c_k (I:131963-131965), and a cell adjacent to X outside it is not in Λ^c_k. That point is within sup-distance 2ML^kη of y, since □ has side C L^λ M η <= 2ML^kη. The boundaries of Λ_k and Ω_k are at least 2MR_k L^k η apart (CMP 119, quoted at I:63572-63574), and R_k >= L > 2 (I:63570). So y ∈ Ω_k. There the level is k >= λ, in B_k and in every stage structure of the step (λ_n = min{μ'', max{k, j}} = k on Ω_k ∩ X'; live pieces miss Ω_k, since W_a ⊂ Ω^c_{k_a} ⊂ Ω^c_k). Off every running class component the structure is that of B_k, and case 1 applies. At a point of a live piece the structure is the frozen one of the innermost live piece (precedence, I:132977-132985). That is the stage structure of the piece's own attempt at its stage n^+ (I:121787-121790), read on its own nest, and cases 2-4 and this paragraph apply to it at its density k_a. If λ >= 1, each case gives □ ⊂ Ω_λ ⊂ Ω_1. QED.

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

(ii) □ has side C L^λ M η <= 2ML^{k_c}η, and it contains x ∈ W_c = X_c ∩ Ω^c_{k_c} (I:131972). X_c is a component of the class Z ⊂ Z_{k_c} = Λ^c_{k_c} (I:131963-131965). A point outside X_c is in Λ_{k_c} or in another component of Z_{k_c}, and a path to it from x leaves X_c into Λ_{k_c} ⊂ Ω_{k_c}. The boundaries of Ω_{k_c} and Λ_{k_c} are at least 2MR_{k_c} units of level k_c apart (CMP 119, quoted at I:63572-63574). So dist_∞(x, X_c^c) >= 2MR_{k_c}L^{k_c}η - η >= 2ML·L^{k_c}η - η > 2ML^{k_c}η, using R_{k_c} >= L (I:63570) and L > 2. Hence □ ⊂ X_c. Then X_c ⊂ Z_{k_c} ⊂ Z_h (I:138393-138398, from (T2), (T4)) and Z_h ⊂ D_2 (I:91991-92031).

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

*Distance on Q^+.* Q^+ has sup-diameter at most (2M + 10 W_aux) L^λ η <= 3 M L^λ η, as M >= 16 W_aux. Join x to any point of Q^+ by four axis-parallel segments inside the box hull of Q^+, which lies in Ω_{λ-1} by the same margin. Each segment has length at most 3ML^λη and crosses at most 3L + 1 M-cubes of level >= λ - 1 (side >= ML^{λ-1}η). So d_sc(x, z) <= 4(3L + 1) <= 16 L for z in Q^+, by the path reading of d_sc in (I-G). Hence d_sc(z, 𝖲) >= Ř_k/2 - 16 L >= Ř_k/4. The path from x stays at positive d_sc from 𝖲. The support of B_2 ends at the cut, and 𝖲 contains the band of D_2 next to the cut (section 2). So the path stays in G, and Q^+ ⊂ G.

*Regularity on Q^+ at scale λ.* Let p be a plaquette (or b a bond) read on Q^+, attached to the block y' of level j := o(y') >= λ - 1. B2(a) gives ρ(y') <= 2 B_3 c_R ε^D_j, so (T1) gives |dU_2(p) - 1| <= 2 B_3 c_R ε^D_j L^{-2j} and the divergence test at L^{-3j}. Compare with scale λ:
- if j = λ - 1: ε^D_{λ-1} <= c_R ε^D_λ by (I-R), so the bounds are at most 2 L^2 B_3 c_R^2 ε^D_λ L^{-2λ} and 2 L^3 B_3 c_R^2 ε^D_λ L^{-3λ};
- if j >= λ: ε^D_j <= c_R (j - λ)^{1/2} ε^D_λ by (I-R), and (j - λ)^{1/2} L^{-2(j-λ)} <= 1, so the bounds are at most 2 B_3 c_R^2 ε^D_λ L^{-2λ} and the same with L^{-3λ}.

So U_2 obeys (T1) read at scale λ on Q^+ at radius ε' := 2 L^3 B_3 c_R^2 ε^D_λ <= 2 L^3 B_3 c_R^2 δ_D(t_γ) α_{0,λ}. This is the hypothesis the gate states for H14.1 (gate section 5, B2(c)).

*Gauge.* H14.1 gives s|A| + s^2|∇A| <= C_L M'' ε' on □, provided C_L M'' ε' is below H12's fixed ceiling c_12 (b102 lines 1882-1885). The ceilings

  (Γ_4)  128 C_L (CM + 2 W_aux) L^3 B_3 c_R^2 δ_D(t_γ) <= φ_flat B C M,
  (Γ_5)  B C M sup_{t >= t_γ} α_0(t) <= c_12,

give C_L M'' ε' <= (φ_flat/64) B C M α_{0,λ} <= c_12. (Γ_4) has degree p_0 + 2r - q < 0 under (Q); (Γ_5) has degree minus infinity; both are fixed last. QED.

*Not covered.* (a) A cube that meets K_0 but violates (S1) is not covered; no consumer routes one to the base bound. (b) b-in.md's "every cube of side at most CML^λη meeting K" is withdrawn. (c) The floor (M') is new; it is of the kind b102's order of constants allows ("Choose the original block and separation floors large ... for ... the independent auxiliary gauge family", b102 lines 1927-1929). M is fixed at Stage 6 of the account's order (I:1537), after d, L and the local constants.
