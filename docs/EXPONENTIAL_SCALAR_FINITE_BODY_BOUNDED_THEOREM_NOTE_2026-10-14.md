# Deriving finite-body field, force and uniqueness bounds

Status: conditional support; a prescribed static source in a fixed flat metric.
Claim type: bounded_theorem. Scientific author: /root.
Primary runner: `scripts/exponential_scalar_finite_body_check.py`.

Density-dependent homogeneous extrema do not establish a finite body's interior
field or measured force. This block derives compactness bounds, a radial surface
force bracket and a sufficient uniqueness/stability criterion from the elliptic
equation. A thin-shell factor and a chosen interior stationary point are not
inserted. The action, particle-density source, boundary and approximation regime
remain declared premises.

The [supplied action](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md),
[local normalization](EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md),
and [environment definitions](EXPONENTIAL_SCALAR_ENVIRONMENT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-10-14.md)
remain conditional. Here chi is the locally/global-along-this-line canonical
coordinate defined by dchi=sqrt(K_uu)du, not the distinct bounded-coordinate chi
used in the earlier confinement note. The negative-branch restriction is explicit.
No observed likelihood, measured body mass or full relativistic exterior is supplied.

The full hand proofs follow. Their original filenames and version references
identify preserved evidence in the recovery archive rather than new premises.

## Can a weak finite body reach the homogeneous density minimum?

Personally derived by /root, 2026-10-14. This addresses a missing environment
bridge: a stationary homogeneous density minimum need not be attained inside a
finite object. The complete supplied scalar action remains conditional. No new
observational data, material law, ambient state or absolute scale is selected.

### 1. The explicit local model

Restrict the supplied action to its consistent x=y=0 scalar channel. Let
chi(u)=integral_0^u sqrt(K_uu(v)) dv, A(0)=1, Y=H_v^2 U, and
beta=d ln A/d chi>0. The scalar kinetic term is -Q(partial chi)^2.
Consider a prescribed, nonnegative, bounded, compactly supported conserved
Einstein particle mass density rhoStar=m_J n_E. Particle locations/volume are
held by unspecified supports. This is not a freely falling fluid, a derived
constitutive law, or fixed physical rho_J: rho_J=rhoStar/A^3.

In a frozen flat spatial patch, after subtracting the constant vacuum energy,
the static equation and energy are

    Delta chi=Y_chi+rhoStar A_chi/(2Q),                  (1)
    E[chi]=integral [Q|grad chi|^2+2Q(Y-Y(0))+rhoStar A] d^3x.

The boundary is chi tending to0 at spatial infinity in this mathematical
decoupling problem. Positive H_v means the full spacetime is not asymptotically
Minkowski; this boundary is an ideal local matching model, not a global GR
solution. Applying it to a body needs a patch small compared with background
curvature/evolution lengths and controlled metric/support corrections.

First suppose a bounded regular solution is entirely on the negative-u branch,
so chi<=0. For nu>0 the candidate has Y_chi<0 for chi<0, Y_chi(0)=0,
0<A<=1 and q=beta^2<a<1/3. Write w=-chi>=0 and c=rhoStar/(2Q).
Let V>=0 be the Newton potential magnitude solving -Delta V=c with V->0;
V(x)=Gvac integral rhoStar(y)/|x-y| d^3y, Gvac=1/(8pi Q).
Its maximum P=||V||_infinity is a supplied compactness functional of the held
mass distribution, not an independently measured gravitational constant.

Because -Delta w=Y_chi+c A beta<=c sqrt(a), comparison with the decaying
Newton solution gives

    0<=w(x)<=sqrt(a) V(x),
    0<=-ln A(x)<=a V(x).                               (2)

For comparison, use Delta(w-sqrt(a)V)>=0, zero limiting boundary and the
maximum principle. These are exact inequalities for (1), independent of nu,
density amplitude and the local effective mass. They already forbid arbitrary
field movement in a weak object merely because its homogeneous density is high.

