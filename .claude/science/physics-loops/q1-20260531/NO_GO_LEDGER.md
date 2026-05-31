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

Status: partly repaired by coefficient bridge; not physically closed.

The arithmetic footprint is shared, and the Q1 nonidentity coefficient is now
exactly typed against APS eta:

```text
coeff_nonid(S_Q1) = -eta_APS.
```

The remaining no-go/firewall is that Q1 is transposition-even and does not by
itself supply the parity-odd signed Brannen phase readout.

## Signed selected-line readout from Q1 alone

Runner: `scripts/frontier_koide_q1_signed_selected_line_readout_no_go.py`

Status: exact no-go.

Q1 is fixed under the transposition swapping `g` and `g^2`; `delta` is odd.
Every equivariant map from a fixed input to an odd line gives zero.  Therefore
Q1 alone cannot supply the signed phase.  It can supply only the magnitude.
