lead: Anthropic/claude-opus-5-5/max 97c171d6-e01d-4994-bd7b-9cb6c6972d86
lease_until: <driver sets this>

## State of attack

**Formulation.** Hard-constraint block RG for SU(2) Wilson on a periodic 4-torus, with the quaternion-mean average with waypoints and a field-chosen base point (Text 1, 5.1, 5.4). This map is defined on the whole compact field space, it pushes Haar exactly to Haar, it gives a Markov kernel mu_W on the fields, and its linearisation is exactly the paired-contour Q of (R4). The induction is I(k) of Text 3.3, **level-only**: r_k is one function of the current field, equal to a small-field form on the regular region Om(V) times a large-field factor G_k(V) <= exp(-c_F eps_0 Y_k(V) / g_k^2), with Y_k the l^1 norm of the rough plaquettes. There are no frozen fine variables and no histories. Rough cubes where the next field is regular go into a hard-core gas in the fluctuation integral, and so into the polymers. The vacuum is subtracted exactly by rho_k(trivial coarse field); with a source this is the counterterm E of UV-CT (Text 6).

**The organising principle, found this round.** Two kinds of constant must be kept apart (Text 3.1, 4.5). *Linear* constants, of the abelian map at the trivial background, are exact or absolute, and free of L and k: ||Q_str||_{l^4} = 1, ||Q_str||_{l^2} <= 1 / L, Lemma 7.1, Lemma 10.1, (5.4), the Morrey and Agmon rates. Only these enter a margin or a contraction. *Nonlinear* constants, the radius and vertices of the map and of F_k beyond second order, may depend on L, and must not depend on k: Theorem G' gives that with a soft Taylor bound at each level and a recursion that cannot compound. Since eps_0 and gamma are chosen after L, nonlinear corrections lose every comparison. This removed most of what I had been calling hard.

**Order of constants.** Text 3.1: L large; R_t, M at most polylogarithmic in L; then c_F; then the nonlinear constants C(L, R_t); then eps_0 small against them; alpha = c_2 eps_0; eps_1 = eps_0 / (4 L^2); p(g); the source radius rho; then gamma. (FLOW) is no longer a hypothesis on L: Proposition 8.4.

**What is derived and what is believed.**
- Derived line by line: Lemma 1.1, Corollary 1.2, identity (1.2), Lemma 2.1, the linearisation in 5.1, identities (5.1)-(5.2), Theorem 5.5, Theorem 4.2, Lemmas 7.1, 7.2, Theorem 7.3, the star removal for q_k, the symbol bound QQ^* >= 1/3, (8.1), b, Lemma 10.1, **Lemmas 4.5a, 4.5b, 4.5c, Proposition 8.4, the quadratic core (4.2) of the excess**, and the three library proofs of mine.
- Derived at the level of each step, given the items named there: Theorem G' on a patch (given the gauge on unwrapped patches), Lemmas 4.5f, 4.5g, 4.5h (abelian), Proposition 4.5i, Lemma 8.5, Proposition 8.6, Theorem 4.3, (4.3), Lemma 4.4b, Proposition 11.1.
- Sketch or scheme: the Wilson term 8.7 (classical, not written out); (CUT) and (GAS); blocked tubes; the source induction 6.1.
- **Theorem I is a target. It is not proved.**
- Numerics. (i) `checks/hard-core--independent_defect_gain.py`, earliest line-averaged map, flat background: PASS-SHEET with max S = 1.000 at L = 3, 5, 7; single links at L = 3, 5 only, since L = 7 was stopped, so PASS-GENERIC is not evaluated at L = 7. **Those runs did not hold the numeric lock:** another push held it, my acquire failed, and I had piped its output through tail, which hid the failure. (ii) `checks/hard-core--independent_lift_form.py`, under a confirmed lock: see Lemma 10.1. (iii) `checks/hard-core--independent_field_ineq.py`, map D3 with the older rule threshold 0.5, under a confirmed lock, at L = 3, 5: PASS-55, max Ratio 1.000 and 0.999 against bounds 12.6 and 15.2, in the SHEET family; CHARGE exact to 2e-16; RULE-EFFECT below. These families can falsify (5.5). They do not confirm it on all fields, and no adversarial search was run. The script now has threshold 0.05 and a search mode, not yet run: the lock is held by another push until 02:30 UTC.
- RULE-EFFECT, TUNED2 on noise: with base fixed at y, min |m| falls to 0.005 to 0.012 at L = 3 and to 0.001 to 0.009 at L = 5; with the rule it stays near 0.56 and 0.73. |W - 1| is larger with fixed base by a factor of 8 to 9 at L = 3. At L = 5 the three seeds give factors 0.6, 21 and 1.7, so the first seed goes the other way. The rule does not lower |W - 1| on every sample; what it reliably does is keep |m| away from zero, which is the hypothesis of 5.3. All ratios are far below the bound here, since the noise inflates the right side. Three seeds per L are a small sample.

**The large-field answer so far.** Theorem 4.2 and Theorem 4.3: a large-field region regenerates the large-field hypothesis at the next step with the same constant, in one line from the field inequality (5.5), because the l^1 norm of rough curvature contracts by L^{-2} under averaging. Every rough coarse plaquette is paid either by fresh regular energy at the finer level, or by rough plaquettes at the finer level with a margin L^2 / C_OS. That margin pays the entropy. Rough cubes under a regular field are a dilute gas in the fluctuation integral, with the excess (4.3) as the cost. The divergent count LF-count is the vacuum part of that gas, cancelled by the named subtraction, and the rest is irrelevant after extraction. I do not claim this is Balaban's R operation: his bodies could not be read (Project Euclid and Deep Blue both served bot checks, and I stopped there).

**Hardest remaining inequality: (GAS), the relative weight of a set S of large cubes in a form the cluster library can use.** For W in the class, the part of (1.2) with large set S, relative to the part with S empty, should be

    rho(S; W) = prod_{c in S} z_c(W) * exp( sum_{T subset S} v(T; W) ),     |z_c| <= exp(-c_3 / g_k^2),   |v(T)| <= C(L) exp(-c tree(T)),

with z, v analytic in W, jointly with the small-cube polymers, with a chart that depends on S only within one cube of S, and with mid cubes included, so that disjoint polymers really are independent and Steps 3 to 5 of the library apply. The single-cube bound is (4.3) with Lemma 4.4b. **What is not written is the joint expansion: S changes the Gaussian non-locally through C_S and C_rem, and a hard-core gas needs exact independence of disjoint polymers.** My route: for fixed S and xi', the first part of the chart is strictly local in xi; the determinant ratio is exp(sum_T v(T)) by the path expansion, and a Mayer expansion of the bonds e^{v(T)} - 1 joins cubes into new polymers, whose activity is paid by exp(-c_3 / g^2) per large cube. I believe this; it is not done. Last round's candidates are down: C_0 free of L was not required (Proposition 8.4), the energy and determinant parts of a single hole are (4.3) and Lemma 4.4b, and (COV) was bypassed by Proposition 4.5i. **Theorem G's sup norm turned out to be wrong near corners of Lambda, which nobody had flagged, so a similar geometric error could hide elsewhere.** Items next in line: the cell-by-cell gauge on unwrapped patches; the lattice Gehring lemma; blocked tubes in the same gas.

