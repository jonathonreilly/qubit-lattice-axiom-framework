# Chunk 30: lines 32466-32993
Sections: Notation and units (32496); Lattices, fields, and action (32506); Averages, Gaussian coordinates, and propagators (32546); Running quantities and source domains (32598); Local families, histories, and analytic requirements (32647); Limits, phases, and reconstruction (32734); Index of arguments and proof obligations (32869); Named statements in the proof outline (32877); Detailed proofs of referenced statements (32881); Statements still to be proved, by package (32891), with Package A (32909), Package C (32911), Package D (32913), Package E (32915), Package F (32917), Package G (32919), Package A--H (32921); Formula and statement navigation (32923). The bibliography occupies 32935-32988 without a section title; 32466-32490 continues the preceding comparison module without a heading.

| Lines | Name / tag | Kind | What it states (one plain sentence, your words) | Status here | Reads (inputs it uses, by tag or name) | Key phrase |
|---|---|---|---|---|---|---|
| 32466-32469 | HB spatial rotation action, V_R | construction | Given full scalar rotation invariance, spatial rotations act on the HB quotient by rotating test tuples. | definition | HB quotient hypotheses; full scalar rotation invariance | "Once full scalar rotation" |
| 32470-32476 | Unitary spatial rotations and spectral covariance | proof | Preservation of the form and local continuity yield a strongly continuous unitary spatial action and rotation covariance of the joint spectrum. | sketched | V_R; positive form and null space; local C^1 continuity; time and spatial translations | "Local \(C^1\) continuity proves strong continuity on dense test vectors" |
| 32477-32480 | Rotated cube cone, E ≥ absolute momentum | proof | Applying cube inequalities on a countable dense rotation set and then approximating a momentum-aligning rotation gives the round spectral cone. | proved conditionally | HB cube inequalities for the limit; spatial spectral covariance | "use a countable dense" |
| 32481-32485 | Centering C_m and sh_ξ | identity | The earlier centering map preserves these conclusions and identifies sh_ξ with C_{−m_ξ}, whose inverse is C_{m_ξ}. | sketched | ch:euclidean-hilbert-bridge; m_ξ(f)=c_ξ∫f | "Centering is the map \(C_m\) proved in" |
| 32486 | Time-mixing rotation operator | remark | The text does not assert an operator implementing a general time-mixing Euclidean rotation. | named open | HB spatial action | "No operator for a general time-mixing Euclidean rotation is asserted." |
| 32487-32490 | Reconstruction, identification, gap, and angular interface | requirement | External reconstruction, F4 identification and a mass gap remain separate, while the periodic angular route retains its own mirror, cone and ultraviolet assumptions. | named open | External OS reconstruction; F4; periodic-state angular proof; optional Ward premises | "any mass-gap estimate remain separate" |
| 32499-32504 | Scope of the notation index | requirement | Uninstantiated auxiliary maps require specified types and estimates as inputs, and listing their symbols does not establish existence. | assumed | Technical definitions of analytic domains and history data | "and required estimates are inputs" |
| 32509-32512 | G, g, N, d_G and trace normalization | definition | The gauge group is SU(2) with Hermitian traceless Lie algebra, half-trace inner product, N=2 and d_G=3. | definition | None | "The gauge group is" |
| 32512-32513 | Statements retaining N | requirement | Any statement retaining a general N must specify its matrix group and trace convention. | assumed | General-N statements | "and trace convention must be specified" |
| 32514-32520 | L, M, cofinal tori and fixed geometry | definition | Blocking uses odd L>1, M=L^{m_0}, compatible tori ℓ=2L^m and geometric constants fixed before cutoffs, fields and sources. | definition | m≥m_0; actual scales a_s | "geometric parameters $M_1,M_2$ and the buffer constants are fixed before" |
| 32521-32524 | K, j, s, a_s, η_j | definition | Depth is s=K−j, physical spacing is L^{−s}, and the fine spacing in level-j units is η_j=L^{−j}. | definition | Blocking integer L | "Level $j$ has depth $s=K-j$" |
| 32525-32529 | Λ_{K,ℓ}, T^(j) and aZ^4 | definition | The finite torus and level-j lattice are specified in physical units, alongside the fixed-spacing infinite lattice. | definition | K, ℓ, L, j | "is a compatible" |
| 32530-32533 | U_b, U_p, ∂U and x(p) | definition | Bond variables reverse by inversion, plaquettes carry ordered transport, and gauge transformations act at bond endpoints. | definition | Gauge group G | "is a positively oriented bond" |
| 32534-32538 | a_p, A(w,U), β and Wilson weight | definition | The plaquette action defines weighted and unweighted Wilson actions with β=g_0^{−2}=2N/g_std^2. | definition | U_p; plaquette barycentres; w | "The inverse coupling convention is" |
| 32539-32543 | O(f), S_n^T and centering | definition | The observable has no spacing prefactor, its connected correlations are logarithmic source derivatives, and centering affects only the first cumulant. | definition | a_p; sourced partition function | "has no additional spacing prefactor" |
| 32549-32553 | M, Q_k, Q_k^sharp | definition | The chosen Borel block average has distinct plain and gauge-straightened linearizations at nontrivial backgrounds. | definition | Regular real configurations; coarse gauge factor | "They are different operators at a nontrivial background" |
| 32554-32556 | Q_k^st, Q_k′ and adjoints | definition | Straight covariant bond averaging and site averaging use adjoints determined by both lattice inner products. | definition | Source and target lattice inner products | "An adjoint always" |
| 32557-32562 | d_0, d_1, d_η and curvature projection | definition | The cochain gradient and circulation are distinguished from the physical scalar difference, while common rescaling leaves the curvature-range projection unchanged. | definition | Relevant cochain theorem; range of d_1 | "is the physical scalar difference in" |
| 32563-32566 | Scalar Q, P, A_η and G′ | definition | With fine weight η^4 and an unweighted coarse sum, arithmetic averaging gives constant lifting, P=Q*Q and G′=(d_η*d_η+P)^{−1}. | definition | Scalar block calculation; specified inner products | "Then $Q^*$ lifts constants" |
| 32567-32568 | Block normalization conversion | remark | Plain inner products change the averaging adjoint, with the unitary conversion proved in the block-normalization section. | sketched | Block-normalization section | "The unitary conversion is proved in the block-normalization section" |
| 32569-32572 | R, bold R and R^(j) | definition | The notation distinguishes a scalar orthogonal projection, the large-field operation and a local remainder by type. | definition | Scalar Landau gauge; QG′ | "not interchangeable" |
| 32573-32579 | P_ex, K and mathsf K | definition | The exact-two-form projection has physical kernel a^{−4}P_ex, and the continuum curvature covariance is specified off zero with contact terms in its Fourier distribution. | definition | Exact lattice two-forms; unit coupling; exterior square | "The Fourier distributions also contain contact terms" |
| 32580-32583 | U_j(V), mathsf G and mathsf H | definition | These symbols denote a constrained regular background, its constrained inverse and its response operator. | definition | Specified coarse averages V | "denote a constrained inverse and a response operator" |
| 32583-32585 | Background obligations A1--A4 | requirement | Existence, domains, gauges and uniform bounds for the background operators must still be proved beyond the scalar model. | named open | A1--A4; proved scalar model | "which we must prove" |
| 32586-32593 | Φ_Λ(B), r_B and Z_y | definition | The collared-box background pair uses dimensionless coarse bond data and a weighted local potential/current output norm. | definition | ch:pointed-window-remainder; ξ_y; H; J | "potential/current background pair on a collared box" |
| 32590-32595 | Product-polydisc response and finite-box comparison | requirement | Response control covers the entire datum polydisc, and comparison uses compatible equations and boundary rows with their natural force weights. | assumed | Φ_Λ; r_B; actual compatible equations; cell weights | "not merely at zero" |
| 32601-32604 | Running x_j, g_j and b_j | definition | Actual marginal increments recursively define x_j and g_j without assuming each increment is positive. | definition | x_0=β; all marginal-action contributions | "is not assumed in the arithmetic theorem" |
| 32605-32608 | One-loop b_j^0 and proposed c_0 | definition | The designated one-loop increment has proposed slope 11N² log L/(12π²) in the stated normalization. | definition | L; N; coupling normalization | "The proposed leading slope is" |
| 32607-32608 | First-passage numerical inputs | hypothesis | The numerical first-passage theorem takes an interval sum law and error envelope as inputs and does not compute c_0. | assumed | b_j^0 interval sum law; error envelope | "it does not calculate this coefficient" |
| 32609-32614 | θ_j, bar g_j and natural superscript | definition | The frozen reference θ_j=g^{−2}+c_0(K−j) defines an auxiliary coupling and the natural-marked quantities computed with frozen choices. | definition | g; c_0; K; j | "is a prescribed frozen reference sequence" |
| 32614-32615 | Calibrated holomorphy and cutoff comparison | requirement | Holomorphy of the calibrated coordinate and comparison between cutoffs require additional analytic assertions. | assumed | Frozen calibrated coordinate | "are additional analytic assertions" |
| 32616-32619 | K(β,g) and W_K(g) | definition | The first scale entering the B_sharp-wide window above g^{−2} determines the first-passage set of bare couplings. | definition | x_j; B_sharp; g | "is the first scale" |
| 32620-32623 | Source triple w,c,z,f_i | definition | A source consists of a constant, a finite real test family and complex coefficients representing w=c+Σz_if_i. | definition | Real tests f_i | "A source is a triple" |
| 32622-32623 | Source representation independence | requirement | Physical quantities must depend only on the relevant plaquette values of the represented source. | assumed | Source triple; plaquette values | "physical quantities must depend only on its relevant plaquette values" |
| 32624-32628 | Sharp/flat source notation and W_r^(s) | definition | The sharp norm combines supremum and scaled Lipschitz norms, giving a weighted triple norm and slice source balls, while the flat symbol is listed without a separate formula. | definition | c_M; L; s; source triple | "The source-triple norm is" |
| 32629-32633 | h_y^(j), φ_j and ζ_j | definition | The source-domain partition, fixed coupling profile and exact-counterterm running shift are fixed data rather than an extra free bare coupling. | definition | Source domain section; exact counterterm identity | "is defined there by the exact counterterm identity" |
| 32634-32638 | varrho, rho and α_{0,j}, α_{1,j} | definition | Source and coupling-disc radii are distinct from the complex field-domain radii. | definition | Domains in respective statements | "are radii of complex" |
| 32637-32638 | Coefficient-extraction radius | requirement | A coefficient-extraction radius cannot be silently replaced by a smaller running radius. | assumed | Declared extraction radius | "cannot silently" |
| 32639-32644 | p_0, check R_j, ε_j and δ_j | definition | The deposit scale, power-of-L localization/waiting scale and presentation-defined frame thresholds are fixed across each source family. | definition | A_0; exponent mathfrak p_0; presentation section | "they are fixed" |
| 32650-32653 | E^(j), R^(j), B^(j) and pointed companions | definition | Regular, remainder and boundary activities may carry base points and require a separately specified infinite-lattice companion. | definition | Local domains; infinite lattice | "a finite-torus total alone does not define it" |
| 32654-32659 | b(E), e_j, mathcal E and vacuum E | definition | The conditional pointed-member extractor is distinct from localized source energies, their sum and the vacuum normalization. | definition | ph:extractor; Requirement B2 | "under Requirement B2's conditional" |
| 32660-32664 | d_j(X), κ and κ_D | definition | Domain size or spanning length, decay exponent and domain-counting exponent describe local-family summation. | definition | Localization domains in level-j cubes | "is a domain-counting exponent" |
| 32663-32664 | Decay versus entropy | requirement | Summing mixed derivatives across separated source supports requires decay stronger than the declared domain entropy. | assumed | κ; κ_D; separated supports | "only when the declared decay beats that entropy" |
| 32665-32669 | Ω_j, Λ_j, Z_j and Λ_j^+ | definition | History regions name the regular region, buffered interior, large-field complement and possible retained islands without supplying their geometry. | definition | Declared geometric data | "the names alone impose no such conditions" |
| 32668-32669 | History geometry formation data | requirement | Exact inclusions, buffers, tower maps and map domains must be part of the declared geometric data. | assumed | Ω_j; Λ_j; Z_j; Λ_j^+ | "declared geometric data" |
| 32670-32674 | h, underlined h and ω | definition | Full, standing and local histories are distinguished, and a standing-history measure need not be a predetermined block-variable law after healing. | definition | Absorbed inner outcomes; healing operation | "records its standing data" |
| 32675-32680 | Ξ_ω, μ_ω, Φ_ω and Ψ_ω | definition | Stored integration spaces and positive reference measures carry external-variable and source exponents with bounds taken on the domains required by induction. | definition | Stored and external variables; mass integral | "reference measure" |
| 32681-32685 | Θ(h), q_a and Σ_k | definition | Prepaid history weights, age survival and weighted-domain aged load are distinguished, with survival affecting output bounds rather than input analytic radii. | definition | Deposits; space-time volume; weighted-domain section | "does not by itself enlarge a complex input radius" |
| 32686-32691 | C_k, U_j^c and independent current | definition | Complete presentation classes and complex pair domains distinguish an independent current coordinate from the current of its field. | definition | Formation data; structural clauses | "An independent current is a coordinate in the pair" |
| 32688-32691 | Presentation membership and closure | requirement | Membership requires every structural clause, map and estimate, and notation alone proves no closure theorem. | assumed | Complete formation data | "Membership requires all declared structural clauses, maps and estimates" |
| 32692-32699 | G_z, K_z, A_z and own-member counterterm | definition | A member's pointed total, free-response Hessian and unit-extractor midpoint tent action use that same member's coefficient even when other sites use other members. | definition | Actual free response; ph:tent-action; ph:own-counterterm | "uses the coefficient of that same member" |
| 32700-32704 | Window-proof rho, sigma, a, a_out and α | definition | The window proof uses a field-radius ratio and scale ratio, with a Hölder exponent distinct from an analyticity radius. | definition | Window proof; α_{i,j} | "is a ratio of field radii" |
| 32705-32706 | Young-age fallback | estimate | The ordinary quadratic radius-ratio bound supplies a finite young-age fallback. | sketched | rho²≤C(1+n−j) | "gives the finite" |
| 32706 | Whole-core membership | requirement | Actual membership of the whole core remains necessary in the window argument. | assumed | Window proof; young-age fallback | "Actual whole-core membership is still required" |
| 32707-32712 | OSF and OH | definition | OSF concerns given source/history objects, while OH concerns complex label measures positive at zero and uses a site count unrelated to gauge N. | definition | ch:ordinary-source-formation-audit; ch:ordinary-history-stability | "positive at zero" |
| 32713-32714 | OH stability/floor inputs | hypothesis | The weighted label sum and all-small-field action bound are inputs to the stability/floor implication rather than consequences of summation. | assumed | OH; τ_S(w) | "not supplied by the final sum" |
| 32715-32718 | Formation map T and inserted potential W_f | definition | A holomorphic potential-norm formation map uses a source potential of size O(α² times the supremum norm of f). | definition | Complex field domain; potential-norm ball | "is a holomorphic formation map" |
| 32719-32724 | Insertion potential norm and analytic room | requirement | Finite insertion and response bootstrap require the potential norm and actual substitution room, which a bare-weight coefficient bound does not imply. | assumed | ch:finite-source-insertion; ch:linear-source-bootstrap; sec:substitution-room | "does not imply this potential bound" |
| 32725-32729 | E(z), E_{ℓ,K} and A_K | definition | Transfer distinguishes a common cell normalizer, a finite-torus vacuum constant and a hypothetical common companion density that may diverge with K. | definition | Transfer lemma; ET8--ET10 | "its hypothetical common companion density" |
| 32730-32731 | Optional finite-reference companion route | remark | Companion comparison is unnecessary if an infinite reference already has D1's common all-state normalizer. | assumed | D1; infinite reference sharing its normalizer | "unnecessary" |
| 32737-32740 | S and σ | definition | Separated test tuples include the empty tuple, allow concatenation only with separated supports and carry a moment functional distinct from connected correlations. | definition | Test supports | "a moment functional, not the connected family itself" |
| 32741-32747 | V^1(A), d(X) and D_L | definition | Compactly supported real C^1 test charts use minimum support separation and the dense lattice translation subgroup, with conventions for empty supports and zero entries. | definition | a_K; sets at positive mutual distance | "A separated-tuple chart is a product of these" |
| 32748-32755 | σ_S and two-state centering | definition | The centered partition sum omits singleton blocks, while centering in another state may leave a linear first moment and preserves the integrating state's higher cumulants. | definition | Connected family S; integrating state rho; centering state nu | "not necessarily in its integrating state" |
| 32756-32760 | S_ne and Schwartz seminorm | definition | Diagonal-flat Schwartz tests vanish with every derivative on coincidence diagonals and use weighted derivative seminorms. | definition | Coincidence diagonals; multi-indices | "flat" |
| 32761-32766 | GS geometry, m(X), X^+ and GS1--GS3 | definition | Cubical localization has a minimal meeting-tree size and fixed-layer source enlargement, with three sharper counts not implied by ST6. | definition | Ma_s cubes; GS1--GS3; ST6 | "Their sharper geometry is not implied" |
| 32767-32771 | D2, k and B(R) | requirement | D2 is the graded all-state moment/cumulant requirement with quartic radius growth, fixed factorial exponent and n-dependent separation power. | definition | thm:graded-rooted-source; D1 in actual geometry; G1 | "requirement derived in Theorem" |
| 32772-32775 | H1, k_E and κ_E | requirement | D2 yields diagonal-flat growth with k_E=20, κ_E=k+32 and seminorm order 20n through the named extension theorem. | definition | D2; thm:quantitative-flat-extension | "requirement derived from D2" |
| 32776-32778 | QF proof scope | remark | The cited proof covers constrained tensor density at diagonals, infinity and the positive-time boundary but supplies neither D1 nor extension across diagonals. | named open | QF proof; D1 | "It does not prove the ordinary" |
| 32779-32786 | UI, PD, p and wp | definition | UI gives a field-count-independent gap insertion exponent and PD gives analytic L^1 plate density with exponent wp=p+5 and compatible padded operators. | definition | thm:uniform-one-field-insertion; thm:plate-density-from-insertion; ordinary repeated-source input | "These follow from the ordinary repeated-source input" |
| 32785-32786 | UI/PD input distinction | requirement | The ordinary repeated-source input is needed for UI and PD because graded moment bounds alone do not supply them. | assumed | Ordinary repeated-source input; graded moment bounds | "from graded moment bounds alone" |
| 32787-32797 | G_{φ,ψ}, μ_φ, Γ_φ, L_s and local ν | definition | Transverse-smearing kernels use positive cone-supported spectral measures, finite positive-time Laplace transforms and boosts, with diagonal-frame ν distinguished from a Gibbs state. | definition | Real compact labels; coordinate spectral representation; TU27 | "coordinate spectral measure is the positive measure" |
| 32798-32806 | UV shape class, theta_* and TU10 | hypothesis | The ultraviolet theorem assumes a uniformly vanishing error over the full TU9 shape class with theta_*=1/12000 and an explicit test-mass bound. | assumed | TU9; TU10; u(d)→0; positions; approximating states; F2--F3 with matching quantifiers | "Its input is (TU10)" |
| 32802-32806 | Positive-shape mass requirement | requirement | Each nonnegative radius-d test must satisfy the explicit integral lower bound in addition to Lipschitz and separation bounds. | assumed | ∫f≥theta_* d^4 times supremum norm of f | "It is not inferred from the Lipschitz condition alone" |
| 32807-32810 | Angular c_m and b_n | definition | Angular coefficients acquire phase e^{4imt}, and b_n records the largest absolute nonzero nonconstant frequency or zero. | definition | Rotated configurations R_t y; angular expansion | "with value zero when there is none" |
| 32809-32810 | Frequency reduction and UV conclusion | proof | Polygon divisibility and convexity give b_{2k}=kb_2, and the ultraviolet argument gives b_2=0. | sketched | Polygon divisibility; convexity; ultraviolet argument | "the ultraviolet argument gives" |
| 32811-32815 | G2 derived scalar rotation | requirement | G2 is the scalar rotation requirement derived by UI--PD--AK--UV--HC for periodic limits and canonical components carrying the specified interface. | definition | D1 in rooted geometry; G1; exact cube cone; ultraviolet law; UI--PD--AK--UV--HC | "the derived scalar rotation requirement" |
| 32816-32818 | Growing-torus and stronger retained routes | requirement | Arbitrary growing cubic-torus limits need their own mirror/cone proof, while stronger retained routes still need typed Ward and matched-cutoff estimates. | named open | Growing cubic-torus limits; typed Ward estimates; matched-cutoff estimates | "require their own mirror/cone" |
| 32819-32828 | G^per, G^tor and G^ex | definition | Periodic DLR states, weak limits of lifted torus measures and translation-ergodic periodic members form distinct classes, also distinct from tuned full sequences. | definition | ch:continuum-compactness; fixed spacing and coupling | "have distinct definitions in" |
| 32825-32826 | Finite periodic lifts and DLR | remark | A periodically lifted finite-torus measure is not asserted to be an infinite-volume DLR measure before passage to the limit. | assumed | Periodic lift; volume limit | "is not asserted to be" |
| 32829-32836 | Common periodization chart f^(ℓ) | construction | Periodization on a single ball containing every support with R<ℓ/4 preserves relevant distances and norms, unlike separately positioned small balls. | definition | π_ℓ; common Euclidean support ball | "periodization is defined by" |
| 32837-32842 | G_j, E_j and D_j | definition | The compact invariant DLR class has an ergodic class-extreme subset and a centering-state decomposition law from the invariant sigma-field. | definition | Fixed spacing and coupling; invariant sigma-field | "equivalently class-extreme" |
| 32843-32848 | I, Pl_ν and N_{ν,r} | definition | The invariant sigma-field defines a plateau inner product of conditional expectations, while G3's reflected size replaces divergent cutoff-product supremum norms. | definition | Upstream lattice law G3; conditional expectations | "in the upstream lattice law G3" |
| 32849-32853 | Phase X, λ and σ_ξ | construction | The conditional phase theorem constructs compact full-support phase coordinates, their probability law and continuous component evaluations from lattice evaluation limits. | sketched | Conditional phase theorem; weak limits of lattice evaluation laws | "conclusions of the conditional phase theorem" |
| 32854-32858 | θ, H-space, H, P, Ω and P_0 | definition | Reflection positivity defines the completed quotient and vacuum, with time and momentum generators when their groups exist and P_0 projecting onto ker H. | definition | Positive form; constructed continuous groups | "when the corresponding" |
| 32859-32862 | U, B and W_4 | definition | Ward rotation defects or fluxes and their insertions are distinguished from signed coordinate permutations, whose invariance alone is weaker than O(4) invariance. | definition | Ward argument; signed coordinate permutations | "does not imply invariance under" |
| 32871-32875 | Argument-index scope | definition | Code families locate retained statements, referenced proofs and outstanding tasks whose exact forms remain in the cited statements and dependency catalogue. | definition | Cited statements; dependency catalogue | "Their exact forms are given at the" |
| 32877-32879 | Named outline statement identifiers | definition | The index lists identifiers without restating their assertions or assigning individual proof statuses. | definition | 0; 1; 1a.1.1; 1a.1.10; 1a.1.11; 1a.1.12; 1a.1.13; 1a.1.14; 1a.1.2; 1a.1.3; 1a.1.4; 1a.1.5; 1a.1.6; 1a.1.7; 1a.1.9; 1a.2.1; 1a.2.10; 1a.2.2; 1a.2.3; 1a.2.4; 1a.2.7; 1a.2.8; 1a.2.9; 1a.3.1; 1a.3.11; 1a.3.12; 1a.3.13; 1a.3.3; 1a.3.4; 1a.3.6; 1a.3.7; 1a.3.8; 1a.3.9; 2; 2.1; 2.11; 2.2; 2.3; 2.4; 2.5; 2.6; 2.7; 3; 3.1; 3.2; 3.3; 3.4; 3.5; 3.6; 3.7; 3.8; 3.9; 4; 4.1; 4.13; 4.14; 4.15; 4.2; 4.3; 4.4; 4.5; 4.6; 4.7; 5; 6; 7.1; 7.2; 7.3; 7.4 | "Named statements in the proof outline" |
| 32881-32883 | 4.10 proof locator | definition | The detailed proof of chessboard domination for arbitrary periodic states is located in the all-state source-transfer section. | definition | 4.10; ch:all-state-source-transfer | "Detailed proofs of referenced statements" |
| 32885 | 4.12 proof locator | definition | The detailed proof of uniform one-point differences is located in the all-state source-transfer section. | definition | 4.12; ch:all-state-source-transfer | "uniform one-point differences" |
| 32887 | 4.17 proof locator | definition | The detailed proof of uniform one-field Hilbert insertion is located in the uniform-insertion section. | definition | 4.17; ch:uniform-insertion | "uniform one-field Hilbert insertion" |
| 32889 | 4.18 proof locator | definition | The detailed proof of analytic insertion density and the conditional plate-bound implication is located in the plate-density section. | definition | 4.18; stated hypotheses; ch:plate-density-from-insertion | "under its stated hypotheses" |
| 32893-32895 | Ordinary history/source outlines, 2.8, 2.10, 2.13, 4.11 | proof | Outlines for four history/source tasks are supplied in the actual-history-closure and actual-ordinary-source-proof sections. | sketched | sec:actual-history-closure; sec:actual-ordinary-source-proof | "proof outlines in Sections~" |
| 32895-32898 | Extraction/transfer outlines, 7.5, 7.6, 7a.1.8 | proof | The extraction and transfer tasks are developed in the clean-box through Gaussian-segment sections and finite-reference-normalizer section. | sketched | ym4:new-clean-box through ym4:new-gaussian-segment; sec:finite-reference-normalizer; 32907 identifies these as outlines | "the locations of the supplied outlines" |
| 32898-32900 | Stronger aged comparison 2.12 | requirement | The stronger aged comparison remains a separate outstanding task from the supplied ordinary-history and source outlines. | named open | Package C; 2.12 | "comparison 2.12 remains separate" |
| 32899-32900 | One-loop calculation locator | definition | The one-loop calculation is located in the new-one-loop-reduction section. | definition | ym4:new-one-loop-reduction | "The one-loop calculation is in" |
| 32902-32904 | Package E: Bałaban's Theorem 8 | theorem | One use of code 8 denotes Bałaban's unproved Theorem 8, which the outline still undertakes to prove. | named open | Bałaban's Theorem 8; no particular source identified here for this theorem | "states without proof and which we must prove" |
| 32902-32904 | Package E: Proposition 8 | proposition | The other use of code 8 cites Proposition 8 of Bałaban's 1985 variational-problem paper. | cited | Bałaban, The variational problem and background fields in renormalization group method for lattice gauge theories, CMP 102 (1985), 277–309 (B85e) | "which is cited" |
| 32904-32906 | Package A--H: Proposition 1.2 | proposition | Code 1.2 cites Proposition 1.2 of Bałaban's first propagator and renormalization paper. | cited | Bałaban, Propagators and renormalization transformations for lattice gauge theories. I, CMP 95 (1984), 17–40 (B84a) | "which is cited" |
| 32909 | Package A: 1a.3.2 | requirement | Package A lists task 1a.3.2 among statements still to be proved without restating its content. | named open | 1a.3.2; cited statement and dependency catalogue | "Statements still to be proved, by package" |
| 32909 | Package A: 1a.3.5 | requirement | Package A lists task 1a.3.5 among statements still to be proved without restating its content. | named open | 1a.3.5; cited statement and dependency catalogue | "Statements still to be proved, by package" |
| 32911 | Package C: 2.10 | requirement | Package C retains task 2.10 as an outstanding ordinary-history/source obligation despite the supplied outline. | named open | 2.10; sec:actual-history-closure; sec:actual-ordinary-source-proof | "Statements still to be proved, by package" |
| 32911 | Package C: 2.12 | requirement | Package C retains the stronger aged comparison 2.12 as outstanding. | named open | 2.12; separate stronger aged comparison | "Statements still to be proved, by package" |
| 32911 | Package C: 2.13 | requirement | Package C retains task 2.13 as an outstanding ordinary-history/source obligation despite the supplied outline. | named open | 2.13; sec:actual-history-closure; sec:actual-ordinary-source-proof | "Statements still to be proved, by package" |
| 32911 | Package C: 2.8 | requirement | Package C retains task 2.8 as an outstanding ordinary-history/source obligation despite the supplied outline. | named open | 2.8; sec:actual-history-closure; sec:actual-ordinary-source-proof | "Statements still to be proved, by package" |
| 32913 | Package D: 4.11 | requirement | Package D retains source task 4.11 as outstanding despite the supplied outline. | named open | 4.11; sec:actual-history-closure; sec:actual-ordinary-source-proof | "Statements still to be proved, by package" |
| 32915 | Package E: code 8 retained task | requirement | Package E retains code 8, with the outstanding theorem distinguished above from the cited proposition sharing its number. | named open | Bałaban's Theorem 8; distinction at 32902-32904 | "Statements still to be proved, by package" |
| 32917 | Package F: 7.5 | requirement | Package F retains extraction/transfer task 7.5 as outstanding despite its development elsewhere. | named open | 7.5; clean-box through Gaussian-segment sections; finite-reference-normalizer section | "Statements still to be proved, by package" |
| 32917 | Package F: 7.6 | requirement | Package F retains extraction/transfer task 7.6 as outstanding despite its development elsewhere. | named open | 7.6; clean-box through Gaussian-segment sections; finite-reference-normalizer section | "Statements still to be proved, by package" |
| 32917 | Package F: 7a.1.8 | requirement | Package F retains extraction/transfer task 7a.1.8 as outstanding despite its development elsewhere. | named open | 7a.1.8; clean-box through Gaussian-segment sections; finite-reference-normalizer section | "Statements still to be proved, by package" |
| 32919 | Package G: 9.1 | requirement | Package G lists task 9.1 as outstanding without restating its content. | named open | 9.1; cited statement and dependency catalogue | "Statements still to be proved, by package" |
| 32919 | Package G: 9.10 | requirement | Package G lists task 9.10 as outstanding without restating its content. | named open | 9.10; cited statement and dependency catalogue | "Statements still to be proved, by package" |
| 32919 | Package G: 9.11 | requirement | Package G lists task 9.11 as outstanding without restating its content. | named open | 9.11; cited statement and dependency catalogue | "Statements still to be proved, by package" |
| 32919 | Package G: 9.3 | requirement | Package G lists task 9.3 as outstanding without restating its content. | named open | 9.3; cited statement and dependency catalogue | "Statements still to be proved, by package" |
| 32919 | Package G: 9.7 | requirement | Package G lists task 9.7 as outstanding without restating its content. | named open | 9.7; cited statement and dependency catalogue | "Statements still to be proved, by package" |
| 32921 | Package A--H: retained identifier 1.2 | proposition | The package list retains 1.2 even though the preceding explanation classifies its proposition as cited. | cited | Bałaban, Propagators and renormalization transformations for lattice gauge theories. I, CMP 95 (1984), 17–40 (B84a); 32904-32907 | "The following list retains the task identifiers" |
| 32921 | Package A--H: 1.6 | requirement | Package A--H lists task 1.6 as outstanding without restating its content. | named open | 1.6; cited statement and dependency catalogue | "Statements still to be proved, by package" |
| 32925-32929 | Hand-numbered theme codes | definition | The first code component assigns backgrounds/propagators to 1a–1c, local interactions to 1d–1e, histories to 2, flow to 3, sources to 4, limits to 5, Euclidean structure to 6, short distance to 7, comparison to 8, rotations to 9 and phases/reconstruction to 10. | definition | Hand-numbered codes across book sections | "records its mathematical theme" |
| 32929-32930 | Grouped-reference scope | requirement | Grouped references retain the hypotheses and scope of the referenced result. | assumed | Stated result | "read with the hypotheses and scope of its stated result" |

