# PRE-STATED — independent hostile review of MINCB55

UTC: 2026-10-29 06:16:01. Written before derivations. Reviewer: Codex; an independent check of the named Opus result. This report does not certify runtime model provenance that the reviewer cannot inspect.

Scope: MINCB55.md, beginning with withdrawn corollary E11; the named consumer/source files and mc55_1–3 checks, accessed by locating strings and bounded ranges. No git commands; this is the sole writable deliverable. Any additional reads will be recorded. Exact rational/symbolic arithmetic in plain Python only.

Pre-stated refutation targets:

1. T1 census: find an omitted reader, an upper-bound/minimum use misclassified as critical-value data, or a chart/domain mismatch in the five purported restricted-minimum consumers. Exhaustiveness needs evidence beyond a selected list.
2. RSM_j: rebuild the Hessian-Lipschitz estimate, trivial-point slice coercivity, critical-chain Schur complement, gauge invariance and attainment implications. A missing uniform constant, wrong slice, incompatible quantifier, or unproved passage between charts defeats the stated implication. Check coarse-fixed versus coarse-free curvature explicitly.
3. LIFT_j and tower: check path/contour bounds and every radius inclusion. Refutation includes an allowed datum whose critical chain is outside the declared minimizing set, or an equality claim requiring gauges beyond the proved invariance domain.
4. FLAT/MIN-fin and MARGIN: reconstruct the zero-energy and compactness arguments; check the quantitative link/plaquette/residual constants separately. Compare nonlinear critical values with STEP55's linear coercivity without identifying different objects.
5. BFT4B bridge: check positivity, exact energy assignment, holomorphy and depth-uniform cube bounds with sigma positive. Distinguish those statements from derivative locality and DENS-reg. An algebraic density identity does not prove differentiated gluing.
6. Findings F-2/F-3/F-5/F-10 and both NOT-VERIFIED findings: evaluate the underlying statements independently. For mc55_1–3, inspect whether each gate could fail and what it actually discriminates; no numerical PASS will be inferred from the author's report.
7. Pin symbols to files and strings; inspect cited line numbers when encountered. Reused names, changed input/output minima, vacuous tests, and impossible gates are explicit attack surfaces.

Review verdict vocabulary: CONFIRMED / NOT-VERIFIED / REFUTED. Claim vocabulary: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. Findings and the final bankable scope will be appended incrementally; a cited prior verdict is not independent evidence.

## Read record

- MINCB55.md: initial locating scan and E11 range; scientific derivations not yet undertaken at this checkpoint.
- docs/ai_methodology/SCIENCE_WORKFLOW.md: bounded operating-rule read required by the supplied agent entry point. The user's later no-git and single-output scope control this assignment.

## Findings (incremental)

### R1 — REFUTED: bounded perturbative Hessians do not preserve a lower bound at the old background

Attachment: MINCB55.md:377–378, locating string `change the Hessian by O(1) per link ... so they do not spoil the bound for g_k small`; also F-15 and the proposed CE-Q-infinity chart discharge in section 10. Claim status: GAP for the full action, even if RSM for the main term is granted.

Re-derivation: take a slice coordinate a, main term F(a)=gamma*a^2/4 with background a=0, and an allowed bounded analytic perturbation P(a)=a on a fixed small chart. The total action S(a)=u*gamma*a^2/4+a has exactly the same Hessian as uF. Nevertheless S(-2/(u*gamma))-S(0)=-1/(u*gamma)<0. For any fixed chart this point lies inside it when u is sufficiently large. Thus no positive quadratic lower bound for S(a)-S(0) follows from the asserted Hessian comparison. This refutes the implication, not a claim that the actual normalizer equals this test perturbation.

The missing hypothesis is DP(0)=0 (criticality of the full action at the same background), or a construction of the shifted critical point with control of its displacement, value and locality. In general strong convexity yields S(a)-S(0) >= DS(0)[a] + (u*gamma/4-C/2)*||a||^2, including the linear term. Section 4.4 itself names full-action criticality separately. E6 repairs the coordinate-locality wording but does not repair this first-derivative problem. Bank only the main-term chart inequality at this stage.

### R2 — CONFIRMED: E11 repairs the exact-lift multiplicity; the withdrawn uniform upper bound remains REFUTED

Attachments: MINCB55.md:761–775, strings `Corollary UB` and `E11`; PROOF.md:5895–5911, `Lemma U0 (the exact lift)`; PROOF.md:6685–6704, `Lemma TOWER-VAR` (b). Claim status: PROVEN for the counting identity; CONDITIONAL for its transfer to the critical value through RSM-tower.

Fix an oriented coarse (mu,nu)-plaquette. Its crossing fine plaquettes have their mu and nu coordinates fixed at the respective block boundaries. Each of the d-2 transverse coordinates has L independent choices. Therefore the count is L^(d-2), not 1. Iterating k times gives L^((d-2)k); in d=4 this is L^(2k), and at L=3 it is 9^k (9 at one step, 81 at two). The soft terms of the lift vanish, so its energy is exactly this multiplicity times the coarse Wilson action. The valid comparison is E_cb <= L^(2k)*S_W, conditional on RSM-tower, and no depth-uniform upper bound follows. When the coarse field is flat both sides are zero, so the multiplicity error does not damage the zero-energy argument in FLAT.

### R3 — NOT-VERIFIED: the stated radii do not establish attainment in the declared minimizing class

Attachments: MINCB55.md:248–259 (`Theorem RSM_j`, `is the minimum`), 311–318 (`RSM_j-class`), 347–356 (`MIN_1-w`), 738–748 (E2/E4). Claim status: GAP for the attainment statements with precisely these radii; the comparison inequality is a separate question.

