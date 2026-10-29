# ru55_2b — criteria (written BEFORE checks/ru55_2b_dag.py exists; `date -u` appended)

Why: CODEX_REVIEW_DAG.md §3.1 (Codex gpt-6-astra, completed 2026-10-29 00:13:04 UTC, read after ru55_2 ran) finds an omitted
cutoff-family edge n_sharp → SC_k [implicit] (PLD l.378: "𝒢_x := Σ_{N≤n_♯}Σ_{S∋x}𝓖^{(N)}_S/|S|") and reports that adding it to
dag55_2's graph enlarges the cutoff SCC from 12 to 14 nodes (adding SC_k and a_ret). Question for U1: is a_ret inside the
cutoff loop on every route, or only through route (ii)'s K12 fallback edge a_ret → theta ("Without (EG), θ ≤ a_ret/a_bad")?
Same driver functions as ru55_2 (checker functions of dag55_2_dag.py, read-only; variants from ru55_2_variants.py, read-only).

Variants:
- W0 := ru55_2's V0 + n_sharp → SC_k [implicit] (string: PLD.md "𝒢_x := Σ_{N≤n_♯}Σ_{S∋x}𝓖^{(N)}_S/|S|").
- W6 := ru55_2's V6 + the same edge.
- W8 := W6 − the edge a_ret → theta [le] (route (iii)/(iv): K12 settled without a_ret, PLD l.2548-2549).
Pre-registered verdict rules:
- REPRO: W0's B-all cutoff SCC has 14 nodes and contains SC_k and a_ret (reproduces Codex). Else report the difference.
- B-strict: W0, W6, W8 all have 0 nontrivial B-strict SCCs (the added edge is implicit). PASS iff so.
- U1-LOOP: report, for W6 and W8, whether a_ret and theta lie in the cutoff SCC. Claim to test (RLARGE_U55 §1): "a_ret
  is in the cutoff loop only through the fallback edge" ⟺ (a_ret ∈ SCC in W6) and (a_ret ∉ SCC in W8). Reported TRUE/FALSE.
- Control: W8 + an injected edge gamma0 → n_sharp [le] must put a_ret back into a nontrivial B-all SCC (shows the test can
  see a return path through a_ret's only remaining successor chain).
Written at (date -u, appended): 2026-10-29T00:42:37Z
