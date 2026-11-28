# Check of library/gap-z2parity-astra.md (FINISH row 870)

- Checker: Claude Opus 5.5 (high effort), by hand, no subagents, no compute.
- Clone commit: c41c001d894a53b5c3b2a743accb3645f5a670e7 (ym4d-lead/clone, pulled 2026-11-12).
- Note checked: D/library/gap-z2parity-astra.md (row 866, OpenAI Codex gpt-6-astra, max effort).
- Definitions from: D/library/gap-hs-max.md (row 860: P1, P2, Lemma OS) and D/library/gap-hs-check-astra.md.
- D = .claude/science/physics-loops/ym4d-hard-route-20261030.

Sources read in full: gap-z2parity-astra.md (575 lines), gap-hs-max.md (263 lines), gap-hs-check-astra.md (232 lines).
Spot-read for definitions: gap-ext-astra.md:78-106 (tori (a,a,c,d), a >= 3, c,d in {a,2a}, N_p = 6a^2cd), gap-expose-astra.md:575-600 ((E16), (E17)), gap-es1-opus.md:129-152 (Lemmas Z2-a, Z2-b).
Line references "Z:n" are to gap-z2parity-astra.md at the clone commit above. No computation was run; every arithmetic step below was redone by hand.

## S1. (E17) is the slice-homology parity problem (Z:77-99) — HOLDS

- Geometry. Z:82-84 matches gap-ext-astra.md:80-82: Lambda = (Z/a)^2 x Z/c x Z/d, time direction 1, time period a, spatial periods (a, c, d) in directions 2, 3, 4.
- Formula. Z:86-90 is (E16) of EX:575-585 rewritten. Z^m - Z^(m+v) = 2 Tr(P_- L_m^a) (EX (E3)) gives Tr(P_-L^a)/Tr L^a = (1 - Z^(m+v)/Z^m)/2. P1 of gap-hs-max (checked HOLDS in gap-hs-check-astra:137-148) gives P_- = 1{<omega_i, C> = 1} on each spin block, with C the mod-2 cycle of half-integer edges. So q_{m,i}(a) = Pr{<omega_i,C> = 1} in the positive one-slice law. All three expressions agree.
- (P) at Z:93-97 is (E17) word for word: max over m_2 = 0, i = 3, 4, bound C a^p eta_*^(a/2), with eta_* the consumer constant.
- The scope remark at Z:91-92 (only the pairing with the chosen cocycle is fixed) is correct. It is the same restriction gap-hs-check-astra:148 imposed on P1.
- "Stronger than (FQ)" (Z:80): correct as stated. EX:589-595 derives (FQ) from (E17) with K(a) = 8 C a^p.
- Labels. The note marks this ARGUED. It is in fact a direct consequence of P1 and (E3), which are checked. Nothing new is claimed, and the note says so. No correction needed.

## S2. The marked polynomial and its area-order zero (Z:256-301) — HOLDS

Checked line by line.
1. (M) is exact. e^(beta eta x) = cosh(beta x)(1 + eta tanh(beta x)) for eta = +-1. So Z^k = Z_ce E_ce prod_p (1 + eta_{k,p} t_p), and Z_k(1) = Z^k/Z_ce. Each Z_k is a polynomial of degree at most N, with Z_k(0) = 1. Z_ce does not depend on k, so ratios at lambda = 1 are the true twisted ratios.
2. Positivity on 0 <= lambda <= 1 (Z:267-271). The identity cosh + lambda sinh = ((1+lambda)/2) e^(beta x) + ((1-lambda)/2) e^(-beta x) is correct. With eta = -1 the two coefficients swap, so the weight is still positive. More: since |t_p| <= tau = tanh(beta) < 1, every factor 1 + lambda eta t_p is positive for real 0 <= lambda < 1/tau. I use this extension in S3 below.
3. Character reading (Z:272-273). cosh(beta x) is even under g -> -g and sinh(beta x) is odd. With chi_j(-g) = (-1)^(2j) chi_j(g), the even part carries exactly the integer-spin coefficients of e^(beta x). So lambda multiplies the half-integer coefficients only. Correct.
4. Closure (M1). Expand the product over subsets S. Replace one link U_l by -U_l. Haar measure and prod cosh(beta x_p) are invariant. Each t_p with l in p changes sign; each plaquette contains l at most once (periods >= 3). So A_ce(S) = 0 unless every link lies in an even number of plaquettes of S, that is, unless dS = 0 mod 2. The sign prod_{p in S} eta_{k,p} is (-1)^<k,S>. No sign of A_ce(S) is used. Correct.
5. Area bound. Let pi be the coordinate projection onto the (1,i)-torus Z/a x Z/L_i. It is cellular. Plaquettes of type (1,i) go to faces; other plaquettes go to lower-dimensional cells and are dropped. This is a chain map mod 2. Since v_{1i} is the pull-back of the generator of H^2 of the 2-torus, <v_{1i}, S> = <[T^2], pi_* S>. If this is odd, pi_* S is a nonzero 2-cycle. On a connected closed square surface each edge has exactly two faces, so a nonzero mod-2 2-cycle is the set of all a L_i faces. Each face needs a preimage plaquette in S, and different faces have different preimages. So |S| >= a L_i >= a^2. Correct. (This is the same count as Lemma Z2-b (a) of gap-es1-opus.md:144-149, applied to a 2-cycle instead of a cocycle.)
6. Divisibility. Z_m - Z_{m+v} = 2 sum over {dS = 0, <v,S> = 1} of lambda^|S| (-1)^<m,S> A_ce(S). So it is divisible by lambda^(A_i). Since Z_{m+v}(0) = 1, log Z_m - log Z_{m+v} = log(1 + (Z_m - Z_{m+v})/Z_{m+v}) is O(lambda^(A_i)) as a germ. Correct.
7. N = |P(Lambda)| = 6 a^2 c d agrees with gap-ext-astra.md:82. N <= 24 a^4.

