# Corrigendum packet for PR #8146 (block 12): derivation attempt 1 of 2

Worker `w-jonathonsmac4f50-jdc8c` (claude-opus-5), unit `J-derive-corrigendum-PR8146-a1`.

**Sources.** Block 12's note, runner and pack files at the PR #8146 head `3acd27d2`. The branch is `physics-loop/…block12…`, and the note is `docs/ADMISSIBILITY_RULE_STRONG_COUPLING_FORMATION_LAW_LEVEL_AUTOMATON_ERODER_METASTABILITY_ORDERED_PHASE_OBLIGATION_BOUNDED_THEOREM_NOTE_2026-09-15.md`. For the use search: the docs notes of PRs #8147–#8178 and the #8179 decision record, all at their heads. Line numbers are those files' lines.

**Provenance.**
- The defect was found by a grok worker: `logs/probes/J:attack-g:PR8146/w-macbookpro90c72-j687e__…`.
- It was confirmed by me as #8413: `J:confirm:J-attack-g-PR8146/w-jonathonsmac4f50-jbe65__…`, claude-opus-5, the same model family as this attempt.
- No other attempt at this corrigendum was on `origin/ai/probes` when I wrote this.

## 1. The statement attempted

Objects: the six-axis menu `{±e₁, ±e₂, ±e₃}` and the product rule `r(s | u, v, w) ∝ φ(s, u)φ(s, v)φ(s, w)`, with `φ = p` (equal), `q` (antipodal), `r` (orthogonal) and `p, q, r > 0`.

**(a) Corrected S1 clause.** For `a` a value and `b, c ⊥ a`:
- The majority `a` of the orthogonal `2:1` triple `(a, a, b)` is its strictly most likely output iff `p > max(q, r)`. This part of the original is right.
- The majority `a` of the antipodal `2:1` triple `(a, a, −a)` is its strictly most likely output iff `p > q` and `p² q > r³`.
- Hence the majority of every `2:1` triple is the strictly most likely output iff `p > P*(q, r) := max(q, √(r³/q))`.
  - `P* = max(q, r)` exactly when `q ≥ r`.
  - `P* = √(r³/q) > r` when `q < r`.

**Largest domain of the original.** For fixed `(q, r)`, the original "iff `p > max(q, r)`" holds for every `p` exactly when `q ≥ r`. When `q < r` it fails exactly on the band `r < p ≤ √(r³/q)`.
- Witness `(5, 2, 4)`: `P(a | a,a,−a) = 25/163 < 32/163 = P(c | a,a,−a)` for each of the four orthogonal `c`.
- 979 of the 13824 integer triples in `{1..24}³` lie in the band.

Bands on the campaign's lines:

| line | failure band |
|---|---|
| `(p, 1, 2)` | `(2, 2√2]` |
| `(p, 1, 1)` | none |
| `(p, 2, 4)` | `(4, 4√2]` |
| `(p, 1, 3)` | `(3, 3√3]` |

## 2. Steps

**S1 (PROVED; CHECKED `A1`). The output weights.**
- For `(a, a, b)`: `p²r` (output `a`), `q²r` (`−a`), `pr²` (`b`), `qr²` (`−b`), and `r³` for each of `±c`.
- For `(a, a, −a)`: `p²q` (`a`), `pq²` (`−a`), and `r³` for each of the four orthogonal values.
- These reproduce S1's closed forms. The argument is the definition, evaluated.

**S2 (PROVED; CHECKED `A2`). Orthogonal pattern.**
- The factored differences are:
  - `W(a) − W(−a) = r(p − q)(p + q)`;
  - `W(a) − W(b) = pr(p − r)`;
  - `W(a) − W(±c) = r(p − r)(p + r)`;
  - `W(a) − W(−b) = r(p² − qr)`.
- The first three are positive iff `p > q` and `p > r`, and then the fourth is positive too. So `a` is the strict argmax iff `p > max(q, r)`.

