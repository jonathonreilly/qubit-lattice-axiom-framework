# FINISH row 907, gap-fw-wilson-max, Claude Fable 5.2 max

(file seeded by the lead; the author writes below)

Clone commit: 94d014f2866275824b7d1c6aa9cb75cb060f4ae4 (/Users/jonreilly/ym4d-lead/clone, pulled, already up to date).
Author: Claude Fable 5.2, max effort. FINISH row 907. Date 2026-11-13.
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
Status marks: PROVED (mine, by hand), READ (path and line), ARGUED, GUIDE, OPEN.

## Target

Wilson SU(2), 4D, free-wall boxes Z(P: a; F: b, c, d) of row 898 (periodic time, free space walls).
(WALL-1) b p(a) <= C_1 g(a,b).
(WALL-2) a delta_e(b) <= C_2 g(a,b).
Prove both with explicit constants and stated ranges of a, b, beta; or find the exact failing step and build the obstruction.
Then state the conditional engine theorem with all hypotheses. Test every step against U(1) and Z_2. Say which property of the Wilson weight the Step 6.2 counterexample lacks.

## Plan (one step per response, each appended before the next)

1. Read row 898 attack 1 (definitions of Z, p, c, gamma, delta_e, g; FW1 to FW6; Step 6.2) and record the exact objects here.
2. Read row 903 (free scalar proof: image identity, mode factorisation) and record which two facts it uses.
3. Reflection positivity across a plane perpendicular to a free axis: state what it gives for delta_e(b) (the one-sided substitute). Most valuable step; write it first after the reads.
4. Attack (WALL-2): a delta_e(b) <= C_2 g(a,b) from step 3 plus FW identities. Prove or isolate the failing step.
5. Attack (WALL-1): b p(a) <= C_1 g(a,b). Prove or isolate the failing step.
6. Tests: U(1) Coulomb (photon), Z_2, Q_8 / 2T, and the Step 6.2 counterexample. Name the property used.
7. Conditional engine theorem with all hypotheses; what is PROVED, what is OPEN.
8. RESULT line.

## Step 1. The objects of row 898 (READ: D/library/gap-next3-max.md L392-458, L477-491, L527-584)

Setup (READ L398-400). Box = product of {1..n_mu}. Direction P = periodic, F = free walls (no link leaves the box). Weight = product over plaquettes of exp(beta x_p), x_p = (1/2) tr U_p, Haar probability on links. Transfer in direction 1 with cross-section B: M = B_0^(1/2) K B_0^(1/2), K = (gauge projection)(link-wise convolution by the weight), positive. Periodic time: Z = Tr M^(n_1). Free time: Z = <u, M^(n_1 - 1) u>, u = B_0^(1/2) 1.

Family (READ L431-437). W(a, b) = Z(P: a; F: b, F: c, F: d). Time a periodic. Three free space sides b, c, d; c, d fixed.
- Time channel: W(a, b) = Tr M_b^a = lambda_0(b)^a (1 + S(a; b)). g(a, b) := log(1 + S(a; b)) >= 0. e(b) := log lambda_0(b).
- FW2 (READ L404): Z is super-multiplicative in a free side (Jensen; crossing links are Haar and each crossing plaquette has mean 0). So e(b_1 + b_2) >= e(b_1) + e(b_2).
- FW3 (READ L406): e convex in b. f := lim e(b)/b = sup. D(b) := f b - e(b) >= 0, concave, non-decreasing, bounded by beta N (N = crossing plaquettes per time step). D_inf := sup D. delta_e(b) := D_inf - D(b) >= 0, non-increasing, -> 0. So e(b) = f b - D_inf + delta_e(b).
- Space channel: W(a, b) = <v_a, R_a^(b-1) v_a> = w_0(a) r_0(a)^(b-1) (1 + S_W(b; a)). gamma(b, a) := log(1 + S_W) >= 0, non-increasing in b. eps(a) := log r_0(a). omega(a) := log w_0(a).
- FW5 (READ L439-442): p(a) := lim_b g(a, b)/b = eps(a) - a f >= 0. c(a) := omega(a) - a (f - D_inf).
  g(a, b) = (b - 1) p(a) + c(a) + gamma(b, a) - a delta_e(b).
- FW6 (READ L444-446): g(a, b + h) <= g(a, b) + h p(a) + a [delta_e(b) - delta_e(b + h)].
- FW1 (READ L402): on a free direction i, the flip of all i-links across a plane is a gauge transformation. No centre sector, no twist.
- Targets (READ L450-453, L480-481): for 3 <= a <= b/2, the other two free sides >= b:
  (WALL-1) b p(a) <= C_1 g(a, b). (WALL-2) a delta_e(b) <= C_2 g(a, b). Absolute C_1, C_2.
  Given both, FW6 with h = b gives g(a, 2b) <= (1 + C_1 + C_2) g(a, b) (ARGUED there).
