# formation-clauses-in-level-time, attempt 1 (worker w-macbookpro90c72-je0c4, model grok-4.6)

Independent of a2/a3 (same-family priors used full-cube TV). Route: the sequential all-aligned mass is a function of the *k-sequence* only; compare clauses by that observable and by k-histograms.

## (1) The statement attempted

Six-axis product rule, records-only sequential formation `r(s | recorded neighbours)`, joint/static law of a window, uniform-clock mixture over orders, NEC kernels of block 12.

**Statement.** For any sequential order `σ` on a window, if `k_i` is the number of already-recorded neighbours of the `i`-th site, then
\[
\mathbb{P}_\sigma(\text{all }+x)=\prod_i \frac{p^{k_i}}{p^{k_i}+q^{k_i}+4r^{k_i}}\qquad(k_i=0:\;1/6).
\]
On the `2×2×2` cube at `(p,q,r)=(3,1,2)`:
- monotone/corner/reverse-level orders share the k-multiset `(0,1^3,2^3,3)` and the mass `2187/44994560`;
- opposite-corners-first has a different multiset and mass `81/2048000`;
- joint/static mass is `59049/775835648` (enumerated `Z` over `6^8`);
- uniform clocks (exact average over `8!` orders) give `338229/7997080000`.

These four are pairwise distinct. The k=1 and k=3 factors are the copy and unanimous NEC kernels. A level of `Z^3` is an independent set, so joint-of-a-level equals sequential-in-level. The unique recorded clause whose finished-window law does not depend on a sequential order is joint formation of the whole window. On the `3×3×2` slab, monotone k-hist `{0:1,1:5,2:8,3:4}` differs from centre-first `{0:2,1:3,2:9,3:4}`, and the all-+x masses differ.

## (2) Steps

**Step 1 — the product formula (PROVED).** Under records-only sequential formation, the all-+x configuration has every recorded neighbour equal to `+x`, so the one-site factor at a site with `k` recorded neighbours is `p^k/(p^k+q^k+4r^k)` (or `1/6` if `k=0`). The joint sequential probability is the product. CHECKED as E2, E3.

**Step 2 — cube k-sequences (CHECKED as E1).** Open `2×2×2`, 12 edges. Level-then-lex, reverse-level, and both corners have k-multiset `(0,1,1,1,2,2,2,3)`. Opposite-first `(0,7,…)` has `(0,0,1,1,1,3,3,3)`.

**Step 3 — four distinct cube masses at (3,1,2) (CHECKED as E3–E5).** Values above. Clocks mix eight k-multisets (`8!` enumerated). Joint `Z` by exact `6^8` sum.

**Step 4 — NEC is the k=3 sequential kernel (PROVED; CHECKED as E2).** Unanimous `ε_0=1-p^3/(p^3+q^3+4r^3)=11/20` at `(3,1,2)`. Majority on a 2:1 triple holds at `(3,1,2)` and fails at `(1,3,2)`. Copy-kernel is k=1. Seeded/clock orders put typical mass on k=1 (cube opposite-first has two k=0 and three k=3; clocks mix), so they do not reduce to NEC.

**Step 5 — level independent set (PROVED; CHECKED as E7).** Adjacent sites differ by 1 in `τ=x+y+z`. Joint formation of a level given the previous level is a product of 3-neighbour kernels, equal to any in-level sequential order.

**Step 6 — order-independence (PROVED from 1–3).** Sequential mass depends on the k-multiset, which changes as soon as the order is not a linear extension of the same ranked poset. Joint/static depends only on the graph and the rule. On any window containing a cycle, sequential ≠ joint (cube: the last vertex has k=3). Hence the unique order-independent recorded clause for a finished window is joint formation of that window.

**Step 7 — slab (CHECKED as E6).** `3×3×2` monotone vs centre-first: different k-histograms and different all-+x masses.

## (3) First failing step, if any

The route does not fail for the all-+x observable. It does not compute full-law TV (a2/a3 did), nor the six invariant measures on `Z^3`, nor a rate-clause continuous-time generator.

## (4) What would finish it

The same k-sequence calculus for two-site *units* (joint connected pairs); the jump-chain generator of block 14 compared to the uniform-order mixture; the leading `p→∞` ordering threshold under each k-histogram (majority vs copy).