### 2. A sharper vacuum-referenced bound

For 0<k<1/3, a=(1-k)(1+3k)/4 and s=(1+k)/[k(1-3k)], the previous exact
negative-branch relation is q=a(1+s-s A^2)/(1+s-3as A^2), with k<=q<a.
Since dA/dchi=A sqrt(q), direct differentiation gives

    -d beta/dchi=(1+k) A^2 (1-3q)^2/(1-3k)^2
                 <=L:=1+k.                            (3)

At chi=0, beta=sqrt(k), and the derivative has magnitude L. Thus
sqrt(k)<=beta(-w)<=sqrt(k)+Lw throughout this branch. Equation(1) implies
-Delta w<=c[sqrt(k)+Lw]. Comparison, followed by a supremum bound for the
positive Newton integral operator, yields

    W:=||w||_infinity <=sqrt(k) P+L P W.

Whenever LP<1, this closes without assuming a constant coupling:

    W<=sqrt(k) P/(1-LP),
    k<=q(x)<=k/(1-LP)^2,
    -ln A(x)<=sqrt(k)W+L W^2/2
              <=k P(1-LP/2)/(1-LP)^2.                 (4)

The global a ceiling can be combined with the q bound. The last expression
bounds an integral of beta; it does not identify the force charge of the body.
For a uniform held sphere with mass MStar and radius R, P=3Gvac MStar/(2R).
The use of Gvac, rhoStar and Einstein radius is explicit. Measured Jordan
compactness requires the previously unresolved calibration/matching bridge.

The interior density minimum can be used as a physical approximation only if
its displacement satisfies these necessary finite-body bounds. Violation is
a failure of that homogeneous-interior approximation under this matching, not
nonexistence of all static solutions or exclusion of the entire theory. A
potential gradient can cancel the volume source and reduce the external
charge. Equations(2)-(4) alone neither prove nor exclude that screening; they
do prove that its ambient/central values cannot be supplied arbitrarily.

### 3. Existence is different from dynamical state selection

For the same prescribed compact source and nu>0, one may minimize E over
nonpositive H^1 fields with the zero boundary at infinity. On this half-line,
U-U(0) is strictly positive away from zero, quadratic with positive coefficient
near zero, and grows quadratically in chi as chi tends to minus infinity.
Continuity therefore gives a positive coercive lower bound proportional to
chi^2 for fixed parameters. The matter contribution is bounded between0 and
integral rhoStar. The direct method uses weak H^1 compactness, local Rellich
convergence on the source support, Fatou for the nonnegative potential, and
dominated convergence for A rhoStar. It gives a minimizing field.

Clipping a positive field to zero lowers its gradient energy, lowers the
candidate potential because U>=U(0), and lowers its matter energy because
A>=1 on the positive branch. A nonpositive minimizer is consequently also
stationary against small admissible variations into the original positive
canonical neighborhood. Clipping sufficiently negative values also lowers
the energy: for bounded rhoStar, Y_chi+c A_chi is negative uniformly at
sufficiently negative chi. The minimizer is bounded. Its elliptic right-hand
side is then uniformly bounded, so translation-uniform local elliptic estimates
give uniform continuity. Uniform continuity together with chi in L^2(R^3)
forces chi to tend uniformly to zero at infinity: otherwise disjoint balls
of a fixed radius and nonzero amplitude would make its L^2 norm infinite.
This establishes the boundary after taking the direct-method limit; H^1 alone
would not do so. Local regularity supports weak comparison across density jumps. This is an existence construction in
the supplied elliptic model. It does not prove uniqueness, dynamical settling,
realization of that minimum, or applicability of the flat/held-source model.

For such a minimizer, E[chi]<=E[0]=MStar. Its scalar energy obeys

    integral [Q|grad chi|^2+2Q(Y-Y(0))]
       <=integral rhoStar(1-A)
       <=MStar ||-ln A||_infinity.                     (5)

