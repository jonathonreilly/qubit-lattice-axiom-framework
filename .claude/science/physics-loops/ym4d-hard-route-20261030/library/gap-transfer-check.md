8 numbered statements hold and 0 fail, with (8e) excluded exactly as in the status line; the first algebraic failure is line 136, the reversed temporal holonomy, outside the proofs of (1a)–(1c).

## Repo search

The lead's general digest, `library/prior/repo-search-2026-11-08.md`, names `MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` on PRs #10114 and #10133: a positive one-step Wilson-loop correlation. Its source points to a much closer earlier result. I fetched PR #10114 and read the following at `f76f6c649cff7dffbab664d8976e680e8f287fe9`, under `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`:

| Source read | What it contains; closeness |
|---|---|
| `MASS_GAP_LOCAL_BLOCK_ASTRA.md:1–149` | Identifies its inherited finite transfer construction, positive ground state and injectivity. Its loop witness is related to (5c), but is not this check. |
| `MASS_GAP_CONSTRUCTION_ASTRA.md:1–225`, especially §1.1–§1.2 | The same full Wilson transfer, with spatial multiplier and gauge projection, for SU(N), including SU(2). It gives a simple positive vacuum, injectivity, density, and the stronger bound `m >= -log(1-exp(-6 beta N^3))` in the present notation. Its omitted scalar per time step cancels from eigenvalue ratios. This is existing work, not a new result of row 667 or this check. |
| `REVIEW_MASS_GAP_CONSTRUCTION_ASTRA.md:1–145` | An earlier source review of that different text, including the finite transfer argument. Its runs and verdict are not proof inputs here. |

Credit these earlier Codex/Astra research notes for the finite-transfer construction and stronger estimate. I stopped any new attack on that already-covered estimate. The present assignment is a check of Claude's particular 277-line proof, including its gauge-fixing remark and slab limits; the older review does not check that text. The pinned `library/open-registry.md` has no competing `gap-transfer-check` owner. Row 668's continuum/OS task is not taken over. `library/prior/gap-transfer-check.md` is absent.

On main, fetched at `3b6e5c0baf4295645a07cbfc99813501c8c08c63`, I checked the three sources named at lines 20–22:

- `docs/AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md:1–212`, especially 115–167: a written representation-ring proof of nonnegative coefficients, with uniform convergence. A runner's presence does not invalidate this hand proof. Line 20 wrongly dismisses it on that ground. This file has the same Git blob at the author's main revision `bf92a1d76` and at the main revision checked here. The source does not give the SU(2) strict lower bound for every coefficient.
- `docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md:1–100`: a supplied SU(3) heat-kernel operator, with Perron–Jentzsch imported and physical identification explicitly missing. Related operator method, different kernel.
- `docs/SPATIAL_SLAB_TRANSFER_OPERATOR_POSITIVITY_AND_DELTA_X_REAL_NOTE_2026-05-19.md:1–90`: conditional spatial-slab claims. These lines do not supply the Wilson construction checked here.

I reused the lead's five-ref search record, not a new exhaustive repository search. The fresh source checks above are the target-relevant hits and their newly discovered direct ancestor.

The outline index was consulted first: README, the matching GL3/GL8 rows of `chunk-02.md` with their neighbouring rows, and the Chunk 02 obligations. I then read SA 2195–2244 and 2313–2335 at `31a47c543775`. GL3 already gives positive one-link convolution eigenvalues. GL8 already gives the gauge-projected transfer and partition trace. They are credited to **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**. These are prior results, not new closures. Both requested source files were fetched once, to `/tmp/sa_ym4.tex` and `/tmp/sa_ca_I.tex`. No complete-account theorem is a proof input here; CA-III 9.98 was not read, and no absence claim about the complete account is made.

## Scope and verdicts

Checker: Codex, task profile gpt-6-astra/high, not the author of `gap-transfer.md`. Checked source: `bf474ee1c47620685597f9122c9ab34bcf3cb60a`, all 277 lines, once in full using bounded recovery of the initially truncated display. Research text, not an audit; grants no status. No numerical or computer-assisted proof step was used. The source file was not edited.

“HOLDS” below concerns the displayed numbered mathematical statement, using the elementary mathematical foundations listed later. It does not certify every remark or claim of self-containment. In particular, the erroneous gauge-fixing remark is explicitly unused by the valid trace proof. Statement (8) is counted with its status-line exception: (8e) is cited, not proved.

