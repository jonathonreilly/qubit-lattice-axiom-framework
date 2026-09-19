# Referee report: J:derive:chessboard-repair:a1

Author: `w-jonathonsmac4f50-j877a` (claude-opus-5). Referee: `w-macbookpro90c72-j507f` (grok-4.6).
Problem: repair block 17's chessboard step (T3 disseminated the wrong event) and prove the best constant.

## Does the attempt prove that statement?

Yes, two nested statements: (route A) site reflections alone give T4 with `ε = 6m/p` in 2D (`p ≥ 216m`) and `ε = 6(m/p)^{3/4}` in 3D (`p ≥ 1296m`); (route B) bond-plane reflection positivity when `φ ⪰ 0` restores the original 3D threshold `216m`. The task asked for a correct chain with the best constant; 216 in both dimensions (via B) is that, and the computed lead `p ≥ q` and `p + q ≥ 2r` is proved as the four-site-ring iff and as a sufficient condition on every even torus.

## Step-by-step

**Step 1 (disseminated event) — holds.** Site reflections preserve transverse parities. Independent: on `(Z/4)²` the orbit of the canonical direction-0 bond has size `N/2 = 8` and a single y-parity.

**Step 2 (one-line lemma) — holds.** Each good bond of `s` forces a mismatch with the proper sequence `a`; each site lies in two bonds, so `bad(s) + 2 bad(s,a) ≥ n`. Independent: exhaustive at `n = 4, 6`.

**Step 3 (counting R2) — holds for `2L ≥ 4`.** Even rows contribute `N/2` bad horizontals; each odd row with both neighbouring even rows (distinct iff `2L ≥ 4`) gives `bad_h + U + D ≥ 2L`; verticals are counted once. 3D: class lines `N/4`, plus two odd-parity families each `N/4`. Sharpness patterns attain `N` and `3N/4` on sides 4 and 6. **The author's 4×2 enumeration is false:** that graph is not 4-regular (`+e_y = −e_y`), unique bonds are 12 not 16, and the min in the event is 6 not 8. It is a bad test, not a hole in the `2L ≥ 4` argument. T6 already takes `2L = 2^k ≥ 64`.

**Step 4 (route A) — holds.** Weight decreases in the number of bad bonds for `p ≥ m`; `Z ≥ 6 p^{dN}`; `μ^{1/N} ≤ 6^{(N−1)/N}(m/p)^{b_0/N} ≤ 6m/p` in 2D. Arithmetic `216^{4/3} = 6^4 = 1296` checked.

**Step 5 (bond-plane RP) — holds.** PSD ⇒ crossing weights are a sum of products `g(H^+) g(H^−)` with nonnegative coefficients, hence RP on every even torus. Independent: eigenvalues of `φ` are `p+q+4r`, `p−q` (×3), `p+q−2r` (×2). Converse on the four-site ring: the quadratic form is `φ ⊗ φ` on the diagonal factor, indefinite iff `φ` is; eigmin `< 0` at `(5,2,4)` and `(1,3,2)`, `≈ 0` at `(3,1,2)`, `> 0` at `(216,1,1)`; an explicit integer witness has `Q < 0` off PSD and `Q > 0` on `(3,1,2)`.

**Step 6 (route B chessboard) — holds, with the stated ASSUMED.** Bond-plane reflections in the transverse directions move parity, so the disseminated event is every direction-`i` bond. T3's iteration is ASSUMED as in block 17; it needs `2L` a power of two, which T6 may take. Combining two directions by a geometric mean is valid.

**Step 7 — holds.** `p ≥ 216 max(q,r)` implies `φ ⪰ 0`. T5–T7 then run as written.

## Classic failure modes

- Quantifier: the 4×2 check is a swapped domain (degenerate torus), not a swapped quantifier in the proof.
- Bound only at checked sizes: R2 is proved, then checked on the sharpness patterns; the false 4×2 min is not the proof.
- Outside theorems: spectral theorem on `6×6` real symmetric (eigenvalues recomputed); Cauchy–Schwarz chessboard ASSUMED from T3.
- Circular: none. The executed ordering `p ≈ 3.6` is not used.

## Verdict

The repair survives. First failing *proof* step: none. First failing *check*: the 4×2 min-bad claim in Step 3.

`HIT: confirmed` — see `check.py`.
