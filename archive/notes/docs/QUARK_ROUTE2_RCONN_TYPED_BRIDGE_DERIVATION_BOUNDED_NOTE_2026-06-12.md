# Quark Route-2 Rconn Typed Bridge Derivation Bounded Note

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived
after independent audit and dependency closure.
**Primary runner:** [scripts/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.py](../scripts/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.py)
**Runner cache:** [logs/runner-cache/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.txt](../logs/runner-cache/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.txt)

## Scope

This note tests the W67 bridge target named by the s3-time checkpoint:

```text
R_conn -> gamma_T(center)/gamma_E(center) = -R_conn = -8/9.
```

The bridge edge, as named by the source-domain bridge packet, must assert:

```text
R_conn = (N_c^2 - 1) / N_c^2
    ?=> gamma_T(center) / gamma_E(center) = -R_conn.
```

Allowed inputs are repo-internal notes only. No literature values, new axioms,
external citations, fitted comparator numbers, observed quark masses, CKM/J
targets, nearest-rational selectors, or new physical weighting rules are used.

## One-Hop Authorities

| Authority | Role used here |
|---|---|
| [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md) | W9 typed-edge inventory, missing bridge definition, and reachability machinery |
| [RCONN_DERIVED_NOTE.md](RCONN_DERIVED_NOTE.md) | Declares the exact `F_adj = (N_c^2 - 1)/N_c^2 = 8/9` support and the connected-trace/readout boundary |
| [RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md) | Separates exact Fierz algebra from the withheld physical `kappa_EW` readout/weighting selector |
| [EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md) | Exact SU(`N_c`) singlet/adjoint Fierz channel algebra and dimension fraction |
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | Definitions of `gamma_E`, `gamma_T`, endpoint ratios, and the reduced readout family |
| [QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md) | Confirms the exact time-coupling family remains conditional on a supplied `P_R` |
| [S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md) | Defines the support-side carrier `K_R` under named admitted inputs |
| [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) | Endpoint equivalence `rho_E = 21/4 <=> q_E = 15/8 <=> c_TE = -8/9` under granted T-side values |
| [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) | Record/Quantum boundary: no readout context, weighting, probability, dynamics, or physical observable bridge |

Non-authority implementation pointers:
[scripts/frontier_quark_route2_source_domain_bridge_no_go.py](../scripts/frontier_quark_route2_source_domain_bridge_no_go.py);
[scripts/runner_cache.py](../scripts/runner_cache.py).

## Definitions Being Tested

The Route-2 readout-map authority defines the restricted center objects by

```text
gamma_E = alpha_E u_E + beta_E delta_A1 u_E
gamma_T = alpha_T u_T + beta_T delta_A1 u_T.
```

On the endpoint columns,

```text
q_T  = gamma_T(center)/gamma_T(shell) = 1 + (beta_T/alpha_T)/6
q_E  = gamma_E(center)/gamma_E(shell) = 1 + (beta_E/alpha_E)/6
s_TE = gamma_T(shell)/gamma_E(shell)  = alpha_T/alpha_E
c_TE = gamma_T(center)/gamma_E(center) = s_TE q_T / q_E.
```

After granting the T-side stretch values,

```text
beta_T/alpha_T = -1,
alpha_T/alpha_E = -2,
q_T = 5/6,
s_TE = -2.
```

The E-side readout remains

```text
rho_E := beta_E/alpha_E,
q_E = 1 + rho_E/6,
c_TE = (-2)(5/6) / (1 + rho_E/6).
```

The Fierz authority supplies a separate color-channel identity:

```text
F_adj = dim(adj) / dim(N_c x N_c-bar) = (N_c^2 - 1)/N_c^2.
```

At `N_c = 3`, `F_adj = 8/9`. This is an exact channel-count fraction. It is
not, by itself, a definition of `rho_E`, `q_E`, `gamma_E`, `gamma_T`, or the
orientation sign of the Route-2 center ratio.

## Derivation Attempt

Start with the exact Fierz algebra:

```text
Tr_color[G G^dagger] = S + C,
S = (1/N_c) |Tr G|^2,
C = 2 sum_A |Tr[G t^A]|^2,
F_adj = dim(adj)/N_c^2.
```

The desired bridge would need to turn that color-channel fraction into the
Route-2 center readout ratio:

