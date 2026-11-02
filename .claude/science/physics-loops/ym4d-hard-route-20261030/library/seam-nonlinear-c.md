lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T20:46Z

# seam-nonlinear-c: nonlinear (NL-pay), (PATCH) and (GLUE-E) at the flat background

Queue row 61, mapped side. Pinned at commit 9793658b6. Author: Anthropic
claude-opus-5-5, effort max, Mac mini worker, 2026-11-02. Same-model work:
not independent in model, not a gate, not an audit, no status.

Status: in progress; sections are written as they are finished. The result
summary at the top is filled in last.

## 1. The statement tested, and criteria fixed before any computation

**Setting.** As in `library/seam-quadratic-c.md` Sections 1 to 5: fine
lattice of unit spacing, L odd, depth n, B = L^n, Q_n, Q_path^(B), C_B, the
tensor maps R, T, Pi and the tensor homotopy h. As in
`library/seam-nonlinear.md` Section 2: a(P) = 1 - Re tr(P)/2, |Z|_F^2 =
tr(Z*Z)/2, (ALIGN) and (SEED). As in `library/seam-nlpay.md`: (PATCH), the
locked pair (PAIR), (LOCK). As in `library/excess-shell-end.md` 4.2: the
replacement cost R_D and (GLUE-E). **Flat background** means: the terminal
parent V has flux at most f <= T_2, with T_2 chosen after L; U is the class
minimizer of the terminal-parent problem with parent V (no frozen fine
links); T is the iterated trial of `parts/hard-core--excess.md` 2.3, with
M_n(T) = V. Top units have side B; for a fine 1-form h, H := B h is its top
normalization, so that, by (SCALE) of `seam-nlpay`,
sum_b |h_b|^4 = ||H||_(L^4)^4 and B^-2 sum_b |h_b|^2 = ||H||_(L^2)^2.

**Questions (queue row 61).**
- Q1. Does the path-gauge primitive H = hG with the chain-map right inverse
  T_n remove the transition-gauge term of (PATCH)?
- Q2. Do they pay the fourth-moment term of (SEED)?
- Q3. Are the remaining nonlinear errors of relative size C(L) x flux,
  uniformly in depth, so that the flux threshold chosen after L absorbs them?
- Q4. (GLUE-E) with exact parent preservation and class membership at every
  intermediate level.

**Registered criteria for the kill test (written before any run).**
1. Identities. Every exact identity used by the hand lemmas below (for the
   locked-pair field H_0 of `seam-nlpay` Section 4: Q_path H_0 = 0,
   G := dH_0 has dG = 0 and C_B G = 0, and hG = H_0 - d(h H_0)) must hold
   to relative error 1e-10. A failure above 1e-8 means a hand step is wrong
   and stops this item there.
2. The claim under test: *the path-gauge primitive is critical*, that is
   sum_b |hG(b)|^4 <= C ||G||_2^4 with C free of B, for closed G with
   C_B G = 0. This is what paying the fourth moment of (SEED) from energy
   alone needs. Record rho_4(B) := sum_b |hG(b)|^4 / ||G||_2^4 and
   sigma_4(B) := sum_p s_p(hG)^4 / ||G||_2^4 for G = dH_0, H_0 the locked
   pair oriented along the first tensor axis, for B = 3, 5, 7, 9, 11 and 13
   if memory allows. REFUTED if rho_4 grows by more than a factor 2 from
   B = 3 to the largest B with log-log slope at least 0.7 over the last two
   points. If it does not grow, the hand lemma of Section 2 has an error and
   I stop to find it. Control: the same pair oriented along the last tensor
   axis must stay bounded (slope below 0.3 over the last two points), and
   the natural representative H_0 itself has sum |H_0|^4 / ||G||^4 = 2/144.
3. What a run can and cannot show. A growing ratio on one explicit field
   only confirms a lower bound that is proved by hand in Section 2. A
   bounded control proves nothing. No statement below rests on a run.

## 2. The path-gauge primitive is not critical (discharged, hand proof; kill test run)

Notation of `seam-quadratic-c` Sections 3 and 4: B = 2m+1, the 1D kernels
zeta_y, eta_c, beta, Lambda, g_1, the 1D homotopy
h a(x) = sum_y zeta_y(x) B^-1 sum_(x'' in I(y)) sigma(x'',x;a), and the 4D
tensor homotopy with Hhat_i = sigma_i(S) [Pi_1 (x) ... (x) Pi_(i-1) (x) h_i
(x) I (x) ... (x) I]. Axes are ordered 1 < 2 < 3 < 4. On a component in the
first axis, Hhat_1 = h (x) I (x) I (x) I: no smoothing at all across the line.

**The field.** The locked pair of `seam-nlpay` Section 4, abelian, amplitude
a > 0 along a fixed unit vector of su(2): with c a top centre and b_+, b_- the
fine bonds in direction 1 based at c + e_2 and c - e_2,

    H_0 := a (delta_(b_+) - delta_(b_-)),     G := dH_0.

