lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T05:17Z

# Check of row 1004 (work items W1 and W2 of `library/gap-outside-box-max.md` 8.7)

Row 1008, `gap-outside-box-check-opus`. Started 2026-11-15 17:17Z on Mac mini worker 2.
Checker: Claude Opus 5.5, max effort. The checked file was written by Claude Fable 5.2 (row 1004),
same provider, so this is a same-provider check, not an independent one.
Source pinned at commit 6d2c02ef7 on branch `claude/ym4d-hard-route`.

## Plan (at most eight steps; one step per response, result appended before the next)

1. Brief: FINISH rules, rows 1004 and 1008, `gap-outside-box-max.md` 8.7. DONE (below).
2. (i-b) Lemma LYP2 (Section 6.1b).
3. (i) Lemma LYP (Section 6.1), and the reading of `gap-skeleton-max.md` L177-178.
4. (ii) Lemma GG (Section 6.2), with Lemma A as the corollary uses it.
5. (iii) Lemma TW (Section 6.3) against Theorem S and `gap-constraints-max.md` row 1 and Section 7 (Theorem 2O).
6. (iv) Proposition CB (Section 3.0): the semicontinuity argument.
7. (v) Theorem TW-T (`gap-transfer-twisted.md` Section 5, five points), with `gap-transfer.md` Sections 1-4 and 9.3 open.
8. W2 (three lines), verdict table, RESULT line.

## Step log

### Step 1. The brief (2026-11-15 17:20Z)

Row 1008 says: do work items W1 and W2 of `gap-outside-box-max.md` 8.7 exactly as written; no new attack.
This is a check row, so the no-duplicate-attack grep does not apply; no open lemma is attacked here.

W1, as written in 8.7 (L399-406), quoted in short:
- Read `gap-outside-box-max.md` Sections 3.0, 6.1, 6.1b, 6.2, 6.3 and `gap-transfer-twisted.md` in full,
  with `gap-transfer.md` Sections 1 to 4 and 9.3 open.
- Verdict per statement: HOLDS, HOLDS AFTER CORRECTION, FAILS.
- (i-b) Lemma LYP2: step (2) (link count; link-disjoint tuples give a^(|E|-4n) b^(4n)); step (3) (three error
  terms, uniform on a disc); signs a_1^4 > 0 and b_0^4 > 0 per group; use of Hurwitz's theorem.
- (i) Lemma LYP: the three formulas (Z_2 sum by hand; SU(2) a_j(x) = 2(2j+1) I_(2j+1)(x)/x; the Schur step);
  part (b) (fourth power on the imaginary axis; J_1 and J_2 have no common zero); part (c) (bound
  e^(beta + 4|Re kappa|), Borel-Caratheodory, evenness). Is "the crux (LY) of B9 is false for one plaquette"
  a fair reading of `gap-skeleton-max.md` L177-178?
- (ii) Lemma GG: step 1 (unitary gauge for a gauge-invariant integrand), step 2 (limit measure is Haar on the
  stabilizer), the corollary's use of Lemma A. Is the reading that a twist is no longer free for kappa > 0 right?
- (iii) Lemma TW: is "the engine needs a pair of clean directions" a correct reading of Theorem S and of
  `gap-constraints-max.md` row 1 and Section 7 (Theorem 2O)?
- (iv) Proposition CB: the semicontinuity argument.
- (v) Theorem TW-T: the five points of its Section 5.
- Stop rule: at the first statement that FAILS, give the failing step and go on to the next statement; do not repair.

W2, as written (L408): decide by hand the power of beta in the twist ratio of the symmetric torus at weak
coupling at fixed size, -log(Z^k/Z^0) = (3/2) log beta + O(log log beta) (row 1004, Section 3.0) against
"about 3 log beta" (row 859 idea 8, `gap-brainstorm-max.md` L284); read `gap-phys-seed.md` for the count
behind "765 log(1/g)". Output: three lines here. It bears on no proof.

Verdict scale used below: HOLDS, HOLDS AFTER CORRECTION (a local fix, stated, that does not change the
statement), FAILS (a step is wrong and the statement as written does not follow). Minor slips that change
nothing are listed as notes.

### Step 2. (i-b) Lemma LYP2 (`gap-outside-box-max.md` L268-288) (2026-11-15 17:35Z)

**Verdict: HOLDS.** Every step was redone by hand. No step fails. Notes 1-4 below change nothing in the lemma.

