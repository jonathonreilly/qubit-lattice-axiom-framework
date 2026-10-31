# PRE-STATED

UTC: 2026-10-29 06:28:44. Written before reading or deriving the target's arguments.

Target: `SRC2_55.md`, with only the named supporting files and at most two additional files, read in located ranges. This is an independent hostile review of the mathematics, not an audit-status promotion. No git commands, source edits, numerical approximations, or long jobs are authorized by this review. The only written file is this deliverable.

Refutation criteria, declared in advance:

1. Exhibit a missing hypothesis or a counterexample to the chain `(Rep_m^C)+(Flow-pos) -> coarse-image bound -> (SP_lambda) -> (X1) -> (H_reg-sep)`, including its order-one case, domains, source radius, factorial growth, and claimed exponents. Recompute all exponent substitutions from the quantified statements.
2. Test whether the frozen/top split actually makes the frozen first derivative cancel under the specified centring, uniformly in the coarse field and scale. A coarse-dependent residual, scale-dependent constant, or an assumed conclusion in Lemma MB refutes the corresponding unconditional implication.
3. Distinguish the named inputs N1 and N2 from deductions; reconstruct any dependency used rather than accepting a status label. An undisclosed unmet input leaves the lattice application GAP/OPEN even if the conditional implication is sound.
4. Rebuild the exact Gaussian-chain covariance in Proposition NF, the harmonic-versus-arithmetic expansion in HOM, and the scalar source-flow estimate in FP. A mismatch of coefficient, quantifier, or counterexample class counts as a refutation of the matching claim only.
5. Inspect the six inherited refutations and the cited `sr2_55_1` checks. Identify gates that cannot fail, cannot pass, or measure a weaker property than the claim, including the preregistered C5 and the first firing order of C1.
6. Locate symbol definitions by filename and locating string before comparing them. Check cited line numbers against current text wherever those citations are examined. Record stale line references and stale input/output quantifiers separately from mathematical defects.

Verdicts are strictly CONFIRMED / NOT-VERIFIED / REFUTED; claim statuses are PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. CONFIRMED will mean the particular scoped assertion was independently reconstructed, not that Yang-Mills or an upstream input was proved. Findings will be appended incrementally, followed by a summary table and an exact statement of what may be banked.

## Review record

The methodology map `docs/ai_methodology/SCIENCE_WORKFLOW.md` was read before this declaration. The user's later scope overrides its git/landing workflows. No target derivation has yet been attempted.

### F1 — The frozen/top implication really supplies the missing singleton

**CONFIRMED. Claim: CONDITIONAL on all of (S0)-(S4), with fixed top offset.** Attachment: `SRC2_55.md:198-260`, locating strings `(SRC-rep_λ)`, `Theorem I`, and `T_f(V) − ν_m(T_f)`.

Write the logarithm as `C(z)+T(z,V)`. Its first derivative is the conditional mean, so global centring gives exactly `T'(0,V)-ν_m(T'(0,·))`. No frozen term survives. Source locality roots the derivative at one of at most `(2L^{j_0}+2)^4` top cells, and Cauchy costs `R_z^{-1}`. Thus the singleton constant really is `C_1=2A_t(2L^{j_0}+2)^4`. This uses the bound at **every** V, not merely almost every V or at the trivial background.

For a block of k>=2 distinct insertions, every contributing activity meets two supports a distance at least λ apart. A chain of k_cell four-dimensional cubes has diameter at most `2k_cell ell_r`, so its rooted sum costs `exp(-d λ/(2ell_r))`. Mixed Cauchy differentiation costs `R_z^{-k}` with no k!. The count `(2/ell_r+2)^4<=256ell_r^{-4}` and the geometric scale sum in SSUM give the stated `C_kappa λ^{-4} R_z^{-k}`. SSUM follows by splitting `t=τL^j` at j=0, bounding the negative-j tail by `L^4/(L^4-1)`, and splitting `t^4 exp(-dt/2)` into `t^4 exp(-dt/4)` times `exp(-dt/4)` on the other tail. Its maximum and geometric remainder reproduce the printed constant.

In each moment partition there are at most `floor(n/2)` nonsingleton blocks. Consequently the product costs at most `C_M^n R_z^{-n} λ^{-2n}`. Independently of the source's Bell recurrence, map each set partition to the permutation whose cycles are its blocks listed in increasing cyclic order; this injection proves `B_n<=n!` for every n. Averaging the entire conditional product then gives `(SP_λ)` with `(b,p,r)=(1,2+α,1)`. For the finitely many K<j_0, the displayed `24(2/a+1)^4<=1944L^{4j_0}` bound is valid. The theorem repairs the order-one defect; it does not assume that global centring makes conditional means zero.

### F2 — Lemma MB is an identity, not a bound or a locality theorem

**CONFIRMED for MB's stated induction; NOT-VERIFIED for its promotion to the full RG input. Claim: PROVEN identity; GAP in the proposed construction of N1.** Attachments: `SRC2_55.md:390-429`, strings `Lemma MB`, `This is exactly the per-step content`, and `The assembly from per-step data`; `SRC2_55.md:433-441`, string `It is not an extra assumption on the RG`.

