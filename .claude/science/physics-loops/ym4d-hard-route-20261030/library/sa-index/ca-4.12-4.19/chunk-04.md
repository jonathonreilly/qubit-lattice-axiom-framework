# Chunk 04: lines 46477-47775
Sections: Continuation of item 4.14 (no section/subsection command occurs here); Bonds, parities and pairings (46486); Symmetries (46506); Symmetric cell weights and lattice-symmetry covariance (46511); Local balls at cut-off radius M/2L (46800); Unit-lattice operators at complex configurations (46952); Walk expansion of the form and base-point bound (47253); Positivity, sector bound and inversion of the block (47686); Step 1: positivity at real backgrounds (47728).

Labels in the table omit the common 4.14: prefix. “Sketched” for the last lemma records that its proof is incomplete within this chunk.

| Lines | Name / tag | Kind | What it states (one plain sentence, your words) | Status here | Reads (inputs it uses, by tag or name) | Key phrase |
|---|---|---|---|---|---|---|
| 46477-46482 | Unit-frame remark, continued | remark | No hull or partition normalization is needed and enlarged boxes lie in Ω_k. | proved conditionally | A2; prop-prepared-data-admissible; B-CMP122a pp.178–179 | "by (A2)" |
| 46486-46504 | Bonds, parities and pairings | definition | Reversal, endpoint sets, representation action, even/odd fields, trace pairing and w notation are fixed. | definition | not-free-current-notation; eq-free-current-notation-c | "A bond field $F$ is called" |
| 46506-46509 | Symmetry group | definition | Reflections and coordinate permutations act on bond spaces, while r in format brackets denotes analytic radius. | definition | Bond spaces | "It acts on bond spaces" |
| 46511-46601 | lem-symmetry-covariance | lemma | Symmetric weights preserve sheet estimates and the current form and yield termwise symmetry covariance. | proved conditionally | Local-term, branching and connector lemmas; elementary covariance; block-size floors | "Then the following hold." |
| 46516-46524 | Local N hypotheses and N_z | hypothesis | N has specified range, local norm and analytic radius and is localized with symmetric cell weights. | assumed | Local-term lemma; eq-free-current-notation-b | "Let $N$ be an operator" |
| 46525-46528 | eq-symmetry-covariance-1 | estimate | N has the enlarged operator-class radius and coefficient bound displayed. | proved conditionally | Local N hypotheses; connector lemma; symmetric weights | "holds in the form" |
| 46530-46532 | eq-symmetry-covariance-2; n_w | estimate | At most three times (2dL+1)^d blocks lie within weighted distance dL. | proved conditionally | M/L>dL; layer grids | "at most $3(2dL+1)^d$ in all" |
| 46533-46538 | Branching, sheet properties and natural weights | proposition | Branching constants and range enlarge as stated while sheet properties and weight covariance persist. | proved conditionally | Branching lemma; weight definition; odd L | "The branching lemma holds" |
| 46539-46558 | eq-symmetry-covariance-3; W_π replacement | identity | Replacing S_- by half S leaves the symmetric current operator unchanged. | proved in detail | Letter definitions; commutator antisymmetry; polarization | "their symmetrisations coincide" |
| 46560-46563 | eq-symmetry-covariance-4 | identity | Dλ is odd and Sλ is even under bond reversal. | proved in detail | Reversal and representation conventions | "Thus $D\lambda$ is odd" |
| 46564-46565 | Odd A,J convention | hypothesis | A and J follow the reflected-bond convention of B-CMP119. | assumed | B-CMP119 | "Take $A$ and $J$ odd" |
| 46567-46572 | eq-symmetry-covariance-5 | identity | Both displayed trilinear terms are orientation independent. | proved in detail | Parities; trace conjugation invariance | "are independent of the orientation" |
| 46573-46588 | eq-symmetry-covariance-6 | identity | Symmetry bijections transport supports, domains and C, J, shifted-inverse and K terms by conjugation. | proved conditionally | Elementary covariance; products; inversion; hulls; core classes; Schur complement | "This clause rests on" |
| 46590-46596 | Elementary covariance inputs | hypothesis | Averaging kernels, geometric letters, differential letters and walks are covariant. | assumed | Averaging scheme; B-CMP99b §C | "The averaging scheme used in this chapter is covariant" |
| 46603-46798 | Proof of symmetry lemma | proof | Local estimates, commutators, parities and transport induction establish the four clauses. | proved conditionally | Connector and branching lemmas; floors; elementary covariance; B-CMP96 (2.3); B-CMP119 | "We now proceed by induction along the construction" |
| 46604-46614 | Distance from bookkeeping block | proof | The endpoint connector gives distance at most dL. | proved conditionally | Connector lemma (i); B-CMP96 (2.3) | "therefore $d(y(\iota),z)\le dL$" |
| 46616-46633 | Decay; eq-symmetry-covariance-7 | estimate | Localized decay coefficients satisfy Sh3 and the stated row-sum bound. | proved conditionally | N locality and norm; weight bounds | "Their row sums satisfy" |
| 46635-46645 | Counting proof | proof | A short path reaches at most three layers with at most (2dL+1)^d blocks each. | proved conditionally | eq-block-size-conditions-a; layer grids | "The number $n_w$ depends on $(d,L)$ only." |
| 46647-46657 | Sheet and branching proof | proof | Enlarged domains preserve the other sheet properties and only two branching constants change. | proved conditionally | Sh1–Sh5; branching lemma | "its proof goes through with the same two changes" |
| 46659-46668 | Naturality proof | proof | Symmetries preserve the endpoint counts defining weights, unlike anchor indicators. | proved in detail | Odd L; centered blocks; eq-free-current-notation-b | "These are the numerator and the denominator" |
| 46670-46681 | Scalar proof; eq-symmetry-covariance-8 | identity | S−2S_- equals ηD and its trace pairing vanishes on equal commutator arguments. | proved in detail | Letter definitions; trace pairing | "vanishes on equal arguments" |
| 46683-46691 | Bilinear proof | proof | The difference of the bilinear forms is antisymmetric and disappears under symmetrization. | proved in detail | Scalar identity; commutator | "the two symmetric operators coincide" |
| 46693-46708 | Word replacement proof | proof | The letter replacement preserves orders and does not increase weights. | proved conditionally | Word lemma for the form; operator theorem series | "their weights are at most the old ones" |
| 46710-46725 | Parity proof | proof | Evaluation on reversed bonds directly establishes the D and S parity formulas. | proved in detail | Reversal; D and S definitions | "For $D$," |
| 46727-46738 | Orientation proof | proof | Conjugation cancels in the trace and both parity products are positive. | proved in detail | eq-symmetry-covariance-5; parity signs | "This product is $(-)(-)(+)=+$" |
| 46740-46747 | Remaining-letter parity | remark | The vertex exchanges parity and the coarse odd letters pair with odd current without orientation dependence. | proved conditionally | Coarse reversal rule; averaged configuration | "exchanges parities" |
| 46749-46773 | Transported objects and bound-only auxiliaries | construction | Symmetries transport term-defining data while anchors and bookkeeping choices affect bounds only. | proved conditionally | Hulls; averaging covariance; B-CMP109 pivot; weights | "The proof is transport of structure" |
| 46775-46798 | Covariance induction | proof | Covariance propagates through products, inversion, core classes and the Schur complement. | proved conditionally | Elementary covariance; B-CMP99b §C; B-CMP119 | "We now proceed by induction along the construction" |
| 46779-46782 | Fixed-order contour caveat | remark | Covariance is not deduced from the nonsymmetric fixed-order contours. | cited | B-CMP98; B-CMP109 | "as noted in \cite{B-CMP109}" |
| 46800-46828 | lem-local-balls | lemma | A cutoff at M/2L embeds local perturbations in the global analytic domain inside a one-cube collar. | proved conditionally | Sheet format; A1; M>2L; theorem E | "Then the following hold." |
| 46801-46811 | Local ball and collar | definition | A global real U and local perturbations of star norm below r/2 define a local ball about a term support. | definition | S_u or core form; U_R; weighted distance | "is called the \emph{local ball}" |
| 46812-46814 | eq-local-balls-1 | definition | The cutoff is a truncated linear function of weighted distance. | definition | [ν]; M,L; weighted distance | "Put" |
| 46817 | Inclusion α | proposition | The cutoff support and weighted neighborhood lie in the one-cube collar. | proved conditionally | A1; compatible grids; layer spacings | "So $C$ touches the cube $Q$" |
| 46818 | Admission β | proposition | Cut-off complex perturbations and current lie in U(r). | proved conditionally | Local star norm; M>2L | "Hence it lies in $\mathcal{U}(r)$." |
| 46819-46823 | Analyticity γ | proposition | Local terms are extension-independent and analytic with W3′, W5cov and W6geo. | proved conditionally | Reading; β; theorem E | "it defines $T_\nu$ on the local ball" |
| 46825-46827 | M/2 cutoff caveat | remark | A larger cutoff does not guarantee collar inclusion at a coarser seam. | proved in detail | Coarser-layer metric; L≥2 | "is no longer guaranteed" |
| 46830-46885 | Proof of α | proof | Layer separation and grid spacing force any nearby cube to touch the support. | proved conditionally | A1; prepared-data admissibility; compatible grids | "This lower bound is condition (A1)" |
| 46887-46919 | Proof of β | proof | The discrete Leibniz estimate keeps the cut-off star norm below r. | proved conditionally | Block-size condition (iii); local ball | "The discrete Leibniz rule gives" |
| 46921-46931 | Proof of γ | proof | Reading locality and linear cutoff composition yield extension independence and analyticity. | proved conditionally | S_u reading; analytic U(r); theorem E | "So $T_\nu$ is analytic on the local ball." |
| 46933-46944 | Proof of larger-cutoff caveat | proof | The coarse-layer path bound can exceed a grid spacing and fails to force touching. | proved in detail | L≥2; coarse spacing | "no longer forces $C$ to touch $Q$" |
| 46946-46950 | Operator theorem H | proposition | The local-ball lemma gives H at ε₁ and at 1 for J and permits collar data. | proved conditionally | lem-local-balls; thm-operator-theorem H | "data given on the one-cube collar" |
| 46952-47063 | lem-unit-lattice-operators | lemma | Unit-lattice operators extend analytically to complex backgrounds with uniform coefficient, inverse and averaging bounds. | proved conditionally | Averaging analyticity theorem; uniformity lemma; complex averaging proposition; regularity ceilings and radii; B-CMP98, B-CMP109 | "with the following property" |
| 46953-46964 | Average, blocks, contours and pivot | definition | M, its k-fold iterate, centered blocks, contour transport and the middle pivot bond are fixed. | definition | def-block-average; Bałaban contours; odd L | "we call $b_0(c)$ the pivot of $c$" |
| 46965-46971 | eq-unit-lattice-operators-1 | definition | Φg and Φflat are logarithmic changes of contour transport and block averaging under e^{iB}. | definition | M; contour transport; complexified Lie algebra | "put" |
| 46972-46980 | Homogeneous parts; eq-unit-lattice-operators-2 | definition | Homogeneous parts define LQflat, g and C^(2), with C^(2) polarized symmetrically. | definition | Unit-lattice operator definition; B-CMP109; Φ | "homogeneous of degree $n$ in $B$" |
| 46981-46990 | Kernel, π_c; eq-unit-lattice-operators-3; source vertex | definition | The kernel normalization, pivot coefficient, Cflat, h, G and source vertex are specified. | definition | Unit-lattice operator definition; B-CMP109 (2.5) | "the pivot coefficient" |
| 46992-46998 | r_flat, W and P | hypothesis | W has small real plaquettes on the read blocks and P restricts both complex perturbations below r_flat. | assumed | d,L; operator supports | "Let $W$ be $G$-valued" |
| 47000-47001 | Joint analyticity, item 1 | proposition | Both Φ maps are jointly analytic and bounded by one on P. | proved conditionally | Averaging analyticity theorem; uniformity lemma; B-CMP98 Propositions 3,7 | "is jointly analytic on $\mathsf{P}$" |
| 47002-47008 | eq-unit-lattice-operators-4 | estimate | Homogeneous coefficients obey power bounds and a linear background-increment bound. | proved conditionally | Item 1; Cauchy estimate; Schwarz lemma | "The Cauchy estimate" |
| 47009-47020 | Pivot smallness and inverse, item 3 | proposition | Under two stated smallness conditions the real and complex pivot inverses have bounds two and four. | proved conditionally | C′₁L²ā₀≤1/2; 8L^{d−1}sup A″≤r_flat²; B-CMP98 (139),(140); item 2 | "Assume $C'_1L^2\bar a_0\le\tfrac12$." |
| 47021-47035 | Admission of averaged backgrounds, item 4 | proposition | U(1) with the prescribed ceiling and A′ radius yields admissible W and V and analytic local operators. | proved conditionally | def-real-backgrounds; eq-block-size-conditions-b,d; items 1–3; B-CMP98 Propositions 2,6 | "Assume the ceiling on the regularity" |
| 47036-47045 | eq-unit-lattice-operators-5 | estimate | Kernels, g, C^(2), pivot inverse, Cflat and the source vertex satisfy the displayed uniform bounds. | proved conditionally | Item 4 hypotheses; coefficient estimates; polarization | "obey the bounds" |
| 47046-47061 | eq-unit-lattice-operators-6; θ_k and κ | estimate | Multilevel Q_j kernels are bounded by 2(1+θ_k)≤4 and one-step averaging is analytic. | proved conditionally | Complex averaging proposition; B-CMP98 (124); B-CMP99b (3.15); α₀,α₁ radii | "satisfy" |
| 47065-47251 | Proof of unit-lattice lemma | proof | Analytic generating functions, coefficient extraction, pivot estimates and averaging bounds prove the five items. | proved conditionally | Averaging analyticity and uniformity results; complex averaging proposition; ceilings; B-CMP98, B-CMP109 | "Items (1)--(3) and the increment therefore apply." |
| 47066-47074 | Proof of item 1 for Φg | proof | The averaging analyticity theorem applies also to backgrounds close to unitary ones. | proved conditionally | Analyticity theorem clause (c); B-CMP98 Proposition 7 | "Joint analyticity and the bound are clause (c)" |
| 47076-47099 | Proof of item 1 for Φflat | proof | Three analytic near-identity factors have an analytic logarithm bounded after shrinking r_flat. | proved conditionally | B-CMP98 (89),(62),(120),(126),(164), Proposition 3; uniformity lemma | "we decrease $r_{\flat}$ until" |
| 47101-47116 | Proof of item 2 | proof | Cauchy bounds control homogeneous terms and Schwarz controls their background increments. | proved conditionally | Item 1; homogeneity; Cauchy and Schwarz | "the Schwarz lemma" |
| 47118-47167 | Proof of real pivot estimate | proof | Exactly L contours contain the pivot, giving an isometric main coefficient with a small remainder. | proved conditionally | Support definition; contour convention; B-CMP98 (124),(139),(140); item 3 smallness | "the Neumann series gives" |
| 47165-47167 | Flat pivot check and example | remark | The identity-background coefficient agrees with B-CMP109 and the d=1,L=3 example counts three contours. | proved in detail | B-CMP109 (0.12); pivot contour count | "For $d=1$, $L=3$" |
| 47169-47185 | Increment and complex pivot inverse | proof | The coefficient increment is small enough for a uniformly convergent analytic Neumann inverse. | proved conditionally | Item 2; real inverse bound; 8L^{d−1}sup A″≤r_flat² | "the Neumann series converges uniformly" |
| 47187-47231 | Proof of item 4 | proof | Regularity ceilings admit the averaged background and radius bounds permit composition with analytic local operators. | proved conditionally | real-backgrounds-a; block-size-conditions-b,d; B-CMP98 (53),(164),(27), Propositions 2,6; items 1–3 | "Analyticity in $A'$ follows from the joint" |
| 47233-47242 | Proof of item 5 | proof | The complex averaging proposition applies to compositions of one-step operators and their generating-function derivatives. | proved conditionally | Complex averaging proposition; analyticity theorem; B-CMP98 (124),(139); B-CMP99b (3.15) | "so that proposition applies to them" |
| 47244-47250 | Two dependence remarks | remark | Complex (139) does not depend on the analyticity theorem and the local constants depend only on d,L. | assumed | Complex averaging bounds; form-bound lemma; a₁⊕,a₀⊕ | "does not depend on the analyticity" |
| 47253-47283 | prf-form-walk-expansion | lemma | The form has convergent inverse series, a complex symmetric sheet expansion, a norm bound and base-point positivity. | proved conditionally | Operator theorem hypotheses; elementary, locality, inversion, flattening, assembly and coercivity results | "Assume the hypotheses of the operator theorem at free current" |
| 47254-47260 | Walk-expansion hypotheses | hypothesis | A1,A2, the four named floors and three named ceilings are assumed. | assumed | prepared-data-admissible-a; block-size-conditions-a,b; B-CMP122a pp.178–179 | "printed without proof" |
| 47263-47268 | Inverse-series conclusion (a) | proposition | q1 and q2 converge absolutely on U(1) and identify Gπ,G₁ and inverses of T,Tπ,T₁. | proved conditionally | Assembly stages 1,3; walk-sheet lemma for T inverse | "converge absolutely" |
| 47269-47273 | eq-form-walk-expansion-1 | estimate | Q belongs to the unit sheet class with radius 8dL²M₁sharp. | proved conditionally | Assembly stage 5; all lemma hypotheses | "Stage 5 yields" |
| 47274-47276 | Symmetry and locality (c) | proposition | Q is complex symmetric, real at real points, covariant and geometry-local on enlarged lists. | proved conditionally | Letter properties; reading hulls; assembly | "hold operator by operator" |
| 47277-47280 | Schur bound (d) | estimate | Q has operator norm at most γ₁=eB_Q S_u(δ_Q). | proved conditionally | Sheet class; Schur bound | "The bound (d) is the Schur bound" |
| 47281 | Base-point bound (e) | estimate | Q at the identity and zero current is bounded below by γ₀. | proved conditionally | Graph identification; coercivity proposition (b); A1,A2; floors | "The first argument gives (e)." |
| 47287-47684 | Walk-expansion proof | proof | Seven inputs assemble the form and trace the exact floors, ceilings and conventions used. | proved conditionally | Inputs (i)–(vii); operator theorem hypotheses | "We supply the inputs (i)--(vii)" |
| 47295-47324 | Input (i): elementary sheets | construction | Complex elementary walk expansions retain norm constants under enlarged reading domains. | proved conditionally | Elementary-sheet lemma; B-CMP99b Theorems 3.4,3.7,3.9,3.10; u1; hull lemma (iv); τ1 | "have walk expansions at complex $\mathbf{U}$" |
| 47312-47316 | Enlarged X and ρ₀ | definition | The elementary domains use enlarged boxes and radius c_X(d)L²M₁. | definition | eq-free-current-notation-a | "The domains are taken as in convention" |
| 47326-47348 | Input (ii): local operators | construction | Symmetric weights change locality and branching constants and expand the listed local complex operators. | proved conditionally | Symmetry lemma (a); elementary sheets; complex localization proposition | "The properties" |
| 47350-47379 | Five-link Δ^(2) chain | proof | Complex localization, Cauchy differentiation and projection bounds supply the displayed Δ^(2) estimate. | proved conditionally | Complex (139); localization proposition and corollary (iii′); averaging lemma; projection (iv); B-CMP98 (142),(159)–(163); L≥8 | "each feeding the next" |
| 47354-47356 | Localization radius and floor | requirement | α₀ must be placed as in complex averaging and the L≥8 floor imposed. | assumed | fl-L; block-size-conditions-a | "is imposed" |
| 47381-47387 | Input (iii): unit-lattice operators | construction | The unit-lattice lemma supplies complex PΛ,Cflat,G and source vertices under the radius and ceiling restrictions. | proved conditionally | lem-unit-lattice-operators; cl-reg+; a₁⊕ minimum members 2–4 | "are supplied by" |
| 47389-47394 | Input (iv): singular word b | construction | The three-factor singular word is expanded with orders (1,0,1) and smooth junctions. | proved conditionally | Singular-word lemma; DG′,D*G₀D,G′D* | "The singular-word lemma expands it" |
| 47396-47426 | Input (v), t1: many-scale sheet setup | construction | Product and flattening operations use a many-scale frame, second cover and enlarged hull lists. | proved conditionally | Walk-sheet lemma; product; flattening F1; τ0–τ3; B-CMP96 Lemma 2.1; hull lemma (i)–(iii) | "are applied to" |
| 47416-47420 | Box property b3 floor | requirement | The second-cover size must exceed 2Lρ₀ to use b3 at the enlarged radius. | assumed | fl-sharp′; free-current-notation-a | "It follows from" |
| 47428-47502 | t2: real-background positivity | proof | Identity positivity and seven localization steps yield T-tilde(U)≥m_flat/2. | proved conditionally | Positivity lemmas; IMS floor; tail bound; reg-sharp; cl-reg-sharp; B-CMP96 Proposition 2.7 | "Assembling the box estimates" |
| 47445-47451 | IMS error and partial-walk tail | estimate | The IMS error is at most m_flat/6 and the partial-walk tail at most m_flat/12. | proved conditionally | b1,b2; F_ms^P; positivity lemma | "This bound follows from the floor" |
| 47452-47464 | Local gauge and complex path | construction | A regularity gauge and cutoff define a complex disc path lying in the elementary sheet fibre. | proved conditionally | reg-sharp; a₁el; a_sharp | "lies in the fibre of the sheet" |
| 47465-47478 | Gauge and reading identity | identity | Gauge covariance and support reading identify the partial walk sum with the path value at one. | proved conditionally | Sh4; Sh2; support within box cubed | "By $(\mathrm{Sh}2)$" |
| 47479-47496 | Schwarz comparison and regularity ceiling | estimate | The stated radius threshold controls the box increment and follows from cl-reg-sharp. | proved conditionally | Schwarz lemma; r_sharp; cl-reg-sharp | "This holds, with a factor $L^2$ to spare" |
| 47504-47511 | t3: sectoriality | estimate | The real part of T-tilde is at least m_flat/4 on U(1). | proved conditionally | Sectoriality lemma; a₁⊕≤ε_T a₁el | "This holds on $\mathcal{U}(1)$" |
| 47513-47526 | t5: inversion floor and sheet | construction | The many-scale inversion lemma gives the stated inverse sheet under F_ms. | proved conditionally | Inversion lemma; coercivity m_flat/4; fl-sharp′ | "It requires the floor" |
| 47528-47531 | t6: flattened inverse | estimate | Flattening F2 gives T inverse in the stated order −2 operator class. | proved conditionally | Flattening lemma F2; t5 | "Part (F2) of the flattening lemma gives" |
| 47533-47541 | Assembly alphabet and tail range | construction | Operators are collected with a common radius and rate and tails within the admissible interval. | definition | Inputs i–v; e=8+d; vertex constants | "The alphabet $\mathfrak{L}$ collects the operators" |
| 47543-47553 | Assembly word convention | identity | The half-S convention gives the same Wπ with zero-order words and no larger weights. | proved conditionally | Symmetry lemma (b); free-current-notation-c | "this is the same symmetric operator" |
| 47555-47578 | Five-stage assembly | construction | Two inverse stages alternate with current-vertex branching before summation and flattening produce Q. | proved conditionally | Branching, summation, product and flattening F3; unit-lattice operators; assembly | "The five stages, numbered $1$ to $5$" |
| 47580-47584 | Assembly radius constraints | requirement | a₁⊕ is a minimum of four radii and a₀⊕ satisfies four smallness conditions controlling c_g. | assumed | eq-block-size-conditions-d; unit-lattice lemma; ε_T a₁el | "the four smallness conditions displayed there" |
| 47586-47600 | Sheet properties and bound proof | proof | Operatorwise symmetry, uniform analytic limits, hull locality and Schur bounds prove (b)–(d). | proved conditionally | Weierstrass; hull lemma (iii),(iv); Schur estimate | "hold operator by operator" |
| 47602-47634 | Input (vii): base-point proof | proof | Graph identification and coercivity at trivial background yield γ₀. | proved conditionally | Coercivity proposition (b); A1,A2; fl-99; fl-M′ i–ii; B-CMP96 Proposition 2.7 | "Part (b) of the coercivity proposition" |
| 47616-47624 | Four coercivity conditions | hypothesis | Admissibility, trivial-background conditions, data floors and criticality are the four inputs to coercivity. | assumed | Coercivity proposition; prepared-data-admissible-a; block-size-conditions-a | "The proposition gives this bound under four conditions." |
| 47631-47634 | Alternative lower-bound proof | remark | A separate Jensen and two-block Poincaré proof is mentioned but not used. | sketched | Jensen inequality; two-block Poincaré inequality; j=k, Ω_t | "it is not used here" |
| 47636-47660 | Hypothesis-use ledger | remark | The proof identifies where A1,A2, each floor and ceiling, reg-sharp and u1 enter. | proved conditionally | Steps i–vii; operator theorem hypotheses | "The hypotheses" |
| 47662-47676 | Applicability of cited proofs | proof | The changed conventions alter only diameters, constants, a scalar and d,L numbers without reversing inequalities. | proved conditionally | Cited lemmas i–vi; notation a–c; radius floors | "No inequality changes direction" |
| 47678-47683 | Partial-walk support requirement | requirement | The path identity requires each selected walk support to lie where the cutoff is one. | assumed | t2δ; Sh2; box cubed; b3 at ρ₀ | "needs only that the support" |
| 47686-47715 | prf-positivity-inversion | lemma | Q has real positivity and a complex sector bound and its shifted block has a uniform inverse sheet. | sketched | Operator theorem hypotheses; walk-expansion lemma; unit-frame positivity and inversion | "Then the following hold." |
| 47687-47692 | Positivity-inversion hypotheses | hypothesis | The operator theorem hypotheses and an arbitrary sub-block B⊂B+ are fixed. | assumed | thm-operator-theorem; prf-form-walk-expansion | "Assume the hypotheses" |
| 47693-47700 | m₁, ε₁, B₀, μ₁, δ₀ | definition | Constants and the reduced analytic radius are defined from the walk-expansion bounds. | definition | γ₀,γ₁,B_Q,δ_Q; S_u | "put" |
| 47703 | Real positivity (a) | estimate | Every admitted real background satisfies Q(U,0)≥γ₀/2. | sketched | Unit positivity lemma; regularity and floors; base-point bound | "Step 1: positivity at real backgrounds." |
| 47704 | Complex sector bound (b) | estimate | Re Q≥m₁ on U(ε₁). | sketched | Operator theorem hypotheses; ε₁; positivity | "on $\mathcal{U}(\varepsilon_1)$" |
| 47705-47711 | Shifted block inverse (c) | estimate | For x≥0 the inverse sheet has radius M/4 and x-independent walks and domains, including C=A inverse. | sketched | A=Q_BB; m₁,B₀,δ₀,ε₁; inversion hypotheses | "with walks and domains independent of $x$" |
| 47717-47726 | Positivity-inversion proof opening | proof | The previous lemma supplies sheet, symmetry, reading and norm bounds and implies γ₀≤γ₁. | proved conditionally | prf-form-walk-expansion; Schur bound | "Evaluating both bounds on a unit vector" |
| 47728-47736 | Unit box system | construction | Cubes of side M/12d and product cutoffs have the specified overlap, Lipschitz, width and hull constants. | definition | Unit box system; B+; b1–b4 | "We use the unit box system" |
| 47738-47743 | Unit box size requirements | requirement | b3 requires M≥144dρ_Q and the construction also requires ℓ≥6 and integer M/ℓ. | assumed | block-size-conditions-a, floor M (iii) | "These require the following." |
| 47745-47753 | b4 inclusion and containing M-cube | proof | A2 places the enlarged unit box and a containing M-cube inside Ω_k. | proved conditionally | A2; dist(Ω_t,Ω_k complement)≥6M; B+ geometry | "This follows from condition (A2)" |
| 47755-47764 | Unit positivity floor | requirement | Applying unit-frame positivity requires F_u^P with the displayed parameters. | assumed | block-size-conditions-a, floor M (v); unit-frame positivity lemma | "Its floor condition is" |
| 47766-47770 | IMS error; eq-positivity-inversion-1 | identity | Q equals its cutoff-localized sum plus the half double-commutator error D. | proved in detail | Partition of unity; commutator expansion | "Expanding the double commutator" |
| 47771-47775 | IMS error bound | estimate | b1,b2 and the sheet estimate bound D by γ₀/6. | proved conditionally | F_u^P; unit-box constants; sheet Schur bound | "the last inequality by the floor condition" |