| Statement | Verdict and first failing line |
|---|---|
| (1), lines 115–122 | **HOLDS.** No failure in (1a)–(1c) or steps 1.1–1.7. The additional temporal-gauge account required by the row fails at line 136. Complete repair R1 below. |
| (2), line 142 | **HOLDS.** The operator and finite-Gram positivity claims are distinct and both proved. Every character coefficient has the correct positive sign for beta > 0. |
| (3), line 159 | **HOLDS.** The proof supplies a Hilbert–Schmidt factorization; it does not infer trace class from compactness or Hilbert–Schmidt membership alone. |
| (4), lines 168–172 | **HOLDS.** A2–A3 prove existence, positivity, continuity, simplicity, and the quantitative separation. Jentzsch is credited but not imported. Gauge invariance is proved on the whole configuration space. |
| (5), lines 183–185 | **HOLDS.** The constant 24 follows from the stated bounds, and the second invariant eigenvalue is strictly positive. The bound is weaker than existing repository work. |
| (6), lines 202–208 | **HOLDS.** The trace tail has the stated finite prefactor and exponent. Complex observables and t = 0 are handled correctly. |
| (7), lines 219–220 | **HOLDS.** The density argument is valid, and no conjugation-closure assumption on the class is missing. |
| (8a)–(8d), lines 239–244 | **HOLDS.** All bounded finite-slab functions, including non-invariant ones, have the asserted limits and clustering. (8e), line 245, remains an explicitly unproved extension theorem. |

## Line-by-line mathematical checks

### Foundations, lines 34–104

N.1–N.8 are consistent. In particular, the entries of an SU(2) inverse really are signed entries of the original matrix. This matters in 5.5. There are `3N^3` positive spatial links and `3N^3` spatial plaquettes. Each plaquette action lies in `[0,2 beta]`; hence `0 <= V <= 6 beta N^3`.

A0.1–A0.5: the two Parseval sums and the absolute double-sum bound in A0.2 are correct with the convention that the first inner-product argument is conjugated. In particular its final expression is `<S_2^* f_m,S_1^* f_m>`, not the opposite order. The finite-rank approximation in A0.4 and the kernel/trace formulas in A0.5 are valid. For completeness, the composition kernel is in L2: if `a(y)^2 = integral |k(y,z)|^2 dz` and `b(w)^2 = integral |l(z,w)|^2 dz`, then `|k circ l(y,w)| <= a(y)b(w)` and its L2 norm is at most `||k||_2 ||l||_2`. All trace integrals are absolutely convergent by Cauchy–Schwarz. The same proofs work between two different Hilbert spaces, as used in §3.

A1 is the positive trace-class definition, sufficient for its uses. A2.1–A2.7 prove the compact positive spectral theorem needed here: the positive-form Cauchy–Schwarz inequality yields the norm formula, compactness turns a maximizing sequence into an eigenvector, and orthogonal restriction produces the entire nonzero spectrum. The displayed resolvent includes the kernel complement. Finite multiplicity and the trace sum follow. None of these steps needs an assumed spectral gap.

A3.1–A3.7 hold. The maximizer may first be made real, then replaced by its absolute value without lowering its Rayleigh quotient. Equality in the explicit residual estimate makes that absolute value an eigenvector. Its continuous representative is obtained by applying the kernel. This gives an everywhere positive function, not merely an almost-everywhere positivity assertion. The representative still satisfies the eigen-equation everywhere, since changing an integrand on a null set does not change its integral.

The norm-one eigenfunction satisfies `sup Omega <= kappa_2/lambda_0` and `||Omega||_1 >= sqrt(lambda_0/kappa_2)`. Both inequalities and all their directions in A3.4 are correct. Multiplication by Omega is unitary from L2(Omega² mu), since Omega and its inverse are bounded. The transformed symmetric kernel has row integral one. Its minorization yields the form bound on the orthogonal complement, including the separate delta = 1 case. That bound, with delta > 0, proves simplicity. This is a proof of the required Jentzsch step, not a citation to it. Full support of mu is not needed for this lemma's assertions about the chosen representative.

A4.1–A4.3 hold. For countable unions, the sum of outer-minus-inner errors costs at most epsilon/2 and the finite-tail error costs less than epsilon/2. The distance quotient has nonzero denominator because F is closed, is contained in O, and Y is compact. The degenerate cases use 0 when F is empty and 1 when O is all of Y. Quantization and clipping give finite-valued approximants dominated in modulus by |f|. Completed-measure L2 functions have Borel representatives modulo null sets, which is the convention needed here.

### (1): links, plaquettes, projection and traces

At each time there are `3N^3` spatial links and `N^3` temporal links: `4N^3 T` Haar factors in total. At each time there are `3N^3` spatial plaquettes and `3N^3` temporal plaquettes: `6N^3 T` action terms. A temporal link can occur in several plaquettes; it is integrated **once**, through the single group variable `g_t(x)` in the slab t. Step 1.3 groups all those plaquettes before that integration. It does not integrate each plaquette independently.

For T = 2 one must retain the conventional periodic lattice as a cell lattice: the positive temporal bonds `(x,0;0)` and `(x,1;0)` are distinct link variables, even though their endpoint pairs coincide after forgetting orientation. This is exactly the configuration space declared in N.6. Collapsing it to a simple graph would change the problem. With this convention the `3N^3 T` temporal plaquettes in 1.1 are distinct. N >= 3 avoids the corresponding spatial degeneracy.

The temporal holonomy is

