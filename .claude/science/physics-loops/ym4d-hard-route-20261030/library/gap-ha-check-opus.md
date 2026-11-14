# Check of library/gap-ha-astra.md (FINISH row 874)

- Checker: Claude Opus 5.5 (high effort), by hand, no subagents, no computation.
- Clone: /Users/jonreilly/ym4d-lead/clone at commit dd5c4ff8affc6901bc622f86c1d34d08dc74fafa.
- Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
- Checked file: D/library/gap-ha-astra.md (row 871, OpenAI Codex gpt-6-astra, max effort).
- Background: D/library/gap-z2parity-astra.md (row 866), D/library/gap-z2parity-check-opus.md (row 870).

## Verdicts (appended one per statement)

Line references "H:n" are to gap-ha-astra.md at the clone commit above. Row 866 = Z, row 870 = Z-check. Every arithmetic step was redone by hand.

## S1. Strict loss of complex information on the real segment (H:171-205, (R0); H:267-311, (R4)-(R5) and the Rouche zeros) — HOLDS (scope as the note states)

(R0), checked line by line.
1. tau_* = tanh(5/2) >= tanh(beta) >= |t_p| for beta in I. R = (1 + 1/tau_*)/2 > 1 and R tau_* = (1 + tau_*)/2 < 1. So M_R is finite.
2. For real |lambda| <= R, each factor 1 + lambda eta t_p lies in [1 - R tau_*, 1 + R tau_*]. nu_ce is a probability. So Z_k(lambda) is between (1 - R tau_*)^N and (1 + R tau_*)^N, and |F| <= N log((1+R tau_*)/(1-R tau_*)) = N M_R. Correct, also for lambda < 0.
3. On the real segment the real logarithm agrees with any holomorphic extension of the germ (identity theorem on the connected set disc cap neighbourhood of the segment). So the real-segment restriction of HA, with r = R and B = M_R, is a theorem.
4. Insufficiency. Z_2 at beta = 5/2 has |t_p| = tanh(5/2) = tau_*, so (R0) holds for it verbatim. Its area-order zero is Z-check S7 item 1. Its q tends to 1/2 (Z-check S5 item 7). So (R0) plus the area-order zero cannot imply (E17). Correct.
5. Single-stack bound. Choose the representative cocycle of v_{1i}: the (1,i)-plaquettes at one (x_1, x_i), over all (x_2, x_j): K_v = L_2 L_j = a L_j <= 2a^2 faces. Z_k depends only on the class (link flip U_l -> -U_l preserves nu_ce and changes eta by a coboundary). The two integrands differ on K_v factors; each ratio (1+x)/(1-x), |x| <= R tau_*, lies in [e^(-M_R), e^(M_R)]. So |F| <= K_v M_R. Correct. Z_2 at 5/2 has F(1) >= log((1 - eps_a)/eps_a), of order a^2, consistent with this bound. So an area-size bound does not force smallness. Correct.

