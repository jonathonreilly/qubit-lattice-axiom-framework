# Post-Record Stable-Kernel Count Audit Interface

**Date:** 2026-06-06
**Type:** exact conditional audit interface
**Claim type:** bounded_theorem
**Status:** exact-support branch-local for exact finite count-statistic audits
under a supplied post-record kernel; kernel, statistic, threshold, physical
clock, and audit verdict remain open; audit_required_before_effective_retained=true;
bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_stable_kernel_count_audit_interface_2026_06_06.py`](../scripts/frontier_post_record_stable_kernel_count_audit_interface_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_stable_kernel_count_audit_interface_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_stable_kernel_count_audit_interface_2026_06_06.txt)

## Result

For a finite post-record alphabet `O`, supplied initial law `p0`, supplied
transition kernel `K`, and finite horizon `N`, every word

```text
w = o_0 ... o_{N-1}
```

has exact supplied-null probability

```text
P(w) = p0(o_0) K(o_0,o_1) ... K(o_{N-2},o_{N-1}).
```

Therefore any finite count statistic

```text
T(count(w))
```

has an exact finite null distribution by summing over `O^N`. For an observed
word `w*`, the one-sided exact p-value is

```text
P(T(count(W)) >= T(count(w*))).
```

This gives stable-kernel audit lanes exact finite calibration without importing
asymptotic concentration. The kernel, statistic, tail direction, and threshold
are still supplied inputs.

Source-anchor phrase: without importing asymptotic concentration.

## What this unlocks

This connects the supplied stable-kernel dynamics layer to audit/count lanes:

```text
supplied finite post-record kernel
  + finite count statistic
  + observed finite word
  => exact finite p-value under that supplied kernel.
```

It is useful for finite-horizon checks of realized count deviations. It does
not apply an audit verdict or infer the physical kernel.

## What remains outside

This note does not derive:

- the kernel or initial law;
- the statistic, threshold, or tail direction;
- a concentration inequality or asymptotic limit theorem;
- a physical clock or transition rate;
- Born weights, an instrument, Hamiltonian, action, or coupling;
- a generation or Koide dial setting;
- any audit verdict or retained status.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: finite count audit remains conditional on supplied kernel, statistic, threshold, and observed word
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is an exact finite audit calculation under a supplied kernel, not a derivation of the kernel or an audit verdict."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner certificate

The runner verifies:

- source-anchor boundaries in landed post-record count/dynamics notes;
- supplied kernel row-stochasticity;
- exact finite word probabilities normalize;
- count distribution is obtained by exact summation over words;
- expected counts from the count distribution match direct time-marginal sums;
- exact count-statistic p-values are conservative by enumeration;
- realized counts remain integral;
- Record does not derive the kernel, statistic, threshold, concentration,
  clock/rate, Born law, Hamiltonian, or generation/Koide dial.

Run:

```text
python3 scripts/frontier_post_record_stable_kernel_count_audit_interface_2026_06_06.py
```