## Forward and backward references

These entries record the chunk's locators without inspecting their targets; bare symbol definitions and proof locators in the table do not assert that a proof is written in this chunk.

- 32466-32476: HB quotient hypotheses and local C^1 continuity are the existing inputs for the spatial action; full scalar rotation invariance must be supplied.
- 32477-32480: HB's cube inequalities, for limits where already established, supply the cone argument.
- 32481-32485: `ch:euclidean-hilbert-bridge` proves the centering map C_m used to identify sh_ξ and its inverse.
- 32487-32490: External OS reconstruction, F4 identification and mass-gap estimates are separate; the periodic-state angular proof retains its mirror/cone/ultraviolet interface, and the optional Ward premises are “above.”
- 32499-32504: Analytic domains and history data are defined in the technical sections; hand-numbered candidate-argument notation refers to this index and the corresponding detailed definitions.
- 32517-32520: The graded ordinary-source argument uses the specified compatible torus family and preselected geometric constants.
- 32557-32558: The relevant theorem determines the cochain conventions of d_0 and d_1.
- 32567-32568: The block-normalization section proves the unitary conversion between inner-product conventions.
- 32583-32585: Background obligations A1--A4 govern existence, domains, gauges and bounds; the proved scalar model supplies only part.
- 32586-32595: `ch:pointed-window-remainder` defines B and the actual background pair Φ_Λ(B), with the product-polydisc response and weighted comparison interface.
- 32603-32604: The arithmetic theorem does not assume positivity of each actual b_j.
- 32605-32608: The numerical first-passage theorem assumes the one-loop interval sum law and error envelope rather than calculating c_0.
- 32611-32615: The technical frame estimates use the frozen auxiliary coupling; calibrated holomorphy and cutoff comparison are additional analytic assertions.
- 32629-32633: The source domain section specifies the anchor support and normalization of h_y^(j) and defines ζ_j by the exact counterterm identity.
- 32634-32638: The respective source/coupling-disc statements and complex field domains specify the radii used in extraction.
- 32639-32644: The presentation section defines ε_j and δ_j; check R_j is the specified localization/waiting scale.
- 32654-32657: `ph:extractor` defines b(E) under Requirement B2's conditional hypotheses.
- 32668-32669: Declared geometric data supply inclusions, buffers, tower maps and their domains.
- 32679-32680: The induction determines the domains and placement under the mass integral of the required suprema and oscillations.
- 32681-32685: The weighted-domain section defines the aged load Σ_k.
- 32686-32691: The declared formation data supply the structural clauses, maps and estimates for presentation membership and closure.
- 32696-32699: `ph:tent-action` defines A_z; `ph:own-counterterm` uses the same pointed member's coefficient.
- 32700-32706: The window proof supplies the radius and scale ratios, local Hölder exponent and ordinary age bound, while requiring actual whole-core membership.
- 32707-32714: `ch:ordinary-source-formation-audit` handles given members, defects, remainders and histories; `ch:ordinary-history-stability` handles complex label measures and assumes the weighted label sum and small-field action bound.
- 32715-32724: The response lemma's potential norm is used in `ch:finite-source-insertion` and `ch:linear-source-bootstrap`, with analytic room described in `sec:substitution-room`.
- 32725-32731: The transfer lemma distinguishes normalizers; ET8--ET10 posit the companion density A_K, while D1's common all-state normalizer can make the finite-reference comparison unnecessary.
- 32761-32766: GS1--GS3 provide rooted, local ball-root and global weighted counts; the weaker ST6 count does not supply that geometry.
- 32767-32771: `thm:graded-rooted-source` derives D2 from D1 in actual geometry and G1.
- 32772-32778: `thm:quantitative-flat-extension` derives H1 from D2; the QF proof includes constrained tensor density but does not prove D1 or extension across diagonals.
- 32779-32786: `thm:uniform-one-field-insertion` is UI and `thm:plate-density-from-insertion` is PD; both use the ordinary repeated-source input, not merely graded moment bounds.
- 32794-32797: The spectral proof uses L_s and a diagonal-frame ν whose cone support is proved from TU27's identity of measures.
- 32798-32806: The ultraviolet theorem fixes the TU9 shape class and assumes TU10 uniformly over shapes, positions and approximating states; F2--F3 imply the input only with matching quantifiers.
- 32807-32810: Polygon divisibility and convexity yield the frequency relation, and the ultraviolet argument yields b_2=0.
- 32811-32818: UI--PD--AK--UV--HC derives G2 under D1 in rooted geometry, G1, the exact cube cone and the stated ultraviolet law; growing-torus and stronger retained routes retain separate interfaces.
- 32819-32828: `ch:continuum-compactness` separately defines the periodic and torus classes, growing-torus limits and conditionally tuned full sequences.
- 32835-32836: The moment estimates use a separate, position-uniform radius convention rather than the common periodization chart.
- 32843-32848: Upstream lattice law G3 defines the reflected size N_{ν,r} used in the phase limit.
- 32849-32853: The conditional phase theorem constructs X, λ and σ_ξ from lattice evaluation laws.
- 32854-32858: H and P refer to generators only once their corresponding continuous groups have been constructed.
- 32859-32862: The Ward argument uses U for a rotation defect or limiting flux and B for its insertion.
- 32871-32875: The cited statements and dependency catalogue give the exact forms of the indexed code families; supporting outlines remain distinct from obligations.
- 32877-32879: The “Named statements in the proof outline” list points to every identifier reproduced in the corresponding table row, without restating content or asserting individual proof status.
- 32881-32883: Detailed proof of 4.10, chessboard domination for arbitrary periodic states → `ch:all-state-source-transfer`.
- 32885: Detailed proof of 4.12, uniform one-point differences → `ch:all-state-source-transfer`.
- 32887: Detailed proof of 4.17, uniform one-field Hilbert insertion → `ch:uniform-insertion`.
- 32889: Detailed proof of 4.18, analytic insertion density and conditional plate-bound implication → `ch:plate-density-from-insertion`.
- 32893-32895: Outlines for 2.8, 2.10, 2.13 and 4.11 → `sec:actual-history-closure` and `sec:actual-ordinary-source-proof` (no individual assignment is given).
- 32895-32898: Development of 7.5, 7.6 and 7a.1.8 → `ym4:new-clean-box` through `ym4:new-gaussian-segment`, and `sec:finite-reference-normalizer` (no individual assignment is given).
- 32898-32899: Stronger aged comparison 2.12 remains separate from those outlines.
- 32899-32900: One-loop calculation → `ym4:new-one-loop-reduction`.
- 32902-32904: Package E code 8 denotes both Bałaban's Theorem 8, stated without proof, and cited Proposition 8 of CMP 102 (1985), 277–309 (B85e, bibliography 32957); no specific source for Theorem 8 is identified in this passage.
- 32904-32907: Package A--H code 1.2 → cited Proposition 1.2 of CMP 95 (1984), 17–40 (B84a, bibliography 32945); the retained task list must be read with this qualification and the preceding outline locations.
- 32909-32921: Package identifiers point to their statements and dependency-catalogue entries: A (1a.3.2, 1a.3.5), C (2.10, 2.12, 2.13, 2.8), D (4.11), E (8), F (7.5, 7.6, 7a.1.8), G (9.1, 9.10, 9.11, 9.3, 9.7), A--H (1.2, 1.6).
- 32925-32930: Code themes persist across separate book sections, and grouped references retain the referenced result's hypotheses and scope.

