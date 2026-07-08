# Quark Route-2 Shell Multiplicity Exact Shell Ratio Surface Boundary

---
claim_type_author_hint: bounded_theorem
claim_scope: >-
  On the named Route-2 endpoint surface (the five named files), the shell
  gammas enter only as probe-convention-dependent finite-difference
  certificates whose full-replay recomputation path is currently broken; no
  exact shell-ratio derivation is available there; SHELL-MULT therefore enters
  the endpoint cluster only as a supplied premise.
---

**Date:** 2026-07-07
**Type:** bounded_theorem
**Runner:**
`scripts/quark_route2_shell_multiplicity_exact_shell_ratio_surface_boundary_2026_07_07.py`

## Surface Statement

This note checks the named Route-2 endpoint surface for an exact derivation of
the shell ratio

```text
s_TE = gamma_T(shell) / gamma_E(shell).
```

The result is a bounded surface boundary. The computation supports only:

```text
on these five files, no exact shell-ratio derivation is available.
```

It does not say the ratio is impossible to derive elsewhere. It does not prove
`s_TE = -2`, prove another exact value, or prove that the fast-certificate
deviation is a finite-window correction around exact `-2`.

The five load-bearing surface files are:

```text
docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md
docs/QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md
scripts/frontier_quark_endpoint_readout_constraints.py
scripts/frontier_same_source_metric_ansatz_scan.py
scripts/frontier_tensor_support_center_excess_law.py
```

The [readout-map note](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) and
the [quotient note](QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md)
are load-bearing authorities. The
[naturality note](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)
is comparison-only context and is checked in the runner's non-fatal tier.

## Exact Shell Configuration

The endpoint replay builds the adapted seven-site basis in
`scripts/frontier_same_source_metric_ansatz_scan.py`:

```python
def build_adapted_basis() -> np.ndarray:
    e0 = np.zeros(7)
    e0[0] = 1.0
    px, mx, py, my, pz, mz = [np.eye(7)[i] for i in range(1, 7)]
    s = (px + mx + py + my + pz + mz) / np.sqrt(6.0)
    e1 = (px + mx - py - my) / 2.0
    e2 = (px + mx + py + my - 2.0 * pz - 2.0 * mz) / np.sqrt(12.0)
    tx = (px - mx) / np.sqrt(2.0)
    ty = (py - my) / np.sqrt(2.0)
    tz = (pz - mz) / np.sqrt(2.0)
    return np.column_stack([e0, s, e1, e2, tx, ty, tz])
```

The endpoint module then uses `s_unit = s / math.sqrt(6.0)`. The runner builds
the exact rational endpoint vectors corresponding to those lines:

```text
e0    = (1, 0, 0, 0, 0, 0, 0)
shell = (0, 1/6, 1/6, 1/6, 1/6, 1/6, 1/6)
```

Using the `delta_A1` endpoint coordinate from the readout-map note on this A1
family, the runner recomputes rather than assigns:

```text
Q(shell) = 1
Q(center) = 1
delta_A1(center) = 1/6
delta_A1(shell) = 0
endpoint gap = 1/6
```

This exact support configuration is available on the surface. It is not, by
itself, an exact derivation of `s_TE`.

## Gamma Path

The endpoint module has a fast certificate path and a full tensor replay path.
The fast path is `FAST_ENDPOINT_READOUT` in
`scripts/frontier_quark_endpoint_readout_constraints.py`:

```text
gamma_E(shell) = -2.010572657265e-04
gamma_T(shell) = +4.031967723697e-04
```

Those literals are stored in dataclass fields annotated as Python `float`.
The full replay path calls:

```python
gamma_e_center, gamma_t_center = center.gamma_pair(e0, ex, t1x)
gamma_e_shell, gamma_t_shell = center.gamma_pair(s_unit, ex, t1x)
```

The center-excess module defines `gamma_pair` as follows.

Source: `scripts/frontier_tensor_support_center_excess_law.py`

