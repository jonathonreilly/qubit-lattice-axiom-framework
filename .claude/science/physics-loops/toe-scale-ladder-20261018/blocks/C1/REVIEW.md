# C1 review

**Reviewer:** a Claude subagent, same model as the author. This is not a different-model check. I wrote and ran my own scripts and did not re-run the block's QMC.
**Date:** 2026-10-19.
**Scope:** I read all of NOTE.md and WORKLOG.md, plus `step2_validate_L2.py`, `step3_validate_W1_L2.py`, `dbg_vend.py`, `lattice.py`, the seed logic and init of `driver.py`, and the winding section of `analyze.py`. Logs read: `step1/2/3`, `dbg_vend`, `winding_fit2`, `queue_A`. Data read: `per_chain.md`, `summary_combined.md`, `winding_gap.{md,json}`, `summary.json`, and the repo cache `logs/runner-cache/ring_model_electric_coupling_..._2026_09_25.txt`.
**Writes:** only this file and `review_scripts/`.

## Review scripts and logs

All jobs ran at nice 10 on one core, each under 1 minute.

| script | what it does | log ends |
|---|---|---|
| `review_scripts/rv1_ed_L2_stoquastic.py` | Own ED at L=2 by brute force over all 2^24 configs, with its own indexing and orientation. It does not use lattice.py, qmc.py, driver.py or step1. Covers ρ=0 and staggered ρ=(−1)^(x+y+z). Also checks odd-count for L=2..16 and an own GF(2) solve for L=2..7. | `TOTAL: PASS=41 FAIL=0` |
| `review_scripts/rv2_refit_winding_gap.py` | Own weighted LSQ (normal equations) on the numbers typed in from NOTE §5.1. Includes sensitivity fits and the repo comparison arithmetic. | `TOTAL: PASS=15 FAIL=0` |
| `review_scripts/rv3_seed_hazard.py` | Builds start states with the current driver and decides each one's sector with its own BFS and flux code. | `TOTAL: PASS=4 FAIL=0` |
| `review_scripts/rv4_start_pairs.py` | Recomputes the §5.3 start-consistency χ². | `TOTAL: PASS=1 FAIL=0` |

Two of my own test errors, disclosed:
- The first rv1 version asserted that D H(g) D has non-positive off-diagonals for both signs of g. That is false by construction, because D H(+g) D = H(−g). It gave 12 FAILs, and the assertion was corrected (see C2). That log was overwritten.
- The first rv4 version used per-chain values rounded to 5 decimals and got χ² = 14.2. With full-precision `summary.json` it gives 12.78, which reproduces the NOTE.

## Per-claim verdicts

