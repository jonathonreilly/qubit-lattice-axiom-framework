# sy1_criteria.md — pre-registered verdicts for the T55-C symbol audit's arithmetic

**Written 2026-10-28T21:25Z, BEFORE `sy1_symbols.py` exists.** Every constant below is quoted from a
file written in an EARLIER session, with its line; **no constant derived in session 25 appears here**.

## Inputs (all prior-session, quoted)

| symbol | value | source |
|---|---|---|
| d, L, N | 4, 3, 2 | RLARGE.md l.1009 |
| A_d(L) = (d−1)L(L−1)/2 | 9 | PLD.md l.42 |
| η_1^RS | min{ε_1/(2L²), ε_1²/(512·N·A_d)} | RLARGE.md l.64, l.976 |
| η_1^KN | c_1ε_1, c_1 = 1/(2(L²+5.5A_d)) = 1/117 | EXISTENCE.md l.1771, l.1774 |
| η_q | min{ε_1/(2L²), ε_1/(256·N·A_d), δ_0/A_d} (δ_0 entry omitted: unevaluated) | RLARGE.md l.64 |
| ε_1 (live headline) | 6.7·10⁻⁴⁰ | RLARGE.md l.72 |
| ε_1 (illustrative) | 2 | RLARGE.md l.73 ceiling; PLD.md l.1067 uses (0, 0.517] |
| m_τ recursion | least m with (L²/(2C_I))^m·η_1 ≥ 2C_I·ε_1/L², C_I ∈ {1, 1.5, 2} | PLD.md l.1097; REVIEW_PLD_S3 l.435 |
| θ_0^SUP | 1/(3.31·10⁷·C_D²) | PROOF.md l.94 (quoting SQ.md Theorem SUP-price l.188) |
| θ_0^SUP (SQ's own form) | ≈ 3·10⁻⁸/C_D², after SQ.md l.216's own correction of l.212's "10⁻⁸/C_D²" | SQ.md l.212, l.216 |
| C′, c_♭ | 53, 1/640 | SQ.md l.297, l.318 |
| τ_R | 2.75·10⁻¹⁵ | REVIEW_SQ_S4 S4-14, quoted TAUFLAT l.170 |
| HW's quoted a_bad | ≈ 5·10⁻²³/C_D⁴ | HW.md l.604 |

## Pre-registered verdicts

- **SY1-1 (MTAU-KN-REPRODUCES / SOURCE-DISAGREES).** m_τ computed at **η_1^KN** for C_I = 1, 1.5, 2.
  **PASS** iff the triple is exactly **(3, 4, 5)**, i.e. it reproduces PLD.md l.1098's "m_τ = 3 at
  L = 3 if C_I = 1" and l.1244's "3, 4, 5". Any other triple is SOURCE-DISAGREES and is reported.
- **SY1-2 (MTAU-RS-DIFFERS).** m_τ computed at **η_1^RS** at ε_1 = 6.7·10⁻⁴⁰. **PASS (a live defect is
  confirmed)** iff every entry of the triple is **≥ 40**; **FAIL (no defect; PLD's 3/4/5 is right at
  RLARGE's threshold too)** iff any entry is ≤ 10. Anything between is INCONCLUSIVE and is reported as
  such. The exact triple is reported whatever the verdict.
- **SY1-3 (DESIGNED-FAIL CONTROL for SY1-2).** The SAME code path, same criterion "every entry ≥ 40",
  run at **ε_1 = 2** (RLARGE's illustrative value, where REVIEW_PLD_S3 l.435 records 5/7/10).
  **This control MUST FAIL.** If it passes, SY1-2's criterion is insensitive to ε_1 and SY1-2 carries no
  information; I then report SY1-2 as EVIDENCE-VOID. A second control: the triple at ε_1 = 2 must equal
  **(5, 7, 10)**, independently recorded by REVIEW_PLD_S3 l.435.
- **SY1-4 (ORDER-REVERSED).** r := η_1/η_q at each of the two η_1 symbols. **PASS** iff r < 1 at η_1^RS
  (RLARGE l.65's recorded ordering holds for its own symbol) **and** r > 1 at η_1^KN (the ordering
  reverses for PLD's). Both halves must hold; one half alone is reported as HALF.
- **SY1-5 (TAUFLAT WINDOW).** The largest C_D with τ_R ≤ θ_0^SUP/C′. **PASS** iff it is
  **455.283301 ± 1·10⁻⁴** (TAUFLAT [TF1-C], an independent file). **Designed-FAIL control:** the same
  computation at τ_R = 2.75·10⁻¹⁴ must give a window **≤ 150** and so must FAIL the ±1·10⁻⁴ test.
- **SY1-6 (HW a_bad STALE).** a_bad := c_♭(θ_0^SUP/C′)² at SQ's **corrected** θ_0^SUP = 3·10⁻⁸/C_D²,
  compared with HW.md l.604's quoted 5·10⁻²³/C_D⁴. **STALE-CONFIRMED** iff the ratio is ≥ 5;
  **NO-DEFECT** iff the ratio is in [0.5, 2]. Anything else is reported as computed.

## Anti-tautology statement (brief defect 3)

Every verdict above can come out either way on inputs this lane actually contains: SY1-2 is run at a
second ε_1 under SY1-3 where the same criterion must and should fail; SY1-4 has two halves that
disagree with each other by construction only if the two symbols really differ; SY1-5 has a control at
a perturbed τ_R. **If SY1-3's control passes, I report SY1-2 as carrying no evidence.**

## What this check does NOT decide

It does not decide which η_1 RLARGE *should* use, nor whether Lemma KN′'s H1 holds. It decides only
**what number PLD's recursion returns at each of the two η_1 symbols**, which is the only question the
rename needs answered.
