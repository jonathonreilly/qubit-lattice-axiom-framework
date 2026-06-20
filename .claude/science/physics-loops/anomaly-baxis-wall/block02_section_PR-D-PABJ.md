# Block02 Section — Route PR-D (P-ABJ internal: KD index vs χ)

**Edge:** P-ABJ / P1 of keystone
`anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26`
(fanout 1105). The internal-route open ray re-targeted by retained
`ABJ_RESIDUAL_GW_NOT_NECESSARY`: "exhibit a framework-internal `χ≠0`/`Q≠0`
background on which the taste-singlet index is nonzero."

**Route:** PR-D — the campaign's **first `χ≠0` runner**. Block01's square-block
no-go is tight on the hypercubic **1-skeleton GRAPH** (ε-index = 0). PR-D tests
the **OFF-graph rays**: the taste-singlet Kähler–Dirac (Dirac–Kähler) index on
the **FULL cochain complex** (0-cells ⊕ 1-cells ⊕ 2-cells ⊕ …, graded by
form-degree parity `(−1)^k`), over a FAMILY of complexes from a balanced flat
torus (`χ=0`) to a curved closed `χ≠0` complex (tetrahedron boundary = S², `χ=2`).
Does the index track `χ` (Catterall–Butt: KD index = `χ`)?

**Runner:** `scripts/frontier_abj_pabj_kd_index_chi_tracking_2026_06_20.py`
**Cache:** `logs/runner-cache/frontier_abj_pabj_kd_index_chi_tracking_2026_06_20.txt`
(+ `.json`). **Result: TOTAL: PASS=45 FAIL=0.**

## Scope and absorbed authority (cited; recomputed in-tree, not rebuilt)

A_min = Lattice (cubic `Z³` nearest-neighbor adjacency) + Quantum + Record, plus
the approved primitives: `kinetic_isotropy_primitive` (emergent time edge grained
on the SAME footing as the spatial cubic edge ⇒ a hypercubic/cubical `Z³×Z_τ`
complex), `scale_reference_primitive` (units only), `realized_state_primitive`
(slot only). None supplies a gauge field, a boundary, a non-cubic cell, or a
curved geometry.

Absorbed (NOT rebuilt) — recomputed in-tree in Part 0 / referenced as context:
- `ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30` — **retained_no_go**.
  Governs the staggered ε-graded index on the **1-skeleton GRAPH**: balanced
  sublattices ⇒ `B` square ⇒ `A_t = 0`. Part 0 reproduces `A_t = 0` on
  `(4,2,2,2)` and `(4,4,4,4)` (`max|A_t| ≤ 4.7e-15`).
- `ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28` —
  **retained_bounded**. Re-targets `(P1')` to the `χ≠0` background — the exact ray
  PR-D builds a real object for.
- Block01 PR `frontier_abj_internal_chi_nonzero_index_escape` (PASS=34) — its R-A
  (imbalance ⇔ all-odd ⇔ grading destroyed, on the GRAPH) and its open-3×3 graph
  index = 1 non-vacuity control are reproduced (P4) and contrasted.

**Literature CONTEXT-ONLY (mechanism verified in-tree, NOT cited as A_min
authority):** Catterall & Butt — Kähler–Dirac fermion index on a simplicial
complex = Euler characteristic `χ`; Becher–Joos / Rabin — Dirac–Kähler equation
as a sum of differential forms, index = `χ`. **Honesty discipline:** an imported
index theorem is NEVER presented as an A_min derivation — Part 1 recomputes the
identity in-tree (combinatorial Hodge Laplacian + graded kernel + `f`-vector),
and the load-bearing verdict rests on the in-tree honesty guard, not the citation.

## The key reframe vs block01: a DIFFERENT object

Block01 governed the staggered ε-graded **spectral** index
`A_t = Tr(ε e^{−tD†D})` on the **1-skeleton** (sites + nearest-neighbor edges).
PR-D builds the **Kähler–Dirac index** of `D_KD = d + d†` on the **full exterior
cochain algebra**, graded by `Γ = (−1)^k`. By Hodge, this index
`= Σ_k (−1)^k b_k = Σ_k (−1)^k f_k = χ`. This is the taste-singlet (Dirac–Kähler)
object the GW-not-necessary note's re-target points at, and it is a strictly
larger object than block01's graph index (it sees plaquettes, cubes, … and the
complex's topology, not just bipartiteness).

