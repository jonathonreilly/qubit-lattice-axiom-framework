# Chunk 01: lines 42670-43968
Sections: No section or subsection heading occurs in this excerpt; it opens in a remark from 4.11 (42670-42722), then contains “Lattice, gauge group, configurations and the current” (42724), “Running radii and fixed exponents” (42881), “Blocks, determining sets and the averaging map” (42950), “Constrained minimisers and their response to small data” (43087), “Large-field geometry, admissible boxes and the source datum” (43208), “Consumers, their determining sets and radii” (43327), “Insufficiency of the unchanged real factor” (43527), “Cube-size floors and coupling thresholds” (43559), “Holonomies along two monotone paths” (43690), “The axial gauge of a box” (43787), and “Plaquettes of a left-perturbed configuration” (43867).

The names below preserve the source's labels, including its `4.12` prefix throughout these objects. Status records what the excerpt presents, without assessing mathematical correctness. The opening remark and final proof are incomplete at the chunk boundaries; “sketched” for the final lemma/proof means only that its complete argument is not contained here. Unnumbered displays are indexed when they define a named object, state an input, or form a separately identified argument.

| Lines | Name / tag | Kind | What it states (one plain sentence, your words) | Status here | Reads (inputs it uses, by tag or name) | Key phrase |
|---|---|---|---|---|---|---|
| 42670 | Opening G-valued-factor scope fragment | remark | The G-valued-factor clause is obtained only from premises whose antecedent precedes this chunk. | assumed | Unavailable antecedent before 42670 | "only from them" |
| 42671-42675 | Cross-tower minimiser comparison excluded | remark | Comparing minimisers across tower rules or tower regions is not supplied or needed for the reproduction proof. | named open | 4.11:thm-clause-reproduction | "comparison is not needed" |
| 42676-42678 | External-display and width-inclusion claims excluded | remark | The section makes no claim about the listed external displays or width inclusions. | named open | B-CMP109 (1.12), (1.17); B-CMP119 (2.38); B-CMP116 | "this section contains no such statement" |
| 42679-42682 | Additional complex-data existence excluded | remark | Existence of tower minimisers and currents beyond the complex data presupposed by class membership is not asserted. | named open | Previously defined classes; tower U_t and J_t | "beyond the data at which" |
| 42683-42685 | Cauchy-family completeness excluded | remark | Completeness beyond the Cauchy-family cases already listed in the reproduction proof is not asserted. | named open | 4.11:thm-clause-reproduction clause (ii) | "beyond the cases listed there" |
| 42686-42693 | Blocking-factor threshold L_fl | estimate | Any positive threshold whose square is at least sqrt(2)(1+β)ρ suffices for the reproduction theorem at odd L above it under the stated coupling ceilings. | proved conditionally | 4.11:thm-clause-reproduction; 4.11:eq-floors-ceilings-c,d | "We prove the" |
| 42695-42722 | Proof of blocking-factor existence form | proof | Squaring the threshold verifies the sole L floor and leaves the coupling ceilings to be imposed afterward. | proved conditionally | 4.11:not-floors-ceilings; 4.11:eq-floors-ceilings-a,c,d; 4.11:thm-clause-reproduction | "that theorem applies" |
| 42724-42813 | 4.12:not-lattice-configurations | definition | The section fixes lattice, group, configurations, plaquettes, one-forms, and current conventions. | definition | B-CMP109 current and operator conventions | "The following conventions are in force throughout this section" |
| 42728-42732 | Lattice and scales η, ℓ_m | definition | The fine lattice has spacing L^(-k), with block side ℓ_m=L^(m-k), in dimension d at least two. | definition | k; L | "Sites are the points of" |
| 42734-42741 | G, hermitian Lie algebra, operator norm, Ad | definition | G is a closed compact subgroup of the unitary matrices and its hermitian Lie algebra generates one-parameter subgroups. | definition | Compact Lie group G | "The group $G$ is a compact Lie group" |
| 42739-42740 | Unitary norm identities | identity | Left multiplication, right multiplication, and conjugation by G preserve the operator norm. | proved in detail | Unitarity; proof at 42857-42858 | "preserves" |
| 42741-42745 | 4.12:eq-lattice-configurations-a | estimate | A unitary element within distance one of the identity has a hermitian principal logarithm bounded by π/3 times that distance. | proved in detail | Spectral diagonalisation; sine concavity; 42815-42839 | "We first prove" |
| 42746-42747 | Local logarithm membership radius ε_G | estimate | Some group-dependent radius at most one ensures that the principal logarithm divided by i belongs to the Lie algebra. | proved in detail | Closed-subgroup theorem; local exponential chart; 42841-42855 | "We next prove the membership statement" |
| 42749-42759 | Configurations, path holonomy, gauge transformation | definition | Bond values reverse by inversion, path values multiply in order, and gauge transformations act at endpoints. | definition | G; oriented bonds | "A configuration" |
| 42757-42759 | Path covariance and gauge composition | identity | Path holonomy transforms at its two endpoints and successive gauges compose in reversed application order. | proved in detail | Gauge definition; cancellation proof at 42860-42866 | "The identities in (iii) are definitional unwindings" |
| 42761-42766 | Plaquette variable ∂U | definition | The plaquette variable is the ordered product around the specified elementary square. | definition | Path holonomy | "The plaquette" |
| 42767-42768 | Plaquette covariance and norm invariance | identity | Gauge transformations conjugate plaquette holonomy and preserve its distance from the identity. | proved in detail | Path covariance; unitary norm identity; 42868-42875 | "therefore gives" |
| 42770-42784 | One-forms, left perturbations, ∇^Y, derivative norm | definition | A hermitian Lie-algebra one-form defines a left-multiplied configuration and a gauge-covariant forward difference. | definition | G; η; Ad; configuration Y | "The covariant" |
| 42786-42791 | Current J and its normalisation | definition | J is the bond current of B-CMP109, whose sizes later provide E_3 and E_4 on the η lattice. | definition | B-CMP109 (1.8) | "The current $J(U)$" |
| 42790-42796 | J1; 4.12:eq-lattice-configurations-b | hypothesis | The norm of the current is invariant under G-valued gauge transformations. | assumed | B-CMP109 current; G-valued σ | "Both are assumed in what follows as hypotheses" |
| 42797-42808 | J2; 4.12:eq-lattice-configurations-c | hypothesis | Three scaled bounds on a one-form near a bond imply the stated cubic-scale current bound at the trivial background. | assumed | B-CMP109 (3.11)-(3.13); ℓ in [η,1]; ϖ≤1/64; two-step neighbourhood bounds | "used here by statement" |
| 42810-42812 | Second-order operator D*D | definition | D*D is the trivial-background operator from B-CMP109 used only in J2 and the response hypothesis. | definition | B-CMP109 (3.12) | "is the second-order operator" |
| 42815-42879 | Proof of lattice and group assertions | proof | Spectral estimates, a local Lie-group chart, and cancellation establish the logarithm, covariance, and configuration assertions. | proved in detail | Closed-subgroup theorem; unitarity; definitions (ii)-(v) | "Finally, in (v)" |
| 42881-42917 | 4.12:not-running-radii | definition | Running radii, fixed exponents, and large-field depth conventions are collected. | definition | Lattice conventions; B-CMP119; B-CMP122a | "Running radii" |
| 42886-42892 | 4.12:eq-running-radii-1 | definition | The level-m radius is g_m C_0 times the q_0 power of log(g_m^(-2)). | definition | B-CMP119 radius; C_0; q_0 | "denotes the radius" |
| 42892-42893 | Small-coupling monotonicity of radius | estimate | The radius increases with the coupling when the coupling is sufficiently small. | proved in detail | running-radii-1; derivative at 42924-42932 | "see the proof" |
| 42894-42897 | 4.12:eq-running-radii-a | estimate | The ratio of a later radius to an earlier one is bounded by (1+β_0) times the square root of one plus their level gap. | cited | B-CMP119 (2.6)-(2.7) | "is the bound of" |
| 42899-42905 | Fixed exponents and standing parameter conditions | hypothesis | β lies between zero and one quarter, θ_* equals 1−4β, and β_0, L_a, and L satisfy the stated bounds. | assumed | Chapter standing auxiliary-parameter conditions | "as part of those standing conditions" |
| 42907-42909 | Depth N_0, level k_0, scale R_m | definition | The large-field operation uses k_0=k−N_0 and the scale R_m from B-CMP122a. | definition | B-CMP122a (1.70) ff. | "is the depth" |
| 42910-42915 | 4.12:eq-running-radii-b | hypothesis | The depth obeys L^(N_0−1)=R_(k_0+1) and R_m has a positive logarithmic lower bound. | cited | B-CMP122a (1.70) ff.; chapter standing conditions | "These two relations are used here as stated" |
| 42916 | Uniform growth of N_0 | estimate | The infimum of the depths tends to infinity when all running couplings tend uniformly to zero. | proved conditionally | running-radii-b; fixed L; c_R,r_R>0 | "Consequently" |
| 42919-42948 | Proof of radius monotonicity and depth growth | proof | Differentiating the radius and taking logarithms of the scale lower bound establish the two asserted limits. | proved conditionally | running-radii-1,b; c_R,r_R>0 | "Only the monotonicity of the radius and the growth" |
| 42943-42945 | 4.12:eq-running-radii-2 | estimate | N_0(k) is bounded below uniformly in k by a constant plus r_R log_L log of the inverse squared supremum coupling. | proved conditionally | running-radii-b; bar g=sup_m g_m<1 | "Taking" |
| 42950-43085 | 4.12:def-determining-sets | definition | Blocks, determining sets, block data, local scales, and the averaging map are specified with explicit input hypotheses. | definition | lattice-configurations; B-CMP98; B-CMP119; B-CMP122a | "Blocks, determining sets and the averaging map" |
| 42962-42964 | L-adic blocks | definition | Level-m blocks are origin-anchored cubes of side ℓ_m subdividing into L^d blocks of the preceding level. | definition | ℓ_m | "the cubes of side" |
| 42965-42984 | Domains, determining sets, base points, block lattices and data | definition | A partition into blocks supplies a graph of adjacent-block base points, gauge data, bond sizes, and plaquette sizes. | definition | L-adic blocks; G | "A \emph{domain} is a union" |
| 42974-42978 | Block-data gauge action and composition | identity | Gauge transformations act at the two block endpoints and compose by pointwise multiplication in application order. | definition | Data D; base-point functions v,v′ | "It acts by" |
| 42985-43006 | Prescribed-level determining set and boundary tower | construction | The determining set at p is required to use the minimum of slot, space, and boundary-tower levels with adjacent levels differing by at most one. | assumed | Determining-set hypothesis; c; X; p | "fixed by the determining-set hypothesis" |
| 42992-42994 | 4.12:eq-determining-sets-a | identity | The block level is min(p,c(x),t_X(x)). | assumed | Determining-set hypothesis | "including" |
| 43002-43004 | 4.12:eq-determining-sets-b | estimate | Distance at least 2M_1ℓ_m from the boundary guarantees tower level at least m. | assumed | Determining-set hypothesis | "It is a hypothesis of this chapter" |
| 43007-43012 | 4.12:eq-determining-sets-1; local block side | definition | The local scale at a bond or plaquette is the smallest side of a block meeting its one-step site enlargement. | definition | ξ^+; determining set | "put" |
| 43013-43016 | Averaging map M_B | construction | The map takes fine configurations to block data using B-CMP98 averages and B-CMP119 interface composition. | cited | B-CMP98 (1.5); B-CMP119 (2.14) | "These data are the" |
| 43018-43027 | 4.12:eq-determining-sets-c | identity | Averaging preserves the identity, is gauge covariant, and reads only the two endpoint blocks. | cited | B-CMP98 Propositions 2,6,7; B-CMP109 covariance lemma | "enter this chapter as inputs" |
| 43029-43042 | 4.12:eq-determining-sets-d; small-field averaging | estimate | A sufficiently small identity-background one-form averages to gauge-transformed exponential data with a block-side bound. | assumed | c_av; c_Q; B-CMP98 equal-level estimate; interface averaging hypothesis | "enter this chapter as inputs" |
| 43044-43052 | 4.12:eq-determining-sets-e | estimate | Small fine-lattice curvature bounds averaged plaquette curvature by twice the squared scale ratio times the local supremum. | cited | B-CMP98 Propositions 2,6,7 and hypothesis (52); c_av | "taken here by statement" |
| 43055-43064 | Determining-set hypothesis | hypothesis | Towers and determining sets with every property in item (iii) are fixed for every domain, space-level function, and slot level. | assumed | B-CMP122a determining sets; B-CMP119 minimal towers; B-CMP109 maximal domains | "It is a hypothesis of this chapter" |
| 43066-43079 | Averaging input provenance and restrictions | hypothesis | Normalisation, locality, equal-level averaging, curvature averaging, and covariance are accepted in their specified real-group forms. | cited | B-CMP98 Propositions 2,6,7, hypothesis (52); B-CMP109 covariance lemma | "taken by statement" |
| 43080-43084 | Interface averaging hypothesis | hypothesis | The equal-level small-field averaging estimate extends to bonds joining blocks of different levels. | assumed | determining-sets-d; B-CMP119 (2.14) interfaces | "it is a hypothesis of this chapter" |
| 43087-43206 | 4.12:def-constrained-minimisers | definition | The section specifies constrained critical configurations and the cited existence, uniqueness, and response inputs. | definition | determining-sets; lattice-configurations | "Constrained minimisers and their response to small data" |
| 43098-43102 | Constraint manifold C(B,D) | definition | The constraint manifold consists of G-valued configurations whose block average is D. | definition | M_B; X; G-valued D | "the \emph{constraint manifold}" |
| 43103-43107 | Wilson action A | definition | The action is the sum over plaquettes of the real trace of one minus plaquette holonomy. | definition | ∂U; X | "The \emph{Wilson action on $X$}" |
| 43108-43110 | Critical constrained configuration | definition | Criticality means that the action derivative vanishes along every differentiable constrained curve through the configuration. | definition | C(B,D); Wilson action | "is \emph{critical} if" |
| 43113-43120 | 4.12:eq-constrained-minimisers-a; data condition | hypothesis | Uniform block-plaquette distance at most ε_1 supplies the cited data hypothesis and is preserved by G-valued gauge transformations. | cited | B-CMP102b hypothesis (7), comparison (172) | "is used in the following form" |
| 43122-43155 | Existence, uniqueness, and constrained minimiser U(B,D) | theorem | Small admissible G-valued data have a constrained critical representative with curvature and current bounds, unique up to gauge within the curvature threshold. | cited | B-CMP102b Theorem 1 and spaces (2),(6),(8); B-CMP109 localisation; constrained-minimisers-a; ε_1≤a_1; B_3 ε_1≤ε_0 | "this block-scale form of the theorem is used here by statement" |
| 43142-43149 | 4.12:eq-constrained-minimisers-b | estimate | Curvature and current satisfy local-scale bounds with B_3 ε_1, and uniqueness uses the displayed ε_0 curvature threshold. | cited | B-CMP102b Theorem 1; local block side | "the two bounds in the first row" |
| 43155 | Name “constrained minimiser” | definition | U(B,D) denotes the selected critical configuration with data D. | definition | Existence and uniqueness statement | "is the \emph{constrained minimiser}" |
| 43157-43167 | Response provenance, δ and scaled block distance | definition | The response uses the B-CMP122a decay constant and distance measured in local-scale M_1 cubes to the nearer endpoint block. | definition | B-CMP122a (1.46)-(1.47); B-CMP102b Proposition 9, (190) | "Several objects enter it" |
| 43168-43175 | Block-sum norm and identity-background response notation | definition | The norm sums bond amplitudes with exponential distance weights, and exponentiating a one-form produces an identity-background configuration. | definition | δ; scaled block distance; b | "the block-sum" |
| 43177-43189 | Small-data response H_B(b) and gauge u′ | construction | Small exponential data yield a minimiser gauge equivalent to an identity-background exponential response one-form. | cited | B-CMP102b Proposition 9, (190); B-CMP99b constants; sup b<b_H; existence hypotheses | "It is used here by statement" |
| 43190-43199 | 4.12:eq-constrained-minimisers-c | estimate | The response and its first and second derivatives are bounded by B_H times the block-sum norm at the corresponding local scales. | cited | Small-data response input; B-CMP109 (3.12); trivial background | "This $1$-form satisfies a bound" |
| 43201-43205 | 4.12:eq-constrained-minimisers-d | estimate | The half-rate exponential distance sum is uniformly bounded by c_d over all determining sets, domains, and steps. | cited | Response input; B-CMP122a scaled block distance; B-CMP99b,B-CMP102b constants | "uniformly" |
| 43208-43306 | 4.12:not-admissible-boxes | definition | The large-field geometry, admissible boxes, and source datum are fixed for the step. | definition | Source-space theorem; B-CMP122a (1.73); running-radii | "We set out only" |
| 43220-43239 | Old level o, healed level n, block level b and thin shells | definition | Old collars, healed regions, and the step determining set assign the displayed levels to the large-field regions and shells. | definition | Z; old domains; B-CMP122a (1.73); determining-sets; N_0 | "The \emph{old level}" |
| 43240-43245 | B_5 | definition | B_5 is the part of Z between the level-(k_0+1) domain and its fifth enlargement, with block level k and old level k_0. | definition | Large-field domains | "Put" |
| 43245-43253 | Cut surface, core C, carried factor U_2 | definition | The core is Z outside the enlarged level-(h+1) domain and carries the second G-valued composite factor U_2. | definition | Large-field geometry; composite configurations | "carried by those" |
| 43253-43263 | Cut band K_c and its geometric inputs | hypothesis | The two-layer cut band outside the core lies in Z''_k, where old levels do not exceed block levels below k. | assumed | Large-field geometry; R_(h+1); M | "both are taken by statement" |
| 43266-43274 | Admissible box | definition | An admissible box lies in Y_4, has healed level k everywhere, and has edges no longer than 204M. | definition | Y_4; healed level; source clause admissible-boxes-a | "An \emph{admissible box} is a box" |
| 43276-43285 | Λ, Λ~; 4.12:eq-admissible-boxes-b | hypothesis | The enlarged box contains Z''_k, lies in Z''_k union B_5 and in Y_4, and has edges at most 102M. | cited | B-CMP122a (1.73) | "used here as stated" |
| 43288-43296 | Source datum and factorisation U=U′ Ubar | definition | A source-space point has a G-valued factor Ubar from the cited factorisation clause. | definition | Source-space theorem; B-CMP119 (2.34)(i) | "The source datum is a point" |
| 43294-43302 | 4.12:eq-admissible-boxes-a | hypothesis | On healed-level-k source plaquettes, the G-valued factor has curvature smaller than the running radius times η squared. | assumed | Source-space defining clause; B-CMP119 (2.34) | "therefore a" |
| 43305 | Claim: Λ~ is admissible and contains Z''_k | lemma | The enlarged geometric box is admissible and covers Z''_k. | proved conditionally | admissible-boxes-b; definitions of B_5, healed level, admissibility | "Proof of the claim" |
| 43308-43325 | Proof of admissible-box claim | proof | The geometric inclusions and edge bound imply all admissibility conditions and hence the source curvature bound throughout Λ~. | proved conditionally | admissible-boxes-b,a; large-field geometry | "satisfies every condition" |
| 43327-43464 | 4.12:def-consumer-radii | definition | Consumer classes, determining sets, minimisers, slot radii, gains, and geometric separation are specified. | definition | running-radii; determining-sets; constrained-minimisers; admissible-boxes; consumer classification | "The consumers' spaces" |
| 43342-43356 | Consumer E, domain D_E, derived-slot convention | definition | A consumer belongs to K1–K5 and reads every allowed subdomain and slot level with pointwise entries E_1,E_3 and derived entries E_2,E_4. | definition | Consumer classification; B-CMP122a (1.64)-(1.69); B-CMP119 (2.34)-(2.39); B-CMP109 (1.11)-(1.16) | "By the convention on derived slots" |
| 43358-43368 | Consumer level function c_E; K1–K5 | definition | The level function is j for old E and R terms, min(o,j) for old B terms, o for last-step B terms, and b for C terms, with K5 read through these classes. | definition | Consumer classification; o; b | "is defined as" |
| 43370-43375 | 4.12:eq-consumer-radii-1; B_E | definition | The consumer determining set has block level min(p,c_E,t_(X'')). | definition | determining-sets-a; determining-set hypothesis | "the consumer's determining set" |
| 43376-43380 | 4.12:eq-consumer-radii-2; U_E | definition | U_E is the constrained minimiser for the consumer determining set with averages of Ubar, whenever that minimiser exists. | definition | constrained-minimisers-b; M_B; Ubar | "whenever the right-hand side exists" |
| 43382-43385 | Consumer level n_E(ξ) | definition | The level of a bond or plaquette is the maximum consumer level at its sites. | definition | c_E | "put" |
| 43387-43395 | 4.12:eq-consumer-radii-b; two-layer interior | definition | Derived slots are imposed only at distance at least 2M times the local consumer block side from the subdomain boundary. | definition | 4.4:not-units-distances; B-CMP109 §1; B-CMP119 (2.35) | "are imposed" |
| 43397-43406 | Coefficient-times-gain ϑ_E | definition | ϑ_E is the positive coefficient-times-gain supplied by the consumer space at the local level. | definition | Consumer space D_E | "be the coefficient-times-gain" |
| 43401-43403 | 4.12:eq-consumer-radii-3; tgt_2 | definition | The curvature slot radius is ϑ_E times the level-n running radius times η²ℓ_n^(-2). | definition | n_E; ϑ_E; running radii | "The consumer's radii" |
| 43404-43406 | 4.12:eq-consumer-radii-c; tgt_4 | definition | The current slot radius is ϑ_E times the running radius times ℓ_n^(-3)L^((n−p)_+). | definition | B-CMP119 (2.37); n_E; p; ϑ_E | "The consumer's radii" |
| 43407-43408 | Interface choice of radius | remark | Taking the maximum site level selects the more demanding interface radius because the radii decrease with level. | assumed | Consumer radius assignments | "The radii decrease with $n$" |
| 43410-43421 | 4.12:eq-consumer-radii-4; G-valued fourth-clause requirements | requirement | Every allowed interior plaquette and bond must satisfy the consumer minimiser curvature and current bounds at every slot and subdomain. | assumed | U_E; tgt_2; tgt_4; two-layer interior | "These are imposed for every slot level" |
| 43423-43431 | 4.12:eq-consumer-radii-d; hat ϑ | estimate | The gain is at least θ_* times one below k_0 and θ_* times L_0^(2(n−k_0)) at intermediate levels. | proved conditionally | Consumer-space coefficient and gain inputs at 43491-43508 | "together with the lower bound" |
| 43432-43435 | 4.12:eq-consumer-radii-e | estimate | A K4 consumer on B_5 at level k has gain at least (1−2β)L_0^(2N_0). | proved conditionally | Consumer-space level-k coefficient and gain; 43506-43508 | "multiplied by the gain" |
| 43437-43440 | Level-k consumers, assertion (i) | lemma | Inside an admissible box in Z''_k union B_5, only K4 consumers reach level k and those points lie in B_5. | proved conditionally | Consumer classification; old-level and block-level geometric inputs | "Hence only" |
| 43442-43451 | 4.12:eq-consumer-radii-a; scaled separation | estimate | A gap of at least two consumer levels forces scaled distance at least (m−n−1)M/M_1. | cited | B-CMP122a (1.46),(1.47), §1 shell widths | "This is the separation estimate" |
| 43454-43460 | Three consumer-space inputs, first two | hypothesis | The argument uses the listed class levels and regions and matching pointwise and derived gains with their stated lower bounds. | assumed | Consumer classification; consumer-radii-d,e | "only through three properties" |
| 43461-43462 | Composite G-valued factor off the core | hypothesis | Every composite W_i has G-valued factor Ubar outside the core. | cited | Theorem on the G-valued factor of the composites | "this property is taken from the theorem" |
| 43466-43525 | Proof of consumer radii and geometry assertions | proof | The proof reads radius and gain assignments from the consumer spaces, excludes level-k old terms, and invokes the cited separation estimate. | proved conditionally | Three consumer-space inputs; consumer classification; B-CMP119 (2.37); B-CMP122a (1.47), §1; old-level geometry | "We justify, in turn" |
| 43470-43489 | Radius identification and change of lattice normalisation | proof | Matching slot gains yields tgt_2 and transporting the cited current radius to the η lattice yields tgt_4. | proved conditionally | Consumer classification; matching-gain input; B-CMP119 (2.37) | "transported from the lattice" |
| 43491-43502 | θ_N and κ_j coefficient inputs | hypothesis | The consumer-space coefficients obey θ_N(m)≥θ_*, θ_N(k)≥1−2β, and κ_j≥1−β. | cited | B-CMP122a (1.64)-(1.69); B-CMP119 (2.34)-(2.39); B-CMP109 (1.11)-(1.16) | "read off from" |
| 43503-43508 | Proof of consumer gain lower bounds | proof | Multiplying the coefficient lower bounds by the supplied gains gives the two claimed gain estimates. | proved conditionally | θ_N and κ_j inputs; gains of consumer spaces | "this gives" |
| 43510-43518 | Proof of level-k assertion | proof | Old consumers have levels below k while K4 uses the block level, whose level-k points lie in B_5. | proved conditionally | Old geometry o≤k_0; old-term j<k; K1–K5; block levels | "such consumers have no" |
| 43520-43524 | Separation justification | proof | The scaled separation is invoked from B-CMP122a using the construction's intermediate-shell widths. | cited | B-CMP122a (1.47), §1 | "this width is part of their construction" |
| 43527-43540 | 4.12:rem-unchanged-factor | remark | Leaving Ubar unchanged transfers source bounds but does not itself supply the distinct consumer minimiser slots. | proved conditionally | Source-space determining set; consumer determining set; healed levels; later derived-slots proposition (c) and corollary | "does not by itself deliver" |
| 43531-43533 | Source determining set B_ν | definition | B_ν is the determining set attached by the source space to the subdomain and slot using the healed level. | definition | Source space; healed ν; determining-sets | "built with the healed level" |
| 43542-43557 | Proof of unchanged-factor insufficiency | proof | Source and consumer determining sets use different block structures, so unchanged factor bounds refer to different minimisers and radii. | proved conditionally | Source healed level ν=k; consumer shells and collars; boundary tower; consumer-radii | "does not" |
| 43559-43628 | 4.12:def-coupling-thresholds | definition | Cube-size floors, coupling ceilings, and their order of choice are collected with uniform feasibility assertions. | definition | running-radii; averaging constants; minimiser/response constants; J2; admissible-box size | "The conditions below are all one-sided" |
| 43570-43578 | One-sided conditions and parameter order | requirement | Choose L_0 and L above their floors, then fix M_1 and δ, then take M large and the couplings small. | assumed | θ_*; B-CMP99b,B-CMP102b; L_*(β)=max(15,6/θ_*,2e²,3L_0²) | "Finally, the couplings are taken small" |
| 43580-43582 | Φ0; 4.12:eq-coupling-thresholds-a | requirement | δM/M_1 must be at least two. | assumed | B-CMP122a choice; later separation property | "These are the conditions" |
| 43583 | Φ1; 4.12:eq-coupling-thresholds-b | requirement | M must be at least M_1. | assumed | M_1 | "These are the conditions" |
| 43584-43589 | Φ2; 4.12:eq-coupling-thresholds-c; M_* floor | requirement | M must be large enough that 2L exp(−δM/(2M_1)) is at most one and all three floors persist above M_*. | assumed | L; δ; M_1 | "hold for every" |
| 43591-43596 | a_max and K_b | definition | These constants collect the axial-gauge size, averaging and response summation factors, and admissible-box side bound. | definition | d; M; running radius; c_Q; c_d; L | "Set" |
| 43597-43607 | Γ0; 4.12:eq-coupling-thresholds-d | requirement | Five groups of smallness inequalities control averaging, minimiser existence, response data, and current estimates at step k. | assumed | c_2; a_1; B_3; ε_0; a_max; c_Q; b_H; B_H; K_b; C_J | "The following conditions are required to hold" |
| 43609 | Γ1; 4.12:eq-coupling-thresholds-e | requirement | 4L³B_3(1+β_0)W(N_0) must not exceed θ_*. | assumed | W; B_3; β_0; θ_* | "The following conditions are required to hold" |
| 43610 | Γ2; 4.12:eq-coupling-thresholds-f | requirement | 6L³B_H K_b(1+β_0)W(N_0) must not exceed θ_*. | assumed | W; B_H; K_b; β_0; θ_* | "The following conditions are required to hold" |
| 43611-43612 | Γ3; 4.12:eq-coupling-thresholds-g | requirement | 4L³B_3 must not exceed (1−2β)L_0^(2N_0). | assumed | L; B_3; β; L_0; N_0 | "The following conditions are required to hold" |
| 43613-43616 | 4.12:eq-coupling-thresholds-h; W(N_0) | definition | W is the maximum of L_0^(-2N_0) and sqrt(1+N_0)L^(-N_0). | definition | L; L_0; N_0 | "where" |
| 43618-43621 | Existence of uniform depth floor N_* | estimate | A finite depth floor guarantees Γ1–Γ3 for every larger depth. | proved in detail | L_0≥2; L≥15; β<1/4; fixed positive constants | "The assertion of this definition has two parts" |
| 43621-43627 | Existence of uniform coupling threshold γ_* | estimate | A sufficiently small uniform bound on the running couplings guarantees Γ0–Γ3 at every step. | proved conditionally | running-radii inputs and depth growth; fixed parameters; N_* | "whenever" |
| 43630-43688 | Proof of threshold feasibility | proof | Solving the M inequalities, using exponential depth gains, and shrinking the couplings establishes the floors and uniform threshold. | proved conditionally | running-radii-a,b and small-radius formula; fixed constants; β<1/4 | "with the stated property" |
| 43631-43642 | Explicit M_*(L) | construction | The maximum of M_1, 2M_1/δ, and 2M_1 log(2L)/δ enforces Φ0–Φ2. | proved in detail | Φ0; Φ1; Φ2 | "each condition can be solved" |
| 43644-43669 | Decay of W and proof of N_* | proof | Both terms in W decrease to zero while the Γ3 gain increases without bound, giving a common depth floor. | proved in detail | L_0≥2; L≥15; θ_*>0; 1−2β>0 | "By the monotonicity" |
| 43671-43688 | Coupling-threshold proof and parameter scope | proof | Small radii enforce Γ0 and uniform depth growth enforces Γ1–Γ3, absorbing all box-size dependence into γ_*. | proved conditionally | running-radii-a,b as cited in text; radius formula; N_*; fixed constants | "No new condition on $L$ or $k$ is introduced" |
| 43690-43706 | 4.12:lem-monotone-paths | lemma | The discrepancy of two monotone path holonomies is bounded by a plaquette bound times their minimum adjacent-transposition distance. | proved in detail | G-valued U; box; plaquette bound φ; monotone paths | "This is the first" |
| 43696-43705 | n_tr and step counts n_μ | definition | n_tr is the smallest number of adjacent swaps between the path words and n_μ counts steps in each direction. | definition | Monotone paths Π,Π′ | "the least number of adjacent transpositions" |
| 43700-43704 | 4.12:eq-monotone-paths-1 | estimate | The holonomy discrepancy is at most n_tr φ and n_tr is at most the sum of all cross-direction step-count products. | proved in detail | Plaquette bound; unitary norm; inversion counting | "This proves the second" |
| 43708-43712 | Ordered path-word convention U(a) | definition | U(a) is the left-to-right ordered bond product for the monotone path starting at u with word a. | definition | lattice-configurations | "denotes the same product" |
| 43714-43785 | Proof of monotone-path lemma | proof | Inversion counting and one-plaquette swaps express the holonomy discrepancy as a product whose norm error adds. | proved in detail | Unitary norms; plaquette definition; inversion count | "By induction on the number of factors" |
| 43733-43739 | 4.12:eq-monotone-paths-2 | identity | Swapping two positive coordinate steps inserts the corresponding oriented plaquette holonomy. | proved in detail | Plaquette definition | "From the definition" |
| 43750-43756 | 4.12:eq-monotone-paths-3 | identity | A full-path swap multiplies its holonomy by a prefix-conjugated plaquette variable or its inverse. | proved in detail | monotone-paths-2; common prefix and remainder | "we obtain" |
| 43758-43783 | Swap-chain factors Ξ_i and product estimate | construction | Iterating swaps gives a product of conjugated plaquettes whose deviations sum to at most n_tr φ. | proved in detail | monotone-paths-3; unitary product estimate | "and iterating" |
| 43787-43809 | 4.12:lem-axial-gauge | lemma | Lexicographic path holonomies give an axial gauge with controlled bond variables and a bounded Lie-algebra logarithm. | proved in detail | Plaquette bound φ; box side Δ; (d−1)Δφ/η≤1; monotone-paths; lattice-configurations-a | "Dividing by" |
| 43794-43797 | Axial-gauge smallness hypothesis | hypothesis | The product (d−1)Δφ/η is assumed at most one. | assumed | d; Δ; η; φ | "Assume" |
| 43798-43805 | Lexicographic paths γ_x, axial gauge a, logarithmic one-form | construction | Coordinate-ordered paths from the minimal corner define a(x)=U(γ_x) and the logarithm of U^a divided by iη. | definition | Path holonomy; principal logarithm | "and put" |
| 43802-43804 | 4.12:eq-axial-gauge-1 | estimate | Each axial-gauge bond is within (d−1)Δφ/η of the identity. | proved in detail | monotone-paths lemma; swap count | "which is" |
| 43806-43808 | 4.12:eq-axial-gauge-2 | estimate | The logarithmic one-form is bounded by (π/3)(d−1)Δφη^(-2). | proved in detail | axial-gauge-1; smallness hypothesis; lattice-configurations-a as invoked | "Dividing by" |
| 43811-43865 | Proof of axial-gauge lemma | proof | Moving the final coordinate step bounds the required swaps, the logarithm estimate bounds the one-form, and tree-path bonds require no swaps. | proved in detail | monotone-paths; lattice-configurations-a; gauge definition | "no transposition" |
| 43867-43882 | 4.12:lem-perturbed-plaquettes | lemma | The curvature of a left perturbation is bounded by background curvature, two covariant derivatives, and explicit mixed and quadratic errors. | sketched | G-valued Y; Lie-algebra W; 4ηw_0≤1; lattice-configurations | "Multiplying out the four exponential series" |
| 43870-43872 | w_0 and perturbation smallness | hypothesis | w_0 is the maximum one-form norm on the four plaquette bonds and 4ηw_0 is assumed at most one. | assumed | W; η; plaquette | "Assume" |
| 43873-43881 | 4.12:eq-perturbed-plaquettes-1 | estimate | The curvature bound has derivative coefficient η², mixed coefficient 4η, and quadratic coefficient 12η². | sketched | Background curvature; covariant derivatives; w_0; unfinished proof | "Multiplying out the four exponential series" |
| 43884-43968 | Proof of perturbed-plaquette lemma, beginning only | proof | The proof transports four exponentials, bounds their summed exponents, and begins the power-series expansion before the chunk ends. | sketched | Unitary norm; left-perturbation definition; covariant derivatives; 4ηw_0≤1 | "the terms of" |
| 43890-43900 | Local variables y_i and W_i | definition | The four oriented background bonds and positive-direction one-form components are named for the product expansion. | definition | Y; W; plaquette corners | "Write" |
| 43903-43907 | 4.12:eq-perturbed-plaquettes-2 | identity | The perturbed plaquette expands into four exponentials interspersed with background bond factors. | proved in detail | Left-perturbation and plaquette definitions | "By the definition" |
| 43909-43926 | Moving group elements right; X_i | construction | Conjugation transports each perturbation into a common frame while preserving its norm. | proved in detail | ge^A=e^(Ad_g A)g; unitary norm | "Moving the group elements to the right" |
| 43916-43919 | 4.12:eq-perturbed-plaquettes-3 | identity | The perturbed plaquette is the product of four transported exponentials followed by the background plaquette. | proved in detail | perturbed-plaquettes-2; conjugation identity; X_i | "becomes" |
| 43928-43951 | Sum of exponents; 4.12:eq-perturbed-plaquettes-4 | identity | The exponent sum Σ is the covariant curl plus a background-plaquette conjugation error. | proved in detail | X_i; ∇^Y definition; y_1 y_2 y_3^(-1)=∂Y y_4 | "therefore gives" |
| 43952-43959 | Conjugation-error norm bound | estimate | The deviation of Ad_g from the identity acting on A is at most twice the distance of g from the identity times the norm of A. | proved in detail | Unitary norm; submultiplicativity | "because" |
| 43961-43965 | 4.12:eq-perturbed-plaquettes-5 | estimate | The norm of Σ is bounded by η times two covariant derivatives plus four times background curvature times w_0. | proved in detail | perturbed-plaquettes-4; conjugation-error bound | "this and" |
| 43967-43968 | Four-exponential expansion parameter s | construction | The expansion parameter s is η times the sum of the four exponent norms and is at most one. | definition | X_i norm bounds; 4ηw_0≤1 | "Put" |

