# Can common metric histories determine the supplied scalar response?

Root's personally authored derivation, begun 2026-10-16. This is an ideal-input
identifiability result inside a stipulated action class. It is not an
observational reconstruction performed on this universe, a new fundamental
action, or a priority claim for scalar-tensor inverse reconstruction. The
neutral contract was sent to a focused checker before this source was exposed.

## Observation entry and conditional class

Primitive records are positions, redshifts, shapes, velocities and clock
comparisons. Assume, conditionally, that a registered inverse measurement
protocol has supplied smooth matter-frame expansion h(tau), scale factor aJ
and linear scalar potentials PsiJ(tau,k), PhiJ(tau,k) for common nonzero
comoving wave numbers. The protocol must specify the same time, coordinates,
Fourier phases, normalization and derivative/error model for every mode.
This campaign has not supplied that protocol or observed functions. Lensing
integrals and growth summaries are not automatically these functions.

Adopt the already checked canonical class

    S = integral sqrt(-gE) [M^2 RE/2 - (partial phi)^2/2 - V(phi)]
        - sum m integral A(phi) dsE,
    gJ = A^2 gE, M>0, A>0,

with one scalar, universal conformal coupling, flat FLRW and pressureless
particles. No extra anisotropic stress is included. This class, flatness,
linearization and matter content remain premises. No potential, coupling
profile, scalar initial condition or effective mass is supplied to the inverse.
The arguments below use C-infinity inputs on a connected interval as a
sufficient regularity condition; they make no claim to minimal regularity.

Set P=(PsiJ+PhiJ)/2, J=(PsiJ-PhiJ)/2 and kj2=k_com^2/aJ^2. Previously checked
notation is b=M A_phi/A, x=phi'/M, q=bx, ell=h-q, w=delta(phi)/M and
kappa=(V_phiphi+rho A_phiphi)/A^2 at fixed bare proper Einstein dust density.
Primes are matter proper-background-time derivatives. Work initially on a
connected b!=0 chart. Then J=bw; no division by P or J is needed.

## Five coefficients from actual mode histories

