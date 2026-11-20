lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T12:03Z

# gap-mini-solve-f-fable: the mass gap of four-dimensional SU(2) Yang-Mills

Queue row 1195. Worker: Claude Fable 5.2, max effort, Mac mini worker 3, pinned at commit 9c5f9600f. Started 2026-11-20T00:03Z.

Labels used below: PROVED (every step written here or in a cited library file), ARGUED (an argument with a named missing step), GUIDE (heuristic or numeric, not a proof step), OPEN.

Status of this file: in progress. Sections are appended one step at a time.

## 0. Log

- 00:03Z. File created. Reading FINISH.md (rules, row 1195), GOAL.md, `parts/gap.md`, and the earlier gap-mini results.
- 00:25Z. Read in full: GOAL.md; FINISH.md L1-84 and L299-356 (rules); row 1195; `parts/gap.md` (all 322 lines); `library/gap-council-brief.md`; `library/gap-council-synthesis.md`; the FINISH RESULT lines of rows 1177-1196. Not read: the other 460 `library/gap-*` files (searched by grep when a statement is used).

## 1. Repo search: where the lane stands (what I rely on, by row)

All of this is prior work of the lane; none of it is mine. Credit: Balaban (ultraviolet renormalization group), Sussman and Alpoge with Claude and Codex (the complete account), the lane's rows as cited.

- Target. Jaffe-Witten for SU(2): a Wightman/OS theory on R^4 with spectrum {0} and [Delta, infinity). Lattice form: Wilson SU(2) on periodic tori along the asymptotically free trajectory (brief, Section 1).
- Consumer side, on file: one seed at one physical box size gives a uniform gap on all larger dyadic boxes and carries to finer cutoffs (Theorems S, SH, rows 697-705; Theorem ZD-c, row 720). The wall (W): bounded Casimir excess (BDD-Delta) together with unbounded size-times-gap (Z-UNB).
- The gap clause alone needs less (rows 731, 1161, 1179 Theorem BP, unchecked in part): the one-cube physical neutral bound (N-phys) plus the continuum datum. By rows 1180 and 1184 (checked by row 1187), (N-phys) is a neutral lattice gap at arbitrarily weak coupling with a lower bound of asymptotic-scaling type.
- Every positive result on file is non-selective (it also holds for compact U(1), a frozen group, or a product with a massless factor). The missing piece is one selective inequality at order-one effective coupling (brief, Section 3).
- The sibling rows with this same plain brief (1188-1190; 1193, 1194 running) screened 12 to 17 standard attacks each and found all on file.

Consequence for this row: a further screening of standard routes has no value. This row picks one mechanism, checks it against the record by grep, and works it to a proof or to its first failing step.

## 2. How best to attack it (step 1; written 00:35Z)

### 2.1 What a proof has to contain (ARGUED, from the record)