**Routes tried and why they failed** (Text 1.5, 2, 5.4, 7, 10): fattening Lambda with a filling rule (unproved volume bound, unnecessary after unwrapping patches); hole filling for the Morrey bound (fails where the local pattern has a loop, replaced by reverse Holder); a global covariant fine-lattice saddle on Om (no global small gauge; replaced by Proposition 4.5i); one-link solve (variance grows linearly with level); entire reference-path average (rough path keeps full weight; fine action no longer dominates at large curvature); line-averaged prefix (star cancels only approximately at large field); iterating the fiber flow for complex bounds (L^2 per level); one-function pointwise induction on all V (entropy compounds unless an excess lemma is proved for arbitrary fields, replaced by frozen islands, later by 4.3); pricing a tower at tuned block centres (needed a density bound I could not prove, replaced by the field-chosen base point of 5.4); two thresholds in recycling (non-analytic indicator, removed); stepwise regularity of the lift (shape factor compounds, replaced by the critical-norm recursion); direct sign analysis of beta per level (dia and constraint terms have no sign; superseded by the telescoping (8.2)); fine-lattice regularity at all depths (three routes, made unnecessary by the level-only scheme); recursion for the third-order part of F_k (needs C_src level by level, replaced by the one-shot Theorem G'); a hard cut on xi in the first version of (EI) (it ignores that |B| < eps_1 is a non-local, sharp function of xi); an analytic cut in B alone (the chart ends at the box, so the integrand is undefined where the analytic cut is merely small; replaced by the polynomial square root in 4.6); that square root in maximal tree gauge (condition number L^4); the same in Landau gauge per block (crossing links large by a factor L in any gauge that is discontinuous across faces, edge of the spectrum L^{-3}; replaced by the Feynman term on the group G_0 of zero block averages); estimating the nested map with Q_root in place of Q_str (norm C_d > 1 per level, compounds); frozen islands with histories and a tree count (worked in outline but carried multi-scale boundaries, replaced by Theorem 4.3); bounding the shift of the constraint by the fraction of bad paths (a term f^2 loses for dense rough sets; replaced by Fenchel-Young with the exact lift in 4.4); a large-field cost of order f^2 per rough plaquette (no margin, the coefficient decays along the flow with the sum of g_k^2 log(1/g_k), Text 4.2); **the sup-norm fixed point of the first Theorem G' near Lambda (curvature r^{-1/3} at re-entrant edges, so not uniform in k; replaced by Theorem G'); demanding C_0 free of L (not consumed; the flow is used only in telescoped form); parity for the second moment of H^# (not needed, size suffices, 6.1); amplitude times cut small in the spectator expansion of (CUT) (false as g -> 0 for fixed range; replaced by Cauchy in the imaginary direction only).**

**Next action.** Write (GAS) line by line: the S-dependent chart, the Mayer step for v(T), and blocked tubes as more large cubes. Then the lattice Gehring lemma and the cell order on unwrapped patches. When a lock is confirmed (held by another push until 02:30 UTC): `field_ineq.py search 3 300`, then rerun the families with threshold eps_0.

## Obligations
- discharged: Lemmas 4.5a, 4.5b, 4.5c, critical composite bound uniform in k, line by line -> Theorem G'
- discharged: lattice Sobolev, box gauge and union of boxes, proved in library/lattice_sobolev_box_gauge.md with credit to Gagliardo, Nirenberg, Loomis, Whitney -> Lemma 4.5d
- discharged: Proposition 8.4, what the induction consumes from the flow, with C_0(L) allowed -> Theorem 4.3, 6.1, 9.6, trajectory in UV-CT
- discharged: quadratic core (4.2) of the excess -> (4.3)
- unchecked: gauge of Lemma 4.5d on unwrapped patches, an order of adding cells with connected facet overlaps, for every pattern (Text 4.5, library Lemma 6) -> Theorem G' near Lambda, 4.5f, 4.5h
- gap: lattice Gehring lemma and lattice HLS, with credit, to be proved in library/ -> Lemma 4.5h
- implication: Theorem G' on a patch, given the gauge on unwrapped patches -> Theorem P, (COER), I(k+1)(a)
- implication: Lemmas 4.5f, 4.5g, 4.5h abelian, given the gauge on unwrapped patches -> locality, regularity of V^*, (4.3)
- implication: Proposition 4.5i, (4.4), from patches to Om, level by level, given Theorem G' on patches -> I(k+1)(a), 4.6, 7.3
- implication: Lemma 8.5, derivative count, given Theorem G' on the torus and Steps 1 to 5 of Proposition 11.1 -> Proposition 8.6
- implication: Proposition 8.6, |d_j| <= C_0(L) uniformly in j, given Lemma 8.5 -> (8.2)
- unchecked: Wilson term 8.7, b log L with no constant, classical one-loop comparison not written out -> (8.2)
- implication: Theorem 4.2, Theorem 5.5 -> Theorem 4.3
- gap: rerun the field-inequality check with threshold eps_0 in the rule, and an adversarial search -> confidence in Theorem 5.5
- implication: large-field regeneration, Theorem 4.3, given (4.1), I(k)(a), (c), (T2) and exterior polymer bounds -> I(k+1)(c)
- implication: (4.3), nonabelian excess, given 4.5g, 4.5h and Theorem G' -> I(k+1)(b)
- implication: Lemma 4.4b, hole determinant, given 4.5g and (CUT) item 1 -> relative activity of large cubes
- unchecked: (GAS) and (CUT), the joint expansion with S-dependent chart, written step by step, with the spectator step corrected (Text 4.4, 4.6) -> I(k+1)(b)
- discharged: (EI) on small cubes, exterior polymer bound by expansion in the white noise, given Theorem G' and 7.3 (Text 4.6) -> I(k+1)(b)
- gap: blocked tubes as a local factor in I(k), checked through one step (Text 4.4) -> I(k+1)
- implication: irrelevance, Proposition 11.1, given the lift bounds of 4.5 and 9.4 (near corners only the Morrey gain: not checked for every polymer term) -> I(k+1)(b)
- implication: decay of the level-k covariance at rate c / L, given the form bounds (Text 7.3) -> 4.6
- unchecked: I^w(k) -> I^w(k+1), written term by term in Text 6.1, given (EI), Theorem G' and 11.1 -> UV-CT
- implication: UV-CT, CT1 to CT4, given I^w(K) and Proposition 8.4 -> upper-chain
- discharged: Lemma 1.1 exact Haar pushforward -> Corollary 1.2, recursion (1.2), mixed bonds
- discharged: Lemma 2.1 fiber flow -> checks
- discharged: exact identity (5.1), inequality (5.2) -> (5.5)
- discharged: Theorem 5.5, field inequality at every real field; the rectangle filling is standard and not enumerated -> Theorem 4.2
- discharged: linearisation of the final map equals (R4) -> propagator setting, (R5), (R7)
- discharged: Lemmas 7.1, 7.2 and Theorem 7.3, abelian coercivity uniform in k -> Theorem P
- discharged: QQ^* symbol bound for Q_str -> Text 7, (CUT) item 1
- discharged: one-loop telescoping identity (8.1) on covariantly constant backgrounds -> (8.2)
- discharged: coefficient b = 11/(3 pi^2), continuum heat kernel -> (8.2)
- discharged: Lemma 10.1, two-sided bound on the abelian perfect form, every n -> Lemma 4.5e, 9.4, Theorem G', Text 6
- discharged: maximal tree gauge, trivial Jacobian at every field -> exterior integral, frozen cubes
- discharged: ultralocal cluster expansion, proved in library/ultralocal_cluster_expansion.md with credit to Dimock and Balaban -> 11.2, 4.4
- discharged: path expansion of an inverse and Mobius locality, proved in library/path_expansion_locality.md -> 4.4, 4.5
- discharged: per-polymer gauge invariance by localising in the white noise only -> Proposition 11.1

## Requests
- Target lead, gate request: the large-field sector, Text 4.1 to 4.4 and Theorem 5.5, is ready for a hostile check. It is the part of this file that answers the charter's question directly: Lyapunov inequality, regeneration with no history, and where the 4D count goes. Theorem G' and Lemma 4.5a in Text 4.5 are next.
- Target lead: Text 6 maps this induction onto UV-CT. CT1 for all w in the class, CT2, CT3 and CT4 follow from I^w(K), with E the named subtraction rho_K^w(1) averaged over lattice symmetries. Please confirm two things. (1) The trajectory can run along a = L^{-K} a_K with L odd and large: Tor has an even number of last cells, so its reflection planes are lattice planes. The upper chain's dyadic a is then replaced by L-adic. (2) Gate item D2 counts modes at the bare coupling. In my scheme the zero-mode factor of Tor is at the fixed coupling g_K, on a bounded number of cells. If the checker sees a log log(1/a) in Text 6.3 CT4, I want the line.
- FROM TARGET LEAD, gate on UV-CT (`git show origin/claude/ym4d-hard-route:.claude/science/physics-loops/ym4d-hard-route-20261030/gates/uv-ct-upper-chain-41489e4876.md`): noted. CT3 is addressed in Text 6.3 by Mobius in the source support, CT1 at complex sources in Text 6.1.
- FROM TARGET LEAD, 2026-10-30: interface changed from UV-EXT to UV-CT. Consumed: Text 6 has been rewritten. The earlier real-s request is withdrawn. I read `parts/upper-chain.md` for the interface statement and its requests only, and I have not read the mapped attempt.

- Target lead, from this round. (1) Theorem G on Om was wrong near corners of Lambda; Text 4.5 replaces it with Theorem G' in the critical norm. (2) (FLOW) is now Proposition 8.4 and needs no large-L sign per step; g_0(K) need not be monotone in K unless C_0(L) is small against b log L. Does the upper chain use monotonicity of the trajectory in K? (3) Files `library/critical-class-and-excess.md`, `library/block-poincare-energy-package.md`, `library/convex-laplace-tree-decay.md` appeared in the shared directory. I did not author them, I read only their names, and I am leaving them unread for independence. Their titles suggest an overlap with Text 4.4, 4.5 and 7. A comparison by someone outside both attempts would be valuable, since independent arrival at the critical norm would mean something only if it really is independent.

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

**3.1 Order.** See the principle in 4.5: linear constants are free of L and k, and they alone enter margins and contractions; nonlinear constants may depend on L and are beaten by the choice of eps_0.
1. The rates delta_0, c, sigma of 4.5, 7.3: absolute.
2. L odd and large, for the margins: Theorem 4.2 (L^2 >= 8 C_OS O (1 + C_M)), the excess (4.3), and the contraction by (M / L)^a. Not for (FLOW): Proposition 8.4.
3. Patch radius R_t = C log L (4.5i). M = M(L) >= C log L, with L >> M, and C_M = C M^4 polylogarithmic in L. The range of the polynomial square root in (CUT) has to fit a level-(k+1) cube of side M, and truncating tails needs M_1 >= C log L. (An earlier version had M absolute. That does not survive the truncation.) M large enough for kappa = c M to run the cluster library, with c absolute by 7.3.
4. C_OS <= C log L (5.5). c_F := c_A / (8 C_OS^2 O), O the overlap number of hulls.
5. Nonlinear constants C(L, R): C_Y, alpha(L), rho_*, the vertex bounds of Theorem G', the constants C_0, C_2 of Proposition 8.4.
6. eps_0 small: at most c_1 L^{-2} for fiber stability, and small against C(L, R)^{-1} and against any power of 1/L that a margin requests. No lower bound on eps_0 is used anywhere.
7. alpha := c_2 eps_0, complex radius, with c_2^2 <= c_F / (C M^3). eps_1 := eps_0 / (4 L^2), the cut on the fluctuation.
8. p(g) = (log 1/g)^{p_0}, 2 p_0 > 1: white-noise cut.
9. rho, the source radius, may be chosen here, so it may depend on L (6.4).
10. gamma, last and small against everything above.

Compare 5.6 of an earlier version of this file, where M > L forced a grace period: with L >> M a cell is already small against a block, and that whole mechanism is gone.

**3.2 Regions and functionals.** For V on T_k: f_p = |V_p - 1|. Rough plaquettes: f_p > eps_0. Y_k(V) := sum over rough p of f_p. Lambda(V) := the cells containing rough plaquettes; Om(V) := its complement. Near: plaquettes in Lambda(V), or within distance 2 of it. E_k(V) := sum over plaquettes neither rough nor near of f_p^2. There are at most C_M := C M^4 near plaquettes per rough cell, each with f <= eps_0, and at most Y_k / eps_0 rough cells, so the sum of f over near plaquettes is at most C_M Y_k.

For a union of cells Om and V regular on Om, F_{k,Om}(V) is the **classical functional with free boundary**, defined tropically: F_{0,Om} = A on Om, and F_{k+1,Om'}(W) := min of F_{k,Om}(V) over the regular slice of the fiber, with constraints only on bonds with both blocks in Om'. Directly from the definition:

    Adding a constraint or frozen boundary data can only raise the minimum: F_{k+1,Om'}(W; frozen) >= F_{k+1,Om'}(W).                          (3.1)

**3.3 Statement I(k).** For every real V on T_k,

    r_k(V) = exp( -g_k^{-2} F_{k,Om}(V) + EE_{k,Om}(V) ) G_k(V),     Om = Om(V),                                                                (3.2)

which *defines* G_k > 0, such that:

(a) *Classical.* On regular V, F_{k,Om} = qcov_n + N_k, with n = L^k, qcov_n the gauge-covariant form of the exact quadratic perfect action of Text 7.1, 10.1, and N_k gauge invariant of third order in the curvature, with density bound |N_k density| <= C_N (local |F|)^3 uniformly in k (Theorem P, 4.5, from Theorem G'). In particular F_{k,Om}(V) >= c_A E_k(V on Om) with c_A >= 1/4.

(b) *Quantum.* EE_{k,Om} is gauge invariant and analytic on the complex class C(Om; eps_0, alpha), EE_{k,Om}(1) = 0, and it is a sum over xi-supports Y of functions e_k(Y; V), each gauge invariant, with sensitivity to V decaying exponentially away from Y at rate kappa / M, |e_k(Y)| <= E_0 exp(-kappa d(Y)), and sum_Y |e_k(Y)| <= C_E |Om| on the class.

(c) *Large field.* G_k(V) <= exp( -c_F eps_0 Y_k(V) / g_k^2 + B_0(g_k) |d Lambda(V)| ), with B_0(g) polylogarithmic in 1 / g, and more precisely the same bound with V complex on Om in the class and real on Lambda, with G_k analytic in the data on Om near Lambda and independent of V on Om far from Lambda up to the terms in (b). In a complex field the superadditivity of 4.3 holds up to a real part: for the analytic gap Delta >= 0 at real fields, Re Delta(V_r + i u) >= - C |u|^2 per affected cell, with C linear, since the first-order term is imaginary, and this is below the cost for c_2^2 C <= c_F. Polymers of EE within r_2(g_k) of Lambda are in G_k (4.6, (CUT) item 4).

(d) *Symmetry.* All objects are gauge invariant and covariant under the lattice symmetries of T_k.

**Theorem I (target).** If g_k <= gamma for all k <= K, then I(k) holds for all k <= K, with constants independent of k, K and the volume. The flow is defined by extracting the marginal part from EE_{k+1} (11.1), and Proposition 8.4 gives what the step needs from it, jointly with I(k), by induction on k.

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

where (C / g_k)^{n_f |H|} is the comparison of Haar with the vacuum Gaussian, and n_f the number of level-k variables per level-k cell. By (4.1) the exponent is at most -2 c_F eps_0 Y_{k+1}(W) / g_k^2, and |H| <= C L^4 Y_{k+1}(W) / eps_0 since each rough coarse plaquette has phi > eps_0. So the entropy is at most C L^4 n_f eps_0^{-1} log(C / g_k) Y_{k+1}(W), which is below (1/4) c_F eps_0 Y_{k+1}(W) / g_k^2 when g_k^2 log(1/g_k) << c_F eps_0^2 L^{-4}, true for g <= gamma. So the exponent is at most -(7/4) c_F eps_0 Y_{k+1}(W) / g_k^2, and g_{k+1}^{-2} <= (7/4) g_k^{-2} by (T2) of Proposition 8.4. **Monotonicity of the flow is not used.** Hence

    G_{k+1}(W) <= exp( -c_F eps_0 Y_{k+1}(W) / g_{k+1}^2 + B_0 |d Lambda'| ).

**No constant has degraded.** This is the answer to the charter's question, for the bound: a large-field region regenerates hypothesis (c) at the next step, with the same c_F, in one line from (5.5), and with no history, no frozen fine variable, no excess lemma, and no tree count. Hypotheses (a), (b) are in 4.5, 4.6.

**4.4 Recycling: rough cubes where W is regular [SKETCH].** Let W be regular on Om', and let V in the fiber have rough cubes inside. There are three types of cube at level k: small (white noise within the cut p(g)); mid (white noise above the cut, |B| < eps_1), weight at most exp(-p^2 / 2) with no entropy, since the Gaussian is normalised; large (|B| >= eps_1, or V rough), frozen, integrated by Haar. A large cube has activity relative to the regular replacement at most exp(-c_F' / g_k^2) (C / g_k)^{n_f M^4}, by the excess bound below.

*Excess (Lemma 4.4a) [quadratic core DERIVED line by line; nonabelian form by Taylor at V^*, derived at the level of each term].* Let W be regular near a set of large cubes, with V^* := V^*(W), mu_* = d_c^* Pi its multiplier, and sup |Pi| <= C sup |F'| by Lemma 10.1 and 4.5g. Let V be in the fiber, with hole H: the links that lie in a rough or near plaquette, or that have |B_b| >= eps_1 relative to V^*, so that V = exp(iB) V^* with |B| < eps_1 on the exterior Ext. Let R be the coarse defect, the difference of W and M(exp(i B_tilde) V^*), where B_tilde is B on Ext and 0 in H.

*Quadratic core.* Abelian and fine-lattice. Let f^* = da^* be the minimal fine curvature for W on the whole region Omega_0, so d^* f^* = Q^* mu_*. Let a be any fine field on the exterior Omega = Omega_0 \\ H, and a_tilde an extension to Omega_0, with coarse data W - R. Fenchel-Young on each plaquette of Omega gives (1/2) |da|^2 >= <f^*, da> - (1/2) |f^*|^2. Sum over Omega, and write the sum over Omega as the sum over Omega_0 minus the sum over the hole. Then <f^*, d a_tilde>_{Omega_0} = <mu_*, W - R> = 2 F_{k+1}(W) - <Pi, d_c R>, and (1/2) ||f^*||^2_{Omega} = F_{k+1}(W) - (1/2) ||f^*||^2_{hole}. So, exactly,

    (1/2) ||da||^2_Omega >= F_{k+1}(W) - <Pi, d_c R> - <f^*, d a_tilde>_{hole} + (1/2) ||f^*||^2_{hole}.                        (4.2)

**No filling of the hole is needed, and no restriction on the size of the rough field enters, because only the coarse defect R and the local curvature of the lift appear.** The sum (R5) is used through d_c R(P) = sum_p w_p (difference of plaquettes near H), so |d_c R(P)| <= C_w L^{-2} sum over rough and near p in hull P of (f_p + eps_1), by (5.4). Take a_tilde in H from a reflection of a across a collar cell, and from a lift of B_tilde inside thick parts, so that ||d a_tilde||_{hole} <= C ( ||da||_{collar} + ||d_k B_tilde||_{hole} ). With Young, <f^*, d a_tilde>_{hole} <= theta ||da||^2_{collar} + C_theta ||f^*||^2_{hole} + C ||d_k B_tilde||^2_{hole}, and theta ||da||^2_{collar} is absorbed by using weight 1/2 - theta in Fenchel-Young on the collar, at a price C ||f^*||^2_{collar}. Then Lemma 4.5h gives ||f^*||^2_{cell} <= C L^{-2 sigma} sup |F'|^2.

*Nonabelian.* Expand at V^*, where everything is exact to the order needed. F_{k,Ext}(exp(iB) V^*) = F_{k,Ext}(V^*) + <grad F_{k,Ext}(V^*), B> + (1/2) <B, Hess B> + O(C(L, R) |B|^3). Three facts: (i) F_{k,Ext}(V^*) >= F_{k,Omega_0}(V^*) - C ||f^*||^2_{near H} (1 + C(L, R) eps_0): the second order of the region dependence is the core above with B = 0, and the third order has a factor eps_0 C(L, R), small by the choice of eps_0. (ii) grad F_{k,Omega_0}(V^*) = (Q^{V^*})^* mu_* and the region difference of the gradient is local to H, with size at most C |f^*| exp(-delta_0 dist); so the first-order term equals <mu_*, Q^{V^*} B_tilde> up to C sup_{near H} |f^*| eps_1 |H|. By the expansion of M, <mu_*, Q^{V^*} B_tilde> = -<Pi, d_c R> + (1/2) mu_* . Hess M (B_tilde, B_tilde) + ..., and the last term combines with Hess into the Lagrangian H_L. (iii) On Ext, with the gauge of (CUT) item 1, <B, H_L B> >= c ||grad B||^2 up to C sup |mu_*| C(L, R) (|R|^2 L^2), which is at most sup |F'| |R| for |R| <= eps_0 by the choice of eps_0. So, with |H| <= C_M Y_k / eps_0 and sup |F'| <= eps_0,

    F_{k,Om(V)}(V) >= F_{k+1,Om'}(W) + (c / 2) ||grad B||^2_{Ext} - C C_M ( L^{-2 sigma} + L^{-sigma - 2} + L^{-2} ) eps_0 Y_k(V).     (4.3)

For L large the last coefficient is below c_F / 2. So relative to the regular replacement, **the net cost is at least (c_F / 2) eps_0 Y_k / g_k^2, with no restriction on Y_k.** If |R| > eps_0 on some coarse plaquette, then it is the case treated by F >= 0: the loss is at most C eps_0^2 per such coarse plaquette, and |R| >= eps_0 forces Y_k(hull) >= eps_0 L^2 / C_OS by (5.5), so the cost is larger than the loss by L^2 c_F / C_OS. *First versions, both wrong:* bounding the shift by the fraction of paths through the rough set, which keeps a term f^2 and loses for dense rough sets; and treating F_{k+1}(W) as (1/2) |F'|^2, which misses its coarse-momentum dependence (R goes up to 12 at P = (pi, pi, pi, pi)). The Fenchel-Young form uses the exact lift f^* and so is sharp. For a cube that is large only through |B| >= eps_1, (4.3) with S empty gives c ||grad B||^2 >= c' L^{-2} eps_1^2, by the Poincare bound of (CUT) item 1.

    c_F eps_0 Y_k - |F'| C_OS L^{-2} Y_k >= (c_F - C_OS L^{-2}) eps_0 Y_k >= (c_F / 2) eps_0 Y_k,

for L^2 >= 2 C_OS / c_F, and this holds with no restriction on Y_k. If R is so large that W with the shift is outside the regular region, use F >= 0: the loss is then at most F_{k+1}(W) on those cells, at most C eps_0^2 per coarse plaquette, and |R| >= eps_0 forces Y_k >= eps_0 L^2 / C_OS, so the cost c_F eps_0 Y_k is at least c_F eps_0^2 L^2 / C_OS, larger by a factor L^2 c_F / C_OS. **My first version bounded the shift by the fraction f of paths through S and kept a term f^2, which lost for dense S. Both were wrong: bad paths deviate by the curvature they enclose, not by 2, and the second-order term has a sign.** For type Z, convexity on the slice gives c eps_1^2 / g_k^2.

*Hole determinant (Lemma 4.4b) [DERIVED at the level of each step; trivial background first, corrections by the choice of eps_0].* Let the hole H contain **all links of near plaquettes**, so that links next to a hole with reduced stiffness are not in the Gaussian at all. They are integrated by Haar. Let X_S be the variations on Ext, extended by zero to H, tangent to the constraint with V|_H frozen. Three facts.
1. *Stiffness.* For b in X_S, d_k b vanishes on near plaquettes. So q_{n,Ext}(b) >= ||d_k b||^2 on all plaquettes, by Lemma 7.1 on plaquettes with hull in the region. With the gauge term of (CUT) item 1, the form on X_S is at least c L^{-2} ||b||^2 with c absolute, **for every hole**, since extension by zero embeds X_S in the unholed space. No shape constant enters.
2. *Region dependence.* Delta := q_{n,Om} - q_{n,Ext} >= 0 on X_S, by monotonicity (3.1), and by 4.5g, Delta(b, b) <= C exp(-2 delta_0 d(b, H)) for a unit link b. So Tr Delta <= C |H|.
3. *Constraint with frozen links.* The tangent constraint Q_S differs from Q on bonds whose paths meet H. On an unblocked tube at least three quarters of the crossing paths avoid large cubes, and on those Ad(T_u) is close to 1 at V^*. So the sum over crossing links is bounded below by 3/4 - 1/4 - small = 1/2 - small, even if the other quarter is rotated arbitrarily, and Q_S Q_S^* >= c on each coarse bond. This is what the threshold one quarter is for.

So, with H_S the form on X_S, interlacing for the compression of the full form H to X_S gives det H / det(H compressed) <= ||H||^{n_H}, with n_H the number of removed variables. Duhamel with 2 gives log det(H compressed) - log det H_S <= c^{-1} L^2 Tr Delta <= C L^2 |H|. Coarse-bond Jacobians contribute C(L)^{(number of bonds near H)}. The result is that **the exterior Gaussian with holes, relative to the full one, is at most (C / g_k)^{n_H} C(L)^{|N(H)|}**, the factor 1 / g_k per removed variable being the Haar comparison. Each is local to H. The Mobius decay in S follows from the path expansion below. Together with (4.3) this gives the relative activity of a large cube: at most exp(-(c_F / 2) eps_0 Y_k / g_k^2) (C / g_k)^{n_H} C(L)^{|N(H)|}, and since Y_k >= eps_0 |H| / C_M, this is at most exp(-c_3 |H| / g_k^2) with c_3 = c_F eps_0^2 / (4 C_M), for g <= gamma.

*Summation.* For fixed S the exterior is a Gaussian on the complement of S with spectator W. The dependence of its logarithm on S has to decay in the distances between holes, and that is the only multi-body input. By `library/path_expansion_locality.md`, the inverse of the exterior form on the complement of S is a sum over paths of patches, each term depending on S only at patches on its path. log det is an integral of a trace of such inverses, and C_S^{1/2} is a contour integral of resolvents, so the same holds for them. Mobius differences in S then pick out paths visiting all of S, and decay in the tree length of S at the rate of 7.3. The hard-core gas of large and mid cubes has activities bounded by a tiny number per cube, and steps 3 to 5 of the cluster library proof, which use only a bound on z(Y), exponentiate it. The result is EE^R(Y; W) in EE_{k+1}. *Scale of cubes.* The fluctuation at level k has range L in level-k units, so white noise is grouped in level-(k+1) cubes of side M, that is M L in level-k units; rough sets are subsets of these, and the factor (1 + tiny)^{(L M / M)^4} is harmless. [Sketch.]

*The divergent count.* Per level-(k+1) cell the recycled gas has activity about L^4 M^{-4} exp(-c / g_k^2), tiny, at every level. Summed over all cells of T_{k+1} and over levels it is of order |T_phys| L^{4(K-k)} exp(-c / g_k^2), which diverges if c beta < 4. This is Proposition LF-count of the program [arithmetic re-derived]. In (1.2) its value at W = 1 goes into the named subtraction and cancels exactly. Its W-dependence is irrelevant after extraction (11.1), with marginal shift of order exp(-c / g_k^2), summable in k. **That is where the 4D price goes.** Nothing in this scheme bounds the count, and no condition on c beta arises.

*Blocked tubes.* If at least a quarter of the crossing paths of a tube pass through large cubes, the exterior cannot carry the constraint with the implicit function theorem, and that term is not analytic in W, even with W regular. Such a V has at least (L / M)^3 / 4 large cubes, so its weight is at most exp(-c (L / M)^3 eps_0^2 / g_k^2), far below everything else. It is kept out of EE_{k+1} and carried in (3.2) as a factor 1 + b_{k+1}(c; W) over blocks, with 0 <= b_{k+1} tiny, real, local. At the next level its cube counts as large, with W frozen and real. So I(k) needs this extra factor, and (c) must be read with it. [Scheme. Not checked in detail.]

**4.5 Theorem P (classical functional): a fixed point in the critical norm.**

*Why the earlier proof was replaced.* The first version of this section solved the nested constrained problem on the fine lattice in the norm sup |a| / eta + sup |grad a| / eta^2. That proof is correct on a box, where the Neumann Green's function has the free-space bound by reflection, but the gluing step used it on every patch of Om, and a patch next to a corner of Lambda is not a box. At a re-entrant edge of a free boundary the minimal field is singular: take the cross-section with an L-shaped domain; a curl-free, divergence-free field with natural boundary condition is the gradient of a function that is constant on the boundary, and that function behaves like r^{2/3} sin(2 theta / 3), so |F| ~ r^{-1/3}. In level-k units the fine curvature is then larger than eta^2 eps by a factor n^{1/3} at the edge, so the sup norm is not uniform in k. **This is not a counterexample to any conclusion, since r^{-1/3} is well inside l^2 and l^4, but the old proof did not cover it, and I had not noticed.** The route below uses no sup norm on the fine lattice and no derivative of a. It also makes the star harmless.

*The principle.* There are two kinds of constant. **Linear constants** belong to the abelian map at the trivial background: Lemma 4.5a, Lemma 7.1, Lemma 10.1, (5.4), the rates in Lemmas 4.5f to 4.5h. They are exact or absolute, free of L and of k, and they are the only ones allowed to enter a contraction or a margin. **Nonlinear constants** are the radius and the vertices of the map and of F_k beyond second order. They may depend on L and on R, and they must not depend on k. Since eps_0 is chosen after L, every nonlinear correction is smaller than any fixed power of 1/L that a margin asks for.

**Lemma 4.5a (the linear map on l^p) [DERIVED, exact].** Q_str acts componentwise. A bond c' along mu has weights q(c', b) = L^{-3} tri(b) on the mu-links of its two blocks, with row sum sum_b q(c', b) = L, by 5.1. For a fixed mu-link b, the two bonds that use it have tri values summing to 1, so the column sum is sum_{c'} q(c', b) = L^{-3}. By Holder,

    ||Q_str B||_{l^4(T_{i+1})} <= ||B||_{l^4(T_i)},      ||Q_str B||_{l^2(T_{i+1})} <= L^{-1} ||B||_{l^2(T_i)}.

Indeed |Q B(c')|^p <= L^{p-1} sum_b q(c', b) |B_b|^p, and summing over c' gives the factor L^{p-1} L^{-3}, which is 1 at p = 4 and L^{-2} at p = 2. **So l^4 is exactly critical, with norm one at every step, and l^2 contracts by 1/L.** Compositions Q_str^i have the same bounds with no constant.

**Lemma 4.5b (one step) [DERIVED].** For a level-i field, let h(y)(B) := avg_x B(path(y -> x)), the star term of 5.1, Xi(y) := exp(i h(y)(B)), and for a coarse bond c' = (y, y') put B'(c') := log[ Xi(y)^{-1} M(exp(iB))(c') Xi(y') ]. On the polydisc |B_b| < alpha(L) no plaquette is rough, the rule of 5.4 picks x_0 = y, and the means are non-zero, so B' is an analytic function of the finitely many variables B|_{hull c'}. Its linear part is Q_str B(c') by 5.1. So

    B' = Q_str B + Y(B),      |Y(B)(c')| <= C_Y(L) sup_{hull c'} |B|^2 <= C_Y(L) ||B||^2_{l^4(hull c')},

on the polydisc, also for complex B, since a sup norm is at most an l^4 norm. C_Y and alpha depend on L only, **and the same function Y occurs at every level**. By covariance of M, the gauge factors Xi at level-(i+1) sites only conjugate at the next level, so B' is gauge equivalent to M(exp(iB)) for all gauge-invariant purposes. [This is a finite-dimensional Taylor bound, and that is the point: at fixed L nothing about the star, about reflection cancellations, or about fine-lattice regularity is needed here.]

**Lemma 4.5c (composite map, no compounding through levels) [DERIVED, line by line].** Let a be a field on a region of T_0, A := ||a||_{l^4}, B_0 := a, B_{i+1} := (B_i)'. Let O_L be the overlap number of hulls and C' := C_Y(L) O_L^{1/2}. If 6 C' A <= 1 and 2 A < alpha(L), then for every i,

    B_i = Q_str^i a + D_i,      ||D_i||_{l^2(T_i)} <= 6 C' A^2,      sup |B_i| <= 2 A.

*Proof.* D_{i+1} = Q_str D_i + Y(B_i), D_0 = 0. By Lemma 4.5b, ||Y(B)||_{l^2(T_{i+1})}^2 <= C_Y^2 sum_{c'} ||B||_{l^4(hull c')}^4 <= C'^2 ||B||^4_{l^4(T_i)}. By Lemma 4.5a, and since l^2 norms dominate l^4 norms on a lattice, ||B_i||_{l^4} <= A + x_i, with x_i := ||D_i||_{l^2}. So x_{i+1} <= L^{-1} x_i + C' (A + x_i)^2. If x_i <= 6 C' A^2, which is at most A, then x_{i+1} <= (6 / L + 4) C' A^2 <= 6 C' A^2 for L >= 3. The sup bound follows from sup <= l^4.  []