## Forward and backward references

This ledger includes references within the chunk as well as targets outside it; repeated uses are listed by their source lines. Bibliographic keys are retained verbatim because the bibliography is outside the permitted source.

- 42670: the opening fragment refers back to unnamed premises for the G-valued-factor clause; the antecedent is outside this chunk.
- 42671-42675: Theorem `4.11:thm-clause-reproduction` is said not to need comparisons of constrained minimisers from different towers or tower regions.
- 42676-42678: B-CMP109 (1.12), (1.17), B-CMP119 (2.38), and B-CMP116 width inclusions are expressly outside the preceding section's claims.
- 42679-42682: membership in the previously defined classes already presupposes tower quantities at certain complex data; no extra existence is asserted here.
- 42683-42684: the Cauchy-family cases in the proof of `4.11:thm-clause-reproduction` clause (ii) are the limit of the completeness assertion.
- 42689-42692: `4.11:thm-clause-reproduction` and coupling ceilings `4.11:eq-floors-ceilings-c,d` are the inputs to the threshold claim.
- 42706: the squared threshold is identified with `4.11:eq-floors-ceilings-a`.
- 42708-42714: `4.11:not-floors-ceilings`, its floor (a), and the restriction and twist cases of the reproduction theorem's heredity proof identify the relevant lower bound.
- 42715-42721: ceilings `4.11:eq-floors-ceilings-c,d` are imposed after L, allowing `4.11:thm-clause-reproduction` to apply.
- 42787: J is defined by B-CMP109 (1.8).
- 42788-42789: E_3 and E_4 are named as current sizes to be introduced later in the section.
- 42797-42798: J2 rests on B-CMP109 (3.11)-(3.13) but is explicitly assumed here.
- 42810-42812: D*D is from B-CMP109 (3.12); its other use is the response-one-form hypothesis below.
- 42816, 42839: `4.12:eq-lattice-configurations-a` is the logarithm estimate proved in this argument.
- 42841-42855: the closed-subgroup theorem and local exponential chart supply Lie-algebra membership; no particular external work is named.
- 42857-42878: assertions (ii)-(v) of `4.12:not-lattice-configurations` supply the norm, gauge, plaquette, and exponential conventions for the proof.
- 42883-42884: `4.12:not-lattice-configurations` supplies running-radius lattice notation.
- 42886-42894: the radius and exponent q_0 are from B-CMP119; monotonicity is assigned to the proof below; the ratio estimate is from B-CMP119 (2.6)-(2.7).
- 42899-42905: chapter standing auxiliary-parameter conditions fix β and the restrictions on β_0, L_a, and L; `running-radii-a` identifies β_0.
- 42907-42915: B-CMP122a defines the large-field level and supplies the scale relations from (1.70) ff.; chapter standing conditions are also invoked.
- 42920-42922: `running-radii-a` is again assigned to B-CMP119 (2.6)-(2.7), and `running-radii-b` is used as stated rather than reproved.
- 42936-42947: `running-radii-b` yields the uniform lower bound `running-radii-2`, which yields depth growth.
- 42951-42960: `4.12:not-lattice-configurations` supplies the group, lattice, gauge, and plaquette conventions for determining sets.
- 42988-42989: the prescribed-level determining set is fixed by the determining-set hypothesis after the list.
- 43013-43016: averaging is from B-CMP98 (1.5), with interfaces composed as in B-CMP119 (2.14).
- 43055-43064: the determining-set hypothesis explicitly includes `determining-sets-a,b` and abstracts B-CMP122a's large-field determining sets, B-CMP119's minimal determining sets and towers, and B-CMP109's maximal possible domains.
- 43066-43071: `determining-sets-c,d,e` are inputs; normalisation, locality, equal-level (d), and (e) are assigned to B-CMP98 Propositions 2, 6, and 7.
- 43074: `determining-sets-e` is taken under B-CMP98 hypothesis (52).
- 43075-43076: `determining-sets-d` is restricted to the identity base configuration and Lie-algebra-valued argument.
- 43078-43079: covariance in `determining-sets-c` is taken from B-CMP109's covariance lemma for averaging.
- 43080-43084: different-level `determining-sets-d` uses interfaces as in B-CMP119 (2.14) but is a chapter hypothesis, expressly not a statement taken from B-CMP98.
- 43089-43095: `4.12:def-determining-sets` supplies the block lattice, averages, and local scale; `4.12:not-lattice-configurations` supplies the current and group conventions.
- 43113-43120: B-CMP102b hypothesis (7), compared with (172), is put in the form `constrained-minimisers-a`, including gauge preservation.
- 43122-43135: B-CMP102b Theorem 1 with spaces (2), (6), and (8) is used in block-scale form; localisation uses B-CMP109; data hypothesis (7) is read as `constrained-minimisers-a`; `4.12:def-determining-sets` fixes the allowed determining sets.
- 43150-43153: uniqueness uses the last row of `constrained-minimisers-b`.
- 43157-43167: the response is B-CMP102b Proposition 9 and (190), at trivial background and G-valued data; block decay and distance are B-CMP122a (1.46)-(1.47), with δ specifically from (1.47).
- 43177-43181: response constants depend on B-CMP99b and B-CMP102b constants; the existence and uniqueness hypotheses above are required.
- 43197-43199: ∇ is the previously defined covariant derivative at the identity, and D*D is B-CMP109 (3.12).
- 43212-43217: `4.12:not-running-radii` fixes the source radius; the chapter's source-space theorem supplies the source space; `admissible-boxes-a` is its needed clause; `admissible-boxes-b` is taken from B-CMP122a (1.73).
- 43225-43231: B-CMP122a (1.73) singles out Z''_k; `4.12:def-determining-sets` supplies the step determining-set meaning.
- 43251-43253: the core factor U_2 is contrasted with Ubar of item (c) below.
- 43256-43263: the two geometric inclusions/level bounds are taken by statement, without an individual theorem label.
- 43271-43274: admissibility invokes the source bound `admissible-boxes-a` from item (c) below.
- 43276-43285: B-CMP122a (1.73) supplies Λ and the enlarged-box properties `admissible-boxes-b`.
- 43292-43302: the source-space theorem supplies the datum's space; B-CMP119 (2.34)(i) supplies factorisation; the source-space definition supplies `admissible-boxes-a`, compared with (2.34).
- 43309-43320: `admissible-boxes-b`, item (a)'s definitions, and item (b)'s admissibility conditions prove the box claim.
- 43322-43324: the remark after the admissible-box definition transfers `admissible-boxes-a` to Λ~.
- 43330-43340: `4.12:not-running-radii`, `4.12:def-determining-sets`, `4.12:def-constrained-minimisers`, and `4.12:not-admissible-boxes` supply the consumer notation and objects.
- 43342-43344: the consumer classification groups the spaces of B-CMP122a (1.64)-(1.69), B-CMP119 (2.34)-(2.39), and B-CMP109 (1.11)-(1.16) into K1–K5.
- 43347-43356: the convention on derived slots and the consumer classification supply subdomains, slot levels, D_E, and its four radius entries; item (g) below gives the G-valued derived-slot conditions.
- 43361-43367: K1 uses the one-scale old terms of B-CMP109 (1.11)-(1.16); the other classes and K5's indirect reading follow the consumer classification.
- 43370-43380: `determining-sets-a` supplies `consumer-radii-1`; `constrained-minimisers-b` governs when `consumer-radii-2` exists.
- 43392-43395: `4.4:not-units-distances` supplies the distance convention; the two-layer exclusion comes from B-CMP109 §1 and B-CMP119 (2.35).
- 43450-43451: scaled distance is used only via `consumer-radii-a` and the response-one-form hypothesis.
- 43454-43462: item (b), `consumer-radii-d,e`, and the theorem on the G-valued factor of the composites supply the three consumer-space properties.
- 43470-43477: the consumer classification's E_1 radius and the second input at the end of the definition identify `consumer-radii-3`.
- 43479-43489: B-CMP119 (2.37), transported to the η lattice, identifies `consumer-radii-c`.
- 43491-43508: `consumer-radii-d,e` are derived from coefficients and gains read from B-CMP122a (1.64)-(1.69), B-CMP119 (2.34)-(2.39), and B-CMP109 (1.11)-(1.16).
- 43510-43518: `4.12:not-admissible-boxes` supplies the old-level property used to prove assertion (i); the consumer classification supplies the old terms' j<k and class-specific levels.
- 43520-43524: `consumer-radii-a` is assigned to B-CMP122a (1.47), with shell and collar widths from its §1 construction.
- 43528-43533: `4.12:def-consumer-radii`, `4.12:not-admissible-boxes`, and `4.12:def-determining-sets` provide the consumer, datum, and two determining-set meanings.
- 43534-43539: the source-space clause preserves Ubar; the later proposition on consumer derived slots for the unchanged factor, part (c), and its corollary are said to establish the desired slots in their stated scope.
- 43543-43556: consumer shells and old collars are compared with the source's healed-level determining set and boundary tower; the respective spaces' slots and radii are the inputs.
- 43560-43568: `4.12:not-running-radii` supplies θ_*, β, β_0, L_0, N_0, C_0, q_0; `4.12:def-determining-sets` is cited for c_2,c_Q; `4.12:def-constrained-minimisers` for a_1,B_3,ε_0; `constrained-minimisers-c` for b_H,B_H,c_d,δ; `lattice-configurations-c` for C_J; `4.12:not-admissible-boxes` for 204M.
- 43577-43578: M_1 and δ are fixed as in B-CMP99b and B-CMP102b; M_*(L) is specified below.
- 43586-43589: Φ0 is identified as the B-CMP122a choice needed for a separation property later in the chapter; Φ0–Φ2 define the floor's purpose.
- 43618-43627: the forthcoming proof promises N_* for `coupling-thresholds-e` through (g), and γ_* for (d) through (g).
- 43634-43641: `coupling-thresholds-b,a,c` are solved explicitly to construct M_*.
- 43654-43669: `coupling-thresholds-e,f,g` use positivity from `4.12:not-running-radii` and the previously established monotonicity to give N_*.
- 43671-43684: `coupling-thresholds-d` is reduced to radius ceilings; the text invokes `running-radii-a` for smallness and `running-radii-b` for depth, then enforces `coupling-thresholds-e` through (g).
- 43708-43712: `4.12:not-lattice-configurations` supplies path ordering, unitarity, and operator norm conventions.
- 43724-43725: inversion counting proves the second inequality of `monotone-paths-1`.
- 43729-43739: the plaquette definition in `4.12:not-lattice-configurations` yields `monotone-paths-2`.
- 43744-43756: `monotone-paths-2` yields `monotone-paths-3`, including the inverse orientation case.
- 43758-43765: `monotone-paths-3` supplies each Ξ_i and the iterated product.
- 43781-43784: the product estimate concludes the first inequality of `monotone-paths-1`.
- 43788-43790: `4.12:not-lattice-configurations` provides the axial-gauge lemma's group, holonomy, and gauge conventions.
- 43836-43843: `4.12:lem-monotone-paths` gives `axial-gauge-1` from the counted swaps.
- 43845-43852: `axial-gauge-1` and `lattice-configurations-a` are invoked for logarithm membership and size, giving `axial-gauge-2`.
- 43854-43864: the identity displayed at the beginning of the axial-gauge proof is reused for tree bonds.
- 43868-43869: `4.12:not-lattice-configurations` supplies the perturbed-plaquette conventions.
- 43900-43907: the left-perturbation and plaquette definitions give `perturbed-plaquettes-2`.
- 43909-43919: conjugation of exponentials rewrites `perturbed-plaquettes-2` as `perturbed-plaquettes-3`.
- 43935-43951: the covariant forward derivative definition gives `perturbed-plaquettes-4`.
- 43958-43965: `perturbed-plaquettes-4` and the proved conjugation estimate give `perturbed-plaquettes-5`.
- 43967-43968: the lemma's smallness hypothesis bounds the expansion parameter; the proof continues outside the chunk, with no forward label given.

