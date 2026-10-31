# Filled cubes and a relative bound on the exact density

Producer: `parts/hard-core--mapped.md`, Text 5. Status: labelled per statement. Not reviewed. Read Prop 8 first; Prop 3, Corollary 4 and Prop 7 are kept as a record of what failed or was superseded.

Credit: constrained minimal configurations and the block average are Balaban's. The relative bound, the cube rule and the crude gap are mine. Nothing here uses the account.

Consumers: rarity of sites (A1) in `library/polymer-covariance.md`; exterior coercivity in Theorem OS. This note replaces, for those consumers, the expansion in `library/critical-class-and-excess.md`, the exterior weight of (P_k) and the Jensen step of the earlier Prop R1.

## Numbers

Level-k units. A box is a level-(k+1) cell, L^4 level-k cells. Inputs from Text 5.3, items (R2), (R3): for V' with flux at most T_f,

- the reference U* = U_{k+1}(V') has energy at most C_s T_f^2 on a box;
- ||F(U*)||_{L^4(box)} <= C flux', in level-(k+1) units. So by Hoelder the energy of U* on a set of |Q| level-k cells is at most C |Q|^{1/2} L^-2 T_f^2.

Put T_c = a_*/L^2, K_0^2 = K-bar L, T_f = L T_c/(C_r K_0). Then the energy of U* on a cube of side l is at most C l^2 T_c^2/K_0^2, up to fixing C_r. Core: cells with flux above T_c. A core cell costs at least c_b T_c^2 in energy.

Let m_* := c_1 L, with c_1 chosen below.

## Lemma 1 (the cube rule). Proved here.

(a) *Dense boxes are dropped at a profit.* A box with at least m_* core cells has cost at least m_* c_b T_c^2, and the reference on it and its C_n neighbours has energy at most C_n C_s T_f^2 = C_n C_s L T_c^2/(C_r^2 K-bar). So the cost is at least twice the reference if c_1 c_b >= 2 C_n C_s/(C_r^2 K-bar).

(b) *Sparse boxes: bounding cubes.* Let a box have m < m_* core cells. Take the bounding cube of each connected cluster, and merge any two cubes at distance less than 2 into their bounding cube. The side of a merged cube is at most the sum of the sides plus 2, so the sum of the sides of the final cubes is at most 3 m. On the final cubes the reference has energy at most sum_i C l_i^2 T_c^2/K_0^2 <= C (3 m)^2 T_c^2/(K-bar L). This is at most (c_b/4) m T_c^2 if 9 C m_* <= (c_b/4) K-bar L, that is if 36 C c_1 <= c_b K-bar. Both conditions hold for K-bar large and c_1 = C'/K-bar, with C' absolute. Then the total side of the cubes in a box is at most 3 c_1 L, a small fraction of L.

Note that doubling, which would make the cubes grow exponentially, does not occur, because cubes merge only when they nearly touch.

(c) *Topology.* The complement in a box of disjoint closed cubes at mutual distance at least 2 is connected at the level of cells, and simply connected, since d = 4. Proof of connectivity: walk on a straight segment; on meeting a cube, walk on its boundary layer, which is connected, and which meets no other cube. Simple connectivity: each cube's boundary is a 3-sphere, and removing a ball from R^4 does not create a non-contractible loop.

So no membrane, no pocket and no isoperimetric statement is needed. An annulus of core cells is inside its bounding cube.

## Lemma 2 (crude exterior gap). Proved here, given Lemma 2 of the energy package on a cell.

Let Ext be a box minus the cubes of Lemma 1. Let H be a fine bond field on Ext, with weight rho the block average of a bond restricted to lines avoiding the cubes. In the gauge of the box, ||H||^2_Ext <= C L^8 ( ||grad H||^2_Ext + |<rho, H>|^2 ).

*Proof.* On each exterior cell c, the lattice Poincare inequality gives ||H - H_c||^2_{L^2(c)} <= C ||grad H||^2_{L^2(c)}, uniformly in eta. For adjacent cells, |H_c - H_c'|^2 <= C ||grad H||^2_{L^2(c u c')}. So the vector of averages is controlled by the Laplacian of the exterior cell graph. That graph is connected, with at most L^4 vertices, so its gap is at least c L^-8 by the standard path bound. At least half of the lines avoid the cubes, by the small total side, so rho has mass at least 1/2 on Ext. This ties the mean. QED

*Why L^8 is harmless.* The constants of the Laplace lemma may depend on L. They enter smallness conditions on a_* and on x_k^-1, in that order, after L. They do not enter the main contraction. T_f/T_c and the cost arithmetic depend only on ratios, so shrinking a_* with L changes nothing in Lemma 1. So the fine-level term |T| <= C a (||B||^2 + ...) is absorbed by taking a_* <= c L^-8. Sharp geometry is not needed.

Next to a dropped box. Bonds whose block meets a dropped box are not constraints on the exterior. For an exterior box that has lost its constraint in a direction, replace the constraint by conditioning on the local average of that component, treated as extra data. This restores coercivity box by box, with no chain and no cascade, at an entropy of order log x per such box, and there are at most C_n of them per dropped box.

