# Flavor — both paths fail; A1's trace votes Q=1 (correcting the "native 2/3 lean")

**Date:** 2026-05-30
**Claim type:** two-paths verdict + rigorous self-correction. Imports nothing.
**Runner:** `scripts/flavor_two_paths_verdict_2026_05_30.py` (+ cache).
**Source:** parallel two-track press (`wf_33a8ac1e`, 0 native forcings survived).

## The two paths, and the verdict: NEITHER forces native 2/3 — and Track 1 inverts.

### Track 1 — A1's trace forces DIMENSION (Q=1), not block-count (2/3)
The C₃-symmetric Hermitian mass operator is `M = aI + bC + b̄C²` with **`b`
complex** (`a` real). The doublet isotype = `(Re b, Im b)` = **two** real dof; the
singlet = `a` = one. `Tr(M²)=3a²+6|b|²`, and the canonical trace-induced
(HS-isotropic) Gaussian gives, by Schur, `E[‖proj onto k-dim block‖²]=k` →
**doublet:singlet = 2:1 = dimension → Q=1** (verified: isotype HS-weight ratio
2.00; median Q=1.34). Block-count (1:1 → Q=2/3) is recovered **only** by setting
`Im b=0` (collapsing the doublet to one real coordinate) — a real-structure
**import** beyond the trace.

**⚠️ This corrects this session's moves 3 / "B" / exactness-closure.** Those
computed the covariant measure with **real `b`** implicitly and got median 2/3.
With the **full complex-`b`** operator — the physical case, since `θ=arg(b)≠0` is
exactly what splits `e,μ,τ` into 3 distinct masses — the *same* covariant trace
measure gives **median Q=1.34**. So **"the native covariant measure ranks toward
2/3" was an artifact of the real-`b` restriction**; A1's canonical full-operator
measure ranks toward **Q=1**.

### Track 2 — a concentrating saddle at b/a=1/√2 exists, but is block-weight-conditional
The 2-sector Shannon entropy of `{3a², 6b²}` stationarizes at `b/a=√2/2` with
`S″<0` (a genuine per-operator maximum, not a median). **But its location rides on
the same block weighting**: the general weighted-log saddle is `r*=ν/(2μ)`, and
`r=1/2 ⟺ ν=μ =` equal **block** weight — the Track-1 open choice. Every block-saddle
functional has a dimension-reading twin landing at `r=1` (Q=1). The only
**unconstrained** native saddle is `b=0` (uniform condensate, Q=1/3). Placing a
minimum *at* `r=1/2` unconditionally requires `F=(r−1/2)²` — reverse-engineered.

## Corrected state of the whole value question
| measure / dynamics | Q |
|---|---|
| A1 canonical full-operator covariant measure (complex b) | **median ~1.34 (dimension → Q=1)** |
| unconstrained native dynamics (condensate saddle) | **1/3** (uniform b=0) |
| block-count (Im b=0 / doublet-phase-not-a-dof) | 2/3 — but an **import**, in tension with θ≠0 |
| chiral constraint `{M,Γ_χ}=0` | exact **2/3** — retained import (non-native Γ_χ) |
| **data** | **2/3** (0.91σ) |

Both tracks reduce to the **same single d.o.f.**: does the doublet's second real
coordinate (`Im b` = the phase `θ`) count as a measure dof? **A1's full operator
says yes → (1,2) → Q=1; block-count needs no → (1,1) → Q=2/3.** Neither makes (1,1)
forced — and A1 actually votes **(1,2)**.

## Honest verdict (the value question, corrected)
The charged-lepton `Q=2/3` is **not natively favored**: A1's canonical measure
gives `Q=1`, the dynamics give `Q=1/3`, and the observed `2/3` (which the data
requires at 0.91σ) sits between them and needs an **import** — the chiral grading
`{M,Γ_χ}=0` (exact 2/3), or the block-count / `Im b=0` restriction (median 2/3,
in tension with the physical 3-distinct spectrum). The session's "native lean
toward 2/3" (moves 3/B/exactness-closure) is **retracted** — it used real `b`.

## Next paths (not a closure)
1. **Is the `Im b=0` (real-`b`) restriction itself native?** Move 1 showed the
   native cube-shift coupling *is* real (`J−I`); the phase `θ` is the separate
   chiral import. So the (1,1) block-count = "the native coupling is real, the
   phase is imported." But the physical 3-distinct spectrum *needs* `θ≠0`. The
   sharp question: is the *Q-relevant magnitude* `|b|` set by the real native part
   alone (→ 2/3) while `θ` is a Q-orthogonal import? That would reconcile (1,1)
   with `θ≠0` — worth a focused computation.
2. Accept the honest map: `Q=2/3` needs the one chiral import; the data requires
   it; A1 alone gives Q=1, dynamics give Q=1/3.

No false closure. The correction is logged; the value question's honest state is
that `2/3` is import-dependent, with the single sharp open question (1) above.
