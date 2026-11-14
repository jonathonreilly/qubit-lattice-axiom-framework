Reviewer model: claude-opus-5-5

# ASSEMBLY55 — the full theorem's proof skeleton, every interface checked (session 26, worker file)

**Current reconstruction interface.** N9, ML2/ML9, item 18 and their summary references now distinguish the reviewed
ABSTRACT REC_LIB + REC_CONT producer from the still-missing Yang–Mills hypotheses. This bounded consumer correction is
[new authorship pending fresh independent review](checks/rec_consumer_alignment_note.md); other historical assembly
verdicts are not re-certified here. The owner's expanded target is full four-dimensional Yang–Mills existence AND a
physical continuum mass gap (MASS_GAP_TARGET.md). Both remain OPEN; the earlier T_OS milestone does not replace that goal.

UTC start: 2026-10-29T03:48:11Z
Author role: Opus 5.5 worker (brief: scratchpad/queue/assembly.md; shared rules: scratchpad/REVIEW_BRIEF_55.md).
Writes: this file and checks/as55_* only. No git.

## PRE-STATED (written before any derivation; statements only)

Targets.
- T1. A numbered theorem tree from T_OS (PANEL_P1.md: OS0-OS3 on R^4, non-free, no gap claimed, from
  H_reg, H_RP, H_Euc, H_int along a diagonal subsequence) down to leaves. For every node: the exact
  statement CONSUMED (norm, class, slice/gauge convention, domain, quantifier order, uniformity in
  k, T, a, R, n), the PRODUCER (file + locating string) with the exact statement PRODUCED, and a
  status in {banked (in PROOF.md [S26-BANKED] with its Codex scope), proven-pending-Codex, ARGUED,
  OPEN, NOT-VERIFIED}. "On disk, still being written" is recorded where it applies.
- T2. An arrow check for every edge: PRODUCED => CONSUMED exactly, or a MISMATCH finding with the
  precise gap and the smallest repair; a repair that is a new lemma is entered as an OPEN leaf, never
  asserted.