Checks, in the order of the brief.

- Single-link functions (L272). Recomputed: Z_2, a = cosh kappa, and the integral of sigma e^(kappa sigma) is
  sinh kappa, so b = sinh kappa. U(1): a = I_0; the integral of e^(+-i theta) e^(kappa cos theta) is
  I_(+-1) = I_1, so each of the two exponentials in cos(theta_1 + theta_2 - theta_3 - theta_4) gives I_1^4
  and b^4 = I_1^4. SU(2): with chi = (1/2) tr = (1/2) chi_(1/2) and Schur, the integral is
  (1/2) d (a_(1/2)/d)^4 with d = 2 and a_(1/2)(kappa) = 4 I_2(kappa)/kappa, so b^4 = (2 I_2(kappa)/kappa)^4,
  and a = a_0 = 2 I_1(kappa)/kappa. All three agree with L272.
  The value b^4 does not depend on which links of a plaquette carry an inverse: for U(1) I_(-1) = I_1; for
  SU(2) the link weight is invariant under U -> U^(-1), so Schur gives the same multiple of the identity.
  So the lattice setting of L270 ("four distinct link variables or their inverses", any pattern) is covered.
- Evenness, step (1). U_l -> -U_l is a measure-preserving map (central element; theta -> theta + pi);
  chi(U_l) changes sign; U_p picks up (-1)^4 = 1. Correct for all three groups.
- Step (2), the count. Expanding exp(beta sum_p chi(U_p)) as a power series and integrating term by term is
  allowed (bounded integrand on a compact space). An n-tuple may repeat plaquettes; L is the union of their
  link sets. Each plaquette has four distinct links, so |L| <= 4n, with equality if and only if the four-sets
  are pairwise disjoint, which excludes repeats. Such tuples number n! N_n. For them the integral factorizes:
  links outside L give a^(|E| - 4n), each plaquette gives b^4 (above). For any tuple the factor on L is
  bounded by exp(|L| |Re kappa|), because chi is real with |chi| <= 1 for all three groups. The bound
  |c_n| <= |P|^n exp(|E| |Re kappa|) is right. Step (2) HOLDS.
- Step (3), the three error terms, on |tau| <= R, kappa = kappa_0 + beta^(1/4) tau, beta <= 1.
  (e1) Link-disjoint tuples, n <= |E|/4: a = beta^(1/4) (a_1 tau + O(beta^(1/4))), b = b_0 + O(beta^(1/4)),
  by Taylor's formula for the entire functions a, b at kappa_0, uniform on the disc; the product is
  beta^(|E|/4) [N_n (a_1 tau)^(|E| - 4n) b_0^(4n) + O(beta^(1/4))]. Correct.
  (e2) Other tuples, n <= |E|/4: |L| <= 4n - 1, so the power of a is at least |E| - 4n + 1 >= 1, and
  |a| <= C beta^(1/4) on the disc; with at most |P|^n tuples and beta^n/n!, the total is
  O(beta^(|E|/4 + 1/4)). Correct.
  (e3) Tail n > |E|/4: 4n and |E| are integers, so 4n >= |E| + 1 and beta^n <= beta^(|E|/4 + 1/4) for
  beta <= 1; the sum of |P|^n e^(|E| |Re kappa|)/n! is at most e^(|P|) e^(|E| R) for beta <= 1. Correct.
  Also N_n = 0 for n > alpha and 4 alpha <= |E| (alpha disjoint four-sets in E). So F_beta -> G uniformly on
  |tau| <= R. Step (3) HOLDS.
- Signs. kappa_0 is pi/2 i (Z_2), j_(0,1) i (U(1)), j_(1,1) i (SU(2)); L272 lists the three in that order.
  Z_2: a_1 = sinh(i pi/2) = i = b_0, fourth powers 1. U(1): a' = I_1, so a_1 = b_0 = I_1(i y_0) = i J_1(y_0),
  fourth power J_1(y_0)^4 > 0; J_1(y_0) != 0 since J_0' = -J_1 and J_0, J_0' have no common zero at y != 0
  (Bessel equation regular there). SU(2): a(i y) = 2 J_1(y)/y, so i a'(i y) = d/dy a(i y) and
  a_1 = -2 i J_1'(y_0)/y_0 (the J_1(y_0)/y_0^2 term vanishes); b_0 = 2 I_2(i y_0)/(i y_0) = 2 i J_2(y_0)/y_0.
  From J_1' = J_1/y - J_2, J_2(y_0) = -J_1'(y_0) != 0. So a_1^4 = b_0^4 = 16 J_2(y_0)^4/y_0^4 > 0.
  The facts used (I_n(i y) = i^n J_n(y), the recurrences) are standard and correct as stated at L234.
  Signs HOLD.
