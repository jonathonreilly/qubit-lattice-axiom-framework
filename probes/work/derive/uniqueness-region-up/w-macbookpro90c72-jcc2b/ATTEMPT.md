# uniqueness-region-up, attempt 1 (worker w-macbookpro90c72-jcc2b, model grok-4.6)

Own plan first: enlarge block 08's `3c<1` region on `(p,1,2)` by (i) a two-level block or (ii) disagreement percolation. After that plan, the refereed a2 partial (Wasserstein `W_ρ` with `α=5/4`, uniqueness on the grid `p=37/10,…,51/10`) is used as a platform: independent machinery, the same criterion, a finer grid past `51/10`, and a 2-level same-copy joint diagnostic.

## (1) The statement attempted

Objects of blocks 08 and 28 (PRs #8138, #8172) and the refereed a2 attempt: six-axis menu, product rule on `(p,1,2)`, level automaton, ground metric `ρ=1` (orthogonal), `α` (antipodal), `1≤α≤2`;
\[
\bar\kappa=\max_{w\neq w'}\max_{\lambda_1,\lambda_2\in\mathcal{A}}\sum\lambda_1(u_1)\lambda_2(u_2)\,\kappa(w,w';u_1,u_2),
\]
`κ=W_ρ/ρ` via the orthogonal-then-antipodal plan (an upper bound on true `W_ρ`). If `3\bar\kappa<1`, uniqueness and exponential forgetting from the second level on.

**Statement.** At `α=5/4`, `3\bar\kappa<1` holds at `p=511/100` as well as on the refereed grid through `p=51/10`. So the proved no-memory region on `(p,1,2)` includes `p=5.11`. It fails at `p=512/100` and at every tested `α∈{1,6/5,8/7,5/4,4/3,3/2,7/5}` for `p=52/10`. The same-copy diagonal 5-site joints give a strictly smaller bilinear (`3\bar\kappa_2=0.987…<1` already at `p=52/10`), but mixed-copy environments still realise `\mathcal{A}\times\mathcal{A}`, so that number does not enlarge the uniqueness region.

## (2) Steps

**Step 1 — the a2 criterion (PROVED there; re-CHECKED independently as E0, E1).** `ρ` is a metric for `α≤2`; the plan's cost is `TV+(α-1)(TV-F)` and is feasible (residual mass, if any, sits on one antipodal pair). Averaged recursion `D_{t+1}≤3\bar\kappa D_t` for `t≥1` as in a2 step 4. Independent code: `3c=0.984995` at `p=37/10` and `1.011100` at `p=19/5`; at `p=51/10`, `α=5/4`, `3\bar\kappa=52187574259076840991934694/52321061656792031643757593=0.99744869…<1`, matching a2 on all 30 ordered pairs.

**Step 2 — finer grid (CHECKED as E2).** Same `α=5/4`, independent `W_ρ` plan. `3\bar\kappa<1` at `p=511/100` (`3\bar\kappa=0.99981627…`). `3\bar\kappa>1` at `p=512/100, 513/100, 514/100, 515/100, 52/10`. The uniqueness theorem of a2 step 7 therefore applies at `p=511/100`.

**Step 3 — other `α` (CHECKED as E3).** At `p=51/10`, `α∈{4/3,3/2,7/5}` still contract; `α∈{1,6/5,8/7}` do not. None of these `α` contracts at `p=511/100` except `5/4`. None contracts at `p=52/10`. Changing `α` does not pass `5.2`.

**Step 4 — same-copy 2-level joints (CHECKED as E4; not used for uniqueness).** Two diagonal predecessors of a site have a 5-site cone; the bilinear of `κ` over those `6^5` joints is strictly less than `\bar\kappa` over `\mathcal{A}\times\mathcal{A}` (`3\bar\kappa_2<1` at `p=52/10`). Mixed copy-1 / copy-2 environments in the three-step path of a2 step 4 are still product laws in `\mathcal{A}\times\mathcal{A}` (different copies, different sites). So this smaller number is not a bound on the mixed-copy `D_t` recursion. It is a precise account of where a 2-level improvement would have to go: a coupling that does not mix copies, or a disagreement-percolation that never uses a mixed environment.

**Step 5 — consequences at `p=511/100` (PROVED, as a2 step 7).** `3\bar\kappa<1` implies `D_t→0`, one invariant law, exponential forgetting of the initial plane.

## (3) First failing step, if any

The `𝒜×𝒜` averaged criterion, for every tested `α`, fails to contract at `p=512/100`. That is a no-go for this one-level average past `5.11`. The 2-level same-copy joints do contract at `p=5.2` but do not control mixed-copy environments.

## (4) What would finish it

A recursion whose environments are only same-copy joints of the 5-site cone (so `3\bar\kappa_2` applies), or a two-level block Lipschitz over the 6-site light cone with exact enumeration; either needs to handle the mixed-copy path in a2 step 4 or replace it. The executed threshold `10.5–11` is not reached.
