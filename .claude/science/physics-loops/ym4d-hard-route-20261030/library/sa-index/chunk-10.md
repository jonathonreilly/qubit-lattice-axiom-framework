# Chunk 10: lines 10073-11495
Sections: Constrained propagators and local decay (10103); (1c) Propagators in a background field: exponential decay produced by the averages (10107); (i) The setting and the objects (10111); (ii) The principal statements (10242); The additional operator estimates (10343); The response and its independent current (10354); (iii) The strategy (10466); Layered row maps and physical Hessians (10584); Cell norms retain the ultraviolet scale (10602); The growth of a ball in the layer metric (10624); The site readout at an outward row (10666); Finite real existence of the site operators (10722); Transport control on one pillar (10742); A real weighted site gap (10782); The complex site domain uses the actual iterated means (10828); Relative forms give the complex site inverse (10875); Exponential decay from the weighted site form (10900); A scalar subsolution estimate at the fine mesh (10938); Pointwise site Green bounds (10984); Site gradients and their complex continuation (11014); The site Gram inverse has its own lower-bound proof (11076); The Hessian read from the constrained minimum (11143); Which coarse coordinates remove the datum curvature (11181); The next curved fibre inserts a different multiplier (11204); A flat Feynman comparison on all the layers (11257); The Wilson Hessian at small curvature (11313); Compact dual bumps for the actual flat field rows (11387); The correction between adjacent levels (11441); The field-row Gram bounds (11471).