(R4)-(R5), checked line by line.
6. P_a, Q_a equal 1 at 0; Q_a >= 1 - eps > 0 on [0,1]. P_a - Q_a = 2 eps lambda^A has order A.
7. log(P/Q) = log((1+x)/(1-x)), x = eps lambda^A/(1+lambda^6). d x/d lambda has numerator eps lambda^(A-1)[A(1+lambda^6) - 6 lambda^6] = eps lambda^(A-1)[A + (A-6) lambda^6] >= 0 since A >= 9. So the derivative of log(P/Q) is >= 0, and the integral of its modulus is its value at 1: log((2+eps)/(2-eps)). With x = eps/2 <= 1/2: integral of 2/(1-t^2) over [0,x] <= 2x/(1 - x^2) <= 8x/3 = 4 eps/3. Correct. So (R) holds for this pair with p_R = 0.
8. Endpoint fraction (1 - Q(1)/P(1))/2 = eps/(2+eps) >= eps/3 = e^(-ga)/3. Correct.
9. Zeros. zeta = e^(i pi/6) is a simple root of 1 + lambda^6. On |lambda - zeta| = delta, 1 + lambda^6 = 6 zeta^5 h + sum_{k>=2} C(6,k) zeta^(6-k) h^k with |h| = delta. The tail is at most delta^2(15 + 20 delta + 15 delta^2 + 6 delta^3 + delta^4) <= 16.1 delta^2 <= 57 delta^2 for delta <= 1/20. 6 delta - 57 delta^2 > 3 delta iff delta < 3/57; 1/20 < 3/57. And |eps lambda^A| <= eps (1+delta)^A <= eps e^(A delta) <= e delta^2 < 3 delta. delta = e^(-ga/2), so delta <= 1/20 and A delta = a^2 e^(-ga/2) <= 1 for large a. Adjacent roots of 1 + lambda^6 are at distance 2 sin(pi/6) = 1. Rouche gives exactly one zero of each of P_a, Q_a in the delta-disc. P_a - Q_a vanishes only at 0, so the zeros differ. The zero of P_a has modulus <= 1 + delta < r for large a, Q_a is nonzero there, and log(P_a/Q_a) is unbounded near it. So no holomorphic extension with any bound exists on any fixed |lambda| < r, r > 1. Correct.

Precision (no correction to the mathematics). Item 8 refutes HA for the pair only when HA's size factor N is read as polynomial in a (for example the degree A, or 24a^4); item 9 refutes it outright. The note's conclusion "(R) does not force HA" is therefore proved by item 9 alone. Both facts concern auxiliary polynomials with no closure, twist or link structure. They establish the strict loss for the class of normalized pairs with an area-order difference, not within the Wilson SU(2) family. The note says this at H:310-311 and H:682-684.

HA implies (R), (R3), checked. With s = (1+r)/2, d = s - 1, the circle of radius d about lambda in [0,1] lies in |z| <= s. Schwarz gives |F| <= BN (s/r)^A = BN e^(-cA) there. Cauchy gives |F'(lambda)| <= BN e^(-cA)/d. With N <= 24 a^4, A >= a^2 and max_a(-c a^2 + g a) = g^2/(4c): (R3) follows. Correct. (R) implies (E17): F(0) = 0, F(1) >= 0 (Z-check S3 item 2), F(1) = integral of R <= integral of |R|, q = (1 - e^(-F(1)))/2 <= F(1)/2. Correct.

## S2. The interpolating measures mu_(k,lambda) and the response (R1) (H:207-222) — HOLDS

1. Density. For 0 <= lambda <= 1 and |t_p| <= tanh(beta) < 1, every factor 1 + lambda eta_{k,p} t_p is >= 1 - tanh(beta) > 0. So the density prod_p(1 + lambda eta t_p)/Z_k(lambda) is positive and bounded, and has nu_ce-mean 1. mu_{k,lambda} is a probability measure. Correct.
2. Score. S_{k,lambda} = sum_p eta t_p/(1 + lambda eta t_p) = d/d lambda log prod_p(1 + lambda eta t_p), pointwise. It is bounded (|S| <= N tanh(beta)/(1 - lambda tanh(beta))). Correct.
3. Identity. Z_k'(lambda) = E_nu[prod_p(...) S_{k,lambda}], so (log Z_k)' = E_{mu_{k,lambda}} S_{k,lambda}. Then R_{m,v} = (log Z_m)' - (log Z_{m+v})'. Each expectation uses its own measure mu_{m,lambda} or mu_{m+v,lambda} with its own normalizer Z_k(lambda). Correct.
4. eta_{m+v,p} = eta_{m,p} (-1)^(v_p) for a chosen representative cocycle; R does not depend on the representatives, since Z_k(lambda) does not (link-flip argument, S1 item 5).
5. The claims at H:232-235 (no absolute value inside either integral or the plaquette sum; contractible decorations kept with signs; actual normalizers) are accurate descriptions of (R1).

Remark. (R1) is defined on the whole real interval 0 <= lambda < 1/tanh(beta), not only on [0,1]. Nothing further is claimed.

