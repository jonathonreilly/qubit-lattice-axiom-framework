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
