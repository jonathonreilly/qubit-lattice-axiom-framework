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

**2.4 How the cut enters the fluctuation integral (READ, written 2026-11-20T13:09Z by date -u).**
- *The regular step.* The account's proof of torus independence (Lemma 4.38:prf-proof-non-wrapping, "the ingredients of
  the localized series", I:58640-58730) lists every object of a localized term Psi_X of Balaban's one-step expansion. One
  item (I:58716-58717): "The factors chi^(k), the signs of [B-CMP116 (2.3)], and d mu_0. They are products over bonds; off
  Z the Gaussian integrates to 1." The cutoff chi^(k) is that of [B-CMP119 (3.16)], at the threshold delta_k (I:148959,
  I:149138-149142); the second cutoff chi'_k "restricts the approximate fluctuation fields" (I:149163; [B-CMP119 (3.3)]).
- *The same expansion written out by the account.* In a large-field stage (Section 4.24) the account carries out "the
  first step of the cluster expansion" of CMP 116 itself (Lemma 4.24:prf-counted-once, I:108483-108507): the Mayer
  expansion [B-CMP116 (2.1)], e^V - 1 = int_0^1 dt V e^(tV) (also I:20620-20626); then "the decomposition [B-CMP116 (2.3)]"
      chi^s = chi_(Y_0) sum_(P subset s) (-1)^|P| chi^c_P,                                              (2.2)
  with Y_0 the bonds of the supports of the Mayer elements and chi^c_P the product over b in P of the characteristic
  functions complementary to the condition |phi(b)| < T_j (I:108531-108533); then conditioning, whitening and decoupling
  ([B-CMP116 (2.5)-(2.8)]), "algebra and Fubini's theorem". One term T(D, P, Z) has integrand
  G_T = (-1)^|P| chi_(Y_0) chi^c_P prod_(e in D) (e^(v_e) - 1) (I:108534-108536) and obeys (Lemma 4.24:prf-single-term,
  I:108508-108519)
      |T(D,P,Z)| <= prod_(e in D) 2 nu(e) * exp(-(1/2) gamma_2 T_j^2 |P|) * exp(-(kappa_1 - 1)|Z \ Z_0|) * exp(c_F |Z|).   (2.3)
  The factor exp(-(1/2) gamma_2 T_j^2 |P|) comes from chi^c_P <= prod_(b in P) exp(-(1/2) gamma_2 T_j^2 + (1/2) gamma_2 |phi(b)|^2),
  the Gaussian factor being absorbed into the Gaussian measure (I:108574-108584); chi_(Y_0) and the signs enter only through
  modulus at most 1 (I:108584-108585); the Mayer factors are bounded by 2 nu(e) on the real support of the cut
  (I:108547-108570).
- *The logarithm.* The account's abstract polymer system (Definition 4.6:def-abstract-polymers, I:21900-21946: finite
  polymer set, reflexive symmetric incompatibility, Ursell coefficients rho^T, partition function Xi, logarithm series Phi)
  and Lemma 4.6:lem-exponential-formula (exp Phi = Xi under absolute convergence), with the convergence theorem "proved
  below in this section" (I:21942-21944); the formula is [B-CMP116 (2.11)-(2.13)].