## S3. The derivative identity (R2) (H:224-230) — HOLDS

1. Z_k(lambda) is a polynomial in lambda of degree <= N (finite expansion of the product). It is positive on [0,1] (S2 item 1). So log Z_k is real-analytic on a neighbourhood of [0,1]; no interchange-of-limits issue arises (the "differentiate under the integral" step is the derivative of a polynomial, term by term).
2. F' = (log Z_m)' - (log Z_{m+v})' = R_{m,v} by S2 item 3.
3. Z_k(0) = 1 for every k, so F(0) = 0 and F(1) = integral over [0,1] of R. Correct.
4. F(1) = log(Z^m/Z^(m+v)) because Z_k(1) = Z^k/Z_ce with Z_ce independent of k (Z-check S2 item 1). Correct.
5. The remark at H:247-248 is correct: without the absolute value the integral is exactly F(1), so the signed version is a restatement of the endpoint problem.

## S4. The initial-value bound (C1) and the reduction to (C2) (H:455-494; also (C3), H:496-510) — HOLDS

Source read for the input: gap-joint-astra.md:97-274 ((J2)-(J9)).

(C1), checked line by line.
1. Structure. By SC (link-sign averaging under nu_ce), Z_k(lambda) = E_nu Xi(lambda w_k; U), where Xi(w;U) is the polymer polynomial of (J2) over compatible link-connected closed surfaces, with activities w_k(S;U) = (-1)^<k,S> prod_{p in S} t_p(U). At fixed U the weight of a compatible family is a product over its members (disjoint plaquette sets). So at fixed U it is a genuine polymer gas; no product law over U is used. Replacing w(S) by lambda^|S| w(S) only multiplies activities by lambda^|S|. Correct.
2. Parameter. The majorant becomes |w(T)| <= (lambda t)^|T| with t = tanh(beta). (J6) then reads 21|S| e lambda t/(1 - 400 e lambda t). With rho = 400 e lambda t and rho < 1/2 this is <= 21|S|/400 < |S|, so (J5) holds with b(S) = |S|. At lambda_0 = 1/2400, rho = e t/6 < 3/6 = 1/2, for every beta (t < 1). Correct, and uniform in beta, not only on I.
3. (J7) at lambda_0 gives pointwise in U: Xi(lambda_0 w_{m+v}; U) >= e^(-delta) Xi(lambda_0 w_m; U), delta = (N/200) rho^A/(1 - rho), using the area lemma |S| >= A for <v,S> = 1. Integrating against nu_ce (the "actual denominator") gives Z_{m+v}(lambda_0) >= e^(-delta) Z_m(lambda_0), that is, F(lambda_0) <= delta. With rho < 1/2: rho^A/(1-rho) < 2 * 2^(-A), so delta < (N/100) 2^(-A). Correct.
4. Nonnegativity. The marked weight is f_lambda(eta U) with f_lambda(U) = cosh(beta x) + lambda sinh(beta x). Its character coefficients are c_j for integer j and lambda c_j for half-integer j (Z-check S2 item 3), all >= 0 for lambda >= 0, and f_lambda >= 0 for lambda <= 1. So the lambda-model is a lattice gauge theory with a positive-type plaquette weight. The transfer operator is M^(1/2) K M^(1/2), with K >= 0 (nonnegative coefficients) and M the pointwise positive spatial multiplier (it carries the spatial twist m). The temporal twist v is the centre insertion, so Z_m(lambda) - Z_{m+v}(lambda) = 2 Tr(P_- L_lambda^a) >= 0. Hence F(lambda) >= 0 on all of [0,1], not only at lambda_0. Correct.

Reduction to (C2), checked.
5. By (R2), F(1) = F(lambda_0) + integral over [lambda_0,1] of R <= (N/100) 2^(-A) + LHS(C2).
6. N <= 24 a^4 and A >= a^2 give (N/100) 2^(-A) <= 0.24 a^4 e^(-(log 2) a^2) <= 0.24 e^(g^2/(4 log 2)) a^4 e^(-ga), since max over a of (-(log 2) a^2 + g a) = g^2/(4 log 2). Then q <= F(1)/2. So (C2) implies (E17) with p = max(p_R, 4). Correct.

