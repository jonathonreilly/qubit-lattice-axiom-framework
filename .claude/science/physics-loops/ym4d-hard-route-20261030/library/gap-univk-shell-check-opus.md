lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-23T11:55Z

# Check 1416 of row 1412 (`library/gap-univk-shell-astra62.md`)

Checker: Claude Opus 5.5, high effort, Mac mini worker 2. Cross-provider check of
row 1412 (written by gpt-6.2-astra max). Started 2026-11-22T23:55Z (date -u).
Pinned at commit 0ff18a68f. No numeric job run unless stated.

## Plan

1. Read row 1412 in full, and the consumer (check 1405, rows 1404/1400 as needed).
2. Check the binary-slot statement from the printed disc against III 17653-17692.
3. Check the one-link SU(2) counterexample: Haar radial masses, inclusions,
   bound on mu(P), the two lower bounds and exponents, printed hypotheses,
   companion torus, added labels.
4. Check the fixed-profile drift statement.
5. Check the common-interior contraction estimate (convexity, Jacobian
   (1-alpha)^3, injectivity, two uses of the map).
6. Consequence for the consumer of check 1405; next two rows.
7. Verdict, at most ten defects ranked.

## Step 1. Read (done 2026-11-22T23:58Z)

Row 1412 (206 lines) read in full. Printed source III 17630-17700
(Lemma 9.1:lem-ramp-comparison, statement and move (m3)) read in
`~/ym4d-papers/sa-ca/theorem_0_complete_account_raw_III.tex`. The slot bound
(III eq. 9.1:eq-ramp-comparison-3) reads, for each interpolated slot,
|eta^A + s(eta^B - eta^A)| <= (1 + 20 C_chi theta^k |s|) 1{f^B < (1+varpi_0) c};
the text states it without a range of s, and uses it on the disc
|s| <= (20 C_chi N_w^4 theta^k)^(-1) = R. Row 1412's reading ("grant it on the
disc of radius R") is the weaker of the two readings, so its conclusions hold
under either.

## Step 2. The binary-slot statement (section "What the printed disc decides")

Verdict: HOLDS.

