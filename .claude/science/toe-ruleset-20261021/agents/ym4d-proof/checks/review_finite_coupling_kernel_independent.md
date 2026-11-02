# Independent reconstruction before author-checker exposure

Frozen target: `FINITE_COUPLING_KERNEL_ASTRA.md`, SHA256
`c85ce075fdae1249b520089a462c8cf3107c0b26901d4dcd55a78c48b78ebc8b`.
Reviewer is a separate-context, same-family Astra/max reviewer with no author
role in this unit. This file precedes inspection of the author's scientific
Python, raw stdout/stderr, results, resource records, and amendment. The source
itself was read completely, including its aggregate numerical claims, and the
read manifest was read. Independence therefore concerns reconstruction and
implementation, not blindness to the claimed result or its reported aggregates.

## Analytic reconstruction

1. Write `M+=G A0`, `M-=B0 G^-1`. The traceless stationary equation for
   `W=G exp(Y)` is `P0(exp(-Y) A0-B0 exp(Y))=0`. Splitting off `-2Y`
   leaves an odd cubic exponential remainder and two perturbative factors.
   Differentiated power series give the two FK5 bounds in complex HS norm.
   At `r=2 eta` the map is strictly contracting; at `r=8 eta_N` its derivative
   remains below one. In two overlapping charts, `||G1^-1 G2-I||HS<=2 eta_N`;
   the logarithm series and the product exponential put the second saddle
   within that larger ball. No global principal traceless logarithm is assumed.

2. A holomorphic invariant top form on SL(N,C), normalized by probability
   Haar at identity, is closed after multiplication by the entire phase.
   Stokes on `[0,1] x SU(N)` translated by `G exp(sY)` proves the full-cycle
   identity. The scalar difference of the recentered two matrices is needed:
   it yields `lambda tr(X^3)/(6N)` in the phase deficit. It is absent for
   SU(2), but is not absent for SU(3).

3. On SU(N), eigenangles close to zero sum to zero. Away from that cap,
   `tr(I-Re U)>=1/(8N^2)`, whereas `|tr(U^-1-U)|<=2N`. This proves the
   deliberately loose `16N^3` global odd bound, including the center. The
   real-part sector estimate has spare margin: `cos(pi/6)-1/8>1/2`.
   The complex symmetric Hessian differs from `I/N` in operator norm by
   at most `4 eta/N`; the bilinear trace bound also controls complex colour
   vectors, not only real directional quadratic forms.

4. The exponential-coordinate Haar density is the determinant of `dexp`.
   The adjoint trace vanishes, giving the even full-adjoint determinant in
   FK12. The quadratic term follows from `Tr(ad X)^2=2N tr X^2`.
   On the local symmetric ball the cubic times this density integrates to
   zero exactly. The finite exponential remainder is bounded by Gaussian
   moments of degrees 2, 4 and 6, each giving `|t|^(-D/2-1)` after its
   displayed powers of t. The choice of r leaves at least `1/(8N)` in the
   Gaussian exponent. Outside the chart, a principal logarithm of HS norm
   less than r would be traceless; therefore the stated positive global
   drop applies. These facts justify a finite uniform estimate, not only
   a formal asymptotic series. The determinant branch and Gaussian factor
   are compatible with probability Haar and HS Lebesgue coordinates.

5. The simultaneous parameter polydisc stays strictly inside the larger
   parameter ball. At real `t>=2t0`, the disc of radius `t/4` has modulus
   at least `3t/4>t0` and angle at most `arcsin(1/4)<pi/6`. Joint Cauchy
   estimates therefore justify every fixed mixed derivative in FK16.

6. The S4-prime contour uses two internally trivial blocks and exactly one
   crossing face, so every baseline word equals the coarse link, for arbitrary
   holonomy and for T=2 with the far seam excluded. Its exact maximum length
   is `L+4(L-1)=5L-4`. A support is contained in two blocks' internal edges
   plus their joining face, with at most `(8L-7)L^3<8L^4` positive fine links.
   Every internal fine link can belong to at most the eight incident coarse
   readers; crossing edges belong to their own reader. Inverse words reverse
   order and invert each factor. In left fine coordinates their negative
   edge is `U0^-1 exp(-x)`, not `exp(-x) U0^-1` and not an adjoint at complex x.
   A fixed anchored scalar derivative has at most eight summands; its other
   indices have at most `D n_c` choices each. This gives the FK22 factor.

