# State of attack

**gap (unrestricted claim).** Lemma 7, Step 1 cites an exhaustive computation for its shelling order. That citation supplies no proof under `GOAL.md`, “No computer-assisted steps.” The assertion for every library-good pattern remains unproved here; no counterexample to that precise class was found by the hand arguments below.

**discharged (hand obstruction).** The literal vertex-good definition in the **part file alone** does not imply shellability: `Q_4 \ {(000,0),(111,0)}` is a counterexample, proved below. The library definition explicitly also requires good facets, so it excludes this example. This does **not** refute Lemma 7 or provide a counterexample to its actual good-pattern class.

**discharged (combinatorial repair).** Every union of parts of a guillotine partition with distinct coordinates is an initial segment of a shelling of the whole cube. The four-block induction below proves this in every dimension, including after restriction to a subcube. No classification or enumeration is used.

**implication (consumer result).** The restricted Lemma 7G below supplies the missing combinatorial step for generated tile regions, box cuts and patches made of lifted tiles, given the local tiling property (T4). Library Lemma 8 and the direct chart uses in Lemmas 4.5d, 4.5f, 4.5j and Theorem G' keep the same shelling input. The remaining analytic estimates are **unchecked** here, not newly discharged.

**gap (honest stop).** The adapted domains `2B` in Lemma 4.5h are not shown to be in the restricted class. The exact still-needed estimate is (AB) below. Consequently the full chain through 4.5h and hence 4.5j is not declared repaired. The shelling task is complete for the generated class; the consumer check stops at this named geometric/analytic handoff.

**discharged (scope).** This session reads only the supplied directory, writes only this file, and uses no numerical job, enumeration, web source, or subagent. The supplied provenance is commit `28e261c17`; it is not independently verified from history. `GOAL.md` and `FINISH-rules.md` were read first.

## Definitions and the first attack

**discharged (source transcription).** Text 3.2 defines `K(S)` to have the retained vertices of `Q_d`, their cube edges, and every square whose four vertices are retained. At an edge (`d=3`), goodness means that every component is simply connected. At a vertex (`d=4`), the part's sentence additionally excludes the cube with exactly an antipodal pair removed. A *region* must pass both the edge and vertex conditions. The definition immediately before library Lemma 7 is stronger and explicit: a vertex pattern must also have good facets. Thus the part's isolated vertex definition and the library's definition are not identical; the all-local-patterns requirement on a region supplies the missing facet condition.

**discharged (precise shelling predicate).** Write `z^J` for flipping the coordinates in `J`. For an ordering `z_1,...,z_m`, put

\[
 D_k=\{i:z_k^{\{i\}}\in\{z_1,\ldots,z_{k-1}\}\}.
\]

The required predicate is: for every `k>1`, `D_k` is nonempty and `z_k^J` is earlier for every nonempty `J` contained in `D_k`. The first vertex is exempt. `I` must mean **all** earlier-neighbour directions, not an arbitrarily chosen nonempty subset: the gauge has to match on every earlier adjacent orthant. With the subset reading every connected graph admits such an order (add a vertex adjacent to the current connected set until all vertices have been added), and a ring would pass too.

**discharged (counterexample to the vertex-only reading).** Let

\[
 S=\bigl((Q_3\setminus\{000,111\})\times\{0\}\bigr)
   \cup\bigl(Q_3\times\{1\}\bigr).
\]

The two removed vertices have distance three, so they are not antipodal in `Q_4`. `K(S)` is connected and simply connected. To see this directly, move each lower-layer edge to its upper twin across its vertical square; the vertical edges needed for this exist at every retained lower vertex. Thus every edge loop is homotopic to an upper-layer loop. In the full upper cube, encode a path by the coordinates it flips. Swapping two consecutive distinct flips crosses a retained square; consecutive equal flips cancel a backtrack. Sorting the word of any loop by these swaps gives an even number of each coordinate, and all flips cancel. This contracts every loop. The same argument applies to continuous loops in this square complex: within each square, replace a path segment by a boundary path, after subdividing a loop into segments in faces; hence its fundamental group is represented by edge loops.