- Step (4). H has leading coefficient N_0 = 1, constant term N_alpha b_0^(4 alpha) > 0, all coefficients
  N_n b_0^(4n) > 0 (any subset of a disjoint family is disjoint, so N_n > 0 for n <= alpha), degree
  alpha >= 1 (one plaquette is a disjoint family). So H has a root, and none in [0, infinity). With
  a_1^4 > 0, a non-zero root tau of G has tau^4 = w/a_1^4 outside [0, infinity), so it is on neither axis.
  Correct.
- Hurwitz, step (5). G is a non-zero polynomial; D is a closed disc around tau_* with no other root and inside
  {Re tau != 0}, so G has no zero on the boundary circle. Uniform convergence on D and Rouche
  (|F_beta - G| < min over the circle of |G| for small beta) give a zero of F_beta in D for every small beta.
  Hurwitz's theorem is stated for sequences; the conclusion "for every beta in (0, beta_0)" follows from the
  Rouche form, or from Hurwitz by contradiction along a sequence. Re kappa = beta^(1/4) Re tau != 0 because
  kappa_0 is imaginary. Evenness gives a zero with Re kappa > 0. Correct.
- Cross-check, one plaquette, SU(2): from L258, Z = a(kappa)^4 + beta b(kappa)^4 + O(beta^2) (the n = 2 weight
  is 8 I_2(beta)/beta = beta + O(beta^3)), so beta^(-1) Z -> (a_1 tau)^4 + b_0^4, which is G for |E| = 4,
  alpha = 1. Agrees with L276 and with the Remark at L288.

Notes (none breaks the lemma).
1. L272 "y_0 = pi/2, the first zero of J_0, the first positive zero of J_1" lists one value per group, in the
   order Z_2, U(1), SU(2); the text does not say so. A reader can recover it from a(i y).
2. "b(kappa) defined by ... is b(kappa)^4" defines only b^4; only b^4 and b_0^4 are used, and the explicit b
   are entire. No gap.
3. L280 "At b = 0 it holds" rests on the classical fact that J_0 and J_1(z)/z have only real zeros (zeros of
   J_nu are real for nu > -1). It is recalled, not proved, and it is outside the lemma's statement.
4. Remark L288 "a hard-core gas ... with a negative activity": H(w) = w^alpha I(b_0^4/w), with I the
   independence polynomial, is right. The zeros found sit at activities x = b_0^4/(a_1 tau)^4 that are roots
   of I; the lemma proves only x not in [0, infinity), not x < 0. "Negative" is loose; it is in a remark.

### Step 3. (i) Lemma LYP (`gap-outside-box-max.md` L236-266) and the reading of B9 (2026-11-15 17:50Z)

**Verdict: Lemma LYP HOLDS. The sentence "the crux (LY) of B9 is false for one plaquette" (L249) HOLDS AFTER
CORRECTION: its quantifier must be fixed (below). The correction does not touch the lemma.**

The three formulas, redone by hand.
- Z_2. Grouping the 16 sign configurations by the number m of minus signs: m = 0, 4 give
  e^beta e^(+-4 kappa); m = 2 gives 6 e^beta; m = 1, 3 give 4 e^(-beta) e^(+-2 kappa). With x = cosh 2 kappa,
  e^(4 kappa) + 6 + e^(-4 kappa) = 4x^2 + 4 and 4 e^(2 kappa) + 4 e^(-2 kappa) = 8x, so
  Z = (1/16)[e^beta (4x^2 + 4) + 8x e^(-beta)] = (e^beta/4)[x^2 + 2 e^(-2 beta) x + 1]. Second route:
  e^(beta s) = cosh beta + s sinh beta gives Z = cosh beta cosh^4 kappa + sinh beta sinh^4 kappa
  = (1/4)[cosh beta (x+1)^2 + sinh beta (x-1)^2], the same. L254 is right.
