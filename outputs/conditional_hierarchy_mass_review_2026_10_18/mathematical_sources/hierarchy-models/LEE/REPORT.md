# Complete exercise argument with controlling corrections

Original source: `.claude/science/exercises/hierarchy-wall-20261018/LEE/REPORT.md`; exact SHA-256 `4808506c82bbcd52f3ed5830abb1d33c17f68b4faf4a2f2cce55133f7e64b10a`.

**Controlling scope:** Interval-union coverage is conditional on the explicit formula library and target measure. Member-hit frequency is not a universal p-value; historical controls are not fresh execution.

**Source-use boundary:** The complete argument below is preserved for inspection, including its original qualifications and counterexamples. Its old verdict labels, claims of completed reviews, operational history and numerical outputs are historical provenance only. Terminal physical exclusions and claims stronger than the controlling scope are deferred, not active conclusions. The canonical conditional exercise note and its correction register control. This attachment is not a separately promoted scientific claim and is not a fresh replay of its exploratory computations.

---

**LEE-1: LEE-COINCIDENCE under the registered rule.** Same-family run, not refereed.

The 0.03% match does not survive equally justified inputs. Inside the registered formula family, a random target gets a match this good about 5% of the time (3–11% across the family variants). That is roughly a 1-in-20 event, not a significant one.

**Read before any conclusion (step 1):**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full.
- `PRIMITIVE_REGISTRY_CHECK.md` and `SCALE_REFERENCE_PRIMITIVE_NOTE.md`.
- `derivation_obligations.json`: three obligations, none on the hierarchy.
- On main: `HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md` in full, including the 09-30 corrigendum, the 10-04 reproduction boundary and the F1–F4 anti-tuning certificates.

**Prior art (step 3):**
- There are no `HIERARCHY_PLAQUETTE_*` files on main.
- The only plaquette values with fermions in the measure are in that note's corrigendum (spot check plus campaign HMC).
- Main has anti-tuning certificates: F4 shows the plaquette ⟨P⟩ cannot be tuned at its licensed precision, and F1–F3 show the discrete pieces are rigid. It also has qualitative "numerology-risk" guards (the B4 attachment enumeration, the DELTA0 probes).
- I found no quantitative look-elsewhere count of the v formula on main.
- I reuse the corrigendum's matter-inclusive shifts. Everything else below is new.

**Pre-registration.**
- `.../hierwall/LEE/PREREG.md` was written and hashed at 21:16:13Z (`PREREG.sha`), before any family member was evaluated.
- It says openly that the part (ii) input values were already known from main.
- The decision family F0 is M_Pl × r^{1/n} × c^k, with:
  - r: 17 values (p/q with p, q ≤ 4; 1−2^{1−s} for s = 2..6; and their inverses);
  - n ∈ {1, 2, 4}, giving 45 distinct prefactors;
  - c: 10 values (α_bare, α_LM, α_s(v), u₀, ⟨P⟩; α/4π for the three couplings; 1−u₀ and 1−⟨P⟩);
  - k = 1..32;
  - 14,400 members in all.

**Results, part (i) (checked):**

| Family | N | Hits within 0.03% | p_hit | p_global at 0.03% | Hits within 1% |
|---|---|---|---|---|---|
| F0 (decision) | 14,400 | 2 (1 distinct value) | 1.4e-4 | **0.048** | 7 (4 distinct) |
| Core c only | 7,200 | 1 | 1.4e-4 | 0.031 | 4 |
| Uniform c/π, c/4π | 21,600 | 2 | 9e-5 | 0.11 | 10 |
| F0 with both M_Pl conventions | 28,800 | 2 | 7e-5 | 0.095 | 9 |