1. The only posted mechanism that crosses an order-one band in an asymptotically free model is OpenAI's stiffness iteration for the 2D O(4) model (read by row 1009, `library/prior/gap-o4-pinned-cell-read-opus.md` L57-200). Its parts are: (a) a rigid continuous symmetry; (b) the stiffness of a pinned cell as "direct cost minus current variance", with the start bound "drop the variance", uniform over all pins; (c) a lower bound on the current variance from the bracket term of the Ward identity (a Cramer-Rao step); (d) small stiffness gives decay of charged observables; (e) neutral observables by association.
2. For 4D SU(2) the port of (b) fails. Row 1011 (`library/gap-pinned-cell-gauge-max.md` Propositions A, W, B, B', SEAG, Lemma FR) proves: the direct term of a fixed-colour link rotation is mass-like, so "drop the variance" gives a bound that grows with the cell. I re-derived this independently before reading row 1011 and agree with it.
3. The port of (d)-(e) has no content: every gauge-invariant observable is neutral. So the neutral sector, which the 2D proof gets from association, is the whole problem (the lane's (SING)).
4. A statement that is uniform over all boundary values is false in 4D at window couplings (row 1072, Proposition CA-FAIL: pinned slabs carry an ordered 3D O(4) magnet). So a 4D proof has to be in the law of the model. The lane's periodic engine (Theorem S, `library/gap-crux-restate.md` 3.4) is of that kind, and it needs a seed.
5. "Area law gives the gap" is false in the class of lattice actions (row 1065: a critical end point inside a confined phase). So the neutral gap needs its own input, and at one fixed lattice coupling that input contains a number.

### 2.2 Ideas screened in this step and found on file (not attacked)

| Idea | Where it is on file | Verdict there |
|---|---|---|
| Rigid group of time-independent gauge transformations in temporal gauge; stiffness in time only | rows 1016, 1190 | gives static-charge decay only; true for U(1) |
| Area law implies the neutral gap | row 1065 4b, row 1190 item 17 | false in the class |
| Small box with 't Hooft twist (no torons, perturbative gap) as a seed | `gap-crux-restate.md` C5, (AC'-lat), row 679 | the twisted gap is scale invariant at weak coupling: side times gap is a constant near pi, so Theorem S cannot start; doubling a twisted side is a signed trace (TM-c) |
| Conditional abelian model in maximal-torus coordinates | rows 1188 (Lemma HF), 1190 (sign pattern) | frustrated; no Ginibre structure |
| Jensen bound with a fixed lab-frame translation | rows 697 (Way 3), 1181 (Proposition J), 1179 | mass-like, of area order |

Correction (00:55Z): an earlier version of this section called the next remark new and PROVED. It is neither. It is ARGUED, and it is on file as Route T (rows 842, 859, 862, 880; row 1181 Section 5.3 table: "No seed holds in the thin box").

- (2.2a, ARGUED, on file) For the 2D engine of Corollary S2 with the two short sides as a fixed twisted fibre, a seed at weak coupling is plausible, because the fibre has a tree-level gap. It gives nothing for 4D: the fibre size cannot be doubled inside the engine.

### 2.3 The attack chosen

The mass-like term of item 2 is the only reason that the start bound of the stiffness iteration fails at an abelian pin. For an abelian pin there is an exact structure that row 1011 did not use: in Hopf coordinates on each link, U = cos(phi) e^(a chi) + sin(phi) e^(a vartheta) j, Haar measure is a product measure in (phi, chi, vartheta), the diagonal phase chi is a U(1) lattice gauge field, and the marginal law of chi after integration over (phi, vartheta) is exactly invariant under U(1) gauge transformations. A shift of chi alone preserves Haar measure. So a Jensen bound in chi after the off-diagonal variables are integrated has no seagull term by construction: its cost is a form in the curl of the shift.

Plan: (i) grep the record for this construction; (ii) state the exact inequality; (iii) decide whether its right side is classical in size, or mass-like through a Meissner response of the off-diagonal variables; (iv) if mass-like in the unfixed ensemble, add a U(1)-invariant soft gauge weight and repeat.

Known risk, written before the work: in the unfixed ensemble the gauge orbit acts as a charged Stueckelberg field for chi, so the chi-marginal should be Higgs-like and the bound mass-like with coefficient b. Then the construction needs the soft maximal-abelian weight, and its open step is a bound on the helicity modulus of the off-diagonal variables.

## 3. The attack: the start bound at an abelian pin (step 2; written 00:55Z)

### 3.0 Target and repo match

Target (S1'): there is a constant C such that, for every box cell c, every b > 0 and every real boundary field theta,

  F_c(e^(a theta)) - F_c(1) <= C b cl(theta),   cl(theta) := min over real extensions theta~ of sum_p w_p (1 - cos (d theta~)_p).

Notation is row 1011's (`library/gap-pinned-cell-gauge-max.md` 3.1): F_c is the pinned free energy, a is a fixed unit imaginary quaternion, w_p the plaquette weights. For U(1), (S1') holds with C = 1 by one line (row 1011 3.2).

Repo match: (S1') with C = 1, in Hessian form, is the statement that row 1011 4.4 leaves OPEN ("H_c(1; a theta) <= b times the classical action of the harmonic extension ... is OPEN; it is not a one-line bound"); `library/gap-boundary-q.md` L56 repeats it as open; check 1014 names the unproved route "omega = 1 minimises F_int". I found no row that attacks it. It is the base bound (M2) of a stiffness iteration, restricted to abelian pins. Kind of result sought: proof of a step the lane leaves open.

What (S1') would and would not give. It would be a first size-uniform non-perturbative bound on a Schrodinger-functional stiffness. It would not move (W): abelian pins are not closed under conditioning on cell boundaries, so it has no consumer on file (row 1011 7.1). I attacked it because it is the smallest statement in which the mass-like term has to cancel.

### 3.1 Lemma F1 (Hopf coordinates; PROVED; the words are on file in row 1181 5.1, the formula with its signs is written here)

Identify a with i, so that C_a := span{1, a} is a copy of the complex numbers, and fix a unit imaginary j orthogonal to a. Every U in SU(2) is U = D + W j with D, W in C_a and abs(D)^2 + abs(W)^2 = 1. Write D = cos(phi) e^(a chi), W = sin(phi) e^(a vartheta), phi in [0, pi/2]. Then:

- (a) Haar measure is 2 sin(phi) cos(phi) d phi (d chi / 2 pi) (d vartheta / 2 pi).
- (b) j z = conj(z) j for z in C_a; (A + B j)(C + E j) = (A C - B conj(E)) + (A E + B conj(C)) j; U^(-1) = conj(D) - W j.
- (c) The gauge transformation g_x = e^(a lambda_x) acts by chi_l -> chi_l + lambda_x - lambda_y, vartheta_l -> vartheta_l + lambda_x + lambda_y, phi_l fixed (l from x to y). So chi is a U(1) lattice gauge field, and W is a link field with charge one at each end.
- (d) For a plaquette with links 1, 2, 3, 4 in row 1011's order (U_p = U_1 U_2 U_3^(-1) U_4^(-1)):

  t_p = Re[ D_1 D_2 conj(D_3) conj(D_4) ] - Re[ D_1 D_2 W_3 conj(W_4) ] - Re[ W_1 conj(W_2) conj(D_3) conj(D_4) ] + Re[ W_1 conj(W_2) W_3 conj(W_4) ]
        + Re[ D_1 W_2 D_3 conj(W_4) ] + Re[ D_1 W_2 conj(W_3) conj(D_4) ] + Re[ W_1 conj(D_2) D_3 conj(W_4) ] + Re[ W_1 conj(D_2) conj(W_3) conj(D_4) ].

Proof. (a) is the volume element of S^3 in these coordinates. (b): a j = - j a gives the first identity; the others follow by multiplying out. (c): e^(a lambda_x) W j e^(-a lambda_y) = e^(a lambda_x) W e^(a lambda_y) j by (b). (d): by (b), U_1 U_2 = (D_1 D_2 - W_1 conj(W_2)) + (D_1 W_2 + W_1 conj(D_2)) j and U_3^(-1) U_4^(-1) = (conj(D_3) conj(D_4) - W_3 conj(W_4)) - (conj(D_3) W_4 + W_3 D_4) j; the real part of the product is Re[A C - B conj(E)] with these four entries. Hand check of the signs: U_1 = U_2 = j, U_3 = U_4 = 1 gives U_p = -1 and the third monomial gives -1; U_3 = U_4 = j gives U_p = (-j)(-j) = -1 and the second monomial gives -1; the six other pairs of j's and the case of four j's give +1 from monomials 5, 6, 7, 8 and 4. QED

Two monomials carry a minus sign. This is the sign pattern of rows 1188 (Lemma HF) and 1190.

### 3.2 Lemma F2 (Jensen through the diagonal marginal; PROVED; I found no statement of it on file)

Let the pins be abelian, omega_l = e^(a theta_l). For a real field chi on the interior links put

  rho(chi; theta) := integral over (phi_l, vartheta_l), l interior, of exp(A_c(U(phi, chi, vartheta); e^(a theta))) against the product of 2 sin(phi) cos(phi) d phi d vartheta / 2 pi,

so that Z_c(e^(a theta)) is the integral of rho(chi; theta) against the product of d chi / 2 pi. Then:

- (a) (exact U(1) invariance) For every real function lambda on the sites of c: rho(chi + d lambda; theta + d lambda) = rho(chi; theta), with (d lambda)_l = lambda_tail - lambda_head.
- (b) For every real field u on the interior links and every pair theta, theta':

  F_c(e^(a theta')) - F_c(e^(a theta)) <= J(u) := E_theta[ log rho(chi; theta) - log rho(chi + u; theta') ],

  where E_theta is the Wilson law of the cell with pins e^(a theta).
- (c) J(u) is unchanged if (u, theta') is replaced by (u + d lambda, theta' + d lambda). In particular J = 0 if (u, theta' - theta) = d lambda.
- (d) J(u) <= E_theta[ A_c(U; e^(a theta)) - A_c(T U; e^(a theta')) ] for every map T that shifts chi by u and acts on (phi, vartheta) by a bijection that preserves their reference measure and may depend measurably on chi. So J(u) is at most every first-moment bound of this kind, the one of row 1181 Lemma 5.1a included.

Proof. (a) Apply the gauge transformation e^(a lambda) (Lemma F1 (c)); the action is invariant, the pins become e^(a (theta + d lambda)), and the shift of vartheta is absorbed by the translation invariance of d vartheta. (b) The product of d chi is translation invariant, so Z_c(e^(a theta')) / Z_c(e^(a theta)) = E_theta[ rho(chi + u; theta') / rho(chi; theta) ]; apply Jensen to the exponential. (c) from (a). (d) Let nu be the conditional law of (phi, vartheta) given chi under E_theta, with density exp(A_c(chi, .; theta)) / rho(chi; theta). By the change of variables T and Jensen, log rho(chi + u; theta') >= log rho(chi; theta) + E_nu[ A_c(T U; theta') - A_c(U; theta) ]. QED

Second-order form (the derivatives exist: all integrands are smooth on compact sets). For theta' = theta + eps theta_dot and u = eps u_dot, with Y the vector field that shifts (chi, theta) by (u_dot, theta_dot):

  H_c(theta; theta_dot) <= E_theta[ - Y Y A_c ] - E_theta[ Var( Y A_c | chi ) ].

The first term is the direct term of row 1011 Proposition A for the diagonal shift. The second is the part of the current variance that survives conditioning on chi. The loss against the exact formula is Var( E[ Y A_c | chi ] ).

Meaning. By (c) the right side of (b) has no cost for exact shifts. The first-moment bound of row 1181 Lemma 5.1a charges exact shifts at volume order, because it does not rotate W. So Lemma F2 removes the part of the mass-like term that comes from the gradient part of the shift. What is left is the response of the off-diagonal variables to a co-exact shift.

### 3.3 First failing step in the Wilson ensemble (ARGUED; three points)

Claim: in four dimensions J(u) is of mass form, with a coefficient of order b, for co-exact u. So Lemma F2 does not give (S1').

1. At large b the interior field is close to a pure gauge g_x g_y^(-1) with g Haar distributed at interior sites (no gauge is fixed). Put n_x := g_x^(-1) a g_x in S^2. The diagonal phases are then chi = d lambda + c(n), with c(n) the phase of the diagonal entry of the coset representatives, and d chi = d c(n) is the pull-back of the area form of S^2 under n.
2. A pull-back of a 2-form from a surface is decomposable. So the field strength f = d chi of such a chi obeys f wedge f = 0. In four dimensions that is one equation per site: closed 2-forms have 3 degrees of freedom per site and n has 2. In two and three dimensions there is no such equation.
3. So in 4D the law of chi sits within distance of order b^(-1/2) of a set of codimension one per site, and a co-exact shift u leaves that set at linear order. The cost is then of order b times the squared distance. In link variables: the infinitesimal gauge motions change chi in 3 directions per site, there are 4 links per site, and the missing direction is paid by the potential u itself, not by its curl.

This is the Higgs mechanism in plain form: the gauge orbit is a charged Stueckelberg field for chi. I did not prove the lower bound on J. The claim rests on the count in point 2.

### 3.4 Second way: a soft covariant weight (PROVED identity; on file in substance as C7 of row 1013; stops at one named bound)

Lemma F3 (PROVED). Let M(U) := sum over interior links of cos(2 phi_l) = sum over l of a . Ad(U_l) a. For lambda_0 >= 0 let N(U) := integral over interior gauge transformations g of exp(lambda_0 M(U^g)). Then N is positive and gauge invariant, and for every bounded gauge-invariant f:

  integral of f e^(A_c) dU = integral of f exp(A_c + lambda_0 M - log N) dU.

N(U) is the partition function of the adjoint S^2 sigma model n_x = Ad(g_x^(-1)) a in the background U, with coupling lambda_0 and n = a on the boundary sites. The weight exp(A_c + lambda_0 M - log N) is invariant under abelian gauge transformations.

Proof. Change variables U -> U^g in the right side, use the invariance of f, A_c, N and Haar measure, and average over g. For the sigma-model form, cos(2 phi) = abs(D)^2 - abs(W)^2 = a . Ad(U) a, and Ad(g_x U_l g_y^(-1)) a paired with a equals n_x . Ad(U_l) n_y. QED

Lemma F2 holds with this weight in place of e^(A_c) (same proof; M does not depend on chi, N does). At large lambda_0 the weight concentrates on maximal-abelian frames, where sin^2(phi) is of order 1/b, and the argument of 3.3 does not apply. The frame n is then a sample of a quenched sigma model: a random covariant frame with no Gribov problem.

What is then needed is one bound, which I name and do not prove:

(HM) There are C and lambda_0(b) such that, in the weighted ensemble, E[ - Y Y (A_c - log N) ] - E[ Var( Y (A_c - log N) | chi ) ] <= C b sum_p w_p (d u)_p^2 for all u, uniformly in the size of the cell.

(HM) says that the off-diagonal variables, in a typical abelian background, have no Meissner response: their seagull term is cancelled by their conditional current variance up to a curl form with a bounded kernel. Exact U(1) invariance (Lemma F2 (a)) gives that the left side is a form in d u. It does not bound the kernel. At weak effective coupling the bound is the transversality of the one-loop vacuum polarisation; the account of Sussman and Alpoge on Balaban's method has it in block form (the gauge-invariant local effective action). At order-one effective coupling I have no tool. This is (N1)-(N2) of row 1011 7.4 in an exact form, with the frame supplied by Lemma F3.

### 3.5 Third way: shifts by the local flux (ARGUED; fails)

Idea: shift each plaquette by its own flux (d u)_p, which is small everywhere, in place of each link by its potential u_l, which is of order (flux) x (size). Then a frame defect would be multiplied by the flux, not by the potential.

It fails at second order. A link map U_l -> exp(xi_l) U_l with the covariant curl of xi equal to (d u) n has xi = u n + xi', and the second-order term of row 1011 Proposition A contains kappa_p(xi) . s_p with kappa of order u^2 abs(D n). With abs(D n) and abs(s_p) of order b^(-1/2) this is of order u^2 per plaquette after the factor b: the same seagull, quadratic in the potential. In plaquette variables with Bianchi constraints the shift does not preserve the constraint surface, for the same reason. A version that rotates the off-diagonal field in wave packets of size R, each in its own local abelian gauge, has a cost of order (d u)^2 per logarithmic scale of R, so a bound b + C log S at best (heuristic count, no proof). It also needs a typical field.

### 3.6 What is PROVED about (S1') (small)

Proposition F4 (PROVED; C = 1; cells with no interior plaquette). Let c be a box with all sides S_mu >= 2 whose interior sites lie on one line (S_mu = 2 for all directions but at most one), so that the links between interior sites form a path and no plaquette has four interior corners. Then for every b > 0, every strength field in [0, b] and every theta: F_c(e^(a theta)) - F_c(1) <= b cl(theta).

Proof. Fix the gauge in which all links between interior sites are 1 (a tree). The remaining interior links q_i join an interior site to a boundary site. The interior of a box is a product of intervals, so a plaquette cannot have two diagonal interior corners with the other two on the boundary; hence every plaquette that is not a pin has exactly two links q_i, q_j, and its trace is Re(q_i^(-1) q_j P_ij) with P_ij = e^(a alpha_ij) a product of pins. By Lemma F1 (b), Re(q_i^(-1) q_j P) = cos(phi_i) cos(phi_j) cos(chi_j - chi_i + alpha_ij) + sin(phi_i) sin(phi_j) cos(vartheta_i - vartheta_j + alpha_ij) up to the orientation conventions of the two links: given the amplitudes the model is two independent XY models with couplings b_p cos cos and b_p sin sin, each with the abelian twists alpha up to sign. For an XY model the shift of its phases by a field mu is measure preserving and changes each bond by exactly the twist, so Jensen gives a cost of at most sum K_ij (1 - cos(alpha_ij + (d mu)_ij)) (the sine terms have mean zero by the reflection of all phases at alpha = 0). Use the same mu, up to sign, in both models: the total is at most sum over bonds of b_p (cos(phi_i) cos(phi_j) + sin(phi_i) sin(phi_j)) (1 - cos(alpha + d mu)) <= b sum (1 - cos(alpha + d mu)), since the bracket is cos(phi_i - phi_j) <= 1. A ratio of integrals is at least the infimum of the ratio of the integrands, so the bound holds after integration over the amplitudes. The minimum over mu, with the pin plaquettes added, is b cl(theta): the phases mu_i of the links q_i are all the interior freedom of an abelian extension in this gauge. QED

Remarks. (i) This is the two-circle decomposition of the O(4) model that OpenAI use in their Section 3.11.3 (row 1009 L183), applied to a thin gauge cell (row 1011 Lemma EMB). (ii) Every 2D cell with equal strengths also satisfies the bound with C = 1, by the same two-circle argument: Z_c depends on the pins only through the boundary holonomy e^(a Theta) and equals the A-fold convolution of the plaquette weight, which is an O(4) chain q_0 = 1, ..., q_A = e^(a Theta) with bonds Re(q_(k-1)^(-1) q_k); shift the phases chi_k by any mu_k with mu_0 = 0, mu_A = Theta mod 2 pi. (iii) The first cell outside the proposition has one interior plaquette. In the tree gauge its holonomy V is a non-abelian left twist on the bonds across one cut, and the two XY models mix. There the bound with C = 1 is undecided; I did not find a proof or a counterexample by hand.
