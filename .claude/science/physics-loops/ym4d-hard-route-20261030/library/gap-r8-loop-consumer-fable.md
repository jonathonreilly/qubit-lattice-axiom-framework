lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T07:39Z

# Row 1498, gap-r8-loop-consumer-fable: a consumer for bootstrap-certified loop data (trigger R8)

Started 2026-11-24T19:39Z (date -u), pinned at commit f7171e34d, branch claude/ym4d-hard-route.
Worker: Claude Fable 5.2, high effort, Mac mini worker 1. No subagents. Nothing committed.

Status of this file: in progress. Each step is appended when it ends. Labels: **proved** (argument
written here in full), **read** (taken from a named source, lines given, not re-derived), **sketched**,
**guessed**.

## 0. Plan

Question of the row. Does any finite-size criterion on file reduce, exactly or with a stated loss, to
finitely many Wilson-loop expectations at fixed precision? The criteria named: the rank-one test
(rows 1373, 1461), Theorem T (row 1332), the cube criterion (W) (row 691), the in-law criterion
(row 845). First lemma: at beta = 23/10, does the hypothesis of (W) on a cube of side 4 follow from
two-sided bounds of relative width 1e-3 on all loop expectations of length at most 16?

Steps, one per response:

1. Read row 1496's trigger (R8) (`library/gap-k2-direction-checkpoint-fable.md` 4.3-4.4) and the four
   criteria at their sources. Write each hypothesis as an exact formula. Classify the object each one
   reads: a loop expectation, a polynomial in loops, a conditional law, a norm of an operator.
2. Read the bootstrap sources (Kazakov-Zheng arXiv 2404.16925; Anderson-Kruczenski) for what a dual
   certificate proves, in which class of states, and with which trusted base.
3. Decide the first lemma: prove, or refute by counting or by two states with the same bounded loop
   data and different criterion values.
4. Record the loop length and precision that would be needed, for each criterion.
5. Verdict on (R8); first build row if a consumer exists; the next two rows.

## 1. Sources and the four criteria (Step 1)

### 1.1 What I read

Read in full: FINISH rules (lines 1-84), GOAL.md, row 1498, `library/gap-k2-direction-checkpoint-fable.md`
Sections 1-6 (trigger (R8) is its 4.4), `library/gap-loop-eq-opus.md` (row 754), `library/gap-ds-gauge.md`
Sections 2 (notation), 3.1, 4, 6 (row 691; I did not re-read the proof of Theorem W, which row 693 checked),
`library/gap-annealed-opus.md` 2.1-2.3, Theorem AG, Lemma N, 4.3 (row 845), `library/gap-shrink-box-fable.md`
1.4, 4.4, 5.1-5.3 (row 1332), `library/gap-verified-compute-sizing-fable.md` section M3 and 4.3 (row 1326),
`library/gap-l3-direction-fable.md` 4.2-4.3 (row 1122), the RESULT lines of rows 691, 845, 1332, 1373, 1461.
Read as digests only: `library/prior/gap-fullread-1.md` Sections 5 and 9 (Kazakov-Zheng arXiv 2404.16925 and
Anderson-Kruczenski arXiv 1612.08140, each read there in full TeX source by gpt-6-luna) and
`library/prior/gap-crux-lit-cross.md` lines 55-57. I did not open the two papers myself in this row.

Memory: `memory_pressure` reported 40 percent free at 19:52Z. That is below the 50 percent rule. No numeric
job was started. Everything below is by hand.

### 1.2 What a bootstrap certificate proves (read, from the digests)

- For SU(2) the identity tr X tr Y = tr(XY) + tr(XY^-1) makes the lattice Schwinger-Dyson equations linear in
  expectations of single loops (Kazakov-Zheng eq. (2), Section 2; rebuilt by hand in row 754, Lemmas 1.1, 1.2).
- The constraints are: these loop equations for loops up to a length L_max; positivity of the matrix of
  Wilson-path inner products; reflection positivity; lattice symmetry. A dual solution is a rational
  sum-of-squares identity. It bounds a chosen loop expectation from one side in every functional that obeys
  the constraints.
- Published reach (read): about 0.1 percent on the plaquette with loops up to length 24 (16 in the smaller
  runs). The published bounds are for the plaquette. The papers do not give width 1e-3 for every loop of
  length at most 16. The row's hypothesis is stronger than what is published. I take it as given.
- The class a certificate covers: every functional on loops that obeys the finite constraint set. By
  Proposition VB of row 754 (proved there) this class contains the ground state of every periodic cube of
  side at least 2r + 3 and every even thermal state of a torus of that size, when the constraints sit in a
  ball of radius r. So a certificate with loops of length at most 16 (r at most 8) holds at the same time in
  the infinite-volume state and in every torus of side at least 19.

