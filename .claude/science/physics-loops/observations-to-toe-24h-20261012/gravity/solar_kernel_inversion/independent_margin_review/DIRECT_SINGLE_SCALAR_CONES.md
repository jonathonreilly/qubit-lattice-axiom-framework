# A spherical single-scalar alternative has a wider characteristic cone

Direct parent derivation, 2026-10-12. This is a second explicit completion
probe, distinct from the failed two-scalar promotion. Its relation to known
scalar MOND and characteristic-cone issues is background, not a novelty claim;
see [Bekenstein2004](https://arxiv.org/abs/astro-ph/0403694) and the principal
symbol analysis in [Babichev, Mukhanov and Vikman2007](https://arxiv.org/abs/0708.0561).
The formulas below use signature(-,+,+,+) and a static spacelike background;
they must not be replaced by the timelike-background sound-speed formula.

## Candidate and its restricted static match

On a smooth interval with D(A)=N(A)+A N'(A)>0, invert the spherical relation
g=A N(A). Define mu(g)=1/N(A(g)). The single-potential elliptic model

    div[mu(|grad phi|) grad phi] = 4 pi G rho

then agrees with the original response for spherical sources with the usual
radial boundary condition. It is a different non-spherical field equation.
The disk and solar fits of the QUMOND model do not transfer to it. If D0
creates a noninvertible interval, even this smooth inversion requires repair.

Propose the Lorentz scalar action L=-H(X)/(8 pi G)-rho phi, with
X=eta^(mu nu)partial_mu phi partial_nu phi and H'(X)=mu(sqrt(X)) on X>0.
A timelike extension and physical matter/metric coupling would be further
assumptions. Examine only its local principal part about a static solution.

## Direct characteristic calculation

The principal coefficient for perturbations is

    Z^(mu nu) = mu eta^(mu nu)
                + [mu'(g)/g] partial^mu phi partial^nu phi.

With the background spatial gradient along x, this is diagonal with entries
(-mu,mu+g mu',mu,mu). Its time kinetic coefficient is positive in the stated
action for mu>0. Radial spatial positivity needs mu+g mu'>0. Direct implicit
differentiation of g=A N gives

    mu'(g) = -N'(A)/[N(A)^2 D(A)],
    mu+g mu' = 1/D(A),
    c_parallel^2/c_matter^2 = (mu+g mu')/mu = N(A)/D(A),
    c_transverse^2/c_matter^2 = 1.

Thus a decreasing enhancement N'(A)<0 with D>0 gives a radial scalar
characteristic speed greater than the metric light speed. It approaches an
unbounded ratio as D approaches zero from above. At response knots these
statements use smooth one-sided coefficients. In constant-response tails
both ratios return to one.

The finite margin candidate's nonzero ramp weights can be inserted into this
formula as a diagnostic. On interval j, set N_hi=1+sum_(k>j)w_k and
c_j=w_j/log(A_(j+1)/A_j). The one-sided maximum ratio in that interval is
N_hi/(N_hi-c_j), provided the denominator is positive. This does not imply
that the alternative theory has successfully fitted any galaxy or ephemeris.

## What is and is not rejected

This construction fails an added requirement that the scalar characteristic
cone lie inside the matter metric cone wherever N decreases. That requirement
is a stated completion premise, not something established by the static data.
A wider cone by itself is not proof of a global causal paradox, vacuum decay,
or an observational exclusion. Full coupled characteristics, allowed initial
data, source coupling and observations would still need study. The cited
k-essence work makes the same distinction between characteristic speeds and
global causality.

Unlike the two-scalar kinetic-sign failure, the local time and gradient signs
here can both be healthy when mu>0 and D>0. This supplies a useful fork in the
inverse program: changing field content can remove the immediate ghost but
changes the static disk/solar map and the propagation assumptions. Neither
candidate is yet a physical unification. No formal audit standing is claimed.
