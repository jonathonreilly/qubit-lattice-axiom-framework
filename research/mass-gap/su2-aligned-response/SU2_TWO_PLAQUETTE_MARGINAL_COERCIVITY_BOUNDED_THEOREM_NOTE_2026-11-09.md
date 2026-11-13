# Compact coercivity of the two-plaquette SU(2) marginal

Status: proposed_retained

This note proves a volume-uniform compact energy bound after integrating the
seven terminal edges belonging to two adjacent plaquettes. It also derives
the identity-chart Hessian of the actual normalized marginal. These are
finite two-step results; the marginal's connected-response bound remains open.
Formal retained status requires the separate audit path.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "compact coercivity for the actual seven-edge two-plaquette marginal"
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Re-establish regional and chart suppliers for the actual marginal, then bound its complete connected fourth response."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Compact deterministic inequality and exact finite-u Hessian for a supplied two-step SU(2) family, with identity exterior and zero sources."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## Exact law and compact theorem

Use the [original normalized word-mean kernel](SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md),
odd L>=3, kappa>0 and fine torus side N=L^2 m with m>=3 in four dimensions.
Let J be the seven independent positive terminal edges in the boundaries of
two distinct elementary terminal plaquettes sharing exactly one edge, and
O=E2\J. Both coplanar and hinged pairs are included. At zero sources and
exterior terminal output V_O=I, the exact hidden marginal is

    rho_J(dU0 dU1)=Q_J^(-1) q_u(U0) K0(U1|U0)
                         product_(c in O) k1,c(I|U1) dU0 dU1.

Here q_u=Z_fine(u)^(-1) exp(-u W0) and t=kappa u. Every surviving kernel is
exp(t<output,M>)/Z(t|M|), with its actual 24L^4 paired-root-leg path mean.
Integrating an edge in J deletes its entire normalized last-layer kernel;
it does not delete any other normalizer or create an intermediate Wilson
action. See the [exact marginal identity](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/partial-terminal-normalization.md).

Use the same terminal-root fine forest as the fully pinned model, with
arbitrary internal spanning trees. All intermediate links remain variables.
Let a_e denote its retained compact group coordinates, w(A)=Re Tr(A)/2, and

    gamma0,e=|M0,e|-<U1,e,M0,e>,
    gamma1,c=|M1,c|-<I,M1,c>,
    E_J=W0+kappa sum_all gamma0,e+kappa sum_(c in O) gamma1,c.

**Compact theorem.** There is a finite C=C(L,kappa) such that, on the entire
compact forest slice,

    sum_retained [1-w(a_e)] <= C E_J.                         (1)

The constant is uniform in volume, placement, orientation and internal tree
choice. The theorem includes zero means and periodic seams, including m=3.
No useful numerical size or optimized value of C is asserted.

The [complete proof](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/two-plaquette-compact-coercivity.md)
has three steps. The two plaquettes use at most three coordinate directions.
Choose an unused direction rho. Every missing terminal edge c has a
three-edge retained detour in the translated rho slice. Its fine straight
transporter T_c and the detour bound an L^2-by-L^2 fine square with identical
lifted endpoints. Thus, with chord distance d,

    d(I,T_c)^2 <= 4 L^4 sum_(p in square(c)) W_p
                       +6 sum_(d in detour(c)) d(I,T_d)^2.   (2)

Actual path-filling discrepancies control each retained T_d by fine Wilson
terms, level-zero centered gaps and its own retained terminal gap. They also
bound each missing auxiliary gamma1,c from above, without replacing a
centered energy by an uncentered one. Expanding all these positive local
forms gives a finite coefficient-mass bound Q(L), including multiplicities.
Since exactly seven constraints are missing,

    E_all <= [1+7 kappa Q(L) max(1,kappa^(-1))] E_J.

The existing [all-terminal forest estimate](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/compact-energy-coercivity.md)
then proves (1), with

    C=K(L) max(1,kappa^(-1))
           [1+7 kappa Q(L) max(1,kappa^(-1))].

Both K and Q have finite template definitions in the complete proof. Taking
coefficient maxima over internal trees and adding projected repetitions
prevents volume-dependent congestion. E_all is an auxiliary deterministic
function; the actual probability law remains rho_J throughout.

## Actual normalized Hessian

Write a_e=exp(i x_e dot sigma) in the injective identity chart and let S_J(x)
be minus the logarithm of rho_J's chart density with respect to Lebesgue
measure. There are n=m^4(3L^8+1+4L^4) retained group links. With
h(s)=log Z(s)-s and j(x)=(sin|x|/|x|)^2, it is exactly

    S_J=log Q_J+log Z_fine(u)+n log(2pi^2)+u E_J
          +sum_all h(t|M0,e|)+sum_O h(t|M1,c|)-sum_e log j(x_e).

Let Q0,Q1 be the actual linear path means and V0,V1,O their summed path
variance forms, with terminal terms only in O. The
[normalized-kernel calculation](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/partial-terminal-normalizer-hessian.md)
gives, for finite u>=1,

    H_J := u^(-1) D^2 S_J(0)
       = H_E,J+kappa[1-Z'(kappa u)/Z(kappa u)] diag(V0,V1,O)
                   +(2/(3u)) I,
    <x,H_E,J x>=||d0 x0||^2+kappa||x1-Q0 x0||^2
                                      +kappa||P_O Q1 x1||^2.

The variance correction is nonnegative. The radial normalizer alone has a
negative Hessian contribution; the formula above uses the complete kernel
and includes the coordinate-Haar correction. No term from a deleted kernel
remains. Expanding (1) at identity proves

    H_J >= [C^(-1)+2/(3u)] I.                              (3)

The finite upper bound and range-two reader property in the normalized-kernel
proof also persist under deletion. This is a precision bound on the stated
forest coordinates, not a physical energy-spectrum gap or global convexity.

## Checking record and next obligation

The [fresh-context check](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/gates/two-plaquette-coercivity-check.md)
records the exact source hashes and independent derivations. These research
checks do not replace a formal audit. Luna's
[repo and primary-literature search](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/sources/two-plaquette-coercivity-prior-art-20261109.md)
found the existing all-terminal supplier but no matching sparse-deletion
theorem in the bounded search. The
[Fable 5.2 approach consultation](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/sources/fable-two-plaquette-approach-20261109.md)
is advice, not a certification or imported theorem.

The next obligation is to check the regional relative-energy estimates,
nonlinear chart estimates and compact connected expansion for rho_J itself,
then bound its complete fourth cumulant with all source and orbit covariance
terms. This note proves no such bound, no nonidentity-terminal extension,
no closure under further blocking, and no continuum Yang-Mills mass gap.