Independently, multiplication of (1) by chi and integration gives
integral |grad chi|^2<=integral c beta w, since chi Y_chi>=0.
These are useful self-consistency bounds; they do not supply a complete metric
error estimate or eliminate material supporting stresses.

### 4. Frozen implementation plan and limits

Verify the canonical derivative identity directly in original E=e^(2sqrt(a)u)
coordinates, its positive/negative domains, the maximum-principle sign, the
bootstrap coefficient, the uniform sphere Newton normalization, and the
potential sign/coercive limits. Deliberately reverse the comparison sign,
replace the kinetic normalization by a half-normalization, and remove the
bootstrap denominator; actual damaged programs must fail independent witnesses.

For numerical illustrations use only synthetic held spheres and expose all
calibrations. Compare a direct nonlinear radial boundary-value solution with
an independent integral/flux residual, mesh/domain refinements, and a massless
or linear massive analytic control. Retain full radial profiles and truncation
errors. No real object or observational exclusion is to be inferred from these
examples. The final model-to-data bridge still needs the ambient state, matter
support, measured compactness/range and a controlled curved-spacetime solution.

## From field excursion to a conditional surface-force bracket

Personally derived by /root after the finite-body excursion calculation. Reuse
all hypotheses and the corrected existence/boundary argument in DERIVATION_v2.md.
This extension concerns a radial negative-branch solution for a spherical, uniform held rhoStar of radius R. It is an
exact bound within the flat static model, not an imported thin-shell factor.
No new calibration, observed body or likelihood is supplied.

Put P=3Gvac MStar/(2R), L=1+k, Wb=sqrt(k)P/(1-LP),
B=kP(1-LP/2)/(1-LP)^2, betaMax=sqrt(k)/(1-LP), with LP<1.
The previous comparison also gives the stronger pointwise bound w<=betaMax V.
The surface scalar attraction relative to the chosen Newton reference is

    eta_s=beta(chi(R)) R^2 chi'(R)/(Gvac MStar).          (1)

This normalization uses held Einstein particle mass. It is not the measured
Jordan gravitational mass including scalar energy, pressure and metric corrections.

### 1. A potential slope envelope derived from the supplied action

Let K0=K_uu(0), Umax=Wb/sqrt(K0), Emin=exp(-2sqrt(a)Umax), Fmin=1+s Emin.
Because dK/dE=-s[(1+3a)+(1-3a)sE]/(1+sE)^3<0,
K(u)>=K0 for u<=0. Therefore w<=Wb implies -Umax<=u<=0.

On this interval, writing alpha=sqrt(a), a conservative explicit envelope is

    Mbar^2 = H_v^2/K0 {
       12 a s(1+s)^2/Fmin^4
       +nu(1+s)[1/Fmin^2+8alpha s Umax/Fmin^3
                             +12a s^2 Umax^2/Fmin^4] }. (2)

To prove it, the base-potential second u derivative is

    12a s(1+s) E[2E-1+sE(2-E)]/(1+sE)^4.

Use E<=1, 2E-1<=1 and E(2-E)<=1. The regulator second derivative is

    nu(1+s)[1/F^2-8alpha s E u/F^3
                   -4a s E u^2/F^3+12a s^2 E^2 u^2/F^4].

Drop the negative term and bound the positive terms by Umax,Fmin. Since
K_u<0 and U_u<0, the canonical Hessian

    Y_chichi=H_v^2[U_uu/K-K_u U_u/(2K^2)]

is no larger than the positive envelope(2). Integration from chi=0 gives

    0<=-Y_chi(-w)<=Mbar^2 w, 0<=w<=Wb.                 (3)

This does not assume a positive Hessian everywhere. Mbar is an explicit
consequence of the action and prior excursion bound, not an assigned effective
mass. At P->0 with fixed parameters it approaches the exact vacuum mass,

    Mvac^2/H_v^2=4(3+3k+nu)/(1-3k).

