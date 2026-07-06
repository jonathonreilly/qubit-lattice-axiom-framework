# Tier-A Residual Owner Adoption and Retirement

**Date:** 2026-07-04
**Type:** meta
**Claim type:** meta
**Status authority:** owner-governance registry action plus independent audit
lane mechanics. This note records explicit owner adoption of the Block49
residual governance candidates and retires the remaining live Tier-A registry
row through `docs/audit/data/owner_governed_premise_nodes.json`. It does not
derive `AC_phi_lambda` or theta as theorems, does not add or amend an axiom,
does not add an approved framework primitive, and does not set any audit
verdict for source-side support or no-go packets.
**Primary runner:**
[`scripts/tier_a_residual_owner_adoption_retirement_2026_07_04.py`](../scripts/tier_a_residual_owner_adoption_retirement_2026_07_04.py)
**Cached output:**
[`logs/runner-cache/tier_a_residual_owner_adoption_retirement_2026_07_04.txt`](../logs/runner-cache/tier_a_residual_owner_adoption_retirement_2026_07_04.txt)

## Current-Main Landing Posture

This landing is applied against current main, not against the stale PR branch
state.

- Theta was already retired from live Tier-A on 2026-07-05 by retained
  derivation, with its record preserved under `retired_derivation_targets`.
  This note does not resurrect theta as an owner-governed premise and does not
  replace that retained-derivation retirement.
- `AC_phi_lambda` remains the live Tier-A target on current main before this
  landing. Its source surface,
  `staggered_dirac_realization_gate_note_2026-05-03`, has itself landed
  through the audit lane as `audited_clean` / `retained_bounded` at main commit
  `5d8df21fe`, with its full basis terminal-grade.
- The registry delta therefore retires the remaining live AC Tier-A slot and
  records the owner-governed AC boundary in
  `owner_governed_premise_nodes.json`.

Accordingly, [`docs/audit/data/tier_a_admissions.json`](audit/data/tier_a_admissions.json)
now has:

```text
genuine_admitted_input_count = 0
canonical_ids = []
derivation_targets = {}
```

Historical details for `AC_phi_lambda` and theta remain in
`retired_derivation_targets`. The live chain-satisfying AC governance premise
id is registered in
[`docs/audit/data/owner_governed_premise_nodes.json`](audit/data/owner_governed_premise_nodes.json).

## Owner Approval

The owner approval in the landing thread was:

```text
I approve #4991's owner-governance adoption of the four Block49 residual candidates, with the exact boundaries in owner_governed_premise_nodes.json, retiring live Tier-A admissions without treating them as axioms, primitives, or audit-ratified theorem closures.
```

Because theta was already retired by retained derivation on current main, the
two theta candidates are approval context only in this landing. The owner
governed premise registry carries the remaining live AC target.

## Adopted AC Text and Boundary

The owner-governed `AC_phi_lambda` premise is the AC part of the Block49
decision: Candidate 1 plus Candidate 2.

**Candidate 1 adopted text:**

```text
For the AC_phi_lambda charged-lepton matter-action surface, the physical
statistical grain is the K/CPT orbit or holomorphic-pair occupancy grain:
the doublet contributes once per K/CPT orbit rather than once per sector or
channel. This premise supplies only the matter-action occupancy grain needed
to discharge the surviving AC(i) measure-side realization binary.
```

**Candidate 2 adopted text:**

```text
For the AC_phi_lambda charged-lepton R-eta surface, the physical readout is
the fixed-locus density class h, identity-read in h-units as the eta angle.
No additional clock-rate, transport, or normalization factor intervenes
between the retained fixed-locus density class and the charged-lepton eta
readout.
```

**Registry boundary:** this adoption retires only the current minimum
`AC_phi_lambda` Tier-A atoms: AC(i) matter-action occupancy grain and AC(ii)
R-eta h-class/h-unit readout license. It supplies no value of `r`, `delta`,
charged-lepton mass, mixing angle, probability rule, above-C3
taste/Dirac/chirality content, CKM/PMNS alignment, or sector-weight law. It
does not set any audit status for the AC support or no-go packet stack.

## Theta Disposition

The owner approval also named:

- `theta_gauge_sector_phase_source_premise`;
- `theta_mass_determinant_channel_w2_premise`.

On current main those candidates no longer retire a live Tier-A target,
because theta is already retired by the retained-derivation basis recorded in
`tier_a_admissions.json`. The theta source row remains a
retained-bounded selected-action-surface theorem in the audit ledger. This
landing does not edit the theta source row, its audit verdict, or its
retirement basis.

## Registry and Pipeline Effect

This block introduces a third accepted-premise registry class:

```text
owner-governed residual premises
```

Those entries are Class B owner-governed governance premises. They are distinct
from both:

- `axiom_premise_nodes.json`: axioms and approved framework primitives;
- `tier_a_admissions.json`: live Tier-A derivation targets that bound
  otherwise clean dependents to `retained_bounded`.

Owner-governed residual premises chain-satisfy without Tier-A bounding, but
only inside the exact boundary recorded in
`owner_governed_premise_nodes.json` and this note. They do not make the
underlying support/no-go packets audited clean or theorem-derived.

## Firewalls

- No axiom is added or amended.
- No approved framework primitive is added or amended.
- No Tier-A target remains live.
- The prior `AC_phi_lambda` and theta rows are preserved only as historical
  `retired_derivation_targets`.
- `Y0` and `g0` remain vacuous survey conventions, not accepted premises.
- The source-side theorem/no-go packets retain their own audit statuses.
- The adoption cannot be broadened by title or summary; cite the registry id
  and exact boundary text.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/tier_a_residual_owner_adoption_retirement_2026_07_04.py
```

Expected close: `FAIL=0`.
