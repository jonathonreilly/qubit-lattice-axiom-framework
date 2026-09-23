---
claim_id: compact_rotor_convex_carrier_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/compact_rotor_convex_carrier_check_2026_09_16.py
upstream_dependencies: ["compact_rotor_bridge_cubic_bounded_theorem_note_2026-09-16"]
claim_scope: "Explicit nonperiodic convex comparison, global derivative bounds and exact equality on the specified small raw-curl region."
---

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

Load-bearing mathematical sources: [Compact Rotor Bridge Cubic Bounded Theorem Note 2026-09-16](COMPACT_ROTOR_BRIDGE_CUBIC_BOUNDED_THEOREM_NOTE_2026-09-16.md).

# A convex real-field action matching the lifted kernel at small curl

Explicit nonperiodic convex comparison, global derivative bounds and exact equality on the specified small raw-curl region.

## 1. A scalar extension with explicit derivative bounds

Fix0<alpha<pi/3. For x>=0 define chi_alpha(x) by

    chi(x)=x,                                  0<=x<=alpha,
    chi(x)=alpha+alpha[u-u^3+u^4/2],
         u=(x-alpha)/alpha,                     alpha<x<2alpha,
    chi(x)=3alpha/2,                            x>=2alpha,

and extend chi oddly to negative x. On the transition interval its
derivative is1-3u^2+2u^3, between0 and1, and its second derivative
matches0 at both endpoints. Thus chi is C2, |chi|<=3alpha/2 and
0<=chi'<=1. Define the even potential v_alpha by

    v_alpha(0)=v_alpha'(0)=0,
    v_alpha''(x)=cos(chi_alpha(x)).                         (1)

