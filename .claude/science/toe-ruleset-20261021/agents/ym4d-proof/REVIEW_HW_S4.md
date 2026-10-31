# REVIEW_HW_S4: hostile review of lane H session 4 (HW.md §20-§28; HW_LOG session 4; checks/w4*, w4b*)

Reviewer: an independent agent that wrote none of HW.md, HW_LOG.md or checks/w4*. I edited no other file. No commits, PRs
or pushes.

Inputs (read-only; md5 at review time): HW.md 3f3a3a01… (1342 lines; §13-§28 read in full, §0-§2 for definitions),
HW_LOG.md 99105480…, REVIEW_RLARGE_V3.md 38b26eda… (Bottom line, Part 1 S-1…S-6), REVIEW_HW_S2.md 363fb1ae… (format),
RLARGE.md a9269bae… (grep: row 10b, K8), PLD.md def1982d… (§16.0-§16.12, l.1291-1606), HIST.md (§7.1-§7.2 l.452-503;
l.960-966 kernel data-reading; l.550 n_H), checks/w4_criteria.md a2cd8019…, w4b_criteria.md 31231b75…, w4_footprint.py
9ece45b5…, w4b_footprint.py 9e4b0f6c…, w4_out.txt, w4b_out.txt 028090b3…, w4*_time.txt, with mtimes. Scratch (the w4b re-run):
scratchpad `rhw4/`.

"Line" means a line of HW.md unless another file is named. Status words as in PROOF.md.

---

## Bottom line

- **Provenance: ACCEPTABLE.** I checked the pre-statement byte for byte: the first 1065 lines of the current HW.md are
  exactly 105745 bytes, md5 dd6b6633…, exactly the log's 10:19:45 record. So §0-§20 have
  not changed since the pre-statement. Both aborts used `kill` on the session's own PID, and the lock was released once each
  time. The w4 → w4b redesign is post hoc and labelled as such.
  - Three wording and disclosure defects (P-1…P-3):
    - the key ideas were reasoned before §20 (the log says so);
    - w4b changed three sample sizes that its criteria file does not name;
    - criterion C is tautological.
- **Lemma TILT, Lemma FP, Lemma NR, Theorem LI^U-0 [HW-9]: CONFIRMED (counted).** I re-derived each step:
  - persistence π(A_m) ⊂ Σ(Ω^c_m) ⊂ A_{m+1};
  - FP (i)-(iii) from the endpoint-block reading of HIST l.964;
  - the constraint step and the spectator step via (A2);
  - the noise representation.
  - **Consequence:** (LI) and (LI^F) hold under μ_{R(𝔥)} with c = 0 for ANY bounded column spectators. (M-i) under μ_{R(𝔥)} is
    PROVEN for SU(2). This is real progress: it closes HW's own open interface item A4.
- **Proposition LI-pw: CONFIRMED as ARGUED.** The mechanism is right: pure gauge inside a good cube, with the curvature on
  the straddling plaquettes, which no bad-only clause reads. Two wording fixes (LP-1): take k ≤ K − 2 with K − k fixed, and
  replace "probability ≥ ½" by "probability → 1". **(CRC) as a definition: CONFIRMED.** Its "written top-down induction" is a
  sketch: ARGUED, not proven (CR-1).
- **Lemma REL-boot [HW-10]: CONFIRMED (counted).** The finite-torus fixed point is valid, and its constants are uniform in T
  and K:
  - M is finite on each torus before the argument starts;
  - the inequality M ≤ 1 + M/4 is linear with coefficient < 1;
  - every constant is independent of T and K.
  - I re-derived steps (2)-(5), including y² + M(y − y²) ≤ 1 + M/4.
  - (PRICE^ℛ), ℛ_𝔥^↑, REL-seq and DECL do leave the route. **This is the most valuable item of the session.**
- **Finding J-1: CONFIRMED (genuine, missed by REVIEW_HW_S2 and REVIEW_RLARGE_V3). Lemma TEL-f: CONFIRMED (exact).** One
  recommended improvement (TF-1): telescope coarse-first. Node A's law then becomes the plain past law ν^R_k with a far
  weight, and the finer capped spectators drop out of it.
- **§24.3 slice requirement: WRONG AS WRITTEN (binding SL-1).**
  - The slice is mis-indexed: s_k(𝔥) is a slice by shadow level, but the level-k factor concerns 𝒰_{k+1}'s columns.
  - PLD §16 NA-PRICE does **not** satisfy it. NA-PRICE's allowance is S's own coarse shadow sum ‖S‖_sh.
  - It does not need to. For S under 𝒰_{k+1} I prove sh_m(S) ⊂ N_1(sh_m(𝒰_{k+1})), so Σ_k‖S_k‖_sh ≤ 81·s(𝔥) + Σ_k|S_k|. That
    is affordable through TEL-f.
- **(E1)/(E2), check (d), wall (CRC-1).**
  - Check (d) as a logical map: CONFIRMED-WITH-FIX.
  - (E1) is likely **false** in sup form, by a stronger argument than HW's (an [inference]). The same objection applies to
    PLD's (LCR), which is stated uniformly over all G that do not read the column (cross-lane, X-1).
  - (E2)'s buffer is undefined as written (E2-1).
  - **(CRC-1)** is a standard kind of object: a local partition-function ratio for the large-field constraints. It is NOT
    available from Theorem CE / CE-col. REL-boot's linear fixed point does not transfer to it as set up.
  - Difficulty: medium-high, of cluster-expansion strength for the constrained coarse gas. It is not a new kind of wall.