## Obligations named here

“Not asserted” entries below are scope exclusions, not promises that the authors will prove them. Requirements with a subsequent proof of feasibility remain requirements on the data or parameters, rather than independent unconditional conclusions.

- 42670: the opening fragment limits the G-valued-factor clause to premises given before this chunk; their content is unavailable here.
- 42671-42675: comparison of constrained minimisers for different tower rules or regions is not supplied and is said not to be needed for clause reproduction.
- 42676-42678: statements about B-CMP109 (1.12), (1.17), B-CMP119 (2.38), and B-CMP116 width inclusions are expressly not made.
- 42679-42682: existence of tower U and J at complex data beyond those already presupposed by class membership is not asserted.
- 42683-42684: completeness of the reproduction proof's Cauchy-family enumeration beyond its listed cases is not asserted.
- 42689-42691, 42715-42721: the reproduction result still requires coupling ceilings `4.11:eq-floors-ceilings-c,d` after L is chosen.
- 42790-42808: J1 covariance and J2's trivial-background current estimate are explicitly assumed and not proved in this section; J2 requires its scale, smallness, and neighbourhood hypotheses.
- 42899-42915: the fixed-exponent restrictions and depth/scale relations are standing conditions or accepted inputs.
- 42985-43006, 43055-43064: the determining-set hypothesis requires every prescribed partition and boundary tower, the minimum-level rule, adjacent-level restriction, constant-level block unions, base points, and boundary-distance bound.
- 43018-43052, 43066-43079: the averaging identities and estimates enter as inputs, with the small-argument restrictions, B-CMP98 hypothesis (52), and identity-background Lie-algebra argument explicitly specified.
- 43080-43084: the different-level interface averaging bound is a chapter hypothesis rather than a B-CMP98 result taken by statement.
- 43113-43135: the minimiser input requires G-valued data obeying the plaquette condition, ε_1≤a_1, and B_3ε_1≤ε_0, and accepts the cited theorem in block-scale localised form.
- 43150-43153: uniqueness applies only to critical constrained G-valued configurations satisfying the last-row curvature threshold of `constrained-minimisers-b`.
- 43157-43205: the response is used by statement at the trivial background and for G-valued data; it requires sup norm below b_H and the existence hypotheses, and includes derivative bounds and uniform exponential summability.
- 43256-43263: the off-core level ordering and cut-band inclusion are both taken by statement.
- 43276-43285: the Λ~ geometry is taken from B-CMP122a (1.73).
- 43294-43302: G-valuedness and the healed-level-k source plaquette bound are hypotheses on the source datum.
- 43347-43356, 43387-43395, 43410-43421: each consumer requires derived slots at all allowed levels and subdomains, on their two-layer interiors, with the displayed curvature and current radii.
- 43376-43380: defining U_E is explicitly contingent on existence under `constrained-minimisers-b`.
- 43407-43408: decreasing radii with level is stated without an argument here.
- 43454-43462: class levels and regions, shared coefficient-times-gain with its lower bounds, and the unchanged off-core composite factor are the three consumer-space inputs.
- 43534-43539, 43551-43556: preserving Ubar does not itself establish consumer slots; their establishment is assigned to the later derived-slots proposition (c) and corollary within their scope.
- 43573-43578: parameter choices must follow the displayed L_0 and L floors, fixed M_1 and δ, the M floor, and then small couplings.
- 43580-43589: Φ0, Φ1, and Φ2 impose the three M floors; Φ0 is needed for a later geometric separation property.
- 43597-43607: Γ0(i) requires the running radius at most c_2; (ii) imposes the a_1 and ε_0 minimiser ceilings; (iii) bounds a_max by min(c_2,1); (iv) imposes all three averaged-data ceilings; (v) imposes both response/current smallness inequalities.
- 43609-43612: Γ1 and Γ2 require the two W(N_0) expressions below θ_*, and Γ3 requires the level-k gain to dominate 4L³B_3.
- 43618-43627, 43630-43688: existence of floors N_* and γ_* is asserted and then argued here, conditionally on the accepted scale/radius inputs.
- 43794-43797: the axial-gauge lemma assumes (d−1)Δφ/η≤1.
- 43872: the perturbed-plaquette lemma assumes 4ηw_0≤1.
- 43884-43968: the perturbed-plaquette proof is unfinished at the chunk boundary; this is a coverage limitation, not an explicitly declared open mathematical obligation.

