# Flavor — the SO(2)/U(1)_b readout crux: "gauge vs physical" is a false binary; the gate is a δ-independent measure-counting, undetermined, both readings native

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Claim boundary:** bounded resolution (corrects this build's own framing) + convergence record + a small NEW_PARITY correction.
**Runner:** `scripts/flavor_so2_readout_false_binary_2026_05_30.py` (SCORECARD PASS=4).
**Source:** 6-agent build `wf_eda631b2`; converges with this session's `wf_9977f75f` (Build C), the parallel worker's K-theory reframe, and PR #2412.

## The question and its dissolution
Asked: does the physical mass readout factor through the SO(2)/U(1)_b doublet-frame quotient (→ r=1/2) or
use the full 2-real-dim content (→ r=1)? The build found the pivot — **"is U(1)_b gauge or physical?"** —
is a **false binary**, and corrected its own framing:
- **U(1)_b is *neither*.** Making `C→e^{iα}C` continuous is incompatible with `C³=I` (only `α∈{0,2π/3,4π/3}`
  survive), so there is no continuous `U(1)_b` to quotient (gauge) *or* to call a physical symmetry — both
  horns collapse.
- **δ=arg(b) is physical for the *spectrum*** (it moves the masses / sets the hierarchy) **but δ-blind in
  Q** (`dQ/dδ=0`; `Σλ=3a`, `Σλ²=3a²+6|b|²` are both δ-independent). So δ's physicality does **not** pull
  the answer to det_R/r=1 — both readings live on the `U(1)_b`-invariant radial sector `(a,|b|)`.

## The actual gate (δ-independent measure-counting)
`det_R(αP_s+βP_d)=αβ²` counts the doublet by its **real dimension 2** → `(1,2)` → r=1 → Q=1; `det_C=αβ`
counts it as **one complex slot** (the SO(2)-frame-reduced determinant) → `(1,1)` → r=1/2 → Q=2/3. They
differ *only* by whether the doublet's SO(2) frame-angle is quotiented before taking the real determinant —
a pure complex-vs-real **measure-counting** choice, orthogonal to δ's physicality.

## Verdict — UNDETERMINED; both readings native; neither forced
framework baseline+retained do **not** fix the counting. Crucially (per the companion correction note this session): the
complex/`det_C`/block reading is **native** — it uses the C₃-equivariant `J_cs=(C−C²)/√3`, which `C³=I` does
**not** forbid (that only blocks the continuous symmetry, not the measure). So this is **not** "det_R forced,
det_C imported"; it is two native readings, **neither uniquely forced** — exactly Build C's result (the trace
Q=1 is privileged only by the unaudited PRR) and the parallel worker's K-theory fork (`K₀`-real Q=2/3 vs
`K₀`-complex Q=1). The slot is a free native reality-structure bit.

## Small correction to NEW_PARITY_IS_CIRCULANT_PHASE
Full `(1+2)` degeneracy occurs at **every** `δ=mπ/3` (the 6 dihedral images), not only at `sin(δ)=0`
(`δ=0,π`). The precise nondegeneracy condition is **δ not a multiple of π/3** (`δ=0,π` are the τ-fixed loci;
`δ=π/3,2π/3,…` are degenerate under the other reflections). Verified.

## Stale-citation flags
- Anchors: `koide_real_rep_block_count_permitted_not_forced` (unaudited, the SO(2)/J handle, matched here),
  `koide_c3_generator_rephasing_obstruction` (retained, constrains the *symmetry* not the `J_cs` measure),
  `new_parity_is_circulant_phase` (retained_bounded — degeneracy locus refined above). Parallel PR #2412
  carries the `K₀`-real-vs-complex equivalence.
