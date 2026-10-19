<!-- Original PR9817 source SHA256 2ba0f05755244fc1b51693a1472c82d4afd549e36791bc5404887453666ee418. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Independent order-ten graph completeness check for separation (3,2)

Disposition: PASS for the connected diagonal-word classification and longitudinal assignments, with the normalization and folded-term qualifications below. No numerical coefficient or full scattering theorem is established by this classification alone.

## Shortest-walk proof of completeness

Consider the transverse projection of a connected diagonal ten-insertion word. At each longitudinal layer each site's X/Y flip count must be even, hence its transverse insertion multigraph is Eulerian. Summing layers preserves even transverse degree. For background dependence on the signs at A=(0,0) and B=(3,2), each of these columns must have odd Y insertion count (and thus odd X insertion count). Both are necessarily vertices of the connected graph.

Choose an Euler tour of this connected ten-edge multigraph starting at A and split it at a visit to B. The two resulting A-to-B walks have total length ten. Each has length at least the Manhattan distance five. Equality forces both to have length exactly five and to be monotone shortest paths, using three x steps and two y steps. Thus EVERY graph in question is the union, with multiplicities, of two monotone shortest A-to-B paths. There is no room for a spur, excursion outside the 3 by 2 bounding rectangle, or another disjoint loop in a connected word.

Odd Y degree at A and B means the two paths start in different axes and end in different axes. Conversely these endpoint conditions, together with two shortest paths, give the required endpoint Z-sign dependence. Other corner signs may also be present; the statement is not that the operator contains only Z_A Z_B.

I independently enumerated the ten monotone paths and their unordered pairs in an inline exact integer calculation. Twelve path pairs satisfy the endpoint conditions, but they produce only NINE distinct edge-multiplicity graphs:

* six simple ten-edge cycles;
* two graphs consisting of a six-cycle and a square touching at one vertex;
* one graph consisting of two squares joined by a single doubled bridge edge.

The touching and dumbbell graphs each admit two decompositions into shortest paths. They must be counted once as multigraphs, not twice because of this decomposition multiplicity. This matches the root's count.

## Longitudinal layer assignments

For a simple cycle, every degree-two vertex forces its two incident insertions to occur in the same longitudinal layer, since diagonal return requires even flips separately at each physical spin. This propagates around the entire cycle: it lies in one layer.

For two cycles touching at a vertex, all degree-two vertices force each individual cycle into one layer. At the shared vertex both cycles already supply an even number of flips, so their layers need not coincide. The native H0 vertical bonds connect their virtual flip energies only if their layers are equal or adjacent. At greater longitudinal separation the energy/cumulant factorizes and the connected energy contribution, including folds, vanishes. With the first cycle at z=0 the connected assignments are z_second=0,+1,-1.

For the dumbbell, each square is likewise confined to one layer. Both occurrences of the bridge must be in the SAME layer. At its endpoints the square contributes either zero or two flips in any layer, so bridge occurrences in two different layers would each leave odd physical flip parity and cannot be a diagonal word. The bridge layer must be equal or adjacent to each square's layer for a connected contribution. With the first square fixed at zero:

    z_bridge in {-1,0,+1},
    z_second in {z_bridge-1,z_bridge,z_bridge+1}.

This gives nine relative assignments, including second-square displacement plus/minus two when the bridge occupies the intermediate layer. This latter case must not be dropped. On the fixed L=10 longitudinal circle these local assignments do not alias; summing the first-square layer gives the usual factor L.

The longitudinal interaction test is about connected virtual energy costs, not simply overlap of operator supports. Distant layers in a common column can share spectator spins in the H0 description, yet their flip-energy variables factor when no vertical bond joins the flipped layers. Their disconnected pieces cancel in the energy cumulant.

## Multiplicity, folds, and completeness limits

The bridge appears twice. If the numerical algorithm labels its two insertions as distinct and sums all labeled orderings, divide the squarefree labeled coefficient by 2! when identifying the labels as the same native coupling. This division must be applied consistently to the complete perturbation coefficient, including normalization/fold terms, not only to the raw resolvent chain. An algorithm that already sums unlabeled multiset words must NOT divide again.

The simple cycles have no proper nonempty diagonal return and permit the primitive-loop formula. The touching and dumbbell graphs do have proper projected returns and require connected subtraction/canonical folded terms. Their contributions cannot be obtained just by multiplying primitive cycle coefficients or by applying the degree-two frequency product at a degree-four repeated site.

The argument excludes all OTHER connected diagonal insertion graphs of total length ten that depend on both specified background signs, in the nonwrapped transverse geometry. Repeated-edge decorations of a smaller connected graph cannot evade the distance bound: any such decorated ten-edge graph is already one of the two-shortest-path unions above. Contributions that do not depend on both A and B cancel from the connected two-column interaction. Disconnected transverse supports cannot be linked by H0 unless they share a column, which would already make the transverse graph connected.

This does not classify all offdiagonal N0 processes at order ten (height-ten winding is a distinct native channel), nor does it replace subsequent state mixing and scattering analysis. It establishes the candidate list for the diagonal connected background coefficient only. Transverse periods must be large enough that periodic shorter paths or wraps do not change the distance bound.
