# A source remainder bound for the full two-electric, two-magnetic coefficient

Personal proof candidate, 2026-09-15. The objects here use the infinite
cubic Hodge kernels and all finite closed component shapes. This treats
one actual connected activity coefficient, including its same-species
interactions and hard core. It does not sum the activity series, select
an infinite-volume state, establish a quadratic coefficient limit, or
identify arbitrary finite-free-boundary limits.

## 1. A graph version of Holder proved directly from trees

Let H be a finite connected multigraph on vertices 0,...,v, with no loops.
Fix x_0=0 in Z^4. Give edge e=ij a nonnegative function f_e(x_i-x_j).
Let lambda_T be a probability distribution on spanning trees, and put
alpha_e=sum_(T containing e) lambda_T. Assume alpha_e>0. Then

    sum_(x_1,...,x_v) product_e f_e(x_i-x_j)
       <= product_e ||f_e||_(1/alpha_e).                (1.1)

Indeed the integrand is the product over T of
[product_(e in T) f_e^(1/alpha_e)]^lambda_T. Holder bounds its sum by
the corresponding product of tree sums. Each tree sum is exactly the
product of edge l1 norms, by successive leaf summation. Combining edge
exponents gives (1.1). Apply first to finite sums and then monotone
convergence; the bound itself certifies convergence. Parallel edges are
distinct factors, so no simplicity assumption is used.

If H has no bridges and M edges, choose, for each edge e, one spanning
tree containing e and one avoiding e. Their uniform distribution over
these 2M choices has edge probabilities beta_e satisfying

    1/(2M) <= beta_e <= 1-1/(2M).                       (1.2)

Existence needs only connectivity and the absence of a bridge: an edge
can be extended to a tree, and deleting a nonbridge leaves a connected
graph. No tree-packing theorem is imported.

## 2. Source parity supplies the missing strict exponents

Let G be a connected multigraph on the four defect vertices. Attach
k_i source edges from vertex i to a new fixed vertex 0, and let
K=sum_i k_i>=4. Suppose deg_G(i)+k_i is even for every i. The augmented
graph H is connected and every vertex has even degree; K is even as
well. It has no bridges: every cut in an even-degree graph has even
cardinality.

Choose a fixed spanning tree of G and one of its K source edges uniformly
to connect vertex 0. This gives a tree distribution with source-edge
probability 1/K. Mix it, with weight

    delta = 1/[4(K-1)],

with the interior distribution in (1.2). The resulting alpha satisfies

    0<alpha_e<1                  for every spatial edge,
    alpha_e<=5/(4K)             for every source edge,
    sum_source alpha_e<=5/4.                           (2.1)

The first statement uses (1.2) even for spatial edges in the fixed tree.
Consequently each spatial exponent p_e=1/alpha_e exceeds one, while
each source exponent is at least 4K/5>2. These strict inequalities are
the point of using source parity and the additional vertex.

Put kappa(x)=(1+|x|_1)^(-4), so kappa belongs to l^p(Z^4) for every p>1.
Suppose each source-edge function L_i,a obeys

    ||L_i,a||_p <= A_i a^(2-4/p), p>=2, 0<a<=1.

Equation (1.1) and (2.1) give, for this fixed graph,

    sum_(x_1,...,x_4) product_spatial kappa(x_i-x_j)
                            product_i |L_i,a(x_i)|^k_i
       <= C_G product_i A_i^k_i a^(2K-5).              (2.2)

Constants depend on graph size and the chosen exponents, not on a or
the source location. The exponent need not be sharp. In particular
K=4 gives O(a^3). If source parity is removed, an unmarked side of a
one-edge cut can force p=1 and this proof no longer applies.

## 3. Actual component bonds and the needed spatial majorant

