# Stationary fill supply and mass outside its chart
Provenance: OpenAI Codex; configured model `gpt-6-astra`, effort `max` (read from local configuration, not an independent identification of the backend); pinned commit `dd46a31ef41db19db1d02596f2cfa1e119931ba0`; author research, not an audit, and no status is granted.

## 1. Scope and first distinction

**Unchecked — reading boundary.** This investigation uses the mapped side only, under GOAL.md and FINISH.md's independence, efficiency and research rules. Source labels are not imported as proofs. No numerical experiment or machine enumeration is evidence below. No theorem recalled from memory is used as a discharged premise. The checkout is at the requested commit; the generic workflow is absent from the sparse working tree and was read from that commit with `git show`. The task-specific instructions govern this single-file investigation.

**Unchecked — methodological memory.** Contraction mapping and the fixed-volume Laplace principle are familiar methods recalled from memory. Their uses here are rebuilt by a geometric-series argument and direct upper/lower integral bounds, respectively. The concentration lemma is a named source input, not a remembered theorem silently treated as proved here.

**Discharged — three different assertions.** Existence of a small stationary solution, identification of that solution with an absolute constrained minimum, and concentration of a constrained measure near that solution are different assertions. If a chart is denoted by G and its full-fibre complement by E, their unnormalised masses satisfy

    Z = Z_G + Z_E,       P(E) = Z_E/(Z_G+Z_E).

A statement about the normalised law on G supplies no estimate of Z_E/Z_G. This is an identity of integrals over a disjoint partition; it does not depend on a choice of reference action.

## 2. First attack: release the transverse bonds in hw-fine

**Unchecked — inherited geometry, to be kept distinct.** The two absolute minima in `hw-fine.md`, Sections 5–6, have every transverse bond frozen on faces of thin slabs. That note explicitly does not put these slabs in the cleared, whole-block frozen-layer geometry. Thus those minima alone are not configurations within the several-jump admission hypotheses. The following calculation tests their proposed transplantation when transverse bonds are integration variables.

**Discharged — an exact descent, including its derivative.** Write the example's coordinates as `(r,y,z,w)`, its coupling as `x`, and put

    Z = diag(i,-i),  m=L^N,  alpha=pi/m,
    f(r)=1 at r=1 mod L, -1 at r=-1 mod L, 0 otherwise,
    d_r=f(r+1)-f(r),  Delta s(y)=s(y+1)-s(y).

Use either endpoint profile from hw-fine, so `|Delta s|=alpha` where its chains vary. Let `h(y)` take values in `[0,1]`, vanish wherever transverse bonds must remain fixed, and be positive on at least one free transverse row. For `0<=t<=1` set

    X_1(t)=exp(d_r s(y) Z),
    X_2(t)=exp(t f(r) h(y) Delta s(y) Z),  X_3=X_4=1.

All factors commute. Multiplication around a `(1,2)` plaquette gives the angle

    -d_r [1-t h(y)] Delta s(y).                         (2.1)

The other five orientations have zero angle: in particular `X_2` is independent of z,w, and a `(1,2)` plaquette reads its two direction-2 edges at the same y. There is no difference of h between successive rows. Hence

    dA(X(t))/dt at t=0
      = -sum_(r,y,z,w: |d_r|=1) h(y) alpha sin(alpha) < 0. (2.2)

The inequality uses `0<alpha<pi` and at least one affected plaquette. It is a descent against all the originally frozen longitudinal links as well: those links have not changed.

**Discharged — exact constraints for this descent on the all-lines branch.** The centre-preserving gauge `g(r,y)=exp(f(r)s(y)Z)` sends the field to

    X_1^g=1,  X_2^g=exp(-f(r)[1-t h(y)]Delta s(y)Z).

First-block centres have `f=0`. In each transverse average, `sum_r f(r)=0`; the rooted-contour average cancels under reflection of r, which changes f to -f and leaves h and the y profile unchanged. The specified all-lines formula therefore has identity parents. Every constituent path phase is bounded by `15L alpha<pi`, so taking its logarithm introduces no branch change. Subsequent parents are identity because the first ones are. Choosing alpha below the class threshold keeps the plaquettes and all these paths on that branch. This explicitly verifies the cancellation used in hw-thick, (5)–(7), for the whole path t, not just its endpoints.

