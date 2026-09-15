# Exact support exclusion preserves a Gaussian-dressed loop source sum

Personal proof candidate, 2026-09-15. This extends the preceding restricted
loop result to the actual support-compatibility rule. It retains every
same-species Gaussian pair interaction in that loop functional. Residual
mixed pair factors, softened forest exclusions and branching graphs remain
outside the result. No physical pressure identity or full field limit is
asserted. Verification is personal, without independent review.

## 1. The exclusion rule has a local footprint

Work on the infinite four-dimensional cubic lattice with the component
definition pinned in prior block27: electric occupied edges are adjacent
when they share a vertex; magnetic occupied three-cells are adjacent when
they share a four-cell. A component is a connected part of that occupied
support. Two same-species components are incompatible when their supports
overlap or are adjacent, since they would form one component.

Give an electric component the footprint consisting of its occupied edges
and all their incident vertices, with these two resource types distinguished.
Give a magnetic component the footprint consisting of its occupied three-cells
and all incident four-cells. Electric and magnetic resource universes are
disjoint. Then incompatibility is exactly footprint intersection. Occupied
cells account for overlap itself; incident endpoints account for adjacency.
Each occupied cell has two endpoints of the relevant type on the infinite
lattice, so a component with integer l1 mass m has

    |A(component)| <= 3 |supp current| <= 3m.             (1.1)

The extra occupied-cell resources are redundant on the infinite lattice,
but keep the same formula valid for the tested finite support convention.
No filling area or bounding-box volume is charged in (1.1). A filling mark
does not change the footprint. Take one representative from each sign pair
and average its separate orientation sign as in the preceding loop note.

## 2. Exclusion is an exact matrix element of local contractions

For each resource u use C^2, unit vector v_u=(1,1)/sqrt(2), and lowering
operator a_u=|0><1|. It has norm one and square zero. Different resources
commute. Put Q_A=product_(u in A) a_u and v=product_u v_u. Then

    product_(i<j) 1[A_i intersect A_j is empty]
       =2^(sum_i |A_i|) <v, product_i Q_(A_i) v>.         (2.1)

If any resource occurs twice, both sides vanish. Otherwise the matrix
element is the product of 1/2 over used resources, proving the identity.
All Q_A commute, including when their product vanishes. Their norms are
one, and the boundary vector has norm one, independently of the number
of resources. For infinitely many resources, the incomplete tensor product
with reference vectors v_u gives the same local operators and unit vector.

The factor 2^|A| is absorbed into the component activity. This is a linear
mass cost by (1.1). The auxiliary two-dimensional factors implement a
summation identity; they are not additional physical degrees of freedom
or a change to the model's microscopic state.

## 3. A trace estimate with operator-valued vertex factors

Let J be a finite selfadjoint scalar matrix on component space H, let
rho=||J||, and let M_i be diagonal operators on H tensor K. Suppose each
entry M_i(a) is a contraction on K. For unit v in K define

    F=<v, Tr_H product_(i=1)^l M_i (J tensor I) v>.

The unmarked bound is

    |F| <= rho^(l-2) Tr_H(J^2), l>=2.                  (3.1)

Move the last scalar J cyclically through the partial component trace.
The boundary map (I tensor <v|)(J tensor I) has Hilbert-Schmidt norm
||J||_2. The other boundary map (J tensor I)M_l(I tensor |v>) has squared
Hilbert-Schmidt norm

    sum_(a,b) |J_ab|^2 ||M_l(b)v||^2 <= Tr J^2.

There are l-2 scalar J factors in the middle, and the remaining vertex
factors are contractions. The two Hilbert-Schmidt bounds and the middle
operator norm prove (3.1). No dimension of K occurs. Entrywise commutation
is not needed for this unmarked estimate.

For the source estimate assume, in addition, that all entries M_i(a)
commute with all entries M_j(b), across every i,j,a,b. Let L be diagonal
and complex on H, and k_i>=0 integers with sum_i k_i=4. Then

    |<v,Tr_H product_i M_i L^(k_i)(J tensor I) v>|
       <=rho^(l-2) S4_2, S4_2=Tr_H |L|^4 J^2.          (3.2)

