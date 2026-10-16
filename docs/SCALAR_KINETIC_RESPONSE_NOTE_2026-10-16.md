# Inferring scalar kinetic curvature from registered response histories

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
conditional_surface_status: "Necessary identification of normalized action derivatives from sufficiently informative registered linear responses within an explicit scalar/dust class."
hypothetical_axiom_status: "The continuum action class, universal conformal matter coupling, background and measurement contract are conditional premises, not framework derivations."
admitted_observation_status: "No empirical arrays or fitted measurements; exact constructed action solutions and declared input-error bounds."
claim_type_reason: "A response-coefficient inverse, original-action existence witnesses, explicit degeneracies and a finite-error weak test."
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Derive a calibrated observation map supplying the registered fields and background errors, then test common action derivatives across independently registered environments."
```

Primary runner: [scalar_kinetic_response.py](../scripts/scalar_kinetic_response.py).
Its five imported helpers cover the original-action family, coefficient
inverse, regular zeros, phase and action derivatives, and weak rejection.
The output is [result.json](../outputs/scalar_kinetic_response/result.json).
All are computed controls, not independent physical experiments.

## Target, measurement question and obligations

**Target.** Within the regular action and registration contract below,
real rank two in the response equation identifies the normalized transverse
kinetic curvature and the sampled action two-jet; a compatible internal
simple zero also fixes the integration constant of a single real response.

The question begins with observations: which time- and phase-resolved metric
and matter responses could distinguish kinetic laws that have the same
homogeneous evolution? The theorem takes the intermediate fields as
conditionally reconstructed. It does not claim existing surveys deliver
them, or identify a measured scalar, a complete theory, or a unique global
action. A chosen potential or boundary state is not used to close the inverse.

| Obligation | Established here | Remaining physical premise |
|---|---|---|
| General kinetic action | Original background and linear equations; explicit noncanonical solutions | This action/species class and continuum description |
| Registered response inputs | Exact necessary relations and conditional inverse | Access to a,q,G,R,P,J,Z, their phase and spatial/time registration |
| Kinetic inference | Density elimination, real rank and regular-zero formulas | Rank or zero and controlled history errors in actual data |
| Other action derivatives | Chain rules for the sampled two-jet | Smooth background reconstruction; absolute scales remain separate |
| Finite-error rejection | Fixed integral test with a conservative input bound | Background, calibration, quadrature and higher-order errors |
| Global action and origin | Explicit same-two-jet extensions | Off-history/nonlinear observations and an initial-state explanation |

The strongest missing bridge is an observation protocol that supplies these
fields and their errors without already selecting the kinetic law. A possible
downstream consumer is reconstruction from lensing, redshift and matter
motion, followed by state-matched comparisons across environments. Neither
an empirical data set nor that completed protocol is supplied here.

## Imports and domain

The following premises are explicit, with distinct roles and open bridges.

| Input | Role and provenance | Open bridge |
|---|---|---|
| Einstein gravity plus one Q(zeta,Y) scalar | Adopted candidate action; standard variational calculus | Derivation from the framework remains open |
| One pressureless species with gJ=exp(2zeta)gE | Candidate universal matter coupling and operational metric | Species universality and measured-environment identification remain open |
| Flat homogeneous background and linear scalar sector | Declared approximation | Environmental validity, mode isolation and second-order errors |
| Registered a,q,G,R,P,J,Z | Conditional continuum inputs, not imported observed values | Clock/distance, angular/spatial kernel, phase and instrument calibration |
| M and A normalization | Dimensionful conventions in equations, not fitted predictions | Inverse below identifies normalized combinations; absolute scale is not fixed |
| Smoothness, q nonzero, R positive, F positive, F+S positive | Local regularity and positive principal kinetic coefficients | Conditions must hold in any application; no global stability assertion |

The approved scale-reference primitive only supplies a ruler; it does not
derive these dimensionless laws or identify the scalar coefficient with
measured gravity. The realized-state primitive permits evaluation at a state;
it does not select the state, response, or probability distribution. Kinetic
isotropy of the framework regulator does not itself identify this candidate
continuum Q or its measured propagation cone. No primitive registry is changed.

Ordinary kinetic effective metrics and sound speeds are established theory;
see [Garriga and Mukhanov, hep-th/9904176](https://arxiv.org/abs/hep-th/9904176).
Reconstruction from background and linear perturbations, including freedom
in higher-order action terms, is prior art; see
[Kennedy, Lombriser and Taylor, 1705.09290v2](https://arxiv.org/abs/1705.09290v2).
The contribution proposed here is the explicit conditional response inverse
and its controls. No novelty claim is made for inverse reconstruction or
kinetic freedom itself.

## Original equations and the necessary transport relation

Locally use zeta=ln A as scalar coordinate; the original coupling derivative
must be nonzero for this chart. Define

    S=integral sqrt(-gE)[M^2 RE/2+Q(zeta,Y)]-sum m integral exp(zeta) dsE,
    Y=-(partial zeta)^2/2, gJ=A^2 gE, A=exp(zeta).

Dots mean Einstein time t; primes mean matter proper time tau, d tau=A dt.
Write v=dot(zeta), H=dot(aE)/aE, a=A aE, h=a'/a, q=zeta', ell=h-q,

    F=Q_Y/M^2, G=Fq, R=rho/(M^2 A^2),
    Pi=Q/(M^2 A^2), E=Q_zeta/(M^2 A^2),
    D=Q_Y+2YQ_YY, S_kin=2YQ_YY/M^2.

S_kin is a coefficient, distinct from the action S. Below abbreviate it as
s. rho is Einstein matter energy density, not bare particle density.
The background equations are

    3M^2 H^2=2YQ_Y-Q+rho,
    -2M^2 dot(H)=2YQ_Y+rho,
    dot(rho)+3Hrho=v rho,
    D dot(v)+3HQ_Yv+2YQ_Yzeta-Q_zeta=-rho.

The equal Einstein potentials are P, scalar perturbation J=delta zeta,
covariant dust velocity potential Um, and bare density contrast db. Equality
of the metric potentials and integration of the momentum gradient require
a specified sector with the homogeneous/traceless-Hessian kernels excluded,
for example the declared full-sky l>=2 convention. They cannot silently be
inferred on an arbitrary local masked patch. Let deltaY=v dot(J)-v^2P.
The complete scalar equations in this sector include

    2M^2[dot(P)+HP]=Q_YvJ-rho Um,
    2M^2 Delta P/aE^2-6M^2H[dot(P)+HP]
       =D deltaY+(2YQ_Yzeta-Q_zeta)J+rho(db+J),
    2M^2[ddot(P)+4Hdot(P)+(2dot(H)+3H^2)P]
       =Q_Y deltaY+Q_zeta J,
    dot(Um)=-P-J-v Um, dot(db)=3dot(P)-Delta Um/aE^2.

For completeness set j=Q_Yv and delta j=D[dot(J)-vP]+vQ_Yzeta J.
The scalar-current variation is

    dot(delta j)+3H delta j-3j dot(P)-[dot(j)+3Hj]P
      -Q_Y Delta J/aE^2-Q_zetazeta J-Q_zetaY deltaY+rho(db+J)=0.

These follow by varying the supplied action, scalar current and particle
number current. Independent checks use direct metric/stress variations.
The controls below verify the full original equations for their fixtures.

With Z=A Um the momentum and Euler equations become

    P'+ell P=(GJ-RZ)/2, Z'=-P-J.

For G nonzero define C=R/G, d=2/G, e=1+d ell. Elimination gives
Z'+CZ=-dP'-eP, without setting Q_YY to zero. If a valid observation inverse
supplies C,d,e and h, then G=2/d, R=2C/d, q=h-(e-1)/d. This statement is
necessary only: it neither proves observable rank nor imports a sibling PR's
photon/calibration theorem. General-Q Hamiltonian and scalar equations must
be used for further checks; canonical residuals cannot certify this class.

The background determines

    Pi=qG+R-3ell^2,
    -2(ell'+qell)=qG+R, R'=(2q-3h)R,
    E=[Pi'+2qPi-G(q'+q^2)]/q=G'+(3h-2q)G+R.

The last equality uses the preceding background constraints. YQ_Y-Q is a
background combination, not a fundamental potential for arbitrary Q.

## Density elimination and response inverse

Assume the registered fields probe the same background state. Define

    Xi=qJ'-q^2P-(q'+q^2)J,
    B_density=2Delta P/a^2-6ell(P'+ell P)
                -F(qJ'-q^2P)-(qF'-E+R)J.

Since Y'=A^2 q(q'+q^2),

    deltaY-(Y'/q)J=A^2 Xi,
    delta rho_Q/(M^2 A^2)
       =F(qJ'-q^2P)+(qF'-E)J+s Xi.

The second identity follows by substituting
F'=qQ_Yzeta/M^2+Y'Q_YY/M^2 into the original density variation, so no mixed
action derivative is selected independently. The Hamiltonian is therefore
B_density=s Xi+R db. Number conservation eliminates db's derivative:

    V=(B_density/R)'-3P'+Delta Z/a^2=(U Xi)', U=s/R.

Stack independent real responses, and the real and imaginary parts of
available complex responses, into rows [Xi,Xi'] with right side V. U and U'
are real. At real rank two the system identifies theta=(U',U). For two real
responses W=Xi1 Xi2'-Xi2 Xi1' nonzero gives

    U=(Xi1 V2-Xi2 V1)/W,
    U'=(V1 Xi2'-V2 Xi1')/W.

For one complex response Wc=Im(conj(Xi)Xi') nonzero gives

    U=Im(conj(Xi)V)/Wc,
    U'=Im(conj(V)Xi')/Wc.

Both quadratures are needed; a complex label on one real measurement adds no
information. Constant phase rotations leave this inverse invariant, while
an unregistered time-dependent phase changes it. If Xi=r exp(i theta),
Wc=r^2theta'. Multiple angular channels with the same temporal response need
not add rank. Xi identically zero gives no s information through this map.

The reconstructed U' must equal dU/dtau; unused rows and every original
field equation must also agree. These are compatibility tests, not identities
for arbitrary records. One fixed-phase response away from zeros permits the
homogeneous freedom C/Xi, restricted so U stays real. A changing complex
phase can remove that freedom; it is incorrect to say two histories are
always required.

At an internal simple zero tau0, continuous U, smooth Xi, continuous V and
an absolutely continuous U Xi imply

    U(tau0)=V(tau0)/Xi'(tau0),
    U(tau)=integral_tau0^tau V(s)ds/Xi(tau).

This fixes the constant where Xi is nonzero. Further zeros require compatible
vanishing integrals and finite limits; identically zero intervals remain
uninformative. A noisy near-zero does not supply an exact zero. If the extra
bound |U|<=B is known, its leftover constant is bounded by B|Xi(tau0)|,
giving B|Xi(tau0)|/xi_min away from zeros, plus integration and input errors.

For a fixed subordinate matrix norm and declared column units, if
eta=||M^-1 deltaM||<1, the ordinary inverse perturbation bound is

    ||delta theta|| <= ||M^-1||/(1-eta)
                       [||deltaV||+||deltaM|| ||theta||].

Exact rank is not experimental conditioning. The runner's small algebraic
matrix example uses the induced infinity norm; it is not an empirical error
certificate or a replacement for controlling differentiated inputs.

## Sampled action derivatives and constructed tests

The inverse yields s=RU and

    c_s^2=F/(F+RU), D/M^2=F+RU,
    B=A^2Q_YY/M^2=RU/q^2,
    L=Q_Yzeta/M^2=F'/q-B(q'+q^2),
    Q_zetazeta/(M^2 A^2)=(E'+2qE)/q-L(q'+q^2).

The last two equations are chain rules along the actual sampled curve. They
require background derivative control. They identify normalized derivatives,
not absolute Q_YY without A and M. The sound speed follows from the local
principal scalar Hessian; it is not measured by a homogeneous mode alone.

An explicit full-action family, in M=1 and normalized Einstein-time units,
has t>0, n>1/2 and

    Q=K0 exp[4(n-1)zeta/5]Y^n-V0 exp(-4zeta/5),
    K0=5/(4n)(8/25)^n, V0=15/4+5/(4n),
    aE=t^(3/2), zeta=(5/2)ln t, A=t^(5/2), rho=1/(2t^2).

Every member obeys the four background equations. Along the curve,
F=2/5, D/M^2=(2/5)(2n-1), E=4t^-7, G=t^(-7/2), R=(1/2)t^-7 and
c_s^2=1/(2n-1). The shared background and transport coefficients do not mean
every linear response is shared. For example the arbitrary-k original
generator gives a different dot(J) at the same specified constrained state.

Local nonconstant harmonic spatial profiles admit P=t^m, J=jP,
Um=u tP, db=bP. Two common modes are
(m,j,u,b)=(0,5/2,-1,-9/2) and (-5/2,-5/3,2/3,3). Both have Xi=0.
The other exponents satisfy

    (2n-1)m(2m+7)+6=0,
    j=(2m^2+10m+10)/(m+4), u=2(j-2m-3), b=3.

The tested n=1,3/2,2 pairs have nonzero W and recover
U=(4/5)(2n-2)t^7. The original equations verify the selected modes. This is
not a claim of a complete eigenbasis at repeated roots (n=97/98 or 11/10),
nor coverage of the excluded displayed denominator m=-4. Harmonic profiles
are local with unspecified boundary completion; they are not nonzero global
square-integrable Fourier modes or observed propagation speeds.

For n=3/2 a real superposition with weights 1 and 7/8 gives an internal
simple zero at t=1, Xi'(1)=-75/8, V(1)=-15/2 and U(1)=4/5. A phase-aware
example instead combines the m=-3 and -1/2 modes with weights 1 and i:

    P=t^-3+i t^-1/2,
    J=-2t^-3+(11/7)i t^-1/2,
    Um=2t^-2-(6/7)i t^1/2, db=3P.

Use the fixed complex harmonic H=(x^2-y^2)+2i xy and real physical fields
Re(PH), Re(JH), and similarly for the matter fields. Independently resolved
real/imaginary spatial components supply the two quadratures. If H were
real and only a real projection were retained, one quadrature would be lost.
The constructed response has no complex Xi zero and
Wc=-1125/(28t^21), recovering U=4t^7/5. All original linear equations hold.
The normalized time choice is not a scale prediction: restoring t0,A0 gives
U=(4/5)A0^2 t0^2(t/t0)^7 for this member.

Finally, if Y=y(zeta) describes the sampled history, the explicit additions
lambda(zeta)[Y-y(zeta)]^3 share its value and full two-jet. The runner
differentiates those additions directly, including mixed derivatives. They
are concrete alternative extensions, not a theorem about every enlarged
theory or a selected nonlinear dynamics.

## Weak rejection with bounded metric-record errors

For a fixed Fourier eigenvalue Delta=-k^2, fixed candidate U, and registered
background, set

    alpha=-6ell/R, beta=-q(F/R+U), gamma=2/(Ra^2),
    delta=(-6ell^2+Fq^2)/R-3+Uq^2,
    epsilon=-(qF'-E+R)/R+U(q'+q^2).

Then B_density/R-3P-U Xi=alpha P'+beta J'+(delta-k^2gamma)P+epsilon J.
For lambda and lambda' zero at both endpoints, integration by parts gives

    integral (wP P+wJ J+wZ Z) d tau=0,
    wP=-(alpha lambda')'+(delta-k^2gamma)lambda',
    wJ=-(beta lambda')'+epsilon lambda', wZ=k^2 lambda/a^2.

Thus this necessary test differentiates no measured P,J,Z. It still uses
background/candidate derivatives and presupposes their calibration. If
|delta P|<=epsP, |delta J|<=epsJ, |delta Z|<=epsZ, the moment error is bounded
by integral(|wP|epsP+|wJ|epsJ+|wZ|epsZ)d tau. Add independently justified
background, quadrature, calibration and higher-order error budgets separately.
Passing finitely many moments does not establish all original equations.

The fixed test is the n=3/2, m=-3 local harmonic member on t in [1,2],
lambda=(t-1)^3(2-t)^3. True U=4t^7/5 gives zero. Wrong canonical U=0,
keeping the same registered background and records, gives dt weights

    wP_dt=18t lambda_tt-7lambda_t,
    wJ_dt=2t lambda_tt+9lambda_t, wZ_dt=0,
    M_wrong=9 integral_1^2 lambda t^-4 dt=567 ln 2-393>0.

Expanding each weight in x=t-1 and summing absolute monomial integrals
gives the conservative rational bound K=630 for their combined L1 norm.
For uniform P,J error eps, worst-case rejection still holds when
eps<M_wrong/(2K), approximately 1.14693472135e-5 in the fixture's unit
amplitude. The factor two allows both actual input perturbation and the
candidate acceptance tolerance. Scale all perturbations and this allowance
by a common sufficiently small amplitude for linear theory; no unit-amplitude
nonlinear accuracy is asserted. The bound assumes exact background and
integration here. This is synthetic rejection of a fixed wrong kinetic
coefficient, not observed exclusion of a physical theory.

## Review record and open work

The root author derived, implemented and integrated this result directly.
Focused independent work derived original action/current equations, a separate
noncanonical family check, and the density-response inverse before reading
the new author sources. Subsequent comparisons exposed and corrected the
overbroad one-record wording for real coefficients with complex data.
The local harmonic/boundary and phase-projection qualifications above are
explicit; the induced infinity norm is correctly named. Historical sources,
the independent normalization failure and its narrow repair are preserved.

The canonical and independent check records are in the campaign packet;
shared landing validation and independent audit remain pending. Author
checks do not assign an audit outcome. All load-bearing executable helpers
are imported by the primary runner, so no helper-registry edit is proposed.
At landing, regenerate the citation manifest and run the shared integrated
pipeline, strict lint and changed-evidence gates on the actual landing tree.

This block replaces the selected canonical kinetic form with conditional
tests for its coefficient on sampled states. It leaves open the action class,
source/species correspondence, state/history origin, actual field extraction,
finite-background errors, scales and nonlinear extension. No observed target
value, selected initial condition, or chosen potential is counted as derived.
