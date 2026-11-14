## Repo search

Searched `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, `pr/10141`
in `/Users/jonreilly/Projects/Physics`, across Markdown and TeX, before deriving anything.
Terms: Fisher-information contraction, `(FC)`, `(GC)`, `LSI-br`, `LSI-J-seed`,
`HC-vac`, hypercontractivity, Brownian bridge, Polchinski, de Bruijn.
Broad searches hit unrelated information-geometry notes and the older mass-gap
method survey. They reached their output caps and establish no absence claim.
The narrower search `LSI.br|LSI.J.seed|FC.seed|HC.vac|Fisher.information contraction|Theorem BR[.: ]`
completed with **no hits** on those five refs.

Ref hashes, in the order above: `3e13676f02af206100abfb2875521904e8f53cda`,
`f76f6c649cff7dffbab664d8976e680e8f287fe9`,
`89faef229ff6e6bde42baad15ed8270c2f4087d8`,
`1e70c7211a2cdbc39001e619f1dd89db45e25851`,
`c73ad7b177d94f89ff37b77386936e3d52b48b05`.

Relevant method hits, read at their source:

| Ref and file | Exact statement and closeness |
|---|---|
| `origin/main:research/mass-gap/library/gap-skeleton-max.md:132–138` | B4 proposes a scale decomposition with lower renormalized-Hessian bounds and a finite integral of their exponential majorant. It labels the criterion recalled and its Wilson input CRUX. Related LSI method; no proof of BR or its seed input. |
| Same file, 190–196 | B11 asks for a defective logarithmic Sobolev inequality and uniform positivity improvement on a fixed physical torus. It explicitly leaves cutoff uniformity open. Related hypercontractivity proposal, not the finite-lattice bridge theorem. |
| `origin/main:docs/COMPACT_ROTOR_BRIDGE_CUBIC_BOUNDED_THEOREM_NOTE_2026-09-16.md:27–63` | Independent real Brownian bridges with covariance `g^2 G_T`, weighted by the cosine action, give proposed cubic derivative bounds for `T<1/sqrt(2)`. Different law and conclusion; no endpoint-vacuum LSI/HC implication. |

The full `prior/repo-search-2026-11-08.md` was read. Its actual targets are
PI/TPI/M3/GEOH/history and related existence inputs, not this contraction
statement. No additional "Repo prior work" line occurs in row 949.
Exact searches of `open-registry.md`, `open-core.md`, and `l17c.md` for
`gap-fc`, Fisher information, hypercontractivity, LSI-br/J, `(FC)`, `(GC)`
have no hits. This is the assigned check of row 947, not a new attack on its
open input or on rows 950/954.

Outline lookup: README, chunk rows and `obligations.md` searched for
hypercontractivity, Fisher information, log-Sobolev, GL8, ground state,
transfer matrix and Brownian bridge. The hit is chunk-02:90–108,164–175.
SA 2313–2373 defines `L=P C_E^(1/2)e^(-V)C_E^(1/2)P`, says it "is positive
and trace class", and derives `Z_s(0)=Tr L^s` (GL8). This supplies the
transfer frame, not BR. Credit: Ethan Sussman and Levent Alpoge, with Claude
and Codex as authors of their account; Gross's norm-differentiation method
and the repository's rows 931, 940, 941 supply the named antecedents.

Provenance: Codex, gpt-6-astra, xhigh; checkout
`c4fc1b80c49666d5f5dc749d91a98aed5cbc3769`; row 949. Research-text check,
not an audit; grants no scientific status. Target: `library/gap-fc-max.md`,
683 lines. The task-specific prior file is absent.

Source SHA-256: `890ecc8e4104d31cd30a753ef46c670159ebfcc7784128ba7cf869700c962189`.
Imported `guide/lane946/fct.py` SHA-256:
`b529bbb1962f4ba289cb6148f92ad0a4413a0a249a625b6916c5d22196e1263a`.

## Working checkpoint

Complete: repository/outline lookup; all statements and embedded code;
fact tests, arithmetic, and report readback. No numerical rerun.
Open obligations remain with their existing owners: the seed-sized SU(2)
LSI input and the endpoint regularity needed by the auxiliary COV-dir
argument. This check starts no further attack. The source remains unchanged.

Only this report is being edited. No numerical run can discharge an obligation.
Source assertions and GUIDE numbers are not accepted from summaries alone.

## First completed checks: definitions and rates

All line numbers below refer to the pinned `gap-fc-max.md` unless another
file is named. Verdicts concern the statement, not scientific standing.

| Statement | Verdict | Reason |
|---|---|---|
| Steps 1–3, definitions of `T_0`, `m`, `nu`, `pi_x`, (A3), (FC), (GC) | HOLDS | Row 941:79–106 supplies the exact unprojected chain. `P_0=P` only on gauge-invariant functions. Retain that restriction, `beta>0`, and spatial side at least 3. |
| (FC-seed), 4.1 | HOLDS | Substituting `alpha_vac=alpha_c(1-theta)` into `alpha_HC=(1/2)log(1+alpha_vac/(beta^2 kbar))` gives exactly the displayed inequality. Require `alpha_c>0`, `0<=theta<1`, and all three inputs on the same box. This is a sufficient condition, not a necessary characterization of the seed. |
| Necessary gap, 4.2 | HOLDS AFTER CORRECTION | An HC rate at least `K_a` forces `E_1>=K_a` and `24a E_1>=24a K_a>24 C_beta+72 log a`. Read "every route" as the route using this HC rate and Proposition HC's sufficient threshold. The seed alone does not imply this gap threshold. |
| Photon test, 4.3 and 5.5 | HOLDS | From FP's source mode list (`gap-seam-max.md:88–116`), `omega_min=2 asinh(sin(pi/(24a)))<pi/(12a)<0.27/a`. The three constants give `1-exp(-2 omega)>=exp(-2 omega)(exp(2K_a)-1)`, exactly `omega>=K_a`. FP passes finite-box FC and fails the seed rate. This is the photon sector, not compact Wilson U(1). |
| SMALL-BOX, 4.4 and 5.5 | HOLDS AFTER CORRECTION | Preserve row 941:166–170's unproved premise `E_1(B,beta)->0` at fixed lattice box. Then every HC-producing rate must tend to zero. Merely inserting `a` in a statement proves no such limit. The bound `(1/2)int alpha_s ds <= sup_s alpha_s/(2 beta)` is correct, and boundedness of that supremum is expressly unproved. |
| Frozen groups, 4.4 | HOLDS AFTER CORRECTION | The specified tangent-gradient FC and LSI-J forms are unavailable on finite Q8/2T; alternative discrete forms can be defined, but are not these definitions. HC and the ambient Gaussian bridge remain meaningful. No frozen-group bridge constant is computed here. The inherited fixed-box large-beta gap fact is supplied by the existing hand bound below; it says nothing about a fixed beta and growing boxes. |
| Entropy implication in 4.5, including EC-nec | HOLDS | For bounded positive densities the stated Jensen/entropy-duality proof gives `Ent(Kg)<=a Ent(g)/b`. Truncation extends it to finite entropy. HC and its dual compose to `P^(2m):L^a->L^b` with the displayed exponents. |
| "(FC)/(GC) are not necessary", marked PROVED in 4.5 and Result | FAILS as a hand-proof claim | The supplied witnesses are numerical grid eigenvalues from row 941. The note itself says the claimed non-necessity rests on GUIDE. No displayed hand-checkable counterexample establishes it for the smooth rotor or Wilson model. Repair: label the witness claim GUIDE, and retain the proved entropy necessity separately. The conditional BR theorem uses neither FC nor GC, but that logical fact alone does not prove non-implication. |

Seed scope: `x_*=log(22/17)` gives the SH seed used here. It does not give
both stricter numerical Form-W bounds; retain the correction in row 938
(`gap-direction-check-astra.md:113–132`). The exact `C_beta` is about
15.999 at beta 2.3 and 16.122 at 2.6. Decimals in 4.1–4.3 are rounded
descriptions, not exact thresholds.

The frozen fixed-box conclusion has an existing hand supplier, not just a
GUIDE witness. Read `gap-crux-exercise2-check-astra.md:227–266`: the flat
holonomies `(1,1,1)` and `(i,1,1)` give two distinct centre-even vectors.
For `E` links and `z=exp(-beta d_G)`,
`||T-P_flat|| <= eta=(1+(|G|-1)z)^E-1+z`, with `d_Q8=1`, `d_2T=1/2`.
Min-max gives `r_1>=(1-eta)/(1+eta)->1` at fixed E. This verifies the
inherited fixed-box fact test and requires no enumeration or rerun.

## Bridge theorem and auxiliary claims

| Statement | Verdict | Scope or correction |
|---|---|---|
| B1 | HOLDS | Since `\|x\|^2=\|w\|^2=L`, the heat kernel equals `kap exp(beta<x,w>)`; `Z=kap lambda_0` for `\|\|Omega\|\|_2=1`. Its endpoint law is exactly nu. |
| B2 | HOLDS | Positive smooth convolutions solve the heat equation. Fubini and the Gaussian semigroup give the stated normalization and reflection symmetry. |
| B3 | HOLDS | Completing the square gives conditional mean `(1-lambda)x+lambda w`, variance `lambda(1-lambda)/beta`, and endpoint joint law J. |
| B4–B5 | HOLDS | Constant endpoint radius removes the `\|w\|^2` term from each log-Laplace transform. Orthogonal simultaneous gauge transformations preserve m and the kernels. |
| Theorem BR, 5.2(i)–(v) | HOLDS | The interior LSI assumption implies the stated one-step norm bound, and iteration gives HC with rate `A/2`. This is an implication only. Read `alpha_s=0` as `alpha_s Ent(phi^2)<=2 E\|grad phi\|^2`, avoiding division by zero. |
| BR-gap | HOLDS | The conditional mean of a centred f remains centred under every bridge marginal. Its second moment has derivative equal to its gradient energy; PI and endpoint Jensen give the bound. Full-interval statements follow by increasing interior intervals. `E_1` is the gap on the gauge-invariant sector being tested. |
| BR-ent | HOLDS | Apply the proved entropy-duality inequality to BR's one-step exponents and let p increase to infinity. Bounded positive approximation covers finite-entropy densities. |
| BR-loss, 5.3 (ARGUED) | HOLDS AFTER CORRECTION | The forward relative-density entropy derivative and integrated entropy loss are correct. The endpoint Fisher energies in the bridge are ambient, however. At the terminal endpoint the intrinsic energy of Pg is only at most the ambient limit. Thus FC is not literally `I_S<=theta I_0` for that unprojected profile; this is a stronger sufficient condition. BR does not use this identification. |
| Gaussian check, 5.4 | HOLDS | `h_s` has precision `c/(1+cs)` and the bridge precision is their sum. Integrating gives `2 log(1+c/beta)=2 omega`. The midpoint precision is `4 beta tanh(omega/2)`. HC, gap and entropy exponents have the printed factors of two. Gaussian LSI is a named input, not newly discharged here. |
| Free-rotor asymptotic, 5.4 | HOLDS AFTER CORRECTION | The quoted asymptotic is a comparison, not a written proof of a uniform bridge PI. A first angular trial function needs regularization at the origin in R^2. Run 2 checks only its finite discretization. No SU(2) input follows. |
| Jumpable-double-well explanation, 5.5 | HOLDS AFTER CORRECTION | Gaussian smoothing at variance at least `2/(9 beta)` follows from B3. Well separation alone does not prove an order-one PI constant. The positive-rate assertion must remain ARGUED/GUIDE for the named cases. If a lower bound gamma on the middle third is supplied, `E_1>=gamma/(6 beta)` follows exactly. |
| All-functions covariance ceiling, 5.5 | HOLDS | The covariance computation and the bound `alpha_HC<=4/(beta+2)` hold for beta>=2. They do not cap BR restricted to invariant functions. The decimals 0.93 and 0.87 are approximate. |
| Non-log-concavity for beta>2, 5.5 | HOLDS | Row 941 proves only the midpoint instance. The calculation below extends it to every interior s; there is no need to assume this extension. It rules out a globally positive Euclidean Hessian bound, not every method for a non-convex LSI. |
| Lemma MS, 5.6 Stage 1 | HOLDS | Spectral calculus on the invariant mean-zero sector gives `P^(2n)(1-P^2)<=r_1^(2n)(1-P^2)`; A3 and P1-av give exactly the stated constant. The reading uses `E_1>0` and `kappa_W>0`; the zero case is immediate. No seed-sized power follows without estimates on these constants. |
| G(s) differential identity, 5.6 Stage 2 | HOLDS | The forward bridge generator and the Bochner identity give the displayed Hessian and conditional-variance terms, with exactly the printed signs. |
| COV-dir implies GC; "GC asks G to grow", same stage | HOLDS AFTER CORRECTION | Interior growth plus the endpoint controls below is sufficient. It is not an equivalent restatement of intrinsic GC: `G(0+)` includes normal components. The source omits the endpoint controls. Keep them explicit in this conditional implication. The scalar Gaussian test has no normal directions and is exact. |
| Lemma INV, 5.7 | HOLDS | On a periodic box of side>=3 distinct links have different unordered endpoint pairs. A central flip kills every linear term and every off-diagonal quadratic block. Independent endpoint actions give all SO(4) on a link, so a symmetric invariant diagonal block is scalar. |
| First nonlocal invariants occur in degree four, 5.7 | FAILS at the printed side>=3 scope | A length-three periodic winding loop on side 3 gives `Re(y_1 y_2 y_3)`, an invariant cubic. Replace this sentence by side>=4 (or restrict to contractible local loops). Lemma INV itself is unaffected; all seed boxes satisfy the stronger size condition. |
| Radial-quadratic/susceptibility relation, 5.7 | HOLDS AFTER CORRECTION | It is exact at fixed interior s, with the local Gaussian term displayed below. Uniformity as s approaches an endpoint is a separate assertion. It proves no susceptibility bound. |
| Relation to row 936, 5.8 | HOLDS AFTER CORRECTION | A centre cut flip preserves m and hence the bridge law. PI splits orthogonally into even and odd sectors. LSI/entropy does not split in that way. No transfer of RARE-P is actually proved, as the note says. |

Independent algebra check of BR. Put `S=1/beta`. The Gaussian bridge
transition has forward generator
`L_s=(1/2)Delta+grad log h_(S-s).grad`.
Its conditional terminal expectation satisfies `(partial_s+L_s)u_s=0`.
The diffusion chain rule gives, for a fixed smooth function F,

`d E[F(u_s)]/ds = (1/2) E[F''(u_s)|grad u_s|^2]`.

Taking `F(v)=v^q` and then allowing q to vary reproduces 5.2(ii) without
using its integration-by-parts cancellation. Dividing by `q E u^q`
and differentiating the exponent gives 5.2(iii). With
`q'=-alpha_s(q-1)` its derivative is nonnegative by LSI.
Both endpoint kernels are genuine conditional laws with the stated
marginals, so Jensen has the required direction. Iterating with
`p_k-1=exp(-A(m-k))` ends at 2. Bounded positive invariant functions are
dense after truncation and gauge averaging. Gaussian tails justify the
interior derivatives. First failing step in the **main BR proof: none**.

