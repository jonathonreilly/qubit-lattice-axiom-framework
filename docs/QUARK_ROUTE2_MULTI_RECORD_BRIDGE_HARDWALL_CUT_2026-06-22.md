# Quark Route-2 Multi-Record Bridge Hard-Wall Cut

**Date:** 2026-06-22
**Type:** no-go / hard-wall cut certificate for the multi-record bridge
**Actual current-surface status:** no-go for the current available support stack alone closing `R_conn -> c_TE=-8/9`
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_multi_record_bridge_hardwall_cut_2026_06_22.py`](../scripts/frontier_quark_route2_multi_record_bridge_hardwall_cut_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_multi_record_bridge_hardwall_cut_2026_06_22.txt`](../outputs/frontier_quark_route2_multi_record_bridge_hardwall_cut_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Result

Blocks115-118 leave a precise hard-wall cut for the Route-2 cross-domain
bridge. The following clauses are exact support:

```text
orientation-free linear adjoint-Hessian contraction is inverse Killing up to scale;
endpoint orientation supplies the negative sign conditionally;
connected-cumulant algebra subtracts factorizable products exactly.
```

The current surface still does not supply the same-source physical theorem
needed to consume those supports. The exact remaining primitive is:

```text
Route-2 same-source covariant multi-record bridge theorem:

construct covariant adjoint records X_A for the physical Route-2 E/T source;
prove the physical readout is D_A D_B log Z for that same source;
prove the identity-line contribution is pure disconnected,
  D_0 D_0 Z = (D_0 Z)^2;
fix the adjoint/singlet coefficient normalization with equal unit weights;
and identify the resulting scalar output with the Route-2 E/T center-ratio
  magnitude readout.
```

With that theorem plus the already separated endpoint-orientation sign support:

```text
kappa = 0
R_phys = 8/9
sigma = -1
c_TE = -8/9.
```

Without that theorem, the current support stack reaches only the missing
primitive node. It does not derive the endpoint triple and does not close the
current Route-2 bridge.

## Why The Cut Is Hard

The remaining clauses are independent:

1. **Source/readout existence.** Current `K_R -> P_R` gives finite readout
   slots, not a same-source covariant adjoint source Hessian.
2. **Identity factorization.** Invariance and cumulants allow a singlet
   residual `eta`; only a same-source factorization theorem sets `eta=0`.
3. **Coefficient normalization.** SU(3) invariance allows independent singlet
   and adjoint invariant contractions; equal unit weight is a physical
   source/readout normalization theorem.
4. **Endpoint magnitude typing.** The negative sign is separately supported,
   but the magnitude still has to be typed from the connected selector into
   the Route-2 center-ratio readout.

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=64, FAIL=0
```
