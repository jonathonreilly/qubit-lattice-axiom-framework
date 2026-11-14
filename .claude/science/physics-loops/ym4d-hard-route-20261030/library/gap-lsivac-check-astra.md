## Repo search

Search terms: `LSI-vac|HC-vac|SG-step|gap-lsivac|Fisher.information contraction`: **no hits** on all five requested refs in `/Users/jonreilly/Projects/Physics`. Method terms: `hypercontract|log.Sobolev|Bakry.Emery|Gaussian domination|Fisher.information`, narrowed to `hypercontract|log.Sobolev|Bakry.Emery|Bobkov|Hopf.Lax`. Broad line searches reached their character caps and are discovery only. The narrowed filename search completed with 33 entries, below its cap of 100. Bounded source reads followed. A further targeted search located the existing ground-state transform.

| Ref | Revision searched |
|---|---|
| origin/main | `4d88da5504d356762deb6b1a1c2695336af9fb81` |
| pr/10114 | `f76f6c649cff7dffbab664d8976e680e8f287fe9` |
| pr/10133 | `89faef229ff6e6bde42baad15ed8270c2f4087d8` |
| pr/10134 | `1e70c7211a2cdbc39001e619f1dd89db45e25851` |
| pr/10141 | `c73ad7b177d94f89ff37b77386936e3d52b48b05` |