**Discharged — what this kills.** Once the displayed transverse rows are free, neither original endpoint is a local constrained minimum: (2.2) is a legal strictly negative first variation. Thus their constrained-minimum proof with transverse bonds frozen cannot establish a second basin for the enlarged integration domain. This conclusion holds before taking a large-coupling limit.

**Implication — a precise large-x statement, with its measure hypothesis visible.** Fix a finite such fibre and a reference measure nu giving finite mass to it and positive mass to every relatively open neighbourhood of the lowered configuration. This measure premise is necessary for an assertion about a hard-conditioned integral. Choose t with `Delta=A(U)-A(X(t))>0`. Continuity gives neighbourhoods N of U and H of X(t) with

    inf_N A >= A(U)-Delta/4,
    sup_H A <= A(U)-3Delta/4.

For the law proportional to `exp(-x A) dnu`, direct upper and lower bounds on the two integrals give

    P_x(N) <= [nu(N)/nu(H)] exp(-x Delta/2).             (2.3)

The same argument applies at T. This is a fixed-fibre conclusion, not a depth- or volume-uniform estimate: the ratio of volumes and the positive Delta depend on the geometry. It excludes persistent mass in sufficiently small neighbourhoods of these two endpoints as x tends to infinity under the stated measure hypothesis. It does not exclude another basin elsewhere or supply a uniform exit estimate.

## 3. What a complement estimate would actually prove

**Discharged — the exact chart/full-law transfer.** For one fixed parent and datum let `mu=(1-q)mu_G+q mu_E`, with `q=mu(E)`. For bounded f,

    |mu(f)-mu_G(f)| <= 2 q ||f||_infinity.                (3.1)

For a square-integrable f the sharper relevant form is

    |mu(f)-mu_G(f)|
      <= sqrt(q) sqrt(mu(|f|^2)) + q |mu_G(f)|.          (3.2)

Both follow by writing the difference as `mu(f 1_E)-q mu_G(f)` and using the triangle inequality, then Cauchy–Schwarz for (3.2). Chart moments alone do not supply the full-law moment in (3.2). A polynomially growing chart observable also requires its definition and control outside that chart before this formula can be used.

**Discharged — the gate's defect 5 survives unchanged under recentering.** Let H be a higher-level event, C the event that the immediate parent is class on the entire read patch, and G its child's chart event. If the reverse kernel is the actual disintegration and the chart bound for E is at most p on C, then

    P(E and H | top)
      <= p P(H | top)
         + P(C and G^c and H | top)
         + P(C^c and H | top).                          (3.3)

Indeed split by C and G and integrate the conditional bound only on `C and G`. The last two events are not estimated by that bound. An unconditional estimate of `P(G^c)` supplies an additive error here; it does not supply the multiplicative price for an arbitrary prescribed set of deep marks. For example, if all mark events equal one event of probability q, their joint probability is q, not q to the number of marks. This example checks the probability inference only; it is not an SU(2) configuration. The actual joint bound needs a full-kernel local odds or compatible-activity estimate stable under the other marks and retained data. Theorem DM's class term has coefficient one for exactly this reason.

**Discharged — a small total error does not automatically give spatial decay.** Write `Z(a,b)=Z_G(a,b)(1+r(a,b))`. If `0<=r<=epsilon` for all four boundary combinations, then

    |log CR(Z)-log CR(Z_G)| <= 2 log(1+epsilon)
                                  <= 2 epsilon.        (3.4)

There are two positive and two negative terms `log(1+r)` in the difference, each in `[0,log(1+epsilon)]`. This proves (3.4). An error independent of shell thickness cannot supply the required decaying cross-ratio at arbitrary thickness. Moreover a gas of many separated rare exits need not have small *total* mass. MD* requires a local decomposition with bounds on the connected terms reaching both boundaries, or an equally strong direct mixed-difference estimate. A one-brick probability estimate is only a first test of that program.

**Discharged — exponentially small complementary mass entails an energy separation at fixed geometry.** Let F be a compact finite-dimensional fibre, nu a finite measure with positive mass on every relative neighbourhood in its support, A continuous, G a chart neighbourhood, and E its complement. Suppose A has chart minimum `A_*` at U_*, and

    Z_E(x)/Z_G(x) <= C x^p exp(-x delta),  delta>0,      (3.5)

