lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T15:36Z

# gap-seed-solve-fable (queue row 1510): crux attack on the physical seed (PUR-io)

Started 2026-11-25T03:36Z (date -u) at commit 43b92735c on branch claude/ym4d-hard-route. Research-stage working state; nothing here is a public claim. Unchecked when written.

## 0. Status log

- 03:36Z started; reading the row, the rules and the inputs.
- 03:40Z read: FINISH rules, row 1510, RESULT lines 1496-1502 and 1461/1462/1465, gap-k2-tool-design-fable 2-3.3, gap-k2-direction-checkpoint-fable in full.
- 03:51Z read: gap-r8-loop-consumer-fable 1.3-2.2 ((W), Lemma GF), gap-k2-direction-checkpoint-check-astra62 in full. Thinking recorded in Section 1 next.
- 03:56Z read: row 1474 3.5 (open bridge step), Theorem W statement (gap-ds-gauge 3.1). Long thinking pass done; writing Section 1.
- 04:02Z Sections 1-2 written; cross-branch search started in the background.
- 04:05Z cross-branch search done: main (83 mass-gap .md files) and PR 10114 (12 MASS_GAP files), pattern 'weighted Poincar|Poincare ... (probability kernel|block kernel|image measure)|PUR-io': no hit. Read Lemma LD-1 and Corollary LD-2 (gap-crux-direction-fable.md L255-281): LD-2 caps the stiffness from above and gives no lower bound, so it does not give the floor of Corollary NF below.
- 04:08Z Section 3 written (route FI: Proposition PC, Corollary NF, Theorem NB, limits of PC).
- 04:10Z Section 4 written (Lemma REV, first unproved lemma (FL), tool, the two open statements, table of other attacks). memory_pressure read 38 percent free, so no numeric job was started; the counts of (F4) are by hand with the control sum 24.
- 04:11Z Sections 5-6 written. Re-read of the proved items is next.
- 04:11Z re-read of the proved items done: (F4) counts recomputed term by term (24+36+24+6 = 90; 12+8+2 = 22; 8+2 = 10; 6; total 192 = half of 384), NF arithmetic, NB threshold (corrected from 1/31 to 1/32 earlier), REV. No further change. Finished.

Labels used below: **proved** (a written proof is in this file), **read** (I read the statement in a row or
source and did not re-derive it), **sketched** (argument outlined, steps missing), **guessed** (my judgment),
**guide** (heuristic number, never a proof step). Nothing here is checked by another model.

## 1. The target and the frame (read; nothing new in this section)

- Target (row 1468, 3.1, Fact PUR; checks 1462, 1465). T is the Wilson transfer operator at beta_K on the
  spatial torus of side n = l b^K, u = n/512, Z_+(v) = Tr(P_0 T^v), P_K = Z_+(2u)/Z_+(u)^2. (PUR-io): P_K is
  at least 457/625 at infinitely many K, for one l and one g_0. It gives s_K(u) <= 4/21 and a gapped
  calibrated limit.
- Readings on file, which I use and do not count: 1 + s = Z_+(u)/lambda_0^u is the neutral thermal sum
  (rows 1367, 1386, 1496 2.1); the rank-one (Hilbert-Schmidt) test of rows 1373, 1461; the replica swap
  (rows 1131, 1201, 1337). In one line: with r_i the neutral eigenvalue ratios, s(u) = sum of r_i^u is the
  sum of the squared canonical correlations of two time slices at lag u/2, and log(1 + s) is 512^3 times
  the pressure over T^4 at temperature T = 512/l. So the seed says: the pressure of the theory at T = 512/l
  is below 1.3e-9 T^4 (guide arithmetic: log(25/21)/512^3). With a mass m this needs m l of order 1e4.
- Closed lines that I do not restate as progress: Theorem K2 and 2.4 of row 1496 (every class of a chain
  already has the purity); check 1484; the end class at beta <= 0.00872 (rows 1471, 1473); the release floor
  (rows 1464, 1470); the weak-side tests (rows 1472-1495); (W) and Lemma GF (rows 691, 1498, 1501); the
  registry of triggers (R1)-(R9).
