# Quark Route-2 T-Side Endpoint Theorem Attempt

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Assessment role:** bounded derivation attempt with named obstruction.
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict. Effective status is
pipeline-derived after independent audit and dependency closure.
**Primary runner:** [scripts/quark_route2_t_side_endpoint_theorem_attempt_bounded_2026_06_12.py](../scripts/quark_route2_t_side_endpoint_theorem_attempt_bounded_2026_06_12.py)
**Runner cache:** [logs/runner-cache/quark_route2_t_side_endpoint_theorem_attempt_bounded_2026_06_12.txt](../logs/runner-cache/quark_route2_t_side_endpoint_theorem_attempt_bounded_2026_06_12.txt)

## Scope

This note tests the first two entries of the s3-time checkpoint target

```text
beta_T / alpha_T = -1,
alpha_T / alpha_E = -2.
```

The result is a localization finding. The cited Route-2 carrier/time
surface reproduces both values exactly once the candidate readout row is
supplied, but the cited surface does not derive that row. The obstructed
step is:

```text
exact carrier columns plus exact slice factor
    -> selected readout row P_R with (alpha_E, alpha_T, beta_T) = (1, -2, 2).
```

The time-coupling authority is exact after `P_R` is supplied; it does not
select `P_R`.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md) | Exact conditional family `Xi_P(t ; c) = (P_R c) otimes V_R(t)` and its explicit dependence on supplied `P_R` |
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | Definitions of `gamma_E`, `gamma_T`, `P_R`, and endpoint algebra |
| [S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md) | Class-A carrier definition and endpoint-fitted status of the old coefficient readout |
| [QUARK_ENDPOINT_READOUT_CONSTRAINTS_NOTE_2026-04-19.md](QUARK_ENDPOINT_READOUT_CONSTRAINTS_NOTE_2026-04-19.md) | Affine coefficient definitions and live endpoint-fit boundary |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Parent row saying the missing readout-map endpoint triple is the theorem target |
| [S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md](S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md) | Factor-rigidity: time-axis structure is universal across supplied readout maps |
| [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) | E-center freedom after granting T-side candidates; used only to separate the sibling E-lift |
| [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) | Record boundary: no readout context, weighting, or normalization rule |
| [QUARK_ROUTE2_ENDPOINT_STEP_FREE_ACTIVE_BRANCH_SLOPES_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_ENDPOINT_STEP_FREE_ACTIVE_BRANCH_SLOPES_BOUNDED_NOTE_2026-06-12.md) | Bounded comparator firewall for live active-branch endpoint slopes; not used as theorem input |

Non-authority implementation pointers: scripts/quark_route2_t_side_endpoint_theorem_attempt_bounded_2026_06_12.py; scripts/runner_cache.py.

## Quote Anchors

The time-coupling note starts the exact family with the phrase "Given any
admissible readout map `P_R`" and later says the missing piece is a theorem
selecting one unique `P_R`. The exact-readout note defines

```text
gamma_E = alpha_E u_E + beta_E delta_A1 u_E
gamma_T = alpha_T u_T + beta_T delta_A1 u_T
```

and the restricted row form

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

The bilinear primitive note says the old coefficients are fixed by endpoint
values from the old `eta_floor_tf` pipeline and calls that readout
"endpoint-fitted, not first-principles". The minimal axiom note says Record
supplies no readout context and no weighting or normalization rule.

## Definitions Traced

On the restricted carrier columns, the exact-readout authority gives

```text
E-shell  = (1, 0, 0,   0)
E-center = (1, 0, 1/6, 0)
T-shell  = (0, 1, 0,   0)
T-center = (0, 1, 0, 1/6).
```

Therefore, for any supplied row coefficients,

```text
gamma_T(shell)  = alpha_T
gamma_T(center) = alpha_T + beta_T / 6
gamma_E(shell)  = alpha_E
```

and

```text
rho_T = beta_T / alpha_T
q_T   = gamma_T(center) / gamma_T(shell) = 1 + rho_T / 6
s_TE  = gamma_T(shell) / gamma_E(shell) = alpha_T / alpha_E.
```

These formulas are exact endpoint algebra. They are not, by themselves, a
selector for the coefficients.

## Target One: rho_T

If the candidate T row is supplied as

```text
alpha_T = -2,
beta_T  =  2,
```

then exact rational arithmetic gives

