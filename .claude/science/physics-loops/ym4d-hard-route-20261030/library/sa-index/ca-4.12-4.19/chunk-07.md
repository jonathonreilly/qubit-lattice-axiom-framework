# Chunk 07: lines 50284-51582
Sections: Continuation of item 4.15 (no section or subsection heading appears in this chunk); internal titled divisions: The decomposition (50327), Cubes attached to bonds (50336), Stage sets (50342), The stages (50354), Output (50375), The creation set (50385), Terms and labels (50461), The level at which R acts (50479), Histories (50528), What the proof uses (51426), Non-circularity (51460), The regime clause in full (51500), The attachment of the level (51519), Levels k ≤ Ř_k (51525), Bałaban's own preparatory large fields (51528).

The source starts inside `4.15:def-small-field-complement`, with the concluding display of `4.15:eq-small-field-complement-c` (its opening label is outside this chunk), and ends at the opening of an unnumbered display in the proof of `4.15:rem-level-inequalities`(b). Labels below retain the source identifiers; mathematical notation is abbreviated in prose. Status describes the presentation here, not an independent assessment of correctness. A statement supplied with explicit substantive inputs is marked `proved conditionally` when its argument is complete here; elementary lemmas with their ordinary quantified assumptions are marked `proved in detail`. External results assumed for use here are distinguished from conclusions actually derived here.