- The two statements left open by the checks: check 1497 (i) (can a class restriction concentrate the
  selective estimate in an entry bound, one transition or the terminal bound, and does that help?) and
  check 1501 (the truth of (W) at side 4 and beta = 23/10). Section 3 answers the first for three explicit
  families of classes. I did not decide the second (Section 4.4).

## 2. Repo search

- Local: `grep -l -i -E "weighted Poincar"` on `library/gap-*.md` and `library/prior/*.md`: no hit.
  `library/open-core.md`: no entry for PUR, purity, the seed or a Poincare carry (grep, 2 unrelated hits).
  `library/open-registry.md`: no hit for PUR-io. Relatives that are on file and that I cite where used:
  Lemma LD-1, LD-2 and Theorem LOSS (row 1460), Lemma NG (row 1474 2.3), Proposition G1 (row 1128),
  Lemma MARG / Proposition SIGMA and Theorem TS-J (row 957), Proposition AVG (row 968 5.4), the two-block
  product defect (row 1474 2.5), Theorem W (row 691), the open bridge step (row 1474 3.5), Lemma BT (row 1353).
- Cross-branch (bare blob-less fetch in a /tmp scratch folder): 83 mass-gap `.md` files of main and the 12
  `MASS_GAP*.md` files of PR 10114, pattern "weighted Poincar", "Poincare ... (probability kernel, block
  kernel, image measure)", "PUR-io": no hit. PRs 10133, 10134, 10141, 10144 were not searched in this row;
  check 1497's search of them for PUR-io and K2-STEP found nothing (read).

## 3. The attack: functional inequalities in law (route FI)

### 3.0 Why this route

The T0 form of the gap is decay of correlations. On file, the two-scale and flow routes to a spectral gap
(rows 957, 968, 970) stop at a supremum over fields ((TILT-COV-sup), requirement (f) of row 1386). The
checkpoint (row 1496 4.1) lists that supremum as the failing line. So I asked one question from the target:
does a functional inequality with field-dependent weights, taken in law and with no supremum, pass through
one exact Q2 step? Answer: yes, exactly (Proposition PC). I then followed the route until it stopped
(Section 4). On the way it gave a statement about every K-II chain (Corollary NF, Theorem NB), which
answers check 1497 (i) for one explicit family of classes.

### 3.1 Setting and elementary facts

X is the space of fine link fields on one period of a torus (twisted or not), a product of copies of
SU(2) = S^3 in the quaternions, with the round metric of the unit sphere. For f on X, grad_l f is the
gradient in the link l. Y is the same for the coarse bonds. Q2 with strength kappa has the kernel
K(W, V) = product over coarse bonds c of k(kappa M_c(W), V_c), where for h in R^4 and v in S^3

    k(h, v) = exp(<h, v>) / Zc(|h|),      nu_h = k(h, .) dv  (dv = Haar),

and <M, V> = Re(M V^-1) for a unit quaternion V. Write t = |h|.

