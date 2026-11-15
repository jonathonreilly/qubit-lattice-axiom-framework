# r55b_num — criteria for the exact-rational number checks (written before the script)

- **N1 (K_f, BFT_B §29.3 / §27.2):** x := 3^{−9/4}; decide by x⁴ = 3^{−9} with rational endpoints: PASS iff
  8.737 ≤ 8/(1 − x) ≤ 8.74. Also report whether the printed intermediate "3^{−2.25} = 0.08434" lies in a rational
  interval containing x (expected NOT: true x ∈ [0.08442, 0.08443]); this is recorded, not a FAIL of K_f.
- **N2 (C_C base, §35.4):** 1 + 8·(27/26) = 121/13 ≤ 9.31 exactly. PASS/FAIL.
- **N3 (ΓT-op (d) constant, §25.1 (d) / §36.2):** 2M_n/n = 4(4n + 1)/n ≤ 20 for n = 3^k, k = 1..12, exactly; and the
  1D-Green identity behind Lemma N1G: for the cycle Z_M, g(t) := (t − M/2)²/(2M) satisfies −Δg = δ_0 − 1/M exactly and
  2(g(0) − g(M/2)) = M/4, for M = 4, 6, 8, 10, 12, 50. PASS/FAIL.
(Copied verbatim from checks/r55b_dip_criteria.md's r55b_num section at 22:44:58Z UTC, before any r55b script exists.)