*Local form.* B_k(c) depends on a only in the two level-k blocks of c. Setting a to zero elsewhere gives |D_k(c)| <= 6 C' ||a||^2_{l^4(blocks of c)}. *Analyticity.* B_i and D_i are analytic in a, as compositions of analytic maps with uniform bounds on an l^4 ball, and also for complex a. So Cauchy gives ||dD_k(a)||_{l^4 -> l^2} <= C(L) ||a||_{l^4}, uniformly in k.

**Lemma 4.5d (gauge with the critical bound) [PROVED in `library/lattice_sobolev_box_gauge.md`].** On a box of side N, every link field has a gauge a' with ||a'||_{l^4} <= C_2 ||da||_{l^2} and ||a'||_{l^2} <= C_2 N ||da||_{l^2}, C_2 independent of N, and the same on a finite union of boxes with box overlaps. Only reflection and Fourier on a torus are used, so a re-entrant corner of the union does no harm. *Regions: no fattening.* A region is a union of level-k cells, with the crossing links between face-adjacent cells of the region. Two cells that are only diagonal neighbours share no site and no link, so there is no pinch on the lattice. Within radius R_t there are finitely many patterns of cells. A pattern need not be simply connected, and V can have large holonomy around a hole, so no small gauge need exist on it. **So patches are unwrapped:** let the patch at x be a finite simply connected piece of the universal cover of the local pattern, containing the intrinsic ball of radius R_t around x. V lifts to it, and has a small gauge there, since every loop bounds a surface of bounded area. There are finitely many unwrapped patches, up to symmetry, for a given R_t. An earlier version fattened Lambda and closed it under a filling rule. That is not needed, and it had an unproved volume bound, which would have been fatal for Theorem 4.2. *What the library has to supply on an unwrapped patch:* the gauge of Lemma 4.5d, built up by adding cells one at a time so that each new cell meets the previous union in a connected union of its facets. **I have not checked that such an order exists for every pattern:** obligation. If it fails for a pattern, the constant is still finite at each n, but uniformity in n would need another argument (a Lipschitz extension on that pattern).