It is C4 and agrees exactly with1-cos x for|x|<=alpha. Globally,

    cos(3alpha/2)<=v_alpha''<=1,
    |v_alpha''-1|<=epsilon_alpha:=1-cos(3alpha/2),
    |v_alpha'''|<=sin(3alpha/2)<=3alpha/2.                  (2)

No periodic globally convex potential is being postulated: v_alpha is
a real, nonperiodic extension. Periodicity remains a separate issue.

## 2. Reconstructing the bridge Hessian bound

Use the supplied Hamiltonian and F(f),P(f),R(f) of the source-bound
note, with r=2T^2<1 and delta0=r+g^2T/[2(1-r)]. Let

    Q(h)=integral_0^T ||h(s)||_2^2 ds,
    A_h=integral_0^T <sin(f+Ceta),h>ds.

Differentiating the positive bridge integral gives

    D_h D_k F
       =E integral <cos(f+Ceta)h,k>ds-g^(-2)Cov(A_h,A_k).  (3)

The same mean/variance estimate as for sine in the source-bound note
gives|E cos(f+Ceta)-cos f|<=delta0 pointwise. Its fluctuation gradient
is C*[cos(f+Ceta)h], with L2-time/link norm at most4sqrt(Q(h)).
The fluctuation precision is bounded below by(1-r)D. The
Brascamp-Lieb covariance estimate and ||D^(-1)||<=T^2/8 yield

    g^(-2)|Cov(A_h,A_k)|<=r/(1-r) sqrt(Q(h)Q(k)).            (4)

This is first a finite positive time-grid inequality, with its physical
time weights included, and then passes by the bounded-integral argument
in the source-bound note. Therefore, putting

    delta2=delta0+r/(1-r),

one has at every real source f

    |D^2R(f)[h,k]|<=delta2 sqrt(Q(h)Q(k)).                  (5)

This proof is included to make the convex comparison self-contained
relative to the covariance tool; no earlier draft's status is imported.

## 3. The comparison and its exact equality region

Set

    P_alpha(f)=integral_0^T sum_p v_alpha(f_p(s))ds,
    F_alpha(f)=P_alpha(f)+R(f),
    delta_*=epsilon_alpha+delta2.                          (6)

Since R is the actual bridge correction, this gives EXACTLY

    F_alpha(f)=F(f) if|f_p(s)|<=alpha for every p,s.         (7)

Everywhere on the real source space, (2) and(5) give

    |D^2(F_alpha-Q(f)/2)[h,k]|
                         <=delta_* sqrt(Q(h)Q(k)).         (8)

It is thus uniformly convex in the source norm when delta_*<1.
The cubic estimate from the source-bound note and(2) is

    |D^3F_alpha(f)[h,k,l]|
       <=T[sin(3alpha/2)+delta3] H_3(h)H_3(k)H_3(l),
    delta3=delta0+(1-r)^(-3)-1.                            (9)

The extension changes the explicitly local straight-source action only;
it keeps the entire coupled bridge correction R. No replacement of an
interacting bridge by isolated plaquette factors is made.

## 4. A chain of slabs and its quadratic carrier

Let a_n be normalized real link fields at discrete times nT, with actual
real lifts x_n=g a_n. Consider the comparison action

    S_alpha(a)=sum_n { ||a_(n+1)-a_n||^2/(2T)
       +g^(-2)F_alpha(g C[(1-s/T)a_n+(s/T)a_(n+1)]) }.
                                                               (10)

The first term is the exact covering-space kinetic action. The reference
quadratic action is

    S0(a)=sum_n {||a_(n+1)-a_n||^2/(2T)
       +(T/6)[||Ca_n||^2+<Ca_n,Ca_(n+1)>+||Ca_(n+1)||^2]}.
                                                               (11)

For variations u define B0(u)=D^2S0[u,u]. Summing(8) and using the
nonnegative kinetic part gives the uniform relative bound

    |D^2(S_alpha-S0)[u,v]|<=delta_* sqrt(B0(u)B0(v)).        (12)

The cubic estimate is

    |D^3S_alpha[u,v,w]|
       <=g[sin(3alpha/2)+delta3]
          product_(z=u,v,w)[T sum_n ||Cz_n||_3^3]^(1/3).   (13)

The space-time L3 bound and Jensen interpolation in the source-bound
note remove the factor2 from the earlier maximum-in-time estimate.
These constants do not grow with the number of spatial sites or time slabs.
When necessary, fix boundary values or quotient the common nullspace of
the temporal difference and C before normalizing a real Gaussian measure.
The displayed derivative statements themselves are valid on the full
space and vanish on the common null directions.

For a periodic time chain, the spatial part of the quadratic carrier has
Fourier coefficient

    b(omega)=(2+cos omega)/3 in[1/3,1].                    (14)

More explicitly, S0 is one half of the time-weighted sum of
|Delta_t a/T|^2 plus b(omega)|Ca|^2 in time Fourier variables. The
factor b is retained; the straight interpolation has not been silently
replaced by a one-slice plaquette action. Thus the quadratic carrier is
uniformly comparable, at fixed T, to the standard temporal-difference
and spatial-curl form after its gauge/null directions are handled.

Equation(7) makes the action(10) agree with the actual product of lifted
Hamiltonian kernels, up to the common free-kernel prefactors, whenever
|g(Ca_n)_p|<=alpha at every endpoint. Affine interpolation then stays
inside the equality region. This is a statement about chosen real lifts.

## 5. Concrete gain and the missing compact comparison

For example, alpha and T can be chosen small enough that delta_* is
as small as a fixed analytic comparison requires, and then g can be
chosen sufficiently small but fixed. Equation(13) supplies the uniform
cubic norm that a Hessian estimate alone does not provide. No specific
external field-limit theorem is declared applicable until all its
operator, carrier, state-matching and source hypotheses are verified.

This work has not established a normalized compact-to-comparison representation, including its Jacobian, multiplicity, weights and source dependence. Equation(7) is equality on chosen real lifts only. The original stronger small-principal-flux/global-lift exclusion and its supporting discussion remain complete in the exact archive; formal negative certification is deferred. No photon theorem or impossibility of a future comparison is asserted.

The next proposed conditional construction is to fill finite coarse
current components by integer sheets in contractible spacetime, obtain
a real lift with raw curl equal to principal curl outside the filled
regions, and check whether enlarged defect regions remain dilute. The
probability hypothesis and its proof status must be explicit; no new
phase premise may be hidden in the word "dilute".


## Evidence, scope and recovery

The [primary](../scripts/compact_rotor_convex_carrier_check_2026_09_16.py) retains the original numerical domains and tolerances. Its [capture destination](../logs/runner-cache/compact_rotor_convex_carrier_check_2026_09_16.txt) and JSON destination under the same directory bind future actual-source evidence. TOTAL counts completed diagnostic families, not individual assertions. No primary was run during author preparation.

The [exact original recovery](work_history/review_loop/pr8166/README.md) preserves every original proof, failed attempt, mutation and output. Historical author review/status statements are not current independent authority.

## No-Go Discipline Gate

N1: Formal negative certification is deferred; no five-route packet is invented. The live claims are the displayed positive conditional implications.
N2: Shared comparison and supplied-model premises are not independent walls.
N3: Geometry, time weights, norms, coupling and mathematical imports remain explicit.
N4: Finite checks support specified identities; they do not execute normalized compact transfer.
N5: The runner states per_element, per_site, per_mode, per_block and lattice_wide scope; infinite-domain conclusions rely on the written proofs.
N6: Exact normalized winding/source representations remain open work; no new axiom is proposed.
N7: Compact transfer, covariance identification and physical selection have not been established here. No impossibility conclusion is substituted.
N8: Original stronger negative arguments remain exact in history, with branch retention for deferred partial closure. The limitation of the certification packet does not disprove the positive mathematics.