| Relevant hit, source range | Exact statement and proximity |
|---|---|
| `origin/main:research/mass-gap/library/gap-skeleton-max.md:190–196` | B11 asks for a defective LSI in the ground-state representation, uniform in spacing, plus uniform positivity improvement; its hypercontractivity literature statement is from memory. Prior route credit, not a quantitative vacuum-slice estimate. |
| `pr/10114` and `pr/10133`, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_CONSTRUCTION_ASTRA.md:170–215` | The ground-state transform is reversible for `psi_0^2 dU`; minorization gives `lambda/lambda_0 <= 1-exp(-2 beta n_s)`. Read the construction on pr/10114. This supplies the qualitative finite-box mixing used below; it explicitly separates the infinite-time vacuum from finite-torus laws. No new claim of inventing that construction. |
| Same two refs, `PLD.md:1167–1179` | Lemma AZ assumes a conditional kernel LSI and influence contraction rho; Herbst and martingale iteration give `P(Phi-E Phi >= r) <= exp[-r^2 kappa(1-rho^2)/(2 c_K C_I^2 g_k^2)]`. Both source passages read. Same concentration method, different soft blocking kernels; no (C1), (C2), or (FC) for this vacuum law. |
| `pr/10134:.claude/science/physics-loops/ym4d-hard-route-20261030/parts/upper-chain.md:1318–1323` | Conditional information between deep and far data does not bound the direct coupling between exteriors across a layer. Different conditional law and consumer; no supplier or refutation of Theorem C. |
| `origin/main:research/mass-gap/library/prior/gap-crux-lit-2.md:126` | The Rothaus review concerns improved Bakry–Emery hypercontractivity for a compact-manifold Laplacian; no Wilson product drift or volume bound is supplied. Literature locator only. |
| `origin/main:docs/HYBRID_GENERATORS_INTEGRATED_RATES_AND_CURVATURE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-15.md:100–119` (also hit on every PR ref) | Proposes `Gamma2>=k Gamma` for its hybrid generator and explicitly says it is not established. Different fixed-clock generator. |
| `origin/main:archive_unlanded/historic_intake_originals/branch01/124_BRIDGE_GAP_EXHAUSTED_ROUTES_CONSOLIDATION_NOTE_2026-05-06.md:121–146` (also hit on every PR ref) | Discusses LSI/BL for an SU(3) plaquette-moment bound at beta=6. Different measure and target; no vacuum-chain theorem is imported. |

Other filename hits are route/literature records and queue echoes, not evidence of an additional theorem. The November 8 digest was read in full: it concerns RG obligations and snapshot lineage, not this check. The current registry has no match for `lsivac|LSI-vac|HC-vac|gap-direction|FC.theta|gap-etohc`. FINISH assigns this exact check to row 943. Rows 944, 946 and 947 own later score/FC work; none is attacked here. No duplicate of this check was found.

The SA index was used first: README, chunk-02:90–108 and obligations:50–77. Searches for GL8, transfer, LSI, hypercontractivity, Fisher, Elitzur, mid-slice and Bakry locate the transfer frame, not these functional inequalities. Outline **2195–2238** proves the SU(2) convolution coefficient `2 exp(-beta) I_n(beta)/beta`; **2313–2360** constructs `L=G C^(1/2) exp(-V) C^(1/2) G` and states `Z_s=Tr L^s` (GL8). These source ranges were read. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. This proved frame is reused; no source claim about an uninspected account passage is made. No Balaban estimate is needed here.

Provenance: Codex, configured gpt-6-astra xhigh; checkout `585260a89b290bb4f9221100085ce680ff1ce42a`. Research-text check of row 941 for row 943; not an audit and grants no status. The target-specific prior digest is absent. Target SHA-256: `8a9e1ef879134c477de7af3be3f847344de2ab80c5d024527a96566a5b3dead6`. All target line numbers below refer to that file. Only this output is being edited. No computation can discharge a proof step.

Completed checkpoint: all 493 target lines read and covered below, with dependent source ranges checked. Core identities and entropy telescoping checked by hand. GUIDE scripts/logs are absent from the checkout; their run results remain unverified. No numerical job run. The unresolved quantitative SU(2) inputs remain with their existing owners. Next decision: adopt the corrected rate and model-matched test, not the literal FC failure/exact-equality claims.

## Findings saved during the check

1. **Theorem C and Theorem C0: HOLDS as conditional implications.** The entropy decomposition is exact. The score entropy bound gives `I(Pg) <= (sigma^2/alpha_c) I(g)`. Summing the entropy losses gives `alpha=alpha_c-sigma^2`; using (FC) directly gives `alpha=alpha_c(1-theta)`. None supplies either hypothesis on the SU(2) seed box.
2. **“U(1): fails as stated” for (FC), lines 433–434: FAILS.** On any finite positive-frequency Gaussian photon product, `theta=exp(-2 omega_min)<1` satisfies precisely the displayed (FC). What fails is the seed-sized rate, or a box-uniform separation of theta from one. The target at lines 418–421 must include that quantitative requirement if it is intended to reject this rival. The same distinction applies to SMALL-BOX.
3. **The GUIDE equality claim at lines 427 and 493: FAILS literally.** The printed plaquette table has `8.23e-4` versus `8.02e-4`, and `1.15e-3` versus `1.12e-3`. These are approximately 2.62% and 2.68% apart. Agreement within 3% is the reported observation; equality is not. It does not prove nonlinear (FC).
4. **The three curvature ceilings: HOLDS for the three named sufficient criteria.** They do not exclude every time-direction curvature argument, nor all sup-form suppliers (C1)/(C2). The latter use gauge-invariant tests under a one-neighbour vacuum conditional; ceiling (iii) uses an unrestricted coordinate test under the distinct two-neighbour law.

## Identities and conditional inequalities

**A1–A3, lines 80–105: HOLDS.** The transfer conventions agree with GL8 by the `AA*`, `A*A` construction, with `A=exp(-V/2) C^(1/2) G`. Here `G` is gauge averaging. Positivity and compactness give a unique positive normalized top eigenfunction; gauge covariance makes it invariant. Removing G leaves that top eigenfunction unchanged. Expanding `exp(beta<x,w>)` in symmetric tensor powers proves positive definiteness. Substitution of `m=exp(-V/2)Omega dx` gives both marginals of J as `Omega^2 dx`. Differentiating its normalized exponential conditional gives A2 and A3, including all normalizing terms. Beta is positive throughout the intended window.

The kernel P_0 is only **simultaneously** gauge invariant; it is not invariant in each argument. Its action equals the projected P on invariant functions. Keep that domain in subsequent statements. The identity for log Omega does not supply locality: m still contains the unknown Omega, and its covariance can couple distant links. “Replaces the nonlocality stop” is valid only as an exact reformulation.

**A4, lines 107–118: HOLDS.** For `F(s)=Lambda(theta_0+s Delta)`, subtracting lambda times the Taylor remainder at 1 from that at lambda leaves weights `(lambda-1)s` and `lambda-s`. Their integrals sum to `lambda(lambda-1)/2`. Thus the displayed Renyi bound has the right factor 1/2. The supremum must cover **all ambient theta**, including extrapolated chord points; values only at theta=beta x would not suffice. The chord/geodesic comparison gives RD with `sigma^2=beta^2 kbar`.

**A5, lines 120–125: HOLDS for SU(2), AFTER CORRECTION of “every group size.”** Haar right invariance gives each 4-by-4 diagonal block Id/4 and mean zero. Distinct positive-orientation bonds on side at least three have an endpoint not shared by the other. Its central sign kills each cross block. This proves exactly the displayed covariance and `kbar>=1/4`. The number 1/4 is specific to these SU(2) quaternion coordinates; U(1) gives Id/2. Pairwise zero covariance does not make the links independent. Replace “at y=0 the links are free” at line 213 by the Haar-marginal/zero-cross-covariance assertion.

**A6, lines 127–139: HOLDS.** Along the product-sphere geodesic, `x_l''=-|v_l|^2 x_l`. Consequently the Hessian of `-2 Lambda(beta x)` is `-2 beta^2 Var(<v,w>)+2 beta sum_l E<x_l,w_l>|v_l|^2`. Ricci contributes 2. The diagonal spatial contribution is `+beta sum_(p containing l) tr(x_p)/2`; mixed link derivatives are retained. In the proof sentence, the ambient radial derivative of V is **minus beta times** that plaquette sum. The displayed Hessian itself has the correct sign. For a free link, `beta Var(w_tan)=A(beta)` cancels the temporal mean term, leaving Ricci=2.

**A7, lines 141–149: HOLDS.** Completing the square in y gives a constant times `exp(-beta|x-w|^2/2)`, which equals a constant times `exp(beta<x,w>)` because both link vectors have squared length L. The y-density is `psi(y)^2`; differentiating twice gives `4 beta Id-8 beta^2 Cov`. Conditional independence proves `B*B=P_0`. On invariant functions this is P. No independence of the spatial links was used.

**Theorem MID, lines 200–216: HOLDS AFTER CORRECTION of its stated dependency list.** In addition to flat-space BGL it uses the explicitly recalled Bakry–Emery implication; neither is proved in this note. Conditional on those inputs, write `chi=chi_mid`. The entropy constant is `4 beta(1-chi)`, and A4 for `theta=2 beta y` gives score proxy `2 beta chi`. The Harnack/BGL proof thus gives B the exponent multiplier `G=(2-chi)/chi`. Duality gives B* the same multiplier, since `(p'-1)/(Q'-1)=G`. Composing gives multiplier G^2 and `alpha'=log G`. Apply this on invariant functions; equivariance suffices to keep `log B(g^p)` invariant. For noncompact y, bounded positive g makes this function bounded Lipschitz; the imported flat BGL version is the required one. The SU(2) hypothesis fails at beta>=2 because `chi>=beta/2`, irrespective of box size.

