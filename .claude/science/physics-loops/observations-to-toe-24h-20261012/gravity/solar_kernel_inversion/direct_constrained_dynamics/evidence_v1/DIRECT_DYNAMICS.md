# Preferred-time attempt preserving the fitted static equations

Direct parent derivation, 2026-10-12. Status:
partial-attempt-with-named-untested-routes. The field-only energy of the
specified constrained model is positive. Its homogeneous anisotropic
linearization fails a finite-support propagation requirement for its physical
scalar. This is a local mathematical diagnosis, not an observational
exclusion, a relativistic causality theorem or a formal audit result.
The assumptions and calculation sequence are in PROTOCOL.md.

## 1. New candidate and its exact static limit

Write psi=Phi_N, phi=Phi, A=|grad psi|, C=1/(8 pi G), and
F(s)=integral_0^s N(sqrt(u))du. Keep the two frozen log-ramp responses from
../DIRECT_STATIC_ACTION.md without altering any weight. Introduce:

    L = C[c_s^(-2) phi_t^2 - 2 grad phi . grad psi + F(|grad psi|^2)]
        - rho phi,                     c_s > 0.                 (1)

Absolute time, a Euclidean space metric, this kinetic term, direct density
coupling, and the identification of -grad phi as the scalar force are supplied
premises. No psi time derivative, gauge symmetry, metric/light sector or
observable cancellation is supplied. These are not inferred from a static fit.

Variation, integrating by parts with fixed boundary data, gives

    Delta psi - c_s^(-2) phi_tt = 4 pi G rho,
    Delta phi = div[N(A) grad psi].                             (2)

The time-independent equations are exactly the previous fitted operator.
This preserves the equations only. Carrying a static fit into a moving
source or finite-time observation also needs a justified quasistatic limit.

