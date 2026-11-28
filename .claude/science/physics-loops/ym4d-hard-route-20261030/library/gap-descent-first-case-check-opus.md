lead: Claude Opus 5.5 (lead session), dispatched 2026-11-17
row: 1113

# Row 1113 check: gap descent, first case

Checker: Claude Opus 5.5, effort max, laptop subagent.
This is a same-provider check. The writer of row 1109 is Claude Fable 5.2.
A same-provider check is not an independent check in the sense of the rules.

## Plan (updated after the brief was read)

Object under check: `library/gap-descent-first-case.md` (row 1109, 231 lines, read in full)
and its runs in `runs/gap-descent-first-case/`. Repo `~/ym4d-lead/clone`, commit 53d7da6a3,
branch claude/ym4d-hard-route.

Sources at the lines the note names: `gap-bridge-vectors-max.md` L215-242 and L296-390
(row 1076); `gap-descent-sign.md` in full (row 1081); `gap-checkerboard-singlet-astra.md`
L187-300 and L608-712 (row 1084).

Items (one per response; each verdict is HOLDS, HOLDS AFTER CORRECTION or FAILS):
- C0. Read the cited lemmas and the runs.
- C1. Step 1: the gauge-invariant coordinates and the decorated-ferromagnet form.
- C2. Step 2: Lemma KIN-G and Lemma FACE-FLUX.
- C3. Step 3: form A, Lemma LOOP, the diamagnetic bound, the three hand values of W.
- C4. Step 4: Example Q8-INF (wall entropy factor 2; rate(0) = 2b - 2 log 2 at leading
  order; can the low-temperature expansion behind it be written).
- C5. Step 5: the claim that (M) needs sharp rates at both ends; the small-b guide for (END-0).
- C6. Step 5: Example INT-2.
- C7. The three named failures: a failure of the method as written, or a gap that a short
  argument closes.
- C8. Is the stop by the third rule valid.
- RESULT line.

Status: all items C0-C8 checked; summary and RESULT at the end. No mass gap is claimed.

## C0. Sources and runs read. DONE.

Read in full: `library/gap-descent-first-case.md` (231 lines); `library/gap-descent-sign.md`
(row 1081, 181 lines). Read at the lines the note names: `library/gap-bridge-vectors-max.md`
L215-242 and L296-390, and also L392-420 (Example KIN-7, which the note uses);
`library/gap-checkerboard-singlet-astra.md` L187-300 (Lemma DEC) and L608-712 (Lemma GH-NA,
(GH5), (GH6)). Not read: row 1108, row 1112 (the brief of row 1113 does not ask for them).

Runs read: `gh2strip.py`, `gh2strip_long.py` (they differ only in the t grid and the output
name), the three logs, the three JSON files. I re-derived the operator of model `gh` by hand:
on the two-site strip the K-neutral gauge-invariant functions are functions of
(A, B) = (B_1^(-1), B_2) under joint conjugation; the cut rotation is A -> A W^(-1), B -> W B,
whose Casimir is j_2(j_2+1); V_f = -b (x(A) + x(B)); K_Phi = lambda_(j_1)^2 lambda_(j_3)^2.
So `K = lam(j1)^2 lam(j3)^2`, `D = lam(j2)(beta_L)`, `N = cas(j2)` in the script is the operator
the note names. Not refuted.