For the obstruction, call a vertex a *corner* of a retained set if every nonempty subset of its retained-neighbour directions leads to a retained vertex. The last vertex of any shelling with at least two vertices must be a corner. Put `a=(000,0)`, `b=(111,0)`, `u=(000,1)`, `v=(111,1)`. If the first-three-coordinate weight of `z` is one, the directions from `z` to `b` all have retained individual neighbours, but their simultaneous flip reaches missing `b`. If that weight is two, use missing `a` instead. This works in either layer. Therefore the only possible corners of `S` are `u,v`, and both are corners since their retained neighbours span the full upper cube.

Delete `u`, as any reverse shelling might. The preceding missing-vertex witnesses still work: none of their required individual neighbours is `u`. At `v` all three upper neighbours remain, but flipping all three reaches the now missing `u`. Thus `S\setminus\{u\}` has no corner. Deleting `v` first gives the identical argument with zero and one interchanged. There can be no shelling.

**discharged (what this breaks and does not break).** The bottom facet is the six vertices of `Q_3` of weights one and two. Each has two neighbours in the facet; the sequence `100,110,010,011,001,101,100` displays its cycle. Every square of `Q_3` contains `000` or `111`, so the facet has no squares. Its cycle is noncontractible: identify the six edges consecutively with the unit circle; lifting a once-around traversal to the real line changes its endpoint by one, whereas an endpoint-fixed contraction would preserve that integer. It violates the edge-good condition. Hence the example refutes the part's vertex-only reading but is **not library-good**. No counterexample satisfying the library's stronger definition has been established here.

**discharged (the other immediate obstruction is expressly excluded).** In `Q_4\{0000,1111}`, a weight-one vertex has all individual neighbours towards `1111`, but the combined flip is missing. At a weight-two or weight-three vertex use `0000` instead. No vertex is a corner, so there is no possible last vertex of a shelling. This is exactly the antipodal exception already present in the definitions, not a new counterexample to them.

## What is actually generated

**discharged (source transcription).** A guillotine partition with distinct coordinates is trivial, or splits on a coordinate `i`, then recursively partitions the two facets using disjoint coordinate sets, neither containing `i`. Text 3.2 defines regions as unions of tiles. Its (T4) says their local tile partitions have exactly this form; (T2) gives nesting under refinement. Lemma 3.2a treats unions of parts and their restrictions to a subcube. Its written induction gives connectivity and simple connectivity via a product intersection. It does not supply a shelling order.

**unchecked (scope boundary).** The shelling proof takes this local guillotine description as its hypothesis. It does not certify the global tiling construction, its numerical claims, or the analytic estimates in the library.

## A shelling by induction, with an extension property

**discharged (product rule).** If `u_1,...,u_s` and `v_1,...,v_t` shell two vertex sets on disjoint coordinate sets, their lexicographic product order (first `u`, then `v`) shells the product. At `(u,v)` the earlier-neighbour directions are exactly `D_u` and `D_v`. A nonempty flip involving a `u` direction lands in an earlier `u` block, and any additional `v` flips stay in the second set by its shelling predicate. A flip involving only `v` directions is earlier in the same block. The union of the direction sets is nonempty except at the first pair. In particular, products of the two-vertex order `0,1` shell a full cube; the zero-dimensional cube has its single vertex as its order. If an order of a full cube starts with `A`, its product with a full cube starts with `A` times that full cube.

**discharged (theorem).** Let `P` be a guillotine partition with distinct coordinates of `Q_d`, and let `S` be any union of its parts. There is a shelling of **all** `Q_d` in which `S` is an initial segment. If `S` is nonempty, that segment is a shelling of `S` and in particular connects it.