**Lemma NC.** For every odd B >= 3 (on Z^4, or on a torus with at least 3
blocks along axis 1 and at least 4 sites along axes 2 to 4):
(a) dG = 0, C_B G = 0, Q_path H_0 = 0, and ||G||_2^2 = 12 a^2.
(b) hG = H_0 - d(h H_0), and |hG| > a/4 on at least 12 m fine bonds, none of
    which is b_+ or b_-.
(c) Hence sum_b |hG(b)|^4 >= (3m/64) a^4 = (m/3072) ||G||_2^4, and
    sum_p s_p(hG)^4 >= (9m/128) a^4, s_p(h) = sum_(b in boundary p) |h_b|.
So there is no constant C free of B with sum_b |hG(b)|^4 <= C ||G||_2^4 on
closed G with C_B G = 0: **the path-gauge primitive is not critical in d = 4.**

*Proof.* (a) dG = ddH_0 = 0. Q_path H_0 = 0 because the kernel q_c(b) of
Q_path depends on the transverse coordinates of b only through the indicator
of the block I(y) (Section 5 of `seam-quadratic-c`), and b_+, b_- have the
same longitudinal position and transverse coordinates in the same block, with
opposite signs. Then C_B G = d'Q_path H_0 = 0 (Corollary 2.3 there). Each of
b_+, b_- lies in 6 plaquettes and they share none (distance 2), so
||G||^2 = 12 a^2.
(b) Lemma 4.1 (b) there on 1-forms: hdH_0 = H_0 - Pi H_0 - d(hH_0), and
Pi H_0 = T R H_0 = T Q_path H_0 = 0. H_0 has only the component S = {1}, on
which every Hhat_i with i >= 2 has h_i on a degree-0 slot and vanishes, so
h H_0 = (h (x) I (x) I (x) I) H_0, that is

    hH_0(x) = a phi(x_1 - c_1) [delta(x_2 - c_2 = 1) - delta(x_2 - c_2 = -1)]
                             delta(x_3 = c_3) delta(x_4 = c_4),

with phi := h(delta_(0,1)) the 1D homotopy of the unit 1-form on the bond
(0, 1). For x >= 1, sigma(x'',x;delta_(0,1)) = [x'' <= 0], so
phi(x) = sum_y zeta_y(x) n_-(y) with n_-(y) := B^-1 #{x'' in I(y): x'' <= 0},
which is (m+1)/B at y = 0, 1 for y <= -B and 0 for y >= B. For 1 <= x <= m,
read off the supports (Lambda(s) > 0 iff |s| < B, beta(s) > 0 iff |s| <= m):
zeta_0(x) = Lambda(x) + 2 g_1 beta(x), zeta_B(x) = x/B - g_1 beta(x),
zeta_(-B)(x) = -g_1 beta(x), and no other zeta_y is nonzero at x. Hence

    phi(x) = (1 - x/B)(m+1)/B + g_1 beta(x) (2(m+1)/B - 1)
           >= ((m+1)/B)^2 + g_1 beta(x)/B > 1/4,

because 1 - x/B >= 1 - m/B = (m+1)/B > 1/2 and 2(m+1) - B = 1. Now take
x_1 - c_1 in [1, m]. The difference d(hH_0) in direction 2 is +-a phi(x_1 - c_1)
on the four bonds based at x_2 - c_2 in {-2, -1, 0, 1} (x_3 = c_3, x_4 = c_4),
and in each of the directions 3 and 4 it is +-a phi on the four bonds that
join the sites x_2 - c_2 = +-1 to their two neighbours along that axis. These
12 bonds are distinct and none is in direction 1, so H_0 vanishes on them and
|hG| = a |phi| > a/4 there; over x_1 - c_1 in [1, m] that is 12 m bonds.
(c) The first bound is 12 m (a/4)^4 against ||G||^4 = 144 a^4. For the
second, each bond lies in 6 plaquettes and s_p^4 >= max_(b in boundary p) |h_b|^4
>= (1/4) sum_(b in boundary p) |h_b|^4, so sum_p s_p^4 >= (6/4) sum_b |h_b|^4. QED

**Where the loss comes from.** Not from the path gauge: H_0 itself has
Q_path H_0 = 0, its contour averages vanish by the reflection of `seam-nlpay`
Section 4, and sum |H_0|^4 = 2 a^4 = ||G||^4 / 72. The homotopy chooses a
different representative of the same curvature, hG = H_0 - d(hH_0): the gauge
function hH_0 is the 1D integral of H_0 along the first axis, with no
transverse smoothing, and its gradient is a string of length about 2B of
size a phi. Averaging the homotopy over the 24 orders of the axes (still a
homotopy for the same Pi, still with R h = 0) keeps the strings of the six
orders in which axis 1 comes first, with weight 1/4 (remark, not used).

**Kill test (criteria of Section 1).** `checks/seamnlc/seamnlc_nc.py`, log
`seamnlc_nc.log`, data `seamnlc_nc.json`; reuses the operators of
`checks/seamqc/seamqc.py`. Torus 3 x 2 x 1 x 1 blocks at B = 3, 3 x 1 x 1 x 1
blocks above. Mac mini, numeric lock acquired and released, BLAS threads 1,
`nice`, memory free 65 percent at start, peak RSS 0.05 GB, run time 0.1 s.

