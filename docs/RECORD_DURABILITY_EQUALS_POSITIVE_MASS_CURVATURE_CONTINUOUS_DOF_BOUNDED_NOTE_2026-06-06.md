# Record Durability Equals Positive Mass-Curvature for a Continuous Degree of Freedom — Bounded Note

**Date:** 2026-06-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem — a narrow equivalence for a **continuous** degree of freedom, **at linear
(leading-curvature) order**. From the Record axiom's durability clause
([`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md): *"Durable means fixed once registered: the
recorded outcome does not change"*), a continuous registered value is **fixed against infinitesimal perturbations**
⟺ it has a linear restoring force `−m²ε` ⟺ the leading energy curvature is positive ⟺ `m² > 0`. Hence a
**symmetry-protected massless** continuous degree of freedom (gauge/Goldstone, flat to *all* orders) is **not a
durable record** (it is free to displace), and the gauge/relative-frame sector — whose displacements are zero-cost
by closed-loop invariance — is the canonical unrecorded-and-massless case. (A fine-tuned `m²=0` minimum pinned only
at higher order, e.g. `φ⁴`, is durable yet massless and is **explicitly excluded** — see step 2 and the steelman.)
**Claim scope:** this derives the **massless ↔ unrecorded split** for continuous degrees of freedom; it is a
re-reading/identification, **not** a new mass spectrum and **not** a derivation of any mass *scale*. It does **not**
cover discrete/topological records (a quantized winding/`K`-CPT-orbit label/`θ`-sector is fixed by *quantization*,
durable without a restoring curvature — a separate durability channel). The standard field-theory identification
`m² = curvature of the energy at the minimum` (Coleman) and the Higgs/Goldstone/Stückelberg mass-from-vacuum
mechanism are **comparators only**, never derivation inputs.
**Status authority:** independent audit lane only. No effective-status change; **Independent audit required.**
**Runner:** [`scripts/audit_companion_record_durability_positive_mass_curvature_exact.py`](./../scripts/audit_companion_record_durability_positive_mass_curvature_exact.py)

## The equivalence

Let a continuous degree of freedom carry a registered value at a minimum `φ₀` of its local energy `V`. Reproven in
the runner (sympy, 9/9):

1. **Cost to displace is the curvature.** At a minimum `V'(φ₀)=0`, so the energy cost to displace by `ε` is
   `V(φ₀+ε) − V(φ₀) = ½·V''(φ₀)·ε²`, and `V''(φ₀) = m²` (the mass-squared **is** the energy curvature). (Runner
   (1).)
2. **Linear durability ⟺ positive curvature.** "Fixed once registered" means the value cannot drift for free under
   an *infinitesimal* perturbation. The leading penalty is `½m²ε² + O(ε⁴)`; the **linear restoring force** is
   `−V''(φ₀)·ε = −m²·ε`, which is nonzero (a restoring force against arbitrarily small displacement) **iff
   `m² > 0`**. So a record stable at **linear order** is **massive**; a value with `m² = 0` has **no linear
   restoring force**. (Runner (2),(4a).) **Caveat (the marginal exception).** `m² = 0` does *not* by itself mean
   "free to all orders": a fine-tuned flat-quadratic minimum with higher-order pinning (e.g. `V = λφ⁴`, where
   `V''(0) = 0` but a displacement still costs `λε⁴`) is durable yet massless — restored only *super-linearly*.
   The clean biconditional is therefore **linear** (leading-curvature) durability ⟺ `m² > 0`, with this
   higher-order-pinned case excluded. It does **not** arise for the physically-relevant massless content: the
   **symmetry-protected** massless directions (gauge connections, Goldstones) are flat to **all** orders — see
   step 3 — hence genuinely free to displace, hence genuinely unrecorded. (Runner (4b) exhibits the `φ⁴`
   exception explicitly.)
3. **The gauge sector is the canonical zero-cost case.** A closed-loop holonomy (a record) is **invariant** under
   the relative-frame shift `θ_xy → θ_xy + (λ_x − λ_y)` (the shift telescopes to `0`). So a gauge displacement is
   **zero-cost**: the connection is free to displace ⟹ **unrecorded** (the relative-frame freedom of
   [`COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md`](./COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md)
   and
   [`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`](./DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md))
   ⟹ **massless**, consistent with the existing tree-level gauge-masslessness theorem
   ([`GLUON_TREE_LEVEL_MASSLESSNESS_THEOREM_NOTE_2026-05-02.md`](./GLUON_TREE_LEVEL_MASSLESSNESS_THEOREM_NOTE_2026-05-02.md):
   `½m²A²` is gauge-invariant only at `m=0`). (Runner (3).)
4. **The converse (for symmetry-protected massless directions).** Contrapositive of (2) at linear order:
   **massless** (zero curvature) ⟹ no linear restoring force. For a direction flat to **all** orders — the
   gauge/Goldstone case of step 3 — this is genuinely free-to-displace ⟹ not fixed ⟹ not durable ⟹ **not a record**
   (unrecorded). (Runner (4a); (4b) shows the excluded `φ⁴` marginal case.)

## What this is, and what it is not

| | statement | status |
|---|---|---|
| **linearly** durable record ⟺ `m² > 0` | from durability + linear restoring force `−m²ε` | **derived** (runner 9/9) |
| symmetry-protected massless DOF ⟹ unrecorded | gauge/Goldstone directions are flat to **all** orders ⟹ free | **derived** |
| the massless ↔ unrecorded **split** | the gauge/relative-frame + flat-to-all-orders sector is exactly the unrecorded one | **derived (re-reading)** |
| `m²=0` with higher-order pinning (`φ⁴`) | durable yet massless — a fine-tuned marginal case | **excluded** (not symmetry-protected; runner exhibits it) |
| discrete/topological records | fixed by **quantization**, durable without a continuous mass | **out of scope** (separate channel) |
| the mass **scale** (why `v ≠ 0`) | not addressed | **open** (separate) |
| a new mass spectrum / new numbers | none claimed | **not claimed** |

**Net.** For a continuous degree of freedom, *being a record durable against infinitesimal perturbations* and
*being massive* are the same condition — a strictly positive **leading** (quadratic) energy curvature. The
genuinely-unrecorded sector (gauge/relative-frame and Goldstone directions, flat to all orders, zero-cost-to-
displace) is therefore exactly the massless one. This is the equivalence stated narrowly and reproven from
primitives; it re-reads the framework's existing gauge-masslessness and Record-invariance results under one
identity, and adds no axiom, import, or number.

## No-go discipline / steelman

**Strongest objection (this just renames the Higgs/Goldstone mechanism).** The *mechanism* (mass = curvature of the
vacuum energy) is standard, and is cited as a comparator, not derived here. The **narrow new content** is the
*equivalence to the Record axiom's durability clause*: that "fixed once registered" is, for a continuous degree of
freedom, the same condition as positive curvature — so masslessness and being-unrecorded are the same property, and
the gauge sector's masslessness is the zero-cost-displacement (unrecorded) case. **Second objection (discrete
records).** Accommodated explicitly: quantized/topological records are durable by discreteness, not curvature, and
are out of scope. **Third objection (a massless `φ⁴` minimum is durable).** Granted and load-bearing: `m² = 0` with
higher-order pinning (`V = λφ⁴`) is durable yet massless, so the biconditional is **linear** (leading-curvature)
durability ⟺ `m² > 0`, with that fine-tuned case excluded. It does not arise for the physically-relevant massless
content, which is **symmetry-protected** (gauge/Goldstone) and therefore flat to all orders — the only case the
gravity application (step 3, and the graviton note) invokes. **Fourth objection (the scale).** Granted — only the
split and ratios follow from the curvature sign; the absolute scale is untouched. The equivalence (Parts 1–4)
stands within the stated linear, continuous-DOF, symmetry-protected scope.

## Forbidden-import / reprove-and-cite

All facts (`cost = ½V''ε²` at a minimum; `V''(φ₀)=m²`; the closed-loop relative-frame shift telescopes to `0`; the
contrapositive chain) are **reproven** from elementary primitives in the runner (sympy, 6/6). Coleman's
`m² = ` curvature-at-the-minimum and the Higgs/Goldstone/Stückelberg mechanism are **comparators** only. No PDG
values; no mass scale is consumed or produced.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md`](./COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md)
- [`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`](./DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md)
- [`GLUON_TREE_LEVEL_MASSLESSNESS_THEOREM_NOTE_2026-05-02.md`](./GLUON_TREE_LEVEL_MASSLESSNESS_THEOREM_NOTE_2026-05-02.md)

**Independent audit required.** This note asserts no effective-status change and changes no Tier-A registry entry.