| Lines | Name / tag | Kind | What it states (one plain sentence, your words) | Status here | Reads (inputs it uses, by tag or name) | Key phrase |
|---|---|---|---|---|---|---|
| 10073–10079 | BGD8, small-multiplier-entry (end only) | estimate | The preceding field-only contraction has a coefficient small in the field radius and current ceiling. | sketched | Coupled contraction preceding chunk | "The coefficient is small with" |
| 10081–10091 | Weighted coupled contraction proof | proof | A large fixed multiplier weight makes both Lipschitz row sums less than one half. | proved conditionally | Displayed epsilon/C Lipschitz matrix | "Both row sums are less than one half." |
| 10092–10097 | Multiplier radius | requirement | The multiplier ball must contain the field radius times the chosen weight in physical norms. | assumed | Theta; field radius | "The admitted multiplier radius must be" |
| 10109 | Uniformity contract | requirement | Local bounds must be uniform in region shapes and number, level, cutoff and torus with two nonlocalized exceptions. | assumed | Large-field analysis; statements 0–8 | "none of the constants may vary" |
| 10113–10127 | Separated sequences, layers, tops, rows and distance | definition | Gapped nested cube regions determine local scales, interior and outward rows, and a distance measuring each layer in its own units. | definition | Odd large L; powers M1 and R1; Dirichlet exterior | "is called" |
| 10129–10137 | Regular, on-shell, real and local pairs | definition | A background and independent current obey scaled curvature, first-order, current and real-gauge bounds, with on-shell current equal to the inner action current. | definition | Balaban 109, p. 262, (1.10)–(1.14) | "Such a pair is required to satisfy" |
| 10139 | Straightened averages and operator conventions | definition | Q is the per-length straightened derivative, Q-prime averages gauge transformations, and a and the Hessians use the specified scale and boundary conventions. | definition | Notation §3; site factors; statement 3 | "is the linear part per unit length" |
| 10141–10155 | G-prime, R, S, G0, G, G1, H, H1 | definition | Ordered inverse formulas define the site inverse, slice map, corrected field inverses and constrained extensions. | definition | Q, Q-prime, a, D, Wilson Hessian, independent current | "The operators are defined in this order" |
| 10155–10161 | Delta(2) and six propagators | definition | The quadratic average defines its paired Hessian, and six named field and row operators constitute the propagators. | definition | C(2); G, G1, H, H1 | "The operators are defined in this order" |
| 10163–10186 | explicit-current-continuation | definition | A symmetric commutator form defines the current correction off shell using the slice gauge parameters. | definition | B85c (3.117)–(3.120); B87 (1.8)–(1.14); G-prime, R, D | "The symmetric bilinear form is" |
| 10187–10198 | Physical Hessian identity | identity | Second-order gauge invariance identifies the physical corrected inner Hessian with its slice pullback but does not determine the off-shell continuation. | sketched | Inner action invariance; explicit-current-continuation | "the second variation" |
| 10200–10206 | Fraktur G, Delta-k, A and C(k)(Y) | definition | Formulas define the constrained covariance, coarse Hessian, pivot-eliminated fluctuation matrix and restricted inverse. | definition | G1, H1, R; plain Q_V, Notation §3; soft axial gauge | "In addition we set" |
| 10208 | Identification of the step Hessian | proof | Differentiating the multiplier system and curved datum constraint gives the displayed fluctuation Hessian at the step. | sketched | (1b); Balaban 102,277 (174); 109 (2.4)–(2.8), (2.11); statement 6 | "A single differentiation of the system yields" |
| 10210 | Walk geometry | definition | Overlapping cells, depth-first parent maps, uncut hulls and carriers define walk localization and connecting-tree distance. | definition | Layers; local scales | "In a" |
| 10212–10240 | Notational dictionary | remark | Reused symbols are distinguished across 1c subparts and the Notation, including cube sizes, rows, multipliers and scaled averages. | definition | 1c.1–1c.10; Notation §§3,5,6,9,11; Balaban 116 | "the following further conventions hold" |
| 10242–10244 | Constants and torus room | requirement | Constants have two specified exceptions and each statement imposes a minimum torus size. | assumed | Statements 2,4,5,7,8; mechanism (i) | "These are lower bounds on the volume" |
| 10246–10254 | Norm and Laplacian conventions | definition | Sources, exponential factors, counting kernels and covariant component Laplacians are fixed for the principal statements. | definition | Layer metric; Notation §5 | "kernels are taken with respect to the counting measure" |
| 10256–10260 | Statement 0, activity-domain membership | proposition | An activity-domain pair is regular on the erosion tower with an O(LM) enlargement of the real-gauge radius. | sketched | (1b.8); activity bounds; 1c.1 | "It is a regular pair" |
| 10262 | Layered domain | definition | Layered domains use running layer radii and designated real-gauge cubes for a label sequence. | definition | (2a), Structures; label regions | "By a" |
| 10262 | Layered-domain membership proof | proof | Cube containment and neighboring-layer gauges give local regularity with O(M) real-gauge loss. | sketched | Layered bounds; cube grids and containment | "repeating the same steps" |
| 10264–10285 | Statement 1, flat theorem | theorem | Flat propagators have scaled decay and regularity, inverse-Gram estimates and a positive coarse form on axial-gauge zero-average data. | sketched | Straight averages; separated sequence; mechanisms (a)–(d); 1c.2–1c.4 | "With this, statement 1 is complete." |
| 10285 | Strict axial gauge | definition | Admissible fields vanish on coordinate-order trees and have zero straight one-step average in interior L-blocks. | definition | Three conditions on B; Notation §3 | "The gauge so defined is the strict axial gauge" |
| 10285 | Gauge necessity for positivity | remark | Dropping gauge fixing leaves null directions, and 1c.8 proves the plain-constraint lower bound. | sketched | Statement 1; 1c.8 | "If the gauge condition is dropped" |
| 10287 | Statement 2, real Balaban backgrounds | theorem | Compressed-Hessian propagators are positive and decay, with single-lattice constraint inverses and comparison to actual averaging rows. | sketched | Small real plaquettes; local gauges; Balaban theorems; 1c.5; mechanism (f) | "on sequences it comes from the flat case" |
| 10289–10305 | Statement 3, averages and gauge identities | proposition | Holomorphic average bounds, gauge intertwining and current-defect identities yield constrained criticality on shell. | sketched | Site factors; inner Hessian; regular pairs; 1c.6; mechanism (e) | "the algebraic identities) yields statement 3" |
| 10307 | Statement 4, regular-pair propagators | theorem | All specified inverses exist holomorphically with real positivity and decay subject to stated derivative exceptions. | sketched | Flat bounds; 1c.6; mechanisms (f),(g); small radii | "uses mechanisms (f), (g) to derive" |
| 10309–10340 | Statement 5, walk expansions | theorem | Named operators admit summable local holomorphic walk terms with reserved length factors, covariance and identical transported assignments. | sketched | Statement 4; statement 6; longer sequences; mechanisms (f)–(i) | "Each such operator is then a sum" |
| 10343–10352 | Additional estimates 6–8 | remark | Fluctuation, decoupling and response bounds follow from walk data, with Gaussian comparison and substitution room elsewhere. | sketched | ch:localized-gaussian-comparison; sec:substitution-room; core bounds | "Their estimates are obtained from the walk" |
| 10356–10372 | R9 response and W_s | construction | Nested equations define a decoupled response from scaled extensions and a nonlinearity reduced before parameter insertion. | definition | Walk operators; Q-hat, H, H1, C | "this expression that defines the map" |
| 10374–10382 | Weighted response norms | definition | Slowly varying weights measure a potential and its first derivative and the scaled force. | definition | Layer distance; scales | "use the norms" |
| 10383–10402 | First response contraction | proof | Operator and nonlinear bounds yield a small holomorphic response with weighted decay, splitting and transport by uniqueness. | sketched | b-hat bounds; W_s Lipschitz estimate; datum ceiling b-hat^(-4) | "gives the same contraction in every such weight" |
| 10404–10410 | Independent-current increment | construction | Pairing the multiplier gradient by parts controls the current increment with first-order response norms. | sketched | Multiplier; H derivative bound | "Its increment is" |
| 10412–10433 | Second reduced system | construction | S, H0, tilde G, the row mass and action remainder define a coupled field–multiplier system. | definition | G, G0, Q-hat; action chart; C and N | "The reduced system" |
| 10434–10444 | Second-system smallness and domains | requirement | Small b-hat squared times datum and independent current yields a unique holomorphic solution on global or strip domains. | sketched | Second system; gamma-cur ceiling | "require the additional ceiling" |
| 10446–10464 | Physical response identification | proof | Gauge transversality and holomorphy identify the constrained background and both systems on their common physical polydisc. | sketched | Critical real pair; s=1; uniqueness; invariance | "Holomorphy extends" |
| 10468–10480 | Proof chain | remark | Subparts 1c.1–1c.10 are assigned the geometry, flat, background, walk, fluctuation and response arguments. | definition | Statements 0–8; systems (I),(II) | "The parts have the following content." |
| 10482–10492 | Noncircular dependency order | requirement | Geometry and flat algebra precede background existence, complex propagators, response decay and final physical identification. | assumed | 1b.1–1b.9; 1c.5–1c.9 | "The results are obtained in the following order" |
| 10496–10503 | Mechanism (a), metric and mass | proof | Weighted conjugation and sufficiently large layer gaps give decay, top summability and scale-ratio absorption. | sketched | Mass gap; Combes–Thomas; Balaban 95, p. 36 | "A single conjugation" |
| 10505 | Mechanism (b), all-bare boundary | construction | Bare-collar local models have identity averages and massive finite-range inverses that avoid fine-lattice Dirichlet losses. | sketched | Separation; local R=0; mechanism (d) | "Finite range together with a mass" |
| 10505 | Dirichlet counterexamples | remark | Flat-face and re-entrant-edge examples obstruct several derivative bounds but not the indicated L2 mixed bound. | sketched | One-scale G; free inverse; divergence representation | "Two examples, a flat face and a re-entrant edge" |
| 10507–10511 | Mechanism (c), one/two scales and sharp gap | proof | Heat kernels and an exact orthogonal gauge decomposition reduce estimates to one-scale bounds and coarse axial-tree gaps. | sketched | H_j, H-prime_j; Q1; 1c.3; Balaban 89 and 96 | "This change of gauge splits the form orthogonally" |
| 10514–10527 | Mechanism (d), flat multiscale assembly | proof | Conjugation controls G-prime and a partition parametrix assembles G0 through small commutator, domain and tail errors. | sketched | Mechanisms (a)–(c); P=1-R; local inverses | "Each commutator costs" |
| 10529 | Gram gaps, right inverse and inverse decay | proof | Test functions and a nilpotently corrected row extension give weighted gaps and then conjugation gives decay and localization. | sketched | E0; N squared zero; Combes–Thomas; Schur; Green identity | "follows by duality with test functions" |
| 10531 | Mechanism (e), gauge algebra | proof | Differentiated covariance and action invariance give current-defect identities while geometric accumulation controls multilevel row norms. | sketched | Straightening; inner action; Balaban 109 and 99,389 | "take the derivative of the covariance" |
| 10533–10546 | Mechanism (f), unfolding and parametrix | proof | Auxiliary variables embed the propagators in a finite-range system assembled from small flat perturbations and cutoff errors. | sketched | Flat system; regular gauges; scaling weights; divergence sources | "combined into a single system" |
| 10548 | Mechanism (g), trees | proof | Small nonlocal current vertices attach branches to trunks with a geometric depth-first tree count. | sketched | H-transpose current; 1c.7–1c.9 | "the number of such trees grows geometrically" |
| 10550 | Mechanism (h), multiplier and positivity | proof | The coarse constraint embeds the covariance in a finite-range inverse, and flat positivity survives a homotopy. | sketched | Double-block form; local inverses; parametrix bound | "a homotopy" |
| 10552–10558 | Mechanism (i), length against parameters | estimate | Tree length absorbs parameter growth apart from a fixed corner factor and leaves reserved walk-length decay. | sketched | Parameter geometry; Balaban 116, p. 5 after (1.11) | "The estimate is" |
| 10560 | All-torus assignment of walk terms | construction | Haar averaging, translations, covering push-forwards and a fixed Montel subsequence give real covariant compatible terms. | sketched | Invariant local bounds; entrywise normality; reserved length factor | "A single assignment for all tori is obtained" |
| 10562–10576 | Mechanism (j), first operators-as-data system | proof | Reducing the nonlinearity first permits weighted contraction without invalid decoupled identities and controls the reduced current. | sketched | Balaban 116 (1.5); Schwarz lemma; W_s; operator bounds | "From then on only bounds are used" |
| 10576 | Decoupled Laplacian limitation | remark | First-order operator bounds do not imply a level-uniform Laplacian bound for arbitrary decoupled responses. | sketched | Oscillating-kernel example; reduced current | "an oscillating kernel belonging to the class of data" |
| 10578 | Mechanism (j), system (II) | proof | The second map contracts when b-hat squared times both datum and current is small, with splitting around the diagonal mass. | sketched | System (II); nonlinear orders; current | "can be made small only through the current" |
| 10580 | Mechanism (k), slice to multiplier | proof | Gauge directions remove the slice defect near zero, holomorphy extends this result, and residual defects connect system (II) to physical equations. | sketched | Critical real pair; s=1; statement 3; identity theorem | "by the identity theorem also on the whole polydisc" |
| 10582 | Choice of constants | requirement | L-dependent data precede cube sizes, parameter room, response ceilings and final field strengths with only two nonlocalized exceptions. | assumed | Statements 6–8; (1b); mechanisms (i),(j) | "chosen in the following order" |
| 10587–10594 | Physical norms and variations | definition | Physical fine and row pairings define mass and row norms, with epsilon and h measuring real and complex regularity. | definition | Larger endpoint pillar scale; determining neighborhoods | "every transpose uses the physical bilinear pairing" |
| 10596–10600 | Own-pillar site operators and completed Hessian | definition | The own-pillar map defines the site inverse and slice projection whose Wilson pullback is the physical completed Hessian. | definition | Site identities; forthcoming field intertwining | "On the physical graph the completed Hessian is" |
| 10604–10608 | PX1, layer-metric | definition | Exact path length integrates inverse pillar scale and extends by bare cells outside the action region. | definition | candidate:background; separated sequence | "Use the exact path metric" |
| 10610 | Species amplitudes | definition | Species-specific amplitudes normalize cell suprema for fields, forces, data and multipliers. | definition | Domain section weighted dual conversion | "declare a positive amplitude" |
| 10612–10616 | PX2, cell-entry | definition | A cell entry is the normalized block operator norm including physical measures. | definition | Species norms; restrictions P_y | "define the normalized cell entry" |
| 10616 | Cell versus kernel bounds | remark | Bounded cell norms preserve Coulomb singularities and do not assert a fine-spacing-independent pointwise kernel bound. | assumed | PX2 | "generally false assertion" |
| 10618–10622 | PX3, cell-composition and proof | estimate | Inserting the cell partition bounds composition by convolution and yields an algebra norm. | proved conditionally | Compatible species; finite partition or absolute convergence | "by inserting" |
| 10626 | Metric growth qualification | remark | Layer metric growth is not assumed polynomial because small-scale regions may contain more pillars. | assumed | Layer geometry | "not assumed to have polynomial volume growth" |
| 10628–10631 | PX4, level-barrier and proof | estimate | Each complete intervening layer costs at least rho in path distance. | proved conditionally | Separation; PX1 | "Arcs belonging to distinct layers have disjoint interiors." |
| 10631–10635 | PX5, path-max-scale | estimate | Bounded metric path length controls the largest reachable scale. | proved conditionally | PX4; scale progression | "The same proof applies" |
| 10637–10640 | PX6, physical-ball | estimate | Reached centers lift into a physical ball controlled by maximum scale times metric length. | proved conditionally | PX5 | "Its physical length is at most" |
| 10640–10647 | PX7, metric-ball-count and proof | estimate | Grid and level counts bound metric balls by a fifth-degree polynomial times a controlled exponential uniformly on tori. | proved conditionally | PX4–PX6; grid spacing; rho at least one | "then summing the possible levels gives" |
| 10649–10652 | PX8, entry-with-scale | hypothesis | The cell entry has exponential decay with a fixed power of the scale ratio. | assumed | Species entry; p and m | "An entry bound of the form" |
| 10653–10661 | PX9, entry-to-schur and proof | estimate | Annular summation gives weighted row and column sums under the explicit rate margin. | proved conditionally | PX4, PX7, PX8, PX10 | "This proves the claim with its precise uniformity." |
| 10658–10663 | PX10, summability-rate | requirement | Decay must exceed metric growth and scale losses unless a stronger direct row estimate is proved. | assumed | m, delta, p, rho, L | "must satisfy" |
| 10670–10674 | PX31, own-pillar-site-average | definition | The site map averages hierarchical transported values at the assigned pillar scale. | definition | Actual admitted internal transports | "For a top of level" |
| 10675–10681 | PX32, site-right-inverse and proof | construction | Inverse transport extends top data to an exact right inverse with unit real sup norm and physical L2 isometry. | proved conditionally | PX31; disjoint pillars; real unitary transports for norm claims | "This proves rank without an elliptic estimate." |
| 10681–10685 | PX33, site-weighted-adjoint | identity | Physical pairings identify the site mean with the extension transpose and give an identity Gram matrix. | proved conditionally | PX31–PX32; invariant bilinear pairing | "The invariant bilinear color pairing gives" |
| 10685 | Complex and counting-transpose qualification | requirement | Complex Hermitian norms retain transport condition numbers and counting transposes retain the physical volume ratio. | assumed | PX33; admitted complex transports | "must include the ratio" |
| 10687–10693 | PX34, outward-site-extension and proof | identity | A full outer-end average is exactly a transported average of the adjacent finer own-pillar means. | proved conditionally | Transport products; adjacent-layer containment | "without an asymptotic or small-field approximation" |
| 10695–10701 | PX35, extended-coarse-difference | definition | Coarse differences use assigned top values internally and averaged finer top values at outward endpoints. | definition | PX34; endpoint extension | "Then define the extended coarse difference" |
| 10703–10707 | PX36, node-factor-gauge-derivative and proof | identity | The node-factor derivative on a gauge direction is the hierarchical site mean minus the site value. | proved conditionally | Mean differential; node product rule; PX31 | "Iterating and using the product rule" |
| 10709–10713 | PX37, raw-straightened-intertwining | identity | Subtracting node derivatives from coarse gauge variation leaves the transported endpoint site means. | proved conditionally | Straightening identity; PX36 | "Subtract the two node derivatives" |
| 10713–10717 | PX38, typed-seam-intertwining and proof | identity | The per-length field row intertwines the fine derivative with the extended coarse derivative of the own-pillar map. | proved conditionally | PX34, PX35, PX37 | "proves the intertwining identity" |
| 10719 | Endpoint counts and complex qualification | estimate | Endpoint extensions have depth-uniform normalized counts but their complex estimates still require transport bounds. | proved conditionally | L^4 tops; eight incident rows; complex transport condition numbers | "the algebraic intertwining does not prove them" |
| 10724–10728 | PX39, finite-site-positivity | proposition | The finite real site operator is positive for admitted unitary means, connected pillars and positive top mass. | proved conditionally | Stated real hypotheses; proof 10729–10733 | "Assume the actual mean transports are admitted and unitary" |
| 10729–10733 | PX40, parallel-gauge-stabilizer and positivity proof | proof | Zero energy gives a gauge stabilizer whose zero pillar mean forces every site value to vanish. | proved conditionally | PX39 hypotheses; actual-mean covariance | "This proves" |
| 10735–10738 | PX41, finite-site-gram | proposition | The site inverse and compressed squared Gram matrix are positive finite matrices before uniform estimates. | proved conditionally | PX39; PX32 surjectivity | "invertibility" |
| 10744–10748 | PX42, pillar-curvature | hypothesis | Curvature is small in pillar units on an embedded rectangular determining neighborhood. | assumed | xi=n eta; adjacent-collar constants | "assume" |
| 10750–10754 | PX43, fine-comb-strip and proof | estimate | A coordinate-comb gauge makes internal links O(epsilon/n) close to identity by filling O(n) plaquettes. | proved conditionally | PX42; unitary Stokes product inequality | "uses at most" |
| 10756–10758 | PX44, pillar-coarse-curvature | estimate | Actual coarse curvature is bounded by epsilon times the squared scale ratio. | assumed | Real curvature iteration proved in the background section of this outline | "proved in the background section gives" |
| 10759–10762 | PX45, pillar-open-recurrence and proof | estimate | An averaged-edge deviation is bounded by L times the prior deviation plus coarse curvature error. | proved conditionally | PX44; comparison loops; unitary product bound | "by the unitary product inequality" |
| 10764–10772 | PX46, pillar-open-bound and proof | estimate | Iterating the recurrence gives epsilon times the scale ratio without depth loss. | proved conditionally | PX43–PX45; geometric sum | "The constants do not multiply with the number of levels." |
| 10774–10780 | PX47, uniform-pillar-transport and proof | estimate | Hierarchical actual transports stay O(epsilon) close to identity uniformly in depth in the comb gauge. | proved conditionally | PX46; smooth means; unitary factors; small epsilon | "not a hypothesis of such a property" |
| 10784–10787 | PX48, block-variance | identity | The squared deviation from a block mean equals the averaged pairwise squared difference. | proved in detail | Arithmetic block mean | "The exact variance identity is" |
| 10788–10794 | PX49, flat-block-poincare and proof | estimate | Coordinate paths and their edge counts give the correctly scaled block Poincare inequality including the mean. | proved in detail | PX48; path length and edge multiplicity; physical fine measure | "Multiplying" |
| 10796–10800 | PX50, block-gradient-comparison and proof | estimate | In the comb gauge the ordinary and covariant internal gradients differ by a small inverse-scale multiplication error. | proved conditionally | PX43; bounded site incidence | "The estimate follows from" |
| 10802–10805 | PX51, block-average-comparison | estimate | The actual site mean differs from the arithmetic mean by a small physically normalized L2 error. | proved conditionally | PX47; Cauchy; physical pillar volume | "Cauchy for the finite average" |
| 10806–10812 | PX52, covariant-block-poincare and absorption proof | estimate | Absorbing the small gradient and average comparison errors gives the covariant block inequality. | proved conditionally | PX49–PX51; sufficiently small curvature ceiling | "Absorption proves" |
| 10814–10824 | PX53, real-weighted-site-gap and proof | estimate | Summing disjoint-pillar inequalities gives a depth-, volume-, shape- and holonomy-uniform site gap without current or criticality. | proved conditionally | PX52; positive lower mass coefficient a-star; nonnegative crossing energy | "Sum over the disjoint pillars." |
| 10826 | Hermitian vectors and unweighted gap | remark | The real site gap extends to complex vectors with Hermitian energy and rescales with the largest physical scale. | proved conditionally | PX53; real matrix of unitary connection | "split into Hermitian real and imaginary parts" |
| 10832–10838 | PX54, complex-one-step-recurrences | estimate | Actual complex one-step averages satisfy quadratic open-edge and curvature recurrences on a fixed local chart. | proved conditionally | Small a and curvature on a two-block neighborhood; proof 10839–10843 | "There are constants" |
| 10839–10843 | Proof and explicit constants for PX54 | proof | Product expansion, plaquette sliding, a complex comb gauge and directional Cauchy bounds give the recurrences with explicit polynomial L-dependent constants. | proved conditionally | Finite actual mean chart; Taylor/flux argument; raw-edge ball c/L | "This proves" |
| 10845–10850 | PX55, complex-transport-gronwall and bootstrap | estimate | Normalizing by scale reduces the iteration to a summable recurrence that stays in its charts for a fixed positive input radius. | proved conditionally | PX54; geometric sum of t_r; sufficiently small Z0 | "Induction then gives" |
| 10850–10855 | PX56, complex-pillar-transport | estimate | The whole hierarchical transport and its inverse are bounded uniformly in depth and remain close to identity. | proved conditionally | PX55; product of internal means; input radius c L^(-3) exp(-C L^8) | "This proves the existence and boundedness" |
| 10857–10861 | PX57, site-complex-input | hypothesis | The actual left complex perturbation has a small physical potential and first covariant derivative. | assumed | PX42–PX43; real reference; h_L | "Assume the actual physical first-order input satisfies" |
| 10861–10867 | PX58, site-transport-lipschitz and proof | estimate | A single directional Cauchy disc bounds the change of actual hierarchical transports by C_L h without dimension or depth loss. | proved conditionally | PX55–PX57; h at most h_L/4; reduced real curvature ceiling | "a single directional Cauchy argument" |
| 10869–10873 | PX59, complex-site-average-difference and proof | estimate | Actual complex and real site means differ by a small weighted L2 operator, with the same result for outer extensions. | proved conditionally | PX58; PX51 calculation; upper mass coefficient; PX34 for outer extension | "The proof squares the average difference" |
| 10877 | Actual real and complex site forms | definition | L_U and L_E use their respective actual derivatives and means, with analytic bilinear transposes for the complex operator. | definition | Actual means; physical transpose convention | "Let" |
| 10879–10882 | PX60, complex-site-gradient-difference | estimate | The derivative perturbation is controlled by h times the weighted site norm using adjacent-scale comparability. | proved conditionally | PX57; finite bond incidence; gaps | "The finite incidence count therefore gives" |
| 10883–10889 | PX61, relative-complex-site-form and proof | estimate | Expanding kinetic and mass differences bounds the complex perturbation relative to the real energy. | proved conditionally | PX53, PX59, PX60; bilinear transpose convention | "Keeping derivatives on the two arguments" |
| 10891–10896 | PX62, complex-site-inverse and proof | construction | Factoring by the real inverse square root yields a holomorphic complex inverse and half the real coercivity. | proved conditionally | PX61; C_L h at most one half | "This is a relative-form argument." |
| 10904–10908 | PX63, site-weighted-rows | definition | Site, edge and top exponential multipliers define conjugated derivative and averaging rows. | definition | Bounded one-Lipschitz psi; PX1 | "Put" |
| 10908–10913 | PX64, site-weighted-row-difference and proof | estimate | Conjugated rows differ from original rows by C_L times the weight parameter in the mass norm. | proved conditionally | PX63; bounded cell diameter; exponential difference inequality; physical volumes | "The edge estimate follows from" |
| 10915–10919 | PX65, conjugated-site-form and proof | identity | Oppositely weighted transposes factor the conjugated site form and give a small relative error also for complex fields. | proved conditionally | PX53, PX62, PX64; small h and weight parameter | "The conjugated form has the exact factorization" |
| 10921–10925 | PX66, weighted-site-inverse and proof | estimate | Testing the weighted equation gives a uniform mass-normalized L2 inverse bound without normality or kernel positivity. | proved conditionally | PX65; real gap constant c | "testing the equation" |
| 10927–10931 | PX67, site-cell-l2-decay and proof | estimate | Truncated distance weights convert the weighted inverse bound into exponentially decaying cell L2 entries with physical scale factors. | proved conditionally | PX66; PX1; bounded pillar diameter | "then yields" |
| 10933–10936 | PX68, site-separation-choice | requirement | Separation must make the metric ball-growth rate less than half the site decay rate to obtain Schur summability. | assumed | PX67; PX7–PX10 | "increase the separation after those constants" |
| 10940–10944 | PX69, scalar-massless-kernel | estimate | The four-dimensional scalar lattice Green kernel and its first gradient have Coulomb bounds uniform in the fine mesh. | proved conditionally | Positive heat kernel; BGH2–BGH5; proof 10945–10964 | "Integrating these inequalities gives the asserted Green bounds." |
| 10945–10964 | Heat-kernel tail and Green-bound proof | proof | Fourier bounds and a half-time convolution split yield off-diagonal tails whose time integrals prove PX69 and the delta identity. | proved conditionally | BGH2–BGH4 Fourier formula; BGH5 tails; heat equation | "Split the sum" |
| 10966–10971 | PX70, subsolution-cutoff-identity and proof | identity | Summation by parts represents a nonnegative scalar subsolution by a positive Green test and a cutoff commutator. | proved conditionally | Lw at most F0; radius at least 8 eta; PX69; cutoff bounds | "This identity follows by moving" |
| 10973–10976 | PX71, scalar-subsolution-estimate and proof | estimate | A commutator bound gives a mesh-uniform local L2-to-pointwise subsolution estimate with a coarse-mesh fallback. | proved conditionally | PX69–PX70; annulus volume; point-value estimate | "Cauchy and the annulus volume therefore prove" |
| 10978–10982 | PX72, discrete-kato and proof | estimate | Unitarity bounds the scalar Laplacian of a vector's magnitude by the magnitude of its covariant Laplacian. | proved conditionally | Real unitary connection; full stencil patch | "This proves the covariant scalar subsolution inequality" |
| 10986–10990 | PX73, site-mass-pointwise | estimate | The mass term at a site is bounded by the pillar L2 norm times its inverse fourth scale. | proved conditionally | Real site equation; upper mass coefficient; Cauchy in actual mean | "Cauchy in the average gives" |
| 10992–10998 | PX74, site-local-l2-to-infinity and proof | estimate | A bounded adjacent-pillar neighborhood controls the solution supremum by local L2 values and forcing, including bare-boundary fallback. | proved conditionally | PX71–PX73; rho greater than C_L L; gap; two-top-block torus room | "This proves" |
| 11000–11006 | PX75, site-pointwise-green and proof | estimate | Cell L2 decay and scale-ratio absorption give a pointwise potential estimate for a bounded cell source. | proved conditionally | PX4, PX67, PX74; positive remaining rate m1 | "absorbs the scale ratio" |
| 11008–11012 | PX76, site-laplacian-green and proof | estimate | The site equation and same-pillar mass bound give pointwise covariant Laplacian decay. | proved conditionally | PX75; actual site equation | "The actual equation also gives" |
| 11016–11021 | PX77, site-local-coefficient-class | hypothesis | A supplied unitary local gauge has a small potential and first derivative on a sufficiently collared two-layer patch. | assumed | Regular-pair gauge clause; separate background estimate | "This gauge clause is an input defining the regular-pair class." |
| 11023–11030 | PX78, site-scalar-equation and proof | estimate | Expanding link differences writes the local site equation as a scalar Laplace equation with small first- and zeroth-order errors. | proved conditionally | PX77; physical link exponential bounds | "Expanding the transported differences gives" |
| 11032–11038 | PX79, site-gradient-absorption and proof | estimate | Applying a scalar gradient estimate at the maximum distance-weighted gradient gives an absorbable interior inequality. | proved conditionally | PX78; scalar interior gradient estimate; small local gauge ceiling | "Here is the interior absorption that supplies the gradient." |
| 11038–11048 | PX80, site-gradient-green and proof | estimate | Absorption and scalar Hölder regularity give decaying covariant gradient and Hölder bounds for bounded cell sources. | proved conditionally | PX75–PX79; scalar interior Hölder estimate; assigned local frame | "Absorption" |
| 11050–11060 | PX81, site-profile-spaces | definition | Source-centered exponential norms normalize the potential, gradient and force for strong complex continuation. | definition | PX7 ball growth; spare decay rate; real cell bounds | "let" |
| 11060 | Real inverse in profile spaces | estimate | Summing real bounded-source estimates gives a uniform map from the force profile space to the field profile space. | proved conditionally | PX75, PX80, PX81; spare rate exceeding ball growth | "Summing the bounded-source cell estimates then proves" |
| 11062–11066 | PX82, strong-site-perturbation and proof | estimate | The actual connection perturbation maps the field profile space to the force profile space with norm C_L h. | proved conditionally | PX58; first-order perturbation input; PX81; bounded pillar diameter | "No second difference" |
| 11068–11072 | PX83, strong-site-neumann and proof | construction | A profile-space Neumann series gives complex potential and gradient bounds, while the equation and scalar estimates add Laplacian and Hölder bounds. | proved conditionally | PX62, PX81–PX82; sufficiently small h; scalar interior estimate | "by uniqueness" |
| 11074 | Mixed divergence-source limitation | requirement | Mixed gradient estimates require cancellation or Hölder input and are not obtained for all bounded raw sources. | named open | Bounded-cell site estimates; Calderón–Zygmund singularity | "No uniform bound for that mixed operator" |
| 11078–11089 | PX84, site-smooth-lift | construction | Smooth pillar bumps corrected by their actual mean matrices provide an exact site right inverse with a second-order energy bound. | proved conditionally | PX77; PX45; small local gauge and curvature; bump grid counts | "The resulting operator" |
| 11090 | Proof of smooth-lift bounds | proof | Local gauge expansion, physical volumes, bounded collar overlap and bare-site bumps establish all PX84 bounds. | proved conditionally | PX84 bump construction; PX77 | "The first equality holds pillar by pillar" |
| 11092–11102 | PX85, site-gram-duality | identity | Testing with the smooth lift of Xi to the fourth times the top vector yields the correctly weighted Gram duality inequality. | proved conditionally | PX84; L_U G-prime_U=1; real adjoints | "use" |
| 11103–11106 | PX86, site-gram-lower and proof | estimate | Dividing the duality inequality gives the site Gram lower bound by c_L Xi to the fourth. | proved conditionally | PX85 | "This proves the operator lower bound" |
| 11108–11112 | PX87, normalized-site-gram | definition | A scale-normalized site column map factors the normalized site Gram matrix. | definition | G-prime, Q-prime, Xi; physical transpose | "set" |
| 11113–11116 | PX88, site-column-cell-bound | estimate | The normalized site column map has decaying L2 cell entries with one scale ratio, giving Schur bounds and real Gram comparability. | proved conditionally | PX67; site injection isometry; complex transport bounds; PX10 with p=1; increased separation | "The cell summability calculation" |
| 11118–11122 | PX89, complex-site-gram and proof | estimate | Directional Cauchy bounds give a small complex normalized-Gram perturbation and a uniform inverse on a smaller physical ball. | proved conditionally | PX86–PX88; actual holomorphic physical ball | "Apply one scalar Cauchy circle" |
| 11124–11127 | PX90, nonlocal-conjugation and inverse-decay proof | estimate | The exponential difference inequality and spare decay make conjugation small, giving exponential entries for the complex Gram inverse. | proved conditionally | Exponential Schur norm; PX89; distance-weight argument of PX67 | "a spare fraction of the exponential rate" |
| 11129–11135 | PX91, site-gram-counting-kernel and proof | estimate | Undoing physical orthonormal coordinates and scale factors gives the inverse site's counting kernel with the asymmetric inverse fourth output scale. | proved conditionally | PX87–PX90; physical top pairing | "Undoing both" |
| 11137–11140 | PX92, site-projector-kernel | identity | The normalized Gram representation gives the holomorphic projector with exponentially localized smoothing part and real orthogonality. | proved conditionally | PX87–PX91 | "It agrees with its original Gram formula" |
| 11140 | Limits of the site package | requirement | Fine vector coercivity, mixed source norms and current-constraint terms require additional arguments beyond the site projector. | named open | PX92 | "are not consequences of" |
| 11145–11150 | PX93, physical-stationarity and proof | identity | Slice criticality and the Ward identity imply full stationarity with a row multiplier, unique when the row map is onto. | proved conditionally | Critical admitted chart; Q S=Q; slice projection; annihilator identity; surjectivity for uniqueness | "The finite-dimensional annihilator identity gives" |
| 11152–11155 | PX94, physical-lagrangian-hessian | definition | The physical Lagrangian Hessian subtracts the multiplier contraction with the second derivative of the same straightened constraint. | definition | PX93; Q H=1; same per-length pairing | "Define the actual Lagrangian Hessian" |
| 11157–11161 | PX95, physical-full-form | identity | The physical G1 inverse is the slice-pulled Lagrangian Hessian plus gauge and row mass terms. | proved conditionally | Physical invariant Wilson completion; PX94 | "therefore" |
| 11162–11165 | PX96, physical-row-readout and proof | identity | Multiplication by the constrained extension reads the row Hessian as the inverse row covariance minus its mass. | proved conditionally | Existing G1 and W1 inverses; physical gauge identity; PX95; Q H1=1 | "This proves all signs" |
| 11165 | Existence excluded from Hessian algebra | requirement | The physical row-readout calculation does not establish either inverse used in it. | named open | PX96; G1 and W1 | "It does not prove the existence of either inverse." |
| 11167–11172 | Per-length datum and multiplier conversion | definition | Diagonal row lengths convert raw reduced data to per-length data and determine the dual multiplier convention. | definition | ym4:exp500-bg:mb:reduced-datum | "they are related to the raw" |
| 11173–11179 | PX97, coarse-action-hessian and proof | identity | Differentiating the actual critical branch gives its derivative and the effective Hessian including the datum-curvature multiplier term. | proved conditionally | Actual critical branch; PX93–PX96; fixed slice; differentiated constraint; inverse existence | "differentiate the value function twice" |
| 11183–11186 | PX98, left-coarse-chart | definition | Relative left exponential coordinates against the same coarse reference make interior reduced data exactly equal to the row coordinate. | definition | Same V0 in fine straightening | "the actual coarse group field is" |
| 11188–11194 | PX99, outward-datum-factor | identity | Outward reduced data contain the transported lower-level endpoint factor, constant when only the highest active level varies. | proved conditionally | ym4:exp500-bg:mb:reduced-datum; PX98; zero lower-level data | "Then" |
| 11194 | Outward support-mask check | requirement | The next-step support mask must be checked against every outward carrier before dropping datum corrections. | assumed | PX99; actual support mask | "must be checked against every outward carrier" |
| 11196 | Absolute-logarithm datum curvature | remark | Absolute logarithmic coordinates generally retain a nonzero second derivative and hence the curvature term in the effective Hessian. | assumed | PX97; relative increment at nontrivial reference | "generally does not vanish" |
| 11198–11202 | PX100, active-datum-flatness | hypothesis | Identity first derivative and zero second derivative on the active injection give the uncurved coarse precision and restricted physical current. | assumed | Literal PX98–PX99 map; active injection iota; physical dual weights | "When the literal map" |
| 11206–11210 | PX101, next-raw-constraint | definition | The next plain constraint is the relative logarithm of the actual one-step average in raw bond increments. | definition | Actual plain M; reference V | "The actual plain constraint logarithm is" |
| 11210–11214 | PX102, next-graph-second-derivative | identity | Twice differentiating the actual pivot graph gives its curvature as minus the pivot injection applied to constraint curvature. | proved conditionally | PX101; actual pivot graph; derivative C_V; right inverse h_V | "Twice differentiating the graph equation gives" |
| 11216–11226 | PX103, next-constrained-hessian | identity | The graph chain rule subtracts next-constraint curvature paired with the new multiplier h_V transpose times the coarse gradient. | proved conditionally | PX102; raw coarse Hessian and gradient | "The chain rule on that graph is" |
| 11227–11231 | E_V(2) and gauge derivatives | definition | The next constraint contraction and the actual gauge function's gradient and Hessian are defined in common raw coordinates. | definition | PX103; actual GF function | "Define" |
| 11232–11247 | PX104, complete-next-precision | identity | The complete free precision includes action and gauge Hessians and both curvature contractions, simplifying only at the physical axial locus. | proved conditionally | PX103; actual GF nonnegative and zero at physical background | "The chain rule for the complete next free precision gives" |
| 11243–11247 | Gauge derivatives at arbitrary references | requirement | Both gauge derivatives and the actual model's gauge definition must be retained away from the axial locus. | assumed | PX104 | "must be retained" |
| 11249–11253 | PX105, coarse-raw-duality and proof | identity | Uniform spacing converts physical Hessian and current to raw counting coordinates with squared and cubed spacing factors. | proved in detail | D=xi B; physical volume xi^4 | "Indeed" |
| 11253 | Nonuniform dual conversion | requirement | Nonuniform lengths require diagonal length matrices on both sides without commuting them, and original coupling coefficients remain in the action data. | assumed | PX105; nonuniform row lengths | "must be kept on both sides" |
| 11255 | Three-Hessian diagram | remark | Fine Lagrangian, coarse value and next-fibre Hessians have different row maps, dual currents and gauge terms. | proved conditionally | PX96, PX100, PX103 | "Each arrow has its own row map" |
| 11261–11266 | PX107, flat-field-average | definition | The actual flat straightened per-length row is an explicit positive double average with coefficients summing to one. | definition | Periodic fine lattice; n=L^j; centered blocks | "its flat per-length average is" |
| 11266–11272 | PX108, flat-row-ltwo and proof | estimate | The explicit flat coefficient bound and Cauchy give the row functional an inverse-square-scale L2 bound. | proved conditionally | PX107; two endpoint blocks; physical fine measure | "For example Cauchy gives" |
| 11274–11282 | PX109, flat-feynman-energy | definition | The flat component Feynman energy combines full fine gradients and physically weighted determining-row masses. | definition | Positive bounded row coefficients; larger endpoint scale | "define" |
| 11284 | Determining-row selection | construction | Each nonbare top has a retained adjacent row in every direction by aligned higher-region geometry. | proved conditionally | Aligned blocks; L at least three; retained outward rows | "Both neighboring sites cannot belong to the higher region." |
| 11286–11290 | PX110, flat-row-mean-comparison and proof | estimate | Subtracting a carrier mean and applying box Poincare compares a chosen row with its pillar mean. | proved conditionally | PX108; coordinate-path Poincare; selected row; nesting gap | "To verify this without a pointwise trace estimate" |
| 11292–11297 | PX111, flat-field-local-poincare | estimate | A second Poincare inequality controls each enlarged pillar by carrier gradients and selected row values. | proved conditionally | PX110; enlarged pillar; direct bare-row control | "A second use of Poincare" |
| 11299–11303 | PX112, flat-feynman-gap and overlap proof | estimate | Uniform carrier overlap across adjacent levels turns the local inequality into a full weighted flat vector gap. | proved conditionally | PX111; separated geometry; row multiplicity; torus room | "Summing" |
| 11305–11309 | PX113, flat-field-row-upper and proof | estimate | Flat row mass is bounded by the fine mass norm using row L2 bounds and the same overlap count. | proved conditionally | PX108; comparable scales; PX112 overlap argument | "The preceding overlap count then applies." |
| 11311 | Compression and vector-comparison limitation | remark | Zero-extension compression preserves the Feynman gap, but inner-Maxwell boundary terms and Landau subtraction need separate comparisons. | proved conditionally | PX112; full positive Feynman form | "Those comparisons are separate in the vector precision problem." |
| 11315–11328 | PX114, plaquette-hessian-exact and proof | identity | The plaquette Hessian is the product of summed transported insertions plus a curvature-proportional bilinear remainder. | proved conditionally | Real unitary prefixes; trace cyclicity; actual plaquette action | "There are only sixteen mixed insertion terms." |
| 11330–11334 | PX115, plaquette-linearized-curl | definition | The plaquette curl sums oriented variations transported through the actual plaquette prefixes. | definition | PX114 prefix convention | "Define the plaquette linearized curl" |
| 11335–11340 | PX116, wilson-form-remainder and proof | estimate | Summing curvature remainders bounds the difference between the Wilson Hessian and curl energy in the physical mass norm. | proved conditionally | PX114–PX115; scaled plaquette smallness; bounded plaquette incidence | "Every bond is in at most six unoriented plaquettes." |
| 11342–11347 | PX117, curl-convention-difference and proof | identity | The difference between plaquette and forward covariant curls is an explicit curvature multiple of nearby field values. | proved conditionally | Four-prefix product; PX115; real curvature bound | "Direct multiplication of the four prefixes proves this identity." |
| 11347–11352 | PX118, wilson-lower-form | estimate | Small real curvature bounds the Wilson Hessian below by covariant curl energy minus a small mass error. | proved conditionally | PX116–PX117; decreased curvature ceiling; positive bounded plaquette weights | "after decreasing the fixed curvature ceiling" |
| 11352 | Signed profiles and current subtractions | requirement | Signed layer weights and additional current corrections require separate estimates. | assumed | PX118 | "must be estimated separately" |
| 11354–11361 | PX119, covariant-hodge-error and proof | estimate | On the periodic graph the covariant Hodge identity has only a small curvature mass error from shift commutators. | proved conditionally | Unitary shifts; plaquette smallness; adjacent scales; full periodic graph | "Expand both squares." |
| 11361 | Inner-graph boundary qualification | remark | Summation by parts on a proper inner graph produces additional boundary terms. | assumed | PX119; inner-graph boundary | "additional boundary terms" |
| 11363–11376 | PX120, landau-feynman-difference | identity | The Landau form subtracts a positive real smoothing form from the Feynman gauge, requiring constrained local models and the bare boundary model. | proved conditionally | Site Gram formula; R; projected comparison after px:feynman-coefficient-comparison | "The difference of the two gauge terms" |
| 11378–11384 | PX121, complex-wilson-relative-form and proof | estimate | First-order physical perturbations give a relative Wilson-form bound with curl and mass norms. | proved conditionally | PX114; local first-order core bounds; complex plaquette and curl comparison | "Subtracting" |
| 11384 | Completion of full-precision comparison | requirement | The Wilson and forthcoming field-row bounds must be joined to projected-current and boundary comparisons. | named open | PX121; field-row comparison below; projected-current and boundary comparisons | "We must join it" |
| 11391–11396 | PX125, row-dual-bump | construction | A single-component compact pillar field separates its longitudinal profile from three transverse profiles. | definition | Nonbare top; centered odd n; interior bond support | "Choose a field" |
| 11396–11400 | PX126, row-profile-moments | definition | Two discrete moments of a fixed even bump have uniform positive lower and finite upper bounds. | definition | Smooth profile supported in the middle half-block | "Write" |
| 11402–11406 | PX127, two-row-moments | identity | Counting longitudinal paths gives the only two coarse rows that see the compact bump. | proved conditionally | PX107; PX125–PX126 | "their two response functionals are" |
| 11407–11416 | PX128, explicit-dual-profiles | construction | Explicit even-plus-odd longitudinal profiles are chosen to separate the two neighboring row responses. | definition | PX126–PX127; m=(n-1)/2 | "Define" |
| 11417–11421 | PX129, dual-profile-exactness and proof | identity | Evenness and moment substitution give response pairs (1,0) and (0,1) with bounded amplitudes and first differences. | proved conditionally | PX127–PX128 | "Substitution" |
| 11423–11427 | PX130, finite-row-profile-matrix and proof | construction | For finitely many small odd blocks an explicit invertible two-bond response matrix supplies exact dual profiles. | proved in detail | n at least three; two longitudinal positions; determinant -n^(-9) | "Its determinant is" |
| 11429–11432 | PX131, one-row-seed | construction | Assigning a dual bump to a top endpoint gives a compact seed biorthogonal to one row on its full level grid. | proved conditionally | PX129–PX130; determining-row endpoint; bare identity row | "removes the only other longitudinal row" |
| 11434–11439 | PX132, seed-energy and proof | estimate | Summing at most eight seeds per pillar gives a uniform mass-plus-gradient energy bound in the weighted row norm. | proved conditionally | PX131; profile bounds; disjoint pillars and bounded collar overlap | "The amplitude and first-difference bounds just proved give" |
| 11443 | Adjacent-level leakage support proof | proof | Carrier containment makes every seed invisible to all lower rows and all rows at least two levels higher. | proved conditionally | Nested regions; strict pillar support; outward carriers; bare endpoints | "Thus only the next level can receive an unwanted value." |
| 11445–11449 | PX133, flat-average-composition and proof | identity | Centered digit decomposition shows exact composition of flat full averages with the per-length normalization. | proved in detail | PX107 defining sums; centered transverse and longitudinal digits | "This proves" |
| 11451 | One-step weighted row norm | estimate | Row and column coefficient sums give a Schur bound L^(-1) between consecutive weighted row spaces. | proved in detail | Flat one-step coefficients; physical row norm | "by Schur" |
| 11453–11458 | PX134, row-triangular-leakage and proof | identity | The seed map composes with Q to identity plus a next-level operator of norm at most L^(-1). | proved conditionally | PX131–PX133; leakage support; weighted Schur estimate | "No sum over the number of levels is introduced." |
| 11460–11467 | PX135, flat-layered-row-lift and proof | construction | Correcting seeds by the triangular inverse gives an exact row right inverse with uniform energy control at finite or infinite compatible depth. | proved conditionally | PX132–PX134; finite triangular or convergent geometric series | "We have proved the explicit flat row lift" |
| 11469 | Flat-holonomy transfer | proof | Pillarwise flat unitary frames transfer the lift to periodic flat holonomies with covariant gradient control and unchanged constants. | proved conditionally | PX135; flat parallel frames; scalar majorants | "This handles periodic flat holonomies" |
| 11469 | Scope of the transferred row bound | remark | The transferred estimate controls covariant gradients and does not assume a bare L2 field-row bound for general nonflat fields. | assumed | Flat-holonomy transfer | "No analogous bare" |
| 11473–11477 | PX136, field-row-extension-premise | hypothesis | A real positive fine precision is assumed to admit an exact actual-row extension with controlled energy. | assumed | Positive K; G=K inverse; physical row pairing; E_row | "Suppose the actual row map has an extension" |
| 11478–11484 | PX137, field-row-gram-lower and proof | estimate | Testing with the extension of Xi squared times the row vector gives the covariance lower bound C^(-1) Xi squared. | proved conditionally | PX136; positive K; weighted duality | "Testing" |
| 11486–11489 | PX138, field-row-trace-premise | hypothesis | A separate trace estimate controls row values by the actual fine precision energy. | assumed | K; Q; Xi; physical row norm | "An upper bound needs the separate actual trace estimate" |
| 11490 | Row Gram upper bound and flat premises | proof | Applying the trace estimate to G to the one-half proves the upper Gram bound, with both premises verified for flat Feynman by earlier estimates. | proved conditionally | PX138; PX113, PX112, PX135 for flat Feynman; PX136 | "Indeed apply it" |
| 11490 | Flat Landau coercivity obligation | requirement | The flat lift bounds Landau extension energy but fine Landau coercivity still needs a separate step. | named open | PX135; zero at most R at most one; PX136 | "the needed fine coercivity is still a distinct step" |
| 11492–11495 | Normalized row covariance conjugation (continues next chunk) | proof | A separately proved exponential Schur bound makes distance conjugation of the normalized row covariance an O(delta) perturbation. | sketched | N=Xi^(-1) QGQ-transpose Xi^(-1); exponential cell Schur bound; exponential difference inequality | "If its exponential cell Schur bound has also been proved" |

