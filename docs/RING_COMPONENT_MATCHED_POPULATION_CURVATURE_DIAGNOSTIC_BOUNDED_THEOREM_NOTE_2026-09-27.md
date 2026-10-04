---
claim_id: ring_component_matched_population_curvature_diagnostic_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: For a supplied finite ring component, deterministic preparation and fixed computational protocol, the three-field curvature functional is compared across four finite walker populations to its matched finite-age numerical reference. Complete independent-replica covariance controls descriptive standard errors and a prespecified held-population diagnostic. No asymptotic extrapolation, confidence coverage or physical photon identification is established.
upstream_dependencies:
- finite_projection_mixed_energy_and_curvature_target_bounded_theorem_note_2026-09-27
runner: scripts/ring_component_matched_population_curvature_2026_09_27.py
---

# Matched finite-population curvature in a supplied ring component

Type: bounded_theorem
Status: proposed_retained

**Target.** Reproduce the completed fixed 1024-replica finite-component test,
using the same preparation, fields and projection ages for each population,
and evaluate its prespecified covariance-aware comparison to the matched
finite-age reference and its held-population prediction. The result is a
finite numerical diagnostic. Standard errors below are descriptive replica
scatter, not certified confidence intervals or a population-limit theorem.

The [finite-projection target theorem](FINITE_PROJECTION_MIXED_ENERGY_AND_CURVATURE_TARGET_BOUNDED_THEOREM_NOTE_2026-09-27.md)
derives the exact-distribution mixed finite-age target and the one-walker
boundary. This note evaluates the finite-population estimator in a specified
small component. It supplies no equivalence between its small-torus bias and
bias in a larger torus or a differently prepared calculation.

## Fixed model, preparation and observable

The supplied model has spin values sigma_l=+-1 on the oriented links of a
periodic L=2 cubic graph, with zero vertex divergence and plaquette reversal.
Each oriented elementary plaquette is retained as a separate graph term,
including the parallel-link geometry of this small torus. With g=1,V=0,
H0 has off-diagonal element minus the number of allowed reversals between
configurations and zero diagonal. The initial state is the canonical pattern
sigma_(v,0)=(-1)^v_1, sigma_(v,1)=(-1)^v_0, sigma_(v,2)=(-1)^v_0. The code checks Gauss legality and exhausts its full
connected plaquette-reversal component: 864 configurations and 6912 nonzero
matrix entries, including spin reversal symmetry. There is no truncated queue.

Define the cyclic transverse field

    F(sigma)=sum_(v,a) cos(pi*v_((a+1) mod3))*sigma_(v,a),
    H_h=H0-h*diag(F),
    psi_hg(sigma)=exp(.2*N_flip(sigma)+.5*hg*F(sigma)).

The two computational guide schemes use hg=.15 for all fields, or hg=h at
its own field. Guides are numerical devices, not additional physical terms.
At each field the initial distribution is the same delta on the canonical
state. In particular, it is not a population-dependent VMC bank.

