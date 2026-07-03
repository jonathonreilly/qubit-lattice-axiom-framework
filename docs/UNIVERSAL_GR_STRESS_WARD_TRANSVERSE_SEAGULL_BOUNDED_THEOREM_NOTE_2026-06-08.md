# Runner-Defined Stress Ward Scheme: Conserved Vertex plus Local Seagull Gives a Leading-Order Transverse Finite-BZ Graviton Diagnostic

**Date:** 2026-06-08
**Claim type:** bounded_theorem / runner-defined finite-Brillouin-zone source
certificate
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_universal_gr_stress_ward_transverse_seagull.py`](../scripts/frontier_universal_gr_stress_ward_transverse_seagull.py)
**Runner cache:** [`logs/runner-cache/frontier_universal_gr_stress_ward_transverse_seagull.txt`](../logs/runner-cache/frontier_universal_gr_stress_ward_transverse_seagull.txt)

## 2026-06-08 Audit-Boundary Repair

This repair narrows the source claim to the artifact that is actually derived
and computed in the restricted packet.

The runner certifies a finite-BZ, runner-defined stress-vertex scheme:

```text
D(q) = i (sigma_x sin q_x + sigma_y sin q_y + sigma_z sin q_z) + m I,
V_cons,cd(q,k) = i/2 [sigma_c cos(q_c+k_c/2) sbar_d + c <-> d],
S = -B0 + B1 + B5
```

where `B0`, `B1`, and `B5` are the explicit local contact basis terms in the
runner. It does **not** prove that this `V_cons` and `S` are the complete metric
Hessian vertices of the full `W=log|det(D+J)|` functional. It also does **not**
prove an exact-all-`k` no-go over every possible local seagull class.

The open bridge for any downstream W-native graviton claim is therefore:

1. derive the full finite-`k` metric-source Hessian/stress vertex of `W`,
   including all contact terms, in the same normalization;
2. prove the continuum Ward/isotropy limit for that derived vertex; and
3. only then identify the runner-defined positive TT sign with a physical
   spin-2 graviton stiffness.

This note supplies bounded source support for the finite scheme above. It is not
a retained or unbounded GR closure.

## Summary

The earlier `universal_gr_induced_graviton_w_native_finite_k` row checked a
`yz` transverse-traceless channel at finite `k`. That channel is transverse by
construction and therefore does not test a full longitudinal Ward residual.
This note tests a larger, explicitly defined lattice stress scheme:

- an exact internal U(1) lattice Ward identity is used as the machinery
  baseline;
- the naive symmetric stress extension fails longitudinal transversality;
- the conserved velocity-times-momentum vertex `V_cons` leaves an `O(k0)`
  longitudinal residual;
- the local contact term `S=-B0+B1+B5` cancels the leading contact, leaving
  `O(k0^3)` residuals in the tested channels; and
- the positive `yz` TT stiffness remains positive for the tested masses.

The new runner check `T6b` solves the small-`k` local contact matching problem in
the chosen `{B0,B1,B5}` basis and recovers coefficients close to
`(-1,+1,+1)`, with the remaining mismatch at the same finite-`k` scale already
reported by `T6`. This makes the seagull a recoverable contact-basis result
inside the runner-defined scheme rather than a purely printed assertion.

## Theorem (Bounded Finite-BZ Scheme)

For the native elliptic `2x2` lattice Dirac operator and the runner-defined
`V_cons` plus `S=-B0+B1+B5` contact term, the finite Brillouin-zone computation
has the following checked properties:

- **T1:** native `iD` is elliptic: `det=m^2+|sin q|^2>0` on all tested BZ modes;
  the bare-Hermitian control is sign-indefinite.
- **T2:** the exact internal U(1) lattice Ward identity is reproduced to
  numerical precision, validating the bubble/seagull and `2 sin(k/2)` machinery
  on an exact internal symmetry.
- **T3:** the naive full symmetric stress vertex has a large, N-independent
  longitudinal residual.
- **T4:** `V_cons` alone has an `O(k0)` residual, while `V_cons+S` has an
  `O(k0^3)` residual; the improvement grows like `1/k0^2`, is N-independent at
  fixed `k0`, and survives an off-axis test.
- **T5:** the `yz` TT stiffness stays positive for `m in {0.5,1.0,1.5}`.
- **T6:** the seagull tadpole reproduces the small-`k` longitudinal contact term
  in the checked channels.
- **T6b:** the small-`k` contact-basis solve recovers `S=-B0+B1+B5` within the
  finite-`k` tolerance.

`TOTAL: PASS=15 FAIL=0`.

## What This Establishes

The row establishes a bounded finite-scheme statement: within the displayed
native Dirac operator, conserved stress vertex, and local contact basis, the
leading longitudinal violation is removed and the positive `yz` TT sign is
preserved.

This is useful upstream support for the universal-GR lane because it gives a
concrete local contact construction to test against a later derived
metric-Hessian vertex. It also supplies a clean negative contrast: the naive
symmetric stress extension fails.

## What Remains Open

- The full metric-source Hessian of `W=log|det(D+J)|`, including all contact
  terms, is not derived in this packet.
- The runner-defined vertex/seagull is not identified as the unique or complete
  W-native stress tensor.
- Exact finite-lattice diffeomorphism transversality is not proved impossible
  over all allowed local contact terms. The runner only reports the residual
  scaling in this tested finite scheme.
- The `E_g/T_2g` spin-2 isotropy continuum limit, induced Newton magnitude, and
  full Einstein-Hilbert closure remain separate open lanes.

## Relation to Retained Inventory

The native elliptic generator is supported by the retained-bounded CPT/real
anti-Hermitian Dirac surface. The exact internal U(1) Ward identity is
reconstructed in the runner as method-context and a machinery check. Sakharov
induced gravity and lattice energy-momentum conservation remain method-context
or future-bridge material here, not load-bearing imports.

Downstream notes may cite this row only as a bounded finite-scheme source
certificate. They still need the missing one-hop W metric-Hessian bridge before
claiming a W-native induced graviton.

## Honest Auditor Read

The clean claim is narrow but real: the runner constructs the matrices,
vertices, contact basis, and finite sums; it verifies exact U(1) machinery,
failure of the naive stress vertex, leading-order longitudinal improvement from
the local contact term, recovery of the seagull coefficients in the chosen
basis, and survival of the positive `yz` TT sign. It does not ask the audit lane
to accept the stronger full metric-Hessian or exact-all-`k` claims.
