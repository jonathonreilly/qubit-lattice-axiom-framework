# Primary source checks during the personal block21 derivation

Conlon-Dabkowski, JSP192,101(2025), DOI10.1007/s10955-025-03478-x,
published PDF SHA256
ae24ac453a1e711ac5daa0a1b29025298ae1eb0facc52aba8c468f027dbb356e.
Pages14 and18 were rendered and visually inspected. These observations
do not constitute a review of the whole paper or a claim that its main
theorems are false. No author contact or external report was made.

1. Theorem3.1/eq3.17 on page14 displays a Riesz operator without the
   Laplacian inverse used in the neighboring formulas. The literal display
   cannot have the stated norm1 at p=2. Block21 specifies the inverse
   explicitly and derives its own periodic bound.

2. Equation4.28 on page18 asserts, for a general Brownian martingale
   terminal variable M and its quadratic variation Q, E exp(M)=E exp(Q/2).
   This equality is false for a random adapted integrand in general.
   A smooth bounded-integrand control is H_t=1 for0<t<=1 and
   H_t=tanh(B_1) for1<t<=2. With independent standard Gaussians
   G=B_1 and Z=B_2-B_1, its terminal value and quadratic variation are

    M=G+tanh(G)Z, Q=1+tanh(G)^2.

   Conditioning on G gives E exp(M)=E exp[G+tanh(G)^2/2]. Since the
   second factor is even, the difference from E exp(Q/2) is exactly

    Cov(cosh(G),exp[tanh(G)^2/2])>0.

   Strict positivity follows from the independent-copy covariance
   identity and the fact that both functions strictly increase with |G|.
   Thus the control is analytic; the separate positive one-dimensional
   quadrature receipt only checks its size. It has no divergent moments
   or failure of the bounded-integrand exponential-martingale condition.

   If Q<=C deterministically, the needed upper bound E exp(M)<=exp(C/2)
   follows instead from the exponential martingale exp(M-Q/2) and its
   expectation1. This can repair an argument that uses only that bound;
   it does not restore the displayed equality. The block21 Gaussianity
   proof uses finite-time source derivatives and finite-dimensional Gibbs
   inequalities, not equation4.28.

Page19's remark correctly notes a volume-dependent relaxation bound and
does not claim its bound tends to zero uniformly in volume. Block21 keeps
finite-time differentiation at fixed finite dimension, then develops a
separate stationary thermodynamic matching argument. It does not infer
uniform local equilibration from that volume-dependent estimate.