## Prop 3 (relative bound). Implication: the induction step is derived given the inputs named.

For a level-k field V, let Y(V) be the cells with flux above T_f. Let V, V^flat be fields equal outside a set Hull, a union of cubes as in Lemma 1 with collar d_1, where V^flat is the minimiser over Hull of A_k given the outside, is class on Hull, and the outside is class within distance d_x of Hull. Let C be the cells of Hull with flux above T_c. Then

    (RP_k)  F_k(V) - F_k(V^flat) >= x_{k-1} ( c_b T_c^2 |C| - E_fill ) - C(L) (|Hull| + d_x^4 |C|) log x_k,

where E_fill is the energy of the fine reference on Hull and its boundary layer, at most (c_b/4) T_c^2 |C| when the outside lies near a class parent's lift. For k = 0 the same holds with x_0 and no entropy.

*Proof of the step.* Let I be the children of Hull^{+d_x}. Outside I the fibres of V and V^flat coincide, with the same chart. So e^{-F_k(V) + F_k(V^flat)} is at most the supremum, over all children xi outside I, of the ratio of the two inner integrals, I(V; xi)/I(V^flat; xi), since the ratio of two integrals with the same outer variables is at most the supremum of the ratio of integrands. No exterior integral is compared, no Gaussian normaliser is matched, and no exterior convexity is used. Both inner integrals are at level k-1, with the same vac_{k-1} on every cell.

*Denominator.* By (Loc_{k-1}) for class inner fields, and with xi at distance d_x L from Hull's children, the inner action is x_{k-1} A^I + (bounded local) + (tail). So I(V^flat; xi) >= exp(-x_{k-1} A^I_k(V^flat) - C |I|) (c/x)^{n/2}, by a Gaussian lower bound near the inner minimiser, using only the upper bound on the Hessian, x g^2 D^2 A <= C. Here n is the number of inner degrees of freedom.

*Numerator.* Sum over the set Y' of inner children above T_f. By (RP_{k-1}), a term with Y' is at most the term with the children filled, times prod e^{-c x T_f^2 + C log x}. Sums to a factor at most e. For class children the action is as in the denominator. So I(V; xi) <= exp(-x_{k-1} A^I_k(V) + C |I|) times int e^{-(x/2) (A^I - min)}. The integral is at most (C/x)^{n/2} by tree gauge and Haar invariance: non-tree bonds correspond to independent plaquettes, each factor being at most C x^{-3/2}. Half of the exponent is kept for this integrability, so c_b is replaced by c_b/2 in the end.

*Classical comparison (exterior-free).* A^I_k(V) >= A^{I minus Hull}_k(W) + A^{Hull}_k(V|Hull) >= A^{I minus Hull}_k(W) + c_b T_c^2 |C|, by dropping fine plaquettes between. And A^I_k(V^flat) <= A^{I minus Hull}_k(W) + E_fill, by an explicit extension of the outer minimiser into Hull, cone-filled from its boundary (the boundary is a union of 3-spheres, and the flux is small). So the difference is at least c_b T_c^2 |C| - E_fill.

*Vacuum.* The number of fluctuating degrees of freedom may differ by 3 per bond whose kernel is independent Haar, each such bond contributing x^{3/2}: an entropy of order log x per such bond. QED

## Corollary 4 (rarity). Implication from (RP_k).

For V' in D_{k+1}, family F, and gamma compatible with F: N_{F u gamma}/N_F <= z^{|gamma|}, z = exp(-c x_k tau^2 + C(L, d_x) log x_k), with core and amplitude-bad cells counted in |gamma|, uniformly in the rest.

*Proof.* Fix the exterior W and the data of F. Numerator: by (RP_k), rho_k(V) <= rho_k(V^flat(W)) exp(-cost + entropy) pointwise, and integrate over the hole with volume at most (C sqrt x)^{dim}. Denominator: for the same W, the hole variables within distance 1 of the minimiser give rho_k >= rho_k(V^flat(W)) e^{-C}, since F_k near V^flat is x_k A_k + R_k with Hessian at most C in B units. The ratio is therefore at most its supremum over W. The Gaussian normaliser of the exterior is not compared, because the exterior integral is the same on both sides and is not computed.

*The constraint.* Lines through core cells are excluded from the block average in the numerator, so W there satisfies exterior average = V'. In the denominator all lines count, so for the same W the hole lines must average to V' too, which is one more linear condition on the hole, at the cost of a volume factor x^{-C} per bond touching the hole. With that condition the same W is in the fibre, with no shift of the exterior. QED

For a cell in Y' (amplitude bad, no core nearby), the same argument applies with the cost coming from convexity: the action is exact, and c x tau^2 replaces the core cost.

## Prop 8: (RP'_k), a relative bound with the far field fixed and nothing dropped at its edge. Main line for rarity from here on.

