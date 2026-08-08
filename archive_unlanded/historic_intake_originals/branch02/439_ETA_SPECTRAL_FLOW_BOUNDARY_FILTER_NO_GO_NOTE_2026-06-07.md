# Eta/Spectral-Flow Boundary Filter No-Go Note

**Date:** 2026-06-07
**Claim type:** no_go
**actual_current_surface_status:** no-go
**trace_class:** negative_route_pruning
**reachability_to_target:** prunes
**Status authority:** source-note proposal only. Independent review and audit
are required before this branch-local result can be used as an effective
repo-wide status.
**Primary runner:** [`scripts/frontier_eta_spectral_flow_boundary_filter_no_go_2026_06_07.py`](../scripts/frontier_eta_spectral_flow_boundary_filter_no_go_2026_06_07.py)
**Cached log:** [`logs/runner-cache/frontier_eta_spectral_flow_boundary_filter_no_go_2026_06_07.txt`](../logs/runner-cache/frontier_eta_spectral_flow_boundary_filter_no_go_2026_06_07.txt)

## Question

The chirality-resolution campaign asks whether the signed-gravity/chirality
lane can avoid adding a source selector by deriving one from boundary eta or
spectral flow.  The concrete route tested here is:

```text
eta / spectral flow on the finite boundary sector
  -> oriented crossing or index sign
  -> canonical chi source branch
  -> active odd source vector [+1,-1].
```

This note gives the finite obstruction to that route.  Eta and spectral flow
can certify a crossing after an oriented path, mass sign, or boundary section
has been supplied.  They do not choose that orientation by themselves.

## Current Repo Surface Used

- The finite `Z_N` spectral-asymmetry theorem supplies eta as a finite
  character-weighted spectral asymmetry and proves constancy on gapped paths.
  It does not derive a continuum APS bridge or a physical fixed-point operator.
- The bulk staggered APS scoping note shows the closed flat staggered-bulk eta
  vanishes by chiral `+/-` spectral pairing at the bare surface.
- The signed-gravity APS source-action proposal already records that
  `sign(eta)` is locally constant on the gapped domain and therefore
  variationally inert unless it is multiplied into an action term by an
  additional source principle.
- The retained boundary-source no-go states that separable APS/Wald/Gauss
  source ingredients span orientation-even active sources plus neutral labels,
  not the required orientation-odd source.

No new axiom, audit row, or authority-surface edit is introduced here.

## Finite Statement

Let `T(m) = [m]` be a one-mode boundary crossing and let
`T_pair(m) = diag(m,-m)` be the paired chiral/bulk model.

1. For `T(m)`, the path `m: -1 -> +1` has spectral flow `+1`, while the
   reversed path `m: +1 -> -1` has spectral flow `-1`.
2. The two paths have the same unoriented endpoint pair.  Any rule that depends
   only on the unoriented crossing data assigns the same value to both, so it
   cannot equal the nonzero oriented spectral flow on both paths.
3. On a gapped component, eta is locally constant.  The finite-difference
   derivative of `sign(eta)` is zero away from a crossing.
4. For the paired chiral/bulk model `diag(m,-m)`, net eta and net spectral flow
   vanish because the upward and downward crossings cancel.
5. A selector such as "start on the negative mass side and end on the positive
   mass side" can choose the `+1` sign, but that selector is exactly the
   external orientation/mass convention the route was supposed to derive.

Therefore eta/spectral-flow data do not canonically select the missing
orientation/source branch.  They are useful certificates for an already oriented
boundary problem, not the source of the orientation.

## Source-Action Consequence

The active source vector required by the signed-gravity proposal is
orientation-odd:

```text
[+1,-1].
```

The separable positive source stack remains orientation-even:

```text
[+1,+1].
```

Multiplying a positive source by a supplied `chi = sign(eta)` label can produce
the odd vector, but the multiplication is an additional cross term.  The eta
label alone has no local variational derivative on the gapped sector and does
not generate the source action.

## Runner Certificate

The paired runner checks:

- forward and reversed scalar spectral flow carry opposite signs;
- eta jumps track the oriented crossing only after orientation is supplied;
- gapped eta has zero finite-difference derivative;
- paired chiral/bulk spectra have zero eta and zero net spectral flow;
- an unoriented path invariant cannot equal nonzero oriented spectral flow;
- the odd source appears only when an eta sign is explicitly multiplied into
  the source stack.

The cached run reports:

```text
SCORECARD: PASS=23 FAIL=0
```

## What This Prunes

This prunes the eta/spectral-flow boundary-filter route as a source of the
missing canonical chirality/source selector on the current axiom surface.

It does not prove:

- signed gravity impossible;
- chirality impossible;
- all APS or eta mechanisms impossible;
- that a later product-grading, Berry/holonomy, boundary dynamics, or
  generation-readout construction cannot supply the missing selector.

The next honest target is a structure that can break the orientation symmetry
before eta or spectral flow is read.  In the current lane map, that points back
to the generation/chiral-grading and Berry/holonomy selector routes rather than
to eta as the selector itself.

## Audit Boundary

This branch does not edit `docs/audit/**`, set an audit verdict, update an
audit queue, or mark a row as retained.  It supplies a reviewable no-go packet
for independent review.