Substituting the one-step density recursion into the assumed factorisation proves MB by induction. That calculation uses no polymer norm, coefficient locality, or cutoff-uniform estimate. In particular any zero-free recursion admits the formal choice `Delta_{k+1}=0` and `F_{k+1}=-log E[exp(-F_k)|V]`; MB then holds whether the remaining top term is bounded or grows with K. This is a diagnostic of the lemma's scope, not a counterexample to its identity.

The E4 obstruction is excluded by **(S1) together with (S4)**: moving its coarse-dependent `sum_r ell_r^{-4}` contribution to the top leaves a top norm of order `a^{-4}`. Freezing a scalar term does not remove that contribution. Thus the new representation bypasses LOC-e as a separately named assumption only by demanding a strong, uniform bound on the complete coarse-dependent remainder. MB alone has not derived that bound or shown that the RG produces the required local activities. N1 remains an analytic input, even when its bookkeeping is exact.

### F3 — Theorem II survives; its n-uniform source class does not establish N1

**CONFIRMED for the conditional implication. Claim: CONDITIONAL; N1 and N2 remain OPEN.** Attachments: `SRC2_55.md:291-343`, strings `Lemma SC`, `(Rep_m^𝒞)`, `(Flow-pos)`, `r_0 :=`; `SRC2_55.md:691-695`, string `E11 (remark on (R3), strict locality)`.

Disjoint supports give `|eta|<=zeta`. In four dimensions the displayed coordinate-derivative norm gives Euclidean Lipschitz constant at most `2zeta/lambda`; together with the sup bound this proves `|eta(x)-eta(y)|<=2zeta min(1,dist/lambda)`. Interpolating this bound gives `2zeta(ell/lambda)^alpha`; the four-corner half-sum doubles it, giving the required `4zeta(ell/lambda)^alpha`. Hence `epsilon_hat=-g_0^2 h_eta` obeys the two defining coefficient bounds on the entire n-variable polydisc for

`r_0=(1/2) min{rho_0/(2gamma^2), epsilon_hat_*/(4gamma^2), r_F}`.

This constant contains no n, and every segment `t z` stays in the same source class. R0 gives a nonvanishing ratio on that simply connected polydisc; R1 supplies its logarithm, R2 its normalisation and frozen independence, R4 holomorphy, and R5 the bounds. R3 really supplies S3: if a coefficient plaquette is contained in X, every corner through which a source enters lies in X. Set the unused level-zero frozen activities to zero. This proves Theorem II with fixed `K-m=j_0`, `c_SP=1`, `A_c=E`, `A_t=F`.

The small derivative inequality in SC's proof at `SRC2_55.md:298` is **REFUTED literally** under its coordinate-derivative norm: `||grad f||_Euclidean<=1/lambda` need not follow; the valid bound is `2/lambda`. A smooth small-amplitude, high-frequency sine in the sum of four coordinates, supported by a fixed cutoff, can have all four partial derivatives arbitrarily close to `1/lambda` at a point. Along the diagonal its derivative approaches `2/lambda`. The final SC constants already contain this factor 2, so neither r_0 nor the conditional theorem needs enlargement. The script's two-dimensional tents do not test this norm conversion, and its assertion that the proof is dimension-free is unsupported for that norm.

E11 explicitly leaves conversion of quasi-local dependence into R3's strict coefficient locality inside N1. I do not treat that unproved conversion as supplied by the notation of a polymer expansion.

### F4 — A smeared coupling-source estimate does not give the point-insertion estimate used in §5.4

**REFUTED as an implication from `(SRC-rep_λ)` alone. Claim: GAP for the pointwise coupling-type W1/W3 extension; the H_reg implication is unaffected.** Attachments: `SRC2_55.md:519-524`, string `smeared`; `SRC2_55.md:543-553`, particularly `inf_csup_V|E[J(x)|V] − c| ≤ B_JL^{d_Jj_0}` and `for coupling-type J from (SRC-rep_λ) alone`.

Exact countermodel to that asserted implication: fix two lattice sites `x_0,y_0` a positive physical distance apart, let the coarse variable Y be a fair sign, and set

`e_a(x)=a^{-4}(1+Y)(1_{x=x_0}+1_{x=y_0})`, with `m=K`, `j_0=0`.

Conditioned on Y the field is deterministic. Its conditional log is

`Phi(eta;Y)=(1+Y)(eta(x_0)+eta(y_0))`.

Use no frozen activities and one top singleton-cell activity for each of the two sites (assign a boundary site to one containing cell). These activities are entire, zero at zero source, strictly source-local, and bounded by `4r_0` in total for every admissible normalised source family: at each site at most one source is nonzero, and `lambda^alpha<=1`. Their rooted exponentially weighted norm is bounded uniformly in a, n and the torus size. Thus every S0-S4 clause holds with fixed constants. The nonnegative field also obeys the crude `24a^{-4}` envelope.

Nevertheless

`E[e_a(x_0)|Y]-omega(e_a(x_0))=a^{-4}Y`, and `inf_c sup_Y |E[e_a(x_0)|Y]-c|=a^{-4}`.