**discharged (induction setup).** Induct on `d`. For a trivial partition, `S` is empty or the full cube and the product order just given works. Otherwise write the root coordinate as `i`, and the disjoint sets of coordinates used in its two subtrees as `X,Y`. The unused coordinates form `R`. On the two facets, selection of leaves depends only on the respective subtree coordinates. Consequently

\[
 S=\left(\{0\}\times A\times Q_Y\;\cup\;
          \{1\}\times Q_X\times B\right)\times Q_R,
\]

where `A` and `B` are unions of parts of the smaller partitions on `Q_X` and `Q_Y`. The induction gives full-cube shellings `prec_X,prec_Y` beginning with `A,B`, respectively. Remove the free factor `Q_R` for now; the product rule restores it at the end. Write `D_X(x),D_Y(y)` for the earlier-neighbour directions in those full-cube orders.

**discharged (empty cases).** If both `A,B` are empty, use any full-cube product order. If exactly one is nonempty, put its entire root facet first, ordering that facet by the smaller cube order with its selected prefix, followed by the free coordinates. Then put the opposite facet in the same facet order. The first facet is a shelling; in the second, the extra earlier direction is `i`, and every mixed flip involving `i` lands in the already complete first facet. Thus this is a shelling, with exactly the desired selected vertices first. This also covers subtrees with no used coordinates.

**discharged (four-block construction when `A,B` are nonempty).** List these four blocks, omitting any empty block. Within each block use the indicated outer and inner loops, always in the previously obtained orders.

| Block | Vertices | Outer loop | Inner loop |
|---|---|---|---|
| 1 | `(0,x,y)`, `x in A`, `y in Q_Y` | `x` | `y` |
| 2 | `(1,x,y)`, `x in Q_X`, `y in B` | `y` | `x` |
| 3 | `(0,x,y)`, `x in Q_X\A`, `y in Q_Y` | `x` | `y` |
| 4 | `(1,x,y)`, `x in Q_X`, `y in Q_Y\B` | `y` | `x` |

Each vertex occurs once. Blocks 1 and 2 are exactly `S` (before restoring `R`). Within facet zero, the combined order of blocks 1 and 3 is the full product order `x` then `y`. Within facet one, blocks 2 and 4 give the full product order `y` then `x`. Hence at every vertex the earlier-neighbour directions within its own facet are exactly `D_X(x) union D_Y(y)`, and all their nonempty subset flips are earlier, by the product rule. Interposing the other facet's blocks does not change this fact.

The only new direction to check is `i`:

| Block | When `i` is an earlier-neighbour direction | Why every mixed subset flip is earlier |
|---|---|---|
| 1 | Never | There is no such subset. |
| 2 | Exactly when `x in A` | Flips in `D_X(x)` keep `x` in `A`, since `A` is an initial segment; all resulting opposite-facet vertices lie in block 1. |
| 3 | Exactly when `y in B` | Flips in `D_Y(y)` keep `y` in `B`; all resulting opposite-facet vertices lie in block 2. |
| 4 | Always | Facet zero is already complete. |

Here a zero-coordinate flip leaves `x` or `y` unchanged, so the same verification includes the subset consisting of `i` alone. For a nonempty flip in `D_X(x)` or `D_Y(y)`, the induction says the result is earlier in that smaller order; the initial-segment property is exactly what keeps it selected when needed.

Finally every vertex other than the first has an earlier neighbour. This follows within either full facet order except at that facet's first vertex. Facet zero's first vertex is the global first vertex. Facet one's first vertex lies in block 2 with the first `x` in `A` and the first `y` in `B`, so its opposite neighbour in block 1 is earlier. This verifies **all** clauses of the shelling predicate. Restoring `Q_R` by the product rule completes the induction.

**discharged (subcube restriction).** Restrict a distinct-coordinate cut tree by fixing some coordinates. At a node whose coordinate is fixed, keep only its prescribed child; at every other node retain the cut. No remaining coordinate is repeated, and the resulting leaves are precisely the nonempty intersections of the old leaves with the subcube. The same theorem therefore applies to `S intersect Q'`. Coordinate permutations and coordinate reversals preserve both the tree property and the shelling predicate.