(C3), checked. |t_p| <= tau_* gives |S_{k,lambda}| <= N tau_*/(1 - lambda tau_*), so |R| <= 2N tau_*/(1 - lambda tau_*), and its integral over [lambda_0,1] is 2N log((1 - lambda_0 tau_*)/(1 - tau_*)). Correct, and of volume order, as stated. The Gronwall remark (H:505-510) is ARGUED and accurate: at F ~ lambda^A, F'/F = A/lambda.

Z_2 remark (H:512-518). (C1) holds for Z_2 (items 1-3 are group-blind; for Z_2, nu_ce is uniform on link signs). F(1) >= log((1 - eps_a)/eps_a) is row 866's Peierls bound (Z-check S5 items 5-7). Correct.

Precision. The reduction removes only [0, 1/2400]. All of the order-one difficulty, near lambda = 1, is kept in (C2). The note says so (H:493-494).

## S5. (D3) is equivalent to HA after shrinking the disc and raising a_0 (H:362-396; with (D1)-(D2), H:326-351) — HOLDS

Set-up, checked.
1. Closed mod-2 plaquette sets are the 2-cycles of the cellular complex of the 4-torus. Each cycle in class h is S_h + b for a unique b in B_2 = im(partial_3). H_2(T^4; F_2) has 64 classes. So (D1) sums each closed surface exactly once, and SC gives Z_m(lambda) = sum_h (-1)^<m,h> H_h(lambda), since <m,S> = <m,h> for S in class h. With (-1)^<m+v,h> = (-1)^<m,h> (-1)^<v,h>, V_{m+v} = V_m - 2 O_{m,v}. Correct. The remark that "null-homologous" includes wrapping boundaries (H:338-341) is correct.

(D3) implies HA, checked.
2. |O| <= K |V_m| on |z| < s, K = C N e^(-cA) <= 1/4 for a >= a_0. Near a zero of V_m the quotient O/V_m is bounded, hence has a removable singularity (Riemann). So w = 2 O/V_m is holomorphic on the disc with |w| <= 1/2.
3. V_{m+v}/V_m = 1 - w has modulus >= 1/2 off the zeros of V_m, and -log(1 - w) is holomorphic on the disc (principal series, |w| <= 1/2). At z = 0, V_m = 1 and O = O(z^A), so it equals the germ F near 0. |log(1-w)| <= |w|/(1 - |w|) <= 2|w| <= 4K. So |F| <= 4 C N e^(-cA) <= 4CN on |z| < s, s > 1. This is HA with r = s, B = 4C. Correct.

HA implies (D3), checked.
4. HA on |z| < r with |F| <= BN. For 1 < s < r, Schwarz on the order-A zero gives |F| <= BN (s/r)^A = BN e^(-cA) on |z| <= s, c = log(r/s). N <= 24 a^4 and A >= a^2, so this is <= log 2 for a >= a_0.
5. V_{m+v} = V_m e^(-F) holds near 0 and both sides are holomorphic on the disc, so it holds on the disc, including at common zeros. Then |O| = |V_m| |1 - e^(-F)|/2 <= |V_m| |F| e^(|F|)/2 <= |V_m| |F| <= BN e^(-cA) |V_m|. This is (D3) with C = B. Correct.
6. Both directions keep the constants uniform in the task data. No estimate on an individual H_h is required. Correct.

Also checked in passing (used by S7): (D5)-(D7). Averaging over z in F_2^E kills every S with partial S != 0, so Phi_k = sum_h (-1)^<k,h> b_h. The pairing H^2 x H_2 -> F_2 is perfect, so the 64-term Fourier inversion (D6) holds. For real |lambda| < 1/tau_* every factor in (D5) is positive, so each Phi_k > 0, b_0 = (1/64) sum_k Phi_k > 0 and |b_h| <= b_0. Correct. The "first failing estimate" (H:432-439) is accurate: after (D7), 64 class means bounded only by 1 remain.