Choose a smooth f supported near y_0 with `f(y_0)=1` and zero near x_0. Then `Õ(f)=Y` and `||E[Õ(f)|Y]-omega(Õ(f))||_2=1`. The point-image factor invoked in §5.4 therefore has **a^{-4}**, not a cutoff-uniform constant, even at fixed positive separation from supp f. All smeared conclusions of Theorem I still hold.

Correction: §5.2's extension covers **smeared** plane-energy insertions. The displayed pointwise use of Proposition MX requires `(Rep^e)`/canonical image scaling for point energy insertions too, or a separate proof of the needed integrated bound. The countermodel refutes the displayed point bound and the claimed inference through it; it does not refute every possible direct integrated W1/W3 estimate. In particular its single-site factor is compensated by a^4 when summed, so I do not claim that this model makes the integrated quantity diverge.

### F5 — The stated SP/X1/H_reg exponents and the torus boundary repair survive

**CONFIRMED. Claim: CONDITIONAL, not an unconditional Yang-Mills construction.** Attachments: `SRC2_55.md:261-270`, strings `BRIDGE (i) gives`, `Codex F11's boundary point`; `OSLEAF55.md:830-852`, `Lemma TP`; `OSLEAF55.md:406-440`, `Theorem EXT`; `CODEX_REVIEW_OSLEAF.md:135-155`, F10/F11.

An independent reconstruction of the losses: localising at `mu=lambda/16` produces at most `(35/lambda)^{4n}` centre tuples. Fourier integration by parts to order `(r+4)n+2` beats the `4n`-dimensional frequency sum after the r-derivative factor costs. The squared factorial in the coefficient bound contributes `(n!)^{2r+8}` up to `C^n`, and the factor `n^{rn/2}` contributes `(n!)^{r/2}`. Thus TP adds `4` to the separation exponent, `6` to the derivative slope, and `5r/2+8` to the factorial exponent. At `(b,p,r)=(1,2+alpha,1)` this is

`p_X=6+alpha`, `r_X=7`, `b_X=1+5/2+8=23/2`, `c_*=4`.

The EXT shell/cube differentiation cost is `n^{2r_X n}((r_X n)!)^5`, hence at most `C^n(n!)^{7r_X}`. Its flat-test Taylor remainder supplies the summable positive power of lambda; the sub-lattice part instead uses `q_X=4`. Absorbing `C^n` in one more factorial gives

`beta=23/2+7*7+1=123/2`, and `s=ceil(max(7+(6+alpha)+7,4+6))=ceil(20+alpha)=21` for **every** `0<alpha<1`.

This is a proof for the interval, not merely the three alpha samples in G5. The derivative and Taylor orders must be rounded upward as in the existing OSLEAF review. FLOW normalisation is consistent: `u=1/g_FLOW^2=2N/g_std^2`, hence `g_std=sqrt(2N)g_FLOW` and `Z=1` gives `q_X=4`.

The boundary repair also works. Each enlarged TP factor stays within `6mu<=3/8` of a point in `B_{R/4}`. Besides injectivity of the chosen chart, one must check torus separation: a coordinate difference that wraps is at most `R/2+3/4`, so its wrapped distance is at least `R/2-3/4>=61/4` when R>=32. Otherwise the Euclidean distance is unchanged. Either case preserves the needed separation `lambda/4<=1/4`. The factors fit in side-2 cubes anywhere on the torus, exactly the enlarged SP domain. The all-X1-cube statement therefore survives this review.

### F6 — NF is a valid Gaussian example, but not a matched refutation of the named Yang-Mills package

**CONFIRMED for the Gaussian identities and the failure of bounded multipliers alone; REFUTED for the assertion that this model meets refutation criterion R6 for `(I1)+banked+LF`. The latter implication remains NOT-VERIFIED, not disproved by this model.** Attachments: `SRC2_55.md:443-461`, `Proposition NF` and `This is a counterexample (refutation criterion R6)`; `SRC2_55.md:628`, V10.

Conditionally independent branch noises have zero cross-covariance. The common terminal variable therefore gives exactly

`Cov(Y_0,Y'_0)=(product_{i=1}^K (1+1/i))^2=(K+1)^2`.

This is `(1+log_L(1/a))^2` at `a=L^{-K}`. For the summable comparison, no infinite-product citation or finite K scan is needed: for i>=2,

`i^2/(i^2-1) - (1+1/i^2)=1/[i^2(i^2-1)]>0`.

Telescoping gives `product_{i=1}^K(1+1/i^2)<=4K/(K+1)<4`, hence covariance <16 for every K. Those claims may be banked for the abstract chain.

But uniform conditional variance and `1<mu_j<=2` are not all the named premises. In this chain `E[Y_j|Y_{j+1}=v]=mu_j v` is unbounded over v even in one step; the top variable is an unbounded Gaussian, not a compact coarse configuration with the asserted all-V source bound. No construction of the coefficient class A, the source-local activities, the prescribed Wilson energy observable, or the stated large-field input is supplied. If the LF input is read literally as `(R0)-(R5)` at every V, it already contains the bound that excludes this example. Thus NF demonstrates a **weaker** non-implication: bounded per-step multipliers do not bound their product. It does not prove that Flow-pos is logically necessary among all possible repairs, or furnish a counterexample satisfying the full original input package. V10's matching-premises refutation must not be banked.

