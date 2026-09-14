# Next nodal term: provisional derivation and a nonuniform numerical lesson

If the low squared energy near a node is q^T G q+C_3(q)+O(|q|^4), the
occupied energy has next term -C_3(q)/(2sqrt(q^T G q)). With the Fourier
convention in BLOCK16_DERIVATION.md,

```text
Fourier[1/sqrt(q^T G q)](r)
 =1/[2pi^2 sqrt(det G)(r^T G^(-1)r)].
delta f_hat(r)=i exp(-ir dot k_alpha)/(4pi^2 sqrt(det G))
             C_3(partial_r)[1/(r^T G^(-1)r)].
```

For A=G^-1, u=Ar and v=r^T A r, the derivative used in the checker is

```text
partial_i partial_j partial_k v^-1
 =-48u_i u_j u_k/v^4
  +8(A_ij u_k+A_ik u_j+A_jk u_i)/v^3.
```

This is a degree-minus-five Fourier term and hence an order-L^-2 twist
energy correction. A cubic Taylor-jet calculation in the aligned carrier
matches the known quadratic metric and is separately challenged against
the direct four-by-four Hamiltonian at shrinking displacements. Its cubic
coefficients use floating arithmetic, not exact interval certification.

The next correction does not uniformly improve every moderate-size sample.
For example, at L=16 and twist(pi,pi,pi), the first-term residual is small
by cancellation, and adding the derived second term makes the absolute
residual larger. At larger sampled sizes the remaining residual times L^3
stays of order tens. This is compatible with, but does not prove, the next
asymptotic order. All samples and the unfavorable comparisons are preserved.
The finite reciprocal cutoffs and unquantified remainder constants prevent
claiming a certified numerical rate or globally best finite-size predictor.

Next review the coefficient convention and dyadic degree-three remainder
analytically, and obtain exact coefficient/tail enclosures only if that
precision helps the interacting holonomy reduction. It is not necessary to
turn this free finite-size refinement into a new theory or a separate PR
before the more load-bearing charged phase questions are addressed.
