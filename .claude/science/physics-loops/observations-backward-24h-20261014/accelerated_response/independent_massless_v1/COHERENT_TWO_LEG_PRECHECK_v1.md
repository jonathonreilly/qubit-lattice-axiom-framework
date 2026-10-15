# Independent coherent two-leg stationary composition precheck

Reviewer `/root/inertial_response_check`; root remains sole campaign author.
This derivation was made before opening any new `coherent_exact_energy` author
source or result. Only the parent's specified configuration and the previously
frozen massless joint theorem were used. No raw observations or formal audit.

## Supplied configuration and initial data

The laboratory light speed is one. Let R=3/5, station x_S=0, spacecraft
x_C=R e_1. Both reference bodies are stationary/free in a flat conformal
background A_b=1. A perfect instantaneous coherent turnaround has constant
factor K and no spacecraft clock or delay. The common linear scalar coupling
is alpha and K alpha=1. Perturbed coordinate displacement is xi_A and station
proper-clock perturbation is eta_S. They obey

    xi_A''(s) = -alpha grad h(s,x_A),
    eta_S'(s) = alpha h(s,0).

The linearized initial positions, velocities and clocks are arbitrary. The
initial epoch s_* is any epoch strictly before the first emission. Initial
clock constants will cancel within each coherent phase; spacecraft clock data
are absent from this ideal coherent model. The massless energy result uses the
previously fixed real field norm ||h||_H^2=2E, with no observer-frame energy
replacement.

## Direct derivation from the two null legs

For receiver reference time s, reflection and emission times are q=s-R and
t=s-2R. The outgoing and returning first-order null equations are

    delta q-delta t = e_1.(xi_C(q)-xi_S(t)),
    delta s-delta q = e_1.(xi_C(q)-xi_S(s)).

Fixed receiver proper time gives delta s=-eta_S(s). The emitted proper-clock
phase transported coherently therefore varies by

    chi(s) = K [eta_S(t)-eta_S(s)
                + e_1.(xi_S(t)+xi_S(s)-2 xi_C(q))].          (1)

Both station endpoint positions and the spacecraft reflection position remain
in (1); the station proper-clock response has not been discarded. There is no
independent spacecraft-clock term.

The position/velocity initial contribution is

    2K e_1.[xi_S,*-xi_C,*
              +(s-R-s_*)(v_S,*-v_C,*)],

an affine function of s. The station initial clock cancels in eta_S(t)-eta_S(s).
The three receiver endpoints are s_j=7/5+j, j=0,1,2. The adjacent-unit-average
contrast is chi(s_0)-2chi(s_1)+chi(s_2), since each average duration is one.
Its coefficients a=(1,-2,1) obey sum a_j=sum j a_j=0, so all initial terms
above vanish. Transverse initial displacements/velocities have no first-order
range component. An extra affine station-clock calibration, if separately
admitted, would also cancel. No initial state has been set to zero to obtain
the contrast operator.

## Compact weights and joint massless amplitude

Let T(z) be the triangular hat on [0,2], equal to z on [0,1] and 2-z on [1,2],
and zero otherwise. Its weak derivative is

    p(z)=1_[0,1](z)-1_[1,2](z).

The sums of the free displacement response kernels are triangular hats because
sum_j a_j (b+j-w)_+ = T(w-b). The earliest emission, reflection and reception
are t_0=1/5, q_0=4/5 and s_0=7/5. After absorbing K alpha=1, the force weights
and direct-field coefficient are

    W_S(w) = e_1 [T(w-t_0)+T(w-s_0)],
    W_C(w) = -2 e_1 T(w-q_0),
    c_S(w) = p(w-s_0)-p(w-t_0),
    c_C(w) = 0.                                             (2)

Here the functional is integral c h + W.a_h with a_h=-grad h; equivalently one
may keep alpha in a_h and K in the weights. The weights are compact H1 with
zero traces and c_S is L2. In particular integral c_S=0, so the observation
also annihilates an arbitrary additive constant field. No absolute background
is thereby determined.

