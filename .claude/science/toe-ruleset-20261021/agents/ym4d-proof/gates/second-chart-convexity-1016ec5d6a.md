# Independent second-chart convexity check

Frozen UTC: 2026-10-30T20:30:20.321747+00:00. Supplied immutable commit `1016ec5d6a8886dd8f7bcecb7645d746664384c1`. GH source SHA-256 `0a3057554efc6469a96338fb31a8a0f60f3d1302ef33b00eb05284b96c2ea2e0`. Its first 1335 lines are byte-identical to the preceding checked target.

**PASS for GH64–GH70: the full two-step law conditioned on the ordinary second chart, at terminal I and zero original sources, within the stated coupling-ratio, physical-cut and common producer-domain hypotheses.** No material defect or source repair was identified. The positive lower bound is for the scaled coordinate Hessian; the resulting variance/tail statements concern this actual chart-conditioned law.

1. **Exact density and cold Hessian, GH65–66 (1359–1406).** FU1 and GH60 use the same phase: the normalized first kernel and the first logarithmic Haar Jacobian are inside F_0, while h_N is outside. Thus GH65 retains the full critical action, determinant, both kernel normalizers and both Haar conventions. The simultaneously induced first-level change when fixing the second tree is the already checked Haar quotient, with gauge volume one. No b_1 replacement occurs.

   Independently let q=Q_0 x and S=average ||theta-q||^2 for one kernel. The moving-output numerator contributes `(t/N)(||q-v||^2+S)` to its negative-log Hessian. Differentiating the actual Haar normalizer contributes `-(t/N)c_N(t)S`: apply its invariance along the common path exp(s q) to evaluate the variance term. Their sum is exactly `(t/N)(||q-v||^2+(1-c_N)S)`. The tilted Haar law has 0<c_N<1, without a large-t approximation. Multiplication by sigma^2 gives kappa times this form. The Wilson term is ||d_0 x||^2. Since the pulled-back Haar Jacobian is j_N(a), its term is `N^2/(6u)||a||^2`, not a diagonal in x. At the cold point all first derivatives vanish, so no second-order change-of-coordinates term survives when x=a+E v. This proves the stated GH66.

2. **SAP15, Schur minimization and the retained modes (1408–1435).** Take all coarse plaquettes in SAP15 and zero sources; the full nonnegative fine energy dominates its indicated reader subset. The actual normalized HS convention gives

       E_0(sx,sv)=s^2[||d_0 x||^2+kappa||Q_0 x-v||^2]/(2N)+O(s^3),
       sum_P ||I-V_P(s)||HS^2/N=s^2||d_1 v||^2/N+O(s^3).

   The quadratic mean-spread term cancels in the classical alignment cost: its smooth maximizing tangent is q. Hence the lower bound is precisely `2c_S||d_1 v||^2`, with the displayed SAP constants and factor two. FU's positive fine Hessian makes the stationary-value Hessian its Schur complement, equivalently the infimum of the joint quadratic form over a. E v has zero fine-tree components, so a ->x is a bijection on the fine tree slice. Dropping the nonnegative finite-u spread and Haar terms preserves the bound. The next exact kernel adds at least `lambda kappa||Q_1 a||^2`, and its Haar term is also positive. Therefore

       D^2 B_2(0) >= min(2c_S,c_-) (d_1* d_1+kappa Q_1* Q_1)
                    >= gamma_2 I.

   F11–12 supply this counting-coordinate gap with all crossing, root, winding and colour directions retained. It is not a physical Hamiltonian gap.

3. **Volume-uniform perturbations of the actual prefactor (1439–1471).** CA/CD/FU supply a fixed positive preliminary analytic product domain for A_1 and K_*, with their complete readers. This is distinct from GH60's shrinking domain for the integral identity. FU's uniqueness identifies the phase/precision branches on the overlap; it does not extend GH60 outside its domain. The common NR cover restriction is sufficient for CD5, so no enlargement of R with beta held fixed is needed. After multiplication by sigma^2, CA13 has a uniform rooted budget: the exact vacuum obeys `sigma^2|log z_(kappa u)|<=2N kappa`. CD19's full log-determinant budget is uniform in u and volume, though generally large.

   On a scalar half-polydisc, repeated-index Cauchy estimates give factors `2!(2/b)^2=8/b^2` and `3!(2/b)^3=48/b^3`. A fixed derivative marks its coordinate owner; the remaining one or two summed slots cost at most n_c|S| or (n_c|S|)^2. The rooted exponential norms pay these by B_1(beta),B_2(beta), exactly yielding the displayed absolute row/column bounds. These are not estimates of an extensive scalar by its total norm. CB9/FU's local bounds also apply separately to the next exact kernel and Haar vertices. Their scalar vacuum can be added uniformly after scaling by sigma_1^2; multiplication by lambda<=c_+ then gives the displayed finite-incidence third-derivative budget. Thus the operator difference is bounded by C_B r_1, independently of volume.