**Lemma 4.5e (lift) [DERIVED].** Let Omega be an unwrapped patch, and v level-k data on its bonds. There is a fine field with Q_str^{(k)} a = v and ||da||_2^2 <= C_up ||v||_2^2, with C_up absolute and independent of n and of the pattern. For a bond c, let b_c be a smooth bump on the mu-links of the central part of its tube, with Q_str b_c(c) = 1, |b_c| <= C n^{-1}, |grad b_c| <= C n^{-2}, supported in the blocks of c, so ||d b_c||_2^2 <= C. Transversally, bumps of different tubes do not overlap, and along mu, Q_str b_c(c') for the neighbouring bonds c' is small if the bump is near the crossing. So the level-k matrix Q_str b is diagonally dominant, and it is invertible with a local inverse, on any pattern. Take a = sum_c ((Q_str b)^{-1} v)(c) b_c. Conversely ||Q_2^{(k)} f||_2 <= ||f||_2 by Lemma 7.1, where Q_2^{(k)} is the direct average on plaquettes. On the whole torus the minimal lift obeys the sharper Lemma 10.1, in terms of ||d_k v||.

**Theorem G' (patch) [DERIVED, line by line given the gauge on unwrapped patches].** Let Omega be an unwrapped patch of radius R. There are rho_*, C depending on L, R, and not on k, such that for level-k data |v| < rho_* in the level-k slice S_k of Omega, the constrained stationary problem for the Wilson action on Omega_n with constraint M^k(exp(ia)) = exp(iv) modulo gauge has a unique small solution, analytic in v, and F_{k,Omega}(exp(iv)) := A(exp(ia(v))) is analytic on that polydisc, with

    F_{k,Omega}(exp(iv)) = (1/2) q_{n,Omega}(v) + sum_{m >= 3} T_m(v, ..., v),     |T_m(v, ..., v)| <= C^m |v|^m,

where q_{n,Omega} is the abelian form on Omega, with ||d_k v||^2 on plaquettes of Omega <= q_{n,Omega}(v) <= C_up ||v||^2.

*Proof.* Hilbert space: h := {da} on Omega_n with the l^2 norm. For f in h let a(f) be the linear gauge of Lemma 4.5d, so ||a(f)||_{l^4} <= C_2 ||f||_2. *Energy.* (exp(ia))_p = exp(i F_p(a)) with F_p(a) = (da)_p + N_p(a), |N_p(a)| <= C (sum_{b in p} |a_b|)^2, so ||N(a)||_2 <= C ||a||^2_{l^4}, and A_p = (1/2) |F_p|^2 + O(|F_p|^4), with sum_p |F_p|^4 <= C ||a||^4_{l^4}. So E(f) = (1/2) ||f||^2 + EE(f), with EE analytic on a ball of h and |EE(f)| <= C_1 ||f||_2^3. *Constraint.* Theta(B) := the small gauge transform of a level-k field into S_k, analytic with Theta(B) = Pi_k B + O(|B|^2), where Pi_k is the linear projection on S_k along gradients; this is a finite-dimensional inverse function statement, at fixed R. Then G(f) := Theta(B_k(a(f))) = QQ f + NN(f), with QQ f := Pi_k Q_str^k a(f), which depends on f only since gradients are killed, ||QQ|| <= C(R) by Lemma 7.1, and QQ has a right inverse bounded by Lemma 4.5e. By Lemma 4.5c, ||NN(f)||_2 <= C(L, R) ||f||_2^2. *Stationarity.* At v = 0 the linearisation of (f, mu) -> (f + dEE(f) - (QQ + dNN(f))^* mu, G(f)) is [[1, -QQ^*], [QQ, 0]], whose inverse is bounded by C(C_up), with no Poincare inequality needed, since on h the energy is exactly the identity form. The quantitative inverse function theorem in Hilbert space, with second derivatives bounded by C(L, R) through Cauchy, gives the solution and its analyticity. The second-order term is (1/2) <v, (QQ QQ^*)^{-1} v> = (1/2) q_{n,Omega}(v). Every constant is uniform in n because C_2, the bound ||QQ||, the right inverse, and Lemma 4.5c all are.  []

*Identification with the tropical F_{k,Omega}.* By induction on k. For real regular V, every W-regular slice at level k - 1 lies in the polydisc in a patch gauge, once eps_0 is small against rho_*. On it F_{k-1,Omega} is strictly convex, by (i) below. So the slice minimum is the unique stationary point. The image at level k - 1 of the solution of Theorem G' is such a stationary point, and it is regular at all intermediate levels, since sup |B_i| <= 2 A forces level-i curvature at most 8 A. So the one-shot value equals the tropical value. **No lattice Uhlenbeck gauge is needed:** that was what stopped the energy-only class in the earlier 7.5. Uniqueness among all fields in a slice comes level by level from convexity, and the fixed point only has to exist.

*Consequences.* (i) *Hessian.* In a patch gauge, Hess F_{k,Omega}(V) = q_{n,Omega} + O(C(L, R) |v|), uniformly in k. With Lemma 7.1 and the Poincare bound of 4.6 on the one-step kernel, this is coercive on the slice for eps_0 small against C(L, R)^{-1} L^{-2}. So (COER) is immediate. (ii) *N_k.* The density is (exact second order) + O(C(L, R) (local |F|)^3), in a frame at the site. Lower bound: ||phi^{(k)}||_2 <= ||f||_2 (1 + C(L, R) sup_p E(hull p)^{1/2}) by Lemma 7.1 and Lemma 4.5c, so F_{k,Omega} >= c_A E_k, with c_A -> 1/2 as eps_0 -> 0. (iii) *Lift.* V^*(W) is the same solution at level k + 1 read at level k. Its level-k curvature is bounded by Lemma 4.5h below in general, and by the linear bound C_s L^{-2} sup |F'| of Text 9.4 in the interior of Om, up to corrections C(L, R) eps_0^2, which are negligible by the choice of eps_0.

**Lemma 4.5f (local Poincare gauge for zero coarse data) [DERIVED, abelian].** Let e be a fine link field on Omega_n with Q_str^{(k)} e = 0 on all bonds of Omega_k. There is a global gauge e' = e + d lambda with Q_str^{(k)} e' = 0 and ||e'||_{l^2(x)} <= C_LP n ||de||_{l^2(N(x))} for every cell x, N(x) its neighbours, with C_LP depending on the finite list of patterns of radius 3 only, not on n.

*Proof.* On each patch N_x (unwrapped, a finite list) write e = e_x + d lambda_x with ||e_x||_2 <= C_2 n ||de||_{N_x}, by Lemma 4.5d, and normalise lambda_x to have block average 0 on the centre block of N_x. Since Q_str(d lambda) is the coarse gradient of the block averages (from Q_root(d Lambda) = Lambda(y') - Lambda(y), and the star term), and |Q_str e_x(c)| <= n^{-1} ||e_x||_2 by the l^2 bound of 4.5a, the block averages of lambda_x are at most C ||de||_{N_x} on N_x. For neighbours x, z, with O a block in the overlap, d(lambda_x - lambda_z) = e_z - e_x. So by Poincare on O, ||lambda_x - lambda_z - c_xz||_{l^2(O)} <= C n^2 ||de||_N, with c_xz the difference of block averages, |c_xz| <= C ||de||_N. Hence ||lambda_x - lambda_z||_{l^2(O)} <= C n^2 ||de||_N. **The constants are controlled by the constraint:** this is why no Cech obstruction appears, while for non-zero coarse curvature it would. Let h_x be a partition of unity at scale n, and lambda := - sum_x h_x lambda_x. On a cell z, e + d lambda = sum_x h_x e_x - sum_x (lambda_x - lambda_z) d h_x, using sum_x d h_x = 0, so its l^2(z) norm is at most C n ||de||_{N(z)}. Finally, its Q_str is the coarse gradient of the block averages of lambda, at most C ||de||_N. Remove it: let tau := sum_y lambdabar(y) psi_y + sum_y r(y) chi_y, with psi_y a partition of unity at scale n, chi_y a bump inside block y of average one, and r(y) chosen to make the block average of tau exactly lambdabar(y). r(y) = sum_{y'} (lambdabar(y) - lambdabar(y')) avg_{B(y)} psi_{y'} involves differences only, so ||d tau||_{l^2(x)} <= C n ||de||_N. With e' := e + d(lambda - tau) we get Q_str e' = 0 and the bound.  []

**Lemma 4.5g (exponential locality of the minimal lift) [DERIVED, abelian].** Let f^* = da^* be the minimal fine curvature on Omega_n for level-k data whose curvature vanishes outside a set S. Then for delta <= delta_0(C_LP), with rho the level-k distance from S,

    ||exp(delta rho) f^*||^2_{l^2(far from S)} <= C ||f^*||^2_{l^2(near S)},

with C, delta_0 independent of n and of the pattern of Omega. Likewise the multiplier obeys |mu(c)| <= C ||f^*||_{N(c)}.

*Proof.* Away from S the data are flat, so subtract a flat lift, which has zero energy, and get e with de = f^* and Q_str e = 0 there. Take e' from Lemma 4.5f. Let phi be Lipschitz at scale n, with slope delta / n relative to phi, equal to zero near S. Let l be a bounded local right inverse of Q_str, ||d l(c)||_2 <= C |c|. Test the Euler-Lagrange equation <f^*, d e''> = <mu, Q_str e''> with e'' := phi^2 e' - l([Q_str, phi^2] e'), for which Q_str e'' = 0:

    ||phi f^*||^2 = - <f^*, d(phi^2) ^ e'> + <f^*, d l([Q_str, phi^2] e')>.

The first term is at most C delta sum_x ||phi f^*||_x n^{-1} ||phi e'||_{l^2(x)} <= C delta C_LP ||phi f^*||^2, up to a bounded weight ratio over N(x) and up to the bounded region where phi is cut off. |[Q_str, phi^2] e'(c)| <= C delta phi^2(c) n^{-1} ||e'||_{N(c)} by 4.5a, which is at most C delta C_LP phi^2 ||f^*||_N, so the second term has the same bound. Absorb for delta small. For mu, test with l(delta_c).  []

So locality comes from a gauge-invariant energy estimate, and it survives re-entrant corners. At the trivial background and on the whole torus it agrees with the analytic symbol of 9.4.

**Lemma 4.5h (Morrey decay at depth) [DERIVED, abelian, absolute constants; uses a reverse-Holder lemma not yet in the library].** With f^* as above on an unwrapped patch, E(x; rho) the fine energy in the ball of radius rho in level-k units, for 1 / n <= rho <= 1 and data of size at most eps,

    E(x; rho) <= C rho^{2 sigma} ( E(x; 1) + eps^2 ),      sigma > 0 depending on the patterns only.

*Proof.* Caccioppoli: test the Euler-Lagrange equation with chi^2 a_loc, where a_loc is a potential of f^* on B_{2 rho}. The source <mu, Q chi^2 a_loc> is at most |mu| n^{-3} (rho n)^2 ||a_loc||_{l^2(B_{2 rho})}. So E(rho) <= C (rho n)^{-2} ||a_loc||^2_{l^2(B_{2 rho})} + C eps^2 rho^6. Sobolev for the potential: on a box, a' = K * f on the reflected torus, with |K(w)| <= C (1 + |w|)^{-3}, the gradient of the lattice Green's function. So by the Hardy-Littlewood-Sobolev inequality, ||a'||_{l^2} <= C ||f||_{l^{4/3}}. With E as an average, this is a reverse Holder inequality between l^2 and l^{4/3}, on all balls of the patch, at all scales above the lattice spacing. **Gehring's lemma then gives f^* in l^{2 + eta} with eta > 0 and uniform constants,** and Holder gives the decay with 2 sigma = 4 eta / (2 + eta). A hole-filling proof, which is shorter, would need H^1 of the local annulus to vanish, and that fails at a corner where the local pattern has a loop.  []

Obligation: a lattice version of Gehring's lemma and the lattice HLS bound, with credit, in the library.

By Lemma 7.1 at level k within a level-(k+1) block, |f_p(V^*)|^2 <= E(hull p), and rho = 1 / L. So **|f_p(V^*)| <= C L^{-sigma} sup |F'|** everywhere on Om, corners included. Regularity of V^* needs only this, and so does the excess of 4.4, which compares with c_F of order (log L)^{-2}.

**Proposition 4.5i (from patches to Om: one-shot locally, level by level globally) [DERIVED at the level of each step].** *Why not one global fine-lattice problem:* the covariant fine-lattice saddle on all of Om in a uniformly local critical norm has no global small gauge, transition functions of order one, and block averages of adjoint-valued gauge functions that are not covariant. I do not need it, as follows.

Let f_{k,x}(V) be the fine energy in cell x of the tropical minimiser. So f_{k+1,x'}(W) = sum_{x in B(x')} f_{k,x}(V^*(W)), which is exact, and sum_x f_{k,x} = F_{k,Om}. Let f^Omega_{k,x} be the same for a patch Omega containing B_r(x) n Om, and delta_k(r) the sup over the complex class of |f_{k,x} - f^Omega_{k,x}|. Claim: for r >= 1,

    delta_k(r) <= C_1 eps_0^2 exp(-c r),      C_1 a polynomial in L, c absolute, uniformly in k and in Om.                     (4.4)

*Step k -> k + 1.* Assume (4.4) at level k. Take a patch radius R_t = C log L at level k. Theorem G' gives the Taylor bounds of f^Omega_{k,x} on a polydisc much larger than the class, and (4.4) with Cauchy adds at most C_1 exp(-c R_t) / c_2^2 to second derivatives on the class, which is small against L^{-2} for C large. So H := Hess F_{k,Om}(V) is, in a frame at each site, exp-local with moments bounded by linear constants, and

    H = ||D_V .||^2 + Delta_q^V + O(C(L, R_t) eps_0),

where Delta_q := q_n - ||d_k .||^2 >= 0 by Lemma 7.1 is the abelian difference, covariantised along short paths. Its symbol is O(P^4), so double commutators with a cutoff h give (grad h)^2 times a second-order form, not times ||B||^2. So an IMS localisation at an absolute radius, with positivity in a patch gauge, gives Delta_q^V >= -small (||D_V B||^2 + tau ||D_V^* B||^2). ||D_V .||^2 itself is nearest-neighbour and needs no patch. On ker Q^V, ||grad_V B||^2 <= ||D_V B||^2 + ||D_V^* B||^2 + C eps_0 ||B||^2 (Weitzenbock), and within a tube of side L, with L^2 eps_0 << 1, Ad is close to 1, so the scalar Poincare inequality gives ||B||^2 <= C L^2 ||grad_V B||^2. **So the level-k saddle S_k is a bounded operator on l^2 of level-k links, invertible with norm polynomial in L, and its kernel decays at rate c / L by the conjugation of 7.3.** Near the free boundary of Om, a union of level-(k+1) cells, the constant in Poincare is C L^2 with C from the finite list of coarse patterns, by scale invariance. Newton for V^*(W), from local solutions glued at level k in patch gauges, converges for eps_0 small, also for complex W, and V^* stays inside the class because the class contracts under the lift (Lemma 4.5h).

Then compare with the patch problem at level k + 1 and radius r, whose level-k form is a patch of radius r L. f_{k+1,x'} - f^{Omega'}_{k+1,x'} = sum_{x in B(x')} ( [f_{k,x} - f^Omega_{k,x}](V^*_glob) + [f^Omega_{k,x}(V^*_glob) - f^Omega_{k,x}(V^*_patch)] ). The first brackets sum to at most L^4 delta_k(r L). The second are at most L^4 sup |grad f| sup |V^*_glob - V^*_patch|, where V^*_glob - V^*_patch solves S_k with a source of size C eps_0 at the boundary of Omega, plus a smaller one from delta_k, so is at most poly(L) eps_0 exp(-c r). Thus

    delta_{k+1}(r) <= L^4 C_1 eps_0^2 exp(-c r L) + poly(L) eps_0^2 exp(-c r),

and for L^4 exp(-c (L - 1)) <= 1/2 this is at most C_1 eps_0^2 exp(-c r) with C_1 := 2 poly(L). **The recursion cannot compound, because the error from level k is exponentially smaller at the same physical distance.** The base case is delta_0 = 0: the Wilson density is strictly local. []

So one-shot is used only to get a priori bounds on small patches, where a small gauge exists and the critical norm works. Level-by-level is used only to pass to Om, where only the ratio L occurs and operators are bounded. **C_1 is polynomial in L with absolute constants** because the large constants C(L, R_t) of Theorem G' only ever appear multiplied by eps_0, so R_t = C log L is consistent. Lambda is not fattened, so C_M = C M^4 is polylogarithmic in L, and the margin L^2 >= 8 C_OS O (1 + C_M) of Theorem 4.2 holds. All local estimates are in the frames of unwrapped patches, and distances are intrinsic to Om.

*Hostile pass on this section.* (a) I looked for compounding in Lemma 4.5c: the recursion uses the same Y at each level, an l^2 contraction 1/L that is exact, and an l^4 bound of norm exactly one, so there is none. (b) Lemma 4.5b is soft, so C_Y(L) could be huge. That is harmless only because eps_0 comes after L. If a consumer needed an L-free nonlinear constant this route would not supply it. I checked the consumers: (FLOW) does not (Proposition 8.4). The contraction of polymers uses the class radius alpha / eps_0, not rho_* (4.6). (c) In Theorem G' the patch energy must be small, R^4 eps^2 << A_0(L)^2, in the patch gauge. So eps_0 is exceedingly small against 1/L. No lower bound on eps_0 is used anywhere: Theorems 4.2, 4.3 and 5.5 hold for smaller eps_0, as long as gamma comes last. (d) The cell-by-cell order on unwrapped patches is unchecked; see 4.5d. (e) Holonomy around a hole is large in general. Unwrapping handles it, since the density at x only sees an intrinsic neighbourhood, up to (4.4). The comparison (4.4) is between the global solution, lifted to the cover, and the patch solution, in the cover. (f) In 4.5i, I attacked the possibility that a patch radius large against L is forced, which would make C_M about L^4 and kill the margin of Theorem 4.2. A naive IMS with ||B||^2 commutators does force it, since the gap is L^{-2}. It is avoided because ||D_V .||^2 needs no patch and the difference Delta_q is fourth order. If Delta_q had a second-order part, this would fail, and Lemma 10.1's numerics R -> 1 as P -> 0 is what rules that out. Lemmas 4.5f and 4.5g remain in use for the L-free bound sup |Pi| <= C sup |F'| in the excess; region dependence in Lemma 4.4b also follows from (4.4). (g) I wrote this without reading the files `library/critical-class-and-excess.md`, `library/block-poincare-energy-package.md`, `library/convex-laplace-tree-decay.md`, which appeared in the shared directory and which I did not author; their names suggest they may overlap with this section. They may come from the sibling attempt, so I am leaving them unread as the charter requires. **The lead should compare them with this section.**

**4.6 The exterior polymer bound (EI) [DERIVED given Theorem G' and the covariance decay of 7.3].** Fix W regular, possibly complex in the class, and V^* = V^*(W).

*Coordinates.* On the slice, fix the gauge by the Feynman term of (CUT) item 1, and solve the constraint by Z + HH(Z), with Z in ker Q, HH of second order and local at block scale, and a Jacobian that is a product over coarse bonds of local analytic functions. This is the structure of CMP 109 (2.9)-(2.13) as transcribed (LANE-READ), with a Feynman term for his exponential gauge. Then C := (Pi H_L Pi)^{-1} on that subspace is coercive by Text 7, with kernel decaying at rate c / L in level-k units by 7.3, with a polynomial prefactor C(L). White noise: Z = g Pi R_D xi, as in (CUT) below, with xi a product measure. (A first version used maximal tree gauge here: see (CUT), item 1, for why that fails.)

*Expansion.* Psi(xi) := g^{-2} R(g ZZ xi) + P(g ZZ xi) + log JJ, where ZZ := Cc C^{1/2} (plus HH), R is the remainder of F_k beyond second order, and P the variation of EE_k. By Theorem G' and Cauchy at V^*, the Taylor coefficients of R of order m >= 3 at V^* have kernels at most C^m exp(-delta_0 tree(b_1, ..., b_m)), and the same for P with m >= 1, with a factor C_E. Inserting Z,

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
1. *Strict finite range by a polynomial square root.* **Conditioning matters here.** In maximal tree gauge the form has spectrum in [c L^{-4}, C], because a smooth mode of Landau amplitude 1 has tree-gauge amplitude L. A Chebyshev polynomial then needs degree about L^2 for a fixed error, so range L^2, which does not fit a level-(k+1) cube of side M L when L >> M. Landau gauge in each block is better but still not right: any gauge that is discontinuous across block faces makes the crossing links larger by a factor L, and the edge of the spectrum is then L^{-3}. So on the small-field part, let X := ker Q_str (covariant at V^*), and Pi the orthogonal projector on X. Q Q^* has symbol at least 1/3, so Pi is a polynomial of bounded degree in Q Q^* up to a small error, with range one coarse cell. The gauge group preserving X is G_0, the level-k gauge functions with zero block average, since Q_str(d lambda) is the coarse gradient of the block averages. Average over the G_0 orbit with weight exp(-tau ||D^* B||^2 / g^2) (the Gaussian form of Faddeev-Popov), whose normalisation is a determinant on zero-block-average scalars, with spectrum in [c L^{-2}, C] by Poincare on a block, so local by the same argument as here, and its logarithm goes into Psi. Put H_tilde := Pi H Pi + tau Pi D D^* Pi + (1 - Pi). At the trivial background, for B in X, <B, H_tilde B> >= ||d_k B||^2 + tau ||d_k^* B||^2 >= min(1, tau) ||grad B||^2, by Lemma 7.1 and the Fourier identity on the torus. Each component B_mu has zero tube-weighted average on every bond, so ||B||^2 <= C L^2 ||grad B||^2, by the scalar Poincare inequality on a tube, crossing links included. **So the spectrum of H_tilde on X is in [c L^{-2}, C], with c, C absolute**, and corrections at V^* are of order C(L, R) eps_0, negligible. Let R_D be the Chebyshev polynomial of degree D approximating H_tilde^{-1/2}, with error at most exp(-c' D / L). Then the covariance on the slice is C = Pi R_D(H_tilde)^2 Pi + C_rem, with C_rem >= 0 after a small adjustment, ||C_rem|| <= exp(-c' D / L), and kernel decaying at the rate of 7.3. So B = g Pi R_D(H_tilde) xi + g C_rem^{1/2} xi', with xi on all links, a product measure, and xi' independent. Truncating the tails of H at range M_1 costs another term of the same kind, and it needs exp(-delta_0 M_1) << L^{-2}, that is, M_1 >= C log L. **So for fixed xi', the first term is a strictly local linear function of the product variable xi.** With D M_1 = M L, the error is exp(-c' M / M_1), small for M large against M_1. So M >= C log L (3.1). [Chebyshev bound standard; range bookkeeping a sketch. This is close to a finite-range decomposition, used here only to get strict locality.] Tree gauge remains the coordinate for frozen rough cubes, where no Gaussian is used.
2. *For fixed xi', the expansion needs no analyticity in xi.* Expand the product of local factors: (e^{Psi_X} 1_{box} - 1). Disjoint polymers are independent for the product measure, so the integrated weights form a hard-core gas with activities z(Y; xi'). Steps 3 to 5 of the cluster library proof use only a bound on |z(Y)|.
3. *Bound on z(Y), cubes of three kinds.* Small: all |xi| <= p in the cube. There |B| <= C(L) g p << eps_1, the indicator is 1, and each factor is at most H_0. Mid: some |xi| > p in the cube, and the box still holds: use the Gaussian integral with exp(theta ||xi||^2), where theta <= C c_1 from g^{-2} |R(g Z)| <= C_3 eps_1 ||Z||^2 <= C eps_1 L^2 ||xi||^2, with eps_1 L^2 = eps_0 / 4. So such a cube costs at most (M L)^4 exp(-p^2 / 3). Large: rough, or outside the box: next item.
4. *Large cubes and the conditional mean.* For a set S of large cubes, freeze V on S. The exterior Gaussian then has a conditional mean of size at most C(L) eps_1 exp(-c dist(., S) / L). At distance r_1 := (L / c) log(C(L) eps_1 / (g p)), it is below g p, the small-field scale, and beyond that the expansion of 2 and 3 runs with the mean as a harmless spectator. On the collar within r_1 there is no expansion: bound the integrand by superadditivity (Text 4.3), which decouples S from the exterior, and use the exterior Gaussian. So a polymer with holes S carries a collar of (r_1 / (M L))^4 cubes per large cube, polylog in 1/g, with no small factor per collar cube; that entropy and the factor exp(kappa |collar|) are paid by the cost c / g^2 of S, for g <= gamma. **This is the margin device, and it is why the frozen hole needs no analyticity near it.** In the collar the mean is at most eps_1, so the quadratic form is changed by a relative C(L, R) eps_1 L^2, tiny by the choice of eps_0; the Gaussian stays normalisable there, with a bounded factor per variable, which is the entropy just counted. *Polymers next to Lambda.* The same device takes care of I(k)(b) near Lambda: a polymer within r_2(g) := C log(1 / g) of Lambda(V) is not kept in EE, but moved into G_k with its bound C_E per cell, paid by the cost. So the contraction of 4.6 is only ever applied at distance r_2 from Lambda, where the lift obeys the interior bound of 9.4 up to exp(-delta_0 r_2) = g^C. Near corners no gain is needed, and the concern that a polymer next to a corner has only the Morrey gain is removed. (The classical term F_{k,Om} cannot be moved in this way, and it stays exact up to the boundary; that is why Theorem G' has to hold near corners.) G_k regenerates at each step by Theorem 4.3, with a fresh bound, so this does not compound.
5. *Decay in S.* C_S on the exterior is local by `library/path_expansion_locality.md`, so polymers with several holes have Mobius decay in the distances.
6. *Spectator xi'.* After 2 to 5, the result z(Y; xi') depends on xi' through B' := g C_rem^{1/2} xi'. Since the main part has a Gaussian density with covariance g^2 Pi R_D^2 Pi on the variables of Y, shifting the contour shows that z is analytic in B' in the strip |Im B'| <= c g, **with Re B' unrestricted**, and bounded there by C sup |z|: the hard cuts stay on the real contour, and the density picks up a factor exp(|Im B'|^2 / (2 g^2 lambda)). The kernel of C_rem^{1/2} decays at the rate of 7.3, so the sensitivity to xi'_c, at distance d in cubes, gives by Cauchy in the imaginary direction a factor at most p exp(-c M d) sup |z|, for a Mobius difference in s where xi'_c(s) = s xi'_c. So a second expansion in xi' converges, its polymers are extended by a range (1 / (c M)) log p, polylog in log 1/g, and their activity is bounded by the sup of the local activity. **My first version asked for (amplitude of B') times p small, which fails as g -> 0 at fixed range. Only the imaginary direction matters.**
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

