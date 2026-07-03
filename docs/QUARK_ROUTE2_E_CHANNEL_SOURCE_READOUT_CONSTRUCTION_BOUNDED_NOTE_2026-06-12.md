# Quark Route-2 E-Channel Source/Readout Construction Attempt

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived
after independent audit and dependency closure.
**Primary runner:** [`scripts/quark_route2_e_channel_source_readout_construction_bounded_2026_06_12.py`](../scripts/quark_route2_e_channel_source_readout_construction_bounded_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/quark_route2_e_channel_source_readout_construction_bounded_2026_06_12.txt`](../logs/runner-cache/quark_route2_e_channel_source_readout_construction_bounded_2026_06_12.txt)
**No-promotion statement:** This source note records a conditional localized
construction attempt only; it creates no promotion, no registry edit, and no
audit verdict.

## Scope

This note attempts the W73 construction. It does not re-name the W69
obstruction; it mirrors the T-channel exact-time-coupling template and asks
which E-channel source/readout objects are actually present in the cited bank.

Allowed inputs are repo-internal source notes, exact rational arithmetic, and
the already declared Route-2 endpoint definitions. No observed masses, fitted
Yukawa entries, CKM/J target minimization, nearest-rational selection from live
endpoint values, external citation, new axiom, new comparator number, or
physical `kappa_EW` weighting rule is used.

Context pointers, not authority links: .claude/tmp/refs/W69_NOTE.md,
.claude/tmp/refs/W71_NOTE.md, scripts/runner_cache.py.

## One-Hop Authorities

| Authority | Role used here |
|---|---|
| [QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md) | Conditional family `Xi_P(t ; c) = (P_R c) tensor V_R(t)` once `P_R` is supplied |
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | Restricted readout row form and endpoint algebra for `alpha`, `beta`, `q`, and `c_TE` |
| [TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md](TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md) | Exact support-side endpoint values `delta_A1(center)=1/6`, `delta_A1(shell)=0` |
| [S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md) | Definition of `K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T)` under named inputs |
| [S3_TIME_BILINEAR_TENSOR_PRIMITIVE_RANK1_FACTORIZATION_NOTE_2026-05-17.md](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_RANK1_FACTORIZATION_NOTE_2026-05-17.md) | Rank-1 factorization `K_R = w v^T`, separating scaling channel `w=(1,delta_A1)` from bright channel |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Parent s3-time row naming the readout endpoint triple as the upstream theorem target |
| [S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md](S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md) | Readout ambiguity is localized in the spatial prefactor; the time factor is shared |
| [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) | Boundary that `rho_E` remains free unless an extra E-center endpoint ratio, source-domain rule, or readout primitive is supplied |
| [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md) | Typed-edge inventory for the color/support bridge attempt |
| [QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md](QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md) | Conditional algebra if `c_TE = -R_conn` is supplied |
| [RCONN_DERIVED_NOTE.md](RCONN_DERIVED_NOTE.md) | Algebraic SU(`N_c`) adjoint channel count `F_adj = (N_c^2 - 1)/N_c^2` |
| [RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md) | Scope boundary separating algebraic channel count from physical weighting/readout selection |
| [ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md) | Registration/positivity frame leaves the readout direction free |
| [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) | Record/Quantum boundary: no readout context, weighting, normalization, probability, dynamics, or observable bridge is supplied |

## Quote Anchors

The time-coupling authority starts after a supplied readout map: "Given any
admissible readout map `P_R`". The exact readout authority defines the row
form

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

The E-channel naturality boundary gives the escape clause: `rho_E` stays free
unless an additional E-center endpoint ratio, source-domain rule, or readout
primitive is supplied. The `Rconn/kappa_EW` boundary supplies the physical
firewall: count is not weight, and Record does not supply the missing readout
context.

## Structural Mirror

The T-channel template has four exact pieces:

| Template ingredient | T-side object | E-channel analog present? | Construction result |
|---|---|---|---|
| Scaling/source channel | `w_shell=(1,0)`, `w_center=(1,1/6)` | yes, same `w` | common support channel computed exactly |
| Bright channel | `u_T` | yes, `u_E` | channel label present, but not a row selector |
| Readout covector | `ell_T=(alpha_T,beta_T)` | form yes; value not selected | supplying `ell_T=(-2,2)` gives `rho_T=-1` |
| Slice evolution | `V_R(t)=exp(-t Lambda_R)u_*` | yes, same `V_R(t)` | exact conditional family for every supplied row |

The mirror makes the decisive point concrete. The current source bank supplies
the scaling channel and the slice evolution. It does not supply the E-channel
covector

```text
ell_E = (alpha_E, beta_E)
```

or a typed rule selecting its slope `beta_E/alpha_E`.

Using the rank-1 carrier notation, endpoint readout is simply covector
evaluation on the scaling channel:

```text
gamma_X(shell)  = ell_X dot (1,0)     = alpha_X,
gamma_X(center) = ell_X dot (1,1/6)   = alpha_X + beta_X/6.
```

Thus the T-side supplied row

```text
ell_T = (-2,2)
```

reproduces

```text
rho_T = beta_T/alpha_T = -1,
q_T = gamma_T(center)/gamma_T(shell) = 5/6.
```

The E-channel target would require, up to nonzero common scale,

```text
ell_E = (1,21/4),
q_E = gamma_E(center)/gamma_E(shell) = 15/8.
```

This row is not produced by the carrier or time factor. It is the exact
source/readout covector selection still needed by this construction.

## Exact Conditional Construction

Grant the T-side values used by the checkpoint:

```text
beta_T/alpha_T = -1,
alpha_T/alpha_E = -2.
```

Then exact rational arithmetic gives

```text
q_T = 1 + (-1)/6 = 5/6,
s_TE = gamma_T(shell)/gamma_E(shell) = -2.
```

For arbitrary E-row slope `rho_E = beta_E/alpha_E`,

```text
q_E = 1 + rho_E/6,
c_TE = gamma_T(center)/gamma_E(center)
     = s_TE q_T / q_E.
