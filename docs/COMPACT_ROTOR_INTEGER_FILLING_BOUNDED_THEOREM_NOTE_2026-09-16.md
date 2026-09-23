---
claim_id: compact_rotor_integer_filling_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/compact_rotor_integer_filling_check_2026_09_16.py
upstream_dependencies: ["compact_rotor_convex_carrier_bounded_theorem_note_2026-09-16", "compact_rotor_sampled_magnetic_event_bounded_theorem_note_2026-09-16", "compact_rotor_magnetic_excursion_bounded_theorem_note_2026-09-16", "compact_rotor_spatial_ground_path_limit_bounded_theorem_note_2026-09-16", "compact_rotor_temporal_oscillation_coarse_current_bounded_theorem_note_2026-09-16"]
claim_scope: "Conditional finite-set probability premise implies locally finite integer fillings, exponential enlarged-box tail and a real lift on contractible Z4; Hamiltonian application uses the full linked path law."
---

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

Load-bearing mathematical sources: [Compact Rotor Convex Carrier Bounded Theorem Note 2026-09-16](COMPACT_ROTOR_CONVEX_CARRIER_BOUNDED_THEOREM_NOTE_2026-09-16.md), [Compact Rotor Sampled Magnetic Event Bounded Theorem Note 2026-09-16](COMPACT_ROTOR_SAMPLED_MAGNETIC_EVENT_BOUNDED_THEOREM_NOTE_2026-09-16.md), [Compact Rotor Magnetic Excursion Bounded Theorem Note 2026-09-16](COMPACT_ROTOR_MAGNETIC_EXCURSION_BOUNDED_THEOREM_NOTE_2026-09-16.md), [Compact Rotor Spatial Ground Path Limit Bounded Theorem Note 2026-09-16](COMPACT_ROTOR_SPATIAL_GROUND_PATH_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-16.md), [Compact Rotor Temporal Oscillation Coarse Current Bounded Theorem Note 2026-09-16](COMPACT_ROTOR_TEMPORAL_OSCILLATION_COARSE_CURRENT_BOUNDED_THEOREM_NOTE_2026-09-16.md).

# Conditional sparse integer fillings and a real lift in four dimensions

Conditional finite-set probability premise implies locally finite integer fillings, exponential enlarged-box tail and a real lift on contractible Z4; Hamiltonian application uses the full linked path law.

## 1. Explicit probability premise

Index dual vertices by Z^4, and join vertices at Chebyshev distance1. The
resulting adjacency degree is D=3^4-1=80. Let B be a random set of bad
vertices satisfying, for a fixed0<=p<=1, the finite-set bound

    P(A subset B)<=p^|A| for every finite A subset Z^4.       (1)

No independence or stochastic domination is assumed. In particular, (1)
by itself is not asserted to imply Bernoulli domination for all increasing
events. All probability estimates below use only unions and specified
intersections of bad-vertex events.

Let j be an integer current on the nearest-neighbor dual edges. Assume
its divergence is zero, |j_e|<=3, and every edge where j_e is nonzero has
both endpoints in B. Current and bad set may be arbitrarily dependent.
For s>=1 set

    a_s=D^(2s-2) p^s,   w(s)=(s+1)^4,  K=4096,
    Lambda(c)=K sum_(s>=1) w(s)^2 a_s exp(c s).             (2)

Assume Lambda(c)<1 for some c>0. In particular D^2 p exp(c)<1. Then
there is a locally finite integral dual2-chain Q with boundary Q=j.
It can be supported in a union of finite enlarged boxes, whose connected
components have the bound

    P(the union component meeting0 reaches distanceR)
         <=[Lambda(c)/(1-Lambda(c))] exp(-c R/2).           (3)

Distance is Chebyshev distance in the dual coordinates. If the origin
is not in the union, the event is empty. Boxes are regarded as closed
subsets of R^4; their enlargement by1 is part of the construction.

## 2. Finite bad components and local fillings

A connected set of s vertices containing a specified vertex has at most
D^(2s-2) possible shapes. To see this, assign a deterministic rooted
spanning tree and traverse each edge twice in a deterministic order.
The resulting length2s-2 walk recovers its visited vertex set. There
are at most D choices at each step. If a bad component has size at leasts,
it contains a connected bad subset of exactlys through its root. Thus
(1) bounds that event by a_s. The condition in(2) makes all bad components
finite almost surely, by a countable union over roots.

For one bad component gamma of size s, restrict j to edges with both
endpoints in gamma. Every nonzero incident current edge stays inside
gamma, so the restricted current j_gamma is divergence-free. There are
at most4s positively oriented nearest-neighbor edges with both endpoints
in gamma. Consequently

    sum_e |j_gamma,e|<=12s.                                (4)

Let a be the coordinatewise minimum corner of gamma's bounding box.
For each vertex x in the box, use the coordinate-ordered lattice path
P_x from a to x, moving in directions0,1,2,3. For a positive edge
 e=(x,x+e_mu), commute its final mu-step backwards through the later
