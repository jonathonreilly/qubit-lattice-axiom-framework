# static-law-in-the-hull, attempt 2 (worker w-macbookpro90c72-j67ba, model grok-4.6)

Independent of a1 (Hölder on `M^k`) and a3 (2×3/cube brute). Window: C4. Separator: `f=1_{\mathrm{all}+x}`.

## (1) The statement attempted

On C4, six-axis `(p,q,r)∈{(3,1,2),(5,2,4),(7,3,5)}`, the static law is **not** in the convex hull of sequential formation laws, including *adapted* (value-dependent) site-selection. Reason: `Z < D_σ` for all 24 permutations, so `μ_{\mathrm{static}}(\mathrm{all}+x)=p^4/Z > p^4/D_σ=μ_σ(\mathrm{all}+x)`. Any adapted scheme, restricted to the all-+x atom, induces some permutation (the values are constant, so the strategy's choices are a fixed order), hence `μ_{\mathrm{adapted}}(\mathrm{all}+x)` is a mixture of `{μ_σ}` and still strictly below static. Path-of-3 (a tree) has `Z=D`.

## (2) Steps

**Step 1 — `D_σ=∏ N_{k_i}` (PROVED).** `N_k=p^k+q^k+4r^k`, `N_0=6`. Sequential all-+x mass is `p^{|E|}/D_σ`.

**Step 2 — C4 census (CHECKED).** 24 orders, three weights, `Z<D_{\min}` with positive integer margins 1680, 15096, 42432.

**Step 3 — adapted schemes (PROVED).** On the all-+x configuration every recorded neighbourhood is all +x, so an adapted rule is a deterministic function of the *set* of remaining sites only, i.e. a permutation. Hull of adapted laws, projected on this coordinate, lies in `[min_σ μ_σ, max_σ μ_σ]`, below `μ_{\mathrm{static}}`.

**Step 4 — tree (CHECKED as E3).** Path-of-3: `Z=864=D`.

## (3) First failing step, if any

Not a theorem for every weight (only three rationals on C4). Hölder for all `(p,q,r)` is a1's claim, not re-proved.

## (4) What would finish it

The same separator on the cube; a Hölder proof that `Z<D_σ` for every cyclic window and every `p>q,r>0`.
