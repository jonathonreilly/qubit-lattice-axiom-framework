---
claim_id: su2_finite_boundary_flux_associative_gluing_bounded_theorem_note_2026_11_07
claim_type: bounded_theorem
claim_scope: For the explicitly supplied five-state SU(2) link model, link subdivision is an exact coassociative isometry onto the new-vertex singlet sector, intertwines compressed transporters, and preserves a once-counted electric term. Edge-disjoint regions with retained boundary representations reconstruct the same finite gauge sector under every grouping when only newly internal constraints are imposed. A four-plaquette square gives an exact nonzero-boundary-flux and intertwiner-multiplicity test. Native homogeneous qubit allocation, spatially covariant nearest-neighbor dynamics, Admissibility/Record realization, state selection and continuum physics remain open.
upstream_dependencies: []
runner: scripts/gb1_cf_boundary_gluing_exact_2026_11_07.py
actual_current_surface_status: candidate-retained-grade
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: Include boundary flux and glue neighboring finite-register gauge patches consistently within the current lattice axioms (GB1-CF).
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: Construct a homogeneous native qubit allocation and compatible spatially covariant update/readout law on the glued observable system.
conditional_surface_status: All results assume the explicit five-state link, tensor composition, graph, group action, Gauss constraints and operator definitions below.
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: Finite-dimensional exact gluing and operator theorem with an independently checked boundary-sector example.
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Boundary flux and associative gluing at fixed link-register size

**Type:** bounded_theorem
**Status:** proposed_retained

This is an author proposal for a supplied finite gauge-model theorem, pending
independent landing review and audit. No lattice axiom is changed, and the
result does not yet implement the full native lattice law.

## Model and statement

On each oriented edge use normalized Haar measure on SU(2), write
\(g=x_4I+i\sum_{a=1}^3x_a\sigma_a\), and retain

\[
R=\operatorname{span}\{1,2x_1,2x_2,2x_3,2x_4\}
  \cong (0,0)\oplus(\tfrac12,\tfrac12).
\]

The endpoint representation includes duals in the natural oriented notation.
Let \(P\) be this Haar-space projection. Define the color-matrix operator
\(U=PM_gP=P_4I+iP_a\sigma_a\), with
\(P_\mu=(|\mu\rangle\langle0|+|0\rangle\langle\mu|)/2\),
and \(E^2=\tfrac34\sum_{\mu=1}^4|\mu\rangle\langle\mu|\).
The link matrix is not a unitary rotor coordinate. It transforms exactly as
\(U_{xy}\mapsto h_yU_{xy}h_x^{-1}\). Products along a path use reverse
traversal order; a reversed link uses \(U^\dagger\).

**Theorem.** This link model admits exact associative cutting and reconstruction
with boundary flux retained. The reconstructed transporter is the product of
segment transporters; the original electric contribution must be counted once.
For any finite graph, grouping disjoint edge regions and imposing Gauss law
only at vertices that have become internal reconstructs the same Hilbert
subspace and the same compatible operators, independent of grouping.

The graph, SU(2) action, five-state representation, tensor composition,
Gauss constraint and chosen operators are explicit conditions of the theorem.
They are not selected by the four physical axioms.

## 1. Cutting a link without deleting boundary flux

Subdivide \(x\to y\) into \(x\to z\to y\), with group variables
\(g_1,g_2\). Define

\[
(Sf)(g_1,g_2)=f(g_2g_1).
\]

Haar invariance gives \(\|Sf\|^2=\|f\|^2\). For the normalized
matrix-coefficient basis \(\phi^j_{mn}=\sqrt{d_j}D^j_{mn}\),

\[
S\phi^j_{mn}
=\frac1{\sqrt{d_j}}\sum_{k=1}^{d_j}
  \phi^j_{kn}(g_1)\phi^j_{mk}(g_2),\qquad d_j=2j+1.
\]

The same label \(j\) occurs on both segments. Hence the retained set
\(j\in\{0,\tfrac12\}\) is exactly closed under this cutting map:
\(S:R\to R\otimes R\). Each new segment still has five states.
The total auxiliary space has dimension 25, while the image has dimension 5.
This is a constrained embedding, not two independent copies of a quantum link.

At the new vertex, \(g_1\mapsto h_zg_1\) and
\(g_2\mapsto g_2h_z^{-1}\). Thus \(S(R)\) is invariant there.
Conversely, the internal endpoint factors \(V_{j_1}\) and \(V_{j_2}^*\)
have an invariant precisely when \(j_1=j_2\), with multiplicity one.
Their two remaining endpoint indices give \(d_j^2\) states. Therefore