Covariance ceiling checked directly. Write `p=lambda(1-lambda)` and
`tau=E_J<x_l,w_l>`. Central flips kill distinct-link covariance blocks,
and SO(4) fixes each diagonal block. Also
`tau=sum_a <x_l^a,P_0 x_l^a>_nu>=0`, by positivity of P0. Thus
`v_s=(1-2p(1-tau))/4+p/beta`. For beta>=2, its minimum is at least
`1/8+1/(4 beta)`. Linearization of an all-functions LSI gives
`alpha_s<=1/v_s`; integration yields `4/(beta+2)`.

At zero field B4 instead gives

`Hess(-log nu_s)(0)=[1/s+1/(S-s)-(1/4)(1/s^2+1/(S-s)^2)] Id`.

Its sign is the sign of `p-(beta/4)(1-2p)`. Since `0<p<=1/4`, this is
negative for beta>2, for every interior s. The carried-over conclusion
therefore holds, though its cited midpoint formula alone did not prove it.

Endpoint correction for Stage 2. For smooth f, the needed statements are

`D_M(Pf)<=G(0+)`, and `G(S-)=D_M(f)`.

The first follows by orthogonally projecting the ambient derivative of
the explicit `(g_S*(f m))/(g_S*m)` extension onto each sphere's tangent space.
The second is an endpoint regularity assertion; it is not proved in the
source. One must supply it, or retain it as a named premise, before
integrating COV-dir to claim intrinsic GC. Interior integration gives
`G(S-)>=exp(int 2(1-k_s/(S-s))/(S-s) ds)G(0+)` under the stated
integrability conditions. With those endpoint premises it gives GC.
This correction concerns the auxiliary attempt, not BR's Jensen endpoints.