```text
rho_T = beta_T / alpha_T = 2 / (-2) = -1,
q_T = 1 + rho_T / 6 = 1 - 1/6 = 5/6.
```

This is an exact conditional reproduction of the target. The obstruction is
the previous line: the cited exact time-coupling family starts after `P_R` is
chosen. The T carrier column `(0, 1, 0, delta_A1)` and the common time factor
`V_R(t)` do not choose `beta_T = -alpha_T`.

Exact counter-witness on the same carrier/time structure:

```text
alpha_T = -2, beta_T = 0
rho_T = 0, q_T = 1.
```

This row is still a channelwise restricted readout row. It breaks the target
without changing the carrier columns or the slice factor.

## Target Two: s_TE

If the candidate shell normalization is supplied as

```text
alpha_E = 1,
alpha_T = -2,
```

then exact rational arithmetic gives

```text
s_TE = alpha_T / alpha_E = -2.
```

Again, the value is reproduced exactly after the row is supplied. The sign is
the relative orientation sign between the T shell row and the E shell row. The
magnitude is the relative shell scale `|alpha_T| / |alpha_E|`. Neither is
fixed by the exact carrier columns, because the E and T shell columns occupy
disjoint coordinates with unit carrier entries.

Exact counter-witnesses on the same carrier/time structure:

```text
alpha_E = 2, alpha_T = -2, beta_T = 2
rho_T = -1, q_T = 5/6, s_TE = -1.

alpha_E = 1, alpha_T = 2, beta_T = -2
rho_T = -1, q_T = 5/6, s_TE = +2.
```

The first changes the magnitude while preserving the T-side shape. The second
changes the sign while preserving the T-side shape. Thus both the sign and
magnitude of `s_TE` are row-normalization data unless a further readout-row
selector is supplied.

## Exact Falsifiers

All values in this section are checked by the runner with `fractions.Fraction`.

| Test | Wrong substitution | Exact falsifier value |
| --- | --- | --- |
| Wrong center gap/dimension | Use `delta_center = 1/5` with the supplied T row | `q_T = 4/5`, not `5/6` |
| Wrong center gap/dimension | Invert `q_T = 5/6` through `delta_center = 1/5` | `rho_T = -5/6`, not `-1` |
| Wrong channel pairing | Reuse the E-center lift `beta = 21/4` as `beta_T` with `alpha_T = -2` | `rho_T = -21/8`, `q_T = 9/16` |
| Wrong shell pairing | Swap the shell quotient | `alpha_E/alpha_T = -1/2`, not `-2` |
| Wrong shell orientation | Use `alpha_T = +2`, `beta_T = -2`, `alpha_E = 1` | `rho_T = -1`, `q_T = 5/6`, but `s_TE = +2` |
| Wrong color dimension route | Use `N_c = 2` in `F_adj = (N_c^2 - 1)/N_c^2` | `F_adj = 3/4`; if forced into `c_TE = -F_adj`, it gives `rho_E = 22/3`, not `21/4` |

The color-dimension falsifier is included only to block a cross-channel
shortcut: color `F_adj` is a center-ratio candidate, not a shell-normalization
selector for `alpha_T/alpha_E`.

## Bounded Comparator Evidence Not Used

The live endpoint and active-branch notes remain comparator evidence only. The
step-free active-branch note reports

```text
|b_T/a_T| = 1.000030809474.
```

That value is not used above. It is a bounded live-surface number for the
implemented eta-floor envelope, not an exact symbolic coefficient theorem and
not a source for fitting `rho_T = -1`.

## Negative-Claim Discipline Checklist

This section records the N1-N8 stress test for the scoped obstruction:
"the cited exact carrier/time surface does not itself select the candidate
readout row `P_R`." It does not rule out a future readout-row theorem,
owner-approved convention, or other source-domain selector.

**N1 alternative routes.**

| Route | Attempt | Result |
| --- | --- | --- |
| Carrier-column route | Read `rho_T` and `s_TE` from the exact endpoint columns. | ATTEMPTED: columns give `(0,1,0,delta_A1)` for T and `(1,0,delta_A1,0)` for E; row coefficients remain external to the columns. |
| Time-factor route | Use `Xi_P(t;c)` and factor rigidity to select the T row. | ATTEMPTED: the time factor is common after `P_R` is supplied and cancels from shell/center ratios. |
| Endpoint-algebra route | Use `q_T = 5/6` and `s_TE = -2` to infer coefficients. | ATTEMPTED: exact, but starts by granting the endpoint targets rather than deriving the row. |
| Bilinear primitive route | Treat the old eta-floor coefficients as the row selector. | RULED OUT BY PRIOR for this packet: the cited primitive labels that readout endpoint-fitted, not first-principles. |
| Record/primitive shortcut | Treat Record or approved primitives as normalization suppliers. | RULED OUT BY PRIOR for this packet: cited axiom/registry text excludes readout context and normalization grants. |
| Live comparator route | Fit to live endpoint or active-branch numbers. | ATTEMPTED only as comparator firewall; the exact proof above does not use those values. |