- **w4b re-run under the lock: IDENTICAL** to checks/w4b_out.txt in every result line (only `secs` differs). OVERALL PASS.
- **Tally:** 8 counted, as HW claims; both new counted items CONFIRMED.

---

## Priority 1. Provenance and the w4 → w4b sequence

### Pre-statement (HW_LOG 10:19:45; HW l.1027-1065): VERIFIED
- `head -n 1065 HW.md` gives 105745 bytes, md5 dd6b6633… (as in the log). Lines 1-1019 are 102014 bytes; with the
  missing final newline of the session-3 file this is the log's "was 102013".
- So the frozen sections §0-§20 have not been edited since. The only post-hoc in-place edit the log records (10:53, §24.3) lies
  after line 1065.
- File mtimes match the log:
  - w4_criteria 10:21:45 is before w4_footprint.py;
  - w4b_criteria 10:38:40 is before w4b_footprint.py;
  - w4b_footprint.py mtime 10:50:09 is the "≤ 2000 draws" fix, before run 2 at 10:50:17;
  - HW.md mtime 10:53:40.

### P-1 (wording; binding, cosmetic): the pre-statement was made after the key ideas
- §20's header (l.1027) says "written before any session-4 derivation", and l.1067 says "started 10:50 UTC".
- HW_LOG (session 4, first entry) lists the exploratory reasoning before the targets: "the tilt is h; footprint … endpoint
  blocks; relaxed shadows; a pure-gauge mechanism". Its 10:50 entry says the derivations "were reasoned 10:00-10:50 (partly
  before §20)".
- w4_criteria.md (10:21:45) already contains A_m := Σ(Ω^c_{m-1}) ∪ N_1(𝒰_m) and the containment law π^{m-k}({x_1, x_2}).
- So TILT, FP, LI^U-0 and the LI-pw mechanism were known in substance when U1-U4 were written. U2 (c) even lists "prove (LI^U)
  false in this case".
- This is the session-2 pattern (RHW2-fix W2-1) again. It is disclosed in the log, so it does not invalidate anything.
- *Fix:* l.1027 → "statements only, written before any WRITTEN session-4 derivation (key ideas reasoned before; HW_LOG)".
  l.1067 → "typed from 10:50 UTC; reasoned from 10:00 UTC, partly before §20". Append, do not rewrite.

### The w4 → w4b sequence: ACCEPTABLE and honestly labelled, with one disclosure gap (P-2)
- w4's FAIL is recorded as FAIL in §27 and §28, and its outputs are kept.
- The diagnosis is right. With density 0.04 / 0.005 per level, A_m covers almost everything (C_tested = 6 in d = 2 and 0 in
  d = 4). The negative control D then has nothing to reach.
- The redesign keeps criteria A-D verbatim. It adds "≥ 10 tests" for B, C and D, which strengthens them.
- Changing the sampler after seeing the failure is legitimate here, for two reasons: the failure was vacuity (nothing
  tested), not a counterexample; and the hypotheses being tested are deterministic combinatorics.
- **P-2 (binding, disclosure).** `diff w4_footprint.py w4b_footprint.py` shows more than the generator and sampler:
  - nhist 2 → 3 (d = 4);
  - nlinks 25 → 30 (d = 4);
  - the D sample cap 25 → 40.
  w4b_criteria.md and §27 say "changes ONLY the history generator and the link sampler". Append the three parameter changes to
  HW_LOG and to §27. (None of them can turn a FAIL of A or B into a PASS: those counts are exceptions, and they stayed 0.)
- **P-3 (recommended, scope).**
  - C is tautological under the reading rule. A level-k link interior to x is read by every level-(k+1) link incident to the
    site x inside π(x), and at least d of the 2d incident links are interior to π(x) when L = 3. So C checks that the rule is
    coded, not that it is non-vacuous.
  - In d = 4 the top torus has side 3, so N_1 of any nonempty set covers all of level K − 1 = 2. Hence S^{(2)} = ∅, and B and D
    are informative there only at k = 0.
  - Say both in §27's scope line.

### Aborts and lock hygiene: CONFIRMED
Each of the two aborted runs used `kill` on its own PID (exit 143). The lock was released once each time by the wrapper's
single rmdir. No pkill was used. HW_LOG and the time files agree, and no process was left.

---

## Priority 2. Lemma TILT, Lemma FP, Lemma NR, Theorem LI^U-0, Corollary LI-0

### Lemma TILT (l.1076-1087): CONFIRMED (elementary, uncounted)
- (i) holds because ∫K_i dU_{i+1} = 1 and Fubini. (ii) and (iii) follow.
- The brief's H_k = ∫K_k1_{R,k+1}h_{k+1} is h^{R,1}_k exactly. "(LI), (LI^F) and the tilt are one family" is right.

### Lemma FP (l.1091-1102): CONFIRMED (counted with LI^U-0)
- The reading rule is HIST l.964 verbatim: "S4' contours of c stay in c's two endpoint blocks". PLD Lemma CW's use, a
  plaquette "with all vertices in c's two endpoint blocks", is consistent with it.
- (i) by induction. A level-(m+1) reader c of a link with endpoints s, s′ has π(s), π(s′) ∈ {X, X + e_μ}, so c is incident to
  π(s) ∈ π^{m-k}({x_1, x_2}).
- (ii) a cube containing both endpoints contains s, hence equals π(s).
- (iii) the endpoint cubes are π(s), π(s′), and a common projection is π²(s).
- The level bookkeeping is correct throughout: a level-m cube is a level-(m+1) site, and "π^{m-k-1}({x_1, x_2}) read as level-m
  sites".

