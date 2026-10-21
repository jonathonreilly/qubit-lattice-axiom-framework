# Koide A1 — fractional-topology synthesis correction and open obligations

**Date:** 2026-04-24; correction 2026-10-21
**Claim type:** open_gate
**Status:** former five-route no-go synthesis withdrawn pending source review
**Status authority:** independent audit lane only; this source does not set an audit verdict.
**Primary runner:** `scripts/frontier_koide_a1_fractional_topology_no_go_synthesis.py`

The former synthesis relied on the O13 Cheeger-Simons construction and
claimed an exhaustive five-route obstruction. That inference is withdrawn.
The [corrected O13 note](KOIDE_A1_O13_CHEEGER_SIMONS_RZ_NO_GO_NOTE_2026-04-24.md)
shows that 2/9 is not the value of a flat character on an order-three class,
that exp(i c) does not descend to R/Z, and that arbitrary flat circle
holonomies are not restricted to rational multiples of pi. Consequently
O13 supplies neither a new independent 2/9 source nor a general phase no-go.

The old numerical relation exp(2 pi i (2/9))=exp(4 pi i/9) remains true for
the supplied value. It does not prove that a physical phase is selected,
that every relevant character value is rational, or that the only missing
input is a choice of units. A real lift/observable map and a physical
selection law are separate obligations. No Koide closure follows from
withdrawing the invalid no-go.

The primary now checks the finite correction predicates and propagates a
failed predicate as a nonzero exit. It does not aggregate old PASS counts
into scientific certification. The previous 49/49 O13 and five-route
closeout flags are superseded. The original source and aggregator are
recoverable at `f24d17d97d372df977476e4a69674577f31af575` under the same paths.

The four other original probe sources remain available for separate review:

- `scripts/frontier_koide_a1_orbifold_chern_probe.py`
- `scripts/frontier_koide_a1_eta_to_radian_lift_probe.py`
- `scripts/frontier_koide_a1_fqhe_analog_probe.py`
- `scripts/frontier_koide_a1_twisted_k_theory_probe.py`

Their historical counts and obstruction labels are not accepted as proof
by this corrected synthesis. Their geometry, coefficient groups, eta
normalizations, physical premises and counterexamples require individual
validation before any new synthesis. The present correction neither
endorses nor independently falsifies all of those claims. No general
N1–N8 closure is asserted.

Historical context, not premises of the finite correction:
`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md`,
`KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md`, and
`KOIDE_BERRY_BUNDLE_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md`.