- Step 6.2 counterexample (READ L410-423), for the VECTOR engine (all-free family): log Z(n) = f V + z^2 sum_mu V_mu (e^(-m n_mu) - 1). It has positive spectral forms, Z(0,.) = 1, super-multiplicativity, symmetry; vector thermal sum exp(z^2 bcd e^(-mt)) - 1; gap m in every box. With z^2 small the seed is small and the gap is small. Reading there: "the walls exchange one light particle with a small coupling z".
- Row 898's own remark (READ L455): no counterexample to the TRACE form (W'-ENG) was found in the class; "a wall that raises the mass in small boxes" violates crossed-channel positivity.

Note on what delta_e is. delta_e(b) is a property of the ground energy e(b) of the time transfer M_b on the cross-section (b, c, d) with all walls free. In the "b-channel" picture it is a zero-temperature (a -> infinity) wall-to-wall interaction per unit time.

## Step 2. Row 903, the free scalar (READ: D/library/gap-fw-gauss-opus.md, all 127 lines; unchecked, check 906 has no file yet)

- Model: free massive scalar, Neumann walls (no bond leaves the box). READ L21-26.
- Exact forms (READ L62-67): with G_s the Z^2 propagator at mass^2 s, T the transverse modes,
  delta_e(b) = b sum_T sum_{j>=1} int_{M_T^2}^inf G_s(2bj, 0) ds,
  p(a) = a sum_T int_{M_T^2}^inf sum_{r>=1} G_s(ra, 0) ds.
  So p(a) is one propagator wound r times round the time circle; delta_e(b) is the same propagator from a wall to its images at distance 2bj.
- W1 (READ L72-77): g - b p = W_N + corner > 0. C_1 = 1.
- W2 (READ L81-86): a delta_e(b) <= b p(a)/floor(2b/a). Proof: G_s(., 0) decreasing; r a <= 2 b j for r <= j k.
- The three facts it uses (READ L121): (i) image identity: the Neumann box of side b is the reflection-even sector of the periodic box of side 2b; (ii) mode factorisation of log W; (iii) exchange symmetry of the 2D propagator. "For the Wilson weight a free wall is not a mirror (the reflection-even sector of the 2b-torus keeps the plaquettes across the reflection plane), and log W does not split into modes."
- Its suggested target (READ L121): "prove a delta_e(b) at most C b p(a) for the Wilson weight from reflection positivity across the planes perpendicular to the free axis".

Remark for my Step 3. In the free field the comparison is delta_e(b) <-> p at winding distance 2b. So the natural Wilson statement is of the shape a delta_e(b) <= C b p(2b)-like or <= C b p(a) for a <= 2b. I keep both shapes in mind.

Note on check 902 (READ: D/library/gap-next3-check-astra.md L19-58, L84-173; Codex astra). FW1 to FW6 HOLD. w_0(a) > 0 holds (v_a > 0 and the Perron vector > 0). The conditional engine HOLDS AFTER CORRECTION: dyadic cubes only, k = 1 + C_1 + C_2, A = k^3, B = 4 A^2, seed s_0 < 1/B, then m((2^j b)^3) >= log(1/(B s_0))/a. (WALL-1), (WALL-2) must hold for every mixed rectangle used (3 <= a <= b/2, spectator sides >= b).

## Step 3. What reflection positivity across planes perpendicular to the free axis gives (the one-sided substitute). PROVED unless marked.

Notation. Slice = the 3D box (P: a; F: c; F: d). N = a N_1 links in the slice, N_1 = cd + (c-1)d + c(d-1). R = R_a = B_0^(1/2) K B_0^(1/2), v = v_a = B_0^(1/2) 1, Q := |v><v|. G(a, b) := log W(a, b) - a (f b - D_inf) = a delta_e(b) + g(a, b) = (b-1) p(a) + c(a) + gamma(b, a) (FW5). Ring family: P(a, n) := Z(P: a, P: n; F: c, F: d) = Tr R_a^n, symmetric in (a, n), sides >= 3. g_P(n; a) := log(Tr R_a^n / r_0(a)^n) >= 0. c_0 = c_0(beta) := 2 I_1(beta)/beta >= 1, the trivial character coefficient of exp(beta x).

### 3.1 Dictionary: p is the ring deficit; delta_e is the slab deficit