The remaining source lines supply bibliography targets, not additional mathematical assertions or proofs:

| Lines | Bibliography key | Work identified here |
|---|---|---|
| 32937 | B82a | T. Bałaban, (Higgs)₂,₃ quantum fields in a finite volume. I. A lower bound, CMP 85 (1982), 603–626. |
| 32939 | B82b | T. Bałaban, (Higgs)₂,₃ quantum fields in a finite volume. II. An upper bound, CMP 86 (1982), 555–594. |
| 32941 | B83a | T. Bałaban, (Higgs)₂,₃ quantum fields in a finite volume. III. Renormalization, CMP 88 (1983), 411–445. |
| 32943 | B83b | T. Bałaban, Regularity and decay of lattice Green's functions, CMP 89 (1983), 571–597. |
| 32945 | B84a | T. Bałaban, Propagators and renormalization transformations for lattice gauge theories. I, CMP 95 (1984), 17–40. |
| 32947 | B84b | T. Bałaban, Propagators and renormalization transformations for lattice gauge theories. II, CMP 96 (1984), 223–250. |
| 32949 | B85a | T. Bałaban, Averaging operations for lattice gauge theories, CMP 98 (1985), 17–51. |
| 32951 | B85b | T. Bałaban, Spaces of regular gauge field configurations on a lattice and gauge fixing conditions, CMP 99 (1985), 75–102. |
| 32953 | B85c | T. Bałaban, Propagators for lattice gauge theories in a background field, CMP 99 (1985), 389–434. |
| 32955 | B85d | T. Bałaban, Ultraviolet stability of three-dimensional lattice pure gauge field theories, CMP 102 (1985), 255–275. |
| 32957 | B85e | T. Bałaban, The variational problem and background fields in renormalization group method for lattice gauge theories, CMP 102 (1985), 277–309. |
| 32959 | B87 | T. Bałaban, Renormalization group approach to lattice gauge field theories. I. Generation of effective actions in a small field approximation and a coupling constant renormalization in four dimensions, CMP 109 (1987), 249–301. |
| 32961 | B88a | T. Bałaban, Renormalization group approach to lattice gauge field theories. II. Cluster expansions, CMP 116 (1988), 1–22. |
| 32963 | B88b | T. Bałaban, Convergent renormalization expansions for lattice gauge theories, CMP 119 (1988), 243–285. |
| 32965 | B89a | T. Bałaban, Large field renormalization. I. The basic step of the R operation, CMP 122 (1989), 175–202. |
| 32967 | B89b | T. Bałaban, Large field renormalization. II. Localization, exponentiation, and bounds for the R operation, CMP 122 (1989), 355–392. |
| 32969 | Wilson74 | K. G. Wilson, Confinement of quarks, Physical Review D 10 (1974), 2445–2459. |
| 32971 | OS73 | K. Osterwalder and R. Schrader, Axioms for Euclidean Green's functions, CMP 31 (1973), 83–112. |
| 32973 | OS75 | K. Osterwalder and R. Schrader, Axioms for Euclidean Green's functions II, CMP 42 (1975), 281–305. |
| 32975 | OSeiler78 | K. Osterwalder and E. Seiler, Gauge field theories on a lattice, Annals of Physics 110 (1978), 440–471. |
| 32977 | FILS78 | J. Fröhlich, R. Israel, E. H. Lieb and B. Simon, Phase transitions and reflection positivity. I. General theory and long range lattice models, CMP 62 (1978), 1–34. |
| 32979 | KP86 | R. Kotecký and D. Preiss, Cluster expansion for abstract polymer models, CMP 103 (1986), 491–498. |
| 32981 | JW | A. Jaffe and E. Witten, Quantum Yang–Mills theory, Clay Mathematics Institute official problem description. |
| 32983-32986 | Kallenberg2002 (display label Kallenberg02) | O. Kallenberg, Foundations of Modern Probability, second edition, Springer, 2002. |

