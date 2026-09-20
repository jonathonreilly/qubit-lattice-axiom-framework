# corrigendum-PR8178: derivation attempt 2 of 2

Worker `w-jonathonsmac4f50-j888a` (claude-opus-5), unit `J-derive-corrigendum-PR8178-a2`.

**Provenance, stated because it bears on independence.** Attempt `a1`
(`w-jonathonsmac4f50-j9532`) was written by the same model family, on the same machine, by the
same running worker. This is not an independent second opinion on it. I therefore did not
re-derive `a1`'s result along `a1`'s route; I took the hostile-reader position on the two things
`a1` asserts but does not check — that changing the **formula** is the repair to make, and that
its line list is **complete** — and tested both by machine. Both tests found something.

**Sources**, at the heads `a1` pins and `check.py` re-pins: block 34 = PR #8178 at
`e6ffae5b460b`, block 35 = PR #8180 at `7c844adf7555`, and the other 23 campaign PRs
(#8146–#8158, #8168, #8170–#8177, #8179) at their heads for the audit.

## 1. The statements attempted

**(a) The corrected statement.** Unchanged from `a1` in substance, re-derived by two machineries
that are not `a1`'s: with `θ̂_k = L^{−1} Σ_x e^{−ik·x} θ_x` the multiplier of
`(Pθ)_x = (θ_x + θ_{x−e₁} + θ_{x−e₂})/3` is `φ_c = (1 + e^{−ik₁} + e^{−ik₂})/3`, and with
`θ̂_k = L^{−1} Σ_x e^{+ik·x} θ_x` it is the stated `φ`. **What is new here is that the note's
defect is confined to one sentence, and that the sentence admits two repairs of very different
cost — and the cheaper one is not the one `a1` recommends.**

**(b) The repair.** Note line 85 reads, in one sentence: *"for `k ∈ (2π/L)Z_L²`,
`θ̂_k = L^{−1} Σ_x e^{−ik·x} θ_x`; `P` acts as multiplication by `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`"*.
Both halves of the defect are there. T1.1 (line 104) restates the formula, and its proof names
the step it skips: *"each shift multiplies `θ̂_k` by `e^{−ik·e}`; the conjugate convention gives
the stated `φ`"*. So:

> **Repair A** (`a1`'s section (c)): `φ → φ_c` in ten lines. Three are executed or frozen — the
> runner's line 199 is code, its line 206 is a check's text, and runner-cache line 18 is that text
> frozen — so A means re-running block 34's runner and regenerating its cache.
>
> **Repair B**: change the transform in line 85 to `e^{+ik·x}`, and the clause in T1.1's proof.
> Two clauses of prose. T1.1 is then true exactly as written; nothing downstream moves; the
> runner, its frozen cache, `GOAL`, `RESULTS` and `HANDOFF` all stay as they are.

**(c) The line list.** `a1`'s list is short by one: `HANDOFF.md:30` carries the formula and is not
in it. Under repair B no line changes but the two clauses; under repair A the list is ten, not
nine.

## 2. Steps

**S1 (PROVED; CHECKED `D1`). The multiplier under each transform.**
- `Σ_x e^{∓ik·x} θ_{x−e} = e^{∓ik·e} Σ_y e^{∓ik·y} θ_y`, so the multiplier is
  `(1 + e^{∓ik₁} + e^{∓ik₂})/3` for the transform `e^{∓ik·x}`.
- `D1` checks it two ways, neither of them `a1`'s matrix construction in `Q(ζ_L)`: symbolically on
  `L = 3, 4` with a symbol per site, summing the transform at every one of the `L²` modes for both
  signs; and numerically with numpy's `fft2` (which is `Σ_x e^{−ik·x}`) on random fields for
  `L = 3..8`, where `|(Pθ)^ − φ_c θ̂| ≤ 4e−16` and `|(Pθ)^ − φ θ̂|` reaches `0.6`.

**S2 (PROVED; CHECKED `D2`). Where the stated `φ` is right anyway.**
- `φ − φ_c = (2i/3)(sin k₁ + sin k₂)`, which vanishes iff `n₁ + n₂ ≡ 0 (mod L)` or, for even `L`,
  `n₂ − n₁ ≡ L/2`. `D2` checks the two descriptions agree exactly for `L = 2..12` (`a1` went to
  `10`), and that for every `L ≥ 3` some mode disagrees.

**S3 (PROVED; CHECKED `D3`, `D4`). Why nothing executed caught it.**
- `|φ| = |φ_c|`, so `T1.2`, the mode variances, `τ_L`, `V_L`, `S_L` and block 35's `T2`/`T3` moduli
  cannot distinguish the two.
- Block 34's own refuting pass is phase-blind **by construction**: its line 23 uses
  `u = (3 + 2cos k₁ + 2cos k₂ + 2cos(k₁−k₂))/9`, which is `|φ|²`. `D4` checks that identity.
- So no executed check in block 34 — runner or control — has any phase in it. This is the reason
  the defect survived a refuting pass, and it is the thing to fix in the runner whichever repair
  is taken.

**S4 (PROVED; CHECKED `D5`). Block 35's refuter does see the phase, and it measures `φ`.**
- Its mode vector is `e_x = e^{+ik·x}/L` — the explicit basis, not numpy's convention — and it
  checks `conj(e)·Σ·(Pˢ)ᵀ·e / conj(e)·Σ·e` against `φˢ`.
- `D5` verifies exactly, for `L = 3, 4` and every mode, that `P e_k = φ_c e_k` and
  `Pᵀ e_k = φ e_k`. The second identity makes the refuter's ratio `φˢ` **identically, for any
  covariance `Σ` and any level `t`** — so its passing tells us the convention, not the dynamics.

**S5 (PROVED; CHECKED `D6`). Block 35's sampler measures `φ` too.**
- It transforms with `fft2` (`e^{−ik·x}`) and compares against `φ`. With `f_k(t)` that coefficient,
  `f_k(t+1) = φ_c f_k(t) + noise`, so `E[f_k(t) conj(f_k(t+s))] = conj(φ_c)ˢ Var = φˢ Var`: with
  the ordering the sampler accumulates, `φ` is again the measured symbol.
- Both of block 35's executed routes therefore agree with `φ` as the notes state it. Repair B
  keeps that agreement with no edit; repair A keeps block 35 correct too (its `T1` is stated in its
  own convention, which `a1` gets right) but leaves the same letter `φ` meaning conjugate things in
  two notes of one campaign.

**S6 (CHECKED `D7`). The audit.**
- `check.py` walks every file the 25 campaign PRs add or change at their pinned heads and selects
  the lines carrying a complex exponential of `k` or a multiplier formula: 47 lines in all across
  the campaign, of which 10 are block 34's `φ`.
- Nine are `a1`'s. The tenth is `HANDOFF.md:30`. `D7` asserts both directions: every line `a1`
  lists still carries the formula at the pinned head, and the set difference is exactly that one
  line.
- The wider patterns (`np.fft`, `multiplier`, `fft2`, `sp.exp(-sp.I`) that `a1`'s search did not
  use turn up two more objects that `a1`'s table does not mention: block 34's control (S3) and
  block 35's refuter (S4). Neither needs an edit; both change what the packet should say.
- Outside block 34 the formula-bearing lines are block 13's `|φ|²` (#8147), the static-law
  transforms of blocks 19–23 and 29, and block 35's own. `a1`'s verdicts on those stand; I checked
  them by reading, not by machine, and say so.

## 3. Where the route stops

- The **choice between A and B is not a mathematical question** and this attempt does not settle
  it: both repairs are correct. What is settled is their cost, and that A is the one that
  invalidates a frozen artefact. A supervisor who prefers the `e^{−ik·x}` convention across the
  campaign should take A and re-run; one who wants the executed evidence and the notes to keep
  agreeing without a re-run should take B.
- The audit is a **line-level** search. It cannot see a statement that uses the multiplier without
  writing it down. I read block 35's note and runner for that and found none beyond `a1`'s table,
  but a reader who wants certainty has to read all 25 notes.
- I did not re-verify `a1`'s verdicts for blocks 13, 19–23 and 29 by machine.

## 4. What would finish it

1. The supervisor picks A or B. If B, the two clauses are: note line 85's `e^{−ik·x}` → `e^{+ik·x}`,
   and T1.1's proof clause → *"each shift `θ ↦ θ_{·−e}` multiplies `θ̂_k` by `e^{+ik·e}`, so
   `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`"*. If A, the list is `a1`'s nine plus `HANDOFF.md:30`, and
   block 34's runner and cache are regenerated.
2. **Either way**, block 34's runner needs one phase-sensitive check, because S3 shows it has none.
   The cheapest is `D1`'s symbolic diagonalization at `L = 3`: it fails under the wrong pairing of
   transform and multiplier, which no current check does.
3. Block 35's note should state its covariance ordering (`Cov(X,Y) = E[X Ȳ]`) explicitly, which is
   `a1`'s line-87 point and stands under both repairs.

## 5. Running it

```
python3 probes/work/derive/corrigendum-PR8178/w-jonathonsmac4f50-j888a/check.py
```
from the repository root. It fetches the two PR branches if they are not already present, and
needs `sympy`; `numpy` is used for one half of `D1` and skipped if absent. About a minute.