\[
\operatorname{Inv}_z(R\otimes R)=S(R),\qquad
\dim\operatorname{Inv}_z(R\otimes R)=1+4=5.
\]

This proves completeness of the constrained image, not merely the existence
of five invariant vectors. Repeating the cut in either order gives
\(f(g_3g_2g_1)\). The maps are coassociative and isometric.

In the real coordinate basis, with tensor factors ordered as segment 1 then 2,

\[
S|0\rangle=|00\rangle,\qquad
S|4\rangle=\tfrac12(|44\rangle-|11\rangle-|22\rangle-|33\rangle),
\]
\[
S|a\rangle=\tfrac12\left(|a4\rangle+|4a\rangle+
\sum_{b,c=1}^3\epsilon_{abc}|bc\rangle\right),\quad a=1,2,3.
\]

These follow directly from \((i\sigma_b)(i\sigma_c)
=-\delta_{bc}I-\epsilon_{bca}i\sigma_a\) and the stated path order.

## 2. Transporters and electric accounting across a cut

Extend \(S\) to the full Haar space and put \(Q=P\otimes P\).
The representation formula above proves \(QS=SP\): cutting preserves the
representation label on both segments, including labels outside the cutoff.
Because the two segment projectors act on different links,

\[
U_2U_1=Q M_{g_2g_1}Q.
\]

Also \(M_{g_2g_1}S=SM_g\). On the retained coarse space this gives

\[
(U_2U_1)S=Q M_{g_2g_1}S=QS M_g=SPM_g=S U.
\]

Repeating the same multiplication argument with \(M_g^\dagger\) proves
\((U_2U_1)^\dagger S=SU^\dagger\). Consequently the cut image is preserved
by the reconstructed transporter and its adjoint. Any word formed from these
specified operators, including plaquette traces with a subdivided edge,
intertwines the corresponding original word. This is stronger than checking
only the projected equality \(S^*(U_2U_1)S=U\).

For the electric terms, the common label instead gives

\[
E_1^2S=E_2^2S=SE^2,\qquad
(E_1^2+E_2^2)S=2SE^2.
\]

Thus representing one original electric term on the cut link requires
\(\lambda_1E_1^2+\lambda_2E_2^2\) with
\(\lambda_1+\lambda_2=1\); an equal split uses one half on each segment.
This is accounting for the original operator. Adding an electric contribution
for each new segment without adjustment defines a different Hamiltonian.
The same rule extends to repeated subdivisions by preserving total weight one.

The artificial cut vertex and its auxiliary factors are representation devices.
This statement does not add physical sites to the framework's supplied lattice.

## 3. Regional gluing and the order of constraints

Fix a finite graph \(\Gamma=(V,E)\) and a set \(V_0\subseteq V\) of
vertices where Gauss law is to hold. Taking \(V_0=V\) closes the graph;
omitting its outer boundary retains flux into an environment.
For an edge region \(A\subseteq E\), let

\[
I(A)=\{v\in V_0:\operatorname{star}_\Gamma(v)\subseteq A\}.
\]

On \(\bigotimes_{e\in A}R_e\), project only the vertices in \(I(A)\).
Call the resulting space \(\mathcal H_A^{\rm ext}\). The other incident
vertices carry unprojected boundary group representations. At an isolated
vertex the projector is trivial, so its assignment makes no difference.

For disjoint edge sets \(A,B\), their tensor factors regroup exactly into
the edge space of \(A\cup B\). Apply the Gauss projectors at
\(I(A\cup B)\setminus(I(A)\cup I(B))\) to obtain
\(\mathcal H_{A\cup B}^{\rm ext}\). Distinct vertex group actions commute:
they act on separate factors or on the commuting left and right actions of a
shared link. Their Haar projectors therefore commute and are idempotent.

Every grouping of a finite regional partition applies exactly the same final
projectors to the same underlying edge tensor product. This proves associative
reconstruction as a subspace identity. At an interface that still touches a
third region, the full star is not yet present: its representations must be
combined and retained, rather than projected to spin zero. Associativity here
includes that boundary convention; it does not validate premature projections.

A concrete three-region example has one half-spin end from A, one from B,
and two from C at a shared vertex. The four ends have two singlets. Projecting
the A/B pair to a singlet first leaves only one. In the four-end bit basis,

\[
|t\rangle=|0011\rangle+|1100\rangle-\tfrac12(
|0101\rangle+|0110\rangle+|1001\rangle+|1010\rangle)
\]

has norm squared 3 and total spin zero, but its first pair is a triplet,
so the premature A/B singlet projection annihilates it. This is an explicit
lost valid state for the specified projection shortcut.

