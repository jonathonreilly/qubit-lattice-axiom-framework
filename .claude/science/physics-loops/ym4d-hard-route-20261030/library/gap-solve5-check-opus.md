# Check of gap-solve5-astra62.md (FINISH row 1152)

Status: done (2026-11-19). Checked line by line, by hand, by Claude Opus 5.5 at max effort, as a laptop subagent.
This is one check of row 1151, cross-provider as row 1152 states. I did not verify the author of row 1151 beyond
its file name. The numeric run in Step 3 is a GUIDE only. It proves nothing.

Task: FINISH row 1152. Check, line by line and by hand, `library/gap-solve5-astra62.md` (row 1151). Positive claims first.

## Plan (eight steps; each step appends its result here)

1. Read the setting (`library/gap-council-brief.md`) and all of `library/gap-solve5-astra62.md`, in ranges.
2. Read the parts of rows 1143, 1147, 1149 and their checks that row 1151 cites.
3. Check Section 14: the whole-endpoint bound (29). Short-time convexity, box holonomy positivity, the Gaussian comparison (30) and its exact cancellation, the mode sum.
4. Check Sections 15-17: the deletion results (31)-(35), dissemination and time folding, (32)-(33), the parity-class moment, the exponent choice.
5. Check Section 13: the equivalence (28).
6. Check the effective seam (1) and Sections 2-5, 8-9.
7. Check the obstructions of Sections 6-7, 10-12.
8. Verdict table and RESULT line.

## Step 1 result: what the note claims

Read in full: `library/gap-solve5-astra62.md` lines 1-534 (in four ranges) and `library/gap-council-brief.md` lines 1-122.

The note works with the one-step log thermal ratio J of row 1149 at fixed physical side L, n = L/a_j, T = n/2,
N = n^3. The target (its (15)) is limsup_j J < log(1651/1650). The note claims, as PROVED:

- (29), L425-456: 0 <= J(beta) <= C_sigma n^3 beta^(-sigma) for every 0 < sigma < 1/16 (a density bound only).
- (31)-(35), L460-512: concentration of clipped deletion factors on one time slice, and complete deletion of
  floor(beta^alpha) residual faces of one class, 0 < alpha < 1/20480 (Section 16), improved to 0 < alpha < 1/80
  (Section 17), with signed error o(1).
- (28), L409-419: the target is equivalent to a shortened signed integral on A_j = D'_j minus S_j, with S_j at zero
  and a terminal interval of width beta^(1+eps)/M_j removed.
- (1)-(14), (19)-(24): an effective seam expansion, Poisson open-cylinder tests, ladder and rung restorations, a
  terminal interval and a local Gaussian comparison.
- Obstructions (15a), (16)-(18), (25)-(27): limits of the methods. None is claimed as a counterexample.

The note marks the face bound (15), the wall (W) and the mass gap OPEN (L534).

## Step 2 result: inputs read

Read: row 1149 (`library/gap-solve4-astra62.md`) L1-408; its check (row 1150, `library/gap-solve4-check-opus.md`)
L712-805; row 1143 (`library/gap-solve-astra62.md`) L205-294 and its check L154-195; row 1145
(`library/gap-solve2-astra62.md`) L15-30 and L368-383; row 1147 (`library/gap-solve3-astra62.md`) L13-30 and the
tilted-variance line L217; the verdict table of its check (row 1148) L549-624.

The inputs row 1151 uses, and their status at this pin:

- Row 1149 (13)-(15) (L180-211): D'_j, v_2, sup over |v| <= v_2 of |J'(v)| -> 0, and the target (15). Row 1150 says
  HOLDS for all 66 statements, including (13)-(15), (16), (20)-(23), (24)-(26). So the note's remark that row 1149
  is "an unchecked research input at this pin" (L3, L17, L417) is now out of date. Its check exists and finds no
  failure. This changes no conclusion.
- Row 1149 Section 2 (L83) and Section 5 (L202): each magnetic block error is bounded by exp(sum of |u_p|) - 1.
  Setting some couplings to zero only lowers that sum. This supports the cold-end claim at L417.
- Row 1149 Section 6 (L224): M_0 >= c(n/B)^3 residual 12-faces with disjoint factors, B = floor(beta^theta). This
  is the source of the count P used in Sections 16-17.
- Row 1143 (14) (L224-229): c b^(-5) I <= K_S <= 24 I and max_e |U_e - 1|^2 <= 8 b A_box on the 4D open cube with
  the comb; chain length <= 4b. Row 1144 says HOLDS. Section 14 of row 1151 uses the 3D spatial version (chain
  <= 3(b+1)) plus temporal chains along the tree. I re-derive this in Step 3.
- Row 1143 (15)-(16) (L231-273): the open-box Gaussian comparison with b = ceil(beta^gamma), gamma < 1/12, credited
  to Chatterjee's free-energy method. Checked HOLDS by row 1144.
- Row 1145 (1) (L19-24): I_d(s)/I_1(s) <= exp[-(d-1)/(1+6 beta)]. Row 1145 (24) and Section 10 (L376-381): the
  target is limsup_j J(beta_j) < log(1 + 1/1650), with log(1+S) <= J <= 2 log(1+S).
- Row 1147 L217: Hoeffding's lemma by the tilted variance (range w gives log moment <= t^2 w^2/8).

## Step 3 result: Section 14, the whole-endpoint bound (29) (L423-458)

Notation: J = psi(T) with psi(q) = 2 log Tr F^q - log Tr F^(2q), F = MCM >= 0 and trace class on the physical
space (C has multipliers a_beta(d) with sum of d^2 a_beta(d) finite).

**14.1 Short time (L432). HOLDS.** Phi(q) = log sum_i (lambda_i/||F||)^q is convex (log-sum-exp of functions
linear in q). For q1 < q2, Phi(2q2) - Phi(2q1) = 2 int_{q1}^{q2} Phi'(2y) dy >= 2 int_{q1}^{q2} Phi'(y) dy, so psi
is non-increasing. The ||F|| terms cancel in psi. Hence J = psi(T) <= psi(m) for every integer 2 <= m <= T.
Convexity alone suffices; the differentiability remark is not needed. With normalized convolutions,
Tr F^m = Z_m z_beta^(-3Nm), and the z_beta powers cancel in 2 log Z_m - log Z_2m. The tiling into sides b, b+1 needs
n mod b <= floor(n/b), true since n >> b^2.

**14.2 One temporal holonomy per box (L434). HOLDS.** Dropping the crossing plaquettes raises Z (weights <= 1) and
factorizes it over the boxes B x Z_s; the joining links integrate to one. In B x Z_s the s spatial comb trees and
the s-1 root temporal links form a spanning tree (s|B| - 1 edges, connected). So the other links, h included,
are independent Haar. Integrating the nonroot temporal links projects onto invariance under the based gauge group
(g(root) = 1). The wrap inserts U_h, which acts on based-invariant states as any gauge transformation with value h
at the root, and commutes with T = M C_0 M >= 0. So Z_{B,s}(h) = Tr(T^s U_h), and
0 <= Z_{B,s}(h) <= Tr T^s = Z_{B,s}(1). (Fixing the spatial trees uses only based transformations, which do not move
h or the root links.) Hence log Z_m <= sum_B log Z_{B,m}(1).

