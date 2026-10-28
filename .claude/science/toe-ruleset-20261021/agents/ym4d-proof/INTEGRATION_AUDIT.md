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
| SQ | the cone-local analogue of BFT-1 for **minimisers** ((REG-min)); plus theta_w > 1 **as a stated value**; plus a cone-box uniqueness / eps-regularity clause with **free boundary** | **~~NO, three ways~~ RESOLVED, see Sec. 6** | ~~A1, A2, A3~~ **withdrawn; replaced by (CONST-T)** |
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

## 6. Revision after REVIEW_SQ_S4 (same session, 2026-10-28)

**A1, A2 and A3 are withdrawn.** REVIEW_SQ_S4 records that REVIEW_SQ_S2's "BFT as stated is insufficient"
is now **moot for SQ**: SQ session 4 **proves theta_w = 2** (so the theta_w > 1 that SQ consumes is in hand
natively and does not depend on how BFT-1 quantifies theta_w), and **EPS-T + NREFL supply the free-boundary
cone-box clause** (A3). (REG-min) is delivered by route beta natively rather than as a corollary of BFT-1,
which is what "a sibling, not a corollary" always meant — so A2 was a real gap in the *routing*, and SQ has
closed it by proving the sibling rather than by extending BFT.

Consequences the lead must carry:
- SQ Sec. 13.8 was not updated, which makes **RLARGE row 9 and HW row A5 stale**. Binding fix on SQ's owner.
- **The audit's question still had to be asked**, and its answer is now much better than when Sec. 2-4 were
  written: of the four named shortfalls, three are closed and one remains.

**A4 stands, and is now the whole of the shortfall.** (L-loc)_k needs all-order mixed-derivative decay;
BFT-3 stops at n <= 4 by construction; REVIEW_X12 fix 3 re-points it to BFT-4's **(BB-mix)**, which is OPEN
(BFT_B_LOG l.28). Recommendation unchanged: **promote (BB-mix) to a named clause, BFT-6.**

**A5 (new, from REVIEW_SQ_S4): (CONST-T).** EPS-T's Moser constant C_T is uncomputed, and the
(CLS-min) -> RLARGE interface carries a number only if C_T <~ 1e13. The reviewer's read of the written proof
puts C_T in 1e9-1e15, i.e. straddling. This is not a defect of the target BFT; it is a missing constant on a
delivered interface, and it is the most tractable high-value item in the project right now: a bounded,
session-scale computation whose outcome decides whether route beta's clean clause-by-clause delivery is
usable or vacuous.

**Revised reading.** The target BFT-0..5 plus BFT-6 (= (BB-mix)) is, as far as this audit can tell, now
sufficient for its consumers. The binding uncertainty has moved from the *adequacy of the target* to the
*size of two constants*: C_T here, and the per-level compounding factor of decision D3.

## 7. Second revision, after NORMS.md (same session)

**A1 is REINSTATED, for a different and stronger reason than it was first raised.** Section 6 withdrew it
because SQ proved theta_w = 2 natively, so SQ no longer depended on how BFT-1 quantifies theta_w. That
withdrawal was correct as far as SQ goes. But NORMS.md Theorem N1-15 shows the defect is more basic:

    A = L^(d - theta_w^r - 2*theta_A),  theta_A = min(1, theta_w^c - 1),  so  A < 1  <=>  theta_w^r + 2*theta_A > d.

At d = 4 this is met by the PAIR (curvature theta_w^c = 2, residual theta_w^r = 3), and **with a single
common theta_w there is no solution in (0, 2] at all.** BFT-1 as stated carries one existential
theta_w in (0, 2]. **So BFT-1 cannot support the composite route as written, for anybody -- not only for SQ --
and must be restated with a weight pair.** This merges with REVIEW_SQ_S2's item (2).

**Recommendation (A1'):** restate BFT-1 with two weights, curvature theta_w^c = 2 and residual
theta_w^r = d - 1, and record per consumer which it needs. This costs nothing to state and it is the
statement the only working route actually needs. Note that it is also the MAXIMAL curvature weight: NORMS.md
records explicitly that this route "needs the maximal theta_w^c = 2 and does not get easier at small
theta_w", so a weaker BFT-1 is not a safer BFT-1 here.

**A5 ((CONST-T)) stands and is under way.** A4 ((BB-mix), proposed as BFT-6) stands.

**A6 (new): PROOF.md's own diagnosis of Z_col is wrong.** PROOF.md l.6211-6213 attributes Z_col = 156 to
"the L^(d-1) = 27 crossing links of one coarse link times the spread". NORMS.md Proposition N1-8 proves by
an exact mass-balance identity that it is the column mass of the curvature kernel, L^d * Kbar ~ 9.7 plus
(2/(d-1)) * K_rho ~ 1.5, and that **the crossing-link count vanishes once the leg is measured through d_1 X**.
Lead to correct in the consolidation. This matters beyond bookkeeping: the wrong diagnosis is what made the
per-level route look like a norm problem, when NORMS.md shows it is a marginality no-go that no
scale-covariant norm can fix.

**Revised reading, superseding Sections 4-6.** The target's shortfall is now: A1' (BFT-1 as a weight pair),
A4 ((BB-mix) / BFT-6). The binding uncertainties are two constants, (CONST-T) and the composite route's
(N-Q), both under way. **And one conceptual correction the lead must carry: the MAGNITUDE problem and the
UNIFORMITY problem are different problems with different causes.** Decision D3 conflated them. The
uniformity problem is solved at the trivial background by Theorem N1-15, conditional on (N-Q) and (N-loc);
the magnitude problem is dominated by 288*A_in*coth^4(m_1/2)*ell_theta, is some 10^32 above the C_flat term,
and is untouched by anything in this session.
