lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T10:59Z

# gap-mini-solve-b-fable (queue row 1189)

Pinned at commit f7e5907e5 of `claude/ym4d-hard-route`. Research-stage working state. It grants no status. Nothing here is a public claim.

**The problem (row 1189).** Prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the sense of Jaffe and Witten.

**Labels.** Each statement below carries one of: PROVED (every step written here or in a cited checked note), ARGUED (an argument with a named unproved step), GUIDE (heuristic or numeric guidance, never a proof step), OPEN.

**Process.** One step per response. Each step is appended here before the next one starts.

## Step 0. Plan (written before reading the earlier work)

1. Read the earlier work on the gap: the FINISH.md RESULT lines for the gap rows, `parts/gap.md`, `library/open-core.md`, and the notes the newest gap rows name. Record what is established and what is open. No duplicate attack (rule 0a).
2. Choose one line of attack on the first open statement the gap needs. Say why it is not a repeat.
3. Carry it through, or name the first step that fails, with the explicit failure.

(Steps follow.)

## Step 1. What the earlier work fixes (read, not re-derived)

Sources read at this pin: `FINISH.md` rows 1007-1018 and 1179-1187 (RESULT lines), `parts/gap.md` L1-104 and the route registry L223-267, `library/gap-council-synthesis.md` in full, `library/gap-mini-branch-fable.md` L300-312. None of these is evidence by itself. Each says where a proof and its check are.