For a final two-region interface, include in its product group only those
interface vertices at which Gauss law must now be imposed. Any remaining
unconstrained outer-boundary degrees of freedom stay in the multiplicity
spaces below. Decompose the two regional spaces as

\[
\mathcal H_A^{\rm ext}=\bigoplus_{\mathbf j}
 M_A(\mathbf j)\otimes V_{\mathbf j},\qquad
\mathcal H_B^{\rm ext}=\bigoplus_{\mathbf j}
 M_B(\mathbf j)\otimes V_{\mathbf j}^*.
\]

At each interface vertex contract equal representations using the normalized
invariant vector. This gives

\[
\mathcal H_{A\cup B}^{\rm ext}
\cong\bigoplus_{\mathbf j}M_A(\mathbf j)\otimes M_B(\mathbf j),
\qquad
\dim\mathcal H_{A\cup B}^{\rm ext}
=\sum_{\mathbf j}m_A(\mathbf j)m_B(\mathbf j).
\]

Dual labels are essential for a general group; for SU(2) each irrep is
self-dual, with the appropriate dual-space identification understood.
There is no additional factor \(d_{\mathbf j}\) in the final singlet count.
All representation and multiplicity spaces remain finite. On a cubic graph
there are at most six incident half-spin ends, so no local combined spin
exceeds 3; retaining those boundary combinations does not enlarge the link
register beyond its original five states.

## 4. Four-plaquette test with nonzero interface flux

Take vertices \((x,y)\), \(x,y\in\{0,1,2\}\), and the 12 nearest-neighbor
edges oriented in positive coordinate directions. For this first test impose
Gauss law at every vertex and divide the edges as follows:

- Region A owns the four vertical edges at \(x=0,1\) and the three
  horizontal edges from \(x=0\) to \(x=1\).
- Region B owns the two vertical edges at \(x=2\) and the three
  horizontal edges from \(x=1\) to \(x=2\).

The interface is \((1,0),(1,1),(1,2)\). Let \(x,y,z\) now denote the
fundamental SU(2) characters at these three vertices. The five-edge outside
tree has one empty configuration and three paths pairing interface ends, so

\[
\chi_B=T=1+xy+yz+xz,\qquad
\chi_A=T(1+xy)(1+yz).
\]

The last two factors are the two middle vertical links. Evaluating all
characters at identity gives \(\dim\mathcal H_B^{\rm ext}=13\) and
\(\dim\mathcal H_A^{\rm ext}=325\). Using
\(\chi_{1/2}^2=\chi_0+\chi_1\) and
\(\chi_{1/2}^3=2\chi_{1/2}+\chi_{3/2}\), the matching sectors are

| Interface label \((2j_0,2j_1,2j_2)\) | \(m_A\) | \(m_B\) | Singlets |
|---|---:|---:|---:|
| \((0,0,0)\) | 4 | 1 | 4 |
| \((1,1,0)\) | 5 | 1 | 5 |
| \((0,1,1)\) | 5 | 1 | 5 |
| \((1,0,1)\) | 4 | 1 | 4 |

The glued singlet dimension is therefore **18**. Setting each region's
interface flux to zero would retain only the first four states.

There is a direct full-graph check. The binary cycle space has dimension
\(12-9+1=4\), giving 16 even occupied-edge patterns. All vertices except
the center have occupied degree at most three, with one singlet for degree
zero or two. Two alternating plaquette-bit patterns give occupied degree four
at the center. Four spin halves have two singlets, from coupling either two
spin-zero pairs or two spin-one pairs to total zero. Thus

\[
\dim\mathcal H_\Gamma^{\rm inv}=14+2\cdot2=18.
\]

Counting only one state per even subgraph would instead give 16. The missing
two states are intertwiner multiplicity, distinct from the 14 states lost by
discarding all nonzero interface representations. These are errors in the
specified counting shortcuts, not universal obstructions to other methods.

The three-piece grouping, with the middle vertical chain separated from the
two outside trees, has the same product character \(T^2(1+xy)(1+yz)\).
At each interface vertex, combine all incident factors before final singlet
projection. This gives the same count and is an explicit instance of section 3.

For an actually open outer boundary, impose Gauss law only at \((1,1)\).
Among its four incident links, \(n\) occupied ones contribute \(n\) half-spin
ends at the center and \(2^n\) unconstrained endpoint states outside it.
The center singlet rank is

\[
\sum_{n\text{ even}}\binom4n\,m_0(n)\,2^n=1+24+32=57.
\]