**2.5 What 2.4 gives (READ, my reading of the account's text).** In the expansion that the account reads in Balaban's CMP
116, the small-field threshold enters a term only through two kinds of factor: the kept cut chi_(Y_0) on the bonds where
Mayer elements sit, and the complementary indicators chi^c_P with sign (-1)^|P|. Everything else in a term (the Mayer
factors at fixed weights and list, the Gaussian measure, its conditioning, whitening and decoupling, the propagators) is
the same at any threshold. This is the structure row 1267 4.5 asked for ("cut integral = cut-free part + cut corrections").
Caveat: for the regular step this is the account's listing of ingredients (I:58716), not a printed term-by-term proof;
the written-out form (2.2)-(2.3) is the account's large-field stage of Section 4.24. Balaban's CMP 116 is not read here
(Project Euclid bot check, row 1264).

**2.6 EM's one-step inputs and the cut (READ, written 2026-11-20T13:15Z by date -u).** Source: Sussman and Alpoge, `YM4/EM/YM4_EM.tex`
at c7fef8b21b58 (2001 lines; fetched by URL into the scratch folder; credit as in 2.1). EM input (1) (EM:612-626): "In the
analytic integral presentation the sharp test is a fixed Borel restriction in the real free variables." EM input (3)
(EM:665-689), for one list: ||F_(k+1)[f]|| <= K {delta(theta_k) + s N_k + exp(-c theta_k delta(theta_k)^2)}; the last
term is the size EM budgets for the cut. EM input (4) (EM:707-716) compares two lists "for the same completed fibre
map, potential and cut domains and logarithm expansion". EM's norm (EM:223-229) is a weighted supremum,
||G||_(j,kappa;a) = sup_(torus, X, z in X) e^(kappa d_j(X)) sup_(P in U_j(X;a)) |G(X,P,z)|, so it is monotone: a
pointwise bound |H| <= c |G| on the cores gives ||H|| <= c ||G||. **No EM input compares two cuts.** (FC-T) asks for
exactly such an input. This row states it (Section 3), derives it from the term structure of 2.4 (Lemma TL), and sums it
(Lemma S).

## Step 3. Statements (written 2026-11-20T13:15Z by date -u)

**3.1 Setting.** Fix a level k of a pin run, the weight x_k, the unmarked list f, and two frame entries phi_k (frozen
scaffold) and psi_k (the run's own), both with |x_k/theta - 1| < sigma_*/2 <= 1/4. Put theta_k := min(phi_k, psi_k).
By row 1267 (Lemma A, Lemma Z, Lemma AX, Proposition SPLIT, 4.4) the two unmarked totals differ only through the
frames' kernels, and at fixed weights the frame enters the kernel through presentations (exact rewritings) and the cut.

**Hypothesis (G) (orbit-invariant cut).** In each frame the all-small-field sharp test is a function of the G_res-orbit
of the fibre configuration (for example, read on the exact axial representative, or gauge averaged as CA-I 4.35 (C)(b)
says the account does "wherever a representative after a reversed Faddeev-Popov step is read", I:157496-157500).
Under (G), Lemma AX (iii) of row 1267 removes every gauge weight, so each frame's integral equals the integral in ONE
common presentation (that of psi: its fibre chart, Gaussian reference, splitting, gauge device, localization partitions
and decoupling) with that frame's own cut. In the common chart write the two cuts as
    chi^i = prod_(u in U) 1[N_u < T^i_u],   i = 1 (frame phi), i = 2 (frame psi),                     (3.1)
over a finite set U of test units (bonds or cubes of the real free array), with Borel N_u >= 0. Put
T_lo := min_(u, i) T^i_u, and assume the cuts are nested (T^1_u >= T^2_u for all u, or <= for all u; this holds when
every threshold is a fixed multiple of the frame's delta, as in (2.1)).

**Hypotheses (E0)-(E5): the supplier's one-step expansion, as the account reads Balaban's CMP 116 (2.4 above).** All
bounds hold for every outer datum P in the output cores of EM's norm (complex cores included), with constants uniform in
k, in the torus and in the list.
- (E0) *Common expansion.* For i = 1, 2 the supplier's construction, run in the common presentation with the cut chi^i,
  applies with the same constants (both thresholds lie in the range where the construction holds: above the floor of
  [B-CMP116 (2.31)] and inside the fluctuation domain [B-CMP119 (3.43)]; cf. the two conditions of CA-I Theorem
  4.3:thm-small-field-step, I:4166-4180).
- (E1) *Term structure* ([B-CMP116 (2.1), (2.3), (2.5)-(2.8), (2.11)-(2.13)] as read at I:58716-58717, I:108483-108507,
  I:21900-21946). The interacting integral of test i is a polymer gas Xi^i on a finite polymer set and an
  incompatibility relation that do not depend on i, with activity F^i(X) = sum_(t in Data(X)) Lambda_t[G^i_t]. The index
  set Data(X) and the linear functionals Lambda_t (Gaussian integration with conditioning, whitening, decoupling and
  Cauchy extraction) do not depend on i, and
      G^i_t = sigma_t chi^i_(Y_0(t)) chi^(c,i)_(P(t)) M_t,   M_t := prod_(e in D(t)) (e^(v_e) - 1),               (3.2)
  with sigma_t in {-1, +1}, chi^i_Y := prod_(u in Y) 1[N_u < T^i_u], chi^(c,i)_P := prod_(u in P) 1[N_u >= T^i_u], and
  Y_0(t), P(t) disjoint sets of test units. The output's interacting part localized at Y is the Ursell sum
      Phi^i(Y) := sum_(n>=1) (1/n!) sum_((X_1,...,X_n): X_1 u ... u X_n = Y) rho^T(X_1,...,X_n) prod_p F^i(X_p).        (3.3)
- (E2) *Mayer bound.* For every t and e in D(t): |e^(v_e) - 1| <= 2 nu(e) on the real support of
  prod_(u in Y_0(t)) 1[N_u < max_i T^i_u].
- (E3) *One-term bound with a tail set* (the account's "general one-term bound" with Gaussian weight parameter gamma_2
  and its absorption bound, I:108537-108600). There are c_A >= 0, gamma_2 > 0 such that for every t, every set Q of test
  units in Y_0(t) u P(t) and every Borel G with |G| <= m prod_(u in Q) e^((1/2) gamma_2 N_u^2) on the real integration
  domain, |Lambda_t[G]| <= m e^(c_A |Q|) w(t), where w(t) := e^(-(kappa_1 - 1)|Z \ Z_0|) e^(c_F |Z|) (I:108508-108519).
- (E4) *Convergence margin.* For some eps in (0, 1] the majorant activity e^eps Fbar, with
      Fbar(X) := sum_(t in Data(X)) (1 + |Y_0(t)|) e^(c_A (|P(t)| + 1)) e^(-(1/2) gamma_2 T_lo^2 (|P(t)| - 1)_+) prod_(e in D(t)) 2 nu(e) w(t),
  satisfies the account's convergence criterion for the logarithm series (I:21942-21944), so that
  Bbar(Y) := sum_n (1/n!) sum_(union = Y) |rho^T| prod_p e^eps Fbar(X_p) is finite, and the pointed family built from
  Bbar with the supplier's pointing has EM norm at most Nbar.
- (E5) *Common post-processing.* The unmarked output's interacting part is obtained from Phi^i by linear operations that
  do not depend on i (scalar separation, vacuum subtraction, pointing, re-localization to the absolute core, the
  counterterm), bounded by C_post in EM's norms.

(E4) asks for slightly more room than the one-test convergence: the factor (1 + |Y_0|) <= prod_(e in D) e^(b |supp e|)
is absorbed into the element weights as the account absorbs e^(c_F |Z|) in (I:108520-108526), and one bond of P loses its
tail factor. (E5) is the form of EM:563-581 and EM:665-700.

**3.2 Lemma TL (two-test Lipschitz bound; PROVED in Step 4 given (E1)-(E4)).** Put eta := exp(-(1/2) gamma_2 T_lo^2).
(a) |F^i(X)| <= Fbar(X) for i = 1, 2, and |F^1(X) - F^2(X)| <= 2 eta Fbar(X), for every polymer X.
(b) |Phi^1(Y) - Phi^2(Y)| <= (2 eta/eps) Bbar(Y) for every Y; the series (3.3) converge absolutely.
(c) Hence the localized difference H := Phi^1 - Phi^2 has EM norm at most (2/eps) eta Nbar.

**3.3 Corollary TC (two-cut comparison; PROVED given (G), (E0)-(E5)).** At step k,
    |||T(E^phi_(k+1)[f]) - T(E^psi_(k+1)[f])|||_(k+1) <= nu_k := (2/eps) C_post Nbar exp(-(1/2) gamma_2 T_lo(k)^2).

**3.4 Lemma S (summability; PROVED in Step 4).** Let a > 0, p_0 >= 1 an integer, X >= 3, c_0 > 0, gamma_2 > 0, and suppose
T_lo(k) >= a (log theta_k)^(p_0) with theta_k >= (X + c_0 (n - k))/3 for 0 <= k < n. Put alpha := gamma_2 a^2/2,
y_* := exp((2/alpha)^(1/(2 p_0 - 1))) and Y(r) := (X + c_0 r)/3. Then
    sum_(k<n) exp(-(1/2) gamma_2 T_lo(k)^2) <= S(X) := sum_(r>=1) exp(-alpha (log Y(r))^(2 p_0)),
S(X) is finite and independent of n, and S(X) <= 9/(c_0 X) once X >= 3 y_*. (Corrected in Step 4: an earlier line here
read 3/(c_0 X) and omitted X >= 3.)

**3.5 Theorem FCT (PROVED given (G), (E0)-(E5) at every step with uniform constants, and (TH) below).** (FC-T) of row
1267 holds along the pin runs with nu_k of 3.3 and sum_(k<n) nu_k <= (2/eps) C_post Nbar S(X), uniformly in n, and the
bound tends to 0 as X tends to infinity. With row 1267's Proposition FC-chain (given its (H1)-(H3), (H5)) the unmarked
coefficients of the two frames satisfy sum_k eta_k <= 2 C_x (2/eps) C_post Nbar S(X).
(TH) *Threshold identification.* In the common chart every threshold is at least a (log theta_k)^(p_0) with a > 0
fixed. READ: frame theta's cut radius in its own normalized field is (A_1/A_0) p_0(g_theta) = A_1 (log theta)^(p_0)
(I:4172-4175, (2.1)); the frame-phi field in psi's normalization is rescaled by (psi_k/phi_k)^(1/2) >= 3^(-1/2) on
|x_k/theta - 1| < 1/4; so a = A_1/3^(1/2) works if the cut units are the normalized field variables. p_0 is a natural
number with p_0 >= 5r (I:1351), so p_0 >= 1. Along a pin run theta_k is at least (X + c_0 (n-k))/3 because the frozen entry
is X + c_0 (n - k) (row 1267 3.3) and both entries are within the factor (1 + 1/4)/(1 - 1/4) < 3 of x_k.

## Step 4. Proofs (written 2026-11-20T13:17Z by date -u)

**4.1 Proof of Lemma TL.** Fix a polymer X and t in Data(X); write Y_0 = Y_0(t), P = P(t), D = D(t),
fbar_t := (1 + |Y_0|) e^(c_A(|P|+1)) e^(-(1/2) gamma_2 T_lo^2 (|P|-1)_+) prod_(e in D) 2 nu(e) w(t), so Fbar(X) = sum_t fbar_t.
All statements are symmetric in the labels 1, 2, so assume T^1_u >= T^2_u for every u. Then
1[N_u < T^2_u] <= 1[N_u < T^1_u], hence chi^2_Y <= chi^1_Y and chi^(c,1)_P <= chi^(c,2)_P, and max_i T^i_u = T^1_u, so the
support named in (E2) is the support of chi^1_(Y_0). Two elementary facts are used:
(F1) for every u, i and real configuration, 1[N_u >= T^i_u] <= exp((1/2) gamma_2 (N_u^2 - (T^i_u)^2)) <= eta exp((1/2) gamma_2 N_u^2),
since the middle term is at least 1 where N_u >= T^i_u and positive elsewhere, and T^i_u >= T_lo;
(F2) for numbers b_1, ..., b_m in {0, 1}: 1 - prod_j b_j = sum_(j=1)^m (prod_(l<j) b_l)(1 - b_j), each summand in {0, 1}.

*(a), one test.* Let i in {1, 2}. Where chi^i_(Y_0) = 0, G^i_t = 0. Where chi^i_(Y_0) = 1, also chi^1_(Y_0) = 1, so
|M_t| <= prod_(e in D) 2 nu(e) by (E2). With (F1) for each u in P,
    |G^i_t| <= [e^(-(1/2) gamma_2 T_lo^2 |P|) prod_(e in D) 2 nu(e)] prod_(u in P) e^((1/2) gamma_2 N_u^2).
(E3) with Q = P gives |Lambda_t[G^i_t]| <= beta_t := e^(c_A |P|) e^(-(1/2) gamma_2 T_lo^2 |P|) prod_(e in D) 2 nu(e) w(t). Since
1 <= 1 + |Y_0|, e^(c_A|P|) <= e^(c_A(|P|+1)) and |P| >= (|P|-1)_+, beta_t <= fbar_t. Summing over t, |F^i(X)| <= Fbar(X).

*(a), difference, P nonempty.* |Lambda_t[G^1_t] - Lambda_t[G^2_t]| <= 2 beta_t = 2 eta e^(c_A|P|) e^(-(1/2) gamma_2 T_lo^2 (|P|-1)) prod 2 nu(e) w(t)
<= 2 eta fbar_t.

*(a), difference, P empty.* Then chi^(c,i)_P = 1 (empty product) and G^1_t - G^2_t = sigma_t M_t (chi^1_(Y_0) - chi^2_(Y_0)).
Enumerate Y_0 = {u_1, ..., u_m} and put b_j := 1[N_(u_j) < T^2_(u_j)]. Because chi^2_(Y_0) <= chi^1_(Y_0) are indicators,
chi^1_(Y_0) chi^2_(Y_0) = chi^2_(Y_0), so chi^1_(Y_0) - chi^2_(Y_0) = chi^1_(Y_0)(1 - prod_j b_j), and by (F2)
    G^1_t - G^2_t = sum_(j=1)^m g_j,   g_j := sigma_t M_t chi^1_(Y_0) (prod_(l<j) b_l)(1 - b_j).
On the support of g_j, chi^1_(Y_0) = 1, so |M_t| <= prod 2 nu(e) by (E2), and by (F1)
|g_j| <= eta prod_(e in D) 2 nu(e) e^((1/2) gamma_2 N_(u_j)^2). (E3) with Q = {u_j} and linearity of Lambda_t give
|Lambda_t[G^1_t - G^2_t]| <= sum_j |Lambda_t[g_j]| <= |Y_0| eta e^(c_A) prod 2 nu(e) w(t) <= eta fbar_t
(for P empty, fbar_t = (1 + |Y_0|) e^(c_A) prod 2 nu(e) w(t)).

Summing the two difference cases over t in Data(X): |F^1(X) - F^2(X)| <= 2 eta Fbar(X). This proves (a).

*(b).* Fix n >= 1 and polymers X_1, ..., X_n; put a_p := F^1(X_p), b_p := F^2(X_p). Then
prod_p a_p - prod_p b_p = sum_(q=1)^n (prod_(p<q) a_p)(a_q - b_q)(prod_(p>q) b_p), so by (a)
|prod a - prod b| <= 2 eta n prod_p Fbar(X_p) <= (2 eta/eps) prod_p e^eps Fbar(X_p), using n < e^(eps n)/eps. By (a),
|rho^T prod_p F^i(X_p)| <= |rho^T| prod_p e^eps Fbar(X_p), and by (E4) the sum of these over n and over n-tuples with union Y,
weighted by 1/n!, is Bbar(Y) < infinity. So both series (3.3) converge absolutely, and subtracting them term by term,
|Phi^1(Y) - Phi^2(Y)| <= sum_n (1/n!) sum_(union = Y) |rho^T| |prod a - prod b| <= (2 eta/eps) Bbar(Y).

*(c).* Point H := Phi^1 - Phi^2 with the supplier's pointing (a linear rule with nonnegative weights, the same for i = 1, 2,
and the one used for Bbar in (E4)). Pointwise |H(Y, P, z)| <= (2 eta/eps) Bbar(Y, z) on the cores (the nu(e) in Fbar are
suprema over the cores). EM's norm is a weighted supremum (2.6), hence monotone, so ||H|| <= (2 eta/eps) Nbar. QED

**4.2 Proof of Corollary TC.** By (G) and row 1267's Lemma AX (iii), each frame's kernel integral equals, up to a
positive constant that does not depend on W, the integral of e^Phi against the G_res-invariant fibre measure with that
frame's cut; the common presentation of psi is an exact rewriting of the same integral (row 1267 Lemma A for the
Gaussian normalizer, Lemma AX for the gauge devices, CA-I 4.35 (C)(b) for the axial and exponential gauge terms). So
T(E^phi_(k+1)[f]) - T(E^psi_(k+1)[f]) = log Xi^1 - log Xi^2 + const, where Xi^i is the interacting integral of test i in the
common presentation (the Gaussian reference, its normalizer and the terms x_k A(U_(k+1)(W)) - S_f(U_(k+1)(W)) of EM
(em:eq-actual-step) are common to i = 1, 2). By the account's Lemma 4.6:lem-exponential-formula (exp Phi = Xi under
absolute convergence, which Lemma TL (b) supplies), log Xi^i = sum_Y Phi^i(Y). By (E5) the two unmarked interacting parts
are L(Phi^1), L(Phi^2) for one linear L with ||L|| <= C_post; by (E0) each is a regular output of the supplier's
construction, and regular families form a linear space (EM:215-218, row 1267 3.1), so L(H) is a regular pointed family
whose total is T(E^phi_(k+1)[f]) - T(E^psi_(k+1)[f]) up to a constant. By the definition of |||.|||_(k+1) (row 1267 3.1)
and Lemma TL (c), |||T(E^phi_(k+1)[f]) - T(E^psi_(k+1)[f])|||_(k+1) <= ||L(H)|| <= C_post (2/eps) Nbar eta = nu_k. QED

