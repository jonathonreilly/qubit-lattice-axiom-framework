# Block 12 V1-V5 Scratch

Row: `s3_time_theta_to_slice_coupling_note`
State: `open_gate`, 689 desc, unaudited.

## Setup

Parent is `S3_ANOMALY_SPACETIME_LIFT_NOTE.md` (route-2 of axiom-first GR survey). Block 07 (PR #1424) closed:
- Claim A: background uniqueness `PL S^3 x R`
- Claim B: Hessian-channel structural no-go

This row is downstream: the s3-time `Theta_R -> Lambda_R` coupling structure
on that background. Cited authorities:
- `QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19` — exact slice backbone
  `Lambda_R` SPD, `T_R = exp(-Lambda_R)`, `V_R(t) = exp(-t Lambda_R) u_*`
- `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19` — audited-clean no-go:
  endpoint triple `(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4)`
  not derived
- `QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28` —
  source-domain detour also blocked

Existing conditional family: `Xi_P(t; c) = (P_R c) ⊗ V_R(t)`, exact once
admissible `P_R` is chosen. Unresolved entry is `rho_E = beta_E/alpha_E`,
with admissible 1-param family `P(rho_E)`.

## Distinct angles from prior blocks

Prior blocks on this lane / Route-2:
- Block 02: AC_phi_lambda C3-foreclosure (different sub-row)
- Block 07: background uniqueness + Hessian channel no-go
- Companion no-gos on bypass channels: readout-map, source-domain, E-channel
  naturality, R-conn center-ratio

V1-V5 must be distinct from all of these.

## V1 — Direct derivation of readout-triple

Try to derive `(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4)`
from carrier `K_R` plus slice backbone.

VERDICT: blocked. `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE` says explicitly
that the current exact stack does not derive these. Anti-pattern: just
restating the audited-clean no-go. SKIP.

## V2 — Source-domain detour

Try to derive `Theta_R -> Lambda_R` without resolving readout, via
source-domain typed-edge inventory.

VERDICT: blocked by `QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO`. SKIP.

## V3 — E-channel naturality detour

Try to fix `beta_E/alpha_E = 21/4` via naturality on the E channel.

VERDICT: blocked by `QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO`. SKIP.

## V4 — R-conn center-ratio bridge detour

Try via R-connection center-ratio bridge.

VERDICT: blocked by `QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE`. SKIP.

## V5 — Structural factorization of the conditional family

This is the angle.

The conditional family is `Xi_P(t; c) = (P_R c) ⊗ V_R(t)` where
`V_R(t) = exp(-t Lambda_R) u_*`.

Observation: the time-dependence is in the **second tensor factor only**,
and `V_R(t)` does NOT depend on `P_R`. So:

(F1) **Slice generator is readout-independent.** `Lambda_R` is defined
     intrinsically by `Schur boundary`, independent of any readout choice.

(F2) **Time-channel uniformity.** For any admissible `P_R` (i.e., any
     `rho_E` in the 1-param family), the second tensor factor `V_R(t)`
     is identical. Hence `(d/dt) Xi_P(t; c) = -(P_R c) ⊗ (Lambda_R V_R(t))`,
     which separates `P_R` (spatial) from `Lambda_R` (temporal).

(F3) **Norm-ratio invariance.** For any two times `t1, t2` and any
     admissible `P_R(rho_E)`,
     `|| Xi_P(t1; c) || / || Xi_P(t2; c) ||` depends ONLY on
     `||V_R(t1)|| / ||V_R(t2)||` and `||P_R c||` cancels in the ratio,
     so this temporal-attenuation ratio is `rho_E`-independent.

(F4) **Semigroup commutation.** The transfer `T_R = exp(-Lambda_R)`
     acts on the second factor only:
     `(I ⊗ T_R) Xi_P(t; c) = Xi_P(t+1; c)`.
     This identity holds for every admissible `P_R`.

(F5) **Spatial-temporal separation of the ambiguity.** Comparing
     `Xi_P(t; c)` for two distinct admissible `P_a, P_b`:
     `Xi_a(t; c) - Xi_b(t; c) = ((P_a - P_b) c) ⊗ V_R(t)`.
     The DIFFERENCE has the same time profile `V_R(t)` (up to scalar
     `(P_a - P_b) c`). The ambiguity is therefore RANK-1 along the
     time-direction for every fixed carrier column.

This is a positive narrow theorem on the row. It is **independent of** and
**does not bypass** the readout-triple no-go: the readout ambiguity is
localized in the SPATIAL factor (the prefactor `(P_R c)`), while the
TEMPORAL factor is universal. We cannot derive the unique coupling, but
we CAN derive the rigidity of the time-channel structure.

This is distinct from:
- Block 02 AC_phi_lambda foreclosure (which is about phi-lambda C3 structure)
- Block 07 background uniqueness (about topology of `PL S^3 x R`)
- Block 07 Hessian channel no-go (about source-rank promotion failure)
- The readout-map / source-domain / E-channel / R-conn no-gos
  (which all try to RESOLVE the readout ambiguity)

V5 takes the readout ambiguity AS GIVEN and proves that the time-channel
structure is universal regardless.

## Chosen angle: V5

Deliverable: positive narrow theorem on the row.
- Statement: Under cited inputs (exact slice backbone + admissible readout
  class), the conditional coupling family `Xi_P(t; c) = (P_R c) ⊗ V_R(t)`
  has a universal time-channel structure: (F1)-(F5) hold for every
  admissible `P_R(rho_E)`.
- Effect on row: the row remains `open_gate` for the unique theorem (the
  upstream readout-triple is still not derived), but a positive narrow
  theorem on the FACTORIZATION RIGIDITY is now landed. The ambiguity is
  RANK-1 along the time-axis and is localized in the spatial prefactor.
- Type: `positive_theorem`, narrow scope. Does NOT close the parent
  `open_gate`. Names the readout-triple as the still-open theorem target.

## Runner plan

1. Build `Lambda_R` from Schur boundary (same as upstream runner).
2. Sample two distinct admissible readouts `P_a = P(0)`, `P_b = P(21/4)`.
3. For carrier columns (E-shell, E-center, T-shell, T-center):
   (a) Verify `V_R(t)` is `P_R`-independent (definition; assert equality
       across two builds).
   (b) Verify time-derivative separation: numerically compute
       `(Xi_P(t+h) - Xi_P(t))/h` and compare to `-(P_R c) ⊗ (Lambda_R V_R(t))`.
   (c) Verify norm-ratio invariance:
       `||Xi_a(t1; c)|| / ||Xi_a(t2; c)|| ≈ ||Xi_b(t1; c)|| / ||Xi_b(t2; c)||`
       for several `t1, t2`.
   (d) Verify semigroup commutation: `(I ⊗ T_R) Xi_P(t; c) ≈ Xi_P(t+1; c)`
       for both `P_a, P_b`.
   (e) Verify rank-1 ambiguity along time: `Xi_a(t; c) - Xi_b(t; c)` factors
       as `((P_a - P_b) c) ⊗ V_R(t)`.

Hard rules: A_min only (no new axiom imports; uses only cited authorities).

## Block 07 cross-reference

Block 07 closed the BACKGROUND (`PL S^3 x R`) uniquely. This row's slice
generator `Lambda_R` lives on that background's spatial slice. F1-F5
operate on that slice and the orthogonal `R` axis. The block 07 inputs
(d_t=1, single clock, anomaly-forced time) are upstream context, not
additional axioms.

## Hard-rules confirmation

A_min only: all ingredients are imported from cited audited authorities
(`QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE` and `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE`).
No new primitives. The theorem is a purely algebraic property of the
already-existing conditional family.
