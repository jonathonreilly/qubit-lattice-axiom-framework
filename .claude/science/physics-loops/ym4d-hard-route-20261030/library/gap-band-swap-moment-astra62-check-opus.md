# Check of library/gap-band-swap-moment-astra62.md (FINISH row 1583)

Checker: Claude (Opus 5.5). Status: complete.

## Plan

1. Read GOAL.md, FINISH.md Rules and Working efficiently.
2. Read the target note in full; read check 1580 item 3b; rows 1573/1574 circle definitions; row 1576 Theorem 1.2 and check 1582.
3. Check the decisive lower bound: local identity, passage to full moment, plaquette mean in the two regimes, matching upper bound.
4. Check the class covered by (6) and look for an admissible circle outside it.
5. Check the purity and comparison-model section.
6. Verdicts, RESULT line, checker line.

## Steps

Provenance: Claude Opus 5.5, line-by-line check of `library/gap-band-swap-moment-astra62.md` (row 1581, gpt-6.2-astra max) as on disk 2026-11-25 (154 lines). Not an audit. All verdicts by hand; no computation used. Inputs read: GOAL.md; FINISH.md Rules and Working efficiently; check 1580 (`library/gap-band-neutral-fable-check-astra62.md`, items 3b, N1, CO/S2/ROT, Lemma W); row 1573 (`library/gap-band-neutral-astra62.md`, in full); row 1574 (`library/gap-band-neutral-fable.md`, Step 3, Lemma W, NOISE, Attack 3); row 1576 (`library/gap-band-neutral-neon.md`, Theorem 1.2, Proposition 1.3, Section 2 opening) and check 1582 (`library/gap-band-neutral-neon-check-opus.md`, Steps 1-6); cited inputs `library/gap-solve7-astra62.md` (9) and line 332, `library/sa-ym4-lean-trajectory-check-astra62.md` BND-1/BND-2, check 1579 item 11.

### Step 1. Setup and the identity E j^2 = ||G B^(1/2)||_HS^2 / Tr B (lines 19-25) -- HOLDS

- u = 2v, so B^(1/2) = M^(1/2) (x) M^(1/2) with M^(1/2) = T^v or P_0 T^v (P_0 is a projection commuting with T). Its kernel is F(X,Y) = k(x1,y1) k(x2,y2), the L of row 1573. Tr B = (Tr M)^2.
- (G B^(1/2))(X,Y) = -i D_X F(X,Y), so ||G B^(1/2)||_HS^2 = integral |D_X F|^2, and sum_j j^2 Tr(Pi_j B) = ||G B^(1/2)||_HS^2. This is check 1580, item 3b.
- X-marginal of nu: integral F^2 dY = (k o k)(x1,x1)(k o k)(x2,x2), the diagonal of M at period u in each replica. It is invariant under vertex gauges and vertex centre signs of either replica separately, because the kernel is gauge-averaged (and centre-projected) at each end. So a_p = E_nu w_p is the spatial plaquette mean of the periodic (or twist-averaged) torus of period u. HOLDS.

### Step 2. Good plaquettes (line 27) -- HOLDS

- The mate e' of a boundary edge e shares a corner c with e. If its other end were a corner, e' would join two corners of the square, so it would be a boundary edge (diagonal corners are not adjacent), contradicting goodness. So v_e is exterior.
- Distinctness: adjacent corners have no common neighbour (bipartite lattice); diagonal corners have exactly the two other corners as common neighbours. So no exterior vertex is adjacent to two corners. At one corner the two mates are distinct links (each link lies in one dimer), so their far ends differ. With n >= 1024 this holds on the periodic grid.
- Straight dimers (rows 1573/1574): two parallel boundary links do not meet; perpendicular links are never a straight dimer. So every plaquette is good. HOLDS.

### Step 3. Lemma 1 (lines 29-45) -- HOLDS

