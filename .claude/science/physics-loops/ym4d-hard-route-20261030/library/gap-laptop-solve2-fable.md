lead: anthropic/claude-fable-5-2/max laptop-subagent

# FINISH row 1269 — gap-laptop-solve2-fable

Target (Jaffe-Witten): four-dimensional SU(2) Yang-Mills theory exists as a
quantum field theory on R^4 and has a mass gap Delta > 0.

Labels used below: PROVED, ARGUED, GUIDE, OPEN.

Status of this file: created at the start of the run. Each step below is
appended as it is finished. Text here is the only record that survives an
error.

## Step 0 — file created

Row 1269, Claude Fable 5.2 (max), laptop subagent, 2026-11-20. Author only; checked by no one.
No outside search. Numeric runs, if any, are named where they occur and are GUIDE only.

## Step 1 — what was read (statements about the record, not mine)

- `parts/gap.md` L1-104: the formulation, the wall (W), the blockage sentence, methods 19-36, the lead rules
  CL and W2.
- `library/gap-laptop-solve-fable.md` (row 1217, the same seat at medium effort) in full.
- RESULT lines, read from `FINISH.md`: rows 678, 679, 684 (thin twisted torus), 1011, 1016, 1018, 1026, 1031
  (the port of the two-dimensional pinned-cell step), 1180, 1190, 1194, 1197, 1199, 1200, 1204, 1215, 1218,
  1254, 1256, 1258, 1260, 1261, 1265.
- `library/prior/gap-o4-pinned-cell-read-opus.md` L1-140 (the reading of OpenAI's O(4) stiffness iteration,
  Sections 3.1-3.7); `library/gap-paths-fable.md` L1-120; `library/gap-ac-lat.md` L1-40;
  `library/gap-skeleton-final.md` (headings, table S1-S6, 13.2); the head and RESULT of `library/gap-s1-opus.md`.
- Keyword searches of `FINISH.md` and `library/` for each idea of Step 2 before any work on it (results
  are given with each idea).
- Not read: the proofs behind rows 720, 1161, 1179, 1180 (the reduction of the gap clause to (N-phys) and the
  continuum datum); the Sussman-Alpoge account; the OpenAI papers themselves. I rely on the RESULT lines as
  pointers only.

The record's own summary, which I do not re-derive: the Jaffe-Witten gap clause is reduced to (i) the
continuum datum (existence is not proved) and (ii) one infrared input at order-one effective coupling, in
the forms (W), (N-phys), (SL)/(RR). No row holds a mechanism for (ii).

## Step 2 — how best to attack it (GUIDE unless marked)

### 2.1 What a proof must contain

G1 (GUIDE). The target splits into the continuum construction and a lower bound on the lattice gap of order
the asymptotic-freedom scale. With beta = 4/g^2 and b_0 = 11/(24 pi^2), the scale is
xi(beta) ~ exp(3 pi^2 beta / 11) up to a power of beta. Balaban's renormalization group controls the flow
while the running coupling is small. The strong-coupling expansion (Osterwalder and Seiler) starts at small
beta. Between them is a band of effective couplings of order one. Every known rigorous tool that works
inside the band (reflection positivity, chessboard, transfer-operator positivity, Dobrushin-Shlosman
finite-size criteria) also holds for compact U(1) at weak coupling, where there is no gap (Guth; Frohlich
and Spencer). The lane says the same in `parts/gap.md` L46-50.

G2 (GUIDE). Only one kind of statement can cross a band of this width without a computation at one
coupling: a one-sided inequality that is true at every value of the running quantity and that moves it
monotonically. The two-dimensional O(4) proof read in rows 1007-1010 (OpenAI; also Ding, Huang and Yang) is
of this kind: the stiffness of a pinned square is "direct cost minus current covariance", and a lower
bound on the covariance (a Cramer-Rao bound fed by Ward identities with a non-abelian bracket term) lowers
the upper bound on the stiffness by (log l)/pi per scale factor l, at every value of the stiffness. So the
question for four dimensions is: which quantity plays the role of the stiffness, and which class of local
systems is closed under conditioning.