**6.1 Induction with a local source: one step [DERIVED term by term; each term is at the level of the corresponding small-field estimate].** Let the bare coupling be beta - w(p), with w complex, |w| <= rho, Lipschitz at the physical scale a_*, constant Lam. All levels k <= K have a_k <= a_K, a fixed fraction of a_*, so Lam a_k <= 1 and is summable in k. Density recursion: f_{0,p} = s_p, f_{k+1,x'}(W) := sum_{x in B(x')} f_{k,x}(V^*(W)), with V^* the source-free lift, so sum_x f_{k,x} = F_k, and these densities are bounded by Theorem G'.

Hypothesis I^w(k), on Om = Om(V):

    log r_k^w(V) = -g_k^{-2} F_{k,Om}(V) + sum_x w_k(x) f_{k,x}(V) + EE_k^w(V) + log G_k^w(V).

Set V = exp(iB) V^*(W). Then, term by term:

1. *B = 0.* -g_k^{-2} F_{k+1}(W) + sum_{x'} w_k(x') f_{k+1,x'}(W) + sum_{x'} sum_{x in B(x')} (w_k(x) - w_k(x')) f_{k,x}(V^*). The last sum is a polymer of size C Lam a_{k+1} per coarse cell times the local action: an irrelevant term with gain a_{k+1}, summable in k.
2. *First order in B.* -g_k^{-2} dF_k . Z vanishes on the slice. And sum_x w_k(x) df_{k,x} . Z: for constant w it is w dF_k . Z, which also vanishes. So only (w_k(x) - wbar) df_{k,x} . Z survives, of size Lam a_k (local |F|) |Z|, with Z of order g p: **a source does not move the background**, up to terms that are small here.
3. *Second order in B.* -(1/2)(g_k^{-2} - wbar) <Z, H Z> + (gradient term). Writing it as a Gaussian at w = 0 plus a perturbation of size rho g^2 p^2 per polymer, H_0 in (EI) gains a term C rho g^2 p^2, which is small.
4. *One-loop with source.* For constant w the Gaussian with stiffness b = g^{-2} - w has determinant b^{-dim/2} (det H_L)^{-1/2}. **So the W-dependence of the one-loop term is the same as at w = 0, for constant w.** In perturbation: the term of order g^2 w is (1/2) g^2 w Tr[C(W) H_L(W)], and Tr[C H_L] = dim, independent of W. This settles a point I had left open: there is no term of order g^2 w in the marginal part. The W-independent part, n log(1 - w g_k^2) per variable, is the term of E at this level. For Lipschitz w the remainder has a gain Lam a_k.
5. *Higher orders.* H^# of 4.6, as a function of b. Analytic in b on a disc of radius 1 / (2 g^2) around g^{-2}, since g enters only through b^{-1/2}. By Cauchy, d/dw of a quantity of size S is at most C g^2 S. The marginal part of H^# has size at most C(L, M) g p^3, by size alone (Proposition 11.1), so its derivative in w is at most C g^3 p^3. Parity would improve this to g^4, and it is not needed.
6. *Flow.* Extract the marginal part of e_{k+1} by 11.1, polymer by polymer, at each x'. Then b_{k+1}(x') = b_k(x') - beta_{k+1}(b_k(x')) + (gradient, gain a_k), with beta_{k+1}(b) = b_* log L + (d_k - d_{k+1}) + rho_k(b), b_* the coefficient of 8.2, where the first two terms do not depend on b, by item 4. So |w_{k+1}(x) - w_k(x)| <= C g_k^3 p^c |w_k(x)| + C Lam a_k. By (T4), sum_k g_k^3 p(g_k)^c is finite and small with gamma, so **|w_k| <= 2 rho for all k, uniformly in K**, for gamma small and a_K small. Lipschitz constant: the same recursion.
7. *Large field.* Stiffness Re b_k >= (1 - 2 rho gamma^2) / g_k^2, and (4.1) is about real V. So Theorem 4.3 holds with the factor 7/4 replaced by (7/4)(1 - 2 rho gamma^2), still above 3/2. (The first version wrote 1 / (2 g^2) here, which would have used up the whole margin; the stiffness is much better than that.)

