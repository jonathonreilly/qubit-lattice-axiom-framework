# Quark Route-2 Binary Exponential Source-Jet Support

**Date:** 2026-06-22
**Type:** exact-support / formal binary source-jet connected-cumulant theorem
**Actual current-surface status:** exact-support for a formal binary source-jet cumulant theorem; not current-surface closure
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_binary_exp_source_jet_support_2026_06_22.py`](../scripts/frontier_quark_route2_binary_exp_source_jet_support_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_binary_exp_source_jet_support_2026_06_22.txt`](../outputs/frontier_quark_route2_binary_exp_source_jet_support_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block142 pruned the shortcut from finite `P_R` rows to a physical `O_CR`
source observable. The next constructive target is source-jet typing:

```text
Can a typed source/readout theorem force kappa = 0 by connected-cumulant
subtraction, without importing the endpoint value?
```

## Exact Binary Source-Jet Model

Let the formal source variable `X_CR` have two outcomes:

```text
X_CR = +1 with probability 2/3,
X_CR = -1 with probability 1/3.
```

Define the source-coupled partition functional

```text
Z_CR[J] = (2/3) exp(J) + (1/3) exp(-J).
```

At zero source:

```text
Z_CR[0] = 1,
D Z_CR |0 = 1/3,
D^2 Z_CR |0 = 1.
```

Therefore

```text
D^2 log Z_CR |0 = D^2 Z_CR |0 - (D Z_CR |0)^2
                = 1 - 1/9
                = 8/9.
```

On the selector line

```text
R_phys(kappa) = 8/9 + kappa / 9,
```

this exact source jet forces

```text
D^2 log Z_CR |0 = 8/9.
```

Therefore it forces

```text
kappa = 0.
```

No endpoint value is used as an input.

## What This Retires

This block retires a narrow technical objection against the source-jet route:
there is an explicit finite exponential source model whose same-source
one-point product is exactly the `1/9` disconnected term and whose connected
Hessian is exactly `8/9`.

It also confirms that the disconnected subtraction must be same-source. If the
raw second jet `D^2 Z |0 = 1` is paired with a different one-point value, the
connected output changes. The source coordinate and one-point product cannot
be treated as separate untyped readouts.

## Remaining Physical Imports

The packet is not a current-surface derivation of the Route-2 endpoint bridge.
The remaining primitive is:

```text
Route-2 physical binary source-jet theorem:

construct the physical Route-2 source coordinate J_CR and prove that the
physical O_CR/readout line is this same-source connected Hessian D^2 log Z_CR;
prove the Route-2 singlet line is the pure disconnected product (D Z_CR)^2;
then prove the source-readout unit isometry and orientation sign needed to map
the connected source fraction to c_TE.
```

With those additional physical typing clauses and `sigma = -1`, the theorem
would give

```text
c_TE = sigma * 1 * (8/9) = -8/9.
```

This last line is a conditional consequence of the typed source/readout and
orientation theorem. It is not imported from the endpoint value.

Expected runner result:

```text
TOTAL: PASS=95, FAIL=0
```