7. CB14 uses the same left free-link chart, original source epsilon, and
   fixed kappa. Its contraction gives `||a(u,epsilon)||sup<=4RG delta_V` for
   `||epsilon||sup<rho_star` and `delta_V<=delta_star`. The extra restriction
   `delta_V<=a/(16RG)` in FK23 places that image in the new scalar theorem's
   a/4 ball. Cauchy's source bound follows without asserting locality of this
   composed map or an integrated denominator. The scalar theorem itself
   has no CB dependency.

## A distinct determinant derivation of FK24

Work at one aligned family after unitary recentering to G=I. Set
`q=avg theta_tau` and `v=avg ||theta_tau-q||HS^2`. Differentiating stationarity
gives `Wstar'=q`. At the aligned point the recentered average satisfies
`S'=0`, and differentiating its trace twice gives `tr S''=-v`. For an
HS-orthonormal su(N) basis, completeness gives
`sum_a T_a^2=-(D/N) I`. Thus

    Tr_colour H'' = -(1/N) tr[S'' sum_a T_a^2]
                   = (D/N^2) tr S'' = -D v/N^2,
    (log A)'' = -(1/2) Tr_colour(H^-1 H'') = D v/(2N).

Here `H'=0` and `H^-1=N I` at alignment. This derives the coefficient
directly and does not infer it by taking a limit in the author's finite-t
Hessian. Separately differentiating the actual Haar integral and using the
common-path invariance gives `Hess(-log k)=t[||q||^2+(1-c_N)v]/N`.
Subtracting the tree and the above determinant gives exactly FK24. The
separate coordinate-Haar Hessian is `N/6`, or `N^2/(6u)` in the F9 scaling.
FLOW's coordinate substitution multiplies a q-jet by `N^(q/2)`; the
additional tree-energy division by N belongs only to UL9. UL10 already
contains the positive half-log of the normalizer covariance determinant.

## Independent SU(3) diagnostic route

For scalar recentered matrices `E=(S+lambda)I`, `F=(S-lambda)I`, let
`p=t(S+lambda)/(2N)`, `q=t(S-lambda)/(2N)`. Expand the Weyl Vandermonde into
two permutation sums. Fourier projection onto determinant one selects a
common integer winding k for all angles. The one-angle Fourier coefficients
of `exp(q z+p/z)` are Bessel coefficients. After permutation summation,

    Z_SU(N)=sum_(k in Z) (p/q)^(Nk/2)
                         det[I_(k+i-j)(2 sqrt(pq))]_(i,j=0,...,N-1).

Changing p/q to q/p merely reindexes k. The measure is probability Haar:
at p=q=0 only k=0 survives and its determinant is one. The proposed
implementation uses this Fourier-determinant identity, not a two-angle grid
or the author's implementation. Scaling every Bessel entry by `exp(-z)`
keeps the expression finite, with outside factor `exp(N z-t S)`.

An independent Wick contraction in full HS coordinates gives
`E tr X^4=N^2(2N^3-5N+3/N)` and
`E (tr X^3)^2=-3N^2 D(N^2-4)` for covariance `N I`.
Consequently, at scalar S, the first coefficient is

    t E_t -> -D/(8S)-D(N^2-4) lambda^2/(24 S^3).

For SU(3) this is `-1/S-5 lambda^2/(3S^3)`, so
`t partial_lambda^2 E_t(t,1,0) -> -10/3`. The latter tests the nonzero
scalar SU constraint beyond SU(2), while the leading power is t^-4.
These are finite diagnostics, not certified values of the conservative t0
or a proof for all parameters.

No interacting integral, hard complement, all-depth source-reader sum,
continuum construction, or physical mass gap is established by this review.
