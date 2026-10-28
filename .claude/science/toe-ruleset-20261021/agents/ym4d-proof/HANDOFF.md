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
2. **Repairing the per-level induction, in any norm.** NORMS.md §N5 proves it is a **no-go**: the d = 4
   cubic vertex is marginal, so A ≥ 1 in every scale-covariant norm, and the weight-invariance half is
   proven — any A < 1 bought with non-canonical weights is cancelled exactly by the initial-condition
   mismatch. [S22]'s cures (W1)/(W2) cannot help there. **Use the composite route.**
3. **Pricing (CO-fun) and the (GE-T) refutation as two items.** BFT_B §36.5: they are the same functional.
4. **Treating (CO-0), (CO-up) or (SB) as open.** The first two are lane A's CONFIRMED Theorems W0 and GU;
   Theorem CO-B removes the third.
5. **The thin-cluster escape for (J-NS^cd)** (dead by computation) and **any finite funnel truncation** for
   the (PW-i) spikes (every one leaves a level-independent remainder, REVIEW_BFT_A_S8's dichotomy).

## The critical path now, in priority order

**1. (N-loc) — the single named input of a proven contraction.** NORMS.md Theorem N1-15 gives
**A_soft = 1/L = 1/3 uniformly in k** for the composite third derivative, and after NQ_CHECK.md's **Theorem
NQ-1 ((N-Q) PROVEN, 𝔮_0 = 11/3)** it is **conditional on (N-loc) alone**. (N-loc) is the exponential
locality of the gauge-variant representative, i.e. **the multi-scale axial gauge already named as (CL-1)'s
open half.** Closing it discharges (H-C)'s C_♭ clause at the trivial background and gives an **alternative
to BFT-4** that avoids (CovLift), (Mult-Y), (Pair-loc) and (I-id) entirely. *Highest value in the project.*
Scope warning: NQ-1 is abelian/linearised, exactly Setting SC's scope, and does nothing for **(N-bg)**,
which is what BR1 and δ_Sch actually consume.

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

**5. (TENT-Q) / (NEUT-box): one scalar per level-k box.** Off the critical set, the entire remaining
obstruction to (NC-Γ) for Γ_E is the compensation charge ⟨χ⁵_X D(S)⟩. **(Y-sup^loc)** — the other factor —
is a **lane-A linear-package item** now, not lane B's.

**6. FLOW: (T-a1-M) and (T-b) are ONE wall** (the fine background-dependent inverse H_⊥(U)^{-1}), and
**(T-c)** (plane-wave ↔ constant-Cartan-flux exchange) decides whether §104-§107 reaches the target at all.

**7. (BB-mix), proposed as BFT-6.** OPEN, and the single gate on layer 2's entire cluster expansion.

## Two target restatements to make before proving anything about BFT-1
- **BFT-1 needs a WEIGHT PAIR** (curvature θ_w^c = 2, residual θ_w^r = d - 1 = 3). With a single common θ_w
  there is **no solution in (0, 2] for any consumer**. Note θ_w^c = 2 is the **maximal** curvature weight: a
  weaker BFT-1 is not a safer one.
- **Promote (BB-mix) to BFT-6.**

## Two cross-lane disagreements left open on purpose
1. **The price of node A's extra R-free ring:** HW's Lemma RING says **×17** (with a proof and check w6 G6);
   PLD says **×82**. HW's is the better-supported figure; a reviewer should settle it.
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