**14.3 Gaussian comparison, upper inequality of (30) (L436-441). HOLDS.** Spatial links: the 3D comb chain of
row 1143 (14) has at most 3(b+1) distinct plaquettes. Temporal links: along the tree path the spatial links are one
on both slices, so the temporal plaquette holonomy is V_x V_y^(-1). At h = 1 the root temporal links are all one,
also across the wrap. So |1 - U_e| <= sum over at most 3(b+1) plaquettes of |1 - U_p|, and with |1 - U|^2 = 2a
Cauchy-Schwarz gives max_e |1 - U_e|^2 <= C b A. Linearized and summed over <= C b^3 s <= C b^4 edges (s <= 2m <= b):
||X||^2 <= C b^5 ||dX||^2. Each edge lies in six plaquettes of four edges, so d*d <= 24. On the chart
|X_e| <= b^(-7/2): the BCH remainder is <= C b^(-7/2) sum_{e in p} |X_e|, so its l2 norm is <= C b^(-7/2) ||X||
<= (C/b) ||dX||. Then beta A lies between (1 -+ C/b)(beta/2)||dX||^2, and the Gaussian changes by
(1 -+ C/b)^(-dim/2) with dim <= C s b^3. That is the error O(s b^2). Haar Jacobian: (sin|X|/|X|)^2 = 1 + O(b^(-7))
per edge. Off the chart, A >= c b^(-8), so the integral is <= e^(-c beta/b^8). The Gaussian is >= e^(-C b^4 log beta).
The ratio is small because beta^(1-8 gamma) >> beta^(4 gamma) log beta, which is gamma < 1/12. The Gaussian leaves
the chart with probability <= C b^4 exp(-c beta b^(-12)), since each variance is <= C b^5/beta. Summing over the
<= N/b^3 boxes gives C N m/b.

