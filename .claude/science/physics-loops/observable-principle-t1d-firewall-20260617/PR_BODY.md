## Summary

This PR repairs downstream retained-language laundering for the conditional
observable-principle T1-d boundary.

The current source already proves T1-d is independent of the minimal axioms and
determinant algebra. This branch takes the audit blocker's second route: keep
downstream citations explicitly scoped to that conditional boundary.

## Honest Status

- Actual current surface status: bounded-support.
- Trace class: direct_blocker_closure for the scoping half of the blocker.
- Not a T1-d derivation.
- Not a retained/proposed-retained claim.
- Independent audit still decides any effective status.

## Artifacts

- `docs/OBSERVABLE_PRINCIPLE_T1D_DOWNSTREAM_CITATION_FIREWALL_2026-06-17.md`
- `scripts/frontier_observable_principle_t1d_downstream_citation_firewall_2026_06_17.py`
- `logs/runner-cache/frontier_observable_principle_t1d_downstream_citation_firewall_2026_06_17.txt`
- `.claude/science/physics-loops/observable-principle-t1d-firewall-20260617/HANDOFF.md`
- `.claude/science/physics-loops/observable-principle-t1d-firewall-20260617/TRACE_GATE.md`
- `.claude/science/physics-loops/observable-principle-t1d-firewall-20260617/CLAIM_STATUS_CERTIFICATE.md`

## Checks

```bash
PYTHONPATH=scripts python3 scripts/frontier_observable_principle_t1d_downstream_citation_firewall_2026_06_17.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_observable_principle_t1d_downstream_citation_firewall_2026_06_17.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_observable_principle_t1d_downstream_citation_firewall_2026_06_17.py
python3 -m py_compile scripts/frontier_observable_principle_t1d_downstream_citation_firewall_2026_06_17.py
git diff --check
```

Review-loop disposition: reviewer-owned, not run in this branch.
