# Focused independent result: pure-clock mass ordering fails for a noncollinear array

Reviewer `/root/localized_history_check`; direct scientific authorship remains
with `/root`. This is a focused check of the supplied linear free KG model, not a
formal audit verdict, a general theory exclusion, an empirical test or a claim
about the actual radio link. No author physical_bridge source or other reviewer's
work was opened. Only this assigned evidence directory was written. No git,
network, state, lock, canonical source or branch mutation was performed.

## Result and scope

The energy dual Gram of a finite-point clock functional is not necessarily
bounded above by its massless counterpart for the same temporal weights.
A three-point noncollinear counterexample below already has
sum_A c_A(t)=0 at every time. Thus even a stronger cancellation than the requested
sum_A integral c_A=0 does not repair a universal ordering assertion.

For collinear fixed points, the pure-clock ordering does hold under the given
smooth compact temporal weights. This includes one or two points. Neither that
restricted positive result nor the noncollinear counterexample automatically
settles a specific coherent two-way count involving physically derived weights,
trajectory forces, repeated clocks, initial-state removal and its own geometry.
Those operators require their own comparison. No result about their full joint
clock/force Gram is inferred here.

## Independent derivation and normalization

The derivation was frozen in MASS_ORDER_PRECHECK_v1.md before numerical work and
without source access. Let C_A(omega)=integral c_A(t) exp(i omega t) dt and use the
unitary spatial Fourier convention. For omega=sqrt(k^2+mu^2), the cosine and sine
response coefficients pair with the real initial data under
||h||_H,mu^2=integral(p^2+|grad h|^2+mu^2 h^2)=2E. Angular integration gives

    G_mu=(1/(2pi^2)) integral_mu^infinity (k/omega)
          sum_(A,B) Re[C_A(omega) conjugate(C_B(omega))]
          sinc(k |x_A-x_B|) d omega.

Here k=sqrt(omega^2-mu^2) and sinc(0)=1. The factor 4pi sinc(k r) is the exact
sphere integral of the spatial phase. The radial measure k^2/omega^2 dk becomes
k/omega d omega. There is no extra real-data factor of two. At one stationary
point and zero mass, Parseval gives G_0=||c||_2^2/(2pi), which cross-checks the
normalization. The dual norm extends the initially smooth-field functional; it
does not assume an unsmeared point trace for arbitrary energy-class data.

The mass change alters both the radial prefactor and the spatial interference
phase. Replacing only k/omega while retaining the massless phase sinc(omega r)
is a different, incorrectly simplified operator. Every temporal C_A here remains
identical when mu changes.

Let M_mu(omega)=(k/omega)[sinc(k r_AB)], zero below the massive threshold.
Since d[k sinc(k r_AB)]/dk=cos(k r_AB), collinear points x_A=s_A e have a positive
semidefinite derivative matrix:

    cos(k(s_A-s_B))=cos(k s_A)cos(k s_B)+sin(k s_A)sin(k s_B).

Integrating from k to omega proves M_mu<=M_0 frequency by frequency. This remains
valid for complex temporal transforms by applying the real symmetric matrix to
their real and imaginary parts. For noncollinear Euclidean distances the cosine
matrix need not be positive semidefinite, and the following example exploits
exactly that failure.

## Explicit counterexample

Choose

    x1=(-3/4,0,0), x2=(3/4,0,0), x3=(0,sqrt(7)/4,0),
    c1=f, c2=f, c3=-2f.

The distances are 3/2,1,1, and the summed clock weight vanishes pointwise. For
a=(1,1,-2), the fixed-frequency quadratic response is

    q_mu(omega)=F(k)/omega,
    F(k)=6k+(4/3)sin(3k/2)-8sin(k).

Set omega0=2pi, mu=pi sqrt(23)/6, so k0=11pi/6. Then

    q_0(omega0)=6,
    q_mu(omega0)=11/2+2/pi+sqrt(2)/(3pi)
                = approximately 6.286672491727098.

The difference is positive. Also a^T[cos(omega0 r_AB)]a=-4, showing directly why
reducing spatial wavenumber can increase this response. This is a finite-array
interference effect, not a changed clock history, fitted mass or amplitude scale.
The fixed frequency alone is diagnostic, but the final counterexample uses the
following genuine smooth compact weight, not a monochromatic distribution.

Let T=40 and g(t)=exp[-t^2/(2T^2)]cos(2pi t). Define b(z)=exp(-1/z) for z>0 and
zero otherwise. Let q(z)=b(z)/(b(z)+b(1-z)) between zero and one, with its smooth
constant continuations outside that interval. Put

    chi(t)=1-q(|t|/T-8), f(t)=chi(t)g(t).

