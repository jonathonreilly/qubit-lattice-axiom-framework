# Axiom-Preserving Block-Spin Is a Channel, Not a Morphism — and Color Re-Emerges Per Scale

**Date:** 2026-06-08
**Type:** narrow no-go (color transport through blocking) + a per-scale re-emergence corollary
**Claim type:** no_go
**Script:** `scripts/frontier_block_spin_cp_compression_color_reemergence_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_block_spin_cp_compression_color_reemergence_2026_06_08.txt`
**Status:** source proposal. All four statements are exact finite algebra (runner
`PASS=12 FAIL=0`). Authority role: source proposal; audit lane sets status.

## The question (ST4's sharpest, from the ST3/ST4 wall-map)

Can a block-spin decimation simultaneously preserve the **Quantum axiom** (one qubit per
site) and the graph-first **SU(3) color** structure? Note the sharp collision: the color
carrier **is** the `2×2×2` taste cube — a standard `2³` blocking consumes exactly the eight
sites that carry it.

## Verdict

**Color is not *transported* through any axiom-preserving blocking — but nothing is lost,
because the construction is scale-blind and color *re-emerges* at every scale.** The
blocking step cannot be an algebra morphism; any unital block-qubit quantum channel used for
it is necessarily non-multiplicative.

## What is proved (exact — runner `PASS=12 FAIL=0`)

1. **(T1) No morphism blocking.** A `2×2×2` block carries the local algebra `M₂₅₆`; the
   axiom requires `M₂` at the block-site. A unital `*`-homomorphism `M_n → M_m` exists
   **iff `n | m`** (the `n` diagonal matrix units map to `n` mutually-orthogonal nonzero
   equivalent projectors summing to `I_m`, so `m = n·r`; verified constructively for
   `M₂→M₄` and by the rank bound for `M₄→M₂`). `256 ∤ 2` — **no algebra-morphism blocking
   preserves the axiom.**

2. **(T2) Axiom-preserving channel blocking is not multiplicative.** If a block-qubit
   coarse-graining were unital and multiplicative, it would be the forbidden `M₂₅₆ → M₂`
   algebra morphism from T1. Thus any unital block-qubit quantum channel is
   non-multiplicative.
   The runner uses the canonical one-leg compression model `E(X) = V†XV` with
   `V: C² → C²⁵⁶`: unital, `*`-preserving, completely positive, and **never
   multiplicative** (forced by T1, spot-verified across 50 random isometries). Information
   loss is intrinsic to the step; the coarse-graining is a **channel**, not an automorphism.

3. **(T3) Color is not transported.** `su(3)` is simple (any Lie map is faithful or zero)
   and has **no faithful action on `C²`** (`dim su(3) = 8 > 3 = dim su(2)`). The compressed
   block site carries **no faithful color action** — no axiom-preserving blocking carries
   the graph-first `SU(3)` across the step. (The
   [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md)
   dimension boundary, reused at the block-site.)