Status: induction derived at the level of a sketch, labels below. Not reviewed. It supersedes Prop 3 and Prop 7 as the route to (A1), and if it holds, (P_k), R^E, the region theorem, Z_Ext, the shift map and exterior coercivity are not consumed by rarity. Lemma 1 (cubes), Lemma 5, Lemma 6 stay.

**Why Prop 3 failed and what changes.** H1: the edge of I. Keep the plaquettes to the far field in both numerator and denominator and compare them as one classical problem with Dirichlet data. Drop only the links to the hull. The atypical data next to the hole (failure 3 below) are then inside I, so they count in the numerator's energy.

**Classical object.** 𝔸_k(V) := the infimum of the fine energy A(U) over fine U from which V is reached by the kernel chain, levels 0 to k. On D_k, with lines not excluded, it is A_k(V). It is non-negative, and it is exact for the Markov kernel: a Haar parent is reachable only from fields that carry its excluded lines' cost. For a region, 𝔸_k(xi, V_I) has xi fixed on the outside.

**Statement (RP'_k).** Let I be a union of blocks at level k, xi level-k data outside I, class on the d_x neighbourhood of I. Let V_I be any data on I, and V^0_I data on I with (xi, V^0_I) class near I. Then

    F_k(xi, V_I) - F_k(xi, V^0_I) >= x_{k-1} ( 𝔸_k(xi, V_I) - 𝔸_k(xi, V^0_I) ) - C(L) |I| log x_k - tail,

uniformly in anything beyond the neighbourhood, including rough fields there. tail <= C x_k e^{-mu d_x} |boundary of I|.

Base k = 0: an equality, with no entropy. (Derived.)

**Step (derived as a sketch).** Children of I are J_0. Numerator and denominator are integrals over children with their parents V_I, V^0_I on I, and common parents xi outside.

*Adaptive region (this is what removes rough data at the edge).* For a child configuration, explore from J_0: J is J_0 together with every cluster at range d_x of children above T_f that touches it, repeatedly, plus collars d_x. Beyond J the children xi'' are class within d_x of J. The event {J, xi''} depends only on the children outside J and on J's boundary. So the numerator is sum_J integral over xi'' of N_J(xi''). For the same (J, xi''), let D_J(xi'') be the denominator's integral over class children on J. Each integral over xi'' of D_J(xi'') is a sub-integral of the denominator, with no overcount, since each J is compared with the full denominator separately. The extra clusters in J \ J_0 cost z^{|J \ J_0|} in the numerator, by (RP'_{k-1}) for them, and the number of J is at most c_a^{|J \ J_0|}. So the sum over J converges, with the factor z c_a << 1.

*Numerator at fixed (J, xi'').* On a child field W, apply (RP'_{k-1}) to its rough clusters only, each with a class fill on a tube (items (h), (i), (j) below), giving W^flat class. Then F_{k-1}(xi'', W) >= F_{k-1}(xi'', W^flat) + x_{k-2} (𝔸_{k-1}(W) - 𝔸_{k-1}(W^flat)) - entropy, paid by their own cost. On class fields, (Loc_{k-1}) applies on J, because xi'' is class within d_x of J: differences of F_{k-1} are x_{k-1} times differences of A_{k-1}^{J+} plus C per bond of J, by a path in the relative field, which stays in class because amplitudes are labelled small outside the cubes and T_f L^{2/3} is small in the cubes. Since x_{k-2} >= x_{k-1} and 𝔸_{k-1}(W) >= 𝔸_{k-1}(W^flat) - small (W^flat is the minimiser), the sum is at least x_{k-1} 𝔸_{k-1}(xi'', W) + common terms - C |J|. Integrate over Haar volume of the fibre: a factor (C(L))^{|J|}.

*Denominator at fixed (J, xi'').* Restrict to a ball of radius of order 1 in B units around the minimiser. Only the upper bound on the Hessian is used, with x g^2 = 1. So D_J >= exp(-x_{k-1} 𝔸_k(xi'', V^0) - common - C |J|) (c/x)^{n/2}.

*Divide.* The ratio is at most exp( -x_{k-1} [ inf_{fibre} 𝔸_{k-1}(xi'', W) - 𝔸_k(xi'', V^0) ] + C |J| log x ). The infimum over the fibre is 𝔸_k(xi'', V_I) by definition. Then replace xi'' by xi: the dependence on the boundary of a difference of two minima is a tail, by decay of the response in the class outside the hull, and a dropped-link lower bound in the numerator (below). J is at most a constant times |I| plus the part already paid. QED of the sketch.

**(A1) from (RP'_k).** At level k, fibre of V' in D_{k+1}, family F, site gamma. Let I be the blocks within d_x of the hull of gamma. Beyond I, up to d_0 - d_x, all fields are class by the labels, and rough fields of F lie beyond. Fix W_far. With V^0 the level-k data of U_D, the class minimiser on I with Dirichlet data W_far and parent V': N(I) <= Vol exp(-F_k(W_far, V^0)) exp(-x_{k-1} (𝔸_k(W_far, V_I) - 𝔸_k(W_far, V^0)) + C |I| log x), sup over labelled V_I; D(I) >= exp(-F_k(W_far, V^0)) (c/x)^{n/2} e^{-C |I|}, by (Loc_k) beyond the hull. So the ratio is z^{|gamma|} provided the classical inequality holds:

    (CI)  𝔸_k(W_far, V_I) - 𝔸_k(W_far, V^0) >= (c_b/4) T_c^2 |C|  for labelled V_I.

*Proof of (CI), from Lemmas 1, 5, 6 (derived at the linear level).* Numerator: drop the links to the hull only; keep the plaquettes to W_far. 𝔸_k >= A^Ext_restr(W_far) + c_b T_c^2 |C|. Denominator: A(U_D) = A^Ext(U_D) + A^{Hull+}(U_D). By Lemma 6 with U_D in place of U* (it uses only criticality of the reference, on I, with Dirichlet data, whose test fields vanish at the edge of I): A^Ext_restr(W_far) >= A^Ext(U_D) - G. So the difference is at least c_b T_c^2 |C| - G - E_D(Hull+). U_D differs from U* by a response to W_far at distance d_x, which decays, so E_D(Q^+) <= 2 E_ref(Q^+) + tail. Hence (CI) by the arithmetic of Lemma 6. In a labelled field, relative amplitudes on Ext are small and Ext inside I is simply connected, so the linear reading is the leading term. QED of the sketch.

No convex integral over a region with free boundary occurs. Theorem OS has site data fixed and retained plaquettes, so its exterior Hessian is the whole-lattice one with v extended by zero. (`library/curl-poincare-exterior.md` stays a dependency of (CI): see item (k) below.)

**Hostile check of Prop 8, recorded.** (a) Does it hold where the pointwise fill failed? Failure 3 says atypical data adjacent to a hole can favour the bad field. Here V^0 is chosen after xi, at distance d_x from the hole, and adjacent fields are in V_I, with energy counted. So I find no conflict. Test: take a V_I that is the bad field plus a matching atypical collar, with total energy below the class minimum. (CI) says this cannot happen for labelled collars, by Lemma 6. So Lemma 6 is what is being tested, and its linear reading is the unproved part. (b) A sup over rough xi far away is taken at level k. At level k-1 it is taken only beyond J, where the children are class within d_x. I checked that the events are measurable in the outside data, but not the overcount in the kernel's exclusion of lines. (c) `𝔸_k` with a Haar parent: if a parent is Haar, the children chain has carried m_* core cells. Then 𝔸_k >= c_1 L^{1/3} c_b T_c^2 per such parent, and the cost c_P T_f^2 of step 5 is restored, with c_P from c_1 c_b C_r^2 K-bar. Haar parents have no classical minimum dependence, so the fibre's infimum is over all children, which is fine for a lower bound. (d) x_{k-2} >= x_{k-1} needs the flow bounds, which are an input (Theorem P1). (e) The tail has x_k e^{-mu d_x}, so d_x >= (2 log x_k)/mu is needed; its growth with k enters only through entropy, |I| ~ d_x^4 per core cell. That is the same as in the file. (f) Not checked: J versus the block structure when d_x < L, where I is a block of size L and contains whole lines; and (Loc_{k-1}) up to the edge of J with data only class to depth d_x, where the tail is what the statement allows. (g) Is it too strong? d = 2 test, with a heat-kernel density: F_k(theta) ~ x_k theta^2 up to a power, and 𝔸_k = minimal energy holds with equality in the exponent. Consistent, with entropy log x. Not a test in d = 4.

**Second hostile pass on Prop 8 (recorded; it changes the step).**

(h) *Applying (RP'_{k-1}) to the whole of J is fatal.* It is one line, but the entropy then obeys E_k(I) = E_{k-1}(J) + ..., with |J| = L^4 |I|, which is the fine count (s_k/eta)^4 log x. So (RP'_{k-1}) may be used only on rough clusters, whose entropy must be paid, and class fields must be handled by (Loc_{k-1}) with C per bond of J, at this level only.

(i) *Inner reference, and failure 4 of the producer's list.* A rough cluster Gamma of children needs a class field W^flat equal to W beyond a neighbourhood. The bounding cube has volume m^4 and a Federer-Fleming filling has volume A^{3/2}. For a large cluster, either exceeds what x T_f^2 A can pay once A^{1/2} >> x. The producer recorded "for a large hole no small-flux filling need exist". That is false when thresholds are constants. A class exterior with holonomy alpha around a 2-sheet of Gamma is filled on a tube of transverse radius R_0 := (pi/T_f)^{1/2}: spread alpha over the transverse disc, with flux about alpha/R_0^2 <= T_f and, along the sheet, about |d alpha/ds| <= T_f R_0, divided by R_0. So X := Gamma^{+R_0} has volume at most C R_0^4 |Gamma|, a constant per rough cell, with no 3-chain. Status: construction described for a sheet; general shapes by the cell-complex trial of (R1) on X, where a loop on the boundary of X bounds in X or is free data. Not written. *This cannot work at thresholds of order g p(g), because R_0 would grow as the coupling falls; constant thresholds are what make it local.* In (RP'_{k-1}) take the rough threshold T_f/(2 C_a), so the fill is below T_f/2, and keep the formula up to T_f.

(j) *Who pays the entropy: first attempt, dropped.* E_{k-1}(X) = C (R_0 + d_x)^4 log x per rough cell cannot be taken as a fraction epsilon of x 𝔸 at each level, since the coefficient would degrade as (1 - epsilon)^k. A split into forced and unforced rough children, with unforced ones paid by an excess over the fibre's infimum, needs (CI) at a rough parent, which has no regularity to stand on. Both are replaced by the following.

**Lemma T (tower count). Proved here for the linear block average; the input is the flux bound below.** Let f := |F(U)| on the fine lattice, and for each level j let R_j be the level-j cells c, of side s_j, with s_j^-2 integral_c f >= T'. Then, for any region X,

    sum_j |R_j cap X| <= 8 ||f||^2_{L^2(X^+)} / T'^2,    with no dependence on the number of levels.

*Proof.* A cell has volume s^4, so sum_{c rough} 1 = integral sum_{c contains x, c rough} s_c^-4 dx. For x in a rough cell, let sigma(x) be the smallest side of a rough cell containing x. The sum over the larger cells containing x is geometric, so it is at most 2 sigma^-4. Rough at sigma says sigma^2 avg_c f >= T', so sigma^-4 <= (M f(x)/T')^2, with M the dyadic maximal function. Doob's inequality gives ||M f||^2 <= 4 ||f||^2. QED

*The flux bound.* A level-j plaquette angle in c is at most C s_j^-2 integral_{c^+} |F|: the composite weight obeys sup rho <= C (Lemma 1 of the energy package), and for a non-abelian field a holonomy is bounded by the integral of |F| over a spanning surface, averaged over the parallel surfaces of the block average. So flux above T_f gives c in R_j with T' = T_f/C, on the enlarged cell, with bounded overlap. Haar parents are charged to their excluded children, at a ratio L^-2 per level, which sums. Status: the bound for log-averages at rough fields, where lines through rough cells are excluded, is by the same surfaces and is not written out.

*What it says.* Nested rough cells cannot share energy without limit: a tower's count is bounded by the energy, however tall. A spike of energy E has only (1/2) log_L(E^{1/2}/T') rough ancestors. This replaces forced and unforced children and all reference to the waiting of rough parents.

**Accounting functional, from Lemma T.** Let 𝔹_k(V) := inf over chains from a fine U to V of [ A(U) - sum_{j<k} sigma_j |R_j(chain)| ], with sigma_j := E_j/x_j, E_j the entropy per rough cell at level j, about C (R_0 + d_x)^4 log x_j plus beta times a local energy. Since sup_j sigma_j -> small for x_j >= x_*(L), Lemma T gives 𝔹 >= A^far + (1/2) A^{near rough} on each chain. By (CI) at class parents at lower levels, a rough cell in a chain below a class parent adds excess at least c T_c^2 >> sigma, so 𝔹_k = 𝔸_k on the class. Then state (RP'_k) with 𝔹 in place of 𝔸, with coefficient x_k:

    F_k(xi, V_I) - F_k(xi, V^0_I) >= x_k ( 𝔹_k(xi, V_I) - 𝔹_k(xi, V^0_I) ) - C(L) |I| log x_k - tail.

*One step.* After the fill, x_{j+1} 𝔸(W^flat) + x_j [𝔹(W) - 𝔸(W^flat)] = x_{j+1} 𝔹(W) + beta_{j+1} [𝔹(W) - 𝔸(W^flat)]. The bracket is bounded below by minus the fill energy, at most C |X| T_f^2, and with one level's beta this is a constant per rough cell, which enters E_j. Entropy of rough cells at level j is the term -x_j sigma_j |R_j| inside the infimum. There is no factor (1 - epsilon) per level: it is one infimum over chains, with Lemma T applied once at the end. C(L) in the statement stays uniform, since each level adds only the C per bond of its own J, and rough clusters have entropy inside 𝔹.

(k) *Correction.* (CI) beyond the linear reading does consume curl-Poincaré: the cubic term and the constraint's second order are at most C(L) T_f ||H||^2, and ||H||^2 <= C_3(L) ||Omega||^2 needs Corollaries 3, 4 of `library/curl-poincare-exterior.md` in a tree adapted to the hole, with Omega := F(U) - F_D. C_3(L) T_f is absorbed by a_*(L). The earlier sentence that the rest of that note is not a dependency is wrong. On Ext, take U the fine minimiser given V_E, whose box energy is at most C a_*^2 by comparison with the trial, with links dropped so that the exterior and hull infima separate.

(k') *Non-abelian (CI), route now (labels per step).* Enlarge each hull by one cell for the classical bound only: Ext' is Ext minus its shell, and the shell plaquettes are dropped too. Then:

1. *Reduce to a regular exterior field (leaf).* In the infimum take U the fine minimiser given V_E on Ext. A labelled V_E has flux at most T_c, so the trial of (R1) gives energy at most C T_c^2 per level-k cell. Below a small absolute energy per cell a lattice Uhlenbeck gauge exists, with ||A||_{H^1(c)} <= C ||F||_{L^2(c^+)}. Frozen leaf `Lattice Uhlenbeck`, consumers: this step and uniqueness in (R2). Route: lattice Gaffney on a cube, an exact identity by reflection to a torus, and continuity in the field. Not written.
2. *Pointwise regularity: tried and dropped.* I first asked for (R4): R(C a_*) at U_D away from free boundaries, from the kernel bound |grad G| <= C/|x|^3 and a bounded source. It fails by a logarithm. At a background the residual contour sum at level j has coefficient a s_{j+1}^2 and weights w' <= 1 that are of order 1 near a block centre. So its contribution to grad H near such a centre is about lambda a L^2, independent of j. At nested block centres all levels add, which gives k lambda a L^2 at distance eta, and log_L(1/r) lambda a L^2 at distance r. This estimate is a scaling count, not a proof, but it removes the claim. It is harmless in L^p: Lemma 4 of the package bounds the same sum in the L^2 operator norm, so (R3) stands, since it uses only ||Q^{o*} lambda||_{L^2} <= C |lambda|. The word "bounded" in the producer's (R3) should be read in L^2.
3. *Relative field in L^4, box by box.* In each box, extend the relative field across the cubes by Lemma 5, and use `Lattice Uhlenbeck` for a Landau gauge, H_b relative to U_D, in which ||H_b||^2_{H^1(box)} <= C (1+l)^4 ||Omega||^2_{Ext' cap box}, in level-(k+1) units, given the small box energy of step 1.
4. *Expansion.* Per box, gauge invariantly, A_b(U) - A_b(U_D) = <F_D, d_{U_D} H_b>_b + <F_D, Q_2(H_b)>_b + (1/2) ||Omega||^2_b. The cubic term is at most ||F_D||_{L^4} ||H_b||^2_{L^{8/3}} <= C T_f (1+l)^4 ||Omega||_b^2, with T_f L^{4/3} small, by (R3) and Sobolev on a box. Overlaps of two boxes' gauges: H_b - H_b' = D_{U_D} omega + second order, and <F_D, d_{U_D} D_{U_D} omega> = <F_D, [F_D, omega]> = 0, so the linear term is gauge invariant at first order, and second-order corrections are absorbed in the same way. This gives one global linear term, to which Lemma 6 applies. The constraint's second-order term is at most C(L) T_f ||H||^2 by Step 4 of Theorem 7, with C_3(L) T_f small by a_*(L).

Status: a route with one named leaf, not a proof. No pointwise bound on U_D is used. Hostile note: the patching in step 4 is by a partition of unity at box scale, and its commutator with the constraint is the same one as in the IMS step of the producer. I have not written it.

(l) *What remains after this pass.* Non-abelian (CI) at class parents; the general trial on X; the flux bound at rough fields; the event structure of J against the kernel's exclusion of lines; (R3) as an input. I have no counterexample.

## Hostile check of Prop 3 (recorded; it damages the proof above)

H1. *The proof of Prop 3 as written is wrong at the outer edge of I.* The supremum runs over all xi, including rough xi adjacent to I. Next to rough xi, (Loc_{k-1}) gives nothing, so the denominator's formula "x A^I + bounded local + tail" is unavailable there. Even for class xi, the plaquettes across the boundary of I cost x (flux)^2 per plaquette. The denominator carries them, and the numerator's upper bound drops them, so bounding the two integrals separately leaves x T_f^2 |boundary of I|, larger than the cost. The interface is common to both integrals and must be cancelled by comparing them, not by bounding each. So the sentence "no exterior convexity is used" is false, and Prop 3 is NOT proved. Lemma 1 and Lemma 2 are untouched.

H2. *Corollary 4, "the constraint".* Numerator and denominator have the same W only if the hole lines average to V' in the denominator, but the same W with a different hole would need the same average on lines that straddle the hole and the exterior. This was asserted, not derived. Open.

H3. *Lemma 2, "uniformly in eta".* The cell-wise Poincare inequality is for scalar-like components in a fixed gauge. The Hessian controls curl energy and the gauge choice, not the full gradient, at a free boundary (finding F1 of the producer). So Lemma 2 controls ||grad H||, which is not what the action supplies near the cubes. See the curl form in the producer.

## Earlier repair: rarity through (P_k), with polynomial extension constants

Superseded as a route by Prop 8; Lemmas 5, 6 and the thresholds below are still used there. Prop 3 is dropped. This route goes back through (P_k) and Jensen (producer, Prop R1), which has a common exterior integral and so no H1. What that route needs is a classical bound with constants free of L, because they multiply x. Everything below is abelian, read at a small background by the absorption of Theorem 5. Label: derived at the linear level; not reviewed; the non-abelian reading is not written.

**Thresholds (changed).** Lemma 1 above used K_0^2 = K-bar L. Now K_0^2 := K-bar L^{2-delta}, T_f := L T_c/(C_r K_0), so T_f^2 = L^delta T_c^2/(C_r^2 K-bar), m_* := c_1 L^delta, c_1 = C'/K-bar, and delta := 1/3. Lemma 1(a) holds with the same constants. T_f/T_c ~ L^{1/6}. Since any crossing of a box costs at least L core cells, more than m_*, a merged cube in a sparse region has side at most C m_*, much less than L, and cubes do not chain across boxes. Cubes keep mutual distance at least 2.

**Lemma 5 (extension into a cube). Proved at the abelian level from Lemma 1 of `library/curl-poincare-exterior.md`.** Let Q be a cube of side l, S its shell of width 1 in level-k cells, H a fine field on S. There is H-tilde on Q u S, equal to H on S, with ||d H-tilde||^2_{Q^+} <= C (1 + l)^4 ||d H||^2_S, C free of eta, l, L.

*Proof.* S is a union of 8 slabs, each a product box with longest side l + 2. Lemma 1 there gives omega_F with ||H - d omega_F||^2 <= C l^2 ||d H||^2 on each slab. On the overlap of two slabs, a box with longest side l + 2, the Poincare inequality gives a constant with ||omega_F - omega_F' - a||^2 <= C l^2 ||d(omega_F - omega_F')||^2 <= C l^4 ||d H||^2. The constants close around elementary loops of slabs, since the shell is simply connected, by the same bound. A partition of unity with gradient at most C at scale 1 gives omega on S with ||H - d omega||^2_S <= C l^4 ||d H||^2_S. Inside Q put H-tilde := chi R^*(H - d omega) + d omega-hat, with R the lattice reflection of S onto the band of depth 1 in Q, chi a cutoff across the band, omega-hat any extension of omega. QED

The power 4 is what this crude proof gives. Any polynomial would do, with a smaller delta: in general delta = 2/(p+2) for the power p.

**Lemma 6 (classical gain). Derived at the linear level.** Let U* be the minimiser on the fibre of V', Ext the complement of cubes Q_i and dropped boxes D, with the plaquettes to them dropped, and with lines through them excluded. For H on Ext with Q_restr H = 0,

    A^Ext(U* + H) >= A^Ext(U*) + (1/2) ||d H||^2_Ext - sum_i ||F*||_{Q_i^+} ||d H-tilde||_{Q_i^+} - C ||F*||_{D^+} ||d H||_{Ext near D} - |<lambda, Q^o H-tilde>|,

so the minimum over H is at least A^Ext(U*) - G, with G <= C sum_i (1 + l_i)^4 E_ref(Q_i^+) + C E_ref(D^+) + C T_f^2 sum_{boxes} f_box, where f_box is the fraction of excluded lines in a box. This uses criticality of U* on the whole lattice in one line, <F*, d H-tilde>_all = <lambda, Q^o H-tilde>, and needs no coercivity of Ext. It replaces `Shift bound` and the holonomy discussion. At dropped boxes the extension is local, in level-(k+1) units, with absolute constants, because a valid coarse bond between two exterior boxes fixes the relative constant of the local gauges by Q^o H = 0, so no shape of D enters. Lines near hull: |theta_line - V'| <= C T_f, by Morrey in the three transverse dimensions, since grad_z theta is F integrated along the line and F is in L^4.

*Arithmetic.* E_ref(Q_i^+) <= C l_i^2 T_c^2/(K-bar L^{5/3}). With m < c_1 L^{1/3} and sum l_i <= 3 m in the region: sum (1+l_i)^4 E_ref <= C m^6 T_c^2/(K-bar L^{5/3}), which is below (c_b/32) m T_c^2, since m^5 <= c_1^5 L^{5/3}. This is what fixes delta = 1/3. The shift term: T_f^2 (3m/L)^3 <= C m^3 T_c^2 L^{-8/3}/K-bar is far smaller. Dropped boxes as in Lemma 1(a), with an absolute constant from the local extension.

**Prop 7 (rarity). Implication; replaces Prop 3 and Corollary 4.** Hypotheses: (P_k) with exterior weight, exterior coercivity below, Lemmas 5, 6. Conclusion: Prop R1 of the producer, with core cost c_b T_c^2 |C|.

*Numerator.* As in Prop R1: exterior weight times the cost, with lines through cubes excluded, so Ext decouples from the hull, and Z_Ext is one integral with constraint avg_ext W = V'.

*Centre of the exterior chart.* Take coordinates xi around U* on a convex domain K := { |xi_c| <= rho/g }, rho := C(L) T_f, with tree adapted to the hole. By exterior coercivity and C'(L) rho << 1, which a_*(L) can ensure, S is uniformly convex on K. So the minimiser W_0 := xi_0 exists, is unique, smooth in V' by the implicit function theorem, and has decay from the Hessian by Combes-Thomas. No separate regularity theorem on Ext is needed, and W_0 need not lie in the class at the scale of a cell: near a dropped box its flux on one cell may exceed T_c. Only C(L) T_f is small. Label: derived, given coercivity on K.

*Denominator: use U*, not W_0.* For W = W_0 + g B in Z_Ext, put W-tilde := U* + g B + H_s, with fill := U* + extension of g B + H_s, and H_s a bump on the exterior lines whose s makes the all-lines average exactly V'. At B = 0 the field is U*, with all lines averaging to V' and s = 0. So H_s carries only the fluctuation: s = -(f/(1-f)) (avg over hull lines of the fluctuation), a contraction with factor about f, Jacobian 1 + O(f) on a space of rank the number of parent bonds touched, so C per cube. *Correcting on the exterior lines rather than inside the tube is essential:* in the tube a mismatch epsilon costs epsilon^2, spread over all lines it costs (f epsilon)^2.

*Jensen.* With mu_Ext the normalised exterior measure, restricted to W-tilde in the cut of T at cells near gamma, at a factor at least (1/2) per such cell by sequential conditioning, T >= Z_Ext exp( - x G - x C E_ref(Hull^+) - C(L) sum |local support| ). Here x (A^Ext(U* + g B) - A^Ext(W_0 + g B)) = x G + (second order in g B), and the mean of the second is tr[ (D^2 A(U*) - D^2 A(W_0)) Cov ] with x g^2 = 1, at most C(L) ||H||_{l^1(local)}. The fluctuating fill costs C(L) per bond of the shell, with no x. *The relaxed field H := W_0 - U* is never extended into the hole*, so C_e enters once, through G.

Divide. The exterior integral cancels. What is left is exp(-x (c_b/2) T_c^2 |C| + C(L) |Hull| + hole volume), with |Hull| at most C m^4 per box, a polynomial in L per core cell, so z = exp(-c x T_c^2 + C(L) log x). QED

**Exterior coercivity (fluctuation only, so C(L) is allowed).** For v on Ext with v = 0 on a spanning tree of the exterior of each box, ||v||^2_box <= C_3(L) q_box(v), by Corollaries 3, 4 of `library/curl-poincare-exterior.md`. Crossing bonds between two exterior boxes are tied by the valid constraint, since its R_c lies in those two boxes. A box beside a dropped box has no bonds into it in the chart: those are hull bonds. So the extra data proposed under Lemma 2 above are not needed. An exterior box with no valid constraint at all decouples, and its constant gauge is a compact zero mode. The tree is chosen for the hole, on each term with a fixed site. The block centre may be in a cube; the contour part is a coarse gauge element, and lines are based at a point of the exterior joined to the centre by a fixed stem. The stem's transport is a group element g, which conjugates V' in the exterior constraint, and Z_Ext is invariant under that conjugation exactly, since A^Ext and R^E are gauge invariant on Ext. So rough stems cost nothing in the numerator. Not written in detail.

**Hostile check of this repair, recorded.** (a) Lemma 6 uses ||F*|| on the shells at L^4 level, with C_r from (R3), which is an implication, not a theorem. (b) The first version of Prop 7 extended the relaxed field H into the hole, which put C_e^4 into the budget and forced delta = 1/5, and it asked W_0 to be class, which is unproved at a free boundary near dropped boxes, where a re-entrant corner can concentrate energy on a cell. Both went away on using U* itself in the denominator. (c) The non-abelian reading of Lemmas 5, 6 is not written. The absorption has polynomial factors in L against T_f <= a_*/L^{1.8}, and a_*(L) can be shrunk at no cost to the ratios, since T_f/T_c does not contain a_*. (d) Prop 7 uses (P_k) in the numerator, so (P_k) step 3 stays an input, and its identification of the integral over E' with local densities of R_k is now the main unwritten step. (e) K must contain the labelled class fields near a dropped box only for an upper bound on the numerator, and it does, since rho exceeds T_c. (f) Theorem OS uses no dropped plaquettes, so it does not see W_0.

## What Prop 7 removes

`Relative chart`, `Shift bound`, the isoperimetric form of `Cut and Poincare`, spanning chains, pruning, and every statement about the shape of the core beyond the cube rule. Local densities of R_k on partial fields remain an input through (P_k).

## What failed on the way

1. Pruning, isoperimetry and Federer-Fleming chains: they were aimed at a sharp Poincare constant that nothing requires, since constants may depend on L.
2. Merging cubes at a distance proportional to their sides, so that extension operators exist: a sequence of single cells at geometric distances makes the side double with each cell. Merging only near-touching cubes avoids this, and the crude gap does not need separation.
3. The supremum over outer data, taken next to the hole, fails: atypical data adjacent to the hole can favour the bad field. Taken beyond a collar d_x ~ (log x)/mu, the outer data influence the inner integrals only through a tail, and the classical comparison is exterior-free. The inner region is then integrated crudely, at C^{|I|}, which is a polynomial in log x per core cell against a cost linear in x.
