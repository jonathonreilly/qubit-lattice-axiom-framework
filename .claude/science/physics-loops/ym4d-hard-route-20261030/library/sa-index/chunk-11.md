# Chunk 11: lines 11466-12888
Sections: The field-row Gram bounds (11471); The actual straightened row is a finite analytic recursion (11508); Summability of the raw radii gives a depth-uniform row bound (11550); The two-legged constraint coefficient has a uniform moment (11612); The nonflat field-row lift follows from the row comparison (11641); Differentiating the physical response (11718); The actual equations and their differentiated right-hand sides (11725); A complete block inverse, including the multiplier (11807); Cell weights and a kernel algebra (11890); Invertibility on the whole complex ball (11998); From local forcing to first response (12064); Spatial differences of the response (12113); Joint Cauchy estimates with joining distances (12163); Finite boxes and compatible boundary forcing (12226); The full substitution and the test for staying inside a core (12294); The mesh-uniform Hölder estimate used by the response (12385); Heat kernels with enough derivative and tail control (12409); A massive resolvent and its first-difference modulus (12534); Off-diagonal resolvent derivatives (12615); An interior estimate with no unknown cutoff gradient (12637); Tori and flat unitary holonomies (12727); Covariant differences and the response equation (12753).

| Lines | Name / tag | Kind | What it states (one plain sentence, your words) | Status here | Reads (inputs it uses, by tag or name) | Key phrase |
|---|---|---|---|---|---|---|
| 11466-11467 | PX135 / flat-layered-row-lift (continued) | proof | The triangular inverse series works at finite and infinite depth with an energy bound. | sketched | PX135 display and preceding construction outside chunk; geometric series | "The same series converges" |
| 11467 | Scope of the triangular inverse | remark | The construction asserts an energy-bounded right inverse rather than a nonlinear background-map estimate. | definition | PX135 | "not an estimate of a nonlinear background map" |
| 11469 | Flat-holonomy transfer of the lift | proof | Pillarwise flat frames preserve scalar Schur constants and replace the ordinary gradient by the covariant gradient. | sketched | PX135; flat unitary frames; two scalar moments | "the same construction uses a flat unitary frame" |
| 11469 | Scope of flat-frame estimates | remark | The statement supplies neither an arbitrary-gauge ordinary-gradient bound nor a general nonflat bare field-row bound. | named open | Flat lift energy estimate | "No analogous bare" |
| 11473-11478 | PX136 / field-row-extension-premise | hypothesis | A right inverse of the actual row map is assumed to have a length-weighted energy bound. | assumed | Positive K; G=K inverse; length multiplier Xi; row volumes | "Suppose the actual row map has an extension" |
| 11478-11484 | PX137 / field-row-gram-lower | estimate | Testing against the extension gives a lower bound for the row covariance. | proved conditionally | PX136; weighted duality | "Testing with" |
| 11486-11490 | PX138 / field-row-trace-premise | hypothesis | The upper covariance bound requires a separate energy-to-row trace estimate. | assumed | Actual Q; K; Xi | "An upper bound needs the separate actual trace estimate" |
| 11490 | Upper Gram bound and flat instances | proof | Applying the trace bound to the square-root covariance proves the upper bound and identifies the flat premises. | proved conditionally | PX138; flat-field-row-upper; flat-feynman-gap; PX135 | "Indeed apply it" |
| 11490 | Flat Landau fine coercivity | requirement | The Landau extension energy estimate leaves fine coercivity as a separate task. | named open | PX135; zero-to-one bound on R | "the needed fine coercivity is still a distinct step" |
| 11492 | Normalized covariance N | definition | N is the row covariance conjugated by inverse row lengths. | definition | Xi; Q; G | "Normalize the row covariance as" |
| 11492-11501 | PX139 / field-row-inverse-counting | estimate | Exponential Schur control and a real lower bound yield exponentially decaying inverse entries with the stated counting weights. | proved conditionally | PX137; exponential cell Schur bound for N; weighted conjugation | "If its exponential cell Schur bound has also been proved" |
| 11501 | Counting-coordinate conversion | proof | Converting orthonormal inverse entries to unnormalized rows supplies the length powers xi_c to minus three times xi_d. | proved in detail | N normalization; physical row volumes | "To check the powers" |
| 11501 | Field versus site Gram weight | remark | The field-row inverse has a different counting weight because its covariance contains G instead of the site Gram's squared G-prime. | proved conditionally | PX139; earlier site-Gram convention | "This differs from the site-Gram counting weight" |
| 11503-11506 | PX140 / nonflat-row-error | hypothesis | A nonflat extension can be corrected if its row error has norm below one. | assumed | Specified E0; D_Q=QE0−1 | "If the actual primitive comparison proves" |
| 11506 | Neumann correction of E0 | construction | Multiplying E0 by the inverse row error gives a right inverse with controlled energy loss. | proved conditionally | PX140; actual-precision energy cost for E0 | "provided that cost for" |
| 11506 | Announced row estimates | requirement | The admitted domain still needs the row-error and trace estimates supplied below. | named open | PX140; PX138 | "We establish the row error and row trace estimates" |
| 11510-11521 | PX141 / actual-one-step-straightening | definition | Relative transport logarithms define u_W and the gauge-straightened coarse logarithm F_W. | definition | Block-chart transports; coordinate-order paths; Federbush mean; regular logarithms | "All logarithms are the regular branch" |
| 11521 | Two distinct averaging operations | remark | The outer exponential of averaged relative logarithms is distinct from the Federbush mean defining internal transports. | definition | PX141; block-chart mean | "This distinction fixes both levels of averaging" |
| 11523 | One-step holomorphic ball | proof | Bounded path lengths and the uniform mean contraction give holomorphy and a uniform bound on a raw ball of radius c/L. | sketched | PX141; block-chart mean contraction | "the mean contraction proved in the block chart" |
| 11525 | Flat derivative S_L | identity | Both gauge factors cancel the internal path sums so the derivative is the straight segment average. | sketched | PX141; W=1 and a=0; S_L | "Differentiating at" |
| 11527-11538 | PX142 / finite-one-step-schur | estimate | Cauchy circles bound derivative row and column norms and the fixed-leg Hessian sum with polynomial one-step constants. | proved conditionally | One-step holomorphic ball; flat derivative; fixed color dimension; finite carriers | "Two scalar Cauchy circles" |
| 11538 | Coordinate-count-free derivative argument | proof | Directional bounds control entry sums through fixed color dimension and fixed coarse-row incidence. | proved conditionally | PX141 holomorphic bound; carrier geometry | "We explain why the derivative estimate is independent" |
| 11540-11543 | PX143 / actual-straightened-recursion | construction | Iterated means, raw increments, and ordered gauge factors define the multilevel recursion. | definition | W_r; a0=eta A; PX141 | "The multilevel recursion is literal" |
| 11544-11548 | PX144 / actual-factorization | identity | The iterated nonlinear mean factors into the straightened increment and its accumulated gauge. | proved conditionally | PX143; PX141; equivariance | "Equivariance of the plain mean gives, by induction" |
| 11552 | Common epsilon and primitive local gauges | hypothesis | Epsilon bounds curvature and supplied local gauges without deriving the latter from curvature. | assumed | Primitive regular-pair hypothesis | "Existence of those local gauges remains the primitive regular-pair hypothesis" |
| 11554-11568 | One-step reference recurrences | estimate | Potential and plaquette errors satisfy finite one-step quadratic recurrences. | sketched | Regular-pair gauge clause; product, plaquette-sliding, Taylor estimates; comb gauge | "The one-step product," |
| 11570-11581 | PX145 / reference-raw-radii | estimate | Summing normalized recurrences bounds reference radii by a depth-independent multiple of L^r/n. | sketched | Reference recurrences; bottom gauge and curvature bounds; weak-field shrinkage | "a first-exit argument bounds their" |
| 11581 | Local cutoff alternative | construction | Extending the small potential with a cutoff gives the same dependence-cone bounds. | sketched | Local potential and first difference; locality; nonflat torus room | "They also follow by extending its local small potential" |
| 11583-11591 | PX146 / fluctuation-raw-radii | estimate | Bounded fine increments stay in summable raw recursion balls without fine derivative assumptions. | proved conditionally | PX142; PX145; F_W(0)=0; small epsilon+h+r; PX147 | "Multiplying the factors proves" |
| 11587-11590 | PX147 / radius-discrete-gronwall | estimate | Normalized fluctuation radii obey a multiplicative recurrence with summable coefficients. | proved conditionally | Taylor formula; PX142; p_s at most 2r | "Taylor's formula and" |
| 11591 | Gauge condition-number product | estimate | Summable increments bound the accumulated complex gauge condition numbers by two. | proved conditionally | PX146; one-step u_W bound; smaller ceiling; PX144 | "A further fixed decrease makes this at most two" |
| 11593-11597 | PX148 / multilevel-row-column-products | estimate | Derivative products have depth-independent constants after extracting row and column scale powers. | proved conditionally | PX142; PX145; PX146; summability | "The constant is bounded by the product" |
| 11599 | Per-length logarithm q_j | definition | The physical row logarithm divides the final raw increment by its coarse length. | definition | PX143; xi=n eta | "The per-length row logarithm is" |
| 11599-11604 | PX149 / actual-row-density | estimate | Physical derivatives have bounded row sum and n to minus four column and entry bounds. | proved conditionally | PX148; physical normalization | "Consequently" |
| 11604 | Counting versus functional derivative | definition | A functional derivative includes an additional inverse fourth power of the mesh relative to the displayed counting-coordinate derivative. | definition | PX149; fine cell volume | "These are counting-coordinate derivatives" |
| 11604 | Flat-product comparison | estimate | Telescoping yields small row and column errors in common local unitary frames. | sketched | PX142; PX148; flat factors; local frames | "Telescoping the products against their flat factors also gives" |
| 11606-11610 | PX150 / actual-row-mass-trace | estimate | Adjacent-level carrier overlap converts row density into the layered mass trace bound. | proved conditionally | PX149; flat-row-ltwo; flat-field-row-upper; carrier overlap | "Cauchy therefore gives the analogue" |
| 11614-11618 | PX151 / actual-hessian-chain | identity | The recursion Hessian is a sum of one-step Hessians between derivative products. | proved conditionally | PX143; chain rule; P products | "Twice differentiating the recursion gives" |
| 11619-11623 | PX152 / raw-hessian-leg-sum | estimate | A column bound on the fixed leg and row bound on the summed leg control the raw Hessian moment. | proved conditionally | PX151; PX148; PX142 | "This step uses a column sum on the fixed leg" |
| 11623 | Fixed-leg density warning | remark | Using row bounds for both Hessian legs would lose the fine-density factor. | proved conditionally | PX152 derivation | "Using two row sums would lose the fine density" |
| 11625-11629 | PX153 / constraint-hessian-leg-moment | estimate | Physical normalization and a geometric sum give a depth-uniform two-leg constraint moment. | proved conditionally | PX152; xi=n eta; geometric sum | "There is no number-of-levels factor" |
| 11629 | Other-leg Hessian moment | estimate | Symmetry of the Hessian gives the corresponding bound with the two legs interchanged. | proved conditionally | PX153; symmetry of second derivatives | "Symmetry of the second derivative gives the corresponding other-leg sum" |
| 11631-11637 | PX154 / quadratic-current-form-bound | estimate | A suitably weighted row current yields a mass-bounded quadratic constraint form. | proved conditionally | PX153; Schur; carrier overlap; current bound | "Schur and the same bounded carrier overlap give" |
| 11639 | Quadratic extension beyond the analytic ball | remark | The coefficient formula extends the quadratic form to every finite fine vector. | proved conditionally | PX154; coefficient formula | "extends to every finite fine vector by its coefficient formula" |
| 11639 | Second-variant operator readouts | requirement | The induced current and S still need row-current and weighted fine-energy bounds. | named open | H[J] transpose J; S; PX154 | "one must still bound the actual induced current" |
| 11643 | Nonflat seed lift E0 | construction | Real-center gauges and endpoint unitary normalization define fixed pillar seeds for complex increments. | definition | row-dual-bump; regular-pair gauges; endpoint transport | "It is fixed at the real center" |
| 11645 | Nearly constant gauge transitions | proof | Telescoping the connection equation along a short path bounds transition variation by C_L epsilon. | proved conditionally | Two local real potentials; first-order class on larger cube | "To prove this, write their connection equation" |
| 11647-11652 | PX155 / actual-row-lift-error | estimate | Same-level and next-level comparisons bound the seed response error strictly below one. | proved conditionally | PX149; gauge transitions; Q_L^0 majorant; carrier argument before flat-average-composition | "We have proved" |
| 11653-11656 | PX156 / actual-layered-row-lift | construction | Inverting the seed response gives the actual lift with bounded mass and covariant-gradient energy. | proved conditionally | PX155; seed derivative bounds; collar overlap; small complex perturbation | "This proves the stated energy bound, including bare seeds" |
| 11658-11664 | PX157 / actual-feynman-poincare | estimate | Local row comparisons give a Feynman Poincare inequality with an absorbable weak-field error. | proved conditionally | flat-row-mean-comparison; PX149; flat-field-local-poincare; bare identity rows | "Absorb the last term by the fixed weak-field ceiling" |
| 11664 | Row-weight convention in Poincare term | definition | The repeated a in the square-root row weight denotes a fixed positive weight rather than the fine field argument. | definition | PX157; c_c row weights | "is the fixed positive row weight" |
| 11666-11671 | PX158 / feynman-coefficient-comparison | estimate | Small complex changes of rows and gradients yield an invertible Feynman form perturbation. | proved conditionally | Actual row comparison; overlap; adjoint transport expansion; PX157; Neumann series | "This completes the component Feynman estimate" |
| 11671-11685 | Projected Landau parametrix | proof | Local constrained models, commutators, and massive boundary blocks are indicated to complete the projected inverse. | sketched | Models (c); comparison (d); landau-feynman-difference; flat decomposition; all-bare inverse bounds | "The full projected" |
| 11687-11715 | Ordered current-corrected inverses | construction | Successive series insert independent-current and induced-current corrections into the propagators. | sketched | G0; Delta'_pi; S; H; PX153; vertices (g); B85c (3.130)–(3.138) | "Include the current corrections in their defining order" |
| 11700-11702 | Source of current expansions | remark | The displayed expansions are identified with B85c using the assigned maps. | cited | B85c, equations (3.130)–(3.138) | "These are the expansions of" |
| 11711-11713 | Actual-block identification | requirement | Species weights, derivative allocation, and adjacent-level endpoint equations must be checked against actual blocks. | named open | Current expansions; assigned row and site maps | "We must check the species weights" |
| 11714-11715 | Excluded Laplacian member | remark | The covariant Laplacian member excluded by B85c is not asserted here. | named open | B85c, Theorem 3.12 | "is not asserted here" |
| 11727-11735 | Raw response conventions | definition | The straightened average, datum, and dual multiplier use raw row logarithms while A remains a physical fine field. | definition | reduced-datum; nonlinear straightening; cell pairings | "use raw row logarithms" |
| 11736-11747 | BGR1 / physical critical equations | identity | The critical pair solves stationarity, the exact reduced constraint, and the fixed-reference gauge slice. | proved conditionally | Physical stationarity proved above; reduced datum; reference R and D | "the physical stationarity identity proved" |
| 11748-11751 | Moving-reference slice derivative | requirement | Moving the reference requires differentiating R and D in the slice equation. | assumed | BGR1; moving reference | "differentiating the slice" |
| 11753-11758 | Exact datum forcing | identity | Datum variation uses the actual reduced-datum derivative including outward block factors. | proved conditionally | reduced-datum; seam-datum-nilpotence | "were computed" |
| 11760-11774 | BGR4 / constrained second variation | definition | The slice Hessian subtracts the multiplier-paired constraint Hessian from the action Hessian. | definition | Fixed slice V; q; cell transpose; datum weights; BGR1 | "The constrained second variation is" |
| 11775-11776 | Constraint-curvature term | requirement | The full constrained Hessian must retain the second fundamental form of the constraint fibre. | assumed | BGR4 | "cannot be replaced by the Hessian" |
| 11778-11783 | BGR5 / differentiated physical system | identity | Fixed-reference differentiation gives a saddle system with exact datum forcing. | proved conditionally | BGR1; BGR4; fixed reference | "Differentiating (BGR1) at a fixed reference gives the exact system" |
| 11784-11796 | BGR6 / general parameter forcing | identity | Explicit parameter derivatives of the equation and constraint give the two saddle forcing terms before solution substitution. | proved conditionally | C(A,p); E(A,omega,p); fixed slice; BGR4 | "Every differentiation" |
| 11798-11805 | Independent-current and gauge matching | requirement | Independently named propagators require matching the complete gauge and current normal form to the physical Hessian. | named open | BGR4; BGR5; Delta'_pi[J]; absolute and relative contour gauges | "must be matched" |
| 11809-11813 | Scope of block inverse | hypothesis | The inverse identity uses bilinear transposes and extends to bounded operators only where its inverses and compositions exist. | assumed | Declared operator spaces; pairings | "when the displayed inverses and compositions exist" |
| 11815-11839 | Response from a primitive constrained inverse | proposition | An onto constraint, a right inverse, and an invertible constrained Hessian determine field and multiplier responses uniquely. | proved conditionally | q onto; qE=I; P onto ker q; BGR7; BGR6 | "Suppose" |
| 11816-11823 | BGR7 / primitive inverse hypotheses and blocks | hypothesis | The kernel parametrization has invertible H and defines L and the corrected datum lift T. | assumed | q; E; P; constrained K | "Assume" |
| 11824-11830 | BGR8 / full response formula | identity | L and T give the field response and an explicit left inverse recovers the multiplier. | proved conditionally | Proposition hypotheses; BGR6; BGR7; proof 11841-11857 | "Then the unique solution" |
| 11831-11838 | BGR9 / symmetric multiplier response | identity | Symmetry identifies the force multiplier block as minus the transpose lift and makes M symmetric. | proved conditionally | BGR7; BGR8; K symmetric | "If" |
| 11841-11857 | Proof of primitive response proposition | proof | Splitting the field into a lift and kernel part solves the constrained equation and recovers its unique multiplier. | proved conditionally | qE=I; qP=0; H invertible; symmetry for BGR9 | "Conversely these formulas satisfy both equations" |
| 11855-11856 | Constrained invertibility suffices | remark | The response proof requires invertibility on the actual constrained slice without requiring positivity of the full Hessian. | proved conditionally | BGR7; proposition proof | "Invertibility was needed on the actual constrained slice" |
| 11859-11864 | Energetic-product and lift bounds | requirement | Uniform response needs bounds on energetic products and a depth-uniform local lift in addition to L. | named open | BGR7–BGR9; LKE; E-sharp KT | "leaves the products" |
| 11866-11888 | Raw-to-per-length conversion | construction | Simultaneous length conversion of data, multipliers, and lifts preserves the Lagrangian and constrained Hessian. | proved in detail | ell=diag(xi_c); raw pairings; BGR9; physical fine normalization | "These conversions preserve both" |
| 11892-11904 | BGR10 / cell-weighted kernel convention | definition | Kernels sum against cell weights and are normalized by input and output amplitudes. | definition | Positive mu_i and s_i; normalized supremum norm | "A kernel is written as" |
| 11902-11904 | Weighted identity kernel | identity | The identity kernel is a delta divided by the input cell weight. | proved in detail | BGR10 | "The identity kernel is" |
| 11906-11914 | BGR11 / exponential two-sided Schur norm | definition | The kernel norm takes the maximum of amplitude-normalized weighted row and column sums. | definition | BGR10; common metric; species weights | "define" |
| 11915-11924 | BGR12 / kernel algebra product bound | estimate | The exponential two-sided norm is submultiplicative. | proved in detail | BGR10; BGR11; metric triangle inequality; absolute convergence | "Indeed, insert the intermediate sum" |
| 11926-11931 | Supremum and weighted square-sum bounds | proof | Row sums control the normalized supremum norm and both sums control the weighted square-sum norm. | proved in detail | BGR11; weighted Cauchy–Schwarz | "To see the latter directly" |
| 11933-11945 | BGR13 / response amplitudes | definition | Potential, gradient, and current amplitudes are inverse first, second, and third powers of local scale. | definition | Actual fine, coarse, and pillar pairings; BGR10 | "the amplitudes are" |
| 11943-11947 | Species and seam normalization | requirement | Actual cell weights, constraint lengths, and species amplitudes must enter before forming or multiplying kernels. | assumed | BGR10–BGR13; declared transpose pairings | "must be inserted before applying" |
| 11949-11954 | Gaussian-coordinate conversion | identity | The change from raw logarithms to canonical Gaussian variables rescales radii by inverse coupling and Hessians by coupling squared. | proved in detail | a=g y; physical radius; BGR10–BGR13 | "A derivative with" |
| 11956-11976 | Uniform response after the primitive bounds | corollary | Primitive kernel bounds control the corrected lift, multiplier response, and force-to-multiplier block. | proved conditionally | BGR7–BGR9; BGR12; BGR14; transpose amplitude convention | "Suppose the actual normalized kernels" |
| 11957-11963 | BGR14 / primitive normalized bounds | hypothesis | Bounds on L, E, KE, and E-sharp K are the inputs for uniform response. | assumed | Actual normalized BGR7 kernels; BGR11 | "satisfy" |
| 11964-11968 | BGR15 / lift and multiplier bounds | estimate | Kernel multiplication bounds T by e+ak and M by k-prime times that quantity. | proved conditionally | BGR14; BGR7; BGR9; BGR12 | "Then" |
| 11970-11984 | Weighted transpose qualification | requirement | Transpose estimates require reciprocal dual amplitudes or a separate check for the chosen physical species. | named open | BGR10; BGR15; force and current amplitudes | "must be checked separately" |
| 11986-11996 | Actual primitive response assembly | proof | The row estimates and projected construction are indicated as supplying BGR14 after derivative transfers and normalization. | sketched | PX156; PX150; construction after PX158; conversions after BGR9 | "The remaining identification consists of recording each block's" |
| 11994-11996 | Remaining species and outward-datum identification | requirement | Every assembled block still needs its species weight and outward datum derivative recorded. | named open | Actual BGR14 assembly | "The remaining identification consists of recording each block's" |
| 12000-12008 | Saddle operator S and reference S0 | definition | S combines the constrained field equation and row equation on fixed paired spaces. | definition | BGR6–BGR9; fixed slice; K; q | "Its domain consists of slice fields and row multipliers" |
| 12008-12015 | BGR16 / complex perturbation premises | hypothesis | A bounded reference inverse and a uniformly small operator perturbation are assumed in the kernel algebra. | assumed | S0; S(B); BGR11; C0 epsilon below one | "If the primitive estimates give" |
| 12016-12021 | BGR17 / complex inverse bound | estimate | A convergent Neumann series bounds the perturbed inverse by C0 divided by one minus C0 epsilon. | proved conditionally | BGR16; BGR12 | "then the Neumann series converges" |
| 12022-12024 | Whole-ball comparison requirement | requirement | The perturbation bound must hold on the entire retained complex ball to support later analytic discs. | assumed | BGR16 | "It is essential that the second bound" |
| 12026-12032 | Relative graph-space perturbation | requirement | An unbounded reference operator must be handled through relative perturbations between its actual graph spaces. | assumed | S0 inverse times S−S0; BGR16–BGR17 | "the correct statement" |
| 12034-12047 | BGR18 / resolvent identity and holomorphy | identity | Operator-norm holomorphy and the resolvent identity give holomorphic inverses, continuity, and differentiation. | proved conditionally | BGR16–BGR17 or convergent relative construction; holomorphic coefficients | "holomorphy follows term by term" |
| 12049-12062 | Actual complex comparison | proof | Local coefficients and projected-current estimates are indicated to give a graph-space comparison after auxiliary-equation matching. | sketched | BGR1; seam-datum-nilpotence; complex-wilson-relative-form; PX158; current expansions; cutoff commutators | "After this" |
| 12057-12060 | Auxiliary and seam matching | requirement | The assembled comparison must match the actual auxiliary equations and seam datum and multiplier normalizations. | named open | Actual S; graph-space comparison | "we must match the auxiliary equations" |
| 12066-12085 | BGR19 / local first-response decay | estimate | A bounded localized forcing column yields exponentially decaying normalized response through the saddle inverse. | proved conditionally | BGR17; BGR6 forcing; support radius r0; amplitude b0; datum derivative | "The proof is the row estimate" |
| 12081-12085 | Proof by weighted row sum | proof | The metric triangle inequality extracts forcing-to-output distance from the inverse row sum. | proved conditionally | BGR17; support and amplitude assumptions; seam-datum-nilpotence | "so multiply by" |
| 12087-12092 | Exponentially local forcing extension | proof | Exponentially decaying forcing gives the same response bound at a smaller common rate. | proved conditionally | BGR19 argument; forcing exponent a; m' below m and a | "Indeed the triangle" |
| 12094-12098 | Separate gradient and current readouts | requirement | A potential-and-multiplier inverse alone does not establish gradient or current response estimates. | named open | Actual primitive inverse; weighted row norm; actual forcing | "Those outputs" |
| 12100-12105 | BGR20 / physical-current derivative | identity | Physical current variation is the derivative of the prescribed current function composed with the field response. | proved in detail | J(U); fixed logarithmic chart; chain rule | "its derivative is" |
| 12106-12111 | Current versus multiplier identification | requirement | Replacing current derivatives by multiplier formulas requires derivation from the physical equation and current definition. | named open | BGR1; J definition; distinction between independent and computed current | "must be derived from (BGR1)" |
| 12118-12129 | BGR21 / translated response equation | identity | Translating the equation gives a difference equation with a coefficient commutator source. | proved in detail | K v=f; mesh shift T; common translation patch | "To prove it, write" |
| 12127-12129 | Boundary translation domain | requirement | The translation calculation must stay on a common interior patch with admissible rows. | assumed | BGR21; boundary geometry | "must be made on the common interior patch" |
| 12131-12138 | BGR22 / divergence-form commutator | identity | A scalar divergence-form operator has a translation commutator built from differences of its coefficients. | proved in detail | K=D-sharp aD+V; constant D; BGR21 | "the coefficient commutator in (BGR21) is" |
| 12139-12147 | BGR23 / energy-dual commutator estimate | estimate | Coefficient difference suprema bound the commutator from energy to dual energy. | proved conditionally | BGR22; stated energy norm; Cauchy–Schwarz | "the bilinear pairing" |
| 12148-12161 | Primitive spatial regularity requirements | requirement | Supremum or Hölder response needs local elliptic bounds and translated interior, gauge, constraint, seam, and boundary commutator estimates. | named open | BGR21–BGR23; actual force/output norms; transport and contour commutators | "Each term must" |
| 12169-12177 | BGR24 / holomorphic first-response premise | hypothesis | A holomorphic normalized readout is assumed to have uniform exponentially localized first derivatives on a product ball. | assumed | Dimensionless bond-logarithm ball; fixed color norm | "Suppose a holomorphic map" |
| 12178-12195 | BGR25 / joint Cauchy derivative estimate | estimate | Cauchy differentiation gives factorial radius losses and decay in the farthest differentiated coordinate. | proved conditionally | BGR24; smaller ball; fixed color polydisc constant; commuting derivatives | "Cauchy's formula applied to the first derivative gives" |
| 12197-12205 | BGR26 / joining-tree comparison | estimate | The minimum spanning-tree length is bounded by the star sum and q times the largest distance. | proved in detail | Underlying metric; star through y | "The star through" |
| 12206-12212 | BGR27 / two-coordinate response estimate | estimate | The second derivative has one radius loss and decay in half the sum of the two distances. | proved conditionally | BGR25; q=2; maximum-distance comparison | "For the second derivative it also gives" |
| 12213-12218 | Fixed-rate arbitrary-order requirement | requirement | Fixed-rate arbitrary-order polymer decay requires nonlinear tree expansions beyond the Cauchy bound. | named open | BGR25; BGR26; nonlinear equations; factorial and entropy costs | "one must use the local nonlinear" |
| 12220-12224 | Hölder-valued Cauchy argument | proof | The same Cauchy proof preserves an already bounded output Hölder seminorm but cannot create one. | proved conditionally | First response bounded in Hölder seminorm on larger ball | "if" |
| 12228-12241 | BGR28 / compatible finite-box difference equation | construction | Comparing finite-box and full equations requires common interior variables and the complete boundary forcing. | assumed | Actual S; prescribed S_Lambda; datum restriction; gauge restoration; cutoff commutator | "their equations must be put on common variables and rows" |
| 12243-12255 | BGR29 / collar-forcing decay | estimate | A polynomially bounded collar force gives exponentially small interior response without a bare-site count. | proved conditionally | Weighted inverse row bound; collar support; force amplitude A R^p | "This follows by extracting the exponential distance" |
| 12257-12266 | BGR30 / exponentially localized collar force | hypothesis | An exponentially decaying collar force also gives the finite-box decay estimate at a smaller rate. | proved conditionally | BGR29 inverse bound; displayed force bound; m' below m and a | "This proves the claim" |
| 12268-12275 | Physical cutoff scaling | estimate | Physical-coordinate cutoffs have first and second normalized differences of orders R inverse and R inverse squared. | proved in detail | Smooth chi(x/R); integral mean-value formula; mesh eta | "by the integral form of the mean-value formula" |
| 12277-12283 | Nonlinear cutoff admission | requirement | Every nontrivial cutoff region requires actual nonlinear forcing and separate field, average, and tower admissibility checks. | named open | Actual nonlinear formula or integral Taylor formula; assigned domains | "is a separate domain check" |
| 12285-12292 | Averaged-Jacobian comparison | requirement | Comparing nonlinear backgrounds requires an admissible common segment and a justified inverse for its averaged Jacobian. | named open | BGR16 common comparison; first-step background section; multilevel ball | "must be justified" |
| 12296-12307 | BGR31 / old-origin substitution | construction | Iterated means of the fine perturbed field define old-origin data on the amplified analytic disc. | definition | M^j; Gamma_j; t, nu, zeta, H, U; old-origin source | "An old-origin source is evaluated on data of the form" |
| 12302-12307 | Full substitution core conditions | requirement | Inner, outer, and removed substitutions must satisfy every assigned field, current, node, gauge, and tower clause. | assumed | BGR31; amplified disc; assigned cores | "Each must satisfy the same list" |
| 12309-12324 | BGR32 / clause-margin admission criterion | estimate | Reference margins and uniformly smaller clause displacements imply that the entire analytic curve stays inside the core. | proved conditionally | Complete reference X0; all hereditary clauses; margins epsilon_a r_a; retained-disc bound | "The proof is the triangle inequality" |
| 12326-12333 | BGR33 / normalized displacement premise | hypothesis | A normalized response displacement bound implies a quantitative condition admitting the amplified inner disc. | assumed | Actual response and average derivatives; C_a; delta_k; sigma_j; alpha_j; margins | "If the actual response and average derivatives imply" |
| 12332-12354 | Window and hereditary margin comparison | proof | Layer decay and the slow-radius inequality uniformly bound the ratios needed to choose a common amplification constant. | proved conditionally | BGR32–BGR33; substitution-room; current and curvature responses; slow-radius inequality; large M | "Choose the common amplification constant" |
| 12356-12366 | Common-branch first-exit argument | proof | Uniform inverse continuation and strict clause margins exclude a first exit from the core. | proved conditionally | Construction after BGR18; BGR32–BGR33; substitution-room; correct substitution addresses | "The branch therefore continues past" |
| 12363-12366 | Substitution address check | requirement | Outer, inner, and removed substitutions must use the assigned tower, current, and node maps. | named open | Full hereditary estimates; common branch | "The finite address check is that the" |
| 12368-12374 | Reference admission at young ages | requirement | The complete unamplified reference must be admitted using the whole-core estimate before spending its remaining margin. | assumed | Young-age whole-core estimate; critical half-datum chart; displacement bound | "The unamplified reference value must also belong to the core" |
| 12376-12381 | Joint-core removed path | requirement | A removed substitution changing field and current together needs a path in the joint core. | assumed | Actual common analytic chart; BGR32; possibly nonconvex hereditary clauses | "must then remain in the" |
| 12396-12407 | BGH1 / lattice differences and Laplacian | definition | Forward and backward physical differences define the nonpositive-symbol lattice Laplacian and its derivative convention. | definition | eta Z^4; eta^4 counting measure; Euclidean distance; fixed alpha | "define" |
| 12411-12417 | BGH2 / unit-lattice heat kernel | definition | Fourier integration of the lattice heat multiplier defines q_T. | definition | omega(theta); unit lattice; T nonnegative | "set" |
| 12418-12427 | BGH3 / positive heat-semigroup expansion | identity | The adjacency-operator series proves that q_T is a nonnegative probability kernel. | proved in detail | Delta1=A−8I; Fourier transform; constant function | "Every coefficient is nonnegative" |
| 12427-12433 | BGH4 / physical heat-kernel density | definition | Rescaling the unit kernel gives the physical density and a contraction on bounded functions. | definition | BGH2–BGH3; eta scaling | "The physical heat-kernel density is" |
| 12438-12450 | Uniform differentiated heat-kernel tails | lemma | Every fixed derivative has uniform polynomial tail bounds in both large- and small-time regimes. | proved in detail | BGH1–BGH4; proof 12452-12530 | "proves (BGH5)" |
| 12441-12449 | BGH5 / differentiated tail estimates | estimate | The weighted absolute derivative tail scales as t to minus r/2 or eta to minus r with arbitrary polynomial decay. | proved in detail | BGH6–BGH10; BGH4; small-time argument | "Substitution" |
| 12452-12530 | Proof of heat-kernel tail lemma | proof | Fourier derivative estimates, weighted Parseval, and Cauchy–Schwarz establish both time regimes after rescaling. | proved in detail | BGH2; BGH4; BGH6–BGH10 | "Substitution" |
| 12453-12463 | BGH6 / difference-multiplier vanishing | estimate | Differentiating the product multiplier leaves the stated power of theta from undifferentiated factors. | proved in detail | Product of r unit-difference Fourier factors | "The bound follows by assigning the derivatives to factors" |
| 12465-12480 | BGH7 / heat-multiplier derivatives | estimate | Repeated derivatives of the heat multiplier have scale powers times a polynomial and Gaussian decay. | proved in detail | omega lower bound and derivative bounds; T at least one | "Multiplying proves (BGH7)" |
| 12482-12493 | BGH8 / Fourier derivative square integral | estimate | Leibniz expansion and four-dimensional scaling give the weighted power T to order minus r minus two. | proved in detail | BGH6; BGH7; scaled integration | "This explains every" |
| 12495-12505 | BGH9 / weighted Parseval bound | estimate | Polynomially weighted square sums of unit heat-kernel differences obey a uniform scaled bound. | proved in detail | BGH8; Parseval; smooth periodic multipliers | "Expand the weight into coordinate monomials" |
| 12507-12520 | BGH10 / reciprocal-weight tail sum | estimate | Comparing unit cubes with a radial integral bounds the reciprocal polynomial weight tail. | proved in detail | T at least one; M>N+2; four-dimensional integration | "One way to check the comparison" |
| 12522-12530 | Tail completion and small-time argument | proof | Weighted Cauchy–Schwarz gives large-time tails and uniformly smooth multipliers give small-time tails. | proved in detail | BGH9; BGH10; bounded multiplier derivatives for T at most one; BGH4 | "The same Parseval argument" |
| 12532 | Small-time derivative necessity | remark | Small-time bounds are needed for second and third discrete differences with constants depending only on fixed orders. | proved in detail | BGH5 proof | "The small-time estimate is needed" |
| 12536-12541 | BGH11 / massive resolvent | definition | Integrating the heat kernel against exponential damping defines the massive resolvent kernel and convolution operator. | definition | Positive mu; BGH4 | "define" |
| 12542-12555 | BGH12 / resolvent equation and uniqueness | identity | The massive resolvent solves the bounded-forcing equation with sup norm at most mu inverse squared and gives its unique bounded solution. | proved in detail | BGH11; heat contraction; bounded Delta_eta at fixed eta | "This also proves uniqueness" |
| 12557-12564 | BGH13 / first resolvent derivative sum | estimate | Integrating the heat derivative estimate gives an absolute first-derivative sum bounded by C/mu. | proved conditionally | BGH5; mu eta at most one | "Integrating (BGH5)" |
| 12566-12577 | BGH14 / translated heat derivative modulus | estimate | Telescoping along a coordinate path bounds translated first heat derivatives by the minimum of first- and second-derivative scales. | proved conditionally | BGH5 with r=1,2; t at least eta squared; lattice displacement | "The second bound follows by summing the second difference" |
| 12579-12590 | BGH15 / logarithmic resolvent modulus | estimate | Time integration gives a first-resolvent-derivative modulus proportional to distance times one plus a logarithm. | proved conditionally | BGH14; small-time bound; eta at most distance at most mu inverse | "Together with the small-time interval, this gives" |
| 12591-12596 | BGH16 / logarithm-to-Hölder inequality | estimate | A power times one plus the logarithm is bounded by an alpha-dependent constant. | sketched | 0<alpha<1; 0<x at most one | "Since for" |
| 12597-12602 | BGH17 / resolvent Hölder modulus | estimate | Both displacement ranges give an alpha-Hölder translation modulus for the first resolvent derivative. | proved conditionally | BGH13; BGH15; BGH16; mu eta at most one | "both ranges imply" |
| 12603-12610 | BGH18 / bounded-forcing gradient regularity | estimate | Convolution with bounded forcing gives uniform gradient and alpha-Hölder gradient bounds. | proved conditionally | BGH13; BGH17; bounded f | "It follows for bounded" |
| 12611-12613 | Endpoint limitation | remark | These estimates do not supply a mesh-uniform Lipschitz bound and may diverge as alpha approaches one. | proved conditionally | BGH15; BGH18 | "do not" |
| 12617-12631 | BGH19 / off-diagonal resolvent derivatives | estimate | Resolvent derivatives through order three have absolute tails of order R to two minus r beyond a fixed fraction of R. | proved in detail | BGH5; R at least eta; mu=1/R; N>max(0,r−2) | "This proves (BGH19)" |
| 12624-12631 | Proof by three time intervals | proof | Integrating the heat tails below eta squared, up to R squared, and above R squared gives the same scale in every interval. | proved in detail | BGH5; exponential damping; chosen N | "which is also" |
| 12633-12635 | Global second-derivative limitation | remark | Only off-diagonal control is asserted for the absolute second-resolvent-derivative sum. | named open | BGH19 | "There is no assertion here" |
| 12639-12641 | Cube convention Q_R | definition | Q_R is the cube of side twice R centered at a lattice point. | definition | Fixed cube ratio | "Let" |
| 12643-12656 | Interior first-difference Hölder bound | theorem | A bounded function with bounded lattice Laplacian has mesh-uniform interior gradient and Hölder-gradient bounds. | proved in detail | R at least 64 eta; u and equation on Q_2R; M and F; proof 12658-12720 | "The constants are independent" |
| 12649-12654 | BGH20 / interior estimate | estimate | The interior gradient scales as M/R+RF and its Hölder seminorm gains the corresponding alpha powers. | proved in detail | Interior theorem hypotheses; BGH12; BGH18; BGH19; BGH21–BGH23 | "Adding the contribution" |
| 12658-12720 | Proof of interior theorem | proof | A separated cutoff and transfer of the commutator to the resolvent kernel avoid any unknown collar gradient. | proved in detail | Interior theorem hypotheses; BGH12; BGH18; BGH19; BGH21–BGH23 | "Move the commutator onto the kernel" |
| 12659-12666 | Separated interior cutoff | construction | A smooth restricted cutoff equals one on Q_R and keeps all difference supports far from the evaluation region. | proved conditionally | R at least 64 eta; smooth cutoff on Q_3R/2 | "makes this separation uniform" |
| 12668-12680 | BGH21 / exact cutoff equation | identity | The cutoff field solves a massive equation with bounded bulk force and a cutoff commutator. | proved in detail | Delta_eta u=f; v=chi u; mu=1/R; BGH12; BGH18 | "the exact product identity is" |
| 12682-12690 | BGH22 / commutator transpose | identity | The scalar Laplacian-cutoff commutator is antisymmetric for the constant cell-weighted pairing. | proved in detail | Scalar multiplication; symmetric Delta_eta; constant pairing | "Move the commutator onto the kernel" |
| 12691-12707 | BGH23 / transferred commutator bound | estimate | Transferring the commutator bounds first and second output derivatives using only the potential supremum and separated resolvent tails. | proved in detail | BGH22; discrete product rule; cutoff bounds; BGH19 | "To check the rule explicitly" |
| 12709-12720 | Completion of interior regularity | proof | Off-diagonal derivative bounds and telescoping give the commutator gradient modulus and complete both interior estimates. | proved in detail | BGH19; BGH23; BGH18; v=u on evaluation cube | "Adding the contribution" |
| 12724-12726 | Finite-dimensional vector extension | remark | The scalar result holds componentwise in any fixed finite-dimensional normed space. | proved in detail | BGH20; equivalence of fixed-dimensional norms | "The result holds componentwise" |
| 12729-12737 | Torus periodization | construction | Periodization preserves derivative-tail and interior estimates when the cubes embed without wrapping. | proved conditionally | Infinite-lattice kernels; BGH19; BGH20; embedded collars, for example periods at least 8R | "the same cutoff proof gives (BGH20)" |
| 12739-12746 | Flat unitary holonomy extension | proof | Unitary factors in the lifted image sum preserve local estimates uniformly in flat holonomies. | proved conditionally | Flat connection; commuting holonomies; embedded common parallel frame; scalar periodization | "Taking the norm and using" |
| 12748-12751 | Flatness and operator-scope restriction | requirement | The preceding proof needs flatness and the componentwise constant-coefficient Laplacian. | assumed | BGH1; holonomy extension | "The argument requires flatness" |
| 12755-12763 | BGH24 / local potential and Laplacian premise | hypothesis | A supplied local real gauge is assumed to bound both the potential and its componentwise Laplacian at the local scale. | assumed | Local real gauge on enlarged cube; C0,C1,m,epsilon,xi | "Suppose a local real gauge has supplied a potential" |
| 12764-12775 | BGH25 / background gradient regularity | estimate | The interior theorem and covering give the stated scaled gradient and Hölder-gradient bounds. | proved conditionally | BGH24; BGH20; local cube covering | "This proves the" |
| 12774-12775 | Missing gauge and nonlinear Laplacian inputs | requirement | The Hölder implication neither constructs the gauge nor proves the nonlinear Laplacian premise. | named open | BGH24 | "does not construct the" |
| 12777-12785 | Coarse-mesh fallback | proof | When the local cube is too small for the theorem, direct differences give the same scaling because xi/eta is bounded. | proved conditionally | BGH24 potential bound; bounded xi/eta; direct first-difference bounds | "They give (BGH25)" |
| 12787-12796 | Covariant componentwise Laplacian | definition | The positive covariant Laplacian is the sum of transpose-gradient products and equals minus Delta_eta at the identity. | definition | Reference U0; local A0; unitary adjoint transports; BGH1 sign | "Thus" |
| 12795-12800 | BGH26 / first transport coefficient | estimate | A small exponential chart bounds the transport difference divided by mesh size by the local potential. | proved conditionally | U0=exp(i eta A0); fixed small chart | "If" |
| 12801-12818 | BGH27 / covariant-to-ordinary Laplacian comparison | estimate | Expanding covariant differences bounds their Laplacian discrepancy by potential, potential-gradient, and field-gradient terms. | proved conditionally | BGH26; integral exponential derivative; common local frame; neighboring stencil | "One can verify this by first writing each covariant first difference" |
| 12813-12820 | Cancellation of apparent inverse-mesh terms | proof | Combining second-difference terms removes isolated inverse-mesh potential-field factors. | proved conditionally | Covariant first-difference expansion; BGH26; transport derivative bound | "the apparent" |
| 12822-12828 | BGH28 / local response readout premise | hypothesis | The local reference potential and its derivative and the response potential, covariant gradient, and Laplacian are assumed bounded. | assumed | Fixed enlargement of local evaluation cube; a0; B | "Assume on a fixed enlargement" |
| 12829-12836 | BGH29 / ordinary response Laplacian bound | estimate | The covariant readouts imply the corresponding ordinary Laplacian bound with a polynomial dependence on a0. | proved conditionally | BGH26; BGH27; BGH28 | "Then (BGH27) implies" |
| 12837-12848 | BGH30 / covariant response Hölder bound | estimate | The interior theorem and coefficient regularity give the alpha-Hölder covariant-gradient readout. | proved conditionally | BGH20; BGH28; BGH29; coefficient difference bounds | "Applying (BGH20)" |
| 12850-12861 | Transported Hölder seminorm | proof | Short-path unitary telescoping extends the local-frame bound to the assigned transported seminorm. | proved conditionally | BGH28; BGH30; transport paths of length at most C times distance | "Hence (BGH30) also holds in that transported seminorm" |
| 12859-12861 | Pointwise gradient premise retained | requirement | The Hölder argument still requires the pointwise covariant-gradient bound. | assumed | BGH28 | "Its premise still includes the pointwise covariant-gradient" |
| 12863-12872 | Physical response Hölder application | proof | Exponential response decay persists through the local Hölder implication once the physical readouts and gauges are identified. | proved conditionally | BGH28; BGH30; local distance comparison; two physical response systems; mechanism (k) | "after obtaining the local real gauge" |
| 12870-12872 | Seam readout and frame comparison | requirement | A seam needs readout verification and comparison of its local frame and equation on a shared two-layer neighborhood. | named open | BGH28; physical response identification; determining neighborhood | "At a seam we must verify these readouts" |
| 12874-12883 | Decoupled-data Hölder route | proof | Arbitrary decoupled data use retained Hölder operator norms and first-order contraction estimates instead of a Laplacian readout. | sketched | Hölder norms of mathfrak G(s), tilde G(s), datum lift; potential/first-difference contraction | "uses the" |

