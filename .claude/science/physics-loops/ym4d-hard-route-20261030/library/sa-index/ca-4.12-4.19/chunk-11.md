# Chunk 11: lines 55360-56650
Sections: No section or subsection heading occurs in this chunk; it continues material labelled 4.18 (55360–56340), then material labelled 4.19 (56342–56650). The opening remark begins before the chunk; the closing proof continues after it.

The index records the source's stated dependencies and proof status, without assessing correctness. Equation identifiers below are the source's labels (printed equation numbers are unavailable in this chunk). Overlapping rows distinguish statements, explicit hypotheses, displays, and their proofs. Unnumbered intermediate calculations are indexed under their named proof steps.

| Lines | Name / tag | Kind | What it states (one plain sentence, your words) | Status here | Reads (inputs it uses, by tag or name) | Key phrase |
|---|---|---|---|---|---|---|
| 55360–55377 | Opening remark, continuation: alternatives (c1)–(c3) | remark | The first two readings preserve cell geometry, whereas the third admits an older retained region whose lower members are only unions of M-cubes. | proved conditionally | Alternative descriptions (c1)–(c3); conditions (i), (ii); proof 55379–55475 | "Under (c1) and under (c2)" |
| 55363 | (c1) | hypothesis | No member of the label lies inside the retained region below its level. | assumed | Label ℓ; retained region Y; level s | "no member of" |
| 55364 | (c2) | hypothesis | Lower label members inside Y are the intersections with sets produced by T-operations. | assumed | Sets Zᵀ_i; Y | "the members" |
| 55365–55367 | (c3) | hypothesis | Lower label members inside Y are the older prepared sets, including the M-cube-only window. | assumed | Prepared sequence of step s; N₀(s) | "of the prepared sequence of that operation" |
| 55379–55475 | Proof of opening remark | proof | The proof traces admissible older operations and compares their label geometry under all three readings. | proved conditionally | (c1)–(c3); B-CMP122a; B-CMP122b; B-CMP119; profile definition | "the three descriptions are treated as alternatives" |
| 55380–55405 | Proof (a): older operations are allowed | proof | The last N steps exclude new regions only at levels h+1 through k and therefore permit an R-operation at s≤h. | proved conditionally | B-CMP122a conditions (i), (ii), (1.2), (1.11) | "violates neither (i) nor (ii)" |
| 55382–55387 | Bałaban's component-class conditions (i), (ii) | hypothesis | A component fits a specified cube and has no new large-field regions during the preceding N steps while previous regions satisfy the size condition. | cited | B-CMP122a | "each satisfies the following two properties" |
| 55393–55398 | Carried older operation and mixed-history boundary terms | construction | The older operation and low-level sets persist, and terms at a component's stopping stage remain boundary terms. | cited | B-CMP122a (1.2), (1.11), mixed-history construction | "is carried unchanged" |
| 55407–55420 | Proof (b): retained regions remain large-field regions | proof | A retained component becomes a large-field region at its operation's level and can belong to the previous region inside Z. | proved conditionally | B-CMP122b p. 390; B-CMP122a (1.72); proof (a) | "by (a) its presence is compatible" |
| 55422–55427 | Label-description identification left unresolved | requirement | The description of the post-R label deciding among the three alternatives is not derived here. | named open | B-CMP122b; B-CMP119 (2.18); 4.18:def-profiles-admissible | "not derived in this section" |
| 55422–55455 | Proof (c): profiles, couplings, and healed regions | proof | The proof describes each alternative's profiles and coupling and says all alternatives agree after a region is healed. | proved conditionally | (c1)–(c3); 4.18:def-profiles-admissible; B-CMP122a/b | "descriptions agree" |
| 55429–55442 | Coupling reset and retained-profile vanishing under (c1) | identity | The cited coupling formula is constant on Y and agrees with the level-s profile vanishing on and near Y. | cited | B-CMP122b coupling formula; 4.18:def-profiles-admissible | "agrees with" |
| 55443–55450 | Profiles and members under (c2), (c3) | remark | Reading (c2) keeps the pre-operation coupling on a retained region while (c3) includes prepared M-cube members. | assumed | Alternative label readings; B-CMP122a | "Description (c3) counts" |
| 55452–55455 | Healed older region | definition | A healed region has had its large-field factor absorbed into small-field format and has no remaining label member or profile contribution. | definition | Later step; retained profile; new constant coupling | "that is, whose" |
| 55457–55467 | Cell geometry under (c1) or (c2) | proof | All lower members are unions of cells because only T-produced sets and retained cell regions occur. | proved conditionally | (c1) or (c2); cell geometry of T sets and R retained regions | "Now assume (c1) or (c2)." |
| 55469–55474 | Cell-geometry failure under (c3) | proof | A retained step-h region allowed by the component conditions carries lower M-cube members that are not cell unions. | proved conditionally | (c3); proof (a), (b) | "Assume (c3)." |
| 55477–55504 | 4.18:lem-older-window — The window length of an older step against the current cell parameter | lemma | The older window length is less than c₁(k−s)+2R_k, also for the alternative cell parameters. | proved conditionally | Coupling flow; g_k≤e⁻¹; r>0; s≤h<k; N₀ relation; cell parameters | "Assume the coupling-flow statement" |
| 55478–55487 | 4.18:eq-older-window-1 | hypothesis | Earlier inverse couplings dominate the current one and their increments telescope with a linear upper bound. | assumed | 1.2:def-couplings; coupling-flow statement; β̄ | "consequences are used" |
| 55488–55498 | Older-window parameter assumptions and 4.18:eq-older-window-a | estimate | The specified cell parameters and integer window relation yield the bound with c₁=4+2r(1+β̄)+3r²β̄. | proved conditionally | 4.18:eq-older-window-1; 4.18:not-scales-partitions; 4.18:def-prepared-sequence; B-CMP122a | "Then" |
| 55499–55503 | 4.18:eq-older-window-2 | hypothesis | Alternative cell parameters lie between the logarithmic power and L times that power. | assumed | Couplings; r; alternative parameters Ř_m | "satisfying" |
| 55506–55606 | Proof of 4.18:lem-older-window | proof | Logarithmic bounds and elementary inequalities convert the implicit older window relation into a current-scale bound. | proved conditionally | 4.18:eq-older-window-1, -2; ceiling; N₀ relation; L≥3 | "This is" |
| 55514–55522 | Step 1: the cell parameter | proof | Minimality of the power of L gives R_m<L y_m^r and an upper bound on ν−2. | proved conditionally | Minimal cell parameter or 4.18:eq-older-window-2; N₀ relation | "by minimality" |
| 55524–55537 | Step 2: the flow | proof | Two applications of the flow bound control the older logarithmic coupling by current data and two logarithmic corrections. | proved conditionally | 4.18:eq-older-window-1; β̄≥0 | "Taking logarithms" |
| 55539–55544 | Step 3: splitting the logarithm | proof | A product bound separates the logarithm of a sum into three logarithmic terms. | proved in detail | Y≥1; a,b≥0 | "hence" |
| 55546–55570 | Step 4: elementary bounds | proof | Base-L logarithms and nested logarithms are bounded using square roots and arithmetic–geometric means. | proved in detail | L≥3 from 1.1:def-lattice; r>0 | "by the inequality of arithmetic and geometric means" |
| 55572–55584 | Collecting | proof | The preceding bounds isolate ν up to a current logarithmic term and a linear age term. | proved conditionally | Steps 1–4 | "Subtracting" |
| 55586–55605 | Step 5: current cell parameter and constant dependence | proof | The current cell parameter bounds the remaining logarithm and leaves a constant depending only on r and β̄. | proved conditionally | Cell-parameter lower bound; u≥1; L≥3 | "depends on" |
| 55608–55680 | 4.18:lem-graded-count — The graded count of older members made of M-cubes | lemma | Older contributions have a shell-graded count and are confined deep inside the prepared region and Λ. | proved conditionally | Hypotheses (a)–(e), including P1–P5; older-window lemma; cited five-layer geometry | "Assume the following." |
| 55609–55622 | Older-operation family S, h(s), s₀(s), Z″⁽ˢ⁾_i | construction | The family lists earlier R-operation steps and their components, windows, and prepared sequences inside Z. | definition | 4.18:def-prepared-sequence; 4.18:eq-scales-partitions-a; B-CMP122a | "Let" |
| 55624–55625 | Graded-count hypothesis (a) | hypothesis | Flow relations hold through k and the current coupling satisfies the stated ceiling. | assumed | 4.18:def-coupling-excess | "hold at all levels" |
| 55626–55627 | Graded-count hypothesis (b) | hypothesis | Every cell parameter satisfies either version of the older-window hypothesis. | assumed | 4.18:lem-older-window | "satisfy the hypothesis" |
| 55628–55629 | Graded-count hypothesis (c) | hypothesis | Each older step has an integer N₀(s) satisfying the cell-window equality. | assumed | S; R_{s−N₀(s)+1} | "For every" |
| 55630–55642 | Hypothesis (d), P1; A⁽ˢ⁾_i | hypothesis | The non-cell label members are exactly the nested older prepared intersections containing the specified older core. | assumed | S; older prepared sequences; Z_{h(s)} | "are exactly the sets" |
| 55643 | P2 | hypothesis | The top older prepared member has a ten-cell margin inside its component. | assumed | a_s; Z″⁽ˢ⁾_s; Y⁽ˢ⁾ | "operatorname{dist}" |
| 55644–55645 | P3 | hypothesis | Intersecting older components satisfy the age ordering and inclusion in the newer component's older region. | assumed | S; h(s); Z_{h(s)} | "If" |
| 55646–55647 | P4 | hypothesis | Each retained component lies in the current label's level-s complement and in Z_h, with the usual Ω–Λ nesting. | assumed | Current label; Y⁽ˢ⁾; Z | "moreover" |
| 55648–55649 | P5 | hypothesis | The level-s member containing a retained component is that component and is a closed cell union. | assumed | Y⁽ˢ⁾; level-s cells | "a closed union" |
| 55651–55652 | Graded-count hypothesis (e) | hypothesis | The first prepared member lies in Λ, which retains an eight-cell margin in Z. | assumed | Z″_{h+1}; Λ; Z | "eight" |
| 55655–55663 | Shell index j(x), cell cover [A]_i, neighbourhood, and n_old | definition | The shell index identifies a label shell and n_old counts older collar contributions outside their prepared sets. | definition | Ω_j; A⁽ˢ⁾_i; a_i | "shell index" |
| 55664–55669 | 4.18:eq-graded-count-a | estimate | The old profile excess is nonnegative and bounded by b₀ times the older contribution count. | proved conditionally | 4.18:eq-profiles-admissible-b; 4.18:eq-coupling-excess-b; 4.18:def-coupling-excess | "By" |
| 55670–55679 | 4.18:eq-graded-count-b | estimate | The count is at most c₁(k−j(x))+c₂R_k and its support lies inside older components with a five-cell inner margin and an eight-cell outer margin. | proved conditionally | Graded-count hypotheses; older-window bound; prepared five-layer geometry | "Then for every" |
| 55682–55784 | Proof of 4.18:lem-graded-count | proof | Localization excludes contributions from two different older steps and then supplies the graded count and support margins. | proved conditionally | (a)–(e), P1–P5; older-window lemma; B-CMP122a (1.11); B-CMP119 (2.1) | "uses them only as stated" |
| 55683–55705 | Orientation for P1–P5 and (e) | remark | The cited construction motivates the geometric clauses without deriving those hypotheses here. | assumed | B-CMP122a prepared sequence, (1.11); B-CMP119 (2.1); B-CMP122b p. 390; closure geometry | "are hypotheses of the lemma" |
| 55707–55709 | Contributing pair | definition | A pair contributes at x when x is in its enlarged cell cover but outside its older prepared set. | definition | A⁽ˢ⁾_i; cell cover; n_old | "contributes" |
| 55711–55722 | Localization of one contribution | proof | A contributing point lies in Y⁽ˢ⁾ and outside the older first prepared member. | proved conditionally | P1; P2; 4.18:eq-scales-partitions-a; a_i≤a_s | "hence" |
| 55724–55742 | At most one step contributes | proof | Two distinct contributing steps contradict the nesting assumptions, so at most N₀(s)−1 pairs contribute. | proved conditionally | Localization; P1; P3 | "which contradicts" |
| 55744–55748 | The shell index | proof | A contributing step satisfies j(x)≤s because its retained component avoids Ω_{s+1}. | proved conditionally | P4; decreasing Ω_j; shell-index definition | "Hence" |
| 55750–55759 | The count | proof | The older-window lemma and the shell-index inequality give the asserted graded count. | proved conditionally | (a)–(c); 4.18:lem-older-window; 4.18:eq-older-window-a | "therefore applies" |
| 55761–55783 | The support | proof | Cited five-layer geometry and the assumed outer margin establish all support inclusions and distances. | proved conditionally | Localization; P4; (e); B-CMP122a (1.11); B-CMP119 (2.1) | "This proves" |
| 55786–55794 | 4.18:rem-graded-form — Why the count must be graded by level | remark | The text argues that current coupling alone cannot control the supremum count and directs subsequent uses to the graded bound. | sketched | 4.18:lem-graded-count; oldest contributing step; B-CMP122b graded bound | "To see this" |
| 55791 | Bałaban's shell-graded bound and decay | estimate | The cited construction controls shell growth by O(1)(k−j) and scaled decay of H_{k,Z}. | cited | B-CMP122b; Ω″ shells; H_{k,Z} | "Ba{\l}aban's own graded bound" |
| 55793 | Subsequent-use rule | requirement | All subsequent uses of the older-member count must use its graded form rather than a supremum over Z. | assumed | n_old; graded bound | "every subsequent use" |
| 55796–55977 | 4.18:prop-graded-excess — The graded excess bound in the large-field estimates | proposition | Ten groups of assumptions yield graded excess and remainder bounds with strengthened absorption ceilings and one extra power of R_k. | proved conditionally | 4.18:def-coupling-excess; older-window and graded-count lemmas; hypotheses I–X | "Assume the following." |
| 55798–55814 | Graded-excess standing setting | hypothesis | The proposition fixes the current operation, cell scales, flow ceiling, bounded increments, and N≤R_k. | assumed | B-CMP122a §1; B-CMP122b §1; older-window lemma; coupling-excess definition | "The ceiling" |
| 55815–55820 | 4.18:eq-graded-excess-1: zone_j | definition | A zone is the level-j shell restricted to Z, equivalently its prepared-shell version for j≤h. | definition | Ω_j; Ω″_j; B-CMP122a §1 | "put" |
| 55822–55835 | Imported small functions, cutoffs, coefficient, coupling and regime | definition | The notation imports m, m′, ζ₀, ζ₁, ζ, G, Γ″_j, c_Γ, x″, δ, and ν from Bałaban's bounds. | definition | B-CMP122b, especially (1.47); regime L⁻ᴺ≤(log g_k⁻²)⁻ν | "taken from" |
| 55837–55843 | Current-stage excess and remainders | definition | The stage excess is d⁽ⁿ⁾=e_n and T_d and T_d_old denote its full and old Z-part remainders. | definition | 4.18:def-coupling-excess; large-field estimates | "current stage" |
| 55844–55846 | C1 | definition | C1 names the coupling ceiling that absorbs the full remainder. | definition | B-CMP122b §1 ceilings; T_d | "denotes the ceiling" |
| 55847–55853 | Companion coupling, current support, and stage increments | definition | The companion coupling x° and increments w_{n+1}, w°_{n+1} are compared using current support E′ and old excess. | definition | 4.18:def-coupling-excess; hypothesis V | "stage increments" |
| 55854–55859 | Plaquette coefficients, majorants, and absorbed remainder | definition | Nonnegative coefficients t_p have zone, graded, and cutoff majorants, and Rem_abs names the companion's absorbed remainder. | definition | Hypotheses III, IV; companion estimate | "denotes the absorbed remainder" |
| 55864–55865 | I | hypothesis | All hypotheses and conclusions of the graded-count lemma hold on Z. | assumed | 4.18:lem-graded-count; 4.18:eq-graded-count-a, -b | "hypotheses" |
| 55866–55868 | II | hypothesis | The old excess is supported in the low-index zones and Z″_{h+1}, with those zones inside the ζ₀=1 region. | assumed | zone_j; Z″_k; ζ₀ | "Moreover" |
| 55869–55871 | III | hypothesis | The old remainder has a termwise plaquette bound whose zone sums are controlled by M_j. | assumed | d_old; t_p; M_j | "obeys the termwise bound" |
| 55872–55882 | IV | hypothesis | Graded and cutoff majorants are bounded by m′ and g_k²m and control the absorbed graded remainder. | assumed | B-CMP122b §1 small functions; M_j; Rem_abs | "The majorants satisfy" |
| 55883–55889 | V | hypothesis | Full remainder and pointwise stage differences split into a current N₀ contribution and the old excess, with current support inside ζ₀=1. | assumed | T_d; d⁽ⁿ⁾; w_{n+1}; w°_{n+1}; E′ | "Pointwise" |
| 55890–55894 | VI; C4 and C4′ | hypothesis | The companion estimate absorbs the original and enlarged constant weights under the respective ceilings obtained by changing the factor in t₄. | assumed | Companion estimate; t₄; b₀L; b₀(1+c₂)L | "equally absorbs" |
| 55895–55897 | VII | hypothesis | The cutoff ζ vanishes on the first prepared member except within a boundary layer of width 2u_h. | assumed | B-CMP122b §1 cutoff statement | "except" |
| 55898–55899 | VIII | hypothesis | On Γ″_j the prepared inverse coupling equals G+d_old and G has the original graded coefficient bound. | assumed | B-CMP122b (1.46)–(1.48) | "one has" |
| 55900–55904 | IX: absorption inputs | hypothesis | Six absorption and regime statements are explicitly assumed in their stated form. | assumed | B-CMP122b (1.47), §1 | "All six items are assumed" |
| 55906–55910 | IX.1; 4.18:eq-graded-excess-3 | estimate | The original coefficient is bounded successively by factors involving 1+k−j and (N+2)(1+h−j). | assumed | g_k; c_Γ; h; N | "All six items are assumed" |
| 55911–55912 | IX.2 | hypothesis | The polynomial dependence on N is absorbed into R_k² using N≤R_k. | assumed | 4.18:eq-graded-excess-3 | "goes into" |
| 55913–55914 | IX.3 | hypothesis | The polynomial dependence on h−j is absorbed into the stated exponential decay. | assumed | 4.18:eq-graded-excess-3; δ; M | "goes into" |
| 55915–55917 | IX.4 | hypothesis | The original R_k⁷ bound is small under the given lower floor on ν. | assumed | B-CMP122b (1.47), §1; p₀,q,r₀ | "It is small" |
| 55918–55919 | IX.5 | hypothesis | An R_k⁸ bound is small after increasing the ν floor by r₀. | assumed | Same regime; p₀,q,r₀ | "one further factor" |
| 55920 | IX.6 | hypothesis | The two floors on ν are independent of L. | assumed | IX.4, IX.5 | "do not depend" |
| 55922–55925 | X | hypothesis | Positivity of x″ζ₁ persists and the companion identity acquires the old-excess contribution. | assumed | x″; x°; d_old; ζ₁; companion estimate | "the latter is the identity" |
| 55930–55933 | Conclusion (1); 4.18:eq-graded-excess-a | estimate | The old excess on a low-index zone is bounded by b₀c₁(k−j)+b₀c₂R_k. | proved conditionally | I; graded-count bounds | "Then the following hold." |
| 55934–55940 | Conclusion (2); 4.18:eq-graded-excess-b | estimate | Both old and full remainders are bounded by graded m′ terms and constant R_kg_k²m terms. | proved conditionally | I–V; N₀≤R_k | "obeys" |
| 55941–55950 | C1′; 4.18:eq-graded-excess-4 | requirement | The strengthened ceiling requires the displayed enlarged remainder majorant to be at most one. | assumed | Ř_k alternative or R_k; b₀,c₁,c₂; m,m′ | "under (C1$'$)" |
| 55951–55961 | Conclusion (3); 4.18:eq-graded-excess-5 | estimate | The companion stage-increment difference splits into graded and constant supported weights absorbed using IV and C4′. | proved conditionally | II; IV–VI; 4.18:eq-graded-excess-a; N₀≤R_k | "The constant part is absorbed" |
| 55962–55964 | Conclusion (4): d_old ζ=0 | identity | Old excess contributes nothing to the ζ term and leaves that term's ceilings unchanged. | proved conditionally | I; II; VII; graded-count support distance | "contributes nothing" |
| 55965–55973 | Conclusion (5): modified Γ″ coefficient and R_k⁸ absorption | estimate | The coefficient gains b₀c₂R_k and a changed graded constant, with R_k⁸ absorption and unchanged positivity. | proved conditionally | VIII–X; excess bound; current ceiling; ν floor | "is small when" |
| 55974–55975 | Conclusion (6): stage-excess bound | estimate | Stage excess on zone j′ is bounded by b₀ times N₀+c₁(k−j′+1)+c₂R_k. | proved conditionally | V; 4.18:eq-graded-excess-a | "On" |
| 55979–56121 | Proof of 4.18:prop-graded-excess | proof | The proof inserts the graded count into majorants, companion bounds, cutoff support, and coefficient absorption. | proved conditionally | I–X; older-window and graded-count lemmas | "This proves" |
| 55980–55985 | Proof of pointwise old-excess bound | proof | The graded-count estimates directly imply conclusion (1). | proved conditionally | I; 4.18:eq-graded-count-a, -b; nonnegative constants | "By hypothesis (I)" |
| 55987–56009 | Proof of old remainder bound | proof | Splitting each zone's weight into graded and constant parts allows the two majorant bounds to be applied. | proved conditionally | II–IV; conclusion (1) | "By the termwise bound (III)" |
| 56011–56023 | Proof of full remainder and strengthened ceiling | proof | The full-remainder assumption and N₀≤R_k yield conclusion (2) and absorption under C1′. | proved conditionally | V; old remainder estimate; C1′ | "This proves" |
| 56025–56043 | Proof for the companion system | proof | Supported stage increments split as claimed and VI and IV absorb the constant and graded parts. | proved conditionally | II; IV–VI; 4.18:eq-graded-excess-a | "by the graded majorant bound" |
| 56045–56058 | Proof for the ζ term | proof | The old support's five-cell margin exceeds the exceptional cutoff layer, forcing the product with ζ to vanish. | proved conditionally | 4.18:eq-graded-count-b; II; VII; scale relations | "Hence" |
| 56060–56112 | Proof for B-CMP122b (1.47) coefficient | proof | Enlarging the graded coefficient and adding the constant term produces the stated R_k⁸ bound and companion analogue. | proved conditionally | VIII–X; IX.1–IX.6; older-window ceiling; N≤R_k | "By (IX.5)" |
| 56114–56120 | Proof of stage-excess bound | proof | Adding the current N₀ term to the old graded excess proves conclusion (6). | proved conditionally | V; 4.18:eq-graded-excess-a | "which is (6)" |
| 56123–56279 | 4.18:thm-action-domain — The domain of the plaquette-action excess in the large-field bounds | theorem | Under the listed inputs, a small coupling ceiling permits enlarged excess-support domains, modified Wilson bounds, unchanged stage constants, and locality. | proved conditionally | Parameter regime; first and second Wilson-term theorems; preparatory-boundary theorem; graded count/excess; imported analytic inputs | "Assume the following statements." |
| 56125–56146 | Action-domain parameter and exponent requirements | requirement | Dimension four, size floors, analytic schedule, auxiliary scale, exponent windows, and the shifted ν floor are imposed. | assumed | 4.18:thm-preparatory-boundary; 4.4:def-post-step-space; 4.18:prop-graded-excess; 4.18:eq-older-window-a | "Assume further" |
| 56150–56154 | First Wilson-term theorem input | hypothesis | Its geometric-class excess estimates, support, cell count, volume, non-containment, and locality statements are assumed. | assumed | B-CMP122b; first Wilson-term theorem | "The first Wilson-term theorem" |
| 56155–56160 | Second Wilson-term theorem input | hypothesis | The all-component Wilson estimates are assumed except their old-excess bound on low-index zones. | assumed | Second Wilson-term theorem; d_old; prepared zones | "excepting its bound" |
| 56161–56162 | Preparatory boundary input | hypothesis | The boundary-term theorem and all its standing hypotheses are assumed. | assumed | 4.18:thm-preparatory-boundary | "together with its standing hypotheses" |
| 56163–56165 | Graded count and excess inputs | hypothesis | The two local graded results are taken as inputs to the domain theorem. | assumed | 4.18:lem-graded-count; 4.18:prop-graded-excess | "together with" |
| 56166–56171 | Imported m, m′, and Ξ inputs | hypothesis | Statements fixing the ordinary, graded, and additional small functions are assumed in the Wilson theorems' forms. | assumed | Bałaban's papers; both Wilson-term theorems | "forms stated" |
| 56172–56173 | Second-remainder input; σ̄ | hypothesis | The cited bound on the second remainder of the excess term is assumed and its right side is called σ̄. | assumed | B-CMP122b (1.32); clause (ii) | "whose right member is the quantity" |
| 56174 | Cutoff input | hypothesis | Bałaban's cutoff-function statement is assumed. | assumed | B-CMP122b | "the statement" |
| 56175–56176 | Three additional paper inputs | hypothesis | Three further statements used by the Wilson proofs are assumed without being individually identified in this chunk. | assumed | Bałaban's papers; two Wilson-term proofs | "three further statements" |
| 56177 | Stage-term regularity input | hypothesis | The stage-term regularity statement is assumed. | assumed | Stage terms | "the regularity statement" |
| 56180–56188 | γ_W and 4.18:eq-action-domain-1 | hypothesis | At the selected step the flow holds through k, g_k is below γ_W, and N₀<N≤R_k with the logarithmic regime holds. | assumed | Flow hypothesis of 4.18:thm-preparatory-boundary; γ_W | "is in force" |
| 56189–56195 | Prepared-stage family; D and N; 4.18:eq-action-domain-2 | construction | Running the prepared-member profiles at every preparatory stage defines D as the union of cell-cover collars and N as a top-member enlargement. | definition | B-CMP122a component class; φ_A; Z″_i; a_i | "Put" |
| 56198–56208 | Clause (i): support, cell count, volume, non-containment | estimate | The excess support lies in D⊂N⊂Z with eight layers removed, with explicit cell and volume bounds but no general inclusion D⊂Λ. | proved conditionally | First and second Wilson-term inputs | "In general" |
| 56209–56214 | Clause (ii): replacement of excess-support domain | estimate | Excess-sensitive estimates use D in place of Λ and the localization statement uses Λ∪D. | proved conditionally | Wilson-term theorems; B-CMP122b (1.14)–(1.48) | "holds with" |
| 56215–56227 | Clause (ii): two excess remainders | estimate | The two Z-part remainders are bounded by the companion contribution plus the stated graded and exponentially small corrections. | proved conditionally | B-CMP122b (1.32); companion profiles; σ̄; m,m′,Ξ; graded-excess proposition | "The second is bounded by" |
| 56228–56231 | 4.18:eq-action-domain-3 | estimate | On every prepared shell the nonnegative coupling excess obeys the enlarged graded bound. | proved conditionally | Wilson inputs; 4.18:eq-graded-excess-a | "the graded bound reads" |
| 56232–56235 | Clause (ii): B-CMP122b (1.37) | estimate | The second term gains at most one beyond the companion term, absorbed into its absolute constant. | proved conditionally | Two Wilson-term theorems | "included in the constant" |
| 56236–56242 | Clause (ii): B-CMP122b (1.46)–(1.48) | estimate | The coefficient acquires the stated graded and constant corrections, R_k⁷ becomes R_k⁸, and (1.48) is unchanged. | proved conditionally | 4.18:prop-graded-excess; ν floor | "holds verbatim" |
| 56243–56247 | Clause (ii): C_k and unchanged integration domains | remark | The collected correction remains a finite localized small sum while integration domains and N≤R_k remain unchanged. | proved conditionally | B-CMP122b (1.14)–(1.48); Wilson inputs | "are unchanged" |
| 56249–56259 | Three readings and the geometric special case | remark | The first two older-label readings eliminate old-excess corrections, while the third needs the graded replacement and three substitutions. | proved conditionally | First/second Wilson theorems; 4.18:lem-graded-count; 4.18:eq-graded-excess-a; graded-excess proposition | "Under the" |
| 56260–56269 | Clause (iii): stage term representation, holomorphy, and bound | estimate | Each preparatory-stage term has the cited representation, holomorphy domains, and bound with unchanged C₀=c_G+1 and prescribed decay. | proved conditionally | 4.18:thm-preparatory-boundary; B-CMP122a (1.63)–(1.70); 4.18:rem-decay-rates | "it is holomorphic" |
| 56270–56273 | Clause (iii): weight-difference support and C₀ share | estimate | Additional weight-difference support lies on the specified collar inside R_n and has the companion's share of C₀. | proved conditionally | B-CMP122a (1.62); 4.18:lem-weight-difference; preparatory-boundary theorem | "constant $C_0$ is unchanged" |
| 56274–56277 | Clause (iv): locality | estimate | D, current excess support, and all modified supports lie inside the eight-layer interior and hence inside X_a. | proved conditionally | Wilson locality inputs; weight-difference lemma; graded-count bound | "supports of all modified terms" |
| 56281–56340 | Proof of 4.18:thm-action-domain | proof | The proof assembles the assumed Wilson and stage results, graded substitutions, and a common small coupling threshold. | proved conditionally | All action-domain hypotheses; 4.18:lem-weight-difference | "which are hypotheses of the theorem" |
| 56282–56290 | Proof of clauses (i), (iv) | proof | Assumed Wilson support and locality statements combine with weight-difference and old-member support control. | proved conditionally | Wilson inputs; 4.18:lem-weight-difference (b); 4.18:eq-graded-count-b | "together with two further inputs" |
| 56292–56313 | Proof of clause (ii) | proof | The first Wilson theorem covers the geometric case, and graded replacements adapt the second theorem to the third older-label reading. | proved conditionally | First/second Wilson theorems; graded count/excess; strengthened ceilings; shifted ν floor | "hypothesis for everything except" |
| 56315–56319 | Proof of clause (iii) | proof | The preparatory-boundary theorem supplies stage properties and its weight-difference lemma supplies support. | proved conditionally | 4.18:thm-preparatory-boundary and standing hypotheses; 4.18:lem-weight-difference | "a hypothesis of the" |
| 56321–56339 | Construction and positivity proof of γ_W | proof | Taking the least of finitely many small-coupling thresholds yields a positive common ceiling without specifying its value. | proved conditionally | Wilson ceilings with graded strengthening; e⁻¹; stage γ₀; small-function threshold behavior | "No value" |
| 56342–56359 | 4.19:lem-flow-bounds — Two-sided flow bounds from per-step bounds | lemma | Summed baseline lower bounds and bounded perturbations imply two-sided inverse-coupling flow bounds. | proved conditionally | 4.19:eq-flow-bounds-1, -2; recurrence x_l=x_{l−1}−β_l | "assume that" |
| 56343–56345 | Flow recurrence and increment decomposition | definition | Real inverse couplings are generated by subtracting increments split into unmarked and large-field parts. | definition | x₀; βᴬ_l; βᴿ_l; β⁰_l | "Put" |
| 56346–56348 | 4.19:eq-flow-bounds-1 | hypothesis | Each interval sum of baseline increments is at least its length times c₀ minus 2c₂. | assumed | β⁰_l; c₀,c₂; 0≤i≤j≤n | "assume that" |
| 56349–56353 | 4.19:eq-flow-bounds-2 | hypothesis | The unmarked increments are bounded and close to baseline while large-field increments obey a small uniform bound. | assumed | c₀; C_β; ς̄ | "assume that" |
| 56354–56358 | λ♯, B♯, c₅; 4.19:eq-flow-bounds-3 | estimate | The defined constants give λ♯≥c₀/4 and linear upper and lower flow bounds with additive defect c₅. | proved conditionally | 4.19:eq-flow-bounds-1, -2 | "Then" |
| 56361–56368 | Application input: finite one-loop law | requirement | The interval baseline bound is supplied by a one-loop lemma whose proof still has an incomplete step. | named open | 4.2:lem-one-loop | "whose proof is incomplete" |
| 56369–56378 | Application inputs: unmarked and large-field bounds and ceilings | requirement | The per-step estimates rely on the incomplete unmarked lemma, the large-field bound, and two explicit smallness ceilings. | assumed | 4.2:lem-unmarked; ε₁ᴵ≤c₀/(2C_rem); C′γ^(κ₀−8)≤min(c₀/4,1); constant-choice order | "together with the ceiling" |
| 56372–56375 | Incomplete unmarked-increment proof | requirement | One step in the unmarked-increment lemma supplying the error estimate is explicitly incomplete. | named open | 4.2:lem-unmarked | "whose proof is incomplete" |
| 56380–56412 | Proof of two-sided flow bounds | proof | Telescoping the recurrence and summing the two per-step inequalities proves the flow bounds and positivity of λ♯. | proved conditionally | 4.19:eq-flow-bounds-1, -2; recurrence | "telescoping gives" |
| 56414–56417 | No per-step sign | remark | The lemma asserts no sign for an individual flow difference and later arguments do not use one. | named open | 4.19:lem-flow-bounds | "No per-step sign" |
| 56419–56460 | 4.19:prop-clause-zero — Clause (0) concluded | proposition | Conditional on the listed RG and representation inputs, first passage defines K with explicit bounds and produces the specified terminal coupling window and lattice flow. | proved conditionally | H1–H6; (a), (a′), (b)–(h); 4.20:thm-representation at earlier levels; first-passage arithmetic | "Assume these jointly" |
| 56420–56422 | Clause-zero standing hypotheses | hypothesis | H1–H6 and the running inverse couplings started within the lower terminal window are assumed. | assumed | 2.2:not-hypotheses; 1.2:def-couplings; g_−(g) | "Assume" |
| 56424 | Clause-zero input (a) | hypothesis | Bałaban's one-step renormalization theorem is an input. | assumed | B-CMP109 Theorem 3 | "one-step renormalization theorem" |
| 56425–56427 | Clause-zero input (a′) | hypothesis | A widened small-cube version of condition (1.12) and its reproduction by each step are inputs. | assumed | B-CMP109 (1.12) | "the statement that the step" |
| 56428–56430 | Clause-zero input (b) | hypothesis | The finite one-loop law and unmarked-increment bounds are assumed despite their explicitly incomplete starred proof steps. | assumed | 4.2:lem-one-loop; 4.2:lem-unmarked | "incomplete at the step" |
| 56431 | Clause-zero input (c) | hypothesis | The large-field coupling-increment bound is assumed. | assumed | Large-field part of the increment | "the bound" |
| 56432–56433 | Clause-zero input (d) | hypothesis | Localized terms are assumed independent of the small-field region. | assumed | 4.4:cor-localised-independence | "the independence" |
| 56434 | Clause-zero input (e) | hypothesis | The operator bounds at free current are assumed. | assumed | Free-current operator bounds | "the operator bounds" |
| 56435 | Clause-zero input (f) | hypothesis | The representation and bound of large-field terms are assumed. | assumed | Large-field terms | "the representation and bound" |
| 56436 | Clause-zero input (g) | hypothesis | The one-power hereditary class is assumed. | assumed | One-power hereditary class | "the one-power hereditary class" |
| 56437 | Clause-zero input (h) | hypothesis | Terms localized in non-wrapping domains are assumed independent of the torus. | assumed | Torus-independence statement | "the torus-independence" |
| 56439–56441 | Joint earlier-level representation hypothesis | hypothesis | Whenever earlier inverse couplings stay above γ⁻², the effective-density representation is assumed at every already reached level. | assumed | 4.20:thm-representation | "at the scales already reached" |
| 56442–56448 | 4.19:eq-clause-zero-1; existence and growth of K | estimate | The first-passage cutoff is a nonnegative integer between the displayed affine bounds and tends to infinity with vanishing bare coupling. | proved conditionally | Clause-zero inputs; 1.2:def-flow-constants; 4.2:lem-first-passage | "Consequently" |
| 56450–56458 | Coupling window, 4.19:eq-clause-zero-2, and realized lattice sequence | estimate | Couplings remain below g, the last lies in its terminal window, the two-sided flow bound holds, and K lattice steps reproduce the sequence. | proved conditionally | Clause-zero inputs; flow-bounds lemma; H4,H5; torus independence | "produce exactly" |
| 56462–56524 | Proof of clause zero | proof | The coupling portion of a joint induction applies first-passage arithmetic and then identifies the abstract flow with the admissible lattice construction. | proved conditionally | (a), (a′), (b)–(h); H1–H6; earlier representation; flow and first-passage lemmas | "the present proof concerns the couplings" |
| 56463–56484 | Structure: joint induction and increment facts | proof | The stated earlier-level inputs give a coupling-only increment and two-sided bounds, with the full joint induction assigned to the representation theorem. | proved conditionally | 4.20:thm-representation; 4.2:def-increment; 4.19:lem-flow-bounds; 1.2:def-flow-constants | "carried out in the proof" |
| 56486–56511 | All members but the last | proof | Threshold separation and first-passage arithmetic establish finite K, terminal windows, flow bounds, and unbounded realized cutoffs. | proved conditionally | H4; 2.3:rem-thresholds; 4.2:lem-first-passage; preceding increment facts | "That lemma yields" |
| 56513–56523 | The last member: lattice realization | proof | Coupling-only and torus-independent increments plus H5 admissibility identify the K lattice steps with the abstract flow. | proved conditionally | Input (h); H5; 4.19:eq-clause-zero-2; increment dependence; cube-size bounds described here | "Together the two facts show" |
| 56526–56528 | Identification with clause (0) and fixed-depth input | remark | These conclusions are the main theorem's clause (0), which the earlier fixed-depth-window paragraph takes as a hypothesis. | definition | 3.1:thm-main; 4.1:thm-clause-zero | "its hypothesis" |
| 56530–56547 | 4.19:prop-containment — Containment: Bałaban's one coupling hypothesis holds along the flow | proposition | Clause (0) and the terminal ceilings place every effective coupling strictly below γ and satisfy Bałaban's stability hypothesis. | proved conditionally | H4; H3 terminal ceiling; 4.19:prop-clause-zero; 2.3:rem-thresholds | "Assume hypothesis" |
| 56532–56535 | Containment assumptions | hypothesis | H4, clause (0), and the stated terminal ceiling from H3 are imposed. | assumed | 2.2:not-hypotheses; 3.1:thm-main; 4.19:prop-clause-zero; 2.3:rem-thresholds | "and the terminal ceiling" |
| 56536–56538 | 4.19:eq-containment-1 | estimate | Each inverse coupling exceeds g⁻² and hence γ⁻²+c₅+1. | proved conditionally | Containment assumptions | "Then for all" |
| 56539–56545 | Containment consequences and ultraviolet-stability hypothesis | estimate | All lower thresholds up to γ⁻²+c₅+1 hold, including the effective-coupling hypothesis of the cited stability theorem. | proved conditionally | 4.19:eq-containment-1; B-CMP122b Theorem 1 | "is satisfied" |
| 56549–56566 | Proof of containment | proof | Monotonicity of inverse squares turns the three coupling ceilings into the claimed lower-bound chain and its consequences. | proved conditionally | Clause (0); H4; H3 | "the first inequality" |
| 56568–56582 | 4.19:cor-windows — Coupling windows at fixed depth and subsequential limit couplings | corollary | At every fixed depth before first passage the inverse couplings lie in explicit windows and a common subsequence converges at every depth. | proved conditionally | Clause (0); 3.1:thm-main; 4.19:prop-clause-zero; g₀⁽ⁱ⁾↓0 | "Assume clause" |
| 56573–56575 | 4.19:eq-windows-1 | estimate | Finite-cutoff inverse couplings lie in the displayed half-open fixed-depth window. | proved conditionally | Clause (0) flow and terminal bounds | "Then" |
| 56576–56581 | 4.19:eq-windows-2 | estimate | Diagonal subsequential inverse-coupling limits lie in the closed windows, including the terminal coupling interval. | proved conditionally | Clause (0); compact fixed-depth windows; continuity | "Along a subsequence" |
| 56584–56630 | Proof of fixed-depth windows and subsequential limits | proof | Terminal bounds give finite windows and compactness plus a diagonal extraction gives simultaneous limits. | proved conditionally | Clause (0); compactness; continuity of inverse square root | "We now make a diagonal extraction." |
| 56597–56599 | 4.19:eq-windows-3 | estimate | Adding the terminal bound to the flow inequality gives the preliminary fixed-depth interval. | proved conditionally | Clause (0); flow bound; terminal window | "Adding these bounds" |
| 56603–56609 | Compact intervals I_s | construction | Each depth's eventually defined inverse couplings lie in a positive compact interval I_s. | definition | 4.19:eq-windows-1; K_i→∞ | "compact" |
| 56611–56622 | Diagonal extraction and limit definition | construction | Nested convergent subsequences and their diagonal define g_{∞,s} simultaneously for every depth. | proved conditionally | Compactness of I_s; K_i→∞; continuous inverse square root | "choose a further subsequence" |
| 56624–56629 | Terminal limit window | proof | At depth zero the inverse-square-root map converts I₀ into [g_−(g),g]. | proved conditionally | c₅≥0 from 1.2:def-flow-constants; I₀ | "Applying" |
| 56632–56647 | 4.19:rem-not-asserted — What clause (0) does not assert | remark | The remark lists tuning, realization, monotonicity, sign, full-limit, and regularity claims excluded from clause (0). | named open | 3.1:thm-main; 4.1:thm-clause-zero; 4.19:prop-clause-zero; fixed-depth corollary | "asserts none of the following" |
| 56636 | Exact prescribed-cutoff tuning | requirement | Clause (0) does not assert a bare coupling attaining g_K=g at prescribed K. | named open | Clause (0) | "asserts none of the following" |
| 56637–56638 | All-integer realization and monotonicity | requirement | Clause (0) does not assert realization of every integer K or monotonicity of K or a tuned bare coupling. | named open | Clause (0) | "nor the monotonicity" |
| 56639–56640 | Per-step signs | requirement | Clause (0) does not assert a sign for individual inverse-coupling differences or increments. | named open | Clause (0) | "Any per-step sign" |
| 56641–56644 | Full fixed-depth convergence | requirement | Clause (0) asserts only subsequential fixed-depth convergence, not convergence along the entire first-passage flow. | named open | Fixed-depth-window corollary 4.19:cor-windows | "without passing to subsequences" |
| 56645 | Increment regularity | requirement | Clause (0) does not assert regularity of increments as functions of the couplings. | named open | Clause (0) | "Any regularity" |
| 56649–56650 | Proof of 4.19:rem-not-asserted, opening only | proof | The proof announces explanations for the exclusions but no explanation appears before this chunk ends. | sketched | 4.19:rem-not-asserted; continuation outside chunk | "We explain why each item lies outside clause (0)." |