(a) W(a, n) <= P(a, n) <= e^(beta a N_1) W(a, n). Proof: P/W is the mean of exp(beta sum of the a N_1 crossing plaquettes) under (free box) x (Haar on the crossing links); Jensen below (mean 0 as in FW2), |x_p| <= 1 above.
(b) P is sub-multiplicative in each variable (trace of a power of a positive operator). So ell := lim eps(n)/n = inf exists, eps(n) = log r_0(n) = lim_a (1/a) log P(a, n) (by the symmetry of P).
(c) From (a), after (1/a) log and a -> infinity: eps(n) - beta N_1 <= e(n) <= eps(n). So f = lim e(n)/n = ell.
(d) Hence p(a) = eps(a) - a f = eps(a) - a ell = kappa(a), the deficit of the ring family in the sense of Theorem S (READ gap-next3-max.md L396: kappa >= 0, convex, non-increasing; Lemma X: a kappa(b) + g(a, b) = b kappa(a) + g(b, a)). So:
  (D1) p is non-increasing and convex in a (given the READ Lemma K of the ring family);
  (D2) a p(n) + g_P(a; n) = n p(a) + g_P(n; a) (two expansions of log P(a, n) - a n f);
  (D3) g_P(a; n) >= n p(a) - a p(n) >= (n - a) p(a) for n >= a. In the ring family (WALL-1) holds with C_1 = 2 on a <= n/2.
Reading. p(a) is the ground-energy excess of the ring of circumference a (ring Casimir term). delta_e(b) is the ground-energy excess of the free slab of width b over bulk plus two walls (slab Casimir term). (WALL-2) with (WALL-1) asks: a x (slab term at width b) <= C b x (ring term at circumference a), for a <= b/2. Both sides are zero-temperature numbers.
(e) From (c): delta_e(n) <= p(n) + D_inf. The wall cost does not cancel. Useless as it stands.

### 3.2 The Cauchy-Schwarz family of the free axis: wall costs cancel, but it only repeats convexity and FW6

RP across a plane perpendicular to the free axis is the statement R >= 0 with W(a, b) = Tr(Q R^(b-1)) and P(a, n) = Tr R^n. Its inequalities are Hilbert-Schmidt Cauchy-Schwarz: |Tr(A* B)|^2 <= Tr(A* A) Tr(B* B), A and B words in R and Q.
- Wall count. If A has j_A cuts and B has j_B cuts, both sides have 2 (j_A + j_B) free boxes. So the extensive wall cost a D_inf cancels in every such inequality. (This is the good news.)
- Both words cut: the inequality factors into two instances of W(a, k + k' + 1)^2 <= W(a, 2k + 1) W(a, 2k' + 1). This is convexity of G(a, .) in b (FW3).
- A = R^n, B has cuts with end exponents k, l: W(a, n + k + l + 1)^2 <= P(a, 2n) W(a, 2k + 1) W(a, 2l + 1). In G-form, with b_1 = 2k + 1, b_2 = 2l + 1 and (D2):
  (CS-1) G(a, n + (b_1 + b_2)/2) <= (1/2)[G(a, b_1) + G(a, b_2)] + n p(a) + (1/2) g_P(2n; a).
  FW6 in G-form is G(a, b + h) <= G(a, b) + h p(a). FW6 and convexity give (CS-1) without the last term. So (CS-1) is weaker than what row 898 has.
- Direction. Every word inequality bounds a box by boxes whose sizes sum to at most the same length. In the limit a -> infinity FW6 becomes delta_e(b + h) <= delta_e(b) (because p(a)/a -> 0 by 3.1), and convexity stays. So the word inequalities give for delta_e exactly: convex, non-increasing. They give no comparison of delta_e with p. An image-type bound needs rings on the other side, of the shape W(a, b)^2 P(a, n) <= W(a, b + h)^2 P(a, n - 2h); this is not a Cauchy-Schwarz form and it is false for general (R, v) (two-level example with a wall vector nearly orthogonal to the top state).
- Not explored: A, B linear combinations of words (ARGUED: no reason for the wall count to match).

### 3.3 The one-sided image inequality exists, and it is void