| Lines | Name / tag | Kind | What it states (one plain sentence, your words) | Status here | Reads (inputs it uses, by tag or name) | Key phrase |
|---|---|---|---|---|---|---|
| 50284-50299 | `4.15:eq-small-field-complement-c` (continued); complement hypothesis | hypothesis | The complement is a finite union of nonnegative enlargements of coarse regions inside P′ ∪ Q′ and of the hull of the incoming Y, which is empty at the first step. | assumed | `4.15:eq-small-field-complement-a`, `-b`, `-3`; coarse partition; Y | "enters as a hypothesis" |
| 50301-50309 | Cube-wise complement and first-step convention | remark | The complement can be expressed by enlarged individual cubes and the old region, but the narrower first-step choice P′ = P′₁ can fail. | proved conditionally | `4.15:eq-small-field-complement-1` (second identity), `-c`, `-b`; P′ = P′₀ ∪ P′₁ | "Under the narrower choice" |
| 50311-50314 | Provenance of decomposition sets | definition | The decomposition sets and small-field domains are the ones specified in Bałaban's formulas. | definition | B-CMP119 (3.2)–(3.5), p. 265; (1.2), (1.4), (1.8), (1.10), pp. 246–248 | "are those of" |
| 50316-50405 | `4.15:def-creation-set`: The large-field region of a step and its creation set | definition | This definition specifies stage recursion, output region, and the creation set for a labelled step. | definition | `4.15:def-small-field-complement`; `4.15:def-enlargement-hull`; large-field recursion definition | "The creation set" |
| 50327-50334 | Replacement decomposition and labels ℓ | construction | The recursion's decomposition replaces Bałaban's decomposition and labels outcomes by R, I, and low-test cubes. | definition | Large-field recursion definition; B-CMP119 (3.16), (1.18); Ω_t; test-cube and coarse-cube sizes | "is replaced by the decomposition" |
| 50336-50340 | Bond attachment K(J) | definition | K(J) consists of the coarse cubes in Ω_t with one layer removed that hold endpoints of bonds in J. | definition | K; coarse partition; bonds of the step | "holding an end-point" |
| 50340 | Union preservation of K | identity | Attaching cubes to a union of bond sets gives the union of their attached cubes. | proved in detail | Definition of K(J) | "Thus" |
| 50342-50345 | `4.15:eq-creation-set-1`: Z[R] | definition | Z[R] is the union of the twice-enlarged small-field complement and the enlargement of the cube set R. | definition | Ω_t; enlargement | "put" |
| 50346-50352 | Comparison with Bałaban's Λ | remark | At R = R′, Z[R] complements Bałaban's displayed region, which contains the final Λ_t defined below. | proved in detail | B-CMP119 (3.20); `4.15:eq-creation-set-3`; stage monotonicity proved at 50409–50416 | "is contained in it" |
| 50354-50363 | Stage initialization, bond test, and untested rim cubes | construction | Each stage starts from the boxed initial region or the previous output and tests bonds and previously untested coarse rim cubes. | definition | Large-field recursion definition; M; K; R′; Λⁿ = (Z⁽ⁿ⁾)ᶜ | "The two tests are those of the definition" |
| 50364-50368 | `4.15:eq-creation-set-2`: stage update | definition | The next cube set accumulates failed tests and the next region boxes the union of the old region with Z of the updated cubes. | definition | R_n; K(I_n); low-test cubes; M; `4.15:eq-creation-set-1` | "Then" |
| 50369-50373 | Stopping index n_* and termination | construction | The run stops at the first pair of empty test outputs, and termination follows from strict growth in a finite cube set established in the recursion definition. | proved conditionally | Strict growth proved where the large-field recursion is defined; finite torus cube set | "grow strictly, as shown" |
| 50375-50377 | Aggregated I and low-test cubes | definition | The output label collects bond and low-cube test outcomes before the stopping stage. | definition | I_n; low-test cubes; n_* | "The outcome has" |
| 50378-50383 | `4.15:eq-creation-set-3`: Λ_t and Z_t | definition | The final stage region is the scale-t large-field region and its complement is Λ_t. | definition | Z⁽ⁿ_*⁾ | "large-field region of scale" |
| 50385-50388 | `4.15:eq-creation-set-a`: creation set Ŵ_t | definition | The creation set unites P′, Q′, R′, bond-attached cubes, and low-test cubes. | definition | P′; Q′; R′; K(I); low-test cubes | "creation set" |
| 50389-50391 | New large-field region created in a component | definition | A component of Λ_tᶜ has a creation at step t when it meets Ŵ_t. | definition | Λ_t; Ŵ_t | "is said to have" |
| 50393-50404 | `4.15:eq-creation-set-b` and closing assertions | identity | Stage cube sets form an increasing accumulated union, all stage regions are coarse regions, and their final union with P′ and Q′ equals Ŵ_t. | proved in detail | `4.15:eq-creation-set-2`, `-a`; K union preservation; M; proof 50407–50458 | "With these definitions" |
| 50407-50458 | Proof of creation-set-b and closing assertions | proof | Enlargement and boxing preserve coarse regions, while unwinding the update proves the accumulated-union formula and creation-set property. | proved in detail | `4.15:def-enlargement-hull`; `4.15:eq-small-field-complement-c`; creation-set-1, -2, -a | "Proof of" |
| 50409-50416 | Proof: monotonicity of stage sets | proof | Extensivity of the stabilized boxing map makes every next stage contain its predecessor. | proved in detail | `4.15:def-enlargement-hull`; `4.15:eq-creation-set-2` | "gives" |
| 50418-50428 | Proof: stages are coarse regions | proof | The coarse-region property follows inductively because enlargement, union, and boxing preserve it. | proved in detail | `4.15:eq-creation-set-1`, `-2`; `4.15:eq-small-field-complement-c`; `4.15:def-enlargement-hull` | "by induction" |
| 50430-50449 | Proof: chain of cube sets | proof | Iterating the cube update and distributing K over the finite union gives both equalities in creation-set-b. | proved in detail | `4.15:eq-creation-set-2`, `-a`; K union preservation; output definitions | "Unwinding the same relation" |
| 50451-50457 | Proof: creation set is a coarse region | proof | Every constituent of Ŵ_t is a union or set of coarse cubes. | proved in detail | `4.15:eq-creation-set-b`; hulls P′, Q′, R′; K | "A union" |
| 50460-50564 | `4.15:def-histories`: Histories of a term and the components acted upon | definition | Terms, eligible components, histories, post-action regions, and pure-T histories are specified. | definition | `1.5:def-densities`; creation-set definition; no-creation definition; B-CMP122a/b | "Histories" |
| 50461-50477 | Terms, labels, and step succession | definition | Each finite-sum term carries its small-field history, T produces labelled descendants, and R then acts on eligible components. | definition | `1.5:def-densities`; `4.15:def-creation-set`; `4.15:eq-creation-set-a` | "Each term carries a label" |
| 50479-50492 | Acting-level conditions (i)–(iii) | requirement | R acts at the first level satisfying a size bound, the adopted no-creation waiting condition, and absence of still-waiting nested components. | definition | `4.15:def-no-creation` condition (ii); waiting depth N_j | "the first" |
| 50484 | Acting-level condition (i) | requirement | An acted-on component must fit in a cube of side 100M Ř_j. | definition | Component C; scale j | "is contained in a cube" |
| 50485-50489 | Acting-level condition (ii) | requirement | A component must have no creations more recent than its waiting window, with an optional additional j ≥ N_j clause under one formulation. | definition | `4.15:def-no-creation`; N_j; creation levels | "no large-field region created" |
| 50490-50491 | Acting-level condition (iii) | requirement | No strictly nested component may still await R. | definition | Nested components; prior R actions | "no component nested strictly inside" |
| 50493-50497 | Level versus density index | remark | Attaching an action to the input density's index gives j − 1 instead of its scale level j. | proved in detail | Tρ_{j−1}; Z_j | "differs by one" |
| 50499-50507 | Eligible class A_j, union 𝒵, and R outcomes | definition | A_j consists exactly of components first meeting the acting conditions, and R acts on their union to produce terms of ρ_j. | definition | Conditions (i)–(iii); B-CMP122a pp. 176–177; B-CMP122a/b | "Membership" |
| 50509-50517 | `4.15:eq-histories-a` | identity | Membership in A_j implies all three acting conditions, including the adopted no-creation clause. | proved in detail | Acting-level definition; proof 50570–50575 | "they are proved below" |
| 50517-50526 | `4.15:eq-histories-b` | identity | If A_j is empty, the term and its label remain unchanged and its large-field region is the recursion's final stage region. | proved conditionally | Componentwise action of R in `1.5:def-densities`, B-CMP122a pp. 176–177; `4.15:def-creation-set`; proof 50577–50597 | "no operation is" |
| 50528-50532 | History of a term | definition | A history is a chain from the unique initial term to the given term, selecting a step and action outcome at each level. | definition | ρ₀; T; R; decomposition outcomes | "is a sequence" |
| 50534-50548 | History data and incoming post-action region | definition | A history records pre-action terms, regions, creation sets, eligible classes, and post-action regions, with the latter read as Y at the next step. | definition | `4.15:def-creation-set`; B-CMP119 p. 265; Z₀^post = ∅ | "it is the region" |
| 50550-50553 | How bond and cube labels enter waiting conditions | remark | The bond and low-cube outcomes affect eligibility through the history's creation sets and waiting rule. | definition | Ŵ_t; conditions (i)–(iii); outcome label | "through the creation set" |
| 50554-50557 | `4.15:eq-histories-c` | identity | An empty eligible class leaves the history's term and large-field region unchanged at that level. | proved conditionally | `4.15:eq-histories-b`; history data; proof 50609–50616 | "By" |
| 50559-50562 | `4.15:eq-histories-1`: pure-T below k | definition | A history is pure-T below k when every eligible class at levels 1 through k − 1 is empty. | definition | A_j | "if" |
| 50563 | Existence of histories | proposition | Every term has at least one history. | proved in detail | Finite-sum recursion `1.5:def-densities`; proof 50599–50607 | "this too is proved below" |
| 50566-50616 | Proof of history assertions and existence | proof | Eligibility, componentwise action, and backwards ancestry establish histories-a through histories-c and existence. | proved conditionally | Acting-level definition; `1.5:def-densities`; B-CMP122a pp. 176–177; creation-set definition | "We prove" |
| 50570-50575 | Proof of histories-a | proof | First satisfaction of the acting conditions implies satisfaction at the acting level. | proved in detail | A_j definition; `4.15:def-no-creation` | "in particular they hold" |
| 50577-50597 | Proof of histories-b | proof | R has no component to change when its acting union is empty, so the sole output is the original term with the final recursion region. | proved conditionally | `1.5:def-densities`; B-CMP122a pp. 176–177; `4.15:def-creation-set` | "Since" |
| 50580-50585 | Unchanged waiting components | remark | R changes nothing outside the union of components acted upon, as specified by Bałaban. | cited | B-CMP122a pp. 176–177 | "Outside that union nothing is" |
| 50599-50607 | Proof: existence of histories | proof | Choosing a parent term successively down to the unique initial term constructs a history, also for a term before the last R action. | proved in detail | ρ_k = RTρ_{k−1}; unique term of ρ₀ | "we descend level by level" |
| 50609-50616 | Proof of histories-c | proof | Applying histories-b to the history's selected term identifies its pre-action and post-action regions. | proved conditionally | `4.15:eq-histories-b`; definitions of Z_j and Z_j^post | "Apply" |
| 50618-50624 | `4.15:lem-cube-sizes-monotone`: The cube sizes do not increase | lemma | For integer L ≥ 2, positive r, and real x_j > 1, the cube sizes exist as nonnegative integer powers of L and decrease with j. | proved in detail | `4.15:not-cube-sizes`; stated L, r, x_j hypotheses | "Then" |
| 50626-50664 | Proof of cube-size monotonicity | proof | A least admissible exponent exists by an elementary growth bound and decreases as the running minimum of x decreases. | proved in detail | `4.15:not-cube-sizes`; Bernoulli's inequality; monotonic logarithm and positive power | "it follows that" |
| 50633-50642 | Admissible exponent set B_j and least exponent b_j | construction | B_j collects the nonnegative exponents meeting the logarithmic threshold and its least element realizes Ř_j. | proved in detail | L ≥ 2; r > 0; x̌_j > 1; `4.15:not-cube-sizes` | "it has a least" |
| 50666-50678 | Hypotheses within Theorem 0 and stronger size comparison | remark | Theorem 0 supplies the monotonicity hypotheses, whereas the stronger scale comparison is assigned to part (a) of the separate cube-size lemma. | proved conditionally | `4.15:eq-cube-sizes-a`; `4.1:thm-clause-zero`; (H2); (H5); cube-size lemma (a) | "rests on part" |
| 50680-50697 | `4.15:lem-component-properties`: Elementary properties of components | lemma | Components partition a finite region into non-touching connected pieces and obey containment, connected-union, and subcollection rules. | proved in detail | `4.15:def-regions-components` | "Elementary properties of components" |
| 50683-50684 | Component properties (a) | lemma | Components are finitely many nonempty connected non-touching regions with disjoint point sets and union X. | proved in detail | `4.15:def-regions-components`; proof 50703–50720 | "Their union is" |
| 50685 | Component properties (b) | lemma | Every nonempty connected subregion belongs to exactly one component. | proved in detail | Component properties (a); proof 50722–50726 | "exactly one component" |
| 50686-50687 | Component properties (c) | lemma | Under inclusion each old component lies in exactly one new component. | proved in detail | Component properties (a), (b); proof 50728–50730 | "exactly one component" |
| 50688-50689 | Component properties (d) | lemma | Joining finitely many connected regions touching a connected anchor preserves connectedness. | proved in detail | Chains and touching; proof 50732–50743 | "is connected" |
| 50690-50692 | Component properties (e) | lemma | A component of a finite union of nonempty connected regions is the union of the constituent regions it contains. | proved in detail | Component properties (a), (b); proof 50745–50753 | "contains at least one" |
| 50693-50695 | Component properties (f) | lemma | A nonempty selection of components remains precisely the component collection of its union. | proved in detail | Component properties (a), (b), (e); proof 50755–50775 | "exactly the members" |
| 50699-50776 | Proof of elementary component properties | proof | Equivalence classes of touching chains give the partition properties and the remaining claims follow by tracing chains. | proved in detail | `4.15:def-regions-components` | "Throughout we use the notions" |
| 50703-50720 | Proof of component properties (a) | proof | Equivalence classes partition the finite cube set, cannot touch across classes, and are internally connected. | proved in detail | Chain equivalence; `4.15:def-regions-components` | "Hence distinct components do" |
| 50722-50726 | Proof of component properties (b) | proof | Chains inside A place all its cubes in one class, and nonemptiness gives uniqueness. | proved in detail | Component properties (a); connected A | "This component is unique" |
| 50728-50730 | Proof of component properties (c) | proof | A component of X is a connected subregion of X′, so part (b) applies. | proved in detail | Component properties (a), (b) | "Part (b)" |
| 50732-50743 | Proof of component properties (d) | proof | Paths from each attached region to the anchor concatenate into paths across the union. | proved in detail | Connected A and A_i; touching | "Concatenating such a chain" |
| 50745-50753 | Proof of component properties (e) | proof | Each cube in a component belongs to a constituent connected region lying wholly in that component. | proved in detail | Component properties (a), (b) | "The reverse inclusion holds" |
| 50755-50775 | Proof of component properties (f) | proof | A chain cannot cross between distinct selected non-touching components, so the union has exactly those components. | proved in detail | Component properties (a), (b), (e) | "Conversely" |
| 50778-50797 | `4.15:lem-enlargement-connected`: Enlargement and hull preserve connectedness | lemma | Enlargement distributes over finite unions, iterates additively, and enlargement and coarse hull preserve connectedness and containment. | proved in detail | `4.15:def-enlargement-hull`; component properties; subdivision independence | "Enlargement and hull preserve connectedness" |
| 50783-50789 | Enlargement properties (a) | identity | Enlargement is extensive and distributes over unions, iterated layer counts add, and an enlarged region is the union of enlarged cubes. | proved in detail | Enlargement definition; proof 50800–50822 | "For" |
| 50790-50791 | Enlargement properties (b) | lemma | Every iterated enlargement of a connected coarse region or single coarse cube is connected. | proved in detail | Component properties (d); subdivision independence; proof 50824–50835 | "In particular" |
| 50792-50795 | Hull properties (c) | lemma | A coarse hull contains its region, distributes over its components, and gives connected enlarged hulls of connected components. | proved in detail | Coarse hull definition; component properties; proof 50837–50856 | "containing" |
| 50799-50857 | Proof of enlargement and hull properties | proof | Touching and finite unions prove the algebraic rules, and attached-cube chain arguments prove connectedness. | proved in detail | `4.15:def-enlargement-hull`; `4.15:lem-component-properties`; `4.15:lem-subdivision-independence` | "We now induct" |
| 50800-50822 | Proof of enlargement (a) | proof | Self-touching, distribution of cube membership, and induction prove the four enlargement identities. | proved in detail | Recursive enlargement definition | "The third relation unwinds the recursive definition" |
| 50824-50835 | Proof of enlargement (b) | proof | Each added cube is connected and touches the old connected region, and induction handles multiple layers. | proved in detail | `4.15:lem-subdivision-independence`; component properties (d) | "We now induct" |
| 50837-50856 | Proof of hull (c) | proof | Partition refinement gives containment, component decomposition gives the hull union, and touching cubes give connectedness. | proved in detail | Finest partition refinement; component properties (a), (d); subdivision independence; enlargement (a), (b) | "Hence" |
| 50859-50892 | `4.15:lem-replacement-maps`: Boxing and components under replacement maps | lemma | Coordinate boxing is connected and replacement maps, including stabilized boxing, preserve a component ancestor in each output component. | proved in detail | `4.15:def-enlargement-hull`; torus coarse partition; component properties; subdivision independence | "The same holds" |
| 50860-50871 | Torus cube indexing c_n and N_t | definition | Coarse cubes are indexed by residue vectors modulo the integer N_t = p/W. | definition | Torus covering π; side W = W_t; `4.15:def-enlargement-hull` | "put" |
| 50873-50874 | Replacement maps (a): touching criterion | lemma | Two indexed cubes touch exactly when each coordinate residue differs by zero or one in either direction. | proved in detail | Torus cube indexing; proof 50895–50907 | "if and only if" |
| 50875-50877 | Linked residue subset | definition | A nonempty residue subset is linked if its elements can be joined by finite steps of size zero or one in either direction. | definition | Z/N_t Z | "Call a non-empty subset" |
| 50877-50881 | Replacement maps (b); `4.15:eq-replacement-maps-1` | identity | Every linked residue set is a cyclic interval of length at most N_t. | proved in detail | Linked-set definition; proof 50909–50921 | "A linked set is a cyclic interval" |
| 50882-50884 | Replacement maps (c): connected box | lemma | Every coordinate range of a connected coarse region is linked and its box is a connected coarse superset. | proved in detail | Replacement maps (a), (b); subdivision independence; proof 50923–50940 | "is a connected" |
| 50885-50887 | Replacement maps (d): component ancestry | lemma | Every component after a replacement map or finite composite contains a component of the original region. | proved in detail | Replacement-map definition; component properties; proof 50942–50963 | "every component" |
| 50888-50890 | Replacement maps (e): stabilized boxing | lemma | M₁ is a replacement map and M is an extensive idempotent finite iterate retaining component ancestry. | proved in detail | q₀ definition; replacement maps (c), (d); proof 50965–50980 | "Hence" |
| 50894-50981 | Proof of boxing and replacement-map properties | proof | Coordinate interval geometry proves connected boxing, and finite connected unions establish ancestry and stabilization. | proved in detail | `4.15:def-enlargement-hull`; component properties; subdivision independence | "This proves the claim" |
| 50895-50907 | Proof of replacement maps (a) | proof | Intersections of lifted coordinate intervals give the residue touching criterion. | proved in detail | p = N_t W; closed unit-grid intervals | "Hence" |
| 50909-50921 | Proof of replacement maps (b) | proof | Removing a missing residue unwraps a proper linked set into an ordinary integer interval, while the full set is immediate. | proved in detail | Linked-set definition | "Returning to residues" |
| 50923-50940 | Proof of replacement maps (c) | proof | Projected chains make coordinate ranges linked and coordinatewise paths connect all cubes of the box. | proved in detail | Replacement maps (a), (b); `4.15:lem-subdivision-independence` | "It is connected" |
| 50942-50963 | Proof of replacement maps (d) | proof | Each added connected region contains an old component and induction preserves this ancestry through composites. | proved in detail | Replacement-map definition; component properties (a), (c), (e) | "For a composite, induct" |
| 50965-50980 | Proof of replacement maps (e) | proof | Boxing small components is a replacement operation and stopping at q₀ yields an idempotent extensive map. | proved in detail | Replacement maps (c), (d); component properties (a); `4.15:def-enlargement-hull` | "this shows" |
| 50983-50986 | Scope of the boxing proof | remark | The proof needs no quantitative iteration, component-count, region-size, or cube-fit estimate. | proved in detail | Proof 50894–50981; coupling-flow bounds and (H5) mentioned only as unused | "is not invoked" |
| 50988-51005 | `4.15:prop-one-step-components`: Components of the large-field region after one step | proposition | Under the complement description, the output contains Y and Ŵ_t, every output component has an old component or creation cube, and old components have unique output containers. | proved conditionally | `4.15:def-creation-set`; `4.15:eq-small-field-complement-c`, concretely -a or -b; component, enlargement, and replacement-map lemmas | "Assume, as hypothesis" |
| 50994-50998 | One-step complement input | hypothesis | The step's small-field complement is assumed to have the adopted enlarged-union form, concretely the stated first-step or later-step formula. | assumed | `4.15:def-small-field-complement`; `4.15:eq-small-field-complement-c`, -a, -b | "Assume, as hypothesis" |
| 51000 | One-step components (a) | proposition | Both the incoming region Y and the creation set Ŵ_t lie in the output large-field region. | proved conditionally | Complement input; creation-set identities; enlargement and replacement-map lemmas; proof 51080–51114 | "Then" |
| 51001-51002 | One-step components (b) | proposition | Every output component contains an old component or a whole coarse creation cube. | proved conditionally | Complement input; component, enlargement, replacement-map lemmas; proof 51008–51078 | "contains a component" |
| 51003 | One-step components (c) | proposition | Every old component lies in exactly one output component. | proved conditionally | One-step components (a); component properties (c); proof 51116–51117 | "exactly one component" |
| 51007-51118 | Proof of one-step components | proof | Decomposition into connected pieces and induction through boxing establish component ancestry, while explicit inclusion chains prove containment. | proved conditionally | Complement input; creation-set-1, -2, -b; component, enlargement, replacement-map lemmas | "By the" |
| 51014-51035 | `4.15:eq-one-step-components-1` | identity | Z[R] decomposes into enlarged source cubes, enlarged hulls of old components, and enlarged new cubes. | proved conditionally | `4.15:eq-small-field-complement-c`; enlargement-connected (a), (c); creation-set-1 | "The second equality uses the distributivity" |
| 51037-51048 | Pieces of Z[R] | construction | The displayed constituents form a finite family of nonempty connected coarse regions each containing an old component or source cube. | proved conditionally | one-step-components-1; component properties (a); enlargement-connected (a)–(c) | "We call the sets" |
| 51050-51052 | Stage assertion (C_n) | definition | C_n asserts that each component of stage n contains an old component or a cube from P′ ∪ Q′ ∪ R_n. | definition | Y; Z⁽ⁿ⁾; R_n | "let" |
| 51054-51078 | Proof of (C_n) and one-step (b) | proof | The piece decomposition proves the base case and inheritance through each union and boxing proves the stage induction. | proved conditionally | Complement input; pieces; component properties (a), (e); replacement maps (e); creation-set-b | "This is" |
| 51080-51114 | Proof of one-step (a) | proof | Hull containment and extensivity carry Y, the concrete complement's P′ and Q′, and the final cube set into the output. | proved conditionally | Complement formulas -a, -b, -c; enlargement-connected (a), (c); replacement maps (e); creation-set-b | "Combining the two chains" |
| 51116-51117 | Proof of one-step (c) | proof | The unique-containing-component lemma applies to the already proved inclusion of Y. | proved conditionally | One-step (a); component properties (c) | "Apply" |
| 51120-51127 | Strength and input scope of one-step (b) | remark | The output component contains a whole creation cube rather than merely meeting the creation set, without using tests, thresholds, or fields. | proved conditionally | `4.15:prop-one-step-components`(b); complement-c; recursion shape | "The proof uses nothing about the tests" |
| 51129-51141 | `4.15:prop-pure-histories`: Creation cubes along histories without large-field actions | proposition | Along a history without earlier R actions, every component at every level through k contains a creation cube from some level at or before it. | proved conditionally | Complement-c; `4.15:def-histories`; A_j = ∅ for j < k; one-step components (b); histories-c | "Assume the reading" |
| 51131-51137 | Pure-history inputs | hypothesis | The enlarged-union complement description and absence of R actions below k are assumed. | assumed | `4.15:eq-small-field-complement-c`; `4.15:def-histories`; A_j | "Assume" |
| 51143-51176 | Proof of creation cubes along pure histories | proof | Induction starts with empty Y and carries old creation cubes forward whenever an output component does not contain a new cube. | proved conditionally | Complement-c; pure history; one-step components (b); histories-c; Z₀^post = ∅ | "this completes the induction" |
| 51178-51192 | `4.15:lem-waiting-rule`: The waiting rule | lemma | An action on a component containing a creation cube from level s must wait at least N_k levels after s under either no-creation convention. | proved conditionally | `4.15:def-histories`; `4.15:def-no-creation`; no-creation-a or -b; whole creation cube at s | "under the no-creation condition" |
| 51181-51185 | Waiting-rule input | hypothesis | The acted-on component is supposed to contain a whole cube of the history's creation set at a level s between 1 and k. | assumed | Ŵ_s; fixed history; no-creation-a or -b | "Suppose that" |
| 51186-51190 | `4.15:eq-waiting-rule-a` | estimate | The action satisfies k − s ≥ N_k and therefore k ≥ s + N_k ≥ 1 + N_k > N_k. | proved conditionally | Whole creation cube at s ≥ 1; histories-a; no-creation-a or -b | "hence" |
| 51194-51235 | Proof of waiting rule | proof | The latest creation in the component lies outside the forbidden recent window under either formulation, giving the waiting inequalities. | proved conditionally | histories-a; no-creation-a or -b; whole cube at s | "In both cases, therefore" |
| 51195-51202 | Creation-level set T_C and latest level t_* | construction | T_C records creation levels inside the component and its maximum exists because containing a whole cube places s in the set under every stated reading of inside. | proved conditionally | Whole creation cube w; meanings from meeting to containing a cube | "Hence" |
| 51210-51212 | Proof for no-creation-a | proof | Exclusion of creation levels strictly above k − N_k forces t_* ≤ k − N_k. | proved conditionally | no-creation-a; t_* ∈ T_C | "Therefore" |
| 51214-51225 | Proof for no-creation-b | proof | The truncated integer waiting interval and t_* ≥ 1 again imply t_* ≤ k − N_k. | proved conditionally | no-creation-b; t_* ∈ T_C; integer levels | "The displayed strict inequality between integers" |
| 51237-51240 | Comparison of no-creation formulations | remark | The two conventions differ only for components with no creation, a case excluded along pure-T histories by the preceding proposition. | proved conditionally | no-creation-a, -b; `4.15:prop-pure-histories` and its complement assumption | "there is no" |
| 51242-51278 | `4.15:lem-action-level`: Large-field actions occur only above the cube size | lemma | Under the stated flow, complement, and acting-level inputs, every action at level k satisfies k ≥ 1 + N_k and hence k > Ř_k. | proved conditionally | Inputs (a), (b), acting-level rule; (H2), (H5); pure histories; waiting rule; cube-size monotonicity | "Assume the following two statements" |
| 51245-51250 | Action-level hypothesis (a) | hypothesis | Clause (0) supplies x_j = g_j⁻² > g⁻² ≥ γ_H⁻² > 1, used only through the level under consideration. | assumed | `4.1:thm-clause-zero`; `4.15:eq-cube-sizes-a` | "It gives" |
| 51251-51253 | Action-level hypothesis (b) | hypothesis | Every step is assumed to have the prescribed enlarged-union small-field complement. | assumed | `4.15:eq-small-field-complement-c`; `4.15:def-small-field-complement` | "The description" |
| 51255-51260 | Action-level rule input | hypothesis | R may act only at the defined levels, using either of the two no-creation conventions. | assumed | `4.15:def-histories` (i)–(iii); `4.15:def-no-creation`; no-creation-a or -b | "only at the level prescribed" |
| 51265-51269 | `4.15:eq-action-level-a` and equivalent exclusion | estimate | Every acted-on component has k ≥ 1 + N_k, so no term has an action at a level k ≤ Ř_k. | proved conditionally | Action-level (a), (b), acting rule; N_k = Ř_k; proof 51280–51362 | "Equivalently" |
| 51271-51277 | Action-level quantifier scope | remark | The bound uses Theorem 0's order of constants and holds uniformly for all its admissible data without extra parameter restrictions. | proved conditionally | Theorem 0 quantifiers; action-level inputs | "No condition" |
| 51280-51362 | Proof of action-level bound | proof | The first action sees an old creation cube and must wait, and monotonic cube sizes transfer that lower bound to every later acting level. | proved conditionally | History existence; histories-b, -c; pure histories; waiting rule; (H2), (H5); action-level (a), (b); cube-size monotonicity | "In both cases" |
| 51287-51290 | `4.15:eq-action-level-1`: first acting level k₁ | definition | k₁ is the least level in the fixed history whose eligible class is nonempty. | definition | Fixed history; A_k nonempty | "Put" |
| 51292-51314 | First-action reduction | proof | All earlier stages are unchanged by R, allowing the pure-history proposition to supply a creation cube in the first acted-on component. | proved conditionally | histories-b, -c; complement-c; pure histories | "which is" |
| 51316-51329 | First-action waiting bound; `4.15:eq-action-level-2` | estimate | Applying the waiting rule at k₁ gives k₁ ≥ 1 + N_k₁ = 1 + Ř_k₁. | proved conditionally | Waiting rule; creation cube at s ≥ 1; N_k₁ = Ř_k₁; either no-creation formulation | "this yields" |
| 51334-51356 | Transfer to later acting levels | proof | Monotonicity of Ř and integrality give the claimed lower bound, with k ≥ 2 + Ř_k when k > k₁. | proved conditionally | `4.15:lem-cube-sizes-monotone`; (H2), (H5); x_j > 1; action-level-2; `4.15:not-cube-sizes` | "Combining this" |
| 51337-51342 | Checked monotonicity inputs | hypothesis | The proof takes integer L ≥ 2 from H2, positive r from H5, and real positive inverse couplings with x_j > 1 from hypothesis (a). | assumed | `2.2:not-hypotheses` (H2), (H5); action-level (a); positive g_j | "This is contained in" |
| 51358-51361 | Proof of equivalent exclusion | proof | Any action at k ≤ Ř_k would contradict the established action-level inequality. | proved conditionally | action-level-a | "a contradiction" |
| 51364-51391 | `4.15:cor-first-action`: No action at or below the cube size; the first action | corollary | There are no actions below the cube-size threshold, first actions inherit creation cubes from pure-T histories, and their preceding index h is positive. | proved conditionally | Clause (0); complement description; acting-level rule; action-level lemma; pure histories | "Assume the following" |
| 51365-51374 | First-action corollary inputs | hypothesis | The corollary assumes the clause-(0) cube-size input, the complement description, and the prescribed acting levels with either no-creation convention. | assumed | `4.1:thm-clause-zero`; cube-sizes-a; pure-histories hypothesis; histories definition; no-creation-a or -b | "Assume the following" |
| 51375-51376 | Pure-T terminology restated | definition | A history is pure-T below k when every earlier eligible class is empty. | definition | A_j; histories-1 | "Call a history" |
| 51378-51380 | First-action corollary (a) | corollary | For k ≤ Ř_k every term has an empty acting class at k. | proved conditionally | Corollary inputs; action-level-a | "acts on no component" |
| 51381-51386 | First-action corollary (b) | corollary | Before its first action a history is pure-T, and each component at that first level contains a whole earlier creation cube. | proved conditionally | Corollary inputs; histories-c; pure histories; empty initial region | "has been produced from the empty" |
| 51387-51389 | First-action corollary (c): h | corollary | The preceding-operation index h = k − N_k is at least one at every acting level. | proved conditionally | action-level-a; B-CMP122a notation h = k − N | "satisfies" |
| 51393-51417 | Proof of first-action corollary | proof | The action-level bound proves (a) and (c), and minimality plus pure-history propagation proves (b). | proved conditionally | action-level lemma; histories definition and histories-c; pure histories | "proved as an implication" |
| 51394-51399 | Proof of first-action (a) | proof | The acting-level inequality excludes any component action at or below its cube size. | proved conditionally | `4.15:lem-action-level`; action-level-a; corollary inputs | "Hence" |
| 51401-51413 | Proof of first-action (b) | proof | The first nonempty class has only pure-T ancestors, so the empty initial region and pure-history proposition give its creation cubes. | proved conditionally | `4.15:def-histories`; histories-c; pure-histories complement assumption | "By the minimality" |
| 51415-51416 | Proof of first-action (c) | proof | Subtracting N_k from the action-level inequality gives h ≥ 1. | proved conditionally | action-level-a | "gives" |
| 51419-51493 | `4.15:rem-non-circularity`: What the lower bound on acting levels uses; no cycle in the induction | remark | The text isolates the geometric and waiting inputs of the acting-level proof and explains their availability before the stage's R operation. | proved conditionally | histories-a, -b; action-level lemma; clause-(0) stage ordering; `4.1:thm-clause-zero` | "creates no cycle" |
| 51426-51457 | Non-circularity (1): inputs and excluded dependencies | remark | The lower-bound proof uses R only through eligibility and unchanged empty-class terms and does not use preparation, post-action heredity, analytic estimates, or clause (i). | proved in detail | Proof of `4.15:lem-action-level`; histories-a, -b | "uses exactly two properties" |
| 51460-51470 | Non-circularity (2): induction-stage ordering | hypothesis | The joint induction fixes the couplings and cube sizes before rewriting the step with a profile and performing R, and then uses the regime clause in the free-current operator theorem. | assumed | Joint proof of Theorem 0 clauses (0), (i); `4.1:thm-clause-zero`; operator theorem at free current | "are fixed first" |
| 51472-51492 | Non-circularity (2): dependency argument | proof | The acting-level bound needs only sizes, clause-(0) positivity through k, completed T steps, and acting-level definitions already available at stage k. | proved conditionally | Claimed stage ordering 51460–51470; action-level proof; cube-sizes-a; T-step and acting-level definitions | "Consequently" |
| 51495-51532 | `4.15:rem-level-inequalities`: The chain of inequalities k > N_k > N₀(k) | remark | The remark relates the action bound to Bałaban's regime condition, a shifted indexing convention, and independence from preparatory creation bookkeeping. | sketched | action-level lemma; external cube-size/N₀ lemma (c); shifted waiting rule; first-action corollary | "The regime clause in full" |
| 51496-51498 | Level-inequalities standing convention | hypothesis | Actions use the defined levels with either no-creation convention and N_k equals Ř_k. | assumed | Acting-level definition; no-creation forms; waiting-depth definition | "Throughout" |
| 51500-51505 | Regime-clause input conditions | hypothesis | The full regime comparison assumes the action-level hypotheses, clause-(0) flow bounds, odd L ≥ 5, and the external lemma's lower bound on g⁻². | assumed | `4.15:lem-action-level`; cube-size/N₀ lemma (c); `4.1:thm-clause-zero`; γ fixed before γ_H | "Assume the hypotheses" |
| 51505-51510 | External N₀ existence and `4.15:eq-level-inequalities-2` | estimate | For k ≥ Ř_k the external cube-size lemma supplies N₀(k) ≤ 2 + log_L Ř_k < Ř_k. | assumed | Cube-size/N₀ lemma (c); its three input conditions; B-CMP122a regime condition | "part~(c) of that lemma states" |
| 51511-51518 | `4.15:eq-level-inequalities-1`: full regime clause | estimate | At every acting level N₀(k) exists and k > N_k > N₀(k). | proved conditionally | action-level-a; clause (0); complement assumption; cube-size/N₀ lemma (c); proof 51535–51566 | "It holds as an implication" |
| 51519-51524 | Shifted attachment and waiting-rule convention | hypothesis | Under the alternative index k′ for scale k′ + 1, the waiting depth and creation waiting inequality are taken at k′. | assumed | N = Ř_k′; creations t ≤ k′ + 1; k′ − t ≥ Ř_k′ | "Suppose the level is attached differently" |
| 51523-51524 | Shifted acting-index bound | estimate | Under the shifted convention every acting index still exceeds its own cube size. | sketched | Shifted waiting rule; pure histories; monotonic cube sizes; proof begins 51568 and continues beyond chunk | "Then every acting index" |
| 51525-51527 | Meaning of the lower bound | remark | The no-action result is only a lower bound on acting levels and imposes no upper bound or additional restriction on K, step counts, or couplings. | proved in detail | `4.15:cor-first-action`(a) | "It bounds nothing from above" |
| 51528-51530 | Preparatory large fields and creation bookkeeping | remark | The action-level lemma is asserted to be independent of whether large-field functions introduced during preparation are counted as creations. | sketched | `4.15:lem-action-level`; Bałaban's preparatory fields; exclusion-of-dependencies discussion 51437–51456 | "does not depend on whether" |
| 51534-51582 | Proof of level-inequalities remark (partial) | proof | Part (a) combines the two bounds, and part (b) begins the first-action argument for shifted indexing before the source cuts off. | sketched | action-level lemma; external cube-size/N₀ lemma (c); shifted waiting rule; pure histories | "applies in the same way" |
| 51535-51566 | Proof of full regime clause (a) | proof | The action-level bound supplies the level hypothesis of the external N₀ lemma, whose estimate then gives the strict regime chain. | proved conditionally | action-level-a; cube-size/N₀ lemma (c); clause-(0) flow bounds; odd L ≥ 5; lower bound on g⁻² | "These hold by assumption" |
| 51561-51566 | External lemma not re-proved and dependency separation | remark | Part (c) of the cube-size/N₀ lemma is an external input to the regime comparison and is neither re-proved here nor used in the earlier action-level proof. | assumed | Cube-size/N₀ lemma (c); action-level lemma | "is not re-proved here" |
| 51568-51582 | Proof of shifted-index claim (b), cut off | proof | The first shifted action contains a creation cube and obeys its waiting bound, after which the text starts transferring the bound to later indices by monotonicity. | sketched | `4.15:lem-action-level`; `4.15:prop-pure-histories`; shifted waiting rule; running-minimum cube-size definition | "Together with" |
| 51568-51570 | First shifted acting index k′₁ | definition | k′₁ denotes the first acting index in the shifted convention. | definition | Shifted indexing convention; fixed history | "let" |
| 51571-51577 | First shifted-action estimate | estimate | A creation at t ≥ 1 and the shifted waiting rule give k′₁ ≥ t + Ř_k′₁ ≥ 1 + Ř_k′₁. | proved conditionally | Pure histories; shifted waiting inequality; no earlier action | "then gives" |
| 51578-51582 | Later shifted-action transfer (incomplete) | proof | The text invokes decreasing cube sizes to combine the first-action estimate with k′ > k′₁, but the resulting display is outside the chunk. | sketched | Running minimum x̌_j; least-power definition of Ř_j; preceding shifted estimate | "this yields" |

