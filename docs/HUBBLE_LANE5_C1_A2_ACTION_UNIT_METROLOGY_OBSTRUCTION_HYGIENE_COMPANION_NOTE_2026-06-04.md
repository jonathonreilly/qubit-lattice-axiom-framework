# Hubble Lane 5 (C1) A2 Action-Unit Metrology Obstruction Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04; source-hygiene refresh 2026-07-04
**Type:** meta (audit-readiness companion / dependency-hygiene evidence)
**Status:** companion-only. This file records source-surface hygiene evidence
for the parent A2 action-unit metrology obstruction. It is not a re-audit, not
a new theorem, not a status prediction, and not a verdict change.
**Companion target:** `hubble_lane5_c1_a2_action_unit_metrology_obstruction_note_2026-04-29`
(parent note
[`HUBBLE_LANE5_C1_A2_ACTION_UNIT_METROLOGY_OBSTRUCTION_NOTE_2026-04-29.md`](HUBBLE_LANE5_C1_A2_ACTION_UNIT_METROLOGY_OBSTRUCTION_NOTE_2026-04-29.md),
parent runner
[`scripts/frontier_hubble_lane5_c1_a2_action_unit_metrology_obstruction.py`](../scripts/frontier_hubble_lane5_c1_a2_action_unit_metrology_obstruction.py)).
**Primary runner:**
[`scripts/audit_companion_hubble_lane5_c1_a2_action_unit_metrology_obstruction_hygiene_2026_06_04.py`](../scripts/audit_companion_hubble_lane5_c1_a2_action_unit_metrology_obstruction_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_hubble_lane5_c1_a2_action_unit_metrology_obstruction_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_hubble_lane5_c1_a2_action_unit_metrology_obstruction_hygiene_2026_06_04.txt)

## Parent Boundary

The parent note is a bounded source proposal for the Lane 5 `(C1)` A2
action-unit metrology obstruction. Its load-bearing statement is that supplied
dimensionless inputs (`g_bare = 1`, `beta = 6`, plaquette/u0 data, APBC
hierarchy factor, and `c_cell = 1/4`) do not select a dimensional action
quantum `kappa` on `P_A H_cell`.

The obstruction is the rescaling witness:

```text
S_dim -> lambda S_dim,
kappa -> lambda kappa,
exp(i S_dim/kappa) = exp(i lambda S_dim / lambda kappa).
```

The missing source input remains a physical clock/source/action metrology map
that ties the dimensionless lattice action and the `P_A` boundary carrier to a
particular dimensional `kappa`.

## Current Hygiene Evidence

The companion runner checks the current source packet rather than a frozen
prior-audit snapshot:

1. the parent note and parent runner exist;
2. the parent note SHA-256 matches the live ledger row's `note_hash`;
3. the parent runner SHA-256 matches the current parent runner cache;
4. the parent runner executes successfully with at least the original eight
   checks and zero failures; on the refreshed surface it reports
   `TOTAL: PASS=16, FAIL=0`;
5. the parent prose still contains the rescaling identity, dimensionless input
   list, shortcut boundary, missing-metrology line, and runner-witness list;
6. the parent header and hypothesis section name the staggered-carrier input
   ([`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md))
   and the supplied `g_bare = 1` parent gate
   ([`G_BARE_DERIVATION_NOTE.md`](G_BARE_DERIVATION_NOTE.md));
7. the live ledger row contains the required dependency edges
   `g_bare_derivation_note`, `minimal_axioms`, and
   `staggered_dirac_realization_gate_note_2026-05-03`;
8. audit-owned fields such as status, criticality, and load-bearing score are
   treated as informational live fields, not as timeless gates;
9. prior-audit history, where present, is used only to confirm that the
   required gate paths were already visible to the audit surface;
10. the helper runner, sister Lane 5 note, companion note, and cached parent
    runner log are present.

## What This Does Not Claim

- It does not claim a new theorem.
- It does not set, predict, promote, or demote any audit-owned status field.
- It does not edit generated ledger, queue, or publication-status files.
- It does not derive `g_bare = 1`.
- It does not derive the staggered-Dirac realization target.
- It does not supply the missing clock/source/action metrology map.
- It does not turn the A2 obstruction into a positive `(C1)` result.

## Reproduction

```bash
PYTHONPATH=scripts python3 scripts/audit_companion_hubble_lane5_c1_a2_action_unit_metrology_obstruction_hygiene_2026_06_04.py
```

Expected current result:

```text
PASS=51 FAIL=0
```