## S6. The thin, everywhere nearly flat event bound of Step 5 ((A1)-(A4), H:523-650) — HOLDS

Sources read for the inputs: gap-z2parity-astra.md:120-175 (the split D_k, (S)) and :386-425 (the Z_2 deletion bound (Z)); gap-seed-limit.md, Lemma FE and its proof.

Set-up, checked.
1. With U = z V(q), x_p = (delta z)_p J_p, so cosh(beta x_p) = cosh(beta J_p) and sinh(beta x_p) = (delta z)_p sinh(beta J_p). Haar on SU(2)^E is uniform z times quotient Haar. So the integral of D_k(q,lambda) dq is Z_ce Z_k(lambda), with a k-free factor. Each factor of D_k is cosh(beta J) +- lambda sinh(beta J) > 0 for 0 <= lambda <= 1, so D_k > 0. Then E_{nu_{m,lambda}} c_{m,v} = (Z_m(lambda) - Z_{m+v}(lambda))/(2 Z_m(lambda)). Correct and exact. The note correctly says c can be negative (row 866 (S) and its NP example).

(A1)-(A3), checked.
2. epsilon > 0: 5 - log 80 > 0 since e^5 > 1097/12 > 80 (Z-check S5 item 7). |tr U_p/2| is invariant under conjugation and under U_p -> -U_p, so G_epsilon is a gauge-invariant event of q.
3. FE for the present weights. Each marked factor equals ((1 + lambda eta)/2) e^(beta x) + ((1 - lambda eta)/2) e^(-beta x), a convex combination of numbers in [e^(-beta), e^(beta)]. The FE proof then gives the factor e^(2 beta |P|) with |P| <= 6|Gamma|, that is e^(12 beta |Gamma|). The proof of FE uses only this oscillation bound and Haar mass one. Correct.
4. Disjoint plaquettes. A (1,2)-plaquette at base x uses only the sites x, x+e1, x+e2, x+e1+e2. Bases with coordinates in {0, 3, ..., 3(k-1)}, k = floor(L/3), differ by >= 3 in coordinates 1 or 2 (and the wrap-around gap is L - 3k + 3 >= 3), or differ in coordinate 3 or 4. So the link sets are disjoint. floor(n/3) >= n/5 for n >= 3 (n = 3k + r <= 5k). So M >= V/625, V = a^2 c d >= a^4. Correct.
5. Under product Haar, disjoint plaquette holonomies are independent and Haar. With tr U/2 = cos theta and Weyl density (2/pi) sin^2 theta on [0, pi], the two caps theta <= epsilon, theta >= pi - epsilon have probability (4/pi) * integral_0^epsilon sin^2 <= 4 epsilon^3/(3 pi). Correct.
6. G_epsilon is contained in the event "the M chosen plaquettes are in the caps", a function of 4M links. FE gives nu(G_epsilon) <= e^(48 beta M) p_epsilon^M. With 48 beta <= 120 and epsilon^3 <= 3 pi e^(-120)/8: e^(48 beta) p_epsilon <= e^(120) e^(-120)/2 = 1/2. So nu(G_epsilon) <= 2^(-M) <= exp(-(log 2) V/625), uniformly in 0 <= lambda <= 1, beta in I and the twists. The bound is for the push-forward of the full marked law; no product law on q is used. Correct.

(A4), checked.
7. For the representative of v on one stack, the m and m+v integrands differ on K_v = a L_j <= 2a^2 factors. Each factor ratio lies in [e^(-2 beta), e^(2 beta)] (both factors in [e^(-beta), e^(beta)]). Integrands are positive, so the ratio of the z-sums lies in the same range raised to K_v. So |c| <= (e^(2 beta K_v) + 1)/2 <= e^(2 beta K_v) <= e^(10 a^2). With V >= a^4: the G_epsilon part of the average is at most exp(10 a^2 - c_0 a^4). Correct.
8. Threshold. a >= sqrt(20/c_0) gives c_0 a^4/2 >= 10 a^2; a >= (2g/c_0)^(1/3) gives c_0 a^4/2 >= g a. So exp(10a^2 - c_0 a^4) <= e^(-ga). Correct.

