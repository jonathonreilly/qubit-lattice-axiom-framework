# Check of library/gap-crux2-astra62.md (FINISH row 1142)

Status: COMPLETE (2026-11-18). All six steps are done. The verdict table
and the RESULT line are at the end. This research check grants no status.

Checker: Claude (Opus 5.5), checker role. Verdicts are per statement:
HOLDS, HOLDS AFTER CORRECTION, FAILS.

## Plan (six steps)

1. Read the file under check, the brief, and the cited passages of row 1018
   (Lemmas FLOW, PROJ, FR+, NAB, items 7-10) and its check.
2. Check (1), the one-link estimate (3) with Z_kappa and M_b, the
   two-plaquette bound (4) with the Gram step, (5) and (6).
3. Check the density estimate (7), the choice of m, the amplitude step,
   theorem (2), the counterexample to P and the frame-defect size.
4. Check the bare estimate (8), the tree gauge, the Gauss identity (10), the
   local polynomial (11), the conditional density bound e^(12bs) and the
   small-value probability.
5. Check the packing, the tree count 8^(V-1), the net, (9), exact failure,
   (12), (13) and the comparison lines. Numeric guides where useful.
6. Verdict table and RESULT line.

## Log

- Step 0 done: output file created.
- Step 1 done (2026-11-18). Read in full: `library/gap-crux2-astra62.md`
  (230 lines, the file under check, cited below as F<line>);
  `library/gap-council-brief.md`. Read in `library/gap-short-step-max.md`
  (row 1018): lines 1-359, which hold FLOW (217-231), PROJ (233-245), FR+
  (247-255), SPLIT and line 269, the sizes at 271-276 (line 273 is the
  request that (8) answers), NAB (306-319) and section 5.5 (FL, DEC).
  Read in `library/gap-short-step-check-astra.md`: lines 1-60 and items
  6-14 (lines 140-265), which include items 7-10.
- Not read, so not checked as citations: rows 1011, 1013 (C8 and its
  check lines 110-111), 1026, 1027, 1034, 1051, 1057, 1128, 884, and the
  Sussman-Alpoge outline lines cited at F15 and F152. Where the file uses
  one of these as a proof step, I check the step directly by hand instead
  (the tree Haar factorization at F152, the commutator at F161).

## Step 2. Statements (1), (3), (4), (5), (6)

Conventions used in my check: a unit quaternion is q = q_0 + u; the
inner product on R^4 is <a,b> = Re(a conj(b)); for an imaginary c,
Re(c h) = -c.Im h. The Wilson weight is exp{b sum_p (1/2) tr U_p} (F19).
The force on a link e, in the frame of its tail, is
N_e = b sum_{p containing e} Im h_p, where h_p is the holonomy based at
the tail and oriented to start along e. Then X(c on e) = -c.N_e. This
matches PROJ (row 1018 line 215 and 238).

**S1. Identity (1), F33-41. HOLDS.** T = Ad U_xy is orthogonal, so
|eta_x n_x - eta_y T n_y|^2 = eta_x^2 + eta_y^2 - 2 eta_x eta_y n_x.T n_y.
The right side of (1) expands to the same expression, because
|n_x - T n_y|^2 = 2 - 2 n_x.T n_y. The identity holds for every real eta;
eta >= 0 is needed only to read the second sum as a non-negative cost.
The value does not depend on the orientation of a bond, since
|s_x - T_xy s_y| = |T_yx s_x - s_y|. The remark at F41 (a bump with slopes
O(1/R) gives P if the second sum is paid by K sum |grad eta|^2) is a correct
count: (1+K) O(R^(d-2)) against sum eta^2 of order R^d.

