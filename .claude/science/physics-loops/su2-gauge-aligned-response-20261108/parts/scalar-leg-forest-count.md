# Scalar-leg rooted Gaussian tree summation

Author proof, 2026-11-09; independent check pending. This is an abstract
positive tree-majorant lemma for bounded primitives. It does not prove an
actual model, connected-log expansion, density-jet estimate, parity rule,
translation estimate or density-reader marking estimate. Its only analytic
input is the all-order integrated density-jet majorant explicitly assumed
below. The proof derives its combinatorics directly; no historical tree
factorial assertion is imported. Only this file is written; no Git, network
or numerical action is used.

## 1. Exact hypotheses and the additional rate reserve

Let Λ be a finite cell set. At most k≥1 scalar coordinates are owned by
each cell, with owner map o(i). A primitive type B has a NONEMPTY finite
connected cell support S_B, active scalar set I_B⊂{i:o(i)∈S_B}, and weight
w_B≥0. Thus |I_B|≤k|S_B|. Primitive labels may contain additional discrete
data; all such labels are included in the sums. Types with empty active set
are allowed, but empty S_B is excluded because the anchored hypothesis
would not control them. In applications a field-independent primitive must
retain its nonempty declared reader support.

Fix β>2δ>0 and suppose the supplied primitive norm is

    sup_(x∈Λ) Σ_(B:x∈S_B) exp[(β−δ)|S_B|] w_B≤h.       (T1)

For each ordered scalar pair i,j let nonnegative path-labeled weights
ε_(ij,P) be given, with P a cell path containing o(i),o(j). Covariance
symmetry is represented by a reversal involution
ε_(ij,P)=ε_(ji,P^rev), preserving the path's cell set. Set

    e_ij=Σ_P exp(β|P|) ε_(ij,P),
    sup_i Σ_j e_ij≤e,
    B_E=sup_x Σ_(i,j,P:x∈P) exp(β|P|) ε_(ij,P)<∞.      (T2)

Here |P| is the number of its declared reader cells; repeated visits can be
retained as a larger length if desired, provided all geometric inequalities
use the same upper count. B_E counts ORDERED scalar pairs. No factor L² is
included in e or B_E. Paths are additional labels summed independently on
each tree edge. The symmetry is only needed for the unoriented edge-cut
identity; rooted estimates use the row bound alone.

Put L≥0 and y=L²eh. Assume BOTH

    y≤1/2,       4ky≤δ.                                (T3)

The second condition alone does not imply the first for arbitrary δ. A
small-rate convention such as δ≤1 ensures it, but (T3) is the exact stated
hypothesis here. The input rate β−δ in (T1) supplies one more size reserve:
the OUTPUT rate is ν=β−2δ>0, not β−δ. Define

    a_B=exp(ν|S_B|)w_B,
    sup_x Σ_(B:x∈S_B) exp(δ|S_B|) a_B≤h.              (T4)

For a labeled tree T and scalar endpoint choices i_(v,e)∈I_(B_v), let
m_(v,i) be the number of tree edges incident to v that use scalar i there.
The assumed integrated all-order density bound is precisely

    L^(2|E(T)|) Π_(v,i) sqrt(m_(v,i)!) Π_v w_(B_v),    (T5)

times the edge path/covariance weights. No additional vertex factorial or
hidden scalar-count factor is assumed or inserted. The majorant below is
the sum obtained after weighting the output support at rate ν and replacing
each path weight by its larger rate-β weight. Orientation toward a root
leaves each nonroot vertex exactly ONE incoming scalar leg. Coincident
scalar endpoints at a vertex are allowed and counted by m_(v,i).

## 2. Rooted coefficients, including their exact factorials

Use finite labeled trees on vertices {1,...,n}; the single-vertex tree is
included. Fix the root to vertex 1 and its primitive type to B. Define
F_B^0 as the following nonnegative formal sum:

    F_B^0 = Σ_(n≥1) 1/(n−1)! Σ_(B_2,...,B_n)
       Σ_(trees T on {1,...,n}) Σ_(scalar endpoints)
       [Π_v a_(B_v)] [Π_(edges {v,w}) L² e_(i_(v,e),i_(w,e))]
       [Π_(v,i) sqrt(m_(v,i)!)],                       (T6)

where B_1=B. For i∈I_B define F_B^i by the SAME formula except that the
root factor sqrt(m_(1,i)!) is replaced by sqrt((m_(1,i)+1)!). This is a
root with one dangling incoming scalar leg at i. That dangling leg has
no covariance weight and no factor L; its future joining edge will supply
L². All other factorials and all internal edges are unchanged.