## Forward and backward references

References below include cross-references within this chunk as well as targets outside it; grouped targets share the indicated source occurrence.

- 10073–10079: BGD8 is the closing tag and discussion of a display begun before this chunk; its coupled contraction is the preceding argument.
- 10109: Balaban papers are identified by CMP volumes 99 (75 and 389), 102 (277), and 122 (175), with full references in the bibliography; principal statements 0–5, auxiliary hypotheses 6–8, and mechanisms (a)–(k) are announced.
- 10127: Balaban 96, (2.46), defines the more restrictive layer-contour distance being compared.
- 10137: Balaban 109, p. 262, (1.10)–(1.14), supplies the independent-current regular-pair framework.
- 10139: Notation §3 defines Q-sharp, the straight linear average, plain logarithmic average, plain derivative and contour means; statement 3 supplies the accumulated site-factor identity and derivative bound; statements 1–2 versus 3–8 use different Wilson Hessian boundary conventions.
- 10155: Statement 3 supplies gauge restoration at the physical current.
- 10163–10165: B85c, (3.117)–(3.120), supplies the gauge identity for the current correction; B87, (1.8)–(1.14), supplies its independent-current treatment.
- 10166–10167: The reference field, site map, slice and pairings are those fixed above.
- 10195–10198: explicit-current-continuation defines the off-shell continuation; the compressed-Hessian boundary comparison is deferred below.
- 10200: Notation §3 supplies the plain one-step linear map Q_V.
- 10208: Identification (1c.1) uses Balaban 102,277, (174), and 109, (2.4)–(2.8), (2.11); the adapted multiplier system is in (1b); Balaban's alternative Hessian expression is compared; statement 6 concerns the displayed form.
- 10212: The symbol dictionary refers to 1c.1–1c.5, 1c.8, and the coarse-cube expansion in 1c.9; the second cube size comes from the Notation; rho and w0 are the 1c.5/1c.9 gap product; statement 7 defines parameter cubes, called w in 1c.9 and Delta in 1c.10; row sets differ in 1c.2, 1c.4, 1c.6, 1c.7 and 1c.10; 1c.10 rescales Q and H; the complex averaging section's Q-st is Notation §3's Q-sharp.
- 10216: Balaban 116, p. 3, uses R1 as a number.
- 10217: Notation §9 defines a different kind of cell.
- 10218–10221: The Notation's coarser-partition hull, gauge factor fraktur G_k, fluctuation operator K in §5, and block B^j(y) are distinguished.
- 10223: Balaban 116 calls the parameter-radius exponent kappa1; the Notation's order of constants calls it bar-kappa.
- 10225: Notation §11 also calls the current radius alpha0.
- 10226–10229: Statement 8 and mechanisms (j),(k) use a multiplier lambda; statement 0, system (I), the clause-1 theorem of 1c.10, statement 6 and system (II) have the specified alternate symbol meanings.
- 10234–10239: In 1c.10, theta0 differs from Notation §6's sequence theta; r, beta, omega, E1 and P1(s) have the stated special meanings.
- 10242: Statement 7's convergence bound and mechanism (i)'s normal-family entry bound are the two constant exceptions.
- 10244: Statements 2, 4 onward, 5, 7 and 8 have the listed torus-room assumptions.
- 10253: Notation §5's Delta denotes the Wilson Hessian, not the component Laplacian used here.
- 10256: Erosion construction (1b.8) supplies the tower for activity-domain membership.
- 10262: (2a), Structures, supplies layered-domain bounds; the regular class and gauge clause are the preceding definitions.
- 10285: Notation §3 defines block axial gauge; 1c.8 proves the plain-constraint lower bound again.
- 10287: Statement 1 supplies the bounds reused for real backgrounds; statements 3–8 use actual averaging rows and the inner Hessian.
- 10301: The second gauge identity is the physical-current completion defined at 10163–10198.
- 10307: Statement 1 supplies upper bounds transferred to six propagators, with stated exceptions.
- 10314: Balaban's H0 and tilde G are identified with the displayed current-zero operators.
- 10315: Statement 4 supplies the radius and cube-size baseline strengthened for the longer sequence.
- 10325–10329: Mechanism (i) consumes the reserved walk factor; statement 4 supplies the four bounds for fraktur G and tilde G and the projector derivative bound; statement 6 supplies the covariance kernel bound also used for the fluctuation matrix.
- 10343–10350: Statements 6–8 concern additional operator estimates; the response is constructed below; ch:localized-gaussian-comparison contains Gaussian comparison; sec:substitution-room supplies hereditary room.
- 10356–10360: Walk expansions supply decoupled operators; the displayed equations are system (R9).
- 10412–10444: The second system complements the first response system and is assigned global and local strip domains, not arbitrary local cores.
- 10446–10464: At physical parameters the first system supplies one second-order bound and the second supplies the other; uniqueness identifies fields only on their common physical domain.
- 10470: 1c.1 defines the operators and classes, counts walks, derives statement 0 and reduces step identification to Balaban's expansion.
- 10471: 1c.2 states the flat theorem, compares published clauses and proves flat algebra with boundary terms and independence from Omega0.
- 10472: 1c.3 handles one-scale estimates, G-prime, the site Gram inverse and R.
- 10473: 1c.4 handles two-scale local models, G0, the row Gram inverse and H, completing statement 1.
- 10474: 1c.5 obtains statement 2 from published whole-lattice theorems and a shortened mechanism (f) on sequences.
- 10475: 1c.6 gives statement 3.
- 10476: 1c.7 uses flat bounds, 1c.6 and mechanisms (f),(g) for statements 4–5.
- 10477: 1c.8 obtains statement 6 except the coarse-cube expansion of A.
- 10478: 1c.9 deduces statement 7 from walk-data properties and geometry and constructs the real, covariant, all-torus assignment.
- 10479: 1c.10 solves systems (I),(II), inserts maps from 1c.6–1c.9 and the data named at the end of statement 7, then treats s=1.
- 10482: Statements 1–7 are independent of a minimizer.
- 10484: 1b.1–1b.2 supply geometry and real averaging calculus.
- 10486: The geometric/algebraic portion of 1b.3 supplies folding, rows, Q-prime/Q/R algebra, top sums and weights without propagator estimates.
- 10487–10488: 1c.5 precedes the remainder of 1b.3 and the existence, regularity and continuation of 1b.4–1b.6.
- 10489: 1c.6–1c.9 use the flat case, block alignment from 1c.5, 1b.1–1b.2 and geometric meet/isometry facts.
- 10490–10491: 1b.7–1b.9 supply response decay and background class membership before final s=1 identification.
- 10503: Statements 5–8, torus comparison and (1d) use local walk terms; mechanisms (d),(f) assemble propagators; Balaban 95, p. 36, discusses conjugation versus walks.
- 10505: Mechanism (d) uses the all-bare local inverse defined in (b); statement 1 is the reference for the mixed derivative bounds compared with the counterexamples.
- 10507: Balaban 89, (2.34), is the scalar scale-recursion precedent; Balaban 96, pp. 246–247, explains gauge-recursion difficulty; 1c.3 supplies simultaneous one-scale estimates; Notation §3's Q1 contains site terms absent from the sharp-gap Q1.
- 10514: Mechanism (a) supplies conjugation for G-prime.
- 10520: Mechanism (c) supplies periodized two-scale inverses, and (b) supplies the bare boundary inverses.
- 10529: Statement 2 is the single-lattice case of the face-test argument; Combes–Thomas and Schur give decay after Gram normalization; the preceding row identity supplies the local-domain comparison.
- 10531: Statement 3 supplies the independent-current defect; Balaban 109, p. 262, uses independent currents; Balaban 99,389, (3.36), (3.38), instead requires second differences for the physical current.
- 10539: Mechanisms (b),(d) use different cubes from the unfolded background system.
- 10548: Tree counting and the convergence threshold agree with 1c.9; 1c.7–1c.8 and 1c.9 use two different depth-first enumerations.
- 10552: Statement 7 defines parameter cubes, distinct from those in (b),(d).
- 10558: Balaban 116, p. 5 after (1.11), gives the parameter-length estimate; p. 3 after (1.7) reserves the extra walk factor.
- 10562: Balaban 116, p. 3, (1.5), supplies the operators-as-data principle; the published response uses identities that do not survive decoupling.
- 10570–10576: The weighted response bounds restate the first system's operator and nonlinearity estimates, and the reduced multiplier current replaces an unavailable full Laplacian estimate.
- 10578: System (II) is the second coupled response system above.
- 10580: System (I) is identified with physical slice equations using statement 3; the residual analysis connects system (II) to the same physical equations.
- 10582: Statement 7 and mechanism (i) are the nonlocalized exceptions; statement 6 fixes coarse cubes; statement 8 identifies the response with (1b).
- 10587: Layers, determining rows and straightening are those defined earlier in this section.
- 10596–10600: R is the previously defined Landau projection; the field-row intertwining is promised below, proved as PX38.
- 10604: candidate:background supplies the compatible spacings and separated sequence.
- 10610: The domain section supplies weighted raw/per-length multiplier conversion.
- 10622: The subsequent row-sum bounds justify infinite-volume composition.
- 10628: PX1 supplies the layer path length.
- 10631: PX4's path-crossing proof also gives the intermediate-point scale bound.
- 10640: PX4 restricts the levels used in counting PX7.
- 10645: The calculation justifies the exponential in PX7.
- 10653: PX4 controls scale ratios and PX7 counts annuli for PX9.
- 10663: PX9 requires PX10 unless a stronger row estimate is supplied.
- 10685: PX33 fixes the weighted, not unweighted, transpose.
- 10693: PX34 is verified by weights and transport products.
- 10695: PX34 defines the outer endpoint extension in PX35.
- 10707: PX36 follows by iterating the one-step mean derivative, using PX31.
- 10709: The actual straightening identity and PX36 supply the subtraction yielding PX37.
- 10713: PX34 supplies the outward-end step in PX38.
- 10717: PX38 supplies the intertwining needed in the earlier slice identities.
- 10733: The zero-energy argument completes PX39.
- 10735–10738: The earlier surjectivity and positive site inverse give PX41 and finite R/S formulas.
- 10740: The quantitative site gap is announced next, proved as PX53.
- 10756: The background section proves the real curvature iteration used as PX44.
- 10764: PX45 is iterated using the PX43 initial bound.
- 10780: PX47 is concluded from the actual transport construction.
- 10788: PX48 plus the path count gives PX49.
- 10796: PX43 supplies the pillar comb gauge.
- 10802: PX47 supplies the average comparison PX51.
- 10806: PX50–PX51 are inserted into PX49 for absorption.
- 10814–10824: Summing PX52 proves PX53.
- 10841: The complex comb/flux calculation proves PX54.
- 10843: Explicit chart and derivative counts supply constants for PX54.
- 10845: PX54 implies the normalized PX55 recurrence.
- 10850: The preceding explicit constants supply a positive uniform input radius; products of internal means give PX56.
- 10857: PX42 and PX43 supply the real reference and comb frame for PX57.
- 10861: The initial complex bounds feed PX55.
- 10863: PX55 fixes the smaller curvature and perturbation ceilings.
- 10867: PX56 gives the uniform bound used in directional Cauchy for PX58.
- 10869: PX51's finite-average calculation is reused for PX59.
- 10873: PX58 bounds each average difference, and PX34 receives the same argument at an adjacent scale.
- 10883: PX60, PX59 and PX53 are combined to prove PX61.
- 10891: PX61 bounds B_E and gives PX62.
- 10902: PX53 is the real weighted gap L_U at least cV.
- 10904: PX1 defines the one-Lipschitz weight.
- 10919: PX64 and PX53 control conjugation; PX62 supplies the admitted complex ball.
- 10927: PX1 controls pillar diameter and PX66 gives distance-weight decay.
- 10933: PX7–PX10 convert PX67 to Schur summability.
- 10940: The scalar local estimate is introduced to explain the absence of fine-singularity loss in PX67.
- 10946–10949: BGH2–BGH4 supply the heat-kernel Fourier formula.
- 10954–10958: BGH5 supplies derivative and order-zero heat-kernel tails.
- 10964: The preceding heat estimates prove PX69 and the normalized delta identity.
- 10971: The Green delta identity proves PX70.
- 10973: PX69 bounds the cutoff commutator for PX71.
- 10992: PX71–PX73 are applied on the local lift to prove PX74.
- 10998: PX71's point-value fallback proves PX74 near bare boundaries.
- 11000: PX67 and PX4 give PX75 after applying PX74.
- 11012: The actual site equation and prior same-pillar bound prove PX76.
- 11016–11021: The regular-pair class supplies PX77; deriving that gauge clause from weaker background tests is assigned to the separate background estimate.
- 11032–11038: A scalar interior gradient estimate, PX78, PX75–PX76 and a scalar Hölder estimate supply PX79–PX80.
- 11048: The earlier bare-boundary observation supplies the direct-difference case.
- 11060: PX7 specifies the spare growth margin needed to sum cell estimates in PX81.
- 11062: PX58 supplies the site mass perturbation in PX82.
- 11072: PX83 agrees with the inverse in PX62 by uniqueness; scalar local estimates then give complex Hölder bounds.
- 11082: PX77 and the real recurrence PX45 control actual transports for the smooth lift.
- 11090: PX77 bounds local derivatives and establishes the last PX84 estimate.
- 11092: PX84 and L_U G-prime_U=1 give the PX85 duality calculation.
- 11106: The Xi-to-the-fourth test in PX85 is essential for PX86.
- 11113: PX67 supplies the normalized column bound PX88.
- 11116: The cell summability calculation PX8–PX10 with p=1 gives the column and product Schur bounds.
- 11118: The actual physical ball constructed above and PX88 support directional Cauchy for PX89.
- 11127: PX89 and the distance-weight argument of PX67 give inverse normalized-Gram decay.
- 11129–11135: The physical top basis and PX87 normalization give PX91.
- 11140: PX87 identifies PX92 with the original Gram projector; vector and current estimates are excluded from its consequences.
- 11150: The earlier Q S=Q and slice identities plus the Ward identity give PX93.
- 11152: PX93 and Q H=1 identify the multiplier used in PX94.
- 11162–11165: The physical gauge identity, PX95 and Q H1=1 prove PX96.
- 11167–11172: PX97–PX100 use per-length coordinates converted from ym4:exp500-bg:mb:reduced-datum.
- 11173–11179: PX95 and differentiated stationarity/constraint prove PX97.
- 11186: The exact interior node identity gives b(B)=B in PX98's chart.
- 11193–11194: ym4:exp500-bg:mb:reduced-datum supplies the raw factor in PX99.
- 11196: PX97 retains its datum-curvature term for absolute coordinates.
- 11198: PX98–PX99 are the literal maps to test for PX100.
- 11210: PX101's pivot graph and right inverse give PX102.
- 11216–11228: PX102 gives PX103 by the chain rule, whose last contraction defines E_V(2).
- 11239–11247: The physical block-axial background makes the actual GF gradient vanish; arbitrary references require the full PX104 expression.
- 11255: PX96, PX100 and PX103 combine into the three-Hessian diagram.
- 11266: PX107 is expressly the flat straightened average, not the plain path map.
- 11286: The coordinate-path proof of the scalar block inequality supplies box Poincare for PX110.
- 11290–11296: The row L2 bound and box Poincare yield PX110 and its second application PX111.
- 11299: Summing PX111 with the carrier overlap count gives PX112.
- 11309: PX108 and the preceding overlap count prove PX113; PX112–PX113 concern the component Feynman form.
- 11311: PX112 applies after zero extension; inner-Maxwell boundary and nonlocal subtraction comparisons are assigned separately to the vector precision problem.
- 11335: Summing PX114 with PX115 gives PX116.
- 11347: Prefix multiplication proves PX117 and the curl comparison used in PX118.
- 11361: The covariant shift expansion proves PX119; inner-graph boundary terms remain additional.
- 11370–11376: The discussion after px:feynman-coefficient-comparison supplies the projected local models and parametrix; the all-bare local boundary model was described above.
- 11378: Subtracting PX114 gives PX121.
- 11384: The field-row comparison is promised below, and projected-current/boundary comparisons must still be joined for the full precision.
- 11402: PX107 supplies the multiplicities used in PX127.
- 11417–11421: Substitution into PX127 proves PX129 for the profiles PX128.
- 11432: PX129 eliminates the other longitudinal row for PX131.
- 11434–11439: Previously proved profile bounds and support overlap give PX132.
- 11449: Digit tiling proves PX133 including normalization.
- 11453: PX131–PX133 and the weighted Schur argument give PX134.
- 11460–11467: The preceding triangular and energy estimates prove PX135.
- 11469: The same flat construction transfers to pillarwise parallel frames.
- 11473: The preceding flat proof is the special case motivating PX136.
- 11478–11484: Testing the PX136 extension gives PX137.
- 11490: PX138 gives the upper bound; PX113, PX112 and PX135 establish both premises for flat Feynman; PX135 and 0≤R≤1 establish only the Landau extension energy cost, leaving coercivity separate.
- 11492–11495: A separately proved exponential cell Schur bound is the premise for applying the earlier exponentially weighted conjugation argument to normalized row covariance; the argument continues beyond this chunk.