## Obligations named here

- 32466-32469: Supply full scalar rotation invariance before asserting the HB spatial action.
- 32477-32480: Establish HB cube inequalities for the limit to which the round-cone argument is applied.
- 32486: A general time-mixing Euclidean rotation operator is not asserted.
- 32487-32488: External OS reconstruction remains separate.
- 32487-32488: F4 identification of the full theory remains separate.
- 32488: Any mass-gap estimate remains separate.
- 32488-32490: Retain the periodic angular proof's mirror, cone and ultraviolet interface; optional Ward premises do not enlarge its state class.
- 32501-32503: Supply the type and required estimates of every uninstantiated auxiliary map; notation does not establish existence.
- 32512-32513: Specify the matrix group and trace convention in statements retaining N.
- 32514-32520: Use the cofinal compatible tori for the graded ordinary-source argument and fix M_1, M_2 and buffers before cutoffs, fields and sources.
- 32554-32556: Use both source and target inner products in every adjoint.
- 32583-32585: Prove background obligations A1--A4, including existence, analytic domains, gauges and uniform bounds beyond the scalar model.
- 32590-32591: Maintain the response bound throughout the full product datum polydisc, not merely at zero.
- 32594-32595: Use actual compatible equations and boundary rows with their natural force norms and cell weights in finite-box comparison.
- 32607-32608: Provide the one-loop interval sum law and error envelope assumed by the numerical first-passage theorem; it does not compute c_0.
- 32614-32615: Supply calibrated-coordinate holomorphy and comparison across cutoffs as additional analytic assertions.
- 32622-32623: Make physical quantities depend only on the relevant plaquette values, independent of source-triple representation.
- 32629-32633: Use the source-domain partition data and exact-counterterm definition of ζ_j rather than choosing another bare coupling.
- 32637-32638: Do not silently replace a coefficient-extraction radius by a smaller running radius.
- 32642-32644: Keep the prescribed curvature and fluctuation thresholds fixed throughout each source family.
- 32651-32653: Specify an infinite-lattice companion; a finite-torus total does not define one.
- 32654-32657: Meet Requirement B2's conditional hypotheses when using the actual-member extractor `ph:extractor`.
- 32663-32664: Require decay stronger than domain-counting entropy when summing mixed derivatives across separated supports.
- 32668-32669: Declare exact history-region inclusions, buffers, tower maps and domains; region names alone impose none.
- 32673-32674: Do not identify a standing-history measure with a predetermined block-variable law after healing without additional justification.
- 32679-32680: Take suprema and oscillations on the stated domains under the mass integral when required by the induction.
- 32684-32685: Do not use an age-survival probability alone to enlarge the complex input radius.
- 32688-32691: Supply all structural clauses, maps, estimates and formation data for presentation membership and any closure theorem.
- 32689-32690: Do not automatically identify the independent current coordinate with the current evaluated on its field.
- 32696-32699: Use the coefficient of the same pointed member in `ph:own-counterterm` despite possible sitewise changes of members.
- 32706: Verify actual whole-core membership even when using the young-age fallback.
- 32713-32714: Supply the weighted label sum and all-small-field action bound as inputs to OH's stability/floor implication.
- 32719-32724: Supply the potential-norm bound and actual substitution room for insertion/response bootstrap; an ordinary bare-weight coefficient bound does not imply them.
- 32725-32731: The finite-reference ET8--ET10 route requires the hypothetical common companion density; that comparison is unnecessary when an infinite reference already shares D1's all-state normalizer.
- 32761-32766: Supply the actual GS1--GS3 geometry and counts; ST6 alone does not imply them.
- 32767-32771: The D2 derivation requires D1 in actual geometry and G1.
- 32772-32778: The H1 extension theorem uses D2; its QF proof does not establish D1 or extend tests across diagonals.
- 32779-32786: Supply the ordinary repeated-source input for UI and PD; graded moment bounds alone do not suffice.
- 32798-32801: Supply TU10 with vanishing u(d), uniformly over the full TU9 shape class, positions and approximating states.
- 32802-32806: Enforce the explicit positive-shape mass lower bound as well as Lipschitz and separation bounds; F2--F3 must use the same quantifiers.
- 32811-32815: Apply derived G2 only under D1 in actual rooted geometry, G1, the exact cube cone and the ultraviolet law, for states/components carrying that interface.
- 32816-32817: Give arbitrary growing cubic-torus limits their own mirror/cone justification.
- 32817-32818: Supply typed Ward and matched-cutoff estimates for the stronger retained routes using them.
- 32825-32826: A finite periodic lift is not asserted to be an infinite-volume DLR measure before the limit.
- 32829-32836: Use a common support ball of radius R<ℓ/4 for periodization to preserve distances and norms; separate small balls do not suffice.
- 32840-32842: Unrestricted DLR extremality is not identified here with extremality inside the translation-invariant class.
- 32849-32853: The phase coordinates, law and evaluations must come from the conditional phase theorem, rather than being assumed continuum data.
- 32854-32858: Construct the corresponding continuous groups before using their generators H and P.
- 32859-32862: Signed-permutation W_4 invariance alone does not supply O(4) invariance.
- 32871-32875: Keep outlined supporting arguments distinct from the outstanding obligations whose exact forms are in their statements and the dependency catalogue.
- 32893-32895, 32911: Task 2.8 remains listed for proof despite its ordinary history/source outline.
- 32893-32895, 32911: Task 2.10 remains listed for proof despite its ordinary history/source outline.
- 32893-32895, 32911: Task 2.13 remains listed for proof despite its ordinary history/source outline.
- 32893-32895, 32913: Task 4.11 remains listed for proof despite its ordinary history/source outline.
- 32895-32898, 32917: Task 7.5 remains listed for proof despite its extraction/transfer development.
- 32895-32898, 32917: Task 7.6 remains listed for proof despite its extraction/transfer development.
- 32895-32898, 32917: Task 7a.1.8 remains listed for proof despite its extraction/transfer development.
- 32898-32899, 32911: Stronger aged comparison 2.12 remains a separate obligation.
- 32902-32904, 32915: Prove Bałaban's Theorem 8, which he states without proof; distinguish it from cited Proposition 8 of B85e.
- 32909: Package A task 1a.3.2 remains listed for proof.
- 32909: Package A task 1a.3.5 remains listed for proof.
- 32919: Package G task 9.1 remains listed for proof.
- 32919: Package G task 9.10 remains listed for proof.
- 32919: Package G task 9.11 remains listed for proof.
- 32919: Package G task 9.3 remains listed for proof.
- 32919: Package G task 9.7 remains listed for proof.
- 32921: Package A--H task 1.6 remains listed for proof; the other retained identifier, 1.2, is expressly classified as cited at 32904-32906.
- 32929-32930: Read every grouped reference with the hypotheses and scope of its stated result.
