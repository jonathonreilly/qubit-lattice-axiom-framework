# S3 Time Factor-Rigidity / Readout-Primitive Split Note

**Date:** 2026-06-21
**Type:** exact support theorem / open-boundary split
**Actual current-surface status:** exact-support
**Trace class:** upstream_support
**Reachability:** supports and narrows the parent `s3_time_theta_to_slice_coupling_note`; not a readout-map selection theorem
**Primary runner:** `scripts/frontier_s3_time_factor_rigidity_readout_primitive_split_2026_06_21.py`

## Purpose

This note separates two statements that are easy to blur:

1. **Safe factor-rigidity side.** The conditional family
   ```text
   Xi_P(t ; c) = (P_R c) tensor V_R(t)
   ```
   has a universal time channel for every admissible `P(rho_E)`. The
   `Lambda_R` backbone, `V_R(t)`, norm-ratio cancellation, semigroup action,
   and rank-one localization of readout differences are all safe consequences
   of the factor-rigidity theorem.
2. **Blocked primitive-selection side.** Those safe time-channel facts do not
   select the readout primitive, do not select one unique `P_R`, and do not
   close the endpoint triple `(-1, -2, 21/4)`.

The point is a source-boundary firewall for downstream consumers: cite
factor-rigidity for time-channel universality and localization of ambiguity;
do not cite it as a readout primitive theorem.

## One-hop authorities

- [`S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md`](S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md)
  proves the five factor-rigidity properties for the full admissible
  `P(rho_E)` family.
- [`S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md`](S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md)
  checks the old endpoint-fitted eta-floor affine readout and lands only
  membership in the broad bright class, not uniqueness or physical-primitive
  selection.
- [`QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md)
  supplies the conditional time-coupling family once an admissible `P_R` is
  supplied.
- [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  supplies the exact restricted bright readout class and names the remaining
  `E`-channel entry.

## Exact local split

After granting the two T-side target coordinates, the reduced readout family is

```text
P(rho_E) = [[1, 0, rho_E, 0],
            [0, -2, 0, 2]].
```

For a restricted carrier vector

```text
c = (u_E, u_T, delta_E, delta_T),
```

the map is

```text
P(rho_E)c = (u_E + rho_E delta_E, -2 u_T + 2 delta_T).
```

Therefore for two admissible choices `rho_a`, `rho_b`,

```text
(P(rho_b) - P(rho_a))c
  = ((rho_b - rho_a) delta_E, 0).
```

This is the exact split:

- any carrier with `delta_E = 0` is blind to `rho_E`;
- any carrier with nonzero `delta_E` can inherit the unresolved E-center
  prefactor;
- the ambiguity is not in `Lambda_R` or in the time semigroup.

On the endpoint columns:

| Carrier | Coordinate | `rho_E` dependence |
|---|---:|---|
| `E-shell = (1,0,0,0)` | `delta_E = 0` | independent |
| `T-shell = (0,1,0,0)` | `delta_E = 0` | independent |
| `T-center = (0,1,0,1/6)` | `delta_E = 0` | independent |
| `E-center = (1,0,1/6,0)` | `delta_E = 1/6` | dependent |

For the E-center witness,

```text
P(rho_E) E-center = (1 + rho_E/6, 0).
```

Thus `rho_E = 0` gives the E-center factor `1`, while `rho_E = 21/4`
gives the E-center factor `15/8`. The factor-rigidity theorem preserves this
as a spatial prefactor choice; it does not decide between those alternatives.

## Factor-rigidity-safe claims

The following statements can be reused without selecting the endpoint triple:

1. `Lambda_R` is readout-independent.
2. `V_R(t) = exp(-t Lambda_R)u_*` is readout-independent.
3. Norm ratios of `Xi_P(t;c)` cancel the `P_R c` prefactor wherever the
   prefactor is nonzero.
4. Right multiplication by the transfer acts only on the time factor:
   ```text
   Xi_P(t;c) T_R^T = Xi_P(t+1;c).
   ```
5. Differences across readout choices factor as
   ```text
   Xi_b(t;c) - Xi_a(t;c)
     = ((P(rho_b)-P(rho_a))c) tensor V_R(t),
   ```
   so the ambiguity is rank-one along the time channel and localized in the
   spatial source prefactor.

These are exact support statements about the conditional family.

## Blocked primitive-selection claims

The following upgrades are not supplied by factor-rigidity:

1. unique selection of `P_R`;
2. selection of `rho_E = 21/4`;
3. identification of the endpoint-fitted eta-floor affine map as the physical
   gate primitive;
4. a theorem that the `E-center` prefactor is independent of the unresolved
   readout entry.

The bridge assessment remains the correct boundary: eta-floor is a member of
the broad restricted bright class, and the one-hop notes do not supply a
uniqueness theorem or physical primitive identification. Factor-rigidity cannot
upgrade broad membership into uniqueness because it is insensitive to the
selector that fixes the spatial prefactor.

## Consumer rule

For downstream work:

- If a consumer uses only `Lambda_R`, `V_R(t)`, norm-ratio time attenuation,
  semigroup propagation, or the rank-one localization form, it may cite the
  factor-rigidity theorem directly.
- If a consumer evaluates an E-center source with `delta_E != 0`, it must keep
  the result conditional on a supplied `rho_E` or cite a separate readout-map
  selection theorem.
- If a consumer needs the exact endpoint triple `(-1, -2, 21/4)`, this split
  note does not provide that selection. The open object remains the readout
  primitive / E-center source rule.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_s3_time_factor_rigidity_readout_primitive_split_2026_06_21.py
```

Expected current result:

```text
TOTAL: PASS=49, FAIL=0
```

The runner checks source anchors, exact `delta_E` algebra, shell/T-center
blindness, E-center dependence, semigroup preservation under both
`rho_E = 0` and `rho_E = 21/4`, and the claim firewall above.

## Honest endpoint

This block adds an exact support/boundary split:

- Factor-rigidity is safe and reusable for the universal time-channel
  structure of `Xi_P`.
- The unresolved readout primitive remains entirely on the spatial prefactor,
  and locally only on carriers with `delta_E != 0`.
- The branch does not select a unique readout map, does not close the endpoint
  triple, and is not a derivation of the readout primitive.
