# Chunk 06: lines 49015-50313
Sections: No section or subsection heading occurs in this excerpt; it continues item 4.14 (49015-49717) and begins material labelled 4.15 (49719-50313). Named divisions are “The weights” (49174), “The power” (49191), “The relation with $a^{\sharp}_F$” (49214), “The inclusion” (49502), “The constant $C$” (49517), “The space at later steps on drop-out nests” (49531), “Hulls at the two lowest levels” (49549), “The powers of $\mathsf{L}_0$” (49555), “The position of the factor” (49593), “The exponent” (49626), “The bound on the power” (49644), “Consequences for the first clause and the radii” (49663), “The regularity clause on cubes of side $M$” (49697), “The constants of the operator theorem” (49711), “Letters” (49722), “Couplings” (49729), “Standing hypotheses on the parameters” (49734), “Cube sizes” (49743), “Waiting depth” (49762), “Partitions” (49885), “Refinement” (49891), “Compatibility” (49898), “Regions” (49909), “Cubes of other partitions” (49917), “Touching” (49930), “Chains and connectedness” (49937), “Components” (49941), “Enlargement and removal of layers” (50038), “Hull” (50046), “Boxing” (50054), “Small components and one application of the boxing map” (50073), “The stabilised boxing map” (50087), “Replacement maps” (50096), “Coarse cubes and test cubes” (50153), “The input region of the step” (50163), “Primed sets” (50168), “Two properties of enlargements” (50173), “The general step” (50186), “The first step” (50231), and “The form of the small-field complement” (50281).

The opening lemma starts before this chunk; the final definition continues beyond it. Display names below retain the source label suffixes, with their 4.14 or 4.15 prefixes. Unnumbered displays are indexed where they define objects or carry a separately identified assertion or construction.

