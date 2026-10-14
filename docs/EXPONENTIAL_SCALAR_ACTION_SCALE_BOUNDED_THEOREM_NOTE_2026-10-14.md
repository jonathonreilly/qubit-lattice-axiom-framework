# Revised scalar action reconstruction and scale nonselection

Status: conditional support, not an observation-derived unique action or scale.
Claim type: bounded_theorem. Scientific author: /root.
Primary runner: `scripts/exponential_scalar_action_scale_check.py`.

A homogeneous history constrains the potential on its sampled field curve, but
leaves an exactly characterized normal Hessian freedom. Additional ideal local
readouts can reconstruct coupling and range only under their forward-model
premises. An overall source-free classical action coefficient also survives
unchanged stationary equations. These are constructive limits on specified
inverses and routes to additional measurements; they do not establish that a
complete observational reconstruction is impossible.

The supplied action is in [the complete action note](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md).
The local force normalization is conditional as in [the local-response note](EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md).
No measured likelihood is evaluated here. Synthetic controls are exposed model
development; a third synthetic point is an algebraic prediction control, not an
independent empirical test. Earlier source corrections and checker failures are
preserved in the recovery evidence. All three complete derivations follow.

## I. Potential first-jet reconstruction and exact degeneracy

Parent-authored derivation v2, independently checked within the scope below.
This block asks what extra observations could determine the remaining potential
assumptions. It does not choose another potential, fit data, or claim an absolute
no-go for reconstructing a theory. All previously accessed observations remain
exposed model-development material. No new empirical data enter this block.

### Conditional first-jet reconstruction

Take the candidate action class

 S=Q integral sqrt(-g)[R/2-K_AB(phi)partial phi^A partial phi^B-2Hv^2 U(phi)]
   +Sm[C(phi)g,psi],

with fixed known positive Q,Hv,K,C and signature (-+++). Put A=sqrt(C),
alpha_A=partial_A log A. These functions and the field coordinates are inputs
to this conditional inverse problem, not quantities already inferred from
expansion data. Use spatially flat homogeneous Einstein proper time t,
v^A=dphi^A/dt, H=da/(a dt), rho and p the Einstein-frame fluid variables.

The background equations in this convention are

 3H^2=K_AB v^A v^B+2Hv^2 U+rho/Q,                       (1)
 Hdot=-K_AB v^A v^B-(rho+p)/(2Q),                        (2)
 D_t v^A+3Hv^A+Hv^2 K^{AB}U_B=-alpha^A(rho-3p)/(2Q),    (3)
 rhodot+3H(rho+p)=alpha_A v^A(rho-3p).                  (4)

In (3), 3Hv^A means 3 H times v^A, not the vacuum scale Hv. If a candidate
regular field curve Gamma=phi(t), its clock, K,C, H,rho,p are known, (1),(3)
reconstruct the value and the full covector gradient of U on that curve:

 U_Gamma=[3H^2-K(v,v)-rho/Q]/(2Hv^2),                    (5)
 (dU)_A|Gamma=-[K_AB(D_t v^B+3H v^B)
                       +alpha_A(rho-3p)/(2Q)]/Hv^2.   (6)

A necessary observable-side check is

 K(v,v)=-Hdot-(rho+p)/(2Q)>=0.                          (7)

For a positive definite metric equality holds exactly where v=0. These
relations do not imply that H alone supplies the hidden field trajectory,
K,C or the Einstein-frame conversion. Even perfect physical-frame expansion
data do not by themselves provide all the inputs of (5),(6).

The value and gradient must be compatible: dU_Gamma/dt=(dU)_A v^A. Differentiate
(5), use d K(v,v)/dt=2K(v,D_t v), and substitute (2),(4). This gives exactly
the contraction of (6) with v. Thus conservation plus the Raychaudhuri equation
are a necessary integrability check; they must not be replaced by separately
chosen potential values and slopes. For a regular embedded curve segment the
compatible value and gradient have local smooth extensions, as follows by
using tubular coordinates (t,n1,n2) and choosing a potential linear in the
normal coordinates with the prescribed normal derivatives. Global extension
across self-intersections or a recurrent path can require additional
compatibility and is not asserted here.

### Exact background degeneracy and its first observable difference

Fix any smooth solution on a regular embedded segment of a three-field
space. In a tubular neighborhood choose two independent smooth functions
f1,f2 that vanish on the curve. For a smooth symmetric 2-by-2 matrix B(phi),
let

 DeltaU=(1/2) f_i B_ij f_j.                             (8)