coordinate steps of P_x. Each interchange supplies one oriented unit
plaquette. The resulting2-chain Q_e obeys

    boundary Q_e=P_x+e-P_(x+e_mu),
    ||Q_e||_1<=sum_(nu>mu)(x_nu-a_nu)<=3(s-1).             (5)

All its plaquettes lie in the component's bounding box. The size bound
uses the fact that a Chebyshev-connected s-vertex set has coordinate
range at most s-1. Negative edge coefficients are handled by linearity.
Now set Q_gamma=sum_e j_gamma,e Q_e. At every vertex the coefficients
of P_x cancel by current conservation, giving

    boundary Q_gamma=j_gamma,
    ||Q_gamma||_1<=36s^2.                                 (6)

This is an integer construction, without a real-valued inverse Laplacian
or an assumption that the current was a single simple loop. Its box may
overlap the boxes of other components; those overlaps are handled next.

## 3. Exponential tail and finite enlarged-box components

Enlarge each component's coordinate bounding box by1 in all directions,
and call it B_gamma. Choose any fixed deterministic vertex anchor r_gamma
in gamma, for example the lexicographically first vertex. Since gamma
has size s,

    B_gamma subset r_gamma+[-s,s]^4.                      (7)

The number of possible anchors of an s-component whose enlarged box
contains the origin is at most(2s+1)^4<=K w(s). For a fixed box of an
s-component, an overlapping box of a t-component has anchor within
Chebyshev distance s+t of its anchor. The number of possible anchors is
at most(2(s+t)+1)^4<=K w(s)w(t). The constant K=4096 deliberately
exceeds both elementary counting constants.

The expected number of enlarged boxes meeting a fixed unit neighborhood
is finite by sum_s K w(s)a_s<infinity. The same estimate holds with a
larger finite constant for any compact region. Thus the box family is
locally finite almost surely.

Consider a path of k distinct overlapping component boxes starting at
one containing0, and let their sizes be s_1,...,s_k. The actual components
are disjoint as vertex sets. For specified component shapes, (1) therefore
bounds the probability that all of their vertices are bad by p^(sum s_i).
Their being maximal components only adds constraints, which may be
dropped. After assigning anchors and shapes with the preceding counts,
the total probability contribution is at most

    K^k product_(i=1)^k [w(s_i)^2 a_(s_i)].               (8)

In deriving this bound, disjointness is used BEFORE summing over a larger
set of shapes; probabilities of overlapping sets are never multiplied.
This avoids an unjustified independence step.

If this box path reaches a point at distanceR, (7) and the overlap
condition imply R<=2 sum_i s_i. Insert exp(c sum s_i) into(8), sum the
sizes and then the path length k>=1. The resulting geometric series is
precisely(3). Local finiteness guarantees that any connected union
component reaching distanceR contains such a finite path of distinct
boxes. Letting R increase proves that every repaired union component
is bounded and contains finitely many boxes.

The sum Q=sum_gamma Q_gamma is therefore locally finite and has boundary
j. Every local coefficient is a finite integer sum. The construction
does not require independent components or disjoint bounding boxes.

## 4. Passing from conserved compact current to a real lift

Work on the infinite contractible cubic complex Z^4. Let a0 be chosen
real representatives of compact link angles, and let F be the oriented
principal2-cochain of da0. Choose the principal value once on each
positive face and extend it antisymmetrically to the opposite orientation;
do not reapply a half-open principal-value map to the opposite orientation.
Then

    m=(da0-F)/(2pi) is integer, J=dF/(2pi)=-dm,
    dJ=0.                                                 (9)

For an explicit orientation convention, a dual face with increasing
axes B based at y maps to a primal face with complementary increasing
axes A based at x=y+sum_(mu in B)e_mu, with sign of the permutation
(A,B). Denote this identification by I_k when the primal degree is k.
Directly expanding the cubical incidences gives
 d I_2(Q)=-I_3(boundary Q). Duality takes J to the divergence-free
integer dual1-chain j with I_3(j)=J. Thus m_dagger=I_2(Q) has
 dm_dagger=-J and support in the enlarged boxes. The sign is explicitly
checked on all six orientations of a unit dual plaquette; it is not
a second choice of the principal branch.

Now M=m-m_dagger is a closed integer2-cochain. On the full contractible
cubic complex, integral cohomology in degree2 vanishes, including for
unrestricted cellular cochains. Hence M=dn for an integer1-cochain n.
There is no decay assertion for n. This exactness also follows directly
from coordinate-path contractions: each coefficient of the contracted
cochain uses only finitely many faces between the origin and that link.
No infinite sum of coefficients is needed at a fixed link.

Set a=a0-2pi n. Then

    da=F+2pi m_dagger.                                    (10)

Outside the repaired boxes, the raw real curl equals the principal curl.
Equation(10) does not claim that a itself is small, bounded, stationary,
or uniquely chosen. Only its curl has the stated local property.

If a0 has zero temporal link component, the lift can preserve that gauge.
Choose an integer0-cochain lambda by summing n_time along each temporal
line from time0, using the signed finite sum for negative times. Then
replace n by n-dlambda. This leaves dn unchanged and sets n_time=0.
The resulting real lift has a_time=0. This step uses infinite or open
time; it is not a proof for periodic time with nontrivial holonomy.