| Lines | Name / tag | Kind | What it states (one plain sentence, your words) | Status here | Reads (inputs it uses, by tag or name) | Key phrase |
|---|---|---|---|---|---|---|
| 49015-49019 | 4.14:lem-top-power-bound, concluding statement | lemma | The operation's top-power gauge constant is bounded by the boxwise constant at every level n at most k. | proved conditionally | small-coupling-regime-a; operation-conventions-a; B-CMP119 (2.9) | "for the layers $n\le k$ of that operation" |
| 49021-49085 | Proof of top-power bound | proof | Three ranges relative to the distinguished level establish the top-power estimate and its gauge-weighted version. | proved conditionally | small-coupling-regime-a; operation-conventions-a; B-CMP119 (2.9); definition of c(beta_0) | "The three ranges exhaust all levels $n\le k$" |
| 49025-49028 | 4.14:eq-top-power-bound-2 | estimate | Raising the small-coupling inequality bounds the top power by 3 to the minus N_0 times L R_*. | proved conditionally | L_0 squared at most L/3; R_*=L^(N_0-1) | "Raising the second inequality, between non-negative numbers" |
| 49029-49035 | 4.14:eq-top-power-bound-3 | estimate | Block counts at two history levels obey the two stated gap-dependent comparisons. | cited | B-CMP119 (2.9), p. 256; small-coupling-regime-a | "For every pair of levels $j>i$ of the history it states" |
| 49036-49038 | Elementary bounds for c(beta_0) | estimate | The supremum dominates every integer term and is at least one third. | proved in detail | definition of c(beta_0) | "by the definition of the supremum" |
| 49040-49059 | Top-power comparison above * | proof | For levels between * and k the gap is bounded by N_0 and absorbed into c(beta_0). | proved conditionally | top-power-bound-2, -3; beta_0 positive | "Since $\beta_0>0$" |
| 49061-49066 | Top-power comparison at * | proof | At the distinguished level the exponential factor is bounded by the fixed constant. | proved conditionally | top-power-bound-2; c(beta_0) at least 1/3; R_n at least 1 | "Here $R_\ast=R_n$" |
| 49068-49077 | Top-power comparison below * | proof | The first block-count comparison bounds all lower levels. | proved conditionally | top-power-bound-2, -3; c(beta_0) at least 1/3 | "Apply the first inequality" |
| 49087-49103 | Scope of the operation's top-power pairing | remark | The pairing applies only through k and gives no asserted uniform bound at later levels. | proved in detail | top-power-bound-3; integer-power-bound; B-CMP122a (1.64)-(1.67) | "No bound of the form" |
| 49105-49107 | Boxwise gauge convention | definition | The adopted gauge constant uses each hull's own level and needs no cross-operation pairing. | definition | mathfrak a(square) | "The value adopted for the gauge constant" |
| 49109-49118 | Inputs and independence of top-power proof | remark | The proof uses only block comparisons, the power bound, and the defining equality for N_0. | proved in detail | B-CMP119 (2.9); L_0 squared at most L/3; R_*=L^(N_0-1) | "The proof above uses only the following inputs" |
| 49120-49160 | 4.14:cor-hull-gauge-value — The gauge constants on a hull | corollary | Printed gauges satisfy territory-weighted hull bounds and the operation constant is dominated by the boxwise value. | proved conditionally | gauge-family; hull-cube; integer-power-bound; top-power-bound; printed gauge clauses; C=1 | "This proves~\eqref{4.14:eq-hull-gauge-value-1}" |
| 49124-49130 | Printed gauge and localisation input | hypothesis | The gauge is supplied by the cited family on Q or only on its intersection with the localisation domain. | cited | B-CMP119 (2.38); B-CMP122a (1.65), (1.67), (1.69); real-backgrounds | "is given on" |
| 49131-49135 | 4.14:eq-hull-gauge-value-a | definition | The boxwise constant is L squared times c_1 B M R_m alpha_0,m with the specified supremum constant. | definition | B; M; R_m; alpha_0,m; beta_0 | "Put" |
| 49137-49144 | 4.14:eq-hull-gauge-value-1 | estimate | Both weighted potential norms are strictly below the boxwise value, supplying reg-sharp at any larger constant. | proved conditionally | printed gauge; hull-cube; integer-power-bound; C=1 | "The strict" |
| 49146-49158 | Operation constant clauses (i)-(iii); 4.14:eq-hull-gauge-value-2 | estimate | The operation constant dominates every printed member and is bounded by the same-level boxwise constant through k. | proved conditionally | gauge-family-a; L_0 at least 1; top-power-bound-a | "For (iii): taking $n:=m\le k$ in (ii)" |
| 49162-49234 | Proof of hull gauge corollary | proof | Restricting a printed gauge, changing weights by at most L squared, and absorbing its power establish all clauses. | proved conditionally | gauge-family; hull-cube (2), (4); integer-power-bound-a; top-power-bound-a; real-backgrounds | "In both cases, therefore" |
| 49166-49172 | 4.14:eq-hull-gauge-value-3 | estimate | The printed gauge bounds the potential and gradient with exponent e at scale m on Q and hence H. | cited | gauge-family; printed gauge clauses; hull-cube (4) | "the gauge $u$ satisfies" |
| 49236-49294 | 4.14:prop-second-gauge-clause — The second gauge clause on admissible nests | proposition | Admissible ordinary, drop-out, and filled-island nests supply the hull cube, family membership, and second gauge clause. | proved conditionally | M floor; admissibility lemma; hull-cube; gauge-family; hull-gauge-value; supplied gauges | "Under the same hypotheses" |
| 49237-49246 | Floor and admissible-nest hypotheses | hypothesis | The proposition assumes the block-size floor and a nest of one of the three admissible types. | assumed | block-size-conditions; admissibility lemma for Bałaban's nests | "Assume the floor" |
| 49251 | Clause (G) | construction | The hull lemma supplies a cube of side M ell_m. | proved conditionally | hull-cube; M floor; admissible nesting | "The hull lemma therefore" |
| 49252-49261 | Clause (C) | estimate | The hull cube belongs to each displayed family with C=1 and the operation's stated exponent bound. | proved conditionally | gauge-family cases (a), (b1)-(b4); gauge-family-a | "Its cases (b1)--(b4) place" |
| 49262-49270 | Clause (V); 4.14:eq-second-gauge-clause-1 | estimate | A supplied family gauge has the boxwise weighted bound on every territory met by the hull. | proved conditionally | hull-gauge-value; supplied printed gauge | "Corollary~\ref{4.14:cor-hull-gauge-value}" |
| 49273-49278 | 4.14:eq-second-gauge-clause-2 | definition | The common gauge constant is the maximum over hull values and is bounded by the layerwise maximum. | definition | hull-gauge-value-a; finitely many levels | "by definition" |
| 49279-49290 | 4.14:eq-second-gauge-clause-3; ceiling criterion | requirement | The layerwise ceiling suffices for the theorem's ceiling, which conversely controls every level represented by a hull. | proved conditionally | second-gauge-clause-2; block-size-conditions-b, -c | "The first equivalence holds because" |
| 49292-49293 | Lowest-level gauge supply | hypothesis | At cover levels zero and one the second gauge clause is supplied in form alpha-prime. | assumed | real-backgrounds-a, (alpha') | "is supplied in the form" |
| 49296-49346 | Proof of second gauge proposition | proof | The hull and gauge lemmas give the three clauses and the finite maximum gives the ceiling equivalence. | proved conditionally | floor; admissibility lemma; hull-cube; gauge-family; hull-gauge-value; lowest-level supply | "The nest satisfies the hypotheses of the hull lemma" |
| 49348-49392 | 4.14:rem-layerwise-ceiling — The layerwise ceiling as a small-coupling condition | remark | The ceiling follows from a one-sided small-coupling threshold uniformly over histories and also controls each operation constant. | proved conditionally | B-CMP119 (2.5), (2.28), (2.9); small-coupling-regime; block-size-conditions | "We first show" |
| 49349-49355 | Ceiling parameters | hypothesis | The exponents and constants are taken from Bałaban and the positive ceiling is fixed by block-size conditions. | cited | B-CMP119 (2.6)-(2.9), (2.5), (2.28), (2.38); B-CMP122a (1.65); block-size-conditions | "the exponent of" |
| 49356-49358 | 4.14:eq-layerwise-ceiling-1 | definition | Phi is the stated coupling times logarithmic factors and fixed constants. | definition | beta_0; r; q_0; C_0; B; L; c_1 | "put" |
| 49360-49368 | Part (a); 4.14:eq-layerwise-ceiling-2; g-sharp | estimate | The gauge quantity is below M Phi(g_m), so a sufficiently small levelwise coupling ensures the ceiling. | proved conditionally | B-CMP119 (2.5), (2.28); positive ceiling | "Take" |
| 49369-49375 | Part (b), one-sided order of constants | remark | The coupling ceiling imposes no history, age, depth, component-count, or operation-count bound. | proved in detail | Phi; block-size-conditions-d | "It involves none of" |
| 49376-49382 | Part (c), uniformity over histories | estimate | Under the small-coupling regime at each operation, each hull constant depends only on its own level's data. | proved conditionally | small-coupling-regime at every operation; hull-gauge-value-a; integer-power-bound | "Assume Ba{\l}aban's small-coupling regime" |
| 49383-49390 | Part (d); 4.14:eq-layerwise-ceiling-3 | definition | The operation constant is the top power times the maximum of its lower-level radii. | definition | operation regime; N_0; k_0; * | "and put" |
| 49388-49390 | Operation domination and ceiling | estimate | The operation constant dominates all its exponent-weighted radii and obeys the layerwise ceiling only through k. | proved conditionally | L_0 at least 1; top-power-bound; block-size-conditions-c | "Nothing is asserted" |
| 49394-49493 | Proof of layerwise ceiling remark | proof | Minimality of R_m and logarithmic decay establish the threshold, history independence, and operation ceiling. | proved conditionally | B-CMP119 (2.5), (2.28), (2.9); integer-power-bound; top-power-bound; layerwise ceiling | "Multiply by" |
| 49420-49429 | Logarithmic contributions assertion | remark | The source's unproved logarithmic-contribution statement is given a layerwise proof using block-count comparisons. | proved conditionally | B-CMP99b; B-CMP122a p.192; B-CMP119 (2.9); integer-power-bound; top-power-bound | "Its layerwise form" |
| 49467-49471 | Alternative operation ceiling route | proof | A top-level integer-power bound followed by R_k at most L R_n gives a ceiling with an extra L. | sketched | integer-power-bound at m=k; B-CMP119 (2.9) | "One route to a ceiling" |
| 49473-49486 | Sharper operation ceiling route | proof | Applying the top-power bound at every lower level and taking the maximum gives the exact stated ceiling. | proved conditionally | top-power-bound-a; block-size-conditions-c | "take the maximum over" |
| 49488-49492 | Later-level limitation | remark | No uniform cross-operation bound is asserted for later levels, while the layerwise constant remains history-uniform. | proved in detail | B-CMP119 (2.9); hull-gauge-value-a | "no bound uniform in the history is" |
| 49495-49500 | 4.14:rem-supply-scope — Scope of the second gauge clause's supply | remark | Five application conditions lie outside the implication of the free-current operator theorem. | assumed | operator-theorem; real-backgrounds-b | "lie outside the implication" |
| 49502-49511 | Supply point (i), inclusion and radius requirement | requirement | The expansion's real background must belong to a space with every required gauge family and sufficiently small radii. | assumed | B-CMP109 (1.12); B-CMP119 (2.38); B-CMP122a (1.65), (1.67), (1.69); real-backgrounds; block-size-conditions | "must lie in a space" |
| 49513-49515 | Global reading of local gauges | definition | Gauges supplied on Q intersect X are read globally on Q intersect Omega_0 by an expansion convention. | definition | B-CMP122a (1.63) | "is a convention of the expansion" |
| 49517-49529 | Supply point (ii), C=1 | requirement | The expansion must allow C=1 because C=2 cubes need not fit beside a one-cube shell. | assumed | B-CMP122a p.191; shell geometry | "The expansion must state its gauge clause" |
| 49525-49529 | Shell-fit explanation | proof | A union of M ell_m cubes need not be a union of twice-sized cubes, explaining the C=1 choice. | sketched | Omega''_m near boundary Z''_m | "need not be a" |
| 49531-49533 | Drop-out | definition | A drop-out is a component where preliminary integrations stop after a new large field appears. | definition | mathsf Z; preliminary integrations | "A \emph{drop-out} is a" |
| 49534-49541 | Later drop-out spaces and carried boundary terms | requirement | The cited construction leaves new B_k^(n) terms among boundary terms and asserts generalisability of spaces without proof. | named open | B-CMP122a p.191 | "printed without proof" |
| 49543-49547 | Supply point (iii), choice of drop-out family | requirement | The expansion must choose which displayed family its later drop-out space carries. | assumed | gauge-family; second-gauge-clause; hull-gauge-value-a | "the expansion therefore has to fix only one thing" |
| 49549-49553 | Supply point (iv), lowest hulls | hypothesis | Cover levels zero and one use the first admitted second-gauge form at block size M_1-sharp. | assumed | real-backgrounds-a; B-CMP99b (3.35) | "is supplied in the first of its two admitted forms" |
| 49555-49563 | Supply point (v), first-clause ceiling reading | requirement | The first gauge ceiling must use M_1 c_1 R_n alpha_0,n at every stage layer. | assumed | block-size-conditions-b; B-CMP99b (3.35); k_0=k-N_0 | "is to be read, in every layer" |
| 49564-49574 | Supply point (v), radius reading and choice order | requirement | Background inclusion radii must use c_1 R_n alpha_dot,n as one-sided coupling conditions after L and M. | assumed | real-backgrounds-b; block-size-conditions-c; block-size-conditions; 2.3:def-cap | "are to be read, in every layer" |
| 49576-49582 | Unchanged clauses and theorem scope | remark | The M-cube regularity clause, its ceiling, and operator constants remain unchanged, and none of the five points bounds the listed parameters below. | proved conditionally | separation statement; top clause; operator-theorem (I); real-backgrounds-a, -b | "Point~(v) moves no constant" |
| 49585-49717 | Proof of supply-scope point (v) | proof | Tracking all seven stage-space entries and their exponents justifies the enlarged readings and unchanged operator constants. | proved conditionally | B-CMP122a (1.64)-(1.68); integer-power-bound; top-power-bound; separation statement; filled-island induction supply | "We prove the assertions of~(v)" |
| 49586-49591 | Points (i)-(iv) and early-stage scope | remark | The first four points remain application checks, and stages through k_0 have no power corrections. | cited | B-CMP122a (1.64)-(1.67), p.191 | "state which conditions the application has to verify" |
| 49593-49624 | Seven-entry stage-space factorisation | estimate | The power multiplies all seven regularity, current, and fluctuation entries in both stage-space bounds. | cited | B-CMP122a p.190, (1.64), (1.66); auxiliary U_p,X and J_p,X | "stands outside the bracket" |
| 49626-49642 | 4.14:eq-supply-scope-1 | estimate | Every radius-indexed exponent in an affected layer lies between zero and n-k_0 at most N_0. | proved in detail | B-CMP122a (1.64), (1.66), (1.68) | "Thus whenever" |
| 49644-49661 | 4.14:eq-supply-scope-2 and two proofs | estimate | The power multiplying an entry is at most c_1 R_n by either power lemma. | proved conditionally | supply-scope-1; integer-power-bound-a; top-power-bound-a; L_0 at least 1 | "The same bound also follows" |
| 49663-49679 | First gauge ceiling derivation | proof | The available gauge has the power-weighted constant, and replacing it by c_1 R_n works also at uncorrected lower layers. | proved conditionally | supply-scope-2; real-backgrounds-a; block-size-conditions-b; R_n at least 1 | "therefore serves every layer" |
| 49681-49695 | Radius reading and non-cap derivation | proof | The same domination controls current and fluctuation radii and gives only layerwise coupling restrictions. | proved conditionally | supply-scope-2; real-backgrounds-b; block-size-conditions-c; 2.3:def-cap | "are therefore not caps" |
| 49697-49705 | M-cube separation and unchanged top clause | proof | Separation from the post-operation large-field region leaves only the zero-exponent top clause on these cubes. | proved conditionally | separation statement for M-cubes; Z_k^post contains drop-outs and retained large fields | "By the separation statement for these cubes" |
| 49707-49709 | Filled-island induction hypothesis supply | requirement | Filled-island use requires the cited assertion that the configuration satisfies the induction hypothesis, printed without proof. | named open | B-CMP122b; second-gauge-clause | "printed without proof" |
| 49711-49716 | Operator constants unchanged | proof | The modification changes supplied background data rather than a constant in the operator theorem. | proved in detail | real-backgrounds; real-backgrounds-a, -b; operator-theorem (I) | "so none is changed" |
| 49719-49766 | 4.15:not-cube-sizes — The cube sizes and the waiting depth | definition | This fixes the section's parameters, running minimum cube sizes, and waiting depth. | definition | H2-H5; Theorem 0 clause (0) | "letters and standing hypotheses" |
| 49722-49732 | Letters and couplings | definition | N, L, M, M_1, M_2, K, d, the couplings, and x_j are assigned their stated meanings and order. | definition | 2.2:not-hypotheses H2-H4; Theorem 0 | "We write" |
| 49734-49741 | Standing coupling hypothesis; 4.15:eq-cube-sizes-a | hypothesis | The only coupling hypothesis used is x_j greater than g inverse squared at least gamma_H inverse squared greater than one. | assumed | 4.1:thm-clause-zero | "The only hypothesis on the couplings that is used" |
| 49743-49752 | Running minimum and 4.15:eq-cube-sizes-1 | definition | Check-x_j is the past minimum of x_i and check-R_j is the least nonnegative integer power of L exceeding its logarithmic power. | definition | cube-sizes-a; H5 exponent r | "Let $\check{R}_j$ be the least power" |
| 49754-49756 | Cube-size existence and monotonicity | lemma | Check-R_j is well defined, at least one, and non-increasing under the stated numerical hypotheses. | sketched | later lemma on cube sizes; cube-sizes-a; L at least 2; r positive | "The lemma on the cube sizes shows" |
| 49758-49760 | Reading of Bałaban's R_j | definition | Every occurrence of the size parameter R_j is read as check-R_j, without renaming sets called R. | definition | check-R_j | "we read $R_j:=\check{R}_j$" |
| 49762-49765 | Waiting depth mathsf N_k | definition | The waiting depth at k is check-R_k. | definition | check-R_k | "The \emph{waiting depth} at level $k$" |
| 49768-49809 | 4.15:def-no-creation — Two formulations of the no-creation condition | definition | Two admitted readings describe the absence of creations in the recent waiting window of a large-field component. | definition | term of T rho; later histories and creation sets; waiting depth; B-CMP122a p.176 | "the following two ways" |
| 49769-49783 | Z_k, creation inside C | definition | Z_k is the small-field complement and a creation is inside C when its creation set meets C as a point set. | definition | 1.5:def-densities; later components, histories, W-hat_t | "A \emph{creation at level $t$ lies inside $C$}" |
| 49791-49798 | (ii'); 4.15:eq-no-creation-a | requirement | The principal reading requires k at least N_k and no creation inside C at k-N_k<t≤k. | definition | waiting depth; creation sets | "The inequality $k\ge\mathsf{N}_k$ holds" |
| 49799-49808 | (ii''); 4.15:eq-no-creation-b | requirement | The alternative reading tests all existing levels in the window without separately requiring N_k preceding steps. | definition | waiting depth; creation sets | "it is not required" |
| 49811-49876 | Justification of the window and of the two readings | proof | The step indexing explains the window, equivalence when enough steps exist, and exclusion of a vacuous early-level reading. | proved in detail | B-CMP122a p.176 and (1.11); no-creation-a, -b; waiting depth | "The two readings differ only" |
| 49819-49827 | Last-creation age and current-step exclusion | estimate | Any last creation inside C must be at least N_k levels old, so current-level creation is forbidden. | proved conditionally | either no-creation reading; N_k at least 1 | "Indeed" |
| 49829-49838 | Renewed-level window | identity | The T_j operations indexed h through k-1 produce exactly the levels renewed by R. | cited | B-CMP122a (1.11); h=k-N_k | "This window agrees with" |
| 49840-49844 | Equivalence and early-level difference of readings | proof | The two windows coincide for k at least N_k, while only the alternative tests early histories. | proved in detail | no-creation-a, -b; integer indexing | "For integers" |
| 49846-49855 | Structural route under alternative reading | requirement | Deriving k at least N_k from creations requires the alternative clause to test every existing step when k is smaller. | proved in detail | alternative no-creation reading; prospective structural creation statement | "it must therefore bear on all the steps" |
| 49857-49860 | Excluded third formalisation | requirement | The chapter excludes automatically satisfying no-creation when fewer than N_k steps exist. | definition | no-creation condition (ii) | "It is not admitted as a reading" |
| 49862-49866 | Narrower intersection readings | remark | Later arguments will produce a common coarse cube, so they also work with narrower notions of intersection. | sketched | later coarse partition and creation arguments | "it produces a cube" |
| 49868-49875 | Additional action conditions | hypothesis | Conditions (i), the remainder of (ii), and (iii) further restrict actions but are not used by the following arguments. | assumed | B-CMP122a p.176; later definition of action level | "use only one property of an action" |
| 49878-49903 | 4.15:def-torus-partitions — Compatible partitions of the torus into cubes | definition | All levels use finite mutually refining common-origin cube partitions on a single torus. | definition | torus period p; powers of L | "All regions of all levels are subsets of one torus" |
| 49879-49883 | Common torus, period and covering map | definition | The ambient torus is R^d modulo p Z^d and pi is its covering map. | definition | p positive | "We write" |
| 49885-49889 | Partition of side a; 4.15:eq-torus-partitions-1 | definition | A partition consists of projected closed lattice cubes with side dividing p and has (p/a)^d members. | definition | p/a a positive integer; pi | "The \emph{partition of side $a$}" |
| 49891-49896 | Refinement and divisibility criterion | definition | Refinement means unique coarse containment of each fine cube and reconstruction of each coarse cube from its fine cubes. | definition | common-origin partitions; integral side ratio | "if two conditions hold" |
| 49898-49902 | Compatibility, finest partition and torus-size scope | hypothesis | The construction uses finitely many pairwise comparable partitions with a finest one and assumes only the stated divisibilities. | assumed | common origin; sides are powers of L times a length; B-CMP119 p.265 | "They are \emph{pairwise compatible}" |
| 49905-49947 | 4.15:def-regions-components — Regions, touching, chains and components | definition | Regions are sets of finest cubes with point-set touching and chain components. | definition | torus-partitions; P_bullet | "A \emph{region} is a set" |
| 49909-49915 | Regions and point-set convention | definition | A region denotes both its finest-cube set and its union in the torus. | definition | finest partition | "The same letter" |
| 49917-49928 | Other-partition cubes and P-regions | definition | Coarse cubes are regions of their constituent finest cubes and P-regions are unions of such cubes. | definition | refinement; torus-partitions | "is regarded as the region" |
| 49930-49935 | Touching and disjointness | definition | Cubes and regions touch when their point sets meet, including at corners or by containment. | definition | region point sets | "have a common point" |
| 49934-49935 | Non-touching implies disjoint point sets | proof | A common point would belong to a touching pair of member cubes. | proved in detail | touching definition | "Indeed, a common point" |
| 49937-49939 | Chains and connectedness | definition | A chain is a finite touching sequence and connectedness requires chains between every pair in a nonempty region. | definition | touching | "A \emph{chain in $X$}" |
| 49941-49946 | Components and chain equivalence | definition | Components are the equivalence classes generated by touching, and the empty region has none. | definition | chains; regions | "The \emph{components} of $X$ are the classes" |
| 49941-49944 | Proof of equivalence relation | proof | Singletons, reversal, and concatenation prove reflexivity, symmetry, and transitivity of chain connection. | proved in detail | chains | "It is reflexive" |
| 49949-49962 | 4.15:lem-subdivision-independence — Components do not depend on the subdivision | lemma | Fine-cube connectivity is equivalent to coarse-cube connectivity, so components stay coarse regions and individual cubes are connected. | proved in detail | torus-partitions; regions-components | "The remaining assertions follow" |
| 49964-50026 | Proof of subdivision independence | proof | Connectivity inside a cube and preservation of touching let chains pass between coarse and fine partitions. | proved in detail | refinement; integral side ratio; touching | "We first record two facts" |
| 49970-49989 | Fact (alpha), fine cubes inside a coarse cube | lemma | Fine cubes inside one coarse cube form a connected region. | proved in detail | lattice index box; coordinate unit moves | "which proves" |
| 49991-49996 | Fact (beta), touching under refinement | lemma | Two coarse cubes touch exactly when some pair of their fine cubes touch. | proved in detail | coarse cubes are unions of fine cubes | "This holds because" |
| 50028-50109 | 4.15:def-enlargement-hull — Enlargement, hull and the stabilised boxing map | definition | This fixes coarse enlargements, hulls, connected-component boxing, stabilisation, and replacement maps. | definition | torus-partitions; regions-components; W_t=LM check-R_t | "Fix a renormalisation step" |
| 50033-50036 | Coarse partition and region complement | definition | P_t has side W_t and X^c consists of finest cubes absent from X. | definition | torus-partitions; check-R_t | "we write $X^c$ for its complement" |
| 50038-50044 | Enlargement, iteration and layer removal | definition | Enlargement adds touching coarse cubes and inverse enlargement removes cubes touching the complement. | definition | P_t; touching; B-CMP119 pp.248,265 | "thus $\sim$ adds one layer" |
| 50046-50052 | P_t-hull and intersection convention | definition | The hull consists of coarse cubes meeting a region, with either intersection reading preserving containment and contact. | definition | touching; B-CMP119 bar-Z_k | "the \emph{$\mathcal{P}_t$-hull}" |
| 50054-50066 | Coarse cube indexing, coordinate ranges and box(C) | construction | Connected coarse regions are boxed by taking the product of their coordinate residue ranges. | definition | N_t=p/W_t; coarse cube c_n | "the product of the coordinate ranges" |
| 50065-50066 | Extensiveness of box(C) | proof | Each original cube has every coordinate in the corresponding range and therefore belongs to its box. | proved in detail | coordinate ranges | "since every" |
| 50066-50071 | Cyclic intervals, connected box and lifted parallelepiped | lemma | A later boxing lemma is assigned cyclic-interval and connectedness claims, with the construction identified with a smallest lifted rectangle when injective. | sketched | later lemma on boxing; B-CMP119 (3.20) | "It is shown" |
| 50073-50080 | Small components | definition | A component is small if it fits in the projected image of a cube of side 100 W_t. | definition | B-CMP119 (3.20); subdivision-independence | "\emph{small} if its point set is contained" |
| 50081-50085 | 4.15:eq-enlargement-hull-1; one-step boxing map | definition | M_1 X adjoins the boxes of every small component to X. | definition | small components; box(C) | "put" |
| 50087-50094 | 4.15:eq-enlargement-hull-2; stabilised boxing map | construction | M X is the first stationary iterate of M_1 and is extensive and idempotent. | proved in detail | finite coarse partition; enlargement-hull-1 | "We prove the assertions made about $q_0$" |
| 50096-50104 | Replacement maps and replacement identity | definition | A replacement map adjoins connected supersets of selected components, equivalently replacing those components by these supersets. | definition | components; connected supersets B_i | "a \emph{replacement map} if" |
| 50103-50104 | Replacement identity justification | proof | Replacing C_i by a superset B_i gives the same union as adjoining B_i. | proved in detail | C_i contained in B_i | "valid because" |
| 50105-50108 | Generality of replacement-map formalisation | remark | Later boxing conclusions use only composition of connected-superset replacements. | sketched | later boxing lemma (d), (e) | "only its structure as a composite of replacement maps is used" |
| 50111-50143 | Proof of stabilisation and idempotence | proof | Increasing subsets of finitely many coarse cubes stabilise, after which iteration and re-stabilisation leave the region unchanged. | proved in detail | enlargement-hull-1, -2; N_t^d finite | "can be strict for at most $N_t^d$ values" |
| 50145-50313 | 4.15:def-small-field-complement — The small-field complement as a union of enlargements | definition | The step's small-field complement is organised as enlargements of new large-field hulls and the incoming large-field hull. | definition | B-CMP119 §§1,3; torus-partitions; enlargement-hull; adopted first-step reading | "The form of the small-field complement" |
| 50148-50151 | First-step substitution | construction | The first step uses the same construction with §1 decompositions replacing those of §3. | cited | B-CMP119 §§1,3 | "with the first-step decompositions of unity" |
| 50153-50161 | Coarse and test cubes | definition | The step uses coarse cubes of side LM check-R_t and test cubes of side L squared M_2 check-R_t. | definition | torus-partitions; regions-components; enlargement-hull; B-CMP119 §§1,3 | "The \emph{test cubes}" |
| 50163-50166 | Incoming region Y | definition | Y is the entering term's large-field region and is empty at the first step. | definition | Z_k=Lambda_k^c; later history definition | "The step takes as input a region" |
| 50168-50171 | Primed sets and bar-Z_k | definition | Priming means taking the coarse hull and Bałaban's bar-Z_k is the incoming hull. | definition | P_t, Q_t, P_0, P_1, Q_1; enlargement-hull | "denotes the union of all coarse cubes meeting it" |
| 50173-50184 | Enlargement identities; 4.15:eq-small-field-complement-1 | identity | Enlargement distributes over unions and cube decompositions, and successive enlargements add layer counts. | proved in detail | enlargement-hull | "Both follow" |
| 50188-50191 | General step (a), P_t | construction | A decomposition of unity outside four layers around the incoming hull sums over test-cube regions P_t. | cited | B-CMP119 (3.2), p.265 | "he introduces the decomposition of unity" |
| 50192-50204 | General step (b), axial gauge, B_t(P''_t); 4.15:eq-small-field-complement-2 | construction | Axial gauge fixing occurs outside one layer around P'_t and five around the incoming hull, giving the displayed complement. | cited | B-CMP119 §3; 1.5:def-block-average | "He takes the subset" |
| 50205-50211 | General step (c), Q_t | construction | The approximate-fluctuation decomposition sums over test-cube subdomains of the one-layer-reduced gauge-fixing region. | cited | B-CMP119 (3.3); B_t(P''_t) | "which restricts the approximate fluctuation fields" |
| 50212-50219 | General step (d), Omega_t | construction | Omega_t excludes the specified enlargements of Q'_t and the gauge-fixing complement and supports only small-field factors. | cited | B-CMP119 (3.5) | "he sets" |
| 50221-50229 | 4.15:eq-small-field-complement-a and derivation | identity | At general steps the complement is the union of two-layer Q', four-layer P', and eight-layer incoming-hull enlargements. | proved conditionally | small-field-complement-1, -2; B-CMP119 (3.5) | "Insert" |
| 50231-50237 | First step (a), P_0 and P_1 | construction | The first step has two plaquette large-field sets, with P_1 outside the enlarged P_0 hull. | cited | B-CMP119 (1.2), (1.4), pp.246-248 | "Both restrict plaquette variables" |
| 50238-50250 | First step (b); 4.15:eq-small-field-complement-3 | hypothesis | The adopted first-step reading expresses the axial-gauge complement as enlargements of the P_0 and P_1 hulls with nonnegative integer depths. | assumed | B-CMP119 definition after (1.4); unspecified a_0,a_1 | "it is the reading of that definition adopted here" |
| 50251-50256 | First step (c), Q_1 | construction | The approximate-fluctuation large-field set Q_1 ranges over test-cube unions in the reduced gauge-fixing domain. | cited | B-CMP119 (1.8); B_1(P''_1) | "It is the large-field set of" |
| 50257-50265 | First step (d), Omega_1 and resummation | construction | The first small-field domain excludes the specified enlargements, has the stated separation, and is fixed during resummation over P_0, P_1 and Q_1. | cited | B-CMP119 (1.10); coarse side W_1 | "Ba{\l}aban sets" |
| 50267-50273 | 4.15:eq-small-field-complement-b and derivation | identity | The first-step complement is the union of enlarged Q'_1, P'_0 and P'_1 with their displayed depths. | proved conditionally | adopted small-field-complement-3; small-field-complement-1; B-CMP119 (1.10) | "rewritten by means of the reading" |
| 50274-50279 | Aggregate primed sets | definition | At the first step P' combines both plaquette hulls and Q' is Q'_1, while later steps use P'_t and Q'_t. | definition | first-step and general-step hulls | "by definition" |
| 50281-50299 | 4.15:eq-small-field-complement-c; downstream complement hypothesis | hypothesis | Every complement is assumed in the finite-union form with new-field generators inside P' union Q' and an incoming-hull enlargement. | assumed | small-field-complement-a, -b; first-step adopted reading -3; finite I; nonnegative layer counts | "enters as a hypothesis" |
| 50301-50304 | Cube-by-cube complement representation | identity | Distributing the generator enlargements rewrites the complement using individual coarse cubes and their maximal applicable depths. | proved conditionally | small-field-complement-1, -c | "By the second identity" |
| 50305-50309 | First-step P' scope and failure of narrower choice | remark | Including P'_0 in P' is necessary for the asserted representation because P'_1 and Q'_1 enlargements need not cover its contribution. | proved conditionally | small-field-complement-b; P'=P'_0 union P'_1 | "it can fail when" |
| 50311-50313 | Identification of general and first-step sets | remark | The named sets are identified with the corresponding general-step and first-step objects in Bałaban. | cited | B-CMP119 (3.2)-(3.5), (1.2), (1.4), (1.8), (1.10) | "The sets" |

## Forward and backward references

References below enumerate occurrences by their local line ranges; repeated targets within one continuous argument are grouped, with the occurrence lines retained. “Later” targets are not treated as proofs present in this chunk. Bibliographic keys are recorded exactly as supplied by the source, without consulting other files.

- 49022-49024: small-coupling-regime-a supplies L_0≥1 and L_0²≤L/3; operation-conventions-a supplies R_*=L^(N_0−1).
- 49029-49035: B-CMP119 (2.9), p.256, supplies both block comparisons and beta_0; small-coupling-regime-a includes them and R_j≥1.
- 49040, 49049-49050, 49065, 49068-49070: top-power-bound-3 and -2 are used in the three level ranges.
- 49079-49084: operation-conventions gives N_0≥2; top-power-bound-a is the estimate proved, and top-power-bound-1 its weighted conclusion (both statements begin before the chunk).
- 49087-49095: top-power-bound scope is compared with B-CMP122a (1.64)-(1.67) and integer-power-bound.
- 49097-49103: top-power-bound-3 explains why top-power-bound-a is not asserted beyond k.
- 49111-49114: B-CMP119 (2.9), the small-coupling power inequality, and the defining equality for N_0 are the proof's stated inputs.
- 49121-49130: gauge-family cases (a),(b) define the nest and cube setting; B-CMP119 (2.38) or B-CMP122a (1.65),(1.67),(1.69) supplies the gauge; real-backgrounds defines its potential representation.
- 49142-49144: real-backgrounds supplies the meaning of reg-sharp.
- 49163-49172: gauge-family supplies the radius index, scale and exponent; hull-cube (4) supplies H⊂Q.
- 49174-49176: hull-cube (2) restricts the territories meeting H.
- 49194-49200: gauge-family-a bounds e and identifies its positive-exponent range; integer-power-bound and integer-power-bound-a control that power.
- 49208-49212: real-backgrounds specifies the single-upper-bound gauge clause; hull-gauge-value-1 supplies its strict inequalities.
- 49216-49220: gauge-family-a yields e≤N_0 and the first inequality of hull-gauge-value-2.
- 49227-49233: top-power-bound and top-power-bound-a give the second inequality of hull-gauge-value-2; hull-gauge-value-a gives its equality.
- 49237-49240: block-size-conditions supplies the floor; the admissibility lemma for Bałaban's nests supplies nesting required by hull-cube.
- 49249-49258: hull-cube-a and hull-cube give Q; B-CMP119 (2.38) and B-CMP122a (1.65)(i),(1.67)(ii),(1.69)(iii) identify its families and indices.
- 49262-49271: real-backgrounds-a fixes the gauge representation; the same printed clauses supply u; hull-gauge-value-a fixes c_1 and B.
- 49279-49290: block-size-conditions-b and operator-theorem impose the ceiling; block-size-conditions-c is the every-level version, compared with second-gauge-clause-3 and -2.
- 49292-49293: real-backgrounds-a (alpha') supplies the second gauge clause at levels 0 and 1.
- 49297-49302: admissibility lemma, hull-cube and hull-cube-a supply (G) from nesting and the floor.
- 49304-49308: gauge-family cases (a),(b1)-(b4), its gauge-family-a estimate, and the printed B-CMP119/B-CMP122a families supply (C).
- 49310-49317: hull-gauge-value, gauge-family and hull-gauge-value-a yield second-gauge-clause-1 and its finite maximum -2.
- 49322-49325: real-backgrounds identifies the numerical upper-bound meaning of a-sharp.
- 49335-49342: second-gauge-clause-1 and -3 establish the relation between block-size-conditions-b and -c.
- 49344-49345: real-backgrounds-a (alpha') is again the supplied lowest-level clause.
- 49349-49355: B-CMP119 (2.6)-(2.9), (2.5), (2.28), (2.38), B-CMP122a (1.65), and block-size-conditions fix the ceiling parameters.
- 49367, 49370-49371: block-size-conditions-c is the desired ceiling and -d sets the order of choices.
- 49376-49384: small-coupling-regime is assumed at every operation, or at the specified operation for part (d); hull-gauge-value-a gives the levelwise dependence.
- 49395-49404: B-CMP119 (2.5) defines R_m by minimality and (2.28) defines alpha_0,m.
- 49410-49418: layerwise-ceiling-1 and -2 prove block-size-conditions-c using the constructed g-sharp.
- 49420-49429: B-CMP99b has the small-M-alpha condition; B-CMP122a p.192 prints the logarithmic assertion without proof; its layerwise form is proved here using B-CMP119 (2.9), integer-power-bound and top-power-bound.
- 49440-49446: B-CMP119 (2.9), displayed in small-coupling-regime-a, is the only cross-level input.
- 49448-49454: integer-power-bound and integer-power-bound-a are applied with each operation's indices; hull-gauge-value gives the own-level bound.
- 49467-49471: integer-power-bound at m=k and B-CMP119 (2.9) give the alternative ceiling route.
- 49473-49486: top-power-bound, top-power-bound-a and block-size-conditions-c prove the sharper route supplying second-gauge-clause.
- 49488-49492: B-CMP119 (2.9) explains the later-level limitation.
- 49496-49500: operator-theorem does not itself prove the expansion's real-backgrounds-b supply conditions.
- 49504-49511: B-CMP109 (1.12), B-CMP119 (2.38), B-CMP122a (1.65),(1.67),(1.69), real-backgrounds and gauge-family specify admitted families; block-size-conditions fixes radii for real-backgrounds-b.
- 49513-49515: B-CMP122a (1.63) gives local representation domains; the expansion supplies the global-reading convention.
- 49518-49529: B-CMP122a p.191 leaves C a small positive integer, allowing the required C=1 choice.
- 49534-49541: B-CMP122a p.191 asserts later drop-out spaces can be generalised and terms carried as boundary terms, explicitly without proof.
- 49543-49547: gauge-family and second-gauge-clause supply cube membership and hull-gauge-value-a under each displayed family, leaving the family choice to the expansion.
- 49551-49553: real-backgrounds-a and B-CMP99b (3.35) provide the admitted lowest-level form at M_1-sharp.
- 49559-49567: block-size-conditions-b, B-CMP99b (3.35), and real-backgrounds-b are to be read at the power-corrected layerwise values.
- 49569-49579: block-size-conditions-c and block-size-conditions set the type and order; 2.3:def-cap defines caps; real-backgrounds-a, block-size-conditions-b and operator-theorem (I) specify unchanged clauses and constants.
- 49581-49591: operator-theorem excludes points (i)-(v) from its implication; B-CMP122a (1.64)-(1.67), p.191, supplies the no-power/void conditions for j≤k_0.
- 49593-49618: B-CMP122a p.190, (1.64) and (1.66), supplies the seven-entry bounds, auxiliary configurations and exponents.
- 49620-49624: B-CMP122a (1.65),(1.67) are only part of the entries multiplied by the power.
- 49629-49637: B-CMP122a (1.64),(1.66),(1.68) supplies all exponent cases, including zero powers above j.
- 49644-49661: supply-scope-1, integer-power-bound and integer-power-bound-a prove supply-scope-2; top-power-bound and top-power-bound-a give the alternative proof.
- 49663-49679: B-CMP99b (3.35), real-backgrounds-a, supply-scope-2, block-size-conditions-b and the regime of integer-power-bound justify the first ceiling reading at all layers.
- 49681-49695: real-backgrounds-b, block-size-conditions-c and 2.3:def-cap give the radius reading and non-cap interpretation.
- 49697-49705: an unlabelled “separation statement for these cubes” supplies distance at least 8LMR_t−2M; the top clause then leaves block-size-conditions-b unchanged.
- 49707-49709: second-gauge-clause identifies filled islands; B-CMP122b supplies the unproved printed sentence that their configuration satisfies the induction hypothesis.
- 49711-49716: real-backgrounds, real-backgrounds-a, real-backgrounds-b and operator-theorem (I) identify the supply modification as outside theorem constants.
- 49722-49732: 2.2:not-hypotheses H2 fixes L_0(N) and L≥5; Theorem 0 gives running couplings; H3 and H4 fix gamma and gamma_H last.
- 49737-49741: Theorem 0 clause (0), 4.1:thm-clause-zero, supplies cube-sizes-a.
- 49751-49756: 2.2:not-hypotheses H5 fixes r; the later “lemma on the cube sizes” is assigned existence, positivity and monotonicity of check-R_j.
- 49758-49760: the convention replaces Bałaban's size R_j by check-R_j wherever it occurs.
- 49774-49779: 1.5:def-densities defines rho; terms, histories, regions, component meaning and creation set W-hat_t are assigned to later in this chapter.
- 49785-49789: not-cube-sizes defines waiting depth; the later action-level definition uses B-CMP122a p.176 condition (ii).
- 49812-49817: B-CMP122a p.176 is quoted for the preceding-step no-creation condition.
- 49827: not-cube-sizes supplies N_k=check-R_k≥1.
- 49829-49838: B-CMP122a and its (1.11) give the T_j indexing and renewed versus unchanged regions.
- 49840-49855: no-creation-a and -b identify the two windows; a structural creation statement is envisaged as the alternative route to k≥N_k.
- 49862-49866: later arguments and the later coarse partition are assigned the production of a cube inside both C and W-hat_t.
- 49868-49875: B-CMP122a p.176 supplies the rest of (ii); the later action-level definition adds (iii); ensuing arguments assume only no-creation.
- 49896-49900: torus-partitions-1 specifies common-origin partitions; B-CMP119 p.265 is the comparison for compatibility with all earlier partitions.
- 49906-49907, 49917-49928: torus-partitions supplies the finest partition and refinement; P', Q', R' and cube-test stage regions are introduced later.
- 49950-49955: torus-partitions and regions-components supply the subdivision lemma's hypotheses and definitions.
- 50029-50032: torus-partitions and regions-components supply the ambient objects for enlargement and boxing.
- 50041-50044: B-CMP119 pp.248,265 supplies the layer-enlargement/removal usage.
- 50048-50052: B-CMP119 bar-Z_k is identified with the coarse hull, with two allowed readings of “intersecting.”
- 50066-50071: the later boxing lemma is assigned cyclic intervals and connectivity; B-CMP119 (3.20) supplies the smallest-rectangle comparison.
- 50075-50080: B-CMP119 (3.20) supplies the 100-coarse-side smallness criterion; subdivision-independence makes components connected coarse regions.
- 50105-50108: clauses (d),(e) of the later boxing lemma are said to use only composition of replacement maps.
- 50115-50116, 50131-50132, 50139-50142: enlargement-hull-1 and -2 give iteration, stationarity and idempotence.
- 50145-50151: B-CMP119 (3.2)-(3.5), p.265 and (1.2),(1.4),(1.8),(1.10), pp.246-248, supply the general and first-step constructions; §§1 and 3 distinguish decompositions of unity.
- 50154-50161: torus-partitions, regions-components and enlargement-hull define cubes and layers; B-CMP119 §§1,3 identify coarse-cube conventions.
- 50163-50166: the history's precise incoming region Y is fixed later in the chapter, with Y empty at t=1 specified here.
- 50168-50175: Bałaban's bar-Z_k is identified with the hull; enlargement-hull supplies the two enlargement properties.
- 50188-50191: B-CMP119 (3.2) supplies the P_t decomposition and domain.
- 50192-50204: 1.5:def-block-average defines the level-t unit lattice; B-CMP119 §3 supplies B_t notation and axial-gauge domain, rewritten as small-field-complement-2.
- 50205-50219: B-CMP119 (3.3) supplies Q_t and (3.5) supplies Omega_t.
- 50221-50229: small-field-complement-2 and -1 rewrite B-CMP119 (3.5) as small-field-complement-a.
- 50231-50237: B-CMP119 (1.2),(1.4),(1.8),(1.10), pp.246-248, supplies first-step data, with (1.2) and (1.4) identifying P_0 and P_1.
- 50238-50250: the definition after B-CMP119 (1.4) is read as small-field-complement-3; the text explicitly says -3 is not a formula printed in that source.
- 50251-50256: B-CMP119 (1.8) supplies Q_1.
- 50257-50265: B-CMP119 (1.10) supplies Omega_1 and its associated first-step construction.
- 50267-50273: small-field-complement-3 and -1 rewrite B-CMP119 (1.10) as small-field-complement-b, conditionally on the adopted reading.
- 50294-50299: small-field-complement-a and -b instantiate -c, which is an input for later statements; the first-step case depends on -3.
- 50301-50309: small-field-complement-1 and -c give the cube-wise representation; -b explains why omitting P'_0 can fail.
- 50311-50313: B-CMP119 (3.2)-(3.5), p.265 and (1.2),(1.4),(1.8),(1.10), pp.246-248, identify all the corresponding named sets.

## Obligations named here

- 49090-49103: The operation-power pairing is asserted only at n≤k; no top-power bound of the same form is claimed at later levels n>k.
- 49121-49130: Hull-gauge use takes the printed family gauge as supplied, restricted to Q intersect Y_loc when the space has a localisation domain, and fixes C=1.
- 49237-49246: The second-gauge proposition assumes M≥13L²M_1-sharp and one of the nests covered by the admissibility lemma.
- 49279-49290: The operator theorem assumes the a-sharp ceiling; the displayed every-level bound is sufficient, and the converse is only asserted at levels represented by hulls.
- 49292-49293, 49344-49345: Lowest-level boxes require the separately supplied alpha-prime form of the second gauge clause.
- 49364-49368: To obtain the layerwise ceiling by this route, every level's coupling must satisfy the constructed smallness threshold.
- 49376-49384: History-uniform use assumes the small-coupling regime at each operation considered; part (d) assumes it for its specified operation.
- 49388-49390, 49488-49492: The operation-wide constant has no asserted uniform later-level pairing; uniformity over histories uses the layerwise constant.
- 49420-49429: B-CMP122a p.192 prints the logarithmic-contribution assertion without proof; this chunk supplies its stated layerwise form from the two power lemmas.
- 49495-49511: The expansion must verify real-backgrounds-b outside the operator theorem's implication, including background membership in a space carrying a displayed gauge clause at every index and the one-quarter epsilon_1 radius bound.
- 49513-49515: Reading representation-domain gauges globally on Q intersect Omega_0 requires the expansion's stated convention.
- 49517-49529: The expansion must allow C=1, either alone or together with C=2; C=2 alone need not fit the shell geometry.
- 49531-49541: Later spaces on drop-out components rest on B-CMP122a's unproved sentence about carrying B_k^(n) among boundary terms and generalising spaces for subsequent steps.
- 49543-49547: The expansion must fix which displayed family its drop-out space carries.
- 49549-49553: Lowest hulls use the supplied B-CMP99b (3.35) form at M_1-sharp.
- 49559-49563: The first-gauge ceiling must be read at M_1 c_1 R_n alpha_0,n in every layer.
- 49564-49574: Background inclusion radii must be read at c_1 R_n alpha_dot,n, as layerwise coupling conditions imposed after L and M.
- 49581-49587: Points (i)-(iv) remain conditions for the application to verify; the subsequent proof proves the assertions of (v), not the background inclusion obligations.
- 49663-49679: The space's available first-clause gauge has a power-weighted constant, so its ceiling must use the enlarged reading rather than the unweighted alpha_0,n.
- 49681-49687: Current and fluctuation radii also carry the power and require the enlarged reading at every affected layer.
- 49697-49705: The unchanged M-cube clause uses the separately named separation statement and the inclusion of all drop-outs and retained large fields in Z_k^post.
- 49707-49709: Filled-island use requires the assertion that the configuration satisfies the induction hypothesis, explicitly printed without proof in B-CMP122b.
- 49722-49741: Section 4.15 assumes the listed parameter conventions and cube-sizes-a from Theorem 0 clause (0); it imposes neither the listed upper bounds nor a lower coupling bound.
- 49754-49756: Existence, positivity and monotonicity of check-R_j are assigned to the later cube-size lemma, not proved in this excerpt.
- 49774-49779: Precise terms, histories, regions, components and creation sets are assigned to definitions later in the chapter.
- 49791-49808: An action must satisfy the no-creation clause in an adopted reading; the principal reading additionally requires k≥N_k.
- 49846-49855: Under the alternative reading, deriving k≥N_k needs a structural creation statement and requires testing all existing steps at early levels.
- 49857-49860: The automatically-true early-level formalisation is explicitly excluded, and no later conclusion is claimed under it.
- 49862-49866: Later creation arguments are announced to produce a common coarse cube; that production is not performed here.
- 49868-49875: The following arguments presuppose the no-creation clause only; other action conditions may be imposed as additional restrictions.
- 49885, 49896-49902: Cube sides must divide the torus period and the construction's partitions must be pairwise compatible; no additional fitting condition is assumed.
- 50066-50071: Cyclic-interval coordinate ranges and connectivity of boxes are assigned to the later boxing lemma.
- 50105-50108: The later boxing lemma's clauses (d),(e) are announced to use only composition of connected-superset replacement maps.
- 50163-50166: The input region along histories is fixed later; the first-step input is stipulated empty here.
- 50238-50250: The first-step axial-gauge complement formula is an adopted reading with nonnegative a_0,a_1, expressly not a printed formula of B-CMP119.
- 50281-50299: Later statements take small-field-complement-c as a hypothesis with finite generators inside P' union Q', nonnegative integer depths and the incoming hull; at t=1 this rests on the adopted first-step reading.
- 50305-50309: The first-step aggregate P' includes P'_0 as well as P'_1; the narrower choice P'=P'_1 can fail to support the claimed complement representation.

## For the stage question

No explicit complex-domain, analytic-ball, or minimiser statement occurs in these source lines. The chunk does discuss analyticity spaces, their localisation and radii, real-background admission, stage-space entries, carried drop-out boundary terms, and shell geometry. It does not establish complex-background admission by these real-background statements. No shell is explicitly called a “prepared shell” here.

| Lines | Stage-related statement | Status here |
|---|---|---|
| 49015-49018, 49090-49103 | A fixed operation's power/radius pairing is limited to its own levels and lower ones, not later layers of later nests. | proved conditionally |
| 49105-49107 | The adopted boxwise gauge constant reads the hull's own level and avoids cross-layer or cross-operation pairing. | definition |
| 49121-49130 | A member is read in an analyticity space; if that space has a localisation domain Y_loc, its supplied gauge is only on Q intersect Y_loc. | cited |
| 49135-49144, 49166-49189 | The hull bound and reg-sharp conclusion hold on the appropriate territory, intersected with Y_loc in the localised case. | proved conditionally |
| 49146-49158 | The per-operation constant dominates printed members and is bounded by the boxwise value at n≤k. | proved conditionally |
| 49238-49246 | Covered nests include hybrid drop-out stage nests both at the stage and at later T steps before a fill, and nests with filled islands. | assumed |
| 49252-49264 | Family membership includes old-nest indices and the stage-nest B-CMP122a (1.69)(iii) family, while a gauge is taken from the corresponding printed clause. | proved conditionally |
| 49265-49290 | These supplied gauges yield the common hull constant under the levelwise ceiling; this is conditional on the proposition's nest and gauge hypotheses. | proved conditionally |
| 49376-49382, 49448-49461 | A late nest may retain regions from several operations; applying each operation's power bound at the hull's own level gives a history-uniform layerwise ceiling. | proved conditionally |
| 49388-49390, 49482-49492 | Operation constants give the same conclusion through k, but no uniform cross-operation estimate is asserted for n>k. | proved conditionally |
| 49495-49511 | Admission of the expansion's real background into a space carrying a displayed clause at every index, with radii at most one-quarter epsilon_1, remains an application requirement outside the operator theorem. | assumed |
| 49513-49515 | The printed gauges live on Q intersect each representation domain X; their global reading on Q intersect Omega_0 is an expansion convention. | definition |
| 49517-49529 | C=1 must be allowed because a C=2 cube need not fit next to the one-M-ell_m-wide shell created by R near boundary Z''_m. | assumed |
| 49531-49533 | A drop-out is a component where preliminary integrations stop when a new large field is introduced. | definition |
| 49534-49541 | The source says to leave new B_k^(n) terms among all boundary terms and generalise spaces for next steps, but prints that assertion without proof. | named open |
| 49543-49547 | Existing hull-family and gauge-value results leave the expansion to choose which displayed family its drop-out space carries. | assumed |
| 49549-49553 | At hull levels zero and one, the second clause is supplied in the first admitted form at M_1-sharp. | assumed |
| 49555-49574 | Stage-nest first-clause ceilings and inclusion radii must be read with c_1 R_n, absorbing powers present in k_0<n≤k. | assumed |
| 49576-49582 | These requirements do not change the regularity clause on M-cubes, its a_Q ceiling, or operator-theorem clause (I), and are not part of the theorem's implication. | proved conditionally |
| 49585-49591 | The proof only establishes point (v); stages j≤k_0 have no power corrections and the (1.66),(1.67) conditions are void. | cited |
| 49593-49618 | The stage space controls seven quantities on stage and old-nest territories, including U_p,X, J_p,X, currents and fluctuation variables, with the displayed numerical factor, power and radius entries. | cited |
| 49620-49624 | The stage-space power multiplies every bracket entry, not just gauge clauses. | proved in detail |
| 49626-49642 | The radius index and exponent are tracked through stage, old-nest, and above-stage clauses, yielding 0≤e≤n−k_0≤N_0 in affected layers. | proved in detail |
| 49644-49661 | Either power lemma absorbs every such stage-space power into c_1 R_n. | proved conditionally |
| 49663-49679 | The only gauge supplied by the affected stage space for the first clause has the power-weighted constant; the enlarged ceiling reading covers all layers. | proved conditionally |
| 49681-49695 | Fluctuation and current bounds also carry the power, so inclusion radii use the same enlarged layerwise reading; these are one-sided coupling conditions. | proved conditionally |
| 49697-49705 | The post-operation large-field set contains every drop-out and retained large-field region; the separately supplied separation puts M-cubes outside it so only the zero-power top clause applies. | proved conditionally |
| 49707-49709 | On filled islands the required induction-hypothesis assertion is cited from B-CMP122b as printed without proof. | named open |
| 49711-49716 | The altered alpha_0 belongs to background supply, not to constants of the operator theorem. | proved in detail |
| 49769-49783 | An entering term's large-field component and creation history are used to define whether a creation lies inside it, with history details deferred. | definition |
| 49791-49808, 49819-49827 | An action must pass the adopted recent no-creation window, excluding current-stage creations; the alternative reading does not separately demand enough preceding steps. | definition |
| 49829-49838 | R renews levels h+1 through k produced by the last N_k one-step operations, leaving Z''_j=Z_j below that range. | cited |
| 49924-49928 | The region convention includes stage regions of the cube-test recursion introduced later. | definition |
| 50163-50166 | A step receives its entering term's large-field region, with the history-specific rule deferred and no incoming region at the first step. | definition |
| 50188-50229 | General-step domains are constructed from the incoming hull and new P_t,Q_t sets; Omega_t carries only small-field characteristic functions. | cited |
| 50238-50250 | The first-step gauge-fixing complement uses an explicitly adopted, unproved reading of the source definition. | assumed |
| 50257-50265 | Omega_1 is fixed during resummation over P_0,P_1,Q_1, has the stated distance from large fields and carries only small-field characteristic functions. | cited |
| 50281-50299 | Every step's complement is used downstream as a finite-union hypothesis, dependent on the adopted first-step reading when t=1. | assumed |

Deferred-proof rows marked “sketched” record assertions whose proof is assigned to a later lemma or argument, rather than supplied here; their targets are listed above. “Named open” records the explicitly unproved printed assertions. Conditional proof rows list their supplied hypotheses or prior results and do not assert that the expansion has verified those inputs.