**discharged (why this supplies the Step 1 combinatorics).** For a nonfirst vertex `z`, set `I=D_z`. The full subcube `{z^J:J subset I}` consists of the new vertex and earlier vertices. Its orthant boxes form the box `B` used by Step 1; `O=B\z` is wholly earlier. Every earlier face-adjacent orthant is one of these `z^{i}`, because `I` contains all such directions. Thus there is no earlier interface omitted by this construction. In dimension four the order has at most `2^4=16` vertices, directly from the four binary coordinates. This bound uses no list of patterns and depends on no lattice depth, tile side, or enumeration.

**discharged (connectivity and loop reduction, independently of Lemma 3.2a).** Every nonempty shellable set is connected, because each new vertex has an earlier neighbour. In an edge loop, choose its latest vertex `z`. A segment `z^i,z,z^j` with `i=j` is a backtrack; with `i!=j`, the shelling supplies the earlier vertex `z^{i,j}` and the retained square, so replace it by `z^i,z^{i,j},z^j`. This removes one visit to `z` without introducing any later vertex. Repeating removes the latest vertex and eventually reduces the loop to the first vertex. This proves the square-complex simple-connectivity condition in edge-loop form, with explicit elementary homotopies.

**discharged (topological detail used above).** Edge loops suffice here for continuous simple connectivity. Triangulate each square, compatibly along edges. The open stars of vertices cover this finite triangulation. Subdivide the parameter circle finely enough that each closed parameter interval maps into one open star. Here is the compactness argument: about each parameter value choose an interval mapped into one star; take a finite collection of the half-sized intervals covering the parameter circle, and a subdivision whose mesh is smaller than half the minimum of their original radii. Any subdivision interval meeting one of the half-sized intervals stays in its original interval. An open star contracts radially to its vertex. Replace each segment using that contraction by the two radial paths through this vertex. At a shared endpoint, the two chosen stars meet, so their vertices and the endpoint lie in one simplex; replace the two radial paths there by its edge. This gives a loop in the triangulated edge graph. For any introduced vertex choose a corner of the smallest original cell containing it. Each triangulated edge and both chosen corners lie in a single original square or edge, a convex set; replace it there by an original boundary-edge path, using straight-line homotopies and the fixed vertex-to-corner paths. Thus every continuous loop is homotopic to an original edge loop, as used in both arguments above. For the ring obstruction, the lift and its homotopy invariance can likewise be seen without a classification theorem: subdivide paths, and a proposed homotopy into a fine grid, until each piece lies in a circle arc of length less than one half; choose the real angle consistently on successive arcs. The lifted endpoint of a closed path is integer-valued and continuous throughout the homotopy, hence constant.

**discharged (generated patterns are library-good).** Apply the shelling and loop reduction also to every three-dimensional facet. Their nonempty retained sets are connected and simply connected. A generated four-dimensional pattern cannot be the excluded antipodal-pair complement, since the theorem shells it whereas the separate corner argument above proves that complement unshellable. Thus the restricted class satisfies every clause of the library definition, without its enumeration.

## Restricted Lemma 7 and the domain check

**implication (Lemma 7G, proposed restricted analytic statement).** Let `Omega` be a finite cell region with the crossing links specified in Lemma 7, cell side `N`, such that at every local face its retained cells form a union of parts of a guillotine partition with distinct coordinates. Replace “all local patterns good” in Lemma 7 by this hypothesis. Subject to the remaining analytic steps of that lemma, there is a linear operator `T` on exact two-forms such that

\[
 dT(da)=da,\qquad
 \|T(da)\|_4\le C\|da\|_2,\qquad
 \|T(da)\|_2\le CN\|da\|_2,
\]
\[
 \|T(da)\|_2\le C\|a\|_2,\qquad
 \|T(da)\|_2\le C\|da\|_{4/3}.
\]