The sums can be defined as monotone limits over bounded tree depth, finite
type lists and finite path lists, so convergence need not be assumed.
Repeated primitive types are allowed in these FORMAL sums. They are a
relaxation of exclusions for an upper bound, not an interpretation as
actual repeated moments or as independent primitive insertions.

The normalization 1/(n−1)! is the correct marked-root version of 1/n!:
marking a vertex in an n-labeled unrooted tree gives n equivalent choices,
and permutation symmetry moves the marked vertex to label 1. Thus summing
F_B^0 over B with x∈S_B is exactly the unrooted 1/n! sum with one marked
vertex whose support contains x, before applying bounds. Similarly summing
F_B^i over B containing the externally specified scalar i is the marked
incoming-leg rooted sum.

To spell out the unordered-child coefficient, orient each rooted tree away
from its root. If the root has r children with subtree sizes n_1,...,n_r,
the exponential generating coefficient gives 1/r! for an ORDERED list of
r child trees. After specifying that list, partitioning the n−1 nonroot
labels into its ordered sizes contributes (n−1)!/Π n_l!, and choosing the
root of each child subtree contributes Π n_l. Combined with the prefactor
1/(n−1)!, this is

    (1/r!) Π_(l=1)^r 1/(n_l−1)!.                      (T7)

The 1/r! removes child order, including repeated formal types through their
usual exponential coefficients. There is no separate unspecified “tree
factorial.” Equation (T7) is also valid for r=0 by the empty-product rule.

## 3. Scalar occupancy generating functions and supersolution

Let

    A_j=Σ_(B:j∈I_B)F_B^j,
    z_i=L² Σ_j e_ij A_j.                              (T8)

The child incoming leg is counted by F_B^j, so its factorial includes the
joining edge once. At the parent, if r_i children choose outgoing scalar i,
then the root factorial is sqrt(r_i!) (ordinary root), or sqrt((r_i+1)!)
at its single incoming scalar (incoming root). Regrouping the ordered
children of (T7) by scalar gives the multinomial coefficient
r!/Π_i r_i!, canceling 1/r!. Thus the EXACT recursions are

    F_B^0=a_B Π_(i∈I_B) H0(z_i),
    F_B^i=a_B H1(z_i) Π_(p∈I_B,p≠i) H0(z_p),           (T9)

where

    H0(z)=Σ_(r≥0) z^r/sqrt(r!),
    H1(z)=Σ_(r≥0) sqrt((r+1)!) z^r/r!.                 (T10)

These are identities of nonnegative formal tree series. For an empty active
set, the first recursion is F_B^0=a_B and there is no incoming-root version.
A vertex never needs two incoming-leg factors, because the graph is a tree
with a single root; all its other legs are outgoing children.

For 0≤z≤1/2 the required elementary bounds are

    H0(z)≤exp(2z),       H1(z)≤exp(4z).                (T11)

Proof: both series are entire by the ratio test. Since sqrt(r+1)≤1+r/2,
termwise differentiation yields H0'≤H0+(z/2)H0', so
H0'/H0≤1/(1−z/2)≤2 on this interval. Since H0(0)=1, integration proves
the first bound. Writing b_r=sqrt((r+1)!)/r!, one has
(r+1)b_(r+1)=sqrt(r+2)b_r. The inequality sqrt(r+2)≤2+r/2 therefore gives
H1'≤2H1+(z/2)H1', and H1'/H1≤2/(1−z/2)≤4.
With H1(0)=1, integration proves the second bound. This establishes the
bounds directly, rather than an incorrect termwise factorial domination.

Use the common supersolution

    Fbar_B=a_B exp(δ|S_B|)                            (T12)

for BOTH ordinary and every incoming-root version. If F_B^j≤Fbar_B, then
by ownership and (T4), A_j≤Σ_(B:o(j)∈S_B)Fbar_B≤h. Hence z_i≤L²eh=y.
For an ordinary root, (T11) bounds its multiplier by exp(2|I_B|y).
For a root with incoming scalar i it bounds it by

    exp[4z_i+2Σ_(p≠i)z_p]≤exp[4|I_B|y]
                           ≤exp[4k|S_B|y]≤exp[δ|S_B|]. (T13)

Thus (T9) maps the common supersolution into itself under (T3).
Starting with depth-zero single vertices F_B^0=F_B^i=a_B, iterate the
finite-depth recursions. Positivity, (T12) and monotone convergence show
that the full formal sums converge and obey

    F_B^0≤Fbar_B,  F_B^i≤Fbar_B,
    sup_x Σ_(B:x∈S_B)F_B^0≤h,
    sup_i Σ_(B:i∈I_B)F_B^i≤h.                          (T14)

This is uniform in support size, active scalar count, volume and primitive
multiplicity; every |I_B| factor has been paid by the explicit δ|S_B|
reserve. No bound on |S_B| independent of B is required.