(F1) (proved) Zc(t) >= 1 (Jensen, the Haar mean of v is 0). So the density of nu_h lies between e^(-t)/Zc
and e^t/Zc, and for every unit vector e: Var_(nu_h)(<e, v>) <= (e^t/Zc) E_Haar <e, v>^2 <= e^t/4.
(F2) (proved from one classical fact) Haar measure on S^3 has Poincare constant 3 (first eigenvalue of the
Laplacian of the unit 3-sphere; read, classical). Hence for every smooth g on S^3, with c its Haar mean:
Var_(nu_h)(g) <= (e^t/Zc) E_Haar (g - c)^2 <= (e^t/(3 Zc)) E_Haar |grad g|^2 <= (e^(2t)/3) E_(nu_h) |grad g|^2.
So nu_h has Poincare constant rho(t) >= 3 e^(-2t).
(F3) (proved) d/dh log k(h, v) = v - m(h), m(h) the mean of nu_h.
(F4) (proved by counting) Let p_lc be 1/384 times the number of traversals of the fine link l by the 384
contours of the coarse bond c. Then the operator norm of the derivative D_l M_c is at most p_lc (a
holonomy is a product of unit quaternions; left and right multiplications are isometries; each traversal
moves the product at unit speed). The sum over l of p_lc is the mean contour length, 2 + 2 E|xi| = 6. The
sum over c of p_lc is at most 2 for every l. Count for the last claim: a link (x, j) lies in the straight
part of exactly two pairs (y, xi) of the bonds of direction j, which gives 48/384 = 1/8. It is a leg link
only if x_j is even; then eta = x mod 2 fixes the coarse site, and for each of the 4 bonds that start
there and the 4 that end there the number of pairs (xi, pi) is 90, 22, 10, 6 for |eta| = 0, 1, 2, 3 (sum
over the a axes after j of binom(3-k, a) 24 k! a!/(k+a+1)!). The maximum is 1/8 + 8 * 90/384 = 2, at the
links that start at a coarse site. Control: the sum over the 64 links of a cell is 8 + 4 * 8 * 192/384 = 24
= 4 bonds times length 6.

### 3.2 Proposition PC (a weighted Poincare inequality passes through the kernel, in law). Proved.

Let mu be a probability measure on X with a smooth positive density, and w_l >= 0 measurable functions on X
with

    (WP(w))   Var_mu(f) <= integral of sum_l w_l |grad_l f|^2 dmu   for every smooth f.

