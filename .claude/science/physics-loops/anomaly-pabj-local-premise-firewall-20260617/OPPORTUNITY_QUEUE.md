# Opportunity Queue

1. `anomaly_forces_time_theorem` P-ABJ local-premise firewall.
   - Expected movement: parent row should become audit-ready after the audit
     pipeline rebuilds the citation graph, because the only non-ready one-hop
     dependency was the conditional ABJ child row.
   - Risk: auditor may still judge local P-ABJ as a conditional premise, but
     that is science status, not queue readiness.

2. P-REC positive bridge.
   - Expected movement: would attack the main remaining science blocker after
     #4191's no-go for the naive epsilon shortcut.
   - Risk: hard frontier science, not suitable for this small source-graph PR.

3. P-HY/P-COMP strengthening.
   - Expected movement: could strengthen the ABJ child row and parent theorem.
   - Risk: #4192 already packages bounded support; avoid duplicate work.
