# Chunk 08: lines 51553-52851
Sections: Item 4.15, continuation on creation and post-action large-field regions (51553–52246); item 4.16, lowest-level regularity (52248–52851). No literal section or subsection heading occurs in this chunk; its titled environments are indexed below. The chunk begins and ends inside proofs.

| Lines | Name / tag | Kind | What it states (one plain sentence, your words) | Status here | Reads (inputs it uses, by tag or name) | Key phrase |
|---|---|---|---|---|---|---|
| 51553–51566 | First-action proof, concluding part (a) | proof | Combining the preceding inequalities gives k > checked R_k = N_k > N_0(k). | proved conditionally | 4.15:eq-level-inequalities-2; 4.15:lem-action-level; clause (0); assumed small-field complements; cube-size lemma (c) | "The only inputs used are" |
| 51564–51566 | Cube-size lemma (c) input | hypothesis | Part (c) concerning checked cube sizes and Bałaban's integer is used without reproving it. | assumed | Unnamed lemma on checked R_j and N_0, part (c) | "Part~(c) of that lemma is not re-proved here" |
| 51568–51585 | First-action proof (b), shifted attachment | proof | A first creation and monotonicity of checked cube sizes imply k′ > checked R_k′ at every acting index. | proved conditionally | 4.15:lem-action-level; 4.15:prop-pure-histories; waiting rule; shifted attachment | "The argument of" |
| 51587–51590 | Attachment convention | definition | An action is attached to the scale of its acted-upon region, including in the regime clause. | definition | B-CMP122a; checked R at k−N_0(k)+1 | "The attachment used in this section is the one of" |
| 51592–51594 | First-action proof (c), empty acting class | proof | No component is acted upon when 1 ≤ k ≤ checked R_k. | proved conditionally | 4.15:cor-first-action (a) | "By part~(a)" |
| 51596–51599 | Preparatory functions as new large fields | remark | Bałaban counts preparatory large-field functions as new fields violating condition (ii), unlike the T-step creation sets. | cited | B-CMP122a; condition (ii); 4.15:eq-creation-set-a | "regards the large-field functions introduced inside a component" |
| 51601–51607 | First-action proof (d), robustness to extra creations | proof | Counting preparatory fields as creations does not affect the action-level lemma because its waiting-rule argument only needs to bar T-step creations. | proved conditionally | 4.15:lem-waiting-rule; condition (ii); 4.15:lem-action-level | "both remain true if further sets are counted as creations" |
| 51609–51629 | 4.15:def-post-action-region — Top large-field region after actions | definition | For a produced term τ the post-action region is Λ_k(τ)^c, and the acted class includes components removed during preparation. | definition | 4.15:def-histories; B-CMP122a pp. 176–177; B-CMP122b p. 390; B-CMP119 p. 265 | "is the set" |
| 51630–51634 | 4.15:eq-post-action-region-a; residual S(X) | identity | The post-action region is the untouched region together with each acted component's intersection with the new region. | proved conditionally | Acted union Z; B-CMP122a (1.1), unchanged outside operation | "Together these give" |
| 51635–51649 | Proof of post-action decomposition | proof | Factorization leaves the outside unchanged and decomposes the inside into residuals. | proved conditionally | B-CMP122a (1.1); definition of S(X) | "To see this, recall that" |
| 51652–51659 | Whole-component condition | hypothesis | Every acted component is either wholly retained or wholly removed, while unacted components remain. | assumed | 4.15:eq-post-action-region-a | "is adopted where it is used and is not derived here" |
| 51660–51662 | Residual alternative | definition | The negation of the whole-component condition is the existence of a nonempty proper residual. | definition | S(X); terms σ′ and τ | "Its negation is recorded after it." |
| 51664–51675 | Equivalence of whole-component formulations | proof | Pairwise disjointness makes empty-or-whole residuals equivalent to retaining a collection of old components. | proved conditionally | 4.15:lem-component-properties (a); post-action-region-a | "The two formulations of the whole-component condition are equivalent." |
| 51677–51682 | No-action case | remark | With no acting components the term and region are unchanged and the whole-component condition is vacuous. | proved in detail | 4.15:def-histories; 4.15:eq-histories-c | "That identity is a consequence of the definitions" |
| 51685–51694 | Acting-class size and history requirements | requirement | An acted component fits a 100MR_k cube and has no new fields in its preceding N_k steps, with earlier regions satisfying their scale-specific cube conditions. | cited | B-CMP122a pp. 176–177 | "each component in the class" |
| 51696–51705 | Preparatory removals; final union Z^fin | construction | Preparatory large-field characteristic functions remove components from the working union, and Z^fin comprises those left. | definition | B-CMP122a §1; acted class A_k | "We write" |
| 51699–51702 | Treatment of preparatory drop-outs | remark | Bałaban says first-decomposition removals remain unchanged under subsequent operations, while later removals are merely stated to be removed. | cited | B-CMP122a §1 | "they are not changed by the subsequent operations" |
| 51707–51716 | New sequence Z″; N_0 and h | construction | The new sequence begins with the cited top two regions and is completed with admissible M-cube complements down to k−N_0+1. | cited | B-CMP122a (1.10)–(1.12) | "The two top members" |
| 51709–51710 | N_k > N_0 | hypothesis | The waiting length exceeds the least positive integer solving the displayed scale-size equation, and h is k−N_k. | assumed | Bałaban's N_0; M; R at k−N_0+1 | "it is assumed that" |
| 51718–51724 | 4.15:eq-post-action-region-b | definition | Lower new regions are enlarged-domain complements inside the acted union down to h+1, and equal the old regions below that. | definition | B-CMP122a (1.11); Ω_j; Z_j; h | "The remaining members are" |
| 51726–51728 | New domains and integration regions | construction | The cited construction defines Ω″, keeps its lower entries, and integrates variables in the differences between old and new large-field regions. | cited | B-CMP122a (1.12) | "New domains" |
| 51730–51740 | New determining set B_k and background U_k | construction | The determining set replaces its data on Z^fin by top-level data and defines the new background U_Bk(V). | cited | B-CMP122b (1.33)–(1.35), (1.71)–(1.72) | "a new determining set" |
| 51742–51750 | First-class components and reversed Faddeev–Popov operation | construction | Small-field components lose trivial characteristic functions and their gauge-fixing delta functions after integration over V_k. | cited | B-CMP122b (1.71)–(1.72); χ_k; V_k integration | "this is possible only because" |
| 51749–51750 | Equivalence rather than equality of densities | remark | Removing first-class gauge-fixing deltas gives an equivalent density rather than an identical one. | cited | B-CMP122b (1.71)–(1.72) | "is equivalent, but not equal" |
| 51751–51755 | Second-class components | construction | Large-field components retain earlier characteristic and gauge-fixing factors and are included again in the new large-field domain. | cited | B-CMP122b (1.71)–(1.72) | "they are included again" |
| 51756–51766 | Top-integrated T′_k(X) and first-class passage to Ω_k | remark | Both classes admit a localized top-integrated operation, while first-class components pass into the new determining domain without thereby fixing their next large-field membership. | cited | B-CMP122b (1.33), (1.71), (1.72), §1 | "does not by itself say what becomes of a first-class component" |
| 51768–51781 | Two readings of the new top set | construction | The cited new-region sentence can use either the unchanged outside region or the new top region Z″_k. | definition | B-CMP122b sentence after (1.101); B-CMP122a pp. 176–177 | "are compatible with two readings" |
| 51785–51793 | 4.15:eq-post-action-region-c | identity | The first reading removes precisely first-class components, whereas the second also retains Z″_k. | proved conditionally | First and second readings; disjoint first/second classes in Z^fin | "Under the two readings" |
| 51794–51807 | Consequences of the two readings | proof | The first reading gives whole residuals, and the second does so when Z″_k equals the acted union but can otherwise give proper first-class residuals. | proved conditionally | post-action-region-c; Z″_k = Z or proper-intersection alternatives | "The whole-component condition therefore holds under the first reading." |
| 51808–51810 | Shell residual and unresolved top set | remark | The cited sentences neither make characteristic functions delimit shells nor settle whether Z″_k equals the acted union. | named open | B-CMP122a and B-CMP122b sentences above; χ_k and χ_k^c | "is not settled by these sentences" |
| 51812–51833 | Operator description does not fix the post-action region | remark | Integration, reference density, live factors and class division permit a retained whole component, a whole exit, or a proper core or shell. | named open | 1.5:def-densities; B-CMP122b (1.71) | "does not fix" |
| 51835–51842 | Hypothesis status of whole-component reading | hypothesis | The book explicitly assumes the whole-component reading wherever it is used and excludes proper residuals there. | assumed | B-CMP122a §1, (1.1), (1.10)–(1.12); B-CMP122b (1.33)–(1.35), (1.71)–(1.72), after (1.101) | "It enters this book as a hypothesis." |
| 51845–51883 | 4.15:prop-creation-cube — Every top component contains a creation cube | proposition | Every pre-action and post-action top component contains a whole earlier coarse creation cube. | proved conditionally | Hypotheses (a) small-field complement and (b) whole-component condition; 4.15:def-histories; one-step-components (b); component-properties (f) | "Assume the following two hypotheses." |
| 51849–51853 | Creation-cube hypothesis (a) | hypothesis | Every step's small-field complement has the specified union-of-enlargements description. | assumed | 4.15:def-small-field-complement; 4.15:eq-small-field-complement-c | "Assume the following two hypotheses." |
| 51854–51860 | Creation-cube hypothesis (b) | hypothesis | Every level's post-action residual is empty or whole and unacted components remain. | assumed | 4.15:def-post-action-region; post-action-region-a | "every residual" |
| 51885–51888 | Pure-history special case | remark | Through the first acting level the earlier pure-history proposition supplies the corresponding creation conclusion with hypothesis (a) alone. | proved conditionally | 4.15:prop-pure-histories; hypothesis (a) | "which assumes hypothesis~(a) only" |
| 51890–51950 | Creation-cube induction | proof | One-step components inherit an earlier cube or contain a new cube, and whole-component retention transfers this to the post-action region. | proved conditionally | Hypotheses (a), (b); 4.15:def-histories; B-CMP119 p. 265; one-step-components (b); component-properties (f) | "the induction is complete" |
| 51952–51958 | Proper-residual limitation of creation theorem | requirement | Creation-cube persistence is not proved when an action can leave a nonempty proper residual. | named open | 4.15:prop-creation-cube; alternative in 4.15:def-post-action-region | "it is not proved" |
| 51960–52003 | 4.15:rem-proper-residual — Case of a proper residual | remark | A proper residual prevents a union-of-whole-components argument and need not be connected. | proved conditionally | Existence of proper S(X); component-properties (a), (f) | "Suppose instead" |
| 51978–51983 | Residual creation obligations | requirement | Both retention of a creation cube in S(X) and retention in each of its components would need proof. | named open | 4.15:prop-creation-cube; P_s; W_s | "two things would have to be shown" |
| 51985–51999 | Top versus lower-region formula | remark | The cited formula only controls j ≤ k−N_0, leaving the top residual componentwise creation claim to prove. | named open | B-CMP122a (1.10), (1.11); B-CMP122b after (1.101); 4.15:def-post-action-region | "the statement to be proved is" |
| 52001–52002 | T-only creation unaffected | remark | The alternative post-action description does not affect the creation statement for renormalization steps alone. | proved in detail | Absence of R-steps | "since no" |
| 52005–52020 | Proof of proper-residual remark (a), (b) | proof | Disjointness rules out a whole-component union and connectedness of a set does not ensure connectedness of its proper subset. | proved conditionally | Proper-residual assumption; 4.15:lem-component-properties (a), (f) | "Both alternatives contradict the assumption" |
| 52022–52042 | 4.15:rem-top-scale-scope — Creation concerns top-scale regions only | remark | The creation proposition excludes new lower regions and condition (ii), and needs the post-action reading only from the first action onward. | proved conditionally | 4.15:prop-creation-cube; pure-histories; post-action-region; cor-first-action | "It claims nothing about the lower regions" |
| 52044–52078 | Top-scale-scope proof (a) | proof | Lower new regions are contained in old ones and none of the structural or waiting assertions requires them to retain creation cubes. | proved conditionally | B-CMP122a (1.11), §1 before (1.10), condition (ii); admissible domains; post-action-region-b | "The definition does not require" |
| 52080–52082 | Top-scale-scope proof (b) | proof | The creation-cube proposition does not refer to condition (ii), so preparatory-field counting is irrelevant to it. | proved in detail | 4.15:prop-creation-cube | "makes no reference to condition~(ii)" |
| 52084–52107 | Top-scale-scope proof (c) | proof | Histories are pure before their first action, and post-action region choices become substantive at that first action. | proved conditionally | 4.15:cor-first-action (b); 4.15:prop-pure-histories; 4.15:def-post-action-region | "enters at the first action" |
| 52109–52120 | 4.15:rem-not-asserted (1), truncated-window convention | remark | A convention automatically satisfying no-creation for k < N_k would not imply the action-level bound. | proved conditionally | Hypothetical convention; 4.15:def-no-creation; other action conditions | "is not derivable" |
| 52121–52126 | Not-asserted (2), action existence and indices | remark | No action existence or bounds on stopping, stabilization, waiting, N_0 or first-action indices are asserted. | named open | n_*; q_0; N_0(k); N_k; creation-set-a | "none of these numbers is bounded" |
| 52127–52132 | Not-asserted (3), residual and lower-region scope | remark | The creation proposition is not asserted for competing post-action regions or new lower entries. | named open | 4.15:def-post-action-region; 4.15:prop-creation-cube; Z″_j | "is not asserted" |
| 52133–52138 | Not-asserted (4), operator-to-region identification | remark | The density description does not supply the assumed region read by the next T-step. | named open | 1.5:def-densities; 4.15:def-post-action-region; creation-cube | "is an assumption there and is not derived" |
| 52139–52144 | Not-asserted (5), intermediate persistence | remark | Finding a creation cube in a component does not assert that it stayed in every intermediate top region. | named open | 4.15:prop-creation-cube | "It is not asserted" |
| 52145–52150 | Not-asserted (6), analytic scope | remark | This section establishes no analytic claims about R, denominators, reference law, operator theorem or clause (i). | named open | B-CMP122b (1.79)–(1.89); Theorem 0; unnamed N_0 remark and cube-size lemma (c) | "Nothing is asserted about the analytic content" |
| 52151–52154 | Not-asserted (7), enlargement counts and L_0 | remark | The argument uses arbitrary nonnegative enlargement counts and no value of L_0. | proved in detail | small-field-complement-a, -b; def-small-field-complement | "No value of the constant" |
| 52155–52162 | Not-asserted (8), omission of initial P_0 | remark | Choosing P′ = P′_1 alone prevents this argument from deriving either creation-cube or action-level conclusions. | proved conditionally | Narrower P′; B-CMP119 (1.2), (1.4); creation-set-a | "neither" |
| 52166–52182 | Not-asserted proof (1) | proof | The actual two no-creation formulations do not hold automatically for short histories, whereas the hypothetical one permits the prohibited action. | proved conditionally | 4.15:def-no-creation; other two action conditions | "cannot be derived" |
| 52184–52196 | Not-asserted proof (5) | proof | The ancestor chain gives containment in the final component without providing an ancestor at every intermediate top level. | proved in detail | Proofs of action-level and creation-cube; def-no-creation | "these inclusions therefore do not give" |
| 52198–52246 | Not-asserted proof (8) | proof | Omitting P′_0 loses the required first-step complement representation and can leave creation-free descendants allowed to act at k = checked R_k. | proved conditionally | Narrower P′; P_0 nonempty; hypothetical descendant; B-CMP119 (1.2), (1.4); small-field-complement-b; def-no-creation | "Hence neither" |
| 52242–52245 | Required first-step P′ convention | hypothesis | The assumed complement description includes P′_0 together with P′_1. | assumed | 4.15:def-small-field-complement; small-field-complement-b; action-level; creation-cube | "That choice is part of the statement assumed" |
| 52248–52298 | 4.16:rem-lowest-levels — Two lowest tower levels | remark | Two printed regularity conditions are carried as a datum clause supporting the operator theorem and Theorem 0. | assumed | B-CMP99b p. 396 (3.35), (3.37); 4.5:def-admissible-pairs; 4.1:thm-clause-zero | "printed without proof" |
| 52253–52260 | B-CMP99b (3.35), quoted regularity class | definition | A configuration admits a gauge potential on each class cube with scale-dependent potential and derivative bounds. | definition | B-CMP99b p. 396; that paper's cube class and notation | "These two sentences are definitions of regularity classes" |
| 52261–52275 | B-CMP99b (3.37), quoted perturbation class | definition | A configuration satisfying (3.35) has a perturbation potential and covariant derivative bounded on each Ω_j. | definition | B-CMP99b p. 396 (3.35), (3.37) | "These two sentences are definitions of regularity classes" |
| 52277–52284 | Carried lowest-level clause (i) | requirement | The real configuration satisfies (3.35) on the level-zero and level-one boxes meeting Z. | assumed | B-CMP99b (3.35); datum U′U | "what this book carries as printed" |
| 52285–52293 | Carried lowest-level clause (ii) | requirement | A′ and the accompanying current J satisfy the specified level-zero radii used in operator-domain admission. | assumed | B-CMP99b (3.37); 4.5:def-admissible-pairs; operator theorem at free current | "it is also an input" |
| 52300–52313 | 4.16:def-fine-positions — Fine sites, bonds and plaquettes | definition | Fine sites are cell centers, bonds are closed neighboring-site segments positioned at their midpoints, and plaquettes are positioned at their centers. | definition | η; ℓ_n; 4.14:not-free-current-notation; B-CMP109 | "The" |
| 52306–52308 | Fine-site boundary exclusion | remark | Nested standard partitions put every fine site off every standard-cube boundary. | proved in detail | Fine sites as cell centers; nested partitions | "Hence no fine site lies on the boundary" |
| 52314–52320 | Pairs; 4.16:eq-fine-positions-1 | definition | Parallel nearest-neighbor bonds, including collinear ones, carry the plain difference quotient η⁻¹(A(b′)−A(b)). | definition | Fine bonds; field A | "The collinear pair" |
| 52321–52326 | 4.16:eq-fine-positions-2 | definition | The position of a bond pair is the midpoint of its bond midpoints. | definition | x_b; x_b′ | "position" |
| 52327–52328 | Independence of later estimates from pair convention | remark | Later arguments explain why collinear pairs and this position convention do not affect their estimates. | sketched | Later pair estimates in this chapter, unnamed | "the reason is given where those estimates are made" |
| 52330–52336 | Carried indices, site maps; 4.16:eq-fine-positions-3 | definition | A closed set carries whole bonds and pairs, and a site map on their endpoints acts by the displayed gauge transformation. | definition | Closed S; fine bond endpoints; G | "we set" |
| 52338–52359 | Reading (W); 4.16:eq-fine-positions-a | definition | Weighted regularity tests every carried index at its position in each shell, imposing both bounds on shell overlaps. | definition | Carried bonds and pairs; X_n; ℓ_n | "Such a clause is read index by index." |
| 52362–52376 | 4.16:def-data-region — Data region and real operator space | definition | The closed data region carries the real configurations satisfying (u1), (reg) and (reg)^sharp for the operator theorem. | definition | 4.14:not-free-current-notation; 4.16:def-fine-positions; operator theorem at free current | "this region" |
| 52378–52385 | Hull condition (col); 4.16:eq-data-region-b | requirement | The two-fine-spacing enlargement of the perturbation hull Ω_0 lies inside the data region. | assumed | Base S; B ⊆ B-hat; Ω_0 | "This hull satisfies" |
| 52387–52397 | Box family D^sharp; data-region-1 and data-region-2 | definition | At level j the lattice spacing s_j is M_1^sharp ℓ_j and the enlarged box has half-side 5s_j. | definition | Shell X_j; lattice s_j Z^d | "put" |
| 52398–52414 | Box regularity (reg)^sharp; 4.16:eq-data-region-a | requirement | Each enlarged box has a gauge potential on its data-region intersection satisfying weighted bounds on every shell it meets. | assumed | Operator theorem at free current; (W); D^sharp; data region | "condition" |
| 52409–52413 | Shell convention for operator regularity | hypothesis | The operator clause uses at most two adjacent shells and includes the entire level-zero shell. | assumed | Operator theorem at free current; 4.14:not-free-current-notation | "there are at most two such shells" |
| 52416–52420 | Regularity ceiling and derivative convention | requirement | The regularity radius obeys the operator theorem's ceilings and its derivative is the plain neighboring-bond quotient. | assumed | Operator theorem at free current; a_reg^oplus; B-CMP99b (3.35) | "It is subject to the ceilings imposed on it there" |
| 52425–52429 | 4.16:eq-data-region-3 | identity | Nesting and (col) place Ω_1 and Ω_0 inside the data region. | proved conditionally | Decreasing nest; (col) | "therefore gives" |
| 52431–52435 | Perturbation bonds carried by data region | proof | The two-spacing locality of perturbation bonds and (col) ensure that U is defined on both bond sets. | proved conditionally | Bond locality within 2η of S; S ⊆ Ω_0; (col) | "Hence" |
| 52437–52444 | Meaning and possible enlargement of square^4 | remark | The chosen enlargement has half-side 5s_j, and the text says a half-side 9s_j interpretation preserves subsequent inclusions and fitting under the same floor. | sketched | Operator theorem convention; B-CMP109 enlargement convention; later cube fitting | "would still hold under the same one-sided floor" |
| 52446–52456 | 4.16:def-cube-class (i), big blocks | definition | A level-j big block is a standard M_1ℓ_j cube, translating Bałaban's block size M into M_1. | definition | 4.16:def-data-region; B-CMP99b §3 | "A" |
| 52457–52462 | Cube-class (ii), aligned N-block cubes | definition | An aligned cube is a union of N^d big blocks, with class cubes using N ≥ 10 and a cited possible choice N = 12. | definition | B-CMP99b §3, (3.35) | "an aligned" |
| 52463–52470 | Cube-class (iii); 4.16:eq-cube-class-a | definition | C_j consists of aligned cubes with 10 ≤ N ≤ N^sharp = 4M_1^sharp/M_1, lying in two adjacent shells and meeting X_j. | definition | Big blocks; shells | "bounded sub-class at level" |
| 52471–52496 | Cube-class (iv), Bałaban class and class hull | definition | The translated class uses its own closed level-zero hull and index-j regions to specify eligible aligned cubes. | definition | B-CMP99b §3; 0.2:not-glossary for distinct R; 4.16:def-data-region | "call it the" |
| 52486–52491 | 4.16:eq-cube-class-1 | identity | The index-zero class region is the closure of the class hull minus Ω_1, while positive index regions are the shells. | definition | B-CMP99b §3; translated B^i(Λ_i) | "in the translation used in this book" |
| 52500–52503 | Cube-class property (a) | remark | N^sharp is integral and the bounded range includes twelve once M_1^sharp ≥ 3M_1. | proved in detail | Block sizes powers of L; divisibility | "These objects have the following properties." |
| 52504–52505 | Cube-class property (b) | remark | Every bounded-size Bałaban cube at index one belongs to C_1. | proved in detail | cube-class-1; cube-class-a | "belongs to" |
| 52506–52508 | Cube-class property (c) | remark | Every bounded-size Bałaban cube at index zero belongs to C_0 and the class hull, although C_0 itself imposes no hull condition. | proved conditionally | (A1) of 4.14:prop-prepared-data-admissible; nested partitions; cube-class definitions | "Membership" |
| 52509–52512 | Cube-class property (d), fixed twelve-block reading | remark | Under the twelve-block reading and F2 the bounded subclasses contain the entire Bałaban classes at indices zero and one. | proved conditionally | Twelve-block reading; lowest-level-regularity-b (F2); properties (a)–(c) | "Suppose" |
| 52513–52527 | Cube-class property (e); 4.16:eq-cube-class-2 | estimate | Bałaban's real gauge bounds translate to fixed index-j weights with ceiling NM_1α_0 over the whole cube. | proved conditionally | B-CMP99b (3.35), §3; U^u = exp(iηA); ℓ_j = L^jη | "this bound is the pair of bounds" |
| 52525–52527 | No class regularity outside class hull | remark | The cited regularity conditions impose no restrictions on U outside the class hull. | cited | B-CMP99b §3 | "do not impose any constraints" |
| 52531–52536 | Cube-class proof (a) | proof | Divisibility and powers of L give integrality and the threshold for including twelve. | proved in detail | Definitions of M_1, M_1^sharp and N^sharp | "Hence" |
| 52538–52547 | Cube-class proof (b) | proof | The translated index-one region and block bounds give exactly the defining conditions of C_1. | proved in detail | cube-class-1; cube-class-a | "These are the conditions" |
| 52549–52586 | Cube-class proof (c) | proof | Three hull and shell inclusions place bounded index-zero class cubes in both C_0 and the class hull. | proved conditionally | (A1); closed finite block unions; nested partitions; M_1 divides M | "We first record three inclusions." |
| 52588–52591 | Cube-class proof (d) | proof | Fixing twelve blocks and applying F2 reduces whole-class inclusion to the previous cases. | proved conditionally | Twelve-block reading; F2; properties (a)–(c) | "Under this reading" |
| 52593–52600 | Cube-class proof (e) | proof | Substitution of the scale and block-size notation yields the fixed-weight regularity inequalities. | proved conditionally | B-CMP99b (3.35); ℓ_j = L^jη; NM_1 size translation | "Multiplying the first" |
| 52602–52609 | Bounded-size fitting and exclusion of larger cubes | remark | Only cubes bounded by N^sharp are placed in one regularity box, and larger cubes receive no gauge-gluing treatment here. | named open | 4.16:eq-cube-fitting-a; (reg)^sharp; unrestricted Bałaban O(1) reading | "no gluing of the gauges of several boxes is attempted" |
| 52611–52618 | Ten-block applications to hats | construction | Hats fit into ten-block cubes in the supremum proof, and the analogous condition for their part in Z is proposed to follow the same way. | sketched | F2; supremum proposition (b); definition of class of hats | "would be obtained in the same way" |
| 52620–52647 | 4.16:def-weighted-norm; 4.16:eq-weighted-norm-a | definition | The complex perturbation-current norm takes the maximum of three suprema weighted by ℓ, ℓ² and ℓ³ and their operator radii. | definition | Complexified Lie algebra; 4.16:def-data-region; B-CMP99b (3.37); a_1^oplus, a_0^oplus; fine positions | "weighted norm" |
| 52636–52647 | Pointwise index weight and radius range | definition | Each index uses the least shell scale at its position, with the specified bond and pair ranges and 0 < r ≤ 1. | definition | X_n; fine-positions; A′ and J domains | "the least" |
| 52649–52655 | Layered-norm variant | remark | Imposing level-n weights on all Ω_n is stronger at boundaries and yields the later regularity bounds without powers of L. | sketched | B-CMP99b (3.37); weighted-norm-a; subsequent clause (b) | "holds under it a fortiori" |
| 52658–52668 | 4.16:def-tiles — Tiles and unions of tiles | definition | Tiles are standard closed level-k LM-cubes used by the next correlation expansion, and Z is any closed union of them. | definition | 4.16:def-data-region; correlation theorem at step k+1 | "A" |
| 52670–52794 | 4.16:prop-lowest-level-regularity — Initial-data regularity | proposition | Specified admissibility and regularity assumptions give real gauge bounds on bounded lowest-level cubes and weighted complex perturbation-current bounds. | sketched | (A1); divisibility and torus size; (col); F1, F2, F2^sharp; (reg)^sharp; norm < r; tile union Z | "We first establish two facts" |
| 52676–52684 | Lowest-level proposition geometric hypotheses | hypothesis | The nest is admissible, block sizes divide, the torus side is a multiple of LM, and (col) supplies the required domain inclusions. | assumed | 4.14:prop-prepared-data-admissible (A1); 4.16:eq-data-region-b; weighted-norm definition | "Assume the following." |
| 52685–52693 | F1; 4.16:eq-lowest-level-regularity-a | requirement | The large block size obeys M ≥ 13L²M_1^sharp. | assumed | Operator theorem at free current | "The floors" |
| 52689–52693 | F2; 4.16:eq-lowest-level-regularity-b | requirement | The intermediate block size obeys M_1^sharp ≥ 3M_1. | assumed | Block parameter order | "hold" |
| 52694–52703 | Consequences and uses of F1 and F2 | remark | The floors imply the three smaller size inequalities, strict separation of block parameters, and admission of ten- and twelve-block cubes. | proved conditionally | F1, F2; odd L ≥ 3; powers-of-L sizes | "each of these three inequalities follows" |
| 52704–52714 | F2^sharp and seam-enlarged cubes | requirement | The additional floor M_1^sharp ≥ 5LM_1 supplies N^sharp ≥ 20L for a later seam class but is unused by clauses (a), (b) and the two facts. | assumed | Later seam-enlarged corollary; lower-seam threshold 3LM_1 | "In addition, the floor" |
| 52715–52716 | Whether existing operator floors imply F2^sharp | requirement | Implication of F2^sharp by the operator theorem's floors is not asserted because a relevant constant is unevaluated. | named open | Operator theorem at free current; unevaluated constant | "is not asserted here" |
| 52717–52723 | Lowest-level proposition field and tile hypotheses | hypothesis | U satisfies box regularity on all indicated shells, the complex pair has norm below r, and Z is a tile union with j zero or one. | assumed | (reg)^sharp; (W); supremum proposition (a); weighted-norm-a; def-tiles | "satisfies" |
| 52728–52742 | Lowest-level clause (a); 4.16:eq-lowest-level-regularity-c | estimate | Restricting a single regularity-box gauge to a class cube's data-region and Z intersection gives the real field and derivative bounds. | sketched | Proposition hypotheses; cube fitting; (reg)^sharp; B-CMP99b (3.35) | "For every" |
| 52744–52750 | 4.16:eq-lowest-level-regularity-1 | estimate | The gauge bounds improve to the next-shell scale where applicable and hold everywhere with the pointwise scale. | sketched | (W); clause (a); pointwise ℓ | "The bound can be sharpened." |
| 52752–52758 | Removal of data-region restriction | remark | Index-one class cubes automatically lie in the data region, and index-zero Bałaban cubes do if the class hull is included there. | proved conditionally | X_1 ∪ X_2 ⊆ Ω_1; (col); class-hull inclusion at index zero | "because" |
| 52761–52766 | Boundary exponent q_j | definition | q_j is one only for j = 1 at positions in X_0, identifying the boundary of Ω_1 within Ω_1. | definition | X_0; Ω_1; fine-index positions | "Put" |
| 52767–52773 | 4.16:eq-lowest-level-regularity-d | estimate | The complex perturbation, its covariant derivative and current have lowest-level bounds with possible boundary losses L, L² and L³. | sketched | Norm < r; q_j; ℓ_j; a_1^oplus, a_0^oplus | "The powers of" |
| 52774–52780 | Location and absence of boundary losses | remark | Losses occur only at level-one boundary-positioned crossing indices and vanish for indices carried by Ω_j or at level zero. | sketched | Fine bond and pair geometry; q_j; lowest-level-regularity-d | "only at" |
| 52782–52791 | Translation to (3.37) and separate current bound | remark | Clause (b) supplies α_1 = L²ra_1^oplus, improves it on carried indices, and adds a current bound absent from B-CMP99b. | proved conditionally | Clause (b); B-CMP99b (3.37); B-CMP109 (1.14); L ≤ L² | "Clause~(b) is this bound" |
| 52793–52794 | Larger class cubes excluded | remark | No conclusion is asserted for cubes exceeding N^sharp blocks per side. | named open | Bounded class C_j | "Nothing is asserted here" |
| 52796–52851 | Proof of lowest-level proposition: two facts, partial | proof | The proof establishes the shell partition fact and begins the adjacent-shell box argument before the chunk ends. | sketched | (A1); nested partitions; F1; divisibility; torus size | "We first establish two facts" |
| 52800–52805 | Fact (i); 4.16:eq-lowest-level-regularity-e | identity | Every shell is a union of standard cubes of side s_j. | proved conditionally | (A1); M_1^sharp divides M; shell definitions | "This proves" |
| 52806–52813 | Proof of Fact (i) | proof | Subdividing the shell's M-cubes, or level-zero LM-cubes, yields its s_j-cubes. | proved conditionally | 4.14:prop-prepared-data-admissible (A1); nested standard partitions | "This proves" |
| 52816–52821 | Fact (ii); 4.16:eq-lowest-level-regularity-f | estimate | An enlarged box centered in a lowest-level shell meets that shell and at most one adjacent shell. | sketched | (A1); F1; box definition; j ∈ {0,1} | "The case" |
| 52823–52830 | Fact (ii), nonwrapping box size | proof | F1 makes the box diameter smaller than M and thus smaller than the torus side. | proved conditionally | F1; ℓ_j ≤ 1; torus side multiple of LM | "So" |
| 52832–52846 | Fact (ii), j = 0 case | proof | Admissible separation keeps the box out of Ω_2 and therefore out of all shells of index at least two. | proved conditionally | (A1) at n = 1; F1; closed nested domains; k = 1 trivial case | "Hence" |
| 52848–52851 | Fact (ii), j = 1 case, beginning only | proof | The argument disposes of k = 1 and starts the k ≥ 2 case by placing the center in the closure of Ω_2's complement. | sketched | X_1 definition; k ≥ 2 | "Let" |