## Forward and backward references

Each entry identifies the location of the reference in this chunk and its target; repeated uses are retained, with contiguous references grouped when they serve the same statement. No target outside this chunk was read.

- **55374–55375:** B-CMP122a and B-CMP122b passages quoted in the following proof are said not to exclude the retained-region configuration.
- **55380–55388:** B-CMP122a supplies the quoted component class and conditions (i), (ii).
- **55389–55395:** B-CMP122a (1.2) supplies the last N one-step operations and carried older operation; (1.11) fixes the unchanged lower Z″_j.
- **55395–55398:** B-CMP122a supplies the mixed-history rule retaining B_k⁽ⁿ⁾ as boundary terms when integrations stop in a component.
- **55407–55420:** B-CMP122b p. 390 supplies the new large-field-region formula; B-CMP122a (1.72) supplies the retained component class, factors, and T′_k(Y_i).
- **55422–55427:** Definition `4.18:def-profiles-admissible` defines which complements carry profiles; B-CMP122b's post-R label description in the form B-CMP119 (2.18) would decide the three readings and is not derived here.
- **55429–55442:** B-CMP122b supplies the post-operation coupling formula; `4.18:def-profiles-admissible` supplies the retained profile's vanishing rule.
- **55446–55450:** B-CMP122a supplies the prepared members' M-cube rather than cell geometry in the older short window.
- **55478–55481:** The coupling-flow statement and `1.2:def-couplings` supply the flow consequences and increment notation in `4.18:eq-older-window-1`.
- **55488–55494:** `4.18:not-scales-partitions` defines R_m; `4.18:def-prepared-sequence` fixes h; B-CMP122a supplies the older-operation N₀ relation uniformly in the step.
- **55499–55503:** `4.18:eq-older-window-a` is extended to the alternative parameters of `4.18:eq-older-window-2`.
- **55508–55509, 55517–55518, 55524–55525:** The proof uses `4.18:eq-older-window-1` for the ceiling and flow and `4.18:eq-older-window-2` for alternative cell parameters.
- **55550–55552:** `1.1:def-lattice` supplies that L is an odd integer greater than one.
- **55586–55589:** `4.18:eq-older-window-2` supplies the alternative lower bound; Bernoulli's inequality is named for the elementary estimate.
- **55599–55605:** The proof identifies its result and constant dependence with `4.18:eq-older-window-a` and its flow input `4.18:eq-older-window-1`.
- **55609–55617:** `4.18:def-prepared-sequence`, `4.18:eq-scales-partitions-a`, and B-CMP122a provide component, label, scale, and older-operation notation.
- **55624–55627:** `4.18:def-coupling-excess` and `4.18:lem-older-window` provide hypotheses (a), (b).
- **55664–55668:** `4.18:eq-profiles-admissible-b`, `4.18:eq-coupling-excess-b`, and `4.18:def-coupling-excess` supply the count-to-excess bound.
- **55670:** Constants are attributed to `4.18:eq-older-window-a` (the source names c₁,c₂ here, while that displayed bound writes 2R_k).
- **55683–55695:** B-CMP122a's prepared sequence, B-CMP122a (1.11), and B-CMP119 (2.1) are offered as orientation for P1, not as a derivation of the assumed clauses.
- **55695–55701:** Ten-layer geometry, bounds on older steps, closure property (ii), and B-CMP122b's “intersect, or touch” component relation are the stated counterparts of P2 and P3.
- **55701–55705:** B-CMP122b p. 390 and B-CMP119 (2.1) are the counterparts of P4; prepared nesting and Λ's eight-layer margin are the counterpart of (e).
- **55714–55715:** `4.18:eq-scales-partitions-a` supplies the cell side used in localization.
- **55739–55740:** The zero-contribution case is identified with the first line of `4.18:eq-graded-count-b`.
- **55750–55759:** `4.18:lem-older-window` and `4.18:eq-older-window-a` give the nonzero count, identified with `4.18:eq-graded-count-b`.
- **55763–55783:** B-CMP122a (1.11) and B-CMP119 (2.1) supply the five-layer support geometry; the result is identified with the remaining lines of `4.18:eq-graded-count-b`.
- **55787:** `4.18:lem-graded-count` supplies the graded count discussed in the remark.
- **55791:** B-CMP122b supplies its own shell-graded bound and scaled-decay treatment of H_{k,Z}.
- **55798–55813:** `4.18:def-coupling-excess`, `4.18:lem-older-window`, `4.18:lem-graded-count`, B-CMP122a §1, B-CMP122b §1, and `4.18:eq-older-window-a` supply the proposition's setting, N≤R_k, constants, and bounded increments.
- **55819:** B-CMP122a §1 supplies equality of original and prepared zones for j≤h.
- **55822–55835:** B-CMP122b supplies the small functions, cutoffs, class coefficient, prepared coupling, decay, and ν regime; (1.47) supplies Γ″_j and c_Γ.
- **55839–55840, 55847–55848:** `4.18:def-coupling-excess` defines current-stage excess and companion coupling.
- **55844–55846:** C1 strengthens ceilings in B-CMP122b §1.
- **55852–55858:** Forward references to V and III–IV specify stage differences, plaquette coefficients, and majorants.
- **55864–55865:** `4.18:lem-graded-count` and `4.18:eq-graded-count-a`, `-b` are explicitly assumed through I.
- **55872–55874:** B-CMP122b §1 supplies the small-function majorant statements assumed as IV.
- **55890–55894:** The companion estimate and its C4 ceiling through t₄ are assumed in VI, together with the enlarged C4′ version.
- **55895–55899:** B-CMP122b §1 supplies the cutoff-layer statement; (1.46)–(1.48) supply the setting of VIII.
- **55900–55920:** B-CMP122b (1.47) supplies the absorption being assumed in IX.1–IX.3; §1 supplies the sufficiently-large-ν regime referenced by IX.4–IX.6.
- **55922–55925:** The companion estimate's identity is restated with a nonzero old excess in X.
- **55941–55950:** `4.18:eq-graded-excess-4` defines the replacement C1′; `4.18:lem-older-window` supplies its alternative cell parameter; `4.18:eq-graded-excess-b` is the bound absorbed.
- **55960–55961:** C4′ and the graded majorant input supply the two absorptions in conclusion (3).
- **55969–55973:** B-CMP122b (1.47), (1.48) are the original coefficient and positivity estimates being modified or preserved.
- **55980–55985:** I, `4.18:lem-graded-count`, its two bounds, and `4.18:lem-older-window` give `4.18:eq-graded-excess-a`.
- **55987–56009:** III, II, `4.18:eq-graded-excess-a`, and IV give the old remainder bound.
- **56011–56023:** V yields `4.18:eq-graded-excess-b`; `4.18:eq-graded-excess-4` replaces C1 and strengthens B-CMP122b §1 ceilings.
- **56025–56043:** V, II, `4.18:eq-graded-excess-a`, VI, and IV prove `4.18:eq-graded-excess-5` and the companion absorption statement.
- **56045–56058:** `4.18:eq-graded-count-b`, VII, and II supply the separation and vanishing used for the ζ term.
- **56060–56082:** VIII and `4.18:eq-graded-excess-a` modify B-CMP122b (1.47); IX.1 and `4.18:eq-graded-excess-3` supply its absorption, with the ceiling from `4.18:lem-older-window`.
- **56091–56099:** `4.18:lem-older-window` supplies R_k≥3; B-CMP122b (1.47), IX.5, and IX.6 supply the original factor, new smallness, and L-independent floor.
- **56101–56112:** B-CMP122b (1.48) and X supply positivity and the companion identity; conclusion (5)'s coefficient bound is reused.
- **56114–56120:** V and `4.18:eq-graded-excess-a` prove the stage-excess bound.
- **56130–56136:** `4.18:thm-preparatory-boundary` supplies the assumed stage theorem's floors and auxiliary constraint; `4.4:def-post-step-space` defines the layered analyticity schedule.
- **56141–56146:** `4.18:prop-graded-excess` supplies the explicit shifted ν floor for B-CMP122b (1.46)–(1.48); `4.18:eq-older-window-a` supplies constants.
- **56150–56160:** The first and second Wilson-term theorems are assumed, with the second's old-excess bound excepted; the domain definition is referred forward to `4.18:eq-action-domain-2`.
- **56161–56165:** `4.18:thm-preparatory-boundary` with standing hypotheses, `4.18:lem-graded-count`, and `4.18:prop-graded-excess` are explicit inputs.
- **56166–56178:** The statements assumed with the Wilson theorems supply m, m′, Ξ, the second remainder of B-CMP122b (1.32), cutoffs, three further paper statements, and stage regularity.
- **56183–56191:** `4.18:thm-preparatory-boundary` names the flow hypothesis; B-CMP122a supplies the component class for the profile-run construction.
- **56208–56214:** B-CMP122a (1.73) identifies Λ; B-CMP122b (1.14)–(1.48), especially (1.14), are the estimates whose excess-support domain changes.
- **56215–56227:** B-CMP122b (1.32) supplies the two-remainder decomposition, assumed second-remainder right member σ̄, and decay constant.
- **56232–56242:** The Wilson-term theorems specify the form of B-CMP122b (1.37); `4.18:prop-graded-excess` fixes O′ in the replacements to (1.46)–(1.48).
- **56243–56247:** B-CMP122b (1.14)–(1.48) supply C_k and the integration domains left unchanged.
- **56249–56259:** The geometric first Wilson theorem is equated to the second with zero old excess; `4.18:lem-graded-count`, `4.18:eq-graded-excess-a`, and `4.18:prop-graded-excess` specify the third-reading substitution.
- **56263–56268:** B-CMP122a (1.63), (1.64)–(1.69), and (1.70) supply representation, holomorphy spaces, and bounds, read through `4.18:thm-preparatory-boundary`; `4.18:rem-decay-rates` supplies decay rates.
- **56270–56277:** B-CMP122a (1.62) identifies the weight-difference member; the Wilson locality statement defines X_a.
- **56282–56290:** The proof uses assumed Wilson support and locality, `4.18:lem-weight-difference` (b), and `4.18:eq-graded-count-b` of `4.18:lem-graded-count`.
- **56292–56313:** The two Wilson theorems, `4.18:eq-graded-excess-a`, `4.18:prop-graded-excess`, and `4.18:lem-graded-count` supply clause (ii), including `4.18:eq-action-domain-3` and the modified B-CMP122b (1.32), (1.46)–(1.48) estimates.
- **56315–56319:** `4.18:thm-preparatory-boundary` and `4.18:lem-weight-difference` supply clause (iii) and support for B-CMP122a (1.62).
- **56323–56330:** The first and second Wilson theorems' ceilings, strengthened by `4.18:prop-graded-excess`, and the stage theorem's γ₀ from `4.18:thm-preparatory-boundary` define γ_W.
- **56361–56368:** `4.2:lem-one-loop`, explicitly incomplete at one step, supplies `4.19:eq-flow-bounds-1` at the next induction level.
- **56369–56378:** `4.2:lem-unmarked`, explicitly incomplete at one step, the large-field-increment bound, and the order of choice of constants supply `4.19:eq-flow-bounds-2` under two ceilings.
- **56386–56411:** The proof uses `4.19:eq-flow-bounds-2` and `-1` to obtain both sides of `-3` and λ♯≥c₀/4.
- **56415–56416:** `4.19:lem-flow-bounds` is identified as making no per-step sign assertion.
- **56420–56421:** `2.2:not-hypotheses` supplies H1–H6; `1.2:def-couplings` supplies the running inverse couplings.
- **56424–56427:** B-CMP109 Theorem 3 and the widened, reproducible form of B-CMP109 (1.12) are assumed.
- **56428–56437:** `4.2:lem-one-loop` and `4.2:lem-unmarked` retain their incomplete (*) steps; the large-field-increment bound, `4.4:cor-localised-independence`, free-current operator bounds, large-field representation/bound, one-power hereditary class, and torus-independence are inputs.
- **56439–56442:** `4.20:thm-representation` is assumed at already reached levels; `1.2:def-flow-constants` defines K.
- **56463–56473:** The joint induction for clause (0) and representation is assigned to the proof of `4.20:thm-representation`; the incomplete lemmas are reiterated and `4.19:lem-flow-bounds` supplies the coupling induction step.
- **56475–56484:** `4.2:def-increment` defines β_n; `4.19:lem-flow-bounds` gives `4.19:eq-clause-zero-2`; `1.2:def-flow-constants` fixes all constants used in that application.
- **56486–56498:** H4 and `2.3:rem-thresholds` give ceiling separation; `4.2:lem-first-passage` applies to the resulting initial segments.
- **56500–56510:** First-passage arithmetic yields `4.19:eq-clause-zero-1`; the preceding flow argument supplies `-2`, while H4 gives the terminal ceiling.
- **56513–56523:** Input (h), `4.19:eq-clause-zero-2`, and H5 supply torus independence, cube-size control, and admissibility of the declared pair (m,K).
- **56526–56528:** `3.1:thm-main` clause (0), its restatement `4.1:thm-clause-zero`, and that theorem's fixed-depth-window paragraph are identified with these conclusions and their use.
- **56532–56535:** `2.2:not-hypotheses` H4, `3.1:thm-main` clause (0) as `4.19:prop-clause-zero`, H3's terminal ceiling, and `2.3:rem-thresholds` are containment inputs.
- **56543–56545:** B-CMP122b Theorem 1 supplies the ultraviolet-stability theorem's effective-coupling hypothesis.
- **56550–56565:** `4.19:prop-clause-zero`, H4, and H3 prove `4.19:eq-containment-1` and verify the hypothesis of B-CMP122b Theorem 1.
- **56570–56571:** `3.1:thm-main` clause (0), through `4.19:prop-clause-zero`, is the sole stated research input to the fixed-depth corollary.
- **56585–56601:** Clause (0)'s two-sided flow and terminal bounds give `4.19:eq-windows-3`, then `-1`.
- **56603–56622:** Clause (0)'s lower bound on K and `4.19:eq-windows-1` supply the compact intervals; the diagonal extraction proves `4.19:eq-windows-2`.
- **56624–56629:** `1.2:def-flow-constants` supplies c₅≥0 for the terminal limit window.
- **56633–56644:** `3.1:thm-main`, `4.1:thm-clause-zero`, and `4.19:prop-clause-zero` are the claims being limited; the fixed-depth-window corollary in this section supplies only subsequential convergence.
- **56649–56650:** The proof of the final remark starts here and continues beyond the provided source range.

