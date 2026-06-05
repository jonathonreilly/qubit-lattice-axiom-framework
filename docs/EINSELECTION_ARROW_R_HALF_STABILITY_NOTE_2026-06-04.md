# Einselection arrow / `r=1/2` stability — which arrow does "irreversible record-formation" pick, and is `r=1/2` stable under it?

**Date:** 2026-06-04
**Claim type:** meta
**Verdict:** **SEPARATRIX-SADDLE-ONLY** (with a sharp "STABLE-UNDER-RECORD-ARROW only if record-formation = einselection-equilibration" caveat).
**Claim boundary:** a bounded map/dynamics theorem on the C₃-generation dial `r=|b|²/a²`. It formalizes the two competing arrows, the genuine einselection pointer map, their fixed points and **linear stability**, the reconciliation, and the multi-stability question. It does **not** derive which arrow the physical charged-lepton sector follows, does **not** derive that `r` evolves by any of these maps, and consumes **no** measured masses, **no** new axiom, and **no** new framework primitive.
**Status authority:** independent audit lane only. This note does not set or predict an audit verdict; effective status is pipeline-derived after independent audit.
**Runner:** [`scripts/einselection_arrow_r_half_stability.py`](../scripts/einselection_arrow_r_half_stability.py) (SCORECARD 27/27).
**Cache:** [`logs/runner-cache/einselection_arrow_r_half_stability.txt`](../logs/runner-cache/einselection_arrow_r_half_stability.txt)

## The question (a stability test, NOT a forcing claim)
Under the reframe, `r=1/2` is the *balanced* setting on the exact Koide line `Q=1/3+(2/3)r`, not a forced value. The record axiom's **irreversibility** clause ("records can't unform; record-formation orders time") picks an **arrow** on the dial. Does that arrow make `r=1/2` a **stable** setting (an attractor the arrow holds)?

Two notes on `origin/main` pull against each other and motivate this:
- [`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md): the Lüders **sharpening** flow `sharpen(r)=2r²` makes `r=1/2` an **unstable separatrix** (multiplier 2).
- [`FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02`](FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md): the reverse map `therm(r)=√(r/2)` makes `r=1/2` a **stable attractor** (multiplier 1/2).

The runner re-verifies these are **exact inverse branches** of one map family (`sharpen∘therm = id`, multiplier product `2·½=1`). So `r=1/2`-stability is **arrow-dependent**; the contradiction is not algebraic, it is an arrow choice. This continues the boundary set by [`FLAVOR_SUPPLIED_HEAT_KERNEL_ARROW_R_HALF_STABILITY_BOUNDED_NOTE_2026-06-04`](FLAVOR_SUPPLIED_HEAT_KERNEL_ARROW_R_HALF_STABILITY_BOUNDED_NOTE_2026-06-04.md).

## Which arrow is "irreversible record-formation"? Two readings, diagnosed by their monotone
A direction is "irreversible" when it carries a monotone that **cannot decrease**. The runner identifies the monotone of each candidate arrow (Part 6):

- **(a) Sharpening = the LITERAL "records can't unform."** 2-sector **purity/distinguishability** is monotone **non-decreasing** under `sharpen`: records get ever sharper, distinguishability monotonically accumulates. This is the most literal reading of "records can't unform / monotone accumulation." Under it **`r=1/2` is the unstable separatrix** — and `r>1/2` runs to `r→∞` (projective doublet collapse), `r<1/2` collapses to `r=0` (singlet, the degenerate `[1,1,1]`, `Q=1/3`).
- **(b) Einselection-equilibration = "a record is a PERSISTENT stable correlation."** 2-sector **entropy** is monotone **non-decreasing** under `therm` (relaxation to equipartition, the second-law direction). A record is not maximal sharpening (that ends in a *collapse*, `r=0` or `r→∞`, which **destroys** the balanced 3-record structure); a record is a correlation that **persists** = a stable fixed point under continued monitoring (an einselection pointer state). Reading "record-formation" as **relaxation to the einselection-stable setting** makes the balanced interior point the **attractor**: under `therm`, **`r=1/2` is the unique stable interior setting** (multiplier 1/2; all positive seeds converge).

The two monotones **disagree at `r=1/2`**: purity-up repels it, entropy-up attracts it (Part 6.3). That is the honest crux.

## The genuine einselection pointer map is FLAT in `r` (it picks neither side)
Crucially, the **literal** Zurek pointer/decoherence map — dephasing `D(ρ)=P₀ρP₀+P₁ρP₁` that kills singlet↔doublet coherence — is a **no-op** on the generation circulant, because `H=aI+bC+b̄C²` is **already block-diagonal** in `{P₀,P₁}` for every `r` and every phase `δ` (`‖P₀HP₁‖~10⁻¹⁶`, by C₃-invariance). Reconstructing `r` from `D(H)` via the exactly-invertible Koide readout `r=(3Q−1)/2` returns the **input `r` unchanged**: the induced map on `r` is the **identity**, multiplier **exactly 1 — marginal** (Part 4, non-circular: the readout is verified faithful). So einselection-**as-dephasing** is a *flat line of fixed points*; it neither stabilizes nor destabilizes `r=1/2`. This reproduces the prior finding of [`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md) from the stability angle.

