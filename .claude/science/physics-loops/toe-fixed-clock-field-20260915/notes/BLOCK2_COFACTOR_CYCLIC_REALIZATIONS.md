# Local cofactor signs and cyclic operator realizations

Personal proof candidate, 2026-09-15. This addresses a specified oriented
resource assignment in a determinant exclusion derivative. Finite sign and
source challenges pass. The following CONTACT_REGISTER_SUM note handles
the resource sum for a prescribed derivative graph; neither note sums all
physical graphs. There is no independent review.

Fix k distinct differentiated pair parameters. Expand the product rule by
assigning each derivative to a shared footprint resource u and to one of
its two oriented matrix entries (r,c). For one such assignment E, let
R_u and C_u be the selected row and column indices at resource u. A repeated
selected row or column in a resource gives zero. Otherwise k_u=|R_u|=|C_u|.
Every endpoint index must have u in its actual footprint. These requirements
are products of local component indicators.

Choose ANY total order O of the vertex indices. For I_u={i:u in A_i}, the
assigned derivative term of det S[I_u,I_u] is

    epsilon_(u,O)(I_u) det S[I_u minus R_u,I_u minus C_u],
    epsilon=sign(matching in the O-sorted R_u,C_u lists)
                (-1)^(sum_(r in R_u) pos_(I_u,O)(r)
                         +sum_(c in C_u) pos_(I_u,O)(c)).

The position is counted from one. Since 2k_u selected row/column positions
occur, changing to zero-based positions would give the same parity. The
cofactor identity follows by grouping determinant permutations containing
the assigned entries. It holds at singular Gram matrices without division.

The sign apparently depends on the entire footprint list. It is actually
local after the resource assignment and O are fixed. Write

    pos_(I_u,O)(r)=sum_(v <=_O r) 1[u in A_v].

Thus epsilon is a fixed matching sign times product_v (-1)^(1[u in A_v] h_(u,v)),
where h_(u,v) is the number of selected rows and selected columns weakly
after v in O. Each factor depends only on A_v. No remote component label
is needed to evaluate that vertex factor.

Let C_i=a*(v_i) with Gram S. On normalized Hilbert-Schmidt space define

    Q_(u,i)(X)=(C_i*)^(1[i in I_u minus R_u])
                          X C_i^(1[i in I_u minus C_u]).

Omit resources outside A_i, enforce the required local endpoint indicators,
and multiply the local sign just derived. Each resulting vertex map is a
contraction. The cross-minor CAR identity from the determinant note gives

    assigned derivative term
       = 2^(-k) product_i 2^|A_i|
                  <I, product_(i in order O) M_i(A_i) I>,

up to the fixed product of matching signs, absorbable into one vertex.
There are |I_u|-k_u surviving creators and annihilators at resource u, so
the trace normalization yields exactly this factor 2^(-k), with k=sum k_u.
The identity vector is unit norm independently of the resource dimension.

The one-sided maps do NOT generally commute. The useful replacement is
that the SAME scalar assigned-derivative coefficient has the displayed
local-contraction realization for EVERY cyclic order of the vertices.
Changing the order changes local sign factors and the matching sign, and
may change the ordered maps; it does not change the scalar cofactor term.
This is a family of realizations, not a false commutation assertion.

For the scalar loop sum at a finite component cutoff, let J be selfadjoint,
rho=||J||, and L its diagonal source. Put the unchanged boost 2^|A| into J's
vertex weight. Include any Gaussian replica phases and normalized source
exponentials in the local contractions. For a specified assignment with k
entries, the coincident four-source case at vertex j can choose the cyclic
order starting at j. The same two boundary Hilbert-Schmidt maps as in the
full-hard-core note give

    |F_(4 at j)| <= 2^(-k) rho^(l-2) Tr |L|^4 J^2.

For distributed four-source powers, use the scalar analytic function of
source exponents defined by the ORIGINAL finite coefficient sum. On each
simplex vertex choose its own cyclic contraction realization. Imaginary
source powers are local modulus-one phases, so the coincident bound is
uniform there. Three-lines interpolation on that scalar function then gives

    |F_(k_1,...,k_l)| <= 2^(-k) rho^(l-2) Tr |L|^4 J^2,
    sum_i k_i=4.

The analytic function need not have one commuting operator realization
valid for every boundary choice. All boundary estimates concern the same
function. Zero source entries are regularized at finite cutoff and then
removed. The same reasoning applies to two source powers.

This is uniform for a FIXED resource assignment. Summing assignments cannot
be justified by taking this uniform bound times their number: the resources
range over an infinite lattice. The retained local membership projections
must be used in that summation. The following CONTACT_REGISTER_SUM note
uses active edge registers to supply that sum for a prescribed graph,
while retaining the cyclic realization and degree-dependent norm bound. No new physical activity-one
or field-scaling claim is made here.


## Author challenges

The runner compares determinant permutation coefficients with the local-sign
CAR realization over 1,920 footprint/assignment/order cases, including
repeated-row assignments that must vanish. Maximum error is 3.06e-16. It
checks all 35 distributions of four source powers for each of four generic
finite loop assignments. Cyclic realizations agree configuration by
configuration, with maximum weighted discrepancy below 9.48e-22. These are
generic matrix checks of the lemma, not an actual-lattice convergence test.
The CAR construction is shared with the preceding separately declared
checks; there is no independent scientific review.

Dropping the local position sign changes an assigned cofactor by 0.409.
A one-sided creation map and a two-sided map have commutator norm 7.685
in a finite challenge, rejecting the tempting false commutation shortcut.
The proof instead uses order-dependent realizations of the same scalar
coefficient, including the same source-exponent analytic function on every
three-lines boundary.