For U=grad psi away from a response knot, define

    M = N I + (N'(A)/A) U U^T,
    D = N + A N'.

M has eigenvalues N,N,D. The primary canonical constraint is pi_psi=0;
pi_phi=phi_t/(4 pi G c_s^2). Preserving pi_psi imposes the second equation
of (2). Its psi derivative is -div(M grad). When M is uniformly positive
and the zero-boundary elliptic problem is invertible, this and pi_psi form
a second-class pair. There is one configuration degree of freedom. The
constant spatial zero mode is fixed by boundary data, not counted as a
separate propagating oscillator.

## 2. Nonlinear field-only energy on a zero-boundary domain

Let Omega be a bounded Lipschitz domain, phi,psi in H_0^1(Omega).
Assume 1<=N<=N_max and a uniform positive lower bound on D on every smooth
piece; the response is continuous at its finitely many knots. These
conditions hold for the frozen finite vectors, with the arithmetic check
below. The Hessian of F(|U|^2) is 2M almost everywhere. Its bounded,
uniformly positive pieces and continuity of its gradient make the function
strongly convex on all U, including across the knots.

For fixed phi the constraint uniquely minimizes

    I_phi(psi) = integral [F(|grad psi|^2)
                          -2 grad phi . grad psi] dx.

Existence follows from coercivity on H_0^1, weak lower semicontinuity of the
convex integral and the direct method; strict convexity gives uniqueness.
Equivalently define the spatial dual functional

    J(phi) = sup_psi {2 integral grad phi . grad psi
                      - integral F(|grad psi|^2)}.

The actual stationary elimination is this supremum. Completing the square,
using F(s)>=s, gives J<=integral|grad phi|^2. Taking psi=phi/N_max and using
F(s)<=N_max s gives the matching lower bound

    (1/N_max) integral |grad phi|^2 <= J(phi)
                                      <= integral |grad phi|^2. (3)

The constrained field energy is

    E_field = integral 2 pi G c_s^2 pi_phi^2 + C J(phi) >= 0.    (4)

For rho=0 it is conserved for sufficiently regular solutions for which
the integrations by parts are valid. No nonlinear existence theorem for
that time evolution is proved here. With matter, the interaction integral
rho phi and the matter action must also be considered: (4) is not a lower
bound on the total interacting Hamiltonian. Zero-boundary nonlinear energy
and the uniform-background calculation next are separate statements.

## 3. Homogeneous linear modes and group velocities

On R^3 take a constant nonzero auxiliary gradient U_0=A_0 e_z, away from
knots. Its field energy over all space is not finite. We examine local
linear perturbations u=delta phi,v=delta psi; the constant background
solves the vacuum static equations. Set M=diag(N,N,D)>0. Then

    c_s^(-2) u_tt = Delta v - 4 pi G delta rho,
    Delta u = L_M v,             L_M=div(M grad).                (5)

For a nonzero wave vector k, set q=k^T M k and n=k/|k|. In vacuum,

    v_hat = |k|^2/q u_hat,
    omega^2 = c_s^2 |k|^4/q
            = c_s^2 |k|^2/[N sin^2(theta)+D cos^2(theta)].       (6)

After eliminating v the quadratic mode action is C times
c_s^(-2)|u_t|^2 - (|k|^4/q)|u|^2. It has a positive kinetic term and a
positive restoring energy for each nonzero k. The transverse and longitudinal
phase speeds are c_s/sqrt(N) and c_s/sqrt(D).

The group velocity, differentiating positive omega, is

    v_g/c_s = 2k/sqrt(q) - |k|^2 M k/q^(3/2),
    |v_g|^2/c_s^2 = (n^T M^2 n)/(n^T M n)^3.                  (7)

For N>=D>0, put m=n^T M n in [D,N]. The numerator is
(N+D)m-ND. Maximizing its ratio to m^3 gives

    vmax/c_s = 1/sqrt(D),                            N<=2D;
    vmax/c_s = 2(N+D)^(3/2)/(3 sqrt(3) N D),          N>2D.       (8)

In the second case the maximizing m=3ND/[2(N+D)] lies inside [D,N].
These are finite mode velocities. They are not a wavefront-support result.

For a nonzero log ramp j, N decreases with A and D=N-c where
c=w_j/d and d=ln(10)/4. In the N>2D regime,

    d/dN log(vmax^2)
      = -2(N^2-Nc+c^2)/[N(N-c)(2N-c)] < 0.

The N<=2D expression also increases as N decreases. Thus the supremum over
a ramp occurs at its upper one-sided endpoint. Constant intervals have
N=D and speed c_s/sqrt(N). Checking the twenty upper one-sided limits and
the outer plateaus covers this frozen finite response's local mode suprema.
At a knot no single classical Hessian is assigned; the stated suprema use
limits. No assertion is made about nonlinear interface characteristics.

## 4. Why bounded mode speeds fail to imply finite propagation here

The reduced source-free equation on R^3 is

    u_tt = c_s^2 Delta L_M^(-1) Delta u.                         (9)

The inverse in (9) is the decaying constant-coefficient elliptic Green
inverse. The acceleration multiplier is -c_s^2 |k|^4/(k^T M k).
For anisotropic M it is not a polynomial. If every compact smooth pair
u(0),u_t(0) propagated with finite support speed, then at any point separated
from its initial support u_tt(0) would vanish. Consequently the convolution
kernel of the acceleration operator would be supported only at the origin.
A distribution supported at a point is a finite sum of derivatives of a
delta distribution, so its Fourier transform must be polynomial. A positive
quadratic form q is irreducible over R in three variables; it divides
(|k|^2)^2 only when proportional to |k|^2. Therefore finite support propagation
for all such data is possible in this class only when M is isotropic.

There is an explicit off-source witness. With r_M^2=x^T M^(-1)x,

    G_M(x) = -[4 pi sqrt(det M)]^(-1) (r_M^2)^(-1/2),
    L_M G_M = delta,
    K_acc(x) = c_s^2 Delta^2 G_M(x).

For M=diag(N,N,D) and z!=0,

    K_acc(0,0,z) =
       -6 c_s^2 (N-D)^2 / [pi N^3 |z|^5].                     (10)

The runner differentiates the Green kernel independently with SymPy.
For example, choose a nonnegative smooth bump approaching unit mass at
the origin. At a sufficiently separated point on the z axis, its
convolution with K_acc has the same nonzero sign. Its initial physical
u,u_t=0 are compact, but its initial acceleration is nonzero there. Fourier
solutions are twice differentiable in time for this smooth data, so this
contradicts finite-support propagation at arbitrarily small positive times.

The consistent auxiliary v is already spatially nonlocal. Compact physical
data here means u and u_t, not simultaneous compactness of every constrained
field. No gauge-invariant observable cancellation has been supplied. A gauge
or metric theory could alter that physical identification; this proof says
nothing about its observables. Nor is an observational signaling protocol,
a bound on a tail's detectability, or a relativistic causal paradox proved.

The isotropic exception is exact: N=D gives v=u/N and the ordinary wave
equation u_tt=(c_s^2/N) Delta u. Both frozen candidates are on an isotropic
plateau at the fitted external E. Their active ramps admit other homogeneous
anisotropic backgrounds. Do not claim a tail has been measured at that E.

## 5. Optional algebraic extension: constant two-field time Hessians

This extension was derived after the protocol was written. It is one
extension of the same kinetic-matrix family, not a second independent
attack family. Keep exactly the same spatial quadratic form and replace
the time term by dot X^T K dot X, with X=(u,v), constant symmetric real K.
No mixed time-space terms, extra fields or constraints are added.

For one k!=0 the spatial matrix is

    S(k) = [[0,-|k|^2],[-|k|^2,q]],       det S=-|k|^4.          (11)

If K is positive definite, both fields propagate and -S has one negative
direction. The generalized omega^2 problem has one negative eigenvalue:
there is a high-frequency gradient instability and field energy is not
bounded below. If K is nonsingular and not positive definite, its canonical
kinetic energy already has a negative direction.

For the positive rank-one case K=lambda a a^T, lambda>0,
a=(a_phi,a_psi), direct determinant expansion gives

    det(S+omega^2 K)
      = -|k|^4
        +lambda omega^2[a_phi^2 q+2 a_phi a_psi |k|^2].          (12)

If a_phi=0 there is no nonzero source-free propagating Fourier mode; the
phi equation constrains v=0. Otherwise set r=a_psi/a_phi. A stable nonzero
mode in every direction requires m(n)+2r>0 and then

    omega^2 = |k|^4 /
       [lambda a_phi^2 (k^T[M+2r I]k)].                        (13)

It retains the same anisotropy N-D. The null-kinetic constraint gives
v_hat=|k|^2/(q+r|k|^2) u_hat. Its denominator is positive under the preceding
stable-mode condition, because m+r>m/2>0. Thus arbitrary physical u data
parametrize this surviving mode, and the nonpolynomial support obstruction
applies again with M+2r I. A negative rank-one kinetic eigenvalue instead
gives negative reduced kinetic energy whenever a mode survives; rank zero
has no time evolution. Singular directions where m+2r=0 are excluded from
a stable, regular evolution, not claimed to repair it.

This classifies the stated constant homogeneous two-scalar time-quadratic
ansatz. It does not classify field-dependent nonlinear constraints, derivative
kinetic operators, first-order/time-space couplings, gauge fields or metric
gravity. It is useful for choosing the next attempt, not a universal no-go.

## 6. Evidence, observations and route status

The runner reads only FROZEN_TRANSFER_INPUT.json. It verifies a rational
ln(10)/4 enclosure, strict one-sided D bounds, Green and determinant
identities, mode maxima, the isotropic exception and a finite nonlinear
Dirichlet optimization. These supplement the proofs above; a finite grid
does not prove the continuum theorem. Candidate speed ratios in RESULTS.json
use the free c_s normalization and are not empirical predictions in light
units. No response is retuned and no extra observational success is claimed.

An action with the same static equations and positive field energy is a
concrete gain over the prior two-independent-Lorentz-scalar attempt. Equations
(9)-(10) identify why this new premise fails the selected finite-propagation
target on anisotropic backgrounds. The next live mechanisms are extra
metric/vector constraints and physical observable cancellation; altered
spatial dynamics must earn any fits anew; a nonrelativistic effective model
may keep (1) while explicitly relinquishing fundamental finite propagation.
None is asserted to work. Missing matter, lensing, tensor radiation and
cosmological bridges remain open, without an invented count of independent
obstructions.

## No-Go Discipline Gate

N1 — FAIL as a broad no-go packet: one actually attempted kinetic-matrix
family, including its rank cases, is recorded. It is not five distinct
families. The nonlinear convex-dual and Fourier support arguments are two
checks of this same family, not extra routes. Metric/gauge completion,
additional vector constraints, mixed derivative kinetic terms, modified
static operators and nonrelativistic effective scope are UNTESTED escapes,
not prior-refuted families. The packet count does not refute (3), (10)
or (12). Classification remains partial-attempt-with-named-untested-routes.

N2 — No claim of multiple independent walls. Selected premises (1), fixed
physical u, elliptic elimination and anisotropy jointly imply the single
support failure (10). Removing it does not establish the omitted empirical
and unification bridges; implications among those broader obligations are
unresolved and no independent-wall count is given.

N3 — Load-bearing hypotheses are all in sections 1-5 and PROTOCOL.md:
G,c_s>0; exact frozen N; positive D; boundary/domain distinction; source-free
homogeneous linearization; nonzero k; absolute time; the physical scalar
identification; absence of supplied gauge cancellation. The energy claim
covers fields alone. Neither observational fit nor a framework primitive is
used to supply these added assumptions.

N4 — Residual match: DIRECT_COVARIANT_PROMOTION_FAILURE.md concerns an
invertible Lorentz-scalar time Hessian with determinant -1; today's
constraint/support residual differs. RETARDED_FIELD_CAUSALITY_PROBE_NOTE.md,
CAUSAL_ESCAPE_WINDOW_NOTE.md and GRAVITATIONAL_WAVE_PROBE_NOTE.md concern
finite imposed scheduling/sensitivity maps, not this action's inverse.
All are context-only and none is a witness proving today's conclusion.
The current calculation stands on its explicit derivations.

N5 — Resolution scope: pointwise kernel away from its source, each nonzero
homogeneous Fourier mode, and a continuum compact-data support statement
are resolved under their domains. No discrete-site/lattice-wide physical
claim, arbitrary inhomogeneous evolution or observational exclusion is made.
The runner emits the five requested resolution lines with these limits.

N6 — No claim that a new axiom is necessary or that the existing framework
lacks a primitive. The user explicitly permitted exploratory assumptions.
An effective-theory reframe can keep the positive-energy model without
claiming fundamental support causality. A gauge/observable reframe would
need actual equations and cancellation, not a label or governance change.
No registry claim is made, so a primitive-registry absence proof is not used.

N7 — Steelman: the elliptic potential of a constrained theory can be
nonlocal without observable acausality. You have stipulated phi is the
entire force carrier and omitted the metric/vector constraints that might
cancel its tail. Derive that larger action and its measurable response
before rejecting a dynamical gravity program. The strongest source support
used here is the limited scope of Milgrom's static QUMOND action
(https://arxiv.org/abs/0911.5464v2), which supplies no such dynamical
identification. This is an actionable out-of-domain escape, not a
counterexample to (10) under the stated physical-data convention.

N8 — Cross-cycle comparison: the three read finite-DAG/lattice notes above
show imposed retardation and exposure sensitivity but explicitly leave
dynamical/readout bridges open. They supply no mechanism cancelling the
present kernel. The prior campaign's Lorentz-sign failure names changed
constraints as an escape; this block implements that escape and obtains
positive energy, then finds a distinct remaining support issue. The broad
main search failed (137); the narrowed source search completed. Scope of
the read comparison, rather than unexamined title matches, is reported.

Gate outcome: FAIL for broad five-family closure; narrow partial attempt
preserved. No formal audit status, universal gravity rejection, novelty
priority or completed TOE is asserted.

