# Repo search

The lead's `prior/repo-search-2026-11-08.md` covers older hard-route and soft-route interfaces. It identifies no prior check of row 970. Its closest transfer hit is `S/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`: a positive one-step plaquette correlation, not a tilted-covariance or log-Sobolev bound. I opened that hit on fetched PR #10114 (`f76f6c649cff7dffbab664d8976e680e8f287fe9`), including its model scope. I also checked the digest's `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145` on fetched main (`8b11ae2bb95e641494fe75ed83d108ee712fa3a9`): it bounds a noncompact determinant-weighted Maxwell covariance on a Dirichlet quotient, a different measure. Neither supplies or duplicates this check. The target-specific prior note is absent. The pinned registry has no `direction2`, `TILT-COV`, `LOC-COV` or `LSI-traj` entry. This checks row 970; it starts no proof lane on those open inputs.

Source: `9bc86cdc21800d2615df32eb930d23d8ff700262`. Checker: OpenAI Codex, configured session; row 972. Research text, not an audit; no status is granted. The author under check is Claude Fable 5.2, row 970. No numerical run will discharge a statement.

## Scope and recovery

The requested checks are complete, in section 8.4 order below; CLASS and GUIDE follow. Only this report is changed. Source proofs, FINISH, registries and status files are unchanged. No numerical simulation or arithmetic guard was run.

The outline and CA-I were fetched once at `31a47c543775` into the new directory `/tmp/sa-gap-direction2-check-astra.VAMByc/`. Anything taken from them is credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Their index describes source status; it does not certify a proof.

## 1. SUB and the row-950 observable