The approach is not asserted uniform at singular parameter boundaries.

### 2. Integrate the actual radial source

Exterior to the body, (r^2 chi')'=r^2 Y_chi<=0. A nonpositive solution tending
to zero cannot have r^2 chi'<0 at an exterior point: monotone decrease of that
flux would prevent its approach to zero from below. Thus exterior scalar
attraction is nonnegative, including at R.

Integrating the exact equation through the body and using A>=exp(-B),
beta>=sqrt(k), and(3) gives

    R^2 chi'(R) >=sqrt(k) exp(-B)c R^3/3
                         -Mbar^2 integral_0^R r^2 w dr,

where c=rhoStar/(2Q). The uniform sphere has V=c(3R^2-r^2)/6 inside and

    integral_0^R r^2 V dr=2c R^5/15,
    Gvac MStar=c R^3/3.

Use w<=betaMax V and multiply by beta(R)>=sqrt(k) only when the lower flux
bound is nonnegative. The resulting unconditional bracket within this model is

    max[0, k exp(-B)-(2/5)k Mbar^2 R^2/(1-LP)]
        <= eta_s <= k/(1-LP)^2.                        (4)

The upper bound follows separately from Y_chi<=0 and A beta<=betaMax in the
volume source. Outside the body, the scalar/Newton-reference ratio is
nonincreasing: differentiate beta r^2 chi', use beta_chi<=0, chi'>=0 and
Y_chi<=0. This monotonicity is a range/property statement, not a positive
lower force bound at an arbitrary distant apparatus.

For small compactness and Mbar R<<1, the lower bound is close to k. Hence a
weak body in this particular vacuum-matched long-range class cannot be assigned
an arbitrarily suppressed scalar charge. If the bracket is zero it says
nothing about the amount of screening. Large range corrections, different
ambient matching, real density/support profiles and full spacetime remain to
be derived. The field excursion theorem alone did not give this lower bound;
the supplied potential envelope and uniform-sphere source integration are new
essential steps.

### 3. Prospective checks on existing synthetic profiles

Before extracting their surface forces, freeze: verify the exact Hessian and
sphere coefficients; challenge the comparison and force directions; compute
the explicit envelope from each previously frozen case; check every recorded
surface flux against(4) with the existing2e-8 absolute numerical slack; and
record cases where the lower bracket is uninformative. Independently sample
the exact Hessian across the whole analytically bounded u interval as a
numerical control, not as the proof of its supremum. Existing profiles are now
exposed development data; this reuse is not a reserved validation sample.
Actual changed envelope/flux-normalization programs must fail exact witnesses.

## A compactness criterion for a unique negative-branch held-body solution

Personally derived by /root. Conditional support inside the same supplied action,
flat elliptic equation, bounded compact nonnegative held particle density, nu>0,
and vacuum boundary as DERIVATION_v2.md. No dynamical state selection or full
metric/matter solution is claimed. This adds a sufficient small-body criterion;
failure of the criterion is not evidence for multiplicity.

Use P=||V||infinity, L=1+k, LP<1, Wb=sqrt(k)P/(1-LP),
K0=K_uu(0), Umax=Wb/sqrt(K0), and alpha=sqrt(a). Suppose

    2 alpha Umax <= ln 2.                              (1)

This is a computable condition on the held-source compactness and the already
supplied parameter k. It is not an additional potential or mass selector. All
bounded decaying negative-branch solutions obey -Umax<=u<=0 from the previous
comparison, hence E=exp(2 alpha u)>=1/2 and F>=1, J>0.

### 1. Derive convexity on the whole reachable interval

Let b=1-3a>0, F=1+sE, J=1+b sE. Direct canonical differentiation of the base
potential gives

 Ubase_chichi = 6 a s(1+s) E / (F^2 J^2)
     * {2J[(2E-1)+sE] - b s E(E-1)F}.                 (2)

For 1/2<=E<=1 every displayed term in braces is nonnegative and sE>0, so this
is strictly positive. Write the regulator as nu(1+s)g^2/2 with g=u/F. Then

 g_chi = [1-2 alpha s E u/F]/sqrt(J),
 g_chichi = -2 alpha s E/J [1+2 alpha u/F]
            -alpha b s E F/J^2 [1-2 alpha s E u/F].    (3)

Because 2 alpha |u|<=ln2<1 and F>=1, (3) is negative, while g<=0. Thus

 Ureg_chichi = nu(1+s)[g_chi^2+g g_chichi] >0.

The total Y=Hv^2 U has Y_chichi>0 throughout the allowed interval (Hv>0).
This is a derived local convexity domain; no global convexity premise is used.

Also A_chichi=A(beta^2+beta_chi)>=-L, since 0<A<=1, beta^2>=0 and
beta_chi>=-L on the negative branch. This one-sided bound is sufficient; no
absolute upper bound on A_chichi is required.

### 2. Uniqueness from the positive Newton operator

Let chi1,chi2 be two bounded decaying negative-branch solutions for the same
held source and parameters. Let d=chi1-chi2. Their segment stays in the above
convex interval. By the mean-value identities, Y_chi(chi1)-Y_chi(chi2) has the
sign of d, and [A_chi(chi1)-A_chi(chi2)]d>=-L d^2.
The distributional Kato inequality therefore implies

    -Delta |d| <= L c |d|,   c=rhoStar/(2Q)>=0.       (4)

The right side has compact support. Both |d| and the Newton potential of
L c |d| decay to zero. The maximum principle applied to their difference gives

    |d(x)| <= L N[c |d|](x)
             <= L ||d||infinity V(x).

Taking suprema yields ||d||infinity<=LP ||d||infinity. LP<1 forces d=0.
The existence proof in DERIVATION_v2 supplies at least one such negative-branch
solution, so it is unique in this explicitly stated class.

For a rotationally symmetric held density, every spatial rotation of that
solution solves the same problem. Uniqueness therefore derives radial symmetry,
without assuming that spherical density by itself guarantees it. For a uniform
sphere satisfying (1), the surface-force bracket applies to this unique static
negative-branch solution. The elliptic solution is still not a proven realized
state of a freely moving body or cosmological environment.

The same Kato proof also gives a stability estimate for changing the held source,
provided both sources satisfy a common reachable convexity interval: with
Vdiff=N[|c1-c2|] and betaMax a common upper bound on A_chi, the difference obeys
||d||infinity <= betaMax ||Vdiff||infinity/(1-L P1).
This last inequality is conditional on those common bounds; it does not derive
source masses, support stresses or a dynamical settling rate.

### 3. Prospective checks

Verify (2),(3) directly from the original action and canonical Jacobian, the
one-sided A_chichi bound and the contraction sign. Check the exact criterion on
the already exposed 18 synthetic body cases; sample Hessians only as numerical
controls in addition to the analytic proof. Deliberately reverse the Kato sign,
connection term or denominator and preserve the failed mathematical witnesses.
No new observation, fit or independent empirical test is implied.

### 4. Stability for the scalar with the source held fixed

The preceding static uniqueness does not itself establish dynamical relaxation.
A separate quadratic-form argument does rule out growing scalar normal modes
while the same particle density and flat metric are held fixed. For nonzero
source let V=N[c]>0. For compactly supported smooth f, ground-state integration
by parts gives the exact identity

 integral |grad f - f grad ln V|^2
   = integral |grad f|^2 - integral (c/V) f^2.

Since V<=P, it follows that integral c f^2<=P integral |grad f|^2.
The identity extends by approximation to the relevant finite-energy form domain;
zero source is the separate trivial vacuum case. On the compact reachable field
interval, continuity and the strict proof in section1 give a positive minimum
mMin^2=min Y_chichi>0 at fixed interior parameters. This minimum is defined by
the supplied action and interval, not a chosen positive mass. Therefore the
linearized held-source operator H=-Delta+Y_chichi+c A_chichi obeys

 <f,Hf> >= (1-LP) integral |grad f|^2 + mMin^2 integral f^2.

The quadratic canonical scalar has equation f_tt+Hf=0, so no negative spectrum
or exponentially growing finite-energy scalar normal mode exists in this held
source, fixed flat metric model. This does not establish damping, attraction to
the stationary solution, stability against moving matter/metric perturbations,
or a realized environment. Freely moving matter has the separate coupled modes
already derived in the dynamical-density block. No uniform gap is claimed as
Hv or nu or parameter-domain distances vanish.

## Numerical and empirical status

The frozen grid has18 synthetic uniform held spheres: k=0.01,0.1,0.3;
nu=0.0001; surface compactness0.0001,0.01; vacuum mass times radius0.1,1,10.
The radius is the numerical length unit. Every field, derivative, conformal
factor, coupling, integrated source flux and enlarged-domain comparison is kept.
The finite-domain Dirichlet solve approximates the stated infinity boundary;
grid checks are not an analytic discretization certificate or a full GR solve.
No state is selected by the sign-bracket search for homogeneous extrema.

Original excursion220/0, surface172/0 and uniqueness98/0 give490 canonical
controls. Surface/uniqueness reuse the already exposed profiles; they are not
independent observational validation. Eleven surface lower brackets are nonzero.
All18 cases meet the sufficient uniqueness criterion. Samples supplement the
analytic Hessian inequalities; a sampled minimum is not a certified eigenvalue.

The original excursion implementation failed while serializing a NumPy boolean;
its18 profiles remain. The serialization repair gave216/4, exposing integral-flux
resolution. A tighter solver attempt gave219/1 because its mesh limit was reached.
Rescaling the unknown by the analytic linear field gave220/0 with the same
physical equations, original solver tolerance and unchanged acceptance tests.
The surface implementation also needed an explicit boolean serialization repair.
All source versions, streams, failures, profiles and exact diffs remain recoverable.

The independent excursion proof check supplies598/0 and22 affected proof controls;
the surface proof check supplies1735/0 and seven actual altered programs. The
uniqueness proof receives a separately sealed focused check. These are mathematical
and numerical controls, not experiments or formal audit grades. Its access record
must disclose that aggregate producer metadata was exposed before independent
algebra; this does not turn the producer count into independent evidence.

The first existence outline lacked a proof of decay after the variational limit.
The corrected proof derives uniform continuity from bounded elliptic forcing and
uses L2 integrability to obtain decay. The surface opening now states radial
solution explicitly. A separate small-compactness theorem derives radial symmetry
from uniqueness; it does not infer symmetry solely from spherical density.

The [recovery archive](work_history/physics/revised-scalar-finite-body-20261014/README.txt)
contains all original proofs, numerical histories, figures, source comparison,
independent reports, source bindings and actual changed-program controls.
The command-line option `--profiles` preserves the complete fresh pipeline. Its
surface/uniqueness source bindings refer to the newly generated excursion output;
different output directories are provenance differences, not changed science.

The primary literature comparison is Khoury and Weltman,
[astro-ph/0309300v3](https://arxiv.org/pdf/astro-ph/0309300), inspected at its static
equation and compact-body discussion. Its established mechanism motivates the
finite-size question. Its runaway potential, constant coupling, ambient minimum
and approximate shell factor are not inserted into this candidate's proofs.

For a weak sufficiently long-range body in the declared class, the source charge
cannot be assigned arbitrary suppression. For a heavier range correction the
zero lower bound is uninformative. Other ambient states, physical density/support
profiles, metric backreaction, moving-matter stability, dynamical relaxation and
conversion to a measured gravitational mass remain open. This is no general
Solar-System exclusion, no complete environmental reconstruction and no TOE.