For completeness, the radial calculation uses `sigma^2=p/beta`,
`mu_l=(1-lambda)x_l+lambda w_l`, and `|mu_l|^2=1-2p+2p t_l`.
For `F(y)=sum_l c_l |y_l|^2`, conditional Gaussian variance gives

`Var(F)=4p^2 Var_J(sum_l c_l t_l)
         +sum_l c_l^2 [4 sigma^2 E|mu_l|^2+8 sigma^4]`,

`E|grad F|^2=4 sum_l c_l^2 [E|mu_l|^2+4 sigma^2]`.

This is the exact fixed-interior-time susceptibility comparison. Positivity
and Fourier diagonalization of the translation-invariant plaquette
covariance describe its zero and nonzero spatial momenta; no bound follows
from gauge invariance alone.

Why the entropy parity split fails: on two equally weighted points exchanged
by a flip, every pure even or pure odd function has constant square and
zero entropy. A mixed function `1+epsilon x` has positive square entropy.
Thus checking only the two parity subspaces cannot recover a general LSI.

## Two-slice replacement and seed test

| Statement | Verdict | Reason |
|---|---|---|
| Lemma J, 7.1 | HOLDS, conditional on Gaussian LSI | Entropy disintegration is exact. Conditional Gaussian LSI contributes `2 sigma^2 E\|grad phi\|^2`. Cauchy–Schwarz after differentiating `sqrt(E[phi^2\|x,w])` contributes the two squared coefficients `(1-lambda)^2` and `lambda^2`. Tangent projections can only reduce their norms. Simultaneous gauge invariance is preserved. |
| Variance version of Lemma J | HOLDS | Total variance, Gaussian PI, and the same derivative bound for the conditional mean give exactly the displayed inverse-constant sum. |
| Corollary BR-J and its two elementary lower bounds, 7.2 | HOLDS | Substitution `ds=d lambda/beta` gives the denominator `rho+(1-2rho)lambda(1-lambda)`. Its maximum is rho for rho>=1/2 and `(1+2rho)/4` for rho<=1/2. These yield both printed lower bounds. Full-interval passage uses interior BR bounds and monotone limits of their integrals. |
| Closed form and large-alpha asymptotic, 7.2 | HOLDS | With `t=2lambda-1`, integrate `4/(1+2rho-(1-2rho)t^2)` over t in [0,1]. This gives the artanh formula and `Xi/2=log(alpha_J/beta)+O(1)`. At rho=1/2, Xi=2 by the integral. |
| Gaussian comparisons and photon test, 7.2 | HOLDS AFTER CORRECTION of one decimal | The two-slice precision has smallest eigenvalue `c=beta(e^omega-1)`. For small omega, `Xi/2 ~ (pi/4)omega`, since the limiting integral is `int_0^1 d lambda/(1-2lambda(1-lambda))=pi/2`. At omega=3 the formula is about 2.962, which rounds to 2.96, not 2.97. The comparison with 3 is unaffected. The omega=0.5 lower bound and photon failure hold. |
| LSI-J implies LSI-vac with the same constant | HOLDS | Use Phi depending on x alone and invariant on that slice. The J marginal is nu and the w derivative vanishes. |
| Implication chain in 7.3 | HOLDS, conditional | If `K_a<=1` and `alpha_J>=2 beta K_a`, the two cases of BR-J both give HC rate at least K_a. This holds for a>=30 in the stated window and with the stated x*. No input constant for SU(2) is proved. |
| “Exact in every Gaussian mode”, 7.3/Result | HOLDS for BR; not for BR-J | BR uses the exact bridge constants and returns omega. BR-J uses a bound on those constants and is explicitly lossy, with small-omega ratio pi/4. Keep the subject of the exactness claim as BR. |
| General Poincare refutation criterion, 7.4 | HOLDS | Linearize LSI at `Phi=1+epsilon F`: `Var_J(F)<=D_J(F)/alpha_J`. One exact ratio above `1/(2 beta K_a)` on the same vacuum seed box contradicts LSI-J-seed. No converse follows from small ratios. |
| Time-like plaquette susceptibility inequality | HOLDS | `grad_x t=w-tx`, `grad_w t=x-tw`; their squared norms sum to `2(1-t^2)`. Translation and cubic symmetry give `Var(sum_l t_l)=L chi_t`. The displayed inequality and the monotone Xi cap follow. In a non-isotropic box use the averaged covariance row sum. |
| Bridge test using `U(F)=(1/2)int ds/R_s(F)` | HOLDS | Wherever the trial variance and energy are positive, linearized LSI gives `alpha_s<=1/R_s(F)`. Thus `U(F)<K_a` excludes LSI-br-seed. This requires the actual bridge laws for that seed box. |
| Final open status | HOLDS | FC/GC at the required rate, LSI-br-seed, LSI-J-seed, HC on the seed box and the seed remain unproved. Neither a Poincare probe nor BR's conditional implication supplies an LSI lower bound. |

