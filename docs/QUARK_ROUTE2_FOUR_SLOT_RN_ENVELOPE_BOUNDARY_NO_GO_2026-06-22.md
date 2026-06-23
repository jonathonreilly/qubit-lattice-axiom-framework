# Quark Route-2 Four-Slot RN Envelope Boundary No-Go

**Date:** 2026-06-22
**Type:** no-go / formal four-slot RN envelope boundary
**Actual current-surface status:** no-go for a formal four-slot RN envelope alone instantiating the physical Route-2 probability surface
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_four_slot_rn_envelope_boundary_2026_06_22.py`](../scripts/frontier_quark_route2_four_slot_rn_envelope_boundary_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_four_slot_rn_envelope_boundary_2026_06_22.txt`](../outputs/frontier_quark_route2_four_slot_rn_envelope_boundary_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block133 names the four-slot shell/center probability-surface target:

```text
Omega_R = {E-shell, E-center, T-shell, T-center}
+ P0 + P_h + RN coordinate functions
```

Can the current Route-2 surface construct enough of this target to close the
probability-surface gate?

## Formal Envelope

A formal finite RN envelope can be written without endpoint input.

Let

```text
Omega_R = {E-shell, E-center, T-shell, T-center}
P0(E-shell) = P0(E-center) = P0(T-shell) = P0(T-center) = 1/4
```

and let the shell/center contrast be

```text
s(E-shell) = -1
s(E-center) = +1
s(T-shell) = -1
s(T-center) = +1.
```

Then `E_0[s]=0` and `E_0[s^2]=1`. The finite exponential path

```text
P_h(omega) = P0(omega) exp(h s(omega)) / Z(h)
```

is positive, normalized, and satisfies `P_h << P0`. The four indicator
functions separate the four gamma-coordinate slots.

So a formal envelope with `Omega_R`, a positive reference, an RN path, and
slot coordinate functionals exists as abstract finite probability geometry.

## Boundary

The formal envelope is not yet the physical Route-2 probability surface.
Nothing in the current Route-2 primitives selects this `P0`, this score line,
or the Fisher-unit Riesz identification with the Block121 connected source.

The obstruction is not the existence of a finite probability model. The
obstruction is the missing canonical source/readout bridge:

```text
Route-2 shell/center source-measure primitive:
construct the physical P0 on the four shell/center slots, construct the RN
score whose covariance readout is the physical center-ratio scalar line, and
prove that this line and the Block121 connected source scalar are the same
Fisher-unit Riesz line.
```

Without that primitive, the same formal slot labels admit multiple positive
references and score normalizations. For example, the same raw shell/center
contrast has Fisher norm square `1` under the uniform reference but `8/9`
under the center-heavy reference

```text
(1/6, 1/3, 1/6, 1/3).
```

Thus the formal envelope does not force `mu=1`; it only narrows the missing
primitive to canonical `P0`, physical center-ratio covariance, and same-source
Fisher-unit Riesz identification.

No endpoint value is used as an input.

Expected runner result:

```text
TOTAL: PASS=91, FAIL=0
```