**N2 wall independence.**

| Wall | Meaning | Independent witness |
| --- | --- | --- |
| W1 | Missing T-row shape selector `beta_T = -alpha_T`. | `alpha_T=-2, beta_T=0` keeps `s_TE=-2` but gives `rho_T=0`. |
| W2 | Missing E/T shell normalization selector `alpha_T/alpha_E=-2`. | `alpha_E=2, alpha_T=-2, beta_T=2` keeps `rho_T=-1` but gives `s_TE=-1`. |

W1 and W2 are independent on the restricted readout algebra. Closing one does
not automatically close the other.

**N3 hidden-wall scan.**

The loaded phrases are "given", "supplied", "candidate", "normalization",
"Record", and "primitive". "Given" and "supplied" are used only for explicit
`P_R` rows. "Candidate" marks the row being tested. "Record" and "primitive"
are cited to the minimal axiom and primitive registry boundaries. No hidden
coefficient selector is promoted.

**N4 residual matching.**

| Witness | Witness residual | Current residual | Match |
| --- | --- | --- | --- |
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | endpoint triple not derived by exact carrier/readout reduction | same endpoint-row selector, first two entries isolated | yes |
| [QUARK_ENDPOINT_READOUT_CONSTRAINTS_NOTE_2026-04-19.md](QUARK_ENDPOINT_READOUT_CONSTRAINTS_NOTE_2026-04-19.md) | endpoint values fix coefficients, but do not derive exact coefficient law | same coefficient-selector residual | yes |
| [S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md](S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md) | factor rigidity does not derive readout triple | same `P_R` selector residual | yes |
| [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) | E-center lift remains free after T-side candidates | sibling residual, used only to separate E lift from T-side rows | yes, separated |

**N5 rhetoric audit.**

The negative claim is only about the cited restricted Route-2 carrier/time
surface and the row coefficients defined above. It is not a claim about all
Route-2 routes, all source-domain rules, or future conventions.

**N6 partial-closure path scan.**

A future source note, explicit convention, or owner-approved readout primitive
could supply the missing row selector. The approved premise registry was
checked: `scale_reference_primitive`, `kinetic_isotropy_primitive`, and
`realized_state_primitive` do not grant readout bridges or normalization rules.

**N7 steelman.**

A reviewer could argue that the exact T-side object is not merely the carrier
column, but the physically intended eta-floor readout row; under that reading,
the near-unit T balance should be promoted to `beta_T = -alpha_T` and paired
with the natural two-channel shell orientation. The strongest support is the
bounded active-branch endpoint note, which shows the implemented T balance is
step-free and stable near `1`. The counterpoint is scope: that note explicitly
does not claim a closed form or endpoint-triple derivation, and the exact
time-coupling authority still starts after `P_R` is supplied.

**N8 cross-cycle echo.**

Similar residuals appear in the exact readout-map note, endpoint-constraints
note, s3-time parent note, and factor-rigidity addendum. None of those cited
surfaces is retired by a convention that selects the specific row
`(alpha_E, alpha_T, beta_T) = (1, -2, 2)`.

Checklist result: completed for this scoped obstruction; no methodology
failure condition was triggered. This is not an audit verdict.

## Boundary

This note does not establish:

- a unique exact `P_R`;
- a physical readout context or normalization rule;
- the E-center lift `beta_E/alpha_E = 21/4`;
- a color-projection bridge to `c_TE`;
- a discharge of the s3-time gate;
- any audit verdict.

It records that the first two target values are exact after the candidate
readout row is supplied, while the current cited carrier/time surface leaves
that row as the named open target.

## Verification

Run:

```bash
python3 scripts/quark_route2_t_side_endpoint_theorem_attempt_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=25, FAIL=0
```

Cache regeneration:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/quark_route2_t_side_endpoint_theorem_attempt_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