## Forward and backward references

References within the chunk are included as well as references outside it; repeated occurrences are retained below in source order. Bibliographic keys are reported exactly as supplied, without inferring titles. “Later” and “earlier” identify the source's direction of reference, not material consulted for this index.

- 51553–51559: `4.15:eq-level-inequalities-2` (existence and combination, twice) and `4.15:eq-level-inequalities-1` (conclusion).
- 51561–51566: `4.15:lem-action-level` (twice), its clause (0) and assumed complement description; unnamed lemma on checked cube sizes and Bałaban's N_0, part (c), explicitly not reproved and not an input to the action-level lemma.
- 51568–51574: `4.15:lem-action-level`, `4.15:prop-pure-histories`, and waiting rule in shifted form.
- 51587–51590: B-CMP122a attachment convention and the regime clause's use of N_0(k).
- 51592–51594: `4.15:cor-first-action` (a).
- 51596–51599: B-CMP122a condition (ii) for preparatory fields; `4.15:eq-creation-set-a` for T-step creations.
- 51601–51606: `4.15:lem-action-level` (twice) and `4.15:lem-waiting-rule`; condition (ii) as the waiting proof's input.
- 51609–51628: B-CMP122b p. 390 for post-action region; `4.15:def-histories` for the acting class; B-CMP122a pp. 176–177 for the union Z; B-CMP119 p. 265 for the region read next.
- 51635–51649: B-CMP122a (1.1), factorization and unchanged outside operation; `4.15:eq-post-action-region-a`, derived here.
- 51655–51659: `4.15:eq-post-action-region-a`, residuals used in the whole-component hypothesis.
- 51664–51675: `4.15:lem-component-properties` (a) and `4.15:eq-post-action-region-a`, equivalence proof.
- 51677–51682: `4.15:eq-post-action-region-a`, `4.15:eq-histories-c`, and `4.15:def-histories`, no-action identity.
- 51685–51694: B-CMP122a pp. 176–177 (twice), acting-class conditions and R_k meaning.
- 51696–51705: B-CMP122a §1, preparatory decompositions, removals and unchanged first drop-outs.
- 51707–51724: B-CMP122a (1.10)–(1.12), new sequence; (1.10) for its top two members; remaining members recorded as `4.15:eq-post-action-region-b`.
- 51726–51728: B-CMP122a (1.12), new Ω″ and integration variables.
- 51730–51740: B-CMP122b (1.33)–(1.35), determining set and background; (1.71)–(1.72), class decomposition.
- 51742–51755: The same B-CMP122b class decomposition supplies first-class integration and delta removal, density equivalence, and second-class reinclusion.
- 51757–51766: B-CMP122b (1.71), localized top-integrated operation; (1.72), R and new Ω_k; (1.33), first-class passage into Γ_k; §1, next-step joining of components.
- 51768–51781: B-CMP122b sentence after (1.101), p. 390; B-CMP122a pp. 176–177, convention suppressing some intersections; new Z″_k sequence for the second reading.
- 51808–51810: The previously cited sentences are explicitly insufficient to decide shell delimitation or Z″_k = Z.
- 51812–51824: `1.5:def-densities`, operator outline; B-CMP122b (1.71), top-integrated operation and region sum.
- 51835–51842: B-CMP122b sentence after (1.101), p. 390; B-CMP122a §1, (1.1), (1.10)–(1.12), pp. 176–179; B-CMP122b (1.33)–(1.35), (1.71)–(1.72); all later uses in the book are said to list the whole-component hypothesis explicitly.
- 51849–51860: `4.15:def-small-field-complement` and `4.15:eq-small-field-complement-c` supply hypothesis (a); `4.15:def-post-action-region` and `4.15:eq-post-action-region-a` supply hypothesis (b).
- 51862–51874: `4.15:def-histories` (twice), history and action attachment; B-CMP119 p. 265, incoming post-action region.
- 51885–51888: `4.15:prop-creation-cube` and `4.15:prop-pure-histories`, identification of the pure-history special case and its sole complement hypothesis.
- 51890–51909: `4.15:def-histories` at 51893 and 51908; B-CMP119 p. 265, induction's incoming region.
- 51911–51917: `4.15:prop-one-step-components` (b), component-or-new-cube alternative under hypothesis (a).
- 51931–51941: Hypothesis (b) of the current proposition; `4.15:lem-component-properties` (f), retained components.
- 51952–51958: Hypotheses (a), (b); `4.15:def-post-action-region`, alternative for which the conclusion is unproved.
- 51969–51983: `4.15:def-post-action-region`; `4.15:lem-component-properties` (f); `4.15:prop-creation-cube` at 51978 and 51983, persistence obligations.
- 51985–51999: B-CMP122a (1.10), p. 179; B-CMP122b (1.101) and following sentence, p. 390; B-CMP122a (1.11), p. 179; `4.15:def-post-action-region` and `4.15:prop-creation-cube`, conditional reuse of proof.
- 52005–52019: `4.15:lem-component-properties` (a) at 52008 and 52017, and (f) at 52013, residual proof.
- 52022–52040: `4.15:prop-creation-cube` at 52023, 52031, 52032 and 52036; `4.15:eq-post-action-region-b`, lower regions; B-CMP122a condition (ii); `4.15:cor-first-action`; `4.15:prop-pure-histories`; `4.15:def-post-action-region`.
- 52045–52062: B-CMP122a (1.11), lower-region definition; §1 before (1.10), smaller-region purpose; `4.15:prop-creation-cube`, creation cubes in X.
- 52064–52078: `4.15:prop-creation-cube` at 52064, 52077; structural top-component statement, waiting rule, regime clause, and B-CMP122a condition (ii)'s size condition (i).
- 52080–52082: `4.15:prop-creation-cube`; this chapter's remark on preparatory large fields.
- 52084–52107: `4.15:cor-first-action` (b) at 52087 and 52096; `4.15:prop-pure-histories` at 52089; `4.15:prop-creation-cube` at 52095; `4.15:def-post-action-region` at 52100 and 52105.
- 52113–52120: `4.15:def-no-creation`, `4.15:lem-action-level`, and `4.15:eq-action-level-a`, nonderivability under the alternative automatic rule.
- 52121–52126: `4.15:eq-creation-set-a`, recursion stopping stage; modification map stabilization index q_0 and Bałaban's N_0(k), all without bounds here.
- 52127–52138: `4.15:prop-creation-cube` at 52127 and 52138; `4.15:def-post-action-region` at 52128 and 52137; `1.5:def-densities` at 52134; Bałaban's lower new sequence.
- 52139–52150: `4.15:prop-creation-cube`; B-CMP122b (1.79)–(1.89); operator theorem at free current; Theorem 0 (i); this section's N_0 remark and the unnamed lemma (c) on which it rests.
- 52151–52162: `4.15:eq-small-field-complement-a`, `-b`; `4.15:def-small-field-complement` at 52153 and 52156; `4.15:eq-creation-set-a`; `4.15:prop-creation-cube`; `4.15:eq-action-level-a`; B-CMP119 (1.4) for P_1 and (1.2) for P_0; proof below for the narrower-choice failure.
- 52166–52182: `4.15:lem-action-level`, `4.15:prop-creation-cube`, `4.15:def-no-creation`, and `4.15:eq-action-level-a`, scope proof (1).
- 52184–52196: Proofs of `4.15:lem-action-level` and `4.15:prop-creation-cube`; `4.15:def-no-creation`, ancestor-chain versus persistence distinction.
- 52198–52207: `4.15:def-small-field-complement`; B-CMP119 (1.2), (1.4); `4.15:eq-small-field-complement-b`; `4.15:eq-creation-set-a`, first-step primed sets.
- 52209–52220: `4.15:eq-small-field-complement-b` at 52211, 52216 and 52220; `4.15:def-small-field-complement` at 52213 and 52219, missing first-step form under narrow P′.
- 52222–52240: `4.15:prop-creation-cube` at 52224 and 52228; `4.15:eq-action-level-a`; the two no-creation formulations, failure to exclude k = checked R_k.
- 52242–52245: `4.15:def-small-field-complement`, `4.15:eq-small-field-complement-b`, `4.15:lem-action-level`, `4.15:prop-creation-cube`, assumed inclusion of P′_0.
- 52248–52275: B-CMP99b p. 396, (3.35), (3.37), explicitly printed without proof; (3.35) introduced at 52253, (3.37) at 52261; p. 396 notation explained at 52266–52275.
- 52277–52293: B-CMP99b regularity-class definitions and p. 396 decomposition U′U; (3.35) at 52283; (3.37) at 52285; `4.5:def-admissible-pairs`, current beside A′; operator theorem at free current; Theorem 0 (0), proved as `4.1:thm-clause-zero`; (i), said to be proved in the same induction; correlation-data operator-domain admission used by (iii).
- 52295–52297: Index closing Part III, listing the four items counted as printed without proof.
- 52301–52312: `4.14:not-free-current-notation`, shells; B-CMP109, fine-bond convention.
- 52327–52328: Later unnamed pair estimates in this chapter supply the reason conventions do not affect estimates.
- 52363–52368: `4.14:not-free-current-notation` and `4.16:def-fine-positions`, scales, shells, carried indices and weighted reading.
- 52373–52376: Operator theorem at free current, real space and hypotheses (u1), (reg), with (reg)^sharp defined in the third item below.
- 52398–52420: Operator theorem's regularity clause and radius ceilings; `4.16:eq-data-region-a`, `4.16:def-fine-positions`, `4.14:not-free-current-notation`; B-CMP99b (3.35), derivative notation.
- 52425–52435: `4.16:eq-data-region-b` at 52426 and 52434, hull inclusion used for the nest and perturbation bonds.
- 52437–52444: Operator theorem's enlargement convention; `4.16:eq-data-region-2`; B-CMP109 alternative enlargement wording; later fitting and common block floor.
- 52447–52462: `4.16:def-data-region`; B-CMP99b §3 (big blocks and O(1) ≥ 10), and (3.35) with O(1) = 12.
- 52471–52496: B-CMP99b §3 at 52473, 52477, 52478, 52484 and 52496; `4.16:def-data-region` for box notation; `0.2:not-glossary` for the unrelated ball radius R; Bałaban's class regions translated to shells.
- 52500–52512: `4.16:eq-cube-class-a`; `4.16:eq-lowest-level-regularity-b` at 52503 and 52511 (forward floor F2); bounded-class inclusion claims.
- 52513–52527: B-CMP99b (3.35), translated regularity; `4.16:def-data-region`, gauge convention; B-CMP99b §3, no restrictions outside class hull.
- 52538–52547: `4.16:eq-cube-class-1` and `4.16:eq-cube-class-a`, proof (b).
- 52560–52586: `4.14:prop-prepared-data-admissible` (A1); `4.16:eq-cube-class-1` at 52573 and 52580; `4.16:eq-cube-class-a` at 52584, proof (c).
- 52588–52600: Properties (a)–(c) and the floor; `4.16:eq-cube-class-2`, proved by translating the cited bounds.
- 52602–52609: `4.16:def-data-region`; `4.16:eq-cube-fitting-a` at 52605 and 52608, forward single-box fitting; larger cubes explicitly untreated.
- 52611–52618: `4.16:eq-lowest-level-regularity-b`; property (a); supremum proposition (b), its hat fitting proof (twice); definition of the class of hats, proposed analogous Z requirement.
- 52621–52628: `4.16:def-data-region` at 52624 and 52627; operator theorem at free current for J's possible domain and radii; B-CMP99b (3.37), covariant quotient.
- 52636–52655: `4.16:def-fine-positions`; `4.16:eq-weighted-norm-a` at 52644, 52651 and 52654; B-CMP99b (3.37) at 52650 and 52655; subsequent clause (b), regularity from stronger layered norm.
- 52659–52664: `4.16:def-data-region`; correlation theorem's expansion at step k+1, identifying its cells as tiles.
- 52671–52684: `4.16:eq-cube-class-a`; B-CMP99b class; `4.16:def-cube-class`; `4.14:prop-prepared-data-admissible` (A1); `4.16:def-weighted-norm`; `4.16:eq-data-region-b`.
- 52693–52703: Operator theorem at free current supplies F1; `4.16:eq-lowest-level-regularity-a` at 52694 and 52697; `4.16:eq-lowest-level-regularity-b` at 52699 and 52701; proof below and subsequent statements use derived inequalities; B-CMP99b's ten- and twelve-block cubes.
- 52704–52716: `4.16:eq-lowest-level-regularity-b` at 52706; operator theorem floors; following seam-enlarged corollary; clauses (a), (b) and two proof facts; `4.16:eq-lowest-level-regularity-a`, `-b` at 52714; unevaluated operator-theorem constant.
- 52717–52723: `4.16:eq-data-region-a`; `4.16:eq-fine-positions-a`; supremum proposition (a), whole X_0 centers; `4.16:eq-weighted-norm-a`; `4.16:def-tiles`.
- 52728–52750: B-CMP99b (3.35) at 52728 and 52739; (reg)^sharp supplies the restricted gauge; `4.16:eq-fine-positions-a`, sharpened shell bounds.
- 52752–52758: Operator theorem at free current's choice of data hull; B-CMP99b hull and (3.35), removing the index-zero intersection restriction.
- 52761–52791: B-CMP99b (3.37) at 52761 and 52782; clause (b)'s radius translation; B-CMP109 (1.14), current bound; B-CMP99b explicitly has no current variable.
- 52796–52813: `4.16:prop-lowest-level-regularity`, proof title; `4.14:prop-prepared-data-admissible` (A1); shell definitions; `4.16:eq-lowest-level-regularity-e`, proved Fact (i).
- 52823–52846: `4.16:eq-lowest-level-regularity-a` at 52824 and 52835; (A1) at n = 1 supplies separation; shell definitions and closedness supply higher-shell containment.
- 52848–52851: Fact (ii)'s index-one proof begins and continues outside the chunk; the last displayed equation is not closed here.

