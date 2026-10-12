# Local vector realization of a homogeneous static response

Date: 2026-10-12.
Claim type: bounded_theorem
Status: conditional-support
Audit authority remains the independent audit lane.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: user_goal
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: construct and test a nonlinear source, background and matter coupling
conditional_surface_status: three real fields with supplied positive constants and a constant unit direction
hypothetical_axiom_status: candidate action explored without adopting a framework premise
admitted_observation_status: no measured data or response coefficients fitted by this theorem
claim_type_reason: explicit local positive-energy realization of a specified linear static susceptibility
proposal_allowed: false
proposal_allowed_reason: physical action and observation identifications remain supplied
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

Primary runner: [local_vector_homogeneous_response_2026_10_12.py](../scripts/local_vector_homogeneous_response_2026_10_12.py).
Its [canonical cache](../logs/runner-cache/local_vector_homogeneous_response_2026_10_12.txt)
records execution and source identities. All proof steps and assumptions needed
by the runner are stated here. No repository theorem, registered framework
primitive, measured target value or hidden fitted selector is a premise.

## Target and observation-first role

A static gravitational response inferred under a source/readout model does not
uniquely determine its dynamics. For arbitrary constants 0<D<=N, alpha>0 and G>0,
this theorem constructs a local vector action with positive field energy,
finite retarded propagation and static scalar susceptibility
(N k_perp²+D k_parallel²)/k^4. The complete proof is below.

The vector-elasticity operator is a mathematical construction, with no novelty
priority asserted. The hypothesis ledger is: three real field components,
a constant unit direction e, positive supplied constants, the stated quadratic
action, and the physical readout phi=e.u. Smooth decaying data define the
classical proof; finite-energy limits preserve its domain of dependence.
These hypotheses are distinct from a demonstrated physical gravitational law.

The construction addresses a homogeneous linear response, not a nonlinear
source-dependent galaxy calculation. The previously attempted two-potential
model below supplies motivating equations, which are derived here as needed;
its fits and its dynamical obstruction are not premises of this positive
construction. Its alternative kinetic architecture is outside this theorem.
The downstream gap is a nonlinear source/background and matter/metric model,
not an unproved lemma inside the displayed linear theorem.

## Action, energy and propagation

Let e be a constant unit vector, 0<D<=N, alpha>0 and G>0. Set mu=1/N and
beta=1/D-1/N>=0, and take three real fields u_i with Lagrangian density

    L = [alpha |u_t|² - mu sum_ij (partial_i u_j)²
         - beta (div u)²]/(8 pi G) - rho phi,
    phi=e.u,       physical scalar force=-grad phi.

This is the ordinary constant-coefficient vector-elasticity operator used
as an explicit mathematical realization. It does not identify space or
matter with a physical elastic substance. alpha, e, N and D are supplied;
there is no rotationally invariant dynamical equation for e in this packet.
The field has three canonical momenta and no auxiliary constraint:
pi_i=alpha u_t,i/(4 pi G). Variation gives

    alpha u_tt - mu Delta u - beta grad(div u) = -4 pi G rho e.

The source sign gives an attractive scalar potential in the isotropic static
limit. The positive field energy is

    E_field = (8 pi G)^-1 integral [alpha |u_t|²
                    + mu |grad u|² + beta (div u)²] dx.

It is conserved for source-free decaying data. With a supplied rho,
the local work term is -rho phi_t. Positivity of this field part does not
bound total matter-plus-interaction energy or supply a matter model.

The Fourier stiffness is B(k)=mu k² I+beta k k^T. Its two transverse
eigenvalues are mu k² and its longitudinal eigenvalue is (mu+beta)k².
There are three stable configuration modes, with positive kinetic energy:

    c_T²=mu/alpha=1/(alpha N),
    c_L²=(mu+beta)/alpha=1/(alpha D),       c_L>=c_T>0.

The local energy proves a domain of dependence with outer speed c_L. To see
the required flux estimate directly, put Q=mu|grad u|²+beta(div u)² and
T_n=mu partial_n u+beta n div u. For any test vector v, Cauchy-Schwarz in
the positive quadratic form gives

    |v.T_n|² <= [mu |v|²+beta(v.n)²] Q <= (mu+beta)|v|² Q.

The energy flux magnitude normal to n is |u_t.T_n|/(4 pi G), bounded by
c_L[alpha|u_t|²+Q]/(8 pi G). Integrating over a shrinking cone gives zero
energy outside the c_L domain of compact full-field data and compact sources.
Smooth compact data suffice; finite-energy weak limits retain the support
statement. A derivative of the local observable phi=e.u also remains local,
so its physical force has no instantaneous off-cone tail in this construction.
No assertion about compact phi alone with unspecified other initial fields
is needed. This distinction matters to comparison with the old constraint.

## Exact static linear response

For k!=0, let P_L=k k^T/k² and P_T=I-P_L. Then

    B^-1 = N P_T/k² + D P_L/k²,
    e.B^-1.e = [N k_perp² + D k_parallel²]/k^4.

Thus a static density has

    phi_hat = -4 pi G rho_hat [N k_perp²+D k_parallel²]/k^4.

