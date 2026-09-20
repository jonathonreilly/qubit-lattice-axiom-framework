# ordering-threshold-down, attempt 2 of 5 — the three deviations have no fixed order

Worker `w-jonathonsmac4f50-j3960` (`claude-opus-5`), unit `J-derive-ordering-threshold-down:a2`.

**Provenance.** Three prior attempts exist. Two (`j8265`, `jc31e`) are the same model family,
machine and running worker as this one, and **`j8265` is mine** — it derived the general noise map
used here. The third (`w-macbookpro90c72-jaf39`) is from another machine. I re-run none of their
routes. `j8265`'s §4 item 2 reads *"block 30's note should carry the domain `p ≥ q`"*; this attempt
works out exactly which comparisons that domain is hiding.

## 1. What is claimed

With `d₁ = (q³+4r³)/(p³+q³+4r³)`, `d₂ = (pq²+4r³)/(p²q+pq²+4r³)` and
`d₃ = (q²r+pr²+qr²+2r³)/(p²r+q²r+pr²+qr²+2r³)`:

> **(i)** The numerator of `d₂ − d₁` is `p²(p − q)(pq² + q³ + 4r³)`. Every other factor is positive,
> so
>
> ```
> d₂ > d₁   ⟺   p > q         (an equivalence, not a sufficient condition).
> ```
>
> That is exactly the domain `j8265` asked block 30's note to carry.
>
> **(ii)** The numerator of `d₃ − d₂` is `−p²(q − r)(pq − q² − 2qr − 4r²)`, so `d₂ = d₃` **exactly**
> on `q = r`, or on the surface `pq = q² + 2qr + 4r²`.
>
> **(iii)** Each of the three is the strict maximum somewhere: `d₂` at `(3,1,2)`, `d₃` at `(3,2,1)`,
> `d₁` at `(1,3,2)`. **No fixed one of them dominates the noise map**, so any argument that names
> one as *the* noise parameter is domain-restricted — and the domain is now explicit.
>
> **(iv)** Inside the lane's own regime `p > q`, (i) says `d₁` is never the maximum; but `d₂`
> against `d₃` still flips — `d₂` at `(3,1,2)`, `d₃` at `(3,2,1)` — so a two-level domination that
> assigns fixed roles must either take the maximum or carry `q < r` as a hypothesis.

## 2. The steps

1. **CHECKED (`O1`).** All three reduce to `5/6` at `p = q = r`, the unbiased rule.
2. **PROVED + CHECKED (`O2`).** The factorization of `d₂ − d₁`, verified identically in `p,q,r`.
   Positivity of the remaining factors for positive weights gives the equivalence.
3. **PROVED + CHECKED (`O3`).** The factorization of `d₃ − d₂`, verified identically, plus the
   `q = r` instances `(10,1,1)` and `(4,1,1)` where `d₂ = d₃` exactly.
4. **CHECKED (`O4`).** The six-triple table, with all three indices occurring as the maximum, and
   the cross-check that `d₁` is maximal only where `p < q` — consistent with step 2.
5. **CHECKED (`O5`).** The sign test of (ii)'s two factors against the actual comparison, at four
   triples.

## 3. Where this stops

- **This does not move the threshold.** `j8265` already said so of itself and it is still true:
  the threshold needs `a1`'s and `a4`'s block renormalization, and nothing here touches it. What
  this fixes is the *hypothesis* under which the existing domination arguments are stated.
- **I have not re-read block 30's note.** `j8265` reports that it fixes a role for `max(d₂,d₃)`;
  if that is right, (iii) says the note is safe inside `p > q` and unsafe outside it, and (iv) says
  the max is doing real work rather than being a convenience. I am relying on `j8265`'s reading of
  the note, which is my own earlier reading, not an independent one.
- **No claim about which deviation *should* appear.** The seed/amplification split is a feature of
  the domination construction, not of the noise map, and I have not checked whether the
  construction's roles survive the flip at `(3,2,1)`.
- **`(1,3,2)` is outside the lane's regime** (`p < q` inverts the ordering preference). It is a
  legitimate point of the positive octant and it is what makes (iii) true as stated, but nobody in
  this lane works there — so (iii)'s force in practice is (iv).

## 4. What would finish it

1. Read block 30's note against (i)–(iv) and record the hypothesis it needs, which is now an
   explicit polynomial condition rather than an informal "`p ≥ q`".
2. Check whether the two-level domination's *roles* (seed `d₁`, amplification `max(d₂,d₃)`) survive
   where `d₃ > d₂`; the construction may be indifferent, in which case (iv) is bookkeeping, or it
   may not, in which case `(3,2,1)`-like weights need a separate argument.
3. The surface `pq = q² + 2qr + 4r²` deserves a look: it is the second way `d₂` and `d₃` can
   coincide, and unlike `q = r` it is not an obvious symmetry of the rule.
4. Another family on `j8265` and this attempt, which share both an author and the noise map.

## 5. Running it

```
python3 probes/work/derive/ordering-threshold-down/w-jonathonsmac4f50-j3960/check.py
```

Standard library plus `sympy`; 13 checks, exact symbolic and rational arithmetic.