for arbitrarily large x, with C,p,delta independent of x. For any v in the support of `nu restricted to E`, continuity gives, for every epsilon>0, a positive-mass set H in E on which `A<=A(v)+epsilon`. On the other hand `Z_G<=nu(G) exp(-x A_*)`. Consequently

    Z_E/Z_G >= [nu(H)/nu(G)]
                 exp(-x[A(v)+epsilon-A_*]).

Comparison with (3.5), taking logarithms, dividing by x and letting x grow, gives `A(v)>=A_*+delta-epsilon`. Let epsilon decrease to zero. Thus (3.5) proves an energy gap on the support of the complement. To infer a statement about every point of F, also require `F=support(nu)` and `E=support(nu restricted to E)`; an isolated excluded null point cannot be tested by its mass. If A restricted to the convex coordinate chart has Hessian at least `m I`, its critical point is its unique chart minimum: integrating the Hessian along a segment gives `A(v)>=A_*+(m/2)|v-U_*|^2`. Under these additional hypotheses (3.5) identifies the unique full-fibre minimum, modulo the gauge already removed.

**Implication — answer to the proposed avoidance of (B).** A direct estimate of integrals can replace an all-chain *proof* of a variational comparison. It cannot make (B) logically irrelevant when it gives the exponential exit estimate (3.5): that estimate implies (B) in the fixed-geometry, zero-temperature limit. Conversely, bare uniqueness of a minimum gives neither a uniform gap as depth grows nor an entropy bound uniform in volume. The signed, multi-level AE-R/HW estimates are stronger than this identification and are not proved necessary by the implication above. At higher RG levels the action and coupling change; the argument applies directly to the underlying finite Wilson fibre, or to a fixed effective action, not without qualification to an x-dependent effective remainder.

**Implication — local exits give the same fixed-volume consequence.** If a finite fibre's complement is covered by finitely many local exit events, each with probability at most `C x^p exp(-delta x)`, the union bound gives the same estimate multiplied by their number. For large x the probability is below 1/2, and its odds are at most twice its probability. Thus (3.5) follows at that fixed volume, with a volume-dependent prefactor. This does not assert that the probability of *some* exit is small uniformly over arbitrarily large volumes at fixed x.

**Gap — what CONC cannot provide.** CONC assumes a convex coordinate domain and a Hessian bound on that domain. Applied to the constructed chart it bounds `mu_G`, hence the first term of (3.3). No argument so far parametrises all label/Haar branches and all exits by that same convex domain with that Hessian bound. In particular, the extra factors enforcing hard constraints and their coarea densities cannot be discarded when transverse bonds are integrated. Calling the law on G a law "on the fibre" does not establish this missing hypothesis. The corrected dimension and solved-bond Lipschitz requirements in defects 3–4 of the specified gate remain additional inputs even for CONC inside G.

**Implication — the part of the complement that convexity does price.** Suppose an enlarged exact chart has a fixed-coordinate patch box `K^+=[-2R,2R]^d`, conditional density proportional to `exp(-S)`, including the Jacobian, `D^2S>=m I`, and conditional mode `eta_*` in `[-R/4,R/4]^d`. Here d is the real dimension, three per independent SU(2) bond, after solving constraints. Supply CONC on this box, uniformly over the allowed exterior chart coordinates. If `mR^2>=16d` and `d>=1`, then its second-moment assertion gives

    E ||eta-eta_*||_infinity <= sqrt(d/m) <= R/4.

The infinity norm is 1-Lipschitz for the Euclidean metric: the difference of two infinity norms is at most the infinity norm, hence the Euclidean norm, of the difference. Exiting `K=[-R,R]^d` forces this norm to exceed `3R/4`. CONC(i), with deviation `R/2`, therefore yields

    P_(K^+)(K^+\K) <= p := exp(-mR^2/16),
    Z_(K^+\K)/Z_K <= p/(1-p) <= 2p.                  (3.6)

The last inequality uses `p<=exp(-1)<1/2`. This is an actual odds bound, conditional on the larger chart, with each constant displayed. It needs a patch-mode estimate and coordinate control but no identification with a minimum outside `K^+`. It says nothing about `F\K^+`; discarding that third region would repeat defect 5.

## 4. Construction (A): the induction one would actually have to close

