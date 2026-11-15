# ar1 criteria — pre-registered, written BEFORE the script

Owner: the a_RS/η_1 repair worker (ARS_FIX.md), session 24.
Written after ARS_FIX.md §0 and **before** `ar1_margins.py` exists.

**This file contains NO numerical constant of any kind** — not one derived in this session, and not one
transcribed either. Every verdict below is a sign test, a branch identification, a logical comparison, or
a reproduction-within-tolerance test whose tolerance is named in ARS_FIX.md §0.5 (factor 1.2 on a
quantity, 0.1 decade on a decade figure). The script will transcribe constants from owning files with
file+line citations; a reproduced number is not an endorsement of its source.

Definitions used below, all from owning files and all pre-dating this session:
- **η_1^RS** := RLARGE l.64 / l.976's min of a linear and a quadratic entry in ε_1.
- **η_1^KN** := EXISTENCE l.1771 / l.1774's c_1ε_1, c_1 = 1/(2(L² + 5.5A_d(L))).
- **a_η** := RLARGE l.1026's bare-level value, proportional to η_1².
- **a_RS** := RLARGE l.1020's min of a_η and the kernel entry.
- **c_RS** := RLARGE l.1021's greedy-disjointness divisor.
- **DX′** := the programme coupling ceiling of REVIEW_SF_S7 l.203 (DX′-1 (iii)).
- **margin** := log10 of (the a_RS-derived coupling ceiling) ÷ (DX′), so a NEGATIVE margin means the
  a_RS ceiling lies BELOW the programme ceiling, i.e. it BINDS.

---

## ar1-1 — branch identification and the ε_1-exponent of a_RS. Verdict: **EXP-4 / EXP-2 / EXP-OTHER**
At each live ε_1 value read from its owning file, and for N and L in the admissible pairs the lane uses:
- **EXP-4** if the active entry of η_1^RS is the quadratic one AND the active entry of a_RS is a_η, so
  that a_RS ∝ ε_1⁴.
- **EXP-2** if the active entry of η_1^RS is the linear one, or if the active entry of a_RS is the kernel
  entry.
- **EXP-OTHER** otherwise.
**Power requirement:** the script must also report the verdict at a counterfactual ε_1 **above** the min's
crossover, where EXP-2 must be returned. If it cannot return EXP-2 anywhere, this check has NO POWER.
Tested against: RLARGE l.64's own formula, which fixes the crossover independently of any margin.

## ar1-2 — does the a_RS ceiling bind? Verdict: **BINDS / NOT-BINDING**, per (form, ε_1, convention)
Computed for form ∈ {η_1^RS, η_1^KN}, for every live ε_1 and for the proposed ε_1, under BOTH ceiling
conventions (with and without the c_RS divisor of RLARGE l.1021/l.1024).
- **(V2) CONFIRMED** iff the η_1^RS margin is negative at **every** live ε_1 under **both** conventions.
- **(V2) REFUTED** iff it is positive at every live ε_1 under both conventions.
- **(V2) SIGN-FRAGILE** otherwise, and then the sign table is the headline.
- **(V3) arithmetic half CONFIRMED** iff the η_1^KN margin is positive at every live ε_1 **and** at the
  proposed ε_1, under both conventions.
**Power requirement (mandatory, §0.6):** the two forms must return OPPOSITE verdicts from the same script
and the same constants; and the script must solve for the interpolating exponent p in a_RS ∝ ε_1^p at
which the margin crosses zero and exhibit the sign change across it. If both forms return the same
verdict everywhere, NO POWER.
Tested against: DX′ from REVIEW_SF_S7 (a different owning file, written for the τ_c question, before this
proposal existed), and cross-referenced to HW's own coupling-ceiling table (written for the ring question).

## ar1-3 — are KN-step's hypotheses available where RLARGE needs them? Verdict: **HYP-AVAILABLE / HYP-FAILS**
Two arithmetic hypotheses of Corollary KN-step (EXISTENCE l.1775), evaluated at threshold t = ε_1:
(a) the upper bound on t involving √N, A_d and c_1; (b) the δ ≤ 1/4 clause.
Plus two reconstruction identities, which are the part of this check with power:
(c) the identity that makes KN-step's c_1 exactly the reciprocal of twice (L² + 5.5A_d), i.e. that the
    first part of its proof is < t/2 on {η < c_1t};
