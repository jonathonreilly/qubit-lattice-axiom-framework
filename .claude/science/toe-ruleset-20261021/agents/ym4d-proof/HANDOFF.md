# YM4D proof push: handoff (rewritten after session 24, 2026-10-28)

*Supersedes the 2026-10-28 pre-session-24 handoff entirely. Everything the old handoff said was in flight
has now either landed or been withdrawn; read this file instead of it.*

## Goal
- Constructive UV stability (layer 1) and existence (layer 2: OS axioms, non-triviality) of 4D lattice
  SU(N) Yang-Mills.
- Method: a soft gauge-covariant RG with S4′ averaging ("decision 4": soft, not Balaban's hard
  delta-constraint).
- **Credit Balaban (CMP series 1983-1989; CMP 109:249-301 (1987) read directly) and Dimock in every public
  text.** Imports are allowed but must be re-verified on our own structures.
- **Nothing has been posted or landed, and nothing should be.** No statement in this repository claims 4D
  Yang-Mills existence or a mass gap.

## Read these, in this order
1. **This file.**
2. **SESSION24_RESULTS.md** — the lead's ledger of all eleven session-24 worker reports, with every finding
   and every reversal. It is the fastest way to the current state.
3. **RTARGET.md §51-§52** — session 24's pre-stated targets and the honest scoring, including three
   corrections to the lead.
4. **INTEGRATION_AUDIT.md** — whether the named target suffices for its consumers (it does not yet; two
   named additions).
5. **PROOF.md's session-24 header and [S24]** — the four binding corrections to this ledger and the
   critical-path summary.
6. Then the lane file and the latest REVIEW_* for whichever lane you are taking.

## THE REVIEW DEBT IS PAID
All five reviews the old handoff asked for are written: **REVIEW_HW_S5, REVIEW_PLD_S5, REVIEW_SQ_S4,
REVIEW_BFT_A_S8, REVIEW_FLOW_S13.** No headline was refuted outright; three were narrowed, one session's
reported verdicts were reversed three times, one framing was relabelled, and REVIEW_BFT_A_S8 supplied a
proof its session lacked.

**UNREVIEWED, and these are the next reviews to run:** HW session 6, PLD session 6, BFT_B sessions 9 and 10,
NORMS.md, NQ_CHECK.md, CONST_T.md, STAR_CONST.md. Every one is from session 24 and none has been audited.
Given this project's record — sixteen reversals historically, five more today — **treat all of them as
provisional until reviewed.**

## WITHDRAWN: things the old handoff told you to do that you must NOT do
1. **"Lower g_0 and recheck the SF thresholds."** WITHDRAWN, independently by two lanes. The smallness
   condition is **satisfiable** (REVIEW_HW_S5 traced the g-dependence: ε₁ sits at a g-free ceiling, H5
   *relaxes* as g → 0, b_n/b_D/c_att are pure geometry), and **the breach does not bind**: the binding
   ceiling is g_0² ≲ 2.5e-152/C_Ω, with slack ×3.59e56. There is no constants crisis.
2. ~~Repairing the per-level induction, in any norm.~~ **THIS INSTRUCTION IS WITHDRAWN by
   REVIEW_NORMS_S1 (binding fix 1), which was addressed to the lead for exactly this reason.** NORMS.md
   §N5's per-level **no-go is NOT ESTABLISHED**: "scale-covariant norm family" is used three times and never
   defined (and as used it **excludes 𝔐's own Hölder leg**); part (i) is true but **vacuous** (it is the
   l = k anchoring identity, which the file itself calls "the same number organised differently" at
   l.178-182); **check n1-D is a tautology** — its code computes k·eA + k·((d-4) - eA) after discarding the
   only derived quantity (`# placeholder, replaced below`) and returns d - 4 whether eA is 10⁶ or 1/3, so
   "the weight-invariance half is PROVEN" has **no computational support**; part (ii) bounds an estimate
   from above **with no lower-bound input**, the standard this ledger itself applies at PROOF.md l.6550;
   and the pre-registered outcome **(O3) was never tested**, although c38 C is literally (O3)'s signature.
   **The per-level route is therefore OPEN, not refuted, and a future session may attack it.** The
   composite route remains the better-supported one (Theorem N1-15 is CONFIRMED), but that is a judgement,
   not a theorem. *Lead's error: the previous version of this file stated the no-go as settled and told the
   next worker not to relitigate it — a no-go was given less scrutiny than a positive theorem, which is
   exactly what this project's standing rule forbids.*
