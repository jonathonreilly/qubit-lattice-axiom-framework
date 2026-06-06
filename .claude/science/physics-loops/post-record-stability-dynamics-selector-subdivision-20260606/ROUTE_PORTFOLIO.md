# Route Portfolio

## Route A: Read-only stability/dynamics subdivision

Status: executed.

Use the upstream selector/dial subdivision and split its 64
`stability_or_dynamics_selector` rows into `flow_or_thermal_stability` and
`arrow_or_dynamics_bridge`.

Reason for selection: it directly operationalizes the user's point that a
stable setting can sit on the dial without being forced as the selected dial.

## Route B: Flow/thermal stable-setting certificate

Status: next candidate.

For rows in `flow_or_thermal_stability`, identify which already have supplied
finite maps, monotone flows, fixed points, attractors, separatrices, or thermal
rules. Output would be a conditional-stability certificate, not a selector.

## Route C: Arrow/dynamics bridge obstruction map

Status: next candidate.

For rows in `arrow_or_dynamics_bridge`, separate physical-arrow imports from
kernel/Hamiltonian/instrument imports. Output would expose which rows need
production dynamics rather than more audit bucketing.

## Route D: Measure/weight/normalization subdivision

Status: queued.

Subdivide the 41 `measure_weight_normalization` rows from the selector/dial
bucket. This is independent of the current stability/dynamics split after the
shared upstream branch lands.

## Route E: Generation/Koide stable-location lane

Status: queued with firewall.

Treat Koide/generation entries as possible stable locations under supplied
surfaces and score rules only. Do not force or select the dial.
