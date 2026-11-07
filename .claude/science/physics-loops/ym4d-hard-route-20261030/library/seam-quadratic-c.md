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
Lemma 3.1), `parts/hard-core--excess.md` 1.1 (Lemma K), 2.1 (the tensor
right inverse) and 3.3, `library/excess-localized-competitor-stop.md`
Sections 1 and 2. Also seen: single grep lines of those files (section
headers, a few lines of excess-shell-end Section 5 and of the mapped state
of attack and obligations, the (ANCHOR) lines of the competitor note).

**Result.** Quadratic (LC) at the flat background is proved here by hand,
for the actual composite constraint at every odd L >= 3 and every depth n.
1. The nested contours and the depth drop out exactly: only B = L^n enters,
   through the tent map C_B (Section 2).
2. An explicit tensor homotopy gives a local primitive H with
   Q_path^(B) H = 0 (Section 4).
3. The competitor's defect obeys
   sum |R|^2 <= (2 c_R/r^2) sum_{S_(r+5)(D)} (|dA_*|^2 + |dA_t|^2) (Section 5).

So (E-SHELL) holds with A_s = (1 + (2c_R)^(1/2)/r)^2, shell radius r + 5 top
units, K = delta and M_* = 1, none of them depending on L or depth.
At the choice r = (2c_R)^(1/2), where A_s = 4, (RATE-exact) holds for every
nu < nu_0 = arcsinh(1/8)/(r+5), and nu_0 is absolute: as written
nu_0 >= 3.9e-6 (crude), and the measurements suggest about 3e-2. The kill test survived. The step cutoff at a block face, tried
as a control, does grow like L^n.

Open: nonlinear (GLUE-E), (NL-pay), (PATCH), and curved backgrounds.

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
the normalized Wilson action. D is any set of fine sites, the plaquette
anchors, each carrying the six plaquettes based there (in particular a
superlevel set of a weight). Distances are sup-norm distances
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

    c_H := 24 sum_{mu<nu} (3^((mu-1)/2) + 6^(1/2) 3^((nu-2)/2))^2 <= 8024,

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
Cauchy-Schwarz over the six components and Lemma 3.1 (f) give c_H; the six
squares, for (mu,nu) = (1,2), (1,3), (1,4), (2,3), (2,4), (3,4), are below
11.90, 27.49, 69.70, 35.70, 82.46, 107.10, with sum below 334.35. The tensor
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

## 5. The competitor and quadratic (LC) (discharged)

**Data.** Q_n A_* = Q_n A_t = v and G := dA_t - dA_*. Then dG = 0 and
C_B G = d' Q_n (A_t - A_*) = 0 (Corollary 2.3), so H := hG has dH = G and
Q_path^(B) H = 0 (Corollary 4.2). H is a primitive in the path gauge, not the
difference of two parent-fixed representatives.

**Cutoff.** For r >= 1 (top units) and a set D of fine sites, put, for every
point z of R^4, chi(z) := clamp(2 - 2 d(z, D^-r)/r, 0, 1) (chi = 0 if D^-r is
empty), chi_b := chi(base of b), chi_p := chi(base of p). chi is 2/r-Lipschitz
in the sup distance, equals 1 on D^-r and 0 off D^+r. Let
Tr := {sites z : r/2 < d(z, D^-r) < r}.

**Competitor.** With T_1 := T on coarse 1-forms and E as in Proposition 2.4,

    Z := chi H - T_1 Q_path^(B)(chi H),      X_D := A_* + Z + d E Phi_n(Z).

**Theorem 5.1 (quadratic (LC) at the flat background).** For every L odd >= 3,
depth n, volume, set D and r >= 1:
(i) Q_n X_D = v.
(ii) dX_D = (1 - chi) dA_* + chi dA_t + R with

    R = [d,chi] H - T_2 d' Q_path^(B)(chi H),     [d,chi]H := d(chi H) - chi dH.   (SEAM-B)