| # | claim (NOTE §) | verdict | severity | evidence / fix |
|---|---|---|---|---|
| C1 | Thm 1: off-diagonals are −g·{0,1} with no multiplicity, so H is stoquastic for g ≥ 0 (§2) | **correct** | — | Own proof agrees: spin-1/2 σ^± elements are 0 or 1, there are no fermionic signs, and distinct plaquettes have distinct link sets (rv1, L=2..16). ED at L=2: every adjacency entry is exactly 1 for both backgrounds. |
| C2 | Thm 2: even L, D = Π_Λ σ^z gives D H(g,V) D = H(−g,V); D preserves Gauss law, winding and components (§2) | **correct** (wording note) | minor | Hand proof re-done: per orientation (xy, yz, xz) the Λ-count is 1 or 3. Periodicity needs even L. ED at L=2 for ρ=0 (9600 states, 937 components, 125 σ-flux sectors) and for staggered ρ (3273 / 165 / 93): H(+1) off-diagonals are ≤ 0. Ungauged H(−1) has off-diagonals equal to +1, while D H(−1) D has all off-diagonals ≤ 0. D H D − H(−g) = 0 exactly. Spectra of H(g), D H(g) D and H(−g) agree to ≤ 5e−14 on every component and every winding sector, for V = 0, 0.5, 0.9. This holds both with the block's Λ and with an independent GF(2) Λ. **Fix (wording only):** "for either sign of g" means the gauge is chosen per sign: identity for g > 0, D for g < 0. No single fixed gauge works for both signs. The NOTE text is consistent with this, but the task phrasing is not. |
| C3 | Odd L: no diagonal gauge (§2 Remark) | **correct** | — | My own GF(2) solve finds δΛ = 1 inconsistent for L = 3, 5, 7 and consistent for L = 2, 4, 6. The plane-cycle parity argument checks out. The zero-winding sector is empty for odd L because the flux of L² odd ±1 terms is odd. |
| C4 | Model: ρ=0 on the cubic torus, and "staggered background" belongs only to the ladder (§1) | **correct** | — | Repo 09-04 note, line 101: "rho_v = 0 on every torus (z_v = 6 even); 2 rho(t_i)=(−1)^i … on the ladder". The stoquasticity result does not depend on the background (staggered case checked in rv1). |
| C5 | L=2 anchors: 864/464 components, E0 = −9.0267209135 and −7.3991109799, ΔE = 1.62761 / 0.73146 (§1, §3.4) | **correct** | — | rv1 reproduces all of these independently. The whole W=0 sector (880 states) has the same E0 as the 864 component. For completeness, exact ΔE(L=2, V=0.9) = 0.1467209690. |
| C6 | Lemma 3 and the periodic control: E = −7.95 vs −9.02 (§3.1) | **correct with fix** | minor | The proof is sound. The control shows a large bias, but no exact *class-restricted* trace was computed, so it is not shown that −7.95 is the n=0 value rather than a different defect. **Fix:** say "consistent with the class restriction", or add the exact n=0-restricted reference. |
| C7 | Step-2 W=0 validation tests what §3.4 says (§3.4, §0.3) | **correct with fix** | minor | The script matches the description: 7 cases, 4 chains, E_mix, N_f(mid/end), S_T, windowed kinetic energy and C(τ), with σ = max(scatter/√4, combined SE). **Fixes:** (a) The failing case fails in **E_mix** (z=+3.1) as well as N_f(end) (z=−3.1). E_mix = (V−g)N_f(end), so they are one observable, but it is the production estimator and should be named. (b) "12 of 13 checks" counts 4 structural checks. Counting QMC-vs-exact cases, it is 8 of 9 pass. (c) `dbg_vend` re-ran only N_f(end), with scatter-only errors and no TOTAL line. It is a reasonable diagnostic, not a re-validation, and the pre-declared rule still records the case as a FAIL. The NOTE reports both results, which is correct. |
| C8 | Seed/W-sector hazard (§3.4) | **correct with fix** | minor | rv3 confirms that under the current driver every step-2 seed starts in the W=1 sector (σ-flux (−2,0,0)), including the periodic-control seeds **129–131**, which the NOTE omits ("101–128"). The recorded log is empirically W=0: its E_mix values of −9.02 to −9.04 match the W=0 exact value, not W=1's −7.40. This supports the claim that the log is valid for the code at that time. dbg_vend seeds 31–36 and the production seeds map correctly. |
| C9 | Step-3 W=1 validation (§3.4) | **correct**; limited scope | minor | Seeds 201–208 are line starts in W=1 (rv3). E_mix agrees at V = 0 and 0.5, T = 4. Not validated: the W=1 RK-walk start (seed 111 type) and V = 0.9 in W=1. Its "independent" reference shares `lattice.py`, but rv1 removes that dependence. |
| C10 | Middle of path not equilibrated, so the S_T, Bragg and ω_eff criteria are not evaluable (§5.4, §6) | **correct** | — | per_chain.md shows the start dependence, and E_mid − E_mix ≈ 0.01 per plaquette at T ≥ 24. Pre-declared rules 1–3 cannot be applied, so rule 4 gives "inconclusive". |
| C11 | Fit table §5.2 and the repo refit §5.5 | **correct** | — | rv2 reproduces every parameter, error and χ² to rounding. Example: Str gives χ² 54.2 vs the NOTE's 54.5 (from rounded inputs). The σ 2σ upper bounds are 0.019 (T=2L) and 0.042 (largest T), matching "≲0.04". The start-pair χ² 12.78/10 is reproduced (rv4). |
| C12 | "Pure σL rejected (χ² 37–54/4)" and "σ ≲ 0.04 g" (§0.5, §6) | **correct but fragile; fix** | **moderate** | The rejection rests on **L=4 alone**. Dropping L=4 gives Str χ² 6.9/3 (p=0.08, T=2L) and 2.7/3 (p=0.44, largest T), so pure σL is no longer rejected. A/L + σL then gives σ = −0.005(26) and +0.021(29), with 2σ upper bounds of about 0.05 and 0.08. L=4 is the smallest torus and the most exposed to finite-size corrections. **Fix:** state that the rejection and the 0.04 bound depend on the L=4 point, give the bound without L=4, and replace "rests mainly on L=4, 6 and 8" with "rests on L=4". A pure σL law is also a straw man; the informative statement is the S-fit σ. |
| C13 | Coulomb (A/L) "consistent, not established" (§6) | **correct** | — | Reproduced: A/L, B/L² and (for the largest T) const all have acceptable χ². With repo precision, A/L is rejected at χ² 51/2, and repo L=4..8 plus block L=10, 12 still gives σ = −0.033(5). |
| C14 | Projection rule: "passes formally at L=8 and 10" (§5.3, §6) | **correct but understated; fix** | moderate | W=1 has only one T at L = 4, 6 and 12, so under the pre-declared rule ("a point is used only if two T agree … otherwise flagged") the ΔE points at L = 4, 6, 12 are **unflagged-but-untested**, yet they carry most of the fit leverage. Also, the single L=6, T=18 W=0 chain (−187.278(71)) lies **1.7σ above** the T=12 value (−187.455(76)). E_mix must decrease with T in expectation. L=6, T=12 starts give χ² 6.3/2 with a spread of 0.24 total, against ΔE(6) = 0.44. **Fix:** flag L = 4, 6, 12 in §5.1 and §6, and report the T=18 inversion. |
| C15 | Repo disagreement on E(W=0, 8³), "3.2σ, unresolved" (§5.5, §8) | **arithmetic correct; understated; fix** | **moderate** | 3.24σ is reproduced. Not stated in the NOTE: (a) against the block's T=16 value (−443.734(77)) it is **4.5σ**. (b) The discrepancy, 0.37–0.46, is **larger than ΔE(8)** itself (0.16–0.32), so the 1σ agreement of ΔE with the repo holds only if the bias cancels between sectors. That is an untested assumption, and ΔE at L ≥ 8 depends on it. (c) At L = 4 and 6 the absolute energies agree (−0.6σ and +0.3σ), so the problem first appears at L=8. (d) The repo's loop moves sample the whole sector, so its target E0(sector) ≤ E0(component). The component/sector difference therefore cannot explain the repo being *higher*: one of the two codes is biased by at least 3e−4 per plaquette, which matches the size of ΔE/N_p at L ≥ 8. **Fix:** put (a)–(d) in §0 and in §6, as the main caveat on every ΔE point at L ≥ 8. |
| C16 | V=0.5 and V=0.9 verdicts (§6) | **correct** | — | V=0.5: σ = 0.0071(184) is reproduced. V=0.9: ΔE(8) = −2.9σ, and the A/L + σL fit gives σ = −0.022(5) (negative at 4σ). "Insufficient projection, no conclusion" is the right reading. |
| C17 | Overall: **INCONCLUSIVE at accessible L** (§6) | **correct** | — | This follows from pre-declared rule 4 once C10 holds, and the ΔE data cannot separate 1/L from faster decay (C13). The supporting phrase "large string tension excluded" is acceptable. It should be qualified by C12 (the L=4 dependence) and C15 (unresolved absolute-energy bias at L=8). |