The proof places the slice representative w_* in the rho_c/2 ball, whereas the asserted minimization domain is the rho_M ball. Neither inclusion rho_c/2 <= rho_M nor a critical-chain bound C_0'*epsilon_M/L <= rho_M is stated. E2 gives C_0'*epsilon_M/L <= epsilon_GI, which is a different object. The still stronger requirement for MIN_1-w is Z_1(v) in S_0(v;epsilon'_M), whose defining plaquette/residual threshold is epsilon'_M = rho_M/[3*sqrt(N)*(1+2*sqrt(N)*n_L)]. E4 asserts this because `it is small`, without comparing these thresholds.

A sufficient explicit repair, using In-A with eta=C_0*epsilon_M, is to impose C_0'*epsilon_M/L <= rho_M, L^(-2)*(2*eta+9*eta^2) <= epsilon'_M, and eta+C_rho*L^(-3)*eta^2 <= epsilon'_M (in the stated HS convention, with any required norm-conversion factors). These are compatible fixed-radius shrinkages, but the present proof must actually make them before claiming the minimum is attained on this particular class. This is not a counterexample to the existence of suitably smaller radii.

### R4 — REFUTED: M13 is presented as a current consumer using a superseded SF obligation

Attachments: MINCB55.md:115 (`M13`), 372–383 (`What SF's (CE-Q^infinity) needs`), 724–725 (proposal to record the chart part as supplied); SF.md:1203–1209 (`the exact wall`), 2100–2101 (`Restated (CE-Q^infinity) after session 5`). Locating strings, including the literal infinity symbol in the source, are authoritative.

MINCB quotes SF's session-3 coercivity requirement as the live wall. SF subsequently restates the deep-chart part as DX-prime, conditional on FP-det and BGC, plus DX-loc and CH-c, and explicitly says the session-4 SL-coer-prime wall on the half-chart `is not needed and is not attacked`. Thus the five-reader census is not a verified census of current obligations: its fifth entry has been superseded in the very file it cites. This does not prove that no other SF argument can use a margin. It does refute treating this historical sentence as evidence that the current CE-Q-infinity route needs the claimed new input. Claim status: GAP for the proposed downstream discharge; current consumer reconciliation remains OPEN.

### R5 — REFUTED: DENS's term-count argument silently changes the lexicographic assignment at a torus seam

Attachments: MINCB55.md:490–513 (`Proposition DENS`, `there are <= 6L^{4k}`, `base root in x number <= 4L^{4m}`); HIST.md:1407–1408 (`lexicographically first vertex`). Claim status: GAP for the displayed C_dens proof with this assignment. The numerical energy bound itself is NOT-VERIFIED, not disproved: slack in other estimates might rescue it.

The definition assigns a term to the ancestor of its lexicographically first vertex. The proof instead counts plaquettes by base vertices and soft terms by base roots. These agree away from a periodic seam, but not under the literal global lexicographic ordering of torus representatives.

Exact countercount: d=4, L=3, k=1, T=3. In the zero cube, for each plaquette orientation, the two plaquette directions have L+1 possible bases (the ordinary L bases and the wrapped final base); the transverse directions have L choices. Thus there are 6*(L+1)^2*L^2 = **864**, not at most 6*L^4 = **486**, assigned plaquettes. A top soft term's S4-prime support is the union of the two adjacent fine blocks. Each of the four directions contributes both the 0-to-1 coarse link and the wrapped 2-to-0 link to the zero cube: **8**, not at most **4**, soft terms. Plain-Python integer enumeration reproduced these numbers; total counts were 39366=6*9^4 plaquettes and 324=4*3^4 soft terms, so the discrepancy is assignment, not duplicated terms.

For n=L^k the safe Wilson count is 6*(n+1)^2*n^2. For n=L^m at soft depth m=k-1-i, it is 4*(n+1)*n^3. A conservative corrected coefficient, retaining the author's other bounds, is

`C_dens_lex = 3*N*(1+1/L)^2*(2+9*eta)^2 + 4*kappa_plus*(1+2*delta_rho) * [1/(1-L^(-2*sigma)) + 1/(1-L^(-(2*sigma+1))) + C_rho^2*eta^2*L^(-6)*(1/(1-L^(-2)) + 1/(1-L^(-3)))]`.

At L=3 the Wilson multiplier is 16/9. The corrected leading soft bracket is 225/104 for sigma=1 (instead of 9/8), and 21/8 for sigma=1/2 (instead of 3/2). These are conservative proof coefficients, not claimed optimal energies. They remain depth-uniform when sigma>0. Alternatively, explicitly define a translation-covariant lifted/base-root assignment, change the density definition accordingly, and prove its consumer interfaces. An unstated convention cannot identify the two density assignments. mc55_1 explicitly excludes geometric counting from its scope, so its PASS cannot detect this defect.

### R6 — REFUTED: FLAT's explicit gauge has the matrix factors in the wrong order

Attachment: MINCB55.md:442–445, locating string `g(z) := T^{(1)}(c ... z)T^{(2)}(c ... z)^{-1}`. Claim status: PROVEN after the algebraic repair below; this error does not refute the single-orbit conclusion.

In this file's convention U^g_xy = g(x)*U_xy*g(y)^(-1), a transport from a pinned root obeys T^g(c,z)=T(c,z)*g(z)^(-1). To map connection 2 to connection 1, the gauge must therefore be

`g(z) = T_1(c,z)^(-1) * T_2(c,z)`,

not `T_1(c,z) * T_2(c,z)^(-1)`. The repaired expression is path independent: replacing the path multiplies both transports on the left by the common based holonomy H, and `(H*T_1)^(-1)*(H*T_2)=T_1^(-1)*T_2`. The printed expression instead becomes `H*T_1*T_2^(-1)*H^(-1)`, which need not be unchanged.

Exact SU(2) witness in unit-quaternion coordinates: choose transports p=(3/5,4/5,0,0), q=(3/5,0,4/5,0) at one non-root vertex, identity at roots, and define flat pure-gauge connections from these vertex transports. The printed gauge at that vertex is p*q^(-1). On a root-to-vertex link it sends the second transport q to q^2*p^(-1)=(-21/125,28/125,72/125,96/125), which is not p; it does not map the first transport to q either. The repaired gauge p^(-1)*q sends q to p exactly. These configurations have identity transport between roots and satisfy the zero-energy constraints. After this repair the based-holonomy proof of FLAT(i), including nontrivial torons, is valid.

The same action-order error occurs at MINCB55.md:274, `e^{xi_*}e^{-xi(w)}`. NSL55.md:78 explicitly defines `(x^g)^h=x^{h g}`. Consequently `w = (U_cb)^{exp(-xi(w))*exp(xi_*)}`, with the factors in that order. The existence of some root-trivial composite gauge survives; the printed identity does not.

### R7 — REFUTED: GI_j confuses the covariant nonlinear residual rho with the weighted linear residual r

Attachments: MINCB55.md:233–236, `the weighted residual part is unchanged (endpoint covariance)` and the displayed `r_y`; NSL55.md:81–88 (the actual norm and residual definitions), 269–294 (`Lemma C`, `Lemma D`). Claim status: GAP in the current proof of GI_j, hence in its dependent RSM argument until repaired. This is a load-bearing symbol/object collision, not merely notation.

The norm contains `r_i = Q*x_i - x_(i+1)`. Endpoint covariance holds for `rho_i = log(U_(i+1)^(-1)*W_0(Mbar(U_i)))`, not for r_i. A nonabelian pure gauge has rho_i=0 but generally r_i != 0. Thus the stated invariance of the residual part, used to put the transported chain in NSL/K-U's ball, is false.

Exact second-order witness using GI's own interpolation: take depth 1, L=3, d=4, coarse torus side 9 (fine side 27), the depth-1 cut of a depth-2 hierarchy with final side T=3. At coarse roots c0=(1,1,1,1) and c1=(4,1,1,1), assign xi=t*A and xi=t*B respectively, with [A,B]!=0; assign zero at all other coarse roots. This is zero at all next-level roots. Let `a(z)=product_nu sigma_5(dist_27(z_nu,c0_nu)/3)` and b analogously for c1, with each factor zero outside distance 3, and let g(z)=exp(t*(a(z)*A+b(z)*B)). Transform the trivial chain and its datum by this gauge. All nonlinear residuals remain exactly zero.

For a fine edge x-to-y, BCH gives `log(g(x)*g(y)^(-1)) = t*(xi0(x)-xi0(y)) - t^2*[xi0(x),xi0(y)]/2 + O(t^3)`, with xi0=a*A+b*B. The bracket coefficient is `a(x)*b(y)-b(x)*a(y)`. Summing it along each S4-prime contour from c0 to c1, then averaging over 24 axis orders and 81 starting sites, plain-Python Fraction arithmetic gives

`Q[bracket coefficient] = 282736057690327/617673396283947`,

whereas the coarse endpoint bracket coefficient is 1. Therefore

`r_0 = (167468669296810/617673396283947)*t^2*[A,B] + O(t^3)`,

which is nonzero for sufficiently small nonzero t. The enumeration covered 1944 contours and 162 fine vertices; no floating-point arithmetic or matrix numerics was used. This tests the actual tent lift, rather than an arbitrary gauge outside GI's construction.

Repair mechanism, re-derived: write rho=r+Delta and assume the local remainder estimate `|Delta_i| <= C_Delta*(h_i^3*eta^2+h_i*eta*|r_i|)`. Covariance of rho and absorption of `C_Delta*h_i*eta(y)<=1/2` give

`|r_i(y)| <= 3*|r_i(x)| + 2*C_Delta*h_i^3*(eta(x)^2+eta(y)^2)`.

Multiplication by the own-unit residual weight gives `L^((2+sigma)*(j-1-i))*h_i^3 = L^(-3)*L^((sigma-1)*(j-1-i)) <= L^(-3)` for sigma<=1. Thus, with a=||xi_tilde||_natural and b=C_0'*||w||_D, a safe replacement for the claimed transported norm bound is

`||y||_(sigma,j) <= (3+5*K_G*a)*b + a*(1+25*K_G*a) + 2*C_Delta*L^(-3)*(eta(x)^2+eta(y)^2)`.

One must enforce the eta-smallness conditions and shrink epsilon_GI, delta_GI using this bound before applying NSL and K-U. It tends to zero uniformly with (a,b), so the invariance theorem is repairable as a CONDITIONAL implication with this additional local-remainder control. The original `r_y` and its radius-selection proof cannot be banked unchanged.

### R8 — CONFIRMED: HL, the envelope-gradient mechanism, and the slice-angle argument, with explicit premises

Attachments: MINCB55.md:171–218 (`Lemma HL`, `Lemma GC`, `Lemma ANG`); PROOF.md:5398–5403 (`Setting N5-0`), 5429–5447 (`Lemma N5-coer`); NSL55.md:201–214 (`Lemma A`). Claim status: PROVEN for HL; CONDITIONAL for GC/ANG on the stated analytic, linear-gauge and coercivity inputs. This does not independently certify the frozen NA-lev constant.

HL re-derivation: for real h with ||h||_infinity<=1, Cauchy on the complex line z+zeta*h bounds each component of H(z)h by 2G/R on P_(R/2). A second directional Cauchy estimate on a line of radius R/4 bounds each component of D H(w)[v]h by 8G/R^2 when ||v||_infinity<=1. At real w these matrices are real symmetric. Choosing h to be the signs of any one row converts the directional estimate into its absolute row sum; symmetry gives the same column bound, and Schur gives the l2 operator bound. Integrating DH along the real segment proves the claimed Lipschitz estimate. No dimension factor or spatial locality has been smuggled in. Reality is essential to this particular row-sign argument and is present.

GC re-derivation: differentiate E(w)=F(Z(w),w). The Z derivative vanishes because F_x=0. This identity extends from the real slice to the complex polydisc by holomorphy. A datum component w_y occurs explicitly in only its top soft term, so a fixed interior local Cauchy radius bounds its derivative independently of depth and volume. For K, the number of contours reading a given fine link is bounded at fixed L,d. This proves existence of G_E,G_K after a uniform interior shrink; it does not require high-order BFT locality.

ANG re-derivation: the Hessian of the eliminated critical value at zero is a Schur complement. The full quadratic chain form is positive semidefinite, with precisely finer gauge degeneracy, so eliminating any complementary slice gives its quadratic minimum H_j. The fixed-coarse one-step form is A_j=H_j+kappa_j*Q^T*Q. It annihilates d*lambda for gauges pinned at the next roots. On pinned lambda, the map `(h(d*lambda), P_res*Delta*lambda)` is injective: its first component makes lambda block-mean zero, and testing the second against lambda gives ||d*lambda||^2=0, hence lambda=0. Domain and codomain each have dimension n_sites-n_blocks per color, so the map is bijective.

Thus any h in ker(Lambda) can be written h=h_N+d*lambda with h_N in ker(h_slice) intersect ker(P_res*d_adjoint). Since Lambda(d*lambda)=-lambda, one has lambda=Lambda(h_N), hence ||h||_2 <= (1+||d*Lambda||)*||h_N||_2. Gauge invariance removes the d*lambda term, and the gauge-fixing quadratic vanishes on h_N. N5-coer therefore gives `A_j[h,h] >= gamma_min/(1+C_dLambda)^2 * ||h||_2^2`. At depth one Lambda is a fixed-range finite-dimensional block map, so its row/column sums and C_dLambda are uniformly finite. This establishes the angle transfer without identifying the two slices or identifying gamma with an unrelated lane constant.

### R9 — CONFIRMED: LIFT and the main-term margin; the soft-residual numerical claim requires E5's restriction

Attachments: MINCB55.md:285–308 (`Lemma LIFT_j`), 363–368 (`Corollary MARGIN`), E5/E6; PROOF.md:5905–5911 (actual S4-prime contour); mc55_3 criteria and script. Claim status: PROVEN for the path-count geometry; CONDITIONAL on the stated NA-alg input for the maximizer step, and on a valid RSM chart for the margin. The E5 soft-residual coefficient remains ARGUED.

Re-derivation: in a block axial gauge each off-tree link is a ladder of at most sum_(nu>mu)|x_nu-c_nu| plaquettes, at most (d-1)(L-1)/2. A boundary-link root-to-root path and any S4-prime contour lie in the same adjacent-block box. Their combined length is at most 2*d*(L-1)+L+1 and the box l1 diameter is (2L-1)+(d-1)*(L-1). Decomposing the loop into axial ladders bounds its transport difference by the product of these numbers times epsilon-prime. This gives n_L=220 for d=4,L=3; the d=3 test correctly uses 144. For T>=3 the box can be lifted without closing a torus cycle, including across a chosen seam.

For the maximizer estimate put x=sqrt(N)*n_L*epsilon-prime<=1/30 and y<=(26/25)*x. NA-alg gives |X_0|<=1.46*y. The rational inequality exp(t)-1<=t/(1-t), 0<=t<1, then gives `(exp(1.46*y)-1)/x <= 28470/17801 < 17/10`. Thus the 1.7 factor is justified with room; the stated 2 factor and principal-log estimate follow. This check uses a rational exponential majorant, not floating-point exponentials.

For the real main-term margin, the exponential map on skew-Hermitian matrices obeys `||exp(A)-exp(B)||_op <= ||A-B||_op`, by integrating `exp((1-t)A)*(A-B)*exp(tB)` and using unitarity. Consequently RSM's gamma_M/4 log-coordinate margin implies even gamma_M*tau^2/4 for a link difference tau; the author's weaker /5 is safe. Telescoping a four-link plaquette gives a factor 4, so /64 is a sufficient plaquette coefficient; /97 is conservative. The same four-link constant does not apply to a soft residual with longer contours. E5 correctly withdraws that extension. Its proposed `gamma_M*tau^2/(20*ell_c^2)` still needs the stated W_0 Lipschitz estimate; this review does not upgrade ARGUED to PROVEN.

### R10 — CONFIRMED: the repaired local-minimum mechanism and its depth-independent telescoping; exact stated attainment remains R3

Attachments: MINCB55.md:244–283 (`Theorem RSM_j`), 320–357 (`RSM-tower`, `MIN_1-w`); LCONV55.md:90–108 (`following set`, `Lemma FOL`), 277–296 (`Theorem NC`). Claim status: CONDITIONAL on In-A–In-J, the repaired GI control in R7 and the radius inclusions in R3. The original uncorrected source is not certified wholesale.

Once those premises hold, HL+ANG give Hess F_j >= gamma_M/2 on the convex slice ball with the coarse v fixed. ID supplies the one-step critical point, NSL places it in the slice, and corrected GI preserves its value and criticality under the fixed gauge diffeomorphism. Integrating the Hessian twice along the segment from that point gives the gamma_M/4 quadratic comparison. Equality at the minimum forces the same slice point and hence the same root-trivial orbit. For a general small-field-class member, LIFT puts it in a sup chart; two such representatives differ by a small gauge because each is linked to a pinned root by a uniformly bounded number of small-link steps. Corrected GI makes the value well defined. R3's extra inequalities are needed to place the minimizing orbit itself in that class.

The tower inequality uses the same radius R=min(rho_M,epsilon_M) at every step: apply the depth-j inequality with datum u_j, then the one-step inequality with fixed datum u_(j+1). No product of radii or constants is incurred. Equality can be glued using ID and correctly ordered composite gauges. To assert attainment and symmetry, require `||B||_D <= min(R, L*R/C_0, epsilon_0)`; then BFT-1 puts every component of Z_k(B) in the competitor class. Including R explicitly avoids depending on an unstated C_0>=L convention in the displayed epsilon_att. This remains a positive depth- and volume-independent datum radius.

There is no contradiction with LCONV: for a soft term near zero mismatch its quadratic form is proportional to `||Q*delta_u-delta_v||^2`. A following variation has delta_v=Q*delta_u and receives zero soft curvature; a fixed-coarse variation has delta_v=0 and retains kappa*Q^T*Q. RSM treats the latter, while NC frees the coarse variables. RSM proves a minimum/comparison in a specified class, not joint convexity of the whole multiscale measure. The NC theorem itself was not independently re-proved here.

### R11 — CONFIRMED: FLAT and MIN-fin after the named algebra/radius repairs; uniform MIN-cb stays OPEN

Attachments: MINCB55.md:435–482 (`Proposition FLAT`, `Proposition MIN-fin`, `Verdict on uniform (MIN-cb)`), E3/E11; PROOF.md:5895–5916 and 6685–6704. Claim status: PROVEN for the zero-orbit geometry with R6's corrected gauge; CONDITIONAL for identification with the given critical branch.

Every chain summand is nonnegative. Zero energy forces the fine field flat; all paths through an adjacent-block box then have one transport. Its unitary average has unique maximizer equal to that transport, so each next field is exactly the blocked flat field. Iterating preserves the based holonomies of all torus cycles and transports between top roots. The corrected gauge in R6 identifies any two zero chains and is identity at every top root. The exact lift supplies such a chain for any flat V; E11's multiplicity is irrelevant at zero. RSM-tower's comparison then identifies the critical value with zero on its scoped datum ball.

For fixed finite k,T the chain space is compact and the energy continuous (a maximum of linear continuous functions over compact SU(N) is continuous even where the maximizer is not unique). The complement of any open neighborhood of the zero orbit has energy at least a positive delta_(k,T). Uniform continuity keeps it above delta/2 for sufficiently small B, while the analytic critical branch has energy tending to zero. Therefore all global minimizers enter that neighborhood. The local slice comparison/uniqueness identifies them with the critical orbit. This proves an epsilon_(k,T)>0, not a uniform epsilon. E3 correctly withdraws its nonlinear use of E-low. Neither this compactness proof nor its volume-dependent cutoff proves that every possible uniform proof is impossible.

### R12 — NOT-VERIFIED: the universal T1 census and the proposed cost-free consumer replacement

Attachments: MINCB55.md:100–126 (M1–M16 and `Answer to T1`), 706–725 (`For the lead`); FLOW.md:134–139 (`Def F-strip`), 240–246 (Laplace integral), 310–321 (`Lemma F-tel`); HIST.md:1399–1416 (localized infimum, superadditivity, recursion and assignment), 1756–1761 (`Self-reproduction in critical-value form`); PLD.md:985–1023 (fixed-V fluctuation law and background map). Claim status: GAP for closing the whole consumer item; restricted-route viability is CONDITIONAL.

The arithmetic census is repaired by E1: ten proposed c/d entries, five proposed restricted entries, and M12 retired under the proposal. That is a classification of a proposed reformulation, not a proof that all current source statements already consume the new object. M13 is stale (R4). M16 is expressly an unrestricted Laplace-limit motivation, not an established critical-value consumer. FLOW's displayed integral in section 5.1 has no small-chart restriction, and Def F-strip explicitly minimizes over a compact group power. A small-chart minimum cannot by itself determine the leading exponent of an unrestricted integral: on a compact domain, neighborhoods of a strictly smaller exterior minimum contribute an exponentially larger term. One must either restrict that integral and control the complement, or keep the full-minimum assertion. Its formal trivial-point jets can be handled by MIN-fin; the uniform near-field integral statement needs its own reformulation.

HIST's localized infimum also supplies superadditivity and the recursion defect assigned to the boundary. For an arbitrary chain, restriction supplies a competitor for each localized infimum; after replacing those infima by region critical values, the same argument needs compatible restricted classes and regional minimum comparisons. Torus RSM does not prove those assertions on regions with holes. PLD explicitly uses a conditional law over the history's local small-field domain, so a minimum on an arbitrarily smaller globally gauged ball does not alone verify that domain's concentration estimate. These are concrete domain/interface obligations, not evidence that a global minimum is inherently necessary for every architecture.

Requested missed-reader search: a bounded lane-wide filename scan for min-tower/E_k/T_k/MIN-cb/minimizer-critical-value strings (excluding snapshots, audit/ledger paths, checks and scratchpad) found **STEP55.md**, which is absent from M1–M16. Its section 2.4 charge allocation and section 2.5 critical-tower comparison are additional readers. Their inspected proofs use a certificate for every chain and the critical chain's estimates, respectively, so they do not supply a counterexample to the proposed c/d classification. Other discovery hits were not opened outside the permitted source set; exhaustiveness is NOT-VERIFIED. This is a search result, not a no-consumer theorem.

Independent disposition of the four inherited refutations and the two uncertainties:

| MINCB item | Review verdict | Re-derived reason and limit |
|---|---|---|
| F-2, ASSEMBLY55:96 `Positivity, the one min-property used` | CONFIRMED as a refutation of that sentence | A positive critical value need not be the least value on the integration domain; e.g. f(x)=(x^2-1)^2 has critical value 1 at 0 and value 0 at +/-1. A Laplace comparison needs more than positivity. |
| F-3, ASSEMBLY55:96 `(i) is needed` for lower bounds | CONFIRMED as a refutation, on a common domain | For every chain x, F(x)>=inf F. Therefore inf F>=L implies F(x*)>=L without identifying x* as a minimizer. Off the critical branch's domain the replacement object still must be constructed. |
| F-5, HIST:1760 `global minimiser ... needs` | CONFIRMED only as a refutation of necessity for an explicitly cut, separately priced route | The chart integral needs domination on its own support; no exterior minimum enters that integral. This does not validate the unchanged unrestricted FLOW formula or the complete regional replacement. |
| F-10, NSL55:394 `exactly the gauges` | CONFIRMED as a refutation | At v=0 the constant SU(2) gauge diag(i,-i) fixes the datum and conjugates all transports and plaquettes, preserving their traces and the maximized soft terms. It is not identity at roots; it conjugates i*sigma_1 to -i*sigma_1. Root-trivial gauges form a subgroup, not the full stabilizer. |
| F-7, claimed BFT implication to all global minimizers | NOT-VERIFIED | A local unique analytic critical branch does not control other distant minima; f(x)=x^2*(x-2)^2 already separates those quantifiers. The quoted REVIEW_S22 source itself was not opened beyond the permitted read set. |
| F-18, NA-lev's c_1=1/3500000 | NOT-VERIFIED | The N5 decomposition and slice transfer were rebuilt in R8; the frozen package's numerical Poincare constant was not re-derived. A conditional argument may assume a uniform positive coercivity constant, but this review does not certify that number. |

### R13 — CONFIRMED: the nonlinear pure-gauge obstruction is compatible with STEP55's 1/38

Attachments: MINCB55.md:395–400 (`The naive perturbative route`), E3; STEP55.md:117–159 (`Setting`, `Lemma CERT`, `Theorem LC`), 198–238 (`LC-chart`). Claim status: PROVEN for the counterexample mechanism and linear certificate; CONDITIONAL for identifying the nonlinear critical value through the finite-volume germ/FLAT argument.

Use the four vertex gauges 1, exp(t*A), exp(t*B), 1 around a plaquette, with [A,B]!=0, and extend them periodically. Every group-valued plaquette is exactly identity. The sum of the four principal link logs is

`-t*A + log(exp(t*A)*exp(-t*B)) + t*B = -t^2*[A,B]/2 + O(t^3)`,

which is nonzero for sufficiently small t. For A=i*sigma_1, B=i*sigma_2 the leading term is t^2*i*sigma_3. The nonlinear normalized chain has zero global minimum at this flat datum; for fixed finite k,T its small analytic critical branch also has zero value by the repaired germ/FLAT argument. The linear energy is positive because dB!=0. Hence `E_cb >= (1-C*eta)*E_lin` fails for every positive prefactor in this neighborhood.

STEP's E_lin is instead the infimum of `||dB_0||^2/2 + sum_i kappa_i*||Q B_i-B_(i+1)||^2/2`, a function of Lie-algebra fields. Rebuild its certificate: dQ=Q_2d by discrete Stokes; row/column sums give ||Q_2||<=1 in d=4. On co-closed forms Q^T=Q_str^T and ||Q_str||<=1/L; d-star has norm at most 4. Telescoping `dB_(i+1)=Q_2*dB_i-d*r_i` and applying weighted Cauchy-Schwarz gives

`E_lin >= ||dB_k||^2 / [2+32*sum_(m=0)^(k-1) L^(-2m)/kappa_(k-1-m)]`.

At L=3,kappa=1 the exact constants are 1/34, 9/338, 81/3074 for k=1,2,3, and the uniform lower constant is **1/38**. The exact rational calculation reproduces them. This c_co is not an already-proved constant for the nonlinear curvature inequality. STEP's LC-chart explicitly retains an additive O(eta^2) curvature threshold and leaves coercivity for all chart fields unverified. Thus there is no contradiction.

The last `must therefore be proven with local gauge choices` in MINCB section 4.3 overstates the counterexample: it refutes this particular linear comparison, not every possible nonlinear proof without explicit local gauges. Treat local gauges as a proposed route, not a proved necessity.

### R14 — CONFIRMED in part: DENS's elementary properties; NOT-VERIFIED for the complete BFT4B bridge

Attachments: MINCB55.md:484–534 (`Proposition DENS`, `Verdict on the bridge`); HIST.md:1689–1697 (A5(B)–(D)), 1720–1735 (`(I_k^E)''`); SF.md:848–858 (`Replacement (L-loc)_k`); CODEX_REVIEW_BFT4B.md:68–79 and 128–140 (R4/R9). Claim status: CONDITIONAL for the elementary torus construction, ARGUED for first-derivative locality, OPEN for DENS-reg and the whole consumer transfer.

Re-derivation: assigning each positive chain summand exactly once gives a nonnegative density and a sum exactly equal to E_cb. Each summand is locally holomorphic on the small complex domain, and composition with the holomorphic critical chain is holomorphic. Finitely many terms suffice at fixed k,T. Corrected real per-cube bounds follow by counting terms as in R5 and summing the residual estimates: the leading soft series is geometric in L^(-2*sigma), whereas sigma=0 makes the chosen majorant grow with k. This establishes sufficiency of sigma>0 for this bound; it does not prove that the actual density must grow when sigma=0. Uniformity is for fixed sigma>0, not uniformly as sigma decreases to zero. For a constant over the datum ball, take eta and delta_rho at uniform upper bounds on that ball.

When a valid restricted-minimum theorem identifies all minimizers modulo composite gauge, each assigned term has the same value on that orbit: Wilson traces are conjugation invariant, and maximized soft terms are invariant under matching left/right endpoint actions. Thus no measurable choice within that orbit is needed. This statement requires the corrected RSM/GI/attainment conditions; it does not identify a free-boundary infimum on a different region.

A decomposition of the scalar total into signed connected polymers is not this assignment. Even the two-term transformation `(E_1,E_2) -> (E_1+H,E_2-H)` preserves a total while changing both pieces and potentially destroying positivity. Equality of totals therefore supplies no density identity. DENS correctly distinguishes these objects.

The derivative-locality gap remains real: differentiating a fine plaquette through a potential response of order L^(-k) gives the bad factor L^(4k)*L^(-2k)*L^(-k)=L^k. Gauge-invariant output response of order L^(-2k) would cancel it, but the nonlinear response estimates needed for every assigned term were not supplied here. Retain DENS(c) as ARGUED. DENS-reg(a)–(d) also does not, by itself, include SF's strictly supported polymer decomposition and all mixed-derivative/centered-norm bounds. Section 6.2(3) acknowledges this; the proposed replacement of the whole BFT4B bridge by DENS-reg alone must not silently delete that additional obligation. Real per-cube boundedness plus mere holomorphy is likewise not the stated uniform complex polymer norm without an additional bound on the complex domain.

### R15 — CONFIRMED within their stated finite scopes: mc55_1–3; none decides the main theorem

Attachments: MINCB55.md:539–568 (`Check record`), checks/mc55_1_criteria.md and mc55_1_levelsum.py, checks/mc55_2_criteria.md and mc55_2_tents.py, checks/mc55_3_criteria.md and mc55_3_lift.py. Claim status: PROVEN for the independently rebuilt arithmetic identities; CONDITIONAL/finite evidence only for the geometric sample checks.

| Check/gate | Actual verification in this review | Can it fail; what does it decide? |
|---|---|---|
| mc55_1 G1/G2 | An independent Fraction implementation compared the direct count-times-square sum against `4*(1-q^k)/(1-q)`, q=L^(-2*sigma), for L=3,5; sigma=1,1/2; k=1..200. Exact limits: 9/2,6,25/6,5. All comparisons and strict increases held. | Wrong exponent bookkeeping can fail. These are geometric-series identities for the assumed counts, not a test of those counts or BFT-1. |
| mc55_1 G4 | Algebraically `6*L^(4k)*(L^(-2k))^2=6` for every k. | An exponent mutation can fail; this cannot certify that the assigned cube has only 6*L^(4k) terms. R5 gives a countercount. |
| mc55_1 C1/C2 | Both give A_200=800. C1 first exceeds 400 at k=101; C2 first exceeds its bound 6 at k=2. | Controls discriminate loss of summability in the chosen majorant; the arbitrary finite 400 threshold is not a theorem about actual densities. |
| mc55_2 T1–T8 | The unmodified exact script was run and printed PASS for every gate, with the cubic control firing. Independently, differentiating sigma_5 gives -30*t^2*(1-t)^2, its derivative-square maximum is 100/3 at roots of 6*t^2-6*t+1, and the third derivative extrema are 60,30,60 in absolute value. Tensor products have at most 16 corners and corner l1 separation 4, giving 16*60*4=3840 for the specified derivative blend bound. | Partition alone is nondiscriminating between cubic/quintic; the cubic fails C2 gluing because its endpoint second derivative is 6. T7's grid does not prove interpolation by itself, but the exact partition polynomial and endpoint values do. T8 does not on its own prove every part of GI's scaled gauge norm. |
| mc55_3 L1–L4 | All five instances were rerun from the inspected script's functions, with only the floating-point epsilon reporting conversion removed in memory. Every L1–L4 flag was True; both controls fired on every instance. No disk script or output was modified. | Tree, ladder, contour and maximizer gates can fail. L1/L2 are useful structural checks. L4 uses a valid rational upper enclosure of the normalized-quaternion distance and conservative rational square-root bounds. This is d=3,N=2 sample evidence only. |
| mc55_3 loose L3 / control | An independent integer-exponent enumeration of the aligned abelian field found a maximum contour/path exponent difference of 4. One witness: X=(0,0,0), mu=0, face link at (2,0,0), contour order (0,1,2), start (0,2,0), contour exponent -6 versus path exponent -2. | For t=1/100000 the exact squared norm ratio is `16*(1-t^2)^2/(1+t^2)^3`, strictly between 15 and 16. Thus the reported rounded worst ratio 4 versus allowance 144 is correct in scope. Reducing 144 to, say, 10 would still pass this sample. The n_L-to-1 control does not validate 144 or the d=4 value 220; the proof in R9 does. |

The checks do not test GI's weighted-r/ nonlinear-rho distinction, chart attainment, the full-action gradient, or the lexicographic seam assignment. None is an unsatisfiable gate in the inspected implementation; no all-green result is used as a theorem verdict. Pre-registration timestamps/hashes were not independently authenticated. E12's correction of the archived timing stderr was noted, but the historical output files were not needed to assert the results of the fresh runs.

## Scope, symbols, and source-location record

Scientific reads used bounded ranges and locating searches in MINCB55, PROOF, FLOW, HIST, SF, PLD, NSL55, LCONV55, STEP55, ASSEMBLY55, CODEX_REVIEW_ASSEMBLY and CODEX_REVIEW_BFT4B, plus the three named mc55 criteria/scripts. The two supplementary procedural reads were SCIENCE_WORKFLOW.md and docs/ai_methodology/skills/review-loop/SKILL.md. The lane-wide search returned filenames only; it was discovery, not scientific verification of every hit. No snapshot, audit ledger, full PROOF read, git command, external lookup, or sub-agent was used. The only written file is this report; Python was run with -B and no test files were created.

Pinning results: MINCB's S_[j]=ker Lambda is not N5's ker h; R8 checks the transfer. Its gamma_min is the unsharpened N5 bound, so using it despite the available doubled gamma-sharp is conservative. STEP55's c_co=1/38 bounds a linear chain; it is not the unknown nonlinear BFT-coer constant. NSL's r is a linear residual and rho a nonlinear mismatch; their collision is R7. eta=C_0*||B|| is data-dependent, epsilon-prime_M is an output chart threshold, and epsilon_M must be compared to it explicitly (R3). HS versus operator norms need an explicit dictionary wherever E10 is invoked; this review uses the HS convention declared by MINCB/NSL and treats upstream alternative conventions conditionally.

Locations were re-found by strings. No literal numerical `PROOF.md l.N` citation occurs in MINCB's reviewed argument, so no invented PROOF line-drift finding is reported. The materially stale citation is to SF's superseded session-3 wall (R4). E8/E9 acknowledge internal reference fixes; they are not new discoveries in this review. E11 and all later errata were treated as overriding the earlier text. The initial heading/location scan preceded the focused E11 read; no derivation relied on the withdrawn UB.

Review completion checkpoint: 2026-10-29 06:52:23 UTC. The report structure was checked: PRE-STATED first, fifteen numbered findings, summary table, and bankable scope last. This structural check is not mathematical evidence.

## Summary table

| Item | Verdict | What can be concluded |
|---|---|---|
| R1 full-action margin from a Hessian perturbation bound | REFUTED | GAP without full-action criticality/recentering. |
| R2 E11 exact-lift multiplicity | CONFIRMED | PROVEN count L^(2k) in d=4; earlier coefficient 1 is REFUTED. |
| R3 exact chart/attainment radii | NOT-VERIFIED | GAP; explicit additional fixed-radius shrinkages suffice. |
| R4 M13 as a current SF obligation | REFUTED | Superseded source cannot discharge the live deep-chart route. |
| R5 lexicographic term counts | REFUTED for the literal periodic assignment | Counts 486->864 and 4->8 at d=4,L=3,k=1,T=3; the original C_dens is NOT-VERIFIED, not numerically disproved. |
| R6 gauge factor order | REFUTED | Correct the explicit gauge and RSM composition; orbit conclusions survive. |
| R7 invariant weighted residual in GI | REFUTED | r != rho; original transported-radius proof has a GAP. Uniform repair is CONDITIONAL on the stated residual remainder estimate. |
| R8 HL / GC / ANG | CONFIRMED in scope | HL PROVEN; GC/ANG CONDITIONAL on their explicit inputs. |
| R9 LIFT / main-term MARGIN | CONFIRMED in scope | Geometry PROVEN; main-term margin CONDITIONAL; E5 soft-residual extension remains ARGUED. |
| R10 corrected RSM and fixed-radius tower mechanism | CONFIRMED as a corrected implication | CONDITIONAL; requires R3/R7 repairs. No joint-convexity claim. |
| R11 FLAT / MIN-fin | CONFIRMED after named repairs | Zero-orbit geometry PROVEN; critical identification CONDITIONAL. Uniform MIN-cb OPEN. |
| R12 complete census / all consumer replacements | NOT-VERIFIED | GAP. Four inherited refutations are defensible only with the stated domain qualifications. |
| R13 pure-gauge obstruction / STEP55 1/38 | CONFIRMED | Nonlinear-to-linear multiplicative comparison fails; the linear certificate is valid. The claimed necessity of a particular local-gauge proof route is NOT-VERIFIED. |
| R14 DENS / full BFT4B bridge | CONFIRMED in part / NOT-VERIFIED as a bridge | Elementary torus properties CONDITIONAL; corrected counts available; first-derivative locality ARGUED; DENS-reg and full polymer/boundary interfaces OPEN. |
| R15 mc55_1–3 | CONFIRMED only in their finite/arithmetic scopes | Fresh exact checks reproduced; no gate certifies the missing theorem inputs. |

## Exactly what may be banked

1. **PROVEN:** Lemma CV's lower-bound transfer, the dimension-free HL lemma, the LIFT path-count mechanism (n_L=220 at d=4,L=3), E11's corrected L^(2k) lift multiplicity, and the elementary positive-assignment/sum identities. The exact rational controls and the counterexamples in R1/R5/R6/R7 are reproducible evidence at their stated scope.
2. **CONDITIONAL:** GC and the ANG slice transfer; the repaired GI/RSM mechanism, its main-term quadratic margin, and fixed-radius tower telescoping **with** the residual control and radius inclusions spelled out in R3/R7/R10. These do not certify the original unamended radius recipe, the frozen numerical c_1, or the actual consumer chart match.
3. **PROVEN/CONDITIONAL as separated in R11:** the corrected flat zero-orbit geometry, its critical-value identification under the repaired comparison, and the finite-k,T compactness/germ result. No uniform global MIN-cb is banked.
4. **CONDITIONAL:** positive holomorphic critical-chain densities on the global torus chart and a depth-uniform real per-cube bound with an explicitly fixed assignment and corrected counting. DENS(c) remains ARGUED. No identification with signed total-action polymers, free-boundary infima, or the complete centered polymer class is banked.
5. **PROVEN in its linear setting:** STEP55's dual-certificate coercivity with uniform constant 1/38 at L=3,kappa=1. The pure-gauge obstruction rules out the naive multiplicative nonlinear comparison. It does not settle nonlinear BFT-coer.

**Do not bank closure of ASSEMBLY work-list item 8 or of the BFT4B consumer bridge. The single most dangerous unverified item is the transfer from the repaired torus restricted critical-chain construction to the actual regional, centered-norm and boundary-controlled (I_k^E)'' / (L-loc)_k interface. DENS-reg(a)–(d) alone does not establish that whole interface.**