4. **The all-cut remainder and GH68 (1473–1491).** The reused GH60 result is the actual full first marginal, including D_all and all original cut sectors. Its T_abs bound at h=sigma has all field-coordinate positions, not just dense directional cancellations. For a fixed row, the two-field part pays the sum over the second coordinate by at most `2E_u/sigma^2`; the one-field part pays at most `E_u/sigma`. Passing from invariant derivatives to exp(a_e) coordinates uses a bounded differential and its first derivative on one link only, so a dimension-dependent C_exp absorbs the component counts without any volume factor or enlarged reader. Consequently the claimed M_R is finite uniformly. The determinant and remainder enter Phi_2 with sigma^2, giving

       D^2 Phi_2 >= [gamma_2-C_B r_1-sigma^2(M_D/2+M_R)]I
                    >= (gamma_2/2)I

   for a volume-independent large-u threshold. Both corrections tend to zero uniformly over the prescribed bounded positive u_1/u interval. No smallness of the unscaled full log determinant is asserted.

5. **Primary convex-boundary theorem and tails (1493–1537).** I checked Kolesnikov–Milman, [arXiv:1310.2526v7](https://arxiv.org/pdf/1310.2526v7), Theorem 1.2(1) on actual PDF page 5 and its case-1 proof on page 18, plus the cached setup/convention excerpts. Its generalized dimension parameter is infinity (unrelated to the gauge-group N). In Euclidean coordinates its curvature tensor is the Hessian of Phi_2/sigma^2. It requires nonnegative second fundamental form and imposes no boundary condition on f; the Neumann condition in the proof belongs to the auxiliary Poisson solution.

   For integer p>=1, `sum_e (||a_e||HS/r_1)^(2p)` is a smooth convex polynomial with nonzero gradient on its unit level. Thus the Omega_p closures have smooth convex boundary, and their open interiors increase exactly to the finite-dimensional product of open balls. Some closures touch the product-ball boundary; this causes no problem because GH62 puts the entire closed chart strictly inside the phase's admitted domain. Normalized dominated convergence proves GH69 with the actual chart normalization.

   Global SU(N) conjugation preserves the full density, terminal I, pinned tree and whole-link balls. The expectation of each a_e must therefore lie in the invariant part of su(N), which is zero. Linear tilts leave the Hessian and domain unchanged. Applying GH69 to <v,a> under every tilt bounds the second derivative of its log moment generating function by `2sigma^2||v||^2/gamma_2`; its zero initial slope gives the stated exponential moment. Each large link has a coordinate of magnitude at least s/sqrt(D). For m distinct links, the selected signed sum has coefficient norm squared m; optimizing Chernoff and summing the (2D)^m choices yields exactly GH70. Independence of the links is neither assumed nor needed.

**Coverage and reuse.** The complete new GH section 16, lines 1337–1537, was read. Actual bounded passages of SAP, F, CA, CD, FU and CB were checked; exact windows and hashes are in the receipt. Unchanged GH56–63, the full-marginal/quotient checks and WR absolute-tensor definitions were reused only in their previously checked scopes. The upstream CA/CD/FU/WR constructions are bounded suppliers, not newly certified in their entirety. The primary PDF was read only in the specified pages/excerpts, not cover to cover. No author route/front or PR records were opened. Requested Astra/max; backend identity is not independently attested. Preflight returned go; direct vocabulary lint is metadata, not mathematical validation.

**Still open:** the full compact posterior's chart-complement probability, original-history connected norms, other terminal centers, physical running, all-depth renewal, non-free four-dimensional SU(N) continuum existence and a positive physical Hamiltonian mass gap.

VERDICT: PASS
