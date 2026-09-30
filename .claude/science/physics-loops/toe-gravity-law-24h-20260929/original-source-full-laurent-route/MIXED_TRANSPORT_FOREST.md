# Complete protected mixed-row transport is a forest

Analytical result under MIXED_COMPATIBILITY_CONTRACT.md. Use the original canceled rotor H2 and physical Gauss phase section, not a surrogate adjacency law. The separately frozen MIXED_ROW_GEOMETRY.md supplies the complete two-term reverse-row classification. The fixed torus has L divisible by four and L>=12. No enumeration or new scientific run is used.

## 1. The exact relation graph

Fix the literal B charge/vacancy pattern chi and the physical W=1 charge sector. A graph vertex is a physical matter configuration in P_+ or P_-, including its hole and all occupied A charges. In a Gauss phase fiber, each configuration has one coordinate; its integer field section is fixed, and the original H entries carry the actual cycle monomials. A graph edge is one ACTUAL mixed outgoing matter row receiving both signs. There are exactly two protected predecessors on this row, by the complete reverse-row theorem. Its row equation is

    t_xy(theta) psi_x + s_xy(theta) psi_y = 0.             (1)

Both coefficients are unit Laurent monomials with nonzero coefficient +1. No arbitrary independently variable edge weight is introduced. Original full G vanishes on the protected inputs, and the mixed output is also G-dark, but this graph describes only the off-support H equations.

Let the source hole be h with polarity sigma. The target hole is c=h+/-4e_i, with polarity -sigma; put a=(h+c)/2 using that length-four axial path. In passing between the two inverse configurations, the exact matter change is

    h: 0 -> sigma;  c: -sigma -> 0;
    a: sigma -> -sigma; all other A charges unchanged;    (2)
    all B charges and vacancies unchanged.

The two actual length-two H paths end at the same output hole a. Their field displacements Delta_x,Delta_y give

    E_y-E_x=Delta_x-Delta_y, ||Delta_x-Delta_y||_1=4.       (3)

The four edges are distinct. Equation (3) states the actual Gauss-consistent inverse transport; in the fiber its phase is precisely the ratio in (1). Reversing the same graph edge reverses (2)-(3) exactly.

## 2. One hole-coordinate class and its physical orientations

Every graph edge preserves the hole coordinate r modulo four, coordinate by coordinate. Fix such a class. Its possible hole positions form a cubic coarse torus of side M=L/4 and have cardinal M^3. Only even-parity r belong to A. Some positions never support a protected word and will be discarded below.

For this FIXED r, an unoriented coarse edge joins h to h+4e_i. Its physical midpoint is h+2e_i. Every such midpoint belongs to exactly one coarse edge. To see this, its residue modulo four is r+2e_i, which identifies the axis i. On that axis the unordered endpoint pair is then midpoint +/-2e_i. At L>=12 these endpoints are distinct; at M=3 the positive and negative neighbors are still distinct. Distinct coarse edges on the same axis have distinct midpoints. Also no midpoint lies in the hole class r.

Define a fixed possible-vertex set from chi: retain h only if its distance-three B neighborhood is full and its immediate B star is uniform of some sign sigma_h. That sign is fixed by chi, independently of A charges. Retain a coarse edge only when both endpoints are possible vertices and their signs are opposite. Call this fixed graph C_(chi,r). It may have cycles; we do NOT assume it is a forest.

For any actual W=1 configuration whose hole lies in r, every midpoint of C_(chi,r) is occupied by an A charge + or -. Orient each edge toward the endpoint whose prescribed sigma equals that midpoint charge. Opposite endpoint signs make this unambiguous. These are physical A charges, not freely assigned auxiliary degrees of freedom.

A protected hole h is a SINK of this oriented graph: every incident midpoint is an A site at distance two from h, so its charge is sigma_h. A legal mixed relation from h to c reverses ONLY the traversed coarse edge. Indeed (2) changes its midpoint charge, while the other changed charges are at h and c, which are never coarse-edge midpoints in this class. The uniqueness of midpoints proves that no other orientation changes. The destination c must again be a sink, because the destination is an actual protected input. Additional A-cone requirements can remove transitions; they do not invalidate these necessary sink rules.

