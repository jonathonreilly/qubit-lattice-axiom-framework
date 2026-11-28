lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-28T16:30Z

# Cross-provider check of row 1661 (`library/gap-newmath-astra62-max3.md`)

Provenance: Claude Fable 5.2, high effort, Mac mini worker 1, pinned commit e5286638b. One reading by one model of another provider (the checked file was written by gpt-6.2-astra max). Not an audit and not human review. Queue row 1663.

Started 2026-11-28T04:30Z (date -u). No commit, claim or push from this machine; the relay copies this file.

Plan: read the whole checked file once, then give a verdict per claim in the order of the brief: 1. (30) and selectivity; 2. (37); 3. (38) / Stage 27; 4. (22), (28a), (29) and the zero count; 5. (34); 6. (39) / Stage 28; 7. the closing OPEN statement and the gap to the isotropic point. Each verdict is appended when reached.

## 0. Status log

- 2026-11-28T04:30Z: file created; reading the checked file.
- 04:31Z: read all 901 lines of the checked file (Stages 1-28). Next: look up the on-file inputs (rows 1468, 1553, 1145, 1143, 1227) and check claim 1.
- (log) inputs read for claim 1: FINISH rows 1661, 1553, 1556, 1468; `gap-k2-tool-design-fable.md` 3.1 (L99-L120); `gap-mech-direction4-fable.md` 1.4-1.5 (L180-L196); `gap-solve-astra62.md` (1) and its proof (L25-L45); RESULT lines of checks 1144, 1384, rows 1227, 1642.

## 1. Claim 1: formula (30) and its selectivity

Verdict: **the formula HOLDS; the selectivity claim HOLDS AFTER CORRECTION (it is selective in the sense "the three numbers differ", and it FAILS the tests (g1), (g3), (g5), (g6) of row 1553); the ordered limit is NOT a limit the consumer can use.**

### 1.1 What I redid (line anchors are of the checked file)

The first entry of (30) rests on (16)-(17) (Stage 13, L342-L387), (20)-(21) (L402-L410), the heat-trace limit (25)-(26) (Stage 17, L497-L533). The other two entries are Stage 20 (L653-L679). I recomputed each constant by hand. Status of my recomputation: ARGUED (a second derivation of the leading terms, not a new complete proof); the proofs are the checked file's.

