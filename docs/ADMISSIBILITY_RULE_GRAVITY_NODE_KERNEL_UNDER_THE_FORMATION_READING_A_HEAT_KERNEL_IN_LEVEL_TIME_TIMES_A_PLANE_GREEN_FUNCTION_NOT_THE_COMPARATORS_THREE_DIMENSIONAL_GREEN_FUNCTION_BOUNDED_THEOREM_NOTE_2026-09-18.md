---
claim_id: admissibility_rule_gravity_node_kernel_under_the_formation_reading_a_heat_kernel_in_level_time_times_a_plane_green_function_not_the_comparators_three_dimensional_green_function_bounded_theorem_note_2026-09-18
claim_type: bounded_theorem
claim_scope: "For the supplied gain-one recurrence on a finite periodic plane, derive early-late Hermitian mode covariance with the conjugated multiplier, its stationary nonzero-mode form, an explicit symmetry subgroup and a mode decay bound. The static lattice Green comparator also has a plane-amplitude times layer-propagator representation, with small-wavevector decay linear rather than quadratic in the transverse wavenumber. This recurrence is a supplied linear comparator, not the exact finite-beta Cartesian mean linearization of the nonlinear sphere kernel. Historical nonlinear simulations are author-reported finite observations, not newly verified results or asymptotic theorems. No physical rule, gravity kernel or axiom selection is derived; no clause is adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
  - admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_and_the_nonlinear_law_measured_against_it_bounded_theorem_note_2026-09-17
runner: scripts/admissibility_rule_gravity_node_kernel_under_the_formation_reading_heat_kernel_in_level_time_times_plane_green_function_2026_09_18.py
---

# Level covariance of a supplied gain-one recurrence and a lattice Green comparison

**Date:** 2026-09-18
**Type:** bounded_theorem

## Result and scope