### Lemma NR (l.1104-1108): CONFIRMED (classical, uncounted)
- This is the randomisation lemma for a probability kernel into a standard Borel space. k_c(·; M) has a continuous density in
  (V, M), so joint measurability holds.
- The induction "U_m off F_m(A) is a function of (U_k off A, ξ)" is right, because K_m = Π_ck_c(V_c; M̄_c(U_m)).
- The equality h(U) = h(U′) holds for every U, U′ that agree off A, not merely almost everywhere, because the representation
  reproduces the law for each fixed argument.

### Theorem LI^U-0 [HW-9] (l.1110-1120): CONFIRMED (counted)
- **Step 1, persistence (re-derived).** Two facts:
  - Ω^c_{m-1} is pushed into Ω^c_m by H-nest (i), so π(Σ(Ω^c_{m-1})) ⊂ π(Ω^c_m) ⊂ N_1(π(Ω^c_m)) = Σ(Ω^c_m);
  - π(N_1(𝒰_m)) ⊂ N_1(π(𝒰_m)), because |⌊u/L⌋ − ⌊v/L⌋| ≤ 1 for |u − v| ≤ 1; and 𝒰_m ⊂ Ω^c_m (sh_m(𝒰_m) = 𝒰_m).
  So π(A_m) ⊂ Σ(Ω^c_m) ⊂ A_{m+1}, and the column of x stays relaxed at every m ≥ k + 1. CORRECT.
- **Step 2, constraints.** Bad-only 1_{R,m} reads ζ_Q(U_m) only for Q ∈ S^{(m)}, and ζ_Q reads the interior plaquettes of Q,
  whose links are interior to Q. By FP (ii) an interior footprint link lies in π^{m-k}(x_i) ∈ A_m. CORRECT.
- **Step 2, spectators.** By FP (iii), Q″ = π^{m-k+1}(x_i) ∈ Σ(Ω^c_m), and 𝒰_{m+1} ∩ Σ(Ω^c_m) = ∅ by (A2). CORRECT.
  Spectators at level m = k itself are excluded by hypothesis, as they must be.
- **Step 3.** Integrate ξ. CORRECT.
- Scope (stated correctly): bad-only, history-independent D_j, under R(𝔥). Collar-bad clauses read collar data across cubes
  and are not covered (scope H4).

### Corollary LI-0 (l.1122-1132)
- **(a): CONFIRMED.**
  - A = int(𝒰_{k+1}) at level k + 1. The endpoint cube is Q ∈ 𝒰_{k+1}, and π(Q) ∈ π(Ω^c_{k+1}) ⊂ Σ(Ω^c_{k+1}) ⊂ A_{k+2}.
  - LI-a: the level-(k+1) clause excludes N_1(𝒰_{k+1}).
  - So H4-red and H4-red′ hold with c_k = 0, and **(M-i) under μ_{R(𝔥)} is PROVEN for SU(2)** (KS PROVEN), with C_mis =
    (1 − λ)^{-3/2} per link.
  - LI-1's restriction to capped weights is indeed no longer needed: an exact independence gives ratio 1 for every weight.
    This resolves REVIEW_HW_S2's objection, rather than contradicting it.
- **(b): CONFIRMED, with a wording fix (LI0-1, binding).**
  - h^{R(𝔥),1}_k does not read U_k off L^far_k(𝔥). In particular it does not read the columns of 𝒰_{k+1} or of N_1(𝒰_{k+1}), nor
    Ω^c_k and its Σ-collar.
  - But "the future tilt on history columns is exactly absent" (l.1127; repeated in §26 "No longer hypotheses", l.1304-1305) is
    an overstatement. The tilt still reweights the column through its correlation with the far field under the past law. That
    is exactly why H6-H7 are stated under ν^{(k),h_k}_k.
  - *Fix:* "the tilt does not read the column; it enters only as a weight that is a function of the far field".
- **(c): CONFIRMED (geometry).** π(N_2(B)) ⊂ N_1(π(B)) for L ≥ 3.

**Answer to S-1 (l.1134-1137): CONFIRMED.** One nit: "(§23: the history columns)" should point to Cor. LI-0 (b) in §22.

---

## Priority 3. Proposition LI-pw and (CRC)

### Proposition LI-pw (l.1141-1163): CONFIRMED as ARGUED, with LP-1 (binding wording)
- **(α) is right in substance.**
  - Pure gauge U_{yz} = g(y)g(z)^{-1} on int x, with the crossing links fixed, keeps every interior plaquette trivial (x good).
    The curvature sits on the straddling plaquettes, which no bad-only clause reads.
  - The transporters of the two level-(k+1) links at x in directions μ and ν pick up relative factor G. So W_0(M̄) of the coarse
    plaquette at x changes by O(|G − 1|), not by a conjugation.
  - The configuration is not a gauge transform of the whole field, because the crossing links are not transformed.
- **(β)** is the KQ / RS-lin concentration at stiffness κu_k. The plaquette must be interior to π(x), so choose x away from the
  boundary of π(x). Say so.
