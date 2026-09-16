# Joint weak-coupling limit of a charged compact rotor

**Provisional author research proposal.** Personally developed and checked;
no independent review, audit, retained status, or main-branch landing.

The proposed result removes a prescribed order of limits from a supplied
charged compact-rotor construction. The microscopic coupling g may tend to
zero and the cubic volume L^3 may tend to infinity along any joint sequence.
For fixed local probes the argument identifies a Gaussian gauge-field state,
a filled-band free-fermion state, their equal-time factorization, finite-time
gauge two-point propagation, and bounded neutral matter correlations at
finitely many times.

The coupling still tends to zero. This proposal does not establish that
making the system large weakens a fixed positive microscopic interaction.
It does not select the Hamiltonian, weights, state or physical clock from
axioms, establish a finite-qubit realization, or complete a TOE.

## Proof map

All load-bearing mathematical arguments are included in this packet.
References to the preceding campaign are history, not unmerged theorem
inputs. The dependency links below identify the connected proposal.

| Argument | New step | Dependencies in this packet |
|---|---|---|
| [Uniform compact-field control and soft response](notes/BLOCK01_UNIFORM_COMPACT_FIELD_AND_SOFT_RESPONSE.md) | Exact Gauss-neutral Gaussian trial; volume-uniform field concentration and low-energy inelastic spectral weight | Supplied model stated in the note |
| [Uniform ground energy and oscillator defects](notes/BLOCK02_UNIFORM_GROUND_ENERGY_AND_OSCILLATOR_DEFECT.md) | Optimized integer Gaussian, exact positive squares, and a block Slater trial with charge dressing; error density O(sqrt(g)+1/L) | Compact-field estimate |
| [Joint gauge characteristic limit](notes/BLOCK03_JOINT_EQUAL_TIME_GAUGE_LIMIT.md) | Fourier covariance positivity and an approximate-annihilator differential equation | Energy/defect and compact-field estimates |
| [Joint gauge and matter state](notes/BLOCK04_JOINT_GAUGE_AND_MATTER_STATE.md) | Weyl products, neutral rooted CAR, filled-band covariance, purity and factorization | The three preceding arguments |
| [Real-time gauge two-point functions](notes/BLOCK05_JOINT_REAL_TIME_GAUGE_TWO_POINT.md) | Exact electric equation, norm generator residual, summable square-root kernel and controlled magnetic-smear approximation | Compact-field and energy/defect estimates |
| [Bounded matter dynamics](notes/BLOCK06_JOINT_BOUNDED_MATTER_DYNAMICS.md) | Rooted CAR generator residual and free-spreading control without a finite-volume gap | Compact-field estimate and limiting matter state |

These are author proofs awaiting independent mathematical review. No open
terminal lemma is being substituted for the stated scoped conclusions.
The broader fixed-positive-g infrared phase is a different unresolved target.
Full nonlinear gauge dynamics and arbitrary mixed unbounded multi-time
products also lie beyond this packet.

## Supplied inputs and restrictions

The model has continuous integer link rotors, exact integer Gauss law with
charges +/-1, positive homogeneous electric/magnetic weights, continuous
Hamiltonian time, and conjugate two-orbital number-conserving Wilson matter.
The initial state is the normalized full ground-space trace in N_+=N_-=L^3.
The band parameters obey0<zeta<1; their values and the weights are supplied.
No fitted or observed empirical number is used in these derivations.

The first compact-field result permits a broader matter class, including
an optional nonnegative onsite charge penalty. All subsequent free-state
and free-dynamics conclusions explicitly exclude an additional unscaled
onsite interaction. Such an interaction would survive when the gauge
coupling vanishes. This restriction is part of the theorem's model domain.

Poisson summation, finite-dimensional spectral algebra, Fourier analysis
and CAR identities are the mathematical machinery. The relevant formulas,
normalizations and hypotheses are derived or checked in the notes. The
[literature screen](READING_LEDGER.md) located no ready theorem with all of
the desired fixed-g massless charged compact hypotheses; that is a search
report, not a literature-exhaustion or impossibility claim. No literature
phase theorem is imported to close the argument.

## Evidence and reproduction

The seven active [finite challenge programs](review/MILESTONE_PERSONAL_REVIEW.md)
test consequential identities using different representations: integer
Fourier sums versus Poisson dual sums, Fock matrices versus Slater determinant
curvature, literal curl matrices versus geometric formulas, finite rotor
exponentials versus transport/Duhamel identities, and a charged Gauss basis
versus rooted-CAR commutators. They do not numerically prove an infinite-volume
phase. Each declares a120-second timeout, its package-local helper inputs
where used, and its source-integrity reads.

From the repository root, reproduce the active raw evidence with:

```sh
pack=.claude/science/physics-loops/toe-interacting-scale-20260916
for runner in "$pack"/evidence/*_check.py; do
  OPENBLAS_NUM_THREADS=1 python3 "$runner" > "${runner%.py}.txt" 2> "${runner%.py}.stderr"
done
OPENBLAS_NUM_THREADS=1 python3 "$pack/review/milestone_mutation_checks.py"
```

The JSON files and paired stdout/stderr are raw author-run artifacts, not
audit caches. The [mutation harness](review/milestone_mutation_checks.py)
changes temporary copies only. Its [record](review/milestone_mutation_checks.json)
retains28 nonzero exits at the intended mathematical assertions, including
wrong signs, missing factors, a lost projection, and reversed time direction.
Assertion totals include repeated finite basis checks and carry no scientific
status. The final byte inventory is [the manifest](MANIFEST.json).

Both unexpected propagation-check failures are preserved: a
[scalar-conversion failure](review/BLOCK05_FAILURE_01/RECORD.json) and an
[insufficient numerical flux cutoff](review/BLOCK05_FAILURE_02/RECORD.json).
The latter was corrected by enlarging the electric basis at the same declared
threshold. Numerical propagation was stable under that refinement. Existing
finite-boundary discrepancies and finite zero-mode ambiguities remain visible.

## Review and downstream boundary

The [personal milestone review](review/MILESTONE_PERSONAL_REVIEW.md) records
the model restriction, semantic checks, mutation coverage, raw-evidence
provenance, and limits of author verification. This is a draft proposal in
an exploratory packet. It introduces no formal claim/audit rows and requests
no audit verdict or direct main merge. Formal source registration, restricted
audit packet mapping, cache execution and integrated landing validation remain
work for a later authorized promotion/review path.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: Remove the prescribed order of weak-coupling and volume limits in the supplied charged-rotor bridge.
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: Independently review the joint-limit argument and pursue the separate fixed-positive-coupling infrared remainder.
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: Provisional model theorem with explicit supplied law, coefficients and state; no axiomatic selection or independent acceptance is asserted.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
