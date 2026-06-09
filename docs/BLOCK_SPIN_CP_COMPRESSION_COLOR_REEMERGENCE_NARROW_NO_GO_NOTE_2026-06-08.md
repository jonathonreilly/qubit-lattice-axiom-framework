# Axiom-Preserving Block-Spin Is CP Compression, Not a Morphism — and Color Re-Emerges Per Scale

**Date:** 2026-06-08
**Type:** narrow no-go (color transport through blocking) + a per-scale re-emergence corollary
**Claim type:** no_go
**Script:** `scripts/frontier_block_spin_cp_compression_color_reemergence_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_block_spin_cp_compression_color_reemergence_2026_06_08.txt`
**Status:** source proposal. All four statements are exact finite algebra (runner
`PASS=12 FAIL=0`). Authority role: source proposal; audit lane sets status.

## The question (ST4's sharpest, from the ST3/ST4 wall-map)

Can a block-spin decimation simultaneously preserve the **QUANTUM axiom** (one qubit per
site) and the graph-first **SU(3) color** structure? Note the sharp collision: the color
carrier **is** the `2×2×2` taste cube — a standard `2³` blocking consumes exactly the eight
sites that carry it.

## Verdict

**Color is not *transported* through any axiom-preserving blocking — but nothing is lost,
because the construction is scale-blind and color *re-emerges* at every scale.** The
blocking step itself is necessarily a CP channel, never an algebra morphism.

## What is proved (exact — runner `PASS=12 FAIL=0`)

1. **(T1) No morphism blocking.** A `2×2×2` block carries the local algebra `M₂₅₆`; the
   axiom requires `M₂` at the block-site. A unital `*`-homomorphism `M_n → M_m` exists
   **iff `n | m`** (the `n` diagonal matrix units map to `n` mutually-orthogonal nonzero
   equivalent projectors summing to `I_m`, so `m = n·r`; verified constructively for
   `M₂→M₄` and by the rank bound for `M₄→M₂`). `256 ∤ 2` — **no algebra-morphism blocking
   preserves the axiom.**

2. **(T2) Axiom-preserving blocking is necessarily CP compression.** Landing on a block
   *qubit* means an isometry `V: C² → C²⁵⁶` with `E(X) = V†XV` — unital, `*`-preserving,
   completely positive, and **never multiplicative**: by T1, for *every* isometry there
   exist block observables with `E(XY) ≠ E(X)E(Y)` (forced, and spot-verified across 50
   random isometries). Information loss is intrinsic to the step; the coarse-graining is a
   **channel**, not an automorphism.

3. **(T3) Color is not transported.** `su(3)` is simple (any Lie map is faithful or zero)
   and has **no faithful action on `C²`** (`dim su(3) = 8 > 3 = dim su(2)`). The compressed
   block site carries **no faithful color action** — no axiom-preserving blocking carries
   the graph-first `SU(3)` across the step. (The
   [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md)
   dimension boundary, reused at the block-site.)

4. **(T4) Color re-emerges per scale (the corollary that defuses the "wall" reading).** By
   construction, the blocked lattice is again `Z³` with one qubit per block-site — it
   satisfies LATTICE + QUANTUM **verbatim**. The retained graph-first construction
   ([`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md), retained) is
   **scale-blind**: re-running it on the *block-level* `2×2×2` cube reproduces the
   identical algebra — selected-axis `su(2)` relations, joint commutant dimension **10**
   (`gl(3)⊕gl(1)`), symmetric/antisymmetric split **3⊕1** — verified exactly at the block
   level. **Color is a per-scale derivation, not an RG-carried quantity.**

## What this means (and does not mean) for RG on the physical lattice

- The framework's coarse-graining step is **necessarily a channel** (CP compression). This
  is *not* a defect relative to standard practice — Kadanoff/block-spin RG is likewise a
  truncating, non-morphism map (method context, not an import). What the framework adds is
  the **exact** localization of why: the one-qubit-per-site axiom plus `M_n → M_m`
  divisibility.
- The **choice of isometry `V`** (which 2 of 256 block states survive) is an **undelivered
  selection** — the same family as the open gauge-link-dynamics input (a generator/
  selection the axioms do not supply). It is **not** supplied here; any concrete RG flow
  needs it.
- **Per-scale color is untouched** (the retained graph-first derivation stands at every
  scale). The no-go is strictly about *transport through the blocking step*.

## Honest residuals (what this does NOT foreclose)

- It does **not** foreclose block-spin RG schemes that relax the one-qubit-per-block
  bookkeeping (e.g. keeping a larger block algebra) — those simply sit outside the QUANTUM
  axiom's per-site reading at the block level, and their status is a separate question.
- It does **not** construct or constrain the framework's actual RG flow (the isometry
  selection and the dynamics input remain open).
- It does **not** touch the single-scale color derivation (retained), the link-carrier
  routing (PR #3398), or the dynamics wall (PR #3394).
- No closing language: other coarse-graining notions (operator-algebraic conditional
  expectations onto subalgebras, tensor-network maps) are not enumerated or foreclosed.

## Forbidden-imports check

No PDG value, fitted number, new axiom, or new framing is consumed. The matrix-unit /
divisibility argument, Stinespring/Kraus form of the compression, `su(3)` simplicity, and
the Kadanoff-blocking context are standard math/method. The block-level re-run uses only
the retained graph-first construction's own checks.

## Cross-references

- The per-scale color derivation (retained, scale-blind): [`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
- The qubit dimension boundary (reused at the block-site): [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md)
- The undelivered-selection family (the dynamics wall capstone): `ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE_NARROW_THEOREM_NOTE_2026-06-08` (PR #3394 — referenced by name, pending merge)
- RG-formalism context (external, registered): [`BBS_RG_BANACH_CONTRACTION_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-10`](BBS_RG_BANACH_CONTRACTION_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-10.md)
- Standard math/method (not imports): matrix-unit divisibility for `*`-homomorphisms (Bratteli); Stinespring/Kraus compressions; Kadanoff block-spin as truncating map.