- U(1). Generating function exp(beta cos phi) = sum_n I_n(beta) e^(i n phi); the link integral of
  e^(+-i n theta) e^(kappa cos theta) is I_n(kappa) (the sine part is odd); I_(-n) = I_n. So
  Z = sum_n I_n(beta) I_n(kappa)^2 I_(-n)(kappa)^2 = sum_n I_n(beta) I_n(kappa)^4. L256 is right.
- SU(2). With the class measure (2/pi) sin^2 theta d theta and sin A sin B = (cos(A-B) - cos(A+B))/2,
  a_j(x) = (1/pi) integral over [0, pi] of e^(x cos theta)[cos 2j theta - cos (2j+2) theta] = I_(2j) - I_(2j+2),
  and I_(n-1) - I_(n+1) = (2n/x) I_n with n = 2j+1 gives 2(2j+1) I_(2j+1)(x)/x. Schur: M = integral of
  f(U) D^j(U) dU commutes with every D^j(V) when f is a class function, so M = (tr M/d_j) Id = (a_j/d_j) Id;
  f(U^(-1)) = f(U) (tr U is real on SU(2)) gives the same M for the inverse links. The plaquette term is
  tr M^4 = d_j (a_j/d_j)^4, and a_j(beta) d_j = 2 n^2 I_n(beta)/beta, a_j(kappa)/d_j = 2 I_n(kappa)/kappa.
  L257-258 are right. The character series of the plaquette weight converges absolutely
  (a_j(beta) > 0 and sum_j d_j a_j(beta) = e^beta), so term-by-term integration is allowed.

Part (a). Evenness: I_n(-kappa) = (-1)^n I_n(kappa), and the fourth power removes the sign (for SU(2) also
for I_n(kappa)/kappa). Bounds: |I_n(kappa)| <= e^(|Re kappa|) from the integral; |a_j(kappa)| <= d_j e^(|Re kappa|)
from |chi_j| <= d_j. With sum_n I_n(beta) = e^beta and sum_j d_j a_j(beta) = e^beta (value at U = 1), the
Weierstrass test gives an entire function with |Z| <= e^(beta + 4 |Re kappa|). For Z_2 each of the 16 terms is
at most e^(beta + 4|Re kappa|). (a) HOLDS.

Part (b). Z_2: x = cos 2y in [-1, 1]; the quadratic has its minimum 1 - e^(-4 beta) > 0 at
x = -e^(-2 beta). U(1): I_n(i y)^4 = i^(4n) J_n(y)^4 >= 0; keeping n = 0 and n = +-1 (J_(-1)^4 = J_1^4) gives
the lower bound I_0(beta) J_0^4 + 2 I_1(beta) J_1^4, positive because J_0 and J_1 = -J_0' have no common zero
(ODE uniqueness at y != 0, J_0(0) = 1). SU(2): (2 I_n(i y)/(i y))^4 = 16 J_n(y)^4/y^4; the n = 1, 2 terms give
(32/(beta y^4))(I_1(beta) J_1^4 + 4 I_2(beta) J_2^4) (coefficients 2 x 16 and 8 x 16 = 4 x 32, right).
J_1 = J_2 = 0 at y != 0 would give J_1'(y) = J_1/y - J_2 = 0 and J_1 = 0 identically. At y = 0 the limit is
2 I_1(beta)/beta > 0. (b) HOLDS for all three groups.

Part (c). Z_2: the roots in x are -e^(-2 beta) +- i (1 - e^(-4 beta))^(1/2), not real; cosh maps C onto C,
so zeros kappa exist (the text does not say this; it is one line); Im cosh(2a + 2ib) = sinh 2a sin 2b forces
a != 0. U(1), SU(2): if Z had no zero, h = log Z would be entire with Re h <= beta + 4|kappa| by (a);
Borel-Caratheodory on |kappa| = r < R = 2r gives |h| = O(r), and the Cauchy estimates give h linear.
Evenness gives e^(2 a kappa) = 1 for all kappa, so a = 0 and Z is constant. For real kappa every term is
>= 0, and the n = 0 term (U(1)) or n = 1 term (SU(2)) tends to infinity. Contradiction; so a zero kappa_0
exists, Re kappa_0 != 0 by (b), and -kappa_0 is a zero by evenness. (c) HOLDS.

Remark (1) of 6.1 (ARGUED) agrees with LYP2: for one plaquette the limit is (a_1 tau)^4 + b_0^4 (step 2 above).

