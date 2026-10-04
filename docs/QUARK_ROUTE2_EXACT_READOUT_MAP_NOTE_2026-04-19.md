# Quark Route-2 Exact Readout Map

**Type:** bounded_theorem
**Claim type:** bounded_theorem


**Date:** 2026-04-19  
**Status:** exact carrier/readout reduction plus exact missing-map obstruction  
**Primary runner:** `scripts/frontier_quark_route2_exact_readout_map.py`
**Runner cache:** `logs/runner-cache/frontier_quark_route2_exact_readout_map.txt`

**Replay-time repair (2026-06-17).** This runner consumes the fast endpoint
certificate replay from `frontier_quark_endpoint_readout_constraints.py`; the
same helper still exposes a full tensor replay opt-in for deep recomputation.


## Quantifier boundary (2026-10-04)

The all-site identity holds for the stated seven-site stencil inside a
Dirichlet box containing all six neighbours. Equality of centre and shell
readouts follows **only when every interpolation stencil avoids the origin**,
the anchor ignores it, and the required denominators are nonzero. Locality
alone does not force this: the six-point control touches the origin and leaks
the spike. The four-point counterexample refutes interpolation-independent
interpretation of the size-15 rationals; it does not select a physical
interpolation. The finite sampled ladder fails a plateau test. Any statement
below that it “does not converge” means that finite diagnostic only; an
asymptotic nonconvergence theorem is not supplied.

## Corrigendum (2026-09-30)

**What was wrong.** The triple `(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E)
= (-1, -2, 21/4)`, the ratio chain `{5/6, -2, -8/9}` and the "live endpoint-fixed
readout" of section 3 are presented as the target of a readout theorem. The
live values are size-15 outputs of a readout that interpolates the lattice
potential with a global cubic spline. The centre and shell sources give the same
potential at every site except the origin (difference exactly `1/6`), so the
`beta_T/alpha_T` and `beta_E/alpha_E` entries are the spline's ringing on that
spike; with a local interpolation both are `0` (`q_T = q_E = 1`) at every box
size, size 15 included.

**Corrected statement.** "Not derived" remains true, but for those two entries the
target is not a property of the field. The middle entry `alpha_T/alpha_E` is a
shell-only ratio and is not decided by this correction.

**What still stands.** The exact carrier/readout reduction, the endpoint
algebra of section 2, and the exact obstruction of section 4: `rho_E = 0` and
`rho_E = 21/4` are both admissible maps on the restricted class. The field
itself gives `rho_E = 0` under a local readout.

**Evidence.** The note `QUARK_ROUTE2_ENDPOINT_TRIPLE_CENTER_MINUS_SHELL_READOUT_IS_A_GLOBAL_CUBIC_SPLINE_ARTEFACT_ON_A_ONE_SITE_SPIKE_BOUNDED_THEOREM_NOTE_2026-09-30.md` proves the identity `phi(e0) - phi(s_unit) = delta_origin / 6` at every site and replays the readout with the interpolation swapped (checker `scripts/frontier_quark_route2_endpoint_triple_center_minus_shell_readout_cubic_spline_artefact_check_2026_09_30.py`, `TOTAL: PASS=24 FAIL=0`). Same-family checks (Claude Sonnet 5.5), no independent referee yet.

## Safe statement

The current branch now separates the Route-2 readout problem cleanly.

The exact bilinear carrier `K_R` and exact endpoint columns already force the
restricted bright readout class into the channelwise form

```text
gamma_E = alpha_E u_E + beta_E delta_A1 u_E
gamma_T = alpha_T u_T + beta_T delta_A1 u_T.
```

That exact reduction is real progress. But the current exact stack still does
**not** derive the endpoint ratio chain

```text
{5/6, -2, -8/9} -> 15/8 -> r_E = 21/4 -> D_E = 21/8.
```

Equivalently, it still does not derive the exact dimensionless readout triple

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4).
```

So the honest endpoint is:

- exact carrier/readout reduction on the restricted class,
- exact endpoint algebra for the ratio chain,
- and an exact missing-map obstruction rather than an exact readout theorem.

## 1. Exact carrier/readout setup

On the live support surface:

```text
delta_A1(e0)        = 1/6
delta_A1(s/sqrt(6)) = 0
```

and the exact carrier columns are

```text
E-shell  = (1, 0, 0,   0)
E-center = (1, 0, 1/6, 0)
T-shell  = (0, 1, 0,   0)
T-center = (0, 1, 0, 1/6).
```

Those four columns span a direct sum of disjoint `E` and `T` endpoint
subspaces. So any admissible bright-preserving linear readout on this
restricted class must reduce to one `E` map and one `T` map:

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

The runner then recomputes the live bounded endpoint values directly from the
current modules and confirms that the endpoint-fixed map reproduces them
exactly on this class.

## 2. Exact endpoint algebra

Once the readout is reduced to `P_R`, the endpoint ratios are algebraic:

```text
q_T   := gamma_T(center) / gamma_T(shell) = 1 + (beta_T / alpha_T) / 6
q_E   := gamma_E(center) / gamma_E(shell) = 1 + (beta_E / alpha_E) / 6
s_TE  := gamma_T(shell) / gamma_E(shell)  = alpha_T / alpha_E
c_TE  := gamma_T(center) / gamma_E(center) = s_TE * q_T / q_E.
```

So the target ratio chain

```text
q_T = 5/6,  s_TE = -2,  c_TE = -8/9
```

is exactly equivalent to

```text
beta_T / alpha_T = -1
alpha_T / alpha_E = -2
beta_E / alpha_E = 21/4.
```

This is the key compression of the theorem target.

## 3. Theorem attempt on the live surface

The live endpoint-fixed readout is

```text
beta_T / alpha_T = -1.000030814262
alpha_T / alpha_E = -2.005382749600
beta_E / alpha_E =  5.257476782081
```

and therefore

```text
q_T  = 0.833328197623
s_TE = -2.005382749600
c_TE = -0.890683778231.
```

So the exact readout theorem does **not** land on the current surface.

The important point is that this is no longer a vague “bad fit.” The branch
now knows precisely what theorem would be needed, and exactly which readout
ratios would have to be proved.

## 4. Smallest exact obstruction

The new runner then proves the smallest exact obstruction.

If the two `T`-side candidates are granted exactly,

```text
beta_T / alpha_T = -1
alpha_T / alpha_E = -2,
```

then the entire remaining readout theorem collapses to one exact map entry:

```text
beta_E / alpha_E = 21/4.
```

This is seen directly on the reduced exact family

```text
P(rho_E) = [[1, 0, rho_E, 0],
            [0, -2, 0, 2]].
```

All such maps agree on the shell `E` normalization, but the center `E` lift is

```text
1 + rho_E / 6.
```

So `rho_E = 0` and `rho_E = 21/4` are both exact admissible maps on the
restricted carrier class, but they produce different center `E` readouts.

That is the theorem-grade obstruction:

> the exact carrier and exact endpoint algebra do not yet fix the readout map
> uniquely; the irreducible missing map entry is the `E`-channel ratio
> `beta_E / alpha_E`.

## Honest endpoint

The current Route-2 readout status is now:

- exact bilinear carrier `K_R`: already present,
- exact restricted readout reduction: closed,
- exact endpoint ratio theorem: not derived,
- smallest exact missing map entry: `beta_E / alpha_E = 21/4` after the
  `T`-side candidates are granted.

That is the right theorem endpoint for this block.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
```

Current expected result on this branch:

- `frontier_quark_route2_exact_readout_map.py`: `PASS=11 FAIL=0`