## Obligations named here

This list distinguishes adopted requirements from explicit gaps and limits; a scope exclusion is not represented as a promise to prove it later.

- 51561–51566: The opening proof uses clause (0), the assumed small-field complement description, and cube-size lemma (c); the latter is not reproved here.
- 51596–51606: Condition (ii) is required before an action and bars T-step creations in its window; counting preparatory large fields as creations does not remove that requirement.
- 51652–51659, 51835–51842: The whole-component condition is adopted as a hypothesis, not derived; every use is to list it explicitly.
- 51685–51694: Acted components must satisfy the cited cube-size and preceding-step no-creation requirements, including the size condition for previous regions.
- 51709: The new-sequence construction assumes N_k > N_0.
- 51743–51750: Removal of first-class gauge-fixing delta functions requires integration over V_k at least on those components.
- 51808–51810: Whether characteristic functions delimit residual shells is not stated by the cited sentences, and whether Z″_k equals the acted union is unsettled there.
- 51812–51833: The density/operator outline does not determine the post-action top region; whole retention, whole departure and proper core or shell remain consistent with it.
- 51847–51860: The creation-cube proposition requires both the union-of-enlargements complement description and the whole-component post-action hypothesis.
- 51952–51958: The creation-cube conclusion for a post-action region is not proved under the proper-residual alternative.
- 51978–51983: A proper residual would have to contain an old creation cube, and every component of that residual would have to contain such a cube; neither is proved.
- 51993–51999: The cited lower-region relation does not settle the top region; if a proper residual occurs, each of its components still needs a creation-cube proof.
- 52028–52031, 52058–52062: Lower new regions are not required to retain creation cubes and are outside the proposition's conclusion.
- 52113–52120: The action-level inequality is not derivable under a convention automatically satisfying no-creation for short histories.
- 52121–52126: Existence of any action and numerical bounds on n_*, q_0, N_0(k), N_k or the first acting level are not asserted.
- 52127–52132: The creation-cube result is not asserted for the competing post-action description or lower new regions.
- 52133–52138: Identification of the next-step region from the density description is not established; the chosen description is assumed.
- 52139–52144: Persistence of the identified cube in every intermediate top region is not asserted.
- 52145–52150: Positivity of R's denominators, its cited analytic estimates and reference density, the operator theorem, Theorem 0 (i), and additional N_0(k) information are outside what is asserted here.
- 52151–52154: No particular enlargement counts or value of L_0 are established or used here.
- 52155–52162, 52209–52245: The narrow P′ = P′_1 convention does not support the complement form or the two conclusions by this argument; inclusion of P′_0 is part of the assumed statement.
- 52248–52252, 52277–52293: The two lowest-level regularity conditions are carried from text printed without proof; the real datum must meet (3.35), while A′ and J must meet the specified level-zero radii.
- 52373–52376: Membership in the operator theorem's real configuration space requires (u1), (reg) and (reg)^sharp.
- 52378–52385: The hull condition requires Ω_0 enlarged by 2η to lie within the data region.
- 52398–52414: Box regularity requires a gauge and weighted potential/derivative bounds on each relevant enlarged box's data-region intersection, using the stated shell convention.
- 52416–52417: The regularity constant must meet the operator theorem's ceilings, including a^sharp ≤ a_reg^oplus.
- 52509–52512: Whole-class inclusion at indices zero and one requires the fixed twelve-block reading and F2.
- 52602–52609: Cubes larger than N^sharp are not treated and no gluing of gauges across several boxes is attempted.
- 52616–52618: The class-of-hats requirement for the part lying in Z is said to be obtainable by the same ten-block method as the supremum proposition's proof.
- 52649–52655: The layered-norm variant is a stronger hypothesis at boundaries, not an equivalent rewriting of the pointwise norm.
- 52674–52684: Lowest-level regularity assumes (A1), block divisibility, torus-side compatibility and the hull condition.
- 52685–52703: F1 and F2 are imposed block-size floors.
- 52704–52714: F2^sharp is an additional imposed floor for a later seam-enlarged class; it is not needed for the current clauses or two preliminary facts.
- 52715–52716: Implication of F2^sharp by existing operator floors is not asserted because a constant remains unevaluated.
- 52717–52723: The proposition assumes real box regularity, the full X_0 box-center convention, complex pair norm below r, a tile union Z, and j in {0,1}.
- 52755–52758: Removing the data-region intersection at index zero requires the class hull to lie inside the data region.
- 52793–52794: The proposition makes no assertion for cubes larger than N^sharp.
- 52796–52851: The proof is unfinished at the chunk boundary; Fact (i), the box-size argument and the j = 0 case are complete here, while the j = 1 case has only begun.