## Forward and backward references

References are listed by their occurrence here; a range groups adjacent references in the same argument. Targets inside this chunk are retained as well as targets elsewhere.

- 46479-46481: A2 of Proposition 4.14:prop-prepared-data-admissible; B-CMP122a pp.178–179, explicitly printed without proof.
- 46484, 46503-46504: Definition 4.14:not-free-current-notation and 4.14:eq-free-current-notation-c define the notation and w.
- 46497-46498: 4.14:eq-symmetry-covariance-4 uses conjugation for Lie-algebra-valued site fields.
- 46513: Definition 4.14:not-free-current-notation supplies the lemma's notation.
- 46516-46524: Local-term lemma, product-construction junction indicators and 4.14:eq-free-current-notation-b supply N assumptions, χ_y and w_z.
- 46533-46537: Branching lemma and the operator construction's sheet format Sh1–Sh5.
- 46550-46558: 4.14:eq-free-current-notation-c defines W_π; the form's word construction supplies polarized words.
- 46564-46565: B-CMP119 supplies the reflected-bond convention.
- 46573-46578: Product, local-term, branching, inversion, core and form-word constructions; Lemma 4.14:lem-reading-hulls supplies inversion hulls.
- 46590-46596: Covariance of the chapter's averaging scheme; B-CMP99b §C supplies walks from Δ′_a,Q′ and its R.
- 46599-46600: Clause (d) is the covariance clause of Theorem 4.14:thm-operator-theorem.
- 46605-46613: 4.14:eq-free-current-notation-b defines the weight numerator; connector lemma (i) supplies weighted connector length; B-CMP96 (2.3) supplies the endpoint exclusion.
- 46622-46623: 4.14:eq-free-current-notation-b gives 0≤w_z≤1.
- 46629-46632: Sh3 is applied with explicitly defined coefficients.
- 46638-46645: 4.14:eq-block-size-conditions-a supplies M/L>dL; the count proves 4.14:eq-symmetry-covariance-2.
- 46655-46657: Branching lemma proof is reused with the row bound 4.14:eq-symmetry-covariance-7 and enlarged radius.
- 46666-46667: 4.14:eq-free-current-notation-b identifies the invariant numerator and denominator.
- 46670-46681: Letter definitions give the scalar identity; 4.14:eq-symmetry-covariance-8 implies 4.14:eq-symmetry-covariance-3.
- 46693-46708: Word lemma for the form and the first two defining Q series in Theorem 4.14:thm-operator-theorem determine where S_- occurs.
- 46725, 46734: Parity proof establishes 4.14:eq-symmetry-covariance-4 and applies it to 4.14:eq-symmetry-covariance-5.
- 46756-46758: Lemma 4.14:lem-reading-hulls defines midpoint rules, index sets and concentric hulls.
- 46761: B-CMP109 identifies the middle pivot bond.
- 46762-46764: Averaging-scheme transformation properties include averaged-bond reversal.
- 46769-46773: Connector and branching lemmas provide bound-only auxiliaries; clause (a) supplies the symmetric-weight definition of terms.
- 46775-46782: Chapter averaging covariance and B-CMP99b §C supply elementary covariance; B-CMP98 fixed-order contours are excluded as its derivation, with the asymmetry noted in B-CMP109.
- 46784-46797: Product, local-term, branching, inversion, core and Schur-complement constructions propagate 4.14:eq-symmetry-covariance-6 to Theorem 4.14:thm-operator-theorem; B-CMP119 is identified as the only published convention on which this covariance rests.
- 46801-46802: The S_u sheet format and its core form supply the class of T.
- 46821-46823: Theorem 4.14:thm-operator-theorem clause E, 4.14:eq-operator-theorem-a, lists W3′, W5cov and W6geo.
- 46831-46832: 4.14:eq-local-balls-1 proves the first cutoff inclusion.
- 46846-46848: A1 of 4.14:eq-prepared-data-admissible-a and Proposition 4.14:prop-prepared-data-admissible provide layer separation, stated without proof in B-CMP122a pp.178–179.
- 46914-46915: Item (iii) of 4.14:eq-block-size-conditions-a guarantees M>2L.
- 46921-46931: The S_u reading property gives extension independence; operator theorem E supplies the inherited properties.
- 46946-46950: Theorem 4.14:thm-operator-theorem H, 4.14:eq-operator-theorem-a, is identified with Lemma 4.14:lem-local-balls at the two radii.
- 46953-46957: Notation 4.14:not-free-current-notation supplies Q; Definition 1.5:def-block-average supplies the iterated block average.
- 46959-46962: Bałaban's contours and middle-bond convention supply transport and pivots.
- 46973-46990: Unit-lattice operator definitions and B-CMP109 identify the Φ coefficients; B-CMP109 (2.5) identifies G.
- 47014-47017: B-CMP98 (139), as placed by the averaging analyticity theorem, supplies C′₁.
- 47021-47027: Definition 4.14:def-real-backgrounds supplies η and U_R; 4.14:eq-block-size-conditions-b,d supply the regularity ceiling and a₁⊕.
- 47032-47034: B-CMP109 (0.6) supplies gauge covariance.
- 47046-47061: B-CMP98 (124) and B-CMP99b (3.15) give multilevel compositions; 4.14:eq-real-backgrounds-a supplies u1 and α₀; the complex averaging proposition supplies c‴,c-natural and the kernel bound; the analyticity theorem gives the generating-function derivative interpretation, using 4.14:eq-unit-lattice-operators-5.
- 47066-47074: Averaging analyticity theorem clause (c) and its final near-unitary assertion apply to B-CMP98 Proposition 7's V′V₀ background.
- 47076-47099: B-CMP98 (89),(62),(120) give the factorization; Proposition 3 and its stated uniformity at V′V₀, the uniformity lemma and the theorem's placement clause supply the middle factor; (126) is the changed bound and (164) bounds the adjoint.
- 47101-47116: Item 1 and Cauchy estimates establish item 2 and 4.14:eq-unit-lattice-operators-4; Schwarz supplies the increment.
- 47118-47133: Unit-lattice operator support definitions identify g,a,Q₁ and the difference operator; B-CMP98 (124) in the analyticity theorem gives Q′₀; B-CMP109 supplies contour and corridor conventions.
- 47143-47147: The analyticity theorem's straight-contour convention and one-element averaging property identify the pivot transporter.
- 47151-47163: B-CMP98 (139),(140), in the analyticity theorem's form, bound the remainder; item 3's hypothesis permits Neumann inversion.
- 47165-47167: B-CMP109 (0.12) is the flat pivot consistency check.
- 47169-47185: Kernel convention, 4.14:eq-unit-lattice-operators-2 and item 2 give the increment and complex inverse.
- 47187-47200: 4.14:eq-real-backgrounds-a supplies local regularity; 4.14:eq-block-size-conditions-b,d fix constants and ceilings; B-CMP98 Proposition 2, (53) bounds averaged plaquettes.
- 47201-47216: B-CMP98 Proposition 6, (164), and (27) give analytic A″ and its logarithmic bound; members 2 and 3 of 4.14:eq-block-size-conditions-d imply the required smallness.
- 47217-47231: Items 1–3, the increment and 4.14:eq-unit-lattice-operators-3 yield the bounds; B-CMP109 (0.6) supplies inherited gauge covariance.
- 47233-47242: Complex unit-lattice averaging proposition, complex B-CMP98 (139), and the analyticity theorem's placement clause provide item 5; B-CMP98 (124), B-CMP99b (3.15), and the unit-lattice composition definition identify the multilevel operators; the generating function and display 5 supply analyticity.
- 47244-47250: The complex (139) input is declared independent of the analyticity theorem; the lemma bounding Q uses items 3–4 through its constant and a₁⊕,a₀⊕.
- 47254-47260: Theorem 4.14:thm-operator-theorem hypotheses are A1,A2 in 4.14:eq-prepared-data-admissible-a, Proposition 4.14:prop-prepared-data-admissible as printed without proof in B-CMP122a, and floors/ceilings in 4.14:eq-block-size-conditions-a,b.
- 47263-47268: q1,q2 are the series of operator theorem A.
- 47285: This lemma is identified as the first step of the operator theorem proof.
- 47288-47293: Inputs i–vii use earlier lemmas under conventions 4.14:eq-free-current-notation-a,b,c and Notation 4.14:not-free-current-notation.
- 47295-47310: Elementary-sheet lemma norm clauses n1–n3 rest on B-CMP99b Theorems 3.4,3.7,3.9,3.10; (3.35) is u1 of 4.14:eq-real-backgrounds-a; (3.43),(3.44) at one-half give n2,n3; (3.94),(3.108) give an extra improving factor.
- 47312-47324: 4.14:eq-free-current-notation-a sets domains; reading-hulls lemma (iv) gives Sh5; the many-scale frame τ1 preserves Sh3.
- 47326-47337: Convention b and symmetry lemma (a) adjust locality and branching constants while preserving sheet properties.
- 47339-47348: Elementary-sheet lemma and Bałaban's construction supply Q′,S,a and vertices; complex localization proposition, complex B-CMP98 (147), supplies Q and its transpose.
- 47350-47379: First complex localization lemma is complex B-CMP98 (139); the localization proposition uses α₀ and fl-L of 4.14:eq-block-size-conditions-a; its first corollary is complex (148) via Cauchy; part iii′ and the averaging lemma feed complex projection iv; its estimate rests on B-CMP98 (142),(159)–(163); the complex averaging constants and kernel differentiation identity enter as values.
- 47381-47387: Lemma 4.14:lem-unit-lattice-operators supplies the complex unit-lattice operators using cl-reg+ in 4.14:eq-block-size-conditions-b and minimum members 2–4 in 4.14:eq-block-size-conditions-d.
- 47389-47394: Singular-word lemma supplies orders and junctions.
- 47396-47409: Walk-sheet lemma for T inverse uses product and flattening F1; many-scale connection lemma and τ0–τ3 supply the frame; B-CMP96 Lemma 2.1 bounds S_ms under fl-M′(ii).
- 47410-47426: Second-cover properties b1–b4 and Sc apply at ρ₀ under fl-sharp′ and convention a; reading-hulls lemma i–iii supplies the inversion sheet properties on enlarged lists.
- 47428-47441: Walk-sheet, inversion and flattening F2 define the route from T to its inverse; identity and real-background positivity lemmas are invoked; B-CMP96 Proposition 2.7 on a collar-enlarged Ω gives identity positivity.
- 47443-47464: Real-background positivity lemma supplies seven steps; b1,b2 and F_ms^P in fl-sharp′ control IMS; reg-sharp in 4.14:eq-real-backgrounds-a supplies a gauge; elementary-sheet radius supplies the complex path.
- 47465-47478: Sh4 and Sh2 give the gauge and reading equalities.
- 47479-47499: Schwarz and cl-reg-sharp of 4.14:eq-block-size-conditions-b bound the box comparison; the identity positivity lemma supplies the base point.
- 47504-47511: Sectoriality lemma applies in A′; the definition of a₁⊕ supplies its radius inequality.
- 47513-47526: Inversion lemma and fl-sharp′ supply the inverse sheet, whose μ_T is fixed in the walk-sheet lemma.
- 47528-47531: Flattening lemma F2 gives the order −2 inverse.
- 47533-47553: Assembly supplies admissible tails and alphabet constants; convention c and symmetry lemma b justify half-S words.
- 47555-47578: Assembly stages invoke branching twice, summation, product and flattening F3; stage 5 gives 4.14:eq-form-walk-expansion-1, stages 1 and 3 give q1,q2 inverses, and input v gives T inverse.
- 47580-47584: 4.14:eq-block-size-conditions-d and the unit-lattice lemma define a₁⊕ and the four a₀⊕ smallness conditions.
- 47586-47600: Weierstrass gives analytic limits; reading-hulls lemma iv and iii give geometry locality; the sheet Schur bound gives (d).
- 47602-47615: Identification of the form on the graph equates Q with the unit-lattice averaging form B; the unit-lattice lemma identifies C^(2); coercivity proposition b supplies γ₀^X/c_Φ².
- 47616-47624: Four coercivity conditions use A1,A2 from prepared-data-admissible-a and its proposition as printed without proof in B-CMP122a; fl-99 and fl-M′ i–ii in block-size-conditions-a supply the data condition; the other conditions are trivial at the identity.
- 47626-47634: The first proof uses elementary expansions and B-CMP96 Proposition 2.7 on extended domains; a second Jensen/two-block Poincaré proof is mentioned as independent of B-CMP99b and unused.
- 47639-47644: A1 is used as B-CMP96 (2.1)–(2.2) at two block-size pairs, in Lemma 2.1 at M/L, and with fl-M′ i to give Sc.
- 47645-47647: A1,A2 are inputs to the B-CMP99b analysis and the coercivity proposition at Λ=Ω_t^(k).
- 47648-47659: The ledger locates fl-99, fl-sharp′, fl-M′, fl-L, cl-99, the unit-lattice lemma's cl-reg+ members, reg-sharp and cl-reg-sharp, and u1 from Definition 4.14:def-real-backgrounds and real-backgrounds-a.
- 47662-47676: Lemmas i–vi remain applicable under conventions a–c; smallness constants refer to block-size-conditions-d and the unit-lattice lemma; τ1 remains valid.
- 47678-47683: The t2δ identity uses support containment in the cutoff-one region; b3 at ρ₀ bounds the changed tail.
- 47687-47692: Theorem 4.14:thm-operator-theorem supplies hypotheses and blocks; Lemma 4.14:prf-form-walk-expansion supplies constants.
- 47713-47714: Conclusions a and c are identified with the operator theorem's B first clause and D second half, at 4.14:eq-operator-theorem-a.
- 47718-47726: Unit sheet notation and Lemma 4.14:prf-form-walk-expansion supply the proof inputs; Schur supplies γ₁.
- 47728-47736: The unit box system supplies cutoffs, projections and b1–b4.
- 47738-47743: Floor M item iii of 4.14:eq-block-size-conditions-a supplies diameter, grid and minimum-side conditions.
- 47745-47753: A2 of prepared-data-admissible-a and its proposition, stated without proof in B-CMP122a pp.178–179, implies unit-box inclusion.
- 47755-47764: Definition 4.14:def-real-backgrounds fixes U; unit-frame positivity lemma uses floor M item v of block-size-conditions-a; B-CMP99b's localization sentence and Sect. B are the indicated positivity argument being expanded.
- 47771-47775: b1,b2, the sheet bound and F_u^P give the displayed IMS error estimate.