For population Nw in {64,128,256,512}, evolve the positive-guide jump process
at proposal rate psi(s')/psi(s) per allowed reversal, with the local energy
(H_h psi)/psi supplying the continuous-time weight. The carried source
implements these local rates and systematic resampling every .015 through
2000 generations. At every generation it records the weighted endpoint
mixed energy before resampling. Retain zero-based indices500:2000, whose
ages are7.515,...,30. The observable is exactly

    chi=(15*Ebar(0)-16*Ebar(.15)+Ebar(.30))/(9*8*.15^2).

This finite-probe functional is the declared target; it is not silently
identified with the second derivative at zero. The mode pi lies at the zone
edge on L=2. The factor9*8*.15^2 is supplied consistently for comparison with
this computational functional, without a physical susceptibility calibration.

## Sampling and analysis fixed before confirmation

Each of 1024 replicas uses Numba seed1930000+j and NumPy seed1940000+j.
For each population/scheme restart those same two seeds, then consume the
streams sequentially across fields0,.15,.30. Pair all24 field/population/guide
means inside each replica. Distinct replicas are the sampling units under the
explicit ideal independent-stream interpretation. Walkers and generations are
not treated as iid. A shared seed does not imply equal paths or zero covariance.

This design was fixed after a completed64-replica diagnostic had revealed
insufficient precision for the intended comparison. It is therefore a new
precision study informed by earlier results, not preregistration before all
model selection. It uses fresh streams and populations64/128/256/512, and
never pools the earlier64 samples. The 1024 run finished at its fixed count;
no outcome-dependent stopping or subsequent sample extension is performed.
The public cold execution reproduces that same design and seeds. It is not
an additional independent statistical experiment.

For replica vectors e_j in R^24, compute the unbiased sample covariance
S_e=sum_j(e_j-ebar)(e_j-ebar)^T/(1024-1). Let W be block-diagonal with weights
(15,-16,1)/(9*8*.15^2). The curvature sample covariance is W S_e W^T, checked
against direct sample covariance. The descriptive SE of a mean contrast a
is sqrt(a^T S_chi a/1024). This algebra retains every cross-field, population
and guide covariance. It assumes no CLT or finite-sample coverage guarantee.

The fixed OLS intercept in1/Nw uses only64,128,256, with weights(-1/2,1/2,1).
Its prediction at held512 uses(-9/28,13/28,6/7). These weights follow from the
three-point normal equations, and are checked independently of the simulation.
The held residual is computed replica by replica before its SE. These are
fixed linear diagnostics, not a validated extrapolation law or a fitted
physical parameter. No acceptance threshold is assigned to a residual.

## Matched reference

Rebuild the integer component, diagonalize each of H0,H_.15,H_.30, and use
all eigenvectors to evaluate the mixed ratio at every retained age. For the
canonical basis vector e0 and the appropriate psi, the exact-distribution
energy is

    E_mix(t)=psi^T H_h exp(-t H_h)e0 / (psi^T exp(-t H_h)e0).

The initial scalar1/psi(e0) cancels. Average these ratios across exactly the
1500 ages before forming the same three-field functional. The public runner
checks spectral residuals/orthogonality and compares a separate sparse
matrix-exponential algorithm at ages7.515 and30 for every field/guide.
These are floating numerical checks, not exact-real error enclosures.
The resulting reference is approximately1.4603833395 for the common guide
and1.4603833554 for per-field guides. It is not the literal ground-state
curvature or an established finite-walker limit.

## Completed fixed results

Every plus/minus entry is a descriptive replica SE under the stated sampling
interpretation. The raw64 experiment is preserved separately. The table below
is the completed1024 experiment whose public reproduction is required.

| Nw | Common guide | Per-field guide | Paired per-field minus common |
| ---: | ---: | ---: | ---: |
| 64 | 1.633409 +/- .015725 | 1.461636 +/- .011327 | -.171772 +/- .017697 |
| 128 | 1.561935 +/- .011571 | 1.456814 +/- .008139 | -.105121 +/- .012969 |
| 256 | 1.518097 +/- .008753 | 1.454643 +/- .005907 | -.063454 +/- .009918 |
| 512 | 1.478740 +/- .006156 | 1.455065 +/- .004194 | -.023675 +/- .007137 |

| Fixed fit/held diagnostic | Common guide | Per-field guide |
| --- | ---: | ---: |
| Intercept | 1.482360 +/- .012194 | 1.452232 +/- .008434 |
| Intercept minus finite-age reference | .021977 +/- .012194 | -.008152 +/- .008434 |
| Prediction at512 | 1.501386 +/- .010042 | 1.453403 +/- .006959 |
| Observed512 minus prediction | -.022646 +/- .011565 | .001662 +/- .007760 |

The common-guide sample means vary substantially with population here, and
the per-field sample means lie closer to the matched reference. The held
common-guide mean is below its fixed prediction; the per-field residual is
small relative to its descriptive SE. These facts neither validate nor
formally reject an asymptotic1/N law. A small held residual alone cannot
establish the infinite-population intercept. The guide comparison is scoped
to this component, preparation, observable and schedule.

## Evidence and review record

The kernel carries eleven definitions from the source at PR9356 head
`1f2e49a0b1b9a2f84f8abc099020baf3655c1518`, original runner SHA-256
`9cf868253ee64f6d4ca2914f2afea94e53900e5848cc600029b513647a06955d`.
Those source definitions are included here; no unmerged file or absolute
private path is a runtime dependency. Only unrelated benchmark execution,
VMC-bank generation and alternative benchmark statistics were omitted.
Independent earlier geometry/rate reconstruction checked all6912 directed
component rates and the matched reference under exact source identities.
The new public construction preserves those definitions and needs its own
composition check. Kernel reuse is disclosed, not called independent physics.

The complete private1024 raw replica stream and six-source freeze are
preserved. A separate independent reconstruction froze scalar-fsum time
averages, explicit covariance sums and scalar normal-equation fits before
reading the primary numerical summaries. It matched865 numeric comparisons
and complete replica arrays within5.9e-14. This is independent extraction
and arithmetic on the same data, not fresh stochastic replication. The
public source/runner closure and its execution are separate obligations;
exact receipts and author mutation controls belong to the publication handoff.
The earlier64 and all original failure evidence remain preserved.

No physical state preparation, dynamics-to-photon identification, physical
field probe or normalization, detector mapping, dimensional calibration,
population/volume limit or empirical comparison is supplied by this fixture.
Those are open research obligations, not an exclusion of possible future
bridges. Mass or cosmological-number claims cannot use these finite numerical
values as measured or parameter-free physical predictions.

## Imports and obligation graph

| Input | Role/provenance | Open bridge |
| --- | --- | --- |
| Spin-link ring graph, g=1,V=0 and canonical state | Supplied finite model, fully constructed in public source | Physical realization is not derived |
| Guide strengths, fields, mode and normalization | Declared computational choices, identical across comparison targets | No long-wavelength or physical susceptibility identification |
| Age schedule, population grid and seed design | Frozen finite experiment, following the disclosed64-replica precision study | No asymptotic law or random-generator independence proof |
| Positive-guide mixed target | Linked conditional mathematical parent with hypotheses retained | Not an independently proved finite-walker convergence theorem |
| Floating diagonalization/exponentials and covariance arithmetic | Public deterministic calculations and separate-method diagnostics | No exact-real interval certificate or CLT coverage theorem |

The obligation graph is finite graph/preparation -> exact-distribution mixed
ratio and matched age/probe functional -> finite stochastic source protocol
-> independent-replica covariance and prespecified held-population diagnostic.
The fixed finite construction and statistical algebra are given here; a
population-limit theorem and physically calibrated source-to-detector chain
remain outside this result. Nonfinite recorded energy/log-weight outputs, a component-ceiling or Gauss
failure, and failed specified numeric tolerances abort execution. Zero
inactive proposal rates are allowed; the code does not assert finiteness
of every intermediate rate or weight. No partial
population family or selectively successful replica subset is reported.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
conditional_surface_status: supplied finite ring component and fixed numerical sampling protocol
hypothetical_axiom_status: no new axiom or primitive adopted
admitted_observation_status: no physical observation supplied
claim_type_reason: finite numerical consequence with explicit mathematical target and uncertainty scope
trace_class: upstream_support
target_claim_id: null
target_blocker_text: observable-specific sampling and extrapolation control before interpreting size trends
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: Control finite-population and volume limits for the same physical observable and preparation before interpreting size trends.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
