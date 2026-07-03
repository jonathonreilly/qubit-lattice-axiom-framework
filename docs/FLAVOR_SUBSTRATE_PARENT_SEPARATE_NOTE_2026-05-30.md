# Flavor Substrate Parent Separate Boundary

**Date:** 2026-05-30
**Updated:** 2026-06-07
**Claim type:** bounded_theorem
**Claim boundary:** finite tensor/parity boundary under a supplied `Z_2`
spin-factor reading. The note does not prove an "only way" folding theorem and
does not decide whether `diag(1,omega)` is native inside complex `M_2(C)`.
Those are left as the det_C / carrier-native bridge.
**Runner:** `scripts/flavor_substrate_parent_separate_2026_05_30.py`
(SCORECARD PASS=5 FAIL=0).

## Scope

The supplied test surface is a lifted two-factor carrier:

```text
M_2(C) tensor generation-C_3.
```

The grading used in the calculation is coin-blind:

```text
I_2 tensor Gamma_chi.
```

The tested parent ansatz is

```text
K = I_2 tensor G_U1 + sigma_x tensor H_chi.
```

This note proves what happens on that supplied surface. It does not classify
all possible complex `M_2(C)` embeddings or all possible parent operators.

## Result 1: The Naive Lift Splits

Under the coin-blind grading, the even/odd projection of `K` is forced:

```text
K_even = I_2 tensor G_U1,
K_odd  = sigma_x tensor H_chi.
```

So the lift is a super-direct-sum, not an indecomposable parent that unifies
the value generator and the chiral operator.

Equivalently, the value operator remains in the commuting/on-block sector, and
the chiral operator remains in the anticommuting/off-block sector.

## Result 2: The C3-Equivariant Native Singlet Reaches Only The Value Side

With the qubit factor treated as a `C_3` singlet, the on-block image is the
circulant generation algebra. The value generator is reachable in that
surface; the `Gamma_chi`-anticommuting operator is not.

This is a finite statement about the supplied tensor surface. It is not a
global no-go for every possible complex parent.

## Result 3: The Rehab Channel Requires An Order-3 Qubit Charge

The explicit two-dimensional charge

```text
diag(1, omega)
```

has order `3` and determinant `omega`. In the supplied `Z_2` spin-factor
reading it is not a `Z_2` charge. It is the same order-3 complex phase
structure that the det_C value route asks about.

This branch does not decide whether that phase should be called native in the
full complex `M_2(C)` algebra. The honest statement is narrower:

```text
on the supplied Z_2 spin-factor reading, unification requires an extra
order-3 complex charge.
```

## Corrected Interpretation

The value and chirality lanes are separate on the tested lift:

```text
value side:     C_3-equivariant / commuting / on-block
chirality side: orbit-splitting / anticommuting / off-block
```

They are connected only by the open det_C / order-3 complex-charge bridge. So
the corrected picture is not "one gate" and not a proved "one root import."
It is:

```text
the naive native lift does not unify them;
an order-3 complex charge would be needed on this route;
the native status of that charge remains the open det_C bridge.
```

## Bottom Line

The finite tensor calculation is retained as bounded support for route
pruning. The unproven parts are removed from the claim surface:

- no "only way" folding theorem;
- no proof that `diag(1,omega)` is non-native in all of `M_2(C)`;
- no claim that value and chirality have a closed common root.

The remaining science target is the det_C / order-3 carrier-native bridge.