| B | rho_4, pair along axis 1 | sigma_4, axis 1 | #{abs(hG) > 1/4}, axis 1 | hand bound m/3072 | control, pair along axis 4: rho_4 | pair along axis 2, offset in axis 3: rho_4 |
|---|---|---|---|---|---|---|
| 3 | 0.00511 | 0.323 | 28 | 0.00033 | 0.013889 | 0.00240 |
| 5 | 0.00958 | 0.542 | 48 | 0.00065 | 0.013889 | 0.00510 |
| 7 | 0.01390 | 0.750 | 72 | 0.00098 | 0.013889 | 0.00647 |
| 9 | 0.01813 | 0.954 | 96 | 0.00130 | 0.013889 | 0.00753 |
| 11 | 0.02233 | 1.156 | 120 | 0.00163 | 0.013889 | 0.00834 |
| 13 | 0.02651 | 1.356 | 144 | 0.00195 | 0.013889 | 0.00897 |

Criterion 1 (identities): PASS, every identity exact to the last bit (0.0):
Q_path H_0, dG, C_B G and hG - (H_0 - d hH_0). Criterion 2: **REFUTED**,
as the hand lemma says: rho_4 grows by a factor 5.2 from B = 3 to 13, with
log-log slope 1.03 over the last two points; the count of large bonds is
exactly 12(B - 1) = 24 m, twice the hand count (phi also exceeds 1/4 on the
other side of the bond). Registered control (pair along the last axis):
rho_4 = 2/144 exactly at every B, since Pi^0 in the offset axis annihilates
the antisymmetric pair, so hG = H_0. The extra column (not registered) rises
slowly toward 2/144: there one Pi^0 factor spreads the string over about 2B
sites, which costs B^-2 in the fourth power.

**What Lemma NC does to the queue's question Q2.**
1. *From energy alone, no.* Take the pair of endpoints U := the locked-pair
   field exp(a(delta_(b_+) - delta_(b_-))) and T := 1. Both are class with
   identity parents (`seam-nlpay` Section 4), and the path-gauge alignment
   h := -hG has gauge function hH_0, which vanishes at every top centre
   (x_2 = c_2 there), so it is an admissible (ALIGN) with q = 1. Its left side
   of (NL-pay) is at least 2 sum_p s_p^4 >= (9m/64) a^4, while the right side
   is at most C_rel(L) 12 (1 - cos a) <= 6 C_rel(L) a^2. So (NL-pay) fails for
   this alignment as soon as m > (128/3) C_rel(L) a^-2, and a is fixed before
   depth. U is not the minimizer for its parent (the identity is), so this
   refutes no statement about the specified U, T. It shows that any proof of
   (NL-pay) through the path-gauge alignment must use a property of the actual
   minimizer beyond class membership. That is the locked-pair lesson of
   `seam-nlpay`, now for this alignment.
2. *Given L^4 control of the endpoint curvatures, yes at the linearized level.*
   By the Schur test (||k||_(p->p) <= (max row sum)^(1-1/p) (max column sum)^(1/p)),
   with the row and column sums of Lemma 3.1 (f) of `seam-quadratic-c`:
   ||h^1D||_(4->4) <= (4B)^(3/4)(6B)^(1/4) < 4.43 B, ||Pi^0||_(4->4) < 1.86,
   ||Pi^1||_(4->4) < 2.72. Each output component of h on 2-forms has three
   terms, each a tensor of at most three Pi factors (at most one Pi^1) and one
   h^1D, so

       sum_b |hF(b)|^4 <= 4 (3 x 1.86^3 x 2.72 x 4.43)^4 B^4 sum_p |F(p)|^4
                       <= 1.2 x 10^10 B^4 sum_p |F(p)|^4,

   locally, with the range of Lemma 4.1 (d) there. In top units
   B^4 sum_(p in Q) |F(p)|^4 = ||F||_(L^4(Q))^4. So if both endpoint curvatures
   obey the top-scale L^4 bound of (R3) in `parts/hard-core--mapped.md` Text
   5.3, ||F||_(L^4(Q)) <= C_3 f(Q^+) with f(Q^+) the largest top flux near Q,
   the quartic term of (SEED) on Q is at most C f(Q^+)^4. Since a top plaquette
   of angle theta' forces fine energy at least about theta'^2 in its shadow
   (Lemma K (c) of `parts/hard-core--excess.md` with Cauchy-Schwarz; abelian
   linear form discharged, nonlinear form needs the composite estimates of
   Section 4), this is C f^2 times the local energy: relative size f^2.