```text
c_TE = gamma_T(center)/gamma_E(center) = -F_adj.
```

The exact Route-2 family gives an immediate rational counter-witness to
entailment by `F_adj` alone. Both rows below keep the same granted T-side
values and the same exact `F_adj = 8/9`:

| `rho_E` | `q_E = 1 + rho_E/6` | `c_TE = (-2)(5/6)/q_E` |
|---:|---:|---:|
| `0` | `1` | `-5/3` |
| `21/4` | `15/8` | `-8/9` |

Thus `F_adj = 8/9` coexists with at least two exact Route-2 readout maps on the
defined center objects. The bridge target is recovered precisely when the
E-center lift

```text
rho_E = 21/4
```

is already supplied. Equivalently, solving `c_TE = -F_adj` inside the Route-2
endpoint algebra returns

```text
q_E = 15/8,
rho_E = 21/4.
```

That is endpoint algebra after the bridge, not a derivation of the bridge from
the Fierz channel count.

## Exact Obstruction Step

The obstructed step is the attempted map

```text
F_adj as a positive SU(3) adjoint channel-count fraction
    -> signed Route-2 center ratio gamma_T(center)/gamma_E(center).
```

This step needs an additional source-domain/readout rule that says the Route-2
E/T center endpoint ratio is the negative of the SU(3) adjoint fraction. The
Fierz identity supplies the fraction `8/9`; the granted T-side values supply a
negative orientation for the T channel; neither supplies the E-center lift
`q_E = 15/8`.

If the attempted proof instead passes through the physical connected-trace
observable, the obstruction becomes the already scoped physical selector:

```text
R_phys(kappa_EW) = F_adj + kappa_EW (1 - F_adj).
```

Choosing `kappa_EW = 0` is the physical readout/weighting rule withheld by the
Rconn open-gate and by the Record/Quantum boundary. This note does not use that
route to block the algebraic bridge. The narrower algebraic obstruction already
appears before the physical EW selector: `F_adj` is not typed as a Route-2
center readout.

## Reachability Re-Run

The W9 machinery has these facts:

```text
CURRENT_TYPED_EDGES + DERIVED_ADDITIONAL_EDGES
```

contains the quote-derived Route-2 support/readout edges and the reverse
endpoint algebra edges

```text
rho_E = 21/4 -> q_E = 15/8,
q_E = 15/8 -> c_TE = -8/9.
```

It still does not contain

```text
su3_R_conn_8_9 -> route2_center_TE_minus_8_9.
```

Re-running reachability on that inventory gives:

```text
su3_R_conn_8_9 -> route2_rho_E_21_4
```

absent without the bridge and present with the hypothetical bridge adjoined.
Since this note does not derive the bridge, the bypass remains absent on the
current derived inventory.

For the s3-time gate forms, the discharge surface is unchanged: the exact
conditional slice family and endpoint algebra remain available, but the
endpoint triple still needs upstream derivation. The typed color-projection
segment is an open target, not a discharge of the full gate.

## No-Go Discipline Gate

This is a narrow obstruction claim, so the N1-N8 stress test is recorded here.

**N1 alternative routes.**

| Route | Attempt | Result |
|---|---|---|
| Direct Fierz count | Identify `F_adj = 8/9` with `|c_TE|`. | ATTEMPTED: exact `rho_E = 0` and `rho_E = 21/4` counter-witnesses share `F_adj` but have different `c_TE`. |
| Sign from T-side orientation | Use `alpha_T/alpha_E = -2` to attach the minus sign. | ATTEMPTED: the sign is compatible, but the magnitude still depends on `q_E`. |
| Endpoint algebra reversal | Use `q_E = 15/8 -> c_TE = -8/9` from W9. | ATTEMPTED: this is reverse endpoint algebra; it starts from the E-center lift rather than deriving it. |
| Physical `kappa_EW = 0` selector | Turn Fierz count into a connected-trace observable first. | ATTEMPTED: this route exits the algebraic W1 bridge into the separate audited-clean open-gate W2, where the physical readout/weighting selector remains withheld. |
| Record/Quantum shortcut | Treat Record or Quantum as supplying the color readout context. | RULED OUT BY PRIOR for this packet: the minimal axiom memo supplies no readout context, weighting, dynamics, or physical observable bridge. |
| Live endpoint comparator | Use the live `c_TE` value near `-8/9`. | ATTEMPTED: live proximity is bounded comparator evidence, not theorem input. |

