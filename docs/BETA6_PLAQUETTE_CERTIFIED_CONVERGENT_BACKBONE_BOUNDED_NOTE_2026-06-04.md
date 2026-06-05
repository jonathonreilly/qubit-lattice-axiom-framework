# Beta=6 SU(3) Plaquette: Certified Convergent Backbone Enclosure

**Date:** 2026-06-04
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. This note writes no audit verdict and supplies no
direct effective-status change.
**Primary runner:** [`frontier_beta6_certified_backbone_2026_06_04.py`](../scripts/frontier_beta6_certified_backbone_2026_06_04.py)

## Scope

This note supplies a **certified (interval/ball-arithmetic) rigorous enclosure**,
at `beta = 6`, of the *convergent backbone* of the SU(3) Wilson plaquette
expectation:

```text
<P>(6)  =  P_1plaq(6)  +  Delta_cube(6)  +  Delta_2cube^(w10)(6)  +  [non-cube remainder]
          \________________________ backbone ________________________/   \____ open wall ____/
```

The three backbone sectors are **convergent at beta=6** (the nearest zero of `J`
is at `|b| ~ 8.205 > 6`), so each is a well-defined number; this note certifies
their sum to ~45 digits. It does **not** close `<P>(6)` (the non-cube remainder is
the open `rho_{p,q}(6)` wall).

## The rigorous coefficient bound (the certification rests on this)

The single-plaquette generating function is the SU(3) Haar integral

```text
J(b) = int_{SU(3)} exp((b/3) Re Tr U) dU = sum_{n>=0} a_n b^n ,
a_n = (1/n!) E[((1/3) Re Tr U)^n] .
```

Because `Re Tr U in [-3/2, 3]` on SU(3), we have `|(1/3) Re Tr U| <= 1`, hence the
**closed-form, rigorous bound on every Taylor coefficient**

```text
|a_n| <= 1/n!                                                        (*)
```

`(*)` is verified in-runner for all `n < 70` against the exact `a_n`. It yields a
rigorous exponential tail bound, `|sum_{n>N} a_n b^n| <= sum_{n>N} b^n/n!` (a tail
of `e^b`), and likewise for `J'` and `J''`. `J` is entire of order 1, so the
series converges for all `b`.

## Method (reprove-and-cite)

- `a_n` computed **exactly** (rationals) from the reproven order-3 Picard-Fuchs
  recurrence `6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2}`,
  seed `a_0=1, a_1=0, a_2=1/36` (the seed matches the Haar moments: `J(0)=1`,
  `E[Re Tr U]=0`, `a_2=1/36`).
- Partial sums `S, S', S''` are exact; tails bounded rigorously by `(*)`.
- `J(6), J'(6), J''(6)` formed as rigorous intervals (mpmath.iv); **`J(6)` is
  certified strictly positive**, so `K = log J` and the divisions below are safe.
- `K' = J'/J`, `K'' = J''/J - (J'/J)^2` by interval arithmetic.
- `Delta_cube  = 72 * K'' * (K')^5`  (cube-sector closed form; reproduces `d_5..d_8`).
- `Delta_2cube^(w10) = 1080 * K'' * (K')^9`  (leading two-cube weight-10 closed
  form; see the two-cube note).

The certified-holonomic-evaluation methodology is the standard of Mezzarobba,
*Rigorous Multiple-Precision Evaluation of D-Finite Functions in SageMath*
(arXiv:1607.01967); here it is realized directly through the closed-form
coefficient bound `(*)` plus interval arithmetic, cited as method/comparator only.

## Result (certified)

```text
P_1plaq(6)         = 0.422531739649983468165680828...   (half-width 8.1e-47)
Delta_cube(6)      = 0.062913415328266145319501722...   (half-width 1.0e-45)
Delta_2cube^(w10)(6)= 0.030079587213370843633018082...  (half-width 5.1e-46)
------------------------------------------------------------------------
BACKBONE(6)        = 0.515524742191620457118200632...   (half-width 1.6e-45)
```

Runner self-check: **PASS=9, FAIL=0.** The certified backbone accounts for
`>= 86.876%` of the `0.5934` Monte-Carlo comparator; the remaining `~13.12%`
(`~+0.078`) is the open non-cube `rho_{p,q}(6)` sector.

## Significance

This **upgrades the convergent core of `<P>(6)` from a Monte-Carlo comparator to a
certified rigorous value** (rigorous to ~45 digits), for the `P_1plaq + full-cube
+ leading-two-cube` sectors. It is a bounded support surface for the
plaquette value.

## Boundary (what this does and does NOT establish)

- It certifies the three named convergent sectors **only**. It is a rigorous
  **lower bound** on `<P>(6)` *iff* the remaining non-cube cluster sectors are net
  non-negative (the `d_9` and weight-10 non-cube contributions are positive, but
  the full remainder's sign is **not** proven here).
- It does **not** close `<P>(6)`. The `~+0.078` remainder is the doubly-walled
  `rho_{p,q}(6)` object (algebraic underdetermination + treewidth-29
  infeasibility); the infinite-hierarchy obstruction stands.
- Convergence of the full multi-cube cluster expansion at `beta=6` reduces to the
  resummation-radius threshold `g_K < 81` (i.e. `R > 6`); the five exact
  coefficients `d_5..d_9` estimate `R ~ 8 > 6` (tentatively convergent), but this
  is undecided against the literature complex-singularity location `~5.7`.
- It does **not** repin any canonical plaquette value, `u_0`, or `alpha_s`.

## Forbidden-import

Clean: every number is reproven from the SU(3) Haar single-link integral plus the
`J` recurrence (Haar primitives). `0.5934` is an after-the-fact Monte-Carlo
comparator, never a derivation input.

## Key files

- [`scripts/frontier_beta6_certified_backbone_2026_06_04.py`](../scripts/frontier_beta6_certified_backbone_2026_06_04.py) (this note's runner)
- [`BETA6_PLAQUETTE_TWOCUBE_CLOSED_FORM_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_TWOCUBE_CLOSED_FORM_BOUNDED_NOTE_2026-06-04.md) (the two-cube weight-10 closed form)
- [`BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md) (exact `d_9`, the engine)
- [`GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md) (why no finite truncation closes `<P>(6)`)