## Forward and backward references

References include dependencies elsewhere **within this chunk** as well as outside it. Repeated references are retained by occurrence or tightly grouped source passage; a range denotes the passage containing the listed occurrences, not an assertion that every line is a reference. Unlabelled targets are named as the text names them; no outside source was inspected.

- 50294–50299: `4.15:eq-small-field-complement-c` is identified with `-a` at later steps and `-b` at the first step; the first-step reading rests on `-3`.
- 50301–50304: second identity of `4.15:eq-small-field-complement-1` supplies the cube-wise interpretation of `-c`.
- 50306–50309: `4.15:eq-small-field-complement-b` supplies the first-step convention and its P′₀ term.
- 50311–50313: B-CMP119 (3.2)–(3.5), p. 265, defines the later-step sets; (1.2), (1.4), (1.8), (1.10), pp. 246–248, defines the first-step sets.
- 50319–50324: `4.15:def-small-field-complement` supplies P′, Q′ and Ω_t; `4.15:def-enlargement-hull` supplies enlargement, layer removal, hulls, and M.
- 50327–50334: B-CMP119 (3.16), first-step (1.18), is replaced by the decomposition in the **definition of the large-field recursion**, which supplies its tests and strict growth.
- 50346–50352: B-CMP119 (3.20) supplies the displayed comparison region; forward reference to `4.15:eq-creation-set-3` for Λ_t.
- 50360–50363: **definition of the large-field recursion** supplies the tests.
- 50370–50373: strict growth and consequent finite termination refer to where the **large-field recursion is defined**.
- 50393–50394: `4.15:eq-small-field-complement-c` supplies that Ω_tᶜ is a coarse region.
- 50407–50408: proof explicitly targets `4.15:eq-creation-set-b` and the closing assertions of `4.15:def-creation-set`.
- 50409–50415: `4.15:def-enlargement-hull` supplies extensivity of M₁ and M; `4.15:eq-creation-set-2` supplies the stage update.
- 50418–50428: `4.15:eq-creation-set-1`, `4.15:eq-small-field-complement-c`, `4.15:def-enlargement-hull`, and `4.15:eq-creation-set-2` supply coarse-region preservation and induction.
- 50430–50440: `4.15:eq-creation-set-2` is unwound to prove the inclusions and first equality of `4.15:eq-creation-set-b`.
- 50441–50449: union preservation of K and output definitions prove the second equality of `4.15:eq-creation-set-b`; comparison with `4.15:eq-creation-set-a` gives Ŵ_t.
- 50451–50457: last line of `4.15:eq-creation-set-b` and the hull/cube definitions give the creation-set coarse-region assertion.
- 50461–50462, 50468–50470: `1.5:def-densities` supplies finite terms, the initial term, and ρ_j = RTρ_{j−1}.
- 50473–50475: `4.15:def-creation-set` and `4.15:eq-creation-set-a` supply each output region and creation set.
- 50475–50477: forward reference to the recalled **rule for the level of action** immediately below.
- 50485–50489: condition (ii) and its two readings refer to `4.15:def-no-creation`.
- 50503–50506: B-CMP122a pp. 176–177 identifies the acting class and its union Z; B-CMP122a and B-CMP122b supply the decompositions inside R.
- 50509: forward promise that the next two statements are proved below (50570–50597).
- 50515–50517: `4.15:def-no-creation` supplies the common no-creation clause in both formulations.
- 50526: `4.15:def-creation-set` identifies the final recursion region in histories-b.
- 50545–50548: B-CMP119 p. 265 supplies the interpretation of the post-action region as next-step input Y.
- 50553–50557: `4.15:eq-histories-b` implies histories-c.
- 50563: forward promise of proof of existence of histories (50599–50607).
- 50567–50568: proof agenda names histories-a, histories-b, existence, and histories-c.
- 50570–50575: acting-level definition proves histories-a; `4.15:def-no-creation` supplies the common clause.
- 50577–50585: `1.5:def-densities` and B-CMP122a pp. 176–177 supply componentwise R actions and the quoted unchanged operation outside their union.
- 50595–50597: `4.15:def-creation-set` identifies the pre-action region with final stage Z⁽ⁿ_*⁾.
- 50609–50614: `4.15:eq-histories-b` is applied to the history data to prove histories-c.
- 50621–50623: `4.15:not-cube-sizes` defines Ř_j in the monotonicity lemma.
- 50632: Bernoulli's inequality is invoked for exponential growth (no work or label cited).
- 50639–50642: `4.15:not-cube-sizes` identifies the least admissible power.
- 50667–50672: the hypotheses of `4.15:lem-cube-sizes-monotone` are supplied by `4.15:eq-cube-sizes-a`, clause (0), `4.1:thm-clause-zero`, (H2), and (H5).
- 50674–50677: the stronger bound Ř_j ≤ L^(k−j)Ř_k is assigned to **part (a) of the lemma on cube sizes**; the proof here uses `4.15:not-cube-sizes` and x̌_j > 1.
- 50681; 50700–50701; 50718–50720: `4.15:def-regions-components` supplies region, touching, chain, connectedness, component, and disjointness conventions.
- 50722–50726: component-properties (a) supplies uniqueness in (b).
- 50728–50730: component-properties (a), (b) imply (c).
- 50745–50753: component-properties (a), (b) supply containment and nonemptiness in (e).
- 50755–50759: component-properties (a), (e) apply to a selected component union in (f).
- 50761–50775: component-properties (a) rules out crossing between selected components; (b) gives the converse containment.
- 50779–50781: `4.15:def-enlargement-hull` supplies enlargement iterates and hulls.
- 50809–50822: recursive enlargement definition and the just-proved distributivity supply the iteration identities.
- 50826–50829: `4.15:lem-subdivision-independence` supplies connectedness of a partition cube; `4.15:lem-component-properties`(d) supplies connectedness after adjoining cubes.
- 50831–50835: preceding one-layer proof and `4.15:lem-subdivision-independence` supply repeated enlargement and the single-cube case.
- 50842–50845: `4.15:lem-component-properties`(a) supplies decomposition into components for the hull identity.
- 50847–50853: `4.15:lem-subdivision-independence`, component-properties (d), and enlargement-connected (b) give connected enlarged hulls.
- 50855–50856: enlargement-connected (a) gives containment in iterated enlargements.
- 50869–50871: `4.15:def-enlargement-hull` supplies coordinate ranges, box, M₁, M, q₀, and replacement maps.
- 50920–50921: the linked-set proof obtains `4.15:eq-replacement-maps-1`.
- 50923–50940: `4.15:lem-subdivision-independence` (50925, 50940), replacement-maps (a), and (b) supply coarse-chain connectedness and coordinate intervals for boxing.
- 50942–50954: **replacement-map definition** and component-properties (a), (e) supply output-component ancestry.
- 50956–50963: component-properties (c) and the preceding one-map result supply the composite argument.
- 50969–50980: component-properties (a), replacement-maps (c), (d), and `4.15:def-enlargement-hull` supply M₁'s replacement property, the finite iterate M, and stabilization at q₀.
- 50983–50986: the unused **cube-fit bound** is attributed to full coupling-flow bounds and (H5).
- 50992–50998: `4.15:def-creation-set` supplies step data; `4.15:def-small-field-complement` and complement-c, concretely -a or -b, are explicit hypotheses of one-step components.
- 51008–51013: `4.15:def-creation-set`, complement-c, and `4.15:lem-enlargement-connected`(a) give the piece decomposition.
- 51024–51035: complement-c, enlargement-connected (a), and (c) justify the equalities of `4.15:eq-one-step-components-1`.
- 51037–51048: one-step-components-1 defines the pieces; component-properties (a), enlargement-connected (b), (c), and (a) supply finiteness, connectedness, and containment.
- 51054–51060: component-properties (e) and replacement-maps (e) establish (C₀).
- 51062–51074: component-properties (a), (e), creation-set-b, and replacement-maps (e), together with (C_n), establish (C_n+1).
- 51076–51078: `4.15:def-creation-set` and creation-set-b identify (C_n_*) with one-step components (b).
- 51080–51088: enlargement-connected (c), (a), one-step-components-1, and replacement-maps (e) give Y containment and increasing stages.
- 51095–51101: complement-c and the concrete formulas complement-a and -b supply coverage of P′ ∪ Q′ by the G_i; the preceding paragraph supplies the final inclusions.
- 51105–51114: extensivity, stage definitions, and creation-set-b give containment of the final cube set and Ŵ_t.
- 51116–51117: component-properties (c) applied with one-step (a) proves one-step (c).
- 51121–51126: one-step components (b) supplies whole-cube containment; complement-c and the recursion shape are identified as its only inputs beyond geometry.
- 51131–51140: complement-c is assumed, and `4.15:def-histories` supplies the history and its regions.
- 51148–51154: one-step components (b), explicitly described as proved above from the assumed complement-c, gives the base case of pure histories.
- 51156–51164: histories-c identifies the incoming old region; one-step components (b) then supplies the two induction cases.
- 51184–51185: no-creation-a and -b in `4.15:def-no-creation` are the alternative hypotheses for the waiting rule.
- 51204–51208: histories-a in `4.15:def-histories` supplies acting conditions, particularly (ii).
- 51210–51212: no-creation-a supplies the untruncated forbidden window.
- 51214–51225: no-creation-b supplies the truncated integer window.
- 51231–51234: the argument identifies the resulting inequalities with waiting-rule-a.
- 51237–51240: no-creation-a/-b are compared using `4.15:prop-pure-histories` to exclude creation-free components in a pure history.
- 51245–51253: clause (0), `4.1:thm-clause-zero`, cube-sizes-a, complement-c, and `4.15:def-small-field-complement` are assumed by the action-level lemma.
- 51255–51260: conditions (i)–(iii) in `4.15:def-histories`, and no-creation-a/-b in `4.15:def-no-creation`, specify permitted actions.
- 51271–51277: Theorem 0 supplies quantifiers, L₀(N), constant-ordering conventions, and admissibility conditions.
- 51282–51285: `4.15:def-histories` supplies a history and its acting classes.
- 51292–51299: histories-b and histories-c show pure-T ancestry before k₁, with empty initial Y from complement-c.
- 51301–51306: `4.15:def-histories` supplies the pre-action term and the initial segment of its history.
- 51308–51314: `4.15:prop-pure-histories` is applied using complement-c as hypothesis (b).
- 51316–51328: `4.15:lem-waiting-rule`, no-creation-a/-b, and waiting-rule-a yield action-level-2.
- 51331–51332: action-level-2 gives action-level-a when k = k₁.
- 51334–51345: `4.15:lem-cube-sizes-monotone` is applied with (H2) from `2.2:not-hypotheses`, (H5), and hypothesis (a); its bound is combined with action-level-2.
- 51349–51356: cube-size monotonicity also supplies integer powers; `4.15:not-cube-sizes` defines N_k = Ř_k, identifying the conclusion as action-level-a.
- 51358–51361: action-level-a gives the equivalent no-action statement.
- 51367–51374: corollary assumptions refer to clause (0), `4.1:thm-clause-zero`, cube-sizes-a, the hypothesis of pure histories, `4.15:def-histories`, and no-creation-a/-b.
- 51381–51386: `4.15:prop-pure-histories` is the stated source of first-action creation cubes.
- 51387–51389: B-CMP122a supplies the preceding-operation notation h = k − N.
- 51394–51399: `4.15:lem-action-level`, explicitly an implication from the assumed inputs, and action-level-a prove corollary (a).
- 51401–51413: `4.15:def-histories`, histories-c, and `4.15:prop-pure-histories` supply the pure first-action ancestry and creation cubes for corollary (b).
- 51415–51416: action-level-a proves corollary (c).
- 51421–51423: `4.15:def-histories` and `4.15:lem-action-level` supply the notation of the non-circularity remark.
- 51426–51435: the proof of the action-level lemma is analyzed through histories-a and histories-b.
- 51440–51456: unused external objects are identified as B-CMP122a's preparatory decompositions and new regions Z″_j, B-CMP122b's two component classes, the second clause of condition (ii) in B-CMP122a, Bałaban's N₀(k), the **lemma on levels of action accompanying their definition**, the **block-law comparison lemma**, the **operator theorem at free current**, and Theorem 0 clause (i); cube-sizes-a is named as the only required coupling-flow bound.
- 51460–51467: the joint induction proving Theorem 0 clauses (0), (i), with clause (0) identified as `4.1:thm-clause-zero`, is asserted to fix couplings and cube sizes first.
- 51469–51470: the **operator theorem at free current** is said to use the regime clause at stage k after couplings are fixed.
- 51472–51483: the proof of the action-level lemma is revisited; cube-sizes-a is said to be available at stage k, and the completed T-step definitions and acting-level definitions are its other inputs.
- 51485–51489: excluded dependencies include Theorem 0 clause (i), the **operator theorem at free current**, **representation and bound of large-field terms**, `4.4:cor-localised-independence`, the **large-field coupling increment**, and the **regime clause**.
- 51491–51492: inserting the action-level lemma in the induction is asserted not to create a cycle.
- 51496–51498: the **definition of the level of action**, both forms of condition (ii), and waiting-depth convention are assumed throughout the last remark.
- 51500–51510: the action-level lemma's hypotheses and **part (c) of the lemma on cube sizes and Bałaban's N₀** are invoked; clause (0), `4.1:thm-clause-zero`, odd L ≥ 5, and its coupling ceiling supply the latter's inputs, and B-CMP122a supplies the regime condition.
- 51515–51518: the full regime clause is identified as an implication from clause (0), the complement description assumed in the action-level lemma, and the external cube-size/N₀ lemma (c).
- 51525–51527: first-action corollary (a) is interpreted as only a lower bound.
- 51528–51530: the action-level lemma is asserted independent of counting **Bałaban's preparatory large-field functions** as creations.
- 51535–51543: the action-level lemma and action-level-a supply the level hypothesis of the cube-size/N₀ lemma (c).
- 51545–51553: `4.1:thm-clause-zero` supplies flow bounds; the odd-L and inverse-coupling bounds remain assumptions; the external lemma (c) supplies N₀ existence and level-inequalities-2.
- 51554–51559: level-inequalities-2 and the action-level bound yield level-inequalities-1.
- 51561–51566: the text explicitly reiterates the action-level lemma's inputs and says the cube-size/N₀ lemma (c) is **not re-proved here** and is **not an input** of the earlier action-level proof.
- 51568–51573: the action-level lemma's argument is reused for shifted indexing; pure histories supplies a whole creation cube at the first acting index.
- 51574–51577: the shifted waiting rule assumed in (b) supplies the first shifted-action estimate.
- 51578–51582: running-minimum and least-power definitions supply cube-size monotonicity for the next, unfinished displayed inference.