**Unchecked — one domain, rather than changing domains after inversion.** Fix L, the smallness thresholds, the widened collars, and the read boxes once. Let `D_n` consist of compatible depth-at-most-n pruned hierarchies with class top, the given quiet frozen data, whole parent blocks, and (7.2) of lc-u at every interface **including (7.3) at every truncated top**. Every truncation and every patch to which the induction is applied must belong to the same definition. In particular, quietness is not a substitute for top clearance. The stronger compatibility, response and analytic estimates below are requirements to prove on this domain, not extra facts included by calling a datum quiet.

**Implication — a noncircular quantitative fixed-point lemma.** On any datum in `D_n`, suppose one has constructed a trial `U_tr` respecting the immutable fine boundary and lying on the prescribed class branch. Let `C_n` be the simultaneous retained constraint map, including the actual endpoint-block rows. It is not a sequence of corrections that may spoil previously imposed rows. In one fixed gauge and coordinate space write the gauge-fixed stationary equations and these constraints as

    E_n(z)=r_n+L_n z+N_n(z)=0,  z=(H,lambda),
    E_n(0)=r_n,  DN_n(0)=N_n(0)=0.                    (4.1)

All fine frozen coordinates are removed before forming this system. Supply Banach norms X_n,Y_n on these finite-dimensional spaces and constants M,b,B,r_0, uniform in n and volume, such that

    ||L_n^-1||_(Y_n -> X_n) <= M,
    ||r_n||_Y <= b a,
    ||N_n(z)-N_n(w)||_Y <= B r ||z-w||_X
                              (||z||,||w||<=r<=r_0). (4.2)

Also supply, on each read box `B_S`, the trial and perturbation estimates

    S ||F(U_tr)||_(4,B_S) <= C_tr a,
    S ||F(exp(H)U_tr)-F(U_tr)||_(4,B_S)
                                      <= C_F(r+r^2), (4.3)

where `||H||_X<=r`; exponentiation includes the source's mesh factor. These norms must control local second differences, or give another proved route to (4.3). A possible field part, in compatible local gauges, is the supremum over read boxes of

    S^-1 ||H||_2 + ||nabla H||_2 + S ||nabla^2 H||_2.

This displayed norm is a proposed analytic choice, not a claim that F-D already estimates it. Multiplier norms must include the locally rescaled row bounds of lc-u (8.5).

Choose

    r=2Mb a,
    a <= min{r_0/(2Mb), 1/(2Mb), 1/(8M^2 b B)}.       (4.4)

Terms with a zero coefficient impose no restriction. The map `Tz=-L_n^-1(r_n+N_n(z))` has Lipschitz constant at most `MBr<=1/4`. Its norm on the radius-r ball is at most `Mb a+MBr^2<=3r/4`, using the Lipschitz bound with w=0. Starting at zero, successive differences are bounded by a geometric series with ratio 1/4. They converge in the finite-dimensional closed ball, and continuity gives a fixed point. Two fixed points in the ball have distance at most one quarter of their distance and hence coincide. Equations (4.3)–(4.4) give

    S ||F(U_*)||_(4,B_S) <= (C_tr+4 C_F Mb) a.        (4.5)

Choose a smaller a after these constants so this lies inside the lc-u admission threshold and every intermediate parent has the required class margin. The latter parent estimate must be proved for this same hierarchy; it is not supplied merely by naming (4.5).

**Implication — removal of the gauge term, with its premise explicit.** The true gauge action leaves A invariant. Suppose the chosen gauge-fixed equation is `DA(U_*)+D_tr psi=DC_n(U_*)^*lambda`, and the permitted gauge generators `D_(U_*)omega` annihilate the retained constraints. Pairing with these generators gives `psi` in the kernel of the adjoint of `D_tr^*D_(U_*)` restricted to the permitted gauge parameters. If its inverse exists there, psi=0. For example, invertibility follows from an invertible trial operator B_0 and `||B_0^-1(B-B_0)||<=1/2`: the series `sum_(j>=0)(-B_0^-1(B-B_0))^j B_0^-1` converges. Thus a proved small-perturbation gauge estimate removes the gauge term. This uses gauge invariance of the first derivative, not the stationary Ward identity at the unknown solution as a premise for constructing it.

