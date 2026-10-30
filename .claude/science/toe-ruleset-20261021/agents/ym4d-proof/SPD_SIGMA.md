# SPD_SIGMA.md — (W2)/(SPD) at a weak exponent σ > 0 (target T55-R)

*Owned by the T55-R worker. I write only this file and `checks/sp1_*`. Anything I want in another lane
file is in `## FOR OTHER FILES (not edited)` at the end, for the lead to land. Append only.*

---

## §S0 PRE-STATED (first edit of this file, 2026-10-28T22:05:47Z; STATEMENTS ONLY)

**Provenance.** This is the first edit of this file and it contains statements, definitions, failure
modes and a check plan only — no proof, no result, no constant derived here. No `checks/sp1_*` file
exists at this moment. My assigned input is `THETAW.md` §T4 (target T55-J, written earlier today,
UNREVIEWED), which I name but do not rely on; every load-bearing step I take from it I re-derive.
All other citations in this section are to files that pre-date session 25 (`BFT_A.md`, unmodified
since checkout; `HANDOFF.md`, last modified 11:52Z; `REVIEW_BFT_B_S9_S10.md`, 10:26Z).

**Disclosure (the review asks for it, and §16's precedent at `BFT_A.md` l.1228-1237 is the form).**
Before this append I read the shared brief, `SESSION25_RESULTS.md`'s T55-J entry, `THETAW.md` §T4 and
its FOR OTHER FILES, `BFT_A.md` §3.9/§6 l.218-250 and l.380-402, §11 l.819-845, §12-§13 l.869-1080,
§15 l.1186-1222, §16 l.1226-1300, [RBA3-fix] l.1320-1345, §18.4-18.7 l.1490-1570, §21 l.1686-1756,
§23.4-23.12 l.1919-2088, §23 table l.2140-2175, `HANDOFF.md` l.115-150 and `COFUN.md` §7. My reasoning
while reading went beyond reading: I computed the symbol of the Gram operator `Q Q^T` on one-forms
(finding it local and tridiagonal), I traced the index σ would occupy in §18.5's five steps, and I
sketched a centring argument for the (COMM) row. **So the failure modes below were considered before
this append and carry no pre-registration weight as predictions;** this section's claim is file order,
and the `sp1` criteria file (to be written after this section and before any script) is the genuine
pre-registration of the checks.

### Targets

- **S-1.** Write (W2)/(SPD) — `BFT_A.md` l.830-831 — as a fully quantified statement: what object, at
  which levels, in which norm, uniform in what. Separate the two things the lane's text calls by that
  name, if they are two. State the **σ-weakened** form of each.
- **S-2.** Identify, **by file:line**, every consumer of a level-decay hypothesis of (W2)'s shape, and
  decide for each whether **σ > 0 suffices** or exponent 1 is required. Candidate consumers to check:
  `BFT_A.md` l.1053-1061 (§13.7's implication), the carrier hypothesis **(SPD-H)** l.1254-1256, the
  carrier class **𝔉_l** l.1698, **Theorem XB** l.1280-1283, **Theorem CO-B** l.1739-1740, and the
  ‖·‖_Pc class-norm consumer behind `HANDOFF.md` l.121-128 / `REVIEW_BFT_B_S9_S10` S10-6.
- **S-3.** Decide whether exponent 1 is a **consumer requirement** or a **supplier output**, by reading
  the proof that delivers it (`BFT_A.md` §13.6, l.1024-1048) against the text that states it (l.830-831).
- **S-4.** Prove, or fail to prove: **Theorem XB_σ and Theorem CO-B_σ** — that `BFT_A.md` §18.5's
  Theorem XB and §23.11's Theorem CO-B hold with **(SPD-H)** replaced by **(SPD-H_σ)** (carried plain
  coarse size ≲ L^{−σ(m−l)}η²) for every σ > 0, with constants depending on σ and uniform in k and T.
  State the exact σ-dependence of the constant.
- **S-5.** Decide whether the ≈ 25(k−1) level-count factor (`BFT_A.md` l.822-824; `HANDOFF.md` l.121-128)
  and the (W2) exponent question are **one obstruction**: specifically, whether carrier decay at any
  σ > 0 turns the level sum geometric, and whether σ = 0 leaves the factor.
- **S-6.** Attempt carrier decay for the **second** GAP-1 (F3) row — the (COMM) term [A^T, χ]A of
  `BFT_A.md` l.244 (GAP 1 at l.387-391) — which no SPD-type proposition in `BFT_A.md` covers. Report
  the σ obtained, or the obstruction.
- **S-7.** If (W2) does not soften, decide whether it shares the structure `BFT_A.md` l.996-999 gives
  (W1) — a per-level deficit surviving α → 0⁺ — or is merely unattempted.

### Definitions I will use (stated now, so they are not tuned later)

- **(SPD-H_σ)**, for σ ≥ 0: co-closed level-l currents R_l (0 ≤ l < k) with
  sup|R_l| ≤ C_0κ_lL^{−3(k−l)}η² and **sup|Q_str^{(l→m)}R_l| ≤ C_1κ_lL^{−3(k−l)}L^{(1−σ)(m−l)}η²**
  (own units of level m) for every l < m ≤ k. Equivalently the carried current
  Ṽ^{(l)}_m := L^{2(m−l)}Q_str^{(l→m)}R_l obeys ‖(Ṽ^{(l)}_m)^c‖_∞ ≤ C_1κ_lL^{−σ(m−l)}η² in **plain
  coarse units of level m**. σ = 1 is `BFT_A.md` l.1254-1256's (SPD-H); σ = 0 is the bound available
  with no cancellation at all (l.919-920).
- **𝔉^σ_l** := {R ∈ C_l : sup|R| ≤ 1 and sup|Q_str^{(l→m)}R| ≤ L^{(1−σ)(m−l)} in own units of level m,
  l < m ≤ k}; 𝔉^1_l is `BFT_A.md` l.1698's 𝔉_l.
- **Θ_σ(t)** := Σ_{j=0}^{t−1}L^{(1−σ)j} (t ≥ 0, Θ_σ(0) = 0); **E_σ(t)** := (t+1)·Θ_σ(t+1).
  Θ_1(t) = t and E_1(t) = (t+1)².

### Failure modes (considered before this append; no pre-registration weight)

- **SP1-F1.** (W2) is two statements and σ-weakening helps only one of them.
- **SP1-F2.** The consumer needs the row's **own-level** decay in (k−l), not the **carried** decay in
  (m−l); these are different statements and the lane's proven proposition supplies only the second.
- **SP1-F3.** The σ-generalisation of XB/CO-B fails because some step uses σ = 1 to cancel an
  L^{+(m−l)} **exactly**, not merely to make a geometric series converge.
- **SP1-F4.** A compounding per-step loss exceeds L, so no σ > 0 survives.
- **SP1-F5.** The (COMM) row has no centring cancellation at all (`BFT_A.md` l.244 says so in its own
  words), hence no carrier decay at any σ > 0.
- **SP1-F6.** The identification of the k-factor with the σ question is false, because the k-factor
  lives in a norm that carrier decay does not reach.
- **SP1-F7.** A clause I treat as superseded is in fact live (the inverse of the stale-citation defect).

### Plan of check `sp1` (criteria file `checks/sp1_criteria.md`, written after this section and before
any script; exact `fractions.Fraction` and Python ints only, no numpy/BLAS, single thread, **no
numeric lock** — rule 6 exempts exact arithmetic)

- **sp1-A.** The exponent identity of §18.5 Step 3, −3(k−l) + 4(m−l) − 2(k−l) + 4(k−m) = −(k−l),
  checked exactly over a grid of (k, l, m).
- **sp1-B.** The closed form Σ_{t≥1}Θ_σ(t)L^{−t} = 1/((L−1)(1−L^{−σ})), checked exactly at rational
  σ with L^{σ} rational.
- **sp1-C.** Convergence of the CO-B_σ Hölder sum Σ_t E_σ(t)L^{−(1−α)t} under 0 < α < σ.
- **sp1-D (designed FAIL control).** σ = 0 must make sp1-B's closed form singular and sp1-C's sum
  divergent. **It must fire.**
- **sp1-E (designed FAIL control).** α = σ must make sp1-C's sum divergent. **It must fire.**

---


---
**[LEAD, 2026-10-28T22:11:08Z] ABANDONED DRAFT.** This worker was stopped mid-run. Nothing in this file is a result.