## Forward and backward references

Targets are recorded as written, including references to earlier material outside this chunk and to later arguments within it; no external target was consulted.

- 11466-11469: PX135, label px:flat-layered-row-lift, is a continued display/proof whose beginning precedes this chunk; “the same construction” transfers that lift to real flat connections.
- 11473: “The last proof” refers to the preceding flat row-lift proof.
- 11490: px:flat-field-row-upper, px:flat-feynman-gap, and px:flat-layered-row-lift supply the flat Feynman extension and trace premises.
- 11490: px:flat-layered-row-lift supplies the Landau upper energy cost in px:field-row-extension-premise; fine coercivity is separate.
- 11501: The earlier site-Gram counting weight and its G-prime squared covariance are contrasted with the field-row covariance.
- 11506: “below” promises the admitted-domain row-error and row-trace estimates, supplied here by PX150 and PX155.
- 11510-11521: The block chart specifies the internal transports, coordinate-order path multiset, and actual Federbush mean.
- 11523: The mean contraction is said to have been proved in the block chart.
- 11525: px:actual-one-step-straightening supplies both gauge factors needed for the derivative cancellation.
- 11538: px:finite-one-step-schur is assigned the enlarged one-step polynomial constant.
- 11548: px:actual-one-step-straightening and px:actual-straightened-recursion justify factorization and gauge multiplication order.
- 11552-11554: The primitive regular-pair hypothesis/gauge clause supplies the real local gauges, potential, and first difference.
- 11581: The previously required nonflat torus room permits the larger cutoff cube; the flat periodic formulas need no extension.
- 11583: px:finite-one-step-schur supplies the recursion-ball estimate.
- 11587: px:finite-one-step-schur supplies the Taylor recurrence.
- 11591: px:fluctuation-raw-radii is proved by first exit; px:actual-factorization is the target of the gauge condition-number bound.
- 11593: px:finite-one-step-schur and the preceding summable radii supply the multilevel products.
- 11606: px:actual-row-density supplies the full layered trace estimate.
- 11610: px:flat-row-ltwo supplies the single-row analogue; the carrier argument of px:flat-field-row-upper proves px:actual-row-mass-trace.
- 11619: px:finite-one-step-schur bounds the one-step Hessian used in the fixed-leg sum.
- 11631: px:constraint-hessian-leg-moment supplies the current-form coefficient bound.
- 11639: px:quadratic-current-form-bound extends by coefficients beyond the holomorphic ball; the “second variant” needs separate induced-current and S readouts.
- 11643: px:nonflat-row-error is the estimate to be completed; px:row-dual-bump defines the pillar profiles.
- 11645: The first-order class on a fixed larger cube supplies both comparison gauges.
- 11647: px:actual-row-density supplies seed response comparison.
- 11649: The carrier argument preceding px:flat-average-composition makes the remaining level blocks zero.
- 11658: px:flat-row-mean-comparison is repeated in common gauges; the comparison after px:actual-row-density supplies row and column errors; px:flat-field-local-poincare supplies the local inequality.
- 11671: px:actual-feynman-poincare supplies relative control of the complex Feynman form.
- 11673-11680: Models “(c)” and the three comparison terms in “(d)” supply the projected Landau construction; px:landau-feynman-difference is explicitly not the lower-bound route.
- 11682-11685: The massive all-bare local blocks supply the stated flat boundary inverse bounds.
- 11700-11702: B85c, equations (3.130)–(3.138), are the source of the current-correction expansions.
- 11704-11708: px:constraint-hessian-leg-moment supplies constraint scale factors; mechanism “(g)” supplies small tree vertices after expanding H.
- 11714-11715: B85c, Theorem 3.12, excludes the covariant Laplacian member also not asserted here.
- 11720-11723: The response/current calculations are attached to the preceding construction.
- 11731-11734: ym4:exp500-bg:mb:reduced-datum defines the raw convention used in BGR1–BGR9.
- 11745-11747: The physical stationarity identity is said to be proved above by testing remaining gauge directions.
- 11753-11758: ym4:exp500-bg:mb:reduced-datum defines the exact datum; ym4:exp500-bg:mb:seam-datum-nilpotence computes its logarithmic differentials and finite two-step inverse.
- 11775-11782: BGR4 fixes the curvature term; differentiating BGR1 gives BGR5.
- 11798-11805: BGR4 identifies the physical Hessian, but matching is needed before inserting an independently named propagator into BGR5.
- 11824-11838: The proposition solves BGR6 through BGR7–BGR9.
- 11842-11855: The proof uses BGR6 to derive BGR8, then symmetry gives BGR9 and the displayed M.
- 11866-11888: The conversion after BGR9 prepares the per-length estimates and amplitudes below.
- 11915-11924: BGR10–BGR11 supply the weighted composition convention used to prove BGR12.
- 11943-11947: Actual fine/coarse/pillar pairings fix cell weights; BGR10 and BGR12 require length and species conversions first.
- 11949-11954: Gaussian-coordinate conversion is additional to BGR10–BGR13.
- 11957: BGR7 supplies the actual kernels assumed bounded in BGR14.
- 11964-11984: BGR15 follows from the primitive bounds and kernel products, with a separate weighted-transpose qualification.
- 11986-11990: px:actual-layered-row-lift and px:actual-row-mass-trace supply lift and trace estimates; the projected construction after px:feynman-coefficient-comparison is assigned the other BGR14 bounds.
- 11992-11996: Conversions after BGR9 fix physical datum/multiplier pairings; BGR15 follows after remaining block identification.
- 12005-12008: BGR6–BGR9 specify the saddle system's force and datum spaces.
- 12016-12024: BGR16 is the Neumann-series premise for BGR17 and must hold throughout the retained complex ball.
- 12026-12032: The same series is applied in actual graph spaces when a bounded-operator comparison is unavailable.
- 12034-12044: BGR18 provides the resolvent route to holomorphy, continuity, and differentiation.
- 12049-12062: BGR1 fixes the actual common ball and slice; ym4:exp500-bg:mb:seam-datum-nilpotence supplies outward factors; px:complex-wilson-relative-form, px:feynman-coefficient-comparison, and the projected-current/cutoff construction above are assigned the relative comparison needed for graph-space BGR16.
- 12066-12080: BGR6 defines the forcing species, BGR17 supplies the inverse bound, and BGR10 supplies the output amplitudes for BGR19.
- 12083-12085: ym4:exp500-bg:mb:seam-datum-nilpotence supplies the reduced-datum derivative that must enter the forcing.
- 12087-12092: BGR19 extends to exponentially local forcing at reduced rate.
- 12106-12111: Any multiplier replacement of the current derivative must come from BGR1 and the definition of J; the independent-current core keeps its independent current distinct.
- 12131-12138: BGR21 supplies the translated equation in which the BGR22 scalar commutator is evaluated.
- 12148-12161: The corresponding local elliptic estimate and full gauge-system commutator list are required beyond the inverse-energy argument.
- 12165-12167: BGR19, uniformly on a complex product ball, is the prerequisite for the higher-response Cauchy argument.
- 12183-12195: BGR24 supplies each possible first derivative used to prove BGR25.
- 12205-12218: BGR25 gives a tree rate m/q via BGR26, gives BGR27 for the pointed Taylor remainder, and requires nonlinear tree expansions for a fixed arbitrary-order rate.
- 12220-12224: The same Cauchy argument applies only if the first response already has the larger-ball Hölder bound.
- 12228-12241: The actual saddle operator and its prescribed finite-box version must be reconciled before checking BGR28.
- 12252-12266: The weighted row estimate proves BGR29 and its exponentially localized BGR30 extension.
- 12285-12292: BGR16 is the suggested common comparison for the averaged Jacobian; the first-step background section is said to use it, while a multilevel application needs its own ball.
- 12302-12307: The assigned cores define the complete clause lists for inner, outer, and removed substitutions.
- 12321-12324: BGR32 is proved by triangle inequality, with its application depending on the infinite hereditary list.
- 12334-12354: Section sec:substitution-room supplies the BGR33 normalized displacement, average derivative, reduced-current response, and real-to-complex tower calculation; the response estimate and slow-radius inequality supply the two bounded margin ratios.
- 12352-12353: The common continuation bound “below” is needed with the strict admission inequalities.
- 12356-12366: The inverse construction following BGR18 supplies continuation; BGR32–BGR33 and Section sec:substitution-room prevent first exit.
- 12368-12374: The young-age whole-core estimate replaces the critical half-datum chart for reference admission.
- 12376-12381: The actual common analytic chart and BGR32 are the suggested joint-core route for removed substitutions.
- 12388-12394: The new scalar estimate is to be applied in local real gauges of the background construction.
- 12406-12407: BGH1 defines all derivative products used subsequently.
- 12425-12433: Fourier transformation identifies BGH3 with BGH2; their scaling defines BGH4 and its contraction.
- 12479-12493: BGH7 follows from the product rule; BGH6 and BGH7 imply BGH8.
- 12503-12505: BGH8 controls each monomial in the weighted Parseval estimate BGH9.
- 12522-12530: BGH9 and BGH10 prove the large-time tail; BGH4 rescales both regimes to BGH5.
- 12557-12564: BGH5 with r=1 gives BGH13.
- 12566-12577: BGH5 with r=1,2 gives BGH14 and its small-time substitute.
- 12579-12591: Integration of BGH14 gives BGH15; twice BGH13 handles larger displacements.
- 12591-12613: BGH16 converts both ranges into BGH17 and then BGH18; BGH15 explains the Lipschitz limitation.
- 12624-12631: The two time regimes of BGH5 prove BGH19.
- 12677-12680: BGH12 gives the cutoff resolvent representation and BGH18 gives its bulk contribution to BGH20.
- 12691-12707: BGH22 transfers the commutator; BGH19 ensures the separated kernel is summable and justifies summation by parts.
- 12709-12720: BGH19 bounds BGH23 for j=1,2 and completes the proof of BGH20.
- 12729-12737: Infinite-lattice periodization gives periodic BGH19 and, on embedded cubes, BGH20.
- 12739-12751: The flat-holonomy image-sum argument inherits the scalar estimates and depends on the BGH1 Laplacian.
- 12755-12775: BGH20 yields BGH25 from BGH24, without supplying BGH24 itself.
- 12777-12785: Direct coarse-mesh estimates recover BGH25 and are also assigned to the response application below.
- 12787-12792: The differentiated Euler–Lagrange equation supplies the covariant Laplacian route, with sign convention fixed by BGH1.
- 12813-12818: Expanding first covariant differences identifies the three terms in BGH27.
- 12829-12838: BGH26 and BGH27 convert BGH28 into BGH29; BGH20 then gives ordinary-gradient Hölder control.
- 12850-12861: BGH28 supplies short-path transport control extending BGH30 to the transported seminorm while retaining the pointwise gradient premise.
- 12863-12872: The two physical response systems above and mechanism “(k)” are assigned the real gauge and BGH28 readouts for the physical s=1 application.
- 12874-12883: For arbitrary decoupled data, the already retained Hölder norms of mathfrak G(s), tilde G(s), and the datum lift supply the alternative contraction route.

