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
  one base datum. Row 1258 gives a sufficient one-coupling form of the base seed, (SL) or (RR) at one cutoff's
  couplings, at slab thickness of a few tens of correlation lengths.
- Every route family for that infrared seed found by about eighty plain-brief rows is on file with a first failing step
  (`parts/gap.md` methods 19-36, route registry RA-RG; screening tables of rows 1189, 1194, 1199, 1237, 1256). Row 998 9.5
  asks for no further fresh-framing exercise. Proposition CA-FAIL (row 1072, check 1074: HOLDS AFTER CORRECTION) refutes
  full-specification strong mixing in the window; (SL) conditions on two slices only, so CA-FAIL does not bind it as
  stated (ARGUED: at slab thickness 2 or more the spatial links between the two pinned slices are free, so no pinned
  3D O(4) layer of CA-FAIL's kind appears).
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
need less than exact agreement: a defect bound with varpi bounded uniformly in K, read at every level of the run up to
its first passage (Step 3, Lemma OFF': the first-passage depth of a_K then stays within a bounded distance of K).

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
with the drift sum of order theta_r^(1/2) (log theta_r)^(p_0) (III:69015-69017, (c), and III:69052-69054, (9.13:eq-canonical-scaffold-2)).
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
"varpi(g)" finds no labelled statement of this own-threshold comparison and no proof of it; every hit on it is a use.
Two further hits use the words otherwise: III:18576 ("the flat scaffold comparison of this chapter", a flat-field
statement about group-valued factors in chapter 9.1) and II:134127 ("The scaffold comparison in all zones", listed as an
assumption of a chapter 8 proposition, with its own ceiling on gamma, II:134149; I did not identify its object). (CA-I's
"scaffold" in chapter 4.21 and CA-II's `5.1:def-source-free-scaffold`, `5.5:not-one-scaffold` and the "frozen scaffold of
the stage" at II:39298 are the machine's geometric scaffold, a different object.)
Theorem 3.1 clause (0) lists among "Not asserted": "a sign of x_k - x_(k+1) at a single step ... monotonicity of a tuned
bare coupling ... regularity of beta_j in the couplings" (I:2552-2556).
So: **(FI) at pins with a bounded defect is the account's unstated "scaffold comparison" at the pins**, and row 1256's
(FI-W) is the same comparison on the window. The account's Theorem 3.1 (v-c)(2) (I:2865-2868), the window inclusion and
the identification of first-passage limits, rests on it through `9.8:cor-subsequential-limits`.

**2.3 What the carry needs from it (PROVED in Step 3 from row 1256).** Lemma OFF and Proposition PIN need only
(SC-pin) |x^own_k(a_n) - x^Theta at level k| <= varpi_n at every level k <= min(n, K(a_n, g)), for every n >= K_0,
with varpi_n bounded uniformly in n. Then Lemma OFF' (Step 3) puts the first-passage depth K(a_n, g) within a bounded
distance of n, which is what Corollary OFF-1 of row 1256 uses. A bound at the last level alone does not suffice: the
lower bound on the first-passage depth reads the intermediate levels. The account's own bound varpi(g) <= 1 would do.

**2.4 A route that fails: calibration by the two-point witness (PROVED, elementary).** Idea of Step 1.4: both runs from
a_K carry the same bare datum, so the same Schwinger functions; a theorem expressing a reference-scale correlation as an
explicit function of the run's coupling would bound the defect. The account's `8.1:thm-two-point-witness` (II:71279-71372,
index PROVED) gives, for first-passage data, S^T_(2;K,m)(f_1, f_2) = N_(K-s)^2 b_0 g_(K-s)^4 K_(K,s)(f_1, f_2)(1 + R_K)
with |R_K| <= 1/4 and N_(K-s) in [2/3, 4/3]. If two runs carried this formula with couplings x^A, x^B at the witness level
(same kernel), then (x^B/x^A)^2 = (g^A/g^B)^4 lies in [(3/4)(2/3)^2/((5/4)(4/3)^2), its inverse] = [3/20, 20/3], so
x^B/x^A lies in [0.387, 2.582]. That bounds the ratio, not the difference: at x of order X the defect can be of order X.
So calibration by any statement with a relative error of fixed size cannot give (SC-pin); it needs a relative error
O(1/X) in g^4, i.e. the two-point function to next-to-leading order with an explicit constant, plus the witness theorem
on the frozen frame (which the account takes as the fourth hypothesis of `9.9:def-tuned-hypotheses`, not as a theorem),
plus a comparison of the s levels between the witness level and the reference level. The route stops at its first step.

## Step 3. The scaffold comparison from a one-step frame-change bound (written 2026-11-20T11:38Z by date -u)

**3.0 The newer manuscripts (READ; credit Sussman and Alpoge, with Claude and Codex as authors of their text).** At
their head c7fef8b21b58 (2026-11-10), `YM4/RT/YM4_RT.tex` ("Coupling trajectories and partition stability", working draft
of 9 November 2026) and `YM4/EM/YM4_EM.tex` treat one frame at a time. EM: "The frame fixes the lattice partitions,
Gaussian references, real fluctuation coordinates and tests. The variable x_k does not change those choices" (EM L504-505).
RT builds the first-passage trajectory with "theta_j = x_j as each new entry is admitted" (RT Theorem
`rt:thm-joint-trajectory`, L960-1000) and tunes on a fixed affine frame (RT Theorem `rt:thm-frozen-tuning`, L1594-1625),
then says: "The tuned endpoint h is a condition on the fixed reference run. First passage is defined separately for the
self-calibrated trajectory" (RT L1670-1673). A grep of RT and EM for "scaffold", "own-threshold", "frame" finds no
comparison of two frames. So no text of the account states or proves the scaffold comparison of 2.2.

**3.1 Setting.** Fix n >= 1 and a real bare weight beta. Levels k = 0, ..., n count steps from the cutoff. A *frame* is a
real sequence phi = (phi_0, ..., phi_n) at which every coupling-dependent choice of the step at level k is evaluated
(2.1). For a frame phi and a weight prefix w = (w_0, ..., w_k) in the tube T_k(phi, s) := (|phi_j - w_j| < s phi_j,
j <= k), the coefficient formed at step k+1 is split as in the account and in EM,
    b_(k+1)[phi; w] = U_(k+1)(phi; w) + q_(k+1)[phi; w],
with U_(k+1)(phi; w) := b^0_(k+1)(phi) + f^phi_(k+1)(phi_0 - w_0, ..., phi_k - w_k) the *unmarked total* (the Gaussian
number plus the unmarked function) and q the *marked remainder* (account: `9.9:not-running-shift` (d), III:55821-55850,
b_(k+1) = beta^0_(k+1) + f_(k+1)(zeta_0, ..., zeta_k) + q_(k+1)(zeta); EM Theorem `em:thm-coefficient-envelope`, EM
L1338-1380, b_(k+1) = b^0_(k+1) + f_(k+1)(z_0, ..., z_k) + q_(k+1), z_i = theta_i - x_i).
Two runs from the same bare weight beta:
- run A, *frozen*: a fixed frame phi^A; weights w^A_0 = beta, w^A_(k+1) = w^A_k - b_(k+1)[phi^A; w^A_(<=k)], for k < n;
- run B, *own threshold*: the run of clause (0); its frame at each level is its own weight, so
  b^B_(k+1) = U_(k+1)(w^B_(<=k); w^B_(<=k)) + q^B_(k+1); it is constructed for the levels k <= K_B := min(n, K(beta, g)).
For the pin run of length n, phi^A_k = theta_(n-k) = X + c_0 (n - k) (canonical scaffold, 9.13).

**3.2 Hypotheses.**
- (G1) Lipschitz bound of the frozen unmarked total: for prefixes w, w' in the half tube T_k(phi^A, sigma/2),
  |U_(k+1)(phi^A; w) - U_(k+1)(phi^A; w')| <= L_k max_(j<=k) |w_j - w'_j|.
  Supplied (READ) by the account's memory bound (9.9:eq-running-shift-5), sup over the half polydisc of
  sum_j sigma_0 x_j |df_(k+1)/dxi_j| <= (4/3) A e_k, which gives L_k = (4/3) A e_k / (sigma_0 min_(j<=k) x_j); and by EM
  Corollary `em:cor-coefficient-slopes` (EM L1403-1438): Lipschitz constant at most C eps_k / theta_k in the sup norm, with
  eps_k = C_u theta_k^(-1/2) (log theta_k)^(p_0). (The Gaussian number does not depend on w, so it drops out of (G1).)
  Status of that supply for the frozen pin run (READ): the account says the running-shift statement with its fine
  bookkeeping holds "for the first-passage runs of the correlation theorem ... by that theorem, about the origin
  zeta = 0 ... which is the run itself", while "for the tuned run of the class Theta_X ... they hold by the hypothesis
  of Definition 9.9:def-tuned-hypotheses that transfers these two statements of the correlation theorem to the runs of
  the class S, read about the values zeta_*^n of the level variables at the tuned run" (Remark `9.9:rem-curvature-scope`
  (3), III:57120-57130). So for run A, (G1) and (G2) are the account's tuned-family hypothesis, not a theorem of the
  account; in EM they are Theorem `em:thm-coefficient-envelope` on a fixed frame, proved from EM's admitted inputs.
- (G2) Marked remainders: |q_(k+1)[phi^A; w^A]| <= eps'_k and |q^B_(k+1)| <= eps'_k. Supplied (READ) by |q_(k+1)| <= v_k,
  v_k = 2 A C_t C_m y_k^(-(kappa_0 - 4)/2) (account 9.9 (d)), and by EM (em:eq-coefficient-envelope),
  |q_(k+1)| <= C theta_k^(-(kappa_0-4)/2) (log theta_k)^(-2q); summable when kappa_0 > 6, and the account's regime has
  kappa_0 >= 10 (III:57245-57247).
- (G3) = **(FC), one-step frame change at the own weights**: whenever the prefix w^B_(<=k) of run B lies in
  T_k(phi^A, sigma/2), |U_(k+1)(phi^A; w^B_(<=k)) - U_(k+1)(w^B_(<=k); w^B_(<=k))| <= eta_k.
  In words: at one step and at the same weights, forming the unmarked total on the frozen frame or on the frame equal to
  the weights changes it by at most eta_k. **OPEN**: no text of the account (CA-I to III, RT, EM) states it (3.0, 2.2).
- (G4) Tube of the frozen run: |phi^A_j - w^A_j| <= sigma phi^A_j / 4 for j <= n. Supplied (READ) for tuned runs by
  aliveness, |zeta_(s)| + 2R <= varrho_s at every depth ((J3) of `9.1:def-tuned-family`, III:1331-1340), together with
  condition 5 of `9.9:thm-nondegenerate-calibration`: "varrho_s <= (1/4) sigma_0 (theta_s - 2c_2) for all s >= 0 ... the
  tube radius at every depth is at most a quarter of the polydisc radius there" (III:57293-57307).
  (G4) is used only to place the prefixes of both runs in the half tube about the frame. When (G1) is stated about the
  frozen run itself, as the account reads it (Remark `9.9:rem-curvature-scope` (3)), on the neighbourhood
  |w_j - w^A_j| <= sigma phi^A_j/4, then (G4) can be dropped and (G5) reads e^Lambda M <= sigma min phi^A/4 as before.
Put Lambda := sum_(k<n) L_k, M := sum_(k<n) (eta_k + 2 eps'_k), and assume
    (G5) e^Lambda M <= sigma min_(k<=n) phi^A_k / 4.

**Lemma GR (PROVED, elementary; an implication from (G1)-(G5)).** For every level k <= K_B,
    |w^A_k - w^B_k| <= e^(Lambda_k) M_k <= e^Lambda M,
where Lambda_k := sum_(l<k) L_l and M_k := sum_(i<k) (eta_i + 2 eps'_i).
*Proof.* Put delta_k := max_(j<=k) |w^A_j - w^B_j|, so delta_0 = 0 (both runs start at beta). Assume
delta_k <= e^(Lambda_k) M_k for some k < K_B. Then delta_k <= e^Lambda M <= sigma min phi^A / 4 by (G5), so for j <= k,
|phi^A_j - w^B_j| <= |phi^A_j - w^A_j| + delta_k <= sigma phi^A_j/4 + sigma phi^A_j/4 = sigma phi^A_j/2 by (G4): both
prefixes lie in the half tube T_k(phi^A, sigma/2). Write
    b^A_(k+1) - b^B_(k+1) = [U_(k+1)(phi^A; w^A_(<=k)) - U_(k+1)(phi^A; w^B_(<=k))]
                          + [U_(k+1)(phi^A; w^B_(<=k)) - U_(k+1)(w^B_(<=k); w^B_(<=k))] + q^A_(k+1) - q^B_(k+1).
The first bracket is at most L_k delta_k by (G1), the second at most eta_k by (G3), the rest at most 2 eps'_k by (G2).
Hence |w^A_(k+1) - w^B_(k+1)| <= |w^A_k - w^B_k| + |b^A_(k+1) - b^B_(k+1)| <= (1 + L_k) delta_k + eta_k + 2 eps'_k, and so
    delta_(k+1) <= (1 + L_k) e^(Lambda_k) M_k + (eta_k + 2 eps'_k) <= e^(Lambda_(k+1)) (M_k + eta_k + 2 eps'_k)
                = e^(Lambda_(k+1)) M_(k+1),
using 1 + L_k <= e^(L_k) and e^(Lambda_(k+1)) >= 1. Induction on k up to K_B. QED

**Sizes (PROVED, elementary, given the account's sizes).** For the pin run, x^Theta at level k is at least
X + lambda (n - k) - 2c_2 (pairwise increment bound on Theta_X-runs, first hypothesis of `9.9:def-tuned-hypotheses`,
III:57249-57253; RT Theorem `rt:thm-frozen-tuning` proves the same spacing with (1/2) c_0, (3/2) c_0 on the frozen frame). With
L_k <= C theta^(-3/2) (log theta)^(p_0) at theta = X + lambda m - 2c_2, m = n - k, and the bound
    integral from Y to infinity of s^(-3/2) (log s)^p ds <= 4 Y^(-1/2) (log Y)^p   for Y >= e^(4p)
(on s >= Y, (log s)^p s^(-1/4) decreases, so the integrand is at most (log Y)^p Y^(-1/4) s^(-5/4)), one gets
Lambda <= C' (X - 2c_2)^(-1/2) (log X)^(p_0) uniformly in n, which tends to 0 as X grows; likewise
sum eps'_k <= C'' X^(-(kappa_0 - 6)/2) for kappa_0 > 6. So e^Lambda <= 2 for X large, and the defect of Lemma GR is
at most 2 (sum_k eta_k) + O(X^(-2)) at kappa_0 >= 10: **all of it comes from (FC)**.

**Corollary SC-pin (PROVED GIVEN (G1)-(G5) on the pin runs).** Let run A be the pin run (Theta_X-run of length n from
a_n, which exists, is alive and has depth-0 coupling X exactly, Theorem 3.1 (v-a)) and run B the own-threshold run of
clause (0) from a_n. Then |x^own_k(a_n) - x^Theta_(n-k)| <= varpi_n := e^Lambda M for every level k <= min(n, K(a_n, g)).
This is the account's scaffold comparison at the pins, with an explicit modulus. The same proof on the window, with
run A the Theta_X-run from a_n - w, gives it for |w| <= varrho_2/2 wherever (G1)-(G5) hold there.

**Lemma OFF' (PROVED GIVEN Corollary SC-pin, the pairwise increment bound of the pin run, and clause (0)).**
Put D' := ceil((B^sharp + 2c_2 + varpi_n)/lambda) and D'' := ceil(max(0, varpi_n + c_5 - B^sharp)/lambda^sharp). Then
the first-passage depth K_0(n) := K(a_n, g) satisfies n - D' <= K_0(n) <= n + D''; if varpi_n + c_5 <= B^sharp, then
K_0(n) <= n.
*Proof.* Upper bound. Suppose K_0 := K_0(n) > n. Then the own-threshold run of a_n reaches level n without passing, so
min(n, K_0) = n and Corollary SC-pin at level n gives x^own_n <= x^Theta_(0) + varpi_n = X + varpi_n. If D'' = 0, then
varpi_n <= B^sharp - c_5 <= B^sharp, so level n is a passage, a contradiction; hence K_0 <= n. If D'' >= 1 and
K_0 >= n + D'', clause (0)'s flow bound, valid for n <= n + D'' <= K_0, gives
x^own_(n+D'') <= x^own_n - lambda^sharp D'' + c_5 <= X + varpi_n + c_5 - lambda^sharp D'' <= X + B^sharp,
a passage at level n + D'', so K_0 <= n + D''. Lower bound. Suppose K_0 <= n - D' - 1. Corollary SC-pin applies at level
K_0 (K_0 <= min(n, K_0)), and the pairwise bound with (i, j) = (K_0, n) gives
x^own_(K_0) >= x^Theta_(n-K_0) - varpi_n >= X + lambda (n - K_0) - 2c_2 - varpi_n >= X + lambda (D' + 1) - 2c_2 - varpi_n
> X + B^sharp, which contradicts the passage at K_0. QED
The offset delta_n := n - K_0(n) lies in {-D'', ..., D'}. In Corollary OFF-1 of row 1256 the pin datum read with reference
length L^(K_0(n)) has torus exponent m_0 + delta_n, so m_0 >= D'' plus the account's torus floor keeps every reading
admissible; the pigeonhole then runs over this finite set.

**Correction to row 1256 (self-correction, same model; not an independent check).** Row 1256's Lemma OFF took clause
(0)'s flow bound at levels up to n, but clause (0) gives it only for 0 <= i <= j <= K, K the first passage (I:2533-2543,
III:68709-68712). Under exact (FI) at every level the bound up to n holds with the pin run's constants, so its offset
bound becomes D_* = ceil((B^sharp + 2c_2)/lambda) (the case varpi_n = 0 of Lemma OFF', where D'' = 0 when
c_5 <= B^sharp), not ceil((B^sharp + c_5)/lambda^sharp). Corollary OFF-1 is otherwise unchanged.

**3.3 What this changes in the one-cutoff carry (PROVED from 3.2 and row 1256).**
- On the pin route (row 1256 Proposition PIN with Lemma OFF and Corollary OFF-1), (FI) at pins is replaced by
  Corollary SC-pin with any modulus varpi_n bounded uniformly in n (Lemma OFF'); by Lemma GR that holds once (G1)-(G5)
  hold along the pin runs, and (G1), (G2), (G4) are per-frame statements the account (as its tuned-family hypothesis)
  and EM state for one frame. **The one new input is (FC) along the pin runs, with sum_k eta_k bounded uniformly in n.**
  No (MON) is needed on the pin route (row 1256 4.2).
- The account's own uses of the scaffold comparison (2.2: Theorem 3.1 (v-c)(2), `9.8:cor-subsequential-limits` (a),
  `9.8:rem-increment-bound` step (*), `9.13:prop-limit-member`) read the same statement on windows; Lemma GR reduces
  each of them to (FC) on the window runs, with varpi = e^Lambda M in place of the undefined varpi(g).
- What (FC) is (ARGUED). At one step and at fixed weights, it compares two exact rewritings of one effective density that
  differ in the frame's choices: lattice partitions, Gaussian references, fluctuation coordinates and tests (EM L504).
  A proof has to show that the formed unmarked coefficient moves by a summable amount when these choices move from
  theta_j to the run's own weight, a relative change of order theta_j^(-1/2) polylog along tuned runs (2.1). That is a
  statement about Balaban's step itself (chapter 4 of the account, EM's formation), not about the flow; I do not attack it
  here. If the choices enter only through thresholds of large-field events, eta_k would be of the size of those events'
  weights and summable; if a discrete choice (a cube size) jumps between theta_j and w_j, (FC) needs a separate
  comparison at that step. Both are GUIDE readings, not proofs.

## Step 4. State after this row (written 2026-11-20T11:40Z by date -u)

**4.1 Record check (rule 0a).** Grep of `library/`, `parts/`, `library/open-core.md` and FINISH.md for "scaffold
comparison", "cross-scaffold", "own-threshold", "own threshold", "frozen frame", "Gronwall", "frame change": no earlier
row treats the comparison of clause (0)'s own-threshold run with the frozen-scaffold runs. Row 1256 named (FI) and (MON)
(`gap-mini-solve-af-opus.md` 3.4, 4.1-4.2). The "frame-change BLOCK" of rows 392, 404, 421 (`library/fc.md`, `fc-r2.md`)
is the complex gauge frame of the hard core's charts, a different object. `open-core.md` (hard-core synthesis) has no
match. So the reading of 2.2, Lemma GR, Corollary SC-pin and Lemma OFF' are new against the record as far as these
greps show.

**4.2 Labels.**

| Statement | Label | Rests on |
|---|---|---|
| Four-dimensional SU(2) Yang-Mills has a mass gap (Jaffe and Witten) | OPEN; not proved, nothing disproved | |
| The infrared seed at the base datum ((N-phys); (SL)/(RR) of row 1258) | OPEN; not attacked (0.3) | |
| 1.3, 2.1: (FI) at pins compares two runs from one bare datum: the own-threshold run of clause (0) and the run on the frozen scaffold Theta_X, whose choices sit at theta_r = X + c_0 r while its couplings drift from theta_r by up to order theta_r^(1/2) polylog | READ | III:55764-55768, III:68946-69030, III:70175-70230, I:2836-2838 |
| 2.2: the account's "scaffold comparison" (|x^own - x^Theta| <= varpi(g) <= 1 at every level) is (FI) with a bounded defect; it is used in Theorem 3.1 (v-c)(2) via `9.8:cor-subsequential-limits` (a), in `9.8:rem-increment-bound` (*), and in `9.13:prop-limit-member`, and is stated and proved nowhere in CA-I, CA-II, CA-III at 31a47c543775, nor in YM4_RT or YM4_EM at c7fef8b21b58 | READ (greps; a search that finds nothing is evidence of absence only for the strings searched) | 2.2, 3.0 |
| 2.4: calibration by the two-point witness cannot bound the defect (ratio x^B/x^A only within [0.387, 2.582]) | PROVED, elementary | II:71279-71372 |
| Lemma GR: (G1)-(G5) imply |x^Theta - x^own| <= e^Lambda sum_k (eta_k + 2 eps'_k) at every level up to min(n, first passage) | PROVED (discrete Gronwall), as an implication | (G1), (G2), (G4) per-frame statements (account: tuned-family hypothesis `9.9:def-tuned-hypotheses`, Remark `9.9:rem-curvature-scope` (3); EM Theorem `em:thm-coefficient-envelope`, Corollary `em:cor-coefficient-slopes`); (G3) = (FC) OPEN |
| Sizes: Lambda <= C (X - 2c_2)^(-1/2) (log X)^(p_0), sum eps'_k = O(X^(-(kappa_0-6)/2)) uniformly in n | PROVED, elementary, given the account's sizes e_k, v_k and the pairwise increment bound | III:55780-55800, III:57249-57253 |
| Corollary SC-pin (the scaffold comparison at the pins, modulus e^Lambda M) | PROVED GIVEN (G1)-(G5) along the pin runs | Lemma GR |
| Lemma OFF' (the first-passage depth of a_n satisfies n - D' <= K_0(n) <= n + D'', D' = ceil((B^sharp + 2c_2 + varpi_n)/lambda), D'' = ceil(max(0, varpi_n + c_5 - B^sharp)/lambda^sharp)) | PROVED GIVEN Corollary SC-pin, the pin run's pairwise increment bound and clause (0)'s flow bound | III:57249-57253, I:2533-2543 |
| Correction to row 1256 Lemma OFF (clause (0)'s flow bound is used beyond the first passage; with exact (FI) the offset is ceil((B^sharp + 2c_2)/lambda)) | PROVED (self-correction, same model) | I:2533-2543 |
| 3.3: on the pin route (FI) is replaced by (FC) along the pin runs; (MON) is not needed there | PROVED from Lemma GR, Lemma OFF', row 1256 | |
| 3.3: what (FC) is and why it is a statement about Balaban's step itself | ARGUED; the size readings are GUIDE | EM L504 |
| (FC): one-step frame change of the unmarked total at fixed weights, summable in the level | OPEN; not attacked (stop rule: two reductions, (FI) to (SC-pin) to (FC)) | |

**4.3 The one-cutoff carry on the pin route after this row.** Inputs: the base seed at one pin (OPEN, the infrared
crux); the 9.1 comparison's hypotheses (a)-(e) at u = 0, (e) = `9.1:prop-blind-site-expansions` OUTSTANDING in the
account; (DET)'s inputs; (V9) at pins (row 1255, check 1263 running); the account's premises; and, in place of (FI),
(FC) along the pin runs together with the per-frame statements (G1), (G2), (G4), which the account takes as its
tuned-family hypothesis. (MON) is off the pin route. Nothing here touches the T0 chain.

**4.4 A route note for the lead (ARGUED, unchecked; not a proof).** Run B of Lemma GR is itself a frozen-frame run,
with frame equal to its own couplings (3.1). The account's tuned family converges on each torus without passage to
subsequences (Theorem 3.1 (ii-T-a)), while its first-passage family converges only along subsequences (ii-T-b). If the
gap consumer read the tuned family instead of first-passage data, the carry would need no (FC) at all. The price is an
infinite-volume limit along tuned data: the account states (ii-R^4) along first-passage data only (I:2684-2700). Which
of the two to pay is a route decision for `library/route-decisions.md`, not a lemma.

**4.5 Credits.** Ethan Sussman and Levent Alpoge's complete account at 31a47c543775 (CA-I, CA-II, CA-III) and their
component manuscripts YM4_RT and YM4_EM at c7fef8b21b58, with Claude and Codex as authors of their text: the two frames,
the scaffold, the tuned family, the fine bookkeeping of the running-shift statement, the memory bound, the two-point
witness theorem, and the account's own uses of the scaffold comparison; EM's Lemma `rt:lem-polydisc-slope` (in RT) and
Corollary `em:cor-coefficient-slopes` for the polydisc Lipschitz bounds. Balaban's renormalization group (CMP 109
(1.22), (3.61); CMP 119 (3.61)), as the account cites it. The lane's rows 1233, 1255, 1256 and check 1242 for the
one-cutoff carry. Checked by no one. A cross-provider check of 2.2 (the reading that the scaffold comparison is stated
nowhere), Lemma GR, Corollary SC-pin and Lemma OFF' is the natural next step. Lead note: 2.2 is a claim about another
group's text; nothing goes outward without the owner.

No numeric run. No subagent. Sources fetched by URL into a scratch folder outside the repository; nothing fetched is
committed.

## Step 5. Where the frame enters one step: the shape of (FC) (written 2026-11-20T11:42Z by date -u; READ, then GUIDE)

**5.1 READ (YM4_EM at c7fef8b21b58).** EM's actual step is
E_(k+1)[x_k, f](W) = log integral K_(k,theta_k)(W, dV) exp(-x_k A(U_k(V)) + S_f(U_k(V))) + x_k A(U_(k+1)(W)) - S_f(U_(k+1)(W))
(em:eq-actual-step, EM L560-568), where K_(k,theta_k) "is the fixed all-small-field kernel on M(V) = W. It uses the
given fibre density, gauge weight and fluctuation cut" (EM L544-546). The action weight enters the Gaussian part only
through tau_k = x_k/theta_k, by the exact rewrite (em:eq-frozen-gaussian-rewrite, EM L584-588) and the scalar multipliers
tau_k^(-d/2), tau_k^(d_g/2); the first belongs to the field-independent scalar v_(k+1), which "has zero curvature
coefficient" (EM L575-577). EM's one-step inputs hold "the lists and all discrete choices ... fixed throughout each such
domain", the cut is "a fixed Borel restriction in the real free variables", "invariance of an arbitrary gauge-fixing
weight is not assumed", and "the creation radius is c_e varepsilon(theta_k) ... where varepsilon is the supplied real
curvature threshold" (EM L611-655). EM's introduction: "the actual one-step theorem [is a premise] of this manuscript"
(EM L166-168), and companions are required to agree "for the same frame and weights" (EM L253-254).

**5.2 What (FC) therefore compares (ARGUED from 5.1).** At fixed weights w and inherited list, the two frames phi^A
and w (self-calibrated) change four things in one step: (i) the sharp fluctuation cut, at the threshold of theta_k or of
w_k; (ii) the relative gauge weight, which on a cut that is not gauge invariant does not integrate out; (iii) discrete
choices (partitions, lists) where they depend on the frame; (iv) the creation radius (this changes only the bounds: a
curvature coefficient of one analytic family does not depend on the radius at which it is read). The Gaussian-number
part b^0 and the tau-multipliers do not contribute to the curvature coefficient beyond what 5.1 already separates.
So (FC) splits into a **cut-comparison estimate** for the all-small-field kernel (items (i), (ii)) and a **partition
matching** at the steps where a frame-dependent discrete choice differs between theta_k and w_k (item (iii)).

**5.3 GUIDE (no proof).** Along tuned runs |theta_k - w_k| is at most of order theta_k^(1/2) polylog (2.1), a relative
change of order theta_k^(-1/2) polylog in the threshold. If the cut sits at a Gaussian-tail threshold of polylogarithmic
size, the fluctuations between the two cuts carry a weight that decays faster than any power of theta_k, and their
curvature coefficient, read at EM's extraction cost of order theta_k (log theta_k)^(-2q) (proof of EM Theorem
`em:thm-coefficient-envelope`, EM L1385-1390), would still be summable in k. A discrete choice that jumps between theta_k
and w_k is a separate matter; its count along a run is not bounded by anything read here. Neither statement is proved.
This is a pointer for a row that attacks (FC), not an input.

**5.4 Stop.** (FI) was reduced twice: to the weaker (SC-pin) with any bounded modulus (2.3, Lemma OFF'), then to the
one-step (FC) (Lemma GR). One route to (SC-pin) was attacked and fails at its first step (2.4). By the stop rule
(FINISH How we work, item 4) the row ends here and reports (FC) as the named open statement.

Status: complete (Steps 0-5 and RESULT, appended step by step).

RESULT: Row 1260 (Claude Opus 5.5 max, Mac mini worker 2, 11:17Z-11:44Z by date -u; author only, checked by no one; no numeric run, no subagent). The Jaffe-Witten mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved; the infrared seed ((N-phys), (SL)/(RR) of row 1258) stays OPEN and was not attacked (no session-sized route off the record). Worked item: (FI) of the one-cutoff carry (row 1256), which no row had attacked. READ in Sussman and Alpoge's complete account at 31a47c543775 (with Claude and Codex as authors of its text; after Balaban): (FI) compares two runs from one bare datum, the own-threshold run of clause (0) and the run on the frozen scaffold theta_r = X + c_0 r whose couplings drift from the scaffold by up to order theta_r^(1/2) polylog; the account uses exactly this comparison under the name "the scaffold comparison" (|x^own - x^Theta| <= varpi(g) <= 1 at every level) in Theorem 3.1 (v-c)(2) via 9.8:cor-subsequential-limits (a), in 9.8:rem-increment-bound (*) and in 9.13:prop-limit-member, but states and proves it nowhere in CA-I to III, and their newer YM4_RT and YM4_EM (c7fef8b21b58) treat one frame at a time ("First passage is defined separately for the self-calibrated trajectory"). PROVED (elementary): calibration by the account's two-point witness theorem cannot bound the defect (relative error 1/4 fixes x only within a factor 2.6). PROVED as an implication (Lemma GR, discrete Gronwall): the scaffold comparison holds with modulus e^Lambda sum_k (eta_k + 2 eps'_k), Lambda = O(X^(-1/2) polylog) uniformly in the cutoff, given the per-frame coefficient bounds (the account's tuned-family hypothesis 9.9:def-tuned-hypotheses, or EM Theorem em:thm-coefficient-envelope and Corollary em:cor-coefficient-slopes) and one new one-step input (FC): forming the unmarked coefficient on the frozen frame or on the run's own frame, at the same weights, changes it by eta_k with sum_k eta_k bounded. PROVED GIVEN that (Corollary SC-pin, Lemma OFF'): the first-passage depth of the pin a_n lies between n - ceil((B^sharp + 2c_2 + varpi)/lambda) and n + ceil(max(0, varpi + c_5 - B^sharp)/lambda^sharp), so on the pin route (FI) is replaced by (FC) and (MON) is not needed; this also corrects row 1256's Lemma OFF, which used clause (0)'s flow bound beyond the first passage. GUIDE: (FC) splits into a cut-comparison estimate for EM's all-small-field kernel and a partition matching. OPEN: (FC); the infrared seed; the 9.1 hypothesis (e); (DET)'s inputs; (V9) at pins; the account's premises; the mass gap. Output library/gap-mini-solve-ai-opus.md.