## Obligations named here

This chunk names no unresolved analytic or mathematical theorem as “remains to be proved.” It does explicitly impose inputs and rules, promise several proofs that it then supplies, and identify an external result not proved here. These distinctions matter for later readers.

- 50288–50299: the complement hypothesis requires finitely many coarse G_i contained in P′ ∪ Q′, nonnegative integer enlargement depths, the coarse hull of incoming Y, and empty Y at t = 1; the first-step reading rests on complement-3 outside the chunk.
- 50327–50334, 50360–50373: the recursion definition elsewhere must supply the stipulated tests and strict growth used to guarantee stopping; the text says the latter is already shown there, not open here.
- 50369–50370: stopping requires both the bond and low-cube outcomes to be empty.
- 50481–50492: eligibility requires the first simultaneous satisfaction of the size bound (i), adopted waiting/no-creation rule (ii), and no still-waiting nested component (iii); the stronger reading of (ii) also requires j ≥ N_j.
- 50509–50526: histories-a and histories-b are promised proofs below; those obligations are discharged at 50570–50597.
- 50563: existence of histories is promised a proof below; it is supplied at 50599–50607.
- 50619–50623: the monotonicity lemma requires integer L ≥ 2, r > 0, and x_j > 1 through the relevant level; the theorem-context sources are named at 50667–50672.
- 50994–50998: the one-step proposition explicitly assumes the small-field complement description, concretely complement-a or complement-b.
- 51050–51052: (C_n) is announced as an induction obligation; 51054–51078 proves it and identifies its final instance with proposition (b).
- 51131–51137: the pure-history proposition requires the complement reading and empty A_j for all j < k.
- 51144–51146: the creation-cube induction statement is announced for each j; the induction is completed at 51175.
- 51181–51185: the waiting lemma supposes a whole creation cube at 1 ≤ s ≤ k inside the acted-on component and requires one of the two stated no-creation formulations.
- 51243–51260: the action-level lemma assumes clause-(0) positivity, the complement description for every step, and actions only at the prescribed levels with either no-creation convention.
- 51316–51325: the proof explicitly checks the waiting lemma's action, fixed-history, and whole-creation-cube premises before using it.
- 51334–51343: the proof explicitly checks the cube-size lemma's integer-L, positive-r, real-coupling, and x_j > 1 premises, drawing on (H2), (H5), and hypothesis (a).
- 51365–51374: the first-action corollary again assumes clause (0), the complement description, and the defined acting levels/no-creation convention.
- 51447–51449: conditions (i), (iii), and the second clause of (ii) are acknowledged as additional restrictions on actions although unused in the lower-bound proof.
- 51460–51470: the non-circularity explanation presupposes the asserted ordering that fixes couplings and cube sizes before profile rewriting and R, with the regime clause used only after the couplings are fixed.
- 51496–51505: the regime comparison assumes the acting-level convention, action-level hypotheses, clause-(0) flow bounds, odd L ≥ 5, and the external lemma's one-sided bound on g⁻² (or ceiling on γ before γ_H).
- 51505–51510, 51542–51553: the external N₀ estimate additionally requires k ≥ Ř_k; the action-level inequality verifies this at acted-on levels, while the other three conditions explicitly “hold by assumption.”
- 51519–51524: the shifted-index variant assumes depth N = Ř_k′ and waiting inequality k′ − t ≥ Ř_k′ for creations t ≤ k′ + 1.
- 51561–51566: the cube-size/N₀ lemma (c) is explicitly “not re-proved here”; this is an external proof dependency, not a declaration that the result remains open.
- 51568–51582: the proof of the shifted-index variant continues beyond the chunk; the displayed combination for later indices is not present here, and no subsequent proof of remark (d) appears in these lines.