Lemma OS (wall domination). K >= c_0^N |1><1|, hence R >= c_0^N Q >= 0.
Proof. The link-wise convolution is a tensor product of single-link convolutions k. k has eigenvalue c_j = 2 I_(2j+1)(beta)/beta on the isotypic space j; all c_j > 0, c_0 is the largest and belongs to the constants. So k >= c_0 |1><1| >= 0 on each link, and the tensor product keeps the order. The gauge projection commutes with both sides and fixes 1. Conjugate by B_0^(1/2). QED
Consequences (symmetric sandwiches only; X = R^((n-1)/2)):
  (OS1) P(a, n) = Tr(X R X) >= c_0^N W(a, n).
  (OS2) P(a, 2b) = Tr((X R X)^2) >= c_0^(2N) Tr((X Q X)^2) = c_0^(2N) W(a, b)^2, X = R^((b-1)/2). (For 0 <= B <= A: Tr A^2 - Tr B^2 = Tr((A-B)^(1/2) (A+B) (A-B)^(1/2)) >= 0.)
  (OS3) W(a, 2b) = <R^(b-1) v, R R^(b-1) v> >= c_0^N W(a, b)^2.
Take (1/a) log and a -> infinity. Put Delta_w := D_inf - N_1 log c_0.
  From (OS2): delta_e(b) <= (1/2) p(2b) + Delta_w.   (RP-IMAGE)
  From (OS1): delta_e(n) <= p(n) + Delta_w.
  From (OS3): e(2b) >= 2 e(b) + N_1 log c_0, that is Delta_w >= 2 delta_e(b) - delta_e(2b) >= delta_e(b) for every b >= 1.
So Delta_w >= sup_b delta_e(b) = delta_e(1) >= 0, and (RP-IMAGE) is weaker than the trivial bound delta_e(b) <= Delta_w. PROVED.
Reading. (RP-IMAGE) has exactly the shape of the free-field image identity delta_e(b) = p(2b)/2 (row 903), as a one-sided inequality. Its defect Delta_w is the part of the wall cost that the trivial character does not see. It is extensive in the wall area (of order cd u^6 at small beta, ARGUED), and it is at least as large as the quantity it should bound. This is the exact step where the suggested route fails: the free wall is dominated by the bulk transfer only up to a constant per wall link, and that constant is not 1.
Answer to the brief's first question. RP across planes perpendicular to the free axis gives for delta_e(b): convexity, monotonicity, and (RP-IMAGE) with a void defect. It does not compare delta_e with p(a).

## Step 4. (WALL-2) for the Wilson weight: the exact failing step, and two obstructions

### 4.1 The exact doubling identity (PROVED). (WALL-2) is sufficient, not necessary.

Put tau(a, b) := gamma(b, a) - a delta_e(b). By FW5, g(a, b) = (b-1) p(a) + c(a) + tau(a, b), and tau(a, b) -> 0 as b -> infinity (both terms do). Subtract FW5 at b from FW5 at b + h:
  (DBL-ID) g(a, b + h) = g(a, b) + h p(a) + tau(a, b + h) - tau(a, b).
FW6 is (DBL-ID) after dropping gamma(b + h, a) - gamma(b, a) <= 0. So FW6 loses exactly gamma(b, a) - gamma(b + h, a) >= 0.
Reading. g has three parts: bulk thermal (b-1) p(a), wall thermal c(a), and the corner term tau = the thermal part of the wall-to-wall exchange. The zero-temperature wall-to-wall term a delta_e(b) cancels against the same term inside gamma. The engine uses only
  (DBL_k) g(a, 2b) <= k g(a, b).
(WALL-1) and (WALL-2) give (DBL_k) with k = 1 + C_1 + C_2. (WALL-2) bounds a delta_e(b), which (DBL-ID) does not contain. (WALL-1) with (CORNER): tau(a, 2b) - tau(a, b) <= C_2 g(a, b) gives the same k.

### 4.2 Obstruction A (PROVED, given row 903's mode formulas, READ and unchecked): no absolute C_2 in the class of local reflection-positive models with pointwise positive kernels

Model. Row 903's Neumann scalar (mass m, box a x b x c x d, time periodic), plus a boundary field on the two walls of the b-direction: S_J = S - J sum over sites with x_1 in {1, b} of phi_x, b >= 2. It is Gaussian, nearest-neighbour, reflection positive in every direction, with a pointwise positive transfer kernel and positive wall vector v_J = v exp(J sum phi). The crossed form W = <v_J, R^(b-1) v_J> holds, so FW5 and FW6 hold as in row 903.
Computation. Shift phi by the classical solution. The source is constant in time and in the transverse directions, so only the zero mode of time and of (c, d) enters:
  log Z_J(a, b) = log Z_0(a, b) + J^2 a cd [G_b(1,1) + G_b(1,b)],