Here `C` may depend on the finite pattern and the chart nerve, as in the source, but not on `N`. The difference `T(da)-a` is closed, and is a gradient when `Omega` is simply connected. This report discharges the missing **shelling** step of this restricted statement, including the order, all earlier interfaces, and the bound of sixteen chart steps. It does not label these analytic inequalities discharged: the box estimates, lattice folding extension, overlap/constant gluing and operator bounds remain the analytic inputs of the original proof.

**implication (Lemma 8G).** Keep the box alternative of Lemma 8; in its chart alternative require a chart whose pattern is generated as above. Its claimed conclusion remains `sup |a'| <= C A N^{-sigma}` under its displayed Morrey hypothesis. The combinatorial induction supplies exactly the chart order used in its sup-norm proof. The phrase “gauge ... of Lemma 6” in its statement must, for this alternative, be read as the Step 1 chart gauge that its proof actually uses. The kernel estimate and the sup-norm folding estimate are not re-proved here.

**discharged (structural closures).** Selecting, deleting, uniting, or intersecting parts of **one fixed** local partition leaves a union of its parts. At a box cut, the allowable incident signs are obtained by fixing coordinates, so the subcube-restriction argument applies. Refining retained coarse cells introduces free coordinates in their interiors and preserves the transverse pattern at their old faces, so the product and restriction arguments apply there too. Reflections and coordinate permutations were already covered. These facts do not assert closure for arbitrary combinations of two unrelated tilings.

**implication (matching Text 3.2).** Assuming its tiling has (T3), its stated (T4) follows directly: restrict the actual tree of cuts to the incident orthants at the face in question. Every cut that separates those orthants passes through that face. By (T3) a coordinate occurs at most once among those cuts. This is precisely a distinct-coordinate guillotine tree. Regions chosen as unions of its tiles therefore have the hypothesis of Lemma 7G. Under (T2), unions and differences involving a coarse region and a finer region are selections in a common finer tiling. The existence, separation bounds and counting assertions for the global tiling are outside this shelling proof; no computation cited for them is adopted here.

**discharged (why local patterns survive a cover).** For a covering of the local square complex, fix one lift of a retained cell at a vertex. Connect any other incident retained cell to it in the local `K(S)`. The shelling loop reduction shows that two choices of path differ by backtracks and square moves. Each such move lifts to a backtrack or a square, so their lifted endpoints agree. Thus a whole connected local pattern lifts as a copy, without splitting or identifying its vertices. This uses the proved simple connectivity, not connectivity alone. In such a lifted star, choosing whole lifted tiles chooses whole parts of the same local partition: the cells of one part are joined within that part. Intersecting with a box again restricts to a subcube. Therefore finite unions of whole lifted tiles followed by box cuts have generated local patterns, assuming the original tiling has (T4).

**implication (consumer ledger; geometric coverage is distinguished from analytic validity).**

| Consumer | What it reads | What the restriction supplies |
|---|---|---|
| Library Lemma 8 | A box or a Step 1 chart; boundedly many sup-norm gluing steps | Generated charts have the required order and at most sixteen steps. Its analytic Morrey argument remains conditional on the stated kernel and folding bounds. |
| Lemma 4.5d, region/patch paragraph | A curvature potential on a finite union of lifted tiles, possibly with periods | Such patches and box cuts have the required local patterns by the preceding cover argument and (T4). All stated norms, linearity and the closed-form alternative are retained in 7G. Its broader opening phrase about finite unions of boxes is not proved here; Lemma 6 has its own ordered-overlap hypothesis. |
| Theorem G', including its loops paragraph | `a(f)` with `d a(f)=f`, the critical norm bound, and bounded `a composed with d` | Its specified patch geometry is covered by 7G. Nothing here makes the whole patch simply connected or removes periods; the separate period argument is still required and unchecked here. |
| Lemma 4.5f, hence the input used by 4.5g and 4.5j | Vertex charts with the local `l^2` gauge bound | These are precisely the generated charts. The local combinatorial constants have at most sixteen steps and introduce no dependence on `P_0`, `P` or refinement depth. The constraint and gauge-normalization estimates are separate analytic inputs. |
| Lemma 4.5h | A potential on **every adapted `2B`**, with `l^{4/3}` to `l^2` control | **gap: not yet supplied by restricting to generated patterns.** Its additional artificial ball boundary needs the check below. |
| Lemma 4.5j | Lemma 8 gauges on the vertex charts of 4.5f, plus the Morrey bound of 4.5h | Its direct chart use is covered. The stated scope “any region with good local patterns” must be narrowed to the generated regions for this repair. Its dependence on 4.5h remains conditional on the adapted-ball issue below and on the other analytic inputs. |