**N2 wall independence.**

Collapsed walls used here:

| Wall | Meaning |
|---|---|
| W1 | Missing algebraic source-domain/readout edge from `F_adj` to Route-2 `c_TE`. |
| W2 | Missing physical `kappa_EW = 0` readout/weighting selector, only if the proof routes through a physical connected-trace observable. |

W1 does not automatically close W2: an algebraic Route-2 bridge could be
stated without deriving the physical EW selector. W2 does not automatically
close W1: selecting the connected color channel would still not identify that
observable with the Route-2 center ratio and sign. They are independent, and
the headline obstruction uses W1.

**N3 hidden-wall scan.**

The phrases "given", "support", "bridge", "Record", "canonical", and
"physical" were re-read. `Given` appears only for explicitly granted T-side or
readout-context clauses. `Bridge` names the target edge. `Record` and
`physical` are cited to the minimal-axiom and Rconn open-gate authorities.
`Canonical` appears only inside authority titles or formulas already scoped by
those authorities. No hidden admission was promoted.

**N4 residual matching.**

| Witness | Witness residual | Current residual | Match |
|---|---|---|---|
| [QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md](QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md) | `R_conn` numeric/support match does not derive `c_TE`. | Same bridge target, now tested against Fierz algebra definitions. | yes |
| [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md) | Current typed bank lacks `R_conn -> c_TE`. | Same edge, reachability re-run after W9 inventory repair. | yes |
| [RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md) | Physical `kappa_EW` selector is not supplied by Record/Quantum. | Separate physical route, not the algebraic W1 obstruction. | yes, with separation |
| [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) | `rho_E` remains free under minimal Route-2 naturality. | Same E-center freedom used as exact counter-witness. | yes |

**N5 rhetoric audit.**

The negative phrase is scoped to the current defined center objects and the
named authority bank. It is not stated lattice-wide, program-wide, or against
future source/readout theorems. Tested resolutions: exact endpoint algebra,
typed-edge graph reachability, Fierz channel algebra, and physical selector
boundary. Untested future routes remain open targets.

**N6 partial-closure path scan.**

The primitive registry lists `minimal_axioms`, `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None supplies a
Route-2 readout bridge, physical observable identification, weighting rule, or
E-center lift. A future owner-approved convention, explicit admission, or
source-domain theorem could still add the typed bridge and then retire the
import; this note does not classify that path as a new axiom.

**N7 steelman.**

A hostile reviewer could argue that the W67 bridge is not trying to derive a
physical EW selector at all: it only needs the representation-theoretic
adjoint fraction from the Fierz authority, and the Route-2 support already has
an E/T two-channel split with a negative T orientation. Under that framing,
`F_adj` might be a pure algebraic label for the missing center ratio rather
than a physical connected-trace observable. The strongest supporting authority
for this steelman is the Fierz note's exact `8/9` channel-count derivation.
The counter-witness above is why this remains insufficient on the current
definitions: the Route-2 E-center lift is still a free map entry.

**N8 cross-cycle echo.**

Similar walls appear in the Lane 3 no-go ledger: Route-2 naturality leaves
`rho_E` free; the `R_conn` numeric match is an import boundary; and the current
typed bank lacks the source-domain bridge. Related Record/readout-context
campaigns separate supplied readout contexts from Record itself. Those echoes
have not been retired by a convention that supplies this specific Route-2
center-ratio bridge.

Gate result: PASS for this narrow obstruction. The result does not rule out a
future typed source-domain theorem, approved convention, or alternate Route-2
readout primitive.

## Boundary

This note does not establish:

- a physical connected-trace selector `kappa_EW = 0`;
- a physical EW current weighting rule;
- a Route-2 E-center source/readout primitive;
- the up-sector scalar law `beta_E/alpha_E = 21/4`;
- non-top quark masses;
- a discharge of the s3-time gate;
- any audit verdict.

It records that the exact Fierz/adjoint fraction remains available as
`F_adj = 8/9`, while the typed edge from that fraction to the signed Route-2
center ratio is not derived by the current definitions.

## Verification

Run:

```bash
python3 scripts/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=62, FAIL=0
```
