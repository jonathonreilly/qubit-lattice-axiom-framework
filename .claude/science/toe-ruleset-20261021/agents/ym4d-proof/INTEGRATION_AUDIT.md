# Integration audit: does the named target serve its consumers? (lead, session 24, 2026-10-28)

**Owner: lead.** This file is written by the integration lead, not by a lane. It judges no lane's mathematics.
It asks one question only: **if every clause of the single named target BFT were PROVEN tomorrow, would the
chain close?** The answer is no, and this file names the shortfall precisely so that it can be assigned.

Nothing here is counted in PROOF.md's tally.

## 1. The target as stated

BFT is stated in REVIEW_S22.md l.389-432 (quoted in PROOF.md [S23]). Clauses BFT-0 (existence, uniqueness,
identification), BFT-1 (scale-weighted regularity), BFT-2 (analyticity), BFT-3 (locality, orders n <= 4),
BFT-4 (branch-action class), BFT-5 (linear stability at the background). Its constants
(eps_0, r_C, theta_w, m_0, C_0, T_0) depend only on (N, L, kappa_+-), and theta_w is quantified
**existentially**: "there exist ... theta_w in (0, 2]".

## 2. Consumer-by-consumer audit

| Consumer | What it needs | Served by BFT as stated? | Shortfall |
|---|---|---|---|
| PROOF / N5 | BFT-0, BFT-1 at theta_w = 0, BFT-2, BFT-4 | **YES** | — |
| SF | BFT-1 (theta_w > 0), BFT-2, BFT-5 | **YES** (existential theta_w in (0,2] implies theta_w > 0) | — |
| FLOW | BFT-2, BFT-3 at z = 0, V_k = 1, orders <= 4 | **YES** | — |
| RLARGE | BFT-3 (R_bg, load-bearing under v2); BFT-1 one-step (C_I, not load-bearing) | **YES** | — |
| SQ | the cone-local analogue of BFT-1 for **minimisers** ((REG-min)); plus theta_w > 1 **as a stated value**; plus a cone-box uniqueness / eps-regularity clause with **free boundary** | **NO, three ways** | **A1, A2, A3 below** |
| EXISTENCE, (L-loc)_k | all-order mixed-derivative decay | **NO** as BFT-3 (orders <= 4); re-pointed by REVIEW_X12 fix 3 to BFT-4's **(BB-mix)** with per-cube smallness | **A4 below** |
| EXISTENCE, (c3-nz) level-uniform | cubic Taylor data of E_k^br at V = 1, k-uniform | BFT-3 at n = 3 is OPEN; REVIEW_X12 fix 9 puts it inside BFT-4 | covered by A4 |
| EXISTENCE, (BG-reg) | |B_D(V)|^2 <= c_B L^{-4n} Q_w(V) | BFT-1 + BFT-3 at n = 1; REVIEW_X12 fix 4: BB-3_1 (k = 1) PROVEN, general k <= (H-G_w) OPEN, BFT-1 only on C_glob as an implication | scope item, not a target defect |

## 3. The shortfall, named

- **A1 (theta_w is under-quantified).** BFT-1's existential "there exist ... theta_w in (0, 2]" is **strictly
  weaker** than what SQ consumes. Larger theta_w demands faster inter-level decay L^{-theta_w(k-j)}, so the
  existential claim may be satisfied at, say, theta_w = 1/4 and still leave SQ's DESC unserved.
  REVIEW_SQ_S2 l.52, 301-306 records this as "BFT as stated is insufficient". **Fix: restate BFT-1 with
  theta_w carried as a parameter, and record per consumer the theta_w each needs** (PROOF/N5: 0; SF: > 0;
  SQ: > 1). The target is then BFT-1(theta_w) for theta_w > 1, which implies all three.
  Cost: none to state; the proof burden rises and must be re-priced by whoever proves BFT-1.