- Curve. With a(s) = m[cos(theta/2) - sin(theta/2) R_s h] and R_s h = h cos s + (d x h) sin s (h orthogonal to d): (a+b)/2 = m cos(theta/2), (a-b)/2 = -m sin(theta/2) h, adot(0) = -m sin(theta/2)(d x h), addot(0) = (b-a)/2. Matches row 1573 Lemma 1 (first replica m q(s)^(-1)). Inversion is quaternion conjugation, real-linear, so reversed links obey the same rules. HOLDS.
- Mean curvature. w_p is real-multilinear in the four boundary quaternions, each used once, so D^2 w_p = sum_e w_p[addot_e] + sum_(e != f) w_p[adot_e, adot_f]. No same-slot second derivative occurs.
  * Acceleration terms: w_p[(b_e - a_e)/2 in slot e]. The term with b_e alone in slot e has nu-mean zero: a second-replica centre sign -1 at either endpoint of e is a gauge, preserves nu, and reverses the term. So the acceleration terms give (1/2) * 4 * (0 - a_p) = -2 a_p.
  * Cross terms: a second-replica Haar gauge at v_e does not touch any plaquette link (v_e is exterior) or any other mate (Step 2). It makes the mate relative quaternion x'^(-1) g y' (or y' g^(-1) x'^(-1) in the tail-based form) Haar given everything else. Its axis is then uniform, so d is uniform on the great circle orthogonal to h_e, and adot_e (linear in d) has conditional mean zero. The four gauges are independent. So the cross terms vanish. This uses only invariance of nu, not decorrelation. HOLDS.
