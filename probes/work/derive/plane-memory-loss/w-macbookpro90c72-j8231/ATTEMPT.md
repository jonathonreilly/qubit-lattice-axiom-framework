# plane-memory-loss, attempt 1 (worker w-macbookpro90c72-j8231, model grok-4.6)

Independent of grok a3 (twist KL) and a4 (mean-field iff β≤1, route (ii) sign). Here: a no-go for route (ii) from `φ(0)=1`, plus the exact Langevin jet of the mean-field map.

## (1) The statement attempted

**Route (ii) fails.** The linear formation law on the infinite plane has `φ(0)=1` (three-predecessor and seven-predecessor stencils), so the spatial-mean mode is a martingale and does not decay. A comparison that dominates the nonlinear law by the linear law cannot prove `m_t→0`.

**Mean-field.** `|m'|=A(3β|m|)`, `A(k)=coth k-1/k`. Small-`m` rate is `β`. Jet `A(k)=k/3-k^3/45+O(k^5)`. At `β=1`, `|m'|=|m|-(3/5)|m|^3+O(m^5)` (cubic decay). The sign identity `3k\cosh k-3\sinh k-k^2\sinh k` has Taylor `-k^5/15-k^7/210+O(k^9)` (CHECKED). Global `A(k)<k/3` for all `k>0` is ASSUMED (standard Langevin). Mean-field therefore forgets for `β<1` and at `β=1` to this order. Block 27's uniqueness window `β<1/√3` is strictly smaller.

Route (i) and (iii) are not carried out.

## (2) Steps

**Step 1 — `φ(0)=1` (PROVED; CHECKED as E1).** Three-pred `φ=(1+e^{ik_1}+e^{ik_2})/3`; seven-pred `φ=1-E/7`. Both equal 1 at `k=0`. The Fourier zero mode of the linear AR is `θ_{t+1}(0)=θ_t(0)+ξ`, a random walk, not a contraction.

**Step 2 — linear comparison is a no-go (PROVED).** If the nonlinear transverse mean were bounded by the linear evolution, the linear zero mode's non-decay would not force `m_t→0`. (The nonlinear constraint `|s|=1` can still dissipate the mean; that needs another route.)

**Step 3 — mean-field jet (CHECKED as E2–E3).** As above.

**Step 4 — Dobrushin vs mean-field (CHECKED as E4).** `1/√3<1`.

## (3) First failing step of the task's route (ii)

The comparison with the linear model: the linear model does not forget, so the comparison cannot prove forgetting. (a4 recorded a different failure: `|S|≥3|m|` with `A` increasing gives the wrong monotonicity for a contraction.)

## (4) What would finish it

A nonlinear relative-entropy or super-martingale for `|m|^2` that uses `|s|=1` (not the linear AR); or route (iii) with an ergodic theorem for the infinite-plane automaton. Global proof of `A(k)<k/3` (e.g. from the continued fraction of `coth`).
