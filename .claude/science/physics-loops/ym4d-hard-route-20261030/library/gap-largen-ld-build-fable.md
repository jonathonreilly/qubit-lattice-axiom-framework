lead: anthropic/claude-fable-5-2 laptop subagent
Started Sat Nov 28 17:56:53 UTC 2026. Author only, checked by no one.

# Ladder LD build (FINISH row 1717)

## 0. Plan (save protocol; sections are written as the work goes)

1. Read library/ladders/README.md, library/ladders/LD.md, row 1708 sections 6-7, row 1710.
2. LD1: strong coupling, explicit constants, log-Sobolev of order N.
3. LD2: single-cube concentration at speed N^2 given a good boundary.
4. LD3: decoupling of separated cubes.
5. LD4: (LD) at order-one beta; first failing estimate; LD-PS interface lemma.
6. U(N) twin and N = 2.
7. Ladder update. RESULT line.

Inputs read: library/ladders/README.md, library/ladders/LD.md, row 1708 (library/gap-largen-build-fable.md, sections 1-8), row 1710 (library/prior/gap-largen-lit-luna.md, sections 1 and 3). Row 1716 (ladder PS) was not read.

## 1. Verdict first

| Rung | Statement | Status |
|---|---|---|
| LD1 | (LD) for d = 4, SU(N), every N >= 2, \|beta\| < 1/48, explicit constants, centred at the finite-N infinite-volume value W^N_beta | PROVED (section 3). No log-Sobolev citation is used; the proof is a gradient estimate. Centring at W_beta needs convergence W^N -> W, which is CITED as reported, not proved here |
| LD3 | The bound for k separated cubes follows from the bound for one cube, if the one-cube bound is uniform in the boundary condition | PROVED at every beta (Lemma D, section 4). It needs no (PS) |
| LD2 | One-cube concentration at speed N^2 | Split. LD2a (variance of order N^-2 for most small sources) and LD2b (exponential concentration outside at most 4/t exceptional source intervals): PROVED at every beta, every boundary condition, every N (section 5). LD2c (the source 0 is not exceptional): equivalent to (LD); OPEN beyond \|beta\| < 1/48 |
| LD4 | (LD) at order-one beta | NOT PROVED. Reduced: (LD) is equivalent to mean stability under small sources (MS) (Theorem R, PROVED). (MS) follows from a deterministic planar statement (GPU) with N spent by convexity of the pressure only (Lemma I, PROVED as an implication). Qualitative form: uniqueness of the tracial solution of the planar equations on Z^4 gives (LD) for N >= N0 (Corollary U, PROVED as an implication, constants not explicit) |

Highest rung reached with a proof: LD1 (and LD3, LD2a, LD2b at every beta). LD4 is reduced to one deterministic statement, which ladder PS owes.

First failing estimates, by name:
- The convexity proof (LD1) stops at beta = 1/48. The Bakry-Emery lower bound is false for beta > 1/12 (N even; Proposition B, PROVED). Convexity restricted to small plaquettes also fails at large beta (section 6.4, ARGUED).
- At order-one beta the missing estimate is (GPU): approximate tracial solutions of the planar equations in a ball, with free boundary values, are close to W_beta at the centre.

## 2. Setting

Row 1708, section 2. Lattice Z^4 (d is kept in the formulas where it costs nothing). G = SU(N). Lambda is a finite set of links (the integrated links). A boundary condition b gives a fixed value in SU(N) to every other link. The action holds every plaquette that has at least one link in Lambda.

  d mu_{Lambda,b}(U) = Z^-1 exp( S(U) ) prod_{e in Lambda} dU_e ,  S = N beta sum_p Re Tr U_p .

tr = (1/N) Tr. Inner product on su(N): <X,Y> = -Tr(XY), |X|^2 = -Tr(X^2) (Hilbert-Schmidt). T_a is an orthonormal basis. X^e_a f(U) = d/dt f(U_e exp(t T_a)) at t = 0. grad_e f = (X^e_a f)_a. Haar measure is invariant, so E_Haar[X^e_a f] = 0.