**Consequence:** "einselection stabilizes `r=1/2`" is true **only** in the relax-to-attractor (`therm`) reading, **not** in the literal dephasing reading. And the genuine **Born/second-law** equilibrium `ρ=I/3` weights the blocks by **dimension** `(1/3,2/3)` → **`r=1`** (`Q=1`), not `r=1/2`; `r=1/2` requires the **equal-power-per-block (block-counting/det_C)** weighting `(1/2,1/2)` — a separate input (Part 5). This is the standing partition gate.

## Attractor or saddle? (honest)
- **On the 1-D dial**, `r=1/2` is a genuine 2-sector-**entropy maximum** (`S₂''(1/2)<0`) and the attractor of the `therm` branch — a **true attractor of that arrow**.
- **On the full doublet density-operator space**, the records-flow Hessian at `r=1/2` is **rank-1, spectrum `{−3/4,0,0}`** (degenerate — a symmetric saddle, not a generic basin; commit `d7c85611e`), and the genuine second-law/Born attractor is `r=1`, not `r=1/2`. The honesty guard (Part 11) confirms the **3-mode** spectral Lüders sharpening does **not** fix the `r=1/2` spectrum — the fixed point lives on the *reduced* 2-sector dial.

So `r=1/2` is the **distinguished symmetric setting** (HS 2-sector equipartition `‖aI‖²=‖bC+b̄C²‖²`, self-dual, the `S₂` max) — a real attractor of the thermalizing/equilibration arrow but only a **symmetric saddle** under the literal "records can't unform" (purity-sharpening) arrow, with the literal dephasing map flat.

## Multi-stability
No single 1-D arrow makes `{r=0, r=1/2, r=1}` simultaneously stable: `sharpen`-stable `={0}`, `therm`-stable `={1/2}`, and `r=1` is not even a finite fixed point of either map (Part 9). The three Koide lanes are the attractors of **three distinct measures/arrows** — spectral/sharpening→`r=0` (`Q=1/3`), block-counting/thermalizing→`r=1/2` (`Q=2/3`), dimension/Born→`r=1` (`Q=1`). **Multi-stability is realized across the measure choice** (the standing partition gate), **not** as a coexisting triple of one flow. The irreversibility clause picks **one** arrow ⇒ **one** stable lane.

## Net
**Verdict: SEPARATRIX-SADDLE-ONLY.** Honestly: the *literal* "records can't unform / monotone accumulation" clause is the **sharpening** arrow (purity-up), under which `r=1/2` is the **unstable separatrix** — a knife-edge (matching the `~10⁻⁵` Koide precision reading). `r=1/2` becomes a **stable attractor** only under the **einselection-equilibration** reading (`therm`, entropy-up, "a record is a persistent stable correlation"), which is a defensible but **distinct** arrow — and the *literal* einselection pointer/dephasing map is **flat** (marginal) in `r`, picking neither. The arrow choice (sharpening-purity vs equilibration-entropy vs Born-dimension) is exactly the standing **block-counting-vs-Born partition gate** in dynamical language; it is **not closed here**.

## The next paths this opens (not closing)
- Find a framework-native reason the charged-lepton coarse-graining is the **equilibration (entropy-up) arrow** on the 2-sector partition rather than the sharpening (purity-up) arrow — that would upgrade `r=1/2` from symmetric saddle to attractor.
- Or supply a stabilizer that pins the **2-sector (block-counting) record basis** as the physical coarse-graining (the partition half), turning the separatrix into a held setting — the object [`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md) reduced to K-reality + the block-counting measure.

## Provenance (verified 2026-06-04)
- `sharpen`/`therm` inverse-branch + stability flip, sharpening separatrix + runaway, thermalizing global attractor, dephasing no-op + marginal multiplier (non-circular Koide-readout reconstruction), Born→`r=1` vs block-counting→`r=1/2`, `S₂`/`S₃` peaks, monotone diagnosis, persistent-record reading, multi-stability, `S₂''(1/2)<0`, HS equipartition, 3-mode honesty guard: verified directly (runner 27/27).
- Anchors (informational; audit lane authoritative): `luders_rule_from_composition_consistency` (retained_bounded, the `r→2r²` flow), `frobenius_isotype_split_uniqueness` (retained_no_go, declines to rank (1,1) vs (1,2)). Sibling flavor notes cited above. The records-flow Hessian `{−3/4,0,0}` is from commit `d7c85611e`.
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