For the supplied gain-one recurrence on a finite periodic plane, derive early-late Hermitian mode covariance with the conjugated multiplier, its stationary nonzero-mode form, an explicit symmetry subgroup and a mode decay bound. The static lattice Green comparator also has a plane-amplitude times layer-propagator representation, with small-wavevector decay linear rather than quadratic in the transverse wavenumber. This recurrence is a supplied linear comparator, not the exact finite-beta Cartesian mean linearization of the nonlinear sphere kernel. Historical nonlinear simulations are author-reported finite observations, not newly verified results or asymptotic theorems. No physical rule, gravity kernel or axiom selection is derived; no clause is adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Exact properties of an explicitly supplied linear recurrence"
source_of_blocker_text: scoped_review
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Establish a controlled connection to the nonlinear kernel before importing linear conclusions"
conditional_surface_status: "Gain-one surrogate and stated finite checks; nonlinear observations remain historical"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Algebraic identities under explicit model assumptions"
```

## Premises and declared objects

Fix beta>0, L>=2, and the supplied recurrence theta(t+1)=P theta(t)+xi(t) from zero, where P averages the sites x,x-e1,x-e2 of the preceding level of the periodic L by L plane. The centered noises are independent across sites and levels with component variance sigma^2=A(3beta)/(3beta), A(kappa)=coth(kappa)-1/kappa. Use the positive-exponent modes X_k=L^-1 sum_x exp(+ik.x)theta_x. The proxy exp(-v_t) is defined from the component site variance; it is not identified with nonlinear magnetization.

The separate nonlinear sphere kernel is K_beta(ds|S) proportional to exp(beta s.S) on the real unit sphere, where S is the sum of three predecessor spins. Its normalization under uniform sphere measure is sinh(kappa)/kappa, kappa=beta|S|. Differentiating gives E[s|S]=A(kappa) S/|S|. At S=3e_z, the transverse Cartesian derivative is delta E[s_perp]=(A(3beta)/3)delta S_perp. Integration by parts in the polar coordinate gives E[s_x^2]=A(kappa)/kappa. Thus the chosen noise variance is the aligned conditional variance, but the exact Cartesian mean gain is A(3beta), not one. A direction-normalized or strong-coupling approximation needs an additional argument; none is supplied here.

The fixed rule and record sentences of [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) motivate the comparison. The [finite-window rule note](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md) supplies background only. All mathematical premises used below are restated here; no unlanded sibling theorem is used as proof.

## Theorem T1 — covariance and its orientation

Define X_k(t)=L^-1 sum_x exp(+ik.x) theta_x(t), phi=(1+exp(ik1)+exp(ik2))/3 and u=|phi|^2. Backward spatial shifts have multiplier exp(+ikj), so X(t+s)=phi^s X(t)+independent later noise. For a centered complex mode, variance means E|X|^2. With initial zero field,

V_t(k)=sigma^2 sum_(j=0)^(t-1) u^j,
C_early,late=E[X(t) conjugate(X(t+s))]=conjugate(phi)^s V_t,
C_late,early=phi^s V_t.

Thus V_t=sigma^2(1-u^t)/(1-u) for u<1 and sigma^2 t at zero. In real site coordinates the early-late covariance matrix is Sigma_t (P^s)^T; on the mean-zero subspace its stationary form is sigma^2(I-PP*)^-1(P*)^s. The plane-average covariance is sigma^2 t/L^2 for all s>=0. The exact matrix checks on L=3,4 include cosine modes; a separate complex L=4 character distinguishes phi from its conjugate.

## Theorem T2 — quadratic form and explicit symmetries

Expanding the exact identity
1-u=(4/9)[sin^2(k1/2)+sin^2(k2/2)+sin^2((k1-k2)/2)]
gives 1-u=k^T M k+O(|k|^4), M=[[2,-1],[-1,2]]/9, with coordinate eigenvalues 1/9 and 1/3. These are oblique level-plane coordinates; their unequal eigenvalues alone do not prove physical anisotropy. The cone axis is normal to the plane, not one of these two in-plane directions.

The substitutions (k1,k2)->(k2,k1) and (k1-k2,-k2) generate the displayed order-six subgroup preserving u. Inversion also preserves u; the runner does not classify a maximal symmetry group. The comparator E(k1,k2,k3)=sum_j 2(1-cos(kj)) is invariant under all 48 signed permutations and has E=|k|^2+O(|k|^4).

## Theorem T3 — decay bound and corrected static comparison

For |kj|<=pi, sin(|kj|/2)>=|kj|/pi gives 1-u>=4|k|^2/(9pi^2). Hence |C_s|/C_0=u^(s/2)<=exp(-(1-u)s/2)<=exp(-2|k|^2 s/(9pi^2)). This is a modewise upper bound, not by itself a scaling-limit theorem. The expansion phi=1+i(k1+k2)/3+O(|k|^2) specifies the phase in this coordinate convention.

The original non-product argument was false. A mixed derivative of log E can exclude a separated frequency product f(k1,k2)g(k3), but cannot exclude a transverse amplitude times an s-dependent propagator after inverse transformation in k3. In fact, for a=2(1-cos k1)+2(1-cos k2)>0, set

rho=(a+2-sqrt(a(a+4)))/2, alpha=-log rho.
G_s(a)=rho^|s|/sqrt(a(a+4))=exp(-alpha|s|)/(2sinh alpha).

Since rho+rho^-1=a+2, this decaying sequence satisfies (a+2)G_s-G_(s-1)-G_(s+1)=delta_(s,0). The zero-site jump follows from rho^-1-rho=sqrt(a(a+4)). It is therefore the inverse in the layer coordinate of a+2(1-cos k3). Both kernels have a plane-amplitude times layer-propagator form. The actual distinction is alpha=arcosh(1+a/2)~sqrt(a) near zero, while -log|phi|=(k^T M k)/2+O(|k|^4). The static decay is linear in small transverse wavenumber, and the supplied recurrence's decay is quadratic. The comparator 1/(beta E) is a supplied Green kernel; an infrared upper bound by it would not identify an actual nonlinear covariance with it.

## Historical nonlinear observations (not fresh evidence)

The following table is preserved from the original author submission. Original simulation scripts, outputs and failed exponential-fit estimator remain recoverable on the original PR branch. They are not included in the current canonical runner certificate. The listed samples neither prove size independence nor a limiting coefficient, an exact phase or a universal memory law.

| `β` | `|m|` | `S₀(k)/[σ²/(1 − u(k))]`, `|k| < 0.3` | `0.6–1.0` | `1.5–2.2` | `3.2–5.0` | `C_s/C_0` against `φ^s` at `k = 2π(4,1)/L`, `s = 64` (modulus) | at `k = 2π(8,8)/L`, `s = 64` |
|---|---|---|---|---|---|---|---|
| 6 | `0.736` | `0.830` | `0.861` | `0.878` | `0.887` | `0.909 / 0.946` | `0.798 / 0.760` |
| 12 | `0.876` | `0.898` | `0.934` | `0.936` | `0.938` | `0.965 / 0.946` | `0.726 / 0.760` |
| 24 | `0.937` | `0.940` | `0.967` | `0.966` | `0.967` | `0.986 / 0.946` | `0.768 / 0.760` |

## Boundaries, falsifiers and imports

No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.

No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

A wrong covariance, multiplier, enclosure or Green recurrence falsifies its stated identity. The finite controls do not prove nonlinear asymptotics, physical anisotropy, a gravitational field or the selection of a model. No audit verdict is applied. Standard finite probability, character diagonalization and elementary series are the mathematical tools.

## Review record

The original author's experiments and review claims are historical provenance. This revision corrects the gain assumption and the covariance conjugation and static factorization argument. The current certificate is the fresh canonical runner output; independent review evidence is recorded by the landing receipt.

## Verification

```bash
python3 scripts/admissibility_rule_gravity_node_kernel_under_the_formation_reading_heat_kernel_in_level_time_times_plane_green_function_2026_09_18.py
```

Cached output: `logs/runner-cache/admissibility_rule_gravity_node_kernel_under_the_formation_reading_heat_kernel_in_level_time_times_plane_green_function_2026_09_18.txt`.
