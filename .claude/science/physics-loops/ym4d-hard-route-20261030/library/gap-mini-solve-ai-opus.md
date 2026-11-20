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

## Step 2. (FI) in the account: what it is, where the account uses it, one route that fails (written 2026-11-20T11:31Z by date -u)

**2.1 The two frames, exactly (READ).** `9.13:not-scaffold-runs` (III:70175-70230) names them. The *own-threshold run*
of clause (0) from a bare coupling has the increments b_j of `1.2:def-couplings`; its first-passage level is
K(g_0, g) = min(k : x_k <= X + B^sharp). The *frozen scaffold* Theta_X "is the assignment ... of every coupling-dependent
choice of Balaban's step at depth r to its value at the coupling g_(r) := theta_r^(-1/2)", theta_r = X + c_0 r, "the same
for all run lengths n"; the action entering the scaffold's choices at depth r "is the pure Wilson action with coefficient
theta_r(X)" (III:70559-70562). The pins a_n = theta_n - zeta_*^n(0) are defined on the frozen scaffold; Theorem 3.1
(v-a) says so in its own words: "the n-step recursion from x_0 = a_n (with infinite-lattice coefficients and the
coupling-dependent choices fixed in terms of X) ... ends at x_n = X exactly" (I:2836-2838). The frozen run's coupling at
depth r differs from theta_r by the shift zeta_(r), and along a tuned run |zeta_(r)| <= |w| + 2c_2 + sum_(u<r) iota_u,
with the drift sum of order theta_r^(1/2) (log theta_r)^(p_0) (III:69020-69030, (c) and (9.13:eq-canonical-scaffold-2)).
So at depth r the two frames evaluate the coupling-dependent choices at couplings whose inverse squares differ by up to
order theta_r^(1/2) polylog. (FI) at pins says these two runs from the same bare datum a_K reach the same coupling at
depth 0.

**2.2 The account's own name for (FI): "the scaffold comparison" (READ).** The account invokes, by name only, "the
scaffold comparison, which compares, at one cutoff, the run carrying its own threshold with the run on a frozen scaffold"
(III:71033-71034), with "the bound |x^own - x^Theta| <= varpi(g) of the scaffold comparison, where that comparison
applies" (III:70519-70521), "at every level" (III:70586-70590), and "varpi(g) <= 1 ... the cross-scaffold modulus of the
scaffold comparison" (III:70723, III:71047). It enters: `9.8:cor-subsequential-limits` (a) (III:54156-54198, OUTSTANDING,
with varpi(r_J, g) undefined there, as row 1256 3.1 found); `9.8:rem-increment-bound`, whose step (*) states "the
scaffold comparison has to apply to the depth-(n+1) scaffold at the bare data a_n - w ... Its hypothesis is stated for
data in the window of a_(n+1), so a continuity or bootstrap argument along w is needed" (III:55650-55654; "Stated; proof
incomplete"); the first half of the uniqueness corollary as used in `9.13:prop-limit-member` (III:70718-70723,
III:71075-71081). A grep of CA-I, CA-II and CA-III at 31a47c543775 for "scaffold comparison", "cross-scaffold" and
"varpi(g)" finds no labelled statement of it and no proof; every hit is a use. (CA-I's "scaffold" in chapter 4.21 and
CA-II's `5.1:def-source-free-scaffold`, `5.5:not-one-scaffold` are the machine's geometric scaffold, a different object.)
Theorem 3.1 clause (0) lists among "Not asserted": "a sign of x_k - x_(k+1) at a single step ... monotonicity of a tuned
bare coupling ... regularity of beta_j in the couplings" (I:2552-2556).
So: **(FI) at pins with a bounded defect is the account's unstated "scaffold comparison" at the pins**, and row 1256's
(FI-W) is the same comparison on the window. The account's Theorem 3.1 (v-c)(2) (I:2865-2868), the window inclusion and
the identification of first-passage limits, rests on it through `9.8:cor-subsequential-limits`.

**2.3 What the carry needs from it (PROVED from row 1256).** Lemma OFF and Proposition PIN need only
(SC-pin) |x^own_K(a_K) - X| <= varpi for every K >= K_0, with varpi bounded uniformly in K;
then by row 1256 3.4 Remark 2 and Lemma OFF the pin a_K first-passes at a depth K + delta with
1 <= delta <= ceil((B^sharp + c_5 + varpi)/lambda^sharp). (The proof of Lemma OFF uses x_K(a_K) only through the window
X - varpi <= x_K <= X + varpi and clause (0)'s two-sided flow bound.) The account's own bound varpi <= 1 would do.

**2.4 A route that fails: calibration by the two-point witness (PROVED, elementary).** Idea of Step 1.4: both runs from
a_K carry the same bare datum, so the same Schwinger functions; a theorem expressing a reference-scale correlation as an
explicit function of the run's coupling would bound the defect. The account's `8.1:thm-two-point-witness` (II:71279-71372,
index PROVED) gives, for first-passage data, S^T_(2;K,m)(f_1, f_2) = N_(K-s)^2 b_0 g_(K-s)^4 K_(K,s)(f_1, f_2)(1 + R_K)
with |R_K| <= 1/4 and N_(K-s) in [2/3, 4/3]. If two runs carried this formula with couplings x^A, x^B at the witness level
(same kernel), then (x^B/x^A)^2 = (g^A/g^B)^4 lies in [(3/4)(2/3)^2/((5/4)(4/3)^2), its inverse] = [3/20, 20/3], so
x^B/x^A lies in [0.387, 2.59]. That bounds the ratio, not the difference: at x of order X the defect can be of order X.
So calibration by any statement with a relative error of fixed size cannot give (SC-pin); it needs a relative error
O(1/X) in g^4, i.e. the two-point function to next-to-leading order with an explicit constant, plus the witness theorem
on the frozen frame (which the account takes as the fourth hypothesis of `9.9:def-tuned-hypotheses`, not as a theorem),
plus a comparison of the s levels between the witness level and the reference level. The route stops at its first step.

