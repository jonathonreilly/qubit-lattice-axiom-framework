# corrigendum-PR8146: derivation attempt 2 of 2

Worker `w-jonathonsmac4f50-jd9fc` (claude-opus-5), unit `J-derive-corrigendum-PR8146-a2`.

**Provenance, stated because it bears on independence.** The other attempt, `a1`
(`w-jonathonsmac4f50-jdc8c`), is by the same model family, machine and running worker. It gives
the corrected S1, the verdict table and the line list, and closes with *"Nothing in (a)–(c) is
open."* That sentence is the one worth testing.

**Result.** `a1`'s corrected condition is right — re-derived here from the weights, independently
— and its line list is not complete. A machine sweep of the block's own pack finds one file it
never mentions, and **that file is the reason the defect survived**.

## 1. The statements attempted

**(i) The condition, re-derived.** For a `2:1` triple (two predecessors at `v`, one at `w`):

| | weights |
|---|---|
| `w = −v` | `v → p²q`, `−v → q²p`, each of the four others `→ r³` |
| `w ⊥ v` | `v → p²r`, `w → r²p`, `−v → q²r`, `−w → r²q`, the two remaining `→ r³` |

The antipodal margins factor as `pq(p − q)` and `p²q − r³`; the orthogonal ones as
`pr(p − r)`, `r(p−q)(p+q)`, `r(p² − qr)`, `r(p−r)(p+r)`. So the majority is the argmax iff

> **`p > q` and `p²q > r³`, i.e. `p > max(q, √(r³/q))`** — `a1`'s formula,

and it **subsumes `p > r`**: `√(r³/q) ≥ r` exactly when `r ≥ q`, and when `r < q` the max is `q`,
itself `> r`. That is why two terms are the whole condition.

**(ii) The band, exactly.** The original fails where `p > max(q,r)` but `p²q ≤ r³`. From
`p > r` and `p²q ≤ r³` we get `r³ ≥ p²q > r²q`, so `r > q`, and `p ∈ (r, √(r³/q)]`. Hence

> **the band is exactly `{ q < r < p ≤ √(r³/q) }`, non-empty precisely when `q < r`.**

On the campaign's own line `(p,1,2)` it is `2 < p ≤ 2√2 = 2.828…` — a real interval, which is
why `a1` finds `(5/2, 1, 2)` there. `(5,2,4)` is the documented point; `(3,1,2)` and `(5,2,3)`
are outside.

**(iii) The miss.** `a1`'s line list names the note, the runner, `RESULTS_block12.md`,
`HANDOFF.md`, `STATE.yaml` and `GOAL_block12.md`. It never names
`.claude/science/…/ASSUMPTIONS_AND_IMPORTS.md`, whose line 78 — block 12's entry among the
file's six — reads:

> "- Counterfactual pass: a menu with `q ≥ p` or `r ≥ p` (the majority is not the most likely
> output; S1's condition fails, S3's `ε` is not small); …"

**(iv) Why that one matters.** `q ≥ p or r ≥ p` is the **negation of the defective condition**.
By (ii) the menus where the majority is not the most likely output are strictly more than that —
the band also fails, and `(5,2,4)` is in it. So the block's own **counterfactual pass, an
executed check designed to exhibit what happens when S1's condition fails, selects its menu by a
rule that can never enter the band.** At `(5,2,4)` the selector says "not a counterfactual menu"
while the majority is not the most likely output. **The check inherits the defect it was meant
to guard**, and it would have found it had it been written with the corrected condition.

## 2. Steps

**S1 (PROVED; CHECKED `U1`).** The weights and the eight margins, factored.
**S2 (PROVED; CHECKED `U2`).** The band, with four test points on both sides.
**S3 (CHECKED `U3`).** The two documented band points, from the weights: at `(5,2,4)` the
antipodal weights are `v → 50`, `−v → 20`, others `→ 64`, so the argmax is *another* value.
**S4 (CHECKED `U4`).** The pack file exists at block 12's head `3acd27d2fca8`, carries six
counterfactual entries, and block 12's is line 78 with the quoted selector.
**S5 (`U5`).** The consequence, and the replacement line.

## 3. Where this stops

- **`a1`'s (a) is not disputed** and its verdict table for the note is not re-audited line by
  line; I checked its PR coverage by machine (the sweep's hits fall in PRs #8146, #8151, #8154,
  #8168, #8179, all of which `a1`'s table mentions) and then looked inside block 12's own pack,
  which is where the miss is.
- **One pack file.** I did not audit the other pack files of the other blocks for the same
  pattern — a counterfactual or a mutation selected by a condition that is itself being
  corrected. Given that this is the second such finding in two corrigendum units, it is probably
  worth doing across the campaign.
- The replacement wording in (iv) is a suggestion; the note's owner writes the edit.

## 4. What would finish it

1. Add `ASSUMPTIONS_AND_IMPORTS.md:78` to the packet, reading "a menu with
   `p ≤ max(q, √(r³/q))`".
2. Sweep the campaign for the general pattern: **executed checks whose selector is the statement
   under correction.** Block 12's counterfactual pass here, block 13's refutation-target list and
   block 34's phase-blind control in the other two corrigendum units — three instances in three
   packets suggests it is systematic, and it is cheap to search for.

## 5. Running it

```
python3 probes/work/derive/corrigendum-PR8146/w-jonathonsmac4f50-jd9fc/check.py
```
from the repository root; it fetches block 12's branch if absent. `sympy`; a few seconds.
