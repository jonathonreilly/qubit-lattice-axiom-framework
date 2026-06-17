# Handoff

This PR repairs source consumers of the single-clock row so they no longer
inherit an unconditional or retained axis-selection claim.

Changed consumers now say that single-clock use is conditional on B-AXIS:
one supplied blocked time step, one declared evolution axis/transfer
construction, and no admitted independent commuting transfer factor.

The PR intentionally does not derive B-AXIS, edit audit data, retag ledger
rows, or land anything to `main`. The reviewer should decide whether to extend
the firewall to additional lower-impact consumers.

Verification:

```bash
python3 scripts/single_clock_baxis_consumer_firewall_check_2026_06_17.py
python3 scripts/axiom_first_single_clock_codimension1_evolution_check.py
python3 -m py_compile scripts/single_clock_baxis_consumer_firewall_check_2026_06_17.py scripts/axiom_first_single_clock_codimension1_evolution_check.py
```
