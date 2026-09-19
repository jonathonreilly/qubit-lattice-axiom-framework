# uniqueness-region-up, attempt 3 (worker w-macbookpro90c72-j736b, model grok-4.6)

Plan, locked before reading a1/a2: task candidate (ii), not Wasserstein.
Two-step Hamming/Dobrushin of the level automaton, with the six 2-step
influences computed by exact enumeration of each grandchild's 5-site
boundary (7776 configurations), not by the path bound `N c^d`.

Grok a1 and claude a2 (both refereed) use an averaged `W_ρ` contraction
and reach `p = 511/100`. This attempt does not re-run that criterion.

Notes: block 08 (PR #8138) `c_k = max TV` of the `k`-neighbor product
kernel at a one-site flip, uniqueness when `3c < 1`; block 28 (PR #8172)
`3c(37/10) = 406962630/413162167 < 1`, `3c(19/5) = 871815/862244 > 1`,
executed formation memory on `(p,1,2)` in `(10.5, 11)`. Control:
`probes/lib/scan_formation_sixaxis.py` (level PCA, three predecessors).

## (1) The statement attempted

Six-axis product rule on `(p,1,2)`, level order on `Z^3`: the record at a
plane site `x` is drawn from
`r(s | a,b,c) ∝ φ(s,a)φ(s,b)φ(s,c)`, independently given the previous
plane, with `φ(s,a) = p` (same), `1` (antipodal), `2` (orthogonal).

**Exact partial.** Let `I_1` (resp. `I_2`) be the maximum total variation
of the two-step law of a 1-path (resp. 2-path) grandchild of a single
seed, over the 5 free sites in that grandchild's 2-step cone and over a
seed flip. The 2-step cone of any site has six ancestors (three of each
type). The Dobrushin row-sum is `λ₂ = 3 I_1 + 3 I_2`. Then:

- `λ₂(499/100) < 1` (CHECKED L.3). Any two copies of the PCA, from
  arbitrary initial planes, have one-site (and finite-window) total
  variation `O(λ₂^{⌊t/2⌋})` at level `t`. Hence at most one invariant
  plane law, and exponential forgetting, at `p = 499/100`. The same
  holds at every tenth `p = 38/10, …, 49/10` (CHECKED L.2 at `19/5` and
  `49/10`).
- `λ₂(5) = 4283413252/4276289513 > 1` (CHECKED L.4). The 2-step
  worst-case Hamming criterion does not fire at `p = 5`.
- Block 08's `3c < 1` already fails at `p = 19/5` (CHECKED C.2), so this
  is a genuine enlargement of the *worst-case* region (path count
  `3^n c^n`) from `p ≤ 37/10` to `p ≤ 499/100`. It does **not** improve
  on the refereed averaged `W_ρ` edge `p = 511/100`.

## (2) Steps

**Step 1 — kernel and `c_3` (PROVED; CHECKED C.1–C.3).** Menu `{0,…,5}`
with antipode `a ⊕ 1`. Homogeneous weights `(p,1,2) = (n,d,2d)` when
`p = n/d`. `c_3 = max TV(r(·|a,b,c), r(·|a',b,c))` over one-site flips.
Matches block 08/28: `c_3(3,1,2) = 27/110`, `3c(37/10)` and `3c(19/5)`
the named rationals. The maximizer is an antipodal flip.

**Step 2 — 2-step cone (PROVED).** In plane coordinates the three
predecessors of `x` are `x`, `x-e_1`, `x-e_2`. A seed at `0` is an
ancestor of six sites two levels later: three 1-path grandchildren
`(0,0)`, `(2,0)`, `(0,2)` and three 2-path grandchildren `(1,0)`,
`(0,1)`, `(1,1)`. Each grandchild's 2-step cone has the seed plus five
free sites (`6^5 = 7776`). The product kernel is symmetric in the three
predecessor slots, so the three 1-path (resp. 2-path) influences are
equal (CHECKED G.1: a second 2-path geometry matches `I_2` at `p = 5`).
Cube symmetry of antipodal vs orthogonal seed flips: it is enough to
maximise over `0→1` and `0→2` (CHECKED G.2: `0→4` agrees with `0→2` at
`p = 5`).

**Step 3 — exact `I_1`, `I_2` (CHECKED L.1–L.4).** The two-step law of a
grandchild is the mixture `E[r(·|U,V,W)]` over its three level-`t+1`
predecessors. Type 1: only one of those three depends on the seed.
Type 2: two depend on the seed. Exhaustive integer-arithmetic TV over
all 7776 boundaries. At `p = 499/100`,
`I_1 = 2814194140585462320880754573399455270870200 / 24625783511450273112712758399765677226463799`,
`I_2 = 5371225220303023355156424506650509468563499 / 24625783511450273112712758399765677226463799`,
`λ₂ = 3(I_1+I_2) < 1`. At `p = 5`, `λ₂ = 4283413252/4276289513 > 1`.

**Step 4 — Dobrushin telescoping (PROVED).** The law of site `x` at level
`t+2` is a function of six sites at level `t`. Flipping those six, one
at a time, and applying the triangle inequality for TV,
`TV(law_x(σ), law_x(τ)) ≤ I_1·(# 1-path ancestors that differ) + I_2·(# 2-path ancestors that differ) ≤ λ₂`.
Iterating: after `2k` levels the one-site TV is `≤ λ₂^k` for *any* pair
of initial planes (the bound does not require a finite initial
disagreement set). A finite window of `m` sites has Hamming expectation
`≤ m λ₂^k`, so every local statistic forgets the initial plane. Two
invariant laws would be equal on every finite window. Existence of at
least one invariant law on a finite menu is compactness of product
space (ASSUMED: Krylov–Bogolyubov for a Feller PCA on a compact metric
space; not used for the contraction itself). One extra 1-step costs at
most `3c` (finite), so odd levels vanish too.

**Step 5 — comparison with `3^n c^n` (PROVED).** The path bound gives
`λ₂ ≤ 3 c^2 + 3·(2 c^2) = 9 c^2 = (3c)^2`, which is `< 1` iff `3c < 1`.
Exact enumeration is strictly tighter: at `p = 19/5`, `(3c)^2 > 1` while
`λ₂ < 1` (CHECKED L.2 vs C.2). That is the purchase of candidate (ii).

## (3) Where the route stops

`λ₂(5) > 1`. Worst-case 2-step Hamming does not reach the executed
threshold `(10.5, 11)` and does not beat averaged `W_ρ` at `511/100`.
A 3-step exact cone is larger than `6^5` and was not enumerated. A
joint coupling of all six grandchildren against one shared boundary
could only lower `λ₂` (sum of maxes vs max of sums); it was not needed
at `499/100` and was not used to push past `5`.

## (4) What would finish it

A 3-step enumeration, or a block criterion whose row-sum stays below 1
through `p ≈ 11`; or a hybrid that feeds the exact 2-step kernels into
the averaged `W_ρ` machinery of a2.
