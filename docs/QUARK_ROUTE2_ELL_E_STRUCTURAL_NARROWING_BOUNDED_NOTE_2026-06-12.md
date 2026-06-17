# Quark Route-2 ell_E Structural Narrowing Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Type:** bounded structural narrowing and sign-separation support.
Status authority: independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome.
**Primary runner:** [scripts/quark_route2_ell_e_structural_narrowing_bounded_2026_06_12.py](../scripts/quark_route2_ell_e_structural_narrowing_bounded_2026_06_12.py)
**Runner cache:** [logs/runner-cache/quark_route2_ell_e_structural_narrowing_bounded_2026_06_12.txt](../logs/runner-cache/quark_route2_ell_e_structural_narrowing_bounded_2026_06_12.txt)

No literature values, external citations, new comparator numbers, fitted
endpoint values, new axioms, or physical `kappa_EW` weighting rule are used.
The calculation restates repo-internal endpoint algebra and exact rational
constraints only.

Context pointers, not authority links: scripts/runner_cache.py,
docs/QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md,
docs/QUARK_ROUTE2_ENDPOINT_STEP_FREE_ACTIVE_BRANCH_SLOPES_BOUNDED_NOTE_2026-06-12.md.

## One-Hop Source Authorities

- [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  for the channelwise bright readout form, the endpoint algebra, and the
  `q_E`, `q_T`, `s_TE`, `c_TE` definitions.
- [S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md](S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md)
  for localization of readout ambiguity in the spatial prefactor while the
  time-channel factor is shared.
- [ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md)
  for the supplied registration/positivity frame: norm conditions do not
  select the E-row direction, while positivity gives a one-sided bound.
- [RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md)
  for the Record/Quantum boundary separating exact Fierz channel algebra from
  physical readout/weighting selection.
- [EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md)
  for the exact SU(`N_c`) singlet/adjoint Fierz channel fraction.
- [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md)
  for the typed-edge target `R_conn -> gamma_T(center)/gamma_E(center) =
  -R_conn`.
- [QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md](QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md)
  for the endpoint-algebra equivalence between the signed center ratio and
  the E-row slope once the T-side values are granted.

## Quote Anchors

The readout-map authority gives the channelwise form:

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

The same source gives the endpoint algebra:

```text
q_E = gamma_E(center)/gamma_E(shell) = 1 + (beta_E / alpha_E) / 6
q_T = gamma_T(center)/gamma_T(shell) = 1 + (beta_T / alpha_T) / 6
s_TE = gamma_T(shell)/gamma_E(shell)  = alpha_T / alpha_E
c_TE = gamma_T(center)/gamma_E(center) = s_TE * q_T / q_E.
```

The factor-rigidity authority puts the unresolved part in the spatial
prefactor:

```text
structurally localized in the spatial prefactor
```

The positivity authority states the structural reason:

```text
rho_E is the readout direction
```

and:

```text
Positivity ... Gives only the one-sided bound rho_E > -6
```

The source-domain bridge authority records the open signed-domain target:

```text
gamma_T(center) / gamma_E(center) = -R_conn
```

The center-ratio obstruction records the exact conditional target:

```text
c_TE = -F_adj = -8/9
```

The source-domain bridge authority states the color-side gap:

```text
The sign and endpoint orientation are not supplied by the color projection
```

The Record/Quantum boundary says:

```text
Count is not weight.
```

and:

```text
Record does not supply the missing readout context.
```

## Attack A: Structural Narrowing of ell_E

Write the E-row covector as

```text
ell_E = (alpha_E, beta_E).
```

On the endpoint scaling channel `w=(1,delta_A1)` with
`delta_A1(shell)=0` and `delta_A1(center)=1/6`, the E readouts are

```text
gamma_E(shell)  = alpha_E,
gamma_E(center) = alpha_E + beta_E/6.
```

The endpoint quotient is defined only when `alpha_E != 0`. In that domain,
scale cancels:

```text
rho_E := beta_E/alpha_E,
q_E   := gamma_E(center)/gamma_E(shell)
       = 1 + rho_E/6.
```

Therefore the endpoint-relevant E-row is not a free affine 2-covector. It is
a projective one-parameter direction plus a representative scale:

```text
ell_E ~ (1, rho_E).
```

The projective slope reduction `ell_E ~ (1, rho_E)` (equivalently
`rho_E = 6(q_E - 1)`, the slope/direction) is RESTATED from the supplied
positivity no-go [ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md)
(it already carries the projective-slope characterization); it is not derived
fresh here. Relative to the exact readout-map and S3-time factor-rigidity
notes, it makes the projective direction explicit, but it is not a selection of
`rho_E`.

The same supplied positivity frame (the cited positivity no-go, its one-sided
bound) gives, as a RESTATED result, the positivity range. With the positive
shell orientation `alpha_E > 0`, positive shell and center readouts require

```text
alpha_E > 0,
alpha_E + beta_E/6 > 0
```

equivalently

```text
rho_E > -6.
```

This one-sided bound is the cited positivity no-go's own result
(`ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08`,
line 79: "Positivity ... gives only the one-sided bound `rho_E > -6`, never a
unique value"), restated here; it is not a new derivation of this note. Thus
the residual structural family on the quotient surface is

```text
E_pos = { lambda*(1,rho_E) : lambda > 0, rho_E > -6 }.
```

If the optional partial-isometry/idempotency normalization is imposed, it
chooses a representative on each ray:

```text
ell_E = +/- (1,rho_E) / sqrt(1 + rho_E^2).
```

That fixes norm, not direction. The same `rho_E` freedom remains, now on the
positive projective interval `rho_E > -6`.

No cited symmetry ties `alpha_E` to `beta_E` or shell to center. The single
datum that pins the remaining family is any shell-vs-center distinguishing
input, for example:

```text
q_E        -> rho_E = 6(q_E - 1),
c_TE       -> q_E = (-5/3)/c_TE,  rho_E = 6((-5/(3 c_TE)) - 1),
rho_E      -> ell_E ~ (1,rho_E).
```

For the named target value:

```text
c_TE = -8/9
q_E  = 15/8
rho_E = 21/4.
```

This note does not derive that magnitude. It records the narrowed family in
which that magnitude would live.

## Attack B: Separating Sign From Magnitude

The exact Fierz authority supplies a positive channel-count fraction:

```text
F_adj = (N_c^2 - 1)/N_c^2.
```

At `N_c=3`, this is `8/9`. The Fierz dimension fraction has no minus sign.
The cited source-domain bridge authority explicitly separates that positive
color projection from the signed Route-2 endpoint orientation.

However, the sign of the Route-2 center ratio can be separated from its
magnitude inside the narrowed positive E-family. Grant the T-side values used
by the readout-map algebra:

```text
rho_T = beta_T/alpha_T = -1,
s_TE  = alpha_T/alpha_E = -2,
q_T   = 1 + rho_T/6 = 5/6.
```

For every `rho_E > -6`, positivity gives

```text
q_E = 1 + rho_E/6 > 0.
```

Therefore

```text
c_TE = gamma_T(center)/gamma_E(center)
     = s_TE q_T / q_E
     = (-2)(5/6)/q_E
     = -5/(3 q_E) < 0.
```

So the minus sign in a future typed bridge

```text
c_TE = -F_adj
```

is already forced at the endpoint-orientation level for the positive
Route-2 family. The magnitude remains open: sign-only gives the whole
interval `c_TE < 0`, not `c_TE = -8/9`.

### Falsifiers

All falsifiers are exact rational substitutions.

| Substitution | Result |
|---|---|
| Correct T orientation, positive E-center, `rho_E=0` | `q_E=1`, `c_TE=-5/3`; sign correct, magnitude not `8/9` |
| Correct T orientation, target E-center, `rho_E=21/4` | `q_E=15/8`, `c_TE=-8/9` |
| Wrong T orientation `s_TE=+2`, positive E-center | `c_TE>0`; wrong sign |
| Positivity violation `rho_E=-7` | `q_E=-1/6`, `c_TE=10`; wrong sign |
| Boundary `rho_E=-6` | `q_E=0`; center ratio undefined |
| Fierz fraction alone | `F_adj=8/9>0`; no signed endpoint ratio |

The falsifier is thus not a floating comparator. It is exact endpoint
arithmetic: wrong T orientation or violated E-center positivity flips or
destroys the sign.

## What Changed Relative To The Durable Prior Bank

This section measures against durable repo notes only: the exact readout-map
note, the S3-time factor-rigidity note, the cited positivity no-go, the
source-domain bridge no-go, the center-ratio obstruction, the Fierz
decomposition note, and the Record/Quantum boundary note.

RESTATED, not new here (attribution): the projective-slope reduction
`ell_E ~ (1, rho_E)` and the one-sided bound `rho_E > -6` are both already in
the supplied positivity no-go
`ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08`
(slope characterization; line 79 for the bound), and the endpoint algebra
`q_E = 1 + rho_E/6`, `c_TE = s_TE q_T / q_E` is in the exact readout-map and
center-ratio/source-domain bridge notes. This note RESTATES and PACKAGES
those, it does not derive them.

NET-NEW STRUCTURAL CONTENT of this note over that durable prior bank is exactly
two items:

1. THE CONSOLIDATED RESIDUAL OBJECT `E_pos = { lambda*(1,rho_E) : lambda > 0,
   rho_E > -6 }` — the prior notes did not state the
   projective-times-positive family as a single named residual.
2. THE SIGN-UNIVERSALITY UPGRADE (Attack B): this note upgrades sign
   compatibility to `c_TE < 0` for EVERY `rho_E > -6` (the whole positive
   family) under the granted Route-2 T orientation plus positive E-center
   readout — tying the sign to the (restated) positivity bound. The magnitude
   `|c_TE| = 8/9` remains open.

In short: Attack A (the projective slope and the `rho_E > -6` bound) is a
recap/packaging of prior source results; Attack B (the sign universality) is the
substantive advance.

## Residual Family

The current structural residual is one positive projective parameter:

```text
rho_E in (-6, infinity),
ell_E ~ (1,rho_E),
c_TE = -5/(3(1 + rho_E/6)).
```

The sign is fixed throughout that family:

```text
c_TE < 0.
```

The remaining open target is the shell-vs-center magnitude datum:

```text
rho_E = 21/4
```

or equivalently

```text
q_E = 15/8,
c_TE = -8/9,
typed bridge F_adj -> |c_TE| = F_adj on the Route-2 center ratio.
```

The physical EW-current route still also needs the withheld readout/weighting
rule before a channel count becomes a physical weighting statement.

## No-Go Discipline Gate

Freshness note: review-loop fetched `origin/main` and followed the current
repo no-go-discipline skill body. This section is not an audit verdict.

Narrow negative claim being stress-tested: the cited color/Fierz authorities
do not by themselves provide a signed typed Route-2 magnitude bridge. This is
not a claim against future source/readout theorems, owner-approved
conventions, or alternate endpoint primitives.

**N1 alternative routes.**

| Route | Marker | Result |
|---|---|---|
| Bright-class form | ATTEMPTED | Narrows a 4-row to channelwise `ell_E`, but leaves the projective slope. |
| Positivity/registration | ATTEMPTED | Positivity gives `rho_E>-6`; norm/idempotency fixes representative scale only. |
| Factor-rigidity/time | ATTEMPTED | The time factor is shared, so the remaining variation is in the spatial prefactor. |
| T-side orientation | ATTEMPTED | Derives `c_TE<0` on the positive E-family, but not `|c_TE|=8/9`. |
| Fierz dimension fraction | ATTEMPTED | Gives positive `F_adj`; no signed Route-2 endpoint map follows. |
| Physical weighting route | ATTEMPTED | The Record/Quantum boundary keeps physical readout/weighting separate. |
| Explicit typed bridge | OPEN TARGET | Supplying `F_adj -> c_TE=-F_adj` would pin `rho_E`; it is not supplied here. |

**N2 wall independence.**

Collapsed walls:

| Wall | Meaning | Relation |
|---|---|---|
| W1 | positive projective slope `rho_E` remains unselected | closed if W2 supplies `c_TE=-8/9` |
| W2 | typed color-to-Route-2 magnitude/domain bridge remains open | not closed by knowing `rho_E` unless the domain map is also supplied |
| W3 | physical EW-current readout/weighting selector remains separate | independent of W1/W2 if the proof routes through physical weighting |

**N3 hidden-wall scan.**

Load-bearing phrases are "positive", "orientation", "typed bridge",
"Record", and "weighting". Each is tied to a one-hop authority or to the exact
rational endpoint equations above. No hidden comparator, fitted value, or
physical weighting rule is introduced.

**N4 residual matching.**

| Witness | Residual in witness | Residual here | Match |
|---|---|---|---|
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | E-row direction remains in `rho_E` | same direction, narrowed to the positive projective family | yes |
| [ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md) | registration/positivity does not select `rho_E`; positivity gives only `rho_E>-6` | same non-selection, packaged as `E_pos` | yes |
| [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md) | source-domain typed bridge is missing | same magnitude/domain target; sign separated by endpoint orientation | yes |
| [QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md](QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md) | exact conditional algebra pins `rho_E=21/4` only after the signed center ratio is supplied | same conditional algebra; magnitude still open | yes |
| [RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md) | channel count is not physical weight | same physical weighting boundary | yes |

**N5 rhetoric audit.**

The negative statement is scoped to the cited Fierz/channel-count authorities
and the current Route-2 endpoint definitions. It does not say that every
possible color orientation theorem fails; it says that the cited channel-count
fraction is positive and does not itself supply the signed endpoint map.

**N6 partial-closure path scan.**

A future exact source-domain theorem, an explicit endpoint convention, or an
approved readout primitive could supply `F_adj -> c_TE=-F_adj` and then the
runner arithmetic would pin `rho_E=21/4`. This note keeps that as the named
next path and does not ask for a new axiom.

**N7 steelman.**

A reviewer could argue that the sign is already latent in the Route-2
T-channel orientation and therefore the missing bridge should be treated as a
magnitude/domain problem only. This note accepts the sign part under the
positive E-family and records exactly that sharpening. The remaining challenge
for that reviewer is to supply the typed equality of the magnitude with
`F_adj`, or an endpoint theorem that gives `q_E=15/8`.

**N8 cross-cycle echo.**

The same shape appears across the exact readout-map authority, the positivity
no-go, the source-domain bridge no-go, the center-ratio obstruction, and the
Record/Quantum color-trace boundary: endpoint algebra works after a
distinguishing shell-vs-center input is supplied, while count/registration/time
structure alone leaves the direction or magnitude unselected. This note narrows
that residual without changing the cited boundaries.

Checklist outcome: complete for this narrow bounded statement. This is not an
audit verdict.

## Verification

Run:

```bash
python3 scripts/quark_route2_ell_e_structural_narrowing_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=47, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/quark_route2_ell_e_structural_narrowing_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
