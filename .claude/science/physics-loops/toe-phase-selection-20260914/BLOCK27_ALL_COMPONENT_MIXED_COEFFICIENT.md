# First mixed coefficient with arbitrary closed defect components

Personal proof candidate,2026-09-15. This extends the elementary-loop
calculation to all finite closed component shapes on the infinite cubic
lattice. It is not an all-order activity theorem or an independent review.
The functional below is defined by convergent sums and signed bounded
operators. A further finite-boundary/pressure-derivative identification is
explicitly separate from this result.

## 1. Component and filling measures

Work on Z^4, with the exact and coexact two-form projections P,Q=I-P.
Their Fourier multipliers have norm1 almost everywhere, and

    P=d_1 H_1^-1 d_1*, Q=d_2* H_3^-1 d_2.

Every finite integer conserved electric component j has a finite integer
two-form filling S with d_1*S=j. Its l1 mass is m=||j||_1. The coordinate
strip construction gives

    ||S||_1<=4m^2,

with support in the component's bounding box. Every finite closed magnetic
three-form component q similarly has n with d_2n=q and ||n||_1<=4m^2,
m=||q||_1: apply the same construction to the conserved dual one-current
and dualize its plaquette filling. This is an INFINITE-lattice construction.
It does not silently replace the relative-boundary filling in a finite box.

Choose odd filling rules and average their pushforwards under the384 signed
coordinate permutations. These are marks of one component, not384 distinct
physical components. Reversing a component reverses its fill. The real
physical source and integer mixed phase are independent of the mark:

    PS is fixed by j, Qn is fixed by q,
    exp[2pi i N<n,PS>] is unchanged by integer filling changes.

Use positive component measures nu_e,nu_m that include all translations,
all shapes, both signs with weight1/2, and the normalized filling marks.
The self-weights per unoriented shape are

    w_e(j)=exp[-g^2<j,H_1^-1j>/2]=exp[-g^2||PS||^2/2],
    w_m(q)=exp[-2pi^2 beta<q,H_3^-1q>],
    g=N/sqrt(beta), b=2pi sqrt(beta), c=2pi N=g b.

Thus integrating an even function against nu_e counts an unoriented
component once with weight w_e. The separate factor2 for its orientation
sum remains in the formulas below. Let nu_e^(1/2),nu_m^(1/2) denote the
same marked measures with the self-weights replaced by their square roots.

The infinite measures have infinite total mass because there are infinitely
many translations. The anchored moments, not their total mass, are finite.

## 2. A direct anchored-moment bound

For either species and integer r>=1 define

    M(r)=sup_i integral |s(i)| ||s||_1^(r-1) nu(ds),

where s denotes its two-form filling. Superscript1/2 means the half-weight
measure. Each component support graph has degree at most14: for electric
edges use a common endpoint, and for magnetic three-cells a common four-cell.
A connected support of size k anchored at a specified cell has at most
14^(2(k-1))=196^(k-1) encodings, by a deterministic depth-first traversal
of a spanning tree. Choosing nonzero integer values of total mass m on k
cells gives2^k binom(m-1,k-1) choices. Summing over k yields the upper bound

    sum_{k=1}^m 196^(k-1)2^k binom(m-1,k-1)
       =2*393^(m-1).                                   (2.1)

Closure only reduces this count. If a marked filling of mass m contains
the given two-cell i, at least one component cell lies within distance12m
of i, a deliberately loose cover of the bounding-box/dual shifts. The
number of potential anchored component cells is at most

    C_anchor m^4, C_anchor=4*25^4=1562500.

Here a radius12m cube has at most(24m+1)^4<=25^4m^4 lattice origins, and
there are four orientations of a one-cell or a three-cell. Normalized marks
do not increase this bound. The full-space Hodge spectral bound H<=16I
gives H^-1>=I/16 on these finite-support energy forms. Hence

    w_e^(1/2)<=exp[-t_e m], t_e=g^2/64,
    w_m^(1/2)<=exp[-t_m m], t_m=pi^2 beta/16.             (2.2)

Since |s(i)| ||s||_1^(r-1)<=(4m^2)^r,

    M^(1/2)(r)
      <=[2 C_anchor 4^r/393]
          sum_{m>=1} m^(2r+4)[393 exp(-t)]^m.            (2.3)

It is finite if t>log393. The explicit sufficient conditions

    beta>=16, N^2/beta>=512                              (2.4)

give t_m>=pi^2>9 and t_e>=8, and suffice for every finite r. They are
conditions for this coefficient estimate, not an assertion of a physical
phase in the whole range(2.4). No optimal threshold is claimed.

All subsequent estimates use moments through order7. Full-weight moments
are bounded by the corresponding half-weight moments.

