# Testing scalar kinetic curvature with primitive photon records

Claim type: bounded_theorem

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "focus on deriving the remaining assumptions rather than supplying them"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: "Necessary kinetic-curvature test using calibrated lensing and actual-event redshift primitives on a registered regular spacetime domain."
hypothetical_axiom_status: "Scalar/dust action class, homogeneous background, photon model, gains and observation coverage remain conditional."
admitted_observation_status: "Exact constructed full-action and arbitrary-operator controls; no empirical arrays or instrumental precision claim."
claim_type_reason: "Explicit adjoint composition, latent-field elimination, full-ray witness, and deterministic coefficient-error bound."
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Supply and bound the required temporal coverage, background and observation errors without choosing the kinetic law."
```

Primary runner: [scalar_primitive_kinetic.py](../scripts/scalar_primitive_kinetic.py).
The [computed output](../outputs/scalar_primitive_kinetic/result.json) records
original-action, primitive-map and exact norm controls. They overlap and are
not independent physical experiments.

## Observation question and result

Can a kinetic law be challenged using lensing and redshift records without
first supplying hidden scalar perturbations, velocity fields or density
initial values? Within the explicit contract below, yes: a necessary
integral residual can be written directly as weights on two photon
primitives. No derivative of a measured record appears in its evaluation.
Candidate coefficients and test weights still need derivatives. This is a
conditional mathematical result, not a demonstrated survey analysis.

The new elimination is of the explicit J and Z readouts from the kinetic
test. It does not retire the action class, background, calibration, geometry,
temporal coverage or physical source identification. It supplies no initial
state selector, absolute scale, full action reconstruction or theory of
everything. A finite set of zero residuals is not sufficient for a solution
of the original equations.

The preceding [kinetic-response result](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9644)
uses registered intermediate fields. The
[photon calibration result](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9641)
uses weak tests of transport and background compatibility. This note composes
the kinetic-curvature residual with the primitive photon map and includes a
noncanonical original-action witness and a certified error bound. Integration
by parts, inverse lensing and weak model discovery are established methods,
not new claims here: [Taylor, astro-ph/0111605](https://arxiv.org/abs/astro-ph/0111605),
[Messenger and Bortz, 2007.02848](https://arxiv.org/abs/2007.02848), and
[Reinbold, Gurevich and Grigoriev, 1911.03365](https://arxiv.org/abs/1911.03365).

## Conditional action and observation contract

Use the candidate action and operational metric

    S=integral sqrt(-gE)[M^2 RE/2+Q(zeta,Y)]-sum m integral exp(zeta) dsE,
    Y=-(partial zeta)^2/2, A=exp(zeta), gJ=A^2 gE.

Matter is one pressureless universally coupled species. Dots denote Einstein
time t; primes denote matter proper time tau, d tau=A dt. The spatially flat
homogeneous background has a=A aE, h=a'/a, q=zeta', ell=h-q. Define

    F=Q_Y/M^2, G=Fq, R=rho/(M^2 A^2), E=Q_zeta/(M^2 A^2),
    U=2YQ_YY/(M^2 R).

The background a,q,F,G,R,E is a conditional candidate history. R>0 and
G!=0 on the test support. K below must also be nonzero there. Absolute
normalizations, the action class and the link to measured gravity are not
derived. Q_Y and Q_Y+2YQ_YY are positive in the example; this is not global
stability or a quantum completion.

P is the equal Einstein metric potential, J=delta zeta, Z=A Um the matter
velocity potential, and db the bare number-density contrast. Equality of
potentials and integrated momentum require the declared linear scalar sector
with homogeneous/traceless-Hessian kernels excluded, here a full-sky l>=2
sector. A general mask does not supply that exclusion for free.

The primitive observations are the lensing potential psi and the registered
actual-event redshift perturbation z after the specified background and
observer/additional source terms have been removed. The Born path model,
common source species, clocks/distances, angular registration, source motion
and observer convention remain premises. The entire rays must lie in the
regular background chart, not only their source events.

Use the pairing measure dmu=d tau r^2 dr dOmega. This is the mathematical
weak-equation measure, not a claim about survey sampling. Tests are compact
in time and an annulus r>0, smooth on the full sphere, and have enough
vanishing boundary traces for all derivatives below. A single harmonic is
allowed. Background/test regularity and measurement errors are separate.

## Necessary kinetic residual from the original equations

The action's background equations are

    3M^2 H^2=2YQ_Y-Q+rho,
    -2M^2 dot(H)=2YQ_Y+rho,
    dot(rho)+3Hrho=dot(zeta)rho,
    (Q_Y+2YQ_YY)ddot(zeta)+3HQ_Y dot(zeta)
      +2YQ_Yzeta-Q_zeta=-rho.

Hamiltonian, momentum, pressure, scalar-current, Euler and bare-number
equations must hold for a full-action solution. The following reduction
uses only a necessary subset; its residual alone is not sufficient. In
matter time set

    Xi=qJ'-q^2P-(q'+q^2)J,
    B=2Delta P/a^2-6ell(P'+ell P)-F(qJ'-q^2P)
       -(qF'-E+R)J.

The original Hamiltonian equation is B=R db+R U Xi. Bare number conservation
is db'=3P'-Delta Z/a^2. Eliminating db gives

    Ckin=B/R-3P-U Xi,
    Ckin'+Delta Z/a^2=0.                              (1)

Equivalently

    Ckin=alpha P'+beta J'+gamma Delta P+delta P+epsilon J,
    alpha=-6ell/R, beta=-q(F/R+U), gamma=2/(R a^2),
    delta=(-6ell^2+Fq^2)/R-3+Uq^2,
    epsilon=-(qF'-E+R)/R+U(q'+q^2).

Momentum and Euler independently imply

    Z'+CZ=-f, J=-Z'-P,
    f=dP'+eP, C=R/G, d=2/G, e=1+dell.                (2)

These equations do not assume Q_YY=0, a chosen scalar potential, a density
initial value, or an assigned transport integration function.

## Eliminate hidden fields in the weak test

Pair (1) with -lambda. Spatial Delta is self-adjoint for the stated measure.
After integrating by parts,

    M=integral(wP P+wJ J+wZ Z)dmu,
    wP=-(alpha lambda')'+delta lambda'+gamma Delta(lambda'),
    wJ=-(beta lambda')'+epsilon lambda',
    wZ=-Delta(lambda)/a^2.                            (3)

Let L=partial_tau+a^-1 partial_r and call the path-corrected redshift Yred=LZ;
Yred is distinct from the action's kinetic argument Y. Euler gives

    M=integral[(wP-wJ)P+vZ]dmu, v=wJ'+wZ.

The commutator [partial_tau,L]=h(partial_tau-L) yields, using (2),

    N=Yred'+(C+h)Yred+(L+h)f=-KZ, K=C'+hC.           (4)

On K!=0 set b=-v/K. The adjoint is

    Ldagger b=-b'-a^-1(partial_r b+2b/r).

Define

    g=(Ldagger+h)b,
    cP=wP-wJ-(dg)'+eg,
    cY=-b'+(C+h)b.

Then M=integral(cP P+cY Yred)dmu. The spherical divergence 2/r and
coefficient derivatives are required. K=0 is an excluded reconstruction
chart, not rejection of the underlying theory. For arbitrary P,Yred,
Z=-N/K need not satisfy the original two first-order equations.

A useful exact check retains that failure. For arbitrary P0,J0,Z0,Y0 let
rE=J0+Z0'+P0 and rN=Y0'+(C+h)Y0+(L+h)(dP0'+eP0)+KZ0. Then

    Mfirst-Meliminated=integral(wJ rE-b rN)dmu.        (5)

Nonharmonic, nonzero arbitrary probes check (5) separately from the physical
solution. They are not represented as new action solutions.

## Compose with primitive photon observations

Let conformal time satisfy d tau=a d eta, reception time u=eta+r, and
D=partial_r|tau-a partial_tau=partial_r|u. The stipulated Born map gives

    I0(u,r,n)=integral_0^r P(u-s,sn)ds,
    psi=2 integral_0^r (r-s)/(rs)P(u-s,sn)ds,
    I0=(r^2/2)Dpsi, P=(1/2)D(r^2Dpsi),
    z=Yred-2partial_u I0,
    Yred=z+a partial_tau(r^2Dpsi).                    (6)

Partial_u=a partial_tau at fixed r. The same matter-time pairing has

    Ddagger=-partial_r-2/r+a partial_tau+a'.

Thus the necessary primitive-only test is

    M=integral(Hpsi psi+Hz z)dmu=0,
    Hz=cY,
    Hpsi=Ddagger{r^2[(1/2)Ddagger(cP)-partial_tau(a cY)]}. (7)

All derivatives fall on candidate coefficients and chosen tests. One cannot
replace partial_tau(a cY) by a cY', or move r^2 through Ddagger. Equation
(7) is necessary for original solutions and is also an exact adjoint
identity for arbitrary primitives and the reconstructed hidden fields with
their residuals retained.

If psi_obs=g_obs(u)psi and z_obs=f_obs(u)z for specified positive candidate
gains bounded away from zero, replace Hpsi by Hpsi/g_obs and Hz by Hz/f_obs
after forming the adjoints. This is a test of supplied candidate gains,
not a calibration derivation. Dividing a nominally path-corrected redshift
after correction can introduce an extra reception-gain term. Different
additive/systematic observation models require their own map.

For resolved full-sky E-mode harmonics l>=2, shear gives
gamma_lm=sqrt[(l-1)l(l+1)(l+2)]psi_lm/2. A known harmonic factor can be moved
onto the weight. Unknown masks, angular extraction or finite catalogues
are not solved by this identity.

## Deterministic error budget

For fixed candidate weights and valid continuum pointwise envelopes,

    |delta M|<=integral[|Hpsi/g_obs|epsilon_psi_obs
                       +|Hz/f_obs|epsilon_z_obs]dmu. (8)

No noise independence or probability law is assumed. If the exact wrong
candidate has moment m!=0 and the right side is at most epsilon B, then
every allowed noisy version of the same records rejects that candidate
whenever 2epsilon B<|m|. Nominal exact-record rejection alone only requires
epsilon B<|m|. Background, geometry, gain, model truncation and quadrature
errors need additional bounds. A fitted candidate needs its own valid
envelope; no confidence level follows.

In the numerical example the records and weights are projected against
normalized real Y20, integral Y20^2 dOmega=1. The two-dimensional norms
therefore apply to errors in the recovered coefficients psi20,z20. For
arbitrary full-sky pointwise errors, coefficient projection instead incurs

    integral |Y20|dOmega=4sqrt(15pi)/9.

The pointwise full-sky sufficient radius is the coefficient radius divided
by this factor. Survey masks and coefficient-error extraction remain open.

Exact tensor Bernstein enclosures bound the radial/time kernel norms.
For p=sum a_kl x^k y^l on the unit square, with degrees(n,m),

    b_ij=sum_(k<=i,l<=j) a_kl binom(i,k)/binom(n,k)
                                binom(j,l)/binom(m,l).

On a cell of area A, positivity and the integrated Bernstein basis give

    A|sum b_ij|/[(n+1)(m+1)] <= integral_cell |p|
       <= A sum |b_ij|/[(n+1)(m+1)].                  (9)

Exact rational de Casteljau subdivision produces nested enclosures. No
float estimate or sampled zero contour is used to shrink an upper bound.
Known norms and conversion/subdivision controls are distinct from physics.

## Original-action witness and corrected full-ray support

Take M=1 and the explicit noncanonical candidate

    Q=(5/6)(8/25)^(3/2)exp(2zeta/5)Y^(3/2)
       -(55/12)exp(-4zeta/5),
    aE=t^(3/2), A=t^(5/2), zeta=(5/2)ln t, rho=1/(2t^2), t>0.

The local linear solution, with a common sufficiently small real amplitude,
is P=t^-3 r^2Y20, J=-2P, Z=2sqrt(t)r^2Y20, db=3P. The original background,
Hamiltonian, momentum, pressure, scalar-current, Euler and number equations
are checked. The spatial solid harmonic is regular at the observer, where
the perturbative observer terms vanish. It has no claimed global finite
energy completion. The homogeneous kinetic principal speed is1/2 in squared
units; this harmonic fixture does not measure a propagation speed.

With eta=-2/sqrt(t)<0,

    a=256/eta^8, h=-eta^7/32, q=-5eta^7/256, ell=-3eta^7/256,
    F=2/5, G=-eta^7/128, R=eta^14/32768, E=eta^14/4096,
    C=-eta^7/256, d=-256/eta^7, e=4, K=eta^14/65536,
    Utrue=65536/(5eta^14), P20=eta^6r^2/64, Z20=-4r^2/eta.

Integrate the photon paths first, with eta=u-r at the source:

    I0_20=sum_j=0..6 binom(6,j)(-1)^j u^(6-j)r^(j+3)/[64(j+3)],
    psi20=sum_j=0..6 binom(6,j)(-1)^j u^(6-j)r^(j+2)/[32(j+2)(j+3)],
    z20=eta^6r^2/64-eta^7r/32-2partial_u I0_20.

The accepted test rectangle is eta in[-4,-3], r in[1,2]. Hence reception
u lies in[-3,-1], and every entire ray eta_s=u-s, 0<=s<=r, lies in[-4,-1].
A surrounding open neighborhood can also avoid eta=0. Source t lies in
[1/4,4/9], and all rays lie in t in[1/4,4]. The spatial mode can be scaled
uniformly small on this finite patch. Fix

    lambda=(eta+4)^8(-3-eta)^8(r-1)^8(2-r)^8Y20.

Its zero extension is C7, not C-infinity. Boundary traces through seven
vanish and suffice for these finite-order integrations by parts. The general
theorem can use a smooth compact test. On the same registered records,

    M(Utrue)=0,
    M(U=0)=827093/50599790841600>0.                   (10)

The latter also equals -(9/32)integral lambda20 eta^5 r^4 d eta dr, whose
integrand is positive in the interior. Strong, first weak, hidden-field
eliminated and primitive evaluations agree. This rejects only the fixed
U=0 choice on this stipulated background and record set; it does not select
a unique Q or exclude all canonical theories with different backgrounds.

At depth3, exact rational enclosures for the two measure-weighted harmonic
kernels have combined upper bound

    B=162677295731424740783879666051795129106258197 /
      204455351051289521995092083836429520181657600.

The sufficient equal coefficient-error radius |M|/(2B) is approximately
1.0271814436e-8 at unit mode normalization. Use a strict inequality below
that radius. This radius scales with the small physical perturbation
amplitude; it is not an instrument requirement or achievable precision.

## Preserved failures and remaining suppliers

The first test window eta[-2,-1],r[1,2] was physically invalid: some whole
rays crossed eta=0 even though source events were regular. Its exact formal
moment and norm runs are preserved as algebra, not as a physical witness.
The accepted window above was declared before recomputation, with the same
action, mode, candidates and rejection rule. A sign mutation also survived
the initial harmonic-only test because Delta Z=0; nonharmonic arbitrary
probes now check that spatial operator separately. The first norm attempt
failed polynomial conversion before output; the next rejected integer ZZ
polynomials under an unnecessarily narrow QQ-domain predicate. Both are
preserved checker failures, not theory exclusions. Corrected exact arithmetic
accepts rational coefficients without changing the bound.

Time coverage remains substantive. Depths on a single past light cone do
not by themselves supply the open reception-time domain in (7). An isolated
integrated time-derivative channel can carry extra information: for
I=-2integral P_eta ds, partial_r|u I=-2P_eta at the source. Raw redshift also
contains endpoint and velocity terms. Redshift drift adds information but
needs source/observer acceleration, clock/path corrections and controlled
finite-baseline remainders; it is not directly scalar acceleration. See
[Loeb, astro-ph/9802122](https://arxiv.org/abs/astro-ph/9802122) for the
cosmological drift context. These are prospective measurement routes.

Geometric examples that vanish on one cone while changing normal jets show
what the raw map alone omits; they are not asserted to satisfy the action,
and do not prove a full-action impossibility theorem. Repeated records,
isolated path effects, statistical ensembles or characteristic evolution
could supply extra information only with their additional premises stated
and tested. A chosen evolution or population selector is not a derivation.

No empirical arrays were opened for this block. Constructed inputs are
development controls, not held-out experimental tests. Independent checks
cover adjoints, original-action photon records, exact norm arithmetic and
temporal-access qualifications with their exposure boundaries recorded in
the accompanying packet. Formal audit and shared landing checks remain
pending; no retained scientific verdict is asserted.