1. **The target splits in two (rows 1179, 1065; check row 1183: main chain HOLDS AFTER CORRECTION).** The Jaffe-Witten gap clause follows from (i) the continuum datum of the T0 chain (existence, with (H2), (TOT)), which is OPEN, and (ii) one lattice estimate, (N-phys), which is OPEN. The Wilson branch selection (BS) enters only the wall (W) as worded (confinement on tori), not the gap clause.
2. **(N-phys) (row 1161, `gap-solve9-astra62.md` L146-148).** At one admissible physical side L, for every cutoff index j >= j_0, with n_j = L/a_j, there is an integer u_j with 3 <= u_j <= n_j/K and s_+(u_j; n_j^3) <= 1/2. Here s_+ is the periodic centre-neutral excited trace of the cube n_j^3 in units of its vacuum. Rows 1180 and 1184 (two independent attacks, unchecked at this pin; check row 1187 running): (N-phys) is a neutral lattice gap at arbitrarily weak coupling together with an upper bound of asymptotic-scaling type on the seed size. Nineteen routes ended at steps already on file.
3. **The map.** Route families RA-RG, LC, BR-2, (T-pin), (DS-W), (A) and methods 1-36 of `parts/gap.md`. The common verdict (row 998 6b): every engine found is blind, and no input excludes the massless branch beyond first passage. Comparison cases that a proof must fail on: compact U(1) at weak coupling, frozen Q_8 and 2T, the K7 endpoint (mixed action), the free photon, a product with a massless factor.
4. **The 2D precedent (rows 1007-1010, reading only).** The posted 2D O(N) proofs cross the band by a stiffness iteration on pinned cells. The gain per scale is a commutator (curvature) term. Rows 1011, 1016, 1018 (Fable 5.2 max, with gpt-6-astra checks): the direct port fails in the class of all pins (Propositions B, B', Theorem BH). SU(2) has the bracket and no symmetric continuous twist. Compact U(1) has the twist and zero gain.

So the open lattice statement is one sentence: **a selective gain at order-one response**. Step 2 chooses the attack.

## Step 2. Choice of attack

### 2.1 Screening (GUIDE; no statement here is a proof step)

Before choosing, I derived candidate routes from the Jaffe-Witten target alone and searched the lane for each (`grep` over `library/gap-*.md` and `parts/gap.md`). Every one has a match. The count is the number of lane files that name the tool.

| Candidate, from first principles | Where it ends | Match on file |
|---|---|---|
| Orbit-space curvature, Bakry-Emery, Helffer-Sjostrand with the O'Neill term | the positive Ricci term is cancelled at order one by the averaged paramagnetic term (lattice Ward identity) | method 31; Helffer 16 files, O'Neill 10, Singer 15 |
| Convex Gribov region, log-concave Faddeev-Popov weight | magnetic energy is not convex | Gribov 15, Zwanziger 10 |
| One-link conditional randomization (Simon and Yaffe) | charged lines only; ultraviolet self-energy | 3 files; route (A), rows 1132-1138 |
| Finite-volume trace anomaly, virial sign | a sign in beta with no number | route RB; rows 710-715 |
| Gradient-flow coupling t^2 E(t) as a twist-free neutral stiffness | Hamilton's monotonicity gives only "the action decreases"; no consumer | `gap-outside-box-max.md` I15 |
| Lee-Yang property of S^3 with beta as the field | true in 2D (zeros of I_1); no zero-free region in 4D | route B9, Lemmas LYP, LYP2; `parts/gap.md` L281 |
| Migdal-Kadanoff recursion (Ito 1985; Mueller and Schiemann 1985) | no comparison with the true lattice; confines 4D U(1) too | route RG; rows 797-801 |
| Durhuus-Frohlich layers; anisotropic 2+2 split; frozen planes | uniform mixing over backgrounds fails; (SING); (MON-L) | method 36; BR-2; rows 1053, 1072-1115 |
| Central twist, vortex containers (Mack and Petkova) | flux half only | council 2c; rows 731, 1018 |
| Pinned-cell stiffness iteration (the 2D engine) | SU(2) has the bracket and no symmetric continuous twist | rows 1011-1018, 1118-1123 |
| Static-potential (force) scheme, concavity (Bachas) | a running-coupling inequality at all scales, as RA | route RA |
| Correlation inequalities for plaquette energies | none known for SU(2); wrong direction for decay | GKS: `parts/gap.md` test table |

Three constraints that I re-derived are on file too. (i) The neutral gap at a fixed coupling in the band reads a number: the mixed action has a critical end-point close to the Wilson axis (K7). (ii) Reflection positivity, gauge invariance and perturbative data do not separate theta = 0 from theta = pi (16 files). (iii) A fixed colour axis has a mass-form twist cost (row 1181 Lemma 5.1a; Lemma FR).

Verdict (GUIDE): this screening found no route off the lane's map. It agrees with rows 1128-1130 and 1179-1184.

### 2.2 The attack chosen

**Item.** Route S2 of row 1103 (`gap-face-exercise-fable.md` L1051-1054, L1318-1327), first stated as a remark in row 1053 6.8 (`gap-wall-vectors-max.md` L296-298): the doubly flat corner, beta_L = beta_T = infinity, mixed coupling beta. Row 1103 records it as "not attempted beyond the kill pass". Row 1053 records it as a corner "at which a theorem looks reachable".

**Why this one.** It is the only place on the map where all three hold at once: (a) the model is four-dimensional and comes from Wilson SU(2) by a limit of plane couplings; (b) it has an exact continuous non-abelian symmetry with a transitive action on boundary data, so the missing object of rows 1011-1018 (a symmetric twist with a bracket) exists exactly; (c) no row has attempted it. Its U(1) version is believed massless (row 1053), so a proof must be selective.

**What it can and cannot give.** It cannot give the Jaffe-Witten gap. Row 1103 marks S2 "wounded twice": the end-point is open, and the two descents to the isotropic point control different rates. So the plan has two parts.
- Part A (Steps 3-4): the end-point. Reduce the gap at the doubly flat corner to one statement about a two-dimensional model, with every identity written. Then attack that statement.
- Part B (Step 5): the descent. Decide by a hand estimate whether the symmetric twist of the corner survives when the in-plane curvature is unfrozen. This is the step that decides whether Part A is on the path of (N-phys).

Stop rule: a proof, a counterexample, or the first failing step with its explicit failure, for each part.

## Step 3. Part A: the doubly flat corner, exact structure

Credit. The corner and the remark that its twists act transitively on pins are row 1053 6.8 (Claude Fable 5.2 max). The picture of anisotropic Yang-Mills as coupled two-dimensional chiral models is P. Orland's (cited by row 1053). Subsystem symmetries: N. Seiberg and S.-H. Shao (cited there). The twist inequality is C. Pfister's form of the Mermin-Wagner argument (also R. Dobrushin and S. Shlosman). The complex twist is O. McBryan and T. Spencer's. Everything below is elementary. The lane holds the corner only as that remark, so the lemmas are written out here.

### 3.1 The model

Sites x = (p, y), with p in a finite box F of Z^2 (directions 1, 2, "fibre") and y in a finite box B of Z^2 (directions 3, 4, "base"). Free boundary. One spin k(x) in SU(2) at each site. Write <a, b> = (1/2) tr(a b^(-1)) for a, b in SU(2); it is the Euclidean inner product of S^3 in R^4. The corner model at coupling beta > 0 is the probability measure

  d mu(k) = Z^(-1) exp(E(k)) prod_x dk(x),   E(k) = beta sum (1/2) tr[ k(x)^(-1) k(x+mu) k(x+mu+nu)^(-1) k(x+nu) ],

where the sum runs over all mixed plaquettes (x; mu in {1,2}, nu in {3,4}) inside F x B, and dk is Haar measure.

**Lemma A0 (origin; ARGUED).** For Wilson SU(2) on F x B with free boundary and plane couplings beta_12 = beta_L, beta_34 = beta_T, mixed coupling beta, the limit beta_L, beta_T to infinity is mu in the variable k = g^(-1) h, where U_mu(x) = g(x) g(x+mu)^(-1) for mu = 1, 2 and U_nu(x) = h(x) h(x+nu)^(-1) for nu = 3, 4.
Argument. On a two-dimensional box with free boundary, the links are in bijection with (plaquette variables, gauge function modulo a constant), and Haar measure goes to product Haar measure (axial gauge). So the limit of the frozen planes is the image of product Haar measure on g and on h. The mixed plaquette is tr[g(x) g(x+mu)^(-1) h(x+mu) h(x+mu+nu)^(-1) g(x+mu+nu) g(x+nu)^(-1) h(x+nu) h(x)^(-1)] = tr[k(x)^(-1) k(x+mu) k(x+mu+nu)^(-1) k(x+nu)]. If g and h are independent and Haar, so is k. The weak limit itself is not written out here; nothing below uses A0.

### 3.2 Exact identities (all PROVED; each is a one-line computation)

**Lemma A1 (sheet form).** For a fibre link e = <p, p'> put m_e(y) = k(p, y)^(-1) k(p', y). Then the mixed plaquette on e and the base link <y, y'> equals <m_e(y), m_e(y')>. So E = beta sum over fibre links e of the two-dimensional O(4) energy of the field y -> m_e(y). The fields m_e are tied by the fibre constraint: the ordered product of m_e around every fibre plaquette is 1.
Proof. (1/2) tr[k(p,y)^(-1) k(p',y) k(p',y')^(-1) k(p,y')] = (1/2) tr[m_e(y) m_e(y')^(-1)]. QED.
The same holds with fibre and base exchanged: for a base link f = <y, y'> put n_f(p) = k(p, y) k(p, y')^(-1); the plaquette is <n_f(p'), n_f(p)>.

**Lemma A2 (symmetries).** mu is invariant under k(p, y) -> c(y) k(p, y) d(p) for every c: B -> SU(2) and d: F -> SU(2). It is invariant under the automorphisms of F and of B. If F = B, it is invariant under the exchange (p, y) -> (y, p) together with k -> k^(-1).
Proof. m_e(y) -> d(p)^(-1) m_e(y) d(p'), and <.,.> is invariant under simultaneous left and right multiplication. For the exchange, tr A = tr A^(-1) in SU(2), and the inverse of the plaquette word with k -> k^(-1) is the plaquette word with mu and nu exchanged. QED.

**Lemma A3 (only singlets survive).** For every nontrivial irreducible representation D and all sites x != x', the expectation of D(k(x)^(-1) k(x')) is 0.
Proof. If the base points differ, average over c at one of them. If they agree, the fibre points differ; average over d at one of them. QED.

**Lemma A4 (a two-dimensional model with a homogeneous spin space).** Put K(y) = (k(p, y))_{p in F}. Then mu is a nearest-neighbour model on B with single-site space T = SU(2) \ SU(2)^F (left diagonal quotient), pair energy E(K, K') = beta sum_e <m_e(K), m_e(K')>, and symmetry group SU(2)^F acting on T from the right. The action is transitive. So any two boundary conditions on a base region differ by a site-dependent symmetry.
The fibre with two sites gives the standard two-dimensional O(4) model for m. A fibre that is a chain (or any tree) gives independent O(4) models, one per fibre link, because the fibre constraint is empty.

**Lemma A5 (one plane, given the others).** Fix p_0 and all k(p, .) with p != p_0. Put s(y) = k(p_0, y). The conditional law of s has density proportional to exp(beta sum over base links <y, y'> of <Q_{yy'} s(y'), s(y)>), with Q_{yy'} = sum over the fibre neighbours n of p_0 of k(n, y) k(n, y')^(-1), a quaternion of norm at most 4, acting by left multiplication. It is invariant under s -> s d, d in SU(2).
So one plane is a two-dimensional O(4) model with link strengths in [0, 4 beta] and a background connection in the left SU(2) only. The right SU(2) is an exact global symmetry for every background. (Method 36 of `parts/gap.md` is the two-sided case, where no symmetry is left.)
Proof. <s(y)^(-1) k_n(y), s(y')^(-1) k_n(y')> = (1/2) tr[s(y') s(y)^(-1) k_n(y) k_n(y')^(-1)]; sum over n. QED.

**Lemma A6 (the symmetric twist and its exact cost).** Fix a fibre site p_0, a unit vector n, and theta: B -> R. Let J = (i/2) n.sigma and T_theta: k(p_0, y) -> k(p_0, y) exp(theta(y) J), all other spins fixed. T_theta preserves product Haar measure. For a fibre link e from p_0 and a base link <y, y'>, with delta = theta(y') - theta(y) and q = m_e(y) m_e(y')^(-1) = q_0 + i q.sigma,

  <m_e(y), m_e(y')> o T_theta = cos(delta/2) q_0 - sin(delta/2) n.q .

No other term of E changes. Hence E o T_theta + E o T_(-theta) - 2E >= -2 C(theta), with C(theta) = beta N sum over base links of (1 - cos(delta/2)) and N at most 4 the number of fibre neighbours of p_0.
Proof. m_e(y) -> exp(-theta(y) J) m_e(y); (1/2) tr[(cos(delta/2) + i sin(delta/2) n.sigma)(q_0 + i q.sigma)] = cos(delta/2) q_0 - sin(delta/2) n.q; and q_0 is at most 1 in absolute value. QED.

### 3.3 Two consequences at every coupling (PROVED)

**Proposition A7 (Mermin-Wagner step, uniform in the fibre and in the pins).** Let nu be mu, or mu conditioned on the values of any spins outside {p_0} x supp(theta). For every bounded f >= 0,

  nu(f o T_theta) nu(f o T_(-theta)) >= exp(-2 C(theta)) nu(f)^2 .

Proof. nu(f o T_theta) = nu(f rho_theta) with rho_theta = exp(E o T_(-theta) - E), by the change of variables k -> T_theta k (the conditioning is untouched). By A6, rho_theta rho_(-theta) >= exp(-2C). Cauchy-Schwarz: nu(f sqrt(rho_theta rho_(-theta)))^2 <= nu(f rho_theta) nu(f rho_(-theta)). QED.
Size of C. Take theta = theta_0 phi / log r with phi the profile in the proof of A8 below (phi(y_0) = log r, phi = 0 beyond sup-norm radius r). Then delta is at most theta_0/(j log r) on the at most 8j + 4 links between shells j and j + 1, and 1 - cos(delta/2) <= delta^2/8, so C(theta) <= (beta theta_0^2/(2 log^2 r)) sum_{j=1}^{r-1} (8/j + 4/j^2) <= 4 beta theta_0^2 (log r + 2)/log^2 r. This tends to 0 as r grows, at a rate free of the fibre size, of the pins and of the other planes. So no boundary condition on the base fixes the right orientation of a spin. This is the first half of the two-dimensional engine. It is blind: it holds verbatim for the U(1) corner.

**Theorem A8 (thin mixed loops decay at least like a power).** Let beta >= 1/32. Let p_0 != p_1 in F and y_0, y_1 in B with r = |y_0 - y_1|_infinity >= 2. Put

  W = (1/2) tr[ k(p_0, y_0)^(-1) k(p_1, y_0) k(p_1, y_1)^(-1) k(p_0, y_1) ] .

Then |mu(W)| <= exp(1/(64 beta)) r^(-1/(128 beta)), for every F and B. By A2 the same bound holds with the roles of fibre and base exchanged.
In the gauge theory W is the Wilson loop of the rectangle with corners (p_0, y_0), (p_1, y_0), (p_1, y_1), (p_0, y_1), in the doubly flat sector. W is invariant under all symmetries of A2, so the bound is not a consequence of A3.

Proof. Take n = e_3, so exp(theta J) = diag(e^(i theta/2), e^(-i theta/2)). Let M = k(p_0,y_0)^(-1) k(p_1,y_0) k(p_1,y_1)^(-1) k(p_0,y_1) and let a be its (1,1) entry; W = Re a and |a| <= 1. Under T_theta, M -> exp(-theta(y_0) J) M exp(theta(y_1) J), so a o T_theta = exp(-i (theta(y_0) - theta(y_1))/2) a. For real theta the change of variables gives

  mu(a) = exp(-i (theta(y_0) - theta(y_1))/2) Z^(-1) int a exp(E o T_theta) dk .

By A6, E o T_theta is a trigonometric polynomial in the numbers theta(y). So the right side is an entire function of theta in C^B. It is constant on R^B, hence constant. Put theta = i alpha with alpha real. By A6 with delta = i eta, eta = alpha(y') - alpha(y): Re(E o T_(i alpha) - E) = beta sum (cosh(eta/2) - 1) q_0 <= 4 beta sum over base links of (cosh(eta/2) - 1). So

  |mu(a)| <= exp[ (alpha(y_0) - alpha(y_1))/2 + 4 beta sum (cosh(eta/2) - 1) ] .

Take alpha(y) = -c phi(y), phi(y) = log(r / max(1, |y - y_0|_infinity)) for |y - y_0|_infinity <= r and 0 beyond, c = 1/(32 beta) <= 1. Then alpha(y_0) - alpha(y_1) = -c log r. The gradient of phi is 0 inside a shell {|y - y_0|_infinity = j} and on the links at y_0; it is at most 1/j on the at most 8j + 4 links between shell j and shell j + 1, 1 <= j <= r - 1. With cosh t - 1 <= (t^2/2) cosh t and cosh(1/2) < 2:

  sum (cosh(eta/2) - 1) <= 2 sum_{j=1}^{r-1} (8j + 4) c^2/(8 j^2) <= 2 c^2 (log r + 2) .

The exponent is at most -(c/2) log r + 8 beta c^2 (log r + 2) = -(log r)/(128 beta) + 1/(64 beta). QED.

Remarks. (i) The bound is blind: the same proof gives it for the U(1) corner, where a Gaussian computation gives a power law, so a power is the best a blind argument can give. (ii) In the isotropic Wilson model a 1 x r loop decays exponentially in r at every coupling (one-link conditional expectation, B. Simon and L. Yaffe; RECALLED, not rebuilt here). In the corner this argument is not available: the conditional law of one plane has an exact continuous symmetry instead of a strictly positive density per link variable in the direction of the loop.

### 3.4 The end-point of route S2 as one statement

**(Sigma-unif) (OPEN).** For every beta there are C and m > 0 such that, for all boxes F, B, all base sets Y, Y' and all bounded f, g, with f a function of the spins over Y and g of the spins over Y' (any fibre positions): |mu(f; g)| <= C |Y| |Y'| sup|f| sup|g| exp(-m dist(Y, Y')). The constants do not depend on F.

**Lemma A9 (assembly; PROVED GIVEN (Sigma-unif)).** (Sigma-unif) gives four-dimensional exponential clustering of the corner model for bounded local observables: if f and g depend on spins in sets of diameter at most D at sup-norm distance R, then |mu(f; g)| <= C' exp(-m (R - 2D)), with C' = C (D+1)^4.
Proof. Either the base projections or the fibre projections of the two supports are at distance at least R - 2D. In the first case apply (Sigma-unif). In the second, apply it after the exchange of A2, which maps the class of all boxes to itself. QED.

What (Sigma-unif) asks of the two-dimensional engine (rows 1007-1010): the pinned-cell stiffness iteration for the homogeneous space T of A4 with the right action of SU(2)^F, uniformly in F. By A5 the one-plane form is the O(4) class with one-sided backgrounds. Whether the posted proof covers one-sided backgrounds is not decided here: its text was not read in this session, and rows 1009 and 1077 read only its Section 3. The first half of the engine is A7. The second half (the bracket gain) is the open part. A plane-by-plane form does not suffice by itself: uniform conditional mixing of each plane given the others does not give joint mixing (two planes that determine each other are a counterexample to the bare implication), so the iteration has to run on T.

## Step 4. Part A, the bracket half: structure, and where it stops

The second half of the two-dimensional engine lowers the stiffness by a commutator term. Its text was not read in this session. What follows is my own computation of the second-order forms in the corner. It shows which twists can carry a gain. It does not prove a gain.

**Lemma A10 (second-order forms; PROVED).** Let e = <p_0, p_1> be a fibre link, <y, y'> a base link, delta = theta(y') - theta(y), and write m = m_e(y) = m_0 + i m.sigma, m' = m_e(y').
(a) Twist of the plane p_0 alone (or p_1 alone). The sheet moves by a one-sided multiplication. The symmetrized change of <m, m'> is -(1 - cos(delta/2)) <m, m'>. All four components of m enter. There is no axis-dependent part.
(b) Common twist of p_0 and p_1, same theta and axis n. The sheet moves by conjugation, m -> exp(-theta J) m exp(theta J). The symmetrized change of <m, m'> is -(1 - cos delta) (m_perp . m'_perp), where m_perp is the part of the vector m orthogonal to n. The components m_0 and m.n do not enter.
(c) In the state mu (free boundary), E[m_a m'_a] = E<m, m'>/4 for each of the four components a. So E[m_perp . m'_perp] = E<m, m'>/2.
(d) For the U(1) corner, a common twist of p_0 and p_1 leaves m_e unchanged.
Proof. (a) is A6. (b) Conjugation fixes m_0 and rotates the vector m about n; the angle between the two rotations is delta; m . R m' = (m.n)(m'.n) + cos(delta) m_perp . m'_perp + sin(delta) (odd term). (c) By A2 with d(p_0) and d(p_1) independent, the pair (m, m') -> (d_0^(-1) m d_1, d_0^(-1) m' d_1), and these maps act on R^4 as all of SO(4). (d) The group is abelian. QED.

**Reading (ARGUED).**
1. A gain at second order needs twists that act on a sheet as a rotation in a two-plane of R^4, as in (b). Then the stiffness reads only two of the four components of the sheet, and fluctuations forced into the other two (by A7 about a second axis) lower it. This is the O(N) mechanism. One-sided twists, as in (a), read all four components and gain nothing at this order.
2. So the one-plane class of A5 (O(4) with a one-sided background) is too small for the iteration at second order: its only symmetries are of type (a). The iteration has to use twists of several planes at once, on the space T of A4. For a fibre block D twisted in common, the interior links are of type (b) and the boundary links of type (a).
3. (d) shows that for U(1) the interior links cost nothing, so a block twist has boundary-order stiffness. For SU(2) the interior links cost (b). So the non-abelian corner is stiffer under common block twists, and softer only after the second axis has acted. A proof of (Sigma-unif) has to win this trade at every coupling.

**Where Part A stops.** (Sigma-unif) is OPEN. First missing step: a lower bound, uniform over pins, over the fibre size and over the configuration of the other sheets, on the components of the sheet fields along the twist axis in a cell of side exp(c beta u), in the form that the two-dimensional engine has for one sheet (row 1009: OpenAI O(3) Lemma 2.3). I did not prove it and did not find a counterexample. Nothing in A1-A10 fails for the U(1) corner except A10 (b)-(c), so the selective content of Part A is confined to this missing step.

## Step 5. Part B: the descent, and why route S2 does not reach (N-phys)

Now the full Wilson model on F x B with plane couplings beta_L (plane 12), beta_T (plane 34), beta (mixed).

**Definition.** For Omega: F x B -> SU(2), the partial gauge transformation T^B_Omega maps U_nu(x) -> Omega(x) U_nu(x) Omega(x+nu)^(-1) for nu = 3, 4 and fixes U_mu for mu = 1, 2. It preserves Haar measure. T^F_Omega is the same with the roles exchanged. T^B_Omega composed with T^F_Omega is a gauge transformation.

**Lemma B1 (exact; PROVED).** Under T^B_Omega every 34-plaquette trace and every 12-plaquette trace is unchanged. The mixed plaquette at (x; mu, nu) becomes (1/2) tr[ V_mu(x) U_nu(x+mu) V_mu(x+nu)^(-1) U_nu(x)^(-1) ], with V_mu(x) = Omega(x)^(-1) U_mu(x) Omega(x+mu).
Proof. The 34-plaquette is conjugated by Omega(x). The 12-plaquette has no changed link. For the mixed one, insert Omega(x) Omega(x)^(-1) and use cyclicity. QED.

**Lemma B2 (one plane; PROVED).** Let Omega = omega(y) on the plane p_0 and 1 elsewhere. Then a mixed plaquette P at (p_0, y) on the base link (y, nu) becomes (1/2) tr[P D_nu(y)], with D_nu(y) = U_nu(p_0, y) omega(y+nu) U_nu(p_0, y)^(-1) omega(y)^(-1). So the cost is a function of the covariant difference of omega with respect to the base links of the plane p_0 itself. The other planes do not enter D.

**Lemma B3 (the corner symmetries are partial gauge transformations; PROVED).** In the corner variables (A0), T^B_Omega is k(x) -> [g(x)^(-1) Omega(x) g(x)] k(x). The left symmetry c(y) of A2 is T^B_Omega with Omega covariantly constant along the fibre links. The right symmetry d(p) is T^B_Omega with Omega = h d(p) h^(-1), covariantly constant along the base links. The twist of A6 is T^B_Omega with Omega(p_0, y) = h exp(theta(y) J) h^(-1).

**Lemma B4 (one frozen orientation; PROVED, on file in substance).** Let beta_T = infinity and beta_L arbitrary. In the gauge U_nu = 1, the map T^F_Omega with Omega = exp(theta(y) J) on the plane p_0 keeps every 12-plaquette trace and has the gradient cost of A6. It moves no function of the 12-plaquette traces at a fixed base point.
So on this face the twist survives for every beta_L, and it is a twist by the residual gauge group. This is the Ward step of row 1077. The observables that it does not move are exactly the ones created by unfreezing: the fibre plaquette traces. Their mixing along the base is the lane's (SING) (row 1053 6.9: "singlets are moved by flux twists").

**Lemma B5 (both orientations unfrozen; PROVED inequality).** Let J be a field of unit vectors of su(2) on the four corners of a plaquette with holonomy u, (1/2) tr u = x. The sum over its four links of |J - (transported neighbour)|^2 is at least (1 - x^2) sin^2(angle between J at the base corner and the axis of u).
Proof. Transport to one corner; the adjoint action is an isometry; the four defects add up to at least |J - Ad(u) J| = 2 |sin(phi/2)| sin(angle), with cos(phi/2) = x; then Cauchy-Schwarz. QED.
By B2 a twist exp(theta J) of one plane with constant theta has D = 1 only if J is covariantly constant along that plane. B5 bounds the defect below by the non-commuting part of the plane's own curvature. Row 1018's Lemma NAB bounds E(1 - x^2) below by xbar/(2 beta), so the defect energy beta (1 - x^2) is of order one per plaquette at every coupling. This is Lemma FR of row 1011 and Lemma 5.1a of row 1181 in the present variables. It is not new.

**Verdict on route S2 (ARGUED from A4, B3, B4, B5).** The corner has a full set of symmetric twists because it has no singlet at all: its base-site space T is one orbit. The first unfreezing (B4) keeps every twist and creates singlets that no twist moves. The second unfreezing (B5) removes the twists. So the two descents of S2 do not carry the corner's mechanism to the isotropic point. The first failing step of S2 as a route to (N-phys) is the first unfreezing: mixing of the fibre plaquette traces along the base at beta_T = infinity, beta_L finite. Explicit failure: the function x_12(p, y) is invariant under every T^F_Omega of B4, so A7 and A8 bound none of its correlations. This is the neutral half again, in the form that rows 1053 and 1076 already hold as (SING).