`g_t(x) U(t+1)_(x,i) g_t(x+e_i)^(-1) U(t)_(x,i)^(-1)`.

Its trace equals that of its inverse, giving the kernel in 1.2. Each slice's spatial action is split into two halves, one from each incident slab. Thus every plaquette weight and every normalized Haar integration appears once. There is no gauge-volume multiplier.

Steps 1.4–1.6 correctly use both left and right Haar invariance, inversion invariance, and simultaneous gauge covariance. Jensen makes P bounded; P² = P = P* then makes it an orthogonal projection. The a.e.-invariance assertion in 1.5 is justified by Tonelli; an invariant representative can be set to zero on the invariant null set where its averaging integral is undefined. P commutes with T, and its averaged kernel is separately invariant in each endpoint.

In 1.7 the two Hilbert–Schmidt factors are the bounded-kernel product containing T-1 transfer factors, and the last transfer factor. T >= 2 is precisely what makes the first factor contain at least one transfer. Zero gaps between equal times simply multiply the corresponding functions. For invariant insertions the product commutes with P, annihilates its orthogonal complement, and its restriction is the displayed product of unprojected T powers. Thus both trace identities hold, including coincident insertions. Remark 1.9 is valid for distinct slices. Remark 1.8 is not: see R1.

### (2) and (3): signs and trace class

In 2.2, each link contributes squared entry norm 2, so the sum over entry indices is `2|E| = 6N^3`. The exponential majorant is exactly

`exp(-beta |E|) sum_n (beta |E|)^n/n! = 1`.

Every `w_n` is strictly positive. The finite-Gram formula and the operator quadratic-form formula in 2.3 therefore have positive signs. The multiplication and projection sandwiches preserve operator positivity.

For the character calculation put `d = 2l`, an integer. The symmetric tensor space has dimension d+1, is invariant and unitary, and its diagonal weights are `exp(i(d-2k)theta)`, `0 <= k <= d`. Their sum gives the stated character, including the signed endpoint value at theta = pi. The character product recurrence gives

`m_(n+1,l) = m_(n,l-1/2) + m_(n,l+1/2)`

with negative-spin terms zero and `m_(0,0) = 1`. All multiplicities are nonnegative integers and `m_(2l,l) = 1`. Consequently

`a_l = sum_n (beta/2)^n m_(n,l)/n! >= (beta/2)^(2l)/(2l)! > 0`.

Evaluation at the identity gives `sum_l m_(n,l)(2l+1) = 2^n`. Thus `sum_l a_l(2l+1) = exp(beta)`, which justifies absolute uniform convergence and every rearrangement. The matrix-entry Gram formula proves positive definiteness of each character kernel, and tensoring proves it for products of links. Irreducibility or Peter–Weyl completeness is not required by this argument. The source uses elementary unitary diagonalization; that foundational input is recorded below.

In 3.2 the map R is first defined on finite sequences. Cauchy–Schwarz gives `||R x|| <= (sum_alpha ||R delta_alpha||²)^(1/2) ||x|| = ||x||`, so it extends to all of l2(J). Its squared Hilbert–Schmidt norm is 1. Polarization of 2.3 yields `C_E = RR*`. Then `T = (R*M)*(R*M)` and `T_P = (R*MP)*(R*MP)`. Tonelli gives `Tr T = integral exp(-V)`, and contraction by P gives `Tr T_P <= Tr T <= 1`. This verifies the trace-class claims without invoking a diagonal-trace theorem for arbitrary continuous kernels.

### (4) and (5): invariant vacuum and the constant 24

The hypotheses of A3 are all checked in 4.1: compact metric X, probability Haar measure, real symmetric continuous kernel, positive lower bound, and operator nonnegativity. Separate gauge invariance of A_T makes its continuous vacuum gauge invariant at every point. For the unprojected T, each gauge transform is a unitary commuting operator. It sends the normalized positive top eigenfunction to another such eigenfunction. Simplicity and positivity force the scalar to be +1. Hence that eigenfunction belongs to Ran P and the two top eigenvalues agree. No invariant-sector truncation has been substituted for the whole gauge-invariant Hilbert space.

Recounting independently, the two half spatial weights each cost at most `3 beta N^3`, and the temporal weight costs at most `6 beta N^3`. Therefore

`exp(-12 beta N^3) <= T_0, A_T <= 1`.

Set `kappa = exp(-12 beta N^3)`. The normalized vacuum has `sup Omega <= 1/lambda_0`, while `lambda_0 >= kappa`. The Doob kernel relative to `nu = Omega² du` is

`r(u,v) = A_T(u,v)/(lambda_0 Omega(u) Omega(v)) >= kappa lambda_0 >= kappa²`.

Subtract its constant minorization and divide by the remaining mass. The result is a symmetric Markov kernel; `2|f(u)f(v)| <= |f(u)|²+|f(v)|²` bounds its quadratic form by `||f||²`. On mean-zero vectors this proves

