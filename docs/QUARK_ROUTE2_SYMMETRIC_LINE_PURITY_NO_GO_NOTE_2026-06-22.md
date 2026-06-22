# Quark Route-2 Symmetric Line Purity No-Go

**Date:** 2026-06-22
**Type:** no-go / E/T-symmetric singlet purity obstruction packet
**Actual current-surface status:** no-go for E/T symmetry alone proving the symmetric line is pure disconnected
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_symmetric_line_purity_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_symmetric_line_purity_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_symmetric_line_purity_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_symmetric_line_purity_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block93 gives a sufficient source-Hessian bridge if the E/T-symmetric line is
a pure factorizable disconnected singlet. Does E/T symmetry alone prove that
purity premise?

## Result

No. E/T parity is a statement about the two output channels. Disconnectedness
is a statement about same-source factorization. They are independent gates.

Write the symmetric E/T contribution as

```text
S_total = d S_ET + eta S_ET
S_ET = (1,1)
```

where `d S_ET` is factorizable disconnected and `eta S_ET` is a connected
singlet residue. Both terms are E/T-symmetric. The connected source Hessian
subtracts only the factorizable disconnected term:

```text
D^2 log Z:  d S_ET + eta S_ET  ->  eta S_ET.
```

Thus `kappa=0` follows only when `eta=0`, i.e. when the symmetric E/T line is
proved pure disconnected for the same source/readout. E/T symmetry alone still
allows connected symmetric residue.

## Missing Primitive

The exact missing primitive is:

```text
Route-2 symmetric-line pure-disconnected typing theorem:

for the same-source physical E/T source-Hessian readout, prove every
E/T-symmetric singlet contribution is factorizable disconnected and has no
connected singlet residue, using framework primitives rather than endpoint
input.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=67, FAIL=0
```
