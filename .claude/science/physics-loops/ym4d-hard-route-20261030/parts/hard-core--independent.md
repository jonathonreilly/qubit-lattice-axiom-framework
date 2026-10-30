lead: Anthropic/claude-opus-5-5/max 97c171d6-e01d-4994-bd7b-9cb6c6972d86
lease_until: <driver sets this>

## State of attack

**Formulation.** Hard-constraint block RG for SU(2) Wilson on a periodic 4-torus, with the quaternion-mean average with waypoints and a field-chosen base point (Text 1, 5.1, 5.4). This map is defined on the whole compact field space, it pushes Haar exactly to Haar, it gives a Markov kernel mu_W on the fields, and its linearisation is exactly the paired-contour Q of (R4). The induction is I(k) of Text 3.3, **level-only**: r_k is one function of the current field, equal to a small-field form on the regular region Om(V) times a large-field factor G_k(V) <= exp(-c_F eps_0 Y_k(V) / g_k^2), with Y_k the l^1 norm of the rough plaquettes. There are no frozen fine variables and no histories. Rough cubes where the next field is regular go into a hard-core gas in the fluctuation integral, and so into the polymers. The vacuum is subtracted exactly by rho_k(trivial coarse field); with a source this is the counterterm E of UV-CT (Text 6).

**Order of constants.** Text 3.1: kappa, M absolute; then L >> M; then eps_0 = c_1 L^{-2}; alpha = c_2 eps_0; eps_1 = eps_0 / (4 L^2); p(g); then gamma. FLOW is a hypothesis of Theorem I, supplied by Text 8 for L large.

**What is derived and what is believed.**
- Derived: Lemma 1.1, Corollary 1.2, identity (1.2), Lemma 2.1, the linearisation in 5.1, identities (5.1)-(5.2), the removal of the star in 5.3 under its hypotheses, the real-s bound in Text 6 given Theorem I, Lemmas 7.1, 7.2, Theorem 7.3, the star removal for q_k, the symbol bound QQ^* >= 1/3, the Fubini identity and the n-dependence in 7.6, the sign of the paramagnetic term in 7.7, (8.1), (8.2), b, Lemma 9.3 off the star, the linear lift bounds in 9.4, the tree gauge, Lemma 10.1, and Theorem 4.2 from (5.5).
- Derived at sketch level: the excess bound and recycling in 4.4, Theorem G and gluing in 4.5, 7.2, 7.3, 9.5. Derived given those: (EI) and closure in 4.6, the one-step source induction in 6.1.
- Derived given stated inputs: Proposition 11.1, given (REG) and per-polymer invariance.
- **Theorem I is a target. It is not proved.** Nothing above is believed without a route, but most small-field items are at the level of estimates by scale counting, not line by line.
- Numerics. (i) `checks/hard-core--independent_defect_gain.py`, earliest line-averaged map, flat background: PASS-SHEET with max S = 1.000 at L = 3, 5, 7; single links at L = 3, 5 only, since L = 7 was stopped, so PASS-GENERIC is not evaluated at L = 7. **Those runs did not hold the numeric lock:** another push held it, my acquire failed, and I had piped its output through tail, which hid the failure. (ii) `checks/hard-core--independent_lift_form.py`, under a confirmed lock: see Lemma 10.1. (iii) `checks/hard-core--independent_field_ineq.py`, map D3 with the older rule threshold 0.5, under a confirmed lock, at L = 3, 5: PASS-55, max Ratio 1.000 and 0.999 against bounds 12.6 and 15.2, in the SHEET family; CHARGE exact to 2e-16; RULE-EFFECT below. These families can falsify (5.5). They do not confirm it on all fields, and no adversarial search was run.
- RULE-EFFECT, TUNED2 on noise: with base fixed at y, min |m| falls to 0.005 to 0.012 at L = 3 and to 0.001 to 0.009 at L = 5; with the rule it stays near 0.56 and 0.73. |W - 1| is larger with fixed base by a factor of 8 to 9 at L = 3. At L = 5 the three seeds give factors 0.6, 21 and 1.7, so the first seed goes the other way. The rule does not lower |W - 1| on every sample; what it reliably does is keep |m| away from zero, which is the hypothesis of 5.3. All ratios are far below the bound here, since the noise inflates the right side. Three seeds per L are a small sample.

**The large-field answer so far.** Theorem 4.2 and Theorem 4.3: a large-field region regenerates the large-field hypothesis at the next step with the same constant, in one line from the field inequality (5.5), because the l^1 norm of rough curvature contracts by L^{-2} under averaging. Every rough coarse plaquette is paid either by fresh regular energy at the finer level, or by rough plaquettes at the finer level with a margin L^2 / C_OS. That margin pays the entropy. Rough cubes under a regular field are a dilute gas in the fluctuation integral. The divergent count LF-count is the vacuum part of that gas, cancelled by the named subtraction, and the rest is irrelevant after extraction. I do not claim this is Balaban's R operation: his bodies could not be read (Project Euclid and Deep Blue both served bot checks, and I stopped there).

**Hardest remaining inequality.** Whether the whole small-field chain has hidden L-dependence in the one place it must not: L_0 := exp(4 C_0 / b) with C_0 from Theorem G's kernel moments. Everything else may depend on L, as gamma comes after L. Concretely: C_0 >= |c_j - c_W|, with the integrand of 8.4a, needs the symbol bounds of H_{t,1}, H_{t,2}, delta_1, delta_2 with constants depending on d only. They come from Theorem G and Lemma 4.5a, which count in the scale-invariant norm ||.||_#, and I have only checked that count by hand. A numerical evaluation of c_1 - c_W or of Hess F_1 at small L is possible in principle and would test this. Other items are written at estimate level and need a line-by-line pass, not a new idea, as far as I can see. That is my belief, not a result.

**Routes tried and why they failed** (Text 1.5, 2, 5.4, 7.5, 9.7, 10.3): one-link solve (variance grows linearly with level); entire reference-path average (rough path keeps full weight; fine action no longer dominates at large curvature); line-averaged prefix (star cancels only approximately at large field); iterating the fiber flow for complex bounds (L^2 per level); one-function pointwise induction on all V (entropy compounds unless an excess lemma is proved for arbitrary fields, replaced by frozen islands); pricing a tower at tuned block centres (needed a density bound I could not prove, replaced by the field-chosen base point of 5.4); two thresholds in recycling (non-analytic indicator, removed); stepwise regularity of the lift (shape factor compounds, replaced by the one-shot bound of 9.4); energy-only regular class (needs a lattice Uhlenbeck gauge I did not prove; set aside away from the trivial background); direct sign analysis of beta per level (dia and constraint terms have no sign; superseded by the telescoping (8.2)); L-free composite bound on rough inputs through the star (L^{1/2} loss, recorded); fine-lattice regularity at all depths (three routes, Text 10.2; made unnecessary by the level-only scheme); recursion for the third-order part of F_k (needs C_src level by level, replaced by the one-shot Theorem G); a hard cut on xi in the first version of (EI) (it ignores that |B| < eps_1 is a non-local, sharp function of xi); an analytic cut in B alone (the chart ends at the box, so the integrand is undefined where the analytic cut is merely small; replaced by the polynomial square root in 4.6); that square root in maximal tree gauge (condition number L^4, range L^2 does not fit a level-(k+1) cube; replaced by block Landau gauge); estimating the nested map with Q_root in place of Q_str (norm C_d > 1 per level, compounds; replaced by Lemma 4.5a, where Q_str has norm exactly 1 and the legs are gauge); frozen islands with histories and a tree count (worked in outline but carried multi-scale boundaries, replaced by Theorem 4.3); bounding the shift of the constraint by the fraction of bad paths (a term f^2 loses for dense rough sets; replaced by the signed quadratic bound in 4.4); a large-field cost of order f^2 per rough plaquette (no margin, the coefficient decays along the flow with the sum of g_k^2 log(1/g_k), Text 4.2).

**Next action.** Line-by-line pass on Theorem G and Lemma 4.5a, tracking constants for dependence on L. When a lock is confirmed (held by another push until 02:30 UTC): `field_ineq.py search 3 300`, then rerun the families with threshold eps_0.