### F7 — N1's advertised per-step origin omits a source-locality proof and quotes a stale decay rate

**REFUTED for the claim that the displayed CX hypotheses by themselves supply the asserted local-parameter content; NOT-VERIFIED for the full N1 construction. Claim: GAP.** Attachments: `SRC2_55.md:402-429`, `This is exactly the per-step content (i)`; `STEP55.md:483-512`, `Theorem CX`; `STEP55.md:679-685`, errata S8/S9; `SRC2_55.md:691-695`, E11.

CX's H2 says that `V_X` reads the **fluctuation A** only in X and is holomorphic in `(bg,V,epsilon_hat)`. It does not say that it reads those **parameters** only in X. H1's displayed locality clause likewise concerns W. This distinction matters for R3, which is locality in the original coefficient field after backgrounds/localised couplings have been substituted.

A direct diagnostic for that missing hypothesis: leave an H1-satisfying covariance and product reference measure unchanged, and take one A-independent interaction on a fixed box X at x, `V_X=t epsilon_x epsilon_y`, with a remote coefficient parameter at y, `|epsilon_x|,|epsilon_y|<=1`, and arbitrarily small nonzero rational t. It is local in A (vacuously), bounded and holomorphic as H2 requires. An A-independent term changes no covariance Hessian; choose t below the fixed H2/H4 size threshold. The integral is exactly `exp(-t epsilon_x epsilon_y)`. Its log has a mixed x/y coefficient derivative `-t` independent of distance. Uniform source-local polymer decay with a summable rooted rate would force that derivative to decay with the distance between x and y, since a contributing polymer must contain both coefficient sites. No such decay follows from the written hypotheses. This challenges the abstract hypothesis-to-source-locality inference, not the local form of an actually constructed Wilson interaction.

E11 correctly places re-localisation inside the **open** input N1. It prevents treating strict locality as an unnoticed premise, but does not supply the missing construction. One must keep the original coefficient dependence of the background, the Gaussian determinant/main-term contribution, and the returned activities in that construction; CX's displayed integral of the interaction alone is not the whole density ratio in MB. STEP55's own S9 explicitly restores the missing main-term and determinant factors in its returned-density formula.

There is also a concrete stale-rate citation. SRC2 quotes the rate `kappa_2-3kappa_CE-3`; STEP55's S8 instructs readers to replace `kappa_2` by `kappa_2/c_fat` throughout CX. The corrected exponent is

`kappa_2/c_fat - 3kappa_CE - 3`,

and its positivity requires `kappa_2>c_fat(3kappa_CE+3)`, before any further entropy loss in converting to a rooted norm. The old positivity threshold cannot be reused after fattening. This correction does not change the downstream exponents when a positive rooted rate d is separately assumed in N1.

Finally, `(LF-src)` is defined at `SRC2_55.md:423-425,578` as **all R0-R5 at every V**, i.e. the full representation property at issue. With that literal reading, `CX + I6^C + LF-src => N1` does not independently reduce N1: its last premise already contains it. A useful smaller large-field obligation would have to state the extension/return estimates without assuming the complete conclusion. Conditional use of N1 itself is legitimate; the claimed derivation from smaller inputs is not yet verified.

### F8 — Scalar FP closes with the printed constants; the vector flow is still open

**CONFIRMED in the scalar model, with the uniform-constant convention below. NOT-VERIFIED for the plane-dependent Yang-Mills flow. Claim: CONDITIONAL; vector extension ARGUED.** Attachments: `SRC2_55.md:345-387`, `Proposition FP`, Steps 1-5, `vector version`; `SRCAN55.md:319-335`, `Lemma SA-F`.

Reconstruction: scalar Cauchy on the half-relative disc gives `|c_loc'|<=2C_b g_j^4/r_rel=q_j`. An averaging operator with nonnegative rows summing to one contracts the sup norm; translation covariance contracts the physical Lipschitz seminorm. The size bound on c_gr then gives precisely

`D_{j+1}<=(1+q_j)D_j+C_g g_j^2 omega_j^2`,

`G_{j+1}<=G_j(1+q_j+2C_g d_B^2 gamma^2 G_j ell_{j+1})`.

The second estimate uses `|y_1-y_2|>=ell_{j+1}` and does not silently assume differentiability of c_gr. On fine levels, summing `ell_{j+1}<=lambda L/(L-1)` closes `G_j<=8e^Q zeta/lambda` using the **second** entry in r_F. The fine-level contribution to `C_g sum g_j^2 omega_j^2` is bounded by

`64C_g d_B^2 gamma^2 e^{2Q} zeta^2 L^2/(L^2-1)<=zeta`,

using its **third** entry. On coarse levels there are at most `1+log_L(1/lambda)` terms, and the `D_j<=6e^Q zeta` bootstrap makes their contribution at most

`144C_g gamma^2 e^{2Q} zeta^2(1+log_L(1/lambda))<=zeta`,

using its **fourth** entry and `lambda^alpha(1+log_L(1/lambda))<=C_alpha`. Therefore `D_{j+1}<=4e^Q zeta`, strictly inside the `6e^Q zeta` bootstrap. The **first** entry ensures the half-disc condition for every step. No factor depending on n or K was lost.