**Implication — the order of a valid depth induction.** Let H(n) assert trial supply, (4.2)–(4.3), exact constraint/gauge identification, and the constructed solution bounds for every datum in `D_m`, `m<=n`. The base is the single-scale version of those same trial and saddle estimates; it cannot be omitted by calling the data quiet. To prove H(n+1), trials and coefficients may use H(n) only on strict truncations; the depth-n+1 linear saddle must be estimated directly on its trial, using the same pruned geometry. Equations (4.1)–(4.5) then construct the depth-n+1 solution. Regularity and the class margin must hold in the iteration ball before the stationary F-D theorem is invoked at its endpoint. The written contraction has constants independent of n, not a factor M at every scale. If the trial estimates are proved directly for arbitrary n, even this depth induction is unnecessary: the same one-shot fixed point applies to each hierarchy. This is a valid *order*, conditional on those estimates; it neither uses an actual integration variable U nor compares its action with the reference. HW, AE-R and a raw fine-energy cap are absent from the argument.

**Gap — why the supplied several-jump theorem does not yet establish H(n).** There are three precise missing bridges.

1. R1 constructs a one-shot trial from coarse data. Its printed stratified construction does not give a trial with all the arbitrary nested quiet frozen data and all simultaneous residuals bounded in the norms (4.2)–(4.3). Relative quiet is defined using local lifts; replacing those lifts by the new constructed branch changes the predicate unless their equality has been proved. QD controls fully frozen plaquettes, not by itself the relative connection, the mixed plaquettes, or these residual norms.
2. lc-u Section 9 assumes stationary compatible class fills. Section 8 uses stationarity exactly in (8.5) to bound lambda, and uses the stationary Hessian/class identification for (8.7). At a trial with lambda=0 the multiplier term vanishes and the Wilson form estimate is available in principle; this suggests a nonstationary saddle proof. It does **not** justify importing the theorem's stationary Ward/class-identification clause before the solution exists. The off-stationary saddle, right-hand sides, and gauge removal in (4.1) need their own verification. No claim is made that stationarity is intrinsically necessary for invertibility.
3. The several-jump output (9.5) is a graph-space inverse `G* x Lambda -> G x Lambda*`. It is not the local second-difference or curvature-fourth-norm estimate (4.2)–(4.3). R3's torus/interior calculation does not display the required estimate at every frozen wall and junction. In energy-by-stages Section 7(ii), the assertion that every Hessian along `R exp(sH)` obeys F-D "by (R3)" is precisely a domain bootstrap still to check: the intermediate fields are not known stationary, and a graph-norm ball alone does not supply their L^4 curvature. The clause concerning lower frozen layers ends with "Not displayed."

**Gap — decision on (A) from the supplied text.** Construction is a legitimate route independent of HW; the failed dense-energy term is not a logical prerequisite of a fixed-point existence theorem. But the existing estimates do not close the displayed induction on `D_n`. Using F-D only as stated would assume its stationary-background admission at the depth being constructed. Using the energy-stage Corollary instead imports the failed LN Section 6/HW supply. Neither is a proof of (A). I have not found a configuration refuting (A) on the admitted domain, and do not claim its negation.

**Implication — the local part of (B) would follow.** If the constructed point has the true fibre Hessian bounded below by c>0 in its fixed finite-dimensional chart, continuity gives a smaller ball on which that Hessian is at least c/2. Stationarity and two integrations along the segment from zero give `A(Phi(h))-A(U_*) >= (c/4)||h||^2`. Thus it is a strict local minimum in that chart. This does not assert uniqueness among all class configurations, which may lie outside the constructed ball, or minimality against the full integration domain.

**Discharged — stationarity is enough for composition of constructed branches.** In finite local coordinates, suppose a lower branch u(v) satisfies `C(u(v))=v` and `DA(u(v))=DC(u(v))^*lambda(v)`. Define `A_star(v)=A(u(v))`. Differentiating the constraint gives `DC Du=I`; hence `DA_star=lambda`. If v(w) is stationary for `A_star` subject to `M(v)=w`, with multiplier mu, then

    DA(u(v(w)))=DC^* DM^* mu = D(M composed C)^* mu.

Thus the composed branch is stationary for the composite constraint. Uniqueness **inside the common constructed ball**, if supplied by (4.2), identifies it with the directly constructed branch and gives `A_star,next(w)=A_star(v(w))`. Frozen coordinates are simply removed in both differentiations. No absolute minimum is used. This is the action-composition identity that a recentered RG would need; writing each action as an infimum instead reinstates (B).

## 5. Which consumers need identification, and which need probability

