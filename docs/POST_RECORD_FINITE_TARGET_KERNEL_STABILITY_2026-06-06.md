# Post-Record Finite Target-Kernel Stability

**Date:** 2026-06-06
**Type:** exact conditional dynamics interface
**Claim type:** bounded_theorem
**Status:** exact-support branch-local for supplied finite target-kernel
stability; target prior, alpha, physical kernel source, and dial selection remain
open; audit_required_before_effective_retained=true;
bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_finite_target_kernel_stability_2026_06_06.py`](../scripts/frontier_post_record_finite_target_kernel_stability_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_finite_target_kernel_stability_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_finite_target_kernel_stability_2026_06_06.txt)

## Result

For a finite post-record alphabet `O`, a supplied target prior `pi` on `O`, and
`0 < alpha < 1`, define the reset/thermalizing kernel

```text
K_{pi,alpha}(i,j) = (1-alpha) delta_ij + alpha pi_j.
```

Then:

```text
pi K_{pi,alpha} = pi
```

and for every row probability vector `p`,

```text
p K_{pi,alpha} - pi = (1-alpha)(p - pi).
```

So the supplied target prior is stationary and linearly attracting. The kernel
also satisfies detailed balance with `pi`.

This is the finite target-stability interface. It proves that once a target
prior is supplied, a simple post-record information kernel can make that target
stable. It does not derive the target prior, the physical source of the kernel,
or a generation/Koide dial setting.

## Dynamics implication

Stability is not selection. Every supplied target prior can be made stable by
this finite kernel family. Therefore any downstream claim that a dial location
is stable must still say where the target prior or kernel came from.

The valid grammar is:

```text
finite post-record alphabet
  + supplied target prior pi
  + supplied reset strength alpha
  => exact stable post-record kernel K_{pi,alpha}.
```

The invalid grammar is:

```text
finite post-record alphabet
  + stability
  => physical target prior / dial.
```

## What remains outside

This note does not derive:

- the target prior `pi`;
- the reset strength `alpha`;
- a physical carrier dynamics producing the reset kernel;
- a clock, rate, Hamiltonian, action, or coupling;
- Born weights or an instrument;
- a selection rule among possible target priors;
- a generation or Koide dial setting;
- any audit verdict or retained status.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: stable target-kernel dynamics remains conditional on supplied target prior and reset strength
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a supplied-target stability interface, not a derivation of the target prior or a dial setting."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner certificate

The runner verifies:

- source-anchor boundaries in the landed stability/dynamics notes;
- target prior normalization;
- row-stochasticity of `K_{pi,alpha}`;
- exact stationarity;
- exact detailed balance;
- exact vector contraction by `1-alpha`;
- multiple supplied target priors have their own stable kernels;
- Record does not derive the target prior, alpha, physical bridge, clock/rate,
  Born law, Hamiltonian, or generation/Koide dial.

Run:

```text
python3 scripts/frontier_post_record_finite_target_kernel_stability_2026_06_06.py
```
