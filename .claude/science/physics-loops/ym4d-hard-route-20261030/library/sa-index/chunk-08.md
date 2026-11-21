# Chunk 08: lines 8366-9582
Sections: A gap for the classical flat fluctuation precision (8396); The actual quadratic forms and their normalization (8413); Plain and straight averaging (8465); Curvature averaging is a contraction in dimension four (8519); The classical constrained pullback (8556); A fixed-cell Fourier calculation (8619); Flat holonomies and the limit of the conclusion (8733); A constructive upper bound for the flat classical action (8776); Discrete interpolation on the actual centered grids (8791); The exact averaging symbol (8852); An exact lift for the plain constraint (8911); Consequences and scope (8964); Supremum norms of the constructed linear lift (8985); Exponential kernels of the classical flat precision (9060); The two constrained minima are equal (9081); Fourier normalization and the auxiliary covariance (9139); Recovering the gauge-invariant energy (9214); Uniform noncentral alias bounds (9258); Cancellation of the apparent gauge denominator (9318); A uniform strip and its Fourier kernels (9368); The actual next-step precision and its inverse (9432); Finite tori, holonomies, and scope (9536).

| Lines | Name / tag | Kind | What it states (one plain sentence, your words) | Status here | Reads (inputs it uses, by tag or name) | Key phrase |
| --- | --- | --- | --- | --- | --- | --- |
| 8366–8371 | QC18 input smallness, continued | requirement | A supplied near-pure-gauge bound requires the stated small lattice spacing, or a direct real curvature bound with a small complex perturbation. | assumed | QC18; supplied bound on V^s; varpi_c | "(QC18) requires" |
| 8373–8379 | Condition-number losses | estimate | A complex gauge of condition number K gives residual, right-inverse, inclusion and radius bounds with the displayed powers of K and L. | sketched | Complex gauge with condition numbers at most K; preceding chart calculation | "conjugation charges one factor" |
| 8379–8381 | Growing gauge condition number | requirement | Growth of the gauge condition number with a larger window must be charged in estimates. | assumed | Condition-number losses; larger window | "must therefore be charged" |
| 8383–8390 | Limits of the one-step chart calculation | remark | The preceding calculation discharges one-step primitives but leaves many-level response and other named estimates separate. | named open | One-step pivot and Taylor primitives; free precision gap; core and tower estimates; conditional exterior forces; clean-class law | "remain separate assertions" |
| 8386–8388 | Window loss in the later Cauchy radius | requirement | A polynomial window-radius loss in the background/core inclusion must be retained in a later Cauchy radius. | assumed | Background/core inclusion; larger run window | "must still be retained" |
| 8399–8411 | Classical flat-gap scope | hypothesis | The claimed gap concerns the actual contour gauge and plain constraint for the unweighted flat Wilson problem with positive soft gauge coefficient. | assumed | Unweighted Wilson action; flat background; prescribed positive soft gauge coefficient | "are not included in the conclusion" |
| 8415–8430 | CF1; raw cochain conventions | definition | Site and bond differences use unit lattice spacing and counting norms, with d_n denoting the spacing-n version. | definition | Scalar site functions; positively oriented bonds | "set" |
| 8432–8435 | Wilson quadratic normalization | identity | The Wilson action at exp(ita) has quadratic term one half t squared times the squared curl norm. | sketched | Wilson action convention; CF1 | "gives" |
| 8436–8446 | CF2; contour gauge and G | definition | The soft gauge sums contour transport means and G records their arithmetic first-order path sums. | definition | Coordinate-order internal paths; implicit transport means | "Denote this linear functional by" |
| 8442–8451 | CF3; soft-gauge Hessian | identity | The soft gauge at exp(ita) has quadratic term one half t squared times the squared G norm. | sketched | CF2; derivative of implicit contour mean | "Consequently" |
| 8452–8455 | Internal locality and gradient telescoping | identity | The contour gauge involves no crossing pivot and takes a gradient to the endpoint difference. | proved in detail | Internal paths; CF1; G | "Internal paths contain no crossing pivot" |
| 8457–8463 | Canonical Gaussian normalization | identity | The physical scaling makes both quadratic coefficients one and excludes normalization and Haar terms from free precision. | proved in detail | g=theta^(-1/2); action and gauge coefficients theta | "Hence" |
| 8467–8473 | CF4; S_n | definition | S_n averages length-n straight bond sums over the centered block of n^4 sites. | definition | Odd n; centered block B_n(y) | "The raw straight bond average is" |
| 8474–8481 | sigma and CF5; plain derivative | identity | The derivative of the actual plain average is S_L minus the coarse gradient of the mean contour sum sigma. | proved in detail | CF4; gamma; actual outer exponential of closed logarithms | "Direct differentiation" |
| 8476–8484 | Proof of CF5 | proof | The reference-segment derivative cancels its negative contribution in the closed logarithms. | proved in detail | Actual nonlinear block-average formula; sigma | "cancels its" |
| 8486–8496 | q_L, r_L and CF6 | identity | Straight averaging intertwines gradients with site averaging, whereas plain averaging intertwines them with center restriction. | proved in detail | CF5; path telescoping; arithmetic site average q_L; restriction r_L | "Telescoping along paths" |
| 8498–8505 | P^[k], psi_k and CF7 | identity | The iterated plain derivative differs from the length-L^k straight average by a coarse gradient. | proved in detail | CF5; CF6; n=L^k | "This proves (CF7) inductively" |
| 8506–8517 | Proof of CF7 | proof | Centered digit and segment tilings compose straight averages, while CF5 and CF6 keep all corrections gradient-valued. | proved in detail | CF5; CF6; centered block subdivisions | "Here is a direct verification" |
| 8521–8529 | CF8; curl of the straight average | identity | The coarse curl of S_n is the weighted sum of fine curls over n-by-n plaquette sheets. | proved in detail | CF1; CF4; cancellation of interior bonds | "Every interior bond cancels" |
| 8530–8535 | T_n and its weights | construction | T_n is the positive plaquette averaging operator with row sum n^2 and column weight n^-2. | proved in detail | CF8; partition into centered blocks | "Each row has sum" |
| 8537–8548 | CF9; curvature contraction proof | proof | Weighted Cauchy and the row-column counts prove that T_n contracts counting l2 norms, including on periodic lattices. | proved in detail | T_n; dimension four; weighted Cauchy | "weighted Cauchy gives" |
| 8549–8554 | CF10; cf:curvature-contraction | estimate | The curl of the iterated plain average is bounded by the fine curl uniformly in the number of levels. | proved in detail | CF7; CF8; CF9; curl of a gradient vanishes | "Taking curls of (CF7) therefore proves" |
| 8558–8563 | CF11; E_k | definition | E_k is the least fine curl energy among fields with prescribed iterated plain average. | definition | P^[k]; current bond data a | "define" |
| 8564–8572 | Face-supported right inverse | construction | Assigning coarse face values to crossing fine bonds and zero internally constructs a right inverse of P^[k]. | proved in detail | Centered subdivisions; nonlinear group lift with internal bonds I | "Its derivative is a right" |
| 8574–8581 | Existence and quadraticity of E_k | proof | Closed affine images or quotient normal equations give an attained quadratic minimum without a uniform inverse bound. | proved in detail | CF11; finite dimensionality; ker P^[k] intersect ker d | "its point nearest" |
| 8582–8588 | CF12; classical lower bound | estimate | The constrained classical energy dominates the squared coarse curl norm. | proved in detail | CF10; CF11 | "applied to every admissible lift" |
| 8590–8604 | Identification with a background Hessian | proof | An exact stationary background lift has classical Hessian E_k because the flat first variation vanishes. | proved conditionally | Twice differentiable exact background lift; linearized constrained stationarity; vanishing bare first variation; CF11 | "A twice differentiable exact background lift" |
| 8597–8604 | Flat constraint correction and lower-bound scope | remark | The flat second-order constraint correction vanishes and the lower bound holds even for arbitrary exact differentiable lifts. | proved conditionally | Zero first variation at identity; exact differentiable lift; CF12 | "Even an arbitrary exact differentiable lift" |
| 8606–8617 | CF13; A_k^flat | definition | The actual free nonpivot precision is E_k pulled back by the flat pivot inclusion plus the contour-gauge quadratic form. | definition | Actual flat pivot inclusion C; E_k; G; CF12 for displayed inequality | "characterized by" |
| 8619–8636 | CF14; fixed-cell Bloch construction | construction | A cell field extends by Bloch phases in a fixed free space of dimension 4L^4−4. | definition | Side-L cells; current bond coordinates; CF5 | "extend a cell field by" |
| 8638–8645 | Flat pivot coefficient | identity | Each plain constraint has a single own-cell pivot coefficient L^-3 without a Bloch phase. | proved in detail | Middle crossing pivot; L^4 parallel segments; L occurrences | "since exactly" |
| 8646–8658 | CF15; C(p) | construction | Solving the pivot block constructs a Laurent-polynomial inclusion with free restriction identity and range ker P(p). | proved in detail | h_0; iota; pivot block L^-3 I_4; P(p) | "follows by solving each pivot equation" |
| 8660–8664 | CF16; B(p) | definition | B(p) is the finite Hermitian comparison matrix obtained by pulling curl and contour gauge back to free coordinates. | definition | C(p); d_p; G | "Define the Hermitian finite matrix" |
| 8665–8688 | No-zero-vector proof for B(p) | proof | Zero curl and contour sums kill internal bonds, and the plain constraint then kills constant crossing-face values. | proved in detail | CF14; CF15; plaquette swaps; connected transverse face grid | "killing every crossing bond as well" |
| 8690–8703 | Explicit closed-field Fourier decomposition | proof | Fine Fourier modes express every closed field as a gradient except the constant harmonic mode, already killed by the local argument. | proved in detail | Finite geometric-series orthogonality; t_mu; no-zero-vector proof | "no zero-frequency mode has been silently omitted" |
| 8705–8715 | CF17; uniform cell gap | estimate | B(p) has a positive lower bound c(L) for every real Bloch parameter. | proved in detail | Continuity of B(p); compact Bloch torus; trivial kernel | "contradicting the" |
| 8705–8711 | Compactness proof of CF17 | proof | A sequence approaching zero Rayleigh quotient would converge to a forbidden unit null vector. | proved in detail | Fixed cell dimension; compact parameter and unit-vector spaces | "Their limit would be a unit" |
| 8717–8731 | CF18; cf:classical-flat-gap | estimate | The actual flat free precision has a lower bound independent of torus volume and the number of finer levels. | proved in detail | CF13; CF16; CF17; discrete Fourier transform; three color copies | "Parseval and (CF17)" |
| 8717–8723 | Fourier proof of CF18 | proof | The unitary transform in block indices decomposes the comparison form into the uniformly positive matrices B(p). | proved in detail | Geometric-series identity; CF13; CF16; CF17 | "It converts the comparison form" |
| 8735–8760 | Real flat-holonomy extension | proof | Block-constant flattening and simultaneous unitary holonomy decomposition reduce flat axial backgrounds to shifted Bloch parameters with the same gap. | proved in detail | Real flat background in prescribed block axial representative; CF9; CF17 | "all these shifted sets satisfy the same" |
| 8762–8770 | Limits and remaining comparisons after CF18 | requirement | Uniform upper bounds, dressed decay and quantitative comparisons for currents, signed profiles, counterterms and complex or non-Abelian perturbations do not follow from the flat gap. | named open | CF18; curved constraints; signed layer profiles; counterterm arrays; non-Abelian perturbations; enlarged complex decoupling parameters | "need their own quantitative comparison" |
| 8779–8789 | WI1; unweighted classical value | definition | E_k is again the constrained minimum for the raw derivative of the iterated plain average on odd centered grids. | definition | n=L^k; odd L; P^[k]; same unweighted classical Gaussian value as flat-gap calculation | "put" |
| 8793–8799 | WI2; nodal hats and interval indicators | definition | The functions phi_n and beta_n are the discrete triangular hat and length-n interval indicator. | definition | Fine integer sites; coarse sites nm | "Write" |
| 8800–8804 | Periodization and partition identities | identity | Periodized hats and intervals partition unity, and the total mass of a hat is n. | proved in detail | WI2; two linear pieces of phi_n | "follow by summing the" |
| 8805–8809 | WI3; hat difference | identity | A unit difference of the nodal hat equals the difference of two interval indicators divided by n. | proved in detail | WI2 | "Also" |
| 8810–8825 | WI4; I_0, I_1, I_2 | construction | Tensor products of hats and indicators interpolate coarse site, raw bond and raw plaquette values onto the fine grid. | definition | WI2; coarse arrays indexed by starting node; raw d_n convention | "Define interpolation of sites, bonds and plaquettes by" |
| 8826–8836 | WI5; cochain interpolation identities | identity | Discrete interpolation commutes with the site and bond exterior differences. | proved in detail | WI3; WI4; reindexing coarse nodes | "proves" |
| 8831–8836 | Proof of the bond identity in WI5 | proof | Differentiating a transverse hat yields the oriented coarse plaquette boundary coefficients. | proved in detail | WI3; I_1; I_2; curl orientation | "This proves the" |
| 8838–8850 | WI6; plaquette interpolation contraction | estimate | I_2 contracts counting l2 norms because its row and column sums are n^-2 and n^2. | proved in detail | WI4; partition identities; dimension four; weighted Cauchy | "Weighted Cauchy therefore gives" |
| 8854–8859 | Straight average on centered grids | definition | S_n averages length-n straight fine bond sums over centered blocks. | definition | Centered B_n(y); raw bond values | "The raw straight average is" |
| 8860–8877 | WI7; exact one-dimensional coefficients | identity | Both longitudinal counts and transverse hat averages give the same central and neighboring coefficients a_0 and a_1. | proved in detail | WI2; WI4; S_n; h=(n−1)/2 | "both have" |
| 8878–8882 | Counting proof of WI7 | proof | Triangular overshoot counts and the two linear hat sums give the three averaging coefficients. | proved in detail | Longitudinal count; transverse hat sum | "give the same two triangular numbers" |
| 8884–8892 | WI8; scalar convolution A_n | identity | S_n I_1 equals the product of four identical-form one-dimensional coarse convolution operators. | proved in detail | WI4; WI7; translations T_lambda | "identical one-dimensional coefficients just computed show" |
| 8893–8900 | WI9; scalar symbol | estimate | Each one-dimensional symbol lies between one half and one for real frequency. | proved in detail | WI7; WI8; cosine bound | "Each one-dimensional symbol is" |
| 8901–8906 | WI10; l2 inverse bound | estimate | The scalar averaging convolution has inverse l2 norm at most 16. | proved in detail | WI9; Fourier transform or unitary-shift quadratic-form bound | "proves" |
| 8907–8909 | Commutation with coarse differences | identity | The scalar convolution and its inverse commute with every coarse difference on sites, bonds and plaquettes. | proved in detail | Commuting coarse shifts; WI8; WI10 | "All shifts commute" |
| 8913–8922 | WI11; exact straight lift w_0 | construction | The field I_1 A_n^-1 a is an exact straight lift with curl norm at most 16 times the coarse curl norm. | proved in detail | WI5; WI6; WI8; WI10 | "This is an exact straight lift" |
| 8923–8936 | WI12; plain and gradient identities | identity | The plain average differs from S_n by a gradient and maps fine gradients to gradients of center restrictions. | proved in detail | Actual closed-logarithm formula; P_L=S_L−d_L sigma; internal contour telescoping | "Iterating proves the second identity" |
| 8929–8936 | Proof of WI12 | proof | Differentiation proves the one-step identities and induction combines straight averages while preserving gradient corrections. | proved in detail | Closed-logarithm differentiation; composition of straight averages; center restriction | "proving the first by induction" |
| 8938–8945 | WI13; exact plain lift w | construction | Correcting w_0 by the interpolated gradient of minus psi_k(w_0) enforces the plain constraint without changing curl. | proved in detail | Nodal identity r_n I_0=1; WI11; WI12 | "The gradient correction has no classical" |
| 8945–8950 | WI14; upper energy bound | estimate | E_k(a) is at most 256 times the squared coarse curl norm. | proved in detail | WI11; WI13; E_k minimum | "We have proved" |
| 8951–8958 | WI15; wi:energy-comparison | estimate | The classical energy lies between one and 256 times the squared coarse curl norm. | proved in detail | WI14; exact curvature average T_n; row and column counts; weighted Cauchy | "The complementary lower bound follows" |
| 8951–8954 | Proof of the lower half of WI15 | proof | The exact curvature average contracts by weighted Cauchy, bounding every admissible lift from below. | proved in detail | T_n; row sum n^2; column weight n^-2 | "The same weighted" |
| 8959–8962 | n=1 and zero-frequency scope | remark | All interpolation statements include n=1 and invert a convolution that stays positive on constants. | proved in detail | WI2; WI4; WI8; WI9 | "All statements include" |
| 8966–8975 | Local norms for the flat precision | estimate | The pivot basis, curl and internal contour norms give bounds of orders L^4, 24 and L^5, with GC=G iota. | sketched | Actual local pivot basis; row and column bounds; four-dimensional curl; absence of internal pivots | "from its row and column bounds" |
| 8975–8983 | WI16; precision upper bound | estimate | The flat free precision is bounded above by C L^8 independently of finer levels and volume. | proved conditionally | WI14; stated local norm bounds at 8969–8974; actual flat precision formula | "these bounds" |
| 8981–8983 | Two-sided precision consequence | remark | WI16 and the separate flat-gap theorem give uniform upper and lower precision bounds. | proved in detail | WI16; CF18, separate flat-gap theorem | "Together with the separate flat-gap theorem" |
| 8987–8999 | WI17; supremum inverse and straight-lift bounds | estimate | The inverse convolution has supremum norm at most 16 and w_0 has supremum norm at most 16/n times that of a. | proved in detail | WI7; WI8; Neumann series; I_1 row sum 1/n | "Its inverse Neumann" |
| 8987–8993 | Neumann-series proof of WI17 | proof | The off-diagonal part in each direction has norm below one and four inverse bounds of two multiply to 16. | proved in detail | a_0; a_1; commuting translations | "Multiplying the four commuting" |
| 9001–9010 | WI18; recursive choice of psi_j | construction | Starting from psi_0=0, the scalar correction is recursively restricted to centers and reduced by the next contour average. | proved in detail | WI12; P_L=S_L−d_L sigma_L; S_(L^j); r_L | "There is an explicit choice" |
| 9011–9019 | Scalar-correction supremum bound | estimate | Path lengths and a geometric sum bound psi_k by 32 times the supremum norm of a. | proved in detail | WI17; WI18; sigma_L norm at most 2(L−1); S_(L^j) norm L^j | "The geometric sum yields" |
| 9021–9028 | WI19; wi:linear-lift-sup | estimate | The correcting gradient and the final exact lift have supremum bounds 64/n and 80/n times the data norm. | proved in detail | WI5; WI13; WI17; bound on psi_k | "Consequently" |
| 9029–9035 | WI20; curl supremum bound | estimate | The constructed lift has curl supremum norm at most 16/n^2 times the coarse curl supremum norm. | proved in detail | Commutation of A_n^-1 with curl; WI5; WI17; I_2 row sum n^-2 | "also give" |
| 9036–9037 | Linear-lift scope | remark | The supremum estimates concern the specified right inverse rather than a minimizing response. | definition | WI19; WI20; explicitly constructed linear lift | "They are not estimates for a minimizing response" |
| 9039–9045 | Twisted interpolation and energy comparison | proof | Unitary character periodization preserves the interpolation estimates and inverse bounds for real flat holonomies. | proved in detail | Universal cover; commuting unitary twists; WI9; WI10; absolute weight counts | "absolute row and column" |
| 9047–9054 | Further kernel and comparison inputs | requirement | Exponential kernels and applications beyond the specified flat lift use separate kernel and actual-operator comparison results. | assumed | ch:flat-exponential-kernels; corresponding actual-operator comparison propositions | "use the corresponding actual-operator comparison" |
| 9063–9079 | Classical kernel problem and normalization | hypothesis | The calculation concerns raw bond coordinates and the canonically scaled unweighted classical precision, with three identical color copies at identity. | assumed | Odd L; n=L^k; Wilson normalization; g=theta^(-1/2); theta g^2=1 | "the real" |
| 9065–9067 | Analytic input beyond the gap | requirement | Kernel decay requires the uniform complex-strip argument supplied below in addition to the flat spectral gap. | named open | Exact symbols; flat gap; proof below | "A spectral gap by itself" |
| 9083–9090 | FX1; straight average | definition | S_n averages raw straight fine bond sums over centered blocks using starting-site coordinates. | definition | P^[k]; B_n(0); fine field w | "The straight average is" |
| 9091–9106 | FX1a; path multiset, gamma, G and sigma | definition | Oriented coordinate-order shortest paths with prescribed multiplicities define the contour mean derivative, gauge matrix and block mean. | definition | ch:block-average-pivot-chart; path multiset G_L(y,x); orientation signs; gamma_(y,y)=0 | "In positive bond coordinates set" |
| 9106–9114 | FX2; iterated plain and gradient identities | identity | The iterated plain derivative differs from S_n by a gradient and the two averaging maps intertwine gradients with restriction and averaging respectively. | proved in detail | FX1a; P_L=S_L−d_L sigma; iteration; r_n; q_n | "Iteration gives" |
| 9115–9118 | Surjectivity of site maps | proof | Assigning center values and using block-constant functions respectively show that restriction and site averaging are onto. | proved in detail | r_n; q_n; finite linear cochains | "Both site maps are onto" |
| 9120–9129 | FX3; equality of constrained minima | identity | The plain and straight constrained curl-energy minima coincide. | proved in detail | FX2; surjectivity of r_n and q_n; gradient corrections | "the same curl" |
| 9120–9124 | Gradient-correction proof of FX3 | proof | Fine gradients correct either constraint to the other without affecting curl. | proved in detail | FX2; q_n f=psi_k(w); r_n f=−psi_k(w) | "Conversely" |
| 9130–9137 | Feasibility and attainment of the minima | proof | The filter's central alias and constant lifts ensure feasibility, and finite-dimensional projection gives both minima. | proved conditionally | Filter calculation below, FX6; nonzero central alias; constant fine lift; curl-null quotient | "Finite dimensional projection" |
| 9141–9148 | FX4; unitary Fourier transforms | definition | Fine and coarse transforms use normalizations (n s)^-2 and s^-2 on their respective four-dimensional tori. | definition | Coarse period s; fine period n s | "Use the unitary transforms" |
| 9149–9157 | Aliases and FX5; b_n and B_n | definition | Fine aliases are indexed by the centered integer cube, and normalized sine ratios define block and segment filters. | definition | p; n; I_n; h=(n−1)/2 | "Put" |
| 9158–9170 | FX6; exact bond filter | identity | The straight filter includes its starting-site phase and a normalized alias sum with factor n^-2. | proved in detail | FX1; FX4; FX5; centered block and straight segment sums | "Thus the exact filter" |
| 9172–9185 | FX7; auxiliary Feynman covariance | construction | The coarse auxiliary covariance is diagonal and sums squared filter amplitudes divided by the positive fine Laplacian symbol. | proved in detail | Fine Feynman form; lambda; p nonzero; FX6; constrained positive quadratic minimization | "Its symbol is component-diagonal" |
| 9187–9199 | FX8; analytic alias factors | definition | The functions q, f and s express the complex alias filter factors and scaled Laplacian denominators with removable ratios filled in. | definition | Fine aliases; complex p | "For complex continuation define" |
| 9199–9207 | FX9; fx:alias-covariance | identity | The analytic covariance is the sum of f_(mu,m)/s_(n,m), obtained by pairing filters at opposite frequencies. | proved in detail | FX6; FX7; FX8 | "giving exactly" |
| 9208–9212 | Normalization proof of FX9 | proof | Multiplying opposite-frequency filters and rescaling the fine Laplacian verifies all powers of n without holomorphically conjugating variables. | proved in detail | FX6; FX8; s_(n,m)=n^2 lambda | "This checks every power of" |
| 9216–9221 | t^+ and t^- conventions | definition | The coarse forward and backward difference symbols are analytically independent holomorphic expressions off real momenta. | definition | Real and complex p; starting-site phases | "In analytic formulas below" |
| 9223–9229 | Fine Hodge identity and gradient removal | identity | At nonzero frequency, subtracting a fine gradient produces a divergence-free field without changing curl and changes its average only by a coarse gradient. | proved in detail | Elementary Hodge identity; lambda; FX2; onto q_n | "Subtracting a fine gradient" |
| 9230–9236 | FX10; Feynman minimization over coarse gauges | identity | The curl minimum equals the auxiliary Feynman quadratic value minimized over one coarse gradient parameter. | proved in detail | FX3; FX7; fine Hodge identity; onto q_n | "It follows that" |
| 9237–9242 | Two-inequality proof of FX10 | proof | A divergence-free curl minimizer gives one inequality and a gradient-corrected Feynman minimizer gives the other. | proved in detail | Curl and Feynman minimizers; FX2; gradient corrections | "the two inequalities use different simple steps" |
| 9244–9251 | FX11; gauge-invariant precision symbol | identity | Solving the scalar gauge minimization gives the Schur-complement expression for E_n. | proved in detail | FX10; diagonal D_n; t^+; t^- | "Solving the scalar minimum gives" |
| 9252–9256 | Zero-mode definition | definition | E_n(0) is zero because a constant coarse one-form has a constant fine lift a/n with zero curl. | definition | Constant fine lift; classical energy; forthcoming holomorphic extension | "We accordingly set" |
| 9260–9267 | Complex alias box and FX12 | estimate | For a nonzero alias component, the scaled sine denominator is bounded below by a constant times one plus its index magnitude. | proved in detail | Small rho; extended real Brillouin box; imaginary width rho | "To see this" |
| 9269–9276 | Proof of denominator and sinc bounds | proof | Real sine bounds, the complex sine identity and zero-free sinc ratios control both noncentral and central components uniformly. | proved in detail | FX8; fixed sine-argument interval; small rho | "zero-free neighborhood" |
| 9277–9280 | FX13; alias filter decay | estimate | Each alias ratio is bounded by C divided by one plus its component index magnitude uniformly in n. | proved in detail | FX12; bounded numerator; central sinc bound | "Hence, uniformly" |
| 9282–9294 | FX14; noncentral denominator separation | estimate | Every noncentral scaled Laplacian denominator has real part at least c times one plus the squared alias norm. | proved in detail | Real part of sine squared; FX12; sufficiently small rho | "Decrease" |
| 9282–9288 | Proof of FX14 | proof | The imaginary displacement costs only order rho squared while the real sine sum supplies order squared alias norm. | proved in detail | FX8; sine-squared real-part inequality | "the imaginary displacement" |
| 9296–9303 | FX15; central term and remainder | definition | D_(mu,n) splits into the central term f_mu/s_n and the noncentral alias remainder R_(mu,n). | definition | FX8; FX9; central q_nu; Q_n; f_mu; s_n | "Write" |
| 9304–9310 | FX16; summable alias majorant | estimate | Noncentral summands are bounded by a fixed absolutely summable product of inverse powers of alias indices. | proved in detail | FX13; FX14; FX15 | "absolutely summable" |
| 9311–9316 | Holomorphy and derivative bounds for R | proof | The summable majorant and Cauchy estimates bound the remainder and all fixed-order derivatives uniformly, with R(0)=0 and an empty sum at n=1. | proved in detail | FX16; smaller complex box; Cauchy estimates; noncentral filter zeros | "holomorphic and uniformly bounded" |
| 9320–9327 | FX17; h_mu and H_n | definition | Inverting the central numerator plus s_n times the remainder defines h_mu and its diagonal matrix H_n. | definition | FX15; near-origin q_nu, s_n and f_mu expansions | "Define" |
| 9328–9329 | Local holomorphy of H_n | estimate | H_n is uniformly bounded and holomorphic on a fixed sufficiently small complex polydisc. | proved in detail | FX17; f_mu=1+O(p^2); bounded R; s_n=O(p^2) | "holomorphic and uniformly bounded" |
| 9329–9338 | FX18; exact filter cancellation | identity | The sum of t_mu^+ t_mu^- divided by f_mu equals s_n/Q_n exactly, including removable values. | proved in detail | FX8; central q_mu; Q_n; t^+; t^- | "It follows directly by canceling the numerator" |
| 9340–9350 | FX19; factorization F_n=s_n J_n | identity | The apparent gauge denominator factors through s_n and a uniformly nonzero analytic factor J_n near the origin. | proved in detail | FX17; FX18; remainder R; J_n(0)=1 | "It is therefore nonzero" |
| 9351–9358 | FX20; fx:origin-cancellation | identity | The precision has a uniformly holomorphic expression with only the nonvanishing denominator J_n. | proved in detail | FX11; FX17; FX19; D_n^-1=s_n H_n | "has the holomorphic form" |
| 9351–9363 | Proof of full complex-cone cancellation | proof | Factoring the original denominator as s_n squared times J_n removes the entire complex zero cone and yields an order-p-squared symbol. | proved in detail | FX19; FX20; meromorphic-domain equality | "This removes the whole complex zero cone" |
| 9362–9366 | Ward identity and n=1 check | identity | The resulting symbol annihilates t^+ and reduces at n=1 to the ordinary curl quadratic form. | proved in detail | FX19; FX20; n=1 empty remainder | "This checks the normalization and phases" |
| 9370–9384 | FX21; real denominators away from zero | estimate | Away from a fixed origin neighborhood, the diagonal covariance and scalar gauge denominator have uniform positive lower bounds. | proved in detail | Positive central q_nu; s_n comparable to squared p; FX15; nonnegative real aliases | "The second inequality uses" |
| 9386–9395 | Complex continuation away from zero | proof | Bounds on central and alias terms and their derivatives preserve separated denominators on a fixed thin complex neighborhood. | proved in detail | FX12–FX16; FX21; Cauchy estimates; FX11 | "quantitative perturbation" |
| 9397–9406 | FX22; uniform analytic strip | estimate | The classical energy symbol is holomorphic and uniformly bounded on one complex strip independent of n. | proved in detail | Origin formula FX20; away-from-zero formula FX11; overlap agreement | "Together they give" |
| 9397–9400 | Gluing proof for FX22 | proof | Choosing the away-from-zero radius inside the origin polydisc lets the two exact formulas agree on overlaps. | proved in detail | FX20; FX11; exact algebraic derivation; continuity | "on their overlaps by continuity" |
| 9407–9411 | Periodicity of the analytic symbol | proof | A coarse momentum shift reindexes aliases and preserves the periodic filters, denominators and analytic continuation. | proved in detail | FX9; FX11; fine-frequency periodicity | "reindexes the aliases" |
| 9413–9418 | FX23; infinite-lattice kernel K_n | definition | The infinite-lattice energy kernel is the inverse Fourier transform of the full classical energy symbol. | definition | FX22; periodic E_n | "Define its infinite-lattice kernel by" |
| 9419–9426 | FX24; exponential energy-kernel bound | estimate | The energy kernel is bounded by M_E times exp(−eta' times the l1 distance). | proved in detail | FX22; FX23; eta'<eta; periodic contour shift | "Periodicity cancels the vertical faces" |
| 9419–9422 | Contour-shift proof of FX24 | proof | Shifting each contour in the sign of its lattice coordinate produces exponential decay while canceling vertical faces. | proved in detail | FX22; FX23; periodicity | "shift the" |
| 9427–9430 | Diagonal terms, weighted sums and Ward identity | remark | The full Fourier kernel retains diagonal terms and has uniform weighted row sums with its already established zero value and Ward identity. | proved in detail | FX20; FX24; full Fourier definition FX23 | "no contact term is added afterward" |
| 9434–9443 | FX25; cell transform U and inverse V | construction | Finite Fourier matrices fold current-lattice frequencies into the next-step side-L cell using analytic inverse phases. | definition | Block momentum P; cell r; aliases j; zeta_j=(P+2 pi j)/L | "analytic inverse are" |
| 9444–9448 | Inversion and strip bounds for U,V | proof | Finite geometric sums prove inverse identities, while bounded cell phase factors give strip norm bounds. | proved in detail | FX25; fixed L; bounded r/L | "Finite geometric-series orthogonality proves" |
| 9449–9457 | FX26; folded energy symbol | construction | Conjugating the aliased energy symbols by U and V defines a periodic uniformly holomorphic cell precision. | proved in detail | FX22; FX25; alias permutation | "Periodicity again follows by the alias permutation" |
| 9459–9466 | Actual pivot basis and analytic transpose | definition | The actual flat pivot map has fixed Laurent-polynomial entries and C-sharp is its opposite-momentum transpose. | definition | Middle-pivot block L^-3 I_4; free restriction identity; G from FX1a | "Define" |
| 9467–9475 | FX27; actual nonpivot precision A_n | definition | The actual next-step precision pulls back the folded classical action and the contour gauge through the pivot basis. | definition | FX26; C-sharp; C; FX1a; FX3 | "The exact classical free nonpivot precision is" |
| 9477–9496 | Independent real-gap proof | proof | Curvature contraction and the trivial kernel of the fixed-cell curl-plus-contour form yield a uniform positive gap for A_n. | proved in detail | FX1; FX27; weighted Cauchy; internal-path argument; plain constraint; compact Bloch torus | "This proves" |
| 9497–9505 | FX28; complex perturbation estimate | estimate | A fixed strip can be narrowed so that the complex perturbation of A_n has norm less than half its real gap. | proved in detail | FX22; FX25; FX27; Cauchy derivative bound M_A(L); real gap c(L) | "Choose its width so that" |
| 9507–9514 | FX29; analytic bounded inverse | estimate | The inverse nonpivot precision is holomorphic and bounded by 2/c(L) on one strip independent of n. | proved in detail | FX28; real gap; Neumann series | "The Neumann series around the real positive matrix then proves" |
| 9516–9527 | FX30; fx:flat-kernel-bounds | estimate | The actual flat nonpivot precision and covariance kernels decay exponentially with current-lattice bond distance uniformly in finer levels. | proved in detail | FX23–FX24 contour argument; FX27–FX29; fixed cell size | "Contour shifting" |
| 9516–9520 | Proof converting strip bounds to bond kernels | proof | Exponential block Fourier coefficients convert to bond-coordinate decay with only fixed changes in constants. | proved in detail | Analytic precision and inverse; fixed L cell | "only changes the" |
| 9528–9534 | Covariance notation and weighted sums | remark | The covariance is distinct from the rectangular pivot map, and exponential weighted row and column sums follow from shell counting. | proved in detail | FX30; fixed-dimensional lattice shells; bond-distance equivalence | "sums follow by summing" |
| 9538–9548 | FX31; exact torus image sum | identity | The finite-torus kernel is the sum of the infinite block kernel over period translates. | proved in detail | Sampled Fourier symbols; discrete orthogonality; absolute convergence; block period s_b | "discrete Fourier" |
| 9549–9556 | Periodic decay and image errors | proof | The image sum yields uniform periodic-distance decay and exponentially small nonwrapping image errors for both precision and inverse. | proved in detail | FX31; exponential kernel bounds; sampled positive precision and inverse | "The image sum preserves an exponential bound" |
| 9558–9566 | Holonomy extension of kernel bounds | proof | Block-constant unitary flattening and character decomposition give shifted momenta or unit-modulus image weights without changing absolute kernel bounds. | proved in detail | Real flat holonomies in block axial representative; commuting adjoint holonomies; FX31 | "All absolute kernel bounds remain" |
| 9568–9573 | Scope of decay and the massless auxiliary covariance | remark | Exponential decay concerns the constrained classical nonpivot problem and does not assert auxiliary massless decay or a physical Yang–Mills mass gap. | named open | D_n; FX30; actual soft gauge | "is not" |
| 9574–9577 | Actual-operator perturbation comparisons | requirement | Signed profiles, counterterms, nonzero currents, non-Abelian backgrounds and enlarged complex decoupling require separate actual operators and uniform perturbation estimates. | named open | Actual operators for the five named extensions; uniform perturbation estimates | "Those require their actual operators" |

## Forward and backward references

References within this chunk are included alongside references outside it; no external target was read.

- 8367–8369 → QC18, the prior physical-chart smallness condition.
- 8373–8379 → The previously defined quadratic residual, h_V, C_V and physical nonpivot radius, now modified for condition number K.
- 8383–8390 → The preceding one-step pivot/Taylor calculation; later many-level response, background/core inclusion and Cauchy radius; separate free precision gap, all-window core and tower estimates, conditional exterior forces and clean-class law.
- 8399–8405 → The actual soft contour gauge and nonlinear block average, distinguished from divergence projection and straight averaging.
- 8442–8446 → The implicit mean of coordinate-order internal transports, whose derivative defines gamma and G here.
- 8457–8463 → The physical step's prescribed g and theta, and other parts of the step containing normalization constants and the Haar Jacobian.
- 8476–8484 → The actual outer exponential of closed logarithms and its reference straight segment; CF5 records the differentiated formula.
- 8486–8494 → CF5 and contour telescoping provide CF6.
- 8498–8517 → The plain k-fold nonlinear average; CF5 starts the induction for CF7 and CF6 propagates gradient corrections.
- 8521–8535 → CF4's straight average supplies CF8 and T_n.
- 8549–8553 → CF7 and the preceding contraction argument CF8–CF9 supply CF10 (cf:curvature-contraction).
- 8564–8572 → The nonlinear group lift with identity internal bonds and its exact averaging property supply a right inverse for P^[k].
- 8574–8585 → CF11 defines the minimum; CF10 gives CF12.
- 8590–8604 → A twice differentiable exact background lift and linearized constrained stationarity identify CF11 as its Hessian; the nonlinear background theorem is explicitly not assumed for defining CF11.
- 8606–8617 → The actual flat pivot inclusion and CF12 give the free precision formula and comparison CF13.
- 8635–8636 → CF5 defines the finite plain constraint matrix P(p).
- 8654–8658 → Solving pivot equations proves CF15 and identifies it with the prior physical-chart pivot map at the flat field.
- 8665–8667 → CF14 extends the field in the kernel proof.
- 8683–8686 → CF15 makes the common crossing-face value vanish.
- 8701–8703 → The preceding local kernel argument also eliminates the harmonic zero mode.
- 8705–8715 → The preceding trivial-kernel argument and compactness prove CF17.
- 8717–8726 → CF13 decomposes into CF16; Parseval and CF17 prove CF18 (cf:classical-flat-gap).
- 8755–8760 → CF9 remains valid with unitary boundary phases, and CF17 covers all shifted Bloch parameters.
- 8762–8770 → CF18 alone supplies neither full background nor interacting Gaussian-law conclusions; separate quantitative comparisons are required.
- 8779–8785 → The flat-gap calculation's unweighted classical Gaussian value and actual P^[k] are reused as WI1.
- 8826–8836 → WI3 and WI4 prove WI5 with the previously specified curl orientation.
- 8848–8850 → The curvature-averaging calculation is recalled for the dimension-four cancellation in WI6.
- 8884–8891 → WI4 and the WI7 one-dimensional counts prove WI8.
- 8901–8909 → WI9's scalar lower bound gives WI10 and difference commutation.
- 8915–8920 → WI5, WI6, WI8 and WI10 imply WI11.
- 8923–8936 → The actual closed-logarithm formula and iterated straight-average composition prove WI12.
- 8938–8946 → WI11–WI12 prove exactness of WI13; the lift amplitude bound is promised below, at WI17–WI20.
- 8946–8958 → The constructed lift proves WI14; the exact curvature average and weighted Cauchy supply the complementary lower bound in WI15 (wi:energy-comparison).
- 8966–8968 → The earlier actual flat precision formula CF13 is reused.
- 8969–8979 → The local pivot basis's row/column bounds and WI14 supply WI16.
- 8981–8983 → The separate flat-gap theorem, CF18, combines with WI16.
- 9001–9009 → The scalar in WI12 is explicitly constructed using P_L=S_L−d_L sigma_L and center restriction.
- 9021–9027 → WI5 and the correction in WI13 give WI19 (wi:linear-lift-sup), using the scalar bound just proved.
- 9029–9034 → WI17 and the I_2 row sum give WI20.
- 9043–9045 → WI9–WI10 retain their bounds for shifted Bloch parameters.
- 9049–9050 → Section ch:flat-exponential-kernels supplies exponential flat-precision kernels, in this chunk at 9060–9577.
- 9050–9054 → Corresponding actual-operator comparison propositions are inputs for minimizing/nonlinear backgrounds, complex cores, tower substitutions, signed profiles, nonzero currents, counterterms and complex decoupling arrays.
- 9065–9067 → The proof below supplies a uniform complex strip before using the flat gap.
- 9091–9095 → Section ch:block-average-pivot-chart defines the actual one-step map and its prescribed shortest-path multiset.
- 9106–9113 → Differentiating that actual map and iterating the one-step identities gives FX2.
- 9120–9129 → FX2 and onto site maps prove FX3.
- 9130–9135 → The filter calculation below, FX5–FX6, supplies nonemptiness through its central alias; projection then supplies minima.
- 9136–9137 → The actual soft gauge is added later on the current one-step fiber, in FX27.
- 9158–9166 → FX1, FX4 and FX5 yield FX6's exact filter and alias normalization.
- 9183–9185 → Positive constrained minimization of the fine Feynman form is an alternative derivation of FX7.
- 9199–9212 → FX6 and FX8 give FX9 (fx:alias-covariance), checking the powers of n and the analytic replacement for FX7's absolute squares.
- 9226–9235 → FX2's gradient intertwining and onto q_n convert the curl minimum FX3 into FX10.
- 9237–9249 → The two minimizer comparisons prove FX10 and its scalar minimization yields FX11.
- 9252–9256 → The zero-mode assignment is promised a uniformly holomorphic extension below, proved in FX20.
- 9274–9276 → FX8's ratios supply the bounded numerator and central sinc quotient for FX13.
- 9282–9292 → FX8's denominator and the preceding sine estimate supply FX14.
- 9304–9316 → The alias bounds FX13–FX14 imply FX16 and then holomorphy and derivative bounds of R in FX15.
- 9340–9357 → FX18 gives FX19, whose factorization removes FX11's denominator and yields FX20 (fx:origin-cancellation).
- 9362–9366 → FX19 gives the Ward identity; n=1 checks the ordinary curl normalization and phases.
- 9375–9384 → FX15's central and nonnegative alias terms prove FX21.
- 9386–9395 → FX12–FX16 and FX21 keep the denominators of FX11 nonzero away from the origin.
- 9397–9405 → FX20 and the away-from-zero formula agree on overlaps to prove FX22.
- 9407–9411 → Alias reindexing in FX9 proves periodicity of FX11 and its continuation.
- 9419–9430 → Contour shifting FX23 under FX22 proves FX24; the zero-frequency and Ward identities are those already proved at 9361–9363.
- 9444–9457 → Finite Fourier orthogonality verifies FX25; the earlier energy symbols produce FX26.
- 9459–9466 → The actual flat middle-pivot basis is reused, and G is explicitly taken from FX1a.
- 9473–9475 → The Feynman form computed FX3 only and does not replace the soft gauge in FX27.
- 9477–9496 → Expanding FX1 and the local fixed-cell null-vector argument independently recover the real gap used next for FX27.
- 9497–9505 → FX22, the finite transform and FX27 give derivative bounds and FX28.
- 9507–9514 → FX28, the proved analytic bounds and the real gap give FX29 by a Neumann series.
- 9516–9526 → Contour shifting as in FX23–FX24 gives FX30 (fx:flat-kernel-bounds).
- 9538–9548 → The already calculated symbols and their infinite block kernels give FX31 by sampled Fourier orthogonality.
- 9554–9556 → The same image-sum argument applies to the inverse symbol because sampled inverses invert sampled positive precisions.
- 9558–9566 → The flat axial holonomy reduction and FX31 extend the kernel bounds with unit-modulus image factors.
- 9568–9577 → FX30 concerns the classical constrained soft-gauge variables; the named extensions still require their actual operators and uniform perturbation estimates.

## Obligations named here

- 8366–8369: Under the supplied local near-pure-gauge bound, QC18 requires a ≤ c/(C_b M L^5); alternatively impose varpi_c ≤ c L^-6 with a small complex perturbation.
- 8379–8381: Charge any gauge condition number that grows with a larger window.
- 8384–8386: The one-step calculation does not bound many-level response or a further coordinate transformation on a large run window.
- 8386–8388: Retain polynomial window-radius loss from the background/core inclusion in a later Cauchy radius.
- 8388–8390: The free precision gap remains a separate assertion at this point; CF18 later proves the classical flat version in this chunk.
- 8388–8390: All-window core estimates remain a separate assertion.
- 8388–8390: Tower estimates remain a separate assertion.
- 8389–8390: Conditional exterior forces remain a separate assertion.
- 8389–8390: The clean-class law remains a separate assertion.
- 8407–8411: The flat-gap statement excludes signed counterterms, nonconstant layer weights, nonzero-current constraint corrections and complex decoupling matrices.
- 8574–8581: The finite-dimensional construction of E_k claims no uniform inverse bound.
- 8592–8604: Identifying E_k with a background Hessian uses a twice differentiable exact lift and linearized constrained stationarity; CF11 itself does not assume a nonlinear background theorem.
- 8762–8765: The flat-gap result does not prove a uniform upper bound or dressed precision decay; WI16 and FX30 later supply upper and decay bounds for the classical flat problem only.
- 8765–8769: Nonzero-current terms from curved constraints require their own quantitative comparison with the positive flat form.
- 8765–8769: Signed layer profiles require their own quantitative comparison with the positive flat form.
- 8766–8769: Counterterm arrays require their own quantitative comparison with the positive flat form.
- 8766–8769: Non-Abelian perturbations require their own quantitative comparison with the positive flat form.
- 8767–8769: Enlarged complex decoupling parameters require their own quantitative comparison with the positive flat form.
- 8769–8770: No full background assertion follows from CF18 alone.
- 8769–8770: No interacting Gaussian-law assertion follows from CF18 alone.
- 8945–8946: The constructed lift's amplitude bound is deferred to below and is supplied in WI17–WI20.
- 9036–9037: The constructed linear lift bounds are not estimates for a minimizing response.
- 9049–9050: Exponential flat-precision kernels are delegated to ch:flat-exponential-kernels, which follows in this chunk.
- 9050–9054: Applications to minimizing or nonlinear backgrounds require the corresponding actual-operator comparison propositions.
- 9051–9054: Applications to complex cores and tower substitutions require the corresponding actual-operator comparison propositions.
- 9052–9054: Applications to signed layer profiles, nonzero currents, counterterms and complex decoupling arrays require the corresponding actual-operator comparison propositions.
- 9065–9067: A spectral gap alone is insufficient for decay; a uniform complex strip for exact symbols is required and supplied below in FX22 and FX29.
- 9130–9135: Feasibility is supported by the filter calculation below and attainment by the curl-null quotient projection.
- 9255–9256: The zero-mode definition must be shown to belong to a uniformly holomorphic symbol; FX20 subsequently supplies this.
- 9288–9292: Shrink rho so that every noncentral denominator has the stated uniformly positive real part.
- 9328–9350: Choose a sufficiently small fixed polydisc to keep h_mu bounded and J_n nonzero.
- 9390–9405: Shrink the away-from-zero neighborhood and common strip width to preserve nonzero denominators and glue the analytic formulas.
- 9501–9514: Choose the complex strip width so that the precision perturbation is less than half the real gap; the inverse uses both analyticity and the gap.
- 9551–9554: The torus image formula does not assert exact equality of the full torus kernel with its infinite-lattice lift.
- 9570–9571: Exponential decay is not asserted for the massless auxiliary D_n.
- 9571–9573: The constrained classical decay result is not a physical Yang–Mills mass-gap assertion.
- 9574–9577: No signed-profile comparison has been proved by this calculation; actual operators and uniform perturbation estimates are required.
- 9574–9577: No counterterm comparison has been proved by this calculation; actual operators and uniform perturbation estimates are required.
- 9574–9577: No nonzero-current comparison has been proved by this calculation; actual operators and uniform perturbation estimates are required.
- 9574–9577: No non-Abelian comparison has been proved by this calculation; actual operators and uniform perturbation estimates are required.
- 9574–9577: No enlarged complex-decoupling comparison has been proved by this calculation; actual operators and uniform perturbation estimates are required.