Then DeltaU=0 and d(DeltaU)=0 everywhere on the curve. Keeping K,C,Q,Hv,
fluid and initial data the same, the original homogeneous solution is also
an exact solution of the modified local potential. Its Einstein metric,
physical metric, fluid history and any observable depending only on that
background are identical. This is exact solution correspondence, not a
numerically close fit or a stability result. A smooth cutoff equal to one
on a smaller tubular neighborhood can localize the change where such a
cutoff exists. No general statement about a whole recurrent infinite curve
or global positivity of a modified potential is required.

On the curve the covariant Hessian changes by

 Delta(U_;AB)=B_ij (partial_A f_i)(partial_B f_j).       (9)

Connection terms vanish because d(DeltaU)=0. Since df_i(v)=0, the Hessian
change annihilates the tangent vector and is otherwise an arbitrary
symmetric form on the two normal directions. Conversely any smooth
potential difference with zero first jet on the curve has Hessian
annihilating its tangent there, by covariantly differentiating d(DeltaU)=0
along the curve. Thus (9) identifies exactly the locally unconstrained
second-derivative directions, rather than just exhibiting one example.

For positive semidefinite B, DeltaU>=0 locally, so this degeneracy does not
require lowering an initially bounded-below potential. Small indefinite B
also remains possible on suitably positive, bounded neighborhoods, but no
global stability statement is made for it. At a stationary single-point
history the tangent argument does not restrict the Hessian: all directions
can change while its first jet remains fixed. If independent histories
sample an open field region and reconstruct the same value there, no such
nonzero local potential difference survives in that region. This is not a
no-go theorem for all observation sets.

Linearized scalar equations contain the mass-map change

 Delta(M^A_B)=Hv^2 K^{AC} Delta(U_;CB).                 (10)

The kinetic curvature, background velocity and matter terms in the full
linear system are unchanged by (8). The potential part of the metric stress
perturbation uses U and dU and is unchanged at first order, but propagation
can change through (10). Turning of the trajectory or matter coupling to
normal directions can make these changes visible. A normal mode decoupled
from all sampled sources and readouts may remain invisible. Neither a
constant vacuum mass nor a single Yukawa equation is being substituted for
the full rolling-background perturbation system.

### An exact degeneracy already present in the revised scalar action

Use the complete revised action fixed in this campaign, with

 a=(1-k)(1+3k)/4, alpha=sqrt(a), s=(1+k)/(k(1-3k)),
 F=1+s exp(2alpha u), J=1+(1-3a)s exp(2alpha u),
 K_u=J/F^2, C=(1+s)exp(2alpha u)/F,
 U=3/2+3s(exp(2alpha u)-1)^2/(2F^2)
   +(k/2)x^2 exp(-(1-k)u/alpha)
   +(k/3)y^2 exp(-(1+k)u/alpha)+nu(1+s)u^2/(2F^2).

For every nu>0 the vacuum u=x=y=0 with v=0,rho=p=0 is exactly the same
physical de Sitter history H=Hv,C=1. Changing nu changes neither U nor dU
there. Nevertheless it changes the matter-coupled vacuum mass by

 m_u^2/Hv^2=4[3(1+k)+nu]/(1-3k),
 Delta m_u^2/Hv^2=4 Delta nu/(1-3k).                   (11)

The vacuum coupling norm remains k. This is a direct, internally supplied
counterexample to determining nu from that history alone, even at fixed k.
It does not assert that the actual present universe is this vacuum or that
non-vacuum histories also remain identical under changing nu. It also does
not transfer the future-convergence theorem to arbitrary nu.

### A concrete additional measurement that could fix the missing mass

In a frozen vacuum, use a weak prescribed nonrelativistic mass source with
negligible pressure and stress, the Newtonian metric/force readout specified
below, and the flat static approximation. A trace-free source would not
excite this scalar response. Let q>0 be an Einstein-frame spatial wavenumber and mu=m_u/c. At C=1 the
frames have identical background lengths. To leading order in source
amplitude, before the density-feedback term (which is second order in a
scaled source) matters, solving the scalar field equation gives the
additional attractive transfer coefficient

 h(q)=k q^2/(q^2+mu^2).                                (12)

This is a defined static transfer function, not a measured PPN parameter,
an astronomical likelihood, or the full cosmological growth observable.
A Yukawa point source equivalently gives potentials proportional to
1 +/- k exp(-mu r); the acceleration instead contains
1+k(1+mu r)exp(-mu r). Mixing a potential ratio with a force readout would
be a false reconstruction. The exact curved vacuum has de Sitter geometry;
this local flat approximation requires curvature and time corrections to
be controlled on the tested scales.