Remark (no correction). The zero is a statement about the difference only. Each log Z_k alone has order-one Taylor coefficients from contractible surfaces. The note says this at Z:301.

## S3. HA implies (P), with an area gain (Z:303-346) — HOLDS

Checked line by line.
1. Schwarz step. F is holomorphic on |lambda| < r and agrees with the germ near 0, so it has a zero of order >= A_i at 0. Then F/lambda^(A_i) is holomorphic there. The maximum principle on |lambda| = s < r gives |F(lambda)| <= BN (|lambda|/s)^(A_i). Let s -> r. Since r > 1, lambda = 1 is inside, and |F(1)| <= BN r^(-A_i). Correct.
2. Branch at lambda = 1. On [0,1] both Z_k(lambda) are positive (S2 item 2), so the real function log Z_m - log Z_{m+v} is real-analytic on a neighbourhood of [0,1]. It agrees with the germ near 0. The disc meets that neighbourhood in a connected open set containing 0. By the identity theorem F(1) = log(Z^m/Z^(m+v)), which is real. It is >= 0 because Z^m - Z^(m+v) = 2 Tr(P_- L^a) >= 0. Correct.
3. (M3). q = (1 - e^(-F(1)))/2 <= F(1)/2 <= (BN/2) r^(-A_i). With N <= 24 a^4 and A_i >= a^2, r > 1: q <= 12 B a^4 r^(-a^2). Correct.
4. Rate. With s = log r, g = -(1/2) log eta_*: max over real a of -s a^2 + g a is g^2/(4s), at a = g/(2s). So e^(-s a^2) <= e^(g^2/(4s)) e^(-g a) = e^(g^2/(4s)) eta_*^(a/2). Correct. (E17) then holds with p = 4 and C_0 = 12 B e^(g^2/(4s)), uniformly over beta in I, tori and twists, because B and r are.
5. Small sizes. q <= 1/2, since Z^(m+v) = Tr(Theta_omega L^a) >= 0 (positive kernel). Finitely many a < a_0 are covered by enlarging C_0. Correct.
6. The sufficient input (Z:334-346), no zeros of Z_k on |lambda| < R. |Z_k| <= E prod |1 + lambda t_p| <= (1 + R tau)^N. g_k = log Z_k exists on the disc with g_k(0) = 0 and Re g_k <= M. The map h = g/(2M - g) satisfies |2M - g|^2 - |g|^2 = 4M(M - Re g) >= 0, so |h| <= 1, h(0) = 0, and Schwarz gives |h| <= r/R. Then |g| = 2M|h|/|1 + h| <= 2M (r/R)/(1 - r/R) = 2Mr/(R - r). This is Borel-Caratheodory. Correct, with B = 4 r log(1 + R tau)/(R - r).