- Finite-angle identity. Under the auxiliary average, a_e(s) becomes alpha a_e + (1 - alpha) b_e with alpha = cos^2(s/2). Expanding by multilinearity, every nonempty proper subset S of the four-cycle has a vertex of odd S-degree (one edge, two adjacent, two opposite, three edges: all checked). A second-replica sign there reverses the term. So E_nu w_p(A(s)) = [cos^8(s/2) + sin^8(s/2)] a_p. At s = pi/2 this is 2/16 = 1/8. cos^8(s/2) = 1 - s^2 + O(s^4), so the second derivative at 0 is -2 a_p, consistent with the first computation. HOLDS.
- Orthogonality. For p, q with disjoint 8-vertex sets (corners and partners), the four second-replica gauges for p do not touch any link read by D w_q (its plaquette links and mates have endpoints in q's vertex set). Each summand of D w_p averages to zero. HOLDS.

### Step 4. Passage to the full moment, (1) and (2) (lines 47-66) -- HOLDS

- Haar invariance: d/ds of integral (D w_p)(R_s X) F(R_s X, Y)^2 at 0 gives integral (D^2 w_p) F^2 + 2 integral (D w_p) F D_X F = 0. With Lemma 1, (1/Tr B) integral (D w_p) F D_X F = a_p. Differentiation under the integral: bounded speed and acceleration, smooth positive finite-volume kernel.
- Bessel in L^2(dX dY) with orthogonal phi_p = (D w_p) F / sqrt(Tr B), ||phi_p||^2 = b_p, psi = D_X F / sqrt(Tr B), ||psi||^2 = E j^2, <phi_p, psi> = a_p: E j^2 >= sum a_p^2 / b_p. If b_p = 0 then phi_p = 0 and a_p = 0. HOLDS.
- b_p bound: the plaquette product has speed at most 4 (four unit-speed-bounded factors, ROT (v)). The tangent gradient of Re on S^3 at U is 1 - (Re U) U, of squared norm 1 - (Re U)^2. So (D w_p)^2 <= 16(1 - w_p^2) <= 32(1 - w_p), and also <= 16. HOLDS.
- (2): 3n^3 spatial plaquettes, 3n^3/2 dimers, each dimer spoils at most one plaquette (two distinct incident edges lie in at most one elementary square), so at least 3n^3/2 good. Each plaquette's 8 vertices lie in base + [-2,2]^3, so intersecting vertex sets force bases within sup-distance 4: at most 3 * 9^3 plaquettes discarded per choice. |I| >= (3n^3/2)/(3 * 9^3) = n^3/(2 * 9^3). (The count is generous; it is valid as stated.) Works for any fixed matching, bent or straight. HOLDS.

### Step 5. Size of the plaquette mean (lines 68-86)

**5a. Calibrated roots, (3) -- HOLDS (given the imported inputs).**
- Input: row 1155 (9) (`library/gap-solve7-astra62.md`, line 132): E exp{c beta sum_(p in S)(1 - w_p)} <= C^|S| with absolute c, C, on a periodic torus; line 332 of that file states the proof uses only rectangular periodicity and positivity. Jensen with |S| = 1 gives E_per(1 - w_p) <= (log C)/(c beta) =: C_0/beta, independent of the periods. I did not re-check (9) itself; it is cited, not re-derived.
- Projected law: 0 <= P_0 T^u <= T^u (P_0 a projection commuting with T >= 0), so Tr(H^(1/2) P_0 T^u H^(1/2)) <= Tr(H T^u) for the slice insertion H = 1 - w_p >= 0. Z_+(u) = (1/8) sum_z Z^z(u) >= Z^0(u)/8 since every twisted integral is positive. So 1 - a_p <= 8 C_0/beta = C_*/beta in both cases. HOLDS.
- beta >= 2 C_* gives a_p >= 1/2, b_p <= 32 C_*/beta, a_p^2/b_p >= beta/(128 C_*); times |I| gives beta n^3/(256 * 9^3 C_*). Arithmetic HOLDS.
- beta_K -> infinity: BND-1/BND-2 of `library/sa-ym4-lean-trajectory-check-astra62.md` (lines 40 and 107: beta_K in [beta_0, B_0 log(l/a_K)] eventually, for every fixed beta_0). So (3) holds at every sufficiently late K at fixed witnesses. HOLDS.

**5b. Band 2 <= beta <= 3, (4) -- HOLDS.**
- Sign flip at t = 0: multiply by -1 every j-link (all times) with fixed x_i = c. A jk plaquette (k != i, spatial or temporal) at x_i = c contains two flipped j-links; ik plaquettes contain none; twist signs sit on temporal plaquettes and are constants. The ij plaquettes with one j-link at x_i = c are reversed. Haar is invariant under -1. So E_0 w_p = 0 for every ij plaquette, in each twist sector and in the mixture. HOLDS.
- d/dt E_t H_ij = Var_t H_ij in the joint (twist, links) law, since the mixture is one Gibbs measure on (z, links). HOLDS.
- Selected links: j-links at sites with all four coordinates even, V/16 of them. Two j-links in one plaquette differ by one unit in one coordinate, so no plaquette has two selected links. Given twist and all other links they are conditionally independent, and H_ij is a sum of one function of each plus a constant. Each selected link lies in two ij plaquettes, six other links. If these are within chord 1/24 of 1, each staple is within 1/8 of 1, so f(q) is within 1/4 of 2 Re q uniformly; centring is an L^2(Haar) contraction and Var_Haar(2 Re q) = 4 * 1/4 = 1, so the centred Haar norm is >= 3/4. Conditional density >= d = e^(-36) (six terms, |beta w| <= 3 each, ratio e^(-18)/e^(18)), for every twist and t <= beta <= 3. Var_rho f = min_c integral (f - c)^2 rho >= d * 9/16. Repeated conditioning gives the six-link event probability >= (dh)^6. Sum: Var_t H_ij / V >= (1/16)(dh)^6 (9d/16) = (9d/256)(dh)^6. HOLDS.
- Integration over [0, beta] with beta >= 2 gives E_beta H_ij / V >= a_* = (18d/256)(dh)^6. Spatial translation, cyclicity in time, and moving the twist seam by a flat centre flip (which preserves contractible spatial plaquettes) make every spatial ij plaquette mean equal to E H_ij / V. HOLDS.
- (4): a_*^2/16 times n^3/(2 * 9^3) = a_*^2 n^3/(32 * 9^3). HOLDS.

### Step 6. Matching upper bound (5) (lines 88-104) -- HOLDS

- Orthogonality E_nu L_r L_s = 0 for vertex-disjoint dimers r, s. For the summand of L_r that differentiates A_e, a second-replica Haar gauge at the far end t_(e') of the mate e' (a vertex of r, hence not of s) leaves F invariant (F is gauge invariant in each replica separately), leaves the first-replica gradient of log F at e unchanged (differentiate F(A, gA') = F(A, A') in A_e), leaves L_s unchanged (s reads only its own links, none at t_(e'); gradients at links not touching t_(e') are unchanged by the same identity), and makes the mate relative Haar, so the velocity of A_e has conditional mean zero. For A'_e use a first-replica gauge at t_(e'). HOLDS.
- One-link Fisher bound. log F = log k(x1,y1) + log k(x2,y2). A spatial link at the pinned end lies in four spatial plaquettes at weight beta/2 and one temporal plaquette at weight beta, also for v = 1. For a once-occurring link, d^2/ds^2 Re(e^(st) Q) = -Re Q. The second derivative of the log of a positive integral is the conditional mean of the second derivative of the exponent plus a variance, so d_t^2 log F >= -(4 beta/2 + beta) = -3 beta; for the projected kernel, the twist label enters the conditional law and the same bound holds. Haar integration by parts: integral F d_t^2 F = -integral (d_t F)^2, so E_nu d_t^2 log F = -2 E_nu (d_t log F)^2. Hence E_nu (d_t log F)^2 <= 3 beta/2 and E_nu |grad_e log F|^2 <= 9 beta/2. HOLDS.
- E L_r^2 <= 4 * sum_(4 terms) E|grad|^2 <= 4 * 4 * 9 beta/2 = 72 beta (Cauchy-Schwarz, four velocities of norm <= 1). At most six dimers use a vertex, so at most 18 dimers meet r. E(sum L_r)^2 <= sum_r deg(r) E L_r^2 <= 18 * 72 beta * 3n^3/2 = 1944 beta n^3. HOLDS.
- Uniformity: no constant depends on the matching, n or u. So Theta(beta_K n^3) at late calibrated cutoffs and Theta(n^3) uniformly on [2, 3], with and without independent centre projection. HOLDS.

### Step 7. Vacuum and frame choices (lines 106-112) -- HOLDS

- Vacuum: simple top eigenvalue with positive eigenvector; gauge and centre maps preserve positivity and commute with T, so they fix Omega. T trace class, so T^u / lambda_0^u -> projector in trace norm (sum_(j>0) r_j^u <= sum r_j^2 for u >= 2). The bounds on a_p are uniform in u, so they pass to the vacuum; Lemma 1 and (1) apply with probability |Omega_2|^2 dX (product, gauge invariant in each replica). Upper bound: E j^2 = sum_(a,b) lambda_a^u lambda_b^u ||G psi_a (x) psi_b||^2 / (Tr M)^2 >= (lambda_0^u / Tr M)^2 ||G Omega_2||^2, and (5) is uniform in u. Even harmonics: U_pi Omega_2 = Omega_2 o S = Omega_2 a.e. HOLDS.
- Frame variants. A fixed matching, either sense of rotation, or a fixed rotation Q of one link's axis coordinates before forming the normal: the Lemma 1 proof uses only (i) the explicit curve with acceleration (b - a)/2, (ii) uniform azimuth of the partner axis under the exterior gauge (Q a' is still uniform), (iii) speed <= 1. All survive. Note: a fixed Q not commuting with Ad of the vertex gauge breaks the diagonal gauge covariance of the circle. The claim does not need it, and Lemma 1 and (5) do not use it. HOLDS.
- Relative frame of row 1573: for fixed h in the compact group of vertex gauges and centre translations of one replica, U_h commutes with M, so U_h^(-1) U_s U_h has Fourier weights Tr(Pi_j U_h B U_h^(-1)) = Tr(Pi_j B). Fibrewise equality of the whole j-law, hence equality after the Haar average over h. HOLDS. The chart circle and the thermal clock are explicitly left out. This is correct.