**4.3 Proof of Lemma S.** Let 0 <= k < n and r := n - k in {1, ..., n}. Then theta_k >= Y(r) = (X + c_0 r)/3 >= 1
(as X >= 3), so log theta_k >= log Y(r) >= 0 and, 2 p_0 being a positive integer, (log theta_k)^(2 p_0) >= (log Y(r))^(2 p_0).
With T_lo(k) >= a (log theta_k)^(p_0): exp(-(1/2) gamma_2 T_lo(k)^2) <= exp(-alpha (log Y(r))^(2 p_0)). Summing over k < n,
that is over r = 1, ..., n, gives the first claim with the sum extended to all r >= 1. If Y >= y_*, then
alpha (log Y)^(2 p_0 - 1) >= alpha (log y_*)^(2 p_0 - 1) = 2 (here 2 p_0 - 1 >= 1), so alpha (log Y)^(2 p_0) >= 2 log Y and
exp(-alpha (log Y)^(2 p_0)) <= Y^(-2). Only the finitely many r with Y(r) < y_* (r < (3 y_* - X)/c_0) can fail this; each
such term is at most 1. The others are at most 9 (X + c_0 r)^(-2), which is summable in r. So S(X) < infinity, with no n
in it. If X >= 3 y_*, every r >= 1 has Y(r) >= y_*, and since s -> 9 (X + c_0 s)^(-2) decreases,
S(X) <= sum_(r>=1) 9 (X + c_0 r)^(-2) <= int_0^infinity 9 (X + c_0 s)^(-2) ds = 9/(c_0 X). QED

