# moving-clumping-bounds, attempt 1 of 4 — a uniqueness region below, and an unfinished route above

Worker `w-jonathonsmac4f50-j6200` (`claude-opus-5`), unit `J-derive-moving-clumping-bounds:a1`.

**Provenance.** No prior attempt existed at claim time. Block 39 is taken as the unit states it;
the correction to its reflection-positivity region is **my own earlier result** (issue #8534), same
model family. *(I claimed and released this unit yesterday for lack of time; this is the second
claim, worked properly.)*

## 1. What is claimed

### (b) BELOW — uniqueness

The seven-state single-site conditional is `P(empty) ∝ 1`, `P(a) ∝ z·Π_{occ nbrs} c·ω(a,s_y)`.
Dobrushin's condition here is `6C < 1`.

> **There are two channels, and they move oppositely in the fugacity.**
>
> | | `z=0.1` | `z=1` | `z=10` | |
> |---|---|---|---|---|
> | `(3,1,2)`, `c=c₀` | 1.4133 | 1.6171 | 1.6321 | **rises** — the *content* channel |
> | `(1,1,1)`, `c=2` | 1.0227 | 0.3956 | 0.0488 | **falls** — the *occupancy* channel |
>
> At uniform weights the content carries no information and only occupancy couples; away from
> uniform the content channel dominates. **So a sup over a grid of `z` proves nothing**, in either
> direction — which is why the next step is needed.
>
> **A `z`-free bound.** Changing one neighbour multiplies `w(a)` by `λ_a` and leaves `w(∅) = 1`.
> The five *unchanged* neighbours contribute the **same** factor to both weights and cancel, so
> `λ` depends on **neither them nor `z`**. With the density ratio confined to `[m, M]`,
>
> ```
> C  ≤  (M − m)/(M + m)          — independent of the fugacity
> ```
>
> giving **uniqueness at every fugacity** wherever `6(M−m)/(M+m) < 1`. Certified here for
> `(1,1,1)` and `(9,8,8)` up to `c/c₀ = 5/4`.

### (c) Content-less records — exactly the lattice gas

With `p = q = r = w` the configuration weight is `z^N (cw)^B` — the **lattice gas** of bond
activity `cw`, i.e. Ising with `K = ¼log(cw)`.

- At the neutral scale `c₀w = 1` **exactly**, and the Dobrushin coefficient is **identically 0**:
  the sites are **independent**, so there is *no transition at any fugacity*.
- For `c > c₀`: **literature, not proved here** — the `Z³` Ising transition at `K_c = 0.2216544…`
  puts the clumping onset at `c/c₀ = exp(4K_c) = 2.4269…`.

> **That calibrates the bound**: `5/4` certified against `2.4269…` true, so the `z`-free bound is
> lossy by about a factor two in the one case where the truth is known. I would rather state that
> than leave the reader guessing how conservative it is.

### (a) ABOVE — the region where the tool applies, and no theorem

The chessboard estimate needs bond-plane reflection positivity, which for this law holds exactly
when the `7×7` pair-weight matrix is positive semidefinite:

```
c ≥ c₀    AND    p ≥ q    AND    p + q ≥ 2r
```

the last two **scale-free**. The unit's statement of block 39's condition omits them, and at
`(5,2,4)` the third fails (`7 < 8`), so **no scale makes the tool available there at all**.

> **NOT DONE: the contour argument itself.** Turning a chessboard estimate into two
> translation-invariant states needs a Peierls count whose constant I did not establish. Part (a)
> therefore yields the **exact region where the method applies and no theorem**. This is not a
> precise no-go; it is an unfinished route, and I would rather label it that way.

## 2. The steps

1. **CHECKED (`U1`).** The `c₀` property on three triples.
2. **CHECKED (`U2`).** The exact Dobrushin coefficient (the five unchanged neighbours enter only
   through their multiset, so 462 cases suffice), and the opposite `z`-trends of the two channels.
3. **PROVED + CHECKED (`U3`).** The cancellation of the unchanged neighbours, the `z`-free bound,
   and the certified region.
4. **PROVED + CHECKED (`U4`).** The lattice-gas reduction, `c₀w = 1`, and `C ≡ 0` at `c₀`.
   `K_c` is **literature**.
5. **`U5`.** The RP region, and the explicit statement of what is missing.

## 3. Where this stops

- **(a) has no theorem.** That is the main gap and I do not want it read as a bracket: I give the
  region where the chessboard estimate is *available*, not a proof that two states exist anywhere.
- **The `z`-free bound is lossy**, by about a factor two where measurable. A sharper uniform
  argument — for instance bounding `sup_z C` directly by exploiting that the two channels peak at
  opposite ends — would enlarge the certified region considerably, and I did not do it.
- **The certified region is small and was sampled, not mapped.** I check a handful of triples at a
  handful of `c/c₀`; I do not trace the boundary surface in `(c,p,q,r)`.
- **Dobrushin is sufficient, not necessary**, so failing `6C < 1` says nothing. None of the
  "FAILS" rows is evidence of clumping.
- The `Z³` Ising `K_c` is quoted, not computed, and the lattice-gas↔Ising map is standard.

## 4. What would finish it

1. The Peierls count for (a) — the actual content of the "ABOVE" half.
2. A sharper uniform-in-`z` criterion: the two channels are extremal at `z → 0` and `z → ∞`, so a
   bound that interpolates between the two limits rather than taking a worst case over both should
   recover most of the factor two.
3. Map the boundary of the certified region in `(c/c₀, p/q, r/q)` instead of sampling it.
4. Another model family, particularly on the cancellation argument in `U3` — it is the step that
   makes the bound `z`-free, and if it were wrong the whole "every fugacity" claim would go.

## 5. Running it

```
python3 probes/work/derive/moving-clumping-bounds/w-jonathonsmac4f50-j6200/check.py
```

Standard library plus `fractions`; 9 checks, exact rational arithmetic throughout. Runs in about
a minute.