- **LP-1 (a): the level.** The allowance has #(A) ≤ K − k for a single cube. The violation grows like e^{cε_1²u_k}, with
  u_k ≈ u_K + β(K − k)log L, so for fixed c_U it beats e^{c_U(|A|+#(A))} only when K − k is held fixed while g_K → 0. With
  k = K − 1, h_k ≡ 1: there are no constraints above level K − 1. So **state k ≤ K − 2 with K − k fixed** (k = K − 2 suffices).
- **LP-1 (b): the probability in (γ).** With "probability ≥ ½" the argument gives h(U) ≤ e^{-cε_1²/g²} + ½. That is a factor of
  about 2 against h(U′), not a divergent ratio. The device must make the n_♯ neighbouring cubes bad with probability → 1 under
  both U and U′ (the same device, applied deterministically off A). Then h(U) → 0. And h(U′) stays bounded below, because the
  n_♯ cubes form a component of size n_♯ without π(x). Replace "≥ ½" by "→ 1", and add that the n_♯ cubes are *-connected
  among themselves.
- The reading (1) "row 10g is false pointwise on constrained columns" stands. It also falsifies PLD §16.0's statement of
  (LI^U) in its full generality ("every finite set S", l.1299-1301); see X-2.

### (CRC)_k (l.1158-1163): the definition and the identity are CONFIRMED; CR-1 and CR-2 are binding
- The identity holds: R(𝔥) ⊂ R^{-B} gives μ_R(E) ≤ μ_{R^{-B}}(E)·Z(R^{-B})/Z(R).
- **CR-1 (binding).** "Theorem LI^U-0 applied to R^{-B}" is not covered by the theorem as stated, which is for R(𝔥).
  - Persistence still holds: π(π^{m-k}(B)) = π^{m+1-k}(B).
  - The spectator step fails if π^{m-k+1}(B) meets 𝒰_{m+1}. (A2) protects only Σ(Ω^c_m).
  - *Fix:* state Theorem LI^U-0′ for R^{-B}, either with F ≡ 1 or with spectators off B's column.
- **CR-2 (binding, status).** The "Top-down analysis of (CRC)" (l.1247-1258) says "(CRC)_k follows from (CRC)_m, m > k, by a
  written top-down induction". It is one paragraph with no displayed inequality chain. Label it ARGUED.
  - It re-introduces relaxed constraint patterns (R(𝔥) with relaxed columns, intermediate telescoping laws) and prices animals
    under them. That is (PRICE^ℛ)'s role in REL-seq, and REVIEW_RLARGE_V3 S-4's uniformity requirement.
  - So "S-3 and S-4 dissolve" (l.1203-1204) holds on the (E1) route only. Under (E2) + (CRC), node A's inputs are needed
    uniformly over the pattern family l.1255-1256 names. Say this at l.1203.

---

## Priority 4. Lemma REL-boot [HW-10] (l.1177-1208): CONFIRMED (counted)

I re-derived every step.
- **(1) A priori finiteness.**
  - T and K are finite, so there are finitely many histories.
  - Z(∅) > 0 (§13.1 (m2)).
  - Z(R(∅)) = Z(∅) by RX (iii), and s(∅) = 0, so M ≥ 1.
  - M is finite. This is the step §3.2's old remark lacked.
- **(2) Containment.** Z(R(𝔥)) ≤ Σ_{𝔥′∈H(𝔥)}Z(𝔥′).
  - On {𝔥(c) = 𝔥′}, a component 𝒟′ of 𝒰′_j is a *-connected subset of D_j with > n_♯ cubes (RX (i), history-independent D_j).
  - If 𝒟′ ⊂ S^{(j)}(𝔥), then it lies in one *-component of D_j ∩ S^{(j)}(𝔥), which contradicts c ∈ R(𝔥).
  - So every component meets A_j(𝔥). CORRECT. For 𝔥 = ∅, A_j(∅) = ∅, so H(∅) = {∅}, which is consistent.
- **(3) Per-history bound.**
  - (PH) for 𝔥′, then Z(R(𝔥′)) ≤ MZ(∅)e^{Bs(𝔥′)}. M enters once, not once per component.
  - s is additive over components by definition (l.1072), so the weights w(j, 𝒟′) factorise. CORRECT.
- **(4) Anchored sum.**
  - A history is determined by its set of pairs. Summing over all nonempty collections of pairs that meet A_j, admissible or
    not, is an upper bound (w ≥ 0): ≤ Π(1 + w) − 1 ≤ exp(Σw) − 1.
  - H-geo (iv) with M = K − 1 − j. (F_R) lower half: e^{-au_j} ≤ e^{-au_K}e^{aR}L^{-aβ_-(K-j)}.
  - The bracket is ≤ 0 for n ≥ n_♯ + 1. 6400^{n-1}(r/6400)^n = r^n/6400, and Σ_{n>n_♯} ≤ 2r^{n_♯+1}/6400 = ε′. All CORRECT.
  - Σ_j|A_j| ≤ 82Σ_j|Ω^c_j| ≤ 82s(𝔥), by H-nest (i), |N_1(𝒰)| ≤ 81|𝒰| and Ω^c_j ⊂ ∪_{i≤j}sh_j(𝒰_i). CORRECT.
- **(5) Fixed point.**
  - e^{-Bs} = y², e^{-Bs}e^{82ε′s} = y, and y² + M(y − y²) ≤ 1 + M/4. Maximising gives M ≤ 4/3. CORRECT.
  - Uniform in volume: yes. The argument is per torus, needs no limit, and every constant (4/3, ε′, B = 164ε′) is independent
    of T and K. Finiteness of M is used only qualitatively.
- **Order of constants.**
  - n_♯ ≥ n_H(a, B_0) with B_0 = c_f + 2 ≥ B_* already implies (n_♯ + 1)aβ_-log L > 38416B_0 ≥ 38416B_*, because
    n_H := ⌊(4 + 38416B_0/log L)/(aβ_-)⌋ (HIST l.550). So "(then …)" (l.1206) is right as written.
  - log(4/3) + 164ε′ ≤ 2 − 1 holds. Non-circular.
- **Recommended (RB-1).** REL-boot is in effect HIST-sum's anchored-sum argument applied to Z(R(𝔥)). One sentence saying so
  would help the integrator. Also note that (PH) is consumed for every admissible 𝔥′. Through Theorem HW^cap this means node
  A's H6-H7 for every 𝔥′. That is not circular (node A consumes no (H-w′)), but it is the full quantifier.

---

## Priority 5. Finding J-1, Lemma TEL-f, the slice requirement, and PLD §16 NA-PRICE

### Finding J-1 (l.1211-1215): CONFIRMED (genuine)
Theorem HW^cap's (M-f^cap) is one joint expectation over all levels (l.743-744). CAP-dec, (SDP)^A and (SF-cap)^A are per
level. The step from per level to joint was missing. REVIEW_HW_S2 Priority 3 and REVIEW_RLARGE_V3 1.1 item 5 both passed over
it. Good catch.

### Lemma TEL-f (l.1216-1224): CONFIRMED (exact)
- E[Φ_{≤k}] = E[Φ_{<k}]·E_{μ^{(k)}}[Φ_k]; induct. Φ_k ∈ [1, e^{θπ}] makes every normalisation positive. CORRECT.
- **TF-1 (recommended, strong): telescope COARSE-FIRST.**
  - Put μ^{[k]} := (Π_{k′>k}Φ_{k′})μ/E_μ[Π_{k′>k}Φ_{k′}]. Then E_μ[Π_kΦ_k] = Π_kE_{μ^{[k]}}[Φ_k] (the same identity, in reverse
    order).
  - The coarser spectators Φ_{k′} (k′ ≥ k + 1) are exactly the spectators Theorem LI^U-0 allows: Q″ ∈ 𝒰_{m+1}, m ≥ k + 1, a
    function of U_m on Q″'s column.
  - So by TILT (ii), μ^{[k]} restricted to U_{≤k} is **the plain past law ν^{R(𝔥)}_k** (constraints of levels ≤ k, no spectator),
    weighted by h^{R(𝔥),F}_k. That weight is again a function of U_k on L^far_k(𝔥) only.
  - With HW's finer-first order, node A's law ν^{(k)}_k carries the finer capped spectators Φ_{k′<k}. Those are functions of the
    finer fields outside A's columns, and no node-A statement is written under such laws: PLD's family ℛ^A_𝔥 has constraint
    patterns only, and its (SF-cap)^{A,+} allows F only on the columns of A′.
  - Coarse-first removes this extra tilt at no cost. It also gives PLD's past law ν^μ_k of PLD §16.0 verbatim.

### SL-1 (binding): the slice s_k(𝔥) in §24.3 (l.1232-1234) is mis-indexed, and NA-PRICE does not satisfy it
- **What HW asks.** The level-k allowance must be s_k(𝔥) := Σ_{(j,𝒟),j≤k}|sh_k(𝒟)|: the level-k shadows of the components of
  levels ≤ k.
  - The reason given is right: an allowance of e^{c·s(𝔥)} per level would compound to e^{Kc·s(𝔥)}.
  - But the remedy is the wrong slice. The level-k factor concerns the columns of 𝒰_{k+1}.
  - For 𝔥 with components only at level k + 1, s_k(𝔥) = 0. The requirement then demands the level-k bound with no allowance at
    all.
- **What PLD §16 NA-PRICE delivers.**
  - PLD l.1408: μ(S ⊂ D_k) ≤ (C_Ae^{-a_Au_k})^{|S|}e^{c_A‖S‖_sh}, with ‖S‖_sh := |S| + Σ_{m>k}|sh_m(S)|. These are S's own COARSER
    shadows (union form).
  - c_A = 4c_U + c_f + c_ns.
  - **So NA-PRICE does not satisfy HW's slice requirement** (‖S‖_sh ≥ K − k − 1, while s_k can be 0).
- **What is actually needed, and why it is affordable (proof).** Let S ⊂ the level-k descendants of A ⊂ 𝒰_{k+1}.
  - Claim: sh_{k+1+r}(S) ⊂ N_1(sh_{k+1+r}(𝒰_{k+1})) for r ≥ 0, where sh_{k+1}(𝒰_{k+1}) := 𝒰_{k+1}.
  - r = 0: Σ(S) = N_1(π(S)) ⊂ N_1(𝒰_{k+1}).
  - Step: Σ(N_1(X)) = N_1(π(N_1(X))) ⊂ N_1(N_1(π(X))) = N_1(Σ(X)).
  - Hence |sh_m(S)| ≤ 81·Σ_{𝒟⊂𝒰_{k+1}}|sh_m(𝒟)| for m ≥ k + 1. Summed over k (one S_k per level in TEL-f): Σ_k‖S_k‖_sh ≤
    Σ_k|S_k| + 81·s(𝔥).
  - The |S_k| part goes into C_A^{|S|} (CAP-dec's 81^{|A′|} count is already there). The s(𝔥) part is the c_f of Theorem HW^cap
    with c_f := 81·c_A.
  - This is REVIEW_RLARGE_V3 S-1's "absorption fact" for CAP-dec, made explicit.
- **Fix.** In §24.3 replace "the level-k SLICE s_k(𝔥)" by "S's own coarse shadow sum ‖S‖_sh (union form) for S under 𝒰_{k+1}",
  and add the claim above as a lemma (elementary, uncounted). In H6-H7 and in B_0, read c_f := 81(c_A + c_sf′).
- **Consequence for NA-PRICE after LI^U-0 (cross-lane note, X-2).**
  - On the HW route every NA-PRICE use is for S under 𝒰_{k+1}, and (SF-cap) is on the columns of A ⊂ 𝒰_{k+1}. These are relaxed
    columns.
  - So FT's tilt H′ = h^{R′,1}_k does not read ℓ(T): T is declared at level k, and the future clauses are R(𝔥)'s. Hence c_U = 0
    exactly.
  - So 4c_U and §16.7's c_f = 2c_U(1 + Δ_sh) vanish, and c_A = c_ns.
  - PLD's general hypothesis (LI^U) "for every finite S" is false pointwise on constrained columns (LI-pw). So NA-PRICE (i) for
    S in constrained columns (the off-route uses: K8 / EXISTENCE's single-cube union bound) rests on a false hypothesis.
  - The integrator should restrict NA-PRICE's (LI^U) to relaxed columns, where it is Theorem LI^U-0 with c_U = 0, and route
    constrained S through (CRC).
  - Also, Proposition WALL (b)'s alternative "(LI^U_loc), depth-free" is then available on relaxed columns: c_U = 0 there.

---

## Priority 6. Check (d), (E1)/(E2) and the wall (CRC-1)

### Check (d) (l.1270-1284): CONFIRMED-WITH-FIX as a logical map
- Every row is right as an implication map:
  - the only entry of coarser-level information on the HW route is h_k on L^far_k;
  - H4-red′ is case 0, exact;
  - REL-boot has no induction over levels;
  - nothing on the route consumes (H-w′), HIST-sum or (RLF-3′) at levels > k.
- Fixes:
  - with TF-1 the entry point is h^{R,F}_k (coarser spectators included), still far-only;
  - the "(E1): non-circular" verdict is right logically, but see E1-1;
  - the REL-boot row should add "(PH) for every 𝔥′ ⇒ H6-H7 for every 𝔥′".

### E1-1 (binding as a status note): (E1) in sup form is very likely false; HW's doubt (l.1242-1245) understates it [inference]
- (E1) asks the bounds for every bounded far weight. That is the essential sup over far-field values of the conditional law of
  the column given U_k on L^far_k.
- Take a far field carrying O(1) curvature at a distance of 2-3 level-(k+1) cubes from 𝒰_{k+1}. It is allowed: small far
  components are unconstrained in Ω^c regions, and permitted with ≤ n_♯ cubes elsewhere.
- Under the past law, the far U_k pulls the finer fields below the far blocks through the kernel likelihood (∝ e^{-κu_{k-1}φ}).
  The finer fields' own action is also ∝ u. So at small g the conditional law concentrates near the minimiser of a
  g-INDEPENDENT variational problem.
- Its interpolation into the column has curvature of order c_0·dist^{-p}, with c_0 = O(1). That is ≫ ε_1 ≈ 7·10⁻⁴⁰ at any fixed
  distance. Classical lattice gauge fields do not screen.
- So the conditional probability that a column cube is bad tends to 1. No g-uniform (SDP)^{A,far} holds in sup form.
- The topological "Stokes" reading at l.1243-1244 is not needed and is weak: the complement of a 4D blob is simply connected.
  The energetic argument is the real one.
- *Fix:* mark (E1) as "expected false in sup form [inference]". The route of record is (E2).
- **X-1 (cross-lane, for PLD / node A; I edit nothing there).** PLD §16.7's (LCR)_{k-1} is stated "for every bounded G ≥ 0 that
  does not read the level-(k−1) links in the columns of A∖A′". That class contains the collar AND the far field, so it is at
  least as strong as (E1).
  - On G_Q (column defect-free) the boundary can force sub-threshold column curvature of order ε_1.
  - Then u_{k-1}·Σ𝓔^{an} ≈ u ε_1²·n_int, which is ≈ 5·10¹² at the recorded g² ≲ 10⁻⁹¹ and ε_1² ≈ 5·10⁻⁷⁹.
  - So the exponential moment is not bounded by a g-independent c_lcr uniformly in G.
  - (LCR) needs the same good-buffer restriction as (E2).

### E2-1 (binding): (E2)'s buffer is undefined as written (l.1238-1241)
- "No level-k defect within the N_1-column collar of A (buffer of one level-(k+1) cube)" is ambiguous.
- The level-k cubes under N_1(𝒰_{k+1}) are in RELAXED columns (π ∈ N_1(𝒰_{k+1}) ⊂ A_{k+1}). Their defects would need no (CRC).
  The (CRC) term Σ_yμ(S ∪ {y} ⊂ D_k) makes sense only if y is in the first ring of FAR columns.
- *Fix:* define Buf_k(A) := {level-k cubes y : π(y) ∈ S^{(k+1)}(𝔥), dist(π(y), A) ≤ 2} (or the intended set), and state (E2) with
  it.
- Note also: by E1-1's mechanism, a good buffer is what makes (E2) plausible. Under a good one-cube buffer, the far defects
  beyond it still pull. (E2) has to assert that a buffer with curvature < ε_1 everywhere screens the column to within the
  (SDP)/(SF-cap) constants. That is plausible, but it is the real content of (E2), and HW should say so.
- [Recommended] Cor. LI-0 (c) lets R(𝔥)'s relaxed collar grow to N_r(𝒰_m) for any fixed r.
  - RX (i) survives: more relaxation is a weaker constraint.
  - REL-boot's count becomes 1 + (2r + 1)⁴.
  - This puts r − 1 buffer rings inside relaxed columns, which need no (CRC). Each (CRC) use is then preceded by r − 1 defect
    prices. It does not remove (CRC); it only suppresses it.

### Wall (CRC-1) (l.1260-1266): verdict
- **Is it a standard polymer or cluster expansion? Standard in KIND; not available OFF THE SHELF; not a new kind of wall.**
- **What it is.** (CRC)_k asks that relaxing the coarser constraints on a set of columns changes Z by a factor that is LOCAL in
  the relaxed set (e^{c_U#(B)}), uniformly in volume.
  - In the multiscale literature, local partition-function ratios for the large-field constraints come out of a convergent
    expansion of the constrained large-field gas, with large-field regions as polymers. Balaban's large-field analysis is the
    model; Kotecký–Preiss is the abstract tool.
  - The same-level regress (level-k far defect ↔ level-(k+1) animal) is the two-species interaction such an expansion handles
    natively.
- **Why the repo's tools do not give it.**
  - Theorem CE / CE-col (PROOF l.357, l.1946: Dimock I Thm 27 re-verified) is an analytic small-field polymer expansion. It needs
    product (or complex product) measures μ_x and activities with norm bounds.
  - Here the "activities" are conditional probabilities under constrained, tilted chain laws. There is no product structure and
    no written polymer representation of 1_{R} over levels > k.
  - CE-col's column version has the same hypotheses.
- **Why REL-boot does not transfer as set up.**
  - REL-boot's inequality is linear in M with coefficient 1/4 and anchored on the global Z(∅).
  - A direct REL-boot-type bound gives only Z(R^{-B})/Z(R(𝔥)) ≤ 1 + (4/3)e^{82ε′s(𝔥)}(e^{2ε′#(B)} − 1), from (PH), REL-boot and
    Z(R(𝔥)) ≥ Z(∅). The global factor e^{82ε′s(𝔥)} is not local, and it compounds through TEL-f's K levels.
  - The local bootstrap (sup over (𝔥, B) of log(ratio)/#(B)) is NONLINEAR: each single-cube use costs e^{c·#({y})} ≤ e^{c(K−k)}.
    A finite a-priori value then does not put it in the contracting basin. A continuity argument in an interpolation parameter
    would be needed.
- **Difficulty: medium-high.** In strength it is a volume-uniform decoupling or cluster estimate for the coarser large-field
  gas with a boundary. That is close in difficulty to R1^J's gas convergence (node A), but for the constrained future.
  - Its constants are favourable: per round ≈ (buffer count ~ 5⁴·81)·C_Ae^{-a_Au_k}·ε′, astronomically small. And c_U ~ 2ε′ ≪
    a_Aβ_-log L, so the depth allowance is beaten.
  - The obstruction is the representation, not convergence.
- **Priority.** (CRC-1) matters only if node A delivers (E2) and not (E1). By E1-1, that is the expected case, so (CRC-1) is in
  practice ON the route. §26 H9 should not read as a contingency.

---

## Priority 7. Check w4b re-run (MANDATORY NUMERIC LOCK; nice 10; OMP/OPENBLAS/MKL/VECLIB threads 1; no timeout; python without -I)

- Load before the run: 2.64 (< 8). The lock was not held. I acquired it with
  `until mkdir …/scratchpad/locks/numeric 2>/dev/null; do sleep 20; done` at 11:01:49 UTC, load 2.77.
- Ran `python3 checks/w4b_footprint.py` under `/usr/bin/time -l nice -n 10`: exit 0, 3.44 s, 16.8 MB peak RSS. Released with a
  single `rmdir` at 11:01:52. No trap, no pkill, no process left.
- Output in scratchpad `rhw4/w4b_rerun_out.txt`. **Identical to checks/w4b_out.txt in every count**: d = 2 A 1440/0, B 983/0,
  C 297/0, D 19/40; d = 4 A 180/0, B 134/0, C 21/0, D 14/40. OVERALL PASS. Only `secs` differs (0.6/2.8 against 0.7/3.1).
- Code review of w4b_footprint.py:
  - the reading rules (l.76-93), the constraint and spectator reads (l.106-117), A_m (l.61) and Ω^c (l.60) implement the
    criteria and HW's definitions faithfully;
  - π on the torus is well-defined (n[m] = top·L^{K−m});
  - the B filter (l.161) correctly excludes sampled links whose second endpoint leaves the relaxed column.
  - Scope caveats as in P-3.

---

## Corrected tally

| item | HW claim | verdict |
|---|---|---|
| §20 pre-statement | frozen at 10:19:45 | **VERIFIED** (bytes + md5); wording P-1 |
| Lemma TILT | uncounted, exact | **CONFIRMED** |
| [HW-9] FP + Theorem LI^U-0 | PROVEN-HERE, counted | **CONFIRMED**, counted |
| Lemma NR | classical, uncounted | **CONFIRMED** |
| Cor. LI-0 (a) | (LI), (LI^F) c = 0; (M-i) PROVEN SU(2) | **CONFIRMED** |
| Cor. LI-0 (b) | tilt "exactly absent" on history columns | **CONFIRMED-WITH-FIX** (LI0-1: far-only, not absent) |
| Cor. LI-0 (c) | geometry | CONFIRMED |
| Prop. LI-pw | ARGUED | **CONFIRMED as ARGUED** (LP-1: k ≤ K − 2 fixed depth; "→ 1" not "≥ ½") |
| (CRC) definition + identity | — | CONFIRMED; CR-1 (LI^U-0′ for R^{-B}) |
| top-down (CRC) analysis | "written induction" | **ARGUED** (CR-2); re-introduces pattern laws (S-4) |
| [HW-10] REL-boot | CONDITIONAL ⇐ (PH), counted | **CONFIRMED**, counted; uniform in T, K |
| Finding J-1 | new, binding | **CONFIRMED** (genuine) |
| Lemma TEL-f | exact, uncounted | **CONFIRMED**; TF-1 coarse-first recommended |
| §24.3 slice s_k(𝔥) | load-bearing | **WRONG AS WRITTEN** (SL-1: use ‖S‖_sh; Σ_k ≤ 81s(𝔥) + Σ|S_k|) |
| (E1) | sufficient; "doubtful" | logically sufficient; **expected false in sup form** (E1-1) |
| (E2) | sufficient with (CRC) | buffer undefined (E2-1) |
| wall (CRC-1) | OPEN, HW | standard kind, not off the shelf; medium-high; effectively ON the route |
| check (d) | written | **CONFIRMED-WITH-FIX** |
| Theorem HW (session-4 form) | CONDITIONAL, H1-H9 | **CONFIRMED-WITH-FIX** (SL-1 in H6-H7 and B_0; LI0-1 in "No longer hypotheses"; H9 not a mere contingency) |
| w4 | FAIL (design) | CONFIRMED as FAIL; diagnosis right |
| w4b | PASS (post hoc, criteria unchanged) | **CONFIRMED** (re-run identical); P-2 undisclosed parameter changes, P-3 scope |

Counted total: **8**, as HW claims (6 + [HW-9] + [HW-10]).

---

## Binding fixes (next lane-H session)
1. **SL-1.** §24.3, H6-H7, B_0: replace the slice s_k(𝔥) by S's own coarse shadow sum ‖S‖_sh. Add the lemma sh_m(S) ⊂
   N_1(sh_m(𝒰_{k+1})), hence Σ_k‖S_k‖_sh ≤ Σ_k|S_k| + 81s(𝔥), and set c_f := 81(c_A + c_sf′).
2. **LI0-1.** Cor. LI-0 (b) (l.1127) and §26 (l.1304-1305): "exactly absent" → "does not read the column; enters as a far weight".
3. **LP-1.** Prop. LI-pw: k ≤ K − 2 with K − k fixed; probability → 1 in (γ); x away from ∂π(x).
4. **CR-1, CR-2.** State Theorem LI^U-0′ for R^{-B} (F ≡ 1 or spectators off B's column). Mark the top-down (CRC) analysis
   ARGUED. At l.1203, restrict "S-3 and S-4 dissolve" to the (E1) route.
5. **E1-1, E2-1.** Mark (E1) "expected false in sup form [inference]", with the energetic mechanism. Define (E2)'s buffer
   explicitly. State that (E2)'s content is screening by a good buffer.
6. **P-1, P-2.** Append to HW_LOG and §27: the pre-statement wording; the w4b parameter changes (nhist, nlinks, D cap).

Recommended:
- TF-1 (coarse-first TEL-f: node A's law becomes the plain past law with a far weight);
- RB-1 (REL-boot = HIST-sum's anchored argument; quantifier "(PH) for every 𝔥′");
- P-3 (C tautological; d = 4 top torus fully relaxed);
- the N_r collar enlargement (E2-1);
- status pointers at §14 (LI^F) and §19 A4 (now PROVEN, c = 0).

Cross-lane, for the integrator and PLD (not HW edits):
- **X-1:** PLD (LCR) uniform over all G is at least (E1)-strength and expected false as stated. Restrict it to good-buffer G.
- **X-2:** PLD's (LI^U) on arbitrary S is false pointwise. On the HW route it is Theorem LI^U-0 with c_U = 0, so NA-PRICE's
  c_A = c_ns there. Off-route constrained S needs (CRC).

---

## Strategic verdict

- **Session 4 is the strongest lane-H session so far.** Two counted items are both correct:
  - LI^U-0 removes HW's own open hypothesis (LI)/(LI^F) outright, with c = 0;
  - REL-boot removes (PRICE^ℛ), ℛ_𝔥^↑ and the uniformity-over-patterns problem, on the (E1) route.
- J-1 is a genuine gap found and repaired, and Lemma TEL-f is the repair. The refutation of the pointwise row 10g is right,
  and it corrects REVIEW_RLARGE_V3 and PLD §16.0.
- **What remains is not HW's.** After this session, the HW route to (H-w′) is conditional on:
  - node A's per-level column bounds under the past law with a far weight (H6-H7);
  - (CLS-min) ⇐ (REG-min) (H2);
  - (F_R) (H1);
  - SU(2) / (KS-N).
- **The live risk has moved to one place: the form of node A's far-weight statement.**
  - (E1) (uniform over far weights) is very likely false at ε_1 ≈ 7·10⁻⁴⁰. PLD's (LCR) already carries that strength (X-1).
  - The realistic form is (E2), screening by a good buffer. It brings back (CRC-1) and the pattern-law uniformity (S-4).
  - So the next decisive work is one joint statement: "(E2)-screening + a local (CRC)". It needs a large-field expansion of the
    constrained coarser gas, a standard kind of object but unwritten here and of R1^J-type difficulty.
- **Recommended order:**
  - (i) apply SL-1 and TF-1, which are cheap and make the node-A interface exact;
  - (ii) the integrator re-states PLD's (LCR)/(J-NS^dir) and NA-PRICE's (LI^U) per X-1/X-2;
  - (iii) attack (CRC-1) together with (E2) as one cluster estimate. Do not attack them as two lanes.