### Step 8. Changing the motion within a dimer, (6) (lines 114-138) -- HOLDS

Hypotheses: a fixed perfect matching of spatial links into dimers of two distinct links sharing a vertex; on each dimer a circle acting only on its four raw links, preserving their product Haar law, commuting with simultaneous vertex gauges, equal to the replica swap at pi; coordinates in the L^2 generator domain.
- s_e >= 1/2: along orbits a o R_pi = b, ||b - a||_2^2 = 2 - 2 E(a.b) = 2 under independent Haar, and ||a o R_pi - a||^2 = 4 sum_(j odd) ||a_j||^2 <= 4 ||Da||^2. HOLDS.
- Mean velocity at given (a, b) vanishes. Covariance: R_s commutes with gauges supported at the two ends of e, so Da(gz) = g_1 Da(z) g_2^(-1), and the mate's product Haar law is invariant under the gauge at the shared vertex. So V(a,b) = E[Da | a,b] is left-right equivariant. At a = 1 the stabiliser of b is conjugation about its axis, so V(1,b) is a multiple of Im b; transitivity on {Re b = x} makes the coefficient a function of x alone: V = f(x)(b - x a). The L^2 version by averaging over the compact frame group is correct. By the half-turn, E[Db | a,b] = (Da)(R_pi z) conditioned, = f(x)(a - x b). Then d/ds E H(a(s).b(s)) = 0 gives E[2(1 - x^2) f(x) H'(x)] = 0 for all polynomials H'; (1 - x^2) f is in L^2 (since |f| sqrt(1 - x^2) = |V|), so the signed measure vanishes and f = 0 a.e. HOLDS.
- Curvature. One-difference terms: first- and second-replica gauges at v_e and a second-replica gauge at the far end of e (a corner) make b, c, d independent Haar given the first-replica plaquette links; the corner gauge moves other second-replica links but none that enter this term. Covariance gives E[a(s) | a] = r_e(s) a with r_e real, and r_e(s) = 1 - (1/2) E|a(s) - a|^2 = 1 - s^2 s_e/2 + o(s^2) (generator domain). Two-difference terms: limits w_p[v_e, v_f], zero by the conditional-velocity identity after independent gauges at v_e and v_f. Three and four differences: o(s^2) in L^1 (uniformly integrable product times a bounded factor tending to zero in probability). The bounded finite-box density transfers L^1 limits. So E_nu w_p(R_s X) = a_p - s^2 s_p a_p/2 + o(s^2). HOLDS.
- One derivative on w_p, one transferred to F^2: (1/Tr B) integral (D w_p) F DF = s_p a_p/2. Orthogonality for vertex-disjoint plaquettes as in Step 3. E_nu[|v_e|^2 | first-replica plaquette links] = s_e (|v_e|^2 is gauge invariant; transitive action). (D w_p)^2 <= (1 - w_p^2) |Udot|^2 <= 4(1 - w_p^2) sum_e |v_e|^2, so E (D w_p)^2 <= 4 s_p E(1 - w_p^2). Bessel gives (6). HOLDS.
- Recovery of (3) and (4): s_p >= 2 and E(1 - w_p^2) <= min{1, 2(1 - a_p)} give per-plaquette terms >= beta/(64 C_*) and >= a_*^2/8, better than (3) and (4). HOLDS.
- Speed bound L: orthogonality uses the conditional-velocity identity after averaging both replicas at the mate's far vertex; the count gives 1944 L^2 beta n^3. HOLDS.

