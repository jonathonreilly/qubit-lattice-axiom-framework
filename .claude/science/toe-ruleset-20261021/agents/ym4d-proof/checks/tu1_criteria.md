# checks/tu1_criteria.md — pre-registered criteria for check tu1 (T-uniformity worker, session 25)

Written 2026-10-28T21:33Z, **before** `tu1_twisted.py` exists. No constant below is derived in this session:
L = 3 and d = 4 are the lane's standing parameters (NORMS §N1), ℓ = L^k is the level-k cell side, and the two
numeric thresholds (100 and 10^3) are round brackets fixed in advance, wide enough that they are not
reverse-engineered pass marks.

## What is being tested

The object is the **twisted cell complex**: 𝒞 = (Z/ℓ)^d with twisted difference operators
`(D_μψ)(u) := ψ(u+e_μ) − ψ(u)`, where crossing the μ-seam multiplies by `z_μ` (so `ψ(u+e_μ)` at `u_μ = ℓ−1`
means `z_μ·ψ(0, u_⊥)`). This is the level-0 de Rham complex of one level-k cell at coarse momentum p, with
`z_μ = e^{ip_μ}`, `ν_μ := z_μ − 1`. All arithmetic is exact over Q (z_μ rational), so the check needs no lock.

The construction under test (call it **CONSTR**), for a 2-form F on 𝒞:
1. `Ω_β := σ_1(F_{1β})` evaluated at `z_1 = 1` (β ≥ 2), where `σ_1(g)(u_⊥) := Σ_{u_1} g(u)`;
2. `Φ := σ_2(Ω_2)` evaluated at `z_2 = 1`;
3. `μ := Θ_2(Ω_2) + σ_2(Ω_2)/ν_2` (the direction-2 line solve), `Θ_2(g)(u) := Σ_{0≤i<u_2} g(i in slot 2)`;
4. `b_1 := −μ/ℓ` (independent of u_1 — the **spread** transverse gauge function);
5. `G_β := F_{1β} + D_β b_1`;  `b_β := Θ_1(G_β) + σ_1(G_β)/ν_1` (β ≥ 2).

## Pre-registered PASS/FAIL verdicts

- **tu1-A (the construction solves the equation).** For every tested (d, ℓ, z) instance with F exact
  (`F := D∧a`, a a random rational 1-form): CONSTR's output b satisfies `D_αb_β − D_βb_α = F_{αβ}` for **every**
  α < β and **every** u ∈ 𝒞, with **zero** discrepancies in exact rational arithmetic.
  **PASS** iff the total discrepancy count over all instances is 0. **FAIL** at any nonzero count.
- **tu1-B (the second obstruction vanishes).** For every tested instance with F exact: `Φ = 0` exactly at every
  transverse site. **PASS** iff all zero; **FAIL** otherwise.
  *Disclosed in advance:* for an **exact** F this identity also follows by telescoping alone, so tu1-B tests the
  σ-identities and the indexing, not the closed-but-not-exact case. The closed-but-not-exact case is covered by
  the proof (which uses closedness only) and is not tested numerically.
- **tu1-C (designed-FAIL control #1: a non-closed input).** Run CONSTR on `F' := F + δ` where δ is a single
  nonzero entry chosen so that `D∧F' ≠ 0`. **The control is expected to FAIL tu1-A's identity** (discrepancy
  count > 0) **and to give Φ ≠ 0 for at least one instance.** If the control PASSES tu1-A, the gate has no power
  and tu1-A is to be reported as evidence-free.
- **tu1-D (designed-FAIL control #2: the b_1 correction is load-bearing).** Re-run CONSTR with step 4 replaced by
  `b_1 := 0`, at `z_1 = 1 + ε` for ε = 1/10, 1/10², 1/10³, 1/10⁴ (other z generic). **Expected:** the uncorrected
  `max|b|` grows by a factor ≥ 10³ across those four ε (a 1/ε pole), while the corrected `max|b|` varies by a
  factor < 10. **PASS** iff both halves hold; **FAIL** otherwise. A FAIL means either the pole is not there (so
  the correction is unnecessary and the proof is over-complicated) or the correction does not remove it (so the
  proof is wrong) — both are reportable findings.
- **tu1-E (the budget: one factor of ℓ, not two).** For every instance with `min_μ|ν_μ| ≥ 1/10`:
  `max|b| ≤ 100 · ℓ · max|F|`. **PASS** iff the inequality holds in every such instance; **FAIL** otherwise.
  (The claim the proof must support is `max|b| ≤ C·ℓ·max|F|` with C absolute; 100 is a deliberately loose
  pre-registered bracket. A failure here is failure mode **U-F2**, the L^k leak.)

## Instances to be run (fixed now)

- d = 4, ℓ = 3 and ℓ = 9; d = 3, ℓ = 5.
- z vectors: (a) generic (no ν_μ small); (b) z_1 = 1 + 10⁻⁶; (c) z_2 = 1 + 10⁻⁶; (d) z_1 = z_2 = 1 + 10⁻⁶;
  plus the tu1-D ladder. Random data from a fixed seed, recorded in the script.

## What a PASS does and does not establish

A PASS establishes that the algebra of §U4's construction is right on instances — it is **not** a proof of the
lemma, which is written out separately and does not depend on this check. A FAIL of tu1-A or tu1-E refutes the
construction as written.