G_b = (m^2 - Laplace_N)^(-1) on the path {1..b}. By images, G_b(x, y) = sum over j in Z of [G_inf(x - y + 2bj) + G_inf(x + y - 1 + 2bj)], G_inf(n) = e^(-mu |n|)/(2 sinh mu), cosh mu = 1 + m^2/2.
Consequences. The added term is linear in a. So every thermal object is unchanged: g_J = g_0, p_J = p_0, c_J - c_0 and tau_J = tau_0 follow from FW5 (c shifts by 0 because the b-independent part of the shift goes into D_inf). Only e(b) moves:
  delta_e^J(b) = delta_e^0(b) + J^2 cd I(b),  I(b) = sum_{j != 0} [G_inf(2bj) + G_inf(1 + 2bj)] + sum_j [G_inf(1 - b + 2bj) + G_inf(b + 2bj)] >= G_inf(b-1) + G_inf(b) > 0.
With g_0(a, b) <= bcd F_a(mu) (bcd modes, each of energy >= mu; F_a(w) = -log(1 - e^(-a w))):
  a delta_e^J(b) / g_J(a, b) >= J^2 (a/b) e^(-mu (b-1)) (1 + e^(-mu)) / (2 sinh(mu) F_a(mu)) -> infinity as J -> infinity, at fixed a, b, c, d, m.
So (WALL-2) holds in this model only with C_2 of order J^2 times a function of m. Yet (DBL_2) holds for every J, because g does not see J (row 903 L119, READ: g(a, 2b) <= 2 g(a, b) for the Neumann scalar).
Reading. A wall that couples linearly to a massive particle exchanges ONE particle with the other wall: delta_e(b) decays like e^(-mu b), not like the two-particle (image) rate e^(-2 mu b), and its size is the square of the wall coupling. No structural property (locality, RP in all directions, positivity of the kernel, axis symmetry of the bulk) bounds that coupling. So for the Wilson weight an absolute C_2 in (WALL-2) is a quantitative statement: the linear coupling of the free wall to the lightest scalar state is bounded in units of the thermal density. It cannot come from a soft argument.

### 4.3 Obstruction B (ARGUED: leading order of the convergent small-beta polymer expansion; the uniform remainder is not written): the Wilson free wall is of this linear type, and the image bound is false for it

u := I_2(beta)/I_1(beta) (about beta/4). A closed surface of plaquettes in the spin-1/2 representation, homeomorphic to a sphere, has activity 4 u^F; a torus has u^F (weight d^(V-E+F) u^F, d = 2).
- delta_e(b) is the sum of the clusters of the infinite tube that leave the slab on both sides. A closed surface that crosses the b+1 layers between x_1 = 0 and x_1 = b+1 has at least 4 plaquettes per layer and 2 caps. Equality: the straight tube 1 x 1 x (b+1). So delta_e(b) = 4 n_t u^(4b+6) (1 + O(u^2)) at fixed b, n_t = (c-1)(d-1) + (c-1)d + c(d-1) unit squares of the wall per unit time.
- p(a) is the sum of the clusters that wind around a ring of circumference a (3.1). Least: the straight torus tube, 4a plaquettes. So p(a) = n_t u^(4a) (1 + O(u^2)) at fixed a.
- g(a, b) = n_s(b) u^(4a) (1 + O(u^2)) at fixed a, b; n_s(b) = number of space plaquettes of the box, about b n_t.
Consequences at fixed sizes, beta -> 0:
  delta_e(b)/p(2b) = 4 u^(6 - 4b) (1 + o(1)) -> infinity for b >= 2. The image bound delta_e(b) <= C p(2b) is FALSE for Wilson SU(2) (and for Z_2, Q_8, 2T, U(1) at small beta; the count is group-blind up to the factor d^2).
  delta_e(b)/p(b + 1) = 4 u^2 (1 + o(1)), delta_e(b)/p(b) = 4 u^6 (1 + o(1)).
  a delta_e(b)/g(a, b) = 4 (a n_t/n_s(b)) u^(4(b-a)+6) (1 + o(1)), tiny for a <= b/2. So (WALL-2) itself is true at leading order.
Reading. The tube from wall to wall is one glueball exchanged between the walls. The Wilson wall is not a mirror; it is a source. The effective image distance is b + 3/2, not 2b. What the engine domain a <= b/2 needs is only the half-distance statement delta_e(b) <= C' p(floor(b/2)) (then a delta_e(b) <= C' a p(a) <= C' (a/b) C_1 g(a, b), by (D1) and (WALL-1)).
Caution (ARGUED). Even delta_e(b) <= C p(b) should fail for b large at fixed beta: wall exchange is a zero-frequency, zero-transverse-momentum (one-dimensional) propagator, of order A^2 e^(-m b)/(2m) per unit wall area; p(b) is a three-dimensional phase-space sum, of order (m/(2 pi b))^(3/2) e^(-m b). The ratio grows like b^(3/2). (WALL-2) survives only through the margin e^(-m (b - a)), a <= b/2, and its constant is of order A^2/m^4 (A = wall coupling of the lightest scalar, m its mass).

