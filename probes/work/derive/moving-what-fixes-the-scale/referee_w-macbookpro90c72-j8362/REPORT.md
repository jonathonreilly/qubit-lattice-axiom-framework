# Referee report: J:derive:moving-what-fixes-the-scale:a2

- **Author:** `w-jonathonsmac4f50-jc19a` (`claude-opus-5`).
- **Referee:** `w-macbookpro90c72-j8362` (`grok-4.6`). Different model family.
- **Checks:** the six-axis stencil, recomputed for every pair. The author's script is not called.

## The statement

An empty site weighs 1. An averaged record with `j` occupied neighbours weighs `c^j (1/6) Σ_s Π_i ω(a_i, s)`. These agree for one neighbour only at `c₀ = 6/(p+q+4r)`. At two neighbours the three pair classes disagree unless `p = q = r`. Averaging the neighbours as well restores 1 at `c₀` for every `j`.

## Steps

**1.** For each of the six contents, `Σ_s ω(a,s) = p+q+4r`. So the one-bond weight is `c S/6`, equal to 1 only at `c = 6/S`.

**2.** The pair sums are `p²+q²+4r²`, `2pq+4r²` and `2r(p+q)+2r²`, and every one of the 36 pairs falls in its class. The equal-minus-opposite difference is `(p−q)²`. With `p = q` the remaining difference is `2(p−r)²`, so the three branches meet only at `p = q = r`.

**3.** `Σ_a ω(a,s) = S` as well, so averaging the neighbours gives `(c S/6)^j`.

**4.** `12r(p+q+r) − (p+q+4r)² = −(p+q−2r)²`. So the orthogonal branch equals 1 at `c₀` exactly when `p+q = 2r`. That holds for `(3,1,2)` and `(7,3,5)`, and not for `(5,2,4)` or `(5,1,1)`.

The uniform prior over contents is the one used here, as in the attempt. It is not derived.

## Verdict

The partial result survives. Matching an empty site to an averaged record fixes `c₀` at one bond and does not fix it at two.
