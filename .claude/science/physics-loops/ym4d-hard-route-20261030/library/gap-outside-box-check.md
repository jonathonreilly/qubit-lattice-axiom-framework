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

