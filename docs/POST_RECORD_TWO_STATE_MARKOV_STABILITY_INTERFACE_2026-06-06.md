# Post-Record Two-State Markov Stability Interface

**Date:** 2026-06-06
**Type:** exact conditional dynamics interface
**Claim type:** bounded_theorem
**Status:** exact-support branch-local for supplied two-state post-record Markov
stability; kernel, physical score source, clock/rate, and dial selection remain
open; audit_required_before_effective_retained=true;
bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_two_state_markov_stability_interface_2026_06_06.py`](../scripts/frontier_post_record_two_state_markov_stability_interface_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_two_state_markov_stability_interface_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_two_state_markov_stability_interface_2026_06_06.txt)

## Result

For a supplied two-state post-record transition kernel

```text
K(a,b) = [[1-a, a],
          [b, 1-b]],
```

with `0 < a < 1`, `0 < b < 1`, the stationary row vector is

```text
pi = (b/(a+b), a/(a+b)).
```

For any row probability vector `p=(x,1-x)`,

```text
(pK)_0 - pi_0 = (1-a-b) (p_0 - pi_0).
```

Thus, when `|1-a-b| < 1`, the supplied kernel has an attracting stable
post-record location. The equal-letter case is the symmetric subcase `a=b`,
where `pi=(1/2,1/2)`.

This is a stability interface, not a dial-selection theorem. Different supplied
kernels on the same two record atoms have different stationary locations. The
kernel, the physical reason for that kernel, and any mapping from stationary
prior to a generation/Koide dial remain separate premises.

## What this unlocks

This gives dynamics lanes a reusable finite grammar:

```text
post-record two-state alphabet
  + supplied transition kernel K(a,b)
  + |1-a-b| < 1
  => exact stable stationary location pi.
```

It supports claims of the form "this supplied post-record dynamics has a stable
location." It does not support claims of the form "Record chose this dynamics."

## Relation to equal-letter stability

The landed equal-letter theorem studies a post-record atom-symmetric reset map
and obtains the stable point `(1/2,1/2)`. This note shows the surrounding
two-state interface:

- `a=b` gives the equal-letter stable location;
- `a != b` gives a biased stable location;
- stability is a property of the supplied kernel;
- choosing which kernel is physical remains a dynamics/bridge problem.

## What remains outside

This note does not derive:

- the transition kernel;
- the physical carrier dynamics that produces the kernel;
- a clock, rate, Hamiltonian, action, or coupling;
- Born weights or an instrument;
- a physical score or selection rule for choosing among kernels;
- a generation or Koide dial setting;
- any audit verdict or retained status.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: stable post-record location remains conditional on a supplied two-state kernel and its physical bridge
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a supplied-kernel stability interface, not a derivation of the kernel or a dial setting."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner certificate

The runner verifies:

- source-anchor boundaries in the record dynamics and prior-stability notes;
- row-stochasticity of supplied two-state kernels;
- exact stationary vectors;
- exact one-step deviation contraction by `1-a-b`;
- multi-step contraction by powers of `1-a-b`;
- equal-letter symmetric subcase;
- different supplied kernels give different stable locations;
- Record does not derive the kernel, physical bridge, clock/rate, Born law,
  Hamiltonian, or generation/Koide dial.

Run:

```text
python3 scripts/frontier_post_record_two_state_markov_stability_interface_2026_06_06.py
```