**Implication — stationarity supplies the Laplace cancellation.** In a fixed, data-independent coordinate box let `Phi(W,0)=U_*(W)` parametrise the exact fibre, and set

    S_W(xi)=x[A(Phi(W,g xi))-A(U_*(W))]
                       +R(Phi(W,g xi))-log J(W,xi),
    x g^2=1.

Stationarity gives `D_xi(A composed Phi)(W,0)=0` for every W. The classical bracket at xi=0 is identically zero, so all its W derivatives vanish there too. Its second xi derivative carries `xg^2=1`; derivatives of order a>=3 carry `g^(a-2)`. Consequently, given uniform derivatives, convexity and a fixed cut, the H1–H3 hypotheses in the Laplace note require no absolute-minimum identification. The R and Jacobian gradients at zero need not vanish. This proves the cancellation only; the derivative and Hessian estimates remain the named analytic inputs.

**Discharged — why the printed minimum normalization cannot just be renamed.** If the printed classical action is `A_min(W)=inf_F A`, then at xi=0 the classical bracket is `x[A(U_*(W))-A_min(W)]`. Stationarity does not make that number zero. For an x-independent nonzero difference, its size grows linearly in x. It cannot be silently included in a remainder required to be uniformly O(1). Replacing the classical action by `A_star(W)=A(U_*(W))`, with the composition identity above, changes the definition of the classical package and requires a new full-law remainder estimate. It is legitimate as a proposed route, not an established identity with the old package.

**Implication — consumer-by-consumer decision.** Each row distinguishes the mathematical use from the supplied proof. "Could" in the last column is conditional on the stated replacement estimates, not a delivery of that consumer.

| Consumer read | Actual use of the centre and of (B) | What a constructed-centre route must supply |
|---|---|---|
| `(MD*_1)`, quiet-boundary-rarity, Prop MD*, Steps 1–3 | The middle-third covariance reads the stationary constrained Hessian and its absolute fast rate. Global minimality is not used in that covariance identity. The other terms are full integrals: crossings at the lower level and floating rough polymers. | One common chart, FILL on all four boundary combinations, uniform connected exit activities and boundary response, including different layer shapes. A scalar error for total complementary mass does not give the required distance dependence; see (3.4). The printed supply uses Z/DM and their all-chain energy comparisons. |
| `(I_2^D)`, the boundary bulk step and cumulative induction | H3 uses only stationarity. The printed `mathbb A_2^D` is an infimum over class chains; identifying it with the branch value requires (B) on that class, or a separate value identity. Statements of nonnegativity against every chain use the stronger global comparison. | Rebase on `A_star` if changing the package, prove the branch-composition identity, then control the full positive exit sum and its derivatives in the same regions. H1–H3 and the Laplace integral alone estimate only its chart term. The inherited stage Corollary does not supply this at present. |
| `(SCR_1)`, interface and Proposition 20.4/17.2 | It is a statement about the actual reverse law. Its proof reads MD*, FILL, and probabilities of failed explorations and missing regular annuli. It contains no minimum-identification premise of its own. | Full-law rarity for the exact read events, uniformly over the unconditioned histories/mixtures specified there. Retain both errors in (3.3); a pointwise chart estimate under a class immediate parent does not control a deep mark. Preserve the absolute fast exponent and the rare slow tier. |
| K-transport, history-budget-sum Section 4 | It uses lower K2/K3 and SCR for one fixed bounded truncation. It uses neither a classical action nor stationarity nor (B). | Keep the full law: the two locality tails cost `2U B_j Phi_j(k_m)`, and truncation at `U/sqrt(tau_j(m))` costs `3U sqrt(tau_j(m))`. These are the constants in the read proof. Source locality and profile absorption remain separate. Replacing SCR by a chart-law estimate invalidates its middle term. |
| Lemma 14.10, Lemma 14.16, CF and the chart/Laplace step | Equipartition is integration by parts for the specified law. The cancellation `sum_c grad_c=0` in 14.16 is CF's stationarity condition. Neither requires a global minimum. The current and smoothing conclusions also read moments and locality, not just that cancellation. | A fixed chart and its Jacobian, the explicit cut derivative or surface-flux term, the `E^good`/`E^r` identification or covariance transfer, and weighted control of the full-law complement for the observables used. Probability alone does not bound an undefined or unbounded continuation outside the chart; (3.2) states what is needed. |
| RAR^1 and RAR^ch; Theorem DM and Z as their present producers | The probability clauses do not mention minimizers. The printed proofs do: DM's denominator ball is local, but its nonclass numerator in Step 3(b) and its marked class numerator in Step 3(a) use Z/OW/W2, with signed action differences against the constrained reference. | Direct full-kernel estimates for compatible marked events, including exits and rough intermediate parents, would be an alternative producer. CONC on one chart, or separate one-level marginal bounds, supplies neither the joint-history clause nor the mu clause. The unchanged proof therefore still reads the failed energy supply. |