Quantifier check: if `A=u_K-R_F` changes with the chosen cutoff/tuned terminal coupling, do not treat its evaluated r_F as a fixed input. A single valid radius is obtained by evaluating the same four entries at

`A_*=gamma^{-2}`, `Q_*=(2C_b/r_rel)(gamma^4+gamma^2/B)`.

The supplied trajectory lower bound gives `A>=A_*` and `Q<=Q_*`; every entry is then no smaller than this fixed choice. This proves a uniform positive lower choice without a stale minimum. It assumes fixed positive `B, gamma, C_b, C_g, d_B, r_rel, alpha, L`, as the conditional model does.

FP has only one scalar field and one scalar local holomorphic function. No norm control for mixing plane components or their marginal anisotropies follows from those hypotheses. The source correctly leaves that extension ARGUED; it cannot discharge N2 for the plane-dependent RG.

### F9 — HOM's coefficient and relative-polydisc obstruction are exact; keep its model scope

**CONFIRMED for the stated constrained abelian model and for an abelian anisotropy mechanism. NOT-VERIFIED as a Yang-Mills flow theorem. Claim: PROVEN model identities; GAP for the actual flow.** Attachment: `SRC2_55.md:489-510`, `Proposition HOM`.

For positive coefficients c_p, write `F_p=Phi/(c_p S)+h_p`, where `S=sum_p1/c_p` and `sum h_p=0`. Completing the square gives

`(1/2)sum c_p F_p^2=Phi^2/(2S)+(1/2)sum c_p h_p^2`.

Thus the minimiser and `c_eff=S^{-1}` are exact, and every nonzero feasible perturbation strictly raises the energy. For two coefficients `u(1+epsilon)` and two `u(1-epsilon)`, `S=4/[u(1-epsilon^2)]`. Therefore the remainder relative to the arithmetic block coefficient is exactly **`-(u/4)epsilon^2`**. The rational identity continues to complex parameters away from its poles; no minimisation order is claimed for complex energies. At `u=1000, epsilon=1/4, C_b=1000` its modulus is `125/8>1`. On a fixed relative disc its size grows like u, whereas the scalar SA-F hypothesis asks for `C_b/u`. The quoted threshold `u^2>4C_b/r_rel^2` is correct. For an actual source with `epsilon=O(zeta/u)`, the remainder is instead `O(zeta^2/u)`, consistent with FP3.

The printed d=2 example has only one plaquette orientation, so it alone does not demonstrate plane anisotropy. The qualitative warning has an elementary independent abelian derivation: let c alternate between two slabs normal to x_1. A closed two-form in the 12 plane may vary with x_1 and minimises at `c F_12=constant`, giving the harmonic coefficient `u(1-epsilon^2)`. For the 23 plane, closure and periodicity fix its transverse-plane average separately at each x_1; convexity makes the minimiser constant in that plane, giving the arithmetic coefficient u. Thus the two orientations already differ at order epsilon^2 in an abelian laminate. This verifies a possible anisotropy mechanism, not the claimed unconstructed plane-dependent Yang-Mills recursion or its uniform bounds.

### F10 — The root-local alternative needs no Peierls assumption

**CONFIRMED for the sufficient bound and the redundancy of SRC-I in this particular statement. Claim: PROVEN simplification of the conditional input.** Attachments: `SRC2_55.md:473-487`, `Corollary LF-loc`; `SRC2_55.md:645-648`, E5; `SRC2_55.md:592`, `only LOCAL Peierls moments`.

The neighbourhood has deterministic cardinality `|N(c)|<=N_N`. Consequently

`exp(C_LF |L(V) intersect N(c)|)<=exp(C_LF N_N)`

for **every** V and every probability law of the bad set. This uniformly bounds the rooted sum at each fixed V by `A_t exp(C_LF N_N)`. There is an essential norm-order distinction: the LF statement takes the V supremum **after** the polymer sum, whereas S4 takes it inside each activity norm. The LF statement is therefore not literally S4. Nevertheless F1's argument can be run at each fixed V, using Cauchy in z before the rooted sum and taking the V supremum last; it gives the same uniform conditional moment bounds. A sufficient multiplier on A_SP is just **`exp(C_LF N_N)`**, with no SRC-I hypothesis. The larger multiplier in E5 is valid but unnecessary; I am not refuting a valid generous upper bound.

This assumption supplies no new probabilistic large-field control: its finite neighbourhood makes all its moments deterministically bounded. Peierls estimates matter for neighbourhoods or paths of unbounded size, which are precisely the case this statement excludes. Thus it should not be counted as discharging an all-order path-envelope problem or as needing the separate open SRC-I input.

### F11 — sr2_55_1 reproduces, but C5 is a weak and misdescribed control

**CONFIRMED for the actual execution and its limited arithmetic/model scope. REFUTED for the quoted C5 firing description and the criteria's first-failure expectation for C1. Claim: PROVEN finite checks; no certification of N1/N2.** Attachments: `checks/sr2_55_1_criteria.md`, strings `Control C1`, `Control C5`, `What this check can and cannot decide`; `checks/sr2_55_1_consts.py:51-79,207-228,274-279`; `SRC2_55.md:596-614`.

