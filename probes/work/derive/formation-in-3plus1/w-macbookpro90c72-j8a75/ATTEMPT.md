# formation-in-3plus1, attempt 2 (worker w-macbookpro90c72-j8a75, model grok-4.6)

Own plan: the task’s comparison route — `A(κ)/κ` decreasing — as the first LRO lemma, plus the linear metric. Locked from `formation_levelplane.py` before reading a1’s writeup. a1 (same family, unrefeered) has the linear dichotomy; this attempt is the Langevin comparison and the mean-field threshold, which a1 did not claim.

Setting: backward 3+1, `n=4`, `φ=(1+∑ e^{-ik_j})/4`, sphere vMF. (a) LRO, (b) kernel bounds, (c) dichotomy, (d) drift/response.

## (1) The statement attempted

**Statement (PARTIAL).** (i) `A(κ)/κ` is strictly decreasing on `(0,∞)`, with `lim_{κ→0} A(κ)/κ=1/3` and `lim_{κ→∞} A(κ)/κ=0`. Proof: `(A/κ)'=-g/κ³` with `g=n(2κ)/(4\sinh^2 κ)` and `n(u)=u^2+u\sinh u-4\cosh u+4`, and `n(0)=n'(0)=n''(0)=n'''(0)=0`, `n''''=u\sinh u≥0` for `u≥0`, so `n>0` on `(0,∞)`. (ii) Mean-field map `m↦A(nβ m)` has derivative `nβ/3` at 0, unstable iff `β>3/n=3/4`. (iii) `1-|φ|^2=k^T M k+O(k^4)` with `M=H/2`, `H`-eigs `1/8` (once, along `(1,1,1)`) and `1/2` (twice), hence `M`-eigs `1/16` and `1/4`; drift of `φ` is `(1,1,1)/4`. (iv) `G_4=1913/1344` finite. Sphere LRO on `Z^4` is not proved; (b) and (d) stay executed.

## (2) Steps

**Step 1 — `A/κ` decreasing (PROVED; CHECKED P1).** As in the statement. The four vanishing derivatives at 0 plus `n''''≥0` give `n≥0` by integrating.

**Step 2 — MF threshold (PROVED; CHECKED P2).** `A'(0)=1/3` by series `A=κ/3+O(κ³)`.

**Step 3 — metric and drift (PROVED; CHECKED P3).** Hessian of `1-|φ|^2` at 0 is the displayed `3×3` matrix; `Im φ(k_1,0,0)=-k_1/4+O(k^3)`.

**Step 4 — `G_4` (CHECKED P4).** Cosine form of `1-|φ|^2` on `(Z/4)^3`.

## (3) Where the route stops

The comparison `A(κ)/κ≤1/3` bounds the vMF transverse variance by the infinite-temperature value. That does **not** by itself give LRO: the linear model with `σ²=A(nβ)/(nβ)` already has a finite return sum in `d=3`, but passing from the linear Gaussian to the sphere law needs a correlation inequality (the task’s “block 27 sign lemma”) which is not proved here. First missing step for (a): a domination `S_{\mathrm{sphere}}(k)≤C S_{\mathrm{lin}}(k)` or a Lyapunov for the plane average that uses Step 1.

## (4) What would finish it

A Griffith / Ginibre / block-27 comparison putting the sphere below a massive Gaussian at large `β`, or a chessboard estimate in level time. Then (b) follows from the linear kernel and the domination.
