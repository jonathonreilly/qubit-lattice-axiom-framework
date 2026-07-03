# Color Link-Index Routing via Cross-Site Matter Bilinear Unitarization

**Date:** 2026-06-08
**Type:** bounded theorem (a link-index-routing existence construction, conditional on the supplied color carrier)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_color_link_index_routing_matter_bilinear_unitarization_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_color_link_index_routing_matter_bilinear_unitarization_2026_06_08.txt`
**Status:** source proposal. The construction and transformation laws are
finite-dimensional algebra checked by the runner (`PASS=11 FAIL=0`). Authority
role: source proposal; audit lane sets status.

## The named residual this addresses

The color residual map
([`COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05`](COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md))
names as a live residual: *"one must still assign quark matter to the symmetric-base
fundamental and **route that color index onto links**"* — and **prunes** the candidate
"primitive one-qubit link algebra already supplies color"
([`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md):
a single qubit link natively carries only `u(2)`, no faithful `su(3)`). The QUANTUM axiom
supplies **one qubit per site and no edge degrees of freedom**, so a fundamental
`SU(3)`-valued link variable has no native carrier. Where, then, can the color index on
links live?

## Verdict

**On the cross-site matter bilinears — natively.** GIVEN the supplied per-cube color
carrier `C³` (the taste-cube symmetric base; the `MR_color` residual — the **same**
conditionality as the sister carrier notes), the cross-site matter bilinear

```
    M(x,y)_ij = Σ_α ψ_α(x)_i ψ_α(y)_j*        (occupied matter modes α)
```

carries the link transformation law `M → g_x M g_y†` **natively**, and its **polar
unitarization** `U = M (M†M)^{−1/2}` is an exactly-unitary link variable obeying the same
law; the determinant reduction `S = U·det(U)^{−1/3}` is `SU(3)`-valued and obeys the law up
to the `Z₃` center. Composite Wilson loops built from these links are **exactly invariant
under independent local color rotations**. The routing requires **no edge degree of freedom,
no quantum-link ontology, and no new axiom** — it lives on objects the matter sector already
supplies.

**Precondition (load-bearing):** the construction is defined **only when the
cross-site bilinear is full rank**. This requires at least three independent
occupied matter modes, and generic three-mode configurations pass the rank
control (Part 4). Lower-occupancy or otherwise rank-deficient states do not
carry this composite link — this is a physical occupancy/rank precondition on
*which states carry a link*, not a mere edge case.

**Fermionic reading:** the `ψ_α` are occupied-**mode amplitudes** (c-numbers). For fermionic
matter the load-bearing object is the cross-site **one-body density block**
`⟨a†_{y,j} a_{x,i}⟩`, which transforms by the identical law `→ g_x ⟨·⟩ g_y†` and whose rank
is controlled by the occupied single-particle modes. Full rank still requires
three independent occupied color directions. The c-number mode sum above is a
faithful finite-dimensional model of that block; anticommutation does not alter
the transformation law or the rank boundary.

## What the runner verifies (`PASS=11 FAIL=0`)

1. **The bilinear is a native link-law carrier:** `M → g_x M g_y†` under per-site rotations
   (100 configs, dev `10⁻¹⁵`).
2. **Polar unitarization preserves the law:** `U(g_x M g_y†) = g_x U(M) g_y†`, `U` exactly
   unitary (dev `10⁻¹²`) — because `M†M → g_y (M†M) g_y†` so the normalizing factor
   co-transforms.
3. **SU(3) reduction:** `det(S)=1` exactly; the law holds **up to the `Z₃` center** (the
   canonical det-branch ambiguity — the physically meaningful center structure of lattice
   gauge theory, stated, not hidden).
4. **Rank boundary (control):** a **single**-mode bilinear has rank 1 and **cannot** be
   unitarized; a full-rank bilinear is required, which in turn requires at least three
   independent occupied modes (generic three-mode draws are full-rank, 50/50).
5. **Teeth:** a basis-dependent unitarization (QR/Gram–Schmidt) **violates** the law
   (violation `1.35`) — the polar map's covariance is special, not generic.
6. **Composite Wilson loops are exactly locally gauge-invariant** (dev `10⁻¹⁴`); an open
   composite link is not — the gauge-invariant content is the closed loops, as it must be.

## Honest boundaries (load-bearing, named)

- **Conditional on the supplied `C³` color carrier** (`MR_color`): this is *not* an
  axiom-level derivation of color; it inherits exactly the sister notes' conditionality.
- **Full-rank bilinear** is required; this needs at least three independent occupied modes,
  while rank-deficient matter configurations remain a real boundary of the construction
  (Part 4 control).
- **`Z₃` center ambiguity** in the SU(3) reduction (Part 3).
- **No dynamics.** This is a *kinematic* carrier/routing existence result. It supplies **no
  generator, rate, or arrow** — the undelivered continuous-time gauge-link dynamics (the
  ST1/ST2 same-wall residual, `ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE` capstone)
  is **untouched**.
- **No selection.** It does **not** claim the framework's physical link *is* this composite —
  that identification belongs to the open **gauging-selection** gate
  ([`GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08`](GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md)).
  It proves **existence** of a native carrier, pruning only the branch "an edge-DOF import is
  *required* for the link-index routing."
- **Does NOT discharge ADM-1** (the local-frame redundancy gate): frame-referencing
  cross-site operators still exist; this construction is frame-*covariant*, compatible with
  either reading. **No ranking of gates is asserted.**

## Relation to the wall

The same-wall capstone reduced the interacting-gauge foundation to one undelivered input —
a continuous-time gauge-link dynamics. This note shrinks that input's *kinematic* footprint:
the link variable itself needs no new ontology (it can live on matter bilinears the framework
already has), so the undelivered piece is genuinely only the **dynamics** (generator + rate +
the frame-redundancy reading), not an additional missing carrier. **This footprint-shrink is
itself conditional on the supplied `C³` carrier and the full-rank bilinear precondition; it
is an existence statement, not a discharge of any gate.** If the dynamics gate ever closes,
the matter sector's own evolution induces the composite link's evolution through this
construction — but *that* statement is conditional future work, not claimed here.

## Cross-references

- The named residual + supplied carrier: [`COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05`](COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md)
- The qubit-link `u(2)` boundary (respected, not enlarged): [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md)
- The endpoint-dressing profile (a different, supplied-link-end model): [`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md)
- The gauging-selection open gate (untouched): [`GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08`](GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md)
- The dynamics wall (untouched): `ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE_NARROW_THEOREM_NOTE_2026-06-08` (PR #3394)
- Color algebra dependency: [`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md).
  Consult the audit ledger for its current status; this source note does not set or update it.
- Standard math cited for method only: polar decomposition; composite/auxiliary-field gauge construction (CP^{N−1} sigma models; hidden local symmetry) as the literature analogue.
