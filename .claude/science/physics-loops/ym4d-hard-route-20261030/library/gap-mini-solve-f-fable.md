lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T12:03Z

# gap-mini-solve-f-fable: the mass gap of four-dimensional SU(2) Yang-Mills

Queue row 1195. Worker: Claude Fable 5.2, max effort, Mac mini worker 3, pinned at commit 9c5f9600f. Started 2026-11-20T00:03Z.

Labels used below: PROVED (every step written here or in a cited library file), ARGUED (an argument with a named missing step), GUIDE (heuristic or numeric, not a proof step), OPEN.

Status of this file: finished at 01:09Z (RESULT line at the end). Sections were appended one step at a time.

## 0. Log

- 00:03Z. File created. Reading FINISH.md (rules, row 1195), GOAL.md, `parts/gap.md`, and the earlier gap-mini results.
- 00:25Z. Read in full: GOAL.md; FINISH.md L1-84 and L299-356 (rules); row 1195; `parts/gap.md` (all 322 lines); `library/gap-council-brief.md`; `library/gap-council-synthesis.md`; the FINISH RESULT lines of rows 1177-1196. Not read: the other 460 `library/gap-*` files (searched by grep when a statement is used).

- 00:35Z. Step 1 written (Section 2): how to attack; five ideas screened and found on file.
- 00:55Z. Step 2 written (Section 3): the attack on the start bound at an abelian pin. Read for it: `library/prior/gap-o4-pinned-cell-read-opus.md` L57-200; `library/gap-pinned-cell-gauge-max.md` L127-262, L294-320, L438-512; `library/gap-crux-restate.md` L29-80, L86-231; `library/gap-mini-free-fable.md` L376-435.
- 01:03Z. Subsection 3.6 rewritten (a shorter proof that covers every cell; the first version is withdrawn).
- 01:07Z. Step 3 written (Section 4): verdict.
- 01:09Z. Search for the new statements in `library/open-core.md` and the FINISH rows; RESULT line.

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

