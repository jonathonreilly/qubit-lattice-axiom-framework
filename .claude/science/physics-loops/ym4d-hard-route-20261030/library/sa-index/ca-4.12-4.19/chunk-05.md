# Chunk 05: lines 47746-49044
Sections: No section or subsection command occurs in this excerpt; internal titled divisions are positivity proof (continued, 47746), Step 2: the sector bound (47850), Step 3: inversion of the block (47863), Block identities, resummed expansions and uniformity (47895), Conventions at a large-field operation (48141), Small boxes in unions of grid cubes (48263), The hull of a second-cover box in one cube (48337), The printed gauge family of the hull's cube (48479), Tiling, later steps and earlier drop-outs (48684), The auxiliary integer's power against the block count (48867), Remarks (48953), The top power against every lower level (48993; proof continues beyond this chunk).

Labels below retain the source's 4.14: prefix; short clause references refer to the operator theorem or the immediately named lemma. Conditional status records stated dependencies, not an assessment of correctness. The opening proof is a continuation; the final proof is incomplete within this excerpt.

| Lines | Name / tag | Kind | What it states (one plain sentence, your words) | Status here | Reads (inputs it uses, by tag or name) | Key phrase |
|---|---|---|---|---|---|---|
| 47746-47753 | Prepared-data condition (A2) | hypothesis | The prescribed separation places the enlarged boxes inside the outer domain. | assumed | 4.14:eq-prepared-data-admissible-a; 4.14:prop-prepared-data-admissible; B-CMP122a pp. 178–179 | "without proof" |
| 47749-47753 | Containing cube Q | construction | A2 gives an M-cube containing the twice enlarged box and a relevant bond. | proved conditionally | A2; ℓ=M/(12d); bond in the top region | "Hence it lies inside" |
| 47755-47764 | Positivity floor Fᵖᵤ | requirement | Sheet positivity uses item (v) of the prescribed floor on M. | assumed | 4.14:def-real-backgrounds; 4.14:eq-block-size-conditions-a(v); positivity lemma for sheets | "which is item (v) of the floor" |
| 47755-47848 | Real positivity argument, continued Step 1 | proof | Localization, gauge cutoff, and analytic comparison with the identity background yield Q≥γ₀/2. | proved conditionally | A2; (b1)–(b3); sheet bounds; real-background regularity; positivity floor; regularity ceiling; Sh2, Sh4; flat lower bound | "This is (a)." |
| 47766-47770 | D; 4.14:eq-positivity-inversion-1 | identity | The double-commutator error expresses Q as its localized pieces plus D. | proved in detail | Partition identity Σh_b²=1; definition of D | "Expanding the double" |
| 47771-47775 | Localization error bound | estimate | The double-commutator norm is at most γ₀/6. | proved conditionally | (b1), (b2); sheet bound; Fᵖᵤ | "the last inequality by the floor condition" |
| 47777-47781 | Local walk sum Qᵇ and tail E_b | definition | Qᵇ retains walks inside the enlarged box and E_b is the remaining compressed tail. | definition | Walk expansion of Q; projection 1″ | "partial walk sum" |
| 47782-47787 | Tail estimate | estimate | The excluded walks have norm at most γ₀/12. | proved conditionally | (b3); first line of Fᵖᵤ | "the last inequality by the first line" |
| 47789-47798 | Extended gauge, cutoff χ, analytic path u_z, radius r_reg | construction | A regular gauge and cutoff produce backgrounds in U(1) for complex parameters of modulus below r_reg. | proved conditionally | 4.14:def-real-backgrounds; 4.14:prf-form-walk-expansion; a₁⊕; A and ∇A bounds | "we have" |
| 47800-47812 | 4.14:eq-positivity-inversion-2 | identity | Covariance and local reading identify Qᵇ at the original background with a unitary conjugate of Qᵇ(u₁). | proved conditionally | Gauge invariance of U_R; Sh4; Sh2; cutoff construction | "By the reading property" |
| 47814-47821 | Analytic local family and regularity ceiling | requirement | The ceiling on a_Q makes the analytic comparison radius at least 12 and bounds the family by γ₁. | assumed | 4.14:eq-block-size-conditions-b; sheet analyticity; uniform convergence; Schur bound | "ceiling on the" |
| 47823-47834 | Schwarz comparison estimate | estimate | Schwarz applied to matrix elements bounds Qᵇ(u₁)−Qᵇ(u₀) by γ₀/6. | proved conditionally | Analytic path; Schur bound γ₁; regularity ceiling; Schwarz lemma | "The Schwarz lemma therefore gives" |
| 47836-47848 | Local and global positive lower bounds | estimate | The flat lower bound survives tail errors and localization to give Q(U,0)≥γ₀/2. | proved conditionally | Flat positivity; tail bound; positivity-inversion-2; Schwarz estimate; positivity-inversion-1 | "Summing over the boxes" |
| 47850-47861 | Step 2: the sector bound | proof | The sector lemma extends real positivity to Re Q≥γ₀/4 on the complex ball U(ε₁). | proved conditionally | Step 1; sector lemma; complex-fibre analyticity; sheet matrix-element bound; unit-frame distance property | "No further hypothesis is used." |
| 47857-47860 | Sector radius ε=ε₁ | definition | The sector radius is γ₀/(8γ₁) and its lower-bound constant is m₁=γ₀/4. | definition | γ₀; γ₁; sector lemma | "Its radius is" |
| 47863-47883 | Step 3: inversion of the block | proof | Compression preserves the sector bound and sheet inversion gives uniform resolvent expansions and C. | proved conditionally | Q sheet; Step 2; inversion lemma; (b1)–(b4); A2; M floors (iii), (iv) | "The lemma gives" |
| 47869-47875 | Inversion floor Fᵤ | requirement | Block inversion requires item (iv) of the M conditions. | assumed | 4.14:eq-block-size-conditions-a(iv); A2; unit box system | "which is item (iv) of the floor" |
| 47876-47883 | Resolvent sheet and C=A⁻¹ | estimate | Nonnegative-x resolvents have a common walk system with domain radius M/4 and the specified norm and decay constants. | proved conditionally | Sheet inversion; ρ_Q≤M/(144d); B₀, m₁, μ₁, δ₀ | "with walks and domains independent of" |
| 47885-47892 | Arbitrary index sets and unused enlarged lists | remark | Irregular bond sets are allowed and this argument uses neither reading hulls nor second-cover regularity. | proved conditionally | Unit frame; A2; inversion lemma; M-cube regularity | "irregular subsets" |
| 47895-47920 | 4.14:prf-block-identities — Block identities, resummed expansions and uniformity | lemma | Inputs (a)–(d) imply the operator theorem's remaining clauses and its covariance, dependence, and Schur-complement statements. | proved conditionally | 4.14:thm-operator-theorem; inputs (a)–(d); form-walk and positivity-inversion lemmas | "Suppose that the following hold" |
| 47896-47913 | Block-identity inputs (a)–(d) | hypothesis | The proof imports the Q and J sheets with enlarged reading lists, real spectral bounds, a complex sector bound, and clause D. | assumed | Operator theorem hypotheses; 4.14:prf-form-walk-expansion; 4.14:prf-positivity-inversion | "established in the preceding parts" |
| 47922-48139 | Proof of 4.14:prf-block-identities | proof | Block algebra and the named sheet, core, local-ball, symmetry, and dependence results establish the remaining claims. | proved conditionally | Inputs (a)–(d); core lemma; local-balls; reading-hulls; symmetry-covariance; dependence lemma; Schur-complement corollary | "clauses and statements were proved above." |
| 47923-47929 | Clause A: analytic symmetric blocks and inverse | proof | Analyticity and symmetry descend to the blocks and the inverse C on U(ε₁). | proved conditionally | Input (a); symmetry lemma for Q; input (d) at x=0 | "by definition" |
| 47931-47936 | Graph identification with Bałaban's form | identity | On the current graph Q is Bałaban's C*Δ⁽ᵏ⁾C in the specified frame. | cited | Graph identity for Q; B-CMP99b (3.117′), (3.126), (3.129); B-CMP109; B-CMP116 | "That" |
| 47937-47947 | 4.14:eq-block-identities-1 | identity | The quadratic form splits into its diagonal blocks and one source cross term on the full complex ball. | proved conditionally | Symmetry of Q; A_k=φ⊕A′; bilinear pairing | "the two cross terms are equal" |
| 47948-47959 | 4.14:eq-block-identities-2 | identity | Completing the square separates the shifted A-form from the Schur-complement form. | proved conditionally | AC=1; symmetry of A and C; block-identities-1 | "Expand the square below" |
| 47955-47959 | Schur complement K | definition | K is the remaining diagonal block minus JᵀCJ. | definition | Q; J; C | "with" |
| 47960-47967 | Conditional-integral identification | remark | The identities hold on all U(ε₁), while the identification with Bałaban's conditional integral is made on the current graph. | proved conditionally | Graph identity; block-identities-1 and -2; B-CMP119 (3.23), (3.25) | "the statement is the linear algebra" |
| 47969-47984 | Clause B | proof | Min–max gives C's base-point spectral interval and its enlarged real-point bound within U(ε₁). | proved conditionally | Inputs (a)–(c); symmetry lemma; min–max | "By the min--max characterisation" |
| 47986-47991 | Clause C | proof | J is real at real points, its transpose is the reverse block, and its norm is bounded by γ₁ on U(1). | proved conditionally | Q symmetry; input (a); coordinate projections | "coordinate projections of norm at most one" |
| 47993-48001 | Core lemma and aligned-collar requirement | requirement | Core regrouping supplies W1, W2, W3′, W5 covariance, and W6 geometry when the nearby collar cubes share an aligned partition. | assumed | Core lemma; A2 of prepared-data-admissible-a; ρ≤M/4 | "That lemma" |
| 48003-48010 | Clauses E and F | proof | The core lemma gives the stated C and J core expansions. | proved conditionally | D at x=0; input (a); core lemma; M≥144dρ_Q | "The core lemma applies" |
| 48012-48017 | Clause G; 4.14:eq-block-identities-3 | identity | Each n-step resolvent walk carries (1+2x/m₁)⁻⁽ⁿ⁺¹⁾ and complex x is handled through its real part. | proved conditionally | D; remark accompanying inversion lemma for sheets | "complex" |
| 48019-48040 | Reading hulls, W6 geometry, W5 covariance | proof | Enlarged lists preserve diameter and distance requirements and transfer geometric reading and covariance termwise. | proved conditionally | Sh5; Sh4; core lemma; reading-hulls(ii)–(v); free-current-notation-a | "applied termwise" |
| 48042-48052 | Clause H: local balls | proof | The local-balls lemma yields the core-form statements with data on the larger prescribed domains. | proved conditionally | 4.14:lem-local-balls(α); A1; M>2L; free-current-notation-d; radii ε₁ and 1 | "holds a fortiori" |
| 48054-48062 | Clause I: initial constant-dependence classification | proof | Constants depend only on d, L and the displayed auxiliary sizes and avoid the listed geometry and coupling variables. | proved conditionally | Form-walk and positivity-inversion lemmas; block-size definition; free-current-notation-a; block-size-conditions-d | "None depends on" |
| 48064-48083 | 4.14:eq-block-identities-4; order of choices | construction | Constants, block sizes, couplings, radii, and g are selected in an order with no backward dependence. | proved conditionally | Block-size-conditions-a and -d; block-size definition; application radius condition | "is used before it has been fixed." |
| 48080-48082 | Application radius condition | requirement | Radii are chosen by the condition imposed at the theorem's application. | assumed | Condition on radii where the theorem is used | "The radii are fixed by the condition" |
| 48085-48091 | Clause I: dependence only on d and L | proof | Fixing M₁ and M₁♯ from d and L makes all listed operator constants depend only on d and L. | proved conditionally | Choice order; auxiliary floors in block-size-conditions-a | "fixed once and for all" |
| 48093-48101 | Clause K | proof | The K1 split has a nonzero pivot cross block and a zero G cross block, with constants fixed before Λ_t choices. | proved conditionally | Pivot-row structure; unit-lattice G identity; I | "by the unit-lattice" |
| 48103-48107 | Covariance statement | proof | Lattice-symmetry covariance follows from symmetric weights, the symmetrizing letter, and parity assignments. | proved conditionally | symmetry-covariance(a)–(d); free-current-notation-b and -c | "This is part (d)" |
| 48109-48113 | Dependence statement | proof | A Λ_t-dependent Cᴷ¹ word contains a complement point and its ℓ/3 collar in its domain. | proved conditionally | Dependence lemma for Cᴷ¹ words; weights leave index 1″ unchanged | "It follows from the dependence lemma" |
| 48115-48130 | Schur-complement statement | proof | Sheet rules give K a sheet expansion and minimization gives γ₀/2≤K≤γ₁ at real base points. | proved conditionally | Schur-complement corollary; sheet sum/product rules; (a), D; B, E, F; block-identities-2 | "Taking the minimiser" |
| 48120-48125 | Real minimizing shift | construction | At a real base point the minimizing field is φ=−CJA′ and its minimum is the K quadratic form. | proved conditionally | A>0 from B; block-identities-2 | "minimised over real" |
| 48132-48138 | Conditional operator-theorem conclusion | theorem | All clauses and supplementary statements follow from prepared-data admissibility at every history nest and the one-sided block conditions. | proved conditionally | prepared-data-admissible-a at every nest; block-size definition; preceding lemmas and proof | "Assume the admissibility" |
| 48141-48206 | 4.14:not-operation-conventions — Conventions at a large-field operation | definition | The convention fixes operation units, partitions, enlargements, component facts, scales, and level symbols. | definition | Small-coupling regime; operation-components definition | "The following conventions are in force." |
| 48142-48147 | Operation setting | hypothesis | The operation acts at a level in Bałaban's small-coupling regime on the specified component class. | assumed | 4.14:def-small-coupling-regime; small-coupling-regime-a; 4.14:def-operation-components; operation-components-a | "Fix a level" |
| 48149-48151 | Units and ℓ_j | definition | Level-k units give spacing ℓ_j=L^(j−k). | definition | Operation level k | "Lengths are measured in the units" |
| 48152-48155 | Compatible partitions | hypothesis | All M-cube and MR_j-cube partitions form one compatible L-adic family. | cited | B-CMP119 p. 256 | "one compatible" |
| 48156-48163 | Metric and layer enlargements | definition | X^(+r) is the closed sup-distance enlargement and X^(∼n) is enlargement by n cube sides. | definition | Partition of side s; union of closed cubes | "For" |
| 48164-48168 | Domain enlargement interpretation | remark | The metric enlargement agrees with the printed layer enlargement on portions whose traces enter the analysis. | assumed | B-CMP122a (1.10)–(1.11); alignment statement for the two enlargements | "this coincidence is the content of the alignment" |
| 48169-48172 | Three component facts | hypothesis | The sequel uses component separation, segment exit, and the location of the exit point for grid-cube unions. | assumed | Unions of closed partition cubes | "are used in the sequel" |
| 48173-48188 | f(n), N₀, k₀, star, σ_i; 4.14:eq-operation-conventions-a | definition | The first scale with f(n)=1 defines N₀ and the transition level, with σ_i the physical block side. | definition | small-coupling-regime-a; B-CMP122a (1.64)–(1.67), pp. 179, 192 | "let" |
| 48189-48202 | Scale conclusions (a)–(f) | lemma | The scales are monotone powers of L with a transition at star, N₀≥2, compatible partitions, and h<star−1. | proved conditionally | Small-coupling regime; R_i powers of L; compatible partitions; N_k>N₀ | "Then the following hold." |
| 48203-48205 | k′ and k₀ symbols | definition | k′ denotes another operation's level while k₀ retains Bałaban's transition-index meaning. | definition | Operation history | "The symbol" |
| 48208-48261 | Proof of operation conventions | proof | Grid geometry and the printed coupling relations establish enlargement closure and all six scale claims. | proved conditionally | small-coupling-regime-a; B-CMP119 (2.9); N₀ definition; N_k>N₀ | "by the gap-one bound" |
| 48209-48214 | Enlargement closure proof | proof | Integer multiples of the cube side preserve unions of closed cubes because enlarged endpoints remain on the grid. | proved in detail | Metric enlargement definition; partition coordinates | "again lie in the grid" |
| 48216-48219 | Gap-one bound | estimate | Power-of-L discreteness improves R_m≤(L+1)R_(m+1) to R_(m+1)≥R_m/L. | proved conditionally | B-CMP119 (2.9); small-coupling-regime-a; powers of L | "forces" |
| 48221-48229 | Proof of scale item (a) | proof | The gap-one bound makes f nonincreasing and operation nontriviality gives f(1)≥L. | proved conditionally | Gap-one bound; ℓ_j; small-coupling-regime-a | "by the gap-one bound" |
| 48231-48235 | Proof of scale item (b) | proof | The regime's scale equality supplies N₀ and gives σ_star=M and R_star=L^(N₀−1). | proved conditionally | small-coupling-regime-a; N₀ and star definitions | "Hence the" |
| 48237-48243 | Proof of scale item (c) | proof | Monotonicity and minimality of N₀ separate the ≤M and ≥LM ranges. | proved conditionally | Item (a); definition of N₀ | "minimality" |
| 48245-48248 | Proof of scale item (d) | proof | f(1)>1 forces N₀≥2 and hence the stated bounds on star and its spacing. | proved conditionally | Item (a); N₀ and star definitions | "Therefore" |
| 48250-48254 | Proof of scale item (e) | proof | Adjacent scale ratios imply monotonicity of σ and power-of-L compatibility at any later level. | proved conditionally | Gap-one bound; partition convention | "so" |
| 48256-48260 | Proof of scale item (f) | proof | N_k>N₀ puts the lowest touched level strictly below star−1. | proved conditionally | small-coupling-regime-a; h=k−N_k | "Therefore" |
| 48263-48270 | 4.14:lem-small-boxes — Small boxes in unions of grid cubes | lemma | A positive-sided closed box of side lengths at most S inside a grid-cube union fits inside an S-cube still in that union. | proved in detail | Aligned grid-cube union; H⊂Ω; side bounds | "proves the lemma." |
| 48264-48268 | Grid cube | definition | Grid cubes are products of adjacent length-S intervals based at the fixed offset o. | definition | S>0; o∈Rᵈ | "call a" |
| 48272-48327 | Proof of small-boxes lemma | proof | Sliding intervals and covering by grid cubes with interior points in H prove the containing-cube assertion. | proved in detail | Grid definitions; H positive side lengths; H⊂Ω | "proves the lemma." |
| 48273-48276 | Grid point and grid interval | definition | Coordinate grid points lie at offset multiples of S and grid intervals join consecutive such points. | definition | Offset o; S | "it has length" |
| 48278-48291 | Straddling and construction of Q | construction | Each coordinate is extended to an S-interval, sliding off the grid when it straddles a grid point. | proved in detail | Side lengths ≤S; at most one interior grid point | "Set" |
| 48293-48304 | Grid cover C_ε | construction | Choosing the two neighboring intervals in each straddling coordinate covers Q by grid cubes. | proved in detail | J_i; K_i; straddling-index set σ | "Each" |
| 48306-48326 | Cover cubes lie in Ω | proof | An interior point of each cover cube belongs to H and forces that entire grid cube to be part of Ω. | proved in detail | H⊂Ω; uniqueness of grid-cube interiors; positive side lengths | "Consequently" |
| 48329-48335 | Off-grid admissibility | remark | The containing cube need not be a partition cube and the cited gauge families allow this. | cited | B-CMP119 (2.38); B-CMP122a (1.65), (1.67), (1.69); B-CMP109 (1.12) | "do not refer to any" |
| 48337-48370 | 4.14:lem-hull-cube — The hull of a second-cover box in one cube | lemma | Each second-cover hull at index at least two fits in a single appropriately scaled cube crossing the next domain boundary and avoiding the domain two levels higher. | proved conditionally | A1; M≥13L²M₁♯; second cover; small-boxes lemma | "which is" |
| 48338-48349 | Hull-cube hypotheses and territories | hypothesis | The nest satisfies A1, the block floor holds, terminal domains are empty, and the second-cover box has its specified center and size. | assumed | prepared-data-admissible-a; block-size-conditions-a; free-current-notation; B-CMP122a | "satisfying condition (A1)" |
| 48349-48353 | Hull square⁴ and m(square) | definition | The hull has half-side 5s_j and m is the highest nest level containing it. | definition | Second-cover box; nest | "define" |
| 48356-48361 | Hull location and size, (1)–(3) | estimate | m is j−1 or j, the hull meets only the specified adjacent territories, and its side is at most Mℓ_m. | proved conditionally | A1; block floor; m definition | "Then the following hold." |
| 48362-48368 | Q(square); 4.14:eq-hull-cube-a | construction | A cube of side Mℓ_m contains the hull inside Ω_m outside Ω_(m+2) and meets the complement of Ω_(m+1). | proved conditionally | Hull-cube (1)–(3); small-boxes lemma; A1 | "There is a closed cube" |
| 48372-48468 | Proof of hull-cube lemma | proof | Nest separation bounds m, controls territory intersections, and lets the small-boxes lemma supply the desired cube. | proved conditionally | A1 as (a)–(c); block floor; small-boxes lemma | "therefore yields a closed cube" |
| 48373-48383 | A1 in the form used | hypothesis | A1 supplies nesting, aligned closed M-cube unions, and one-layer metric separation. | assumed | A1 of prepared-data-admissible-a; terminal empty domains | "We use condition (A1) in the following form" |
| 48385-48405 | Proof of hull-cube (1) | proof | Separation puts the hull in level j−1 while its center's territory prevents containment in level j+1. | proved conditionally | A1; M≥13L²M₁♯; center in X_j | "and" |
| 48407-48437 | Proof of hull-cube (2) | proof | A point outside Ω_(m+1) and layer separation exclude Ω_(m+2) and all nonadjacent territories. | proved conditionally | Maximal m; A1; block floor | "The only territories that remain" |
| 48439-48442 | Proof of hull-cube (3) | proof | The block floor and m≥j−1 imply the hull-side bound. | proved conditionally | Proof of (1); m≥j−1 | "By" |
| 48444-48459 | Proof of hull-cube (4) | proof | The small-boxes cube contains an outside point and separation keeps it disjoint from Ω_(m+2). | proved conditionally | A1; (2), (3); small-boxes lemma; L>1 | "therefore yields a closed cube" |
| 48461-48467 | Low-index hull backgrounds | remark | Hulls at indices zero and one use the nest-independent alternative α′ and are unaffected by the large-field operation. | cited | real-backgrounds-a(α′); B-CMP99b (3.35) at M₁♯ and indices 0,1,2; h≥1 | "That condition does not depend on the nest" |
| 48470 | Units in the two papers | definition | The lengths written L^iξ and L^iη in the cited papers are both interpreted as ℓ_i. | definition | operation-conventions; B-CMP119; B-CMP122a | "are both equal to" |
| 48472-48476 | Printed gauge-family requirement | requirement | Each family cube must admit a Lie-algebra gauge potential satisfying the two scaled bounds on the configuration's domain intersection. | assumed | B-CMP119 (2.38); B-CMP122a (1.65), (1.67), (1.69); cube size CMℓ_i or CM | "there must exist a gauge transformation" |
| 48477 | Scale, printed bound, α-index, L₀-exponent, e(Q) | definition | These names record the spacing, numerical gauge bound, radius index, and auxiliary-integer exponent attached to a cube. | definition | B-CMP119 (2.28); B-CMP122a (1.24); printed gauge inequalities | "We call" |
| 48479-48575 | 4.14:lem-gauge-family — The printed gauge family of the hull's cube | lemma | The hull cube belongs to the printed old-nest or stage family with scale ℓ_m, α-index m, and controlled exponent. | proved conditionally | Hull-cube lemma; stage admissibility; exits and stage nests; printed families | "Then exactly one of the following holds." |
| 48481-48496 | Gauge-family part (a) | lemma | For any admissible nest Q belongs to B-CMP119's family and hence to the one-sided B-CMP122a families with C=1. | proved conditionally | hull-cube-a; B-CMP119 (2.38); B-CMP122a (1.65), (1.69) | "A fortiori" |
| 48497-48505 | Old nest, Z″, new domains, k₀ and h | definition | The operation is supplied with its pre-operation nest, modified domains, transition index, and lowest touched level. | definition | operation-components; operation-conventions-a; B-CMP122a (1.10)–(1.12) | "Attached to it are:" |
| 48506-48518 | Exit stage p and stage nest N⁽ⁿ⁾ | definition | For a component leaving after n integrations the stage nest uses new domains through p=h+n and old domains above p. | definition | Exit-stage convention; B-CMP122a p. 191, (1.12), (1.64)–(1.69) | "stage nest" |
| 48518-48523 | Persistence and stage-nest admissibility | hypothesis | The exiting component keeps its stage nest until a containing fill and that nest satisfies A1 for every state assignment. | assumed | Exits and stage-nests lemma; operation-components rule; lemma asserting stage nests admissible | "By the lemma" |
| 48527-48533 | (G1) | construction | If m<p, Q uses the new-domain family (1.65) at index m with exponent max(0,m−k₀). | proved conditionally | Stage nest; hull-cube-a; B-CMP122a (1.65)(i) | "so" |
| 48534-48546 | (G2) | construction | If m=p and Q meets the old star-domain complement, Q uses family (1.65), and this case is forced when p≤k₀. | proved conditionally | Stage nest; hull-cube-a; old-nest nesting; B-CMP122a (1.65)(i) | "This case" |
| 48547-48561 | (G3); old-nest index bar m | construction | If m=p and Q lies in the old star-domain, its last old containment level places it in family (1.67) with exponent p−bar m. | proved conditionally | Stage nest; hull-cube-a; old-nest nesting; B-CMP122a (1.67)(ii) | "Hence" |
| 48562-48565 | (G4) | construction | If m>p, Q uses the unchanged old-domain family (1.69) with exponent zero. | proved conditionally | Stage nest; hull-cube-a; B-CMP122a (1.69)(iii) | "Hence" |
| 48568-48574 | 4.14:eq-gauge-family-a | estimate | The exponent lies between zero and max(0,m−k₀), with the listed casewise values and a positive exponent only above k₀. | proved conditionally | Part (a); G1–G4 | "More precisely" |
| 48577-48682 | Proof of printed gauge-family lemma | proof | Membership tests against the printed families and an exhaustive case split give every bound and exponent. | proved conditionally | hull-cube-a; stage-nest definition; B-CMP119 (2.38); B-CMP122a (1.65), (1.67), (1.69) | "exhaustive" |
| 48578-48598 | Proof of part (a) | proof | The hull-cube conditions are exactly the old family conditions and imply the weaker one-sided conditions. | proved conditionally | hull-cube-a; printed families | "dropping a condition only enlarges a family" |
| 48600-48605 | Exhaustiveness proof | proof | Comparing m and p and then testing containment in the old star-domain gives four exclusive cases. | proved in detail | m≤k; cases G1–G4 | "and mutually exclusive." |
| 48607-48618 | Proof of G1 | proof | Substituting the new domains through p gives the family-(i) conditions and its printed bound. | proved conditionally | Stage nest; B-CMP122a (1.12), (1.65); hull-cube-a | "These are the conditions" |
| 48620-48635 | Proof of G2 | proof | The case hypothesis supplies the top family-(i) condition and nesting forces it for p≤k₀. | proved conditionally | hull-cube-a; stage nest; old nesting; B-CMP122a (1.65), p. 191 | "Thus (G2) applies" |
| 48637-48658 | Proof of G3 | proof | Maximal old containment produces the family-(ii) index and the exponent bound p−bar m≤m−k₀−1. | proved conditionally | G2 exclusion; bar m definition; hull-cube-a; B-CMP122a (1.67); terminal empty domains | "These are the" |
| 48660-48669 | Proof of G4 | proof | Above p the old domains supply family-(iii) membership with no auxiliary power. | proved conditionally | Stage nest; hull-cube-a; B-CMP122a (1.69) | "these are the conditions" |
| 48671-48681 | Exponent proof | proof | Reading off the four cases proves the common exponent bound and its positive-exponent range. | proved conditionally | Part (a); G1–G4 | "read off the" |
| 48684-48772 | 4.14:rem-tiling-later-steps — Tiling, later steps and earlier drop-outs | remark | The gauge-family classification is extended to tiling, persistent stage nests, earlier drop-outs, and componentwise states. | proved conditionally | Gauge-family lemma; new-family statement; persistence statement; admissibility proposition; printed generalized space | "Under either reading" |
| 48685-48699 | Remark setting and territory notation | definition | The remark fixes an exiting component, its stage nest and territories, and the hull cube and metric enlargement notation. | definition | gauge-family(b); operation-components-a; operation-conventions-a; hull-cube-a | "We write" |
| 48701-48722 | Tiling on Z; 4.14:eq-tiling-later-steps-1 | estimate | On Z the old layers from star through p lie inside the stage-p territory at scale ℓ_p, while no such off-Z tiling is asserted. | proved conditionally | New-family inclusion Z″_p⊂Z″_k; stage nest; star=k₀+1; G2 and G3 | "It therefore suffices" |
| 48718-48719 | Regularity scale of the tiled territory | remark | The regularity condition with bound a♯ weights the stage-p territory at precisely ℓ_p. | assumed | Regularity condition bounded by a♯; stage-p territory | "exactly the scale" |
| 48723-48729 | Later-step carried nest | remark | The nest carried by an exited term agrees with its exit-stage nest on X through level k until a containing fill. | proved conditionally | Persistence clauses (a), (b); B-CMP122a unchanged-domains statement; gauge-family(a) after fills | "until a fill" |
| 48731-48743 | Generalized later-step space and two readings | hypothesis | The later-step space imposes nearby conditions that may be read as current-nest families or retained stage families. | cited | B-CMP122a generalized-space sentence; (1.64)–(1.69); B-CMP119 (2.38) | "printed without proof there; cited as printed." |
| 48744-48750 | Membership and exponent under both readings | estimate | Q belongs to either corresponding family and its exponent is at most max(0,m−k₀), with family selection deferred to another lemma. | proved conditionally | gauge-family(a), (b); hull-cube-a; persistence; lemma on families of the later-step space | "Under either reading" |
| 48751-48757 | Earlier drop-outs and second-class components | remark | Earlier exits retain their own stage nests and second-class survivors use the final-stage nest with p=k and no G4 case. | proved conditionally | Persistence; gauge-family(b); Ω_(k+1)=empty | "part (b) holds" |
| 48758-48770 | Global componentwise nest | construction | Each component uses new domains only through its own last stage, producing an A1 nest whose hull analysis reads at most one state. | proved conditionally | State-assignment admissibility proposition; component separation; gauge-family(a), (b) | "defined componentwise" |
| 48774-48865 | Proof of tiling/later-step remark | proof | New-family inclusion, persistence, family memberships, and component separation establish the four assertions. | proved conditionally | New-family statement; persistence clauses (a), (b); admissibility proposition; gauge-family lemma; R_k≥3 | "This is the final assertion." |
| 48775-48801 | Proof of part (1), tiling | proof | Taking complements of Z″_p⊂Z″_k places the old star-domain inside Ω″_p on Z and yields the displayed inclusions. | proved conditionally | New-family statement; star=k₀+1; stage nest; operation unchanged off Z | "This is the second inclusion." |
| 48803-48829 | Proof of part (2), later steps | proof | Persistence gives nest agreement and the two family interpretations give the common exponent ceiling. | proved conditionally | B-CMP122a unchanged-domains statement and p. 192; persistence (a), (b); gauge-family(a), (b); hull-cube-a | "Each of these" |
| 48831-48839 | Proof of part (3), earlier drop-outs | proof | Substituting each exit stage preserves the same k₀ and at p=k eliminates G4. | proved conditionally | Persistence; gauge-family(b); m≤k; terminal empty domain | "by the" |
| 48841-48864 | Proof of part (4), componentwise nest | proof | State-assignment admissibility supplies A1 and the cube's diameter and component spacing prevent reading two states. | proved conditionally | Proposition establishing A1 and A2; component separation MR_k≥3M; ℓ_m≤1; gauge-family(a) | "only the state" |
| 48849-48860 | Single-component distance estimate | estimate | A hull cube meeting one component stays at least 2M from every other component. | proved conditionally | Cube side Mℓ_m≤M; distinct Z_k components separated by MR_k; R_k≥3 | "at distance at least" |
| 48867-48896 | 4.14:lem-integer-power-bound — The auxiliary integer's power against the block count | lemma | Auxiliary powers up to exponent m−k₀ are bounded by a fixed multiple of R_m. | proved conditionally | small-coupling-regime-a; B-CMP119 (2.9); N₀ definition; L₀≥1; L₀²≤L/3 | "Then" |
| 48868-48878 | Integer-power hypotheses | hypothesis | The regime supplies power-of-L block counts, two interlevel inequalities, N₀, and the auxiliary-integer bounds. | assumed | B-CMP119 (2.9); B-CMP122a p. 192; operation-conventions-a | "Thus every block count" |
| 48879-48885 | 4.14:eq-integer-power-bound-a | estimate | L₀^(2e)≤L₀^(2(m−k₀))≤c(β₀)L(L+1)R_m for the specified levels and exponents. | proved conditionally | Integer-power hypotheses; c(β₀) definition | "This is the first inequality" |
| 48883 | c(β₀) | definition | c(β₀) is the supremum of 3^(−v)v^β₀ over v≥1. | definition | β₀>0 | "sup" |
| 48886-48889 | 4.14:eq-integer-power-bound-1 | estimate | At m=k the top auxiliary power is bounded by 3^(−N₀)N₀^β₀L(L+1)R_k and then by c(β₀)L(L+1)R_k. | proved conditionally | integer-power-bound-a and its proof; m=k; e=N₀ | "In particular" |
| 48890-48895 | Bałaban's comparison chain | estimate | The text records Bałaban's related chain with an N₀-dependent polynomial and an N₀⁻¹ endpoint. | cited | B-CMP122a p. 192 | "displayed in" |
| 48898-48951 | Proof of auxiliary-power lemma | proof | Exponential damping, the defining scale equality, and the nonconsecutive block-count inequality give the claimed uniform constant. | proved conditionally | L₀≥1; L₀²≤L/3; R_star=L^(N₀−1); B-CMP119 (2.9); β₀>0 | "which gives both inequalities" |
| 48902-48913 | Reduction through R_star | estimate | Setting a=m−k₀ bounds L₀^(2a) by 3^(−a)L L^(m−star) and then uses L^(m−star)≤R_star. | proved conditionally | Auxiliary ceiling; m≤k; R_star equality | "Hence" |
| 48914-48931 | 4.14:eq-integer-power-bound-2 | estimate | Both the equal-level and separated-level cases give L^(m−star)≤(L+1)a^β₀R_m. | proved conditionally | B-CMP119 (2.9); R_star equality; a=m−star+1; β₀>0 | "In both cases" |
| 48932-48942 | Completion of integer-power estimates | proof | Substitution into the damped power bound proves the general estimate and its top-level specialization. | proved conditionally | integer-power-bound-2; definition of c; m=k specialization | "gives both inequalities" |
| 48944-48950 | Finiteness and optional bound for c(β₀) | proof | Decay makes c finite, and for β₀≤1 its value is at most one third, an optional regime allowed by the cited coupling choice. | proved in detail | Continuous function 3^(−v)v^β₀; β₀>0; optional B-CMP119 remark after (2.6) | "so its supremum is finite." |
| 48953-48969 | Remarks (1): exact inputs and insufficient gap-one bound | remark | Only three printed inputs are used, whereas iterating the adjacent-level bound yields merely R_k≥1 and no flow or elapsed-time information enters. | proved conditionally | B-CMP119 (2.9); N₀ equality; L₀²≤L/3; gap-one bound | "would not" |
| 48971-48983 | Remarks (2): weaker auxiliary ceiling | remark | Replacing L₀²≤L/3 with L₀<L/2 gives a squared type of block-count bound and the stronger printed condition is retained. | proved conditionally | Hypothetical weaker B-CMP122a ceiling; integer-power-bound-2; small-coupling-regime-a block-count bound | "would give" |
| 48985-48990 | Remarks (3): alternative route | proof | A top-level estimate followed by R_k≤LR_n gives a lower-level bound with an extra L factor. | sketched | B-CMP122a p. 192; first inequality of B-CMP119 (2.9); integer-power-bound-a | "There is an alternative route." |
| 48993-49019 | 4.14:lem-top-power-bound — The top power against every lower level | lemma | The fixed operation's top auxiliary power is bounded by c₁R_n at every n≤k, yielding the per-operation-to-boxwise comparison. | sketched | integer-power-bound hypotheses; small-coupling-regime-a; operation-conventions-a; c₁ definition; proof truncated at 49044 | "We distinguish three ranges" |
| 48994-48998 | Top-power hypotheses | hypothesis | The top-power lemma inherits the auxiliary-power regime and the defining star-level equality. | assumed | 4.14:lem-integer-power-bound; 4.14:def-small-coupling-regime; operation-conventions | "Let the hypotheses" |
| 48999-49005 | c(β₀) and c₁ | definition | c₁ is 1+c(β₀)L(L+1), matching the block-size definition's constant. | definition | integer-power-bound-a; 4.14:def-block-size-conditions | "Put" |
| 49006-49008 | 4.14:eq-top-power-bound-a | estimate | L₀^(2N₀)≤c₁R_n for every history level n≤k. | sketched | Top-power hypotheses; c₁; proof continues beyond chunk | "We distinguish three ranges" |
| 49009-49012 | 4.14:eq-top-power-bound-1 | estimate | Multiplying the top-power estimate bounds L₀^(2N₀)L²BMα_(0,n) by L²c₁BMR_nα_(0,n). | proved conditionally | top-power-bound-a (only partly proved in this chunk); nonnegative bound factors | "Consequently" |
| 49013-49018 | Layerwise meaning of a♯_F | remark | For this fixed operation each layer's member of a♯_F is no larger than its boxwise regularity value. | proved conditionally | top-power-bound-1; per-operation constant a♯_F; operator-format B | "This holds for the fixed operation" |
| 49021-49044 | Proof of top-power lemma, opening only | proof | The proof reduces the power to R_star, recalls two count inequalities, and begins the range n>star. | sketched | small-coupling-regime-a; operation-conventions-a; B-CMP119 (2.9); c definition | "We distinguish three ranges" |
| 49025-49028 | 4.14:eq-top-power-bound-2 | estimate | The auxiliary ceiling and star equality give L₀^(2N₀)≤3^(−N₀)L R_star. | proved conditionally | L₀²≤L/3; R_star=L^(N₀−1) | "Raising the second inequality" |
| 49029-49035 | 4.14:eq-top-power-bound-3 | hypothesis | For j>i the printed relations bound R_j by LR_i and R_i by (L+1)(j−i)^β₀R_j. | cited | B-CMP119 (2.9), p. 256; small-coupling-regime-a | "it states" |
| 49036-49038 | Two supremum facts | estimate | Each integer value 3^(−t)t^β₀ is bounded by c and the value at t=1 gives c≥1/3. | proved in detail | Definition of c(β₀) | "by the definition of the supremum." |
| 49040-49044 | Range star<n≤k, initial comparison | estimate | The second interlevel inequality gives R_star≤(L+1)(n−star)^β₀R_n in the first range. | proved conditionally | top-power-bound-3; n>star | "This is admissible" |

