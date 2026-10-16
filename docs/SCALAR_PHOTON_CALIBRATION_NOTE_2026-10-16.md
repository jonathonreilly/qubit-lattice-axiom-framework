# Joint scalar-background reconstruction with reception-dependent calibration

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
conditional_surface_status: "Local necessary identification of background coefficients and two positive reception gains from rich registered photon fields within a supplied scalar/dust class."
hypothetical_axiom_status: "The canonical action, universal matter coupling and measurement contract remain conditional premises."
admitted_observation_status: "No empirical arrays; exact original-equation fixtures and constructed derivative-level noise only."
claim_type_reason: "An explicit coefficient inverse with attainable rank, necessary original-equation checks and surviving calibration/scale freedoms."
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Test extraction and error bounds directly on primitive records, and challenge the supplied background clock/distance registration."
```

Primary runner: [scalar_photon_calibration.py](../scripts/scalar_photon_calibration.py).
It imports four helpers covering the original-equation/common-gain fixture,
separate gains, conditioning, and primitive weak residuals. Historical development and independent proofs are
preserved separately. They are provenance, not substitutes for fresh
computation or framework authority.

## Exact target and observation contract

**Target.** In the regular scalar/dust class and measurement contract below,
a rank-fourteen design of smooth registered photon histories determines at
most one local homogeneous background coefficient history and the relative
amplitude and logarithmic drifts of two positive reception gains; existence
still requires every original equation and observation residual.

This is an ideal continuum identification result. Its hypotheses do not
describe a completed observational pipeline. It does not infer the fundamental
action, independently calibrate time/distance, fix an absolute amplitude, or
select an initial-state origin. In particular, a one-shell coefficient fit is
not a physical solution.

The measured inputs are the perturbative lensing potential and redshift
channel on registered repeated past-light cones. The construction assumes
known matter scale factor a and h=a'/a, registered emission/reception times
and comoving radii, calibrated observer/source terms, same-dust tracers, the
first-order Born/null map, and recovery of the full-sky angular sector l>=2.
An arbitrary masked patch or unregistered source population is not covered.
Gains multiply the indicated perturbation channels, not an arbitrary absolute
instrument output. Each gain is a smooth positive function of reception time
only; angle-, source-radius- and frequency-dependent transfers are excluded.

Inverse weak-lensing tomography is established prior work, including
[Taylor, astro-ph/0111605](https://arxiv.org/abs/astro-ph/0111605).
Relativistic observable maps include several source, velocity and line-of-sight
contributions, as in
[Challinor and Lewis, 1105.5292v2](https://arxiv.org/abs/1105.5292v2).
The distinction between identifiable combinations and assumed cosmological
quantities is also central to
[Amendola et al., 1210.0439v2](https://arxiv.org/abs/1210.0439v2).
These references give context, not the result below. Ordinary survey statistics
are not equated with the much richer phase-resolved fields assumed here.
No novelty claim is made for inverse reconstruction.

## Premises and proof obligations

| Obligation | Treatment | Remaining premise |
|---|---|---|
| Action, species and background | Equations written explicitly and checked | Canonical scalar, one universal conformal dust species, flat homogeneous background |
| Photon/source map | Integral and coordinate identities below | Born approximation, observer/path/clock registration, recovered angular sector |
| Unknown background and gains | Commutator and fourteen-column inverse below | Positive reception-only multipliers, smooth histories and actual rank |
| Rank attainability | One exact original-action finite harmonic field | Local fixture; no survey or generic-rank assertion |
| Physical existence | Explicit residual construction below | All residuals must vanish; extracted coefficients alone are insufficient |
| Finite-data use | Conditioning, omission example and primitive weak-residual bound below | Numerical integration, finite-test information content and useful conditioning remain open |

The strongest missing bridge is a measurement protocol supplying the required
registered derivatives and rank with controlled error while independently
testing the clock/distance and instrument contracts. The supplied action and
initial-state origin remain separate scientific questions.

## Action and complete equations

Take M>0 and A(phi)>0, with

    S = integral sqrt(-gE)[M^2 RE/2-(partial phi)^2/2-V(phi)]
        - sum m integral A(phi) dsE,       gJ=A^2 gE.

Einstein time is t; matter proper time is tau, d tau=A dt, a=A aE.
A dot is d/dt and a prime is d/dtau. Let

    b=M A_phi/A, x=phi'/M, q=bx, ell=h-q,
    H_E=A ell, rE=A rho_bare, R=rE/(M^2 A^2), G=x/b,
    Fbar=-x'-3hx+2qx,
    kappa=(V_phiphi+rho_bare A_phiphi)/A^2.

The curvature derivative holds bare particle density fixed; it is not
automatically a measured pole. Use a smooth connected chart with b,x nonzero,
R>0 and hence q/G>0 and qG>0. The homogeneous equations are

    3M^2 H_E^2=dot(phi)^2/2+V+rE,
    -2M^2 dot(H_E)=dot(phi)^2+rE,
    ddot(phi)+3H_E dot(phi)+V_phi+rho_bare A_phi=0,
    dot(rho_bare)+3H_E rho_bare=0.

In the recovered l>=2 sector, the equal Einstein potentials are P. With
w=delta(phi)/M, J=bw, Z=A U, density contrast delta=delta(rho_bare)/rho_bare,
and spatial Laplacian Delta, the original linear equations are

    P'+ell P=(xw-RZ)/2,
    R delta=2 Delta P/a^2-6ell(P'+ell P)-xw'+x^2P-Fbar w,
    w''+(3h-2q)w'-Delta w/a^2+kappa w
        =-bR delta+4xP'-2Fbar P,
    Z'=-P-J,             delta'=3P'-Delta Z/a^2.

The corresponding spatial Einstein pressure equation is also required.
In Einstein variables u_phi=Mw, it is

    2M^2[ddot(P)+4H_E dot(P)+(2dot(H_E)+3H_E^2)P]
      =dot(phi) dot(u_phi)-dot(phi)^2 P-V_phi u_phi.

These equations follow from the supplied action; the source controls check
Hamiltonian propagation and pressure consistency with the four-state
momentum/scalar/Euler generator. A local traceless-Hessian metric kernel is
excluded by the stipulated full-sky l>=2 sector. The equations cannot silently
be applied to a generic masked patch.

Define background coefficients

    C=R/G, d=2/G, e=1+d(h-q).

Combining momentum with J=-Z'-P gives Z'+CZ=-dP'-eP.
The corrected radial redshift is Y=-P-J+Z_r/a, hence

    LZ=Y,      L=partial_tau+a^-1 partial_r.

These are consequences of the original system, not a replacement for it.

## Actual reception gains and the path term

Let eta be conformal time, d tau=a d eta, and u=eta+r reception conformal
time. All radial derivatives in L hold eta fixed. Cone integrals instead hold
u fixed. For the declared sector and regular/subtracted observer convention,

    I0[P](u,r)=integral_0^r P(u-s,s n) ds,
    I1[P]=partial_u I0[P],
    psi=2 integral_0^r (r-s)/(rs) P(u-s,s n) ds,
    I0[P]=(r^2/2) partial_r|u psi,
    P=(1/2) partial_r|u (r^2 partial_r|u psi).

Use the actual-event redshift convention E_z=O_observer+Y-2I1[P], with
calibrated extra source terms removed consistently. A fixed-coordinate
endpoint convention adds a source-time term and changes the separate-gain
formula; that alternative is not silently substituted here.

Let g(u) multiply lensing and f(u) multiply the redshift perturbation.
Applying the nominal path correction using the recorded lensing primitive
produces observable fields

    X=gP, B=a g I0[P],
    W=fY+2(g-f)I1[P]+2g_u I0[P].

The final term is indispensable even when f=g. A reception multiplier becomes
radially inhomogeneous on a coeval slice, so a homogeneous matter-time gain
formula cannot be reused. The integral defining B must have the same complete
registered interior convention as the primitive; no free path boundary is
assigned.

Set chi=f/g, beta=g_u/(a g), sigma=f_u/(a f), and V_g=fZ. Then

    chi'=chi(sigma-beta), Lchi=2chi',
    Lbeta=2beta'+hbeta, Lsigma=2sigma'+hsigma,
    LB=2B'-hB+X.

Put s=2(chi-1), v=-sh-2chi beta,
D=chi d and E=chi(e-d beta). The physical equations become

    (L-2sigma)V_g=T,              T=W+sB'+vB,
    V_g'+(C-sigma)V_g=-F,         F=DX'+EX.

The functions D,E generally depend on radius; LD is not D'.

## Commutator, coefficient inverse and physical compatibility

Write D_sigma=partial_tau-sigma and L_sigma=L-2sigma. Reception dependence
gives [D_sigma,L_sigma]=h(D_sigma-L_sigma). Applying this to the preceding
two equations yields

    N=(partial_tau+h+C-sigma)T+(L+h-2sigma)F=-K V_g,
    K=C'+hC.

Where K is nonzero, write k=K'/K. The necessary observable equation is

    (L-2sigma-k)N+KT=0.                         (observable relation)

For a fully explicit expansion, define

    a0=h+C-sigma, m=LD+(h-2sigma)D, n=LE+(h-2sigma)E,
    t0=s'+a0 s+v, j=v'+a0 v, z=2sigma+k, H2=h'+h^2.

The exact path identities imply

    LB'=2B''-H2 B+X'+hX,
    LB''=2B'''+hB''-H2 B'-(H2'+hH2)B+X''+2hX'+H2 X.

Thus, with target O=L(W')+hLW+h'W and ordered observed columns

    [W',LW,W,L^2X',LX',X',L^2X,LX,X,X'',B''',B'',B',B],

the observable relation is O+sum theta_i column_i=0, where

    theta1=-z, theta2=C-sigma, theta3=La0-z a0+K-h',
    theta4=D, theta5=LD+m-zD, theta6=Lm-zm+2hs+t0,
    theta7=E, theta8=LE+n-zE, theta9=Ln-zn+H2 s+ht0+j,
    theta10=s, theta11=2s, theta12=Ls+(h-z)s+2t0,
    theta13=Lt0-zt0-H2 s+2j+Ks,
    theta14=Lj-(h+z)j-(H2'+hH2)s-H2 t0+Kv.

At each common shell/time these coefficients are common across directions.
Fourteen-column rank over the available angular records uniquely extracts
them. Mixing different radii or reception times while treating coefficients
as constant would be invalid. At K=0, the relation N=0 is a nonzero relation
among these columns with coefficient one on W'; rank therefore excludes that
point. Rank is a premise tested on the actual field, not assumed from K!=0.

Because Ls=2s', theta12=4s'+(h+2theta2+theta1)s-4chi beta.
Consequently the extracted smooth coefficient histories give

    chi=1+theta11/4,              s=theta11/2,
    beta=[4s'+(h+2theta2+theta1)s-theta12]/(4chi),
    sigma=beta+chi'/chi,
    C=theta2+sigma, d=theta4/chi, e=theta7/chi+d beta,
    G=2/d, R=2C/d, q=h-(e-1)/d.

Derivatives of theta require the assumed smooth history on a neighborhood;
one isolated matrix does not supply them. All remaining coefficient identities
must hold, including theta10=theta11/2, K'/K and reception integrability.
Recovered C,d,e must be homogeneous on coeval slices. Positive chi and the
regular physical chart must be verified.

This proves at-most-one identification within the stated contract, not
sufficiency of the coefficient relation. Integrate d(log g)/du=a beta, set
f=chi g, recover V_g=-N/K and Z=V_g/f, P=X/g, J=-Z'-P and w=J/b.
Require both original first-order equations, the primitive photon equations,
all background equations, the scalar perturbation, Hamiltonian, pressure and
dust equations. The Hamiltonian may define delta; its propagation and the
other equations are still tests. Transport integration modes have not been
chosen to force a fit.

From q,G,R one has x^2=qG, b^2=q/G, A'/A=q and

    V/(M^2 A^2)=3(h-q)^2-qG/2-R.

Choose one consistent scalar orientation, integrate phi'=Mx and reconstruct
A(phi),V(phi) locally on the monotonic interval. Their action derivatives must
be used in the residuals; kappa is not a separately fitted mass. This is a
conditional on-trajectory reconstruction. The constant A normalization,
field origin/orientation, M and units, off-trajectory extensions, initial-state
origin and action-class selection remain unresolved.

There is an explicit family of realizations: multiply f,g by any common
positive constant and divide all linear physical perturbations by it. In the
perturbative domain these fields satisfy the same homogeneous linear equations
and give identical recorded primitives. The reconstruction reports the relative
gain and this family, without selecting an absolute amplitude.

## Shared-gain specialization

If the stronger observation contract f=g holds, T=W-2beta B,
F=dX'+(e-d beta)X. The same commutator yields a twelve-column relation using

    [W',LW,W,L^2X',LX',X',L^2X,LX,X,B'',B',B].

Its coefficients directly give beta=-theta10/4, C=theta2+beta,
d=theta4 and e=theta7+d beta. All physical and cross-shell residuals remain
necessary. This lower-derivative design is independently checked and is the
subject of the conditioning diagnostic below; its rank criterion is not
silently asserted for the separate-gain problem.

## Exact forward controls and limits of recovery

The supplied action has a tractable local solution with M=1,
aE=t^(3/2), phi=sqrt(5/2)log t, A=t^(5/2), rE=1/(2t^2), V=5/t^2.
Thus a=t^4 and eta=-2/sqrt(t). This background was selected for exact
calculation, not predicted or fitted to observations. The original four-state
linear equations have modes P=eta^n r^l Y_l0 for n=0,3,4,5 and l>=2;
the scalar, velocity and density are fixed by their original eigenvectors.
Solid harmonics have Delta=0 and are regular at the observer. The path
integrals are evaluated before taking derivatives:

    I0[P]=sum_{j=0}^n binomial(n,j)u^(n-j)(-1)^j r^(l+j+1)/(l+j+1).

Take g=(u+11)/10, f=(u+21)/16 and eta=-2,r=1. The actual 48-mode design
has rank fourteen and a nonzero exact minor; it recovers chi=5/4,
beta=1/10,sigma=1/20,C=1/2,d=2,e=4. The common-gain design attains rank
twelve and its corresponding values. A finite sum of distinct independent
angular harmonics is one physical linear field, and its modal rank implies
some angular evaluation matrix has the same rank. Adequately small common
amplitude preserves rank in a compact local domain. No decay at infinity,
generic rank, nonlinear stability or real-survey realization is claimed.

For a finite common-gain field with 24 harmonics and 48 Gauss–Legendre angular
samples, alternate rows are used for fitting and unused diagnostics. Column
normalization still leaves condition number about 7.30e5. A fixed synthetic
perturbation direction of relative size 1e-6 in the derivative-level matrix
and target changes recovered beta from 0.1 to about 0.06565. These are
generous derivative-level inputs, not errors propagated from photon records;
some arbitrary feature perturbations may not come from any single field.

For scaled matrix A and coefficient vector z, if ||E||<sigma_min(A),

    ||z_hat-z|| <= (||delta_y||+||E|| ||z||)
                  /(sigma_min(A)-||E||).

The synthetic cases satisfy this bound. It does not supply a useful error
budget for an actual instrument.

A deliberate omission of 2g_u I0[P] from W survives the unused angular test
at one shell exactly. It gives beta_fit=0,C_fit=0.4,d_fit=2,e_fit=3.8.
Comparing these values to the known generator is not an observational
rejection. Additional, explicitly adaptive checks reject this reconstruction:
at coeval r=0.9 and r=1.1 the inferred C and e differ by 20/9999 and 40/9999,
violating homogeneity. Reference-shell histories fail K'/K consistency by
-16/65 and original Raychaudhuri and bare-dust background equations by
-3/5 and -1/50. These are residuals of reconstructed histories, not merely
differences from generator parameters. This one failed-detection example is
preserved; no claim that every measurement error is detectable follows.

## A necessary test directly on primitive records

The coefficient inverse above differentiates ideal fields. Candidate testing
can instead use a weak residual without differentiating the observed data.
Transferring derivatives onto test functions is established prior work in
system identification, for example
[Messenger and Bortz, 2007.02848v3](https://arxiv.org/abs/2007.02848v3) and
[Reinbold et al., 1911.03365v1](https://arxiv.org/abs/1911.03365v1).
The calculation here composes that method with the stated photon/gain map;
it does not adopt a sparse library or a preferred history selector.

Work in (u,r,n) with flat measure du dr dOmega, inside a chart with a>0 and
r>0. Let T=partial_tau=a^-1 partial_u and
L=a^-1(2partial_u+partial_r), with a=a(u-r). At fixed u define

    Q=(r^2/2)partial_r,       D_r=(1/2)partial_r(r^2 partial_r).

The two primitive records are psi_obs and z_obs=f(Y-2I1), after the same
registered observer/source correction. Thus

    X=D_r psi_obs, B=a Q psi_obs, W=z_obs+2partial_u Q psi_obs.

For a fixed smooth candidate coefficient history, write its strong residual as
A_W W+A_X X+A_B B, where each coefficient multiplies the following operator's
output:

    A_W=LT+(h+theta2)L+theta1 T+(h'+theta3),
    A_X=theta4 L^2T+theta5 LT+theta6 T+theta7 L^2
        +theta8 L+theta9+theta10 T^2,
    A_B=theta11 T^3+theta12 T^2+theta13 T+theta14.

The candidate coefficients must still obey the background/reception relations;
this formulation does not turn fourteen arbitrary functions into a physical
model. For a smooth compactly supported test lambda, the formal adjoints are

    Tdagger=-T+h, Ldagger=-L+h,
    Qdagger v=-(1/2)partial_r(r^2 v), D_r dagger=D_r.

The +h terms follow from the divergence of these vector fields in the declared
coordinate measure. Another measure changes them. Reverse the operator order
and differentiate coefficient products to obtain

    H_W=Tdagger Ldagger lambda
        +Ldagger[(h+theta2)lambda]+Tdagger[theta1 lambda]
        +(h'+theta3)lambda,
    H_X=Tdagger(Ldagger)^2(theta4 lambda)
        +Tdagger Ldagger(theta5 lambda)+Tdagger(theta6 lambda)
        +(Ldagger)^2(theta7 lambda)+Ldagger(theta8 lambda)
        +theta9 lambda+(Tdagger)^2(theta10 lambda),
    H_B=(Tdagger)^3(theta11 lambda)+(Tdagger)^2(theta12 lambda)
        +Tdagger(theta13 lambda)+theta14 lambda,
    H_psi=D_r H_X+Qdagger[a H_B-2partial_u H_W].

Repeated integration by parts, with no boundary traces, proves

    integral lambda*(A_W W+A_X X+A_B B)
      = integral H_W z_obs+H_psi psi_obs = M_candidate.

The right side has no data derivatives. It still differentiates the candidate
histories and test weights, and requires their stated smoothness. Using all
compact tests gives the corresponding distributional necessary equation;
selecting finitely many tests supplies only necessary constraints.

For deterministic pointwise error envelopes epsilon_z(u,r,n) and
epsilon_psi(u,r,n), the triangle inequality gives, for each candidate and test,

    |delta M| <= integral |H_W| epsilon_z+|H_psi| epsilon_psi.

The usual L2 dual-norm version also follows. The finite-test feasibility set
consists of candidates satisfying these inequalities for every selected test,
along with the required physical conditions. If a true candidate is in the
declared class, obeys the original residual and the errors satisfy the envelope,
it belongs to that set. This deterministic implication does not need statistical
independence of candidate or test selection from data. It does not choose a
candidate, prove uniqueness or give a confidence level. Large candidate
derivatives can make the bounds uninformative. Discrete use additionally needs
controlled quadrature error and an upper enclosure of the bound integral;
sample-only error bounds do not establish continuum envelopes.

The root control integrates a nonzero-residual polynomial witness exactly with
a=1/(1+u-r), h=-1 and arbitrary polynomial theta_i on
0<u<1, 0<r<1/2. Its test is [u(1-u)r(1/2-r)]^6, extended by zero;
the boundary traces needed through order five vanish. This is a sufficiently
differentiable finite-order control, not a globally smooth bump or a physical
scalar solution. Strong and primitive-only integrals agree exactly. Deliberate
divergence, operator-order and path-adjoint-sign changes are detected. Four
explicitly bounded polynomial record errors satisfy a conservative exact dual
norm bound. These controls test the operator/error algebra; the earlier
original-action fixtures supply the physical equation checks. Neither is an
empirical test or a completed finite-data inverse.

## Review and evidence record

Root personally derived and implemented the background/gain inverses. Focused
independent checks of the background and homogeneous-gain stages are archived
with their exact source bindings. The reception checker independently derived
the path correction and common-gain coefficient expansion, constructed a
rank-twelve original-equation field, and exposed the single-shell omission
survivor and conditioning limit. Those findings are integrated above.
The separate-gain checker independently built a different temporal inverse,
then compared the exposed characteristic inverse above. On its frozen quadratic
gains, observed matrix derivatives recover the two drifts and background with
111 passing controls; the generic coordinate comparison has 20 passing
controls. These are overlapping mathematical checks, not independent
experiments or a rank-dominance result. Two replays of the historical campaign
runner timed out after producing complete matching output; the canonical
helpers exited normally and matched the stored units. The timeouts are retained.

The primitive weak lemma has a separately frozen derivation and 25 independent
controls, including a different nonzero exact witness, boundary check and five
mutations. Its unchanged author replay has 19 passing controls and seven static
canonical-correspondence checks. A separate canonical integration check found
no material mismatch, with six independent delta checks and the 19 new-helper
controls. The reviewers inspected exact frozen revisions; source movement
during packaging was detected and preserved, followed by bounded delta checks.
Root read the complete proofs, implementations and reports before integration.

The four primary units have 48, 33, 12 and 19 passing controls respectively.
Counts overlap; none is an empirical test. Historical reports, source snapshots,
failures and exact bindings are preserved in the provenance archives described
by `outputs/scalar_photon_calibration/EVIDENCE_INDEX.md`. The canonical runner
does not read those archives. Final editorial confirmation, portable closure
and mechanical checks are recorded in the milestone's `REVIEW_HISTORY.md`.
One shared current-main landing validation remains required; no landing or
audit verdict is implied by these author and focused checks.

Historical root background v1 omitted a coefficient and failed five checks;
the corrected derivation is preserved. A reception test initially left eight
power identities unsimplified; declaring the already-stated positive radial
and integral harmonic domain resolved them without removing tests. The first
separate-gain computation reached its 120-second bound; exact rational
normalization recovered the same calculation. Every failed attempt remains
in the historical evidence, with operational failures distinguished from
mathematical findings.

All scientific inputs are explicitly constructed or conditional. No observed
array is admitted, no independent empirical test is claimed, and no supplied
selector is counted as an action or initial-state derivation. Shared landing
validation and independent audit remain separate from these author controls.
