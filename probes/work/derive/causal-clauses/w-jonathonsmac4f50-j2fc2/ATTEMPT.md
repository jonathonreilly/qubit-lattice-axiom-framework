# causal-clauses: derivation attempt 3 of 3

Worker `w-jonathonsmac4f50-j2fc2` (claude-opus-5), unit `J-derive-causal-clauses-a3`.

**Provenance, stated because it bears on independence.** Two attempts existed at claim time:
`a1` (`w-macbookpro90c72-jc4f8`, another machine and session) and `a2`
(`w-jonathonsmac4f50-j8f9d`, the same machine and running worker as this one). They answer the
task's (a)–(d) and agree with each other. I do not re-derive their theorem, their clause list or
their reading of (c). I take the one item `a1` files under "what would finish it" that is a
mathematical question rather than a decision for the lane:

> "Fix the extent of the past: the finite window of Step 2 or the infinite-past limit (Step 18).
> **This includes a uniqueness proof or a counterexample where `3 α₃ ≥ 1`.**"

## 1. The statement attempted

`a1`'s Step 18 cuts the past of a finite window at level `−L`, couples the cuts level by level
with the maximal coupling at each site, and gets

`P(x differs) ≤ (3α₃)^{ℓ(x)+L}`, `α₃ :=` the largest total variation between two three-parent
kernels differing in one parent,

so the window's law converges as `L → ∞` when `3α₃ < 1`. `a1` reports `3α₃ = 81/110`,
`31950/63407`, `1/3` at `(3,1,2)`, `(5,2,4)`, `(2,1,2)` — all `< 1` — and `390/137 ≈ 2.85` at
`(40,1,1)`, where "this bound gives nothing".

> **(i)** On the campaign's `(p,1,2)` line, where `α₃`'s maximizer holds,
> **`α₃(p) = p²(p−1)(p+33) / ((p³+33)(p²+p+32))`**.
>
> **(ii)** `3α₃ = 1` at **`p* =` the smallest positive root of
> `x⁵ − 2x⁴ − 64x³ + 132x² + 33x + 1056`**, `p* = 3.7563598183…`.
>
> **(iii)** `3α₃ → 3` as `p → ∞`, so the criterion — not the estimate — is what fails at strong
> coupling.
>
> **(iv)** The counterexample `a1` asks for **is the campaign's own ordered phase**: block 25
> (PR #8168) with block 30's sharpening (PR #8174) gives at least two invariant laws of the level
> dynamics for `p ≥ 4165` on `(p,1,2)`, hence two distinct infinite-past limits on the same causal
> DAG. Uniqueness fails there, and `3α₃ = 2.9986`.

So the answer is: **no uniqueness proof is possible in general — the limit really is non-unique —
and the open region is the interval between the two.**

## 2. Steps

**S1 (CHECKED `M1`). `a1`'s four values, recomputed.** From the rule — six axis values, weight
`Π_j φ(a, u_j)` with `φ = p, q, r` on equal, antipodal, other — the largest single-parent
total variation is `27/110`, `10650/63407`, `1/9`, `130/137` at `a1`'s four parameter points,
exactly. `a1` is on another machine; this is a recomputation from the rule, not a re-run of its
script, and it agrees on all four.

**S2 (PROVED for its range; CHECKED `M2`). The closed form.** At `(p,1,2)` the maximizing pair is
three equal parents with one flipped to its antipode, and the total variation is the expression
above. Brute force over all `6³ × 3 × 5` pairs agrees exactly at `p = 5/2, 3, 7/2, 15/4, 4, 5`
and **disagrees at `p = 8` and `p = 20`**, where a different configuration takes over. The closed
form is used only on the range where it is verified, which contains the threshold.

**S3 (PROVED; CHECKED `M3`). The threshold.** Brute force gives
`3α₃ = 1455300/1457713 < 1` at `p = 15/4` and `21011234850/20991436937 > 1` at `p = 94/25`, so
the crossing is between them; on that range `3α₃ = 1` reduces to the quintic, whose smallest
positive root is `p* = 3.756359818320370`. Below `p*`, `a1`'s Step 18 gives a unique infinite-past
limit for every finite window.

**S4 (CHECKED `M4`). Why no sharper constant helps.** `α₃ = 0.9771, 0.99952, 0.99980` at
`p = 100, 4165, 10⁴`: as the kernel becomes deterministic a single parent controls the child, so
`3α₃ → 3`. Any improvement of the coupling estimate that keeps the per-parent influence as its
ingredient is bounded below by the same limit. The criterion fails, not the estimate.

**S5 (CITED, not re-proved; CHECKED `M5` for the arithmetic). The counterexample.** Block 25
proves Toom-type stability of the noisy level automaton — the 3D formation law orders — and block
30 sharpens the threshold to `p ≥ 4165` on `(p,1,2)`. An ordered phase is exactly two distinct
invariant laws, and on a causal DAG the invariant laws of the level dynamics are the infinite-past
limits. So the limit is non-unique there. This is the campaign's own result; I only connect it to
`a1`'s question and check that `3α₃ ≥ 1` at that point.

**S6 (CHECKED `M6`). The map.**

| region on `(p,1,2)` | what is known | source |
|---|---|---|
| `p < 3.7564` | unique infinite-past limit | `a1` Step 18 + S3 |
| `3.7564 < p < 4165` | **open** | — |
| — of which `p ∈ (10.5, 11)` | where block 28 *locates* the transition by execution | PR #8172 |
| `p ≥ 4165` | **not** unique: two invariant laws | blocks 25, 30 |

The located transition sits inside the open interval, and the two proofs stand a factor ~380
apart around it — the same factor block 30 records as its own remaining gap. So the extent of the
past is settled exactly where the ordering question is settled, and nowhere else.

## 3. Where the route stops

- **S5 is a citation.** I do not re-prove block 25's Toom argument or block 30's sharpening; the
  attempt's contribution is the connection and the arithmetic, not the ordering theorem.
- **The identification "invariant law of the level dynamics = infinite-past limit"** is stated,
  not proved here. It is immediate for the finite-window marginals `a1` works with, but I have not
  written the argument, and a referee should treat it as the one soft joint.
- **The closed form is verified on `[5/2, 5]` only**, which is enough for the threshold and
  nothing more. The maximizing configuration changes above, and I did not classify where.
- **Only the `(p,1,2)` line.** The other two campaign points `(5,2,4)` and `(2,1,2)` are inside
  the uniqueness region by `a1`'s own numbers; I did not map the surface.

## 4. What would finish it

1. Close the interval `[3.7564, 4165)`, which is the same problem as closing block 30's remaining
   factor of 380 — the two questions are now known to be the same question.
2. Write the identification in S5's second bullet properly.
3. A criterion that does not go through single-parent influence. The failure in S4 is structural:
   at strong coupling one parent nearly determines the child, so *any* Dobrushin-type sum over
   parents exceeds 1, while the law is perfectly well behaved. What the strong-coupling side needs
   is the Toom route, which is what blocks 25 and 30 use.

## 5. Running it

```
python3 probes/work/derive/causal-clauses/w-jonathonsmac4f50-j2fc2/check.py
```
from the repository root. `sympy` and the standard library; about a minute, most of it in the
exact brute force over the `6³` parent configurations at ten values of `p`.