The named Gaussian-LSI input in Lemma J remains a cited, unreconstructed
input in this lane. This check verifies the implication given that input;
it does not silently turn that citation into a discharged step.

## GUIDE computations: model, code and arithmetic only

All three embedded scripts were read in full. For their imported SU(2)
implementation I read `guide/lane946/fct.py:1–95,129–338`: graph construction,
plaquette orientation, link colouring, staples, conditional heat bath,
overrelaxation, transported slices, quaternion multiplication and tangent
loop gradients. The row-947 raw logs and arrays are not in this checkout;
their `/tmp/gap-fc-947/` paths name the author's other machine. I did not
read unrelated temporary folders or claim to have recovered those files.

No numerical rerun was made. The prescribed local `scripts/lab_ops.py`
numeric-lock entry point is absent from this sparse checkout. No lock or
convergence check was bypassed. The verdicts below distinguish checking
the printed computation from independently reproducing its output.

| Item | Verdict | What was checked |
|---|---|---|
| Branch decision from row 946 | HOLDS | The source report's E1–E4 uses open time; `fct.py` implements that geometry. Its box logs b1/b5 and published span results supply no refutation. There is no periodic return factor. A fixed-box spectral expansion permits an exponentially decaying boundary error, but gives no quantified error at K=6/8 or on a seed box. This reuses row 948's already assigned check rather than rerunning it. |
| Flat-chain script and its model | HOLDS AFTER CORRECTION to numerical scope | T is the symmetric quadrature of the stated Gaussian kinetic kernel, and m is `exp(-V/2)Omega`. The stiffness matrix is the nearest-neighbour finite-difference energy; its generalized eigenvalue approximates PI. Dropping small-density nodes, finite spatial truncation and a 40-node time quadrature all change the computed objects. The restricted P need not be exactly stochastic after masking. These are GUIDE approximations, not certified continuum constants. |
| Flat-chain table: nine rows, K1–K3 arithmetic | HOLDS for the printed data | Each displayed `r_1^2` is compatible with `exp(-2E_1)` and each displayed bridge exponential with `exp(-2E_BR)`. All nine satisfy K1. Exactly five listed theta_GC values exceed 1; their rate ratios are 0.846, 0.797, 0.820, 0.829, 0.790, all above 0.25. No original-output reproduction is claimed. |
| Two Gaussian calibrations | HOLDS | The code uses `V=beta kappa x^2/2`. At kappa=1, `r=(3-sqrt(5))/2`, so `r^2=(7-3sqrt(5))/2`, approximately 0.14590. At kappa=1/2, `cosh omega=5/4`, `exp omega=2`, so `r^2=1/4` exactly. Beta rescales the variance, not these ratios. This is a hand calibration. |
| Rotor script and polar energy | HOLDS AFTER CORRECTION to numerical scope | Mass weights `density*r dr dphi`, radial conductances `density*r dphi/dr`, and angular conductances `density*dr/(r dphi)` implement the stated polar Dirichlet form. Finite outer radius, density masks, 160x64 cells, 256 endpoint angles and 24 time nodes remain uncontrolled discretizations. No convergence study is supplied. |
| Rotor sign correction and K0 | HOLDS | With both coefficients present, positive V and negative V are different models. `u->u+pi` flips h1 alone; `u->u+pi/2` flips h2 when h1=0. The two positive-sign mixed cases have minima at cos(u)=-1/2. They cannot calibrate the negative-sign reference. The two corrected rows restore the printed matches. |
| Rotor table: ten distinct models, K1'/K3' | HOLDS for printed arithmetic | All ten satisfy the displayed inequality; the double-well ratios are 0.776 and 0.867. The free-rotor ratios 0.941, 0.923, 0.962, 0.998 have the stated approximate losses. These are numerical PI estimates, not LSI estimates or analytic refutations of GC. |
| “19 solvable chains; seven double wells where GC is false” | HOLDS AFTER CORRECTION | Nine flat plus ten rotor discretizations makes 19. Five flat plus two rotor GUIDE witnesses makes seven. Say “19 numerically diagonalized models” and “GC violations indicated by their discretizations”. The two Gaussian benchmarks alone have the exact calculations displayed. |
| Run 3 observable/gradient code | HOLDS | The three F columns are precisely the two spatial plaquette sums and transported time-like sum. Diagonal and cross Gram entries agree with their tangent derivatives. The f1/f2 cross gradient is zero since they read different slice variables. `eigh(C,Dm)` computes the largest ratio in this three-dimensional span. |
| Run 3 probability law | HOLDS AFTER CORRECTION of refutation language | On 2K+1 open slices, the central adjacent pair has density proportional to `(T_0^K b)(x) T_0(x,w) (T_0^(K-1)b)(w)`. It is not the symmetric vacuum J. No bound converts this run's ratios into vacuum ratios. “No threshold exceeded in this finite-cylinder probe” is the supported statement. |
| Run 3 error analysis | HOLDS AFTER CORRECTION | The script computes the stated leave-one-chain-out jackknife, over 16 or 8 chains. This measures sampling spread, not cold-start equilibration, finite-time bias, all-lag mixing, or vacuum approximation. Lag-one autocorrelation alone bounds none of those. A three-error criterion is a heuristic GUIDE rule, not a certified refutation. |
| Run 3 table arithmetic and caps | HOLDS AFTER CORRECTION | The printed susceptibility identity agrees: `0.1677/[2(1-0.4575)]` is about 0.1546; the other columns give about 0.1518 and 0.1108. Local t ratios give about 0.0844, 0.0848, 0.0673. Three-error maxima round to 0.167, 0.163, 0.115. Reciprocals of the estimated span maxima are about 6.5, 6.6, 9.0, producing the stated approximate Xi caps if they were exact vacuum ratios. They are estimates for J_K, not proved bounds on alpha_J. |
| Threshold arithmetic, 4.1, 7.3–7.4 and final RESULT | HOLDS AFTER CORRECTION | Use exact K_a in inequalities. At beta=2.3 the a=40,60,100,200 thresholds are approximately 0.305,0.446,0.715,1.350; 0.31,0.45,0.72,1.35 are rounded comparison values. At beta=2.6 the a=40 value is about 0.269. At a=30 they are about 0.232 and 0.205. Thus “every seed threshold (0.31 and more)” is false. All printed three-error maxima still lie below these comparison thresholds. |
| “Worst function is the time-like sum”; “no growth 4 to 6” | HOLDS AFTER CORRECTION | The largest estimated ratio is a linear combination in the three-span, slightly above f3 alone. f3 dominates that span. The two beta=2.3 box estimates show no statistically resolved growth in this probe, not a bound as the box grows. |
| One-plaquette companion, not run | HOLDS as a proposed comparison only | `r_1^2=8.02e-4` from row 941 corresponds to `E_1=-log(r_1^2)/2`, about 3.56. No J or bridge constant was computed for this companion. It supplies no additional calibration here. |