## Summary of required fixes

1. **Moderate (C12):** say that the σL rejection and the bound σ ≲ 0.04 depend on L=4. Without it, σ < 0.05–0.08 at 2σ.
2. **Moderate (C14):** the L = 4, 6, 12 ΔE points are not projection-tested under the pre-declared rule. Report the L=6 T=18 inversion.
3. **Moderate (C15):** the L=8 disagreement is 3.2–4.5σ and larger than ΔE(8). It cannot be explained by component vs sector. ΔE at L ≥ 8 assumes the bias cancels between sectors. Move this into the bottom line.
4. **Minor (C2, C6, C7, C8, C9):** say that the gauge is chosen per sign. Weaken the wording of the periodic-control attribution. Name E_mix as the failed observable and use 8/9 for the QMC cases. Add seeds 129–131 to the hazard. State the limits of the step-3 scope.

No claim was found incorrect. The stoquasticity theorem (C1–C3) is confirmed independently, including all winding sectors and a staggered background at L=2.

## Correction confirmation (2026-10-19)

**Who and what.** The same reviewer (a Claude subagent, same model as the author) read the complete corrected NOTE.md (434 lines), including its "Review dispositions" table.

**Per finding:**

| finding | resolved? | where |
|---|---|---|
| C2 (gauge chosen per sign of g) | yes | §0.1 |
| C6 (periodic-control attribution) | yes | §0.2 |
| C7 (validation counts, failed observable) | yes in §0.3; residual in §3.4 | §3.4 line "The failure is V=0.9, T=3: N_f(end) z = −3.1" still names only N_f(end) and not E_mix (nit) |
| C8 (seed hazard incl. 129–131, W=0 evidence) | yes | §3.4 |
| C9 (step-3 scope) | yes | §3.4 |
| C12 (L=4 dependence) | yes | §0.5, §6, §9; numbers match rv2 |
| C14 (L=4, 6, 12 projection untested; T=18 inversion) | yes | §0.5, §6 |
| C15 (8³ disagreement) | yes | §0.5, §5.5, §6, §9; residual in §8 (nit) |

**Residual nits.** None of these is a defect that changes any verdict.
1. §3.4: also name E_mix (z=+3.1) as the failed observable.
2. §8 "Repo context": still says "3.2σ"; it should say 3.2–4.5σ.
3. §5.5 "biased by at least about 3e−4 per plaquette": the two comparisons give 0.37–0.46 / 1536 = 2.4–3.0e−4. The imprecision originated in this review's C15 wording, and "≳2.4e−4" is accurate.
4. §10 refers to `blocks/C1b`, which does not exist yet. Mark it as planned.

**New defects.** None found. The verdicts, fit numbers and the overall INCONCLUSIVE verdict are unchanged and consistent with the review.

**Final verdict: READY.** The four nits above are optional wording fixes.
