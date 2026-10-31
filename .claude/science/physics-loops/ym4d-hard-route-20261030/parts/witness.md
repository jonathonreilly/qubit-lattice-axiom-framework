lead: Anthropic/claude-opus-5-5/max 1af63194-89a7-4dd0-9b82-781b24334af3
lease_until: 2026-10-31T21:00Z

## State of attack

**Formulation.** Test against Gaussian laws: the odd function T = (1/2) Tr(W_1 W_2 W_3) - (1/2) Tr(W_1 W_3 W_2) on three holonomies at one base point, in a closed sum around a rectangle (Text 3). NT1: two values of a connected correlator (Text 4). Everything is at a fixed level j at distance m from the top of the hard core's trajectory, with order of constants: rectangle size D, far distance R, L, then g_j small by m large.

**What is settled.**
- The coefficient does not vanish. For the corner cluster K_total = 0.6157 on the Wilson lattice, formula and Monte Carlo agree (Text 2.4). Of this, K_comp = 0.3969 is present in a Gaussian potential with no vertex, and the vertex part is K_vert = 0.2188 in Feynman gauge.
- **The gate's repair is half right.** T vanishes on the flux class F (W_i = exp(i b_i), b_i linear), and it does not vanish on the potential class G, where holonomies are path ordered. Sampling confirms this. F is separated from connection laws by the group law alone, so the force of NT2 is in G.
- **NT2 as worded cannot hold with the correlator chosen before the law**, on G (Proposition 1.1), and it is false in d = 2 (Proposition 1.2). Proposed wording: Text 6.
- **A separating test for G.** On a Gaussian potential whose covariance has a 90 degree rotation symmetry about a plaquette axis, the rectangle sum of T equals -24 times a far flux, with no regularity on the far field (Lemma 3.2, exact, checked to 1e-13). On the Wilson weight the sum is O(|x|^-5) by the Ward identity, and the vertex is what does it (Lemma 3.4, Proposition 2.2). So no such Gaussian potential has the Wilson tree values, under one square-summability assumption (B) (Theorem 3.5). Monte Carlo sees the opposite signs at D = 1, R = 2.
- **The whole difference is the vertex on a slice**, by (3.3). In d = 4 no translation-invariant Gaussian potential, with any colour structure and no regularity, has a slice on which the vertex vanishes (Theorem 3.8, by the limit k^3 -> 0). Compactness gives a finite family for link variance O(g^2) (Corollary 3.9), not explicit. At level j the soft limit replaces the Wilson vertex (Theorem 3.10). The step that needs d >= 4 is one line, and it fails at d = 3; d = 2 is a true counterexample.
- **Rate.** T needs third moments of the fibre to o(g) with the first-order term evaluated: nothing more than that, no rate on L, and any power beyond g works. Lemma 5.1 gives it on the convex route given a g-refined (H2). Lemma 5.1' gives it from (EI) of hard-core--independent, in the regular chart, with rate g^2 times a power of log(1/g). The statement is (OS_j) with (b+), (c+), (d+), under Requests.
- **Conditional theorems.** Theorem 4.1 is unconditional given Theorem 10.2; Theorem 4.3 gives the two values with no L-free constant, avoiding the gate's D5 (NT1). Theorem 5.3 (T at level j to o(g^4), by a recursion up the levels, no L-free constant beyond C_s), Lemma 5.4 (rectangle at level j), Theorem 5.5 (NT2 at fixed scale, classes (i) and (ii)), Theorem 3.19 (class (iii), colour-isotropic with no symmetry and bounded link variance, given (RANK-U)).
- A separated test exists on F: beta <T s_q>_c / Cov(s_p, s_q) tends to about -3.2 (Text 2.6), and T s has an exact sum rule. On G: Proposition 3.11, T on a near cluster against a far s_q, with coefficient g^6; at tree level the Gaussian value is exact and the Wilson value is smaller by the ratio 0.49, 0.36, 0.27, 0.20 at R = 6, 8, 10, 12.

- **The gate's D6 and D7 are reduced on the mapped route** (Lemma 5.6): a far rough region enters only through the law of the outer data, about which nothing is asked, at the cost of a radius growing like log(1 / g). With Lemma 5.1, (c+) is then an implication of hard-core--mapped's local form. On the independent route the regular chart is Lemma 5.1'; the R sector is not checked.

- **No symmetry, colour-isotropic, Wilson tree values at the lattice scale: done (Text 3.13).** The cubic form is VV = sum_p phi_p ^ m_p ^ n_p. If a slice S exists, then for b in S the matrix VV(., ., b) has rank at most 2 codim S, about half its size, with no assumption on S. A triangular argument (Lemma 3.14) and a budget on what a gauge can make vanish (Lemma 3.15) give rank at least 3.25 per site against the bound 2. So no real symmetric c has the Wilson tree values on a box of side 23 (Theorem 3.16), with no symmetry, no positivity and no bound on c. There is a uniform eps_0 with no bound on gauge parts at quadratic order (Theorem 3.17), and one finite family with one eps for all c tensor 1_3 up to link variance c_1 g^(4/3) (Corollary 3.18). The route separates d = 2 from d >= 3, as it must. It also shortens 3.8 for colour-isotropic c.
- **The sign difference is seen on blocked links.** Monte Carlo at beta = 16, one blocking step, rectangle D = 1, R = 2: blocked Wilson +0.249(65) against tree +0.203; Gaussian potential on the same coarse links -0.113(40) against tree -0.200; separation 4.8 sigma (Text 5.3).
- **Fine potential class: settled by the wording.** A Gaussian potential on a finer level m is a potential at its own scale, so a member of the family at level m applies to it, given the hard core at level m. A family at one fixed scale cannot do it: rough gauge modes have rank per coarse cell growing with the block volume (Text 3.12, route 2). So the family in the wording of NT2 must be countable, one finite family per level.

**Hardest remaining inequality in this part.** Three, in order. (1) **The level-j form of 3.13.** Lemma 3.14 uses a largest shift, and the level-j cubic form has exponential tails. The upper bound and the gauge dependence are unchanged. Current route (Text 3.14): many well-separated cells and one far plaquette. On the kernel of the site densities all near gauge parts drop out, and the cross form between cells is, at long distance, a kernel matrix between a moment map m of one cell and the dipole of another, with the level-j action absorbed. It has rank growing with the number of cells, against at most 6 from the far star. So only (RANK-U) is needed: m is not zero on one box, for every gauge in a bounded set. That is a universal lattice statement, with evidence and a WKB sketch, not proved. (2) **Colour mixing with no symmetry.** T is a colour singlet, so there is no labelled isotropy; the system has nine gauge functions per current per site, signature (+ + + + - - - - -), and the rank bound is empty. Numerics: residual 20 times smaller than one flavour, not zero, growing with the box. Translation-invariant colour mixing stays covered by 3.8. (3) **Link variance above g^(4/3)**, where the Levy triple enters.