## What PR-D found

### P1 — KD index = χ identity verified in-tree (NOT imported blind)
On point, interval, `C₅`/`C₈` (S¹), filled triangle (disk), tetra-boundary (S²),
cubical `T²`: KD graded-kernel index equals `χ` (from the `f`-vector) equals
`Σ(−1)^k b_k` (from the combinatorial Hodge Laplacian). The tetra-boundary S²
yields Betti `{b₀=1, b₁=0, b₂=1}`, `χ=2`, **KD index = 2**.

### P2 — THE FAMILY: the index TRACKS χ (first χ≠0 of the campaign)
Flat `T²` (2×2, 3×3, 4×4): KD index = 0. **Curved closed S²: KD index = +2.**
The taste-singlet KD index is **nonzero exactly on the curved closed surface** and
tracks `χ` across the family. This is a genuine, non-vacuous **escape MECHANISM**:
the GW-not-necessary re-target ray DOES have a real witness — the index becomes
nonzero on a `χ≠0` complex, with the `χ=2` read off S²'s OWN combinatorics
(`f₀−f₁+f₂ = 4−6+4`), **no injected gauge twist anywhere** (honesty guard vs
block01 R-C: there is no gauge field at all in Part 2).

### P3 — CONTROL: the FULL cubical complex on `Z³×Z_τ` has χ = 0
Block01 used the 1-skeleton graph. PR-D builds the **full cubical cochain
complex** (vertices, edges, plaquettes, cubes, hypercubes) on `Z³` tori and on
the 4d `Z³×Z_τ` A_min substrate (the cubical torus WITH the kinetic-isotropy
emergent time edge). Result: `χ = 0` at every size, in every dimension
(e.g. `(2,2,2,2)`: `f = {16,64,96,64,16}`, `χ=0`; KD index on the full cubical
`T³` = 0). **Adding higher cells to block01's graph does NOT create χ** — the
cubical torus is flat.

### P4 — off-substrate non-vacuity witnesses (two distinct mechanisms)
- Block01's control reproduced: open 3×3 **GRAPH** staggered index `= N₊−N₋ = 1`
  (needs a BOUNDARY A_min withholds).
- PR-D's KD witness is a **different non-A_min structure**: S² is **CLOSED**
  (every edge bounds exactly 2 faces — no boundary) yet has KD index = 2. The
  driver is **curvature/topology**, not a boundary. So the two escapes (open
  boundary vs closed curvature) are genuinely distinct; neither is A_min-native.

### P5 — HONESTY GUARD (decisive): the χ≠0 geometry is ADMITTED, not native
Enumerated **28** A_min-native cubical tori (dim 2..4, edge lengths in {2,3}):
**every one has `χ = 0`.** Structural reason: a cubical torus is a product of
circles and `χ` is multiplicative, `χ(S¹)^n = 0^n = 0`, independent of size. The
S² (`χ=2`) is **not** a product of circles and **not** a cubic torus — A_min's
Lattice axiom (cubic nearest-neighbor adjacency) + kinetic isotropy supply ONLY
flat cubical complexes. **Therefore the `χ≠0` geometry is admitted, not native.**
The admitted datum is the **curved GEOMETRY itself** (a combinatorial `f`-vector
invariant with zero gauge field) — categorically distinct from block01 R-C's
injected gauge topological charge `Q`.

## The wall, sharpened and re-localized

Block01 localized the P-ABJ internal wall on the GRAPH: `χ≠0 ⇔ all-odd ⇔
chirality grading destroyed` (mutually exclusive). PR-D shows that the **full
cochain complex does NOT rescue the route** and **re-localizes the wall to a
cleaner, more fundamental statement:**