## Obligations named here

These are the text's explicit assumptions, requirements, and limits of establishment; an assumed input is not automatically a claim that the source intends to prove it later. Likewise, the final non-assertions are scope limits, not promises of future proofs.

- **55363–55367, 55422–55427:** One of the alternative lower-label descriptions (c1)–(c3) must be specified; the post-R label description deciding them is not derived in this section.
- **55382–55387:** The cited component class requires the size condition (i) and no-new-large-field/previous-region condition (ii).
- **55457–55474:** The two geometry conclusions are conditional on the chosen reading, (c1)/(c2) versus (c3).
- **55478–55487:** Assume the coupling-flow consequences at every level through k, including inverse-coupling comparison and bounded accumulated increments.
- **55488–55494:** Require the current ceiling g_k≤e⁻¹, the specified cell parameters, s≤h<k, and the integer N₀(s) cell-window equality.
- **55499–55503:** For the alternative version, require the two-sided logarithmic cell-parameter bounds.
- **55624–55625:** Graded-count (a) assumes the flow relations and ceiling through k.
- **55626–55627:** Graded-count (b) assumes the older-window cell-parameter hypotheses.
- **55628–55629:** Graded-count (c) assumes the integer N₀ relation for every older step.
- **55630–55642:** P1 assumes the exact identification, nesting, and core inclusions of non-cell older members.
- **55643:** P2 assumes the ten-cell interior distance for each older top prepared member.
- **55644–55645:** P3 assumes the ordering and nesting of intersecting older components.
- **55646–55647:** P4 assumes the current-label complement, Ω–Λ nesting, and inclusion in the current older region.
- **55648–55649:** P5 assumes that the containing level-s member is the retained component itself and is a closed cell union.
- **55651–55652:** Hypothesis (e) assumes the prepared-region inclusion in Λ and its eight-layer margin.
- **55683–55705:** P1–P5 and (e) remain hypotheses; cited construction statements are recorded only for orientation.
- **55787–55793:** A bound depending only on the running coupling is declared unavailable, and subsequent uses are restricted to the graded form.
- **55798–55814:** The graded-excess proposition requires the named setting, N>N₀, h<k, N≤R_k, cell parameters, coupling ceiling, and bounded increments.
- **55864–55865:** I assumes all graded-count hypotheses and conclusions.
- **55866–55868:** II assumes old-excess support and the zone inclusions into the cutoff-one region.
- **55869–55871:** III assumes termwise remainder and zone-majorant bounds.
- **55872–55882:** IV assumes small-function majorants, their sums, and absorption of the graded weight.
- **55883–55889:** V assumes the full remainder decomposition, stage-excess and stage-increment bounds, and current-support inclusion.
- **55890–55894:** VI assumes constant-weight absorption under C4 and its enlarged counterpart C4′.
- **55895–55897:** VII assumes the cutoff vanishing statement outside its exceptional boundary layer.
- **55898–55899:** VIII assumes the prepared-coupling decomposition and coefficient bound on Γ″_j.
- **55900–55910:** IX.1 assumes the original coefficient's two-stage absorption inequality.
- **55911–55912:** IX.2 assumes absorption of the N polynomial into R_k².
- **55913–55914:** IX.3 assumes absorption of the h−j polynomial into exponential decay.
- **55915–55917:** IX.4 assumes smallness of the R_k⁷ expression under the stated ν floor.
- **55918–55919:** IX.5 assumes smallness of the R_k⁸ expression under the shifted ν floor.
- **55920:** IX.6 assumes the ν floors do not depend on L.
- **55922–55925:** X assumes cutoff-weighted positivity and the companion identity with old excess.
- **55941–55950, 56020–56023:** C1′ imposes the enlarged remainder-majorant ceiling, with the chosen version of the cell parameter.
- **55960–55961, 56037–56043:** Companion absorption requires C4′ and the additional graded-majorant input.
- **55969–55973, 56097–56099:** The new R_k⁸ bound requires ν≥p₀+max(p₀,q)+8r₀+1.
- **56125–56146:** The domain theorem imposes d=4, L≥8, M above both stated floors, κ≥κ₀(d), β≤1/4, ℓ₀²≤L/3, q_*≥p₁+1, p₀≥5r, and the shifted ν floor, with fixed absolute constants.
- **56150–56154:** Assume the first Wilson-term theorem's estimates, support, cell count, volume, non-containment, and locality statements.
- **56155–56160:** Assume the second Wilson-term theorem with its low-zone old-excess bound explicitly excepted.
- **56161–56162:** Assume the preparatory-boundary theorem and all its standing hypotheses.
- **56163–56165:** Assume the graded-count lemma and graded-excess proposition.
- **56166–56171:** Assume the imported statements fixing m, m′, and Ξ.
- **56172–56173:** Assume the second-remainder bound from B-CMP122b (1.32), whose right member is σ̄.
- **56174:** Assume the cutoff-function statement from B-CMP122b.
- **56175–56176:** Assume the three further paper statements entering the Wilson proofs, not individually specified here.
- **56177:** Assume regularity of the stage terms.
- **56183–56191:** At the operation step require flow through k, 0<g_k≤γ_W, N₀<N≤R_k, the logarithmic regime, a component in the cited class, and prepared-member profiles at every preparatory stage.
- **56208:** General containment D⊂Λ is expressly not asserted; the text states general non-containment instead.
- **56307–56310:** The domain-theorem substitutions require both strengthened coupling ceilings and the shifted ν floor.
- **56321–56339:** γ_W is chosen from the listed thresholds; no numerical value is asserted.
- **56343–56353:** The two-sided-flow lemma assumes real data, the recurrence, constant signs, the interval baseline bound, and all per-step perturbation bounds.
- **56361–56368:** The finite one-loop law supplying the interval estimate has a proof incomplete at one step.
- **56369–56378:** The per-step application requires the unmarked and large-field bounds and the explicit ε₁ᴵ and γ ceilings; the unmarked lemma's proof is incomplete at one step.
- **56414–56417:** No per-step sign is asserted or used.
- **56420–56422:** Clause zero assumes H1–H6 and the stated initial coupling window.
- **56424:** Clause-zero (a) assumes B-CMP109 Theorem 3.
- **56425–56427:** Clause-zero (a′) assumes widened condition (1.12) on smaller cubes and its reproduction by the step.
- **56428–56430:** Clause-zero (b) assumes the one-loop and unmarked lemmas despite incomplete (*) proof steps.
- **56431:** Clause-zero (c) assumes the large-field-increment bound.
- **56432–56433:** Clause-zero (d) assumes localized-term independence from the small-field region.
- **56434:** Clause-zero (e) assumes free-current operator bounds.
- **56435:** Clause-zero (f) assumes representation and bounds of large-field terms.
- **56436:** Clause-zero (g) assumes the one-power hereditary class.
- **56437:** Clause-zero (h) assumes torus independence in non-wrapping domains.
- **56439–56441:** Assume the effective-density representation at all earlier reached scales while the prior inverse couplings exceed the threshold.
- **56463–56473:** The joint induction is assigned to the representation theorem's proof, and the incomplete (*) inputs are reiterated.
- **56532–56535:** Containment assumes H4, clause (0), and H3's terminal ceiling.
- **56543–56545, 56563–56565:** Bałaban's stability theorem requires all effective couplings in (0,γ], which containment conditionally verifies.
- **56570–56572:** The fixed-depth corollary assumes clause (0), a bare-coupling sequence decreasing to zero, and K_i≥s for each finite-depth assertion.
- **56636:** Exact terminal tuning g_K=g at prescribed K is not asserted.
- **56637–56638:** Realization of every K, monotonicity of K, and monotonicity of a tuned bare coupling are not asserted.
- **56639–56640:** Signs of individual flow differences or increments are not asserted.
- **56641–56644:** Full-sequence fixed-depth convergence is not asserted; only subsequential convergence is supplied.
- **56645:** Regularity of increments in the couplings is not asserted.
- **56649–56650:** Only the opening announcement of the proof explaining these exclusions is present here.

