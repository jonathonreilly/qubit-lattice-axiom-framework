trace_class: upstream_support
target_claim_id: "2026-05-03-gbare-parent-retention-gate"
target_blocker_text: "The only non-circular route to forcing N_F is to make the per-site spin-double-cover normalization propagate to the gauge su(3) by derivation rather than by the bridge admission."
source_of_blocker_text: audit_strategy_finding
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Use this split to target V_3 trace-surface closure without treating the species-label bijection as load-bearing for g_bare."

# Trace Gate

If true, this artifact supports the `g_bare` parent route by narrowing the
staggered-Dirac dependency: `g_bare` needs the physical `V_3` trace surface and
per-site-to-gauge SU(2) scale bridge. It does not need a forced species-label
bijection. The artifact does not close the parent gate.