**4.4 Proof of Theorem FCT.** At each step k < n, Corollary TC gives (FC-T) at step k with
nu_k = (2/eps) C_post Nbar exp(-(1/2) gamma_2 T_lo(k)^2), the constants being uniform in k by hypothesis. (TH) gives
T_lo(k) >= a (log theta_k)^(p_0) with theta_k >= (X + c_0 (n - k))/3 along the pin runs (3.5). Lemma S gives
sum_(k<n) nu_k <= (2/eps) C_post Nbar S(X), uniformly in n, and S(X) <= 9/(c_0 X) -> 0 for X >= 3 y_*. Row 1267's
Proposition FC-chain (3.4) then gives sum_k eta_k <= 2 C_x sum_k nu_k <= 2 C_x (2/eps) C_post Nbar S(X). QED

**4.5 What the proofs use and do not use.** Lemma TL and Lemma S use only (E1)-(E4), (F1)-(F2) and arithmetic; no
property of SU(2), of Yang-Mills or of the coupling enters them. The selective content (none here) and the analytic
content (Balaban's expansion) sit in the hypotheses. The size eta_k = exp(-(1/2) gamma_2 a^2 (log theta_k)^(2 p_0)) is
the term exp(-c theta_k delta(theta_k)^2) that EM input (3) already budgets for the cut (2.6), with theta delta^2 =
A_1^2 (log theta)^(2 p_0) by (2.1).

## Step 5. Record check, labels, state of the carry (written 2026-11-20T13:19Z by date -u)

**5.1 Record check (rule 0a).** Greps of `library/*.md`, `library/prior/*.md`, `parts/*.md` and `FINISH.md` for
"two-test", "two-threshold", "two-cut", "two cut", "cut comparison", "threshold comparison", "Lipschitz in the
activit", "difference of two polymer", "two polymer gases", "FC-T", "CMP116 (2.3)", "CMP 116 (2.3)":
- "(FC-T)" in this sense: row 1267 only (`gap-mini-solve-ak-opus.md` 4.5, 5.2-5.6, author). The other "FC-T" hits
  (`fc-r2.md`, `fcon.md`, `assembly-status.md` and others) are name collisions in hard-core files; FINISH.md names row
  1267's open item (FC-1).
- "two-threshold": row 1267; `gap-pe-max.md` L665 (a Peierls ratio, unrelated); `parts/hard-core--mapped.md` L300 (the
  account's two-threshold split at the creating step, a large-field device, not a comparison of outputs).
- "cut comparison": `bz-geom.md`, `bz-own.md` (the account's geometric cut comparison of a joined sequence, Y
  37390-37460: regions, not thresholds), `gap-joint-check-opus.md` L80 (a transfer-matrix decoupling), `gap-fp-astra.md`
  (one-plaquette count); none compares two thresholds of Balaban's small-field step.
- "Lipschitz in the activities", "difference of two polymer", "two polymer gases", "CMP116 (2.3)": no hits before this row.
So Corollary TC, Lemma S and Theorem FCT are new against the record as far as these greps show. Lemma TL is an elementary
fact of the polymer-expansion kind (telescoping plus a majorant); it is written out here because the record has no copy
of it, not because it is new mathematics. Lemma AX, Proposition SPLIT and Proposition FC-chain are row 1267's.

**5.2 Labels.**

| Statement | Label | Rests on |
|---|---|---|
| Four-dimensional SU(2) Yang-Mills has a mass gap (Jaffe and Witten) | OPEN; not proved, nothing disproved | |
| The infrared seed ((N-phys); (SL)/(RR) of row 1258) | OPEN; not attacked (Step 1) | |
| 2.1: the account's threshold is delta_m = A_1 (log g_m^(-2))^(p_0) g_m, so theta delta(theta)^2 = A_1^2 (log theta)^(2 p_0) | READ | I:29060-29120 |
| 2.3: the cited one-step theorem (I:4136-4210) bounds each frame's output separately and says nothing on threshold dependence; separate bounds give a constant per step, not summable | PROVED, elementary | I:4136-4210 |
| 2.4-2.5: in the expansion the account reads in Balaban's CMP 116, the threshold enters only through the kept cut chi_(Y_0) and the signed complements chi^c_P; one complement unit costs exp(-(1/2) gamma_2 T^2) | READ (regular step: list of ingredients I:58716-58717; written out for a large-field stage: I:108483-108600) | account; CMP 116 not read (bot check) |
| 2.6: no EM one-step input compares two cuts; EM input (3) budgets exp(-c theta delta^2) for the cut | READ | EM:612-716 |
| Lemma TL: (E1)-(E4) give |F^1 - F^2| <= 2 eta Fbar, |Phi^1 - Phi^2| <= (2 eta/eps) Bbar, ||H|| <= (2/eps) eta Nbar | PROVED (given (E1)-(E4)) | 4.1 |
| Corollary TC: the two-cut comparison |||T(E^phi) - T(E^psi)|||_(k+1) <= nu_k = (2/eps) C_post Nbar exp(-(1/2) gamma_2 T_lo^2) | PROVED GIVEN (G), (E0)-(E5) | 4.2; row 1267 Lemmas A, AX |
| Lemma S: sum_k exp(-(1/2) gamma_2 a^2 (log theta_k)^(2 p_0)) <= S(X) < infinity, uniformly in n; S(X) <= 9/(c_0 X) for X >= 3 y_* | PROVED, elementary | 4.3 |
| Theorem FCT: (FC-T) of row 1267 along the pin runs with sum_k nu_k <= (2/eps) C_post Nbar S(X), and so sum_k eta_k <= 2 C_x (2/eps) C_post Nbar S(X) -> 0 as X -> infinity | PROVED GIVEN (G), (E0)-(E5) with uniform constants, (TH), and row 1267's (H1)-(H3), (H5) | 4.4 |
| (TH): the thresholds in the common chart are at least a (log theta_k)^(p_0), a = A_1/3^(1/2) | ARGUED (READ I:4172-4175, I:1351; the unit conversion between the two frames' normalized fields is my reading) | 3.5 |
| (E1)-(E3): term structure, Mayer bound, one-term bound with a tail set, for the regular step | READ in the account's large-field stage and ingredient list; for the regular step a reading, not a printed proof | I:58716, I:108483-108600 |
| (E4): convergence with a small extra margin; (E5): common linear post-processing | ARGUED (the account absorbs the same kind of factors at I:108520-108526; EM:563-581, 665-700) | |
| (E0): the supplier's construction applies with one presentation at either threshold | ARGUED (I:4199-4205: couplings enter only through containment and two conditions) | not checked against Balaban |
| (G): the cut is a function of the G_res-orbit | ARGUED, not settled (5.6) | I:157494-157500, I:157566-157572; EM:633-647 |

**5.3 What stays open on this item, stated for the next row.**
- **(FC-G), the gauge-device part, if (G) fails.** If the cut is not orbit-invariant, the frame comparison gains
  log < pi_(w_phi)[chi^phi] / pi_(w_psi)[chi^phi] > (row 1267 (4.1) with one cut and two gauge weights). By Lemma AX (i),
  pi_w[chi] - pi_(w')[chi] = - int du (1 - chi(V^u)) (rho_w(u) - rho_(w')(u)), a tail quantity; but in a common Gaussian
  presentation the ratio w_phi/w_psi is a vertex of size |phi_k/psi_k - 1| (order theta_k^(-1/2) polylog, not a tail),
  whose localized contributions cancel only in sum. A proof must organize that cancellation locally (a Ward identity
  inside the expansion, as EM does for its Gaussian mismatch family G_(k+1,tau), EM:1326-1335). Not done here.
- **(E0)-(E5) against Balaban's text.** CMP 116 is behind a Project Euclid bot check (row 1264); the account cites it by
  statement. A reading of CMP 116 Section 2 (its (2.1), (2.3), (2.5)-(2.13), (2.31), (2.41)) would turn (E1)-(E3) from
  "read in the account" to "read at the source".
- **Bookkeeping of row 1267:** (H2) cross-admission and (H3) the total form of EM input (4).

**5.4 The one-cutoff carry on the pin route after this row.** Row 1260: (FI) at pins reduces to (FC) (Lemma GR). Row
1267: (FC) reduces, through Proposition FC-chain, to the one-step (FC-1), and (FC-1) to (FC-T) (Lemmas A, Z, AX,
Proposition SPLIT). This row: (FC-T) holds with a summable bound that tends to 0 as the scaffold floor X grows, given
(G) and the supplier's expansion in the form (E0)-(E5) (Theorem FCT). So, on the pin route, (FI) now reads: (G) or
(FC-G); (E0)-(E5) as readings of Balaban's CMP 116; row 1267's (H2), (H3), (K). The carry's other inputs are unchanged:
the base seed (OPEN, the infrared crux), the 9.1 hypothesis (e) and 9.1:prop-blind-site-expansions, (DET)'s inputs, (V9)
(row 1275), the account's premises. Nothing here touches the infrared seed or the T0 chain.

**5.5 Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the complete account
CA-I at 31a47c543775 (Theorem 4.3:thm-small-field-step, Definition 4.7:not-running-couplings, Definition
4.15:def-small-field-complement, Section 4.24's written-out first step of the cluster expansion and its single-term bound,
Section 4.38's list of ingredients, Definition 4.6:def-abstract-polymers and Lemma 4.6:lem-exponential-formula) and
YM4_EM at c7fef8b21b58 (the actual step, the one-step inputs, the pointed norm). Tadeusz Balaban: the renormalization
group, its decompositions of unity and its cluster expansion (CMP 109, 116, 119, 122, as the account cites them). Rows
1256, 1260, 1267 of this lane (pins, Lemma GR, Lemmas A, Z, AX, Proposition SPLIT, Proposition FC-chain). Checked by no
one; a cross-provider check of Lemma TL, Corollary TC, Lemma S and Theorem FCT, and of the readings (E1)-(E3) and (TH)
against the cited lines, is the natural next step.

No numeric run (none was needed). No subagent. Sources fetched by URL into a scratch folder outside the repository;
nothing fetched is committed.

**5.6 Reading of (G) (READ and ARGUED, written 2026-11-20T13:20Z by date -u).** CA-I 4.35 (C)(b) (I:157490-157500): Balaban's
representation "is written in the axial gauge [B-CMP119 (1.5)]", uses the exponential gauge-fixing term of [B-CMP109
(1.5), (2.11)] "together with its normalisation", uses the decompositions of unity of [B-CMP119 Section 3], and "the
integrand of each piece is averaged over gauge transformations wherever a representative after a reversed
Faddeev-Popov step is read". The account's reason that the representation is exact (I:157566-157572; row 1267 cites
this passage as I:157620-157627, which at this file holds other text): "for gauge-invariant F, Balaban's display evaluates
int (F o M) d tau ... because the Faddeev-Popov Jacobian of the axial gauge on trees is 1, and because the exponential
gauge-fixing term ..., with its normalisation, is an exact rewriting of the same integral". EM input (2) (EM:633-647)
requires "the admitted gauge change of variables for the actual fibre measure, relative gauge weight and cut".
The fork, for the next row:
- (G-a) If the decompositions of unity are functions of the exact axial representative (the representation "written in
  the axial gauge"), each cut is a function of the G_res-orbit, (G) holds, and Theorem FCT applies as stated.
- (G-b) If a frame-dependent gauge average (the soft weight's precision) enters the cut itself, the cut factor of frame
  phi in psi's presentation is pi_(w_phi)[chi^phi], a [0, 1]-valued gauge average, not an indicator product; (E1) fails
  as written and (FC-G) of 5.3 is needed.
The texts read here do not decide between (G-a) and (G-b); Balaban's CMP 119 Section 3 and CMP 109 Section 2 would.

## Step 6. (G) read at the source: it fails for the account's representation (written 2026-11-20T13:23Z by date -u)

**6.1 READ (Balaban, CMP 119, owner's copy outside git; OCR text checked against the page image in 6.2).** Section 1,
display (1.5) and the remark after (1.7), p. 247: the "axial gauge fixing" is a soft, truncated weight on the contour
variables U(y, x) from each block centre y to the points x of its block, inserted as an identity
1 = prod_y prod_(x in B(y), x != y) int du(x) z^(-1) chi(|U^u(y,x) - 1| < eps_0) exp(-g_0^(-2) [1 - Re tr U^u(y,x)])
(corrected from the page image at the time stamp of Step 7: the truncation is at eps_0, not at a fixed constant),
followed by the Faddeev-Popov procedure, which leaves the weight exp(-g_0^(-2) G(P_1, U)) with
G(P_1, U) = sum_y sum_(x != y) [1 - Re tr U(y, x)] (1.6)-(1.7). Balaban: "The main point in introducing it in the form
(1.5) is to preserve the Euclidean invariance, but this can be done also with the gauge fixing defined by the delta-functions
of the contour variables ... and we average over the Euclidean transformations of the lattice ... so it can be an
alternative to the above definition." The restrictions on the approximate fluctuation field are introduced after this,
on the configuration itself ("UU_(box)^(-1), where U_(box) is taken in the axial gauge"). At step k (Section 3, p. 265)
"we introduce the axial gauge fixing as in (1.5), with V_k, eps_k, g_k instead of U, eps_0, g_0", then the
decomposition (3.3) restricting approximate fluctuation fields, then the fluctuation field and the decomposition (3.16).

**6.2 Consequence (PROVED from 6.1 and row 1267 Lemma AX).** In the account's representation (CA-I 4.35 (C)(b) cites
exactly [B-CMP119 (1.5)]; RT's truncated Haar normalizer z(x) = int chi(U) exp(-x(1 - tr U/2)) dU is the same device) the
gauge weight has precision g_k^(-2), the frame's own, and the cuts are functions of the softly gauge-fixed configuration,
not of its orbit. So (G) fails as a reading of the account: case (G-b) of 5.6. Theorem FCT covers the threshold part
only; the frame comparison also moves the gauge precision by the relative amount |phi_k/psi_k - 1|, which is of order
theta_k^(-1/2) polylog (row 1267 3.3), not a tail. Under Balaban's stated alternative (delta-function axial gauge on the
contour variables, averaged over the block's lattice symmetries) (G) holds, with each block's cut an average of indicator
products, and Theorem FCT applies after the evident change in (E1) (an average over a finite group of indicator products
obeys (F1)-(F2) termwise).


**6.3 Page check (READ, written 2026-11-20T13:25Z by date -u).** CMP 119 p. 247 read as a page image (rendered from the owner's copy into
the scratch folder): (1.5) is as corrected in 6.1, with truncation chi(|U^u(y,x) - 1| < eps_0) and precision g_0^(-2);
the decomposition (1.8) restricts sup_b |U(b) U_(1,box')^(-1)(b) - 1| < 2 delta_0, with U the integrated (softly gauge
fixed) configuration and U_(1,box') a minimizer "taken in the axial gauge". So the cut compares a softly gauge-fixed
configuration with an exactly axial one: not an orbit function. 6.2 stands.

## Step 7. The soft gauge precision: rescaling the gauge parameters (written 2026-11-20T13:25Z by date -u)

**7.1 Setting.** One block fibre at step k (outer datum W fixed). G_res := gauge transformations equal to 1 at the block
centres; it preserves the fibre and the fibre measure mu_W, and F := e^Phi is G_res-invariant (row 1267 4.3). For a
non-central site x of the block of centre y, U(y,x) is the parallel transport along Balaban's fixed contour from y to x;
under u in G_res, U^u(y,x) = U(y,x) u_x^(-1). For a frame entry theta the soft axial weight per contour is
    omega_theta(U) := z_theta^(-1) 1[|U - 1| < eps(theta)] exp(-theta [1 - Re tr U]),   z_theta := int 1[|U - 1| < eps(theta)] e^(-theta[1 - Re tr U]) dU,
(CMP 119 (1.5) at step k, with tr normalized so that 1 - Re tr U = 1 - cos alpha for eigen-angles +-alpha), and frame
theta's integral is I_theta = int mu_W(dV) F(V) prod_x omega_theta(U_V(y,x)) chi^theta(V), with chi^theta the frame's other
cuts (1.8)/(3.3) and (3.16), each a product of unit indicators at thresholds of the form const * theta^(-1/2) (log theta)^(p_0).

**Lemma AXR (axial disintegration; PROVED, elementary).** For V in the fibre let u^0(V) in G_res be u^0_x := U_V(y,x),
and ax(V) := V^(u^0(V)) (all contour variables equal to 1). Then for every mu_W-integrable Psi,
    int mu_W(dV) Psi(V) = int mu_W(dV) int dv Psi(ax(V)^v),
with dv the normalized Haar measure of G_res, and U_(ax(V)^v)(y,x) = v_x^(-1).
*Proof.* With (V^u)_(x,y) = u_x V_(x,y) u_y^(-1) (row 1267 Lemma AX), (V^a)^b = V^(ba), and U^u(y,x) = u_y U(y,x) u_x^(-1)
= U(y,x) u_x^(-1) since u_y = 1. So U^(u^0)(y,x) = U(y,x) U(y,x)^(-1) = 1: ax(V) is in the exact axial slice, and
V = ax(V)^((u^0)^(-1)). By G_res-invariance of mu_W and Fubini, int mu_W Psi = int mu_W(dV) int du Psi(V^u). For fixed V,
V^u = (ax(V)^((u^0)^(-1)))^u = ax(V)^(u (u^0)^(-1)); as u runs over G_res with normalized Haar measure, so does
v := u (u^0)^(-1) (right translation preserves Haar measure). So int du Psi(V^u) = int dv Psi(ax(V)^v). Finally
U_(A^v)(y,x) = U_A(y,x) v_x^(-1) = v_x^(-1) for A = ax(V). QED

Hence, with F(ax(V)^v) = F(V),
    I_theta = int mu_W(dV) F(V) int prod_x [dv_x omega_theta(v_x^(-1))] chi^theta(ax(V)^v),          (7.1)
and by the normalization of z_theta each factor dv_x omega_theta(v_x^(-1)) is a probability measure: the gauge parameters
v_x are independent given V.

**7.2 Exponential coordinates.** Write v_x^(-1) = exp(X_x), X_x in su(2) with |X_x| the eigen-angle alpha, on |X| < pi.
Normalized Haar measure is dv = J(X) dX with J(X) = c_J (sin|X| / |X|)^2 (the SU(2) density in exponential coordinates;
c_J a constant), and 1 - Re tr exp(X) = 1 - cos|X|, |exp(X) - 1| = 2 sin(|X|/2). So the density of X_x in frame theta is
    rho_theta(X) = z_theta^(-1) 1[2 sin(|X|/2) < eps(theta)] e^(-theta(1 - cos|X|)) J(X).

**Lemma RS (rescaling; PROVED, elementary).** Let phi, psi > 0, c := (psi/phi)^(1/2), s := |X'|. Then
    rho_phi(c X') c^3 = kappa_1 (1 + r(X')) e^(-psi(1 - cos s)) J(X') z_psi^(-1) 1[2 sin(c s/2) < eps(phi)],
with kappa_1 := c^3 z_psi/z_phi (a constant) and 1 + r(X') := [J(cX')/J(X')] exp(-R(s)),
R(s) := phi(1 - cos(cs)) - psi(1 - cos s). If |c^2 - 1| <= 1/2 and s <= 1/2, then
    |R(s)| <= psi |c^2 - 1| s^4/12,   |J(cX')/J(X') - 1| <= |c^2 - 1| s^2.
*Proof.* The identity is the definition of r. For R: phi(1 - cos(cs)) = psi h(c^2), psi(1 - cos s) = psi h(1), with
h(t) := (1 - cos(t^(1/2) s))/t = sum_(m>=1) (-1)^(m+1) t^(m-1) s^(2m)/(2m)!. For t in [1/2, 3/2] and s <= 1/2,
|h'(t)| <= sum_(m>=2) (m-1) t^(m-2) s^(2m)/(2m)! <= s^4/24 + s^6 (2 * 1.5)/720 + ... <= s^4/12, so by the mean value theorem
|R(s)| = psi |h(c^2) - h(1)| <= psi |c^2 - 1| s^4/12. For J: J(cX')/J(X') = (sin(cs)/(cs))^2 / (sin s/s)^2 and
log(sin y/y) = -y^2/6 - y^4/180 - ..., so |log(J(cX')/J(X'))| = 2 |log(sin(cs)/(cs)) - log(sin s/s)| <= 2 |c^2 - 1| s^2 (1/6 + s^2/90 * 3 + ...) <= |c^2 - 1| s^2 / 2
for s <= 1/2, and |e^y - 1| <= 2|y| for |y| <= 1/2. QED

**7.3 What Lemma RS does to the frame comparison (PROVED given (7.1) and Lemma RS).** In (7.1) for theta = phi substitute
X_x = c X'_x at every non-central site (dX = c^3 dX'). Then
    I_phi = kappa_1^(N_s) int mu_W(dV) F(V) int prod_x [rho^0_psi(X'_x) dX'_x (1 + r(X'_x))] chihat^phi(V, X'),
    I_psi = int mu_W(dV) F(V) int prod_x [rho^0_psi(X'_x) dX'_x] chihat^psi(V, X'),
with rho^0_psi the frame-psi density without its truncation, N_s the number of non-central sites (a constant), and
    chihat^phi(V, X') := prod_x 1[2 sin(c|X'_x|/2) < eps(phi)] * chi^phi(ax(V)^(v(cX'))),
    chihat^psi(V, X') := prod_x 1[2 sin(|X'_x|/2) < eps(psi)] * chi^psi(ax(V)^(v(X'))),
where v(X)_x := exp(X_x)^(-1). Reading (7.1) backwards with Lemma AXR, both are integrals over the fibre against frame
psi's soft weight: frame phi's integrand is frame psi's integrand times the local vertex prod_x (1 + r(X'_x(U))), with
its cut replaced by chi^phi o Psi_c, where Psi_c(U) := ax(U)^(v(c X'(U))) dilates each configuration's deviation from the
exact axial gauge by the factor c, and X'(U)_x := log U(y,x). So, at the same weights and list, the two frames differ by:
- (i) a W-independent constant (kappa_1^(N_s); invisible to |||.|||);
- (ii) a local vertex of size rho_k := sup |r| on the domain of the cuts;
- (iii) two cuts that are products of unit indicators, with unit functions N_u o Psi_c, N_u and thresholds T^phi_u, T^psi_u;
  no longer nested, but |N_u o Psi_c - N_u| <= Lip_u |c - 1| (local size of the gauge deviation) on the domain.
**Sizes.** By row 1267 3.3 (from CA-III 69015-69017), |c^2 - 1| = |psi_k/phi_k - 1| <= C_zeta theta_k^(-1/2) (log theta_k)^(p_0).
On the cut domain s = |X'_x| <= 2 arcsin(eps(theta)/2) <= 2 eps(theta), with eps(theta) = A_0 theta^(-1/2) (log theta)^(p_0).
So by Lemma RS, for theta_k large enough that the conditions hold,
    rho_k <= 2 [ |c^2 - 1| s^2 + psi |c^2 - 1| s^4/12 ] <= C_r theta_k^(-3/2) (log theta_k)^(5 p_0),          (7.2)
not a tail, but a power theta_k^(-3/2) up to logarithms; and the cut functions move by a relative amount
|c - 1| <= C_zeta theta_k^(-1/2) (log theta_k)^(p_0), so (iii) is again a tail comparison.

**7.4 Lemma TL* (Lipschitz bound for two polymer gases; PROVED, the argument of Lemma TL (b)-(c)).** Let two polymer
gases share the polymer set and the incompatibility relation, with activities F^1, F^2, and let Fbar >= 0 satisfy
|F^i(X)| <= Fbar(X) and |F^1(X) - F^2(X)| <= lambda Fbar(X) for all X. If e^eps Fbar satisfies (E4) with Bbar and Nbar,
then |Phi^1(Y) - Phi^2(Y)| <= (lambda/eps) Bbar(Y) and the pointed difference has EM norm at most (lambda/eps) Nbar.
*Proof.* Lemma TL (b)-(c) with 2 eta replaced by lambda. QED

**7.5 The three comparisons.** Write E^psi for frame psi's output, E^(phi,rs) for frame phi's output written after the
rescaling of 7.3 (same total up to the constant (i)), and E^(mix) for the run in frame psi's presentation with the vertex
of (ii) and frame psi's cut. Then T(E^phi) - T(E^psi) = [T(E^(phi,rs)) - T(E^(mix))] + [T(E^(mix)) - T(E^psi)] + const.
- *Cut part.* E^(phi,rs) and E^(mix) differ only in the cut: chi^phi o Psi_c with truncation at eps(phi), against
  chi^psi with truncation at eps(psi). Hypotheses (E1)-(E4) are read with a non-nested pair of unit families
  (N^1_u, T^1_u) = (N_u o Psi_c, T^phi_u) and (N^2_u, T^2_u) = (N_u, T^psi_u), and with:
  (E2') the Mayer bound on the union domain {for every u: N^1_u < T^1_u or N^2_u < T^2_u};
  (E3') the one-term bound with Gaussian factors e^((1/2) gamma_2 (N^i_u)^2) for either i.
  Then the proof of Lemma TL goes through with one change in the P-empty case: for a_u := 1[N^1_u < T^1_u],
  b_u := 1[N^2_u < T^2_u], prod a - prod b = sum_j (prod_(l<j) a_l)(a_j - b_j)(prod_(l>j) b_l) (telescoping), each summand
  supported in the union domain, and |a_j - b_j| <= (1 - a_j) + (1 - b_j) <= eta' (e^((1/2) gamma_2 (N^1_(u_j))^2) +
  e^((1/2) gamma_2 (N^2_(u_j))^2)) by (F1), with eta' := exp(-(1/2) gamma_2 T'_lo^2), T'_lo := min over u, i of T^i_u. The
  majorant Fbar takes the factor (1 + 2|Y_0|) in place of (1 + |Y_0|). So the cut part is at most
  (2/eps) C_post Nbar' exp(-(1/2) gamma_2 T'_lo^2).
- *Vertex part.* E^(mix) and E^psi differ by the local vertex prod_x (1 + r(X'_x)) = prod_x (1 + q_x), |q_x| <= rho_k on
  the cut domain (and on the complex domains of the expansion, with the same bound up to a constant). Add the q_x as new
  single-site Mayer elements (prod_x (1 + q_x) is already in Mayer form). The data without new elements carry exactly the
  terms of E^psi; a datum with m >= 1 new elements has integrand bounded by rho_k^m times the bound of the same datum
  without them. So |F^(mix)(X) - F^psi(X)| <= rho_k Fbar_v(X), where Fbar_v counts data with new elements with weight
  rho_k^(m-1). Hypothesis (E6): e^eps Fbar_v satisfies (E4) with a norm bound Nbar_v (one more element type in the
  supplier's convergence, with activity at most rho_k <= 1). Then Lemma TL* gives the vertex part at most
  (rho_k/eps) C_post Nbar_v.

**Theorem FCT' (PROVED GIVEN (E0), (E1), (E2'), (E3'), (E4)-(E6) at every step with uniform constants, (TH), and row
1267's (H1)-(H3), (H5); hypothesis (G) is no longer used).** Along the pin runs, (FC-1) of row 1267 holds with
    nu_k <= K_1 exp(-(1/2) gamma_2 a'^2 (log theta_k)^(2 p_0)) + K_2 theta_k^(-3/2) (log theta_k)^(5 p_0),
K_1 := (2/eps) C_post Nbar', K_2 := (C_r/eps) C_post Nbar_v, a' := a/2 (T'_lo >= T_lo (1 - C |c - 1|) >= T_lo/2 for theta_k
large), and
    sum_(k<n) nu_k <= K_1 S'(X) + K_2 S''(X),   S''(X) := sum_(r>=1) Y(r)^(-3/2) (log Y(r))^(5 p_0),  Y(r) = (X + c_0 r)/3,
with S' the S of Lemma S at a' in place of a; both are finite and independent of n, and tend to 0 as X tends to infinity.
So sum_k eta_k <= 2 C_x (K_1 S'(X) + K_2 S''(X)) (Proposition FC-chain of row 1267).
*Proof.* (TH) and Lemma RS's sizes (7.2) hold once theta_k exceeds a fixed floor, which holds along the pin runs for X
large (theta_k >= X/3). The cut part and the vertex part (7.5) bound the two brackets; the constant (i) is invisible to
|||.|||; the triangle inequality for |||.||| (row 1267 3.1) adds them. Summation: Lemma S for the first term. For the
second, q := 5 p_0 and f(y) := y^(-3/2) (log y)^q, which decreases for y >= e^(2q/3). If X/3 >= e^(4q), then
sum_(r>=1) f(Y(r)) <= int_0^infinity f((X + c_0 s)/3) ds = (3/c_0) int_(X/3)^infinity f(y) dy, and integrating by parts,
int_(Y_0)^infinity f = 2 Y_0^(-1/2) (log Y_0)^q + 2q int_(Y_0)^infinity y^(-3/2) (log y)^(q-1) dy
<= 2 Y_0^(-1/2) (log Y_0)^q + (2q/log Y_0) int_(Y_0)^infinity f, and 2q/log Y_0 <= 1/2, so int_(Y_0)^infinity f <= 4 Y_0^(-1/2) (log Y_0)^q.
Hence S''(X) <= (12/c_0) (X/3)^(-1/2) (log(X/3))^(5 p_0) -> 0. For smaller X the finitely many terms with
Y(r) < e^(4q) are each at most a constant and the rest are bounded as above. QED

**7.6 Remark (PROVED arithmetic): why the power term is summable but would not be at the order of the frame drift.** A
frame change moves the gauge precision by the relative amount |c^2 - 1| ~ theta^(-1/2) polylog. Its first-order effect
on the Gaussian part is exactly removed by Lemma AXR and the rescaling (it is a change of variables), so only the
quartic and Jacobian remainders survive, of order |c^2 - 1| (theta s^4 + s^2) ~ theta^(-3/2) polylog per site. Without
the rescaling, the vertex would be (phi - psi)(1 - cos s) ~ theta^(1/2) polylog * theta^(-1) = theta^(-1/2) polylog per
site, whose sum over a pin run diverges like n^(1/2): this is row 1267 3.3's obstruction, met here at the gauge weight.

**7.7 One more frame dependence: the test-cube size (READ and OPEN, written 2026-11-20T13:28Z by date -u).** In the account R_k is the
least admitted power of L with R_k >= (log g_k^(-2))^r (CA-I I:45900-45905; the cell-size multiplier R-check_k "is a function
of its argument", I:56729-56731). So the two frames use the same test cubes except at the steps where (log theta)^r
crosses a power of L between psi_k and phi_k; around each crossing point theta_a = exp(L^(a/r)) this is a window of about
theta_a^(1/2) polylog / c_0 consecutive steps. Theorem FCT' assumes (U): at every step both frames use one family of test
units, up to the dilation Psi_c. At the window steps the unit functions differ (reference minimizers computed on cubes of
different sizes, CMP 119 (1.8)); the union-domain bound of 7.5 extends to two different unit families if both families'
complements enter one expansion, which is a further reading of the supplier, ARGUED here and not proved. If the account's
R-check is frozen on the scaffold (EM's age gate uses R(min theta_i), EM:364-380), (U) may hold by construction; not
read here.

## Step 8. Labels and state after this row (written 2026-11-20T13:28Z by date -u)

**8.1 Labels added by Steps 6-7** (the table of 5.2 stands, except that (G) is now known to fail for the account's
representation and is no longer needed):

| Statement | Label | Rests on |
|---|---|---|
| 6.1-6.3: in Balaban's representation (CMP 119 (1.5)-(1.8), p. 247; Section 3, p. 265) the axial gauge fixing is a soft truncated weight with precision g_k^(-2) and truncation at eps_k, and the cuts are imposed on the softly gauge-fixed configuration; so the cuts are not orbit functions, and (G) fails for the account's representation (CA-I 4.35 (C)(b) cites this (1.5)) | READ (page image) and PROVED (elementary) | CMP 119 pp. 247, 265; row 1267 Lemma AX |
| Lemma AXR: axial disintegration int mu_W Psi = int mu_W(dV) int dv Psi(ax(V)^v) | PROVED, elementary | invariance, Haar translation invariance |
| Lemma RS: rescaling the gauge parameters by c = (psi/phi)^(1/2) turns frame phi's soft weight into frame psi's times a vertex 1 + r with |r| <= 2(|c^2 - 1| s^2 + psi |c^2 - 1| s^4/12) | PROVED, elementary | 7.2 |
| (7.2): along the pin runs rho_k <= C_r theta_k^(-3/2) (log theta_k)^(5 p_0) | PROVED given row 1267 3.3's drift bound (from CA-III 69015-69017) | 7.3 |
| Lemma TL*: Lipschitz bound for two polymer gases | PROVED | 7.4 |
| Theorem FCT': (FC-1) along the pin runs with nu_k <= K_1 exp(-(1/2) gamma_2 a'^2 (log theta_k)^(2 p_0)) + K_2 theta_k^(-3/2) (log theta_k)^(5 p_0), sum_k nu_k <= K_1 S'(X) + K_2 S''(X) uniformly in n, -> 0 as X -> infinity | PROVED GIVEN (E0), (E1), (E2'), (E3'), (E4)-(E6), (TH), (U), and row 1267's (H1)-(H3), (H5) | 7.5 |
| 7.6: without the rescaling the gauge-precision change is a vertex of order theta^(-1/2) polylog per site, whose sum diverges like n^(1/2) | PROVED, arithmetic | 7.3 |
| (U): both frames use one family of test units at every step | OPEN (fails in windows around the jumps of R_k unless R is frozen on the scaffold; 7.7) | I:45900-45905, I:56729-56731 |

**8.2 The one-cutoff carry on the pin route after this row.** (FI) at pins reduces (row 1260, Lemma GR) to (FC); (FC)
reduces (row 1267, Proposition FC-chain) to the one-step (FC-1); this row proves (FC-1) along the pin runs, with a sum
that tends to 0 as the scaffold floor X grows, given: the supplier's one-step expansion in the form (E0), (E1), (E2'),
(E3'), (E4)-(E6) (Balaban CMP 116 as the account reads it; written out by the account for a large-field stage at
I:108483-108600; CMP 116 itself not read, bot check); (TH) (a reading of the threshold units); (U) (test cubes; 7.7);
and row 1267's bookkeeping (H1)-(H3), (H5). The frame's gauge device, which row 1267 removed only for orbit-invariant
cuts, is handled for Balaban's actual soft gauge by Lemmas AXR and RS at the price of a summable power term. The
carry's other inputs are unchanged: the base seed (OPEN; the infrared crux, not attacked), the 9.1 hypothesis (e) and
9.1:prop-blind-site-expansions, (DET)'s inputs, (V9) (row 1275), the account's premises.

**8.3 What a checker should redo first.** Lemma TL (4.1) and its non-nested form (7.5); Lemma AXR and Lemma RS with the
constants of 7.2; the size (7.2) against row 1267 3.3 and CA-III 69015-69017; the summations (Lemma S, S''); the
readings (E1)-(E3) against I:108483-108600 and I:58716-58717, (TH) against I:4172-4175 and I:29060-29120, and 6.1-6.3
against CMP 119 pp. 247 and 265.

RESULT: Row 1268 (Claude Opus 5.5 max, Mac mini worker 2, 12:59Z-13:28Z by date -u; author only, checked by no one; no numeric run, no subagent). The Jaffe-Witten mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved; the infrared seed ((N-phys), (SL)/(RR) of row 1258) stays OPEN and was not attacked (no engine off the record). Worked item: (FC-T)/(FC-1) of row 1267, the one-step frame comparison of the pin-route carry, left to this row by row 1275. READ in Sussman and Alpoge's CA-I (31a47c543775) and YM4_EM (c7fef8b21b58), with Claude and Codex as authors of their text, and in Balaban's CMP 119 (owner's copy, page image): the cited one-step theorem (CA-I 4.3) bounds each frame separately and EM states no two-cut comparison; in the expansion the account reads in CMP 116 the threshold enters only through kept cuts and signed complements, one complement costing exp(-(1/2) gamma_2 T^2) (written out at I:108483-108600); and Balaban's axial gauge (CMP 119 (1.5)) is a soft truncated weight at precision g_k^(-2) with cuts on the gauge-fixed configuration, so row 1267's orbit-invariance route does not apply. PROVED: Lemma TL/TL* (two polymer gases with activities within lambda of a common convergent majorant have localized logarithms within lambda/eps); Lemma S (summability of exp(-c (log theta_k)^(2 p_0)) along pin runs, S(X) <= 9/(c_0 X)); Lemma AXR (axial disintegration); Lemma RS (rescaling the gauge parameters turns a frame's soft gauge precision into the other's times a vertex of size O(theta^(-3/2) polylog), where the unrescaled change is O(theta^(-1/2)) per site and not summable). PROVED GIVEN the supplier's expansion in the form (E0), (E1), (E2'), (E3'), (E4)-(E6), the threshold reading (TH), the test-cube hypothesis (U) and row 1267's (H1)-(H3), (H5): Theorem FCT', (FC-1) along the pin runs with nu_k <= K_1 exp(-c (log theta_k)^(2 p_0)) + K_2 theta_k^(-3/2) (log theta_k)^(5 p_0), sum bounded uniformly in n and tending to 0 as the scaffold floor X grows, hence (FC) and, with row 1260, the scaffold comparison at pins. OPEN: (U) at the jumps of R_k, the readings (E0)-(E6) against Balaban's CMP 116 text, row 1267's (H2)-(H3), the infrared seed, the 9.1 hypothesis (e), (DET)'s inputs, (V9), the account's premises, the mass gap. Output library/gap-mini-solve-al-opus.md.