## 3. Local filling frames and a summable nonlinear cross kernel

Define bounded two-form operators

    K_e=integral S tensor S nu_e(dS),
    K_m=integral n tensor n nu_m(dn).

Their absolute row and column sums are bounded by M_e(2),M_m(2).
Translation and signed cubic covariance hold after mark averaging. They
are absolutely summable matrix convolutions; their Fourier matrices are
continuous and scalar at0. These frame operators are mathematical
coefficient objects, not physical field covariances.

For theta(S,n)=c<n,PS>, put C(S,n)=cos(theta)-1 and

    K_eC=integral S tensor S [integral C(S,n) nu_m(dn)] nu_e(dS),
    K_mC=integral n tensor n [integral C(S,n) nu_e(dS)] nu_m(dn).

Both are nonpositive quadratic forms. Using |C|<=theta^2/2 gives

    ||K_eC||_Schur <=(c^2/2) M_m(2) M_e(4),
    ||K_mC||_Schur <=(c^2/2) M_e(2) M_m(4).              (3.1)

Here the Schur norm is the larger of the absolute row/column sums. For
example, the inner integral is at most(c^2/2)<PS,K_mPS>, which is at most
(c^2/2)M_m(2)||S||_1^2. Summing the outer rank-one row gives(3.1).

The sine kernel between the physical source directions is decomposed as

    K_em=integral sin(theta) S tensor n nu_e(dS)nu_m(dn)
         =c K_e P K_m+R_em,                             (3.2)

where the first term is defined as a signed bounded operator. The
remainder is an absolutely summable convolution and obeys

    ||R_em||_Schur <=(c^3/6) M_e(4) M_m(4).              (3.3)

To see this, use |sin(theta)-theta|<=|theta|^3/6. For a fixed row i,
sum the absolute values over the output coordinate to obtain an inner
integral with ||n||_1 |<n,PS>|^3. Since

    |<n,PS>|<=||n||_1||S||_1,

this inner integral is at most

    ||S||_1 <PS,K_m^(2)PS>
       <=M_m(4)||S||_1^3,
    K_m^(2)=integral ||n||_1^2 n tensor n nu_m(dn).

The outer row sum is M_e(4). Interchanging the species proves the column
bound. No absolute row bound for P is used.

## 4. The normalized mixed source functional

For a real two-form test h write x=Ph,y=Qh,

    U_S=g<S,x>, V_n=b<n,y>.

The first mixed component functional is the orientation-summed source
coefficient, normalized by its value at h=0:

    T(h)=4 integral C(S,n)[cosh(U_S)cos(V_n)-1] dnu_e dnu_m
          -4 integral sin(theta) sinh(U_S)sin(V_n) dnu_e dnu_m.  (4.1)

The sine term is defined using(3.2), not by an unproved absolute double
sum. More precisely split sin(theta)=c<n,PS>+[sin(theta)-theta]. The
first term factors into an inner product through P; the second converges
absolutely under the estimates below. This agrees with the limit of
finite cutoffs taken in those bounded-operator factors. A theorem about
arbitrary orders of conditionally convergent cutoffs is not asserted.

Its quadratic part is

    T_2(h)=2g^2<x,K_eC x>-2b^2<y,K_mC y>
             -4g b<x,[cK_e P K_m+R_em]y>.                (4.2)

The activities in nu_e,nu_m already include both self-weights; no extra
w_e w_m factor is placed outside(4.1) or(4.2).

## 5. Large components cannot be bounded by a local complex strip

An estimate exp(|U_S|)<=exp(g||S||_1||h||_infinity) by itself is unusable:
the filling area is quadratic in component mass. Instead retain its actual
Coulomb self-energy. Completion of a scalar square gives

    w_e exp(|U_S|)
      <=exp(||h||_2^2) w_e^(1/2).                       (5.1)

Indeed |U_S|<=g||PS||||h||_2, and -a^2/2+aH<=-a^2/4+H^2.
The resulting half-activity still has every anchored moment in(2.3).
This is a uniform bound for bounded ||h||_2. It neither asserts a uniform
complex strip for the local filling expansion nor ignores arbitrarily
large components. The magnetic source stays trigonometric and needs no
corresponding growing exponential.

For a rank-one frame and k>=1, Holder gives

    integral |<s,z>|^k nu(ds)<=M(k)||z||_k^k             (5.2)

when these anchored moments are finite. Weighted versions follow by
replacing M(k) by M(k+l) for an additional factor||s||_1^l.

For the C term, Taylor's theorem bounds the nonquadratic remainder by a
constant times exp(|U|)(|U|^4+|V|^4). Combining(5.1), the inner theta^2
bound, and(5.2) with moments through order6 yields

    |remainder_C|<=C_H[||x||_4^4+||y||_4^4],            (5.3)

