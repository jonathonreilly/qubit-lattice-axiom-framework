---
claim_id: ckm_cp_phase_arctan_sqrt5_bridge_reduction_open_gate_note_2026-06-08
claim_type_author_hint: open_gate
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# CKM CP Phase arctan(sqrt5) Bridge Reduction Open Gate

**Date:** 2026-06-08
**Claim type:** open_gate.
**Review boundary:** exact bridge reduction plus open residual; no admission,
Tier-A registration, primitive approval, no-go, or audit-status change.
**Primary runner:**
[`scripts/ckm_cp_phase_arctan_sqrt5_bridge_reduction_open_gate.py`](../scripts/ckm_cp_phase_arctan_sqrt5_bridge_reduction_open_gate.py).

## Result

The CKM-atlas phase identity
`delta_CKM = arccos(1/sqrt(6)) = arctan(sqrt(5))`
([`CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md`](./CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md),
[`CKM_ATLAS_AXIOM_CLOSURE_NOTE.md`](./CKM_ATLAS_AXIOM_CLOSURE_NOTE.md))
reduces to one supplied bridge:

```text
cos^2(delta) = 1 / n_quark .
```

The exact forced skeleton is smaller than the full CKM-atlas interpretation:

- If `rho = radius * sqrt(w_sym)` and
  `eta = radius * sqrt(1 - w_sym)`, then
  `cos^2(delta) = rho^2 / (rho^2 + eta^2) = w_sym`; the radius cancels.
- The democratic projection of one basis state in an `n`-state module has
  weight `w_sym = 1/n`.
- With the supplied choice `n_quark = 6`, this gives
  `cos^2(delta) = 1/6` and `delta = arctan(sqrt(5))`.

The open residual is the bridge that supplies the interpretation of
`w_sym = 1/n_quark` for the physical CKM CP phase: the CP-even/CP-odd channel
assignment, the `1 + 5` projector split, and the choice of `n_quark = 6` as the
relevant count.

## Open-Gate Evidence

The runner exhibits the residual rather than asserting a global no-go:

- Other symmetric-block choices on the same six-state module give different
  angles: `2 + 4 -> 54.736... deg` and `3 + 3 -> 45 deg`.
- A three-generation democratic count gives `arccos(1/sqrt(3))`, not the atlas
  angle, so the weak-times-color count is load-bearing.
- The inverse-square count identity is an exact re-encoding of the same
  `(rho, eta)` values, not an independent selector.
- The cited `K_R` carrier surface
  [`S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`](./S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md)
  is `claim_type: open_gate` and says the physical tensor-primitive meaning is
  asserted, not derived. Despite its filename, it is not an approved framework
  primitive in
  [`docs/audit/data/axiom_premise_nodes.json`](./audit/data/axiom_premise_nodes.json).
- The narrow rho/eta theorem
  [`CKM_CP_PHASE_RHO_ETA_TO_DELTA_NARROW_THEOREM_NOTE_2026-05-10.md`](./CKM_CP_PHASE_RHO_ETA_TO_DELTA_NARROW_THEOREM_NOTE_2026-05-10.md)
  explicitly does not derive the `1 + 5` projector split.

## Non-Claims

This note does not claim:

- `delta_CKM = arctan(sqrt(5))` is false;
- the CKM-atlas package is internally wrong;
- no future derivation of the bridge can exist;
- `delta_CKM` is a Tier-A admission or approved primitive;
- Record, Lattice, Quantum, or the scale-reference primitive supply the bridge;
- any empirical gamma comparator is a derivation input or forward falsifier;
- an audit verdict or effective-status change.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`CKM_ATLAS_AXIOM_CLOSURE_NOTE.md`](./CKM_ATLAS_AXIOM_CLOSURE_NOTE.md)
- [`CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md`](./CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md)
- [`CKM_CP_PHASE_RHO_ETA_TO_DELTA_NARROW_THEOREM_NOTE_2026-05-10.md`](./CKM_CP_PHASE_RHO_ETA_TO_DELTA_NARROW_THEOREM_NOTE_2026-05-10.md)
- [`S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`](./S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md)

## Verification

Run:

```text
python3 scripts/ckm_cp_phase_arctan_sqrt5_bridge_reduction_open_gate.py
```

Expected:

```text
SCORECARD PASS=13 FAIL=0
```