## For the stage question

This chunk contains no explicit assertion about admission or inclusion of **background fields**, no stated **analytic ball**, and no **minimiser** statement. The holomorphy assertion below concerns referenced spaces whose definitions are outside this chunk; it must not be expanded into an unstated claim about their complex-domain size or admitted backgrounds. “Admitted” at the opening refers to geometric configurations of retained regions, not admission of background fields. The term “drop-out” does not occur; the stopping and carrying rule is indexed below.

| Lines | Statement relevant to stages, domains, carrying, or prepared shells | Status here | Inputs / scope |
|---|---|---|---|
| 55363–55375 | Three alternatives specify lower members inside a retained region, and the third admits a step-h retained region that fails cell geometry. | proved conditionally | (c1)–(c3); component conditions (i), (ii); subsequent proof |
| 55389–55405 | The last N steps produce levels h+1 through k, while the older level-h operation is carried unchanged and lower Z″_j equal Z_j. | cited | B-CMP122a (1.2), (1.11) |
| 55395–55398 | If integrations stop in a component at n because new large field appears, the new B_k⁽ⁿ⁾ terms remain among all boundary terms. | cited | B-CMP122a mixed-history statement; this is the chunk's explicit stopping/carrying rule |
| 55407–55420 | Whole retained components keep their characteristic functions, attached factors, and T′ operation and become large-field regions of the operation's level. | proved conditionally | B-CMP122b p. 390; B-CMP122a (1.72); opening proof (a) |
| 55422–55427 | The actual post-R label description is not derived, so lower-stage members are treated under three alternatives. | named open | B-CMP122b; B-CMP119 (2.18) |
| 55429–55450 | The alternatives give different retained-region profile/coupling behavior and decide whether older prepared M-cube members remain in the label. | assumed | (c1)–(c3); cited coupling formula and profile definition |
| 55452–55455 | After a later step heals a region by absorbing its large-field factor into small-field format, no label member remains there and all readings agree. | definition | Definition of healed region and stated consequences |
| 55457–55474 | Cell geometry persists at every step under the first two readings but fails in an admitted retained step-h configuration under the third. | proved conditionally | (c1)–(c3); cited geometry; opening proof |
| 55488–55494, 55496–55503 | The older-stage short window is related to its cell parameter and bounded in terms of its age and the current parameter. | proved conditionally | Flow, ceiling, older-window hypotheses |
| 55614–55649 | Older prepared members, their core nesting, separation, interactions, and membership in the current label are specified in P1–P5. | assumed | Graded-count geometric hypotheses; these are not established from the current label here |
| 55651–55663 | The first prepared member is required to lie inside Λ with an outer margin, and j(x) indexes the current label's shell. | assumed | Hypothesis (e); shell index itself is a definition at 55655–55657 |
| 55670–55679, 55761–55783 | Older contributions lie inside the first prepared member with a five-cell inner separation and the eight-cell outer margin. | proved conditionally | P1–P5; (e); cited five-layer geometry |
| 55683–55705 | The correspondence of older-step geometry to the cited construction is explanatory, with later T-operations described as appending levels. | assumed | Explicitly retained geometric hypotheses; B-CMP122a/b and B-CMP119 |
| 55787–55793 | Counts and subsequent estimates are graded by shell depth, with Bałaban's comparison using prepared Ω″ shells. | sketched | Graded-count lemma; B-CMP122b |
| 55815–55820 | For j≤h the original and prepared shells restricted to Z coincide and are called zone_j. | definition | B-CMP122a §1 |
| 55839–55853 | The excess and the family/companion coupling increments are indexed by current preparatory stage n. | definition | Coupling-excess definition; hypothesis V |
| 55866–55868, 55883–55899 | Old excess lies on low-index prepared zones, stage differences split into current and old terms, and cutoffs and Γ″ coefficients obey the stated support rules. | assumed | II, V, VII, VIII |
| 55951–55961, 56025–56043 | Family/companion stage-increment differences obey the graded-plus-constant supported bound and corresponding absorption. | proved conditionally | II, IV–VI; graded excess |
| 55962–55964, 56045–56058 | The old excess has zero product with ζ because it lies deeper inside the first prepared member than the exceptional cutoff layer. | proved conditionally | Graded-count support; II; VII |
| 55974–55975, 56114–56120 | At stage n, the excess on each low-index zone obeys the stated graded bound. | proved conditionally | V; graded old-excess estimate |
| 56130–56136 | The theorem imports the layered analyticity schedule and stage-theorem parameter restrictions. | assumed | 4.4:def-post-step-space; 4.18:thm-preparatory-boundary |
| 56161–56162, 56177 | Boundary-term stage bounds, their standing hypotheses, and stage-term regularity are inputs. | assumed | Preparatory-boundary theorem; imported regularity statement |
| 56189–56195 | The construction uses prepared-member profiles at every preparatory stage and defines the spatial excess domains D and N. | definition | B-CMP122a component class; prepared family; these are spatial support sets, not analytic balls |
| 56198–56208 | D contains the excess support, lies in the eight-layer interior, and is generally not contained in Λ. | proved conditionally | Assumed Wilson support, volume, and non-containment inputs |
| 56209–56247 | Excess-sensitive estimates replace Λ by D while the listed integration domains remain unchanged. | proved conditionally | Wilson inputs; graded substitutions; no background-admission conclusion is stated |
| 56228–56231 | Every prepared Ω″ shell has the displayed graded coupling-excess bound. | proved conditionally | Action-domain theorem inputs; graded-excess proposition |
| 56260–56269 | At every preparatory stage n+1 the family term has representation (1.63), is holomorphic on spaces (1.64)–(1.69), and obeys (1.70) with C₀=c_G+1 and the referenced decay rates. | proved conditionally | B-CMP122a; reading of spaces in 4.18:thm-preparatory-boundary; 4.18:rem-decay-rates; this is the explicit complex-analytic statement |
| 56270–56273 | The family's added weight-difference support is a quarter-cell collar inside R_n, and its share of C₀ equals the companion's. | proved conditionally | B-CMP122a (1.62); weight-difference lemma; preparatory-boundary theorem |
| 56274–56290 | Modified supports lie in the eight-layer interior and locality set X_a, using Wilson locality, weight-difference support, and the old-member count. | proved conditionally | Wilson theorems; 4.18:lem-weight-difference (b); graded-count bound |
| 56315–56319 | The proof explicitly assigns the stage holomorphy and bounds to the assumed preparatory-boundary theorem and its support lemma. | proved conditionally | 4.18:thm-preparatory-boundary; 4.18:lem-weight-difference |
| 56323–56330 | The common small-coupling ceiling includes the stage theorem's γ₀. | definition | Wilson ceilings; graded strengthening; preparatory-boundary stage theorem |
| 56425–56427 | The widened small-cube condition is assumed to be reproduced by a renormalization step. | assumed | B-CMP109 (1.12); this is not a background-domain admission statement |
| 56439–56441, 56463–56484 | Representation at already reached levels is an induction input jointly with coupling control. | assumed | 4.20:thm-representation; clause-zero inputs; no analytic-ball inclusion is stated |
| 56513–56523 | H5 is said to make the declared lattice pair admissible for every step through K, and those steps reproduce the abstract couplings. | proved conditionally | H5; torus independence; flow bounds; admissibility concerns lattice size, not background fields |
