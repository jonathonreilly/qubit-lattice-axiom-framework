lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T12:11Z

# Row 981, `gap-ladder-check-opus`: line-by-line check of row 978 (`library/gap-ladder-max.md`)

Check item, N1 of `library/gap-ladder-max.md` Section 8. Checker: Claude Opus 5.5, max effort, Mac mini worker 2, fresh session started 2026-11-15T00:11Z at commit 5093baf30 on `claude/ym4d-hard-route`. Author of the checked text: Claude Fable 5.2 (row 978). This is a different model from the author, but the same vendor; it is not an independent check in the sense of a different derivation unless stated per step. No new attack (row 981 scope). No numeric run.

## Plan (at most eight steps; one per response)

1. Read FINISH.md rules (build on published work, efficiency, rules) and `library/gap-ladder-max.md` Sections 5.1, 5.2, 5.6, 5.7, 8 and the (R2) claim; record the exact statements under check with line numbers.
2. Check Lemma IHC (5.1) line by line.
3. Check Corollary CU (5.2) and the derivation of (TH); read `library/gap-phys-seed.md` 1.1.5 (iii) and its conditional check (row 727).
4. Read in the account (CA-I/II/III at 31a47c543775) the two assumptions left by row 727: (a) V = E_m in one normalisation of Z; (b) delta_vac-bar uniform in the cutoff; quote file and line.
5. Check 5.6 (a).
6. Check 5.7 (the square-root test).
7. Check (R2): the size test K_a grows like 3 log(1/a) + log beta in physical units.
8. Verdict table (HOLDS / HOLDS AFTER CORRECTION / FAILS, with the line) and RESULT line.

## Progress log

- 2026-11-15T00:11Z: file created; step 1 starting.

## Step 1. What is under check (read 00:12Z-00:20Z)

Read in full: `library/gap-ladder-max.md` at 5093baf30 (283 lines, 52,293 bytes; last relay commit 0bb19c7ce). FINISH.md sections Joining, Working efficiently, Rules, How we work. Line numbers below are of `gap-ladder-max.md` at that commit.

| Item | Lines | Claim |
|---|---|---|
| Lemma IHC, statement | L121-123 | (HC-vac)_alpha on B gives X(2s + 2m; B) <= theta_m X(2s; B), theta_m = 1 - tanh(alpha m), for all integers s >= 1, m >= 0 |
| Lemma IHC, proof (i)-(iv) | L125-128 | Chapman-Kolmogorov and self-adjointness; Holder between L^1 and L^2; Jensen; (5.3) |
| Lemma IHC, remarks | L131-135 | s = 1 gives Proposition HC with 36 beta abs(B); odd times; necessity of the rate; sharpness; Renyi remark (not used) |
| Corollary CU | L139-148 | (TH) and (HC-phys) give X(n; B) <= 2 Theta e^(-M_H (ell - tau_0 - a_iota)), hence (SEED-phys) under (SIZE-phys) |
| (TH) from two-sided stability | L150 | X(t_0; B) <= 2 c_F abs(B) t_0 (a/a_*)^4 = 16 c_F ell^3 tau_0/a_*^4 |
| What changes for the lane | L152 | K_phys(ell) = log(2 Theta/x_*)/(ell - tau_0) replaces K_a |
| (TH) from the account | L228-232 | Theta = 8 C ell^3 l from row 720, 1.1.5 (iii); (PHYS-SEED) once M_H (ell - l - a_iota) >= log(16 C ell^3 l/log(1 + s_*)) |
| 5.6 (a) | L182-186 | IHC needs (HC-vac) only on the functions p_s(u, .): (HC-traj)_(alpha, s) |
| 5.7, CU with (APR) | L197-201 | Proposition Delta and (APR) give (TH) with tau_0 = L_0, Theta = (2 ell/L_0)^3 A |
| 5.7, square-root test | L203 | slice restriction of a 4D inequality gives rate 2 sinh^2(omega/2), about omega^2/2, against the true omega |
| 5.7, defective form | L205 | defect D gives X(2s + 2m) <= 2D + theta_m X(2s), then the gap half |
| (R2) | L59, mark L254; restated L152, L244, L283 | K_a times the physical seed size grows like 3 log(1/a) + log beta |

Inputs to read for the check: (5.3), (HC-vac), Lemma HOT and Proposition HC (row 931, `gap-direction-max.md`); Theorem BR (`gap-fc-max.md`); K_a and Lemma RATE (`gap-trajtest-opus.md`, row 974); (SEED-phys) and Proposition P (`gap-seed-limit.md` Section 5); `gap-phys-seed.md` 1.1.5 (iii), Lemma Z, (APR), Proposition MB; Proposition Delta (`gap-mid-max.md`, row 709); `gap-phys-seed-check.md` (row 727); the account's lines for (a) and (b).