## Obligations
- discharged: Lemma 4.5a, nested constraint with no compounding, free of L -> Theorem G
- discharged: Theorem 5.5, field inequality at every real field, with (5.4); the rectangle filling is standard and not enumerated -> Theorem 4.2
- discharged: Theorem 4.2, Lyapunov inequality, from Theorem 5.5 -> Theorem 4.3
- gap: rerun the field-inequality check with threshold eps_0 in the rule, and an adversarial search; the script tests threshold 0.5 -> confidence in Theorem 5.5
- implication: large-field regeneration, Theorem 4.3, given (4.1), I(k)(a), (c) and exterior polymer bounds -> I(k+1)(c)
- implication: Theorem P, third-order bound and Hessian, given Theorem G -> I(k+1)(a), (FLOW), 4.6
- unchecked: Theorem G, one-shot fixed point near the trivial background, with Lemma 4.5a derived and the rest of the estimates written but not line by line (Text 4.5) -> Theorem P
- discharged: saddle stability in scaled norms, commutator with a cutoff C / R (Text 4.5) -> gluing, 7.3
- unchecked: gluing patches and Newton on Om, given Theorem G and library/path_expansion_locality.md (Text 4.5) -> I(k+1)(a)
- discharged: (EI) on small cubes, exterior polymer bound by expansion in the white noise, given Theorem G and 7.3 (Text 4.6) -> I(k+1)(b)
- unchecked: (CUT), polynomial square root, three kinds of cube, margin device, spectator expansion, written step by step (Text 4.6) -> I(k+1)(b)
- unchecked: recycling, exterior with holes by path expansion, given library/path_expansion_locality.md (Text 4.4) -> I(k+1)(b)
- unchecked: excess bound in the nonlinear regime, given the signed quadratic bound (Text 4.4) -> I(k+1)(b)
- gap: blocked tubes as a local factor in I(k), checked through one step (Text 4.4) -> I(k+1)
- implication: irrelevance, Proposition 11.1, given Holder control of the lift (Text 4.5) -> I(k+1)(b)
- unchecked: |c_j - c_W| <= C_0(d), by power counting from symbol bounds (Text 8.4a); the cubic and quartic low-momentum vanishing is argued from gauge invariance, not computed -> (8.2)
- implication: (FLOW) for L >= L_0, beta in [(b/2) log L, 2 b log L], given |c_j - c_W| <= C_0, Theorem G and (EI) for the O(g^2) -> Theorem I hypothesis, trajectory in UV-CT
- unchecked: covariant Combes-Thomas decay (Text 7.3), given coercivity and saddle stability -> Theorem P, 4.6
- unchecked: lattice Sobolev on a torus and zero-mean handling per tube, given Gagliardo-Nirenberg on Z^4 -> Lemma 9.3, 9.5
- unchecked: I^w(k) -> I^w(k+1), written term by term in Text 6.1, given (EI), Theorem G and 11.1; the second moment of H^# in item 5 not extracted -> UV-CT
- implication: UV-CT, CT1 to CT4, given I^w(K) and FLOW -> upper-chain
- discharged: Lemma 1.1 exact Haar pushforward -> Corollary 1.2, recursion (1.2), mixed bonds
- discharged: Lemma 2.1 fiber flow -> checks
- discharged: exact identity (5.1), inequality (5.2) -> (5.5)
- discharged: linearisation of the final map equals (R4) -> propagator setting, (R5), (R7)
- discharged: Lemmas 7.1, 7.2 and Theorem 7.3, abelian coercivity uniform in k -> Theorem P
- discharged: QQ^* symbol bound for Q_str -> Text 7.3
- discharged: one-loop telescoping identity (8.1) on covariantly constant backgrounds -> (8.2)
- discharged: coefficient b = 11/(3 pi^2), continuum heat kernel -> (8.2)
- discharged: Lemma 9.3 off the star, non-compounding second derivative of the composite map -> 9.5
- discharged: linear lift bounds free of L, given the upper bound on q_n -> 4.5, 9.5
- discharged: Lemma 10.1, two-sided bound on the abelian perfect form, every n -> 9.4, 9.5, Theorem P, Text 6
- discharged: maximal tree gauge, trivial Jacobian at every field -> exterior integral
- discharged: ultralocal cluster expansion, proved in library/ultralocal_cluster_expansion.md with credit to Dimock and Balaban -> 11.2, 4.4
- discharged: path expansion of an inverse and Mobius locality, proved in library/path_expansion_locality.md -> 4.4, 4.5
- discharged: per-polymer gauge invariance by localising in the white noise only -> Proposition 11.1

## Requests
- Target lead, gate request: the large-field sector, Text 4.1 to 4.4 and Theorem 5.5, is ready for a hostile check. It is the part of this file that answers the charter's question directly: Lyapunov inequality, regeneration with no history, and where the 4D count goes. Theorem G and Lemma 4.5a in Text 4.5 are next.
- Target lead: Text 6 maps this induction onto UV-CT. CT1 for all w in the class, CT2, CT3 and CT4 follow from I^w(K), with E the named subtraction rho_K^w(1) averaged over lattice symmetries. Please confirm two things. (1) The trajectory can run along a = L^{-K} a_K with L odd and large: Tor has an even number of last cells, so its reflection planes are lattice planes. The upper chain's dyadic a is then replaced by L-adic. (2) Gate item D2 counts modes at the bare coupling. In my scheme the zero-mode factor of Tor is at the fixed coupling g_K, on a bounded number of cells. If the checker sees a log log(1/a) in Text 6.3 CT4, I want the line.
- FROM TARGET LEAD, gate on UV-CT (`git show origin/claude/ym4d-hard-route:.claude/science/physics-loops/ym4d-hard-route-20261030/gates/uv-ct-upper-chain-41489e4876.md`): noted. CT3 is addressed in Text 6.3 by Mobius in the source support, CT1 at complex sources in Text 6.1.
- FROM TARGET LEAD, 2026-10-30: interface changed from UV-EXT to UV-CT. Consumed: Text 6 has been rewritten. The earlier real-s request is withdrawn. I read `parts/upper-chain.md` for the interface statement and its requests only, and I have not read the mapped attempt.

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

**So the explicit subtraction is log rho_K(1; beta), the constrained partition function with the coarse field trivial.** It is exact at every beta, and it carries every vacuum term, including the vacuum part of every large-field gas. With a source it becomes the counterterm of UV-CT (Text 6.2).

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

### 3. Order of constants and the induction statement (level-only scheme)

Everything is stated on the current level's lattice. r_k is one function of the level-k field V; nothing finer is ever carried, and there is no sum over histories. Credit: the split of an effective density into a small-field form and a large-field factor, and the extraction of a cost from the action, are the organisation of Balaban (titles and reviews only; bodies unread) as exposed for d = 3 scalar by Dimock II, III, which I read. Iterating polymers with a contraction per step, rather than re-evaluating them at a composite background, is Dimock's Lemma 11 in part I. CMP 109 (LANE-READ) re-evaluates instead. The Lyapunov inequality below is derived here, and **I make no claim about how this relates to Balaban's R operation.**

**3.1 Order.**
1. kappa, M: polymer rate and cube, absolute. The classical kernels have range of order 1 in level units, and fluctuations at level k have range of order 1 in level-(k+1) units (3.3), so nothing forces M above L.
2. L odd, large against M and all absolute constants: L >= L_0(M). (FLOW) needs it (8.2), and contraction by (M/L)^alpha needs it.
3. C_OS <= C log L (5.5). c_F := c_A / (8 C_OS^2 O), O the overlap number of hulls.
4. eps_0 := c_1 L^{-2}, c_1 small absolute: fiber stability needs coarse curvature below an absolute constant (7.2), and that means level-k curvature below c_1 / L^2.
5. alpha := c_2 eps_0, complex radius, with c_2^2 <= c_F / (C M^3). eps_1 := eps_0 / (4 L^2), the cut on the fluctuation.
6. p(g) = (log 1/g)^{p_0}, 2 p_0 > 1: white-noise cut.
7. gamma, last and small against everything above.

Compare 5.6 of an earlier version of this file, where M > L forced a grace period: with L >> M a cell is already small against a block, and that whole mechanism is gone.

**3.2 Regions and functionals.** For V on T_k: f_p = |V_p - 1|. Rough plaquettes: f_p > eps_0. Y_k(V) := sum over rough p of f_p. Lambda(V) := the cells containing rough plaquettes; Om(V) := its complement. Near: plaquettes in Lambda(V), or within distance 2 of it. E_k(V) := sum over plaquettes neither rough nor near of f_p^2. There are at most C_M := C M^4 near plaquettes per rough cell, each with f <= eps_0, and at most Y_k / eps_0 rough cells, so the sum of f over near plaquettes is at most C_M Y_k.