3. *But the homotopy normalization cannot carry the nonlinear relative field.*
   The nonlinear relative field must be one exact field with T^g = exp(h) U.
   Imposing the homotopy normalization h(h) = 0 on it is a nonlinear gauge
   fixing whose iteration applies the 1D integration h to products of the
   field; with only L^4 data the products are not in a space that h maps
   back to L^4, for the same reason as Lemma NC (diagnostic, not a theorem).
   With pointwise data it would close, but pointwise regularity of the class
   minimizer is what the mapped attempt dropped: `library/relative-density-bound.md`
   item 2 finds, by a scaling count, a logarithm at nested block centres.
   So the relative field has to be taken in a critical gauge, and then the
   contour averages of Section 3 must be controlled separately.

## 3. What replaces (PATCH), and what the gauge of the relative field must control

**3.1 (PATCH) is not a necessary step (discharged).** The transition term
D_U v of (PATCH) appears only when the relative gauge is assembled from
independently chosen local gauges r_Q and then forced to agree on overlaps.
A construction that uses one relative field on the whole lattice,
U^g = exp(H/B) T bond by bond with one fine gauge g, has no overlap condition
and no transition term. The counterexample of `seam-nlpay` 3 (overlap gauges
+1 and -1 on two disjoint pieces) is about uncoordinated choices and has no
analogue for a single field. At the linear level the path-gauge primitive is
such a global formula, so **Q1 has the answer yes at the linear level**. At
the nonlinear level the homotopy formula does not by itself produce an exact
relative field (Section 2, item 3), so the transition term is removed by any
global relative field, not by the homotopy as such. The mapped attempt
already builds one: (R2) of `parts/hard-core--mapped.md` Text 5.3 solves for
the class lift as e^(i eta H) U^tr around a smooth trial, in one global gauge
(P_r D^* H = 0), by a fixed point with Sad#^-1 (implication from Theorem F,
not reviewed). What such a field must satisfy is (REL) of Section 4.

**3.2 Lemma GG (the linear seam in any parent-preserving gauge; discharged).**
Setting of `seam-quadratic-c` Section 5: Q_n A_* = Q_n A_t = v,
G := dA_t - dA_*, chi the cutoff of slope 2/r (top units), T_n := T_1 + d E
Phi_n T_1, so that Q_n T_n = I and d T_n = T_2 d'. Let H be **any** fine
1-form with dH = G and Q_n H = 0 (for instance A_t - A_* itself, or that plus
d lambda with lambda constant at the top centres). Put

    X_D := A_* + chi H - T_n Q_n(chi H).

Then (i) Q_n X_D = v; (ii) dX_D = (1 - chi) dA_* + chi dA_t + R with
R = [d, chi] H - T_2 d' Q_path(chi H); (iii) with A_2 the bonds within 3 top
units of the transition set Tr,

    sum_p |R(p)|^2 <= (155568 / r^2) B^-2 sum_(b in A_2) |H_b|^2.

*Proof.* (i) Q_n T_n = I. (ii) d(chi H) = chi G + [d, chi] H, and
d' Q_n(chi H) = d' Q_path(chi H) - d'd' Phi_n(chi H) = d' Q_path(chi H).
(iii) Write Q_path(chi H)(c) = P_1(c) + P_2(c), P_1(c) := Q_path((chi -
chi(c_*)) H)(c), P_2(c) := chi(c_*) Q_path H(c). The proof of Theorem 5.1 (iv)
of `seam-quadratic-c` gives sum_c |P_1(c)|^2 <= (4/r^2) B^-2 ||H|_(A_2)||^2 and
||[d,chi]H||^2 <= 24 ||H|_(A_1)||^2 / (r^2 B^2); it used Q_path H = 0 only to
remove P_2. Here Q_n H = 0 gives Q_path H = d' Psi with Psi := Phi_n H. On a
coarse plaquette P with boundary bonds c_1, ..., c_4, the signed sum of
d' Psi(c_i) vanishes, so

    d' P_2 (P) = sum_i +- (chi(c_i*) - chi(P_*)) Q_path H(c_i),

and |chi(c_i*) - chi(P_*)| <= 1/r (sup distance 1/2 top unit, slope 2/r). A
coarse bond lies in 6 coarse plaquettes, so ||d' P_2||^2 <= (24/r^2) sum_c
|Q_path H(c)|^2 <= (24/r^2) B^-2 ||H|_(A_2)||^2 by the Schur bound for
Q_path (row sums B, column sums B^-3). With ||d' P_1||^2 <= 24 sum |P_1|^2,
||d' Q_path(chi H)||^2 <= (2 x 96 + 2 x 24)/(r^2 B^2) ||H||^2 =
240 ||H||^2/(r^2 B^2); ||T_2||^2 <= 324; and |a + b|^2 <= 2|a|^2 + 2|b|^2. QED

So at the quadratic level the path gauge is one way, not the only way, to
get the seam: **any parent-preserving primitive with a local L^2 bound
works**, and the only property of the contours used is d'd' Phi_n = 0. In
top units the constant is (155568/r^2) ||H||_(L^2(A_2))^2, against 62256/r^2
in the path gauge.

