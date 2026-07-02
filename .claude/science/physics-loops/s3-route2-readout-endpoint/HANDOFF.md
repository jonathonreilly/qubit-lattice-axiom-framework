# Block37 Handoff

## Summary

Block37 adds a constructive conditional primitive for the S3/Route-2 E-center readout gap.

If a typed source-domain primitive selects one line in the SU(3) adjoint space and the E-center excess reads the normalized complement rank, then:

```text
e_E = 7/8
q_E = 15/8
rho_E = 21/4
c_TE = -8/9
```

all follow exactly. The runner also proves rank 7 is unique among integer adjoint-projector ranks and that line-rank, full-adjoint, and `F_adj=8/9`-as-E-excess readings fail.

Actual status: conditional-support only. The current source bank does not supply the single-adjoint-line selector.

## Artifacts

- `docs/QUARK_ROUTE2_E_CENTER_SINGLE_ADJOINT_LINE_SELECTOR_CONDITIONAL_SUPPORT_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_e_center_single_adjoint_line_selector_conditional_2026_06_21.py`
- `outputs/frontier_quark_route2_e_center_single_adjoint_line_selector_conditional_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/*`

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_single_adjoint_line_selector_conditional_2026_06_21.py` -> `PASS=27 FAIL=0`

Completed focused checks:

- `python3 -m py_compile scripts/frontier_quark_route2_e_center_single_adjoint_line_selector_conditional_2026_06_21.py` -> pass
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py` -> `PASS=103 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py` -> `PASS=14 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_primitive_chain_reaudit.py` -> `PASS=24 FAIL=0`
- branch-local positive-overclaim scan over 16 changed files -> `positive_overclaim_hits=0`

## Scope

This block does not derive the single adjoint line from current primitives. It identifies the exact primitive that would work and records falsifiers for that primitive.

## PR

- PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4567
- Branch: `physics-loop/s3-route2-readout-endpoint-block37-20260621`
- Base: `main`
- Status: open, identity verified only. Conflict/mergeability was not checked.

## Next Action

Try to derive the single adjoint line from current source/support geometry. If absent, prove the sharp no-go for current source-bank line selectors.
