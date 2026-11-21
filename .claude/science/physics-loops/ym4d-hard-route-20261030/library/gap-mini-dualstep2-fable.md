lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-21T19:05Z

# Row 1360, `gap-mini-dualstep2-fable`: the dual-class block step (independent attempt)

Worker: Claude Fable 5.2 (max), Mac mini worker 1, one session, pinned at commit 149762b33. Checked by no one.
Research-stage working state. Nothing here is a public claim. Row 1358 (`gap-mini-dualstep-fable`) is the sibling
attempt on the same problem; this row does not read it.

## Status log

- 2026-11-21T07:05Z (date -u): file created. Read so far: GOAL.md, FINISH.md rule sections (How we work, Working efficiently,
  Rules), the queue row 1360. Next: the RESULT lines of rows 1351, 1354, 1356, 1357, then `parts/gap.md`.
- 07:05Z (date -u): read row 1354 (`library/gap-mini-nphys-fable.md`, whole): classes (10), (10*), Lemma B0,
  Proposition B, Corollary B1, Theorem E, the open step (BS*) of its 6.1 and the three stops of its 6.2.
- 07:17Z (date -u): read check row 1357 (verdict paragraphs on Theorem E, (BS*), the packet Fourier transform) and
  the RESULT lines of rows 1332, 1340, 1341, 1345, 1348, 1351, 1352, 1353, 1355, 1356. Row 1358 not read.
- 2026-11-21T07:31Z (date -u): read row 1345 L5-110 (maps (1)-(3), bounds (4)-(9)), row 1351 L106-152 (class (10), the
  deletion induction, obstruction (13)), check row 1347 RESULT and its lines on (7), (8). Section 1 written.
- 2026-11-21T07:32Z (date -u): Section 2 written (Lemma D1, Lemma A, Lemma T, Theorem N).
- 2026-11-21T07:34Z (date -u): Section 3 written (Proposition TOP, Corollary TOP1, Lemma FR, the three cases).
- 2026-11-21T07:35Z (date -u): criteria of the guide run written (Section 5); numeric lock acquired (holder row1360-fable,
  memory free 66 percent by memory_pressure).
- 2026-11-21T07:39Z (date -u): guide run done and lock released; results in 5.3 (C0, C1 passed; C2 failed marginally at
  one step, reported).
- 2026-11-21T07:44Z (date -u): cross-branch search done (main, PR #10114: no hit); Section 4 written (the corrected open
  step, attempts at a thick map, Proposition EP).
- 2026-11-21T07:48Z (date -u): line anchors of rows 1345 and 1351 corrected from `grep -n`; 4.6, Sections 6 and 7 written.
- 2026-11-21T07:49Z (date -u): 3.5 added (quantitative form of Lemma FR, sketched).
- 2026-11-21T07:50Z (date -u): 4.3 item 4 added (the collar); Not done completed.
- 2026-11-21T07:51Z (date -u): hand arithmetic of Lemma A, Lemma T and Remark N1 confirmed with exact Bessel values (one second,
  under the numeric lock, memory free 64 percent): 0.6574 at 59, 1.0144 at 58, 6 sqrt(u) = 0.830 at 245.

## Repo search

- This folder: the registry grep of Section 1 ("Rule 0a"), run before the attack.
- origin/main and PR #10114 (branch claude/ym4d-proof-draft), by a bare blob-less depth-1 fetch into a scratch
  folder, 2026-11-21T07:44Z (date -u): the 67 `.md` files of main with "ym4d" in the path (25 of them contain "Wilson") and the
  21 mass-gap files of PR #10114 (`MASS_GAP_*`, `RTARGET`, `PROOF` and files with "gap" in the name) have no hit
  for: "t Hooft loop", "thin monopole", "signed packet", "packet sign", "electric sheet", "centre sheet",
  "center sheet", "vortex free energy", "thick vort", "Mack". PRs #10133, #10134, #10141, #10144 were not searched.

## 1. How best to attack it (decision, written 2026-11-21T07:31Z, date -u)

**1.1 The problem in parts (from rows 1332 6.1, 1354 1.2 and 6.1; nothing new).** A proof by Proposition CH needs:
(i) the account's carry to the first passage; (ii) block steps that keep both masses, at an effective coupling of
order one; (iii) an end class with a hand end theorem. Row 1354 names the end class: the Fourier-dual class (10*)
of its Theorem E. It also names the map: the centre-sign block map of row 1345, "read in the dual variable" (its
6.2 item 1), with the hope that the electric sheets become rare "after the angular environment is integrated, by
cancellation" (its 4.4). Its open step is (BS*) of its 6.1.

