# Post-Record Stable-Kernel Expected-Frequency Interface

**Date:** 2026-06-06
**Type:** exact conditional dynamics/count interface
**Claim type:** bounded_theorem
**Status:** exact-support branch-local for expected empirical frequencies under
a supplied stable reset kernel; target prior, kernel, probability law, and
physical clock remain open; audit_required_before_effective_retained=true;
bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_stable_kernel_frequency_interface_2026_06_06.py`](../scripts/frontier_post_record_stable_kernel_frequency_interface_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_stable_kernel_frequency_interface_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_stable_kernel_frequency_interface_2026_06_06.txt)

## Result

For a supplied finite target prior `pi`, supplied `0 < alpha < 1`, and reset
kernel

```text
K(i,j) = (1-alpha) delta_ij + alpha pi_j,
```

the ensemble distribution after `t` event steps from initial law `p0` is

```text
p_t = pi + (1-alpha)^t (p0 - pi).
```

Therefore the expected empirical frequency vector over the first `N` event
slots is

```text
E[f_N]
  = (1/N) sum_{t=0}^{N-1} p_t
  = pi + ((1-(1-alpha)^N)/(N alpha)) (p0 - pi).
```

This is an ensemble expectation under a supplied post-record kernel. A realized
history still has integral counts and rational empirical frequencies
`count(w)/|w|`; the realized post-record state is not itself a probability
vector over unrealized alternatives.
Equivalently, the realized post-record state is not itself a probability vector.

## What this unlocks

This gives audit/count lanes a finite transient formula:

```text
supplied stable post-record kernel
  + supplied initial law
  + finite event horizon N
  => exact expected empirical frequency.
```

Rows can use it to compare expected count behavior under a supplied target
kernel against realized post-record counts. Rows still need a supplied
probability model and audit rule to turn deviations into p-values or verdicts.

## What remains outside

This note does not derive:

- the target prior `pi`;
- the reset strength `alpha`;
- the initial law `p0`;
- the transition kernel as physical dynamics;
- a clock, rate, Hamiltonian, action, coupling, Born law, or instrument;
- almost-sure convergence or a concentration bound;
- a generation or Koide dial setting;
- any audit verdict or retained status.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: expected frequencies remain conditional on supplied target, kernel, and initial law
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is an ensemble expected-frequency interface under a supplied kernel, not a derivation of probabilities or audit status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner certificate

The runner verifies:

- source-anchor boundaries in landed post-record count/dynamics notes;
- exact reset-kernel distribution iterates;
- exact finite-N expected empirical frequency formula;
- enumeration/iteration agreement;
- realized counts remain integral while expectations can be fractional;
- different supplied targets give different expected frequencies;
- Record does not derive target, kernel, initial law, concentration, clock/rate,
  Born law, Hamiltonian, or generation/Koide dial.

Run:

```text
python3 scripts/frontier_post_record_stable_kernel_frequency_interface_2026_06_06.py
```