The reading of B9 (`gap-skeleton-max.md` L177-178, with L23 and L100).
- The weight is the same. L23 defines a_p(U) = 1 - (1/2) Re tr U_p and L100 A(U) = sum_p a_p(U); so
  exp(-b A(U) + kappa sum_l (1/2) tr U_l) = e^(-b |P|) times the LYP weight with beta = b. The factor does not
  move zeros. "The first component of the unit 4-vector" is (1/2) tr U = s_0. So the SU(2) case of LYP is the
  B9 weight on one plaquette, as L242 says.
- The quantifier is not the same. L100 opens Section 1.B, before B1, and fixes the notation of every approach
  B1-B13: "Lambda is a finite periodic lattice in d = 4". (LY) at L178 quantifies over these Lambda.
  One plaquette with four free links is not a finite periodic lattice in d = 4. So Lemma LYP alone is a failure
  of the half-plane property on a system that (LY) does not quantify over. It is not a counterexample to (LY)
  as written. (B9's own check "On one link it is true" is also a degenerate system; it shows the author used
  small systems as tests, but it does not widen the quantifier.)
- Lemma LYP2 closes the difference, at small b only. Its setting includes "a periodic torus with sides at least 3"
  (L270), which in d = 4 is an admissible Lambda. So (LY) as written at L178 is false: for every finite periodic
  lattice in d = 4 with sides at least 3 and every b in (0, beta_0(Lambda)). (LY) needs only one Lambda and one
  b to fail, so this refutes it.