```

If a typed E-center source/readout bridge supplies

```text
c_TE = -8/9,
```

then

```text
q_E = (-2)(5/6)/(-8/9) = 15/8,
rho_E = 6(15/8 - 1) = 21/4.
```

Equivalently, if the color route supplies the typed signed bridge

```text
F_adj(N_c=3) = 8/9  ->  c_TE = -F_adj,
```

the same exact arithmetic returns `rho_E = 21/4`. The present bank supplies
`F_adj` as algebraic color-channel count. It does not supply the typed signed
Route-2 center-ratio bridge.

## Algebraic Edge Versus Physical Weighting

This note keeps two steps separate.

The algebraic edge is:

```text
F_adj = (N_c^2 - 1)/N_c^2.
```

At `N_c=3`, this is `8/9`. That number can be used in exact falsifier
arithmetic as a channel-count fraction.

The physical weighting/readout edge is different:

```text
R_phys(kappa_EW) = F_adj + kappa_EW(1 - F_adj).
```

Selecting the connected-trace specialization `kappa_EW=0` is not supplied by
Record or Quantum. The construction here does not use `kappa_EW=0` as a proof
input. If a future route attempts to turn color trace algebra into a physical
EW-current readout, the named withheld step is the physical readout/weighting
rule. The narrower Route-2 algebraic bridge still also needs the typed sign
and domain map `F_adj -> c_TE = -F_adj`.

## Wrong-Structure Falsifiers

All entries below are exact rational substitutions.

| Substitution | Exact result |
|---|---|
| Correct support denominator `6`, `N_c=3`, and supplied signed bridge | `F_adj=8/9`, `q_T=5/6`, `q_E=15/8`, `rho_E=21/4` |
| Wrong color count `N_c=2`, denominator `6` | `F_adj=3/4`, `q_E=20/9`, `rho_E=22/3` |
| Wrong support denominator `5`, `N_c=3` | `q_T=4/5`, `q_E=9/5`, `rho_E=4` |
| Wrong support denominator `12`, `N_c=3` | `q_T=11/12`, `q_E=33/16`, `rho_E=51/4` |
| Wrong bridge sign `c_TE=+8/9` | `q_E=-15/8`, `rho_E=-69/4` |
| No E-center lift `rho_E=0` | `q_E=1`, `c_TE=-5/3` |
| Same-slope reuse `rho_E=rho_T=-1` | `q_E=5/6`, `c_TE=-2` |

These falsifiers show that the target is not produced by free pattern matching
to `6` or `8/9`. It appears in this construction only when the support
denominator, the supplied T-side row, and the signed typed center bridge are
all present.

## Outcome

Outcome: localized construction.

The construction reaches the exact scaling-channel covector problem:

```text
derive ell_E such that ell_E dot (1,1/6) / ell_E dot (1,0) = 15/8.
```

Equivalently, through the strongest visible color route, derive the typed
signed bridge

```text
F_adj(N_c=3) -> c_TE = gamma_T(center)/gamma_E(center) = -F_adj.
```

The cited algebraic ingredients present in the current bank are the support
endpoint scalar `delta_A1`, the rank-1 carrier factorization, the conditional
time factor, the restricted row form, endpoint algebra, and the SU(`N_c`)
channel-count fraction. The withheld ingredient is the source/readout rule
that selects the E-channel covector, or, on the physical color route, the
readout/weighting rule that turns channel count into the signed Route-2 center
ratio.

If that typed source/readout bridge is supplied later, the exact arithmetic in
this note makes the E-channel value immediate and opens the source-domain
bypass named by the reachability notes; this sentence is conditional on that
bridge being independently supplied.

## How This Differs From W69 And The Naturality Boundary

W69 named the missing theorem. This note performs the construction pass through
the T template and localizes the missing object as a covector on the scaling
channel `w=(1,delta_A1)`, with `V_R(t)` already factored out.

The 2026-04-28 naturality boundary tested carrier linearity, shell
normalization, T-side transfer, low-rational naturality, and endpoint-chain
rewrites. This note instead follows the source/readout construction route:
rank-1 carrier factorization -> row covector evaluation -> conditional center
bridge arithmetic -> physical-weighting firewall.

Comparator rows such as
docs/QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md
and
docs/QUARK_ROUTE2_ENDPOINT_STEP_FREE_ACTIVE_BRANCH_SLOPES_BOUNDED_NOTE_2026-06-12.md
are not proof inputs here. They remain separate bounded comparator context.

## No-Go Discipline Gate

Scoped negative claim: the construction above does not derive the E-channel
row from the cited current bank; it localizes the remaining link to the typed
source/readout bridge or, on the physical color route, to the withheld
readout/weighting rule. This is not a claim about every future source theorem.

**N1 alternative routes.**

| Route | Marker | Result |
|---|---|---|
| Direct carrier covector route | ATTEMPTED | `K_R=w v^T` supplies `w`, not `ell_E` |
| Time-factor route | ATTEMPTED | `V_R(t)` is common and cancels from endpoint ratios |
| T-row mirror route | ATTEMPTED | Supplying `ell_T=(-2,2)` reproduces T data; the template does not select `ell_E` |
| Endpoint algebra route | ATTEMPTED | Exact after `q_E=15/8` or `c_TE=-8/9` is supplied |
| Algebraic color route | ATTEMPTED | `F_adj=8/9` is present; the typed sign/domain bridge to Route-2 `c_TE` is not supplied |
| Physical weighting route | ATTEMPTED | `kappa_EW=0` is withheld by the current Record/Quantum boundary |
| Registration/positivity route | RULED OUT BY PRIOR | Norm/sign constraints leave the E-row direction free |

**N2 wall independence.**

Collapsed walls:

| Wall | Meaning |
|---|---|
| W1 | Missing E-channel row covector selection `ell_E` on `w=(1,delta_A1)` |
| W2 | Missing typed signed bridge `F_adj -> c_TE=-F_adj` if the color path is used |
| W3 | Missing physical readout/weighting selector `kappa_EW=0` if the proof is routed through physical EW-current weighting |

W2 would compute W1 through endpoint algebra under the granted T-side values,
but would not by itself supply W3. W3 would still need a typed Route-2 sign and
domain map before it becomes `c_TE`. W1 is the direct E-row target.

**N3 hidden-wall scan.**

Loaded phrases were "supplied", "typed", "bridge", "physical", "Record",
"conditional", and "source/readout". Each is tied to an explicit authority
above. No hidden E-row covector, endpoint quotient, or physical weighting rule
is introduced.

**N4 residual matching.**

| Witness | Witness residual | Current residual | Match |
|---|---|---|---|
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | endpoint readout row not uniquely selected | same E-row slope | yes |
| [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) | `rho_E` free without extra E-center/source/readout input | same E-center lift | yes |
| [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md) | missing typed `R_conn` to Route-2 center-ratio edge | same color-path bridge | yes |
| [RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md) | channel count does not supply physical weighting/readout | same physical route boundary | yes |

**N5 rhetoric audit.**

The negative phrase is scoped to this cited bank and this construction. It is
not a lattice-wide impossibility claim and not a claim against a future typed
source/readout theorem, convention, or owner-approved admission.

**N6 partial-closure path scan.**

A future exact tensor endpoint theorem, a typed color/support source theorem,
or an explicit approved readout convention could supply the missing bridge
without changing the axioms. This note does not classify that future path as a
new axiom.

**N7 steelman.**

The strongest counter-route is that the measured E-center calibration has
already located the correct stack functional: the exact infinite-volume limit
of that functional may produce `q_E=15/8`, after which this note's covector
condition is immediately satisfied. This note leaves that as a concrete next
calculation, not as comparator evidence upgraded into a derivation.

**N8 cross-cycle echo.**

Similar residuals appear in the exact readout-map, source-domain bridge,
record/positivity, and s3-time rows: conditional arithmetic works after a
distinguishing input is supplied, while the present bank does not supply that
input. This note preserves that split.

Gate result: PASS for the scoped localized construction result. This is not
an audit verdict.

## Boundary

This note does not establish:

- a direct derivation of `rho_E = 21/4`;
- a direct derivation of `q_E = 15/8`;
- a direct derivation of `ell_E = (1,21/4)`;
- a typed derivation of `gamma_T(center)/gamma_E(center) = -F_adj`;
- a physical `kappa_EW` weighting selector;
- quark-mass or CKM/J target closure;
- any audit verdict.

It records that the E-channel construction reaches an exact, named
source/readout covector bridge. Once that bridge is supplied, the downstream
arithmetic is exact and structure-sensitive.

## Verification

Run:

```bash
python3 scripts/quark_route2_e_channel_source_readout_construction_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=37, FAIL=0
```

Regenerate cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/quark_route2_e_channel_source_readout_construction_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
