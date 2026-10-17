# Recovering a matter background without choosing scalar evolution

Claim type: bounded_theorem

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "derive background, calibration and required time coverage from observations without assuming the scalar evolution being tested"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
conditional_surface_status: "Kinematic recovery from specified distance and drift records; exact distinct scalar-background witnesses."
hypothetical_axiom_status: "FLRW geometry, operational metric and observational calibration contracts remain conditional; no new framework axiom is adopted."
admitted_observation_status: "Constructed controls only; no empirical arrays or held-out observations used."
claim_type_reason: "Explicit inverse, rank and domain conditions, error enclosures and original-equation witnesses."
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Jointly constrain scalar histories with perturbation and local-gravity channels; bound actual distance/drift systematics before empirical use."
```

Runner: [scalar_background_observations.py](../scripts/scalar_background_observations.py).
Output: `outputs/scalar_background_observations/result.json`.
The downstream consumer is the [primitive kinetic test](SCALAR_PRIMITIVE_KINETIC_NOTE_2026-10-16.md).
This block supplies a route to its **matter geometry**, not all its scalar
background coefficients or photon gains. The latter distinction is decisive.

## Question and scope

Can a background be inferred without supplying the scalar evolution that the
kinetic test is supposed to challenge? Under a declared FLRW observational
contract, relative distance and redshift drift can determine a matter expansion
history, curvature and constant distance calibration. The inverse has a
checkable identifiability condition and a version avoiding distance derivatives
when spatial flatness is supplied. These are reconstructions from records,
not parameter predictions from fundamental axioms.

The result does not identify the scalar background. Two explicit scalar/dust
actions below solve all homogeneous equations, give the same matter geometry
and matter density, and have different scalar histories and invariant matter
couplings. This is a background-level witness, not a claim that their lensing,
perturbations, local gravity or quantum theories are observationally identical.

No empirical data are used. No observational availability, precision forecast,
new cosmological law or new general inverse-reconstruction theorem is claimed.
The bridge is assembled from known kinematics, with the exact remaining
supplier tested rather than silently discarded.

## Observation contract and prior art

Use c=1, present matter scale factor a0=1, matter proper time tau, a regular
expanding FLRW interval and constant spatial curvature k (positive for closed).
Observers and sources are comoving for the homogeneous signal. Peculiar
velocities/accelerations, observer terms, anisotropy and nonlinear lensing must
be removed or bounded separately. The observational identification itself is
not derived here.

D(z) is transverse comoving distance, not radial proper distance. Let the
recorded shape be d(z)=D(z)/L with one unknown constant L>0. A shape with an
arbitrary redshift-dependent gain is outside this inverse. If d is obtained
from luminosity distance, the conversion D=dL/(1+z) requires the corresponding
photon propagation/duality contract; a calibrated brightness population is
not automatically supplied by the geometry. Define

    v(z) = (d z/d tau0)/(1+z).

The clock and redshift standards are independent inputs. Homogeneous v is
not the perturbation redshift z in the primitive kinetic note.

The standard FLRW identities are

    H(z)=(1+z)[H0-v(z)],    [H(z)D_z(z)]^2=1-kD(z)^2.       (1)

The curvature identity and its independence from Friedmann dynamics are prior
art: [Clarkson, Bassett and Lu, 0712.3457v2, equations 1–3](https://arxiv.org/html/0712.3457v2).
Redshift drift is also established prior art; see
[Loeb, astro-ph/9802122](https://arxiv.org/abs/astro-ph/9802122).
Combining drift and distance to examine geometry is not new:
[Uzan, Clarkson and Ellis, 0801.0068](https://arxiv.org/abs/0801.0068).
Only the abstract of the latter two sources was newly accessed in this block;
the equations used here are derived directly below. This is a bounded
repository implementation and identification analysis, not a novelty claim
for those cosmological ideas.

For completeness, fixed comoving source distance implies d tau_e/d tau0=1/(1+z).
Differentiating 1+z=a(tau0)/a(tau_e) gives the first identity. Writing
D=S_k(chi), chi=integral_0^z dz/H, with (S_k')^2=1-kS_k^2 gives the second.
Neither derivation uses an action, scalar equation, potential or Friedmann law.
Use the pre-turning branch D_z>0 when reconstructing the unsquared relation.

## Four-row recovery with an explicit compatibility gate

Set A(z)=(1+z)^2 d_z^2, b=L^-2 and introduce the lifted vector

    theta=(x,y,b,k)=(H0^2,H0,L^-2,k).

Equation (1) is exactly

    [A,-2Av,-1,d^2] theta = -Av^2.                       (2)

Given four distinct registered redshifts, form matrix M and right side r.
If det M is nonzero, theta=M^-1 r is the unique lifted candidate. To obtain a
physical candidate, additionally require x=y^2, b>0, H=(1+z)(y-v)>0,
D_z>0 and the unsquared radial branch, and check (2) at all other available
redshifts. Four calibration points are not four independent tests. Any failure
rejects this stipulated combination of geometry, readout contract and records,
not scalar physics alone. There may simply be no compatible FLRW history.

Proof: expansion of A(H0-v)^2=b-kd^2 gives (2); invertibility fixes theta.
The nonlinear square and sign constraints exclude extraneous lifted solutions.
On a connected interval including the observer, also require d(0)=0,v(0)=0
and the regular origin condition. With continuum compatibility and positive
orientation, the first-order equation D_z=sqrt(1-kD^2)/H and D(0)=0 reconstructs
the standard FLRW distance on its regular branch. Finite nodes alone do not
prove continuum compatibility. Invertibility is sufficient, not necessary.

An exact development fixture is

    d=(z+z^2)/2, v=1-1/[(1+z)(1+2z)],
    calibration z={1/4,1/2,3/4,1}.

Here det M=33/4096 and theta=(1,1,1/4,0), so L=2,
H=1/(1+2z), D=z+z^2. The functions satisfy (1) on z>=0; no matter dynamics
are asserted for this fixture. A fifth constructed point is a test control,
not held-out empirical evidence. A separately implemented checker used
z={1,2,3,4}, d=z+z^2 and found det M=23712, L=1.

Rank loss alone is inconclusive: d=z, v=z/(1+z) has rank three but the physical
constraints leave the unique candidate (H0,b,k)=(1,1,0); the other algebraic
candidate (0,0,-1) violates b>0. For d=ln(1+z),v=0 there really is a family:
every H0>0, L=1/H0,k=0 gives the same records. These are explicit examples,
not a classification of all singular matrices.

A computable stability certificate uses any induced norm. For perturbations
M+E,r+e, if eta=||M^-1|| ||E||<1, then

    ||theta_hat-theta|| <= ||M^-1|| (||e||+||E|| ||theta||)/(1-eta). (3)

This follows from theta_hat-theta=(M+E)^-1(e-E theta) and the Neumann bound.
It concerns the lifted inverse only. Bounds on d_z, redshift sampling and
clock errors must actually produce E,e; finite noisy distances do not supply
derivative errors for free. The nonlinear physical constraints and reconstructed
functions need interval checks after (3), not projection onto a preferred fit.

## Flat distance-integral route

If flatness is separately accepted (as in the previous kinetic note), avoid
d_z entirely. For h>sup v on [0,z2], define

    F(h,z)=integral_0^z ds / [(1+s)(h-v(s))].

Then F(h,z)=L d(z). For 0<z1<z2, solve

    F(h,z2)/F(h,z1)=d(z2)/d(z1), L=F(h,z1)/d(z1).     (4)

This removes the absolute distance scale from the h equation. If v is strictly
increasing on [0,z2], the ratio is strictly decreasing in h. To see this,
write F2=F1+G for G integrated over (z1,z2). The numerator of the derivative
of G/F1 is a double integral with positive weights and factor

    -1/[h-v(t)]+1/[h-v(s)]
      =[v(s)-v(t)]/[(h-v(t))(h-v(s))]<0,
    0<s<z1<t<z2.

Strictly decreasing v reverses the sign. Thus a compatible h is unique on
that domain; existence is not guaranteed. Constant or nonmonotone v does not
meet this sufficient criterion. For the fixture above, h=1 gives F=z+z^2,
so the inferred scale is again 2. The choice h>sup v is a regular expanding
branch restriction, not an assumed expansion law.

Interval records give a deterministic feasibility procedure. Suppose continuum
bounds v_minus<=v<=v_plus and 0<d_minus<=d<=d_plus are available and
h>sup v_plus. Compute

    F_minus=integral ds/[(1+s)(h-v_minus)],
    F_plus =integral ds/[(1+s)(h-v_plus)].

At each registered z, a compatible constant L must lie in
[F_minus/d_plus,F_plus/d_minus]. Intersect these intervals over z for each h.
An empty intersection excludes that h under the contract; a nonempty one is
only necessary when correlations or continuum constraints remain. This
procedure assumes neither a scalar potential nor an interpolating cosmology.
It still needs continuum drift envelopes: finite samples without inter-bin
regularity do not provide them. Quadrature enclosures are also required in an
empirical implementation.

## Clock, gain and time-coverage boundary

If the time rate has unknown constant gain c, the exact transformation

    v->cv, H0->cH0, H->cH, L->L/c, k->c^2 k

leaves (1)–(2) compatible with the same distance shape. An absolute clock is
therefore a named calibration input; the inverse does not derive units.
A constant distance gain can be absorbed into L. An arbitrary gain g(z) cannot:
given a different candidate distance D_new, g_new=d_observed/D_new can mask
its shape on an interval D_new>0. This is a readout ambiguity, not a theorem
that nature admits arbitrary gains. A registered units primitive does not
supply that empirical instrument response or the scalar–gravity bridge.

Finite observation duration gives a usable but conditional error budget.
Let f(tau0)=ln[1+z(tau0)] for a tracked source. A centered pair separated by
2T estimates v=f'(tau0). If endpoint log-redshift errors are at most epsilon
and |f'''|<=B3 throughout the interval, then

    |v_est-v| <= epsilon/T + B3 T^2/6.                (5)

Taylor's integral remainder proves the second term; two endpoint errors
prove the first. For positive B3,epsilon the unconstrained optimum is
T=(3epsilon/B3)^(1/3); observing windows and source stability can prevent it.
The cubic control attains the truncation coefficient. B3 is an additional
regularity bound, not something finite samples derive. An exact derivative
must not be inferred by silently sending T to zero at fixed noise.

Homogeneous a(tau) follows kinematically from H(z) via a=1/(1+z),
d tau/dz=-1/[(1+z)H(z)], up to the time origin. This does not recover an open
reception-time domain of perturbation records. The primitive kinetic integral
still needs repeated fields, masks, observer/source corrections and their
separate uncertainties. No scalar evolution has been used to fabricate them.

## Same matter background, different scalar histories

The remaining scalar-coefficient supplier is real even after ideal matter
geometry and homogeneous density are given. Fix the same Einstein normalization
M=1 and universal matter coupling exp(zeta). On tau in[1/2,1], construct two
candidate actions Q=F(zeta)Y-V(zeta), Y=dot(zeta)^2/2, with

    aJ=tau^2, A=tau^s, zeta=s ln tau,
    aE=tau^(2-s), dt=d tau/A, rhoE=tau^(4s-6)/8.

Candidate1, s=1/2:

    F=6-exp(-6zeta)/2,
    V=6exp(-2zeta)-exp(-8zeta)/16.

Candidate2, s=1/4:

    F=42-2exp(-14zeta),
    V=(63/8)exp(-6zeta)-exp(-20zeta)/16.

These functions are constructed candidates, not derived laws or observed
potentials. Direct substitution verifies all four homogeneous equations

    3HE^2=FY+V+rhoE, -2 dot(HE)=2FY+rhoE,
    dot(rhoE)+3HE rhoE=dot(zeta)rhoE,
    F ddot(zeta)+3HE F dot(zeta)+F_zeta Y+V_zeta=-rhoE. (6)

One systematic construction is to set q=s/tau, ell=(2-s)/tau,
R=rhoE/A^2, use F q^2=-2(ell'+q ell)-R and
V=A^2(3ell^2-Fq^2/2-R). Dust conservation and the first two equations then
imply the scalar equation for q!=0; (6) is also checked directly, so this
argument is not the only verification path. Such single-history action
reconstruction is known methodology, not claimed new here.

Both give rhoJ=rhoE/A^4=tau^-6/8, the same normalized A(1)=1, the same
matter expansion HJ=2/tau, and therefore the same homogeneous distances and
drift. With aJ(1)=1, HJ(z)=2sqrt(1+z) and v=2-2/sqrt(1+z).
The candidate actions are healthy at the homogeneous kinetic-sign level on
this interval: F1>=2,F2>=42-16sqrt(2)>0, and Q_Y+2YQ_YY=F>0.
This is not a global, nonlinear or quantum stability claim. The potentials
are also positive there. The runner checks monotonic positive factors giving
these signs, separately from the original-equation residuals.

They are not merely scalar coordinate relabelings with the same fixed
Einstein normalization and matter coupling. The canonical field satisfies
d chi=sqrt(F)d zeta, so the invariant squared matter slope is
(d ln A/d chi)^2=1/F. At A=1 it is 2/11 for candidate1 and 1/40 for candidate2.
Their q values differ as well. A field relabeling preserving the action and
matter coupling cannot change that invariant. Actual local-force measurement
requires its own environmental solution; no measured Newton constant is
identified with this slope here.

Thus a matter-background reconstruction cannot, by itself, replace q,F,R,E
in the primitive test by unique observations. It retires a supplied matter
expansion function only when its observational premises hold. Perturbations
and measured-gravity/environment channels are a concrete next discriminator
between these candidates, not optional details of a completed TOE.

## A tensor channel for the missing scalar history

There is a concrete prospective discriminator, beyond merely reporting the
twins. Within the same Einstein-scalar action class, the quadratic tensor action
on the spatially flat homogeneous background is

    S_T=(1/8) integral b_T^2[(partial_eta h_T)^2-(grad h_T)^2],
    b_T=aJ M/A=aE M.

No choice of Q or scalar background equation is needed to read this tensor
kinetic factor from the Einstein term. This is still conditional on that
action class, a linear transverse tensor sector and a homogeneous background.
A Fourier mode satisfies, exactly within that linear sector,

    h_T''+2(b_T'/b_T)h_T'+omega^2 h_T=0,
    mu=b_T h_T,
    mu''+[omega^2-b_T''/b_T]mu=0.                    (7)

Here primes mean conformal-time derivatives only in (7), and omega is comoving
wave number, not spatial curvature k. Neglecting the displayed masslike term
in a justified geometric-optics regime gives amplitude transport proportional
to 1/(aJ Mstar), Mstar=M/A. Relative to electromagnetic distance, and with source
amplitude normalization separated from propagation, this gives

    X_prop=dL_GW/dL_EM=Mstar_obs/Mstar_emit=A_emit/A_obs. (8)

This sign is also obtained by normalizing b_T to its observer value before
comparing aJ/b_T. The equation (7) identity is exact; interpreting (8) as a
finite-frequency observation requires a propagation-error bound not derived
here. Tensor luminosity distance is established prior art, not a new signal:
[Belgacem et al., 1712.08108v2, equations3–9](https://arxiv.org/html/1712.08108v2).

For the homogeneous twins with endpoints on their supplied backgrounds,

    X_prop,1=(1+z)^(-1/4), X_prop,2=(1+z)^(-1/8), 0<=z<=3.

They agree at the observer but differ at every z>0 in that range. This is a
conditional propagation prediction. It is not a forecast of a catalogue
measurement or a claim that unscreened compact sources exist in these models.

If an independently isolated homogeneous X_prop were available, fix the
constant normalization A=A0 X_prop and define matter-time derivatives by
partial_tau=-(1+z)HJ partial_z. Then, on q!=0 and for known rhoJ and M,

    q=partial_tau ln X_prop, ell=HJ-q,
    R=rhoJ A^2/M^2,
    F=[-2(ell'+q ell)-R]/q^2, G=Fq,
    Y=A^2 q^2/2,
    Qbar/M^2=A^2(Fq^2+R-3ell^2),
    E=[(Qbar/M^2)'-F Y']/(A^2 q).                    (9)

These primes are matter-time derivatives. Raychaudhuri and Friedmann give F
and Qbar along the observed trajectory; the chain rule
Qbar'=Q_zeta q+Q_Y Y' gives E. The action class is being tested through its
necessary equations, while no particular scalar history or potential is
supplied in (9). The runner reconstructs these coefficients for both twins
and compares with their explicit actions. This provides a conditional route
for the coefficient inputs of the primitive kinetic test. It does not uniquely
extend Q off the observed trajectory or determine Q_YY. No inference is made
at q=0, from noisy derivatives without bounds, or without density/normalization
information. The unknown A0/M normalization also remains a supplier unless
fixed by an independently justified gravitational calibration.

The important failed shortcut is equating a measured siren ratio to homogeneous
X_prop without its environmental map. Geometric optics on an inhomogeneous
scalar background uses **local** source and detector values of Mstar, not
necessarily their homogeneous values. This is treated explicitly by
[Dalang, Fleury and Lombriser, 1912.06117v3, introduction equation1](https://arxiv.org/html/1912.06117v3).
Their stated scope is luminal propagation with negligible scalar radiation.
Equal local effective Planck masses can give unity even with a changing
cosmological value. Binary generation, scalar radiation, source parameters,
orientation, photon calibration, detector response, and matching across local
environments also need independent treatment. Equation (8) cannot be used to
fit those away and then be counted as an independent scalar measurement.

For example write A_local,emit=b_emit A_background(z) and
A_local,obs=b_obs A0. The propagation ratio is then
(b_emit/b_obs) X_prop, before any source-amplitude nuisance factor. If those
endpoint factors are unconstrained, choosing b_emit/b_obs=1/X_prop yields unity
for either constructed history. This algebra does not prove such screening
solutions exist for either twin; it shows why an environmental solution must
be calculated rather than assigned. The next discriminating computation is
that local matching/source-response problem, with both candidates held fixed.

## Evidence and remaining work

The paired runner performs 54 exact development controls. A separate checker
reconstructed different sampling rows and the rank-three exception. Another
checker independently substituted both actions, checked signs and the
canonical matter-slope invariant. Independent reports and source identities
are preserved in the loop pack. Repeated symbolic identities are not 54
independent experiments. Formal audit is not performed here.

No real dataset has been fitted or tested. Distance and drift records in an
empirical run would be calibration inputs; other redshift ranges/channels
reserved before fitting could supply independent tests. The algebraic
compatibility relation is a falsifier of the full stated contract, not a
license to tune a redshift-dependent gain after seeing the residual.

Remaining obligations are actual continuum error envelopes, source/observer
corrections, observational geometry tests, time coverage for perturbations,
lensing/redshift gains, and a joint scalar/environment inference. Those are
explicit suppliers rather than claimed derivations. The tensor route above computes a conditional discriminator and identifies
its unclosed local matching and source-calibration obligations.