### Step 9. The class covered, and admissible circles outside it

**Covered (each checked above):**
- Dimer patterns: any fixed perfect matching of spatial links into pairs of distinct links that share a vertex, straight or bent. Every plaquette is good for straight dimers. For bent dimers at least half the plaquettes are good.
- Frames: either sense of rotation per dimer; a fixed (field-independent) rotation of the axis coordinates in which the two relative axes are compared. These ROT-shaped variants are covered by the Lemma 1 proof. They are not covered by the hypotheses of (6), since a generic fixed rotation breaks diagonal gauge covariance; the note claims them only via Lemma 1, which is correct.
- Motions within a dimer: every circle in the hypotheses of Step 8, with a different circle allowed on each dimer, and with no uniform speed bound.
- The relative frame of row 1573 (fixed h, then a Haar average over h): the j-law is exactly that of the raw circle, fibre by fibre.
- Compact U(1): the square-contour circle of row 1574 (Step 10).

**Not covered. Admissible circles exist outside the class.** Here "admissible" means a Haar-preserving Koopman circle on the doubled slice with half-turn equal to the swap a.e. For such a circle Lemma W, the exact winding law and 1 - P <= 2 E j^2 all hold.
1. **The orbit-chart circle of row 1573 (lines 58-66; HOLDS by check 1579).** Row 1576's Proposition 1.3 is the same construction (check 1582, Step 2). It is Haar-preserving, it descends to G_+ x G_+ orbits, and its half-turn is the swap of orbits. Its generator moves chord holonomies of long tree loops, so it is not dimer-local, and its velocities are not zero-mean under a single-replica exterior gauge. Its moment is estimated nowhere on file. Row 1573 states "no such estimate here". Row 1576 calls it "analytically dead" with an ARGUED O(beta n^3) remark, which is not a proof.
2. **Finite-range circles of other shapes.** Examples are block circles whose blocks contain two boundary links of every plaquette (for instance joint motions on vertex stars), motions that read neighbouring links (relative axes compared after transport along short paths, needed for pairs of non-incident links), and dimer circles that are neither diagonally covariant nor ROT-shaped. The proof as written does not reach these. Without covariance, E[Da | a,b] need only be a Haar-divergence-free field, not zero.
3. **The thermal clock V_s of row 1573, Lemma 3.** It preserves w(X)dX, not Haar, so its winding law is relative to another reference measure. The note correctly leaves it out (line 112).
4. **Structures I and II of row 1576 are not circles in this sense.** They interpolate the action at two seams or cuts (check 1582, Step 3: Structure I is the linear interpolation between direct and crossed seam pairings). No measure-preserving map of configurations is involved, so there is no winding law and no one-end moment. They are outside the question, not counterexamples to it.