Distances. Two links are neighbours (e ~ e') if they are different and lie in one plaquette. Each link has 6(d-1) neighbours and lies in 2(d-1) plaquettes. Two different links lie in at most one common plaquette. dist(e,e') is the graph distance for ~. The sup-norm distance between the point sets of two links is at most dist(e,e'). So a hypothesis "sup-norm distance >= L" gives "dist >= L".
The inner boundary of Lambda is the set bd(Lambda) of links of Lambda that lie in a plaquette with a link outside Lambda.

Loops. A loop l is a closed word in oriented links; n_e(l) is the number of occurrences of e or e^-1; |l| is the length. "l is in a set of links" means all its links are.

Markov property (used often). Let Lambda' be a subset of Lambda. Under mu_{Lambda,b}, the conditional law of the links of Lambda' given all other links is mu_{Lambda',b'}, where b' holds the other links. PROVED: the density is a product of plaquette factors.

Bad cube. As in row 1708: a cube Delta of side L is (eps, l0)-bad with centre function w if some loop l in Delta with |l| <= l0 has |tr U_l - w(l)| > eps. The event depends on the links of Delta only. The number of rooted closed words of length <= l0 in Delta is at most n(L,l0) := 2 (L+1)^4 8^l0.

## 3. Rung LD1: strong coupling, explicit constants. PROVED

### 3.1 Three facts about SU(N)

(F1) sum_{a,b} <[T_a,T_b],T_c> <[T_a,T_b],T_d> = 2N delta_cd.
Proof. The left side is sum_b <[T_c,T_b],[T_d,T_b]> = -Tr(ad_{T_c} ad_{T_d}) by ad-invariance of the inner product. On gl(N), ad_X ad_Y Z = XYZ - XZY - YZX + ZYX, and the traces of the four maps are N Tr(XY), Tr X Tr Y, Tr X Tr Y, N Tr(XY). So Tr(ad_X ad_Y) = 2N Tr(XY) for traceless X, Y, and the identity direction of gl(N) adds 0. So -Tr(ad_{T_c} ad_{T_d}) = -2N Tr(T_c T_d) = 2N delta_cd. QED. (This is Ric = N/2 for this metric. It is the line that reads the group: for U(N) the central direction gives 0, for U(1) everything gives 0.)

(F2) sum_a (X^e_a)^2 commutes with every X^e_b. Reason: it is the Casimir element; sum_a [T_a^2, T_b] = sum_{a,c} c_abc (T_a T_c + T_c T_a) = 0 because c_abc is antisymmetric in (a,c).

(F3) For unitary matrices A, B and X, Y in su(N): |Tr(A X)| <= sqrt(N) |X|, and |Tr(A X B Y)| <= |X| |Y|. (Cauchy-Schwarz for the Hilbert-Schmidt product; a unitary factor keeps the Hilbert-Schmidt norm.)

### 3.2 Second derivatives of the action

For unit vectors x, y in R^(N^2-1), with X = sum x_a T_a, Y = sum y_b T_b:
- e != e' in one common plaquette p: sum_{a,b} x_a y_b X^e_a X^e'_b S = N beta Re Tr( .. X .. Y .. ) up to a sign, so its modulus is at most N |beta| by (F3). If e, e' have no common plaquette it is 0.
- e' = e: sum x_a y_b X^e_a X^e_b S = N beta sum_{p contains e} (+ or -) Re Tr( A_p X Y ) or Re Tr(A_p Y X), with A_p unitary. Modulus at most 2(d-1) N |beta|. (A plaquette holds e once.)
Summed form: for a tangent vector X = (X_e), |Hess S(X,X)| <= N |beta| sum_p ( sum_{e in p} |X_e| )^2 <= 4 N |beta| sum_p sum_{e in p} |X_e|^2 = 8(d-1) N |beta| |X|^2.

### 3.3 The gradient inequality

L = sum_{e in Lambda, a} (X^e_a)^2 + sum_{e,a} (X^e_a S) X^e_a. Then E[f (-L) g] = E[ sum_{e,a} X^e_a f X^e_a g ] for mu = mu_{Lambda,b}. P_t = exp(tL) keeps positivity, P_t 1 = 1, and P_t G -> E[G] uniformly for smooth G (compact connected manifold, elliptic generator; standard).

Let u = P_t G and phi_e = |grad_e u|^2 = sum_a (X^e_a u)^2.

**Lemma 3.1.** (d/dt - L) phi_e <= -N (1 - 10(d-1)|beta|) phi_e + N |beta| sum_{e' ~ e, e' in Lambda} phi_e' . Also (d/dt - L) sum_e phi_e <= -2K sum_e phi_e with K = N (1/2 - 8(d-1)|beta|).
Proof. (d/dt - L) phi_e = 2 sum_a (X^e_a u) [X^e_a, L] u - 2 sum_{a, e', b} (X^e'_b X^e_a u)^2.
Commutator: [X^e_a, sum (X^e'_b)^2] = 0 by (F2) (fields on different links commute). So [X^e_a, L] = sum_{e',b} (X^e_a X^e'_b S) X^e'_b + sum_b (X^e_b S) [X^e_a, X^e_b]. The last part gives 2 sum_{a,b,c} (X_a u)(X_b S) c_abc (X_c u) = 0 by antisymmetry in (a,c).
Square term: keep e' = e only. The matrix M_ba = X^e_b X^e_a u has antisymmetric part (1/2)[X^e_b, X^e_a] u, so sum M_ba^2 >= (1/4) sum_{a,b} ( [X_b,X_a] u )^2 = (1/4) 2N phi_e by (F1). So the square term is at most -N phi_e.
Mixed term, by 3.2: 2 sum_{e'} (..) <= 4(d-1) N |beta| phi_e + 2 N |beta| sum_{e' ~ e} sqrt(phi_e phi_e') <= 10(d-1) N |beta| phi_e + N |beta| sum_{e' ~ e} phi_e'. This is the first claim.
For the sum over e: the mixed terms add to 2 Hess-type form 2 sum_{e,e'} (X^e_a u)(X^e_a X^e'_b S)(X^e'_b u), which is at most 2 * 8(d-1) N |beta| sum phi_e by the summed form of 3.2 (the antisymmetric part of the block e' = e drops out). With -N sum phi_e this is the second claim. QED.

**Lemma 3.2 (gradient decay).** (a) sup |grad P_t G|^2 <= exp(-2Kt) sup |grad G|^2. (b) Let theta >= 0, r_theta = 1 - 10(d-1)|beta| - 6(d-1)|beta| e^theta, and let D_G be the set of links on which G depends, g = max_e sup |grad_e G|. Then sup |grad_e P_t G|^2 <= g^2 exp(-theta dist(e, D_G)) exp(-N r_theta t).
Proof. For a smooth family phi(t): phi(t) = P_t phi(0) + int_0^t P_{t-s} [(d/ds - L) phi(s)] ds. (a) Apply this to exp(2Kt) sum_e phi_e; the bracket is <= 0. (b) Put psi_e = exp(gamma t) phi_e, gamma = N(1 - 10(d-1)|beta|). Then (d/dt - L) psi_e <= N|beta| sum_{e'~e} psi_e', which is >= 0. With abar_e(t) = sup psi_e(t) and v_e = exp(-theta dist(e,D_G)): abar_e(t) <= abar_e(0) + N|beta| int_0^t sum_{e'~e} abar_e'(s) ds. Let A(t) = max_e abar_e(t)/v_e. Because v_e' <= e^theta v_e for neighbours, A(t) <= A(0) + 6(d-1) N |beta| e^theta int_0^t A. Gronwall gives A(t) <= A(0) exp(6(d-1)N|beta|e^theta t), and A(0) <= g^2. QED.

In d = 4: K = N kappa with kappa = 1/2 - 24|beta|; r_theta = 1 - 30|beta| - 18|beta| e^theta; r_0 = 1 - 48|beta| = 2 kappa. Both are positive exactly for |beta| < 1/48. This is the window that row 1710 reports for Shen-Zhu-Zhu (arXiv:2204.12737, Theorem 1.1 and Corollary 1.5, as reported by Luna; not read by me). The equality of the two windows suggests the same convention; I did not check it.

### 3.4 Concentration, covariance, boundary influence

**Proposition 3.3 (concentration; any Lambda, b, N >= 2, |beta| < 1/(16(d-1))).** For real smooth F with sup |grad F|^2 <= ell^2: E exp(lambda (F - E F)) <= exp(lambda^2 ell^2 / (2K)), and mu(F - E F > t) <= exp(-K t^2 / (2 ell^2)).
Proof. d/dt E[exp(lambda P_t F)] = lambda E[exp(lambda P_t F) L P_t F] = -lambda^2 E[exp(lambda P_t F) |grad P_t F|^2] >= -lambda^2 ell^2 exp(-2Kt) E[exp(lambda P_t F)]. Integrate d/dt log E[exp(lambda P_t F)] from 0 to infinity; P_t F -> E F. Then Chernoff with lambda = K t / ell^2. QED.
For F = Re(c tr U_l), |c| = 1: |grad_e F| <= n_e(l)/sqrt(N) by (F3), so ell^2 <= sum_e n_e(l)^2 / N <= |l|^2/N, and

  mu( F - E F > t ) <= exp( - kappa N^2 t^2 / (2 |l|^2) )   (d = 4).

This is speed N^2. The factor N^2 is N (curvature) times N (the 1/N in tr).

**Proposition 3.4 (covariance).** For real smooth F, G and theta with r_theta > 0:
  |Cov(F,G)| <= (2 g / (N r_theta)) sum_e sup|grad_e F| exp(-theta dist(e, D_G)/2).
Proof. Cov(F,G) = int_0^infinity E[ sum_e <grad_e F, grad_e P_t G> ] dt, because d/dt E[F P_t G] = -E[<grad F, grad P_t G>] and P_t G -> E G. Use Lemma 3.2(b) and int_0^infinity exp(-N r_theta t/2) dt = 2/(N r_theta). QED.
Example: Cov(Re tr U_l, Re tr U_l') is at most 2 |l| |l'| N^-2 r_theta^-1 exp(-theta dist(l,l')/2). So the truncated two-loop function is of order N^-2 and decays exponentially, uniformly in N, volume and boundary condition.

**Proposition 3.5 (boundary influence).** Let b, b' be two boundary conditions on the same Lambda, l a loop in Lambda, D = dist(l, bd(Lambda)). Then
  | E_{Lambda,b} tr U_l - E_{Lambda,b'} tr U_l | <= C_beta |l| exp(-theta D / 2),  C_beta = 48 pi (d-1) |beta| / r_theta  ( = 144 pi |beta| / r_theta in d = 4).
Proof. Each V in SU(N) is exp(Y) with Y in su(N) and operator norm at most 2 pi (take angles in (-pi, pi], then shift by 2 pi as many angles as needed to make the sum 0); so |Y| <= 2 pi sqrt(N). Join b to b' by b_s(e') = b(e') exp(s Y_e'), s in [0,1]. Then d/ds E_{b_s}[F] = Cov_{b_s}(F, G_s), G_s = d/ds S. G_s depends on the links of bd(Lambda) only, and by (F3) |grad_e G_s| <= N|beta| * 2(d-1) * 3 * 2 pi sqrt(N). So g <= 12 pi (d-1) |beta| N^(3/2). Proposition 3.4 with F = Re tr U_l or Im tr U_l gives 24 pi (d-1)|beta| r_theta^-1 |l| exp(-theta D/2) for each part; add the two parts. QED.

**Corollary 3.6.** For |beta| < 1/48 and every N >= 2 the limit W^N_beta(l) = lim E_{Lambda,b} tr U_l exists as Lambda grows to all links, does not depend on b, is translation invariant, and |E_{Lambda,b} tr U_l - W^N_beta(l)| <= C_beta |l| exp(-theta dist(l, bd(Lambda))/2).
Proof. For Lambda inside Lambda', E_{Lambda',b'} tr U_l is an average of E_{Lambda,b''} tr U_l (Markov property). So all values with dist >= D lie in one disc of radius C_beta |l| exp(-theta D/2). QED.

### 3.5 Theorem LD1

**Theorem LD1 (PROVED).** d = 4, G = SU(N), N >= 2, |beta| < 1/48, kappa = 1/2 - 24|beta|, theta > 0 with r_theta = 1 - 30|beta| - 18|beta|e^theta > 0, C_beta = 144 pi |beta| / r_theta. Let eps in (0,1], l0 >= 1 and

  L >= 1 + (2/theta) log( 2 C_beta l0 / eps ).

Then for every finite Lambda, every boundary condition, and all cubes Delta_1..Delta_k of side L in Lambda with mutual sup-norm distances and distances to the links outside Lambda at least L:

  mu_{Lambda,b}( all Delta_i are (eps,l0)-bad with centre W^N_beta ) <= [ 4 n(L,l0) exp( - kappa N^2 eps^2 / (16 l0^2) ) ]^k .

So (LD)(beta; eps, l0, L, c) holds with c = kappa eps^2 / (32 l0^2) for N^2 >= 32 l0^2 log(4 n(L,l0)) / (kappa eps^2), with centre W^N_beta.
Proof. One cube, any region Gamma that contains every link at sup-norm distance < L from Delta, any boundary condition: dist(l, bd(Gamma)) >= L - 1 for l in Delta, so |E tr U_l - W^N_beta(l)| <= eps/2 by Corollary 3.6 and the choice of L. If |tr U_l - W^N_beta(l)| > eps then |tr U_l - E tr U_l| > eps/2, so one of the four functions +-Re, +-Im of tr U_l exceeds its mean by eps/(2 sqrt 2). Proposition 3.3 gives exp(-kappa N^2 eps^2/(16 |l|^2)) for each. Sum over the loops. Then Lemma D (section 4). QED.

Centre W_beta. If W^N_beta(l) -> W_beta(l) as N -> infinity for |l| <= l0 (this convergence is CITED in kind: Jafarov, arXiv:1610.03821, Theorem 1.1, in "a sufficiently small strong-coupling region", as reported by Luna; I did not read it and I do not know that its region contains 1/48), then (LD) holds with centre W_beta and 2 eps for N large. Proposition 3.4 gives factorisation, so every limit point of W^N_beta solves the planar equation of row 1708 exactly; uniqueness of that solution is the missing step for a proof here. NOT PROVED here.

Remarks.
- The ladder file says "from a log-Sobolev inequality". None is used. The inequality itself (constant 2/K) follows from Lemma 3.1 by the Bakry-Emery theorem (CITED by name only; I do not give a theorem number).
- Twin test. U(N): (F1) gives 0 in the central direction, the proof fails at that line. U(1): fails at the same line. At strong coupling U(1) and U(N) have a gap too (Nissim, arXiv:2510.22788, Theorem 1.1, as reported by Luna), so here the failure is a property of the method, not of the statement.
- N = 2: every statement of this section holds, with the same constants. Corollary 3.6 and Proposition 3.4 give uniqueness and exponential clustering for SU(2) at |beta| < 1/48 (known: Shen-Zhu-Zhu as reported). The (LD) bound is true and empty: with N^2 = 4 the right side exceeds 1 for all eps <= 1, l0 >= 1.

## 4. Rung LD3: separated cubes. PROVED at every beta

For a cube Delta of side L let Delta^+ be the set of links with a point at sup-norm distance < L from Delta.

**(SC)(beta, N; eps, l0, L, p), single-cube bound.** For every cube Delta of side L and every boundary condition b on Delta^+: mu_{Delta^+,b}(Delta is (eps,l0)-bad) <= p.

**Lemma D (PROVED).** (SC) with p gives: for every finite Lambda, every b, and cubes Delta_1..Delta_k of side L with mutual distances and distances to the outside of Lambda at least L, mu_{Lambda,b}(all bad) <= p^k. Conversely the case k = 1 of this bound, with Lambda = Delta^+, is (SC).
Proof. Delta_k^+ is inside Lambda. The links of Delta_j, j < k, are outside Delta_k^+. Condition on all links outside Delta_k^+. By the Markov property the conditional law is mu_{Delta_k^+, b'}. So mu(B_1 .. B_k) = E[ 1_{B_1..B_{k-1}} mu_{Delta_k^+,b'}(B_k) ] <= p mu(B_1 .. B_{k-1}). Induction. QED.

Meaning. With "uniformly in the boundary condition" in the target, decoupling is free. It uses no decay and no (PS). The whole content of (LD) is the one-cube bound for the worst boundary condition at distance L. The ladder's present LD3 ("decoupling ... using (PS) at rate m") is this lemma plus the mean statement of section 6; (PS) enters the mean, not the decoupling.
If the one-cube bound is known only for a class of good boundary conditions, Lemma D fails at the conditioning step: the conditional boundary condition b' must be good, and that is an (LD)-type event on the shell. I do not follow that route; section 6 keeps the boundary free.

## 5. Rung LD2: what convexity of the pressure gives at every beta. PROVED

Fix N, beta (any real value), Lambda, b. Let F_1..F_M be real functions of the configuration with |F_j| <= 1. For J in R^M put

  mu_J = Z_J^-1 exp( N^2 J.F ) mu_{Lambda,b} ,  P(J) = N^-2 log E_{Lambda,b} exp( N^2 J.F ).

P is smooth and convex, d_j P = E_J F_j in [-1,1], d_j^2 P = N^2 Var_J(F_j), |P(J) - P(J')| <= |J - J'|_1. With F_j = Re tr U_l or Im tr U_l, mu_J is a Wilson-type law with the extra action N J_j Re(c Tr U_l). All statements below are uniform in beta, Lambda, b.

**Lemma F (LD2a: variance of order N^-2 for most sources).** For every J* and lambda_1 > 0, with Q = J* + [0,lambda_1]^M: the mean over J in Q of sum_j Var_J(F_j) is at most 2M/(lambda_1 N^2). So at least half of Q (Lebesgue) has sum_j Var_J(F_j) <= 4M/(lambda_1 N^2).
Proof. int_0^{lambda_1} N^2 Var_J(F_j) dJ_j = d_j P(end) - d_j P(start) <= 2. Integrate the other coordinates, sum on j, then Markov. QED.

**Lemma E (LD2b: exponential concentration off exceptional intervals).** For J, j, lambda > 0, t > 0, with omega = d_j P(J + lambda e_j) - d_j P(J) >= 0:
  mu_J( F_j - E_J F_j > t ) <= exp( - N^2 lambda (t - omega) ).
On a line J + s e_j, cut s into intervals of length lambda. At most 4/t of them have omega >= t/2. On every other interval, mu_J(F_j - E_J F_j > t) <= exp(-N^2 lambda t/2) at its left end point.
Proof. E_J exp(lambda N^2 (F_j - E_J F_j)) = exp( N^2 [P(J+lambda e_j) - P(J) - lambda d_j P(J)] ) <= exp(N^2 lambda omega), by convexity. Chernoff. The increments omega over disjoint intervals add to at most 2. QED.

Meaning. In a finite volume with any boundary condition, concentration at speed N^2 of one loop can fail at a source value only if the mean of that loop jumps by a fixed amount when the source moves by lambda. That is a first-order transition in the source, at scale lambda. There are at most 4/t such places on a line. The open rung is to show that the source 0 is not one of them, uniformly in N, volume and boundary condition:

**LD2c (OPEN beyond |beta| < 1/48).** For the given beta there is lambda_0 > 0 with d_j P(lambda_0 e_j) - d_j P(0) <= t/2 for all N >= N1, all cubes, all boundary conditions at distance L.

**Lemma C (convexity transfer).** For lambda, s > 0 and every J' in (lambda + s) e_j + [0,lambda_1]^M: d_j P(lambda e_j) <= d_j P(J') + 2 M lambda_1 / s.
Proof. J'' = J' - s e_j lies in lambda e_j + [0,lambda_1]^M. Then d_j P(lambda e_j) <= [P((lambda+s) e_j) - P(lambda e_j)]/s <= [P(J') - P(J'') + 2 M lambda_1]/s <= d_j P(J') + 2M lambda_1/s. The first and last steps are convexity on a line in direction e_j; the middle step is the Lipschitz bound. QED.

## 6. Rung LD4: (LD) at order-one beta

### 6.1 Theorem R: (LD) is a statement about means

**(MS)(beta; eps, l0, L, lambda_0, N1), mean stability under one small source.** For all N >= N1, every cube Delta of side L, every b on Delta^+, every loop l in Delta with |l| <= l0, every c in {1, -1, i, -i} and every lambda in [0, lambda_0]:

  E_{Delta^+, b; lambda} [ Re( c (tr U_l - W_beta(l)) ) ] <= eps ,

where the law has the extra factor exp( lambda N^2 Re(c tr U_l) ).

**Theorem R (PROVED, every beta, every N).**
(a) (MS)(beta; eps, l0, L, lambda_0, N1) gives (SC)(beta, N; 2 sqrt(2) eps, l0, L, p) with p = 4 n(L,l0) exp(-lambda_0 eps N^2) for N >= N1. With Lemma D: (LD)(beta; 2 sqrt 2 eps, l0, L, c) with c = lambda_0 eps/2 for N^2 >= max(N1^2, 2 log(4 n(L,l0))/(lambda_0 eps)).
(b) (SC)(beta, N; eps, l0, L, exp(-c N^2)) for N >= N1 gives (MS)(beta; eps + 2 exp(-c N1^2/2), l0, L, c/4, N1).
Proof. (a) With F = Re(c tr U_l) and w = Re(c W_beta(l)): log E exp(lambda_0 N^2 (F - w)) = N^2 int_0^{lambda_0} (E_s F - w) ds <= N^2 lambda_0 eps. So mu(F - w > 2 eps) <= exp(-lambda_0 eps N^2). If |tr U_l - W_beta(l)| > 2 sqrt 2 eps, one of the four choices of c has F - w > 2 eps. Sum over loops. (b) The density of the tilted law against mu is at most exp(2 lambda N^2). So the tilted probability of "bad" is at most exp(-(c - 2 lambda)N^2) <= exp(-c N^2/2) for lambda <= c/4. Off the bad event |tr U_l - W_beta(l)| <= eps; on it the modulus is at most 2. QED.

So (LD) at any beta is equivalent, with explicit changes of constants, to a first-moment statement: a source of size lambda_0 N^2 on one short loop in a cube moves the mean of that loop by at most eps from W_beta, for the worst boundary condition at distance L. No second moment and no probability is left in (MS). This is where the two ladders meet.

### 6.2 The interface with ladder PS

Notation. cl(Delta^+) is Delta^+ together with the links of the plaquettes that meet Delta^+. F^e_beta is the planar map of row 1708, section 7. A function w on the loops in cl(Delta^+) is of tracial type if w(l) = tau(u_l) for unitaries u_e, u_{e^-1} = u_e^*, in a von Neumann algebra with a normal tracial state tau. Every w(l) = E tr U_l of a law on SU(N)^Lambda with fixed boundary links is of tracial type (algebra L^infinity(mu) tensor M_N, tau = E tr).

**(GPU)(beta; eps, l0, L, l1, delta), planar uniqueness in a ball with free boundary.** l1 >= l0. For every cube Delta of side L and every w of tracial type on the loops in cl(Delta^+): if

  | w(l) - F^e_beta(w)(l) | <= delta  for every loop l in cl(Delta^+) with |l| <= l1 - 4 whose plaquette deformations at e stay in cl(Delta^+), and every link e of l that lies in Delta^+,

then |w(l) - W_beta(l)| <= eps for every loop l in Delta with |l| <= l0.

**Lemma I (the LD-PS interface; PROVED as an implication, every beta).** Assume (GPU)(beta; eps, l0, L, l1, delta) with eps, delta <= 1. Let M = 8 (3L+3)^4 8^l1. Then for all N with

  N^2 >= N_I^2 := (2/delta) [ l1 + 192 M^2 l1 (l1 + 6|beta|) / (delta eps) ]

(SC)(beta, N; 3 sqrt(2) eps, l0, L, p) holds with p = 4 n(L,l0) exp( - delta eps N^2 / (8 l1) ). So (LD)(beta; 3 sqrt 2 eps, l0, L, c) holds with c = delta eps / (16 l1) for N^2 >= max( N_I^2, 16 l1 log(4 n(L,l0)) / (delta eps) ).

Proof. Fix Delta, b on Delta^+, N >= N_I. Let F_1..F_M be the functions +-Re tr U_l, +-Im tr U_l for all rooted closed words l in cl(Delta^+) with |l| <= l1 (their number is at most M). Use section 5 with Lambda = Delta^+. Put lambda = delta/(12 l1), lambda_1 = lambda eps/(4M).
Step 1, sourced loop equation. Under mu_J the proof of Lemma 1 of row 1708 applies with the action S + N sum_j J_j Re(c_j Tr U_{l_j}). The new term has the form of the plaquette terms with p replaced by l_j rotated to each occurrence of e. For a single loop l and a link e of l in Delta^+, after division by n_e(l), the source terms have absolute sum at most 2 eta_e(J), eta_e(J) = sum_j |J_j| n_e(l_j), because every loop function has modulus at most 1. (PROVED by the computation of Lemma 1; I rely on row 1708 for Lemma 1 itself.)
Step 2, defect. With w_J(l) = E_J tr U_l and v = max over the listed loops of E_J |tr U_l - w_J(l)|^2, equation (SD) for the one-loop sequence gives
  | w_J(l) - F^e_beta(w_J)(l) | <= |l| N^-2 + (|l| + 6|beta|) v + 2 eta_e(J)  for |l| <= l1 - 4,
because the split and last terms of (SD) differ from their factorised forms by covariances of two listed loops (|Cov| <= v), with at most n_e - 1 and 6|beta| after division, and the t_e^2 term is at most n_e/N^2.
Step 3, a good source. Fix j with l_j in Delta, |l_j| <= l0. Let Q' = 2 lambda e_j + [0,lambda_1]^M. By Lemma F there is J' in Q' with v <= 4M/(lambda_1 N^2) = 16 M^2/(lambda eps N^2). For it eta_e(J') <= 2 lambda l1 + lambda_1 M l1 <= 3 lambda l1 = delta/4. With N >= N_I the defect of w_J' is at most delta/2 + delta/2. w_J' is of tracial type. (GPU) gives d_j P(J') = E_J' F_j <= W_j + eps, where W_j is the matching part of W_beta(l_j).
Step 4. Lemma C with s = lambda: d_j P(lambda e_j) <= W_j + eps + 2M lambda_1/lambda = W_j + 3 eps/2. Then log E exp(lambda N^2 (F_j - W_j)) = N^2 int_0^lambda (d_j P(s e_j) - W_j) ds <= (3/2) eps lambda N^2 (d_j P is nondecreasing in s). So mu_{Delta^+,b}(F_j - W_j > 3 eps) <= exp(-(3/2) eps lambda N^2) = exp(-delta eps N^2/(8 l1)). Sum over the four parts and the loops. Lemma D gives (LD). QED.

Where N is spent: Lemma F only. N^2 must exceed the square of the number M of loop observables in the conditioning region, divided by delta^2 eps. So N0 is of order L^4 8^l1 / (delta sqrt eps). This is larger than the guess N0^2 = C L^4 l0 / c of row 1708, section 7.

**Corollary U (qualitative LD4; PROVED as an implication).** Suppose that at beta the planar equations w = F^e_beta(w), for all loops l on Z^4 and all links e of l, have exactly one solution of tracial type, W_beta. (No translation invariance is assumed of w.) Then for every eps and l0 there are L, c, N0 with (LD)(beta; eps, l0, L, c) for all N >= N0.
Proof. If (GPU)(beta; eps, l0, L, l1, delta) fails for every (L, l1, delta), take L, l1 -> infinity, delta -> 0 with counterexamples w_n, translated so that the loop where |w_n - W_beta| > eps starts at the origin (W_beta is translation invariant, and the loop is at distance >= L_n from the outside). Tracial states on the group algebra of the free group on the links of Z^4 form a weak-* compact set. A limit point w is of tracial type, satisfies every planar equation exactly (each equation has finitely many terms), and differs from W_beta on one of finitely many loops. Contradiction. So (GPU) holds for some finite (L, l1, delta), and Lemma I applies. QED.
The constants L, c, N0 are not explicit. Explicit constants need a quantitative (GPU).

**What ladder PS owes ladder LD.** Exactly (GPU). (PS) of row 1708 is the linear, infinite-volume form: a bounded inverse of 1 - DF_beta(W_beta) in a weighted norm. (GPU) needs three things more:
1. Global: a function of tracial type with small defect and arbitrary boundary values is in the basin of W_beta at the centre. This is the statement that no boundary condition can hold another planar state over the distance L. It is false at a planar first-order transition for every L (two solutions), and near one L must exceed the critical droplet size. It is not a linear statement. Corollary U gives it from exact uniqueness, without constants.
2. Local and quantitative (ARGUED, not proved): inside the basin, (PS)(beta; m, a, kappa) should give |w - W_beta| <= C kappa (delta + a^(l0 - l1) + e^(-mL)) on short loops at the centre. This is the place for L of order (1/m) log(1/eps) and l1 of order l0 + log(1/eps)/log a. The quadratic remainder of the split term is compatible with the length weight (a^|l1| a^|l2| = a^|l|) and has row sum at most n_e - 1 <= l1, so a Newton step needs ||w - W|| <= 1/(2 kappa l1). The radial weight e^(m r) is not multiplicative; I did not check that step.
3. Truncation: the defect is controlled only for |l| <= l1 - 4, with values of modulus <= 1 at larger lengths. The weight a > 1 of (PS) is what must absorb them. This is the tail problem that row 1708 names for the Newton-Kantorovich route.

In the other direction, ladder LD gives ladder PS: Lemma F. Any use of the loop equations at order-one beta may assume factorisation with error 4M/(lambda_1 N^2), in any volume, with any boundary condition, at the price of sources of size lambda_1 on M loops. No estimate on the measure is needed for it.

### 6.3 Why the proof of LD1 does not continue: Proposition B. PROVED

**Proposition B.** Let N be even, d >= 3, beta > 1/(4(d-1)) (beta > 1/12 in d = 4). Then there are a finite Lambda, a boundary condition, a configuration U and a tangent vector X with Ric(X,X) - Hess S(X,X) < 0. So the Bakry-Emery lower bound with a positive constant fails for the Wilson law at these beta.
Proof. The 2-cochain with value -1 on every plaquette is closed mod 2 (each cube has six faces). Z^d is contractible, so there is sigma_e in {1,-1} with product -1 around every plaquette. Put U_e = sigma_e times the identity (in SU(N) for N even), and let X be supported on one link e. Then Hess S(X,X) = N beta sum_{p contains e} Re Tr(U_p X_e^2) = 2(d-1) N beta |X_e|^2, and Ric(X,X) = (N/2)|X_e|^2. QED.
Between 1/48 and 1/12 the criterion is undecided here. A uniform log-Sobolev inequality by another proof is not excluded by Proposition B, but it gives uniqueness of the infinite-volume state, so it cannot hold through a bulk transition.

### 6.4 Restricted convexity fails on the weak side. ARGUED

Write U_p(t) = U_p exp(tZ_1)..exp(tZ_4) with Z_i the transported +-X_i. Then d^2/dt^2 Re Tr U_p(t) = Re Tr(U_p Z^2) + Re Tr((U_p - 1) C), Z = sum Z_i, C = sum_{i<j} [Z_i, Z_j] (PROVED: Tr C = 0). The first term is at most -lambda_min(Re U_p)|Z|^2. The second has modulus at most ||U_p - 1||_op * 2 sum_{i<j}|X_i||X_j|. So on the set where every plaquette has ||U_p - 1||_op <= eta <= sqrt 2: Ric - Hess S >= N (1/2 - 6(d-1) beta eta) (PROVED for beta > 0). In d = 4 this needs beta eta < 1/36. The typical plaquette angle at large beta is of order beta^(-1/2) (GUESSED, from the Gaussian approximation), so beta eta grows like sqrt(beta). The commutator term N beta <F, [a,a]> is the lattice form of the indefinite term of the Yang-Mills Hessian at a non-flat connection. Also one outlier eigenvalue of U_p costs exp(-cN), not exp(-cN^2), and breaks the operator-norm condition. So convexity is not the mechanism on the weak side. This route is closed here.

### 6.5 Statement of the first failing estimate

At order-one beta everything that uses the measure is done by Lemma D, Lemma F, Lemma C and Theorem R. What fails is deterministic: (GPU), or its qualitative form, uniqueness of the tracial solution of the planar equations with no boundary or invariance assumption. I have no proof of it at any beta. At |beta| < 1/48, Theorem LD1 with Theorem R(b) gives (MS), the form of (GPU) restricted to Wilson laws with one small source, if the centre is W^N_beta; so the Wilson-law form is not empty there.

## 7. The U(N) twin and N = 2

U(N).
- Lemma D, Lemma F, Lemma E, Lemma C, Theorem R, Lemma I and Corollary U hold word for word for U(N) (PROVED: they use |tr| <= 1, the Markov property and Lemma 1 in its U(N) form). In (GPU) the map F^e_beta loses its last term. So the reduction does not read the group. The twin test falls on (GPU): a proof of (GPU) at weak coupling must use the last term of (SD).
- LD1's proof reads the group at (F1) and fails for U(N).
- Weak coupling (ARGUED). Write U = e^(i phi) V. A boundary condition with an abelian field strength of size eps' per plaquette costs nothing (it is a boundary condition). To screen it the bulk needs det-monopoles at density N eps'/(2 pi) per plaquette. Where the plaquette eigenvalue density has a gap (weak side), one eigenvalue winding costs of order N beta, so screening costs N^2 beta eps' against a field energy N^2 beta eps'^2: no screening for small eps'. Then the mean of tr U_p at the centre is turned by the phase eps' for every L. So (MS) fails, and by Theorem R (b) so does (LD) in its form uniform in the boundary condition. By Lemma I the U(N) form of (GPU) fails, and by Corollary U the U(N) planar equations then have more than one tracial solution at such beta (states with a constant abelian flux; GUESSED form, not constructed).
- Strong coupling: not decided here. Row 1710 reports Nissim's Theorem 1.5 (concentration and factorisation for U(N), small beta) with constants that depend on N. I do not know that it gives a bound uniform in N and in the boundary condition.

N = 2.
- Section 3 holds in full (uniqueness and clustering for |beta| < 1/48); the (LD) bound is true and empty.
- Sections 4 and 5 hold. Lemma I needs N^2 >= N_I^2 > 384 M^2, so it never applies. Theorem R holds but (MS) with lambda_0 N^2 = 4 lambda_0 is a tilt of order one, and tr U_l has a law of order-one width at every beta > 0: there is no master field and (LD) with small eps is false for SU(2) (ARGUED: at finite beta and N = 2 the law of tr U_l given the other links has a density that is positive on an interval).
- Nothing in this ladder is a step toward (PUR-io). The only transferable tool is Lemma E: in any finite-N Wilson law, a failure of exponential concentration of a bounded observable at source J is a jump of its mean in the source. At N = 2 the speed is the constant 4, so it gives no small number.

## 8. Checks done and not done

- No statement here was checked by another reader or by a machine. The planned exact check of (F1) for N = 2, 3 was not run (sympy is not installed; I did not write a fractions version). (F1) is proved by hand in 3.1.
- Lemma 1 of row 1708 is used as given. The sourced form (Lemma I, step 1) uses only the count of terms and |phi| <= 1, not the signs.
- Conventions of Shen-Zhu-Zhu, Jafarov and Nissim were not matched; all three are cited as Luna reports them.
- Not checked: that P_t G is smooth enough for the Duhamel formula of Lemma 3.2 when G is smooth (standard for an elliptic generator with smooth coefficients on a compact manifold).

## 9. Ladder update (for library/ladders/LD.md; the lead copies)

| Rung | Statement | Status | Gate |
|---|---|---|---|
| LD1 | (LD) for SU(N), d = 4, N >= 2, \|beta\| < 1/48, c = kappa eps^2/(32 l0^2), kappa = 1/2 - 24\|beta\|, L >= 1 + (2/theta) log(2 C_beta l0/eps), centre W^N_beta | PROVED by the author, row 1717 section 3; gradient estimate, no log-Sobolev citation | check by the other provider |
| LD1b | W^N_beta -> W_beta for \|beta\| < 1/48 (uniqueness of the planar solution at small beta) | open; CITED in kind only | proof by hand or exact reference |
| LD3 | k cubes from one cube when the one-cube bound is uniform in the boundary condition (Lemma D) | PROVED by the author, every beta; needs no (PS) | check |
| LD2a | Variance <= 4M/(lambda_1 N^2) for at least half of the sources in any box of side lambda_1 (Lemma F) | PROVED by the author, every beta | check |
| LD2b | Exponential concentration at speed N^2 off at most 4/t source intervals (Lemma E) | PROVED by the author, every beta | check |
| LD4a | (LD) <=> (MS), mean stability under one small source (Theorem R) | PROVED by the author, every beta | check |
| LD4b | (GPU) => (LD) with c = delta eps/(16 l1), N0 of order L^4 8^l1/(delta sqrt eps) (Lemma I); uniqueness of the tracial planar solution => (LD) without explicit constants (Corollary U) | PROVED by the author as implications | check |
| LD4c | (GPU) at an order-one beta | open; owed by ladder PS; fails at a planar first-order transition; U(N) twin expected to fail at weak coupling | joint with PS |
| closed | Bakry-Emery convexity beyond beta = 1/12 (Proposition B), and convexity restricted to small plaquettes at large beta (6.4) | refuted (B: PROVED, N even) / ARGUED (6.4) | keep as negative |

Changes to the present file: the old LD2 ("given a good boundary") is replaced by LD2a, LD2b and LD4a-c, because the boundary is kept free. The old LD3 no longer uses (PS). The interface to PS.md is the single statement (GPU) of section 6.2; PS.md should carry a rung "(GPU) from (PS) plus global uniqueness" with the three items of 6.2.

RESULT: LD1 PROVED (author only): (LD) for SU(N), N>=2, |beta|<1/48, c = (1/2-24|beta|) eps^2/(32 l0^2), centre W^N_beta; centre W_beta needs cited convergence. LD3 PROVED at every beta (Markov; no PS). LD2 split: variance N^-2 for most sources and concentration off <=4/t source intervals PROVED at every beta. LD4 not proved; highest proved rung LD1. Reduction PROVED: (LD) <=> mean stability under one small source; interface Lemma I: (GPU) (tracial functions with planar defect <= delta in a ball, free boundary, are eps-close to W_beta at the centre) => (LD), c = delta eps/(16 l1), N0 ~ L^4 8^l1; exact tracial uniqueness => (LD) non-quantitatively. Bakry-Emery fails for beta>1/12. U(N): reductions hold verbatim, LD1 proof fails, (LD) argued false at weak coupling. N=2: LD1 true but empty; no master field.