## For the stage question

No minimiser is defined or discussed in these lines. No analytic ball or complex-background admission theorem is proved here. The only explicit reference to a ball radius is the disambiguation of R at 52477–52479; complex perturbation/current domains and their radius bounds do occur. The entries below record the stage, carried-data, inclusion, removal and shell statements actually present.

| Lines | Statement relevant to stages, domains or carried data | Status here |
|---|---|---|
| 51568–51585 | With shifted attachment the history is pure T below the first acted-region level, so its first component contains a creation cube and every acting index exceeds its own checked cube size. | proved conditionally |
| 51587–51594 | Actions are attached to the acted region's scale, and the acting class is empty for levels at most their checked cube size. | proved conditionally |
| 51596–51606 | Preparatory large-field functions count as new fields for Bałaban's condition (ii), but this counting does not alter the waiting-rule implication used here. | proved conditionally |
| 51611–51629 | The term after a level's actions supplies the top region read by the next step; preparation drop-outs still belong to the original acting class. | definition |
| 51630–51649 | The outside of the acted union is unchanged, while the inside is the union of residuals of acted components. | proved conditionally |
| 51652–51662 | Whole-component retention or deletion is assumed where used; a nonempty proper residual is the alternative it excludes. | assumed |
| 51677–51682 | At a level with no action, the carried term is unchanged and its post-action region equals its pre-action region. | proved in detail |
| 51685–51705 | Preparation can remove a component when a large-field characteristic function destroys its no-creation property; first-decomposition drop-outs are cited as unchanged by subsequent operations, and later drop-outs are only said to be removed. | cited |
| 51707–51728 | The new internal sequence has admissible complements with M-cube separation, retains the old lower entries at j ≤ h, and defines new domains with Ω″_j = Ω_j there. | cited |
| 51730–51740 | The new determining set agrees with B″_k off the surviving preparation union, uses top data inside it, and defines the new background U_k = U_Bk(V). | cited |
| 51742–51750 | First-class components carry remaining small-field characteristic functions, undergo V_k integration and reversed gauge fixing, and yield equivalent rather than equal densities. | cited |
| 51751–51755 | Second-class components retain earlier characteristic and delta factors and are included again in the large-field domain. | cited |
| 51757–51766 | Both classes have localized T′_k(X); first-class components pass into the new top determining domain, while next-step whole-component joining does not itself settle their large-field membership. | cited |
| 51768–51793 | Two readings of the cited new-region sentence respectively remove first-class components or additionally retain the new top set Z″_k. | definition |
| 51794–51807 | The first reading leaves all preparation drop-outs whole and removes first-class components whole; the second can leave proper first-class residuals depending on Z″_k. | proved conditionally |
| 51808–51810 | Residual shells would follow if characteristic functions delimited new regions, but the cited text does not say so or settle Z″_k = Z. | named open |
| 51812–51833 | The operator outline integrates a treated component, extends independence of V_k and multiplies a reference density, while live second-class gauge factors and first-class reference laws do not decide whole retention, whole departure, or residual cores/shells. | named open |
| 51835–51842 | The selected whole-component post-action reading is explicitly carried as a hypothesis throughout the book. | assumed |
| 51845–51950 | Whole-component retention and the complement hypothesis allow creation cubes to pass through every history's pre-action and post-action top components by induction. | proved conditionally |
| 51952–51999 | With proper residuals, neither creation-cube retention nor retention in each residual component has been proved, and the lower-region formula does not decide the top case. | named open |
| 52005–52020 | A nonempty proper residual destroys the whole-component-union description and need not inherit connectivity. | proved conditionally |
| 52022–52078 | New lower regions can be smaller proper subregions, need not contain creation cubes, and are excluded from the top-scale creation assertion; condition (ii) only asks previous regions for the size condition. | proved conditionally |
| 52084–52107 | Post-action region assumptions first matter at the first action, and later steps read regions produced from them. | proved conditionally |
| 52121–52126 | No bounds are asserted for the recursion stopping stage n_*, modification stabilization index q_0 or first acting level. | named open |
| 52127–52150 | Neither proper-residual/lower-region creation, determination of the next region from the density, persistence at all intermediate top levels, nor analytic properties of R are established here. | named open |
| 52198–52245 | The first-step complement must include the P_0 contribution in its creation convention; otherwise a creation-free descendant can escape the waiting argument. | proved conditionally |
| 52277–52293 | The datum is written U′U with real group-valued U and U′ = exp(iηA′), and its two lowest-level requirements are carried into the operator theorem and correlation-data domain admission used by Theorem 0. | assumed |
| 52300–52303 | Shell territories X_n and scales are imported from the free-current notation. | definition |
| 52330–52359 | A set carries entire bonds and pairs; weighted box regularity uses every shell containing an index position, including both bounds at shared shell boundaries. | definition |
| 52362–52376 | The closed data region is the domain of real U for the operator theorem, with real configuration-space membership determined by its regularity hypotheses. | definition |
| 52378–52385 | Perturbation bond sets have a base in the nest hull, whose 2η enlargement must lie within the data region. | assumed |
| 52387–52414 | Box gauges are defined on enlarged-box intersections with the data region and satisfy shellwise bounds; the level-zero territory is all X_0. | assumed |
| 52425–52435 | Nesting and the hull condition imply Ω_1 ⊆ Ω_0 ⊆ Ω_0^dat and carry all perturbation bonds in the data region, so U is available on them. | proved conditionally |
| 52463–52496 | The bounded cube classes use adjacent shells, while Bałaban's index-zero class hull is distinct from the perturbation hull. | definition |
| 52477–52479 | The R defining the class hull is explicitly unrelated to the glossary ball radius R. | definition |
| 52504–52512, 52549–52591 | Bounded Bałaban cubes are admitted to C_0 or C_1, with index-zero class cubes lying in the class hull; the entire class is admitted under the twelve-block convention and F2. | proved conditionally |
| 52524–52527 | Bałaban's class bound uses one level weight even in the adjacent shell and imposes no constraints outside the class hull. | cited |
| 52602–52618 | Only bounded cubes are fitted into one gauge box; larger cubes receive no gluing, while hats and their portions in Z use a cited or proposed ten-block construction. | sketched |
| 52620–52647 | A′ and J take values in the complexified Lie algebra on their bond domains, with J alternatively defined on all data-region bonds; the norm uses operator radii and 0 < r ≤ 1. | definition |
| 52636–52647 | The complex norm uses the minimum shell scale at each index position, unlike the simultaneous shellwise reading (W) for box regularity. | definition |
| 52649–52655 | The alternative layered complex norm is stronger at shell boundaries and is said to remove the later powers-of-L losses. | sketched |
| 52658–52668 | Z is any closed union of level-k LM tiles, the cells of the correlation expansion at step k+1; only carrying of the relevant object by Z is used. | definition |
| 52676–52723 | The regularity proposition assumes admissible prepared-domain geometry, hull inclusion, floors, real box regularity on all X_0, and the complex norm bound. | assumed |
| 52704–52716 | An extra floor admits a later seam-enlarged cube class, but implication of that floor by existing operator floors is not asserted. | assumed |
| 52728–52750 | The proposition claims a restricted real gauge on the cube/Z/data-region intersection and stronger bounds at adjacent-shell positions. | sketched |
| 52752–52758 | Every C_1 cube is already in the data region; index-zero Bałaban cubes need class-hull inclusion, which is said to hold for the operator theorem's data-hull choice. | proved conditionally |
| 52761–52780 | Complex perturbation/current bounds can lose L, L² or L³ only at level-one boundary positions, with no loss for indices carried by Ω_j or at level zero. | sketched |
| 52782–52791 | The perturbation radii translate to the cited (3.37) condition, while the current bound is additional because B-CMP99b has no current variable. | proved conditionally |
| 52800–52813 | Admissibility and nested partitions make every shell a union of s_j-cubes. | proved conditionally |
| 52816–52851 | The proof of two-adjacent-shell intersection establishes box size and the index-zero case, then starts the index-one case before the source stops. | sketched |