## Forward and backward references

Occurrences are listed in source order, including repeated applications; references within this chunk are retained so the dependency direction is visible.

- 47746–47748: 4.14:eq-prepared-data-admissible-a is a hypothesis of 4.14:thm-operator-theorem and a statement of 4.14:prop-prepared-data-admissible; B-CMP122a pp. 178–179 states the proposition without proof.
- 47755–47764: 4.14:def-real-backgrounds supplies U_R; the positivity lemma for sheets is applied; its floor is 4.14:eq-block-size-conditions-a(v); B-CMP99b's localization sentence is the positivity claim being explicated.
- 47771–47787: Earlier box properties (b1)–(b3), the sheet bound, and the positivity floor supply the error estimates.
- 47789–47798: 4.14:def-real-backgrounds supplies the regular gauge; 4.14:prf-form-walk-expansion fixes a₁⊕ and the ball U(1).
- 47800–47812: Sheet properties Sh4 and Sh2 supply covariance and local reading.
- 47814–47833: 4.14:eq-block-size-conditions-b supplies the regularity ceiling; Schur and Schwarz bounds are invoked.
- 47841–47848: 4.14:eq-positivity-inversion-2 transfers the local lower bound; 4.14:eq-positivity-inversion-1 sums it.
- 47850–47861: Sector lemma, Step 1, and the sheet/unit-frame distance properties give the complex sector bound.
- 47869–47883: Inversion lemma for sheets, box properties (b1)–(b4), A2, and 4.14:eq-block-size-conditions-a(iii),(iv) give clause (c).
- 47885–47892: The inversion lemma allows arbitrary index sets; 4.14:thm-operator-theorem's enlarged lists and 4.14:lem-reading-hulls are explicitly said not to enter this proof.
- 47896–47919: 4.14:thm-operator-theorem supplies the hypotheses and target clauses; 4.14:prf-form-walk-expansion and 4.14:prf-positivity-inversion are said to establish inputs (a)–(d), including theorem clause D.
- 47923–47929: Symmetry lemma for Q and input (d) at x=0 give analytic symmetric inversion.
- 47931–47936: Graph identity for Q uses B-CMP99b (3.117′), (3.126), (3.129) only on the graph, the substituted-current definition in B-CMP109, and the frame of B-CMP116.
- 47960–47967: 4.14:eq-block-identities-1 and -2 identify covariance and source; B-CMP119 (3.23), (3.25) are the B-star specialization.
- 47969–47984: Input (b), the symmetry lemma, and inputs (a),(c) give the spectral bounds.
- 47986–47991: Input (a) gives the source norm; 4.14:eq-free-current-notation-a through -d are explicitly unnecessary for A–C.
- 47993–48001: The core lemma supplies W1, W2, W3′, W5 covariance, and W6 geometry of operator-theorem clause E; A2 of 4.14:eq-prepared-data-admissible-a supplies its aligned-collar requirement.
- 48003–48010: Clause D at x=0 gives the C sheet; input (a), the core lemma, and 4.14:eq-block-size-conditions-a give the J sheet's core form.
- 48012–48017: Clause D and the remark accompanying the inversion lemma handle resolvents and complex x.
- 48019–48040: 4.14:eq-free-current-notation-a enters only through W6 geometry; core lemma and inversion-word Sh5 use 4.14:lem-reading-hulls(iii),(iv); parts (ii),(v) preserve domain diameters; notation-b and -c do not enter, and Sh4 supplies W5 covariance.
- 48042–48052: 4.14:lem-local-balls and its part (α), A1 of prepared-data-admissible-a, the M>2L floor in block-size-conditions-a, and free-current-notation-d establish H.
- 48054–48066: Constants come from form-walk-expansion, positivity-inversion, free-current-notation-a, 4.14:def-block-size-conditions, and block-size-conditions-d.
- 48078–48091: Block-size-conditions-a fixes the auxiliary sizes and M; block-size definition fixes couplings; an application-specific condition fixes radii; block-identities-4 records the order.
- 48095–48101: The unit-lattice identity for G and clause I supply the K1 cross-block and noncircularity assertions.
- 48103–48107: 4.14:lem-symmetry-covariance(d), supported by (a)–(c), and free-current-notation-b,-c supply covariance.
- 48109–48113: The dependence lemma for Cᴷ¹ words supplies the complement-point-and-collar statement.
- 48115–48130: Schur-complement corollary, sheet sum/product rules, clauses D,E,F, block-identities-2, and B supply K and its bounds.
- 48132–48138: Prepared-data-admissible-a at every history nest and the block-size definition are the final assumptions; form-walk-expansion and positivity-inversion supply D and inputs (a)–(c).
- 48142–48147: 4.14:def-small-coupling-regime / small-coupling-regime-a and 4.14:def-operation-components / operation-components-a define the operation setting.
- 48152–48155: B-CMP119 p. 256 is the compatible-partition source.
- 48164–48168: B-CMP122a (1.10)–(1.11) are read metrically; the statement on alignment of the two enlargements establishes agreement.
- 48173–48188: Operation-conventions-a below records σ_i and star; small-coupling-regime-a guarantees N₀ exists; B-CMP122a (1.64)–(1.67) and p. 192 use k₀, and p. 179 uses N₀; items (b),(d) below prove the displayed relations.
- 48200–48201: The small-coupling-regime definition supplies N_k.
- 48216–48219: B-CMP119 (2.9), as recorded in small-coupling-regime-a, supplies the gap-one inequality.
- 48221–48229: Gap-one bound and small-coupling-regime-a establish monotonic f and R_k≥L.
- 48231–48235: Small-coupling-regime-a supplies the exact f(n)=1 input used to define N₀.
- 48237–48254: Scale proofs (c)–(e) use (a), N₀ minimality, and the gap-one bound.
- 48256–48260: Small-coupling-regime-a supplies N_k>N₀.
- 48329–48335: B-CMP119 (2.38), B-CMP122a (1.65),(1.67),(1.69), and B-CMP109 (1.12) allow cubes not tied to a partition.
- 48338–48349: A1 of prepared-data-admissible-a, the first M floor in block-size-conditions-a, B-CMP122a's empty-terminal-domain convention, and 4.14:not-free-current-notation define the hull setting.
- 48373–48383: A1 is unpacked into nesting, alignment, and separation, with level spacing recalled.
- 48444–48459: 4.14:lem-small-boxes constructs Q; the argument proves 4.14:eq-hull-cube-a.
- 48461–48467: real-backgrounds-a(α′) invokes B-CMP99b (3.35) at M₁♯ for indices 0,1,2.
- 48470: 4.14:not-operation-conventions identifies B-CMP119 and B-CMP122a length conventions.
- 48472–48477: B-CMP119 (2.38) and B-CMP122a (1.65),(1.67),(1.69) are the gauge families; B-CMP122a p. 191 specifies integer C; B-CMP119 (2.28) defines α_(0,i), and B-CMP122a (1.24) defines the auxiliary integer.
- 48481–48496: 4.14:lem-hull-cube supplies Q's membership in B-CMP119 (2.38) and the one-sided B-CMP122a (1.65),(1.69).
- 48497–48505: Operation-components, B-CMP122a (1.10)–(1.12), operation-conventions, and operation-conventions-a supply the operation data.
- 48506–48523: B-CMP122a p. 191 defines completion of preliminary integrations; the exits-and-stage-nests lemma supplies the exit possibilities and persistence; (1.12) leaves levels ≤h unchanged; (1.64)–(1.69) define the stage space; operation-components supplies the component rule; the stage-nest admissibility lemma supplies A1 for every state assignment.
- 48524–48525: 4.14:lem-hull-cube is applied to the stage nest with top k.
- 48527–48533: G1 reads B-CMP122a (1.65)(i) at index m.
- 48534–48546: G2 reads B-CMP122a (1.65)(i) at its top alternative j=p.
- 48547–48561: G3 reads B-CMP122a (1.67)(ii) at old-nest index bar m and top j=p.
- 48562–48565: G4 reads B-CMP122a (1.69)(iii).
- 48578–48598: hull-cube-a and the hull lemma's empty-domain convention prove part (a) against B-CMP119 (2.38) and B-CMP122a (1.65),(1.69).
- 48600–48605: The hull lemma and m definition give the range used in the exhaustive split.
- 48607–48618: Stage-nest definition, B-CMP122a (1.12), hull-cube-a, and (1.65) prove G1.
- 48620–48635: hull-cube-a and B-CMP122a (1.65) prove G2; p. 191 is cited for the absence of powers and the empty (ii) range when j≤k₀.
- 48637–48658: hull-cube-a, its empty-domain convention and that of B-CMP122a, and (1.67)(ii) prove G3.
- 48660–48669: hull-cube-a and B-CMP122a (1.69)(iii) prove G4.
- 48671–48681: Parts (a), G1–G4 prove gauge-family-a and the positive-exponent range.
- 48685–48699: The tiling remark reuses gauge-family(b), operation-components-a, operation-conventions-a, and hull-cube-a.
- 48701–48722: B-CMP122a (1.64),(1.66),(1.68) impose regional conditions beyond the families in (1.65),(1.67),(1.69); the tiling is matched to the gauge-family case list and the a♯ regularity scale.
- 48723–48729: Persistence until a containing fill is used; after fills gauge-family(a) applies.
- 48731–48750: B-CMP122a's “it is easy to generalize” sentence introduces the generalized later-step space without proof; its interpretations use B-CMP119 (2.38) or the stage families; gauge-family-a bounds the exponent; the lemma on families of that space is to settle which family is used.
- 48751–48757: gauge-family(b) is applied to earlier exit stages and to the final stage; the hull lemma's Ω_(k+1)=empty convention is reused.
- 48765–48770: The componentwise nest is asserted to satisfy A1 of prepared-data-admissible-a and to support gauge-family(b), or (a) when no component is met.
- 48775–48801: The statement on the new families Z″_j, first clause, gives Z″_p⊂Z″_k and its formula; this proves tiling-later-steps-1.
- 48803–48811: B-CMP122a's unchanged-domains sentence and the component-nest persistence statement (a),(b) give later agreement; gauge-family(a) applies after fills.
- 48813–48829: hull-cube-a and gauge-family(a),(b) give memberships in B-CMP119 (2.38), B-CMP122a (1.65),(1.67),(1.69); p. 192 gives the top exponent k−k₀=N₀.
- 48831–48839: The same persistence, gauge-family(b), and the hull lemma's terminal empty-domain convention establish earlier-drop-out and final-stage claims.
- 48841–48847: The proposition establishing A1,A2 of prepared-data-admissible-a for all state assignments supplies A1 for the componentwise nest.
- 48849–48864: Component spacing, R_k≥3, and gauge-family(a) justify the single-state reading and old-structure alternative.
- 48868–48878: small-coupling-regime-a contains B-CMP119 (2.9), β₀, and the auxiliary bounds; operation-conventions-a and B-CMP122a p. 192 give the defining N₀ equality.
- 48890–48895: B-CMP122a p. 192 is the source of the comparison chain recorded after the main bound.
- 48900–48913: integer-power-bound-a and the N₀ equality supply the proof's target and reduction.
- 48921–48937: The second inequality of B-CMP119 (2.9), applied to (m,star), gives integer-power-bound-2, then integer-power-bound-a.
- 48939–48942: Specializing the general argument to m=k proves integer-power-bound-1.
- 48948–48950: The remark after B-CMP119 (2.6) permits β₀ arbitrarily small for small g; the lemma does not need β₀≤1.
- 48955–48969: B-CMP119 (2.9) and B-CMP122a p. 192 explain the three-input proof and why the consecutive-level consequence is insufficient.
- 48971–48983: B-CMP122a's weaker L₀<L/2 ceiling is considered hypothetically; integer-power-bound-2 and small-coupling-regime-a's block-count ceiling supply the squared and logarithmic bounds.
- 48985–48990: An alternative starts with B-CMP122a p. 192 and uses the first inequality of B-CMP119 (2.9); integer-power-bound-a instead gives a direct levelwise bound.
- 48994–49005: integer-power-bound hypotheses, small-coupling-regime-a and its definition, operation-conventions and operation-conventions-a are inherited; integer-power-bound-a defines c and the block-size definition defines c₁.
- 49013–49018: top-power-bound-1 is interpreted as a comparison of the operation's a♯_F member with the boxwise value at layer n.
- 49022–49035: small-coupling-regime-a and operation-conventions-a give top-power-bound-2; B-CMP119 (2.9), p. 256, supplies top-power-bound-3 and β₀.
- 49036–49044: The supremum definition gives two c facts; top-power-bound-3 is applied to (n,star) in the first range, with the remaining proof outside this chunk.

