<!-- Original PR9776 source SHA256 e7f2a146421e105b2747a626bf31303293b39d80aa01562f292db95295c8554b. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Two-arm anisotropic cavity threshold: independent check

Disposition: PASS for the stated coefficient graph, with the numerical critical value labeled numerical and the source asymptotic conditional on the stated overlap. Read /tmp/neutral_threshold_root.md, /tmp/neutral_binding_threshold.py and JSON. No canonical/shared-file edits.

## Cavity criterion and uniqueness

In the normalized inversion-even root basis (|+x>+|-x>)/sqrt(2), (|+y>+|-y>)/sqrt(2), removing the origin gives exactly

 Gxx=g00+g20-2g10^2/g00,
 Gyy=g00+g02-2g01^2/g00,
 Gxy=2g11-2g10*g01/g00.

Each attached hopping-2 ray has self-energy sigma(E)=(E+sqrt(E^2-16))/2<0 for E<-4, using the positive real square root. The positive Birman matrix is B(E)=sigma(E)G_hole(E). A bound state below Eh=-4(1+b) is equivalent to an eigenvalue of B reaching 1. There are no additional states invisible at both roots below this edge: the disconnected host and rays individually have no such spectrum.

At fixed b>0, both -G_hole(E) and |sigma(E)| increase as E increases from minus infinity toward Eh. Thus each Birman eigenvalue increases strictly from zero; its edge value counts the below-edge solutions. At the edge, -G_hole is the compressed inverse of the origin-Dirichlet operator 2Lx+2bLy, with L=2-S-S*. Increasing b decreases this inverse in quadratic-form order. The scalar |sigma(Eh)| strictly decreases. Since the compressed inverse is positive definite, the resulting Birman eigenvalues strictly decrease with b. The same argument gives a strictly negative derivative locally: the scalar derivative already supplies a strictly negative contribution.

The supplied edge difference formulas follow directly from the free lattice recurrence. In the b down to zero limit, -Gxx tends to 1/2, -Gxy stays finite, and -Gyy diverges; hence the smaller Birman eigenvalue tends to 1 and the larger diverges. Strict decrease implies the smaller stays below 1 for every b>0. At b=1 the largest is 2-sqrt(3)<1. Consequently exactly one critical b_c exists, with one simple bound state below the continuum for 0<b<b_c and none for b>b_c. This proof does not classify the threshold vector at b=b_c as an L2 eigenstate. The approximate value .23475690092702978 is supported by the supplied quadrature/root solve, not a certified interval enclosure.

## Logarithmic approach

Near the host minimum the dispersion excess is 2kx^2+2b ky^2. With normalized Brillouin measure this gives

 g00(Eh-delta)=-c log(1/delta)+O(1), c=1/(8pi sqrt(b)).

Writing gx=g00+Dx etc. in the exact cavity formula cancels the divergent constant and leaves the rank-one correction

 G_hole=G_edge+2DD^T/[c log(1/delta)]+O(log(1/delta)^(-2)),

D=(Dx,Dy). Thus for the normalized positive top eigenvector v at criticality,

 mu(E,b)=mu_edge(b)-K/log(1/delta)+O(log(1/delta)^(-2)),
 K=2|sigma(Eh)|(v.D)^2/c>0.

The sign is correct: moving below the edge reduces the Birman eigenvalue. Positivity of v and D ensures the logarithmic coefficient does not vanish. Smooth dependence near b_c and m=-mu_edge'(b_c)>0 give

 log(1/delta) ~ K_c/[m(b_c-b)].

This is an essential exponential small binding energy, not a power law. The transverse decay lengths have anisotropic prefactors proportional to sqrt(2/delta) and sqrt(2b/delta); both scale as delta^(-1/2) near the fixed positive b_c. No analogous divergence of the attached-ray decay length follows: the host edge stays a fixed distance below -4 there.

## Normalization and source