4. **(T4) Color re-emerges per scale (the corollary that defuses the "wall" reading).** By
   construction, the blocked lattice is again `Z³` with one qubit per block-site — it
   satisfies Lattice + Quantum **verbatim**. The retained graph-first construction
   ([`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md), retained) is
   **scale-blind**: re-running it on the *block-level* `2×2×2` cube reproduces the
   identical algebra — selected-axis `su(2)` relations, joint commutant dimension **10**
   (`gl(3)⊕gl(1)`), symmetric/antisymmetric split **3⊕1** — verified exactly at the block
   level. **Color is a per-scale derivation, not an RG-carried quantity.**

## What this means (and does not mean) for RG on the physical lattice

- An axiom-preserving block-qubit coarse-graining step cannot be an algebra morphism. If it
  is a unital quantum channel, it is necessarily non-multiplicative. The runner models this
  by an isometric CP compression. This is *not* a defect relative to standard practice —
  Kadanoff/block-spin RG is likewise a truncating, non-morphism map (method context, not an
  import). What the framework adds is the **exact** localization of why: the
  one-qubit-per-site axiom plus `M_n → M_m` divisibility.
- The **choice of isometry `V`** (which 2 of 256 block states survive) is an **undelivered
  selection** — the same family as the open gauge-link-dynamics input (a generator/
  selection the axioms do not supply). It is **not** supplied here; any concrete RG flow
  needs it.
- **Per-scale color is untouched** (the retained graph-first derivation stands at every
  scale). The no-go is strictly about *transport through the blocking step*.

## Honest residuals (what this does NOT foreclose)

- It does **not** foreclose block-spin RG schemes that relax the one-qubit-per-block
  bookkeeping (e.g. keeping a larger block algebra) — those simply sit outside the Quantum
  axiom's per-site reading at the block level, and their status is a separate question.
- It does **not** construct or constrain the framework's actual RG flow (the isometry
  selection and the dynamics input remain open).
- It does **not** touch the single-scale color derivation (retained), the link-carrier
  routing (PR #3398), or the dynamics wall (PR #3394).
- No closing language: other coarse-graining notions (operator-algebraic conditional
  expectations onto subalgebras, tensor-network maps) are not enumerated or foreclosed.

## No-Go Discipline Gate

**Result:** PASS for the narrowed transport no-go only. This does not say RG is impossible,
that color cannot be recovered at a new scale, or that every coarse-graining formalism is
foreclosed.

**N1 — Alternative route enumeration.**

| Route | Test / status | Why it does not transport graph-first color through one-qubit blocking |
|---|---|---|
| Unital algebra morphism `M₂₅₆ → M₂` | ATTEMPTED, runner T1 | Divisibility fails: a unital `*`-homomorphism `M_n → M_m` requires `n | m`, and `256 ∤ 2`. |
| Isometric CP compression | ATTEMPTED, runner T2 | It lands on `M₂`, but if it were multiplicative it would be the forbidden morphism; the tested compression is a non-transporting channel. |
| General unital block-qubit channel | RULED OUT BY PRIOR (T1) | A multiplicative unital channel would be the forbidden algebra morphism; a non-multiplicative channel may coarse-grain but does not transport color as an algebraic structure. |
| Faithful color action on the block qubit | ATTEMPTED, runner T3 | A faithful `su(3)` action cannot fit on `C²`; the block qubit has only the `su(2)` traceless-operator dimension. |
| Per-scale graph-first re-derivation | ATTEMPTED, runner T4 | This succeeds, but it is re-derivation on the new block-level cube, not transport through the blocking map. |
| Keeping the full block algebra | RULED OUT BY PRIOR (Quantum axiom) | This can retain `M₂₅₆`, but then the block site is not the one-qubit Quantum-axiom site reviewed here. |
| Tensor-network, conditional-expectation, or other RG formalisms | RULED OUT BY PRIOR (T1) for this claim; open otherwise | If they still claim unital one-qubit morphism transport, T1 applies; if they use larger bond/block data, they are outside this claim and remain open. |
| Dynamics or isometry-selection route | RULED OUT BY PRIOR (T1) for this claim; open otherwise | Selection may choose a channel or flow, but it does not turn a one-qubit channel into the forbidden multiplicative transport map. |

**N2 — Wall-independence audit.** The collapsed wall is one algebraic transport wall:
`M₂₅₆` cannot be transported to an axiom-level `M₂` block site by a unital algebra morphism.
The color-action dimension check is a separate diagnostic of the same transport failure, not
a second independent import demand.

**N3 — Hidden-wall scan.** "Axiom-preserving" means only the supplied Lattice + Quantum
block-site reading; "channel" is a quantum-map category, not an added dynamics; "standard
Kadanoff" is method context only; and "scale-blind" is supported by the explicit T4 rerun.
No readout, weighting, dynamics, or selection premise is hidden in the claim.

**N4 — Residual matching.** The qubit-link dimension boundary matches only the no-faithful
`su(3)`-on-`C²` diagnostic. The graph-first note matches only the single-scale/per-scale
construction. The ST1/ST2 wall note matches only the undelivered dynamics/selection family.
No cited witness is used as a global RG no-go.

**N5 — Rhetoric audit.** The tested negative is per block-spin step and per block-site:
no unital algebra morphism `M₂₅₆ → M₂`, and no faithful `su(3)` action on that block qubit.
The note does not claim a lattice-wide impossibility for RG, color, or other coarse-graining
categories.

**N6 — Partial-closure path scan.** Three live closure paths remain explicit: keep a larger
block algebra, rederive graph-first color per scale, or derive/import a dynamics and channel
selection rule with owner approval. The current Lattice + Quantum + Record baseline and the
approved primitives do not supply those extra choices.

**N7 — Steelman.** A hostile reviewer would say color should be encoded in a larger
effective block Hilbert space, a tensor-network bond space, or a selected channel rather than
in the one-qubit block site itself. That is compatible with this note: those routes are left
open, while the exact one-qubit morphism-transport route is closed.

**N8 — Cross-cycle echo.** Prior dynamics-wall notes repeatedly warn against upgrading a
failed transport or selection route into a global impossibility. This note adopts that
lesson: it lands only the finite algebra transport boundary and the per-scale re-emergence
corollary.

## Forbidden-imports check

No PDG value, fitted number, new axiom, primitive, Tier-A admission, or new framing is
consumed. The matrix-unit / divisibility argument, the CP-channel/compression category,
`su(3)` simplicity, and the Kadanoff-blocking context are standard math/method. The
block-level re-run uses only the retained graph-first construction's own checks.

## Cross-references

- The per-scale color derivation (retained, scale-blind): [`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
- The qubit dimension boundary (reused at the block-site): [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md)
- The undelivered-selection family (the dynamics wall capstone): [`ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE_NARROW_THEOREM_NOTE_2026-06-08`](ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE_NARROW_THEOREM_NOTE_2026-06-08.md)
- RG-formalism context (external, registered): [`BBS_RG_BANACH_CONTRACTION_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-10`](BBS_RG_BANACH_CONTRACTION_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-10.md)
- Standard math/method (not imports): matrix-unit divisibility for `*`-homomorphisms (Bratteli); Stinespring/Kraus compressions; Kadanoff block-spin as truncating map.
