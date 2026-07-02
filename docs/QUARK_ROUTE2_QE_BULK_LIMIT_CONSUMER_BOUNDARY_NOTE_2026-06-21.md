# Quark Route-2 q_E Bulk-Limit Consumer Boundary Note

**Date:** 2026-06-21
**Claim type:** no-go / negative route pruning
**Actual current-surface status:** no-go
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_qe_bulk_limit_consumer_boundary_2026_06_21.py`](../scripts/frontier_quark_route2_qe_bulk_limit_consumer_boundary_2026_06_21.py)

This note connects the already-landed `q_E(N)` box-size scan to the
`S3_TIME_PRIMITIVE_CHAIN_NOTE.md` consumer. It does not re-run the heavy
box-size computation, does not update any audit verdict, and does not claim
endpoint closure.

## Question

The S3 primitive-chain gate and the Route-2 readout map reduce the missing
readout endpoint to

```text
rho_E := beta_E / alpha_E = 21/4,
q_E := gamma_E(center) / gamma_E(shell) = 15/8,
```

after granting the two T-side candidates. The measured-calibration note found a
stack-internal finite-box anchor near the target at `N=15` and named a
box-size scan as the discriminator for the possible route

```text
q_E(N) from the stack shell-response functional -> 15/8 in a bulk limit.
```

The box-size scan has now settled that discriminator negatively for the tested
functional. This note records the downstream consequence for the primitive
chain: the bulk-limit route is pruned, while the fixed-carrier readout selector
remains open.

## Two-Layer Boundary

### Layer 1: bulk-limit route pruned

The box-size scan proves that the `N=15` agreement with `15/8` is a fixed-box
feature of the stack shell-response functional, not an infinite-volume value of
that functional.

The load-bearing facts are:

- the reconstructed `N=15` endpoint coefficients anchor to the landed
  center-excess cache;
- under the fixed-radius boundary-removal limit, `q_T(N)` sign-flips and
  `q_E(N)` runs large-negative for larger boxes rather than approaching
  `(5/6, 15/8)`;
- under the box-proportional probe limit, the channel quotients converge
  toward `(1, 1)`, not `(5/6, 15/8)`;
- the mechanism is a one-box denominator/numerator excursion in the delicate
  differenced E-channel coefficient, not a smooth approach to `15/8`.

Therefore the measured-calibration route

```text
finite N=15 calibration near q_E=15/8
  + boundary-removal limit
  => exact q_E=15/8
```

does not supply the missing Route-2 primitive.

### Layer 2: primitive-chain gate unchanged

This negative result does not prove that no Route-2 E-center primitive can
exist. It only removes one candidate source for the primitive: the bulk-limit
promotion of the measured `N=15` shell-response value.

The S3 primitive-chain owner row remains a fixed-carrier structural-selection
problem:

```text
derive beta_E / alpha_E = 21/4
```

or equivalently

```text
derive gamma_E(center) / gamma_E(shell) = 15/8
```

from an independent E-center endpoint ratio, source-domain rule, or stronger
readout-map primitive. The standing naturality no-go already says the current
restricted carrier/readout class leaves `rho_E` free unless such an additional
ingredient is supplied. The box-size scan does not sharpen or weaken that
fixed-carrier no-go; it only blocks the separate bulk-limit escape route.

## Exact Algebra Preserved

With the T-side candidate `rho_T = -1`, the T-channel quotient is

```text
q_T = 1 + rho_T / 6 = 5/6.
```

The target E-channel entry is exactly equivalent to

```text
rho_E = 21/4
<=> q_E = 1 + rho_E / 6 = 15/8
<=> q_E = (9/4) q_T
<=> c_TE = -8/9
```

when the shell ratio `gamma_T(shell) / gamma_E(shell) = -2` is granted.
This note does not derive any member of that chain. It records that the
specific bulk-limit attempt to justify `q_E = 15/8` fails for the tested stack
functional.

## What Is Claimed

- The heavy box-size scan already closed the measured-calibration bulk-limit
  route: no infinite-volume limit of that stack functional recovers `15/8`.
- The S3 primitive-chain consumer should not treat the finite `N=15`
  shell-response match as a derivation of `rho_E = 21/4`.
- The remaining positive target is sharper: a fixed-carrier E-center/source/
  readout primitive, not a bulk-limit extrapolation of the measured
  calibration functional.

## What Is Not Claimed

- No derivation of `rho_E = 21/4`.
- No derivation of `q_E = 15/8`.
- No derivation of the endpoint triple `(-1, -2, 21/4)`.
- No unique exact `Theta_R -> Lambda_R` coupling theorem.
- No final Einstein/Regge identification.
- No audit verdict or ledger/status change.
- No exhaustive no-go against future E-center/source/readout primitives.

## Downstream Use

Allowed downstream use:

- cite this packet to rule out the bulk-limit promotion of the `N=15`
  measured calibration for the current shell-response functional;
- cite this packet to keep the S3 primitive-chain gate focused on a
  fixed-carrier readout selector rather than a box-size extrapolation;
- cite the exact algebraic equivalence among `rho_E = 21/4`, `q_E = 15/8`,
  `q_E = (9/4) q_T`, and `c_TE = -8/9` as a target rewrite only.

Forbidden downstream use without a new theorem:

- do not cite this packet as a derivation of `beta_E / alpha_E = 21/4`;
- do not cite it as a derivation of `gamma_E(center) / gamma_E(shell) = 15/8`;
- do not cite it as closure of the Route-2 readout endpoint triple;
- do not cite it as closure of the unique readout-to-slice time-coupling law;
- do not use it as an all-routes no-go against future fixed-carrier
  E-center/source/readout primitives.

## Load-Bearing Inputs

- [`S3_TIME_PRIMITIVE_CHAIN_NOTE.md`](S3_TIME_PRIMITIVE_CHAIN_NOTE.md) names
  the open primitive-chain gate and the missing `beta_E / alpha_E = 21/4`
  entry.
- [`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
  records the direct consumer: the unique `Theta_R -> Lambda_R` law remains
  open until the readout endpoint triple is derived.
- [`QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md`](QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md)
  supplies the measured `N=15` finite-box calibration and names the box-size
  discriminator.
- [`QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md`](QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md)
  closes that discriminator negatively for the tested stack functional.
- [`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)
  supplies the standing fixed-carrier non-selection boundary.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_bulk_limit_consumer_boundary_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=37, FAIL=0
VERDICT: bulk-limit promotion is pruned; fixed-carrier readout selection remains open.
```