The exact scalar equation after eliminating the Hamiltonian density source is

    w''+3ell w'+(kj2+d_eff)w
      =(6b ell+4x)P'
       +[2b kj2+6b ell^2-b x^2+2(x'+3hx-2bx^2)]P,
    d_eff=kappa+b x'+3bhx-2b^2 x^2.

This identity retains time derivatives, force away from a density minimum,
metric mixing and the clock conversion. It is not alone a physical-mode
equation. Substitute w=J/b and L=b'/b, keeping both quotient derivatives:

    J''+kj2 J = -a J' - c J + d P' + e kj2 P + f P,       (1)
    a=3ell-2L,
    c=d_eff+L^2-L'-3ell L,
    d=6b^2 ell+4q,
    e=2b^2,
    f=6b^2 ell^2+2b x'+6hq-5q^2.                        (2)

At each epoch form the real matrix D with rows [-J',-J,P',kj2 P,P] and y with
entries J''+kj2 J. Real and imaginary components can be separate rows only
when their common Fourier/time registration is known. If rank(D)=5 and y is
in its column space, the common coefficient vector (a,c,d,e,f) is unique.
For more than five rows the residual y-D theta is an additional consistency
test. Five rows by themselves solve for coefficients; they do not establish
the action or physical compatibility.

Rank five is not inferred by counting modes. In particular, if every row has
the same kj2, columns four and five are proportional. Rank below five invalidates
this simple linear extraction, but does not prove that all nonlinear or
time-integrated reconstruction routes are impossible. No preferred mode
initial conditions are assumed in the inverse.

## Deriving b squared, scalar speed and fixed-density curvature

Define from the extracted coefficients

    B=e/2 > 0, L=B'/(2B),
    q=h-(a+2L)/3,
    b=s sqrt(B), x=q/b, s=+1 or -1 constant,
    kappa=c-q'-3hq+2q^2-2qL-L^2+L'+3hL.                (3)

These are explicit functions of the registered input, including its
derivatives. They do not choose a root for a scalar initial velocity. Require
q!=0 for the subsequent monotonic action chart. The remaining two coefficient
conditions are

    d=6B(h-q)+4q,
    f=6B(h-q)^2+2(q'-qL)+6hq-5q^2.                     (4)

The earlier research plan proposed q=(d-6Bh)/(4-6B). Its apparent singularity
at B=2/3 is an artifact of that elimination choice. Equation (3) uses the
independently extracted damping a and the derivative of B and stays regular
there. This removes that artificial exclusion; B=0 is still a genuine
excluded chart of this derivation. Differentiation is an information and
noise requirement, not a free observational operation.

## Background compatibility and local action construction

Set

    R=2q'-2h'-2hq+(2-1/B)q^2 > 0,                    (5)
    D_bg=R'+(3h-2q)R,
    K_bg=x''+3h x'+[3h'+kappa-2q'+6hq-4q^2]x
                           -3b(h-q)R.               (6)

Require D_bg=K_bg=0. The first is dust conservation after the Einstein
Raychaudhuri equation fixes R. The second is the checked fixed-bare-density
curvature compatibility, not an assumed density minimum.

For arbitrary positive A0 and field origin phi0 construct locally

    A=A0 exp(integral q d tau), phi=phi0+M integral x d tau,
    dtE=d tau/A, aE=aJ/A,
    r=M^2 A^2 R, rho=r/A,
    V=M^2 A^2 [3(h-q)^2-x^2/2-R].                    (7)

Since x!=0 these give single-valued A(phi), V(phi) on the sampled field
interval. The Friedmann and Raychaudhuri equations hold by construction.
D_bg ensures rho aE^3 is constant. Differentiating Friedmann with those two
facts gives the ORIGINAL scalar KG equation because phi_dot!=0. It does not
merely give a differentiated scalar equation with a lost integration constant.
Differentiating its force along this trajectory and using K_bg then gives
(V_phiphi+rho A_phiphi)/A^2=kappa. Thus the background is sufficient inside
this local, smooth, positive-dust, monotonic class. No extension of the
potential outside the sampled field interval follows.

## Full perturbation compatibility

For each mode put w=J/b, Fbar=-x'-3hx+2qx and define

    Z=[xw-2(P'+ell P)]/R,
    delta=[-2kj2 P-6ell(P'+ell P)-xw'+x^2 P-Fbar w]/R. (8)

Z=A U is the matter-frame comoving dust velocity potential, where
aE^2 d(x_coord)/dtE=gradient U. Delta is the bare proper Einstein dust contrast;
the matter-frame physical contrast is deltaJ=delta-3J. Equation (8) is exactly
the momentum and Hamiltonian constraints, not a supplied source profile.
Require the two matter residuals

    Z'+P+J=0,
    delta'-3P'-kj2 Z=0.                              (9)

Equivalently deltaJ'=3PhiJ'+kj2 Z and Z'=-PsiJ. The velocity variable is a
comoving potential, so no omitted Hubble-friction term belongs in this form.

To check sufficiency, the uneliminated scalar equation in matter time is

    w''+(3h-2q)w'+(kj2+kappa)w
                  =-bR delta+4xP'-2Fbar P.          (10)

Substitute (8) into (10): it is exactly (1) divided by b when (2)-(4) hold.
Momentum and Hamiltonian hold by definition, and (9) supplies both dust
equations. In Einstein variables u=Mw, U=Z/A, r=M^2 A^2 R the previously
checked constraint identity E_dot+3HE E=0 and the spatial-trace consequence
then supply the remaining Einstein scalar equation. No anisotropic-stress
equation is missing because PsiE=PhiE=P in the stipulated class. Hence
(1),(3)-(6),(8),(9), the positivity/chart conditions and smoothness are a
necessary and sufficient LOCAL compatibility test on this rank-five chart.
This sufficiency is for linear scalar perturbations about the constructed
background, not nonlinear stability, radiation, multiple species or a TOE.

## Physical feasibility of rank five

Take the exact original-equation background M=1, tE>0,

    aE=tE, phi=ln(tE), A=exp(phi)=tE,
    rho=tE^-3, r=tE^-2, V=(3/2)exp(-2phi),
    tau=tE^2/2, h=2/tE^2, b=1, x=1/tE^2,
    R=tE^-4, kappa=7/tE^4.

All four background equations hold. At tE=1 the five coefficient values are
(a,c,d,e,f)=(3,9,10,2,9). Choose a small nonzero epsilon and five nonzero
wave-number squares 1,2,3,4,5. Initial (u,u_dot,P,U), in units of epsilon,
are respectively

    (0,1,0,0), (1,0,0,1), (0,0,0,-2),
    (0,0,1,-2), (0,0,1,-2).

For each mode the Hamiltonian determines delta; the exact full linear
initial-value equations allow these four free initial amplitudes and
preserve the constraint. At this epoch D/epsilon is

    [-1,  0, 0, 0, 0]
    [ 0, -1, 0, 0, 0]
    [ 0,  0, 1, 0, 0]
    [ 0,  0, 0, 4, 1]
    [ 0,  0, 0, 5, 1].

Its determinant is -1, so rank five is realized by legitimate initial data,
not inconsistent algebraic sources. Smooth linear ODE existence and
continuity give a nonzero interval of full rank. Root's numerical forward
check integrates the ORIGINAL Einstein-time scalar, dust and momentum
equations to test this construction over a declared finite interval.
This stipulates synthetic initial modes for a feasibility witness only;
it does not select this universe's initial state or establish survey rank.

## What is removed and what remains

If the ideal registered inputs pass all these tests, independently supplied
b(tau), kappa(tau), local scalar velocity and potential shape are unnecessary
inside this action class. The sign s and phi0 are field orientation/origin;
there remains a continuous A0 scale freedom. Under A0 -> lambda A0, r,V
scale by lambda^2, rho by lambda, aE by 1/lambda and dtE by 1/lambda.
The supplied h, matter potentials, mode clocks, B,q,kappa,R and matter dust
contrasts/velocity Z remain identical. In particular the matter-frame Planck
coefficient M^2/A^2 is not calibrated by these potentials alone. A measured
matter density would add rhoJ=(M^2/A^2)R, but is not supplied here.

At a reference time the reconstructed perturbation amplitudes follow from
the potential histories; their cosmological origin, probability law and
prehistory are not derived. These deterministic histories do not supply
quantum probabilities. b=0, x=0, R=0, rank loss, species/anisotropic stress,
global continuation and nonsmooth histories need other charts or routes.
Negative kappa is not excluded here by fiat; stability is a separate test.

## Conditioning limitation

For an exact consistent y=D theta with smallest singular value sigma>0,
perturbed D+E and y+eta obey, for the least-squares coefficient estimate,

    ||theta_hat-theta|| <=
       (||eta||+||E|| ||theta||)/(sigma-||E||),         (11)

provided ||E||<sigma. This uses the norm of the pseudoinverse of D+E and
Weyl's singular-value bound. Row/column units and normalization must be fixed
before interpreting sigma. Small potential errors alone do not control their
derivatives, B', B'' or the reconstructed q,kappa. A uniform high-frequency
perturbation can have vanishing amplitude but large derivatives; equation
(11) is therefore not a practical survey error budget. Additional registered
derivative regularity/noise bounds and distance/velocity/lensing inversions
remain necessary. No observational arrays have been opened for this block.