- Correction of L249 (and of the RESULT line's gloss): "(LY) fails on the one-plaquette system at every b > 0
  (Lemma LYP); (LY) as written, over finite periodic lattices in d = 4, is false by Lemma LYP2, for every such
  lattice with sides at least 3 at all small b > 0. Whether it fails at every b > 0 on such a lattice is not
  shown." The line L280 of 6.1b, "the crux (LY) of B9 fails on every lattice Lambda for all small b > 0", is
  already correct as written, with "for all small b" depending on Lambda.
- Remark (2) is right that neither lemma touches a zero-free neighbourhood of the positive real kappa axis:
  the zeros found sit near kappa_0 = i y_0, at distance of order beta^(1/4) from the imaginary axis.

Notes (none breaks the lemma).
1. Remark (3) cites `gap-skeleton-max-b.md` L581 for "2 I_1(beta)/beta has imaginary zeros only"; this rests on
   the classical reality of the zeros of J_1(z)/z, recalled and not proved; outside the lemma.
2. In (c) for Z_2 the existence of a zero is implicit (cosh is onto C); stated above.

### Step 4. (ii) Lemma GG and Corollary GG1 (`gap-outside-box-max.md` L290-310) (2026-11-15 18:05Z)

**Verdict: HOLDS (Lemma GG; Corollary GG1 as an implication from its stated hypothesis). The reading that a
twist is no longer free for kappa > 0 is right, classically.** Three notes, none breaking a step.

Gauge invariance of the weight. <Ad(g_x) phi_x, Ad(g_x U g_y^(-1)) Ad(g_y) phi_y> = <phi_x, Ad(U) phi_y>,
since Ad is orthogonal; U_p goes to g_x U_p g_x^(-1) and w is a class function. Right.

Step 1 (unitary gauge). A measurable s with Ad(s(phi)) phi = e_3 exists (a measurable section of the Hopf map
U -> Ad(U)^(-1) e_3). For fixed phi, g_x = s(phi_x) and gauge invariance give
(F W)(U, phi) = (F W)(g.U, e_3). For fixed g, U -> g.U multiplies each link on both sides by fixed elements,
so it preserves the product Haar measure. The U-integral at fixed phi therefore equals the integral of
F(U, e_3) W(U, e_3) dU. The invariance is used phi by phi, so no joint measurability of the transformed map
is needed; Fubini applies to the continuous integrand. The normalized phi-integral is 1. Step 1 HOLDS.

Step 2 (one link). Ad: SU(2) -> SO(3) is onto and pushes Haar to Haar, so Ad(U) e_3 is uniform on S^2 and
t = <e_3, Ad(U) e_3> is uniform on [-1, 1] (Archimedes). Then the integral of e^(kappa (t - 1)) is
(1/2)(1 - e^(-2 kappa))/kappa = c_kappa, and nu_kappa(t <= 1 - delta) = (e^(-kappa delta) - e^(-2 kappa))/(1 - e^(-2 kappa)).
Both recomputed; both right. {t = 1} = {U : Ad(U) e_3 = e_3} = H. t(hU) = t(Uh) = t(U) for h in H, and Haar
measure is bi-invariant, so nu_kappa is H-bi-invariant. A weak limit nu along a subsequence gives
nu(t < 1 - delta) <= liminf nu_kappa(t < 1 - delta) = 0 (open set, portmanteau), so nu is carried by H; it
is H-invariant because translation is continuous; an H-invariant probability on H is Haar_H. All subsequential
limits agree, so nu_kappa -> Haar_H. Step 2 HOLDS.

Step 3. After step 1, <F>_kappa is a quotient of integrals against the product of the nu_kappa (the factors
c_kappa^|E| cancel); finite products of weakly convergent probability measures on compact metric spaces
converge weakly; the integrands are continuous; the denominator tends to Z_(U(1), w) > 0 because w > 0.
On H, U_p = u(theta_p) with theta_p the oriented sum (H abelian), and Haar_H is d theta/2 pi. Also
Z_kappa = c_kappa^|E| times the denominator, so c_kappa^(-|E|) Z_kappa -> Z_(U(1), w). For the Wilson weight,
(1/2) tr u(theta) = cos theta, so the end point is Wilson U(1) at the same beta. Step 3 HOLDS.

Corollary GG1, the use of Lemma A. Lemma A is `gap-crux-restate.md` L37 (6.2 does not name the file):
for S >= 0 trace class, (Tr S^k)^(1/k) decreases to lambda_0, and lambda_0^k >= Tr S^(2k)/Tr S^k for S != 0.
- The normalization is consistent: on B x Z/j the number of links is j e_B (e_B links per time slice), so
  Z~(j) = Tr(T~^j) with T~ = c_kappa^(-e_B) T, a positive trace-class operator if T is one. So the sandwich
  (Z~(2j)/Z~(j))^(1/j) <= lambda~_0 <= Z~(j)^(1/j) is Lemma A (b) and (a) for T~. Right.
- Order of limits. For fixed j, Lemma GG on the finite tori B x Z/j and B x Z/2j gives Z~_kappa(j) -> Z_U(1)(j)
  and Z~_kappa(2j) -> Z_U(1)(2j). So limsup over kappa of lambda~_0,kappa <= Z_U(1)(j)^(1/j) and liminf >=
  (Z_U(1)(2j)/Z_U(1)(j))^(1/j), for every j. As j -> infinity both bounds tend to lambda_0 of the U(1) model
  (for the lower bound: the bracket (m + sum r_i^(2j))/(m + sum r_i^j) lies in [m/(m + Tr T/lambda_0), 1] for
  j >= 1, so its j-th root tends to 1). Then S_kappa(k) = Z~_kappa(k)/lambda~_0,kappa^k - 1 converges.
  The argument is right.
- Note 1 (hypothesis). The j -> infinity step needs (TM) also for the U(1) end model with weight w, and the
  finite-kappa step needs it for SU(2) with weight w plus the site field. The (TM) on file
  (`gap-transfer.md` N.1, N.4; `gap-crux-restate.md` L33) is for SU(2) with the Wilson weight only. The label
  "PROVED given (TM) for the family" covers this if "the family" includes its end point and the weight w;
  the label names only the site-field extension as ARGUED. The change of group (U(1)) and of weight
  (w of positive type) is the same proof, but it is also not written. Not a failure; a label to widen.
- The thermal sum: `gap-crux-restate.md` defines S(k; B) = sum over i >= 1 of r_i^k, which equals
  Z(k)/lambda_0^k - 1 when lambda_0 is simple, as (TM) asserts. Consistent with GG1.

The reading "a twist is no longer free for kappa > 0" (L310). Right, and the reason can be made complete.
A zero-action twisted configuration needs (twisted) flat plaquettes and a covariantly constant site field.
Flatness with a twist in the (1,2) plane gives holonomies with Omega_1 Omega_2 Omega_1^(-1) Omega_2^(-1) = -1;
a covariantly constant phi gives Ad(Omega_1) phi_0 = Ad(Omega_2) phi_0 = phi_0, so both lie in the stabilizer
of phi_0, a U(1), and commute: contradiction. So the minimum of the action is positive for kappa > 0 (and is
attained, by compactness). The text argues with the twist eaters i sigma_1, i sigma_2 (rotations by pi about
two orthogonal axes, no common fixed unit vector); since flat twisted pairs are conjugate to these up to the
centre, its reason is complete for the flat case, and the conclusion "a defect of the site field or an
abelian flux" is right. At kappa = infinity, -u(theta) = u(theta + pi), so the twisted stack carries an extra
angle pi, half a U(1) flux quantum, with classical cost of order beta at fixed size. Right.
"An adjoint field does not see the centre" is right: Ad(-U) = Ad(U), so flips and twisted partition functions
exist for every kappa.

Note 2 (slip in the Reading, no consequence). For the SU(2) class function equal to the Villain function on H,
with Fourier coefficients v_k on H, the character coefficients are w_j = (1/pi) integral over [0, pi] of
w(theta)[cos 2j theta - cos (2j+2) theta] d theta = v_(2j) - v_(2j+2), not (1/2)(v_(2j) - v_(2j+2)) (L310).
Test: w = 1 gives w_0 = 1 = v_0. The sign, and so "of positive type", is unaffected (v_k decreases in k >= 0).

Note 3 (outside the brief, recorded only). The Reading's "for every N_max there is kappa_0 with no seed of size
up to N_max" needs the U(1) no-seed statement to be strict at each of the finitely many sizes (an open
condition), as in Proposition CB; that is step 6 below.

