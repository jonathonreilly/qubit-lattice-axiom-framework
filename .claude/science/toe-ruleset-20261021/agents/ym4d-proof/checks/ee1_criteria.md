# ee1 — pre-registered criteria for EPS1_EXEC's numeric checks (target T55-B)

**Written BEFORE `ee1_exec.py` exists.** Session 25, ym4d-proof lane, EPS1_EXEC worker.
Rule 2 of the session brief: criteria before scripts, and **no constant derived in this session appears
here**. Every number named below is a transcription from a file written in session 24 or earlier, with
its file:line; the script's job is arithmetic consistency between transcriptions, so a reproduced number
is **not** an endorsement of its source.

Arithmetic: exact `fractions.Fraction` in plain `python3 -I`, single thread, no numpy, no BLAS, no
numeric lock. `Decimal` at 50 digits for display only; every verdict decided on exact rationals.

---

## Transcribed inputs (file:line for each; none derived here)

| symbol | value | source |
|---|---|---|
| ε_1 in force (claimed) | 6.7·10⁻⁴⁰ | RLARGE.md l.72, l.612 |
| ε_1, pre-TB-1, rerun class | 9.52·10⁻⁴⁰ | RLARGE.md l.71; REVIEW_SF_S7.md l.53, l.247 |
| ε_1, post-TB-1, old class | 8.95·10⁻⁴⁰ | REVIEW_SF_S7.md l.47, l.200, l.297; RLARGE.md l.611 |
| ε_1, pre-TB-1, old class | 1.2687·10⁻³⁹ | REVIEW_SF_S7.md l.196; SF.md l.2837 (as 1.27·10⁻³⁹); NORMS.md l.746 |
| TB-1 factor | 0.7056 | REVIEW_SF_S7.md l.199-200, l.47, l.53 |
| class factor (rerun vs old), stated | ×0.75 | REVIEW_SF_S7.md l.251 |
| proposed cut | 9.38495112638·10⁻⁴⁵ | EPS1_SWEEP.md §4.5 |
| TAUFLAT's quoted cut | 9.38496·10⁻⁴⁵ | TAUFLAT.md l.408 |
| η_♭ at C_D = 4.76·10¹⁵ | 3.52310·10⁻⁸⁸ | TAUFLAT.md l.196, l.213 |
| η_♭ as a function of C_D | 1/(5.04991·10⁹·(3.31·10⁷·C_D²)²) | TAUFLAT.md l.567 |
| t_pr = θ_0^SUP | 1/(3.31·10⁷·C_D²) | TAUFLAT.md l.372 |
| 1/(c_♭/C′⁴) | 5.04991·10⁹ (= 53⁴·640) | TAUFLAT.md l.204 |
| strengthening factor 2√(C′⁴/c_♭) | 142125 | TAUFLAT.md l.205 |
| C_3 (reference) | 1 | TAUFLAT.md l.211; (a3-q) is OPEN at HIST.md l.1669 |
| C_D | ≈ (0.5-0.9)·10³·C_T | REVIEW_SQ_S4 S4-16, quoted TAUFLAT.md l.182 |
| C_T(q) row | q=10: 2.463e13, q=11: 9.774e12, q=12: 5.288e12, q=16: 2.031e12, q=24: 1.528e12, q=32: 1.454e12, q=100: 1.396e12 | EPSSTAR.md l.547-553 |
| C_T without (H2) | 8.05·10¹⁵ | EPSSTAR.md l.590 |
| C_T floor at q = 12 | 4.4·10¹² | EPSSTAR.md l.608 |
| C_T at q = 8 | ≥ 1.27·10¹⁴ | HANDOFF.md critical path item 4 |
| η_1 (RLARGE's, quadratic branch) | ε_1²/(512·N·A_d) ; = ε_1²/(4608N) at d=4, L=3 | RLARGE.md l.64, l.1009 |
| a_η | η_1²/(2N) | RLARGE.md l.1026 (= η_1²/4 at N = 2, RLARGE.md l.1248) |
| a_RS | min{a_η, κε_1²/(256N)} | RLARGE.md l.1020 |
| η_1 (KN-step's, linear branch) | c_1ε_1, c_1 = 1/(2(L²+5.5A_d)) = 1/117 | EXISTENCE.md l.1771 |
| g_0 at DX′ | ≤ 1.57·10⁻⁷⁶/√C_Ω | REVIEW_SF_S7.md l.204 |
| g_0² at DX′ | ≤ 2.456·10⁻¹⁵²/C_Ω | REVIEW_SF_S7.md l.203 |
| (SG^net) t-range | 0 ≤ t ≤ ε_1/(σ_*²g_k²) | PLD.md l.984 |
| (SG^net) necessary condition | v ≤ σ_*²g²(1 + 2m_*g/ε_1) | PLD.md l.995 |

N = 2, L = 3, d = 4, A_d(3) = 9 throughout (RLARGE.md l.1009 fixes 512·N·A_d = 4608N at these values).

---

## ee1-1 — (C6): do the four live ε_1 values factorise on two named, independently-sourced axes?

**Question.** Is the set {1.2687e-39, 9.52e-40, 8.95e-40, 6.7e-40} the 2×2 table
(old class / rerun class) × (pre-TB-1 / post-TB-1), with the class factor and the TB-1 factor each
transcribed from a *different* line of REVIEW_SF_S7 than the cell being predicted?

**Pre-registered verdicts, exactly one:**
- **FACTORISES** — all four cells are reproduced from the single base 1.2687·10⁻³⁹ times the two
  transcribed factors, each cell within **×1.01**.
- **DOES-NOT-FACTORISE** — any cell misses by more than ×1.01. Then the four values are *not* two
  corrections of one number, (C6) is **NOT DISCHARGED**, and T55-B stops (failure mode (X1)).

**Designed-FAIL control (mandatory).** Re-run the same gate with the TB-1 factor replaced by 1/2 (a
plausible-looking wrong value: "a_c ≈ a_p/2" read as a factor on ε_1 rather than on its square).
**The control MUST return DOES-NOT-FACTORISE.** If it returns FACTORISES, the gate has no power and is
reported as such, not as a PASS.

**What this gate cannot catch, stated in advance:** it cannot validate SF's derivation of either factor,
nor decide which cell is in force. The cell in force is decided by *reading* (RLARGE l.70's class
declaration and REVIEW_SF_S7's "TB-1 (binding)"), not by this arithmetic.

## ee1-2 — (C4): is the proposed value on the safe side of its own bound, and what fixes it?

**(a) Rounding direction.** With C_3 = 1 and η_♭ = 3.52310·10⁻⁸⁸ (TAUFLAT l.196), the clause is
4C_3ε_1² ≤ η_♭.
- **SAFE-SIDE** — the proposed 9.38495112638·10⁻⁴⁵ satisfies it **and** TAUFLAT's 9.38496·10⁻⁴⁵ does not.
- **UNSAFE-SIDE** — the proposed value does not satisfy it.
- **NO-DISCRIMINATION** — both satisfy it, or neither does. Then (C4) as stated is not about rounding and
  must be re-read.

**Designed-FAIL control (mandatory).** Feed the gate 9.3850·10⁻⁴⁵ (above the bound by ≈5·10⁻⁶ relative).
**The control MUST return UNSAFE-SIDE.**

**(b) What the value is a function of.** Compute ε_1^cut = t_pr/142125 with
t_pr = 1/(3.31·10⁷·C_D²) and C_D = 0.9·10³·C_T, over EPSSTAR l.547-553's C_T(q) row, plus the
no-(H2) C_T and the q = 8 C_T.
- **VALUE-PINNED** — the spread of ε_1^cut over the admissible q range is **< 0.30 decades**, i.e. the
  value is insensitive to the q choice and may be written as a bare number.
- **VALUE-PARAMETRIC** — the spread is **≥ 0.30 decades**. Then the value is an evaluation at one choice
  of a free parameter, writing it as a bare number plants a stale constant, and **(C4) is more than
  bookkeeping** (failure mode (X2) / C2-F1).

*0.30 decades (a factor 2) is chosen as the threshold because EPS1_SWEEP §1.1 dismissed a ×1.90 spread in
ε_1 as immaterial; a spread at or above that scale is by its own standard material.*

**Designed-FAIL control.** Run the same spread computation with the C_T row replaced by a constant row
(every q giving 5.288·10¹²). **The control MUST return VALUE-PINNED** (spread exactly 0).

## ee1-3 — (C5): do the two steeper prices equal (exponent) × (the move in decades)?

With Δ := log₁₀(ε_1^in-force / ε_1^proposed):
- a_RS at RLARGE's quadratic η_1 (a_RS ∝ ε_1⁴) should cost **4Δ**;
- a_RS at KN-step's linear η_1 (a_RS ∝ ε_1²) should cost **2Δ**;
- the Cauchy C³ constant on 𝔇_{α_E} (∝ ε_1⁻³) should cost **3Δ**.

Each is checked **twice**: once as (exponent)×Δ, and once by evaluating the owning file's formula at both
ε_1 (RLARGE l.64 + l.1026 + l.1020 for a_RS; EXISTENCE l.1771 substituted for the linear case).

- **PRICES-AGREE** — the two routes agree to **1·10⁻³ decades** for all three, and the ε_1⁴ figure
  reproduces EPS1_SWEEP §4.2's 19.415 and the ε_1² figure its 9.707, each to **±0.01 decades**.
- **PRICES-DISAGREE** — otherwise.

**Designed-FAIL control (mandatory).** Assert the a_RS price at exponent 2 against the formula evaluated
on the **quadratic** η_1 branch. **The control MUST return PRICES-DISAGREE** (it should miss by 2Δ ≈ 9.7
decades). A check that passes under the wrong exponent cannot distinguish the two (C2) outcomes and is
worthless for the job it is being run for.

## ee1-4 — (C3): which way does PLD l.995's 2m_*g/ε_1 move?

EPS1_SWEEP §2.2 states this quantity "**shrinks as ε_1 falls at fixed g**" and §2.3 tabulates it as
"**falls 4.854 decades**" at the DX′ coupling, calling it "the one ratio with the unhelpful sign".
Evaluate 2m_*g/ε_1 (m_* cancels; the gate is on g/ε_1) at the two ε_1, at fixed g = 1.57·10⁻⁷⁶.

- **RATIO-FALLS** — g/ε_1 is smaller at the proposed ε_1 (EPS1_SWEEP's stated direction).
- **RATIO-RISES** — g/ε_1 is larger at the proposed ε_1 (the opposite direction; then EPS1_SWEEP's sign
  is inverted and (C3) as written would plant a false sentence in PLD.md).

Both verdicts are reportable; neither is a failure of the check. Separately, the window margin
log₁₀(ε_1/g) is computed at both ε_1 and compared with EPS1_SWEEP §2.2's **36.63 → 31.78** at ±0.01.

**Designed-FAIL control (mandatory), two of them.**
1. **Known-invariant control.** Re-run at the ε-driven ceiling (g ∝ ε_1, EPS1_SWEEP §2.4's structural
   fact). The gate **MUST** return neither RISES nor FALLS but **INVARIANT** (|Δlog₁₀| < 10⁻¹²). A gate
   that reports a change where the lane's own structural fact says there is none is broken.
2. **Reversed-input control.** Re-run with ε_1 **raised** ×10 instead of lowered. The gate **MUST**
   return **RATIO-FALLS**. A gate that returns RISES for both directions has no power.

---

## Precision control (applies to every gate)

Every verdict is recomputed at 50 and 100 `Decimal` digits. **PRECISION-STABLE** if identical;
**PRECISION-UNSTABLE** otherwise, in which case the affected verdict is withdrawn.

## Pre-registered honesty clauses

- A failed check is reported as a FAIL with the script and output unaltered. A re-run takes a new id
  (`ee1b_…`) and leaves this file untouched.
- Any probe run after seeing a result is labelled **POST-HOC** in the script, the output and the file.
- If a designed-FAIL control does **not** fail, the corresponding gate is reported as **NO POWER**, not
  as a PASS, and no conclusion is drawn from it.
