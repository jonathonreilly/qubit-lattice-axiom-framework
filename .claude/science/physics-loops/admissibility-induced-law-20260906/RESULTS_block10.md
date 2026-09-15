# RESULTS — block 10: the recorded-set Gibbs theorem (2026-09-15)

**Deliverables (branch `physics-loop/admissibility-induced-law-block10-recorded-set-gibbs-theorem-20260915`, stacked on block 09):** the note `docs/ADMISSIBILITY_RULE_RECORDED_SET_GIBBS_THEOREM_FORMATION_LAWS_MARKOV_GRAPH_BOUNDED_THEOREM_NOTE_2026-09-15.md`; the runner `scripts/admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_2026_09_15.py` (18 checks, 10 mutations, exact); the pinned cache; the control `specs/supervisor_control_block10_recorded_set.py` and the refuting pass `specs/supervisor_control_block10_refuter.py` with outputs; `GOAL_block10.md`; `CHECKER_block10_findings.md`; this record.

## Result, in one paragraph

For every finite window and every total formation order, the formation law is the Gibbs law `(1/6)^{n_0} Π_edges K / Π_{|A_x| ≥ 2} K_{|A_x|}(v_{A_x})` (T1), hence a Markov field for the recorded-set graph — the lattice edges plus the pairs inside each recorded set (T2). The vacuum-normalized potential of a positive law on a finite window is unique and, under a Markov hypothesis, supported on cliques (T3a, re-proved); the formation law's term on a maximal recorded set of size `k` is `−m_A Δ_k log K_k`, nonzero whenever the `k`-th mixed difference is nonzero — executed nonzero for `k = 2..6` at `(3,1,2)` and `(5,2,4)`, zero at the constant rule (T3b). Since co-recorded neighbors are never adjacent on the bipartite lattice, a formation law is a nearest-neighbor Markov field iff every recorded set has at most one element (T4) — block 01's condition, now for the Markov property — and otherwise it is Markov for no graph missing a co-recorded pair; the induced interaction reaches distance `√2` and `2` with genuine `k`-body terms up to six (T5). Executed canonical potentials: the plaquette with its last site recording two (pair term `12/13` on the co-recorded non-adjacent pair, zero on the other non-edge on all 1296 configurations) and the star with its center last (three-body term `165/169` on the leaves) (T6). No order is selected.

## Certificate
- Runner: `TOTAL: PASS=18 FAIL=0`; 10 mutations each in its family; no floating-point literal; classical names only under Prior art and Imports.
- Refuting pass (closed-form `exp(−Δ_k log K_k)` against the Möbius inversion; the vacuum moved to `−x`): equal / same verdicts (`CHECKER_block10_findings.md`).
- Claim type `bounded_theorem`; status `bounded-support`; trace `upstream_support`; audit required.

## Not claimed
Nonzero mixed differences at every nonconstant triple; infinite-volume laws for non-monotone classes; non-product rules.