### Step 5. (iii) Lemma TW (`gap-outside-box-max.md` L312-324) (2026-11-15 18:20Z)

**Verdict: HOLDS.** "The engine needs a pair of clean directions" is a correct reading of Theorem S, of row 1 of
`gap-constraints-max.md` and of its Theorem 2O, for the partition function Z^k of one twist class. Two scope
notes below; neither is a failing step.

What the three sources require (read at this pin).
- Theorem S (`gap-crux-restate.md` 3.4, L170-200). The setting of Lemmas K, X, E (L174) is: W(a, b) = W(b, a),
  and for each b a positive trace-class T_b with W(a, b) = Tr T_b^a. With the symmetry this is a positive trace
  in both channels: W(a, b) = Tr T_a^b is what Lemma K (b) and Lemma E use (Tr T_a^(2b) <= (Tr T_a^b)^2), and
  Lemma K (c) uses that b -> log Tr T_a^b is a log-sum of exponentials with positive weights. The proof of
  Theorem S (L202) applies Lemma E to the pairs (1,2), (1,3), (1,4), so the cube form needs all four
  directions in such pairs; a two-direction form (Corollary S2, L205, with the other sides as spectators) needs
  one pair.
- Row 1 of the audit (L94): "The engine needs a trace in both channels of an exchanged pair (1.1) ... Spectator
  directions need (TM) only". Same requirement; a twist in the spectator plane is allowed, because the transfer
  operator of a box with a twisted spatial weight is positive by (TM-tw).
- Theorem 2O (L317-409). Setting (2O): positive trace-class T_b and T'_a with W(a, b) = Tr T_b^a = Tr (T'_a)^b,
  and no symmetry. So 2O removes the exchange symmetry, not the positive trace in each channel. Lemmas K2 (b),
  E2o and D use Lemma A (a) in both channels.

Lemma TW against these.
- (a) is (TM-tw) of `gap-flux-exercise.md` L115 read in one direction: the planes through mu enter as the
  insertion C = C^e, the others as the twisted spatial weight of T_(B,m). The top eigenvector of T_(B,m) is
  strictly positive (strictly positive kernel, by (TM-tw)), and C maps positive functions to positive functions
  and commutes with T, so the top eigenvector is C-even; hence Tr(T^j C) = lambda_0^j (1 + S_even(j) - S_odd(j)).
  Right.
- (b) Right in its operator form: Tr((T^(n_mu) C)^j) = Tr(T^(j n_mu) C^j), and C^2 = 1. The sentence "multiplying
  the side n_mu by j multiplies every k_(mu nu) by j modulo 2" means the j-fold cover of the twisted torus, which
  is the object the engine's step Tr S^(jb) <= (Tr S^b)^j produces; a torus of side j n_mu can of course carry
  class k itself, but then no such inequality is available. With that reading, "a doubling leaves the family"
  is right.
