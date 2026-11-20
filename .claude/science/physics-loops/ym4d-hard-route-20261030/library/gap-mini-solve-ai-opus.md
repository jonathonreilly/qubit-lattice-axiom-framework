lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T23:17Z

# gap-mini-solve-ai-opus (FINISH row 1260)

Started 2026-11-20T11:17Z (date -u) at commit 9cea71828 on branch claude/ym4d-hard-route.

The problem (row 1260): prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the sense of Jaffe and Witten.

Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.

## Step 0. Orientation (written 2026-11-20T11:22Z by date -u)

**0.1 What the record fixes (pointers to evidence, not evidence).** Read for this row: GOAL.md; FINISH.md sections
How we work, Joining, Working efficiently, Rules; the RESULT lines of rows 1180-1258; `parts/gap.md` State of attack;
row 1256 (`gap-mini-solve-af-opus.md`, Steps 1, 3, 4); row 1258 (`gap-mini-solve-ag-opus.md` 4.1, 6).
- Beside the account's premises, the Jaffe-Witten gap on the account's tr F^2 sector reads one infrared input: (N-phys)
  (rows 1161, 1179, 1225; check 1232), or, on the one-cutoff carry of row 1233 (check 1242; rows 1255, 1256), a seed at
  one base datum. Row 1258 states the base seed in its weakest proved-sufficient form, (SL) or (RR) at one cutoff's
  couplings, at slab thickness of a few tens of correlation lengths.
- Every route family for that infrared seed found by about eighty plain-brief rows is on file with a first failing step
  (`parts/gap.md` methods 19-36, route registry RA-RG; screening tables of rows 1189, 1194, 1199, 1237, 1256). Row 998 9.5
  asks for no further fresh-framing exercise. Proposition CA-FAIL (row 1072, check 1074: HOLDS AFTER CORRECTION) refutes
  full-specification strong mixing in the window; (SL) conditions on two slices only, so CA-FAIL does not bind it as
  stated (a pinned single slice leaves the next layer of spatial links free, so no pinned 3D O(4) layer appears).
- The one-cutoff carry on the pin route (row 1256 Proposition PIN, Lemma OFF) reads, beside the base seed: (FI) at pins
  (clause (0)'s Balaban flow from the pin a_K reaches the reference coupling X after K steps, as the tuned run does),
  the 9.1 hypotheses (a)-(e) at u = 0 with (e) = `9.1:prop-blind-site-expansions` OUTSTANDING in the account, (DET)'s
  inputs, (V9) at pins (row 1255; its check, row 1263, is running), and the account's premises. (MON) is needed only on
  the first-passage-top route.

**0.2 Running beside this row (same plain brief, files not visible at this pin):** row 1259 (worker 1) and row 1264
(worker 3). Overlap with them cannot be checked from this checkout; the item chosen below is named so that the lead can
compare.

**0.3 Plan (judgement, ARGUED).** The infrared seed is the open core of the problem and no session-sized route to it is
on record; I do not re-screen it. I take the next input of the carry that no row works on: (FI) at pins, which row 1256
4.1 named and left as "construction-level". Step 1 reads the account's two frames (clause (0)'s couplings, CA-I
`1.2:def-couplings`; the tuned runs, CA-III `9.1:def-tuned-family`, `9.12:def-runs-coupling-map`) and the hypotheses the
account itself states for the identity (III:68713-68716, III:54429-54434, III:54832-54835). Step 2 either proves (FI) at
pins, or a weaker form with a bounded defect that Lemma OFF and Proposition PIN can read, from proved account
statements, or names the first account statement it needs. Step 3: status table and RESULT.
Moves: (FI) of the one-cutoff carry, an open input of the gap chain's ultraviolet half (row 1256 4.2). Success: (FI)
at pins leaves the input list or is replaced by proved account statements plus one named estimate. Failure: the first
account statement that the identity needs and the account does not prove.

## Step 1. The two frames in the account, read (written 2026-11-20T11:26Z by date -u; READ unless marked)

Source: Sussman and Alpoge's complete account at commit 31a47c543775 (`theorem_0_complete_account_raw_I.tex`, `_III.tex`,
fetched by URL into a scratch folder outside the repository; credit Ethan Sussman and Levent Alpoge, with Claude and
Codex as authors of their text; the construction is Balaban's). I:n and III:n are TeX lines.