Thus f is real C-infinity, equals g for |t|<=320, and vanishes for |t|>=360.
The same f and fixed points are used in both comparisons. The cancellation
sum_A c_A=0 is exact regardless of the small nonzero integral of f.

## Strict analytic finite-packet margin

The precheck gives a conservative elementary bound, independently of numerical
integration. On I=[2pi-0.1,2pi+0.1], the corresponding k is in [5.64,5.88],
-4<=F'(k),F'(omega)<=0, and k'<1.14. This yields

    |(q_mu-q_0)'| < 8.56/6.18+2.666/(6.18^2) < 1.456,
    q_mu-q_0 > 0.286-0.1*1.456 > 0.13.

Outside that band each q is a nonnegative angular average bounded by
(sum |a_A|)^2=16, so q_mu-q_0>=-16. The Gaussian positive-frequency squared
transform norm is

    I_all=pi^(3/2)T[1+exp(-T^2 omega0^2)]/2.

The fraction outside I is at most 2 erfc(4)+erfc(T omega0)<3.2e-8. Therefore

    G_mu(g)-G_0(g)
      >= I_all/(2pi^2)[0.13-16.13*(3.2e-8)] > 0.7.

The cutoff changes the temporal L2 norm by at most
sqrt[T exp(-64)/8]<3e-14. Each quadratic clock operator on common temporal f
has operator norm <=16/(2pi). The change of their difference is thus bounded by
(16/pi)(2||g||_2+delta)delta<1e-10. Consequently the actual smooth compact f obeys

    G_mu(f)-G_0(f) > 0.7-1e-10 > 0.

This conservative analytic inequality is the strict sign argument. Evaluation of
the sharper displayed expression gives about 0.7334435464894, but those digits
are ordinary floating evaluation, not an interval certificate. The rigor does
not depend on their last digits, the sampled frequency grid or numerical errors.
The proof uses the exact tail inequalities and conservative bounds above.

For even f an explicit real Riesz field is also available:

    h0hat_mu(kvec)=(2pi)^(-3/2) C(omega)
                    sum_A a_A exp(-i kvec.x_A)/omega^2,
    p0hat_mu=0.

It has conjugate symmetry and finite energy. Its energy-Hilbert squared norm is
the computed G_mu. At mu=0 the summed coefficients improve the infrared behavior,
and an added constant gives zero response. These representers characterize the
dual norm, not a physically selected observed field.

## Independent implementation and controls

The first execution passed all 120 controls; there is no failed run to repair.
The source and stdout/stderr remain intact. The controls include exact geometric
separations and zero-sum weights; closed sine factors; positive angular quadrature
at two resolutions; the negative cosine-matrix direction; twenty-five collinear
mass/frequency comparisons with their derivative-Gram controls; independent
composite temporal quadratures of the explicit compact f; Gaussian-transform
comparison with the separately bounded cutoff tail; spectral resolution; and
real-field conjugate symmetry and three-dimensional Riesz energy integration.

The finite spectral integration gives

    G_0 approximately 33.851821532785884,
    G_mu approximately 35.46813498682403,
    G_mu-G_0 approximately 1.6163134540381492,
    G_mu/G_0 approximately 1.0477467202901543.

Direct three-dimensional energy integration of the Gaussian Riesz fields gives
33.8518215327861 and 35.46813498682416 respectively, agreeing with the spectral
values. Those field checks use the analytic Gaussian transform on a finite
radial band; the actual compact packet is connected to it by the explicit global
L2 perturbation bound. They are not mislabeled as exact numerical integration
of the entire compact field spectrum. Direct compact temporal quadrature provides
another representation; it cannot resolve the exponentially tiny cutoff change
at floating precision and does not replace the analytic bound.

The scalar profiles, locations and mass are synthetic mathematical choices.
There are zero empirical tests and zero imported observed or fitted quantities.
No broad statement about nonlinear theories, actual data or all noncollinear
geometries is inferred. The result is one explicit counterexample to the
universal ordering and a separate sufficient theorem for collinear pure-clock
arrays. The physically derived coherent fixture remains a separate question.

## Exact identities

MASS_ORDER_PRECHECK_v1.md:
30518157177387a7d90d3c218a638ae78aa30fb8cfbab310f663d34076c3fb51

independent_mass_order_check_v1.py:
3d60a7a1a45fba1aefe5b532e880d2d6bf43c3c464e27fea03bda32bba09012b

MASS_ORDER_REVIEW_IDENTITY_v1.json binds these original files, the result,
execution records and this report. No author sources are included or claimed
reviewed. The precheck is preserved without alteration.
