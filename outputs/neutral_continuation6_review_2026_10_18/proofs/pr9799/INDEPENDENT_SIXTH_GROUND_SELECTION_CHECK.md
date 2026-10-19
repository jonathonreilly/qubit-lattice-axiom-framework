<!-- Original PR9799 source SHA256 3f2c03ac0ff6d924b354584f62745f5be91130a0bc8ddada71412b64aa5515db. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Focused check: height-six global ground selection at fixed transverse size

The proposed leading flat-code Hamiltonian and all-positive plane-character selection are supported for each fixed even R>=8, provided the conclusion is obtained through sufficiently high-order finite-dimensional analytic perturbation theory. The existing truncation at native order six alone cannot control a splitting of order lambda^(R+4). No size-uniform threshold follows.

## Native matrix-element lower bounds

In the N=0 aligned-column basis, a term changing k columns must flip 6k physical spins. Each transverse insertion flips two spins, so its native order is at least 3k. Moreover k is even: each longitudinal Z-plane parity is exact and a complete column flip changes every such plane parity once. Thus every nonzero off-diagonal N=0 matrix element has k>=2.

At k=2 and order six, minimal spin counting forces one insertion on the edge joining those two columns at each longitudinal layer. The columns must be nearest neighbors. These are precisely the known height-six winding terms, with coefficient -gamma lambda^6 and gamma=63/8192 in units J. Background-dependent phases cancel for even height six, so both transverse orientations have this negative coefficient. No other two-column motion saturates that lower bound.

Diagonal coefficients, including higher plaquette interactions, are constant within the flat code: exact physical plane flips act transitively on its computational backgrounds. This statement does not assert that diagonal coefficients outside the flat code are constant.

## Competing weighted orders

First perform the finite-size analytic reduction to N=0, subtract its scalar and rescale by lambda^4. The leading operator is the diagonal plaquette Hamiltonian, with an order-one gap from the flat code to any nonflat state. Its four-flux gap coefficient is Delta_c=3/8. Diagonal corrections and higher coefficients can be expanded about this invertible complement; they do not introduce denominators smaller than lambda^4 at this stage.

An effective path with r off-diagonal native N=0 jumps changing k_1,...,k_r columns has order at least

3 sum_j k_j -4(r-1) = sum_j k_j+4+2 sum_j(k_j-2).

The final changed-column count m is at most sum_j k_j. Therefore its weighted order is at least m+4. Equality requires every jump to change exactly two columns at native order six and requires no column to be flipped twice. Extra nonconstant diagonal insertions are higher order relative to the leading flux resolvent; leading order-four diagonal contributions are already resummed in that resolvent. Repeated visits to the flat code belong to the subsequent degenerate effective expansion and cannot create an earlier nonidentity transition. In a first minimal-row process no proper subset is flat at all.

This rules out a competing four-column order-twelve native jump: replacing two elementary jumps removes one lambda^-4 flux denominator and raises rather than lowers its weighted order. The argument also handles higher native jumps and arbitrary paths that flip columns redundantly.

## Minimal flat operators and coefficient

A nonidentity flat pattern has the form a_x b_y. On an R by R torus the smallest support is R columns, attained exactly by one whole row or one whole column for R>=4. Thus the first nonconstant flat operator is at order R+4. Saturating paths use n=R/2 disjoint adjacent pairs covering that row or column. There are precisely two perfect matchings of the cycle. Any proper partial matching with c occupied runs produces four bad plaquettes per run and costs J Delta_c lambda^4 c.

The ordering sum for each matching is binom(2n-2,n-1), so the first flat-code Hamiltonian, after its scalar, is

-J t_R lambda^(R+4) [sum_x R_x+sum_y C_y],

t_R=2 binom(R-2,R/2-1) gamma^(R/2)/(Delta_c)^(R/2-1)>0.

Each coefficient has negative sign: n negative hopping factors and n-1 negative resolvent denominators. There is no proper intermediate flat state in such a path, hence no folded cancellation of this first transition.

## Character selection and actual ground

The row and column flips commute, with the single relation product_x R_x=product_y C_y. They act regularly on the 2^(2R-1) dimensional flat code. The displayed Hamiltonian has its unique minimum in the character with every row and column eigenvalue +1. The nearest allowed character changes at least two signs, giving a leading splitting 4J t_R lambda^(R+4); this is a statement about the flat-code splitting, not the higher four-flux excitation gap.

For even R and longitudinal height six, the physical Y plane agrees with its logical column flip on N=0: Y tensor six is -X tensor six times Z tensor six on a column, and the product over an even number R of aligned columns has the compensating sign +1. Physical X planes give the other flips directly. Every flat background has physical z-plane Z product +1 because product_(x,y) a_x b_y=(product_x a_x)^R(product_y b_y)^R=1. These labels therefore match the stated physical plane characters, and exact symmetry preserves the labels through dressing.

For fixed R the Hilbert space is finite. Analytic block diagonalization across the original order-J wall gap followed by analytic degenerate reduction across the rescaled plaquette gap makes the effective expansion legitimate to any required finite order. Its remainder can be made o(lambda^(R+4)). The unique leading character minimum then selects the actual microscopic ground for all sufficiently small positive lambda. Higher wall sectors stay an order-J distance away. A fourth- or sixth-order global error bound alone is insufficient for this last step; the fixed-R analytic argument is essential.

## Scope

The threshold in lambda may depend strongly on R, and t_R itself varies rapidly with R. There is no justified exchange of the fixed-R weak-coupling limit with a growing transverse volume. The result removes a chosen-plane-sector premise in the ordered finite-size limit, but does not supply a uniform thermodynamic ground-selection theorem, an isolated bulk pole or an empirical particle identification. Any subsequent readout calculation must still use the actual symmetry sector and control its own perturbative order.