**Discharged — the denominator ball is not where global minimality is spent.** In DM Step 3, a small ball around any admissible stationary U_* with an upper quadratic bound supplies a positive lower bound for the denominator. The lower bound follows by integrating only that ball. Its use needs positivity and local size estimates, not that fields elsewhere have larger action. The step that compares *every numerator field* with that same reference is different; this is precisely where the energy comparison or a full-mass replacement is required. Likewise, existence of one compatible fill gives positivity only for its own data; MD* still needs FILL for the entire product support of its four combinations.

**Implication — consequence for fine energy.** TYP and the specified gate establish an extensive-energy statement for the ordinary Wilson law, with the repaired plaquette-support count. They are not a theorem for a hard-conditioned identity-parent fibre. They therefore neither refute a small stationary background nor prove that the hw-fine pair profiles are typical on that fibre. They do rule out using a depth-independent raw fine-energy cap as a generally typical-field premise for the unconditioned law. The constructed-centre proposal must test own-level chart/flux departures and integrate fine fluctuations, rather than declare the entire extensive energy an exit.

## 6. A strictly smaller mass inequality, and the stopping decision

**Gap — the remaining test (ONE).** Fix L and the mapped thresholds, with `0<T<=1/2`. Use a periodic four-dimensional fine lattice of side `NL`, with N large enough that the chosen plaquette and its one-step read neighbourhood do not wrap. There is **one blocking step**, no frozen datum, no lower history, no effective remainder, and no insertion. Use exactly the mapped Markov kernel of Text 5.2, including its rough-label probabilities, rerouted constraints and Haar-parent branches. All fine links, in particular every transverse link, are integrated.

For a parent field W put

    W_epsilon = { max_(coarse bonds e) angle(W_e) < epsilon },
    0<epsilon<=epsilon_0:=min(T_2/8,1/16),
    E_p = { angle(U_p) >= 2T }

for one specified fine plaquette p. Define finite positive integrals without conditioning on a measure-zero exact parent:

    Z_(N,x,epsilon)(E)
       = integral dU exp(-x A(U)) 1_E(U)
                            K_0(U,W_epsilon).

Here `K_0(U,W_epsilon)` already sums all its auxiliary labels and integrates all parent fields in that set; it lies in `[0,1]`. The sought inequality is

    Z_(N,x,epsilon)(E_p)
      <= C x^(p_0) exp(-c x T^2) Z_(N,x,epsilon)(all),  (ONE)

with `C,c>0`, finite `p_0>=0` and `x_*`, depending on L and the fixed thresholds but **not** on N, epsilon, p or x, for every `x>=x_*`. The constants need not have the absolute fast spatial rate requested by MD*. The neighbourhood formulation demands uniformity as epsilon decreases towards the identity parent and avoids choosing an arbitrary version of a conditional probability at that single parent. No limiting identification of densities is used here.

**Discharged — this test uses positive finite masses.** The integrand is at most one with normalized Haar measure. At U=1 the class map has parent 1 and every label is class. Continuity of its finite all-lines formula gives an open neighbourhood of U=1 on which every flux is below T and the parent belongs to `W_epsilon`. That neighbourhood has positive product Haar mass, and its Wilson weight is positive. The denominator is therefore finite and strictly positive for every finite N,x and epsilon>0. No coarea prescription at an isolated parent is required for (ONE).

**Discharged — (ONE) is a necessary, strictly smaller test of the proposed exit control.** These parent fields are class: if SU(2) factors have angles a,b with a+b<=pi, their scalar quaternion product is at least `cos a cos b-sin a sin b=cos(a+b)`, so the product angle is at most a+b. Iterating on the four edges gives `angle(W_plaquette)<=4epsilon<=T_2/2`. The base chart in the mapped construction has fine plaquette flux at most T. Thus E_p is contained in its complement; a cell with flux at least 2T also carries a forced rough label. Any bound uniform over class parents for this local complement, including all label branches, implies (ONE) by integrating that bound against the true parent marginal over `W_epsilon`.