### 1.3 The four criteria, each as the object it reads

| Criterion | Hypothesis, exact form | What it reads | In the Wilson state? |
|---|---|---|---|
| (W), row 691, 3.1 | Numbers k_z for the boundary links z of V_R, sum per direction at most delta N_R, N_R = R (R+1)^3, with: for all boundary values tau, tau' that differ at z only, a coupling of gamma_V(. given tau), gamma_V(. given tau') with mean Hamming distance at most k_z | A supremum over all boundary values of a transport cost between two conditional laws of the specification | No. No expectation in any Gibbs state occurs |
| (AN), row 845, 2.3 | (AN1) for every block sequence and every set of m jumps at distinct times: E[product of m response fields along the stationary block chain] at most the product of numbers k; (AN2) the k obey (BC-gen) with margin kappa | Mixed moments in the Wilson law of response fields R^a_jc, which are norms of transport fields (solutions of a Poisson equation in the block, a function of the block and its exterior) | Yes, in law. But infinitely many moments (every m), of functions that are not polynomials |
| (KER), Theorem T, row 1332 | 2 log Z(a x B) - log Z(2a x B) at most tau, on one pair of tori at one coupling | A difference of free energies of two tori | No. By Corollary 5.2 of row 754 it is an integral over the coupling of a difference of torus plaquette means |
| Rank-one test, rows 1373, 1461; (PUR-io) | HS distance at most 2/5 between c^-1 P_0 T^w and the vacuum projector; or P_K = Z_+(2u)/Z_+(u)^2 at least 457/625 | Sixteen torus masses with twists, on n = l b^K sites a side | No. Torus quantities of the same kind as (KER) |

### 1.4 What is on file already on this question (read; cited, not redone)

- Proposition VB (row 754): local loop equations with positivity do not see the volume. Theorem O (row 760,
  check 762) and Remark OS (row 1326): a local certificate proves a seed only if a torus of the size of its
  patch has a seed. Precision: (KER) needs about 3e-10 on the plaquette (row 1326, M3) and the weight to
  1.9e-10 (row 1332, 5.2). So the two torus criteria are closed for bounded loops on file. I add nothing.
- Lemma 3.1 of row 754: reflection positivity turns one correlation into a lower bound for a thermal sum.
  That is a necessary condition for a gap, not a sufficient one.
- Theorem EP-NO (row 754): no Griffiths or Ginibre inequality over plaquette monomials holds for SU(2).
- Lemma GM and Lemma TILT (row 1122, 4.2): a normal boundary link at the inside of a face is a gauge move,
  so k_z is at most 7 there. Remark J3 there: the proof of Theorem W needs the supremum over boundary values.
- Row 1326, 4.3: "A worst-case certificate takes a supremum over boundary values ... An in-law certificate
  must evaluate the Wilson measure itself." This row makes that split exact for loop data.

So the open part of (R8) is: (W) and (AN) against loop data, and the general form of a consumer.

## 2. The first lemma (Step 2)

**The lemma under test (L16).** "For the Wilson state at beta = 23/10, the hypothesis of criterion (W) on a
cube of side 4 follows from two-sided bounds of relative width 1e-3 on all loop expectations of length at
most 16."

**Verdict: refuted as a reduction. The truth of (W) at (23/10, 4) itself is not decided here.** The parts:

### 2.1 Lemma A: the loop data are idle for (W) (proved)

Write P(beta; R, delta) for "(W) holds at (R, delta) for Wilson's specification at beta". P is a sentence
about the kernels gamma_V(. given tau), tau any boundary value. Each kernel is an explicit integral that
depends on beta only. No Gibbs state occurs in P.

Statement. Let B be any set of true statements about a Gibbs state of the specification at beta. Then
"B implies P(beta; R, delta)" holds if and only if P(beta; R, delta) holds.

Proof. B is true. QED

This is logic only, and it is the point. (L16) is not weaker than P(23/10; 4, delta). A proof of (L16) in
which the loop bounds do work would have to bound a supremum over tau from above by an integral over tau.
For each z and each Gibbs state mu, the average over mu of a cost is at most its supremum. So in-law data
bound each k_z from below only. Lemma GF is the exact form of that.

### 2.2 Lemma GF: a floor for delta from the plaquette (proved; the complement of Lemma GM of row 1122)

