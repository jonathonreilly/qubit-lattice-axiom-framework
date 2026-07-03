# Post-Record Transition-Kernel Interface

**Date:** 2026-06-06
**Type:** exact conditional interface
**Claim type:** bounded_theorem
**Status:** exact-support branch-local for the supplied-kernel interface;
transition-kernel derivation remains open; audit_required_before_effective_retained=true;
bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_transition_kernel_interface_2026_06_06.py`](../scripts/frontier_post_record_transition_kernel_interface_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_transition_kernel_interface_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_transition_kernel_interface_2026_06_06.txt)

## Result

The exact post-record layer supplies realized words and counts. If a finite
transition kernel is supplied on the record alphabet, that kernel has a clean
interface with the append/count layer.

For a finite alphabet `O`, an initial law `mu_0` on `O`, and a row-stochastic
kernel

```text
K(o,o') = Pr(next=o' | current=o),
```

the probability of a finite history is

```text
Pr(o_0 ... o_n)
  = mu_0(o_0) * K(o_0,o_1) * ... * K(o_{n-1},o_n).
```

For a realized history `w` ending in `o`, the one-step ensemble expectation of
the count vector is

```text
E[count(w next) | w] = count(w) + K(o,-).
```

The realized update remains integral:

```text
count(w o') = count(w) + e_{o'}.
```

The fractional vector is an ensemble expectation conditional on the supplied
kernel, not the post-record state itself.

## What this unlocks

This gives conditional dynamics lanes a precise grammar:

```text
post-record append/count algebra
  + supplied transition kernel
  => finite-history probabilities and expected count dynamics.
```

Rows can cite this when they already have a justified stochastic kernel,
instrument law, or empirical transition model. Rows that need the kernel
itself still need a separate bridge.

## What remains outside

This note does not derive:

- the transition kernel;
- the Markov property or stationarity;
- record-production dynamics;
- Born weights or an instrument;
- a clock/time metric or transition rate;
- a Hamiltonian/action/coupling;
- a generation or Koide dial setting.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: physical stochastic dynamics remains conditional on a supplied kernel
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a supplied-kernel interface, not a derivation of the kernel or a status promotion proposal."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner certificate

The runner verifies:

- source-anchor boundaries in the post-record count/history and dynamics notes;
- supplied kernels are row-stochastic finite objects;
- finite-history probabilities normalize over fixed length;
- expected counts computed by enumeration match the Markov recursion;
- conditional next-count expectation equals realized count plus the current
  row of the supplied kernel;
- realized updates remain integral while expectations can be fractional;
- different supplied kernels give different predictions for the same realized
  history;
- Record does not supply the kernel, clock, rate, Born law, Hamiltonian, or
  generation/Koide dial.

Run:

```text
python3 scripts/frontier_post_record_transition_kernel_interface_2026_06_06.py
```
