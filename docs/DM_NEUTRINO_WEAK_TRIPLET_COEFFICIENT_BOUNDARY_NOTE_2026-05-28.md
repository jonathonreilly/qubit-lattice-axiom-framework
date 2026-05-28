# DM Neutrino Weak-Triplet Coefficient Boundary

**Date:** 2026-05-28
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; independent audit owns
`claim_type`, `audit_status`, and effective status.
**Primary runner:** [`scripts/frontier_dm_neutrino_weak_triplet_coefficient_axiom_boundary.py`](../scripts/frontier_dm_neutrino_weak_triplet_coefficient_axiom_boundary.py)

## Purpose

The archived predecessor
`archive_unlanded/dm-neutrino-stale-runners-2026-04-30/DM_NEUTRINO_WEAK_TRIPLET_COEFFICIENT_AXIOM_BOUNDARY_NOTE_2026-04-15.md`
failed audit because its runner was stale and could not reproduce the
coefficient-normalization checks from repo-local inputs. This note is the
active re-audit surface after the runner was made repo-local.

No new axiom is introduced. "Axiom" here means only the current framework
baseline in [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md):
physical `Cl(3)` local algebra on the `Z^3` spatial substrate.

## Bounded Claim

On the cited source packet, the runner verifies the transfer-coefficient
boundary:

```text
c_odd = +1
M_even = v_even [1, 1]
v_even = (sqrt(8/3), sqrt(8)/3)
```

equivalently,

```text
gamma = a_sel
E1 = sqrt(8/3) (tau_E + tau_T)
E2 = (sqrt(8)/3) (tau_E + tau_T).
```

The runner checks the source-side selector slot, target-side odd slot,
odd bosonic normalization, even swap reduction, even bosonic normalization,
and the remaining benchmark/source-amplitude boundary.

## Non-Claims

- This does not derive the selector amplitude `a_sel`.
- This does not derive the symmetric weak source amplitude `tau_+`.
- This does not rebuild the leptogenesis benchmark around the exact transfer
  law.
- This does not close the PMNS/leptogenesis branch from primitives.
- This does not promote the archived source note or its stale table.

## Re-Audit Scope

Audit the runner-backed coefficient boundary only. The prior archived note is
history, not a retained authority. If the runner passes, the useful recovered
science is a bounded coefficient-normalization packet with the source-amplitude
law still open.
