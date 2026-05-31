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

## Hidden bottom-up sign primitive from Q1

Runner: `scripts/frontier_koide_q1_bottom_up_sign_orientation_audit.py`

Status: exact no-go.

From the C3 group algebra alone,

```text
S_Q1 = 10/9 e - 2/9(g+g^2)
J    = i(g-g^2).
```

Q1 generates only `span{e,g+g^2}`.  The selected-line sign lives on the odd
line `span{J}`.  The projection is exactly zero, and the mirror selected-line
spectra at `+delta` and `-delta` are degenerate unless a based orientation is
supplied.

## Source-oriented gamma sheet as selected-line sign

Runner: `scripts/frontier_koide_q1_gamma_sheet_sign_probe.py`

Status: exact candidate-pruning no-go.

The fixed imaginary slot has real algebraic content, but it is not the missing
selected-line sign for the current bridge.  Gamma reversal obeys

```text
H(m,-gamma) = conjugate(H(m,+gamma)),
```

and the selected-line bridge reads only real diagonal slots of `exp(H)`.
Therefore the selected-line amplitude, branch endpoints, and `delta=+2/9`
point are invariant under `gamma -> -gamma`.  The sign still lives in the
oriented slot/Fourier frame or a based endpoint/source primitive.

## Wrong-sign interpretation

Runner: `scripts/frontier_koide_q1_oriented_sign_compatibility_closeout.py`

Status: pruned.

The sign is not proved wrong.  In an admitted oriented C3 frame,

```text
delta_oriented = -coeff_g(S_Q1) = +2/9.
```

The correct remaining obstruction is underivation of the physical orientation,
not a contradiction of the current `+2/9` selected-line sign.