After reading the entire 279-line script in bounded ranges, I executed it directly with `python3 -I -B`, with stdout returned to the tool and no redirection or file creation. Exit status was 0. It printed **9/9 gates, 7/7 controls, VERDICT: PASS**, matching the saved output; the saved error file was empty. This is execution evidence for those checks, not a mathematical proof of the RG inputs.

Discrimination audit of every gate:

| Gate | What can fail | What it cannot decide |
|---|---|---|
| G1 | Exact Bell values can exceed the proposed factorial bound; C1 actually does so at n=2. | The all-n theorem needs the injection/induction in F1, not the scan through 80. |
| G2a/G2b | The product can differ from K+1 or exceed 4; controls C2/C2b violate their proposed caps. | Whether the Gaussian model satisfies the named Yang-Mills hypotheses. F6 supplies the separate all-K proof. |
| G3 | A rational upper bound on the scale sum can exceed the lower bound on the proposed constant; C3 discards a genuinely needed tail term. | Unsampled parameters or the RG's actual decay constant. The EU/EL directions and both tail bounds are correct. |
| G4a/G4b/G4c | The rational identity, feasible minimiser/energy comparison, or size inequality can fail. C4 detects harmonic versus arithmetic averaging. | Four-dimensional Yang-Mills homogenisation or a vector flow estimate. |
| G5 | Computed exponents can disagree with the independently specified expected values. | Any analytic SP/TP/EXT hypothesis; comparing composed formulas alone is algebra, not analytic evidence. |
| G6 | The sampled difference can exceed the squared Lipschitz bound; C6 fails at opposite-sign source centres. | The four-dimensional gradient-norm conversion or the full continuum source class. Tents test a Lipschitz subclass. |

For G3, `P_N(x)<=exp(x)` makes EU an upper bound for every nonnegative x even when the code chooses N=30 for large x. EL's geometric Taylor-tail majorant is valid on its used x<40 domain; returning zero beyond that remains a lower bound. The high-scale tail starts past the maximum of `x^4 exp(-d x/4)`, and the low-scale tail is a geometric power sum. No sign reversal in those enclosures was found.

**C1 correction:** B_1=1 equals 0!, but **B_2=2>1!**. The first failure is **n=2**, not the criteria's expected n=3. SRC2 already reports this correctly; the preregistered existential control still fires.

**C5 correction:** the code fires exactly when **`s!=20 AND beta!=61`**. It fails to fire when **`s=20 OR beta=61`**. SRC2's sentence `fire only if the computation returns exactly 20 or 61` (`:608-609`) has these conditions reversed. The grossly wrong pair `(999,999)` passes C5's predicate. Moreover s_c and b_c are recomputed separately from G5's loop, so C5 is not a mutation test of that loop. This is a weak pre-registered check, not an unsatisfiable one. C5b is correctly labelled informational and unregistered; changing inputs to `(b,r)=(0,0)` tests a different parameter instance, not a damaged analytic proof. G5 itself still has a meaningful arithmetic failure condition.

No gate in this script establishes zero-freeness, source locality, closure, an all-V top bound, or plane-dependent flow admissibility. There is no new PASS for any of those inputs.

### F12 — The six inherited REFUTED labels do not amount to six verified original-source refutations

**Mixed verdicts below.** Attachment: `SRC2_55.md:619-628`, V1, V5, V6, V7, V8, V10. The original SRCCD55/LARGE55 files and the worker's brief were not added to the permitted read set; their exact original formulations are therefore not independently authenticated here.

| Item | Review verdict and claim status | Independent reason / correction |
|---|---|---|
| V1, SRC-poly singletons | CONFIRMED for the non-implication model; PROVEN in that abstract scope. | `SRCAN55.md:842-852` gives a deterministic coarse-field example. A level-r singleton-cell activity has bounded size, but its centred first derivative sums `sum_r ell_r^{-4} ~ a^{-4}`. Higher conditional cumulants vanish. Frozen independence plus a bounded top remainder excludes it; generic SRC-poly sup bounds do not. |
| V5, mandatory fixed-radius scale window | CONFIRMED that the asserted necessity is false for this sufficient route; CONDITIONAL application. | A fixed source radius incurs `lambda^{-alpha}` in the coefficient Hölder bound. Choosing the n-free radius `r_0 lambda^alpha` cancels it and costs only `lambda^{-alpha n}` in Cauchy. F1/F3/F5 extend that bound to the flat-test domain. This is not a point-source bound or a proof of N1/N2. |
| V6, plain sup-norm coefficient ball | CONFIRMED that sup smallness does not imply the required cf class; NOT-VERIFIED as a full refutation of the original four-dimensional BFT assertion. | A lattice-oscillating relative coefficient of amplitude delta has bounded sup but a unit-scale Holder seminorm of order `delta a^{-alpha}`. Even `delta~1/log(1/a)` does not control it. However `SRCAN55.md:244-274` labels the background-curvature size consequence ARGUED; I found no completed matching soft-model witness in the allowed ranges. Source-class inadequacy must not be promoted to a theorem excluding every sup-norm route. |
| V7, PP-2 gives SRC spatial content | NOT-VERIFIED as an original-source disposition; the limited averaging implication is CONFIRMED/PROVEN. | Normalised positive kernels average a uniformly bounded conditional product without enlarging its sup. This proves AVG-V. Positivity by itself supplies no distance/localisation estimate. Checking the exact M2 and PP-2 hypotheses requires the unexamined original source; their refutation is not re-certified here. |
| V8, higher conditional cumulants suffice | CONFIRMED for the refutation and its repair; PROVEN probabilistic non-implication. | Take a fair coarse sign Y and centred field `a^{-4}Y`. All conditional cumulants of orders >=2 vanish, but two separated smearings with lattice integrals one have product expectation `a^{-8}`. Order one is essential. F1 explicitly supplies it. |
| V10, full per-step package refuted by NF | REFUTED as a claim that NF is a matching counterexample; full package implication NOT-VERIFIED. | F6: the abstract Gaussian example proves only failure of bounded multipliers alone, not failure under all the named Wilson/source/large-field premises. Flow-pos is a sufficient additional input of this route, not a proved unique or universally necessary repair. |

