# No-Go Ledger

## Direct Q1 -> RHN activation

Runner: `scripts/frontier_koide_q1_rhn_direct_bridge_no_go.py`

Status: scoped no-go.

The Koide `Q=1` normal source is charge zero; a Majorana pairing activation is
charge minus two.  A U(1)-equivariant current-stack map cannot send one to the
other in the tested bridge class.

## Q1 dark matter closure

Runners:

- `scripts/frontier_koide_q1_neutrality_classifier.py`
- `scripts/frontier_dm_rhn_koide_q1_axis_abundance_compatibility.py`

Status: not closed.

The neutral `nu_R` slot is a natural target axis, but the retained bridge,
abundance, stability, and transport closures are absent.

## Typed 2/9 unification

Runner: `scripts/frontier_koide_two_ninth_provenance_classifier.py`

Status: not closed.

The arithmetic footprint is shared, but matrix coefficient, Brannen phase,
Callan-Harvey anomaly, and APS eta remain different typed objects.