## Obligations named here

This list records requirements and explicit limits where they occur, including ones subsequently addressed in this chunk.

- 11469: Do not use the flat-frame energy estimate as an ordinary-gradient bound in an arbitrary gauge or as an assumed general nonflat bare field-row bound.
- 11473-11478: Supply the actual row extension and its energy bound (PX136).
- 11486-11490: Supply the separate actual trace estimate (PX138); the flat Landau case still needs fine coercivity.
- 11492-11497: Prove an exponential cell Schur bound for N before applying the inverse-entry conjugation argument.
- 11503-11506: Prove a strict row-error contraction and the E0 energy cost in the actual precision before correcting the nonflat lift.
- 11506: Establish the row-error and row-trace estimates on the admitted domain.
- 11525: Use both internal gauge factors in the actual straightening to obtain its claimed flat derivative.
- 11552-11554: Supply local real gauges through the primitive regular-pair hypothesis rather than infer them from curvature.
- 11581: Provide the torus room for the larger nonflat cutoff cube.
- 11587-11591: Choose the common ceiling small enough for first-exit control, strict one-step ball inclusion, and the gauge condition-number bound.
- 11639: Bound the actual induced current H[J]-transpose J in the stated row norm.
- 11639: Bound S in the weighted fine energy spaces for the second variant.
- 11653: Choose a depth-, volume-, and M1-independent weak-field ceiling making the lift error smaller than one.
- 11664: Absorb the Poincare mass error with the fixed weak-field ceiling and retain bare identity-row boundary control.
- 11671-11685: Complete the projected estimate through the local constrained models and boundary construction.
- 11711-11713: Check species weights in identifying the current-expanded products with actual blocks.
- 11711-11713: Check derivative allocation in those products.
- 11711-11713: Check adjacent-level endpoint equations in those products.
- 11714-11715: The covariant Laplacian member excluded in B85c Theorem 3.12 is not asserted.
- 11748-11751: Include the derivative of the slice when the reference moves with the datum.
- 11753-11758: Keep the actual outward-block derivatives in the reduced-datum forcing.
- 11775-11776: Retain the constraint-curvature contribution in the constrained Hessian.
- 11794-11796: Differentiate explicit parameters before substituting the solution.
- 11798-11805: Match the full independent-current and gauge normal form before using a separately named propagator in BGR5.
- 11809-11813: For an operator-space extension of the algebraic inverse, ensure all displayed inverses and compositions exist.
- 11816-11823: Supply surjectivity of q, a right inverse E, an isomorphism P onto its kernel, and invertibility of H.
- 11859-11864: Control LKE and E-sharp KT, and the size and locality of a lift uniform in layer count.
- 11866-11888: Convert raw datum, its dual multiplier, and its lift together before using per-length estimates.
- 11943-11947: Use actual pairings and insert constraint lengths and species amplitudes before kernel multiplication at seams.
- 11957-11963: Supply the actual normalized primitive bounds in BGR14.
- 11970-11984: Check the weighted transpose separately when force/current amplitudes are not reciprocal dual amplitudes.
- 11994-11996: Record every assembled block's species weight and outward datum derivative.
- 12008-12024: Establish BGR16 with a strictly small perturbation throughout the whole retained complex ball.
- 12026-12032: Use relative perturbations on actual graph spaces when the reference operator is unbounded in the chosen norm.
- 12034-12047: Supply operator-norm holomorphic coefficients and a genuine complex norm comparison or another convergent inverse construction.
- 12057-12060: Match auxiliary equations and every seam's datum and multiplier normalizations to the actual saddle operator.
- 12083-12085: Include the exact reduced-datum derivative in the forcing column.
- 12094-12098: Construct the actual primitive inverse, verify its weighted row norm, and compute actual datum forcing.
- 12096-12098: Supply separate gradient and current readout maps if the inverse controls only potential and multiplier.
- 12106-12111: Derive any multiplier formula for the current derivative from BGR1 and J, keeping independent and computed currents distinct until the physical pair is imposed.
- 12127-12129: Perform translated equations only on the common admissible interior patch at boundaries.
- 12148-12151: Supply a local elliptic estimate to pass from energy regularity to supremum or Hölder regularity.
- 12153-12161: Bound the translated interior equation, gauge-row commutator, constraint-row commutator, and every seam or exterior boundary row in their actual norms.
- 12165-12177: Establish uniform holomorphic first response on the larger complex product ball before applying joint Cauchy estimates.
- 12213-12218: Use nonlinear tree expansions with factorial and entropy costs if an arbitrary-order polymer estimate needs a fixed decay rate.
- 12220-12224: Supply first-response Hölder control on the larger ball before taking Cauchy estimates in that seminorm.
- 12228-12241: Put finite-box and full equations on common rows, verify the exact difference identity, and include boundary, datum, gauge-restoration, and cutoff forces.
- 12240-12241: Redo the comparison if an actual boundary is replaced by Dirichlet boundary conditions.
- 12268-12275: Construct cutoffs in physical coordinates and distinguish normalized from unnormalized differences.
- 12277-12283: Include every nontrivial nonlinear cutoff point in the transition collar and check field, average, and tower admissibility separately.
- 12285-12292: Justify the averaged-Jacobian inverse along a common admissible segment on the actual multilevel ball.
- 12302-12307: Admit the full amplified disc, including all field, independent-current, node, gauge, and hereditary tower clauses for each substitution.
- 12309-12324: Supply reference margins and uniform displacement control for every clause in the infinite hereditary list.
- 12326-12354: Verify BGR33 and choose the common amplification constant from the normalized gap and slow-radius suprema.
- 12356-12363: Supply common analytic continuation with uniform radius before using first exit to prove admission.
- 12363-12366: Check that outer, inner, and removed substitutions use their assigned tower, current, and node maps.
- 12368-12374: Admit the complete unamplified reference, using the young-age whole-core estimate where appropriate, before spending displacement margin.
- 12376-12381: Keep the joint field/current comparison path inside the joint core for removed substitutions.
- 12435-12448: Supply both time regimes of the differentiated heat-kernel tails; these are proved in 12452-12530.
- 12557: Impose mu eta at most one for the first-resolvent-derivative estimates.
- 12611-12613: No mesh-uniform Lipschitz conclusion for the resolvent gradient is supplied from bounded forcing alone.
- 12633-12635: No globally uniform absolute second-resolvent-derivative sum is asserted.
- 12644-12648: Supply the equation and bounded data on the enlarged cube, with R at least 64 eta and all evaluation differences inside the specified enlargement.
- 12682-12683: Avoid an unknown cutoff-collar gradient by transferring the commutator to the kernel.
- 12729-12737: Ensure torus cubes and collars embed without wrapping for the local cutoff argument.
- 12748-12751: Retain flatness and the componentwise constant-coefficient Laplacian for the flat-holonomy argument.
- 12755-12775: Supply the local real gauge and the nonlinear componentwise-Laplacian bound in BGH24; the Hölder implication does not prove them.
- 12795-12800: Keep the local transport in a fixed small exponential chart for BGH26.
- 12822-12828: Supply the local reference-potential bounds and all three response readouts in BGH28 on the enlarged cube.
- 12850-12861: Use controlled-length comparison paths for transported seminorms and retain the pointwise covariant-gradient premise.
- 12868-12872: Obtain the physical real gauge and three readouts from the response systems and their mechanism-(k) identification.
- 12870-12872: At seams, verify the readouts and compare the local frame and equation on the common two-layer determining neighborhood.
- 12874-12883: For decoupled data use the retained Hölder operator norms; a componentwise-Laplacian bound is not among the declared norms.
