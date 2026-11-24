lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-25T03:38Z

# gap-k2-signed-readout-fable (queue row 1479)

Status: IN PROGRESS. Started 2026-11-24T15:38Z (date -u). Pinned at commit 490b37e88.

## 0. Plan

Item: the signed one-step readout of the block map Q2, i.e. statement (DR): for a fixed strength
ratio a and an analytic family of centres containing the SU(2) Wilson input at large x, enclose the
one-step transverse Hessian coefficient b(Phi) (decrement x - x') with explicit error, or exhibit an
admissible centre with nonpositive limiting decrement.

Steps (each is appended here when done):

1. Read the sources the row names: `library/gap-k2-tool-design-fable.md` 3.2, 4.3-4.4;
   `library/gap-k2-t1-small-field-astra62.md`; Proposition GA; row 1472's record. Fix the exact
   definitions of Q2, x, x', b(Phi), "admissible centre", (DR).
2. Write the one-step formula for x' as an exact expression (saddle + Gaussian one-loop +
   remainder) and isolate the non-abelian terms using Proposition GA.
3. Evaluate or enclose the limiting decrement b; compare with (11/(3 pi^2)) log 2 = 0.2575.
4. Remainder bound K/x, or the obstruction; verdict on (DR).
5. Next two rows with decisive outcomes.

Nothing below this line is established until its step is written.

## 1. Repo search and sources (step 1, done 2026-11-24T15:46Z)

Read in full: row 1479; `gap-k2-tool-design-fable.md` 3.1 to 5.4 (map Q2, Lemma TW, (K2-STEP), Proposition
GA, filter); `gap-k2-t1-small-field-astra62.md` (row 1472); the RESULT of row 1472.

Greps (library/open-core.md, library/gap-k2-*.md, gap-rg-*.md, signed-cut.md, FINISH rows) for
`perfect action|Hasenfratz|Niedermayer|tadpole|classical image|fixed-point action`: no match for the
statements of Sections 3 to 6 below. Nearest matches:

- Row 1465 (check of row 1461): "the literal form is a tadpole fact, dead as a gap mechanism (not
  selective)". This is about a different one-step statement (a plaquette margin). Section 6 below finds the
  same failure of selectivity for the first-step decrement of Q2.
- Check 1469 (`gap-k2-tool-design-check-astra62.md` line 88): "GA gives no interacting one-loop coefficient
  for Q2". So the coefficient is not on file.
- Row 1472's file, last section: the readout row must "control the chosen centre's increment for Q2 or prove
  a strict lower bound directly"; RF10 of the outline allows a bounded cumulative finite part.

Memory: `memory_pressure` gave 37 percent free at 15:38Z and at 15:46Z. That is below the 50 percent rule. So
no numeric job was started, and every step below is by hand. Section 7 specifies the computation that is
left.

Credit. The block map Q2 is a small-side form of the normalized contour kernel of Ethan Sussman and Levent
Alpoge (with Claude and Codex). The small-field and large-field scheme and the one-loop law are Tadeusz
Balaban's. The classical saddle-point form of a block step with a kernel strength proportional to the
coupling is the "classically perfect action" construction of P. Hasenfratz and F. Niedermayer (Nucl. Phys. B
414 (1994) 785; recalled, not re-read here). Rows 1468 to 1472 supplied the map, Proposition GA, and the
question.

## 2. Setting and notation (step 1)

Quaternion notation. A link is a unit quaternion W = exp(A), A an imaginary quaternion, abs(A) the angle. For
a plaquette p, s_p = 1 - Re W_p = 1 - cos(angle of W_p). To second order s_p = abs((dA)_p)^2 / 2.