`lambda_1/lambda_0 <= 1-kappa lambda_0 <= 1-exp(-24 beta N^3)`.

Since `-log(1-x) = integral_0^x (1-s)^(-1) ds > x` for `0 < x < 1`, the claimed strict logarithmic bound holds. Thus **24 is correct for this proof**, not an optimal constant. The older repository proof uses the unnormalized gauge-averaged kinetic factor and gives 6; it is not re-derived here.

Steps 5.3–5.7 supply the separately needed positive second eigenvalue. If the invariant restriction had rank one, every vector perpendicular to Omega would have zero quadratic form. Since all w_n > 0, it would be orthogonal, after multiplication by M, to both 1 and the degree-four plaquette polynomial W. Thus both M and MW would be multiples of Omega and W would be a.e. constant. The chosen four links are distinct for N >= 3. Setting one to -1 and the other links to 1 changes W from 2 to -2. Both strict sign neighbourhoods have positive Haar measure by the finite-translate covering argument. Contradiction. This proves `lambda_1 > 0`, not merely its upper bound. The rank-one beta = 0 endpoint is correctly separated in 5.8.

### (6) and (7): limits, complex observables and density

Steps 6.1–6.3 use the trace-class factorization to evaluate the trace in an eigenbasis without a cyclic-trace assumption. With `s = T-t >= 2`, each scaled diagonal element G_j is bounded by `||A||_infinity ||B||_infinity`, and

`sum_(j>=1) rho_j^s <= rho_1^(s-1) sum_(j>=1) rho_j <= exp(-m(s-1))/lambda_0`.

This gives the stated `2 exp(12 beta N^3)` prefactor and exponent `T-t-1`. The denominator is `1+b_T >= 1`; the subtracted denominator term is correctly included. At t = 0 the insertion is AB, so there is no missing identity/projection issue. In 6.4 the left vector is conjugate A times Omega, which is required by the chosen inner-product convention. Its centered norm equals sigma_A. The series is asserted only for t >= 1, so possible zero modes are not incorrectly included at t = 0.

For (7a), density of `{F Omega}` implies density of `{conjugate F Omega}`, even when the class is not closed under conjugation. The nonzero finite-dimensional lambda_1 eigenspace first supplies B, then the conjugated dense family supplies A with nonzero gamma. The remaining coefficients are absolutely summable by Bessel and Cauchy–Schwarz. Dividing by rho_1^t and using dominated convergence leaves gamma, so no cancellation can hide this eigenvalue from every such pair. Comparison of exponential rates gives mu <= m. The constants may depend on A and B.

For (7b), 1/Omega is bounded, continuous and invariant. A4 approximates psi/Omega in L2 by continuous functions; applying the contraction P preserves convergence and makes them continuous and invariant. Multiplying back by bounded Omega proves the claimed density. This uses the whole continuous invariant class, not an unproved density of plaquette observables. The constants-only example in 7.7 is correct.

### (8): the time period tends to infinity

For a slab of length L = b-a >= 1 and T >= L+2, all slab slices are distinct and the complement has at least two transfer steps. Integrating only the complement gives `Tr(K_F T_P^(T-L))` even for a non-invariant F: no gauge transformation has been applied to F. The bound `|K_F| <= ||F||_infinity a_L` gives `|<phi,K_F phi>| <= ||F||_infinity lambda_0^L ||phi||²`. The same summable eigenvalue tail as in (6) proves the asserted limit and rate, for each fixed F and slab. No exchange of an infinite-volume or continuum limit occurs.

The explicit slab density is positive and has integral `lambda_0^(-L)<Omega,T_P^L Omega> = 1`. Extension of a slab and time translation preserve the finite-period expectations for all sufficiently large T, so they preserve the limits. Alternatively an endpoint can be integrated out using the vacuum equation; repeated endpoint integrations prove consistency. Single-slice functions can be placed inside any positive-length slab. Thus no length-zero kernel has been silently used.

For disjoint slabs with d >= 1, the intervening integral is T_P^d. Projecting both endpoint vectors with P is legitimate because this power annihilates the non-invariant complement. The vacuum subtraction yields the centered power, bounded by lambda_1^d. The two endpoint norms cost at most `||F||_infinity lambda_0^(b-a)` and `||H||_infinity lambda_0^(b'-a')`. These powers cancel the normalization, leaving precisely `exp(-md)` with coefficient 1. This verifies 8.5 for complex and non-invariant functions as well.

(8a)–(8d) establish all finite-slab expectations. They do **not** construct a single probability measure on the infinite cylinder. Line 245 correctly leaves that to the extension theorem; line 274 must preserve this exception.

## Defects, overstatements and complete repairs

### R1. Line 136: reversed holonomy; repair proved

The ordered product remaining after the stated transformation is `g_0 g_1 ... g_(T-1)`, not its reversal. Here is the full change of variables.