First put all four source factors on one vertex. Because the resource
entries commute, rotating that vertex to the front of the component trace
does not change their word in the scalar matrix-element expansion. Move
two scalar L factors to the opposite end by partial-trace cyclicity.
The two boundary maps now have Hilbert-Schmidt norms at most sqrt(S4_2):

    ||(I tensor <v|) L^2 M_i (J tensor I)||_2^2
       =sum_(a,b) |L_a|^4 |J_ab|^2 ||M_i(a)*v||^2 <=S4_2,
    ||(J tensor I)L^2(I tensor |v>)||_2^2=S4_2.

The remaining l-2 propagators give rho^(l-2), proving the coincident case.
Complex phases of L are absorbed into diagonal contractions.

For completeness, extend from this case to any distribution by scalar
three-lines interpolation, rather than assuming a matrix-valued ALT bound.
In a finite restriction first replace |L_a| by max(|L_a|,epsilon)>0.
In the trace replace L^(k_i) by |L|^(4 z_i), absorbing the original phases
into M_i, and impose sum z_i=1. This is analytic in the z_i. On every
vertex of the simplex Re z_i>=0, sum Re z_i=1, only one vertex carries
four real source powers. All imaginary powers have modulus one and can
be absorbed into the commuting entries, so the coincident bound holds
uniformly in imaginary directions. Repeated Hadamard three-lines gives
the same bound throughout that simplex. One explicit induction separates
z_1=z and writes z_j=(1-z)alpha_j for j>1, with nonnegative alpha_j summing
to one. The Re z=1 boundary is the first coincident case; the Re z=0
boundary uses the lower-dimensional induction, with imaginary factors
absorbed into M. Finite sums of these imaginary exponentials are bounded
on the strip, so the usual bounded three-lines theorem applies. Take
z_i=k_i/4 and then epsilon down to zero. This proves (3.2).

## 4. Apply the lemma to the complete hard core and Gaussian dressing

Use the local activity w_i=(2/384)exp[-x_i||current_i||_2^2/64] and the
same-species stable Gaussian G_sigma from the preceding loop note. Its
replica covariance s_ij K_species is positive semidefinite, fixed independently
of component labels and positions. Conditional on its real Gaussian fields,
each vertex contributes a scalar phase of modulus one. Multiply that phase
by Q_(A_i). These are precisely the commuting entries required by (3.2).
The finite Gaussian expectation and orientation average preserve the bound.

For physical amplitudes L_e=-g<S,P h_a>, L_m=-i b<n,Q h_a>, and |z|<=R,
put the complete positive weight

    q_i=w_i 2^|A_i| exp(R|L_i|)                        (4.1)

into the scalar sine matrix T. The remaining source exponential divided
by exp(R|L_i|) is a diagonal contraction. In counting coordinates set

    T_(m,e)=sqrt(q_m q_e) sin(c<n,PS>),
    J=[[0,T*],[T,0]], c=2pi N=gb.

Species projectors may be included among the diagonal factors. Thus the
matrix element of the trace gives exactly the alternating loop sum with
full hard core, local weights w, G_sigma and its source. There is no omitted
overlap term, no trace over the resource space, and no resource dimension
factor in the estimate.

The earlier bound |L_i|<=C_f a sqrt(x_i)m_i shows that for
a<=min(g,b)/(128 C_f R), with R=0 interpreted directly,

    q_i <= (2/384) exp[-(x_i/128-3log2)m_i]
        <= (2/384) exp[-x_i m_i/256]                   (4.2)

when x_i/256>=3log2. Let M_species(k) be the filling anchored moments
for q. The full signed sine operator bound and shape count give

    rho <= c sqrt(M_e(2)M_m(2))
                 +(c^3/6)sqrt(M_e(6)M_m(6)),
    M_species(k)<=4 C_A 4^k exp(-x/256)
                  /[1-393*2^(2k+4)exp(-x/256)], k=2,6. (4.3)

