# r55k_2 — POST-HOC criteria (written after reading checks/r55k_1_out.txt, BEFORE checks/r55k_2_posthoc.py exists)

Reviewer model: claude-opus-5-5. Same arithmetic rules as r55k_1 (rational intervals, outward rounding). Everything in
r55k_2 is POST-HOC: it was designed after seeing r55k_1's D-block (the F / Stage-1 radius inconsistency) and the A3
verdict-code defect. It carries pre-registered verdicts below, but its existence is post-hoc and is labelled so.

- P1  Re-run the QFIX chain (P-max, |𝒩_S| = 3, c_N = 2, C_3 = 1, m(q) chosen so that A_cγ_c ≤ 1) with a radius
      allocation that is CONSISTENT with Stage 1:
      (a) EPSSTAR's own Stage-1 radii: Stage-1 gap R/4 − 4, Stage-2 budget R/4 − 3, R_0 = 64, F = r55k_1 D2's max F;
      (b) re-allocated: Stage-1 gap R/16 − 4, Stage-2 budget 7R/16 − 3, R_0 = 256, F = r55k_1 D3(c=16)'s max F,
          Stage-1 cut-off coefficient 256·16² = 65536 in place of 4096.
      Report C_T(q), C_D(q), ε_1^cut(q) at q ∈ {8, 11, 12, 16, 32, 100, 1000, ∞}, the real q at which C_D = 6.7·10¹⁵,
      and the lever obj(∞) − obj(8).
      P1-i   PASS ("q = 12 meets C_D ≤ 6.7·10¹⁵ under EPSSTAR's own radii") iff C_D(12; a) ≤ 6.7·10¹⁵.
      P1-ii  PASS ("EPSSTAR/QFIX's ε_1^cut(12) survives a consistent allocation to 0.1 decade") iff
             |log10(ε_1^cut(12; b)/1.2948·10⁻⁴⁴)| ≤ 0.1.
      P1-iii PASS ("the 24.089-decade lever is allocation-independent to 0.01 decade") iff |lever(b) − 24.0891| ≤ 0.01.
- P2  c′_ϑ at ϑ = 1/2 equals 1 exactly (pure Fraction arithmetic, no transcendental): PASS iff exactly 1.
- P3  Fixed F = 175.8, R_0 = 64, q = 12, P-max, A_cγ_c ≤ 1: minimum of C_T over the δ-budget grid δ_2 ∈ {j/400},
      T ∈ {j/1000}, with ρ ∈ {1/16, 1/1000} (ρ only enters κ): REPORT the smallest value found (an achievable value,
      i.e. an upper bound on the true minimum) — compared with EPSSTAR l.608's 4.4·10¹².