Set `h_0 = 1` and `h_t = g_0 ... g_(t-1)` for `1 <= t <= T-1`, pointwise at each spatial vertex. Define `W(t) = h_t . U(t)`. For each fixed collection of temporal links, this preserves the product Haar measure of all spatial links. Simultaneous covariance gives

`T_0(U(t),g_t . U(t+1)) = T_0(W(t),(h_t g_t h_(t+1)^(-1)) . W(t+1))`.

For `0 <= t <= T-2`, the parenthesis is 1, since `h_(t+1) = h_t g_t`. For the last slab the next slice is 0, so `h_T` in this formula is `h_0 = 1`, and the remaining temporal link is

`H = h_(T-1) g_(T-1) = g_0 g_1 ... g_(T-1)`.

Equivalently, the full spacetime gauge transformation is `g'_t = h_t g_t h_(t+1)^(-1)`, with periodic h. It sets the first T-1 temporal layers to 1 and leaves H on the last layer. It does not set the periodic time holonomy to 1. The transformed weight is

`[product_(t=0)^(T-2) T_0(W(t),W(t+1))] T_0(W(T-1),H . W(0))`.

For fixed `g_0,...,g_(T-2)`, the map `g_(T-1) -> H` is a left translation on the product gauge group, so `dH = dg_(T-1)`. The other normalized temporal integrals equal 1. Integration of H supplies one P, giving `Tr(T^T P)`. Invariant slice observables are unchanged by the spatial substitutions. This proves the repaired temporal-gauge formulation with all integrations counted.

A hand-checkable failure of the reversed order occurs at T = 3. In SU(2) take

`I = diag(i,-i), J = [[0,1],[-1,0]], K = IJ = [[0,i],[i,0]]`.

Then `I J K = -1` whereas `K J I = 1`. Put `g_0(x)=I`, `g_1(x)=J`, `g_2(x)=K` at one vertex x and put all other temporal links equal to 1. Set every transformed spatial link W(t) to 1. The correct H is -1 at x, so the last slab has six incident link factors `c(-1)` and weight `exp(-12 beta)`. The reversed H is 1 everywhere and would give weight 1. N >= 3 makes those six incident links distinct. Thus the claimed pointwise transformed weight is wrong. Both orders have Haar law after full integration; this does not make the stated change-of-variables identity correct, nor does it invalidate the separately proved partition trace.

### R2. Line 264: a logarithmic Hamiltonian needs injectivity

Sections 1–8 prove a second positive eigenvalue, not injectivity of `R_inv`. Defining `-log R_inv` as a densely defined self-adjoint operator on the entire stated space additionally requires `ker R_inv = 0`. An infinite-dimensional zero eigenspace cannot be assigned a finite Hamiltonian eigenvalue or simply omitted from a dense domain.

This is a proof omission, not a counterexample to injectivity of the actual Wilson operator. That injectivity is already proved, using Peter–Weyl, in the older construction cited above. To prove it from 2.3 alone would require density of the entry polynomials; A4 proves density of continuous functions, not polynomial density. I do not redo that covered task. The correction table replaces the logarithmic formulation by the equivalent eigenvalue-ratio inequality, which follows directly from the definition of m. It is a complete repair of the asserted equivalence without adding an unproved operator construction.

### R3. Line 260: sector maximum and physical identification

The commuting involutions do give eight orthogonal projections

`E_e = (1/8) product_(k=1)^3 (1+e_k R_(Z_k))`.

Their products satisfy `E_e E_f = 0` for e != f, `E_e² = E_e`, and `sum_e E_e = 1`, by expanding the three commuting involution factors. They commute with the transfer. The vacuum lies in the all-plus sector by the already proved uniqueness argument. Therefore the **excited** maximum is

`lambda_1 = max_e ||R_inv restricted to (H_e intersect Omega^perp)||`.

Taking the maximum of the unrestricted sector tops instead gives lambda_0, because the all-plus sector contains the vacuum. The source must say which maximum it means. The further identification of the lowest small-torus states with particular states studied by 't Hooft and van Baal is stated without a read source or proof. The algebraic sector decomposition does not establish that identification. The table removes it while preserving the labels.

### R4. Line 256: finiteness does not follow from kernel positivity

The continuous kernel `k(y,z)=1` on a probability space is strictly positive, compact, positive as an operator, and positivity improving. Its operator has rank one. It has no positive excited eigenvalue; with the convention in 5.8, its gap is infinite. Thus m < infinity is not a consequence of the generic properties claimed at line 256. It uses the beta-dependent polynomial argument in 5.3–5.7. Also, the explicit bounds decay, not the truth of the qualitative statements m > 0 and m < infinity. The corrected paragraph makes this distinction.

### R5. Lines 266–268: limits and the positive lower bound on beta

“Any beta(a) bounded below” is insufficient literally: positive beta(a_N) = N^(-4) is bounded below by zero, but `exp(-24 beta(a_N) N^3) = exp(-24/N)` does not tend to zero. The needed assumption is an eventual strictly positive lower bound beta_*.