Setting: Wilson SU(2) at any beta, V = V_R, R at least 2. Let x be a site of the box with exactly one
coordinate, the i-th, at an end value. Let z be its normal link (the one link at x that is not in V). Let
T_x be the six links of V at x in the directions j other than i. For l in T_x let p_l be the plaquette that
holds z and l.

Facts (proved by inspection). The six plaquettes that hold z are the p_l. Each p_l holds exactly one link of
V, namely l: its two other links have an end outside the box. Write x_p = (1/2) tr U_p.

**Lemma GF.** For every Gibbs state mu of the specification, k_z is at least the sum over l in T_x of
mu(x_(p_l)). If mu is invariant under the lattice symmetries, k_z is at least 6 u_P, u_P = mu(x_p).

Proof. Fix tau. Let tau^z equal tau except tau^z_z = -tau_z. Then x_(p_l)(sigma, tau^z) = -x_(p_l)(sigma, tau),
and no other plaquette that meets V changes. Let h multiply the eight links at x by -1. It keeps every
plaquette term and Haar measure. It maps tau to tau^z (z is the only boundary link at x). So gamma_V(. given
tau^z) is the image of gamma_V(. given tau) under sigma -> h sigma (this is Lemma GM of row 1122). Put
f(sigma) = (1/2) sum over l in T_x of x_(p_l)(sigma_l, tau), with tau fixed. Each term depends on one link
and lies in [-1/2, 1/2]. So |f(sigma) - f(sigma')| is at most the number of links where sigma, sigma'
differ. For every coupling of the two laws, the mean Hamming distance is at least
E_tau f(sigma) - E_tau f(h sigma) = 2 E_tau f = sum over l of E_tau[x_(p_l)].
So k_z is at least that sum, for every tau. Integrate tau against mu. By the DLR equation, the integral of
gamma_V(x_(p_l) given tau) is mu(x_(p_l)). QED

**Corollary GF (proved).** There are 2 (R-1)^3 such links z in each direction (row 1122, "The count"). So
(W) at (R, delta) for Wilson SU(2) at beta needs

  delta >= 12 (R-1)^3 u_P / (R (R+1)^3),   at R = 4:  delta >= (81/125) u_P.

The factor 12 (R-1)^3/(R (R+1)^3) is 0.222, 0.5, 0.648, 0.711, 0.729, 0.723 at R = 2, ..., 7. It is below
0.73 at every R, so the floor alone refutes (W) at no R.

Remarks.
- Guide number, not proved: u_P(23/10) is about 0.60 (Monte Carlo, recalled). Then delta is at least about
  0.39 at R = 4. A proved lower bound on u_P(23/10) by hand is poor: a ball of radius 0.2 about the identity
  gives a negative free-energy bound at this coupling, and monotonicity of the mean plaquette from the
  strong-coupling range gives a few percent (sketched). So this floor is one true consumer
  of a certified plaquette bound. It points the wrong way: it is necessary for (W), not sufficient.
- With sgn(x_p) in place of x_p in f the floor is 6 mu(sgn x_p), which is larger. It is not a loop polynomial.
- Not found on file: grep of library/ for "end-cap", "gauge-flip", "necessary condition for (W)" gave no
  hit; `library/open-core.md` has no entry for (W), (DS-W) or a bootstrap. Row 1122 has the upper bound
  k_z <= 7 for the same links. Proposition B of row 691 is a different necessary condition.

**Is (W) true at (23/10, 4)? Not decided (guessed: false).** Counts at R = 4 per direction: 54 links of the
kind of Lemma GF, 196 normal links at edges and corners, 600 layer links, N_R = 500. By Lemma GF and Lemma GM
the 54 links cost between 324 u_P (about 195) and 378. So (W) needs the other 796 links to cost less than
305 in sum, a mean below 0.39 each. A layer link flips one of six staples of a surface link. An edge link
has no gauge move. I expect means near 0.3 and above 2 (guessed, no estimate proved). The proved count of
row 1122 gives (DS-W) only for R at least 14/delta. So no bound on file reaches side 4 from either direction.

### 2.3 Proposition M: in-law data need a uniqueness theorem (proved)

**Proposition M.** Let K be a convex set of translation-invariant probability measures on the link
configurations of Z^4. Suppose every member of K clusters on loop functions: nu(F tau_x F) tends to nu(F)^2
as x tends to infinity, for every loop polynomial F. Then all members of K agree on loop polynomials.

Proof. Let mu_1, mu_2 be in K and nu = (mu_1 + mu_2)/2, also in K. Clustering of the three gives
(1/2)(mu_1(F)^2 + mu_2(F)^2) = ((mu_1(F) + mu_2(F))/2)^2. So (mu_1(F) - mu_2(F))^2 = 0. QED

Every condition that a bootstrap certificate can state is convex in the state: a linear loop equation, a
positivity or reflection-positivity condition, a symmetry, a window on a loop value. So:

**Corollary M1 (two states; proved).** Take the class of translation-invariant, reflection-positive,
gauge-invariant measures, and any windows of positive width whose interior holds the loop data x of one
clustering member mu. Then the class holds a member with data in the windows that does not cluster:
nu = (1 - eps) mu + eps mu_0, mu_0 the Haar product measure, eps small. Its data are (1 - eps) x, and
nu(F tau_x F) - nu(F)^2 tends to eps (1 - eps) mu(F)^2, which is positive for F = x_p when u_P is not 0.
So no theorem derives decay from windows on finitely many loops plus positivity and symmetry.

**Corollary M2 (what a consumer must contain; proved).** A theorem "state in K and windows imply clustering",
with K convex, is true only if K with the windows holds at most one state on loops. If K is the set of
symmetric reflection-positive Gibbs states of Wilson at beta, the certified windows hold on all of K. Then
the theorem has no hypothesis: it is uniqueness plus decay at beta, outright. If K is cut out by finitely
many loop equations, the theorem needs **(UNIQ-LE): the positive symmetric solution of the SU(2) loop
equations at beta = 23/10 with short loops in the windows is unique.** Row 754 (Proposition CR and its
reading) has the state of that: the homogeneous loop map has sup-norm ratio 2 beta at one passage and at
least 1 at four passages at every beta, positivity does not bound differences of two solutions, and a
weighted contraction at order-one coupling is OPEN there. Windows on short loops do not change the ratio for
long loops. So (UNIQ-LE) is the open uniqueness problem in loop variables, not a smaller one.

This is the exact form of the clause in (R8), "the theorem must fail for the first-order test model". At a
first-order point the two phases and their mixtures obey the same loop equations, and a window wider than
the jump holds all of them.

### 2.4 Summary of Step 2

(L16) fails as a reduction: its consequent reads no in-law quantity (Lemma A); loop data bound the k_z from
below only (Lemma GF); and no theorem from convex in-law conditions gives decay without uniqueness
(Proposition M). What is left open: the truth value of (W) at (23/10, 4), which no loop data decide.

## 3. Loop length and precision that would be needed (Step 3)

### 3.1 Lemma LEN: what loops of length at most N can represent (proved)

Let Span_N be the closure in sup norm of the linear span of 1 and the W_C, C a closed lattice path of length
at most N. For a function F of the links, links e, e' and values a, a', the mixed difference is
D F = F(U) - F(U with U_e = a) - F(U with U_e' = a') + F(U with both).

**Lemma LEN.** If an end site of e and an end site of e' are at l1-distance above N/2, then D F = 0 for
every F in Span_N.

Proof. Two sites of a closed path of length n are joined by two arcs of total length n, so their l1-distance
is at most n/2. So no path of length at most N holds both e and e'. Each W_C then does not depend on e or
does not depend on e', and D W_C = 0. D is linear and continuous in sup norm. QED

**Count for the cube of side 4 (proved).**
- The cube with its boundary has 2000 + 3400 = 5400 links (850 boundary links in each direction, row 1122).
- Functions of the closed cube in Span_16 come from reduced closed paths inside it. There are at most
  2 x 5400 x 7^15 x 49/48 < 6e16 of them (an oriented first link, then at most 7 steps each time).
- V_4 holds 100 plaquettes with no link in common: plane (1,2), lower corner (a, b, c, d) with a, b in
  {0, 2} and c, d in {0, ..., 4}. Under Haar measure their holonomies are independent with mean 0. So the
  2^100 products over subsets are orthogonal gauge-invariant functions of V_4. 2^100 is about 1.3e30.
- Example outside Span_16: F = x_p x_q with p at the corner (0,0,0,0) and q at (2,2,4,4). Their sites are at
  l1-distance at least 10, and D F is not 0. By Lemma LEN, F is in Span_N only for N at least 22.
- Two gauge-invariant laws of the closed cube with the same loops of length at most 16 and different E[F]:
  the densities 1 + eps G and 1 - eps G against Haar, G the part of F orthogonal to Span_16 in L^2(Haar),
  eps = 1/sup|G|. They differ on F by 2 eps ||G||^2. (These are laws of a cube, not Gibbs states. For states
  use Corollary M1.)

So an exact in-law statistic of the cube of side R with its boundary needs loops up to length 8 (R + 2) + 2,
which is 50 at R = 4 (opposite corners at l1-distance 4 (R + 2)). Length 16 reads sets of l1-diameter 8.

### 3.2 Precision (trivial bound proved; the example is sketched)

If F = sum of c_C W_C plus a remainder of sup norm eta, windows of half-width e_C give mu(F) within
sum |c_C| e_C + eta. A hypothesis with margin m needs sum |c_C| e_C + eta at most m. No criterion on file
has a polynomial hypothesis, so eta is never 0.

Example (sketched; an upper estimate by one method, not a lower bound). The one-link heat-bath mean is
I_2(beta |S|)/I_1(beta |S|) times a trace, S the sum of six staples. Its power series in the staples has
absolute sum of order e^(6 beta), about 1e6 at 23/10, and reaches eta = 1e-3 near degree 42 (13.8^d/d! falls
below 1e-3 between d = 40 and 45). Each staple adds three links, so the loops have length near 130, and the
windows must be near 1e-9. For this one function the loop equation of row 754, Lemma 1.1, does the sum
exactly. Nothing does it for a block statistic such as a transport norm or a total-variation distance.

### 3.3 Table: what each criterion would need

| Criterion | Loop length | Precision | Status |
|---|---|---|---|
| (W) at side 4 | none suffices: not an in-law statement (Lemma A) | none | proved |
| the floor of Corollary GF | 4 (the plaquette), lower bound only | any; delta floor scales with the bound | proved; wrong direction |
| an in-law statistic of the closed cube of side 4 | 50 for exact support; 22 already for one product of two plaquettes | not polynomial, so no finite precision by itself | proved (LEN); no consumer theorem for an in-law form (row 1122, J3) |
| (AN), row 845 | unbounded: (AN1) has every number m of jumps; one jump for a block of closed l1-diameter D needs 2D + 2 | not polynomial (transport fields) | proved from the definition |
| (KER), (PUR-io), rank-one test | patch as large as a seed box: n = 2r + 4 at least 12 at beta 2.2986 in the guide model, larger on the trajectory | about 3e-10 on the plaquette; 1.9e-10 on the weight | read: rows 754, 760, 1326, 1332 |

### 3.4 The one reduction with a stated loss that I can prove: a free-energy bound (new here, small)

**Lemma FE (proved given a certificate at each grid point).** On a periodic torus let f(beta) be
log Z(beta) per site, Z normalized by Haar measure, and ubar(s) the mean plaquette. Then f(0) = 0,
f' = 6 ubar, and ubar is non-decreasing (f is convex). So for 0 = s_0 < ... < s_n = beta and certified
bounds a_k <= ubar(s_k) <= b_k:

  6 sum a_(k-1) (s_k - s_(k-1))  <=  f(beta)  <=  6 sum b_k (s_k - s_(k-1)).

Proof. Riemann sums of a monotone function. QED. The certificate holds on the torus by Proposition VB of
row 754 when the torus has side at least 2r + 3 (read; VB names the ground state and the even thermal state;
for the plain periodic torus of even side the same three checks apply, sketched).

Width: with relative width 1e-3 at each point and a grid of step h, the width of f is about
6 beta (1e-3 ubar + h max ubar'). So fixed precision gives the free-energy density to fixed precision.
This is the only quantity in this file where bounded loops at fixed precision suffice with no further loss.

**Remark CB (sketched; the chessboard estimate is recalled from Frohlich, Israel, Lieb and Simon, with
reflection positivity of the Wilson action from Osterwalder and Seiler; not rebuilt here).** For a
reflection-symmetric cell event B the chessboard norm is z = (Z_B/Z)^(1/N), and P(B on every cell of S) is
at most z^|S|. Z_B has a hand bound from above. Z needs a bound from below, and by hand that bound is
f >= 0 (Jensen) at this coupling. Lemma FE replaces it by a certified number. Guide: f(23/10) is about 3.9,
from ubar about s/4 at small s rising to 0.60 (recalled values, trapezoid rule). Example: B = "every
plaquette of the cell has x_p <= c" has Z_B <= e^(6 beta c) per site, so z < 1 when c < f/(6 beta), about
0.28, against c < 0 by hand.

What this does and does not give. It is a consumer for one component: the one-time Peierls weight of a bad
event, as in Proposition PB of row 845 (row 845, 4.3 names the chessboard norm as "a free-energy quantity").
It is not a consumer for a gap. (SP-ext) of row 845 is a space-time bound along the chain, and its good-block
number k_g is a supremum over good exteriors, which no loop data bound (Lemma A again). So no build row
follows. Not found on file: grep of library/ for "free energy" with "bootstrap" or "loop equation" on one
line gives two files, neither with this statement.