**Relation to Theorem 1.2 (row 1576; HOLDS by check 1582, Step 1).** The engine of the lower bound is a single-replica exterior gauge average that randomises the mate's relative frame. This is the mechanism of Lemma NOISE. It is available exactly because the circle is local and only diagonally covariant. A circle that descends to single-replica orbits gives this average nothing to randomise. By Theorem 1.2, a regular, Haar-dominated deterministic swap interpolation that descends cannot have finite range R with n >= 2R + 7. The two results together leave two routes to a small moment: nonlocal descending circles (item 1, unestimated), or finite-range non-descending circles outside the dimer form (item 2, unestimated). Neither is excluded.

**Verdict on the scope claims.**
- Line 138, "A volume-independent moment at release therefore requires leaving this class": HOLDS.
- Final RESULT, "The small-moment route fails": HOLDS AFTER CORRECTION. Corrected text: "The small-moment route fails for every circle in the class of (6) (fixed incident-link matchings, dimer-local Haar-preserving diagonally covariant circles, the ROT frame variants and the fibred relative frame of row 1573). For nonlocal circles that descend to gauge orbits, such as the orbit chart of row 1573 or Proposition 1.3 of row 1576, and for finite-range circles of other shapes, the moment is not estimated."
- Counterexample: I have no admissible circle with o(n^3) moment. A heuristic I did not prove: at the release roots the chord variables of the comb tree are holonomies of long loops, close to Haar, and plaquettes are products of up to four chords. An independent replica rotation of the chords therefore moves most plaquettes at order-one speed, which suggests Theta(beta n^3) for item 1 as well. This is ARGUED only, not a proof step.

### Step 10. Purity and the comparison models (lines 140-152)