for ||h||_2<=H. Constants depend on the fixed parameters and the displayed
finite moments, not on a spatial cutoff.

For the linear part of the sine kernel define

    F_e(x)=integral S sinh(g<S,x>) nu_e(dS),
    F_m(y)=integral n sin(b<n,y>) nu_m(dn).

Their linear parts are gK_e x and bK_m y. The scalar inequalities
|sinh u-u|<=|u|^3 exp(|u|)/6 and |sin v-v|<=|v|^3/6, followed by a
weighted absolute-frame Schur bound, give

    ||F_e-gK_e x||_2<=C_H ||x||_infinity^2||x||_2,
    ||F_m-bK_m y||_2<=C_H ||y||_infinity^2||y||_2.        (5.4)

The required weighted frame norm is M^(1/2)(4). Since ||P||_2<=1, these
bounds control the error in c<F_e,P F_m>.

For the sine-minus-linear remainder, use

    |sinh(U)sin(V)-UV|
       <=C exp(|U|)[|U|^3|V|+|U||V|^3]
       <=C exp(|U|)[|U|^4+|V|^4].

At fixed S, the inner integral of |<n,PS>|^3 is at most
M_m(3)||S||_1^3, using a weighted frame exactly as in(3.3).
The version with the species interchanged also holds. Equations(5.1)-(5.2)
therefore bound this source remainder with moments through order7 by
C_H(||x||_4^4+||y||_4^4). These estimates justify the nonlinear factors
and the convergences prescribed after(4.1).

## 6. Macroscopic limit of the coefficient

For a smooth compactly supported real continuum two-form f, set
h_a(p)=a^2 f(a midpoint(p)). Discrete Fourier Poisson summation gives
||hhat_a||_L1=O(a^2), so

    ||Ph_a||_infinity+||Qh_a||_infinity=O(a^2),
    ||Ph_a||_2+||Qh_a||_2=O(1),
    ||Ph_a||_4^4+||Qh_a||_4^4=O(a^4).

Equations(5.3)-(5.4) and the remainder estimate imply

    T(h_a)-T_2(h_a)=O(a^4).                             (6.1)

All absolutely summable coefficient matrices in(3.1)-(3.3) have continuous
Fourier transforms. Signed cubic covariance forces each zero-frequency
matrix to be scalar on the six two-form orientations: a coordinate
reflection kills an off-diagonal entry, and a permutation equates the
diagonal entries. Thus write

    K_e(0)=k_e I, K_m(0)=k_m I,
    K_eC(0)=a_e I, K_mC(0)=a_m I, R_em(0)=r I.

In the cross term, the leading scalar matrices give

    P(k)[c k_e k_m P(k)+rI]Q(k)=0.

The continuous remainders tend to0 in operator norm as k->0. Fourier
concentration of h_a and the ordinary Hodge-symbol limit consequently give

    T(h_a) -> 2g^2 a_e ||P_cont f||_2^2
                 -2b^2 a_m ||Q_cont f||_2^2.            (6.2)

The constants a_e,a_m are finite and nonpositive. They are strictly negative
because elementary loops are included with positive self-weight and their
mixed cosine kernel has a strictly negative row sum. This is a quadratic
coefficient limit with no surviving mixed P-Q term. It includes arbitrary
finite closed component shapes, not merely elementary plaquettes.

The limiting diagonal constants a_e,a_m do not depend on the chosen filling marks. Physical phases,
PS and Qn were already invariant. Also a finite difference of two fillings
with the same current/charge has zero total two-form area: its finite
Fourier transform obeys k contraction T(0)=0, or k wedge T(0)=0, for every
k, which forces T(0)=0. Thus zero-frequency frame contributions are
unchanged by a different integer filling rule. This assertion concerns the
limiting diagonal constants; individual pieces of the signed cross
decomposition need not be separately invariant under a mark change.

## 7. Exact scope and next obligation

This proof proposes a well-defined infinite-kernel mixed component
functional and its macroscopic quadratic limit. It does not establish a
nonzero convergence radius for the complete component expansion, or justify
evaluating that expansion at physical activities1. It also does not yet
prove that the functional is the volume-uniform mixed activity derivative
of the original finite-free-boundary pressure. Matching those boundary
limits requires the actual cochain projections and source sequence, not
just pointwise replacement by an infinite Green function.

The next useful step is a genuine signed resummation/nonlinear estimate,
with any thermodynamic interchange explicit. More finite-order coefficients
would not by themselves complete that step. Independent review and new
finite frame/source challenges remain distinct requirements. The accompanying
finite frame checker passed its listed algebraic and source-energy tests;
independent review is still pending. No public PR, new
primitive, selected physical coupling, or axiom wall is claimed here.