(d) that KN's threshold constant, pushed through KN-step's union bound with the ribbon bound, reproduces
    KN-step's own stated numerical coefficient in (a) — **up to the §0.5 factor-1.2 tolerance**, from my
    derivation and not from its text.
- **HYP-AVAILABLE** iff (a) and (b) hold at every live ε_1 and at the proposed one, and (c) and (d) both
  reproduce within tolerance.
- **HYP-FAILS** if any of (a)-(d) fails; (c) or (d) failing is reported as **SOURCE-DISAGREES** against
  EXISTENCE, with both figures.
**Power requirement:** the script must report (a) at a counterfactual t large enough that (a) FAILS.
Tested against: EXISTENCE's own stated coefficients (a different lane), which I did not choose.

## ar1-4 — consumer sweep: does the linear form break a consumer? Verdicts as listed
(a) **ORDER-PRESERVED / ORDER-REVERSED** — RLARGE l.65 records η_1 ≤ η_q on the admissible ε_1 range.
    Evaluate that inequality under both forms. REVERSED is a finding, not automatically a failure; the
    file must then say what consumes the ordering.
(b) **RS-COMPATIBLE / RS-INCOMPATIBLE** — REVIEW_PLD_S3 l.305 states a ceiling on any RS-compatible
    threshold (a multiple of ε_1/L², fixed before this proposal). Test η_1^KN against it.
    **Power requirement:** report the verdict at a counterfactual c_1 for which it must read
    RS-INCOMPATIBLE.
(c) **SU23-STANDS / SU23-FAILS** — PLD l.765-776's summability condition at t = η_1. Recompute the least
    N for which it holds, under both forms, and check whether PLD's stated conclusion for the two smallest
    groups survives. A disagreement with REVIEW_PLD_S3's independently scanned N is **SOURCE-DISAGREES**.
(d) **MTAU-REPRODUCES / SOURCE-DISAGREES** — REVIEW_PLD_S3's (Arch-3) depth m_τ, recomputed from its own
    stated inequality under both forms, at the ε_1 values that review used and at the live ones. Integer
    agreement required; otherwise SOURCE-DISAGREES.
Tested against: REVIEW_PLD_S3 and PLD.md (different owning files, written for the PLD-architecture
question, before this proposal existed).

## ar1-5 — does the claimed gain reproduce? Verdict: **GAIN-REPRODUCES / SOURCE-DISAGREES**
The gain is margin(η_1^KN) − margin(η_1^RS), evaluated separately at today's ε_1 and at the proposed one.
- **GAIN-REPRODUCES** iff the figure EPS1_SWEEP quotes for the gain agrees within 0.1 decade at the ε_1
  value to which that file attributes it.
- **SOURCE-DISAGREES** otherwise, and the script must then say at which ε_1 value, if any, the quoted
  figure does hold — because the gain is a difference of two margins with different ε_1-exponents and so
  is itself ε_1-dependent, and a figure correct at one value is wrong at the other.
This check can fail and is expected to be able to fail in either direction.

## ar1-6 — precision. Verdict: **PASS / FAIL**
Every decade figure recomputed at two display precisions must agree to better than the 0.1-decade
tolerance. Exact `fractions.Fraction` for all ratios; `Decimal` for display only. A disagreement is a FAIL
of my arithmetic, not of any claim under test.

---

## Pre-registered global outcome

- **EPS1_SWEEP's finding CONFIRMED** iff ar1-1 = EXP-4 and ar1-2 (V2) = CONFIRMED.
- **EPS1_SWEEP's finding REFUTED** iff ar1-1 = EXP-2 or ar1-2 (V2) = REFUTED. In that case I stop and
  report the refutation; no repair is written.
- **The repair ADOPTABLE** iff additionally ar1-2 (V3) arithmetic half = CONFIRMED, ar1-3 = HYP-AVAILABLE,
  and no consumer in ar1-4 returns a failure that the linear form causes.
- **The repair CONDITIONAL** iff the arithmetic goes through but a hypothesis of KN-step is not supplied
  by RLARGE at the point of consumption (a reading question, settled in the file, not by this script), or
  a consumer in ar1-4 fails. The named input is then stated.
- A quoted figure that does not reproduce is **SOURCE-DISAGREES** with both figures given, and its
  direction (favourable / unfavourable to the claim under test) stated. It does not by itself refute the
  finding.

**Explicitly NOT sufficient for any verdict above:** that EPS1_SWEEP's numbers reproduce; that RLARGE
lists Lemma KN as PROVEN-HERE; that a review asked for the adoption; that the post-repair margin is large.
