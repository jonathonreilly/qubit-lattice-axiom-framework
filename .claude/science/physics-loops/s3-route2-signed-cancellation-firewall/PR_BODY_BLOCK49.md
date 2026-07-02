# Summary

This physics-loop block tests the signed affine one-pole escape:

```text
F_X = a / w_X + b.
```

Exact arithmetic shows the endpoint fit exists only with `b=-6a/5`, so every
nonzero fit uses a negative coefficient. Coefficient-positive affine
source/readout rules cannot reach `9/4`; pointwise positivity alone still
allows the signed fit and therefore is not a selector theorem.

# Honest Status

- actual current-surface status: `no-go`
- conditional status if signed selector/firewall is derived/admitted: exact support
- trace class: `negative_route_pruning`
- no audit verdicts applied
- no repo-wide authority surfaces edited
- no claim over arbitrary future signed or nonlinear observables

# Artifacts

- Note:
  `docs/QUARK_ROUTE2_SIGNED_CANCELLATION_FIREWALL_NOTE_2026-06-21.md`
- Runner:
  `scripts/frontier_quark_route2_signed_cancellation_firewall_2026_06_21.py`
- Output:
  `outputs/frontier_quark_route2_signed_cancellation_firewall_2026_06_21.txt`
- Loop pack:
  `.claude/science/physics-loops/s3-route2-signed-cancellation-firewall/`

# Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_signed_cancellation_firewall_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_signed_cancellation_firewall_2026_06_21.py
PYTHONPATH=scripts python3 scripts/frontier_route2_readout_record_positivity_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_channel_readout_naturality_no_go.py
git diff --cached --check
```

Results:

- new runner: `PASS=92 FAIL=0 TOTAL=92`
- `py_compile`: pass
- record/positivity parent: `TOTAL: PASS=8 FAIL=0`
- E-center blindness parent: `TOTAL: PASS=14, FAIL=0`
- E-channel naturality parent: `TOTAL: PASS=28, FAIL=0`
- exact readout parent: `PASS=11 FAIL=0`
- staged diff check: pass
- overclaim scan: pass

No audit verdicts were run or applied. No mergeability or conflict checks are
part of this physics-loop PR.

# Remaining Target

Define and test a larger nonlinear tensor-observable class, or pivot to a
different direct consumer if the endpoint route remains blocked.