Under that assumption the ratio of the displayed lower bound to `m_ell ell/N` is at most `N exp(-24 beta_* N^3)/(m_ell ell)`. It tends to zero; indeed its logarithm is at most `log N - log(m_ell ell) - 24 beta_* N^3`, and the first two terms are eventually at most `12 beta_* N^3`. This proves the intended comparison. It compares a lower bound, not the actual gap. The preceding equivalence to dense-class decay is correct. “Nothing ... bears on” overstates its lack of relevance; the preceding results supply that equivalence but not the uniform estimate.

No infinite-volume transfer operator is constructed in this file. Consequently line 268 does not prove a theorem that compactness fails for such an operator. Replace that assertion by the precise limit of the finite-volume argument.

### R6. Line 274: preserve the exception for (8e)

“All eight are proved” omits the express exception in lines 4 and 245. The correction retains (8a)–(8d) and the cited status of (8e). The asserted measure exists by the cited extension theorem if that theorem is accepted; it is not constructed by this proof.

### R7. Lines 20, 24 and 277: prior-work and credit corrections

Line 20's inference from the presence of a runner is false. The source has a written proof, quoted in the Repo search section by its exact location. Line 277's claim that **any** better bound remains open is contradicted by the earlier Wilson-transfer construction. This is the same operator up to a positive scalar: the earlier kinetic factor omits `exp(-beta |E|)`, so all normalized eigenvalues and m agree. No extrapolation from an SU(3) heat kernel is involved. The stronger finite-volume bound still degenerates and does not establish (G-ell) or (G-inf). Line 24 should also give the requested Claude/Codex authorship credit.

### R8. Lines 24, 155 and 276: unrebuilt mathematical inputs

Line 276 is accurate only if “cited” means the one explicitly imported research theorem. It is not a complete dependency list. Ordinary foundations remain inputs, as detailed next. In addition, line 24's equal-nonzero-spectrum observation and line 155's Schur/Bessel observation are correct side facts, not proved in this file and not used in (1)–(8).

The spectral observation can be checked without a new spectral theorem. For `X=PM C_E^(1/2)`, commutation with P gives `XX*=T_P` and `X*X=L`. If `XX* u=lambda u`, lambda > 0, then `||X*u||²=lambda ||u||²`, so X* is injective on that eigenspace and maps it into the lambda eigenspace of X*X. Its inverse there is X/lambda. The reverse calculation is identical with X and X* exchanged. Thus the nonzero eigenvalues and eigenspace dimensions agree. A bounded positive square root exists here by applying A2 to C_E and taking square roots of its eigenvalues. No unitary equivalence of the whole operators is needed.

## Facts used without proof: exact scope and hypotheses

The following are imported foundations, not computer-assisted steps. These dependencies do not conceal Jentzsch, a mass-gap theorem, or an unproved gauge-fixing theorem.

| Source uses | Exact unproved fact and hypotheses; affected statements |
|---|---|
| N.1, 1.3–1.7 and throughout | Existence of normalized surface/product measure; invariance of surface measure under orthogonal maps; change of variables for measure-preserving transformations. Compact SU(2) and its finite products meet these conditions. All statements. N.1 verifies the relevant group maps are orthogonal, but does not construct surface integration from first principles. |
| A0.1–A0.5, A2.7, 3.2, 6.1, 7.3 | A Hilbert space has orthonormal bases, Parseval's identity, Bessel's inequality, bounded adjoints, and orthogonal projections onto closed subspaces. A specified unit vector or orthonormal family can be completed to a basis. The spaces here are complete L2 or l2 spaces; invariant complements are closed. All statements through A0/A2. |
| A0.1–A0.5, A2.7, A4.1, 1.3, 1.5–1.7, 2.3, 3.2–3.3, 8.1–8.5 | Tonelli for nonnegative functions/series; Fubini for absolutely integrable functions; continuity of a finite measure from above/below. The proof supplies the L2 Cauchy–Schwarz bounds, bounded integrands on probability spaces, or nonnegative summands. All statements. |
| A4.3, 2.3, 7.3 | Dominated convergence: pointwise convergence plus an integrable dominating function permits passage under the integral/sum. Dominators are respectively a constant multiple of |f|², |f(u)f(v)| times the uniform kernel majorant, and the Bessel/Cauchy–Schwarz summable coefficient product. Directly (2), (7); indirectly its consumers. |
| A0.2–A0.5, A2.1, A3, 1.5 and subsequent norm estimates | Cauchy–Schwarz in Hilbert/L2 spaces and for positive semidefinite sesquilinear forms; Jensen for the square under a probability average; polarization of complex quadratic forms; 2ab <= a²+b². All hypotheses are satisfied by the specified positive forms or normalized measures. All statements. |
| N.3, A0.4, A3.4, A4.2, 1.4, 7.5 | Closed bounded subsets of finite-dimensional Euclidean space are compact; finite products are compact; continuous functions on a compact metric space are bounded and uniformly continuous; finite-dimensional bounded sequences have convergent subsequences. These are used with finite products of SU(2), their gauge group, or finite-rank ranges. All statements through compactness and continuity. |
| 2.5, line 152 | A unitary 2-by-2 complex matrix admits an orthonormal eigenbasis; determinant one makes its eigenvalues exp(±i theta), and the diagonalizing unitary can be rescaled to determinant one. The tensor restriction is unitary and finite dimensional. This fact supplies the explicit characters in (2d). It is not proved in the source; the direct entry-Gram argument for (2b) does not need it. |
| 2.2, 2.5, 5.2 and 7.4 | The absolutely convergent exponential power series, elementary trigonometric identities, monotonicity and integral formula for log, and elementary exponential-limit comparison. Applied to bounded finite-dimensional variables, beta > 0 and numbers in (0,1). The displayed expansions and comparisons check their required signs and convergence. |