## Obligations named here

These include explicit defining requirements and assumptions, quantitative choices, and statements expressly excluded from the proofs; inclusion does not mean that every item is an unresolved conjecture.

- 10081–10094: Assume the stated two-component Lipschitz matrix, choose Theta and epsilon in order, and admit a multiplier radius at least Theta times the field radius.
- 10109: Keep all localized constants uniform in region geometry and number, level, cutoff and torus, allowing only the two named nonlocalized exceptions.
- 10113–10119: Use odd large L, power-of-L cube/gap sizes, R1 at least L, separated cube regions and Dirichlet conditions outside Omega0.
- 10129–10137: Regular pairs must satisfy the scaled curvature, first-order and independent-current bounds and the real gauge clause on every specified cube.
- 10137: The local real-gauge bound is alpha0 throughout the cube rather than O(M1) alpha0; on-shell pairs must equal the inner-plaquette current at bonds touching Omega1.
- 10139: Use straightened rather than plain averages for the intertwining and near-one derivative bound, and use the Hessian boundary convention assigned to each statement.
- 10163–10198: Fix the common reference, site map, slice and physical pairings, and specify the off-shell current correction by its explicit formula; the physical identity alone does not specify it.
- 10208: Step identification for the actual averages uses the (1b) multiplier differentiation and the quadratic one-step constraint term.
- 10242–10244: Respect the L-only constant contract and the distinct torus-room thresholds for statements 2, 4 onward, 5, 7 and 8.
- 10262: Layered radii must not exceed their running levels' radii, and the construction's field strengths are fixed after M.
- 10285: Flat positive-form data must have interior support, zero straight average and strict axial-tree gauge fixing; removing gauge fixing leaves null directions.
- 10287: Real compressed-Hessian estimates require local gauges and small plaquettes, including plaquettes protruding from Omega0 for G0.
- 10287: The single-lattice right-inverse claim additionally requires the stated current/plaquette smallness.
- 10307: Fix the regularity ceiling before M1 independently of M1, and retain the stated exceptions for second differences, Hölder ranges and complex G-prime bounds.
- 10315: The fluctuation covariance and precision need regularity on the longer sequence, a larger M1 and a smaller radius ceiling.
- 10332–10340: Walk terms must have local holomorphy, trace dependence, reality, gauge covariance and identical transported assignments, with the stated translation/isometry restrictions.
- 10369–10372: Reduce the quadratic nonlinearity before inserting decoupling parameters; do not impose undecoupled identities on decoupled sums.
- 10374–10392: Weights must satisfy the metric variation bound, the field ball must lie below c/b-hat, and datum size must be at most c b-hat^(-4).
- 10434–10444: The second system requires both b-hat squared times datum and b-hat squared times independent-current ceiling to be small, and is restricted to its stated global/strip domains.
- 10446–10464: Physical constraint identification requires s=1 and a critical real reference before analytic continuation; no arbitrary-decoupling constraint identity is asserted.
- 10482–10492: Preserve the stated noncircular order of background and propagator results.
- 10496: Choose the conjugation rate below c gamma L^(-2) and then the gap product large enough relative to rate and scale power.
- 10505: Put boundary cubes and cutoff collars inside the all-bare collar; the cited fine-lattice Dirichlet counterexamples preclude substituting general nonbare boundary models.
- 10507: The gauge-propagator proof needs one-scale bounds simultaneously in all orders rather than iterating the two-scale recursion.
- 10539–10546: Local unfolded perturbations must be small relative to flat constants, and the cutoffs and scaling/source structure must preserve the finite-range parametrix estimates.
- 10552–10558: Parameter-cube size must pay for parameter growth in the exponential rate, with the unavoidable exp(16 bar-kappa) factor retained.
- 10560: Covariant/real/all-torus properties of single terms must be produced by construction using invariant bounds; the normal-family entry bound may not enter localized estimates.
- 10562: Decoupled operator sums lack the physical right-inverse and gauge identities, so those identities must be used only before defining W_s.
- 10576: First-order data do not yield a uniform full Laplacian bound for arbitrary decoupled response; the reduced multiplier current is the supplied replacement.
- 10578: System (II) requires small b-hat squared times current as well as datum, and splitting must account for its globally carried diagonal mass.
- 10580: The slice-to-multiplier argument starts at a critical regular real pair and s=1 and uses the factorization with site and seam factors.
- 10582: Follow the specified order of constants, choose final field strengths small relative to (LM)^(-1), and choose the background datum small relative to M1^(-1) for statement 8's identification.
- 10587–10594: Use physical bilinear fine/row pairings, the per-length straightened map, and actual first-order complex variation bounds.
- 10616: Cell bounds must include physical measures and must not be replaced by a fine-spacing-independent pointwise kernel assertion.
- 10622: Infinite-volume cell composition requires absolute convergence from the row sums.
- 10658–10663: PX10's numerical rate margin must hold, or a stronger actual row estimate must be proved directly; arbitrarily weak exponential decay is insufficient.
- 10685: Complex transport norms need actual condition numbers and a counting transpose must include the volume ratio.
- 10717–10719: Outward rows must use the extended endpoint mean; the algebraic intertwining does not establish complex transport bounds.
- 10724: Finite real site positivity assumes admitted unitary actual means, a connected pillar path from every active site to its top, and positive a.
- 10744–10748: The transport argument assumes small scaled pillar curvature and an embedded rectangular determining neighborhood with any adjacent collar accounted for.
- 10774–10780: Choose epsilon small enough to admit every internal mean in the real transport construction.
- 10806: Choose the real curvature ceiling so the comparison error absorbs into at most half the block inequality.
- 10814: The global real site gap requires a(y)=c_y xi_y^(-2) with a strictly positive uniform lower coefficient.
- 10832–10843: Complex one-step edges and curvature must lie in their admitted chart, with finite construction bounds fixed before iteration.
- 10850: Choose Z0 below the chart radius times the inverse Gronwall growth factor to keep every level admitted.
- 10857–10863: The complex input must control both potential and first covariant derivative, with h at most h_L/4 and a jointly reduced real curvature ceiling.
- 10873: The site-average difference bound uses a uniform upper mass coefficient and actual adjacent-scale transport bounds.
- 10891–10896: Choose C_L h at most one half for the relative complex inverse; an unscaled coefficient perturbation norm is not supplied.
- 10904–10919: Exponential weights must be bounded and one-Lipschitz, with h and the conjugation parameter small enough for a half-sized relative error.
- 10933–10936: Choose or verify separation so 8 log L/rho is less than m/2; the rate is fixed before this choice.
- 10966–10976: The scalar subsolution proof requires nonnegative w, a local Laplacian upper bound and the prescribed cutoff, with the point-value fallback at bounded mesh ratios.
- 10978–10982: Kato's argument uses a real unitary connection and a full covariant stencil; bare boundary cells use the fallback instead.
- 10992–10998: Choose gaps so the local ball meets only adjacent comparable layers and use the stated torus room to control lifted multiplicity.
- 11000–11006: Separation must leave a positive m1 after paying the three-power scale ratio in the pointwise Green estimate.
- 11016–11021: The small local gauge clause is an input of the regular-pair class; deriving it from weaker background tests is a separate background estimate.
- 11021: Local gauge patches and collars must exclude a third layer.
- 11038–11048: Choose C_L a_loc at most one half, use the declared local frame or transport for Hölder comparison, and do not assume a uniform constant as the exponent approaches one.
- 11060: The profile-space rate must leave a spare margin exceeding metric ball growth.
- 11062–11068: Complex strong continuation requires first-order control of E, not only its supremum, and h below the Neumann threshold.
- 11074: A mixed gradient with divergence source needs its specified cancellation or Hölder input; no all-bounded-raw-source estimate is established.
- 11078: Invertibility of G-prime alone does not prove a uniform site Gram inverse; the separate bump argument is required and then supplied.
- 11082–11090: Smooth-lift mean matrices require a fixed small local gauge/curvature ceiling and a one-fine-cell collar with bounded overlap.
- 11106: The Gram duality test must use Xi to the fourth rather than the unweighted smooth lift.
- 11116: Increase fixed separation if necessary for the p=1 site-column Schur bound.
- 11118–11127: Restrict to the smaller physical ball for the complex Gram inverse and reserve a fraction of exponential rate for conjugation.
- 11140: Fine vector coercivity, mixed derivative source norms and current-constraint terms are not consequences of the site projector package.
- 11145–11150: The Hessian calculation presupposes an admitted critical chart and fixed reference slice; multiplier uniqueness additionally needs onto rows or an existing row Gram inverse.
- 11155: The Lagrangian quadratic constraint must be the second derivative of the same straightened row map with the same per-length pairing.
- 11165: The physical row-readout algebra does not prove existence of either G1 or W1 inverse.
- 11167–11179: Critical-branch differentiation must retain the raw-to-per-length datum conversion and the datum-curvature contraction.
- 11194: Check the actual next-step support mask against every outward carrier; a mask alone does not flatten a logarithmic coordinate.
- 11196–11202: Removing datum curvature requires the literal relative chart and PX100 on the actual active injection, with the restricted current and physical dual weights retained.
- 11210–11214: Use the actual pivot graph and its right inverse, rather than an arbitrary extension selected after the Hessian.
- 11224–11226: The next constraint multiplier is h_V transpose times the raw coarse gradient, not the unreduced gradient unless that transpose is already included.
- 11239–11247: Away from the physical block-axial locus retain both gauge derivatives and use the actual gauge definition.
- 11253: At nonuniform row lengths retain diagonal length matrices on both sides without commuting them, and retain the original action couplings.
- 11255: The three physical Hessians are not interchangeable despite their chain-rule relations.
- 11274–11282: The flat Feynman energy uses positive bounded row coefficients and the physical pairing without an extra fine volume or unweighted transpose.
- 11299–11303: Global flat-vector summation requires the proved adjacent-level overlap count and bounded torus-lift multiplicity.
- 11311: Inner-plaquette boundary terms and Landau's nonlocal subtraction still need separate vector-precision comparisons.
- 11335–11340: The Wilson remainder estimate assumes curvature small in the largest corner scale.
- 11352: Signed layer profiles and additional current subtractions must be estimated separately.
- 11361: On proper inner graphs the Hodge calculation has additional boundary terms.
- 11370–11376: The projected comparison must retain Landau subtraction together with row mass and use the all-bare boundary model; global R is not asserted zero at an interface.
- 11384: Join the Wilson and field-row comparisons to projected-current and boundary comparisons to obtain the full precision.
- 11391–11400: Compact bump profiles must have strict interior support and uniformly positive discrete moments.
- 11429–11439: Assign outward seeds to interior tops and preserve the bounded seed/collar multiplicity used for the energy estimate.
- 11469: Flat-holonomy transfer controls the covariant gradient, not an ordinary gradient in an arbitrary gauge; no general nonflat bare L2 row bound is assumed.
- 11473–11477: The general row Gram lower bound assumes real positive K and an actual exact extension with the PX136 energy cost.
- 11486–11490: The row Gram upper bound requires the separate actual trace premise PX138; flat Feynman premises are verified here.
- 11490: Flat Landau still needs fine coercivity as a distinct step despite the established extension energy bound.
- 11492–11495: Exponential conjugation of normalized row covariance assumes its exponential cell Schur bound has already been proved; the argument is unfinished at this chunk boundary.
