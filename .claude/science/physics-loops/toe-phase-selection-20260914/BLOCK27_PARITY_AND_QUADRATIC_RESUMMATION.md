# Opposite orientations, physical sources, and the surviving quadratic kernel

Personal unfinished stretch,2026-09-15. This continues block27 rather than
opening another support PR. The target is the coupled finite-clock defect
law. The calculations below identify a concrete resummation mechanism and
its unresolved source/nonlinear estimates. They do not prove Gaussianity.

## 1. Component expansion of the actual coupled representation

Use the free-cubic coupled law at PR8133 revision
f8e7219b5e79bcb271bb3c1df635ecdeeb57dbe8. Decompose each nonzero conserved
integer electric current a and each closed integer magnetic charge q into
its connected support components. Each component can be grouped with its
negative; choose one representative of each such pair. The two orientations
are signs sigma,tau in{-1,1}. Local odd magnetic fillings are component-additive.

Two distinct components of the SAME species are compatible only when their
support adjacency permits the given component decomposition. There is no
extra electric/magnetic hard-core exclusion. The self-weights of components
j and q are

    w_e(j)=exp[-N^2<j,G_1j>/(2beta)],
    w_m(q)=exp[-2pi^2 beta<q,G_3q>].

The exact pair factors, before summing orientations, are

    electric/electric: exp[-sigma tau J_e],
       J_e=(N^2/beta)<j,G_1j'>;
    magnetic/magnetic: exp[-sigma tau J_m],
       J_m=4pi^2 beta<q,G_3q'>;
    electric/magnetic: exp[i sigma tau theta],
       theta=2pi N<n(q),d_1G_1j>.                         (1.1)

This is an expansion of the specified coupled sum, which has complex
individual terms. It is not a positive joint law for the two defect species.
Self-energies, hard-core restrictions and every mixed phase are retained.

The next two-component calculation is an exact coefficient test: attach
formal activities z,w to two chosen unoriented components and set the other
component activities to zero. This extracts a coefficient of the component
expansion. It does not claim that these two components dominate the actual
model, or that a lowest-loop truncation has a volume-uniform error bound.

## 2. Orientation pairing improves the source-free pair but not every source

Give the two signs test phases exp(i sigma s+i tau t). For a mixed pair,
direct summation yields

    sum_{sigma,tau} exp[i sigma s+i tau t+i sigma tau theta]
      =4[cos(theta)cos(s)cos(t)-i sin(theta)sin(s)sin(t)].  (2.1)

The coefficient of zw in the logarithm of the two-component partition
polynomial is therefore

    4[(cos(theta)-1)cos(s)cos(t)
         -i sin(theta)sin(s)sin(t)].                     (2.2)

At s=t=0 it is4(cos(theta)-1), quadratic in a small distant coupling.
However its mixed source derivative at0 is -4i sin(theta), which is
LINEAR to leading order in that coupling.

For a compatible same-species pair,

    sum_{sigma,tau} exp[i sigma s+i tau t-sigma tau J]
      =4[cosh(J)cos(s)cos(t)+sinh(J)sin(s)sin(t)],         (2.3)

and its connected coefficient is obtained by replacing cosh(J) by
cosh(J)-1 in the first term. Its mixed source derivative is4sinh(J),
again linear at small coupling. An incompatible same-species pair has no
two-component term and instead contributes the hard-core subtraction.

Thus orientation cancellation in the vacuum coefficient cannot be reused
unchanged after differentiating sources. These are deliberately general
component sources. Their exact relation to the physical full-flux source
still has to be proved before interpreting a derivative as an observable.

## 3. Same-model elementary loops exhibit the precise summability distinction

Take the infinite four-dimensional cubic Hodge operator. Let P=d_1H_1^-1d_1*
be the exact two-form projection, defined by its bounded Fourier multiplier;
Q=I-P is the coexact projection. The zero-frequency point is irrelevant
to the infinite-volume multiplier. For elementary plaquettes p,p', choose

    j=d_1* e_p,   q=d_2 e_p',   n(q)=e_p'.

They are legitimate finite component shapes. The phase is filling-independent
modulo2pi for the integer current, even if another odd filling is used.
Their cross kernel is theta(p,p')=2pi N P(p,p'). Their same-species
interaction kernels are respectively(N^2/beta)P(p,p') and4pi^2 beta Q(p,p').
For disjoint plaquettes, Q(p,p')=-P(p,p'). This last equality is an
infinite-volume statement; a finite torus also has a harmonic projection.

Translation/cubic symmetry and rank(P(k))=3 for k!=0 give P(p,p)=1/2.
Projection and Parseval give the stronger square-summability identity

    sum_{p'} |P(p,p')|^2=P(p,p)=1/2.                    (3.1)

For the same orientation12, the diagonal multiplier is

    P_12,12(k)=[4sin^2(k_1/2)+4sin^2(k_2/2)]
                /sum_{j=1}^4 4sin^2(k_j/2).             (3.2)

