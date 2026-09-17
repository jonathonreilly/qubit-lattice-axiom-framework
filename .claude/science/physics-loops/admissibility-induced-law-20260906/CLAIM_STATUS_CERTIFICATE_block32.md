# Claim status certificate — block 32 (close, 2026-09-17)
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "T1 proved (component lemma; single-seed characterization; the exact level dynamic program) and executed against brute force on tiny realizations. T2 proved by exhibition with exact enumeration: on Z_A and Z_B every tree of the counted family has E >= 3(|S| - 1) + |A| (minimum 0 at c = 1, positive at 99/100), so the family's constant is at least 1 and no construction within the family has c < 1. T3 by exhibition: c*(W1) = 3/4, verified trees at 4/11 (W2) and E - 3(|S|-1) = -12 (W3). T4 exact: the stake p >= 453/232/905/677 conditional on a construction with c = 1 (not claimed); the floor p = 368 on (p, 1, 2) unconditional for the family counted by block 25's recursion. Executed, not claimed: c* never above 1 in about 10^4 realizations (conjecture c* = 1). Conditional on the records-only reading, positivity, the six-axis menu and the monotone order as the automaton's supplied meaning"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "a family-level lower bound by explicit realizations re-executed through the declared automaton with an exact dynamic program whose correctness is proved from the family's structure and cross-checked by brute force; the floor by a one-variable maximum and t^c <= t; the stake by exact super-solutions"
dependency_classes: "one premise node (minimal_axioms); block 01 (on main; proposed, unaudited); blocks 25, 30, 31 (open PRs) for the family, the automaton, the recursion, the witnesses and the certificates, restated and re-executed; block 28 (open PR) as the evidence address for the located strength"
open_imports: "the records-only reading; positivity; the six-axis menu; the monotone order with corner (+,+,+)"
review_loop_disposition: pending (supervisor-run block; author checks only)
independence_class: "single seat (Fable, supervisor): controls (integer program; two dynamic programs; brute-force cross-checks; climbs), contract with a lens pass, primary, refuting pass by the integer program in floating point, a numpy rule, union-find components, brute force on further realizations and simulated annealing, fold (a constant in the general program; a wrong baseline in one check)"
audit_required_before_effective_retained: true
bare_retained_allowed: false