## For the stage question

There are **no statements here about complex domains, analytic balls, admission or inclusion of backgrounds, or minimisers**, and no occurrence of an explicitly named drop-out or prepared shell. “Small-field domain” here denotes a spatial region; this chunk does not establish any complex analytic domain or background-admission property. The relevant stage, term-carrying, preparation, and exclusion statements are indexed below, without identifying them with those absent analytic notions.

| Lines | Statement relevant to stages or preparation | Status here |
|---|---|---|
| 50284–50299 | The incoming region Y enters each step's complement through its coarse hull and is empty at the first step. | assumed |
| 50301–50309 | The complement incorporates the previous step's large-field region, and first-step inclusion needs the adopted P′₀ ∪ P′₁ convention rather than the narrower P′₁ convention. | proved conditionally |
| 50327–50334 | A labelled term uses the replacement recursion's outcome R, I, and low-cube set, with R in the shrunken small-field spatial domain. | definition |
| 50354–50368 | A stage has cube set R_n, boxed region Z⁽ⁿ⁾, complementary Λⁿ, bond tests, and previously untested rim cubes; its updates accumulate cubes and retain the old region. | definition |
| 50369–50373 | Every term-labelling outcome stops after finitely many stages because the cube sets grow strictly in a finite set, using growth established elsewhere. | proved conditionally |
| 50375–50391 | The final stage supplies the output large-field region and aggregate creation data for that term. | definition |
| 50393–50458 | Stage regions increase and remain coarse regions, while the final cube union records all accumulated creation cubes. | proved in detail |
| 50461–50477 | Terms carry sequences of small-field labels, T branches into outcome terms, and R subsequently acts on components that become eligible. | definition |
| 50479–50507 | R acts at the first level satisfying the size, waiting, and nesting conditions, and its actions produce labelled terms of ρ_j. | definition |
| 50517–50526; 50577–50597 | An empty eligible class carries the term and its label unchanged into ρ_j, retaining the final recursion region. | proved conditionally |
| 50528–50548 | A history selects the outcome at every step and distinguishes pre-action Z_j from post-action Z_j^post, which is the next step's input Y. | definition |
| 50550–50557; 50609–50616 | Bond and low-cube labels enter the waiting rule through creation sets, and empty-class levels have equal pre-action and post-action regions. | proved conditionally |
| 50559–50563; 50599–50607 | Pure-T histories have no earlier acting class, and every term, including a pre-action term, has a history. | proved in detail |
| 50988–51005; 51007–51118 | Assuming the complement description, each step retains the old region and creation set, and every output component contains an old component or a whole new creation cube. | proved conditionally |
| 51050–51078 | At every recursion stage each component has an old-component or source-cube ancestor, by induction through the update and boxing. | proved conditionally |
| 51120–51126 | The whole-cube ancestry result uses recursion shape and the complement hypothesis, without field tests or thresholds. | proved conditionally |
| 51129–51176 | Before any R action, old creation cubes persist through the sequence of T-produced regions in the stated component-containment sense. | proved conditionally |
| 51178–51240 | An acted-on component containing a creation cube must wait the stated depth, and the two no-creation formulations agree for components along pure-T histories. | proved conditionally |
| 51242–51362 | Every acting level exceeds its own cube size; the argument uses the history before its first action and monotonicity to control later levels. | proved conditionally |
| 51364–51417 | The first acted-on region is produced from the empty region by T alone, each component contains an earlier creation cube, and the preceding-operation index is at least one. | proved conditionally |
| 51426–51435 | The action-level proof uses only the no-creation eligibility clause and the fact that an empty acting class leaves a term and its next-step input unchanged. | proved in detail |
| 51437–51446 | The proof does not use Bałaban's preparatory decompositions or their excluded components, the Z″_j sequence, B-CMP122b's division into two classes, post-action regions, or heredity of creations through R. | proved in detail |
| 51440–51442 | The components excluded by preparatory decompositions are said to concern only a nonempty acting class A_j. | assumed |
| 51460–51467 | At induction stage k the couplings and cube sizes are fixed before profile rewriting and the R half-step, and the same ordering is asserted for stage k + 1. | assumed |
| 51469–51470 | The regime clause is used at stage k by the free-current operator theorem after g₀ through g_k are fixed. | assumed |
| 51472–51492 | The action-level argument uses data available by stage k and excludes analytic estimates, large-field term bounds, localized-term independence, and the regime clause as dependencies. | proved conditionally |
| 51500–51518; 51535–51566 | The external cube-size/N₀ result and the action-level bound together imply the full regime clause at every acted-on level without following creation cubes through R steps. | proved conditionally |
| 51519–51524; 51568–51582 | With the alternative density-index attachment and its assumed waiting rule, the text begins the analogous first-action and later-index argument, which is cut off here. | sketched |
| 51528–51530 | Counting or not counting large-field functions introduced during Bałaban's preparation as creations is asserted not to affect the action-level lemma. | sketched |

The preparation references above describe dependencies and excluded components; they do not supply a stage-by-stage background-admission theorem or identify any prepared-shell mechanism in this chunk.