Repo match: (S1') with C = 1, in Hessian form, is the statement that row 1011 4.4 leaves OPEN ("H_c(1; a theta) <= b times the classical action of the harmonic extension ... is OPEN; it is not a one-line bound"); `library/gap-boundary-q.md` L56 repeats it as open; check 1014 names the unproved route "omega = 1 minimises F_int". FINISH rows 1011, 1014 and 1016 list "the Schrodinger-functional bound at the trivial pin" as still OPEN. `library/open-core.md` has no entry for it (grep for trivial pin, abelian pin, start bound: no match). I found no row that attacks it. For Lemma F2 and (HM) below, a grep of `library/`, `library/prior/`, `library/open-core.md` and FINISH.md for diagonal phase, diagonal marginal and the integration of the off-diagonal variables gave no match; the substance of (HM) is (N2) of row 1011 7.4. It is the base bound (M2) of a stiffness iteration, restricted to abelian pins. Kind of result sought: proof of a step the lane leaves open.

What (S1') would and would not give. It would be a first size-uniform non-perturbative bound on a Schrodinger-functional stiffness. It would not move (W): abelian pins are not closed under conditioning on cell boundaries, so it has no consumer on file (row 1011 7.1). I attacked it because it is the smallest statement in which the mass-like term has to cancel.

### 3.1 Lemma F1 (Hopf coordinates; PROVED; the words are on file in row 1181 5.1, the formula with its signs is written here)

Identify a with i, so that C_a := span{1, a} is a copy of the complex numbers, and fix a unit imaginary j orthogonal to a. Every U in SU(2) is U = D + W j with D, W in C_a and abs(D)^2 + abs(W)^2 = 1. Write D = cos(phi) e^(a chi), W = sin(phi) e^(a vartheta), phi in [0, pi/2]. Then:

- (a) Haar measure is 2 sin(phi) cos(phi) d phi (d chi / 2 pi) (d vartheta / 2 pi).
- (b) j z = conj(z) j for z in C_a; (A + B j)(C + E j) = (A C - B conj(E)) + (A E + B conj(C)) j; U^(-1) = conj(D) - W j.
- (c) The gauge transformation g_x = e^(a lambda_x) acts by chi_l -> chi_l + lambda_x - lambda_y, vartheta_l -> vartheta_l + lambda_x + lambda_y, phi_l fixed (l from x to y). So chi is a U(1) lattice gauge field, and W is a link field with charge one at each end.
- (d) For a plaquette with links 1, 2, 3, 4 in row 1011's order (U_p = U_1 U_2 U_3^(-1) U_4^(-1)):

  t_p = Re[ D_1 D_2 conj(D_3) conj(D_4) ] - Re[ D_1 D_2 W_3 conj(W_4) ] - Re[ W_1 conj(W_2) conj(D_3) conj(D_4) ] + Re[ W_1 conj(W_2) W_3 conj(W_4) ]
        + Re[ D_1 W_2 D_3 conj(W_4) ] + Re[ D_1 W_2 conj(W_3) conj(D_4) ] + Re[ W_1 conj(D_2) D_3 conj(W_4) ] + Re[ W_1 conj(D_2) conj(W_3) conj(D_4) ].

Proof. (a) is the volume element of S^3 in these coordinates. (b): a j = - j a gives the first identity; the others follow by multiplying out. (c): e^(a lambda_x) W j e^(-a lambda_y) = e^(a lambda_x) W e^(a lambda_y) j by (b). (d): by (b), U_1 U_2 = (D_1 D_2 - W_1 conj(W_2)) + (D_1 W_2 + W_1 conj(D_2)) j and U_3^(-1) U_4^(-1) = (conj(D_3) conj(D_4) - W_3 conj(W_4)) - (conj(D_3) W_4 + W_3 D_4) j; the real part of the product is Re[A C - B conj(E)] with these four entries. Hand check of the signs: U_1 = U_2 = j, U_3 = U_4 = 1 gives U_p = -1 and the third monomial gives -1; U_3 = U_4 = j gives U_p = (-j)(-j) = -1 and the second monomial gives -1; the four other pairs of j's and the case of four j's give +1 from monomials 8, 7, 6, 5 (pairs 13, 14, 23, 24) and 4. QED

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

### 3.6 What is PROVED about (S1') (elementary; rewritten 01:03Z)

A first version of this subsection proved the next statement for cells with no interior plaquette by a two-circle decomposition. The proof below is shorter and covers every cell; the earlier text is withdrawn.

Proposition F4 (PROVED; elementary; the upper-bound side of row 1011 Proposition B' at an abelian pin). Let c be a box with all sides S_mu >= 2, strengths in [0, b]. For every real boundary field theta,

  F_c(e^(a theta)) - F_c(1) <= b cl_0(theta),   cl_0(theta) := min of sum_p w_p (1 - cos (d theta~)_p) over the real extensions theta~ that vanish on every link between two interior sites.

Proof. (1) With all S_mu >= 2 a link between two boundary sites lies in a boundary face, so every link is a pin, joins an interior site to a boundary site, or joins two interior sites. The interior corners of a plaquette are none, one, two adjacent, or all four (the interior is a product of intervals). So a plaquette that is neither a pin plaquette nor an interior plaquette contains one pin (two interior corners) or two adjacent pins (one interior corner), and its trace is Re(e^(a alpha_p) Y_p) with alpha_p the signed sum of theta over its pins and Y_p in SU(2) its holonomy at theta = 0, based next to the pins. (2) Keep the interior links and change only the pins: by Jensen, F_c(e^(a theta)) - F_c(1) <= E_0[A_c(U; 1) - A_c(U; e^(a theta))], E_0 the law at the trivial pin. Re(e^(a alpha) Y) = cos(alpha) t(Y) - sin(alpha) a . s(Y). The constant gauge transformation j at all sites fixes the trivial pin and the law and sends a . s(Y) to - a . s(Y), so E_0[a . s(Y_p)] = 0. Hence the right side is sum over pin plaquettes of b_p w_p (1 - cos (d theta)_p) plus sum over the plaquettes of (1) of b_p E_0[t_p] (1 - cos alpha_p(theta)), and E_0[t_p] <= 1. (3) F_c(e^(a theta)) = F_c(e^(a (theta + d lambda))) for every real lambda on the boundary sites (row 1011 3.1). A boundary site with an interior neighbour has exactly one, so lambda is a field mu on the links between interior and boundary sites, and alpha_p(theta + d lambda) is the curl at p of the extension that equals mu on those links and 0 between interior sites. Minimise over lambda. QED

Corollaries. (i) If the interior sites lie on one line, every abelian extension is U(1)-gauge equivalent to one that vanishes between interior sites, so cl_0 = cl and (S1') holds with C = 1. (ii) Every 2D cell with equal strengths satisfies (S1') with C = 1: Z_c depends on the pins through the boundary holonomy e^(a Theta) only and is the A-fold convolution of the plaquette weight, an O(4) chain q_0 = 1, ..., q_A = e^(a Theta) with bonds Re(q_(k-1)^(-1) q_k) = cos cos cos(chi_k - chi_(k-1)) + sin sin cos(vartheta_(k-1) - vartheta_k); shift chi_k by any mu_k with mu_0 = 0 and mu_A = Theta mod 2 pi and use Jensen for the circle chi at fixed amplitudes. (iii) In general cl_0 is of mass form in the boundary field: a flux f per boundary plaquette on a cube of side S has cl_0 of order f^2 S^5 against cl of order f^2 S^4 (row 1011 4.2, reading). So Proposition F4 is the trivial bound, and it is sharp in order for the class supremum.

Lemma F5 (PROVED; exact form of the first cell with an interior plaquette). Let the interior sites of c be the four corners z_1, ..., z_4 of one plaquette, fix the gauge in which the links z_1 z_2, z_2 z_3, z_3 z_4 are 1, and let V be the link z_4 z_1. Write q_i for the links from interior to boundary sites, and say that a bond (i, j) crosses the cut if q_i starts at z_4 and q_j at z_1. With equal strength b outside the interior plaquette and strength b_V on it,

  Z_c(e^(a theta)) = (pin factor) x integral over psi in [0, pi] of (2/pi) sin^2(psi) e^(b_V cos psi) x integral over the amplitudes phi_i of Z_XY(b cos cos; alpha + psi 1_cut) Z_XY(b sin sin; alpha - psi 1_cut),

where Z_XY(K; gamma) is the partition function of the XY model on the bond graph with couplings K_ij and twists gamma_ij, and alpha = alpha(theta) as in Proposition F4.

Proof. Every bond is Re(q_i^(-1) L_ij q_j e^(a alpha_ij)) with L = V across the cut and 1 elsewhere. The substitution q -> g q, V -> g V g^(-1) shows that the q-integral is a class function of V; by the Weyl integration formula take V = e^(a psi). By Lemma F1 (b), q_i^(-1) e^(a psi) q_j = (conj(D_i) D_j e^(a psi) + W_i conj(W_j) e^(-a psi)) + (...) j, so the bond is cos(phi_i) cos(phi_j) cos(chi_j - chi_i + alpha + psi) + sin(phi_i) sin(phi_j) cos(vartheta'_j - vartheta'_i + alpha - psi) with vartheta' = - vartheta. QED

Meaning. The two circles of each link carry the flux of the interior plaquette with opposite signs. An abelian flux psi_0 through the interior plaquette is a shift of psi that helps one circle and costs the other. This is the frame obstruction of row 1011 (Lemma FR) at its smallest scale, in one exact formula. For this cell (S1') with C = 1 is one inequality between explicit integrals; I did not decide it.

### 3.7 Two remarks found on the way (small)

Remark F6 (PROVED; a shortcut that is not available). The plaquette function (U_1, U_2, U_3, U_4) -> t(U_1 U_2 U_3^(-1) U_4^(-1)) is not a positive-definite function on the product group SU(2)^4. A positive-definite function F on a group satisfies F(gamma^(-1)) = conj F(gamma). Here, with quaternion units i, j, k: F(i, j, k, 1) = t(i j k^(-1)) = t(k (-k)) = 1, and F(i^(-1), j^(-1), k^(-1), 1) = t((-i)(-j) k) = t(k k) = -1. So "Z_c is positive definite in the pins, hence maximal at the trivial pin" does not follow from the product of plaquette weights, as it does for an abelian group. The route "omega = 1 minimises F_c", named unproved by check 1014 (`library/gap-boundary-q.md` L56), stays unproved; I did not prove it another way.

Remark F7 (reading; ARGUED). For a half-space cell in the axial gauge along the normal direction, the pinned free energy at an abelian pin is minus the logarithm of the vacuum wave functional of the transfer operator at the abelian configuration e^(a theta), up to the pin plaquettes. In this form (S1') says: the SU(2) vacuum wave functional, on abelian configurations, is at least the C-th power of the free-photon one. I found no handle on it.

## 4. Verdict of this row (step 3; written 01:07Z)

### 4.1 The attack on (S1')

Not proved. No counterexample. Stop by the rule of three ways (How we work, item 11), on one named statement:

(HM) of 3.4: after a U(1)-invariant soft frame weight, the response of the off-diagonal link variables to a co-exact shift of the diagonal phases is bounded by C b times the curl energy of the shift, uniformly in the cell size.

Why each way failed.

1. Jensen through the diagonal marginal in the Wilson ensemble (3.2, 3.3): exact U(1) invariance removes the cost of exact shifts, but in four dimensions the diagonal phases of a nearly flat SU(2) field in a random gauge lie near a set of codimension one per site (f wedge f = 0), so a co-exact shift pays a mass term with coefficient of order b. ARGUED, not proved.
2. The same with a soft covariant frame (3.4): the mass term has coefficient of order one, and its cancellation is the transversality of the response of the off-diagonal variables with a bounded kernel. That is known only where the account's small-field analysis holds, and it is false as a pin-uniform statement (row 1011 Proposition B'). No tool at order-one effective coupling.
3. Shifts by the local flux (3.5): the potential returns at second order through the bracket term of row 1011 Proposition A.

Common reason, in one sentence: a first-moment comparison cannot see the cancellation between the seagull term and the current variance, and for pins the only exact Ward identities are those of gauge transformations (row 1011 Proposition W), so the cancellation is a statement about a response kernel, not about a symmetry.

What stands: Lemma F1 (d) (the plaquette in Hopf coordinates, with signs), Lemma F2 (Jensen through the exactly U(1)-invariant diagonal marginal, at most every first-moment bound of its kind), Lemma F3 (soft frame weight as a quenched adjoint sigma model; in substance row 1013 C7), Proposition F4 (the trivial bound b cl_0, equal to b cl exactly when the interior sites lie on a line; all 2D cells), Lemma F5 (exact two-circle formula for one interior plaquette: the two circles carry its flux with opposite signs), Remark F6. All PROVED by hand here, checked by no one, none selective, none with a consumer on the gap path.

### 4.2 Value for the wall

None directly. (S1') is a start bound at abelian pins. Abelian pins are not closed under conditioning, so even a proof of (HM) would not start an iteration (row 1011 7.1), and the lane's proved engine (Theorem S) reads periodic tori, not pinned cells. The row confirms, by one more independent derivation, the lane's reading: the 2D mechanism has no 4D gauge form because the gauge theory has no rigid frame, a pin-uniform class is false in 4D, and every gauge-invariant observable is neutral.

I do not propose a proof row on (HM) or on the inequality of Lemma F5: neither has a consumer.

### 4.3 Conditions of the run

- No numeric run. At 01:03Z memory_pressure reported 42 percent free, below the 50 percent gate, so the sign checks of Lemma F1 (d) were done by hand (thirteen test configurations, seven of them listed in its proof). No statement here rests on a computed value.
- No outside search. Sources read: this folder only (files named in Sections 0 to 2). The OpenAI O(4) text was read only through row 1009's reading note.
- No subagent. No file other than this one was edited.
- Times in this file are from `date -u` at the moment of writing.

### 4.4 Open after this row

(HM); (S1') with C = 1 for the cell of Lemma F5; "the trivial pin maximises Z_c" for a general cell; and, unchanged: (N-phys), the continuum datum, (BS), (W), any selective inequality at order-one effective coupling, the Jaffe-Witten mass gap.

RESULT: Row 1195 (Claude Fable 5.2 max, Mac mini worker 3, 00:03Z-01:09Z, plain brief; author only, checked by no one; no numeric run, memory was below the 50 percent gate; no outside search). The mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved. Attack chosen: the one statement in which the mass-like term of the 2D stiffness mechanism has to cancel, the start bound at an abelian pin (S1'), which FINISH rows 1011, 1014 and 1016 list as OPEN ("the Schrodinger-functional bound at the trivial pin"). It is NOT proved; stopped after three written ways at one named bound (HM), a size-uniform bound on the response of the off-diagonal link variables to a co-exact shift of the diagonal phases; (HM) is (N2) of row 1011 in exact form and has no consumer on the gap path. PROVED by hand, small, none selective: Lemma F1 (the plaquette in Hopf coordinates, eight monomials with signs); Lemma F2 (a Jensen bound through the exactly U(1)-invariant marginal of the diagonal phases; it is free on exact shifts and at most every first-moment bound of its kind); Lemma F3 (a soft covariant frame weight as a quenched adjoint sigma model; in substance row 1013 C7); Proposition F4 (the trivial bound b cl_0 at every abelian pin, equal to the classical bound exactly when the interior sites lie on one line, and for 2D cells); Lemma F5 (exact formula for the cell with one interior plaquette: two XY models that carry its flux with opposite signs); Remark F6 (the plaquette weight is not positive definite on the product group of its links, so "the trivial pin maximises Z_c" has no one-line proof). ARGUED: in four dimensions the bound of Lemma F2 is of mass form in the Wilson ensemble (the diagonal phases of a nearly flat field obey f wedge f = 0). Five further ideas were screened and are on file (Section 2.2). OPEN: (HM); (S1') with C = 1 for the cell of Lemma F5; and, unchanged, (N-phys), the continuum datum, (BS), (W), a selective inequality at order-one effective coupling, the Jaffe-Witten mass gap. Output library/gap-mini-solve-f-fable.md.
