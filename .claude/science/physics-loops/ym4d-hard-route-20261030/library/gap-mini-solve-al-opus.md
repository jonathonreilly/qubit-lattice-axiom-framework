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
