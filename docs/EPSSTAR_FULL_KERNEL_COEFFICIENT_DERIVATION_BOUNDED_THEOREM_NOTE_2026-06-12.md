# eps* Full-Kernel Coefficient: the Divided-Difference Kernel's T-Dependence Flips the Naive Sign (Bounded Finite-Cell Note, 2026-06-12)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note sets source
claim metadata only; it does not set, predict, or edit any audit outcome.
**Primary runner:** [`scripts/frontier_epsstar_full_kernel_coefficient_2026_06_12.py`](../scripts/frontier_epsstar_full_kernel_coefficient_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/frontier_epsstar_full_kernel_coefficient_2026_06_12.txt`](../logs/runner-cache/frontier_epsstar_full_kernel_coefficient_2026_06_12.txt)
**No-promotion statement:** This source note creates no promotion, no registry
edit, no audit verdict, and no downstream status change; status remains owned
by the independent audit lane.

## Claim

On the one-particle, finite Harper/PT surface with `Q=24`, `Ly=2`,
`GL=20`, and the fixed branch bracket `[1.2, 2.4]`, the m=0 boundary
root obeys

```text
chi(mu*(T), T) = 0
```

and the coefficient of `mu*(T)^2` in `T^2` is reproduced only after the
finite-temperature divided-difference kernel is retained.  The diagonal
Sommerfeld/seagull proxy remains the internally recomputed precursor negative:

```text
alpha_seagull = -9.266358431847
```

Keeping the complete finite-T kernel gives

```text
alpha_kernel = +13.408176855550
alpha_full   =  +4.141818423703
```

against the internally recomputed finite-root comparator

```text
d_measured = +3.877078419950
relative mismatch = 6.83%
```

with the frozen runner tolerance `15%`.

## What is and is not the result

The load-bearing finding is the **sign-flip mechanism**, not an independent
re-derivation of the magnitude. The naive (occupation-smearing) Sommerfeld
coefficient of the precursor route keeps only the seagull/contact piece and gives
`alpha_seagull = -9.27` — the wrong sign. Decomposing the full coefficient
`alpha_full = alpha_seagull + alpha_kernel` shows the divided-difference
kernel's explicit finite-`T` dependence contributes `alpha_kernel = +13.41`,
which **flips the sign** and is larger in magnitude than the seagull term. This
is the precise localization left by the precursor route: the `T^2` growth of
the boundary is governed by the kernel's `T`-dependence, which the naive proxy
drops. No closed PR is a load-bearing authority for this note; the runner
recomputes the T=0 branch anchor, seagull coefficient, and finite-root slope
internally.

The agreement `alpha_full ≈ d_measured` (6.83%) is a **consistency
cross-check**, not an independent second derivation of the slope: `alpha_full`
is computed as `-2 mu0 (dchi/dT^2)/(dchi/dmu)`, i.e. the implicit-function-theorem
prediction of `d(mu*^2)/d(T^2)` from `chi`'s partials at the fixed point, while
`d_measured` is the direct fit of the root locus `mu*^2(T)`. The two routes must
agree by the IFT up to discretization; their agreement validates the numerics
and confirms no sign/scale blunder, but the physics content is the decomposition.

**Limitation (disclosed):** `dchi/dT^2` is estimated at a single fixed surface
scale `T = eta = 0.05` (one-point `chi(mu0,eta)/eta^2`), not Richardson-
extrapolated; the 6.83% gap is consistent with that `O(eta^2)` truncation plus
the finite-difference of `dchi/dmu`. Tightening the estimate is a named follow-on.

## Method

The runner uses the same finite two-band Harper/PT machinery:

- `Q=24`, `Ly=2`, `N=48`, `GL=20`;
- `chi_PT = seagull + divided-difference kernel`;
- `K(E_i,E_j;T) = (f_i - f_j)/(E_i - E_j)` with the fixed degenerate
  limit `f'(E)`;
- branch bracket `[1.2, 2.4]`.

The T=0 anchor is the same finite surface proxy recomputed from the precursor
route: Gaussian surface width `eta=0.05`, branch window
`[1.48, 1.56]`.  It gives

```text
mu0 = 1.515550712171
alpha_seagull = -9.266358431847
```

The full-kernel coefficient is computed by a separate route from the
finite-root fit: after anchoring the T=0 response to zero at `mu0`, the
runner evaluates the complete finite-T PT integrand once at the fixed
surface scale `T=eta=0.05` and divides by `T^2`.  This retains the
near-degenerate finite-T divided-difference behavior of the actual kernel
instead of replacing the kernel by its T=0 occupation-smearing proxy.

## Gates

The runner freezes these checks:

- T=0 branch root stays in the internally recomputed `mu*_0 ~= 1.5216` region.
- Naive seagull alpha stays in the internally recomputed `-9.27` region.
- Interband `|H1|` weight at the root is nonzero/nontrivial.
- The finite-root branch reproduces internally recomputed `d ~= +3.88`.
- `alpha_full` and `d_measured` are both positive.
- `alpha_full` matches `d_measured` within `15%`.
- `alpha_seagull < 0`, `alpha_kernel > 0`, and
  `|alpha_kernel| > |alpha_seagull|`.

Smoke output:

```text
TOTAL: PASS=7 FAIL=0
```

## Scope

This is a bounded finite-cell statement on the m=0 axis.  It does not
promote the full `(m,T)` surface, and it does not claim a continuum theorem.
Memory: one-particle only.

The audit lane grades.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  (the current axiom surface; scope reference only).
