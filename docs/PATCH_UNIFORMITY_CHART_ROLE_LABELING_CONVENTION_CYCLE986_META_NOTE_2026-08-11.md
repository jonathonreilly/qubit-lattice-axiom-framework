# Cycle 986 chart-role labeling convention

Date: 2026-08-11
Cycle: 986
Claim type: `meta`
Audit-status authority: independent audit lane only

This is a convention and audit-binding note, not a physics theorem. It records
no audit verdict and changes no axiom, approved primitive, registry, queue,
policy, or effective-status surface.

## Convention

For a target `t`, first express its closed-star chart in centre-relative wire
roles: centre `C` and the six signed axial directions. Bind each such role to
the coordinate-labelled Boolean site `q_x` at its translated global
coordinate `x`.

A shared-site restriction compares those coordinate bindings. A shared-pair
restriction compares the role-normalized local record: pair incidence,
`Z^3` edge status, Boolean table, dependence class, `J`, changed-edge count,
and canonical global path. “Agreement” means equality of that normalized,
coordinate-bound record.

This convention does not identify distinct global target components and does
not require unrelated target bits to be numerically equal. In particular,
adjacent and diagonal overlap rows compare chart-role formulas, not one
simultaneous global update map. It supplies no infinite allocation or
execution schedule.

## Separation from the bounded theorem

The Cycle-986 finite-patch theorem imports this convention only to define its
chart records. Its algebraic gluing claim is separate: compatible pairwise
record restrictions plus the coordinate-binding site cocycle glue over a
finite union. No theorem is asserted in this meta note.

## Audit-bound refutation checker

Primary runner:
[`frontier_cycle986_patch_uniformity_induction_independent_check_2026_08_11.py`](../scripts/frontier_cycle986_patch_uniformity_induction_independent_check_2026_08_11.py)

Pinned artifacts:

- [`patch_uniformity_induction_cycle986_independent_check_receipt_2026_08_11.json`](../outputs/patch_uniformity_induction_cycle986_independent_check_receipt_2026_08_11.json)
- [`frontier_cycle986_patch_uniformity_induction_independent_check_2026_08_11.txt`](../logs/runner-cache/frontier_cycle986_patch_uniformity_induction_independent_check_2026_08_11.txt)

The checker independently constructs the coordinate bindings and normalized
overlap records, derives their agreement flags, derives base, extension, and
induction outcomes, and rejects its declared mutation campaign. It neither
imports nor executes the primary theorem runner or the pinned Cycle-719
router.
