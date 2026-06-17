# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| B-AXIS.1 supplied blocked time step | Clock unit for single-clock consumers | declared premise | single-clock source note | yes | yes | future retained time-step theorem or accepted primitive | not retired here |
| B-AXIS.2 evolution axis/transfer construction | Axis label and transfer surface | declared premise | single-clock source note | yes | yes | per-axis BC-asymmetry theorem or registration-direction bridge | not retired here |
| B-AXIS.3 no independent commuting clock factor | No-second-clock exclusion | declared premise | single-clock source note | yes | yes | theorem excluding independent commuting positive transfer factors | not retired here |
| Current single-clock runner | Verification of axis-conditional finite-block clauses | computed support | scripts/axiom_first_single_clock_codimension1_evolution_check.py | yes | yes | maintained by this PR | guard repaired |
| Direct-consumer firewall runner | Verification that stale wording is removed from scoped consumers | computed source hygiene | scripts/single_clock_baxis_consumer_firewall_check_2026_06_17.py | yes | yes | reviewer may extend target list | added |