## 4. Root on a marked covariance path: exact edge-cut coefficient

For a cell x define the ordered endpoint matrix

    p_ij(x)=Σ_(P:x∈P) exp(β|P|) ε_(ij,P),
    Σ_(i,j)p_ij(x)≤B_E.                               (T15)

Consider the UNROOTED labeled tree sum with coefficient 1/n!, n≥2, with
one tree edge marked and its path constrained to contain x. All other edges
are summed with e_ij. Count the marked edge once as an UNORIENTED edge.
Cutting it gives two rooted trees, each with one incoming scalar leg at
the cut endpoint. Conversely two such rooted trees and the marked path
reconstruct the original marked-edge tree. The exact positive majorant
identity is

    EdgeRoot(x)=(L²/2) Σ_(i,j) p_ij(x) A_i A_j.         (T16)

The factor 1/2 is essential for this convention: ordered pairs of rooted
halves orient the cut edge and count its two orientations. For clarity,
if the halves have p,q≥1 vertices, p+q=n, distributing the n labels into
an ordered pair of sets gives n!/(p!q!), and choosing their two root labels
gives pq. Dividing by n! and by two gives exactly

    1/[2(p−1)!(q−1)!],                                (T17)

the product of the coefficients in (T6), times 1/2. This derivation also
covers identical formal component types, coincident scalar endpoints and
equal-looking rooted halves: labeled vertices are still distinct before
division. The reversal symmetry in (T2) identifies the two orientations
without changing their weights.

The density factorial at each cut endpoint is correct because its incoming
root factor already includes the removed leg. No additional sqrt factorial,
scalar count or L is needed; the joining edge contributes its single L².
By (T14)–(T15),

    EdgeRoot(x)≤(L²/2)B_E h²≤L² B_E h².                (T18)

If instead the marked edge is defined to carry an ORIENTATION, its exact
coefficient lacks 1/2 and its bound is L²B_Eh². Thus the requested latter
bound is valid under either convention, with the convention now explicit.
There is no unaccounted n or number-of-edges factor: summing the marked
edge choices on the original side is exactly what the cut identity counts.

## 5. Geometric-root consequence at the stated output rate

For a fully path-labeled tree let

    U=union_v S_(B_v) union union_edges P_e

be its complete declared cell support. It is connected, because primitive
supports are connected and every edge path joins its selected endpoint
owners. Nonnegative ν=β−2δ gives

    exp(ν|U|)≤Π_v exp(ν|S_(B_v)|) Π_edges exp(ν|P_e|)
              ≤Π_v exp(ν|S_(B_v)|) Π_edges exp(β|P_e|). (T19)

If x∈U, then x lies in at least one primitive support or at least one edge
path. Bound this indicator by the sum of those marked incidences. With the
original unrooted 1/n! coefficient, the primitive-support part is exactly
controlled by the vertex-root sum in (T14), and the path part by (T18).
Therefore the full geometric-root majorant satisfies

    sup_x Σ_(unrooted trees, paths; x∈U)
              (1/n!) exp(ν|U|) [original nonnegative tree weight]
        ≤ h+(L²/2)B_Eh²
        ≤ h+L²B_Eh².                                  (T20)

“Original tree weight” here means exactly Π_v w_(B_v), the path weights
Π_e ε_(i_ej_e,P_e), and the assumed jet factor (T5), summed over all labeled
primitive assignments and scalar endpoints as in (T6). Repeated types and
incompatibilities may be relaxed only for this positive upper bound. If an
actual application has a smaller admissible collection, termwise domination
by the formal sum is legitimate; (T20) asserts no existence of moments for
relaxed duplicate insertions.

## 6. Scope and checks required of a consumer

The lemma proves the rooted and incoming-leg sums with the precise
unordered-child 1/r! coefficients, plus the full marked-path-root bound.
The operative conditions are y=L²eh≤1/2 and 4ky≤δ, with an input primitive
norm at β−δ and output rate β−2δ. A suggested small choice
δ=min(β/8,1/8) satisfies β>2δ and keeps the rate reserve explicit; it does
not replace checking y. The coefficient H1 is a single incoming leg, not a
parity repair or a multi-root estimate.

A consumer must separately supply (T1), (T2), and the all-order integrated
jet inequality (T5) with its EXACT L and factorials, and verify that its
labeled tree expansion really has coefficient 1/n!. Nothing here proves
those inputs for a covariance interpolation, a density forest, or a compact
model. In particular there are no translation or density-reader marks and
no source derivative estimates. The input support must include the full
native reader; support connectedness cannot be restored by silently adding
unpriced cells. Independent checking of this combinatorial proof remains
pending; no full-log or physical-response theorem is inferred.
