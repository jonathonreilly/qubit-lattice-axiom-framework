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

## Automatic retained/unbounded upgrade from Q/delta compatibility

Runner: `scripts/frontier_koide_q1_last_mile_unlock_cascade.py`

Status: pruned.

The last-mile cascade is exact but conditional.  `P_ORIENT` would close
`delta=+2/9`, `P_SOURCE` would close `Q=2/3`, and both would make the Koide
Q/delta dimensionless package audit-ready.  It does not by itself derive either
premise, does not bypass independent audit, and does not upgrade generation
labels, absolute masses, Q1 dark matter, or Y_T unbounded closure.

## Full P_ORIENT from spatial/taste carrier alone

Runner: `scripts/frontier_koide_q1_physical_orientation_basepoint_probe.py`

Status: bounded support only.

The oriented generator `g` is not a free convention: it is the proper spatial
`C3[111]` rotation and the `T1` image of full taste-cube descent.  However,
this still does not derive the microscopic source/endpoint/readout law needed
to turn the oriented carrier into the physical selected-line basepoint.  The
full `P_ORIENT` premise remains open.

## S-record source-endpoint / measure shortcut

Runner: `scripts/frontier_koide_q1_source_endpoint_record_measure_no_go.py`

Status: exact no-go for the restricted shortcut.

The sharp record `S=C+C^2` forces two atoms,

```text
P0 = (I+C+C^2)/3, rank 1
P1 = I-P0,        rank 2
```

but it does not force the atom measure.  Equal atom count gives the
block-count `Q=2/3` lane; rank/Born push-forward from `I/3` gives the
trace/default `Q=1` lane.  Both are `C3`-invariant completions.

The same record is reflection-even: reflection fixes `S` while swapping
`C <-> C^2` and full-cube `Qf <-> Qb`.  Therefore an `S`-only or
reflection-even source law cannot select the forward channel.  The coordinate
endpoints also form a free `C3` orbit, so no unbased endpoint selector exists.
The next theorem must add an orientation-odd source/boundary law or an
independent measure principle.

## Automatic quotient measure from source-measure machinery

Runner: `scripts/frontier_koide_q1_record_quotient_measure_fork.py`

Status: exact fork / no closure of the selection principle.

The embedded sharp record has two projectors:

```text
P0 = (I+C+C^2)/3, rank 1
P1 = I-P0,        rank 2
```

Full Hilbert trace/Born push-forward gives

```text
(tau_H(P0), tau_H(P1)) = (1/3, 2/3)
```

and therefore the trace/default `Q=1` branch.  The abstract rank-erased
quotient record algebra has two atoms with counting trace

```text
(tau_count(e0), tau_count(e1)) = (1/2, 1/2)
```

and therefore the conditional `Q=2/3` branch.

These are different reference laws:

```text
(tau_H o iota)(x0,x1) = (x0+2*x1)/3
tau_count(x0,x1)      = (x0+x1)/2
```

Existing source-measure / record-intervention theorems make record-facing
states probability laws and expose a full-support reference `P0`, but do not
derive the quotient counting reference.  The remaining positive theorem must
be a physical rank-erasing recordization / count-on-record-atoms principle.

## Objectivity or max entropy deriving the Q-side premise

Runner: `scripts/frontier_koide_q1_q_side_objectivity_premise_audit.py`

Status: exact support for the minimal premise / no closure from tested
objectivity routes.

Bare atom-anonymity on the rank-erased quotient algebra is sufficient:

```text
Aut(C^2 as bare two atoms) contains the swap
swap-invariant probability = (1/2, 1/2)
Q = 2/3
```

But the physical `S`-labeled record is not bare.  The atom swap changes the
`S` eigenvalue pair `(2,-1)` to `(-1,2)`, so the automorphism group preserving
the labeled record is only the identity.  The identity imposes no measure
constraint; both `(1/3,2/3)` and `(1/2,1/2)` remain invariant.

Max entropy also fails to choose the premise without first choosing the
algebra:

```text
full Hilbert microstate count then erase rank -> (1/3,2/3) -> Q=1
erase rank then count quotient atoms          -> (1/2,1/2) -> Q=2/3
```

The remaining positive Q-side theorem is therefore sharper: prove that
physical charged-lepton readout erases Hilbert rank before reference selection,
or derive the separate strict-onsite `P_SOURCE` law.