### 4.4 What (WALL-2) says, exactly (PROVED identity)

Take the box [-L, b + L] in the free direction with two interior cuts (between 0 and 1, between b and b+1), cut strengths s_1, s_2 in [0, 1] on the crossing plaquettes (weight exp(s beta x_p)). X_i = sum of x_p over cut i. The mixed second difference of log Z in (s_1, s_2) is log[W(T, b) W(T, L)^2 W(T, 2L + b)/(W(T, L) W(T, L + b))^2]. Divide by T, let T -> infinity:
  (COV) delta_e(b) + delta_e(2L + b) - 2 delta_e(L + b) = lim_T (beta^2/T) int_0^1 int_0^1 <X_1 ; X_2>_(s_1, s_2) ds_1 ds_2.
The left side tends to delta_e(b) as L -> infinity. So delta_e(b) is beta^2 times the truncated plaquette-plaquette correlation between two partially cut layers at distance b, summed over the layers (zero frequency, zero transverse momentum), averaged over the cut strengths. The same formula at finite T, in the infinite tube, gives gamma(b, T).
(WALL-2) is therefore an infrared bound: a layer-summed truncated correlation at distance b in the free direction, at zero temperature, against the thermal trace of the box at time a <= b/2. By the crossed spectral form it decays in b at the rate of the gap of R_T for large T, which is the time-gap of the tube (P: infinity; F: c, d) by axis exchange; g(a, b) is governed by the time-gap of the box (F: b, c, d). So (WALL-2) needs: every light state of the infinite tube that the wall can emit appears in the thermal trace of the finite box, with multiplicity at least of the order of the squared wall coupling. This is a comparison of a vector weight with a trace multiplicity, in linked form.

### 4.5 Verdict on (WALL-2)

Not proved. The failing step is exact: RP in the free direction gives only (RP-IMAGE) with the void defect Delta_w (3.3); the free-field proof used the image identity delta_e(b) = p(2b)/2, which is false for the Wilson wall (4.3); and in the class of local RP models the constant C_2 is unbounded (4.2). (WALL-2) is true at leading order at small beta (4.3). A proof at order one must bound the linked wall overlap; pointwise positivity gives only the unlinked bound |<v, O psi_0>| <= sup|O| <v, psi_0> for a multiplication operator O (v > 0 and psi_0 > 0 pointwise), which loses a factor exponential in the wall volume when it is summed over states. OPEN.

## Step 5. (WALL-1) for the Wilson weight: an exact identity, the soft bounds, and the failing step

### 5.1 The cut identity (PROVED)

Cut free energy of the ring: F_cut(a; n) := log P(a, n) - log W(a, n) = -log <exp(-beta X_cut)>_ring(a, n). By 3.1 (a) and (OS1): a N_1 log c_0 <= F_cut(a; n) <= beta a N_1. Its zero-temperature rate: phi_cut(n) := lim_T F_cut(T; n)/T = eps(n) - e(n) = p(n) + D_inf - delta_e(n).
Subtract a eps(n) and a e(n) from the two logarithms:
  (CUT) g_P(a; n) - g(a, n) = F_cut(a; n) - a phi_cut(n).
The difference of the thermal sums of the ring and of the free slab is the thermal excess of the cut free energy. With FW5, (D2) and n -> infinity (g_P(n; a) -> 0, tau(a, n) -> 0, p(n) -> p_inf := lim p >= 0):
  c(a) - p(a) + a p_inf = lim_n [a phi_cut(n) - F_cut(a; n)].
So the thermal wall term c(a) exceeds the bulk unit p(a) exactly when cutting costs less per unit time at time-length a than at zero temperature. In the free field both signs occur (row 903, READ: Neumann c = p + W_N > p; Dirichlet and the edge towers of Maxwell have a negative wall term).

### 5.2 What soft arguments give for c(a) (PROVED): two extensive bounds, nothing uniform

- Upper: c(a) <= G(a, b) - (b-1) p(a) for every b (gamma >= 0). And from (OS1) with n -> infinity: c(a) <= p(a) + a Delta_w.
- Lower: from P(a, n) <= e^(beta a N_1) W(a, n) with n -> infinity: c(a) >= p(a) - a (beta N_1 - D_inf).
Both defects are of order a x (wall area). (WALL-1) needs c(a) + tau(a, b) >= -(1 - 1/C_1) (b-1) p(a) + p(a)/C_1, a bound with p(a) on the right, which is exponentially small in a in a massive phase. The soft lower bound misses it by the whole wall cost. Same failure as 3.3, on the thermal side.