For a union of cells Om and V regular on Om, F_{k,Om}(V) is the **classical functional with free boundary**, defined tropically: F_{0,Om} = A on Om, and F_{k+1,Om'}(W) := min of F_{k,Om}(V) over the regular slice of the fiber, with constraints only on bonds with both blocks in Om'. Directly from the definition:

    Adding a constraint or frozen boundary data can only raise the minimum: F_{k+1,Om'}(W; frozen) >= F_{k+1,Om'}(W).                          (3.1)

**3.3 Statement I(k).** For every real V on T_k,

    r_k(V) = exp( -g_k^{-2} F_{k,Om}(V) + EE_{k,Om}(V) ) G_k(V),     Om = Om(V),                                                                (3.2)

which *defines* G_k > 0, such that:

(a) *Classical.* On regular V, F_{k,Om} = qcov_n + N_k, with n = L^k, qcov_n the gauge-covariant form of the exact quadratic perfect action of Text 7.1, 10.1, and N_k gauge invariant of third order in the curvature, with density bound |N_k density| <= C_N (local |F|)^3 uniformly in k (Theorem P, 4.5, from Theorem G). In particular F_{k,Om}(V) >= c_A E_k(V on Om) with c_A >= 1/4.

(b) *Quantum.* EE_{k,Om} is gauge invariant and analytic on the complex class C(Om; eps_0, alpha), EE_{k,Om}(1) = 0, and it is a sum over xi-supports Y of functions e_k(Y; V), each gauge invariant, with sensitivity to V decaying exponentially away from Y at rate kappa / M, |e_k(Y)| <= E_0 exp(-kappa d(Y)), and sum_Y |e_k(Y)| <= C_E |Om| on the class.

(c) *Large field.* G_k(V) <= exp( -c_F eps_0 Y_k(V) / g_k^2 + B_0 |d Lambda(V)| ), and more precisely the same bound with V complex on Om in the class and real on Lambda, with G_k analytic in the data on Om near Lambda and independent of V on Om far from Lambda up to the terms in (b).

(d) *Symmetry.* All objects are gauge invariant and covariant under the lattice symmetries of T_k.

**Theorem I (target).** If g_k <= gamma for all k <= K, then I(k) holds for all k <= K, with constants independent of k, K and the volume. The flow is defined by extracting the marginal part from EE_{k+1} (11.1) and (FLOW) gives the trajectory.

### 4. One step k -> k+1: what regenerates (the crux)

**4.1 Field input.** (5.5): for any real V and any split of the hull plaquettes of a coarse plaquette P into irr and reg, |W(dP) - 1| <= C_OS ( L^{-2} ||f||_{l^1(irr)} + ||f||_{l^2(reg)} ).

**Theorem 4.2 (Lyapunov inequality) [DERIVED from (5.5)].** For every real V, with W = M(V) and L^2 >= 8 C_OS O (1 + C_M),

    c_F eps_0 Y_{k+1}(W) <= (1/2) [ c_F eps_0 Y_k(V) + c_A E_k(V) ].                                                                                 (4.1)

*Proof.* Take a coarse plaquette with phi := |W(dP) - 1| > eps_0. Put irr = rough and near plaquettes of the hull, so ||f||_{l^1(irr)} <= (1 + C_M) Y_k(enlarged hull P). Then (5.5) gives phi <= 2 C_OS L^{-2} (1 + C_M) Y_k(hull P), or phi <= 2 C_OS E_k(hull P)^{1/2}. In the second case, phi <= phi^2 / eps_0 <= 4 C_OS^2 E_k(hull P) / eps_0. In either case

    phi <= 2 C_OS (1 + C_M) L^{-2} Y_k(hull P) + 4 C_OS^2 E_k(hull P) / eps_0.

Sum over such P, with each level-k plaquette in at most O hulls, and multiply by c_F eps_0.  []

This is why near plaquettes are put on the l^1 side: their energy is not controlled by F_{k,Om} (they are in Lambda, or too close to the boundary for the local form of (R5)), but their l^1 weight is at most C_M Y_k, and L >> M makes L^{-2} C_M small.

*Why a cost linear in f.* A cost of order f^2 per rough plaquette looks natural, and I tried it first. It has no margin: a smooth W with curvature phi has children of curvature phi / L^2 with total f^2 equal to phi^2 by (R5), which is sharp. The entropy paid at each level then has to come out of the coefficient, c_F^{(k+1)} = c_F^{(k)} (1 - C g_k^2 log(1/g_k) + beta g_k^2), and along the flow the sum of g_k^2 log(1/g_k) over levels is about (log K)^2 / (2 beta log L), so c_F decays with K. **That fails.** With a cost linear in f, the l^1 term contracts by L^{-2}, because of (R7) and not of the action; the margin is there at every level, and no history is needed. Any cost f^a with 1 <= a < 2 has margin of order L^{4 - 2a}.

**Theorem 4.3 (large-field regeneration) [DERIVED from (4.1) and I(k)(a), (c); factorisation sketched].** For W with rough set Lambda', and frozen variables on the hull H of Lambda', use mu_W as a probability measure on V|_H. For the classical part use superadditivity, F_{k, Om_1 u Om_2} >= F_{k, Om_1} + F_{k, Om_2} for disjoint regions, which holds at level 0 since A is a sum, and passes through the minimum. This decouples H from the exterior in the direction of an upper bound, and the exterior minimum is then exactly F_{k+1, Om'}(W). Off H the quantum part is compared with the vacuum using polymer bounds. Then

    G_{k+1}(W) <= sup_V exp( -[c_F eps_0 Y_k(V) + c_A E_k(V; H)] / g_k^2 ) * (C / g_k)^{n_f |H|} * exp(B_0 |d H|),

where (C / g_k)^{n_f |H|} is the comparison of Haar with the vacuum Gaussian, and n_f the number of level-k variables per level-k cell. By (4.1) the exponent is at most -2 c_F eps_0 Y_{k+1}(W) / g_k^2, and |H| <= C L^4 Y_{k+1}(W) / eps_0 since each rough coarse plaquette has phi > eps_0. So the entropy is at most C L^4 n_f eps_0^{-1} log(C / g_k) Y_{k+1}(W), which is below c_F eps_0 Y_{k+1}(W) / g_k^2 when g_k^2 log(1/g_k) << c_F eps_0^2 L^{-4}, true for g <= gamma. Since 1/g_k^2 >= 1/g_{k+1}^2 when beta >= 0,

    G_{k+1}(W) <= exp( -c_F eps_0 Y_{k+1}(W) / g_{k+1}^2 + B_0 |d Lambda'| ).

**No constant has degraded.** This is the answer to the charter's question, for the bound: a large-field region regenerates hypothesis (c) at the next step, with the same c_F, in one line from (5.5), and with no history, no frozen fine variable, no excess lemma, and no tree count. Hypotheses (a), (b) are in 4.5, 4.6.

**4.4 Recycling: rough cubes where W is regular [SKETCH].** Let W be regular on Om', and let V in the fiber have rough cubes inside. There are three types of cube at level k: small (white noise within the cut p(g)); mid (white noise above the cut, |B| < eps_1), weight at most exp(-p^2 / 2) with no entropy, since the Gaussian is normalised; large (|B| >= eps_1, or V rough), frozen, integrated by Haar. A large cube has activity relative to the regular replacement at most exp(-c_F' / g_k^2) (C / g_k)^{n_f M^4}, by the excess bound below.

*Excess [derived in the quadratic regime; nonlinear version sketched].* Let V be in Fib(W), with rough set S and W regular nearby. Let R := the weighted sum over S of parallel-transported F_p, the amount of coarse curvature carried by rough plaquettes: |R| <= C_OS L^{-2} Y_k(hull). The regular part must then carry F' - R. Its minimum energy is (1/2) |F' - R|^2 >= (1/2) |F'|^2 - |F'| |R|, since the term (1/2) |R|^2 has the favourable sign. So relative to the regular replacement, the net cost is at least

    c_F eps_0 Y_k - |F'| C_OS L^{-2} Y_k >= (c_F - C_OS L^{-2}) eps_0 Y_k >= (c_F / 2) eps_0 Y_k,

for L^2 >= 2 C_OS / c_F, and this holds with no restriction on Y_k. If R is so large that W with the shift is outside the regular region, use F >= 0: the loss is then at most F_{k+1}(W) on those cells, at most C eps_0^2 per coarse plaquette, and |R| >= eps_0 forces Y_k >= eps_0 L^2 / C_OS, so the cost c_F eps_0 Y_k is at least c_F eps_0^2 L^2 / C_OS, larger by a factor L^2 c_F / C_OS. **My first version bounded the shift by the fraction f of paths through S and kept a term f^2, which lost for dense S. Both were wrong: bad paths deviate by the curvature they enclose, not by 2, and the second-order term has a sign.** For type Z, convexity on the slice gives c eps_1^2 / g_k^2.

*Summation.* For fixed S the exterior is a Gaussian on the complement of S with spectator W. The dependence of its logarithm on S has to decay in the distances between holes, and that is the only multi-body input. By `library/path_expansion_locality.md`, the inverse of the exterior form on the complement of S is a sum over paths of patches, each term depending on S only at patches on its path. log det is an integral of a trace of such inverses, and C_S^{1/2} is a contour integral of resolvents, so the same holds for them. Mobius differences in S then pick out paths visiting all of S, and decay in the tree length of S at the rate of 7.3. The hard-core gas of large and mid cubes has activities bounded by a tiny number per cube, and steps 3 to 5 of the cluster library proof, which use only a bound on z(Y), exponentiate it. The result is EE^R(Y; W) in EE_{k+1}. *Scale of cubes.* The fluctuation at level k has range L in level-k units, so white noise is grouped in level-(k+1) cubes of side M, that is M L in level-k units; rough sets are subsets of these, and the factor (1 + tiny)^{(L M / M)^4} is harmless. [Sketch.]

*The divergent count.* Per level-(k+1) cell the recycled gas has activity about L^4 M^{-4} exp(-c / g_k^2), tiny, at every level. Summed over all cells of T_{k+1} and over levels it is of order |T_phys| L^{4(K-k)} exp(-c / g_k^2), which diverges if c beta < 4. This is Proposition LF-count of the program [arithmetic re-derived]. In (1.2) its value at W = 1 goes into the named subtraction and cancels exactly. Its W-dependence is irrelevant after extraction (11.1), with marginal shift of order exp(-c / g_k^2), summable in k. **That is where the 4D price goes.** Nothing in this scheme bounds the count, and no condition on c beta arises.

*Blocked tubes.* If at least a quarter of the crossing paths of a tube pass through large cubes, the exterior cannot carry the constraint with the implicit function theorem, and that term is not analytic in W, even with W regular. Such a V has at least (L / M)^3 / 4 large cubes, so its weight is at most exp(-c (L / M)^3 eps_0^2 / g_k^2), far below everything else. It is kept out of EE_{k+1} and carried in (3.2) as a factor 1 + b_{k+1}(c; W) over blocks, with 0 <= b_{k+1} tiny, real, local. At the next level its cube counts as large, with W frozen and real. So I(k) needs this extra factor, and (c) must be read with it. [Scheme. Not checked in detail.]

**4.5 Theorem P (classical functional).** The recursion for N_k I first wrote here (N_{k+1} = N_k(V^*) + bracket, contraction L^{-2}) needs C_src and C_s and a comparison of covariantised forms at each level. I replaced it with a one-shot argument, which needs no recursion through levels at all.

*Theorem G (local analyticity, one-shot) [DERIVED at the level of each estimate; not line by line].* Let Omega be a ball of R level-k cells, with free boundary, and let V be regular on Omega with curvature bound eps <= eps_*(R). In a coarse gauge where V = exp(iv) with |v| <= C R eps, F_{k,Omega}(exp(iv)) is given by a convergent fixed-point expansion around the trivial background. Its Taylor coefficients at v = 0 of each order m are bounded by C^m m! on level-k sup norm, with exponential decay in the distances between links at rate delta_0, with C, delta_0 depending on d only and **not on k or L**.

*Proof.* Work on the fine lattice of the hull, with spacing eta = 1/n in level-k units. Norm: ||a||_# := sup |a| / eta + sup |grad a| / eta^2. Modulo coarse gauge the star through block centres is a coarse gauge factor up to second-order cross terms, by 5.3. Fixing fine Landau gauge d^* a = 0 and minimising over coarse gauge, stationarity reads

    Delta a = Q_str^* mu + J(a),    Q_str a = v + d_c lambda + NN(a),    d_c^* mu = 0,

where J collects the nonlinear part of the gradient of A(exp(ia)) and (Q^U - Q)^* mu, and NN is the nonlinear part of the composite constraint.
- *Linear solve.* v -> (mu, a). In momentum space G_mu(P) = [a(P) + P^2 c(P)] / P^2 with a, c analytic in a strip, a(0) = 1, positive on the real torus by Lemma 10.1, so 1 / G_mu is analytic in a strip of width delta_0, depending on d only: mu is exponentially local in v, in the coarse curvature. The form is exact and depends only on n. Then a = G * Q_str^* mu, and since d^* of a (mu nu) tube weight has only in-plane derivatives, the source is bounded by C eta^3 |mu|; |grad G(x)| <= C |x|^{-3} gives |grad a| <= C eta^2 and |a| <= C eta, per unit of v in the local gauge. [Derived. On a box, the Neumann Green's function has the same bound by reflection.]
- *Nonlinear source.* F_p = (da)_p + [a, a]_p + ..., so J contains grad(a a), [a, da], [a, [a, a]], of size eta^3 ||a||_#^2 (1 + ||a||_#). **J contains only first derivatives of a,** so grad G * J has the scale eta^2 with no derivative loss: |grad G * J| <= C n eta^3 ||a||^2_# = C eta^2 ||a||^2_#, using the decay of the conditional propagator at scale n. (Q^U - Q)^* mu has size eta^3 |mu| ||a||_#, from transport phases along a path of length n.
- *Nonlinear constraint.* By Lemma 4.5a below, |NN(a)| <= C ||a||_#^2 and |grad NN(a)| <= C ||a||_#^2, with C depending on d only.
So the map a -> a' is a contraction on the ball ||a||_# <= C R eps for eps <= eps_*(R). Analyticity follows, since all the expressions are analytic in a and v with these bounds on complex polydiscs.  []

*Lemma 4.5a (no compounding through the nested map) [DERIVED].* Scaled norm on level-i links: [B]_i := sup |B| / xi_i + sup |grad B| / xi_i^2, with xi_i = n_i / n. For small a, with ||a||_# = A <= A_0, and modulo coarse gauge at level k, M^k(exp(ia)) = exp(i(Q_str^{(k)} a + NN(a))), [NN(a)]_k <= C A^2.

*Proof.* (i) *Q_str has norm exactly 1 from [.]_i to [.]_{i+1}.* |Q_str D(c')| = |avg_x sum_{t < L} D(x + t e)| <= L sup |D|, and xi_{i+1} = L xi_i. For the gradient, Q_str D(c' + L e_nu) - Q_str D(c') is an average over the tube of a sum of L differences over distance L, at most L^2 sup |grad D|, and xi_{i+1}^2 = L^2 xi_i^2. The norm is exactly 1, because Q_str is a positive average with total length L. **This is the point: Q_root with its axial legs would have norm C_d > 1 and would compound as C_d^k, and that is why the star must be removed first.**

(ii) *One step, modulo gauge.* All paths in the family of a coarse bond have the same endpoints, so for a reference path S, M = S exp(i avg_pi Phi_pi + O(disp^3)), where Phi_pi is the log of the holonomy between pi and S, a sum of transported level-i plaquette logs over a surface of area at most C L^2. So disp <= C L^2 xi_i^2 [B]_i = C xi_{i+1}^2 [B]_i. By the common-factor structure of 5.3 the legs from block centres enter M only by a coarse gauge factor, plus a cross term (star dispersion) x (path dispersion) <= C xi_{i+1}^4 [B]_i^2. So the next field is, modulo gauge, exp(i(Q_str B + NN_1(B))) with:
- commutators on the straight reference S: pairs (b, b') give |[B_b, B_b']| <= |B_b| |B_b - B_b'| <= xi_i * L xi_i^2 [B]^2, over L^2 pairs: C xi_{i+1}^3 [B]_i^2;
- the term sum_p w_p [B, B]_p in avg Phi: its constant part is sum_{mu < nu} [Bbar_mu, Bbar_nu] x (mean signed area), and the mean signed area of the family is exactly 0 by the reflections of transverse axes, which fix the bond and preserve the family: x and z are uniform and the axial orders are symmetric. The variation of B over the hull contributes C L^2 * xi_i * L xi_i^2 [B]^2 = C xi_{i+1}^3 [B]_i^2;
- transport factors in Phi: (area) x (xi_i^2) x (path length x xi_i): C xi_{i+1}^3 [B]_i^2;
- third-order terms of the mean: disp^3 <= C xi_{i+1}^6 [B]_i^3.
So |NN_1(B)| <= C xi_{i+1}^3 [B]_i^2, that is, xi_{i+1}^{-1} |NN_1| <= C xi_{i+1}^2 [B]_i^2. The gradient, by the same count with one factor replaced by its difference over a block, gives xi_{i+1}^{-2} |grad NN_1| <= C xi_{i+1} [B]_i^2.

(iii) *Induction.* Write B_i = Q_str^{(i)} a + D_i. Direct average gives [Q_str^{(i)} a]_i <= A, and D_{i+1} = Q_str D_i + NN_1(B_i). So [D_{i+1}]_{i+1} <= [D_i]_i + C (xi_{i+1} + xi_{i+1}^2) (A + [D_i]_i)^2. Since sum_i (xi_{i+1} + xi_{i+1}^2) <= 3 for L >= 3, and with the bootstrap [D_i]_i <= A, we get [D_k]_k <= 12 C A^2, consistent if 12 C A_0 <= 1.  []

The sum over levels is dominated by the top level, the bound is free of L because every count is scale invariant in L, and the constant does not grow with k since Q_str has norm 1. *Hostile:* in (ii) the reflection argument needs the family to be exactly reflection symmetric. On fields with no rough plaquette x_0 = y and it is. On the patch, rough plaquettes do not occur.

*Consequences.* (i) N_k bound: F_{k,Omega} - qcov has vanishing second order by Lemma 7.1 and Lemma 10.1, and third order bounded by Theorem G, in a frame at each site. So |N_k density| <= C (local |F|)^3: this is immediate, and no C_src recursion occurs. (ii) Hessian: in the frame, Hess F_{k,Omega}(V) = Hess F_{k,Omega}(1) + O(R eps), with the exact Hessian at trivial background bounded by 1 <= kappa <= (pi^2/4)^6 on closed forms. On ker Q the correction is relative to ||D_V B||^2 through Poincare at block scale, as C phi L^2 <= C c_1, so coercivity holds for c_1 small, with no L. (iii) Lift: the same fixed point on the level-(k+1) block gives V^*(W), with curvature at most C_s L^{-2} sup |F'| and Holder modulus (|x - x'| / L)^a, with C_s absolute, since grad G * (bounded source) is Holder. (iv) Lower bound: F_{k,Omega} >= c_A E_k on Omega minus a boundary layer, from (ii) with Lemma 7.1, and c_A -> 1/2 as eps -> 0.

*Saddle stability and the commutator [DERIVED].* Norms: on fine fields ||a||_E^2 := ||grad a||^2 + eta^2 ||a||^2, and l^2 on level-k links for the multiplier. Then Q is bounded: ||Q a||^2_{l^2} <= 2 eta^2 ||a||^2, by Cauchy-Schwarz along the tube (Text 9.2). Q has a bounded right inverse: the Feynman lift has ||grad a||^2 = <B, GG^{-1} B> <= C ||B||^2, since G_mu^{-1} <= (pi^2/4)^5 P^2 is bounded on the torus. K is bounded on E, and coercive on ker Q by Poincare at block scale, by Lemma 7.2 and 7.3. So by Babuska-Brezzi the saddle operator S is invertible from E x l^2 to its dual with bound depending on d only. For a scalar cutoff h at scale R n: [K, h] has norm at most |grad h| ||a||_{l^2} / ||a||_E <= C / R, since |grad h| = eta / R, and [Q, h] a(c) = avg over the tube of (h - h(c)) a, with |h - h(c)| <= C / R on the tube, and the same Cauchy-Schwarz gives C / R. **So ||[S, h]|| <= C / R, with C depending on d only, in spite of the multiplier being on the coarse lattice.** With local inverses S_c bounded by C_S, the parametrix error is at most C C_S nu / R.

*From patches to Om (gluing) [SKETCH].* For V regular on Om, take the local solutions on overlapping patches. Two of them agree on an overlap, in a common patch gauge, up to exp(-delta_0 dist(boundary)), by Combes-Thomas for the flat form. Glue with a partition of unity at scale R n into U_0: residual exp(-delta_0 R / C), tiny. The saddle operator at U_0 has a parametrix built from the local inverses, with error C / R: commutator of the partition with the operator, at scale 1/(R n), against gap scale n. `library/path_expansion_locality.md` gives its inverse by a path expansion, with no gauge choice beyond one patch. Newton from U_0 converges and gives an exact critical point with all of the above, and on the slice it is the unique minimum by (ii). So Om is handled by finite-range bookkeeping, for R fixed absolute and eps <= eps_*(R). Long-distance holonomy never enters.

**4.6 The exterior polymer bound (EI) [DERIVED given Theorem G and the covariance decay of 7.3].** Fix W regular, possibly complex in the class, and V^* = V^*(W).

*Coordinates.* On the slice, use block Landau gauge, with its local Faddeev-Popov factor, and solve the constraint by Z + HH(Z), with Z in ker Q, HH of second order and local at block scale, and a Jacobian that is a product over coarse bonds of local analytic functions. This is the structure of CMP 109 (2.9)-(2.13) as transcribed (LANE-READ), with Landau for his exponential gauge. Then C := (Pi H_L Pi)^{-1} on that subspace is coercive by Text 7, with kernel decaying at rate c / L in level-k units by 7.3, with a polynomial prefactor C(L). White noise: Z = g Pi R_D xi, as in (CUT) below, with xi a product measure. (A first version used maximal tree gauge here: see (CUT), item 1, for why that fails.)

*Expansion.* Psi(xi) := g^{-2} R(g ZZ xi) + P(g ZZ xi) + log JJ, where ZZ := Cc C^{1/2} (plus HH), R is the remainder of F_k beyond second order, and P the variation of EE_k. By Theorem G and Cauchy at V^*, the Taylor coefficients of R of order m >= 3 at V^* have kernels at most C^m exp(-delta_0 tree(b_1, ..., b_m)), and the same for P with m >= 1, with a factor C_E. Inserting Z,

    Psi(xi) = sum_{m >= 1} g^{m-2 or m} sum T_m(b_1, ..., b_m) xi_{b_1} ... xi_{b_m},    |T_m| <= C(L)^m exp(-(c / L) tree(b_1, ..., b_m)),

with g^{m-2} for the classical part, for m >= 3, and g^m for P.

*Localisation in xi, not in W.* Group xi in cubes of side M L in level-k units, that is, level-(k+1) cubes of side M. Define H(X; xi, W) as the Mobius sum in the support of xi over X. Resetting xi to 0 outside a set is invariant under the Ad rotation accompanying a gauge transformation of W, so H(X) is jointly gauge invariant. In the alternating sum only monomials whose indices meet every cube of X survive. So a monomial contributes only if m >= |X|, and it has tree length at least (|X| - 1) M L. Hence on the cut |xi| <= p(g),

    |H(X; xi, W)| <= C(L, M) ( g p^3 + C_E g p ) exp(-c M (|X| - 1)),                                                                                 (EI)

for g C(L, M) p <= 1. **So kappa = c M depends on M only, H_0 = C(L, M) g p^3 is small for g <= gamma, and the bound is uniform in k, W and the volume.** The exponential sensitivity to W comes from the same kernels.

*Output.* `library/ultralocal_cluster_expansion.md` gives log int exp(sum_X H) dmu_cut = sum_Y H^#(Y; W), with |H^#(Y)| <= C H_0 exp(-r |Y|). H^# is analytic in W and gauge invariant. So the polymers from the expansion are of size g p^3, and only the one-loop term is of order one.

*One-loop term.* By (8.1), L_k(V^*) - L_{k+1}(W). Differentiating in W gives a trace of C(W) against a local kernel, so it is local with the decay of 7.3, gauge invariant, analytic, and bounded by E_0(L, M). It feeds nothing back into itself, since the kernels above come from F_k and not from it.

*Closure.* e_{k+1} consists of the output above, the recycled gas of 4.4, and the old polymers at B = 0, carried by 11.1 with xi = 1/L: contraction (M / L)^a. So ||e_{k+1}|| <= C (M / L)^a ||e_k|| + E_0, and C_E <= 2 E_0 for L large: **no recursion in E_0 beyond this geometric sum.** [Derived given 11.1 and the items above.]

*The cut (CUT) [ROUTE written step by step; the bound on z(Y) is by direct estimate, not line by line].* The slice is cut by |B_b| < eps_1, a box in B. But B = g ZZ xi, so with C^{1/2} of exponential tails this indicator is **not** a product in the white noise: it depends on all of xi, with a sharp edge. In Dimock II the analogous function is carried in the large-field characteristic functions, and his Rome lectures (p. 57 in the program's notes) call restoring its locality "a difficult technical problem", with no analyticity available. The first version of (EI) assumed a cut on xi alone and so missed this. An analytic cut (erf of width eps_1 g^{1/2}, then Cauchy in each cube) was my second attempt; it cannot serve alone, because the fluctuation chart ends at the box, so the integrand is not defined where the analytic cut is only small and not zero.

Route.
1. *Strict finite range by a polynomial square root.* **Conditioning matters here.** In maximal tree gauge the form has spectrum in [c L^{-4}, C], because a smooth mode of Landau amplitude 1 has tree-gauge amplitude L. A Chebyshev polynomial then needs degree about L^2 for a fixed error, so range L^2, which does not fit a level-(k+1) cube of side M L when L >> M. So on the small-field part use block Landau gauge: let Pi be the projector on ker Q intersected with d^* B = 0 in each block, local at block scale, and let H_tilde := Pi H Pi + (1 - Pi). By Poincare at block scale its spectrum is in [c L^{-2}, C]. Let R_D be the Chebyshev polynomial of degree D approximating H_tilde^{-1/2}, with error at most exp(-c' D / L). Then the covariance on the slice is C = Pi R_D(H_tilde)^2 Pi + C_rem, with C_rem >= 0 after a small adjustment, and ||C_rem|| <= exp(-c' D / L). So B = g Pi R_D(H_tilde) xi + g C_rem^{1/2} xi', with xi on all links, a product measure, and xi' independent. Pi is itself a polynomial up to an error of the same kind: Q Q^* has symbol at least 1/3 and needs bounded degree, and the block Laplacian has condition number L^2. The Faddeev-Popov factor of block Landau gauge is a local analytic functional of (W, B), with log FP of order |B|, and it goes into Psi. Truncating the exponential tails of H at range M_1 costs another term of the same kind. **So for fixed xi', the first term is a strictly local linear function of the product variable xi.** With D M_1 = M L, the error is exp(-c' M / M_1), small for M large against M_1, and free of L. [Chebyshev bound standard; range bookkeeping a sketch. This is close to a finite-range decomposition, used here only to get strict locality.] Tree gauge remains the coordinate for frozen rough cubes, where no Gaussian is used.
2. *For fixed xi', the expansion needs no analyticity in xi.* Expand the product of local factors: (e^{Psi_X} 1_{box} - 1). Disjoint polymers are independent for the product measure, so the integrated weights form a hard-core gas with activities z(Y; xi'). Steps 3 to 5 of the cluster library proof use only a bound on |z(Y)|.
3. *Bound on z(Y), cubes of three kinds.* Small: all |xi| <= p in the cube. There |B| <= C(L) g p << eps_1, the indicator is 1, and each factor is at most H_0. Mid: some |xi| > p in the cube, and the box still holds: use the Gaussian integral with exp(theta ||xi||^2), where theta <= C c_1 from g^{-2} |R(g Z)| <= C_3 eps_1 ||Z||^2 <= C eps_1 L^2 ||xi||^2, with eps_1 L^2 = eps_0 / 4. So such a cube costs at most (M L)^4 exp(-p^2 / 3). Large: rough, or outside the box: next item.
4. *Large cubes and the conditional mean.* For a set S of large cubes, freeze V on S. The exterior Gaussian then has a conditional mean of size at most C(L) eps_1 exp(-c dist(., S) / L). At distance r_1 := (L / c) log(C(L) eps_1 / (g p)), it is below g p, the small-field scale, and beyond that the expansion of 2 and 3 runs with the mean as a harmless spectator. On the collar within r_1 there is no expansion: bound the integrand by superadditivity (Text 4.3), which decouples S from the exterior, and use the exterior Gaussian. So a polymer with holes S carries a collar of (r_1 / (M L))^4 cubes per large cube, polylog in 1/g, with no small factor per collar cube; that entropy and the factor exp(kappa |collar|) are paid by the cost c / g^2 of S, for g <= gamma. **This is the margin device, and it is why the frozen hole needs no analyticity near it.**
5. *Decay in S.* C_S on the exterior is local by `library/path_expansion_locality.md`, so polymers with several holes have Mobius decay in the distances.
6. *Spectator xi'.* After 2 to 5, the result is a function of B' := g C_rem^{1/2} xi', and Gaussian convolution by xi makes it analytic in B' with radius of order g. B' has size g exp(-c' D L^{-2}). So a second expansion in xi', with amplitude exp(-c' D L^{-2}), converges and gives polymers smaller by that factor.
7. *Analyticity in W.* Hard cuts are in B, on a real contour, independent of W. z(Y; W) is an integral of those cuts against the Gaussian density of B on the support of Y, with covariance analytic in W and real part positive. So z(Y; W) is analytic in W with the same bound, up to exp(theta' |B|^2 / g^2), theta' <= C alpha / L, which is absorbed. For the same reason the partition is independent of W.

So **there is no hard indicator in xi except through local functions, and no analyticity in xi is used.** The output is the hard-core gas of 4.4.

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

**5.3 Two elementary facts.** (i) For a flat mean with reference h a unit quaternion: |m - h| <= D := avg |g_i - h|, so 1 - |m| <= D and |Mean - h| <= 2 D, **with no lower bound on |m|**, whenever m != 0. (ii) For nonzero a, b in R^4: |a/|a| - b/|b|| <= 2 |a - b| / |b|.

**5.4 The map, final form (D3).** Call a plaquette of a block *rough* if f_p > eps_0. For a site x_0 in B(y) put s(x_0) := sum over rough p in B(y) of min(1, dist(p, x_0)^{-2}). Put

    Psi_y^mu(z) = path(y -> x_0) * Mean over x in B(y), and over axial orders, of [ R(x_0, x) R_mu(x, z) ],

with x_0 = y if s(y) <= s_rule, an absolute constant, and otherwise x_0 a minimiser of s; ties and the axial order of path(y -> x_0) are decided by uniform choice in the kernel, a finite mixture of hard constraints, so the kernel is exactly covariant under the lattice symmetries. All of this depends on interior links only, so the crossing links stay private and Lemma 1.1, Corollary 1.2, Lemma 2.1 hold for each element of the mixture. On fields with no rough plaquette this is the map of 5.1, with linearisation (R4). A field in the small-field region has f_p <= eps_0 / 2 (3.1 item 4), so the rule depends only on frozen rough data, not on exterior data, and analyticity through the exterior is unaffected.

*Why the rule.* A defect of fixed size next to y can make the mean over stars small. Rotating the first links out of y in directions +-e_0, +-e_1 by -1 changes the sign of half of all paths from y. Numerics, TUNED2 in `checks/hard-core--independent_field_ineq.py`: with x_0 = y fixed, min |m| is 0.001 to 0.012, and with the rule it stays near 0.56 to 0.73. *First version of the rule was wrong:* it used a separate absolute threshold eps_rule >> eps_0. Then about 1 / eps_rule plaquettes just below eps_rule, next to x_0, make the star disperse with l^1 weight of order one, which L^{-2} ||f||_1 does not see. So the threshold must be eps_0. The check script tests the older threshold 0.5, so it has not tested this form.

**Theorem 5.5 (field inequality) [DERIVED; constants not computed].** For every real V, every coarse plaquette P, and every split of the hull plaquettes into irr, reg such that irr contains the rough ones,

    |W(dP) - 1| <= C_OS ( L^{-2} ||f||_{l^1(irr)} + ||f||_{l^2(reg)} ),    C_OS <= C log L.                                                       (5.5)

*Proof.* Step 1 (common factor). Fix a block y, the x_0 of the rule, and a second site x' used only in the analysis. Put Xi_x = R(x_0, x) R(x, x'), rho_x(z) = R(x, x')^{-1} R_mu(x, z), where R(x, x') has orders averaged over, as a flat mean. Then R(x_0, x) R_mu(x, z) = Xi_x rho_x(z), with **Xi_x independent of z and of mu**. With rho(z) := rho_{x_1}(z) for a reference x_1, and d(z) := avg_x |rho_x(z) - rho(z)|, we have m_z = Xi_bar rho(z) + e, |e| <= d(z), so by (ii), |Psi(z) - star Xi_hat rho(z)| <= 2 d(z) / |Xi_bar|, where star = path(y -> x_0) and Xi_hat = Xi_bar / |Xi_bar|. So if |Xi_bar| >= 1/4 the error is at most 8 d(z).