### 2.2 The directions of the two easy inequalities (ARGUED; standard)

Let r(L) = Z_tw / Z on the symmetric torus of side L, one centre twist in the (1,2)-plane, F_v = -log r.
With T_1 the transfer operator in direction 1 and P_2 the centre flip of the links of direction 2 across
one layer, Z = A_+ + A_-, Z_tw = A_+ - A_-, A_pm = Tr(T_1^L restricted to P_2 = pm 1) >= 0. So

    A_- / A_+ = (1 - r)/(1 + r) = tanh(F_v / 2),        F_e := -log(A_-/A_+) = -log tanh(F_v/2).      (2.1)

This is 't Hooft's duality in the form of Tomboulis and Yaffe. The lane uses the same sector algebra (the
tanh form is in row 1018, Lemma PAR; sector weights are in row 1155 (34) as quoted in
`library/gap-paths-fable.md`); I did not look for the exact line of (2.1) in the record. Two remarks follow.

(a) An upper bound on F_v (vortices are cheap) is a lower bound on the electric flux free energy F_e
(confinement of flux). Upper bounds on a free-energy cost are the variational direction (Gibbs' inequality,
Cramer-Rao); lower bounds are the reflection-positivity direction. So the hard half of the gap problem
for the flux sectors is the easy half for the vortex. The two-dimensional proof works in the same
direction: it needs only upper bounds on the stiffness.

(b) Weak-coupling start values (on file; I re-derived the count and agree; a first draft of this paragraph
used the abelian constant field for the single-plane twist, which is wrong, and is corrected here). For a
single-plane twist the twisted sector has zero-action configurations (twist eaters: U_1 = i sigma_1 on one
layer, U_2 = i sigma_2 on one layer), isolated up to gauge. The periodic sector has a four-dimensional
valley of flat connections with stabilizer U(1). The dimensions of the two minimum sets differ by 3, and
the valley integral has a logarithm at the origin (the SU(2) matrix integral in four dimensions is
marginal). So at fixed lattice size F_v = (3/2) log beta + log log beta + O(1): rows 1004 and 1008, and
item 7 of the table in `library/gap-solve-check-opus.md`. With a running coupling this reads (GUIDE)

    r(L) ~ C / (beta_eff(L)^(3/2) log beta_eff(L)),      beta_eff(L) = beta - (11/(3 pi^2)) log(L/a),

so r grows on each doubling by the factor 1 + (11 log 2/(2 pi^2))/beta_eff: a relative step of order g^2
(row 1200 says the same of every neutral quantity). A sector with positive minimal action c/g^2 (the
crossed twist, c = 4 pi^2, row 1200) has weight exp(-c beta/4) (L/a)^(11 c/(12 pi^2)), which reaches order
one at L/a ~ exp(3 pi^2 beta/11) for every c: the scale of G1. In both forms, "the twist ratio grows on
each doubling until it is of order one, then tends to 1" is the crux written as a monotonicity statement.
It is false for frozen Z_2 at weak coupling (r decays like exp(-tau L^2)). A proof must resolve a relative
step of order g^2, as the two-dimensional proof resolves a step (log 2)/pi against a stiffness h.

### 2.3 Ideas tried in thought, each with its first failing step and its place in the record

I1. Lichnerowicz / Bakry-Emery on the gauge quotient. For gauge-invariant f the Hessian has forced
components along the orbits, which add the O'Neill term to the curvature: the effective Bakry-Emery
tensor is Ric + Hess S + Q with Q(X,X) = sum_k (2 |(nabla_X V_k)^H|^2 + |(nabla_X V_k)^V|^2), V_k an
orthonormal frame of gauge generators. In lattice units Q is of order one per link, as is Ric. The
Hessian of the Wilson action has negative directions of size beta |s_p| ~ sqrt(beta) per link at typical
fields (the term "F . [X, X]", the spin-paramagnetic coupling). So the tensor is not positive at large
beta. First failing step: convexity. On file in substance (methods 24, 31; rows 957, 968, 982).

