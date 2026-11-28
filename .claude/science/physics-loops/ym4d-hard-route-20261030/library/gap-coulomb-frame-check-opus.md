# Check of row 1042 (library/gap-coulomb-frame.md): row 1044

Started: 2026-11-16T11:30:46Z (date -u).
Provenance: Claude Opus 5.5, max effort, background agent on the lead's MacBook, commit bf8a0f879; same provider as the author (Claude Fable 5.2 medium).
Task: FINISH.md row 1044. Line-by-line check. No new attack. Proofs must be Lean-formalizable; no computer-assisted proof.

## Plan (eight steps; each step appends its result below)

1. Read the file under check and the background files (row 1038 definitions and its two checks, row 1036, row 1043 read, lattice-uhlenbeck, parts/gap). Record the definitions used.
2. Hand tests: the even split q = h^(1/4) on the cube; one value of CUBE-COUL; Lemma SQ on the form 2xy of check 1041.
3. Lemma CG and Lemma UNIQ.
4. Theorem LIP-C (constant 4 (S_1 + S_2)(S_1 + 1) S_2) and why NOLIP of row 1038 does not apply.
5. Lemma CUBE-C, Theorem CUBE-COUL, Lemma LEAD-C.
6. Theorem EXIST with Lemma HIER: Borel covariant selection, connectivity in step (5), discreteness of the exceptional beta set.
7. Proposition LOOP, Lemma SQ, Proposition CURL-P (constant C and field class), the U(1) control.
8. Meaning, verdict table, RESULT line.

## Step results

### Step 1 (done 2026-11-16T11:47:07Z): sources read; definitions used

Read in full: `library/gap-coulomb-frame.md` (the object, 542 lines, as at bf8a0f879), `library/gap-collapse-frame.md` (row 1038),
`library/gap-collapse-frame-check-astra.md` (check 1041), `library/prior/gap-coulomb-frame-read-luna.md` (row 1043).
Read in part: `library/gap-collapse-frame-check-opus.md` (check 1040) Steps 3-6 and its verdict table; `library/gap-boundary-q.md`
(row 1036) Step 2, 4.1-4.5, 5.1-6.3; `library/lattice-uhlenbeck.md` L1-30 (setting, statement of Lemma U, Step 1);
`parts/gap.md` L18-40, L106-115, L144-148 (the wall (W), route (ii) entries). `library/gap-pinned-cell-gauge-max.md` L131-145
(row 1011 3.1, the weights). I did not open row 1045's file.

Definitions used below (all from the sources named).
- SU(2) = unit quaternions, t = Re, s = Im. Link l = (x -> y), head y. Gauge: omega_l -> g_x omega_l g_y^(-1). D_l n = n_x - Ad(omega_l) n_y.
- A link is pinned if it lies in a boundary 3-face (row 1036 Step 2). Weights w_p = 1/(number of cells of the tiling that
  contain p): 1, 1/2, 1/4 (row 1011 3.1). So a plaquette of a 2-face has w_p = 1/4 > 0. (Row 1036 TP4 writes only 1 and 1/2.)
- GR (row 1036 4.1): for lambda on L, the pin curve is omega_eps,l = exp(- eps lambda_y n_x) omega_l exp(eps lambda_y n_y), the frame frozen at
  the base pin, and H_c(omega; (d lambda) n) = (d/d eps)^2 F_c(omega_eps) at 0.
- Hh_0 = K_0 - C_0 is the Hessian of Phi(eta) = F_c((e^(eta_l))_l) at 0; K_0(l, l') = sum_p beta_p w_p xbar_p [p : l][p : l'], xbar_p = 1 on boundary
  plaquettes; C_0 the force covariance at the trivial pin (row 1038 5.1). M_3 = sup of the norm of D^3 Phi on the ball of radius r_0 <= 1
  (check 1041 section 4).
- CUBE-H (row 1038 3.1; HOLDS in checks 1040 and 1041) and CUBE-Z (row 1036 4.2) for the cube.

### Step 2 (done 2026-11-16T11:48:01Z): the three hand tests. All three PASS

All by hand. No machine evaluation is used in this step.

**Test (a): the even split q = h^(1/4) on the cube (object L130-151). PASSES.**
Pin: omega_a = e^((pi/2) i), omega_1 = omega_2 = omega_b = 1. So h = omega_a omega_1 omega_2^(-1) omega_b^(-1) = e^((pi/2) i), phi = pi/2, u = i, q = e^((pi/8) i).
- The gauge of L133 with g_000 = 1: g_100 = q^(-1) omega_a = e^((3 pi/8) i), g_010 = q omega_b = e^((pi/8) i), g_110 = q^(-2) omega_a omega_1 = e^((pi/4) i).
  Then H_a = omega_a g_100^(-1) = q, H_1 = g_100 g_110^(-1) = q, H_b = g_010^(-1) = q^(-1), H_2 = g_010 g_110^(-1) = q^(-1).
  Product H_a H_1 H_2^(-1) H_b^(-1) = q^4 = h. Correct. In general H_2 = q h^(-1) q^2 = q^(-1) because h = q^4 when g_000 = 1 (L141).
- Trace sum 4 cos(pi/8) = 3.695 (to 3 decimals). Tree gauge (all of h on l_2): 3 + cos(pi/2) = 3. Split two-two
  (H_a = H_1 = e^((pi/4) i), others 1): 2 + 2 cos(pi/4) = 3.414. Both are lower. Correct direction.
- Zero divergence (L92): site 000: s(q) + s(q^(-1)) = 0; site 100: out s(H_1) minus in s(H_a) = 0; site 010: s(q^(-1)) - s(q^(-1)) = 0;
  site 110: - (s(q) + s(q^(-1))) = 0. Correct.
- Second variation in one gauge direction: g_100 -> e^(eps v) g_100, v orthogonal to i, |v| = 1. Then H_a -> q e^(- eps v),
  H_1 -> e^(eps v) q. First order: - Re(q v) + Re(v q) = s(q) . v - s(q) . v = 0. Second order: (eps^2/2)(Re(q v^2) + Re(v^2 q)) = - eps^2 cos(pi/8) < 0.
  A strict local maximum in that direction. Correct.
- The proof's global step, at this pin: the class angle is the distance from 1 on the 3-sphere, so the four class angles
  have sum at least pi/2. If the sum is above pi/2, lowering angles to sum pi/2 raises the cosine sum strictly; so every
  configuration has cosine sum at most the maximum over sum = pi/2, which is 4 cos(pi/8) by the two-step mean inequality
  (cos x + cos y <= 2 cos((x + y)/2) needs x + y <= pi; here all sums are at most pi/2). Equality forces all angles pi/8 and
  equality in the triangle inequality, so the broken path 1, H_a, H_a H_1, ..., h is the unique minimising geodesic
  (0 < phi < pi), and every factor is q. The phrase "lower one angle otherwise" (L137) is a comparison with this numerical
  bound, not a move by a gauge; read that way it is correct.
- Defect with a = j (gamma = pi/2): abs(D_a n) = 2 abs(s(q) x j) = 2 sin(pi/8) = 0.765, the value 2 sin(phi/4) sin(gamma) of L146.

**Test (b): one value of CUBE-COUL (object L153-173). PASSES (two values, so the diagonal and the cross coefficient are both tested).**
Same pin, phi = pi/2, s = i, t = 0, psi = pi/4, c = cos(pi/4) = sqrt(2)/2, colour a = j (gamma = pi/2), A := b_0 + kappa(0).
Ad(e^(theta i)) j = cos(2 theta) j + sin(2 theta) k (direct quaternion product). So u_0 = j, u_1 = Ad(q) j = (j + k)/sqrt(2), u_2 = (j - k)/sqrt(2),
d_1 = (1/sqrt(2) - 1) j + (1/sqrt(2)) k, d_2 = (1/sqrt(2) - 1) j - (1/sqrt(2)) k. s . d_1 = s . d_2 = 0, so the kappa' term of CUBE-H is 0, and t = 0 kills t abs(v)^2.
- theta = (1, 0) (lambda = indicator of 100): CUBE-H gives H_c = A . 2 s . (- u_0 x d_1). u_0 x d_1 = (1/sqrt(2)) j x k = (1/sqrt(2)) i. So H_c = - sqrt(2) A.
  Closed form: - 2 A (1 - c)(1 + 2 c) = - 2 A (1 - 1/sqrt(2))(1 + sqrt(2)) = - 2 A (1/sqrt(2)) = - sqrt(2) A. Equal.