The only additional named extension theorem proposed for the numbered results is **Kolmogorov extension**, line 245: a projectively consistent family of finite-coordinate probability laws on a countable product of standard Borel spaces extends uniquely to a probability measure on the product sigma-algebra. Here each coordinate is SU(2), a compact metric space, the set of lattice links is countable, and the consistent slab laws determine every finite-coordinate marginal. These hypotheses hold. The theorem itself is cited, unread and unproved; (8e) expressly does not claim otherwise. None of (1)–(7) or (8a)–(8d) uses it.

Other cited facts are side remarks, not proof inputs:

- Line 24: SA GL3's convolution eigenvalues `2 exp(-beta) I_(2l+1)(beta)/beta`, and GL8's projected partition trace. The source passages were read; they use Schur's lemma, the SU(2) Weyl integration formula, and a Bessel recurrence. The checked file gives its own positive-coefficient and trace arguments instead. The X*X/XX* comparison is proved above.
- Line 155: Schur orthogonality gives the eigenvalue `exp(-beta) a_l/(2l+1)` on the spin-l matrix coefficients. Its hypotheses are an irreducible unitary spin-l representation and normalized Haar measure. The symmetric powers used here are the usual spin-l representations, but their irreducibility and Schur orthogonality are not proved in this file. No numbered result uses this identification or the Bessel formula.
- Lines 26 and 83: Perron, Frobenius, Jentzsch, Osterwalder–Seiler and Lüscher are historical credits. Their papers were not read by the author. No theorem from them is imported into (1)–(8a–d); A2–A3 supply the actual operator proof.
- Line 260: the 't Hooft/van Baal statement is unverified physical identification, not a needed mathematical input. Remove it as specified below.

## Correction table

All line numbers and old words refer to `gap-transfer.md` at the pinned commit. Rows replace the specified substring unless they say “whole line.” The checked file remains untouched. R1–R8 above supply the reasons, counterexamples and mathematical justifications; the following are exact replacement words.