The exact finite-difference eigenvalues, raw Monte Carlo moments, elapsed
times, peak RSS and lock receipts of row 947 were **not independently
reproduced**. Its printed table arithmetic and the embedded code are what
the GUIDE verdicts cover. A search for lane947/br_guide/br_rotor/rj_guide
artifacts under this checkout's `library/guide/` found no saved raw record.

## Disposition

The main conditional result survives: BR gives HC from bridge marginal
LSIs with rate one half their integrated constants. BR-gap, BR-ent, Lemma
MS, Lemma INV, the conditional Lemma J/BR-J, and the susceptibility test
also survive in the scopes above. The proof of the seed-sized SU(2)
inequality is still absent.

Corrections that matter before reuse are: keep numerical non-necessity
claims at GUIDE; distinguish ambient and intrinsic endpoint gradients;
do not split entropy by parity; restrict the first-nonlocal-invariant
statement to side at least 4; and keep numerical laws, errors, thresholds
and caps attached to their actual discretized or finite-cylinder models.
The source file, registry, FINISH and scientific status records were not edited.

Only this report was written. It remains uncommitted and unpushed in the
requested lane; this session grants read-only access to the Git metadata.

RESULT: HOLDS for Theorem BR, BR-gap, BR-ent, Lemma MS, Lemma INV, and the conditional Lemma J/BR-J and susceptibility test; HOLDS AFTER CORRECTION for endpoint-gradient identifications, parity language, seed/model scopes and GUIDE arithmetic; FAILS for the PROVED non-necessity claim based only on GUIDE and for the degree-four-first assertion on side-3 tori. No seed-sized SU(2) FC, GC, bridge/two-slice LSI, seed or mass gap is proved or refuted. Research-text check only; no status granted.
