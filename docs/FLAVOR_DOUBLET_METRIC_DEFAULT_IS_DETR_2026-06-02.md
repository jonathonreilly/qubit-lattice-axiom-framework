# Flavor Doublet Metric: Reading-Neutral `diag(3,6,6)`

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Actual current-surface status:** bounded-support
**Trace class:** negative_route_pruning
**Reachability to target:** prunes the route "the HS/coherent-state metric alone selects the `det_C` equal-block reading".
**Bare retained allowed:** false
**Audit required before effective status change:** true
**Runner:** `scripts/flavor_doublet_metric_default_is_detR_2026_06_02.py` (SCORECARD PASS=7).

## Closed Packet

This note proves the finite metric calculation and its honest boundary:

> On the `C3` circulant coefficient surface `(a, Re b, Im b)`, the
> Hilbert-Schmidt/coherent-state metric is `diag(3,6,6)`. The metric is
> reading-neutral: it does not by itself choose whether the doublet is counted
> as two real directions or one complex block.

The packet also checks two route-pruning facts:

- multiplication by `i` on the displayed operator-symbol map
  `H_lin(b)=bC+conj(b)C^2` exits the Hermitian observable algebra, so that
  operator-symbol route does not descend a complex-linear `J`;
- a continuous rephasing `C -> exp(i alpha) C` is compatible with `C^3=I` only
  at the discrete `C3` phases, so the continuous `U(1)_b` selector route is
  blocked.

## Conditional Arithmetic

The runner also records the two arithmetic readings on the same metric:

```text
det_R / per-real-direction reading:
  3a^2 = 6(Re b)^2 = 6(Im b)^2 -> |b|^2=a^2 -> r=1 -> Q=1

det_C / equal-complex-block reading:
  3a^2 = 6|b|^2 -> r=1/2 -> Q=2/3
```

These are conditional readings. This packet does not prove that the full
framework selects either reading as the physical mass readout.

## What This Does Not Claim

This repair intentionally does not claim:

- A1 uniquely defaults to `det_R`;
- all admissible field-space complex structures on the doublet are excluded;
- `Q=1` is selected by the framework;
- `Q=2/3` is impossible or disfavored;
- the charged-lepton value problem is closed.

The remaining frontier question is a physical/readout or field-space theorem
that selects how the doublet is counted.

## Provenance

- The paired runner verifies the metric, operator-symbol real-linearity
  obstruction, conditional `r,Q` arithmetic, phase observability in the
  no-continuous-`U(1)_b` reading, and the order-three rephasing obstruction.
- No `docs/audit/**` status is updated by this packet.
- No new axiom is introduced.