**S3 (PROVED; CHECKED `A2`). Antipodal pattern.**
- `W(a) − W(−a) = pq(p − q)` and `W(a) − W(orthogonal) = p²q − r³`. So `a` is the strict argmax iff `p > q` and `p²q > r³`.
- If `p > q` and `p²q > r³`, then `p³ > p²q > r³`, so `p > r`.
- If `q ≥ r`, then `p > q` already gives `p²q > q³ ≥ r³`, so the condition is `p > q = max(q, r)`.
- If `q < r`, the condition is `p > √(r³/q)`, and `√(r³/q) > r`.
- The direct argmax agrees with the condition, with no mismatch:
  - on all `24³` integer triples, for each pattern separately and for both together;
  - on a 640-point rational grid.

**S4 (PROVED; CHECKED `A3`, `A4`). Failure set and witnesses.**
- The original's "iff" fails exactly for `q < r` and `r < p ≤ √(r³/q)`.
- On the four lines the bands are as in the table in §1; a point inside each band is checked exactly.

**S5 (CHECKED `A4`). Why the runner passed.**
- Block 12's executed couplings on `(p, 1, 2)` are `p = 3, 10, 30, 100, 1000`. All have `p² > 8`, so they lie outside the band.
- The runner's B4 test points are `(3,1,2)`, `(2,1,3)`, `(1,2,1)` and `(2,2,1)`. Each gets the same verdict under the original and the corrected condition, so B4 cannot detect the defect.

**S6 (PROVED; CHECKED `A5`). What does not use the clause.**
- The deviations' expansions `(q³ + 4r³)/p³`, `q/p` and `r/p` (S1's second sentence).
- S3's `ε`, which is the maximum of the deviations over triples with two entries `a`, and its coupling.
- S6's `ε(p) = max(q, r)/p + O(p⁻²)`.
- None of these uses "most likely".

## 3. (b) Every use, with a verdict

Verdicts are "unaffected", "holds on the corrected domain" or "needs its own repair".

### Block 12 note (PR #8146 @ `3acd27d2`)

| Lines | Statement | Verdict |
|---|---|---|
| L4 (claim_scope, S1) | "the majority the most likely value iff p > max(q, r) (proved)" | needs its own repair (the condition) |
| L26–32 | "strongly prefers", "the rule's preference", qualitative | unaffected |
| L40–46 | the closed forms, the eroder, `ε(p)` | unaffected |
| L124 | "S1 … the majority-preference condition \| proved" | holds with the corrected condition (no condition is written in the row) |
| L171–173 | the deviations' leading terms | unaffected (S6) |
| L173–174 | "The majority value of a `2:1` triple is its most likely output iff `p > max(q, r)`." | needs its own repair |
| L176–182 (proof) | orthogonal part; antipodal "… which holds when `p > max(q, r)`" | the orthogonal part holds; the antipodal clause is false for `q < r` and needs its own repair |
| L183–185 | "the preference condition on the two sides of `p = max(q, r)` (B4)" | needs its own repair: no test point lies in the band |
| L209–227 (S3) | `ε` as a maximum of deviations; the attaining patterns at `p = 3, …, 1000` | unaffected |
| L293–304 (S6) | `ε(p) = max(q, r)/p + O(p⁻²)` crosses `ε₀` | unaffected |
| L363 (N7 steelman) | "… the `p > max(q, r)` condition" | needs its own repair (the condition) |
| L369 (Falsifiers) | "a coupling with `p > max(q, r)` at which a `2:1` triple's majority is not the most likely output (B4)" | this falsifier fires at `(5, 2, 4)` and needs its own repair |
| L398 (Families) | "B … the preference condition" | holds with the corrected condition |

### Block 12 pack files (PR #8146 branch)

| Location | Verdict |
|---|---|
| `RESULTS_block12.md` L6 ("the majority is the most likely output iff `p > max(q, r)` (S1)") | needs its own repair |
| `HANDOFF.md` L48 ("majority most likely iff `p > max(q, r)`") | needs its own repair |
| `STATE.yaml` L178 (comment: "majority iff p > max(q,r)") | needs its own repair |
| `GOAL_block12.md` L9 (target statement) | needs its own repair |
| `GOAL_block12.md` L13 (edge case "`p ≤ max(q, r)` (no majority preference; S1's last clause)") | needs its own repair: the no-preference set is `p ≤ max(q, √(r³/q))` |
| `CLAIM_STATUS_CERTIFICATE_block12.md`, `NO_GO_LEDGER.md`, `CHECKER_block12_findings.md` | no use found |