Remark (precision, not a correction). The conclusion of HA is much stronger than (E17). It gives q <= 12 B a^4 e^(-(log r) a L_i): an area law for the electric-flux fraction in the (1,i) plane, with string tension at least log r, uniform on I. (E17) needs only decay e^(-g a). The note says HA is stronger than (P) (Z:312, Z:546). The size of the gap matters for the plausibility question below.

## S4. The density-1/3 construction (Z:199-240) — HOLDS

Checked line by line.
1. The direction-3 and direction-4 spatial edges at fixed x_2 form the square torus Z/c x Z/d. There are a such planes, and they are disjoint. Correct.
2. Uniform law on a coset B + h of the boundary space B of one plane. For an edge e, adding the boundary of a plaquette through e is a translation by an element of B. It maps the coset onto itself and flips e. So Pr(e occupied) = 1/2 exactly, in every plane and in either law. Periods >= 3 keep the plaquette boundary a set of four distinct edges.
3. Density. 2acd plane edges among 3acd spatial edges, each occupied with probability 1/2: mean fraction (1/2)(2/3) = 1/3. Correct.
4. Local indistinguishability. Let B (the box) omit a coordinate-4 value x_4^*. The direction-3 winding loop gamma at (x_2 of the chosen plane, x_4^*) has no vertex in the box, so no edge of the box. b -> b + gamma is a bijection from the zero coset onto the direction-3 winding coset, and fixes every edge of the box. So the push-forward of the uniform law is the uniform law, with the same restriction to the box. The other planes have the same law under mu_0 and mu_1. So the two laws have the same joint marginal on every such box. Correct. (Only the coordinate-4 omission is used for this loop; the coordinate-3 omission at Z:213 is not needed. Harmless.)
5. Parity. The winding loop crosses the cut cocycle omega_3 once, so <omega_3, b> is 0 under mu_0 and 1 under mu_1. mu_theta has odd-sector probability theta. Correct.
6. Realization as SU(2) states. Each vertex meets the cycle in 0, 2 or 4 edges (the direction-2 edges carry spin 0). Invariant tensors exist: the singlet for two spin-1/2 lines, a 2-dimensional space for four. A spin network with nonzero intertwiners is a nonzero gauge-invariant function in the block j(b); different spin assignments are orthogonal by Peter-Weyl. So sum_b mu_theta(b) |psi_b><psi_b| is a positive, normalized, gauge-invariant density matrix whose spin law is mu_theta. Theta_omega acts on psi_b by (-1)^<omega,b>, so the centre character is 1 - 2 theta for any omega pairing with the chosen winding and 1 otherwise. Correct.

Scope (stated in the note, Z:229-235, and correct). The example rules out a deduction of (P) from local marginals, density, low-spin support, Gauss parity and positivity alone. It is not a Wilson transfer power, it breaks x_2-translation, and its local law (density 1/2 per plane edge) is not the Wilson one. It says nothing against identities that link different homology sectors or against noncontractible observables.

## S5. The finite-beta Z_2 test (Z), (Z2-test), and the refutation of an environment-uniform conditional bound (Z:386-442) — HOLDS (scope: beta > (log 80)/2, about 2.191, which includes 5/2)