Let mu' = mu K be the image on Y, and let E[. | V] be the conditional expectation under the joint law
mu(dW) K(W, dV). Put t_c = kappa |M_c(W)|, sigma^2(t) = the largest eigenvalue of the covariance of nu_h,
rho(t) = the Poincare constant of nu_h, and

    alpha_lc(W) = kappa ||D_l M_c(W)|| sigma(t_c) rho(t_c)^(-1/2),
    b_c(W) = sum_l w_l(W) alpha_lc(W) sum_(c') alpha_lc'(W),
    w'_c(V) = E[ 1/rho(t_c) + b_c(W) | V ].

Then (WP(w')) holds for mu': Var_mu'(g) <= integral of sum_c w'_c |grad_c g|^2 dmu' for every smooth g.

Proof. Var_mu'(g) = E_mu Var_K(W)(g) + Var_mu(Kg). (1) K(W, .) is a product measure. By the Efron-Stein
inequality and the Poincare inequality of each factor, Var_K(W)(g) <= sum_c E_K(W)[ rho(t_c)^-1 |grad_c g|^2 ].
(2) By (WP(w)) for f = Kg, Var_mu(Kg) <= E_mu sum_l w_l |grad_l Kg|^2. Let zeta be a unit tangent vector at
the link l and u_c = kappa D_l M_c zeta in R^4. By (F3), zeta(Kg) = sum_c E_K(W)[ g <u_c, V_c - m_c> ]. The
factor <u_c, V_c - m_c> has mean zero in V_c, so the c-th term is E_K(W)[ Cov_c(g, <u_c, V_c>) ], Cov_c the
covariance in V_c alone. By Cauchy-Schwarz and the Poincare inequality of the factor,
|Cov_c(g, <u_c, V_c>)| <= (rho(t_c)^-1 E_c |grad_c g|^2)^(1/2) sigma(t_c) |u_c|. By Jensen,
|grad_l Kg| <= sum_c alpha_lc G_c^(1/2) with G_c = K(|grad_c g|^2)(W). So
|grad_l Kg|^2 <= (sum_c alpha_lc)(sum_c alpha_lc G_c), and summing over l with the weights w_l gives
Var_mu(Kg) <= E_mu sum_c b_c(W) G_c(W) = E sum_c b_c(W) |grad_c g|^2(V) under the joint law. (3) Add (1)
and (2) and condition on V. QED

Remarks. (i) No supremum over fields occurs. The proof uses only that the kernel is a product of
exponential families with smooth parameters; M_c may be any smooth map. (ii) With w constant the statement
is the usual Poincare inequality for mu and a weighted one for mu'. (iii) Relatives on file: Lemma MARG and
Proposition SIGMA of row 957 and Proposition AVG of row 968 (read in the digests, not re-read) treat
marginals and averaged curvature; Lemma LD-1 of row 1460 is the Hessian identity of the same kernel. I did
not find the weighted form (Section 2).

### 3.3 Corollary NF (the floor of a weak kernel). Proved.

For every probability measure mu on X with a smooth positive density and Poincare constant rho_0 > 0, and
every kappa > 0, the image mu K has Poincare constant rho' with

    1/rho' <= e^(2 kappa)/3 + kappa^2 e^(3 kappa) / rho_0 .

For kappa = 1/4: 1/rho' <= 11/20 + (2/15)/rho_0. After j steps of Q2 with strength 1/4,
1/rho_j <= 33/52 + (2/15)^j / rho_0.

Proof. t_c <= kappa. By (F1), (F2), (F4): alpha_lc <= kappa p_lc (e^(kappa/2)/2)(e^kappa/sqrt 3). With
w = 1/rho_0: b_c <= (kappa^2 e^(3 kappa)/(12 rho_0)) sum_l p_lc sum_c' p_lc' <= (kappa^2 e^(3 kappa)/(12 rho_0))
* 6 * 2. Also 1/rho(t_c) <= e^(2 kappa)/3. For kappa = 1/4: e^(1/2) < 33/20 and e^(3/4) < 53/25, so
e^(2 kappa)/3 < 11/20 and kappa^2 e^(3 kappa) < 53/400 < 2/15. The recursion y -> 11/20 + (2/15) y has the
fixed point 33/52. QED

The recursion contracts when kappa e^(3 kappa/2) < 1, that is for kappa below about 0.48 (guide arithmetic).
A smooth positive density on a compact product has rho_0 > 0 (Holley-Stroock against Haar; read, classical).

### 3.4 Theorem NB (classes of normalized measures are blind; weak steps erase the shape). Proved.

Let D be any family of sixteen smooth positive densities at a level that allows j more halvings, rho_0 the
least Poincare constant of its sixteen normalized measures, and D_j its image under j steps of Q2 with
strength 1/4. Then (a) P(D_j) = P(D), and (b) each of the sixteen normalized measures of D_j has Poincare
constant at least (33/52 + (2/15)^j / rho_0)^-1, which is above 3/2 once (2/15)^j <= rho_0/32 (then 1/rho_j <= 33/52 + 1/32 = 277/416 < 2/3).

Proof. (a) is Lemma TW of row 1468 with check 1497 (i). (b) is Corollary NF on each torus; the twisted
field spaces are products over one period and the kernel is the same product of exponential families
there (Lemma TW). QED

Consequences.
1. Purity is a function of the sixteen masses. A property of the normalized measures does not see them:
   multiply the eight densities of time side 2v by a constant c, and P is multiplied by c with all sixteen
   normalized measures unchanged. So no terminal class can be defined by a Poincare, log-Sobolev or
   covariance-decay property of the normalized measures. (One line; the lane uses unnormalized masses for
   this reason, check 1497 (iii) last paragraph.)
2. Theorem NB adds that such a property is not only blind but free. A K-II chain may use any strengths.
   With strength 1/4 it sends every family, of every purity, into the class "Poincare constant above 3/2"
   in a number of steps that is logarithmic in 1/rho_0. For a family on tori of side n with rho_0 at least
   n^-A this is at most 1 + (A log n + log 32)/log(15/2) steps, fewer than the log_2 n halvings that the
   tori allow when A < log_2(15/2) = 2.9 (arithmetic; the bound rho_0 >= n^-A for a given family is an
   input, not proved here).
3. For check 1497 (i): a class restriction on the normalized measures cannot carry any part of the
   selective estimate, at the entry, at a transition or at the end. A chain can only read the unnormalized
   densities, as one local functional on the sixteen tori. For such classes the statement of row 1496 2.4
   holds (every class has the purity), and I found no factorization that helps. This is an answer for the
   two explicit families (normalized classes: no; action classes: 2.4 applies), not for all classes.

### 3.5 What Proposition PC does not give

- Direction. PC goes from fine to coarse. It carries an upper bound for 1/rho with the factor b. In the
  abelian linear case, with Q the signed averaging map, the factor on the constant mode is exactly
  L^(2-d) = 1/4 for side 2 in d = 4 (Q^T 1 = 1/8 on each fine link of the same direction, since the signed
  leg terms of the bonds that start and end at a coarse site cancel; Q applied to it gives 2/8).
  This is the canonical scaling of a squared mass. A chain of such steps transports a gap; it does not
  make one. The entry bound it needs is rho_0 l^2 of order (m l)^2, the gap in the physical box. That is
  the target. By the equivalence rule this is no progress on (PUR-io), and I claim none.
- Sign (guide, not proved). With rho_k of order x_k m_k^2 and m_(k+1) = 2 m_k, the in-law factor of a step
  at weak coupling must be x_k/(4 x_(k+1)), above 1/4. Asymptotic freedom makes the carry lose stiffness,
  as it must. So PC with its factor is not a place where a selective sign can enter.
- Purity. By 3.4 a Poincare constant says nothing about the sixteen masses.

## 4. Where the route stops

### 4.1 Lemma REV (the step from coarse to fine, in law). Proved; elementary.

Notation of 3.2. Let mu^V be the posterior of W given V (density proportional to mu(dW) K(W, V)), and
S_c(W, V) = grad_(V_c) log k(kappa M_c(W), V_c), the tangential part of kappa M_c(W) at V_c; |S_c| <= kappa.
Assume, for mu'-almost every V and measurable u_l, gamma_cl >= 0 on X x Y:

- (H1) Var_(mu^V)(f) <= E_(mu^V)[ sum_l u_l |grad_l f|^2 ] for every smooth f;
- (H2) |Cov_(mu^V)(f, S_c)|^2 <= E_(mu^V)[ sum_l gamma_cl |grad_l f|^2 ] for every smooth f and every c;
- (WP(w')) for mu'.

Then (WP(w)) holds for mu with w_l(W) = E[ u_l + sum_c w'_c(V) gamma_cl(W, V) | W ].

Proof. Var_mu(f) = E_mu' Var_(mu^V)(f) + Var_mu'(F), F(V) = E_(mu^V) f. Differentiating the quotient
F = (integral of f mu K)/(integral of mu K) in V_c gives grad_c F = Cov_(mu^V)(f, S_c). Apply (WP(w')) to F,
then (H2); apply (H1) to the first term; take the expectation under the joint law and condition on W. QED

(H2) always holds with gamma_cl = kappa^2 u_l (Cauchy-Schwarz and (H1)). Then the sum over c is of the
order of the volume. So the content of (H2) is locality: gamma_cl small when c is far from l. With PC this
gives an exact calculus of weighted inequalities in both directions with no supremum over fields.

### 4.2 The first lemma that I could not prove

**(FL), one order-one step in law.** Let J = [2, 3] (any closed interval that contains 23/10). For Wilson's
measure mu at beta in J on every torus with even sides at least 8, and Q2 with strength kappa = beta, there
are measurable gamma_cl >= 0 on X x Y and constants C, m > 0 that do not depend on the torus, with (H2) for
mu'-almost every V and E[gamma_cl] <= C exp(-m dist(c, l)) under the joint law. (The chain needs the same
for the blocked family at each level, with moments of the composed weights; (FL) is the first case.)

State of (FL): not proved, not refuted, not tested. What I can say exactly:

- (FL) is a carry, not a selective statement. In the Gaussian approximation the posterior has a mass of the
  order of the inverse block side from the constraint, for a massless theory too (Balaban's fluctuation
  propagator; read, not rebuilt). So (FL) is expected for compact U(1) and in five dimensions as well
  (guessed). It fails none of the tests (t1)-(t6) because it claims no gap.
- At weak coupling (FL) is the small-field decay of the fluctuation covariance, with the large fields
  moved into the moments of the weights. That is T1 in a weighted form. T1 is parked (row 1496 Section 3,
  check 1497 (ii)), and this route gives it no consumer.
- At beta near 23/10 there is no small parameter. Kinds A, B, C of row 1496 4.1 apply to (FL) unchanged:
  no expansion, no certificate of feasible size (the posterior of one step on a side-8 torus has more than
  16,000 links), no sign. A pointwise bound ((TILT-COV-sup) of rows 968 and 970, (LOC-COV) of row 968) implies (FL)
  with constant weights; (FL) is formally weaker. I cannot show that it is easier, so under the equivalence
  rule I claim no progress from stating it.
- (FL) does not finish the route. Three more parts are open after it: (i) the source of a gap at the
  coarse end. Corollary NF gives a Poincare constant there for free, but only for weak strengths, where
  (H2) for the posterior is the gap of the fine measure under bounded local tilts (circular). With an
  informative strength the source needs the blocked action at small readout, which is T2 of row 1474, a
  closed line. (ii) The composition over the levels multiplies random weights; it needs joint moments
  (the large-field problem in this language). (iii) A weighted Poincare inequality with bounded mean
  weights must still give decay of correlations (not proved here; with constant weights and a local
  action this is classical).

So route FI does not pass the wall. It removes the supremum over fields from the two carry steps (PC, REV)
and leaves the order-one input where it was.

### 4.3 What mechanism or tool the lemma needs, and the first component

- The tool is an estimate of the covariance of S_c with an arbitrary smooth f in the posterior of one block
  step, local in law, at coupling of order one. Its first component is the pair PC and REV (built here,
  proved by hand, unchecked). The second would be a local-to-global theorem that takes (H2) on one block
  with typical boundary values and returns (H2) on every torus. By Proposition M of row 1498 (checked,
  row 1501) such a theorem from in-law data must contain a uniqueness input; the nearest item on file is
  candidate 2.5 of row 1474 (block tensors in L2, no supremum), which has no gluing theorem and no
  feasible evaluation. I found no second component that is not on
  file as stopped.
- I therefore do not recommend a build row for (FL). The calculus PC + REV is the part worth keeping: if
  an order-one input in law is ever found (trigger (R1) or (R8)), these two statements are its consumer on
  the carry side without (TILT-COV-sup).

### 4.4 The two statements that the checks left open

- Check 1497 (i). Answered for two explicit families of classes in 3.4: classes of normalized measures
  cannot carry any part of the selective estimate (and weak steps reach them for free); for action classes
  row 1496 2.4 applies and I found no factorization that helps. For other families of classes it stays
  open.
- Check 1501, the truth of (W) at side 4 and beta = 23/10. Not decided. A refutation by Lemma GF needs a
  proved lower bound on a plaquette mean near 0.6, which no hand method on file gives; a proof needs upper
  bounds on 796 influences with a supremum over boundary values. One remark (sketched, not on file by
  `grep -i "modulo gauge|gauge-quotient"` in `gap-ds-gauge.md` and its check): the 54 links of Lemma GF are
  gauge moves (Lemma GM of row 1122), so their cost is 0 if the distance between configurations is
  counted modulo gauge transformations inside the cube. The floor (81/125) u_P is a property of the
  Hamming distance, not of the specification. A version of Theorem W for the distance modulo gauge is not
  written, and it has no supplier, so I do not propose it as a row.

### 4.5 Other attacks tried in this session, each with the place where it stops

I tried these before and beside route FI. Each landed on a line that is on file. The anchors are from the
RESULT lines and my memory digests of the rows, not from a new reading of the files.

| Attack | Stops at | On file |
|---|---|---|
| Direct bound of 1 + s = Z_+(u)/lambda_0^u by convexity in u, by the cross channel (time along a long side), or by a trial state | Log-convexity and reflection positivity give Z_+(u) >= lambda_0^u only; a trial state must overlap the vacuum on n^3 sites | row 1496 4.1; (VIR_K) row 708 |
| P_K as the swap-twisted partition function of two replicas, with Tomboulis-Yaffe type inequalities | They bound an order observable by the weight of the odd sector, so they give lower bounds on 1 - P, necessary conditions only | Lemma 3.1 of row 754; rows 1131, 1201 |
| One transition of large side or weak strength into the end class | The image's normalization is not local: log D' = log(mass) + a local part, and the mass is the unknown (3.4) | row 1496 2.4; Theorem LOSS, row 1460 |
| Bridge from (W) to purity | Theorem W (A) is weak mixing with the distance to the whole boundary; the bridge needs the influence of one wall on a function at the other wall, and the cube average loses in the collar | row 1474 3.5; row 691 2.1 |
| Temporal gauge: exactly solved time chains per link, coupled by spatial plaquettes | A Dobrushin or Wasserstein contraction per link; holds only in the hand range | row 691 (open point 3); ceilings in `gap-status-1113.md` |
| Thin twisted tori, where the gap is perturbative | The bridge to a large torus (adiabatic continuity) has no inequality | `gap-ac-lat.md`; row 720 Part 2 |
| SO(3) x Z_2 variables with duality and Griffiths for the Z_2 part | The signs of the Z_2 couplings are frustrated; no Griffiths inequality | row 1025; Theorem EP-NO, row 754 |
| Integrated Gamma_2 with the mean Hessian (positive by gauge invariance) | The fluctuating part of the Hessian has no bound in law | rows 957, 1003, 1006; row 1496 4.1 |
| Block dynamics in L2(mu) with weights equal to finite-block constants at the actual boundary value | The gap of the block dynamics is a maximal correlation across the overlap, which is the gap again | row 1474 2.2 and 2.5; row 957; check 1497 (iii) |

## 5. The next two rows and their decisive outcomes

I propose no attack row and no build row.

**Row 1, `gap-seed-solve-fable-check-astra62` (cross-provider check of Sections 3 and 4.1; gpt-6.2-astra).**
Order: (i) the counts of (F4): 90, 22, 10, 6 pairs, the maximum 2 and the sum 6, by an exact enumeration
of the 384 contours (I did them by hand; memory was at 38 percent free, so I ran nothing); (ii) the proof
of Proposition PC line by line, in particular the Efron-Stein step and the identity for grad_l Kg; (iii)
the arithmetic of Corollary NF (e^(1/2) < 33/20, e^(3/4) < 53/25, 33/52 + 1/32 < 2/3 are rational
statements that Lean can check); (iv) Theorem NB and whether consequence 3 says more than is proved; (v)
Lemma REV. Decisive outcome: if it holds, the registry gets one line (classes of normalized measures are
excluded from K-II designs; steps with strength below about 0.48 carry no shape; PC and REV are the carry
calculus without (TILT-COV-sup)), and check 1497 (i) is closed for that family. If a line is wrong, the
check names it; nothing else on file depends on this row.

**Row 2, `prior/gap-inlaw-two-scale-lit-luna` (bounded literature row; held until Row 1 reports).**
Question: is there a published proof of a spectral gap, a log-Sobolev inequality or a covariance decay for
a continuous-spin lattice model with a non-convex interaction at coupling of order one that uses neither a
correlation inequality nor a supremum over boundary values or tilts (weighted or defective inequalities,
typical boundary values, Lyapunov conditions)? Decisive outcome: a hit whose method supplies (H2) in law
gives (FL) a proof row with that method named, and trigger (R1) or (R8) is met in this form. No hit closes
route FI on the literature examined, and (FL) is added to the triggers as (R10): an in-law covariance
bound for the posterior of one block step at order-one coupling, with a local-to-global theorem.

If row 1511 (the independent attack by gpt-6.2-astra, which I did not read) names a first lemma, the lead
should compare it with (FL) and with T2 of row 1474 before either row above is queued.

## 6. Labels, credits, what was not done

- Proved here by hand, one author, checked by no one: facts (F1)-(F4), Proposition PC, Corollary NF,
  Theorem NB with consequences 1 and 2, Lemma REV. Each is short. None of them moves (PUR-io).
- Sketched: consequence 3 of Theorem NB beyond the two families named; the remark on the distance modulo
  gauge in 4.4; the reasons in the table of 4.5.
- Guessed: that (FL) is true; that it holds for U(1) and in five dimensions; that no second component of
  the tool exists that is not on file as stopped.
- Guide numbers only: 1.3e-9 for the pressure, m l of order 1e4, the bound 0.48 for the strength, the sign
  remark in 3.5.
- Not done: no numeric run (memory_pressure read 38 percent free, below the 50 percent rule), no Lean,
  no Monte Carlo test of (FL), no decision of (W) at (23/10, 4). I read RESULT lines and the named sections
  of the input files, not the full files, except `gap-k2-direction-checkpoint-fable.md` and its check,
  which I read in full. `library/open-registry.md` was searched by grep, not read. I did not read the
  output of row 1511.
- New against the record, as far as the greps of Section 2 show: the weighted in-law form of the carry
  (PC, REV) and the floor of a weak kernel (NF, NB). Relatives are named in 3.2 (iii).
- Credit. Sussman and Alpoge, with Claude and Codex, for the kernel, the contour mean and the release that
  the frame rests on. Balaban for the block method and the fluctuation propagator. Efron and Stein; Holley
  and Stroock; Dobrushin and Shlosman; Otto and Reznikoff and Grunewald, Otto, Villani, Westdickenberg for
  the two-scale idea that REV follows; Bauerschmidt, Bodineau and Dagallier for the multiscale criterion
  whose supremum this row tried to remove. In the lane: rows 1461, 1468 (Claude Fable 5.2, gpt-6.2-astra),
  checks 1462, 1465, 1469, 1484, 1497, 1501 (Claude Opus 5.5, gpt-6.2-astra), rows 691, 957, 968, 1122,
  1460, 1474, 1496, 1498 as cited.

## 7. Result

RESULT: Row 1510 (Claude Fable 5.2 high, Mac mini worker 1; author only, checked by no one; no numeric run because memory was at 38 percent free, no Lean, nothing committed). (PUR-io), (M-io-exists) and the gap are NOT proved and not moved; outcome of the third kind. Route tried from the target: functional inequalities in law, with field-dependent weights and no supremum over fields. Proved by hand: Proposition PC (a weighted Poincare inequality passes through one Q2 step exactly, with explicit weights) and Lemma REV (the converse two-scale step in law); Corollary NF (for every measure, one Q2 step of strength kappa gives 1/rho' <= e^(2 kappa)/3 + kappa^2 e^(3 kappa)/rho_0; at strength 1/4 the limit is 33/52); Theorem NB (j weak steps keep the sixteen masses and put every family, of every purity, in the class with Poincare constants above 3/2, so classes of normalized measures can carry no part of the selective estimate; this answers check 1497 (i) for that family, and for action classes row 1496 2.4 applies). First lemma not proved, stated exactly in 4.2: (FL), an in-law bound with decay for the covariance of the kernel score in the posterior of one Q2 step at beta in [2, 3]; it is a carry, formally weaker than (TILT-COV-sup), not shown easier, and after it the route still needs the blocked action at small readout (T2 of row 1474), joint moments of the weights, and decay from a weighted inequality. Nine other attacks stopped on lines already on file (table 4.5). Not decided: (W) at side 4 and beta = 23/10 (check 1501). Next: a cross-provider check of Sections 3 and 4.1; then one bounded literature row on in-law two-scale methods; no attack or build row.