- theta = (1, 1) (lambda = indicator of {100, 010}): bracket - u_0 x d_1 + u_0 x d_2 + d_1 x d_2 = - (1/sqrt(2)) i - (1/sqrt(2)) i + (sqrt(2) - 1) i = - i,
  so H_c = A . 2 . (i . (- i)) = - 2 A. Closed form: - 2 A (1 - c)[(1 + 2c) 2 - 2c] = - 4 A (1 - c)(1 + c) = - 4 A sin^2(pi/4) = - 2 A. Equal.
- Side values of the proof (L168): s . (a x d_1) = sin(phi) sin^2(gamma) sin(psi) = 1/sqrt(2), and s . (d_1 x d_2) = 2 (1 - 1/sqrt(2))(1/sqrt(2)) = sqrt(2) - 1. Both agree.

**Test (c): Lemma SQ on the form 2xy of check 1041 (object L432-437). PASSES.**
q(x, y) = 2 x y on R^2, X = the x-axis, Y = the y-axis. The polar form is q((x, 0), (0, y)) = x y. So A = 0, B = 1, and
q((0, y)) = 0: the best m is 0, and SQ needs m > 0. SQ gives nothing, as it must: q((x, y)) = 2 x y is not at most C x^2 (take y large).
Perturbed form q_m = 2 x y - m y^2: then A = 0, B = 1, and SQ gives q_m <= x^2/m. Direct maximisation over y (at y = x/m) gives
exactly x^2/m. So SQ is sharp here. Correct, and it is the answer to the remark of check 1041 (C4): the strict sign m > 0 on Y
is what controls the mixed term.

### Step 3 (done 2026-11-16T11:49:24Z): Lemma CG, Definition COUL, Lemma UNIQ (object L63-121). CG HOLDS; UNIQ HOLDS AFTER CORRECTION of one constant

**Lemma CG (L63-85). HOLDS; one sentence of the proof of (d) needs a wording fix.**
- (a) Ad(omega_l) n_y = Ad(omega_l g_y^(-1)) a and omega_l g_y^(-1) = g_x^(-1) H_l, so D_l n = Ad(g_x)^(-1) (a - Ad(H_l) a). With
  abs((1 - Ad(h)) a)^2 = 4 (abs(s)^2 - (s . a)^2) = 4 abs(s x a)^2 (check 1041 section 1) and abs(H - 1)^2 = (1 - t)^2 + abs(s)^2: the chain of (a). Correct.
- (b) g_x exp(- eps lambda_y n_x) g_x^(-1) = exp(- eps lambda_y Ad(g_x) n_x) = exp(- eps lambda_y a), and the same at y. So the GR curve in the frozen
  gauge g is T_(eps lambda) H. T_theta T_theta' = T_(theta + theta') (one axis a); conjugation keeps Haar measure; for k_x = e^(phi_x a)
  everything on the axis a commutes, so T commutes with these gauge maps. Correct.
- (c) F_c(omega^g) = F_c(omega) for a gauge g on the pinned sites (row 1036 Step 2). So F_c(omega_eps) = F_c(T_(eps lambda) H) and
  H_c = Hess f_H(0)[lambda, lambda]. Correct. It needs only that g is frozen at the base pin, as GR does.
- (d) Existence of g_x with Ad(g_x) n_x = a: SO(3) is transitive on the sphere. Uniqueness up to the stabiliser circle of a: correct.
  Covariance: if n(omega^k) = Ad(k) n(omega), then g(omega^k) = r g(omega) k^(-1) with r_x fixing a, so H(omega^k) = H(omega)^r. Correct.
  The converse: correct.
  Wording fix. The proof says: "the constant c = g_x k_x g_x^(-1)". For k in the stabiliser of omega, c_x := g_x k_x g_x^(-1) is in the
  stabiliser of H, and Ad(c_x) a = a at every site; but c_x need not be constant in x (on a tree graph, with H not 1 on a link,
  non-constant stabiliser elements exist). What is true, and what the row uses (2.2, 5.2): every CONSTANT c that commutes with all
  H_l gives k := g^(-1) c g in the stabiliser of omega, so Ad(c) a = a. Corrected text for L77 and L82-83: "a is fixed by every constant
  c that commutes with all H_l (start from c and put k := g^(-1) c g)".
- The Reading (L84-85): correct. By (d) every pin-measurable frame is a constant colour in a gauge that can be chosen
  measurably (a measurable section of SU(2) -> S^2 exists); the class is the gauge condition.

**Definition COUL (L87-101). HOLDS as a definition; one remark needs its scope.**
- The stationarity condition (L92-93): out of x, t(e^(eps v) H_l) has derivative Re(v H_l) = - v . s(H_l); into x, t(H_l e^(- eps v)) has
  derivative - Re(H_l v) = v . s(H_l). So sum out s(H^C_l) = sum in s(H^C_l). Correct.
- The left constant and "a as extra data" (L95-98): correct. No covariant a on the pure-gauge orbit: correct (every constant fixes 1).
- Scope of L99-100 ("at a reducible pin, a must lie on the common axis; then D n = 0"). This needs H^C to be abelian along one axis.
  That holds where the maximiser is unique up to the left constant: if k fixes omega, then g k^(-1) is again a maximiser, so
  g k^(-1) = c g with c constant, so the stabiliser of H^C is constant and H^C lies in one circle subgroup. This covers the cube
  (h != -1) and the set of UNIQ, which are all the uses. At a reducible pin with copies it is not shown. Add "(where the
  maximiser is unique up to the left constant)". A null set; nothing below depends on it.

**Lemma UNIQ (L103-116). HOLDS AFTER CORRECTION: the last displayed factor is 0 at eps = eps_G.**
Line by line.
- M(g) >= M(1) with t = 1 - abs(. - 1)^2/2 gives sum abs(K_l - 1)^2 <= sum abs(omega_l - 1)^2 <= N eps^2. Correct.
- abs(g_x - g_y) = abs(g_x g_y^(-1) - 1) and g_x g_y^(-1) = K_l (g_y omega_l^(-1) g_y^(-1)), so abs(g_x - g_y) <= abs(K_l - 1) + abs(omega_l - 1) <= (sqrt(N) + 1) eps. A path from o has at
  most V - 1 links: abs(g_x - 1) <= delta. Correct.