(iii) R vanishes on plaquettes based farther than 4 top units from Tr, and R
reads G only on N_5 := {plaquettes based within 5 top units of Tr}, which
lies in the plaquettes based in S_(r+5)(D).
(iv) With c_R := 62256 c_H <= 5.0 x 10^8,

    sum_p |R(p)|^2 <= (c_R/r^2) sum_{p in N_5} |G(p)|^2
                   <= (2 c_R/r^2) sum_{p based in S_(r+5)(D)} [|dA_*(p)|^2 + |dA_t(p)|^2].   (LC)

So (LC) holds with C_seam = 2 c_R / r^2, kernel K = delta_0, shell S_(r+5)(D).
Nothing here depends on L, n, the volume, D or the position.

*Proof.* (i) Q_path Z = Q_path(chi H) - (R T) Q_path(chi H) = 0, then
Proposition 2.4 (i). (ii) dX_D = dA_* + dZ, and dZ = chi G + [d,chi]H
- T_2 d' Q_path(chi H) because d T = T d'; finally dA_* + chi G
= (1 - chi) dA_* + chi dA_t.
(iii) On the plaquette p = (z; mu nu),
[d,chi]H(p) = (chi(z+e_mu) - chi(z)) H_nu(z+e_mu) - (chi(z+e_nu) - chi(z)) H_mu(z+e_nu),
e the fine unit steps. Since |d(z, D^-r) - d(z', D^-r)| <= 1/B < r/2 for
neighbours, a value change between neighbours puts one of them in Tr. Because
Q_path H = 0, Q_path(chi H)(c) = Q_path((chi - chi(c_*)) H)(c), c_* the midpoint
of the coarse bond c, and every bond base in the support of the kernel q_c of
Q_path at c lies within sup-distance B - 1/2 fine units, below 1 top unit, of
c_* (along mu the support is [y-m, y+m+B-1], across it I(y)). So
Q_path(chi H)(c) = 0 unless c_* is within 1 + 1/B of Tr; its coarse curl lives
on coarse plaquettes centred within 2 of Tr; T_2 spreads at most 1 + 1/(2B)
along the plaquette axes and below 1.5 across (Lemma 3.1 (e)). Hence R lives
within 4 of Tr. R reads H on bonds within 2 + 1/B of Tr and H reads G below
2 further (Lemma 4.1 (d)): G on N_5. If a site u is within 5 of some z in Tr,
then d(u, D) < 5 + r, and u is not in D^-(r+5), for otherwise every site within
r of z would be in D, so z would be in D^-r. So N_5 lies in S_(r+5)(D).
(iv) From (iii), |[d,chi]H(p)| <= (2/(rB)) (|H_nu(z+e_mu)| + |H_mu(z+e_nu)|), and a
bond plays this role in at most 3 plaquettes, so ||[d,chi]H||^2 <= 24 ||H|_A1||^2/(r^2 B^2)
with A1 the bonds within 1 of Tr. Next q_c >= 0 with sum_b q_c(b) = B (Q_path of
the constant 1-form is B) and sum_c q_c(b) = B^-3 (each x - s e_mu lies in
exactly one block). Cauchy-Schwarz with |chi_b - chi(c_*)| < 2/r gives
sum_c |Q_path(chi H)(c)|^2 <= (4/r^2) B B^-3 ||H|_A2||^2, A2 the bonds within
3 of Tr. A coarse plaquette has 4 bonds and a coarse bond lies in 6 coarse
plaquettes, so ||d'Q_path(chi H)||^2 <= 24 sum_c |Q_path(chi H)(c)|^2, and
||T_2 .||^2 <= 324. With |a + b|^2 <= 2|a|^2 + 2|b|^2,

    ||R||^2 <= (48 + 2 x 324 x 24 x 4) ||H|_A2||^2 / (r^2 B^2) = 62256 ||H|_A2||^2 / (r^2 B^2),

and Corollary 4.2 gives ||H|_A2||^2 <= c_H B^2 ||G|_N5||^2. Last,
|G|^2 <= 2|dA_*|^2 + 2|dA_t|^2. QED

**Relation to (SEAM) of excess-shell-end 4.2.** (SEAM-B) is (SEAM) with two
choices made: the relative field is H = hG in the path gauge (Q_path H = 0)
instead of a parent-fixed representative, and the right inverse is
T_n := T_1 + d E Phi_n T_1, for which Q_n T_n = I and d T_n = T_2 d'. Then
d T_n Q_n(chi H) = T_2 d' Q_n(chi H) = T_2 d' Q_path(chi H): the contour part of
the first-order commutator [Q_n, chi] is a coarse gradient and is annihilated
exactly, and the path part is first order in H but carries the factor 2/r.
X_D equals A_* + chi H - T_n Q_n(chi H) up to a pure gauge.

**The transverse mode crossing a block face.** On a face plaquette the first
term of (SEAM-B) is (chi(z+e_mu) - chi(z)) H_nu(z+e_mu), H_nu the component
along the face. For the top-smooth cutoff above this is O(1/(rB)) H_nu spread
over a transition of width r/2 top units, which is what (iv) pays. For a
block-adapted step cutoff (chi jumping by 1 at a block face) the same term is
H_nu on one fine layer: when H is smooth on the top scale the layer carries
about 1/B of the block's ||H||^2, about B ||G||^2 by Corollary 4.2, so the
explicit construction's constant grows like B = L^n. Measured: linear growth,
0.20 to 0.86 from B = 3 to 13 (Section 7). This is a statement about the
explicit construction with a step cutoff, not about every gluing: cutoffs
must vary on the top scale, not jump at block faces.

## 6. (E-SHELL), A_s, r, M_* and (RATE-exact) (discharged)

**Theorem 6.1.** For every set D of fine sites, r >= 1 and eps > 0, with
S' := S_(r+5)(D) and C_seam = 2 c_R / r^2,

    A_*(D) - A_t(D) <= [(1 + eps) + (1 + 1/eps) C_seam] [A_*(S') + A_t(S')].

At eps = C_seam^(1/2) this is (E-SHELL) with

    A_s = (1 + (2 c_R)^(1/2)/r)^2,   K = delta_0,   M_* = 1,   shell radius r_E = r + 5.

*Proof.* A_* is the minimizer on {Q_n A = v} and Q_n X_D = v, so
A(A_*) <= A(X_D). Split the plaquettes by base: I := D^-(r+5), the shell S',
and O := the complement of D^+(r+5). On I, R = 0 and chi_p = 1 (I lies in
D^-r), so dX_D = dA_t; on O, R = 0 and chi_p = 0 (d(u, D^-r) >= d(u, D) > r), so
dX_D = dA_*. On S' use |v + R|^2 <= (1+eps)|v|^2 + (1+1/eps)|R|^2 and convexity
|(1-c)u + ct|^2 <= (1-c)|u|^2 + c|t|^2 for 0 <= c <= 1. Cancelling A_*(O):

    A_*(I) - A_t(I) <= eps A_*(S') + (1+eps) A_t(S') + (1 + 1/eps) ||R||^2.

Since D minus I lies in S' and D misses O, A_*(D) - A_t(D) <= A_*(I) - A_t(I)
+ A_*(S'). Insert Theorem 5.1 (iv). QED

The term (1 + eps) >= 1 is structural: near the boundary of D the excess can
equal the shell energies, whatever the gluing.

**Corollary 6.2 (rate).** beta_* = 2 A_s M_* sinh(nu r_E)
= 2 (1 + (2c_R)^(1/2)/r)^2 sinh(nu (r + 5)). Take r := (2 c_R)^(1/2) <= 31623. Then
A_s = 4, r_E <= 31628, and

    (RATE-exact) holds  iff  nu < nu_0 := arcsinh(1/8) / r_E,   nu_0 >= 3.9 x 10^-6.

Then (WAM-req) holds by `library/excess-seam.md` Section 2 with
D_A = 2 b_s/(1 - beta_*), b_s = 8 r_E cosh(nu r_E), uniformly for 0 <= s <= nu.
At nu = nu_0/2: beta_* < 0.5, b_s < 2.6 x 10^5, D_A < 1.1 x 10^6.

**L-dependence.** None. A_s, r_E, M_*, nu_0, b_s and D_A are absolute numbers:
free of L, the depth n, the volume, the position, D, x and the weight
normalization. So (RATE-exact) holds at a rate nu fixed before L, for every
nu < nu_0, and nu_0 does not move when L is chosen. The written nu_0 is crude;
the measured worst case (Section 7) suggests C_seam near 0.25 at r = 2 and an
admissible rate of order 3 x 10^-2 with r_E = 7, guidance only.

## 7. Kill test (numerics; guidance only)

Files: `checks/seamqc/seamqc.py` (all code), `seamqc_results.json`,
`seamqc_run.log`, `seamqc_rscan.json`, `seamqc_rscan.log`. Runs on the Mac mini
under `lab_ops.py numeric-lock` (acquired, then released), BLAS threads 1,
`nice`, a 2 GB RSS stop (peak 1.92 GB), memory free 64 to 65 percent at
start. Run time 24 s plus the r scan.

**Criterion 1, identities: PASS.** Largest deviation 4.6e-13, an absolute
maximum of C_B P_0 v for the FFT projector P_0 onto G_0 at B = 13; every
other check is at most 2.5e-15, relative or absolute. Checked: the 1D
identities of Lemma 3.1 for B = 3, 5, 7, 9, 11, 13, 21, 41 on circles of 1, 2
and 5 blocks; R^(L) R^(L) = R^(L^2) for L = 3, 5; the 4D chain maps, R T = I,
(I - Pi) = dh + hd on 0-, 1- and 2-forms, R h = 0, adjoints; for the actual
nested map at L = 3, n = 2 with axial-staircase contours on 18^4:
d'Q_2 = C_9 d, Q_2 d = d' r_2, Q_2 - Q_path^(9) curl- and holonomy-free, and the
competitor of Section 5 has Q_2 (Z + d E psi) = 0 to 8e-16. In every seam run:
dH = G, Q_path H = 0, C_B dZ = 0, and (SEAM-B). One apparent failure
(dT^0 = T^1 d' at one block per circle, relative error 1.0) is 0/0: both
sides vanish identically there, absolute difference 3e-16.

**Criterion 2, depth and L: SURVIVE.** Slab D = half the torus along axis 0,
torus of 8 x 1 x 1 x 1 top blocks (also 8 x 2 x 2 x 2 for B <= 7), top-smooth
cutoff with r = 1, boundary of D on a block face. Ratio ||R||^2/||G||^2,
G = (I - Pi) dA for the test fields; the first column is the worst case over
all of G_0 (power iteration with an FFT projector onto G_0, 40 steps; 60 steps
in the r scan agree to 3 digits).

| B | worst case on G_0 | face mode, top-scale transverse | face mode, fine transverse | face mode, narrow | white noise | smooth noise | step cutoff, narrow face mode (control) |
|---|---|---|---|---|---|---|---|
| 3 | 0.287 | 0.0291 | 0.0291 | 0.0000 | 0.0100 | 0.0079 | 0.201 |
| 5 | 0.232 | 0.0339 | 0.0138 | 0.0016 | 0.0048 | 0.0064 | 0.345 |
| 7 | 0.215 | 0.0362 | 0.0078 | 0.0067 | 0.0032 | 0.0056 | 0.501 |
| 9 | 0.207 | 0.0376 | 0.0049 | 0.0106 | 0.0022 | 0.0051 | 0.623 |
| 11 | 0.203 | 0.0386 | 0.0034 | 0.0131 | 0.0017 | 0.0046 | 0.740 |
| 13 | 0.200 | 0.0393 | 0.0025 | 0.0147 | 0.0014 | 0.0042 | 0.860 |

Two departures from the registered wording, neither affecting the
criterion. The cutoff used is that of Section 5, of slope 2/r rather than
1/r: it is one fixed top-unit geometry at every B. The shell-normalized
ratios (denominator over plaquettes within 4 top units of the transition)
were recorded and coincide with the full-norm ones tabulated, because in
this geometry that neighbourhood of the two transition layers is the whole
torus. So this run does not separately test a thin shell; Theorem 5.1 does.

The worst case falls with B. The top-scale face mode levels off (increments
0.0048, 0.0023, 0.0014, 0.0010, 0.0007). The narrow face mode is still rising
at B = 13 (it resolves better as B grows), but stays below the worst case,
which is a supremum over all of G_0. The step-cutoff control grows linearly in
B, as Section 5 predicts, so the test does see depth growth where it exists.
With two transverse blocks the face modes are 0.105, 0.087, 0.085
(top-scale) at B = 3, 5, 7, also falling.

**r scan** (torus 12 x 1 x 1 x 1 blocks, worst case on G_0): 0.340 and 0.432
at r = 0.5, 0.232 and 0.207 at r = 1, 0.127 and 0.124 at r = 2, for B = 5 and 9.
It falls with r, more slowly than r^-2 at these small r, because the
neighbourhood that h reads has a fixed size of about 2 top units. All values
are far below the written bound c_R/r^2.

**What the runs do not establish.** They cover one geometry and finite
families; they prove no bound. The bound is Theorem 5.1. They refute
nothing: no identity failed and no ratio grew for the proposed construction.

## 8. Verdicts, consumers, and what stays open

| Statement | Label |
|---|---|
| Prop 2.4: at the flat background the quadratic seam problem depends on L and n only through B = L^n; contours and the point-anchored gauge drop out | discharged here, hand proof; checked at L = 3, n = 2 |
| Cor 4.2: closed G with C_B G = 0 has the local primitive hG in the path gauge | discharged here |
| Thm 5.1: quadratic (LC), C_seam = 2 c_R/r^2, K = delta_0, shell S_(r+5)(D) | discharged here |
| Thm 6.1: (E-SHELL), A_s = (1 + (2c_R)^(1/2)/r)^2, M_* = 1, r_E = r + 5 | discharged here, quadratic flat level |
| Cor 6.2: (RATE-exact) at every nu < nu_0 = arcsinh(1/8)/r_E, nu_0 absolute (>= 3.9e-6 as written) | discharged here, quadratic flat level |
| Kill test of Section 1 | survived |

All same-model work, not read by anyone else yet; no status.

**Consumers that change.**
1. (LC) of `excess-shell-end.md` 4.2 should be read with the path-gauge
   primitive H = hG and a chain-map right inverse (d T_n = T_2 d'). Then the
   contour part of [Q_n, chi] drops out exactly, and no parent-fixed alignment
   (the END and (ANCHOR) issue) is needed at the quadratic level.
2. The rate gap of `excess-seam.md` closes at this level without any post-L
   repair: the mapped order gains one pre-L ceiling, nu <= nu_0 with nu_0
   absolute, and then (DS-rate) forces mu <= nu_0/2 and delta_# >= 4 mu. Every
   reader of nu and mu must accept these small fixed rates; not checked here.
3. D_A (about 1e6 as written) enters D_TOP of (UP-constants); it is absolute,
   so FALL's L-dependent slots are untouched.

**What stays open (first step not carried through).**
1. **Nonlinear (GLUE-E), (NL-pay), (PATCH).** Section 2 is linear. For the
   nonlinear M_n the contour part is a coarse gauge transformation only up to
   the O(L^2 a^2) terms of Lemma LE, at every level of the composite. The chain
   map T, the primitive hG and the seed chi H have no nonlinear counterparts
   here; class membership of the intermediate images and the replacement cost
   with tails are untouched. Unproved remark: since C_seam is absolute,
   nonlinear errors of relative size C(L) x flux would be paid by the flux
   threshold chosen after L. That is the form the nonlinear step must take.
2. **Curved backgrounds** (class branch, walls): the linearized constraint
   becomes Ad-twisted, and the tensor structure of Sections 3 and 4 is lost.
   Not attempted.
3. **Assumptions used:** contour families covariant under coarse translations
   (true for a fixed rule such as Balaban's); the quadratic class is the whole
   fibre {Q_n A = v}; anchors are fine sites, distances sup-norm in top units.
4. The written c_R and nu_0 are crude, by about 1e4 in nu_0 against the
   measurements. Sharpening them is routine and was not done.

**Read and not read.** Read: the files listed in the header, nothing else of
the repository. Not read: `library/seam-quadratic.md`, every file excluded for
the mapped side in FINISH.md, every gate, and the Sussman-Alpoge repository.
No literature was consulted. No subagent, commit, push or post.
