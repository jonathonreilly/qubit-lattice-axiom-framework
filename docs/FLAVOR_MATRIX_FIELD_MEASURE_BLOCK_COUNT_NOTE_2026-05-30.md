# Flavor — the covariant matrix-field measure ranks block-count (Q=2/3) over dimension (Q=1)

**Date:** 2026-05-30
**Claim type:** bridge-gap attack move 3 / native measure tie-breaker (a LEAN
toward the value, NOT a forcing). Imports nothing.
**Runner:** `scripts/flavor_matrix_field_measure_block_count_2026_05_30.py` (+ cache).

> ⚠️ **CORRECTED by `FLAVOR_TWO_PATHS_VERDICT_NOTE_2026-05-30`.** This note's
> "covariant `Tr(M²)` measure → block-count → 2/3" used **real `b`** (one doublet
> dof). The full Hermitian operator has **complex `b`** = two doublet dof
> (`Re b, Im b`); the same trace measure then gives `E[‖doublet‖²]:E[‖singlet‖²]
> = 2:1` = **dimension → Q=1** (median 1.34). So the "block-count over dimension"
> ranking is **inverted** for the full operator — A1's trace actually votes
> dimension/Q=1, and block-count needs the `Im b=0` import. Retract the "lean
> toward 2/3" reading.
Resolves (partially) the move-2 3-way measure fork
(`FLAVOR_BA_RATIO_BOUND_HS_EQUIPARTITION_NOTE_2026-05-30`).

## The question
Move 2 reduced the value gate to: *which measure does the matter sector place on
the S₃-invariant operator space `span{I, J−I}`?* — HS/block-count → Q=2/3,
dimension/Plancherel → Q=1, fermion dynamics → Q=1/3. The campaign's long-standing
verdict was **"rep theory ranks neither block-count nor dimension."** This move
finds a native tie-breaker.

## The result — the standard matrix-field action gives block-count
The **standard covariant matrix-field action** `S = Tr(M²)` — the unique
unitarily-invariant quadratic, native to A1's operator algebra (`Cl(3)=M₂(ℂ)` has
a **unique tracial state** = the trace) — realizes the **block-count** measure,
not the dimension measure. Under `e^{−Tr(M²)/2}` on `M = aI + b(J−I)` (verified
analytically and by Monte Carlo, N=4×10⁵):
```
⟨singlet isotype weight⟩ = ⟨λ₀²⟩    = 1
⟨doublet isotype weight⟩ = ⟨2λ₁²⟩   = 1      (EQUAL)
```
Equal expected C₃-isotype weights **is** the block-count condition ⟺ `r=1/2` ⟺
**Q=2/3**.

**Why the dimension factor cancels:** the doublet has dim 2 (two states), *but*
the doublet operator `(J−I)` has 2× the HS-stiffness (`Tr((J−I)²)/Tr(I²)=6/3=2`),
so each doublet state fluctuates at **half** variance (1/2); `2 × ½ = 1` = the
singlet weight. The covariant matrix-field measure weights the two C₃ isotypes
**equally** — block-count, Q=2/3 — whereas the non-covariant flat-in-coefficients
measure gives the dimension answer Q=1.

So the framework's **matrix-field structure breaks the "rep theory ranks neither"
tie — toward Q=2/3** — because the natural covariant action on a matrix-valued
mass field is the block-count measure. This is the first native argument that
*ranks* the two canonical measures.

## Honest caveats — this is a LEAN, not a forcing
1. **Expectation, not per-operator.** `⟨W_singlet⟩=⟨W_doublet⟩` means the measure's
   *expected* weights satisfy the Q=2/3 condition; a specific operator's weights
   fluctuate, so its Q ≠ 2/3 exactly. The covariant measure realizes block-count
   *on average*.
2. **Bare, not dynamical.** This is the free `Tr(M²)` measure. The fermion
   **dynamics** (this session, 3 computations) modifies it and drives `b→0`
   (Q=1/3). The lean is kinematic; whether the dynamics preserves or overrides it
   is the open piece.
3. **Background mean.** A nonzero diagonal mean (bulk mass `a`) is not modeled by
   the zero-mean Gaussian; with a strong background, `r=b²/a²` is small (→ Q=1/3).

## Status / where this leaves the frontier
A genuine, import-free **native lean toward the observed Q=2/3**: the covariant
matrix-field action selects block-count over dimension, removing the Q=1 branch on
*field-theory* (not rep-theory) grounds. The campaign's "two equally canonical
measures" is broken by the framework having an actual **matrix field**.

The frontier is now one sharp, decidable question:
> **Does the `g_bare=1` matter dynamics preserve the covariant block-count
> `Tr(M²)` measure (→ Q=2/3) or collapse it (→ Q=1/3)?**

i.e. does the fermion loop renormalize the corner-coupling stiffness away from the
bare HS value? That is the move-2 tension, now sharpened to a concrete
renormalization question on the corner cube. No false closure; `Q=2/3` is a native
*lean*, not yet derived — but the dimension/Q=1 alternative is now disfavored on
covariance grounds, and the observed value sits exactly at the covariant
block-count point.