**gap (AB: the exact additional obligation in Lemma 4.5h).** In `lattice_gehring_hls.md`, Section 3, for `r <= N/4` an adapted ball is a union of grid cubes of side `r/4` meeting an intrinsic ball; larger radii use an unspecified finite list of unions of cells and parts of cells. A union of those small cubes is not stated to be a union of parts of a single original local guillotine partition, or an intersection with a single box. The closure arguments above therefore do not establish its local shellability. Nor does “boundedly many cubes joined by faces” provide the ordered, full, comparable-box overlaps required by Lemma 6, which that library's hostile check (c) invokes at small scales. No failure of the estimate is proved here; the geometric handoff has not been justified.

For exactly the adapted domains used in the reverse Holder argument, what remains to be supplied is a constant `C` independent of `N`, `r`, the refinement depth and the allowed region, such that

\[
 \boxed{\quad
 \text{for every exact }f\text{ on }2B,
 \quad\exists a_{\rm loc}:\quad
 d a_{\rm loc}=f\text{ on }2B,\qquad
 \|a_{\rm loc}\|_{\ell^2(2B)}
       \le C\|f\|_{\ell^{4/3}(2B)}.
 \quad} \tag{AB}
\]

It is enough for the consumer to prove (AB) for its minimal curvature `f=f^*`. A route through 7G requires a hand proof of the generated-pattern hypothesis for those `2B`, together with the uniformly comparable cell geometry. A route through Lemma 6 requires the actual box order and its full overlap bounds, with the `l^{4/3}` input estimate. Neither route follows merely from the shelling theorem proved here. Changing the adapted domains would also require checking the covering and reverse Holder argument on the changed family.

**discharged (read/write record).** Read `GOAL.md` and `FINISH-rules.md`; the definitions, construction and relevant consumers in `parts/hard-core--independent.md`; the definition and Lemmas 5–8 with relevant nearby text in `library/lattice_sobolev_box_gauge.md`; and the adapted-ball definition and its stated handoff in `library/lattice_gehring_hls.md`. Searches also returned nearby material in those permitted files; none of its reported runs is used as proof. No check script was read or run, no other account or external source was consulted, and only `library/shelling-by-hand.md` was written. No commit, post or subagent was made.

## Final status

**discharged.** The construction theorem, its product and subcube closures, and its explicit four-block order prove the shelling required by Step 1 for every generated pattern, in any dimension. The order handles all earlier neighbours and uses at most sixteen orthants in dimension four. The two obstruction arguments are hand proofs; neither is a counterexample to the library's full good-pattern definition.

**implication.** On the generated domains, the analytic conclusions of 7G and 8G follow only if the original box, folding, gluing and operator estimates hold. Matching the draft's actual tile domains additionally uses (T4), or (T3) with the cut-tree argument above; common refinement uses (T2). The full uses of 4.5h and the consequent Morrey input to 4.5j additionally require (AB), besides their other analytic hypotheses. These are the dependencies retained, not conclusions established by the combinatorial proof.

**gap.** A hand proof or a genuine counterexample for shellability of every library-good pattern remains open here. More immediately for the restricted route, the adapted-ball handoff (AB) remains open. **unchecked.** The rest of Lemmas 7 and 8, the global tiling existence/estimates, and the analytic/period arguments of the consumers were not audited or re-proved.

