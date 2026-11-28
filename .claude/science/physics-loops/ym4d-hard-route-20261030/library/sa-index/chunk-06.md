# Chunk 06: lines 6423-7042
Sections: Field coordinates and the radius of quadratic extraction (6453; `ch:extraction-radius-normalization`); Physical fields, Gaussian fields and the coefficient (6470); A near-zero ball lies in the hereditary core (6559); Cauchy's estimate, response decay and entropy (6662); What the squared radius ratios pay for (6759); The construction and the plan of proof (6829; `candidate:orientation`); 0. Objects and proof strategy (6836); (0a) The theorem, stated clause by clause (6909).

| Lines | Name / tag | Kind | What it states (one plain sentence, your words) | Status here | Reads (inputs it uses, by tag or name) | Key phrase |
| --- | --- | --- | --- | --- | --- | --- |
| 6423–6430 | R28, numerical history weight (continued) | definition | The visible end of R28 defines the live-object weight Θ using deposits and volumes with nonnegative coefficients and w below one. | definition | Lineage creation costs; Dep; Vol; beginning of R28 outside this chunk | "defines the numerical weight" |
| 6432–6433 | End mark | definition | The end mark is Θ at the final level and differs from label marks. | definition | R28; final level K | "The end mark is" |
| 6433–6435 | Prepaid stability | hypothesis | The weighted sum of history measures is bounded by the prescribed exponential volume budget. | assumed | R28; stipulated normalization and dials | "The prepaid-stability input is" |
| 6436–6437 | Preconditions for prepaid stability | requirement | Applying prepaid stability requires creation-deposit and operation-majorant bounds. | assumed | Creation-deposit bound; operation-majorant bound | "Its use requires" |
| 6439–6441 | Class C_k(θ) | definition | The class consists of complete typed presentations obeying R13–R28 and their structural, positivity and analytic-domain clauses. | definition | R13–R28; analytic domains | "consists of the complete" |
| 6441–6444 | Step closure | hypothesis | The induction assumes a next presentation preserving constants, margins and represented measures under the kernels. | assumed | C_k(θ); step kernels | "uses the step-closure input" |
| 6444–6447 | Supporting analytic estimates | requirement | Background, response, substitution, island-mass, drop-out-majorant and closure estimates must be proved for the step. | named open | Step closure; typed presentations | "which we must" |
| 6456–6463 | Physical extraction versus Gaussian normalization | remark | Physical quadratic extraction uses different coordinates from Gaussian normalization and the core inclusion uses existing background and tower estimates. | sketched | Analytic field domains; background and tower estimates; ER5–ER11 below | "follows" |
| 6465–6468 | Uniform constants and non-Abelian inputs | hypothesis | Constants are independent of level, volume and earlier depth while non-Abelian background and tower estimates remain hypotheses. | assumed | Fixed blocking and localization parameters | "explicit hypotheses" |
| 6472–6484 | ER1, trivial-field coordinates and norm | definition | The physical potential and independent current form a pair with a norm controlling the potential, its first difference quotient and the current. | definition | Bare spacing η_j; level-j units | "no coupling multiplies it by definition" |
| 6486–6488 | Physical block datum and background map | definition | The datum V is exp(iB) and p_j is its configuration-current pair in a fixed near-zero gauge. | definition | ER1 | "Let" |
| 6488–6496 | ER2, background linear response | hypothesis | The background fixes the trivial pair and has derivative h_jB equal to the stated potential-current response at a coupling-independent physical radius. | assumed | p_j; H_j; D*D; ER1 | "Suppose" |
| 6497–6500 | Vanishing first derivative and argument | proof | Constant gauge invariance forces the derivative of a local invariant interaction to vanish on the semisimple Lie algebra. | proved in detail | Gauge invariance; semisimple Lie algebra | "that functional is zero" |
| 6502–6509 | ER3, pullback Hessian and argument | identity | The pullback Hessian is the Hessian of E on two linear responses because the term containing the second derivative of p_j vanishes. | proved conditionally | ER2; DE(0)=0; chain rule | "it is multiplied by" |
| 6511–6514 | Polarisation kernel, T[E], b(E) | definition | The ER3 kernel and its second spatial moments define the curvature tensor and its invariant scalar action coefficient using physical B derivatives. | definition | ER3; invariant scalar channel | "Its second spatial moments define" |
| 6514–6521 | ER4, block Wilson normalization | definition | The Wilson functional of the block datum has action coefficient one and quadratic part one half the squared curvature norm. | definition | b; block Wilson functional | "use the normalization" |
| 6521–6526 | Pulled-back Wilson and counter-insertion normalizations | requirement | Normalizing a pulled-back Wilson family and requiring T[A[c]]=c need linear-response identities beyond a coordinate change. | named open | Background linear-response identities; allowed constant curvature tensor c | "Neither identity for" |
| 6528–6530 | Gaussian field and rescaled interaction | construction | Gaussian variables divide the fluctuation field by g_j and evaluate E at p_j(g_j B^s). | definition | ER2; g_j | "one instead sets" |
| 6530–6541 | ER5, Gaussian-to-physical coefficient conversion | identity | Two derivatives in the Gaussian variable multiply the Hessian, tensor and coefficient by g_j squared, so physical readout divides by that factor. | proved in detail | Chain rule; definitions of T and b; rescaled interaction | "the chain rule gives" |
| 6543–6552 | ER6, Cauchy radius conversion | estimate | Under the amplitude hypotheses the Gaussian Cauchy bound converts to the physical bound CM_j/a_j squared. | proved conditionally | ER5; ER13 below; response decay; localization; radius a_j; norm M_j | "then transforms as" |
| 6553–6557 | Power-law physical radius | remark | Writing the physical radius as g_j to the γ gives the coefficient bound CM_j g_j to minus twice γ without changing the radius loss. | proved in detail | ER6; algebraic coordinate conversion | "The coupling cancels from the coordinate conversion." |
| 6561–6569 | Hereditary core at (a_0,a_1) | definition | A core imposes curvature, gauge, potential, derivative and current conditions on a real-complex triple and every allowed restricted tower. | definition | Triple (U,A′,J); local regular gauges; tower rules | "A core at radii" |
| 6571–6584 | ER7, uniform holomorphic tower estimate | hypothesis | Small simple conditions produce holomorphic towers whose curvature and current obey radius K_T(ε_0+ε_1²) uniformly in rule, restriction and depth. | assumed | Simple core conditions; change-of-unit factors | "Assume the following uniform tower estimate." |
| 6586–6597 | Near-zero core inclusion / ER8 | proposition | A sufficiently small physical C¹ ball of radius c min(a_0,a_1,1) lies in the hereditary core uniformly in level. | proved conditionally | ER7; ER1; small a_0,a_1 | "Under (ER7)" |
| 6598–6630 | Proof of near-zero core inclusion | proof | The plaquette bound and reduced radii establish all simple conditions and ER7 supplies every hereditary condition. | proved conditionally | ER7; ER9; trivial real configuration | "This proves (ER8)." |
| 6599–6613 | ER9, plaquette estimate and expansion argument | estimate | Expanding a plaquette bounds curvature by η_j² times the first derivative norm plus the squared potential norm without inverse spacing loss. | proved in detail | ER1; small exponential chart; discrete curl | "This follows by expanding a plaquette product" |
| 6615–6627 | Reduced-radius choice | construction | The chosen ε_0 and ε_1 leave enough room for the simple bounds and the tower radius budget. | proved conditionally | ER7; ER9; sufficiently small c | "Taking" |
| 6632–6636 | Necessity of the C¹ ball | remark | A potential-only supremum bound permits lattice oscillations with a derivative larger by inverse spacing and cannot replace ER8's ball. | sketched | ER1; ER8; bare-lattice oscillations | "arbitrary" |
| 6638–6645 | ER10, background continuation bound | hypothesis | The continued background is holomorphic in a physical datum ball and its potential-current C¹ norm is bounded linearly by B. | assumed | ER2; r_B; C_B | "suppose the continued background" |
| 6647–6652 | ER11, admissible datum radius | estimate | The continued background triple lies in the core when B is below both half the continuation radius and the scaled ER8 radius. | proved conditionally | ER8; ER10 | "Then its triple belongs to the core whenever" |
| 6654–6660 | First-order response and physical-radius scope | remark | The derivative of ER10 gives the response version and fixed or running core radii yield corresponding physical datum radii. | sketched | ER8–ER11; background continuation; first-order bounds; ER7 | "uses the derivative of" |
| 6664–6666 | Torus transfer inputs | hypothesis | Passing the infinite-lattice argument to tori uses uniform response bounds and lift convergence from the background hypotheses. | assumed | Background hypotheses; lift convergence | "supplied by the" |
| 6666–6673 | Local family size and usable ball | hypothesis | Pointed local families have exponential tree-length decay with norm M on a core containing a usable radius-a ball. | assumed | Core; tree length d(X) | "assume that the near-zero ball" |
| 6673–6678 | ER12, response decay | hypothesis | A single-bond background response decays exponentially with its distance from the local domain in the ER1 norm. | assumed | h_j; ER1; level-j distances | "Assume also the uniform response decay" |
| 6680–6684 | Localization entropy and volume | hypothesis | Rooted domain counts grow at rate κ_D while the number of pointed sites grows at most quartically with tree length. | assumed | Fixed root cube; level-j distance | "suppose the number of domains" |
| 6686–6699 | Amplitude bound with its radius / ER13 | proposition | A positive entropy margin gives absolutely convergent exponentially decaying polarisation and coefficient or tensor size CM/a² uniformly in level and volume. | proved conditionally | Local family bound; radius a; ER12; entropy and volume bounds; κ>κ_D; covariance conditions; torus transfer inputs | "If" |
| 6700–6743 | Proof of the amplitude bound | proof | Bidisc Cauchy estimates, response decay and entropy summation bound the polarisation kernel and its spatial moments. | proved conditionally | ER12; local family bound; radius a; entropy margin; fixed localization cubes; torus transfer inputs | "This proves the first" |
| 6701–6706 | Bidisc Hessian estimate | estimate | The two-variable Cauchy formula bounds the local Hessian by CM/a² times localization decay and the two direction norms. | proved conditionally | Analytic radius a; local family size M | "The two-variable Cauchy formula on a bidisc inside the ball gives" |
| 6708–6713 | ER14, one-term response bound | estimate | Each Hessian contribution has the Cauchy factor and exponential decay in tree length and both response distances. | proved conditionally | Bidisc Hessian estimate; ER12 | "Combining this with (ER12)" |
| 6715–6732 | Entropy summation argument | proof | Allocating a small part of the decay to external separation leaves enough decay to sum pointed sites, domain shapes and root locations. | proved conditionally | ER14; fixed cube side M_0; κ>κ_D; entropy and volume bounds | "The remainder is summable." |
| 6734–6743 | Moment bound and scalar identification scope | proof | Polynomial moment factors are absorbed by exponential decay, while identifying the invariant tensor as a scalar uses separate symmetry identities. | proved conditionally | Polarisation bound; moment definitions; Ward and lattice-symmetry identities for identification only | "This proves the tensor" |
| 6745–6757 | Running-radius extraction norm | remark | Running radii θ_j^(-1/2)(log θ_j)^q impose an inverse-square loss that may instead be retained in a weighted extraction norm. | proved conditionally | ER13; q≥0; running-radius formula | "provided that this normalization is retained" |
| 6761–6765 | Gauge-invariant window scaling | hypothesis | A vacuum-subtracted remainder has no linear term and each quadratic curvature scales inversely with area while the volume scales in four dimensions. | assumed | Remainder size r_j; physical radius a_j; gauge invariance | "Assume a gauge-invariant window estimate" |
| 6765–6773 | ER15, relative quadratic evaluation weight | estimate | Cancelling the geometric scale factors leaves quadratic evaluation weight w_(n,j)=(a_n/a_j)² multiplying the birth size. | proved conditionally | Gauge-invariant window estimate; radii a_j,a_n | "After these geometric factors cancel" |
| 6773–6779 | ER16, readout cancellation | identity | Applying the final inverse-square radius readout to the evaluated remainder exactly restores the inverse-square birth-radius factor. | proved in detail | ER15; physical coefficient readout | "so" |
| 6781–6784 | Avoiding double charging or missing readout | remark | An extra birth-radius loss double counts extraction while dropping the final readout confuses potential size with coefficient size. | proved in detail | ER16 | "count the same shrinking input radius twice" |
| 6785–6788 | Nonlinear remainder domain requirements | requirement | The full nonlinear bound needs actual backgrounds inside their original analytic domains and separate large-domain control. | assumed | Original analytic domains; large-domain estimates; ER15 | "The full nonlinear remainder estimate also requires" |
| 6790–6794 | Summation example hypotheses | hypothesis | Remainders decay with exponent κ_0 greater than four and inverse couplings grow at least linearly into older levels above a large lower bound. | assumed | Running radii; λ>0; C_0; r_j | "suppose" |
| 6793–6807 | ER17, summed remainder and coefficient | estimate | Integral comparison gives θ_n^(1−κ_0/2) for evaluated remainders and θ_n^(2−κ_0/2)(log θ_n)^(-2q) after readout. | sketched | ER15–ER16; summation hypotheses; running radii | "Integral" |
| 6809–6812 | Two sources of power loss | remark | Summing older levels and extracting the quadratic coefficient each lose one power of θ in the usual g^(κ_0−4) bound. | proved in detail | ER17 | "The two losses are already present in (ER17)." |
| 6816–6822 | Scope for marked and unmarked chains | remark | Fixed radii preserve the unmarked bound while marked smallness pays readout and the other named propositions need additional estimates. | assumed | ER13; ER17; background, response and entropy hypotheses; complex-window, tensor-marginal, weighted-sensitivity, large-field-zone derivative estimates | "use their additional stated estimates" |
| 6833–6835 | Dagger convention | definition | A dagger marks auxiliary assertions outside the central targets without changing how their hypotheses and dependencies are read. | definition | Central target statements | "A dagger marks auxiliary assertions" |
| 6844 | Gauge group and lattice setup | definition | The construction fixes SU(2), N=2, torus lattices of spacing L^(-K) and the plaquette action density a_p. | definition | Torus family L; configurations U; plaquette holonomy | "We take" |
| 6844–6850 | Wilson measure, smeared density and connected correlations | definition | The normalized Wilson weight defines μ, the plaquette sum defines O(f), and its cumulants define S^T_n. | definition | β; a_p; partition function Z; Haar measure | "we consider the following objects" |
| 6852 | Continuum interpretation of O(f) | remark | The spacing-free plaquette sum approximates the integrated curvature-squared action density. | sketched | Plaquette curvature approximation; Riemann sums | "is a Riemann-sum approximation" |
| 6852 | Separated test tuples S_n(E) | definition | Tests are real compactly supported C¹ functions with pairwise disjoint supports. | definition | E equal to a torus or Euclidean space | "which are tuples of real" |
| 6854 | Running inverse couplings | construction | RG steps assign x_0=β and subtract bounded increments independent of torus and later cutoff. | assumed | Steps 1–2; (3b); (3d); B_sharp | "The renormalisation group of steps 1 and 2 assigns" |
| 6854–6861 | First-passage time, window and datum | definition | K(β,g) is the first entry time into the reference window and W_K(g) labels bare couplings with that time. | definition | x_k; g; B_sharp | "is called a first-passage datum" |
| 6863–6867 | Dilation identity and rescaled tests † | identity | Dilation identifies connected correlations at (K,ℓ) with those at first passage (K′,L^bℓ) using f^[b](x)=f(L^(-b)x). | proved in detail | K′=K(β,g); Wilson weight; spacing-free O(f) | "holds exactly, for all bounded" |
| 6869 | Proof of dilation identity † | proof | The lattice dilation preserves plaquettes, barycentres, Haar measures and the observable formula. | proved in detail | Definitions of μ and O; lattice dilation | "To see this, note that the dilation" |
| 6869 | Gibbs-state dilation and norm consequences † | remark | Dilation extends to periodic Gibbs states, increases distances and does not increase test norms, while contraction needs a lower volume bound and can enlarge norms. | sketched | Dilation identity; (3d); sharp norm | "The same identity holds" |
| 6871 | Fixed-torus versus infinite-volume uniqueness scope | remark | Convergent renormalised couplings remove subsequences only on fixed tori under clause (d)(1), leaving infinite-volume uniqueness unasserted. | assumed | Theorem 0(a)(ii)–(iii); (d)(1) | "does not assert uniqueness of the infinite-volume limit" |
| 6871 | Reference run and renormalised inverse coupling | definition | x^natural_K is the final coupling of a run whose auxiliary choices use θ_k=g^(-2)+c_0(K−k), with c_0 the displayed one-loop constant. | definition | K-step run; frozen choices; natural logarithm | "The renormalised inverse coupling" |
| 6871 | Freezing construction and comparison rationale | construction | Freezing choices allows entrywise coupling comparisons and a common linear operation without changing measure quantities and incurs the stated small coupling shift. | sketched | (3c); (8b); Theorem 0(d)(1); integer cube sizes | "Each of these two devices needs the choices to coincide" |
| 6871–6879 | Continuum limit at g | definition | A continuum limit is a first-passage correlation limit as cutoff is removed on a fixed torus or expanding tori, also including tuned torus limits. | definition | W_K(g); separated tests; (a)(i) | "By a continuum limit at" |
| 6879 | Periodic torus-limit states and volume-first limit | definition | A volume-first limit removes volume at fixed lattice data to obtain periodic torus-limit states and then removes spacing along first-passage data. | definition | G^tor_(K,β); periodic extensions; S^T_n[ν] | "A volume-first limit" |
| 6881 | Order of parameter choices | requirement | Exponents precede large L, the remaining constants and finally small g. | assumed | Exponents; blocking factor; theorem constants | "The exponents are fixed first." |
| 6881–6895 | Theorem 0 overview | theorem | The target theorem gives uniform correlation bounds, nontrivial short-distance normalization, existence, inherited Euclidean properties, torus uniqueness and a rotation criterion. | assumed | First-passage data; separated supports; Theorem 0(a)–(e); periodic Wilson DLR states for factorial growth | "Theorem 0 states the following." |
| 6888 | Free two-point kernel | definition | K_free(f,h) integrates f(x)h(y) against the inverse eighth power of separation. | definition | Separated bumps f,h | "where" |
| 6888 | Short-distance error scope | remark | The relative error tends to zero on each torus but is only bounded above and below on Euclidean space. | assumed | Theorem 0(c)(3)–(4); short-distance pairs | "the clause consists of the bounds by the two constants" |
| 6897 | Centred moment functional σ_S | definition | Summing products of connected functions over partitions without singleton blocks defines the moments with zero one-point function. | definition | Connected S_n; partitions with blocks of size at least two | "the one-point function is set to zero" |
| 6897–6904 | Canonical decomposition | construction | A compactly supported probability measure and continuous injective component map represent σ_S and its asymptotically separated products. | assumed | Theorem 0′; volume-first limit; translations; centred moments | "This functional admits a canonical decomposition" |
| 6906 | Component properties and reconstruction obligations | requirement | Component Euclidean properties await analytic obligations and reconstruction additionally needs quantitative growth and external analytic continuation. | named open | Theorem 0′; `ch:precise-reconstruction`; external analytic-continuation theorem, unnamed here | "Once the stated analytic obligations are proved" |
| 6911 | Common theorem thresholds and uniformity | hypothesis | Shape and source parameters determine nested small-coupling thresholds under which the two theorems have the specified uniform constants. | assumed | Step 4; first-passage data; torus family L(g); earlier fixed constants | "Throughout" |
| 6913 | Torus frame, mirrors and observable covariance | remark | Even torus lengths and odd blocking make mirror cuts and nested bond mirrors compatible with exact barycentric observable covariance. | proved in detail | ℓ=2L^m; odd L; barycentres; (4d) | "Because barycentres are used" |
| 6913 | Gaussian mean and diagonal exclusion | remark | The exact-cochain Gaussian mean has a divergent leading Riemann sum and the inverse-eighth-power kernel is not locally integrable, motivating centred separated observables. | sketched | `ch:lattice-curvature-comparison`; first-passage scaling; V_K | "its leading Riemann-sum behavior" |
| 6913 | Limits of diagonal-flat testing | requirement | Diagonal flatness removes contact-term sensitivity but does not establish growth, continuity or analytic-continuation hypotheses for reconstruction. | named open | `ch:precise-reconstruction`; diagonal-flat test domain | "it does not supply the growth bound" |
| 6913 | Coordinate and diagonal mirrors | definition | Euclidean mirrors have coordinate or pairwise diagonal normals, whereas torus mirrors are coordinate pairs with slab sides. | definition | θ_Σ; E_+(Σ); coordinate vectors | "By a mirror" |
| 6915 | Theorem 0(a), first passage and scaling | theorem | Every admissible run reaches first passage with linear passage-time bounds, torus-independent couplings and the stated uniform asymptotic freedom slope. | assumed | Steps 3, 5, 8; b_k≤B_sharp; common theorem hypotheses | "[existence; 3, 5, 8]" |
| 6915 | Theorem 0(a)(i), tuned limit | theorem | For sufficiently small g there is a tuned bare coupling at every K with linear bounds and whole-sequence torus correlation convergence. | assumed | γ_U; x^natural_K; steps 3, 5, 8; separated Lipschitz tests | "Then for each" |
| 6915 | Theorem 0(a)(ii)–(iii), subsequential limits | theorem | First-passage sequences admit fixed-torus and expanding-torus subsequential limits and the same existence holds for volume-first data. | assumed | Steps 3, 5, 8; K_j→∞; ℓ_j→∞ for Euclidean limits; G^tor states | "one can extract a subsequence" |
| 6915 | Meaning of a limit of (a)(iii) | definition | This phrase denotes a continuum limit along a defining sequence of expanding tori and bare data. | definition | Theorem 0(a)(iii); (K_j,ℓ_j,β_j) | "means" |
| 6917–6921 | Theorem 0(b)(i)–(iv), inheritance | theorem | Limits inherit translation and hypercubic invariance, coordinate reflection positivity, symmetry, regularity and the appropriately scoped correlation bounds. | assumed | Step 6; (4c)–(4e); (8a); (c)(1)–(2); periodic Wilson DLR states for factorial bound | "Each continuum limit has the following properties." |
| 6922–6928 | Theorem 0(b)(v), growth | estimate | Euclidean limits from periodic Wilson DLR states satisfy factorial growth controlled by the displayed graded Schwartz seminorm. | assumed | Periodic Wilson DLR states; step 6; growth constants | "satisfies the growth condition" |
| 6928 | Reflection-positive Hilbert-space construction | construction | The centred reflected form on positive-time tests defines the separable space H(S). | assumed | σ_S; reflection positivity; positive-time test algebra | "take the form" |
| 6930–6932 | Theorem 0(b)(v), time and spatial symmetries | theorem | H(S) carries a positive-energy self-adjoint time semigroup, commuting spatial translations and hypercubic spatial symmetries fixing the vacuum. | assumed | Step 6; reflection-positive construction; inherited invariance | "which form a strongly continuous semigroup" |
| 6935 | Volume-first embedding and diagonal positivity | theorem | Each volume-first limit at g≤γ_J is an expanding-torus limit with diagonal reflection positivity. | assumed | (5c); (10a); Theorem 0(a)(iii) | "each volume-first limit is a limit" |
| 6937–6940 | Theorem 0(c)(1), finite-volume bound | estimate | Separated Lipschitz cumulants obey an order-dependent bound with an exponential torus-volume factor. | assumed | Steps 4, 7; common hypotheses; separation d | "[bounds, non-triviality; 4, 7" |
| 6937–6941, 6945, 6951 | Theorem 0(c)(2), volume-uniform bound | estimate | A per-order bound holds on sufficiently large tori and without a volume condition for periodic Gibbs states, with separation-monotone constants. | assumed | Steps 4, 7; (10a); support radius R; first passage | "with no condition on a volume" |
| 6942–6949 | Periodic Wilson DLR factorial bound | estimate | Real C¹ tests in periodic Wilson DLR states obey a factorial bound with B(R)=C(R+1)^4 and separation power 5n. | assumed | D1 in actual rooted geometry and compatible source tori; G1; `thm:graded-rooted-source` | "under D1 in its actual rooted geometry" |
| 6950–6951 | Stronger factorial or separation bounds | requirement | A finite-torus factorial bound or separation prefactor of degree independent of n needs another estimate. | named open | Additional estimate unspecified here | "requires an additional estimate" |
| 6953 | Pair class T_E(d;ϑ) | definition | Nonzero nonnegative Lipschitz bumps satisfy prescribed support radii, separation, mass and Lipschitz shape bounds. | definition | d; ϑ; E | "consists of the pairs of Lipschitz functions" |
| 6953 | Two-point scale and cutoff conditions | hypothesis | The two-point law requires small g and d, an admissible pair and at least n_0 steps between the tested scale and cutoff. | assumed | γ_W(ϑ); d_0; T_E; s(d); n_0 | "Assume also" |
| 6955–6960 | Theorem 0(c)(3), two-point law | theorem | The connected two-point function equals the free kernel times the stated running-coupling normalization with a uniformly small torus error and a bounded Gibbs-state error. | assumed | Steps 4, 7; (3a); (4b); (10a); two-point scale and cutoff conditions | "For periodic Gibbs states the identity remains true" |
| 6960 | Scale coupling and running normalization | definition | g(d) is the running coupling at level K−s(d) and ζ_K(d) is its inverse-coupling response to a constant bare shift. | definition | g_k; s(d); ζ′; (4b) | "is the running normalisation" |
| 6960 | Affine envelope and short-distance errors | estimate | Inverse couplings have affine scale envelopes and normalization and asymptotic-freedom errors are controlled by monotone functions vanishing at short distance. | assumed | (3a); (4b); bar η; bar ε_ℓ | "One has" |
| 6962 | Theorem 0(c)(4), continuum law and nontriviality | theorem | First-passage continuum limits inherit the short-distance law with the displayed error bounds and Euclidean Hilbert dimension at least two, excluding tuned torus limits. | sketched | (a)(ii)–(iii); (c)(3); C¹ pairs; bar η; bar ε | "Consequently" |
| 6964 | Quadruple class T_E^(4)(d;ϑ) | definition | All six pairs are admissible and the four supports lie in small balls with collinear centres. | definition | Pair class T_E; radius d/16 | "consists of the quadruples" |
| 6964–6970 | Theorem 0(c)(5), positive four-point bound | theorem | For sufficiently small scale and enough cutoff steps, admissible torus quadruples have strictly positive connected four-point functions of size g(d)^8. | assumed | Steps 4, 7; ϑ_square; γ_W; n_4≥n_0; quadruple class | "the bound below holds whenever" |
| 6972–6973 | Theorem 0(d)(1), window proximity | theorem | At large source radius and sufficiently small g every first-passage window lies within one quarter source radius of the tuned coupling. | assumed | Step 8; (a)(i); γ_U′; ρ | "Then the first-passage windows lie close" |
| 6974 | Theorem 0(d)(2), reference-run parametrization | theorem | Nearby reference runs have uniformly bi-Lipschitz final couplings converging to a function whose compact interval range contains a specified neighbourhood. | assumed | Step 8; tuned couplings; source radius ρ | "converge uniformly" |
| 6975 | Theorem 0(d)(3), unique torus family | theorem | The continuous family S^(ℓ,x) contains the tuned limit and attracts every nearby bare sequence whose renormalised coupling converges to x. | assumed | Step 8; interval I; reference-run coupling; separated Lipschitz tests | "with no passage to a subsequence" |
| 6977 | Torus uniqueness consequence | proof | Two nearby bare sequences with the same limiting renormalised coupling converge to the same torus theory by clause (d)(3). | proved conditionally | (d)(1)–(3); (a)(ii) | "They have the same limit" |
| 6979–6983 | Shell flux B_(ω,χ) | definition | The boundary term in the rotational Ward identity is the displayed combination of plaquette densities and cutoff differences. | definition | Wilson measure; deformation χ(y)ωy; lattice differences; β | "The shell flux is the boundary term of this identity" |
| 6985–6991 | Local correction h_(ω,χ) | definition | The correction sums cutoff differences over plaquette bonds against bounded gauge-invariant local densities. | definition | d_(b,p,ρ); barycentres; spacing a_K | "the" |
| 6991 | Shell support argument | proof | Every term contains a cutoff difference, so the radial-cutoff flux is supported in the stated enlarged shell. | proved in detail | Flux definition; χ_R | "Each term contains a difference" |
| 6991–6997 | Theorem 0(e), rotation-flux criterion | theorem | An expanding-torus limit is O(4)-invariant exactly when the far-shell flux correlation vanishes in the stated iterated limit, yielding spatial O(3) symmetry. | sketched | Step 9; (a)(iii); Theorems 9.3 and 9.1; smooth separated tests; Theorem 0′ for volume-first limits | "What the equivalence uses." |
| 6999–7004 | Theorem 9.3, rotational Ward identity | identity | The sum of rotated-test correlations equals a bulk artefact correlation plus the shell-flux correlation. | named open | Package G; (9a); χ=1 near supports | "to be proved; Package G" |
| 7006 | Bulk term U and rotation defect | definition | U correlates the observables with dimension-six lattice artefacts over the cutoff support, and the rotation defect is the derivative under simultaneous rotations. | definition | Ward identity; χ; continuum S | "This term is the correlation" |
| 7006 | Proof sketch of the rotation-flux equivalence | proof | If the bulk term vanishes along every defining sequence, the continuum rotation defect is minus the limiting flux correlation. | sketched | Theorem 9.3; Theorem 9.1; limits of Ward identity | "Once" |
| 7008 | Theorem 9.1, bulk vanishing | theorem | Bulk artefacts vanish on all defining sequences after first-order insertion bounds and volume transfer. | named open | Package G; Propositions 9.7–9.11; (9b); anisotropy exponent c_1 | "to be proved; Package G" |
| 7008 | Proposition 9.7, first-order insertion input | proposition | This is the first of three inputs following a non-action insertion through K steps to obtain bulk vanishing on fixed and slowly growing volumes. | named open | Package G; (9b); first-order flow; c_1 | "to be proved; Package G" |
| 7008 | Proposition 9.8, first-order insertion input | proposition | This is the second of the three first-order insertion inputs for bulk vanishing, without its separate statement given here. | assumed | (9b); non-action insertion flow; c_1 | "The first three yield the vanishing" |
| 7008 | Proposition 9.9, first-order insertion input | proposition | This is the third first-order insertion input for bulk vanishing, without its separate statement given here. | assumed | (9b); non-action insertion flow; c_1 | "The first three yield the vanishing" |
| 7008 | Proposition 9.11, multiple-insertion moment bound | proposition | A simultaneous multiple-insertion moment bound supplies the fourth ingredient for volume transfer. | named open | Package G; (9b) | "to be proved; Package G" |
| 7008 | Proposition 9.10, volume transfer | proposition | Volume transfer extends bulk vanishing to every sequence of diverging torus sizes. | named open | Package G; (9b); Proposition 9.11; first three insertion propositions | "to be proved; Package G" |
| 7010 | Marginal anisotropy decay threshold | requirement | The traceless diagonal Wilson anisotropy must decay with exponent c_1 greater than one half to overcome its bare square-root-K coefficient. | assumed | Marginal flow; coefficient g_0^(-1); bulk term U | "What is needed is" |
| 7012 | Plane-weight perturbation and m(l) | construction | Differentiating plane-weighted one-loop coefficients defines m(l) as the eigenvalue on traceless diagonal plane weights. | definition | Weights 1+e_π(p); W_4; traceless e_μ | "Let" |
| 7012 | Cumulative anisotropy exponent c_1 | requirement | The cumulative response must dominate c_1 c_0 times the interval length up to a constant with c_1 in (1/2,1]. | assumed | m(l); c_0; anisotropy threshold | "is an exponent such that" |
| 7012 | One-loop anisotropy law | estimate | The cumulative anisotropy response differs from c_0k by a bounded amount and therefore permits c_1=1. | sketched | m(l); telescoping covariance; heat coefficient; (9b) | "The one-loop law in this channel" |
| 7014 | Telescoping one-loop proof sketch | proof | Total covariance reduces step responses to a bare trace whose logarithmic proper-time term has the same coefficient c_0 as the coupling. | sketched | Total covariance; constant abelian background heat coefficient; (9b) | "The law comes from a telescoping sum." |
| 7014 | Independent route to volume-first rotations | remark | Theorem 0′ obtains rotation invariance without a Ward identity or the anisotropy exponent. | assumed | (10b); Theorem 0′(1) | "without any Ward identity" |
| 7017–7023 | Theorem 0′, common hypotheses | hypothesis | The second theorem concerns a volume-first limit with g below both displayed shape-dependent thresholds. | assumed | Step 10; γ_W(ϑ); γ_W(ϑ_0); defining sequence (K_j,β_j,ν_j) | "let" |
| 7024 | Theorem 0′(1), invariance and spectral inequalities | theorem | Volume-first states are translation-invariant periodic Gibbs states whose continuum limits have O(4) symmetry, diagonal positivity and H≥abs(P_j). | assumed | Step 10; (10a)–(10b); Theorem 0(b), (c)(4), (a)(iii) | "is invariant under all translations of the lattice" |
| 7025 | Theorem 0′(2), canonical decomposition | theorem | The canonical decomposition is unique, identifies the vacuum subspace with L² of the component measure and is permuted measure-preservingly by invariant isometries. | assumed | Step 10; canonical decomposition; H; σ_S | "exists and is unique up to isomorphism" |
| 7025 | Decomposition isomorphism and P_0 | definition | An isomorphism transports the component measure and functionals by a homeomorphism, and P_0 projects onto ker H. | definition | Compact component space X; λ; σ_ξ; H | "Here an isomorphism is a homeomorphism" |
| 7026–7027 | Theorem 0′(3)(i), component inheritance | theorem | Each component inherits the stated invariance, positivity, symmetry and regularity. | assumed | Step 10; canonical decomposition; analytic obligations at 6906 | "It has the same invariances and positivity properties" |
| 7028 | Theorem 0′(3)(ii), component moments and bounds | theorem | Components have continuous constant one-point densities averaging to zero and satisfy uniform growth, per-order bounds and the Euclidean two-point law. | assumed | Step 10; (c)(2); (c)(4); canonical decomposition | "With the same constants" |
| 7029 | Theorem 0′(3)(iii), component spectrum and vacuum | theorem | Each component has the inherited operators, a unique vacuum, forward-cone spectrum and continuous spatial O(3) symmetry. | assumed | Step 10; (b)(v); component Hilbert spaces | "a unique vacuum" |
| 7030–7037 | Theorem 0′(3)(iv), uniform clustering | estimate | Component moments factorize at large separation with an inverse-square error uniform over components and volume-first limits at fixed g. | assumed | Step 10; separated test products X,Y; canonical components | "It has the cluster property" |
| 7038 | Theorem 0′(4), external reconstruction implication | theorem | Under the analytic and quantitative reconstruction hypotheses, each component gives a local scalar Wightman theory with unique vacuum, Poincaré covariance and forward-cone spectrum. | cited | External reconstruction / analytic-continuation theorem (not named by author here); `ch:precise-reconstruction`; growth, Euclidean invariance, reflection positivity, symmetry, clustering | "Applying the external reconstruction theorem" |

