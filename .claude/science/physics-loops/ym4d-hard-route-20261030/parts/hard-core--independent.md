lead: Anthropic/claude-opus-5-5/max 97c171d6-e01d-4994-bd7b-9cb6c6972d86
lease_until: <driver sets this>

## State of attack

**Formulation.** Hard-constraint block RG for SU(2) Wilson on a periodic 4-torus, with the quaternion-mean average with waypoints and a field-chosen base point (Text 1, 5.1, 5.4). This map is defined on the whole compact field space, it pushes Haar exactly to Haar, it gives a Markov kernel mu_W on the fields, and its linearisation is exactly the paired-contour Q of (R4). The induction is I(k) of Text 3.3: a sum over families of frozen islands, plus a small-field form on the complement. An island is recycled into the small-field polymers as soon as it is smaller than a block, the surrounding coarse field is eps_0-regular and no large fluctuation is next to it.
The vacuum is subtracted exactly by rho_k(trivial coarse field), which is also the named subtraction for UV-EXT.

**Order of constants.** Text 3.1: L; kappa, M; eps_0; eps_1 <= eps_0 / (4 L^2); m_R, eps_rule; E_0, B_0, alpha_0, alpha_1; r(g); gamma. FLOW is a hypothesis, not an input.

**What is derived and what is believed.**
- Derived: Lemma 1.1, Corollary 1.2, identity (1.2), Lemma 2.1, the linearisation in 5.1, identities (5.1)-(5.2), the removal of the star in 5.3 under its hypotheses, the real-s bound in Text 6 given Theorem I, Lemmas 7.1, 7.2, Theorem 7.3, the star removal for q_k, the symbol bound QQ^* >= 1/3, the Fubini identity and the n-dependence in 7.6.
- Derived at sketch level: (5.4), (5.5), (EX) up to nonlinear remainders, the tree count in 4.5, 7.2, 7.3, 7.4.
- Believed, not proved: (SF3), (SF4), the non-abelian part of (SF1), (CL) near frozen data, FLOW. **Theorem I is a target. It is not proved.**
- Numerics: flat-background defect check on an earlier form of the map, L = 3, 5, 7 for sheets, L = 3, 5 for single links; L = 7 single links did not finish. Pre-stated PASS-SHEET held, with max S = 1.000 at each L. Not yet run on the final map D3. **These runs did not hold the numeric lock:** up-6e18 held it from 21:30 UTC, my acquire failed, and I had piped its output through tail, which hid the failure. Load stayed near 3, RSS was small, and I have stopped them. No further numeric job runs until an acquire is confirmed.

**The large-field answer so far.** Large-field regions regenerate the hypotheses, conditionally on the frozen statements, and without any condition on c_F beta. The unrenormalised per-level count diverges (Proposition LF-count), but nothing in this scheme sums that quantity. An isolated fine core does not survive to a coarse level (DEC), so the sum over unrecycled shapes is a tree sum with bounded entropy per node. The divergent part is the vacuum part of the recycled gas, and it is cancelled by the named subtraction. I do not claim this is Balaban's R operation: his bodies could not be read (Project Euclid and Deep Blue both served bot checks, and I stopped there).

**Hardest remaining inequality.** (FLOW): beta_m >= beta_min > 0 for this map, uniformly in m, on the small-field and recycled parts together. It is the only item with a sign in it: if it fails, g_k leaves ]0, gamma] and Theorem I says nothing. It has no derivation here beyond the decomposition in 7.6, and no readable paper supplies it. The precise inequality to attack: |c_m - c_{m-1}| <= C_0, with C_0 independent of L, where c_m is the finite part of the second background derivative of log Z^{comp}_m. Close behind it: the non-abelian contraction in the norm N of 7.4.

**Routes tried and why they failed** (Text 1.5, 2, 5.4, 7.5): one-link solve (variance grows linearly with level); entire reference-path average (rough path keeps full weight; fine action no longer dominates at large curvature); line-averaged prefix (star cancels only approximately at large field); iterating the fiber flow for complex bounds (L^2 per level); one-function pointwise induction on all V (entropy compounds unless an excess lemma is proved for arbitrary fields, replaced by frozen islands); pricing a tower at tuned block centres (needed a density bound I could not prove, replaced by the field-chosen base point of 5.4); two thresholds in recycling (non-analytic indicator, removed); stepwise regularity of the lift (shape factor compounds, replaced by the one-shot identity); energy-only regular class (needs a lattice Uhlenbeck gauge I did not prove, set aside).

**Next action.** Compute items 1 and 2 of 7.7 at constant abelian background in U(1) inside SU(2), with the constraint Q^U in the charged sector, where the spectrum is explicit. If they cannot be bounded per level, fall back to |c_m - c_{m-1}| <= C_0 of 7.6. When the lock is confirmed held by this session: rerun the check on D3, and test q_k <= C ||d_k B||^2 in momentum space.

## Obligations
- gap: (FLOW), positivity of beta for this map, including recycled gas: diamagnetic and constraint-variation terms per level, size of the paramagnetic term (Text 7.7); or |c_m - c_{m-1}| <= C_0 independent of L (Text 7.6) -> Theorem I hypothesis, trajectory in UV-EXT
- gap: exact form of I(k), Mayer polymer with multi-body boundary terms (Text 3.3, 4.4, 5.6 item 5) -> Theorem I
- gap: (EX) with nonlinear remainders on the real fiber (Text 5.5) -> I(k+1)(d)
- gap: non-abelian contraction for the background in the norm N, with the operator bound in 7.4 -> (SF1), I(k+1)(a), (b)
- gap: (SF3) fluctuation integral with cut eps_1 and frozen boundary, bulk polymers independent of boundary -> I(k+1)(b)
- gap: (SF4) renormalisation of polymers: Ward identities and marginal extraction, for this map -> I(k+1)(b), uniform bound (3.3)(b)
- gap: gauge fixing in exterior blocks for this map, compatible with frozen neighbours -> (SF3)
- gap: rerun the field-inequality check on the final map D3; so far the script tests the earlier line-averaged map, and the lock was not held -> confidence in (5.5)
- unchecked: abelian upper bound q_k(B) <= C_I ||d_k B||^2 by a dual-basis lift, given the scaling of the tube weights -> normalisation in Text 6, (SF3)
- unchecked: non-abelian coercivity (Text 7.2) given N(U) <= eps(L) -> (SF3), (EX), uniqueness in (SF1)
- unchecked: Combes-Thomas decay (Text 7.3) given coercivity and saddle stability -> (SF3), polymer decay
- unchecked: (CL) from Text 7.2 next to frozen data, given N(U) <= eps -> 4.3 type F
- unchecked: weights (5.4), rectangle count, given axial surfaces with uniform vertices -> (5.5)
- unchecked: tree count in 4.5 given the fresh-core rule and the Load Lemma -> I(k+1)(c), Mayer convergence
- implication: (5.5), the unconditional form of (4.1), given (5.4) -> 4.3
- implication: real-s two-sided bound and UV-EXT in real form, given Theorem I and FLOW -> upper-chain
- discharged: Lemma 1.1 exact Haar pushforward -> Corollary 1.2, recursion (1.2), mixed bonds in 4.4
- discharged: Lemma 2.1 fiber flow -> Lipschitz estimate, checks
- discharged: exact identity (5.1), inequality (5.2) -> (5.5)
- discharged: linearisation of the final map equals (R4) -> propagator setting, (R5), (R7)
- discharged: Lemmas 7.1, 7.2 and Theorem 7.3, abelian coercivity uniform in k -> Text 7.2
- discharged: QQ^* symbol bound for Q_str -> Text 7.3
- discharged: paramagnetic term sign-definite per level, at second order and fixed Q -> (FLOW), partial

