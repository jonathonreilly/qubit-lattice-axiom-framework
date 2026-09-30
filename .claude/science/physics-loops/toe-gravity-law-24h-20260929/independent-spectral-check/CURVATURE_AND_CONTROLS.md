# Curvature recurrence and independent Fourier controls

Before author coefficient comparison, independently expand inverse metric
B_r=(-h)^r and define S_lij=partial_i h_jl+partial_j h_il-partial_l h_ij.
Then Gamma_(r)^k_ij=(B_(r-1))^kl S_lij/2 for r>=1, and

 Ricci_(n)ij=partial_k Gamma_(n)^k_ij-partial_j Gamma_(n)^k_ik
   +sum_(r+s=n)[Gamma_(r)^k_kl Gamma_(s)^l_ij
                         -Gamma_(r)^k_jl Gamma_(s)^l_ik].
 R_(n)=sum_(r=0,...,n-1) B_r^ij Ricci_(n-r)ij.

The volume coefficients needed for potential degree<=4 are
 v0=1, v1=t/2, v2=t^2/8-tr(h^2)/4,
 v3=t^3/48-t tr(h^2)/8+tr(h^3)/6.
Thus Cpotential_(n)=-K sum_(r=0,...,n-1)v_r R_(n-r), n=1,...,4.
This explicitly defines every placement/coefficient once the spectral derivative
and pointwise product are fixed. The standard continuum parent, with its own
momentum convention and unit coefficients, is also exhibited in Arnowitt,
Deser and Misner, The Dynamics of General Relativity, equations3.14–3.15:
https://arxiv.org/html/gr-qc/0405109v1 . Those exact equations were inspected
after the earlier independent sign/kinetic derivation was frozen. This contact
is historical formula verification, not framework premise adoption or the
missing finite-cutoff proof. No asymptotically flat boundary theorem is used
on the present periodic torus.

The small control script was priced below1second/50MB; it uses finite rational
Fourier dictionaries and integer-valued complex coefficients, with no author
code. For F=mean(N q^2/2), H=mean(M p^2/2) evaluated at N=M=q=p=cos(x),
the full-grid PB is3/8. Projecting both functional gradients to the input band
|k|<=1 gives1/4. This demonstrates why setting absent high variables to zero
before differentiating tests a different bracket. It does not say that a
separately defined projected canonical bracket fails its own Jacobi identity.

For the one-dimensional metric-weight-two action L_xi q=xi Dq+2(Dxi)q,
take q=1, xi=exp(iJx), eta=exp(ix) on n=2J+1 sites. Direct wrapped Fourier
matrix multiplication gives

 ([L_xi,L_eta]-L_(xi Deta-eta Dxi))q
       =2(2J+1)(J-1) exp(-iJx).

Pairing with momentum exp(iJx) gives a nonzero canonical generator defect for
J>=2. Complexification is only a compact way of displaying a real polynomial
identity failure. This is the specified full-zone generator control, not an
obstruction to other finite-grid symmetries. Increasing the carrier cutoff so
all intermediate modes remain unaliased restores the same tested identity.
These controls do not replace universal coefficient transfer or complete
normal-constraint/Jacobi checks, which remain pending comparison.