## Forward and backward references

Internal references are included as well as references outside this chunk; a reference to a later step records the outline's attribution, not a proof inspected elsewhere. The target theorems stated without arguments here are marked `assumed` in the table; explicit deferrals are marked `named open`, and indicated arguments are marked `sketched`.

- 6433–6436: Prepaid stability invokes the stipulated normalization and dials, creation-deposit bounds and operation-majorant bounds from the preceding presentation framework.
- 6437: R28 defines the numerical weight (its beginning precedes line 6423).
- 6439–6441: The presentation class refers to R13–R28, their structural and positivity clauses and previously specified analytic domains.
- 6442–6447: Induction invokes step closure and the background, response, substitution, island-mass, drop-out-majorant and closure estimates, explicitly still to be proved.
- 6460–6462: The near-trivial-field inclusion uses background and tower estimates already used to define analytic field domains.
- 6488: Background derivatives are taken in the ER1 chart.
- 6511–6514: Polarisation and moment definitions use the kernel of ER3.
- 6521–6526: Pulled-back Wilson and counter-insertion normalizations require the background map's linear-response identities rather than the subsequent coordinate conversion.
- 6538–6541: Gaussian extraction and physical readout use the rescaling identity ER5.
- 6543–6547: The ER6 example imports response-decay and localization hypotheses from the amplitude proposition at 6686–6699.
- 6568–6569, 6581–6582: The core and ER7 use the prescribed tower rules, restricted domains and change-of-unit factors.
- 6587: The near-zero inclusion proposition assumes ER7.
- 6612–6613: The lack of inverse-spacing loss in ER9 explains the derivative included in ER1.
- 6628–6629: The tower estimate ER7 supplies the hereditary clauses and completes ER8.
- 6635–6636: The weaker supremum ball is distinguished from the C¹ ball of ER8.
- 6638–6644: ER10 adds continuation and uniform bounds to the background introduced in ER2.
- 6647–6652: ER11 applies the core radius from ER8 to the ER10 bound.
- 6654–6660: First-order response uses the derivative of ER10, and the radius conclusion combines ER8–ER11 with background continuation and hereditary tower estimates.
- 6664–6666: Torus versions import uniform response bounds and lift convergence from the background hypotheses.
- 6695–6698: Scalar and summed-tensor interpretations require the prescribed covariance conditions, whose full formulation is not given here.
- 6708–6712: The one-term bound ER14 combines the Cauchy estimate with ER12.
- 6722–6732: Entropy summation uses ER14 and proves the first inequality of ER13.
- 6734–6742: Moment extraction uses the earlier definitions of b and T, while scalar identification needs separate Ward and lattice-symmetry identities.
- 6745–6757: Fixed and running extraction norms use ER13, with the weighted normalization required in subsequent estimates.
- 6773–6778: ER16 applies physical readout to the evaluation weight ER15.
- 6785–6788: The full nonlinear remainder estimate needs original analytic-domain membership and separate large-domain control; ER15 supplies only its radius factor.
- 6790–6807: ER17 uses the earlier running-radius formula and the weights ER15–ER16 under the displayed summation hypotheses.
- 6809–6812: The two identified power losses refer to ER17.
- 6816–6822: Unmarked and marked chains use ER13 and ER17 respectively; complex-window, tensor-marginal, weighted-sensitivity and large-field-zone derivative propositions need their own additional estimates.
- 6838–6842: The orientation attributes methods to Bałaban and classical tools without naming a particular work, and says later steps contribute to (0a).
- 6852: The reason for restricting tests to separated tuples is deferred to “The frame” in (0a), here at 6913.
- 6854: Running couplings come from RG steps 1 and 2; torus independence is assigned to (3b), and cutoff independence to (3d).
- 6869: The periodic Gibbs-state dilation identity and the contracted-torus qualifications refer to (3d).
- 6871: The distinction between subsequential and unique limits refers to Theorem 0(a)(ii), (a)(iii), (d) and (d)(1).
- 6871: Coupling-dependent integer cube sizes refer to (3c); the coupling shift from frozen choices refers to (3c) and (8b), under (d)(1).
- 6879: The continuum-limit definition includes tuned limits from (a)(i); volume-first limits use the periodic torus-limit class G^tor.
- 6881–6895: The theorem overview previews Theorem 0(a)–(e), including the periodic-Wilson-DLR restriction on factorial growth in (b).
- 6897–6904: Rotation invariance and canonical decomposition are attributed to Theorem 0′.
- 6906: Component Euclidean properties are deferred to Theorem 0′ once analytic obligations are proved; quantitative growth and external analytic continuation are specified in `ch:precise-reconstruction`.
- 6911: Source radius ρ comes from step 4; clause brackets identify the later steps supplying results and their dependencies.
- 6913: Paired chessboard cells refer to (4d).
- 6913: The exact-cochain Gaussian mean is attributed to `ch:lattice-curvature-comparison`.
- 6913: The diagonal-flat test domain and reconstruction requirements refer to `ch:precise-reconstruction`.
- 6915: Theorem 0(a) attributes existence to steps 3, 5 and 8; clause (a)(iii) also defines the phrase “a limit of (a)(iii).”
- 6917: Theorem 0(b) attributes inheritance to step 6, bounds to (4c)–(4e), tuned-limit bounds to (8a), and its last sentence to (5c) and (10a).
- 6921: Regularity inherits (c)(1), (c)(2) for (a)(ii)–(iii) with the fixed-torus volume condition, and the following factorial bound only for periodic Wilson DLR limits.
- 6935: Volume-first limits are identified with limits of (a)(iii), using the (5c)/(10a) attribution at 6917.
- 6937: Theorem 0(c) attributes bounds and nontriviality to steps 4 and 7, the running-coupling envelope to (3a), and periodic Gibbs-state results to (10a).
- 6946–6949: The factorial bound assumes D1 in its actual rooted geometry and compatible source tori together with G1, and refers to Theorem `thm:graded-rooted-source`.
- 6951: Bound (c)(2) extends to arbitrary periodic Gibbs states without a volume condition.
- 6960: The running normalization ζ is the constant-bare-shift response from (4b); the affine envelope is attributed to (3a) in the heading at 6937.
- 6962: The continuum law refers to the opening of the text and limits (a)(ii)–(iii), explicitly excluding tuned S^natural,ℓ.
- 6964: The quadruple class uses the pair class T_E(d;ϑ) defined at 6953, and its cutoff threshold satisfies n_4≥n_0.
- 6972: Uniqueness is assigned to step 8 and uses tuned couplings and limits from (a)(i).
- 6977: The uniqueness consequence uses (d)(1)–(3) and identifies every (a)(ii) limit with a member of the renormalised-coupling family.
- 6979: Theorem 0(e) attributes the rotation criterion to step 9 and invokes the rotational Ward identity for Wilson's measure.
- 6991–6997: The criterion concerns (a)(iii) limits, extends the W_3 representation and says Theorem 0′ settles the infrared input for volume-first limits.
- 6999: The displayed Ward identity is Theorem 9.3, explicitly “to be proved; Package G,” in (9a).
- 7006: The deduction of clause (e) depends on bulk vanishing along every defining sequence.
- 7008: Bulk vanishing is Theorem 9.1, explicitly “to be proved; Package G.”
- 7008: The first three insertion inputs are Propositions 9.7, 9.8 and 9.9 in (9b); 9.7 is explicitly tagged “to be proved; Package G.”
- 7008: The simultaneous-insertion bound is Proposition 9.11 and volume transfer is Proposition 9.10, both explicitly “to be proved; Package G,” in (9b).
- 7012–7014: The anisotropy exponent comes from cumulative one-loop responses and the telescoping law; the continuum coordinate-change interpretation refers to (9b).
- 7014: Theorem 0′(1) obtains rotation invariance by the separate route (10b), without the Ward identity or c_1.
- 7017: Theorem 0′ is assigned to step 10.
- 7024: Theorem 0′(1) identifies S as an (a)(iii) limit and adds conclusions to (b) and (c)(4).
- 7025: The canonical decomposition refers to the construction at 6897–6904.
- 7027–7028: Component invariance and positivity refer to the preceding theorem properties, and component bounds and short-distance laws refer to (c)(2) and (c)(4).
- 7029: Component operators are those of (b)(v).
- 7038: Reconstruction invokes an external reconstruction theorem with the quantitative hypotheses of `ch:precise-reconstruction`; no author or title for that external theorem is supplied in this chunk.