- T3. Missing leaves: inputs the top needs that no file produces (at least: RG estimates -> H_reg
  moment bounds for a determining family; diagonal-subsequence choice compatible with the sphere
  route's R -> infinity; the shared bare-coupling trajectory a -> g_0(a)).
- T4. The ordered list of OPEN leaves, each tagged by route (sphere vs flat; soft vs hard scheme;
  witness choice), and the single most dangerous one.

What would count as a refutation of an entry in this map (for the Codex checker).
- R1. A node marked "banked" whose statement or scope is not what PROOF.md's [S26-BANKED] block and
  the matching CODEX_REVIEW_*.md "Exactly what may be banked" say (located by string on disk now).
- R2. An arrow marked MATCH where the produced statement differs from the consumed one in any of:
  norm/weight, function class, slice or gauge convention, domain (lattice/torus/R^4, level k, flow
  time set), quantifier order, or uniformity parameter — or an arrow marked MISMATCH where the two
  statements are in fact identical (a wrong mismatch is as bad as a wrong match).
- R3. A leaf marked "missing / no producer" for which some lane file does produce the exact
  statement (cite file + string), or a leaf marked "produced" whose cited string does not say it.
- R4. Any node this map calls proved that its producer and Codex have not both established.
- R5. A symbol comparison made without fixing, by file:string, which object each symbol denotes
  (systemic defect 1), or an inequality quoted at a constant value that has since become an output
  (systemic defect 2).

Method commitments.
- Large files (PROOF.md, BFT_B.md, PLD.md, BFT_A.md, HW.md, FLOW.md, SF.md, SQ.md) are read only by
  grep -n then sed -n ranges; citations are by locating string because line numbers drift.
- Codex review files are read as they are on disk now; unfinished tails are flagged.
- Any numeric check gets checks/as55_<id>_criteria.md before its script; exact arithmetic only.

### PRE-STATED addendum (2026-10-29T04:04:46Z; coordinator's mid-task question, before any verdict on it is written)
Target C (coordinator). CODEX_REVIEW_NSL ("Exactly what may be banked", last paragraph) names as the most dangerous remaining
identification "uniform E_j^cb = the independently prescribed BR1 E_j^br for all j". Decide, arrow by arrow, whether ANY consumer in
the tree (RLARGE/HW/PLD/HIST, the flow, N5 / eps_N5_unif, existence-lane items) consumes E_j^br rather than E_j^cb; record each such
arrow as a MISMATCH with the smallest repair.
Refutation of my answer: (i) a consumer I call convention-free whose proof uses a BR1-specific object at a level j >= 2 (BR1's slice
ker h_{U^(0)}, its radius r(eps) = 12 c_inf eps, its constant 1 + 48 c_inf, NAH-ind's per-level radii) on a level-uniform domain; or
(ii) a consumer I call mismatched that in fact reads only trivial-point jets (germs), where the three objects below agree.
Reading done before this addendum (located by string): NSL55 §4.0 "Objects (Balaban's convention, BA-9)", §5 "Is E^cb = E^br
needed?"; CODEX_REVIEW_NSL "Exactly what may be banked"; PROOF "Lemma TOWER-VAR", "Lemma BR1 (the critical branch of the level-0
problem", "(MIN_1)", "(H-C) **in its extended form (H-C⁺)"; NORMS "By TOWER-VAR (d), D³E_k^br(1) = D³𝔉_k(1)"; FLOW "Def F-strip",
"(SF-bg)"; HIST "14.0 The tree tower", "(a5-U)"; PLD "fixes 𝔟(V) := the minimiser of E_k + the kernel term"; SF "(BG-unif)
[HYPOTHESIS", "A1.0 level-0 → 1 critical branch U(V) (BR1/NAH1)"; EXISTENCE "(M4) (BG-reg) [owner: layer 1, BR1/NAH1]",
"(N5-unif) CONDITIONAL ⇐ (H-K) + (H-C⁺) + (H-ℂ)"; SMALLNESS_DAG nodes eps_N5_unif, C_flat_i, CEexp; RLARGE "Current ε_1 ceiling",
row 3a, row 4; grep counts of E^br/BR1/C_♭/BG-unif/NAH in every consumer file (HW, PLD, HIST, SQ: zero E^br and zero BR1 hits).

---

# §1. Coordinator's question: which consumers read E_j^br rather than E_j^cb (answered first, as asked)

## 1.1 There are THREE objects, not two (symbols pinned by file and string; systemic defect 1)
- **E^br (PROOF's per-level branch).** PROOF "Lemma BR1 (the critical branch of the level-0 problem at curvature-small V):
  PROVEN-HERE [S20]": U(V) critical for F(·, V), unique in BR1's sup ball (radius r(ε) = 12𝔠_∞ε about the lift U^(0)(V)) in BR1's
  slice ker h_{U^(0)}; levels j ≥ 2 by NAH-ind with per-level hypotheses (I_j) and shrinking radii (PROOF "replacing BR1's
  ε_{i+1} ≤ ε_i/(1 + 36p_L𝔠_∞^{(i)})"; NSL55 §5.1 reading (R-P)). Defined on the CURVATURE-small class (global ε_V), not only on 𝒞_glob.
- **E^cb (Balaban's convention).** NSL55 §4.0: "E^cb_j(w) := 𝔉_j(exp Z_j(w); e^w)", Z_j = the depth-j point of Theorem BFT-E, on
  the fixed domain ‖w‖_D ≤ ε_u, 𝒞_glob only. Its own per-level recursion (Theorem ID (I2)) holds on fixed-radius balls (Corollary
  K-U). Banked conditionally (PROOF [S26-BANKED] "(NSL) and BFT-0's per-level identification — CONFIRMED conditionally").
- **E^min (the global-minimum tower)** — a third object the coordinator's question does not name, but which most large-field and
  flow consumers actually read. HIST "14.0 The tree tower": "𝓔_0 := Σ_ps(U_p), 𝓔_{i+1}(V) := min_U[𝓔_i(U) + κΦ_i(U, V)] (minimum
  over a compact group power; it exists)", with the elementary identity "𝓔_k(V) = inf over chains … of the equalised chain energy";
  FLOW "Def F-strip (the tree tower; uniform κ)": "𝒯_{k+1}(V) := min_U[𝒯_k(U) + κΣ_ck̃(V_c, M̄_c(U))]"; PROOF names its level-1
  instance E_1^NA ("E_1^br = E_1^NA needs (MIN_1) ⊂ B-NA"; "*Not shown:* that U(V) is the global minimiser of F(·, V) …
  named **(MIN_1)**").
- **Bridges that exist.** E1 (NSL55 §5.3; CODEX_REVIEW_NSL item 4 CONDITIONAL "E1 on its stated BR1 overlap"): E_1^br = E_1^cb on
  𝒞_glob(ε_E1), with ε_E1 built from BR1's not-computed C_♭, C_Δ^{BR1}, r_♭ (finiteness only), and CODEX_REVIEW_NSL notes BR1's
  proof "contains an L=3 specialization". E-ind (NSL55 §5.4): E^br_j = E^cb_j on j-dependent balls only. **E^min ↔ E^cb: no bridge
  on any uniform domain**; the needed statements are named but OPEN: HIST "(a5-U) [OPEN; lane D; classical] For real U ∈
  R_{2ε_1}(Λ_k) the minimiser of E^♭(·; U) is unique modulo chain gauge", PROOF (MIN_1).

## 1.2 Arrow-by-arrow verdicts

| # | Consumer arrow (file, locating string) | Object read; domain/quantifier it needs | Verdict | Smallest repair |
|---|---|---|---|---|
| C1 | SF "(BG-unif) [HYPOTHESIS" and "A1.k level-k tower uniform in k ((BG-unif))": "a tower U_{k-1}, …, U_0 with U_j a critical point of F_j(·, U_{j+1})" (F_j = E_j^br + κφ̂) and clause "(iv) the N_0-Lipschitz constants of Hess E_j^br in the chart at the lift ≤ C_BG", "for every k ≥ 1" | **E^br at every level j**, on a level-uniform class | **MISMATCH (convention).** REVIEW_S22 re-points (BG-unif) to BFT ("(i) ⊂ BFT-0 + BFT-1 … (iv) ⇐ BFT-4", RLARGE l.79), and BFT's producers deliver E^cb (BFT-E/ID; BFT34 route C "for the composite critical point"; BFT4W55 "for the composite critical value"). E-ind cannot carry level-uniform clauses (radii depend on j). | Restate (BG-unif) in Balaban's convention: F_j := E^cb_j + κ_jφ̂, tower := Theorem ID (I2)'s points, uniqueness := Corollary K-U (mod 𝒢^rt_j, fixed radius). No new estimate if SF's level-j uses are only through (BG-unif) (my reading; a line-by-line SF audit is NOT done here). Also a CLASS mismatch remains: (BG-unif) is for curvature-small V, BFT-E for 𝒞_glob (OPEN, OFFGLOB55). |
| C2 | EXISTENCE "(N5-unif) CONDITIONAL ⇐ (H-K) + (H-C⁺) + (H-ℂ) (or ⇐ BFT-0,1,2,4 without (H-K))" (quoted at SMALLNESS_DAG node CEexp); PROOF "(H-C) **in its extended form (H-C⁺) — level-uniform C_θ^{(i)}, … 𝔠_∞^{(i)}, C_♭^{(i)}" and "(H-ℂ) *the tower's complex extension has a level-uniform radius*" | **E^br at every level i**: class-wide Lipschitz constants of Hess E_i^br and the complex radius of E^br's tower, level-uniformly | **MISMATCH (convention)**, same reason as C1; the "or ⇐ BFT" alternative silently changes the object. Downstream arrows inherit it: eps_N5_unif → eps1, eps_loc, eps_J_loc (SMALLNESS_DAG edges 157, 158, 330), eps_N5_unif → CEexp (edge 304) → EXISTENCE (M2) "level-uniform stage-j expansion", RLARGE row 3a "N5 level-uniformity". | State N5-sf_i at the (R-B) background: the fluctuation operator Õ_i built from E^cb_i at ID's U_i(v); then (H-C⁺)/(H-ℂ) for E^cb follow from BFT-2 + BFT-4 by Cauchy (REVIEW_S22: "Consequently, by Cauchy: C_♭^{(k)}, (H-G) and the C_θ, C_θ^ρ, ε_θ constants are level-uniform") — once BFT-4 is proved for E^cb (BFT4W55 (a) pending Codex; (b) open). Retire NAH-ind from this chain. |
| C3 | SMALLNESS_DAG node "C_flat_i · off · … C_♭^{(i)} ((H-C)'s class-wide Lipschitz constant of Hess E_i^br, per level)" | E^br, per level | off-route; **MISMATCH only if revived** | Mark it retired under (R-B); its live replacement is BFT-4's Cauchy constant for E^cb. |
| C4 | Level-1 readers of BR1: SF "A1.0 level-0 → 1 critical branch U(V) (BR1/NAH1)" and "**C_bg** is read off BR1 (iii)"; EXISTENCE "(M4) (BG-reg) [owner: layer 1, BR1/NAH1] … BR1/NAH1 construct U(V)"; RLARGE "Current ε_1 ceiling" (2.40·10⁻⁷/C_♭, 1.13·10⁻¹⁸/C_Δ, 7.5·10⁻⁵r_♭: BR1's constants); SF "(real BR1 background (U(V), V) ∈ 𝔑(α_*)" (N5-sf0's background); PROOF "E_1^br = E_1^NA needs (MIN_1)" | **E^br_1 only** (level 1), on the curvature-small class | **MATCH on 𝒞_glob(ε_E1), conditionally** (E1; Codex NSL item 4). **Outside 𝒞_glob there is no E^cb to mismatch with**: these consumers then rest on BR1 itself, which is fine at level 1 but is a CLASS gap for the BFT route, not a convention gap. Two flags: ε_E1 is not explicit (BR1's C_♭, C_Δ^{BR1}, r_♭ unevaluated: RLARGE row 3c "(C_♭-eval), C_Δ evaluation" OPEN); BR1's proof is L = 3-specialised (CODEX_REVIEW_NSL), so BR1-at-level-1 consumers at odd L ≠ 3 are unsupported until BR1 is re-checked. | None now; when OFFGLOB55 extends E^cb off 𝒞_glob, add an E1-type overlap lemma on the curvature-small class at level 1. Evaluate or bound C_♭, C_Δ^{BR1}, r_♭ only if a two-sided window consumes them (they enter (TH-ch″), a one-sided ceiling). |
| C5a | Jet-only readers of the min-tower: FLOW55 "b_k is a one-step, gapped, trivial-point number b_k = 𝔅(J_k) of the tree jets J_k = (D², D³, D⁴)𝒯_k(1)"; UIR55 "(TC-b)_𝔍 orders 3, 4" and Lemma SPLIT/ENV-𝒯 "at every V near 1" (fixed n); FLOW55 table row "cubic tree jet D³𝒯_k(1) k-uniform \| Theorem N1-15"; NORMS "By TOWER-VAR (d), D³E_k^br(1) = D³𝔉_k(1)[ζ^c·, ζ^c·, ζ^c·]"; banked (T-UNIF) | trivial-point jets of order ≤ 4 (germs at V = 1), at each fixed k and T (UIR55: infinite volume) | **MATCH at germ level, given one unwritten lemma (GERM).** Jets at a point see only the germ; TOWER-VAR (d) and NORMS Lemma N1-2 already express D³ through the composite functional and the composite linear branch, gauge-reparametrisation-invariantly. The convention-independence of N1-15's bound (it is a statement about D³𝔉_k(1)[ζ^c…]) means the banked (T-UNIF) transfers to E^cb and E^min verbatim. | **(GERM)** [OPEN, small, standard]: at every fixed k, T, the three value functions are the values of nondegenerate critical families through the trivial chain on some neighbourhood of 1 (E^br: IFT at the nondegenerate trivial point; E^cb: ID (I2); E^min: compactness of the chain space + zero set at V = 1 = the pure-gauge orbit + N5-coer), hence share all trivial-point jets; formally (jet level) also in infinite volume. Plus CODEX_REVIEW_FLOW55 item 2: FLOW's k̃-tower must be the φ-tower for N ≥ 3 (jets of order ≤ 5 agree). |
| C5b | Uniform-domain readers of the min-tower: FLOW "(SF-bg) … The tree tower Φ_{j←n} and the functionals 𝒯_k are real analytic on a complex neighbourhood of the trivial field (in normalised Lie coordinates, uniformly in k)"; FLOW55 §7 "given **(SF-g)_k** (… analytic polymer representation of the step output on D_α(X) … constants uniform in k, K, T"; HIST "(I_k^E)" main term u_k𝓔_k with "𝓔_{k,x} … defined on the small-field domain by (SF-bg) (FLOW §4: the tower minimiser is unique, real-analytic and exponentially local there)" → HW, PLD ("fixes 𝔟(V) := the minimiser of E_k + the kernel term given V"), RLARGE row 4 "(I_k^E)″" | **E^min** on a k-, T-uniform domain, and LOCALLY on the small-field region Λ_k(𝔥) | **MISMATCH (object + class).** The producer (BFT-E, ID, BFT-2, BFT-3) gives E^cb on 𝒞_glob; nothing identifies the global minimiser with the BFT-E critical point on a uniform domain ((a5-U), (MIN_1) OPEN). This is NOT E^br-vs-E^cb, but it is the same kind of gap and it sits on the flow's remainder half and on the whole large-field main term. | Either (i) **(MIN-cb)** [OPEN]: for real data in the small-field region, every global minimiser of the chain energy lies, modulo composite gauge, in BFT-E's fixed slice ball, uniformly in k, T (then E^min = E^cb there by K-U; it contains (a5-U) and (MIN_1)); or (ii) restate FLOW's 𝒯_k and HIST's 𝓔_k as the critical value E^cb_k on the small-field domain (HIST already does so on its complex domain: "the critical value of the holomorphically continued chain energy at a critical chain"). Positivity, the one min-property used on that domain, survives (ii) for free: 𝔉_k is a sum of non-negative terms (s ≥ 0, φ̂ ≥ 0), so E^cb_k = 𝔉_k(x*) ≥ 0 = E^cb_k(1). Where HIST compares with large fields ((CLS-NA)), the min definition is genuinely used and (i) is needed. |
| C6 | Producers that print "E_k^br" while proving composite statements: BFT34_55, BFT4W55, KFACTOR_OFF55, BGT55, SRCCD55 §5.1 "BFT-4 (E_k^br = S_W + R_k …)", SRCAN55 row 15 | E^cb (they prove composite statements) | **MATCH** once BFT-0's clause states Balaban's convention (NSL55 §5.5's recommendation, not yet applied to REVIEW_S22's text) | Write "E_k^br := E^cb_k (Balaban's convention, BA-9)" into BFT-0/BFT-4's statement wherever cited. |
| C7 | NBG_A / NBG_B / NBG_ADJ / GREENT / RTARGET: "(H-C) names the Lipschitz constant of Hess E_k^br **on the class**", (N-bg) | E^br, per level | off-route (their consumer B-NA-red's per-level (G♯) is superseded by BFT-5's composite slice Hessian, REVIEW_S22 "BFT-5 (linear stability at the background). The composite slice Hessian at Z(V_k)") | Same as C2 if revived. |

**Answer in one line.** Yes: two live arrows read E^br at every level on a level-uniform domain — **C1 (SF's (BG-unif)/A1.k)** and
**C2 (the N5-unif chain: (H-C⁺), (H-ℂ) → eps_N5_unif → RLARGE thresholds and EXISTENCE (M2))** — both repaired by restating them in
Balaban's convention, which costs no new estimate beyond BFT-4 for E^cb (itself open) provided the consumers use no BR1-specific
object at j ≥ 2 (not audited line by line here). The level-1 readers (C4) are covered by E1 on 𝒞_glob(ε_E1) only. **The larger
interface problem is C5b: the flow's (SF-bg)/(SF-g) and the whole large-field main term (I_k^E) read a third object, the
global-minimum tower, which no banked statement identifies with E^cb on a uniform domain.** The flow's coefficient core (C5a) is
safe at the germ level.

---

# §2. Conventions of the tree

- Status words. **banked** = listed in PROOF.md [S26-BANKED] (as on disk 2026-10-29 ≈04:00Z, incl. the NSL line), with the scope of
  the matching CODEX_REVIEW_*.md "Exactly what may be banked"; **pending-Codex** = PROVEN/PROVEN-HERE by its Opus 5.5 producer, no
  completed Codex review (or a review on disk without a bankable section, or with one that has not yet been entered in PROOF);
  **ARGUED**; **OPEN**; **NOT-VERIFIED** (a Codex or my verdict that it is not established); **[m]** literature from memory.
- Arrow verdicts. **MATCH** (produced ⇒ consumed exactly), **MATCH-cond** (exact up to a named, unproved but stated side input),
  **MISMATCH** (finding F#, §5).
- Files in flight at the time of reading (on disk, still being written; status taken as on disk at the time given): CODEX_REVIEW_HINT2
  (to F13, no bankable section, 04:12Z); OFFGLOB55 (§0-§4.3, 04:12Z); ALIGN55 (§0-§2+, 04:12Z); LARGE55, BFT4B55 (PRE-STATED only);
  LCONV55 (§A-§G written, no Codex); UIR55 (complete through §8, no Codex); SPHERE55 (complete, §13 report, no Codex);
  HINT2_55 (complete, Codex in flight). CODEX_REVIEW_SRCAN and CODEX_REVIEW_BFT4W reached their bankable sections at ≈04:10Z;
  CODEX_REVIEW_NSL is complete and entered in [S26-BANKED].
- Level indexing (checked consistent across SRCCD55 §3.1, HINT2_55 R2.1, FLOW55 §1, RLARGE "(F_R)"): level 0 = bare lattice (spacing
  a), level K = reference scale ℓ_ref = L^K a = 1; u_j = 1/g_j², and β_- > 0 means u decreases toward coarse levels. MATCH.

# §3. The top

**N0. T_OS (target).** PROOF §0 "T_OS (the owner's target)": "There is a state on an E(4)-covariant algebra of gauge-invariant
observables on R^4. It arises as such a limit, satisfies OS0-OS3 (…), and is not a free theory." PANEL_P1 §1 "Reading of the
assignment": at a fixed nonzero renormalized coupling/scale; "The algebra, the renormalized lattice-to-continuum observable maps,
and the meaning of 'free' must be specified; otherwise those words can hide the main theorem." Owner leaves that the text leaves
open: **(OWN-alg)** which algebra; **(OWN-free)** which free class and identification; **(OWN-S4)** whether S^4_R lattice
regularisations with a position-dependent bare coupling count as "arising as such a limit" (PLAN_S26 §10: "the owner must accept
S^4 lattice regularizations as 'arising as such a limit'"; SPHERE55 §13: identifying the sphere state with a flat Wilson selection
"is needed only under the strict reading of T_OS, P4 H6"). Status: target; three owner leaves OPEN.

**N1F. Flat assembly lemma** (consumes N2-N5 on ONE common algebra along ONE sequence). Producer: PANEL_P1 "PROVEN — Assembly from
this contract" (Codex gpt-6-astra panellist P1). Produced: "Use the same subsequence for all required joint moments. … H_reg gives
continuous extension and OS0; H_RP gives OS2 …; bosonic permutation identities give OS3. H_Euc gives invariance first on the dense
subgroup and dense test family, then on the full Euclidean group by continuity. Continuity of W and H_int give |W(ω)| ≥ c". Status:
PROVEN by P1 (Codex); the decomposition is panel-unanimous (PLAN_S26 §10 (ii)); **not in [S26-BANKED]**. My check: the closure step is
elementary and I re-derived it (finite limits of finitely many moments preserve normalisation, each RP quadratic form, each permutation
identity and each fixed-g invariance identity; continuity of the E(4) action on the limit extends dense-subgroup invariance; a
continuous W passes a strict lower bound): **CONFIRMED as an implication, for inputs stated on one fixed algebra and one sequence.**
Its two silent requirements — the named reconstruction theorem behind "H_reg gives OS0" and a single algebra for all four inputs —
are leaves N9 (REC) and N6 (ALG) below.

**N1S. Sphere assembly lemma** (alternative top for the sphere route). Producer: CODEX_REVIEW_P4 §4.1 "Geometry and conditional
transfer" (**CONFIRMED** "with the uniformity and observable hypotheses below") and §4.2 (OS0 local-to-global, CONFIRMED conditional);
SPHERE55 §5.2-§5.3 (re-derived, agrees). Produced: given continuum sphere states ω_R (a → 0 at FIXED R, subsequentially) on a
common local algebra, invariant under SO(5) on the cap, RP for great spheres through the base point, with compatible normalisations,
and position-uniform unit-ball moment bounds "sup_{R≥R_0} E_R|Φ_R(f)|^n ≤ A^n(n!)^b p(f)^n, with A, b and the finite derivative order
in p independent of R, n", diagonal extraction over R gives E(4) invariance, RP for every affine hyperplane, OS3, OS0 on R^4; plus a
radius-uniform witness (CODEX_REVIEW_P4 §4.3: "Non-freeness is not a closed property"). **Order of limits: iterated** (§4.3: "The
safe order is continuum extraction for each R, followed by R→∞. A single joint sequence instead needs explicit control of the cutoff
errors along that sequence"). Status: Codex-CONFIRMED conditional implication; Opus agreement in SPHERE55 §5.3; not in [S26-BANKED]
(the only banked sphere item is equatorial RP).

# §4. Level 1: the contract inputs, consumed vs produced

**N2. H_reg.** *Consumed* (N1F, PANEL_P1 item 1): "Joint observable moments have cutoff- and volume-uniform continuity/growth bounds
sufficient for OS0, and a subsequence (a_j, R_j) with a_j → 0 and R_j → ∞ converges on a countable dense determining family"; growth
in n "sufficient for the reconstruction theorem actually invoked" (§1 table). Quantifiers: uniform in a, R; all orders n with a fixed
growth law; one algebra. (N1S consumes the unit-ball moment form (U-mom), N13.)
*Producer:* SRCCD55 "Proposition E (OS0 for the field e from SRC-κ(+LF) and SRC-I; no coarse decay)": separated n-point functions of
the clover density e_a in OS's ^0𝒮 form [m], power singularities δ^{-p_n}, factorial growth, uniform in a, R. *Status:* **NOT-VERIFIED**
(CODEX_REVIEW_SRCCD §7 and item 7: singleton gap, all-order LF path moments — exact counterexample within the stated Peierls hypothesis
— and the large-distance weight); its downstream distributional step CONFIRMED (§7 last paragraph). CODEX_REVIEW_SRCAN item 10: fixed
separated tests are reached, the full flat-test space "needs a uniform extension estimate". *Arrow:* **MISMATCH F2a** (form: moments
vs ^0𝒮 distributions) + inputs OPEN (N10).

**N3. H_RP.** *Consumed* (N1F): "The approximants to every positive-half polynomial obey reflection positivity, or have negative errors
tending to zero, for one common time reflection." (N1S): RP for great spheres through the base point S (CODEX_REVIEW_P4 §4.1 item 4).
*Producers.* Flat: PROOF "L9a. RP of the Wilson action, link reflection and site reflection: IMPORTED-AND-REVERIFIED" (pre-S24 ledger,
standard [Osterwalder–Seiler]; **not** in [S26-BANKED] — HANDOFF's "H_RP is exact for the Wilson action on the torus … (banked)"
overstates the banking status, not the mathematics). The OS-algebra elements e_a(x) are functions of the BARE links, and the soft
chain's level-0 marginal is the Wilson measure exactly (CODEX_REVIEW_HINT item 4, "invariance of the bare marginal under normalized
soft kernels"), so lattice RP applies to them directly once supports are at distance > a from the plane (eventually true for fixed
positive-time tests). **MATCH (flat).** Sphere: SPHERE55 §1.5 "The theta_mu RP is proved exactly as in §2 (same three ingredients)"
— a one-line claim, pending-Codex; the banked item is the EQUATORIAL RP (CODEX_REVIEW_P4 §1.1), which SPHERE55 §5.2 says "is not
needed for the flat limit at S". **MISMATCH F3 (status: the consumed RP is not the banked RP).**

**N4. H_Euc.** *Consumed* (N1F): "For each fixed compactly supported test polynomial F and each Euclidean motion g in a countable
dense subgroup, |ω_{a_j,R_j}(F_g) − ω_{a_j,R_j}(F)| → 0" along the common sequence; translations come free from exact lattice
translations plus continuity (PANEL_P1 "Translation invariance has a simpler mechanism"); the dense rotation subgroup from rational
rotations (CODEX_REVIEW_UNIV item 4, banked "with a continuous action required on the eventual state space"). (N1S) consumes fixed-R
SO(5) invariance of ω_R on the cap.
*Producers.* Flat: ROTDEF (CODEX_REVIEW_ROTDEF item 4, banked: "assuming the full CD, SRC-O, and SRC-W bounds, the stated
vanishing-error reduction to the single **normalized** coarse torque … equivalent to rotation invariance on the tested pair's orbit")
+ TQ55 (banked reductions; **TQ itself NOT-VERIFIED**, an infrared input). Sphere: SPHERE55 "Theorem 3.6 (fixed-R symmetry restoration
for the tested pair). CONDITIONAL on W0, W1, W3, N5, SRC-E" (pending-Codex as an implication; inputs OPEN; E10 corrects the
quantifiers of W1/N5); alternative mechanism UNIV55 Theorem U (CODEX_REVIEW_UNIV item 9, banked as an abstract induction with p > 2
and an AF envelope; its comparison inputs N1-N5 OPEN).
*Arrows:* **MISMATCH F4 (order: both producers give invariance of TWO-point orbits only)**; **MISMATCH F5 (sphere: SRC-E and U-mom
are of the form Lemma V refutes for point composites)**; **MISMATCH F6 (quantifier order: sphere produces iterated limits; N1F
consumes a joint sequence)** — repaired by using N1S as the sphere top plus a diagonal lemma (N7); flat route additionally needs
**TQ (OPEN, IR)**.

**N5. H_int.** *Consumed* (N1F, PANEL_P1 item 4): "A specified continuous finite-moment witness W vanishes on the named class of free
physical theories and satisfies |W(ω_{a_j,R_j})| ≥ c > 0 … at fixed nonzero renormalized coupling. The witness is local and survives
the physical OS quotient". (N1S, CODEX_REVIEW_P4 §4.3): "a fixed-scale, correctly normalized observable witness separated by a
positive amount from its calibrated free Yang–Mills comparator, uniformly in both cutoff and radius".
*Producer:* HINT2_55 "Theorem H-RED♮. PROVEN implication; CONDITIONAL on (F-tune), (TS-up), (TS-low), (MOM-E)": W_m = f(t₀) −
f(t^{(m)}) for the 4D Wilson-FLOWED **bare** plaquette density 𝓔 = t²E_pl (R1.1, Lemma INT is "stated for E_pl only"), separation
from conv(𝔊^col_∞ ∪ 𝔖) by SEP^col **relative to (ID♮)**. Banked part: HINT55 comparator for the narrower quadratic abelian class
(CODEX_REVIEW_HINT items 1-4). CODEX_REVIEW_HINT2 (in flight) F1: "ID♮ is a legitimate, preselected associated-graded/tree-level
calibration … The relative separation theorem is meaningful; absolute reconstructed-theory non-freeness is still GAP." F2-F3 CONFIRM
PAIR/colour and arbitrary-subtraction separation; F9 CONFIRMS INT/CONV/semicontinuity.
*Arrow:* **MISMATCH F1 (algebra / OS-quotient: the witness is not on the algebra on which N2-N4 are produced, and its one-point
function is not an OS invariant — HINT2_55 R1.10 (ii): "The 4D-flowed one-point function is not an OS invariant (CT, Codex
CONFIRMED)")**; the YM-side inputs are OPEN (N15), (TS-up) needing a large-field estimate no lane file approaches (F17).

**N6. (ALG) the common algebra — MISSING LEAF (no producer).** Consumed by N1F ("a fixed common local continuum algebra/test
hierarchy", PANEL_P1 §3) and N1S ("on a common local algebra", CODEX_REVIEW_P4 §4.1). What each producer actually uses: N2, N4
(flat and sphere): the clover energy density e_a, smeared, in ^0𝒮 form (SRCCD55 §3.2 "For OS0 the minimal list is 𝒪_0 := {e_a}";
ROTDEF/SPHERE55 F_s = centred product of two smeared e's); N5: the flowed bare density 𝓔(t, x) on 𝔈 (HINT55 §1.2), or Branch D's
block energy Ψ_m, or the time-zero 3D-flowed 𝓑 (HINT2_55 R1.9). No file states one algebra containing a determining family for OS0,
an E(4) action, a positive-half generating set, AND the witness (or a proof that non-freeness on 𝔈 implies non-freeness of the
OS theory of the e-field). **OPEN** (owner part: OWN-alg, OWN-free; mathematical part: F1's repair).

**N7. (SEQ/DIAG) one sequence.** Flat: one subsequence (a_j, R_j) for N2-N5; HINT2_55 "Lemma CONV" supplies "along a further
subsequence of any H_reg subsequence the joint laws of {𝓔(t, 0)}_{t∈D}, … converge (jointly with H_reg's other observables, by the
same diagonal argument)" (CODEX_REVIEW_HINT2 F9 CONFIRMS at the probability-law level): **MATCH-cond** on N6. Sphere: the iterated
construction needs **(DIAG)** to meet "arises as such a limit": from per-R subsequential limits ω_{a,R} → ω_R and ω_R → ω_∞ on one
countable family (the same for every R: SPHERE55 (U-alg)), extract a_j(R_j) with ω_{a_j(R_j),R_j} → ω_∞ — a metrizable diagonal
argument. **OPEN, standard, unwritten** (and only needed under OWN-S4's strict reading if lattice states on the sphere count at all).

**N8. (TRAJ) the shared bare-coupling trajectory — MISSING as a single stated object.** Consumers and the trajectory each reads:
SRCCD55 §3.1 "The coupling sequence is the chain's own, obeying (F_R) … with g_K = g_ref ≤ min(g_thr, γ_0) fixed (ROTDEF I3)";
HINT2_55 R2.1 "F-tune's tuned sequence at fixed renormalised coupling g ∈ (0, g₁]"; RLARGE "(F_R)_{[0,k]}" along "the soft chain's
own effective coupling sequence (u_k) (FLOW Def F-g)", a fixed-point condition (FI-1, banked conditionally: CODEX_REVIEW_RLU item 2);
CODEX_REVIEW_UNIV §9: Theorem U needs the two-sided envelope g_j² ≤ (g_*^{-2} + B(n − j))^{-1}, "not a formal ≈"; SPHERE55 §1.4: a
POSITION-DEPENDENT profile β_Q = 2N/G(aΩ(z_Q))², with (G-np) "the bare coupling of the flat Wilson lattice on a line of constant
physics fixed nonperturbatively" or (G-pert) a two-loop formula. *Producer:* FLOW "Theorem F-tune" (defined in infinite volume, Def
F-g + (SF-∞)), conditional on N16. *Arrows:* torus consumers: **MATCH-cond** — all read F-tune's g_0(a; g_ref) at ℓ_ref = 1; the
envelope Codex UNIV asks for follows from (F_R)'s lower half iff u_K > R (put g_*^{-2} := u_K − R, B := β_- log L; the same condition
CODEX_REVIEW_SRCAN item 6 records as "u_K − R_F > 0"), i.e. g_ref² < 1/R must be imposed explicitly. Sphere: **MISMATCH F14** — no
flow theorem for a position-dependent bare coupling exists (FLOW/UIR55 are constant-coupling, translation-invariant statements), and
W0 needs either the exact lattice step-scaling (G-pert: mismatch O(G⁴) "IF the exact lattice step-scaling function … has the
perturbative two-loop asymptotics nonperturbatively") or locality of the marginal flow (G-np). CODEX_REVIEW_SRCAN item 3/6:
propagation of a marginal shift has a proved UPPER bound only; the lower bound needs sup_j q_j < 1.

**N9. (REC) — ABSTRACT producer available; actual YM application OPEN.** The former literature-only MISSING label is
superseded by [REC_LIB](REC_LIB.md) §§6,15,18 and [REC_CONT](REC_CONT.md), reviewed in [REVIEW2_REC](REVIEW2_REC.md).
The precise consumer is now OSLEAF55 REC (e). It requires ONE hierarchy on the flat test spaces ^0𝒮_n with S_0=1, reality,
permutation symmetry, full E(4) covariance, ordered-half mixed-word reflection positivity, and
  |S_n(F)|≤α(n!)^β‖F‖_{sn,1}    for ALL n≥1,
with one fixed (s,α,β). For a scalar, ‖·‖_{k,1}=|·|_k; for finitely many real Cartesian tensor species it is the sum over
component words, with the explicit J=D_E(θ), C=⊕diag(i,1,1,1)^{⊗rank} dictionary of OSLEAF55 §4 / REC_LIB §15.
General unspecified O(4) representations are not covered. This producer yields tempered local Wightman fields, a cyclic
invariant vacuum and forward-cone spectrum on the SAME OS Hilbert space, with its semigroup generator identified. It does
not prove that the actual YM hierarchy meets the input contract, identify a scalar sector with the full physical theory,
or give a unique vacuum, a nonzero excited sector or a physical mass gap.

**Dependency direction and matching.** Actual all-order RG/source estimates → cutoff/volume-uniform H_reg-sep → common
limit satisfying E0′; add the actual E1/E2/E3/(Re)/S_0 contract → REC. Reconstruction CONSUMES growth; it does not produce
H_reg from SRC-κ. REC_LIB §16 / OSLEAF55 GROW prove the conditional pointwise match: with Z=1, q_X=4 and uniform
UNCONDITIONAL (SEP-pt), s=11 and β=b_0+1. To set b_0=p+2 requires the all-order outer joint-cumulant bound (16.4), including
singleton blocks; the higher conditional SRC-κ bounds alone are insufficient. For q_X≥0 use Q=ceil(q_X) and
s=max(11,Q+6). The alternative smeared route needs (X1) with its linear-growth and shrinking-separation quantifiers before
EXT applies. Actual singleton/outer-product moment bounds, these uniform inputs, all-order covariance, the common field
hierarchy/sequence and its physical identification remain OPEN. Sphere use also retains the radius-uniform flat-limit
hypotheses; the flat abstract theorem supplies none of them. E0 alone gives the OS semigroup and single-cut analyticity,
not the full multi-time continuation: the reviewed continuation uses E0′. The older warning about products of unbounded
continued insertions remains valid.

# §5. Level 2: from the RG to the contract inputs

**N10. SRC (source-inserted RG) and its clauses.** *Consumed* by N2 (Prop E), N11 (ROTDEF inputs), N13 (sphere W1/W3 analogues), N15
((TS-up) "Needed: (SRC) two-sided control of E[𝓔(t)(U₀) | level-k field]"). Statement consumed (SRCCD55 §3.3 "SRC-κ (the consumed
form)"): constants depending only on (N, L, κ_±, g_ref), **for every a, every torus R and every U_K ∈ 𝒮_K** (𝒮_K: "max_P|log U_{K,P}|_op ≤
ε_0 (BFT's ε_0 at level K)", a CURVATURE-small class); (κ-1) e-cumulants **all orders n**, mutual distances ≥ 4a, POINTWISE weights
δ_i^{-d_α}·(logs)·e^{−m_c tree_ℓ}, growth C_0^n(n!)^p; (κ-2) one insertion of O_α with **0 ≤ n ≤ 2** further e-insertions; (κ-3)
coarse images bounded and quasi-local; SRC-κ-LF path-sum form on large coarse fields; SRC-M (eight constants O(g_bare²), remainders
O(a²𝔏)); **SRC-I** "P_ν(A ⊂ 𝔏(U_K)) ≤ ε_LF^{|A|}, uniformly in a, R".
*Producers and status.* SRC-poly ⇒ SRC-κ (SRCCD55 Proposition A; CODEX_REVIEW_SRCCD item 2: CONFIRMED only as "separated-support
local-counterterm cancellation and the mixed Cauchy estimate … a corrected two-set geometry"; "Neither H-Bal-loc's unconditional
statement nor the sup-norm polydisc supplies the full pointwise SRC-κ package"); SRC-poly itself OPEN. SRCAN55 Proposition SA-S:
SMEARED SRC-κ (e-part, all orders) from (A) uniform complex bounds on cross-support second derivatives + (B) real-tilt CD — CONFIRMED
as conditional inequalities (CODEX_REVIEW_SRCAN item 3: "geometric growth follows only with explicitly uniform-in-n radii and
envelope control"); (A) partly done (SA-K tree level on 𝒞_glob, CODEX_REVIEW_SRCAN item 4; N5/N6/RLF complex, (Flow-an), rooted
summability OPEN), (B) OPEN; pointwise weights and κ-3(e): reduced to (P1)/(LOC-e) — CODEX_REVIEW_SRCAN item 9: "reduction to the
scalar flow derivative NOT-VERIFIED", item 8: "need for genuine local first-order image control". SRC-I: on hypercubic tori "EXISTENCE's
chessboard Lemma CBE + (RLF-3^dis)" (SRCCD55 §0; CODEX_REVIEW_SRCCD item 4 confirms only "the chessboard-to-Peierls implication for
matching reflected block events"). Proposition B (exact Markov/source recursion) banked.
*Arrows:* **MISMATCH F10** (smeared vs pointwise; OS0 needs a uniform test-function extension); **MISMATCH F7** (𝒮_K is
curvature-small, every BFT producer is on 𝒞_glob); **MISMATCH F4** (κ-2 stops at n ≤ 2 while H_Euc needs all n); **MISMATCH F15**
(coupling-field norm); **MISMATCH F24** ("decay = BFT-4's decoupling family" identifies a classical family with the quantum (D1)).

**N11. ROTDEF's I5 inputs (flat H_Euc): CD-avg, SRC-E′, SRC-O, SRC-W′.** SRCCD55 Propositions C, D (as implications of SRC-κ(+LF),
SRC-M, SRC-I). CODEX_REVIEW_SRCCD item 5: CONFIRMED "the product-cumulant identity, … the symmetry-allowed insertion contact, and the
a²ℒr⁵ coarse bulk estimate under its explicit moment/matching hypotheses. **NOT-VERIFIED:** the complete derivation of SRC-E′, SRC-O,
and SRC-W′ from the present literal package". The replacement SRC-E → SRC-E′ is banked in substance (item 3: SRC-E is incompatible
with non-vacuity along (F_R)). *Arrow to ROTDEF:* **MATCH-cond** (ROTDEF's Theorem 7.1 is stated with SRC-W; it needs SRC-W′'s O(g²)
contact, which its error term already contains — SRCCD55 §0 item 2).

**N12. TQ (flat-route IR input).** TQ55; CODEX_REVIEW_TQ items 1-8 banked as reductions; "**TQ for four-dimensional Wilson Yang–Mills
remains NOT-VERIFIED**". Item 5's sufficient condition RA-1 is "SRC-E-supported" — **MISMATCH F19** (uses the refuted SRC-E; restate with
SRC-E′). **OPEN, infrared, flat route only.**

**N13. Sphere-route UV inputs (SPHERE55 §6 list).** W0 (sup_x|c_4(a; x)| → 0), W1 (bulk insertions, two-scale conditional, renormalised
form per E10), W3 (|C(s)|/Z_e² ≤ C[g_bare² + a²L(a)]), N5 (seam transparency, separated Ward form; N5-cond ⇒ N5 PROVEN-HERE as an
implication; N5a/N5b OPEN; mechanism ARGUED), (N5-RG) (BFT/RLF/flow for the seam contour family "outside" the hypercubic statements),
(N5-op), SRC-E (sphere), (U-mom), (U-alg) (by construction), (U-NT). All pending-Codex as implications; every input OPEN.
*Arrows:* **MISMATCH F5** (SRC-E, U-mom), **MISMATCH F13** (domain), **MISMATCH F14** (W0 needs a position-dependent flow).

**N14. Rotated-lattice universality (alternative to N13's Ward route).** UNIV55 Proposition T (banked: "the coarse law never enters" at
fixed volume) and Theorem U (banked abstract induction, CODEX_REVIEW_UNIV item 9, with **p > 2**, the AF envelope of N8, N3 at all
coarse configurations, N4 observable comparison, the curved/profile variants and N5 seam). "These assumptions contain the main unproved
two-theory comparison" (Codex §9). **OPEN.**

**N15. H_int's Yang–Mills side.** HINT2_55 R2.1: **(TS-up)** f_{K,R}(c_tL^{−2(K−k)}) ≤ C₊g_k^{2(1−ϑ)}, ϑ < 1, all K, R ≥ R₀, d₀ ≤ k ≤
K − m₀; **(TS-low)** f_{K,R}(t₀) ≥ c₋g_{k₀}²; **(MOM-E)** sup_{K,R} ω_{K,R}(𝓔(t₀,0)^{1+δ}) < ∞. All **OPEN**; R2.4: (TS-up) needs (SRC) for
the flowed bare density at every level **and** (LF-inst) "P_j ≤ Ce^{−c_LF u_j} … with c_LFβ₋ > 4" (ARGUED: the Balaban-type factor
e^{−c p(g_j)²} loses against L^{4(k−j)}; "no estimate in the lane delivers a large-field bound of that strength"). CODEX_REVIEW_HINT2 F4
(in flight): "The large-field source and coupling normalization are stale". **F17.**

# §6. Level 3: the RG core

**N16. Coupling flow.** *Consumed* (N8, N10's (F_R), N14's envelope, N15's F-tune, RLARGE's (F_R)/F-mono, SA-F): FLOW55 §1 summary —
"(i) one-step: |u_k − u_{k+1} − b_k| ≤ C_ρg_k² (+|δβ_k| ≤ g_k⁶) whenever g_0..g_k ≤ γ, (ii) cumulative (F_R), (iii) tuning, (iv) all of it
torus-independent", with β_- > 0 fixed before C_ρ and γ.
*Producer chain:* FLOW Theorems F-flow/F-tune (arithmetic CONFIRMED upstream; spot-checked in FLOW55 §7) ⇐ (UNIV-1L) ⇔ (UIR^♮)
(CODEX_REVIEW_FLOW55 item 4, banked conditional reduction; "(UIR♮) itself remains NOT-VERIFIED") ⇐ UIR55 Theorem UIR-T: (TC-b)_𝔍 at
orders 3, 4 + (ρ-null) ⇒ (UIR^♮) (pending-Codex; (ρ-null) ARGUED after UIR55's own erratum 3.5′) — plus, for the remainder half,
**(SF-g)_k** (needs N5 at levels ≥ 1 at complex backgrounds, (NA-H_loc) OPEN, and BFT-0 analytic), **(RLF-δ)_k** (FI-1, banked
conditionally), **(SF-cont)** (IMPORTED, CMP 109 as read by FLOW), **(SF-∞)** (stated hypothesis).
*Arrows:* **NEW MATCH F23** — UIR55 lists "(TC-b)_𝔍 orders 3, 4 … OPEN (order 3: N1-15 unweighted, CONDITIONAL; order 4: nothing)" and asks
lane A for "an exponentially weighted version of Theorem N1-15 (order 3) and its quartic analogue"; BFT34_55 "Theorem BFT3-glob" (E)
already gives, at every B in its polydisc (so at B = 0), "|∂^nE_k^br/∂B_{y_1}⋯∂B_{y_n}| ≤ C_E(n − 2)!(2/ϱ)^{n−2}(N² − 1)^{n/2}·
e^{−(m/(n−1))𝔱(y_1, …, y_n)}" uniformly in k ≥ 1 and T ≥ 3 (banked conditionally: CODEX_REVIEW_BFT34 item 1, "Rates through order four
… μ/3 for E"), conditional on (H1) (= BFT-E, banked), (H2)_m (GV-E_m banked, CODEX_REVIEW_GV item 6; or Corollary H2W, CODEX_REVIEW_BFT4W
item 2 CONDITIONAL) and (H3)_m (BFT4W55 Theorem H3, CONDITIONAL on reading (R), CODEX_REVIEW_BFT4W item 3 and "Single most dangerous
unverified input: (R)"). A pointwise bound C e^{−(m/(n−1))𝔱} gives the weighted row-sum bound (J2) for any m_0 < m/3 (n ≤ 4; polynomial
entropy of trees in d = 4). Remaining to make the arrow exact: (GERM) (C5a of §1: FLOW's 𝒯_n is the φ-normalised min-tower, BFT3-glob's
E is the composite critical value — same trivial-point jets), the T → ∞ limit of T-uniformly decaying translation-invariant kernels
(standard), and the normalisation map between 𝔉_k's κ_jφ̂ and the "stripped φ-tower". So **(UIR^♮) ⇐ (ρ-null) + (R) + (GERM) +
standard items**, not "(TC-b) + nothing at order 4". **MISMATCH F11/C5b** on the remainder half ((SF-bg), (SF-g)_k read the min-tower on
a k-uniform domain); **F22** (FLOW's literal k̃-tower is REFUTED for N ≥ 3 at non-trivial backgrounds; use the φ-tower, CODEX_REVIEW_FLOW55
item 2).

**N17. BFT-0/1/2.** *Consumed* (REVIEW_S22 "Statement (BFT)"): for every k ≥ 1, every torus with level-k side ≥ T_0 **and every
non-wrapping box**, every level-k field V_k = e^zV_k^r with "max_P|log V^r_{k,P}| ≤ ε ≤ ε_0" (CURVATURE-small) and |z|_∞ ≤ r_ℂε; norm 𝔐
(Hölder curvature, divergence-form sources, level weights L^{θ_w(k−j)}); BFT-0's identification "E_k^br(V_k) = 𝔉_k(Z(V_k); V_k)".
*Producer:* GV55 "Theorem BFT-E (assembly)" (banked: CODEX_REVIEW_GV item 4; KOFF item 5) — **on 𝒞_glob** ("V_k = e^{B_k}, s := ‖B_k‖_D in
one global gauge"), m = 0, T ≥ 3, trivial-chain centring, slice S_E (Γ^{(T)} at T = 3, 4), weights (θ_w^c, θ_w^r, θ_A) = (2, 2 + σ, 1),
conditional on the lane-A linear package (N24); NSL55 Theorem ID + Corollary K-U (banked conditionally, CODEX_REVIEW_NSL items 2-4):
the composite-action tower in Balaban's convention; "Not banked: uniform identification with the independently prescribed higher-level
BR1 actions E_j^br …, boxes, non-trivial backgrounds, complex I3/I4"; SRCAN55 SA-K: survives complex position-dependent couplings in the
sup-plus-Wilson-Hölder class (CODEX_REVIEW_SRCAN item 4). Off 𝒞_glob: OFFGLOB55 (in flight: Proposition C4 "𝒞*_glob is a strict subclass;
the size gap is √ε"; U2 "the C^{1,α} half fails for the axial gauge"; LOC-cc_U; nothing assembled yet).
*Arrows:* **MISMATCH F7** (class), **F21** (boxes), **F11** (E^br readers C1/C2).

**N18. BFT-3.** Banked conditionally on the global potential-small domain (CODEX_REVIEW_BFT34 item 1; "Neither the original per-level
tower identification nor the full curvature-small class is banked"); route T rates conditional on (H2)^Lip, (H3)^Lip (BFT4W55: supplied
as implications, Codex CONDITIONAL). *Consumers:* RLARGE (BG)_k ("locality radius R_bg of 𝔟(V) (load-bearing)", on the LOCAL
small-field region of a history) — **MISMATCH F7**; EXISTENCE "(M4) (BG-reg) … ⇐ BFT-1 + BFT-3 at n = 1" — MATCH-cond on 𝒞_glob(ε_E1)
via E1 (C4); FLOW/UIR55 jets at 1 — **MATCH F23**; CE-exp^k's (L-loc)_k needs ALL orders ("BFT-3 states orders ≤ 4 only, so (L-loc)_k is
beyond BFT as stated", SMALLNESS_DAG node CEexp quoting EXISTENCE) — BFT4W55 §7 "All orders, order-independent rate" via BBcc + lane B
BB-4c(iv) (CODEX_REVIEW_BFT4W item 3 CONDITIONAL, premise (R)) — **MATCH-cond**.

**N19. BFT-4.** *Consumed* (REVIEW_S22): "E_k^br = S_W + R_k with R_k = Σ_X R_k(X) a sum of **gauge-invariant local** polymers, and
||R_k||_𝒜 ≤ C_0", sup on "the BFT-2 [polydisc] in **curvature-adapted coordinates**"; consumers: PROOF/N5 (via Cauchy: "C_♭^{(k)}, (H-G)
and the C_θ, C_θ^ρ, ε_θ constants are level-uniform"), SRC (κ-3 locality, (D1)). *Producer:* BFT4W55 "Theorem BFT4a-glob" — "E_k^br(B)
= S_W(e^B) + R_k(B)" for the composite critical value on the global-gauge polydisc 𝒫_ε (PD-glob), pieces "invariant under constant
gauges", "not locally gauge invariant"; Convention C (centred contours). Status: CODEX_REVIEW_BFT4W item 3 CONDITIONAL "with (R)/F^σ and
the local complex density, linear and Ward estimates named as premises"; item 5: do not bank "local gauge invariance of the pieces, or
extension off the global potential-small domain". BFT-4 (b): BFT4B55 (PRE-STATED only). *Arrows:* **MISMATCH F8** (constant vs local gauge
invariance; consumption of (b) undecided — BFT4B55's T0), **MISMATCH F7** (PD-glob vs curvature-adapted polydisc), **F9** (Convention C
must replace the lane's default lower-corner positions wherever W-mult^σ is used: CODEX_REVIEW_BFT4W item 1 PROVES "the lower-corner
all-chain multiplier obstruction").

**N20. BFT-5 (linear stability at the background).** Z = 1: banked (GF-E/GF-E′ on S_E at m = 0; clause (b) gauge-invariant half CC-FUN,
TOP-cc, CC-INV; with decay COF_m, CC-FUN_m, TOP-cc_m; GV-E, GV-E_m; TR∞/CC-CRIT∞ — CODEX_REVIEW_GSHARP, TOPCC, COFM, GV, HIGHER).
Z ≠ 1: Theorem GA banked (CODEX_REVIEW_BGT items 1-5) + "an actual alignment with uniform quotient/source/defect estimates" OPEN — ALIGN55
(in flight) "Lemma RED (exact reduction). PROVEN-HERE": GA's hypotheses ⇐ (P1), (P2-tw), (NC), (NS), (HD), (FW), (AC). *Consumers:* SF
"(a5-G♯)" posed in "per-level covariant slice through ψ^r"; B-NA-red "Let 𝒮 be a linear chain gauge slice"; G-pert/(G♯-patch).
*Arrows:* **MISMATCH F12** (GSHARP55 "Proposition GF-DEP": clause (b) "as written is false for field components"; correct form: orbit norm
or the named slice S_E; consumers still posed in the per-level slice must be restated — GSHARP55 §5.5 "no live route consumes it");
**F7** (Z ≠ 1, local).

**N21. Large fields.** *Consumed* by SRC-I and SRC-κ-LF (N10), (RLF-δ) (N16), (I_k^E)″ (main term), N13's (N5-RG) "action-based
large-field bounds" (no chessboard on the sphere), (TS-up)'s (LF-inst). *Producers:* RLARGE v3 "Theorem RLF, v3 (amended target; OPEN)";
banked pieces: W-cb♯, FI-1 (CODEX_REVIEW_RLU items 1-2, conditional); node A: reductions + BL-TILT banked (CODEX_REVIEW_NODEA, NRES);
LCONV55 (pending-Codex) "**(LC-1′) is FALSE on the lane's multiscale small-field region; the multiscale claim is REFUTED**" (stripe,
exact checks lc55_1-4) and G1 "the convexity window and the Peierls window are disjoint", G3 recommended residual "(LCR°) ⟸ [one-step
conditional positivity …] + [a cluster expansion … with an inhomogeneous coupling] + [(LC-3′)^tilt]" — "a larger obligation than (LC°)";
(a5-U), (CLS-NA), (MIN_1) OPEN; LARGE55 (PRE-STATED only) is re-pricing the whole architecture against an action-based Balaban/Dimock
split (CODEX_REVIEW_BALX: coupling-dependent cuts p(g_k) "coexist with fixed regularity radii"). **OPEN; F18.**

**N22. Per-step fluctuation estimates.** N5 (one-step covariance decay): Theorem N5-sf0 at level 0 "PROVEN [S19, unreviewed]" (PLD
l.1020 table), levels ≥ 1 ⇐ (NA-H_loc)_i OPEN; N6 (per-step polymer bound) OPEN (SRCCD55 §0); Theorem RW at the trivial background
(lane). *Consumers:* (SF-g)_k (N16), SRC (A) complex (N10), (N5-unif)/eps_N5_unif (C2 of §1). **OPEN** (and C2's convention repair).

**N23. Constants.** SMALLNESS_DAG: strict acyclicity banked (CODEX_REVIEW_DAG); NOT-VERIFIED "source completeness, an unconditional acyclic
choice hierarchy, exhaustive K/T uniformity, FI-1, the stronger moment-tail input, and the analytic-width matching"; the two-sided windows
(TC) (removed from W-cb♯ only), EXISTENCE Compatibility (K), and the complex-width interface ("Until node A chooses one, steps 3 and 5
cannot both use their stated complex domains") are OPEN; the cutoff-family edge n_♯ → SC_k closes a return path (an obligation). LCONV55
G1 adds a new two-sided incompatibility (convexity needs t ≲ g, Peierls needs u t² ≫ 1). **OPEN.**

**N24. The lane-A linear package** (LINEAR_PACKAGE Thm 4.2(ii), LES-div, LR-pot, W0, GU, BL-4/5, Lemma Λ, Q-hold, CR-1, Corollary WR …).
Every banked BFT item is "conditional on the named lane-A linear inputs" (CODEX_REVIEW_KOFF item 5; GV items 2/6); GV55 §3.2 row 5:
"banked/CONFIRMED at lane level … conditional on their own named inputs (not re-audited here)". These are pre-S24 ledger items, not
re-banked in S26. **Status for this map: inherited, NOT-VERIFIED at the S26 two-family standard** (a leaf, not a gap I can price).

# §7. Arrow findings (every MISMATCH, with the precise gap and the smallest repair; repairs that are new lemmas are OPEN leaves)

**F1 — H_int ↛ T_OS: the witness is not on the OS algebra (MISMATCH, algebra/quotient).** Consumed (PANEL_P1 item 4): "The witness is
local and survives the physical OS quotient", evaluated on the same state as OS0-OS3. Produced (HINT2_55 H-RED♮): a bound on Euclidean
one-point functions of the 4D-flowed bare density on 𝔈, separating from free classes **relative to (ID♮)**; HINT2_55 R1.10 (ii): not an
OS invariant; CODEX_REVIEW_HINT2 F1: absolute non-freeness "still GAP"; the e-field algebra of N2-N4 does not contain 𝓔. *Gap:* no file
proves that non-freeness of the joint Euclidean state on 𝔈 implies non-freeness of the OS theory reconstructed from the e-field.
*Smallest repairs (each an OPEN leaf):* (a) **(W-T0)** use HINT2_55 R1.9's time-zero 3D-flowed 𝓑, which is positive-time local and has a
reconstructed-theory comparator value, and add 𝓑 and its rotated versions to the OS algebra (needs OS0 for 𝓑, OS1 for the rotated
family, sharp-time finiteness, (TS-up)^B); or (b) **(W-e)** a calibrated witness built from separated e-field correlations (e.g. the UV
behaviour of r^8 S_2^e(r)), which needs a new comparator theorem for :F²: two-point functions of free field strengths (no file) and an
AF upper bound at n = 2 that SRC-κ's growing logarithmic envelope 𝔤_α does not give; or (c) an owner ruling (OWN-free) that non-freeness
"relative to (ID♮) on the joint Euclidean state" is what T_OS means, plus joint convergence (Lemma CONV: MATCH).

**F2a — H_reg ↛ N1F as worded (MISMATCH, form).** PANEL_P1 speaks of "Joint observable moments" and CODEX_REVIEW_P4 §4.1/§4.2 and
SPHERE55 (U-mom) of unit-ball moments of smeared fields; for the point composite e_a no cutoff-uniform moments exist with a non-vacuous
state-independent normalisation (SRCCD55 Lemma V; CODEX_REVIEW_SRCCD item 3, scoped to (F_R)). The producer (Prop E) is posed in ^0𝒮.
*Repair:* restate H_reg (and N1F's closure step) for separated Schwinger distributions in ^0𝒮 — the closure step survives (RP forms pair
θx with y at strictly positive times; permutation and invariance identities are linear in the distributions) — and add the uniform
extension estimate CODEX_REVIEW_SRCAN item 10 names ("the full flat-test space needs a uniform extension estimate"). Bookkeeping for the
restatement; the extension estimate is an OPEN leaf (**(EXT)**).

**F3 — H_RP (sphere): the consumed RP is not the banked RP (MISMATCH, status).** N1S consumes RP for great spheres through S; SPHERE55
§5.2 uses θ_μ ("the four coordinate great spheres {z_μ = 0} are exact lattice RP planes"), justified only by §1.5's "proved exactly as in
§2 (same three ingredients)" (pending-Codex; §1.5's own "I do not use it below except as a cross-check" contradicts §5.2/§13 — internal
inconsistency). The banked equatorial RP feeds only PANEL_P4's S3 route, which needs observables crossing the equator, i.e. N5 in
contact form, which SPHERE55 says it does not need. *Repair:* a Codex check of θ_μ RP on K_a (the only non-standard cells are prism cells
crossing {x_μ = 0}); then bank it. **OPEN (small).**

**F4 — H_Euc producers give two-point orbits only (MISMATCH, order n).** Consumed: invariance for "each fixed compactly supported test
polynomial F" (all n). Produced: ROTDEF item 4 "rotation invariance on the tested pair's orbit"; TQ item 1 "the centred Wilson two-point
orbit"; SPHERE55 "Theorem 3.6 … for the tested pair". And SRC-κ's (κ-2) carries "0 ≤ n ≤ 2 further e-insertions", so the inputs exist
only for pairs. *Repair:* the n-point version — the Ward identities (ROTDEF Prop. 3.2; SPHERE55 §3.1) hold for every smooth F, so the
work is the inputs: (κ-2) for all n with stated growth, W1/W3/N5 (sphere) and CD/SRC-O/SRC-W′/TQ (flat) for n-fold centred products, with
Z_e^{-n} normalisation. **OPEN (both routes).**

**F5 — SPHERE55 consumes hypotheses of the type Lemma V excludes (MISMATCH, consistency).** SPHERE55 §3.5 "SRC-E (sphere): Var(F_s)/Z_e^4
bounded uniformly in a and s" (used in Lemma 3.5's term "(Var F)^{1/2} inf_c (…)^{1/2}" and in Theorem 3.6) and §5.4 "(U-mom)
Position-uniform local moment bounds for the renormalized smeared energy density" with Z_e(a) "the state-independent normalization of e_a
(ROTDEF SRC-E)". SPHERE55 never cites SRCCD55 or Lemma V. *Gap:* (U-mom) at n = 2 gives Var(O_a(f))/Z_e² ≤ A²p(f)², while Lemma V gives
Var(O_a(f)) ≥ (3/2000000)g_0⁴a⁻⁴(‖f‖² − O(a)) — on tori (CODEX_REVIEW_SRCCD item 3); its proof (as reconstructed in CODEX_REVIEW_SRCAN
item 1: conditioning on single links of an even sublattice and their SU(2) cosets) is local, so it applies in the bulk of K_a with the
local coupling (**my reading; NOT-VERIFIED**). Then Z_e² ≳ g_0⁴a⁻⁴, and every polylogarithmic separated upper bound makes the normalised
separated correlator vanish: exactly the scoped incompatibility Codex banked. For SRC-E (sphere) (a degree-2 product) the same conclusion
needs a joint lower bound on two conditional variances, which I have not proved (ARGUED). *Smallest repair:* in Lemma 3.5 keep
‖E[F|W_s] − EF‖_2 instead of bounding it by (Var F)^{1/2} — the inequality |Cov(E[F|W_s], E[J|W_s])| ≤ ‖E[F|W_s] − EF‖_2·‖E[J|W_s] − c‖_2 is
exact — which replaces SRC-E by an SRC-E′-type coarse-image bound at scale s (consistent with SPHERE55's own E10 accounting); replace
(U-mom) by separated-point ^0𝒮 bounds (U-sep) and re-prove CODEX_REVIEW_P4 §4.1's contraction lemma in that form. **OPEN leaf
(U-sep + ^0𝒮 contraction); the Lemma 3.5 change is bookkeeping.**

**F6 — sphere route vs N1F (MISMATCH, quantifier order).** N1F needs one joint sequence with lattice-state defects → 0; the sphere route
produces "For each R: a -> 0 along a subsequence … Then R -> infinity" (SPHERE55 §5.1). *Repair:* use N1S (Codex-confirmed iterated
transfer) as the sphere top, plus (DIAG) for "arises as such a limit" (N7). **OPEN-small (DIAG standard, unwritten).**

**F7 — BFT class: 𝒞_glob / PD-glob produced, curvature-small or LOCAL consumed (MISMATCH, class/domain).** Produced: BFT-E (𝒞_glob),
BFT3-glob ("This is BFT-3 on 𝒞_glob(ε_0(m)/2) … It is **not** BFT-3 on BFT's full class"), BFT4a-glob (PD-glob), ID (𝒞_glob), SA-K
(𝒞_glob), GV-E_m/COF_m (Z = 1). Consumed: REVIEW_S22 BFT (curvature-small, tori and boxes); SRC-κ on 𝒮_K (curvature-small at level K on
a torus of side R → ∞, where a generic small-curvature field is not potential-small in any global gauge — OFFGLOB55 Proposition C4,
in flight, "𝒞*_glob is a strict subclass"); RLARGE (BG)_k on a history's small-field region; SF (BG-unif); HIST (I_k^E) and (a5-U) on
Λ_k(𝔥)/R_{2ε_1}(Λ_k); BFT-4's Cauchy step on "the BFT-2 one in curvature-adapted coordinates"; BFT-5 at Z ≠ 1. *Repair:* BFT-0..5 on
the curvature-small class and on local small-field regions with frozen exterior: (UHL)/(G♯-patch)/(SL-cov)/(LOC-GA) + the Z ≠ 1
alignment (ALIGN55) + the local Hessian inverse CODEX_REVIEW_BALX names. **OPEN (OFFGLOB55, ALIGN55; the most load-bearing analytic
leaf).**

**F8 — BFT-4 pieces: constant-gauge vs local-gauge invariance (MISMATCH if (b) is consumed).** Consumed: "a sum of gauge-invariant local
polymers" (REVIEW_S22); the per-polymer localisation that extracts marginal constants (SRCCD55 §5.4 (iii): "BFT-4's single polymer norm
does not do this"). Produced: BFT4a-glob pieces "invariant under constant gauges", "not locally gauge invariant" (CODEX_REVIEW_BFT4W
item 5). *Repair:* BFT4B55's T0 (is (b) consumed?) then (CovLift)/(Mult-Y)/(Pair-loc)/(I-id)_Z. **OPEN (BFT4B55).**

**F9 — contour positions (MATCH-cond).** CODEX_REVIEW_BFT4W item 1 PROVES the lower-corner multiplier obstruction; Convention C
(centred) must be adopted for every W-mult^σ/(W-comm)^σ use, including lane B's §10.8 and BFT34_55's (refuted) RW-cc-walk.
Bookkeeping.

**F10 — SRC: smeared produced, pointwise consumed (MISMATCH, test-function class).** Prop E consumes (κ-1)'s pointwise weights;
SRCAN55 delivers smeared SRC-κ only and "CANNOT … give pointwise weights"; CODEX_REVIEW_SRCAN item 10 re-diagnoses the residue as "a
missing uniform test-function estimate" and names a second strategy (source radius r_z(δ) = cδ^α, giving power singularities
δ^{−α(n−2)}). *Repair:* either (P1)/(LOC-e) canonical first-order images at every level, or the shrinking-radius envelopes. **OPEN.**

**F11 — E^br / E^cb / E^min (§1).** C1, C2 MISMATCH (restate in Balaban's convention); C4 MATCH on 𝒞_glob(ε_E1) via E1; C5a MATCH given
(GERM); C5b MISMATCH (needs (MIN-cb) or a critical-value restatement). **(GERM), (MIN-cb) OPEN.**

**F12 — slice convention for BFT-5 (b) (MISMATCH, bookkeeping).** GSHARP55 "Proposition GF-DEP" (banked, CODEX_REVIEW_GSHARP): "Even
for one fixed (cc) source there is no C with ||x_Γ||_{X_c} ≤ C for every admissible gauge fixing Γ"; consumers SF "(a5-G♯)" ("per-level
covariant slice through ψ^r"), B-NA-red ("Let 𝒮 be a linear chain gauge slice", per-level by choice), RTARGET's (G♯_0-field) wording.
*Repair:* restate each in S_E or the orbit norm (GSHARP55 §4.2). Bookkeeping, no new estimate (GSHARP55 §5.5's per-level transfer is
ARGUED and not needed).

**F13 — RG producers live on hypercubic tori; the sphere consumes them on K_a (MISMATCH, domain).** SPHERE55 §4.5: "BFT and RLF are
stated for hypercubic hierarchies on tori and non-wrapping boxes; a seam family is outside them"; K_a has digital-ball boundaries, a prism
seam with valences {5..9} and weights in [3/4, 3/2]β, shortest-path seam contours, a position-dependent β_Q; SRC-I's chessboard is
torus-only ("the sphere has only five RP planes, so FILS chessboard estimates are unavailable globally"). *Repair:* (LOC-T) a locality
transfer for the bulk (conditional estimates given the coarse field depend only on the local geometry: ARGUED, SPHERE55 §5.4 "Why
local") + (N5-RG) for the seam layer + action-based SRC-I. **OPEN (sphere route; large).**

**F14 — constant-coupling flow produced, position-dependent profile consumed (MISMATCH, trajectory).** See N8. *Repair:* **(FLOW-pos)**
a flow/locality theorem for slowly varying bare profiles (W0's c_4 → 0), with a lower propagation bound (CODEX_REVIEW_SRCAN item 6:
"A positive lower propagation bound additionally needs sup_j 2C_bg_j⁴/ρ < 1"). **OPEN (sphere route; also SRC sources).**

**F15 — coupling-field class for source insertions (MISMATCH, norm).** SRCCD55 §0 (i): "BFT, N5, N6, RLF and (F_R) must therefore hold
uniformly over a sup-norm ball of coefficient fields"; SRCAN55 Lemma SA-J: "the sup-norm class is too large for BFT-1's Hölder clause";
CODEX_REVIEW_SRCAN item 4 banks SA-K "in the sup-plus-Wilson-Hölder coefficient class". *Repair:* restate SRC's source class in ‖·‖_cf;
point sources then enter only through the shrinking-radius route of F10. Bookkeeping + F10.

**F16 — witness density (MATCH-cond).** HINT55 R1.1 allows "a fixed (plaquette or clover) lattice energy density"; Lemma INT (the
continuous-time step) is "stated for E_pl only". Fix E_pl. Bookkeeping.

**F17 — (TS-up) needs a large-field estimate of instanton strength (OPEN, no mechanism on disk).** HINT2_55 R2.4 (ARGUED): surviving
fine concentrations contribute L^{4(k−j)}P_j; Balaban-type e^{−c p(g_j)²} loses; sufficient (LF-inst) "P_j ≤ Ce^{−c_LF u_j} … with
c_LFβ₋ > 4". Needed by every OS-compatible witness (𝓔, 𝓑); Branch D's bounded block witness avoids it but is not in an E(4)-covariant
algebra (F1). **OPEN.**

**F18 — node A's only route is refuted pending Codex (OPEN, route change).** LCONV55 C5/G1/G3 (see N21). If Codex confirms, node A's
residual is the larger "one-step conditional positivity + inhomogeneous-coupling cluster expansion + (LC-3′)^tilt"; (CEM°)'s consumers are
unaffected in form. **OPEN.**

**F19 — flat-route TQ sufficient condition uses SRC-E (MISMATCH, consistency).** CODEX_REVIEW_TQ item 5: "T-E3's repaired RA and
SRC-E-supported RA-1 imply the sufficient decay". *Repair:* restate RA-1 with SRC-E′ (coarse-image moments). Bookkeeping + re-check.

**F21 — boxes (MISSING producer).** REVIEW_S22 "every non-wrapping box with the boundary convention of N5-sf0"; consumers: HIST
(I_k^E) and RLARGE local regions, SPHERE55's seam (mixed boundary conditions, Dimock II §2.5 as method), OFFGLOB55 T2. GV55 §3.3 item 3
"Boxes … not addressed"; CODEX_REVIEW_NSL item 4 "Do not bank … boxes". **OPEN.**

**F22 — FLOW's k̃-tower (MATCH-cond after restatement).** CODEX_REVIEW_FLOW55 item 2: "For N ≥ 3, the every-background version must use
the actual φ-tower; the literal k̃-based zero-minimum setting is REFUTED. Their trivial-point jets relevant to β agree." Restate FLOW
Def F-strip with φ; the coefficient core (C5a) is unaffected. Bookkeeping.

**F23 — a missed arrow (MATCH, new): UIR55's (TC-b)_𝔍 at orders 3, 4 is supplied by BFT34_55's Theorem BFT3-glob (E) at B = 0.**
Details in N16. With it, (UIR^♮) ⇐ (ρ-null) [ARGUED] + reading (R) [BFT4W55's premise; CODEX_REVIEW_BFT4W's "single most dangerous
unverified input"] + (GERM) + the T → ∞ limit of jets + the normalisation map to the stripped φ-tower. FLOW55 §9 and UIR55 §7 ask lane A
for a weighted N1-15 and a quartic analogue; that request is superseded by the existing BFT-3 E-part (conditional). **Arrow-level
claim only; nothing here is proved beyond reading the two statements together; the rate is m_0 < m/3 with m ≤ m_Y ≤ 1.666·10⁻⁴ (BFT34_55
"Rate"), astronomically small but positive and k-, T-uniform — only m_0 > 0 is used by Lemma FP.**

**F24 — SRC's decay node is not BFT-4's decoupling family (MISMATCH, object).** SRCAN55 §0/§7 (SESSION25 §RESUME quotes it): "SRC's
decay node is the same object as BFT-4's decoupling family … with the coupling as a spectator". BFT4W55's BBcc family is a polymer
representation of the CLASSICAL composite critical value; (D1) needs a polymer representation of the CONDITIONAL source-inserted generating
function, which contains the fluctuation integrals (N6). CODEX_REVIEW_SRCAN item 11: "Bond-parameter analyticity is useful only together
with a true decoupling/splitting identity, a sufficient complex radius, and bounds on the family … These are valid alternatives. 'Exactly
two ways' is not an established classification". *Repair:* state (D1) for the quantum conditional generating function (SRC-poly) with
BBcc as one input among N6 and the large-field cluster expansion. **OPEN (part of N10).**

**F25 — HANDOFF status wording (minor).** HANDOFF: "H_RP is exact for the Wilson action on the torus and on the sphere's equator
(banked)" — the torus statement is PROOF L9a (IMPORTED-AND-REVERIFIED, pre-S24), not in [S26-BANKED]; and on the sphere route the
banked RP is not the consumed one (F3). Wording only.

# §8. Remaining application inputs (the abstract REC producer and conditional EXT route are distinguished below)

| id | Leaf (exact statement needed) | Needed by | Nearest text on disk |
|---|---|---|---|
| ML1 | **(ALG)** one local algebra 𝒜 carrying: a determining family for OS0 (^0𝒮 Schwinger distributions of e_a), the E(4) action, a positive-half generating set for RP, and the non-freeness witness (or a theorem transferring non-freeness from 𝔈 to the e-field OS theory) | N1F, N1S, N5 | PANEL_P1 §1 demands it; HINT55 §1.2 defines 𝔈; SRCCD55 §3.2 picks {e_a} |
| ML2 | **(REC application)** the actual common YM hierarchy meeting N9's full E0′/E1/E2/E3/(Re)/S_0 contract, with the scalar or finite Cartesian tensor dictionary; actual growth and full-field identification remain OPEN | N1F/N1S and full reconstruction | ABSTRACT producer: REC_LIB + REC_CONT, reviewed by REVIEW2_REC; conditional growth: REC_LIB §16 / OSLEAF55 GROW; actual source bounds not supplied |
| ML3 | **(DIAG)** from per-R subsequential continuum limits and ω_R → ω_∞ on one countable family, a single lattice sequence (a_j(R_j), R_j) converging to ω_∞ | N1S + T_OS "arises as such a limit" | CODEX_REVIEW_P4 §4.3 ("safe order"); none |
| ML4 | **(FLOW-pos)** the coupling flow and its locality for slowly varying bare profiles, with two-sided propagation; W0: sup_x|c_4(a; x)| → 0 | sphere W0; SRC position-dependent sources | SPHERE55 §1.4, §3.4 T4; SRCAN55 SA-F (upper bound only, CODEX_REVIEW_SRCAN item 6) |
| ML5 | **(GERM)** at each fixed k, T (and formally in infinite volume) E^br_k, E^cb_k and E^min_k (φ-tower) are values of nondegenerate critical families through the trivial chain near 1, hence share all trivial-point jets | flow core (C5a), F23 | TOWER-VAR (d), NORMS Lemma N1-2 (D³ only) |
| ML6 | **(MIN-cb)** for real small-field data, every global minimiser of the chain energy lies modulo composite gauge in BFT-E's fixed slice ball, uniformly in k, T (and locally on Λ_k(𝔥)) | FLOW (SF-bg)/(SF-g), HIST (I_k^E)″, PLD 𝔟(V) | named in parts: HIST (a5-U), PROOF (MIN_1), both OPEN |
| ML7 | **n-point H_Euc inputs**: SRC-κ (κ-2) for all n; CD/SRC-O/SRC-W′ (flat) and W1/W3/N5 (sphere) for n-fold centred products | N4 (all routes) | none (every producer is "for the tested pair") |
| ML8 | **(U-sep)** radius-uniform separated-point ^0𝒮 bounds for the e-field on S^4_R near S, and the CODEX_REVIEW_P4 §4.1 contraction lemma re-proved in ^0𝒮 form | N1S | CODEX_REVIEW_P4 §4.1-4.2 (unit-ball moments only) |
| ML9 | **(EXT application)** actual uniform per-scale (X1), including linear growth in n and power-law separation dependence down to c_*a, or unconditional (SEP-pt) with the stated crude bound; fixed-separated control alone is insufficient | N2, N9 | Conditional extension/pointwise implications: OSLEAF55 EXT/GROW; REC_LIB §16 checks the pointwise growth match. Actual YM inputs remain OPEN; this correction does not re-certify the full EXT proof |
| ML10 | **(LOC-T)** bulk locality transfer: torus-proved conditional RG estimates hold in the bulk of K_a with constants independent of R | N13, F13 | SPHERE55 §5.4 "Why local (ARGUED)" |
| ML11 | **(BOX)** BFT-0..5 on non-wrapping boxes / local small-field regions with frozen exterior | REVIEW_S22, HIST, RLARGE, SPHERE55 seam | GV55 §3.3 item 3 "not addressed"; OFFGLOB55 T2 (in flight) |
| ML12 | **(TRAJ)** one written trajectory: F-tune's g_0(a; g_ref) at ℓ_ref = 1 for every torus input, with u_K − R > 0 (g_ref² < 1/R) stated, the soft-kernel level couplings fixed by FI-1, and the sphere profile rule declared to be (G-np) | N8 | FLOW Theorem F-tune; SRCCD55 §3.1; HINT2_55 R2.1; SPHERE55 §1.4 |
| ML13 | **(W-T0)** or **(W-e)**: an OS-compatible witness with its comparator theorem and its YM-side bounds | N5, ML1 | HINT2_55 R1.9 (comparator side for 𝓑 PROVEN for free fields; YM side ARGUED) |

# §9. The ordered list of OPEN leaves (the remaining work), with routes

Route tags: **[all]** every route; **[flat]** torus + TQ; **[sphere]** S^4_R; **[soft]/[hard]** scheme; **[𝓔]/[𝓑]/[Ψ]/[e]** witness choice
(4D-flowed bare density / time-zero 3D-flowed / hard block energy (Branch D) / e-field correlations). Order = dependency order (what must
exist before what consumes it). Status as on disk ≈04:15Z.

*Tier 0 — decisions (owner), which fix what the top means.*
1. **OWN-alg + OWN-free** [all]: the algebra and the meaning of "free" (F1, ML1). Coupled to the witness choice: [𝓔] fails the OS-quotient
   requirement unless OWN-free accepts (ID♮)-relative non-freeness of the Euclidean state; [Ψ] is bounded and level-local but needs the
   hard scheme (HINT2_55 R3.3; PLAN_S26 §11: CMP 98 "would need re-proving first") and is not E(4)-covariant; [𝓑] and [e] are OS-compatible.
2. **OWN-S4** [sphere]: S^4_R regularisations with a position-dependent profile count as "arising as such a limit".

*Tier 1 — the shared RG core (bottom-up).*
3. **Lane-A linear package re-verification** [all] (N24): every banked BFT item is conditional on it.
4. **Reading (R)** [all] (BFT4W55 Theorem H3's premise; CODEX_REVIEW_BFT4W "Single most dangerous unverified input"): per-density
   holomorphic estimates on local constraint sets. Feeds BFT-3 (H3)_μ, BFT-4 (a), and through F23 the flow.
5. **BFT off 𝒞_glob + boxes** [all] (F7, ML11; OFFGLOB55): (UHL)/(G♯-patch)/(SL-cov)/(LOC-GA), and **(MIN-cb)** (ML6) for the min-tower readers.
6. **BFT-5 at Z ≠ 1: an actual alignment** [all] (ALIGN55: Lemma RED's (P1), (P2-tw) + (NC), (NS), (HD), (FW), (AC)).
7. **BFT-4 (b)** [all, if consumed] (F8; BFT4B55 T0 first).
8. **Convention restatements** [all, bookkeeping]: Balaban's convention in SF (BG-unif) and the N5-unif chain (F11 C1/C2), S_E/orbit-norm
   restatement of BFT-5 consumers (F12), Convention C (F9), φ-tower (F22), E_pl (F16), ‖·‖_cf source class (F15).
9. **N5 at levels ≥ 1 at complex backgrounds ((NA-H_loc)) and N6** [all] (N22): needed by (SF-g)_k and by SRC (A).
10. **(ρ-null)** [all] (UIR55 §3.5′, ARGUED) and **(GERM)** (ML5): with item 4 and F23 these give (UIR^♮), hence (UNIV-1L), hence F-flow/F-tune.
11. **(SF-∞)** (stated hypothesis) and **(SF-cont)** (IMPORTED, CMP 109 as read by FLOW) [all]: the flow's volume uniformity and continuity.
12. **Constants** [all] (N23): the two-sided windows (TC), (K), complex width; FI-1's uniform inputs; the n_♯ → SC_k cutoff edge.

*Tier 2 — large fields.*
13. **The large-field architecture** [all] (N21; LARGE55): either RLARGE v3 with node A restated per LCONV55 G3 (one-step conditional
    positivity + inhomogeneous-coupling cluster expansion + (LC-3′)^tilt), (a5-U), (CLS-NA); or an action-based Balaban/Dimock split with
    coupling-dependent cuts. Outputs needed: (RLF-δ), SRC-I, SRC-κ-LF, (N5-RG)'s large-field part. [sphere]: SRC-I without chessboard.

*Tier 3 — correlation functions (H_reg).*
14. **SRC (A)** [all]: complex position-dependent-coupling stability of N5/N6/RLF, (Flow-an), TOWER-VAR^η, rooted summability; **SRC (B)**:
    real-tilt CD for the fixed-kernel chain (CODEX_REVIEW_SRCAN item 11); **SRC-poly/(D1)** for the quantum conditional generating function (F24).
15. **Pointwise or shrinking-radius envelopes** [all] (F10): (P1)/(LOC-e), or r_z(δ) = cδ^α envelopes; κ-3(e) singleton control.
16. **LF product moments** [all]: all-order uniform moments of products of conditional cumulants (CODEX_REVIEW_SRCCD §7's counterexample
    shows the stated Peierls hypothesis is insufficient; SA-MOM's envelope moments, CODEX_REVIEW_SRCAN item 12).
17. **SRC-M** [all]: the eight matching constants O(g_bare²) and O(a²𝔏) remainders (CODEX_REVIEW_SRCCD item 6: SRC-OW NOT-VERIFIED).
18. **Actual H_reg-sep and the REC application** [all] (ML9, ML2). Prove uniform (X1) and its EXT hypotheses, or
    unconditional all-order (SEP-pt) and the crude bound, on ONE common field hierarchy/sequence. The pointwise order is
    s=11 for Z=1, q_X=4, or s=max(11,ceil(q_X)+6) for q_X≥0; β=p+3 additionally needs the singleton-inclusive outer-cumulant
    bound. These are OPEN Yang–Mills estimates. Once E0′ and the remaining N9 axioms are obtained, the completed ABSTRACT
    REC_LIB + REC_CONT producer reconstructs that hierarchy. It supplies neither those estimates nor a physical mass gap.

*Tier 4 — Euclidean invariance (H_Euc), by route.*
19. **[all] n-point inputs** (ML7, F4).
20. **[flat] TQ** (N12; infrared; nothing on disk excludes its failure) + the CD/SRC-O/SRC-W′ derivation (N11) + RA-1 with SRC-E′ (F19).
21. **[sphere]** θ_μ RP Codex check (F3); (FLOW-pos)/W0 (ML4); W1, W3 (two-scale, renormalised, E10 quantifiers); N5 via N5-RG, N5-op,
    N5a/N5b (F13; SPHERE55 §6: "the single most likely point of failure of the IR-freeness claim" is N5b/N5-RG at large coarse fields);
    (LOC-T) (ML10); Lemma 3.5 without SRC-E and (U-sep) + ^0𝒮 contraction (F5, ML8); (DIAG) (ML3). Alternative mechanism: UNIV55
    Theorem U's comparison inputs (N14).

*Tier 5 — non-freeness (H_int).*
22. **(ALG) + an OS-compatible witness** [all] (ML1, ML13): [𝓑] needs OS0/OS1 for the time-zero family and sharp-time finiteness; [e]
    needs a new comparator theorem for :F²: two-point functions and an AF-decaying envelope (SRC-κ's 𝔤_α grows instead).
23. **(TS-up) with (LF-inst)** [𝓔, 𝓑] (F17), **(TS-low)**, **(MOM-E)** [all witnesses], **SRC for flowed bare observables** ((FLOW-BLK) or
    (SRC) at every level) [𝓔, 𝓑]; [Ψ] instead needs the hard-scheme H-Bal-1, H-sg, H-loc-LF (HINT2_55 R2.4 "Contrast").

**The single most dangerous OPEN leaf: item 23 together with item 22 — H_int on the OS algebra, i.e. (TS-up) with a large-field estimate of
instanton strength (LF-inst) for an OS-compatible witness.** Reasons, each from the files: (i) every route needs it (N1F, N1S); (ii) no
candidate witness on disk meets the top's three constraints at once — [𝓔] is not an OS invariant (HINT2_55 R1.10 (ii); CODEX_REVIEW_HINT2
F1: absolute non-freeness "still GAP"), [Ψ] leaves the E(4)-covariant algebra and the soft scheme, [𝓑]/[e] have no YM-side bounds;
(iii) for the OS-compatible flowed witnesses the YM-side bound needs (LF-inst) — "P_j ≤ Ce^{−c_LF u_j} … with c_LFβ₋ > 4", i.e.
dilute-instanton strength — while the lane's large-field technology is polylogarithmic (e^{−c p(g)²}) and HINT2_55 R2.4 shows its union
bound diverges against L^{4(k−j)} (the necessity of (LF-inst) itself is ARGUED, not proved); (iv) no file proposes a mechanism, and unlike
items 5-6 (Balaban's local-gauge patching) there is no precedent: Balaban's programme controls the partition function, not non-Gaussian
continuum correlations. **Most load-bearing analytic leaf (runner-up): item 5 (BFT off 𝒞_glob, F7)** — every arrow from the RG to SRC,
RLARGE, SF, HIST and N5-unif crosses it, and CODEX_REVIEW_BALX names its linear core ("a k- and volume-uniform inverse bound for the
actual nonabelian composite Hessian … at Z ≠ 1") as its most dangerous item.

# §10. Status update — the lead's 04:1xZ banking batch (read at 04:20Z, after §1-§9 were written; overrides the statuses it names)

PROOF.md [S26-BANKED] now also contains (located by string): "**Coupling flow: (UIR^♮) reduced further — CONFIRMED as a conditional
implication** (UIR55 + CODEX_REVIEW_UIR items 1-5)"; "**BFT-4 (a) on 𝒞_glob — CONFIRMED conditionally, with one named premise (R)**";
"**SRC via analyticity — scoped pieces CONFIRMED**"; "**Non-freeness witness — comparator mathematics CONFIRMED, the identification
bridge NOT**". Effects on the map:
- **N16 / F23.** CODEX_REVIEW_UIR item 4 banks "(common weighted tree jets at orders 2–4) + (actual ρ-null) ⇒ UIR" in infinite volume and
  says "Do not bank: actual cubic/quartic uniform tree locality, actual ρ-null, … finite-volume uniformity from a definition". It does not
  mention BFT-3. F23 is therefore still a new arrow, now between two banked items: BFT34_55 Theorem BFT3-glob (E) at B = 0 (banked
  conditionally on (H1), (H2)_m, (H3)_m), with (H3)_m ⇐ BFT4W55 Theorem H3 ⇐ (R) (banked conditionally on (R)), supplies the orders-3, 4
  tree-jet bounds on every torus T ≥ 3 uniformly in k and T, for the composite critical value. To reach UIR's hypothesis three short
  items remain: **(GERM)** (ML5), **(JET-∞)** the T → ∞ limit of T-uniformly exponentially decaying translation-invariant jet kernels
  (the direction UIR needs — torus to infinite volume — is the easy one, the opposite of the "finite-volume uniformity" Codex declines to
  bank), and the normalisation map from 𝔉_k's κφ̂ to the stripped φ-tower. **So the coupling flow's open content is (ρ-null) + (R) +
  (GERM) + (JET-∞), not "(ρ-null) + tree locality".** (R) is the same premise BFT-4 (a) and BFT-3's (H3) already carry, so it is one
  item, not a new one. Status of the arrow: MATCH (arrow-level; nothing proved beyond reading the two banked statements together).
- **N19.** BFT-4 (a): banked conditionally on (R). F7 (PD-glob vs curvature-adapted polydisc) and F8 (constant-gauge pieces) unchanged.
- **N10.** SRCAN pieces banked; the bank line names "tilted large-field envelopes (the most dangerous input, incl. large coarse fields)"
  as NOT-VERIFIED — the same object as my ordered item 16. F10/ML9 unchanged ("the full test space needs a uniform extension estimate").
- **N5 / F1.** The banked HINT2 line: "**above all (ID♮) as an observable-algebra / OS identification — its contraction does not preserve
  products, so it does not show the reconstructed theory is non-free.** H_int stays OPEN." This is F1 from the comparator side; F1's
  algebra-side statement (the witness and the OS fields live on different algebras) is independent of it and still stands. The corrected
  instanton coefficient "(4π²/N)u (restoring 11N/3)" fixes (LF-inst)'s currency; F17 unchanged.
- **Most dangerous leaf: unchanged** (§9: H_int on the OS algebra, items 22-23).

# §11. Summary table (every node, arrow and leaf of this map, with its verdict)

| # | Item | Status / verdict |
|---|---|---|
| N0 | T_OS | target; OWN-alg, OWN-free, OWN-S4 OPEN |
| N1F | flat assembly lemma | P1 PROVEN, re-derived here: CONFIRMED as an implication on one algebra; not in [S26-BANKED] |
| N1S | sphere assembly lemma | Codex-CONFIRMED conditional (P4 §4.1-4.3); iterated order; not banked |
| N2 | H_reg ← Prop E | Prop E NOT-VERIFIED (Codex); arrow MISMATCH F2a |
| N3 | H_RP | flat MATCH (L9a, pre-S24 ledger); sphere MISMATCH F3 |
| N4 | H_Euc | MISMATCH F4, F5, F6; flat needs TQ (OPEN, IR) |
| N5 | H_int ← H-RED♮ | MISMATCH F1; YM inputs OPEN; F17 |
| N6 | (ALG) | MISSING (ML1) |
| N7 | one sequence / (DIAG) | flat MATCH-cond (Lemma CONV); sphere (DIAG) OPEN |
| N8 | (TRAJ) | torus MATCH-cond (needs u_K − R > 0 stated); sphere MISMATCH F14 |
| N9 | (REC) | ABSTRACT producer reviewed (REC_LIB + REC_CONT); exact consumer contract stated; actual YM hierarchy/growth/application OPEN |
| N10 | SRC | OPEN; MISMATCH F4 (κ-2), F7, F10, F15, F24 |
| N11 | ROTDEF I5 inputs | MATCH-cond; derivations NOT-VERIFIED (Codex SRCCD item 5) |
| N12 | TQ | OPEN (IR, flat); F19 |
| N13 | sphere UV inputs | OPEN; MISMATCH F5, F13, F14 |
| N14 | universality (Theorem U) | OPEN inputs |
| N15 | (TS-up)/(TS-low)/(MOM-E) | OPEN; F17 |
| N16 | coupling flow | OPEN ((ρ-null), (R), (GERM), (JET-∞)); NEW MATCH F23; MISMATCH C5b; F22 bookkeeping |
| N17 | BFT-0/1/2 | banked on 𝒞_glob (+ID, conditional); MISMATCH F7, F21; F11 readers |
| N18 | BFT-3 | banked cond. on 𝒞_glob; MISMATCH F7 (RLARGE); MATCH F23; MATCH-cond (M4), (L-loc) |
| N19 | BFT-4 | (a) banked cond. on (R); MISMATCH F8, F7; F9 MATCH-cond |
| N20 | BFT-5 | Z = 1 banked; Z ≠ 1 OPEN (ALIGN55); MISMATCH F12 |
| N21 | large fields | OPEN; F18 (node A route refuted, pending Codex) |
| N22 | N5 levels ≥ 1, N6 | OPEN |
| N23 | constants | OPEN windows; acyclicity banked |
| N24 | lane-A package | inherited; NOT-VERIFIED at S26 standard |
| C1 | SF (BG-unif)/A1.k reads E^br | MISMATCH (restate in Balaban's convention) |
| C2 | N5-unif chain reads E^br ((H-C⁺), (H-ℂ)) | MISMATCH (same repair) |
| C3 | SMALLNESS_DAG C_flat_i | off-route |
| C4 | level-1 BR1 readers | MATCH-cond on 𝒞_glob(ε_E1) via E1 |
| C5a | flow jets at 1 | MATCH-cond on (GERM) |
| C5b | min-tower on uniform domains (FLOW (SF-bg)/(SF-g), HIST (I_k^E)″, PLD 𝔟(V)) | MISMATCH; (MIN-cb) or critical-value restatement |
| C6 | producers printing E_k^br | MATCH once Balaban's convention is written into BFT-0/4 |
| C7 | (N-bg)/(H-C) files | off-route |
| F1-F25 | arrow findings | MISMATCH: F1, F2a, F3, F4, F5, F6, F7, F8, F10, F12, F13, F14, F15, F19, F24 (+C1, C2, C5b); MATCH-cond: F9, F16, F22; MATCH (new): F23; missing producer: F21; wording: F25; OPEN: F17, F18 |
| ML1-ML13 | remaining application inputs | OPEN; ML2 now means actual YM application of the available abstract REC producer, and ML9 the actual extension/growth inputs |

**Historical counts (the original assembly pass; no new global certification).** Nodes: 25 (N0-N24, with N1 split). Arrow verdicts: **18 MISMATCH** (F1, F2a, F3, F4, F5, F6, F7, F8, F10, F12, F13, F14, F15, F19,
F24, C1, C2, C5b), **11 MATCH-cond** (N7-flat, N8-torus, N11, N18-(M4), N18-(L-loc), F9, F16, F22, C4, C5a, N3-sphere-after-Codex is not
counted), **3 MATCH** (N3-flat, F23, C6). Original leaf IDs: 13. Ordered items: 23 (§9); N9/ML2 and item 18 now distinguish
available abstract reconstruction from missing application inputs. Inherited claims refuted here: none of a banked
item; flagged against unbanked text: SPHERE55's SRC-E/(U-mom) (F5; the degree-1 case follows from banked Lemma V + Codex SRCCD item 3
transplanted to K_a — my reading, NOT-VERIFIED; the degree-2 case ARGUED), SPHERE55 §1.5 vs §5.2 internal inconsistency (F3), UIR55/FLOW55's
"order 4: nothing" (superseded by F23), SRCAN55's "same object" (F24, agreeing with CODEX_REVIEW_SRCAN item 11), HANDOFF's torus-RP
"(banked)" (F25).

# §12. Codex verdicts used — agree or disagree (each read as on disk at the time stated in §2/§10)

| Codex file, item | Used for | Mine |
|---|---|---|
| NSL items 1-4 and "single most dangerous remaining unverified identification" | §1, N17 | **agree**; §1 shows which consumers actually need that identification (C1, C2) and adds a third object (E^min, C5b) |
| SRCCD items 2-5, 7 and §7 (Prop E's three gaps; the Peierls path-moment counterexample) | N2, N10, F2a, F5 | **agree**; I re-did the counterexample arithmetic by hand: 80(4·(1/1024) + 1/12800) = 80·51/12800 = 51/160 < 1, and (1/1024)^ℓ(2^ℓ)^{11} = 2^ℓ |
| SRCAN items 1, 3, 4, 6, 8-12 | N8, N10, F10, F15, F24, ML9 | **agree**; item 10's re-diagnosis (uniform extension estimate, not an analyticity obstruction) is adopted in F10/ML9 |
| P4 §1.1, §4.1-§4.3 | N1S, F3, F6, ML3, ML8 | **agree**; §4.1's unit-ball moment hypothesis must be replaced by a ^0𝒮 form for point composites (F5/ML8) — a scope remark, not a disagreement |
| UNIV §9 (AF envelope, p > 2), items 4, 9, §11 judgment | N4, N8, N14 | **agree**; checked that (F_R)'s lower half gives the envelope iff u_K − R > 0 |
| TQ items 1, 5, 8 | N4, N12, F19 | **agree**; F19 only notes that item 5's RA-1 is "SRC-E-supported" |
| ROTDEF item 4 | N4, F4 | **agree** |
| FLOW55 items 2, 4; UIR items 1-5 and "Do not bank" | N16, F22, F23 | **agree**; F23 adds an arrow neither review drew (BFT3-glob (E) supplies the orders-3, 4 tree locality conditionally) |
| BFT34 item 1 | F23, N18 | **agree** |
| BFT4W items 1-3, 5 and "(R)" | N19, F8, F9, F23 | **agree** |
| GV items 4, 6; KOFF item 5 | N17 | **agree** |
| HINT items 1-5; HINT2 F1, F9 and its bankable section | N5, F1 | **agree**; F1's algebra-side mismatch is a separate, compatible statement |
| GSHARP (GF-DEP) | F12 | **agree** |
| DAG, RLU items 1-2, BALX (most dangerous linear core) | N21, N23, §9 runner-up | **agree** |
No Codex verdict used here is disputed.

# §13. What should change in PROOF.md's tally / HANDOFF's critical path (the lead edits; nothing here is banked)

1. **Tally: no change** (every result here is an arrow verdict or a missing-leaf statement, not a theorem).
2. **HANDOFF's open-inputs table lacks rows** for: (ALG) + an OS-compatible witness (ML1, ML13); n-point H_Euc inputs incl. SRC-κ (κ-2) for
   all n (ML7); actual REC application inputs (ML2; abstract producer available); actual EXT/growth inputs (ML9); (DIAG) (ML3); (TRAJ)/(FLOW-pos) (ML12, ML4); (GERM)/(MIN-cb) (ML5, ML6); boxes (ML11); θ_μ RP on
   K_a (F3).
3. **H_int row**: "free comparator banked for a narrower class; Yang–Mills side open" should add "and the witness is not on the OS algebra
   (F1): needs OWN-free or an OS-compatible witness ([𝓑] or [e])".
4. **Coupling-flow row**: "(UIR^♮) ⇐ (ρ-null) + (R) + (GERM) + (JET-∞)" via F23 (BFT3-glob (E) at B = 0), replacing "tree locality OPEN".
5. **Sphere row**: the banked equatorial RP is not on SPHERE55's flat-limit path (θ_μ RP needs a Codex check); SRC-E and (U-mom) must be
   replaced (F5: Lemma 3.5 with ‖E[F|W_s] − EF‖_2; (U-sep) + a ^0𝒮 contraction lemma); every RG input must be re-proved on K_a (F13)
   with a position-dependent flow (F14).
6. **HANDOFF "H_RP … torus … (banked)"**: L9a is IMPORTED-AND-REVERIFIED (pre-S24), not in [S26-BANKED] (F25).
7. **BFT-0 identification row**: write Balaban's convention into BFT-0/BFT-4; restate SF (BG-unif) and the N5-unif chain in it (C1, C2);
   add (MIN-cb) for the min-tower readers FLOW (SF-bg)/(SF-g), HIST (I_k^E)″, PLD 𝔟(V) (C5b).
8. **Node A row**: LCONV55 (pending Codex) refutes multiscale convexity; the residual becomes G3's larger statement (F18).
9. **PANEL_P1's H_reg wording** ("Joint observable moments") should read "separated Schwinger distributions in ^0𝒮" (F2a).

# §14. Errata to this file (append-only; each overrides the text it names)
- **E1 (§11 "Counts").** MATCH-cond count is **10**, not 11: N7-flat, N8-torus, N11, N18-(M4), N18-(L-loc), F9, F16, F22, C4, C5a. The
  parenthetical "N3-sphere-after-Codex is not counted" is void.
- **E2 (§7 F23, symbols; systemic defect 1).** In "m_0 < m/3", m_0 is UIR55's jet-class parameter in 𝔍(m_0, C_J, c_E) (weight
  e^{m_0·diam}, FLOW55 "|||T|||_m := sup_{b_1}Σ|T|e^{m·diam(b_1..b_r)}") and m is BFT34_55's weight of (H2)_m; neither is REVIEW_S22's BFT-3
  rate m_0 nor SRC's m_c. The bound uses diam ≤ 𝔱 (minimal spanning-tree length) and polynomial tree entropy in d = 4, so any
  0 < m_0 < m/(n − 1) works at order n; m/3 covers n ≤ 4.
- **E3 (§4 N4, §7 F4).** "TQ item 1" is CODEX_REVIEW_TQ "Exactly what may be banked" item 1; "ROTDEF item 4" is CODEX_REVIEW_ROTDEF's item 4.
- **E4 (scope of my own checking).** I re-derived only: N1F's closure step; the (F_R) → envelope algebra (N8); the Codex SRCCD counterexample
  arithmetic; the Lemma 3.5 replacement inequality (F5); the row-sum summability in F23/E2. Everything else in this file is a comparison of
  statements located by string, not a re-proof. No numeric script was run (no checks/as55_* files): every verdict here is a quantifier or
  object comparison, and the one arithmetic item is two lines done by hand above.

Completed: 2026-10-29 (UTC time of the last append is printed by the shell command that wrote it).
Completed (UTC, from date -u just before this line): 2026-10-29T04:22:29Z
- **E5 (§9 route tags, appended after the completion line).** A fifth witness option was omitted from the tags: the SOFT block witness
  with (NOISE-ADD) and a lower noise comparison (ANTI-♭) (HINT2_55 R3.1: "(NOISE-ADD): survives as an input, only where HINT55 used it";
  R3.2: "(ANTI-♭): survives as an OPEN input; its route (β) does not survive"). It shares [Ψ]'s algebra problem (block observables are
  not an E(4)-covariant family, F1) and adds (ANTI-♭). No verdict elsewhere changes.
