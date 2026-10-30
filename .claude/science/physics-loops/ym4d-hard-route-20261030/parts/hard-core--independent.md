lead: Anthropic/claude-opus-5-5/max 97c171d6-e01d-4994-bd7b-9cb6c6972d86
lease_until: <driver sets this>

## State of attack

**Formulation.** Hard-constraint block RG for SU(2) Wilson on a periodic 4-torus, with the quaternion-mean average with waypoints and a field-chosen base point (Text 1, 5.1, 5.4). This map is defined on the whole compact field space, it pushes Haar exactly to Haar, it gives a Markov kernel mu_W on the fields, and its linearisation is exactly the paired-contour Q of (R4). The induction is I(k) of Text 3.3: a sum over families of frozen islands, plus a small-field form on the complement. An island is recycled into the small-field polymers as soon as it is smaller than a block, the surrounding coarse field is eps_0-regular and no large fluctuation is next to it.
The vacuum is subtracted exactly by rho_k(trivial coarse field), which is also the named subtraction for UV-EXT.

**Order of constants.** Text 3.1: L; kappa, M; eps_0; eps_1 <= eps_0 / (4 L^2); m_R, eps_rule; E_0, B_0, alpha_0, alpha_1; r(g); gamma. FLOW is a hypothesis, not an input.

**What is derived and what is believed.**
- Derived: Lemma 1.1, Corollary 1.2, identity (1.2), Lemma 2.1, the linearisation in 5.1, identities (5.1)-(5.2), the removal of the star in 5.3 under its hypotheses, the real-s bound in Text 6 given Theorem I, Lemmas 7.1, 7.2, Theorem 7.3, the star removal for q_k, the symbol bound QQ^* >= 1/3, the Fubini identity and the n-dependence in 7.6, the sign of the paramagnetic term in 7.7, (8.1), (8.2), b, Lemma 9.3 off the star, the linear lift bounds in 9.4, the tree gauge.
- Derived at sketch level: (5.4), (5.5), (EX) up to nonlinear remainders, the tree count in 4.5, 7.2, 7.3, non-abelian 7.4, 9.5, 11.2.
- Derived given stated inputs: Proposition 11.1, given (REG) and per-polymer invariance.
- Believed, not proved: (SF3), the non-abelian part of (SF1), (CL) near frozen data, |c_j| <= C_0 and hence FLOW. **Theorem I is a target. It is not proved.**
- Sketch only: Text 10.2, one-shot Newton.
- Numerics. (i) `checks/hard-core--independent_defect_gain.py`, earlier line-averaged map, flat background: PASS-SHEET with max S = 1.000 at L = 3, 5, 7; single links at L = 3, 5 only, since L = 7 was stopped, so PASS-GENERIC is not evaluated at L = 7. **Those runs did not hold the numeric lock:** another push held it, my acquire failed, and I had piped its output through tail, which hid the failure. (ii) `checks/hard-core--independent_lift_form.py`, under a confirmed lock: see Lemma 10.1. (iii) `checks/hard-core--independent_field_ineq.py`, final map D3, under a confirmed lock, at L = 3, 5: PASS-55, max Ratio 1.000 and 0.999 against bounds 12.6 and 15.2, in the SHEET family; CHARGE exact to 2e-16; RULE-EFFECT below. These families can falsify (5.5). They do not confirm it on all fields, and no adversarial search was run.
- RULE-EFFECT, TUNED2 on noise: with base fixed at y, min |m| falls to 0.005 to 0.012 at L = 3 and to 0.001 to 0.009 at L = 5; with the rule it stays near 0.56 and 0.73. |W - 1| is larger with fixed base by a factor of 8 to 9 at L = 3. At L = 5 the three seeds give factors 0.6, 21 and 1.7, so the first seed goes the other way. The rule does not lower |W - 1| on every sample; what it reliably does is keep |m| away from zero, which is the hypothesis of 5.3. All ratios are far below the bound here, since the noise inflates the right side. Three seeds per L are a small sample.

**The large-field answer so far.** Large-field regions regenerate the hypotheses, conditionally on the frozen statements, and without any condition on c_F beta. The unrenormalised per-level count diverges (Proposition LF-count), but nothing in this scheme sums that quantity. An isolated fine core does not survive to a coarse level (DEC), so the sum over unrecycled shapes is a tree sum with bounded entropy per node. The divergent part is the vacuum part of the recycled gas, and it is cancelled by the named subtraction. I do not claim this is Balaban's R operation: his bodies could not be read (Project Euclid and Deep Blue both served bot checks, and I stopped there).

**Hardest remaining inequality.** (LOC-NA) together with the per-polymer gauge invariance on which Proposition 11.1 stands. Precisely: with V eps_0-regular at level k, sup_p |F_p(U_k(V))| <= C eta^2 sup |d_k V| and the Holder modulus of F at scale eta^{-1}, uniformly in k, near frozen data, for complex V in a fixed disc. It is consumed by (SF1), (CL), (EX), 11.1 and 11.2, while Text 10.2 has it only as a sketch. Every other small-field item now has a route that reduces to it.