The target's list has six entries, but their mathematical and provenance scopes differ. No blanket six-refutation tally is banked by this review.

### F13 — Symbol, quantifier, and citation audit

**REFUTED for an unambiguous use of R and for the cited bank block's current end line; CONFIRMED for the explicitly distinguished quantities below. Claim: notation/citation repairs, not a new scientific result.**

| Object | Exact attachment | Disposition |
|---|---|---|
| Torus size versus source radius | `SRC2_55.md:109-115`, symbol pins; `:132`, `T_R`; `:217`, `Put R := R_z(λ)` | R is repurposed inside Theorem I despite the symbol pins. In `R^{-n}`, `R^{-2}` and the source discs it means R_z; in `every ... R` and `S^{a,R}` it means R_tor. Use these distinct names. No torus-size power was used in my source-radius calculation. |
| The singleton C_1 versus CX's C_1 | `SRC2_55.md:218` versus `:404`; `STEP55.md:495-496` | The former is `2A_t(2L^{j_0}+2)^4`; the latter is a cluster-expansion constant depending on d and kappa_CE. They are different objects. No equality/comparison is banked. |
| Two B2 labels | `SRC2_55.md:391` and `:408-410`, corrected in `:642-644` | The conditional-law display and the background-map derivative hypothesis are unrelated. E4 already repairs this; the actual `(B2)` in N1 is still OPEN. |
| Flow A versus moment A_SP | `SRC2_55.md:109-112`, `:228`, `:356-359` | A is a lower trajectory margin, not the moment prefactor. If it varies with the terminal output, freeze the uniform choice in F8 before taking minima. |
| Fixed top offset | `SRC2_55.md:110-112`, `:199-201`, `:329` | j_0 must be independent of the cutoff. Merely setting `j_0=K-m` for an arbitrary moving fine level would make `L^{4j_0}` diverge. The global symbol/representation statements do fix it, so the intended conditional theorem survives. |
| Source Holder threshold | `SRC2_55.md:309-312`, `:329-339` | epsilon_hat_* is N1's coefficient-field threshold, not one of the unrelated lane epsilon_* constants. r_0 is evaluated from the fixed source inputs and gamma, not from a later output radius. |
| PROOF bank range | `SRC2_55.md:60`, `PROOF.md [S26-BANKED] block (lines 5-47, by string)` | The marker is currently at `PROOF.md:5`, but the block now runs through the dictionary corrections at `:54`; `:47` is the Off-𝒞_glob entry. The current range is **5-54**, not 5-47. This is current citation drift, not evidence that the author's earlier timestamped read was false. I relied on no scientific status from that block. |
| CX rate after fattening | `SRC2_55.md:404` versus `STEP55.md:679-682` | F7's correction applies before checking positivity/smallness. This is the concrete stale-threshold hazard in this target. |

I found no target citation of the form `PROOF.md l.NNNN` requiring a deep PROOF lookup. The only PROOF content read was the opening bank range and the narrow locator checks above; its status labels were not substituted for proofs.

## Scope and verification receipt

The review used the named target, STEP55, SRCAN55, CODEX_REVIEW_OSLEAF, the explicitly requested sr2_55_1 check family, the named methodology map, and narrow opening PROOF ranges. The two additional files selected were the local `docs/ai_methodology/skills/review-loop/SKILL.md` procedure and `OSLEAF55.md` for the original TP/EXT/SP statements. All scientific files were inspected by string search and bounded sed ranges. No snapshots, audit ledgers, git commands, other original-source files, or external literature were used. No subagents were launched. Only this deliverable was written.

The check script was executed once as described in F11. Independent inline Python used only exact integers/Fractions to verify the NF telescoping majorant algebra, exponent substitutions, the C5 wrong-answer witness, and the two-site/HOM exact values. The all-parameter assertions in this review are proved in prose, not inferred from samples. No generated logs, scripts, bytecode or output files were created.

The source's E1-E12 errata were considered, including E11's explicit open locality conversion and E12's corrected count sentence. I do not count superseded source text as an uncorrected mathematical defect. The numerical source-check corrections concern the still-current wording or the preregistered criteria, as specified. The final metadata check at 2026-10-29 06:54:40 UTC reported SRC2_55.md as 87,410 bytes, last modified at 06:27:06 UTC, before this review began; no git identity was requested or used.