For two distinct sampled q_i and inferred positive h_i, define
x_i=1/q_i^2, y_i=1/h_i. Then

 y_i=c0+c1 x_i, c0=1/k, c1=mu^2/k,
 c1=(y1-y2)/(x1-x2), c0=(x1*y2-x2*y1)/(x1-x2),
 k=1/c0, mu^2=c1/c0.                                  (13)

Compatibility of this particular action requires c0>3, c1>0 and, if Hv
has been independently determined in the same unit convention,

 nu=(1-3k)c^2 mu^2/(4Hv^2)-3(1+k)>0.                  (14)

One measurement leaves a continuous k,mu degeneracy. Two distinct exact
measurements can determine the two conditional parameters; two points
alone cannot test the affine shape. A third scale predicts
1/h3=c0+c1/q3^2. A genuine independent observation would have to be withheld
from choosing and fitting the model, with its errors and readout map fixed
before inspection. No such measurement has been accessed in this block.

The determinant of the Jacobian of (h1,h2) with respect to (k,mu^2) is

 k q1^2 q2^2 (q2^2-q1^2)/[(q1^2+mu^2)^2(q2^2+mu^2)^2]. (15)

It is nonzero for k>0 and distinct positive q_i. Algebraic identifiability
is not adequate conditioning: at q_i>>mu both h_i nearly saturate k, while
at q_i<<mu both nearly determine only k/mu^2. Finite precision and errors
can leave the mass poorly constrained. No numerical precision is supplied
by exact uniqueness.

### Assumption disposition and next derivation

Retired as a permissible inference: identical homogeneous expansion alone
fixes the off-trajectory potential Hessian. Instead its normal part is an
explicit remaining function to be constrained with perturbations or local
response. This conditional non-identifiability proof does not retire the
action, field-count, matter metric, kinetic metric, scales or initial-state
assumptions. Equations (5),(6),(13),(14) provide reconstruction formulas if
their missing physical inputs can actually be obtained; they are not new
empirical parameter determinations. The useful next route is a controlled
cosmological-to-local perturbation/readout map, including which observable
combinations can infer h(q) without presupposing the parameter to be tested.

## II. Ideal lensing and dynamical readout

Parent derivation v2, independently checked within the stated conditional scope.
No new observational data are read, fit or tested.
This develops the missing measurement map in the potential-identifiability
block; it does not identify the actual local environment with the vacuum.

Take the same complete candidate action, an exact u=x=y=0 vacuum background,
and work to first order in a weak static nonrelativistic mass source, with
negligible pressure/stress. In a locally flat region relative to the vacuum
curvature and time scale, subtract the background metric. The sole linearly
matter-coupled mode has coupling squared k>0 and inverse length mu=m_u/c>0.
All following equations require the vacuum/frozen-background/linear-source
approximation; no finite-distance error bound for a rolling environment has
been supplied. In particular, a compact astronomical body can require a
form factor and realistic equilibrium; the point-source expressions below
refer to an ideal point mass, or a body with a justified negligible form
factor, and radii outside it.

Let m=Gstar M/c^2, with C=1 at the vacuum, and use positive dimensionless
weak potentials in g00=-(1-2Phi), gij=(1+2Psi)deltaij. The scalar Helmholtz
solution and conformal multiplication give

 Phi(r)=m/r [1+k exp(-mu r)],
 Psi(r)=m/r [1-k exp(-mu r)],
 W=(Phi+Psi)/2=m/r.                                    (1)

At this order the stress of the scalar excitation beyond the constant
vacuum-energy term is quadratic about the vacuum. The constant term still
contributes to the curved-background metric equations and is neglected only
within the stated local-flat approximation. These expressions do not insert
an independent anisotropic-stress function.
Null propagation depends on Phi+Psi. The weak light deflection of the point
source is the transverse integral of grad(Phi+Psi); its magnitude at impact
parameter b is

 theta(b)=4m/b.                                        (2)

The integral is taken along the unperturbed line in the local flat static
approximation. The de Sitter background is not globally asymptotically flat;
(2) is not an exact global-lensing formula or a statement about measured
distances without geometric control.

Slow massive tracers instead measure a_dyn/c^2=-dPhi/dr, so

 a_dyn(r)=c^2 m/r^2 [1+k(1+mu r)exp(-mu r)].             (3)

Inferring m=b theta/4 from the SAME isolated source, with known physical
b,r and the required local geometry, gives the dimensionless excess

 e(r)=4 r^2 a_dyn(r)/(c^2 b theta)-1
     =k F(mu r), F(x)=(1+x)exp(-x).                    (4)