Step 2 (coarse link). T_u = Psi_y(u^-) u Psi_{y'}(u^+)^{-1} = (star Xi_hat)_y tau_u (star Xi_hat)_{y'}^{-1} up to at most 8 (d_y(u^-) + d_{y'}(u^+)), where tau_u = rho_y(u^-) u rho_{y'}(u^+)^{-1}. By covariance of the mean and (i), with M_tilde = conjugate of M by the common factors: |M_tilde - tau_{u_1}| <= 16 avg_u (d_y + d_{y'}) + 2 avg_u |tau_u - tau_{u_1}|, for every u_1. **The common factors cancel exactly from W(dP).**

Step 3 (loops). |W(dP) - 1| <= |tau_{u_1} tau_{u_2} tau_{u_3}^{-1} tau_{u_4}^{-1} - 1| + sum_i |M_tilde_i - tau_{u_i}|. Each term on the right is the distance from 1 of a holonomy of a closed polygon, directly or after averaging, and non-abelian Stokes gives |holonomy - 1| <= sum_{p in surface} f_p for any spanning surface. So |W(dP) - 1| <= C sum_p w_p f_p, where w_p is the probability, over the random vertices, that p is in the surface.

Step 4 (weights, (5.4)). Vertices of the polygons: x, x_1, x' (uniform on blocks), and z = u^-, whose transverse coordinates are uniform. z is reached and left along mu, on one line, so those two segments merge and z_mu is not a vertex coordinate. So every vertex coordinate that remains is a uniform variable, indexed by (vertex, axis), and independent for different indices. Fill an axial polygon with a bounded number C_d of axis-parallel rectangles, each of side at most 2 L, with each of the two perpendicular coordinates equal to one such variable. They have different axes, hence are independent. So a fixed plaquette is in a given rectangle with probability at most L^{-2}. Averaging over x' uniform gives

    w_p <= C_w L^{-2},   sum_p w_p <= C_w L^2,  C_w depending on d only,                                                                       (5.4)

and Cauchy-Schwarz on reg gives sum_p w_p f_p <= C_w L^{-2} ||f||_{l^1(irr)} + C_w ||f||_{l^2(reg)}. The average over x' may be restricted to the x' with |Xi_bar| >= 1/4; if those are at least half of the block, w_p at most doubles.

Step 5 (when |Xi_bar| is small). For a block, |Xi_bar| >= 1 - avg_{x, x_2} |Xi_x - Xi_{x_2}| >= 1 - sum_p w^*_p f_p, with w^*_p the weight of the polygon x_0, x, x', x_2. Its surfaces have stars at x_0 and x'. So w^*_p <= C (min(1, dist(p, x_0)^{-2}) + min(1, dist(p, x')^{-2}) + L^{-2}). Averaged over x' the second term is at most C L^{-2}. So if the x' with |Xi_bar| < 1/4 are more than half of the block, then

    (3/4)(1/2) <= C s(x_0) + C sum over p with f_p <= eps_0 of min(1, dist(p, x_0)^{-2}) f_p + C L^{-2} sum_p f_p.

By the rule, either s(x_0) <= s_rule, which is small against the left side for s_rule small, or s(x_0) = min s, at most the average C L^{-2} sum over rough f_p (since sum over x_0 of min(1, dist^{-2}) <= C L^2). The middle term is at most (C log L)^{1/2} ||f||_{l^2(f <= eps_0)}, as sum_p min(1, dist^{-2})^2 <= C log L. So one of: L^{-2} ||f||_{l^1} >= c, or ||f||_{l^2(f <= eps_0)} >= c (log L)^{-1/2}. Plaquettes with f <= eps_0 that the split puts in irr obey ||f||^2_{l^2} <= eps_0 ||f||_{l^1}, and eps_0 L^2 = c_1, so they fall under the first case at the price of a factor log L. In every case the right side of (5.5) with C_OS = C log L is at least the trivial bound |W(dP) - 1| <= 2.  []

*Status.* All five steps are derived here. The rectangle filling in Step 4 is the standard axial homotopy and was not enumerated by hand. No explicit value of C_OS is available. Theorem 5.5 needs L^2 >> C_OS O (1 + C_M) to feed Theorem 4.2, which only asks for L large.

*Numerics.* On the earlier rule, under a confirmed lock, L = 3, 5: PASS-55, with max Ratio 1.000, 0.999, in the SHEET family. CHARGE is exact to 2e-16. No adversarial search has been run.

### 6. What this gives the interface UV-CT

The lead replaced UV-EXT by UV-CT (`parts/upper-chain.md`, Text 7, read for its statement only, as the request directs). The reason: a constant real shift cannot feed the chain. I take the statement as given and do not read anything behind its wording.

**6.1 Induction with a local source: one step [DERIVED term by term; each term is at the level of the corresponding small-field estimate].** Let the bare coupling be beta - w(p), with w complex, |w| <= rho, Lipschitz at the physical scale a_*, constant Lam. All levels k <= K have a_k <= a_K, a fixed fraction of a_*, so Lam a_k <= 1 and is summable in k. Density recursion: f_{0,p} = s_p, f_{k+1,x'}(W) := sum_{x in B(x')} f_{k,x}(V^*(W)), with V^* the source-free lift, so sum_x f_{k,x} = F_k, and these densities are bounded by Theorem G.

Hypothesis I^w(k), on Om = Om(V):

    log r_k^w(V) = -g_k^{-2} F_{k,Om}(V) + sum_x w_k(x) f_{k,x}(V) + EE_k^w(V) + log G_k^w(V).

Set V = exp(iB) V^*(W). Then, term by term:

1. *B = 0.* -g_k^{-2} F_{k+1}(W) + sum_{x'} w_k(x') f_{k+1,x'}(W) + sum_{x'} sum_{x in B(x')} (w_k(x) - w_k(x')) f_{k,x}(V^*). The last sum is a polymer of size C Lam a_{k+1} per coarse cell times the local action: an irrelevant term with gain a_{k+1}, summable in k.
2. *First order in B.* -g_k^{-2} dF_k . Z vanishes on the slice. And sum_x w_k(x) df_{k,x} . Z: for constant w it is w dF_k . Z, which also vanishes. So only (w_k(x) - wbar) df_{k,x} . Z survives, of size Lam a_k (local |F|) |Z|, with Z of order g p: **a source does not move the background**, up to terms that are small here.
3. *Second order in B.* -(1/2)(g_k^{-2} - wbar) <Z, H Z> + (gradient term). Writing it as a Gaussian at w = 0 plus a perturbation of size rho g^2 p^2 per polymer, H_0 in (EI) gains a term C rho g^2 p^2, which is small.
4. *One-loop with source.* For constant w the Gaussian with stiffness b = g^{-2} - w has determinant b^{-dim/2} (det H_L)^{-1/2}. **So the W-dependence of the one-loop term is the same as at w = 0, for constant w.** In perturbation: the term of order g^2 w is (1/2) g^2 w Tr[C(W) H_L(W)], and Tr[C H_L] = dim, independent of W. This settles a point I had left open: there is no term of order g^2 w in the marginal part. The W-independent part, n log(1 - w g_k^2) per variable, is the term of E at this level. For Lipschitz w the remainder has a gain Lam a_k.
5. *Higher orders.* H^# of 4.6, as a function of b. Analytic in b on a disc of radius 1 / (2 g^2) around g^{-2}, since g enters only through b^{-1/2}. By Cauchy, d/dw of a quantity of size S is at most C g^2 S. The Gaussian mean of a cubic term vanishes by parity of the cut, so the marginal part of H^# is O(g^2 p^c).
6. *Flow.* Extract the marginal part of e_{k+1} by 11.1, polymer by polymer, at each x'. Then b_{k+1}(x') = b_k(x') - beta_{k+1}(b_k(x')) + (gradient, gain a_k), with beta_{k+1}(b) = b_0 log L + (c_k - c_{k+1}) + O(g^2 p^c), where the first two terms do not depend on b, by item 4. So |w_{k+1}(x) - w_k(x)| <= C g_k^4 p^c |w_k(x)| + C Lam a_k. Along the flow, sum_k g_k^4 p(g_k)^c < infinity, so **|w_k| <= 2 rho for all k, uniformly in K**, for gamma small and a_K small. Lipschitz constant: the same recursion.
7. *Large field.* Stiffness Re b_k >= 1 / (2 g_k^2), and (4.1) is about real V. So Theorem 4.3 holds with g_k^2 replaced by 2 g_k^2.

*Complex w and phases.* The modulus must never be taken through more than one level: |rho^w(1)| is smaller than rho^{Re w}(1) by a factor exp(c a^{-4} (Im w)^2 g^4), so a modulus bound at the bare level would lose an amount of order a^{-4}. In the step k -> k+1 the modulus is taken only over level-k variables of frozen cubes, and comparing Haar with the Gaussian at complex b_k costs |1 - w g_k^2|^{-n/2} per cube, which is 1 + O(g^2). Finer levels in that cube are already integrated, analytically in w, inside r_k^w. So there is **no loss of order a^{-4}**: this is the phase cancellation the gate asks about, and it follows from the level-by-level structure.

**6.2 The counterterm.** E(w) := log rho_K^w(1) - log rho_K^0(1), the source-dependent constrained partition function with the coarse field trivial, which is the named subtraction of (1.2). It is a convergent sum over levels of polymers at W = 1, so it is analytic and non-zero on the polydisc. Averaging over the lattice symmetries of Tor, E_sym(w) := avg_g E(w o g).

**6.3 CT1-CT4 from I^w(K) [DERIVED given I^w(k)].**
- *CT1.* <exp(w . s)>_Tor = exp(E(w)) [int r_K^w dW] / [int r_K^0 dW]. |int r_K^w dW| <= sup |r_K^w| <= exp(C |T_K|), from I^w(K). And int r_K^0 dW >= exp(-C |T_K|), from the ball |log W| <= g_K. So |<exp(w . s)>| <= exp(Re E(w) + c), with c = 2 C |T_K| depending on a_K, which is fixed, for **all** w in the class and not only the pattern. Since the left side does not change under g, CT1 holds for E_sym, by the geometric mean.
- *CT2.* E_sym(w o g) = E_sym(w) by construction, and E(conj w) = conj E(w), since rho^w is real for real w and analytic.
- *CT3.* By Mobius in the support of w, which is a scalar source with natural base point 0, E(w) = sum_k sum_X e_k(X; w|_X), with e_k(X; 0) = 0, |e_k(X; w)| <= C rho g_k^2 exp(-kappa |X|_k). (Check against the gate's reading: the leading term is n w_k g_k^2 per level-k variable, the quadratic part n w^2 g_k^4 / 2 is the contact term, dominated by level 0 at order a^{-4}, and the gradient part is of order Lam^2 a_k^2 g^4 per cell, which gives a^{-2}, as upper-chain Remark 3.3 expects. All three are local at each level, so they are additive on separated supports.) In E(sum w_i) - sum E(w_i) only polymers meeting two supports survive. Such a polymer has at least eta / a_k cells, so its level contributes at most C rho g_k^2 (v / a_k^4) exp(-kappa' eta / a_k). The sum over k converges with no dependence on a. So tau(v, eta) <= C rho v eta^{-4}. The bound e_k uses I^w(k)(b) at W = 1, where the white-noise expansion is the only input.
- *CT4.* On a torus of side L_T = 2^m P, Z = rho_K(1) int r_K dW. log rho_K(1) is a sum over levels of vacuum polymers at W = 1 that are the same functions on both tori, except those wrapping around Tor, at most C exp(-kappa P / a_k) per cell at level k, all of order one in the last levels. So log rho_K^{(L_T)}(1) = (L_T / P)^4 log rho_K^{(P)}(1) + O((L_T / a_*)^4). Also int r_K^{(L_T)} dW >= exp(-C (L_T / a_K)^4) and int r_K^{(P)} dW <= exp(C (P / a_K)^4). Together these give CT4, with c_F = C (a_* / a_K)^4. **Here the normalisation factors g_k^{n} are extensive at each level, and the last integral is at the fixed coupling g_K. So no log log(1/a) from the zero modes of Tor arises:** the torus at scale a_K has a bounded number of cells and a fixed coupling, so its zero-mode factor is a bounded constant. This answers the worry in gate item D2, whose mode count is at the bare coupling on a lattice of T cells. I have not compared the two counts line by line.

**6.4 Requirements on the consumer.** (a) My blocking factor L is odd and large, so the lattice is a = L^{-K} a_K, not dyadic. Tor has an even number T_K of last cells, so planes at multiples of P/2 are lattice planes. Lemma 7.2 of the upper chain needs even side and doubling at larger tori, not dyadic a. Its subsequence in a must be along L-adic values. **Request to the lead.** (b) CT1 is delivered for all w in the class, so the conjugate pattern is not needed on my side.

**6.5 Hostile pass on Section 6.** (a) The whole section is conditional on I^w(k), whose small-field part is sketched. (b) In CT3, e_k(X; w) needs Mobius in w-support to converge. That is the same analytic trick as Step 5 of the library proof, in a variable s_c multiplying w on cube c, and holds if I^w(k)(b) is analytic in w on a polydisc larger than the class, with bound at most C rho g_k^2 per cube. Not checked at the walk level. (c) Item 5 of 6.1 claims the marginal part of H^# is O(g^2 p^c). That is a size statement about the second moment of a polymer, and the cut breaks nothing, since it is symmetric, but I have not written the second-moment extraction for H^#. (d) E must absorb the quadratic contact term, of order a^{-4}, and it does: it is in the Mobius sum at level 0, where it has range a. (e) In CT1 the constant c depends on (a_* / a_K)^4 and on gamma, through g_K, and these are fixed. So c is large but cutoff-free.

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

**8.4 What |c_j| <= C_0 requires (CLASS-4), and why C_0 can be free of L.** Only differences enter (8.2), so c_j may be replaced by c_j - c_W, with c_W the same constant for the Wilson action on a lattice in its own units, which does not depend on j. That difference compares two operators with the same low-momentum form, so it is infrared safe, and no log coefficient needs to be recomputed for the perfect action. c_j is a one-loop quantity on the level-j lattice in level-j units. Split momenta at p_0 small. Below p_0: Hess F_j at low momentum is the universal operator -D^2 - 2 ad F, because (R4) reproduces constant curvature exactly, with no factor, and gauge invariance fixes the cubic and quartic vertices at leading order. The corrections are suppressed by |p|^a, so the low part converges to b log(1/mu) plus a bounded constant. Above p_0: it needs a bound on the propagator and the vertices up to fourth order, at the trivial background.
- Propagator: by Lemma 7.1, the quadratic form is at least ||d_j B||^2 with constant exactly 1, so with a Feynman term the propagator is at most 1 / p-hat^2. No L. [DERIVED.]
- Linear lift: Q_j depends only on n = L^j. [DERIVED.] So the quadratic form depends on n only, and not on how n factorises.
- Vertices: Section 9.

**8.4a The integrand of c_j - c_W [DERIVED by power counting, with symbol bounds from Theorem G; not line by line].** On the level-j lattice, in Feynman gauge, the one-loop functional is Phi[V] = -(1/2) log det H(V) + log det Gh(V), with Gh(V) = D_V^* D_V for the gauge group of that level, **the same for the perfect and for the Wilson form, so the ghost cancels in the difference.** Put H_W(V) = Hess A^{(j)}(V) + D_V D_V^*, delta(V) = Hess D_j(V), with D_j := F_j - A^{(j)} gauge invariant, H_t = H_W + t delta. With a background of amplitude e and momentum q, expand: delta = delta_0 + delta_1 + delta_2 + ..., H_t = H_0 + t delta_0 + H_{t,1} + H_{t,2} + ..., G_t := (H_0 + t delta_0)^{-1}. By Lemma 7.1 delta_0 >= 0, so ||G_t(p)|| <= 1 / phat^2 for all t, with no L. Then

    Phi_n^{(2)} - Phi_W^{(2)} = int_0^1 dt ( -(1/2) Tr[G_t delta_2] + (1/2) Tr[G_t H_{t,1} G_t delta_1] + (1/2) Tr[G_t H_{t,2} G_t delta_0] - (1/2) Tr[G_t H_{t,1} G_t H_{t,1} G_t delta_0] ).

Symbols at small p, q. delta_0 has size at most C p^4 (the perfect form differs from Wilson by O(P^4), which is the R = 1 + O(P^2) of Lemma 10.1's numerics, and analytically G_mu^{-1} = P^2 (1 + O(P^2)) since a(P) = 1 + O(P^2)). delta_1 has size at most C e (|p| + |q|)^3, and delta_2 at most C e^2 (|p| + |q|)^2. These hold because D_j has no F^2 term: a term of lower derivative order in the cubic and quartic vertices of a gauge-invariant functional would be tied by gauge invariance to an F^2 term, and odd derivative counts are excluded by the inversion in the hypercubic group. H_{t,1} has size C e (|p| + |q|), H_{t,2} size C e^2. All symbols are analytic in p, q in a strip, by the exponential decay of Theorem G, so the constants C come from moments of kernels, and depend on d only.

Power count of the coefficient of q^2 (two derivatives in q, which lower the degree by 2): each of the four terms has integrand at most C e^2 / p^2 for |p| >= |q| small, and int d^4 p / p^2 converges at small p. At large p, all are bounded. So

    |c_j - c_W| <= C_0(d), uniformly in j and L,

and the limit mu -> 0 of the mass regulator is harmless, since the difference has no infrared logarithm. Then (8.2) reads beta_{j+1} = b log L + (c_j - c_W) - (c_{j+1} - c_W) + O(g^2). So **(FLOW) holds for L >= L_0(d)**, given Theorem G, and the sign is from b > 0 alone. c_W itself is never needed. Level 0: c_0 = c_W exactly.

For the Wilson form the coefficient b: the mu-derivative of Phi_W^{(2)} is an integral dominated at p of order mu, where the lattice symbols equal the continuum ones up to O(mu^2). So its limit is the continuum value computed in 8.2. [Derived at this level.]

**8.5 Hostile pass on Section 8.** (a) Formula (8.1) is exact on covariantly constant backgrounds, while (SF4) extracts beta at momentum q -> 0 from a plane wave. Equality of the two coefficients is by gauge invariance, argued and not written. On non-constant backgrounds mu != 0 adds a term linear in mu, of higher dimension. (b) On a torus, constant non-abelian background needs a quantised flux, so the extraction needs T large; c_j is defined as a limit. (c) The neutral sector and torus zero modes appear equally in L_j and L_{j+1} and cancel, at leading order; not checked at second order in B through the nested means. (d) At low momentum the claim that Hess F_j is universal rests on F_j being close to the continuum action on smooth fields, uniformly in j. That is (CLASS-4). (e) C_0 is not computed, so L_0 is not explicit. Its independence of L rests on Theorem G's constants, which depend on d only. If a hidden L dependence appeared there, (8.2) would prove nothing. (f) The claim is one-loop plus O(g^2): the O(g^2) needs (SF3).

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
- *Gauge fixing [DERIVED].* Maximal tree gauge in each L-block, based at the block centre: for a gauge-invariant integrand, setting tree links to 1 has trivial Jacobian on Haar measure, at every field, rough or not, so there is no Gribov problem. It serves for frozen rough cubes. On the small-field slice it is badly conditioned, by a factor L^2 (4.6), and block Landau gauge is used there. On a near-flat block, Landau gauge is unique and its Faddeev-Popov factor is a local analytic functional.
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

**10.2 (LOC-NA) on the fine lattice: superseded.** Text 4.5 replaces it. Before that I tried three ways to get sup |F_fine| <= C eta^2 sup |d_k V| at all depths: level-by-level Whitney interpolation (F jumps across faces, so J has surface measures and the first Newton step carries a logarithm of 1/eta at the faces); a bootstrap from the stepwise bound (fine curvature only eta^{2 - c'} eps, so the holonomy of a level-k loop is eta^{-c'} eps and no patch gauge exists at block scale); and one-shot Newton from glued linear lifts, which looked viable but needs the composite nested map at all depths with local gauges. In the level-only scheme no fine-lattice field at depth occurs beyond the trivial background (9.4), so **the sup bound at depth is no longer an obligation.** I do not know that it is false. It is simply not used.

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

Steps 1 to 5 are complete at this level. Step 6 and the Holder modulus are one-step inputs in the level-only scheme, with xi = 1/L, from 4.5. So the gain is alpha < 1 and not Balaban's, and the expansion needs third order only. **I have not read his proof, and I do not know why he goes to fifth order; the likely reason is the regularity class he works in. Do not read this as an improvement on him until the Holder input is proved.**

**11.4 Hostile pass.** (a) Step 2 uses only sup curvature on the hull of X. For rough backgrounds it fails, but polymers are only evaluated on M^j(U) with U regular. (b) Step 3's linear term and Step 2 need each function to be gauge invariant. Resetting links to 1 outside a set would break this. **Resolved:** localise only in the white noise, not in V. Reset xi to 0 outside a set: 0 is invariant under the Ad rotation that accompanies a gauge transformation of the background. So the polymers e(Y; V) are indexed by xi-supports Y, are jointly invariant, and have V as a spectator with exponentially decaying sensitivity. 11.1 applies with radial gauge from Y: amplitude grows polynomially with distance, against the exponential decay of sensitivity. This is why I(k)(b) is stated with sensitivity and not with strict support. [Derived at this level.] (c) Step 5 requires covariance of the family under the full hypercubic group, which D3 has only as a mixture. It holds for the sum. (d) In 11.2 the size of P assumes a level-k variation is smooth at level j: this holds for lifts by 9.4, including for B rough at level k, since lifts are smooth below the level-k scale.
