lead: anthropic/claude-opus-5-5/max laptop-subagent
row: 1075

# Check of row 1072 (gap-bridge-exercise-opus.md), line by line

Provenance: row 1072 was written by Claude Opus 5.5 high. This check is
by Claude Opus 5.5 (max effort, laptop subagent). Same provider. This is
a same-provider check, not an independent check.

## Plan (at most eight steps; one step per response; results appended below)

1. Read FINISH row 1075 and record its exact instructions here.
2. Read the file under check in full; list its numbered claims.
3. Check claims, first block (line by line).
4. Check claims, second block (line by line).
5. Check claims, third block (line by line).
6. Check every cited source inside this checkout (quote the line used).
7. Recheck any FAILS or corrections; scope every negative.
8. Verdict table and RESULT line.

The plan may be refined after step 1; the refined plan is recorded in step 1.

## Step results

### Step 1. Row 1075 as written (FINISH.md line 1156), and the refined plan

Row 1075 asks for a check of row 1072 by Claude Opus 5.5 max, same provider
as the author, run at the same time as row 1074, without reading row 1074's
file. It says: follow work item 1 of section 8.7 of
`library/gap-bridge-exercise-opus.md` exactly. The items to check line by line:

- (i) Remark RP-ANI;
- (ii) Lemma MON-T and Corollary NO-MON (step 3.1);
- (iii) Lemma CONT and C4-C5 (3.2);
- (iv) Proposition CA-FAIL with its precision (6c and the head of step 7);
- (v) the U(1)-range correction (6c);
- (vi) row 10 of 6d;
- (vii) Lemma MON-L-cov FALSE and the (MON-L) class argument (7.3);
- (viii) Lemma LIN-perp (7.4);
- (ix) the kill table 7.2 with the verdicts on BR-2 (wounded) and BR-3
  (blocked-stronger).

Files to read: the file under check; `library/gap-aniso-trajectory.md`
L166-203 (Claim S2); `parts/gap.md` L223 and L231; the reading
`library/prior/gap-bridge-read-luna.md` (row 1073).

Tests first: (T1) the Schur step and the analytic-zero step in MON-T;
(T2) whether the Frohlich-Simon-Spencer threshold for three-dimensional O(4)
in the normalization beta s.s' is below 2.3 (the author recalled 1.01; read
an open copy); (T3) whether the lane's Theorem D2 already contains CA-FAIL.

Verdicts: HOLDS, HOLDS AFTER CORRECTION (with the text), FAILS (with the
first failing line). No new attack. Lean-formalizable proofs only; no
computer-assisted proof. End with one RESULT line.

Refined plan (replaces the plan above; still eight steps):