Side finding on the run table (step 7 of the note; guide grade, not one of the brief's items).
I recomputed the table columns from the JSON files with a short script (scratch, inline; not kept).
All printed values agree, except one cell: for b = 4 the column "least m(t) - m(0), t in (0, 20]"
says "below 0". The b = 4 heat-kernel run covers t in (0, 3] only (`out_gh_14.json`,
`out_gh_18.json`; the long run stops at b = 3.5), and there the least value is +2.0e-3 and
m(3) - m(0) = +0.0059. The negative end value at b = 4 is in the Wilson column only
(m(beta_L = 0.05) - m(infinity) = -0.030). Correction: for b = 4 the cell should read
"+2.0e-3 on (0, 3]; t > 3 not run". The note's reading "the end-point form fails from b between
3.5 and 4" rests on the Wilson column and stands at guide grade. For b = 8 and 12 the cell
"below 0" is right on (0, 3] (-3.1e-2 and -2.0e-2).

## C1. Step 1: gauge-invariant coordinates and the decorated-ferromagnet form. HOLDS (two scope notes).

Checked line by line by hand (Claude Opus 5.5).
- Gauge and rigid actions. Phi_i(u)^(-1) a_e Phi_i(v) is fixed by the local group and is
  conjugated by k_i under K. So the weight is invariant. HOLDS.
- rho(u) = Phi_1(u)^(-1) Phi_2(u) and v_e = Phi_1(u)^(-1) a_e Phi_2(v) are gauge invariant
  (the g's cancel). In the gauge Phi_1 = 1 (g(u) = Phi_1(u)^(-1)): rho = Phi_2, v_e = a_e rho(v),
  so a_e = v_e rho(v)^(-1). The map (a, Phi_2) -> (v, rho) is a bijection and keeps Haar measure
  (right translation of a_e by rho(v) at fixed rho). The gauge Phi_1 = 1 is a site gauge, so the
  coordinates are complete on every graph, tori included. HOLDS.
- Higgs part. With a_e = Phi_1(u) v_e Phi_2(v)^(-1): sheet 1 gives Re(v_e rho(v)^(-1)) = v_e . rho(v);
  sheet 2 gives Re(rho(u)^(-1) v_e) = rho(u) . v_e (Re(p q-bar) = p . q for unit quaternions).
  So the Higgs part is b sum_e (v_e . rho(u) + v_e . rho(v)). At beta_L = 0 this is (DEC1) of
  row 1084 exactly; integrating v_e gives omega(b abs(rho(u) + rho(v))), the n = 2 weight of
  Lemma GH2-0 (s^2 = 2b^2 + 2b^2 rho . rho'). The S^3 integral (2/s) I_1(s) was recomputed
  from the density (2/pi) sin^2 theta of v_1 = cos theta. HOLDS.
- Six-spin term. With corners 1 = (0,0), 2 = (1,0), 3 = (1,1), 4 = (0,1):
  a_p = a_12 a_23 a_43^(-1) a_14^(-1)
      = Phi_1(1) v_12 [Phi_2(2)^(-1) Phi_1(2)] v_23 v_43^(-1) [Phi_1(4)^(-1) Phi_2(4)] v_14^(-1) Phi_1(1)^(-1)
      = Phi_1(1) v_12 rho_2^(-1) v_23 v_43^(-1) rho_4 v_14^(-1) Phi_1(1)^(-1).
  By cyclicity Re a_p = Re(v_14^(-1) v_12 rho_2^(-1) v_23 v_43^(-1) rho_4), the note's formula.
  rho_1 and rho_3 drop out because corner 1 is the tail of both its edges and corner 3 the head
  of both; the factors alternate inverse / not inverse. HOLDS.
- K acts by rho -> k_1^(-1) rho k_2, v -> k_1^(-1) v k_2. HOLDS.
- beta_L = infinity. On a simply connected box all plaquettes are 1, a_e = h(u) h(v)^(-1) with h
  fixed up to h -> h c, and Psi_i = h^(-1) Phi_i are two independent O(4) models at coupling b,
  with one common left rotation left over. rho = Psi_1^(-1) Psi_2. E[rho(0) . rho(x)] =
  Re(E[Psi_2(0) Psi_2(x)^(-1)] E[Psi_1(x) Psi_1(0)^(-1)]) by independence and bilinearity; each
  mean is fixed by conjugation (global left invariance), so it is c(x) times 1. Hence c(x)^2. HOLDS.
  Scope note 1: "a is a pure gauge" needs a simply connected free box. On a torus, or on a free
  subgraph with a hole, flat holonomies stay (Remark TOR of row 1076). The note's step 1 says
  "free subgraph or torus" for the model; the beta_L = infinity line holds for boxes only.
- Channels at beta_L = infinity ("argued"). The channel "one particle on each sheet" has a written
  lower bound: split F into its (L_1, L_2) isotypic parts; by independence and Schur the
  left-spin-j part (j >= 1/2) gives sums of products of two one-sheet charged correlations, so
  rate >= 2 x (charged rate of one sheet). The channel "two on one sheet" is the left-singlet gap of
  one O(4) sheet. That it equals 2m needs the particle content of the O(4) model (no left-singlet
  one-particle state, no bound state below 2m). That is physics, not on file.
  Scope note 2: the sentence "the rate at infinity is a two-particle rate, 2m" is physics
  reasoning for the one-sheet channel; it is not "argued" in the lemma sense.

Verdict C1: HOLDS, with the two scope notes above (they restrict wording; they change no claim the
note uses later).

## C2. Step 2: Lemma KIN-G and Lemma FACE-FLUX. KIN-G HOLDS; FACE-FLUX HOLDS AFTER CORRECTION.

Checked line by line by hand (Claude Opus 5.5).

**Setting.** In temporal gauge the plaquette between times tau and tau+1 over the spatial link k
is Re(a_k(tau) a_k(tau+1)^(-1)): convolution on a(k), that is K_a. The temporal Higgs bonds are
b Re(Phi_i(k,tau)^(-1) Phi_i(k,tau+1)): right convolution on Phi_i(k), that is K_Phi. The spatial
Higgs bonds give V. K_a, K_Phi and V commute with the slice gauge group (convolution by a class
function commutes with left and right translations; right convolution commutes with left
translation; V is gauge invariant). So T maps H^G to H^G. HOLDS.

**Lemma KIN-G.**
- (a) g(1) = 1, g(k+1) = g(k) a(k) gives g.a = 1; the stabiliser of a = 1 is the constant g: one
  common left rotation. f(a, Phi) = f(1, g_a Phi); the norm is kept (Haar invariance in Phi, then
  the a-integral is 1); onto by h -> h(g_a Phi). Same proof as Lemma KIN (b) of row 1076. HOLDS.
- (b) The gauge transformation g = 1 at sites <= k and g = W at sites > k sends
  (a(k) = W, other a = 1) to a = 1 and Phi_i(k') to W Phi_i(k') for k' > k. So
  f(a(k) = W, others 1, Phi) = f(1, rho_k(W) Phi). For all links at once
  (K_a f)(1, Phi) = int prod_k w_L(V_k) h(g_V Phi) dV with h = R f and
  h(g_V Phi) = (rho_(n-1)(V_(n-1)) ... rho_1(V_1) h)(Phi) (the order of row 1076's proof).
  The integrals factor, and Schur gives M_k = sum_j lambda_j P_k^j. R commutes with e^(-V/2)
  (V at a = 1 is V_f) and with K_Phi. So R T R^(-1) = e^(-V_f/2) D K_Phi e^(-V_f/2), and with
  [D, K_Phi] = 0 this is S* D S. Heat kernel: M_k = e^(-t C_k), D = e^(-tN). HOLDS.
- (c) For k < l, J_k = J_mid + J_l with J_mid on the sites k < k' <= l; C_l commutes with J_l
  (Casimir) and with J_mid (other sites); so [C_k, C_l] = 0. Right convolution commutes with left
  translation for every weight. HOLDS.
  One line is implicit and true: C_k commutes with G (the generator of G is J_(<=k) + J_k, and C_k
  commutes with both), so D maps K to K. Row 1076's Lemma KIN (a) states it; KIN-G (c) omits it.
- "The same statement in the measure": in temporal gauge on a free box the pure-gauge law makes
  each a_k(tau) a walk in tau with independent steps of law w_L, independent in k; the Higgs
  partition functions tilt it. HOLDS (a restatement).

**Per-cut Proposition DIL.** On K the kernel of C_k contains the constants and
Re(Phi_1(1)^(-1) Phi_2(1)) (sites <= k only), so the second smallest eigenvalue of C_k is 0 and
delta_2 = 1. The kernel of N = sum_k C_k contains every function of the rho(k), so nu_1(N) = 0 too;
hence "the losses add" is right: in GH2 the dilute range of row 1081 is empty. HOLDS.
**Correction.** Proposition DIL bounds with psi = S Omega_f / norm(S Omega_f), the top vector of
S S*, not with Omega_f, the top vector of S* S (Rayleigh with Omega_f gives
<Omega_f, S* D S Omega_f> = lambda_0(infinity) <psi, D psi>). C_k does not commute with V_f, so
the two means differ in general. Corrected text: "m_k(t) - m(0) >= - 2 t <psi, C_k psi>,
psi = S Omega_f / norm, the top vector of S S*." The same correction applies to n_0(0) wherever
Identity KIN-5 is used (there phi_0(0) is the top vector of S S*).

**Lemma FACE-FLUX.** S* S and S S* are both tensor products of the two one-sheet chains; each
one-sheet factor commutes with the left rotation of its own sheet; its top vector is unique
(Perron-Frobenius for the positive kernel of S_i* S_i; for S_i S_i* because the non-zero spectra of
S* S and S S* agree with multiplicity), so it is invariant under that rotation (a one-dimensional
representation of SU(2) is trivial). The product vector lies in K and is the top vector there.
**Missing line (true, one step).** Invariance under the global left rotation of sheet i does not by
itself say that J_k^i, the generator for the sites beyond the cut only, has mean 0. It does:
U(g)* J_k^(i,a) U(g) = R(g)^a_b J_k^(i,b), because the rotation of the sites <= k commutes with
J_k^i. So the mean vector <J_k^i> in an invariant state is fixed by every R(g) in SO(3), hence 0.
(The vacuum is smooth, being the image of a smoothing operator, so J acts on it.) Then
<J_k^1 . J_k^2> = sum_a <J_k^(1,a)> <J_k^(2,a)> = 0 and <C_k> = 2 q_k. HOLDS after this line is added,
for Omega_f and, by the same proof, for psi (with q_k the one-sheet value in the top vector of
S_1 S_1*).

**The class remark of way 1.** "No inequality that uses only Lemma KIN-G, D <= 1, D = 1 on
flux-free states, positivity of the kernel and a gap at the face can give it": Example KIN-7 of
row 1076 has all five properties (its K is the convolution by four positive weights; lambda_sigma,
lambda_tau >= 0 for beta >= 0) and its sign is wrong. So the remark HOLDS as a statement about that
class (on a small box; that suffices to exclude an inequality that would also apply there).

Verdict C2: Lemma KIN-G HOLDS (one implicit line, true). Lemma FACE-FLUX HOLDS AFTER CORRECTION
(the missing line above; in the per-cut DIL bound read psi, the top vector of S S*, for Omega_f).

## C3. Step 3: form A, Lemma LOOP, the diamagnetic bound, the three hand values of W. HOLDS.

Checked line by line by hand (Claude Opus 5.5).

**Form A.** Free box, sites (k, tau). The time links and the spatial links of row 0 form a spanning
tree (a comb), so the axial gauge is complete. The plaquette over (k, tau) is
P_k(tau) = a_k(tau) a_k(tau+1)^(-1); for each k the map (a_k(1..T)) <-> (P_k(0..T-1)) is
triangular with Haar-preserving steps, so the P_k(tau) are i.i.d. with law w_L. With
g(k, tau) = a_1(tau) ... a_(k-1)(tau): a_k = g(k)^(-1) g(k+1), so the spatial bond is
Re(Psi_i(k)^(-1) Psi_i(k+1)) for Psi_i = g Phi_i (no twist), and the time bond is
Re(Psi_i(k,tau)^(-1) U_k(tau) Psi_i(k,tau+1)) with U_k(tau) = g(k,tau) g(k,tau+1)^(-1), the
holonomy around the plaquettes of row tau in columns 1..k-1. HOLDS.
The walk: U_1 = 1 and U_(k+1)(tau) = Q_k(tau) U_k(tau), Q_k(tau) = g(k,tau) P_k(tau) g(k,tau)^(-1).
Induction on k: the P of columns < k fix all g(k, .) and all Q of columns < k; given them, the
P_k(.) are i.i.d. w_L and independent of them, and conjugation by a fixed element keeps the law
w_L (class function). So all Q_k(tau) are i.i.d. w_L, over k and over rows. Heat kernel: U_k(tau)
has law h_(t(k-1)). HOLDS.

**Lemma LOOP.** Re(Phi(u)^(-1) a Phi(v)) = Phi(u) . L_a Phi(v) (Re(p-bar q) = p . q). Moments of
the uniform law on S^3: E[s_(i_1) ... s_(i_2k)] = (sum over pairings of deltas) / (4 . 6 ... (2k+2));
checked at k = 1 (1/4) and k = 2 (E s_1^4 = 3/24 = 1/8). Contracting the deltas closes the strands
into loops; a strand run against the edge orientation gives L_a^T = L_(a^(-1)); L is a
homomorphism, so a loop gives tr L_(a_l) = 4 Re a_l (eigenvalues e^(+-i theta), each twice).
Backtracking strands give holonomy 1. Exchange of sum and integral: sum_n b^n abs(x)^n / n! <=
e^(b abs(x)) is integrable (Fubini); the pairing sum is finite for fixed (n_e); at a = 1 every term
is >= 0, so sum_omega p(omega) = Z_Phi(1) < infinity, and the series converges absolutely for every a.
HOLDS.

**Diamagnetic bound.** Z_Phi(a) <= sum p(omega) prod abs(Re a_l) <= Z_Phi(1); Z_Phi(a) > 0 as the
integral of a positive function. Z_GH2 = Z_YM E_YM[Z_Phi(a)^2], and the loop expansion of the square
with |prod Re a_l| <= 1 gives the stated formula, abs(W) <= 1, pbar a probability, and
Z_GH2 <= Z_YM Z_Phi(1)^2. W = 1 at beta_L = infinity holds on a simply connected box (trivial
holonomy). HOLDS.

**Hand values.** For a simple closed curve around A plaquettes of a free box the holonomy has law
w_L^(*A) (product of conjugates of A independent plaquettes, as in form A), so
E chi_j(hol) = (2j+1) lambda_j^A.
- One loop: E Re(hol) = E chi_(1/2)/2 = lambda_(1/2)^A. HOLDS.
- Two loops around the region: Re(g)^2 = chi_(1/2)^2/4 = (1 + chi_1)/4; W = (1 + 3 lambda_1^A)/4 >= 1/4
  (lambda_1 >= 0 for the Wilson and heat-kernel weights). The same for opposite orientations.
  HOLDS.
- One loop twice around: Re(g^2) = cos 2 theta = (chi_1 - 1)/2 (chi_1 = 1 + 2 cos 2 theta);
  W = (3 lambda_1^A - 1)/2 < 0 iff lambda_1^A < 1/3. At beta_L = 0:
  (2/pi) int_0^pi cos 2theta sin^2 theta d theta = -1/2. Such a loop occurs in Lemma LOOP: n_e = 2 on
  the boundary edges with a pairing that switches strands at one site. HOLDS.

Notation remark (no change of content): the note uses the letter A for the area and for the
holonomy in the same line.

Verdict C3: HOLDS (form A, Lemma LOOP, the diamagnetic bound, the three hand values). The facts
W = 1 at beta_L = infinity and the law w_L^(*A) need a simply connected free box, which is the
note's setting for this step.

## C4. Step 4: Example Q8-INF. HOLDS AFTER CORRECTION. (Written in two saves: the hand check first, then the guide run and the verdict.)

Checked by hand (Claude Opus 5.5).
- Bond weights. Q_8 with Re(+-1) = +-1, Re = 0 on the six elements of order 4. In the gauge
  Phi_1 = 1 the two Higgs bonds of an edge are Re(a) and Re(a q'), q' = rho(v) rho(u)^(-1); the sum
  over a is invariant under conjugation of q', so f is a class function of rho(u)^(-1) rho(v).
  Recomputed term by term: f(1) = (e^(2b) + e^(-2b) + 6)/8; f(-1) = 1; for q = i the eight a give
  e^b (a = 1), e^(-b) (a = -1), e^(-b) (a = i), e^b (a = -i), 1 (a = +-j, +-k), so
  f(i) = (2e^b + 2e^(-b) + 4)/8. HOLDS.
- Wall weight at beta_L = 0: f(i)/f(1) = 2 e^(-b) (1 + 2e^(-b) + O(e^(-2b))). The two terms e^b
  are a = 1 (the jump in sheet 2) and a = q^(-1) (the jump in sheet 1). In the decorated picture
  they are the two positions of the midpoint spin v_e (aligned with rho(u) or with rho(v)). So the
  entropy factor 2 per wall bond is right at leading order. f(-1)/f(1) = 8 e^(-2b): a jump by -1
  is subleading. HOLDS.
- Wall weight at beta_L = infinity: each sheet is a Q_8 model with bond weight e^(b Re q):
  relative weight e^(-b) for a jump of order 4, e^(-2b) for -1. The flatness constraint forces one
  sheet for a whole wall, so the factor 2 is per wall (a prefactor), not per bond. HOLDS.
- Rates at leading order. In a pure phase in infinite volume the truncated correlation over time n
  of a local observable is carried by a tube of two vertical walls: weight (wall weight)^(2n) times
  entropy that is O(e^(-b)) per unit length (kinks cost one more broken bond each). So
  rate(infinity) = 2b + o(1) and rate(0) = 2b - 2 log 2 + o(1). The gap 2 log 2 is of order one,
  so the o(1) terms do not change the order for b large. HOLDS at leading order.
- **Correction needed (the class of observables).** The note's (W) and (M) are for all
  gauge-invariant local observables in the symmetric finite-volume measures (free subgraphs, tori).
  For Q_8 at large b, rho(0) and rho(x) are both close to one random element (long-range order,
  Peierls), so Cov(f(rho(0)), f(rho(x))) does not decay for a K-charged f, at beta_L = 0 and at
  beta_L = infinity (row 1076, T2 and T3). In that class both rates are 0; (M) holds trivially and
  (W) fails. Example Q8-INF is a counterexample to the K-neutral form: rate is the decay rate of
  truncated correlations of gauge-invariant local observables that are invariant under K (for these
  the symmetric-state covariance equals the pure-phase covariance, since K acts transitively on the
  ground states at both ends). That is the form of Example KIN-7 (class functions) and of the
  step-7 run (K-neutral sector).
- Box remark. With free boundaries and observables next to the boundary, one wall from the boundary
  suffices; the box-uniform K-neutral rates are then b + o(1) and b - log 2 + o(1). The inequality
  rate(0) < rate(infinity) is the same.

Next: a guide run (periodic strips, K-neutral sector) of the two end models at large b, then the
question whether the expansion can be written.

**C4 guide run (guide only; discharges nothing).** Script `runs/gap-descent-first-case-check-opus/q8strip.py`, log
`runs/gap-descent-first-case-check-opus/log_q8strip.txt` (written in scratch, copied by the lead; one job, nice 10, one BLAS thread,
Python -I with the user site path added in the script for numpy). Two Q_8 models on a periodic strip
of width L, transfer matrix in time, sector invariant under r -> c r k: 'inf' = one sheet at
beta_L = infinity (bond weight e^(b Re q)); 'zero' = the rho model at beta_L = 0 (bond weight f).
Code check: at L = 3 the orbit-reduced matrix and the full 512 x 512 projected matrix give the same
gap to 10 digits (b = 2.4 and 6, both models).
| b | m_inf (L = 3 / 4 / 5) | m_0 (L = 3 / 4 / 5) | m_0 - m_inf at L = 5 |
|---|---|---|---|
| 2.4 | 4.2589 / 4.2959 / 4.3230 | 2.0310 / 1.8404 / 1.8073 | -2.516 |
| 4 | 7.8908 / 7.9012 / 7.9056 | 6.3184 / 6.3404 / 6.3504 | -1.555 |
| 8 | 15.9980 / 15.9982 / 15.9982 | 14.6083 / 14.6087 / 14.6089 | -1.3894 |
| 12 | 23.99996 (all L) | 22.61361 (all L) | -1.38635 |
The limits are 2b and 2b - 2 log 2 (2 log 2 = 1.386294). So the factor 2 per wall bond and
rate(0) = 2b - 2 log 2 + o(1) are confirmed at guide grade, and the sign of (M) in the K-neutral
form is wrong for Q_8 on these strips already at b = 2.4.

**Can the low-temperature expansion be written? Yes, by standard means; it is not written in the
note or here.** What it needs:
- (a) rate(0) <= 2b - 2 log 2 + O(e^(-b)). Short. The rho model has a positive transfer matrix:
  f = (phi * phi)/8 with phi = e^(b Re), so f is positive definite on Q_8. For a K-neutral F on one
  time row, the spectral form of Jensen gives E[F; tau_n F] >= E[F;F] (E[F; tau_1 F] / E[F;F])^n.
  With F = 1{rho(0,0) differs from rho(+-1,0)}: E[F] = 96 e^(-4b)(1 + O(e^(-b))) (isolated site,
  6 jumps, 4 wall bonds) and E[F tau_1 F] = 384 e^(-6b)(1 + O(e^(-b))) (vertical domino, 6 wall
  bonds), so the ratio is 4 e^(-2b)(1 + O(e^(-b))). The local probabilities come from a convergent
  cluster expansion of the pure phase.
- (b) rate(infinity) >= 2b - o(1). Longer. A contour cluster expansion of the pure phase of one
  sheet, with a refined count of near-straight walls (a wall of length 2n + 2k across distance n has
  e^(O(k log(n/k)))-many shapes). Crude Peierls counting is not enough: with the connective constant
  mu = 2.64 of the square lattice it gives only rate >= 2b - 2 log mu = 2b - 1.94, below
  2b - 2 log 2 = 2b - 1.39.
- A shorter finite form exists: on one fixed periodic strip of width L the comparison is a
  finite-dimensional perturbation statement in e^(-b) (the pattern of Example KIN-7). It is not the
  infinite-volume statement of the note.

The reading "This is Example KIN-7 without a box" is a loose analogy (KIN-7 is a large-beta_L dip at
beta_M -> infinity on a one-sheet box; Q8-INF is the beta_L = 0 end of GH2_2). No claim rests on it.

**Verdict C4: HOLDS AFTER CORRECTION.** The bond weights, the factor 2 and rate(0) = 2b - 2 log 2
+ o(1) < 2b + o(1) = rate(infinity) are right at leading order. Corrected text for the first line:
"Example Q8-INF (argued counterexample, at leading order of a low-temperature expansion that is
not written out, to (M) in its K-neutral form for frozen Q_8 at large b in infinite volume: rate is
the decay rate of truncated correlations of gauge-invariant local observables that are invariant
under K, equivalently in a pure phase. In the class of step 1, all gauge-invariant local
observables in symmetric finite-volume measures, Q_8 at large b has rate 0 at both ends, because the
K-charged correlations of rho do not decay; there (M) holds trivially and (W) is false)."

## C5. Step 5: (M) needs sharp rates at both ends; the small-b guide for (END-0). The "needs ... first" claim FAILS; the rest HOLDS AFTER CORRECTION; the guide HOLDS at leading order.

Checked by hand (Claude Opus 5.5).

**(W) ends "on file, given OpenAI's Theorem 3.1".** At beta_L = 0 the measure in (rho, v) is (DEC1)
exactly (C1), so every gauge-invariant local observable is a function on the decorated O(4)
ferromagnet and (DEC4) applies (free subgraphs; tori with sides at least C Xi(b)). At
beta_L = infinity on a simply connected box the two sheets are independent O(4) models; for joint
observables Cov(F, H) = E_2 Cov_1(F, H) + Cov_2(E_1 F, E_1 H) reduces to Theorem 3.1 for one sheet
(one line; not written in the note). HOLDS for boxes. Scope: at beta_L = infinity on a torus, or on
a free subgraph with a hole, flat holonomies stay (Remark TOR); Theorem 3.1 for such twisted sheets
is not on file. The brief's class includes tori.

**(END-0) "that is, the rate of the decorated O(4) model is at least twice the rate of c(x)".**
The rho channel gives rate(infinity) <= 2 rate(c) rigorously (E[rho(0) . rho(x)] = c(x)^2 and
E rho = 0). So "rate(DEC) >= 2 rate(c)" implies (END-0); the converse needs rate(infinity) =
2 rate(c), which is the physics of C1 scope note 2. Corrected text: "(END-0) follows from 'the rate of
the decorated O(4) model at coupling b is at least twice the rate of c(x)', and is equal to it if
rate(infinity) = 2 rate(c)." HOLDS AFTER CORRECTION.

**"A sufficient form is E_DEC[rho(0) . rho(x)] <= C c(x)^2."** Not shown. That bound controls one
channel; (END-0) is about every gauge-invariant local observable at beta_L = 0. Corrected text: "A
necessary form (given rate(infinity) = 2 rate(c)) is E_DEC[rho(0) . rho(x)] <= C_eps e^(eps abs(x))
c(x)^2. It is sufficient only together with a statement that the rho channel carries the slowest
decay of the decorated model; no file has that statement." HOLDS AFTER CORRECTION.

**"A proof of the monotone form needs sharp rates at both ends first."** FAILS. First failing line:
that sentence (the "Consequence" bullet of step 5). Counterexamples in the lane's own files: Proposition
DIL of row 1081 proves m(t) - m(s) >= (t - s)(nu_1 - 2 n_0(s)), hence a non-decreasing gap on one-sheet
boxes when n_0(0) <= 3/4 (Corollary N2-SMALL: n = 2, beta_M <= 3/2), and Corollary KIN-3 of row 1076
gives m(beta_L) >= m(infinity) in the frustration-free case. Neither uses a rate at either end. A sign
such as (FLUX-EXC) uniform in the box would prove (M) with no rate known at either end; (END-0) would
then be a corollary, not an input. Corrected text: "(M) contains (END-0), a comparison of the true
rates at the two ends. Lower bounds of the type of Theorem 3.1, with constants that are not named,
cannot give it, and no file has it. So a proof of (M) must compare true rates directly (for example
by a sign such as (FLUX-EXC) uniform in the box); a lower bound at each end is not enough. The weak
form is the form whose two ends are theorems (given Theorem 3.1, on boxes)."
The same correction applies to the RESULT line of row 1109 ("the monotone form needs sharp rates at
both ends").

**Small-b guide for (END-0).** Re-derived at leading order.
- u = I_2(b)/I_1(b) is the one-bond mean E[Psi . Psi'] = d/db log((2/b) I_1(b)) and the spin-1/2
  character coefficient lambda_(1/2)(b); u = b/4 + O(b^3).
- rate(c): the strong-coupling expansion of c(x) is a sum over self-avoiding paths with weight u per
  step. Directed paths along an axis have, per column, the factor 1 + 2 sum_(l >= 1) u^l =
  1 + 2u/(1 - u) (a vertical run up or down between two horizontal steps). So
  rate(c) = - log u - log(1 + 2u/(1 - u)) = - log u - 2u + O(u^2). Backward steps and vacuum loops
  enter at higher order. HOLDS.
- beta_L = 0: integrating v_e convolves two half-edge weights, so the rho bond has character
  coefficients lambda_j^2, in particular u^2 for spin 1/2. The rho two-point function has rate
  - 2 log u - 2u^2 + O(u^3). At small b it is the slowest channel at beta_L = 0 (K-neutral channels
  need two paths). HOLDS.
- beta_L = infinity: the slowest channels at small b are two spin-1/2 paths (rho . rho = c^2, and the
  one-sheet singlets); a single spin-1 path costs lambda_1 = (2/3) u^2 (1 + O(u)) per step, a larger
  rate. So rate(infinity) = 2 rate(c) = - 2 log u - 4u + O(u^2) at small b. HOLDS (physics of the
  expansion at leading order; this also settles C1 scope note 2 at small b at the same grade).
- Difference rate(0) - rate(infinity) = 4u + O(u^2) > 0. HOLDS at leading order. Reading: at
  beta_L = 0 the two sheet paths are glued into one path of weight u^2 per step, which loses the
  transverse entropy 2u of each of the two free paths.
The guide is a leading-order count, not a proof; no remainder is bounded.

Verdict C5: the claim "a proof of (M) needs sharp rates at both ends first" FAILS (counterexamples
above; corrected text above). The end statements HOLD AFTER CORRECTION (two wording corrections and the
torus scope). The small-b guide HOLDS at leading order, guide grade.

## C6. Step 5: Example INT-2 (and the three tries (3a)-(3c)). HOLDS (one notation fix).

Checked by hand (Claude Opus 5.5).
- With U = [[c, -s], [s, c]] (c = cos theta, s = sin theta), S = U Lambda^(1/2): S* S = Lambda.
  U^T diag(d_1, d_2) U = [[c^2 d_1 + s^2 d_2, cs (d_2 - d_1)], [cs (d_2 - d_1), s^2 d_1 + c^2 d_2]].
  With d_1 = w^a, d_2 = 1 and the factors Lambda^(1/2) on both sides:
  T_11 = w^a c^2 + s^2, T_22 = e^(-m)(w^a s^2 + c^2), T_12 = e^(-m/2) s c (1 - w^a). Matches the note.
- Structure: T(w) = w^a S* P_1 S + S* P_2 S with both coefficients positive semi-definite; all
  entries >= 0 for w in [0, 1], theta in (0, pi/2); T_12 > 0 for w < 1 (irreducible); N >= 0 with the
  flux-free vector e_2. Ends: T(1) = Lambda, gap m for every theta; T(0) = S* P_2 S has rank one,
  gap infinite. HOLDS.
- Avoided crossing. At eps := w^a = e^(-m): T_11 - T_22 = s^2 (1 - eps^2) and T_12 = eps^(1/2) s c (1 - eps).
  The splitting is 2 eps^(1/2) theta (1 + O(theta)), the mean level is eps (1 + O(theta)), so the gap
  there is 2 theta e^(m/2) (1 + O(theta)): as small as wanted, while both end gaps stay >= m. HOLDS.
- At theta = 0 the example is Example KIN-6 with c = 0 (S = diag(1, e^(-m/2)), N = diag(a, 0)). HOLDS.
- Notation fix: with w = e^(-t/4) and D = e^(-tN), N = diag(a, 0) gives D = diag(w^(4a), 1), not
  diag(w^a, 1). Read "N = diag(a/4, 0), a a positive integer" (then 4N has integer spectrum, as
  Corollary KIN-D needs, and D = diag(w^a, 1)). Nothing else changes.
- Scope (relevant to C7): INT-2 lies in the class that Corollary KIN-D uses (S* e^(-tN) S, N >= 0,
  4N with integer spectrum, a non-negative kernel). It does not have the further structure of the
  model: there e^(-tN) is a positivity-preserving semigroup that fixes the strictly positive constant
  vector, the flux-free sector is infinite-dimensional (all functions of the rho(k)), and the face
  vacuum carries flux on every cut (Lemma FACE-FLUX). In INT-2 the face vacuum e_1 carries all the
  flux and the excited vector is flux-free (the KIN-6 pathology). So INT-2 refutes an interpolation
  that uses only the class of KIN-D, which is what the note claims; it does not refute one that uses
  the further structure.

The three tries of way 3:
- (3a) For 0 <= w <= w' <= 1, T(w') - T(w) = sum (w'^k - w^k) A_k >= 0, so each ordered eigenvalue is
  non-decreasing in w (min-max) and lambda_1(w)/lambda_0(w) <= lambda_1(1)/lambda_0(0); the right side
  is e^(-m(infinity)) lambda_0(1)/lambda_0(0), whose second factor is the volume factor of KIN-2. The
  Cauchy-Schwarz bound is that of KIN-D. HOLDS.
- (3b) m = 2 log lambda_0 - log(lambda_0 lambda_1), a difference of two convex functions of t
  (KIN-CVX); end values of such a difference do not bound it inside (every C^2 function is one). HOLDS.
- (3c) A maximum-principle bound needs control on the whole boundary of a complex domain, that is, at
  complex w, where the weights are complex and only abs Z(w) <= Z(abs w) is given. Zero-freeness
  uniform in the box is Route Z (crux Z6, open on file). HOLDS as a description.

Verdict C6: Example INT-2 HOLDS as a counterexample to the interpolation step in the class of
Corollary KIN-D, with the notation fix above.

## C7. The three named failures: failures of the method as written, or gaps a short argument closes? All three are failures of the method as written (way 2 after the C4 correction). One correction to the test table.

Checked by hand (Claude Opus 5.5). For each way I asked: does an argument of a few lines, from files on
hand, close the stated failure? None does.

**Way 1 (Lemma KIN-G, bound per unit length; stops at the self term).** HOLDS as a method failure.
- What is solid: in GH2 the kernel of N on K is infinite-dimensional (every function of the rho(k)),
  so nu_1(N) = 0 and Proposition DIL has no dilute range at all; summed over cuts its loss
  2t <psi, N psi> grows with the box (C2). This kills DIL for both forms of (INT-CMP): for (M) (no
  sign) and for (W) (no box-uniform lower bound on m(t)).
- The class argument is sound: Example KIN-7 has Lemma KIN-G's structure, D <= 1, D = 1 on flux-free
  vectors, a positive kernel and a face gap, and its sign is wrong (C2). So no inequality built from
  those facts alone closes the step.
- Further evidence that no short argument exists: on the two-site strip the derivative form (FLUX-EXC)
  is false for b >= 3.2 (guide, step 7 of the note, confirmed from the JSON in C0). So a box-uniform
  per-unit-length sign must use b <= about 3 and the window; nothing on file does that. Row 1081's
  three failed ways for the same sign at n = 2 point the same way.
- Caveat: the diagnosis "the self term" rests on the string/self/contact decomposition, which the
  note marks as physics reasoning. The failure itself does not need that decomposition.

**Way 2 (exact integration and the lift test).** HOLDS AFTER CORRECTION as a method failure.
- Form A, Lemma LOOP, the diamagnetic bound and the hand values HOLD (C3). Part (i) of the lift test
  is Corollary KIN-1. Part (ii): the loop weight is signed, so abs(W) <= 1 bounds partition functions,
  not normalised means; that blocks the simple loop route (it is not a proof that no loop route
  exists).
- The class obstruction "lifting levels does not give gaps" needs Q8-INF in its K-neutral form
  (correction of C4): in the class of the note's (W)/(M), both Q_8 rates are 0 and Q8-INF refutes
  nothing. In the K-neutral form it holds at leading order (C4, with the strip guide). Example KIN-7
  carries the same obstruction on a small box. The level statements that way 2 uses hold for Q_8 in
  operator form (Lemma KIN-G holds for every compact group), so the obstruction applies.
- The C4 guide adds: for Q_8 the K-neutral rate at beta_L = 0 is below the rate at infinity already at
  b = 2.4 on periodic strips of width 3 to 5 (by 2.2 to 2.5). So the obstruction is not only a
  large-b effect.
- Correction (step 6 test table, row "Frozen Q_8"): "Every statement argued here holds for Q_8" is
  too broad. Lemma LOOP and the hand values of W use the moments of the uniform law on S^3 and the
  SU(2) characters; for Q_8-valued fields the fourth moments differ (E s_1^4 = 1/4, E s_1^2 s_2^2 = 0,
  against 1/8 and 1/24 on S^3), so the pairing formula of Lemma LOOP does not hold as written.
  Corrected text: "The operator statements argued here (Lemma KIN-G, D <= 1, D = 1 on flux-free
  vectors, a positive kernel, the coordinates (rho, v)) hold for Q_8; Lemma LOOP and the hand values
  of W are SU(2) statements, and Lemma FACE-FLUX is stated with Lie-algebra generators, so for Q_8 it
  needs a restatement (not checked here)." The class obstruction uses only the operator statements,
  so it stands.

**Way 3 (interpolation in w; Example INT-2; (NO-1ST)).** HOLDS as a method failure.
- INT-2 HOLDS in the class of Corollary KIN-D (C6). It survives more structure than the note claims:
  take N = [[1, -1], [-1, 1]] (a Markov generator; e^(-tN) is positivity preserving and fixes the
  strictly positive vector (1, 1)), V the orthogonal matrix with columns (1, -1)/sqrt 2 and
  (1, 1)/sqrt 2, and S = V U Lambda^(1/2). Then S* S = Lambda, the face vacuum S e_1 carries flux, and
  S* e^(-tN) S = Lambda^(1/2) U^T diag(e^(-2t), 1) U Lambda^(1/2): INT-2 with w^a = e^(-2t) (4N has
  spectrum {0, 8}). So the avoided crossing is not excluded by a Markov flux semigroup, a strictly
  positive flux-free vector, or a face vacuum with flux. (Here S itself has a negative entry; whether
  a positivity property of the model's S = K_Phi^(1/2) e^(-V_f/2) excludes such crossings is not
  settled here.)
- The missing statement (NO-1ST), stated with a gap bound uniform in the box, contains (W) at every
  beta_L; so way 3 reduces the step to a statement at least as strong as the target. No short argument
  closes that.

**Verdict C7.** Way 1: HOLDS (failure of the method). Way 2: HOLDS AFTER CORRECTION (Q8-INF in its
K-neutral form; the test-table sentence corrected as above). Way 3: HOLDS (failure of the method;
INT-2 holds even with a Markov N). I found no short argument that closes any of the three.

## C8. Is the stop by the third rule valid? HOLDS (valid), with three qualifications.

The rule (row 1109 brief): "one named step that failed in three written ways, the association ports of
row 1084 not counted."
- One named step: (INT-CMP), a box-uniform comparison of the first K-neutral level with the vacuum
  level of S* D S at interior beta_L, b in the window, with a sign form (for (M)) and a bounded form
  (for (W)). Named and stated. Yes.
- Three written ways: the three methods that the brief prescribes, (1) Lemma KIN per unit length,
  (2) exact integration and the lift test, (3) interpolation in w. Each is written out, and each stops
  at a named point (C7). Yes.
- None by association: no step uses association, monotone coordinates or FKG (step 6, row GH-NA).
  Yes.
- Each failure is a failure of the method, not a gap a short argument closes (C7). Yes.
- No hand counterexample to (M) for SU(2) exists in the file (the strip result is a guide, at b >= 4,
  outside the window, on a strip narrower than any reasonable L_0), so the second rule does not apply.

Qualifications.
1. The three ways hit (INT-CMP) mainly in its sign form. For the bounded form, way 3 (INT-2) is a real
   attempt, way 1 fails by the volume factor of Proposition DIL (nu_1(N) = 0), and way 2 only notes
   that it gives no bound and that the first unprovided input is (GH5) of row 1084. So the stop is
   strongest for (M). For (W) it rests on way 3, on the DIL volume factor and on row 1084's (GH5).
2. Way 2's citation of Example Q8-INF needs the K-neutral qualifier (C4). With it, the failure stands.
3. Lines of the RESULT of row 1109 that need correction (they are not part of the stop's reasoning):
   "the monotone form needs sharp rates at both ends" (FAILS, C5); "Example Q8-INF ... for frozen Q_8"
   (add "K-neutral form", C4); "(M) is true only where the sheets are disordered at the gauge scale" is
   listed under ARGUED, but the note's own marks table gives it "physics reasoning; guide grade", so it
   belongs under GUIDE.

Verdict C8: the stop by the third rule is valid.

## Summary of verdicts

| Item | Verdict | Correction or note |
|---|---|---|
| C1 coordinates (rho, v); decorated O(4) ferromagnet plus six-spin term | HOLDS | beta_L = infinity line needs a simply connected box; "rate at infinity = 2m" is physics for the one-sheet channel |
| C2 Lemma KIN-G | HOLDS | implicit line [C_k, G] = 0 (true) |
| C2 Lemma FACE-FLUX | HOLDS AFTER CORRECTION | add: <J_k^i> = 0 because the mean vector is SO(3)-invariant; in the per-cut DIL bound read psi = S Omega_f / norm (top vector of S S*) |
| C3 form A, Lemma LOOP, diamagnetic bound, three hand values of W | HOLDS | simply connected free box |
| C4 Example Q8-INF | HOLDS AFTER CORRECTION | counterexample to the K-neutral form of (M); in the note's class both Q_8 rates are 0. Factor 2 and 2b - 2 log 2 right at leading order (guide run: difference -> -1.3863). Expansion writable by standard means; the lower bound at infinity needs a refined wall count |
| C5 "(M) needs sharp rates at both ends first" | FAILS | Proposition DIL (row 1081) and Corollary KIN-3 (row 1076) prove monotone inequalities with no rate at either end; corrected text in C5 |
| C5 end statements ((W) ends; (END-0) wording; "sufficient form") | HOLDS AFTER CORRECTION | "that is" -> "follows from"; the rho bound is necessary, not shown sufficient; tori at beta_L = infinity not covered |
| C5 small-b guide for (END-0) | HOLDS at leading order (guide) | rate(0) - rate(infinity) = 4u + O(u^2) re-derived |
| C6 Example INT-2; (3a)-(3c) | HOLDS | notation: D = diag(w^(4a), 1) for N = diag(a, 0) |
| C7 way 1 | HOLDS (method failure) | the "self term" diagnosis is physics reasoning; the failure does not need it |
| C7 way 2 | HOLDS AFTER CORRECTION (method failure) | needs Q8-INF in K-neutral form; step-6 sentence "every statement holds for Q_8" corrected |
| C7 way 3 | HOLDS (method failure) | INT-2 survives a Markov flux semigroup |
| C8 stop by the third rule | HOLDS (valid) | strongest for (M); for (W) it rests on way 3, the DIL volume factor and (GH5) |
| Side finding: step-7 run table | one cell not supported | b = 4, heat-kernel column: +2.0e-3 on (0, 3], not "below 0" |

## What this check did not cover

- Row 1108, row 1112 and OpenAI's paper (Theorem 3.1, estimate (3.61)) were not read; I used them only
  as the lane's files report them.
- The low-temperature expansion behind Q8-INF is judged writable; I did not write it.
- The string/self/contact decomposition of step 2 and the order/disorder reading and scale regions of
  step 4 (iii) are physics reasoning; I did not check them as lemmas.
- Step 6 rows other than "Frozen Q_8" were read, not checked line by line.
- The step-7 runs were not re-run; I re-derived their operator and recomputed the table from the JSON.
- One guide run of my own (Q_8 strips, `runs/gap-descent-first-case-check-opus/q8strip.py`); it guides only.
- Tori, as in the note.
- This is a same-provider check (Claude Opus 5.5 on a Claude Fable 5.2 file). It is not independent of
  provider. No mass gap is claimed.

RESULT: Row 1113 (Claude Opus 5.5 max, laptop subagent; same-provider check of row 1109, written by Claude Fable 5.2 medium; not independent of provider): the stop by the third rule is VALID; C1 coordinates (rho, v) and the decorated-O(4)-plus-six-spin form HOLD (scope: the beta_L = infinity line needs a simply connected box, "rate at infinity = 2m" is physics for the one-sheet channel); C2 Lemma KIN-G HOLDS and Lemma FACE-FLUX HOLDS AFTER CORRECTION (a missing line: <J_k^i> = 0 because the mean vector is SO(3)-invariant; the per-cut DIL bound needs psi = S Omega_f / norm, the top vector of S S*); C3 form A, Lemma LOOP, the diamagnetic bound and the three hand values of W HOLD; C4 Example Q8-INF HOLDS AFTER CORRECTION (the factor 2 and rate(0) = 2b - 2 log 2 + o(1) < 2b + o(1) are right at leading order, a guide run on periodic strips gives m_0 - m_inf -> -1.3863; it refutes only the K-neutral form of (M), since in the note's class both Q_8 rates are 0; the expansion is writable by standard means, the bound at infinity needs a refined wall count); C5 the claim "a proof of (M) needs sharp rates at both ends first" FAILS (Proposition DIL and Corollary KIN-3 give monotone inequalities with no rate at either end; corrected text given), the end statements HOLD AFTER CORRECTION, the small-b guide for (END-0) HOLDS at leading order (difference 4u); C6 Example INT-2 HOLDS (notation D = diag(w^(4a), 1)); C7 all three named failures are failures of the method as written (way 2 after the C4 correction; INT-2 survives a Markov flux semigroup; the step-6 sentence "every statement argued here holds for Q_8" corrected); side finding: one cell of the step-7 run table (b = 4, heat-kernel column) is not supported by the runs. No mass gap claimed. Output `library/gap-descent-first-case-check-opus.md`.