The proved construction has the contractible domain Z^4. A periodic-domain extension is outside this result. The original stronger topological exclusion discussion remains exact in history with its formal negative certification deferred.

## 5. Conditional application to the supplied compact Hamiltonian

This application uses the linked magnetic-excursion and temporal-oscillation results for the supplied compact Hamiltonian, including the full spatial ground-path construction and its local compact path specification. The sampled-event parent supplies the Hamiltonian and common constants. Thus an actual infinite spatial-volume path law is available, rather than just two finite-volume event formulas. The abstract geometric result in sections1-4 remains independent under its explicit finite-set probability premise(1).

For each coarse4-cell (spatial cube times an interval of durationT),
declare it bad if any of its six spatial faces has a principal magnetic
excursion of size at least alpha, or any of its twelve spatial edges
has circle oscillation at least alpha during that interval. There are
18 possible basic witnesses. Take0<alpha<=pi/3.

Let epsilon_B and epsilon_E be the linked same-orientation joint
bounds for distinct magnetic and temporal basic events, and set
 epsilon=max(epsilon_B,epsilon_E). They have six orientation classes
in total. A specified collection of r distinct witnesses is bounded
by epsilon^(ceil(r/6)), by taking the most numerous orientation class.
Each witness belongs to at most four coarse4-cells. Thus for n specified
bad cells, choose one of18 witnesses for each cell, remove repetitions,
and use at least ceil(n/4) distinct witnesses. A union bound yields

    P(all n cells bad)<=p^n,
    p=min(1,18 epsilon^(1/24)).                            (11)

Every nonzero coarse3-cell current has a boundary face of magnitude at
least pi/3. Both adjacent4-cells contain that witness, so both endpoints
of its dual current edge are bad. Spatial faces at a time boundary are
included in the closed-interval excursion event of either adjacent slab.
The principal-face formula also gives |J|<=3. These are exactly the
geometric hypotheses, once the path-event premise is justified.

The explicit supplied-model bounds, for0<g<=1, are

    C0=3pi^2/16+12(1/3-2/pi^2), c_alpha=1-cos(alpha/2),
    q_B=min(1,exp[-T c_alpha/g^2]
                       +16exp[-alpha^2/(512g^2 T)]),
    q_E=min(1,4exp[-alpha^2/(8g^2 T)]),
    epsilon_B=min(1,exp(C0 T) q_B^(1/4)),
    epsilon_E=min(1,exp(C0 T) q_E^(1/4)).                  (12)

At fixed positive alpha,T, decreasing g makes p and Lambda(c) tend to0.
This supplies a nonempty conditional parameter regime; the specific
numeric thresholds are only sufficient estimates. They do not measure
a critical coupling or fix the model's coupling from the axioms.

Outside the repaired regions every coarse cell is good, raw curl equals
principal curl, and the endpoint spatial curls are smaller than alpha.
Consequently the equality region of the convex lifted-kernel construction
is available locally. This conclusion is geometric and pointwise.

## 6. What this does not settle

The real lift is a coarse-time link field selected by a field-dependent
integer construction. It is not automatically the continuous lift of the
original Brownian paths; interval winding labels, particularly in repaired
regions, have not been recovered from endpoint angles alone.
It is not a measure-preserving coordinate chart with demonstrated
Jacobian, multiplicity or normalized density. Macroscopic stiffness and normalized source matching remain unestablished by this work.
No equality, total-variation convergence or field-limit equivalence
between the compact and convex measures is asserted.

The next obligation is an exact, normalized representation that carries
these regions and their source dependence, followed by bounds sufficient
for the desired response or field limit. The integer construction
resolves a conditional geometry question; it does not assume that final
analytic obligation under the name "dilute defects".


## Evidence, scope and recovery

The [primary](../scripts/compact_rotor_integer_filling_check_2026_09_16.py) retains the original numerical domains and tolerances. Its [capture destination](../logs/runner-cache/compact_rotor_integer_filling_check_2026_09_16.txt) and JSON destination under the same directory bind future actual-source evidence. TOTAL counts completed diagnostic families, not individual assertions. No primary was run during author preparation.

The [exact original recovery](work_history/review_loop/pr8166/README.md) preserves every original proof, failed attempt, mutation and output. Historical author review/status statements are not current independent authority.

## No-Go Discipline Gate

N1: Formal negative certification is deferred; no five-route packet is invented. The live claims are the displayed positive conditional implications.
N2: Shared comparison and supplied-model premises are not independent walls.
N3: Geometry, time weights, norms, coupling and mathematical imports remain explicit.
N4: Finite checks support specified identities; they do not execute normalized compact transfer.
N5: The runner states per_element, per_site, per_mode, per_block and lattice_wide scope; infinite-domain conclusions rely on the written proofs.
N6: Exact normalized winding/source representations remain open work; no new axiom is proposed.
N7: Compact transfer, covariance identification and physical selection have not been established here. No impossibility conclusion is substituted.
N8: Original stronger negative arguments remain exact in history, with branch retention for deferred partial closure. The limitation of the certification packet does not disprove the positive mathematics.
