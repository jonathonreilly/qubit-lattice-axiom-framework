# ab1 — criteria (pre-registered). Written 2026-10-28T21:34:24Z+, BEFORE `ab1_margins.py` exists.

Target T55-M. Exact rational arithmetic in plain python (`fractions.Fraction`), decades via
`math.log10` of a Fraction converted at the last step only. No BLAS, no numeric lock.

## Provenance of every input (defect 1 + defect 2)

All inputs are quoted from files that pre-date session 25, with file:line. **No constant below is
derived in this session.** Where a session-25 *claim* is the thing under test, it is labelled
[S25-CLAIM] and is a **hypothesis**, not an input.

| symbol | value | source (file:line) | still an input today? |
|---|---|---|---|
| ε_1 (headline) | 6.7·10⁻⁴⁰ | `RLARGE.md` l.72 (and l.612 "≲ 6.7·10⁻⁴⁰") | yes |
| ε_1 (spread) | 8.95·10⁻⁴⁰, 9.52·10⁻⁴⁰, 1.27·10⁻³⁹ | `RLARGE.md` l.71 (9.52), l.611 (8.95, 1.27) | contested; defect-2 spread |
| N | 2 | `RLARGE.md` l.414 "scope SU(2)" | yes |
| L, A_d(L) | 3, A_4 = 9 | `RLARGE.md` l.1009 | yes |
| κ | 1 | `RLARGE.md` l.1248 (c32's value) | **illustrative only** (reading note l.837) |
| η_1 | min{ε_1/18, ε_1²/(4608N)} | `RLARGE.md` l.1009 | yes (Lemma RS (R3)) |
| η_q | min{ε_1/18, ε_1/(2304N), δ_0/9} | `HIST.md` l.180 | yes (Lemma RS-lin) |
| RS plaquette branch | η_1²/(2N) | `RLARGE.md` l.981 (R5) | yes |
| RS kernel branch | κε_1²/(256N) | `RLARGE.md` l.1009 | yes |
| RS-lin kernel branch | κε_1²/(1024N) | `HIST.md` l.174, l.182 | yes |
| a_RS | min{a_η, κε_1²/(256N)} | `RLARGE.md` l.1020 | **under test** |
| a_RS ledger value | 5.93136·10⁻¹⁶⁶ | `SYMBOLS.md` l.356 | session-25 but a *restatement* of RLARGE l.1020 at l.72's ε_1 |
| c_RS (RS, greedy) | 5⁴ = 625 | `RLARGE.md` l.1021 | superseded per l.832 |
| c_RS (RS-joint) | 81 | `RLARGE.md` l.435; `HIST.md` l.185-186 | superseded per l.435 |
| c_pr | c_♭/C′² = (1/640)/53² | `RLARGE.md` l.90 | yes |
| a_bad | c_pr·ε_1² (for ε_1 < t_pr) | `RLARGE.md` l.88, l.92-93 | yes |
| θ bound | θ < 1/24 | `RLARGE.md` l.612 (and l.88 max{6θ,24θ}<1) | yes |
| live defect exponent a | min{θa_bad, a_A}, a_A ≥ θa_bad | `RLARGE.md` l.87-89, l.398, l.414 | yes |
| RLF ceiling rule | g² ≲ a/10² (log C_ℓ ≈ 93) | `RLARGE.md` l.616-617 | yes |
| DX′ ceiling | g_0² ≲ 2.5·10⁻¹⁵²/C_Ω | `RLARGE.md` l.618 (REVIEW_SF_S7 C-1) | yes; C_Ω unevaluated |
| the 15.62-decade breach | a_RS/10² vs DX′ | `PROOF.md` l.71-73 [S24] | **under test** |
| [S25-CLAIM] RS-lin per-cube | 6.525·10⁻⁸⁹ | `SESSION25_RESULTS.md` T55-H item 1 | hypothesis under test |
| [S25-CLAIM] RS-lin gain | 79.84 decades over a_RS/c_RS | same | hypothesis under test |
| [S25-CLAIM] RS-lin clears DX′ | +61.42 | same | hypothesis under test |
| [S25-CLAIM] C_Ω reversal | 4.14·10¹⁵ (bare) | `SESSION25_RESULTS.md` T55-H "Most dangerous" | hypothesis under test |

δ_0: `HIST.md` l.152 gives 256Nδ_0 = 0.4 at N = 2,3, so δ_0 = 0.4/(256N) = 1/1280 at N = 2.
At every ε_1 in the table ε_1 ≪ 0.4, so the δ_0/9 cap of η_q does **not** bind; the script asserts this.

## Pre-registered PASS/FAIL

Decades always mean log₁₀. Tolerance for a "reproduces" verdict: **≤ 0.01 decades** (the quoted
figures carry 3-5 significant digits). A verdict outside tolerance is a **FAIL** and is reported as one.

- **(A1) PASS** iff a_RS computed from `RLARGE.md` l.1020's formula at ε_1 = 6.7·10⁻⁴⁰, N = 2, κ = 1
  equals `SYMBOLS.md` l.356's ledger value 5.93136·10⁻¹⁶⁶ to ≤ 0.01 decades.
- **(A2) PASS** iff the min in a_RS is attained by the **plaquette** branch η_1²/(2N), i.e.
  η_1²/(2N) < κε_1²/(256N), at every ε_1 in the table.
- **(A3) PASS** iff RS-lin's per-cube exponent min{η_q²/(2N), κε_1²/(1024N)}/81 reproduces the
  [S25-CLAIM] 6.525·10⁻⁸⁹ to ≤ 0.01 decades at ε_1 = 6.7·10⁻⁴⁰, N = 2.
- **(A4) PASS** iff log₁₀[(A3's value)/(a_RS/625)] reproduces the [S25-CLAIM] 79.84 to ≤ 0.01 decades.
- **(A5) PASS** iff log₁₀[(A3's value)/10² ÷ 2.5·10⁻¹⁵²] reproduces the [S25-CLAIM] +61.42 to
  ≤ 0.01 decades at C_Ω = 1.
- **(A6) PASS** iff log₁₀[(a_RS/10²)/(2.5·10⁻¹⁵²)] reproduces `PROOF.md` l.71-73's **−15.62** to
  ≤ 0.01 decades at C_Ω = 1.
- **(A7) PASS** iff the live exponent a = θa_bad at θ = 1/24 gives a ceiling a/10² that sits
  **above** 2.5·10⁻¹⁵² at C_Ω = 1 — i.e. `RLARGE.md` l.618's sentence is **true** when evaluated at
  the exponent l.617 actually names (**a**, not a_RS). Report the margin in decades.
- **(A8) PASS** iff the C_Ω value at which the a_RS breach of (A6) reverses reproduces the
  [S25-CLAIM] 4.14·10¹⁵ to ≤ 0.01 decades.
- **(A9) DECOMPOSITION.** Report the split of (A4) into log₁₀(η_q/η_1)² and log₁₀(625/81). PASS iff
  they sum to (A4) exactly (to ≤ 0.001 decades) **and** log₁₀(η_q/η_1)² = log₁₀(4/ε_1²), the
  ε_1-dependence `HIST.md` l.181 states ("for ε_1 → 0, η_q/η_1 = 2/ε_1").
- **(A10) SPREAD (defect 2).** Report (A4), (A5), (A6), (A7) at all four ε_1 of the table. PASS iff
  **no verdict's sign changes** across the spread. A sign change is a FAIL and means the figure binds
  only at the constant it was written for.

## Designed-FAIL controls (defect 3). Each MUST fail; a control that passes invalidates its test.

- **(C-F1)** Re-run (A4) with η_q **replaced by η_1** in RS-lin's plaquette branch (mechanism removed;
  keep c = 81 vs 625). Pre-registered: the gain must collapse to **log₁₀(625/81) = 0.888**, not 79.84.
  **This control FAILS (A4)'s 79.84 threshold by construction.** If instead it returns ≈ 79.84, (A4)
  is not measuring re-centring and (A4) is void.
- **(C-F2)** Assert the min in a_RS is the **kernel** branch κε_1²/(256N). Pre-registered: **FAIL**
  (contradicts (A2)). If it passes, (A2) is void.
- **(C-F3)** Run (A7)'s ceiling test with the exponent **a_RS** in place of **a**. Pre-registered:
  **FAIL** (this is (A6), −15.62). If it passes, (A7) is not discriminating between the two exponents
  and the whole a-vs-a_RS distinction is unmeasured by this script.
- **(C-F4)** Run (A1) at ε_1 = 0.5 (`RLARGE.md` l.1248's c32 value, which reading note l.837 calls
  "illustrative only"). Pre-registered: **FAIL** (must not reproduce 5.93136·10⁻¹⁶⁶). If it passes,
  the script is ε_1-blind and every ε_1-indexed verdict above is void.

## What this check CANNOT decide (stated in advance)

Arithmetic cannot decide whether a_RS is **consumed**. That is a reading question, settled in
`ARS_BIND.md` §2-§5 by tracing consumers, not here. This script only prices the quantities so that
the reading's consequences are quantified, and tests whether the four session-25 figures reproduce.
A PASS on (A3)-(A5) therefore does **not** establish that RS-lin should be adopted.