### Other notes of the campaign (PRs #8147–#8178, #8179)

| Note | What it uses | Verdict |
|---|---|---|
| Block 25 (#8168) T0 (L100, L109–113) | re-proves S1's closed forms, the monotonicity of the deviations and S3's coupling; not the argmax clause | unaffected |
| Block 30 (#8174) T1 (L99, L105–109) | the two-level domination from the closed forms | unaffected |
| Block 28 (#8172) | the eroder bound (L116) and "preference strength" as a name for `p` | unaffected |
| Blocks 13 (#8147) and 19–20 (#8153, #8154) | cite block 12 for level time or context | unaffected |
| Block 17 (#8151) and the decision record (#8179) | `max(q, r)` as the static law's own threshold scale `216·max(q, r)`, a different statement | unaffected |

No other note states or uses "the majority is the most likely output". The search covered "most likely", "`max(q, r)`", "block 12" and "#8146" over all 25 fetched notes.

## 4. (c) The exact lines to change

### Note (`3acd27d2`)

- **L4:** "the majority the most likely value iff p > max(q, r) (proved)" → "the majority the most likely value iff p > max(q, sqrt(r^3/q)) (= max(q, r) when q >= r) (proved)".
- **L173–174:** "The majority value of a `2:1` triple is its most likely output iff `p > max(q, r)`." → "The majority value of the orthogonal `2:1` triple is its strictly most likely output iff `p > max(q, r)`, that of the antipodal one iff `p > q` and `p²q > r³`; so every `2:1` triple's majority is its most likely output iff `p > max(q, √(r³/q))`, which is `max(q, r)` when `q ≥ r`."
- **L181–182:** "so `a` wins iff `p > q` and `p² q > r³`, which holds when `p > max(q, r)`" → "so `a` wins iff `p > q` and `p² q > r³` (which forces `p > r`), i.e. iff `p > max(q, √(r³/q))`; for `q < r` this is stronger than `p > max(q, r)` (at `(5, 2, 4)`: `25/163 < 32/163`)".
- **L184–185:** "the preference condition on the two sides of `p = max(q, r)` (B4)" → "the preference condition on the two sides of `p = max(q, √(r³/q))`, including a point of the band `max(q, r) < p ≤ √(r³/q)` (B4)".
- **L363:** "the `p > max(q, r)` condition" → "the `p > max(q, √(r³/q))` condition".
- **L369:** "a coupling with `p > max(q, r)` at which a `2:1` triple's majority is not the most likely output (B4)" → "a coupling with `p > max(q, √(r³/q))` at which a `2:1` triple's majority is not the strictly most likely output, or one with `p ≤ max(q, √(r³/q))` at which every `2:1` majority is (B4)".

### Runner (`scripts/admissibility_rule_strong_coupling_formation_law_level_automaton_eroder_metastability_2026_09_15.py` at `3acd27d2`)

- **L7 (docstring):** "the majority-preference condition p > max(q, r)" → "p > max(q, sqrt(r^3/q))".
- **L285–290 (B4):** add band points, and assert the corrected predicate `p > q and p²q > r³`:
  - `(5, 2, 4)`: the orthogonal majority is the argmax, the antipodal one is not;
  - `(5/2, 1, 2)`: the antipodal majority is not the argmax.
- **L294 (B4 message):** state the corrected condition and the band point.
- **L43–51 and L292–293 (mutations):** keep `majority_preference_wrong`, and add a mutation that swaps in the original condition `p > max(q, r)`; the new B4 fails it.
- **L475 (`N5_LINES`):** "the preference condition at four triples" → "at six triples, two in the band".

### Pack files

`RESULTS_block12.md` L6, `HANDOFF.md` L48, `STATE.yaml` L178, `GOAL_block12.md` L9 and L13: replace `p > max(q, r)` by `p > max(q, √(r³/q))`.

## 5. What would finish it

Nothing in (a)–(c) is open. The edits are the note owner's; no PR is touched here.