A **shape** is a gauge-invariant smooth function S of the fine field that is a sum of local terms, with
minimum 0 exactly on the gauge orbit of W = 1 (on the periodic torus: on the flat fields), and with Hessian at
W = 1 equal to the curl form sum_p abs((dA)_p)^2. So the centre x S has readout x. The Wilson shape is
S_W = sum_p s_p. The plaquette family is S_f = sum_p f(s_p), f analytic near [0, 2], f(0) = 0, f'(0) = 1,
f > 0 on (0, 2]. Put gamma = f''(0)/2, and S_gamma for f(s) = s + gamma s^2.

Remark FA (the plaquette family holds the fundamental-adjoint plane). 1 - (1/3) tr_adj(W_p)
= (4/3)(1 - (Re W_p)^2) = (4/3)(2 s_p - s_p^2). So beta_F s_p + beta_A (1 - tr_adj/3) = x (s_p + gamma s_p^2)
with x = beta_F + (8/3) beta_A and gamma = -(4/3) beta_A / x. Positive adjoint coupling is gamma < 0.

The kernel. Zc(t) = integral of exp(t Re g) dg = 2 I_1(t)/t, and Zc(t) = sqrt(2/pi) t^(-3/2) e^t (1 + O(1/t)).
So with kappa = a x

    K(W, V) = prod_c exp(-a x T_c(W, V)) (a x abs(M_c(W)))^(3/2) sqrt(pi/2) (1 + O(1/(x abs(M_c)))),
    T_c(W, V) = abs(M_c(W)) - Re(M_c(W) V(c)^(-1)) >= 0.

T_c vanishes exactly when V(c) = M_c/abs(M_c). To second order at W = 1, V = exp(B): T_c = abs((QA)(c) - B(c))^2 / 2,
Q the linear contour mean of Proposition GA. (The variance of the 384 contour angles cancels between abs(M_c)
and Re M_c. PROVED: M = m_0 + m with m_0 = 1 - mean(abs(theta_e)^2)/2, m = mean(theta_e) to second order, and
abs(M) - m_0 = abs(m)^2/2 to second order.)

The total energy is E(W, V) = S(W) + a T(W, V), T = sum_c T_c. The image is
F_x(V) = -log (Q2_(ax) e^(-xS))(V).

## 3. The form of one step at large x (step 2)

**Proposition L (Laplace form of a step; PROVED on a fixed finite torus, as x tends to infinity; the
uniformity in the torus is NOT proved here and is the content of row 1480).** Fix an even periodic torus, a
shape S and a > 0. For V in a neighbourhood of 1 (depending on the torus),

    F_x(V) = x (R_a S)(V) + Psi_S(V) + c(x) + O(1/x),   with all V-derivatives,
    (R_a S)(V) = min over W of E(W, V),
    Psi_S(V) = (1/2) log det Hess_W E (W_*(V), V) - (3/2) sum_c log abs(M_c(W_*(V))).