The restriction is strict in several independent quantifiers: flat-parent neighbourhoods in place of all class parents; no quiet wall; one plaquette in place of arbitrary separated marks or connected exits; one step in place of arbitrary depth; no amplitude exits; no moments or data derivatives. Even proving (ONE) would not settle construction (A), MD*, or the joint rarity clauses. Conversely, a failure of (ONE) would defeat the proposed uniformly rare-complement route already in its simplest class-parent sector. It would not by itself refute the fixed-point existence assertion (A).

**Discharged — the available energy bound and exactly why it falls short.** On E_p,

    A(U) >= 1-cos(2T) >= T^2.                          (6.1)

For the last inequality, on `0<=u<=1` use `sin u<=u` to obtain `cos u>=1-u^2/2>=1/2`. Twice integrating `cos u-1/2>=0`, with zero value and derivative at zero, gives `1-cos u>=u^2/4`; take u=2T. Consequently the numerator in (ONE) is at most `exp(-xT^2)` with normalized product Haar measure. This estimate loses the parent-window mass entirely. A lower bound obtained by restricting every fine link to a small neighbourhood of identity costs a power of its radius for **every** free bond, hence grows with the volume and deteriorates as epsilon shrinks. It cannot provide the constants in (ONE). The missing step is cancellation/localisation of that constrained entropy, not the elementary positive energy of a rough plaquette.

**Unchecked — expectation and reason.** I expect (ONE) to be true for this fixed-L kernel at sufficiently large x. The reason is that the flat reference has zero action, the event has the definite local cost (6.1), and the proposed antipodal frustration is removed by free transverse variations preserving the parents. A successful local integrated comparison should lose only a fixed number of powers of x per defect, rather than a power per bond of the torus. That last comparison is the unproved inequality, not a consequence of locality by itself. I have neither a hand-checkable counterconfiguration to (ONE) nor a volume- and epsilon-uniform proof of it. This expectation carries no status.

**Gap — decision.** (A) is not proved by the stated stationary F-D theorem; Section 4 supplies the exact noncircular contract and identifies its missing analytic admission steps. (B) is not refuted on the admitted geometry by hw-fine: its two minima lose stationarity when the relevant transverse bonds are released. Stationarity suffices for the local chart and Laplace algebra, and the probabilistic consumers could use a new full-mass producer. Such a producer cannot be replaced by CONC on the chart or by the tower property, and exponential suppression would itself imply minimum identification at fixed geometry. The investigation stops at the single inequality (ONE), with the strict reduction and expectation stated above, rather than asserting that HW is necessary or that the constructed-centre route closes.

## 7. Reading and evidence boundary

**Unchecked — bounded source record.** Read GOAL and the three requested FINISH sections first. The mathematical reads were the specified portions of hw-fine; hw-thick Sections 3 and 5; lift-nonlinear Section 6; heavy-wall Section 5; lc-u Sections 1 and 6–9; mapped Text 5.1–5.3 and 5.9 and relevant statement searches; quiet-boundary-rarity's Setting, Z/DM, MD*, boundary bulk step and induction; energy-by-stages Sections 2 and 7; active-energy-junction-cubes' statement and open-input sections; fibre-propagator's setting and torus theorem; and fd-jumps' first obligation and scalar test. Read explicit-region-two-step's TYP, CONC/FIB and two-step definitions, and the specified gate's relevant verdicts and defects 3–6. Consumer checks used upper-chain's neutral interface and the relevant Text 14, 17, 20 and 21 statements/proofs, convex-laplace-tree-decay's hypotheses, generated-observable-history's transport pointer, and history-budget-sum Section 4. Searches in the upper-chain file also exposed attribution and historical snippets referring to the other attempt; no proof from that attempt is used here, and its chart-development sections were not opened for this argument.

**Discharged — operational boundary.** None of the expressly forbidden files or gates was opened. No external literature, mathematical computation, numerical run, enumeration, audit, subagent, commit, push or post was used. Only this file was written. Source assertions left as premises are labelled implication or gap above; the fixed-point and integral algebra do not certify those premises.

STOPPED