## Obligations named here

These entries distinguish explicit assumptions and required inequalities from outstanding proofs; satisfying a condition within this chunk does not make it an open problem.

- 46479-46481: A2 is borrowed from prepared-data admissibility, explicitly printed without proof in B-CMP122a.
- 46516-46519: The local N input requires locality, range c_N, the block norm estimate and analytic radius r.
- 46564-46565: A and J must use the odd reflected-bond convention.
- 46587-46596: Term covariance rests on elementary-letter covariance, including the stated covariance of the averaging scheme.
- 46638-46640: The short-path count needs M/L>dL, supplied by the block-size conditions.
- 46801-46809: The local-ball construction assumes a sheet or core form, a real U on the whole lattice and local star norms below r/2.
- 46825-46827, 46933-46943: The collar inclusion is explicitly not guaranteed at cutoff M/2; the given argument does not establish it there.
- 46846-46848: Layer separation A1 is an admissibility input stated without proof in B-CMP122a.
- 46914-46915: Admission into U(r) needs M>2L, supplied by block-size item iii.
- 46992-46998: W must be G-valued with read plaquettes bounded by r_flat and perturbations in P must be smaller than r_flat.
- 47009-47020: Pivot inversion assumes C′₁L²ā₀≤1/2, and complex inversion additionally needs 8L^{d−1}sup|A″|≤r_flat².
- 47021-47027: Item 4 assumes the regularity ceiling and the a₁⊕ radius in the A′ direction.
- 47091-47099: The analytic factor argument uses uniformity of Proposition 3 at V′V₀ and shrinks r_flat to make the logarithm and bound valid.
- 47159-47160, 47178-47185: Real and complex Neumann inversions explicitly use the item 3 smallness hypotheses.
- 47187-47216: The admitted averaged background must satisfy the plaquette ceiling and the second and third radius-minimum restrictions; the text verifies these implications.
- 47254-47260: Walk expansion assumes A1,A2, fl-99, fl-sharp′, fl-M′, fl-L, cl-99, cl-reg+ and cl-reg-sharp; admissibility is again explicitly cited without proof.
- 47303-47308: The B-CMP99b elementary expansion requires background condition (3.35), identified with u1.
- 47354-47356: Complex localization imposes the prescribed α₀ placement and L≥8.
- 47384-47387: Complex unit-lattice operators require the r_flat members of cl-reg+ and minimum members 2–4 for a₁⊕.
- 47407-47408: The many-scale summation bound requires fl-M′ ii.
- 47416-47420: Box property b3 requires M₁sharp>2Lρ₀ at the enlarged radius.
- 47445-47448: The IMS error bound uses the positivity floor F_ms^P inside fl-sharp′.
- 47452-47464: The local comparison path requires a gauge supplied by reg-sharp and must remain inside the elementary analytic fibre.
- 47479-47496: Schwarz comparison needs the displayed lower bound on r_sharp, equivalently the displayed upper bound on a_sharp, supplied by cl-reg-sharp.
- 47504-47511: Complex sectoriality on U(1) requires a₁⊕≤ε_T a₁el.
- 47513-47520: Inversion requires the displayed F_ms floor, included in fl-sharp′.
- 47533-47536: Assembly tails are chosen in [-5,5] within the admissible range [-e,e].
- 47580-47584: a₁⊕ must satisfy four radius restrictions and a₀⊕ four smallness conditions; these alone constrain c_g here.
- 47616-47624: Coercivity has four conditions, supplied respectively by A1,A2, triviality at the identity, the data floors and trivial criticality.
- 47639-47659: The hypothesis ledger requires the listed admissibility, floor, ceiling and background assumptions at their named points of use.
- 47667-47673: Reusing the cited proofs requires floors at the changed diameters and the specified alphabet, current-radius and d,L constants.
- 47678-47683: The gauge/path identity requires selected walk supports inside the region where the cutoff equals one.
- 47687-47692: Positivity and inversion assume the operator theorem hypotheses and the preceding walk-expansion constants.
- 47738-47743: Unit b3 requires ρ_Q≤ℓ/12, equivalently M≥144dρ_Q, and the box construction requires ℓ≥6 and integer M/ℓ.
- 47745-47753: Unit b4 requires the enlarged box inside Ω_k, supplied by A2, itself cited from a statement without proof.
- 47755-47761, 47771-47775: Unit-frame positivity and its IMS error require F_u^P with the displayed parameters.

