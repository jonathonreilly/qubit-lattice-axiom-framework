# Flavor — b/a not forced, but RP-bounded and = the Hilbert-Schmidt equipartition

**Date:** 2026-05-30
**Claim type:** bridge-gap attack move 2 / honest bound + characterization (NOT a
derivation of the value). Imports nothing as derived.
**Runner:** `scripts/flavor_ba_ratio_bound_hs_equipartition_2026_05_30.py` (+ cache).
**Source:** 6-angle attack workflow (`wf_10741a2a`, 0/6 forced, RP bound +
HS-equipartition lead) + independent verification (all to 1e-15).

## The question
Does the `g_bare=1` action FORCE or BOUND the distance-2/distance-0 corner-coupling
ratio `b/a` — the import-free Koide value gate (`Q=2/3 ⟺ b/a=1/√2`, from move 1)?

## (1) Not forced
No native, non-circular principle forces `b/a=1/√2=0.7071`. Every native candidate
for the heat-kernel time `t` (`b/a=tanh²t`) misses:
- naive `t=g_bare²=1` → `b/a=0.580` (Q=0.558)
- bare-action `t→0` → `b/a=0` (Q=1/3)
- nearest Casimir `t=C₂(1,0)=4/3` → `b/a=0.757` (Q=0.715, closest, still 7% high)
- target `t*=atanh(2^{-1/4})=1.2242` is transcendental — no Casimir / Laplacian-
  eigenvalue / counting origin. **0/6 angles survived to a forcing.**

## (2) Reflection-positivity bound (native, import-free)
`Y = aI + b(J−I)` must be PSD (Osterwalder–Schrader / a sensible Hilbert space):
eigenvalues `a+2b≥0` (singlet), `a−b≥0` (doublet) ⟹
```
b/a ∈ [−1/2, 1].
```
`1/√2` is a **strict interior point** — `0.293` below the upper edge `b/a=1`
(which is `Q=1`, a massless doublet). So RP **contains** but does not pin `1/√2`.
The actual criticality limits land at the *edges*: zero-mode critical → `b/a=1`
(Q→1); generation-sector critical → `b/a=−1/3` — i.e. **at the critical points the
geometry predicts Q=1, not Q=2/3**; `1/√2` is a non-critical interior modulus.

## (3) The Hilbert-Schmidt equipartition (clean characterization — the lead)
`1/√2` is the **unique** point where the off-diagonal operator `b(J−I)` carries the
same canonical-trace (HS) norm as the diagonal `aI`:
```
Tr((aI)²) = 3a² ,   Tr((b(J−I))²) = 6b²   ⟹   equal ⟺ b/a = √(3/6) = 1/√2.
```
The **factor 2** is `Tr((J−I)²)/Tr(I²) = 6/3 = dim(doublet)/dim(singlet)`. Under the
canonical HS measure `e^{−Tr(M²)/2}`, the ensemble variance ratio is
`⟨b²⟩/⟨a²⟩ = (1/6)/(1/3) = 1/2` ⟹ **Q = 2/3 exactly**. This is not a tuned number —
it is the max-entropy / flat measure on the 2-dim S₃-invariant operator space
`span{I, J−I}` under the HS inner product.

## (4) The crux — a 3-way MEASURE fork (now concrete)
| measure on `span{I, J−I}` | `r` | `Q` |
|---|---|---|
| HS / trace (equipartition) | 1/2 | **2/3** |
| dimension / Plancherel | 1 | 1 |
| fermion **dynamics** (this session, 3 computations) | 0 | 1/3 |

The observed `Q=2/3` matches the **HS measure**. But the framework's fermion vacuum
selects **neither** HS nor dimension — the gap equation / competing-orders /
effective-potential computations all give the uniform-condensate-wins answer,
`b→0`, `Q=1/3`. So `1/√2` is the **HS-max-entropy value, which the dynamics does
not realize.** This is a genuine, sharp tension: *native dynamics → Q=1/3;
observed → Q=2/3 = HS-equipartition.*

## Import caught
`b/a` is numerically Brannen's fitted circulant amplitude `η` (`η²=1/2` *fit to
observed lepton masses*). Citing `η` to "fix" `b/a` imports the answer
(wrong-escape-via-citation; already flagged 2026-05-29). The `tanh²(t)` *form* is
native; its *evaluation point* is not.

## Status (caveats verified vs origin/main ledger)
Valid retained: `cl3_color_automorphism_theorem` (retained),
`site_phase_cube_shift_intertwiner_note` (retained),
`g_bare_rescaling_freedom_removal` (retained_bounded),
`action_uniqueness_note` (retained_bounded), `action_normalization_note`
(retained_no_go). **Not load-bearing:** the 4 `bridge_gap_hk_*_2026-05-06` notes are
*unaudited*; `staggered_dirac_realization_gate` is `audited_renaming` (still open,
no retained no-go forecloses `b≠0`). The cube-heat-kernel ↔ generation-mass
identification is itself a *candidate*.

## The path this opens (not a wall)
The value gate is now **bounded and characterized**, and the open question is
**decidable**: *which inner product does the matter-sector OS-reconstruction measure
place on `span{I, J−I}`?* HS/trace → `1/√2` (Q=2/3, the equipartition lead);
dimension → Q=1; or does the fermion dynamics (→ Q=1/3) govern? That single native
OS-measure derivation on the corner cube promotes `1/√2` from "positivity-consistent
HS-equipartition point" to forced — or resolves the dynamics-vs-measure tension
explicitly. No false closure; `b/a=1/√2` is not claimed derived.