**Routes tried and why they failed** (Text 1.5, 2, 5.4, 7.5, 9.7, 10.3): one-link solve (variance grows linearly with level); entire reference-path average (rough path keeps full weight; fine action no longer dominates at large curvature); line-averaged prefix (star cancels only approximately at large field); iterating the fiber flow for complex bounds (L^2 per level); one-function pointwise induction on all V (entropy compounds unless an excess lemma is proved for arbitrary fields, replaced by frozen islands); pricing a tower at tuned block centres (needed a density bound I could not prove, replaced by the field-chosen base point of 5.4); two thresholds in recycling (non-analytic indicator, removed); stepwise regularity of the lift (shape factor compounds, replaced by the one-shot bound of 9.4); energy-only regular class (needs a lattice Uhlenbeck gauge I did not prove; set aside away from the trivial background); direct sign analysis of beta per level (dia and constraint terms have no sign; superseded by the telescoping (8.2)); L-free composite bound on rough inputs through the star (L^{1/2} loss, recorded); level-by-level Whitney starting guess (F jumps across faces, logarithm at the first Newton step, replaced by glued linear lifts); bootstrap from the stepwise bound (holonomy eta^{-c'} eps, no patch gauge at block scale).

**Next action.** Write the linear statement near frozen data (a version of 9.4 with Dirichlet part), then the one-shot Newton of 10.2 with its norm. Settle 11.4 (b), gauge invariance of individual polymers, since 11.1 rests on it.

## Obligations
- gap: (LOC-NA) non-abelian background and Hessian near a regular field, with frozen boundary: the glued starting guess and one-shot Newton of Text 10.2, not written line by line; items of 10.4 -> (SF1), (SF3), (SF4), (EX), (CL)
- unchecked: |c_j| <= C_0 with C_0 depending on d only: low-momentum expansion of T_3, T_4 and per-site traces, given (R4), Ward identities and 9.4 (Text 9.5) -> (8.2)
- implication: (FLOW) for L >= L_0, beta in [(b/2) log L, 2 b log L], given |c_j| <= C_0 and (SF3) for the O(g^2) -> Theorem I hypothesis, trajectory in UV-EXT
- gap: exact form of I(k), Mayer polymer with multi-body boundary terms (Text 3.3, 4.4, 5.6 item 5) -> Theorem I
- gap: (EX) with nonlinear remainders on the real fiber (Text 5.5) -> I(k+1)(d)
- gap: (SF3) fluctuation integral with white-noise cut p(g), mid-field gas up to eps_1, frozen boundary, bulk polymers independent of boundary (Text 9.6, 11.2, 11.3) -> I(k+1)(b)
- gap: per-polymer gauge invariance after localisation (Text 11.4 b) -> Proposition 11.1
- implication: (SF4), Proposition 11.1, irrelevance by Fock-Schwinger gauge polymer by polymer, given (REG) with Holder modulus and per-polymer invariance -> I(k+1)(b), uniform bound (3.3)(b)
- gap: rerun the field-inequality check on the final map D3; so far the script tests the earlier line-averaged map, and the lock was not held -> confidence in (5.5)
- unchecked: lattice Sobolev on a torus and zero-mean handling per tube, given Gagliardo-Nirenberg on Z^4 -> Lemma 9.3, 9.5
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
- discharged: one-loop telescoping identity (8.1) on covariantly constant backgrounds -> (8.2)
- discharged: coefficient b = 11/(3 pi^2), continuum heat kernel -> (8.2)
- discharged: Lemma 9.3 off the star, non-compounding second derivative of the composite map -> 9.5
- discharged: linear lift bounds free of L, given the upper bound on q_n -> (REG), 9.5
- discharged: maximal tree gauge, trivial Jacobian at every field -> (SF3)
- discharged: ultralocal cluster expansion, proved in library/ultralocal_cluster_expansion.md with credit to Dimock and Balaban -> 11.2
- discharged: Lemma 10.1, two-sided bound on the abelian perfect form, every n -> 9.4, 9.5, normalisation in Text 6

## Requests
- FROM TARGET LEAD, gate on UV-CT (`git show origin/claude/ym4d-hard-route:.claude/science/physics-loops/ym4d-hard-route-20261030/gates/uv-ct-upper-chain-41489e4876.md`; same-model): CT3 carries all the separated content, since in the Gaussian family only CT3 fails. E is not free: Jensen forces E close to log G in L^1. CT4 is equivalent to p_P - p_infinity <= c_F (a/a_*)^4 and, by a mode count not yet checked, fails at Gaussian order by log log(1/a) unless two-loop running of the zero-mode factor rescues it. So treat CT4 as non-Gaussian. CT1 at complex sources is the least tested clause.
- FROM TARGET LEAD, 2026-10-30: the interface changed from UV-EXT to UV-CT; see `git show origin/claude/ym4d-hard-route:.claude/science/physics-loops/ym4d-hard-route-20261030/GOAL.md` and `git show origin/claude/ym4d-hard-route:.claude/science/physics-loops/ym4d-hard-route-20261030/parts/upper-chain.md`, Requests and Text section 7. Answer to your real-s request: a constant real shift cannot feed the chain, whatever the subtraction (upper-chain Theorem 4). A real form exists at position-dependent real bump sources with a two-sided bound (Theorem 7.8), and it gives normalized exponentials rather than the linear field. Your named subtraction at constant coupling now feeds only CT4. The UV-CT wording traces partly to the Sussman-Alpoge account through the mapped attempt; use the interface, and keep your charter's limits on what you read.
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

**7.4 (REG): regularity of the lift [abelian: superseded and done in 9.4; non-abelian SKETCH].** Needed: N(U_k(V)) <= B eps. The obvious step iteration fails: lifting one level gives curvature at most C_s L^{-2} of the coarse value with a shape factor C_s > 1, and iterating gives (C_s / L^2)^k instead of L^{-2k}. That loss is an artefact, since the lift converges to a fixed smooth profile, but it shows the estimate must be one-shot. One-shot identity, abelian: the minimal lift has F = Pi A_k^* mu with Pi the projector on exact forms and mu = (A_k Pi A_k^*)^{-1} d_k B. By the semigroup A_k = A^{(j)}_{k-j} A_j,

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

### 8. FLOW by telescoping: the sign without per-level evaluation

Credit: the background-field structure of the coupling recursion is Balaban's CMP 109 (1.3), (1.4), (0.20) as transcribed in NOTES section 9 (LANE-READ). The diamagnetic and paramagnetic split at constant field is Nielsen and Hughes. The telescoping below is derived here.

**8.1 Exact one-loop identity [DERIVED].** Let F_j be the classical functional, F_{j+1}(W) = min over Fib(W) of F_j(V), the tropical recursion (exact, with F_0 = A). Let V^* be the minimiser and H_L = Hess F_j(V^*) - mu . Hess M the Hessian of the Lagrangian, with mu the multiplier. By Legendre duality, Hess F_{j+1}(W) = (Q^U H_L^{-1} (Q^U)^*)^{-1}. By the Fourier representation of the delta function,

    int dB delta(Q^U B) exp(-(1/2) <B, H_L B>) = (2 pi)^{(N - d)/2} (det H_L)^{-1/2} (det Q^U H_L^{-1} (Q^U)^*)^{-1/2} = (2 pi)^{(N-d)/2} (det H_L)^{-1/2} (det Hess F_{j+1}(W))^{1/2}.

No separate Jacobian appears: the weights of Q^U are inside Hess F_{j+1}. On covariantly constant backgrounds mu vanishes with D^* F, so H_L = Hess F_j. Gauge directions go through the exact factorisation of the orbit integral: [dB_j / G_j] = [dW / G_{j+1}] [fiber / G_{j,0}]. Define L_j(V) as the one-loop gauge-invariant integral of Hess F_j. Then

    log Z^{(j)}(U) = L_j(V) - L_{j+1}(W),                                                                                   (8.1)

so the one-step fluctuation determinant is a **difference of two copies of one functional at adjacent levels**. The sum over levels telescopes. This replaces the direct sign analysis of 7.7: items 1 and 2 there no longer appear separately, since the variation of the constraint is inside Hess F_{j+1}.

**8.2 The coefficient b [DERIVED, continuum, formal in the usual heat-kernel sense; the value agrees with the known one-loop coefficient].** Take SU(2), background F_12 = B_ad on the charged components, i.e. link U = exp(i theta sigma_3) with B_ad = 2 curl theta, so that the action density of A = sum_p (1 - (1/2) tr U_p) is B_ad^2 / 8. A complex scalar of charge 1 has K(t) = (16 pi^2 t^2)^{-1} (B t / sinh B t). In Feynman gauge the charged vector has spin shifts +2B, -2B and two zero shifts, and the charged ghost enters twice with the opposite sign. So with mass mu,

    X = int (dt / t) e^{-mu^2 t} K(t) [ 2 + e^{2 B t} + e^{-2 B t} - 2 ] = int (dt / t) e^{-mu^2 t} K(t) 2 cosh(2 B t),

and the B^2 term is (B^2 / 16 pi^2)(4 - 1/3) int dt / t e^{-mu^2 t}, which is (11/3)(B^2 / 8 pi^2) log(1 / (mu a)). In terms of A this is

    X = b log(1 / (mu a)) * A,    b = 11 / (3 pi^2) = 0.3715...,

the 4 being paramagnetic and the -1/3 diamagnetic. Check: in this normalisation 1/g_B^2 runs at the rate 4 N b_0 = 11 N^2 / (12 pi^2) at N = 2, as recorded in the program's Proposition LF-count.

**8.3 Formula for beta [DERIVED given 8.4].** Suppose that on a torus of side T_j in level-j units, L_j(V) - L_j(1) = (b log T_j + c_j + o(1)) A(U) on smooth small backgrounds, with c_j the finite part. Since T_j = L T_{j+1} and by CMP 109 (1.3) beta_{j+1} is the coefficient of A in log Z^{(j)}(U) - log Z^{(j)}(1), (8.1) gives

    beta_{j+1} = b log L + c_j - c_{j+1}.                                                                                  (8.2)

So **FLOW holds for L >= L_0 := exp(4 C_0 / b), as soon as |c_j| <= C_0 for all j, with C_0 not depending on L.** Then beta_{j+1} lies in [(b/2) log L, 2 b log L]. For the large-L choice this is compatible with the order of constants: L comes first, and every other constant may depend on it. The sign comes entirely from b > 0, an explicit computation at the universal low-momentum operator. The non-universal parts only have to be bounded. Higher loops are O(g^2) in beta, and the recycled gas is smaller still, both controlled by g <= gamma: conditional on (SF3), (SF4). The one-loop part of the level sum is 1/g_0^2 - 1/g_m^2 = b m log L + c_0 - c_m + O(sum g^2), which is the form (0.31).

**8.4 What |c_j| <= C_0 requires (CLASS-4), and why C_0 can be free of L.** c_j is a one-loop quantity on the level-j lattice in level-j units. Split momenta at p_0 small. Below p_0: Hess F_j at low momentum is the universal operator -D^2 - 2 ad F, because (R4) reproduces constant curvature exactly, with no factor, and gauge invariance fixes the cubic and quartic vertices at leading order. The corrections are suppressed by |p|^a, so the low part converges to b log(1/mu) plus a bounded constant. Above p_0: it needs a bound on the propagator and the vertices up to fourth order, at the trivial background.
- Propagator: by Lemma 7.1, the quadratic form is at least ||d_j B||^2 with constant exactly 1, so with a Feynman term the propagator is at most 1 / p-hat^2. No L. [DERIVED.]
- Linear lift: Q_j depends only on n = L^j. [DERIVED.] So the quadratic form depends on n only, and not on how n factorises.
- Vertices: Section 9.

**8.5 Hostile pass on Section 8.** (a) Formula (8.1) is exact on covariantly constant backgrounds, while (SF4) extracts beta at momentum q -> 0 from a plane wave. Equality of the two coefficients is by gauge invariance, argued and not written. On non-constant backgrounds mu != 0 adds a term linear in mu, of higher dimension. (b) On a torus, constant non-abelian background needs a quantised flux, so the extraction needs T large; c_j is defined as a limit. (c) The neutral sector and torus zero modes appear equally in L_j and L_{j+1} and cancel, at leading order; not checked at second order in B through the nested means. (d) At low momentum the claim that Hess F_j is universal rests on F_j being close to the continuum action on smooth fields, uniformly in j. That is (CLASS-4). (e) I have not computed C_0, so L_0 is not explicit, and if C_0 did depend on L, for instance as a power, (8.2) would prove nothing. That is the point that must be attacked next. (f) The claim is one-loop plus O(g^2): the O(g^2) needs (SF3).

### 9. Vertices of the classical functional in the critical norm: constants free of L

Attack on (e) of 8.5. In d = 4 the L^4 norm of a 1-form is scale invariant. I use it to bound the nested map and the vertices of F_j at the trivial background, in a way that does not compound through levels and does not see L. This is the route set aside in 7.5, now used only at the trivial background, where no Uhlenbeck gauge is needed.

**9.1 One-step expansion [DERIVED].** Let V = exp(iB) on T_i. For a flat mean over paths pi with independent waypoints, T_pi = exp(i X_pi) with X_pi = sum_{b in pi} B_b + (i/2) sum_{b < b'} [B_b, B_b'] + ..., and M = m / |m| = exp(i Y) with Y = avg X + O(X^3): the second-order scalar in m is absorbed by the normalisation. The nesting of a_u, b_u inside the mean over u has the same form, with the prefix and suffix chosen independently. So Y_2(c) = (i/2) avg_pi sum_{b < b'} [B_b, B_b'], and

    |Y_2(c)| <= (1/2) avg_pi ( sum_{b in pi} |B_b| )^2 <= C L avg_pi sum_{b in pi} |B_b|^2 = C L sum_b P(b in pi) |B_b|^2.

Off the block-centre star, P(b in pi) <= C L^{-3}. So |Y_2(c)| <= C L^{-2} ||B||^2_{l^2(hull c)} <= C ||B||^2_{l^4(hull c)}, since the hull has order L^4 links. In the same way, |Y_n(c)| <= C^n L^{n - 4} ||B||^n_{l^4(hull c)} for n >= 4, and n = 3 has no positive power of L. So the terms with n <= 4 are free of L, and the series converges for ||B||_{l^4(hull)} << 1/L. Squaring and summing over c: ||Y_2||_{l^2(T_{i+1})} <= C ||B||^2_{l^4(T_i)}.

**9.2 Two scale facts [DERIVED].** For a level-i link variable, Cauchy-Schwarz along the tube gives ||Q^{(r)} b||_{l^2(T_{i+r})}^2 <= 2 L^{-2r} ||b||^2_{l^2(T_i)}, and Holder gives ||Q^{(i)} a||_{l^4(T_i)} <= C ||a||_{l^4(T_0)}, with C depending on d only. The first says that a term born at level i is damped by L^{-1} per level on the way up. The second says that the critical norm does not grow on the way up.

**Lemma 9.3 (non-compounding second derivative of the composite map) [DERIVED off the star].** ||d^2 M^j (a, a)||_{l^2(T_j)} <= sum_{i < j} sqrt 2 L^{-(j - i - 1)} C ||Q_i a||^2_{l^4(T_i)} <= C' ||a||^2_{l^4(T_0)} <= C'' ||grad a||^2_{l^2(T_0)}, the last step in Landau gauge by the lattice Sobolev inequality. C'' depends on d only: not on j, and not on L. **This is the one-shot statement the level-by-level approach could not get.**

*The star.* Near y, P(b in pi) is about dist(b, y)^{-3}, and 9.1 does not apply as written. By 5.3 the star through y is a common left factor, so it enters as a gauge transformation at the coarse site, up to a cross term of size (dispersion of the star) x (dispersion of the star-free part). Crudely that cross term is at most L^{1/2} ||B||^2_{l^4(hull)}: dispersion of the star at most (L sum_b dist(b,y)^{-3} |B_b|^2)^{1/2}, and sum over b of dist^{-6} converges. **So Lemma 9.3 has an L^{1/2} loss on general inputs through the star.** On smooth lifts the cross term is of order (xi L)^4 in the gauge vanishing at y, with no loss. Consequence: on rough a the star term is not free of L, and no consumer may use Lemma 9.3 with an L-free constant on rough inputs. The consumer in Section 8 uses it only on smooth lifts.

**9.4 Lift bounds, free of L [DERIVED given the upper bound on q_n].** The lift for a level-j link depends only on n = L^j, in the linear theory. Since Q_str has weights n^{-3} on a tube, the constrained equation is Delta a = Q_str^* mu, with mu on the level-j lattice. Poincare at block scale n has a constant depending on d only, so Combes-Thomas gives |mu(c)| <= C exp(-delta d(c, c_0)) for a unit source at c_0, with C and delta depending on d only. Then, with the lattice Green's function bound |grad G(x)| <= C |x|^{-3},

    |grad a(x)| <= C int_{|y| <~ n} |x - y|^{-3} n^{-3} |mu| <= C n^{-2} exp(-delta d),    |a(x)| <= C n^{-1} exp(-delta d),

and level-i curvature obeys |F^{(i)}| <= n_i^2 sup |F| <= C (n_i / n)^2 by the row sum. **This replaces the Calderon-Zygmund step of 7.4:** the source Q_str^* mu is bounded, since only in-plane derivatives of the tube weight enter, and so grad G * source is an order-one smoothing, with no logarithm at the block faces. The second difference of a does have a logarithm at the faces, but only F and J = Q^* mu enter (1.2) of CMP 109, and J is bounded. So (REG) at the linear level is done, with constants free of L. Fields far away are handled in a coarse gauge adapted to x, where B grows polynomially against the exponential decay.

**9.5 Vertices at the trivial background (CLASS-4) [SKETCH].** F_j(exp(iB)) = (1/2) <B, Delta_n B> + T_3 + T_4 + ... , with a = H_n B:
- T_3 = V_3(a, a, a) + <mu, d^2 M^j(a, a)>. |V_3| <= ||da||_2 ||a||_4^2 <= C ||grad a||^3_2, by Sobolev. Also ||mu||_2 <= C ||B||_2 and 9.4 for the second term.
- T_4 is the same with one exchange term through the fine conditional propagator, which is bounded in the energy norm.
All constants are free of L and of j, on smooth lifts. Per-site traces come from the same bounds together with the exponential locality of 9.4. So the high-momentum part of c_j is bounded by a constant depending on d only. In the low-momentum part, the correction to the universal operator is O(|p|^a), since (R4) is exact at p = 0 and has a p^2 correction, and it integrates against d^4 p / p^4 to a bounded constant. **Hence |c_j| <= C_0 with C_0 depending on d only, and therefore FLOW for L >= L_0.** That sentence is a sketch: the low-momentum expansion of T_3, T_4 has not been written out, and the Ward identity is what fixes the leading vertices.

**9.6 Other items settled in passing.**
- *Gauge fixing in exterior blocks [DERIVED].* Maximal tree gauge in each L-block, based at the block centre: for a gauge-invariant integrand, setting tree links to 1 has trivial Jacobian on Haar measure, at every field, rough or not. So there is no Faddeev-Popov determinant and no Gribov problem. Frozen neighbours do not matter, since the tree is per exterior block, and Lemma 7.2 runs with g = 0 on the tree. The tree breaks the lattice symmetry of individual polymers but not of the integrated function, so polymers are symmetrised after integration. This replaces the exponential gauge of CMP 109 (0.14).
- *Two-tier fluctuation cut [DERIVED as a scheme].* Theorem 27 of Dimock I (ultralocal cluster expansion, which I read) needs H_0 small, which fails on the whole range |B| < eps_1, where the cubic term reaches eps_1^3 / g^2. So use the white-noise cut |W| <= p(g), p(g) = (log 1/g)^{p_0}, for the expansion, as Dimock does. A mid-field cell, with p(g) < |W| and |B| < eps_1, is an island with activity at most exp(-p^2 / 2) and no compact-integral loss, since the Gaussian is normalised. It is always recyclable next to a regular field. Beyond eps_1 is type Z. The marginal shift from mid-field cells is at most sum_k exp(-p(g_k)^2 / 2), which converges for 2 p_0 > 1 along the flow, and it is far below g^4. Statement (SF3) is amended accordingly.

**9.7 What failed in this round.**
- *L-free constants through the star on rough inputs:* the crude bound has L^{1/2}, above. Not needed for FLOW. It is an open point for any later use of a composite estimate on fluctuating fields.
- *Direct per-level sign analysis of 7.7:* superseded by (8.2).
- *Calderon-Zygmund in 7.4:* replaced by 9.4. My first reading feared a logarithm from the jumps of the box weight. Only in-plane derivatives enter d^* of a (mu nu) form, so the source is bounded.

**9.8 Hostile pass on Section 9.** (a) Sobolev on a torus needs zero mean; constant modes are excluded by the constraint on ker Q_j, but a lift is not in ker Q_j. Handled per tube only in outline. (b) In 9.4 the Green's function bound and Combes-Thomas together give pointwise bounds only because mu lives on the coarse lattice. For the fine conditional propagator itself, no pointwise bound is claimed. (c) The upper bound on q_n by a dual-basis lift is still unchecked and is consumed in 9.4, 9.5. (d) 9.5 is at the trivial background. The non-abelian contraction near a regular background is still a sketch (7.2, 7.4). (e) For j small, for example j = 1 with L large, the fine Wilson lattice is close to the continuum on a block, and c_1 is near its limit. For j = 0, c_0 is the Wilson lattice constant, a finite number. No uniformity problem appears there, but I have not computed either. (f) n <= 4 is free of L, but the analyticity radius in the critical norm is of order 1/L, so alpha_1 depends on L. This is allowed by the order of constants, but it means eps_0 is much smaller than any power of 1/L that I have written down. And (8.2) must not use anything that depends on eps_0: C_0 is defined at the trivial background, and it does not.

### 10. Upper bound on the lift form, and (LOC-NA) by one-shot Newton

**Lemma 10.1 (two-sided bound on the perfect form, abelian, every n) [DERIVED].** ||d_j B||^2 <= q_n(B) <= (pi^2 / 4)^6 ||d_j B||^2, about 226 ||d_j B||^2.

*Proof.* Lower bound: Lemma 7.1. Upper bound: in Feynman form on the coarse level, Q_str is diagonal in direction, so the coarse covariance is diagonal, G_mu(P) = n^{-2} sum_m prod_i D_n(p_i)^2 D_n(p_mu)^2 / phat(p_m)^2, and Landau differs from Feynman on the coarse level only by a coarse gradient. So q_n(B) <= B_perp^* G^{-1} B_perp, with B_perp the part of B orthogonal to chat. Keep only the alias m = 0: |n p_i / 2| <= pi / 2 gives D_n(p_i)^2 >= (2 / pi)^2, since sin x / (n sin(x / n)) >= sin x / x >= 2 / pi there, and phat^2 <= p^2 = P^2 / n^2. So G_mu(P) >= (4 / pi^2)^5 / P^2. And ||d_j B||^2 = |chat|^2 |B_perp|^2, with |chat|^2 >= (4 / pi^2) P^2.  []

*Numerics, under the lock, script* `checks/hard-core--independent_lift_form.py`*, criteria stated first:* PASS-LOWER, with min R = 1 up to rounding at n = 1, 3, 9, infinity. PASS-UPPER, with max R = 6.45, 11.03, 12.2 at n = 3, 9, infinity, attained at P = (pi, pi, pi, pi); cutoffs 8 and 12 agree within 0.04 percent and grid against random within 2.5 percent. R -> 1 as P -> 0, as (R4) requires. These are float searches, and they only serve as a check of the lemma, whose constant 226 is crude against 12.2. The lemma holds with no dependence on L.

**10.2 (LOC-NA) [SKETCH, every step named; nothing here is line by line].** Target: for V eps_0-regular at level k, there is a unique fine U = U_k(V) in the class N(U) <= B eps with M^k(U) = V and the Euler-Lagrange equation, analytic in V, and with Hessian and kernel bounds, all with constants uniform in k. Three pieces.

(a) *Starting guess, one-shot.* On a patch of M' level-k cells, V is near flat: in a patch gauge V = exp(iv) with |v| <= C eps M'. Take the exact linear lift H_n v of 9.4 in that patch, so F and J are bounded with the right scales and the Euler-Lagrange equation holds exactly at the linear level. Adjacent patches: Q_str(d Lambda) = d_c(avg Lambda), so two patch lifts agree up to a fine gauge transformation with avg Lambda = lambda, the coarse transition, up to nonlinear terms O(eps^2 M'^2) and tails exp(-delta M'). Glue with a partition of unity at scale M' n. The errors are of relative size eps M'^2 + exp(-delta M'), including in J. [Sketch. Linear part from 9.4.] So N(U_0) <= C eps, with a residual relatively small against eps.

(b) *One-shot Newton.* Norm: rho(U) = sup |F| / eta^2 + sup |J - Q^* mu| / eta^3 + (residual of the constraint), for the current multiplier mu. Step: U' = exp(ia) U, where a solves the linear saddle problem at U with the current residual as source. On the class N(U) <= 2 B eps, each block hull is near flat, with holonomy of order eps L^c, so local bounds hold in a patch gauge by perturbation of 9.4. The sum over patches comes from the covariant Combes-Thomas of 7.3, which chooses no gauge. So |a| <= C eta rho, |grad a| <= C eta^2 rho. Remainders: the classical one is of order |a| |grad a| = eta^3 rho^2, against J at scale eta^3. The constraint one is d^2 M^k(a, a), at most C rho^2 by the smooth-input estimate of 9.1 and 9.3, with no compounding. So the residual part of rho obeys rho' <= C rho^2, the iteration converges from the small residual of (a), and the total move is at most C eps. The linear operator is inverted once per step, at the composite level: **no level iteration occurs anywhere in (b).**

(c) *Where near-flatness is used, and where it is not.* A patch gauge is only used over one block hull, and only to pass from the l^2 bounds of 7.2, 7.3 to pointwise bounds by interior elliptic estimates. Long-distance holonomy never enters, since the weighted bound is gauge free. This combines the two tools named in the hardest-inequality statement. On the class N, sup bounds are given, so no Uhlenbeck gauge is needed.

**10.3 What failed.**
- *Level-by-level Whitney interpolation as the starting guess.* Whitney has shape factor exactly 1, which removes compounding in sup |F|. But Whitney F jumps across cell faces, so J = D^* F contains surface measures at fine scale, and order-one smoothing of a surface source leaves a logarithm of 1/eta near the faces at the first Newton step. Found by the hostile pass, and it would have put a level-dependent factor in the class N. Replaced by the glued linear lifts in (a), whose source Q^* mu is bounded.
- *Bootstrapping from the stepwise bound.* If only (C_s / L^2)^{k-j} is available, then fine curvature is at most eta^{2 - c'} eps with c' = log C_s / log L, and the holonomy of a level-k loop is at most eta^{-c'} eps, not small at large k. So a patch gauge at block scale is unavailable from the stepwise bound. A Campanato iteration from smaller patches might repair it, but I did not write the lattice harmonic comparison. (a) makes it unnecessary.
- *Uniqueness among all critical orbits.* Convexity from 7.2 gives uniqueness only on the slice |B| < eps_1 and in the regular class. Global uniqueness is neither claimed nor needed: rough lifts are islands.

**10.4 Hostile pass on 10.2.** (a) In the gluing, the patch lifts agree only up to gauge. The fine gauge transformation with prescribed block averages is not unique, and its choice must not introduce fine-scale roughness: take Lambda as the linear lift of lambda, smooth at scale n. Not written out. (b) The class N controls curvature, and the iteration keeps J in the form Q^* mu, with a bound from the coarse multiplier; the nested Q^U has weights differing from Q by 1 + O(Y), so Q^{U*} mu is bounded but its bound must be rechecked at the top levels, where Y is largest. (c) Complex V: the analyticity radius of the whole construction has not been traced. (d) The class N is stated for fine fields. Fluctuation fields at level k are not in it. Only backgrounds are. (e) Frozen boundary: the patch construction near a frozen island has not been done; Lemma 1.1 removes the constraint from mixed bonds, but the linear lift with a Dirichlet part needs its own version of 9.4.

### 11. Irrelevance by Fock-Schwinger gauge, polymer by polymer (a route without the Ward hierarchy)

Target: (0.28)-(0.29) of CMP 109 for this scheme, which is the content of (SF4), together with the closure of the polymer bound. CMP 109 Sections 4 and 5 (LANE-READ) reach it by a fifth-order expansion in local coordinates and Ward identities relating orders. The route below does not use them: each polymer is gauge invariant separately, so it can be evaluated in a gauge centred on itself.

**Proposition 11.1 (irrelevance) [DERIVED given (REG): N(U) <= eps and Holder control of F].** Let E(X; .) be functions on level-j fields on X such that: each is invariant under gauge transformations on X; each extends analytically to sup_b |log V(b)| < alpha_1; |E(X; .)| <= E_0 exp(-kappa d_j(X)) there; E(X; 1) = 0; and the family is covariant under level-j translations and the hypercubic group. Let V_j = M^j(U) with U at level k, xi = L^{j-k}, and level-j curvature phi <= xi^2 eps on the hull. Then there is a number beta(E), the second moment of the family, with

    sum_X E(X; V_j) = beta(E) A(U) + sum_X V(X),     |V(X)| <= C xi^{4 + alpha} exp(-kappa' d_j(X)),   any alpha < 1,

where C depends on E_0, kappa, alpha_1, and eps and not on k or j.

*Proof.*
1. *Large X.* Let D = diam X. If C D phi >= alpha_1, then d_j(X) >= c alpha_1 / (M xi^2 eps), and exp(-kappa d_j(X)) is smaller than any power of xi.
2. *Gauge.* Otherwise, transform by axial transport from a site of X. A link b is then the holonomy of a loop around a surface of area at most C D, so |v_b| := |log V'(b)| <= C D phi, and v is in the disc of analyticity.
3. *Taylor at the identity.* The constant term vanishes. The linear term is <c, v> with c invariant under constant colour rotation, because constant gauge transformations act on X; the adjoint has no invariant vector, so c = 0. The remainder after second order is at most E_0 exp(-kappa d) (C D phi / alpha_1)^3, of order xi^6 exp(-kappa' d).
4. *Second order.* v_b = sum over the surface of parallel-transported F_p. Replacing transports by 1 costs a relative C D phi. Replacing F_p by its value F_0 at the base site costs a relative Holder modulus (D xi)^alpha. So the quadratic term is c^X(F_0, F_0) + O(xi^{4 + alpha} exp(-kappa' d)), with c^X(F_0, F_0) := Pi^X(a[F_0], a[F_0]), a[F_0] the axial potential of a constant field.
5. *Symmetry.* Sum over X with given base site. By translation covariance the form is independent of the site. Colour invariance makes it delta_{ab} on colour. A reflection of one axis flips F_{mu nu} when mu or nu is that axis, which kills F_12 F_34 and F_12 F_13. Permutations equate the rest. So it equals beta' sum_{mu < nu} |F_{mu nu}|^2, the only invariant, at the base site. **No rotation invariance and no second marginal coupling are involved.**
6. *Identification.* By the row sum and Holder, F_j(x) = n_j^2 F(x) (1 + O(xi^alpha)), so sum over level-j sites of |F_j|^2 equals sum over fine plaquettes of |F|^2 up to the same factor, which is 2 A(U) (1 + O(eps^2 eta^4)). Localise A(U) to level-j cells.  []

Steps 1 to 5 are complete at this level. Step 6 and the Holder modulus need (REG). So the gain is alpha < 1 and not Balaban's, and the expansion needs third order only. **I have not read his proof, and I do not know why he goes to fifth order; the likely reason is the regularity class he works in. Do not read this as an improvement on him until the Holder input is proved.**

**11.2 Closure of the polymer bound [SKETCH].** As in CMP 109 (1.3), polymers at level j are fixed functions: nothing is iterated. At step k, with W regular, V = exp(iB) V^*(W), U_{k+1}(W) = U_k(V^*(W)) exactly, so the values of old polymers at B = 0 are the old polymers at the new background. The new polymer is

    E^{(k+1)}(W) = [one-loop term (8.1)] + log int dmu(xi) chi exp( g^{-2} R(g C^{1/2} xi) + P(g C^{1/2} xi) ),

with C = C(W) from 7.3, xi the white noise with cut p(g), R the remainder of F_k beyond second order, and P the variation of all earlier polymers. Sizes per polymer:
- R: cubic in B through the bounds of 9.5, localised by Mobius differences with the decay of 9.4 and C^{1/2}. So |g^{-2} R(X)| <= C(L, M) g p^3 exp(-kappa d(X)).
- P: from 11.1, the variation of a level-j polymer under a level-k variation is summed over j with gain xi^alpha, after the marginal part is put in the action. So |P(X)| <= C_E eps g p exp(-kappa d(X)).
- So H_0 = C(L, M) g p^3 is small for g <= gamma. The library theorem `library/ultralocal_cluster_expansion.md` gives a polymer of the same size, with a rate kappa' a fixed fraction of kappa, paid by taking M large.
- One-loop term: differentiate in W, then use the decay of C. It is local, gauge invariant, analytic, and bounded by a constant E_0 = E_0(L, M), with **no dependence on earlier polymers**. So the polymer bound closes: E_0 does not feed back, since the only dependence on earlier polymers is through C_E eps g p, which is small.

So there is no recursion for E_0 and no recursion for C_E: C_E = C(E_0, ...) (1 - L^{-alpha})^{-1}, by 11.1 and the geometric sum in j.

**11.3 What this does not cover.** The cut functions on the white noise are not analytic in the noise, and that is fine, since W enters only through C(W), V^*(W). Near frozen data, 11.1 applies only to polymers inside Om, and the rest are boundary terms. The mid-field cells of 9.6 are not in the expansion above. They enter as islands. None of the sizes above has been checked against the Gaussian weight at the edge of the cut, where g p^3 is largest.

**11.4 Hostile pass.** (a) Step 2 uses only sup curvature on the hull of X. For rough backgrounds it fails, but polymers are only evaluated on M^j(U) with U regular. (b) Step 3's linear term vanishes polymer by polymer only if each E(X) is invariant under constant rotation. After symmetrising the tree-gauge output, invariance under gauge transformations holds for the sum and I must arrange it per polymer, by defining polymers after integrating with a gauge-invariant Mobius localisation. Not written. If per-polymer invariance fails, Step 2 also fails, so **this is the load-bearing assumption of 11.1, and it must be checked against the construction of the polymers.** Mobius differences defined by resetting links to 1 outside a set do not preserve gauge invariance. Candidate fix: reset the field in a gauge-covariant way by using a local-frame reference, or localise only in the white noise, which is gauge neutral once the background is fixed: the output is then a function of W in a fixed form, gauge invariant if W-dependence comes through gauge-invariant data of the background on X. Open as written. **Route for it:** weaken hopping between M-cubes by scalars s_c, which commute with Ad and hence preserve gauge covariance; s_c = 0 decouples the cube. Then F(s) is manifestly a function of the included field, covariantly. The parametrix sum over M-cube local inverses, whose bounds come from Text 7, gives analyticity in s to radius exp(delta M / 2). The Mobius difference M(X) = sum_{Y subset X} (-1)^{|X \\ Y|} F(1_Y) is then a finite difference of order |X| of an analytic function, so it is at most (C exp(-delta M / 2))^{|X|} sup |F|, as in Step 5 of the library proof. Each polymer so defined is gauge invariant on X. This reintroduces random walks, but only as a bookkeeping device on the level-k lattice, with covariant local inverses controlled by forms, and no local gauge choice. [Route; not carried out.] (c) Step 5 requires covariance of the family under the full hypercubic group, which D3 has only as a mixture. It holds for the sum. (d) In 11.2 the size of P assumes a level-k variation is smooth at level j: this holds for lifts by 9.4, including for B rough at level k, since lifts are smooth below the level-k scale.