The Gaussian midpoint check is correct with the Gaussian kinetic diagonal retained. Completing the Gaussian joint square gives conditional precision `beta(e^omega+1)` and midpoint precision `4 beta tanh(omega/2)`. Thus `chi=2/(e^omega+1)`, `G=e^omega`. One cannot extend A7 to nonconstant |w| by simply dropping the Gaussian diagonal factors.

**Proposition W, lines 227–247: HOLDS.** Assume positive gamma_c and finite kbar_h. The invariant output has horizontal gradient, so scalar covariance Cauchy–Schwarz yields the stated pointwise energy inequality. Iteration and stationarity give `D(P^k f)<=kappa_W^(2k)D(f)`. The conditional-variance decomposition sums to `Var_nu f<=D(f)/[gamma_c(1-kappa_W^2)]`. The terminal variance vanishes by the existing finite-box positive-kernel minorization. An eigenfunction with nonzero eigenvalue is smooth; applying the energy bound to it gives `r^2<=kappa_W^2`. Zero eigenvalues require no division. This covers the invariant spectrum, not additional charged states of P_0.

**Theorem C, lines 249–260: HOLDS, with the corrected SGC endpoint.** For m=E_pi g, centered score phi and t>0, Gibbs' inequality gives

`E_pi[g phi] <= Ent_pi(g)/t + m t sigma^2/2`.

Apply both score signs and optimize t. For zero entropy take t down to zero; row 940's original “infinity” endpoint is wrong, as already corrected in row 942 (`gap-etohc-check-astra.md:43–45`). Thus `|grad Pg|^2/Pg <= 2 sigma^2 Ent_pi(g)`. Combining C1 gives `F(Pg)<= (sigma^2/alpha_c) P F(g)`. Exact conditional entropy decomposition and the geometric series give the printed LSI constant. Positivity, compactness and minorization justify the vanishing entropy remainder; positive regularization handles zeros. This checks the implication, not C1 or C2 for Wilson.

**Corollary C', lines 262–268: HOLDS AFTER CORRECTION of the abbreviated summaries.** Keep the explicit **all tangent directions** C2 assumption and the row-940 HC1/Harnack/BGL input, with SGC repaired. COV is an alternative only when it supplies its own all-field bound and corresponding proxy. Although P_0 lacks separate gauge invariance, HC1's proof applies to invariant g: `F=log P_0(g^p)` is invariant by equivariance. This proves the needed invariant norm bound. Equivalently, average the input over gauge transformations to obtain the projected operator bound. The resulting rate is `log(alpha_c/sigma^2)/2` when sigma>0 and alpha_c>sigma^2. If the score vanishes, P is constant on invariant functions; interpret separately.

The auxiliary full-function C1/Herbst statement HOLDS: for `f(w)=<z,w>`, `|grad f|<=1`; applying C1 to exp(tf) and integrating `(log E exp(tf))/t` bounds the centered log-mgf by `t^2/(2 alpha_c)`. Hence one **may choose** `sigma^2=beta^2/alpha_c`, and, if alpha_c>beta, obtain `alpha'>=log(alpha_c/beta)`. Horizontal-only C2 in the final summary is not the stated HC1 hypothesis. The parenthetical horizontal-geodesic extension is labelled ARGUED and is not used as a proved input here.