The host component reconstructed from its root vector u is psi_host=(E-H_host)^(-1) P sigma u, so its norm squared is sigma^2 u^T[-G_hole'(E)]u. The sign uses d(E-H)^(-1)/dE=-(E-H)^(-2). The attached-ray norm is bounded times |u|^2 near b_c and is subleading compared with the divergent host norm.

The required differentiated edge expansion is valid, but should be justified from the Green integral rather than by formally differentiating an unspecified O(log^-2) remainder. Splitting a small neighborhood of the nondegenerate minimum gives g00'=-c/delta+O(log(1/delta)); the derivatives of g_r-g00 grow at most logarithmically for these symmetric fixed-displacement entries. Substitution into the EXACT cavity formula yields

 -G_hole'(E)=2DD^T/[c delta log(1/delta)^2]*(1+o(1))

in its divergent rank-one part; the other terms are smaller. Consequently, with u/|u| tending to v,

 |u|^2 ~ c delta log(1/delta)^2/[2 sigma^2(v.D)^2].

For the separately supplied source lambda(-1,b), the proposed weight follows:

 lambda^2 c delta log(1/delta)^2 [(-1,b).v]^2/[2 sigma^2(v.D)^2],

provided (-1,b_c).v is nonzero. The conditional statement is correct; its nonzero value needs the separate computation/algebra requested by root. No factor of two is missing in this normalized two-root basis. A different physical Fourier/source normalization must be applied separately.

All conclusions concern the specified complete K1 graph at selected momentum. Extremely near threshold, higher native orders can exceed the exponentially small binding gap; no uniform full-H transfer follows without a quantified double-scaling/remainder comparison. Neither the large spatial extent nor the bound coefficient branch establishes a Lorentz scalar, physical particle, selected state, or nonvanishing macroscopic readout strength.

## Elementary potential formulas: confirmed

The proposed formulas are exact for b>0:

 Dx=atan(1/sqrt(b))/(2pi),
 Dy=atan(sqrt(b))/(2pi b),
 Dxy=1/(2pi sqrt(b)).

To verify, write A=1-cos x, f(x)=sqrt(A/(A+2b)), theta=atan(1/sqrt(b)), and use the supplied one-dimensional integral formulas. With u=cos(x/2),

 integral_0^pi f(x) dx=2 integral_0^1 du/sqrt(1+b-u^2)=2theta.

Also I2=integral_0^1 u^2 du/sqrt(1+b-u^2)=[(1+b)theta-sqrt(b)]/2, so

 integral_0^pi cos(x) f(x) dx=4I2-2theta=2b theta-2sqrt(b).

Thus Dx=(1/(4pi)) integral f=theta/(2pi), while Dy=(1/(4pi b)) integral(1-f)=(pi/2-theta)/(2pi b). Finally integral cos x=0 gives

 Dxy=Dx-(1/(4pi b)) integral cos(x)f(x)dx=1/(2pi sqrt(b)).

These expressions remove quadrature from the critical-matrix evaluation. At a critical matrix K=|sigma|(-G_edge) with Perron eigenvalue 1 and positive off-diagonal, Kxx<1 and the positive eigenvector ratio is exactly

 vx/vy=Kxy/(1-Kxx).

Consequently a rigorous enclosure proving this ratio strictly exceeds b throughout a certified critical bracket proves (-1,b).v<0, eliminating the previously conditional nonzero source premise. This implication and denominator sign are verified here; the proposed interval bracket/ratio certificate has not yet been supplied in this review, so its actual numerical inequalities remain to be checked. A floating-point root alone is not that certificate.

## Divergent transverse second moments: confirmed

PASS for the normalized coefficient eigenstate as b approaches b_c from below, provided the previously derived cavity representation and simple critical eigenvector are used. Here r is the relative transverse displacement of the two singleton columns, not an individual column's displacement from their center. The latter would have second moments smaller by a factor four.

The exact inversion-even Fourier numerator is

 N(k)=sqrt(2)sigma{u_x(cos kx-1)+u_y(cos ky-1)-(u.D)/g00}.

Its constant part is order sqrt(delta), because |u| is order sqrt(delta)log(1/delta) and 1/g00 is order 1/log(1/delta). The momentum-dependent part is O(sqrt(delta)log(1/delta)|k|^2). At |k|=O(sqrt(delta)) the latter is relatively O(delta log(1/delta)), so it does not affect the leading scaled profile. With the normalized Brillouin measure dkx dky/(2pi)^2, that profile is

 psi_hat(k) ~ A_delta/[delta+2kx^2+2b ky^2],
 |A_delta|^2 ~ delta/c, c=1/(8pi sqrt(b)).

This is a statement about the shrinking-momentum/scaled L2 profile and its leading moment integrals, not a uniform relative approximation over the full Brillouin zone. The normalization follows from integral [delta+2kx^2+2bky^2]^-2 dk/(2pi)^2=c/delta.

The moment claim requires more than L2 profile convergence, but the explicit numerator supplies the needed control. Split the integral into a small neighborhood of k=0 and its complement. In the complement the host denominator stays bounded away from zero and numerator and its derivatives are O(sqrt(delta)log(1/delta)), so the contribution to the derivative norm is O(delta log(1/delta)^2). In the small neighborhood use N=N(0)+O(sqrt(delta)log(1/delta)|k|^2), grad N=O(sqrt(delta)log(1/delta)|k|), and dispersion D=delta+2kx^2+2bky^2+O(|k|^4). These bounds show the numerator-derivative term and the variable-numerator correction are o(delta^-1) in the squared derivative norm; their cross terms are controlled by Cauchy-Schwarz. Quartic dispersion errors are likewise lower order. Thus no hidden ultraviolet term competes with the leading delta^-1 moments.

Set px=sqrt(2)kx, py=sqrt(2b)ky. The continuum integral is exactly

 integral px^2/(delta+p^2)^4 d^2p/(2pi)^2=1/(48pi delta^2).

Consequently Parseval gives

 <r_x^2> ~ |A_delta|^2/(12pi sqrt(b)delta^2)=2/(3delta),
 <r_y^2> ~ 2b/(3delta) ~ 2b_c/(3delta).

The inversion quotient does not change these even moments: its normalized embedding in the full relative-coordinate lattice preserves the norm and r_i^2 expectation. The root/ray contribution has total norm O(delta log(1/delta)^2); its interval-length distribution has a uniformly bounded decay length near b_c, so it cannot compete with these transverse moments. Fixed transverse positions on the arms likewise give negligible transverse moment contributions.

The interpretation is therefore specifically a large separation between two singleton defects in the host, with vanishing arm probability. It is not a growing number of flipped spins, a long longitudinal interval, or a demonstrated macroscopic particle. The transverse RMS lengths diverge as delta^-1/2 with the constants above; their COM-relative individual positions have the corresponding factor-one-half lengths.
