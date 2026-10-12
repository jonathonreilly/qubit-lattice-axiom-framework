# Independent infinite boundary-defect admissibility

This algebra is independent of any fitted V2 parameters. Work with the
dimensionless gamma measure rho_s(x)=x^(s-1)exp(-x)/Gamma(s), x>0, s>0,
and its positive Jacobi multiplication operator J. A physical inverse-length
variable would be mu=x/ell. Let J_delta=J+delta|e0><e0| with delta=b-s, and
define m0(z)=<e0,(J-z)^(-1)e0>=integral rho_s(x)/(x-z)dx.

The rank-one resolvent identity gives

\[
m_\delta(z)={m_0(z)\over1+\delta m_0(z)},\qquad
\rho_\delta(x)={\rho_s(x)\over|1+\delta m_0(x+i0)|^2}.
\]

The continuous density alone is not always the full spectral measure: any
real resolvent poles supply atoms. Its total mass including atoms is one,
since m_delta(z)=-1/z+O(1/z²). Thus this is a normalized positive spectral
measure, but nonnegative support must be checked separately before identifying
its eigenvalues with physical scalar masses. The static and Wightman kernels
must both use this new measure. Reusing the gamma force/noise formulas is wrong.

For delta<0, a negative eigenvalue exists precisely when
1+delta*m0(0-)<0 (including m0(0-)=infinity). The negative root is unique:
m0(z) increases strictly from zero to m0(0-) as z increases from minus
infinity to zero. Equivalently, a direct quadratic-form Cauchy–Schwarz bound
uses |psi0|² <= <psi,J psi> integral rho_s(x)/x dx. Therefore

\[
J_\delta\ge0\ \Longleftrightarrow\
\begin{cases}
b\ge s,&0<s\le1,\\
b\ge1,&s>1.
\end{cases}
\]

This differs from the N=3 positivity condition
b > s(s+4)/(s²+4s+6), obtained by the Schur complement of the lower block.
A positive finite matrix does not certify a physical nonnegative infinite
mass spectrum. Gamma Carleman determinacy fixes the unperturbed spectral
measure; the bounded rank-one perturbation preserves self-adjointness.

At the threshold s>1,b=1, delta=-(s-1), the candidate zero eigenfunction in
the original spectral representation is proportional to 1/x. It belongs to
L²(rho_s dx) exactly for s>2. In that case the new endpoint measure has a
massless atom of weight

\[
w_0={1\over\delta^2\int\rho_s(x)x^{-2}dx}
={s-2\over s-1}.
\]

For 1<s<=2 there is no zero atom; threshold infrared behavior still changes.
For 1<s<2 the continuum density scales as x^(1-s), rather than x^(s-1).
At s=2 the integrable borderline is proportional to 1/[x(log x)^2].
For s>2 it scales as x^(s-3) and the atom gives a separate long-range
massless contribution. Away from threshold with s>1, the low-x exponent is
unchanged but its normalization is changed by [1+delta/(s-1)]^-2.
For 0<s<1 and positive delta the low-x exponent changes to1-s; at s=1
logarithms replace a pure gamma density. These cases prevent inferring a
universal gamma static/noise power solely from a fitted finite-block s.

If b>1 and s>1, no massless atom or negative eigenvalue is present. There
are no isolated positive atoms for a finite delta because the unperturbed
gamma density is strictly positive throughout (0,infinity), giving nonzero
imaginary part to m0(x+i0). An endpoint pole can occur only at zero or below
the continuum. A future fitted result must be evaluated under these exact
conditions, not just the three eigenvalues.