## Obligations named here

Each entry records an explicit input, requirement, restriction or unestablished step; it does not assert that an assumed input is itself false or unproved elsewhere.

- 6433–6435: Supply prepaid stability with the stipulated normalization and dials.
- 6436: Supply creation-deposit bounds before using prepaid stability.
- 6436: Supply operation-majorant bounds before using prepaid stability.
- 6439–6441: Complete presentations must satisfy R13–R28, structural and positivity clauses and the specified analytic domains.
- 6442–6444: Step closure must form the next presentation, preserve constants and margins, and preserve represented measures under its kernels.
- 6444–6447: Prove the background estimates supporting the induction step.
- 6444–6447: Prove the response estimates supporting the induction step.
- 6444–6447: Prove the substitution estimates supporting the induction step.
- 6444–6447: Prove the island-mass estimates supporting the induction step.
- 6444–6447: Prove the drop-out-majorant estimates supporting the induction step.
- 6444–6447: Prove the closure estimates supporting the induction step.
- 6465–6468: The stated uniformity excludes dependence on level, torus size and earlier depth, and statements retain non-Abelian background and tower estimates as hypotheses.
- 6488–6496: Assume ER2's trivial background value and linear response, with a coupling-independent physical continuation radius.
- 6521–6523: Pulled-back Wilson normalization requires the background map's linear-response identities.
- 6524–6526: Establish the prescribed counter-insertion identity T[A[c]]=c separately; neither pulled-back normalization follows merely from the coordinate change.
- 6540–6541: Recovering the physical action coefficient requires division by g_j².
- 6543–6545: ER6 assumes response-decay and localization hypotheses, a usable physical radius and the family norm bound there.
- 6565–6569: The core requires simple curvature, gauge, potential, derivative and current bounds and the corresponding bounds on every allowed restricted tower.
- 6571–6584: Assume ER7's holomorphic tower existence and uniform curvature/current bounds for both rules, all restrictions and all depths, including unit conversions.
- 6587–6594: ER8 requires ER7 and sufficiently small core radii; its local inclusion is proved here under those assumptions.
- 6638–6645: Assume ER10's holomorphic background continuation and uniform physical C¹/current bound.
- 6654–6659: The first-order response conclusion uses the derivative of ER10 and retains background continuation, uniform first-order bounds and the hereditary tower estimate.
- 6664–6666: Torus versions require uniform response bounds and lift convergence from the background hypotheses.
- 6666–6673: The amplitude argument assumes exponential local-family decay and a near-zero ball of usable radius a.
- 6673–6678: Assume the uniform exponential response bound ER12.
- 6681–6684: Assume the rooted-domain entropy and pointed-site volume bounds.
- 6687, 6695–6698: ER13 needs a fixed positive localization margin above entropy and the prescribed covariance conditions for scalar or summed-tensor identification.
- 6740–6742: Identifying the invariant tensor with the scalar action coefficient requires separate Ward and lattice-symmetry identities.
- 6755–6757: Any radius-weighted formulation of uniform extraction must retain that normalization in all subsequent estimates.
- 6761–6765: Assume a vacuum-subtracted remainder and the gauge-invariant window scaling for curvature factors and volume.
- 6785–6788: The full nonlinear remainder estimate requires its actual backgrounds to lie in their original analytic domains.
- 6785–6788: The full nonlinear remainder estimate separately requires control of large domains; ER15 supplies no continuation beyond the original domains.
- 6790–6794: ER17 assumes remainder decay with κ_0>4, linear backward growth of inverse couplings with λ>0 and a sufficiently large common lower bound.
- 6819–6822: The chain radius estimates retain background, response and entropy hypotheses; complex-window, tensor-marginal, weighted-sensitivity and large-field-zone derivative propositions require additional stated estimates.
- 6852: The observable test domain is restricted to separated real compactly supported C¹ tuples.
- 6854: The running-coupling construction uses increments bounded by B_sharp and their torus and cutoff independence.
- 6869: Applying the dilation identity in the contracting direction requires a lower bound on ℓ and allows the stated norm growth.
- 6871: Entrywise coupling comparison and a common linear operation on bare densities require coincident auxiliary choices at the compared couplings.
- 6871: Fixed-torus uniqueness is under (d)(1); the text does not assert uniqueness of the infinite-volume limit even when renormalised couplings converge.
- 6881: Choose exponents, then large L, then remaining constants in order, then small g.
- 6906: The stated analytic obligations must be proved before asserting the component Euclidean properties of Theorem 0′.
- 6906: Reconstruction additionally requires quantitative growth and the external analytic-continuation theorem specified in `ch:precise-reconstruction`.
- 6911: The theorem clauses assume the common small-coupling thresholds, torus family and first-passage datum, with the specified dependence and uniformity of constants.
- 6913: Diagonal-flat testing does not provide the growth bound needed for reconstruction.
- 6913: Diagonal-flat testing does not provide continuity needed for reconstruction.
- 6913: Diagonal-flat testing does not provide the analytic-continuation hypotheses needed for reconstruction.
- 6921–6926: The fixed-torus per-order bound retains its volume condition, and the factorial/growth claims are supplied for limits formed from periodic Wilson DLR states.
- 6937–6941: The correlation bounds require separated Lipschitz supports, with support-radius and minimum-volume conditions for (c)(2) on finite tori.
- 6946–6949: The factorial bound requires real C¹ tests and periodic Wilson DLR states under D1 in its actual rooted geometry and compatible source tori together with G1.
- 6950–6951: A finite-torus factorial bound requires an additional estimate.
- 6950–6951: A polynomial separation prefactor whose degree is independent of n requires an additional estimate.
- 6953: The two-point law assumes the prescribed small-coupling and short-distance thresholds, an admissible pair, and K−s(d)≥n_0.
- 6960–6962: The Gibbs-state relative error is only bounded by one half, and the continuum law excludes the tuned torus limits.
- 6964: The four-point lower and upper bounds require the shape threshold, small g, small d, an admissible collinear quadruple and K−s(d)≥n_4≥n_0.
- 6972–6975: Uniqueness requires the stated small-coupling threshold, source-radius proximity to tuned couplings and convergence of the renormalised coupling; window proximity additionally requires large ρ and g≤γ_U′.
- 6979, 6991–6997: The rotation criterion requires the supported cutoff and the stated far-shell flux condition on smooth separated tuples; the latter is the identified infrared input.
- 6999–7004: Prove Theorem 9.3, the rotational Ward identity, in Package G / (9a).
- 7006–7008: Prove Theorem 9.1, vanishing of the bulk artefact term along every defining sequence, in Package G.
- 7008: Prove Proposition 9.7, the explicitly open first-order non-action insertion input, in Package G / (9b).
- 7008: Propositions 9.8 and 9.9 are additional first-order insertion inputs in (9b), but are not individually marked “to be proved” here.
- 7008: Prove Proposition 9.11, the simultaneous multiple-insertion moment bound, in Package G / (9b).
- 7008: Prove Proposition 9.10, volume transfer to every diverging-volume sequence, in Package G / (9b).
- 7010: The marginal anisotropy must have decay exponent c_1>1/2 to overcome its initial coefficient.
- 7012: The cumulative anisotropy response must satisfy the stated interval lower bound for c_1 in (1/2,1]; the one-loop law giving c_1=1 is only sketched here.
- 7017–7023: Theorem 0′ assumes a volume-first limit and both displayed shape-dependent small-coupling thresholds.
- 7038: The Wightman reconstruction conclusion retains the theorem's analytic hypotheses and the quantitative hypotheses of `ch:precise-reconstruction` when applying the external reconstruction theorem.