Checked line by line.
1. Surface form. Z^k_{Z2} = e^(beta N) N_fl sum over D in k + B^2 of u^|D|, u = e^(-2 beta). This is Lemma Z2-a of gap-es1-opus.md:131-139 (read). The factor e^(beta N) N_fl does not depend on k. Correct.
2. All-class ensemble. Summing over the 64 classes gives the measure proportional to u^|D| on all 2-cocycles D. On the dual lattice a cocycle is a closed plaquette surface (each 3-cube = dual edge meets an even number). Components through shared dual edges are closed: all D-plaquettes at a given dual edge are in one component. Class is additive, so a nonzero total class forces a component with nonzero class. Correct.
3. Minimum size. Lemma Z2-b (a) (gap-es1-opus.md:144-149, read): a cocycle with [F]_{mu nu} = 1 has a plaquette in each of the N_{mu nu} planes, N_{mu nu} = product of the two other sides >= a^2 here. Correct.
4. Counting. Each plaquette has 4 edges; each edge of the 4D lattice lies in 6 plaquettes, so 5 others: degree <= 20. Rooted connected sets of size n: at most C_(n-1) <= 4^(n-1) plane-tree shapes times 20^(n-1) neighbour choices, so <= 80^(n-1). The map from (shape, choices) to sets is onto, which is all that is needed. Correct.
5. Peierls step. If gamma is a closed component of D, then D -> D + gamma is injective into closed surfaces and multiplies the weight by u^(-|gamma|). So Pr(gamma is a component) <= u^|gamma|. Union over roots: Pr(nonzero class) <= N sum_{n >= a^2} 80^(n-1) u^n = (N/80) b^(a^2)/(1 - b). Correct.
6. Ratio. Pr(class v) <= eps_a and Pr(class 0) >= 1 - eps_a give Z^v/Z^0 <= eps_a/(1 - eps_a). Correct.
7. Arithmetic at beta = 5/2. 1 + 5 + 25/2 + 125/6 + 625/24 + 3125/120 = (120 + 600 + 1500 + 2500 + 3125 + 3125)/120 = 10970/120 = 1097/12 = 91.41... > 80, so b = 80 e^(-5) < 1. Correct. With N <= 24 a^4, eps_a -> 0 and q^{Z2}_{0,i}(a) -> 1/2.
8. Scope. The constant 80 needs e^(2 beta) > 80, that is beta > 2.191. At beta = 43/20, e^(4.3) is about 73.7 < 80, so this proof does not reach the left end of I. HA is quantified uniformly over I, so one beta (5/2) suffices for the refutation. No correction needed; the note uses only beta = 5/2.
9. Conditional bound. With U = z V(q), Haar on SU(2) is uniform z times quotient Haar, so Z^k = int D_k(q) dq (Z:130-137, consistent). The conditional marked polynomial is 2^(-|E|) sum_z prod_p [cosh(beta J_p) + lambda eta_{k,p} (dz)_p sinh(beta J_p)]. At lambda = 0 it does not depend on k. Flipping z_l gives closure, and the S2 area argument applies, so the conditional difference also has the area-order zero. All conditional weights are positive on [0,1] (|tanh| < 1). So a conditional HA, with B, r uniform over environments, gives the conditional (M3). At the identity environment J_p = 1 and the conditional object is Z_2 gauge theory with twist k. (M3) would force the Z_2 value of q to 0; item 7 gives 1/2. Contradiction for large a. Correct.
10. Positive measure. At fixed torus the conditional q is continuous in the environment (locally continuous lifts; D_k does not depend on the lift choice), and nu_0 has a positive continuous density D_0/Z^0 against quotient Haar. So the violation holds on an open set of positive nu_0-measure. An essential-supremum version also fails. Correct.

Aside (not on the list; checked because S7 cites it): the frozen 2T count (Z:450-483). Anticommuting unit quaternions must both be purely imaginary and orthogonal (from g1 g3 + g3 g1 = 0 the scalar parts vanish). N_0 = 16 + 3(256 - 16) + 4(1296 - 16) = 5856, N_{v13} = 24 x 2 x 2 = 96, 96/5856 = 1/61, q -> 30/61. Correct at fixed torus as beta -> infinity, as the note says.

## S6. The shrinking-disc limit of analytic continuation (Attempt A, Z:348-362; Final checkpoint item 3, Z:556-557) — HOLDS AFTER CORRECTION (scope wording)

Checked.
1. Auxiliary law t_p = tau eps for all p, eps = +-1 with probability 1/2. The average of prod(1 + lambda t_p) is ((1 + w)^N + (1 - w)^N)/2, w = tau lambda. It is positive for real 0 <= lambda < 1/tau. Zeros: ((1+w)/(1-w))^N = -1. With w = i tan(pi/(2N)), (1+w)/(1-w) = e^(i pi/N), whose N-th power is -1. So there is a zero at lambda = i tan(pi/(2N))/tau, which tends to 0. Correct.
2. Crude bound. |Z_k - 1| <= sum over nonempty S of |lambda|^|S| tau^|S| = (1 + |lambda| tau)^N - 1 < 1 iff |lambda| < (2^(1/N) - 1)/tau, about (log 2)/(N tau). Correct.
3. Attempt B (Z:364-375): |A_ce(S)| <= tau^|S| and Z_m(1) >= (1 - tau)^N hold pointwise. The resulting bound keeps a cost exponential in N. Correct.

Correction (scope). The auxiliary law has no link structure: every t_p is the same variable, A(S) is nonzero for every S, and there is no closure (M1) and no twist. So it refutes only the inference "every factor zero-free on |lambda| < 1/tau, and the average positive on the real segment, imply a zero-free average on a fixed disc". It does not show that the Wilson polynomials Z_k have zeros near 0. It also bears only on the sufficient input of Z:334-346 (zero-free Z_k), not on HA itself, which needs only the ratio. Z:358 says the first point; the Final checkpoint line 556 ("real positivity supplies only a shrinking disc") should read: "positivity on the real segment and |t_p| <= tau, used alone, supply only a disc of radius O(1/N); the closure structure (M1) is not used by that bound and is not shown insufficient."

