# Six-node flux threshold Dirichlet check

Disposition: PASS. The stated negative 1/log R endpoint sum is correct for the static Dirichlet coefficient problem, and supplies no nonzero infinite-volume threshold limit or full scattering rate.

For the flipped columns (0,0),(1,0), T_s differs from free -Adj by +2 on the four vertical bonds joining these central sites to (0,+/-1),(1,+/-1). Set L0=4-Adj and V equal to these four symmetric +2 bonds. With boundary value one the exact interior equation is u=1-G_R V u, where G_R is the Dirichlet inverse of L0. The six-node restriction is sufficient; the nonsymmetric boundary rows in the root sparse solve merely impose Dirichlet values and do not change the symmetric interior problem.

## Green normalization and constants

The infinite potential difference is

 A(m,n)=int_[BZ] [1-cos(m kx+n ky)]/[4-2cos kx-2cos ky] d^2k/(2pi)^2.

Integrating ky first yields the one-dimensional integral

 A(m,n)=1/pi int_0^pi [1-cos(mx) r(x)^|n|]/[2 sqrt((2-cos x)^2-1)] dx,
 r(x)=2-cos x-sqrt((2-cos x)^2-1).

This gives A10=1/4, A11=1/pi, A20=1-2/pi, A12=2/pi-1/4. In particular the normalization is for 4-Adj, not the random-walk I-Adj/4. Independent numerical integration of all four constants agrees within 1.7e-16. A10 also follows directly from the origin equation, and the remaining constants are consistent with the lattice harmonic recurrence.

For fixed nodes in a growing square, G_R(i,j)=g_R-A(i-j)+o(1), g_R=log R/(2pi)+O(1). One rigorous route uses this potential kernel and the killed-walk representation: the boundary correction is the harmonic average of A(exit-j), and fixed changes in i,j give vanishing differences at distances of order R. The logarithmic coefficient follows directly from the small-k denominator kx^2+ky^2. An O(1) domain-shape constant changes g_R but not the result below.

## Schur algebra

With central amplitude a and outer amplitude b in the leading reflection-symmetric six-node system, V u equals 4b at each of the two central sites and 2a at each of the four outer sites. Its total is 8(a+b). Subtracting the explicit a or b from the potential-kernel contributions gives exactly

 0=1-8g(a+b)+b+4a/pi,
 0=1-8g(a+b)+4b/pi+2a.

Hence r=a/b=(4-pi)/(4-2pi)=-0.37596919694205444 and

 2a=2r/[8g(1+r)-1-4r/pi].

The actual square [-R,R]^2 is not exactly symmetric under x->1-x. Thus equal central amplitudes are an asymptotic statement, not an exact finite-R identity for the root geometry. This only affects the vanishing Green remainder.

To control that remainder without assuming exact symmetry, write C=I-A V and the full six-node matrix C+g 1(1^T V). With p=1/pi its exact determinant is

 det C=4(8p^2-1)(8p^2-4p+1),

which is nonzero. Moreover beta=1^T V C^-1 1=-4(8p-3)/(8p^2-1) is nonzero. Sherman-Morrison therefore gives the full limiting solution C^-1 1/(1+g beta)=O(1/g), while the inverse matrix remains uniformly bounded for large g. Adding an o(1) matrix remainder changes the solution by o(1/g). This justifies the claimed additive o(1/log R) error, including the finite-square asymmetry.

Consequently

 lim_(R->infinity) log R [u(0,0)+u(1,0)]
 =pi r/[2(1+r)] = -0.9463812213285369.

The endpoint sum is therefore negative and nonzero for sufficiently large finite R, but tends to zero logarithmically. The negative sign is compatible with a signed-bond Laplacian: a scalar positivity/maximum-principle argument does not apply to its site amplitudes.

## Scope

This is a static energy-at-free-threshold coefficient boundary-value problem, with specified unit boundary data. It corrects the naive exact free-wave cancellation: the defect-dressed endpoint source is nonzero at finite R. It does not establish a finite nonzero infinite-volume threshold matrix element; the displayed limit instead vanishes before logarithmic rescaling. Nor does it give a retarded on-shell scattering amplitude, outgoing normalization, finite-frequency threshold continuation, relaxed heavy state, full native channel, or universal matter coupling. Those require their own matching and limiting prescription.

Independent algebra/integral checks are in /tmp/neutral_flux_reviewer.py. Root /tmp/neutral_flux_scatter.py was read, not modified; no heavy duplicate solve or repository edits were performed.