## Obligations named here

This list separates requirements used as inputs from unfinished or externally unsupported claims; it does not turn ordinary theorem hypotheses into assertions that their verification is open.

- 47746–47748: Prepared-data admissibility, including A2, is an operator-theorem hypothesis and is stated in B-CMP122a pp. 178–179 without proof.
- 47749–47753: A2 requires distance at least 6M between the top region and the complement of Ω_k.
- 47755–47761: The positivity lemma requires its displayed floor Fᵖᵤ, identified with block-size-conditions-a(v).
- 47789–47798: The real-background definition must supply a gauge on the containing M-cube with the stated A and ∇A bounds; the analytic path must fit in the previously fixed U(1) radius.
- 47814–47821: The ceiling of block-size-conditions-b bounds a_Q by a₁⊕γ₀/(24γ₁).
- 47850–47856: The sector step uses analyticity on the complex fibre and the sheet-derived matrix-element bound as its named inputs.
- 47869–47875: Sheet inversion requires box properties (b1)–(b4), A2, floor item (iii), and its displayed Fᵤ floor, item (iv).
- 47896–47913: The block-identity lemma assumes the operator-theorem hypotheses and inputs (a)–(d): sheets and norm control with enlarged Sh5 lists, real base-point spectrum, the complex sector bound, and clause D.
- 47993–48001: The core lemma requires nearby collar cubes to be level-k M-cubes of one aligned partition, supplied by A2.
- 48003–48010: Applying the core lemma requires domain radius at most M/4; the stated floor M≥144dρ_Q supplies this for J.
- 48031–48037: The core/packing argument uses the enlarged-domain diameter bound and the inequality between the regrouped and original distances.
- 48042–48047: Local balls require layer-crossing cost at least M, grid alignment at each level, and M>2L.
- 48078–48083: The M₁, M₁♯, and M floors, layer-coupling ceilings, and application-specific radius condition govern the order of choices.
- 48132–48138: The final operator conclusion explicitly assumes prepared-data admissibility at every nest of Bałaban's history and the one-sided block-size conditions.
- 48142–48147: The operation conventions are conditional on the named small-coupling regime and operation-component class.
- 48152–48155: The M and MR_j partitions are taken to form a compatible L-adic family.
- 48164–48172: Metric/layer agreement is delegated to the alignment statement, and component separation and segment-exit facts are named as facts used subsequently.
- 48180–48184, 48231–48235: Existence of a history level with f(n)=1 is an input of small-coupling-regime-a, used to define N₀.
- 48256–48260: The regime's requirement N_k>N₀ is used to obtain h<star−1.
- 48264–48269, 48273: The small-boxes lemma assumes an aligned grid-cube union, H⊂Ω, and positive side lengths at most S.
- 48338–48349: The hull lemma assumes A1, M≥13L²M₁♯, the terminal empty-domain convention, and a second-cover box at j≥2 with its prescribed size and center.
- 48373–48383: The precise A1 inputs are nesting, closed aligned level-i M-cube unions, and the displayed separation between Ω_i's complement and Ω_(i+1).
- 48461–48467: Low-index backgrounds are assigned to the α′ condition from B-CMP99b (3.35), using M₁♯ at indices 0,1,2 and h≥1.
- 48472–48477: Every printed-family cube must admit the gauge transformation and both scaled potential and derivative bounds; this paragraph specifies the requirement rather than proving gauge existence.
- 48506–48523: The stage classification relies on the exits-and-stage-nests persistence result and on stage-nest admissibility for every assignment of states.
- 48615–48618, 48625–48627, 48647–48649, 48667–48669: Membership checks must satisfy the printed families' size, index-range, and domain conditions; the text verifies these conditions for G1–G4.
- 48701–48705: B-CMP122a (1.64),(1.66),(1.68) impose additional regional conditions beyond the cube-family conditions.
- 48731–48750: The generalized later-step space is explicitly cited as printed without proof; its actual choice of cube family is deferred to the lemma on families of that space.
- 48765–48770, 48841–48847: The componentwise construction relies on the external proposition proving A1,A2 for every component-state assignment.
- 48849–48859: The single-component argument uses the stated separation of Z_k components and R_k≥3.
- 48868–48879: The auxiliary-power lemma assumes the small-coupling block-count inequalities, power-of-L counts, existence of N₀, β₀>0, L₀≥1, and L₀²≤L/3, with its stated m and e ranges.
- 48944–48950: Finiteness of c is explicitly named as remaining to show and is discharged immediately by continuity and decay; β₀≤1 is explicitly not required.
- 48961–48965: The consecutive-level inequality alone is explicitly said not to suffice for the auxiliary-power argument.
- 48971–48983: The weaker auxiliary ceiling is only a hypothetical replacement; the text keeps L₀²≤L/3.
- 48994–49005: The top-power lemma inherits the auxiliary-power hypotheses and the prescribed definitions of c and c₁.
- 49029–49044: Comparing R_star with R_n is explicitly named as remaining, and the proof announces three ranges but this chunk includes only the opening comparison in the first range.

