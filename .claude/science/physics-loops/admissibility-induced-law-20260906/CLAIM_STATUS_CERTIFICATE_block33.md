# Claim status certificate — block 33 (close, 2026-09-17)
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "T1 proved (extension lemma; seed lemma by the fork-below construction; the inductive step; the reduction of the unit budget E <= 3(|S|-1) + |A| to the tight-sibling lemma), instances executed by exact rooted brute force on 140 tiny realizations where the rooted inequality holds at all 788 sites; T2 exact on the extremal realizations (tight roots with predecessors at -1) and executed on ~10^4 realizations (no violation, no tight siblings); T3 exact certificates for the one-processed-child count at (2921,1,2), (1464,1,1), (5841,2,4), (4380,1,3) with c = 2 and (405,1,2), (208,1,1), (810,2,4), (605,1,3) with c = 1, with block 30's certificate passing the same code; T4 executed: the restriction admissible on tiny realizations and at c = 1 on 125 realizations, not cost-free at c = 2 (W3: -61 against -62). The tight-sibling lemma and the restriction's admissibility are open; no region is claimed. Conditional on the records-only reading, positivity, the six-axis menu and the monotone order as the automaton's supplied meaning"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "three-line lemmas about rooted trees of the counted family with an exhaustive case analysis; exact super-solutions of a modified recursion whose up-factor is a symbolic identity; exact enumeration on tiny realizations; the open statements labelled and unclaimed"
dependency_classes: "one premise node (minimal_axioms); block 01 (on main; proposed, unaudited); blocks 25, 30, 31, 32 (open PRs) for the recursion, the automaton and budget, the witnesses and certificates, the family and the extremal realizations — restated and re-executed"
open_imports: "the records-only reading; positivity; the six-axis menu; the monotone order with corner (+,+,+)"
review_loop_disposition: pending (supervisor-run block; author checks only)
independence_class: "single seat (Fable, supervisor): controls (integer program with a level cap; hard-case listing; candidate lemmas; climbs; shape statistics; the kind-typed count; certificates), contract with a lens pass, primary, refuting pass by the integer program, an independent assembly of the seed lemma's trees through the runner's verifier, two independent iterations of the restricted count, and an adversarial climb, fold (the seeds' rooted value; two divergences of the eight-variable count)"
audit_required_before_effective_retained: true
bare_retained_allowed: false