**Lemma SUB (row 970, 3.4): HOLDS**, for nonzero z. At b = 0, the joint law is the product of pi_(phi/s) and pi_(phi/s'). With phi = s' beta u, its second factor is pi_(beta u). Independence gives

    Var(<z,q~>) = s^(-2) Var_(pi_(phi/s))(<z,x>)
                 + s'^(-2) Var_(pi_(beta u))(<z,w>).

The action is linear, so the orbit tangent at phi is s' beta times that at u. Drop the first nonnegative variance. This proves the stated inequality without any slab approximation.

**Observable identification: HOLDS AFTER CORRECTION** to the law and to the SC-hor constant. Row 950 (`gap-sc-max.md:44–118,138–178`) distinguishes its temporal-gauge law pi~_u from its gauge-averaged law pi_u. Row 970's pi_(beta u) equals the former. For a pure imaginary quaternion xi_l, right multiplication by u_l preserves the real inner product, hence

    <xi_l u_l,w_l> = <xi_l,Im(w_l u_l^*)>.

Thus its electric statistic is exactly linear in w. For u_xy and one unit colour e, put

    xi_x(v) = (-1)^(v_x+v_y) e / sqrt(2 L^3),
    xi_y(v) = -xi_x(v),   xi_z(v) = 0,   z_l = xi_l u_l.

Then |z| = 1. Its lattice divergence vanishes: the x difference is 2 xi_x and the y difference is -2 xi_x. At this central slice that proves horizontality. Global colour invariance gives zero mean and equal variances in the three colours. The statistic equals O^e/sqrt(2 L^3), so its variance equals the reported one-colour second moment under the exact symmetric law.

Two qualifications matter to consumers:

- Row 950's actual runs have six free time slices and a half-weight far end. They sample a finite-slab approximation, not pi_(beta u) exactly. The half-space identification is a limit as slab depth tends to infinity. No depth-uniform or depth-convergence estimate accompanies these numbers.
- Row 950 defines SC-hor by Hess_M F <= C_h, whereas SUB bounds the ambient covariance. Its exact Hessian identity gives the sufficient constant C_h = beta^2 s'^2 kbar_(s,0) + beta, not C_h = s'^2 kbar_(s,0). The latter is the covariance constant only.

The row-950 original code and raw logs are named under `/tmp/gap-sc-950/`, outside this task's allowed scratch folders and absent from `library/guide/lane950/`. They are not inspected here. The observable and stated model above are checked from the note; row 970's available implementation is checked below. Finite side lengths do not establish an unbounded-volume counterexample. SUB transfers a genuine variance lower bound, not that inference from a finite table.

## 2. FH and QUOT

**FH(a)–(c): HOLDS.** Write f = log F. Equivariance of the gradient gives grad f(exp(tX)phi) = exp(tX)grad f(phi). Differentiating at zero gives Hf(phi) Xphi = X grad f(phi), including the sign in (b). If Xphi = 0 this gives X grad f = 0, hence (c). This is also a direct check of the source's differentiated orthogonality argument.

**FH(d): HOLDS** on its stated gradient vectors. Complete the orthonormal orbit vectors e_alpha to an orthonormal basis. Then

    |Hf|_HS^2 >= sum_alpha |Hf e_alpha|^2
              = 4 F^(-1) sum_alpha |X_alpha grad sqrt(F)|^2.

Changing a lift X_alpha by Y with Yphi = 0 changes nothing, because Y grad sqrt(F) = 0. A change of orthonormal orbit basis preserves the sum. The same reasoning defines Q_phi on every vector satisfying the stabiliser condition in QUOT. It need not define Q on an arbitrary horizontal vector without that condition.

**Theorem QUOT: HOLDS**, conditional on the named flow identity and Theorem BR. Gaussian convolution preserves gauge invariance. Therefore z = grad sqrt(F_t) is horizontal and fixed by the infinitesimal stabiliser. Keeping FH(d) in the flow identity gives

    (L_t - partial_t)|grad sqrt(F_t)|^2
       >= -2 Cov_(J_(b_t,phi))(z,z) + Q_phi(z)
       >= -2 kbar_(s,t) |z|^2.

After integrating against nu_t, I'(t) <= 2 kbar_(s,t) I(t). Integration and Ent(F) = 2 integral I(t) dt give exactly POL-BR's constant. This checks the use of FH, not the supply of a seed-sized kbar. The one-link check in 5.2 uses a *unit* radial z; for general radial z its Q is 3|z|^2/r^2.

**ROTOR model: HOLDS.** The partition function is sinh(h)/h. Twice differentiating its logarithm gives Var = R^2(1/h^2 - 1/sinh(h)^2). The two unit orbit vectors give Q = 2/rho^2. At D = 0 the only vector fixed by the full SO(3) stabiliser is zero. Thus the quotient test has no missing nonzero test there. This model does not identify the entire lattice quotient covariance. In particular, the plain colour mode of SUB at u_xy is not stabiliser-fixed and cannot by itself violate QUOT.

## 3. TIE

**TIE(a)–(c), including (b): HOLDS.** Gaussian convolution multiplies both cosh(a phi) and sinh(a phi) by exp(a^2 t/2). Their quotient is unchanged. Completing the square gives the printed equal mixture and its variance a^2 sech^2(a phi). The supremum is a^2. For that minimal constant the criterion returns (exp(2a^2 c)-1)/(2a^2), with its continuous value c at a = 0.

**TIE(d): HOLDS AFTER CORRECTION** of “every t” to “almost every t,” as in ABS-flow. At an isolated discontinuity an admissible piecewise continuous rate may be assigned any value without changing that hypothesis or its integral. The bound holds at every continuity point; it holds everywhere for a continuous representative.

Here is the hand check of the coefficient and the Chebyshev step. Take |eps| < 1 and F = 1 + eps G. Dividing ABS-flow by eps^2/4 and taking eps to zero gives

    2 E[a^2 sech^2(a phi) G'^2] <= 2 kap_t E[G'^2] + E[G''^2].

The common normalization of nu_t cancels. With u = a phi, its three terms are 2a^3 M_5, 2 kap_t a M_3 and 4a^3(M_3-M_5), for a > 0. Hence kap_t >= a^2(3 M_5/M_3 - 2). Let U,V be independent with density proportional to sech^3. Both f(u)=sech^2(u) and g(u)=exp(-u^2/(2A)) decrease with |u|, so

    Cov(f(U),g(U))
      = (1/2) E[(f(U)-f(V))(g(U)-g(V))] >= 0.

Integration of the derivative of tanh(u) sech^(n-2)(u) gives I_n = (n-2)I_(n-2)/(n-1). Substituting sinh(u) gives I_1 = pi. Thus I_5/I_3 = 3/4, M_5/M_3 >= 3/4, and kap_t >= a^2/4. The a = 0 case is trivial.

This is a necessary lower bound. It does **not** prove that kap_t = a^2/4 is admissible for all F. “Gains a factor 4” must mean *at most* that improvement in this bound. Sections 6.3–6.4 do not prove its transfer to a lattice neighbourhood: their cutoff and transverse terms remain open.

## 4. Identity MM

**Gradient formula: HOLDS. Identity MM: HOLDS AFTER CORRECTION** of its unspecified coupling. FLOW gives one-time marginals; those alone do not establish the asserted Markov chain. In particular, using the *same* Gaussian xi in the displayed formula at different t does not give that chain. The following coupling supplies the missing step.

Write Q = q~ and r = c-t. Under either prior J or J', take a Brownian motion B_r independent of (x,w), and set Y_r = rQ+B_r for 0 <= r <= c. Put phi_t = Y_(c-t). Then

    Y_r | Y_c=y, Q = (r/c)y + N(0, r(c-r)Id/c).

This conditional law does not depend on Q. Thus (x,w) -> phi_0 -> phi_t is Markov with the same forward kernel under both priors. Under J its reverse conditional kernel is

    P_(0,t)H(phi) = [g_t * (exp(-V_0)H)](phi) / exp(-V_t(phi)).

Bayes' formula therefore gives P_(0,t)(l'_0/l_0) = l'_t/l_t. Differentiating the Gaussian mixture gives grad log l'_t = E_[J'][Q|phi_t]-phi/(c-t); subtraction gives exactly the source's gradient formula. No change of the posterior's b_t is missing: under J the factor exp(-(c-t)|Q|^2/2) changes beta to t/(ss').

