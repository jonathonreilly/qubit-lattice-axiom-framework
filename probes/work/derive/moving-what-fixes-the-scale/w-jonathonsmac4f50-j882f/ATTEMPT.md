# moving-what-fixes-the-scale: derivation attempt 1 of 5

Worker `w-jonathonsmac4f50-j882f` (claude-opus-5), unit `J-derive-moving-what-fixes-the-scale-a1`.

**Provenance.** No prior attempt on this problem existed at claim time; the claim printed none.
Nothing here builds on another attempt.

**Setting** (block 39's, as the unit states it): a site is empty or carries one record with a
content in the six axes; two neighbouring records weigh `c·ω` with `ω = p, q, r` for equal,
opposite and orthogonal contents; a bond with an empty end weighs `1`; `c₀ = 6/(p+q+4r)`.

## 1. The statement attempted

The unit lists five candidates and asks what each *fixes*. I answer three of them exactly and
say plainly that I did not reach (d) or (e).

> **(a) "No state is privileged", applied to the empty state: only a relation.**
> The sentence says an empty neighbour should weigh what a record neighbour weighs — but not
> *which* average. Four readings one can write with the same words give four different scales:
>
> | reading | `c` | at `(3,1,2)` |
> |---|---|---|
> | arithmetic mean (`c₀`) | `6/(p+q+4r)` | `1/2` |
> | geometric mean | `(pqr⁴)^{−1/6}` | `2^{1/3}3^{5/6}/6 ≈ 0.605` |
> | harmonic mean | `(1/p + 1/q + 4/r)/6` | `5/9` |
> | same content | `1/p` | `1/3` |
>
> All four are distinct. **The sentence fixes a relation, not a number.**
>
> **(b) The identification with block 24's integrated reading: impossible at any scale.**
> With a **pendant** unrecorded site (one occupied neighbour of content `s`) the integrated
> reading contributes `(1/6)Σ_a c·ω(a,s) = c(p+q+4r)/6`, which is `1` — the vacancy weight — **iff
> `c = c₀`**. With **two** occupied neighbours it contributes `c²·(1/6)Σ_a ω(a,s₁)ω(a,s₂)`, and
> that sum takes three distinct values (`s₂ = s₁`, `s₂ = −s₁`, `s₂ ⊥ s₁`) — at `(3,1,2)` they are
> `17/6`, `7/3`, `8/3`. The vacancy contributes the **constant** `1`. A constant cannot equal a
> non-constant function of the neighbours' contents, so **no `c` identifies the two readings once
> an unrecorded site has two occupied neighbours.** `c₀` is special only in the pendant case —
> which is exactly block 24's condition that the readings agree iff every unrecorded component is
> pendant.
>
> **(c) The formation rate: `c₀` is what "on average" gives, and nothing gives it pointwise.**
> With `k` occupied neighbours, averaging each neighbour's content uniformly,
>
> **`⟨Z_k⟩ = 6·(c(p+q+4r)/6)^k = 6·(c/c₀)^k`.**
>
> This equals the empty-neighbourhood value `6` **for every `k` iff `c = c₀`** — and at, say,
> `c = 2c₀` the `k = 2` average is four times the `k = 0` one. But at `c₀` the *pointwise*
> two-neighbour normalizer still takes three distinct values (`17/3`, `14/3`, `16/3` at
> `(3,1,2)`), so **no scale makes the rate neighbourhood-independent pointwise.**

**What this settles.** Of the candidates examined, **exactly one fixes `c₀`**: the formation rate
being independent of the neighbourhood *on average*, at every neighbourhood size. That is also
the sentence that picks the arithmetic mean out of (a)'s four — "the rate a record forms at does
not depend on how many neighbours it has, on average" forces `(c/c₀)^k = 1` for all `k`, hence
`c = c₀`. The other two candidates give a relation and an impossibility.

## 2. Steps

**S1 (PROVED; CHECKED `A1`).** `Σ_a ω(a,b) = p + q + 4r` for any fixed `b` (one equal, one
opposite, four orthogonal), so the arithmetic-mean reading is `c(p+q+4r)/6 = 1`. The other three
means are computed and compared at `(3,1,2)`.

**S2 (PROVED; CHECKED `A2`).** The pendant identity, and that `c₀` is its unique solution.

**S3 (PROVED; CHECKED `A3`).** The three two-neighbour sums, distinct; hence the impossibility.
The argument is one line and needs no scale-dependence: one side of the proposed identity is
constant in `(s₁,s₂)` and the other is not.

**S4 (PROVED; CHECKED `A4`).** `⟨Z_k⟩ = 6(c/c₀)^k`, because the average factorizes over
neighbours: `(1/6)Σ_{s}ω(a,s) = (p+q+4r)/6` independently of `a`. That independence is the whole
mechanism, and it is what makes the arithmetic mean the relevant one.

**S5 (CHECKED `A5`).** The pointwise failure at `c₀`.

## 3. Where this stops

- **(d) and (e) are not attempted.** Consistency between formation and motion — a record formed
  at `x` and moved to `y` against one formed at `y` — is the candidate I would take next, and the
  detailed-balance statement the unit quotes is the tool for it. The memo's natural-unit gate
  (e) I did not look at.
- **(b)'s first half is not attempted**: whether the transfer matrix is a strict contraction on
  the complement of its top state, and whether `c₀` is where an eigenvalue vanishes. What I
  settle is the second half — the identification with block 24's reading — and it is a no-go.
- **The uniform prior over contents is an assumption.** Both (b) and (c) average an unrecorded
  or unknown content uniformly over the six axes. That is the natural reading of "integrated over
  contents" and of "a record of uniformly random content" in the unit's own statement of `c₀`,
  but a different prior would move the arithmetic mean and hence `c₀` itself. Any derivation of
  `c` from this route inherits that choice, and it should be stated wherever `c₀` is.
- **Nothing here is dynamical.** The motion rule enters only through the static law it is in
  detailed balance with; I have not simulated `moving_gas.py`.

## 4. What would finish it

1. (d): formation-then-motion against formation-in-place. If that consistency also forces `c₀`,
   the scale has two independent derivations and the primitive is discharged; if it forces
   something else, the two sentences disagree and the lane has a fork to record.
2. The prior in S3's caveat: is "uniformly random content" itself derivable, or is it the same
   choice appearing twice?
3. (b)'s transfer-matrix half, which is the only candidate that could make `c₀` special for a
   spectral reason rather than an averaging one.

## 5. Running it

```
python3 probes/work/derive/moving-what-fixes-the-scale/w-jonathonsmac4f50-j882f/check.py
```
from the repository root. `sympy` only; a few seconds.
