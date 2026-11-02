lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T19:25Z

# seam-quadratic-c: quadratic (LC) at the flat background, blind rerun

Queue item 33, mapped side. Pinned at commit ba5277f05. Author: Anthropic
claude-opus-5-5, effort max, Mac mini worker, 2026-11-02. Same-model work:
not independent in model, not a gate, not an audit, no status.

**Firewall.** `library/seam-quadratic.md` was not opened (no grep touched it;
every search ran on an allow-list that excludes it and the mapped-side
exclusions of FINISH.md). Read: FINISH.md, GOAL.md,
`library/excess-seam.md` (whole), `library/excess-shell-end.md` Sections 1 to
4.2, `parts/hard-core--mapped.md` Text 1 and 3.1 to 3.2 (the block operator,
Lemma 3.1), `parts/hard-core--excess.md` 1.1 (Lemma K) and 2.1 (the tensor
right inverse), `library/excess-localized-competitor-stop.md` Sections 1 and 2.

Status while writing: in progress; sections are appended in order.

## 1. The statement tested, and criteria fixed before any computation

**Setting (from the sources).** Trivial background, linearized fields. Fine
lattice of unit spacing; L odd >= 3; depth n >= 1; B := L^n, the top block
side; top units are B fine units. The one-step map is the linearization Q of
Balaban's average as in mapped Text 3.1,

    Q theta(c) = avg_{x in B(y)} [ theta(Gamma_{y,x}) + theta([x,x+L e_mu])
                                    - theta(Gamma_{y',x+L e_mu}) ],

with contours Gamma (or an average over contour orders) whose family at y' is
the translate of the family at y. Q_n is the n-fold composite. A_* minimizes
||dA||^2 on {Q_n A = v}; A_t is any field with Q_n A_t = v. The energy of a
fine field is sum over fine plaquettes of |dA(p)|^2, the quadratic part of
the normalized Wilson action. D is any set of fine plaquette anchors (in
particular a superlevel set of a weight), distances are sup-norm distances
in top units, D^{+r} = {d(., D) <= r}, D^{-r} = {z : d(z', z) <= r implies
z' in D}, S_r(D) = D^{+r} minus D^{-r}.

**Statements to deliver** (excess-shell-end 4.2 and Section 3,
excess-seam Section 2):

    sum_p |R(p)|^2 <= C_seam sum_p (K*1_{S_r(D)})(p) [|dA_*(p)|^2+|dA_t(p)|^2]   (LC)
    A_*(D) - A_t(D) <= A_s [A_*(K*1_{S_r(D)}) + A_t(K*1_{S_r(D)})]               (E-SHELL)
    beta_* = 2 A_s M_* sinh(nu r) < 1,   M_* = sum_z K(z) exp(nu d(z,0))         (RATE-exact)

where R is the curvature defect of an admissible competitor X_D,
Q_n X_D = v, with dX_D = (1 - chi) dA_* + chi dA_t + R.

**Registered criteria for the kill test (written before any run).**
1. Identities. Every exact identity used by the hand proof (chain maps,
   right inverses, the homotopy, the vanishing of the path average on the
   chosen primitive, the exact parent and the curvature of the glued field,
   and the reduction of the composite contour map) must hold to relative
   error below 1e-10 in double precision. Any failure above 1e-8 means the
   written proof has an error and stops this item there.
2. Depth and L. At fixed top-unit geometry (slab D, cutoff Lipschitz 1/r in
   top units), the measured ratio rho(B) = sum|R|^2 / sum_{enlarged shell}|G|^2,
   G = dA_t - dA_*, worst over the test family (transverse modes crossing a
   block face, white noise, smooth noise, and a power-iteration search), is
   recorded for B = 3, 5, 7, 9, 11, 13 at least. KILL if rho grows by more
   than a factor 1.5 from B = 5 to the largest B with log-log slope above 0.3
   over the last two points. SURVIVE otherwise. Also record that rho stays
   below the hand bound of Section 5.
3. What a run can and cannot show. A bounded ratio on a finite family proves
   nothing; only the written argument of Sections 2 to 6 is offered as a
   proof. A violated identity or a growing ratio would refute.

## 2. Reduction: contours and depth drop out exactly (discharged, hand proofs)

Notation on one lattice of unit spacing, one step of side b (odd), block
B_b(y) = y + {-(b-1)/2, ..., (b-1)/2}^4, theta([x, x+b e_mu]) the sum of theta
over the b bonds of that segment:

    Q_path^(b) theta(y, mu) := b^-4 sum_{x in B_b(y)} theta([x, x + b e_mu]),
    Av_b lambda(y) := b^-4 sum_{x in B_b(y)} lambda(x),   r = restriction to centres.

**Lemma 2.1 (path parts compose).** For L odd, applying the level-(k+1) path
average (side L in level-k units) to the level-k field Q_path^(L^k) theta
gives Q_path^(L^(k+1)) theta. Hence the path part of the composite is the
one-step path average of side B = L^n.

*Proof.* The level-k bonds of the segment from x_k to x_k + L^(k+1) e_mu are
the L translates x_k + j L^k e_mu, j < L. Each carries the average over
x in B_(L^k)(x_k + j L^k e_mu) = B_(L^k)(x_k) + j L^k e_mu of the fine segment
of L^k bonds; pairing x with x + j L^k e_mu and summing over j concatenates
them into the fine segment [x, x + L^(k+1) e_mu]. Averaging over x_k in
B_(L^(k+1))(y) (level-k sites) of the average over x in B_(L^k)(x_k) is the
average over x in B_(L^(k+1))(y), because these L^4 blocks tile it: in each
axis, y + L^k a + [-(L^k-1)/2, (L^k-1)/2], |a| <= (L-1)/2, are disjoint, consecutive
and end at y +- (L^(k+1)-1)/2. QED

**Lemma 2.2 (contours are a coarse gradient at every depth).** Assume the
contour family of block y + b e_mu is the translate of that of y.
(a) Q d = d' r: the contour, the segment and the reversed shifted contour
telescope to lambda(y') - lambda(y).
(b) Q = Q_path^(L) - d' Phi with Phi theta(y) = avg_{x in B(y)} theta(Gamma_{y,x})
(mapped Lemma 3.1, read with x' = x + L e_mu and translation covariance).
(c) Q_path^(b) d = d' Av_b: the average of lambda(x + b e_mu) - lambda(x) over
x in B_b(y) is Av_b lambda(y + b e_mu) - Av_b lambda(y).
(d) Q_n = Q_path^(B) - d' Phi_n with Phi_1 = Phi and
Phi_(k+1) = Av_L Phi_k + Phi^(k+1) Q_k; and Q_n d = d' r_n.

*Proof of (d).* Q_(k+1) = (Q_path^(k+1) - d' Phi^(k+1))(Q_path^(L^k) - d Phi_k).
By Lemma 2.1 the first product is Q_path^(L^(k+1)); by (c) the cross term is
Q_path^(k+1) d Phi_k = d' Av_L Phi_k. Block centres nest for odd L, so (a)
iterates to Q_n d = d' r_n. QED

**Corollary 2.3 (curvature form of the constraint).** d' Q_n = d' Q_path^(B)
= C_B d, where C_B is the tensor map of Section 3 on 2-forms (R^1 in the two
plaquette axes, R^0 in the other two). C_B is the tent average B^2 <.>_chi of
`parts/hard-core--excess.md` Lemma K with L replaced by B. *Proof:* d'd' = 0
removes the contour term; the rest is the 1D identity R^1 d = d' R^0
(Lemma 3.1(a) below) tensored over the four axes. QED

**Proposition 2.4 (the quadratic seam problem depends on L and n only through
B).** Put Zset := {Z fine 1-form : Q_path^(B) Z = 0}, and let E be any map of
top 0-forms to fine 0-forms with r_n E = identity (for example: the value at
each top centre, zero elsewhere).
(i) For Z in Zset, X := A_* + Z + d E Phi_n(Z) has Q_n X = v and dX = dA_* + dZ.
(ii) Conversely, if Q_n X = v there is Z in Zset with dZ = d(X - A_*).
So {dX : Q_n X = v} = dA_* + d Zset. The minimizer's curvature, every trial
curvature, every competitor curvature, and hence every quantity in (LC),
(E-SHELL) and (RATE-exact), are those of the one-step problem of side B.

*Proof.* (i) Q_n X = v + Q_path Z - d'Phi_n Z + d' r_n E Phi_n Z = v by 2.2(d);
dd = 0. (ii) W := X - A_* has Q_n W = 0, so Q_path W = d'Phi_n W. Take
lambda := T_0 Phi_n W with the 4D tensor right inverse T_0 of Av_B
(Section 3), so Av_B lambda = Phi_n W; by 2.2(c) Z := W - d lambda is in Zset,
and dZ = dW. QED

*Consequence for the item's worries.* The nested contours, the parent-fixed
point-anchored gauge (the source of the eta^-2 loss in
`library/excess-localized-competitor-stop.md` Section 5) and the first-order
contour part of [Q_n, chi] never enter a curvature: contour mismatches are
removed by pure gauges d E Phi_n(.), whose size is irrelevant. Checked
numerically for the actual nested map at L = 3, n = 2 with axial-staircase
contours (Section 7): d'Q_2 = C_9 d and Q_2 d = d' r_2 to 2e-15.

## 3. One-dimensional chain maps, right inverse and homotopy (discharged)

The right inverse is the one of `parts/hard-core--excess.md` 2.1 in spirit
(hat interpolation plus a block correction), with the hat in place of the
cubic B-spline so that every kernel is explicit; side B in place of L.

**Definitions.** B = 2m+1 >= 3. Work on Z (the torus case follows: every map
is covariant under B Z and the periodized kernels obey the same Schur bounds).
Coarse sites y in B Z, I(y) = [y-m, y+m]; fine bond x = (x, x+1); coarse bond
c = (y_0, y_0+B); Delta f(t) = f(t+1) - f(t).

    R^0 phi(y)  = B^-1 sum_{x in I(y)} phi(x)
    R^1 a(y_0)  = B^-1 sum_{x in I(y_0)} sum_{s=0}^{B-1} a(x+s) = B^-1 sum_t tau(t-y_0) a(t)
    tau(t) = #{a in [-m,m] : a <= t <= a+B-1}   (tent; sum tau = B^2, sum_{y_0} tau(t-y_0) = B)
    Lambda(t) = max(0, 1-|t|/B),  beta(t) = c_B max(0, 1-|t|/(m+1)),  c_B = B/(m+1),
    g_1 = m(m+1)/(2B^2) < 1/8
    zeta_y = Lambda(.-y) + g_1 [2 beta(.-y) - beta(.-y-B) - beta(.-y+B)],   T^0 psi = sum_y psi(y) zeta_y
    eta_c  = B^-1 1_[y_0, y_0+B) + g_1 [Delta beta(.-y_0-B) - Delta beta(.-y_0)],   T^1 alpha = sum_c alpha(c) eta_c
    h a(x) = sum_y zeta_y(x) B^-1 sum_{x'' in I(y)} sigma(x'',x;a),
    sigma(x'',x;a) = sum_{x''<=x'<x} a(x') - sum_{x<=x'<x''} a(x')   (= phi(x) - phi(x'') if d phi = a)

**Lemma 3.1.** (a) R^1 d = d' R^0. (b) R^0 T^0 = I; sum_y zeta_y = 1 and
sum_y y zeta_y(x) = x. (c) d T^0 = T^1 d' and R^1 T^1 = I, also on a circle.
(d) h d = I - T^0 R^0 on 0-forms, d h = I - T^1 R^1 on 1-forms, R^0 h = 0.
(e) zeta_y vanishes for |x-y| > B+m; eta_c vanishes off [y_0-m-1, y_0+B+m];
(ha)(x) reads a only on |x'-x| < 2B. So Pi^0 := T^0 R^0, Pi^1 := T^1 R^1 and h
have range below 2B fine units, that is below 2 top units.
(f) Norms on l^2: ||R^0||^2 <= 1/B, ||R^1||^2 <= B, ||T^0||^2 <= 3B,
||T^1||^2 <= 6/B, ||Pi^0||^2 <= 3, ||Pi^1||^2 <= 6, ||h||^2 <= 24 B^2.

*Proof.* (a) R^1(d phi)(y_0) = B^-1 sum_{x in I(y_0)} [phi(x+B) - phi(x)]
= R^0 phi(y_0+B) - R^0 phi(y_0).
(b) B^-1 sum_{|x|<=m} (1-|x|/B) = 1 - m(m+1)/B^2 = 1 - 2 g_1 (by
sum_{x=1}^m x = m(m+1)/2); B^-1 sum_{|x|<=m} Lambda(x-B) = B^-1 sum_{x=1}^m x/B = g_1;
Lambda(.-y) vanishes on I(y') for |y'-y| >= 2B. beta is supported in I(0) and
B^-1 sum beta = (c_B/B)(B-m) = 1. Hence R^0 zeta_y(y') = (1-2g_1) delta_{y'y}
+ g_1 delta_{|y'-y|=B} + g_1(2 delta_{y'y} - delta_{y',y+B} - delta_{y',y-B}) = delta_{y'y}.
The hats reproduce constants and affine functions; the bracket has
sum_y [2 beta(x-y) - beta(x-y-B) - beta(x-y+B)] = 0 and the same with weight y,
by shifting the summation index.
(c) sum_{y >= y_0+B} Lambda(x-y) is the ramp 0 (x <= y_0), (x-y_0)/B, 1
(x >= y_0+B), with difference B^-1 1_[y_0,y_0+B); the bracket telescopes to
beta(.-y_0-B) - beta(.-y_0). So eta_c = Delta(sum_{y>=y_0+B} zeta_y)
= -Delta(sum_{y<=y_0} zeta_y), compactly supported, and summation by parts gives
sum_c eta_c (d'psi)(c) = sum_y psi(y) Delta zeta_y = d(T^0 psi). Then
R^1 T^1 d'psi = R^1 d T^0 psi = d' R^0 T^0 psi = d'psi. On a circle the coarse
1-forms are d'psi plus constants, and T^1 1 = T^1 d'(y/B) = d T^0(y/B)
= d(x/B) = 1/B on the cover by affine reproduction, with R^1(1/B) = 1.
(d) On the cover pick phi with d phi = a. Then ha = sum_y zeta_y (phi - R^0 phi(y))
= phi - T^0 R^0 phi by (b), independent of the choice of phi and periodic when
a is. So h(d phi) = (I - T^0 R^0) phi; d(ha) = a - T^1 d' R^0 phi
= a - T^1 R^1 d phi = a - T^1 R^1 a by (c) and (a); R^0 h a = R^0 phi - R^0 T^0 R^0 phi = 0.
(e) Read off the definitions; for h, x'' in I(y) and |x-y| <= B+m give
|x''-x| <= B+2m < 2B.
(f) Schur: ||k||^2 <= (sup row sum)(sup column sum) of |k|. R^0: 1 and 1/B.
R^1: B and 1. T^0: sum_y |zeta_y(x)| <= 1 + 4 g_1 c_B < 2 (one block contains x),
sum_x |zeta_y(x)| <= B(1 + 4 g_1) < 3B/2. T^1: |Delta beta| <= c_B/(m+1) < 4/B and
x, x+1 lie in at most two blocks, so sum_c |eta_c(x)| <= 1/B + 2 g_1 (2)(4/B) < 3/B;
sum_x |eta_c(x)| <= 1 + 2 g_1 (2 c_B) < 2 (total variation of beta is 2 c_B).
h: |w_y(x,x')| <= 1 for the weight of a(x') in the y-term; row sums
<= (sum_y |zeta_y(x)|) max_{x''} |x-x''| < 2 (2B); a column x' meets at most
four y (|x'-y| < 2B), each with sum_x |zeta_y(x)| < 3B/2, so columns < 6B. QED

Measured norms (guidance only, B = 3 to 41): ||T^0||^2/B in [1.21, 1.29],
B ||T^1||^2 in [2.6, 3.64], ||Pi^0|| in [1.10, 1.14], ||Pi^1|| in [1.11, 1.24],
||h||/B = 0.31. The Schur constants above are crude by factors 2 to 16.

## 4. Four-dimensional tensor homotopy and the primitive in the path gauge (discharged)

Write a fine k-form as components F_S, S a k-subset of the axes {1,2,3,4},
each a tensor of one-dimensional 1-forms on the axes in S and 0-forms on the
others. The lattice exterior derivative is d = sum_i sigma_i(S) d_i with
sigma_i(S) = (-1)^#{j in S : j < i} (Koszul sign), for instance
(dH)_{mu nu} = d_mu H_nu - d_nu H_mu. Let R = (x)_i R_i (R^1 on the axes in S,
R^0 elsewhere), T = (x)_i T_i likewise, Pi = T R, and for each axis i

    Hhat_i := sigma_i(S) [Pi_1 (x) ... (x) Pi_(i-1) (x) h_i (x) I (x) ... (x) I],   h := sum_i Hhat_i,

with h_i acting on axis i (zero on a degree-0 slot) and Pi_j = Pi^1 or Pi^0
by the degree of slot j.

**Lemma 4.1.** (a) R and T are chain maps (R d = d' R, d T = T d') and R T = I.
On 1-forms R = Q_path^(B); on 2-forms R = C_B.
(b) d h + h d = I - Pi.
(c) R h = 0.
(d) (hF)(z) reads F only within sup-distance below 2 top units of z. On
2-forms ||hF||^2 <= c_H B^2 ||F||^2 with

    c_H := 24 sum_{mu<nu} (3^((mu-1)/2) + 6^(1/2) 3^((nu-2)/2))^2 <= 8023,

and on coarse 2-forms ||T beta||^2 <= 324 ||beta||^2.

*Proof.* (a) Tensor products of Lemma 3.1 (a) to (c); the Koszul signs are the
same on both sides because R_i, T_i preserve degrees. (b) Fix i and an axis j.
If j > i, slot j of Hhat_i is I, which commutes with d_j, and Hhat_i lowers the
degree of slot i < j, which flips sigma_j: the two terms of d_j Hhat_i + Hhat_i d_j
cancel. If j < i, slot j is Pi_j, a chain map by Lemma 3.1 (c) and (a), and d_j
raises the degree of slot j < i, which flips sigma_i: they cancel again. For
j = i both signs are sigma_i(S) (they read only the slots before i), so the
pair gives Pi_(<i) (x) (d_i h_i + h_i d_i) (x) I_(>i) = Pi_(<i) (x) (I - Pi_i) (x) I_(>i)
by Lemma 3.1 (d). The sum over i telescopes to I - Pi_1 (x) ... (x) Pi_4 = I - Pi.
(c) Slot i leaves Hhat_i at degree 0, where R applies R^0, and R^0 h_i = 0.
(d) Ranges from Lemma 3.1 (e). On the component S = (mu, nu), Hhat_mu has norm
at most ||Pi^0||^(mu-1) ||h|| and Hhat_nu at most ||Pi^0||^(nu-2) ||Pi^1|| ||h||;
Cauchy-Schwarz over the six components and Lemma 3.1 (f) give c_H. The tensor
T on a 2-form component is T^1 (x) T^1 (x) T^0 (x) T^0, of norm squared at most
(6/B)^2 (3B)^2 = 324. QED

**Corollary 4.2 (primitive in the path gauge).** Let G be a fine 2-form with
dG = 0 and C_B G = 0. Then H := hG satisfies dH = G and Q_path^(B) H = 0, and
for every set A of bonds ||H|_A||^2 <= c_H B^2 ||G|_(A+2)||^2, A+2 the plaquettes
based within sup-distance 2 top units of A. In particular every such G is exact.

*Proof.* Pi G = T(C_B G) = 0 and dG = 0, so (b) gives G = d(hG); (c) gives
R hG = 0; (d) applied to G times the indicator of A+2 gives the local bound,
because H on A does not read G off A+2. QED

This is the local estimate that 4.2 of `excess-shell-end.md` names as
unproved ("controlling H by the two endpoint curvatures in a parent-fixed
gauge"): it holds once "parent-fixed" is replaced by the path gauge
Q_path^(B) H = 0, which is enough because the contour part is a pure gauge
(Proposition 2.4). The constraint C_B G = 0 is essential: it is what makes
Pi G vanish and the primitive local, with no long-range period of H around
loops in the shell.