Source-mass normalization cancels in this ideal comparison. No value of Gstar
or M is required by (4), but universal matter/light coupling, source geometry,
weak-source response and a common environment remain assumptions. A mass
profile independently fitted under the tested theory must not silently replace
the lensing determination. The phrase 'mass independent' here concerns this
normalization only, not a real extended profile or source-shape uncertainty.

For 0<r1<r2 and positive inferred excesses e1,e2, take the ratio

 R=e1/e2=F(mu r1)/F(mu r2).
 L(mu)=log R=log(1+mu r1)-log(1+mu r2)+mu(r2-r1).       (5)

Then L(0)=0, L->infinity as mu->infinity, and for mu>0

 L'(mu)=mu [r2^2/(1+mu r2)-r1^2/(1+mu r1)]>0.          (6)

The last sign follows because r^2/(1+mu r) increases strictly for r>0.
Therefore every exact R>1 determines a UNIQUE positive mu within this ideal
model, after which k=e1/F(mu r1). It is compatible with this action only if
0<k<1/3 and the separately calibrated Hv gives
nu=(1-3k)c^2 mu^2/(4Hv^2)-3(1+k)>0. R<1 is incompatible with this specific
single-mode attractive Yukawa readout; R=1 gives mu=0 as a limit, which is not
a finite positive-Hv member of the stated vacuum action. Finite measurement
error and unmodeled environment effects prevent interpreting a noisy ratio
alone as an exclusion. Zero or negative measured excesses also require an
uncertainty analysis, not the positive logarithmic inverse above.

A third-radius measurement predicts e3=k F(mu r3). It can test the shape only
if it was not used in model selection/calibration. No actual measured e_i
or observational uncertainty has been supplied in this calculation.

The mathematical uniqueness is poorly conditioned for a long range:

 F(mu r)=1-(mu r)^2/2+(mu r)^3/3+O((mu r)^4),
 L(mu)=mu^2(r2^2-r1^2)/2-mu^3(r2^3-r1^3)/3+O(mu^4).

Thus small differences, not simply precise agreement in an effective Newton
constant, are needed to determine the range. For nu=1 and small k,
mu is approximately4Hv/c. A range-sensitive transition near mu r=1 then has
Hv r/c about1/4, so a parametrically controlled local-flat treatment cannot
simultaneously assume that transition scale is arbitrarily far below the
vacuum curvature scale. On much shorter scales the mass signal is suppressed
quadratically. A full cosmological/curved-background readout, or an independently
justified much heavier scalar, is needed before using the transition as a
precision measurement. This scale comparison is conditional on nu=1 and small
k and supplies neither a new fitted nu nor an actual measurement.

A finite source need not have the point-source Yukawa charge M. For a prescribed
spherically symmetric density in the same linear approximation, the external
scalar charge is weighted by sinh(mu r')/(mu r'), whereas the tensor/lensing
monopole is M. The point-source cancellation then becomes e=k F_body(mu)F(mu r).
For this finite-body comparison the lensing impact parameter b and every
dynamical radius must lie outside the body; an interior light ray requires
a projected-profile correction to (2). At fixed common body, two-radius
ratios still cancel the unknown constant
amplitude and determine mu ideally, but the recovered amplitude determines
k F_body rather than k until source shape is known. This is an explicit
remaining source input, not permission to introduce a free screening factor.
Nonlinear density feedback, pressure or time dependence can further change
this statement and have not been absorbed into F_body by assumption.

## III. Classical scale nonselection

Direct author /root, October 14, 2026. Independently checked conditional result.
No quantum theory, observation fit or universal impossibility theorem is claimed.
Units c=hbar=1 throughout.

### Which observation would identify which parameter?

At the specified constant-scalar vacuum, the supplied candidate action gives
H_E=Hv, alpha_m^2=k, Q=Q0(1+k). In its weak, unsuppressed local vacuum regime,
the measured Newton coefficient would be

    G_vac=(1+k)/(8 pi Q)=1/(8 pi Q0).

Here G_vac refers to that stipulated regime, not an assumed experimental
measurement in our actual environment. If the same physical vacuum H_vac=Hv
were independently identified, the dimensionless hierarchy would be

    r=Hv^2/Q0=8 pi G_vac H_vac^2.                      (1)

Both environmental identifications remain to be checked. In a rolling or
matter-filled cosmology, the observed present expansion H0 is not automatically
Hv; it cannot silently replace H_vac in (1). Knowing a laboratory unit standard
does not supply a gravitational/vacuum ratio. An observation can calibrate r
once its forward model is justified; that is different from a theory selecting
r before calibration.