## S7. "HA fails for Z_2 at beta 5/2" and "a background-uniform SU(2) version fails" (Z:378-382, 437-442, table Z:535) — HOLDS (both), with the scope the note itself states

1. Z_2 at beta = 5/2. The Z_2 marked polynomial is sum over closed S of (lambda tau)^|S| (-1)^<k,S>, up to a k-free factor. Every step of S2 and S3 holds for it verbatim: closure by flipping one Z_2 link, the projection area bound, positive weights on [0,1]. So the Z_2 analogue of HA would give the Z_2 value of q at most 12 B a^4 r^(-a^2) -> 0. S5 item 7 gives q -> 1/2 at beta = 5/2. So the Z_2 analogue of HA is false at beta = 5/2, for every choice of B, r > 1, a_0. Correct.
2. Background-uniform SU(2). This is S5 items 9-10: the identity SO(3) environment reduces the conditional object exactly to Z_2 at beta, and the failure persists on a set of positive nu_0-measure. Correct.
3. What is not claimed, and is not shown. Neither result refutes the averaged HA for SU(2) (Z:442 says so). The Z_2 proof covers beta > 2.191 only (S5 item 8), not all of I; this is enough because HA asks for uniformity on I.

Not on the list, spot-read only, not checked: Step 2's negative-integrand example (relies on the prior Lemma NP of gap-kappa-order.md, which I did not open), the loop-reconnection identity of Step 3 (standard; consistent), the fusion-grading lemma of Step 6 (consistent).

## HA: plausibility for SU(2) at order one (my assessment; ARGUED, with recalled numbers marked GUIDE)

Not refuted, not supported, and at least as hard as a confinement theorem. Reasons:
1. Its real-axis content is an area law. By S3, HA gives q <= 12 B a^4 e^(-(log r) a L_i): the odd electric-flux fraction decays with the area of the (1,i) torus, with string tension at least log r, uniformly on I. This matches the believed physics of SU(2) in I (positive string tension). GUIDE, recalled lattice values: sigma a^2 is about 0.13 at beta = 2.3 and about 0.03 at beta = 2.5. So HA can hold only with log r <= sigma(5/2), that is, r at most about 1.03. Such an r is allowed. But proving it means proving a uniform lower bound on the electric-flux free energy per unit area at order-one coupling. That is a confinement theorem, much stronger than (E17), which needs only decay e^(-g a).
2. The room is small. Every factor 1 + lambda eta t_p is zero-free only for |lambda| < 1/tanh(beta). This bound is 1/tanh(5/2) = 1.0136 (e^5 = 148.41) and 1/tanh(43/20) = 1.0275 (e^4.3 = 73.70). HA does not need factor zero-freeness, but at beta = 5/2 the disc must go past the physical point while staying within about 1.4% of where single-plaquette weights vanish.
3. Real segment. On [0, 1/tau) all weights are positive. Lowering lambda below 1 lowers every effective Z_2 coupling lambda tanh(beta J_p), so it adds centre disorder. No transition is expected on [0,1] if SU(2) confines at lambda = 1 (heuristic). The point lambda = -1 gives Z_k(-1) = Z^(k + kappa)/Z_ce, where kappa is the class of the all-plaquette cocycle (6 faces per cube, so it is a cocycle). The check there reduces to near-equality of temporally twisted partition functions, which is again the confining behaviour. So the two real test points are consistent.
4. Off the real axis there is no evidence either way, in the note or the lane. The note's own Z_2 picture shows the mechanism HA must use. At the identity environment the lambda-model is Z_2 at effective coupling lambda tanh(beta). The recalled self-dual point is tanh(beta_c) = 0.414, so that model has its transition at |lambda| about 0.42 < 1. HA therefore needs the SO(3) average (frustration) to push every complex zero of the twisted ratio beyond |lambda| = r > 1, uniformly in volume. I know no method that gives such a complex zero-free region at a coupling where the correlation length is several lattice spacings.
Verdict: HA as stated is plausible as a true statement on the real segment. Its complex-disc content is unassessed. It is not a plausible shortcut to (E17): it is strictly stronger and is itself an order-one confinement statement.