**S2. One-link law, F55. HOLDS.** For a plaquette p through the link e,
(1/2) tr U_p = Re(q g) = <q, conj g> after a cyclic shift, or
Re(conj(q) g) = <q, g> when e occurs inversely; |g| = 1. With periods at
least three the six plaquettes through e are distinct and each meets e once.
So the conditional density is e^{h.q}/Z_kappa with h = b sum of six unit
vectors, kappa = |h| <= 6b, and Z depends on kappa only (SO(4) invariance
of Haar). For a plaquette holonomy with three links fixed,
h_p = g_1 q^(+-1) g_2 is the image of q under an orthogonal map of R^4 that
preserves Haar on S^3, so its law is e^{h'.h_p}/Z_kappa with |h'| = kappa.

**S3. Pushforward and fibre average, F57. HOLDS.** phi(q) = Ad q n
satisfies phi(gq) = Ad g phi(q), so phi pushes Haar to an SO(3)-invariant
law on S^2, the uniform one. phi(q) = phi(q') iff q^(-1) q' commutes with n,
so the fibre is the circle q exp(tn) = q cos t + (qn) sin t. The vectors q
and qn are orthonormal in R^4 (Re(q conj(n) conj(q)) = Re conj(n) = 0), so
the fibre is a great circle in the plane P they span. On it
h.(q cos t + qn sin t) = v cos(t - t_0) with v = |proj_P h| <= kappa, and
the uniform fibre average is I_0(v) <= I_0(kappa). I_0 is increasing on
v >= 0 by its even power series. The tilted density on S^2 at the image
point is I_0(v)/Z_kappa.

**S4. Z_kappa and its lower bound, F57-64. HOLDS.** In the chart
q = (r cos th, r sin th, sqrt(1-r^2) cos ph, sqrt(1-r^2) sin ph) the three
coordinate vectors are orthogonal with lengths 1/sqrt(1-r^2), r,
sqrt(1-r^2). The volume element is r dr dth dph, of total 2 pi^2, so the
normalized element is (2r dr)(dth/2pi)(dph/2pi). With h = kappa e_1,
h.q = kappa r cos th, and Z_kappa = int_0^1 2r I_0(kappa r) dr. (It equals
2 I_1(kappa)/kappa; this is not used.) On
1 - 1/(2(1+kappa)) <= r <= 1 one has r >= 1/2, so 2r >= 1. The file
states I_0(kappa r) >= e^(-1/2) I_0(kappa) without a reason. The reason is
one line: kappa r cos t >= kappa cos t - kappa(1-r) for every t, and
kappa(1-r) <= kappa/(2(1+kappa)) < 1/2. So
Z_kappa >= e^(-1/2) I_0(kappa)/(2(1+kappa)), and the density is at most
2 e^(1/2)(1+kappa) <= 3.30(1+6b) <= 4(1+6b) = M_b.

**S5. Cap and the cross product, F64. HOLDS.** |w-n|^2 = 2 - 2 w.n, so
the cap |w-n| <= 2t is w.n >= 1 - 2t^2, of area fraction
(1-(1-2t^2))/2 = t^2 for 0 <= t <= 1. For q = cos a + sin a w_hat, Ad q is
the rotation by 2a about w_hat, so |n - Ad q n|^2 = 2(1 - cos 2a)|n_perp|^2
= 4 sin^2 a |n_perp|^2 = 4|u x n|^2.

**S6. Estimate (3), F66-70. HOLDS.** P{|u x n| <= t | other links} =
P{Ad q n in the cap of chord radius 2t} <= M_b t^2, by S2-S5. The bound is
uniform in the conditioning links and in the unit vector n, and it is
stated in the original Wilson law at coupling b.

**S7. Gram step, F79. HOLDS.** With M = u_1 u_1^T + u_2 u_2^T,
sum_i |u_i x v|^2 = v^T((tr M) I - M) v, so the minimum over unit v is
tr M - mu_1(M). M has rank at most two, so its spectrum is
mu_1 >= mu_2 >= 0 = mu_3, the minimum is mu_2, and mu_1, mu_2 are the
eigenvalues of the Gram matrix U^T U (U = [u_1 u_2]). Since
|v - A_i v|^2 = 4|u_i x v|^2 (S5), D/4 is the smaller Gram eigenvalue, in
every rank. For a 2x2 positive semidefinite matrix,
mu_2 = det/mu_1 >= det/tr; det = |u_1 x u_2|^2. On |u_1| >= |u_2| with
u_1 != 0 the trace is at most 2|u_1|^2, so mu_2 >= |u_2 x u1_hat|^2/2 and
D >= 2|u_2 x u1_hat|^2.

**S8. Bound (4), F72-79. HOLDS.** The north-east and south-west squares at
x in the (1,2)-plane have eight distinct bonds, all inside the 3^d cell.
Up to null sets, {D < delta_b} lies in
A_1 = {u_1 != 0, |u_2 x u1_hat|^2 < delta_b/2} union A_2 (indices swapped).
Let e_2 be a link of the second square and F_2 the sigma-algebra of all
other links. Then u1_hat is F_2-measurable, and S6 applied to h_2 with
t^2 = delta_b/2 <= 1/16 gives P(A_1 | F_2) <= M_b delta_b/2. The same holds
for A_2 with a link of the first square. {u_i = 0} = {h_i = +-1} is null
for a law with a density. The sigma-algebra of links outside the cell lies
in F_1 and in F_2, so the tower property gives
P{D < delta_b | outside} <= M_b delta_b = 4(1+6b)/(8(1+6b)) = 1/2.

**S9. Identity (5), F81-87. HOLDS.** For orthogonal A_0 = I, A_1, A_2,
|sum_i A_i v|^2 = 3|v|^2 + 2 sum_{i<j} <A_i v, A_j v>
= 9|v|^2 - sum_{i<j} |(A_i - A_j) v|^2. Dividing by 9 gives (5). On the
event of (4), the right side is at least
(1/9)(|v-A_1 v|^2 + |v-A_2 v|^2) >= D|v|^2/9 >= delta_b|v|^2/9, and
|(A_1-A_2)v|^2 <= 2|v-A_1 v|^2 + 2|v-A_2 v|^2 gives the factor three.

**S10. Bound (6), F87-92. HOLDS.** Around a square x = x_0, x_1, x_2, x_3,
x_0, s_x - A_i s_x = sum_{k=0}^{3} T_{x0x1}...T_{x(k-1)xk}
(s_{xk} - T_{xk x(k+1)} s_{x(k+1)}), a sum of four orthogonal images of bond
differences. Cauchy-Schwarz gives |s_x - A_i s_x|^2 <= 4 sum over the square.
Then (delta_b/9)|s_x|^2 <= (3/9) * 4 * (sum over the eight bonds), which is
(6) with the constant 12/delta_b. Remark, not a correction: the detour
through (5) is not needed for (6). D|s_x|^2 <= sum_i |s_x - A_i s_x|^2
gives the constant 4/delta_b directly. The F94 caveat (the signed
cancellation needed at M is separate) is correct.

- Step 2 done: S1-S10 above. No failure found.

## Step 3. (7), the choice of m, the amplitude step, (2), P, the frame defect

**S11. Density estimate (7), F96-101. HOLDS.** A side of l >= 3 sites holds
floor(l/3) >= l/6 disjoint blocks of three (l = 3, 4, 5 give 1 >= l/6;
l >= 6 gives floor(l/3) >= (l-2)/3 >= l/6). So N >= |B|/6^d. The indicator
G_j of a cell is a function of the eight bonds of its two squares, which lie
inside that cell. For disjoint cells, sigma(G_1, ..., G_(i-1)) lies in the
sigma-algebra of links outside cell i, so S8 and the tower property give
P{G_i = 1 | G_<i} >= 1/2. Then E[3^(-G_i) | G_<i] = 1 - (2/3) P{G_i = 1 | G_<i}
<= 2/3, and iteration gives E 3^(-sum G) <= (2/3)^N. Markov's inequality:
P{sum G < N/4} = P{3^(-sum G) > 3^(-N/4)} <= (3^(1/4) 2/3)^N
= exp(-N (3 log 3 - 4 log 2)/4) = e^(-gamma N), gamma = (1/4) log(27/16)
= 0.1308.

**S12. Choice of m and the union bound, F103. HOLDS.** With
m = ceil((A log(2+R))^(1/d)) one has m^d >= A log(2+R), so every rectangle
has N >= m^d/6^d >= (k+d+1) log(2+R)/gamma and failure probability at most
(2+R)^(-(k+d+1)). Pieces of length m with the remainder (< m) merged give
sides in [m, 2m) when m <= R/2. There are at most R^d rectangles, so the
total failure probability is at most R^d (2+R)^(-(k+d+1)) <= (2+R)^(-k). On
the good event every rectangle has at least N/4 >= rho|B| good roots,
rho = (4 6^d)^(-1). Also m >= 6 for every R >= 0, since
A log 2 >= 15.9 * 6^d > 5^d; so R_0 is fixed by m <= R/2 alone. R_0 does not
depend on b.

**S13. Amplitude step, F105-111. HOLDS.** |f_x - f_y| <= |s_x - T_xy s_y|
is the reverse triangle inequality with |T s_y| = |s_y|. For the variance:
(1/|B|) sum_B (f - fbar)^2 = (1/2) E (f(X) - f(Y))^2 for independent uniform
X, Y. Change the coordinates one at a time; Cauchy-Schwarz gives the factor
d. For the i-th change the other coordinates are uniform on the
cross-section, and on a line of l_i sites
|f(a) - f(b)|^2 <= l_i (sum of squared bond differences on that line). The
average over the line pair and the cross-section is at most
(l_i^2/|B|) E_i, where E_i is the energy of the direction-i bonds of B.
So sum_B (f - fbar)^2 <= (d/2) max_i l_i^2 E_B <= 2 d m^2 E_B, as stated.
At the roots, fbar^2 <= 2(f_x - fbar)^2 + 2 f_x^2, summed over at least
rho|B| roots, gives |B| fbar^2 <= (2/rho) sum_roots [(f_x - fbar)^2 + f_x^2].
The squares of distinct roots lie in distinct cells, so (6) applies on
disjoint bond sets inside B: sum_roots f_x^2 <= (12/delta_b) E_B. With
sum_B f^2 = sum_B (f - fbar)^2 + |B| fbar^2 this gives the display at F113,
with the constant (1 + 2/rho) 2 d m^2 + 24/(rho delta_b).

**S14. Theorem (2), F45-53 and F117. HOLDS.** Summing over the rectangles
and using that the bonds between rectangles add non-negative terms gives
sum |s|^2 <= C E_U(s) with
C = (1 + 8 6^d) 2 d m^2 + 768 6^d (1+6b). Since
m^2 <= 2 (A log(2+R))^(2/d) + 2, C <= C'_{d,k} (1 + b + (log(2+R))^(2/d)).
So (2) holds with c_{d,k} = 1/C'_{d,k}, on the event of S12, of probability
at least 1 - (2+R)^(-k). The event is defined by U alone, and on it the bound
is deterministic in s. So the quantifier over s after the sample (F53) is
correct, and every field-built frame, amplitude or exceptional set is
included. The constants c_{d,k} and R_0(d,k) do not depend on b. Remark:
every estimate used is conditional on the links outside a 3^d cell, so the
same bound also holds conditionally on any exterior of the cube. The file
does not claim this, and nothing below needs it.

**S15. Counterexample to P, F119. HOLDS.** The constants in (2) do not depend
on b (S14). So for any sequence b_R, R^2 times the lower bound is
c R^2/(1 + b_R + (log(2+R))^(2/d)), which tends to infinity when
b_R = o(R^2). On the events of (2), of probability at least
1 - (2+R)^(-k), every nonzero s has Rayleigh quotient above K/R^2 once R is
large. This covers b in [2.3, 2.6] uniformly. For the trajectory,
b_j = O(log(1/a_j)) = O(log R_j) = o(R_j^2). P (F28) asks for an
O(R^(-2)) quotient on a typical cell. Free faces give the least energy, so
the statement also covers other boundary conditions on the same bonds. The
"conditional" label at F119 is right: it assumes the stated growth of
beta_j.

**S16. Size of the defect for a frame, F121. HOLDS.** Take the central cube
of side floor(R/2). Its distance to the outer faces is at least
floor((R - floor(R/2))/2) >= R/4 - 1/2 >= R/8 for R >= 4, so
eta = min(1, dist/that distance) has bond slopes at most 8/R. There are at
most d R^d bonds, so sum |grad eta|^2 <= 64 d R^(d-2). The proof of (7)
needs only sides of at least three, so it applies to the plateau, with
N >= (R/24)^d cells for R >= 16 and failure probability at most
e^(-gamma N) = e^(-c_d R^d). On the complement at least N/4 roots are good.
At each, (6) with |n_x| = 1 gives at least delta_b/12 = 1/(96(1+6b)) on its
eight bonds, where eta_x eta_y = 1. The second sum of (1) is therefore at
least N/(384(1+6b)) >= c'_d R^d/(1+6b), for every unit field n at once. The
ratio to 64 d R^(d-2) is c''_d R^2/(1+6b). The conclusion at F121 follows
for b = o(R^2).

- Step 3 done: S11-S16 above. No failure found.

## Step 4. (8), the tree gauge, (10), (11), the density bound, small values

**S17. Prior geometry, F125. HOLDS as a reading of row 1018 and its
check.** FR+ is at row 1018 lines 247-255 and NAB at 306-319. NAB (iii)
gives E lambda_x >= 1/(3924 beta^2) under xbar >= 3/4 (line 312). Check
items 11-13 restrict the common-mean step to a cubic torus, or to the local
means of item 12. The file's sentence matches this. Rows 1011 (FR) and 1128
(HOL) were not read by me.

**S18. Bare estimate (8), F127-133. HOLDS.** The forward squares at x in
planes 12 and 34 have eight distinct links and the root x. S8 used only
these two facts and S6, which holds for every link of a four-torus with
periods at least three. So P{D >= delta_b} >= 1/2 for this pair. With
lambda_x = min_v sum over the six forward plaquettes of |Im U_p x v|^2 (row
1018 line 308) and D/4 = min_v sum over the pair of |u_i x v|^2 (S5),
dropping four non-negative terms gives lambda_x >= D/4. Hence
E lambda_x >= (delta_b/4)(1/2) = 1/(64(1+6b)), with no mean hypothesis and on
rectangular tori. For b >= 1 this is at least 1/(448 b), which is the
c/beta asked at row 1018 line 273. Where NAB applies (xbar >= 3/4, so b is
not small), (8) is the larger bound. So "strengthens" (F221) is right.

**S19. The constraint paragraph, F135. HOLDS as a reading.** With
(d lambda)_e = lambda(e^-) - lambda(e^+) and div j(z) = sum_{e^- = z} j_e -
sum_{e^+ = z} j_e, summation by parts gives
X((d lambda) n) = -sum_e (d lambda)_e j_e = -sum_z lambda_z div j(z). By the
Gauss law this div j equals -sum_{e^+ = z} (D_e n).N_e, which is PROJ (iii)
(row 1018 line 240). H_c = -E[V Psi_V] - Var(Psi_V) is FLOW (line 225). For
an internal move with zero Haar divergence, E X = 0 and -E[V X] = E X^2
(check item 7). The zero-force odd torus is check item 10. Rows 1026, 1027
and 1034 were not read by me.

**S20. Tree gauge, F152. HOLDS (checked by hand; the outline citation was
not read).** T is a spanning tree of the cell C. Extend it to a spanning
tree T' of the torus. No added link has both ends in C, since T already
spans C. Put g_root = 1 and g_y = g_x U_xy along each T' edge from parent x
to child y. Then every T' link of U^g is 1, and a chord becomes
g_x U_c g_y^(-1), where g_x and g_y depend on tree links only. Given the
tree links, this map preserves Haar on each chord (left and right
invariance). So under product Haar the gauge-fixed chords are product Haar,
independent of the tree links. Gauge invariance of the weight then gives
the law of the chords as W(1 on T', c) times product Haar, normalized. The
transported frame obeys n(U^g)_x = Ad(g_x) n(U)_x because g_root = 1, and
N_e is covariant in the frame of its tail. So j_e and div j are the same in
both gauges, and in the T-gauge the frame equals v at every cell site.

**S21. Gauss identity (10), F152-159. HOLDS.** A gauge rotation exp(eps c)
at z moves each outgoing link by the left generator c and each incoming
link by -Ad(U_e) c. Gauge invariance of the action gives
0 = -c.sum_{e^- = z} N_e + c.sum_{e^+ = z} Ad(U_e)^(-1) N_e for every c.
This is PROJ (ii); on the torus every site is free. In the T-gauge,
n = v on all eight links at a strictly interior z, so
div j(z) = v.(sum_out N_e - sum_in N_e) = v.B_z, as in (10). Each of the
six plaquette terms of N_e has norm at most b, so |N_e| <= 6b,
|(Ad(U_e)^(-1) - I) N_e| <= 12b and |B_z| <= 48b.

**S22. The local polynomial (11), F161-169. HOLDS.** The six plaquettes
through l = (y, y+i) are (y; i, k) and (y-k; i, k), k != i. Only (y; i, j)
contains m = (y, y+j). With every other support link at 1, each of the
other five has holonomy u from y along l. They give 5b Im u, which
Ad(u)^(-1) fixes. The common plaquette, traversed from y along l, has
holonomy u 1 1 w^(-1) = u w^(-1). So
B_z/b = Ad(u)^(-1) Im(u w^(-1)) - Im(u w^(-1)) = Im(w^(-1) u - u w^(-1)).
Directly: w^(-1) u = (9 + 12i - 12j + 16k)/25 and
u w^(-1) = (9 + 12i - 12j - 16k)/25, with difference 32k/25. The general
formula [w^(-1), u] = 2 Im u x Im w gives 2 (4/5)^2 k, the same. The other
incoming links at z carry 1, so they add (Ad(1)^(-1) - I) N_e = 0. The
support count 4 x 6 x 4 = 96 is an upper bound; in fact every support link
lies within max-norm distance 2 of y, so "three" at F175 is safe. The
evaluation point puts 1 on every tree link, so it is admissible for every
tree/chord mask with l, m chords. Conjugating all support links by one g
keeps tree links at 1 and turns B_z into Ad(g) B_z. So for each unit v some
admissible point gives v.B_z/b = 32/25. If the opposite sign convention is
used for N_e, B_z changes sign, and nothing later uses the sign.

**S23. Null zero set and small values, F171. HOLDS.** In the stereographic
chart from -1, q = ((1 - |x|^2) + 2x)/(1 + |x|^2), a polynomial F of degree
D in the quaternion coordinates becomes P(x)/prod_i (1 + |x_i|^2)^D. The
point of S22 has no coordinate equal to -1, so P is not the zero
polynomial. Its zero set is null in R^(3s) (induction and Fubini). Haar has
a smooth positive density in the chart, and the omitted set
{some q_i = -1} is Haar-null. So {v.B_z = 0} is null, and continuity from
above gives P_Haar{|v.B_z| <= 2 eps b} -> 0 as eps -> 0. This probability
does not depend on v (S22, invariance of product Haar under simultaneous
conjugation). There are finitely many masks and direction pairs (i, j), so
q_H(eps) -> 0.

**S24. Conditional density e^(12bs), F173. HOLDS.** In the gauge-fixed law
the conditional density of the s local chords, given all other chords, is
e^S / int e^S with S the sum of the at most 6s plaquette terms that contain
a local chord. Each term b (1/2) tr U_p lies in [-b, b], so the oscillation
of S is at most 12bs, and the density is at most e^(12bs). With b <= 13/5
and s <= 96 this gives q(eps) = e^(12 (13/5) 96) q_H(eps), about
e^2995 q_H(eps). It is finite, so a small enough eps makes q(eps) as small
as needed, uniformly in the torus, in b <= 13/5 and in the outside chords.

- Step 4 done: S17-S24 above. No failure found.

## Step 5. Packing, tree count, net, (9), exact failure, (12), (13), comparisons

**S25. Packing, F175. HOLDS.** Sites with all coordinates in [4, R-5]
number (R-8)^4 >= 3V/4 once R >= 116. Such a y has its four
positive-coordinate bonds inside C. If fewer than two of them are chords, at
least three are tree edges with tail y. Each of the V-1 tree edges has one
tail, so at most (V-1)/3 such y exist, and at least 3V/4 - V/3 = 5V/12 >=
V/3 candidates remain. The support of the test at z = y + i lies within
max-norm distance 2 of y (S22), so "three" is safe. Candidates at mutual
distance at least 7 have disjoint supports, and the greedy step removes at
most 13^4 sites per choice. So N >= V/(3 13^4) >= alpha V with
alpha = (4 13^4)^(-1). The test sites z are at least three layers inside.
All choices use T only.

**S26. Independent small values, F177. HOLDS.** For fixed T and v, the
indicator of a small value at one test depends only on the chords in its
support. Conditioning on all other chords and using S24 gives at most q(eps)
for the last test, and iteration over disjoint supports gives q(eps)^h for
any h specified tests. The union over the sets of ceil(N/2) tests gives at
most 2^N q(eps)^(N/2) = (2 sqrt(q(eps)))^N.

**S27. Tree count, net and union, F180-183. HOLDS.** A spanning tree with a
fixed root is fixed by the parent of each non-root site, one of at most
eight neighbours, so there are at most 8^(V-1) trees. For a net point v'
with |v - v'| <= eps/48, |v.B_z - v'.B_z| <= (eps/48)(48b) = eps b. With
2 sqrt(q) < exp(-(log 8 + 2)/alpha) and N_T >= alpha V, the total exceptional
probability is at most 8^(V-1) M e^(-(log 8 + 2)V) = M e^(-2V)/8 <= e^(-V)
for V >= log M. Off it, for every T and every unit v, more than N_T/2 tests
have |v'.B_z| > 2 eps b, hence |div j^{T,v}(z)| = |v.B_z| > eps b. So
(1/V) sum |div j|^2 >= (alpha/2) eps^2 b^2, which is (9) with
c = alpha eps^2/2. Each event is gauge invariant (S20), so it is an event of
the original Wilson law.

**S28. Statement (9), F141-150. HOLDS.** S20-S27 give it with c and R_1 free
of b in the window, of the torus (beyond containing C) and of the tree. A
change of root on the same tree maps the set {n^{T,v} : |v| = 1} to itself.
For the whole periodic cube with wrap bonds the same steps apply: every site
is interior, the tree count and the packing are unchanged, and R large keeps
the supports from wrapping.

**S29. Exact failure, F185. HOLDS.** If div j^{T,v} = 0 at three test sites,
the unit v is orthogonal to B_z1, B_z2, B_z3, so their determinant vanishes.
In the T-gauge this determinant is a polynomial in the chords of three
disjoint supports. Independent conjugations of the three (11) patterns give
B_zk/b = (32/25) e_k, so the determinant is (32/25)^3 at an admissible
point. Its zero set is Haar-null (S23). The Wilson law, and its conditional
law given the exterior of C, have densities with respect to Haar for every
finite b > 0 (for b = 0 all forces vanish, which is why b > 0 is needed).
The union over the finitely many trees gives probability zero. Since every
support lies inside C, the conclusion holds for every exterior pin, which
is stronger than "almost every".

**S30. Sign average and (12), F187-194. HOLDS.** Summation by parts gives
sum_e (d lambda)_e j_e = sum_z lambda_z div j(z) when lambda vanishes off
interior sites. For independent signs, E_lambda (sum_z lambda_z a_z)^2 =
sum_z a_z^2. The tests lie at least three layers inside (S25), so
restricting lambda to sites at least two layers inside keeps every test, and
then d lambda vanishes on links that touch the outer face. Averaging over
lambda gives E_b sum_z |div j(z)|^2 >= (1 - e^(-V)) c b^2 V for any
measurable choice of tree and axis, so some fixed lambda reaches the average.
For an internal move with zero Haar divergence, E X = 0 and the Jensen cost
-E[V X] is E X^2 (FLOW; check item 7). A gradient has d(d lambda) = 0, so no
bound K sum_p |(d theta)_p|^2 can hold. Supporting remark: for a fixed tree
and a fixed root axis the frame move has zero Haar divergence. Only the tree
link from tail(l) to its parent moves n_tail(l), and it moves it by
2 e_a x n_tail, whose a-component is zero. This agrees with the conditional
use of C8 at F194. C8 itself (row 1013) was not read by me. The caveats at
F194 (Jacobian for adaptive rules, c given by existence, comparison with
the bracket gain open) are accurate.

**S31. Statement (13), F196-202. HOLDS.**
|j_e(n) - j_e(n')| <= |n - n'|_(e^-) 6b, and each site is the tail of four
edges, so ||j(n) - j(n')|| <= 12b ||n - n'||. ||div j||^2 <=
sum_z 8 sum_{e at z} j_e^2 <= 16 ||j||^2. For any T and v, on the event of
(9), sqrt(c) b sqrt(V) <= ||div j(n^{T,v})|| <= ||div j(n)|| +
48 b ||n - n^{T,v}||, the norms taken over interior sites. Taking the
infimum over T and v and dividing by sqrt(V) gives (13). With div j(n) = 0
this gives d_T(n)^2 >= c/48^2. The Jacobian variant is the triangle
inequality.

**S32. Comparison lines, F206-212. HOLDS.** U(1): Ad is the identity, so
D = 0, B_z = 0 and the commutator vanishes. (3) fails because Ad q n = n for
every q. SU(2) x massless: the spectator directions carry the trivial
adjoint, so a constant spectator vector has zero energy, and node M cannot
contract 1 (x) f. Q_8, 2T: a conditional law on a finite group gives
positive mass to holonomy +-1, so P{|u x n| <= t} stays positive as t -> 0,
against M_b t^2. Real parts in Q_8 are 0, +-1, and the extra 16 elements of
2T have real part +-1/2, so 3/5 is absent. Atoms also break the null-set
step: q_H(eps) no longer tends to zero. There is no Lie-algebra force N_e.
Row 884 was not read by me.

**S33. Sector and measure, F214. HOLDS.** div j^{T,v} is gauge invariant
when v is carried with the root gauge, so the minimum over v is invariant
under site gauge maps. A centre-plane flip multiplies by -1 the links in
direction mu that cross one hyperplane. Every plaquette contains zero or
two of them, so all holonomies are unchanged, including h_p based at a tail
and starting along a flipped link (its opposite link is also flipped).
Hence N_e, Ad U_e and the tree transport are unchanged, and so is every
div j^{T,v}.

**S34. Leaf table and RESULT line, F218-230. HOLDS.** Each PROVED entry
matches what S1-S33 verify: (3), (4), (8) for the bare fluctuation; (2) and
(6) for P, with (7) used and (8) not needed there; (9)-(12) for tree frames,
with zero Haar divergence named as the hypothesis of the cost reading; and
(13). The OPEN entries are not claimed. Nothing in the RESULT line goes
beyond (8) and (9).

Not checked, by the scope of the row: the GUIDE paragraphs F11-15 (search
and source pins), F216 (registry comparison) and F228. The citations listed
in Step 1 were not read.

### Numeric guides (no proof step uses them)

Pure-Python scripts in the session scratchpad, not committed: `quat.py`,
`trees.py`, `check_algebra.py`, `check_prob.py`, `check_mc.py`, run with
`python3 -I`. Peak memory was about 18 MB.

- Algebra (3x3x4x3 torus, b = 2.45, Haar links). The force convention
  dS/deps = -c.N_e agrees with finite differences to 2.5e-9. The Gauss law
  holds at every site to 6e-15. max |N_e|/(6b) = 0.75. The (11) pattern
  gives B_z/b = (0, 0, 1.28) for the direction pairs (1,2), (2,1), (3,4),
  (1,4); 32/25 = 1.28. For a random spanning tree with wrap bonds, the tree
  gauge sets the tree links to 1 (to 2e-15), and div j^{T,v}(z) in the
  original gauge equals v.B_z in the tree gauge at every site (to 3e-14).
  Identity (5) holds to 5e-15, D/4 equals the smaller Gram eigenvalue to
  3e-14, and the Gram lower bound held in 2000 samples. The (13) ratios are
  0.22 and 0.35 (each must be at most 1).
- (3) and (4). Z_kappa by quadrature equals 2 I_1(kappa)/kappa. The sup of
  the tilted density is kappa I_0/(2 I_1) = 8.06 at kappa = 15.6, against
  2 e^(1/2)(1+kappa) = 54.7 and M_b = 66.4. With 2e5 samples at
  kappa = 15.6 and tilts along 1, k, i, (1+k)/sqrt2: P{|u x k| <= t} = 0.020,
  0.078, 0.28 at t = 0.05, 0.1, 0.2, against M_b t^2 = 0.17, 0.66, 2.66.
  With both holonomies tilted to 1 at kappa = 15.6, P{D < delta_b} = 0.030,
  against 1/2.
- (11) test. The support has 44 distinct links, all within max-norm
  distance 2 of y. Under product Haar with all support links chords,
  P{|v.B_z|/b <= 2 eps} = 0.0021, 0.0097, 0.027, 0.11 at eps = 0.005, 0.02,
  0.05, 0.2. This is about linear in eps, as q_H(eps) -> 0 needs.
- Heat bath on a 4^4 torus (60 sweeps, then 20 measurements 3 sweeps
  apart). b = 2.3: plaquette 0.605, E lambda_x = 1.31 (smallest 0.116),
  against (8)'s 0.00106. P{D >= delta_b} = 0.992 for both pairs.
  b = 2.6: plaquette 0.669, E lambda_x = 1.16, against 0.00094;
  P{D >= delta_b} = 0.990 and 0.991. For (9) on the whole torus, 15 random
  spanning trees per b gave min_v (1/V) sum |div j|^2/b^2 between 5.2 and
  6.2. The constant in (9) is given by existence and is far smaller.
  Adversarial trees were not sampled.

### Independent derivations (a different method from the file)

- Poincare constant of S13. The Neumann gap of a box is
  4 sin^2(pi/(2 l_max)) >= 4/l_max^2 > 1/m^2, so
  sum_B (f - fbar)^2 <= m^2 E_B. This is below the file's 2 d m^2 E_B.
- Density of S4. With Z_kappa = 2 I_1/kappa and the RECALLED bound
  I_1(x)/I_0(x) >= x/(1 + sqrt(1 + x^2)) (Amos), the sup density is at most
  1 + kappa/2 <= 1 + 3b. This is below M_b. The file's own bound is also
  correct.

- Step 5 done: S25-S34 above, and the guides. No failure found.

## Step 6. Verdict table

F<n> is the line in `library/gap-crux2-astra62.md` at the time of reading.

| # | Statement | Line | Verdict |
|---|---|---|---|
| S1 | Identity (1) | F33-41 | HOLDS |
| S2 | One-link law, kappa <= 6b; plaquette holonomy law | F55 | HOLDS |
| S3 | Uniform pushforward; fibre average I_0(v) <= I_0(kappa) | F57 | HOLDS |
| S4 | Z_kappa = int 2r I_0(kappa r) dr, its lower bound, M_b = 4(1+6b) | F57-64 | HOLDS (one-line reason for I_0(kappa r) >= e^(-1/2) I_0(kappa) supplied) |
| S5 | Cap fraction t^2; abs(n - Ad q n)^2 = 4 abs(u x n)^2 | F64 | HOLDS |
| S6 | Estimate (3) | F66-70 | HOLDS |
| S7 | Gram-matrix step, D/4 = smaller Gram eigenvalue | F79 | HOLDS |
| S8 | Two-plaquette bound (4), delta_b = 1/(8(1+6b)) | F72-79 | HOLDS |
| S9 | Identity (5) | F81-87 | HOLDS |
| S10 | Bound (6), constant 12/delta_b | F87-92 | HOLDS |
| S11 | Density estimate (7), gamma = (1/4) log(27/16) | F96-101 | HOLDS |
| S12 | Choice of m, the partition, the union bound | F103 | HOLDS |
| S13 | Amplitude step, variance bound 2 d m^2 | F105-111 | HOLDS |
| S14 | Theorem (2) | F45-53, F113-117 | HOLDS |
| S15 | Counterexample to P | F119 | HOLDS |
| S16 | Frame-defect size, ratio c'' R^2/(1+6b) | F121 | HOLDS |
| S17 | Prior geometry (reading of FR+, NAB, check items 11-13) | F125 | HOLDS as a reading |
| S18 | Bare estimate (8) | F127-133 | HOLDS |
| S19 | Constraint paragraph (FLOW, PROJ, check items 7-10) | F135 | HOLDS as a reading |
| S20 | Tree gauge and Haar factorization | F152 | HOLDS (by hand; outline citation not read) |
| S21 | Gauss identity (10), abs(B_z) <= 48b | F152-159 | HOLDS |
| S22 | Local polynomial (11), B_z/b = (32/25) k | F161-169 | HOLDS |
| S23 | Null zero set; q_H(eps) -> 0 | F171 | HOLDS |
| S24 | Conditional density e^(12bs); q(eps) | F173 | HOLDS |
| S25 | Packing, N >= alpha V | F175 | HOLDS |
| S26 | Product bound (2 sqrt q)^N | F177 | HOLDS |
| S27 | Tree count 8^(V-1), the net, the union | F180-183 | HOLDS |
| S28 | Statement (9) | F141-150 | HOLDS |
| S29 | Exact failure | F185 | HOLDS (holds for every exterior pin, stronger than stated) |
| S30 | Sign average, (12), cost reading | F187-194 | HOLDS (cost reading conditional on zero Haar divergence, as stated) |
| S31 | Statement (13) | F196-202 | HOLDS |
| S32 | Comparison lines (U(1), SU(2) x massless, Q_8, 2T) | F206-212 | HOLDS |
| S33 | Sector and measure | F214 | HOLDS |
| S34 | Leaf table and RESULT line | F218-230 | HOLDS |

No statement FAILS. No correction is needed.

Remarks, none load-bearing:

1. F61 states I_0(kappa r) >= e^(-1/2) I_0(kappa) without its reason. The
   reason is one line (S4).
2. F87-92: (6) also follows directly with the constant 4/delta_b. The route
   through (5) loses a factor three.
3. F161 and F175: the support of a test has 44 links within max-norm
   distance 2 of y (counted by a script, a guide). The file's 96 and 3 are
   safe upper bounds.
4. The citations named in Step 1, including the Sussman-Alpoge outline
   lines, were not read. Each proof step that leans on one was checked
   directly instead.
5. Provenance. This is one check by a different provider (Claude Opus 5.5)
   of a Codex hand proof. It is not a second independent derivation of every
   step. Independent derivations were made only for the Poincare constant
   and the density bound (above). The numeric runs are guides only.

RESULT: HOLDS. All 34 checked statements of `library/gap-crux2-astra62.md` (row 1141) hold by hand, with no correction: (1), (3) with Z_kappa and M_b = 4(1+6b), (4) with the Gram step, (5), (6), (7) and the choice of m, the amplitude step and theorem (2), the counterexample to P and the frame-defect size, the bare estimate (8) E lambda_x >= 1/(64(1+6b)), the tree gauge and (10), (11) with B_z/b = (32/25)k, the e^(12bs) density and small-value bound, the packing, the count 8^(V-1), the net and (9), exact failure, (12), (13) and the comparison lines; three non-load-bearing remarks (an omitted one-line reason at F61, a constant lost through (5), safe overcounts at F161/F175); the cited rows and the outline lines were not read; numeric guides agree.
