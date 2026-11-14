# FINISH row 842: Theorem S1 (twisted thin torus weak-coupling gap), Opus author note

Author: Claude Opus 5.5 (max effort), FINISH row 842.
Clone: /Users/jonreilly/ym4d-lead/clone at commit d7a3a22a9e9a6d6485df28693d11e86d041535c6
(2026-11-12 20:09:26 -0500, "docs(ym4d): record row 843 (Q8/2T test, low-spin filter; HS open), add rows 854-855").
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
Status tags: PROVED (mine), READ (path:line), ARGUED, GUIDE, OPEN.

## Target statement (as given in the row brief; to be checked against D/library/gap-skeleton-final.md)

Theorem S1. For each n >= 2 there are beta_0(n) > 0 and c > 0 such that, for beta >= beta_0(n),
the Wilson SU(2) measure (weight exp(beta tr U_p / 2)) on the twisted thin torus
(Z/n)^2 x (Z/M)^2, with the centre twist in the thin plane, has exponential decay at rate c/n
of gauge-invariant correlations, uniformly in the base size M. It needs no input from the
Sussman-Alpoge account.

## Plan (at most eight steps)

1. Read the sources: skeleton S1 lines (36, 128, 180, 217, 342, run 1 Part 4 P2 P3, 548-559),
   gap-assume-opus.md Section 3.4, gap-twist-chart.md and its check file, other gap-twist-*.md.
2. Fix the exact statement and the setup (twist convention, action, observables, what
   "rate c/n" means, uniformity in M). Record the classical minimum of the twisted thin action.
3. Classical part: the twisted action minimum per thin 2-torus fibre; lower bound on the
   action in terms of distance to the minimum manifold (a coercivity/Lojasiewicz type bound);
   explicit n-dependence.
4. Small-field part: the Gaussian (Hessian) around the minimum manifold; spectral gap of the
   fluctuation operator restricted to the thin directions; zero modes (moduli) and their fate.
5. Effective 2D model on the base (Z/M)^2: what the thin torus reduces to; decay mechanism
   (massive modes plus residual moduli); the n- and beta-dependence of the rate.
6. Large-field (bad-region) estimate: state it as one named lemma; prove what can be proved
   (Peierls-type suppression exp(-c beta) per bad plaquette versus entropy).
7. U(1) check and SU(2)-specific inputs.
8. Assembly: what is PROVED, what is OPEN; RESULT line.

## Work log (appended step by step)

### Step 1 (reading), part 1

Short names: SK = D/library/gap-skeleton-final.md; R1 = D/library/gap-skeleton-max.md (run 1);
AS = D/library/gap-assume-opus.md; CH = D/library/gap-twist-chart.md.

- READ SK:36. S1 and S2 of section 7 do not use the account.
- READ SK:75. Lattice Lambda(n, M) = (Z/n)^2 x (Z/M)^2. A^tw(U) = sum_{p not in P_0} (1 - (1/2) tr U_p)
  + sum_{p in P_0} (1 + (1/2) tr U_p); P_0 = the (1,2)-plaquettes at (x_1, x_2) = (n-1, n-1).
  mu^tw = Z^{-1} exp(-beta A^tw) dU. The twist-eating V: U_1 = i sigma_1 on links with x_1 = n-1,
  U_2 = i sigma_2 on links with x_2 = n-1, all others 1; A^tw(V) = 0.
  Note: this is the Wilson weight exp(beta tr U_p / 2) with a sign flip (beta -> -beta) on P_0,
  up to the constant factor exp(-beta |P|); a change of variables U -> z U on one link per P_0
  plaquette shows it is the standard 't Hooft twist.
- READ SK:77. "The minimum of the action is one gauge orbit with stabilizer +-1 (Facts 1, 2), and the
  Hessian has the gap (2 sin(pi/2n))^2 on the transverse space (Fact 3). The pair (i sigma_1, i sigma_2)
  does not exist for U(1)."
- READ SK:83 (T2 = S1 in the perturbed form): covariance of gauge-invariant F, G in [-1, 1] over base
  sets X, Y is at most C(n, beta) size(X) size(Y) exp(-(c/n) dist(X, Y)), beta >= beta_0(n), all M, all W
  with norm at most eps_0(n); c absolute.
- READ SK:180. S1 = T2 with W = 0, "No account input", needs gap-twist-chart and gap-twist-lat.
- READ SK:217. Queue order 3 of worker 1: gap-twist-chart, then gap-twist-lat: theorem S1;
  source R1 Part 4, P2, P3, lines 548-559.
- READ SK:301-312 (Section 13.2). (CH) proved by Claude Fable 5.2 medium (row 679), checked line by line
  by Claude Opus 5.5 high (row 695, D/library/gap-twist-chart-check.md). Not proved there: the chart over
  base regions with holes, derivative bounds of U -> X, the bad-region bound.
- READ SK:342-343. S1 (plain Wilson weight, fixed n) "is still a target of its own";
  gap-twist-lat and gap-twist-bad not queued "until T2 is stated again".
- READ AS:476-484 (Section 3.4). S1 is unqueued by priority, not by a block. Skeleton (ARGUED there):
  (i) small fields via (CH); (ii) large fields cost beta delta_0(n) per plaquette; (iii) a 2D cluster
  expansion in the base with locality (CH)(c); (iv) the centre ambiguity is fixed by the twist.
  Hard step named there: charts over base regions with holes (class in H^1(D; Z_2)) and the bad-region
  estimate.
- READ R1:548-552 (P2) and P2-next (gap-twist-bad): for a connected set D of base blocks of side n,
  Z_D/Z <= exp(-(beta delta_0(n)/2 - C n^4) |D|); fixes beta_0(n) ~ n^4 log n / delta_0(n).
- READ R1:554-558 (P3, P3-next gap-twist-polymer): after the chart the good-region weight is
  exp(-(beta/2)(X, K X) - R(X)), K >= (2 sin(pi/2n))^2 on the transverse space, |R(X)| <= C beta |X|^3;
  needs a tree bound for the Ursell functions with decay c/n. "The proof must not use the fractional
  instanton as a solution (2.9, correction 7)."
- READ CH (all 262 lines). Theorem (CH) over a rectangle B of the base with free base boundary:
  (a) chart U^h = V exp(X), X transverse (D_0^* X = 0), sup |X| <= C(n) sqrt(delta), unique up to the
  centre among charts with sup |X| <= eps_1(n); (b) A^tw(U) >= (mu_n/16) sum_l |X_l|^2,
  mu_n = (2 sin(pi/2n))^2 >= 4/n^2; (c) locality at rate alpha_n/2 >= 1/(3n).
  Lemma L (CH:92-97): |d omega|^2 + |d^* omega|^2 >= mu_n |omega|^2 on all cochains, every colour.
  Lemma G (CH:103-111): Green function of Delta_0 decays at rate alpha_n = sqrt(mu_n/8).
  Lemma R Step C (CH:146-150): the sign field e_a(b) is a flat Z_2 field on the base; on a rectangle
  it is a pure gauge. CH 8.4 (CH:237-243): over a region with holes the class in H^1(D; Z_2) is an
  extra datum (argued, not written out). Constants (CH:197-206): C(n) = 6.1e4 n^9,
  delta_0(n) = (eps_2/C(n))^2 ~ n^{-32}, eps_2 = min(1/(4200 C_3 n^7), 1/(13 C_4 n)).
  Open there: Jacobian of U -> X (needed for the change of variables), holes, bad regions.

### Step 1 (reading), part 2

- READ R1:503 (Fact 2, last sentence): "With a periodic base there are also the holonomies of the two
  base cycles; they commute with P_a and P_b, so they are +-1: four minima, exchanged by the centre
  flips of the base." So on (Z/n)^2 x (Z/M)^2 the zero set of A^tw is four gauge orbits.
