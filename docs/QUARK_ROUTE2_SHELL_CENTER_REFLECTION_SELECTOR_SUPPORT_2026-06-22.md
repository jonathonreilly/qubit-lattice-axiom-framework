# Quark Route-2 Shell/Center Reflection Selector Support

**Date:** 2026-06-22
**Type:** exact-support / conditional shell-center source-measure selector
**Actual current-surface status:** exact-support for a conditional shell/center reflection selector; not current-surface closure
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_shell_center_reflection_selector_support_2026_06_22.py`](../scripts/frontier_quark_route2_shell_center_reflection_selector_support_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_shell_center_reflection_selector_support_2026_06_22.txt`](../outputs/frontier_quark_route2_shell_center_reflection_selector_support_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block135 shows that four-slot typing plus E/T symmetry leaves a free
shell/center source-measure parameter. What exact additional primitive would
select the canonical `P0` without endpoint input?

## Conditional Selector Theorem

Let

```text
Omega_R = {E-shell, E-center, T-shell, T-center}.
```

Suppose Route-2 supplies a source-measure reflection `tau_sc` such that

```text
tau_sc(E-shell)  = E-center
tau_sc(E-center) = E-shell
tau_sc(T-shell)  = T-center
tau_sc(T-center) = T-shell.
```

If the physical reference `P0` is invariant under `tau_sc` and under E/T
channel exchange, then all four reference weights are forced to be equal:

```text
P0(E-shell) = P0(E-center) = P0(T-shell) = P0(T-center) = 1/4.
```

If the physical shell/center score is `tau_sc`-odd,

```text
s(E-shell) = -1
s(E-center) = +1
s(T-shell) = -1
s(T-center) = +1,
```

then `E_0[s]=0` and `E_0[s^2]=1`. The finite exponential RN path

```text
P_h(omega) = P0(omega) exp(h s(omega)) / Z(h)
```

is therefore a positive normalized unit-score path on the four-slot surface.

## Boundary

This packet does not prove that current Route-2 primitives already supply
`tau_sc` as a physical source-measure symmetry, nor that the `tau_sc`-odd score
is the physical center-ratio covariance readout, nor that it is the same
Fisher-unit Riesz line as the Block121 connected source scalar.

It is a precise sufficient primitive:

```text
Route-2 shell/center reflection source theorem:
construct tau_sc as a physical source-measure automorphism, prove P0 is
tau_sc-invariant, prove the physical center-ratio score is tau_sc-odd, and
identify that score with the Block121 scalar source through a same-source
Fisher-unit Riesz line.
```

No endpoint value is used as an input.

Expected runner result:

```text
TOTAL: PASS=119, FAIL=0
```
