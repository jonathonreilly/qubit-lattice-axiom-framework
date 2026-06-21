# S3 Time Direct-Consumer E-Center Dependency Classification Note

**Date:** 2026-06-21
**Status:** exact support / dependency classification; no unique readout theorem
**Runner:** `scripts/frontier_s3_time_direct_consumer_ecenter_dependency_classification_2026_06_21.py`
**Primary parents:**
`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`,
`QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md`,
`S3_TIME_PRIMITIVE_CHAIN_NOTE.md`,
`S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md`,
`S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`,
`QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md`

## Scope

This note records a branch-local exact classification for direct consumers of
the current S3/Route-2 carrier, readout, and time-coupling surfaces.

It does not select a readout primitive. In particular, it does not turn the
unresolved E-center entry

```text
rho_E := beta_E / alpha_E
```

into a current-surface theorem. The result is a dependency split: consumers
that do not evaluate the E-center delta direction can reuse the exact
time/slice backbone, while consumers that do evaluate that direction remain
conditional on a separate E-center/source/readout rule.

## Source Surface

After the two T-side entries are granted, the restricted Route-2 readout family
has the form

```text
P(rho_E) =
[[1, 0, rho_E, 0],
 [0,-2, 0,     2]].
```

The endpoint carrier columns are

```text
E-shell  = (1, 0, 0,   0)
E-center = (1, 0, 1/6, 0)
T-shell  = (0, 1, 0,   0)
T-center = (0, 1, 0, 1/6).
```

The E-center-blind subspace is

```text
span{E-shell, T-shell, T-center}.
```

The missing direction is

```text
E-center - E-shell = (0, 0, 1/6, 0).
```

The runner checks that the blind subspace has rank `3`, adding E-center gives
rank `4`, and the E-center delta direction is not in the blind subspace.

## Exact Dependency Identity

For a carrier vector

```text
c = (u_E, u_T, delta_E, delta_T),
```

two admissible values `rho_a` and `rho_b` satisfy

```text
(P(rho_b) - P(rho_a)) c = ((rho_b - rho_a) delta_E, 0).
```

Therefore dependence on the unresolved readout entry is exactly equivalent to
dependence on the E-center `delta_E` coordinate.

The runner checks the special comparison between `rho_E = 0` and
`rho_E = 21/4` only as a classifier:

```text
P(0) E-shell    = P(21/4) E-shell
P(0) T-shell    = P(21/4) T-shell
P(0) T-center   = P(21/4) T-center
P(0) E-center  != P(21/4) E-center.
```

No endpoint value is used as proof input.

## Consumer rule

A direct consumer is E-center safe exactly when its current-surface statement
depends only on `Lambda_R`, `V_R(t)`, the time semigroup, a definition-only
carrier, or endpoint columns with `delta_E = 0`.

A direct consumer is E-center dependent when it requires a unique `P_R`,
evaluates `q_E`, evaluates `rho_E`, uses the center `T/E` ratio, promotes the
eta-floor as a physical primitive, or identifies the packet with the final
Einstein/Regge tensor law.

## Safe direct consumers

These current-surface consumers are safe under the classification above:

| Consumer | Reason |
|---|---|
| `Lambda_R backbone` | Uses the Schur/slice construction and no `P_R` evaluation. |
| `V_R(t) time seed` | Depends on `Lambda_R` and the canonical time seed, not on `rho_E`. |
| `norm-ratio time attenuation` | The nonzero spatial prefactor cancels from the time-ratio identity. |
| `semigroup propagation` | The transfer acts on the time factor only. |
| `K_R definition-only carrier` | Records the bilinear carrier before a physical readout primitive is chosen. |
| `E-shell/T-shell/T-center endpoint data` | Uses `delta_E = 0` or T-only endpoint columns. |

These are exact support uses of the current parent surfaces. They can be
cherry-picked as support for time-channel or carrier-local statements, provided
the downstream wording does not claim a unique readout map.

## E-center-dependent consumers

These consumers remain open until a separate E-center/source/readout rule is
available:

| Consumer | Remaining dependency |
|---|---|
| `unique P_R theorem` | Requires a rule selecting the unresolved readout entry. |
| `q_E or rho_E endpoint` | Evaluates the E-center direction directly. |
| `c_TE center ratio` | Is equivalent to an E-center lift once the T-side values are fixed. |
| `eta-floor as physical primitive` | Requires either a bridge theorem or an admitted convention. |
| `Einstein/Regge final identification` | Requires the physical readout primitive and final dynamics bridge. |

This table is a boundary for downstream use. It preserves the positive
time-channel statements while keeping the E-center source/readout problem
visible.

## Relation To Prior Blocks

The factor-rigidity theorem shows that readout ambiguity is localized in the
spatial prefactor of the conditional family

```text
Xi_P(t; c) = (P_R c) tensor V_R(t).
```

The E-center blindness no-go shows that E-center-blind endpoint constraints do
not select the missing readout entry. This note combines those two facts into a
consumer-facing classification:

- time-channel and carrier-definition consumers can be reused when they do not
  evaluate `delta_E`;
- endpoint or physical-readout consumers that do evaluate `delta_E` remain
  blocked by the same E-center/source/readout residual.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_s3_time_direct_consumer_ecenter_dependency_classification_2026_06_21.py
```

Expected branch result:

```text
TOTAL: PASS=29, FAIL=0
VERDICT: direct consumers are classified by whether they evaluate the E-center delta_E direction.
```

The runner also checks source-note anchors, the exact carrier ranks, the
comparison between E-center-blind and E-center-sensitive columns, and the full
consumer label inventory above.

## Handoff Boundary

This note is intended as exact support and dependency hygiene for review. It
does not modify the parent row status, does not supply the missing E-center
source rule, and does not justify any downstream final physics identification.