```python
def gamma_pair(q: np.ndarray, ex: np.ndarray, t1x: np.ndarray) -> tuple[float, float]:
    beta_e = float((eta_floor(q + EPS * ex) - eta_floor(q - EPS * ex)) / (2.0 * EPS))
    beta_t = float((eta_floor(q + EPS * t1x) - eta_floor(q - EPS * t1x)) / (2.0 * EPS))
    red = shell.reduced_data(phi_from_q(q))
    a_aniso = float(red["anchor_per_Q"]) * float(np.sum(q))
    return beta_e / a_aniso, beta_t / a_aniso
```

Here `EPS = 0.005`. At a fixed endpoint point, the denominator is common to
both channels, but the numerator is still a finite-difference probe of the
selected tensor scalar.

The named surface exposes `eta_floor` only as:

```python
def eta_floor(q: np.ndarray) -> float:
    return float(two.tensor_metrics(phi_from_q(q))[0])
```

Checking that route shows no exact algebraic definition in the named modules.
The visible route through `eta_floor` is float-only on this surface: it
delegates to tensor metrics and immediately casts the selected value to
`float`. Therefore there is no exact route through `eta_floor` available in the
five named files.

## Full Replay Observation

On the current tree, the full tensor replay path is not available. This was
verified on 2026-07-07 by running the endpoint import path with
`QUARK_ENDPOINT_FULL_TENSOR_REPLAY=1`.

The exception is raised on the CENTER call:

```python
gamma_e_center, gamma_t_center = center.gamma_pair(e0, ex, t1x)
```

This is endpoint line 133, before the shell call at endpoint line 134.
Inside `center.gamma_pair`, the failing statement is:

```python
red = shell.reduced_data(phi_from_q(q))
```

Exact exception:

```text
AttributeError: module 'one_parameter_shell' has no attribute 'reduced_data'
```

Consequence: on this named surface, the only live source of the shell gammas is
the frozen fast certificate. No exact recomputation of the shell ratio is
currently available from the named modules.

The runner records this as `PASS=observation-recorded`: PASS means the dated
observation was recorded and matched the current tree, not that full replay is
available.

## Readout Surface

The readout-map note reduces the restricted carrier class to:

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]]
```

On the shell columns:

```text
gamma_E(shell) = alpha_E
gamma_T(shell) = alpha_T
s_TE = alpha_T / alpha_E
```

The [readout-map note](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
also states that the current exact stack does not derive the target
dimensionless readout triple. Thus the exact surface names the coefficient
ratio that would be needed, but does not select it.

Two exact maps of the reduced form illustrate the remaining freedom:

```text
Choice A:
alpha_E = 1, alpha_T = -2, beta_E = 0, beta_T = 0
s_TE = -2
```

```text
Choice B:
alpha_E = 1
alpha_T = -4031967723697 / 2010572657265
beta_E = 0
beta_T = 0
s_TE = -4031967723697 / 2010572657265
```

Both maps have the exact reduced form allowed by the readout surface. They
differ only in `alpha_T / alpha_E`. The surface names this ratio; it does not
derive it.

The
[naturality note](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)
is only comparison context here. At its retained scope, it grants the T-side
candidates `beta_T / alpha_T = -1` and `alpha_T / alpha_E = -2` as hypotheses
and then leaves the E-channel entry free. It does not derive the T-side shell
candidate. This boundary note is consistent with that comparison result.

## Routes Considered

The exact shell support route closes only the support coordinates:
`Q(shell) = 1`, `delta_A1(shell) = 0`, and endpoint gap `1/6`.

The reduced readout route closes only the form of the map. It reduces the
shell question to the coefficient ratio `alpha_T / alpha_E`.

The fast-certificate route supplies current endpoint floats. It does not
supply an exact theorem-grade contraction identity.

The finite-difference tensor route depends on the probe convention
`EPS = 0.005`, the selected directions `ex` and `t1x`, the scalarization
`eta_floor`, the `anchor_per_Q` normalization, and the replay tier.

The `eta_floor` route is float-only on the named surface. No exact algebraic
definition of `eta_floor` is present in the five named files.

The full replay route is currently broken on the center call before any shell
gamma can be recomputed.

These routes support the bounded statement that the exact shell ratio is not
derived on the named file surface. They do not establish that the ratio cannot
be derived on a future or different surface.

## Fast Certificate Reifications

Treating the fast endpoint values as Python binary floats gives:

```text
gamma_T(shell) / gamma_E(shell)
  = -14875335342499166 / 7417703850033121
  = -2.005382749600167...
