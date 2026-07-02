# s3-Time Readout Primitive Bridge Assessment

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set,
predict, or change the audit status of any claim or dependency. It records a
source-side bridge assessment; classification belongs only to the independent
audit lane.
**Assessment role:** scope-limited check of whether the old `eta_floor_tf`
endpoint-fitted affine coefficients discharge the gate-level
physical/admissible readout-primitive bridge.
**Primary runner:** [scripts/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.py](../scripts/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.py)
**Runner cache:** [logs/runner-cache/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.txt](../logs/runner-cache/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.txt)

## One-Hop Authorities

- [`S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md)
  supplies the bilinear carrier definition, the old `eta_floor_tf`
  endpoint-fitted affine projection, and the named physical-primitive bridge
  gap.
- [`QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md)
  supplies the gate family `Xi_P(t; c)`.
- [`S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md`](S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md)
  supplies the localization of readout ambiguity in the spatial prefactor.
- [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  supplies the restricted bright readout class and the exact missing map entry.

## Quote Anchors

From the bilinear primitive note, the named bridge target is:

> "A bridge theorem identifying the bilinear carrier `K_R(q)` with any physical tensor primitive in the GR-readout chain"

The same note describes the old eta-floor coefficients as:

> "endpoint-fitted, not first-principles"

From the time-coupling note, the gate starts only:

> "Given any admissible readout map `P_R`"

and still lacks a theorem that:

> "selects one unique `P_R`"

From the rigidity note, the readout ambiguity is:

> "structurally localized in the spatial prefactor"

while the:

> "time-channel structure is universal"

From the readout-map note, the relevant class is:

> "any admissible bright-preserving linear readout"

and the remaining named entry is the:

> "irreducible missing map entry"

## Admissibility Checklist

The gate-level phrase "physical/admissible readout primitive" decomposes into
these source-imposed conditions.

1. Carrier-domain condition. The readout must act on the restricted carrier
   coordinates
   ```text
   vec K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T).
   ```

2. Bright-preserving channel condition. On the restricted endpoint class, any
   admissible bright-preserving linear readout has the channelwise form
   ```text
   P_R = [[alpha_E, 0, beta_E, 0],
          [0, alpha_T, 0, beta_T]].
   ```

3. Gate-family condition. Once `P_R` is supplied, the gate consumes it only
   through
   ```text
   Xi_P(t; c) = (P_R c) tensor V_R(t),
   V_R(t) = exp(-t Lambda_R) u_*.
   ```
   Therefore changing `P_R` changes the spatial source prefactor but not the
   time-channel backbone.

4. Normalized target-family condition. The exact target used by the Route-2
   readout map compresses to
   ```text
   (beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E)
     = (-1, -2, 21/4).
   ```
   After granting the two T-side target entries, the one-parameter family is
   ```text
   P(rho_E) = [[1, 0, rho_E, 0],
               [0, -2, 0, 2]],
   rho_E = beta_E / alpha_E.
   ```

5. Physical-primitive bridge condition. Membership in the bright class is not
   enough to make the readout the physical primitive for the gate. The bilinear
   note names a separate bridge theorem identifying `K_R` or its affine
   projection with the physical tensor primitive used by the gate.

## Eta-Floor Check

The old eta-floor endpoint-fitted affine construction gives

```text
gamma_E = a_E u_E + b_E delta_A1 u_E
gamma_T = a_T u_T + b_T delta_A1 u_T
P_eta  = [[a_E, 0, b_E, 0],
          [0, a_T, 0, b_T]].
```

So at the broad restricted-class level it is a member: it has the required
channelwise row support, nonzero shell coefficients, and it reproduces the
live endpoint coefficients on the four carrier endpoint columns. The runner
checks the carrier residual at `2.220e-16` and the endpoint readout residual
at `1.084e-19`.

The eta-floor `t_balance` is exactly the live absolute T-channel
slope/intercept ratio on this surface:

```text
t_balance = |b_T/a_T| = 1.000030814262
```

equivalently `|beta_T/alpha_T|` for `P_eta`. That verifies what the checkpoint
said: `t_balance` is a computable endpoint-fitted comparator, not by itself a
gate primitive selection theorem.

The exact target triple is rationally:

```text
rho_T = beta_T/alpha_T = -1
mu    = alpha_T/alpha_E = -2
rho_E = beta_E/alpha_E = 21/4
```

and gives, by exact arithmetic,

```text
q_T = 1 + rho_T/6 = 5/6
q_E = 1 + rho_E/6 = 15/8
c_TE = mu q_T/q_E = -8/9.
```

The live eta-floor endpoint-fitted map does not equal that normalized target
triple at exact tolerance:

```text
rho_T = -1.000030814262
mu    = -2.005383530819
rho_E = +5.257481167681.
```

This is not a rounding route to a closed form. The exact target-family values
come from rational arithmetic; the live eta-floor values are live-module
floating readouts.

## Selection Freedom

After T-side normalization, the selection freedom is exactly

```text
rho_E = beta_E / alpha_E.
```

Using exact rational arithmetic on the endpoint columns,

```text
E-shell  = (1, 0, 0,   0)
E-center = (1, 0, 1/6, 0)
```

the family gives

```text
P(0)      E-shell  = (1, 0)
P(21/4)   E-shell  = (1, 0)
P(0)      E-center = (1, 0)
P(21/4)   E-center = (15/8, 0).
```

So the shell normalization does not select `rho_E`; the center E lift is
`1 + rho_E/6`. This is the lane's readout-underdetermination analog.

The rigidity note does not remove that freedom. It shows that for any two
admissible choices,

```text
Xi_a(t; c) - Xi_b(t; c) = ((P_a - P_b)c) tensor V_R(t),
```

so the ambiguity remains in the spatial prefactor. The runner verifies the
live factor residual at `3.469e-18` and a rank-tail of `0.000e+00` for the
`E-center` witness.

## Outcome

The bridge attempt lands only at broad membership:

- `P_eta` is a restricted bright, endpoint-fitted affine readout on
  `vec K_R`.
- `P_eta` is not the exact normalized target-family member at exact tolerance.
- The one-hop authorities do not supply a theorem selecting `P_eta` as the
  physical gate primitive.
- After T-side normalization, the named selection freedom is `rho_E`.

Therefore the current bridge outcome is membership-but-not-uniqueness, with an
additional exact-target mismatch for the live endpoint-fitted coefficients. The
open target is not a new time law; it is a selection/identification theorem for
the readout map.

What would pin it:

1. a derivation of a unique admissible `P_R` for the gate;
2. equivalently, a derivation of the endpoint triple
   `(-1, -2, 21/4)`;
3. or an explicit convention declaring the endpoint-fitted eta-floor affine
   map to be the gate readout convention, in which case the result is a
   convention-backed readout, not a derived physical primitive.

## Negative-Claim Discipline Gate

The obstruction statement above is deliberately narrow: it does not say no
route can identify a physical readout. It says the requested eta-floor bridge is
not derived by the cited one-hop authorities and live checks.

N1 route enumeration:

- Broad class membership route: succeeds only as membership in
  `P_R = [[alpha_E,0,beta_E,0],[0,alpha_T,0,beta_T]]`; it does not select the
  physical gate primitive. Marker: `ATTEMPTED` here, against the readout-map
  and time-coupling notes.
- Exact normalized target route: checked here; the live eta-floor ratios miss
  `(-1, -2, 21/4)` at exact tolerance. Marker: `ATTEMPTED` here, against the
  exact readout-map target triple.
- Factor-rigidity route: checked here; it preserves time-channel universality
  but leaves the spatial prefactor choice. Marker: `ATTEMPTED` here, against
  the rigidity note.
- Endpoint algebra route: checked here; it shows equivalence of the target
  triple to `(5/6, 15/8, -8/9)` but does not derive the triple. Marker:
  `ATTEMPTED` here, against the exact endpoint columns.
- Physical primitive bridge route: the bilinear note names this bridge as a
  separate theorem target, so it cannot be imported from the eta-floor fit.
  Marker: `RULED OUT BY PRIOR`, by the bilinear primitive note's open-gap
  statement.
- Convention route: viable only as a convention-setting move, not as a
  derivation from the cited notes. Marker: `ATTEMPTED` here, as the explicit
  partial-closure path.

N2 wall independence:

The collapsed residual is one selection wall: derive or explicitly declare the
gate readout map. The subconditions `rho_T`, `mu`, and `rho_E` are coordinates
of that wall, not separate independent closures in this note.

N3 hidden-wall scan:

The load-bearing words are "admissible", "physical", and "canonical". This note
uses "admissible" only for the restricted bright class, "physical" only for the
separate bridge theorem, and "canonical" only for a selected unique map.

N4 residual matching:

All four one-hop authorities point at the same residual: the readout map is not
uniquely selected for the gate.

N5 rhetoric audit:

The negative statement is not "eta-floor can never be a readout." The tested
statement is narrower: eta-floor is not derived here as the physical/canonical
gate primitive.

N6 partial-closure path scan:

A convention could select `P_eta` as the gate readout convention. That would
pin the practical map but would not turn the endpoint-fitted coefficients into
a first-principles physical primitive theorem.

N7 steelman:

The strongest counterargument is that the time-coupling note needs only a
supplied admissible `P_R`, and `P_eta` is indeed an admissible restricted bright
readout. This note accepts that membership point. The counterargument does not
select a unique physical gate primitive unless a convention or theorem is added.

N8 cross-cycle echo:

The bilinear tensor primitive note already classifies the old eta-floor
coefficients as endpoint-fitted rather than first-principles. This note
confirms that warning on the live modules and redirects the residual to the
selected readout map.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.py
```

Current runner total:

```text
TOTAL: PASS=14, FAIL=0
```

Cache regeneration command:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