Use the odd, normalized cubic marked filling rules and measures of
the previous all-component note at e3fc0b7707dce894ef98e7981a9feaf6041708f8.
Each mass-m filling has l1 norm at most 4m^2 and support in its component
bounding box, with fixed dual-cell offsets allowed. Anchored shape count
is at most 2*393^(m-1), up to a fixed orientation factor.

The infinite Hodge projection kernel has the entrywise estimate

    |P_ab(x)|+|Q_ab(x)| <= C kappa(x).                 (3.1)

One can see this directly from its Fourier symbol. On a dyadic annulus
|k|~2^(-j), its r-th derivatives are bounded by C_r 2^(jr). Smooth
dyadic partition and repeated integration by parts bound its Fourier
coefficient by C_L 2^(-4j)(1+2^(-j)|x|)^(-L). Summing the annuli with
L>4 gives (3.1); the part away from zero is smooth and rapidly decaying.
The identity contribution to Q is supported at x=0 and fits the bound.

For fixed component shapes i,j with anchors x_i,x_j, the raw same-species
couplings J_ij=x_e<S_i,PS_j> or x_m<n_i,Qn_j>, and mixed theta_ij,
are therefore bounded in absolute value by

    A_ij kappa(x_i-x_j),                              (3.2)

where A_ij is a fixed-parameter polynomial in m_i,m_j. For example
a constant times (1+m_i+m_j)^4 m_i^2 m_j^2 suffices, multiplied by
x_e, x_m or c as appropriate. The inequality
1+|x|<= (1+|x+y|)(1+|y|) controls the finite filling shifts.

For a same-species incompatibility indicator chi_ij, overlapping or
adjacent support forces anchor separation at most C(m_i+m_j). Thus
chi_ij is bounded by another mass polynomial times kappa^2. This also
covers repeated components and different marks of the same component.

The actual Mayer pair factor, at fixed signs, is C_ij+sigma_i sigma_j O_ij:

    same:  C=(1-chi)(cosh J-1)-chi,
           O=-(1-chi)sinh J;
    mixed: C=cos theta-1, O=i sin theta.

For a chosen same-species C bond, split its displayed two summands.
Every even bond then has two spatial kappa factors; every odd bond has
one. Use |cos theta-1|<=theta^2/2, |sin theta|<=|theta|,
|cosh J-1|<=J^2 exp(|J|)/2 and |sinh J|<=|J|exp(|J|).
The only extra exponential factors are exp(|J_12|) and exp(|J_34|),
one for each same-species pair; they occur only at compatible pairs.

This last restriction matters. There are just two components of each
species. For a compatible pair, current supports are disjoint, and
G>=I/16 implies

    E_i+E_j-2|<current_i,G current_j>|
       >= (||current_i||_2^2+||current_j||_2^2)/16.

Apply the spectral inequality to current_i plus or minus current_j.
The original self-weights times the possible exp(|J_ij|) hence retain
exp[-x(m_i+m_j)/32]. If that pair bond is absent or is its incompatible
hard-core term, its individual self-weights give at least the same
reserve. This proves an exp[-sum_i x_i m_i/32] majorant for every
selected bond term in this four-component calculation. It is not an
estimate for the absolute Mayer graphs of arbitrary particle number.

## 4. The subtracted physical source coefficient

Let h_a(p)=a^2 f(a midpoint(p)) for smooth compactly supported real f.
Write the actual source amplitudes as L_i=-g<S_i,Ph_a> for electric
components and L_i=-i b<n_i,Qh_a> for magnetic ones. For fixed shapes,
Young's inequality and the l2/linfinity source estimates imply

    ||L_i||_p <= C_f sqrt(x_i) ||fill_i||_1 a^(2-4/p), p>=2.  (4.1)

Their pointwise large-component bound is |L_i|<=C_f a sqrt(x_i)m_i.
For |z|<=R and sufficiently small a this absorbs exp(R sum_i |L_i|)
into half the reserve of section 3, leaving exp[-sum_i x_i m_i/64].