1. Row 1075 recorded (this step).
2. Read the file under check in full, and the file list (trajectory L166-203,
   parts/gap.md L223 and L231, row 1073's reading). List the items.
3. Test T1: the Schur step and the analytic-zero step in MON-T; then
   Corollary NO-MON and Remark RP-ANI.
4. Test T2: read an open copy of Frohlich-Simon-Spencer 1976; check the
   threshold in the normalization beta s.s'. Then Proposition CA-FAIL with
   its precision and the U(1)-range correction (6c, head of step 7).
5. Test T3: does the lane's Theorem D2 already contain CA-FAIL. Then Lemma
   CONT and C4-C5 (3.2) and row 10 of 6d.
6. Lemma MON-L-cov FALSE and the (MON-L) class argument (7.3); Lemma LIN-perp
   (7.4).
7. Kill table 7.2 and the verdicts on BR-2 and BR-3.
8. Verdict table and RESULT line.

### Step 2. What was read, and the items under check

Read in full: `library/gap-bridge-exercise-opus.md` (row 1072), 506 lines,
86437 bytes, L1-506. Read: `library/gap-aniso-trajectory.md` L166-203
(Lemma PERP, Claim S2 and their proofs); `library/prior/gap-bridge-read-luna.md`
(row 1073), 71 lines, in full.

Line numbers of `parts/gap.md`. The checkout HEAD is 5113576a3. Row 1072
worked at 6a6f2701a (its header). Commit 5113576a3 changed `parts/gap.md`
(+3 -2), which moved the test table down one line. At 6a6f2701a, L223 is the
row "Compact U(1), Coulomb phase" and L231 is the row "Theorem D2; Lemma
SUB". At HEAD they are L224 and L232. Both rows are unchanged in text. So the
citations in row 1072 are right for its commit. The U(1) row says, in part:
"in the lane for Villain at beta >= 2^14 (row 786, per exercise 2). At beta of
order 1 to a few it is a BELIEF." The D2 row says: "not a model: a theorem
that a form of hypothesis is false (supremum over tilts)", binding "beta above
4 G_S (1.07 on side 4)".

Items under check, with their lines in row 1072's file:

| Item | Lines |
|---|---|
| Remark RP-ANI (and C1) | L119, L160 |
| Lemma MON-T | L121-127 |
| Corollary NO-MON and its reading line | L129-130 |
| Lemma CONT, Q_fix, Q_some, C4, C5 | L134-140, L163-164 |
| Proposition CA-FAIL, proof, "Meaning" | L337-339 |
| Precision to CA-FAIL ("head of step 7") | L368 |
| Correction of the U(1) range | L341 (and 8.3, L470) |
| 6d row 10 (method 27) | L356 (and 8.3, L472) |
| Lemma MON-L-cov FALSE | L412-414 |
| The (MON-L) class argument | L416 |
| The face paragraph that uses CA-FAIL | L418 |
| Lemma LIN-perp | L428 |
| Kill table 7.2; verdicts on BR-2 and BR-3 | L393-404, L420, L430-432 |

### Step 3. Test T1 (MON-T), then Corollary NO-MON and Remark RP-ANI

**Input check: Claim S2 (row 1066 L186-201), as MON-T uses it.** Re-derived
by hand. First order vanishes (flip of sheet 3, a symmetry of the sheet law,
makes x_p odd). Pairs (p, q) with q not p vanish (flip a link of q outside the
boundary of p). Pairs without p vanish by the term-by-term splitting in the
proof of Lemma PERP (two transverse plaquettes share at most one link). Then
kappa_0(F, H, x, x') = E_0[F~ H~ x x'], since all odd moments in x vanish and
Cov_0(F, H) = 0. E over sheets 3 and 4 of x(u) x(u') = (c/4) <M(u), M(u')>,
because E[N(u) (x) N(u')] commutes with the SO(4) action N to g N h (left
invariance of sheet 4, right invariance of sheet 3; SO(4) acts absolutely
irreducibly on R^4), and c = G(u, u')^2. Collecting (1/2)(1/4)(1/2) = 1/16
gives Claim S2's formula. HOLDS (agrees with row 1070).

**T1(a), the Schur step. HOLDS.** Line by line:
- The anchor law E_0 is a product of sheet laws on a finite free box; each is
  invariant under Phi to g Phi h for constant g, h in SU(2). True on free
  boxes (the weight depends on Phi(u) Phi(v)^(-1) only up to conjugation by g,
  and the trace removes it). Pins would break this; MON-T is stated on free
  boxes.
- F = (1/2) tr(Phi_1(a) Phi_1(b)^(-1)) is invariant under Phi_1 to Phi_1 h;
  Phi_1(u')^(-1) Phi_1(u) goes to h^(-1)(...)h. So A = h^(-1) A h for all h.
  True.
- A = E_0[F~ Phi_1(u')^(-1) Phi_1(u)] with F~ real, so A lies in the closed
  real span of SU(2), which is the quaternion algebra H. The centre of H is R.
  So A = kappa_1 I, kappa_1 = (1/2) tr A = Cov_0(F, e_uu') (cyclicity of the
  trace). True.
- B = kappa_2 I by left invariance (Phi_2 to g Phi_2 fixes H and conjugates
  Phi_2(u) Phi_2(u')^(-1)). True.
- kappa_1 = kappa_2: F and H are the same function (e_ab) of two sheets with
  the same law; e_uu' is the same function. True.
- tr(A B) = 2 kappa^2, so c_2 = (1/16) sum G^2 (2 kappa^2) = (1/8) sum G^2
  kappa^2, every term >= 0 (G and kappa are real). True.
- The term (u, u') = (a, b): kappa(a, b) = Var_0(e_ab) > 0, since e_ab is
  non-constant under Haar measure (it is the real part a_0 of a uniform point
  of S^3) and the sheet law has a positive density. True.

**T1(b), the analytic-zero step. HOLDS.** On a finite box, E_0[e_ab] is a
ratio of two entire functions of beta_M with a positive denominator on R, so
it is real-analytic on R. Its expansion at 0: E_0[e_ab] = beta_M sum_c
Cov_Haar(e_ab, e_c) + O(beta_M^2). For a bond c other than (a, b) the Haar
covariance is 0 (integrate out a site of (a, b) not in c, or a site of c not
in (a, b); E_Haar[Phi] = 0). For c = (a, b) it is E_Haar[((1/2) tr U)^2] = 1/4
(Haar density (2/pi) sin^2 theta for (1/2) tr U = cos theta; the integral of
cos^2 sin^2 over [0, pi] is pi/8). So G(a, b) = beta_M/4 + O(beta_M^2): not
identically zero, hence its zeros in R are isolated. Off them c_2 >= (1/8)
G(a, b)^2 kappa(a, b)^2 > 0. Then Cov_t = c_2 t^2 + O(t^3) with Cov_0 = 0.

Remark (not a correction). The discrete exceptional set depends on the box
and the bond. Corollary NO-MON (i) needs one box per beta_M. On the box with
Lambda_long = {a, b} (one bond), G(a, b) = d/d beta_M log Z(beta_M) > 0 for
every beta_M > 0 (log Z is strictly convex with derivative 0 at 0). So the
corollary holds for every beta_M > 0, with that box.

**Lean form.** Schur for H (centre of the quaternions is R), the isolated-zero
lemma for real-analytic functions, the Haar moment 1/4, and Claim S2. All are
finite-dimensional integrals and algebra. Formalizable as stated.

**Lemma MON-T: HOLDS** (PROVED on finite free boxes, given Claim S2).

**Corollary NO-MON.**
- (i) HOLDS. Cov_0 = 0 and Cov_t = c_2 t^2 + O(t^3), c_2 > 0, so abs(Cov)
  strictly increases on some (0, t_1]. The statement is on the face, on finite
  boxes, for the pair (F, H): that is how it is written.
- (ii) HOLDS AFTER CORRECTION. The step "beta_T <= eps X(beta_M)^(-2) <= eps,
  since X >= 1" uses X >= 1. Row 1066 L76 defines X by (MIX) and gives only
  X >= xi_2; X >= 1 is not part of the definition. The conclusion does not
  need it. Corrected text: "A point P' of R_eps that dominates (beta, beta,
  beta) has beta_M(P') >= beta and beta_T(P') >= beta. In R_eps, beta_T(P') <=
  eps X(beta_M(P'))^(-2). So no point of R_eps dominates a window point once
  eps < beta inf_{beta_M >= beta} X(beta_M)^2; with X >= 1 on beta_M >= 2.3
  (expected, as X >= xi_2 and the sheet length is large there; not proved
  here) this is eps < 2.3."
- Reading line (L130). HOLDS with one precision on scope. R_eps and the window
  are not ordered coordinatewise in either direction (R_eps has beta_L >= 1/eps
  when X >= 1, the window has beta_L = beta). So a comparison bridge needs
  mixed signs: correlations non-decreasing in beta_L and non-increasing in
  beta_T. MON-T refutes the beta_T half at the anchor, on the face. A
  mixed-sign principle claimed only at finite beta_L is not refuted by MON-T:
  at finite beta_L and beta_T = 0, Cov(F, H) need not vanish (F and H share
  the longitudinal link at transverse site x + e_2), and its sign is not
  known. So "it cannot use R_eps" holds for principles that hold on the face
  (beta_L = infinity is in R_eps's closure, and the anchor is used as the
  start). The scope line of 8.8 ("for coordinatewise comparisons, with the
  reverse direction refuted for one pair on finite boxes") already says this.
- "Group-blind (U(1) gives the same sign ...; ARGUED)". HOLDS as ARGUED.
  Checked by hand: for plane-rotator sheets, x_p = cos(theta_1 + theta_2 -
  theta_3 - theta_4), E over sheets 3, 4 of x x' = (G^2/2) cos(M - M'), and
  kappa_0(F, H, x, x') = (G^2/2) kappa^2, so c_2 = (1/4) sum G^2 kappa^2 >= 0.
  Precision: for U(1) the reality of A comes from the reflection theta to
  -theta (U(1) is abelian, so invariance alone does not force A real), not
  from Schur; the constant is 1/4, not 1/8.

**Remark RP-ANI. HOLDS** (given I12, the Osterwalder-Seiler theorem, recalled
by the author and by me; row 1073 read only the abstract, which states a
positive self-adjoint transfer matrix from reflection positivity). Line by
line: a reflection orthogonal to axis mu maps a plaquette in plane (mu, nu) to
a plaquette in plane (mu, nu), and a plaquette in a plane without mu to one in
the same plane. So types L, M, T are preserved, and the couplings are
theta-invariant. Link reflection: the crossing plaquettes lie in planes (mu,
nu); after the usual gauge fixing of the crossing links each gives a term of
the form sum_i B_i theta(B_i) with coefficient beta_type(mu, nu) >= 0. Site
reflection: no plaquette crosses; the plaquettes inside the hyperplane have
real theta-invariant weights e^(beta_type x_p) = f theta(f) with f = e^(beta_type
x_p / 2). Both arguments use only non-negative, theta-invariant
coefficients. Precision for the "Consequence" line: positivity of the transfer
matrix itself comes from link reflections; site reflections give it for the
square of the one-step operator. The consequence as written (positive transfer
matrices at every point) stands with link reflections. C1 HOLDS.

### Step 4. Test T2 (the FSS threshold), Proposition CA-FAIL with its precision, the U(1)-range correction

**Sources tried.** Frohlich, Simon and Spencer, Comm. Math. Phys. 50 (1976)
79-95. Project Euclid (/tmp/fss1976.bO9vJE) and the publisher
(/tmp/fss1976s.Jt7nRX) both returned a bot challenge page, not the paper.
Neither was bypassed. So the original was NOT read. Open copy read instead:
R. Peled and Y. Spinka, "Lectures on the spin and loop O(n) models",
arXiv:1708.00058, LaTeX source fetched into the new empty folder
/tmp/peledspinka.HDEdiw, read with grep and sed only (no code run from it).
Its section "Long-range order in dimensions d >= 3 - the infra-red bound"
reproduces the FSS argument and cites FSS 1976. Nothing downloaded is
committed.

**What the open copy states (read).** Model (their eq. (2.1)): density
proportional to exp(beta sum over edges <sigma_u, sigma_v>), sigma uniform
on S^(n-1). This is the normalization beta s.s'. Infrared bound:
E|sigma-hat^j_k|^2 <= |Lambda|/(beta lambda_k), lambda_k = 2 sum_j (1 - cos
k_j), for k not 0. Theorem (long-range order): for every d, n, beta,
liminf over L of |Lambda|^(-2) sum_{x,y} E<sigma_x, sigma_y> >= 1 - (n/(2 beta))
int_{[0,1]^d} dt / sum_j (1 - cos(pi t_j)).

**The number.** For d = 3 the integral is Watson's integral W_3 =
(1/pi^3) int_{[0,pi]^3} d theta / (3 - sum cos theta_j) = 0.505462.
(Published closed form: W_3 = u/3 with u = 1.516386..., the simple-cubic
Green's function at the origin; Watson 1939.) GUIDE check, scratchpad script
`watson.py`, Python -I, one thread: the Bessel form int_0^infinity (e^(-t)
I_0(t))^3 dt gives 0.5054620. So the bound is positive for beta > n W_3 / 2:
n = 4 gives **beta_FSS = 2 W_3 = 1.0109**; n = 2 gives 0.5055. The author's
recalled "about 1.01" is right. 1.0109 < 2.3. **T2: HOLDS** (threshold read
in an open secondary copy that follows FSS; the original not read).

Note on the identification. In CA-FAIL the conditional law is exp(beta sum
(1/2) tr(Phi(x) Phi(y)^(-1))) times Haar on SU(2). Haar measure on SU(2) is
the uniform measure on S^3, and (1/2) tr(a b^(-1)) = a.b for unit
quaternions. So the slab law is exactly the model above with n = 4 and the
same beta. Checked.

**Proposition CA-FAIL, line by line.**
- Plaquettes meeting V: a temporal link between slices t and t+1 lies only in
  the (0, i) plaquettes of that slab. With the spatial links of both slices
  pinned to 1, U_P = Phi(x) Phi(x + e_i)^(-1). True.
- Conditional law = 3D O(4) at coupling beta: true (above).
- Periodic slices: the torus law is the model of the theorem; LRO holds for
  beta > 1.0109 uniformly in L. True, with the threshold read.
- "So the conditional covariance of Phi(x).Phi(y) does not decay": true in
  the averaged sense the theorem gives (the torus average of E<Phi(0),
  Phi(y)> is at least c > 0, and E Phi = 0 by symmetry). A bound C e^(-m
  abs(x - y)) uniform in L would make that average tend to 0. True.
- The periodic box is not a finite subset of Z^4. The precision paragraph
  (L368) handles this. Checked: with V the temporal links over a 3D box
  Lambda in the slab, all other links fixed, the conditional law is 3D O(4)
  on Lambda with an arbitrary boundary condition (any outside temporal links
  can be chosen). Non-uniqueness of the infinite-volume 3D O(4) Gibbs
  measure at beta > 1.0109: for every R and L >= R, the box average
  |B_R|^(-2) sum_{x,y in B_R} E_L<sigma_x, sigma_y> >= c, because every torus
  Fourier coefficient of the two-point function is >= 0, so the box average is
  at least the k = 0 term. This passes to every limit state. A unique Gibbs
  state is the limit of the torus states, is O(4)-invariant (mean 0) and is
  extremal, hence tail-trivial, hence mixing; then the box averages tend to 0.
  Contradiction. Uniform weak mixing over finite volumes and boundary
  conditions implies uniqueness. So it fails. True.
- "Hence complete analyticity ... fails": true for every complete-analyticity
  or finite-size condition that implies weak mixing uniform over finite V and
  boundary conditions (contraposition).

Corrections to CA-FAIL (wording; the mathematics stands):
- (a) Row 1073 read Dobrushin and Shlosman's setup as finite-range, finite
  spin; the file accepts this in 8.3. So "complete analyticity in the
  Dobrushin-Shlosman sense" is not defined for SU(2) links. Corrected text:
  "Hence every complete-analyticity or finite-size condition, for compact
  continuous spins, that implies weak mixing uniform over all finite volumes
  and boundary conditions fails at every beta > 1.0109, so at every window
  coupling. For finite spins this includes Dobrushin-Shlosman complete
  analyticity."
- (b) The precision's phrase "contradicting a non-zero limit of the two-point
  function" should read "contradicting the lower bound c on box averages of
  the two-point function, which passes to limit states because all torus
  Fourier coefficients are non-negative". FSS gives an averaged bound, not a
  pointwise limit.
- (c) "the lane's D2 threshold 1.07 on side 4 is of the same kind": corrected
  in step 5 (test T3).

**The "Meaning" paragraph (L339) and its use in 7.3 (L418).** HOLDS as
written ("for boundary data in u"), with a precision on scope. In the sheet
form of the face (longitudinal links gauge-fixed to 1), the variables are the
sheets Phi_l(u). Pins in u leave sheets at other u, so no slab appears: true.
But pins of whole sheets are transverse data, and they do produce the device
on the face. Pin the e_2-sheets of two adjacent transverse rows x_3 = s and
s + 1 to 1. The free e_3-sheets between them carry exactly the 3D O(4) model
on (u_0, u_1, x_2) with couplings (beta_M, beta_M, beta_T): each sheet keeps
its M-plaquettes, and the two T-plaquettes at each u become Phi_(x_2)(u) .
Phi_(x_2 + 1)(u). At (infinity, beta, beta) with beta > 1.0109 and infinite
transverse extent this model has long-range order. On a transverse torus
Z_T^2 and a u-torus Z_L^2 it is the 3D O(4) model on Z_L^2 x Z_T; at L = T
it is the 3D torus, which has long-range order (FSS), so no mixing bound
holds uniformly in T and L together. Corrected text for L339 and L418: "On
the face the obstruction is absent for boundary data in u. It is present for
transverse data (pins of whole sheets): in infinite transverse volume, and on
tori without uniformity in T and L together. So a face finite-size argument
may be uniform over u-boundary data only, with the transverse directions
periodic and unpinned."
This narrows the "structural point in favour of the face"; it does not
remove it.

**Correction of the U(1) range (L341). HOLDS.** Checked against its sources:
Proposition U1-BR (row 1066 L221-223) quantifies over "each isotropic point
(beta, beta, beta)" and uses (F3) "at beta at least 2^14 (Villain form)". The
lane's test table at 6a6f2701a, L223, says "in the lane for Villain at beta >=
2^14 ... At beta of order 1 to a few it is a BELIEF" and "theorem-grade at
very large beta only". So a carry with endpoints in the window is bound by
U(1) at belief grade only. The reading is right and is the table's own range.
One precision: "U(1) near 1.01" is the Wilson-action transition (numerics);
the theorem range 2^14 is for the Villain action. Both put the window in the
U(1) Coulomb phase at belief grade, so the conclusion is unchanged.

### Step 5. Test T3 (does Theorem D2 contain CA-FAIL), Lemma CONT and C4-C5, 6d row 10

**T3. Answer: Theorem D2 does not contain CA-FAIL; Lemma SLAB of row 1013
contains its mechanism and its conclusion in qualitative form.**
- Theorem D2 (row 977, `library/gap-tiltproof-max.md` L240-253, read). It is
  Gaussian domination on the pinned sheet: slices 0 and 1 with transverse links
  pinned, sheet variables P_k(y) on a 2D plane (directions 2, 3), E(p) = 2 -
  cos p_2 - cos p_3. It bounds the zero-mode variance on a periodic box of
  side S: G-hat(0) >= A (1/4 - G_S/beta), with G_S about (1/(2 pi)) log S +
  0.0488 (G_4 = 103/384; G_120 = 0.81072). It refutes a hypothesis with a
  supremum over tilts, (TILT-COV-sup), on boxes of given side. Its threshold
  4 G_S grows with the side (1.07 on side 4, 3.24 on side 120 for Low = {0}).
  A 2D sheet has no long-range order in infinite volume. So D2 gives no
  statement uniform over volumes, and no non-uniqueness. It does not imply
  CA-FAIL.
- Lemma SLAB (row 1013, `library/gap-invent-selective-max.md` L220-226,
  read; kill-sheet entry K3', L57). It pins two neighbouring hyperplanes;
  the links between carry "exactly the three-dimensional O(4) spin model with
  weight exp(beta q.q')". Its consequence, marked there "ARGUED, given a
  RECALLED theorem": "at weak coupling a family of conditional laws that
  contains 'given two neighbouring hyperplanes' has no uniform mixing". It
  says "for large beta" and gives no threshold. Row 1013 is unchecked.
- So CA-FAIL = Lemma SLAB + the explicit range beta > 2 W_3 = 1.0109 (FSS's
  constant, read in step 4) + the open-slab and non-uniqueness precision + the
  application to complete-analyticity and finite-size carriers. The file
  credits this ("it is the slab device K3' of row 1013 applied to complete
  analyticity", L337). What is new in row 1072 is the explicit range covering
  the window and the application; the device and the no-uniform-mixing
  conclusion were on file.

Corrections from T3:
- L337, "the lane's D2 threshold 1.07 on side 4 is of the same kind". Corrected
  text: "The lane's D2 threshold 4 G_S (1.07 on side 4) comes from the same
  Gaussian domination on a two-dimensional pinned sheet; it grows like (2/pi)
  log S with the side and gives no infinite-volume statement. The
  three-dimensional device is Lemma SLAB (row 1013); with FSS's constant it
  binds for beta > 2 W_3 = 1.0109, uniformly in the side."
- 6c table, row "Theorem D2, Lemma SUB, slab device K3'": the "Binds from"
  cell gives D2's threshold for all three. Corrected: D2 and SUB bind
  statements with a supremum over tilts, from beta > 4 G_S (side-dependent);
  K3' (Lemma SLAB) binds families closed under conditioning on two
  neighbouring hyperplanes, from beta > 1.0109 (FSS), every side.
- RESULT line of row 1072: "Proposition CA-FAIL given Frohlich-Simon-Spencer"
  should name its source in the lane. Corrected: "Proposition CA-FAIL (Lemma
  SLAB of row 1013 made explicit: FSS's threshold 1.0109 covers the window;
  applied to complete-analyticity carriers)".

**Lemma CONT (L134). HOLDS.** S open and closed in [0, 1] and 0 in S give S =
[0, 1] by connectedness. Lean form: `IsClopen` and `isPreconnected` of the
unit interval.

**Q_fix (L137). HOLDS as ARGUED.** Closedness given uniqueness at the limit
point: weak limits of Gibbs states at P(t_n) are Gibbs states at P(t) (finite
range, couplings converge, continuous specification); covariances of local
observables are continuous in the weak topology; so the bound passes, and with
uniqueness it covers every limit state. The uniqueness hypothesis is stated.
Right.

**Q_some (L138). HOLDS AFTER CORRECTION.** "Openness can come from a strict
finite-box criterion (I13 ...)". After CA-FAIL, a finite-box criterion that
implies mixing uniform over boundary conditions is false at the window. The
file corrects route RC in 8.3 but not this line. Corrected text: "Openness can
come from a strict finite-box criterion of the constant-coupling kind (the
lane's Theorem S on periodic boxes): a condition at one size L is a continuous
function of the couplings, so its strict form is open. Criteria that imply
mixing uniform over boundary conditions are false at the window (CA-FAIL)."

**C4 (L163). HOLDS AFTER CORRECTION (marks).** "C4 (PROVED, Lemma CONT):
every path bridge is a continuity argument; one of openness or closedness
carries the whole content." Lemma CONT is proved. The rest is not a theorem.
That every path bridge has this form is true trivially: any proof that Q
holds on [0, 1] makes S = [0, 1], which is open and closed. So the frame
alone says nothing. That one of openness and closedness carries all the
content is ARGUED for Q_fix and Q_some only. Corrected text: "C4 (Lemma CONT
PROVED; the rest a reading): every path bridge can be written as a continuity
argument; for Q_fix the content is openness (an improvement estimate), for
Q_some it is closedness (constants bounded along the path) (ARGUED)."

**C5 (L164). HOLDS AFTER CORRECTION.** Two corrections that the file makes
later (5.1 corrections, 6c) are not carried back to C5, and C5 is quoted in 8.2.
Corrected text: "C5 (ARGUED from C4, I4-I6, I11, I18): the content is an a
priori estimate excluding gap closing along the path. It must read the group:
at theorem grade for path classes reaching isotropic beta >= 2^14 (U(1),
Villain), at belief grade for paths ending in the window (6c). It must read
the dimension (five dimensions, belief grade). A start from the anchor helps
only if the carry's proof uses the start's SU(2) data (step 5 correction);
the dimension must be read in the carry."

**6d row 10 (L356; method 27). HOLDS AFTER CORRECTION.** Source checked: row
998 L507 gives method 27 as "The beta_t path from zero temporal coupling
(Identity G) | needs three-dimensional mixing and (NOCRIT)". At beta_t = 0 the
4D model is a stack of 3D slices, so "3D mixing" is the 1 + 3 start. The
re-judgment (the start premise is split-specific) is right. One part is
incomplete: "carry premise unchanged". In the 2 + 2 split one coupling at 0
does not decouple the model: beta_T = 0 at finite beta_L is the
transverse-lattice point of BR-9, with no posted input. The decoupled start
is the corner beta_L = infinity, beta_T = 0. So a 2 + 2 version of method 27
needs a second carry, in beta_L, that the 1 + 3 version does not have.
Corrected text for the last cell: "method 27 with the 2 + 2 anchor: start
premise changed (posted 2D theorems plus (S)); carry premise (NOCRIT)-type
along beta_T, plus a carry in beta_L from infinity that the 1 + 3 version does
not need." The same correction applies to 8.3, L472.

### Step 6. Lemma MON-L-cov FALSE and the (MON-L) class argument (7.3); Lemma LIN-perp (7.4)

**Lemma MON-L-cov FALSE (L412-413). HOLDS.** Line by line:
- On the face every L-plaquette is the identity (Lemma FACE-LIM: in-plane
  links pure gauge), so x_p = 1 and Var(x_p) = 0 there. True.
- At finite beta_L, on a finite box, x_p has a law with a positive density, so
  Var(x_p) > 0. True.
- Infinite volume: given all other links, the law of one link U in p has a
  density rho on SU(2) with e^(-2 s) <= rho <= e^(2 s), s the sum of the
  couplings of the six plaquettes that contain U. Then Var(x_p | rest) >=
  e^(-2 s) Var_Haar((1/2) tr(U W)) = e^(-2 s)/4 (Haar invariance), so Var(x_p)
  >= e^(-2 s)/4 in every Gibbs state (DLR). True; the file's "bounded below by
  e^(-c beta)" is this bound with c beta = 2 s.
- So abs(Cov(x_p, x_p)) at (beta_L, beta, beta) exceeds its face value 0. The
  universal covariance form is false. True.

Precision on the next line (L414), "So (ii) can only be a statement about the
rate". The lemma refutes the covariance form quantified over all pairs. It
does not refute covariance forms restricted to observables that are not frozen
on the face, or normalized forms. Corrected text: "So (ii) cannot be the
covariance form for all pairs; the form kept here is the rate form (MON-L)".

**The (MON-L) class argument (L416). HOLDS AFTER CORRECTION (sources and
grade).** Line by line:
- "(MON-L) is a sign of d m/d beta_L". Precision: a sign d m/d beta_L <= 0 on
  [beta, infinity) implies (MON-L); (MON-L) compares each point with the face
  value only and is weaker. The kinship with route RB stands.
- "parts/gap.md L181: 'a sign with no small number; false in the class'". At
  6a6f2701a, L181 reads "| 5 | RB, sign in beta | stronger |
  blocked-equivalent | Theorem D (f) | as RA | L678 |". The quoted words are
  not there. They are in `library/gap-part-draft.md` L158 ("a sign with no
  small number; false in the class (exercise 2, 6a row 5)"). Citation to fix.
- The 3D Z_2 example. Wegner duality: Z_2 gauge coupling beta corresponds to
  Ising coupling K* with tanh K* = e^(-2 beta). Small beta (confined) is the
  Ising low-temperature side; large beta is the high-temperature side. The
  file attributes "positive again above it" to "exponential decay of truncated
  correlations of the low-temperature Ising model ... Duminil-Copin, Goswami and
  Raoufi". That is the wrong side: DGR's low-temperature result covers gauge
  beta < beta_c; gauge beta > beta_c is the Ising high-temperature phase
  (Aizenman, Barsky and Fernandez; Duminil-Copin and Tassion). Also, Aizenman,
  Duminil-Copin and Sidoravicius prove continuity of the 3D Ising spontaneous
  magnetization at the critical point; that is not the statement that the
  gauge gap tends to zero there. The gauge gap is the decay rate of Ising
  energy-energy correlations; its vanishing at beta_c is not proved by the
  cited results and is a BELIEF here. All three sources are recalled by the
  author and by me, not read.
- Without the vanishing at beta_c the example shows only that the gap is
  positive on both sides, which refutes no monotone statement.
- The lane already has a class example for this kind of sign statement:
  exercise 2 (row 878) 6a row 5, "(MONO-Delta) | false for the ordered Ising
  model, so not a property of the class", at GUIDE grade (exact transfer
  matrices), and 6d row 5, "it says a proof must be selective, not that the
  statement is false for SU(2)".
- Corrected text: "A gap need not be monotone in a coupling. The lane's class
  example is the ordered Ising model (row 878, 6a row 5; GUIDE). In the 3D Z_2
  gauge model (dual to 3D Ising, Wegner) the gap is positive for beta below
  beta_c (dual Ising low-temperature phase; Duminil-Copin, Goswami and Raoufi)
  and above it (dual high-temperature phase; Aizenman, Barsky and Fernandez;
  Duminil-Copin and Tassion), and is believed to vanish at beta_c (not the
  content of Aizenman, Duminil-Copin and Sidoravicius, who prove continuity of
  the magnetization). So a class-wide monotone gap statement is false at GUIDE
  grade, and a proof of (MON-L) must be selective (ARGUED)."
- The five-dimensional sentence: conditional ("if the 2 + 3 face at (infinity,
  beta, beta) is gapped"), and the face's status is stated as open. HOLDS as
  written.

**Lemma LIN-perp (L428). HOLDS AFTER CORRECTION (scope and the needed
facts).** Line by line:
- "by Lemma PERP the transverse covariance at transverse distance d is
  O(t^d)": true on each finite box; the constants depend on the box (row 1066
  L184, remark 2).
- "by Lemma MON-T it is of exact order t^2 at the first step for the pair
  (F, H)": true on finite boxes (step 3).
- "So on finite boxes the transverse decay per unit transverse step is of
  order log(1/t)": not shown beyond the first step. PERP gives an upper bound
  with box-dependent constants; MON-T a lower bound at d = 1 only. On a finite
  box an asymptotic rate is not defined.
- "the transverse rate is infinite at t = 0 and finite for t > 0": infinite at
  t = 0 is exact (product measure). Finite for t > 0 is not proved here (it
  needs a lower bound at all transverse distances). It is expected; at the
  window m_perp = m_par by the lattice symmetry.
- "d log m_perp/dt is unbounded as t to 0": this needs m_perp(t) to tend to
  infinity as t decreases to 0. That follows from (S-q) only if (S-q) holds for
  every small eps with C independent of eps (row 1066 states (S) for some eps).
  Otherwise m_perp may jump at t = 0, and the conclusion still holds in the
  weaker form below.
- The conclusion (state (LIN-path) for the longitudinal gap) is right in every
  case: a law -d log m/dt <= C cannot start from m(0) = infinity.
- Corrected text: "Lemma LIN-perp (ARGUED). At t = beta_T = 0 the sheets are
  independent, so m_perp = infinity there. If m_perp is finite at some point
  of the path, no law -d log m_perp/dt <= C can carry m_perp from t = 0: either
  m_perp jumps at 0, or (if (S-q) holds for every small eps with C free of eps)
  m_perp(t) tends to infinity as t decreases to 0 and its log-derivative is
  unbounded. Inputs: Lemmas PERP and MON-T on finite boxes; the rate statement
  is an infinite-volume one. So (LIN-path) is stated for the longitudinal gap,
  as in its definition (or for min(m_par, m_perp), which equals m_par near the
  anchor)."

### Step 7. Kill table 7.2, and the verdicts on BR-2 (wounded) and BR-3 (blocked-stronger)

**A structural fact the table does not state.** BR-2 and BR-3 use the two
orders of the same two moves on the rectangle with corners (infinity, beta,
0) and (beta, beta, beta):
- BR-2: beta_T from 0 to beta at beta_L = infinity (the face path), then
  beta_L from infinity to beta at beta_T = beta.
- BR-3 (path of 7.4): beta_L from infinity to beta at beta_T = 0, then beta_T
  from 0 to beta at beta_L = beta.
In both, the beta_L move is believed to raise the gap (the file says so for
BR-3's leg; the same belief, lowering beta_L adds disorder, is BR-2's "what
one must believe"), and the beta_T move is believed to lower it. So each
route has one RB-type step in beta_L and one carry in beta_T. They differ in
where the beta_T carry sits: on the face (a system two-dimensional in u, where
CA-FAIL's device does not act on u-boundary data) for BR-2; at beta_L = beta,
in the full 4D model, for BR-3. The verdicts should rest on that difference.

**BR-2 row and verdict "wounded" (L397, L420). HOLDS AFTER CORRECTION.**
- "Terminal obligation vs target: unknown/comparable". (FACE-SG) alone is about
  the face model and is not comparable with C_beta: right. But the route's
  obligations together, (FACE-SG) at (infinity, beta, beta) and (MON-L) on
  [beta, infinity), give a gap at every point (beta_L, beta, beta) of the
  descent. By the criterion the table uses for BR-3 ("it gives clustering at
  every point of the path"), that is stronger than C_beta.
- (MON-L) has no mechanism. The file says so (L498: no proof row on (MON-L),
  "route RB type, no mechanism"), and the lane's registry has RB as "stronger |
  blocked-equivalent" (parts/gap.md L181 at 6a6f2701a). So the descent step is
  blocked in the same way RB is.
- Corrected cell: "stronger (with (MON-L), a gap at every point of the
  descent); (FACE-SG) alone: unknown/comparable". Corrected verdict:
  "wounded at the face step (a candidate method: the face as a 2D system,
  OpenAI's 2D argument, u-boundary data only); blocked at the descent step
  (MON-L), which is RB-type with no mechanism. Not near closure."
- "Fails a test in valid form? see 7.3": 7.3 gives MON-L-cov FALSE (holds),
  the class argument (holds after the source correction of step 6) and the
  five-dimensional test (conditional). Right as a pointer.
- "Already tried? partly (V1, row 1053; '(BR-L') no mechanism')": consistent
  with row 1072's own search note (L408). Not re-checked in row 1053.

**BR-3 row and verdict "blocked-stronger" (L398, L430-432). HOLDS AFTER
CORRECTION.**
- "stronger (it gives clustering at every point of the path)": true.
  (LIN-path) with the start gives m(P(t)) >= m(P(0)) e^(-C t) for all t.
- Verdict "blocked-stronger": holds. No mechanism for a volume-free one-sided
  law is on file (row 878 F5 gives only the square-root law with a volume
  factor; read at `library/gap-crux-exercise2-max.md` L182-187, L214).
- "First open statement: (LIN-path) on the leg where the gap decreases". In
  chain order the first open statement is on leg 1: a volume-free
  bounded-decrease law in beta_L at beta_T = 0, m(beta_L, beta, 0) >= e^(-C)
  m(infinity, beta, 0) for beta_L in [beta, infinity). It is believed (the gap
  is believed to increase there) but not proved. "A one-sided law needs to
  control decreases only" (L430) is a statement about beliefs; a proof must
  control every leg. Also, the anchor's data enter BR-3 only through leg 1;
  leg 2 starts at (beta, beta, 0), which is BR-9's start.
- Corrected verdict text: "blocked-stronger. Open statements: on leg 1, a
  volume-free bounded-decrease law in beta_L at beta_T = 0 (an RB-type
  statement, believed); on leg 2, (LIN-path) along beta_T from (beta, beta, 0),
  the anisotropic form of row 878's missing linear law ((NOCRIT) in
  differential form). The anchor's data enter only through leg 1."
- "survives as the exact form of a path bridge" (L398): "exact" is too
  strong. (LIN-path) is one sufficient form (a differential a priori law on the
  gap); C-3 and C-6 of the file name other forms (other carried quantities;
  discrete steps). Corrected: "survives as the differential form of a path
  bridge for the gap".
- 8.6 (L492) builds on this: "a path bridge from R_eps to a window coupling is
  equivalent in strength to a volume-free one-sided bound on the gap along the
  decreasing part of the path". Corrected text: "a path bridge of this form
  needs a volume-free one-sided bound on the gap along the whole path; on the
  parts where the gap is believed to increase the bound is believed but open.
  The bound implies the bridge; the converse is not shown."
- L430, "Row 878 F5 applies verbatim to any one-parameter family H(t) = A -
  t B of transfer-matrix generators". F5 is stated for H(x) = A - x B with B
  bounded. The generator -log T of a lattice gauge transfer matrix is not
  linear in a plaquette coupling (T = e^(-V/2) K e^(-V/2) with K depending on
  the couplings of plaquettes that contain the transfer direction). The
  variational and Feynman-Hellmann steps extend to smooth families with an
  extra term of order h sup ||H''||, so the conclusion (the general law is the
  square-root law with a volume factor) stands. Precision only.

**The other rows of 7.2.**
- BR-0. HOLDS. The equivalence "given (S), (BR-iso)_beta iff C_beta" is the one
  of rows 1066, 1069, 1070 (row 1066 REN; row 1070 section 9, as quoted in row
  1072's own reading).
- BR-1 "dead (PROVED on finite boxes for the observables of MON-T)". HOLDS
  with the scope of step 3: R_eps and the window are not ordered, so a
  comparison needs mixed signs (correlations non-decreasing in beta_L,
  non-increasing in beta_T); MON-T refutes the beta_T half on the face. A
  mixed-sign principle claimed only at finite beta_L is not refuted. The file's
  registry (7.5: "reopen: an inequality comparing non-ordered points") and 8.8
  carry this scope. "Dead" in 7.2 should read "retired for comparison
  principles that hold on the face", as 7.5 does.
- BR-4 "dead in its uniform form". HOLDS given CA-FAIL with the corrections of
  steps 4-5 (uniform form for compact continuous spins; the device is Lemma
  SLAB of row 1013; threshold 1.0109).
- BR-5 "blocked-stronger". HOLDS. The cited miss is in `parts/gap.md` L153 at
  6a6f2701a: "strong coupling reaching the band (a 5.4x miss at beta 2.3)".
- BR-6 "blocked-stronger (ARGUED)". HOLDS as ARGUED, with one precision: "so
  it implies transverse clustering of the window" needs control of the fine
  variables given the blocked ones (true for an exact decimation with local,
  mixing conditional laws; not for a general RG map). The file's reopen
  condition ("an exact transverse decimation") already points to this.
- BR-7 "blocked-equivalent in the full model; on the face it merges into
  BR-2". HOLDS as ARGUED. With step 4: on the face, a gap uniform in T must use
  u-boundary data only (sheet pins defeat uniformity in T and L together).
- BR-8. HOLDS as reported (row 1025 not read by the author; not read here).
- BR-9 "dead for now: worse start than R_eps". The substance holds (no posted
  input at (beta, beta, 0)). The word "dead" disagrees with 7.5
  ("blocked-local") and hides the link to BR-3: BR-9's carry is BR-3's leg 2.
  Corrected verdict: "blocked-local: its start (beta, beta, 0) has no posted
  input; its carry is BR-3's leg 2".

### Step 8. Addendum to T2, verdict table, what was not covered, RESULT

**Addendum to T2: the threshold claim needs no numerics.** For |x| <= pi,
1 - cos x >= 2 x^2/pi^2 ((1 - cos x)/x^2 = (1/2)(sin(x/2)/(x/2))^2 decreases
on (0, pi] to 2/pi^2). So sum_j (1 - cos p_j) >= (2/pi^2) |p|^2 on [-pi, pi]^3,
and with p = pi q:
  W_3 <= (2 pi)^(-3) (pi^2/2) int_{[-pi,pi]^3} |p|^(-2) dp = (1/16)
  int_{[-1,1]^3} |q|^(-2) dq <= (1/16)(4 pi + 8 - 4 pi/3) = 1/2 + pi/6.
(The unit ball gives 4 pi; on the rest of the cube |q|^(-2) <= 1, volume 8 -
4 pi/3.) So beta_FSS = 2 W_3 <= 1 + pi/3 < 2.05 < 2.3, by hand. The numeric
value 1.0109 is a GUIDE only. This makes CA-FAIL's range claim Lean-friendly
given the infrared-bound theorem.

**Verdict table.**

| Item (row 1072 line) | Verdict | Where |
|---|---|---|
| Remark RP-ANI, C1 (L119, L160) | HOLDS (given Osterwalder-Seiler, recalled); precision: positivity of the one-step transfer matrix from link reflections | step 3 |
| Lemma MON-T (L121-127): T1 Schur step | HOLDS | step 3 |
| Lemma MON-T: T1 analytic-zero step | HOLDS (exceptional set box-dependent; for NO-MON (i) the one-bond box gives c_2 > 0 at every beta_M > 0) | step 3 |
| Corollary NO-MON (i) (L129) | HOLDS | step 3 |
| Corollary NO-MON (ii) (L129) | HOLDS AFTER CORRECTION: X >= 1 is not in the definition of X; corrected text given | step 3 |
| NO-MON reading line (L130) | HOLDS with scope (face-valid principles; mixed-sign principles claimed only at finite beta_L not refuted); U(1) remark HOLDS as ARGUED (reflection, not Schur; constant 1/4) | step 3 |
| Lemma CONT (L134) | HOLDS | step 5 |
| Q_fix (L137) | HOLDS as ARGUED | step 5 |
| Q_some (L138) | HOLDS AFTER CORRECTION (constant-coupling criteria only, after CA-FAIL) | step 5 |
| C4 (L163) | HOLDS AFTER CORRECTION (marks: Lemma CONT proved, the rest a reading) | step 5 |
| C5 (L164) | HOLDS AFTER CORRECTION (U(1) grade by path range; start reading as corrected in step 5 of row 1072) | step 5 |
| T2: FSS threshold, 3D O(4), beta s.s' | HOLDS: 2 W_3 = 1.0109 (open secondary copy, Peled-Spinka; original not read); hand bound 1 + pi/3 < 2.3 | steps 4, 8 |
| Proposition CA-FAIL, proof and precision (L337-338, L368) | HOLDS AFTER CORRECTION (wording: compact continuous spins, averaged long-range order, the D2 sentence) | steps 4, 5 |
| CA-FAIL "Meaning" and L418 | HOLDS with a scope precision: the face escapes the device for u-boundary data only; sheet pins restore it | step 4 |
| T3: does Theorem D2 contain CA-FAIL | No. Lemma SLAB of row 1013 (K3') contains the device and the no-uniform-mixing conclusion for large beta; CA-FAIL adds the threshold 1.0109 and the application. RESULT-line credit and 6c table row corrected | step 5 |
| U(1)-range correction (L341) | HOLDS (precision: 1.01 is the Wilson-action numerics, 2^14 the Villain theorem range) | step 4 |
| 6d row 10 (L356) | HOLDS AFTER CORRECTION (a 2 + 2 method 27 needs a beta_L carry too) | step 5 |
| Lemma MON-L-cov FALSE (L412-413) | HOLDS; precision on "can only be a statement about the rate" | step 6 |
| (MON-L) class argument (L416) | HOLDS AFTER CORRECTION: Z_2 duality sides and the ADS attribution are wrong; vanishing at beta_c is a BELIEF; the quoted RB words are in `library/gap-part-draft.md` L158, not `parts/gap.md` L181; conclusion kept at GUIDE grade (the lane's ordered-Ising example) | step 6 |
| Lemma LIN-perp (L428) | HOLDS AFTER CORRECTION (the needed facts; "finite for t > 0" and "order log(1/t)" not shown and not needed) | step 6 |
| Kill table, BR-2 "wounded" (L397, L420) | HOLDS AFTER CORRECTION: obligations jointly stronger than C_beta; wounded at the face step, blocked at (MON-L) (RB type, no mechanism) | step 7 |
| Kill table, BR-3 "blocked-stronger" (L398, L432) | HOLDS AFTER CORRECTION: verdict stands; the first open statement in chain order is the beta_L leg at beta_T = 0; "exact form" and 8.6's "equivalent" too strong | step 7 |
| Kill table, other rows | BR-0, BR-4, BR-5, BR-6, BR-7, BR-8 HOLD as scoped; BR-1 HOLDS with scope ("retired for face-valid principles"); BR-9 wording ("blocked-local"; its carry is BR-3's leg 2) | step 7 |

No item FAILS. No first failing line.

**What this check did not cover.** The original FSS 1976 paper (Project Euclid
and the publisher served bot challenges; not bypassed); Osterwalder-Seiler
1978 (RP recalled); Aizenman-Duminil-Copin-Sidoravicius, Duminil-Copin-
Goswami-Raoufi, Aizenman-Barsky-Fernandez, Duminil-Copin-Tassion, Wegner
(recalled, not read); row 1053 (BR-2's "already tried" cell and its K3 row);
rows 1066 REN, 1069 and 1070 beyond what row 1072 quotes (BR-0's equivalence is
taken as quoted); row 1025. Lemma SLAB of row 1013 was read (L57, L220-239)
but not checked beyond the identity used in CA-FAIL. Row 1074's file was not
opened. No numeric run decided anything; the one GUIDE run (scratchpad
`watson.py`, Python -I, one thread) only confirmed W_3. Provenance: written by
Claude Opus 5.5 at max effort, laptop subagent, same provider as the author;
this is not an independent check. Only this file was written; nothing
committed or pushed.

RESULT: Row 1075 (Claude Opus 5.5 max, laptop subagent; same-provider line-by-line check of row 1072, not independent): no item FAILS. HOLDS: Remark RP-ANI; Lemma MON-T (Schur step and analytic-zero step checked, Claim S2 re-derived); Corollary NO-MON (i); Lemma CONT; Lemma MON-L-cov FALSE; the U(1)-range correction; and test T2: the FSS threshold for 3D O(4) in normalization beta s.s' is 2 W_3 = 1.0109 (read in Peled-Spinka's open notes; the 1976 original not fetched), with a hand bound 1 + pi/3 < 2.3. HOLDS AFTER CORRECTION (texts given): NO-MON (ii) (X >= 1 is not in the definition); Q_some, C4, C5; Proposition CA-FAIL (wording; test T3: Theorem D2 does not contain it, but Lemma SLAB of row 1013 holds its device and qualitative conclusion, so CA-FAIL is that lemma made explicit for the window; the face escapes the device for u-boundary data only); 6d row 10 (a 2 + 2 method 27 also needs a carry in beta_L); the (MON-L) class argument (Z_2 duality sides and the ADS attribution wrong; vanishing of the gap at beta_c is belief; kept at GUIDE grade via the lane's ordered-Ising example); Lemma LIN-perp (scope); kill table: BR-2 is stronger than the target, wounded at its face step and blocked at (MON-L); BR-3 stays blocked-stronger, but its first open statement in chain order is the beta_L leg at beta_T = 0, and 8.6's equivalence is not shown.