This equals the homogeneous linear response of the earlier two-potential
static equations: Delta psi=4 pi G rho and Delta phi=div(M grad psi),
where M=N I+(D-N)e e^T. It includes the same anisotropy at every nonzero k,
not just along the distinguished axes.

The real-space scalar Green function is

    e.B^-1(x).e = [N+D+(N-D)(e.xhat)²]/(8 pi r),
    phi_point(x) = -G m [N+D+(N-D)(e.xhat)²]/(2r).

The Fourier identity follows also from F^-1(1/k²)=1/(4 pi r) and
F^-1(1/k^4)=-r/(8 pi), with the decaying anisotropic inverse specified.
It is a fundamental-solution statement; distributions at the origin are
handled by the Fourier definition. In the isotropic case D=N it reduces to
phi=-Gm N/r as required.

## Retarded response and the cancellation outside the wavefront

For a unit vector force source in the equation alpha u_tt+B u=f, the
retarded tensor in Fourier space is

    G_hat(k,t)=H(t)/alpha [P_T sin(c_T k t)/(c_T k)
                         +P_L sin(c_L k t)/(c_L k)].

Consequently the observable driven along e has two nonnegative spectral
weights, sin²(theta) and cos²(theta), where theta is the angle between e and
k. Equivalently its frequency response has denominators
mu k²-alpha(omega+i0)² and (mu+beta)k²-alpha(omega+i0)². At zero frequency
their sum is exactly the previous static susceptibility. At finite frequency
it is generally different from the old constrained scalar's single branch
omega²=k^4/(alpha [N k_perp²+D k_parallel²]). Both branches share the old
axis speeds, but not its intermediate-angle dispersion.

For r>0, n=x/r, the full retarded tensor is

    G_ij(x,t) = 1/(4 pi alpha) {
        (delta_ij-n_i n_j) delta(t-r/c_T)/(c_T² r)
        + n_i n_j delta(t-r/c_L)/(c_L² r)
        + (3 n_i n_j-delta_ij) t/r³
                    [H(t-r/c_L)-H(t-r/c_T)] }.

The last term lies between the two wavefronts and is necessary. Omitting
it gives the wrong Fourier/static response. Although P_L and P_T separately
are nonlocal spatial projections, their retarded combination vanishes for
t<r/c_L; the real tensor makes the cancellation explicit. For t<0 it is
zero as well. The source response is u=-4 pi G G_ret*(rho e).

One derivation writes G=alpha^-1[I g_T+partial_i partial_j h], where
g_c=delta(t-r/c)/(4 pi c² r) and Delta h=g_L-g_T. For fixed t>0 the
two shells each integrate to t. Thus h'=0 beyond the outer shell, and
h'=-t/(4 pi r²) between the shells. Radial differentiation gives the two
surface terms and the displayed intervening term, with no outer support.

The time integral recovers B^-1(x). After contraction with e, integration of
the intervening term gives
(3cos²(theta)-1)(1/c_T²-1/c_L²)/(8 pi alpha r), which combines with the
two shell integrals to give [N+D+(N-D)cos²(theta)]/(8 pi r).
This is a direct causal-to-static bridge, not inference from a group velocity.

## What changed and what remains unbuilt

The old two-scalar classification fixed the spatial action and allowed only
a constant two-field time Hessian. This construction replaces that action
with three propagating local components and couples the source to e.u.
It is outside that proved restriction. It provides a constructive example
of why the old result did not exclude all causal realizations of the static
linear susceptibility.

For N=D, beta=0 and c_L=c_T: the intervening term cancels, all three fields
obey the same wave equation and only the e component is sourced/read out.
As D approaches zero with N and alpha fixed, c_L diverges. There is no
uniform finite-speed or uniformly bounded-coefficient D=0 limit.
A response with D=0 is outside the strict D>0 hypothesis.

For a nonlinear response N(A), identifying e with a background gravitational
field direction and D with N+A N' can label homogeneous coefficients. It does
not reconstruct a nonlinear vector law. Making e,N,D functions of dynamical
fields changes the variational equations and introduces additional terms.
No such substitution is silently made here. The original nonlinear static
operator and any of its empirical comparisons require separate derivations.

The observational target is now sharper: any such completion must account
for extra propagating modes and its background direction while recovering
the source-dependent static response. No mode is identified with measured
tensor radiation or light, and alpha has no empirical calibration. A nonlinear source and
matter/metric coupling, background formation, lensing, cosmology and quantum
interaction completion remain open. This packet is conditional constructive
mathematics, not a TOE or an empirical detection.

## Reproduction and checked resolution

Run `python3 scripts/local_vector_homogeneous_response_2026_10_12.py`.
Use `--json` for the same deterministic scientific result as JSON; an optional
`--output-json PATH` writes an exclusive same-run sidecar. Normal invocations
work repeatedly without replacing canonical files. The paired note is an
explicit package-integrity input. Scientific constants in the controls are
synthetic and are not physical calibrations.

The runner checks the complete symbolic tensor inverse, stable eigenvalues,
frequency response, static point-source kernel and retarded time integral.
Sixty-four real-space/Fourier comparisons include an independently integrated
intervening term. One hundred twenty flux samples and nine off-cone points
are diagnostics supporting the analytic proof. Omitting the intervening term
is a deliberate failed alternative caught by a decisive control. Sampling
alone is not the proof of causality, positivity or the continuum theorem.