## Requests
- UV-EXT (lead, upper-chain): see Text 6. Real s is what this route gives uniformly in a and in volume. Zero-freeness at complex s is only available in a disc of radius of order 1/(physical volume in last-scale units), uniform in a. Please confirm the consumer can work from real s: the exponential moments in a chessboard bound have positive integrand. Also the named subtraction is log rho_K(1; beta).

## Text

### 1. The hard constraint, on the whole compact field space [DERIVED here; hostile check in 1.6]

Credit: taking a coarse link to be an average of paths through a pair of blocks is Balaban's construction (CMP 98; CMP 109
(0.4) as transcribed in the program's NOTES section 9.2, LANE-READ, body not re-read by me). The paired-contour linearisation
is RENEW section 2. The quaternion mean, the exact Haar pushforward and the rest of this section are derived here and are
specific to this push; I have not checked whether the mean appears in his papers. It is a choice of map: nothing of his
is imported on the strength of "many definitions serve".

**1.1 Geometry.** L odd. T_k = level-k torus, spacing 1 in level-k units; T_{k+1} = centres of L-blocks B(y). For a coarse
bond c' = (y, y + L e_mu), let I(c') be the set of L^3 level-k links crossing the face between B(y) and B(y + L e_mu).
Links of I(c') occur in no family for any other coarse bond, because every other family stays inside its own two blocks
and crosses its own face. "Interior links" are those inside a block.

**1.2 Quaternion mean.** Identify SU(2) with the unit quaternions in R^4. For a finite family with common endpoints and
fixed nonnegative weights summing to one, put m = sum_i w_i g_i in R^4, and Mean{g_i} = m / |m| whenever m != 0. Then:

- Mean(a g_i b) = a Mean(g_i) b, for a, b in SU(2); no element is singled out and the weights are permutation covariant.
- If g_i = exp(i A_i), then Mean = exp(i sum_i w_i A_i + O(|A|^3)): the second-order term is absorbed by the normalisation.
- If m != 0 and h_i is another family with sum over i of w_i |g_i - h_i| = delta and delta <= |m|/2, then |Mean{g} - Mean{h}| <= (4/|m|) delta.
- In SL(2,C) the same formula m / det(m)^{1/2} is holomorphic off det m = 0, so the map is analytic on the set where |m| is
  bounded below, with analyticity radius proportional to |m|.

For u in I(c') with transverse position t, let line(u) = {x in B(y) with transverse position t}. Put
a_u = Mean over x in line(u) of [P(y,x) * straight(x -> u^-)], and b_u = Mean over x in line(u) of
[straight(u^+ -> x + L e_mu) * P(y + L e_mu, x + L e_mu)^{-1}], with P the Mean over axial orders of axial paths. Both a_u, b_u are
functions of interior links only. Let T_u = a_u u b_u and define

    m(V, c') = L^{-3} sum_{u in I(c')} T_u(V),      M(V, c') = m(V, c') / |m(V, c')|.                                (1.1)

Where an inner mean has m = 0, take the first element in a fixed order: this happens on a null set and only makes the map
Borel, which is all that 1.3 needs. M is gauge covariant, with the block centres carrying the coarse gauge transformation.

*Linearisation.* With V = exp(iA) at first order,

    (QA)(c') = |B|^{-1} sum_{x in B(y)} A(straight(x -> x + L e_mu)) + h(y) - h(y + L e_mu),   h(y) = |B|^{-1} sum_x [avg axial A from y to x].

The h term is one function of the block for all directions, so it is pure gauge, and the coarse curvature is exactly the
average (R4) of RENEW section 2: F'(X) = L^{-4} sum_{y in B(X)} sum_{s,t < L} F(y + s e_mu + t e_nu). RENEW's (R5) and (R7), with their sharp
constants, apply to this linearisation. A family using a different x set for each direction would leave a residual
g_mu(y) - g_nu(y), a star through the block centre that gives weight of order 1 to plaquettes next to y; so the x set is the
full block, and the line average in a_u, b_u is what keeps each crossing link in exactly one element of the family.

**1.3 Lemma 1.1 (exact Haar pushforward).** Under product Haar measure on the level-k links, M(V) is Haar distributed on the
coarse links, and the coarse links are independent. Conditionally on the interior links the same is true, and the
crossing-link sets I(c') are independent. Hence D(W) := int dV delta(W^{-1} M(V)) = 1 for every W.

*Proof.* Condition on the interior links. Then {a_u, b_u} are fixed, and the sets I(c') are independent Haar families, with M(., c')
depending on I(c') only. For fixed c' and g in SU(2), the substitution u -> u b_u g b_u^{-1} on every u in I(c') preserves the product
Haar measure, and it sends T_u to T_u g for every u at once. So m -> m g and M -> M g on the full-measure set m != 0. Therefore the
conditional law of M(., c') is right-invariant, so it is Haar.  []

**Corollary 1.2 (Markov kernel, fibers, Jacobian).** Off the closed null set {m = 0}, M is real-analytic in the crossing links and
a submersion. Its Jacobian per coarse bond obeys J >= L^{-9/2}: the simultaneous right translation in the proof moves
L^3 links at unit speed each and moves M at unit speed, so dM dM^* >= L^{-3} on su(2). Fib(W) = {V : M(V) = W} is a
real-analytic manifold, non-compact only towards {m = 0}, and for bounded Borel f,

    int dV delta(W^{-1} M(V)) f(V) = int_{Fib(W)} f dsigma / J,      total mass 1 for every W.

So delta(W^{-1} M(V)) dV is, for each W, a probability measure mu_W on the level-k fields, and rho -> int mu_W(dV) rho(V) is a Markov operator.

**1.4 Exact recursion and the named subtraction.** rho_0 = exp(-beta A), rho_{k+1}(W) = int mu_W(dV) rho_k(V). All rho_k are
positive and gauge invariant, and int dW rho_k(W) = Z for every k. With 1 the trivial coarse field and r_k = rho_k / rho_k(1),

    r_{k+1}(W) = [ int mu_W(dV) r_k(V) ] / [ int mu_1(dV) r_k(V) ],      Z(beta) = rho_K(1; beta) int dW r_K(W; beta).        (1.2)

**So the explicit subtraction for UV-EXT is log rho_K(1; beta), the constrained partition function with the coarse field
trivial.** It is exact at every beta, and it carries every vacuum term, including the vacuum part of every large-field gas.

**1.5 Routes that failed.**
- *One-link solve.* M = X_1(others) V(b_0) X_2(others) gives a global graph and exact Haar. It gives b_0 weight 1, so the composite
  constraint routes each level through a single link, and in the linearised model the variance of the level-k coarse link is
  a sum of k terms of order one. That destroys the uniform bound on Q_k G Q_k^*. Scaling count, enough to drop the route.
- *Entire average around a reference path,* M = exp(i avg psi(T_u S^{-1})) S with psi entire and psi(T) = 0 at T = -1. It is holomorphic and
  a submersion, but psi differs from the logarithm at large angle, so a rough S keeps full weight once every loop through it is
  rough. A flux tube around S costs of order 30/L in level-k action and makes the coarse link rough by a large angle: the
  fine action no longer dominates the coarse action at large curvature, and a rough link on a composite straight line persists at no
  further cost. The quaternion mean has neither defect: each path has weight L^{-3} in m at every field.

**1.6 Hostile check of Section 1.** (a) A first proof of submersion for the reference-path average used loops indexed by x in B(y),
so a crossing link entered L loops, and the annihilation step only gave that a sum over a line vanishes. The line
averages a_u, b_u fix that here too: each crossing link is in one T_u. (b) Lemma 1.1 needs the crossing link to appear only once
in T_u and in no other coarse family. True by construction, provided a_u, b_u are built from interior links, and the straight
legs are interior except for u itself. (c) M is discontinuous on {m = 0}. The fiber near that set is where |m| is small, which needs
every T_u to be spread out: a large region of rough field in the tube. Upper bounds are unaffected, because mu_W is a probability
measure whatever happens there. Analyticity in W is not available there, and any consumer must keep away from it by a
lower bound on |m|. (d) This M is SU(2)-specific; for SU(N) the polar part has the same right-equivariance, up to a det
phase, which is a later target. (e) Nonlinear corrections in M have not yet been compared with any bound on Q_k G Q_k^*: a
small-field obligation, listed.

### 2. Fiber flow and the two ways the coarse field enters [DERIVED]

**Lemma 2.1 (fiber flow).** For g in SU(2) acting on one coarse bond c', define phi_g on level-k fields by u -> u b_u g b_u^{-1} for every
u in I(c') and the identity on all other links. Then M(phi_g V, c') = M(V, c') g, the other coarse links do not move, phi_g preserves
Haar measure and (phi_g)_# mu_W = mu_{W g}. So for bounded Borel F,

    int mu_{W g}(dV) F(V) = int mu_W(dV) F(phi_g V).                                                                      (2.1)

*Proof.* The substitution in Lemma 1.1, done on one bond.  []

Formula (2.1) is holomorphic in g for fixed interior links whenever F is holomorphic in the crossing links. In exchange it moves
L^3 links by the full angle of g. In a flat frame phi_g is a rotation of one face, so it leaves plaquettes inside the face
unchanged at first order and puts curvature of size |g - 1| on the order of L^2 plaquettes on the edges of the face. The action
cost is of order L^2 |g-1|^2, against |g-1|^2 for the smooth lift. Consequently:

- **Never iterate (2.1) to bound rho_k at a complex coarse field.** Using it at each level multiplies the constant in
  |r_k(e^{iy} V)| <= r_k(V) exp(C |y|^2 / g_k^2) by L^2 per step. [Scaling count.] The small-field part gets its complex bound from the smooth
  lift, and a frozen island only sees the coarse field through regular exterior data (Section 4).
- Formula (2.1) remains a useful exact identity for bounds at real W, for the Lipschitz estimate
  |log r_{k+1}(W g) - log r_{k+1}(W)| <= sup_V |log r_k(phi_g V) - log r_k(V)|, and for checks.

### 3. Order of constants and the induction statement

**3.1 Order.** Fix, in this order:

1. L odd, large (a function of d = 4 only; used for L^{-2} decay of defects against the constants of 4.2).
2. kappa, the polymer decay rate, large enough for the Mayer and Fubini steps; then M = L^{m_0} >= M(L, kappa), random-walk and polymer cube.
3. eps_0, the regularity threshold for the current field, small depending on L, M; c_A, the action constant of (CL).
4. eps_1 <= eps_0 / (4 L^2), the fixed fluctuation cut. Then a field within eps_1 of the level-k background of an eps_0-regular level-(k+1) field is automatically eps_0-regular: its curvature is at most eps_0 / L^2 + 4 eps_1. m_R, the grace depth of (DEC), from eps_0 and L. eps_rule >> eps_0 absolute (5.4).
5. E_0, B_0: polymer and boundary-polymer bounds. alpha_0, alpha_1: analyticity radii. These are allowed to depend on everything above.
6. r(g) = (log 1/g)^{r_0}: collar width, if (SF3) needs one (5.6 item 2).
7. gamma, the bound on all the g_k, last and small depending on everything above.

Two constants are not in this list and no statement may assume them: a bare-coupling relation (the flow is a hypothesis of
Theorem I and an obligation, not an input to any large-field step), and any power of g in the large-field thresholds.

**3.2 Islands.** A *cell* is a level-k M-cube. An *island at level k* is Y = (D, C, n, zeta), where D is a connected union of cells (its
domain), C subset D is its core, n records for each part of D the finer level at which it was frozen, and zeta are the
frozen variables at those levels, and D contains the r(g_k)-neighbourhood of C. Islands in a family are disjoint and non-touching.

**3.3 Statement I(k) (draft; the words "frozen", "recyclable" are fixed in Section 4).** For all real V on T_k,

    r_k(V) = sum_{families Y} [ prod_{Y in Y} F_k(Y; V|_{D(Y)^+}) ] exp( -g_k^{-2} A_{Om}(U_Om(V)) + sum_{X subset Om} E_k(X; U_Om(V)) ) chi_k(Om; V),    (3.1)

with Om = Om(Y) the complement of the domains, and U_Om(V) the background on Om, such that:

(a) *Small-field form.* chi_k(Om; V) forces V to be eps_0-regular on Om. U_Om exists and is analytic on the regular set (SF1).
(b) *Polymers.* E_k(X; .) is gauge invariant, depends on U on X only, is analytic on the complex class of radius alpha_1 and obeys
    |E_k(X)| <= E_0 exp(-kappa d_k(X)), E_k(X; 1) = 0 and, summed against the level-to-level renormalisation (SF4), the uniform bound
    sum_{X subset Om} |E_k(X; U)| <= C_E |Om| on regular U. E_k contains the recycled gas.
(c) *Island bound.* F_k >= 0 on real data. For each island, with type-T core cells counted per the level at which they became core,

        F_k(Y; V) <= prod_{j <= k} prod_{cells c in C_j(Y)} exp(-c_F / g_j^2),                                               (3.2)

    uniformly in the data, c_F > 0 fixed (4.3), where C_j(Y) is the set of type-T cells core at level j. This bound carries no
    constant per domain cell: all collar and normalisation losses have been absorbed by the core cells of the same level.
    Type Z cores have no absolute action cost, because F(U) can nearly cancel delta F on a cell. They are charged relative to the background, in (d), or to a type-T core within their margin, which pays their polylog count.
(d) *Recyclability.* If the level-(k+1) field is eps_0-regular on the margin of D(Y), no Z core lies in it and D(Y) is smaller than an L-block at level k+1, the **activity**
    a_k(Y; V) := F_k(Y; V) exp( -g_k^{-2} [A_{Om}(U_Om) - A(U)] ) / (vacuum Gaussian on D(Y)), the island compared with its regular replacement,
    is the restriction of a function analytic on the complex class of radius alpha_1 of the exterior data on D(Y)^+, and it obeys the
    bound (3.2) up to a factor 2. The comparison is global: (3.2) for F_k alone does not imply it. See (EX) in Section 5.
(e) *Gauge and lattice symmetry.* All objects are gauge invariant and covariant under the lattice symmetries of T_k.

**Theorem I (target).** Suppose g_k <= gamma for all k <= K. Then I(k) holds for all k <= K, with constants not depending on k, K or the volume.
The flow 1/g_k^2 = 1/g_{k+1}^2 + beta_{k+1}(g_k) is defined by the extraction in (SF4), with beta including the recycled gas.

### 4. One step k -> k+1: what regenerates, and why (the crux)

Credit: the sum over large-field regions, frozen variables, the bound by the level's own action and the collars are the
organisation of Balaban (CMP 119, 122; titles and reviews only, bodies unread) as exposed by Dimock II and III, which I read
for d = 3 scalar (Theorem 3.1 of II, Lemmas 11 to 13 of III). Dimock II Remark 3 says only that the R operation converts some
large-field contributions back to small-field ones. **The recycling below is my reconstruction of that sentence. I do not claim it is
Balaban's operation.**

**4.1 Frozen statements consumed here (leaves, come back later).**

- (SF1) *Background with frozen boundary.* Given coarse field W eps_0-regular on a union of level-(k+1) cells Om', and frozen
  regular level-j data (j <= k) on the boundary, the multi-scale constrained minimiser U_Om' exists and is unique among regular
  orbits, analytic in W on the complex class of radius alpha_1, with exponential decay of its dependence on boundary data.
- (SF2) *Fluctuation covariance on Om'*, with hard constraint and frozen boundary: uniform bound and decay.
- (SF3) *Fluctuation integral with frozen boundary and cut |B| < eps_1 at fixed eps_1.* log of the integral over the exterior, relative
  to the vacuum normalisation, is sum over X subset Om' of E^{nofr}(X; U) plus sum over X touching the boundary of B(X; W, frozen),
  with bulk polymers identical to the boundary-free ones and |B(X)| <= B_0 exp(-kappa d(X mod boundary)).
- (SF4) *Renormalisation.* Any polymer family that is gauge invariant, symmetric, analytic on the complex class of radius alpha_1 and
  bounded by E_0 exp(-kappa d) splits, with constant and marginal parts extracted at the trivial background, so that the remainder gains
  (L^j eta)^{4+alpha}. This is the machine of CMP 109 Section 4 and 5 (LANE-READ). Applied to E^{nofr} plus the recycled gas.
- (FLOW) beta_{k+1}(g) >= beta_min > 0 for g <= gamma, in the scheme above. Not supplied by any readable paper.

**4.2 One-step field inequality (OS)** [statement frozen, to be proved in Section 5]. Let V be real on the hull of a coarse plaquette
P, with W = M(V). Split the level-k plaquettes of the hull into irr = {|V_p - 1| > eps_0} and reg = the rest, and let f_p = |V_p - 1|.
Suppose every tube has |m| >= 1/2. Then

    |W(dP) - 1| <= C_OS ( L^{-2} ||f||_{l^1(irr)} + ||f||_{l^2(reg)} ),                                                      (4.1)

with C_OS depending weakly on L (see (5.5)). If some tube has |m| < 1/2, at least a fixed fraction of the
crossing paths in that tube are mutually misaligned, and then the hull contains at least c L^2 plaquettes with f_p >= c/L^2 (Lemma 5.x).

**4.3 Consequence: fresh cores (DEC) and the load of a core.** Split in (5.5) at eps_0: irr = {f > eps_0}, reg = the rest, and put Lam = L^2 / (2 C_OS). Let W have curvature phi >= eps_0 at a coarse plaquette. Then at least one holds: (F) ||f||_{l^2(reg)} >= phi / (2 C_OS), a fresh energy at level k, with cost at least c_A phi^2 / (4 C_OS^2 g_k^2) through (CL), since these plaquettes are in the small-field region; or (D) ||f||_{l^1(irr)} >= phi Lam, so eps_0-irregular children carry total curvature at least phi Lam. Iterating (D): if no node of type F occurs down to depth t, the irregular descendants at depth t carry total curvature at least eps_0 Lam^t. Since f <= 2, their number is at least N_t := (eps_0 / 2) Lam^t, which is above 1 only for t > m_R := log(2 / eps_0) / log Lam. Level 0 counts as type F, since there the plaquette is the bare action. So:

*Load Lemma.* Charge each type-D cell equally to the type-F cores below it. A type-F core then carries total load at most sum_{t <= m_R} 1 + sum_{t > m_R} Lam^{-(t - m_R)} <= m_R + 2 per column of ancestors. [Follows from (5.5).]

A chain of single irregular children has depth at most m_R, since curvature must grow by Lam at each level going down and it is capped at 2. c_F := min(c_A eps_0^2 / (4 C_OS^2), c_Z eps_1^2) with c_Z from (EX). eps_R plays no part in this.

**4.4 The step.** Fix W. Take a term of (3.1) with family Y at level k, and integrate over V under mu_W.

(i) Bad set. Only two kinds of new core exist. On the set where W is eps_0-regular, write V = exp(iB) V^*(W), with V^* the level-k background. *Type Z:* a level-k cell with |B| >= eps_1. *Type T:* a level-(k+1) cell where W is eps_0-irregular; freeze V on its hull. If W is eps_0-regular and no Z cell is present, V is eps_0-regular by 3.1 item 4. So V being irregular is not a third case, the indicator chi_k equals 1 on the exterior, and it never enters an analytic function: the cut is on B, the integration variable, which does not depend on W. S is the union of these cores, of the old domains, and of collars if any. Partition of unity on these events.

(ii) Exterior. Off the r(g_k)-collar of S, apply (SF3). The frozen part is the integral over V on S and collar under the conditional
measure with M(V) = W. On a tube partly outside the frozen part, exterior links solve the constraint.

(iii) Normalisation. Dividing by the exact vacuum: frozen cells lack the vacuum factors of level k, and that gives at most (C/g_k)^{n} per
frozen level-k cell, plus e^{C_E} from renormalised polymers and e^{B_0} per boundary cube. All level-j vacuum terms with j < k were cancelled at
level j, because the fields at level j there were regular. **That is the point where the unrenormalised per-level count disappears: fine levels
inside a coarse large cell were recycled early and did not wait for the coarse cell.**

(iv) New island weights. Group components. Each component has domain D', core C' and the old cores. Losses per new frozen cell are
n log(C/g_k) + C_E + B_0, and frozen cells number at most C r(g_k)^4 |C'| + (rim of old domains). With g <= gamma, the losses are at most (c_F / 2 g_k^2) per new
core, and the rim is paid by the grace budget of 4.5.

(v) Recycling. If a component has domain smaller than an L-block at level k+1, and W is eps_0-regular on its margin, and no Z core lies in the margin, then all its level-k variables are integrated over Haar without any hard constraint on the exterior: by Lemma 1.1 the mixed bonds impose nothing on interior links, and the exterior carries the constraints of the fully exterior bonds. So its activity a(Y'; W) depends on W only through regular exterior data. It is analytic there, because U_Om' is (SF1), Re A at complex boundary links grows only at second order in Im, and the frozen data are real. Sum over the hard-core gas of all recyclable components in Om': the Mayer series gives sum over X of E^R(X; W), normalised at W = 1. Add E^R to E^{nofr} in E_{k+1}, and let (SF4) run on it. **E^R(X; W) is defined and analytic on every eps_0-regular W on X, with no indicator: this was wrong in my first version, which recycled only where W was eps_R-regular and so left a non-analytic indicator in E_{k+1}.**

(vi) Everything that does not get recycled stays as an island, with bound (3.2) at level k+1.

**4.5 The count (the crux of the 4D price).** Why the sum over island shapes converges with no condition on c_F beta.

The old obstacle: per level-(k+1) cell there are L^{4(k+1-j)} level-j cells, each with weight exp(-c_F/g_j^2), and along a flow with
1/g_j^2 = 1/g_{k+1}^2 + beta (k+1-j) log L the product exp(-c_F/g_{k+1}^2) L^{(4 - c_F beta)(k+1-j)} diverges when c_F beta < 4. Since c_F is of order eps_1^2, it is in that range for small thresholds.
This is Proposition LF-count of the program [arithmetic re-derived here; depends on the flow].

Now use the rule that governs what can still be frozen at level k+1. By 4.4(v) and 4.3, a level-j core survives to level k+1 only if, at each level i in
j + m_R + log_L(M r) <= i <= k+1, there is a new core inside its margin: a Z cell at level i-1, or a T cell at level i. A T cell has a fresh core within depth m_R. So an island's
cores form a connected graph in space and scale, where a core at level j has a neighbour at a level in (j, j + m_R] within its margin, or the island is
still within grace of j. Hence the number of placements is governed by the tree-graph count, with a bounded number of positions per node:
(C L^{4 m_R} r^4) per node, and not L^{4(k+1-j)}. Each node costs at least exp(-c_F/g_{k+1}^2). **So the sum over shapes rooted at a level-(k+1) cell is bounded by a convergent tree
sum with node weight C L^{4 m_R} r(g)^4 exp(-c_F/g^2), for every value of c_F beta, provided only g <= gamma.** The factor L^{4(k+1-j)} never arises, because no isolated fine core is ever still frozen
at a far-coarser level.

What happens to the divergent quantity? It is the vacuum part of the recycled gas: at level j + m_R, each cell gets an activity of order
L^{4 m_R} exp(-c_F/g_j^2), small, and at W = 1 this goes into log rho_K(1; beta) as a term of order L^{4(K - j)} exp(-c_F/g_j^2) per unit volume, which may diverge as K grows. It is
**cancelled exactly by the named subtraction**, not bounded. The W-dependent part of the same activity goes through (SF4): marginal shift of order
exp(-c_F/g_j^2), which is summable in j, and the remainder gains (L^j eta)^{4+alpha} [conditional on (SF4)].

### 5. The field inequality (OS) [DERIVED except where marked]

**5.1 A change in the average: waypoints.** The prefix of 1.2 averages x over line(u), which depends on the direction mu. Termwise that leaves a star through y
whose cancellation is only approximate at large field. Replace it, keeping every other line of Section 1:

    Psi_y^mu(z) = Mean over x in B(y), and over axial orders, of [ path(y -> x) * R_mu(x, z) ],     a_u = Psi_y^mu(u^-),     b_u = Psi_{y'}^mu(u^+)^{-1},

with R_mu(x, z) first moving transversely from x to (z_perp, x_mu), and then straight along mu to z (reversed for the suffix). Everything is interior, so each crossing link is still private, so
Lemma 1.1, Corollary 1.2 and Lemma 2.1 hold unchanged. The mean over x and orders is one flat mean, with no inner normalisation, and the x set is all of B(y) for every direction.

*Linearisation.* QA(c') = h(y) - h(y') + avg_u [ avg_x A(R_mu(x, u^-)) + A(u) + avg_{x'} A(R_mu(u^+, x')) ]. The transverse legs cancel in the mean: x_perp and u_perp are independent and identically distributed, and swapping them reverses the path while the reversed order is also in the family, so the expected signed use of a transverse link is exactly zero.
A longitudinal link at (xi_mu, xi_perp) in B(y) is used when u_perp = xi_perp and x_mu <= xi_mu, with probability L^{-3} (xi_mu + o + 1) / L, and likewise in B(y'), which is the triangular tube weight of the paired-contour average. **So Q is exactly the Q of (R4), and RENEW's (R5), (R7) with their sharp constants apply.** [Derived.] In particular constant curvature is reproduced exactly with no factor per level. The check script as first written tests the earlier line-averaged map. **Obligation:** rerun the check on this map.

**5.2 Exact identity.** For unit quaternion families with means m_i = |m_i| M_i, and independent indices,

    |m_1| |m_2| |m_3| |m_4| * M_1 M_2 M_3^{-1} M_4^{-1} = avg_{u_1, u_2, u_3, u_4} T^{(1)}_{u_1} T^{(2)}_{u_2} (T^{(3)}_{u_3})^{-1} (T^{(4)}_{u_4})^{-1},          (5.1)

because quaternion multiplication is multilinear and (avg T)^* = avg T^*. Each term on the right is the holonomy Gamma of a closed loop. Since the left side is a positive multiple of a unit quaternion,

    |W(dP) - 1| <= (2 / prod_i |m_i|) avg |Gamma - 1|.                                                                                     (5.2)

(If Re W >= 0 then |W - 1| <= sqrt 2 |Im W|, and Im W is the average of Im Gamma over the product of the |m_i|. If Re W < 0 then avg Re Gamma < 0, so avg |Gamma - 1| >= 1.) This holds at every field with all m_i != 0.

**5.3 Removing the star.** Termwise Gamma still passes through each y_i. Fix a block y, and a waypoint x_0 in B(y), used only in the analysis. Put Xi_x = path(y -> x) R(x, x_0) and rho_x(z) = R(x, x_0)^{-1} R(x, z), a path from x_0 to z through x which does not visit y.
Then path(y -> x) R(x, z) = Xi_x rho_x(z), with **Xi_x independent of z and of the direction mu**. Let rho(z) be any element and d(z) = avg_x |rho_x(z) - rho(z)|. Then

    m_z = avg_x Xi_x rho_x(z) = Xi_bar rho(z) + (error of size <= d(z)),   Xi_bar = avg_x Xi_x.

If |Xi_bar| >= 1/4 and d(z) is below 1/16, then Psi(z) = (Xi_bar / |Xi_bar|) rho(z) up to an error C d(z) with C an absolute constant. **The factor Xi_bar / |Xi_bar| is common to all z and all directions at y, so it cancels from W(dP) exactly.** What remains are the paths rho(z),
which are star free. Then (5.2) applied to the star-free families, and non-abelian Stokes, |holonomy of a closed loop - 1| <= sum_{p in surface} f_p for any spanning surface, give

    |W(dP) - 1| <= C sum_p w_p(x_0) f_p,   where w_p(x_0) = probability, over the uniform endpoints, that p lies in the chosen spanning surface.                                 (5.3)

Here x_0 is free in each block, so average (5.3) over x_0 uniform in B(y). Then every vertex of the polygon is uniform on a block, or on a face with the mu-coordinate re-randomised by the transverse-first rule, and the surfaces can be taken as a bounded number of axial rectangles, each with two
perpendicular coordinates equal to independent uniform coordinates of the vertices. A fixed plaquette thus has probability at most C L^{-2}, and the area is at most C L^2:

    w_p <= C_w L^{-2},    sum_p w_p <= C_w L^2,     with C_w depending on d only.                                                                                    (5.4)

Splitting at eps_0 and Cauchy-Schwarz on the regular part give (4.1), with C_OS = C C_w independent of L, **under the hypotheses |Xi_bar| >= 1/4, d(z) <= 1/16 and |m_i| >= 1/2 at every block of the plaquette.** [Derived; the rectangle count in (5.4) is a sketch, not checked line by line.] If d(z) > 1/16 then (5.3) has a right side of order one
at some scale, and that case is on the (D) side of 4.3 with a large weighted sum, so it is harmless there. The hypothesis that can fail with a small weighted sum is the next one.

**5.4 The exception and the repair: a field-chosen base point.** |Xi_bar| small is not excluded by the weighted sum (5.3). Rotating the first links out of y in directions e_1, e_2 by -1 makes half of all paths from y change sign, with about 16 rough plaquettes next to y, whatever L is. If then |Xi_bar| <~ d, the factor cannot be removed, W near y is erratic, and a coarse link at y can be rough from a defect of fixed size. Since y can be a block centre at the next level too, a tower can form at nested centres. I first tried to price this tower: one position per level, tuned set of Haar volume (g_i/eps_R)^4, and zero net dimension count because the 24 frozen links at y are matched by 24 constraints. That needed a density bound I could not prove. So I changed the map instead.

**Final map (D3).** Fix eps_rule with eps_0 << eps_rule. Call a plaquette *rule-rough* if f_p > eps_rule. For z in B(y) and a site x_0 in B(y), put

    Psi_y^mu(z; x_0) = path(y -> x_0) * Mean over x in B(y), and over axial orders, of [ R(x_0, x) R_mu(x, z) ],

and let s(x_0) = sum over rule-rough p in B(y) of min(1, dist(p, x_0)^{-2}). Choose x_0 = y if s(y) <= s_rule, an absolute constant. Otherwise x_0 is a minimiser of s, and ties and the axial order of path(y -> x_0) are decided by uniform choice in the kernel, which makes the kernel a finite mixture of hard constraints. All of this depends on interior links only, so the crossing links stay private and Lemma 1.1, Corollary 1.2 and Lemma 2.1 hold for each element of the mixture; mu_W is still a probability measure, and the kernel is exactly covariant under the lattice symmetries because the choice is uniform over the orbit.

- On fields with no rule-rough plaquette, x_0 = y, so this is the map of 5.1, with the same linearisation (R4).
- Exterior regular fields have f <= eps_0 << eps_rule, so the rule depends only on frozen rough data, not on exterior data. Analyticity in W through the exterior is unaffected.
- path(y -> x_0) is a **common left factor** for every z and every direction at y. It cancels exactly in W(dP), however rough it is. There is no mean over stars through y, hence nothing to tune.

**(4.1) for D3, unconditional.** Averaging s over x_0 shows min s <= C (number of rule-rough plaquettes in the block) L^{-2}. Let the star weights around x_0 be w*_p = min(1, dist(p, x_0)^{-2}), with sum of squares at most C log L. The dispersion over x of the paths from x_0 is at most C sum w*_p f_p. Case A: this is at most 1/8 at every relevant block. Then all |m| >= 1/2 and 5.3 applies with no star, giving (4.1). Case B: it exceeds 1/8 at some block. Then either the rule-rough part has C L^{-2} ||f||_{l^1(rule-rough)} >= 1/16, or the part with f <= eps_rule has sqrt(C log L) ||f||_{l^2} >= 1/16. In both, the right side of (4.1) exceeds the trivial bound |W - 1| <= 2, up to the constant. So

    |W(dP) - 1| <= C_OS ( L^{-2} ||f||_{l^1(irr)} + ||f||_{l^2(reg)} ),   C_OS <= C sqrt(log L),   at every real field.                                   (5.5)

C_OS depends weakly on L, Lam = L^2 / (2 C_OS) is still large, and 4.3 is unchanged. [Derived, given (5.4) and the rectangle count, with the split threshold anywhere up to eps_rule. Case A's constant has not been computed.] **So the tower at nested centres does not occur for this map, and the Load Lemma of 4.3 stands with no special case.**

**5.5 Global excess (EX) (statement; consumer: (3.3)(d)).** Let W be eps_0-regular on the hull of an island smaller than an L-block, let U be its regular background, and let V in Fib(W) be regular off the core C. Then

    A(V) - A(U) >= c_E sum_{cells c in C} min_p-in-c f_p(V)^2 - (corrections of smaller order).

*Argument so far.* Write V = exp(i delta) U. Then A(V) - A(U) = <F(U), delta F> + (1/2)|delta F|^2 + higher. At the core, delta F is at least eps_0 / 2 and F(U) is at most eps_0 L^{-2}, so the sum of the first two terms is at least (1/4)|delta F|^2 there, with no sign problem. Off the core, the first-order term is <D^* F(U), delta>, and U being the constrained minimiser means D^* F(U) lies in the range of Q^*; so that term is <J, Q delta>.
On a real fiber, Q delta vanishes only to linear order. The frozen rough paths contribute to it with weight f, the fraction of paths through the core, so the term is at most |J| f, at most eps_0 f at coarse-bond scale. That needs f << eps_0, which holds for islands that are small against a block: this fixes the extra grace levels. A comparison over the domain alone would have a boundary cross term of order
(eps_0 eps_1 L^{-2}) |dD| and would lose: the comparison has to be global. [Derived at this level of detail. Nonlinear remainders are not done.]

**5.6 Attack log on Sections 3 to 5** (hostile, in the order found).
1. *Collars with g-dependent r.* In a comparison over the domain, the cross term above beats the core cost once r is large. Fixed by the global comparison in 5.5. The same issue for losses per frozen cell, n log(C/g) r^4, is absorbed by c_F / g^2 for polylog r.
2. *Are collars needed at all?* Exterior integration against a regular boundary gives B_0 per boundary cube with no log(1/g). Freezing a whole collar is therefore wasteful, and it may be replaced by boundary polymers. Decision: keep r only if (SF3) needs it for a tiny remainder.
3. *Thresholds.* A two-threshold version recycled only where W met a stricter threshold, leaving a non-analytic indicator in E_{k+1}. Removed: see 3.1 item 4 and 4.4 (i), (v). There is one regularity threshold eps_0 and one cut eps_1.
4. *M-cubes against L-blocks.* A cell is an M-cube and M > L, so a fresh island is never smaller than an L-block at the next level. Recycling can only start about log_L(M r) levels later. This is part of the grace, and it is paid from the core budget.
5. *Multi-body boundary polymers.* Polymers that touch two islands prevent activities from factorising. Handled by treating connected sets of islands and polymers as one Mayer polymer: the standard localisation, but not written out.
6. *Fresh energy near an island.* (CL) must hold for the multi-scale background next to frozen data. Listed in (SF1).

### 6. What this gives UV-EXT [DERIVED given Theorem I and FLOW]

Fix the trajectory: K levels, a = L^{-K} in units of the last cell, and g_K <= gamma. |T_K| is the physical volume in last-cell units. By (1.2), Z(beta + s) = rho_K(1; beta + s) int dW r_K(W; beta + s).

**Real s.** Let s be real with |s| <= s_0 := 1/(2 gamma^2), in the normalisation of (0.2) of CMP 109: an additive shift of beta shifts every 1/g_k^2 by about s, so all g_k stay below gamma' = sqrt 2 gamma. This agrees with the guide in GOAL.md that s is of order one in beta, and it is not a fractional shift. Apply Theorem I at beta + s.
- Upper bound: r_K(W) <= exp(C |T_K|) for every W, because polymers sum to at most C_E |Om|, the action is positive, each island has activity at most 1 by (3.2), and the sum over families is at most exp(tiny |T_K|).
- Lower bound: on the ball |log W| <= g_K, r_K >= exp(-C), and the ball has Haar mass at least (c g_K)^{n |T_K|}.
Therefore

    exp(-C |T_K|) <= Z(beta + s) / rho_K(1; beta + s) <= exp(C |T_K|),     C = C(gamma) not depending on K or the volume.

So log Z(beta + s) - log Z(beta) - [log rho_K(1; beta + s) - log rho_K(1; beta)] is at most 2 C |T_K| in absolute value, for real s. **This is UV-EXT in real form, with the subtraction named.**

**Complex s.** |Z(beta + s)| <= Z(beta + Re s) is trivial. Non-vanishing is not. rho_K(1; beta + s) != 0 should hold with the polymer expansion at the trivial field, uniformly in a and volume. [Believed.] But int dW r_K(W; beta + s) is a weak-coupling lattice integral on |T_K| cells at coupling g_K <= gamma, and no statement in this file controls it beyond |log r_K(W; beta + s) - log r_K(W; beta + Re s)| <= C |Im s| |T_K|. That gives zero-freeness in |Im s| <= c / |T_K|: uniform in a, and **not** uniform in volume. A disc uniform in volume would say that Lee-Yang zeros stay away from the real axis in infinite volume, an infrared statement, at a coupling where the expansion has stopped. So UV-EXT as drafted is more than this route gives. **Proposed wording:** real s in a fixed interval uniform in a and volume; complex s in a disc of radius c / |T_K|, uniform in a; the constant times physical volume in both. This is a request, not an edit: the target lead owns the wording.


### 7. Fluctuation form: a route without random walks [labels on each step]

**Target (COER).** At a regular non-abelian background, with frozen boundary, the fluctuation form on ker Q is bounded below, and its inverse has exponentially decaying kernel, uniformly in k and the volume. Every Gaussian in (SF3), the uniqueness in (SF1), the Z-core cost and the normalisations consume it. My only source is CMP 99:389, unread; Dimock's analogues are abelian, and they use random walks with local gauge patches. The route below uses neither.

**7.1 Lower bound, abelian.** Let q_k(B) = min{ ||dA||^2 on the fine lattice : Q_k A = B }.

*Lemma 7.1.* q_k(B) >= ||d_k B||^2_{l^2(T_k)}, for every k. [DERIVED.] The curvature map is the n-fold direct average, n = L^k, by the composition rule: base-point offset and path offset written in base L biject the nested sums with the direct ones (RENEW section 2, rechecked). Its row sum is n^2 and its column sum is n^{-2}, so Cauchy-Schwarz gives the bound with constant exactly 1. Nothing compounds, since this is one-shot.

*Lemma 7.2 (block Poincare).* If QB = 0 on the bonds of a block pair, then sum_b |B_b|^2 <= C_P(L) ( sum_p |d_k B_p|^2 + sum_{x} |g(x)|^2 ), summed over the hull, where g(x) is the axial average of B from the block centre to x. [DERIVED.] An interior link equals g(x + e) - g(x) up to plaquette sums over a bounded surface. Two crossing links of the same face differ by interior links and a strip of plaquettes. The average over the face is fixed by QB = 0, in terms of interior links and h(y) = avg_x g(x). All constants depend on L only, and the statement lives on a finite graph at level k.

*Theorem 7.3 (abelian COER).* With Balaban's gauge term ||G B||^2 = sum |g|^2, the form q_k + G^* G is at least 1 / C_P(L) on ker Q, for all k, and so the fluctuation covariance is bounded by C_P(L) at each level-k link. [DERIVED from 7.1, 7.2.] Mixed bonds, with one block frozen, impose nothing on interior links by Lemma 1.1, so the same proof runs on exterior blocks; frozen variables have zero variation. **The whole lower bound is finite-graph plus one Cauchy-Schwarz.**

*Star removal.* Q_root(d Lambda) = Lambda(y') - Lambda(y), so q_k(B) = min over coarse gauge of the same problem with Q_str, in which there is no star through y. Hence q_k(B) depends on B only through d_k B: q_k(B) = min{ ||F||^2 : F closed, A_k F = d_k B }. [DERIVED.]

*Saddle stability.* In units of the block, Q_str has diagonal QQ^* weight int tri^2 = 2/3 and overlap int tri(x) tri(x+1) = 1/6 with each of two neighbours along the bond, and none across directions or transversely. So its symbol is 2/3 + (1/3) cos theta >= 1/3. [DERIVED, explicit.]

**7.2 Non-abelian lower bound [SKETCH; consumes (REG) of 7.4].** Let U have all-level norm N(U) := sup_{j <= k} sup_P L^{2(k-j)} |curv_j(P)| <= eps. For a variation A with B = DM^k_U A,

    (D_V B)_P = sum_p m^U_{Pp} Ad(tau_{Pp}) (D_U A)_p + R_P.

Ad is an isometry, so Cauchy-Schwarz loses nothing from the transports. The weights are the linear ones up to factors 1 + O(Y_i), with Y_i the path dispersion at level i, and for such U sum_i Y_i <= C eps is geometric, so there is **no compounding through levels**. R_P is at most sum m_p |F_p| |A_p| <= eps eta^2 ||A||_{2,hull}. Fine-level Poincare per tube gives ||A||^2_{2,hull} <= C eta^{-2} ( |B|^2 + ||D_U A||^2 + ||D_U^* A||^2 ), so R_P <= C eps eta (...), negligible. The paramagnetic term <A, ad F A> <= eps eta^2 ||A||^2 <= C eps ( |B|^2 + ||D_U A||^2 ). Therefore

    <B, Delta^{(k)}(U) B> >= (1 - C eps) ||D_V B||^2 - C eps ||B||^2,

and D_V-Poincare on the block, in a near-flat gauge, gives coercivity once eps <= eps(L). In particular the Nielsen-Olesen negative mode does not appear in the fiber at eps L^2 << 1: its scale is below the gap only for curvature of order 1 in block units. And a regular field's fiber slice |B| < eps_1 is strictly convex, so the minimiser there is unique with no further argument.

**7.3 Decay by Combes-Thomas, no gauge patches [SKETCH].** On the fine lattice, take the saddle operator S built from K = H_U + Q_k^* G^* G Q_k + tau D_U D_U^* and the constraint Q^U_{k+1}. Conjugate by exp(phi), phi scalar, |grad phi| <= delta / ell, ell the block scale. A scalar weight commutes with Ad, so D_U(exp(phi) f) = exp(phi) (D_U f + (grad phi) f), and the commutator is at most (delta / ell) ||f|| ||D f||, which by Poincare is at most C delta ||D f||^2. Q has kernel at scale ell, so its commutator is C delta in scaled norms, and inf-sup comes from QQ^* >= 1/3 up to O(eps). So S_phi is invertible for small delta, which gives C_fine with weighted bound C ell^2. Finally ||Q_k^* h||^2 = O(ell^{-2}) for a unit source at a level-k link. Hence

    |C_k(b, b')| <= C(L) exp(-delta(L) d(b, b')),   uniformly in k, in regular U and in the frozen boundary.

This is the point of the route: a local gauge is never chosen, so non-translation-invariance and large holonomy over long distances cost nothing. It yields l^2-weighted bounds, which on the level-k lattice dominate sup bounds. It does **not** give fine-lattice sup bounds on lifts: those are (REG) below.

**7.4 (REG): regularity of the lift [DERIVED for the abelian identity; rest SKETCH].** Needed: N(U_k(V)) <= B eps. The obvious step iteration fails: lifting one level gives curvature at most C_s L^{-2} of the coarse value with a shape factor C_s > 1, and iterating gives (C_s / L^2)^k instead of L^{-2k}. That loss is an artefact, since the lift converges to a fixed smooth profile, but it shows the estimate must be one-shot. One-shot identity, abelian: the minimal lift has F = Pi A_k^* mu with Pi the projector on exact forms and mu = (A_k Pi A_k^*)^{-1} d_k B. By the semigroup A_k = A^{(j)}_{k-j} A_j,

    F^{(j)} = A_j F = (A_j Pi A_j^*) [ (A^{(j)}_{k-j})^* mu ].

The bracket has amplitude at most L^{-2(k-j)} ||mu||_infty, with weights Lipschitz at the scale of the coarse block, and A_j Pi A_j^* is a Calderon-Zygmund operator at level j, bounded on such slowly varying input. So |F^{(j)}| <= C L^{-2(k-j)} ||mu||_infty, uniformly in j, k. [The operator bound on slowly varying input is a sketch.] The non-abelian case is a contraction in the norm N, with this linear bound. Nonlinear means contribute Y^3, where Y_i ~ eps L^{-2(k-i)}, so their sum over levels is geometric. **Not done line by line.**

**7.5 What failed in this section, and why.**
- *Energy-only regular class.* In d = 4 the classical terms are controlled by the critical norm: |V_3| <= ||dA||_2 ||A||_4^2, and ||A||_4 <= C ||grad A||_2 uniformly in the lattice spacing, while level-j links are bounded by the local L^4 norm. So a class defined by small local energy would dispense with fine sup bounds altogether. I did not adopt it. It needs a lattice Uhlenbeck gauge, ||grad a||_2 <= C E^{1/2} from small E. The abelian case is exact, by Hodge. The non-abelian bootstrap ||grad a|| <= ||F|| + C ||grad a||^2 needs a priori smallness and a discrete continuity argument that I did not complete. Recorded as an alternative to (REG), not used.
- *Translation-invariant Laurent route.* In the abelian case (Q_k G Q_k^*)^{-1} is analytic in a strip by the usual factorisation, and zero-free by Lemma 7.1. It gives decay, but does not extend to a non-trivial background. Replaced by 7.3.
- *Step-wise (REG):* above.
- *(COER) as the hardest inequality.* I named it hardest at the start of this round. By this route the lower bound is short. So it was not the hardest, and that designation moves: see the state of attack.

**7.6 FLOW: the structure so far [BELIEVED except as marked].** By Gaussian Fubini, sum_{i < m} log Z^{(i)}(U) = log Z^{comp}_m(U), the one-loop constrained integral on the fine lattice. [DERIVED.] Let c_m be defined by: coefficient of the action in log Z^{comp}_m = 2 b_0 m log L + c_m. Then beta_m = 2 b_0 log L + c_m - c_{m-1}. The linear constraint Q_m depends only on n = L^m and not on how n factorises. [DERIVED: direct average.] So c_m has a UV part fixed by the Wilson action and an IR part from the block at scale n, up to nested-mean terms at the top levels. If |c_m - c_{m-1}| <= C_0 with C_0 independent of L, then beta_m >= 2 b_0 log L - C_0 > 0 for L >= L_0, and that is all Theorem I needs. **The claims that the log coefficient is the universal 2 b_0, and that C_0 does not depend on L, are not derived here.**

**7.7 FLOW: first attack, by sign instead of by evaluation.** The route of 7.6 evaluates beta_m. Here I tried to get the sign without evaluating anything, since the one-loop split is 4 against 1/3 in favour of the paramagnetic term, a margin of 12, so crude bounds might do.

*Exact reduction.* [DERIVED, Gaussian identity.] For the one-loop integral, Z^{comp}_m(U) = (det H_U)^{-1/2} (det Q^U_m G_U (Q^U_m)^*)^{-1/2} (det Q^U_m (Q^U_m)^*)^{1/2}, up to the gauge sector. det H_U does not depend on m, so beta_m comes only from coarse determinants of the level-m covariance and of QQ^*.

*Paramagnetic term is sign-definite at every level.* [DERIVED, second order in V = 2 ad F at fixed Q.] Let C_m be the inverse of H_0 on ker Q_m, extended by zero. Since ker Q_{m-1} is contained in ker Q_m, 0 <= C_{m-1} <= C_m as forms. The first-order term vanishes because ad F is traceless in colour and C is colour diagonal. The second-order term in log Z^{comp}_m is (1/4) Tr(C_m V C_m V). And for 0 <= C' <= C, Tr(C V C V) - Tr(C' V C' V) = Tr((C - C') V C V) + Tr(C' V (C - C') V) >= 0, because Tr(X V Y V) = ||X^{1/2} V Y^{1/2}||^2_HS for X, Y >= 0. So the paramagnetic part of log Z^{(m-1)}(U) is nonnegative at every level, on the lattice, for every L and every m, and its sign is the asymptotically free one: it lowers 1/g^2 going to coarser scales. No perturbative constant enters this statement.

*Where the route stops.* Three other contributions at the same order have no such sign, and I have no bound on them yet.
1. Diamagnetic: the second order in a of -D^2, with the ghost. Kato gives the sign of the whole diamagnetic determinant, but I need an upper bound on its coefficient per level, and the operator-monotone argument does not apply to it, because the first-order term in a is present and enters with the opposite sign.
2. Constraint variation: Q^U depends on the background at first and second order, and in the nested map this depends on L at the top levels. Gauge invariance ties it to the rest only through the Ward identity.
3. The lower bound on the size of the paramagnetic term: Tr((C_m - C_{m-1}) V (C_m + C_{m-1}) V), which should be of order log L ||F||^2 in the normalisation of the action. I expect this from the momentum range 1/n to L/n, not proved.

So this gives a sign for one term and not an inequality for beta_m. **Failed as a proof of FLOW.** What it does establish is that the only possible obstruction to beta_m > 0 is items 1 and 2. Next try: constant abelian background in U(1) inside SU(2), where neutral modes decouple and charged modes have an explicit Landau spectrum, and compute both items there, since Ward identities make the coefficient obtainable at constant F.

**7.8 Hostile pass on Section 7.** (a) Lemma 7.1 is for the linearised map only: its strength at non-trivial U rests on the weights being positive up to 1 + O(Y), which is sketch. (b) The inf-sup in 7.3 uses Q_str, with coarse gauge quotiented; in a non-trivial background the quotient is by the covariant version, not checked. (c) In 7.2 the fine-level gauge term tau D_U D_U^* is a device: the actual measure has Balaban-type gauge fixing at each level, and that the fine form computes the level-k covariance is argued only through the push-forward, not written. (d) The operator bound in 7.4 is the crux of (REG) and is a sketch. Calderon-Zygmund on slowly varying input needs the commutator with the weights to be summable over scales, which I checked only by scaling. (e) (5.5) is on real fields, and it says nothing on the complex class. Complex bounds come from analyticity of the exterior only. (f) None of the numerics tested the final map.