This is the step that fails without the coordinate-class argument: across different r classes a physical midpoint can belong to different axial pairs. Such classes are not connected by any mixed relation here.

## 3. No nonbacktracking return, including actual fields

Consider any sequence of legal mixed relations. Delete an immediate reversal whenever it occurs. By (2)-(3) it restores the COMPLETE prior configuration and field word, so this deletion is exact, not only a deletion in a projected hole path.

A remaining nonbacktracking path cannot repeat a hole position. Suppose otherwise and choose the first repeated hole, giving a segment h_0,h_1,...,h_m=h_0 with m>=3 and distinct intermediate positions. At the first occurrence of h_0 every incident edge points into h_0. In particular the closing edge {h_(m-1),h_0} points into h_0. It has not been traversed in this segment: any earlier traversal would already repeat one of these positions. Only traversal of that same edge can change its orientation. Thus when the path reaches h_(m-1), the closing edge still points AWAY from h_(m-1). This contradicts that the current protected hole must be a sink. The argument also applies to any segment between repeated positions in a longer path.

Consequently every nonbacktracking actual relation path has distinct hole positions and length at most M^3-1. In particular, a relation component contains at most one configuration over each hole position: a path between two different configurations at the same hole could be reduced, and would contradict the preceding argument. Every component is a tree, and the hole projection embeds it as a tree subgraph of C_(chi,r).

There are no multiple relation edges between the same pair of configurations. The complete mixed-row geometry gives the unique axial midpoint and unique inverse field paths. Every closed walk in a component therefore reduces to successive exact reversals. Its net physical field displacement is zero, and its Laurent transport product is one.

This proves a COMPLETE relation-graph forest statement, not just acyclicity of a selected set of rows. It holds for every physical cycle phase. It does not assert that the fixed coarse graph C_(chi,r) is acyclic.

## 4. Exact Laurent kernel and its size

Choose a root in each tree C. Define z_root=1 and propagate along its edges by

    z_y = -t_xy s_xy^(-1) z_x.                           (4)

There is a unique path, so each z_x is a signed unit Laurent monomial. On physical phases |z_x|=1. Equations (1) have the complete solution

    psi_x = z_x(theta) a_C,   x in C.                    (5)

Over the Laurent ring in the TRUE physical cycle variables this kernel is free, of rank the number of components (isolated vertices included). Its row matrix has exact rank |vertices|-|components| at EVERY physical phase. Tree elimination uses only invertible monomials and introduces no exceptional phase or denominator zero. The physical field displacement from root to x has l1 at most 4(M^3-1), before expressing it in a chosen cycle basis; this is a transport bound, not an energy/preparation claim.

Thus the proposed mixed-cycle phase obstruction is absent in this complete relation graph on L divisible by four: every cycle transport is pure gauge because every closed walk is a sequence of actual inverse steps. Arbitrarily assigning independent phases to these edges would obscure, rather than prove, the required observability.

## 5. What remains

Equation (5) solves ONLY mixed-sign outgoing rows. It leaves all one-polarity outgoing rows and the eigenvalue equations on protected input rows. Those can couple different trees and different coordinate classes. A tree leaf is not a uniquely fed H output: several same-polarity protected columns can feed the same remaining row. No leaf-zero or full-rank conclusion follows here.

The exact residual operator and its spectral criterion are stated separately in REDUCED_PROTECTED_MODULE.md. The present theorem proves neither a protected-union eigenvector nor its exclusion, no positive-Haar dark module, and no actual source weight. Unprotected columns, both full Laurent observability and actual projected-history image density remain open.

The restriction L divisible by four is essential to this proof. For L=2 modulo four, step-four hole transport explores a parity class in which distinct axial edges can share a physical midpoint, and a midpoint can itself be a later hole position. The single-edge-reversal orientation argument then does not apply. No extension to that case is asserted.
