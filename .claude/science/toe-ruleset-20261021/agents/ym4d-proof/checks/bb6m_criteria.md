# bb6m criteria (lane B session 6, RS5-10; written before checks/bb6m_mask.py exists)

Ternary (arity 3) Deslauriers-Dubuc interpolatory masks DD4, DD6, DD8 (Lagrange interpolation through 4/6/8 coarse nodes
centred on the coarse interval, evaluated at offsets ±1/3; a_0 = 1, a_{3j} = 0 for j ≠ 0). σ(z) := 1 + z + z².
Exact integer/rational arithmetic only (Python ints and Fractions); floats only for the final logarithms.
- M1: Σ_j a_{3j+r} = 1 for r = 0, 1, 2 exactly; a(z) divisible by σ(z)³ exactly (remainder 0). PASS required.
- M2: e := 9a/σ³; ρ_n := ||S_e^n||_∞^{1/n} (max over residues mod 3^n of the ℓ¹ norm of the coefficients of
  e(z)e(z³)…e(z^{3^{n-1}}) in that residue class). For DD8 at the largest n run (n ≤ 10): β_n := -log_3 ρ_n ≥ 0.47 (the
  reviewer's value 0.4732 at n = 10, REVIEW_BFT_B_S5 Part D). PASS required.
- M3: for DD6 at n ≤ 10: β_n ≥ 0.25 for the largest n run (reviewer: 0.2677 at n = 10). PASS required.
- M4: for DD4: ρ_n ≥ 1 for every n run (no C² certificate; consistent with the reviewer's spurious eigenvalue). PASS required.
- M5 (informational): the DD4 4-point weights at offset 1/3 equal (-5, 60, 30, -4)/81.
Verdict: ALL PASS iff M1-M4. Resources < 1 GB, < 20 min; numeric lock.