### Source-free classical action

The inherited action is

    S_g=Q integral sqrt(-g) [R/2-K_AB grad(phi^A)grad(phi^B)-2Hv^2 U] d^4x.

K and U depend on dimensionless fields and supplied dimensionless k,nu. Write
xi=Hv*x and the dimensionless line element dbar(s)^2=Hv^2 ds^2. Thus the
physical curvature is Hv^2 Rbar and the four-volume is Hv^-4 times the barred
volume. The scalar kinetic term scales by Hv^2. Exactly,

    S_g=Xi I[gbar,phi;k,nu],
    Xi=Q/Hv^2=(1+k)/r,
    I=integral sqrt(-gbar)[Rbar/2-K_AB bargrad(phi^A)bargrad(phi^B)-2U] d^4xi.
                                                                  (2)

For every Xi>0, delta S_g=0 is equivalent to delta I=0 when Xi is a fixed
parameter rather than a varied field. The entire source-free dimensionless
classical solution set, not merely the constant vacuum, is independent of Xi.
This includes dimensionless geometric/scalar boundary or initial data held
fixed. Choosing those data is still a separate assumption. A boundary condition
that explicitly depends on Xi, a measure over histories, or variation with
respect to Xi would add a premise; none follows from the supplied equations.

Therefore the source-free classical equations and Xi-independent dimensionless
boundary data cannot select one value of r from this positive parameter family.
This is an exact limited nonselection statement. It does not assert that all
physical observations are identical when Q is changed, that matter is absent
from the universe, or that a quantum completion cannot select a hierarchy.

### A units choice is not a selection mechanism

Under a change of length unit by a factor lambda>0 with c=hbar=1, the numerical
Hv changes to lambda*Hv and the numerical Q0 to lambda^2*Q0. Thus r and Xi are
unchanged. Two theories with unequal r are not identified by a units convention.
The prefactor cancellation in the classical vacuum equations is a degeneracy
of those equations with respect to physical parameters, not license to call
an observed dimensionless hierarchy a unit choice.

### What matter and an independently known mass change

The matter stress in the metric equation enters as T/(Q Hv^2) after this
rescaling. Holding known physical matter parameters fixed does not generically
leave the same dimensionless histories when Q changes. No scaling symmetry of
the complete measured matter theory is asserted.

For a prescribed point-source worldline, S_m=-M integral ds_J. In barred
variables S_m=-(M/Hv) integral dbar(s)_J. Dividing the total classical action
by Xi leaves the dimensionless source coefficient

    M Hv/Q=8 pi m Hv,  m=M/(8 pi Q).

At fixed Hv,k,nu, scaling Q0->lambda Q0 and an UNKNOWN source mass
M->lambda M preserves this coefficient and the weak exterior geometry, clock
ratios and lensing/force parameters. It changes the physical hierarchy r by
1/lambda. This is a family of different source-mass assignments, not equal
physical masses, and is removed if M is independently known in fixed units.
It makes explicit why a gravitational readout with an uncalibrated source
cannot alone fix Q0. No universal rescaling of atomic clocks, particle masses,
thermal distributions or known laboratory masses is being adopted.

More generally, supplied stress profiles that scale with Q keep T/Q fixed;
known thermal matter with fixed particle masses need not obey that operation.
The already derived initial-value and inverse results therefore remain
conditional on matter calibration. Their dimensionless mathematics cannot be
counted as an independent prediction of Q0 or r.

### Where a new mechanism would have to enter

In a quantum amplitude exp(i Xi I), Xi is relevant even in the vacuum sector;
the preceding classical cancellation is not a quantum equivalence. Defining a
quantum state, renormalized action, measure or dynamical extra field could change
the selection problem. Those are unconstructed inputs here, not derived rules.
Extremizing over Xi merely because it is free would change the variational
problem and must not be counted as a consequence of the inherited action.
No value of r, Q0, Hv, k,nu or an initial state is selected by this argument.

### Frozen exact controls before execution

Verify the four-dimensional scaling of volume, curvature, kinetic and potential
terms, the Xi-independent variational equation, G_vac cancellation, r's unit
invariance and the physical-parameter/source rescaling separately. Use exact
rational lambda values 1/7,2,11. Keep Hv and k fixed while varying Q0: all
source-free dimensionless equations must be unchanged, while the predicted
force of a FIXED known mass changes. With the simultaneously changed unknown
source mass, m and M Hv/Q must be unchanged. The zero-Q and zero-Hv limits are
outside the stated positive domain and must not be divided through. These are
exact algebraic controls of a scoped argument, not actual observation tests.
