# Flavor — operator-realization bridge substantially BUILT: 2/9 is the Atiyah-Bott local fixed-point density of the native C3-equivariant staggered Dirac (surviving global vanishing)

**Date:** 2026-05-31
**Claim type:** bounded_theorem
**Claim boundary:** bounded positive (operator-realization substantially built) + named remaining physical-identification step.
**Runner:** `scripts/flavor_operator_realization_local_density_2026_05_31.py` (SCORECARD PASS=4).
**Source:** operator-realization build `wf_9d871247` (staggered-Dirac Lefschetz / local-vs-global / chirality-distinctness / adversary → adjudication), verified first-principles at L=4 and L=6.

## Question
The single open gate to promote the asymmetry `2/9` from "forced weight-density" to a **closed topological
prediction**: does a *genuine* framework Dirac operator produce the Atiyah-Bott/APS fixed-point density that
equals `L₃(1,2)=2/9`?

## Verdict — substantially BUILT on the operator side; the key hope confirmed
The native **staggered / Kogut-Susskind Dirac on Z³** (Kawamoto-Smit phases; the framework's retained
kinetic operator) genuinely realizes `2/9` as a local fixed-point density:
1. **It is C₃-axis-equivariant — a nontrivial operator fact.** The *raw* axis-permutation `U` (cyclic
   x→y→z) does **not** commute (`‖[U,H]‖=13.9` — the KS phase breaks naive axis symmetry); only the
   **gauge-corrected** `U_phys = U·S` commutes *exactly* (`[U_phys,H]=0`, `U_phys³=I`, verified L=4 & L=6),
   where `S` is the site-local Z₂ gauge from the **retained** "S₃-axis-is-gauge" theorem. So the
   C₃-equivariance is real and retained-grounded, not free.
2. **The fixed set is the diagonal `{x=y=z}` (the singlet), the doublet is transverse** — and the operator's
   *own* C₃-action on its hopping tangent at a fixed site has eigenvalues `{1, ω, ω²}`. The transverse
   weights `(1,2)` are thus **operator-intrinsic** (read off `U_phys`), not assumed; `det(1−dg|⊥)=3`.
3. **The local Atiyah-Bott density per fixed point = `L₃(1,2) = 2/9`** exactly (`(1,1)/(2,2)→1/9`).

## The key hope — CONFIRMED: local survives, global vanishes
The global equivariant index / η / graded-Lefschetz **all vanish** (verified L=4,6): the staggered chirality
`Γ₅=(−1)^{x+y+z}` anticommutes with `H`, pairing the spectrum `±λ` so `η = Σ sign(λ) = 0` (the `χ=0` /
spectral-flow=0 obstruction). **But `2/9` is a *per-fixed-point local* density — it is well-defined and nonzero
even though every global readout vanishes.** This is exactly the hoped-for behavior: the local-density framing
**dodges the global obstruction** (`χ=0`) that killed the chiral / orbit-splitting route.

## Distinct from the chirality gate — and not a tautology
- **Distinct:** the local density uses **only** C₃-equivariance + the transverse linearization — `Γ₅` is
  *never* used to compute it. `Γ₅` enters only in the *opposite* role (killing the global). So the route
  does **not** ask the C₃ orbit to carry a chiral grading, and therefore does **not** inherit the
  `comm(S) ∩ anticomm(Γ_χ) = {0}` chirality no-go. It is a structurally easier, *native* class.
- **Not a rep-weight tautology:** the C₃-equivariance is a nontrivial operator fact (raw permutation fails;
  the gauge correction is retained content), and the `(1,2)` weights are *extracted* from the operator's own
  hopping-tangent action — not imposed from representation theory.

## What remains (now a sharp, named physical-identification step)
The operator side is built. The remaining bridge is the **physical identification**:
> the charged-lepton asymmetry datum `δ` = the **single-fixed-point LOCAL Lefschetz density** (one diagonal
> fixed point's holomorphic-Lefschetz contribution `= 2/9`), **not** the vanishing global η.

Plus the still-`audited_conditional` Cl(3) PL-`S³`/ABSS global-bridge stipulation. This is a *which-object-is-
physical* identification (one local contribution vs the global sum), not a computation gap — and it is the
genuinely-remaining, well-posed step, a live route.

## Standing — the closest the campaign has to a closed topological prediction
The asymmetry `2/9` is now a **derived local topological density of a real, native, C₃-equivariant framework
Dirac operator** — at the forced `d=3`, with the forced `(1,2)` weight, surviving the global vanishing, and
escaping the chirality gate. It is no longer "an abstract weight"; it is the operator's own Atiyah-Bott
fixed-point density. The one step from a fully-closed prediction is identifying the physical asymmetry with
the single-fixed-point local density rather than the global η — a clean, named, live target.

## Stale-citation flags
- `axiom_first_z_n_equivariant_spectral_asymmetry` (retained_bounded, `L₃(1,2)=2/9`); the staggered-Dirac
  kinetic surface (substeps 1-3, bounded_theorem / positive_theorem mix; substep-2 Kähler-Dirac unaudited);
  `staggered_axis_symmetry_is_S3` (retained — the gauge correction `S`); `closure_c_staggered_dirac_gate`
  (was open_gate — this build substantially advances it on the local-density side); the Cl(3) PL-`S³`/ABSS
  global bridge remains audited_conditional.