**Theorem C0 and variance analogue, lines 295–308: HOLDS.** Entropy losses telescope; (FC) bounds their Fisher terms by theta^k I(g), and the terminal entropy vanishes as above. For the variance analogue use the identical conditional-variance telescoping identity. Expanding `g=1+epsilon f` gives `I(g)=epsilon^2 D(f)+O(epsilon^3)` and `I(Pg)=epsilon^2 D(Pf)+O(epsilon^3)`, proving (GC) as a necessary consequence. The form inequality is on the invariant Sobolev domain. An eigenfunction then gives `r^2<=theta`.

**(W') and (C-av), lines 311–320: HOLDS AFTER CORRECTION of regularity and finiteness scope.** To use C(M), choose bounded continuous c; unspecified pointwise “constants” do not ensure that operator is defined on C(M). Alternatively use bounded Borel c on the sup-norm Banach space of bounded Borel functions. Positivity gives `||(cP)^n||=||(cP)^n 1||`, and the spectral-radius formula gives the printed trajectory expression and eigenvalue bound. For C-av let `a(x)=1/(2 alpha_c(x))` and `M_c` denote multiplication. Reversibility gives the exact adjoint calculation

`<a,P(M_c P)^k F>_nu = <(P M_c)^k P a,F>_nu`.

This proves the stated nonnegative series S. Pointwise convergence alone gives the weighted inequality, not a positive uniform LSI constant: require `sup S<infinity` for the latter. Positive measurable constants and Tonelli suffice for the weighted statement. No claim about rates for the actual SU(2) conditional laws follows.

**Gaussian domination, lines 322–331: HOLDS for both displayed inequalities; “annealed (C2) with proxy beta” needs correction.** The Fourier transform of the Gaussian is nonnegative, so the autocorrelation of its convolution with m is maximal at zero translation. Constant link norms convert this to the stated mgf of `beta<h,U_0-U_1>`. Its second derivative at zero gives `beta E(<h,U_0-U_1>^2)<=|h|^2`. Conditional variance minimizes squared prediction error, hence `beta E Var(<h,U_1>|U_0)<=|h|^2`. This is an **averaged covariance bound for fixed deterministic h**. It does not assert C2 for the centered conditional score, nor an adaptive horizontal direction h(x). The result-table phrase at line 471 must say that. The unneeded several-time parenthesis specifies no precise inequality and supplies no further theorem.

## Seed and fact tests

**Seed implication, lines 46–56 and 406–414: HOLDS conditionally.** The source of Proposition HC was read at `gap-direction-max.md:305–320`. With the gauge-projected kernel, HC applies to each invariant density `p_1(u,.)`; HOT gives `log sup p_1<=36 beta |B|`. Squaring its L^2 bound and integrating gives exactly `X(2m+2)<=72 beta |B| exp(-2 alpha' m)`. Take even a>=4 and m=(a-2)/2. The sufficient constant is

`C_beta(x_*)=log(72 beta 24^3/x_*)`.

For SH take `x_*=log(22/17)`; for the two stated W bounds take `x_*=log(20/19)`. These corrected scopes are already in the target. No odd-time interpolation is implicit. At beta=2.3 the first constant is below 16; at 2.6 it is about 16.12. For W at 2.3 it is about 17.61. For a hand-checkable strict 16 bound, `log(22/17)>0.2578` follows from `2(z+z^3/3)`, z=5/39. Also `e^4>sum_(j=0)^14 4^j/j!>54.59`, hence `e^16>8,880,000`. Their product exceeds `2,289,264>72(2.3)24^3=2,289,254.4`. Decimal approximations at other couplings are not substituted for the exact threshold.

**The actual residual must be quantitative.** The chain in Step 6 requires, on that same box,

`alpha_c(1-theta) >= beta^2 kbar [exp(2 K)-1]`,

where `K=[C_beta(x_*)+3 log a]/(a-2)`, `alpha_c>0`, `0<=theta<1`, and kbar is the COV supplier. This is just substitution in the printed arrows, not a new proof lane. `theta<1` alone does not meet the seed. The constants of C1, C2, C1-av, COV and FC may all depend on B. The sentence at line 291 that the box enters “only through Proposition HC” needs that qualification.

**Gaussian checks, lines 118, 138–139, 209–211, 271–274, 306–309, 413–414: HOLDS on the positive-frequency photon sector.** Let `r=e^(-omega)`, `A=2 beta sinh omega`, beta,omega>0. The conditional law is `w=r x+xi`, `Var(xi)=1/(beta e^omega)`, while `nu=N(0,A^(-1))`. Consequently

`alpha_c=gamma_c=beta e^omega`, `kbar=1/(beta e^omega)`, `sigma^2=beta e^(-omega)`, `kappa_W=r`, `theta=r^2`.

Theorem C gives A; C0 gives `beta e^omega(1-r^2)=A`; HC gives omega. There is no factor-of-two error. For an independent check of sharpness, use exponential densities `g_t(x)=exp(t x-t^2/(2A))`: `I(g_t)=t^2`, `I(Pg_t)=r^2 t^2`, `Ent(g_t)=t^2/(2A)`, and the entropy loss is `(1-r^2)t^2/(2A)`. The linear eigenfunction attains the variance bounds. Tensor products take the weakest positive frequency. These Gaussian statements do not include a compact zero mode without further analysis.

**FT-U1, lines 155–161, 309, 426 and 432–434: HOLDS AFTER CORRECTION of model and quantifiers.** The actual definition was read at `gap-seam-max.md:88–116`: FP is a specified Villain-without-monopoles mode model, with Gaussian transverse modes and three compact Polyakov modes. It is not the interacting compact Wilson U(1) law. For the photon sector,

`omega_min=2 asinh(sin(pi/(24a))) < pi/(12a) < 0.27/a`.

Thus `omega_min(a-2)<0.27` and `(16+3 log a)/0.27>1600/27>59` for admissible a. At a=2 the sufficient seed is impossible directly. This verifies the “above 59” arithmetic for the indicated seed-rate test. The full FP chain has the additional flux energy `1/(2 beta b)`; at b=24a its HC rate can be no larger, giving `alpha'(a-2)<1/(48 beta)<0.01` in the stated window. This compact **sector of FP** must not be relabelled the compact Wilson model, and full FP's optimal rate need not equal omega_min.

At each fixed finite photon box, theta=r^2<1. Hence the literal “(FC) fails” is false. Its separation from one vanishes with box size, and the displayed quantitative seed condition fails. In this restricted Gaussian sector, `alpha_c>=beta` and `kbar<=1/beta` stay adequate while that rate degenerates. This is the precise sense in which FC carries the rate loss. Nothing here proves the corresponding optimal constants for the compact Wilson U(1) model or its toron Fisher information.

**FT-FROZEN, lines 162–165 and 433–434: HOLDS with the stated fixed-box quantifiers.** The ordinary product-manifold gradient used here is unavailable for Q8 and 2T; a discrete Dirichlet form would be a different LSI. HC and its spectral consequence remain defined. Reuse the existing hand witness in `gap-crux-exercise2-check-astra.md:227–266`, also cited by `gap-glue-check-astra.md:403–423`: `(1,1,1)` and `(i,1,1)` give inequivalent centre-even flat classes. At fixed B the normalized transfer satisfies

`||T-P_flat||<=eta=(1+(|G|-1)e^(-beta d_G))^E-1+e^(-beta d_G) -> 0`,

with `d_Q8=1`, `d_2T=1/2`. Min-max gives `r_1>=(1-eta)/(1+eta)->1`, so E_1 tends to zero. HC implies `alpha'<=E_1` by linearizing its norm bound at 1. No beta-uniform positive HC rate survives on that fixed box. This says nothing about all box sizes at one chosen finite beta.

**SMALL-BOX, lines 166–171 and 434–435: HOLDS AFTER CORRECTION.** Its explicitly unproved premise is `E_1(B,beta)->0` at fixed B for actual Wilson SU(2). Given it, no beta-independent positive HC rate or fixed-a seed-sufficient rate can persist. If C' remains applicable with `alpha_c/sigma^2>1` throughout the limit, that ratio must approach one from above. If it falls below one, the criterion simply stops applying; convergence to one is not forced. Nor must every individual input degrade: a growing score proxy alone can make the HC rate small. Existence of a beta-dependent gradient LSI is not refuted. The deconfinement and “true seed near a=20” remarks are unverified GUIDE, not consequences of this premise.

**FT-CEIL, lines 172–174: HOLDS AFTER CORRECTION to the named operators.** The prior 1/3, 2/3, `4/(2+sqrt(10))` (about 0.775), and `4G_3` (reported about 1.0109) concern different specific curvature, single-link, vertex and slab criteria. Calling all of them bounds on one conditioning-slice supremum is too broad. As the target correctly says here, none of those cited ceilings refutes its COV, C1 or C2. The Green-integral decimal and the imported slab premise are not recomputed or promoted by this check.

**New method ceilings, lines 175–187: HOLDS for the named full-form criteria.**

| Criterion | Hand computation | Exact scope |
|---|---|---|
| Uniform positive Bakry–Emery tensor for nu | At one negative central link, four spatial plaquettes give -4 beta; the temporal mean contributes at most +2 beta and covariance contributes nonpositively. With Ricci=2, the tensor is at most 2-2 beta on the selected vector. | No such full tensor bound for beta>1. This is not a counterexample to an invariant LSI. |
| Global log-concavity of eta | At y=0, covariance Id/4 makes the Hessian `4 beta(1-beta/2) Id`. | Negative for beta>2; MID's strict chi<1 already fails at beta=2. |
| Both-neighbours unrestricted LSI constant greater than 2 beta | Antipodal neighbours cancel the field. Gauge invariance makes a link coordinate Haar, with variance 1/4 and energy 3/4; hence its Poincare and LSI constants are at most 3. | Impossible for beta>=3/2, relative to the recalled criterion. The coordinate is not gauge invariant. |

For U(1), replace Ricci=2 by 0 and the two coordinate moments by 1/2. The corresponding caps are 0, 1 and 1/2, as printed. All calculations are independent of box size, with side at least three. “Group-blind” means these analogous obstructions affect both specified groups; the constants differ. The broad conclusions at lines 218–221, 430 and 493 **FAIL**: three failed sufficient criteria do not exclude every time-direction curvature argument or every sup-form supplier. No new exclusion family is claimed here.

**One free SU(2) link, lines 275–283: HOLDS as an ambient rotor test, AFTER CORRECTION of domain wording.** Set V=0 and take the full S3 rotor (trivial gauge restriction); an isolated open bond with independent endpoint gauge transformations has only constant invariant functions. Rotational differentiation gives tangential variance `A(beta)/beta`, A=I2/I1. For a transverse coordinate y, `E y^2=A/beta`; its Rayleigh quotient is `3+beta I3/I2`. The recurrence `I1-I3=4 I2/beta` gives the W allowance `beta/A=4+beta I3/I2`, one larger. Thus the claimed comparison is valid.

At beta=2.3 the printed rounded Bessel data give `A` about 0.4793, `beta A` about 1.102, `3+beta I3/I2` about 3.799, and the two ratio bounds about 3.447 and 4.354. Hence “3.45 versus 4.36” is consistent at the rough precision intended. Rounding I2 before the next recurrence gives the quoted I3 about 0.3493; these decimals are not precision-certified values. The exact Bessel formulas carry the comparison. Small-beta ratios are `12/beta^2` and `16/beta^2` at leading order. The large-beta expansions `I2/I1=1-3/(2 beta)+O(beta^-2)` and `I3/I2=1-5/(2 beta)+O(beta^-2)` give `1+2/beta` versus `1+3/beta`, as printed. These are asymptotics, not finite-beta inequalities.

## GUIDE computations and proposed test

**Run provenance, lines 333–336 and 481–488: HOLDS AFTER CORRECTION to an unverified author report.** A filename search of the allowed checkout found none of `propw_guide`, `propw_av_guide`, `plaq_guide`, `plaq_r1_check`, or `gc_guide`, including their logs. The cited `/tmp/gap-lsivac-941/` files are not supplied checkout artifacts. This check did not search existing /tmp folders or another machine. It therefore cannot verify the 256/400/300-point runs, 60/80-character convergence, discretized derivative, numerical eigensolvers, predeclared criteria, wrong-coefficient discarded run, numeric lock, memory claim, or pass counts. No new numerical job was run. Their truth or falsity is not decided by their absence. The following checks cover the stated models and arithmetic recoverable from the text.

**Runs 1–2, lines 338–357: HOLDS AFTER CORRECTION to that scope.** All eight rows satisfy the displayed eigenvalue checks `r_1^2<=rho_c<=sup c`. Every PASS/EMPTY label agrees with whether the corresponding printed factor is below one: the sup factors below one are 0.0438, 0.3830 and 0.9229; the trajectory form additionally has 0.3244 and 0.1618. Neither printed table supplies the measured vacuum Poincare constant, so the separate gamma lower-bound test cannot be reconstructed. The free-circle model has Fourier multipliers `I_n(beta)/I_0(beta)`; commutation with its Laplacian gives `theta_GC=r_1^2` exactly. The displayed free-rotor values 0.0220, 0.1993, 0.5496 and 0.8747 are consistent with that formula to the quoted precision. The inhomogeneous spectral, conditional and trajectory constants remain unverified run values. “Non-convex-like” is not a mathematical hypothesis and those rows do not exclude every sup-form method.

**Run 3, lines 359–374: HOLDS for the character coefficient; HOLDS AFTER CORRECTION for the numerical report.** GL3 above supplies the single-link convolution eigenvalue `2 I_n(beta)/beta` after removal of its irrelevant exp(-beta) scalar. On a four-link loop each integration contributes that same eigenvalue to the character; hence the fourth power is correct. An extra division by n would indeed be an error. This is an open one-plaquette graph reduced to class functions, not a periodic three-dimensional seed slice.

| beta | Square and log arithmetic from printed r_1 | Relative excess of rho_c over printed r_1^2 |
|---|---|---|
| 1.0 | `0.00295^2=8.7025e-6`; 8.69e-6 is compatible with the rounding of r_1. `-log r_1` rounds to 5.83. | about 1.61% |
| 2.3 | `0.02832^2=8.020224e-4`; `-log r_1` rounds to 3.56. | about 5.24% |
| 2.6 | `0.03341^2=1.1162281e-3`; `-log r_1` rounds to 3.40. | about 5.36% |
| 4.0 | `0.03912^2=1.5303744e-3`; `-log r_1` rounds to 3.24. | about 5.23% |
| 8.0 | Same printed r_1 as at 2.6, hence the same square and rounded energy. | zero at printed precision |

The claimed “within 6 percent” agrees with the displayed numbers. Each row also has `r_1^2<=rho_c<=sup c`, with rho_c<1. This verifies arithmetic consistency, not the eigenvalues or the asserted agreement of two grids.

**Run 4, lines 386–402 and 437–441: HOLDS AFTER CORRECTION; the exact-equality summary FAILS.** There are thirteen listed cases: eight rotors and five plaquettes. Their printed numbers all obey `r_1^2<=theta_GC`. The two double-well values 9.535 and 1.055 exceed one; every other printed value is below one. In the free rotor, equality is an exact model identity as just noted. In the two nonuniform one-well rotor rows, the relative differences are about 1.09% and 0.19%. In the five plaquette rows they are about 0.92%, 2.62%, 2.68%, 1.31% and zero at printed precision. Thus “within a few percent” is the reported observation. “Equals” in Step 6 and the RESULT line is false as an exact numerical statement.

A computed grid value exceeding one tests its specified grid form. Without a specified derivative and a continuum error estimate, it is not a hand counterexample to the continuum (GC). Likewise theta_GC<1 tests only the **linearized** form, not nonlinear FC. A double-well label alone does not imply failure; the reported counterinstances have specific parameters. `2.3^(-1/2)` about 0.66 is correct arithmetic, but its interpretation as the actual interacting link displacement is heuristic.

**Other recalled numerical claims, lines 58–60 and 169–171: HOLDS AFTER CORRECTION to unverified GUIDE.** The glueball values 1.3 and 0.5, the deconfinement statement and the “true seed” estimate have no supplied data or error control here. Even using 1.3 as a hypothetical upper bound, a=20 gives `1.3(20-2)=23.4<16+3 log20`, so 20 is not a sufficient integer size under that estimate; a=22 passes that necessary comparison. Using 0.5, even a=60 passes the analogous necessary comparison, while 58 does not. These yield sides 528 and 1440, roughly the stated range. An energy upper bound makes these only necessary size comparisons: it gives no lower HC rate and establishes no seed.

**Proposed frozen-slice test, lines 442–455: FAILS as an unqualified test of the specified vacuum seed; HOLDS AFTER CORRECTION as a model-matched diagnostic.** The algebraic refutation criterion itself is right: on the same vacuum box, a smooth invariant f with `D(Pf)/D(f)>=1` contradicts every FC_theta with theta<1 by linearization. It does not refute LSI-vac, HC-vac, every use of the gradient form, or the conditional theorems above.

The sampling prescription needs two qualifications that affect the quantity measured:

1. On a finite periodic cylinder with N time slices, transfer disintegration gives

   `pi_(N,x)(dw)=T(x,w) T^(N-1)(w,x) dw / T^N(x,x)`.

   The one-slice marginal is proportional to `T^N(x,x)`, not Omega(x)^2. The vacuum conditional instead has `T(x,w)Omega(w)/(lambda_0 Omega(x))`. At finite N the additional backward transfer factor depends on x, so its derivative is absent from A3's score. The distinction applies also in the temporal-gauge representation. Freezing a slice and resampling the rest of a finite cylinder therefore does not directly measure the stated vacuum covariance or R(f). Supply a ground-state limit with controlled error, or explicitly label the measurement as a different finite-cylinder diagnostic. Also use the temporally transported links of A1, not raw links in an independently gauge-averaged next slice: a gauge sign at their endpoint makes their raw covariance with invariant f vanish. A3 belongs to pi_x for P_0, not to the raw separately gauge-projected coordinates.
2. A violation on a small box or an open one-cube graph refutes an assertion for that box/model. It does not refute an inequality only asserted on `(24a)^3` without a transfer between sizes and boundaries. No such transfer is supplied here. Even for the matching model, a GUIDE discrepancy needs a hand-checkable witness before the proof chain consumes it.

The claimed relation between `R(f)<1` and row 936's TYP-1 is a proposed analogy; no implication between their full quantified statements is written. The one-cube spectral reduction and the SU(2) test were explicitly not run.

**Spatial-locality conclusions, lines 376–384 and 430: FAILS as necessity claims; retain only as ARGUED heuristics.** A per-site probability much greater than 1/N does not alone imply that a typical N-site sample contains a pattern; highly correlated occurrences are an immediate reason. Nor does it identify the optimal whole-slice constants with the worst local ratio. No quantitative mixing or comparison premise is supplied. Even if a given trajectory bound becomes poor, that does not prove that every proof of FC must be local in space. The note's unknown Omega remains inside m throughout the exponential-family reformulation.

## Coverage and disposition

This covers all PROVED/CONDITIONAL entries in the source result table, their auxiliary claims and every printed fact-test/ GUIDE table. HOLDS always retains the exact stated model and named premises.

| Target lines / statement | Verdict |
|---|---|
| 46–56, 406–414: HC seed arithmetic and arrows | HOLDS conditionally, at even integer times, SH/W thresholds distinguished; HC inputs remain unsupplied |
| 84–105: A1–A3 | HOLDS; ambient kernel restricted to invariant functions when identified with P |
| 107–118: A4 and COV-to-RD | HOLDS; all ambient tilts required; HC use conditional on its imported lemmas |
| 120–125: A5 | HOLDS AFTER CORRECTION of the group-size wording; Id/4 is the SU(2) value |
| 127–149: A6–A7 | HOLDS for the displayed formulas; the radial-derivative proof sentence needs its minus-beta factor |
| 155–161, 309, 432–434: FT-U1 | HOLDS AFTER CORRECTION to the FP photon/compact-sector scopes; literal failure of finite-box FC FAILS |
| 162–165: frozen groups | HOLDS at fixed box as beta grows; no inference at one beta for every box |
| 166–174: SMALL-BOX, old ceilings | HOLDS AFTER CORRECTION to the conditional and criterion-specific scopes |
| 175–187, 195–198: three new ceilings | HOLDS for the three named unrestricted sufficient criteria |
| 200–216: MID and Gaussian test | HOLDS AFTER CORRECTION of its explicit Bakry–Emery/BGL dependencies; strict hypothesis fails in the target window |
| 218–221, 430, 493: exclusion of all time curvature/sup suppliers | FAILS |
| 227–247: C1/C2 consequences and Proposition W | HOLDS as implications |
| 249–260: Theorem C | HOLDS using corrected SGC |
| 262–268, 285–289, 468: C' and Herbst | HOLDS AFTER CORRECTION: preserve the full-tangent score hypothesis, positive constants and conditional HC input |
| 271–283: Gaussian and free-link tests | HOLDS AFTER CORRECTION of domain and decimal precision, as detailed above |
| 295–308: C0, variance version and GC linearization | HOLDS |
| 311–320: W', C-av | HOLDS AFTER CORRECTION of operator regularity and bounded-S requirement for a positive uniform LSI |
| 322–331, 471: Gaussian domination | Displayed mgf and averaged covariance HOLDS; identification with annealed C2 FAILS if read as that conditional sub-Gaussian hypothesis |
| 333–374, 386–402: GUIDE Runs 1–4 | HOLDS AFTER CORRECTION to arithmetic-consistent, unverified author reports; literal plaquette equality FAILS |
| 416–435: “smallest” FC residual | HOLDS AFTER CORRECTION to the quantitative seed-rate inequality above; theta<1 alone is insufficient |
| 442–455: refutation criterion and test proposal | Algebraic same-model criterion HOLDS; finite-cylinder/other-box substitution FAILS |
| 376–384, 430, 475, 493: necessary spatial locality | FAILS as a proved necessity; remains ARGUED |
| 476–477: SU(2) FC, companions, LSI/HC and seed remain OPEN | HOLDS as the conclusion about what this text has not proved |

The main useful implications survive. The first material seed-level failure is the FC quantifier at lines 416–434, not the entropy telescoping proof. Its repair adds the required rate; it does not provide that rate. The exact-equality, general-method-exclusion and direct finite-cylinder-test claims also fail as written. Neither the representation of Omega nor any GUIDE row closes the SU(2) input.

No target source, registry, FINISH, ledger or status file was changed. No numerical run, search outside the authorized source trees, audit, commit or push was performed. This output remains local at the requested lane path for its owner. The existing FC/score owners retain all proof tasks.

RESULT: HOLDS for A1–A4, the SU(2) A5 identity, A6–A7, the three named method ceilings, Proposition W, Theorems C and C0, and the displayed Gaussian-domination inequalities under their stated premises; HOLDS AFTER CORRECTION for MID/C', trajectory forms, fact-test scopes and GUIDE reporting; FAILS for the literal finite-box U(1) FC failure, plaquette equality, blanket method/locality exclusions and unqualified finite-cylinder refutation test. The SU(2) seed-box (LSI-vac)/(HC-vac), quantitative FC and its companions remain OPEN; no status is granted.