- **Wilson separation at matching parameters (line 142) -- HOLDS.** At fixed beta the conditional density bound is d = e^(-12 beta) (six terms of size <= beta). The derivative argument over [0, beta] gives a_p >= beta (9d/256)(dh)^6. For beta < 2/9, row 1573 (4)-(5) (HOLDS by check 1579, item 11, given row 1568 Theorem E) bounds -log P_K <= B_K <= pi^2(M + pi^2 M^2/4), with M <= 18 N beta^2 sum_(r >= v-2)(r+1) q^r, q = 9 beta/2 < 1, N = 3n^3 and v = n/1024. So -log P_K -> 0. On the same boxes and for the same circle, (1) gives E j^2 >= a_p^2 n^3/(32 * 9^3) -> infinity. At fixed n with beta -> 0 the moment tends to 0 (check 1580, 3b). That is consistent: the lower bound here is of order beta^2 n^3. The example is off the calibrated trajectory, and the note says so.
- **Neutral spectator (line 144) -- HOLDS.** With G = G_W + G_m and B^(1/2) = B_W^(1/2) (x) B_m^(1/2), the cross term is 2 Re[Tr(G_W B_W) Tr(G_m B_m)]-type. Tr(G_W B_W) = (-i/2) integral D_X(F_W^2) = 0 by Haar invariance. So the second moments add, given that both are finite (the Gaussian spectator has polynomial scores). The Wilson lower bound persists. The tanh(pi/512) bound is imported from row 1573 (HOLDS by check 1579).
- **Weak 4D compact U(1) (lines 146-148) -- HOLDS.** On a side where |psi| = rho > |phi|, the relative angle phi moves at speed 4 rho/pi. The link angle is the midpoint minus phi/2, so the link velocity is +-(2/pi) psi 1_(|psi| > |phi|). This is odd in psi, so it has mean zero at fixed phi under the uniform partner angle. Its mean square is (4/pi^2) E[psi^2 P(|phi| < |psi|)] = (4/pi^2)(1/pi^2)(pi^4/4) = 1, so s_e = 1 and s_p = 4. Antipodal reflection is the half-turn and commutes with the circle, so the law of the angle change is symmetric and r_e(s) is real. On the circle, |grad Re U|^2 = 1 - (Re U)^2. The orientation argument uses -1 in U(1), and Var_Haar(2 cos phi) = 2. So (6) gives c(beta) n^3 at every fixed beta. The endpoint test E j^2 >= (1 - P_even)/2 > 1/4 follows from 1 - P <= 2 E j^2. It depends on row 1573's P_even < 1/2, which uses row 1565's coset and positive-mixture inputs (check 1571 for those, given the periodic Villain input).
- **5D SU(2) (line 150) -- HOLDS (as a sketch with changed constants).** The spatial slice has 6n^4 plaquettes, 4n^4 links and 2n^4 dimers, so at least 4n^4 plaquettes are good. The selection has bounded degree. The orientation step has eight plaquettes per link, a 1/32 fraction of the links, and d = e^(-16 beta). Every step is the 4D step with changed constants. "No phase or dimension discrimination" follows, since the order is n^(d-1) in both gapped and gapless comparisons.
- **Threshold arithmetic (line 152) -- HOLDS.** 1 - 457/625 = 168/625, so E j^2 <= 84/625 suffices, and 42/625 a fortiori. Both fail eventually on the calibrated roots by (3). Odd weight at the calibrated roots remains undetermined. The note says so.

## Verdicts

| Part | Verdict |
|---|---|
| Setup, moment identity (lines 19-25) | HOLDS |
| Good plaquettes (27) | HOLDS |
| Lemma 1, local identity, finite-angle formula, orthogonality (29-45) | HOLDS |
| Passage to full moment, (1), (2) (47-66) | HOLDS |
| Plaquette mean at calibrated roots, (3) (70-76) | HOLDS, given row 1155 (9) and BND-1/BND-2 as cited (not re-checked here) |
| Plaquette mean on [2,3], (4) (78-86) | HOLDS |
| Upper bound (5) (88-104) | HOLDS |
| Vacuum, frames, relative frame (106-112) | HOLDS |
| Class (6), motions within a dimer (114-138) | HOLDS |
| Scope: "requires leaving this class" (138) | HOLDS |
| Scope: RESULT "The small-moment route fails" (154) | HOLDS AFTER CORRECTION (restrict to the class of (6); corrected text in Step 9) |
| Admissible circles outside the class | Exist: the orbit-chart circle (row 1573 = row 1576 Prop. 1.3), finite-range circles of other shapes; moment unestimated; no counterexample found |
| Wilson separation at beta < 2/9 (142) | HOLDS |
| Neutral spectator (144) | HOLDS |
| Weak 4D compact U(1) (146-148) | HOLDS, given row 1565 inputs for the endpoint test |
| 5D SU(2) (150) | HOLDS (sketch, changed constants) |
| Threshold arithmetic (152) | HOLDS |

RESULT — The decisive lower bound holds: for the paired-link circle of rows 1573/1574 the one-end moment is Theta(beta_K n^3) at every sufficiently late calibrated cutoff and Theta(n^3) uniformly on beta in [2,3], with and without independent centre projection. Lemma 1, the Bessel passage (1)-(2), both plaquette-mean regimes (the calibrated one given row 1155 (9) and BND-2 as cited), the upper bound (5), the vacuum version and the class (6) all hold. The comparison section also holds. One correction: "the small-moment route fails" holds only for circles in the class of (6). Admissible circles outside it exist (the nonlocal orbit-chart circle of row 1573, which is the same as row 1576's Proposition 1.3, and finite-range circles of other shapes), and their moments are unestimated. Row 1576's Structures I and II are not circles and have no winding law. (PUR-io) and the mass gap remain open.
Checked line by line by Claude (Opus 5.5).