- READ R1:505 (Fact 3) and CH:92-97 (Lemma L): every colour component is antiperiodic in at least one
  fibre direction, so the transverse Hessian has the gap mu_n.
- READ R1:287 (B14, U(1) test): "a pair of non-commuting transition functions does not exist in U(1).
  There the twist is a constant flux, the photon is neutral and stays massless."
- READ R1:436 (2.9, correction 7): the fractional instanton that saturates the bound is numerical,
  not proved; (W-twist) must not use it.
- READ R1:442 (2.10): Tanizaki-Unsal footnote on centre-symmetry breaking at intermediate couplings
  (large N, one site). Not relevant at fixed n and large beta, but it is the failure mode of (AC').
- READ D/library/gap-ds-gauge.md:85-95, 186-191 (row 691). The finite-box criterion needs (W), a bound
  uniform over ALL boundary values. Line 191: "both hypotheses are suprema over all boundary values,
  rough ones included". (Used in Step 7: for the twisted thin torus a uniform-in-boundary statement
  fails below an exponentially large scale; ARGUED there.)
- READ D/library/gap-twist-port.md:157 (row 684, interface to T2): only for T1's class; not used here.
- D/library/twisted-order-calculus.md (head read): a constant-flux charged-sector calculus on Z^4;
  not the thin torus; not used.
- No other file D/library/gap-twist-*.md exists at this commit (ls: chart, chart-check, port).

### Revised plan (after reading; still at most eight steps)

The reading shows two named hard steps (AS:482): (H1) charts over base regions with holes,
(H2) the bad-region estimate. The plan now attacks them first (hardest first), then the U(1) check,
then the assembly.

2. Setup and exact statement (twist, observables, rate, uniformity in M; parity of M).
3. Theorem BAD: the bad-region estimate by reflection positivity in the BASE directions and the
   chessboard estimate (rebuilt), with a lower bound on Z. Explicit in n, beta, delta.
4. Theorem CH-D: the chart over a connected good base region D with holes; the class in H^1(D; Z_2).
5. The small-field form: local Taylor bound of the action in the chart; the Gaussian rate.
6. U(1) check, and the list of SU(2)-specific inputs.
7. What is missing: one named lemma (the polymer step), stated exactly; why a finite-box criterion
   uniform in boundary values cannot replace it (ARGUED); thresholds beta_0(n).
8. Assembly and RESULT.

## Step 2. Setup and the exact statement

**Lattice.** Lambda = Lambda(n, M) = (Z/n)^2 x (Z/M)^2. A site is y = (x, b), x in (Z/n)^2 (fibre),
b in (Z/M)^2 (base). Links (y, mu), mu = 1..4; plaquettes (y; mu < nu). The base point of a link or
plaquette is the base point of its first site. Per base point there are n^2 sites, 4 n^2 links and
6 n^2 plaquettes (n^2 in each of the six planes).

**Measure.** dmu^tw = Z^{-1} exp(-beta A^tw(U)) prod_l dU_l, dU normalized Haar, A^tw as in SK:75,
defect d_p(U) as in CH:23 (d_p = 1 - (1/2) tr U_p off P_0, 1 + (1/2) tr U_p on P_0), so
A^tw = sum_p d_p and 0 <= d_p <= 2. Since exp(-beta A^tw) = e^{-beta |P|} exp(sum_p s_p beta tr U_p / 2)
with s_p = -1 on P_0 and +1 elsewhere, mu^tw is the Wilson SU(2) measure with weight
exp(beta tr U_p / 2) and the sign of beta reversed on the stack P_0 (one fibre plaquette per base
point): the 't Hooft twist n_12 = 1 in the thin plane. (Elementary; PROVED by the display.)

**Observables.** F : SU(2)^{links} -> [-1, 1], measurable and invariant under all gauge
transformations, depending only on the links whose two ends lie over a base set X ("F over X").
dist(X, Y) is the l^1 distance on the base torus; |X| is the number of base points.

**Target (S1), as SK:83 with W = 0.** For each n >= 2 there are beta_0(n) < infinity, an absolute
c > 0 and C(n, beta) < infinity such that for beta >= beta_0(n), all M, all F over X and G over Y:
    |mu^tw(F G) - mu^tw(F) mu^tw(G)| <= C(n, beta) |X| |Y| exp(-(c/n) dist(X, Y)).

**Symmetries used below (PROVED, by inspection).**
(i) Base translations b -> b + a preserve P_0 (P_0 is the full stack over every base point), so they
    preserve mu^tw.
(ii) Base reflections R: b_3 -> 2j - b_3 (j an integer), and the same in b_4. They act on links by
    (R U)_mu(x, b) = U_mu(x, Rb) for mu = 1, 2, 4 and (R U)_3(x, b) = U_3(x, Rb - e_3)^{-1}. A
    (1,2)-plaquette at b goes to the (1,2)-plaquette at Rb with the same orientation, so P_0 goes to
    P_0; a plaquette in a plane containing direction 3 goes to a plaquette with reversed orientation,
    and tr U^{-1} = tr U in SU(2). So A^tw(RU) = A^tw(U), and Haar measure is invariant under
    inversion and relabelling. R is a symmetry of mu^tw. On the torus Z/M it is well defined for
    every M; for M even it has two fixed planes, b_3 = j and b_3 = j + M/2.
(iii) Base centre flips (multiply every direction-3 link over one slice b_3 = j by -1) preserve every
    plaquette (each plaquette contains 0 or 2 of these links): a symmetry. A gauge-invariant F over a
    set X that contains no non-contractible base loop is invariant under it (on links over such an X
    the flip is a gauge transformation by +-1). The four zero sets of A^tw (READ R1:503) are exchanged
    by these flips.

**Good and bad.** For delta > 0 a base point b is delta-bad for U if some plaquette with base point b
has d_p(U) > delta; otherwise delta-good.

**Parity.** Step 3 uses reflection positivity, which needs M even. Statements for odd M are marked.

## Step 3. Theorem BAD: the bad-region estimate (hard step H2), by reflection positivity in the base

Credit. Reflection positivity of lattice gauge measures is due to Osterwalder and Seiler (1978); the
chessboard estimate is due to Frohlich, Israel, Lieb and Simon (1978). Neither paper was read for this
row. Both lemmas are rebuilt below in full (the run-length proof of the chessboard estimate is the
textbook one as I recall it); nothing below rests on a citation.

Throughout this step M is even, M >= 4, and beta >= 1. (For M = 2 every closed cell is the whole base
and the cell map t -> g_t of 3.2 is not unique; M >= 4 is used there.)

### 3.1 Lemma RP (PROVED)

Fix j and R = R_j : b_3 -> 2j - b_3 (Step 2 (ii)). Let Lambda_+ be the sites with
b_3 in {j, j+1, ..., j+M/2} and Lambda_- = R(Lambda_+); they meet in the two planes b_3 = j, j + M/2.
A link or plaquette lies in Lambda_+ if all its sites do. Every link and every plaquette lies in
Lambda_+ or in Lambda_- (its sites have at most two consecutive values of b_3). Let A_+ be the bounded
measurable functions of the links in Lambda_+, and (RF)(U) := F(RU).
**Claim.** On real F, G in A_+ the form <F, G> := mu^tw(F . RG) is symmetric and positive
semidefinite. Hence mu^tw(F . RG)^2 <= mu^tw(F . RF) mu^tw(G . RG).
*Proof.* L_0 = links in both halves (links of directions 1, 2, 4 in the two planes; R fixes each of
them, since Rb = b there); L_+ = the other links in Lambda_+; L_- = the other links in Lambda_-.
The map U_{L_-} -> (RU)_{L_+} is a relabelling with inversions, so it preserves Haar measure.
Split the plaquettes into P_pl (in a plane), P_+ (in Lambda_+, not in a plane) and P_- = R(P_+), and
A^tw = A_+ + A_- + A_pl accordingly. Since d_p(RU) = d_{Rp}(U) (Step 2 (ii)), A_+(RU) = A_-(U) and
A_pl(RU) = A_pl(U). So exp(-beta A^tw) = E . RE with E = exp(-beta (A_+ + A_pl/2)) in A_+. Then
    Z <F, G> = int dU_{L_0} [int dU_{L_+} F E] [int dU_{L_-} (G E)(RU)] = int dU_{L_0} g_F g_G,