- (c) If mu and nu are clean, every entry with index mu or nu is zero; only the complementary entry is free.
  So the classes with a clean pair are k = 0 and the six single-plane twists. Exchanging the two clean axes
  fixes the complementary entry, so Z^k is symmetric in the pair and Theorem S's two-direction form applies,
  with the twisted plane as spectators. Right.
- (d) S_4 acts transitively on the six planes, so an invariant class is 0 or all ones, and all ones leaves no
  clean direction. Right.

Scope note 1 (single class). The lane runs the engine in every direction on sector sums
W_w = sum over k of w(k) Z^k (`gap-flux-exercise.md` 8.4, Lemma W (b): T_B^w = direct sum of T_(B,m) P_(Sigma,m),
positive because P_(Sigma,m) is a projection commuting with T). These sum over the twists through mu with
characters, so the sign is removed. Lemma TW is stated for one class Z^k and does not contradict this. The
RESULT gloss "the engine runs only in directions outside every twisted plane" is right for one class and should
say so.

Scope note 2 ("only if"). (c)'s first sentence, "an exchanged pair with positive traces in both channels is a pair
of clean directions", is shown for the traces that (TM-tw) supplies. A signed trace sum_i c_i lambda_i^n can equal a
positive trace sum_j mu_j^n for all n only if, at every value lambda, the C-even multiplicity is at least the
C-odd one (uniqueness of exponential sums); (a) does not exclude this coincidence, and nothing in the lane supplies
it. The label "PROVED given (TM-tw) and the reading" covers this; it is not a gap in what TW is used for.

### Step 6. (iv) Proposition CB (`gap-outside-box-max.md` L122-125) (2026-11-15 18:30Z)

**Verdict: HOLDS.** The semicontinuity argument (the step-8 version at L123) is right as written.

The argument, redone. Fix the box B = (2N)^3 and the direction of the time k. The hypothesis "models of the
engine's class" gives, for each t, a positive trace-class T_t != 0 with Z_t(k) = Tr T_t^k; the hypothesis of
the proposition gives t -> Z_t(k) continuous for every k (every torus k x B).
- Upper semicontinuity. By Lemma A (a) the sequence Z_t(k)^(1/k) is non-increasing with limit lambda_0,t, so
  lambda_0,t = inf over k of Z_t(k)^(1/k). An infimum of continuous functions is upper semicontinuous. Right.
- Lower semicontinuity. Z_t(k) >= lambda_0,t^k > 0, so q_k(t) = (Z_t(2k)/Z_t(k))^(1/k) is continuous. By
  Lemma A (b), q_k(t) <= lambda_0,t. And q_k(t) -> lambda_0,t: with m the multiplicity of lambda_0 and
  r_i < 1 the other ratios, q_k = lambda_0 [(m + sum r_i^(2k))/(m + sum r_i^k)]^(1/k), and the bracket lies in
  [m/(m + Tr T/lambda_0), 1] for k >= 1, so its k-th root tends to 1. Hence lambda_0,t = sup over k of q_k(t),
  a supremum of continuous functions, lower semicontinuous. Right. (The text says "they tend to it" without the
  bracket bound; the bound above is the one line it needs.)
- So lambda_0,t is continuous and positive, and S_t(N; B) = Z_t(N)/lambda_0,t^N - 1 is continuous. The set
  {t : S_t < 1/5041} is the preimage of an open set, open in [0, 1]. (i) is openness at 0. (ii): the limit of
  S_(t_k) <= q along t_k -> 0 is S_0 <= q < 1/5041. Right.
- If only k >= 3 is allowed (tori with sides at least 3), the inf and the sup over k >= 3 are the same limits,
  so nothing changes.
- S here is Z/lambda_0^N - 1, the S of the setting of Lemmas K, X, E (`gap-crux-restate.md` L174), which is the
  S of the seed in Theorem S. Consistent.

The step-8 correction (L123) is right to drop the earlier inference: the continuity of two traces does not give
norm continuity of T_t, and the proof above does not need it.

The Reading (L125) follows from (ii) with one detail: (ii) needs a uniform margin q < 1/5041 along the sequence;
"seeds of bounded size" then gives one N that repeats along a subsequence (pigeonhole), and (ii) applies. Seeds
with S_(t_k) -> 1/5041 from below would not carry back. The proposition states the margin; the Reading leaves it
implicit. Not a defect in the proposition.