It tends to1 along the k_1 axis and to0 along the k_3 axis. If its real-space
kernel were absolutely summable, its Fourier series would be continuous,
contradicting these directional limits. Hence

    sum_x |P_12,12(x)|=infinity,
    sum_x |P_12,12(x)|^2<infinity.                       (3.3)

No asymptotic Green-function differentiation is required for this argument.
In particular, the scalar Green-function estimate O(|x|^-4) in its remainder
must not be differentiated twice and then called an asymptotic proof of(3.3).

For each fixed finite N, |cos(theta)-1|<=theta^2/2 proves absolute
summability of the mixed vacuum pair coefficient. Since an ell^2 sequence
tends to zero, sin(theta)/theta tends to1 in the distant tail. Equation(3.3)
therefore proves non-absolute-summability of its same-orientation mixed
source coefficient. Removing finitely many nearby incompatible shapes
does not change this conclusion. For same-species pairs, cosh(J)-1 is
bounded by J^2 cosh(||J||_infinity)/2, while sinh(J)/J tends to1. The same
vacuum/source distinction follows.

This rejects only an estimate that takes absolute values of EVERY distant
pair source kernel before summation. It does not reject signed summation,
quadratic resummation, multiscale analysis, or cancellations in the actual
physical-source combination. Nor does it establish a lower bound on an
actual physical fourth cumulant.

There is also a direct finite-volume failure of an absolute Neumann-series
criterion. Let C_L be the periodic same-orientation convolution with
symbol(3.2), assigning0 to its zero mode, and let A_L be its entrywise
absolute matrix. Its nonnegative constant-vector eigenvalue is the row sum
S_L=sum_x|C_L(x)|. Each fixed kernel entry converges to the infinite Fourier
coefficient by Riemann summation of a bounded multiplier with only a
point singularity. Fatou and(3.3) therefore imply liminf S_L=infinity.
For every fixed z>0, the Neumann series in z A_L eventually fails to
converge on the constant vector. In contrast, ||C_L||_2<=1, so the signed
series in z C_L converges uniformly for0<z<1. This isolates a norm choice
that loses the cancellations; it is not failure of the actual gas.

## 4. Exact quadratic resummation template

The operator P is bounded on ell^2 even though its absolute-entry kernel
is not summable. At the quadratic level, for s>-1,

    (I+sP)^-1=I-[s/(1+s)]P.                             (4.1)

A two-species version is equally explicit. For finite2x2 matrices A,B,
let K=A tensor P+B tensor Q. Whenever I+A and I+B are invertible,

    (I+K)^-1=(I+A)^-1 tensor P+(I+B)^-1 tensor Q.       (4.2)

For the illustrative complex-symmetric pair-kernel form

    A=[[a,-i c],[-i c,0]], B=[[0,0],[0,b]],
    a,b>=0, c real,

the Hermitian part of I+K is at least I. Hence I+K is invertible and
||(I+K)^-1||_2<=1 in every finite Fourier fiber, uniformly in the infrared.
Its exact-sector2x2 determinant is1+a+c^2. Neither a mass regulator nor
an absolute-row-sum bound is needed for this algebra.

Equation(4.2) is a template for retaining the signed quadratic kernels.
The coefficients a,b,c have NOT been identified with fully renormalized
couplings of the clock law. A complex quadratic inverse alone is not a
positive auxiliary probability or a proof of the nonlinear continuum limit.
Its role is to show that the specific failure of an absolute-value estimate
has a concrete possible repair.

## 5. Remaining decisive work

1. Match the complete physical flux/score source to the component expansion,
   including the real versus imaginary source directions and contact terms.
2. Extract the actual quadratic term with controlled coefficients and retain
   its signed Hodge kernels rather than taking an absolute row norm.
3. Bound the remaining multi-component/large-field terms uniformly in volume
   in a norm that contracts under scaling or directly controls higher source
   cumulants. Source-free pair summability is not that bound.
4. Identify a physical infinite-volume state and a nondegenerate covariance;
   the source transformation must concern that same state.

These are open proof obligations, not assumed conclusions. The existing
spectral/covariance milestone remains the strongest fixed-clock proposal.
The point of this calculation is to replace a vague coupled-defect obstacle
by a particular quadratic term to preserve and a nonlinear estimate to try.

## Primary reading and finite scope

Lawler-Limic, *Random Walk: A Modern Introduction*, local PDF and
https://www.math.uchicago.edu/~lawler/srwbook.pdf: printed pages81-86 and
125-129 were read for Green-function normalization and difference estimates.
Corollary4.3.3 states a second-difference upper bound, not the sharper
angular second-derivative asymptotic considered during the search. None of
that unproved sharper asymptotic is used in(3.1)-(3.3).

Finite Fourier/symbol and orientation checks now pass. Direct four-sign
sums challenge the connected/source coefficients; full exterior-product
symbols challenge the split complex inverse; and five periodic sizes check
Parseval, the harmonic correction and vacuum/source row sums. Their scope
is normalization and source algebra, not convergence of the complete gas.