Write mu=n.e_1, and subtract the common arrival-time origin t_0. The spacecraft
arrival coordinate is tau=w-mu R. Applying the previously frozen signed joint
amplitude C-partial_tau H gives

    D_mu(z) = (1-mu) p(z-2R) - (1+mu) p(z)
                       + 2mu p(z-R(1-mu)).                 (3)

The reflected-path coefficient is evaluated in the same arrival coordinate as
the station, not at the same coordinate time. The second observed channel is
translated by one: D_2,mu(z)=D_mu(z-1).

Let delta be the channel translation. Axisymmetry reduces the exact Gram to

    G_delta = (1/(4pi)) integral_{-1}^1 dmu
                     integral_R D_mu(z) D_mu(z-delta) dz.   (4)

For the step hat derivative, define the even autocorrelation

    r(d)=2-3|d|       if 0<=|d|<=1,
         |d|-2       if 1<=|d|<=2,
         0           otherwise.

Let B=(-(1+mu), 2mu, 1-mu) and ell=(0,R(1-mu),2R). Then

    4pi G_delta = integral_{-1}^1
                     sum_{a,b} B_a B_b r(delta+ell_b-ell_a) dmu.  (5)

Every term is a cubic polynomial on intervals with rational endpoints. Splitting
where delta+ell_b-ell_a hits -2,-1,0,1,2 and integrating exactly gives

    4pi G_0 = 3064/405,
    4pi G_1 = -1871/405.

Thus the scalar norm and the full two-channel matrix are

    G_0 = 766/(405pi),

    G = (1/(1620pi)) [[3064, -1871],
                      [-1871, 3064]].                       (6)

The eigenvalues are 1193/(1620pi) and 4935/(1620pi), both positive. The numerical
values of the diagonal and off-diagonal are about 0.6020379575723053 and
-0.3676282697838718. The two contrast operators are therefore independent in
this specified massless energy space. Equation (6) is a sensitivity Gram,
not a field-state selection, observation fit or supplied energy budget.

## Separate direct coherent plane-wave representation

To cross-check the composition without starting from (2), insert the original
laboratory plane wave h=exp(ik n.x-ik s) into (1). Particular solutions are

    eta_S(s)=alpha i exp(-iks)/k,
    e_1.xi_A(s)=alpha i mu exp(ik n.x_A-iks)/k,

up to the initial constant/affine terms already shown to cancel. Applying
(1,-2,1) at the receiver times yields the wave coefficient

    A(k,mu) = i exp(-ik t_0) (1-exp(-ik))^2/k
               * [(1+mu) - (1-mu)exp(-2ikR)
                          -2mu exp(-ikR(1-mu))].            (7)

This is also the Fourier transform of (3), including the station-clock/force
relative sign. The translated channel multiplies (7) by exp(-ik). Real-field
pairing with ||h||_H^2=2E gives

    G_delta = 1/(4pi^2) integral_{-1}^1 integral_0^infinity
                         |A(k,mu)|^2 cos(k delta) dk dmu.   (8)

Write A=i/k sum_n b_n exp(-ik t_n), ignoring the common t_0. The nine terms
have b_n=a_j*(1+mu, -(1-mu), -2mu), and
 t_n=j+(0,2R,R(1-mu)). Their sum is zero. The exact radial identity

    integral_0^infinity (1-cos(kd))/k^2 dk = pi |d|/2

therefore changes (8) into

    G_delta = -1/(8pi) integral_{-1}^1
                   sum_{n,m} b_n b_m |delta+t_m-t_n| dmu.   (9)

An independent exact implementation of this nine-term absolute-distance sum
must reproduce (6). It uses the coherent null-leg plane-wave coefficient and
radial integral directly, rather than the step-overlap function in (5). Further
pointwise checks compare (7) to separately integrated compact weights. All such
checks will remain distinct from the author source comparison.

This is strictly a massless, ideal stationary/free coherent-link result.
Accelerated reference paths, finite turnaround delay, actual calibration,
media, noncoherent spacecraft clocks, nonlinear errors and nonzero mass require
their respective new response models or arguments. No new author draft/result
has been opened before this precheck was written.
