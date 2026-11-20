lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T00:59Z

# gap-mini-solve-al-opus: the SU(2) mass gap in four dimensions (FINISH row 1268)

Started 2026-11-20T12:59Z (date -u), pinned at commit 2a8526154 on branch claude/ym4d-hard-route. Research-stage working state; nothing here is a public claim.

Labels: PROVED (complete written argument here or cited with location), ARGUED (argument with a named gap), GUIDE (heuristic or numeric guide, never a proof step), OPEN.

## Step 0. Plan (written first, per the save protocol)

Reading order: FINISH.md rules and the RESULT lines of the gap rows; `parts/gap.md`; `library/open-core.md`; `library/prior/gap-onebound-read-sol.md` (row 1218, new published work); the latest gap-mini-solve outputs (-ak-, -am-) and the memory-flagged route screens, so that this run does not repeat a closed route. Then choose one attack and do it in steps, appending each step here.


## Repo search and record read (written 2026-11-20T13:04Z by date -u)

Read for this row: `GOAL.md`; `FINISH.md` L1-84 and L299-352 (rules), the queue row 1268 and the RESULT lines of rows
1256-1279; `parts/gap.md` L1-104 (state of attack); `library/prior/gap-onebound-read-sol.md` L1-260 (row 1218, the
published-work reading: A's thermal criterion, B's Corollary 166, Zeng's tunnelling package); row 1267
(`library/gap-mini-solve-ak-opus.md`) in full; the opening of the concurrent row 1275 (`library/gap-mini-solve-am-opus.md`).

What the record fixes (pointers, not evidence):
- The gap clause reads one infrared input, (N-phys) (rows 1161, 1179), or, on the one-cutoff carry (row 1233
  Proposition 3.7, check 1242), a seed at one base datum; row 1258 (check 1265) gives sufficient one-coupling forms
  (SL)/(RR). No engine for the band is on file: about 45 route families end at a named failing step (`parts/gap.md`
  methods 19-36 and route registry; rows 1188-1273). Row 1275 ran a grep screen of 36 further mechanism names in the
  gap files and found every one on file.
- The carry's open inputs after rows 1256, 1260, 1267 and checks 1263, 1266: (FC-T) (row 1267 4.5), the bookkeeping
  hypotheses (H2), (H3) and the kernel form (K) of row 1267, (V9) (row 1255; taken by the concurrent row 1275), the
  account's 9.1 hypothesis (e) and 9.1:prop-blind-site-expansions (row 1264, blocked on Balaban CMP 116), (DET)'s inputs,
  the account's premises.
- Row 1275 (Mac mini worker 1) states that it leaves "(FC-1)/(FC-T) of row 1267" to this row.

## Step 1. How best to attack it (judgement, ARGUED; written 2026-11-20T13:04Z by date -u)

The Jaffe-Witten gap for four-dimensional SU(2) needs two things on this lane: an order-one input at one physical scale
(the seed), and a carry of that input to every finer cutoff. For the seed I have no engine that is not on file, and the
record (row 998 9.5, row 1275 Section 1) says a further blind screen is waste. A session-sized result that any future
proof must pass through is on the carry. Its open input with no owner is (FC-T).

**Item: (FC-T) of row 1267.** At one step k and at the same weights and list, the frozen-scaffold frame phi_k and the
run's own frame psi_k (|phi_k - psi_k| at most of order theta_k^(1/2) polylog) give unmarked totals that differ by
log < pi_phi / pi_psi >_psi + const (row 1267 Proposition SPLIT); (FC-T) asks for coherent localizations of this total
with |||.|||_(k+1) <= nu_k and sum_k nu_k bounded uniformly in n.

Moves: the one-cutoff carry on the pin route (row 1233 Proposition 3.7; rows 1256, 1260, 1267). Success: (FI) at pins
leaves the carry's input list, given (H2), (H3), (K). Failure: the first statement of the account's chapter 4 (or of
Balaban's step as the account cites it) that (FC-T) needs and that is not stated, or a frame-dependent cut at an
order-one threshold that moves the total by a non-summable amount; then the pin route needs a different matching, and
the lead should know it.

Rule 0a: `library/open-core.md` and the FINISH rows name (FC-T) only in row 1267 (author); no queued row owns it
(grep in Step 2).

**Plan.** Step 2: fetch CA-I (and CA-II/III if needed) at 31a47c543775 into a scratch folder; read chapter 4's
decompositions of unity (which variables, which thresholds, which units) and the one-step localization with its failure
term. Step 3: state (FC-T) in the account's notation. Step 4: prove it, or name the first failing step. Step 5: labels,
state of the carry, RESULT.

## Step 2. How the thresholds enter the account's step (READ; partial, written 2026-11-20T13:06Z by date -u)

Source: Sussman and Alpoge, complete account CA-I at 31a47c543775 (`theorem_0_complete_account_raw_I.tex`, 166711
lines), fetched by URL into a scratch folder outside the repository; I:n is a TeX line. Credit Ethan Sussman and Levent
Alpoge, with Claude and Codex as authors of their text; the construction is Balaban's (CMP 109, 116, 119, 122).

**2.1 The thresholds (READ, I:29060-29120, Definition 4.7:not-running-couplings).** With p_0(g') = A_0 (log g'^(-2))^(p_0)
(Balaban's degree function), eps_m := g_m p_0(g_m) and
    delta_m := (A_1/A_0) eps_m = A_1 (log g_m^(-2))^(p_0) g_m,                                        (2.1)
"the threshold of [B-CMP119 (3.16)]". The complex fluctuation box of [B-CMP119 (3.43)] is |A| < C_1 p_1(g_k), and "at level m
the fluctuation size on the box is C_1^fl delta_m". The exponents obey q - p_0 >= 3r + 2 > 0 and p_0 >= 5r (I:29113-29117).
Here g_m is "the running coupling at level m of the history actually produced by the steps performed" (I:29064-29066).
So in row 1267's notation (theta = x = g^(-2)) the threshold is delta(theta) = A_1 theta^(-1/2) (log theta)^(p_0), and
theta delta(theta)^2 = A_1^2 (log theta)^(2 p_0): row 1267's GUIDE size is the account's own threshold.

**2.2 The one-step theorem the account uses (READ, I:4136-4210, Theorem 4.3:thm-small-field-step, "cited by statement"
from Balaban CMP 109 Theorem 3, with CMP 116 and CMP 119 (3.43)).** For an arbitrary family of effective actions with
Balaban's inductive properties and an arbitrary g in (0, gamma], "the fluctuation integral [B-CMP109 (2.12)-(2.13)] at
coupling g produces an effective action E^(k+1) with the same properties and the same constants"; under two conditions on
g (C_1 g p_1(g) <= eps^I_1, and the cutoff radius (A_1/A_0) p_0(g) above the constant of [B-CMP116 (2.31)]) the same holds
"with the fluctuation domain of [B-CMP119 (3.43)]" and "the cutoff radius just described", and the non-Gaussian part of
E^(k+1) obeys [B-CMP116 (2.41)] with the factor eps^I_1. The account adds (I:4199-4205): "In Balaban's argument the
couplings enter only through the containment 0 < g_k <= gamma and, in the second part ..., through the two conditions
stated there"; "no special asymptotic behaviour of the couplings is assumed".

**2.3 Consequence for (FC-T) (PROVED, elementary, from 2.2).** The cited theorem bounds each of the two outputs (frame phi,
frame psi) separately, by eps^I_1 times the decay; it states nothing on how the output moves with the cutoff radius. So the
difference of the two outputs is bounded by the theorem only by 2 eps^I_1 per localized term, a fixed constant, which is
not summable in k. (FC-T) therefore needs a statement that is not in the cited theorem: a bound on the dependence of the
localized output on the threshold. Where the account or Balaban's CMP 116 treats the cut inside the fluctuation integral
decides whether such a bound is available (2.4 below).

(Stopped here at 2026-11-20T13:06Z: next, read how the account treats the small-field cut inside the fluctuation integral, I:60052 ff.,
I:62551-62571, I:88656, and the 4.15 decompositions of unity, to find whether the cut enters through correction terms.)
