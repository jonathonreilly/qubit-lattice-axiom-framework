lead: anthropic/claude-fable-5-2 laptop subagent
Started Sat Nov 28 18:14:30 UTC 2026. Author only, checked by no one.

# FINISH row 1722: ladder PS, rung PS7 — the right statement (PS')

## 0. Plan

1. Read library/ladders/README.md, PS.md, row 1716 (gap-largen-ps-tool-fable.md) in full, row 1708 section 7 (Theorem T), row 1717 (Lemma I).
2. Find why (PS) fails in the twin's weak phase; state the replacement (PS').
3. Check line by line that (PS') feeds Theorem T and Lemma I.
4. Prove (PS') in the twin in both phases; prove what is possible in 4D.
5. Decide on the Wilson action at large N; effect on the SU(2) consumer.
6. Ladder update. RESULT line.

Sources read: the brief; library/ladders/README.md and PS.md; row 1716 (library/gap-largen-ps-tool-fable.md) in full; row 1708 (library/gap-largen-build-fable.md) in full; row 1717 (library/gap-largen-ld-build-fable.md) in full; on the coordinator's mid-task note, check 1715 (library/gap-largen-build-fable-check-astra62.md), sections 4 to 7. Row 1720 was not read. No web. Scripts: /private/tmp/claude-501/largen-ps7/fam.py and encl.py (python3 -I, fractions only). Every citation below is from memory and UNVERIFIED unless it names a lane file.

## 1. Verdict first

1. The right statement is not linear. In the twin's weak phase every linear lower bound for 1 - DF(W) on bounded loop functions fails (row 1716), and it also fails on differences of positive solutions (section 3.3). The loop equations are first-variation equations. What repairs them in the twin is positivity plus one more exact equation, not a better norm.
2. New exact equation, the centre equation (Lemma Z, PROVED, 4D, every N >= 3, every beta > 0, every volume and boundary condition): |sum_{p contains e} Im E tr U_p| <= 6 tan(pi/N). It comes from the translation U_e -> e^(2 pi i/N) U_e and Jensen's inequality. At N = infinity it reads (CE): sum_{p contains e} (W(p) - W(p^-1)) = 0 at every link.
3. New refutation (PROVED in the twin, exact checks): the SU(N) planar equation of row 1708, with its last term and without (CE), has a one-parameter family of exact positive-type solutions through the Gross-Witten field in the weak phase (Im W_1 != 0; "winding" family). So (GPU) of row 1717 and the hypothesis of its Corollary U are FALSE as stated in the SU(N) twin for beta > 1. With (CE) the last term of the planar equation is zero and the family is excluded.
4. Replacement (PS'), section 4: positive planar stability. For functions of tracial type on the loops of a ball, with free boundary values: small defect in the planar equations and in (CE) gives closeness to W_beta at the centre. It is (GPU) plus the hypothesis (CE). It allows any modulus. In the twin it is PROVED in both phases (Theorem U1 and Corollary U2), and a Lipschitz modulus is PROVED impossible in the weak phase (atom family: distance at least c sqrt(defect/l1)).
5. (PS') feeds Lemma I of row 1717 with one added line (Lemma Z with sources); checked line by line in section 5.1. It gives (LD). It does NOT feed Theorem T as row 1708 wrote it: step 3 of Theorem T needs a linear inverse on good regions, and the twin shows that no such inverse exists in a weak phase (the bad direction is reachable inside the small-field region). (PS') gives clustering down to a floor (Corollary T', PROVED as an implication). A gap at fixed N needs a further input, named (RESP) in section 5.3: a Lipschitz, sourced, linear statement on the response class. This is also the relation to N^2 Cov that check 1715 asks for.
6. Wilson action: keep it for the theorem, at a beta on the weak side outside the metastability window of the reported bulk transition (UNVERIFIED lore). Inside that window (PS') is expected FALSE for the Wilson action (ARGUED: metastable planar states solve the loop equations). Fallback: the fundamental-adjoint action with negative adjoint coupling. Its planar equation is the Wilson planar equation with the coupling beta + 2 gamma W(p) (Lemma M, PROVED at the level of the equation). The SU(2) consumer is not affected by either choice, because the large-N theorem is a separate theorem (row 1708 section 9).
7. Proof route in 4D at order-one beta (section 7): (PS') is the statement that a loop-equation bootstrap certifies. A dual feasible point of the positivity programme on a ball is a finite exact certificate for (PS') at one (eps, l0). In the twin the exact enclosure of W_1 closes to below 2^-14 at length 16 in both phases (exact tests, guide). Nothing is proved in 4D beyond Lemma Z, Lemma M and the implications.

## 2. The twin, solved on the positive class

Twin of row 1716, section 4.2: loops p^k, W_k = tau(v^k) for one unitary v, u = beta/2 > 0. Positive type means W_k = int e^(ik theta) d rho for a probability measure rho on the circle, W_-k = conj(W_k). The SU(N) planar equation of row 1708 section 7 for the loop p^k (n_e = t_e = k, one plaquette), with s = Im W_1:

  (1 - 2 i u s) W_k = - sum_{j=1}^{k-1} W_j W_{k-j} + u (W_{k-1} - W_{k+1}),  k >= 1.     (P)

The term 2 i u s W_k is the last term of F: u W_k (W_1 - W_-1). For U(N) it is absent. The twin of (CE) is s = 0. With s = 0 the two groups have the same equation.

Generating identity (PROVED, as in row 1716). G = sum_{k>=1} W_k z^k, b' = 1 - i beta s + u(1/z - z), S = b' + 2G. (P) for all k is G^2 + b' G - u(z + W_1) = 0, so S^2 = b'^2 + 4u(z + W_1). H = 1 + 2G = int (1 + z e^(i theta))/(1 - z e^(i theta)) d rho is analytic in the disc with Re H > 0. On the circle z = e^(i theta), with R = Re W_1:

  S^2 = g(theta) := 1 + 2 beta R + 2 beta cos(theta) - beta^2 (s + sin(theta))^2  (real),  and  Re H = Re S.

(The imaginary parts cancel exactly when s = Im W_1; this fixes the sign of the last term.)

### 2.1 Theorem U1 (uniqueness with the centre equation). PROVED

For every beta > 0 the system (P), s = 0 has exactly one solution of positive type: W_1 = beta/2, W_k = 0 (k >= 2) for beta <= 1, and the Gross-Witten field, W_1 = 1 - 1/(2 beta), for beta >= 1.

Proof. s = 0. Put zeta = z + 1/z and D = 4u(u - W_1) = beta^2 - 2 beta W_1. Then z^2 S^2 = u^2 z^4 + 2u z^3 + (1 - 2u^2 + 4u W_1) z^2 + 2u z + u^2 (row 1716), which is

  S^2 = (1 + u zeta)^2 - D.

S = H + u(1/z - z) is analytic in the punctured disc, so every zero of S^2 there has even order.
(a) D < 0. The zeros are at zeta = (-1 +- i sqrt|D|)/u, not real. z + 1/z = zeta has two roots with product 1, not on the circle (there zeta is real), and the four roots are simple. One is in the open disc. Contradiction.
(b) D = 0. S = 1 + u zeta (the sign is fixed by the pole u/z of S at 0). H = 1 + 2uz. Re H = 1 + beta cos(theta) on the circle. This is positive type exactly for beta <= 1.
(c) D > 0. Zeros at zeta_+- = (-1 +- sqrt D)/u, real and different. If |zeta_-| > 2 the roots of z + 1/z = zeta_- are real and simple, one in the open disc. Contradiction. So -1 - sqrt D >= -2u, that is sqrt D <= beta - 1; this needs beta > 1. Then all four zeros are on the circle, S is continuous on the closed disc minus 0, and rho = Re S d theta/(2 pi). On the interval (-1, 0) of the real axis zeta < -2, S^2 has no zero and is positive, S is real, and S has the sign of u/z, which is negative. So S(-1) = - sqrt(g(pi)) with g(pi) = (beta - 1)^2 - D. If sqrt D < beta - 1 the density is negative near theta = pi. Contradiction. So D = (beta - 1)^2, W_1 = 1 - 1/(2 beta). For this value g = beta^2 (1 + cos theta)(cos theta - x), x = 1 - 2/beta, S > 0 on the arc cos theta > x (it is positive at z = 1), S is imaginary off the arc, and rho >= 0.
Existence in each case: the S found defines H with H(0) = 1, Re H >= 0, and the quadratic identity is (P). QED.

By-product (PROVED): for beta > 1 the solutions of (P), s = 0 with all |W_k| bounded are exactly W_1 in [1 - 1/(2 beta), beta/2]. Only the left end is positive. Inside the interval the solution has a negative density on a second arc at theta = pi. Outside it G has a branch point in the open disc, so the W_k are not bounded. So the Gross-Witten field is on the boundary of the bounded solutions. The even kernel of row 1716 is the one-sided tangent of this family.

### 2.2 Proposition W (the winding family). PROVED by construction; exact checks

For beta > 1 and |phi| small put

  s = sin(phi) - tan(phi)/beta,  R = ( tan^2(phi) - 1 + 2 beta cos(phi) ) / (2 beta),  W_1 = R + i s.

Then (P) with this W_1 has a solution of positive type, and s != 0 for phi != 0 (ds/dphi = 1 - 1/beta at 0). So the SU(N) planar equation of the twin, as written in row 1708, has a curve of positive solutions through the Gross-Witten field.
Proof. With these values g(pi + phi) = 0 and g'(pi + phi) = 0 (direct substitution: g' = -2 beta^2 (s + sin) cos - 2 beta sin). At phi = 0, g = beta^2 (1 + cos)(cos - x) has a double zero at pi, where g <= 0 nearby, and two simple zeros. For small phi the double zero stays (by the choice of R, s) and the simple zeros move continuously. z^2 S^2 is a quartic and z^-2 times it is real on the circle, so its four zeros are these. S is then single-valued in the disc, real and positive on the arc where g > 0, imaginary elsewhere. H = S - u(1/z - z) + i beta s has H(0) = 1, first coefficient 2 W_1 (expansion of the square root at 0), and Re H = Re S >= 0 on the circle. QED.

What the family is (ARGUED). In eigenvalue form (P) is the equilibrium condition with the force beta (sin theta - s), s = int sin d rho: the trace direction is projected out. An equilibrium measure on an arc under the force beta sin theta + mu has int (beta sin theta + mu) d rho = 0 automatically, so every mu is self-consistent. These are the planar limits of the SU(N) one-plaquette law conditioned on the sum of the principal eigenangles, sum theta_i = 2 pi n with n/N fixed. They are large-deviation states at speed N^2. The loop equation does not see the condition, because it is locally constant on SU(N) away from the wall "an eigenvalue at pi", where the weak-phase density is zero. In the strong phase there is no gap and no such family near the master field (by-product of 2.1 for s = 0; for s != 0 near 0 I did not prove it).

Consequences (PROVED in the twin):
- "Exactly one solution of tracial type" (hypothesis of Corollary U, row 1717) is false for the SU(N) twin at beta > 1.
- (GPU) of row 1717 is false there for every (l1, delta): the family has defect 0 and distance |s| from W_beta on the loop p.
- The odd SU kernel of row 1716, -u delta_1 (P_k - P_{k-1}), is the tangent of this family (same generating function to first order; not re-derived line by line here).
- The last term of (SD) does not select the state. A second relation does: (CE).

### 2.3 Proposition A (the atom family; no Lipschitz modulus). PROVED by construction; exact checks

Let Phi_rho(f) = (1/2) int int (f(theta) - f(phi)) cot((theta - phi)/2) d rho d rho - beta int f sin d rho, with the value 2 f'(theta) of the kernel on the diagonal. PROVED identity: Phi_rho(e^(ik theta)) = i d_k, where d_k = W_k + sum_{j<k} W_j W_{k-j} - u(W_{k-1} - W_{k+1}) is the defect of (P) at s = 0. An atom of mass alpha at pi adds the diagonal term alpha^2 f'(pi). So a measure rho_alpha = alpha delta_pi + (arc part in equilibrium with the atom) has defect exactly

  d_k = (-1)^k k alpha^2  for all k,  with Im W_1 = 0.

Exact form: S^2 = (1 + u zeta)^2 - D - 4 alpha^2/(zeta + 2); the arc part is in equilibrium when [(1 + u zeta)^2 - D](zeta + 2) - 4 alpha^2 = u^2 (zeta - zeta_a)(zeta - zeta_d)^2. Then D = (1 + u zeta_d)^2 + 2u(1 + u zeta_d)(zeta_d + 2) and 4 alpha^2 = -2u(1 + u zeta_d)(zeta_d + 2)^2. A positive atom needs zeta_d < -2 (S must change sign on (-1, 0)). Rational instance: beta = 2, zeta_d = -17/8, alpha = 3/32, D = 99/64, W_1 = 157/256, zeta_a = 1/4.
Meaning. With defects required only for k <= l1: defect delta = l1 alpha^2, distance |W_1 - 3/4| = 35/256 at alpha = 3/32, and of order alpha in general (first order in alpha; the tangent is the even kernel of row 1716). So every modulus in the twin's weak phase has eps >= c sqrt(delta/l1). A linear bound ||w - W|| <= kappa (defect) is false on positive functions. The same family shows that a linear lower bound fails on differences of positive approximate solutions: the linear residual of rho_alpha - rho_0 is its defect minus a quadratic term, both of order alpha^2 k.
Positivity of rho_alpha for all k: from the construction (density S/(2 pi) > 0 on the arc zeta > zeta_a, atom alpha > 0). I label the sign discussion ARGUED and the finite checks below exact.

### 2.4 Exact checks (fam.py)

Core (complex rationals as pairs of Fractions; Toeplitz matrix T[j][k] = W_{j-k}; pivots of Hermitian elimination without pivoting):

```
def su_twin(beta,W1,K,defect=None):
    # W_{k+1} = W_{k-1} - (1/u)[(1-2ius)W_k + sum_{j<k} W_j W_{k-j} - d_k],  s = Im W_1
    u=beta/2; s=W1.b; W=[C(1),W1]; fac=C(1,-2*u*s)
    for k in range(1,K):
        acc=fac*W[k]
        for j in range(1,k): acc=acc+W[j]*W[k-j]
        if defect: acc=acc-C(defect(k))
        W.append(W[k-1]-C(1/u)*acc)
    return W
# family: t = tan(phi/2); sn=2t/(1+t^2); cs=(1-t^2)/(1+t^2); tn=2t/(1-t^2); s=sn-tn/beta; R=(tn*tn-1+2*beta*cs)/(2*beta)
```

Output (floats only print exact rationals):

```
A t=1/10  W_1 = 2931695/3959604 + i*(970/9999)
  family member : max|W_k|^2 for k<=200 = 0.557605 ; Toeplitz size 22 pivots all >0: True ; min pivot 6.114e-07
   W_2 = 0.240777 +0.046642i ; |W_200| = 4.494e-05
  same s, Re W_1 + 1/1000 : max|W_k|^2 for k<=200 = 0.559086 ; Toeplitz size 22 pivots all >0: False ; min pivot -1.046e+01
  same s, Re W_1 - 1/1000 : max|W_k|^2 for k<=200 = 0.556125 ; Toeplitz size 22 pivots all >0: False ; min pivot -7.666e-05
A t=1/4  W_1 = 10763/15300 + i*(52/255)
  family member : max|W_k|^2 for k<=200 = 0.536446 ; Toeplitz size 22 pivots all >0: True ; min pivot 5.025e-06
   W_2 = 0.213368 +0.082981i ; |W_200| = 1.372e-04
  same s, Re W_1 + 1/1000 : ... Toeplitz size 22 pivots all >0: False ; min pivot -1.886e-02
  same s, Re W_1 - 1/1000 : max|W_k|^2 for k<=200 = 171.911202 ; Toeplitz size 22 pivots all >0: False ; min pivot -6.501e-03
GW beta=2 : max|W_k|^2 for k<=200 = 0.562500 ; Toeplitz size 22 pivots all >0: True ; min pivot 4.070e-07
B atom family alpha=3/32 : max|W_k|^2 for k<=200 = 0.376114 ; Toeplitz size 22 pivots all >0: True ; min pivot 1.612e-07
   W_k-(-1)^k alpha at k=50,100,199,200: 1.251e-03 -4.322e-04 -1.855e-04 -1.468e-04
   W_1(GW)-W_1 = 35/256 ; defect at k: k*alpha^2 = k*9/1024
  same W_1, no defect : max|W_k|^2 for k<=200 = 5.1e+76 ; Toeplitz size 22 pivots all >0: False ; min pivot -2.189e-02
```

(Two lines are shortened here: "..." and the value 5.1e+76 replace a repeated field and a 77-digit number.) What this certifies: at beta = 2 the two family members (Im W_1 = 970/9999 and 52/255) and the atom member satisfy their recursions exactly (by construction), stay bounded to k = 200, and have positive definite Toeplitz matrices of size 22 (exact). A change of Re W_1 by 1/1000 at the same s destroys positivity at size 22. The atom member's moments tend to (-1)^k alpha. This is not a proof for all k; the proofs are 2.2 and 2.3.

### 2.5 Corollary U2: (PS') holds in the twin in both phases. PROVED

Twin form of (PS'): for every beta > 0, eps > 0 and l0 there are l1 and delta > 0 such that every probability measure on the circle with |d_k| <= delta for 1 <= k <= l1 (d_k the defect of (P)) and beta |Im W_1| <= delta has |W_k - W_beta,k| <= eps for k <= l0.
Proof. If not, there are measures rho_n with l1 = n, delta = 1/n and some k <= l0 with |W_k - W_beta,k| > eps. A weak limit point is a probability measure; each equation has finitely many terms, so the limit solves (P) with s = 0 for all k; and it differs from W_beta at some k <= l0. This contradicts Theorem U1. QED.
The constants are not explicit. By Proposition A, delta <= C l1 eps^2 in the weak phase. GUESSED: delta of order eps^2 is enough there, and delta of order eps in the strong phase.

## 3. What 4D has that the loop equation alone does not: two exact relations. PROVED

Setting of row 1708 section 2: SU(N), Wilson law in a finite set of links with any boundary condition, w(l) = E tr U_l.

### 3.1 Lemma Z (centre equation)

Let N >= 3, beta > 0, and let e be an integrated link whose six plaquettes are in the action, each written as a word p that starts with e. Then

  | sum_{p contains e} Im w(p) | <= 6 tan(pi/N).

With sources (the law mu_J of row 1717 section 5, extra factor exp(N^2 sum_j J_j Re(c_j tr U_{l_j})), |c_j| = 1, t_j = t_e(l_j)):

  | beta sum_{p contains e} Im w_J(p) + sum_j J_j t_j Im(c_j w_J(l_j)) | <= (pi/N) ( 6 beta + sum_j |J_j| t_j^2 ) + 4 pi^2 beta / N^2.

Proof. z = e^(2 pi i/N) times the identity is in SU(N). The map tau: U_e -> z U_e keeps Haar measure, so E[exp(S o tau - S)] = 1 and, by Jensen, E[S o tau - S] <= 0. Under tau, Tr U_p -> z Tr U_p for the six words p and Tr U_l -> z^(t_e(l)) Tr U_l. Without sources: S o tau - S = N beta sum_p [ (cos(2 pi/N) - 1) Re Tr U_p - sin(2 pi/N) Im Tr U_p ]. So - sin(2 pi/N) sum Im w(p) <= (1 - cos(2 pi/N)) sum Re w(p) <= 6 (1 - cos(2 pi/N)), that is sum Im w(p) >= -6 tan(pi/N). The map tau^-1 gives the other side. With sources use |z^t - 1 - 2 pi i t/N| <= 2 pi^2 t^2/N^2, N^2 (1 - cos(2 pi/N)) <= 2 pi^2 and |N sin(2 pi/N)/(2 pi) - 1| <= 2 pi^2/(3 N^2), and divide by 2 pi N. QED.

Remarks.
- At N = infinity: (CE) sum_{p contains e} (W(p) - W(p^-1)) = 0 at every link, and with sources the lattice Maxwell equation beta d^* Im w(p) = - (current of the sources). The powers z^k give more (PROVED the same way, k/N -> nu): the number sum_{p contains e} W(p) is real and >= 0.
- On a function that satisfies (CE) the last term of F^e_beta of row 1708 is zero. So the SU(N) planar system with (CE) is the U(N) planar system with (CE). For U(N), (CE) is the loop equation in the trace direction and is exact at every N. So no planar single-loop statement built from these equations reads the group. This agrees with check 1715 section 7 ("FAILS at must") and replaces the claim of row 1708 that the last term is the selective line at leading order. The two groups differ in the size of the (CE) defect (0 against pi/N) and at order N^-2.
- N = 2: z = -1, sin = 0, the lemma is empty; all traces are real.
- Twin: (CE) is Im W_1 = 0. It removes the winding family of 2.2.

### 3.2 Lemma Z2 (staple alignment inequalities)

Let beta > 0, e as above with initial site x, and C any closed word at x that does not contain e or e^-1. Then, for every N >= 1 and every boundary condition, for SU(N) and for U(N):

  sum_{p contains e} Re w(C p) <= sum_{p contains e} Re w(p).

Proof. g = U_C does not depend on U_e. The map U_e -> g U_e keeps Haar measure given the other links, and S o tau - S = N beta sum_p Re Tr((g - 1) U_p) = N^2 beta sum_p Re( tr U_{C p} - tr U_p ). Jensen. QED.
These are linear inequalities with no error term. They come from a finite displacement, so they are not consequences of the loop equations. I use them only as extra constraints for the certificate of section 7. They are empty in the twin.

### 3.3 Why no linear statement on bounded loop functions can be right

PROVED in the twin (2.1 by-product, 2.3): the Gross-Witten field is a boundary point of the set of bounded solutions, and positive approximate solutions exist at distance alpha with defect alpha^2 l1. So in a weak phase the map defect -> distance is of square-root type on the positive class. Check 1715 section 4 proves that (PS) gives local isolation among bounded solutions; the twin's weak phase has no such isolation (the interval of 2.1). The two facts agree: (PS) is false there.

## 4. The replacement (PS')

Notation of row 1717 section 6.2. F0^e_beta is F^e_beta of row 1708 without its last term. w is of tracial type on the loops of cl(Delta^+).

**(PS')(beta; eps, l0, L, l1, delta), positive planar stability.** For every cube Delta of side L and every w of tracial type on the loops in cl(Delta^+): if
 (P) |w(l) - F0^e_beta(w)(l)| <= delta for every loop l in cl(Delta^+) with |l| <= l1 - 4 whose plaquette deformations at e stay in cl(Delta^+), and every link e of l in Delta^+, and
 (C) |beta sum_{p contains e} Im w(p)| <= delta for every link e in Delta^+,
then |w(l) - W_beta(l)| <= eps for every loop l in Delta with |l| <= l0.
Here W_beta is a fixed translation-invariant solution of (P), (C) with delta = 0 on Z^4, of tracial type, with W_beta(p) real.

**(PS'_exact).** The system (P), (C) with delta = 0, for all loops and links of Z^4, has exactly one solution of tracial type. (No invariance is assumed of w.) By the compactness argument of Corollary U of row 1717, which applies word for word, (PS'_exact) gives (PS') for every (eps, l0) with some (L, l1, delta).

**(PS'_m), rate form.** (PS') holds for all L >= L_0 with eps = kappa (e^(-m L) + delta^theta + a^(l0 - l1)), for fixed m > 0, theta in (0, 1], a > 1. The twin allows theta = 1/2 at most in a weak phase.

How (PS') differs from (PS) and from (GPU):
- Class: positive (tracial) functions with free boundary values, not bounded functions. This excludes the bounded non-positive solutions of 2.1.
- One more equation: (C). This excludes the winding family of 2.2. With (C) the last term is not needed.
- Nonlinear, any modulus. This admits the square-root behaviour of 2.3.
- Centre: W_beta is defined as a solution of the system, as check 1715 section 4 asks (a specified state). That the Wilson states converge to it is a conclusion (Corollary T'), not a hypothesis.

(i) Twin test. (PS') holds in the twin for every beta > 0 (Corollary U2). (PS) is false there for beta > 1 (row 1716). (GPU) without (C) is false there for SU(N), beta > 1 (2.2). So the twin's weak-phase solution is excluded by positivity, and the new family by (C). PROVED.

## 5. What (PS') feeds

### 5.1 Lemma I of row 1717, line by line. PROVED as an implication

**Lemma I'.** Let beta > 0. Assume (PS')(beta; eps, l0, L, l1, delta), eps, delta <= 1. Then the conclusion of Lemma I holds with delta replaced by delta/4: for N^2 >= max( N_I^2(delta/4), (8 pi (6 beta + l1)/delta)^2, 64 pi^2 beta/delta ), (SC)(beta, N; 3 sqrt 2 eps, l0, L, p) holds with p = 4 n(L, l0) exp(-delta eps N^2/(32 l1)), and (LD) with centre W_beta and c = delta eps/(64 l1) for N^2 also above 64 l1 log(4 n)/(delta eps).
Check of each step of the proof of Lemma I, with lambda = delta/(48 l1), lambda_1 = lambda eps/(4M):
- Step 1 (sourced loop equation): no change. It uses Lemma 1 of row 1708 and |tr| <= 1.
- Step 2 (defect): no change. It bounds the defect for F^e_beta, with the last term.
- Step 3 (a good source J'): as before the F-defect of w_J' is at most delta/4 and eta_e(J') <= 3 lambda l1 = delta/16. New line: by Lemma Z with sources, |beta sum Im w_J'(p)| <= eta_e + (pi/N)(6 beta + l1 eta_e) + 4 pi^2 beta/N^2 <= delta/16 + delta/8 + delta/16 = delta/4 for the stated N. This is (C). The last term of F is at most (beta/2)(|t_e|/n_e) 2 |sum Im w(p)| <= delta/4, so the F0-defect is at most delta/2. This is (P). w_J' is of tracial type. (PS') gives d_j P(J') <= W_j + eps.
- Step 4 (convexity transfer, Chernoff, Lemma D): no change.
QED. The U(N) form holds with (C) exact. N = 2 never enters (N_I^2 > 384 M^2).
Check 1715 section 5 (the event of (LD) fails at low rank; a bias bound is needed): Lemma I' gives (LD) only above an explicit rank, and (PS') is exactly the bias bound, for all boundary conditions at distance L.

### 5.2 Theorem T of row 1708, line by line

- Step 1 (Lemma 1): unchanged. Lemma Z is added.
- Step 2 (small-field loop equations with a cutoff): not used. Lemma F of row 1717 replaces it: for most small sources the one-loop function w_J has small defect, with no cutoff and no pinning. This removes the cutoff terms that check 1715 section 6 item 1 names.
- Step 3 ((PS) inverts the linearised equation on good regions; no floor): FAILS, and cannot be repaired by any statement that is true in the twin's weak phase. Reason (PROVED in the twin): a state with a fraction alpha of the eigenvalues at pi is inside every small-field region of tolerance above alpha, its difference from the master field has linear residual of order alpha^2, and its probability is exp(-c alpha N^2). The bad direction is paid for by the measure, linearly in alpha, not by an inverse of the loop operator.
- Step 4 ((LD), dilute bad cubes): (LD) is supplied by Lemma I'. The expansion of the law across good regions is not supplied (check 1715 section 6 item 3).
- Step 5 (transfer gap from floor-free clustering): unchanged, and not reached.

What (PS') does give:

**Corollary T' (clustering to a floor; PROVED as an implication).** Assume (PS')(beta; eps, l0, L, l1, delta), beta > 0, and N as in Lemma I'. For every finite Lambda that contains Delta^+, every boundary condition, every loop l in Delta with |l| <= l0:
 (a) |E_{Lambda,b} tr U_l - W_beta(l)| <= 3 sqrt 2 eps + 2p;
 (b) |Cov(tr U_l, G)| <= 2 (3 sqrt 2 eps + 2p) sup|G| for every bounded G of the links outside Delta^+.
Proof. (a) for Lambda = Delta^+: off the bad event the distance is at most 3 sqrt 2 eps, on it at most 2. For larger Lambda use the Markov property. (b) Cov(tr U_l, G) = E[(E[tr U_l | links outside Delta^+] - E tr U_l) G], and both means are within (a) of W_beta(l). QED.
So (PS'_exact) gives: the planar limit of single-loop means exists, is W_beta, and does not depend on the boundary condition. With (PS'_m) the floor at rank N is of order e^(-m L_N theta'), L_N the largest L allowed by the rank condition (N of order L^4 8^l1/delta). This is a floor, not a gap.

### 5.3 Relation to the connected response N^2 Cov (answer to check 1715 section 4)

Three levels must be kept apart.
1. Means, order one: (PS'). It says nothing about a mass. At a factorised field the connected function of normalised traces is zero at leading order (check 1715).
2. Response, order N^-2. Put chi_c(l; l') = d/d lambda of w_lambda(l) at lambda = 0, where w_lambda is the mean under the extra factor exp(lambda N^2 Re(c tr U_l')). At finite N this is N^2 Cov(tr U_l, Re(c tr U_l')). Differentiating the sourced system (P), (C) (formal; PROVED as algebra when the derivative exists and factorisation holds to first order in lambda) gives the response equation:
   chi - DF0^e(W_beta) chi (l) = sigma^e_{l'}(l), a row that is zero unless e is a link of l' (it holds the deformations of l by l' at e, with modulus at most n_e(l')/n_e(l) in total);
   beta sum_{p contains e} Im chi(p) = - t_e(l') Im(c W_beta(l')).
   The source is localised on the links of the second loop. This is the equation that check 1715 section 6 item 2 says is missing, at N = infinity. The second line is a Maxwell equation: on the links of l' the plaquette field Im chi(p) is forced to be nonzero. Whether the solution decays (a spanning-surface solution) or is a Coulomb field (a closed solution) is the place where SU(N) and U(N) must differ. It is not decided by (P), (C). GUESSED.
3. Fixed rank, all orders: a gap at fixed N. Not reached by 1 or 2.

**(RESP)(beta; m, kappa), the statement a gap needs at level 2 (STATED, OPEN).** Let R_W be the space of hermitian functionals chi on the loop algebra with chi(1) = 0 that are continuous for the C*-seminorm of the representation of W_beta (no weight outside the spectrum of the master field). For chi in R_W that solves the response equation with source at l': |chi(l)| <= kappa C(l) C(l') e^(-m dist(l, l')).
Twin: on measures carried by the arc, with zero mass, the linearised operator with (C) is rho times the finite Hilbert transform, and it is injective (ARGUED from the classical airfoil equation; the atom at pi and the tangent of the winding family are not in the class or violate (C)). So a linear statement survives in the twin only on R_W. It applies to minimisers, not to all positive approximate solutions. That N^2 Cov has its limit in R_W is itself a consequence of an (LD)-type bound (eigenvalues outside the spectrum cost exp(-cN) each). ARGUED.
I do not claim that (PS') gives (RESP), or that (RESP) gives a gap at fixed N. The chain is (PS') -> (LD) and the floor; (RESP) -> decay of the planar connected functions; a fixed-N gap needs an expansion of the law in which (LD) pays for the directions outside R_W.

## 6. Is the Wilson action the right one at large N?

Reported fact (numerical physics, from memory, UNVERIFIED): 4D SU(N) Wilson theory has a first-order bulk transition at an order-one beta for N above about 5, with strong metastability at large N.

**Consequence for (PS') (ARGUED, conditional on that fact).** At N = infinity a metastable state is a restriction of the Wilson law to a set with boundary flux exp(-c N^2). It satisfies the loop equations and Lemma Z in the limit, and it is of tracial type. So in the whole metastability window, not only at the transition point, the system (P), (C) has at least two tracial solutions (three with the unstable branch), and (PS'_exact) and (PS') are false for the Wilson action there. (LD) can still be true there away from the transition point, but Lemma I' cannot prove it. Check 1715 section 4 notes that coexistence does not refute the local, linear (PS); it does refute a global uniqueness statement, and Lemma I needs a global one because the boundary is free.

**Lemma M (mixed action; PROVED at the level of the equation).** Take S = N beta sum_p Re Tr U_p + gamma sum_p Tr U_p Tr U_p^-1. Then d_a S = (N/2) sum_p [ (beta + 2 gamma tr U_p^-1) Tr(T_a U_p) - (beta + 2 gamma tr U_p) Tr(T_a U_p^-1) ], and with the proof of Lemma 1 of row 1708 and factorisation the planar equation is F0 with the deformation term

  (1/2) sum_x eps_x sum_p [ (beta + 2 gamma W(p)) W(l (-)_x p) - (beta + 2 gamma W(p^-1)) W(l (+)_x p) ].

The last term and Lemma Z do not change (the new term is invariant under the centre translation, and its 1/N parts cancel). So the planar solutions of the mixed action are the Wilson planar solutions with the local coupling beta_p = beta + 2 gamma W(p). For an invariant real solution: W = W^Wilson_{beta'} with beta' = beta + 2 gamma W^Wilson_{beta'}(p).
Twin (PROVED from 2.1): beta = beta' - 2 gamma W_1(beta'), W_1 = beta'/2 or 1 - 1/(2 beta'). For gamma <= 0 the map beta' -> beta is increasing, so the mixed twin has one positive solution for every beta. For gamma > 1 it is decreasing on the strong branch, and several solutions exist: a positive adjoint coupling makes a first-order structure, a negative one removes it.
4D (ARGUED): if the Wilson curve beta' -> W(p) has an S shape, then for gamma < 0 with 2|gamma| > max |d beta'/dW| on the back-bending branch the map to beta is monotone. The mixed action then has no bulk transition at N = infinity, and its master fields include the Wilson-unstable branch.
Reflection positivity for gamma < 0: holds for reflections in planes of sites for every real plaquette action (ARGUED, standard argument); positivity of the one-step transfer operator needs positive character coefficients and is NOT checked.

**Decision.**
1. Keep the Wilson action as the first target, at one beta on the weak side above the upper end of the metastability window. There (PS'_exact) is not excluded by anything in this file. The window itself must be located by the certificate of section 7 (it fails to close inside the window).
2. If the continuum-side beta of interest is inside the window, or a connected beta range is wanted, use the mixed action with gamma < 0. Then (PS') is a statement about Wilson planar equations with self-consistent local couplings.
3. The SU(2) consumer: no effect in either case. Row 1708 section 9 already has the large-N theorem as a separate theorem with no interpolation in N. If one family for all N were wanted, the SU(2) results would have to be proved again for the mixed action; I do not recommend that.

## 7. A proof route for (PS') at order-one beta in 4D (ARGUED)

(PS') quantifies over positive functionals on a finite loop algebra that satisfy finitely many polynomial relations. This is the form of a loop-equation bootstrap (Anderson-Kruczenski; Kazakov-Zheng; from memory, UNVERIFIED). The certificate:
- Variables: w(l) for loops in cl(Delta^+) up to length l1, no symmetry assumed.
- Constraints: the Gram matrix [w(l_i^-1 l_j)] of open paths is positive semidefinite (tracial type); (P) with the split products relaxed by a second positive matrix; (C); the inequalities of Lemma Z2; |w| <= 1.
- Claim: max and min of Re w(l), Im w(l) for the short loops at the centre.
- Proof object: a dual feasible point with rational entries. Weak duality is a finite identity; Lean can check it. A defect delta changes the bound by delta times the sum of the dual multipliers, so one certificate proves (PS') with an explicit delta.
What is new against rung PS4: the certificate proves a statement that is true in the twin's weak phase, it needs no tail lemma (the truncation only weakens the bound), and positivity is used in the statement itself.
Twin instance (encl.py; exact tests at dyadic points, bisection outward from the master value; a guide, because the admissible set is assumed to be an interval near it). A_K = { r = W_1 : |W_k(r)| <= 1 for k <= K and the Toeplitz matrix of size K+1 has positive pivots }:

```
beta=2 K=4 master ok=True  excluded: r <= r0 - 2163/16384 (1.32e-01)  and  r >= r0 + 7/8192 (8.54e-04)
beta=2 K=8 master ok=True  excluded: r <= r0 - 77/16384 (4.70e-03)  and  r >= r0 + 1/16384 (6.10e-05)
beta=2 K=16 master ok=True  excluded: r <= r0 - 1/16384 (6.10e-05)  and  r >= r0 + 1/16384 (6.10e-05)
beta=9/10 K=4 master ok=True  excluded: r <= r0 - 543/8192 (6.63e-02)  and  r >= r0 + 435/16384 (2.66e-02)
beta=9/10 K=8 master ok=True  excluded: r <= r0 - 5/1024 (4.88e-03)  and  r >= r0 + 27/8192 (3.30e-03)
beta=9/10 K=16 master ok=True  excluded: r <= r0 - 1/8192 (1.22e-04)  and  r >= r0 + 1/8192 (1.22e-04)
```

(K = 24, 32: the same as K = 16 up to the resolution 2^-14.) Each "excluded" value is an exact test at that point. So in the twin the positivity enclosure closes at length 16 in the weak phase (beta = 2) as well as in the strong phase. In the twin the equations fix all W_k from W_1; in 4D they do not, and the cost of a ball without symmetry is far above the counts of row 1716 section 6. I did not size it.
Other route (GUESSED): a variational proof. In the twin the master field is the unique minimiser of a strictly convex free energy, J(nu) - J(rho) = ||nu - rho||^2 (logarithmic energy) + 2 int V_eff d nu, and this, not the loop equation, is what excludes the atom at speed N^2. The 4D analogue is a free-entropy functional; no formula is known to me. Convexity of the action itself stops at beta = 1/12 (row 1717 Proposition B).

## 8. What is proved in 4D, and what is open

PROVED in 4D (author only): Lemma Z, Lemma Z2, Lemma I', Corollary T' (the last two as implications), Lemma M (equation level).
NOT proved in 4D: (PS') at any beta. At |beta| < 1/48 row 1717 gives the Wilson-law form (its Theorem LD1 with Theorem R(b)), not the tracial form.
Open by name:
- (PS'_exact) for the Wilson action at one weak-side beta; the 4D analogue of the winding family (a tracial solution of the row 1708 equation with sum Im W(p) != 0) is GUESSED to exist and was not built.
- The metastability window (location; whether the weak-side target is outside it).
- (RESP); the spanning-surface against Coulomb alternative for the sourced (C).
- The step from the floor to a fixed-rank gap.
- Explicit modulus in the twin (delta of order eps^2 is GUESSED).
- For U(N) without (C) I did not classify the positive solutions with Im W_1 != 0.

## 9. Ladder update (for library/ladders/PS.md; the lead copies)

| Rung | Statement | Status | Gate |
|---|---|---|---|
| PS7 | Restated: (PS')(beta; eps, l0, L, l1, delta) = tracial functions on a ball with free boundary, small defect in the planar equations without the last term and in the centre equation (C), are eps-close to W_beta at the centre. Linear (PS) is dropped on the weak side | done (unchecked), row 1722 section 4; twin: PROVED in both phases (Theorem U1, Corollary U2) | check by the other provider |
| PS7a | Centre equation: \|sum_{p contains e} Im E tr U_p\| <= 6 tan(pi/N), with sources (Lemma Z); staple alignment inequalities (Lemma Z2) | PROVED by the author, 4D, every beta > 0 | check |
| PS7b | (GPU) of row 1717 and "one tracial solution" are false in the SU(N) twin for beta > 1 without (C) (winding family, Im W_1 != 0) | refuted, PROVED in the twin, exact checks; keep with its counterexample | check; tell row 1720 |
| PS7c | No Lipschitz modulus in a weak phase: atom family, defect (-1)^k k alpha^2, distance of order alpha | PROVED in the twin (signs ARGUED), exact instance alpha = 3/32 | check |
| PS6 = GPU | Replace by (PS'): Lemma I' ((PS') gives (LD), c = delta eps/(64 l1)) and Corollary T' (boundary-independent planar limit, clustering to a floor) | PROVED as implications | check |
| PS8 (new) | (PS'_exact) or (PS') at one weak-side beta by a positivity (bootstrap) certificate on a ball: Gram positivity, relaxed (P), (C), Lemma Z2; dual rational point | open; twin enclosure closes at length 16 (exact tests, guide) | size it; Lean-checked dual |
| PS9 (new) | (RESP): decay of the sourced linear response on the class R_W (no weight outside the spectrum of W_beta); the level of N^2 Cov | stated, open; twin injectivity ARGUED | statement check first |
| PS10 (new) | Action: Wilson outside the metastability window, or mixed action gamma < 0 (Lemma M: planar coupling beta + 2 gamma W(p)) | Lemma M PROVED at equation level; window UNVERIFIED lore | decide after PS8 locates the window |
| PS2, PS4 | Tail lemma and Newton-Kantorovich certificate for linear (PS) | weak side: closed as negative (the statement is false in the twin); strong side: unchanged | |
| PS5 | U(N) twin | changed: (P), (C) do not read the group at leading order; the twin test moves to PS9 (Maxwell form of the sourced (C)) | |

For LD.md: LD4c "(GPU) at an order-one beta" becomes "(PS') at an order-one beta"; Corollary U needs (C) added to its hypothesis. For Theorem T (row 1708): step 3 is withdrawn on the weak side; the proved output is Corollary T'.

RESULT: PS7 done (author only). Linear (PS) is replaced by (PS'): tracial functions on a ball, free boundary, small defect in the planar equations and in a new centre equation (C), are close to W_beta at the centre. PROVED: (C) in 4D from U_e -> e^(2 pi i/N) U_e and Jensen, |sum Im E tr U_p| <= 6 tan(pi/N); (PS') in the twin in both phases; without (C) the SU(N) twin has a curve of exact positive solutions for beta > 1, so (GPU) and Corollary U of row 1717 are false as stated; no Lipschitz modulus in a weak phase. (PS') feeds Lemma I ((LD)) and gives clustering to a floor; Theorem T step 3 fails; a gap needs (RESP), the N^2 Cov level, open. Wilson kept outside the metastability window (UNVERIFIED); fallback mixed action gamma < 0. 4D (PS'): open; route: positivity certificate.
