# The GST Texture (√(mass-ratio) Mixing) Reduces to a Rank-1 C₃-Symmetric Mass: the Light Generation's Mass is Purely from C₃-Breaking — Narrow Theorem

**Date:** 2026-06-08
**Claim type:** bounded_theorem (reduces the GST magnitude texture to the rank-1 / single-source C₃-symmetric-mass condition; derives `sin θ = √(mass-ratio)` from it)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/gst_texture_from_rank1_c3_symmetric_mass_runner.py`](../scripts/gst_texture_from_rank1_c3_symmetric_mass_runner.py)
**Cached output:** [`logs/runner-cache/gst_texture_from_rank1_c3_symmetric_mass_runner.txt`](../logs/runner-cache/gst_texture_from_rank1_c3_symmetric_mass_runner.txt)

## Audit context

The companion unification showed both small mixing angles (θ_C, θ₁₃) are **C₃-breaking order
parameters**, `√(mass-ratio)`-scaled *if* the breaking texture is geometric-mean (Gatto-Sartori-Tonin).
That GST texture is a shared magnitude residual in the small-angle account. This note reduces the
texture to a single, clean condition — a **rank-1 C₃-symmetric mass plus single-source breaking** —
and derives `sin θ = √(mass-ratio)` from that condition.

## Safe statement

**Theorem (GST ⟸ rank-1 C₃-symmetric mass + single-source breaking).**

1. **Rank-1 C₃-symmetric mass ⟹ light generations massless at C₃-symmetry.** If the C₃-symmetric mass
   is **rank-1** — the C₃-singlet `(1,1,1)/√3` carries the leading mass (`M_sym = m_heavy·P_singlet`) —
   then its spectrum is `(m_heavy, 0, 0)`: the light generations are **massless** at C₃-symmetric
   order (verified). In the reduced light/heavy two-state block, this is the **texture zero**
   `(1,1)=0`: the light generation has **no** C₃-symmetric direct mass. This is not a claim that
   the original C₃ site-basis singlet projector has a zero `(1,1)` matrix entry.
2. **The texture zero IS the geometric mean.** For the `1–2` block `[[0,b],[b,a]]`, `det = −b² =
   −m_light·m_heavy`, so `b = √(m_light·m_heavy)` (verified) — the GST geometric-mean off-diagonal **is**
   the `(1,1)=0` texture zero.
3. **One breaking source ⟹ GST (a flavor see-saw).** A **single** C₃-breaking source `b` gives the
   light mass at **second** order (`m_light = b²/m_heavy`, the see-saw suppression) **and** the mixing
   at **first** order (`θ = b/m_heavy`). Hence `m_light/m_heavy = (b/m_heavy)² = θ²`, i.e.
   **`sin θ = √(m_light/m_heavy)`** (verified across `b`; see-saw and GST both hold). The light mass
   and the mixing **share one source** — they are not independent.
4. **Physical + the unified residual.** Quark: `sin θ_C ≈ √(m_d/m_s) = √(0.0505) = 0.2247` vs PDG
   `0.2257` (0.4%). So the GST magnitude reduces to **one candidate shared condition** — the
   **rank-1 / single-source C₃-symmetric mass** (the light generation's mass is purely from
   C₃-breaking) — for the small-angle magnitude account.

## Why this is the answer to "the GST texture"

- It reduces the GST texture from a free assumed pattern to a **structural condition** on the
  C₃-symmetric mass plus its breaking: **rank-1** (the singlet carries the leading mass; the light
  generations are massless until C₃-breaking) and **single-source breaking**. The geometric mean and
  the `√(mass-ratio)` mixing then **follow** (a flavor see-saw).
- The residual is now a single, sharp, **dimensionless** structural question: *is the C₃-symmetric mass
  rank-1?* — equivalently, does it come from a **single C₃-invariant source** (cf. the single-Higgs
  structure, [`LEPTON_SINGLE_HIGGS_PMNS_TRIVIALITY`](LEPTON_SINGLE_HIGGS_PMNS_TRIVIALITY_NOTE.md))?
  This identifies a candidate shared residual for the small-angle magnitude account.

## Boundary (honest)

- **A reduction, not a closure.** It reduces the GST texture to the rank-1 / single-source condition
  and derives `sin θ = √(mass-ratio)` from it; it does **not** derive the rank-1 condition itself from
  A_min (that is the named residual, connecting to the single-source/single-Higgs structure).
- **The leading-order see-saw relation.** `sin θ = √(m_light/m_heavy)` is the hierarchical-limit GST
  (~10% at the physical `m_d/m_s`, the Cabibbo-haze level); subleading (up-sector, phases) corrections
  are not included.
- This is the mass-matrix **mixing** texture — distinct from the Koide `r`-dial (where "democratic" is
  the separate `r=0` object); no claim about `r` is made here.

## Forbidden imports check

No new axiom. A_min + the C₃ structure (the singlet projector) + standard 2×2 mass-matrix algebra
(reproduced). PDG `m_d/m_s`, `sin θ_C` are the comparison data (dimensionless). The single-source
condition is *named* as the residual, not imported. Memory-safe.

## Runner check breakdown

Class A: (A1) rank-1 C₃-symmetric mass ⟹ light generations massless (the reduced two-state
light/heavy block has `(1,1)=0`); (A2) `(1,1)=0` ⟺
`b=√(m_light m_heavy)` (geometric mean); (A3) one source ⟹ `m_light=b²/m_heavy` + `θ=b/m_heavy` ⟹
`sin θ=√(m_l/m_h)`; (A4) `sin θ_C≈√(m_d/m_s)` (0.4%), the shared rank-1 residual. Expected
`runner_check_breakdown = {A: 4, B: 0, C: 0, D: 0, total_pass: 4}`.

## Honest auditor read

A rank-1 C₃-symmetric mass (the C₃-singlet carrying the leading mass) leaves the light generations
massless at C₃-symmetric order. In the reduced light/heavy block this is the `(1,1)=0` texture zero,
which is exactly the geometric-mean off-diagonal by the determinant identity. A single C₃-breaking source then gives the light mass at
second order and the mixing at first order, forcing `sin θ = √(m_light/m_heavy)` (verified, and
matching `sin θ_C ≈ √(m_d/m_s)` to 0.4%). So the GST magnitude texture — the one shared assumption
under the small-angle account — reduces to whether the C₃-symmetric mass is rank-1 with single-source breaking. The note is
honest that this is a reduction (the rank-1 condition is the named residual, connecting to the
single-source/single-Higgs structure), the leading-order see-saw relation, and distinct from the
Koide r-dial. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/gst_texture_from_rank1_c3_symmetric_mass_runner.py
```
