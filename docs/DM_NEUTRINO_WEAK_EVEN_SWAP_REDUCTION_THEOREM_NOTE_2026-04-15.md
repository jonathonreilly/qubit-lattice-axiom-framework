# DM Neutrino Weak Even Swap-Reduction Theorem

**Type:** bounded_theorem
**Date:** 2026-04-15  
**Status:** support - structural or confirmatory support note
transfer leg  
**Script:** `scripts/frontier_dm_neutrino_weak_even_swap_reduction_theorem.py`

## Framework sentence

In this note, “axiom” means only the single framework axiom `Cl(3)` on `Z^3`.
This is historical terminology. The calculation below separately assumes
a swap-invariant linear readout; this premise is not derived from carrier
closure or from the current framework axioms.

## Question

Once the odd leg is closed as

- `gamma = c_odd a_sel`
- `c_odd = +1`,

does the exact current weak source carrier already reduce the remaining even
law beyond a generic `2 x 2` matrix

- `[E1, E2]^T = M_even [tau_E, tau_T]^T`?

## Bottom line

Only with the supplied invariant-readout premise.

The exact weak tensor carrier

`K_R(q) = [[u_E(q), u_T(q)], [delta_A1(q)u_E(q), delta_A1(q)u_T(q)]]`

is closed under source-column swap and carries no exact `E/T`-distinguishing
datum on the current single-axiom stack.

If a linear readout is additionally required to be invariant under the
source-column swap, it descends to the swap quotient. Under that supplied
readout premise, the fixed-point equation forces

`M_even = [[v_1, v_1], [v_2, v_2]] = v_even [1, 1]`

for one real target vector

`v_even = (v_1, v_2)^T`.

Equivalently:

`[E1, E2]^T = v_even (tau_E + tau_T)`.

Within the supplied invariant-readout class the remaining object is the
two-real vector `v_even`; the generic readout problem remains four-real.

## Exact source-side reason

The exact weak carrier is the bilinear support object

`K_R(q) = [1, delta_A1(q)]^T [u_E(q), u_T(q)]`.

Its column swap is internal:

`K_R(q) P_ET = K_R(delta_A1(q), u_T(q), u_E(q))`

with

`P_ET = [[0,1],[1,0]]`.

So the exact current source family is closed under `E/T` exchange.

Family closure does not imply that a readout is invariant. For example,
`M_even=I_2` is a linear readout on this labeled carrier, but
`I_2 P_ET != I_2`. We separately impose the readout-invariance premise

`M_even = M_even P_ET`.

Solving this fixed-point condition gives exactly

`M_even = [[v_1, v_1], [v_2, v_2]]`.

## Equivalent factorization

The antisymmetric source mode

`tau_- = tau_E - tau_T`

lies in the exact kernel:

`M_even [1,-1]^T = 0`.

So only the symmetric source combination survives:

`tau_+ = tau_E + tau_T`.

Then the exact current even law is simply

`[E1, E2]^T = v_even tau_+`.

This reduces the coefficient count from four to two only under the supplied
swap-invariance condition.

## Why this does not contradict the old Route-2 staging tools

The old two-channel source-side objects

- `Theta_R^(0)(q) = (gamma_E(q), gamma_T(q))`
- `Xi_R^(0) = d Theta_R^(0) / d delta_A1`

do distinguish `E` and `T`.

But both are already recorded as **bounded**, not exact.

So they do not yet supply an exact single-axiom `E/T`-distinguishing readout.
They remain staging tools, not theorem-grade coefficient laws.

## Conditional reduction and open premise

Given `M_even P_ET=M_even`, the matrix has equal columns and rank at most
one (rank zero when v_even=0). The coefficient problem then has two real
parameters. Without that readout-invariance premise a generic real 2x2
linear map still has four parameters. Source-family closure alone does not
remove them, nor does it select the values of v_1 or v_2.

## Benchmark consequence

This sharpening originally used the following historical, prerepair benchmark
(not the current direct-ODE result; see the branch table in
`DM_LEPTOGENESIS_TRANSPORT_STATUS_NOTE_2026-04-16.md`):

- `eta = 1.81e-10`
- `eta / eta_obs ~= 0.30`

That historical benchmark was bounded because `v_even` is still not fixed, even though
the odd normalization is now closed and the even transfer shape is reduced.

## Command

```bash
python3 scripts/frontier_dm_neutrino_weak_even_swap_reduction_theorem.py
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [s3_time_bilinear_tensor_primitive_note](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md)
- [s3_time_tensor_primitive_prototype_note](S3_TIME_TENSOR_PRIMITIVE_PROTOTYPE_NOTE.md)
- [s3_time_constructed_support_tensor_primitive_note](S3_TIME_CONSTRUCTED_SUPPORT_TENSOR_PRIMITIVE_NOTE.md)
