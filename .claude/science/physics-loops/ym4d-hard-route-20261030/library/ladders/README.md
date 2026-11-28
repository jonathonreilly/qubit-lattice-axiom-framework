# Build ladders for the purity campaign

Owner, 2026-11-28: "Each of these can have its own ladder of work if needed." Earlier the same day: "Build the new math and physics we need to solve the crux - and keep using our LLM bandwidth to do so."

One file per component. Each file holds the target, the rungs in order, and for each rung its status, the row that works it, and its gate. Rules:
- A rung is one statement with quantifiers and constants, small enough for one lane.
- When a lane closes a rung (PROVED and checked by the other provider, or refuted), the lead marks it and queues the next rung at once.
- A lane may split a rung. It records the split in its output; the lead copies it here.
- Every rung that claims to read SU(2) passes the U(1) twin test of the crux card (library/gap-purity-crux-card.md section 3).
- A refuted rung is kept, with its counterexample, and the ladder is rerouted, not dropped.

Ladders: LD.md, PS.md, LOOPEQ.md, THM-T.md (the large-N gap, rows 1708-1722); CARRY.md (A1); RANK.md (candidate A of row 1707); LOCAL.md (candidate B of row 1707, for ExpClusters); LEAN.md (the Lean consumer).