## For the stage question

- **42671-42675 — named open (scope exclusion):** no comparison is made between constrained minimisers belonging to different tower rules or regions, and the preceding reproduction theorem is said not to require such a comparison.
- **42676-42678 — named open (scope exclusion):** the section makes no statement about the listed B-CMP109/B-CMP119 displays or B-CMP116 inclusions across widths.
- **42679-42682 — named open (scope exclusion):** existence of tower quantities U_t and J_t at complex data is not supplied beyond the data at which class membership already presupposes their existence; this is the explicit complex-data statement in the chunk.
- **42683-42684 — named open (scope exclusion):** the enumeration of Cauchy families in the preceding reproduction proof is not claimed complete beyond the listed cases.
- **42772-42784, 42797-42812 — definition / assumed:** left perturbations use Lie-algebra-valued one-forms of G-valued backgrounds, while J2 and D*D are specifically at the trivial background; no complex extension is asserted by these definitions or hypotheses.
- **42907-42916 — definition / cited / proved conditionally:** the operation at step k uses k_0=k−N_0, with depth tied to B-CMP122a scales and growing uniformly at small coupling.
- **43029-43042, 43075-43084 — assumed:** the small-field averaging input is for an identity base configuration and Lie-algebra-valued argument, and its different-level interface version is separately assumed.
- **43055-43064 — assumed:** prescribed determining sets and towers are fixed for every domain and space-level function; the input explicitly abstracts the determining sets entering large-field minimisers, minimal towers, and maximal possible domains.
- **43098-43110 — definition:** constrained configurations are G-valued, with averaging constraints and criticality for the Wilson action.
- **43122-43155 — cited:** B-CMP102b's minimiser theorem is used in a local-block-scale form on localisation domain X, with G-valued data and gauge uniqueness inside the stated curvature threshold.
- **43157-43205 — cited:** the minimiser response is used at V_0=1 and for G-valued exponential data, producing a G-valued gauge transform of a Lie-algebra-valued response with derivative and decay bounds.
- **43220-43239 — definition:** old levels are carried by old collars, healed level is k on Z union the old top domain, and the step determining set has levels assigned to thin shells Γ''_m and deeper shells Γ''_j.
- **43240-43253 — definition:** B_5 has block level k and old level k_0, while the core carries the second G-valued factor U_2 in its composite configurations rather than Ubar.
- **43253-43263 — assumed:** the cut band consists of two layers of width MR_(h+1); outside the core it lies in Z''_k, whose old and block levels obey the stated ordering.
- **43266-43285 — definition / cited:** admissible boxes are spatial boxes in Y_4 with healed level k and bounded edge length, and the accepted geometry places Z''_k inside the enlarged box Λ~ within Z''_k union B_5 and Y_4.
- **43288-43302 — definition / assumed:** the source datum belongs to the source space supplied by a separate theorem, its factorisation has G-valued Ubar, and the healed-level-k curvature bound is a hypothesis on that datum.
- **43305-43325 — proved conditionally:** Λ~ is shown admissible and containing Z''_k using the accepted inclusions, so the source curvature bound applies throughout it.
- **43342-43368 — definition:** the consumers include old E^(j), R^(j), old B^(j), last-step B^(k), and C terms with target space U_N, with their distinct level functions and K5 read through K1–K4.
- **43347-43356, 43370-43421 — definition / assumed:** consumers read every permitted subdomain and slot level; their minimisers average Ubar on consumer-specific determining sets and are defined only when existence holds; their curvature/current admission conditions use the two-layer interior and consumer radii.
- **43437-43440, 43510-43518 — proved conditionally:** only K4 consumers reach level k inside the specified admissible boxes, and those points lie in B_5; old terms have lower levels.
- **43442-43451, 43520-43524 — cited:** scaled separation uses intermediate shell and old-collar widths from B-CMP122a; the shells are geometric inputs rather than an additional admission theorem.
- **43461-43462 — cited:** the theorem on the G-valued factor of composites supplies Ubar as every composite's G-valued factor off the core.
- **43527-43557 — proved conditionally:** unchanged Ubar alone does not establish consumer E_2/E_4 slots, because source healed-level determining sets and consumer shell/collar determining sets differ; the actual slot assertion is deferred to the later proposition (c) and corollary.
- **43597-43627, 43671-43688 — assumed / proved conditionally:** the Γ conditions must hold at each step, and a uniform coupling threshold is argued to enforce them at every k under the radius/depth inputs.
- **43787-43865 — proved in detail:** the axial-gauge construction is stated and proved for a G-valued configuration on a spatial box with small plaquette curvature.
- **43867-43968 — sketched (proof continues):** the last lemma concerns perturbing a G-valued background by a Lie-algebra one-form; the excerpt ends during its proof, after the transported exponent sum has been bounded.

No analytic ball, drop-out, or “prepared shell” is named in these lines. The boxes and domains defined here are spatial lattice domains. No statement here establishes complex-background admission, analytic-ball inclusion, or inclusion of all carried stage terms; the explicitly discussed consumer admission issue is the pair of G-valued derived slots and the distinction between source and consumer minimisers.