- p_global is the chance that a log-uniform random target gets at least one hit. Exact interval-union and 2e5-sample Monte Carlo agree to 0.001. It stays at 0.048–0.054 for target ranges from ±½ to ±3 decades (post-hoc check).
- The only member within 0.03% is the candidate itself. Its duplicate, (α_s(v)/4π)^8, equals α_LM^16 exactly, because α_bare = 1/4π (**proved**, one line).
- **The registered p_hit cannot do its job (proved, and checked by the script).** In any column of fixed prefactor and c, successive members are spaced by |ln c| ≥ |ln u₀| = 0.13. That is wider than even the full 1% window (0.02), so a column holds at most one hit and p_hit ≤ 1/32 for every target. The first clause of LEE-COINCIDENCE (p_hit ≥ 0.05) can therefore never fire. The first clause of LEE-SIGNIFICANT (p_hit ≤ 1e-3) is met almost automatically. p_hit is a fraction of family members, not a chance-coincidence probability, so p_global is the number to quote.

**Results, part (ii) (checked).** The match size is |δ₀| = 0.0255%, so the 10× threshold is 0.255%. "EJ" means an input pre-registered as equally justified.

| Input | ⟨P⟩ | v_cand (GeV) | Shift ÷ \|δ₀\| | Status |
|---|---|---|---|---|
| Licensed value | 0.5934 | 246.28 | 0 | baseline |
| Edge of main's stated ±0.0006 | 0.5928 / 0.5940 | 247.28 / 245.29 | **15.9** | EJ |
| April pure-gauge ensembles | 0.59369(2) | 245.80 | 7.7 | EJ |
| 1 taste in the measure | 0.5996 | 236.3 | **160** | EJ |
| 2 tastes (HMC / reweighted) | 0.6006 / 0.6053 | 234.7 / 227.5 | **185 / 299** | EJ |
| 4 tastes (HMC / linear) | 0.6146 / 0.6194 | 214.0 / 207.5 | **514 / 618** | EJ |
| Reduced M_Pl | 0.5934 | 49.1 | 3138 | not EJ under the primary rule |

- The direct computation and the dln v/dln⟨P⟩ = −4 elasticity agree for small shifts.
- The M_Pl uncertainty is 0.04 |δ₀|, so it plays no part.
- Matter-inclusive ⟨P⟩ counts as equally justified because the formula's own determinant carries fermion modes. Main's corrigendum calls the pure-gauge measure an unlabelled premise.

**Post-hoc diagnostic (not pre-registered; checked).** I re-ran the same family at each equally justified ⟨P⟩. A different member matches v_obs each time, often better than the original candidate:
- at ⟨P⟩ = 0.59369: (31/32)·α_LM^16, −0.007%;
- at the 1-taste value: (32/31)^{1/4}·α_LM^16, −0.000%;
- at the 2-taste reweighted value: (16/15)^{1/2}(1−u₀)^18, +0.001%.

How close the match is is generic to this family. Only which member wins depends on the inputs (**suggested** reading).

**Reading.**
- **LEE-COINCIDENCE**, fired by the second clause: the 1-, 2- and 4-taste matter-inclusive values, and the edge of main's stated ±0.0006 plaquette band, each move v_cand by more than 10 |δ₀|.
- LEE-SIGNIFICANT fails its second clause: the matter-inclusive inputs move v_cand 4–16% from v_obs.
- Counting the reduced M_Pl as equally justified would not change the reading.
- Under the narrowest set (pure-gauge inputs P0 and P2 only, without the ±0.0006 band) the registered rule would read SIGNIFICANT. That outcome comes only from the p_hit defect above; p_global still says about 5%.

**Strongest objection.** F0 is one family shape that I chose. Removing the reduced variants of c drops p_global to 3%. Against that, sums, exponentials, other 2^d exponents, and the historical "exact-246 at α_V = 0.49" route are forking paths that were not counted. So 3–11% is a lower bound on the real look-elsewhere freedom (**suggested**).

**Limits.** The matter-inclusive shifts are main's small-lattice numbers (4⁴, reweighting or HMC); I did not re-run them. No claim is made about v itself.

**Files** (all in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/hierwall/LEE/`):
- `PREREG.md`, `PREREG.sha`
- `scripts/lee_family.py`, `scripts/lee_inputs.py`, `scripts/lee_range.py` (post-hoc)
- `lee_family.out`, `lee_inputs.out`, `lee_range.out`

Peak memory was under 30 MB, nothing is left running, and nothing outside the folder was edited.