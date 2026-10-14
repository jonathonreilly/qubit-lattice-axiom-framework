# Physical-clock past bounds and conditional gravity calibration

**Date:** 2026-10-14
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [exponential_scalar_physical_past_check.py](../scripts/exponential_scalar_physical_past_check.py)

The complete supplied action is in the
[future-confinement note](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md).
The normalization of the local source response is derived in the
[local-response note](EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md).
The [curvature reconstruction](EXPONENTIAL_SCALAR_CURVATURE_LOOPHOLE_BOUNDED_THEOREM_NOTE_2026-10-14.md)
shows why positive curvature deserves a separate analysis.
These dependencies supply an explicitly conditional action, not a derivation of
that action from the framework primitives or observations.

The observable targets are physical expansion, spatial curvature, radiation
density and a calibrated local gravitational response. The equations below
turn specified targets into necessary conditions; none of the target tolerances
is declared to be measured here. Primary scalar-tensor BBN work distinguishes
cosmological and Cavendish couplings and treats mass thresholds and a varying
expansion rate dynamically. A single speed-up tolerance is not a light-element
likelihood. See [Coc et al., equations30–31 and sectionIII.A.6](https://arxiv.org/pdf/astro-ph/0601299).
This is an exposed development source; its model-specific histories and dated
numerical observations are not transferred to this three-field candidate.

The result applies to homogeneous classical histories with positive separately
conserved radiation and stated nonnegative matter density/enthalpy. An earlier
physical stationary event, or a quantitatively slow event, contradicts a later
near-flat bare radiation-law target. Under that target a bounded physical past
has a finite proper-time bound. A distinct derivation relates this obstruction
to a positive local calibration only in its stated response regime; the required
environment, error estimate and actual data comparison remain open.

The three proof parts below retain their own equation numbering. Here a_E,a_J
are scale factors; the symbol a in action identities is the fixed positive
parameter (1-k)(1+3k)/4. No energy fraction is equated with an H-normalized
fraction at a turning point.


## I. Finite physical stationary event

Direct candidate theorem by /root, extending the separately checked-domain
Einstein-bounce comparison. This closes a possible frame loophole only under
explicit additional interval premises; it is not a measured exclusion of the
scalar theory. The physical radiation diagnostic uses bare Q/C, and the
observational calibration of that coefficient remains open.

Use dimensionful Einstein time t, H=H_E, v=dot(phi), b=d ln A, q=|b|_K^2,
A=sqrt(C)>0, Z=H+b.v, H_J=Z/A and kappa=Kc/a_E^2. The supplied action gives

    3Q(H^2+kappa)=Q|v|_K^2+V+rho_r+rho_m,
    V=2Q H_v^2 U>=3Q H_v^2>0,
    Hdot=kappa-|v|_K^2-[rho_m+p_m+(4/3)rho_r]/(2Q).

Assume all fields/metrics remain regular on a closed finite time interval
[t_b,t_f], Q>0, rho_r>0, rho_m>=0 and rho_m+p_m>=0. The candidate's positive
scalar metric and full action give

    q=a_k/J<a_k<1/3,
    a_k=(1-k)(1+3k)/4,
    J=1+(1-3a_k)s exp(2sqrt(a_k)u)>1.

Radiation is separately conserved throughout: rho_r a_E^4=constant. The
initial event is only a physical stationary point Z_b=0; it need not be an
Einstein bounce or even a strict physical minimum. The later event has Z_f>0
and d_f=kappa_f/Z_f^2<=1. We will derive Kc>0 rather than adopt it separately.

### 1. A physical stationary event requires positive curvature

At Z_b=0, H_b=-b.v_b and H_b^2<=(q_b)|v_b|_K^2. Therefore

    3Q kappa_b
      =Q[|v_b|_K^2-3(b.v_b)^2]+V_b+rho_r,b+rho_m,b
      >=Q(1-3q_b)|v_b|_K^2+V_b+rho_r,b+rho_m,b
      >rho_r,b.                                     (1)

Thus kappa_b>0 and Kc>0, and f_b=rho_r,b/(3Q kappa_b)<1.
This does not require Hdot_J,b>0. Positivity of V makes the final inequality
strict even if v_b=0. The coupling-norm condition and density assumptions are
substantive; they are supplied-action consequences/interval premises, not a
general theorem about arbitrary scalar-tensor theories.

### 2. The later near-flat physical expansion has H_f>0

If H_f<=0, put t=-H_f/Z_f>=0. Since Z_f>0,

    b.v_f=Z_f-H_f=Z_f(1+t).

Cauchy-Schwarz and the positive-energy constraint give

    Z_f^2(1+t)^2 <= q_f |v_f|_K^2
                       < 3q_f(H_f^2+kappa_f).

Consequently

    d_f > (1+t)^2/(3q_f)-t^2
         =1/(3q_f)+2t/(3q_f)+(1/(3q_f)-1)t^2 > 1.     (2)

This contradicts d_f<=1. Hence H_f>0. The proof covers H_f=0 as well;
the intermediate strict inequality uses V+rho_r+rho_m>0. No equality at a
zero field-space norm q is needed; the candidate has q>0 at regular points.

### 3. Chronological split removes the radius ambiguity

If H has no zero in [t_b,t_f], continuity and H_f>0 imply H>0 throughout.
Thus a_E,f>a_E,b (for distinct events). Conservation and curvature scaling give

    f_f := rho_r,f/(3Q kappa_f)=f_b(a_E,b/a_E,f)^2<1.

If H has a zero, let t_* be its last zero before t_f. It exists because the
zero set is closed in the compact interval and H_f>0 gives a zero-free final
neighborhood. On (t_*,t_f] H>0, so a_E,f>a_E,*. Differentiability and positivity
to the right imply Hdot_*>0 or Hdot_*=0. The Raychaudhuri equation and
nonradiation enthalpy>=0 then give

    kappa_* >= 2rho_r,*/(3Q),
    f_* <= 1/2,
    f_f=f_*(a_E,*/a_E,f)^2 < 1/2.                    (3)

A tangential zero, a degenerate crossing or a zero at t_b is allowed. We do
not divide by H or presume a strict Einstein bounce. The interval equations
and nonradiation enthalpy assumption are crucial in this second case.
Both cases yield f_f<1.

### 4. Physical consequence and remaining empirical boundary

At the final event use the actual physical spatial curvature and radiation
density but retain the bare physical Ricci coefficient Q/C:

    d_J=Kc/(a_J^2 H_J^2)=kappa/Z^2,
    F_r,J=H_J^2/[C rho_r,J/(3Q)]=3QZ^2/rho_r.

Their product is 1/f_f, so the necessary conclusion is

    d_J F_r,J > 1.                                  (4)

In the case with an intermediate Einstein zero it is >2. Therefore an earlier
regular physical turning point cannot precede a later physical expanding event
that simultaneously has d_J<=epsilon<=1 and F_r,J<=1+delta with

    epsilon(1+delta)<=1, delta>=0.                    (5)

This is a conditional obstruction to a near-flat GR-like radiation law using
the bare coupling, not a numerical CMB/BBN fit or local measured-gravity result.
Present near-flatness and positive CMB temperature alone do not imply (5),
because radiation does not dominate the present expansion. No observed bound
is silently transferred from LambdaCDM. Physical effective scalar density is
not equated with Einstein scalar energy.

The theorem does not derive a singular origin, choose a state, prove global
completeness, or exclude quantum/inhomogeneous alternatives. Radiation charge
production or exchange, a changed action/coupling norm, or violations of the
positive density/enthalpy premises can evade its domain. Naming such a route
is not deriving an energy-transfer mechanism or a new viable theory.

## II. Quantitative slow past and bounded duration

Direct candidate extension by /root. The earlier physical-turnaround proof
requires an exact finite event Z=0. Here that condition is replaced by an
explicit inequality. The supplied action itself bounds the coupling norm
uniformly at fixed k, so a physical Hubble rate tending to zero also enters
the forbidden class. No new initial-state selector is introduced.

Use the complete action and definitions from physical_turnaround_bound_v1:
H=H_E, w=|dot(phi)|_K^2, L=b.dot(phi), q=|b|_K^2<1/3, Z=H+L,
C=A^2, H_J=Z/A, kappa=Kc/a_E^2, V=2Q H_v^2 U>=3Q H_v^2>0.
Positive radiation is separately conserved and other density/enthalpy is
nonnegative. All connecting finite time intervals must be regular. Parameters
0<k<1/3,nu>0,Q>0,H_v>0 are fixed; no uniform endpoint-parameter limit is used.

### Exact local completion and a sufficient slow-event condition

Decompose v into its component along b^sharp and its K-orthogonal complement.
Since q>0, w=L^2/q+w_perp with w_perp>=0. The constraint gives

    3Q kappa-rho_r = V+rho_m+Q[w-3(Z-L)^2],
    w-3(Z-L)^2
      =w_perp+(1-3q)/q [L+3qZ/(1-3q)]^2
        -3Z^2/(1-3q).                               (1)

Thus an earlier event obeying

    Z_b^2 < (1-3q_b)(V_b+rho_m,b)/(3Q)                (2)

necessarily has 3Q kappa_b>rho_r,b>0. It has positive curvature and
f_b=rho_r,b/(3Q kappa_b)<1, exactly the intermediate conclusion needed
by the physical-turnaround chronology proof. No actual zero, minimum,
Einstein bounce, or sign of H_J at this earlier event is required.

If a later event has Z_f>0 and d_f=kappa_f/Z_f^2<=1, the original endpoint
argument still proves H_E,f>0. The same no-zero/last-zero split therefore
gives f_f<1 and

    d_f F_bare,f > 1,                                (3)

with >2 in the last-Einstein-zero branch. All original conservation,
positivity and regularity premises remain essential. Condition (2) is
sufficient, not necessary, and is not an observational error bar on H.

### An exact action-wide physical slow-rate threshold

Let a=(1-k)(1+3k)/4, beta=1-3a=(1-3k)^2/4>0 and
Cmax=(1+s)/s, s=(1+k)/(k(1-3k)). At any finite field point, 0<C<Cmax and

    q=a(1-C/Cmax)/(1-3a C/Cmax),
    (1-3q)/C=beta/[C(1-3a C/Cmax)].                  (4)

Completing this scalar quadratic gives

    Cmax/(12a)-C(1-3a C/Cmax)
       =(3a/Cmax)[C-Cmax/(6a)]^2 >=0.

The denominator is positive on the action domain. Therefore

    (1-3q)/C >= 12a beta/Cmax,
    h_* = H_v sqrt(12a beta/Cmax) > 0.               (5)

The coupling-only minimum occurs at C=Cmax/(6a), inside the allowed interval
because a>1/4. This does not minimize the full potential-dependent threshold
in (2), or select that field value. It is an exact conservative uniform bound.

Since Z^2=C H_J^2 and V>=3Q H_v^2, any finite earlier event with

    |H_J| < h_*                                      (6)

satisfies (2). A sequence of physical Hubble rates tending to zero along
an arbitrarily remote past therefore contains a sufficient finite event;
there is no need to include the infinite endpoint in a compactness argument.
This also works when C tends toward a boundary, provided every finite
connecting segment is regular and the parameters stay fixed.

### A bounded-past duration corollary

Suppose a later event satisfies the exact symbolic target

    H_J,f>0, d_f<=1, d_f F_bare,f<=1.                (7)

Then no earlier finite event in a connected regular interval satisfying the
same matter/action premises can obey (6), because it would contradict (7).
Hence |H_J|>=h_* throughout that earlier interval. Continuity and H_J,f>0
force the positive sign, including near the final event; otherwise a zero
or an open neighborhood of small magnitude would occur. Thus

    H_J >= h_*,
    a_J(t_J)<=a_J,f exp[-h_*(t_J,f-t_J)].             (8)

For any additionally required lower physical radius a_J>=a_min>0,

    t_J,f-t_J <= log(a_J,f/a_min)/h_*.               (9)

An unbounded past proper-time interval with a positive lower physical scale
factor is therefore impossible under (7) and these hypotheses. If instead
one postulates an upper bound rho_r,J<=rho_max>=rho_r,J,f, separate physical
radiation conservation rho_r,J a_J^4=constant gives the equivalent duration

    t_J,f-t_J <= log(rho_max/rho_r,J,f)/(4h_*).        (10)

The density/radius cutoffs are explicit additional conditions, not derived
fundamental scales. If the physical past duration is unbounded with no such
cutoff, (8) forces a_J to zero and rho_r,J to infinity in that limit. This
is not a proof of divergent physical curvature, finite-time singularity,
spacetime inextendibility or geodesic incompleteness: C may vary strongly,
and no Einstein energy is silently equated with Jordan effective energy.

The bare target (7) must be distinguished from a measured local-gravity
radiation law. The separate gravity_calibration_v1 analysis supplies only
conditional conversion inequalities, not a data likelihood. Present CMB
radiation and present near-flatness alone are not (7). Neither changing a
potential within the stated positive lower bound nor choosing a special
radiation charge repairs the obstruction; production/exchange, a changed
action, positivity failures or a different empirical target leave its domain.

## III. Local calibration and environment energy requirement

Direct derivation by /root. The physical-turnaround result uses the bare
squared-Planck coefficient Q/C. This block connects that diagnostic to the
previously derived leading weak-source gravitational coefficient, and makes
its environment dependence explicit. It does not assert that any laboratory
or primordial-element measurement satisfies the local approximation.

### Supplied action and the local coefficient

Use the full supplied action, Q=Q0(1+k), 0<k<1/3, nu>0 and finite fields.
Write a=(1-k)(1+3k)/4, s=(1+k)/(k(1-3k)), E=exp(2 sqrt(a) u),
F=1+sE, J=1+(1-3a)sE and C=(1+s)E/F. The matter covector is
b=(sqrt(a)/F,0,0) and its field-metric squared norm is q=a/J<1/3.
For a weak nonrelativistic source in a locally frozen background, when the
spatial principal operator dominates mass, mixing and time variation, the
scalar Green function and physical mass/radius conversion give

    G_pr(phi)=C(phi)(1+q(phi))/(8 pi Q).
    G_bare(phi)=C(phi)/(8 pi Q).                       (1)

These are coefficients in the source response, not a fit to a measured
finite-body force or a choice of a screening factor. This normalization
was independently checked in the earlier local and rolling response blocks.

A separately conditional extension includes a constant positive field metric
and a self-adjoint nonnegative mass-squared operator. Whiten the field metric
and diagonalize the operator. With orthonormal eigenvectors e_i and masses
m_i>=0, put w_i=(e_i dot K^(-1/2)b)^2, so sum_i w_i=q. The static point-source
force at Einstein radius r then has coefficient

    G_force(r)=G_bare [1+sum_i w_i (1+m_i r) exp(-m_i r)]. (2)

The physical radius is sqrt(C)r at the frozen background. Since
0<=(1+z)exp(-z)<=1 for z>=0, G_bare<=G_force<=G_pr. This does not certify a
positive operator at every field point, a static global solution around
an arbitrary background, finite-body sensitivities, environmental matching,
or a controlled cosmological remainder. Negative eigenvalues or additional
source/boundary modes are outside (2), not suppressed by declaration.

### Same background: enhancement cannot be chosen arbitrarily

Let the cosmic event have C_c. Throughout this comparison require G_cal>0
and hence gamma>0; use target/error parameters 0<epsilon<=1, delta>=0 and
eta>=0. Positivity follows from (1) and (2) in their stated domains, but
must be added explicitly when only a calibration error ceiling is supplied.
Set
F_cal=H_J^2/[(8 pi G_cal/3)rho_r,J]. Its relation to the bare diagnostic is

    F_cal=F_bare / gamma, gamma=G_cal/G_bare,c.          (3)

If the calibration has the same local background, equation (1) or the domain
of (2) gives gamma<=1+q<4/3. The physical-turnaround theorem says

    d_J F_bare > m, m=1,

or m=2 in its last-Einstein-zero case; the later event also has Z>0,d_J<=1.
Hence

    d_J F_cal > 3m/4.                                 (4)

A near-flat radiation-law target d_J<=epsilon<=1, F_cal<=1+delta is
incompatible with this class if epsilon(1+delta)<=3m/4. The inequality
is a consequence of the supplied action and matched local background,
not a universal scalar-tensor or empirical exclusion.

To expose approximation error, a separately supplied bound
G_cal<=(1+eta)G_pr, eta>=0, weakens (4) to

    d_J F_cal > 3m/[4(1+eta)].                         (5)

No numerical eta is derived here. The eta=0 equations are exact for the
leading coefficient and the frozen nonnegative-mass model, not exact for
an actual finite-distance experiment unless its errors have been controlled.

### Different backgrounds: an absolute leading ceiling

Let the calibration background be any finite (u_l,x_l,y_l), even at another
epoch, with the same action constants and physical matter units. Define
chi=s(C_l-1) and B=4k^2(1-3k)/(1+k)^2. Exact action algebra yields

    C_l(1+q_l)/(1+k)=1-B chi^2/(1-3k chi)<=1,           (6)
    -s<chi<1, 1-3k chi>0.

The maximum is attained at u_l=0, regardless of x_l,y_l in this principal
coefficient. Thus G_pr,l<=1/(8 pi Q0); increasing an arbitrary calibration
field cannot make this coefficient unbounded. The local experiment's
admissibility and any environment solution remain open.

If G_cal<=(1+eta)G_pr,l, equations (3) and (6) give

    gamma <= (1+eta)(1+k)/C_c,
    d_J F_cal > m C_c/[(1+eta)(1+k)].                  (7)

A target d_J<=epsilon<=1, F_cal<=1+delta therefore necessarily requires

    C_c < Ccrit=(1+eta)(1+k)epsilon(1+delta)/m.         (8)

This is necessary, not sufficient. It neither constructs an environment nor
establishes a history joining its calibration point to the cosmological
point. When Ccrit>=1 it gives no positive small-C energy floor of the type
below. Radiation at the current epoch is not presumed to dominate expansion.

### Energy cost of the remaining distinct-background route

For 0<C<1, invert the actual supplied coupling, without choosing a selector:

    E=C/(1+s-sC), u=log[C/(1+s-sC)]/(2 sqrt(a)).

At fixed u, x=y=0 minimizes U over x,y. The resulting potential is

    U0(C)=3/2+(3/2)s(1-C)^2
          +nu(1+s-sC)^2 log^2[C/(1+s-sC)]/[8a(1+s)]. (9)

It decreases strictly as C grows from zero to one. To check the total
potential, put t=2sqrt(a)u<0. The sign of U_u is the sign of

    12a(exp(t)-1)+nu t(1-t)+nu t/[s exp(t)],

whose three terms are negative for every t<0. Thus no upper bound on nu
is required on this negative-u branch. The map C(u) is increasing.
Consequently, if 0<Ccrit<1, the target in (8) implies

    U(phi_c)>U0(Ccrit),
    rho_phi,E/(2Q H_v^2)>=U(phi_c)>U0(Ccrit).           (10)

For the campaign energy e=|dphi/d(H_v t_E)|_K^2/2+U-3/2,
e>U0(Ccrit)-3/2. Kinetic and transverse potential energy only increase
this floor. As Ccrit tends to zero with k,nu fixed, the last term diverges
like nu(1+s)log^2(Ccrit)/[8a]. This is a conditional necessary energy cost;
a large early-universe scalar density is not automatically inconsistent.
No observational amplitude or measured dimensional age is inferred.

### What was derived and what survives

The scalar enhancement and the global leading calibration ceiling follow
from the supplied action. Conditional on the previous turning-point theorem,
they turn the unknown environment into a necessary inequality and energy
cost rather than an arbitrarily assigned conversion factor. The action,
k,nu,Q0,H_v, radiation/thermal state, local response applicability, bounded
error eta and an actual environment/history solution remain inputs or gaps.

A speed-up parameter is not a primordial abundance likelihood. An actual
comparison needs temperatures, species thresholds, interaction/entropy
history, nuclear rates, measured abundances and their correlations, and
the relevant cosmological curvature inference. No synthetic target values
here count as independent observations. No charge-production mechanism,
initial-state selector, singularity theorem or completed TOE is claimed.

## Computation, provenance and surviving inputs

The standalone primary runner contains the three direct algebraic control
blocks with isolated namespaces. Exact inequalities and the last-zero/
compactness arguments are the written proofs; finite checks are not substitutes
for those arguments. Kinematic chronology examples are not called full field
solutions. Synthetic calibration targets are not observations or independent
empirical tests. The exact critical-emergent solution is a full origin/radiation
example that fails the target, preserving the need for that premise.

The physical-turnaround producer first returned38/2 because two unexpanded
SymPy positivity queries were undecided; a separate exact expansion check
passed2/0. The canonical block uses those expansions. Calibration first
returned65/1 on an undecided exponential sign query, then66/0 after an exact
calculus certificate. Slow-past first returned49/1 on an undecided sign query,
then52/0 after square-plus-positive-slack certification and a threshold/minimum
identity. Every original run and repair remains recoverable. Four actual
altered calibration implementations and four actual altered slow-past
implementations were rejected. Canonical execution is a disclosed reuse/rerun,
not another independent proof.

The action, scales, k and nu, matter species and state, separate radiation
conservation, local response applicability and positive calibration remain
premises. Finite-body environmental matching, a controlled approximation error,
thermal/entropy history, actual abundance/curvature likelihoods, initial-state
selection, action selection and dimensional hierarchy are not derived here.
The conditional duration bound does not establish curvature divergence or
geodesic incompleteness. No empirical exclusion or completed unification is
claimed, and no formal audit verdict is applied by this milestone.
