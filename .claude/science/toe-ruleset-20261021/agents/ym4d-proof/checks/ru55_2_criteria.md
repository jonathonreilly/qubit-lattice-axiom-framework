# ru55_2 — criteria (written BEFORE checks/ru55_2_variants.py and checks/ru55_2_dag.py exist; time stamped by `date -u` below)

Question: RLARGE_U55 §1.5, §2.5 and §3.4 — do the proposed changes (W-cb♯; the θ/a_A order; FI-1's γ condition) create a cycle
or a K-/T-growth in SMALLNESS_DAG's graph? Method: SMALLNESS_DAG §11's own recipe ("to test a proposed change, edit a copy of
checks/dag55_2_graph.py under a new id and re-run the checker"). The checker logic is NOT copied or edited: the driver imports
the functions of checks/dag55_2_dag.py (schema, string_audit, adjacency, tarjan, nontrivial, propagate, witness,
condensed_order, controls) and the data of checks/dag55_2_graph.py, read-only, and builds the variants below in memory
(deep copies). Plain python 3, standard library, no floats.

Variants (every added node/edge carries a file + verbatim string; the string audit S2 must PASS for each variant):
- V0 baseline = dag55_2's graph unchanged.
- V1 (W-cb♯, RLARGE_U55 §2.2): remove the (TC) edge eta_q → eps_loc [le]; add node eta_star (η*, tier 2, live) with def edges
  from eta_q, eps_loc, N, A_d; add eta_star → a_cb [def]; a_cb keeps its other inputs.
- V2 (quietness-threshold form, §2.4): remove the (TC) edge; add node eta_quiet (η′ := η_q/R) with def edges from eta_q, eps_loc,
  N, A_d; add eta_quiet → a_cb [def] and eta_quiet → a_ret [def] (a_ret^{PLD}'s binding (β) entry prices non-quiet sea cubes at
  the quietness threshold).
- V3 (route (iii)'s a_A, literally): V0 + theta → a_A [def] (PLD.md "a_A := min{λκε_1²/256, 6θa_bad}").
- V4 (the order of §1.5): V3 − (a_A → theta [le]) + node a_A0 (a_A°, θ-free entries) with def edges kappa_RL → a_A0,
  eps1 → a_A0, edges a_A0 → theta [le] ("θ := min{θ_cap, a_A°/a_bad}") and a_A0 → a_A [def] ("a_A := min{a_A°, 6θa_bad}").
- V5 (FI-1's γ condition, §3.2): V0 + R → gamma, kappa_RL → gamma, L → gamma [le] (beta0p → gamma already exists).
- V6 = V1 + V4 + V5 (the three accepted changes together).

Verdict rules (pre-registered):
- V0 must reproduce dag55_2: B-strict 0 nontrivial SCCs; B-all exactly 2 nontrivial SCCs of sizes 12 and 4; DAG-F2 live seeds
  ['C_fun', 'V_LF']. If not, the driver is unable to decide (stop).
- U3 NO-CYCLE: PASS iff V1 has 0 nontrivial B-strict SCCs AND V1's B-all SCC family equals V0's (as sets of node sets).
- U3 NO-GROWTH: PASS iff V1's live GROWTH (K/T/Tk) seeds equal V0's AND eta_star is not in V1's GROWTH-taint set (live subgraph)
  AND eta_star's UNIFORMITY-NOT-ESTABLISHED taint status equals eps_loc's in V0 (it inherits ε_1's, nothing new).
- U3 ORDER: PASS iff in V1's live B-strict order pos(eta_q) < pos(eta_star), pos(eps_loc) < pos(eta_star), pos(eta_star) < pos(a_cb),
  and the order's validity re-check PASSes.
- U3 SCOPE (informational, not pass/fail): report descendants(eta_star) in V1 and descendants(eta_quiet) in V2 (B-all edges);
  statement "W-cb♯ touches strictly fewer nodes" is reported TRUE iff desc_V1(eta_star) ⊊ desc_V2(eta_quiet).
- U1 LITERAL 2-CYCLE: V3 must report a nontrivial B-strict SCC containing a_A and theta (else "claim not reproduced").
- U1 RESOLVED: PASS iff V4 has 0 nontrivial B-strict SCCs. Report V4's B-all SCC family (membership changes vs V0 are reported,
  not pre-judged).
- FI-1 NO-CYCLE: PASS iff V5 has 0 nontrivial B-strict SCCs AND V5's B-all SCC family equals V0's AND gamma precedes g1_FLOW and
  g0 in V5's live B-strict order.
- V6: PASS iff 0 nontrivial B-strict SCCs, live GROWTH seeds equal V0's, and the checker's own controls C1-C7
  (dag55_2_dag.controls) report ABLE TO DECIDE on V6.
Controls of this driver: C-A (the V3 positive control above must FIRE); C-B (re-inserting the (TC) edge AND an edge
a_cb → eta_q into V1 must create a B-strict SCC — shows that the driver would see a cycle through the new node); C-C (seeding
eta_star with a K tag in V1 must taint g0 — shows the growth propagation reaches the sink through the new node).
Written at (date -u, appended): 2026-10-29T00:36:01Z