**3.3 Lemma CT (contour averages enter the correction field; discharged).**
Same setting, Psi := Phi_n H, chi~(y) := chi(y) at top centres. For every top
bond c = (y, y'),

    Q_n(chi H)(c) = Q_path((chi - chi(c_*)) H)(c) - (d' zeta)(c) - beta_Psi(c),
    zeta(y) := Phi_n((chi - chi(y)) H)(y),
    beta_Psi(c) := (chi(y') - chi(c_*)) Psi(y') - (chi(y) - chi(c_*)) Psi(y).

*Proof.* Q_n = Q_path - d' Phi_n; Q_path(chi H)(c) = P_1(c) + chi(c_*) d'Psi(c);
Phi_n(chi H)(y) = zeta(y) + chi(y) Psi(y); and
chi(c_*) d'Psi(c) - d'(chi~ Psi)(c) = -beta_Psi(c). QED

*Reading.* zeta vanishes at every centre whose contours see a constant chi,
so d'zeta is the gradient of a top 0-form supported near Tr. beta_Psi is
supported near Tr and |beta_Psi(c)| <= (|Psi(y)| + |Psi(y')|)/r. Using
T_1 d' = d T_0,

    T_n Q_n(chi H) = T_1 P_1' - d T_0 zeta - T_1 beta_Psi + d E Phi_n T_1 Q_n(chi H),

P_1'(c) := Q_path((chi - chi(c_*))H)(c). The two gradient terms have gauge
functions supported near Tr, so at the nonlinear level they are exact gauge
transformations at no cost that leave the parent far from Tr alone. T_1 P_1'
is bounded by the L^4 norm of H (the tent kernel of Q_path has bounded L^(4/3)
norm). The remaining term T_1 beta_Psi has size about |Psi|/r in top units on
the transition, small curvature (its coarse curl is d'beta_Psi = -d'P_2, since
beta_Psi = d'(chi~ Psi) - P_2, and that reads only d'Psi = Q_path H, as in
Lemma GG), and it is not a gradient of a
function supported near Tr: along a coarse path gamma from a centre y_in at
the inner edge of the transition to a centre outside it,

    sum_(c in gamma) beta_Psi(c) = -Psi(y_in) - sum_(c in gamma) chi(c_*) Q_path H(c),

and the last sum has O(r) nonzero terms (chi(c_*) > 0 only across the
transition, of width r/2), each bounded by the L^4 norm of H.
So any split of T_1 beta_Psi into such a gradient plus a rest leaves a rest
whose line integrals across the transition are at least |Psi(y_in)| minus
critically controlled terms.

*Consequence at the nonlinear level.* A gradient of size |Psi|/r is free
when it is an exact gauge transformation. Here it cannot be one, because its
gauge function would have to equal -Psi(y_in) on the inner side, where that
changes the parent of T. Exponentiated as a field it is a modulated near-gauge
of size |Psi|/r, whose quartic cost in (SEED) is of order (|Psi|/r)^4 per top
cell (the commutator example (GRAD) of `seam-nonlinear` 3 is exactly this
kind of term). **So the nonlinear seam needs |Psi(y)| = |Phi_n H(y)| bounded
by the local data at every top centre y, uniformly in depth.** Two remarks:
(a) Psi can be moved by a gauge d lambda with lambda constant at the centres,
Psi -> Psi + Av_B lambda - const; making Psi constant puts H in the path
gauge, and then the cost moves into the L^2 and L^4 norms of d lambda, which
are again of size |Psi| (up to a capacity factor at the centres, remark only).
(b) Psi is a contour average, an integral of H over lines through the top
centre y, which is a centre at every level. It is not controlled by L^4
norms: H equal to s B^(-1/4) on the m bonds of the first contour segment from
y has sum_b |H_b|^4 = m s^4 B^-1 <= s^4 and Phi_n H(y) of order s B^(3/4)
(the first segment carries a fixed fraction of the contours), for the
one-step map. A W^(1,4) bound on H at the top scale controls such line
integrals; L^4 alone does not.

**3.4 Where this leaves Q2 and Q3.** The nonlinear relative field must be
(i) critical, L^4 at the top scale, for the fourth moment of (SEED)
(Section 2); (ii) L^2 at the top scale with an absolute constant, for the
second moment and for Lemma GG, since that constant sets r and hence the rate;
(iii) contour-controlled at the top centres, for the term T_1 beta_Psi. The
homotopy primitive has (ii) and (iii) at the linear level (path gauge) but
not (i) (Lemma NC). A Landau-type global gauge has (i) and (ii) but (iii) is
a line-integral statement beyond L^4.

## 4. Nonlinear (GLUE-E) at the flat background, from one relative-regularity input

**4.1 The input (REL) (gap; the first step of this route not carried).**
Top units throughout; Q ranges over closed top cubes of side 1; for a top
cube Q', E(Q') := E_U(Q') + E_T(Q') is the sum of squared fine plaquette
angles of U and of T based in Q'; K_delta(Q, Q') := c_delta exp(-delta d(Q, Q'))
with sum_(Q') K_delta(Q, Q') = 1. (REL) asks for a fine gauge g with g = 1 at
every top centre and a fine su(2)-valued 1-form H, in top normalization, with

    (REL-g)  U^g_b = exp(H_b / B) T_b  for every fine bond b,
    (REL-2)  ||H||_(L^2(Q)) <= C_2 (K_delta * E)(Q)^(1/2),   C_2 and delta absolute,
    (REL-4)  ||H||_(L^4(Q)) <= C_4 (K_delta * E)(Q)^(1/2),   C_4 = C_4(L),
    (REL-Phi) |Phi_n^(T) H(y)| <= C_Phi (K_delta * E)(Q_y)^(1/2) at every top centre y,
             C_Phi = C_Phi(L), Q_y the top cube centred at y,
    (REL-E)  E(Q) <= C_E f^2 for every Q,

all uniform in depth and volume. Phi_n^(T) is the composite contour average
of the linearized block map at the background T (mapped Text 3.1 read at T).

*What is supplied, and by what.* (REL-E) for T is discharged: (TOP-tr)
gives fine flux at most C_7 B^-2 f, so E_T(Q) <= 6 (B + 1)^4 C_7^2 B^-4 f^2.
(REL-E) for U is (R2) of mapped Text 5.3, ||F(U)||_(L^2(c)) <= C a
(implication from Theorem F, not reviewed). (REL-g), (REL-2) and (REL-4)
are what (R2) and (R3) of Text 5.3 claim for the class lift relative to the
one-shot trial U^tr, in one global gauge, with exponential decay of the
response at rate delta_*: here they are needed relative to the iterated trial
T, which needs Sad#(T) invertible with exponential decay (Theorem F at T),
the identification of the fixed point with the class minimizer (item (o) of
`library/relative-density-bound.md`, a sketch), and the conversion of a
response bound in the top flux into one in the local energy (a top plaquette
of angle theta' forces fine energy about theta'^2 in its shadow: abelian
linear case by Lemma K (c) and Cauchy-Schwarz; nonlinear case needs (CMP)).
**(REL-Phi) is not supplied by any statement I found.** It is a line-integral
bound at top centres (Lemma CT, remark (b)). The H^2 bound of (R3), proved
there in local Landau gauges on boxes, would give it after a comparison of
the local gauges with the global one; that comparison is not written.

*Why (REL) is strictly smaller than (GLUE-E).* It concerns the pair (U, T)
alone: no set D, no cutoff, no competitor, no parent correction, no class
check. It is a regularity statement for the class minimizer relative to the
trial.

*Respecting the locked pair.* (REL-E) is false for frozen data: (LOCK) of
`seam-nlpay` packs floor(B/(4 t_0))^3 locked pairs in one top cube, so E grows
with depth. In the construction below (REL-E) is used exactly once, to turn
the quartic term into C f^2 times the energy; for the unfrozen minimizer it
comes from (R2), not from class membership.

**4.2 Composite inputs (CMP) (unchecked inputs).** The conclusions of Lemma
AN1 of `library/analytic-lift.md` at the background U_0 := T, for the
contour-free composite N^(n) of `library/block-poincare-energy-package.md`
Theorem 7 Step 1 with base chain the chain of T, together with the background
residual of the contour part from its proof: for fine K with
sup_Q ||K||_(L^4(Q)) <= rho(L) and e_j(b) := ||K||_(L^4(b^+)) at every level j,

    |log N^(j)(e^(K/B) T)(b) - log N^(j)(T)(b) - Q^(o,(j)) K(b)| <= C_2(L) e_j(b)^2,
    |Q^(o,(j)) K(b)| <= C_1 e_j(b),   C_1 absolute,

and Q^(T)_n = Q_path^(T) - d' Phi_n^(T) + (residual at most C(L) f e_n), with
Q_path^(T) the path average with transports of T. AN1's hypotheses (i), (ii)
hold at T: flux at most C_7 L^(-2m) f at every level (TOP-tr), and pointwise
fine curvature at most C_7 B^-2 f, so ||F(T)||_(L^4(box)) <= C f. AN1 is an
own derivation of the mapped push, not reviewed; I did not re-derive it. Also
read as part of (CMP): the exact-fibre Picard step of `parts/hard-core--excess.md`
2.2 (finite-range derivative, Neumann series), run at depth n with the
tensor right inverse T_n in the frames of T, with depth-uniform constants.

**4.3 Theorem GN (implication: (REL) + (CMP) give (GLUE-E) at the flat
background).** For every odd L >= L_0, there is T_2(L) > 0 such that for
flux(V) <= f <= T_2(L), every depth n, volume and set D of fine sites, and
every r >= 1, there is a field X_D with
(i) M_n(X_D) = V exactly;
(ii) every intermediate image M_j(X_D), 0 <= j < n, of flux at most
     C(L) f <= T_class, hence class at every level;
(iii) R_D <= A_s sum_p (K * 1_(S_(r + R_0)(D)))(p) [a_U(p) + a_T(p)], with

    A_s = (1 + C_seam^(1/2))^2,   C_seam = 311328 C_2^2 / r^2 + C(L) f^2,

R_0 an absolute enlargement (correction range plus R_M <= 2, the reach of the
composite map, plus 5), and K a probability kernel, the transpose of K_delta
smeared by the exponential tail of the Picard correction, whose rate tends to
infinity as f -> 0.
Choosing r := 1116 C_2 (so that the linear part of C_seam is at most 1/4)
and then f small after L gives A_s <= 2.56. Then, for every nu <= delta/2,
M_* := sum_z K(z) exp(nu d(z, 0)) <= C_M(delta, R_0), and

    (RATE-exact) 2 A_s M_* sinh(nu r_E) < 1, r_E := r + R_0, holds for
    nu < nu_0 := min(delta/2, arcsinh(1/(6 C_M)) / r_E),

**with nu_0 absolute provided C_2 and delta are absolute.** Every L-dependent
constant (C_4, C_Phi, C_2(L) of (CMP), the Picard and residual constants)
enters only through C(L) f^2 or C(L) f, which T_2(L) absorbs.

**4.4 Proof, at the level of each term.**

*Step 1 (gauge; discharged).* Replace U by U^g of (REL-g). Since g = 1 at
the top centres, M_n(U^g) = V; each intermediate image is a gauge transform
of that of U, so class; plaquette actions are unchanged, so R_D is unchanged.
Write U for U^g, so U_b = exp(H_b/B) T_b.

*Step 2 (seed and its action; discharged).* Y_b := exp((1 - chi_b) H_b / B) T_b.
Then Y_b = T_b where chi_b = 1 and Y_b = U_b where chi_b = 0. The matrix
remainder of `seam-nonlinear` 2, with relative increments of size |H_b|/B and
|chi_j - chi_p| <= 2/(rB) on the four bonds of p, gives
P_Y = chi_p P_T + (1 - chi_p) P_U + E_p, |E_p|_F <= (2/(rB)) s_p + s_p^2,
s_p := B^-1 sum_(b in boundary p) |H_b|. With |v + e|^2 <= (1 + eps)|v|^2 +
(1 + 1/eps)|e|^2 and convexity of the squared norm,

    a_Y(p) <= (1 + eps)[chi_p a_T(p) + (1 - chi_p) a_U(p)]
              + (1 + 1/eps)[(4/(r^2 B^2)) s_p^2 + s_p^4],

with equality a_Y = chi_p a_T + (1 - chi_p) a_U when chi is constant on the
four bonds. Counting four bonds per plaquette and six plaquettes per bond,
sum_p (4/(r^2 B^2)) s_p^2 <= (96/r^2) ||H||_(L^2)^2 and
sum_p s_p^4 <= 384 ||H||_(L^4)^4, both over the bonds where chi varies.

*Step 3 (defect of the seed; implication from (CMP)).* delta(c) :=
log(M_n(Y)(c) V(c)^-1) vanishes unless the composite support of c, within
R_M <= 2 top units of c, meets bonds with 0 < chi_b < 1 or meets both
chi_b = 0 and chi_b = 1 (locality of M_n: M_n(Y)(c) reads only those
bonds; discharged). By (CMP) with K = (1 - chi) H, and the exact relation
log(M_n(U) V^-1) = 0 (U has parent V), the computation of Lemma CT at the
background T gives

    delta(c) = -Q_path^(T)((chi - chi(c_*)) H)(c) + (d' zeta)(c) + beta_Psi(c) + rho(c),
    |rho(c)| <= C(L) [e_n(c)^2 + f e_n(c)],   Psi := Phi_n^(T) H,

with zeta supported near Tr. The first term is at most (C/r) e_n(c) (tent
kernel, slope 2/r over the support), beta_Psi at most (|Psi(y)| + |Psi(y')|)/r.

*Step 4 (exact parent; implication from (CMP)).* The gradient d'zeta, and the
contour part produced by each correction, are removed by an exact gauge
transformation omega with omega = 1 off the top centres near Tr (free:
actions are invariant, and the parent far from Tr is untouched). The rest is
removed by Z, solving M_n(omega e^(Z/B) Y) = V by the Picard iteration of
(CMP): linearized map (Z, psi) -> Q_n^(Y) Z + d'_V psi, approximate inverse
alpha -> (T_1 alpha, -Phi_n^(T) T_1 alpha) in the frames of T (the nonlinear
form of T_n = T_1 + d E Phi_n T_1), contraction factor
q <= C(L)(f + sup_Q ||H||_(L^4(Q))) <= C(L)(1 + C_4 C_E^(1/2)) f <= 1/2 for f
small after L. The fixed point gives (i). Z has exponential tails at rate
log(1/q)/R_1 in top units, R_1 absolute.

*Step 5 (size and curvature of Z; implication).* By Steps 3 and 4,
||Z||_(L^4(Q)) <= C sum_c K_q(Q, c)[e_n(c)/r + |Psi(y_c)|/r + C(L)(e_n(c)^2 + f e_n(c))],
and by Lemma GG read at the background T (the transports of T change the
constant 240 by a factor 1 + C(L) f),

    ||dZ||_(L^2)^2 <= (1 + C(L) f) 324 x 240 r^-2 ||H||_(L^2)^2 + C(L)(f^2 + sup_Q ||H||_(L^4(Q))^2) ||H||_(L^4)^2,

over the region near Tr, with the K_q tail. Psi does not enter dZ (Lemma CT:
the coarse curl of beta_Psi reads only Q_path H); it enters Z itself.

*Step 6 (cost of the correction; implication).* omega is a gauge
transformation, so a_X = a_(e^(Z/B) Y). On each plaquette
P_X = (prod_j exp(gamma_j)) P_Y with gamma_j the transported increments of
Z/B, and |prod exp(gamma_j) - I - sum gamma_j| <= s_p(Z)^2/2 as in Step 2; the
sum of the gamma_j is the covariant curl of Z/B at Y, which differs from
B^-2 dZ(p) by C(L) f |Z|/B (transports of Y in the frames of T). So, with a
distance-dependent eps'(p) := eps_0 q^(d(p, Tr)/2) to handle the tail,

    a_X(p) <= (1 + eps'(p)) a_Y(p) + (1 + 1/eps'(p)) C [B^-4 |dZ(p)|^2 + s_p(Z)^4 + C(L)^2 f^2 |Z_b|^2 B^-2],

and the eps'(p) a_Y(p) terms far from Tr are charged to the exponential
profile, which is part of K.

*Step 7 (class at every level; implication from (CMP)).* By (CMP) at each
level j, with K = H + Z and (REL-4), (REL-Phi), (REL-E) and Step 5,
flux(M_j(X)) <= flux(M_j(T)) + C(L) sup_Q ||H + Z||_(L^4(Q)) + C_2(L)(...)^2
<= C_7 f + C(L)(C_4 + C_Phi) C_E^(1/2) f, and at the fine level a single link
value obeys |H_b + Z_b|/B <= ||H + Z||_(L^4(Q)). So every level has flux at
most C(L) f <= T_class for f <= T_2(L). This needs no smallness of fine energy
on top cubes beyond (REL-E).

*Step 8 (assembly; discharged given Steps 2 to 7).* As in Theorem 6.1 of
`seam-quadratic-c`: write R_D = sum_p [a_X(p) - 1_D(p) a_T(p) - (1 - 1_D(p)) a_U(p)].
Since chi_p = 1_D(p) off S_r(D),

    R_D <= sum_p [eps(p) + 1_(S_r(D))(p)] (a_T + a_U)(p) + sum_p (1 + 1/eps(p)) ERR_p,

where ERR_p collects the seed terms of Step 2 and the correction terms of
Step 6. By (REL-2), (REL-4), (REL-Phi), (REL-E) and Steps 2, 5 and 6,
sum_p ERR_p <= [311328 C_2^2/r^2 + C(L) f^2] sum_p (K * 1_(S_(r+R_0)(D)))(p) E(p),
where 311328 = 2 x (96 + 155568) and the quartic terms are
384 C_4^4 (K_delta * E)^2 <= 384 C_4^4 C_E f^2 (K_delta * E), likewise
C_Phi^4 r^-4 (K_delta * E)^2 for the beta_Psi part of Z. The squared angles
E and the actions a differ by fixed factors at these fluxes ((ANGLE) of
`seam-nlpay`: 2 t^2/pi^2 <= 1 - cos t <= t^2/2). Optimizing a constant
eps_0 gives A_s = (1 + C_seam^(1/2))^2, as in `seam-quadratic-c` 6.1; the
coefficient 1 in front of 1_(S_r(D)) is the structural term recorded there.
The rate statement is the arithmetic of `seam-quadratic-c` 6.2 with the
constants above. QED, as an implication.

**4.5 Q3: which nonlinear errors are C(L) x flux, depth-uniformly.**

| Term | Size relative to the shell energy | Depth uniformity comes from |
|---|---|---|
| quartic seed term s_p^4 | 384 C_4^4 C_E f^2 | (REL-4), (REL-E) |
| second-moment seed term | 96 C_2^2 / r^2, absolute | (REL-2) with C_2 absolute |
| linear correction curvature | 77760 C_2^2 / r^2 (1 + C(L) f) | Lemma GG at the background T |
| contour-average part of Z | C_Phi^4 r^-4 C_E f^2 | (REL-Phi) |
| nonlinear parent remainder rho | C(L) (C_4^2 C_E + 1) f^2 | (CMP): L^-2 per level of the critical norm |
| transports of T, Y in the correction | C(L) f | pointwise smoothness of T |
| Picard tail | absorbed in K, rate log(1/q)/R_1 | q <= C(L) f |
| class margin | C(L) f <= T_class | (CMP) at each level |

So **Q3 has the answer yes, given (REL) and (CMP)**: every L-dependent
constant multiplies f or f^2, and T_2(L) chosen after L absorbs it; A_s, r,
R_0, M_* and nu_0 come from the linear part only and are absolute when C_2 and
delta are. If C_2 depended on L, r would have to grow with it, and
(RATE-exact) at a rate fixed before L would fail for this construction:
that is the one place where an L-dependence would be fatal.