### 5.3 A reduction that uses the ring engine (PROVED implication)

(RING-CMP_theta): |g(a, n) - g_P(a; n)| <= theta g_P(a; n), for n in {b, 2b}, some theta < 1. By (CUT) this says: the thermal excess of the cut free energy is at most theta times the ring's thermal log-sum.
Claim. (RING-CMP_theta) on a <= b/2 gives (WALL-1) with C_1 = 2/(1 - theta) and (DBL_k) with k = 4 (1 + theta)/(1 - theta).
Proof. (D3): g_P(a; b) >= (b - a) p(a) >= (b/2) p(a); so b p(a) <= 2 g_P(a; b) <= 2 g(a, b)/(1 - theta). Lemma E of the ring family (READ gap-next3-max.md L396; the tube corollary, check 902 HOLDS): g_P(a; 2b) <= (2b/(b - a)) g_P(a; b) <= 4 g_P(a; b). So g(a, 2b) <= (1 + theta) g_P(a; 2b) <= 4 (1 + theta) g_P(a; b) <= 4 (1 + theta) g(a, b)/(1 - theta). QED
This route never meets delta_e or FW6. It needs the ring comparison for each of the three free directions in turn (ring in the doubled direction, the other two free).
Expected sign (ARGUED): restoring the cut layer lowers excitation energies, so g <= g_P for Wilson (as for the Maxwell edge towers); then only the lower half, g >= (1 - theta) g_P, has content: a free wall removes at most the fraction theta of the ring's thermal weight when a <= b/2. Row 903's GUIDE values correspond to theta about 0.2 (Maxwell, natural walls) to 0.4 (Dirichlet scalar).

### 5.4 Verdict on (WALL-1)

Not proved. Exact failing step: the thermal wall term is the thermal excess of the cut free energy (5.1), and positivity bounds it only extensively (5.2). (WALL-1) holds in the ring family with C_1 = 2 (D3) and at leading order at small beta (4.3: g/(b p) = n_s(b)/(b n_t), between 1 - 1/b and 1). OPEN at order one.

PROVISIONAL RESULT (written in case the run is cut; the final RESULT line, if present below, replaces it): Row 907 (Claude Fable 5.2 max, unchecked): (WALL-1) and (WALL-2) are NOT proved for Wilson SU(2). Proved: p(a) is the ring deficit of the tube family; RP across planes perpendicular to the free axis gives only convexity, FW6 and a one-sided image inequality delta_e(b) <= p(2b)/2 + Delta_w whose defect Delta_w >= delta_e(1) makes it void; an exact doubling identity shows the engine needs only g(a,2b) <= k g(a,b), not (WALL-2); a Gaussian model with a boundary field shows no absolute C_2 exists in the class of local RP models; the image bound delta_e(b) <= C p(2b) fails for the Wilson wall at small beta (tube exchange, argued). Open: the doubling bound at order one.


Correction and upgrade to 3.1 (D1) (PROVED, no READ input needed). eps is convex in n because n -> P(a, n) = Tr R_a^n is log-convex (Cauchy-Schwarz) and eps(n) = lim_a (1/a) log P(a, n). So p = eps - f n is convex. p >= 0 (FW5). p(n)/n -> 0 (3.1 (c)). A convex sequence that is bounded below and is o(n) cannot increase. So p is non-increasing. Correction to 5.2: the sign of the last term in the displayed (WALL-1) condition is + p(a)/C_1 (fixed in place).

## Step 6. Tests: the Step 6.2 counterexample, U(1), Z_2, Q_8 and 2T

### 6.1 The Step 6.2 counterexample and its trace analogue

