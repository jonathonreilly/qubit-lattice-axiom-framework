# Flavor — exactness closure: native measure CENTERS on 2/3; exact 2/3 = the chiral import

**Date:** 2026-05-30
**Claim type:** value-question closure / honest reduction (NOT a derivation of exact 2/3).
Imports nothing.
**Runner:** `scripts/flavor_exactness_closure_2026_05_30.py` (+ cache).
**Source:** 7-angle exactness press (`wf_53b417b9`, 0/7 native exact-forcings survived) +
independent verification.

> ⚠️ **CORRECTED by `FLAVOR_TWO_PATHS_VERDICT_NOTE_2026-05-30`.** The claim here that
> "the native covariant measure *centers* on 2/3" used **real `b`** (`Im b=0`)
> implicitly. With the **full complex-`b`** Hermitian operator (the physical case,
> `θ=arg(b)≠0` for 3 distinct masses), the *same* covariant trace measure gives the
> **dimension weighting → median Q≈1.34**, not 2/3. So A1's canonical full-operator
> measure votes **Q=1**, not 2/3; block-count/2/3 needs the `Im b=0` import. The
> "native median 2/3" reading below is retracted accordingly.

## The question and the answer
The observed charged-lepton operator sits at `Q=2/3` to ~1e-5. **What forces it
exactly?** Answer: **no native mechanism forces exact 2/3.** The native covariant
measure *centers* on 2/3 (median, ratio-of-expectations) but does **not** concentrate;
exact 2/3 is the chiral **constraint** (the import); and the data does **not** even
demand exactness (0.91σ).

## Three verified facts
**(1) The covariant matrix-field measure centers on 2/3 but does not concentrate.**
`e^{−Tr(M²)/2}` (with `Tr(M²)=λ₀²+2λ₁²`, correct doublet multiplicity) gives **median
`Q=0.667`** and equal expected block masses (`⟨λ₀²⟩=⟨2λ₁²⟩=1`). **But per-config `Q`
is Cauchy-broad** — only ~5% of configs land in `[0.6,0.7]`, and `P(|Q−2/3|<1e−2)≈1%`.
So 2/3 is the **median/center, not a concentration**: the measure does *not* force the
observed 1e-5 sharpness (which is measure-zero in the per-config distribution).

**(2) Exact 2/3 = the chiral constraint (the import).** Only the per-operator condition
`{M,Γ_χ}=0` (retained `koide_anticommuting_operator_derivation_theorem`) →
`⟨v|Γ_χ|v⟩=0` → `Q=2/3` exactly, θ-independent. `Γ_χ=(2/3)J−I` is the generation
grading: **non-native** (retained_bounded no-go `koide_z3_equivariant_anticommuting_no_go`),
the **same import** as the open generation-ID chirality gate.
*Correction:* the **eigenvector cone** condition `⟨v|Γ_χ|v⟩=0` (→ 2/3) is **not** the
operator-trace condition `Tr(M·Γ_χ)=0`, which gives `−a+4b=0 → b/a=1/4 → Q=0.375`. The
2/3 needs the cone condition, not the trace.

**(3) Data does not demand exactness.** `Q_obs=0.66666051`, `|Q−2/3|=6.16e−6 = 0.91σ`
(m_τ-limited). "`Q≈2/3`" (the measure median) fits within ~1σ.

## Verdict on the whole value question
- The native covariant measure **ranks / centers toward 2/3** — genuine and import-free,
  **modulo the doublet-multiplicity-2 (block-count) weighting**, which is the audit-open
  measure-normalization choice. And "`≈2/3`" is **all the data demands**.
- **Exact 2/3 reduces cleanly to the chiral import** (`{M,Γ_χ}=0`), which coincides with
  the generation-ID chirality gate.
- So the framework gets `Q≈2/3` **natively** (the median of its covariant measure);
  **exact** 2/3 needs the single chiral import — and the data only requires the former.

## Next paths (not a closure)
1. **Derive the doublet-multiplicity-2 (block-count) weighting** from the Cl(3) qubit
   measure / OS-reconstruction on the generation factor. If forced, the native
   2/3-ranking becomes a *consequence* (not a normalization choice), and **exactness
   becomes a non-question** (data only needs the rank). This is a measure-derivation
   problem, distinct from — and plausibly softer than — the chiral-grading import.
2. **A variational functional whose *saddle* (not expectation) sits at `b/a=1/√2`.** The
   only native saddle currently is `b=0` (Q=1/3); a functional whose minimum is the
   block-balanced point would force 2/3 without the chiral operator.

## Corrections logged
- Stale memory: `koide_signed_eigenvalue_vs_singular_value_readout` is **audited_failed**
  on main (a memory entry calling it a "28/28 PASS new theorem" is stale — not a valid
  source). Load-bearing retained crux confirmed: `koide_z3_equivariant_anticommuting_no_go`
  (retained_bounded) + `koide_anticommuting_operator_derivation_theorem` (retained) +
  `koide_circulant_q_two_thirds_algebraic_narrow_theorem` (retained).

No false closure. The charged-lepton value is now fully mapped: native median 2/3
(import-free modulo one audit-open weighting), exact 2/3 = the chiral import, data needs
only ≈2/3.
