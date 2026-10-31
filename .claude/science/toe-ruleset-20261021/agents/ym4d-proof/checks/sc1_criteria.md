# checks/sc1_criteria.md — pre-registered criteria for check sc1 (STAR-CONST, session 24)

Written 2026-10-28 13:3x UTC, **after** STAR_CONST.md §1 (PRE-STATED) and **before** any script of mine exists.

**Provenance statement (read this before accepting the criteria).** This file contains **no constant derived by me**.
Every number in it is either
- quoted from SQ.md §15.0-§15.1 (C_S = 3, the exponent schedule p_i = 2^{i+1}, the radius schedule, q), or
- quoted from REVIEW_SQ_S4 (the 10¹³ ceiling on C_T; R_0; the 1.6·10⁴), or
- quoted from **CONST_T.md, which landed on disk before STAR_CONST.md was created** and which is the *input* my task
  is defined against (its §3.1 B(m) values, its §3.2 F values, its §6.1 formula, its §6.3 q_min table, its SUPPLIED
  c_c = 50 and ε_* = 10⁻⁴), or
- a decision rule (a threshold, a tolerance, a monotonicity direction) that I fix now.

Nothing below is a prediction of my own §2-§4 output; SC1-4 deliberately has **no** pre-registered pass value,
because its inputs are exactly what §2-§4 will produce and I must not be able to tune a criterion to them.

Arithmetic rules for every item: plain python, single thread, no BLAS, no numpy, no numeric lock. Exact
`fractions.Fraction` wherever the quantity is rational; `decimal.Decimal` with 40 significant digits where a power
x^a or a logarithm is needed, repeated at 60 digits as a stability control (SC1-5).

---

## SC1-1 — harness validation: the β-telescope

**Object.** B(m) := Π_{i≥0}(p_i − 1)^{m/p_i} with p_i = 2^{i+1}, truncated at i = 200.

**PASS** iff all three of CONST_T.md §3.1's published values are reproduced to within 0.5 % relative:
B(4) = 43.95, B(8) = 1931.5, B(4.17) = 51.45.

**FAIL** otherwise. A FAIL means my reading of CONST_T's B is wrong and every number downstream of it in this
session is suspect; I must then say so and not quietly re-define B.

## SC1-2 — harness validation: reproduce CONST_T's q_min table

**Object.** CONST_T.md §6.1's formula, read exactly as written there:

  C_T(q; C_1C_V) = √6 · F · B(4a) · [ ½·(36·C_1C_V·486)^a + ½·(A_cγ_c)² + 288·C_1·Q ],  a = q/(q−4),

with CONST_T's own parameter values: F = 175.8 (optimised schedule, §3.2), A_cγ_c = 236.9·C_1 at (c_c, ε_*) =
(50, 10⁻⁴) (§4.2 reference point), Q read off CONST_T's own statement 288·C_1·Q ≈ 6.5·10⁶ at q = 100 with C_1 = 20,
and the ceiling C_T ≤ 10¹³ (REVIEW_SQ_S4 S4-16). q_min := the smallest **integer** q > 4 with C_T ≤ 10¹³. For the
split of the product, CONST_T's reference point C_1 = 20 is used wherever C_1 appears alone.

**PASS** iff the computed q_min equals CONST_T §6.3's published table at **all five** points:

| C_1C_V | 1 | 100 | 2000 | 10⁴ | 5·10⁴ |
|---|---|---|---|---|---|
| q_min | 9 | 16 | 31 | 132 | none |

**FAIL** otherwise. A FAIL is reported as a FAIL and the discrepancy is named (which of F, A_cγ_c, Q or the C_1-alone
reading I have mis-read), and every q_min I report afterwards is reported under **both** readings.

## SC1-3 — sanity/monotonicity

**PASS** iff both hold on the grid C_1C_V ∈ {1, 10, 10², 10³, 10⁴} and integer q ∈ [5, 400]:
(i) q_min is non-decreasing in C_1C_V;
(ii) for fixed C_1C_V, C_T(q) is strictly decreasing in q over q ∈ [8, 400].

**FAIL** otherwise. (ii) failing would mean raising q can cost, which contradicts CONST_T §4.2 and would have to be
reported as a disagreement with it.

## SC1-4 — the result (REPORTED, no pre-registered pass value)

Evaluate C_T(q) and q_min from CONST_T §6.1's formula with the source term's base replaced by

  36 · c_s · μ_s(q),   μ_s(q) := |𝒩|^{1−2/q} · |𝒩_rev|^{2/q},

where c_s (the product C_1·C_V^source), |𝒩| (the plaquette-maximum multiplicity) and |𝒩_rev| (the link→plaquette
reverse count) are whatever §2-§4 of STAR_CONST.md derives, under each of:
- **multiplicity conventions** M-lit (|𝒩| = |𝒩_rev| = 14406 / 486, SQ.md l.1479-1480 read literally),
  M-ct (486, CONST_T §2.3's split), M-sharp (the values my expansion of step (3) needs);
- **β-power conventions** P-ct (B(4a), a = q/(q−4): CONST_T §6.1 as written) and P-max (B(4·max{a,2}): the
  convention forced if any absorbed potential enters with a β⁴ coefficient at exponent σ = 4).

Report, for each of the six combinations, C_T at q = 8 and q_min. **The verdict is then read off STAR_CONST.md
§1.3's pre-registered table, not from this file.** Nothing here can pass or fail; it can only be reported.

## SC1-5 — numerical stability control

**PASS** iff every C_T value reported in SC1-2 and SC1-4 has the same decade (same ⌊log₁₀⌋) when the Decimal
precision is raised from 40 to 60 significant digits, and every q_min is identical between the two precisions.

**FAIL** otherwise, in which case no decade claim may be made.

---

## What a FAIL means, by item

- SC1-1 or SC1-2 FAIL → my harness does not reproduce the file I am substituting into. I report the FAIL, keep the
  failing output unaltered, and (if I re-run) do so under a new id with this file untouched.
- SC1-3 FAIL → a disagreement with CONST_T §4.2 that must be reported as such, not smoothed over.
- SC1-5 FAIL → all decade claims withdrawn.
- SC1-4 cannot fail. If its inputs do not exist (because §2-§4 reaches OPEN-STEP), it is reported as not evaluated.