For completeness, a direct entropy calculation checks the coefficient without a numerical guard. Let p_r,p'_r be the densities of Y_r. Their scores are a_r-y/r and a'_r-y/r, with a_r=E[Q|Y_r] and a'_r=E'[Q|Y_r]. Each solves

    partial_r p_r = -(1/2) Delta p_r - div((y/r)p_r).

This follows by differentiating each Gaussian with mean rQ and variance r. Differentiate D(p'_r|p_r), integrate by parts, and cancel the common dilation term. The remaining term is

    dD/dr = (1/2) integral p'_r |grad log(p'_r/p_r)|^2
           = (1/2) E'|a'_r-a_r|^2.

Q is bounded at fixed s and box. If |Q| <= R, convexity of relative entropy and any coupling of the two priors give D(p'_r|p_r) <= (r/2) E|Q'-Q|^2 <= 2rR^2. Thus the lower endpoint is zero. Integrating r from 0 to c proves MM with its factor 1/2. Gaussian tails justify the integrations for r away from zero. Replacing J' by (1-eps)J'+eps J and passing to the limit handles a bounded density which can vanish; the score difference stays bounded by 2R.

MM is an identity for a bridge marginal. It supplies no entropy contraction rate and no estimate that atypical tilts carry little Fisher information. The latter is explicitly left unproved in 7.3.

## 5. TRAJ and the gauge-averaged HC kernel

**TRAJ: HOLDS AFTER CORRECTION** to an explicit kernel convention and endpoint limit. The required family of test functions is sufficient; no log-Sobolev inequality outside that family is used.

Let P_0 be the temporal-gauge Doob operator, p_0 its density relative to nu, and Pi the gauge average. Define

    P_bar = P_0 Pi = Pi P_0,
    p_bar(u,w) = integral_G p_0(u,g.w) dg.

Omega and nu are gauge invariant. Thus p_bar is a density, separately gauge invariant, and P_bar agrees with P_0 on invariant functions. Use h_u=p_bar(u,.) and f_(u,k)=P_bar^k h_u in TRAJ. The bridge in BR still uses the unaveraged joint law J; for invariant f, P_0 f=P_bar f, and its interpolation U is invariant. These two conventions are compatible.

The source of HC already defines p_s spectrally on gauge-invariant functions (`gap-direction-max.md:172–175,260–270`). With that convention p_1 is p_bar. Row 970's claim that p_1 is “invariant only under a joint transformation” concerns p_0 instead. Its proposed gauge average is the right clarification, not a reason to change the physical spectral trace.

**The kernel note and HOT bound: HOLDS AFTER CORRECTION** of that distinction. The estimate is fully checkable. Using row 970's action with its constant removed, both T_0 and its gauge average lie between exp(-6 beta |B|) and exp(6 beta |B|). Their common Perron vector is gauge invariant. With ||Omega||_2=1, its maximum/minimum ratio is at most exp(12 beta |B|), giving exp(-12 beta |B|) <= Omega <= exp(12 beta |B|). Also lambda_0 >= exp(-6 beta |B|). Therefore

    p_bar(u,w) <= exp(36 beta |B|).

Averaging cannot increase the sup bound. The Hilbert-Schmidt identity is

    integral nu(du) ||P_bar^m h_u||_2^2
      = Tr(P_bar^(2m+2)) = 1 + S(2m+2;B),

where S includes exactly the physical, non-vacuum eigenvalues. No unphysical eigenvalue is inserted.

For A_eps = integral_[eps,1/beta-eps] alpha_s ds, fix m and put p_k=1+exp(-A_eps(m-k)). BR's one-step proof for f_(u,k) uses only U_(u,k,s)^(q(s)/2), with p_k <= q(s) <= p_(k+1) <= 2. The derivative and Jensen endpoint steps at `gap-fc-max.md:147–178` apply unchanged. Iteration gives ||P_bar^m h_u||_2 <= ||h_u||_(p_0). The HOT estimate and the trace identity give

    X(2m+2;B) <= 72 beta |B| exp(-A_eps m).

Assume measurable nonnegative alpha_s with the stated finite truncated integrals, and let eps decrease to zero. The claimed bound follows whenever (1/2) integral alpha_s ds >= alpha. This supplies the endpoint step omitted in TRAJ's inspection proof. The m=0 case is the density/HOT bound alone.

The EC-traj corollary also survives, but BR's *duality proof* of BR-ent cannot simply be restricted: it sends p to infinity, outside TRAJ's test family. Instead let q decrease to 1 in TRAJ's LSI. For f=f_(u,k), the bridge entropy H(s)=Ent_(nu_s)(U_s) satisfies H'(s)=(1/2) integral |grad U_s|^2/U_s >= alpha_s H(s). Jensen at the ends gives Ent_nu(P_bar f) <= exp(-A) Ent_nu(f). MM computes the interior bridge entropies; recovering the endpoint slice entropies requires s to approach 0 or 1/beta. Here bounded continuous, strictly positive f makes that limit legitimate by dominated convergence of the conditional averages.

## 6. SLAB

**SLAB's covariance implication: HOLDS.** The argument requires all sufficiently long slabs with the same bound. It needs no quantitative gap uniform in B. A fixed finite box has a positive continuous transfer kernel on compact M. Its simple Perron eigenvalue strictly dominates the remaining spectrum. Spectral convergence in L^2, followed by the bounded map T:L^2 -> C(M), gives uniform convergence of lambda_0^(-n)T^n1 to <Omega,1>Omega. Normalizing gives Omega_n -> Omega uniformly. Positivity keeps the tilted normalizers nonzero. For every fixed b,phi,z, all moment integrands are bounded on M x M, so variances converge. Passing the common bound to each fixed triple proves the claimed supremum bound. No interchange of supremum and limit in the wrong direction is used.

**Slab-law description: HOLDS AFTER CORRECTION.** Omega need not be normalized as a probability density, and m_n should be normalized when called a law. For n>=1 the literal density exp(-V(x_0)/2)(T_0^n1)(x_0) integrates the path weight

    exp[ beta sum_(i=0)^(n-1) <x_i,x_(i+1)>
         - V(x_0) - sum_(i=1)^(n-1) V(x_i) - V(x_n)/2 ].

Thus m has **full** spatial plaquette weight at the retained boundary, with a half-weight far end in this approximation. The “half weight on the boundary” description in 1.3 belongs to Omega, before multiplication by exp(-V/2). This correction agrees with the two central full-weight slices in the GUIDE code. The scalar normalization cancels in J_(b,phi).

SLAB does not validate a single slab depth. Its fixed-box Perron convergence is a qualitative spectral separation, not the requested quantitative physical mass gap. Consequently “no gap” in its heading must mean no assumed uniform or seed-sized gap.

## 7. CLASS against the complete account

**CLASS(a)–(c): HOLDS**, conditional on the recalled convex-domain Brascamp-Lieb inequality. **The assertion that all three seed-law hypotheses fail: FAILS as a proof.** Literal non-membership is enough to block the direct port; the claimed separate Q and P failures have not been established for the interacting law.

The primary source is Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, [CA-II at 31a47c543775](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L83837). Index rows `ca-full/index.tsv:867–893` and their neighbours were read before the source. The source ranges read for this comparison are CA-II 83820–83975, 83289–83332 and 84940–84995.

At 83837–83866, each K_x is an **“open bounded convex set.”** At 83846–83857 the potential is

    Phi(y) = (1/2)<y,Qy> + <h,y> - P(y),
    Q >= q_- Id,  q_- > 0,  ||P''|| <= varpi <= q_-/4.

The linear term h has no bound. Item (v) separately imposes an exponentially weighted coupling bound; item (vi) preserves the class under conditioning. Consequently Hess Phi >= 3q_-/4, and Brascamp-Lieb gives Cov_mu <= 4 Id/(3q_-), uniformly under linear tilts, in these y coordinates. This proves the abstract portion of CLASS. Strong convexity alone gives that operator bound, not the spatial exponential kernel; the latter also uses item (v).

The covariance-decay lemma at 83869 begins **“Assume the following statement, the Helffer–Sjöstrand covariance representation.”** It also requires extra smoothness and bounded derivatives of P on a neighbourhood of the enlarged compact window (83882–83889). The index label PROVED does not remove either hypothesis. Row 970 acknowledges the representation but omits the extra regularity in its summary. The clean extraction at 83289–83332 is explicitly a fluctuation covariance on a clean branch, at K-s <= j <= K. The class-membership proposition at 84948 starts with explicit operator and locality/analyticity assumptions. None of these passages identifies the unrestricted boundary law m with that fluctuation law.

The failure in the proposed application is precise:

- **W, literal class membership:** J_(b,phi) has a strictly positive density on (S^3)^(2|E(B)|) relative to product Haar. In its stated ambient coordinates it is singular relative to Euclidean Lebesgue measure and its support is not a product of convex windows. Thus it is not literally a member of S, at any beta. A change of variables or a decomposition into windows would require a new argument. A mean plaquette near 0.60 alone does not quantify the mass outside a specified window.
- **Q:** a low eigenvalue in the Gaussian photon model does not prove the same eigenvalue for the interacting boundary law. The exact law contains log Omega. No comparison controlling its Hessian is supplied. Absence of the one-step block constraint does not itself prove absence of every uniform coercivity mechanism.
- **P:** the quoted Wilson Hessian and the bridge's one-link negative curvature do not bound the remainder P'' of a specified representation of the full seed law. No such Q,h,P representation is supplied. The GUIDE numbers therefore cannot establish varpi > q_-/4 for that law.

The repaired reading is: **the cited class-S estimates do not directly supply the seed-scale inequality. Its application remains a new open obligation.** It is not a proof that all three analytic mechanisms fail, or that no other part of the account can supply an estimate.

The bounded source checks support this restriction. CA-I 2533–2564 keeps the running coupling at most gamma_H and explicitly points to block-law statements whose proofs are outstanding. CA-I 2610–2620 asserts no separation decay in its per-ball bound. The outline at 17257 and 32639–32644 retains the small-field thresholds; 31871–31882 separates polynomial clustering from a mass gap. These were found through the outline index and obligations, with neighbouring rows read. No assertion of absence throughout CA-III is made here.

## 8. GUIDE model and arithmetic; consequences for the direction

**7b model guard: HOLDS as a description of the saved check.** `check_models.py` computes S^2 rotor moments, the scalar two-phase flow, and relative entropy for two different priors on the same two-point Gaussian channel. `check_models.log` records the stated parameter grid and errors within its thresholds. The largest listed MM relative error is 2.8e-7. C2's a=3 values divided by 9 give 0.440, 0.546 and 0.811. No run was repeated. Sections 2–4 above check the mathematics by hand; the guard supplies no proof. TIE uses a scalar model with no gauge identification of its two states, so its odd test function is admissible there.

**7a/7c model identification: HOLDS AFTER CORRECTION.** The complete `twoslice_tilt.py` was read. Its staple orientation, negative-cross-product quaternion convention, temporal neighbours, linear tilt and checkerboard updates agree with the stated SU(2) model. At T=5 its intended central marginal is J_(b,phi) formed with m_4 = exp(-V/2) T_0^4 1, up to normalization, not the infinite-depth m. Each half has five free slices, including its retained slice. The two retained slices have full spatial plaquette weight, and the far ends have half weight. At b=0 the two halves factor exactly. At the mid-slice beta=2.6,

    c = 1/(4 beta),  b_t = 4 beta^2 t,
    Var(<z,q~>) = 4 beta^2 Var(<z,x+w>).

The measured electric statistic has the normalization in section 1. Untwisted scalar outputs average the three colours; their expectations equal the one-colour moment by symmetry. With the z twist, the code retains the same x/y statistic and reports colours separately.

There is a numerical implementation caveat: `sweep` replaces |S| by max(|S|,1e-6), then uses S/that value as a unit quaternion. If |S|<1e-6, the new link has norm |S|/1e-6<1. The zero/small-field branch is therefore not an exact Haar heat bath. No minimum-|S| diagnostic is saved to show that branch was unused. A repair would keep an exactly normalized direction and handle the small concentration law separately. This is not evidence that the observed growth is caused by the branch.

**Saved lattice evidence and arithmetic: HOLDS AFTER CORRECTION of its evidential scope.** `batch.log` and `batch2.log` record the listed parameters, durations and successful exits. The cited `results.jsonl` and `results2.jsonl` are absent from this pinned checkout, including ignored files. The batch logs contain no measured values. Thus the reported measurements and error bars cannot be traced to raw results here. The following is hand arithmetic on the note's tables, not independent verification of the samples:

- V0: 4.14 versus 4.19 differs by about 1.2%; 22.98 versus 22.62 by 1.6%. Both are inside 20%.
- V1: 208.7/28.81 is about 7.24; 241.3/33.32 about 7.24; 262.0/34.65 about 7.56. Each exceeds 4. At b=0, replacing the measured cross term by zero is justified for the *target product law*, provided both marginal moment estimates are valid. It does not check their equilibration.
- V2: 784.8/241.3 is about 3.25 and 865.3/262.0 about 3.30. Each exceeds 2. The first gives 4 beta^2 lam_sum about 21,221 at L=12, consistent with “21,000.” The “within 1%” frame-lock statement has a small exception: 28.81 versus 4 times 7.32 differs by about 1.6%.
- W0 fails: 7.42 versus 11.4 differs by about 35%, and 1.59 exceeds 1.5. W1's colour-3 ratios are about 7.75 and 3.30, but the transverse ratios exceed 1.5. The stated formal verdict **INCONCLUSIVE** follows. Colour-3 shares at L=8 and 12 are about 96.0% and 97.3%.

**The inference that integral kbar dt grows like L^3: FAILS.** Three sampled times do not give a lower bound on a time integral, even assuming their variance values were exact and held on arbitrarily large boxes. For fixed sample times t_i, the continuous nonnegative functions

    k_L(t) = 1 + L^3 sum_i max(1 - L^4 |t-t_i|, 0)

have height at least L^3 at each t_i but integral at most c+3/L. A persistence interval of width bounded below independently of L, or another integrated estimate, is missing. Sampling t=c also reads an endpoint of measure zero. Finite spatial sides and finite slab depths add the separate limits already noted. The available GUIDE supports growth at the sampled parameters, not a mathematical refutation of a box-uniform bound.

**The claimed quotient/ABS-flow refutation for SU(2): FAILS as a deduction.** The model TIE supplies no cutoff or transverse estimate in the lattice, as 6.3 itself admits. Gauge-inequivalent states do not imply Q_phi(z)=0: for the usual SO(2) action, phi=(r,0) and unit horizontal z=(1,0) have trivial infinitesimal stabiliser yet Q_phi(z)=1/r^2. Different radii are gauge inequivalent, and that radial test distinguishes them. The gain depends on the orbit geometry of phi and z, not only on whether two states are gauge equivalent. The lattice needs an actual bound on that gain and a justified invariant test-function construction. Run 7c's own verdict is inconclusive.

Accordingly, the supplied arguments do not justify closing the quotient or averaged-flow routes across the whole window. They also do not establish the general claim “strictly stronger than the gap”: the Gaussian example compares finite-box and uniform-box assertions with different quantifiers, while the SU(2) non-implication is only conjectural evidence. The valid no-larger-box observation and the conditional trajectory reduction remain intact. LSI-traj-seed is still open.

SUB also does not refute LOC-COV's typical-tilt formulation, which explicitly allows a bad set and a negative-curvature budget. Ordering at one exceptional tilt does not decide its required recovery estimate.

## Final verdicts

| Statement | Verdict | Boundary |
|---|---|---|
| SUB | HOLDS | Exact temporal-gauge law; nonzero test vector |
| Row-950 identification | HOLDS AFTER CORRECTION | Finite slab versus half-space; covariance versus Hessian constant |
| FH(a)–(d) | HOLDS | Q is defined on the stated stabiliser-fixed vectors |
| QUOT | HOLDS | Conditional on the named flow identity and BR; no supplied seed rate |
| ROTOR | HOLDS | Stated rigid-frame model only |
| TIE(a)–(c) | HOLDS | Stated scalar two-phase model |
| TIE(d) | HOLDS AFTER CORRECTION | Almost everywhere; necessary lower bound, not an admissible rate |
| MM gradient | HOLDS | Gaussian mixture at fixed positive remaining time |
| MM / Markov step | HOLDS AFTER CORRECTION | Explicit Brownian coupling; entropy endpoint justified |
| TRAJ and HC kernel note | HOLDS AFTER CORRECTION | Physical averaged kernel and truncated-time limit made explicit |
| SLAB implication | HOLDS | One common bound at every sufficiently large depth |
| SLAB law description | HOLDS AFTER CORRECTION | Full retained-boundary weight; probability normalization |
| CLASS(a)–(c) | HOLDS | Conditional on convex-domain Brascamp-Lieb |
| CLASS: all three seed hypotheses fail | FAILS | Q and P are not established for the interacting law |
| 7b saved model guard | HOLDS | Model and saved arithmetic only |
| 7a/7c | HOLDS AFTER CORRECTION | Finite-slab model, small-field sampler caveat, raw measurements unavailable |
| Integrated-flow / quotient / ABS-flow refutation | FAILS | Missing uniform time width and lattice transfer |

The errors in the direction statements do not break the independent conditional TRAJ implication. Nothing here supplies LSI-traj-seed, a seed-sized covariance bound, or a Yang–Mills mass gap. No route status is changed.

## Source receipt

The report credits the existing reductions of Claude Fable 5.2 in rows 931, 947, 950, 968 and 970, and Claude Opus 5.5's row-952 GUIDE design. BBD denotes Bauerschmidt, Bodineau and Dagallier. Their flow identities are the named conditional inputs as transcribed in row 968; a targeted filename search did not locate their original PDF in the allowed paper folder, and it was not rechecked here. The entropy calculation above is a separate written derivation. The downloaded CA-II copy is `/tmp/sa-gap-direction2-check-astra.SdiMhh/sa_ca_II.tex`. CA-I and the outline remain in the first scratch directory. No Balaban PDF or OCR layer was needed.

SHA-256 bookkeeping (not mathematical verification):

- `gap-direction2-max.md`: `def641d220cb9e210e4bf1d9ffd17e0c7feeacd0a1ca8279d9680e849352799f`
- `gap-direction-max.md`: `dbf8d872f64475d3b3e81123a69465cde774f4d9b6c1e98d86f90f5473a9637e`
- `gap-fc-max.md`: `890ecc8e4104d31cd30a753ef46c670159ebfcc7784128ba7cf869700c962189`
- `gap-avgcurv-max.md`: `6648a0c433db8f4c60c48f4bfe13195308bf2c73f9242ff84c6321c21bef0b3f`
- `gap-sc-max.md`: `bc6b2f8cae19357dda91881b925857ef7907dae2cc31063b86837e581faf9f29`
- `guide/lane970/twoslice_tilt.py`: `8356cf2941ad5cfc84aa834e54b99575a0567b4318b2a551027fd9ebffc3b155`
- `guide/lane970/check_models.py`: `8e939333f7f05e655984fe1846b3686c8285bb25b53bb78334cd66d89a512dd1`
- `guide/lane970/check_models.log`: `24955642db3de5911fb92b0bf16bb101783c1ccf1e0cf440b4a13b1282495d05`

RESULT: Row 972 checks row 970 at 9bc86cdc2. SUB, FH, conditional QUOT, the model identities and SLAB survive; MM, TRAJ, the HC kernel note and TIE(d) require the explicit corrections above. CLASS's claimed threefold interacting-law failure and the integrated/quotient/ABS-flow refutations do not follow. LSI-traj-seed remains open. GUIDE is finite-model evidence only; raw lattice result files are absent. Research check only, no status granted.
