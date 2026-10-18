# Fixed-occupation ladder: independent algebra check

Disposition: PASS for each fixed finite M after making the M-dependent interval truncation explicit below. The adjacent-vertex conclusion is supported; the optional compressed-operator/CCR extension should remain unclaimed. Read /tmp/neutral_fixed_ladder_root.md. No shared/canonical edits.

## Host algebra and hard-core projection

The site-boson device has the correct factors. Takagi-factorizing symmetric Phi reduces B_b^dag=(1/sqrt(2))sum Phi_ij a_i^dag a_j^dag to independent squared-mode creators. The exact vacuum generating function is

 sum_m ||(B_b^dag)^m vac||^2 t^m/(m!)^2
 =det(I-2t rho)^(-1/2)
 =exp[sum_(k>=1)2^(k-1)Tr(rho^k)t^k/k].

The k=1 term is wt. For fixed m, all remaining contributions contain a higher trace, yielding m!w^m+O_m(Tr rho^2) while w remains bounded. This is a finite-degree algebraic identity; no physical canonical bosons have been introduced.

Projecting canonical occupation states to occupations at most one identifies (B_b^dag)^m vac with the spin host product exactly. On the discarded configurations, the number of assignments/matchings is bounded by a constant depending only on m (including bounded occupation factorials). Cauchy-Schwarz converts their squared coefficient norm into an independent-pair probability sum. Each pair's single-site marginal is uniform; the chance of a coincidence between sites from two different pairs is O(1/V). Union over the fixed number of pairs proves discarded norm SQUARED O_m(1/V). Thus the proposed spin-host norm estimate is valid, not just a heuristic pair-overlap argument.

For the mixed source, take a complex directional derivative Phi -> Phi+epsilon Xi while fixing the conjugate variable. The left norm derivative is m times the mixed matrix element. The derivative of the leading term m!w^m is m*m!w^(m-1)Tr(Phi^dag Xi), giving exactly the stated m!w^(m-1)a. Higher traces obey

 |partial_epsilon Tr(rho^k)|<=k||rho||^(k-1)||Phi||_HS||Xi||_HS.

At fixed degree this gives O_m(lambda_max(rho)). Both collision vectors have norm O_m(V^-1/2) when the local source pair has uniform marginals and bounded norm, so their mixed correction is O_m(1/V); the weaker O_m(V^-1/2) also suffices. This step requires the stated translated local source, not an arbitrary Xi concentrated on one site.

## Ray terms and wall projection

A surviving host-only m-product has exactly 2m down spins. Any product with one or more nonzero ray factors has at least 2m+2. Thus its inner product with the host-only vector vanishes. The same count eliminates terms with exactly one ray factor across the two sides of the mixed source inner product, since F adds two spins. Terms remaining across both sides contain at least two ray factors in total and are O_m(eta^2).

The decomposition bound polynomial in total interval length supplies the required multiplication estimate for strings. Uniform conditional ray-length moments then give norm O_m(eta^j) for each j-ray contribution; merely knowing the ray norm eta without those moments would not suffice. Hence the stated norm and mixed-vertex expansions follow, with errors small relative to a~sqrt(delta)log(1/delta).

For fixed m, a union bound over feature pairs gives O_m(1/V) weighted contact probability. Combining it with the finite polynomial decomposition/transition counts proves an O_m(V^-1/2) physical contact norm, both for the incorrect-wall-count projection and the K_(4m) intertwining defect. The bound remains independent of the growing transverse feature separation because contact probabilities count occupied sites and uniform COM translations, not bounding-box area. Higher coefficients act on the full N=4m configuration space, not an assumed closed m-feature manifold; the occupied-length weighted bound controls their action. These arguments genuinely extend the two-feature construction, but their constants are not uniform as m grows.

## Necessary explicit cutoff fix

For a theorem for arbitrary fixed M, replace the inherited ell<L/16 truncation by, for example, ell<L/(16M) for every string. Then the down-spin supports of two M-feature configurations plus fixed-order local modifications cannot cover an entire longitudinal column. This establishes ground-orbit disjointness and the excitation-map isometry uniformly over rungs 0,...,M. Reusing L/16 without an M-dependent restriction would not justify that support argument for large fixed M. The new cutoff discards only exp[-c L/M] ray tails, still superpolynomial for every fixed M; it changes no asymptotic conclusion.

## Actual windows and permitted algebra claim

With that cutoff, the fixed-order residuals, ground-orbit transfer and source-contact comparison give the stated normalized coefficient vertices sqrt(m)lambda a[1+o(1)]. Choose an actual low-energy cutoff above all M window centers. Its source bound has M-dependent constants, which is allowed. The same O_M(lambda^2/delta) projection error is small relative to lambda a for alpha<2/3. The actual windows are mutually disjoint for small lambda, so their normalized vectors are orthonormal, including the exact ground rung.

This proves an adjacent-matrix-element ladder of any FIXED finite length, with additive window centers. It does not prove an autonomous oscillator, eigenstate ladder, or operator CCR. The proposed argument that C1 globally has only grades +/-4 should not be used without proof: in an excited local environment other wall-count changes can occur; the already established contact estimate is the safe way to suppress those effects on these particular trials. Likewise an arbitrary exact ground superposition need not have a definite translation momentum. Neither issue affects the adjacent-vertex proof as written, but both obstruct casually promoting it to a full compressed-operator statement.

The small selected overlap a means most source weight remains outside this ladder. No finite-density, growing-M, lifetime, stable-particle, Lorentz-scalar, or cosmological conclusion follows.
