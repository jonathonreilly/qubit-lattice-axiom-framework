# DM Neutrino Weak-Triplet Coefficient Axiom Boundary Live Packet

**Date:** 2026-04-15; live-source repair 2026-06-08
**Status:** bounded-support coefficient-boundary packet; proposed for independent re-audit, not effective retained.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_dm_neutrino_weak_triplet_coefficient_axiom_boundary.py`](../scripts/frontier_dm_neutrino_weak_triplet_coefficient_axiom_boundary.py)
**Primary runner cache:** [`logs/runner-cache/frontier_dm_neutrino_weak_triplet_coefficient_axiom_boundary.txt`](../logs/runner-cache/frontier_dm_neutrino_weak_triplet_coefficient_axiom_boundary.txt)

## Purpose

This note restores a current source surface for the legacy claim id
`dm_neutrino_weak_triplet_coefficient_axiom_boundary_note_2026-04-15`.
The archived note failed audit because the old runner read absolute paths and
exited before checking the coefficient-normalization packet.

The current runner is repository-local and its cache is fresh:

```text
SUMMARY: PASS=14 FAIL=0
```

This note does not edit audit results. It queues the current bounded packet for
independent re-audit.

## Framework Sentence

In this row, "axiom" means only the single framework axiom:

```text
Cl(3) on Z^3
```

The transfer-class theorem and the coefficient-normalization notes are derived
atlas rows on top of that surface, not additional axioms.

## Live Claim

Within the current single-axiom `Cl(3)` on `Z^3` stack plus the cited derived
atlas rows, the weak-triplet transfer coefficients are no longer the open
part of this lane.

The runner checks:

- the framework sentence and transfer-class theorem boundary;
- the exact one-real-slot source selector `a_sel`;
- the exact odd triplet target slot `gamma`;
- the bosonic matching theorem fixing `|c_odd| = 1`;
- the source-oriented sign convention recording `c_odd = +1`;
- the exact weak source carrier's symmetric bright-column form;
- the swap-reduction theorem's common-column form `M_even = v_even [1,1]`;
- the antisymmetric source mode in the kernel of that swap-fixed exact class;
- the even bosonic-normalization theorem fixing
  `v_even = (sqrt(8/3), sqrt(8)/3)`;
- the source-side factorization through `tau_+ = tau_E + tau_T`;
- the current boundary that source amplitudes and benchmark rebuild remain
  open.

Equivalently, the bounded coefficient packet records:

```text
gamma = a_sel
E1 = sqrt(8/3) (tau_E + tau_T)
E2 = (sqrt(8)/3) (tau_E + tau_T)
```

## Remaining Boundary

This packet does not derive:

- the selector amplitude `a_sel`;
- the symmetric weak source amplitude `tau_+`;
- the fully rebuilt leptogenesis benchmark in the exact transfer law;
- a retained physical benchmark prediction.

The old benchmark value therefore remains bounded/open:

```text
eta = 1.81e-10
eta / eta_obs ~= 0.30
```

The benchmark runner has not yet been rebuilt around that exact transfer law.
The current closure is coefficient-boundary closure only, not source-amplitude
or benchmark closure.

Put differently, the live gap is the source-amplitude law for `a_sel` and
`tau_+`, not the transfer coefficients.

## Provenance

The archived stale note remains historical provenance only:
[`archive_unlanded/dm-neutrino-stale-runners-2026-04-30/DM_NEUTRINO_WEAK_TRIPLET_COEFFICIENT_AXIOM_BOUNDARY_NOTE_2026-04-15.md`](../archive_unlanded/dm-neutrino-stale-runners-2026-04-30/DM_NEUTRINO_WEAK_TRIPLET_COEFFICIENT_AXIOM_BOUNDARY_NOTE_2026-04-15.md).