## HA and the U(1) Coulomb test — PASSES as a target (ARGUED); the proved steps pass no selection (agrees with Z:503-507)

1. U-test arithmetic (Z:487-501) checked. For the constant mode, (1/(2e^2)) L^3 int (theta-dot/L)^2 dt = (L/(2e^2)) int theta-dot^2 dt. H = e^2(-d^2/d theta^2)/(2L) has eigenvalues e^2 n^2/(2L). At time period L the weights are e^(-e^2 n^2/2). The centre flip theta -> theta + pi acts by (-1)^n. So the odd fraction is sum over odd n of e^(-e^2 n^2/2) divided by the sum over all n, which is positive and independent of L. Correct, for compact free Maxwell.
2. The steps S2 and S3 hold verbatim for U(1) with the Z_2 centre marker (flip theta_l -> theta_l + pi; e^(beta cos) = cosh + sinh). So HA for U(1) would give q -> 0 like a^4 e^(-(log r) a^2). In a Coulomb phase the odd-flux fraction stays order one (U-test). So HA is false in a Coulomb phase, and it passes the U(1) test as a target statement. Also, at lambda = 0 the U(1) marked model has q = 0, and at lambda = 1 in the Coulomb phase q is of order one. So the infinite-volume flux free energy must be non-analytic in lambda inside (0,1], which is exactly what HA excludes for SU(2).
3. Limits. The rigorous leg for Wilson-cosine U(1) on these twisted tori is not in the lane. U-test is free Maxwell. gap-hs-check-astra:207 records that the lane's Coulomb theorem is for the Villain Langevin generator. So "HA fails for Wilson U(1) at large beta" is ARGUED, not PROVED.
4. The proved parts of the note (closure, area zero, HA => (P), the density-1/3 example, Borel-Caratheodory) are group-blind. Any proof of HA must use an input that Wilson U(1) in the Coulomb phase lacks. The note says this.

## Summary table

| Statement | Lines | Verdict |
|---|---|---|
| S1 (E17) = slice-homology parity problem (P) | Z:77-99 | HOLDS |
| S2 marked polynomial (M), (M1); area-order zero (M2), A_i = a L_i >= a^2 | Z:256-301 | HOLDS |
| S3 HA => (P), (M3), rate kept; zero-free => HA (Borel-Caratheodory) | Z:303-346 | HOLDS |
| S4 density-1/3 construction: same local data and density, free class weight | Z:199-240 | HOLDS |
| S5 Z_2 Peierls test at beta = 5/2, q -> 1/2; environment-uniform conditional bound refuted on a positive-measure set | Z:386-442 | HOLDS (proof covers beta > 2.191) |
| S6 shrinking disc from positivity and factor bounds | Z:348-375, 556 | HOLDS AFTER CORRECTION: the auxiliary law has no closure; it refutes only the generic inference and the zero-free sufficient route, not the Wilson polynomials or HA |
| S7 HA fails for Z_2 at beta 5/2; background-uniform SU(2) HA fails | Z:378-382, 437-442, 535 | HOLDS |
| Aside: frozen 2T count 5856, 96, q -> 30/61 | Z:450-483 | HOLDS (fixed torus, beta -> infinity) |

No mass gap, (E17), (FQ) or HA is established by the note or by this check. Research check only; no status granted. Only this output file was written; no repository file was edited; no subagent, no computation, no download.

RESULT: HOLDS — S1 ((E17) = slice-homology parity), S2 (marked area-order zero, |S| >= a L_i), S3 (HA => (E17) with area gain; zero-free => HA), S4 (density-1/3 construction), S5 (Z_2 Peierls test at beta 5/2, q -> 1/2, environment-uniform conditional bound refuted; proof valid for beta > 2.191), S7 (HA fails for Z_2 at beta 5/2 and in the background-uniform SU(2) version); HOLDS AFTER CORRECTION — S6 (the shrinking-disc example has no closure structure: it refutes only the generic positivity/factor inference, not the Wilson polynomials or HA); HA is plausible on the real segment as an area law, is unassessed off the real axis, is strictly stronger than (E17) (it is an order-one confinement statement with string tension >= log r, so r <= about 1.03 at beta 5/2, GUIDE); HA passes the U(1) Coulomb test as a target (ARGUED: free-Maxwell U-test checked, Wilson-cosine leg not in the lane), while the note's proved steps are group-blind; (E17) remains open. Checked by Claude Opus 5.5 (high), by hand.