3. **Pricing (CO-fun) and the (GE-T) refutation as two items.** BFT_B §36.5: they are the same functional.
4. **Treating (CO-0), (CO-up) or (SB) as open.** The first two are lane A's CONFIRMED Theorems W0 and GU;
   Theorem CO-B removes the third.
5. **The thin-cluster escape for (J-NS^cd)** (dead by computation) and **any finite funnel truncation** for
   the (PW-i) spikes (every one leaves a level-independent remainder, REVIEW_BFT_A_S8's dichotomy).

## The critical path now, in priority order

**1. T-UNIFORMITY, not (N-loc).** NLOC.md's **Lemma NL-1** (the torus Hodge bound, PROVEN) with **Theorem
NQ-1** gives **Theorem NL-3′** and hence **Corollary NL-4: Theorem N1-15 is UNCONDITIONAL at d = 4, trivial
background, linearised, at FIXED coarse side T ≥ T₀, with no (N-loc) at all** — confirming REVIEW_NORMS_S1's
RN1-20. **So (N-loc) is bypassed, and what is actually open is uniformity in T, which layer 2 needs** and
which "had never been written down" as the content of the open half. Price at fixed T: T^d ≈ 2.8e28.
- **Cheapest win in the lane (ARGUED, commissioned as GREENT.md):** the **Coulomb representative**'s
  |x|^{-d} tail (= LINEAR_PACKAGE Prop 3.7's Π_ex) gives **log T instead of T^d — 10²⁸ → ≈ 16** — and needs
  only a classical lattice Green's-function bound. **A log T is still not T-uniformity; say so.**
- **(N-loc-cell)** is the reduced fine half: **a finite list of cell-flux divisibility conditions on the
  already-proven symbol**, i.e. **(CL-1)'s open half in scalar form rather than a construction to invent.**
  Its leading condition is PROVEN.
- **Dead routes, PROVEN dead:** global axial gauge (fails by a factor T, Dirac string); within-cell axial
  gauge (meets the ℓ¹ budget, **fails the sup budget by L^k** — NORMS's near/far trade, carried out, fails);
  and **gluing via Theorem RW** — N5-sf0's gluing works because R_g is block-diagonal orthogonal and the
  object is an *operator*, whereas **a potential shifts affinely, so RW has nothing to conjugate.**
  *The lead briefed Combes-Thomas on box compressions as the likely quick route; it is not the relevant
  question.*
- **Do NOT claim (H-C)'s C_♭ clause from any of this.** N1-15 bounds D³E_k^br(1); **(H-C) names the
  Lipschitz constant on the class.** **(N-bg) is untouched and is the larger wall**, and NQ-1 provably does
  not cross it (abelian/linearised; the slice identity has no nonabelian analogue).

**2. The nontrivial background: (N1) + (CovLift)'s non-residual g_Z at θ > 0.** Now the biggest BFT
obstruction, because **every lane-A input (W0, GU, CO-0R, CO-upR, CO-B, LIN0) is proven at the trivial
background only.** Paper-scale.

**3. (CEM-1) and (CEM-2), plus the level-0 clause (0a)/(0b).** The whole HW/node-A chain reduces to these.
**(CEM-2)** is a decoupling across one R-free ring and is **not obtainable from the buffer-good event
alone** — the event bounds curvature by ε₁ where a g-independent constant needs ≈ g_K, a gap of 4.489e15 —
so **the mechanism must be the weight's typicality, not the event** (both REVIEW_HW_S5 and PLD §18 point
this way). **(CEM-1)** = (LCR) + the main-term reduction off G_Q + u-uniformity, three named single-level
statements. The level-0 clause is OPEN on both sides and is the largest residual after the moment.

**4. (CONST-T): expand C_1 and C_V in the energy inequality's steps (2)-(4)** (SQ.md l.1471-1487).
CONST_T.md has everything after (★) in closed form; **at q = 8, C_T ≥ 1.27e14, provably over the 1e13 the
(CLS-min) → RLARGE interface needs; at q ≈ 30 it is under**, with compatibility checked clause by clause
(q > 4; scale-invariance exact for every q; EPS-0b-avg with ~25 decades of headroom; and C_T′ falls
22.63 → 16·C_T so the ceiling itself rises to ~1.7e13). **q = 8 is the worst admissible choice** (the Moser
absorption exponent is a = q/(q-4), so a = 2 squares the one-step constant, costing 3.5e7). STAR_CONST.md
was commissioned for exactly this; if it has landed, read it.

**5. The level-count factor k, which is UPSTREAM of (TENT-Q), (NEUT-box) and (Y-sup^loc).**
REVIEW_BFT_B_S9_S10 refutes **Corollary COF-crit (§35.6)**: it substitutes a per-level row bound for Theorem
COF's ‖j‖_Pc = max_l L^{θ(k-l)}π_l(j_l), which differ by L^{θ(k-1)}, so **Theorem NCE (i) is NOT k-uniform**
and the sharper route leaves **≈ 25(k-1)**. Three independent records agree (lane A's [RBA2-fix] B3,
REVIEW_BFT_A_S8's S8-13, and **§36.5 (iv) contradicting §36.5 (i)**). The missing input is lane A's
**(SPD)/(W2)**, OPEN. **All three of (TENT-Q), (NEUT-box) and (Y-sup^loc) could be granted and still leave
≈ 25(k-1)** — so attack the factor k first. *An earlier version of this file banked the k,T-uniform form;
that was the lead's error.*
Below it: the compensation charge ⟨χ⁵_X D(S)⟩ ((TENT-Q)/(NEUT-box)), one scalar per level-k box; and
**(Y-sup^loc)**, whose reduction from (GT-sup) the review marks **NOT-VERIFIED** (it demands
max_own|Y^p_0| ≲ 1/n near p, contradicted by the |z|^{-3} profile behind 𝒩(Y^p) ≍ n), so **(GT-sup) may be a
spike-support question after all.**

**6. FLOW: (T-a1-M) and (T-b) are ONE wall** (the fine background-dependent inverse H_⊥(U)^{-1}), and
**(T-c)** (plane-wave ↔ constant-Cartan-flux exchange) decides whether §104-§107 reaches the target at all.

**7. (BB-mix), proposed as BFT-6.** OPEN, and the single gate on layer 2's entire cluster expansion.

**8. (MS-Sob) and (SQ-dev) are BACK ON THE CRITICAL PATH — this list did not name them.** TAUFLAT.md
adjudicated EPSSTAR §6.6 to **CONFIRMED**: τ_♭ is a min whose two entries **both bind**, the joint window is
**C_D ≤ 455.28** exactly against a current C_D = 4.76e15, and the **DESC-ε (iii)** clause fails by **9.707
decades of energy / 4.854 of ε_1**. Because SQ §16 records that **DESC-ε's hypothesis (REG-min) is
DISCHARGED while AE-red's (MS-Sob) is OPEN**, DESC-ε was **the only route to AE-red's size clause free of an
open hypothesis** — so its failure is a **status regression**, not the loss of a convenience. **SQ §0.5's
"all five are discharged by DESC-ε" dies for 3 of 5 consumers** (HIST A5 (A), HIST (I_k^E)′ (a4), SF.md),
and **(MS-Sob)/(SQ-dev) return to the critical path.**
*Survives, so do not over-read this:* (CLS-min) to HW TE (ii) and RLARGE branch (iii) (margin ×1.99);
RLARGE's a_bad; **A5 via AE-red, which clears by 63.00 decades**; DESC-ε (i)/(ii); RED-0; EPS-T/EPS-0/
(REG-min); and **layer 2 is unchanged**, since the existence lane already records (AE) OPEN and contains
**zero** occurrences of DESC-ε or (REG-min).
*Cheapest repairs, priced by TAUFLAT:* **(C) lower ε_1 by 4.854 decades to ≤ 9.38e-45 — zero new
mathematics, OWNER-GATED and now under audit (EPS1_SWEEP.md), because nobody has swept the ε_1 consumers and
lowering it enlarges the large-field region. (D) prove (MS-Sob)**, which restores all three consumers at
once and is already the route of record. **(A) sharpening C_T is DEAD** (0.080 decades of room against 4.854
needed); **(B)** sharpening C_err's prefactor lands ≈1.7 decades short; **(F)** a weaker DESC-ε is **not
available** — the quadratic τ_♭ dependence *is* the descent mechanism.

## Two target restatements to make before proving anything about BFT-1
- **BFT-1 needs a WEIGHT PAIR** (curvature θ_w^c = 2, residual θ_w^r = d - 1 = 3). With a single common θ_w
  there is **no solution in (0, 2] for any consumer**. Note θ_w^c = 2 is the **maximal** curvature weight: a
  weaker BFT-1 is not a safer one.
- **Promote (BB-mix) to BFT-6.**

## Two cross-lane disagreements left open on purpose
1. ~~The price of node A's extra R-free ring (×17 against ×82).~~ **SETTLED by PLD session 7 (p7 F1), and
   the lead's steer was wrong.** Both lanes were right about different columns: **×17 is correct for the
   OPEN column** (level-k BUF), **×82 for the CLOSED column** (level-(k-1) BUF) — **and the closed column is
   the application the proof actually makes**, so **§18.4's ×82 stands** and **HW §41 item 4 is reversed**.
   1 + 3⁴ = 82 against 1 + 2⁴ = 17, ratio exactly 81/16. *The earlier version of this file called HW's the
   better-supported figure because Lemma RING carried a proof and a check; it did, for a column the proof
   does not use. A proof of the wrong statement is not better support.*
2. **TF-2:** HW recorded both positions and did not propagate. Node A says PLD §17.2's law already carries
   the finer spectators, and HW session 6 agrees. A reviewer should close it.

## One PROOF-owned constant conflict
PLD §16.8's λ_min = 3.17e-3 against REVIEW_PLD_S3's binding L0-1 (6.6e-10). **If L0-1 governs, a_ret falls
×4.80e6.** Route (ii) defuses it. For SF/PROOF to settle.

## Process rules (binding, unchanged — and three were breached in session 23/24, so read them)
- **Hostile review after every session**, written to REVIEW_<LANE>_S<n>.md by a reviewer that did not write
  the session.
- **PRE-STATED first.** The first edit of a session holds statements only; log its byte size in the *_LOG.md.
- **Criteria before scripts, and a criteria file may contain NO constant derived in the same session.**
  HW session 5 breached this (b_n, b_D, c_att in the w5 criteria). SQ's q5 criteria and FLOW's B4 criteria
  were themselves wrong — FLOW's fixed a FAIL at pre-registration. **Check your own criteria against this.**
- **A "FOR OTHER FILES" section** whenever you raise a demand on another lane. HW.md lacked one through
  session 5; §41 repairs it.
- **Numerics.** Take the lock with `until mkdir <scratch>/locks/numeric; do sleep 20; done`, run, `rmdir`
  exactly once. Never pkill. nice 10, one thread. Under 20 min and under 1 GB — **FLOW session 13 breached
  the 1 GB cap at 1.03 GB and it was consequential**, forcing the torus substitution that weakened its
  evidence. One numeric job machine-wide. Exact rational/symbolic arithmetic in plain python needs no lock.
- **Statuses.** PROVEN / ARGUED / CONDITIONAL (name the input) / GAP / OPEN, honestly. A failed check is
  reported as a fail, output and script kept unaltered, re-runs under a new id with criteria untouched, and
  any post-hoc probe labelled post-hoc. Session 24's workers did this well — four disclosed FAILs, none
  dressed up — and that is the standard.
- **Never edit the axioms. No Sci-Hub/LibGen. Pay for nothing.**
- **Landing (only once the full proof is complete and reviewed):** one PR landed by an independent
  review-loop agent; then draft the HN / OpenAI-thread text for the owner to approve word for word.
  **This condition is not met and is not close to being met.**

## The honest distance to finish
PROOF.md [S16] records REVIEW_S15_CONVERGENCE's finding that **the flat "24 OPEN" is a counting artefact**
and that the weighted critical-path DAG is the honest measure. The count has now been flat for sessions
15-24 while substantial mathematics was added — including today.

**LINEAR_PACKAGE.md §10 (frozen 2026-10-27) gives layer 1 as about 6-7 PAPER-SCALE tasks and 15-18
session-scale tasks**, paper-scale meaning "about one Balaban-sized paper", with the analogous CMP papers
named: background fields for SU(N) [cf. CMP 102, parts of 99]; propagator bounds at a general background
[cf. CMP 95, 96, 99]; localisation and polymer bounds for one soft RG step [cf. CMP 116]; the coupling flow
over all scales [cf. CMP 109 Thm 2, CMP 119]; large-field renormalisation [P×2; cf. CMP 122 I and II];
assembly [cf. CMP 119]. **Layer 2 is additionally at 9 HYPOTHESIS-NEW and 12 OPEN** (EXISTENCE §21.5) and is
paused on the layer-1 outputs in its §21.3 consumer list.

**Read that as the real answer to "how far".** It is several Balaban-sized papers, not several sessions.
What is genuinely in reach as a deliverable is the frozen linear package plus the conditional existence
architecture — "if layer 1 delivers X, then the OS axioms and non-triviality follow" — which is a theorem
about the reduction and is valuable whether or not X is ever proven.

## The pattern worth carrying forward
Across all eleven session-24 worker reports, **the mathematics was largely sound and the orders of magnitude
were hiding in quantifiers, currencies and incidentally-fixed parameters**: q = 8 (worst admissible, cost
3.5e7), a single θ_w where a pair was needed, a ×6561 shadow constant that was really ×81, the (E1)/(E2)
quantifier mismatch, and an allowance currency that two lanes had each denominated differently. **Before
attacking an estimate, check what someone fixed once and nobody revisited.**