No statement here explicitly says a new theorem “remains to be proved.” The last lemma's proof stops at the IMS error estimate because the chunk ends; its real positivity, complex sector bound and inversion conclusions are not fully proved within these lines.

## For the stage question

- 46477-46481 — **proved conditionally**: Unit-frame grids and partitions are independent of the nest; A2 admits the enlarged boxes inside Ω_k, with A2 cited from a statement without proof.
- 46516-46528 — **proved conditionally**: Local operator sheets retain analytic radius r while range and domain diameter enlarge.
- 46573-46596, 46749-46798 — **proved conditionally**: Symmetry transports the defining data, supports and domains through each construction stage; anchors and bookkeeping choices enter bounds only.
- 46801-46814 — **definition**: A local analytic ball uses perturbations of star norm below r/2 near a support, but its real reference U is specified on the whole lattice.
- 46817-46823, 46830-46931 — **proved conditionally**: The cutoff admits (e^{iηχA′}U,χJ) into U(r), preserves local term values, and gives analytic extension-independent terms on local balls.
- 46825-46827, 46933-46943 — **proved in detail**: The argument explicitly fails to guarantee one-cube collar inclusion at the larger cutoff M/2.
- 46946-46950 — **proved conditionally**: Operator theorem H uses radius ε₁, or radius 1 for J; data on the weighted neighborhood, hence on the collar, suffice.
- 46953-46980 — **definition**: At step k the operators depend on V=M^k(U-bold), and perturbation B takes values in the complexified Lie algebra.
- 46992-47008 — **proved conditionally**: For real W with small plaquettes, both logarithmic maps are jointly analytic on the two-variable complex domain P and obey homogeneous and increment bounds.
- 47009-47020, 47169-47185 — **proved conditionally**: Small complex increments preserve pivot invertibility, bound the inverse by four, and give analytic inverse dependence.
- 47021-47045, 47187-47231 — **proved conditionally**: The prescribed ceilings and a₁⊕ radius admit averaged U(1) backgrounds into the local complex operator domain; analyticity, supports, gauge covariance and geometric locality persist, and J does not enter these formulas.
- 47046-47061, 47233-47242 — **proved conditionally**: Multilevel averaging operators on all layers have complex kernel bounds and analytic one-step factors.
- 47066-47074 — **proved conditionally**: The analyticity input includes backgrounds within e^τ of unitary ones, with the stated radius and isometry-factor changes.
- 47076-47099 — **proved conditionally**: The group-average logarithm is analytic for the complex background through three near-identity factors, using uniformity at V′V₀.
- 47244-47250 — **assumed**: The dependence remarks say complex (139) does not depend on the analyticity theorem and local bounds depend on d,L rather than k.
- 47254-47281 — **proved conditionally**: The form's inverse series converge on U(1), the form is complex symmetric and real symmetric on real points, and it has a base-point lower bound, under the named admissibility and size hypotheses.
- 47295-47324 — **proved conditionally**: Elementary walks exist at complex U-bold under u1, with enlarged reading domains but unchanged decay constants.
- 47326-47379 — **proved conditionally**: Local operators and the Δ^(2) source vertex are bounded at complex U-bold via the complex localization chain.
- 47381-47387 — **proved conditionally**: Complex unit-lattice operators entering assembly are supplied only with the specified cl-reg+ and a₁⊕ restrictions.
- 47428-47502 — **proved conditionally**: Positivity is extended from the identity to every U in U_R using localized gauges, tails and Schwarz comparison.
- 47452-47478 — **proved conditionally**: The complex path u_z lies in the sheet fibre; at z=1 its local walk values agree with the gauged real background because supports lie in the cutoff-one region.
- 47479-47496 — **proved conditionally**: The comparison disc must meet the stated radius threshold, and reg-sharp/cl-reg-sharp enter only in the gauge and Schwarz steps.
- 47504-47511 — **proved conditionally**: The sectoriality radius contains U(1) because a₁⊕ was chosen below ε_Ta₁el.
- 47513-47531 — **proved conditionally**: Inversion and flattening construct T inverse at analytic radius 1 under the stated coercivity and floor.
- 47533-47578 — **proved conditionally**: The five assembly stages construct Gπ and Tπ inverse, insert j₀ in Δ^(2), construct G₁ and T₁ inverse, insert j in the source vertex, and form Q by summation and flattening.
- 47580-47584 — **assumed**: Assembly radii are the prescribed minimum and four smallness constraints, rather than independent enlargement choices.
- 47586-47600 — **proved conditionally**: Uniform analytic limits and geometry-determined supports preserve the assembled sheet properties.
- 47602-47629 — **proved conditionally**: The identity/zero-current point lies on the graph, every J vertex vanishes there, and graph identification plus coercivity give the lower bound.
- 47639-47659 — **assumed**: The background class for elementary sheets and tower bounds is the class fixed by u1, with reg-sharp reserved for the named comparison steps.
- 47678-47683 — **proved conditionally**: Enlarging walk supports makes fewer walks qualify for the partial sum, and the discarded tail is controlled by b3 at ρ₀; this is a walk-selection statement, not a claim about background drop-outs.
- 47686-47715 — **sketched**: The final lemma states positivity for all U_R, sectoriality on U(ε₁) and shifted inverses there with walks and domains independent of x; the proof is unfinished in this chunk.
- 47718-47726 — **proved conditionally**: The previous complex sheet bounds and identity positivity imply γ₀≤γ₁, used later to ensure r_reg>1.
- 47728-47753 — **proved conditionally**: The unit-box system and a containing M-cube fit inside Ω_k using A2, with the necessary size floors.
- 47755-47775 — **proved conditionally**: The real-background positivity argument starts with an admitted U_R and the unit-frame positivity floor, deriving the IMS identity and error bound.

There is no explicit discussion here of minimisers, carried effective terms at renormalization stages, background drop-outs, or prepared shells. “Stages” here name the covariance induction and the five-stage operator assembly. Prepared large-field data appear through the A1/A2 admissibility assumptions, not through a shell-admission construction.