## Summary table

| Finding | Verdict | Bankable claim status / limit |
|---|---|---|
| F1 frozen/top => all-order coarse products, including order one | CONFIRMED | CONDITIONAL on S0-S4; Bell bound and geometric estimates PROVEN. |
| F2 MB and its promoted role | CONFIRMED identity; NOT-VERIFIED construction | MB PROVEN under its factorisation premise; N1 construction GAP. |
| F3 source class and Theorem II | CONFIRMED implication; REFUTED intermediate gradient factor 1 | CONDITIONAL N1+N2; correct four-dimensional factor 2 already fits final constants. |
| F4 coupling point-image/W1-W3 inference | REFUTED | Smeared control allows a^{-4} point images; pointwise extension GAP without extra input. |
| F5 TP/EXT exponents and all-cube torus repair | CONFIRMED | CONDITIONAL; s=21, beta=123/2 survive. |
| F6 NF | CONFIRMED Gaussian model; REFUTED premise-matching claim | Model identities PROVEN; the full package non-implication NOT-VERIFIED. |
| F7 CX-to-N1 origin and stale rate | REFUTED displayed source-locality inference/stale rate; NOT-VERIFIED actual assembly | R3 re-localisation, full density control, closure and all-V bounds remain GAP/OPEN. |
| F8 FP | CONFIRMED scalar implication; NOT-VERIFIED actual plane flow | CONDITIONAL scalar theorem; vector extension ARGUED. |
| F9 HOM | CONFIRMED model identities | PROVEN abelian mechanism; no Yang-Mills flow theorem. |
| F10 LF-loc | CONFIRMED with simpler proof | CONDITIONAL moment estimate; SRC-I unnecessary for fixed finite root neighbourhoods. |
| F11 sr2_55_1 | CONFIRMED execution; REFUTED C5 description/C1 expected first order | Finite arithmetic/model checks only; no analytic-input PASS. |
| F12 inherited six | Mixed; blanket six-refutation certification NOT-VERIFIED | Preserve individual scope, especially V6/V7/V10. |
| F13 symbol/citation audit | REFUTED unambiguous R/current range; other pins CONFIRMED | Notation and stale-threshold corrections; no changed H_reg exponents. |

## Exactly what may be banked

1. **PROVEN conditional theorem:** on the stated L-adic tori, with fixed top offset and all N1 clauses R0-R5 plus N2 (Flow-pos), the source radius is n-independent, `R_z=r_0 lambda^alpha`. The frozen/top representation gives uniform conditional products including singletons. Averaging gives `(SP_lambda)` with `b=1, p=2+alpha, r=1, c_SP=1`. Neither N1 nor N2 has been proved for Yang-Mills.
2. **PROVEN conditional continuation of that theorem:** the torus-wide SP domain supplies every TP factor, including those from boundary-touching X1 cubes. The sufficient parameters are `p_X=6+alpha`, `r_X=7`, `b_X=23/2`, `c_*=4`, and **`s=21, beta=123/2`** with FLOW units, `Z=1`, `q_X=4`. This is the separated/flat-test H_reg route. The local-versus-infinite-radius distinction of the existing OSLEAF bank remains; no global theory at fixed radius is asserted.
3. **PROVEN algebraic and model results:** the tower averaging lemma; MB with its actual factorisation hypothesis; the scalar FP implication with a uniform radius fixed as in F8; NF's exact covariance `(K+1)^2` and its all-K summable comparison `<16`; HOM's harmonic coefficient and remainder `-(u/4)epsilon^2`. These do not establish the full RG hypotheses or a necessity theorem for a unique repair.
4. **PROVEN scope boundaries:** E4 defeats generic per-level source-polymer sup bounds for singletons; higher conditional cumulants need order-one control; the two-site model in F4 defeats the claimed inference to uniform point-energy images. A smeared coupling insertion is covered; its unsmeared point version needs its own size/representation input. No W1/W3 pointwise estimate from N1 alone is banked.
5. **PROVEN simplification:** the stated finite-root LF envelope suffices without SRC-I, by fixed-V rooted estimates and the deterministic factor `exp(C_LF N_N)`. This does not control unbounded paths or supply the missing actual LF envelope.
6. **CONFIRMED execution record only:** sr2_55_1 returns its reported 9/9 and 7/7. C1's first failure is n=2. C5 is weak, its firing description is reversed, and neither it nor the other gates certifies N1/N2.

**Not banked:** N1's derivation from STEP55 CX/(B2)/I6^C/LF-src, strict source re-localisation with uniform rate, the complete normalised all-V complex representation, plane-dependent Flow-pos, an unconditional separation estimate, the matching-premises V10 refutation, the blanket six-refutation tally, or any unconditional continuum/nontriviality/mass-gap conclusion.

**Single most dangerous unverified item:** N1's cutoff-uniform, strictly source-local representation of the **complete normalised** density ratio, with a bounded coarse-dependent top remainder at **every** coarse field. Its locality and bounds are precisely what make the singleton cancellation useful; MB, CX's spectator holomorphy, and the literal LF-src restatement do not establish them.

