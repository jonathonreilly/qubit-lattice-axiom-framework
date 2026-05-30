# Axiom-First Coleman-Mermin-Wagner IR-Sum Threshold Packet

**Date:** 2026-04-29 (2026-05-29 scope repair).
**Claim type:** bounded_theorem.
**Status:** bounded-support lattice IR-sum threshold; not a retained
dimensional-minimality theorem.
**Runner:** `scripts/axiom_first_coleman_mermin_wagner_check.py`

## 2026-05-29 Scope Repair

The conditional audit accepted the lattice IR-sum scaling exhibit but rejected
the stronger substrate-minimality theorem. Two bridge pieces were missing:

- Ward/commutator-normalized order-parameter extraction for the
  Mermin-Wagner no-continuous-SSB implication.
- Theorem-grade authority for the D9 long-range-force/kernel-stability
  condition.

This repair removes those bridge pieces from the load-bearing claim. The row
now proves only the finite and asymptotic lattice IR-sum threshold associated
with the Goldstone dispersion. It does not claim `d_s = 3` is derived as the
framework substrate dimension.

No new axiom is introduced. No external physics theorem is used as a
load-bearing premise.

## In-Scope Theorem

For a periodic `L^d` lattice with nonzero momenta

```text
k_mu = 2 pi n_mu / L
```

and lattice dispersion

```text
E_k = 2 sum_mu (1 - cos k_mu),
```

define the finite-volume IR sum

```text
I_d(L) = (1/L^d) sum_{k != 0} 1/E_k.
```

Near `k = 0`, `E_k ~ |k|^2`, so the continuum scaling proxy is

```text
int_{1/L}^{1} r^{d-1} dr / r^2 = int_{1/L}^{1} r^{d-3} dr.
```

Therefore:

- `d = 1`: linear divergence in `L`;
- `d = 2`: logarithmic divergence in `L`;
- `d >= 3`: finite IR behavior in the continuum scaling proxy.

The runner independently computes finite lattice sums for `d in {1,2,3,4}`
and checks that the observed finite-lattice scaling matches this threshold.

## Non-Claims

This row does not prove:

- the order-parameter Ward/commutator normalization needed to turn the IR sum
  into a no-continuous-SSB theorem;
- no spontaneous breaking of continuous symmetries in `d <= 2`;
- existence of symmetry-broken Gibbs states in `d >= 3`;
- the D9 long-range-force/kernel-stability premise;
- `d_s = 3` minimality for the framework substrate;
- electroweak/Higgs compatibility.

Those remain separate bridge problems and are not load-bearing inputs for this
narrowed row.

## Verification

Run:

```bash
python3 scripts/axiom_first_coleman_mermin_wagner_check.py
```

Expected closeout:

```text
IR_SUM_THRESHOLD_PACKET=TRUE
FORMAL_IR_THRESHOLD_D_LE_2_DIVERGES=TRUE
FORMAL_IR_THRESHOLD_D_GE_3_FINITE=TRUE
FINITE_LATTICE_SCALING_CHECKS_PASS=TRUE
D3_MINIMALITY_CLAIMED=FALSE
ORDER_PARAMETER_WARD_NORMALIZATION_PROVEN=FALSE
D9_KERNEL_AUTHORITY_LOAD_BEARING=FALSE
ACTUAL_CURRENT_SURFACE_STATUS=BOUNDED_SUPPORT
```