1. Coordinates. The comb gauge and the triangular pivots are ON FILE (row 1143 (1), `gap-solve-astra62.md` L29-L41, checked by row 1144). I checked that the pivot face of a link (x, i) uses the first earlier coordinate j with x_j > 0, so it never wraps in both directions. So the seam field (wrapping i-links h_i, all else 1) has every pivot equal to 1, as L357 uses. Count: 3N links, N - 1 tree links, 3 windings, M = 2N - 2. Correct.
2. Magnetic exponent. For pure quaternions, log of the group commutator of exp(x), exp(y) is 2 x times y + O(3). With h_i = exp(X_i/sqrt(an)) the double-seam curvature is 2 (X_i x X_j)/(an), on the n faces with chi_i chi_j = 1. The source is closed (it depends on x_i, x_j only). Its mean is 1/n^2 of its seam value. Half the squared norm of the harmonic part, times s, is (n^3/2) (2 sqrt(s)/(a n^3))^2 |X_i x X_j|^2 = 2 gamma |X_i x X_j|^2 at s = gamma n^3 a^2. This is (18) and the display after it. Correct. The exact part is removed by a shift of the pivot Gaussian because range(dL) is the space of exact two-forms: dimensions 2N - 2 on both sides per colour, and a closed one-form that vanishes on the tree and on the three based wrapping edges is zero. Correct.
3. Electric exponent. The seam one-form chi_i (R Y_i - X_i)/sqrt(n), in units a^(-1/2), has harmonic part of squared norm |R Y_i - X_i|^2. So the kernel is (17). Correct. Error terms: pivots are O(1/a), seams O(a^(-1/2)), sqrt(s) = O_n(a); every mixed or cubic term times sqrt(s) is O_n(a^(-1/2)). Correct.
4. Tails. With r_i = sqrt(an) phi_i, row 1143's upper bound and the identity 1 - Re[h_i, h_j] = 2 sin^2 phi_i sin^2 phi_j |omega_i x omega_j|^2 give the radial bound C prod r_i^2 prod_(i != k) (1 + c r_k^2 r_i^2)^(-1) <= C' |r|^(-2). The electric bound for arbitrary slice fields is exp(-c_n |r - r'|^2): along a based line, |g h' g^(-1) - h| <= sum of the n link mismatches, so the constant is c_n of order 1/n^2. Fixed n only, as the file says at L379. The kernel exp(-c|x - y|^2) is Hilbert-Schmidt for |x|^(-2) d^3x (the displacement integral is C/|z|). Correct.
5. Dilation. X = gamma^(-1/6) Y turns (17) into e^(-hU) e^(h Delta/2) e^(-hU) on rotation invariants, h = gamma^(1/3). Correct. (21): m trial functions give lambda_m >= 1 - C_m h, the top eigenvalue is at most 1, and purity <= lambda_1^v / Tr S^v <= 1/(m (1 - C_m h)^v). Correct.
6. Heat trace. The arithmetic-geometric step at L515-L519 is exp(-2h sum_j U_j) = prod_j [exp(-t(U_j + U_(j+k)))]^(1/v) <= mean. Correct. The two-point majorant is the same radial bound. The limit object is H = -Delta/2 + 2U on invariants; its discrete spectrum and finite heat trace are ON FILE (row 1227 (4)-(8), `gap-solve25-astra62.md` L61-L93, check 1230). The purity of exp(-tH) increases strictly in t (its log-derivative is 2(E_t - E_2t) of the thermal mean energy). So q rises strictly from 0 to 1 and tau_* is unique. With gamma = kappa/n^3 and v = n/512, v h = kappa^(1/3)/512. Correct: first entry of (30).
7. Five dimensions (four spatial directions, N = n^4, M = 3(N - 1)). Scale h_i = exp(X_i/sqrt(a n^2)). Electric constant part: n^4/(n^2 n^2) = 1. Magnetic: (n^4/2)(2 sqrt(s)/(a n^2 n^2))^2 = 2 s/(a^2 n^4). So gamma_4 = kappa/n^4 and v h = kappa^(1/3) n^(-1/3)/512 -> 0. Radial weight w(r) <= C (1 + |r|)^(-4) on R^4. It is not integrable (a logarithm, the on-file log of row 1143 (2)), and it is square integrable, which is what the Hilbert-Schmidt bound needs at v >= 2. Correct: second entry.
8. Compact U(1), order-two flips. Plaquettes do not see the windings; the windings are Haar; a cycle of v slices keeps v - 1 Gaussian winding differences of width a^(-1/2) in d = 3 coordinates. So Z_+(v) is of order [slice constant]^v a^(-3(v-1)/2) and P is of order a^(-3/2) -> 0 at every fixed n, v. Correct: third entry. With the whole centre in the projector the kernel reads only the pivots, which move by s^(-1/2) = o(a^(-1/2)); rank one in the limit; purity 1. Correct.
9. Numbers in (14) (used by Stage 14 and later, not by (30)): Tr K = 4 pi sqrt(pi/2), ||f||^2 = 2 pi^(3/2), ratio sqrt 2; second term 1/72; 72 sqrt 2/73 - 1 < 2/5; (25/29)^2 = 625/841 > 457/625. Correct. The limit measure de d^3A/|A|^2 in (19): the Jacobian gamma^2 d^9X = r^(-2) dr de d^2A d^4w and the two transverse determinants |A|^2/r^2 give 1/|A|^2. Correct.

First failing step in the proof of (30): none found. Not rechecked by me: row 1143 (1) and row 1227 (4)-(8) (both have a check on file), and the Feynman-Kac identification at L522 beyond its outline.

### 1.2 The selectivity tests

What decides each entry (ARGUED, from the proof lines above):

- 4D SU(2) against 4D U(1): the commutator potential U = sum |X_i x X_j|^2 is not zero for su(2) and is zero for u(1). So the unprojected winding modes are bound for SU(2) and free for U(1). This is the Lie algebra. Which winding modes are unprojected is the centre convention: with the centre of U(1) (the whole group) in the projector, the U(1) entry is 1, which is >= 457/625.
- 4D against 5D: the one exponent in v h = kappa^(1/3) n^(1 - d/3)/512, d the number of spatial directions. It comes from the volume factor n^d in the harmonic projection. This is the dimension. With s = kappa n a^2 in five dimensions the same proof gives gamma_4 = kappa/n^3 and a five-dimensional entry q_4(kappa^(1/3)/512), which passes for large kappa. So the sign in the 5D entry is a power of n in the chosen magnetic scale.
- The 4D SU(2) entry changes sign with kappa. kappa sets the thermal time of the constant-mode Hamiltonian H against its level spacing. Any Hamiltonian with discrete spectrum and a simple ground state has this crossing. It is a property of an anisotropy parameter of the lattice, not of the Wilson law at a fixed physical size.

Tests of row 1553 (`gap-mech-direction4-fable.md` L188-L193), with F = "the ordered-limit purity is at least 457/625":

- **(g1) FAILS in the consumer's own convention.** The consumer's projector P_0 is on the centre-neutral states (row 1468 3.1). The centre of U(1) is U(1). With that projector the file's own table gives 1 for weak 4D U(1) (L651, proof L679). So F holds in a massless model. F is false for U(1) only with the order-two projector, where the failing line is "the flat winding torus carries free translation modes" (L672-L677).
- **(g2) passes formally**, at the line "v h -> 0 at d = 4" (L668).
- **(g3) FAILS.** The U(1) line fires in the gapped twin 3D compact U(1): the abelian proof at L670-L677 is written for general d and gives P of order a^(-d/2) -> 0 at d = 2 (the file says the same for the iterated limit at L323). The 5D line is a power count with no coupling left in it, because a went to infinity first; it cannot tell a gapped member from a gapless one. Also, the 4D SU(2) entry itself is 0 for small kappa, in a family whose members are all 4D SU(2) Wilson laws.
- **(g4) not informative.** Purities multiply under products, so the product with a factor of ordered-limit purity 0 gives 0, and the product with weak 4D U(1) under its full centre gives q: a model with a massless factor passes F. This is the Lemma ALG situation in the consumer's convention.
- **(g5) FAILS by construction.** The inner limit is a -> infinity on a fixed lattice. The box has physical size zero. Row 1553 asks that the hypothesis fail when the coupling grows on a fixed lattice; here the statement lives only there.
- **(g6) FAILS.** No consumer, no carry. The file says so at L681.

Answer to the brief's question: the difference in (30) is a property of the centre convention, of the Lie algebra (U not zero) and of the dimension (the exponent 1 - d/3). No line of the proof reads the law at a fixed physical size. By Lemma ALG and (g1) it is not an input.

ON FILE, to be credited: the constant-mode quartic Hamiltonian on a small torus is the small-volume Hamiltonian of Luescher (and Koller and van Baal), named in the lane at `gap-solve25-astra62.md` L99 and `gap-direction8-astra62-check-opus.md` L99; row 1227 has its one-vertex spectrum. What Stage 13 adds is a derivation on the full n^3 cube in an anisotropic joint limit, with the exact discrete-time kernel (17). I found no earlier lane text with (17) on the full cube (grep of "sinh", "K_gamma", "gamma n^3" in library/open-core.md and FINISH.md: see Section 8). The file does not name Luescher at Stages 13-17; it should.

### 1.3 Can the consumer use the ordered limit?

No. Three separate reasons, each enough.

1. Ratio. (PUR-io) is at s = a = beta_K. The limit is at s = kappa a^2, so s/a -> infinity.
2. Order and rate. (PUR-io) has a = beta_K of order log n on n = l b^K. The limit needs a -> infinity at fixed n. The constants of Stage 13 (c_n of order 1/n^2, C_n from row 1143 with Q = n^2) give no rate; the windings are concentrated at angle (an)^(-1/2) in the limit and are Haar on the calibrated sequence (file L440, L533; row 1145). So the two regimes are separated by an observable, not only by a missing estimate.
3. At the consumer's ratio the same ordered limit gives the wrong side for 4D SU(2) itself: (15) (L331-L336) gives P of order a^(-3/2)/log a -> 0 at s = a for fixed n, v >= 3, and (21) with gamma = 1/(beta_K n^3) gives 0 (L434). So at s = a the ordered limit gives 0 for all three models.

The checked file states 1-3 itself (L434, L440, L681). Its RESULT line "In the ordered weak limit (30), 4D SU(2) passes the threshold" is true and is not progress on the seed.

### 1.4 Required corrections for claim 1

- C1. L651 and L900: replace "selective" and "law-dependent" by the facts of 1.2: with the consumer's projector, weak 4D U(1) passes; the 5D entry is a power of n; the statement lives at physical size zero.
- C2. L311 and L651: "the strict intermediate value still fails" is true and is not a test. The consumer reads only P >= 457/625.
- C3. Stages 13-17: credit Luescher's small-volume Hamiltonian and row 1227.

- 04:36Z: Section 1 (claim 1) written. Next: claim 2, formula (37).
- (log) inputs read for claims 2 and 3: FINISH rows 1072, 1077, 1108, 1115, 1145, 1146, 863, 1215, 1334 (RESULT text); `gap-bridge-exercise-opus.md` L74-L75, L380, L406-L420; `gap-solve2-astra62.md` L16-L30 (row 1145 (1), (2)).

## 2. Claim 2: formula (37)

Verdict: **HOLDS** (first failing step: none found). **New** as far as my search shows. **Not equivalent to the seed, and not equivalent to BR-2's face leg.** It is not selective: it holds with purity exactly 1 in 5D SU(2) and in weak 4D U(1) under its full centre.

### 2.1 What I redid (ARGUED recomputation; the proofs are the checked file's)

1. Flat density (11) (L237-L261). Around a regular flat field with axis e, a charged momentum p has symbol z_p with |z_p|^2 = 4 sum_i sin^2((2 pi p_i + 2 theta_i)/(2n)). The gauge orbit contributes |z|^2. Two complex normal directions contribute |z|^(-2) each. Product |z|^(-2). Correct. In four spatial directions there are three normal directions, the product is |z|^(-4), and |theta|^(-4) is not integrable at 0 in four variables: the point mass of L263. Correct. Commuting triples in SU(2) lie in one maximal torus, so the flat moduli space is connected; no second component is missed.
2. Uniform density (35) (L809-L814). The one-coordinate product is 2(cosh(n omega) - cos(2 theta_i)) exactly. For p_perp != 0 on the centred grid and |theta_j| <= pi/2, |2 pi p_j + 2 theta_j| >= pi |p_j|, so n omega >= c |p_perp| and the dependence on theta_i sums to a constant free of n. At p_perp = 0, cosh(n omega) - cos(2 theta_i) is comparable to |theta|^2 on the cell. Correct.
3. Lower bound of (36) (L825). The link weight is g_(x+i) . Q_i g_x with Q_i = L(U_i^(-1)) R(V_i) in SO(4); both flat fields can be put on one axis because the vertex integral contains the global rotation. Inversion x -> -x transposes Q_i; (e^x + e^y)/2 >= e^((x+y)/2); the symmetric part of Q_i differs from 1 by at most C(|theta_i| + |theta_i'|)^2/n^2; there are n^3 bonds per direction. Correct.
4. Upper bound of (36) (L827-L832). (i) Dropping a twist: T = M^(1/2) C M^(1/2) is positive, the plane rotation by O_j is unitary and commutes with T because the three rotations commute; so |Tr(T^n R)| <= Tr T^n. Correct. (ii) Gaussian domination (Froehlich, Simon, Spencer; ON FILE in the lane as row 1375 (12)) for the nearest-neighbour O(4) model on the even periodic cube: E exp<f, g^k> <= exp(<f, G f>/(2a)), f of mean zero. The plane-minus-volume test has <f, G f> = n^(-3) sum_(r=1)^(n-1) [4 sin^2(pi r/n)]^(-1) = (n^2 - 1)/(12 n^3) <= 1/(12 n). So P(|m_i - g_bar| > x) <= C exp(-c a n x^2). With t = c a/n^2, ||G|| <= C n^2 and Tr G <= C n^3 give log E exp(t sum |g - g_bar|^2) <= C c n, and sum |g_x - g_bar|^2 = n^3 (1 - |g_bar|^2); so P(|g_bar| < 3/4) <= C exp(-c a n) for a >= a_0. Correct. (iii) Hellinger step: with p = A^2/Z and p' its rotate, the events E and E' are disjoint when delta_i > 0, so the affinity is at most sqrt(P'(E)) + sqrt(P(E^c)) <= 2 sqrt(P(E^c)). Correct. (iv) delta_i >= c | |theta_i| - |theta_i'| | for every centre sign, by the reverse triangle inequality on R/pi Z. Correct.
5. Spectral step (L845-L859). K is positive, K <= C exp(-c sum (|A_i| - |B_i|)^2), Hilbert-Schmidt for mu = |A|^(-2) d^3A with a bound free of n and a; K >= d_R on balls; lambda_1 >= 4 pi d_1. The identity lambda_1 - lambda_2 = (1/2) int int K h h |f/h - f/h|^2 holds (expand, use both eigen-equations, ||f|| = 1). On D^2, K >= (d_R/H_R^2) h(x) h(y), which gives the Gram determinant form. Tails of eigenfunctions with eigenvalue >= l/2 are at most 2 eps_R/l. Correct. So lambda_2/lambda_1 <= r_0 < 1, and 1 - P <= C r_0^(v-2).
6. Why this works (my reading, ARGUED). After s = infinity the Hilbert space is L^2 of three winding angles. One time step ties the angles within (an)^(-1/2). The orbit weight |theta|^(-2) makes a path near theta = 0 heavier, per step, by the factor (an |theta_0|^2) than a path near theta_0. So the top state sits at |theta| of order (an)^(-1/2), with an order-one gap per step. For U(1) the weight is flat, the angles diffuse freely with rate 1/(an) per step, and u/(an) = 1/(512 a) -> 0: purity 0. This agrees with L861.
7. The fixed-K step (L843, L859): at fixed n, u, a the purity is continuous at s = infinity (Stage 10), so P_(n,u)(beta_K, s) > 457/625 for s >= s_0(K). Correct. The file is right that there is no bound on s_0(K). By (38) the winding law has not converged before s >> beta_K n^2 (Section 3), so I expect s_0(K) to be at least a power of n; this last sentence is GUESSED, since (38) bounds the winding law and not the purity.

Not rechecked by me: the Laplace limit on the regular locus beyond the mode count (L261), row 1143 (1), row 1375 (12).

### 2.2 Comparison with statements on file

- **Row 1145, the small magnetic strip** (ON FILE; (22), (25); check 1146): for s in [0, c/(1 + a)], a seed and a gap uniform in the volume, by a block polymer expansion; no SU(2)-specific step. (37) is the other end of the same real axis of s at fixed a. The two are disjoint in range and in method. Row 1145 (24) and row 1334 (22) write the s-derivative of log P as a difference of spatial plaquette means on the u and 2u circles; (37) adds a second base point to that formula, at s = infinity. It adds no bound on the integrand.
- **Row 863 Lemma A2** (ON FILE): s = 0 is seeded at every a. Same end as the strip.
- **BR-2** (ON FILE; rows 1072, 1077, 1108, 1115). BR-2 lives on Z^2 x Z^2 with one plaquette orientation (type L) at infinity. Its face is a system of two-dimensional O(4) sheets coupled by the mixed and transverse plaquettes. Its face leg (FACE-SG) is open beyond the strip beta_T up to about Xi^(-2) (row 1108); its descent (MON-L) is a sign with no mechanism (row 1072 7.3, row 1108); the registry holds BR-2 as blocked-local at (SING) (row 1115).
  (37) freezes the three spatial orientations. Its face is a stack of three-dimensional O(4) layers, one per time step, that talk only through three winding angles. On this face the face statement is easy and is now proved: that is (37). So (37) is the analogue of BR-2's face leg on a different face. It is not (FACE-SG), and neither implies the other (ARGUED: different frozen sets, different surviving fields; (FACE-SG) keeps a two-dimensional non-abelian mass problem, (37) keeps three angles).
  The analogue of (MON-L) for this face is: P_(n,u)(beta_K, s) does not fall below 457/625 as s comes down from s_0(K) to beta_K. Its end point is the seed. So the descent is the seed or stronger. Rows 1072 and 1108 already judged this kind of statement ("a sign of d m/d beta_L ... false in the class"; "contains C_beta and has no mechanism").
- **Is (37) on file?** My greps of FINISH.md for "magnetic coupling", "spatial coupling", "frozen spatial", "flat spatial", "large magnetic", "magnetic tail", "KS-ZONE" give rows 863, 881, 934, 1145-1147, 1334 and this row; none treats s -> infinity at fixed a. `library/open-core.md` has no hit. Row 1215 and row 1227 (10)-(15) treat a fixed cube with both couplings large. So (37), and (35)-(36) behind it, are new in the lane as far as I can see. Section 8 lists the greps.
- **Is (37) equivalent to the seed?** No. It is proved and the seed is open; and the seed at s = beta_K does not give the frozen purity either. (37) does not shorten the seed: the interval between s_0(K) and beta_K has no bound.

### 2.3 Selectivity of (37)

- 5D SU(2): the frozen law is a point; purity exactly 1 (L263, L861). F = (37) holds. (g2) FAILS. The file says this at L861.
- 4D U(1) with its full centre: purity exactly 1 (L861). (g1) FAILS in the consumer's convention. With order-two flips it is 0.
- So the only model that (37) separates from 4D SU(2) is U(1) with a partial centre projector, and the separating line is the orbit weight |theta|^(-2), that is, the dimension of the stabilizer of the central flat field. This is the Lie algebra.

A consequence for claim 7 (ARGUED): 5D SU(2) at weak coupling has both ends of the s-axis seeded as well (the strip proof of row 1145 is a polymer expansion with no step that reads the dimension or the group, check 1146; the frozen end is exact). If 5D SU(2) is unseeded at s = a (BELIEF, row 1531), then no argument that uses only the two seeded ends and properties shared with 5D can reach s = a.

### 2.4 Required corrections for claim 2

- C4. L843 "at least for an above an absolute constant" and "every even n >= 4": keep both; (36) needs even n (reflection) and a >= a_0. On the release sequence n = l b^K is even because 1024 divides l. No change of substance.
- C5. L863 "proves the desired numerical bound on a nonempty tail of the real magnetic-coupling axis": add that the tail starts at an s_0(K) with no bound in K, and that the same sentence is true, with purity 1, for 5D SU(2) and for U(1) with its centre.

## 3. Claim 3: formula (38) and Stage 27

Verdict: **HOLDS** (first failing step: none found).

1. Private links (L875). On the three based lines drop the first and the last bond. A 12-plaquette that contains the 1-link at k e_1 has its 2-links at k e_1 and (k+1) e_1; these lie on the based 2-line only for k = 0 or k = n - 1, which are dropped. Two links of one straight line share no plaquette. An electric plaquette has one spatial link per slice. So no face holds two selected links. A spatial link has four spatial and two electric plaquettes: staple norm at most B = 4s + 2a. Correct.
2. The Bessel ratio bound (L876-L879) is what the proof of row 1145 (1) shows, and that proof is right: R_k = I_(k+1)/I_k obeys R_k' = 1 - (2k+1) R_k/x - R_k^2 (from I_k' = I_(k+1) + k I_k/x and I_(k+1)' = I_k - (k+1) I_(k+1)/x); the positive root of the right side is u_k = -(k+1/2)/x + sqrt(1 + (k+1/2)^2/x^2) = exp(-arsinh((k+1/2)/x)); u_k increases in x; R_k ~ x/(2k+2) < x/(2k+1) ~ u_k at small x; at a first contact R_k' = 0 < u_k', which a contact from below forbids. So R_k < u_k for all x > 0, k >= 1. (This is the upper bound of Amos 1974; recalled, not looked up.) Row 1145 then weakens u_k to exp(-1/(1+x)); Stage 27 keeps u_k. PROVED in row 1145's text; my re-derivation agrees.
3. Product: I_d/I_1 <= exp(-sum_(k=1)^(d-1) arsinh((k+1/2)/x)). With arsinh y >= c min(y, 1) and the terms k >= d/2, the sum is at least c min((d-1)^2/(1+B), d-1) for 0 < x <= B. Correct, also at d = 2.
4. Density: the selected links are V_k W_k with V_k central of multiplier rho_d(x_k) <= rho_d(B) (the multiplier increases in x). The Fourier coefficient of the winding is a unitary times the product of the multipliers. So the density is at most sum_d d^2 rho_d(B)^m, m = n - 2. Below d - 1 = 1 + B this is a Gaussian sum, at most C(1 + ((1+B)/m)^(3/2)); above it, C e^(-cm). Correct.
5. Haar mass of the two balls of radius b/sqrt(an) is at most C b^3 (an)^(-3/2); three conditionally independent windings: (38). Correct.
6. Frozen side (L882): h >= c on |A| <= 1 from the eigen-equation, K >= d_R on D and int_D h >= 3/(4 H_R). mu(|A| <= b) = 4 pi b. Top weight -> 1. So the frozen probability is at least c b. Correct.
7. Conclusions: if s = o(a n^2) the right side of (38) tends to 0 for each b, and the frozen law is tight in A: total variation -> 1. If s <= L_0 a n^2, choose b with C_(L_0) b^9 < c b/2. Correct.

Scale check (ARGUED): a winding is a product of n links, each spread by s^(-1/2) at large s, so its spread is (n/s)^(1/2). This is below the frozen width (an)^(-1/2) only if s >> a n^2. So (38) is sharp in its scale.

What (38) does and does not say: it separates one observable's law. It gives no bound, either way, on the purity for s below a n^2. The file says this at L873.

- 04:42Z: Sections 2-3 (claims 2, 3) written. Next: claim 4 (Stages 2-7, 16-19).

## 4. Claim 4: the affine path, (1)-(9), (22), (27), (28a), (29)

Verdict: **HOLDS** for every PROVED item of Stages 2 to 7 and 16 to 19 (first failing step: none found). One citation note. None of these items is selective, and the file says so (L89, L139, L637).

I re-derived each step below by hand (ARGUED recomputation; the proofs are the checked file's).

1. Stage 2 (L17-L37). For 0 < |t| < 1 and j >= 1 the series of I_j after the factor (t/2)^j/j! has tail at most e^(1/8) - 1 < 1, so no multiplier vanishes; M(t) is invertible. So A(zeta) = T(zeta)^u is not zero where D(zeta) = 0, and A/D has a pole of the order of the zero. N(zeta, conj zeta) = ||A(zeta)||_HS^2 > 0 because A(conj t) = A(t)^*. The map lambda -> h_lambda(zeta) is affine with slope zeta(1 - zeta/beta_K), not zero; so N(zeta, h_lambda(zeta)) is a non-zero entire function of lambda. Correct. This is a weak statement (generic slab deformations have poles) and the file treats it as such.
2. Stage 3 (L44-L87). At t = 0 the 1- and 2-links are Haar-averaged by their electric bonds, the invariant functions are class functions of the n^2 direction-3 holonomies, and a character of dimension j gets rho_j^n. So |k_0 - 1| <= delta = (1 + eta)^(n^2) - 1. Conjugation by M_0 turns T(0)/int M_0^2 into the kernel k_0 on L^2(p) (I checked: B g = C(M_0^2 g)). Weak bonds: 2 n^3 electric traces and two half slices of n^3 magnetic traces give the factor e^(3 n^3 |t|): (2). Rank-one step: ||S||_HS <= ||J(J - Pi)||_HS + ||E(I - Pi)||_HS <= 3d + d(1 + 3d) <= 5d; Tr B^v = lambda^v (1 + e_v) with |e_v| <= (5d/(1 - d))^v. Cauchy on |t| = delta/(12 n^3) gives (1). Correct.
   Citation note C6: row 1145 (1) is stated as I_d(s)/I_1(s) <= exp(-(d-1)/b_beta) for s <= 6 beta. The form used at L63, rho_j <= exp(-(j-1)/(1 + alpha)), is what row 1145's proof gives (u_k(s) <= exp(-1/(1+s))), not its displayed statement. Say so.
3. Stage 4 (L94-L108). k_0' = 0: a first-order term has one weak electric bond between two direction-3 circuits; the sign change g -> -g on one circuit keeps every strong bond and flips that trace. Correct. m_t J m_t / a(t) is an idempotent of norm at most 2. (3), (4) follow. Correct.
4. Stage 5 (L115-L137). In axial gauge along 2 the slice law at t = 0 is a family of independent closed chains along 2 for the 1-links and the 3-links; a rectangle one step wide along 2 is a product of independent central increments, up to the closure factor 1 + O(sum_j j^2 rho_j^(n-1)). Var W_0L -> 1 + 3 e^(-8) - 4 e^(-6) > 0 at L = ceil(2 alpha) (from 1 - rho_2 ~ 3/(2 alpha), 1 - rho_3 ~ 4/alpha); ||W_ab - W_0L||_2 <= C sqrt h. The W_ab are Haar-orthonormal eigenfunctions of the electric product with eigenvalue rho_2(t_*)^2 rho_2(alpha)^(2(b-a)) >= c t_*^2. The quadratic-form inequality passes to L^2(p_*) because <M^2 g, phi>_Haar = (int M^2) <phi, g>_p. Rank-two Gram step: product of the two eigenvalues c q t_*^2 Var Y, sum at most 2. Correct: (5), (6), (7).
5. Stage 6 (L144-L156). Hadamard's three-circle bound for P_v - 1 between r and w, with log(w/r) = (1/2) log(1/delta) + O(log n) and (1 + alpha)(log n)^2/n -> 0, gives (8): v^(-1) log M >= log(b_1 W^2) - o(1). Correct.
6. Stage 7 (L163-L196). Jensen: at most C n^3 v w zeros of F_v, F_2v in |z| <= 4w. The log-derivative splits as sum nu_a/(z - a) + G with |G| <= C n^3 v. p_S H is holomorphic and at most C n^3 v on |z| <= w. Integrating H over [0, t_*] against (6): |S| log(3 w n^3/c') >= v (log(b_1 W^2) - o(1)). Correct. Doublings: b_(j+1) - b_j = (N^+ - N^-)/(2 v_j); a run without many poles raises b_j by c_0/(4 log n) per step and b_j <= C n^3/alpha. Correct.
7. Stage 16 (L446-L488). Evenness: the signs (-1)^(x_1) on 3-links and (-1)^(x_1 + x_2) on 4-links flip exactly the 13, 14, 24 faces (I checked all six orientations; n is even). (23): restrict all links to a ball of radius (1 + alpha + x)^(-1/2). H = L Re z - log|F_v| is non-negative and superharmonic on the right half plane, so the Poisson bound gives the segment integral; log^+|P_v| <= 2H because P_v(0) <= 1 and F_2v has type 2L: (24). G = J_S (P_v - 1) is holomorphic, |G| <= 1 on the real diameter, and the two-constants bound with harmonic measure C w/S gives v^(-1) log^+|G| <= 1/4 on |z| <= w for large B. Each Blaschke factor at t_* is at least c'/(S n^3). So m log(S n^3/c') >= v(log(b_1 W^2) - 1/4 - o(1)): (22). Correct.
8. Stage 18 (L539-L577). f is odd and g is even; on the imaginary axis f is imaginary and g is real (m even, erf(ix) imaginary). The vertex signs (-1)^(x_1 + x_2) negate the weak electric bonds, so the projected electric operator is self-adjoint there; for self-adjoint B and even v, 1/P <= (||B||_HS/||B||)^4. Quadrant step: squaring maps the quarter disk to a half disk; arc measure C (w/S)^2; alpha v w^2/S = v W^2/B. Both counts follow. Correct. This is on modified paths, as the file says.
9. Stage 19 (L585-L635). At t = 0, in axial gauge along 2, the strong faces are transitions of 1-link and 3-link chains along 2 and of 4-link chains along 3 given the 3-links. With Haar anchors every L to 2L steps the weight is prod b_sigma times normalized bridges, |b_sigma - 1| <= eta_L. A cell holds at most 6L segment factors and 12 L^2 weak faces: ||f_C|| <= exp(6 L eta_L + 12 L^2 |t|) - 1. No chain runs along the time axis, so the dependency graph does not see the period. Deletion formula and the bound |Z_A/Z_(A-i) - 1| <= 1/2 on |lambda| <= 2: the standard dependency-graph expansion. Coefficients of degree below c_1 v have supports that do not wrap the time circle; they agree for every twist and double with the period. The rest is at most C n^3 v 2^(-c_1 v). Correct: (28a). (29) follows from Stage 7 with |x - a| >= c/L^2 in place of c/n^3: log(C w L^2) = O(log(2 + alpha)). Correct.

Consistency checks I ran by hand: (6) and (28a) at t_* (the lower bound (b_1 alpha^2 n^(-10))^v/2 is far below C n^3 v e^(-cv)); Stage 6 (failure of bounded continuation at W/alpha) against (28a) (closeness on c/L^2, and 1/L^2 << 1/alpha); (22) against (28a) (the pole disk A n^3 log n/alpha contains the zero-free disk).

What these items give the seed: nothing, and the file does not claim otherwise. (28a) is a statement at |t| <= c/(beta_K log beta_K)^2, a strong-coupling corner in the three weak orientations. The counts (22), (29) show that P_K(t) is not analytic and bounded on a neighbourhood of [0, beta_K] of width above C/beta_K. This answers the question of check 1659 (cancellation of zeros) in the negative for bounded continuation and for exact double cancellation, on the affine path. Selectivity: every step is group-blind and dimension-blind (file L89, L139, L637); I agree.

- 04:46Z: Section 4 (claim 4) written. Next: claims 5 and 6 (Stages 21-24, 28).
