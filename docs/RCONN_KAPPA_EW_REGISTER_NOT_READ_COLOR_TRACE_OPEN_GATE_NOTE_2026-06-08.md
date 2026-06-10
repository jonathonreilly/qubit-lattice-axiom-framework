# Rconn Kappa EW Register-Not-Read Color-Trace Open Gate

**Date:** 2026-06-08
**Claim type:** open_gate
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived
after independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_rconn_kappa_ew_register_not_read.py`](../scripts/frontier_rconn_kappa_ew_register_not_read.py)
**Cached log:**
[`logs/runner-cache/frontier_rconn_kappa_ew_register_not_read.txt`](../logs/runner-cache/frontier_rconn_kappa_ew_register_not_read.txt)
(TOTAL: PASS=18 FAIL=0)

## Purpose

**2026-06-10 route repair.** This note now separates two facts that were
previously too close together:

1. the exact Fierz trace/traceless algebra is still valid support; and
2. the proposed register-not-read shortcut does not close the `κ_EW = 0`
   selector on the current Record/axiom surface.

The source surface therefore records a **route-demotion**, not a positive
closure. It does not set, predict, or estimate any audit verdict.

The retained no-go [`RCONN_DERIVED_NOTE`](RCONN_DERIVED_NOTE.md) establishes
the exact SU(`N_c`) Fierz adjoint fraction
`F_adj = (N_c^2 - 1)/N_c^2` (`= 8/9` at `N_c = 3`) but leaves the physical
EW-current readout selector free:

```text
R_phys(κ_EW) = F_adj + κ_EW(1 - F_adj),
κ_EW = 0 -> 8/9,    κ_EW = 1 -> 1.
```

The old proposed route was:

```text
If a future retained theorem proves that the register-not-read discipline
governs the color operator-trace channel, then the registered channel is the
traceless connected channel and κ_EW = 0.
```

That antecedent is not proved here, is not supplied by the Record axiom, and
is too weak as stated. A future retained theorem would need to supply an
actual finite central-sector readout context plus the physical weighting or
observable-bridge rule. Merely relabeling the Fierz singlet trace channel as
unregistered does not close `κ_EW`.

## Inputs

| Input | Source | Role |
|---|---|---|
| `R_phys = F_adj + κ_EW(1 - F_adj)` and the prior failed CMT/OZI selector routes | [`RCONN_DERIVED_NOTE`](RCONN_DERIVED_NOTE.md) | open selector left by the retained no-go |
| exact Fierz `S + C` channel decomposition and `F_adj = (N_c^2 - 1)/N_c^2` | [`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md) | exact group-theory support |
| `N_c = 3` from spatial `d = 3` (`Z^3`) | [`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md), [`NATIVE_GAUGE_CLOSURE_NOTE`](NATIVE_GAUGE_CLOSURE_NOTE.md) | fixes the `8/9` specialization of the exact channel count |
| Record axiom boundary | [`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md) | Record supplies no readout context, weighting, normalization, probability, dynamics, within-sector data, or observable bridge |
| route-demotion finite algebra | [`FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION_NARROW_NO_GO_NOTE_2026-06-08`](FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION_NARROW_NO_GO_NOTE_2026-06-08.md) | sibling source proposal; mirrored by this runner, not used as an audit verdict |
| axiom-baseline boundary for `κ_EW` | [`EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09`](EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md) | contextual source proposal: current approved baseline does not supply the missing weighting rule |

No PDG value, fitted number, new axiom, new primitive, or Tier-A admission is
load-bearing in this note.

## Exact Algebraic Support

For a color matrix `G`, the SU(`N_c`) Fierz completeness identity gives

```text
Tr_color[G G^\dagger] =
  (1/N_c) |Tr G|^2 + 2 Σ_A |Tr[G t^A]|^2
  = S + C.
```

In the orthonormal operator basis `{I/sqrt(N_c), sqrt(2) t^A}`:

- `S = (1/N_c)|Tr G|^2` is exactly the `I/sqrt(N_c)` trace component.
- `C = 2 Σ_A |Tr[G t^A]|^2` is the traceless adjoint component.
- The channel-count fraction for the traceless component is
  `(N_c^2 - 1)/N_c^2 = F_adj`.

The runner verifies this decomposition for `N_c = 2, 3, 4, 5`, verifies that
the adjoint generators are traceless, verifies the `κ_EW = 0` and `κ_EW = 1`
specializations, and verifies the `N_c`-universal channel-count fraction.

This is support for the channel algebra only. It is not a physical readout
selector.

## Route-Demotion On The Current Surface

The register-not-read discharge fails on the current surface for three
finite-algebra reasons.

**Twirl is not a finite central-sector partition.** The singlet-channel map is

```text
E_sing(M) = (Tr M / N_c) I,
```

the SU(`N_c`) depolarizing/Haar twirl target. It is not a finite partition map
`D(M) = Σ_k P_k M P_k`: a partition preserves its diagonal blocks, while the
twirl replaces them by their average. On the irreducible color triplet, the
only symmetry-respecting central projectors are `{0, I}`; the corresponding
partition is the identity map, not `E_sing`.

**Count is not weight.** The fixed fraction `8/9` is a channel-count fraction.
`κ_EW` is the physical singlet-channel weight in
`R_phys = F_adj + κ_EW(1 - F_adj)`. A central-sector partition can supply
sectors and counts; it does not supply within-channel weights. Declaring the
singlet "unregistered" would assign a weight by fiat.

**Record does not supply the missing readout context.** The current Record
axiom says that a record supplies no readout context, decomposition,
weighting, normalization, probability, dynamics, within-sector data, or
occupancy rule. The Quantum axiom likewise supplies no physical observable
bridge. Therefore the current axiom surface cannot by itself turn the Fierz
channel split into a `κ_EW = 0` selector.

## Open Gate

The `κ_EW` gate remains open, but the live route is narrower than before. To
close it, a separate non-axiom theorem, convention, or owner-approved
admission must supply a genuine physical EW readout/weighting rule. It is not
enough to invoke register-not-read on the Fierz trace channel.

If a future retained theorem or approved admission supplies that stronger
bridge, one possible consequence could still be:

```text
registered channel = traceless connected channel,
κ_EW = 0,
R_conn = F_adj = (N_c^2 - 1)/N_c^2.
```

At `N_c = 3`, this would give `R_conn = 8/9`. This note does not close that
antecedent.

## Boundary

This note does not establish:

- that Record supplies a color-trace readout context;
- that Record identifies arbitrary operator traces with registered outcomes;
- a weighting, normalization, probability, or measurement rule;
- the missing `κ_EW` selector as an unconditional theorem;
- that the register-not-read color-trace shortcut remains a valid closure
  route on the current surface;
- the separate Route-2 `c_TE = -R_conn` bridge;
- the `ρ_E` readout;
- a retained status before independent audit.

It preserves the exact Fierz trace/traceless algebra and demotes the
previously proposed register-not-read shortcut. The remaining open gate is a
stronger non-axiom readout/weighting bridge, not a direct consequence of
Record.

## Command

```bash
python3 scripts/frontier_rconn_kappa_ew_register_not_read.py
```

Expected: `TOTAL: PASS=18 FAIL=0`.
