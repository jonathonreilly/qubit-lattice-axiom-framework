# The Interleaved Mean Map: the Peripheral Count Collapse, and the Removal of the #3491 Almost-Periodicity Obstruction at the Mean Level

**Date:** 2026-06-10
**Type:** bounded theorem (retire-mode; owner-directed assault on the R1/R2 pair; panel-narrowed)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_interleaved_mean_map_peripheral_count_collapse_relaxation_2026_06_10.py`
**Cache:** `logs/runner-cache/frontier_interleaved_mean_map_peripheral_count_collapse_relaxation_2026_06_10.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=14 FAIL=0`, exact,
deterministic, no MC. A mandatory 4-lens adversarial panel returned `land_with_edits`;
**all ten required edits are applied** — including the decisive one: the draft's
"floorless" iteration was *not* floorless (peripheral round-off captured the iterate by
`n≈100`), and every M3 quantity is now computed on **deflated genuine signal**.

## The wall, and what this note is — and is not

R1 is double-walled by retained boundaries (`record_classical_semigroup` /
`record_markov_generator_embeddability`); R2 is the **i.i.d.-central-step-measure**
premise of the heat-kernel CLT. **This note is not an R2 delivery** — it delivers no
measure on SU(3), and its own central finding (the induced orientation converges to a
*delta*) is the **opposite** of the nonzero-variance spread the CLT premise needs; a
future reader must not mistake mean-trajectory convergence for CLT progress. What it
*is*: the composition of the two **landed exact one-body rules** (the #3457 flow and the
block-02 record channel) into one exact linear map `Φ = D_λ∘Ad_W` (81×81, computed), whose
spectral analysis **removes the #3491 almost-periodicity sub-obstruction at the mean
level** and identifies exactly what is conserved.

## The results (exact — runner `PASS=14 FAIL=0`)

**(M1) The peripheral count collapse — the new load-bearing structure.** `Φ`'s peripheral
spectrum is **exactly 3-dimensional**: the per-color uniform diagonals, i.e. **the
conserved color counts** — verified as exact fixed points, with the dimension count
closing the identification. The genuinely new content is the **collapse 9 → 3** driven by
the color-blind hop (the gap itself is per-step, per-color *decoherence damping* — a
single-color toy reproduces the same gap values; "mixing" in the forbidden
continuous-ergodic sense is neither claimed nor implied; the map is **discrete-time**
throughout). Gap values instance-labeled (`0.321` at `(λ,τ)=(0.45,0.35)`; `0.174` at
`(0.25,0.6)` — structure stable, values parameter-dependent: `λ, τ` are *supplied*
parameters of the named instrument admission). The matter mean **relaxes to the count
form** `ρ_color(x) = diag(N_c)/N` (#3474-T4; equal counts ⟺ neutral — the #3486 clause
in count form), and the mean link carrier dies at the derived dominant **per-step ratio**
(clean-window match; tolerance instance-labeled).

**(M2) The refuted shortcut** *(a one-body re-exhibit of block-02 content)*. One record
step is exact scalar damping on the cross-block — polar-invariant in isolation — but the
composition with the flow is **not** scalar: the induced orientation departs at order 1
within six steps. The polar-invariance shortcut is false; exhibited so it isn't retried.

**(M3) The removal of the almost-periodicity obstruction — the single load-bearing new
dent.** Along the interleaved mean trajectory, computed on **deflated genuine signal**
(the panel-fixed iteration `X ← (I−P_per)Φ(X)` with the oblique peripheral spectral
projector — plain renormalization lets `μ=1` round-off capture the iterate by `n≈100`,
and the draft's original M3 numbers were noise): the induced curvature `C(n)`
**converges** (last-century change `<10⁻⁸`; the limit value is **one realization's
number** — state-realization data, not a derived constant); the orientation converges
Cauchy-tight; the converged cross-block lies in the dominant family's cross-block image,
whose **rank is exactly 3** (panel-tightened guard; the random control's expected
residual for a 3-of-9 image is `√(1−⅓) = 0.816` — its power is dimension-counting,
disclosed as such); and **the convergence rate is itself derived**: the orientation-error
log-slope matches `ln(|μ₂|/|μ₁|)` to a few percent (`−0.0176` vs `−0.0172` per step — an
earlier apparent "crossover" was the un-deflated noise artifact, panel-caught).
**Corpse-angle qualification (panel):** the fixed point itself is *diagonal* — it carries
**no link**; the convergent object is the polar **orientation of the vanishing centered
transient** (a scale-invariant direction), *not* a gauge configuration present at the
fixed point. The limit is **initial-state-dependent**: no universal selection is claimed
(the #3486 clause).

**(M4) I-B erasure** *(a one-body re-exhibit of block-02's #3425)*: site-pinching is
scalar **zero** on adjacent cross-blocks — instant link erasure at measured sites; the
on-site color block is preserved exactly.

## Where this leaves R1/R2

- **Removed:** the #3491 sub-obstruction (*no relaxation, no stationary configuration at
  the mean level*) — with records interleaved, the induced trajectory relaxes, at a
  derived per-step rate, into a derived spectral subspace.
- **Untouched, stated plainly:** the retained R1 boundaries (discrete-time map
  throughout; no continuous generator or rate law is claimed or implied); R2's
  step-measure premise (**nothing here supplies a distribution on SU(3)**; mean
  convergence to a delta is a measure of how much is still missing, not progress toward
  the spread). The link remains slaved (campaign blocks 01–03).
- **Doors named:** the **stochastic unraveling** (outcome-resolved trajectories would
  carry the step distribution the CLT needs — requires outcome-weight/Born structure; a
  named separate thread); **structured/frame-naming instruments** (= the `{P_r}` root);
  **interactions** (#3457-T4 breaks one-body closure). Conditional on the supplied `C³`
  carrier, the named hopping, and the named instrument classes (instrument existence =
  the standing admission, with `λ, τ` its supplied parameters). No new axiom, primitive,
  measure, or weight; `r` untouched. The audit lane grades.

## Cross-references

- Nearest prior art for the dephasing+unitary spectral composition (panel-required):
  the unistochastic pointer-frame fork (PR #3436, on main) and the block-03
  pointer-sector fixed point (PR #3427, on main) — M1 generalizes their fixed-point
  analyses to the full sites×colors space with the exact peripheral-completeness
  statement; M2/M4 are one-body re-exhibits of block-02 (PR #3425, on main).
- The R1 boundaries respected: `record_classical_semigroup_boundary_2026-06-06`
  (retained), `record_markov_generator_embeddability_boundary_2026-06-06`
  (retained_no_go).
- The almost-periodicity obstruction removed at the mean level: PR #3491
  (**branch-only; PR open**).
- The exact one-body rules composed: PR #3457 (branch-landed). The count form: PR #3474
  (T4; branch-landed). The state-realization clause: PR #3486 (branch-landed).
- Standard math (method only): linear dynamical maps; peripheral spectra; oblique
  spectral projectors and deflation; projective/subspace iteration; non-normal matrix
  numerics.
