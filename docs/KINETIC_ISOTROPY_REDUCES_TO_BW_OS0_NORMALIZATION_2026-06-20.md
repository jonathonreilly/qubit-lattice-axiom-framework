# Kinetic Isotropy Reduces to the Berezin–Wick/OS0 Normalization r = 1 (and B4/S4-Transitivity Routes Are Circular as a Class)

> **Key terms used in this doc** are indexed A–Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-20
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.

**Primary runner:**
[`scripts/kinetic_isotropy_reduces_to_bw_os0_normalization_2026_06_20.py`](../scripts/kinetic_isotropy_reduces_to_bw_os0_normalization_2026_06_20.py)
**Cached runner output:**
[`logs/runner-cache/kinetic_isotropy_reduces_to_bw_os0_normalization_2026_06_20.txt`](../logs/runner-cache/kinetic_isotropy_reduces_to_bw_os0_normalization_2026_06_20.txt)

## What this is (a reduction, not a derivation)

The registered primitive **`kinetic_isotropy`**
([`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md))
asserts the emergent four-axis kinetic form is hypercubically isotropic,
`c_t = c_s` — equivalently the Euclidean regulator block `Z^3 x Z_tau` is
`B4`-symmetric (the Osterwalder–Schrader OS0 normalization, *"one tick is one
edge in form, not only in spacing"*). It is the time-direction analogue of the
`LATTICE` axiom's spatial cubic adjacency `a_x = a_y = a_z`.

This note does **not** derive `c_t = c_s`. It certifies three exact structural
facts that together **shrink the primitive's content** from a monolithic
graining choice to a **single metric-layer normalization residual** `r = c_t/c_s
= 1`, and it proves that the most natural-looking derivation strategy — "the four
Euclidean axes are `B4`/`S4`-equivalent, so the kinetic form must be
`B4`-invariant" — is **circular as a class**. The residual `r = 1` survives and
is left to a separate attack (see *Honest boundary*).

This complements the protection result
[`ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md`](ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md),
which shows that **given** the `B4`-symmetric surface, the marginal Lorentz
violation `c_s != c_t` is forbidden to all perturbative orders. That theorem
*consumes* the surface this note isolates: the present note pins exactly what
remains to be supplied for that protection to stand on the three axioms alone.

## The three certified facts

Let a diagonal quadratic kinetic form be `Q(p) = sum_mu c_mu p_mu^2`, metric
`G = diag(c_t, c_s, c_s, c_s)` on axes `(t, x, y, z)`.

**(C1) The invariant-dimension wall.** On the space of diagonal quadratic forms
(and on the full 10-dimensional space of symmetric `4x4` matrices), the spatial
cubic group `O_h` (signed permutations of the three spatial axes, time fixed;
`|O_h| = 48`) leaves a **two-dimensional** invariant space — `c_t` and `c_s`
independent, spanned by `diag(1,0,0,0)` and `diag(0,1,1,1)`. Only the full
hypercubic group `B4` (signed permutations of all four axes; `|B4| = 384`)
collapses it to **one** dimension, `c_t = c_s`. (Exact Reynolds-projector rank
over `Q`.) `O_h` is exactly the symmetry the `LATTICE` axiom supplies; the
collapse to isotropy needs precisely the generator `O_h` lacks — the
**time–space axis exchange**.

**(C2) The circularity certificate.** That missing generator is the time–space
swap `W` (e.g. `t <-> x`). A purely spatial swap is a symmetry of `G` for **all**
`(c_t, c_s)` (so `O_h` is automatic), but
```
        W^T G W - G = diag(c_s - c_t, c_t - c_s, 0, 0),
```
which vanishes **iff `c_t = c_s`** (exact sympy). Therefore the premise *"the
four axes are `B4`/`S4`-equivalent"* (i.e. `W` is a metric symmetry) is
**logically identical to the conclusion** `c_t = c_s`, not antecedent to it. Any
route that forces isotropy by invoking four-axis equivalence / `S4`-transitivity
**assumes the conclusion** — it is circular as a class. (An axis-relabel
certificate that transports a *label* among four axes already equal by
construction does not derive the equal footing.)

**(C3) Layer-independence of the residual.** On a **geometrically square**
lattice (`a = 1` on all four axes) the anisotropic free Euclidean scalar with
`c_t != c_s` has one-step transfer eigenvalue `lambda(k) in (0,1)` for every
spatial mode, so its time two-point function is a positive exponential and the
OS reflection Gram matrix is PSD — **reflection positivity / positive transfer
holds across the entire `c_t/c_s` family** and does not select isotropy, even
though the anisotropy is genuinely Lorentz-violating (front-speed^2 `= c_s/c_t
!= 1`). Hence the residual `r = c_t/c_s` is **independent** of the geometric,
causal-cone and reflection-positivity layers; it is purely the kinetic-form
normalization.

## The reduction (layer ladder)

`kinetic_isotropy` is not monolithic. It factors into:

| Layer | Content | Status |
|-------|---------|--------|
| L0 | one-parameter tick generator exists (`U = exp(-i t H_gen)`) | retained-derived (`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10`) |
| L1 | arrow / time **direction** | already-admitted (`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05`) |
| L2 | causal cone, "one tick = one edge in **count**" | candidate-derived (minimum-time-step) |
| L3 | real-time carrier saturation `|v| = 1` | candidate-derived (strict-license chiral winding; integer quantization, not tuning) |
| **R** | **the Berezin–Wick/OS0 normalization `r = c_t/c_s = 1`** ("one tick = one edge in **form**") | **the lone surviving metric-layer residual** |

Net: from one monolithic primitive to **one** metric-normalization bridge, with
the direction layer already admitted and the others derived or candidate-derived.

## Honest boundary

- This is a **reduction, not a derivation**. `r = 1` is **not** derived here; by
  C1–C2 it cannot be sourced from `{LATTICE, QUANTUM, RECORD}` together with the
  single-clock, reflection positivity/OS, scale, six-nearest-neighbor
  reachability, strictness, unitarity, or winding structures without circularity,
  because the `O_h -> B4` extension generator is itself equivalent to `c_t = c_s`.
- **The residual must NOT be reduced to the past-hypothesis / registration-
  direction admission.** That admission is the *order* layer (L1); collapsing the
  *metric* residual `r` into it would re-cross the order/metric boundary and
  re-commit exactly the circularity of C2. The only legitimate reduction target
  for `r` is the metric-layer clock-rate/normalization family
  (`POST_RECORD_CLOCK_RATE_INTERFACE`, tick/edge-spacing companion); the
  Stone scope-boundary shows even that family relabels rather than removes (`tau`
  fixes only the product `tau * H`).
- This note does **not** lock the promotion path. The open, non-circular seam —
  untouched by all of the structures above — is whether the canonical OS / Wick
  analytic continuation of a **single emergent record tick** fixes `r = 1`
  uniquely. That is a separate target; if a later retained derivation supplies
  `r = 1`, the `kinetic_isotropy` primitive is retired and the all-orders `B4`
  protection above stands on the three axioms alone.
- No new axioms, imports, or comparators are introduced. The note uses only
  existing registered structure plus exact finite group theory and a
  finite-dimensional positivity witness.

## Inputs

- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — the primitive being reduced
- [`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md) — the `O_h` 2-dim / `B4` 1-dim gate
- [`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md) — L0
- [`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md) — L1
- [`ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md`](ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md) — consumes this surface

## Reproduce

```
python3 scripts/kinetic_isotropy_reduces_to_bw_os0_normalization_2026_06_20.py
# expect: TOTAL: PASS=16 FAIL=0
```