**1.1 Clause (0)'s frame.** `1.2:def-couplings` (I:606-628): x_0 = g_0^(-2), x_(k+1) = x_k - beta_(k+1), with beta_(k+1)
"Balaban's coupling renormalization ... defined in [B-CMP109, (1.22)]", identified with [B-CMP119, (3.61)]; its
construction "within Balaban's step" belongs to Chapter 4. `9.13:cor-coupling-shift` (III:68697-68745) states clause (0)'s
two-sided flow bound lambda^sharp (j - i) - c_5 <= x_i - x_j <= B^sharp (j - i), and takes as hypothesis (b) that x_k is
"a function of (Lambda_n, x_0) and of k only" (III:68713-68716). The identification of clause (v)'s pins with these
couplings "is part of the statement of Theorem 3.1 and is not proved again here" (III:68760-68763).

**1.2 Chapter 9's frame.** `9.13:not-canonical-scaffold` (III:68946-69060): the canonical scaffold is the linear ramp
theta_r = X + c_0 r; a run of length n from the bare deviation zeta has bare inverse coupling theta_n - zeta and
zeta_(r) = zeta_(r+1) + b_(r)(zeta) - c_0, x_(r) = theta_r - zeta_(r), with b_(r) = beta^0_(n-r) + f_(n-r)(zeta_(n), ...,
zeta_(r+1)) + q_(r). The pin is a_n = theta_n - zeta_*^n(0), the bare coupling whose run has x_(0) = X exactly. The step
function is defined in `9.9:not-running-shift` (III:55752-55800): "b_(k+1)(zeta) is the number defined in [B-CMP109,
(3.61)], computed for the whole-lattice family of the correlation theorem ... at bare weight x_0 - zeta. In computing it,
every threshold, every cube size, every decomposition, every background and every reference law is frozen at its value
in the run with zeta = 0. No statement is made here about the run of the recursion started at x_0 - zeta"
(III:55764-55768). On the scaffold, the zeta = 0 run is the run from the bare point theta_n.

**1.3 What (FI) at pins is (ARGUED from 1.1-1.2).** The tuned run at the pin computes the increments at bare weight
a_K = theta_K - zeta_*^K(0) with every threshold, cube size, decomposition, background and reference law frozen at the
run from theta_K. Clause (0) computes Balaban's increments at bare weight a_K with these data taken from the run from
a_K itself. (FI) at pins says the two depth-0 couplings agree: x_K(a_K) = X. The account makes no statement relating the
two (III:55767-55768) and assumes the identity where it uses it (1.1). So (FI) is a representation-independence statement:
two exact rewritings of one bare datum, with different auxiliary data, assign the same effective coupling. Exact
agreement is not to be expected (the coupling of a Balaban representation is the coefficient of the Wilson term beside
remainders that depend on the auxiliary data). What the carry needs is less: Lemma OFF and Proposition PIN of row 1256
need only a defect bound |x_K(a_K) - X| <= varpi with varpi bounded uniformly in K (row 1256 3.4 Remark 2: the offsets
become 1 <= delta <= ceil((B^sharp + c_5 + varpi)/lambda^sharp)).

**1.4 A route that avoids a step-by-step comparison (idea, to be tested in Step 2).** Both frames describe the same bare
datum, so they have the same Schwinger functions at the reference scale. If an account theorem expresses one physical
reference-scale quantity S of a run as Phi(x_(0)) + err, with Phi explicit, strictly monotone with |Phi'| bounded below,
and err bounded, for every run of the correlation theorem's class, then applying it in both frames gives
|x_K(a_K) - X| <= (err_A + err_B)/inf|Phi'|. The account has such theorems: `8.1:thm-two-point-witness` (II:71279, index
PROVED), `9.9:thm-nondegenerate-calibration` ("Non-degenerate calibration by the two-point witness", III:57243, index
PROVED), `9.9:thm-differentiated-witness` (III:57753); and `9.9:prop-remainder-derivative` (III:56333) is OUTSTANDING.
Step 2 reads them and decides whether they apply to both frames.