**14.4 Lower inequality of (30) (L443). HOLDS.** The union of the box trees is a forest, so this is a valid gauge
fixing and the joining links stay Haar. Each crossing plaquette (spatial: two joining links and two
boundary-tangent links; temporal: two joining links and two boundary temporal links) then has every link restricted
or tree-fixed. So its action is O(1/beta). A ball of radius 1/beta has Haar mass >= c beta^(-3). That costs
O(s b^2 log beta) per box for the O(s b^2) restricted links. For an internal plaquette with restricted links,
|1 - U_p| <= |1 - U_p^0| + sum |1 - U_e|, and (v+w)^2 <= (1 + beta^(-1/4)) v^2 + (1 + beta^(1/4)) w^2 gives
beta a_p <= (1 + beta^(-1/4)) beta a_p^0 + C beta^(-3/4). (The note's additive O(s b^2) is a weaker valid bound.)
The comparison of 14.3 holds on the principal restriction. The Schur complement on the removed coordinates has
spectrum in [c b^(-5), 24] (min-max). So the removed Gaussian coordinates cost <= C log beta each, and the
coupling (1 + beta^(-1/4)) beta costs O(s b^3 beta^(-1/4)). Summed: log Z_2m >= sum_B log G_{B,2m}
- C N m log(2 + beta)/b.

**14.5 Exact Gaussian cancellation (L445-450). HOLDS.** The temporal plaquette on edge e gives
x_{t+1}(e) - x_t(e) - (grad phi_t)(e). The phi_t integral (phi_t(root) = 0, at h = 1 also across the wrap) gives a
constant times exp(-(beta/2)||P(x_{t+1} - x_t)||^2), the same constant for every t. The map x -> Px from
tree-fixed fields onto ker grad* is a bijection (Px = 0 means x = grad psi, zero on the tree, so psi is constant).
Also d_s x = d_s Px, since d_s grad = 0. On ker grad*, d_s* d_s > 0 (box simply connected). Each mode gives the
periodic chain (2 + lambda) I - S - S^(-1), with determinant prod_k (2 cosh w - 2 cos(2 pi k/s)) = 2 cosh(s w) - 2
= e^(s w)(1 - e^(-s w))^2. Every per-step scalar enters log G_{B,s} linearly in s and cancels. So
2 log G_{B,m} - log G_{B,2m} = 3 sum_lambda log[(1 + e^(-m w))/(1 - e^(-m w))]. GUIDE run (not proof):
`check1152/gauss_box_pure.py` in the scratchpad builds the full gauge-fixed quadratic form with periodic time and
h = 1. On boxes 2x2x3, 2x3x3 and 3x3x3 with m = 1, 2, 3 it gives 2 log G_m - log G_2m equal to the analytic mode
sum to ten digits. (For example 8.8279364168 for 3x3x3, m = 1.)

**14.6 Mode sum and the final bound (L452-456). HOLDS.** The function f(lambda) = log[(1 + e^(-m w))/(1 - e^(-m w))]
is >= 0. Delta_1 = grad grad* + d_s* d_s preserves ker grad*, where it equals d_s* d_s. So the mode sum is at most
the sum over spec(Delta_1). On a product of paths, for direction-i edges,
Delta_1 = (path edge Laplacian)_i + sum_{j != i} (vertex Laplacian)_j. The cross terms cancel because d_1 and d_2*
act on different tensor factors and commute. The Neumann cosine vectors and their gradients diagonalize this:
lambda(q) = sum_j 4 sin^2(pi q_j/(2 a_j)), with q_i >= 1. Then lambda >= 4|q|^2/(b+1)^2 and w >= c|q|/b. Writing
f = 2 sum_{l odd} e^(-l m w)/l, and using O(r^2) indices at sup-radius r and sum_r r^2 e^(-x r) <= C x^(-3), gives
<= C (b/m)^3 per box. So J/N <= C[m^(-3) + m log(2 + beta)/b]. With m = floor((b/log(2+beta))^(1/4)) this is
C (log beta)^(3/4) beta^(-3 gamma/4) <= C_sigma beta^(-sigma) for 4 sigma/3 < gamma < 1/12. Also 2m <= b and m <= T
hold. The lower bound J >= 0 is Tr F^(2T) <= (Tr F^T)^2.

**14.7 Size of the short-time comparison (L458). HOLDS.** For q with all three q_j in [b/(4m), b/(2m)], the three
direction modes at lambda(q) contain one gradient. So ker grad* holds two transverse modes with m w <= C, each
giving f >= c. Their number is >= c (b/m)^3 per box. So this Gaussian upper comparison is >= c N/m^3, which tends
to infinity since m <= b << n. It can control only the density J/N, as the note says.

**14.8 Statement (29) and its scope (L425-430). HOLDS.** It is a density bound: n_j^3 grows faster than every
power of beta_j, so the right side diverges. The remark that it also bounds the signed face integral of row 1149
(15) up to its o(1) cold end is right, by row 1149 (14).

## Step 4 result: Sections 15-17, the deletion results (L460-532)

**15.1 Setting and (31), second clause (L462-469). HOLDS.** mu_* = E e^{|Z|^2/4} = (1 - 1/2)^(-3/2) = 2^(3/2). With
X = sum_i |Z_i|^2/4: mu_*^r - m_{r,beta} = E(e^X - B)_+ <= B^(-1/2) E e^{(3/2)X} = 8^r B^(-1/2).

**15.2 Spatial dissemination (L471). HOLDS.** For orientation 12, direction x3 carries the marks inside its
layers: a positive multiplication operator, so the layer step K^(1/2) M_c K^(1/2) is positive. In directions x1
and x2 the mark is on a crossing plaquette. In axial gauge its trace is w(V U^(-1)) of the two layer links. So the
marked kernel is k(g_1,...,g_r) = prod_i e^(-beta a(g_i)) exp(s g_p), a class function in each argument with
k(g^(-1)) = k(g), real. Its convolution is self-adjoint and commutes with the diagonal gauge action. It may be
indefinite. With n even, ||T_c||_n^n = Tr T_c^n, and Tr T_c^n is a positive path integral. Trace Holder gives
log Z(C) <= n^(-1) sum_c log Tr T_c^n. Iterating over x1, x2, x3 leaves only the all-marked slice pattern, with
weight P/N, and the unmarked pattern. So log E e^{s sum_C g} <= (P/N) log E e^{s sum_slice g}, for every real s.

**15.3 Time folding and (32) (L473-478). HOLDS.** Tr(F^T (x) F^T SWAP) = Tr F^(2T). So the d period-2T fields become
2d period-T copies, and the r readings sit on one folded slice. With A = C^(1/2) M, AA* has the nonzero spectrum
of F. H and H_s = A^(x)r e^{s sum g} A*^(x)r are positive. Trace Holder: |Tr(H^(T-1) H_s U)| <=
(Tr H^T)^(1-1/T) (Tr H_s^T)^(1/T). The denominator is (Tr F^T)^(r-2d) (Tr F^(2T))^d. Dividing gives
log E e^{s sum_slice g} <= d J + T^(-1) log(Tr H_s^T/Tr H^T) = d J + N [p_r(s) - p_r(0)]. With 15.2 this is (32).

**15.4 (33) (L480-486). HOLDS.** H_1: on {e^X < B}, |grad e^X| = e^X |r| <= B sqrt(2 log B). Upper bound: dropping
crossing actions raises the integral; dropped sources are <= e^(|s|B) each, on a fraction O(1/b + b/n). Off the
chart a cube costs <= r exp(|s| B b^4 - c beta/b^8), negligible since |s| B <= 1. On the chart the radius error has
squared sum <= C b^(-2) beta sum_i ||dX_i||^2. By Cauchy-Schwarz over <= C b^4 faces and 2xy <= x^2/b + b y^2, the
source error is <= beta sum ||dX||^2/(2b) + C b^3 s^2 H_1^2 per cube. The first part goes into the precision
(1 - C'/b) beta K. The second part is C s^2 H_1^2/b per site, inside the last term of (33). Normalizers: (22b) gives
O(r Delta_b) per site. The source sum has Lipschitz constant <= C H_1 sqrt(V) in standard normals (the curl map has
norm <= (1 - C/b)^(-1/2)). So the Section 9 Gaussian bound gives C s^2 H_1^2 per site.

**15.5 Mean of the source and (31), first clause (L488). HOLDS.** The projection difference has
||P_open - P_per||_HS^2 = O(b^3) over 6 b^4 faces (verified in Step 7, 12.1). So the mean squared diagonal error is
O(1/b). |sqrt(u) - 1/sqrt 2| <= sqrt 2 |u - 1/2|, and Cauchy-Schwarz gives the error C H_1/sqrt(b). Exponents, with
sigma = 1/32 and |s| = beta^(-1/64), each divided by |s|: J/N gives <= C beta^(-1/64); Delta_b gives
beta^(-3/64) log beta; H_1/sqrt b gives beta^(1/512 - 1/32) (log beta)^(1/2); B/b gives beta^(1/512 - 1/16);
|s| H_1^2 gives beta^(-6/512) log beta. All are o(beta^(-1/512)), and |s| B = beta^(-7/512) <= 1. Exponential Markov
in both signs gives exp[-P |s| beta^(-1/512)(1 - o(1))] = exp[-c P beta^(-9/512)].

**16.1 Statement of Section 16 (L492). HOLDS, with a wording precision.** "(28) holds with A_j = D'_j minus S_j"
must be read as "the equivalence of (15) with (28) holds for this A_j", as in Section 13 and the RESULT line L534.
The inequality (28) itself stays OPEN. The count: row 1149 L224 gives M_0 >= c(n/B)^3 residual faces on a layer.
The largest of the six classes has at least a sixth of them, so P >> beta^C for every C.

**16.2 (34) (L494-499). HOLDS.** For one field, prod_{p in I} H_p^(1+delta_0) is the (23)-moment of |I| or 2|I|
distinct faces of one class. The readings at t0 and t0 + T have the same orientation and parity, so (23) applies.
Distinct S is needed, as stated.

**16.3 (35), bad event (L500-504). HOLDS.** E[prod_S H 1_bad] <= e^{C r k/(1+delta')} P(bad)^(delta'/(1+delta')),
and P(bad) <= 2 exp(-c P beta^(-9/512)) with P beta^(-9/512) >> k. This is o(1) and mu_*^{rk} >= 1.

**16.4 (35), good event (L506). HOLDS.** Lower: with replacement and weights g_p/(P a), the collision probability is
<= C(k,2) max g/(P a) <= k^2 B/(2P), since a >= 1; ordered distinct tuples number <= P^k. So
E_S prod g >= a^k (1 - k^2 B/P). Upper: for disjoint (L, S') with |L| = l, the average over S' of prod g is
<= (P a)^(k-l)/(P-k)^(k-l) <= e^{C k^2/P} a^(k-l). Also h_p <= B^(-delta') H_p^(1+delta'), and (34) at delta' holds
for distinct L. The sum is e^{C k^2/P}(mu_*^r + d_beta + e^{C r} B^(-delta'))^k. Ratio -> 1 needs k d_beta -> 0
(alpha < 1/1024), k B^(-delta') -> 0 (alpha < delta'/512) and k^2 B/P -> 0. All hold for alpha < 1/20480.

**16.5 Signed normalizers (L508). HOLDS.** Two independent fields with the same S give E_S W_i(S)^2. So
E_S (W_i/mu_*^{ik} - 1)^2 -> 0, and 2 log W_1 - log W_2 -> 0 in probability.

**16.6 Simultaneous terminal interval (L510). HOLDS.** With u = q t/beta = q beta^eps/|D'_j| and the two-sided
estimate of Section 8 (L278-284; negative u covered by (22a) on |u| <= 1/4):
log E e^{q Y_i} = O(|q| beta^(eps - eta) + q^2 beta^(2 eps)/|D'_j|) -> 0 for eps < eta < 1/24. The tilt keeps
P(bad) up to C sqrt(P(bad)) by Cauchy-Schwarz, and keeps (34) at delta' by Holder with exponent
(1+delta_0)/(1+delta'). The swap of the tilt on S_j and of |D'_j| for |A_j| each cost <= 2 i t k
= 2 i beta^(1+eps+alpha)/|D'_j| -> 0. The cold end is row 1149 (14) with individual couplings (Step 5). So the
tilted normalized moments -> 1 for a deterministic S_j, and the hot end of (28) is J_full + o(1).

**16.7 Absolute accuracy (L512) and OPEN (L514). HOLD.** A constant reading u(1+d) gives (1+d)^k, which is trivial
and correct. It is a limit of this moment method only, as stated.

**17.1 Finer class (L518). HOLDS.** There are 3 x 8 classes, so P keeps the same order. T = n/2 is even on the
dyadic grid, so t0 and t0 + T have the same time parity.

**17.2 Dissemination with four parities (L520). HOLDS.** Pairing a marked-parity step with its homogeneous
neighbour gives Tr(... L_i L L_j L ...) = Tr(... (L^(1/2) L_i L^(1/2))(L^(1/2) L_j L^(1/2)) ...) with L >= 0. For
the in-plane directions there are n/2 pairs, an even number for n >= 4 dyadic, so the self-adjoint, possibly
indefinite, pair operator has Tr|.|^(n/2) = Tr(.)^(n/2). The perpendicular spatial direction and time carry
positive magnetic factors. The fully disseminated pattern marks V/16 faces, hence the factor 16|S|.

**17.3 Pointwise bound M_0 <= (3/2) U_0 (L522). HOLDS.** For p in the (mu,nu) plane the four cubes are the
extensions by +-rho and +-sigma. Five-face telescoping and weighted Cauchy-Schwarz with weights (2;1,1,1,1) give
a_p <= 6(a_o/2 + sum_sides a_s). The opposite face p +- e_rho has flipped rho parity, so it is unmarked. It is the
opposite face of exactly the two marked faces o -+ e_rho. A face o -+ e_sigma has the wrong sigma parity, so it is
not marked. A side face in the (mu,rho) plane fixes the extension direction rho. The nu parity picks the base, and
the rho parity picks the end. So each side face is used at most once. Opposite faces (same orientation, wrong
parity) and side faces (other orientations) are disjoint unmarked sets. So M_0 <= (6/4) U_0. Then
U_0 - delta M_0 >= (1 - 3 delta/2) U_0 >= (2/5)(1 - 3 delta/2)(U_0 + M_0), and the Section 9 pressure comparison at a
fixed coupling ratio gives a constant for each delta < 2/3.

**17.4 Choice of exponents (L524-530). HOLDS.** The feasibility condition alpha/delta' < sigma/2 - alpha is
alpha < sigma delta'/(2(1 + delta')). Its supremum, at sigma -> 1/16 and delta' -> 2/3, is
(1/16)(2/3)/(10/3) = 1/80. After division by |s| = beta^(-sigma/2 - kappa): exchange gives beta^(kappa - sigma/2);
Delta_b gives beta^(-1/16 + sigma/2 + kappa) log beta, at most the same since sigma < 1/16; H_1/sqrt b gives
beta^(kappa - 1/32) (log beta)^(1/2); |s| H_1^2 gives beta^(kappa - sigma/2) log beta. All are o(beta^(-h)) for
h < sigma/2 - kappa. |s| B = beta^(-sigma/2) <= 1. Also k beta^(-h) -> 0 (alpha < h), k B^(-delta') -> 0
(kappa > alpha/delta'), and the clipped Gaussian mean error is O(B^(-delta')) since
E e^{(1+delta')|Z|^2/4} < infinity for delta' < 1.

**17.5 Limitation (L532). HOLDS.** a/|s| + b|s| >= 2 sqrt(ab) with a = beta^(-sigma), b = H_1^2. This reproduces the
same 1/80 restriction. The last sentence is a scope remark.

## Step 5 result: Section 13, the equivalence (28) (L409-421)

**13.1 (28) is equivalent to (15) (L411-417). HOLDS.** The integrand: d/dv[2 log Z_1 - log Z_2] with M_j and
2 M_j faces at weight e^(-v a) gives 2 M_j w_{1,A} - 2 M_j w_{2,A}; the constants -M_j cancel. The integral of (28)
equals J(A at beta - t, S at 0) - J(A at v_2, S at 0). That of row 1149 (15) equals J_full - J'(v_2). Both cold
values are o(1). Row 1149 (14) bounds each magnetic group by exp(sum of |u_p|) - 1 (its L83 and L202), and zeroing
a coupling only lowers that sum and deletes polymers. The hot ends agree up to o(1) by 13.2. So the two limsups
coincide, and the strict inequalities are equivalent. S_j lies in the slab of h_2 = 1 + m_2 H_2 layers, which is
polylogarithmic in n, as Section 9 requires.

Status remark (not a correction): L417 calls row 1149's box estimate "still an unchecked input at the pin". The
check of row 1149 (row 1150, `library/gap-solve4-check-opus.md` L805) now finds all of (13)-(15) HOLD. The same
out-of-date remark is at L3 and L17.

**13.2 Hot end with both changes (L419). HOLDS.** Here k denotes the number of periods, 1 or 2. Inputs: (23) gives
E e^{(1+delta_0) X} <= e^{C_0 k |S_j|} = beta^C. The two-sided Section 8 estimate, with u < 0 allowed because
couplings beta(1 + |u|) > 0 keep every layer positive and Jensen gives the linear lower bound, gives
log E e^{R Y} = O(k beta^(eps' - eta) + k beta^(2 eps')/M_j) -> 0. The tail steps: on {Y > R^(-1/2)},
e^{(p - R) Y} <= e^{-(R - p)/sqrt(R)}, and Holder with exponent 1 + delta_0 on e^X gives
<= beta^C e^{-sqrt(R)/p}(1 + o(1)) -> 0, since sqrt(R) = beta^((eps' - eps)/2) beats log beta. The set
{Y < -R^(-1/2)} is handled the same way with e^{-R Y}. E e^X >= 1. So log E e^{X+Y} = log E e^X + o(1). The centring
(3/4) k beta^eps cancels between 2 x (period one) and (period two), and the X-part is the Section 9 deletion.

**13.3 OPEN paragraph (L421). HOLDS as a summary.** e^(-J) = p(0)^2/Pi(0,0) by (26), so J < log(1651/1650) is
p(0)^2/Pi(0,0) > 1650/1651. A product spectator adds the same J_X at both ends: the signed integral is unchanged
and the cold value moves by J_X. Both remarks are correct. No counterexample and no gap is claimed.

## Step 6 result: Section 1, the effective seam (1), Sections 2-5, 8-9

**1.1 Set-up (L13-17). HOLDS.** With K_v unnormalized, d/dv[2 log Tr(B K_v) - log Tr(B K_v B K_v)]
= 2(2N w_1) - 2(2N w_2) = 4N(w_1 - w_2), and the z_v powers cancel. At v_0, row 1149 (20) gives
N(1+beta) v_0^2 = 1/log^2(2+n) -> 0. A relative e^(+-eps) change moves Tr(BK) by e^(+-eps) and Tr(BKBK) by
e^(+-2 eps), so J moves by <= 4 eps. The constant kernel gives J = 0. The status remark of 13.1 applies to "pending"
in L17.

**2.1 Expansion and radius of (1) (L21-34). HOLDS.** S_b is linear in each line's spins, and the line law is
invariant under g -> -g on that line, so E S_b = 0. Row 1149 (20)'s two-circle bound at t = +-u/d needs
u/d <= c/(1+beta), true for large n. That gives E e^{u|S_b|/d} <= 2C. The pairs form the edges of the 4-regular
transverse torus, so the conflict degree is 6 and a greedy 7-edge-colouring exists. Holder over colours, with
independence inside a colour, gives |E prod (e^{z S_b} - 1)| <= (C|z|d)^#pairs. The polymer identity
Z(V) = Z(V - b) + sum_{A containing b} w(A) Z(V - N[A]) is correct, since components of disjoint line sets factor.
|N[A]| <= 7k, which gives 2^{7k}. The induction gives |log Z| <= C n^2 on |z| <= c_1/d, for complex z. Flipping one
checkerboard class of lines (n even) makes Z even. Cauchy from degree four gives O(n^2 d^4 v^4)
= O(n^4 (1+beta)^2 v^4). The count 6^(2k): a depth-first walk of a spanning tree on k vertices has 2(k-1) moves.
Each move goes to one of at most 5 non-parent neighbours or back to the parent (6 neighbours at the root), so
there are at most 6^(2(k-1)) walks.

**2.2 Value of the cumulant (L36). HOLDS.** Different pairs: some line appears once, so the term is odd under that
line's flip and vanishes. A q-step stationary walk has E[g_k g'_l] = (a^q/4) delta_kl, since E u = a 1 by
conjugation invariance. The return arc of length >= n/2 has density 1 + O(e^{-cn/(1+beta)}) (row 1145 (1)).
X q Y^(-1) on R^4 is the (1/2,1/2) representation, with trace (2 w(X))(2 w(Y)). So
(v^2/2) * 2 * (a^{2q}/16) * 4 w_R(x) w_R(y) = (v^2/4) a^{2q} w_R(x) w_R(y). The diagonal 1/4 goes into c_j(v).
The range: v <= c_1/(2d) with d = sqrt(n(1+beta)). The o(1) claim needs v = o(1/(n sqrt(1+beta))), and then
N beta v^2 can still be ~ n. Correct.

**3.1 (2)-(3) (L41-58). HOLDS.** Poisson: E[(w_R(x) w_R(y))^{N_R}] = exp(t_R(w_R(x) w_R(y) - 1)). Sewing once and
twice gives z <1,B1> and <1,B1>^2 E G(f,f')^2, so e^(-J_rect) = E G(f,f')^2/z^2. Lower bound: the terms with f' empty
have u_{f'} = u_1 and give ||(1-P) u_f||^2; with the symmetric case this is 2 e^(-lambda) D. Upper bound:
<u_1, rho u_1> = E G(f,1)^2/z = 1 - D/z, and Tr rho^2 >= <u_1, rho u_1>^2. Also e^(-lambda) <= z <= 1, since
|f| <= 1 and G is a probability integral. lambda ~ N beta v^2 Sum_q a^(2q)/2 lies in a compact subset of (0, inf),
by row 1145 (1) and 1 - a <= C/beta. At v ~ (N beta)^(-1/2) = o(1/(n sqrt(beta))), (1) has error o(1).

**3.2 (4) (L60-66). HOLDS.** Tr(F_0^(n-q) V* F_c^q V) = sum_{i,j} lambda_i^n |<j,Vi>|^2 (lambda_j^c/lambda_i)^q. The
weights sum to one because V is an isometry (tr(U*U)/2 = 1). Jensen gives E w_R >= (E w_p)^q. The half-tilt
(row 1149 (16)) and Jensen give 1 - E w_p <= C/beta. Hence 1 - E w_R <= C q/beta.

**3.3 Limitation of equal-time control (L68). HOLDS.** G_0 and G_1 have the marginal mu. For G_1,
D = E Var_mu(f). The q links on one long side share no plaquette; each has at most 5 <= 6 staples at the open end.
Row 1145 (2) gives the product density in [1/2, 3/2] once eta(q/(1+6 beta)) <= 1/2, that is for q >= A(1+beta).
Then Var >= (1/2) Var_Haar(w) = 1/8. By (2) the cost stays >= c.

**3.4 Comparison rests (L70). HOLDS.** h(x) h(y) gives G_0. sum_A (h 1_A)(x)(h 1_A)(y)/mu(A) has marginal h and form
sum_A mu(f 1_A) mu(g 1_A)/mu(A) -> mu(fg) on continuous invariant f, g as the cells shrink. Both are positive
gauge-invariant kernels.

**4.1 Rods and the rod expansion (L75-84). HOLDS.** The rods are open walks (trees), so the zero-coupling seam is
identically one and has rank one. The rod graph Z_m x Z_n x Z_n has degree 6, and it is bipartite because m, n, n
are even. Grouped factors satisfy |e^{z S} - 1| <= e^{(s+1)|z|} - 1. The induction gives |log| <= C N/s on
|z| <= c/s, and Cauchy gives N s^3 v^4. Break bonds contribute only diagonal terms: each cross moment has a rod
that appears once.

**4.2 (6) (L86-93). HOLDS.** Rotating a spatial axis into time and using the half-coupling order (row 1149 (16)),
min-max and Schatten Holder give mu exp[(beta/2) sum_A a] <= C_0^|A|. With e^{a^2} - 1 <= C beta^(-2) e^{beta a/2}
(a <= 2), the product expansion gives (1 + C_1/beta^2)^N per orientation. Markov and a union bound then give (6).

**4.3 (7)-(9) (L95-112). HOLDS.** sum t w w = lambda - sum t D(x) - sum t D(y) + sum t D(x) D(y). |1 - U_R| <= sum of
the q plaquette distances, so D_R <= q sum a_p and D_R^2 <= q^3 sum a_p^2. With at most C s^2 rectangles per
plaquette, E <= (v^2/4) sum_R D_R(x) D_R(y) <= C v^2 s^5 N/beta^2 on the good set. The exceptional part is
<= C k e^{C' k Q - c N/beta^2}. At v_* = beta/(sqrt(N) log^3(2+beta)) and s ~ log beta: N s^5 v^2/beta^2 =
O(1/log beta), N s^3 v^4 -> 0, and Q = O(beta^2/log^5 beta) = o(N/beta^2). Also v_* <= c/s.

**4.4 Obstruction and (10) (L114-121). HOLDS.** There are >= c N s rectangles of length in [s/4, s/2] inside rods,
with eigenvalue a^(2q) a_v(2)^2 >= c v^2. So Tr K >= 1 + c N s v^2, and N s v_*^2 = s beta^2/log^6 beta -> infinity.
For 0 <= K <= I, 2 log Tr K - log Tr K^2 >= log Tr K. (10): at v = beta the break bonds restore the homogeneous
seam, so the endpoint is J_full, and the factor is 2(m n^2 + 2N).

**5.1 Fourier scales (12) (L132-137). HOLDS.** With r ~ z/sqrt(s) and z ~ z^2 e^(-z^2/2), E r^2 = 3/s.
1 - cos r ~ r^2/2 gives 3/(2s). 1 - (4 cos^2 r - 1)/3 = (4/3) sin^2 r gives 4/s. The ratio bound comes from
row 1145 (1).

**5.2 Integration against the rest, (13), parity sum and (11) (L139-153). HOLDS.** Marked links (i + y + z even) on
the two boundary slices share no plaquette. Each has 4 spatial staples plus 1 inward temporal staple (the seam is
removed), so s_e <= 5 beta. Integrating an inserted central variable multiplies the dimension-d part by a_{s_e}(d)
<= a_{5 beta}(d). Rail parts: odd d are even under a central flip and even d are odd. This gives 1 + O(b_3) and
O(b_2). In the sign average over a cyclic ladder only the all-even and all-odd gap patterns survive (each rung must
meet an even number of odd gaps). Exponents: b_2 = exp(-(3/2 + 3/10) h/beta) = n^(-9 gamma/5) and
b_3 = n^(-24 gamma/5). So K b_2^2 <= n^(3 - 18 gamma/5) -> 0 iff gamma > 5/6, and K b_3 -> 0. (11): K = m n^2/2 with
m = floor(n/h).

**5.3 Sharp exterior comparison and order count (L161-163). HOLDS.** With fixed rails, b_2 = a^h, which gives
K b_2^2 -> 0 iff gamma > 1. Consecutive full rungs give eigenvalues a^(2 h_i + 2), and K a^(2h+4) -> infinity for
gamma < 1. The order count: the spacings sum to <= 2 n^3, and Markov gives >= K'/2 spacings <= 4N/K'. Each gives an
eigenvalue >= exp(-C(1 + N/K')/beta) = n^(-o(1)) when K' >> N/(beta log n). So the trace diverges.

**8.1 (19)-(21) (L244-261). HOLDS.** Lower bound: Jensen and translation invariance give t |S_p| E a = |S_p| u p_V'(0).
Upper bound: chessboard trace Holder. For u <= 1/2 the marked layers stay positive (Wilson convolution at coupling
beta(1-u) >= 0, or a positive magnetic factor), so no parity condition is needed. Dissemination over four axes leaves
the uniform patterns with weights |S_p|/V and 1 - |S_p|/V. (19) follows from the two-sided moment and the exact
cancellation 2(3/4)|S|u - (3/4)(2|S|)u = 0. (20) needs eps < eta: |S| u^2 = beta^(2 eps)/|S| -> 0 and
|S| u beta^(-eta) = beta^(eps - eta) -> 0.

**8.2 (22a)-(22b) (L263-284). HOLDS.** g_b(u) - g_b(0) = -(3/(2 b^4)) log det(I - uH), with H between 0 and I. The
p-block trace of the curl projection is m_b/6 by the cube symmetries, where m_b = 3b^4 - 4b^3 + 1. So
g_b'(0) = m_b/(4b^4) = 3/4 + O(1/b), and |g_b''| <= (3/(2b^4)) Tr H^2/(1-|u|)^2 <= C. Convexity of p_V and the secant
squeeze give |p_V' - g_b'| <= C d with d^2 = Delta_b. With 2 eta < gamma, C(d + 1/b) = O(beta^(-eta)). The (22b)
steps repeat row 1143 (15)-(16) (checked by row 1144) with weights in [1/2, 3/2]. For mixed orientations, Holder with
exponent six needs 6u <= 1/4, which holds for u <= 1/48.

**8.3 Precision of the pressure argument (L286). HOLDS.** g_+-''(u) = 2 +- c (x e^(-x^2))''|_(x=u/d) > 0 for small c.
The sup error is O(d^2), and the slopes at zero differ by 2cd.

**9.1 Complete deletion, k <= c_* log(2 + beta) (L291, L319-321). HOLDS.** Truncation: E(e^X - F) <=
E e^{(1+delta_0) X} e^(-delta_0 H) <= e^{C_0 2k - delta_0 H}. Here sum c_p^2 r_p^2 <= 2X gives the Lipschitz bound
e^(2H) sqrt(H). With 2 kappa < gamma/2 the error of (24) is beta^(2 kappa - gamma/2) polylog -> 0. Translation
invariance gives E_W F(S) = E_W Y. Independent tilings on the two halves give the mean g^2 away from the cuts, with
exceptional fraction C(span + b + 1)/T -> 0. Since g >= 1, 2 log W_1 - log W_2 -> 0.

**9.2 (23) (L293-300). HOLDS.** Pairing odd and even layers gives positive L^(1/2) L_i L^(1/2), so trace Holder works
in the perpendicular direction. In-plane, the even side n makes Tr|F_i|^n = Tr F_i^n. Pointwise: five-face
telescoping and Cauchy-Schwarz give a_p <= 5 sum. At most 4 cubes contain a plaquette, with one even base each, so
M_0 <= 20 U_0. With delta_0 = 1/40: U_0 - M_0/40 >= U_0/2 >= (U_0 + M_0)/42. The pressure gap from beta/42 to beta is
(9/2) log 42 + o(1) per site (nine Gaussian coordinates per site).

**9.3 (24) (L302-317). HOLDS.** The density bound e^(C V Delta_b) relative to the product of open-box Wilson laws
survives marginalization and the box-by-box Markov map. Then the per-box factor 1 + e^(C' b^3) adds V/b <= V Delta_b.
Relative entropy is at most the log of the sup density. Maurey-Pisier interpolation gives pi^2 t^2 K_0^2/8, with
Lipschitz constant H_1 sqrt(l/V), since each radius is read by at most l translations. Donsker-Varadhan and
optimization in t give H_1 sqrt(l Delta_b). The chart probability is e^(C b^4 - c beta/(12 b^8)) by the half tilt
with Holder over six orientations, and beta/b^12 -> infinity.

**9.4 Scope of the deletion (L323). HOLDS.** It is the cold-end remark of 13.1.

## Step 7 result: the obstructions of Sections 6-7 and 10-12

**6.1 (15a) and the boundary data (L168-176). HOLDS.** In D the fixed rung links are (-1)^i. A marked link at
(i', y, z) has four staples equal to +beta. Only the staple across the matched line can hold a rung link, and so
equal -beta, and only when i' or i' + 1 is a mark. Gaps have length >= 2, so at most one staple is negative and
the strength is 5 beta or 3 beta, centred at one. Constants that depend on one environment cancel in the cross
ratio. Positive-probability neighbourhoods and continuity are as stated. The note claims no typicality.

**6.2 Evaluation (L178-189). HOLDS.** The d = 2 term of a normalized central density is 2 m_2 chi_2. So each rail
is 1 + 2 b_i chi_2 + O(u), with u/b^2 = n^(-6 gamma/5) -> 0. In AA and DD the rung arguments carry
x_rung y_rung^(-1) = 1. In AD and DA the substitution g'_i -> (-1)^i g'_i makes the rungs positive and reverses one
rail in each gap (factor (-1)^i (-1)^(i+1)). The even part is 1 + 4 eps b b' X_i + O(u). With g'_i = r_i g_i and
E rho_2(r) = a_beta(2) I, E X_i = a_beta(2)^2 E chi_2^2 = a_beta(2)^2 -> 1. The product lemma: log(1+Y) = Y + O(b^4);
Holder over at most three classes of disjoint rung pairs gives the upper bound, and Jensen the lower. So
log H_rs = 4 eps K b^2 (1 + o(1)), and the cross ratio is 4 x 4 K b^2 = 16 K b^2 = n^(3 - 18 gamma/5 + o(1)), which
diverges for gamma < 5/6.

**7.1 (16) set-up and (17) identity (L194-214). HOLDS.** C^(1/2) M (MCM)^(T-1) M C^(1/2) = (C^(1/2) M^2 C^(1/2))^T
= L_e^T. Since sum_eta s^eta Q_eta = U_s, sum_{eta,xi} s^(eta+xi) ||Q_eta rho Q_xi||^2 = Tr(rho U_s rho U_s).
Non-negativity: this is ||L^(T/2) U_s L^(T/2)||_HS^2.

**7.2 Bad endpoints (L216-221). HOLDS.** In Tr prod (U_i A D_i A*), Holder gives
(Tr(A D A*)^k/Tr L^k)^(1/k) = P_k(D on all slices)^(1/k). A mixed term with D_y and (1 - D_x) is bounded the same way,
since A(1 - D)A* <= AA*. At least k m/4 of the k m candidates are bad, and two thirds of these share a direction. The
half tilt gives (C e^(-beta/64))^l for l faces with a > 1/32. Then 3 * 2^(km) (C e^(-beta/64))^(km/6) has k-th root
<= e^(-c_1 beta m).

**7.3 Good endpoints (L223). HOLDS.** sqrt(2a) <= 1/4 at both ends. With sign product -1, the four seam distances sum
to >= 2 - 1/2 = 3/2. With bounded incidence the seam action is >= c_2 m. The seam operator becomes
C^(1/2) H C^(1/2), with multipliers a_(beta/2)(d)/a_beta(d) <= 1 (row 1149 (16)). The insertion U_1 H sits between A*
and A, so the trace is bounded by Tr L^k. The position integrand is pointwise >= 0, so dropping the good-set
indicator is an upper bound. A flat s is a gradient times a global centre flip that commutes with L, and U_s^2 = 1,
which gives exactly one.

**7.4 Counting and (16) (L225-231). HOLDS.** The flat fields number 2^(N-1) x 8, so the image has 2^(2N-2) elements.
pi-hat is constant on curl classes because the flat factor commutes with L and squares to one. The cycle space has
dimension 3N - (N-1) = 2N + 1 and the boundary space 2N - 2. Plaquette boundaries and three windings span the
cycles. Martingale ranges: 4 per plaquette bit and n per winding, so the sum of squared ranges is 16 x 3N + 3 n^2.
Hoeffding (row 1147 L217) then gives (16). The zero-homology remark is correct: a global centre flip commutes with
rho, so sum over a winding of delta is 0.

**7.5 (18) (L233-239). HOLDS.** E_s s^(eta+xi) = e^(-tau |delta|/N), and the diagonal blocks are unchanged, so
Tr rho_tau = 1 and Tr rho_tau^2 = Tr rho^2 E_pi e^(-2 tau |delta|/N) -> Tr rho^2 e^(-3 tau) by (16) with b = 0. One-period
traces with any normalized electric seam are unchanged, since such seams commute with U_s. Taking
tau > log(1651/1650)/3 gives J_tau >= 3 tau + o(1).

**10.1 (25) (L328-336). HOLDS.** The moments of a uniform point of S^3 are pairings divided by 4 x 6 x ... x (2r+2).
The real trace of the rotations around a strand is 4 w_l(x) w_l(y). The coefficients are positive and their total is
K(1,1) < infinity.

**10.2 (26) (L338-342). HOLDS.** Tr(BK) = K(1,1) <1,B1> z and Tr(BKBK) = K(1,1)^2 <1,B1>^2 Z_2. Also
p(0) = q(0)/z and Pi(0,0) = q(0)^2/Z_2, so p(0)^2/Pi(0,0) = Z_2/z^2 = e^(-J).

**10.3 Why the dilute test stops (L344). HOLDS.** The parity law of Pi is pi: with C_eta = Q_eta C Q_eta,
||Q_eta rho Q_xi||^2 = Tr(B C_eta B C_xi)/Z^2. So Pi(0,0) <= pi(delta = 0) <= 2^(-2N+o(N)), and p(0) <= max_eta p_eta
(row 1149 (18)). Under B_tau, G_tau(f_w, f_w) = G(f_w, f_w), so p is unchanged, and G_tau(f, f') = e^(-tau|delta|/N) G(f, f').

**10.4 Opposite sides (L346). HOLDS.** For B_inf = |M psi><M psi|, G(f, f')^2 = G(f, f) G(f', f'), so Pi = p x p and
J = 0. Conditional on eta, xi has density e^(o(N)) relative to the uniform cycle law (row 1149 (18) against mass
2^(-(2N+1))). So (16) holds and J_tau -> 3 tau.

**10.5 Resummed rectangles (L348-352). HOLDS.** For central y the seam argument x_e (g y_e g'^(-1))^(-1) loses y_e
when x = y, so K(y,y) = K(x,x). In K(x,y) each of the N frustrated 23-plaquettes has product -1 for every gauge.
That forces seam action >= cN, while the ball restriction costs only C N log(2+beta) in K(x,x). Every kernel
f(x) f(y) Phi(rectangle data) has cross ratio one at this pair, since x and y have the same rectangle data.

**10.6 Limit of Section 9 (L354). HOLDS.** Jensen and (22a) give log moment >= (3/4 - o(1)) k, while the clipped test
has log moment <= H, so clipping loses order k if H = o(k). The (24) error is about e^(2H) sqrt(H k) beta^(-gamma/2),
which vanishes only if H <= (gamma/4 - c) log beta. So this route needs k = O(log beta), as stated.

**11.1 Perimeter bound along the path (L359-361). HOLDS.** The endpoint plaquettes stay at beta, so the bad-end
bound is e^(-c beta m). |Tr(R_D U_s R U_s)| <= ||R_D||_HS ||R||_HS. The ratio of squared norms is
Tr(K D B K B D)/Tr(K B K B) <= P(bad end). On good ends every seam coupling is >= v, which gives e^(-c v m), and
z_(v/2)/z_v <= C for v >= v_c.

**11.2 Seam sign perturbation (L363-367). HOLDS.** Both sums are >= 1 (the empty mask, and non-negative position
integrals) and <= (sum_s lambda^|s| e^(-c v m(s)/2))^(1 or 2). So |Delta J| <= 2 log of that sum. In each of the
2n^2 rows every sign change frustrates its own (1,j)-plaquette, and a run costs e^(-c v) lambda^l. Hence the row
weight is <= exp(n e^(-c v) lambda/(1 - lambda)) + lambda^n, and the product -> 1 when N r e^(-c_1 v) -> 0 and r <= 1/4.

**11.3 Missing channel (L369). HOLDS.** The averaged sign multiplies the dimension-d multiplier by
1 - r + r(-1)^(d-1). Odd d are unchanged. a_v(3) = (I_2/I_1)(I_3/I_2) is strictly increasing in v.

**12.1 One-face covariance (L389). HOLDS.** Periodic: the rank is 4b^4 - (b^4 - 1) - 4 = 3b^4 - 3 over 6b^4 faces,
so the diagonal is (1 - b^(-4))/2. The two curl images share the span of the interior columns. Each projection
differs from that span's projection by rank O(b^3) and norm <= 1. So ||P_open - P_per||_HS^2 = O(b^3), and the mean
squared diagonal difference is O(1/b) per orientation.

**12.2 Finite marked faces and Laplace moments (L391). HOLDS.** Faces at distance > b lie in distinct tiles,
independent under the array. Holder and the half tilt bound E exp(2 sum t_i beta a) for t_i < 1/32. Also
E e^(t|Z|^2/4) = (1 - t/2)^(-3/2).

**12.3 Coupling variation and the multiplier ratio (L393-400). HOLDS.** e^(-lambda beta a)/z_(lambda beta)
= (e^(-beta a)/z_beta) e^((1 - lambda) beta a) z_beta/z_(lambda beta). z_beta/z_(lambda beta) -> lambda^(3/2), and
lambda^(3/2)((1 + lambda)/2)^(-3/2) = (2 lambda/(1 + lambda))^(3/2). The Gaussian Fourier limit holds at bounded
d/sqrt(beta). Monotone decrease in d beyond that holds because R_d(lambda beta)/R_d(beta) <= 1.

**12.4 (27) (L374-387, L402). HOLDS.** With lambda = 1/(1+x), 2 lambda/(1 + lambda) = (1 + x/2)^(-1). The tail bound
P(S > R) <= E(1 - e^(-xS))/(1 - e^(-xR)), uniqueness by analytic continuation, and E e^(-x|Z|^2/4) = (1 + x/2)^(-3/2)
give D/sqrt(beta) -> |Z|/sqrt 2. The second-moment argument uses the O(b^3/N) close pairs. nu has no atoms.

**12.5 Brownian representation (L404). HOLDS.** e^(X.y - s/2) is a martingale, bounded by e^beta up to tau. Optional
stopping gives E[e^(-tau/2) e^(beta w'.y)] = e^(v w.y), so C_v = Q_(v,beta) C_beta for 0 <= v < beta.

**12.6 Noise needed (L406). HOLDS.** On a band a <= d/sqrt(beta) <= b_0 the ratio is
<= e^(-(1/lambda - 1) a^2/2) + o(1) < 1. ||(1 - r) I + r E rho(R) - I|| <= 2r. B_tau tilts the finer
(l, l') law by the same e^(-2 tau |delta|/N), so its density -> 1 in L^1.

## Step 8. Verdict table and result

Scope remarks (not corrections).
(a) (28), (10) and (14) are exact restatements of (15), and so of (W) through rows 1145 and 720. They carry no
estimate of their own.
(b) (29) is a density bound. The right side C_sigma n^3 beta^(-sigma) diverges on the physical sequence, as the note
says (L458, L514). (29), (31)-(35) and the deletions of Sections 9 and 16-17 are not selective in the sense of the
brief, Section 4. Their proofs use positivity, the continuous identity chart and the open-box Gaussian comparison.
None of these separates SU(2) from compact U(1) at weak coupling. The note does not claim otherwise (L421).
(c) Status: L3, L17 and L417 call row 1149 unchecked or pending at the pin. Its check, row 1150, now finds all 66
statements HOLD. This changes no conclusion.
(d) Wording: L492, "(28) holds with A_j = D'_j minus S_j", means that (15) is equivalent to (28) for this A_j. The
inequality (28) itself stays OPEN.

Not checked: the GUIDE paragraphs L3 and L5 (repo search and credits), beyond (c). I did not open the external
source lines they cite (Sussman-Alpoge outline and CA-I at `31a47c543775`). They are not load-bearing for any
PROVED step here.

| # | Statement (line in `gap-solve5-astra62.md`) | Verdict |
|---|---|---|
| 1 | (29), statement and scope (L425-430) | HOLDS |
| 2 | Short time: Phi convex, 2 Phi(q) - Phi(2q) non-increasing, J <= psi(m), normalizers cancel, tiling (L432) | HOLDS |
| 3 | One temporal holonomy per box: spanning tree, Z(h) = Tr(T^s U_h), 0 <= Z(h) <= Z(1) (L434) | HOLDS |
| 4 | (30), upper inequality: chains <= 3(b+1), c b^(-5) <= d*d <= 24, chart and Taylor errors (L436-441) | HOLDS |
| 5 | (30), lower inequality: forest gauge, restrictions, Schur complement, precision factor (L443) | HOLDS |
| 6 | Exact Gaussian cancellation into the mode sum (L445-450) | HOLDS (GUIDE run agrees to 10 digits) |
| 7 | Mode sum <= C (b/m)^3 per box; J/N <= C(m^(-3) + m log(2+beta)/b); choice of m; sigma < 1/16 (L452-456) | HOLDS |
| 8 | The short-time comparison is >= c (b/m)^3 per box (L458) | HOLDS |
| 9 | (31), second clause, mu_* = 2^(3/2) (L462-469) | HOLDS |
| 10 | Spatial dissemination of e^(s g_p) (L471) | HOLDS |
| 11 | Time folding and (32) (L473-478) | HOLDS |
| 12 | (33) (L480-486) | HOLDS |
| 13 | Mean of the source and (31) by exponential Markov (L488) | HOLDS |
| 14 | Section 16 statement, count P, S_j (L492) | HOLDS (wording remark d) |
| 15 | (34) (L494-499) | HOLDS |
| 16 | (35), bad event (L500-504) | HOLDS |
| 17 | (35), good event, lower and upper bounds (L506) | HOLDS |
| 18 | Signed normalizers, convergence in probability (L508) | HOLDS |
| 19 | Simultaneous terminal interval and the deterministic S_j (L510) | HOLDS |
| 20 | Absolute accuracy of the sampling argument (L512) | HOLDS |
| 21 | OPEN paragraph (L514) | HOLDS |
| 22 | Section 17 statement and the finer class (L518) | HOLDS |
| 23 | (23) for delta < 2/3: dissemination with four parities, factor 16 (L520) | HOLDS |
| 24 | M_0 <= (3/2) U_0 and the pressure bound (L522) | HOLDS |
| 25 | Choice of exponents, alpha < 1/80 (L524-530) | HOLDS |
| 26 | Limitation of the first and second moment data (L532) | HOLDS |
| 27 | (28) equivalent to (15), cold end (L411-417) | HOLDS (status remark c) |
| 28 | Hot end with both changes (L419) | HOLDS |
| 29 | OPEN paragraph (L421) | HOLDS |
| 30 | Section 1: J(v), 4N(w_1 - w_2), v_0, the 4 eps rule, rank one (L13-17) | HOLDS |
| 31 | (1): exponential moment, seven-colour Holder, deletion induction, evenness, radius (L21-34) | HOLDS |
| 32 | (1): value of the cumulant (L36) | HOLDS |
| 33 | (2) and (3) (L41-58) | HOLDS |
| 34 | (4) (L60-66) | HOLDS |
| 35 | Limitation of equal-time control, Var >= 1/8 (L68) | HOLDS |
| 36 | Comparison rests (L70) | HOLDS |
| 37 | Rod geometry, rank-one seam, rod expansion O(N s^3 v^4) (L75-84) | HOLDS |
| 38 | (6) (L86-93) | HOLDS |
| 39 | (7)-(8) (L95-105) | HOLDS |
| 40 | (9) and (5) (L107-112) | HOLDS |
| 41 | Tr K^rod >= 1 + c N s v^2; stand-alone ratio diverges (L114) | HOLDS |
| 42 | (10) (L116-121) | HOLDS |
| 43 | (11), statement (L126-130) | HOLDS |
| 44 | (12) and the ratio bound (L132-137) | HOLDS |
| 45 | Integration against the rest, marked links, (13), parity parts (L139-147) | HOLDS |
| 46 | Parity sum over rungs (L149) | HOLDS |
| 47 | Exponents for gamma > 5/6, and (14) (L151-159) | HOLDS |
| 48 | Sharp comparison with an arbitrary exterior (L161) | HOLDS |
| 49 | Order count with unbroken rails (L163) | HOLDS |
| 50 | (15a) and the boundary data A, D (L168-176) | HOLDS |
| 51 | Evaluation of log H_rs = 4 eps K b^2 (1 + o(1)) (L178-189) | HOLDS |
| 52 | (16)-(17): definitions and the Fourier identity (L194-214) | HOLDS |
| 53 | Bad endpoints in a twisted trace (L216-221) | HOLDS |
| 54 | Good endpoints; (17) (L223) | HOLDS |
| 55 | Counting and concentration; (16) (L225-231) | HOLDS |
| 56 | (18) (L233-239) | HOLDS |
| 57 | (19)-(20) (L244-253) | HOLDS |
| 58 | (21) (L255-261) | HOLDS |
| 59 | (22a)-(22b) (L263-276) | HOLDS |
| 60 | General marked set and the cancellation (L278-284) | HOLDS |
| 61 | Precision of the pressure argument (L286) | HOLDS |
| 62 | Complete deletion of k <= c_* log(2 + beta) faces (L291) | HOLDS |
| 63 | (23) (L293-300) | HOLDS |
| 64 | (24) (L302-317) | HOLDS |
| 65 | One versus two periods (L319-321) | HOLDS |
| 66 | Scope of the deletion (L323) | HOLDS |
| 67 | (25) (L328-336) | HOLDS |
| 68 | (26) (L338-342) | HOLDS |
| 69 | Why the dilute test stops (L344) | HOLDS |
| 70 | Comparison on opposite sides (L346) | HOLDS |
| 71 | Obstruction after resumming the longitudinal rectangles (L348-352) | HOLDS |
| 72 | Limit of the local comparison of Section 9 (L354) | HOLDS |
| 73 | Perimeter bound along the one-step path (L359-361) | HOLDS |
| 74 | Seam sign perturbation (L363-367) | HOLDS |
| 75 | Missing dimension-three channel (L369) | HOLDS |
| 76 | Full-endpoint dimension law and (27), statement (L374-387) | HOLDS |
| 77 | One-face covariance of the reference (L389) | HOLDS |
| 78 | Finite marked temporal faces, Laplace moments (L391) | HOLDS |
| 79 | Reading dimensions by varying a coupling (L393) | HOLDS |
| 80 | a_(lambda beta)(d)/a_beta(d) limit, uniform in d (L395-400) | HOLDS |
| 81 | Joint dimension law, empirical law, (27) (L402) | HOLDS |
| 82 | Brownian representation C_v = Q_(v,beta) C_beta (L404) | HOLDS |
| 83 | How much noise is needed (L406) | HOLDS |
| 84 | Plan summary (L9) | HOLDS |
| 85 | RESULT line (L534) | HOLDS |

No statement FAILS. No correction is needed. There are four remarks (a)-(d) on scope, status and wording. None
changes a conclusion. The file claims no mass gap, and neither does this check.

RESULT: HOLDS — check of row 1151 (`library/gap-solve5-astra62.md`), checked line by line by hand by Claude Opus 5.5
(max effort), positive claims first.
- The whole-endpoint bound (29), 0 <= J <= C_sigma n^3 beta^(-sigma) for 0 < sigma < 1/16, HOLDS. This covers the
  short-time convexity, the box holonomy positivity 0 <= Z(h) <= Z(1), the Gaussian comparison (30), its exact
  cancellation into 3 sum log[(1 + e^(-m w))/(1 - e^(-m w))] (a GUIDE run agrees to 10 digits) and the mode sum.
- The deletion results HOLD: (31)-(35), the spatial dissemination and time folding (32), (33), the four-parity
  moment (delta < 2/3), and the exponents alpha < 1/20480 and alpha < 1/80.
- The equivalence (28) HOLDS, and so do the effective seam (1), (2)-(14), (19)-(24) and every obstruction:
  (15a), (16)-(18), (25)-(27) and Sections 10-12.
- 85 statements; 0 FAILS; 0 corrections; four remarks. Among them: row 1149 is now checked (row 1150), and (29) is
  a non-selective density bound whose right side diverges.
- The strict bound in (15), (W) and the four-dimensional SU(2) mass gap stay OPEN.