*Complex w and phases.* The modulus must never be taken through more than one level: |rho^w(1)| is smaller than rho^{Re w}(1) by a factor exp(c a^{-4} (Im w)^2 g^4), so a modulus bound at the bare level would lose an amount of order a^{-4}. In the step k -> k+1 the modulus is taken only over level-k variables of frozen cubes, and comparing Haar with the Gaussian at complex b_k costs |1 - w g_k^2|^{-n/2} per cube, which is 1 + O(g^2). Finer levels in that cube are already integrated, analytically in w, inside r_k^w. So there is **no loss of order a^{-4}**: this is the phase cancellation the gate asks about, and it follows from the level-by-level structure.

**6.2 The counterterm.** E(w) := log rho_K^w(1) - log rho_K^0(1), the source-dependent constrained partition function with the coarse field trivial, which is the named subtraction of (1.2). It is a convergent sum over levels of polymers at W = 1, so it is analytic and non-zero on the polydisc. Averaging over the lattice symmetries of Tor, E_sym(w) := avg_g E(w o g).

**6.3 CT1-CT4 from I^w(K) [DERIVED given I^w(k)].**
- *CT1.* <exp(w . s)>_Tor = exp(E(w)) [int r_K^w dW] / [int r_K^0 dW]. |int r_K^w dW| <= sup |r_K^w| <= exp(C |T_K|), from I^w(K). And int r_K^0 dW >= exp(-C |T_K|), from the ball |log W| <= g_K. So |<exp(w . s)>| <= exp(Re E(w) + c), with c = 2 C |T_K| depending on a_K, which is fixed, for **all** w in the class and not only the pattern. Since the left side does not change under g, CT1 holds for E_sym, by the geometric mean.
- *CT2.* E_sym(w o g) = E_sym(w) by construction, and E(conj w) = conj E(w), since rho^w is real for real w and analytic.
- *CT3.* By Mobius in the support of w, which is a scalar source with natural base point 0, E(w) = sum_k sum_X e_k(X; w|_X), with e_k(X; 0) = 0, |e_k(X; w)| <= C rho g_k^2 exp(-kappa |X|_k). (Check against the gate's reading: the leading term is n w_k g_k^2 per level-k variable, the quadratic part n w^2 g_k^4 / 2 is the contact term, dominated by level 0 at order a^{-4}, and the gradient part is of order Lam^2 a_k^2 g^4 per cell, which gives a^{-2}, as upper-chain Remark 3.3 expects. All three are local at each level, so they are additive on separated supports.) In E(sum w_i) - sum E(w_i) only polymers meeting two supports survive. Such a polymer has at least eta / a_k cells, so its level contributes at most C rho g_k^2 (v / a_k^4) exp(-kappa' eta / a_k). The sum over k converges with no dependence on a. So tau(v, eta) <= C rho v eta^{-4}. The bound e_k uses I^w(k)(b) at W = 1, where the white-noise expansion is the only input.
- *CT4.* On a torus of side L_T = 2^m P, Z = rho_K(1) int r_K dW. log rho_K(1) is a sum over levels of vacuum polymers at W = 1 that are the same functions on both tori, except those wrapping around Tor, at most C exp(-kappa P / a_k) per cell at level k, all of order one in the last levels. So log rho_K^{(L_T)}(1) = (L_T / P)^4 log rho_K^{(P)}(1) + O((L_T / a_*)^4). Also int r_K^{(L_T)} dW >= exp(-C (L_T / a_K)^4) and int r_K^{(P)} dW <= exp(C (P / a_K)^4). Together these give CT4, with c_F = C (a_* / a_K)^4. **Here the normalisation factors g_k^{n} are extensive at each level, and the last integral is at the fixed coupling g_K. So no log log(1/a) from the zero modes of Tor arises:** the torus at scale a_K has a bounded number of cells and a fixed coupling, so its zero-mode factor is a bounded constant. This answers the worry in gate item D2, whose mode count is at the bare coupling on a lattice of T cells. I have not compared the two counts line by line.

**6.4 Requirements on the consumer.** (a) My blocking factor L is odd and large, so the lattice is a = L^{-K} a_K, not dyadic. Tor has an even number T_K of last cells, so planes at multiples of P/2 are lattice planes. Lemma 7.2 of the upper chain needs even side and doubling at larger tori, not dyadic a. Its subsequence in a must be along L-adic values. **Request to the lead.** (b) CT1 is delivered for all w in the class, so the conjugate pattern is not needed on my side. (c) The step of the bare coupling between K and K + 1 is b log L + d_K - d_{K+1} + O(gamma-small), known only within 4 C_0(L). So if a consumer needs rho to cover half a trajectory step (gate item D4), rho must be chosen as a function of L, which is allowed: rho comes before gamma in 3.1. The step is not the 0.13 of a dyadic trajectory. (d) g_K = gamma / sqrt 2 exactly, by (T5), but g_0(K) need not be monotone in K unless C_0(L) is small against b log L. If the chain needs a monotone trajectory, then L must be taken large against C_0 by another route, or a subsequence of K used. **Request to the lead:** say whether monotonicity in K is used.

**6.5 Hostile pass on Section 6.** (a) The whole section is conditional on I^w(k), whose small-field part is sketched. (b) In CT3, e_k(X; w) needs Mobius in w-support to converge. That is the same analytic trick as Step 5 of the library proof, in a variable s_c multiplying w on cube c, and holds if I^w(k)(b) is analytic in w on a polydisc larger than the class, with bound at most C rho g_k^2 per cube. Not checked at the walk level. (c) Item 5 of 6.1 needs only the size of the marginal part of H^#, C(L, M) g p^3, and the summability of g^3 p^c. The earlier appeal to parity is withdrawn. (d) E must absorb the quadratic contact term, of order a^{-4}, and it does: it is in the Mobius sum at level 0, where it has range a. (e) In CT1 the constant c depends on (a_* / a_K)^4 and on gamma, through g_K, and these are fixed. So c is large but cutoff-free.

### 7. Fluctuation form: a route without random walks [labels on each step]

**Target (COER).** At a regular non-abelian background, with frozen boundary, the fluctuation form on ker Q is bounded below, and its inverse has exponentially decaying kernel, uniformly in k and the volume. Every Gaussian in (SF3), the uniqueness in (SF1), the Z-core cost and the normalisations consume it. My only source is CMP 99:389, unread; Dimock's analogues are abelian, and they use random walks with local gauge patches. The route below uses neither.

**7.1 Lower bound, abelian.** Let q_k(B) = min{ ||dA||^2 on the fine lattice : Q_k A = B }.

*Lemma 7.1.* q_k(B) >= ||d_k B||^2_{l^2(T_k)}, for every k. [DERIVED.] The curvature map is the n-fold direct average, n = L^k, by the composition rule: base-point offset and path offset written in base L biject the nested sums with the direct ones (RENEW section 2, rechecked). Its row sum is n^2 and its column sum is n^{-2}, so Cauchy-Schwarz gives the bound with constant exactly 1. Nothing compounds, since this is one-shot.

*Lemma 7.2 (block Poincare).* If QB = 0 on the bonds of a block pair, then sum_b |B_b|^2 <= C_P(L) ( sum_p |d_k B_p|^2 + sum_{x} |g(x)|^2 ), summed over the hull, where g(x) is the axial average of B from the block centre to x. [DERIVED.] An interior link equals g(x + e) - g(x) up to plaquette sums over a bounded surface. Two crossing links of the same face differ by interior links and a strip of plaquettes. The average over the face is fixed by QB = 0, in terms of interior links and h(y) = avg_x g(x). All constants depend on L only, and the statement lives on a finite graph at level k.

*Theorem 7.3 (abelian COER).* With Balaban's gauge term ||G B||^2 = sum |g|^2, the form q_k + G^* G is at least 1 / C_P(L) on ker Q, for all k, and so the fluctuation covariance is bounded by C_P(L) at each level-k link. [DERIVED from 7.1, 7.2.] Mixed bonds, with one block frozen, impose nothing on interior links by Lemma 1.1, so the same proof runs on exterior blocks; frozen variables have zero variation. **The whole lower bound is finite-graph plus one Cauchy-Schwarz.**