Inclusion of the old bad environments, checked.
9. The bi-invariant angle on SU(2) satisfies d(UV, 1) <= d(U, 1) + d(V, 1). Four link lifts within epsilon/4 give a plaquette angle <= epsilon, so J_p >= cos epsilon, inside G_epsilon. Gauge transformations keep it inside.
10. 5 cos epsilon >= 5 - (5/2) epsilon^2 >= 5 - (5 - log 80)/2 = (5 + log 80)/2 > log 80. The conditional object is a Z_2 gauge theory with positive couplings beta J_p. Its frustrated-plaquette weights are u_p = e^(-2 beta J_p) = e^(-5 J_p) <= e^(-5 cos epsilon) at beta = 5/2. The deletion step of (Z) needs only u_p <= u_max with 80 u_max < 1. So the conditional odd fraction tends to 1/2 uniformly on that set (at lambda = 1). Correct.
11. The model checks are correct. U(1): cap probability 4 epsilon/(2 pi) = 2 epsilon/pi; the same choice works for small epsilon, so (A3) does not separate U(1). Z_2: every plaquette is in the cap, cap probability 1. 2T: the central elements +-1 are 2 of 24; the noncentral ones have |tr/2| in {0, 1/2}; so a cap with cos epsilon > 1/2 has Haar probability 1/12, and e^(120)/12 is not small. Exactly frozen 2T: all plaquettes central, probability 1.

Scope (stated in the note, correct). The event has volume-order exponentially small probability. The bound beats the area-size pointwise bound on c only because of that. On the complement the same pointwise bound is e^(O(a^2)) times a probability near 1. So (A4) controls a negligible set and gives no information on the typical environment. It is a real, proved statement about a part of the average, not a step toward (C2).

## S7. The binding tests of Step 6 (H:652-676; and the Z_2 test of Step 3, H:441-449) — HOLDS AFTER CORRECTION (one table cell)

Controls, checked against Z-check.
1. Z_2 at beta 5/2: q -> 1/2 (Z-check S5, valid for beta > (log 80)/2). Frozen 2T: N_0 = 5856, N_v = 96, Z^v/Z^0 = 1/61, q = 30/61, at fixed torus as beta -> infinity (Z-check aside). Free Maxwell odd fraction: Z-check U(1) item 1. The note's statement that the Wilson-cosine U(1) identification is not proved is correct.

Step 3 Z_2 test, checked. Integrating (D6): H_h = (1/64) sum_k (-1)^<k,h> Z_k(1). Z^k/Z^0 <= eps_a/(1 - eps_a) for all 63 nonzero k (the all-class bound). So H_h/H_0 -> 1 for every h. Exactly 32 of the 64 classes pair oddly with v. So O/V_0 -> 1/2 = q. Correct.

Table rows, checked one by one.
2. Row (R0). U(1): x_p = cos theta_p, |t_p| <= tanh(beta), (R0) holds verbatim. Z_2: holds (S1 item 4). Frozen 2T: R tau < 1 fails as tanh(beta) -> 1, so no beta-uniform R; correctly stated. Correct.
3. Row (R1)-(R2), (R), (C2). Identities: group-blind, correct. Z_2: F(1) -> infinity, so (R) fails; (C1) holds for Z_2 (S4), so (C2) fails. Frozen 2T: F(1) -> log 61; (R) gives integral over [0,1] of |R| >= log 61; (C1) is uniform in beta (S4 item 2), so integral over [lambda_0,1] of |R| >= log 61 - (N/100) 2^(-A); (C2) with beta-uniform constants fails. U(1): ARGUED, conditional on the Coulomb matching. Correct.
4. Row (D1)-(D7). Correct (item above and S5).
5. Row (D3) = HA. HA implies (E17) (Z-check S3), and (E17) fails for Z_2 at 5/2 and for the frozen family. Correct.
6. Row (C1), (C3). Correct (S4).
7. Row (A3)-(A4). Correct (S6 item 11).
8. Row (R4). Correct.