- **A2 (the cone sibling is not a corollary).** REVIEW_S22's own consumer table records SQ's (REG-min) as
  "**a sibling, not a corollary**: the same weighted-sup absorption estimate as [BFT-1], on a cone with free
  boundary, without uniqueness". A proof of BFT-1 therefore does **not** yield (REG-min). Either it is
  proven natively in SQ (route beta of SQ session 4 is the live attempt) or BFT must acquire a clause.
  **Fix: name it BFT-1c and give it an owner.** It currently has neither a name nor an owner, which is why
  it has fallen between the lanes.
- **A3 (free-boundary cone-box uniqueness / eps-regularity).** REVIEW_SQ_S2 item 4. Not stated by BFT at all.
  SQ session 4's Theorem EPS-T is the candidate supplier; whether it supplies it is for REVIEW_SQ_S4.
- **A4 (all-order mixed-derivative decay).** BFT-3 stops at n <= 4 by construction. (L-loc)_k, which
  CE-exp^k and hence the whole layer-2 cluster expansion consume, needs **all orders**. REVIEW_X12 fix 3
  re-points it to BFT-4's (BB-mix) with per-cube smallness (BFT_B l.510-512), and records that "BFT-3 does
  not supply it, and all-order decay at k = 1 (BB-3_1) is proven but insufficient". **(BB-mix) is OPEN**
  (BFT_B_LOG l.28). So the re-pointing is sound bookkeeping but moves the item, it does not discharge it:
  **layer 2 is blocked on (BB-mix), not on BFT-3.**

## 4. Consequence for planning

1. **BFT-0..5 is not a sufficient target.** Proving all six clauses leaves A1-A4 open, and A4 alone blocks
   every counted conditional theorem of the existence lane that routes through CE-exp^k.
2. The honest target is **BFT-0..5 with BFT-1 parameterised in theta_w > 1, plus BFT-1c (cone, free
   boundary, no uniqueness), plus (BB-mix)**. Three additions, two of which (A1, A2) are restatements that
   cost nothing to make and should be made before any further proof effort is spent on BFT-1, so that the
   effort is spent on the statement the consumers actually need.
3. **(BB-mix) should be promoted** from an internal lane-B item to a named clause, because it is the single
   gate on layer 2's expansion. Suggested name: **BFT-6 (all-order mixed-derivative decay)**.

## 5. Distance to finish, by the project's own measure

PROOF.md [S16] records REVIEW_S15_CONVERGENCE's finding that **"the flat 24 is a counting artefact; the
critical-path DAG with paper-scale / session-scale weights is the honest progress measure"**, and the count
has indeed been flat at 24 OPEN for sessions 15-23 inclusive while substantial mathematics was added.

LINEAR_PACKAGE.md Sec. 10 (frozen 2026-10-27) gives the measure for layer 1:

> about 6-7 paper-scale tasks and 15-18 session-scale tasks

where paper-scale = "about one Balaban-sized paper", with the analogous CMP papers named: background fields
for SU(N) [cf. CMP 102, parts of 99]; propagator bounds at a general background [cf. CMP 95, 96, 99];
localisation and polymer bounds for one soft RG step [cf. CMP 116]; the coupling flow over all scales
[cf. CMP 109 Thm 2, CMP 119]; large-field renormalisation [P x2; cf. CMP 122 I and II]; assembly [cf. CMP 119].

Layer 2 (ym4d-existence) is additionally at 9 HYPOTHESIS-NEW and 12 OPEN of its own (EXISTENCE Sec. 21.5),
and is paused on the layer-1 outputs listed in its Sec. 21.3 consumer list.

**Reading.** This is the correct order of magnitude for the remaining work and it is several paper-scale
tasks, not several sessions. No statement in this repository claims 4D Yang-Mills existence or a mass gap,
and none should be drafted. The deliverable that is in reach is the conditional architecture plus the
individual proven components, credited to Balaban's program and Dimock's expositions.