**1.2 Decision.** Row 1354 tested the class (10) of row 1351 by an invariant (the eight twisted masses) before
anyone tried to land in it. I do the same for (10*). The invariant is larger than the twisted masses: the Wilson
masses with a sign on whole packets, Z_tau, for all sign patterns tau of the coarse plaquettes, closed or not.
They are intrinsic numbers of the Wilson theory (thin 't Hooft loops on the coarse dual lattice). A representation
of the coarse model of row 1345 must reproduce all of them, and the class (10*) restricts all of them. So the
proposal can be decided before any angular integral is attempted.

**1.3 Outcome of the test (Sections 2 and 3).** The proposal fails at every late cutoff and every block side:

- Theorem N: for beta >= 59 the packet-sign masses of Wilson are not the masses of any model of (10*).
- Proposition TOP: at late cutoffs the coarse centre sector of row 1345 is topological. The weight of a coarse
  electric sheet depends only on its homology class, up to an error that tends to zero. Bounding sheets are not
  rare. They all have the weight of the empty sheet.
- Lemma FR: with independent link variables and plaquette-local rules, a frozen closed sign field has a fixed
  class. So the format of row 1351 cannot hold a frozen centre with a free class.

**1.4 What is then left (Section 4 on).** The dual class can be reached only through a coarse centre variable that
is thick, that is, through a map that integrates angular variables inside blocks. No exact map on file does this.
I then try the thick step itself and record where each attempt stops.

**Rule 0a (searched before writing; counts are files among `library/gap-*.md`, `library/prior/gap-*.md`,
`parts/gap.md`).** "sign-source": 0. "thick monopole": 0. "thin monopole": 1 (`gap-brainstorm-max.md` L504, idea G18
of row 859: "Thin monopoles freeze at large beta; the thick w_2 needs a multiscale definition. Restates (V) at
order one"; its L335, idea 47 (d), states the equidistribution of the Stiefel-Whitney class). "packet sign" /
"signed packet": rows 1345, 1351, 1354 and check 1357 only. `library/open-core.md` has no line on (10*), on the
dual class or on (BS*). Nearest statements on file, used and credited below: row 1345 (7), (8), (9) (gpt-6.2-astra;
check row 1347, Claude Opus 5.5: HOLD); row 1354 6.2 item 1 and check 1357 L87-97 (the packet Fourier transform;
"Uniform near-independence of arbitrary packet signs would need control of the sum of the Fourier errors"; the
check corrects row 1354's "classical cost" by row 1345's bound). Neither row draws the conclusion of Theorem N.
origin/main and PR #10114 were searched after the attack (see "Repo search" above): no hit.

## 2. Theorem N: the packet-sign masses of Wilson are not the masses of a model of (10*) (written 2026-11-21T07:32Z, date -u)

Credit. G. Mack and V. Petkova for the centre split. G. 't Hooft for the loop operator that Z_tau realizes.
gpt-6.2-astra for the block map and the bounds (7), (8) of row 1345, and for the deletion induction of row 1351.
Claude Fable 5.2 (row 1354) for Theorem E and the packet Fourier transform. The checks are rows 1347, 1352, 1357.

**2.1 Setting.** Fine periodic torus Lambda. Weight e^(beta q(U_p)), q = tr/2, Haar links.

- For a sign pattern tau in C^2(Lambda; F_2), one sign for each fine plaquette, put
  Z[tau] = integral of prod_p exp(beta (-1)^(tau_p) q(U_p)) dU. Z[0] is the periodic Wilson mass.
- Blocks of side B as in row 1345 L18-28. The coarse torus Lambda' has v sites, 4v links, 6v plaquettes and
  4v three-cubes. The packet S_B(P) of a coarse plaquette P is the set of the B^2 fine plaquettes at its two
  cuts. For tau' in C^2(Lambda'; F_2) let i(tau') be the fine pattern that equals tau'_P on S_B(P) and 0 off the
  packets. Put Z'[tau'] = Z[i(tau')]. These are the "signed packet" masses of row 1345 L73-79.
- A(beta) = integral of e^(beta q) dU = 2 I_1(beta)/beta.

Facts on file:

- (F1) Z'[tau' + d xi'] = Z'[tau'] for every coarse link pattern xi' (row 1345 L89; check 1357 L95).
- (F2) Z'[tau'] = integral over a_B(dy, d rho) of E_t exp(sum_P (-1)^(tau'_P) J'_P(y, rho) (dt)_P) (row 1345
  (2), (3)). So tau' changes the sign of the coefficient J'_P and nothing else.
- (F3) For every tau and every set D of fine plaquettes that share a coordinate direction, the mass with the
  signs tau and with the factors of D deleted is at most A(beta)^(-|D|) Z[0]. In particular 0 < Z[tau] <= Z[0]
  (row 1345 (7); check 1347 L148: HOLDS).
- (F4) If k coarse cubes have (d tau')_c = 1 and 6 sqrt(u_beta) < 1, then Z'[tau'] <= q_B^k Z[0], with
  u_beta = e^(17 beta/18)/A(beta) and q_B = (6 sqrt(u_beta))^(B/19) (row 1345 (8); check 1347 L158-160: HOLDS).

**2.2 Definition (a representation with its packet signs).** Let M be a model of the class (10*) on Lambda':
independent link variables x, scalars a_P > 0, plaquette functions alpha_P, beta_P with the bounds (10*) (row 1354
3.1), or the moment form with component factorization that check 1357 L81 admits. For tau' let M^(tau') be M
with beta_P replaced by (-1)^(tau'_P) beta_P. It is in the class, with the same constants, because every
hypothesis is a bound in absolute value. Write Per(M) for the periodic mass,

    Per(M) = prod_P a_P  sum over cycles S of E[ prod_{P in S} beta_P  prod_{P not in S} alpha_P ].

M represents the Wilson theory *with its packet signs*, with the scalar K > 0, if Z'[tau'] = K Per(M^(tau'))
for every tau'.

Which representations have this property (PROVED, one line). By (F2), Z'[tau'] is the integral over a_B of the
function sum over cycles S of prod_{P in S} (-1)^(tau'_P) sinh J'_P prod_{P not in S} cosh J'_P of the coefficient
array. So every re-expression of the coarse model of row 1345 that changes the environment variables only has
the property: it is enough that the array (a_P alpha_P(x), a_P beta_P(x))_P under K times the product law has
the joint law that (cosh J'_P, sinh J'_P)_P has under a_B. This is the reading of row 1354 4.4 and 6.2 item 1.
A representation that matches only the eight (or 64) twisted masses does not have it and is not covered.

**2.3 Lemma D1 (the class side; PROVED GIVEN the deletion induction of row 1351 L134 in the dual form of Theorem
E, checked in rows 1352 and 1357 L45).** For every model M of (10*) and every coarse plaquette P_0,

    511/513 <= Per(M^(1_{P_0})) / Per(M) <= 513/511.

For a pattern tau' with n nonzero entries the ratio Per(M^(tau'))/Per(M) lies between (511/513)^n and (513/511)^n.

Proof. For a set D of coarse plaquettes let Q_D be the sum, over cycles S inside D and sets X inside D disjoint
from S, of E[prod_S beta_P prod_X h_P], h_P = alpha_P - 1. Then Per(M) = prod a_P times Q_T, T the set of all
plaquettes. The deletion induction says: for every D and every P in D, Q_(D minus P) > 0 and
|Q_D / Q_(D minus P) - 1| <= 1/512. (Row 1351 L134 proves this for the class (10) at |s| <= 2; Theorem E's proof
is the same induction for primal cycles; I use s = 1 and the trivial character.) The terms of Q_T that do not use
P_0 are the terms of Q_(T minus P_0). They do not contain beta_{P_0}. So Q_(T minus P_0) is the same number for M
and for M^(1_{P_0}). Both models satisfy the hypotheses. So both values of Q_T lie within the factor 1 +- 1/512
of the same positive number, and their ratio lies between (1 - 1/512)/(1 + 1/512) and its inverse. For n signs
change one sign at a time; every intermediate model is in the class. QED

**2.4 Lemma A (a hand bound for A; PROVED).** For beta >= 3/2,

    A(beta) >= (4/(3 pi)) (3/(2 beta))^(3/2) e^(-3/2) (2 - 3/(2 beta))^(1/2) e^beta.

Proof. In the class angle, Haar measure of SU(2) has the density (2/pi) (1 - q^2)^(1/2) in q on [-1, 1]. For
0 < eta <= 1 restrict the integral to q >= 1 - eta, where e^(beta q) >= e^(beta (1 - eta)) and
(1 + q)^(1/2) >= (2 - eta)^(1/2). The integral of (1 - q)^(1/2) over [1 - eta, 1] is (2/3) eta^(3/2). Take
eta = 3/(2 beta). QED

Numbers: (4/(3 pi)) (3/2)^(3/2) e^(-3/2) = 0.17397. At beta >= 59 the square root is at least 1.4052, so
A(beta) >= 0.24446 e^beta beta^(-3/2). (The true constant is (2/pi)^(1/2) = 0.798; it is not needed.)

**2.5 Lemma T (the Wilson side: one thin monopole cube; PROVED GIVEN (F3); new here, unchecked).** Let tau have
at least one fine three-cube c with (d tau)_c = 1. Then

    Z[tau] <= 3 ( e^((sqrt 3 / 2) beta) / A(beta) )^4  Z[0].

For beta >= 59 the right side is at most 0.658 Z[0].

Proof. Step 1 (Bianchi with signs; the argument of row 1345 L81 with the geodesic distance in place of the
chord). Let h_1, ..., h_6 be the six face holonomies of c, based at one vertex and ordered as in row 1345 L81, so
that h_1 ... h_6 = 1. Put g_i = (-1)^(tau_i) h_i. The signs are central and their product is -1, so
g_1 ... g_6 = -1. The distance d(g, g') = arccos(tr(g^(-1) g')/2) on SU(2) = S^3 is bi-invariant and obeys the
triangle inequality, so pi = d(1, -1) <= sum_i d(1, g_i). Put theta_i = d(1, g_i) = arccos((-1)^(tau_i) q_i),
with q_i the trace of the face (basing and orientation do not change it). So at every configuration

    theta_1 + ... + theta_6 >= pi,      (-1)^(tau_i) q_i = cos theta_i.

Step 2 (four faces with one common direction). The cube has three directions. Each face contains two of them.
For a direction k let D_k be the set of the four faces that contain k, and Theta_k the sum of their angles. Then
Theta_1 + Theta_2 + Theta_3 = 2 sum theta_i >= 2 pi, so some Theta_k is at least 2 pi/3.

Step 3 (the weight of four faces). For all theta in [0, pi], cos theta <= sqrt 3/2 - (theta - pi/6)/2. (The
right side is the tangent of the cosine at pi/6. The difference has the derivative sin theta - 1/2. It is zero
at pi/6, it increases up to 5 pi/6, and at pi it is still 1 + sqrt 3/2 - 5 pi/12 > 0. On [0, pi/6] the
difference decreases to zero.) So on the event Theta_k >= 2 pi/3 the sum of cos theta_i over D_k is at most
2 sqrt 3 - (Theta_k - 2 pi/3)/2 <= 2 sqrt 3.

Step 4. Split the integral of Z[tau] by the three events of Step 2 (a union bound). On the event for k bound
the four factors of D_k by e^(2 sqrt 3 beta), drop the indicator, and use (F3) for the pattern tau with D_k
deleted: the four faces of D_k share the direction k. This gives
Z[tau] <= 3 e^(2 sqrt 3 beta) A(beta)^(-4) Z[0].

Numbers. With Lemma A, x = e^((sqrt 3/2) beta)/A(beta) <= e^(-0.1339746 beta) beta^(3/2)/0.24446 for beta >= 59.
At beta = 59: e^(-7.9045) = 3.6906e-4, 59^(3/2) = 453.19, so x <= 0.6842 and 3 x^4 <= 0.6573. The function
e^(-0.134 beta) beta^(3/2) decreases for beta > 11.2, and the constant of Lemma A increases with beta. So the
bound holds for all beta >= 59. (At beta = 58 the same arithmetic gives 1.014; the threshold of this method is
between 58 and 59. GUIDE arithmetic with the exact Bessel value of A: the bound 3 x^4 passes 511/513 at beta = 46.9;
the constant of Lemma A is 3.24 times smaller than the true one.) QED

**2.6 Theorem N (PROVED GIVEN Lemma D1, Lemma T and (F1)-(F3)).** Let beta >= 59. Let B >= 1 be any block side
and Lambda any torus that the tiling of row 1345 admits. Then for every coarse plaquette P_0

    Z'[1_{P_0}] <= 0.658 Z'[0],

and no model of the class (10*) represents the Wilson theory with its packet signs. The same holds for the
moment form of the class, as long as it has the deletion bound of Lemma D1.

Proof. The pattern i(1_{P_0}) is the packet S_B(P_0). A fine cube that contains exactly one plaquette of the
packet has (d tau)_c = 1. There are 4B such cubes: take a plaquette of the packet at the end of the B-interval
of one transverse coordinate, and the cube spanned by it and that coordinate, pointing out of the interval (row
1345 L79 counts them: B fine cubes for each of the four coarse cubes that contain P_0). So Lemma T gives the
first claim. If M represented the theory with its packet signs, then
Z'[1_{P_0}]/Z'[0] = Per(M^(1_{P_0}))/Per(M) >= 511/513 > 0.996 by Lemma D1. This contradicts 0.658. QED

**Remark N1 (the same conclusion from checked statements only).** Without Lemma T, use (F4). The pattern
1_{P_0} has k = 4. If 6 sqrt(u_beta) <= 9/10 then Z'[1_{P_0}]/Z'[0] <= (9/10)^(4B/19) <= (9/10)^(4/19) < 0.979
for every B >= 1. With Lemma A, u_beta <= e^(-beta/18) beta^(3/2)/0.2445, and 6 sqrt(u_beta) <= 9/10 holds for
beta >= 245 (at 245: e^(-13.611) 245^(3/2)/0.2445 = 0.0192 <= 0.0225). So for beta >= 245 Theorem N rests only on
statements that rows 1347, 1352 and 1357 have checked, plus Lemma A.

**2.7 What Theorem N shows, and what it does not.**

1. (PROVED.) The hope of row 1354 4.4, that in the representation of row 1345 the electric sheets "can be rare
   only after the angular environment is integrated, by cancellation of the signs of sinh J_P", is false at
   every bare coupling beta >= 59, for every block side. The integrated quantities are the numbers Z'[tau'].
   They do not depend on how the environment is represented, and they fail the test by a factor 0.658 against
   0.996. So (BS*) of row 1354 6.1 has no realization through the map of row 1345 at any late cutoff: the bare
   coupling of the trajectory tends to infinity.
2. (PROVED.) The failure is not a matter of block size. The bound of Lemma T does not depend on B, and (F4)
   improves with B. A thin coarse monopole always costs at least one fine monopole cube.
3. It does not exclude a model of (10*) that has only the eight twisted masses of Wilson at the two periods.
   Such a model must differ from the coarse model of row 1345 in its centre variable. Section 4 says what kind
   of variable that is.
4. It says nothing at a coupling of order one: Lemma T loses the factor (e^beta/A(beta))^4, of order beta^6.
   Section 5 gives guide numbers at beta = 2.3.
5. At beta <= 1/46 Wilson is in (10*) with B = 1 (row 1354 3.2 item 2), and the test is passed there:
   1 - Z[1_p]/Z[0] is of order beta^6. So the test separates the two regimes, and the threshold of the true
   ratio lies between.

## 3. The coarse centre sector at late cutoffs is topological (written 2026-11-21T07:34Z, date -u)

**3.1 Sheet weights.** Keep 2.1. For a set S' of coarse plaquettes put

    W_B(S') = 2^(-6v) sum over all tau' of (-1)^(<tau', S'>) Z'[tau'].

Facts (PROVED; the first two are finite Fourier analysis on F_2^(6v) with (F1), the third is check 1357 L89-93):
(a) W_B(S') = 0 unless S' is a cycle; (b) Z'[tau'] = sum over cycles S' of (-1)^(<tau', S'>) W_B(S');
(c) W_B(S') = integral over a_B of prod_P cosh J'_P prod_{P in S'} tanh J'_P. So W_B(S') is the weight of the
coarse electric sheet S' in the reading of row 1354 4.4, after the environment is integrated. If a model M
represents the theory with its packet signs (2.2), then W_B(S') = K prod a_P E[prod_{S'} beta_P prod_{off S'} alpha_P].

Let C = im d' (dimension r = 3v - 3) and H^2 = ker d'/C (64 classes). By (F1), Z'[tau'] is one number Z_h on each
closed class h. For a class c in H_2(Lambda'; F_2) put X_c = (1/64) sum over h of (-1)^(<h, c>) Z_h. For c with
temporal components only this is the transform that gives the electric sector traces of row 1354 2.4 (there
over the eight temporal twists).

**3.2 Proposition TOP (PROVED GIVEN (F4); the estimate is that of row 1345 (9), read for one sheet).** Let
6 sqrt(u_beta) < 1 and eps_B = 64 [(1 + q_B)^(4v) - 1]. For every coarse cycle S', with c its homology class,

    | W_B(S') - 2^(r - 6v) 64 X_c |  <=  2^(r - 6v) eps_B Z[0].

Proof. Split the sum over tau' into closed and not closed patterns. The closed patterns are the 64 cosets h + C,
each of 2^r elements. For a closed tau' and a cycle S' the pairing <tau', S'> depends only on the classes. So the
closed part is 2^(-6v) 2^r sum_h (-1)^(<h, c>) Z_h. For the rest: a nonzero syndrome m = d' tau' with k cubes has
64 times 2^r preimages; there are at most (4v choose k) such syndromes; and Z'[tau'] <= q_B^k Z[0] by (F4). The
sum over k >= 1 is 2^(-6v) 2^r 64 [(1 + q_B)^(4v) - 1] Z[0]. QED

**Corollary TOP1 (bounding sheets are not rare; PROVED).** Since 64 X_0 = sum_h Z_h >= Z[0], for every set V' of
coarse cubes

    (1 - eps_B)/(1 + eps_B)  <=  W_B(boundary of V') / W_B(empty)  <=  (1 + eps_B)/(1 - eps_B).

For a cycle of class c the ratio W_B(S')/W_B(empty) is X_c/X_0 up to the same relative error in numerator and
denominator. At fixed coarse volumes eps_B tends to zero on the first-passage tail (row 1345 L103: v q_B -> 0,
with B = L^K or with one fixed large B).

**Reading (PROVED statements in words).** At late cutoffs the coarse centre model of row 1345 has no local
content. The weight of a coarse electric sheet is a function of its homology class. Every bounding sheet, of any
size and shape, weighs as much as the empty sheet. In the magnetic picture this says: Z'[tau'] vanishes (to
eps_B) unless tau' is closed, and then it is the class mass Z_h. The only numbers that the centre sector carries
are the 64 class masses of each torus, which are the twisted masses. Alternative I is the statement that
wrapping sheets are rare (X_c small against X_0). The class (10*) asks that *local* sheets are rare, by the
factor u^6 for the boundary of one cube. They have relative weight one. This is Theorem N again, now for all
bounding sheets, in the range of (F4).

**3.3 Lemma FR (a frozen closed rule on independent links has a fixed class; PROVED, elementary).** Let Lambda'
be a four-dimensional torus with all sides at least 3. Let the link variables x_E be independent, with any
laws. For every plaquette P let sigma_P be a measurable function of the four link variables of P with values in
F_2. Assume that d sigma(x) = 0 on every three-cube, for almost every x. Then there are link functions g_E of
x_E alone and a constant closed cochain c with

    sigma_P(x) = c_P + sum over the four links E of P of g_E(x_E)      for almost every x.

So the cohomology class of sigma(x) is the constant class of c.

Proof. Fix a link E and two plaquettes P, P' through E that lie in one three-cube. In that cube E lies in the
faces P and P' only, and P and P' share no other link. Write a for the other three links of P and b for those of
P'. The cube equation reads sigma_P(x_E, a) + sigma_P'(x_E, b) = R, where R does not depend on x_E. Write it for
two independent copies x_E and y_E and add: sigma_P(x_E, a) + sigma_P(y_E, a) = sigma_P'(x_E, b) + sigma_P'(y_E, b)
almost everywhere. The left side does not depend on b and the right side not on a, and a and b are independent.
So both sides equal one function phi(x_E, y_E) almost everywhere (fix a good b). Fix a good y_E:
sigma_P(x_E, a) = phi(x_E, y_E) + sigma_P(y_E, a). So sigma_P is a function of x_E plus a function of a. This
holds for each of the four links of P, and a function on a product that splits off each coordinate in this way
is a sum of four one-variable functions and a constant (induction on the coordinates). The same phi serves P and
P', so the one-variable parts of P and P' at E differ by a constant. The six plaquettes through E are joined by
the relation "in one three-cube" (two of them are in one cube exactly when they lie in different planes, and
any two are joined through a third). So one function g_E serves all six, and the constants go into c_P. Then
d sigma = d c, so c is closed, and sigma = c + d g has the class of c. QED

**3.4 The three cases for the format of row 1351 (the first two PROVED, the third ARGUED).** The format: independent
link variables x, positive weights w_P(x; z) on each plaquette that read the four links of P, centre curvature z
summed over C. Put b_P = (w_P(x; 0) - w_P(x; 1))/(w_P(x; 0) + w_P(x; 1)), in (-1, 1), and let mu be the positive
measure with the density prod_P (w_P(x; 0) + w_P(x; 1)) against the product law. Then the sheet weights of the
model are the mu-integrals of prod_{P in S'} b_P. Let the model represent the Wilson theory with its packet
signs at a late cutoff. By Corollary TOP1 the mu-mean of the product of b_P over the six faces of any cube is at
least (1 - eps_B)/(1 + eps_B). So under mu the field b is frozen and its sign field is closed, up to mu-mass of
the order eps_B for each cube.

- (a) The centre is nearly free: b small in the sense of (10*). Excluded by Theorem N (PROVED).
- (b) The centre is frozen and the environment is the product law itself (all w_P(x; 0) + w_P(x; 1) constant),
  with exact closure. Then Lemma FR applies to sigma = sign b: the class is fixed, one class mass is positive
  and the other 63 vanish. This is alternative II in its extreme form (PROVED). For an environment close to the
  product law in the sense of (10) the same conclusion is Proposition B of row 1354 (one heavy class).
- (c) The centre is frozen, the class is free. Then mu must give almost all its mass to configurations where a
  plaquette rule is closed and is not a coboundary of link functions. Under the product law such an event
  has probability at most (1 - p)^(number of independent cubes) with p > 0 the defect probability of one cube.
  So the density of mu is not a small perturbation of a constant: it carries a weight of order e^(const v)
  (ARGUED; the quantitative form of Lemma FR is sketched in 3.5). The Wilson theory itself is of this kind with
  B = 1: x is the SO(3) link, w_P(x; 0) + w_P(x; 1) = 2 cosh(beta q_P), and closure of sign q_P comes from the
  Bianchi identity where all plaquettes are close to the identity. No end theorem on file covers it, and it is
  the problem itself.

**3.5 A quantitative form of Lemma FR (ARGUED: the steps are written, the constants are not fixed).** (FR-q): in
the setting of Lemma FR assume only that d sigma differs from zero on each three-cube with probability at most
p. Then there are link functions g_E and constants c_P with P(sigma_P differs from c_P + sum_E g_E(x_E)) <= C p
for every plaquette, with an absolute constant C, and c is closed when (6C + 1) p < 1.

Steps. (i) The cube equation holds outside probability p. With an independent copy y_E of x_E, the two
functions F = sigma_P(x_E, a) + sigma_P(y_E, a) and G = sigma_P'(x_E, b) + sigma_P'(y_E, b) differ with
probability at most 2p. (ii) For fixed (x_E, y_E) let f be the probability over a that F = 1. Since a and b are
independent, P(F differs from G) >= min(f, 1 - f). So with phi = 1[f > 1/2] the function F differs from
phi(x_E, y_E) with probability at most 2p. (iii) By Markov's inequality one value y_0 serves the six plaquettes
through E at once, with the error 2p replaced by 14p. So each sigma_P is a function of x_E plus a function of
the other three links, outside probability 14p, and the functions of x_E for the six plaquettes agree up to
constants. (iv) Repeat for the four links of P; each step picks a good base point by Markov and multiplies the
error by a constant. (v) On a cube, the sum of the six approximants is d c, a constant; it is zero outside
probability (6C + 1) p, so it is zero.

Use. With (FR-q), case (b) of 3.4 extends from the exact product law to every environment whose marginal on
the links of one cube is comparable with the product law: the class of the sign rule is then constant outside a
small probability, and one class mass dominates. The comparison of the cube marginal with the product law in
the class (10) is the missing written step (it needs the deletion bounds with the cube variables held fixed).
Together with Theorem N this would give: no model in the format of row 1351 whose total plaquette weights are
close to constants represents, with its packet signs, a theory that is in alternative I at a late cutoff. OPEN
as a written theorem. Row 1354 Proposition B is the case of the class (10).

**Conclusion of Sections 2 and 3.** For a confining Wilson theory at a late cutoff, the coarse model of row 1345
lies in neither end class, in any representation that keeps its centre variable: not in (10*) (Theorem N), and
not in (10), which fixes one heavy class (row 1354 Proposition B; obstruction (13) of row 1351). Its centre
sector is frozen with a free class. In the format "independent links, plaquette-local weights, small local
moments" such a sector does not exist (Lemma FR and case (c)). So the chain "centre-sign map, then a local
moment test on the centre weights" is closed in both directions. This does not touch the neutral target or the
gap clause. It removes one route to them.

## 4. What a landing in a dual class must be: a thick centre variable (written 2026-11-21T07:44Z, date -u)

**4.1 The open step, corrected (OPEN).** (BS-thick): there are a block side B and, for every late cutoff, a model
M of an end class with the conclusions of Theorem E, and a scalar K, such that K times the mass of the class h of
M is the Wilson twisted mass Z_h, for the eight temporal twists at the two periods, with the common-cover rule.
By Theorem N the centre variable of M is not the pivot sign of row 1345: M is not a re-expression of that coarse
model in other environment variables. This replaces (BS*) of row 1354 6.1, which left the map open and suggested
the map of row 1345.

**4.2 Why the variable must be thick (ARGUED from Lemmas D1 and T; the numbers are GUIDE).** In a model of (10*)
the change of the sign of the odd part of one plaquette weight changes the mass by less than 0.4 percent, and a
product of such changes over a closed surface that is not exact is the twist. In the Wilson theory the operation
with this second property that acts on the fine plaquettes of one packet costs a factor 0.66 or less for
beta >= 59 (Lemma T), and about 0.34 for one plaquette at beta = 2.3 (5.3). The cost sits on the rim of the
packet, on the monopole cubes, and it does not decrease with the block side. An operation without a rim cost
must change the angular variables in a region of the size at which the centre flux spreads without cost. That
is the confinement scale. So the coarse plaquette variable of a dual landing reads the angular field in a whole
block. On file, objects of this kind are the vortex containers of Mack and Petkova (rows 1025 and 1029,
`library/gap-cr-tomboulis-max.md`) and the twisted boxes of 't Hooft (rows 720 and 1179); idea G18 of row 859
already says "the thick w_2 needs a multiscale definition".

**4.3 Attempts at an exact thick map, and where each stops.**

1. *Coarse SU(2) links with a centre-covariant kernel (decimation along straight paths, or an averaging kernel).*
   Let k(V | U) be a probability kernel from fine fields to coarse link fields V with
   k(V | (-1)^(i_1 xi') U) = k((-1)^(xi') V | U) for every coarse link pattern xi', where i_1 xi' flips the
   whole bundle of each link with xi'_E = 1. Put rho'_tau(V) = integral of prod_p e^(beta (-1)^(tau_p) q_p) k(V | U) dU.
   Then (PROVED, one substitution, using d i_1 = i d'): the integral of rho'_tau over V is Z[tau], and
   rho'_(i d' xi')(V) = rho'_0((-1)^(xi') V). So the centre of a coarse link acts on the fine theory through the
   thin bundle flip again. The Fourier transform of rho'_0 in the coarse link signs gives, for each loop pattern,
   the sum of the sheet weights over all sheets with that boundary. It does not give the weight of one closed
   sheet. Those are defined only when the coarse weight is a product of plaquette functions, and an exact map
   does not produce such a product. Stops at: the locality of the coarse weight, which is a mixing statement at
   the scale B.
2. *Sum the thin monopoles first.* The cosh-packet model W_B of row 1345 (9) is a positive local product, and
   by Proposition TOP it is the sum of all class masses up to eps_B. Its class fractions and its two-volume
   free energy are the open items that row 1345 L105 names. Nothing new here.
3. *A polymer end class in place of (10*).* A thick map can at best produce small non-local terms. The end
   theorem survives them (4.4). Then a landing is a convergent polymer representation of the eight masses with
   common local terms at the two periods. For a fixed pair of tori the existence of such a representation is
   close to the conclusion itself; the content is in a construction that a finite computation can certify. The
   suppliers on file are strong coupling (rows 701, 785) and block statements uniform over boundary values, which
   the frame test of row 1277 exposes at beta >= 2.5 (GUIDE there). Stops at: a block statement in the law of the
   model at a coupling of order one, as in rows 1340 and 1356.

4. *Hide the rim.* The rim cost of a packet disappears if the plaquette factors are deleted in a collar N of
   the coarse dual one-skeleton: with free links in N the monopole lines of any pattern tau' cost nothing, and
   the intersection parity of a closed fine sheet outside N with a dual plaquette minus its collar is a
   homology invariant. A bounding coarse sheet then needs a fine sheet that links a tube of N, of area of the
   order of the square of the collar width, and such sheets are rare in a confining theory when the collar is
   wider than the correlation length (ARGUED; the strong-coupling series shows it at small beta). But this is
   the Wilson theory with the collar deleted, a different theory. Restoring the collar multiplies each mass by
   a factor that is exponential in the length of the network, and no statement on file compares the
   two-period defects of the two theories. The closed, rim-free flips are the twists themselves, and inside
   a region with fixed boundary field they are the vortex containers of Mack and Petkova. Stops at: a coarse
   centre variable with a cheap flip exists only for closed surfaces, that is, for classes. This is
   Proposition TOP again.

**4.4 Proposition EP (the end theorem for abstract polymers; PROVED GIVEN the deletion induction and the tail
estimate of row 1351 L134-136, which use nothing else).** On T_t = (t, m, m, m), min(t, m) >= 16,
j_0 = floor(min(t, m)/8), v = t m^3. A polymer is a set gamma of plaquettes that is connected for the adjacency of
row 1351 (a common link or a common three-cube; a closed neighbourhood has at most 41 plaquettes per plaquette).
It has a real activity rho(gamma) and a class [gamma] in H_2(T_t; F_2). Assume:

- (P) for every plaquette p, the sum over gamma containing p of |rho(gamma)| (2 e^(41/256))^|gamma| is at
  most 1/512;
- (L) a polymer with fewer than j_0 plaquettes has class zero, and the polymers of T_2t with fewer than j_0
  plaquettes are exactly the two lifts of those of T_t, with the same activities;
- for each twist h the mass is Z^h(T_t) = K_t times the sum, over families of pairwise non-adjacent polymers,
  of the product of chi_h([gamma]) rho(gamma), with K_2t = K_t^2.

Then the 64 masses Z^h(T_t) are positive and within the factor e^(2 tau) of each other, tau = (12 v/256) 2^(-j_0),
and |2 log Z(T_t) - log Z(T_2t)| <= (48 v/256) 2^(-j_0) for Z = Z^0 and for the mean over the eight temporal
twists.

Proof. Mark each polymer with s^|gamma|. For a set D of plaquettes let Q_D(s) be the sum over families inside D.
For p in D, Q_D = Q_(D minus p) + sum over gamma containing p of chi rho(gamma) s^|gamma| Q_(D minus N(gamma)),
with N(gamma) the closed neighbourhood, of at most 41 |gamma| plaquettes. If every one-plaquette deletion ratio on
smaller sets has modulus at least e^(-1/256), then |Q_(D minus N(gamma))/Q_(D minus p)| <= e^(41 |gamma|/256). With
(P), for |s| <= 2, |Q_D/Q_(D minus p) - 1| <= 1/512, and |log| < 1/256. This closes the induction, and
|log Q_T| <= 6v/256 on |s| <= 2. The coefficients of log Q_T have connected supports. Below the degree j_0 they do
not depend on the character and repeat once per lift, by (L). Cauchy's estimate bounds the rest at s = 1 by tau.
The mean of positive numbers within e^(+-tau) of a common value is within the same factor. QED

Remarks. (1) The classes (10) and (10*) are the cases where rho(gamma) is the sum of the coefficients of the
connected pairs with support gamma; their bound (12) gives (P). So Wilson at beta <= 1/46 is in the class (row
1354 3.2 item 2), and a confining theory can reach it. (2) Lemma D1 has no analogue here: an abstract
polymer model has no plaquette sign to flip. So Theorem N does not exclude a landing in the class of
Proposition EP. (3) The class is open under small changes of the activities in the norm of (P). (4) I did not
re-derive the constant of the Cauchy tail; it is that of row 1351 L136, checked in row 1352.

**4.5 What a thick step must use (on file; cited, not re-derived).** It must fail for compact U(1) at large
coupling and for Z_2 at large coupling (row 1353 Section 6; check 1355 corrects the scope: the centre-sign map
needs a central involution). It must integrate the angular variables of a block of the size of several
correlation lengths (row 1354 6.3: about 6^4 sites at beta = 2.3 for the constant 1/40). Sections 2 and 3 add:
no part of it can be done on centre variables alone.

**4.6 Remark (the failure is not special to weak coupling; ARGUED from the leading order of the strong-coupling
series, GUIDE for the numbers).** For a stack of B x B plaquettes the series gives
1 - Z'[1_{P_0}]/Z'[0] = 32 B (beta/4)^6 at leading order: the rim has 4B monopole cubes, each cube boundary has
the sheet weight 4 (beta/4)^6 (check 1357 L101), and the factor 2 comes from the Fourier inversion. For B = 1
this is the value that the run of Section 5 confirms at beta = 1.0 and 0.5. So a thin 't Hooft loop has a
perimeter law at small beta too, with the rate mu(beta) = 8 (beta/4)^6 for each unit of rim, and the bound of
Lemma D1 fails as soon as 32 B (beta/4)^6 exceeds 2/513. At beta = 1/46 this needs B above 4.7e9, so the remark has
no practical weight there. Its meaning is structural: under the map of row 1345 the class (10*) is not kept at
any coupling. The coarse centre always flows to the frozen form of Proposition TOP, and the free centre of (10*)
is the transient of small beta and small B. (A proof inside the hand range needs the convergent expansion for
the logarithm of the ratio; I did not write it.)

## 5. Guide run at a coupling of order one: the thin test at beta = 2.3 (criteria written 2026-11-21T07:35Z, date -u, before the run)

(The criteria of this section were written before Section 4, because they must precede the run.)

**5.1 What is tested (GUIDE only; a Monte Carlo is never a proof step).** Theorem N is proved for beta >= 59.
(BS*) of row 1354 is meant at a coupling of order one, with a block side of a few units. The same necessary
condition applies there: a model of (10*) that represents the theory with its packet signs needs
Z'[1_{P_0}]/Z'[0] >= 511/513 = 0.9961 (Lemma D1). The run estimates this ratio at beta = 2.3 for B = 1 (one
plaquette, R_1 = <exp(-2 beta q_p)>) and for B = 2 (a stack of 2 x 2 parallel plaquettes, R_2, as a product of
four successive one-plaquette ratios, each measured forward and backward).

**5.2 Criteria, fixed before the run.**

- Control C0: the script's self-test (quaternion product against 2 x 2 matrices; the staple against the change
  of the signed action) must agree to 1e-10.
- Control C1: the mean plaquette at beta = 2.3 on 6^4 must be 0.602 +- 0.004 (the published value is 0.6024).
- Control C2: for each of the four steps the forward ratio times the backward ratio must be 1 within 0.15.
- Result: the thin test "passes" at beta = 2.3 if R_1 >= 0.996, and "fails at guide level" if R_1 plus three
  standard errors is below 0.99. The same for R_2.
- What the run cannot show: a bound. It cannot replace Lemma T at order one.

**5.3 Results (run 2026-11-21T07:39Z, date -u; one job at a time under the numeric lock, plain numpy heat bath, script and log in a
scratch folder outside the repository; total run time about 3 minutes, peak memory 40 MB).**

| Quantity | Lattice, sweeps | Value |
|---|---|---|
| C0 self-test | | 6e-17 (product), 7e-14 (staple): passed |
| C1 mean plaquette, beta = 2.3 | 6^4, 300 + 1500 | 0.6040 +- 0.0006: passed |
| R_1 = <exp(-2 beta q_p)>, beta = 2.3 | 6^4, all plaquettes | 0.3382 +- 0.0023 |
| R_1, beta = 1.0 | 4^4, 300 + 3000 | 0.99288 +- 0.00055 |
| R_1, beta = 0.5 | 4^4, 300 + 3000 | 1.00016 +- 0.00024 |
| stack 2 x 2, beta = 2.3, forward ratios | 4^4, 500 + 8000 each | 0.313(19), 0.451(37), 0.422(28), 0.773(46) |
| the same, backward ratios (inverse steps) | | 3.23(13), 2.42(13), 1.99(9), 1.45(7) |
| C2 forward times backward | | 1.01, 1.09, 0.84, 1.12 |
| R_2, product of the forward ratios | | 0.046 |
| R_2, inverse product of the backward ratios | | 0.044 |

**5.4 Reading (GUIDE).**

- C2 failed at the third step by a small amount (0.84 against the preset window 1 +- 0.15; the statistical
  error of that product is about 0.07). Averages of exponentials are biased low on short runs. I report the
  failure and did not rerun. The two estimates of R_2 agree (0.046 and 0.044), and the conclusion below does
  not depend on a factor of two.
- At beta = 2.3 the thin test fails at guide level for B = 1 and for B = 2: R_1 = 0.338 and R_2 about 0.045,
  against the required 0.996. So also at a coupling of order one, where (BS*) was meant to be decided by a
  computation, the coarse model of row 1345 is not in (10*), for the block sides tested.
- The fourth step of the stack costs least (0.77): the stack of 2 x 2 has as many monopole cubes (8) as the
  stack of three. This is the perimeter effect of a thin 't Hooft loop.
- At beta = 1.0 the value 0.9929 is below 0.9961 by about six standard errors, and it agrees with the leading
  term 1 - 32 (beta/4)^6 = 0.9922 of the strong-coupling series (four cubes through the plaquette, each with the
  sheet weight 4 (beta/4)^6 of check 1357 L101). At beta = 0.5 the value is one within errors (series: 0.99988).
  So the true ratio crosses the bound of Lemma D1 near beta = 0.9 (GUIDE; by the series, 32 (beta/4)^6 = 2/513
  at beta = 0.89). This is far below the bulk crossover. In the pivot variables the class (10*) is a class of
  bare strong coupling and nothing else.

## 6. The first failing step (written 2026-11-21T07:48Z, date -u)

**6.1 The step (OPEN).** (BS-thick) of 4.1, or in the form that Proposition EP admits: for every late cutoff, a
polymer representation of the eight temporal twisted masses of Wilson on the two tori, at one physical coarse
mesh, with the bound (P), the lift rule (L) and K_2t = K_t^2. It gives the neutral and the periodic two-period
bounds together. It is at least as strong as (N-phys), which the gap clause needs.

**6.2 Four ways tried here, and where each stops.**

1. *The centre-sign map of row 1345 into (10*), with any representation of the environment.* Refuted for
   beta >= 59 (Theorem N), for beta >= 245 from checked statements alone (Remark N1), and at guide level at
   beta = 2.3 and 1.0 (Section 5). Stops at: the rim of a thin packet (Lemma T).
2. *The same map into any local-moment class on the centre weights.* At late cutoffs the centre sector is frozen
   with a free class (Proposition TOP). The format of row 1351 holds a frozen centre only with a fixed class
   (Lemma FR, exact case; Proposition B of row 1354 for the class (10)), or with an environment far from a
   product law (3.4 (c)). Stops at: the environment, which is the whole problem.
3. *A thick map.* A centre-covariant kernel to coarse SU(2) links reproduces the thin bundle flip (4.3 item 1).
   It gives twisted coarse densities and no sheet weights, and the coarse weight is not a product of plaquette
   functions. A polymer end class accepts non-local terms (Proposition EP), and then the landing is a block
   statement in the law of the model at a coupling of order one. Stops at: the same statement as rows 1340, 1353,
   1354 and 1356.
4. *A coarse centre variable without a rim* (4.3 item 4). It exists after the action is deleted in a collar
   of the dual one-skeleton, which changes the theory, or for closed surfaces only, which are the classes.

**6.3 What would reopen the dual route.** (a) An exact map whose coarse centre variable costs no rim: none is on
file, and 4.3 item 1 shows that a centre-covariant kernel alone does not give one. (b) A proof that the polymer
activities of a blocked Wilson theory obey (P) at one coupling above the strong-coupling range. This is a
finite-coupling block statement; it must fail for compact U(1) at large coupling (row 1353).

## 7. Summary

**Solved?** No. The block step is not built. (N-phys) and the mass gap are not proved. No statement of the
chain is disproved. One proposed route is closed with proofs.

**PROVED here (by hand; checked by no one).**

- Lemma A: A(beta) >= (4/(3 pi)) (3/(2 beta))^(3/2) e^(-3/2) (2 - 3/(2 beta))^(1/2) e^beta for beta >= 3/2.
- Lemma T (given the signed deletion bound (7) of row 1345): a sign pattern with one monopole cube has
  Z[tau] <= 3 (e^(sqrt 3 beta/2)/A(beta))^4 Z[0], which is at most 0.658 Z[0] for beta >= 59.
- Lemma D1 (given the deletion induction of row 1351 and Theorem E): in a model of (10*) a change of sign of
  one plaquette's odd part changes the periodic mass by a factor between 511/513 and 513/511.
- Theorem N: for beta >= 59 and every block side, no model of (10*) represents the Wilson theory with its
  packet signs. So no re-expression of the coarse model of row 1345 in other environment variables lies in
  (10*). Remark N1: the same for beta >= 245 from statements that rows 1347, 1352 and 1357 checked.
- Proposition TOP and Corollary TOP1 (given (8) of row 1345): for 6 sqrt(u_beta) < 1 the weight of a coarse
  electric sheet of row 1345 is 2^(r - 6v) 64 X_c up to 2^(r - 6v) eps_B Z[0], with c the homology class of the
  sheet. Every bounding sheet weighs as much as the empty one, up to (1 +- eps_B)/(1 -+ eps_B).
- Lemma FR: on independent link variables a plaquette-local rule with values in F_2 that is closed almost
  surely is a constant closed cochain plus a coboundary of link functions. Its class is constant.
- 4.3 item 1: for a centre-covariant kernel the coarse sign flip is the thin bundle flip of the fine theory.
- Proposition EP (given row 1351 L134-136): the end theorem of rows 1351 and 1354 for abstract polymers with the
  hypotheses (P) and (L).

**ARGUED here.** 3.4 (c): a frozen centre with a free class needs an environment far from a product law (no
quantitative form of Lemma FR was written). 4.2: a landing in a dual class needs a thick centre variable. 4.6:
the class (10*) is not kept by the map of row 1345 at any coupling.

**GUIDE.** Section 5: at beta = 2.3 the one-plaquette ratio is 0.338 +- 0.002 and the ratio for a 2 x 2 stack is
about 0.045, against the 0.996 that (10*) needs; at beta = 1.0 the ratio is 0.9929 +- 0.0006. One preset control
(C2) failed by a small amount at one step and is reported in 5.4.

**OPEN.** (BS-thick) in any form; a quantitative Lemma FR; Lemma T at a coupling of order one; (N-phys); the
mass gap.

**Not done.** Row 1358 and its file were not read. `parts/gap.md` (130 KB) was not read; I worked from the RESULT
lines of rows 1332 to 1357 and from the files of rows 1345, 1351, 1354 and checks 1347, 1357. PRs #10133, #10134, #10141, #10144 were not searched. I read
no published paper in this row; Mack and Petkova, 't Hooft and Tomboulis and Yaffe are cited through the rows
that read them. I did not re-derive the constants of row 1351's cluster bound (12) or of its Cauchy tail. The
proofs of Section 2 to 4 are unchecked.

**For the lead (proposals; no other file was edited).**

1. Do not queue (BS*) for the map of row 1345. Theorem N and Proposition TOP close it in both end classes.
2. A check of this row needs: Lemma T (four steps, with row 1345 L73 and L81), Lemma D1 (one paragraph, with row
   1351 L134), Proposition TOP (the count of row 1345 (9)), Lemma FR (elementary), Proposition EP.
3. Lemma T also improves the range of (8) and (9) of row 1345: with the geodesic distance and four faces for
   each cube the factor for one disjoint-face cube is 3 e^(sqrt 3 beta/2)/A(beta), which is below one for
   beta >= 66 (hand constant of Lemma A; 54.8 with the exact A), where the on-file form needs 6 sqrt(u_beta) < 1,
   that is beta >= 213.5 with the exact A. (ARGUED: among h cubes at least
   h/4 choose the same coordinate direction for their four faces. Not written out, not needed on the tail.)
4. If a dual end class is kept as a target, use the polymer form of Proposition EP, which a thick map could
   meet, and state the block step as a statement in the law of the model.

