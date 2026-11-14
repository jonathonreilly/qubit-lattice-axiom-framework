# dag55_2 — criteria (written 2026-10-28, BEFORE checks/dag55_2_graph.py and BEFORE checks/dag55_2_dag.py exist)

Why a second id: dag55_1 ran (checks/dag55_1_out.txt, kept unaltered). Re-reading its output against the sources, I found
seven omissions in the GRAPH DATA (no code defect). Per dag55_1's own rule, the corrected graph runs under a new id; dag55_1's
criteria, graph, script and output are not edited.

## Rules: identical to checks/dag55_1_criteria.md, including Addendum A (S2 string audit, C7), unchanged
Same data model, same verdict rules A-E, same controls C1-C7 with the same pass conditions. The script
`checks/dag55_2_dag.py` is a byte copy of `checks/dag55_1_dag.py` except for the graph path constant (dag55_1_graph.py →
dag55_2_graph.py); nothing in the logic changes.

## The seven graph corrections (all additions; no dag55_1 node or edge is removed or re-typed)
1. Node R0 (R_0, FLOW's UNIV-1L deviation): add growth tag `unstated-K` — RLARGE §4.2 row 1 records "k-uniform vector step
   gap OPEN [s]" for Theorem UNIV, of which (UNIV-1L) (hence R_0) is the consequence.
2. Edges L → C_fun and kappa_pm → C_fun (def): the row size the level count multiplies is "π_l(V_l) ≤ 2C_NCC_bchκ_+L²η²"
   (REVIEW_BFT_B_S9_S10 S10-6).
3. Edge tau_sizes → q_RES (def): RES-dec's ratio "q := L⁻³ + C_qτ" depends on the smallness τ.
4. Edges alpha_star → lam_bg and C_Delta → lam_bg (def): the session-23 class gap is evaluated on the class C_Δα_* = 1.0568·10⁻³
   (PROOF CS-1).
5. Edge C_Delta → c_inf (def): 𝔠_∞ contains "+ C_Δα_*".
6. Edges L → K_FP and d → K_FP (def): K_FP is a function of c_D(L), s_M(L) and d.
7. Edge c_A → B_0 (def): HW §13.2's B_0 := B_1 + c + 1 contains (PRICE^ℛ)'s c, which HW §18.1's Remark identifies with c_A.
Also (informational, no verdict effect): node lambda_star gains string2 = RLARGE §5.4's "log C_ℓ ≈ (3n_int/2)·log(1/(1 - λ_*)) ≤
324·log(4/3) ≈ 93 at λ_* ≤ ¼" (the a-priori bound that keeps C_ℓ g-independent).

## Pre-registered expectations (stated so that a different outcome is visible, not as a pass condition)
Corrections 1-7 add edges INTO nodes that already lie downstream of their new sources, except 7, whose source c_A is already in
dag55_1's B-all SCC with B_0. I expect no change in the B-strict verdict (NOT FOUND); if B-strict reports a cycle, that cycle is
a finding and is reported as such. Correction 1 adds one more uniformity-not-established seed on the live route.