> The taste-singlet KD index genuinely tracks `χ` and is nonzero on a curved
> closed complex (escape mechanism is REAL, witnessed at index = +2 on S²), but
> **every closed complex A_min supplies is a flat cubical torus with `χ = 0`**.
> The `χ≠0` background the GW-not-necessary note re-targets to **exists, but only
> as an ADMITTED curved geometry** — A_min's flat-cubic Lattice axiom withholds
> it. The wall is no longer "the index is structurally always 0"; it is
> precisely **"A_min's Lattice axiom is flat-cubic; the consumer must ADMIT a
> curved (χ≠0) geometry,"** a single named geometric admission.

This is **sharper** than block01 because (a) it is the full-complex (not graph)
object, closing the "maybe the graph is too small / maybe higher cells help" gap;
(b) it identifies a concrete, non-vacuous nonzero index (the campaign's first
`χ≠0`), so the wall is demonstrably NOT vacuity; and (c) it pins the residual to a
single admission — the **flat-cubic Lattice axiom** — rather than a diffuse "no
internal route."

## Honest status

- **Internal route: SHARPER NO-GO (most-likely outcome realized).** The KD/χ index
  IS the right object and IS nonzero off-substrate (S², index +2 — first `χ≠0` of
  the campaign), but no A_min-native closed complex has `χ≠0` (28 cubical tori, all
  `χ=0`, by the `χ(S¹)^n=0` product law; full cubical `Z³×Z_τ` complex `χ=0`). The
  `χ≠0` geometry is **admitted**, not native. **No non-vacuity crack** — the small
  chance the route mentioned did not materialize: the geometry that carries the
  index is outside A_min's flat-cubic Lattice axiom.
- **Where the index becomes nonzero:** on the curved closed S² (tetra boundary),
  KD index = `χ = 2`. **Native?** No — A_min supplies only flat cubical complexes.
  **Admitted.**
- **External premise unchanged:** P-ABJ/P1 (the Adler–Bell–Jackiw
  anomaly-to-inconsistency implication, B2) remains a categorically external
  registered admission, not derivable from A_min by policy. PR-D does not touch it;
  it works only the internal-route open ray.

## What this unlocks on the 1105 cone

No audit movement claimed (independent audit lane is sole authority; nothing under
`docs/audit/**` touched). The audit-relevant content for the consolidation note:

1. **Re-localize the P-ABJ internal-route wall** from block01's GRAPH framing
   (`χ≠0 ⇔ grading destroyed`) to the cleaner full-complex statement: **the wall
   is the flat-cubic Lattice axiom**; a `χ≠0` taste-singlet KD index is a real,
   non-vacuous escape that requires an ADMITTED curved geometry. This converts a
   diffuse "internal route walled" into a **single named geometric admission**
   the consumer would have to make — easier for the audit lane to fence and to
   state as a no-go escape condition.
2. **Non-vacuity is now witnessed in-tree** (index = +2 on S²), satisfying the
   exercise N7 steelman ("a curved/non-hypercubic framework complex witnesses a
   nonzero index") with a concrete object — and answering it: **yes such a complex
   exists, no it is not A_min-native.** The exercise-skill flag on the P-ABJ
   internal wall is dischargeable: the steelman is settled, not open.
3. **Control result** (full cubical complex on `Z³×Z_τ` has `χ=0`) closes the
   "block01 only used the 1-skeleton" gap, so the consolidated obstruction note can
   state the internal route is walled at the level of the **full cochain complex**,
   not merely the graph.

## Firewall / forbidden-surface attestation

New artifacts only: this section, the runner
`scripts/frontier_abj_pabj_kd_index_chi_tracking_2026_06_20.py`, and its caches
(`.txt` + `.json`). **No file under `docs/audit/`, `docs/publication/`,
AUDIT_LEDGER/QUEUE, MISSING_DERIVATION_PROMPTS was edited.** `docs/audit/data/`
was read-only. No row/effective status set; no audit verdict asserted. Independent
audit required before any effective-status movement. The keystone and parent are
NOT cited as authority for any load-bearing fact — every load-bearing claim
(square-block graph index = 0; KD index = χ; the family tracking; the cubical
control; the native-flatness enumeration) is recomputed in-tree.