The other eight links are unconstrained, giving
\(\dim\mathcal H_\Gamma^{\rm ext}=57\cdot5^8=22{,}265{,}625\).
This large but finite space is counted by representation theory; no dense
matrix of that size is needed or claimed to have been constructed.

## 5. What operators and dynamics glue

A regional operator commuting with the constraints being imposed preserves
their common invariant subspace, so its restriction is well defined after
gluing. At a vertex where Gauss law is being imposed, a boundary-charged
operator needs its matching boundary action from the other region; it is not
automatically a standalone physical observable. Unconstrained outer-boundary
actions need no such matching.
Section 2 proves this matching explicitly for transporters across a cut.

For genuinely overlapping plaquette patches, a common physical edge is one
tensor factor in \(\bigotimes_{e\in A\cup B}R_e\). Each patch algebra embeds
by identities on the other edges and uses exactly the same operator on the
intersection. This establishes compatible local descriptions without treating
the overlap as independent quantum copies. It does not imply commutation of
overlapping plaquette operators.

With each physical plaquette and electric term counted once, a finite global
generator made from their sum is independent of how the edge set was divided
for calculation. Gauge invariance follows from the closed-loop contractions
and the Casimirs. Equal coefficients on geometric symmetry orbits give
covariance under those graph symmetries, and the global exponential inherits it.
The word "global" matters: this does not provide a fixed-depth nearest-neighbor
schedule, nor identify separately ordered products of patch exponentials.

## 6. Relation to the current lattice axioms

Each five-state link embeds in three qubits on an initialized five-word code;
extend its operators by zero on the unused words and its gauge action trivially.
The resulting code is preserved by the specified generators. Boundary gluing
requires representation matching and all invariant multiplicities, but no
infinite link register. The unused code words are not removed by gauge
invariance alone. The cuts above are algebraic devices, not a homogeneous
physical allocation of those qubits on \(\mathbb Z^3\).

The construction establishes finite boundary/gluing consistency for the
supplied gauge model. It leaves these physical obligations open:

- one native qubit/observable allocation compatible with translations and
  proper cubic rotations;
- a compatible local update with the required nearest-neighbor structure;
- the fixed local probability law, record formation, permanence and
  content-only readout required by Admissibility and Record;
- state, clock, physical coupling and Euclidean/continuum identifications.

In particular, Admissibility is not a supplied Hamiltonian axiom. Selecting
the generator above does not derive a record law. No new axiom, physical
vacuum, continuum Yang-Mills construction or mass gap follows here.

## Evidence and provenance

The [primary runner](../scripts/gb1_cf_boundary_gluing_exact_2026_11_07.py) uses
exact coordinate matrices for the cut and operator identities. The separately
authored [checker](../scripts/gb1_cf_boundary_fusion_check_2026_11_07.py) uses
normalized representation coefficients, occupancy/fusion, and independent
Laurent-character counts. The supervisor's analytic derivation was recorded
before comparing their results. The derived matrices, counts and normalization
conditions agree. Shared model family and raw premises remain independence
limitations; no audit grade follows from successful assertions.

The primary imports and invokes the checker only after both original
derivations were frozen. Its explicit cache-input declaration includes that
helper. Both final runners executed through the repository's content-bound
cache API. Local mutations reject incorrect cut normalization, reversed
transporter order and unweighted electric accounting. The graph checker's
three separately invoked faults reject premature zero-flux projection,
discarded intertwiner multiplicity and a missing intermediate spin-one channel.

The [research handoff](../.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/HANDOFF.md)
records precise source identities, full execution and mutation evidence,
source-review coverage and recovery. The original resource-limit launch
failure is preserved; successful final runs used the supported monitored
memory protection. The canonical caches are the
[combined certificate](../logs/runner-cache/gb1_cf_boundary_gluing_exact_2026_11_07.txt)
and [independent certificate](../logs/runner-cache/gb1_cf_boundary_fusion_check_2026_11_07.txt).
Formal landing review and audit remain separate obligations. The negative
examples here are explicit witnesses for specified shortcuts; they do not
exclude other encodings, schedules or physical laws.

The boundary-state and link-splitting machinery is established in Donnelly,
[Decomposition of entanglement entropy in lattice gauge theory](https://arxiv.org/abs/1109.0036),
section II, equations (8)-(14). The finite-cutoff closure, compressed-operator
intertwining and the displayed graph counts are derived here for the explicit
model, without a literature-priority claim or an imported continuum result.

The previous two-plaquette note and assembly PR #10139 motivate GB1-CF. No
unmerged external theorem or mutable planning document is a mathematical
runtime input to this construction. Existing physical axioms and authority
files remain unchanged.
