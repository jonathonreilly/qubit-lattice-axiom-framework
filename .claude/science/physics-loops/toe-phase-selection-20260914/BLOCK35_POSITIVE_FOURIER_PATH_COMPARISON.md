# Block35: all-coupling path comparison by positive Fourier coefficients

Personal derivation, 2026-09-15; independent review pending. This is a
stronger route to path-independent static thresholds than Block33's
curvature comparison: it uses beta>0 and finite N only. The quantitative
Coulomb-form bound still requires its separate large-beta source hypotheses.

## 1. Positive electric-coordinate transfer

For the same finite spatial clock box, put A=V^(1/2) C^(1/2), so

 T=A A^*, Ttilde=A^* A=C^(1/2) V C^(1/2).               (1)

All operators are invertible. In the Fourier basis, C is diagonal with
strictly positive products of the one-link coefficients c_k. V is a
convolution matrix whose coefficients are nonnegative: each plaquette
Villain weight has coefficients c_r>0, and their product expands as

 Vhat(m)=sum_(d1* s=m modN) product_p c_(s_p).           (2)

Thus Ttilde is entrywise nonnegative. Its largest eigenvalue lambda0 is
simple because T has a strictly positive configuration-space kernel.
Perron-Frobenius supplies a normalized nonnegative Fourier-coordinate
eigenvector Psi0. The original Perron vector is
Omega0=A Psi0/sqrt(lambda0), up to its positive overall phase.

For a spatial character U_j, define v_j=A^* U_j Omega0. Since U_j commutes
with V and shifts Fourier coordinates,

 v_j=C^(1/2) V U_j C^(1/2) Psi0/sqrt(lambda0).           (3)

Every Fourier coordinate of v_j is nonnegative. This assertion concerns
these transformed insertion vectors; it does not assume that sqrt(V) has
nonnegative Fourier coefficients.

For every integer time T>=1,

 W_j(T)=lambda0^(-T) <v_j,Ttilde^(T-1) v_j>.            (4)

This follows from (AA*)^T=A(A*A)^(T-1)A*. The distinction between T and
T-1 is essential.

## 2. A fixed surface bounds coefficient ratios

Suppose j-k=b=d1* S for a finite integer spatial plaquette field S. On Z3
every finite conserved difference b has such a finite filling. Work in
spatial boxes containing its support. Define

 R(S)=product_(p in support S) max_(r in Z_N) c_r/c_(r+S_p).

It is finite and at least1. Because c_r=c_(-r), the maximum for S_p and
-S_p agrees. In (2), changing the plaquette current variable s to s+S
is a bijection between the fibers for m and m+b, and each product weight
changes by a factor between R(S)^(-1) and R(S). Therefore

 R(S)^(-1) Vhat(m)<=Vhat(m-b)<=R(S) Vhat(m)             (5)

for every m. If a coefficient vanishes, the shifted one vanishes too by
the same bijection, so no division by an unsupported coefficient is made.

Equation(3), term by term, now gives

 R(S)^(-1) v_k <= v_j <= R(S) v_k                     (6)

in the Fourier coordinate order. Since every power Ttilde^(T-1) is
entrywise nonnegative, (4) implies

 R(S)^(-2) W_k(T)<=W_j(T)<=R(S)^2 W_k(T), T>=1.         (7)

The constant depends only on the fixed filling and local positive couplings,
not the spatial box or time length. It may be very large, and no optimized
surface or continuum parameter estimate is claimed.

## 3. Infinite free state and common thresholds

Pass (7) through the matched free-boundary limit at each fixed T. All
correlations have positive spectral representations, hence their long-time
rates exist. The fixed multiplicative comparison proves equal rates for
j and k, at every beta>0 and fixed finite N. Positivity at finite T follows
also from the transformed nonnegative vectors and positive definiteness;
the infinite positivity and finite rate follow from Block32's inverse
moment bound, which gives E_visible<=log K(j) by Jensen for the spectral
probability measure.

This removes the smallness premise from the path-independence input of
Block34's common transfer-space construction. Under the additional curvature
conditions, the sharper separation-uniform Coulomb upper bound continues to
hold. At other couplings no such separation bound is inferred from R(S),
K(j), or path independence alone. In particular a confining phase can still
have a path-independent static energy growing with endpoint separation.

The weaker square-root-log comparison of Block33 remains a valid separate
all-real-source estimate. It is no longer the only route to identifying a
common static threshold. No axiom, primitive or physical law is changed.


Five finite square systems and ten surface comparisons pass the direct
Fourier/coefficient/insertion-vector checks. The initial full eigensolve at
N2,beta1.2 mixed nearly degenerate charge sectors, producing a spurious
negative Fourier component of about9.37e-13. Its exact source and failure
are preserved. Restricting to the algebraically known neutral Fourier sector,
then reconstructing and checking the full Perron vector and eigenvalue,
resolves this without changing tolerances or clipping coordinates.
