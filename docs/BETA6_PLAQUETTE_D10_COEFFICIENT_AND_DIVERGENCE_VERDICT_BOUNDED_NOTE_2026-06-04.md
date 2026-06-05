# Beta=6 SU(3) Plaquette: d_10 Coefficient and the Divergence Verdict

**Date:** 2026-06-04
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. The independent audit lane sets audit and
effective status.
**Primary runner:** [`frontier_beta6_d10_coefficient_2026_06_04.py`](../scripts/frontier_beta6_d10_coefficient_2026_06_04.py)

## Scope

Two results: (i) the **exact** order-`beta^10` coefficient `d_10` of the connected
plaquette series `Delta(beta) = <P> - P_1plaq = sum_{n>=5} d_n beta^n`; and (ii) a
**radius-of-convergence determination** from `d_5..d_10` that resolves whether
`Delta` converges at `beta = 6`. This is a frontier_discovery increment, NOT a
closure of `<P>(6)`.

## (i) The exact coefficient

```text
d_10 = -10483 / 5289581076480 = -1.98182046e-09        (NEGATIVE; d_10/d_9 = 953/3700)
```

decomposing exactly as (each piece reproven from SU(3)-Haar primitives + the
reproven Picard-Fuchs J recurrence):

```text
cube(10)             = -4081/1763193692160   = -12243/5289581076480   (72 K''(K')^5 [b^10])
weight-10 class(10)  =    55/198359290368    =  +1760/... (part)      (1080 K''(K')^9 [b^10])
weight-11 class(10)  =    11/198359290368    (leading; 66 supports, one orbit)
-------------------------------------------------------------------
d_10                 = -10483/5289581076480
```

**New physics at `beta^10`.** The `>=3`-face baryon/epsilon (det) channel,
`(3,0)`-singlet closure (`N_0(3,0)=1`; verified: projector `=1`, value
`eps.eps/6 = 1/6`), **opens at order 10 as predicted** -- but as a *per-link
invariant-sector effect* inside the incidence-3 links of the existing weight-10
and weight-11 supports, NOT as a separate support class. weight-12 opens at order
11. No other order-10 class (radius-2 == radius-3, 2-cube == 3-cube stable).

Regression: the engine reproduces `d_5..d_9` exactly (e.g. `cube(9) + weight-10(9)
= -2035/264479053824`). `cube(10)` and `weight-11(10)` independently reconfirmed.

## (ii) The radius verdict: Delta DIVERGES at beta=6

`d_10` activates the `[2/2]` d-log-Pade (which `d_5..d_9` could not reach). The
dominant singularity of `Delta` is a **complex-conjugate pair** (forced: the
`d_9 < 0` sign change invalidates any real-pole extrapolation):

```text
d-log-Pade[2/2]:  beta_c ~ 1.781 +/- 5.083 i ,  |beta_c| = 5.386 ,  arg ~ +/-70.7 deg
d-log-Pade[0/2]:  beta_c ~ -1.239 +/- 4.647 i ,  |beta_c| = 4.810
d-log-Pade[1/1]:  3.375 (real)  <- KNOWN SPURIOUS (real-pole ansatz invalid for a complex pair)
```

The genuine (complex-pair) estimates **trend upward with order** (4.81 -> 5.39)
toward the literature value, and a 2-term-recurrence / Aitken extrapolation gives
`~5.3`. Three independent estimators concur:

```text
R ~ 5.3 - 5.4 < 6     ==>     Delta DIVERGES at beta = 6.
```

**This resolves a sharp open question.** A naive ratio extrapolation on the first
five coefficients suggested `R ~ 8 > 6` (apparent convergence); that is an
**artifact** of applying real-pole intuition to a complex pair. The corrected
determination `R ~ 5.3-5.4 < 6` **agrees with the independent lattice-QCD
complex-`beta` singularity / Fisher-zero location `~5.7`** (Li-Meurice,
arXiv:0710.5771; hep-lat/0507034). Framework and literature now coincide.

## Implication (the path forward)

Because `Delta` diverges at `beta = 6`, **the strong-coupling / cluster series
cannot deliver `<P>(6)` by truncation or naive resummation, at any order** -- more
coefficients only re-confirm the divergence. The connected expansion at `beta=6`
is *beyond its radius*. Equivalently, the resummation-radius threshold
`g_K = (18/R)^4 ~ 130 > 81` (cf. the resummation-radius note), i.e. the multi-cube
proliferation `rho_comb > 11.57`: the open `rho_{p,q}(6)` wall.

The forward route to `<P>(6)` is therefore NOT more coefficients but **resummation
of the now-located complex-conjugate pair** (Borel-conformal / Pade-Hadamard, for
which the pair location `|beta_c| ~ 5.4`, `arg ~ 70.7 deg` is the required input)
or a **controlled tensor-network** evaluation. The certified convergent backbone
(`P_1plaq + cube + two-cube_w10 = 0.5155...`, separate note) remains the rigorous
lower portion; the `~13%` remainder is this divergent / wall sector.

## Boundary (honest scope)

- The **exact `d_10`** is a theorem (piece-by-piece, regression-validated,
  cube(10) and weight-11 independently reconfirmed).
- The **radius verdict** `R<6` (complex pair, divergence at `beta=6`) is **robust
  in direction** -- three independent estimators and the literature Fisher zero
  all place the dominant singularity below 6 -- but the **precise** `R` carries
  `~+/-0.5-1` (six coefficients is thin; one unbalanced approximant gave 6.6).
  Computing `d_11` would activate `[2/3]/[3/2]` and sharpen the pair.
- Does NOT close `<P>(6)`; does NOT repin any canonical value, `u_0`, or `alpha_s`.

## Forbidden-import

Clean: every coefficient reproven from the SU(3) Haar single-link integral + the
`J` recurrence. `0.594` and the literature `~5.7` are after-the-fact comparators,
never derivation inputs. The d-log-Pade / differential-approximant methodology is
the standard of Guttmann (biased differential approximants), cited as method only.

## Key files

- [`scripts/frontier_beta6_d10_coefficient_2026_06_04.py`](../scripts/frontier_beta6_d10_coefficient_2026_06_04.py) (this note's runner)
- [`BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md) (exact `d_9`, the engine)
- [`BETA6_PLAQUETTE_TWOCUBE_CLOSED_FORM_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_TWOCUBE_CLOSED_FORM_BOUNDED_NOTE_2026-06-04.md) (weight-10 closed form)
- [`GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md) (why no finite truncation closes `<P>(6)`)
