# Flavor — the trace-vs-center fork is INVERTED and largely DISSOLVES; r=1/2 is a free modulus, sharpened to the signed/Hermitian readout class

**Date:** 2026-05-30
**Claim type:** bounded clarification (corrects a prior panel reframe) + honest reduction.
**Status authority:** independent audit lane only; this note sets source metadata only.
**Runner:** `scripts/flavor_trace_vs_center_dissolves_2026_05_30.py` (SCORECARD PASS=4).
**Source:** 9-agent build `wf_c498a020` (map → 4 tests → 3 adjudications → synthesis), all numerics re-verified.

## Question
The 20-physicist panel's surviving reframe proposed: r=1/2 (Q=2/3) = the symmetric STATE on the
abelian CENTER of `A=ℝ[Z₃]` (block-count), and r=1 (Q=1) = the faithful TRACE (dimension/Plancherel).
The decidable fork: which functional does mass generation use? Four native tests + adjudication.

## Result — the fork is INVERTED and largely DISSOLVES
The build's own adversary and three independent routes found the panel's MAP **numerically backwards**,
and the empirical observable settles it:

- **The empirical Koide observable `Q=(Σm)/(Σ√m)²` is TRACIAL.** On the native real-circulant spectrum
  `{a+2b, a−b, a−b}` the doublet eigenvalue `a−b` appears with its **physical multiplicity 2** (there
  really are two of the three leptons in the doublet) in *both* sums. With the signed/Hermitian readout
  (mass=λ², √m=signed λ): `Q=(a²+2b²)/(3a²) = 1/3 + (2/3)r` **exactly**, so **Q=2/3 ⟺ r=1/2**. This is
  the **trace / dimension-weighted** reading — the panel's "center → r=1/2" was inverted.
- **The center / block-count weight (w₁=1)** gives `Q=1/3+(1/3)r → Q=2/3 at r=1`, not r=1/2. The
  literal center reading cannot even resolve the dim-2 multiplicity (it gives r=0). So no non-tracial
  center-state is needed or physical; the dim-2 doublet weighting **is** the physical generation count,
  which is forced, not chosen.

## No principled native test forces r=1/2
Four tests, none lands r=1/2 from a measure-free principle:
| test | r landed | note |
|---|---|---|
| classical Fisher `I_s=I_d` | `r = 17/2 − 6√2 ≈ 0.0147` | reparam-invariant point, physically meaningless |
| Bures / SLD sector-balance | `r = 1/16` | panel #11's predicted `r=1/4` is **falsified** |
| equivariant APS η, weights (1,2) | `r = 1` | the doublet gap `a−b` genuinely closes at `b=a`; forced, but to **1** |
| heat-trace / Seeley-DeWitt extremization | `r = 0` or `1` | r=1/2 only by imposing equal split `3a²=6b²` by hand |

`r=1/2` re-appears **only** when one imposes the equal-HS-split `3a²=6b²` (equipartition) — exactly the
unforced equal-block constraint, by hand. (Eigenvalue-as-mass / singular-value readout instead sends
`Q=2/3` to `r≈0.916`.)

## Honest reduction — what the value now rests on
1. **The fork dissolves toward the trace/dimension reading**, which is forced (the doublet multiplicity
   2 is the physical generation count). On it `Q=1/3+(2/3)r` is an **exact identity**.
2. **r=1/2 is therefore a free Fourier modulus** `r=|b|²/a²` pinned only by matching the observed
   `Q=2/3`; no native principle (Fisher / index / heat-trace) selects it — those select `r=1`, `0`, or `≈0.015`.
3. **The one genuine, now-sharpened structural input is the readout CLASS:** `Q=1/3+(2/3)r` is exact
   *only* on the **signed/Hermitian** branch (mass=λ², √m=signed λ), i.e. the native Dirac-type operator
   `H=iD` (det_R / Brannen class). The singular-value readout breaks the clean identity. This is the
   same residual flagged in `project_koide_signed_vs_singular_value` — the *measure* question dissolves,
   the *readout-class* question remains, and it is largely native (H=iD is the framework's Dirac operator).

## Reconciliation flag (not a refutation)
This build's "empirical Koide is tracial → r=1/2" coexists with the retained_bounded
`KOIDE_Q23_BLOCK_WEIGHT_FRONTIER` ("equal-block→Q=2/3, dimension→Q=1") as **two parametrizations of one
unforced freedom**: fix the (forced) trace weighting and vary the modulus r (→ r=1/2 ⟺ Q=2/3), vs fix
the operator at the symmetric config `|b|=a` and vary the block measure (→ equal-block gives Q=2/3). The
retained note is not contradicted; this note locates the empirical observable on the trace branch and
identifies the residual as the modulus + readout class, not a measure choice.

## Sharpest next path (not closing)
Derive the **signed/Hermitian readout from the framework's emergent-time / KMS structure** (`H=iD` as the
native generator), and — for the still-free modulus — probe whether a **finite-β KMS / modular-equilibrium
condition on the doublet operator block fixes the Fourier amplitude `|b|=a/√2`** rather than leaving it
matched to data. A non-tracial weight carries a nontrivial modular automorphism, so the KMS route is the
natural candidate to pin the modulus; that is the live thread for r=1/2 itself.

## Stale-citation flags (verified vs origin/main ledger)
- `koide_signed_eigenvalue_vs_singular_value_readout` is **audited_FAILED** — used only for the qualitative
  signed-vs-singular distinction, not cited as retained.
- Anchors: `KOIDE_Q23_BLOCK_WEIGHT_FRONTIER` (retained_bounded), `koide_z3_equivariant_anticommuting_no_go`
  (retained_bounded), `koide_anticommuting_operator_derivation_theorem` (retained).
