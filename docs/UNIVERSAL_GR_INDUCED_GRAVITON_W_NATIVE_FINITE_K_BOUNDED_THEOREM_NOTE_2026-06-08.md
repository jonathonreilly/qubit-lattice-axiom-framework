# Finite-k yz TT Bubble Sign Diagnostic for the Native Elliptic Dirac Operator

**Date:** 2026-06-08
**Claim type:** bounded_theorem / finite-Brillouin-zone source certificate
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_universal_gr_induced_graviton_w_native_finite_k.py`](../scripts/frontier_universal_gr_induced_graviton_w_native_finite_k.py)
**Runner cache:** [`logs/runner-cache/frontier_universal_gr_induced_graviton_w_native_finite_k.txt`](../logs/runner-cache/frontier_universal_gr_induced_graviton_w_native_finite_k.txt)

## 2026-06-08 Audit-Boundary Repair

This repair narrows the row to the source packet that is actually computed. The
runner checks a finite-`k`, `yz` transverse-traceless bubble diagnostic for the
native elliptic anti-Hermitian lattice Dirac operator:

```text
D(q) = i (sigma_x sin q_x + sigma_y sin q_y + sigma_z sin q_z) + m I.
```

The packet does **not** prove that the `yz` vertex is the complete finite-`k`
metric-source Hessian of `W=log|det(D+J)|`. It also does **not** prove the full
diffeomorphism Ward identity, the `E_g/T_2g` spin-2 isotropy continuum limit, or
a physical induced-graviton dispersion law.

The auditable claim is narrower:

> In the runner-defined `yz` TT channel, the native elliptic operator gives a
> positive, convergent, mass-robust `k^2` bubble slope, while the non-elliptic
> bare-Hermitian control gives a negative, N-divergent slope.

This keeps the useful science: finite momentum changes the sign diagnostic
relative to the `k=0` no-go probes. It does not close the full GR bridge.

## Theorem (Bounded Finite-BZ Diagnostic)

- **T1:** the native anti-Hermitian `iD` is elliptic:
  `det(iD+m)=m^2+|sin q|^2>0` on all tested BZ modes. The bare-Hermitian
  `sigma.sin` control has sign-indefinite determinant and is not a valid
  partition-function surrogate in this diagnostic.
- **T2:** the `yz` channel with momentum along `x` is transverse-traceless by
  construction: `k^i h_ij=0` and `tr h=0`.
- **T3:** on the native elliptic operator, the `yz` TT `k^2` slope is positive
  and stable over the tested BZ sizes.
- **T4:** the sign is robust for `m in {0.5,1.0,1.5,2.0}`; the tested trace
  channel has the opposite sign.
- **T5:** the non-elliptic bare-Hermitian control gives a negative, N-divergent
  slope.

`TOTAL: PASS=8 FAIL=0`.

## What This Establishes

The row establishes bounded finite-scheme support for a positive native
elliptic `yz` TT bubble slope at finite momentum. It also records a useful
control: changing to the non-elliptic bare-Hermitian operator flips the behavior
to a negative, divergent diagnostic.

This is a real upstream clue for universal GR: the `k=0` homogeneous-metric
obstructions do not by themselves decide every finite-momentum stress-bubble
sign. The result is still only a channel diagnostic until the missing bridges
are supplied.

## What Remains Open

- Full finite-`k` metric-source Hessian of `W`, including all contact terms.
- Full symmetric stress vertex and diffeomorphism Ward identity.
- `E_g/T_2g` spin-2 isotropy continuum limit.
- Induced Newton magnitude and physical dispersion normalization.
- Chiral limit control.

## Relation to Inventory

The native elliptic generator is supported by the retained-bounded
CPT/real-anti-Hermitian Dirac surface. The `k=0` scalar-kernel and degenerate
supermetric no-go rows remain valid at their stated scope. This row supplies a
finite-momentum diagnostic that can be tested against the later full stress
vertex, not a replacement for that bridge.

## Honest Auditor Read

The source is bounded and channel-scoped. The runner constructs the finite-BZ
operator and `yz` vertex, computes the bubble slopes, checks convergence and
mass robustness, compares the trace channel sign, and reproduces the
non-elliptic negative control. It does not ask the audit lane to accept a
physical spin-2 graviton, a complete W metric Hessian, or full GR closure from
this packet alone.