**Routes tried and why they failed or were left.** (a) Oddness alone (the gate's lead): false on G. (b) One T with a far loop and the R^-3 decay of the Gaussian reading against R^-4: the gauge part of the covariance can tune one number, the tail term dominates in range, and the claim is gauge dependent. Replaced by the closed sum, which is gauge independent. (c) Plaquette planes chosen against an unknown far gradient (a table in 6 x 6 planes): works for smooth far fields and general C, needs regularity. Set aside after the rotation symmetry was seen to make the increments exactly uniform, which gives (3.1) with no regularity. It is the natural start for covariances with no symmetry and regular far fields: there the vector-valued form says span{u_mu(x)} has dimension at most 2 at each x, against 6 independent far modes in the curl. Not written. (d) Bessel over far loops with no assumption: bounds E on average only by R^-2 and needs a lower bound on a Gram matrix, which C need not have; (B) is the form that works for Theorem 3.5, and Lemma 3.7 removes it for translation-invariant C. (c') Three further routes on covariances with no symmetry: the soft limit for periodic covariances, norm bounds with a test tensor, and the rectangle alone. All fail, for the reasons in Text 3.12. (c'') Rank at most 2 of the far-field vectors u_mu(x): this is what regular far fields must obey, from parallel pairs, and I tried to contradict it by Taylor expansion at a point. It is an overdetermined system, 8 conditions per point on 6 gauge functions. The first order gives a linear constraint on the kernel of the map from 2-forms to covectors, and the second order only a relation on the second fundamental form of the distribution, with solutions. I stopped there. No contradiction found. (d') A first proof of Theorem 3.8 by flattening the form on three hyperplanes, for colour-isotropic C with (B): correct and replaced, because the soft-limit proof also covers colour-mixing gauge parts and needs no (B). A rank argument on tr(h_1 h_2) was the step before that, and it is not needed. (c-rank) Tensor rank of the far-near-near table (Text 3.12): a bound with no known lower bound to meet it. Replaced by the rank of a contraction (Text 3.13), which is a matrix. (c-two-boxes) For level j, the same rank argument on two boxes: main rank at most 12, too close to the far star, and for a simple far flux in a special gauge only 2. Replaced by many cells (Text 3.14). (e) Bounding the terms of the recursion in Theorem 5.3 rather than evaluating them: needs L-free constants not on offer. Replaced by g -> 0 at fixed L, with Lemma 5.2. (f) Second moment for the event G^c as in Theorem 10.7: gives g^4 and is not enough. High moments suffice.

**Hostile pass at this stop:** Text 7, 30 items. Corrections this stint: a sign in the current of two fields; prediction M2 restated after the gauge was found not to be Fock; two adversaries re-posed (one fooled by normalisation, one running away with t); the two-box form of 3.14 replaced. The L = 4 zero of the moment map for simple Fock flux, which looked like a counterexample, is a small-box artefact.

**Next action.** The order for the next stint: (1) a proof of (RANK-U): separate rough and smooth parts of t on a large box, following the sketch in Text 3.14, and treat modes staggered in three directions apart; or a counterexample by adversary at L >= 5. (2) Link variance above g^(4/3): the excess kurtosis of a truncated plaquette is (5/3) delta^4 whatever the correlation (`checks/witness_kurtosis.py`, K1 passes on ten random covariances), so a test of E s_p^2 bounds the Levy area; the Levy triple is then below g^4 for gauge modes uncorrelated with the flux. What remains there is the dressing of currents at relative order kappa, and correlated modes. (3) Colour mixing: linear elimination over several far sources gives a tensor condition; it is the next idea not tried. (4) The R sector for Lemma 5.1' if the hard core does not answer. (5) Respond to any gate.

## Obligations

- discharged: tree coefficient of the odd test on the Wilson lattice, formula, value 0.6157 at the corner cluster, Monte Carlo -> plan of NT2 (Proposition 2.1, 2.4)
- discharged: Ward identity at tree level, exact in any d, K_total depends only on the curvatures -> Lemmas 3.4, 5.4 (Proposition 2.2)
- discharged: rectangle identity for Gaussian potentials with rotation-invariant covariance, -24 Flux, exact -> Theorem 3.5 (Lemma 3.2)
- discharged: lattice Green's function bounds -> Lemmas 3.4, 5.4 (Lemma 3.3)
- discharged: Wilson rectangle sum O(|x|^-5) on Z^4 -> Theorem 3.5 (Lemma 3.4)
- discharged: no rotation-symmetric Gaussian potential with (B) and link variance O(g^2), any colour structure, has the Wilson tree values, explicit family -> NT2 at tree level (Theorem 3.5)
- discharged: closed form of the lattice cubic form on plane waves -> Theorem 3.8 (Lemma 3.6)
- discharged: symbol of a translation-invariant covariance, finite a.e. with no (B) -> Theorem 3.8 (Lemma 3.7)
- discharged: no translation-invariant Gaussian potential with any colour structure has the Wilson tree values in d = 4, and a finite family by compactness for link variance O(g^2) -> NT2 at tree level (Theorem 3.8, Corollary 3.9)
- discharged: H not zero on the orthocomplement from two distinct values of a correlator, given Theorem 10.2 -> NT1 (Theorem 4.1)
- discharged: tree consistency of the coefficient across levels, from the tropical definition of F -> Theorem 5.3 (Lemma 5.2)
- implication: first-order local Gaussian limit with a cut, given Steps 1 to 4 of the convex library and a g-refined (H2) -> (c+) on the mapped route (Lemma 5.1)
- implication: first-order local Gaussian limit in the regular chart, given (EI) and the cluster library, with the split of Psi as stated -> (c+) on the independent route (Lemma 5.1')
- implication: full local Gaussian limit at level j as g_j -> 0 at fixed L, and with it (WIT+) with no L-free constant, given (FF), (OS_j) uniformly in j, the flow, C_s free of L -> NT1 (Theorem 4.3, Corollary 4.2)
- implication: T at level j to o(g_j^4), given (FF), (OS_j) with (b+), (c+), (d+) uniformly in j, the flow, C_s free of L -> Theorem 5.5 (Theorem 5.3)
- implication: rectangle at level j, uniform in j and L, given gauge and lattice covariance, strict locality and componentwise linearisation of M -> Theorem 5.5 (Lemma 5.4)
- implication: no-slice theorem at level j by the soft limit, given gauge invariance of F_j and symbol bounds on H_j and F_j^(3), uniform in j -> Theorem 5.5 (Theorem 3.10)
- implication: NT2 at a fixed physical scale against classes (i) and (ii) of Gaussian potentials, given Theorems 3.5, 3.10, 4.3, 5.3 and Lemma 5.4 -> NT2 (Theorem 5.5)
- implication: separated form of the test against G, T on a near cluster with a far plaquette energy, given the recursion of Theorem 5.3 at higher degree -> a separated test against G (Proposition 3.11)
- unchecked: C_s free of L in the lift bound (a), at the level needed in the recursion, given hard-core--independent Lemma 10.1 for the abelian form -> Theorems 4.3, 5.3
- unchecked: covariance of the field-chosen base point under reflections and rotations about cell centres -> Lemma 5.4
- unchecked: symbols of H_j and F_j^(3) as asked in Theorem 3.10, given I(k)(a) and Lemma 10.1 of hard-core--independent -> Theorem 3.10
- implication: first-order local Gaussian limit on G with far rough cells, the gate's D6 and D7, on the mapped route, given (H1)-(H3) in the ball with the g-refined (H2), (A1), rarity of Omega near y', (Loc_k) -> (c+), Theorems 4.3, 5.3 (Lemma 5.6)
- gap: the statements Lemma 5.6 and 5.1' consume, namely (H1)-(H3) in the ball, (A1), (Loc_k), or (EI) with the R sector, together with (FF_j) and the lift bound, uniform in j; producer hard-core -> Theorems 4.3, 5.3
- discharged: plaquette form of the Wilson cubic vertex, VV = sum_p phi_p ^ m_p ^ n_p, K_vert = 24 VV -> Theorem 3.16 (3.8)
- discharged: no real symmetric c has the Wilson tree values on a box of side 23, colour-isotropic, no symmetry, no positivity, no bound; d = 2 excluded from the statement as it must be -> NT2 at tree level, lattice scale (Theorem 3.16)
- discharged: no isotropic subspace of the right codimension at all, for L large, so a uniform eps_0 at quadratic order with no bound on c; one family with one eps for c tensor 1_3 up to link variance c_1 g^(4/3) -> NT2 at tree level, lattice scale (Theorem 3.17, Corollary 3.18). Boundary terms estimated: Text 7, item 26
- gap: (RANK-U), the moment map on the kernel of the site densities is not zero, on one box, for every gauge in a bounded set; universal, no level and no g; evidence only -> Theorem 3.19
- implication: the level-j form of Theorem 3.16 for colour-isotropic covariances with no symmetry and bounded link variance, given (RANK-U) and the far-field inputs of Theorem 3.10 and Lemma 5.4; correction terms estimated, Text 7 item 29 -> NT2 for every Gaussian law (Theorem 3.19)
- gap: colour-mixing gauge parts with no symmetry; rank bound empty, T is a singlet -> NT2 for every Gaussian law
- gap: non-zero mean with a large gauge part; a large mean rotates colour frames, which is the colour-mixing case -> NT2 for every Gaussian law
- gap: link variance above c_1 g^(4/3), at the Wilson lattice scale and at level j; the Levy triple, and aligned gauge modes with no Levy area -> NT2 for every Gaussian law

## Requests

- target lead: adopt the wording of NT2 in Text 6, with the order of quantifiers family, law, member, one family per scale. Reason: with the correlator chosen first, NT2 is false on G by Proposition 1.1, for T by rescaling the covariance and for any single f by a point mass. A Gaussian potential on a finer lattice is then tested at its own scale, which answers the question of the fine potential class. In d = 2 the fine class contains Yang-Mills (Proposition 1.2).
- hard-core--independent: Lemma 5.1' derives (c+) from (EI) in the regular chart, with rate C g^2 p^(n+6). Please confirm or correct the split used there: the third-order Taylor term of -g^-2 F_k(V(b)) as a polymer of size g p^3, the remainder after it of size g^2 p^4, and C_E g p replaced by C(L) |F^*| g p + C(L) g^2 p^2 because the linear terms of PP, log JJ, log FP vanish at flat W by colour. Also say how far rough cubes under a regular W affect a local polynomial (the gate's D6), and confirm (b+), (d+) from analyticity on the class, and C_s free of L in the lift at level k. This is only a rate o(g) with the first-order term evaluated, not a new estimate on the induction.
- hard-core--mapped: confirm (H2) in the g-refined form |D_xi^alpha S| <= C g^(|alpha| - 2) e^(-mu tau(alpha)) for |alpha| >= 2 in your chart, with the cubic and quartic Taylor split. Lemma 5.1 then gives (c+) at fixed site data. Lemma 5.6 here reads your "Theorem OS, local form" to get (c+) on the event that W is class on a ball of radius C log(1 / g), for the fibre law with any far data, which is the gate's D6 and D7. Please say whether that reading is right, in particular Step 4, the bound on U^ref(omega, d) - V^*_loc near D, and whether your (H1)-(H3) in the ball hold at this radius.
- upper-chain: Corollary 4.2 needs Theorem 10.7 at two offsets with supports ordered on all axes, for instance (d, d, 2d, 2d) and (d, d, 2d, 3d), with D5 to D8 repaired. Theorem 5.3 replaces the Chebyshev bound on G^c by high moments. No other change.
- target lead, gate request: Lemma 3.2, Lemma 3.4, Theorem 3.5 and Theorem 5.3 are ready for a hostile check. Attack first: the claim that Lemma 5.2 identifies the sum of the terms in the recursion of Theorem 5.3, and the reach of (B).

## Text

### 0. Notation

Level-0 lattice, unit spacing. Weight exp(-beta sum_p s_p), s_p = 1 - (1/2) Tr U_p, as in `parts/upper-chain.md`, Text 0. So g^2 = 1 / beta in the notation of its Theorem 10.7, and the usual coupling is 4 / beta. U_b = exp(i A_b . sigma / 2) with A_b in R^3. For a closed lattice path Gamma from a base point o, in path order b_1, ..., b_n with signs eps_s = +-1 (eps_s = -1 when b_s is traversed backwards), W_Gamma is the ordered product and psi_Gamma in R^3 its logarithm, W = exp(i psi . sigma / 2), for W near 1. The current of Gamma is J_Gamma = sum_s eps_s delta_(b_s), a conserved link function, and Phi_Gamma = <J_Gamma, A> = sum_s eps_s A_(b_s), the linear flux. With d the lattice curl from links to plaquettes, d_0 the gradient from sites to links, and d^T, d_0^T their transposes.

BCH gives psi_Gamma = Phi_Gamma + Q_Gamma + O(|A|^3), with Q_Gamma = -(1/2) sum_(s<t) eps_s eps_t A_(b_s) x A_(b_t). (Check: exp(i X . sigma / 2) exp(i Y . sigma / 2) = exp(i (X + Y - (1/2) X x Y + ...) . sigma / 2), from [sigma_a / 2, sigma_b / 2] = i eps_abc sigma_c / 2.)

**The test.** For three closed paths at one base point,

    T(Gamma_1, Gamma_2, Gamma_3) := (1/2) Tr(W_1 W_2 W_3) - (1/2) Tr(W_1 W_3 W_2) = 2 v_1 . (v_2 x v_3),

where W_i = a_i + i v_i . sigma. Derivation: (i)^3 (1/2) Tr(sigma_a sigma_b sigma_c) = -i . i eps_abc = eps_abc, and the second ordering has the opposite sign. So |T| <= 2, T is gauge invariant, and T = (1/4) psi_1 . (psi_2 x psi_3) + O(|psi|^5). T is one bounded gauge-invariant function of the links in the union of the three paths. When the paths lie in a small region it is a local observable, and it is an element of the blocked net when the links are blocked links. "Joined" is therefore not a defect in itself: a one-point function of a local bounded observable is a correlator in the sense of the net. It is a defect only for a claim about separated supports, which is treated in 2.6 and 3.6.

### 1. What NT2 can and cannot say

Three comparison classes. Fix a finite family of closed paths at a base point, or a finite window of links.

- **Flux class F.** (W_i) = (exp(i b_i . sigma / 2)), with (b_i) jointly Gaussian and centred, any covariance. Three free Maxwell copies with b_i the surface flux of F^a belong here, and this is what Theorem 10.7's main term computes.
- **Potential class G.** U_b = exp(i A_b . sigma / 2), with (A_b) jointly Gaussian and centred, any covariance C on R^3 tensor links; the W_i are the ordered products. No gauge is singled out: the law of gauge-invariant functions depends on C itself and not only on d C d^T, because a gradient in A is not a gauge transformation of U.
- **Fine potential class.** The same at a finer lattice, followed by the blocking. It is not contained in G at the coarse lattice, since M is nonlinear. It is not treated here (Obligations).

**Proposition 1.1 (the order of quantifiers).** [Derived.] (a) On F, the function T vanishes in expectation for every law: T(-b) = -T(b) exactly, since v_i is odd in b_i and a_i is even. (b) On G with non-centred laws allowed, any single real continuous gauge-invariant f and any law omega have mu in G with mu(f) = omega(f). (c) On centred G, for T with the corner cluster of 2.4 and beta large, the Wilson value of <T> is attained by a centred Gaussian potential, by rescaling C. So "some correlator differs from its value in every law of G", read with the correlator chosen first, is false for T and for every f under (b). The statement that can be true is the other order: for every law in G, some correlator of a fixed family differs. **Proposed edit to NT2: Text 6.**

Proof. (a) is the display. (b) Take point masses, C = 0 and mean A at the points where f attains its extreme values, and join them by a path of means, which is possible since exp maps R^3 onto SU(2). f is continuous along the path, and omega(f) lies between the extreme values. (c) mu_t := the centred Gaussian potential with covariance (4 / t) G, Feynman gauge as in 2.1. By 3.1, mu_t(T) = K_comp / t^2 + O(t^-3), K_comp = 0.3969 > 0. mu_t(T) is continuous in t and tends to 0 as t -> infinity, and the Wilson value K_total / beta^2 (1 + O(1 / beta)) with K_total = 0.6157 lies in the range, near t = 0.803 beta. The Wilson value is taken from 2.4, at the level of the Laplace expansion. []

**Proposition 1.2 (d = 2 is inside G: any test must see the dimension).** [Derived at the level of the steps below; not load-bearing.] Take d = 2, a fine lattice of spacing a, A_2 = 0, and A_1(x, y) centred Gaussian with independent colours, independent in x, a Brownian motion in y, of variance g_c^2 a y per colour on the link (x, y). Then for a rectangle [x_0, x_1] x [y_0, y_1], the holonomy converges in law as a -> 0 to Brownian motion on SU(2) at time g_c^2 x area, independent of y_0, and disjoint rectangles give independent holonomies. So the law of gauge-invariant functions of this Gaussian potential tends to the Yang-Mills law on the plane in axial gauge (Driver's description of YM_2, recalled for the name; the steps below are mine).

Steps. Let U(x) be the ordered product along the bottom edge up to x. With X_x := A_1(x, y_0) and Delta_x := A_1(x, y_1) - A_1(x, y_0), which are independent, the holonomy is an ordered product over x of exp(-i Ad(U(x)) Delta_x) up to the replacement of exp(i (X + Delta)) by exp(i X) exp(i Delta). That replacement costs a commutator of size |X| |Delta|, a^(1/2) a in standard deviation per step, with mean zero given the past, so the sum over 1 / a steps tends to 0 in L^2. Since the law of Delta_x is invariant under rotations and independent of U(x), the rotated increments are independent Gaussians of variance g_c^2 a (y_1 - y_0) per colour. Their ordered product is a random walk on SU(2) with total time g_c^2 (x_1 - x_0)(y_1 - y_0). Independence of disjoint rectangles comes from the independent increments in x and y.

So in d = 2 no test can separate the Yang-Mills limit from all of G, and in d = 2 the test must vanish on Yang-Mills or be matched by a choice of C. Proposition 2.3 shows how this happens at tree level: the vertex cancels the Gaussian value exactly. It is the check that the formula below knows the dimension.

### 2. The tree coefficient on the Wilson lattice

**2.1 The formula.** Let G = (-Delta)^-1 on zero-mean functions, acting on each link direction (Feynman gauge), E_i := G J_i, P_i(p) := (d E_i)_p, and P_ij := <J_i, E_j>. For a plaquette p with links b_1, ..., b_4 in path order and signs eps_s,

    V_p(E_1, E_2, E_3) := sum_(s<t) eps_s eps_t det [ (P_k(p), E_k(b_s), E_k(b_t)) ]_(k = 1, 2, 3),
    A_Gamma(E, F) := sum_(s<t on Gamma) eps_s eps_t [ E(b_s) F(b_t) - E(b_t) F(b_s) ].

A_Gamma is the Levy area, twice the signed area of the path in the plane with increments (eps_s E(b_s), eps_s F(b_s)).

**Proposition 2.1 (tree coefficient).** [Derived; rigorous as a Laplace expansion on a contractible box, formal on a torus or on Z^4.]

    <T> = K_total / beta^2 + O(beta^-3),   K_total = K_comp + K_vert,
    K_comp = -12 [ A_1(E_2, E_3) + A_2(E_3, E_1) + A_3(E_1, E_2) ],
    K_vert = 12 sum_p V_p(E_1, E_2, E_3).

K_comp alone is the leading value in the Gaussian potential with covariance (4 / beta) G.

Proof. On a contractible box, flat fields are one gauge orbit, and the maximal tree gauge has no Jacobian (hard-core--independent, discharged). The action has a nondegenerate minimum at 0 on the non-tree links, Haar density is 1 + O(|A|^2), and T is smooth, so Laplace's method gives

    <T> = <T^(3) + T^(4)>_0 - <T^(3) S_3>_0 + O(beta^-3),

with <.>_0 the Gaussian of S_2 = (beta / 8) sum_p |Phi_p|^2 and S_3 = (beta / 4) sum_p Phi_p . Q_p. The last follows from s_p = |psi_p|^2 / 8 + O(|psi_p|^4). Here T^(3) = (1/4) Phi_1 . Phi_2 x Phi_3 and T^(4) = (1/4)(Q_1 . Phi_2 x Phi_3 + Phi_1 . Q_2 x Phi_3 + Phi_1 . Phi_2 x Q_3). Write the Gaussian as covariance (4 / beta) c tensor 1_3 with c in the tree gauge, and E_i := c J_i. Then d^T d E_i = J_i, with E_i = 0 on the tree. (d^T d E_i - J_i vanishes off the tree by the equation for c, it is conserved, and a conserved function on a tree is 0.)

Wick for the vertex term. Contractions inside T^(3) vanish, since eps_abc delta_ab = 0. The cross contractions give, for X, Y, Z linear in A,

    < eps_abf Phi_1^a Phi_2^b Phi_3^f  eps_cde X^c Y^d Z^e >_0 = 6 (4 / beta)^3 det [ e_k(X), e_k(Y), e_k(Z) ],   e_k(X) := <E_k, X>.

Since Phi_p . Q_p = -(1/2) sum_(s<t) eps_s eps_t eps_cde Phi_p^c A_s^d A_t^e, this gives -<T^(3) S_3>_0 = (1/4)(beta / 4)(1/2) 6 (64 / beta^3) sum_p V_p = 12 beta^-2 sum_p V_p.

Wick for the composite term. In <Phi_1^a Phi_2^b Q_3^f> eps_abf the contraction of Phi_1 with Phi_2 vanishes by colour. The other two give 6 E_1(s) E_2(t) - 6 E_1(t) E_2(s) (4 / beta)^2, from eps_abf eps_fab = 6 and eps_abf eps_fba = -6. So it equals -48 beta^-2 A_3(E_1, E_2), and the prefactor 1/4 gives -12 beta^-2. The other two are the cyclic images. By Proposition 2.2 the result is the same in Feynman gauge, and the box may grow. []

**Proposition 2.2 (invariance: the Ward identity at tree level).** [Derived, exact, any d.] Let E_1, E_2, E_3 satisfy d^T d E_i = J_i, the J_i the currents of closed paths with one base point. Then K_total(E_1, E_2, E_3) is unchanged by E_i -> E_i + d_0 theta for each i separately, with any function theta on sites. K_comp alone is not.

Proof, for i = 3; K_total is cyclic. Let v_0, ..., v_n be the vertices of a closed path Gamma, E_s the increments of E. From sum_(t>s) (d_0 theta)_t = theta(v_0) - theta(v_s) and sum_(t<s) (d_0 theta)_t = theta(v_(s-1)) - theta(v_0),

    A_Gamma(E, d_0 theta) = 2 theta(v_0) oint_Gamma E - 2 <J_Gamma, theta_bar E>,  <J_Gamma, theta_bar E> := (1/2) sum_s E_s (theta(v_(s-1)) + theta(v_s)).

Expanding the third row of the determinant, with P_3 unchanged in the first column up to zero (the curl of a gradient vanishes), gives V_p(E_1, E_2, d_0 theta) = P_1(p) A_p(E_2, d_0 theta) - P_2(p) A_p(E_1, d_0 theta). In the sum over p, the terms in theta(v_0(p)) cancel between the two, and what remains is

    sum_p V_p(E_1, E_2, d_0 theta) = -2 <sum_p P_1(p) J_p, theta_bar E_2> + 2 <sum_p P_2(p) J_p, theta_bar E_1> = -2 <J_1, theta_bar E_2> + 2 <J_2, theta_bar E_1>,

using sum_p P_i(p) J_p = d^T d E_i = J_i. In K_comp, A_1(E_2, d_0 theta) + A_2(d_0 theta, E_1) equals the same thing, since theta(o) P_12 cancels. So the change of K_comp and of K_vert cancel. []

So K_total depends on the E_i only through the P_i, and each E_i may be evaluated in its own gauge. Checked: `checks/witness_tree_coeff.py` C1, relative change 1e-15 under a random theta, with K_comp changing by 0.49.

**Proposition 2.3 (d = 2).** [Derived, exact on the plane.] For lassos around disjoint plaquettes in d = 2, K_total = 0. Proof: P_i(p) = delta_(p, p_i) on the plane, so sum_p V_p = A_(l_1)(E_2, E_3) + A_(l_2)(E_3, E_1) + A_(l_3)(E_1, E_2). By Chen's identity, for a lasso Gamma = tau l tau^-1,

    A_Gamma(E, F) = A_l(E, F) + 2 ( E(tau) F(l) - F(tau) E(l) ),                                        (2.1)

and the tail terms vanish, because F(l) = P_ij = 0 for i != j. So the sum over p cancels K_comp exactly. [] On a torus, P has a -1/V tail, and the check gives K_total = -0.0502, -0.0119, -0.0029 at T = 16, 32, 64, scaling as 1 / V (C2), while K_comp = -0.148 stays. The vertex is what removes the Gaussian value in d = 2.

**2.4 Values.** Corner cluster: W_1 = U_12(x), W_2 = U_23(x), W_3 = U_31(x), plaquettes at one site. Evaluated on tori T = 16, 24, 32 by Fourier transform (`checks/witness_tree_coeff.py`):

| T | K_comp | K_vert | K_total |
|---|---|---|---|
| 8 | 0.39689 | 0.21842 | 0.61531 |
| 16 | 0.39686 | 0.21881 | 0.61568 |
| 24 | 0.39686 | 0.21884 | 0.61570 |
| 32 | 0.39686 | 0.21884 | 0.61570 |

**So K_total = 0.6157 and the odd test has a non-zero leading term.** The plan does not change. Relative to the size of T, which is beta^(-3/2), it is of relative order g.

Monte Carlo, Wilson action, heat bath, T = 8, beta = 6 to 32 (`checks/witness_mc_corner.py`, criteria written first): beta^2 <T> = 0.5152(9), 0.5403(9), 0.5672(8), 0.5796(12), 0.5923(11), 0.5985(12) at beta = 6, 8, 12, 16, 24, 32. Fit K + K_2 / beta: K = 0.6182(9), K_2 = -0.619(8), chi^2 / dof = 0.26. The formula at T = 8 is 0.6153. All pre-registered criteria pass: K differs from 0 and from K_comp, and it agrees with K_total within the stated 0.03. The difference from 0.6153 is 3 standard errors of a fit that omits 1 / beta^2. A fit using only beta >= 12 gives 0.617, which removes most of it. I did not refit formally.

Gaussian potential, sampled directly, covariance (4 / beta) G on T = 8 (`checks/witness_gauss_sample.py`): fit K = 0.3968(14), against K_comp = 0.39689. Flux class on the same samples: 0 within error at each beta. **So the statement in `gates/net-tier-upper-chain-c3242879df.md`, D2 repair, that T vanishes for a symmetric Gaussian, holds on F and fails on G, at the same order as the vertex term.** The gate wrote W_i = exp(i b_i) with b_i linear. A loop in a Gaussian potential is not that, since Q_Gamma is even in A.

So what the coefficient shows. K_vert = 0.2188 is the vertex in Feynman gauge. It is not gauge invariant by itself. Only K_total is. The test T separates the Wilson weight from F at once, by K_total != 0. It does not separate from G for one number, by Proposition 1.1(c). Text 3 does that.

**2.5 The sum rule and a separated test.** For a far plaquette q, the same Laplace expansion with beta replaced by beta - t on q, and using delta E_i = (t / beta) P_iq E_q from the change of the Gaussian, gives

    <T s_q>_c = L_q / beta^3 + O(beta^-4),
    L_q = 12 { sum_i P_iq B_i(E_q) - V_q(E_1, E_2, E_3) },
    B_1(E) := sum_p V_p(E, E_2, E_3) - A_2(E_3, E) - A_3(E, E_2),   and cyclically.

Here delta E_i is computed from (4 / beta) c -> (4 / beta) c + (t / 4)(4 / beta)^2 c J_q J_q^T c, from the term t |Phi_q|^2 / 8, and the last term in L_q comes from the coupling beta - t in S_3 on the plaquette q. [Derived at the same level as 2.1.] Exact check: sum_q P_iq E_q = E_i, so sum_q L_q = 12 (3 sum V - 2 sum A - sum V) = 2 K_total, which is -d<T>/dbeta at this order. Brute force on T = 4 (`checks/witness_separated.py`, Q1): 1.2129748815 on both sides, relative 4e-15.

Since B_1 is invariant under E -> E + d_0 theta, by the proof of 2.2, B_i(E_q) is of the order of the field strength of q at the cluster, so L_q has the decay of P^2. On the flux class <T s_q>_c = 0 exactly, odd times even.

**2.6 A separated test exists, on the flux class.** Corner cluster at the origin, far plaquette q in the (1,2) plane at offset (d, d, 2d, 2d), which is ordered along all four axes:

| d | L_q | L_q^G (no V terms) | P_1q | L_q / ((3/2) P_1q^2) |
|---|---|---|---|---|
| 3 | -2.360e-10 | -3.819e-10 | 6.98e-6 | -3.23 |
| 4 | -2.089e-11 | -3.484e-11 | 2.09e-6 | -3.19 |
| 5 | -2.878e-12 | -4.960e-12 | 7.79e-7 | -3.16 |

So beta <T s_q>_c / Cov(s_p, s_q) tends to a number near -3.2, stable within 3% over this range (Q2). The cluster T mixes with the plaquette energies at relative order 1 / beta, and the flux class has mixing exactly 0. **A separated correlator, with supports ordered along all axes, separates the Wilson weight from the flux class, with coefficient g^6.** L_q^G is of the same size and decay at this symmetric cluster, so this ratio alone does not separate from G. Note that at this cluster the far-field term of order d^-7 predicted for G is absent or small: I did not resolve it (slopes -8.3 and -8.7 between d = 3, 4, 5).

### 3. Separating from Gaussian potentials: a Gaussian potential reads a far flux

**The idea.** In a Gaussian potential, T with one far loop reads the gauge-dependent field of that loop near the other two, through the rotation of a tail. In a gauge-invariant weight the vertex removes this, by the Ward identity. Summing the reading around a closed circuit removes the gauge choice in G too, by Stokes, and what is left is a far flux with coefficient -24. On the Wilson weight the same sum has no such term.

**Lemma 3.1 (Gaussian value).** [Derived.] Let C = 4 g^2 c tensor 1_3, with c symmetric positive semidefinite on links, c_bb <= kappa_hat, and paths of total length n. Then, with E_i := c J_i,

    mu_C(T) = g^4 K_comp[c] + O_n(kappa_hat^3 g^6),   K_comp[c] := -12 [ A_1(E_2, E_3) + A_2(E_3, E_1) + A_3(E_1, E_2) ],
    mu_C( 1 - (1/2) Tr(W_i W_j^-1) ) = (3/2) g^2 (c_ii + c_jj - 2 c_ij) + O_n(kappa_hat^2 g^4),   c_ij := <J_i, c J_j>.

Proof. T and (1/2) Tr are entire functions of A, bounded, with Taylor remainder after order 5 (resp. 3) at most C_n |A|^6 (resp. |A|^4) for all A, since the polynomial dominates the bounded function for |A| >= 1. Odd orders have mean zero. T^(3) contributes nothing, and the order 4 is the Wick computation in the proof of 2.1. For the second line, (1/2) Tr(W_i W_j^-1) = 1 - |Phi_i - Phi_j|^2 / 8 + order 3 + order 4. []

**Colour (Lemma 3.1').** [Derived.] For general C, let E_i^(ad)(b) := <Phi_i^a, A_b^d> / (4 g^2), Gamma_ij^(ab) := <Phi_i^a, Phi_j^b> / (4 g^2), and for 3 x 3 matrices a(M, N) := tr M tr N - tr(M N). Since eps_abc eps_cde = delta_ad delta_be - delta_ae delta_bd, Wick gives

    mu_C(T) = -2 g^4 sum_cyc { A^col_k(E_i, E_j) + sum_(s<t on Gamma_k) eps_s eps_t Gamma_ij^(ab) (C_st^(ab) - C_st^(ba)) / (4 g^2) } + O_n(kappa_hat^3 g^6),
    A^col_Gamma(E, F) := sum_(s<t) eps_s eps_t [ a(E(s), F(t)) - a(E(t), F(s)) ].

For E = e 1_3, F = f 1_3 one has a = 6 e f, which returns the isotropic formula. The second term vanishes when Gamma_ij is symmetric in colour. Isotropy of a pair is testable: (Tr Gamma_pq)^2 = 3 ||Gamma_pq||_HS^2 holds for the Wilson tree values, with Tr Gamma read from 1 - (1/2) Tr(W_p W_q^-1) = (g^2 / 2) (Tr Gamma_pp + Tr Gamma_qq - 2 Tr Gamma_pq) + ... and ||Gamma||^2 from Cov(s_p, s_q) = (1/2) g^4 ||Gamma_pq||^2 + ..., at leading order. Precisely, if |Tr Gamma - 3 P| and | ||Gamma||^2 - 3 P^2 | are at most eps, then ||Gamma - P 1_3||^2 <= (1 + 2 |P|) eps, and the antisymmetric part is bounded by the same.

**Rectangle.** Let l(y) be the plaquette in the (1,2) plane with corner (0, 0, y_3, y_4), in path order +1, +2, -1, -2. Let y_k, k in Z_4, be the corners of a D x D square S in the (3,4) plane, sigma_k the straight segment from y_k to y_(k+1), and l_3 a plaquette in the (3,4) plane at a far position x, tau_k a lattice path from y_k to a corner of l_3. With base point y_k put

    T^(k) := T( l(y_k),  sigma_k l(y_(k+1)) sigma_k^-1,  tau_k l_3 tau_k^-1 ),

and for a covariance c write E_k := c J_(l(y_k)), e := c J_(l_3), P_k := <J_(l(y_k)), E_(k+1)>, P_(3,k) := <J_(l(y_k)), e>, Flux := sum_(p in S) (d e)_p = sum_k e(sigma_k), with S the square at (x_1, x_2) = (0, 0).

**Lemma 3.2 (rectangle identity).** [Derived, exact. Checked: `checks/witness_stokes.py` S1, `checks/witness_identity.py` I1, I2.] Let c be invariant under the rotation by 90 degrees of the (x_1, x_2) plane about the point (1/2, 1/2). Then E_k has equal increments P / 4 along the four steps of every l(y'), with P = <J_(l(y')), E_k>, and if all P_k != 0,

    sum_k K_comp^(k)[c] / P_k = -24 Flux - 12 sum_k A_(l_3)(E_k, E_(k+1)) / P_k
                                 - 24 sum_k [ P_(3,k+1) (E_k(tau_k) - E_k(sigma_k)) - P_(3,k) E_(k+1)(tau_k) ] / P_k.     (3.1)

No regularity of e is used, and no bound on E. The far loop's field e may be wild.

Proof. The rotation rho fixes every l(y') as a set, preserves its orientation and sends each step of its path to the next, and rho J_(l(y_k)) = J_(l(y_k)). So <J_(step s+1), c J_(l(y_k))> = <rho J_(step s), c rho J_(l(y_k))> = <J_(step s), c J_(l(y_k))>, and the increments are equal. Their sum is P. For a field with increments d_1, ..., d_4 on l and E with equal increments f,

    A_l(e, E) = f sum_(s<t) (d_s - d_t) = f (3 d_1 + d_2 - d_3 - 3 d_4) =: f Theta(e; l).

Using (2.1) on the two lassos,

    K_comp^(k) = -12 { (P_k / 4) [ Theta(e; l(y_(k+1))) - Theta(e; l(y_k)) ] + 2 e(sigma_k) P_k + A_(l_3)(E_k, E_(k+1))
                       + 2 P_(3,k+1) (E_k(tau_k) - E_k(sigma_k)) - 2 P_(3,k) E_(k+1)(tau_k) }.

Divide by P_k and sum over k in Z_4. The Theta terms telescope, and sum_k e(sigma_k) = Flux. []

**Colour form of (3.1).** [Derived.] If C is invariant under the rotation, acting on positions only, then E_k^(ab) has equal increments Gamma^(ab) / 4 on l(y'), in each colour entry, by the same proof. If moreover Gamma_(k, k+1) = P_k 1_3, then for E_k = (P_k / 4) 1_3 on a plaquette, a((P_k / 4) 1_3, N) = (P_k / 2) tr N. So the Theta terms involve tr e and telescope. In (2.1) the colour form has 2 [ a(E(tau), F(l)) - a(F(tau), E(l)) ], and a(e(sigma_k), P_k 1_3) = 2 P_k tr e(sigma_k) = 6 P_k ebar(sigma_k), with ebar := tr e / 3. So (3.1) holds with e replaced by ebar, Flux by the mean colour flux (1/3) sum_(p in S) tr Gamma_(3 p), which the tests of Lemma 3.1 read, and with A_(l_3) replaced by A^col_(l_3) / 6. An error Gamma_(k, k+1) - P_k 1_3 of size eps enters multiplied by at most C (kappa_hat)^(1/2). So Theorem 3.5 below needs no colour isotropy of C, once the isotropy test of the near pairs is in its family.

In Feynman gauge on the lattice, the directions decouple: E_k lives on directions 1, 2 and e on directions 3, 4. So P_(3,k) = 0 and A_(l_3)(E_k, E_(k+1)) = 0 exactly, and (3.1) reads sum_k K_comp^(k) / P_k = -24 Flux. Since P_(3,k) = 0 for the Wilson weight at this order, a law that matches has P_(3,k) small, and the last line of (3.1) is small, whatever the tail: the size of E_k(tau_k) enters only multiplied by it.

**Lemma 3.3 (lattice Green's function).** [Derived.] With nabla the lattice differences on Z^4, |nabla^n G(x)| <= C_n (1 + |x|)^(-2-n) for n <= 3. Proof. Let f(k) be the symbol, prod_mu (e^(i k_mu) - 1)^(n_mu) / khat^2. Then f is smooth on the torus off k = 0, with |d^a f(k)| <= C |k|^(n - 2 - |a|). Split at |k| = 1 / |x| with a smooth cut. The low part is at most C |x|^(-(n-2)-4). In the high part integrate by parts m > n + 2 times in the coordinate mu with |x_mu| >= |x| / 2, with no boundary terms by periodicity. This gives |x|^-m times the integral over |k| > 1 / |x| of |k|^(n-2-m), which is C |x|^(m-n-2), plus the terms where derivatives hit the cut, which are of the same size. Total C |x|^(-n-2). The same proof, applied to the difference of the symbol from its continuum form, which obeys |d^a f(k)| <= C |k|^(n - |a|), gives nabla^n G(x) = d^n (1 / (4 pi^2 x^2)) + O(|x|^(-n-4)), for n = 1, 2, 3, x != 0. []

**Lemma 3.4 (the Wilson side reads nothing).** [Derived on Z^4, at the level of each step below.] Let c = G. For the rectangle above with far plaquette at x,

    Stk_W := sum_k K_total^(k) / P_k = O_D( |x|^-5 ),  while -24 Flux = -24 D^2 (1 - 2 (x_3^2 + x_4^2) / x^2) / (pi^2 x^4) (1 + O_D(1 / |x|)).

Proof. Let Lambda[e] := sum_k { 12 sum_p V_p(E_k, E_(k+1), e) - 12 [ A_(l(y_k))(E_(k+1), e) + A_(l(y_(k+1)))(e, E_k) + 2 e(sigma_k) P_k ] } / P_k. Since P_(3,k) = 0 and A_(l_3)(E_k, E_(k+1)) = 0, Stk_W = Lambda[G J_(l_3)]. By 2.2, Lambda vanishes on gradients. By 3.2, Theta telescopes, so Lambda[e] = 12 sum_k sum_p V_p(E_k, E_(k+1), e) / P_k - 24 sum_k e(sigma_k). The proof of 2.2, with equal increments, gives

    sum_p V_p(E_k, E_(k+1), d_0 theta) = 2 P_k ( theta_bar(y_(k+1)) - theta_bar(y_k) ),                                   (3.2)

theta_bar(y) the average of theta over the four corners of l(y).

*Step 1, Lambda vanishes on uniform fields.* For an antisymmetric matrix F and a centre c_0 let e_(F, c_0)(y, nu) := (1/2) sum_mu F_(mu nu) (y - c_0)_mu, whose curl is F exactly on each plaquette. The sum over p converges absolutely: its terms are of size |z|^-6. Let c_k := (1/2, 1/2, midpoint of edge k). The reflections x_1 -> 1 - x_1 and x_2 -> 1 - x_2 reverse both l(y_k) and l(y_(k+1)), so they leave E_k, E_(k+1) unchanged up to two signs, and they send F_(1 nu) -> -F_(1 nu), F_(2 nu) -> -F_(2 nu). The reflection in the 3-plane through edge k, when the edge is along the other axis of (3,4), fixes both plaquettes and sends F_34 -> -F_34. So sum_p V_p(E_k, E_(k+1), e_(F, c_k)) = 0 for every F. With c_0 the centre of the square, e_(F, c_0) = e_(F, c_k) + d_0 theta_k, theta_k linear, and by (3.2), summing over k, 12 sum_k sum_p V_p / P_k = 24 sum_k (theta_k_bar(y_(k+1)) - theta_k_bar(y_k)) = 24 D^2 F_34, by a direct count over the four edges, each giving (D^2 / 4) F_34. Also sum_k e_(F, c_0)(sigma_k) = D^2 F_34. So Lambda[e_(F, c_0)] = 0.

*Step 2, the remainder.* Let e = G J_(l_3), F := (d e) at c_0, rho := |x| / 2. On the ball B(c_0, rho), by 3.3, |d e - F| <= C |y - c_0| |x|^-5, so a gauge by line integrals along coordinate paths gives e = d_0 theta + e_(F, c_0) + e_2, with |e_2(y)| <= C |y - c_0|^2 |x|^-5. Cut theta off smoothly between rho / 2 and rho. By Lemma 3.3, |theta| <= C rho |x|^-3 there, so the gradient of the cutoff term is at most C |x|^-3. So e - d_0(chi theta) - e_(F, c_0) is e_2 on the inner ball, and outside the inner ball it is at most C (|x|^-3 + |e(y)| + |y - c_0| |x|^-4). Now Lambda is a sum over p of terms |P_k| |E_(k+1)| |.| + |E_k| |E_(k+1)| |d .|, with |E_k(z)| <= C_D |z|^-3 and |P_k(z)| <= C_D |z|^-4 by 3.3 (a plaquette current has zero charge and is a dipole). On the inner ball the sum is at most C_D |x|^-5 sum_z (|z|^-7 |z|^2 + |z|^-6 |z|) = C_D |x|^-5. Outside, at most C_D sum_(|z| > rho/2) ( |z|^-7 (|x|^-3 + |e(z)| + |z| |x|^-4) + |z|^-6 (|x|^-4 + |P_3(z)|) ) <= C_D |x|^-6 log |x|, the logarithm from the plaquette l_3 itself. The line term is at most C D^3 |x|^-5. []

Numbers, torus T = 40, far loop on the axis, x = (R, 0, c, c) centred on the square (`checks/witness_stokes.py`):

| D | R | Stk_comp = -24 Flux | Stk_total | ratio |
|---|---|---|---|---|
| 3 | 6 | -1.619e-2 | +7.85e-3 | 0.48 |
| 3 | 8 | -5.242e-3 | +1.88e-3 | 0.36 |
| 3 | 12 | -1.037e-3 | +2.27e-4 | 0.22 |
| 3 | 16 | -3.51e-4 | +4.63e-5 | 0.13 |
| 5 | 8 | -1.219e-2 | +4.73e-3 | 0.39 |
| 5 | 16 | -9.32e-4 | +1.52e-4 | 0.16 |

Identity S1 holds to 1e-12. S3: K_total does not depend on the tail, to machine precision, as it must since P_(3,k) = 0. Stk_total has slope -5.2, -5.5 between R = 8, 12, 16, against about -4 for the flux (torus effects at the end). The opposite sign is not a claim. Per edge at D = 3, R = 8: K_comp = -2.96e-6, K_vert = +4.03e-6, K_total = +1.06e-6, P_k = 2.26e-3. **So K_vert is what removes the flux reading: this test measures the three-gluon vertex, in gauge-invariant form.**

**Monte Carlo of the rectangle sum at the smallest size,** D = 1, R = 2, T = 8, averaged over translations and the 24 axis permutations, 800 configurations (`checks/witness_mc_rect.py`, criteria written first). beta^2 sum_k <T^(k)> / P_k on the Wilson weight and on the Gaussian potential in Feynman gauge, sampled directly, against the tree values +0.347 and -0.266 (which equals -24 Flux here):

| beta | Wilson | Gaussian potential |
|---|---|---|
| 16 | +0.308(36) | -0.213(23) |
| 32 | +0.355(56) | -0.277(45) |
| 64 | +0.246(61) | -0.267(64) |

The pre-registered criteria pass at beta = 64: Wilson within 0.3 of the formula's value relative to it, 8 standard errors from the Gaussian value, and Gaussian within 1 standard error of its formula. **So the sign difference and the size are seen at finite beta: the vertex is what separates them, and the formula holds for lassos with tails.**

`checks/witness_identity.py`: covariances c = G + gradient terms, invariant under lattice translations and reflections, with a free function that includes rapidly oscillating factors. (3.1) holds to 1e-13 in every case, also where the example is not positive, and the increments are uniform to 1e-14. In the positive examples tried (a = 0.5, b = 0, smallest eigenvalue 0.81; a = 0.5, b = 0.7, smallest eigenvalue 0.72) the far term moves the sum by under 3% at R = 6 and under 0.2% at R = 8. Note that any gauge term of the form d_0 X d_0^T leaves E_i unchanged, because J is conserved: all covariant gauges have the same K_comp.

**Theorem 3.5 (no symmetric Gaussian potential has the Wilson tree values).** [Derived given Lemmas 3.1 to 3.4, for the Wilson tree values on Z^4.] Fix kappa_hat_0, A < infinity. There are D, n, R_0, a finite family 𝔉 of bounded gauge-invariant functions, namely 1 - (1/2) Tr(W_i W_j^-1) on pairs of lassos and T^(k) with far plaquettes in dyadic shells R_0 2^j <= |x| < R_0 2^(j+1), j = 1, ..., n, and eps, g_0 > 0, such that the following holds for g < g_0. Let mu be a Gaussian potential with C = 4 g^2 c tensor 1_3, c_bb <= kappa_hat_0, c invariant under the rotation of 3.2, and

    (B)  sum_b |(c J_(l(y)))(b)|^2 <= A^2   for the plaquettes l(y) of the square.

The same holds for general C (not colour-isotropic), by the colour form of (3.1), with Cov(s_p, s_q) on the near pairs added to 𝔉, and with (B) on the matrix-valued fields. Then some f in 𝔉 has |mu(f) - W_g(f)| >= eps g^(deg f), with deg f = 2 and 4 respectively, where W_g is the Wilson tree value at beta = 1 / g^2: W_g(1 - (1/2) Tr(W_i W_j^-1)) = (3/2) g^2 (P_ii + P_jj - 2 P_ij) and W_g(T) = g^4 K_total.

Proof. Suppose not. By Lemma 3.1 and the first class of tests, all c_ij in the family are within C eps of their Wilson values, for g small. So |P_k[c] - P_k| and |P_(3,k)[c]| are at most C eps, and |Flux[c] - Flux| <= C eps D^2. By the second class, |K_comp^(k)[c] - K_total^(k)| <= 2 eps. Insert (3.1), sum over the far plaquettes m in a shell M_j, with |M_j| <= C (R_0 2^j)^4, and use Lemma 3.4:

    24 sum_(m in M_j) |Flux^(m)| <= C_D sum_m |x_m|^-5 + C(D, R_0, n, kappa_hat_0) eps + 12 sum_k sum_(m in M_j) |A_(l_3^(m))(E_k, E_(k+1))| / |P_k|.

Here the second term collects eps / |P_k| over the family and the last line of (3.1), where |E_k(tau_k)| <= |tau_k| (kappa_hat_0 c_ll)^(1/2) by Cauchy-Schwarz is finite and multiplied by |P_(3,k)[c]| <= C eps.

The left side is at least 24 D^2 (log 2 - o(1)), since (x_3^2 + x_4^2) / x^2 is uniform on [0, 1] on the sphere S^3, so the mean of |1 - 2 t| is 1/2, and the shell has measure 2 pi^2 log 2 against 1 / (pi^2 x^4). The first term on the right is at most C_D / (R_0 2^j). In the third, |A_(l_3)(E, E')| <= 12 max |E| max |E'| on its links, and each link lies in at most 2 plaquettes of the (3,4) plane, so by Cauchy-Schwarz the sum over m is at most C ||E_k||_(l^2(S_j')) ||E_(k+1)||_(l^2(S_j')), with S_j' the links near the shell. By (B), sum_j sum_k ||E_k||^2_(l^2(S_j')) <= C A^2, so there is a j with all four norms squared at most C A^2 / n. Choose D first, odd, with P_k != 0: the values 2.262e-3 at D = 3 and 2.130e-4 at D = 5 are computed, and P_k = (1 + O(D^-2)) / (pi^2 D^4) by Lemma 3.3. Then take n and R_0 large so that the terms are below 6 D^2, and then eps small. For that j this is a contradiction. []

This is what the test demands of a Gaussian potential: rotation invariance of the covariance about a plaquette axis, and (B). Both are mild. (B) holds for G: sum_b |G J_l(b)|^2 is the integral of |J_l^(k)|^2 / khat^4, finite since |J_l^(k)|^2 <= C |k|^2. A Gaussian potential whose covariance has no symmetry is not covered (Obligations). Note on d. In d = 2 the proof breaks at Flux: P_(ij) = 0 at separated plaquettes, so Flux = 0 and the Wilson and Gaussian values agree (2.3). In d = 3 the rectangle needs a transverse plane of dimension 2, and (1,2) plus (3,4) needs d >= 4; the analogue in d = 3 would need another geometry. I did not look for one. In d >= 5 the same geometry applies with different exponents. That is fine: the proof uses that the weight is gauge invariant and has the vertex forced by its quadratic form. The statement is about one finite family at fixed small g, and dimensions enter through the Green's function. It says nothing about which theory is UV stable, which is the hard core's job.

**Proposition 3.11 (a separated test against G).** [Derived at tree level. The form at level j is the recursion of Theorem 5.3 at higher degree, not written: Obligations.] Let Lam be a plaquette in the (3,4) plane inside the square, q a far plaquette in the (3,4) plane at x, and T_k the function T of l(y_k), sigma_k l(y_(k+1)) sigma_k^-1, tau_k Lam tau_k^-1. The cluster T_k and s_q are local observables at distance about |x|. By 2.5 and the same computation on a Gaussian potential,

    <T_k s_q>_c = L_q(k) g^6 + ...   on the Wilson weight,   L_q^G[c](k) g^6 + ...   on the Gaussian potential,
    L_q^G[c](k) = 12 sum_i c_iq ( the terms A of B_i(c J_q) ) - 12 V_q(c J_1, c J_2, c J_3).

If c is invariant under the rotation of 3.2 and c_(l(y), q) = 0 as for the Wilson weight, the proof of (3.1) with e replaced by c J_q gives

    sum_k L_q^G[c](k) / P_k = -24 c_(Lam, q) Flux[c J_q] - 12 sum_k V_q / P_k,   sum_k L_q(k) / P_k = c_(Lam, q) Lambda[G J_q] - 12 sum_k V_q / P_k.

Here Lambda is the functional of Lemma 3.4, so the second is of order |x|^-4 |x|^-5, and the first of order |x|^-4 |x|^-4. The term V_q vanishes exactly for c = G, since the directions decouple, and in general it is controlled on average over q by (B), as in Theorem 3.5.

Numbers, D = 3, torus T = 32, Lam the plaquette at the centre of the square, q at (R, 0, 1, 1) (`checks/witness_separated_rect.py`). The first identity holds to 3e-16:

| R | sum_k L_q^G / P_k = -24 P(Lam, q) Flux | sum_k L_q / P_k | ratio |
|---|---|---|---|
| 6 | -1.502e-6 | +7.30e-7 | 0.486 |
| 8 | -1.395e-7 | +5.03e-8 | 0.360 |
| 10 | -2.267e-8 | +6.18e-9 | 0.273 |
| 12 | -5.512e-9 | +1.12e-9 | 0.203 |

**So a separated test against G exists, with coefficient g^6.** Its demand on the hard core is the same: first-order term evaluated, with rate o(g).

**The whole difference is the vertex on a slice.** For any c with d^T d c J = J on conserved J, Proposition 2.1 and 2.2 give

    K_total(Gamma_1, Gamma_2, Gamma_3) - K_comp[c](Gamma_1, Gamma_2, Gamma_3) = 12 sum_p V_p(c J_1, c J_2, c J_3),                    (3.3)

when the sum converges absolutely. The right side is trilinear in the currents. So a Gaussian potential has the Wilson tree values on all triples of loops exactly when the cubic form of the Wilson action vanishes on the linear slice S := c(conserved currents), which is transversal to gradients. Theorem 3.5 is one consequence, with an explicit finite family. The next statement drops the rotation symmetry for translation-invariant c, and it is where d = 4 enters sharply.

**Lemma 3.6 (the cubic form on plane waves).** [Derived: exact symbolic identity plane by plane, `checks/witness_vertex_sympy.py`, S1 passes. Also checked numerically on d = 4, `checks/witness_vertex_form.py`, X1.] For E_i = a^i exp(i k^i . x), k^1 + k^2 + k^3 = 0, a^i_mu = atil^i_mu exp(i k^i_mu / 2), the sum of V_p over the plaquettes at one site is

    -2i [ (atil^1, D_3 atil^2) (Y_12 . atil^3) + (atil^2, D_1 atil^3) (Y_23 . atil^1) + (atil^3, D_2 atil^1) (Y_31 . atil^2) ],

with (a, b) the bilinear pairing, D_l := diag(cos(k^l_mu / 2)), Y_ij := (2 sin((k^i_nu - k^j_nu) / 2))_nu. Proof: the form is a sum over planes, once the same-index terms are shown to vanish. In one plane, both claims are identities of rational functions in the half-angle phases and the six polarisations, verified by sympy. The shape was recalled from the standard lattice three-gluon vertex, and nothing depends on that recollection.

**Lemma 3.7 (the symbol of a translation-invariant covariance).** [Derived.] Let C be positive semidefinite on R^3 tensor links of Z^4, invariant under lattice translations, with C_bb <= 4 g^2 kappa_hat, and with Gamma_pq = P_pq 1_3 on plaquette pairs, in units of 4 g^2. Use tilde coordinates, atil_mu(k) := a_mu(k) exp(-i k_mu / 2), so that a gradient of theta is i khat theta, with khat := 2 sin(k / 2). A conserved finitely supported J has jtil(k)_mu := exp(i k_mu / 2) sum_x J_mu(x) exp(i k . x), and jtil(k) lies in S_k := khat(k)^perp. Then for a.e. k and v in S_k, the field of the source v tensor e_a has symbol

    delta^(af) v / khat^2 + khat h^(af)(k; v),    with h(k; .) linear, measurable and finite a.e.,

with E_J(x) = the integral over T^4 of these against exp(i k . x), an L^1 density. No (B) is needed.

Proof. By Bochner, C is the Fourier transform of a finite positive matrix measure mu on T^4. Split C^4 tensor C^3 by the unit vector n := khat / |khat| and S_k. The curl is injective on S_k, and the matching gives the S S block of mu equal to 1_(S_k) tensor 1_3 / khat^2 dk. The n n block rho is a finite positive measure, possibly singular. By Cauchy-Schwarz for positive matrix measures, |mu_(n S)(B)|^2 <= rho(B) mu_(S S)(B), so mu_(n S) is absolutely continuous with respect to Lebesgue measure, with density m(k), and |m(k)|^2 <= rho_ac(k) / khat^2. Put h := m / |khat|. A point mass at k = 0, and the singular part of rho, do not act on conserved sources. []

**Formula (*).** [Algebra derived. Checked over 200 random complex samples in `checks/witness_colour_slice.py`: Z1 worst relative difference 3e-14, Z2 and Z3 at 1e-14.] Let (i, j, l) run over the cyclic orders of (1, 2, 3), u_i := v_i / khat_i^2, t_i := tr h_i, a(M, N) := tr M tr N - tr(M N), D_l := diag cos(k^l_mu / 2), and

    lam_1 := (v_1, D_3 khat_2),  lam_2 := (v_2, D_1 khat_3),  lam_3 := (v_3, D_2 khat_1).

From the lattice identity Y_23 = D_3 khat_2 - D_2 khat_3 and (v_1, khat_1) = 0 one gets Y_23 . v_1 = 2 lam_1, and cyclically, so form(u_1, u_2, u_3) = (2 / Pi) [ (v_1, D_3 v_2) lam_3 + (v_2, D_1 v_3) lam_1 + (v_3, D_2 v_1) lam_2 ], Pi := khat_1^2 khat_2^2 khat_3^2. Ward gives form(a^1, a^2, khat_3) = (j_2, D_3 a^1) - (j_1, D_3 a^2), with j the source of a, and form(khat_1, khat_2, khat_3) = 0. Contracting colours by eps_abc eps_fgh gives

    Z(v_1, v_2, v_3) := eps eps form = 6 form(u_1, u_2, u_3) + 2 sum_cyc t_l (v_i, D_l v_j) (1 / khat_i^2 - 1 / khat_j^2) - sum_cyc a(h_j, h_l) lam_i.   (3.4)

By the colour form of Proposition 2.2, for matched C, K_total - K_comp[C] depends only on the currents, is trilinear in them, and equals -4 i / (2 pi)^8 times the integral over (k^1, k^2) in T^4 x T^4 of Z(v_1(k^1), v_2(k^2), v_3(k^3)), with v_i(k) := jtil_i(-k), k^3 := -k^1 - k^2. The integral converges absolutely. In the term 6 form, one has |v| <= C |k| and three factors of 1 / khat^2, with form of order |k|. In the others, |t|, |h| <= rho_ac^(1/2) / |khat| is in L^1 by Lemma 3.7, and the remaining factors are bounded by 1 / |k^i| + 1 / |k^j|.

**Theorem 3.8 (no translation-invariant Gaussian potential has the Wilson tree values).** [Derived given Lemma 3.6, Lemma 3.7, (3.4).] In d = 4, let C be as in Lemma 3.7, with any colour structure and no symmetry beyond translations. Then K_comp[C] != K_total on some triple of closed paths.

Proof. Suppose equality on all triples. Lattice translates multiply jtil by exp(i k . y), and plaquette currents span S_k for a.e. k. So Z = 0 for a.e. (k^1, k^2) and all v_i in S_(k^i).

Fix rho_0 small and let B be the ball of radius rho_0 about k = 0, and A_M := {k in B : |t(k; .)| + |h(k; .)| <= M}. Since h is finite a.e., choose M with |B \ A_M| <= eps_0 |B|, with eps_0 chosen below. Fix k^3 of small size eta, generic so that Fubini applies, and let Q := ker t(k^3; .) in S_(k^3), of dimension at least 2. Let k^1 =: k vary in G := A_M cap (-A_M - k^3), which is nearly all of B. Put S_1^0 := S_(k^1) cap ker lam_1 and S_2^0 := S_(k^2) cap ker lam_2, each of dimension at least 2. Since khat_2 = -khat_1 - D_1 k^3 + O(eta^2) and D_3 = 1 + O(eta^2), both planes are within O(eta / |k|) of P_k := {khat_1, D_1 k^3}^perp, when the angle between khat_1 and D_1 k^3 is bounded below. So v in P_k has projections v_1 in S_1^0, v_2 in S_2^0, and v_1, v_2 = v + O(eta / |k|). The linear functional t_1(v_1) - t_2(v_2) on the 2-dimensional P_k has a kernel. **This is the step that needs d >= 4.** Take a unit v in the kernel, and call tau the common value, |tau| <= C M. Take v_3 in Q. In (3.4), lam_1 = lam_2 = 0 and t_3 = 0. Multiplying by khat_3^2, the equation Z = 0 reads

    12 (v_1, D_3 v_2) (v_3, D_2 khat_1) / (khat_1^2 khat_2^2) + 2 tau (v_3, D_2 v_1 - D_1 v_2) + O(khat_3^2 (M^2 + M / |k|^2)) = 0.

Since D_2 - D_1 and v_1 - v_2 are O(eta) for fixed |k| >= rho_0 / 2, this gives |(v_3, sin k)| <= C(M, rho_0) eta for all unit v_3 in Q, using D_1 khat_1 = sin k. So sin k lies within C(M, rho_0) eta of the complex subspace Q^perp, of dimension at most 2. The set of real x in B, |x| >= rho_0 / 2, within c_0 |x| of a complex 2-plane has a fraction of B at most 1/10, uniformly in the plane, for c_0 small, by compactness of the Grassmannian. The set of k with a small angle to k^3 is also of small fraction. Choosing eps_0 small and then eta small against c_0 / C(M, rho_0), there is k in G violating this. []

**So the Wilson vertex cannot be removed by any linear gauge, in d = 4, for a real or complex covariance, with no regularity.** Where d enters. At d = 3 the plane P_k is a line, the functional t_1 - t_2 need not vanish on it, and the argument stops. At d = 2, the axial slice makes the form vanish, by sum_cyc cos(c) sin(a - b) = 0 for half angles with a + b + c = 0, as Proposition 2.3 says. One triple of momenta is not enough: for hyperplanes with normals n_3 = Y_12, n_1 = Y_23, n_2 = Y_31, the form vanishes on that triple (`checks/witness_vertex_form.py` X3). What excludes this is that the slice at k^3 cannot depend on k^1. That is also why one T can be matched and a family cannot.

**Corollary 3.9 (a finite family for all translation-invariant Gaussian potentials with link variance O(g^2)).** [Derived.] Fix kappa_hat_0. There are a finite family of functions, consisting of 1 - (1/2) Tr(W_i W_j^-1) and the connected Cov(s_p, s_q) on pairs and T on triples of closed paths, and eps, g_0 > 0, such that for g < g_0 and each centred Gaussian potential with C invariant under lattice translations and C_bb <= 4 g^2 kappa_hat_0, some f in the family has |mu_C(f) - W_g(f)| >= eps g^(deg f). The family is not explicit here; Theorem 3.5 is, under its symmetry.

Proof. The set of such C / (4 g^2) is compact for pointwise convergence, positivity and invariance being closed conditions. For fixed loops the leading coefficients of Lemma 3.1' are polynomials in finitely many entries, so they are continuous, and the remainders are uniform for fixed loops. If no finite family and eps existed, a limit C_inf would have all leading coefficients equal to the Wilson values on all pairs and triples. The pairs give Tr Gamma_pq = 3 P_pq and ||Gamma_pq||^2 = 3 P_pq^2, so Gamma_pq = P_pq 1_3 by equality in Cauchy-Schwarz. So C_inf is as in Lemma 3.7, and Theorem 3.8 is contradicted. []

**Theorem 3.10 (the same at level j, by the soft limit; implication).** [Derived at the level of the steps below, given: F_j gauge invariant, F_j = (1/2) <A, H_j A> + F_j^(3) + ..., with symbols of H_j and F_j^(3) C^1 near small momenta away from k = 0, and G_j(k) = (1 + O(|k|^2)) / khat^2 on conserved vectors, uniformly in j; I(k)(a) of hard-core--independent with Lemma 10.1 there, unchecked by me.] Replace the Wilson vertex by F_j^(3), and u_i by G_j(k^i) v_i. Theorem 3.8 and Corollary 3.9 hold for the level-j tree values, with family and eps uniform in j large.

Why (3.4) changes only in the term form(u_1, u_2, u_3). The gauge action on the level-j link variables is the same as at level 0, A -> A + d_0 theta - theta_bar x A + O(A^2 theta), so D_l enters in the same way. Ward for F_j gives, with H := H_j in tilde coordinates, H(-k) = H(k)^T, H(k) khat(k) = 0,

    form^(j)(a^1, a^2, khat_3) = (H(k^2) a^2, D_3 a^1) - (H(k^1) a^1, D_3 a^2).                               (3.5)

So the terms with t and h are the same with H u_i = v_i, and lam_i are the same.

*The soft identity.* The form is linear in a^3, and I write form^(j)(a^1, a^2, a^3) = sum_nu a^3_nu X_nu(k^1, k^2; a^1, a^2). Put k^1 = k, k^2 = -k - k^3, and let k^3 -> 0 at fixed a^1, a^2. In (3.5), D_3 = 1 + O(|k^3|^2), and (H(k^2) a^2, a^1) = (a^2, H(k^2)^T a^1) = (a^2, H(-k^2) a^1) = (a^2, H(k + k^3) a^1). So the right side is B(k + k^3) - B(k) + O(|k^3|^2), with B(k') := (a^2, H(k') a^1), and the left side is sum_nu khat_(3 nu) X_nu. Comparing first order in k^3,

    form^(j)(a^1, a^2, e_nu) at k^2 = -k^1 = -k equals d_(k_nu) (a^2, H(k) a^1).                                 (3.6)

This is exact, and it holds for any gauge-invariant quasi-local F with C^1 symbols. At level 0, H = khat^2 - khat khat^T, and on conserved a^1, a^2 it gives (a^1, a^2) 2 sin(k_nu), which agrees with the explicit limit in the proof of 3.8.

*The rest of the proof.* In the proof of 3.8, with v_3 in Q and u_3 = G_j(k^3) v_3 = v_3 / khat_3^2 (1 + O(eta^2)), the only change is that khat_3^2 form^(j)(u_1, u_2, u_3) tends, up to the C^1 modulus of the symbol times eta, to (3.6) contracted with v_3, at a^1 = G_j(k) v_1, a^2 = G_j(k) v_2. Taking v_1, v_2 near a unit v in P_k, this is (v_3, w(k)) with w(k) := grad_k' (u, H_j(k') u) at k' = k, u = G_j(k) v, and for G_j = (1 + O(k^2)) / khat^2 and H_j = khat^2 (1 + O(k^2)) on conserved vectors one has w(k) = 2 sin k / khat^4 (1 + O(|k|)). So for rho_0 small, w(k) ranges over a set not near any complex 2-plane, and the proof ends in the same way. Uniformity in j: the symbol of the blocked Gaussian G_j is smooth and converges as j -> infinity at fixed k, by Lemma 3.3 and the strict locality of the blocking. So at a fixed physical scale, where j -> infinity as i -> infinity, the family and eps do not depend on the scale, and g_r < g_0 holds for r small.

**3.12 Covariances with no symmetry: what I tried and what stands.** This is the attempt on the first gap in the Obligations at this stop. No theorem came out. The reduction and the negative results are kept, because they say what any theorem has to do.

*Exact reduction for a sparse family.* [Derived; E0 of `checks/witness_slice_search.py`, brute force against the formula, 1e-13.] Let p, q, r be plaquettes with pairwise disjoint corners, and a(q) := E_q + d_0 X(q) with X(q) arbitrary. On p, let m_q(p) be the mean of X(q) over the corners, y_p^q in R^2 its mean gradient in the plane of p, and c_p^q in R^2 the mean in-plane value of E_q. Write corners of a function on p in the basis constant, gradient along each axis, and staggered. The staggered part decouples: theta_bar on the links does not see it, and the antisymmetric form on corners has no matrix element with it. So, with u ^ v := u_1 v_2 - u_2 v_1, w_p^q := y_p^q + c_p^q,

    sum_p' V_p'(a(p), a(q), a(r)) = V_0(p, q, r) + sum_cyc { 2 m_q(p) P_pr - 2 m_r(p) P_pq + 2 w_p^q ^ w_p^r - 2 c_p^q ^ c_p^r }.     (3.7)

So wild lattice-scale structure enters a plaquette only through three numbers per ordered pair, and Lemma 3.2 is the case where w_p^q vanishes on aligned parallel pairs.

*Rank bound.* [Derived.] Let I_1, I_2, I_3 be disjoint subsets of the family, and A the known tensor V_0 - 2 sum_cyc c ^ c on I_1 x I_2 x I_3. For fixed p the matrix in (q, r) of the term with centre p has rank at most 4: m_.(p) tensor P_p, and the two components of w_p. So if a Gaussian potential has the Wilson tree values, then A has **tensor rank at most 4 (|I_1| + |I_2| + |I_3|)**, with no assumption on C at all, not even a bound on its entries. A generic tensor has rank of order |I|^2. This would be a proof if a rank lower bound linear with coefficient above 12 for equal sizes were available for this tensor. Known explicit lower bounds on tensor rank do not reach that (recalled: flattenings give at most about 2 to 3 times the side), so I did not get a proof from it. The numerical search below is what it points to.

*Search on sparse families.* (`checks/witness_slice_search.py`, criteria written first.) Solving (3.7) = 0 by Levenberg-Marquardt, with unknowns (m, y), 3 N (N - 1) of them, against N (N - 1) (N - 2) / 6 equations, on random sparse plaquettes:

| case | unknowns | equations | smallest relative residual, 5 starts |
|---|---|---|---|
| d = 4, N = 12 | 396 | 220 | 1e-16 (solver control) |
| d = 2, N = 30 | 2610 | 4060 | 6e-16 |
| d = 4, N = 30 | 2610 | 4060 | 2.18e-2 |
| d = 4, N = 40 | 4680 | 9880 | 4.26e-2 |
| d = 3, N = 30 | 2610 | 4060 | 5.08e-2 |
| d = 3, N = 40 | 4680 | 9880 | 7.25e-2 |

The starts agree within 5% in d = 3 and d = 4. **So at the same over-determination, d = 2 has an exact solution and d = 3, 4 do not appear to have one, and the residual grows with N.** This is numerical evidence that no Gaussian potential at all has the Wilson tree values, not a proof: a non-convex search can miss a solution, and a finite torus is not Z^4. It is also evidence of how small the margin can be: with free gauge correlations the family of 40 is matched to 4% in norm, with |m|, |y| of order 1e-2, and so a test against wild potentials must be read at a tolerance below that.

*Failed route 1: the soft limit for periodic covariances.* The proof of Theorem 3.8 does not extend to covariances invariant only under a sublattice. For period 2 a source of momentum k^3 also has gauge components at k^3 + kappa, kappa in {0, pi}^4. These enter (3.4) as a(h_3^kappa, h_1^kappa) (v_2, D khat(k^1 + kappa)), and the factor no longer vanishes on S_2^0, so h_3 at small k^3 is back in the equation, with coefficient bounded below. The rest of the argument, which used that the singular part 1 / khat_3^2 could only be met by bounded terms, is lost. Counting at each k leaves enough freedom to meet the singular term, with six or more kappa. I did not construct a solution, and the equations at k^1 + k^2 far from 0 are many more than the unknowns.

*Failed route 2: norm bounds.* Pairing (3.7) with a test tensor W gives |<W, V_0>| <= 2 M sum_b ||W_b|| |f_b| + M^2 sum_b ||W_b||, with M the size of X in the flux norm and W_b the contraction of W at the link b. So small M is excluded. But the ratio |<W, V_0>| / sum_b ||W_b|| is of order 1 at the lattice scale, and of order 1 / N for test currents at scale N, because the Levy area of small rapid gauge modes accumulates over volume, like the area of a rough path: xi_x = eta_1 cos(kappa . x) + eta_2 sin(kappa . x) has xi_x ^ xi_(x + mu) = sin(kappa_mu) eta_1 ^ eta_2 with no derivative. So at long wavelengths wild gauge modes can produce any antisymmetric form of bounded rank per lattice cell. This is why no theorem with no symmetry can come from tests at large scale alone, and why the rank per cell is the true obstruction.

*Failed route 3: the rectangle alone.* There is a translation-invariant assignment, at leading order in 1 / R and ignoring the far Levy term, that passes the whole rectangle family, if rotation invariance is dropped. Lock the planes: far field gradient in the (1,2) plane, y_q^f := R e_f^perp(y_q), with R a rotation from the (3,4) plane to the (1,2) plane, and near pairs y_r^q := (1/2) P(y_r - y_q) J R (y_r - y_q), with J the rotation by 90 degrees of the (1,2) plane. Then 2 P e_f . D is cancelled edge by edge in (3.7), with entries of Feynman size. Theorem 3.8 excludes this C by other triples. So class (ii) uses the rotation symmetry in an essential way, and class (i) uses triples beyond the rectangle.

**3.13 Covariances with no symmetry, colour-isotropic: a rank bound.** This route replaces the tensor rank of 3.12, which is a bound on the wrong object. Contract one slot of the cubic form and bound the rank of the resulting matrix. A matrix rank is something one can bound below. All steps are derived here, on the Wilson tree values at the lattice scale. The level-j form is in 3.14.

*The plaquette form.* [Derived; R1 of `checks/witness_rank_vertex.py`, 1e-15 in d = 2, 3, 4.] On a plaquette with step values a_1, ..., a_4 let phi := sum a_s, m := (a_1 - a_3) / 2, n := (a_2 - a_4) / 2, and sigma_1 := a_1 + a_2, sigma_2 := a_2 + a_3, sigma_3 := a_3 + a_4, sigma_4 := a_4 + a_1 the corner sums. As forms on the four steps, with zeta := (a_1 - a_2 + a_3 - a_4) / 4,

    sum_(s<t) a_s ^ a_t = 2 m ^ n - phi ^ (m + n + zeta),   so   K_vert = 24 VV,   VV := sum_p phi_p ^ m_p ^ n_p.                  (3.8)

VV is a 3-form on link fields, a sum of one decomposable 3-form per plaquette. Let sigma(x) := (-1)^(sum x_mu). All of phi, m, n vanish on d_0 sigma, whose steps on a plaquette alternate. Write abar(l) := a(l) / (d_0 sigma)(l). Then each corner sum and each of 2 m, 2 n is a constant times a difference abar(l) - abar(l') of two links of p, phi is a constant times the alternating sum of the abar, and the term of p is a constant times the 4 x 4 determinant with columns 1, abar, abar', abar'' on the four links: the signed volume of a tetrahedron whose vertices are the links of p. In particular the entry of B[b] := VV(., ., b) between two links of p is +- (bbar(l'') - bbar(l''')), with l'', l''' the other two links of p. (3.3) reads K_total - K_comp[c] = 24 VV(c J_1, c J_2, c J_3).

*Reduced form.* Let R_0 be a box of side L, R_1 the box of side L + 2 around it, W_0 the link fields on R_0, and **W** := W_0 + C^0(R_1) / constants. For x_i = (y_i, theta_i) put

    **V**(x_1, x_2, x_3) := VV(y_1 + d_0 th_1, y_2 + d_0 th_2, y_3 + d_0 th_3),  th_i any compactly supported extension of theta_i.

With H := d^T d, the proof of 2.2 gives, on compactly supported fields, VV(a, a', d_0 theta) = - <H a, thetabar a'> + <H a', thetabar a>, and VV(a, d_0 theta, d_0 theta') is <H a, theta'bar d_0 theta> up to sign, and it vanishes when a is a gradient. These read theta only on the supports of H y_j, which lie on links of R_1. So **V** does not depend on the extension. It is a 3-form on a finite-dimensional space, known exactly.

**Lemma 3.13 (a matching gives an isotropic graph).** [Derived.] Let c be real symmetric on links, with no other assumption, not even positivity, such that <J_p, c J_q> = P_pq on plaquettes of R_1 and K_comp[c] = K_total on triples of plaquette lassos of R_1, with fixed tails. Then for y in W_0, c (H y) = y + d_0 Y(y) on R_1, with Y linear, and S := { (y, Y(y)) } has **V** = 0 on S x S x S. Its codimension in **W** is |R_1| - 1.

Proof. <J_p, c H y> = P(J_p, H y) = <J_p, G H y> = <J_p, y>, since G H y - y is a gradient, both decaying and having one curl. So c H y - y has no flux through any plaquette of R_1, a contractible box. For plaquette currents, K_total - K_comp[c] = 24 VV(E_p + d_0 th_p, E_q + d_0 th_q, E_r + d_0 th_r), with th_p compactly supported and E_p + d_0 th_p = c J_p on R_1: K_comp reads only the values on the loops, and K_total = K_comp[a] + K_vert[a] by 2.1 and 2.2. The right side is trilinear in the currents, with th linear, so it vanishes on all currents in the span, including H y. Replacing E_i = y_i + d_0 chi_i (chi_i decaying) by y_i in VV uses the Ward identity for decaying functions, whose boundary terms vanish since the fields decay like |z|^-3 and the fluxes like |z|^-4. []

**Upper bound.** [Derived.] For b in S the 2-form **B**[b] := **V**(., ., b) vanishes on S x S. A bilinear form that vanishes on A x A' has rank at most codim A + codim A'. So

    rank **B**[b] <= 2 (|R_1| - 1).                                                                                          (3.9)

**Lemma 3.14 (lower bound).** [Derived; B1 of `checks/witness_rank_box.py`, all 48 choices in seven engineered gauges, L = 3, 4.] Let b be a link field on R_0 and pi = (mu, nu) a plane, s = +-1, rho_1, rho_2 the other two directions, h_1, h_2 in {mu, nu}. Then

    rank B[b] on W_0 >= sum_(p in pi) (2 - [c_a(p) = 0] - [c_b(p) = 0]) + #{ p in (h_1, rho_1) : mean of b on the h_1 links != 0 } + #{ p in (h_2, rho_2) : mean of b on the h_2 links != 0 },

with (c_a, c_b) = (sigma_2, sigma_4) for s = +1 and (sigma_1, sigma_3) for s = -1, the corner sums of b.

Proof. Let D(l) := tau . (midpoint of l), tau := e_mu + s e_nu. Conjugating by exp(t D) does not change the rank, and exp(-t) exp(t D) B exp(-t D) tends to C_+, the part of B with D(column) - D(row) = 1, the largest shift. So rank B >= rank C_+. Going through the plaquettes: in pi, the shift 1 entries are the 2 x 2 block with rows the two lower links and columns the two upper links; a plaquette of (h, rho) contributes the hop (x, rho) -> (x + e_h, rho), with entry the mean of b on its h links; every other entry has shift at most 1/2. Rows and columns of the blocks of pi are disjoint, and they do not meet those of rho_1, rho_2. So C_+ is a direct sum. By the entries above, twice the block is, for s = +1, [[sigma_3, sigma_2 - sigma_3], [sigma_4 - sigma_3, -sigma_1]], which unimodular row and column operations bring to [[sigma_3, sigma_2], [sigma_4, 0]], using sigma_1 + sigma_3 = sigma_2 + sigma_4. Its rank is at least [sigma_2 != 0] + [sigma_4 != 0]. For the hops on rho-links, order rows by x_(h') - x_h, with h' the other element of pi: the hops along h form a triangular matrix with diagonal the means. []

**Lemma 3.15 (few things can vanish).** [Derived; B2 of `checks/witness_rank_box.py`.] Let f be a flux on R_0, outside a finite union of hyperplanes and with f_p != 0 for all p. Let b have d b = f, and consider on the plaquettes of R_0 the six pair functionals sigma_1, ..., sigma_4, 2 m, 2 n. Let Ob := #{zero sigma_i} + 2 #{zero means}. Then

    Ob <= 9 R,   R := rank on link fields of the zero functionals,   R <= |R_0| - 1.

Proof. If a combination of the zero functionals lies in the conserved currents Z, as a functional xi, then xi(b) = 0 is a linear relation on f. There are finitely many subsets of the functionals, so f outside finitely many hyperplanes excludes all such relations, and the span of the zero functionals meets Z only in 0. Its dimension is at most dim(W*/Z) = |R_0| - 1. Join two links of a plaquette when their pair functional vanishes. Since each functional is a difference of bbar, the rank is the graph rank: v_c - 1 on each component c with v_c links, on which bbar is constant. A plaquette has at most 3 links in one component, since four would give f_p = 0. A plaquette with k = 3 links in c contributes 2 corners and 1 parallel pair, weight 4; k = 2 contributes at most 2. So its weight is at most (4/3) k, and since a link lies in at most 6 plaquettes, Ob_c <= 8 v_c. Also Ob_c <= 2 * (number of pairs) = v_c (v_c - 1). The smaller of the two is at most 9 (v_c - 1). []

*The average.* Over the 48 choices of (pi, s, h_1, h_2) in 3.14, a zero corner is lost in 4 of them, a zero mean in 8. So the mean loss is Ob / 12 <= (3/4) (|R_0| - 1). Each choice has base value 4 L^2 (L - 1)^2. In the box there is a choice with

    rank B[b] >= 4 L^2 (L - 1)^2 - (3/4) (L^4 - 1).                                                                          (3.10)

**Theorem 3.16 (no Gaussian potential c tensor 1_3 has the Wilson tree values; no symmetry).** [Derived given 3.13 to 3.15.] In d = 4, for L >= 21, there is no real symmetric c on links with the P_pq and the K_total of the Wilson weight on the plaquettes of a box of side L + 2.

Proof. Take b := (y_b, Y(y_b)) in S with y_b in W_0 of generic flux on R_0; W_0 reaches every closed flux on R_0. On (W_0, 0) x (W_0, 0) the form **B**[b] is the local matrix of 3.14. So (3.10) and (3.9) give 4 L^2 (L - 1)^2 - (3/4)(L^4 - 1) <= 2 ((L + 2)^4 - 1). At L = 21 the left side is 559740 and the right side 559680. Larger L only widens it. []

No translation or rotation invariance, no positivity, no bound on c, no regularity. The unknown gauge parts enter only through the budget R, not through any estimate, which is why wild lattice-scale structure costs nothing.

*Numbers.* (`checks/witness_rank_box.py`, `checks/witness_rank_vertex.py`, `checks/witness_dense_search.py`.) The true rank of B[b] is far above the bound: W - 2 in every gauge tried, against 2 (V - 1) about W / 2 (generic, smooth, axial, light-cone, piecewise axial, greedy maximal zero sets; L = 3, 4, and tori). Ob is about 1 / 5 of 9 R in the greedy gauges. An adversary on the torus T = 3, minimising the singular values beyond the bound in absolute size over X, stops at 0.52 to 0.75 of the tail at X = 0, the same value from three starts, with full rank. (A first form of that adversary, normalised by the largest singular value, was fooled by huge localised X and is recorded as uninformative in the script.) A direct search on the dense family, all cycles of a box with one gauge function per current per site, gives relative residual 0.19 on the single hypercube (255 unknowns, 680 equations) and 0.42 on 2 2 3 3 (1715, 18424). So numerically the family could be a single hypercube, and L = 21 is only what the crude count gives.

*Dimensions.* [Derived.] In d = 2 the bound (3.9) is the size of the matrix: no contradiction, as Proposition 1.2 requires. In d = 3 the base value is 3 per site (a plane and one hop direction). There are 12 choices, and each zero corner or zero mean is lost in 2 of them. A link lies in 4 plaquettes, and a plaquette with k links in a component has at most k pairs when k = 3, at most k / 2 when k = 2. So the count of zero pairs in a component is at most min(4 v_c, v_c (v_c - 1) / 2) <= 4.5 (v_c - 1), the mean loss is at most (3/4) |box|, and rank B >= (9/4) |box| against 2 |box|, at large L. For d >= 5 the base value is d per site, against 2. So for colour-isotropic c the rank route separates d = 2 from d >= 3, the true dichotomy. This corrects my earlier remark that d = 3 escapes: that was a limit of the soft-limit proof of 3.8.

*The translation-invariant case in one paragraph.* [Derived.] For c = c tensor 1_3 translation invariant, 3.8 has a shorter proof. For b in S_q nonzero and a.e. k^1, the 4 x 4 matrix M(b) of Lemma 3.6 vanishes on S_(k^1) x S_(k^2), each of codimension 1, so rank M(b) <= 2. At q = 0 it is 2 (kappa . beta) 1 - kappa beta^T - beta kappa^T, kappa := khat, beta := D b, exactly, whose eigenvalues are 2 (kappa . beta) twice and (kappa . beta) +- |kappa| |beta|: rank 4 for generic k. Minors are trigonometric polynomials in k^1, and q -> 0 is continuous, so rank M(b) >= 3 a.e. for small q. This is a contradiction, in d = 3 as well (M is 3 x 3 there, rank 3 against 2).

**Theorem 3.17 (closure: no bound on the gauge parts at quadratic order).** [Derived given 3.13 to 3.15; the constants below are from leading terms.] For L large (L = 150 suffices in the leading count), **V** has no isotropic subspace of codimension |R_1| - 1 at all, graph or not. So there is eps_0 > 0, depending on L only, such that every real symmetric c has either a pair defect |<J_p, c J_q> - P_pq| or a triple defect |K_comp[c] - K_total| at least eps_0, on plaquettes of R_1, with no bound on the entries of c.

Proof. Let S be isotropic of that codimension, and add to it the null vectors (d_0 th_0, -th_0) of **V**, with th_0 interior. Let F_S be the flux image of S on R_0 and g := dim F_S^perp in Z(R_0). The elements of S with no flux on R_0, modulo nulls and up to boundary terms, give a space G_S of gauge functions of dimension about g, with Theta_J(th, th') := <J, thbar d_0 th'> = 0 on G_S for all currents J of S. The matrix of Theta_J is the antisymmetric adjacency matrix with weights J(l) / 2, and hops along one direction are triangular, so its rank is at least the number of nonzero J_mu(x) for each mu. A generic J in a subspace of dimension D has support at least D, here (3 - g / Lam) Lam with Lam := |R_0|. An isotropic space has dimension at most Lam - rank / 2. So g / Lam =: gamma <= 1 - (3 - gamma) / 8, gamma <= 5 / 7 + O(1 / L). Take b in S with generic flux in F_S. Lemma 3.15 changes: the span of the zero functionals meets Z in at most g dimensions, so R <= Lam - 1 + g; and a plaquette may now have four links in one component, when phi_p lies in F_S^perp, which adds 8 / 3 per such plaquette; there are at most 3 g of them, since at most 3 plaquettes share a lexicographically largest link, so plaquette currents have rank at least a third of their number. So Ob <= 9 (Lam + g) + 8 g, and (3.10) becomes 4 - 3/4 - (17 / 12) gamma >= 2.238 per site at large L, against 2 from (3.9), with boundary terms of order L^3. Then let Psi(S) be the largest value of |**V**| on unit vectors of S. It is continuous and positive on a compact Grassmannian, so it has a positive minimum. For c as stated, take an orthonormal basis x_i = (y_i, Y(y_i)) of S_c, so |y_i| <= 1. The defects bound |**V**(x_i, x_j, x_k)| by a constant times the largest defect; an error e in the flux enters K_comp as Levy terms in (e_j, s_k) with |e_j| <= C eps and |s_k| <= C, so large gauge parts are harmless. []

**Corollary 3.18 (the family, for all colour-isotropic Gaussian potentials up to link variance g^(4/3)).** [Derived given 3.17 and Lemma 3.1.] There are eps, c_1, g_0 > 0 and a finite family, namely the pair functions and T on the plaquette lassos of a box of side L + 2, such that for g < g_0 and every centred Gaussian potential with C = 4 g^2 c tensor 1_3, c positive semidefinite with no symmetry and c_bb <= c_1 g^(-2/3), some f in the family has |mu_C(f) - W_g(f)| >= eps g^(deg f). Proof: Lemma 3.1 has remainders kappa_hat^2 g^4 in the pair functions, relative g^(2/3), and kappa_hat^3 g^6 in T, relative c_1^3. []

So the upper limit on link variance has moved from a fixed multiple of g^2 to c_1 g^(4/3), and the whole of it is covered by one family with one eps. Above g^(4/3) the Levy triple of the next paragraph enters.

*What this does not do, and why.* **(a) Colour mixing.** T is a colour singlet. By (3.4), gauge parts enter only as a(h_j, h_l) = 6 t_j t_l / 9 - tr(Y_j Y_l), with t the trace and Y the traceless part. So with colour mixing the system is the one above with nine gauge functions per current per site, with signature (+, + + +, - - - - -): trace, antisymmetric, symmetric traceless. There is no labelled isotropy to use, only the singlet. The upper bound (3.9) becomes 18 per site against a matrix of size 12 per site: empty. Numbers from `checks/witness_dense_search.py`, dense family, Gauss-Newton with a limited number of steps, so these are upper bounds on the true smallest residual:

| box | flavours | unknowns | equations | relative residual, starts |
|---|---|---|---|---|
| 2 2 2 2 | 1 | 255 | 680 | 0.19, 0.20, 0.28 |
| 2 2 3 3 | 1 | 1715 | 18424 | 0.42, 0.47, 0.42 |
| 2 3 3 3 | 1 | 4346 | 88560 | 0.62, 0.58 |
| 2 2 2 2 | 9 | 2295 | 680 | 2e-14 (control, under-determined) |
| 2 2 3 3 | 9 | 15435 | 18424 | 6.4e-3, 5.8e-3 |
| 2 3 3 3 | 9 | 39114 | 88560 | 2.7e-2, 2.8e-2 |
| 3 3 3 3 | 9 | 97920 | 410040 | 7.1e-2 |

So colour mixing has far more room, by a factor 10 to 20 in the residual, but it does not reach an exact solution in the steps run, and the residual grows with the box: 6e-3, 2.7e-2, 7.1e-2 at over-determination 1.2, 2.3, 4.2. Criteria D3, D4 read this as evidence only, against an exact solution. I do not have a theorem here; for translation invariance 3.8 still covers it, by the soft limit. **(b) Level j.** See 3.14. **(c) Mean.** A non-zero mean with flux o(g) and bounded gauge part changes T only at higher order; a large mean gauge part rotates colour frames, which is the colour-mixing case.

**3.14 What the level-j action changes.** (Implication and a named open statement.) Let F be gauge invariant and local, with quadratic form H = phi^T h phi. Its cubic form has the same Ward identity with H, and VV^F - sum_p (h phi)_p ^ Theta_p is annihilated by contraction with gradients, so it is a 3-form in fluxes alone. [Derived.] That is, with phit_p := sum_q h_pq phi_q and tau_pq any link functional with tau_pq(d_0 th) = thbar_p - thbar_q,

    VV^F = 2 sum_p phit_p ^ m_p ^ n_p + (1/2) sum_(p, q) h_pq tau_pq ^ phi_q ^ phi_p + (a 3-form in fluxes).                  (3.11)

The reduced form **V** and the upper bound (3.9) are the same, and the gauge dependence of **V** is the same polynomial; only V_0 and the field values change. What fails is Lemma 3.14. It uses a largest shift, and F_j has exponential tails, so conjugation is limited to weights below the decay rate. So one box is not enough at level j, and the argument below uses many.

*The elimination.* [Derived, exact, any F.] Let C_i be boxes of side L_c on a grid of spacing D, and b a far plaquette (the third current). Let A_i := a_b on C_i, a field with uniform flux F up to O(L_c / R), and write A_i = e_F + d_0 t_i with t_i arbitrary. Let N_i := {J in Z(C_i) : rho(J, A_i) = 0}, rho_x(J, A) := (1/2) sum_(l at x) J(l) A(l). In normalised variables, rho(J, A) = 0 says that J and the product of J with abar(l) := A(l) / (d_0 sigma)(l) are both conserved. For J in N_i, J' in N_j, i != j, the system for (J, J', b) loses all near gauge parts, since they enter only as <X, rho>:

    VV^F(G J, G J', E_b) - <J, tbar_i E_J'> + <J', tbar_j E_J> + Far_b(J, J') = 0,                                          (3.12)

where Far_b is the Levy term on the far plaquette, a bilinear form of rank at most 6 (three numbers per current for its gauge part, three for the field values).

*Universality.* [Derived at the level of the steps; numbers below.] Let PP_h be the polynomial link fields of degree at most 3 with H u = 0, and P[F', F] a polynomial with H P = J2(e_F', e_F), J2(l) := VV(delta_l, e_F', e_F). If H_F - H has at least four derivatives on polynomials, which lattice symmetry and gauge invariance give, then PP_h and the top part of P are the same for F_j as for Wilson. Lower-degree parts of P are in PP_h. For J in NN(t) := N intersect PP_h^perp,

    first two terms of (3.12) = m_J(F') + O(L_c / D), with F' the flux of G J' at C_i,    m_J(F') := <J, P[e_F', F] - tbar e_F'>,        (3.13)

and the third term of (3.12) is smaller by D^-3, since E_J at C_j has no dipole, quadrupole or next moment. The value of m_J on NN(t) does not depend on the gauge of e_F': the Ward identity turns a gradient into <X, rho>. So at long distance **the level-j cubic form has dropped out**, in the sense that m_J is the same lattice object for every F_j. Current of two fields in the continuum: J2_nu(A', A) = -(d . A') A_nu + (d . A) A'_nu - A' . d_nu A + A . d_nu A' + 2 F'_mu_nu A_mu - 2 F_mu_nu A'_mu. For A = M x + c, A' = M' x + c', this is R(M) A' - R(M') A, R(M) := tr(M) 1 - 2 M + M^T.

*The kernel.* [Derived given the statement below.] With F'(z) = Q(z) dip(J') + ..., Q(z) the dipole field of Lemma 3.3, invertible, the matrix of (3.12) between cells I and cells I' disjoint is u_i . Q(z_i - z_j) d_j up to corrections, u_i := m_(J_i), d_j := dip(J'_j). By (3.12) it has rank at most 6. But kappa_(u, d)(z) := u . Q(z) d is a nonzero homogeneous analytic function of z, and a translation-invariant kernel of finite rank is an exponential polynomial, so kappa(z - z') has infinite rank. Take a finite net of directions (u, d); for each net point a 7 x 7 configuration with nonzero determinant; and let the grid be large enough for the Gallai-Witt theorem to give a copy, scaled and with one colour, of the union of the configurations, in any colouring of the cells by the nearest net point of (u_i, d_i). Homogeneity keeps the determinants. So a matching on this one finite family is impossible, whatever the t_i, as soon as:

    (RANK-U)  For F != 0 and t on a box of side L_c with |d_0 t| <= M |F|: the limit of NN(t) along any sequence in this set carries an m that is not zero, and N(t) a dip that is not zero; with the row normalised against the higher polynomial moments of the same J, so that the corrections in (3.13) are small against it.

This is a statement on one box, about polynomials and an arbitrary function t, with no level and no g in it. M is finite: by Cauchy-Schwarz |a_b(l)| <= (kappa_hat_0 P_bb)^(1/2), so M is about kappa_hat_0^(1/2) R^4 for a plaquette at distance R. It cannot be dropped: as t grows, m tends to 0 like |F|^2 / |d_0 t|, because a polynomial pure gauge at F = 0 has m = 0 (a run at L = 5 showed this, with t up to 1e4, all singular values small and non-zero).

**Theorem 3.19 (the level-j form; implication).** [Derived given (RANK-U), and the far-field inputs of Theorem 3.10 and Lemma 5.4; the correction terms are estimated, Text 7, item 29.] Fix kappa_hat_0. For colour-isotropic c with no symmetry and c_bb <= kappa_hat_0, on the level-j lattice, the level-j tree values are not matched on a finite family of pair tests and T on triples (J, J', b) over the cells, the family depending on kappa_hat_0. With Lemma 3.1 and Lemma 5.2 this would give class (iii) of Theorem 5.5.

*A sketch for (RANK-U).* [Not a proof.] m = 0 for a flux F' means: there is A' := e_F' - d_0 lambda + u, with u in PP_h, with VV(delta_l, A', A) = 0 on interior links. Write t = t_s + t_r, smooth and rough. The term lambdabar d_0 t_r = d_0(lambda t_r) - tbar_r d_0 lambda shows that the rough part of t sees only the smooth field A'_s := e_F' - d_0 lambda_s. At frequency q the rough part of the equation, with A_s = c locally, reads cos(q_mu / 2) (A'_(s mu) that + c_mu lambdahat) = 2 i sin(q_mu / 2) chihat for each mu, so A'_s lies in the plane of c and tan(q / 2) whenever that is not zero. If t_r has modes at two generic q, A'_s is parallel to A_s at that point. Then F' - alpha F = d_0 alpha ^ A, so A ^ F' is parallel to A ^ F. Since A ^ . has rank 3 on 2-forms, at most 4 directions F' satisfy it: rank m >= 2, the same number as in polynomial gauges. The exceptions are modes staggered in three directions, t_r = sigma_perp(x) f(x_4): they have tbar zero on three directions and they pass. This is a WKB statement on large boxes. To be a proof it needs the two scales separated, and t_r not small against c. I have not done that.

*A weaker statement suffices.* [Derived.] The gauge part X_J' on C_i is one function, for all third currents. So with two far plaquettes b_1, b_2, rows in tensors J_1 tensor b_1 + J_2 tensor b_2 with rho(J_1, A_1) + rho(J_2, A_2) = 0, and columns in N_j(A_1) intersect N_j(A_2), which has about one current per site left, the near gauge parts still drop out. Then (RANK-U) is needed only in the form: there is no single lambda_F' with P[e_F', F_a] - tbar_a e_F' in (lambdabar_F' A_a + PP_h + gradients) for both a = 1, 2 and all F'. Three far plaquettes leave no columns in this form. In the sketch above, rough t_1 and t_2 would force the smooth part of e_F' - d_0 lambda to be parallel to both A_1 and A_2, so zero where they are independent. I expect this form to be the one to prove.

*What is known about (RANK-U).* [Numerics, evidence only. `checks/witness_rank_moment.py`, `checks/witness_rank_poly.py`.] Singular values of the six-component m on NN(t):

| t | F | L = 4 | L = 5 | L = 6 |
|---|---|---|---|---|
| Fock | generic | 1.3, 1.1, 0.76, 0.58, 0, 0 | 5.4, 4.9, 3.5, 3.2, 0, 0 | 15.5, 14.8, 9.8, 9.3, 0, 0 |
| Fock | simple F_01 | all 0 (small-box artefact) | 3.0 four times, 0, 0 | 11.4 four times, 0, 0 |
| a_nu = x_mu gauge | generic | 1.9, 1.6, 0.09, 0.008, 0.003, 0 | 7.8, 7.7, 0.5, 0.10, 0.04, 0 | 22.0, 21.7, 1.2, 0.30, 0.07, 0 |
| a_nu = x_mu gauge | simple F_01 | 1.95, 1.95, 0 ... | 7.9, 7.9, 0 ... | |
| random, amplitude 1 | generic | 4.2, 4.1, 3.6, 3.4, 3.0, 0 | 9.9, 9.7, 9.0, 8.6, 8.1, 0 | 24, 23, 20, 19, 18, 0 |

m(F) = 0 to 1e-14 in every case: this is the derived identity, and it is why the last value is always 0. Prediction M2' (rank 4 in Fock gauge, since [F, *F] = 0 and J2 = (3/4) [F, F'] x) holds at L = 4, 5, 6 for generic F, and for simple F from L = 5. In polynomial gauges, solving R(M) M' = R(M') M, the largest dimension of fluxes reached is 4, so the rank is at least 2, attained by M of rank one with u . v = 0, such as A = x_0 e_1, whose partners are x_0 e_2, x_0 e_3 and F_23. These are the non-abelian plane waves. An optimiser over M found the same value and no lower. So the smallest rank seen is 2, against the 1 needed. **The one case that looked like a counterexample, L = 4 with simple Fock, went away at L = 5**, so adversaries must run on L >= 5.

An adversary at L = 5, |F| = 1, |t| <= 30 (M5), over polynomial gauges, functions of one or two coordinates, and rough t, two starts each, Powell with 400 evaluations, minimising the sum of squares of all singular values of m. For generic F the smallest total is 0.117 of its value in Fock gauge, with singular values 2.0, 1.6, 1.4, 0.63, 0.27. For simple F the smallest is 5.5e-3 of Fock, for a function of x_0, with singular values 0.34, 0.29, then 8e-5, 6e-5, 3e-5: the rank-2 family again. Rough starts stay above Fock. So no zero of m appeared, and the criterion's threshold (1e-4) is not reached; numerical evidence only, at one size. dip on N(t) has rank 5 in every case at L = 5 (singular values 21 to 3), the sixth being F . dip = 0, which is the identity <J, A> = 0. A t staggered in three directions, which the sketch says should pass, does change the values (7.5, 1.1, 0.6, 0.2, 0.05 from 7.8, 7.7, 0.5, 0.1, 0.04); so the sketch is not sharp there, and the rank stays 5.

*Check of (3.13) on real fields.* (`checks/witness_cross_cell.py`, Wilson lattice, T = 36, double precision.) For exact polynomial fields (3.13) is an identity by summation by parts, since G J decays fast when J is orthogonal to PP_h. On real far fields it has corrections in L / D with a coefficient near 2 L / D, since |grad F| / |F| = 4 / |z|. The test is the matrix Mat := VV(G J, G J', E_b), J in NN on one cell, J' in N on another, combined so as to have no field on the far plaquette, against Pred := m_J(F'(J')). Registered: Frobenius error below 0.5 at L = 3 in three geometries. **That fails at L = 3** (1.9, 33, 7.7): there NN has dimension 23 and m is nearly rank one and tiny, so the box is too small to carry the statement. At L = 4, run in the same job: error 0.35, 0.54, 0.45, and the largest singular values agree: 2.36e-11 against 2.17e-11, 3.42e-11 against 3.45e-11, 1.16e-10 against 1.34e-10. So at L = 4 the formula has the right size and sign at about the expected accuracy, in the leading direction, with D = 11 and 17. The smaller singular values do not agree, as expected at this L / D. An earlier test with J' a plaquette failed for a reason I then found by hand: J' must be in N_j, or a charge term larger by R / L appears. Two bugs in that script are recorded in it (a rank tolerance, and single-precision momenta). This is support at one size, not a proof.

*What failed on the way.* (a) A single pair of boxes: the matrix has rank at most 12, and at t = Fock on generic F it has rank 8 against 6 from Far_b, while a simple F, which is what a far plaquette gives (the dipole field of a simple 2-form is simple), has rank 4. That was too close, and the count looked lost in several gauges until many cells made the main rank grow without bound. (b) Taking a kernel of the map J |-> X_J on far loops, to remove Far_b: the adversary can take X = L(flux), and then the kernel has no flux. (c) A rank condition at one plaquette over pairs of far fields, which has rank at most 2 modulo phi and has no t in it: the far stars on the far loops have unbounded rank, so it is not usable without an assumption like (B). (d) Tests at long wavelength only: rough-rough products have no constraint (Text 3.12, route 2).

*A limit of Corollary 3.9.* When the link variance is large against g^2, there is one more channel that Lemma 3.1 hides. For colour-isotropic gauge modes theta with covariance kappa C-hat, Q_Gamma is of order kappa and T has the term (1/4) <Q_1 . Q_2 x Q_3>, proportional to kappa^3 Tr(l_1 C-hat l_2 C-hat l_3 C-hat), with l_i the antisymmetric form of the Levy area around Gamma_i. At kappa of order g^(4/3), that is amplitude g^(2/3) against flux g, it is of the size of the signal, with Q still small against the flux, so the pair tests do not see it. So the bound on the link variance in class (i) is not technical: above g^2 kappa_hat_0, T has a new term whose structure is a product of three two-point functions. It is not a star, which is why I expect it not to match on a family, but I have not shown that.

**Lemma 3.20 (excess kurtosis of a truncated plaquette).** [Derived; K1 of `checks/witness_kurtosis.py`.] Let u, xi, xi' be colour vectors, jointly Gaussian and colour isotropic, with any correlation, and psi := u + xi x xi', Q := xi x xi'. Then E|psi|^4 - (5/3) (E|psi|^2)^2 = (5/3) delta^4, delta^2 := E|Q|^2 = 6 (v v' - c^2). Proof. Terms odd in the fields vanish. Write u = u_par + u_perp with u_perp independent of (xi, xi'). A change of (xi, xi') of determinant one leaves Q fixed, so u_par may be taken along xi. Then u_par . Q = 0 and E|u_par|^2 |Q|^2 = 30 alpha^2 v^2 v_perp against E|u_par|^2 E|Q|^2 = 18 alpha^2 v^2 v_perp, and 2 (30 - (5/3) 18) = 0, while for u_perp, 2 + 4/3 - 10/3 = 0. What is left is E|Q|^4 - (5/3) (E|Q|^2)^2 = (120 - 60) (v v_perp)^2. []

On a plaquette Q has exactly this form, with xi, xi' the two diagonal differences, whatever the number of modes, so a plaquette cannot hide its Levy area as Gaussian-looking noise. Since Y has excess kurtosis of size g^6 up to logs by the rate of Lemma 5.1', a test of E s_p and E s_p^2 bounds delta by g^(3/2) up to logs, and then |<Q_1 . Q_2 x Q_3>| is below g^(9/2) up to logs, under g^4. So the Levy triple is not the obstacle above g^(4/3). [Derived at this level; the terms of higher degree are the next paragraph.] The degree-3 term R_3 of psi adds to the excess a connected term of size (g^2 M)^3, M the size of the flux-link correlation in units of g^2, and to T a term of size g delta kappa^(3/2) and g^2 kappa^2. For gauge modes uncorrelated with the flux, M is bounded, and T = g^4 K_comp (1 + O(kappa)) + o(g^4) up to kappa of order g^(1/2). This is a count, not a proof, and correlated modes with M large are not covered above kappa_hat of order g^(-2/3).

### 4. NT1

**Theorem 4.1 (H is not zero, from two separations).** [Derived given Theorem 10.2 of `parts/upper-chain.md`, with the gate's D10 and D13.] Let A, B be in a countable family as in Theorem 10.2, with A, B real, and x, x' = x + t e_4, t > 0, offsets such that the supports of A and tau_x B, and of A and tau_(x') B, are strictly ordered along all four axes. Let c(y) := lim_i ( <A_i tau_y B_i> - <A_i> <B_i> ) along the subsequence, at L-adic y near x and x'. If c(x) != c(x'), then in the reconstruction of Theorem 10.2(d), H is not zero on the orthocomplement of Omega.

Proof. For n = 2 there is one cut, so Lemma 10.1 applies directly and the gate's D11 does not arise: C_i is equi-Lipschitz near x and x', and c extends to a continuous function there, equal to the limit of the mollified correlators as the mollifier shrinks. Let phi, phi' >= 0 have integral 1 and small support. Translate so that a time plane separates the supports, put A' := Theta A, in the family by reflection invariance, and F := A'[phi], G := B[phi'], both supported in t > 0, with separation in time at least the time gap. By Theorem 10.2(d), for s >= 0,

    S(Theta F . tau_(s e_4) G) - S(F) S(G) = < [F]_perp, exp(-s H) [G]_perp >,   [F]_perp := [F] - S(F) Omega,

since exp(-s H) Omega = Omega. If H = 0 on the orthocomplement of Omega, the right side does not depend on s. The left side is an average of c(y + s e_4) over y in the small support of phi and phi', near x. Taking supports to a point, c(x + s e_4) = c(x) for s in [0, t], which contradicts c(x') != c(x). []

Quantitatively, for F = G the function s -> S_c(s) is completely monotone, and if H <= Lambda on the cyclic subspace of [F]_perp then S_c(t_2) >= exp(-Lambda (t_2 - t_1)) S_c(t_1). So the ratio also gives a lower bound on the top of the spectrum there. It gives no gap and no clustering: a part of the spectral measure at 0 is not excluded, so NT1 as defined does not imply a unique vacuum.

**Corollary 4.2 (the gate's suggestion, checked).** Let p be a level-j plaquette in the (1,2) plane and x = (d, d, 2d, 2d), x' = (d, d, 2d, 3d). The Maxwell values are P(x) = 0.6 / (100 pi^2 d^4) = 0.00600 / (pi^2 d^4) and P(x') = (11/15) / (225 pi^2 d^4) = 0.00326 / (pi^2 d^4), so the Gaussian values (3/2) g^4 P^2 differ by a factor 3.39. If Cov(s_p, s_(p + x)) and Cov(s_p, s_(p + x')) are each within a factor 1 +- delta of (3/2) g_j^4 P^2, with delta <= 1/2, along the trajectory at fixed level distance from the top and in the limit i -> infinity, then H != 0 on the orthocomplement of Omega. Given (WIT) at one separation and the upper bound at another, no vertex is used, and none is needed: **NT1 is a statement about the free propagator's decay at a scale where the fibre is Gaussian. It is a corollary of Theorem 10.7 at two values of the offset.** The static law of the gate's D1 fails this: its correlator is the same at x and x'.

What it consumes: the relative error delta <= 1/2 at the two offsets, along the trajectory, at one fixed level distance m. No rate is needed for omega. Without an input NT1 cannot hold: beta_i -> infinity fast gives a flat limit, with an empty orthocomplement. Theorem 4.3 below supplies the relative error from (OS_j) and (FF) by a route that avoids the gate's D5.

**Theorem 4.3 (local Gaussian limit of the full law at level j; implication).** [Derived given (FF), (OS_j) uniformly in j <= K - m_0 with the gate's D6, D7 repaired, C_s free of L, and the flow.] Fix L. Let A be a polynomial of bounded degree in the rescaled fluxes psi_p / g_j, p in a ball of bounded radius. Then E[A] -> E_(N(0, Gamma^(j)))[A] as g_j -> 0 uniformly in the volume, where Gamma^(j)_pq = 4 P^(j)_pq 1_3 with P^(j) the full Gaussian covariance of level-j flux, the covariance of the blocked Gaussian. In particular

    Cov(s_p, s_q) = (3/2) g_j^4 ( (P^(j)_pq)^2 + o_L(1) ),   as g_j -> 0 at fixed L and p, q.

Proof. Let eps_j(n) be the sup over monomials of degree at most n, with coefficients bounded in the class closed under the lift, of the error at level j. In one step, on G, condition on W. By (b), (c), E_W[A] is the Gaussian moment with mean phi and covariance Gamma^fib(W), up to omega_L(g_j) and C(L) g_j times polynomials in phi. By (d), Gamma^fib(W) may be replaced by Gamma^fib(1), up to C(L) |F^*|, of mean C(L) g. What is left is a polynomial in phi, with phi_p = (g_(j+1) / g_j) sum_c A_pc psi_c(W) / g_(j+1) + O(C(L) g), and |A_pc| <= C_s L^(-kappa) with tails. Since Gamma^fib + (A Gamma^(j+1) A^T) = Gamma^(j), by the Gaussian conditioning identity for the blocked Gaussian, the term of the recursion with the moment at level j + 1 reproduces the Gaussian moment at level j, up to L^(-2 kappa) C_s^2 eps_(j+1)(n), since every coarse-field monomial carries at least two factors of phi. G^c costs less than any power of g by high moments. So eps_j(n) <= (1/2) eps_(j+1)(n) + o_L(1), for L large. At j = K - m_0 the a priori bound is finite by Lemma 10.6. Iterate over the levels. []

**Remark (the gate's D5 is avoided).** D5 said that the constants of (FF_j) depend on L, so that Theorem 10.7's bound, with errors C L^(-2 kappa), has no controlled gain. In Theorem 4.3 no such error is left in the limit: moments of order 1 at each level enter with a constant allowed to depend on L, and each is multiplied by a positive power of g, so L stays fixed and g_j -> 0 by going down the levels. What is lost is any statement at g_j of a fixed size relative to L: the scale r must be small enough given L. For NT1 and NT2 that costs nothing, since one scale suffices, and the trajectory has g_r -> 0 as r -> 0.

**So NT1 is an implication given (OS_j), (FF), uniformity in j, and the flow, with no separate estimate and no vertex.** The gate's D6 and D7 stay with (OS_j). A proof by a route that does not go through the fibre was not found. An easier form, which needs only upper bounds on the correlator at large time together with one lower bound, is the same statement.

### 5. What accuracy the test demands, and from which one-step statement

**5.1 The rate.** T is of size g^3 and its mean is of size g^4, so a third moment of the fibre variables must be known to o(g). Theorem 10.7 has omega(g) with no rate, and Lemma 10.9 bounds the first-order term rather than evaluating it, so neither reaches the test. All that is demanded is o(g) with the first-order term evaluated. A power g^(1 + delta), or g^2 times a power of log(1/g), is more than enough. There is no demand on L beyond those already made: the order is L fixed, then g -> 0.

**Lemma 5.1 (local Gaussian limit to first order, with a cut).** [Derived from Steps 1 to 4 of `library/convex-laplace-tree-decay.md`, which I read and did not recheck. It replaces Lemma 10.9.] In the setting there, with no parameter v, let S = (1/2) <xi, H xi> + g R_3 + R_4 on K = prod K_c, where H >= gamma has exponentially decaying kernel, R_3 is a cubic polynomial and R_3, R_4 are sums over x of local terms r_x, r'_x with

    |D_xi^alpha r_x| <= C e^(-mu tau(x, alpha)),   |D_xi^alpha r'_x| <= C g^2 e^(-mu tau(x, alpha)) Omega(x)^(4 - |alpha|)_+,  for |alpha| <= 4,

and Hess(S_tau) >= gamma / 2 for S_tau := (1/2) <xi, H xi> + tau (g R_3 + R_4), with the cut Psi = sum_c Psi_c as in Lemma 10.9 (chi_c = exp(-Psi_c) = 1 on |xi_c| <= rho). Then for a polynomial A of bounded degree in the xi near a finite set D, with bounded coefficients,

    | E_mu[A] - E_0[A] + g Cov_0(A, R_3) | <= C_A ( g^2 + exp(-c rho^2) ),

with E_0, Cov_0 in N(0, H^-1), C_A and c free of the volume, and Cov_0(A, R_3) absolutely convergent uniformly in the volume.

Proof. With the cut fixed, d/dtau E_tau[A] = -Cov_tau(A, g R_3 + R_4). By (C) and (M), |Cov_tau(A, R_4)| <= C g^2. Write Cov_tau(A, R_3) = Cov_0(A, R_3) - integral_0^tau kappa_(3, sigma)(A, R_3, g R_3 + R_4) d sigma, with kappa_3 the third cumulant. For one pair of local terms r_x, r_y, Step 4 (S) splits kappa_3(A, r_x, r_y) at the largest edge of a minimal spanning tree on the three supports, and (C) with (M) bounds it by C exp(-delta' tau(D, x, y) / 2). The double sum over x, y is bounded, uniformly in the volume. So |kappa_3(A, R_3, g R_3 + R_4)| <= C g, and the first term becomes g Cov_0(A, R_3) + O(g^2), where E_0, Cov_0 so far are in the Gaussian with the cut. Remove the cut one cell at a time. For E_0[A] this is Step 2 of Lemma 10.9. For Cov_0(A, r_x), adding the cell c_0 changes it by kappa_3(A, r_x, chi_(c_0)) / E[chi_(c_0)] up to products of covariances, and by (S), (C) this is at most C exp(-delta' tau(D, x, c_0) / 2) exp(-c rho^2 / 2), because D chi_(c_0) is bounded and supported on |xi_(c_0)| > rho. The sums over x and c_0 are bounded, free of the volume. So the total cost is C exp(-c rho^2). []

So on the route of hard-core--mapped, what is asked of hard-core is a refinement of (H2) by powers of g, which is what x g^2 = 1 and the chart give by counting derivatives (D_xi^a of x F(V(g xi)) carries g^(a-2)), and the Taylor split at third order.

**Lemma 5.1' (the same from (EI), on the route of hard-core--independent).** [Derived given (EI), the Mobius form of Text 4.6 there, and `library/ultralocal_cluster_expansion.md`, which I read and did not recheck.] Let nu be the white-noise product measure with the cut |xi_c| <= p(g), and suppose that Psi = sum_X H(X; xi, W), with |H(X)| <= H_0 exp(-kappa |X|) on the cut, H_0 small. Let A be a polynomial of degree n in b_hat(xi) near D, with Mobius pieces A(X) in the white noise, |A(X)| <= C p^n exp(-kappa |X|) with the tails of the chart. Then, uniformly in the volume,

    | E_W[A] - E_nu[A] - Cov_nu(A, Psi) | <= C |D| p^n H_0^2,

when the fibre law is the regular chart. Proof. For complex z, s put H_(z, s)(X) := z H(X) + s A(X). The library allows complex activities and gives log Xi(z, s) = sum_Y H^#(Y; z, s), analytic in (z, s), with sum over Y meeting D bounded by C |D| c_0 on the polydisc |z| H_0 <= c_0 / 2, |s| C p^n <= c_0 / 2. The polymers not meeting D do not depend on s. E_W[A] = d_s log Xi at (1, 0). Its value at z = 0 is E_nu[A], and its z-derivative at z = 0 is Cov_nu(A, Psi). Cauchy in z and s for the second z-derivative gives the bound, once H_0 <= c_0 / 4. []

To get (c+), split Psi as in 4.6 there, Psi = -g^-2 R(b) + PP(b) + log JJ(b) + log FP(b).
- The third-order part of -g^-2 R is g Psi_3, homogeneous cubic in xi. The rest of it has polymers at most C(L, M, eps_0) g^2 p^4, by one more order in Cauchy in the display before (EI), since R_Lam vanishes to third order and is bounded on the polydisc.
- PP(b) is the variation of EE, which vanishes to second order at the flat field by colour. So its first-order term is at most C(L) |F^*| g p, and its second-order term at most C(L) g^2 p^2.
- log JJ and log FP are analytic and colour-covariant, so their linear term at flat W vanishes, and it is at most C(L) |F^*| g p at W. Their quadratic terms are at most C(L) g^2 p^2.

So Cov_nu(A, Psi) = g Cov_nu(A, Psi_3) + O(C(L) p^n (g^2 p^4 + g |F^*| p)). Replacing nu by the Gaussian costs exp(-p^2 / 2) p^n, and this is below any power of g, since 2 p_0 > 1. So (c+) follows with pi(g) = p^(n + 6) and rate C(L, M, eps_0) g^2 p^(n+6), in the regular chart.

What is not covered: the R sector of 4.7, rough cubes under regular W. A rough cube near D costs exp(-c_F eps_0 Y / g^2), below any power of g, but rough cubes far from D act as spectators, and their effect on A is what the gate's D6 asks about. I expect it to decay at the rate kappa / M from the gas form, and I did not write it.

The label for this route: I did not check (EI) itself, and I read 4.6 only at the level needed to write the split. See Requests.

**5.2 The one-step statement.** (OS_j) of `parts/upper-chain.md`, with the gate's repairs and:

- **(b+) Chart to second order.** For a gauge-covariant su(2)-valued function psi, smooth in V_j, with base point in D and bounded C^3 norm: psi(Phi(W, g xi)) = psi(V^*) + g (D psi)[xi] + g^2 (1/2) (D^2 psi)[xi, xi] + (the second-order term of the chart) + O(C(L) g^3 (1 + |xi|_loc)^3).
- **(c+) First-order local Gaussian limit.** For polynomials A of degree at most 8 in xi near D with bounded coefficients, uniformly in W on G and in the volume, | E_W[A] - E_0^W[A] - g Cov_0^W(A, Psi_3^W) | <= C(L) ( g^2 pi(g) + g |F^*|_(B(D, R)) ) + C(L) exp(-c R / L), where g Psi_3^W is the third-order Taylor term in xi of -g^-2 F_j(Phi(W, g xi)), and pi a power of log(1/g).
- **(d+) Continuity to first order.** Gamma(W), Psi_3^W and the quantities in (b+) are C^2 functions of the coarse field near flat W, with norms at most C(L), up to the tail C(L) exp(-c R / L). C^2 and not Lipschitz: term 2 in the proof of Theorem 5.3 needs the first derivative as a function, to identify the coefficient (hostile pass, item 7). The tail is the gate's D7. In hard-core--independent, where everything is analytic on the class in W, this is a consequence of the construction.
- **Uniform in j:** all constants uniform for j <= K - m_0, the gate's D8.
- **Moments.** All moments of X_p bounded at levels j, j + 1, with constants allowed to depend on L: Lemma 10.6, and the gate's D5 costs nothing here since L is fixed before g.

**Lemma 5.6 (first order on G, with far rough cells: the gate's D6 and D7).** [Implication. Derived at the level of each step below, given from hard-core--mapped, Text 5.3, "Theorem OS, local form": the split into Omega and Y, (H1)-(H3) in the ball at fixed data, the rarity (A1), the rarity of Omega near y', and (Loc_k). None of these is proved, and the mapped file labels them derived at the level of each term. Lemma 5.1 is used as stated.] Let W = V_(j+1) be class on B(D, 2 R) only, and arbitrary beyond, R := (C_0 / mu) log(1 / g_j) in level-j units, with C_0 large given L. Let V^*_loc be the classical minimiser on the fibre in the ball, with free boundary, H_* its Hessian in the chart and R_3^* the cubic term. For a bounded function f of V_j near D that is a polynomial in xi to the order used,

    | E_W[f] - E_(N(0, H_*^-1))[f] + g Cov(f, R_3^*) | <= C(L) g^2,

uniformly in W beyond the ball. So (c+) holds with its tail replaced by g^4, on the event G with radius R(g). The cost of the larger radius is nothing: P(G^c) <= C R(g)^4 (g^2 / eps_1^2)^n for every n.

Proof. *Step 1, the mixture, exact.* By the local form, the fibre law of V_j given W is an average over omega := V_j on Omega, whose law mu nothing is asked about, then over the site data d of the gas in Y, then over the exterior variables xi of the chart at fixed (omega, d). The mixture is only used through this order of conditioning.

*Step 2, rare near events.* Let N_r be the event that Omega or a site of d comes within r of D, r := R / 2. By the chain peeling in the local form, the mass of Omega near D is at most exp(-c x T_2^2 (d' - r) L / d_0). By (A1) at fixed omega, a site near D has conditional probability at most C r^4 z, z = exp(-c x T^2 + C log x). Since |f| is bounded, this costs less than any power of g.

*Step 3, one log-concave law.* Off N_r, at fixed (omega, d), the exterior law is uniformly log-concave with a cut independent of W, (H1), with bounds (H2). Take the chart at the exact reference U^ref(omega, d), which is critical among variations on the exterior, so the linear term is absent. Lemma 5.1 applies with the g-refined (H2). So E[f | omega, d] = E_(N(0, H^-1))[f] - g Cov(f, R_3) + O(C(L) g^2), with H, R_3 at U^ref(omega, d).

*Step 4, locality.* Off N_r, the fields near D are class, and U^ref differs from V^*_loc near D by the classical response: at most C T exp(-delta r), plus the mean-field shift x exp(-mu r) of (Loc_k). So the Hessians agree near D up to C(L)(T exp(-delta r) + x exp(-mu r)). The propagators are exponentially local at fixed data, (J) of the library, with rate delta_0(L) independent of the size of the exterior. So H^-1 and H_*^-1 near D differ by at most C(L) (T exp(-delta r) + x exp(-mu r) + exp(-delta_0 r)), and the same for the first-order term, since R_3 is a sum of local terms with decay. With C_0 large this is at most C(L) g^4.

*Step 5, average.* The right side no longer depends on (omega, d), so averaging over them is trivial. No property of mu is used beyond Step 2. []

So on the route of hard-core--mapped, D6 and D7 are not new estimates. A far rough region only enters through the law mu, and nothing is read from it. The price is that R must grow like log(1 / g), and this is what the gate proposed for D7. (d+) follows on this route from (H2) by differentiating H_* in W through V^*_loc: C^2, with norms C(L). I did not write the derivative count. On hard-core--independent, the analogue is Lemma 5.1' with the region tails of I(k)(b) and the gas of 4.7, which I have not checked; the request stands.

**Lemma 5.2 (tree consistency).** [Derived.] Let F_(j+1)(W) = F_j(V^*(W)) = min over the fibre of F_j, as in hard-core--independent 3.2, on small fields. Let psi_1, psi_2, psi_3 be smooth, gauge-covariant, with base point o. Then the tree coefficient of (1/4) eps_abc psi_1^a psi_2^b psi_3^c under exp(-x F_j) is (1/4) eps_abc d^3 w_j / d tau_1^a d tau_2^b d tau_3^c at tau = 0, where w_j(tau) := min_V [ F_j(V) - sum_i tau_i . psi_i(V) ], and w_j(tau) = min_W min_(V in fibre(W)) [ ... ]. Thus the coefficient at level j is the same as the coefficient of psi o M for the Wilson action at level 0. In particular, the sum of the terms "fibre", "mixed" and "coarse" in a one-step expansion of it is exactly the coefficient at level j.

Proof. The third connected tree correlator of the psi_i is the third derivative of the minimum, by the Laplace expansion with sources tau / x, since (H + gauge fixing) is nondegenerate after gauge fixing and everything is gauge covariant. The minimum over V is the iterated minimum. Since mean values of psi_i at tau = 0 vanish, the connected and full third moments agree at this order. []

**Theorem 5.3 (the odd test to order g^4; implication).** [Derived given (FF), (OS_j) with (b+), (c+), (d+) for all j <= K - m_0, and the flow in the form x_j / x_(j+1) -> 1 as x_j -> infinity, by (T1)-(T3) of hard-core--independent 8.4.] Fix L. Let psi_1, psi_2, psi_3 be gauge-covariant functions in a class 𝔇_j of functions of V_j in a ball of bounded radius, with bounded C^3 norm and vanishing at flat fields. Then

    | E[(1/4) psi_1 . psi_2 x psi_3] / g_j^4 - K^(j)[psi] | <= C(L) g_j pi(g_j) + 2^(-(K - m_0 - j)) C / g_(K - m_0),

where K^(j)[psi] is the tree coefficient of Lemma 5.2. So along the trajectory, at fixed level distance m = K - j and i -> infinity, the limit of g_j^-4 <T> is within C(L) g_j pi(g_j) of K^(j)[psi].

Proof. Let eps_j be the sup over 𝔇_j of the left side. In one step, condition on W = V_(j+1), on the event G. The complement of G costs less than any power of g_j, by the moments (and here Chebyshev with high moments is used: the second moment, as in Theorem 10.7, gives g^4 and would not be enough). On G expand by (b+), and apply (c+). The terms are:
1. (1/4) eps psi_1^* psi_2^* psi_3^*, with psi_i^* := psi_i(V^*(W)). This is a function of W only. By the lift bound (a), |D psi_i^*| <= C_s L^(-kappa) in the sense of the first derivative of psi_i o V^*, so psi_i^* / (C_s L^(-kappa)) is in 𝔇_(j+1), for a class with C^3 norm allowed to depend on L. Hence its mean is C_s^3 L^(-3 kappa) g_(j+1)^4 (K^(j+1) + O(eps_(j+1))).
2. g^2 (1/4) eps psi_1^* Gamma_23^bc(W) and its cyclic images, with Gamma^bc := Cov_0^W(D psi_2^b, D psi_3^c). At flat W this is symmetric in b, c and the term vanishes. By (d+) it is C(L) |F^*| |psi^*|, and its mean is of order g^4, evaluated by the local Gaussian limit at level j + 1, with error o(g^4).
3. g^3 [ (1/4) eps E_0(q_1 b_2 b_3) + cyclic ] + g^4 Cov_0((1/4) eps b_1 b_2 b_3, Psi_3^W), with b_i := D psi_i [xi] and q_i the second-order term. At W = 1 this is the fibre coefficient, and by (d+) its dependence on W costs C(L) E |F^*| <= C(L) g.
4. All other terms are at least g^5 C(L) polynomially in psi^* / g, by moments.

By Lemma 5.2 the sum of the coefficients in 1, 2, 3 at x_j = x_(j+1) is K^(j). The difference between g_j and g_(j+1) costs C(L) g^2. So eps_j <= C_s^3 L^(-3 kappa) (g_(j+1) / g_j)^4 eps_(j+1) + C(L) g_j pi(g_j). For L large, the first factor is at most 1/2. At j = K - m_0 use the a priori bound eps <= C / g, from E|psi|^3 <= C g^3. Iterate. []

Remark. Since all L-dependent constants are multiplied by a positive power of g, no L-free constant is demanded here. An earlier version of this argument bounded the terms in 1, 2 instead of evaluating them, and needed a first variation of Gamma free of L. Going to g -> 0 at fixed L removes that.

**5.3 The rectangle at level j.** Let T_j^(k) be the rectangle functions of Text 3 with level-j plaquettes, with base point and tails at level j.

**Lemma 5.4 (the rectangle at level j; implication).** [Derived at the level of each step below, given that M is gauge covariant, strictly local, covariant under the lattice symmetries including reflections in planes through the centres of level-j cells, with linearisation acting componentwise up to a gradient, of bounded mass; hard-core--independent 3.3(d), Lemma 4.5a, 5.1. For L odd these planes are lattice planes of the fine lattice.] With K^(j) the tree coefficient,

    | sum_k K^(j)(T_j^(k)) / P_k^(j) | <= C_D |x|^-5 + C D^-1 |x|^-4,   while   Flux^(j) = D^2 P^Maxwell_(34,34)(x) (1 + O(1 / D) + O(D / |x|)),

in level-j units, and P_k^(j) = (1 + O(D^-2)) / (pi^2 D^4), uniformly in j and L.

Proof. By Lemma 5.2 the coefficient is computed at level 0, with sources the blocked currents J_i^(j) = Q^T J_i, conserved, of bounded mass and support within a bounded number of level-j cells, and with E_i := G J_i^(j) on the fine lattice. It has the form 12 sum_p V_p - 12 sum_cyc A~_k, where A~_k is the antisymmetric form from the second-order part of psi_k o M^j. The gauge covariance of M gives A~_k(E, d_0 theta) = 2 theta(o) <J_k, E> - 2 <J_k, theta_bar E>, which is all that the proof of 2.2 uses. So 2.2 and (3.2) hold, with theta_bar now a mean of theta against the blocked current's weights. By the componentwise linearisation, E_k lies along directions 1, 2 and e along 3, 4, so P_(3,k) = 0. The term A~_(l_3)(E_k, E_(k+1)) is at most C |x|^-6: the two fields are of size |x|^-3 there. Lemma 3.3 gives |E_k(z)| <= C |z|^-3, with an expansion around the dipole with relative error 1 / |z|, in level-j units, uniformly in j.

Rotation covariance about the axis of l(y_(k+1)) gives, near that plaquette and in plane coordinates xi around its centre, E_k = (P_k^(j) / 2) (xi_1 d xi_2 - xi_2 d xi_1) + O(D^-6 |xi|^3). The 180 degree rotation removes all terms xi^n d xi with n even, and the coefficient of order n is at most C D^(-3-n) by Lemma 3.3. So A~_(l(y_(k+1)))(e, E_k) = (P_k^(j) / 4) Theta~(e; y_(k+1)) + O(D^-6 |e|_(near)), with Theta~ a linear functional that does not depend on k. The Theta~ terms telescope around the square, as in 3.2. Evaluate the error in the gauge where |e| <= C D |x|^-4 near the square, which Lemma 2.2 allows. The error is at most C D^-5 |x|^-4 per edge, and after dividing by P_k, of size D^-4, it is C D^-1 |x|^-4 in the sum, against the main term of size D^2 |x|^-4.

Steps 1 and 2 of Lemma 3.4 use reflections and Lemma 3.3 only. []

So with D large and absolute and |x| large against D^3, the rectangle sum on the Wilson side is small against 24 |Flux|, at each level and uniformly in L. The statement to be consumed is that the ratio is at most 1/4 on average over a shell.

**Check at level 1 for one simple map** (`checks/witness_block_tree.py`, criteria written first). The map is L = 3, normalise( w_0 U_straight + w_1 sum of the six height-1 staples ), which is not the hard core's map. The tree coefficient is computed exactly from the second-order form A~ on the fine lattice T = 36. B1: K^(1) is unchanged under a random fine gauge shift of E_3, while K_comp moves: the second-order form and Lemma 5.4's use of Ward are right. B2: the (1,2) and (3,4) blocked plaquette currents decouple exactly. B3 passes: at coarse D = 1, |Stk^(1)| / 24 |Flux^(1)| = 2.14, 1.29, 0.84, 0.51 at R = 2, 3, 4, 5, decreasing. B4 as first written failed, ratio 34 against level 0, because the criterion compared unit plaquettes with 3 x 3 loops at D = 1; that criterion was badly posed and is kept in the script as written. The replacement B4', at coarse D = 3, compares w_0 = 0.4 with straight fine loops of the same size: the ratio of Stk is 1.001 and of Flux 1.000 at R = 4 and 5, with P_k equal to five digits, so the sum does not depend on this map at D = 3.

The ratios from all sizes lie on one curve in R / D: 0.75 at 1.33, 0.54 at 1.67, 0.48 at 2, 0.36 at 2.67, 0.22 at 4, 0.13 at 5.33 (torus effects at the last). That fits a continuum scaling form, with Stk_W of order D^3 / R^5 against 24 Flux of order D^2 / R^4. So the size asked of the rectangle is R / D >= 4 for a ratio near 1/4, not R large against D^3, which is what the proof gives. Observed, not proved.

**Monte Carlo of the rectangle on blocked links.** (`checks/witness_mc_block.py`, criteria written first.) Fine torus 12^4 at beta = 16, heat bath, blocked with L = 3, w_0 = 0.4, then the rectangle D = 1, R = 2 on the coarse links, averaged over fine translations and 6 axis permutations; 3 runs of 1000 configurations, statistically independent. Against that, a Gaussian potential on the coarse links with the blocked covariance. In units of beta^2 sum_k <T^(k)> / P_k:

| | run 1 | run 2 | run 3 | mean | tree prediction |
|---|---|---|---|---|---|
| blocked Wilson | +0.191(100) | +0.236(108) | +0.321(129) | +0.249(65) | +0.203 |
| Gaussian on coarse links | -0.082(82) | -0.111(66) | -0.144(54) | -0.113(40) | -0.200 |

L1 passes: the blocked Wilson value agrees with Stk_total^(1), 0.7 sigma, so Lemma 5.2 and the form A~ hold in the actual law at level 1. L3 passes: 2.2 sigma. L2 is resolved and passes: the predictions differ by 6.2 standard errors of the Wilson run, and the two measured values by 4.8 of the difference. **So the sign difference between a blocked Wilson field and a Gaussian potential on the same blocked links is seen at beta = 16, at one coarse level.** Only that map and that size; the Gaussian value sits below its tree value at 2.2 sigma, and I did not try to resolve that.

**Theorem 5.5 (NT2 at a fixed physical scale; implication).** [Derived given Theorems 3.5, 3.10, 4.3, 5.3, Lemma 5.4 and the hypotheses of 5.3.] Let the trajectory have g_(K - m) -> 0 as m -> infinity. Fix kappa_hat_0, A. There is m_0 and a finite family 𝔉 of bounded gauge-invariant functions of V^(r), r = a_(K - m), such that for every m >= m_0, the limit state omega at scale r differs from every centred Gaussian potential at level K - m in either of the following classes, on 𝔉, by at least eps g_r^(deg f).

- (i) Covariance invariant under lattice translations, link variance at most kappa_hat_0 g_r^2, any colour structure, no other condition. Here 𝔉 is given by compactness.
- (ii) Covariance invariant under the rotation about a plaquette axis, not necessarily under translations, link variance at most kappa_hat_0 g_r^2, with (B). Here 𝔉 is explicit: the pair functions and the rectangle functions T^(k) of Text 3.

The difference is the three-gluon vertex, in the sense of (3.3) and Lemma 3.4, and it is of order g_r^4 against values of order g_r^4.

Proof. For (ii), Theorem 3.5 at the level-j lattice, with W_g replaced by the values of Theorems 4.3 and 5.3, and Lemma 5.4 in place of Lemma 3.4. For (i), Theorem 3.10, with the same replacement. []

**5.4 Flux class.** On F, <T> = 0, and <T s_q>_c = 0 exactly. Since F is not a law on connections (multiplicativity W_(Gamma Gamma') = W_Gamma W_(Gamma') fails for the Gaussian b), it is separated from any connection law already by the group law. So T on F is a true but cheap test, and it is the class G that carries the force of NT2. Part of K_total on a given triple is also kinematic: replacing a tail by another with the same ends changes T by a universal term -24 P_12 Flux(lambda) on G and on the Wilson weight alike, by (2.1). This is why the test of Text 3 is a closed sum and not a single T.

### 6. The gate's D1 to D3, checked; other leads; the wording of NT2

**D1.** Checked by hand, not re-run. Reversal of axis mu sends sigma_1 to -sigma_1 on the mu links, which is conjugation by i sigma_2, under which sigma_2 is fixed, so gauge-invariant functions are unchanged and Theta F . F = |F|^2 pointwise. Right. Theorem 4.1 excludes that law, and so does the rectangle test: on it, far correlators do not decay, and its plaquettes in other planes are trivial, so T vanishes on the corner cluster, which already disagrees with K_total.

**D2.** Right, with one correction. The main term of Theorem 10.7 is the value on F: there is no vertex in it. (NF1) is kinematic. The repair written there, that T vanishes on a symmetric Gaussian, holds on F and is false on G (2.4). So relative order g is a statement against F, and against G only in the closed sum of Text 3.

**D3.** Right. I did not find anything to add. The trajectory here is the hard core's, not the one of Proposition 10.3, so Theorem 5.5 does not rest on it.

**Other leads.** Deviations at relative order g^2: at that order the expansion of the Gaussian law itself competes, Q^2 and the order-4 terms of s_p, and the Gaussian class has more freedom, so I see no gain over order g, and the demand on the hard core would be o(g^2) with the second-order term evaluated. An area-type bound on large loops needs control above a_K, which the hard core does not offer. Running of the coupling, (NF2): separated from RP Gaussian vector fields by the Kallen-Lehmann argument of the gate. On G it is weaker, since the potential covariance need not be reflection positive when only gauge-invariant functions are. The test of Text 3 does not use the flow at all beyond g_r -> 0.

**Proposed wording of NT2 (for the target lead).**

> **NT2, interaction.** For every small scale r there is a finite family F_r of bounded gauge-invariant functions of the coarse field at scale r, of one shape for all r, such that, for every centred Gaussian potential on the level-r lattice in a class stated with the theorem, some f in F_r has a different value in the limit. The order of quantifiers is: the family first, then the law, then the member. A single correlator chosen before the law cannot serve, by Proposition 1.1. A Gaussian potential on a finer lattice is tested at its own scale.

The last sentence is needed, not cosmetic. At one fixed scale rough gauge modes at finer scales have a rank per coarse cell that grows with the block volume (Text 3.12, route 2), so a fixed family cannot be expected to exclude them. Every Gaussian potential on a lattice has an own scale, and there the theorems apply. A Gaussian field with no lattice has no path-ordered holonomies to compare.

The class stated with Theorem 5.5 is the union of (i) and (ii) there; Theorem 3.19 would add class (iii), all c tensor 1_3 with c_bb <= kappa_hat_0, given (RANK-U). What it does not yet reach at level j is in the Obligations: covariances with no symmetry (done at the Wilson lattice scale for colour-isotropic c, Theorem 3.16), colour mixing with no symmetry, and link variance above g_r^(4/3). In d = 2 this statement is false, as it must be (Proposition 1.2).

### 7. Hostile pass at this stop

I attacked the newest steps.

1. *Is K_total an artefact of forward plaquettes?* The corner cluster breaks reflections, so K_total includes lattice terms. It does not matter for the value: Monte Carlo confirms the number for this exact function. But it means K_total at the corner has no continuum meaning, and the separated Text 3 is what is universal. Conclusion recorded in 5.4.
2. *Is K_vert the vertex or a gauge artefact?* By itself it is gauge dependent. In covariant gauges it does not change, because E_i does not, and in the identity check the far-flux coefficient is -24 exactly whatever the gauge. The gauge-invariant statement is Stk_W = O(|x|^-5) against -24 Flux on G.
3. *Could a symmetric Gaussian law cancel -24 Flux through the far term of (3.1)?* A_(l_3)(E_k, E_(k+1)) is the only freedom left. A cancellation for a fixed far loop would need |E_k| of size |x|^-2 at that loop. The averaging over a shell with (B) is what excludes it. Without (B) I do not exclude it for rotation-symmetric covariances that are not translation invariant. Example: a covariance with long-range correlation between near fluxes and far gradients. (B) is an assumption on class (ii), and it is named as such. Class (i) does not need it.
3'. *With no symmetry, can the rectangle sum alone be passed?* Yes, on paper: the rectangle family does not exclude covariances with no symmetry. Let the far field have a gauge part with in-plane gradient, theta = x_1 theta_0(y), so e_1 = theta_0(y) on the in-plane links; and let the near fields have a gradient part with dipole 2 P_(y y') along direction 1 on l(y). Then the local terms of (3.1) cancel 2 e(sigma) P for that in-plane position. This needs a dipole growing with x_1 at other in-plane positions, unless theta oscillates in x_1 at the lattice scale, which keeps it bounded. I did not construct a positive C that does this on all tests. So class (ii) really uses the rotation symmetry, and any theorem without symmetry must use more than the rectangle: Theorem 3.8 uses all triples, and it needs translation invariance.
4. *Lemma 3.1 at fixed n and g -> 0.* The constant C_n grows with the length of the tails, and tails of length R occur, so g must be small after R. That is the order used.
5. *Is the Laplace expansion on Z^4 legitimate?* Not as a theorem at fixed beta in infinite volume. Proposition 2.1 is rigorous on a contractible box. On Z^4 I use K_total only as a defined number (absolutely convergent sums), and 5.3 obtains it at level j from the hard core's statements, not from Laplace in infinite volume. Torus: flat moduli change the propagator at long distance. The Monte Carlo at T = 8 includes them, and it agrees at the local cluster within 0.5%. At level j the gate's D7 is the corresponding warning, and it is a tail in (d+).
6. *Lemma 5.1.* The third cumulant bound uses Step 4 and (C) of the library, with r_x of polynomial growth. (F) in the library is for D_v^beta S; here the r_x play that role, with the bounds assumed in the statement, so nothing beyond (M) is used. Removing the cut: Step 2 of Lemma 10.9 runs at tau = 1 with the Gaussian measure as the end point; I treated E_0 and Cov_0 with and without cut as differing by exp(-c rho^2), which is the same computation with A replaced by A R_3 terms and a sum over cells. I believe this and did not write it in full. Recorded as a gap below, small.
7. *Theorem 5.3, the order-of-limits trap.* If C_s were not free of L, the recursion would not contract. (a) states C_s free of L, and it is checked on neither file at the level needed here: Lemma 10.1 of hard-core--independent gives it for the abelian perfect form. Recorded. Also, the proof says term 2 is "evaluated by the local Gaussian limit at level j + 1". That needs only rate o(1), and it is Theorem 10.7's mechanism, but with functions that depend on W through Gamma(W): their first-order expansion in F^* is what (d+) must supply as a function, not only as a bound. As written (d+) says Lipschitz, which is not enough to identify the coefficient as in Lemma 5.2. It is enough if Gamma(W) is C^1 in W near flat with a C(L) modulus. **This is a weakness in what I wrote. (d+) should read C^2, or analytic, in the coarse field near flat. The independent file has analyticity on the class.** Corrected in Requests.
8. *Lemma 5.4.* Stated uniformly in j and L, with the rotation about the axis of a level-j plaquette acting on the fine lattice. For L odd the centre of a level-j cell is a centre of a fine cell, so the rotation is a lattice symmetry of the fine lattice. The field-chosen base point of hard-core--independent 5.4 must commute with it. Claimed there (3.3(d)), not checked by me. The gate says the same.
9. *Does the test work in every dimension?* Theorem 3.5 holds in every d >= 4, at tree level, on Wilson tree values, and fails in d = 2 because the flux is zero. So by itself it is not the part of the argument that knows d = 4. The input that does is UV stability at fixed coupling. So the charter's warning does not bite on 3.5, which uses the actual weight through its vertex, but one should not read 3.5 as a statement about the existence of anything. It says: if the hard core holds, the limit has the vertex.
10. *Could the test be passed by a non-Gaussian free theory?* It is not asked to exclude all free theories. A generalized free field with non-Gaussian law of the potential is not a Gaussian law. A test of a Ward identity would pass for any gauge-invariant local action. That is: this NT2 test certifies that the limit is not a function of a Gaussian potential, not that it is Yang-Mills. Identifying the coefficient K^(j) in fact does the latter at the level of the tree coefficient.
11. *Theorem 3.8: is the term with h_3 really gone?* h_3 can be large near k^3 = 0, up to rho_ac^(1/2) / khat_3^2, so any term with it could beat 1 / khat_3^2. It enters in (3.4) through t_3 and through a(h_2, h_3) lam_1, a(h_3, h_1) lam_2. These vanish exactly on the chosen v_3 in ker t_3, v_1 in ker lam_1, v_2 in ker lam_2. This is why the proof restricts v_1, v_2 to S^0 and not because of the size of lam. Stands.
12. *Theorem 3.8: is positivity used?* Only in Lemma 3.7, to make h a function and not a measure. If C is merely a bounded translation-invariant kernel, the symbol could be singular, and a singular gauge part could correlate with the fluxes. A Gaussian law has a positive covariance, so this is no restriction.
13. *Theorem 3.10 at small momenta.* The soft limit formula was checked at level 0 by comparing with the explicit form. At level j it rests on differentiating Ward in k^3, which I did not write term by term. Its proof must also control a form^(j)(u_1, u_2, u_3) minus its soft limit, of order khat_3 times the C^1 norm of the symbol, as k^3 -> 0. That is the hypothesis stated, unchecked against I(k)(a).
14. *Lemma 5.4 against the check.* B3 is for coarse D = 1, where the proof gives nothing, and it passes for R >= 5 only, with a torus T_c = 12. The trend with R is the content, not the value. B4' uses a map whose linearisation is close to straight lines, so it is a weak test of independence of the map. A map with a large block average, like the hard core's, is not tested.
15. *Does anything here know the coupling flows?* Theorem 3.5, 3.8 and the rectangle compare at a fixed scale, and use the flow only for g_r -> 0. A scale-invariant interacting theory with small coupling would pass too. So NT2 as proved is "not a Gaussian potential", with the vertex, not "asymptotically free".
16. *A slip in my procedure.* `checks/witness_vertex_form.py` ran for about a second outside the numeric lock while another of my jobs held it. No effect on the numbers.
17. *Lemma 5.6, Step 4.* The propagator's rate delta_0 may be as small as c / L, and T as small as eps_0, so C_0 in R = (C_0 / mu) log(1 / g) depends on L and on T. That is allowed: R enters only through P(G^c) and the tail, and g is small after L. But it means that the ball is large in level-j units at small g, and that the local objects H_*, R_3^* must be well defined on a ball of radius growing with log(1 / g). The file hard-core--mapped says this needs d' polylogarithmic for the collective term, and it allows that. Stands, at the level of a reading of its statements.
18. *Lemma 5.6, Step 3.* It uses the exact reference U^ref, so that there is no linear term. If U^ref near D were not close to V^*_loc, for instance if the sites in the ball shift the minimiser by more than the tail, Step 4 fails. The bound is the classical response in the class, (J), at distance r from the sites, and Step 2 removes sites within r. This reads (H3) at d >= d_x. I did not derive the response bound.
19. *The search (E3).* It is on random sparse plaquettes on a torus T = 12, so periodic images enter V_0 and P; all starts are Gaussian random with small scale, and a far-out solution with large m, y would be missed. The residual growing with N is what I rely on, not its value. Nothing here excludes a law where X is large. A value of r that is small but positive at N = 30 also means that any finite-family theorem with no symmetry would have a small margin.
20. *Failed route 3.* The locked assignment is at leading order, and it was not tested numerically. A covariance with those entries exists by taking the gauge block large, but then link variance is not O(g^2) unless the entries are of Feynman size, which they are. I did not write this C down in closed form.
21. *Theorem 3.16: is K_total - K_comp[c] really trilinear on currents?* K_comp alone is not, because of tails. The difference is, since it equals 24 VV on fields E + d_0 th with th linear in the current. If tails differ between tests, K_total and K_comp change together (2.2). No correction.
22. *Lemma 3.13: the cut-off.* Y(y) is known only on R_1. **V** reads only values on the supports of the H y_j, all on links of R_1, by the Ward identity. I checked the case of th vanishing on R_1 with both endpoints of a link inside: thetabar = 0 there. No correction. The Ward identity for decaying th, used to pass from E_i to y_i, has boundary terms of size |x|^3 |x|^-2 |x|^-3 |x|^-4, which vanish.
23. *Lemma 3.14: conjugation on a box.* D is a function on links, finite box, no wrap, so conjugation is well defined. On a torus the argument fails by a boundary slice, and all statements are on boxes. The limit is lower semicontinuity of rank. I also checked by machine that rank B >= rank C_+ >= the formula in all 48 choices in seven gauges.
24. *Lemma 3.15: "finitely many hyperplanes" includes the requirement that b exists with generic flux in S.* Yes: y_b is any element of W_0, and S is a graph over W_0. No correction. But the proof does not apply to far sources, whose flux is nearly uniform and not generic. This is why the near-source form of **V** is used, and why the far-source form in 3.14 needs its own argument.
25. *The count Ob <= 9 R.* A first attempt divided the budget between means and corners as if independent, which is false: a mean is a difference of corner sums. The graph form treats both as edges of one graph. Machine: Ob is far below 9 R in all gauges tried, so the count is crude and not tight.
26. *Theorem 3.17.* The boundary terms in "elements of S with no flux" are estimated, not written out: I take the loss to be of order L^3 against the margin 0.238 L^4. A hostile reader should check dim(S intersect the no-flux fields) against the boundary sites of R_0. This is why L is stated as large, with 150 only as the leading count.
27. *What was wrong in this stint.* (a) My prediction M2 (rank 4 at t = 0 in `checks/witness_rank_moment.py`) was wrong as stated, since that t is not Fock. Its first run gave rank 5, and rank 2 for simple F. (b) My hand formula for the current of two fields had a sign error. Correct: J2_nu = -(d . A') A_nu + (d . A) A'_nu - A' . d_nu A + A . d_nu A' + 2 F'_mu_nu A_mu - 2 F_mu_nu A'_mu; in Fock gauge J2 = (3/4) [F, F'] x. The factor 2 is the spin term. Lattice check by hand on A = x_0 e_1, A' = x_1 e_2: 2 x_0 on 2-links, as the formula says. (c) The first adversary of `checks/witness_rank_vertex.py` was badly normalised. (d) A rank-4 far star against a rank-4 main term looked fatal for the two-box form of 3.14; with many cells the main term has growing rank, so it is not.
28. *Scope.* Theorems 3.16, 3.17 and Corollary 3.18 are about the Wilson tree values at the lattice scale. T1 needs level j. I must not read them as covering the limit. Theorem 5.5 is unchanged by them until 3.14 closes.
29. *Theorem 3.19, the corrections.* The rows of the matrix are small when |d_0 t| is large, like |F|^2 / |d_0 t|. The term from the bulk of the torus in VV(G J, G J', E_b) does not shrink with t: it is of size |F| D^-(d + 6) for J with moments vanishing to degree d. It is below the row only if D^(d + 2) is large against M, with M up to kappa_hat_0^(1/2) D^4 if the cells spread to the distance of b. So d >= 3 is needed and the family depends on kappa_hat_0. I estimated this, not proved it. Far-field non-uniformity of F across a cell enters at relative L_c / R, and the row is suppressed by the same mechanism only in part: `checks/witness_cross_cell.py` tests the leading term on real fields, Text 3.14.
30. *The test of (3.13).* I weakened nothing after seeing data in the registered criterion, which is reported as failed at L = 3. The L = 4 numbers are from the same job and are reported beside it, not in its place. A hostile reader should note that the error at L = 4 is near the threshold and that only 3 columns were kept.