with g_F(U_{L_0}) = int dU_{L_+} (F E)(U_{L_0}, U_{L_+}): the second inner integral equals g_G after the
change of variables U_{L_-} -> (RU)_{L_+}, because (RU)_{L_0} = U_{L_0}. Symmetric and >= 0. QED.
The same holds for the reflections in direction 4. The twist enters only through P_0, which R maps to
P_0; nothing else about the group or the twist is used.

### 3.2 Lemma CB, the chessboard estimate (PROVED)

*Cells.* For t in T := (Z/M)^2 the closed cell Q_t is the base set {t_3, t_3+1} x {t_4, t_4+1}; A(Q_t)
are the functions of the links whose two ends lie over Q_t. Let G be the group of base isometries
generated by all R^{(3)}_j, R^{(4)}_j. In one direction G consists of b -> b + 2k and b -> 2j - b; the
first maps {0, 1} to {2k, 2k+1}, the second to {2j-1, 2j}. So for each t there is exactly one g_t in
G with g_t(Q_0) = Q_t (translation if t_i is even, reflection if odd, in each direction), and
R^{(3)}_j g_t = g_{t'} with t' = (2j - 1 - t_3, t_4). Put (theta_t f)(U) := f(g_t U), with g U defined
as for R; theta_t maps A(Q_0) to A(Q_t).
**Lemma CB.** For bounded measurable f_t >= 0 in A(Q_0), t in T,
    mu^tw( prod_t theta_t f_t ) <= prod_t [ mu^tw( prod_{s in T} theta_s f_t ) ]^{1/M^2}.
*Proof.* Xi(f) := mu^tw(prod_t theta_t f_t) for a family f = (f_t). (1) Fix R = R^{(3)}_j. The cells
with t_3 in {j, ..., j+M/2-1} lie over Lambda_+, the others over Lambda_-. So prod_t theta_t f_t =
A . RB' with A = prod_{t right} theta_t f_t and B' = prod_{t left} theta_{t'} f_t, both in A_+. By
Lemma RP, Xi(f)^2 <= Xi(f^->) Xi(f^<-), where f^-> copies the right half onto the left by the mirror
t -> t' and f^<- copies the left half onto the right. (2) Normalise. If every Xi(f_t const) > 0, put
h_t = f_t Xi(f_t const)^{-1/M^2}; Xi is multilinear, so it suffices to show Xi(h) <= 1 when every
constant family has Xi = 1. (If some Xi(f_t const) = 0, apply the result to f_t + eta and let eta -> 0.)
Let C be the finite set of families with entries among the h_t, and L := max_C Xi >= 1 (constants
are in C). (3) Columns. For a family f and c in Z/M the column f(c, .) is a map Z/M -> {h_t}. Among
maximisers choose f with the longest cyclic run of equal consecutive columns, a, ..., a+k-1, and
suppose k < M. Take j = a + k. If k <= M/2 the run lies in the left half, and f^<- has the run and
its mirror image side by side: a run of 2k > k columns. If k > M/2 the left half lies inside the run,
and f^<- has all columns equal. In both cases L^2 = Xi(f)^2 <= Xi(f^->) Xi(f^<-) <= L Xi(f^<-), so
f^<- is a maximiser with a longer run: a contradiction. So some maximiser has all columns equal.
(4) Rows. Reflections in direction 4 act on all columns alike, so they keep families with equal
columns. The argument of (3) in direction 4, among maximisers with equal columns, gives a constant
maximiser. Hence L = Xi(h_t const) = 1 for some t. QED.

### 3.3 Lemma Z, a lower bound on the partition function (PROVED)

**Lemma Z.** For beta >= 1 and every M: Z >= exp(-n^2 M^2 (6 log beta + 27)).
*Proof.* Let r = beta^{-1/2} <= 1 and B = {U : rho(U_l, V_l) <= r for every link}. For U in B and
every plaquette, rho(U_p, z_p) <= 4r by the rules (R1), (R2) (READ CH:25), and d_p = 1 - cos(rho/2)
<= rho^2/8 <= 2 r^2 (off P_0, z_p = 1 and (1/2) tr U_p = cos(rho(U_p, 1)/2) by CH:23; on P_0, z_p = -1
and d_p = 1 - (1/2) tr(-U_p) with rho(-U_p, 1) = rho(U_p, -1)). So beta A^tw <= 12 n^2 M^2 on B.
Write U_l = V_l exp(X), |X| = 2 psi; normalised Haar measure has density (2/pi) sin^2 psi on
psi in [0, pi]. So Haar{rho(U_l, V_l) <= r} = (2/pi) int_0^{r/2} sin^2 psi d psi = (r - sin r)/(2 pi)
>= (19/120) r^3/(2 pi) >= r^3/40 for r <= 1 (alternating Taylor series). With 4 n^2 M^2 links:
log Z >= 4 n^2 M^2 (-log 40 - (3/2) log beta) - 12 n^2 M^2 >= -n^2 M^2 (6 log beta + 27). QED.

### 3.4 Theorem BAD (PROVED)

**Theorem BAD.** Let n >= 2, M even with M >= 4, beta >= 1, 0 < delta <= 2. For every set S of base points,
    mu^tw( every b in S is delta-bad ) <= eps^{|S|},   eps = eps(n, beta, delta) := 6 n^2 beta^{6 n^2} e^{27 n^2} e^{-beta delta / 4}.
*Proof.* Choose for each b in S a plaquette p_b with base point b; the event lies in the union of the
(6 n^2)^{|S|} events {d_{p_b} > delta for all b in S}. Fix one choice. The plaquette p_b lies over the
closed cell Q_b. Put q_b := g_b^{-1}(p_b), a plaquette over Q_0, f_b := 1{d_{q_b} > delta}, so that
theta_b f_b = 1{d_{p_b} > delta}; and f_t := 1 for t not in S. Lemma CB bounds the probability by
prod_{b in S} mu^tw(d_{g_s q_b} > delta for all s in T)^{1/M^2}. A plaquette lies over at most four
closed cells (its base set is a point, an edge or a face), and g_s q_b lies over Q_s, so s -> g_s q_b is
at most 4-to-1: the event asks at least M^2/4 distinct plaquettes to have defect above delta. On it
A^tw >= delta M^2/4, so its probability is at most e^{-beta delta M^2/4} / Z (Haar measure is
normalised and A^tw >= 0). Lemma Z gives the M^2-th root at most e^{-beta delta/4} beta^{6n^2} e^{27n^2}.
Sum over the choices. QED.

**Corollary BAD-b (the form of R1:552, PROVED).** For disjoint base sets B_1, ..., B_k of at most m
points each, mu^tw(each B_i contains a delta-bad point) <= (m eps)^k. For blocks of side n:
    Z_D / Z <= exp( -(beta delta/4 - 6 n^2 log beta - 27 n^2 - log(6 n^4)) |D| )
for every set D of blocks, connected or not. R1:552 asked for exp(-(beta delta_0/2 - C n^4)|D|) on
connected D. The form here has 1/4 for 1/2 and an entropy 6 n^2 log beta + O(n^2) for C n^4: smaller
in n, larger by log beta. Either form fixes the threshold below.

**Threshold.** With delta = delta_0(n) of CH:203 and a := 48 n^2 / delta_0(n):
eps <= exp(-beta delta_0(n)/8) for all beta >= beta_BAD(n) := 4 a log(4 a)
= (192 n^2 / delta_0(n)) log(192 n^2 / delta_0(n)).
*Check.* Need beta delta_0/8 >= 6 n^2 log beta + 27 n^2 + log(6 n^2). For n >= 2,
27 n^2 + log(6 n^2) <= 29 n^2, so it suffices that beta/2 >= a log beta and beta/2 >= 232 n^2/delta_0.
For a' >= e, beta >= 2a' log(2a') implies beta >= a' log beta (the function beta - a' log beta
increases for beta > a' and is >= a'(log 2a' - log log 2a') >= 0 at 2a' log 2a'); take a' = 2a.
And 4a log(4a) >= 192 n^2 log(768)/delta_0 >= 464 n^2/delta_0. (PROVED.)
Sizes: delta_0(n) is of order n^{-32} (CH:206), so beta_BAD(n) is of order n^{34} log n, explicit up to
the absolute constants C_3, C_4 of CH:121-129. If the chart held with delta_0 of order n^{-4} (CH:234,
OPEN there), beta_BAD would be of order n^6 log n.

**Remarks.**
1. (PROVED) Nothing in 3.1-3.4 uses SU(2) beyond compactness and a small-ball volume bound
   Haar{rho <= r} >= c r^{dim G}; the twist enters only as a set P_0 that the base reflections preserve.
   The same theorem holds for U(1) and for the untwisted torus. So the U(1) filter is not passed here:
   it is passed (or failed) in the small-field part (Steps 4-6).
2. (PROVED) The bound is for the torus measure itself, for every set S, uniformly in even M. It is not
   a bound for conditional measures with fixed boundary values: chessboard estimates need the full
   reflection-symmetric torus.
3. (OPEN) Odd M. For odd M each reflection has one site plane and one link plane; RP for the link
   plane is the Osterwalder-Seiler positivity of exp((beta/2) tr(A B^{-1})), but the cell structure of
   3.2 (one g_t per cell) fails. Theorem BAD is not proved here for odd M.
4. What this closes. AS:482 named "the bad-region estimate" as one of the two hard steps of S1, and
   R1:552 (gap-twist-bad) asked for it with blocks of side n. Theorem BAD proves it, for even M, in a
   stronger form (any set, no connectedness). It is unchecked by another model.

## Step 4. Theorem CH-D: the chart over a good base region with holes (hard step H1)

CH 8.4 (CH:237-243) indicates this argument and leaves it unwritten. Here it is written out as a list of
the changes to the proof of (CH), each change proved. The rectangle case is the checked theorem
(row 695); the changes below are mine and unchecked.

**Objects.** D is a set of base points (in Z^2 or in the base torus). K_D is the 2-complex with
vertices D, edges the base links with both ends in D, faces the base unit squares with four corners in
D. Sigma_D: the sites over D, the links with both ends over D, the plaquettes with four sites over D.
Then Sigma_D = F x K_D as cell complexes, F the fibre torus: a plaquette of Sigma_D is a fibre face
over a vertex, a fibre edge times an edge of K_D, or a fibre vertex times a face of K_D. d_D is the path
metric of the graph (D, edges of K_D). A Z_2 1-cochain e on the edges of K_D is flat if the product of
e around each face of K_D is 1; H^1(K_D; Z_2) is flat cochains modulo coboundaries
(e ~ e . delta zeta, (delta zeta)_a(b) = zeta(b) zeta(b + e_a)). A flat e acts on base links as the
central element e_a(b) at every fibre point.

**Theorem CH-D (PROVED; unchecked).** Fix n >= 2. Let D be connected and U a configuration on Sigma_D
with d_p(U) <= delta <= delta_0(n) for every plaquette of Sigma_D (for example: every point of D is
delta-good). Constants C(n), eps_1(n), delta_0(n), C_c(n) are those of CH:197-206. Then:
(a') There is a flat Z_2 cochain e on K_D, with a class [e] in H^1(K_D; Z_2) that depends only on the
gauge orbit of U, such that for every flat representative eps of [e] there is a gauge transformation h
with U^h = eps V exp(X), X transverse (D_0^* X = 0 at every site of Sigma_D), sup |X| <= C(n) sqrt(delta).
X does not depend on the representative. Among charts with the same eps and sup |X'| <= eps_1(n),
h' = +-h and X' = X. So X is a gauge-invariant function of U.
(b') sum over the plaquettes of Sigma_D of d_p(U) >= (mu_n/16) sum over the links of Sigma_D of |X_l|^2.
(c'') Locality in the path metric: if U' on Sigma_{D'} has all defects <= delta' <= delta_0(n), and
R := {b in D : d_D(b, b_0) <= r} (r a non-negative integer) is also the d_{D'}-ball of radius r about b_0
in D' with the same edges and faces, and U = U' on the links over R, then for every link l at b_0,
|X_l(U) - X_l(U')| <= C_c(n) (sqrt(delta) + sqrt(delta')) exp(-r/(3n)).

**Proof: the changes to CH.**

(1) Lemma L on Sigma_D. On cochains of Sigma_D = C(F) (x) C(K_D), the coboundary is
d = d_F (x) 1 + gamma_F (x) d_K, gamma_F = (-1)^degree on fibre cochains. This is CH's d of CH:76 with
the factors 1, 2 grouped into F and the base part restricted to the subcomplex K_D (D_0, D_1 of CH:46-47
are cellular coboundaries, and K_D is a subcomplex, so the restriction is again a coboundary). The cross
terms of d^* d + d d^* are (d_F gamma_F + gamma_F d_F) (x) d_K^* and its adjoint; d_F raises the degree
by one, so gamma_F d_F = -d_F gamma_F and the cross terms vanish. Hence
    d^* d + d d^* = Delta_F (x) 1 + 1 (x) Delta_K,   Delta_K >= 0.
Every tau is diagonal in colour and the central field eps does not enter tau (Ad of a central element is
1). For each colour c the factor i(c) of F is antiperiodic (CH:35), and the chain fact (CH:90) with (2.1)
on F alone gives Delta_F >= mu_n in every degree. So |d omega|^2 + |d^* omega|^2 >= mu_n |omega|^2 on
every cochain of Sigma_D: Lemma L (i), (ii) hold on Sigma_D with free boundary of D. (This is the
statement of CH:242, now proved.)

(2) Lemma G on Sigma_D. Its proof (CH:103-111) uses Lemma L, that a site has at most 4 base neighbours,
a 1-Lipschitz weight phi across base links, and the sum over b' of exp(-t |b - b'|_1) over Z^2.
On Sigma_D take phi 1-Lipschitz for d_D (for example phi = -d_D(., b(y))); then (i) holds with
d_D(b(y), b(y')) in place of |b(y) - b(y')|_1, and since d_D >= |.|_1 on Z^2 (and >= the torus distance
on the torus), (ii) holds with the same K_n = 25 n^6. On the base torus the sum over b' is at most the
sum over Z^2 (send each torus point to its nearest preimage).

(3) Lemma R. Steps A and B (CH:137-144) use one fibre and one base link at a time: unchanged on
Sigma_D. They give fibre gauges h_b and signs e_a(b) on the edges of K_D. Step C, first half (CH:146):
for each face of K_D the product of the four signs is within theta + 4 eps_0 < 2 pi of 1, so it is 1: e is
flat. Second half, changed: let eps be a flat representative of [e]. Since K_D is connected and
e . eps is flat and in the trivial class, e . eps = delta zeta for some zeta : D -> {1, -1}. Put
h(x, b) := zeta(b) h_b(x). Fibre links do not change (central factors cancel at the two ends). A base link
becomes zeta(b) zeta(b + e_a) (h_b U h_{b+e_a}^{-1})_a = e_a(b) eps_a(b) (h_b U h_{b+e_a}^{-1})_a, within
eps_0 of e_a(b)^2 eps_a(b) = eps_a(b). So U^h = eps V exp(X^0) with sup |X^0| <= eps_0.
*The class does not depend on the choices.* Two fibre gauges over b that both bring the fibre links
within eps_f of V differ by g_b with rho(g_b(x), z_b) <= 2.4 n (2 eps_f) for a sign z_b (the first part of
the proof of Lemma Q, CH:174, uses only the fibre over one base point; READ CH:214 says so). The signs
computed from the two choices differ by z_b z_{b+e_a}, a coboundary. A gauge transformation of U is
absorbed in the fibre gauges. So [e] is a function of the gauge orbit of U.

(4) Lemma T (CH:168-170). (eps V e^{X^0})^{exp lambda} = eps V exp(F(lambda, X^0)) because eps is central,
so the fixed-point problem is the one of CH:170 on Sigma_D, solved with Lemma G on Sigma_D. Unchanged.

(5) Lemma Q (CH:174-177) with a fixed eps. If (eps V e^X)^g = eps V e^{X'}, then on each link
g(y) eps_l V_l e^{X_l} g(y+mu)^{-1} = eps_l V_l e^{X'_l}, and eps_l cancels. The rest is CH's proof; it
uses that Sigma_D is connected, which holds since D is. Independence of the representative: if
U^h = eps V e^X then U^{zeta h} = (eps . delta zeta) V e^X, so the representative eps . delta zeta has
the same X; by uniqueness every chart with that representative and small X has this X.

(6) Part (b) (CH:181-193). In E_p of (1.1) the central factors cancel: a mixed plaquette (fibre edge
times base edge) contains eps_a(b) twice, at two fibre points, once inverted; a base face of K_D contains
the product of eps around the face, which is 1 by flatness; fibre plaquettes contain no eps. So E_p, Y_p
and the bound are those of CH 7, with the sums over the plaquettes and links of Sigma_D.

(7) Part (c'') (CH:208-229). Replace the l^1 ball by the d_D-ball R. It is connected (each point joins b_0
by a geodesic inside R). Step 1 of CH:214 needs one sign z over R: choose for U and U' the same fibre
gauges h_b over R (U = U' there), so e = e' on the edges of R, and use the representatives eps = e on
K_D and eps' = e' on K_{D'}; then eps = eps' over R, the central factors cancel as in (5), and Step 1
holds. Steps 2-4 use R^o = {d_D <= r - 1}, R^oo = {d_D <= r - 2}, a weight w = exp(-(alpha_n/2) d_D(., b_0))
(1-Lipschitz exponent, so (2) applies), and the fact that every link of Sigma_D at a site over R^o has
both ends over R. All hold in the path metric. The constant is unchanged. QED.

**Corollary CH-T (the base torus; PROVED).** For D = the whole base torus (every base point
delta_0-good), H^1 = Z_2^2 and U is gauge equivalent to eps V e^X with eps one of four classes: the four
sectors of R1:503, now with the chart around each. The class is the base Z_2 holonomy.

**What CH-D does not give (OPEN).** Derivative bounds for U -> X (the Jacobian of the change of
variables to (gauge orbit, X)); CH:258 lists the same gap. CH-D is a statement for one configuration;
the expansion of Step 7 needs it for all good regions at once, which it gives, since D is arbitrary.

(Citation note: the CH line numbers in Steps 1-4 were corrected against the file by grep after Step 4;
all CH:n citations now point to the lines of D/library/gap-twist-chart.md at this commit.)

## Step 5. The small-field form: Taylor bound and the Gaussian rate

**Lemma TB (PROVED).** There is an absolute C_5 such that, on Sigma_D with U^h = eps V e^X as in
CH-D and sup |X| <= eps_2(n) (CH:201), for every plaquette p of Sigma_D:
    | d_p(U) - (1/8) |(D_1 X)_p|^2 | <= C_5 |u_p|^3,
where u_p is the vector of the four link values of X on p (|u_p|^2 = sum of |X_l|^2 over the four links).
Hence beta A^tw = (beta/8) <X, K_V X> + R(X), K_V = D_1^* D_1, |R(X)| <= C_5 beta sum_p |u_p|^3.
*Proof.* By CH-D (6), d_p = 1 - cos(|Y_p|/2), Y_p = (D_1 X)_p + Q_p, |Q_p| <= (C_4/2) |u_p|^2 (CH:121-129,
(3.2)). Each of the four terms of (D_1 X)_p has norm |X_l| (tau is an isometry), so
|(D_1 X)_p| <= 2 |u_p|. Then ||Y_p|^2 - |(D_1 X)_p|^2| <= |Q_p| (2 |(D_1 X)_p| + |Q_p|)
<= (C_4/2)(4 + (C_4/2)|u_p|) |u_p|^3 <= 3 C_4 |u_p|^3, since |u_p| <= 2 eps_2 <= 2/(13 C_4 n) <= 1/C_4
(so (C_4^2/4)|u_p| <= C_4/4).
And |1 - cos(t/2) - t^2/8| <= t^4/384 for all real t (alternating series bound for t <= 1, and the
bound for |Y_p| <= 1 is what is used: |Y_p| <= 4 eps_2 + 2 C_4 eps_2^2 <= 1 by CH:187). With
|Y_p| <= 2|u_p| + (C_4/2)|u_p|^2 <= 3 |u_p| <= 1: t^4/384 <= 81 |u_p|^4/384 <= |u_p|^3. So C_5 = 3 C_4/8 + 1.
(The bound |1 - cos s - s^2/2| <= s^4/24 holds for all real s.) QED.
This is the input form of R1:558 (gap-twist-polymer): "|R(X)| <= C beta |X|^3 link by link".

**Lemma GR, the Gaussian rate (PROVED).** On Sigma_D (any D, free boundary), let
Delta_1 = D_1^* D_1 + D_0 D_0^* on link fields. Then Delta_1 >= mu_n (CH-D (1)), and for
a_n := sqrt(mu_n/192) >= 1/(7n), every colour and all links l, l':
    |Delta_1^{-1}(l, l')| <= (2/mu_n) exp(-a_n d_D(b(l), b(l'))).
The same holds for Delta_0^{-1} with rate alpha_n = sqrt(mu_n/8) (CH:103, Lemma G (i), extended by CH-D (2)).
*Proof.* Combes-Thomas as in CH:106. Delta_1(l, l') is non-zero only if l and l' share a site or a
plaquette. A link lies in at most 6 plaquettes (CH:183), each with 3 other links, and each end of l
carries at most 7 other links: at most 32 links l' != l. Two distinct links share at most one plaquette
and at most two sites (two sites only when n = 2), so each entry of D_1^* D_1 is at most 1 and each
entry of D_0 D_0^* at most 2 in absolute value: |Delta_1(l, l')| <= 3. For phi 1-Lipschitz in d_D and
T = e^{a phi} Delta_1 e^{-a phi}: <u, T u> >= <u, Delta_1 u> - (cosh a - 1) 96 |u|^2 >= (mu_n/2)|u|^2 when
96 a^2 <= mu_n/2 (cosh a - 1 <= a^2 for a <= 1). So ||e^{a phi} Delta_1^{-1} e^{-a phi}|| <= 2/mu_n;
take phi = -d_D(., b(l')). And a_n = sqrt(mu_n/192) >= (2/n)/sqrt(192) >= 1/(7n). QED.

**What GR means.** On transverse fields D_0^* X = 0, so <X, K_V X> = <X, Delta_1 X> >= mu_n |X|^2,
and Delta_1 commutes with the transverse projection Pi = 1 - D_0 Delta_0^{-1} D_0^* (from d d = 0:
Delta_1 D_0 = D_0 Delta_0). The Gaussian measure exp(-(beta/8) <X, K_V X>) on transverse fields has
covariance (4/beta) (Delta_1^{-1} - D_0 Delta_0^{-2} D_0^*) (the density is exp(-(1/2) <X, (beta/4) K_V X>);
D_1 D_0 = 0 by d d = 0 for the product complex of CH:76), whose kernel decays at rate >= 1/(7n) in the
base, uniformly in D and beta. This is the tree-level gap of SK:77 in kernel form, with the rate c/n,
c >= 1/7 for the kernel. (PROVED, from GR and the identity.)

**What is not here (OPEN).** (i) The Jacobian J(X) of the change of variables from Haar measure on
Sigma_D to (gauge orbit) x (transverse X): it is the Haar density in exponential coordinates times a
Faddeev-Popov determinant det(D_0^* D_{0,X}) / det(Delta_0), D_{0,X} the linearised gauge action at
eps V e^X. Its logarithm is a sum of local terms with decay a_n by GR, if the determinant is expanded
as log det(1 + Delta_0^{-1} B(X)) with |B(X)| <= C sup |X|; this is ARGUED, not written. (ii) The
expansion itself (Step 7).

## Step 6. The U(1) check, and what is specific to SU(2)

**Setting.** Same lattice; U_l = e^{i theta_l} in U(1); theta_p the plaquette angle;
A^tw_{U(1)} = sum_{p not in P_0} (1 - cos theta_p) + sum_{p in P_0} (1 + cos theta_p). Put
phi_p = theta_p off P_0 and phi_p = theta_p - pi on P_0, so d_p = 1 - cos phi_p.

**Proposition U1 (PROVED).**
(i) No flat twisted configuration: for every U and base point b, the sum of theta_p over the n^2 fibre
plaquettes at b is 0 mod 2 pi (each fibre link occurs in two of them with opposite signs), so the
sum of phi_p is pi mod 2 pi. Hence A^tw_{U(1)} >= (2/n^2) M^2 > 0 for every U. *Proof of the bound:*
with representatives phi_p in (-pi, pi], sum |phi_p| >= pi, so sum phi_p^2 >= pi^2/n^2 by
Cauchy-Schwarz, and 1 - cos phi >= (2/pi^2) phi^2 on [-pi, pi]. In U(1) the twist does give a
positive classical minimum (a flux pi through each fibre). In SU(2) it gives the minimum 0 (A^tw(V) = 0,
CH:33), because the flux is eaten by the pair (Gamma_1, Gamma_2).
(ii) The flat directions survive. Let U* have fibre angles phi_p = pi/n^2 on every fibre plaquette (a
fibre connection with any prescribed angles of total 0 mod 2 pi exists, since the image of the
coboundary into R/2piZ-valued 2-cochains of the fibre torus is the kernel of the sum), the same at
every base point, and base links 1; then the mixed and base plaquettes have angle 0. U* is a critical
point of A^tw_{U(1)}: the first variation is sum_p sin(phi*_p) (dX)_p = sin(pi/n^2) sum_b
(sum of (dX)_p over the closed fibre torus at b) = 0. Its Hessian sum_p cos(phi*_p) (dX)_p^2 is >= 0.
For f : (Z/M)^2 -> R put X_1(x, b) = f(b), X_2 = X_3 = X_4 = 0. Then d^* X = 0 (transverse), the fibre
and base plaquettes have dX = 0, the (1, a) plaquettes have dX = f(b) - f(b + e_a), so
    Hess(X, X) / |X|^2 = <f, (-Delta_base) f> / |f|^2,
which is 4 sin^2(pi/M) for a lowest non-constant Fourier mode, and 0 for f constant (a harmonic,
exactly flat direction). So the transverse Hessian of the twisted U(1) action has no gap uniform in M:
the fibre-constant parts of X_1, X_2 are massless fields on the base. In SU(2) the same transverse
Hessian is >= mu_n >= 4/n^2 for every M (Lemma L, CH-D (1)).
(iii) Where the difference sits: in SU(2), Ad(Gamma_1) = diag(1, -1, -1) and Ad(Gamma_2) = diag(-1, 1, -1)
(CH:35) have no common fixed vector, so every colour is antiperiodic in a fibre direction; in U(1),
Ad = 1 and every component is periodic.

**What U1 does not prove (ARGUED).** That S1's conclusion fails for U(1). The massless modes of (ii)
are, at the level of the action, a pair of compact scalars on the base (the phases of the fibre
Polyakov loops) with stiffness of order beta; a two-dimensional compact scalar at large stiffness has
power-law decay (Frohlich and Spencer, 1981; not read here). So for U(1) the fibre Polyakov-loop
correlation is expected to decay as a power of the distance at large beta. A proof would need that
theorem for this model; it is not attempted.

**Where the proof of S1 uses SU(2) (READ/PROVED, item by item).**
1. A^tw(V) = 0 needs Gamma_1 Gamma_2 Gamma_1^{-1} Gamma_2^{-1} = -1 (CH:33). No abelian group has it.
2. G3 (CH:119): a pair whose commutator is near -1 is near (Gamma_1, Gamma_2) up to conjugation. It uses
   the quaternion form of SU(2). This is the step that removes the moduli (Lemma R, Step A).
3. G2 (CH:117): the elements fixed by conjugation with Gamma_1 and Gamma_2 are near the centre {1, -1}:
   the stabiliser of V is finite. In U(1) it is all of U(1).
4. Lemma L (CH:92-97) via Ad(Gamma_i) as in (iii): the gap mu_n. In U(1) it fails by (ii).
5. The base Z_2 field (Step C, CH-D (3)) and the four sectors are the centre Z_2 of SU(2).
6. Theorem BAD (Step 3) and Lemma Z use no property of SU(2) beyond compactness and small balls.
So the U(1) filter is passed exactly at items 1-4, all in the small-field part, as the brief expects.
(For SU(N) with the clock and shift twist eaters the adjoint splits into non-trivial characters of
Z_N x Z_N, and items 1-4 should hold with mu replaced by (2 sin(pi/(N n)))^2: ARGUED, not used;
compare the count READ R1:347.)

## Step 7. What is missing, two warnings about the statement, and the thresholds

### 7.1 Corollary BAD-s: a small-field threshold at the fluctuation scale (PROVED)

Theorem BAD holds for every delta in (0, 2]. Fix kappa >= 0 and put
    delta_1 = delta_1(n, beta, kappa) := (4 kappa + 24 n^2 log beta + 116 n^2) / beta.
Then eps(n, beta, delta_1) = exp(log(6 n^2) - 2 n^2 - kappa) <= e^{-kappa} (log(6 n^2) <= 2 n^2 for n >= 2),
so for even M and every set S: mu^tw(every b in S is delta_1-bad) <= e^{-kappa |S|}.
If beta >= beta_SF(n, kappa) := max(4 a log(4 a), (8 kappa + 232 n^2)/delta_0(n)), a = 24 n^2/delta_0(n),
then delta_1 <= delta_0(n) (same argument as the threshold of 3.4), and CH-D applies on every connected
delta_1-good region with sup |X| <= C(n) sqrt(delta_1) = C(n) beta^{-1/2} (4 kappa + 24 n^2 log beta + 116 n^2)^{1/2}:
fields of the fluctuation size beta^{-1/2}, up to n-dependent and logarithmic factors. On such regions
Lemma TB gives |R(X)| <= C_5 beta sum_p |u_p|^3 with |u_p| <= 2 C(n) sqrt(delta_1), so the cubic term per
plaquette is at most 8 C_5 C(n)^3 (beta delta_1)^{3/2} beta^{-1/2}, small once beta is a large power of n
times a power of log beta. (PROVED, by Theorem BAD, CH-D and TB.)

### 7.2 Proposition FLUX: the forced vortex (PROVED)

Let H be a finite set of base points and D a connected region with D union H a rectangle R and H
enclosed by D (every base point of R next to H that is not in H lies in D). Let gamma be a closed
edge path in K_D around H. If U is delta_0-good on D and the class [e] of CH-D (a') takes the value -1 on
gamma, then H contains a delta_0-bad point.
*Proof.* Otherwise every point of R is delta_0-good. CH-D on R gives a flat sign field e_R, in the trivial
class (R is a rectangle). With the same fibre gauges over D, e_R restricted to D is a sign field for U on
D, so by CH-D (3) (independence of the choices) it represents [e]. Its product around gamma is the
product of a coboundary on R: +1. Contradiction. QED.

### 7.3 Two warnings about the statement of S1 (ARGUED; heuristic, no proof)

**W1. A finite-box criterion uniform in the boundary values cannot give S1 at the scale n.** Row 691's
Theorem W needs (W), a bound uniform over all boundary values (READ D/library/gap-ds-gauge.md:85, :191).
For a base box Q with good boundary values of flux -1 around Q, Proposition FLUX forces a bad point in
Q. A smooth vortex costs an action of order one in units of beta (about pi^2 beta in the continuum
reading, READ R1:285), wherever it sits, so its position in Q is spread over Q, and the law of the
centre of Q under flux -1 differs at order one from the law under flux +1. Boxes in which flux -1 is
not rare must have area at least of order 1/rho, rho the vortex density, of order exp(-c beta). So a
criterion of the type of (W) can hold only at scales exponentially large in beta: this matches
Proposition B of D/library/gap-ds-gauge.md:165 (READ), which forces R to be at least the correlation
length, here with the correlation length of the Z_2 flux, not the 1/n of the massive modes.

**W2. The |X| |Y| form of S1 (SK:83) for large Y needs the area law and a huge constant.** Take F a
"vortex detector" over a ball X of radius s at b_0, and G = W_Gamma the base Wilson loop at one fibre
point around a square Gamma of side 2r about b_0, so |Y| is about 8r and dist(X, Y) about r. In the
dilute-vortex picture W_Gamma is (-1)^{(number of vortices inside Gamma)} times a perimeter factor
exp(-a |Gamma|) with a of order 1/beta. Flipping the sign of every vortex activity inside Gamma changes
mu(F) by an amount of order rho s^2 that does not decay in r, so
    |Cov(F, W_Gamma)| is about rho s^2 <W_Gamma>,   <W_Gamma> about exp(-8 a r - sigma (2r)^2),
with string tension sigma of order rho. For S1 with rate c/n this needs
C(n, beta) >= exp((c/n - 8a)^2 / (16 sigma)) up to powers, which for beta >> n is doubly exponential in
beta. If sigma were 0, S1 in this form would be false at large beta, since a ~ 1/beta < c/n. So the
|X| |Y| form of S1 contains an area law (with a constant of that size). A cluster expansion gives
naturally a prefactor C^{|X| + |Y|} for general F, G, which is weaker for large Y.

**Proposed restatements (to be decided by the lead; both are what T3 and T4 consume).**
(S1-loc) For |X|, |Y| <= K: |Cov(F, G)| <= C(n, beta, K) exp(-(c/n) dist(X, Y)).
(S1-T) The transfer matrix of mu^tw in a base direction (it exists by Lemma RP) has a spectral gap
at least c/n on the complement of its top eigenvector, uniformly in M: equivalently
|Cov(F, G)| <= 2 exp(-(c/n) d) for |F|, |G| <= 1 on the two sides of a pair of base planes at distance d.
(S1-T) implies (S1-loc) with rate c/(2n) (two sets of diameter at most K at distance d are separated in
one base direction by at least (d - 2K)/2). (S1-T) is the form R1 N4 (SK:85) uses for the Hamiltonian.

### 7.4 The one missing lemma

**Lemma PE (restricted-ensemble expansion; OPEN).** For each n >= 2 there are beta_PE(n), an absolute
c_PE > 0 and, for each K, C(n, beta, K), such that for beta >= beta_PE(n), every even M, and all
gauge-invariant F over X and G over Y with values in [-1, 1] and |X|, |Y| <= K,
    |Cov(F, G)| <= C(n, beta, K) exp(-(c_PE/n) dist(X, Y)),
and the transfer-matrix form (S1-T) with the same rate.
PE is (S1-loc) and (S1-T). What is proved for it here, and what its proof still needs:
- Large fields at two thresholds, delta_0(n) and delta_1 ~ n^2 log beta / beta, as unconditional Peierls
  bounds for every set of points: PROVED (Theorem BAD, Corollary BAD-s). Still needed: the local
  (conditional) activity form for a bad region with a given small-field exterior, with thresholds
  chosen so that the matching cost at the region's boundary (of order beta C(n)^2 delta_1 per boundary
  plaquette) is below the Peierls gain. OPEN; standard in kind.
- Small fields: chart on every connected good region with holes, the Z_2 class as a datum (CH-D,
  PROVED); cubic Taylor bound (TB, PROVED); Gaussian kernel decay at rate >= 1/(7n) (GR, PROVED).
  Still needed: (J) the Jacobian of the change of variables (Haar density in exponential coordinates
  times the Faddeev-Popov ratio det(D_0^* D_{0,X})/det(Delta_0)) as exp of a sum of local terms with decay
  a_n and bounded derivatives. OPEN; this is also the open item of CH:258.
- The decoupling of the massive Gaussian across blocks of side of order n log beta (an interpolation of
  the covariance in the style of Glimm, Jaffe and Spencer, or a finite-range decomposition), the sum over
  the Z_2 labels of holes, and the convergence of the polymer gas. OPEN; standard in kind. The closest
  model with a gauge field is the mass-gap proof for Higgs models on a unit lattice by Balaban, Brydges,
  Imbrie and Jaffe (1984), and the restricted-ensemble method of Borgs and Imbrie (1989); neither was
  read for this row, and nothing here rests on them. In the twisted thin torus the role of the Higgs
  field is played by the fibre holonomies, and the Landau-gauge ghost operator Delta_0 is itself massive
  (Lemma L (i)), so no massless mode appears at any step.
The statement R1:558 (gap-twist-polymer) is the expansion step of PE with the bad-region input; with
Theorem BAD and CH-D proved, PE is the single remaining item of S1 in the forms (S1-loc), (S1-T).

### 7.5 Thresholds and the rate

beta_0(n) for S1 is max(1, beta_BAD(n), beta_SF(n, kappa_*), beta_PE(n)), with kappa_* the
Peierls constant PE needs (an absolute number for a polymer gas on Z^2 with blocks of side ~ n log beta;
not computed). beta_BAD(n) = (192 n^2/delta_0(n)) log(192 n^2/delta_0(n)) and beta_SF are explicit up to
the absolute constants C_3, C_4 of CH (both of order n^{34} log n, from delta_0(n) of order n^{-32});
beta_PE(n) is not known. Rate: the Gaussian kernel decays at rate >= 1/(7n) (GR) and the chart is local
at rate 1/(3n) (CH (c)); an expansion loses a fixed fraction of the rate, so c_PE of order 1/14 is the
expectation (GUIDE: no computation behind the number).

### 7.6 GUIDE run (discharges nothing)

Script: scratchpad/lane842/scripts/guide_hessian.py (this row's scratchpad), run on the Mac mini
(numpy 2.0.2, one BLAS thread, nice 10, peak 186 MB, 0.35 s); output in scripts/guide_hessian.out.
Lattices (Z/n)^2 x (Z/M)^2 with a PERIODIC base (the torus case of CH-D, Corollary CH-T), built from
the definitions of CH:46-47 with the signs of CH:35.
Criteria written before the run, and the outcome:
(1) D_1 D_0 = 0, SU(2) each colour and U(1): PASS in all cases (exactly 0).
(2) SU(2): least eigenvalue of Delta_1 and of Delta_0 "equals mu_n" for each colour. As written this
    FAILED for colour 3 (index c = 2): its value is 2 mu_n (n = 2: 4.0; n = 3: 2.0). The criterion was
    wrong, not the claim: colour 3 is antiperiodic in both fibre directions, so the chain fact gives
    mu_n + mu_n. Colours 1 and 2 give exactly mu_n. So every colour is >= mu_n and the minimum over
    colours is mu_n, for (n, M) = (2, 4), (2, 6), (3, 4): this is what CH-D (1) states.
(3) U(1) at U*: gradient 0; exactly 4 zero modes on the transverse space (the harmonic constants);
    least positive eigenvalue = 4 sin^2(pi/M) to six digits ((n, M) = (2, 8): 0.585786; (3, 6): 1.000000).
    PASS. This agrees with Proposition U1 (ii): no gap uniform in M for U(1).

## Step 8. Assembly

**S1 is not proved here.** Nothing in this file was checked by another model. "Even M" means even
M >= 4 throughout.

**PROVED (by hand, this file; unchecked).**
| Item | Statement | Where |
|---|---|---|
| Lemma RP | the twisted measure is reflection positive for base reflections through site planes (any compact group) | 3.1 |
| Lemma CB | chessboard estimate on closed base cells (even M) | 3.2 |
| Lemma Z | Z >= exp(-n^2 M^2 (6 log beta + 27)), beta >= 1 | 3.3 |
| Theorem BAD | mu(every b in S delta-bad) <= (6 n^2 beta^{6n^2} e^{27 n^2} e^{-beta delta/4})^{|S|}, every set S, even M | 3.4 |
| Cor. BAD-b | R1:552's bad-region estimate for blocks of side n, any set D of blocks; beta_BAD(n) = (192 n^2/delta_0) log(192 n^2/delta_0) | 3.4 |
| Cor. BAD-s | Peierls factor e^{-kappa} per point at the threshold delta_1 = (4 kappa + 24 n^2 log beta + 116 n^2)/beta | 7.1 |
| Theorem CH-D | the chart (CH) over any connected good base region, with holes; the class in H^1(K_D; Z_2) as datum; locality in the path metric | 4 |
| Cor. CH-T | on the base torus: four sectors, each with a chart | 4 |
| Lemma TB | beta A^tw = (beta/8)<X, K_V X> + R, |R| <= C_5 beta sum_p |u_p|^3, C_5 = 3 C_4/8 + 1 | 5 |
| Lemma GR | Delta_1^{-1} kernel decays at rate >= 1/(7n); transverse Gaussian covariance (4/beta)(Delta_1^{-1} - D_0 Delta_0^{-2} D_0^*) | 5 |
| Prop. FLUX | Z_2 flux -1 around a hole of a good region forces a bad point in the hole | 7.2 |
| Prop. U1 | U(1): positive classical minimum (>= 2 M^2/n^2) but flat directions survive; transverse Hessian at the critical point U* has 4 zero modes and eigenvalue 4 sin^2(pi/M) -> 0 | 6 |

**READ.** SK:36, 75, 77, 83, 180, 217, 301-312, 342-343; AS:476-484; R1:285, 287, 347, 349, 436,
442, 503, 505, 548-558; CH in full (262 lines), cited by line; D/library/gap-ds-gauge.md:85, 165, 191.

**ARGUED.** W1 (7.3): no finite-box criterion uniform in boundary values at scales below about
exp(c beta). W2 (7.3): the |X| |Y| form of SK:83 for large Y contains an area law and forces
C(n, beta) to be doubly exponential in beta; proposed forms (S1-loc), (S1-T). U(1) power-law decay via
Frohlich-Spencer (Step 6). SU(N) extension (Step 6). Locality of log J (Step 5).

**GUIDE.** 7.6 (one criterion misformulated for colour 3, reported; no claim rests on the run).

**OPEN.**
1. Lemma PE (7.4), the one missing lemma: the restricted-ensemble expansion, giving S1 as (S1-loc) and
   (S1-T). Inside it: (a) the local (conditional) activity form of the Peierls bound, with thresholds
   chosen against the boundary matching cost; (b) the Jacobian (J) of the change of variables, with the
   Faddeev-Popov ratio (also CH:258); (c) the decoupling of the massive Gaussian across blocks, the sum
   over Z_2 labels of holes, and convergence. beta_PE(n) unknown.
2. Theorem BAD for odd M (3.4, remark 3).
3. S1 in the literal |X| |Y| form for large Y (needs an area law; T3 of SK:84 is the related node).
4. delta_0(n) of the natural size n^{-4} (CH:234); it would lower beta_BAD from about n^{34} log n to
   about n^6 log n.

**Dependence on n and beta (as far as proved).** Peierls factor per base point
6 n^2 beta^{6 n^2} e^{27 n^2} e^{-beta delta/4}; small-field threshold delta_1 of order n^2 log beta/beta;
chart size C(n) sqrt(delta), C(n) = 6.1e4 n^9; Gaussian rate >= 1/(7n), chart locality 1/(3n);
beta_0(n) >= beta_BAD(n), of order n^{34} log n with the constants of CH (explicit up to C_3, C_4).

**SU(2)-specific inputs.** Items 1-4 of Step 6 (the anticommuting pair, G3, G2, Lemma L via Ad);
all in the small-field part. Theorem BAD is group-free. The U(1) filter is passed at Lemma L and fails
for U(1) exactly there (Proposition U1 (ii); GUIDE 7.6 (3)).

**Credits.** The chart (CH): Claude Fable 5.2 medium (row 679), checked line by line by Claude Opus 5.5
high (row 695). Run 1 (R1, B14 and P2-P3): Claude Fable 5.2 max (row 669). The skeleton SK: the lead,
Claude Fable 5.2 (row 676). The assumptions exercise AS: Claude Opus 5.5 max (row 838). Row 691
(gap-ds-gauge): Claude Fable 5.2 medium. The twisted thin torus and the tree-level count:
't Hooft; Tanizaki and Unsal, arXiv:2201.06166 (read by run 1, not here). Reflection positivity:
Osterwalder and Seiler; chessboard estimates: Frohlich, Israel, Lieb and Simon; the expansion methods
named in 7.4: Glimm, Jaffe and Spencer; Balaban, Brydges, Imbrie and Jaffe; Borgs and Imbrie; the
two-dimensional power law: Frohlich and Spencer. None of these papers was read for this row; every
lemma used from them is rebuilt here, and none is load-bearing as a citation.

**Suggested next rows (the lead decides).** (i) A check, by a model that did not write this file, of
Lemma RP, Lemma CB (the run-length step), Theorem BAD, and CH-D (1), (3), (7). (ii) An author row on
Lemma PE in the form (S1-T), starting from Corollary BAD-s, CH-D, TB and GR, with (J) as its first
sub-lemma. (iii) A decision on restating S1 (7.3, W2) before PE is queued.

RESULT: S1 not proved; its two named hard steps are proved by hand (unchecked): the bad-region estimate (Theorem BAD, by base reflection positivity and a rebuilt chessboard estimate: mu(every b in S is delta-bad) <= (6n^2 beta^{6n^2} e^{27n^2 - beta delta/4})^{|S|} for every set S and even M >= 4, giving beta_0(n) of order n^34 log n with the chart's delta_0) and the chart over good regions with holes (Theorem CH-D, Z_2 class as datum), plus a cubic Taylor bound, Gaussian kernel rate >= 1/(7n) and the U(1) check (the twist leaves massless directions in U(1): transverse Hessian eigenvalue 4 sin^2(pi/M); the SU(2) inputs are the anticommuting pair, G2, G3 and Lemma L); missing: one lemma PE (the restricted-ensemble expansion: local Peierls activities, the Faddeev-Popov Jacobian, Gaussian decoupling, Z_2 labels), and S1 should be restated in bounded-support or transfer-matrix form, since the |X||Y| form for large loops needs an area law (ARGUED).