I2. A thick-vortex bound by Gibbs' inequality (the argument of Pfister, and of McBryan and Spencer, for
spin systems): F_v <= E[S_tw(TU) - S(U) - log Jac_T(U)] for a bijection T. For T = left multiplication of
link l by exp(i r_l sigma_3) in the lab frame, the gauge average gives an exact formula,

    E[tr U'_p] = cos(r_1 - r_4) cos(r_2) cos(r_3) E[tr U_p]                                            (2.2)

(PROVED here in three lines: the three sites of the plaquette that carry a twisted tail are gauge-averaged
independently, the average of exp(i a n.sigma) over the direction n is cos a; links numbered so that
l_1 and l_4 leave the base site). So the cost is (beta/4) E[tr U_p] sum of r^2, with no cancellation
between links: of order beta L^2 for a potential of a uniform flux pi. In a smooth gauge the coefficient
beta becomes a constant, and the L^2 stays: it is the seagull term, and only the current covariance
cancels it. First failing step: first-order variational bounds lose the covariance. On file: rows 1011
(Proposition B, Lemma FR), 1016 (Identity AV, Corollary AV2), 1141, 1190. Formula (2.2) is the
one-plaquette case of AV2.

I3. A stiffness for a symmetry background. The pure gauge theory has one global symmetry, the Z_2
one-form centre symmetry. Higher-form symmetries are abelian, so its background field (the 't Hooft
twist) has no bracket term; and it is discrete, so it has no infinitesimal Ward identity. The continuous
paths to the centre, exp(i a n.sigma) with n in S^2, are gauge invariant only after an average over n per
plaquette, which makes the twist a change of the plaquette weight (its character coefficients are
multiplied by chi_j(a)/d_j), not a vortex. First failing step: no rigid non-abelian symmetry acts on the
integration variables. On file: Lemma CEN+ (row 1016), row 1197.

I4. Plaquette (two-form) twists in a transported frame. The response to a twist of the plaquette weights
by exp(i B_p sigma_3), in a frame carried from the pins along fixed paths, is "direct minus covariance"
with direct term at most beta |B|^2 for every pin: the start bound is trivial and has no seagull. But
the thick two-form twist is not the centre vortex: the difference is removed by a link rotation only
when the links commute with sigma_3, and the defect is the frame cost of I2. First failing step: the
identification of the two-form response with a vortex cost. On file: row 1197 ("the one-form twist
carries the frame defect").

I5. The gradient modes of the two-dimensional proof have no gauge analogue (ARGUED here). In the O(4)
proof the test field is "rotate ring mode i about the axis a by the force on the same mode in the colour
a x A"; the force on a gradient mode has an exactly known variance (integration by parts), and the
bracket turns the zero-mode current into that force. In a gauge theory the generators G_lambda of gauge
transformations are divergence-free and annihilate the action, so G* = -G, and the same test variable is
S = -sum_i G_(lambda_i a) (d_(lambda_i f A') V) = const . d_((sum lambda_i^2) f A) V: it is the current
itself, and the Cramer-Rao bound is the identity Var J >= Var J. The modes that give the logarithm in two
dimensions are pure gauge in four. The anti-screening of the gauge theory sits in the variance of a
bilinear of transverse modes (the spin current), and its lower bound must also cancel the divergent
seagull exactly. First failing step: no exactly known variance. Row 1190 states the conclusion
("a one-sided stiffness induction cannot close in pure gauge theory, because a small twist cost needs a
roughness bound on the field", ARGUED there).

I6. Temporal gauge. Between two time slices the group of time-independent gauge transformations is a
rigid non-abelian symmetry, and the class of time slabs with arbitrary top and bottom pins is closed
under conditioning. A pin-uniform bound on the response must be invariant under the adjoint action of
that group, so it is site-diagonal: it bounds single Polyakov lines (a self-energy, the same for U(1))
and says nothing on smooth twists. First failing step: uniformity in the pins. On file: Identity HAM1
(row 1016), Corollary AV2, row 1190 ("the temporal-gauge rigid group").

I7. Two directions as base. The four-dimensional theory is a two-dimensional array of O(4) chiral fields,
one per internal link, coupled by the internal plaquettes and by a gauged two-sided SO(4) background. A
single O(4) field at b = beta has correlation length exp(pi beta), longer than exp(3 pi^2 beta/11) since
3 pi/11 < 1. No inequality follows: a bound of the four-dimensional loop by a two-dimensional two-point
function is false for U(1) (perimeter law against a power law in the area form), and the layer in a
two-sided background is row 1139 (no background-uniform rate at large b). First failing step: the
comparison is not class-wide, and no selective form is known.

I8. The thin twisted torus (Tanizaki and Unsal; 't Hooft). At weak coupling it has a gap and an area law by
semiclassics. It is the lane's Route T (rows 676-684, 842). Theorem S1 (decay at rate c/n for fixed fibre
side n and beta >= beta_0(n)) is not proved there: Lemma PE (the restricted-ensemble expansion) is
missing. The crux of the route, (AC'-lat), is as hard as (W).

I9. Tests that bind every route: the mixed fundamental-adjoint action with its first-order line (K7,
on file); the thermal slab, where a constant abelian background has a true screening mass, so that no
argument that is blind to the geometry can remove the seagull of I2 (ARGUED here; I did not find this
sentence in the record, but it is a remark, not a result).

### 2.4 The choice

None of I1-I9 passes its first step, and all but the remarks are on file. The honest reading is the
lane's own: the missing object is a one-sided, scale-monotone inequality for a gauge-invariant response,
valid at order-one coupling. I do not have one. The next steps of this file work on the one place where
I see room for a statement that is exact, gauge invariant and not yet written: the transverse and
longitudinal doubling inequalities for the twist ratio on asymmetric tori (2.1), and what they can and
cannot give together. Results are appended below.

## Step 3 — the doubling relations in vortex variables

### 3.1 Setting and inputs

Torus with sides (L_1, L_2; L_3, L_4), Wilson SU(2) weight, one centre twist on a column of (1,2)-plaquettes
(all x_3, x_4). Z_0 is the periodic partition function, Z_1 the twisted one, r = Z_1/Z_0, x = -log r.

Inputs taken from the record and not rechecked here:
- (In-1) The transfer operator T_1 in direction 1 on gauge-invariant functions of a slice is positive and
  trace class, commutes with the centre flip P_2 (all links of direction 2 across one layer), and
  Z_0 = Tr T_1^(L_1), Z_1 = Tr(T_1^(L_1) P_2). The same with the roles of directions 1 and 2 exchanged.
  (Osterwalder and Seiler; `library/gap-transfer.md` Statement (1), as cited by `library/gap-ac-lat.md`; the
  Flip lemma and Lemma B of `library/gap-ac-lat.md`. I read the citations, not the proofs.)
- (In-2) The transfer operator in direction 3 of the slice with the twisted plaquettes, T_3^(1), is positive
  and trace class, and Z_1 = Tr (T_3^(1))^(L_3); also Z_0 = Tr (T_3^(0))^(L_3). The same in direction 4.
  (`library/gap-ac-lat.md` Lemma A step 1; `library/gap-transfer-twisted.md`.)

### 3.2 Lemma D (PROVED given (In-1), (In-2); elementary)

Put psi(t) = -log tanh(t/2) on (0, infinity). For a positive trace-class operator T != 0 with largest
eigenvalue lambda_0 put s_k(T) = Tr T^k / lambda_0^k - 1 and J_k(T) = 2 log Tr T^k - log Tr T^(2k).

(i) psi is a decreasing involution of (0, infinity).

(ii) 0 <= J_k(T) <= 2 log(1 + s_k(T)).

(iii) Let A_pm = Tr(T_1^(L_1) restricted to P_2 = pm 1) and y = log(A_+/A_-). Then y = psi(x), and

    y(2 L_1) = 2 y(L_1) + J^-(L_1) - J^+(L_1),        x(2 L_3) = 2 x(L_3) + K^1(L_3) - K^0(L_3),          (3.1)

where J^pm = J_(L_1)(T_1 on the sector P_2 = pm 1) and K^i = J_(L_3)(T_3^(i)). The other sides are fixed in
each identity. The first holds also for direction 2 (with P_1), the second for direction 4.

(iv) Hence, for the symmetric torus of side L and its double,

    x(2L) <= 4 psi( 4 psi(x(L)) - 2 d_1 - d_2 ) + 2 d_3 + d_4      whenever 4 psi(x(L)) > 2 d_1 + d_2,   (3.2)

with d_1 = J^+ for the step (L,L;L,L) to (2L,L;L,L), d_2 = J^+ (direction 2, flip P_1) for the step to
(2L,2L;L,L), d_3 = K^1 for the step to (2L,2L;2L,L), and d_4 = K^1 (direction 4) for the step to (2L)^4.
Each d_i is at most twice the logarithm of one plus a thermal ratio: for d_1, d_2 the ratio of the
flip-even sector of a periodic slice; for d_3, d_4 the ratio of the twisted slice.

(v) The map Phi(t) = 4 psi(4 psi(t)) is increasing, Phi(t) < t on (0, x*), Phi(t) > t on (x*, infinity),
where x* = psi(y*) and y* is the unique zero of h(y) = psi(y) - 4 psi(4y). Also Phi(t) = t^4/2 (1 + o(1))
as t tends to 0 and Phi(t) = 4t - 8 log 2 + o(1) as t tends to infinity.

Proof.
(i) tanh(psi(t)/2) = (1 - e^(-psi(t)))/(1 + e^(-psi(t))) = (1 - tanh(t/2))/(1 + tanh(t/2)) = e^(-t). So
psi(psi(t)) = t. psi'(t) = -1/sinh t < 0.
(ii) With eigenvalues lambda_0 >= lambda_1 >= ... >= 0, s_k = sum over i >= 1 of (lambda_i/lambda_0)^k, and
s_2k = sum of squares of non-negative numbers, so 0 <= s_2k <= s_k^2. J_k = 2 log(1 + s_k) - log(1 + s_2k).
The upper bound is s_2k >= 0. The lower bound is (1 + s_k)^2 >= 1 + s_k^2 >= 1 + s_2k.
(iii) By (In-1), Z_0 = A_+ + A_- and Z_1 = A_+ - A_-. Z_1 > 0, as the integral of a positive weight, so
A_+ > A_- >= 0, and A_- > 0 because T_1 is positive and not zero on the odd sector. A_-/A_+ =
(1 - r)/(1 + r) = tanh(x/2), which is y = psi(x). The first identity of (3.1) is
log A_+(2L_1) - log A_-(2L_1) - 2 log A_+(L_1) + 2 log A_-(L_1) = -J^+ + J^-. The second is the same
computation for x = log Z_0 - log Z_1 with (In-2).
(iv) By (iii) and (ii), y(2L_1) >= 2 y(L_1) - d_1. Apply it again in direction 2 on the torus (2L,L;L,L):
y(2L,2L;L,L) >= 4 y(L) - 2 d_1 - d_2. Since psi is decreasing and x = psi(y), x(2L,2L;L,L) <=
psi(4 psi(x(L)) - 2 d_1 - d_2) when the argument is positive. By (iii) and (ii), x(2L_3) <= 2 x(L_3) + d_3,
and again in direction 4. This gives (3.2).
(v) Phi is a composition of two decreasing maps. With y = psi(t), Phi(t) < t is 4 psi(4y) < psi(y), that
is h(y) > 0. h'(y) = -1/sinh y + 16/sinh 4y = (1/sinh y)(4/(cosh y cosh 2y) - 1), because
sinh 4y = 4 sinh y cosh y cosh 2y. So h increases on (0, y_1) and decreases on (y_1, infinity), where
cosh y_1 cosh 2 y_1 = 4. As y tends to 0, h(y) = 5 log 2 + 3 log y + o(1), which tends to minus infinity.
As y tends to infinity, h(y) = 2 e^(-y)(1 + o(1)) > 0. So h has exactly one zero y*, it lies in (0, y_1),
and h > 0 exactly on (y*, infinity). Since psi is decreasing, y > y* is t < x*. The two asymptotic forms
follow from psi(t) = log(2/t) + o(1) at 0 and psi(t) = 2 e^(-t)(1 + o(1)) at infinity. QED

GUIDE (one run in pure Python, under one second, outside the repository): x* = 1.61410, r* = e^(-x*) =
0.19907, y* = 0.40353; a grid of step 0.001 on (0.02, 30) shows one sign change of Phi(t) - t, at 1.615.

### 3.3 What Lemma D says and does not say (ARGUED)

- Below x*, with small defects, the bound improves like t^4/2 per doubling. This is the area law in
  vortex form: exp(-sigma L^2) to the fourth power is exp(-sigma (2L)^2). It is the flux-sector part of the
  lane's doubling engine (Theorem S, Corollary S2, Lemma ADD of row 1018), written for one twist. It is not
  an engine by itself: the defects d_i must be small at every later scale, and that needs all sectors.
- Above x*, with zero defects, (3.2) would read x(2L) <= 4 x(L) - 8 log 2 + o(1). Frozen Z_2 at weak
  coupling has x(2L) = 4 x(L) (the cost tau L_3 L_4 does not depend on the transverse sides), which violates
  that form. There is no contradiction: there d_1 and d_2 are of order log 4 (the other flux sectors of the
  flip-even part are degenerate with the vacuum), 4 psi(x) is exponentially small, the condition of (3.2)
  fails, and the lemma is silent. So the defects cannot be dropped, and the inequalities carry no part of
  the running.
- At weak coupling SU(2) starts on the upper branch, at x = (3/2) log beta_eff + log log beta_eff + O(1)
  (Step 2.2 (b)), and must move down by (11 log 2/(2 pi^2))/beta_eff per doubling. There 4 psi(x) is about
  8 r, of order beta_eff^(-3/2), and each d_i is of order one (the thermal ratios of a free gluon gas at
  aspect ratio one are of order one; row 1158 quotes 18 for the cube at T = n/2). The condition of (3.2)
  fails again and Lemma D is silent on the whole perturbative range.
- The twist ratio reads one channel. A product of SU(2) with a free photon has the same r(L) and no gap
  (Lemma PT of the lane). So even r(L) to 1 at the area-law rate gives confinement of flux, not the
  neutral gap (row 1197 says this of a complete port).

So Step 3 proves nothing that moves the wall. It is recorded because the fixed point x* and the identity
(3.1) are exact and short; I did not find x* in the record, and (3.1) is a rewriting of what is there.

## Step 4 — a last attempt: a size-uniform upper bound on the twist cost (the "start bound")

Statement tried. (SB) For Wilson SU(2) at a fixed beta there is C(beta) with F_v(L) <= C(beta) for the
symmetric torus of every side L. In words: the theory is never magnetically ordered; the flux sectors
never become degenerate at the rate of frozen Z_2, Q_8 or 2T. It is the gauge analogue of the trivial
bound "stiffness at most the bare coupling" from which the two-dimensional iteration starts. It is weaker
than (W) and it is selective against the frozen groups, not against U(1). OPEN; I did not find it proved
in the record (rows 1011 and 1016 list the Schrodinger-functional form of the start bound as open). I made
no literature search in this run; before (SB) is treated as new or as open in print, a reader should check
Yaffe (1980) and Tomboulis and Yaffe (1985) on bounds for the vortex free energy. I state nothing about
their content.

Three routes, each to its first failing step (ARGUED).

1. Gibbs' inequality with a link map. By (2.2) a lab-frame abelian map gives no gain in the gauge-invariant
   ensemble. A gauge-fixed or covariant-frame map leaves the seagull term c L^2 (Step 2.3, I2). First
   failing step: the frame.
2. The longitudinal form. F_v <= E_m L_3 + log(1 + s^0), with E_m the magnetic flux energy of the slice
   and s^0 the thermal ratio of the periodic slice ((In-2) and Lemma D (ii)). An upper bound on E_m needs a
   trial state for the twisted slice. The twisted and the periodic slice are locally conjugate (Lemma C
   of `library/gap-ac-lat.md`), but the conjugation is a lab-frame rotation of one layer of links, and
   in the vacuum state it has the cost of route 1. A trial state glued from local pieces of the periodic
   vacuum needs a finite correlation length. First failing step: the trial state presupposes the gap.
3. A Higgs comparison. Add a term kappa sum_l (1/2) tr(sigma_3 U_l sigma_3 U_l^(-1)), which fixes a
   frame. At large kappa the links are nearly abelian, the frame cost of the thick vortex is small, and
   F_v(kappa) <= pi^2 beta/2 + O(1) on the symmetric torus by route 1. If F_v(kappa) were non-decreasing
   in kappa, (SB) would follow with C = pi^2 beta/2 + O(1). PROVED (elementary, all sides at least 5):
   with h_l = (1/2) tr(sigma_3 U_l sigma_3 U_l^(-1)) = (Ad U_l)_33 and N_l the number of links,

       F_v(kappa) = F_v(0) + (kappa^4/81) sum_p ( E_0[chi_adj(U_p)] - E_1[chi_adj(U_p)] ) + O(kappa^5),

   where E_0, E_1 are the periodic and twisted Wilson expectations and chi_adj(U) = (tr U)^2 - 1.
   Proof. log Z_i(kappa) is the cumulant generating function of X = sum_l h_l under E_i, and X is bounded.
   Both measures are gauge invariant, so a monomial in the h_l may be averaged over independent Haar
   gauge rotations at the sites. Under a gauge rotation h_l = e_3^T G_x R_l G_y^T e_3, with R_l = Ad U_l and
   G_x, G_y the adjoint matrices at the two ends. Three facts. (a) If a site meets exactly one link of the
   monomial, and that link occurs once, the average is 0 (the adjoint representation has no invariant
   vector). (b) With sides at least 5, two different links share at most one site, the graph has no
   triangle, and its only 4-cycles are plaquettes. (c) Ad U_l is Haar distributed, so h_l is uniform on
   [-1, 1]: E[h^2] = 1/3, E[h^3] = 0, E[h^4] = 1/5; and E over one end of l of h_l^2 is 1/3 whatever the
   rest is (a row of a rotation matrix is a unit vector). From (a)-(c): E_i[X] = 0; E_i[X^2] = N_l/3;
   E_i[X^3] = 0 (a monomial l, l, l' has an end of l' that meets nothing else; three different links
   with no such end form a triangle); and in E_i[X^4] the patterns (l,l,l,l), (l,l,l',l') give
   N_l/5 + N_l(N_l - 1)/3, the patterns (l,l,l,l') and (l,l,l',l'') give 0 (an end of l' meets nothing
   else, or the three links form a triangle), and four different links give 0 unless they are the links
   of a plaquette. For a plaquette, the averages at three corners give E[G^T e_3 e_3^T G] = 1/3 each and
   the fourth gives (1/3) tr Ad(U_p), so E_i[h_1 h_2 h_3 h_4] = E_i[chi_adj(U_p)]/81, and there are 24
   orderings. So the fourth cumulant is a sector-independent number plus (24/81) sum_p E_i[chi_adj(U_p)],
   the second is N_l/3 in both sectors and the first and third vanish. QED
   So to leading order the frame term acts as an adjoint plaquette coupling, and the sign of the
   derivative is the sign of the response of the twist cost to that coupling: positive in one-loop
   perturbation theory (the effective beta grows), not known in general. Monotonicity at all kappa is a
   correlation inequality of Ginibre type, and none is known for SU(2) (rows 1194, 1199: the three-sheet
   energy is not of Ginibre type; the diamagnetic comparison is open in the linear class and false for a
   hard cap). First failing step: the correlation inequality.

(SB) stays OPEN. It has no consumer on the path of (W) by itself: (W) needs the twist cost small, not
bounded, and the neutral gap as well.

## Step 5 — what failed and what is left

- Not proved: the mass gap of four-dimensional SU(2) Yang-Mills theory in the sense of Jaffe and Witten.
  Nothing is disproved.
- Attack considered best (Step 2): a one-sided, scale-monotone inequality for a gauge-invariant response,
  in the variational direction, as in the two-dimensional O(4) proof. Nine openings were taken to their
  first failing step. Each fails at one of three places: no rigid non-abelian symmetry on the integration
  variables (I3, I5, I6); the frame or seagull term, which only an exact lower bound on a current
  covariance can cancel (I2, I4, Step 4); or convexity (I1). All nine are on file in substance.
- Proved here, small, not selective, and moving nothing on the path of (W): formula (2.2); Lemma D with
  the fixed point x* of the idealized doubling map; the kappa^4 formula for the twist cost under a frame
  term in Step 4, route 3.
- Corrected here: my first draft of Step 2.2 (b) used the abelian constant field for the single-plane
  twist. The record's count (rows 1004, 1008) is right: F_v = (3/2) log beta + log log beta + O(1) at fixed
  size, because twist eaters have zero action.
- OPEN, unchanged: (N-phys), (W), (SL)/(RR), the continuum datum (existence), the selective inequality at
  order-one response. OPEN, named here: (SB) (literature not searched).
- Limits of this run: one author, no check by another model or provider; the inputs (In-1), (In-2) and
  every row cited are used as read from RESULT lines, not rechecked; one numeric run (the fixed point x*),
  GUIDE only. This seat is the same model family as most earlier seats, so its agreement with the lane's
  map is not independent evidence.

Credits: Jaffe and Witten (the problem); Balaban (the renormalization group and ultraviolet stability);
Sussman and Alpoge, with Claude and Codex as authors of their text (the account the lane ports);
Osterwalder and Seiler (reflection positivity, the transfer operator, strong coupling); 't Hooft (twisted
boundary conditions, flux duality); Tomboulis and Yaffe (flux inequalities); Mack and Petkova (vortex
containers); Guth, and Frohlich and Spencer (the massless phase of U(1)); Pfister, and McBryan and Spencer
(the variational spin-wave argument); Lott, and O'Neill (curvature of quotients); Bakry and Emery; Ginibre;
Luscher, van Baal, Gonzalez-Arroyo (small-volume analysis and twist eaters); Tanizaki and Unsal (the thin
twisted torus); Durhuus and Frohlich (the layer comparison); Chatterjee (the probabilistic formulation);
OpenAI, and Ding, Huang and Yang (the two-dimensional O(N) proofs, as read in rows 1007-1010); Bhattacharjee
and co-authors (the one-scale criterion, as read in row 1218); the lane rows cited above.

RESULT: Row 1269 (Claude Fable 5.2 max, laptop subagent; author only, checked by no one; one GUIDE run under one second, no outside search). The mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved. Attack judged best: a one-sided scale-monotone inequality for a gauge-invariant response in the variational direction (the form of the two-dimensional O(4) proof); nine openings taken to a first failing step (no rigid non-abelian symmetry on the integration variables; the frame or seagull term; convexity), all on file in substance. PROVED, elementary, not selective, no consumer on the path of (W): Lemma D (given transfer-operator positivity as on file: F_e = psi(F_v) with the involution psi(t) = -log tanh(t/2), the exact one-direction doubling identities (3.1), the symmetric bound (3.2) with four thermal defects, and the idealized map Phi(t) = 4 psi(4 psi(t)) with exactly one fixed point x*, GUIDE value 1.61410, below which the bound improves like t^4/2 and above which the lemma is silent, as it is for frozen Z_2 and on the whole perturbative range of SU(2)); formula (2.2) (a lab-frame abelian link rotation multiplies the mean plaquette by cos(r_1 - r_4) cos r_2 cos r_3, so no such Gibbs bound beats the frame cost; the one-plaquette case of row 1016 AV2); under a frame term kappa sum_l (Ad U_l)_33 the twist cost changes by (kappa^4/81) sum_p (E_0 - E_1)[chi_adj(U_p)] + O(kappa^5), on tori with all sides at least 5. Corrected in place: the weak-coupling start value of the single-plane twist is (3/2) log beta + log log beta + O(1), as rows 1004 and 1008 have it. OPEN, unchanged: (N-phys), (W), (SL)/(RR), the continuum datum, the selective inequality at order-one response; OPEN, named here with three failed routes: the size-uniform start bound (SB). Output library/gap-laptop-solve2-fable.md.