*Star removal.* Q_root(d Lambda) = Lambda(y') - Lambda(y), so q_k(B) = min over coarse gauge of the same problem with Q_str, in which there is no star through y. Hence q_k(B) depends on B only through d_k B: q_k(B) = min{ ||F||^2 : F closed, A_k F = d_k B }. [DERIVED.]

*Saddle stability.* In units of the block, Q_str has diagonal QQ^* weight int tri^2 = 2/3 and overlap int tri(x) tri(x+1) = 1/6 with each of two neighbours along the bond, and none across directions or transversely. So its symbol is 2/3 + (1/3) cos theta >= 1/3. [DERIVED, explicit.]

**7.2 Non-abelian form [DERIVED from Theorem G'].** In a patch gauge Hess F_{k,Omega}(V) = q_{n,Omega} + O(C(L, R) |v|), uniformly in k. So at a regular background the form is coercive on the slice as soon as eps_0 is small against C(L, R)^{-1} L^{-2}: the lower bound is linear (Lemma 7.1 and the Poincare bound of (CUT) item 1), and the correction is nonlinear. In particular the Nielsen-Olesen negative mode does not appear in the fiber at this curvature. The first version of this section needed an all-level sup norm on U, which is what (REG) was for. It is gone.

**7.3 Decay of the level-k covariance [DERIVED at trivial background; perturbation by the choice of eps_0].** On the level-k lattice, take H := Hess F_{k,Om}(V^*), with the gauge term of (CUT) item 1 and the projector Pi on ker Q^{V^*}. At the trivial background and away from holes, H has exponentially local kernel at the absolute rate delta_0 ((4.4) at level k, or the analytic symbol of 9.4 at the trivial background), and the form on ker Q has spectrum in [c L^{-2}, C], with c, C absolute. Conjugating by exp(phi), scalar, |grad phi| <= delta / L: the form changes by at most C (delta / L) ||grad B|| ||B|| + C (delta / L)^2 ||B||^2, and ||B|| <= C L ||grad B|| on ker Q, so the relative change is at most C delta. Pi is local at scale L, so its commutator is also C delta. Hence

    |C_k(b, b')| <= C(L) exp( - c d(b, b') / L ),    c absolute,

uniformly in k. A scalar weight commutes with Ad, so the non-abelian case has no gauge patches, and the corrections are of order C(L, R) eps_0, small against c L^{-2} by the choice of eps_0. **The rate c / L with c absolute is linear data, and that is what makes kappa = c M in (EI) free of L.**

**7.4 What failed in this section, and why.**
- *Energy-only regular class.* The first version of this section set this aside, because it seemed to need a lattice Uhlenbeck gauge. **It is what Theorem G' now does, without that gauge:** the fixed point is perturbative, the regular class is still defined by curvature, and uniqueness comes level by level from convexity. The one idea I had missed is that l^4 is exactly critical for Q_str with norm one, so the sup norm on the fine lattice was never needed.
- *Translation-invariant Laurent route.* It gives decay in the abelian case, but it does not extend to a non-trivial background or to a region with boundary. Replaced by 4.5g and 7.3.
- *Step-wise (REG):* shape factors compound as (C_s / L^2)^k. Replaced by the critical norm, in which a shape factor does not enter.
- *(COER) as the hardest inequality.* I named it hardest early on. The lower bound is short, so it was not.
- *Sign of beta by per-level analysis.* The paramagnetic second-order term has a sign at every level, because ker Q_{m-1} is inside ker Q_m and Tr(X V Y V) >= 0 for X, Y >= 0. [Derived.] The diamagnetic and constraint terms do not. So a sign per level did not come out, and it is not needed: (8.2) and Proposition 8.4.

**7.5 Hostile pass on Section 7.** (a) Lemma 7.1 is for the linearised map only. Its use at non-trivial U now goes through the analytic bound of Theorem G', with a correction proportional to |v|. (b) The gauge term of (CUT) item 1 is a device for the Gaussian; the integrand is gauge invariant and the normalisation of the device is a determinant on zero-block-average scalars. It goes into the polymers with the rest, and I have not computed it beyond its locality. (c) (5.5) is on real fields, and it says nothing on the complex class. Complex bounds come from analyticity of the exterior only. (d) None of the numerics tested the final map at threshold eps_0.

### 8. FLOW by telescoping: the sign without per-level evaluation

Credit: the background-field structure of the coupling recursion is Balaban's CMP 109 (1.3), (1.4), (0.20) as transcribed in NOTES section 9 (LANE-READ). The diamagnetic and paramagnetic split at constant field is Nielsen and Hughes. The telescoping below is derived here.

**8.1 Exact one-loop identity [DERIVED].** Let F_j be the classical functional, F_{j+1}(W) = min over Fib(W) of F_j(V), the tropical recursion (exact, with F_0 = A). Let V^* be the minimiser and H_L = Hess F_j(V^*) - mu . Hess M the Hessian of the Lagrangian, with mu the multiplier. By Legendre duality, Hess F_{j+1}(W) = (Q^U H_L^{-1} (Q^U)^*)^{-1}. By the Fourier representation of the delta function,

    int dB delta(Q^U B) exp(-(1/2) <B, H_L B>) = (2 pi)^{(N - d)/2} (det H_L)^{-1/2} (det Q^U H_L^{-1} (Q^U)^*)^{-1/2} = (2 pi)^{(N-d)/2} (det H_L)^{-1/2} (det Hess F_{j+1}(W))^{1/2}.

No separate Jacobian appears: the weights of Q^U are inside Hess F_{j+1}. On covariantly constant backgrounds mu vanishes with D^* F, so H_L = Hess F_j. Gauge directions go through the exact factorisation of the orbit integral: [dB_j / G_j] = [dW / G_{j+1}] [fiber / G_{j,0}]. Define L_j(V) as the one-loop gauge-invariant integral of Hess F_j. Then

    log Z^{(j)}(U) = L_j(V) - L_{j+1}(W),                                                                                   (8.1)

so the one-step fluctuation determinant is a **difference of two copies of one functional at adjacent levels**. The sum over levels telescopes. This replaces the direct sign analysis of 7.4: the variation of the constraint is inside Hess F_{j+1}.

**8.2 The coefficient b [DERIVED, continuum, formal in the usual heat-kernel sense; the value agrees with the known one-loop coefficient].** Take SU(2), background F_12 = B_ad on the charged components, i.e. link U = exp(i theta sigma_3) with B_ad = 2 curl theta, so that the action density of A = sum_p (1 - (1/2) tr U_p) is B_ad^2 / 8. A complex scalar of charge 1 has K(t) = (16 pi^2 t^2)^{-1} (B t / sinh B t). In Feynman gauge the charged vector has spin shifts +2B, -2B and two zero shifts, and the charged ghost enters twice with the opposite sign. So with mass mu,

    X = int (dt / t) e^{-mu^2 t} K(t) [ 2 + e^{2 B t} + e^{-2 B t} - 2 ] = int (dt / t) e^{-mu^2 t} K(t) 2 cosh(2 B t),

and the B^2 term is (B^2 / 16 pi^2)(4 - 1/3) int dt / t e^{-mu^2 t}, which is (11/3)(B^2 / 8 pi^2) log(1 / (mu a)). In terms of A this is

    X = b log(1 / (mu a)) * A,    b = 11 / (3 pi^2) = 0.3715...,

the 4 being paramagnetic and the -1/3 diamagnetic. Check: in this normalisation 1/g_B^2 runs at the rate 4 N b_0 = 11 N^2 / (12 pi^2) at N = 2, as recorded in the program's Proposition LF-count.

**8.3 From (8.1) to the flow [DERIVED given the marginal coefficients below].** Let Phi_F(V) := -(1/2) log det H_F(V) + log det Gh(V) on the lattice of the level in question, with a Feynman term: H_F(V) = Hess F(V) + D_V D_V^*, Gh(V) = D_V^* D_V. Each Phi is massless and has no polymer form of its own: only differences do. Insert the Wilson form A^{(j)} on the same lattice:

    log Z^{(j)}(V^*(W)) = [Phi_{F_j} - Phi_A]^{(j)}(V^*(W)) - [Phi_{F_{j+1}} - Phi_A]^{(j+1)}(W) + WW_L(W) + X_mu(W),
    WW_L(W) := Phi_A^{(j)}(V^*(W)) - Phi_A^{(j+1)}(W).

Let d_j be the coefficient of A in [Phi_{F_j} - Phi_A]^{(j)} on slowly varying fields, that is, d_j = c_j - c_W in the notation of the earlier version; d_0 = 0 since F_0 = A. On slowly varying W, A(V^*(W)) = A(W) up to irrelevant terms, by exactness of (R4) on constant curvature. WW_L has coefficient b log L (8.7). X_mu is the term linear in the multiplier in (8.1). It has the form <mu, Y(W)>, with Y a covariant local link-valued function, and the only covariant vector of dimension at most 3 is D_nu F_{nu mu}. Both factors have dimension 3, so X_mu has dimension 6 and no marginal part: on the scaled field of Lemma 8.5 it is O(xi^2) in total. So, with g_{j+1}^{-2} = g_j^{-2} - beta_{j+1},

    beta_{j+1} = b log L + d_j - d_{j+1} + rho_j,                                                                          (8.2)

with rho_j the marginal part of the higher-order polymers, and of the recycled gas. By size alone, |rho_j| <= C_2(L, M) g_j p(g_j)^3, Proposition 11.1 applied to (EI). **I do not use any parity improvement to g^2.**

**Proposition 8.4 (what the induction consumes from the flow) [DERIVED, line by line].** Let (8.2) hold for j <= k, with |d_j| <= C_0 and |rho_j| <= C_2 g_j p(g_j)^3, **where C_0, C_2 may depend on L**, and g_j <= gamma, with gamma small against C_0, C_2, L. Put u_j := g_j^{-2}, w_j := u_j - d_j. Then:
- (T1) w_{j+1} = w_j - b log L - rho_j, and b log L + rho_j lies in [(b/2) log L, (3b/2) log L]. So **w_j is strictly decreasing, for any L > 1**, while u_j itself need not be monotone.
- (T2) |u_{j+1} - u_j| <= 2 b log L + 2 C_0, so u_{j+1} <= (7/4) u_j for gamma small. This is all Theorem 4.3 uses: it has a factor 2 in hand.
- (T3) For i <= j: u_i >= u_j + (j - i)(b/2) log L - 2 C_0 >= gamma^{-2} / 2 + (j - i)(b/2) log L.
- (T4) sum_{i <= j} g_i^3 p(g_i)^c and sum_{i <= j} exp(-p(g_i)^2 / 2) are finite, uniformly in j, and tend to zero with gamma. These are the summability that 6.1 item 6 and the mid-field shift of 9.6 ask for. [From (T3): the first sum is at most C gamma p(gamma)^c / (b log L). The second converges since 2 p_0 > 1.]
- (T5) (Trajectory.) For every K there is g_0 with g_K = gamma / sqrt 2 exactly and g_j <= gamma for all j <= K, and then 1 / g_0^2 = 2 / gamma^2 + K b log L + (d_0 - d_K) + sum_j rho_j.

*Proof of (T5).* g_K is continuous in g_0 on the set where g_j <= gamma for j < K, because each beta is a continuous function of the earlier couplings. For g_0 small, u_K is large. Lower u_0 until some u_j = gamma^{-2}, j <= K. By (T1), u_K <= u_j + 2 C_0 <= gamma^{-2} + 2 C_0 < 2 gamma^{-2} at that point. The intermediate value theorem gives u_K = 2 gamma^{-2} with all u_j >= gamma^{-2} on the way.  []

**So the demand that C_0 be free of L, which I named the hardest inequality in the last round, was not a real requirement.** It came from asking beta_{j+1} > 0 at each step. That is not consumed: gamma comes after L, so a bounded local reversal of the flow costs a relative change gamma^2 C_0 in the coupling. What is needed is that c_j stays bounded in j at fixed L, and that the coefficient of log T is exactly b at each level. Also L need not be large for (FLOW): L large is for the margins in 3.1. (T5) replaces a monotone trajectory; a ~ L^{-K} remains a function of K, and g_0(K) is what the interface receives.

**Lemma 8.5 (derivative count without Ward identities) [DERIVED given Theorem G' and Steps 1 to 5 of Proposition 11.1].** Let D := F_j - A^{(j)}. Its Taylor kernels at the trivial background have symbols, analytic in a strip, with

    |D^(2)(p)| <= C |p|^4,   |D^(3)(p, q)| <= C (|p| + |q|)^3,   |D^(4)(p, q, r)| <= C (|p| + |q| + |r|)^2,

with C depending on the constants of Theorem G', and so possibly on L, but not on j.

*Proof.* D is a sum of gauge-invariant densities with exponentially decaying sensitivity (Theorem G', 4.5g), with no F^2 term, since the second-order form is ||d_j B||^2 (1 + O(P^2)) by Lemma 10.1 and the expansion G_mu(P)^{-1} = P^2 (1 + O(P^2)). Take a fixed trigonometric polynomial f and V_xi := exp(i xi f(xi .)). Compute D(V_xi) in two ways. (1) By Steps 1 to 5 of Proposition 11.1 applied to the densities, which only needs smoothness of the explicit field with alpha = 1: per site D(V_xi) is at most C xi^5, so in total, over xi^{-4} sites, D(V_xi) = O(xi). (2) By Taylor in f and Euler-Maclaurin in the kernels, D(V_xi) = sum_{m, r} xi^{m + r - 4} P_{m,r}(f), with P_{m,r}(f) the local polynomial of degree m in f with r derivatives, whose coefficient is the degree-r Taylor coefficient at the origin of the symbol of D^(m). Comparing powers of xi for all f, and using homogeneity in f, gives P_{m,r} = 0 for m + r <= 4. By polarisation the Taylor coefficients of D^(m) of degree r vanish for m + r <= 4. The hypercubic inversion removes odd m + r. That leaves exactly the stated orders.  []

The same argument gives H_{t,1}, H_{t,2} of the expected orders. **This replaces the Ward hierarchy, and the claim in the earlier 8.4a that gauge invariance ties the low vertices to the F^2 term is now a proof.**

**Proposition 8.6 (|d_j| <= C_0(L), uniformly in j) [DERIVED given Lemma 8.5; power count written out, not all terms line by line].** In Feynman gauge the ghost is the same for F_j and for A^{(j)}, so it cancels in the difference. Put H_t(V) = H_A(V) + t delta(V), delta = Hess D. With a background of amplitude e and momentum q, expand delta = delta_0 + delta_1 + delta_2 + ..., H_t = H_0 + t delta_0 + H_{t,1} + H_{t,2} + ..., G_t := (H_0 + t delta_0)^{-1}. Since delta_0 >= 0 by Lemma 7.1, ||G_t(p)|| <= 1 / phat^2 for all t, **with a linear constant equal to 1**. Then

    second order in e of Phi_{F_j} - Phi_A = int_0^1 dt ( -(1/2) Tr[G_t delta_2] + (1/2) Tr[G_t H_{t,1} G_t delta_1] + (1/2) Tr[G_t H_{t,2} G_t delta_0] - (1/2) Tr[G_t H_{t,1} G_t H_{t,1} G_t delta_0] ).

Lemma 8.5 gives delta_0 ~ p^4, delta_1 ~ e (|p| + |q|)^3, delta_2 ~ e^2 (|p| + |q|)^2, H_{t,1} ~ e (|p| + |q|), H_{t,2} ~ e^2. By gauge invariance of the difference, Pi_{mu nu}(q) vanishes at q = 0 and is transverse; the only transverse tensor of order q^2 allowed by the hypercubic group is q^2 delta_{mu nu} - q_mu q_nu; call its coefficient d_j. For |p| >= 2 |q|, Taylor in q: the q^2 coefficient of each term is at most C e^2 / phat^2, and int d^4 p / phat^2 converges at small p; at large p all is bounded. The Taylor remainder is C q^4 / p^4 in the integrand, so it contributes O(q^4 log(1 / |q|)). For |p| <= 2 |q| each term is at most C e^2 q^4 / (p^2 (p + q)^2) or C e^2 q^2 / p^2 or C e^2 q^2 / (p + q)^2, or C e^2, and each integrates to O(e^2 q^4). So Pi_diff(q) = d_j (q^2 delta - q q) + O(q^4 log (1 / |q|)), with |d_j| <= C_0, where C_0 is the constant of Lemma 8.5 times a number depending on d. Uniform in j, because Theorem G' is. No infrared logarithm appears in the difference, so **the coefficient of log T is the same for every j**, and it is the Wilson value.

**8.7 The Wilson term [DERIVED at the level of the usual lattice one-loop computation].** For a smooth field AA on a torus of side T, Phi_A at lattice spacing a equals (b log(T / a) + c_W) A[AA] + Univ[AA] + o(1) as a -> 0, with Univ a functional of the continuum field on the torus: the second-order kernel is (q^2 delta - q q) Pi_1(q a), and x d Pi_1 / dx at small x = q a is an integral dominated at momenta of order q, where the lattice symbols equal the continuum ones up to O(q^2 a^2). So it has the continuum value of 8.2. Since WW_L compares spacing a with spacing L a on the same field, up to irrelevant terms, its coefficient is exactly b log L, with c_W and Univ cancelling, and it is the same for every j. I have not written out Pi_1 on the lattice. This statement is the classical comparison of a lattice one-loop integral with its continuum limit, and it is exact only in the limit; the error is irrelevant in the sense of 11.1. c_W itself is never needed.

**8.8 Hostile pass on Section 8.** (a) (8.1) is exact on covariantly constant backgrounds; on general slowly varying backgrounds the difference is X_mu, of dimension 6, by the argument in 8.3. That argument classifies Y by covariance and dimension. The classification is one line, and Y has an analytic local expansion by Theorem G' and 4.5g. Accepted. (b) A torus has only quantised constant curvature. Since beta is now extracted polymer by polymer (11.1) from one-step densities on a slowly varying field, no constant curvature background is needed, and (8.1) enters only through the identity of densities. (c) The neutral sector and zero modes appear in Phi at both levels; they are the same functions of the coarse field at leading order, and they differ by irrelevant terms because the difference of densities is local. Not checked at second order through the nested means, except through Lemma 8.5, which does cover nested means, as it is a statement about F_j itself. (d) In (T5) continuity of beta in the earlier couplings needs the hard cuts of (CUT) to depend continuously on g. They do, after integration. (e) (T1) needs C_2 g p^3 small against b log L, which is why gamma comes after L. If L were close to 1, that would break, but L is large anyway. (f) A real weakness: c_j is only known to be bounded, not computed, so the actual step of beta is known only within 4 C_0(L). The interface must not be told a numeric trajectory step; see 6.4. (g) Proposition 8.6 depends on Theorem G' at the trivial background only, on the whole torus, where shapes do not enter. So the list-of-shapes obligation does not touch (FLOW).

### 9. Linear lift bounds and the gauge notes

An earlier version of this section bounded the vertices of F_j with constants free of L, off the star, in the l^4 norm, with a loss L^{1/2} through the star on rough inputs. **No consumer needs L-free nonlinear constants any more** (Proposition 8.4, Text 4.5), so that bookkeeping is gone; the part that is still consumed is the following.

**9.4 Lift bounds, free of L [DERIVED given Lemma 10.1; linear].** The lift for a level-j link depends only on n = L^j, in the linear theory. Since Q_str has weights n^{-3} on a tube, the constrained equation is Delta a = Q_str^* mu, with mu on the level-j lattice. On the torus 1 / G_mu(P) is analytic in a strip, so |mu(c)| <= C exp(-delta d(c, c_0)) for a unit source at c_0, with C and delta depending on d only. Then, with the lattice Green's function bound |grad G(x)| <= C |x|^{-3},

    |grad a(x)| <= C int_{|y| <~ n} |x - y|^{-3} n^{-3} |mu| <= C n^{-2} exp(-delta d),    |a(x)| <= C n^{-1} exp(-delta d),

and level-i curvature obeys |F^{(i)}| <= C (n_i / n)^2 by the row sum. The source Q_str^* mu is bounded, since only in-plane derivatives of the tube weight enter, so grad G * source is an order-one smoothing, with no logarithm at the block faces. So in the interior of Om, the level-k curvature of V^*(W) is at most C_s L^{-2} sup |F'|, with Holder modulus (|x - x'| / L)^a, up to corrections C(L, R) eps_0^2, negligible by the choice of eps_0. Near corners of Lambda only the Morrey bound of 4.5h holds.

**9.6 Gauge notes and the cut.**
- *Maximal tree gauge [DERIVED].* In each L-block, based at the block centre: for a gauge-invariant integrand, setting tree links to 1 has trivial Jacobian on Haar measure, at every field, rough or not, so there is no Gribov problem. It serves for frozen rough cubes. On the small-field slice it is badly conditioned, by a factor L^2, and (CUT) item 1 is used there.
- *Two-tier fluctuation cut [DERIVED as a scheme].* Theorem 27 of Dimock I (ultralocal cluster expansion, which I read) needs H_0 small, which fails on the whole range |B| < eps_1, where the cubic term reaches eps_1^3 / g^2. So use the white-noise cut |W| <= p(g), p(g) = (log 1/g)^{p_0}, for the expansion, as Dimock does. A mid-field cell, with p(g) < |W| and |B| < eps_1, is an island with activity at most exp(-p^2 / 2) and no compact-integral loss, since the Gaussian is normalised. It is always recyclable next to a regular field. Beyond eps_1 is type Z. The marginal shift from mid-field cells is at most sum_k exp(-p(g_k)^2 / 2), which converges by (T4), and it is far below g^4.

### 10. Upper bound on the lift form

**Lemma 10.1 (two-sided bound on the perfect form, abelian, every n) [DERIVED].** ||d_j B||^2 <= q_n(B) <= (pi^2 / 4)^6 ||d_j B||^2, about 226 ||d_j B||^2.

*Proof.* Lower bound: Lemma 7.1. Upper bound: in Feynman form on the coarse level, Q_str is diagonal in direction, so the coarse covariance is diagonal, G_mu(P) = n^{-2} sum_m prod_i D_n(p_i)^2 D_n(p_mu)^2 / phat(p_m)^2, and Landau differs from Feynman on the coarse level only by a coarse gradient. So q_n(B) <= B_perp^* G^{-1} B_perp, with B_perp the part of B orthogonal to chat. Keep only the alias m = 0: |n p_i / 2| <= pi / 2 gives D_n(p_i)^2 >= (2 / pi)^2, since sin x / (n sin(x / n)) >= sin x / x >= 2 / pi there, and phat^2 <= p^2 = P^2 / n^2. So G_mu(P) >= (4 / pi^2)^5 / P^2. And ||d_j B||^2 = |chat|^2 |B_perp|^2, with |chat|^2 >= (4 / pi^2) P^2.  []

*Numerics, under the lock, script* `checks/hard-core--independent_lift_form.py`*, criteria stated first:* PASS-LOWER, with min R = 1 up to rounding at n = 1, 3, 9, infinity. PASS-UPPER, with max R = 6.45, 11.03, 12.2 at n = 3, 9, infinity, attained at P = (pi, pi, pi, pi); cutoffs 8 and 12 agree within 0.04 percent and grid against random within 2.5 percent. R -> 1 as P -> 0, as (R4) requires. These are float searches, and they only serve as a check of the lemma, whose constant 226 is crude against 12.2. The lemma holds with no dependence on L.

**10.2** Sup bounds on the fine lattice at depth are not an obligation in the level-only scheme, and near corners of Lambda they are false (4.5).

### 11. Irrelevance by Fock-Schwinger gauge, polymer by polymer (a route without the Ward hierarchy)

Target: (0.28)-(0.29) of CMP 109 for this scheme, which is the content of (SF4), together with the closure of the polymer bound. CMP 109 Sections 4 and 5 (LANE-READ) reach it by a fifth-order expansion in local coordinates and Ward identities relating orders. The route below does not use them: each polymer is gauge invariant separately, so it can be evaluated in a gauge centred on itself.

**Proposition 11.1 (irrelevance) [DERIVED given curvature at most eps on all levels of U and Holder control of F; both are one-step inputs, from 9.4].** Let E(X; .) be functions on level-j fields on X such that: each is invariant under gauge transformations on X; each extends analytically to sup_b |log V(b)| < alpha_1; |E(X; .)| <= E_0 exp(-kappa d_j(X)) there; E(X; 1) = 0; and the family is covariant under level-j translations and the hypercubic group. Let V_j = M^j(U) with U at level k, xi = L^{j-k}, and level-j curvature phi <= xi^2 eps on the hull. Then there is a number beta(E), the second moment of the family, with

    sum_X E(X; V_j) = beta(E) A(U) + sum_X V(X),     |V(X)| <= C xi^{4 + alpha} exp(-kappa' d_j(X)),   any alpha < 1,

where C depends on E_0, kappa, alpha_1, and eps and not on k or j.

*Proof.*
1. *Large X.* Let D = diam X. If C D phi >= alpha_1, then d_j(X) >= c alpha_1 / (M xi^2 eps), and exp(-kappa d_j(X)) is smaller than any power of xi.
2. *Gauge.* Otherwise, transform by axial transport from a site of X. A link b is then the holonomy of a loop around a surface of area at most C D, so |v_b| := |log V'(b)| <= C D phi, and v is in the disc of analyticity.
3. *Taylor at the identity.* The constant term vanishes. The linear term is <c, v> with c invariant under constant colour rotation, because constant gauge transformations act on X; the adjoint has no invariant vector, so c = 0. The remainder after second order is at most E_0 exp(-kappa d) (C D phi / alpha_1)^3, of order xi^6 exp(-kappa' d).
4. *Second order.* v_b = sum over the surface of parallel-transported F_p. Replacing transports by 1 costs a relative C D phi. Replacing F_p by its value F_0 at the base site costs a relative Holder modulus (D xi)^alpha. So the quadratic term is c^X(F_0, F_0) + O(xi^{4 + alpha} exp(-kappa' d)), with c^X(F_0, F_0) := Pi^X(a[F_0], a[F_0]), a[F_0] the axial potential of a constant field.
5. *Symmetry.* Sum over X with given base site. By translation covariance the form is independent of the site. Colour invariance makes it delta_{ab} on colour. A reflection of one axis flips F_{mu nu} when mu or nu is that axis, which kills F_12 F_34 and F_12 F_13. Permutations equate the rest. So it equals beta' sum_{mu < nu} |F_{mu nu}|^2, the only invariant, at the base site. **No rotation invariance and no second marginal coupling are involved.**
6. *Identification.* By the row sum and Holder, F_j(x) = n_j^2 F(x) (1 + O(xi^alpha)), so sum over level-j sites of |F_j|^2 equals sum over fine plaquettes of |F|^2 up to the same factor, which is 2 A(U) (1 + O(eps^2 eta^4)). Localise A(U) to level-j cells.  []

Steps 1 to 5 are complete at this level. Step 6 and the Holder modulus are one-step inputs in the level-only scheme, with xi = 1/L, from 9.4 in the interior of Om. Polymers near corners of Lambda are not in EE at all: (CUT) item 4. So the gain is alpha < 1 and not Balaban's, and the expansion needs third order only. **I have not read his proof, and I do not know why he goes to fifth order; the likely reason is the regularity class he works in. Do not read this as an improvement on him until the Holder input is proved.**

**11.4 Hostile pass.** (a) Step 2 uses only sup curvature on the hull of X. For rough backgrounds it fails, but polymers are only evaluated on M^j(U) with U regular. (b) Step 3's linear term and Step 2 need each function to be gauge invariant. Resetting links to 1 outside a set would break this. **Resolved:** localise only in the white noise, not in V. Reset xi to 0 outside a set: 0 is invariant under the Ad rotation that accompanies a gauge transformation of the background. So the polymers e(Y; V) are indexed by xi-supports Y, are jointly invariant, and have V as a spectator with exponentially decaying sensitivity. 11.1 applies with radial gauge from Y: amplitude grows polynomially with distance, against the exponential decay of sensitivity. This is why I(k)(b) is stated with sensitivity and not with strict support. [Derived at this level.] (c) Step 5 requires covariance of the family under the full hypercubic group, which D3 has only as a mixture. It holds for the sum. (d) In 11.2 the size of P assumes a level-k variation is smooth at level j: this holds for lifts by 9.4, including for B rough at level k, since lifts are smooth below the level-k scale.
