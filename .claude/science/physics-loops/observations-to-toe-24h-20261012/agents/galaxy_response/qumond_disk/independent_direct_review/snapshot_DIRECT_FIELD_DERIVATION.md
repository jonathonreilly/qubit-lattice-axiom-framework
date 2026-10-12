# Direct authorship: closing the algebraic-to-field gap

This chat took over scientific authorship at the user's request on October 12,
2026. The inherited protocol and source-only galaxy selection are unchanged.
The background author's unfinished code did not supply this implementation;
the only existing disk artifact was its forward contract. This derivation and
`direct_qumond_disk.py` are direct work in this chat. They are conditional
candidate calculations, with no retained or audit status and no novelty claim
for the established field equation.

The scientific question is whether the already fitted algebraic rotation rule
approximates the specified field equation on the same baryonic sources well
enough to transfer its parameters into the solar comparison. We first compute
the field at fixed parameters, before any new velocity residual or refit.
The underlying theory is the supplied [QUMOND equation](https://arxiv.org/abs/0911.5464v2).
Its equation does not follow from the rotation data alone.

## Personally reconstructed projection

Use the outward potential gradient U=grad(Phi_N) and A=nu(|U|/a0)U, with
laplacian(Phi)=div(A). Expand an axisymmetric, reflection-symmetric field as
A_r=sum a_l(r)P_l(c) and A_theta=sum b_l(r)partial_theta P_l(c), c=cos(theta).
The angular normalization gives

    a_l=(2l+1) integral_0^1 A_r P_l dc,
    b_l=(2l+1)/(l(l+1)) integral_0^1 A_theta partial_theta P_l dc.

The radial source is H_l=(r^2 a_l)'/r^2-l(l+1)b_l/r. The regular interior and
decaying exterior Green solution for l>=2 is

    phi_l= -[r^(-l-1) integral_0^r t^(l+2) H_l dt
             +r^l integral_r^infinity t^(1-l) H_l dt]/(2l+1).

Integrating each term by parts cancels the local r*a_l terms. Differentiation
then gives

    phi_l'=a_l-l(l+1)/(2l+1) (S_l+T_l),
    S_l=r^(-l-2) integral_0^r t^(l+1)[a_l+(l+1)b_l]dt,
    T_l=r^(l-1) integral_r^infinity t^(-l)[a_l-l b_l]dt.

The monopole has phi_0'=a_0; no zero-at-infinity condition is imposed on the
isolated MOND logarithmic monopole. At the equatorial plane, use the exact
upper trace A_R(R,0+) and subtract the summed solenoidal correction multiplied
by P_l(0). This avoids reconstructing that trace by a truncated scalar series.
Reflection symmetry includes the gas-sheet normal jump in the distributional
divergence; the transverse correction is continuous there.

The gradient check is analytic, independent of an expected numeric constant:
for A=grad[f_l(r)P_l(c)], a_l=f_l' and b_l=f_l/r. The two integrands become
derivatives of r^(l+1)f_l and r^(-l)f_l, giving S_l=f_l/r and T_l=-f_l/r
when their respective boundary terms vanish. The correction must vanish.

In log radius u, S and T are one-sided exponential convolutions with positive
rates l+2 and l-1. The implementation integrates a linearly interpolated
coefficient exactly on each cell. With cell width d and rate k, its moments
are A=(1-exp(-kd))/k and B=[1-(1+kd)exp(-kd)]/k^2. The forward cell adds
(B/d)f_left+(A-B/d)f_right; the reverse cell swaps the coefficients. A series
for B prevents cancellation when kd is small. Initial and final convolutions
are set to zero at finite cutoffs, so their truncation is tested by changing
the boundaries; it is not an exact infinity condition.

## Personally reconstructed Newtonian source

For each Gaussian-smoothed ring the planar Hankel transform is
M exp(-sigma^2 k^2/2)J0(kA)/(2pi). Direct convolution of the Newtonian vertical
factor exp(-k|z-z'|) with exp(-|z'|/h)/(2h) gives

    Z_h=[exp(-kz)-kh exp(-z/h)]/[1-(kh)^2],
    V_h=[exp(-kz)-exp(-z/h)]/[1-(kh)^2],
    -partial_z Z_h=k V_h.

The removable limits at kh=1 are (1+z/h)exp(-z/h)/2 and
(z/h)exp(-z/h)/2. The code evaluates V first and Z=V+exp(-z/h)/(1+kh), using
expm1 only where its product cannot overflow. A gas sheet uses Z=V=exp(-kz).
Thus U_R and U_z are the Hankel integrals with k J1(kR)Z and k J0(kR)V,
respectively. The midplane gas normal trace is evaluated independently as
2pi G Sigma_gas. The stellar normal trace vanishes.

The finite-height convolution is directly integrated in the control runner.
The central Gaussian sheet has closed midplane and axial force controls. The
spherical Plummer input has exactly zero angular correction. In either open
half-space of a Kuzmin disk, U points to one displaced center, so multiplying
it by the scalar nu(|U|/a0) remains a gradient. Its continuous tangential
trace is the exact QUMOND force and tests both the gas-sheet convention and
the projection without using real galaxy targets.

## Scope and numerical decisions

The implementation uses the pre-existing positive source mixtures and fixed
global U and a0. It supplies no new source fit, likelihood, confidence region,
full-PDE parameter fit, or uncertainty marginalization. Every run records its
source hash and refuses to overwrite its output. Analytic controls precede
real-source calculation. Numerical refinement and boundary checks govern
whether velocity residuals can be inspected. Failed checks remain evidence.

The mixed baryonic field can contain outward radial contributions. The input
nu depends on its full vector norm. A nonpositive total radial prediction is
preserved as a failure of that circular-support model; it is not made positive
by taking its absolute value. Independent source review remains required
before substantial downstream reliance on this new implementation.