Here W_*(V) is the minimizer in the block tree gauge (the 15 tree links of each block equal to 1; the
Jacobian of this gauge is 1 by Haar invariance, as in row 1472's file), and the Hessian is taken in the
coordinates W = W_* exp(a_l) on the other links.

Proof. In the tree gauge the minimizer at V = 1 is W = 1 and it is unique: S = 0 forces a flat field, T = 0
forces M_c = 1 for all c, hence all 384 contours of every bond equal to 1; a flat field with all contours
trivial is a gauge transform that is constant on base points, and the tree gauge leaves the global constant,
under which E is invariant only jointly with V. The Hessian at (1, 1) is d^T d + a Q^T Q on tree-gauge
fields. Its kernel is zero: dA = 0 and QA = 0 give A = d lambda with d'(lambda at base points) = 0, so lambda
is constant on base points, and the tree gauge then gives lambda constant. So the minimum is nondegenerate, it
persists for V near 1 by the implicit function theorem, and Laplace's method on the compact manifold gives the
expansion; the Riemannian Hessian at a critical point is the coordinate Hessian in exponential coordinates
centred at the point, and the Haar density is the Riemannian volume. The factor abs(M_c)^(3/2) is the
prefactor of the kernel. QED

**Corollary L1 (the leading image is not of Wilson form). PROVED (same domain).** The image of the centre x S
is x R_a S + O(1). R_a S is the classical block image (the saddle-point map of Hasenfratz and Niedermayer). Its
Hessian at V = 1 is (1/a + Q (d^T d)^(-1) Q^T)^(-1) on transverse fields (Proposition GA), which is at most a
at every momentum. The Wilson Hessian symbol reaches 16. So for a < 16, R_a S_W is not a Wilson shape, and the
difference x (R_a S_W - S_W) is of order x times the local action. In the norm of 4.2 of the design note
(divide by 1 + theta x E_X) this difference does not tend to 0 as x grows: it is of order 1/theta. SKETCHED
(the last sentence; no constant computed).

Consequence for (K2-STEP). The centres of the chain cannot be Wilson shapes x_k S_W with a small radius. The
natural centres are x_k S_k with S_k = R_a^k S_W, the classical orbit, plus the one-loop term. The readout row
is then a statement about b(S_k; a) for all k, not about b(S_W; a) alone.

**Corollary L2 (classical marginality, nonlinear form of GA). PROVED (same domain).** The readout of
x R_a S is x. (The Hessian of R_a S at V = 1 is the Schur complement of the Hessian of E, which is the
Gaussian model of Proposition GA with the curl form.) So

    x' = x - b(S; a) + O(1/x),   b(S; a) = - (transverse k^2 coefficient of the Hessian of Psi_S at V = 1).

b is the **limiting decrement**. It is a finite lattice sum on a torus. It is not universal: it depends on
S and on a. Only its sum along an orbit has the universal part (11/(3 pi^2)) log 2 per step (RF10 of the
outline; SKETCHED here: k steps make a block map of side 2^k, and the one-loop coefficient of a block of side
L is (11/(3 pi^2)) log L + O(1)).

**Lemma AB (abelian backgrounds suffice). PROVED.** The Hessian of Psi_S at V = 1 is a multiple of the
identity in colour. For B = beta k (one colour direction k), the second-order part of Psi_S is the second-order
part of Psi_S evaluated at W = exp(k Abar beta), V = exp(k beta), where Abar = a (d^T d + a Q^T Q)^(-1) Q^T is the
linear minimizer. Proof. Colour covariance gives the first claim. The exact minimizer is
exp(k Abar beta) corrected at order beta^2 or higher (in fact beta^3, by the symmetry beta to -beta composed
with a colour rotation by pi about an axis orthogonal to k). The first derivative of the gauge-invariant
function Psi at (1, 1) in any direction is zero by the same rotation. So the correction enters at order
beta^3. QED

For a transverse coarse plane wave of momentum p tending to 0, Abar beta is smooth to leading order: its
components at the alias momenta p/2 + pi m, m not 0, are O(p^2 abs(beta)), because the pin force
a(beta - Q Abar beta) equals the image Hessian applied to beta, which is O(p^2). Its curvature is O(p^2) at
the aliases against O(p) at m = 0. So to leading order each fine plaquette of orientation (mu, nu) carries
the angle f_(mu nu) = (coarse plaquette angle)/4. PROVED (from Proposition GA's symbol bounds).

## 4. The slope of the decrement in the quartic coefficient (step 3; the main proved statement)

Notation. H_0 = d^T d + a Q^T Q on tree-gauge fields (one colour). For a fine plaquette p put

    g_p(a) = the (p, p) entry of d H_0^(-1) d^T
           = x times the variance of one colour of (dA)_p under the weight exp(-(x/2) <A, H_0 A>).

g_p has period 2 in every direction. gbar(a) is its mean over the 96 plaquettes of a block.

**Lemma G (the pinned plaquette variance). PROVED.** For every a > 0: 15/32 <= gbar(a) <= 1/2, and the mean of
g_p over the 16 plaquettes of one orientation in a block is gbar for each of the six orientations.

Proof. Work on a torus with N fine sites, then let N grow (g_p is the limit, by the gap of H_0 on a torus;
the bounds below are uniform). Without the pin, d (d^T d)^+ d^T is the orthogonal projector P on exact
2-forms. Its rank is 4N - (N - 1) - 4 = 3N - 3, and by symmetry its diagonal is (3N - 3)/(6N) < 1/2. With the
pin, minimise first over the gauge part of A: this replaces Q by Pi' Q, Pi' the projector on the
orthocomplement of the coarse gradients, of rank 4N/16 - (N/16 - 1) = 3N/16 + 1. So H_0 is d^T d plus a
positive form of rank at most 3N/16 + 1 on transverse fields (plus the four harmonic directions). By the
Woodbury formula d H_0^(-1) d^T = P - R with 0 <= R <= P and rank R <= 3N/16 + 5. So
0 <= trace(P) - sum_p g_p <= 3N/16 + 5, and the mean of g_p over the 6N plaquettes lies between
15/32 - 2/N and 1/2. Q2 with corner bases is covariant under the 24 permutations of the axes that fix the
corner. They permute the six orientations transitively. QED

**Theorem SL (slope). PROVED given Proposition L (so: on every fixed finite torus; in infinite volume given
the uniformity that row 1480 is to supply).** For the plaquette family of Section 2 and every a > 0,

    b(S_f; a) = b(S_W; a) - 5 gamma gbar(a),   gamma = f''(0)/2,   75/32 <= 5 gbar(a) <= 5/2.

Only f''(0) enters. In particular b(S_gamma; a) is affine and strictly decreasing in gamma.

Proof. By Lemma AB take B = beta k and the background W = exp(k Abar beta), with plaquette angles
Phi_p = phi_p k, phi_p = (d Abar beta)_p.
(1) R_a S_f. f(s) - s = gamma s^2 + O(s^3) is of fourth order in the field. So the Hessian of R_a S_f at V = 1
is that of R_a S_W, and the minimizer changes at order beta^3 only.
(2) The normalisation term of Psi depends on W_* only: no change at order beta^2.
(3) The determinant. Write the plaquette angle as Theta_p = Phi_p + (da)_p + O(beta a) + O(a^2). Then
gamma s_p^2 = gamma abs(Theta_p)^4/4 + O(6). Its second variation in a is
gamma (abs(Theta)^2 abs(d Theta)^2 + 2 (Theta . d Theta)^2 + abs(Theta)^2 Theta . d^2 Theta). At the
background the first two terms are gamma (phi_p^2 abs((da)_p)^2 + 2 phi_p^2 ((da)_p^k)^2) + O(beta^3), and the
third is O(beta^3). So Hess E changes by a term H_gamma of order beta^2, and has no change of order beta.
Therefore the change of (1/2) log det at order beta^2 is exactly (1/2) trace(H_0^(-1) H_gamma) (the
second-order term in H_gamma is of order beta^4; the cross term with the order-beta part of the Wilson
Hessian is of order beta^3). With three colours of variance g_p each:

    (1/2) trace(H_0^(-1) H_gamma) = (gamma/2) sum_p phi_p^2 (3 g_p + 2 g_p) = (5 gamma/2) sum_p g_p phi_p^2.

(4) The k^2 coefficient. For a transverse plane wave with p tending to 0, phi_p is f_(mu nu) on every fine
plaquette of orientation (mu, nu), to leading order (end of Section 3). By Lemma G,
sum_p g_p phi_p^2 = gbar sum_p phi_p^2 (1 + O(p)). The leading term of the image is (x/2) sum_p phi_p^2 with
readout x. So the readout of the change is + 5 gamma gbar, and b changes by - 5 gamma gbar.
(5) Terms of f beyond s^2 are of sixth order in the field. They change Hess E at order beta^4. QED

Check against the literature (recalled, unchecked): with all steps taken (gbar replaced by the unpinned
value 1/2) the shift of the effective coupling is (5/2) gamma. With gamma = -(4/3) beta_A/x and the one-loop
rate 11/(3 pi^2) per unit of log scale this is a change of log Lambda by (5 pi^2/11)(2 beta_A/x). The factor
5 pi^2/11 is the known one of the SU(2) fundamental-adjoint Lambda ratio (Gonzalez-Arroyo and Korthals
Altes 1982; Bhanot and Dashen 1982). So the slope has the right value in the limit where it is known.

**Corollary SL1 (the second outcome of the row holds for the plaquette family). PROVED given Proposition L.**
For every a > 0 put gamma_0(a) = max(0, b(S_W; a)) / (5 gbar(a)). Every centre x S_gamma with
gamma >= gamma_0(a) has limiting decrement b <= 0. These centres are positive, analytic, single-plaquette and
gauge invariant, with f increasing on [0, 2], and they are fundamental-adjoint Wilson actions with
beta_A = -(3/4) gamma x <= 0 (Remark FA), on the side of the plane away from the first-order line of (C5). So
uniform strict drift (DR) fails on every family that contains {x S_gamma : 0 <= gamma <= gamma_0(a)}. If
b(S_W; a) <= 0 the Wilson centre itself is the example.

**Corollary SL2 (the first outcome is a statement about a slab).** If b(S_W; a) >= b_W > 0 then
b(S_gamma; a) >= b_min on gamma <= (b_W - b_min)/(5/2), and nowhere beyond
gamma = (b_W' - b_min)/(75/32), b_W' an upper bound of b(S_W; a). With the GUIDE value b_W about 0.26 and
b_min = 0.13 the slab is gamma <= 0.05, that is beta_A >= -0.04 x. PROVED as an implication.

**Corollary SL3 (a lower bound on the readout error K of a tube). PROVED given Proposition L.** A centre with
a fixed adjoint coupling beta_A (not growing with x) has gamma = -(4/3) beta_A/x. Its decrement differs from
the Wilson one by (20/3) gbar beta_A / x. So a statement abs(x' - x + b) <= K/x with one b for all centres
with abs(beta_A) <= A needs K >= (20/3)(15/32) A = (25/8) A. With K <= 50 b_min and b_min = 0.13 this allows
A <= 2.1. So the bound of the row holds at most on a family whose adjoint spread is about 2 or less in
absolute units. This is compatible with (C5) (an order-one margin), and it prices it.

What Theorem SL does not give: the value or the sign of b(S_W; a).

## 5. The Wilson decrement b(S_W; a): what is exact by hand, and what is not (step 3, continued)

By Lemma AB the background is abelian, W = exp(k alpha_l) with alpha = Abar beta. Fluctuations split into the
neutral colour (along k) and two charged colours. Write u = a^i + sqrt(-1) a^j for the charged pair. An
abelian link exp(k alpha) rotates u by the angle 2 alpha.

**Exact second variation of a plaquette at an abelian background. PROVED.** Let the plaquette be
D_1 D_2 D_3 D_4 with D_i = exp(k alpha_i) exp(a_i) in its orientation, angle F = sum alpha_i, and let
at_i be a_i transported to the first corner by D_1 ... D_i. Then W_p = exp(omega) exp(k F) with
omega = sum at_i + (1/2) sum_(i<j) [at_i, at_j] + O(a^3), and

    s_p = 1 - cos F + sin F (sum_i at_i^k) + (1/2) cos F abs(sum_i at_i)^2
          + (1/2) sin F (sum_(i<j) [at_i, at_j])^k + O(a^3).

For charged entries (1/2)[at_i, at_j]^k = Im(conj(ut_i) ut_j). So the plaquette Hessian is
cos F times the covariant curl form plus sin F times the ordered antisymmetric (spin) form on the charged
pair, and cos F times the plain curl form on the neutral colour.

So Psi at order beta^2 is the sum of these parts, with G = H_0^(-1):

| Part | Formula at order beta^2 | Contribution to b | State |
|---|---|---|---|
| (N1) neutral plaquette tadpole, from cos F = 1 - F^2/2 | -(1/4) sum_p g_p phi_p^2 | + gbar/2, in [15/64, 1/4] | PROVED (as Theorem SL step 4) |
| (C1) charged plaquette tadpole from cos F | -(1/2) sum_p g_p phi_p^2 | + gbar, in [15/32, 1/2] | PROVED (two colours) |
| (Z) normalisation -(3/2) sum_c log abs(M_c) | (3/4) sum_c Var_e(theta_e) | - 3/16 exactly | PROVED below |
| (C2) charged transport tadpoles: second order of the rotations by 2 alpha in the covariant curl, and sin F times first-order rotation in the spin form | (1/2) trace(G H_2) | a lattice sum | not evaluated |
| (C3) charged bubbles: the covariant-curl vertex and the spin vertex, each of order beta | -(1/4) trace(G H_1 G H_1) <= 0 in total | >= 0 in total; holds the universal part | not evaluated |
| (P) pin vertices: T_c at the abelian background, neutral and charged | tadpoles and bubbles with a Q^T(...)Q | a lattice sum | not evaluated |

Proof of (Z). At an abelian background M_c = mean_e exp(k theta_e), so
abs(M_c) = 1 - Var_e(theta_e)/2 + O(4) and -(3/2) log abs(M_c) = (3/4) Var_e(theta_e) + O(4). For a constant
fine field strength f (potential A_rho(x) = (1/2) sum_sigma f_(sigma rho) x_sigma) the contour of bond
(y, mu) with offset xi has theta_e = 2 sum_sigma xi_sigma f_(sigma mu), for every order of the axes: the two
legs differ by the translation 2 e_mu, which shifts A by the constant f_(mu .), and the two straight links give
sum_sigma f_(sigma mu) xi_sigma. The offsets are uniform on {0,1}^4, so
Var_e(theta_e) = sum over sigma not mu of f_(sigma mu)^2. Summed over the four bonds of a coarse site this is
2 sum_(sigma<mu) f^2, and (Z) is (3/2) sum_(sigma<mu) f^2 per coarse site. The leading term
(x/2) sum_p phi_p^2 is 8 x sum_(sigma<mu) f^2 per coarse site. So (Z) raises the readout by (3/2)/8 = 3/16.
The alias corrections are of relative order p (Section 3). QED

So

    b(S_W; a) = (3/2) gbar(a) - 3/16 + (C2) + (C3) + (P),   with (3/2) gbar - 3/16 in [33/64, 9/16] = [0.516, 0.5625].

**Not enclosed.** (C2), (C3) and (P) are sums over the Brillouin zone of products of the propagator
H_0(q)^(-1), which holds the 384-contour symbol of Q. I found no hand evaluation. The sign of b(S_W; a) is
therefore NOT proved here. GUESSED: b(S_W; a) lies between 0.5 and 1.2 for a of order one. Reason: the
unpinned plaquette tadpole is 3/4 (the known shift beta to beta - 3/4 of the SU(2) Wilson action, from
<1 - Re U_p> = 3/(4 beta)), Lemma G shows that at least 15/16 of it is taken in the first step, the total
finite part of the Wilson action against a continuum scheme is about 1.1 in x (from the Lambda ratio 19.82 of
A. and P. Hasenfratz 1980; recalled), and one step holds the universal 0.2575.

**Remark RS (reflections; noticed here, ARGUED, not on file by the greps of Section 1 and by
`reflection|hypercubic` in the two k2 design files).** Q2 with corner bases commutes with the coarse
translations and with the 24 permutations of the axes. It does not commute with a reflection of an axis: the
reflected kernel uses the offsets {0, -1} in that direction, that is the opposite corner. The design note
3.2 (iii) says this for reflection positivity; check 1469 line 46 comments on it. The point here is the
readout. Without reflections the quadratic gauge-invariant forms of dimension four are two:
sum F_(mu nu)^2 and I = sum over mu and over nu not rho of F_(mu nu) F_(mu rho). I is invariant under
permutations and under the total inversion, and it changes under a single reflection. At the Gaussian level
the coefficient of I is 0 (the symbol of Q is 2 + O(k), so the image Hessian is x p^2 times the transverse
projector up to O(p^3)). At one loop nothing forces it to vanish. So (i) the class of 4.2 asks for hypercubic
covariance that the image of Q2 does not have; (ii) the readout may be two numbers after one step. The
decrement b of this note is the coefficient of sum F^2 (measured on one component F_12, where I vanishes).
Whether the coefficient of I is nonzero is OPEN; the computation of Section 7 can measure it. A map with
centred bases and odd side has the reflections.

## 6. Selectivity: the first-step decrement is not the mechanism (step 4)

**Compact U(1) with the Wilson action (filter (t1)).** The same computation with one neutral colour, the
normaliser I_0 (prefactor exponent 1/2) and no charged sector gives

    b_U(1)(a) = gbar(a)/2 - 1/16 + (P_neutral),

with gbar/2 - 1/16 in [11/64, 3/16]. PROVED for the two displayed terms; (P_neutral) not evaluated. Over all
steps the abelian decrements add up to 1/4 (the known tadpole shift of the Wilson U(1) coupling;
recalled). So in compact U(1) the first Q2 step has a decrement of order 0.2, and the later ones are summable.
This corrects one line of the design note 4.5 (t1): "the Gaussian part gives x' = x, the remainder is
monopole loops" holds for the Villain model; for the Wilson U(1) action the one-loop term is not zero. The
row's sentence "b comes from the non-abelian terms" is also not exact: (N1) and (Z) are abelian terms.

**Consequence.** A proof that b(S_W; a) > 0 at the first step would not be selective: the abelian model has
a positive first-step decrement of the same order, by the same tadpole. Row 1465 found the same for the
plaquette margin ("a tadpole fact, dead as a gap mechanism"). What separates SU(2) from U(1) is the
decrement that persists along the orbit.

**Proposition FP (the persistent decrement). SKETCHED.** Let S_k = R_a^k S_W be the classical orbit. Suppose
S_k converges to a fixed shape S_* = R_a S_* fast enough that b(S_k; a) converges to b(S_*; a). Then
b(S_*; a) = (11/(3 pi^2)) log 2 for SU(2), for every a, and 0 for U(1). Argument: by Proposition L applied k
times the readout after k steps is x - sum_(j<k) b(S_j; a) + O(k/x) (the one-loop term of an earlier step is
an O(1) perturbation of the shape, and R_a moves its marginal part unchanged by Corollary L2). The k-fold map
is a block map of side 2^k, whose one-loop coefficient is (11/(3 pi^2)) k log 2 + O(1). So the Cesaro mean of
b(S_j; a) is (11/(3 pi^2)) log 2. For U(1) the sum converges. Not proved: the existence of S_*, the rate, the
continuity of b in the shape. Theorem SL gives the size of the continuity constant in one direction (5/2 per
unit of quartic coefficient).

So the statement that a chain needs is:

    (DR-orbit)  b(S_k; a) >= b_min > 0 for every k >= 0, with b(S_k; a) tending to 0.2575,

and the tube of step k is centred at x_k S_k plus the one-loop term, not at a Wilson shape. The first steps
(k = 0, 1, 2) are finite computations. The tail needs a rate for S_k and the continuity of b. By Theorem SL
and Section 5 the margin is not large: the persistent value 0.2575 equals a quartic shift gamma of 0.11.