No theorem is explicitly designated a “named open” result here. The two “without proof” notices concern cited external statements, while the last proof is incomplete because the excerpt ends.

## For the stage question

These entries record relevant statements, including both full complex-domain claims and the real-background restrictions of the geometry and gauge arguments; they do not infer admission or inclusion beyond what is written.

| Lines | Statement relevant to domains, admission, stages, or carried data | Status here | Scope / dependency |
|---|---|---|---|
| 47746–47753 | A2 puts the local enlarged boxes and an M-cube inside Ω_k. | proved conditionally | Uses prepared-data admissibility, whose proposition is cited as stated without proof. |
| 47755–47761 | Positivity is first considered for U in the real-background class U_R. | assumed | Real-background definition and positivity floor. |
| 47789–47798 | Real M-cube regularity produces a gauge and a cutoff analytic path u_z lying in U(1) for modulus below r_reg. | proved conditionally | This is a complex-parameter path constructed from a real background, using a₁⊕ from the form-walk lemma. |
| 47800–47812 | Gauge invariance keeps the transformed real background in U_R and the reading property identifies its local walk sum with that at u₁. | proved conditionally | Sh4, Sh2, local agreement, and a unitary gauge action. |
| 47814–47834 | The local sheet is analytic on U(1) and along the complex disk; the regularity ceiling makes its disk large enough for the Schwarz comparison at z=1. | proved conditionally | Uniform analytic walk convergence, Schur bound, and a_Q ceiling. |
| 47836–47848 | The positivity conclusion is obtained at real u₁ and real base points (U,0). | proved conditionally | Real symmetry, identity-background positivity, and localized comparison. |
| 47850–47861 | Analyticity on the complex fibre and a matrix-element bound extend positivity to Re Q≥m₁ on U(ε₁). | proved conditionally | Sector lemma; no further hypothesis is said to be used. |
| 47863–47883 | Re A≥m₁ and the inverse/resolvent sheet exist on U(ε₁), with common walk domains for all nonnegative x. | proved conditionally | Compression and sheet inversion with its floors. |
| 47885–47892 | Arbitrary irregular bond subsets are admitted; reading hulls and second-cover regularity do not enter this positivity/inversion proof. | proved conditionally | Unit frame, A2, and M-cube regularity. |
| 47903–47913 | The next lemma assumes the Q norm bound on U(1), base-point real spectrum, complex-sector bound on U(ε₁), and clause D. | assumed | Inputs previously attributed to the form-walk and positivity-inversion lemmas. |
| 47923–47929 | A and C are analytic and complex symmetric and AC=1 on the whole U(ε₁). | proved conditionally | Input (a), symmetry lemma, and invertibility from D. |
| 47931–47936, 47960–47967 | Identification with Bałaban's form and conditional integral is made on the current graph, while the algebraic identities hold throughout U(ε₁). | proved conditionally | Graph identity and block-identities-1,-2; B-CMP99b, B-CMP109, B-CMP116, and B-CMP119. |
| 47969–47984 | Base points have the sharper real spectral bounds, real points of U(ε₁) have the enlarged bounds, and the complex ball retains the sector estimate. | proved conditionally | Inputs (a)–(c), symmetry, and min–max. |
| 47986–47989 | J has norm at most γ₁ on U(1) and is real at real points. | proved conditionally | Q sheet norm and symmetry. |
| 48012–48017 | Complex resolvent parameter x is treated through Re x. | proved conditionally | Remark accompanying the inversion lemma; this is a parameter-domain statement rather than a new background-admission assertion. |
| 48019–48040 | Geometric reading uses enlarged lists containing reading hulls, while their size and distance bounds remain suitable for core expansions. | proved conditionally | Reading-hulls lemma and sheet/core properties. |
| 48042–48052 | Local-ball results are applied with radius ε₁ for C and resolvents and radius 1 for J, and data on the larger set [ν]∼ suffice. | proved conditionally | Local-balls lemma, A1, M>2L, and its cutoff. |
| 48078–48083 | Radii are chosen according to the condition imposed where the theorem is applied. | assumed | No universal new admission statement is made here. |
| 48120–48130 | The minimizing shift φ=−CJA′ is explicitly a minimization over real φ at a real base point, used to bound the Schur complement. | proved conditionally | Positive real A and block-identities-2; the passage does not assert complex minimization. |
| 48132–48138 | The operator theorem is concluded only after assuming admissibility of prepared large-field data at every history nest. | proved conditionally | prepared-data-admissible-a and one-sided block-size conditions. |
| 48164–48168 | Metric enlargement agrees with layer enlargement on portions of Ω_j whose traces on the operation components enter the analysis. | assumed | Agreement is assigned to the alignment statement elsewhere. |
| 48173–48202 | The operation has a transition level star with σ_star=M, finer levels at most M, upper levels at least LM, and lowest touched level h<star−1. | proved conditionally | Small-coupling regime and the convention proof at 48208–48261. |
| 48337–48368 | A hull on an A1 nest at j≥2 lies in a single cube with m∈{j−1,j}, crossing the next boundary and avoiding Ω_(m+2). | proved conditionally | Block floor and small-boxes lemma; geometric containment does not itself prove a background gauge bound. |
| 48461–48467 | Backgrounds on index-zero or index-one hulls use α′, a nest-independent condition, and the operation produces pairs strictly above h≥1. | cited | real-backgrounds-a and B-CMP99b (3.35). |
| 48472–48477 | A printed gauge family requires a gauge on the cube's intersection with the configuration domain, a Lie-algebra potential, and both printed regularity bounds. | assumed | The scale, α-index, and L₀-exponent are defined here; this is the gauge-admission requirement itself. |
| 48481–48496 | The hull cube belongs geometrically to the old-nest family and to its one-sided relatives. | proved conditionally | Hull-cube lemma and the cited family definitions; no separate complex-background extension is stated here. |
| 48506–48518 | A component exiting after n preliminary integrations is assigned the stage nest using Ω″ through p=h+n and Ω above p, with levels ≤h unchanged. | definition | The source identifies this as the nest defining the stage-n space in B-CMP122a (1.64)–(1.69). |
| 48518–48523 | The exit-stage nest persists until a containing component is filled and satisfies A1 for every assignment of states. | assumed | Exits-and-stage-nests lemma, operation-component rule, and stage-admissibility lemma elsewhere. |
| 48527–48533, 48607–48618 | At m<p the hull cube is admitted to printed family (i) on the new domains with exponent max(0,m−k₀). | proved conditionally | G1 and its membership proof. |
| 48534–48546, 48620–48635 | At m=p outside the old star-domain, family (i)'s top alternative applies, necessarily so if p≤k₀. | proved conditionally | G2 and its membership proof. |
| 48547–48561, 48637–48658 | At m=p inside the old star-domain, family (ii) uses the last old containment index bar m and exponent p−bar m. | proved conditionally | G3 and its membership proof, including the terminal empty-domain case. |
| 48562–48565, 48660–48669 | Above the exit stage, family (iii) uses old domains and has exponent zero. | proved conditionally | G4 and its membership proof. |
| 48568–48574, 48671–48681 | Every family has scale ℓ_m and α-index m with exponent at most max(0,m−k₀); positive exponents occur only from star through k. | proved conditionally | Part (a) and G1–G4. |
| 48701–48722, 48775–48801 | On Z the old layers from star to p enter the stage-p territory at scale ℓ_p, matching the a♯ regularity scale, whereas off Z no such tiling is asserted. | proved conditionally | New-family inclusion and stage-nest definition; additional regional requirements are cited from (1.64),(1.66),(1.68). |
| 48723–48729, 48803–48811 | At later renormalization steps the term created by an exit carries the same nest on X through k until a containing fill erases that structure. | proved conditionally | B-CMP122a unchanged-domains sentence and persistence (a),(b); gauge-family(a) applies at filled levels. |
| 48731–48743 | Outside X near a hull the nest may change through later fills and new large-field removals, and the generalized space imposes a condition there. | cited | The generalized-space sentence in B-CMP122a is explicitly printed without proof. |
| 48738–48750, 48813–48829 | The generalized-space condition has two natural readings, current-nest families or retained stage families, both giving Q membership and the same exponent ceiling. | proved conditionally | Hull-cube and gauge-family lemmas; actual family selection is assigned to another lemma. |
| 48751–48757, 48831–48839 | Earlier drop-outs keep their own exit-stage nest with the same k₀, and components still large-field after the operation carry the final nest with p=k and no G4 case. | proved conditionally | Persistence and gauge-family(b). |
| 48758–48770, 48841–48847 | At a current stage each survivor or earlier drop-out contributes its own state to the global componentwise nest, with the old nest off Z, and that nest satisfies A1. | proved conditionally | State-assignment admissibility proposition. |
| 48849–48864 | A hull cube reads at most one component state because it remains at least 2M from all other components; a cube meeting none reads the old structure. | proved conditionally | Side bound Mℓ_m≤M, component spacing MR_k≥3M, and gauge-family(a). |
| 48867–48951 | The auxiliary-integer exponent bound is controlled level by level by R_m rather than by the number of elapsed steps. | proved conditionally | Small-coupling inequalities, N₀ equality, and L₀²≤L/3. |
| 48955–48969 | The power-bound argument uses neither the number of RG steps, the operation's preliminary integrations, nor elapsed time since a large-field region was created. | proved conditionally | The three printed inputs identified in Remarks (1). |
| 48993–49018 | The top-power lemma states that every layer n≤k of a fixed operation has its per-operation a♯_F member bounded by the layer's boxwise value. | sketched | top-power-bound-a,-1; proof is only begun in this chunk. |
| 49021–49044 | The top-power proof reduces to comparing R_star with R_n and starts the range star<n≤k. | sketched | Auxiliary ceiling, N₀ equality, and B-CMP119 (2.9); two further ranges and completion are outside this excerpt. |

There is no explicit prepared-shell construction or prepared-shell admission statement in these lines. The text does discuss prepared-data admissibility, carried stage nests, drop-outs, fills, printed real gauge families, and complex operator balls as indexed above; it does not state a general complex-background admission theorem for all later stages here.