In any finite component/translation restriction, introduce counting
activities lambda_e,lambda_m in the exact component partition function.
Its log coefficient of lambda_e^2 lambda_m^2 is

    C_22,a(z)=4 integral dnu_e^2 dnu_m^2
       average_sigma exp(z sum_i sigma_i L_i)
          sum_(connected simple graphs on four labels)
                              product_edges (C_ij+sigma_i sigma_j O_ij).

The factor is 2^4/(2!2!); nu uses the sign-half and normalized-mark
convention of the earlier notes. Repeats are included with the actual
hard core. This is a finite formal Taylor coefficient at activities zero,
not an assumption that the activity series converges at one.

Choose which edges are odd. Summing each sign leaves a factor cosh(zL_i)
at an even odd-edge degree and sinh(zL_i) at an odd degree. Expand exactly

    cosh(zL)=1+(zL)^2/2+remainder_4,
    sinh(zL)=zL+remainder_3,

with |remainder_r|<=C_R |L|^r exp(R|L|). After removing the total constant
and quadratic terms, the remaining finite product expansion has monomials
with total source degree 4<=K<=16, matching the odd-edge degree parity
at every vertex. Double every even bond and keep each odd bond once.
The resulting spatial multigraph is connected and satisfies precisely
the parity assumption of section 2.

Apply (2.2) with (4.1). Each term is O(a^(2K-5)), hence O(a^3), times
a mass polynomial and exp[-sum_i x_i m_i/64]. The complete sum over
all marked shapes converges whenever both x_i/64>log 393. The explicit
range beta>=16 and g^2>=512 suffices. The finite number of four-vertex
graphs and Taylor-product choices changes only the constant.

It follows that the subtracted integral, defined by making the subtraction
inside the component sum, is absolutely convergent and obeys

    sup_(|z|<=R) |C_22,a(z)-C_22,a(0)-(z^2/2) C_22,a''(0)|
       <= C_(f,R,beta,N) a^3.                         (4.2)

Equation (4.2) is shorthand for that convergent subtracted integral and
its uniform finite-restriction bound. It does not assert separate absolute
convergence of the unsubtracted source coefficient or its quadratic part.
The bound passes to arbitrary increasing component restrictions of this
subtracted infinite-kernel functional by dominated convergence.

## 5. What this resolves and what it leaves

The non-quadratic source remainder at the first two-by-two mixed coefficient
vanishes, with all finite component shapes, the surviving odd cycles,
the same-species Coulomb factors, and the actual support incompatibility
included. The power a^3 is a sufficient, unoptimized upper bound. It is
a derivation about the supplied clock law's coefficient, not a simulation
of its complete phase or an independently reviewed theorem.

The constants are not controlled as particle number tends to infinity.
In fact the near-l1 spatial exponents deliberately permit large constants.
Also, the separate quadratic coefficient still needs its signed limiting
operator analysis, and finite-free-boundary matching is not supplied here.
The full characteristic-functional limit at physical activities one remains
open. The four-component energy reserve in section 3 must not be reused
for arbitrary absolute Mayer graphs without a new stability argument.

## 6. Finite author verification

The checker enumerates all 624 connected absent/even/odd bond patterns on
four labels and all 23,556 parity-matched Taylor remainder choices. It
constructs the containing/avoiding spanning trees explicitly; all spatial
exponents are strictly above one and all source exponents satisfy the
stated bound. A graph with an unmarked side of a bridge rejects the
containing/avoiding-tree premise. Three direct finite-group sums satisfy
the graph Holder inequality.

Separately, connected partition inversion and the even/odd bond expansion
give the same complex-source remainder for compatible, electric-overlap
and double-overlap component lists on the previously constructed four-cube
chain. The maximum arithmetic discrepancy is 6.17e-61 at 60-digit working
precision. Its projection inputs come from floating cochain linear algebra;
this checks the identities at those supplied entries and does not certify
their entries to 60 digits. No scaling simulation or independent review
is claimed.