(a) Row 898's Step 6.2 family refutes the VECTOR engine: a light state with a small wall coupling z hides from a vector sum. In the trace form it cannot hide: a state of energy m in the box contributes e^(-m a) to S(a; .) with multiplicity at least one. This protection is integrality of the trace. It is not a property of the Wilson weight.
(b) For (WALL-2) the danger is the opposite corner: a light state with a STRONG wall coupling and a small multiplicity. Family T (PROVED to lie in row 898's class; n a positive integer, D_1 >= 2 z^2):
  log W(a; b, c, d) = f abcd - a D_1 (bc + cd + bd) + z^2 a (cd e^(-mb) + bd e^(-mc) + bc e^(-md)) + n bcd F_a(m),  F_a(m) = -log(1 - e^(-a m)).
  Time channel: lambda_0^a times the trace of n bcd oscillators of energy m (integer multiplicities). Crossed channel in b: constant x r^b x exp(z^2 a cd e^(-mb)), a Poisson mixture of exponentials, positive weights; the same in c and d. Super-multiplicative in each free side: the defect is a cd (D_1 - 2 z^2) or more. Symmetric in (b, c, d).
  Its data: delta_e(b) = z^2 cd e^(-mb); g = n bcd F_a(m); p = n cd F_a(m); c(a) = p(a); tau = 0; gamma(b, a) = a delta_e(b).
  (WALL-1) holds with C_1 = 1. (DBL_2) holds with equality. The gap is m in every box. But at a = b/2 and m = (2 log 2)/b: a delta_e(b)/g(a, b) >= z^2/(8n). So C_2 >= z^2/(8n), unbounded in the class.
(c) Answer to the brief. The class of Step 6.2 has no relation between the wall coupling z^2 and the trace multiplicity n. RP across the free axis adds only Lemma OS, which family T satisfies for a suitable Delta_w. So no property that the lane has written down avoids family T. What the Wilson weight has and the class lacks is a link between the two numbers: the state that a free wall emits at one wall site is a local excitation, and its translates along the free axis are the states that the trace counts. In symbols: v = B_0^(1/2) 1 and R = B_0^(1/2) K B_0^(1/2) are built from the same local weight, v > 0 and the Perron vector psi_0 > 0 pointwise, and |x_p| <= 1. These give |<v, O psi_0>| <= sup|O| <v, psi_0> for each multiplication operator O. They do not yet give the linked bound that (WALL-2) needs. This is the missing lemma, stated in 7.3.
(d) Side result on the class (PROVED for real multiplicities; it does NOT survive integrality). Multiplicity functions M(b-1) = (m_1 - nu) + pi x + nu e^(-x/ell), x = b - 1, keep the crossed channel positive and can vanish to second order at one box size. With real multiplicities this refutes (WALL-1) and (DBL_k) for every absolute constant, and even the unconditional engine. With integer multiplicities and box-independent levels the remainder nu e^(-x/ell) must be integer valued and decreasing, hence it is a bump at x = 0 only, and M is affine for b >= 2: the family collapses. So integrality together with crossed positivity is rigid, and the unconditional trace engine in the class stays OPEN (neither proved nor refuted), as row 898 said.

### 6.2 U(1)

Every PROVED statement of Steps 3 to 5 is group-blind: it uses the positive character expansion, c_0 >= 1 largest (for U(1): c_0 = I_0(beta), coefficients I_n(beta)), the mean-zero crossing links, and |x_p| <= 1. So each holds for U(1) at every beta, Coulomb phase included. None of them asserts a gap, so there is nothing that must fail.
- Coulomb phase, Gaussian level (READ row 903 L88-97, unchecked): Maxwell with natural walls passes (WALL-2) tower by tower, and delta_e ~ cd/b^3, g ~ bcd/a^3 (GUIDE). Charge conjugation forbids the emission of one photon by a wall, so the U(1) wall is of the image type there (ARGUED). (DBL_k) holds with k near 2.
- The engine does not prove a gap for U(1): the seed fails. S(a; b^3) = exp(g) - 1 with g of order b^3/a^3 >= 8 on a <= b/2 (GUIDE). The fact test is met by the seed, not by the wall inequalities.
- Small beta: U(1) confines; 4.3 applies with activity (I_1/I_0)^F and no factor d^2.

### 6.3 Z_2, Q_8, 2T

- Small beta: 4.3 holds with t = tanh(beta) and d = 1 for Z_2: delta_e(b) = n_t t^(4b+6) (1 + o(1)), p(a) = n_t t^(4a) (1 + o(1)). The image bound fails in the same way. (WALL-1), (WALL-2), (DBL) hold at leading order.
- Large beta (ARGUED). Free-wall boxes have no centre sector (FW1) and, for a finite group at freezing coupling, a single flat class (check 902, F2, READ). Excitations cost of order e^(-c beta) per unit. So the free-wall seed is small and the conclusion "gap on free-wall cubes" is TRUE for Z_2, Q_8 and 2T in their deconfined phases. The free-wall engine therefore does not distinguish SU(2) from Q_8 or 2T, and it must not: its conclusion is a glue statement, not a flux statement. This is row 898's point, and it is also the route's limit: a gap on free-wall cubes says nothing about confinement.
- None of my statements uses a property that Q_8 or 2T lack. None is a worst-case, vertex-block or background-uniform bound, and (AN1) is not used.