Correction (one cell). Row "(D3) equivalent to HA", column "U(1) Coulomb check" reads "Same implication, no group selection". It should also state the target-level outcome, as the row above does: "HA, hence (D3), would force the odd-flux fraction to 0; false in a Coulomb phase if the Wilson-cosine matching is supplied (ARGUED; Z-check U(1) item 2)." As written, the cell can be read as "the test is not applied". This does not change any proof.

Precision (no correction). Every "fails" entry in the Z_2 and frozen-2T columns for (R), (C2), (D3) and HA follows from one fact: each implies (E17) by a group-blind argument, and (E17) fails there. So the tests confirm that these targets are not refuted by structure they share with Z_2, frozen 2T or U(1). They do not discriminate between the targets.

## S8. (C2) as a target: the three tests, and its strength relative to (E17)

Tests (all three use the same mechanism: (C1) is group-blind and beta-uniform, S4 items 1-3, so (C2) + (C1) gives F(1) small and hence (E17) in the model).
1. U(1) Coulomb test — PASSES (ARGUED). For Wilson U(1) with the Z_2 centre marker, (C1) holds with the same proof. So U(1)-(C2) would give q -> 0. In a Coulomb phase the odd-flux fraction stays order one (free-Maxwell U-test, Z-check U(1) item 1). So (C2) is false there, as it must be. The Wilson-cosine leg is not in the lane, as before.
2. Z_2 at beta 5/2 — PASSES (PROVED). (C1) holds; F(1) >= log((1 - eps_a)/eps_a) -> infinity. So integral over [lambda_0,1] of |R| -> infinity. (C2) is false for Z_2.
3. Frozen 2T — PASSES (PROVED, as a beta-uniform statement at fixed torus). (C1) holds for every beta; F(1) -> log 61 as beta -> infinity. So integral over [lambda_0,1] of |R| >= log 61 - o(1). (C2) with beta-uniform constants is false for 2T.
Consequence: a proof of (C2) must use a property of Wilson SU(2) on I that Z_2 at 5/2, frozen 2T and Coulomb U(1) lack. These are the same three tests (E17) passes, for the same reason.