At both x>=32768, this majorant is less than 3.862e-33. Each separated
factor x^(k/2) sqrt(M_species(k)) in the norm majorant decreases beyond
that endpoint (differentiate its displayed exponential bound). Fixed
beta=1024,N=8192 is one example satisfying both inequalities. This is a
sufficient range for the restricted loop estimate, not a new phase window.

The source trace is bounded directly with J^2, avoiding a square root of
the activity. The frame estimate on each row gives

    S4_2 <= c^2 sum_species M_other(2)
                   integral |L_i|^4 ||fill_i||_1^2 q_i
           <=c^2 [M_m(2) g^4 M_e(6)||P h_a||_4^4
                   +M_e(2) b^4 M_m(6)||Q h_a||_4^4]
           <= C a^4.                                 (4.4)

Here |<F,u>|^4<=||F||_1^3 sum_y |F(y)||u(y)|^4, followed by the order-six
anchored moment, proves the second line. The last line uses the already
proved infinite-lattice smooth-source l2 and linfinity bounds. All arbitrary
finite component shapes and all normalized marks are included.

## 5. The restricted source remainder sums over every loop length

Let C_l^HC(z), l=2r>=4, be the loop functional just defined, with all
same-species hard-core pairs present at full strength. The same-species
Gaussian may use any prescribed replica correlation matrix satisfying
section4. All non-cycle mixed pair factors are absent from this definition.
The factor i^l for the l odd mixed bonds is harmless. Global sign reversal
makes the orientation average even in z.

Subtract its constant and quadratic source terms inside each finite
component sum. The fourth-order integral Taylor remainder has l^4 ordered
source choices. Apply (3.2) and (4.4) to each, using (4.1) for the residual
source exponential. The result is

    sup_(|z|<=R) |C_l^HC(z)-C_l^HC(0)-z^2(C_l^HC)''(0)/2|
        <= (R^4/24) l^4 rho^(l-2) S4_2
        <= C l^4 rho^(l-2) a^4.                       (5.1)

This is uniform in the component restriction, Gaussian replica correlations
and normalized interpolation averages. At each fixed l, the earlier graph
Holder proof separately gives absolute convergence of the subtracted
source sum: a spatial cycle plus four source legs is bridgeless. The
same-species positive Gram reserve and source bound dominate all fixed-degree
mass polynomials. Hard-core indicators have modulus at most one. Thus
infinite component cutoffs pass at fixed l without an additional unproved
operator-valued trace limit theorem. Finally (5.1) sums over l=2r>=4 with
the defining coefficient 1/r, since sum_r r^3 rho^(2r-2)<infinity.

The resulting restricted loop functional has an O(a^4) non-Gaussian source
remainder. Its unsubtracted pressure and quadratic source term are not
asserted separately convergent here. The coefficient 1/r defines this loop
sum; it has not been identified with the physical connected-expansion weight.

## 6. Finite challenges and exact remaining scope

The runner checks the exclusion matrix element against direct set exclusion,
then compares auxiliary operator loop traces with original scalar sums in
which incompatible labels are explicitly removed. It exercises all 35
distributions of four sources among four vertices, five source distributions
on a nonzero six-cycle family, and a four-cube physical cochain fixture.
The cochain constructor is shared and declared; the tests are not independent
scientific review. Actual finite support adjacency is compared with footprint
intersection, including relative-boundary cells, and obeys the 3m bound.

Replacing the lowering operator by a projector makes a repeated resource
survive; omitting the factor 2^|A| gives one half for a single resource.
Those explicit negative controls reject both shortcuts. The finite physical
fixture is beta=.5,N=3 and its boosted norm exceeds one: it tests identities,
not the large-parameter range or convergence. The latter uses the separate
analytic majorant, whose endpoint is evaluated at high precision.

The progress is specific: actual complete support exclusion can coexist
with the signed loop cancellation and full same-species Gaussian dressing.
The remaining mixed pair factors and branching networks still need control.
The softened forest factor product(1-s_ij chi_ij) is also distinct from the
full hard core treated here. A naive resource for each vertex pair charges
O(l m) resources per component and does not preserve the local activity
bound. No such replacement is used. The full physical activity-one law,
its selected state, quadratic limit and finite-free-boundary matching remain
open. There is no model or axiom obstruction conclusion.
