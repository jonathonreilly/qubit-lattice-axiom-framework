# ordering-threshold-down: derivation attempt 5 of 5

Worker `w-jonathonsmac4f50-j8265` (claude-opus-5), unit `J-derive-ordering-threshold-down-a5`.

**Provenance, stated because it bears on independence.** Two attempts existed at claim time:
`a1` (`w-macbookpro90c72-jaf39`, another machine) and `a4` (`w-jonathonsmac4f50-jc31e`, the same
machine and running worker as this one). Between them they close route (ii), price the refinement
histories, carry out the exhaustive small-cone check, and agree that a block renormalization is
the remaining lever. **I do not attack the threshold.** With the time this unit had, a fifth
attempt at a route two careful attempts have costed would be a guess.

**What this attempt does instead.** The task carries a note that is not about the threshold:

> "NOTE a confirmed defect: block 30's T1(a) `d_1 ≤ max(d_2, d_3)` is false for general positive
> weights (fails at `(1,2,1)`); **establish it on the lines you use.**"

Both attempts establish it on `(p,1,2)` and stop there. A lemma a campaign leans on deserves its
**domain**, not a line — and the domain turns out to be one inequality.

## 1. The statements attempted

The deviations, for **every** positive `(p,q,r)` (the right value is `v`; `φ = p, q, r` for equal,
antipodal, orthogonal; a site's kernel weights `a` by `Π_j φ(a, u_j)`):

`d₁ = (q³ + 4r³)/(p³ + q³ + 4r³)` — all three predecessors right;
`d₂ = (pq² + 4r³)/(p²q + pq² + 4r³)` — one at the antipode;
`d₃ = (q²r + pr² + qr² + 2r³)/(p²r + q²r + pr² + qr² + 2r³)` — one orthogonal.

> **(i) The repair.** The numerator of `d₂ − d₁` factors as `p²(p − q)(pq² + q³ + 4r³)`, whose
> last factor is positive, so
>
> **`d₁ ≤ d₂` if and only if `p ≥ q`.**
>
> **(ii) The full criterion.** `d₁ ≤ max(d₂,d₃)` iff `p ≥ q` **or**
> `p²r + pq² + pqr + 2pr² ≥ q³ + 4r³`.
>
> **(iii)** At `(1,2,1)` both halves fail (`p < q`, and the cubic is `−3`), which is exactly the
> documented counterexample. The second half is not idle: at `(1, 21/20, 1/2)` we have `p < q` but
> the cubic is `7759/8000 > 0` and T1(a) holds.
>
> **(iv) The branch of `ε₂`.** `d₂ − d₃` has numerator `p²(q − r)(pq − q² − 2qr − 4r²)`, so
> `ε₂ = max(d₂,d₃)` switches on that surface — which on `(p,1,2)` is `21 − p`, i.e. `a4`'s
> crossing at `p = 21`, now in general.
>
> **(v) A cross-lane identity.** `α₃ = d₂ − d₁` identically, `α₃` being the Dobrushin
> single-parent influence of the `causal-clauses` lane.

**So T1(a) holds for every rule in which alignment is at least as likely as anti-alignment**, and
`r` does not enter that half at all. Every line the campaign uses — `(p,1,2)` with `p ≥ 1`,
`(p,1,1)`, `(p,2,4)` — is inside it.

## 2. Steps

**S1 (PROVED; CHECKED `Q1`). The general map.** The three deviations are read off the kernel. The
check confirms they restrict on `(p,1,2)` to `a4`'s closed forms `33/(p³+33)`,
`(p+32)/(p²+p+32)`, `(2p+11)/(p²+2p+11)`, which is the independent confirmation that the general
expressions are the same objects the two prior attempts use.

**S2 (PROVED; CHECKED `Q2`). `d₁ ≤ d₂ ⟺ p ≥ q`.** Exact factorization; the cofactor
`pq² + q³ + 4r³` is a sum of positive terms.

**S3 (PROVED; CHECKED `Q3`). The full criterion and both witnesses.** The `d₃ − d₁` numerator is
`p²` times the stated cubic, so the disjunction is exact. `(1,2,1)` fails both halves; the
`(1, 21/20, 1/2)` witness shows the second half is doing work, so the criterion cannot be
simplified to `p ≥ q`.

**S4 (PROVED; CHECKED `Q4`). The `ε₂` branch, in general.**

**S5 (PROVED; CHECKED `Q5`). `α₃ = d₂ − d₁`.** The `causal-clauses` lane found the maximizing
configuration for the Dobrushin influence to be *three equal parents with one flipped to its
antipode* — which is precisely the pair `(d₁, d₂)` of this lane. The two constants coincide
identically, on the line and by the same factorization in general. **The uniqueness lane's
Dobrushin constant and the ordering lane's noise map are one object**, which is worth one line in
both notes: a bound proved for one is a statement about the other.

## 3. Where this stops

- **It is not a threshold.** The unit asked for a proved threshold below 58 on `(p,1,2)`; this
  attempt does not deliver one, and says so. `a1` and `a4` between them have costed routes (i) and
  (ii); their shared recommendation — a block renormalization — stands untouched here.
- **The domain is for T1(a) alone.** Block 30 has other steps with their own weight conditions,
  and I have not audited them.
- **(v) is an identity of constants, not of theorems.** That `α₃ = d₂ − d₁` does not by itself
  transport a result from one lane to the other; it says the two lanes are estimating the same
  number, so an improvement in either is an improvement in both.

## 4. What would finish it

1. The threshold still needs `a1`'s and `a4`'s block renormalization. Nothing here changes that.
2. Block 30's note should carry the domain `p ≥ q` (or the disjunction) with T1(a), and the
   `(1,2,1)` counterexample beside it, so the next reader does not re-find it.
3. The identity in (v) belongs in both notes.

## 5. Running it

```
python3 probes/work/derive/ordering-threshold-down/w-jonathonsmac4f50-j8265/check.py
```
from the repository root. `sympy` only; a few seconds.