Strength — (C2) is NOT weaker than (E17). It is (E17) in derivative form plus a variation condition.
4. (C2) implies (E17) (S4 item 6). So (C2) cannot be weaker than (E17).
5. (C2) implies more. For every lambda' in [lambda_0,1], F(lambda') <= F(lambda_0) + integral over [lambda_0,lambda'] of |R|. So (C2) gives the lambda'-analogue of (E17), with the same rate g, for every interpolated model on [lambda_0,1].
6. Converse under monotonicity. F >= 0 on [0,1] (S4 item 4). If R >= 0 on [lambda_0,1] (F nondecreasing), then integral over [lambda_0,1] of |R| = F(1) - F(lambda_0) <= F(1) = -log(1 - 2q) <= 4q for q <= 1/4. So (E17) implies (C2), and the two are equivalent up to constants. Monotonicity of F in lambda is neither proved nor refuted for Wilson SU(2) on I.
7. Without monotonicity the converse fails in the class of normalized pairs. Take Q = 1 and P = 1 + 2(A+1) lambda^A (1 - lambda). P - Q has order A, P >= 1 on [0,1], and F(1) = 0, so the endpoint fraction is 0. At lambda* = A/(A+1), lambda*^A (1 - lambda*) >= e^(-1)/(A+1), so F(lambda*) >= log(1 + 2/e) > 0.55, and the integral over [lambda_0,1] of |F'| >= 1.1 - F(lambda_0), with F(lambda_0) -> 0. So (C2) fails while the endpoint bound holds. (Auxiliary polynomials only; no Wilson SU(2) statement.)
8. Logical order: HA => (R) => (C2) => (E17) [the last with (C1)], and (E17) + (R >= 0 on [lambda_0,1]) => (C2). HA is strictly stronger than (R) on the class of normalized pairs (S1). (C2) is either a restatement of (E17) (if the response has a sign) or strictly stronger.
9. Wording correction. H:207 ("a weaker real averaged sufficient statement"), H:678-680 and the note's RESULT line ("a weaker real averaged response bound suffices") are correct only as "weaker than HA". They should say so. Suggested text for H:678-680: "HA is an unnecessary strengthening of the consumer. (C2) is a real sufficient criterion between HA and (E17): strictly weaker than HA on normalized pairs, and at least as strong as (E17); it is equivalent to (E17) when the response R has a sign on [lambda_0,1]." Its value is the representation of F' as a difference of two expectations with actual normalizers, which a proof may attack at each lambda; it is not a reduction of what must be proved.

## Summary

| Statement | Lines | Verdict |
|---|---|---|
| S1 real-segment restriction of HA holds automatically ((R0), single-stack bound) and is insufficient; (R) does not imply HA ((R4), (R5), Rouche zeros); HA => (R) => (E17) | H:171-311 | HOLDS (strict loss shown on normalized pairs, not within Wilson SU(2), as the note states) |
| S2 interpolating measures mu_(k,lambda), scores, (R1) | H:207-222 | HOLDS |
| S3 derivative identity (R2) | H:224-235 | HOLDS |
| S4 (C1) (rho = e t/6 < 1/2, F(lambda_0) <= (N/100) 2^(-A), F >= 0 by transfer positivity) and reduction to (C2); (C3) | H:455-518 | HOLDS |
| S5 (D1)-(D2); (D3) <=> HA after shrinking the disc and raising a_0; (D5)-(D7) | H:326-439 | HOLDS |
| S6 thin everywhere nearly flat event, (A1)-(A4), and the model checks | H:523-650 | HOLDS (it controls a set of probability <= 2^(-V/625) only) |
| S7 binding tests of Step 6 and the Step 3 Z_2 test | H:441-449, 652-676 | HOLDS AFTER CORRECTION: the U(1) cell of the "(D3) = HA" row should state the target-level outcome (false in a Coulomb phase, ARGUED) |
| S8 (C2) as a target | H:482-494, 678-680 | Passes U(1) Coulomb (ARGUED), Z_2 at 5/2 (PROVED), frozen 2T (PROVED, beta-uniform); NOT weaker than (E17): (C2) => (E17), and (E17) => (C2) only if R has a sign on [lambda_0,1]; wording "weaker" must read "weaker than HA" |

No mass gap, (E17), (C2), (R) or HA is established by the note or by this check. Research check only; no status granted. Only this output file was written; no repository file was edited; no subagent, no computation, no download.

RESULT: HOLDS — S1 (real-segment HA is automatic via (R0) and insufficient; (R) does not imply HA on normalized pairs, (R4)-(R5) and Rouche zeros checked), S2 (mu_(k,lambda), (R1)), S3 ((R2)), S4 ((C1) with rho = e t/6 < 1/2 and F >= 0 by transfer positivity; reduction to (C2); (C3)), S5 ((D3) <=> HA after shrinking the disc), S6 (thin nearly flat event, nu(G_eps) <= 2^(-V/625), contribution <= e^(-ga)); HOLDS AFTER CORRECTION — S7 (Step 6 tests correct; the U(1) cell of the (D3)=HA row should state the ARGUED Coulomb failure); (C2) as a target passes U(1) Coulomb (ARGUED), Z_2 at 5/2 (PROVED) and frozen 2T (PROVED, beta-uniform), but it is NOT weaker than (E17): (C2) implies (E17) and the lambda-analogue of (E17) on all of [lambda_0,1], and (E17) implies (C2) only if the response R has a sign there, so (C2) is a restatement of (E17) (under monotonicity of F in lambda, unproved) or strictly stronger; the note's "weaker" must read "weaker than HA". Checked by Claude Opus 5.5 (high), by hand.