- abs(g'_x g_x^(-1) - 1) <= 2 delta and 2 sin(abs(v)/2) >= (2/pi) abs(v) on [0, pi] (Jordan) give abs(v_x) <= pi delta. Correct.
- phi'(0) = phi'(1) = 0 (both are maximisers, hence critical; M(c g) = M(g) makes the constraint g_o = 1 harmless). Correct.
- phi''(t) = sum Re(v_x^2 K(t) - 2 v_x K(t) v_y + K(t) v_y^2): direct. At K = 1 it is - abs(v_x)^2 + 2 v_x . v_y - abs(v_y)^2 = - abs(v_x - v_y)^2.
  The rest is at most abs(K(t) - 1)(abs(v_x) + abs(v_y))^2. Correct.
- abs(K_l(t) - 1) <= sqrt(N) eps + t abs(v_x) + t abs(v_y) <= sqrt(N) eps + 2 pi delta. Correct.
- abs(v_x)^2 <= V sum abs(v_x - v_y)^2 (Cauchy-Schwarz on a path) and sum (abs(v_x) + abs(v_y))^2 <= 2 d sum abs(v_x)^2 <= 2 d V^2 sum abs(v_x - v_y)^2. Correct.
- FIRST FAILING LINE (L114): "phi'' <= - (1 - 32 d V^3 sqrt(N) eps) sum abs(v_x - v_y)^2. This is negative unless v = 0". With eps = eps_G =
  1/(32 d V^3 sqrt(N)) the factor is exactly 0, so the displayed chain gives phi'' <= 0 only, and phi'(0) = phi'(1) is no contradiction.
  Repair (it uses slack already in the proof): sqrt(N) + 1 <= 2 sqrt(N) and V >= 1 give sqrt(N) eps + 2 pi delta <= (1 + 4 pi V) sqrt(N) eps
  <= (1 + 4 pi) V sqrt(N) eps < 14 V sqrt(N) eps. Then phi'' <= - (1 - 28 d V^3 sqrt(N) eps) sum abs(v_x - v_y)^2, and the factor is at least
  1 - 28/32 = 1/8 at eps_G. The graph is connected and v_o = 0, so v != 0 gives a non-zero sum, and phi'(1) - phi'(0) < 0. The lemma then
  HOLDS as stated. Corrected text for L112-114: "abs(K_l(t) - 1) <= sqrt(N) eps + 2 pi delta < 14 V sqrt(N) eps ... phi'' <= - (1 - 28 d V^3 sqrt(N) eps) sum ...,
  and 1 - 28 d V^3 sqrt(N) eps_G = 1/8 > 0". (Equivalently keep 16 and state the hypothesis with a strict inequality.)
- Continuity: the constraint set {g : g_o = 1} is one compact set, M is jointly continuous, and the maximiser is unique; a
  unique maximiser is then continuous (Berge). Correct. Uniqueness also transfers along the gauge orbit: if omega = omega'^k, the
  maximisers for omega are (maximisers for omega') k^(-1), and the left constant is fixed by g_o = 1.
- The use in LOOP (L383-384): the proof needs, for both points, abs(g_x - 1) <= delta and sum abs(K_l - 1)^2 <= N eps^2, and criticality.
  g = 1 at a pin of zero divergence with abs(omega_l - 1) <= eps has all three. So "the proof applies to two critical points" is correct.
- Credit (L218-224): the gauge condition is credited to Zwanziger through row 1043's reading; I did not fetch the sources.

**Selection off the UNIQ set (L117-121).** ARGUED in the object. It is the same construction as EXIST step (4); see Step 6.
The sentence "Nothing below uses copies" is correct: EXIST does not use frame COUL; LOOP is inside the UNIQ set; the cube
is in closed form.

### Step 4 (done 2026-11-16T11:50:06Z): Theorem LIP-C and NOLIP (object L236-265). (i)-(iii) HOLD with C_F = (S_1 + S_2)(S_1 + 1) S_2; the title HOLDS AFTER CORRECTION

**(i)-(iii) HOLD.**
- (i): abs(H - 1)^2 = 2 (1 - t(H)), so maximising sum t is minimising sum abs(H_l - 1)^2 over the gauges on F. Correct.
- (ii), first two inequalities: CG (a) on each link. Third: (i) with the comb-tree gauge of row 1038 4.3, which is a gauge on F. Correct.
- Fourth (the constant). LIP-TREE with LAD gives abs(H^T_l - 1) <= sum over Sigma_l of abs(U_p - 1), abs(Sigma_l) <= S_1 + S_2 (HOLDS in checks 1040
  and 1041). Cauchy-Schwarz: abs(H^T_l - 1)^2 <= (S_1 + S_2) sum over Sigma_l of abs(U_p - 1)^2. abs(U_p - 1) is a class function, so the gauge does not matter.
  Multiplicity, with the ladders of check 1040 Step 3: a (1, 2)-plaquette ((j, x_2, x_3); 1, 2) is in Sigma_l only for l = ((x_1, x_2, x_3), 2) with x_1 > j,
  at most S_1 links; a (1, 3)-plaquette the same; a (2, 3)-plaquette ((0, k, x_3); 2, 3) only for l = ((x_1, x_2, x_3), 3) with x_2 > k and any
  x_1 in {0, ..., S_1}, at most (S_1 + 1) S_2 links; (2, 3)-plaquettes with x_1 > 0 are in no Sigma_l. The maximum is (S_1 + 1) S_2 >= S_1. So
  sum_l abs(H^T_l - 1)^2 <= (S_1 + S_2)(S_1 + 1) S_2 sum_p abs(U_p - 1)^2 = C_F sum_p abs(U_p - 1)^2. The constant HOLDS.
- abs(U - 1)^2 = 2 (1 - t) <= 2 (1 - t^2) = 2 abs(s)^2 for t >= 0. Correct.
- (iii): one term of the sum of (ii) is at most the sum. Correct.

**Title (L236), "the Coulomb frame minimises the defect in mean square": FAILS as written; HOLDS AFTER CORRECTION.**
What (i) proves is that the Coulomb gauge minimises sum abs(H_l - 1)^2, which bounds the defect (4 times it bounds sum abs(D_l n)^2). It does
not minimise the defect itself. Counterexample on the cube, from the object's own closed forms (3.2): with the same colour a at 000
at angle gamma to the axis u, frame COUL has sum abs(D_l n)^2 = 16 sin^2(phi/4) sin^2(gamma) and frame TREE has 4 sin^2(phi) sin^2(gamma). As phi -> pi the first
tends to 8 sin^2(gamma) and the second to 0. Corrected title: "(the Coulomb gauge minimises sum abs(H_l - 1)^2 on the face, a bound for the
defect; range and constant written)". L251-252 already say this correctly ("COUL is the minimiser of the left side of (i)").

**NOLIP does not apply (L248-249). HOLDS.** NOLIP needs a set N and sites x in N, x' with (L1) n_x reads only links inside N and
(L2) n_x' reads no link inside N. For COUL every n_x is Ad(g_x)^(-1) a with g a maximiser over the whole face, and a reads the base
site; so for any N that contains a link of F, (L2) fails, and for any other N, (L1) fails (n_x reads links of F that are not
inside N). Precisely: NOLIP applies only to a rule shown to satisfy (L1)-(L3); COUL is defined by a maximisation over the whole
face and nobody has shown it independent of the links outside a proper N (it is not expected to be). So NOLIP (C6) says nothing
about COUL as defined, and
there is no conflict between LIP-C (a stencil of the whole face) and NOLIP (fixed range). "PROVED by inspection" is a fair mark.

**The rest of 4.1-4.2.**
- "Not uniform in S" (L250-252) and "the same mean-square bound holds for frame TREE" (it is the middle term): correct.
- The description of Lemma U (L253-256): checked against `library/lattice-uhlenbeck.md` L7-23. It is a 4D box, the gauge delta a = 0 with
  a = log U, sup abs(a) <= C_U ||theta|| with C_U absolute, "Not reviewed" in that file. The object's description is accurate. For the 3D face
  and the maximal-trace gauge it is OPEN, as stated.
- L257-258 (a fixed-distance bound expected false): ARGUED in the object. Not checked.
- 4.2 (L264-265): on the UNIQ set, sum abs(H^C_l - 1)^2 <= sum abs(omega_l - 1)^2 in the near gauge, so abs(D_l n) <= 2 abs(H^C_l - 1) -> 0 at pure gauge, for
  every unit a. Correct.
- The cube defect (3.2, L146-151): 2 abs(s(q) x a) = 2 sin(phi/4) sin(gamma); sin(phi) - sin(phi/4) = 2 cos(5 phi/8) sin(3 phi/8) >= 0 exactly for phi <= 4 pi/5;
  abs(U_p - 1) = 2 sin(phi/2) >= 2 sin(phi/4) for all phi in [0, pi]; TREE's sum 4 sin^2(phi) sin^2(gamma) is four times COUL's at small phi.
  All correct.

### Step 5 (done 2026-11-16T11:51:20Z): Lemma CUBE-C, Theorem CUBE-COUL, the cube Q (3.4), Lemma LEAD-C (object L130-201, L277-295). All HOLD

**CUBE-C (L130-144). HOLDS** (test (a) of Step 2 at one pin; here in general).
- Given g_000, the three other g's choose H_a, H_1, H_2^(-1) freely, and H_b^(-1) is fixed by the product g_000 h g_000^(-1). So the problem is: maximise
  sum cos(phi_i) over four factors with product conjugate to h. The class angle is the distance from 1 for the bi-invariant metric, so
  phi <= sum phi_i (left invariance and the triangle inequality along 1, A, AB, ABC, ABCD).
- For any admissible angles: if sum phi_i > phi, lowering angles to sum phi raises sum cos strictly (cos decreases on [0, pi]);
  and for sum = phi <= pi the two-step mean inequality gives at most 4 cos(phi/4), with equality only at phi_i = phi/4 (cos(phi/4) > 0).
  So the maximum is 4 cos(phi/4) (attained by the even split) and every maximiser has phi_i = phi/4 and equality in the triangle
  inequality. For 0 < phi < pi the minimising geodesic from 1 to the conjugated h is unique, the one-parameter group of its axis,
  so the four factors are e^((phi/4) u'). The g's of L133 solve it (checked in Step 2 for one pin; in general H_2 = q h^(-1) q^2 = q^(-1)).
- h = 1: the maximum 4 forces all H_l = 1. h = - 1: every great semicircle is minimising, so the axis u' is free (a two-sphere of
  copies). Correct. "Unique for h != - 1" means unique up to the left constant. Correct.
- The frame vectors (L143-144): n_x = Ad(g_x)^(-1) a with the g's of L133; moved to 000, u_1 = Ad(omega_a) n_100 = Ad(q) a, u_2 = Ad(q^(-1)) a; Ad(q) turns
  about u by phi/2. Correct.

**CUBE-COUL (L153-177). HOLDS.** Re-derived in full from CUBE-H.
- a = cos(gamma) u + sin(gamma) e, f = u x e: Ad(q) a = cos(gamma) u + sin(gamma)(cos(psi) e + sin(psi) f), so d_1, d_2 are as in L166. s = sin(phi) u, so s . d_i = 0.
- a x d_1 = sin(gamma)[cos(gamma)(cos(psi) - 1) f - cos(gamma) sin(psi) e + sin(gamma) sin(psi) u], so s . (a x d_1) = sin(phi) sin^2(gamma) sin(psi); a x d_2 is the same with
  sin(psi) -> - sin(psi). d_1 x d_2 = 2 sin^2(gamma)(1 - cos(psi)) sin(psi) u. abs(v)^2 as in L169. All four lines of L168-169 agree.
- Insert in CUBE-H (t = cos(phi)): the display L170. Coefficient of theta_1^2: 2 (1 - c) cos(phi) - 2 sin(phi) sin(psi) with cos(phi) = 2c^2 - 1 and
  sin(phi) sin(psi) = 2 c (1 - c^2): = - 2 (1 - c)(1 + 2c). Coefficient of theta_1 theta_2: 2 cos(phi)[sin^2(psi) - (1 - c)^2] + 4 sin(phi) sin(psi)(1 - c) =
  4 (1 - c)[c cos(phi) + sin(phi) sin(psi)] = 4 (1 - c) cos(phi - psi) = 4 c (1 - c). So the closed form of L156 HOLDS.
- Eigenvalues of [[1 + 2c, - c], [- c, 1 + 2c]]: 1 + c and 1 + 3c, positive since c = cos(phi/2) >= 0. (i)-(iv) follow. (ii) needs h != 1
  (c < 1), sin(gamma) != 0 and b_0 + kappa > 0. Near the trivial pin 2 (1 - c) = phi^2/4 + O(phi^4): L164 HOLDS (the error is even O(phi^2)).
- Relation to TUNE (L174-177): for a orthogonal to u, Ad(q) a = cos(psi) a + sin(psi)(u x a), and w = s x u_0/abs(s) = u x a; so COUL is TUNE
  with u_0 = a, alpha = phi/2, sigma = + 1; equal closed forms when b_0 + kappa > 0. Correct. t'(0) = - s . v = 0: the velocity is tangent
  to the level set of F_c, as C11 says.

**The cube Q with the best constant (3.4, L179-191). HOLDS to leading order** (not on the row's list; checked because it is short).
- Hh_0 = (b_0 + kappa)[p_0 : l][p_0 : l'] and C_0 = beta xbar delta - kappa [p_0 : l][p_0 : l']: row 1036 4.3 gives Q (= - E[A'']) and H_c for an
  arbitrary first-order pin velocity b at the trivial pin (its proof uses only t(W_i) and t(h)), so Var(sum b_l . N_l) = beta xbar sum abs(b_l)^2
  - kappa abs(sum [p_0 : l] b_l)^2 for every b. Correct.
- LEAD (or LEAD-C) with [p_0 : l] eta_l = xi on four links: H_c = - 2 (b_0 + kappa) abs(xi_perp)^2 sum over ordered pairs (lambda_l - lambda_l')^2 = - 16 (b_0 + kappa) abs(xi_perp)^2 Vv;
  Var = 4 abs(xi_perp)^2 [beta xbar sum lambda_l^2 - kappa (sum lambda_l)^2] = 4 abs(xi_perp)^2 [beta xbar Vv + 4 (beta xbar - 4 kappa) lbar^2]. Vv = (3 theta_1^2 + 3 theta_2^2 - 2 theta_1 theta_2)/4. Correct.
- A constant c added to lambda changes the GR curve by the gauge map exp(- eps c n) at all pinned sites, so H_c does not change; only the
  extension (hence Var) changes. With c = - lbar: Q = 4 abs(xi_perp)^2 Vv [beta xbar - 4 (b_0 + kappa)] + O(phi^3) (the shifted lambda has sum of squares Vv over the four
  links, so the error is O(phi^3 Vv)). Signs for b_0 = beta/2 and b_0 = 0: correct (xbar < 1; 4 kappa <= beta xbar from C_0 >= 0 on the vector ([p_0 : l])).

**LEAD-C (L277-291). HOLDS** (fixed cell and beta, ball r_0 <= 1, as C8).
- T_theta e^eta = e^(R_theta eta): exp(- theta a) e^eta exp(theta a) = exp(Ad(e^(- theta a)) eta), a turn about a by - 2 theta. On the plane orthogonal to a = i,
  z -> e^(- 2 i theta) z. Norms are kept.
- Taylor step: (d/d eps)^2 Phi(eta(eps)) = D^2 Phi(eta)[eta', eta'] + D Phi(eta)[eta''], abs(eta') <= 2 Lambda r, abs(eta'') <= 4 Lambda^2 r. Replacing D^2 Phi(eta) by Hh_0
  costs M_3 r (2 Lambda r)^2 = 4 M_3 Lambda^2 r^3; replacing D Phi(eta) by Hh_0 eta (D Phi(0) = 0) costs (M_3 r^2/2)(4 Lambda^2 r) = 2 M_3 Lambda^2 r^3. Total 6 M_3, as stated.
  Lambda = max abs(lambda_y) <= abs(lambda)_2.
- Quadratic part: (1/2) Hh_0(R eta, R eta) = const + (1/2) sum Hh_0(l, l') Re(conj(R z_l) R z_l') = const + E_z(- 2 theta), using the block form Hh_0(l, l') I_3
  (colour symmetry, row 1038 5.1 (1)) and u . u' = Re(conj(z) z') in the plane. Its second eps-derivative is 4 Hess E_z(- 2 theta)[lambda, lambda]. Correct.
- At theta = 0: 4 Hess E_z(0)[lambda, lambda] = - 2 sum over ordered pairs Hh_0(l, l')(lambda_l - lambda_l')^2 Re(conj(z_l) z_l'), the H_c line of row 1038 LEAD. The W form of
  L283-284 is the same sum grouped by heads (pairs of heads are ordered). The one-site line L291: correct.
- 5.2 (L293-295): W(y, y') = (b_0 + kappa) times a sum of abs(xi_perp)^2 >= 0 on the cube at the trivial pin. Correct.

### Step 6 (done 2026-11-16T11:54:21Z): Lemma HIER and Theorem EXIST (object L297-370). HIER HOLDS; EXIST HOLDS AFTER CORRECTION

**Lemma HIER (L297-311). HOLDS** (one missing definition).
- E_j = E_(j-1) + r_j Re(e^(- i vartheta_j) g_j): r_i r_j Re(c_ij e^(i(vartheta_j - vartheta_i))) = r_j Re(e^(- i vartheta_j) r_i conj(c_ij) e^(i vartheta_i)), since Re(w) = Re(conj(w)). Correct.
- With r_(i+1) <= q r_i and q <= 1/2: sum over i > m of r_i <= r_m q/(1 - q) <= 2 q r_m, and sum over all i of r_i <= 2 r_1. Then abs(g_j - b_j) <= 2 r_1 c_max <= b_min/2
  when b_j != 0; when b_j = 0, abs(g_j) >= r_m c_min - c_max . 2 q r_m >= r_m c_min/2 with q <= c_min/(4 c_max). So g_j != 0 at every angle. Correct.
- j = 1: the hypothesis for j = 1 is b_1 != 0; E_1 = r_1 abs(b_1) cos(vartheta_1 - arg b_1) has a non-degenerate maximum. Correct.
- Step: d/d theta Re(e^(- i theta) g) = Im(e^(- i theta) g), d^2/d theta^2 = - Re(e^(- i theta) g) = - abs(g) at theta = arg g. The Jacobian at r_j = 0 is block lower
  triangular with blocks Hess E_(j-1) (invertible) and - abs(g_j) != 0. The implicit function theorem gives a curve of zeros; for r_j > 0 a zero
  is a critical point of E_j. Hessian blocks A + O(r_j), r_j v, - r_j (abs(g_j) + o(1)); Schur complement - r_j abs(g_j)(1 + o(1)) - r_j^2 v^T (A + O(r_j))^(-1) v.
  The second term is >= 0 (A is negative definite) but of order r_j^2, so the complement is negative for small r_j > 0. Correct as written.
- Missing definition: if all c_ij are 0, c_min is not defined; put c_min := 1 then (q is then any number <= 1/4; every b_j is non-zero by
  the hypothesis, and the case b_j = 0 does not occur). Not a gap in the mathematics.

**Theorem EXIST, steps (1)-(3) (L325-334). HOLD.**
- (1) BFS from ground: each y_j has a neighbour that is ground or some y_i with i < j, so a non-zero block of Hh_0. b_j and c_ij are
  sesquilinear forms with non-zero real matrices; each zero set {b_j = 0} or {c_ij = 0} is a proper real-algebraic set, and finitely many
  of them miss a common point. Grouping E_z by heads: the G-y_j terms give r_j Re(e^(- i vartheta_j) b_j) (the two orders are equal because
  Hh_0 is real symmetric); the y_i-y_j terms give r_i r_j Re(c_ij e^(i(vartheta_j - vartheta_i))); same-head and G-G terms are constant. So E_z = E + const.
  Correct. The ground is what breaks the shift symmetry vartheta -> vartheta + const on Y, so a non-degenerate maximum can exist.
- (2) z(rho eta) = rho z, so Hess E_(rho z) = rho^2 Hess E_z. f_(H*)(theta) = f_H(theta + theta*) (T is a group action), so Hess f_(H*)(0) = Hess f_H(theta*). LEAD-C at
  H = e^(rho eta), theta = theta* = - vartheta*/2: Hess f <= - 4 mu rho^2 abs(lambda)^2 + 6 M_3 rho^3 abs(eta)^3 abs(lambda)^2 <= - 2 mu rho^2 abs(lambda)^2 for rho <= mu/(3 M_3 abs(eta)^3)
  and rho abs(eta) <= r_0. The largest eigenvalue of a finite symmetric matrix is continuous in H, so a closed ball B with Hess f_H(0) <= - mu rho^2 exists. Correct.
- (3) P = the gauge saturation of int B: a union of images of an open set under homeomorphisms, so open; gauge invariant; non-empty.
  CG (c) with any g with omega^g in B gives the bound. Correct. B lies within O(rho) of 1, so P lies in any given neighbourhood of
  the pure-gauge orbit for small rho and small B. Correct.

**Step (4), the Borel covariant selection (L335-341). The argument is correct; it is not Lean-ready as written; a continuous construction replaces it.**
- The canonical representative (L336-339): on Omega_12 := {pins whose tree-gauge holonomies H_(l_1), H_(l_2) are non-central with
  non-parallel axes}, the turn c(omega) (axis of H_(l_1) to i, axis of H_(l_2) into the half plane of i and + j) is unique up to sign and
  continuous; under a gauge k, H -> k_o H k_o^(-1) and c -> c k_o^(-1). With gamma_x(omega) := c(omega) P_x(omega)^(-1): omega^ = omega^gamma is gauge invariant and
  continuous, and gamma(omega^k) = gamma(omega) k^(-1) up to sign. Omega_12 is open, gauge invariant and of full Haar measure (in tree gauge the
  non-tree holonomies are independent Haar elements). All correct.
- The lexicographic minimum (L339-341): the correspondence omega^ -> {g : (omega^)^g in B} has compact values and closed graph, so it is upper
  semicontinuous and measurable for the Effros structure; the map K -> lexicographic minimum of K on compact subsets of R^(4V) is Borel
  (each coordinate minimum is continuous in the Hausdorff metric and each arg-min step is upper semicontinuous). So psi is Borel, and
  g := psi(omega^) gamma(omega) gives n covariant. This is a true standard fact (measurable selection); I did not rebuild it line by line,
  and it is not in a Lean-ready form.
- A continuous replacement (checked here line by line; no selection theorem). Take H0 in int B intersected with Omega_12 (non-empty: int B is
  open and Omega_12 is open and dense) and put g* := gamma(H0)^(-1). Then (H0^)^(g*) = H0 in int B. Let P' := {omega in Omega_12 : (omega^)^(g*) in int B}:
  open (a continuous preimage), gauge invariant (omega^ is), and it contains H0. On Omega_12 put g(omega) := g* gamma(omega) (site by site) and
  n_x := Ad(g_x(omega))^(-1) i. Then omega^(g(omega)) = (omega^)^(g*) (the rule (omega^a)^b = omega^(b a)), so on P' the representative lies in int B and
  H_c <= - m_0 sum lambda_y^2 for every lambda on L. g(omega^k) = g(omega) k^(-1) up to sign, so n is covariant; n is continuous on all of Omega_12,
  a frame defined off a null set. P' is inside P. So EXIST holds with P replaced by P', and step (4) no longer needs the ARGUED mark.
- Wording fix (L317-318): "P minus the reducible pins (a null set)" should read "P minus the null set where the two chosen
  tree-gauge holonomies are central or have parallel axes". That set contains irreducible pins too.

**Step (5), the connectivity (L342-355). HOLDS. The sketch is complete after the fill-ins below; this is the step with the most care.**
- Two distinct links lie in at most one common plaquette. Pinned links of a boundary plaquette p: K_0(l, l') = beta w_p [p : l][p : l'] (xbar_p = 1).
- 2-face criterion (L344): a link (x, mu) has its plaquettes in the directions nu != mu; the plaquette in direction nu is a boundary plaquette
  iff one of the two OTHER transverse coordinates is on the boundary. If two transverse coordinates are on the boundary, every plaquette
  is a boundary plaquette; if only x_kappa is, the plaquette in direction kappa (exactly one lies in the cell) is interior. So the criterion is
  correct. For p in a 2-face, every link of p has two transverse coordinates on the boundary, its staples are made of pinned links,
  N_l is a function of the pin, C_0(l, .) = 0, and Hh_0(l, l') = +- beta w_p = +- beta/4 != 0 for every beta > 0 (w_p = 1/4 by row 1011 3.1; any w_p > 0 suffices).
- p in exactly one 3-face (w_p = 1/2): a link of p not in a 2-face has exactly one transverse coordinate on the boundary, so four boundary
  plaquettes and one interior plaquette (weight 1). At the trivial pin the boundary staples are 1, so N_l = beta Im R (R the interior staple),
  abs(N_l) <= beta, and by isotropy C_0(l, l) = (1/3) E abs(N_l)^2 <= beta^2/3. Cauchy-Schwarz: abs(C_0(l, l')) <= beta^2/3. A link of p that lies in a 2-face has
  C_0(l, .) = 0. So abs(Hh_0(l, l')) >= beta/2 - beta^2/3 > 0 for 0 < beta < 3/2. Correct.
- Edge lemma (L348-351): let (y, nu) be pinned, lying in the face kappa_0. Option 1 (mu outside {nu, kappa_0}, y_mu >= 1): (y - e_mu; mu, nu) has the transverse
  coordinate kappa_0 on the boundary. Option 2 (mu = kappa_0, y_kappa_0 = S_kappa_0, another transverse coordinate on the boundary): also a boundary
  plaquette. Option 1 fails only if the two transverse coordinates other than kappa_0 are 0; then option 2 fails only if y_kappa_0 = 0;
  so both fail only when all three transverse coordinates are 0, that is on an axis through 0. The plaquette's links (y - e_mu, mu) and (y, nu) have heads y and
  y + e_nu, the two ends of (y, nu). So every pinned link off the four axes joins its two ends in the (CONN) graph (U merged into ground). Correct.
- Graph fact (L351-355). Let y != 0 be a boundary site off the four axes; it has at least two non-zero coordinates. If some y_kappa = 0, then in
  the face kappa all non-zero coordinates of y are face coordinates, at least two of them. If no coordinate is 0, y lies in an upper face
  and its three face coordinates are non-zero. So y has two or more non-zero face coordinates in some face that contains it.
  In one face these sites are joined to (1, 1, 1) of that face by links between
  such sites (raise the one zero to 1, then lower each coordinate to 1; all sides are at least 2); such links are off the axes (an axis link
  has at most one non-zero coordinate at each end). Two faces kappa != kappa' share the site with x_kappa, x_kappa' at their face values and the other two
  coordinates 1, which has at least two non-zero face coordinates in both faces; the face graph of the eight faces is connected
  (opposite faces through a third). An axis site t e_nu (t >= 1) has the off-axis pinned link (t e_nu, mu) to t e_nu + e_mu, which has two non-zero
  coordinates. U contains (1, 1, 1, S_4) (S_mu >= 2). So the boundary minus 0, with the off-axis pinned links, is connected, and (CONN) holds for
  0 < beta < 3/2. Correct.
- GUIDE (it proves nothing): one pure-Python run, `python3 -I`, OPENBLAS_NUM_THREADS = OMP_NUM_THREADS = 1, 2026-11-16T11:51:55Z (`date -u`),
  0.46 s, 16 MB. Script and output: `/tmp/r1044.Tfijyg/conn_guide.py`, `conn_guide.out` (not committed). It tests on the 16 boxes with sides in
  {2, 3} and on (4, 2, 3, 2), (2, 5, 2, 4): (F1) a pinned link into every boundary site except 0, none into 0; (F2) the 2-face criterion; (F3) the
  edge lemma; (F4) connectivity of the boundary minus 0 with the off-axis links, U non-empty; (F5) connectivity of Y + ground with all
  pairs of distinct pinned links in one boundary plaquette. All 18 boxes pass every test. The numeric lock was not used (no BLAS, no
  numerics, under one second); I record that as a deviation from the lane's lock habit.

**Step (6), whether the exceptional set of beta is discrete (L356-358). HOLDS, and a slightly stronger statement is true.**
- Z_c(beta) = int exp(beta sum_p w_p t_p) over a compact group: an entire function of beta, with all pin-derivatives entire too, and Z_c >= exp(- abs(beta) sum w_p) > 0
  for real beta. So Hh_0(l, l'; beta) = K_0 - C_0 (a combination of ratios with denominators powers of Z_c) is real analytic on all of R.
- Each Hh_0 used in (5) is non-zero on (0, 3/2), so not identically zero on R, so its zero set has no accumulation point in R (identity
  theorem). D := the union of the zero sets in (0, infinity) of the finitely many pairs of (5). D is closed and discrete, has no
  accumulation point in R (also not at 0 or at 3/2), does not meet (0, 3/2), and meets [2.3, 2.6] in finitely many points. Outside D the same
  edges exist, so (CONN) holds, and steps (1)-(4) use nothing else that depends on beta (M_3, r_0, mu, rho are chosen at fixed beta).
- What is not known: whether D is empty; whether D is bounded; any point of [2.3, 2.6] outside D by name (no Hh_0 value is computed).
  The true exceptional set of (CONN) is a subset of D. "Really discrete": yes.

**The statements "What EXIST is" (L359-370). HOLD.** Existential quantifiers: correct. The frame is not COUL: correct (it is the colour i in a
gauge that brings the pin into B). "Strict maximum of F_c on a torus orbit (to second order)": correct with the qualifier (the gradient
of f_H at theta* vanishes at order rho^2 and is O(rho^3)). (O2) not proved, since Var(Psi) is of the same order rho^2: correct. Nothing uniform in S; m_0 not a
number; beta not named: correct.

### Step 7 (done 2026-11-16T11:55:12Z): Proposition LOOP, Lemma SQ, Proposition CURL-P, the U(1) control (object L372-473). All HOLD; one wording fix in 7.3

**Proposition LOOP (5.5 (ii), L381-387). HOLDS** (beta < 3/2, one site, frame COUL).
- Zero divergence: on p, s(H_l) = sin(rho)[p : l] xi; at the four corners of p the out-sum minus the in-sum is (x) s_1 + s_4 = 0, (x + e_mu) s_2 - s_1 = 0,
  (x + e_nu) s_3 - s_4 = 0, (y) - (s_2 + s_3) = 0, with s_1 = s_2 = - s_3 = - s_4. Same for p_ref. So g = 1 is critical; by Step 3 (the UNIQ proof for two
  critical points) the pin is its own Coulomb representative for small rho. Correct.
- a: the Coulomb-fixed holonomy of p_ref is e^(4 rho a_0) (the four factors [p_ref : l]-oriented), axis a_0; covariant under the left constant; continuous where
  that holonomy is non-central. Correct.
- LEAD-C with a = a_0: z = rho [p : l] xi on the four links of p, 0 elsewhere (p_ref is parallel to a_0). in(y) = {l_2, l_3, one more face link with z = 0}.
  For lambda the indicator of y, (lambda_l - lambda_l')^2 = 1 exactly for one link in {l_2, l_3} and one in {l_1, l_4}; ordered pairs give the factor 2:
  H_c = - 4 rho^2 sum over i in {1, 4}, j in {2, 3} of Hh_0(l_i, l_j)[p : l_i][p : l_j] + O(rho^3). Each pair lies in p only, w_p = 1/2, so K_0 [p : l_i][p : l_j] = beta/2,
  and abs(C_0) <= beta^2/3 (deep links, Step 6 (5)). So H_c <= - 16 rho^2 (beta/2 - beta^2/3) + O(rho^3) < 0 for beta < 3/2 and small rho, and on an open set by
  continuity of frame COUL on the UNIQ set. Correct. It is one lambda only.

**5.5 (i), (iii), (iv) (L376-380, L388-402).** (i) is a second-order criterion with both alternatives OPEN; I checked only that it is
LEAD-C read for a Coulomb representative (transverse up to O(rho^3)), with "to second order" kept in the negative alternative. (iii)
and (iv) are ARGUED in the object and feed no proof; NOT CHECKED here.

**Lemma SQ (7.1, L432-437). HOLDS.** q(x + y) = q(x) + 2 q(x, y) + q(y) <= A abs(x)^2 + 2 B abs(x) abs(y) - m abs(y)^2 and 2 B abs(x) abs(y) <= (B^2/m) abs(x)^2 + m abs(y)^2.
Two lines, Lean-ready. Hand test (c) of Step 2 shows it is sharp and that m = 0 gives nothing.

**Proposition CURL-P (7.2, L439-451). HOLDS given EXIST; the constant C = (A_0 + 16 A_0^2/m_0)/mu_1 is correct.**
- hh(theta) = (d/ds)^2 F_c(exp(s theta n) omega): F_c'' = - E[A''] - Var(A') along a curve of pins. For hh(d lambda), exp(s (d lambda) n) omega is the GR curve
  followed by the gauge map exp(s lambda n) at the pinned sites (GR (a)), so hh(d lambda) = H_c(omega; (d lambda) n). Correct.
- (a): a plaquette has at most four pinned links; its second derivative is at most (sum abs(theta_l))^2 <= 4 sum theta_l^2 and its first at most sum abs(theta_l);
  a link lies in at most six plaquettes; weights at most 1. So abs(E[A'']) <= 4 . 6 beta abs(theta)^2 and Var(A') <= E[A'^2] <= (6 beta sum abs(theta_l))^2 <= 36 beta^2 N abs(theta)^2.
  A_0 = 24 beta + 36 beta^2 N. Correct.
- (b): abs(d lambda)^2 <= 2 sum_l (lambda_x^2 + lambda_y^2) <= 2 . 8 sum_y lambda_y^2 (lambda = 0 on U and at 0; at most eight pinned links at a site); EXIST gives
  hh(d lambda) <= - m_0 sum lambda_y^2 <= - (m_0/16) abs(d lambda)^2. lambda -> d lambda is injective on R^Y (the boundary is connected and lambda = 0 on U). The corner value
  lambda_0: all links at 0 are pinned and point away from 0, and exp(s lambda_0 n_0) on them is a gauge map at 0 that commutes with the move
  (same axis n_0); so hh(theta + lambda_0 d e_0) = hh(theta) exactly, with every mixed term. Correct.
- (c): the norm of the symmetric bilinear form is sup abs(hh(theta))/abs(theta)^2 <= A_0, so B = A_0; SQ with m = m_0/16 gives A_0 + 16 A_0^2/m_0. Correct.
- (d): d o d = 0, so d theta = d theta_c; for theta_c orthogonal to ker d, abs(theta_c)^2 <= (1/mu_1) abs(d theta_c)^2. The decomposition is unique since d lambda is in ker d.
  Correct.
- The field class: ker d on the boundary (homeomorphic to S^3) is the boundary gradients, so (ker d)-perp is the co-exact fields, and the
  class covered is co-exact fields plus gradients d lambda with lambda constant on U.

**7.3 (L453-473). HOLDS after one wording fix.** "The gradients d lambda with lambda not zero on U ... are not in the space of (d)" should read
"with lambda not constant on U": a gradient with lambda equal to one constant c on U is d(lambda - c), and lambda - c is supported on L. The other
bullets: "mu_1 of order S^(-2)" is not proved in the object (ARGUED-level; not checked); the rest restates limits correctly.

**U(1) control (Step 6, L415-428). HOLDS.** One axis, Ad trivial: T_theta is the identity, f_H is constant, H_c = 0; there is no transverse z, so
E_z = 0, every b_j and c_ij is 0, HIER's hypothesis fails, and EXIST's strict conclusion is false for U(1). LIP-C's left side is 0. Gradients are pure
gauge moves for U(1), so the mixed terms vanish and SQ is not needed; the classical curl bound stands (row 1036 7.1). Zero gain: correct.
The strict negative values of SU(2) have no U(1) form because U(1) has no direction orthogonal to its axis: correct.

### Step 8 (done 2026-11-16T11:56:53Z): the meaning, the verdict table, corrected texts, limits, RESULT

**The meaning: "(O2-min) settled positively for generic beta by a descent of F_c at special pins, not a stiffness, so the wall (W)
does not move." HOLDS, with these precisions.**
- What is settled: the existential, extension-free form (O2-min), H_c(omega; (d lambda) n) <= - m_0 sum lambda_y^2 for every lambda on L, for one
  covariant frame on one non-empty open gauge-invariant pin set, in one fixed 4D cell. Check 1040 item (3) left exactly this open
  (ORB gave only a closed set of orbit maxima, measure not computed). (O2-min) is necessary only (C3); (O2) itself is not proved.
- "Generic beta": every beta in (0, 3/2) and every beta > 0 outside the closed discrete set D (Step 6). No beta of 2.3 to 2.6 is named.
- "A descent of F_c at special pins": the pins sit, to second order, at non-degenerate maxima of F_c on torus orbits; there every
  boundary-gradient pin curve has velocity tangent to the level set at leading order and lowers F_c at second order. This is
  the mechanism of TUNE and C11. "Not a stiffness": m_0 = mu rho^2 tends to 0 as the pin set approaches pure gauge, the sign comes from the
  position of the pin on its orbit, not from a curl energy, and the companion bound CURL-P has a constant of order A_0^2/(m_0 mu_1).
- "The wall (W) does not move": (W) is the physical-size seed (`parts/gap.md` L18-22). EXIST gives no sign or smallness at the pins that
  carry the measure (N1), nothing for (N2), (N3) or (O1), no classical constant, no upper-face gradients and no tiling. So no step of
  route (ii) toward (W) is discharged. Correct.

**Verdict table.**

| Item (object lines) | Verdict |
|---|---|
| Hand test: even split q = h^(1/4) on the cube | PASSES (Step 2 (a)) |
| Hand test: one value of CUBE-COUL | PASSES at two lambda (- sqrt(2) A and - 2 A at phi = pi/2, a orthogonal to u) |
| Hand test: SQ on 2xy | PASSES (m = 0 gives nothing; 2xy - m y^2 <= x^2/m, sharp) |
| CG (L63-85) | HOLDS; the proof of (d) HOLDS AFTER CORRECTION (start from a constant c in the commutant) |
| Frame COUL (L87-101) | HOLDS as a definition; L99-100 HOLDS AFTER CORRECTION ("where the maximiser is unique up to the left constant") |
| UNIQ (L103-116) | HOLDS AFTER CORRECTION; first failing line L114 (the factor is 0 at eps_G); repaired with the bound 14 V sqrt(N) eps, factor >= 1/8 |
| Selection off the UNIQ set (L117-121) | ARGUED in the object; not rebuilt; not used by any statement |
| CUBE-C (L130-144) | HOLDS |
| Cube defect (L146-151) | HOLDS |
| CUBE-COUL (L153-177) | HOLDS (re-derived from CUBE-H) |
| Cube Q with the best constant (L179-191) | HOLDS to leading order |
| LIP-C (L236-246) | (i)-(iii) and C_F = (S_1 + S_2)(S_1 + 1) S_2 HOLD; the title FAILS as written, HOLDS AFTER CORRECTION |
| NOLIP does not apply to COUL (L248-249) | HOLDS |
| LEAD-C (L277-291) | HOLDS (fixed cell, C8) |
| HIER (L297-311) | HOLDS (define c_min when all c_ij are 0) |
| EXIST steps (1)-(3) | HOLD |
| EXIST step (4), Borel covariant selection | the argument is a true standard fact, not rebuilt; HOLDS AFTER CORRECTION by the continuous construction of Step 6 (P' inside P); null-set wording corrected |
| EXIST step (5), connectivity | HOLDS (fill-ins written in Step 6; GUIDE on 18 boxes, proves nothing) |
| EXIST step (6), D discrete | HOLDS (D closed, no accumulation point in R, empty on (0, 3/2), finite on [2.3, 2.6]) |
| LOOP (L381-387) | HOLDS (beta < 3/2, one lambda) |
| 5.5 (i) | a second-order criterion; consistent with LEAD-C; both alternatives OPEN |
| 5.5 (iii), (iv) | ARGUED in the object; NOT CHECKED |
| SQ (L432-437) | HOLDS |
| CURL-P (L439-451) | HOLDS given EXIST; constant correct; the class is co-exact fields plus gradients of potentials constant on U |
| 7.3 (L453-473) | HOLDS AFTER CORRECTION ("lambda not constant on U") |
| U(1) control (L415-428) | HOLDS; zero gain |
| Meaning (RESULT L542) | HOLDS with the precisions above |

**Corrected texts for the lead (I edited no other file).**
- UNIQ, L112-114: "abs(K_l(t) - 1) <= sqrt(N) eps + 2 pi delta <= (1 + 4 pi) V sqrt(N) eps < 14 V sqrt(N) eps ... Hence phi'' <= - (1 - 28 d V^3 sqrt(N) eps) sum abs(v_x - v_y)^2, and
  1 - 28 d V^3 sqrt(N) eps_G = 1/8 > 0."
- LIP-C, L236: "(the Coulomb gauge minimises sum abs(H_l - 1)^2 on the face, a bound for the defect; range and constant written)".
- CG (d), L77 and L82-83: "a is fixed by every constant c that commutes with all H_l (put k := g^(-1) c g; k fixes omega)".
- COUL, L99: "At a reducible pin where the maximiser is unique up to the left constant, a must lie on the common axis".
- HIER, L302: "(c_min := 1 if all c_ij are 0)".
- EXIST step (4), L335-341, replace by: "Fix a spanning tree and two non-tree links. Omega_12: the pins whose two tree-gauge holonomies are
  non-central with non-parallel axes (open, gauge invariant, full measure). On Omega_12 the canonical gauge gamma (tree gauge, then the turn
  that sends the first axis to i and the second into the half plane of i and + j) is continuous up to sign and gamma(omega^k) = gamma(omega) k^(-1).
  Take H0 in int B intersected with Omega_12, g* := gamma(H0)^(-1), g(omega) := g* gamma(omega), n_x := Ad(g_x)^(-1) i. Then n is continuous and covariant on
  Omega_12, and on P' := {omega in Omega_12 : omega^(g(omega)) in int B}, an open gauge-invariant set that contains H0, the bound of (3) holds." And in the
  Claim, L316-318: "a non-empty open gauge-invariant set P' of pins ... continuous and gauge covariant off the null set where the two chosen
  tree-gauge holonomies are central or parallel". Table L496: "PROVED" (step (4) by this construction); table L486: the
  ARGUED mark stays for the COUL selection of 2.3 only.
- 7.3, L454: "The gradients d lambda with lambda not constant on U".
- The object's proposed `parts/gap.md` text (L531-538): "non-degenerate maxima of F_c on torus orbits (to second order)"; drop "selection ARGUED";
  "on the cube the Coulomb frame with a colour orthogonal to the axis is TUNE with tilt phi/2, and with any colour off the axis it has H_c
  negative definite where b_0 + kappa > 0".
- The lead's current `parts/gap.md` L148 entry: "a curl bound follows on that pin set for lower-face fields only" should read "for co-exact
  boundary fields plus gradients of potentials that are constant on the relative interiors of the upper faces"; "Borel selection ARGUED"
  can read "covariant selection by a continuous construction (check 1044)"; and the check status changes to "checked by the same
  provider (check 1044: UNIQ and LIP-C after correction; EXIST, HIER, LEAD-C, CUBE-COUL, LOOP, SQ, CURL-P HOLD)".

**Limits of this check.**
- Same provider as the author: this is not an independent check in the lane's sense. The cross-provider check (row 1045) was not opened.
- Not checked: 5.5 (iii) and (iv) (ARGUED in the object); the ARGUED expectation of L257-258; mu_1 of order S^(-2) (L457-458); the standard
  measurable-selection fact of step (4) and of L117-121 line by line (the continuous replacement was checked); Lemma U itself (only its
  statement was compared); row 1043's sources (not fetched); the object's GUIDE run (3.6; not re-run); the inputs CUBE-H, CUBE-Z, GR, LEAD and
  row 1036 4.3, which I used as checked by checks 1037, 1040 and 1041 (I re-derived CUBE-COUL from CUBE-H, not CUBE-H itself).
- One GUIDE run (Step 6), combinatorics only; it proves nothing. No Lean run. No commit, no push, no other file edited.
- Revisions: at the end (2026-11-16T11:58:14Z, `date -u`) HEAD was e94da715d, two lead commits after bf8a0f879. `git diff` shows the
  object `library/gap-coulomb-frame.md` unchanged between them, so every line reference above holds. Those commits also change
  `parts/gap.md`; my note on its L148 refers to the text at bf8a0f879. I did not read the new version, nor row 1045's file.

Finished: 2026-11-16T11:56:53Z (`date -u`); last edit (the Revisions note and two reference fixes) at 2026-11-16T11:58:46Z (`date -u`).

RESULT: Row 1044 (Claude Opus 5.5 max, background agent on the lead's MacBook, commit bf8a0f879; same provider as the author, so not independent; by hand, one small combinatorial GUIDE run that proves nothing) checked row 1042 line by line: the hand tests PASS (the even split q = h^(1/4) is the Coulomb gauge of the cube; CUBE-COUL gives - sqrt(2) A and - 2 A at phi = pi/2, equal to CUBE-H; SQ gives nothing for 2xy and is sharp for 2xy - m y^2); CG, CUBE-C, CUBE-COUL, the cube Q, LEAD-C, HIER, LOOP (beta < 3/2), SQ, CURL-P (C = (A_0 + 16 A_0^2/m_0)/mu_1 on co-exact fields plus gradients of potentials constant on U) and the U(1) control HOLD; UNIQ HOLDS AFTER CORRECTION (first failing line L114: the factor 1 - 32 d V^3 sqrt(N) eps is 0 at eps_G; the bound 14 V sqrt(N) eps gives 1/8); LIP-C's bound with 4 (S_1 + S_2)(S_1 + 1) S_2 HOLDS and NOLIP does not apply, but its title "minimises the defect" FAILS as written (it minimises sum abs(H_l - 1)^2; on the cube near phi = pi frame TREE has the smaller defect); Theorem EXIST HOLDS AFTER CORRECTION: its Borel lexicographic selection is a true standard fact but is replaced by a continuous covariant frame on the full-measure set of pins with two non-central non-parallel tree-gauge holonomies, with the strict sign on a non-empty open gauge-invariant P' inside P, so no ARGUED step remains; the connectivity of step (5) is complete after the written fill-ins (GUIDE passes on 18 boxes); the exceptional set D is really discrete (closed, no accumulation point in R, empty on (0, 3/2), finite on [2.3, 2.6], not known to be empty, no beta named); the meaning HOLDS: existential (O2-min), a necessary test only, is settled for beta < 3/2 and beta outside D by a descent of F_c at pins near non-degenerate torus-orbit maxima, not a stiffness, so the wall (W) does not move and (N1), (N2), (N3), (O1), the classical constant and upper-face gradients stay open; not checked: 5.5 (iii)-(iv), mu_1 of order S^(-2), the selection fact line by line, row 1043's sources, the object's GUIDE run.