Checked by hand. Write b = b_k = 20 C_chi theta^k, a, b' in [0,1] the native
slot values at a common point. For real s, |s| = R, sign chosen with
s(b'-a) >= 0, the left side is a + R|b'-a| >= 0, so the bound gives
R|b'-a| <= 1 - a + bR, i.e. |b'-a| <= b + (1-a)/R. Correct.

- a = 1, b' = 0: take s = -R: 1 + R <= 1 + bR, impossible when b < 1, for
  every R > 0, so "at any volume" is right.
- a = 0, b' = 1: R <= 1 + bR, i.e. b + 1/R >= 1; with R = 1/(V b) this is
  (V+1) b >= 1. So binary slots agree when (V+1) b < 1. Correct.
- Off the enlarged indicator: s = 0 gives a = 0; any s != 0 then gives b' = 0.
  (Row 1412 says "by the affine bound"; true for any nonzero s in the disc,
  not only s = 1.)
- Disc |s| <= 2 (Y 130293-130308 reading): a = 0, b' = 1 is excluded iff
  2 > 1 + 2b, i.e. b < 1/2. Correct. Slot bound for every s: |b'-a| <= b,
  so b < 1 forces equality. Correct.
- Consequences: b < 1 gives a = 1 => b' = 1, so S^A subset S^B when all
  changing factors are binary slots, hence s^A = 0; both shells vanish when
  (V+1) b < 1. On P every native indicator equals one at both ends, so a
  product of indicators has Theta^A = Theta^B on P and d_test = 0. Correct
  (this is CAP(c) of row 1404 as corrected by check 1405 at its scope).

Defect (nit, D-b1): the statement "if every changing outcome factor is such
a binary slot" presupposes that the failure outcome of a recorded failed test
is itself a slot obeying the same affine bound. Row 1412 flags this ("apply
this statement to its actual outcome factor, which may be a complement");
the printed display covers only the small production slots of P, so the
statement applies only to those. No error, a scope note.

Reading of the result: the printed bound is so strong for {0,1}-valued
slots that the moving small slots in the account cannot be literal changing
indicators in the range (V+1) b_k < 1; either they are smooth (positive,
nonconstant) or they do not change. Row 1412 draws this conclusion
correctly.

## Step 3. The one-link SU(2) counterexample

Verdict: HOLDS as an insufficiency statement for the displayed bounds
(III eq. -3 slot bound, eq. -1 variation bound, the account's mass window
[1/B, A] of row 1391 L97) **with a constant linear in V**; HOLDS AFTER
CORRECTION of its scope (D-c1 below). Every computation was redone by hand.

Source facts used (III 11806-11870, Notation 9.1:not-centre-normalisation):
N_w = 2 L^(m_0 + w), w = w(g) the stop depth, k = n - w; A^sharp =
e^(E_+^(sharp sharp) N_w^4) (III 12142). So in the account V is fixed by g
and k grows with n; A^sharp is itself exponential in V.

3.1 Haar facts. Normalized Haar radial density about any point is
(2/pi) sin^2 q dq (area 4 pi sin^2 q over total 2 pi^2). Ball of radius
v <= r: mass >= (2/pi) int_0^v (2q/pi)^2 dq = c_1 v^3. Band of width v:
mass <= (2/pi) v. Group norm of an element at angle q is |e^(iq) - 1| =
2 sin(q/2), 1-Lipschitz in q. Threshold c = 2 sin(r/2). All correct.

3.2 Profile. g = (1 - chi) f + chi with f(u) = exp(-(log u)^2) on (0,1),
chi a smooth nondecreasing step from 0 at r/8 to 1 at r/4, gives
g' = (1-chi) f' + chi' (1 - f) >= 0 (f' > 0 on (0,1), f <= 1, r/4 < 1);
flat at 0 since f^(n)(u) = u^(-n) P_n(log u) f(u) -> 0. The profile
g(r - d(v,a)) is constant near both poles, smooth elsewhere. Correct.
(Row 1412 says "interpolate by a smooth increasing cutoff"; the convex
combination above is one explicit way; no defect.)

3.3 Inclusion S^B subset S^A. Centres on one great circle at angles 0, -h,
2r - h - t; a lies on the short arc from b to z (length 2r - t < pi). For
v in B(z,r) cap B(b,r), b, z in B(v,r); for u = (lam b + mu z)/|lam b + mu z|,
lam, mu >= 0: u.v > cos r (lam + mu)/|lam b + mu z| >= cos r, using
cos r > 0 and |lam b + mu z| <= lam + mu. So a in B(v,r). Correct.
Hence P = S^B, s^B = 0, F_P^A = F^H (unit weights), F_P^B = F^B.

3.4 Hypotheses. |eta^B - eta^A| <= M h (reads differ by <= h). If eta^A > 0
then d(v,b) < r + h and 2 sin((r+h)/2) <= 2 sin(r/2) + h < (1+varpi_0) c
iff h < varpi_0 c. So both slots vanish off E_B and
|eta^A + s(eta^B - eta^A)| <= eta^A + |s| M h <= 1 + b_k |s| on E_B, every
complex s, once kappa <= 20 C_chi / M. Variation: int J |eta^B - eta^A| <= M h
<= b_k <= C_test theta^k A^sharp. Disc modulus 1 + b_k R = 1 + 1/V. Correct.

What is and is not verified: the example satisfies the *displayed* stop
estimates (slot bound, variation bound, modulus) and the mass window. It does
not, and as a one-link model cannot, instantiate the other hypotheses listed
in item (a) of the lemma (ramp-weight statements, doubling persistence, the
weight statement, clauses (C1), (C2)) as statements about the account's
objects. Row 1412's own body says "the displayed stop estimates"; the FINISH
summary and the queue wording "every printed hypothesis" overstate this
slightly. Defect D-c3 (nit, wording).

3.5 Shell mass. On P: r - t < d(v,b) < r (from d(b,z) = 2r - t), and
d(v,a) > d(v,b) - h gives r - d(v,a) < h + t. mu(P) <= (2/pi) t,
F_P^A <= C t g(h + t) <= C t g(2h). Ball of radius h/8 about x(r - h/2):
d(., z) < r - h/2 - t + h/8 < r; d(., a) <= r - 3h/8; d(., b) >= r + 3h/8.
So it lies in S^A minus P with eta^A >= g(3h/8) >= g(h/4); mass >= c h^3 g(h/4).
With T = log(1/h): log g(h/4) - log g(2h) = (T - log 2)^2 - (T + log 4)^2 =
-2 T log 8 - (log^2 4 - log^2 2). So s^A >= c h^(-9 + 2 log 8), and
9 - 2 log 8 = 4.841 > 0. Correct: log(1 + s^A) >= 4.84 T - C, linear in k.

3.6 Smooth-test mass on P. Ball radius t/4 about x(r - h - t/2): distances
to b and z are < r - t/4, so it is in P, with r - d(., b) >= t/4 and
r - d(., a) >= h + t/4. On P, r - d(v,b) < t. So F^H >= c t^3 g(h),
F^B <= C t g(t), F^B >= c t^3 g(t/4). log g(h) - log g(t) = -T^2 + 144 T^2.
So log(F^H / F_P^B) >= 143 T^2 - 24 T - C. Correct. F^B >=
c exp(-36 T - (12 T + log 4)^2). Correct.

3.7 Parameters and floors. With k = floor(gamma N_w^2), T = k |log theta| + O(1),
T^2 ~ gamma^2 |log theta|^2 V, so every mass is >= e^(-C V) once
144 gamma^2 |log theta|^2 is below the prescribed floor exponent, and
V theta^k = N_w^4 theta^(gamma N_w^2) -> 0, R -> infinity. Correct.
Signed identity: B_rec = 0, the smooth term is about -143 T^2, the A-shell
term enters with a minus sign, s^B = 0; so log(F^B / F^A) <= -143 T^2 + O(T).
Correct; the costs reinforce. Added labels J(1 - eta^m), 1 - J with weight
e^(-D V): on B(z,r), r - d(v,a) < h + t and r - d(v,b) < t, so eta^m < 1 on
J and the two added labels have identical positive sets at both ends; their
masses are <= e^(-D V), below the original floor when D exceeds its
exponent, so the logarithmic lower bounds move by O(1). Correct. Sharp
variant: s^A >= c h^(-9), d_test = 0, and its moving indicator violates the
slot bound once (V+1) b_k < 1, by Step 2. Correct.

**D-c1 (ranked first; scope correction, not a refutation).** The obstruction
is to a constant **linear in V**, and only in the regime where V grows at
least like T^2 (about k^2). At fixed V, which is the account's own
parametrization at fixed g (N_w = 2 L^(m_0 + w(g)), k = n - w -> infinity),
no example of this class can violate a bound C(V) theta^k: in the example the
hybrid term is the A term, so the absolute variation bound pays the A-shell
in absolute form, int over S^A minus P of eta^A <= int J |eta^B - eta^A| <= M h,
and with the floor F_P^A >= 1/B = e^(-C_low V) this gives
s^A <= M h e^(C_low V); likewise |F_P^B - F^H| <= M h gives
d_test <= log(1 + M h e^(C_low V)). So the example is a geometric instance of
row 1391 Remark 7.1 (absolute bound with masses in [1/B, A] gives the log
only with the factor A B = e^(c V); sharp) at the level of a single shell,
and it should be cited as such. It refutes (SHELL) and the d_test rate in
the form the consumer needs (row 1391 7.2b/Row B outcome (2): an
exponential-in-V constant limits the reach of the carry), not a fixed-volume
rate. The FINISH summary "the printed bounds do not give either rate" should
read "do not give either rate with a constant linear in V".

**Strengthening (new here, by hand; regime V ~ k for the shell).** If the
slot need only be Lipschitz (the printed slot bound needs no more), take
g(u) = min(u_+ / r_0, 1), r_0 = r/4, M = 1/r_0, same centres, t = h^12. Then
F_P^A <= mu(P) (h + t)/r_0 <= C t h, the h/8 ball has A-mass >= c h^3 h, so
s^A >= c h^3 / t = c h^(-9), log(1 + s^A) >= 9 T - C; all masses are
>= c t^3 (t/4)/r_0 >= e^(-48 T - C). So the shell obstruction holds with
extensive floors already at k = floor(gamma V), gamma small, with
V theta^k -> 0. For a C-infinity slot vanishing at its edge the masses near
the edge are smaller than every power of h, so floors force V/k -> infinity;
the row's choice exp(-(log u)^2) gives V ~ k^2, and u^(omega(log 1/u)) with
omega -> infinity slowly gives V ~ k omega(k). Whether the consumer needs the
regime V >= k (or V >= k^2) is not stated in rows 1391-1405; see Step 6.
(The d_test lower bound in the Lipschitz variant needs a lower bound on
eta^A over the whole lens P, not done here.)

Prior-art grep for the Lipschitz variant: `library/open-core.md` has no hit
for "shell"; FINISH has no hit for a Lipschitz or piecewise-linear shell
slot. It is a variant of row 1412's construction, credited to that row.

## Step 4. Fixed-profile drift (section "Smooth drift for any fixed profile")

Verdict: HOLDS, with the same scope as D-c1.

- Existence of y_j: Q = -log g is nonincreasing, Q -> infinity as y -> 0+
  (g continuous, g(0) = 0). If -Q'/Q <= K on (0, y_0), then
  (log Q)' >= -K and log Q(y) <= log Q(y_0) + K y_0, bounded: contradiction.
  Correct. (The row's "bounded derivative" is right because Q' <= 0 gives
  0 <= -(log Q)' <= K.)
- The constant-read fibre: masses g(y), g(y-h) on a unit fibre, both
  >= e^(-Q(y-h)) >= e^(-2 Q(y)) >= e^(-2V); slot change <= Lip(g) h <= b_k;
  P is the whole fibre; d_test = Q(y-h) - Q(y) >= -h Q'(y)/2. With
  V <= C_L Q(y): d_test/(V h) >= -Q'(y)/(2 C_L Q(y)) -> infinity. Correct.
- D-d1 (scope): V ~ Q(y_j) -> infinity is forced by the floor. At fixed V
  the floor e^(-2V) keeps y >= y_V > 0, where Lip(Q) is finite, so
  d_test <= C(V) h. Same reading as D-c1: the obstruction is to a constant
  linear in V.
- The sentence "This also applies to the edge profile of O 27216-27246
  (GCB6)" was NOT verified here (the short outline O is not on this
  machine; not fetched).

## Step 5. Common-interior contraction (section "A sufficient geometric estimate")

Verdict: HOLDS as stated (a conditional sufficient criterion).

- Hemisphere: v in S^m gives d(v, z^m) <= r_i, so d(v, z^l) <= r_i + h_i
  < pi/2; o_j has d(o_j, z^l) <= a_i - sigma_i < pi/2. The open hemisphere
  {x : x.z > 0} contains the short geodesic between two of its points
  (positive combinations). Correct.
- Convexity: for a great circle gamma of speed b, cos q = z.gamma gives
  sin q q'' = cos q (b^2 - q'^2), so q'' = cot q (b^2 - q'^2) >= 0 since
  |q'| <= b and cot q > 0 for 0 < q < pi/2; at q = 0 the kink is convex.
  Correct.
- The bound <= max(q, a_i): for q >= a_i the excess is
  -alpha q + (1-alpha) h + alpha (a - sigma) <= (1-alpha) h - alpha sigma <= 0
  iff alpha >= h/(sigma + h); for q < a_i the value is
  <= a + (1-alpha) h - alpha sigma <= a. Correct, and H_i nonincreasing with
  H_i = 1 on [0, a_i] gives target test >= source test. Correct.
- Jacobian: in polar coordinates about o, T: s -> (1-alpha) s with Haar
  density proportional to sin^2 s; Jacobian (1-alpha) sin^2((1-alpha)s)/sin^2 s
  >= (1-alpha)^3 since sin((1-alpha)s) >= (1-alpha) sin s on [0, pi]
  (concavity, sin 0 = 0). Note: the exponent is 3 because the Jacobian
  carries sin^2, i.e. the factor squared; the row's text "[sin((1-alpha)s)/sin s]^2"
  is right. Injective off the antipode of o (null). Correct.
- Two uses: F_P^m >= int over T(S^m) of Theta^m w^m = int over S^m of
  Theta^m(Tv) w^m(Tv) Jac >= e^(-B) F^m (target = source end, T(S^m) in P).
  For d_test, T(P) subset T(S^A) subset P; source A, target B with weights
  w^B on P subset S^B gives F_P^B >= e^(-B) F^H; exchanging the test roles
  gives F^H >= e^(-B) F_P^B. Correct; the weight inequality is used only on
  S^B for w^B, as assumed.
- Rate: alpha <= 1/2 gives -log(1-alpha) <= 2 alpha, so B <= (A + 6n) alpha.
  Correct.
- Falsifiability example (identical runs, caps at separation 2r - eps):
  with h = 0 the criterion holds with alpha = 0 but only with clearance
  sigma <= eps/2, so uniform *fractional* clearance fails while both costs
  are zero. Correct as stated ("strictly stronger than the requested
  bounds").
- D-e1 (open input, flagged by the row): the weight response A. For the
  stop weight e^(A^w) the response to moving every free link by
  alpha d(o_j, v_j) is of order alpha times the local Lipschitz constant of
  A^w on the fibre; that this is <= C_0 V uniformly in g (and not of order
  V / g^2) is the content of the open "weight response of a reopened fibre".
  Not a defect of the row; it is where the criterion is expensive.
- D-e2 (reinforcement of the row's caution): Y's window route as printed
  (Y 96968-97063, read here) pays each tile a constant factor C_win > 1
  ("as close to one as desired", aw:many-tile-windows), and its budget
  aw:window-budget is C e^(-C) 2^(-(k-j)), of order one at j = k. So
  as printed it gives an extensive constant loss, not O(V theta^k); a
  relative error proportional to theta^k is an extra input, as row 1412
  says. Y 130281-130320 (the move with the |s| <= 2 disc) and Y 134756-134801
  (C vartheta p_0^3, p_0^2; the row writes g_j, the source g_k) read and
  consistent.

## Step 6. Consequence for the consumer of check 1405

The identity log(F^B/F^A) = log(F^H/F_P^A) + log(F_P^B/F^H) + log(1+s^B)
- log(1+s^A) is exact (F^m = F_P^m (1 + s^m)). With B_rec = |first term| the
bound of check 1405 is B_rec + d_test + max_m log(1+s^m) + 2 C V r_K;
since the shells enter with opposite signs, |log(1+s^B) - log(1+s^A)|
<= max_m log(1+s^m). Correct.

Whether the printed bounds are shown insufficient. Yes, for the form the
consumer needs. Row 1391 (7.1, Row B outcome (2), table at L145) needs a
two-cutoff constant linear in V; with a constant e^(cV) the reach of the
carry is at most a multiple of (log K)^(1/4), i.e. V of order k. The example
lives at V ~ k^2 (smooth slot) and the Lipschitz variant at V ~ k / gamma,
both with V theta^k -> 0 and floors e^(-CV); the smooth one is inside the
regime V >> k the consumer needs beyond the reach of the e^(cV) constant.
So: the displayed stop estimates (slot bound, variation bound, modulus, mass
window) do not imply (SHELL) or d_test = O(V theta^k). What the example does
not show: insufficiency at fixed V with an e^(cV) constant (D-c1), nor any
property of a Wilson history (the row says so).

Signed increment. In the example the retained increment itself,
log(F^B/F^A) <= -143 T^2 + O(T), violates the rate; so no rearrangement of
the four terms (e.g. absorbing the slot into the weight, which moves d_test
into B_rec) escapes it. Correct as the row states.

Are the two proposed next rows the right ones? Yes, in this order, with
two amendments.

1. `gap-univk-stop-slot-identification` is decisive and cheap: Step 2 shows
   that if every interpolated small production slot is a native
   characteristic function, both shells and d_test vanish once
   (V+1) b_k < 1, which is the consumer's own regime (V theta^k small).
   Amendment (a): the row must also list every support decision that
   differs between the runs and is *not* among the slots interpolated by
   (m3) (the common-slot statement of item (a) claims the others are
   common; the row should confirm that against the pullbacks, since a
   changing decision outside the (m3) list has no slot bound at all).
   Amendment (b): if a slot is positive and nonconstant, record its
   regularity at the edge (Lipschitz, C^m, flat), because by Step 3 the
   regime in which the obstruction bites (V ~ k for Lipschitz, V/k -> infinity
   for flat) depends on it.
2. `gap-univk-conditioned-stop-window` is the right second row only if the
   first finds a positive varying slot. Amendment: its target is a
   *relative* window estimate at rate theta^k per read (Step 5 D-e2: Y's
   printed window gives a constant per tile), and it must include the
   weight response A of the reopened fibre (D-e1).

## Verdict

**HOLDS AFTER CORRECTION.** No mathematical step of row 1412 fails. The
corrections are of scope and wording. The first line needing correction is
the result paragraph's "the printed bounds do not give either rate" (row
1412, section "Result for row 1412", and the FINISH summary item (b)): it
holds for a constant linear in V in the regime V >> k, not at fixed V.

Decisive outcome. The printed bounds are shown insufficient for (SHELL) and
for d_test = O(V theta^k) in the form the consumer of check 1405 needs (an
extensive constant, row 1391 7.1). The two proposed next rows are the right
ones, in the proposed order, with the amendments of Step 6.

Defects, ranked by what each breaks (none breaks a proof):

1. D-c1. The counterexample (and Step 4's fixed-profile example) refutes
   only a constant linear in V, and only with V growing at least like k^2
   (smooth slot). At fixed V the example's own absolute bound pays both
   costs at M h e^(C_low V). It is a geometric instance of row 1391
   Remark 7.1 and should cite it. Breaks: the unqualified wording of the
   result.
2. D-c2 (strengthening). A Lipschitz slot profile gives the shell obstruction
   with floors already at V ~ k/gamma; for a C-infinity slot floors force
   V/k -> infinity. So the slot's edge regularity decides the regime; row 1
   should record it.
3. Next-row amendment (a): changing support decisions outside the (m3) slot
   list have no printed slot bound and must be listed by row 1.
4. D-e2. Y's printed window route gives a constant loss per tile, not
   O(theta^k); the second row's target must be relative at rate theta^k.
5. D-e1. The weight response A of the contraction is the expensive open
   input (uniformity in g).
6. D-c3 (wording). The example satisfies the displayed stop estimates and
   the mass window, not the whole of item (a) of III 17642-17652.
7. D-b1 (scope). The binary-slot statement covers the small production slots
   of (m3) only.
8. D-d1. GCB6 claim (O 27216-27246) not verified here (O not on this
   machine).

Not checked: the citations to CA-I, CA-II and the short outline O (not on
this machine; not fetched, as the verdict does not depend on them); the
row's "Repo search" section. Checked against source: III 11806-11870,
12142, 17630-17700; Y 96968-97063, 130281-130320, 134700-134810; rows 1391
(7.1, L145, L224), 1404 (5.4, L125-126), check 1405 (L10, L46-48).

No numeric job was run; all checks are by hand. Finished 2026-11-23T00:03Z (date -u).

RESULT: Check 1416 of row 1412: HOLDS AFTER CORRECTION. Verified by hand: the binary-slot statement ((V+1) b_k < 1 forces agreement; b_k < 1 alone excludes switching off), the one-link SU(2) counterexample (Haar masses, S^B in S^A, mu(P) <= C t, s^A >= c h^(-4.84), d_test >= 143 T^2 - 24 T - C, floors, added labels), the fixed-profile drift, and the common-interior contraction (convexity, Jacobian (1-alpha)^3, injectivity, both uses). Correction: the examples refute only a constant linear in V (V ~ k^2; at fixed V the absolute bound pays both costs with e^(CV)), an instance of row 1391 Remark 7.1, which is the form the consumer needs; a Lipschitz slot gives the shell obstruction already at V ~ k. Printed bounds are insufficient for (SHELL) and d_test at the extensive rate; the two proposed rows are right in order, amended to list changing decisions outside the (m3) slots and the slot's edge regularity, and to target a relative window at rate theta^k. (SHELL), d_test, and the weight response of a reopened fibre stay OPEN.
