# Quark Route-2 Covariance Score-Lift No-Go

**Date:** 2026-06-22
**Type:** no-go / formal covariance score to physical center-ratio score lift
**Actual current-surface status:** no-go for finite four-slot covariance algebra alone proving the physical center-ratio covariance score
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_covariance_score_lift_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_covariance_score_lift_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_covariance_score_lift_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_covariance_score_lift_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block139 shows that the identity four-slot lift supplies a formal odd
shell/center contrast but not the physical score-lift theorem. Does ordinary
finite covariance algebra identify that contrast as the physical center-ratio
covariance score?

## Formal Covariance Algebra

On the four slots

```text
E-shell, E-center, T-shell, T-center
```

with uniform reference `P0`, let

```text
s(shell) = -1, s(center) = +1.
```

Then `E0[s]=0`, `E0[s^2]=1`, and the normalized exponential path

```text
P_h(omega) = P0(omega) exp(h s(omega)) / Z(h)
```

has RN score `s` at `h=0`. For any four-slot observable `O`,

```text
d/dh E_h[O] |_{h=0} = Cov_0(O, s).
```

In particular, the centered layer observable `O=s` has unit covariance response
`Cov_0(s,s)=1`. This is exact finite probability algebra.

## Boundary

The algebra does not identify which four-slot observable is the physical
Route-2 center-ratio covariance readout. Different observables on the same
formal source path give different covariance responses:

```text
center indicator        -> +1/2
shell indicator         -> -1/2
E-channel indicator     -> 0
center-minus-shell score -> +1
```

Thus the current surface still needs a theorem that names the physical
center-ratio observable and proves its RN score is the odd shell/center
contrast. The source-jet no-go still leaves source coordinates, the partition
functional, raw second moments, one-point products, and same-source
identification missing. The Fisher/Riesz and source-readout isometry packets
still leave same-source unit identification missing.

## Missing Primitive

The exact missing primitive is:

```text
Route-2 physical covariance score-lift theorem:

construct the Route-2 center-ratio observable O_CR on the same source space as
the P_R/E-T readout; construct its normalized source path P_h; prove that
d/dh E_h[O_CR]|0 is the physical center-ratio covariance readout; prove the
RN score d log(dP_h/dP0)/dh|0 is the tau_sc-odd shell/center contrast; and
identify this score as the same-source Fisher-unit Riesz representative of the
Block121 connected scalar.
```

No endpoint value is used as an input.

Expected runner result:

```text
TOTAL: PASS=95, FAIL=0
```