| Line | Old words | Exact new words |
|---|---|---|
| 20 | `it carries a runner, so under GOAL.md it cannot discharge anything; step 2.3 gives a by-hand proof that does not use it.` | `Its sections 2–3 contain hand proofs of nonnegative character coefficients and positive Gram kernels; the presence of a runner does not invalidate them. These are prior results. Our steps 2.2–2.5 give an explicit SU(2) specialization, including strict positivity of every character coefficient.` |
| 24 | `Credit: Ethan Sussman and Levent Alpoge.` | `Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.` |
| 136 | Whole line, beginning `Remark 1.8 (temporal gauge; not used).` | `Remark 1.8 (temporal gauge; not used in 1.1–1.7). Put h_0=1 and h_t=g_0...g_(t-1) for 1<=t<T, pointwise at each vertex, and set W(t)=h_t dot U(t). For fixed temporal links this preserves spatial product Haar measure. Simultaneous covariance changes each slab factor to T_0(W(t),(h_t g_t h_(t+1)^(-1)) dot W(t+1)), where the last next-slice transformation is h_0. The parenthesis is 1 for t<T-1 and H=g_0...g_(T-1) for t=T-1. Thus the weight is the product of the first T-1 ordinary transfer kernels and T_0(W(T-1),H dot W(0)). Holding the first T-1 temporal layers fixed, left Haar invariance gives dH=dg_(T-1); their remaining normalized integrals equal 1. The H integral inserts one P and gives Z_T=Tr(T^T P). Invariant slice insertions are unchanged. No periodic holonomy is set to 1.` |
| 256 | Whole line, beginning `9.1. **Uniform in nothing.**` | `9.1. **The displayed lower bounds are not uniform in volume or coupling.** The kernel floor, the lower bounds on lambda_0 and m, and the reciprocal ground-state bounds degenerate as N or beta tends to infinity. The error prefactors in (6a) and (8a) grow. This describes the estimates, not the actual gap. At each fixed beta>0 and N>=3, compactness, operator positivity and positivity improvement give m>0; the additional argument 5.3–5.7 gives m<infinity. Strict positivity of a continuous kernel alone does not give a positive excited eigenvalue.` |
| 260 | `The $\lambda_1$ of (5) is the maximum over all eight sectors.` | `The lambda_1 of (5) is the maximum, over all eight e, of the norm of R_inv restricted to H_e intersect Omega-perp. In particular the vacuum is removed from the all-plus sector before taking this maximum.` |
| 260 | `on a torus of small physical side the lowest states of the sectors $e\ne(+,+,+)$ are the electric-flux states of 't Hooft and van Baal (**not read**; no claim is made on their energies).` | `no identification of lowest states with those studied by 't Hooft or van Baal is proved here; those sources were not read.` |
| 264 | `equivalently, the lattice Hamiltonian $H_N=-a_N^{-1}\log(\mathsf T_P/\lambda_0)$ on $\mathcal H_{\rm inv}\ominus\mathbb C\Omega$ satisfies $H_N\ge m_\ell$, uniformly in $N$.` | `equivalently, lambda_1(beta(a_N),N)/lambda_0(beta(a_N),N) <= exp(-m_ell a_N), uniformly for N>=N_0. This file does not construct a logarithmic Hamiltonian on the entire invariant space; that formulation additionally needs injectivity and its operator domain.` |
| 266 | `Nothing in Sections 1-8 bears on (G-ell): the bound (5b) gives $m_N\ge e^{-24\beta(a_N)N^3}$, smaller than the required $m_\ell\ell/N$ by a factor $e^{-cN^3}$ for large $N$ (any $\beta(a)$ bounded below).` | `Sections 1–8 give this equivalence but do not prove (G-ell). If beta(a_N)>=beta_*>0 eventually, the ratio of the displayed lower bound exp(-24 beta(a_N)N^3) to m_ell ell/N is at most N exp(-24 beta_* N^3)/(m_ell ell), which tends to zero. This is a limitation of the lower bound, not an upper bound on the actual gap.` |
| 268 | `where neither compactness of $\mathsf T_P$ nor (5b) survives.` | `for which this file constructs no transfer operator and proves no gap. The finite-volume lower bound (5b) tends to zero as N tends to infinity at fixed beta>0.` |
| 274 | Whole line, beginning `10.1. No numbered statement failed.` | `10.1. Statements (1)–(7) and (8a)–(8d) hold for the stated finite-volume domains. Statement (8e) remains cited, not proved. The original temporal-gauge remark 1.8 had its remaining holonomy in reverse order; the corrected remark supplies that part of the row's request. The trace proof 1.1–1.7 does not use the remark.` |
| 276 | Whole line, beginning `10.3. Cited and not rebuilt:` | `10.3. The proof uses ordinary Hilbert-space, integration, topology and finite-dimensional linear-algebra facts without rebuilding their foundations. The compact positive spectral theorem and the positive-kernel simplicity argument are rebuilt in A2–A3. Kolmogorov extension in (8e) is cited and not rebuilt, and no preceding statement uses it. The Schur/Bessel identifications in 0.4 and 2.6 are side facts, not inputs to the numbered proofs.` |
| 277 | Whole line, beginning `10.4. Open, outside this item:` | `10.4. Open, outside this item: (G-ell) and (G-inf). A stronger finite-volume bound already appears in the earlier Codex/Astra note MASS_GAP_CONSTRUCTION_ASTRA.md, section 1.2, on PR #10114 at f76f6c649cff7dffbab664d8976e680e8f287fe9, under .claude/science/toe-ruleset-20261021/agents/ym4d-proof/: m>=-log(1-exp(-6 beta N^3)) in the present lattice-time units. It concerns the same Wilson transfer up to a positive scalar and is credited as prior work. Neither that bound nor (5b) supplies a continuum or volume-uniform gap.` |

## Uses of gap-skeleton names: inventory only

This list reports use sites without evaluating the plan. `gap-skeleton.md` itself was not opened for this check.

| Line | Name or reference used |
|---|---|
| 4 | `(G-ell)` in the status-line reference to §9. |
| 12 | `library/gap-skeleton.md`; its section 1; `(G-ell)`, `(G-inf)`; row 662 as the stated source of those names. |
| 28 | `gap-skeleton`, row 662, in the author's coverage account. |
| 196 | `(G-ell)` in the fixed-volume-bound remark. |
| 260 | `(G-ell)` and `gap-skeleton` in the sector-choice sentence. |
| 262 | `(G-ell)` in the heading and introduction to its proposed uniform statement. |
| 264 | `(G-ell)` as the proposed inequality's label. |
| 266 | `(G-ell)` in the decay equivalence and in the lower-bound comparison. |
| 268 | `(G-inf)` in the heading and twice in the paragraph; `(G-ell)` in the fixed-side comparison; row 662's names. |
| 277 | `(G-ell)` and `(G-inf)` in the open-items list. |

No source, registry, FINISH row, audit file or plan was changed. Only this check report is delivered. No result here supplies a continuum mass gap or a status grant.