```

Treating the printed decimal strings as exact decimal inputs gives:

```text
gamma_T(shell) / gamma_E(shell)
  = -4031967723697 / 2010572657265
  = -2.005382749600167...
```

The two exact reifications differ as rationals, but agree to the printed
precision checked by the runner:

```text
-2.005382749600167
```

For the decimal-string reification, the displayed residual from `-2` is:

```text
(-4031967723697 / 2010572657265) + 2
  = -10822409167 / 2010572657265
```

The displayed relative deviation from `-2` is:

```text
10822409167 / 4021145314530
```

These fractions are not promoted here to truncation noise around exact `-2`.
They are also not promoted to a final exact non-`-2` value.

## Endpoint Premise Boundary

The [quotient note](QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md)
names `SHELL-MULT` as a supplied premise:

```text
SHELL-MULT (named conditional premise): the shell coefficient ratio
(historically the shell-multiplicity candidate) is SUPPLIED as
a_T/a_E = -2.
```

The same source names the shell-counting target that is still open:

```text
3. derive SHELL-MULT from shell-counting algebra if a future row needs the
   denominator law without a supplied premise.
```

It also records the bridge target in the re-audit guidance:

```text
missing_bridge_theorem: provide a retained first-principles derivation
of gamma_E(center)/gamma_E(shell) = 15/8, and separately close the
a_T/a_E = -2 bridge before promoting the denominator law.
```

Source for all three quotes in this section:
[the quotient note](QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md).

On the present surface, that bridge is not closed. Therefore `SHELL-MULT`
enters the endpoint cluster only as a supplied premise.

## Citation Contract

This note may be cited only for:

```text
On the five named files, no exact shell-ratio derivation is available;
SHELL-MULT remains a supplied premise on that endpoint surface.
```

It may not be cited as proving `s_TE = -2`, proving a different exact closed
form, proving that the live deviation is finite-window noise, proving that the
live deviation is intrinsic to a final tensor theorem, or proving that the
exact shell ratio differs from `-2`. The exact value is undetermined on this
surface, not known-different.

## Firewall

This note may not be cited as deriving `ENDPOINT-QE`, deriving `rho_E`, or
landing any endpoint theorem. It records only the named-surface boundary for
this shell-ratio derivation block.

This note may not be cited against the retained naturality boundary. It is
consistent with that boundary because the T-side candidate was granted there
as a hypothesis, not derived there.

`SHELL-MULT` may not be cited as refuted. It remains a supplied premise unless
a future counting surface derives or rejects it.

This note may not be cited as a no-go.

## Validation

Run:

```bash
python3 scripts/quark_route2_shell_multiplicity_exact_shell_ratio_surface_boundary_2026_07_07.py
```

Current output on this tree:

```text
Surface-boundary worker
RETYPE=bounded_theorem
QUOTE-FIXES=verified
LOAD-BEARING: PASS=13 FAIL=0
CONTEXT-TIER (comparison-only; non-fatal)
CONTEXT: PASS=1 FAIL=0
exit-code separation self-test: context failures are non-fatal
full replay: PASS=observation-recorded CENTER line 133 before shell line 134
binary-float ratio: -14875335342499166/7417703850033121
decimal-string ratio: -4031967723697/2010572657265
printed agreement: -2.005382749600167
displayed residual: -10822409167/2010572657265
relative deviation: 10822409167/4021145314530
totals: shell=1 gap=1/6 PASS=13/0 NONFATAL=1/0
```
