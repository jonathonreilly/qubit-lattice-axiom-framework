# Static-Source Readout I1 Accepted-Premise Bridge Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / current-source dependency evidence)
**Status:** companion-only. This records that the parent I1 bridge runner,
source note, dependency rows, and exact algebra remain reproducible on the
current tree. It does not claim a new theorem, does not set or promote audit
status, and does not perform independent audit work. Audit-lane values are
informational here, not companion pass/fail targets.

**Companion target:** `static_source_readout_i1_accepted_premise_bridge_bounded_note_2026-05-27`
([`STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md))
**Primary runner:**
[`scripts/audit_companion_static_source_readout_i1_dep_resolution_2026_06_04.py`](../scripts/audit_companion_static_source_readout_i1_dep_resolution_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_static_source_readout_i1_dep_resolution_2026_06_04.txt`](../logs/runner-cache/audit_companion_static_source_readout_i1_dep_resolution_2026_06_04.txt)

## Current Boundary

The parent bridge is a bounded accepted-premise bridge for I1 static-source
readout. Given the supplied static-source readout premise `P1`, the
framework-local `Z^3` Green-kernel asymptotic, the sibling I2 identity
`alpha := g_bare^2/(4*pi)`, and the sibling `g_bare` bridge, the parent runner
recomputes the exact substitution chain:

```text
V(r) = -C g_bare^2 G(r)
G(r) -> 1/(4 pi |r|)
alpha := g_bare^2/(4 pi)
V(r) -> -C alpha/|r|
```

The current parent runner reports `PASS=59 FAIL=0`; this companion accepts
later additive parent-runner checks if fail counts remain zero.

The evidence here is current-state evidence. It does not depend on generated
audit-lane values for the sibling I2 row, and it does not decide any audit
status.

## What The Runner Checks

The primary runner checks:

1. the parent runner exits successfully, with at least the current
   `EXACT=48`, `BOUNDED=11`, and `TOTAL=59` passing checks and zero failures;
2. parent, companion, I2, `g_bare`, and Green-kernel ledger rows exist, with
   audit-lane fields printed as metadata only;
3. the parent and I2 source-note hashes match their live ledger rows;
4. the parent runner source does not consult generated audit-status fields
   outside its source-firewall exclusion list;
5. the parent note registers the static-source premise and carries the
   `(B1)`-`(B4)` proof walk without asserting dependence on a dependency grade;
6. the I2 note contains the structural dimensionless-coupling identity and
   keeps I1 isolated as sibling content;
7. independent `sympy` checks rederive the `(B1)`-`(B4)` substitution chain;
8. numerical checks recompute `alpha = 1/(4*pi)`, `C_F = 4/3`, and the sampled
   `V(r)` equality.

## What This Does Not Claim

- It does not claim a new theorem.
- It does not set, change, or predict any audit status.
- It does not resolve the supplied static-source readout premise `(P1)`.
- It does not promote the parent alpha-bare bridge.
- It does not derive the I2 dimensionless-coupling convention from first
  principles.
- It does not derive the sibling `g_bare` premise.
- It does not edit generated ledger, queue, or publication-status files.

The safe downstream use is this meta evidence: the parent source and runner
remain reproducible, the exact algebraic substitution chain still checks
directly, and generated audit-lane values are not used as companion gates.
