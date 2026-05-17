# Block 05 SCORECARD — g_bare C-iso (a_τ=a_s) Convention-Orbit Invariance

**Date:** 2026-05-17
**Lane:** g_bare (third in trio L3a ✓ L3b ✓ C-iso ✓ this)
**Branch:** `physics-loop/g-bare-c-iso-block05-2026-05-17`
**Honest status:** **bounded_theorem CLOSED (positive)** on the canonical LO
Trotter dictionary scope.

## Deliverables

- **Source theorem note:** `docs/G_BARE_C_ISO_CONVENTION_ORBIT_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-17.md`
- **Audit-companion runner:** `scripts/audit_companion_g_bare_c_iso_convention_orbit_invariance_exact_2026_05_17.py`
- **Cached output:** `logs/runner-cache/audit_companion_g_bare_c_iso_convention_orbit_invariance_exact_2026_05_17.txt`
- **V1–V5 written before PR:** `.claude/science/physics-loops/filter-excluded-positive-closures-2026-05-17/blocks/block05/V1_V5.md`

## Runner result

```
TOTAL  : PASS = 183, FAIL = 0
```

(Expected PASS >= 65 per source-note disclosure; achieved 183 due to
parametric sweep over ξ ∈ {1/16, 1/4, 1, 4, 16, 64} × g_bare ∈ {1/2, 1,
√3, π} × N_c ∈ {2, 3, 4} with mpmath cross-check at 50 dps.)

## What closed

Closure: the W-substitution algebra for `g_bare² = 1` involves **no
lattice-spacing symbols** (a_τ, a_s, ξ) in any of its load-bearing
inputs (W1), (W2), (AN), (NC). On the canonical leading-order Trotter
dictionary, the C-iso convention orbit (a_τ ≠ a_s, parameterized by
ξ = a_s/a_τ ∈ (0, ∞)) routes its full degree of freedom into the
anisotropic Wilson coefficient doublet (β_σ, β_τ) via a bijection
(g_bare, ξ) ↔ (β_σ, β_τ) with:

- **Geometric-mean direction** (g_bare): `sqrt(β_σ · β_τ) = 2 N_c / g_bare²`
  — exactly ξ-independent.
- **Ratio direction** (ξ): `β_τ / β_σ = ξ²` — fully carries the C-iso
  DOF, never appears in g_bare expression.

Conclusion: the parent W-substitution result `g_bare = 1` (positive
branch, N_c = 3) is invariant along the C-iso orbit at any ξ.

## What does NOT close

- C-iso (a_τ = a_s) itself remains an admitted convention per
  `C_ISO_DERIVED_THEOREM_NOTE_2026-05-07_w3.md` (`open_gate`).
  This row only proves the choice is convention-routing **for g_bare
  specifically**, not that the convention is uniquely forced.
- Spatial plaquette expectation `<P_σ>(g², ξ)` IS ξ-dependent at
  O(s_t²) per `C_ISO_SU3_NLO_CLOSURE_BOUNDED_NOTE_2026-05-08_su3nlo.md`.
  The bare-coupling orbit invariance does not extend to
  expectation-value-level observables.
- NLO Trotter dictionary corrections (O(g²) shifts in (β_σ, β_τ))
  are not addressed; the bounded_theorem framing reflects the LO
  truncation.

## Three-DOF orthogonality (distinctness from L3a, L3b)

The block runner explicitly verifies that the three named convention
DOFs (L3a trace-surface, L3b overall scalar, C-iso lattice-spacing
ratio) act independently:

- Block 03 L3a: rescaling T_a → c T_a violates Tr(T_a T_b) = δ_ab/2 by
  c², shifts β by c². Orthogonal to ξ.
- Block 04 L3b: rescaling F → λ F scales c0 → λ² c0. Orthogonal to ξ.
- Block 05 C-iso (this row): doublet (β_σ, β_τ) parameterized by
  (g, ξ). Orthogonal to (c, λ).

All three orbits leave the canonical closure `g_bare = 1` invariant
on their respective canonical surface.

## Next-block recommendation

**Recommended:** move from the named-admission trio to W1.exact engineering
frontier (the remaining open frontier per the bridge-gap fragmentation
memory). Specifically:

- The C_ISO_SU3_NLO_CLOSURE_BOUNDED_NOTE's named compute frontier is
  the next live boundary: ε_witness ~3×10⁻⁴ on `<P>_KS` requires
  ξ ≳ 430 at 16³ × T_t (GPU MC) or analytic SU(3) NNLO closure of
  the c_3 coefficient. The NNLO bounded note exists; the action item
  is to derive c_3 in closed form rather than asymptotic-fit it.

**Alternative recommendation:** if continuing in the convention-orbit
mode, the next narrowest admission is the **Wilson plaquette action
form** itself (carried by `G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md`
Claim 3) — i.e. the equivalence-class of Wilson vs Symanzik-improved
actions under tree-level matching for the bare coupling specifically.
This is structurally analogous to the C-iso closure here but on the
action-form DOF.

## Hard-rules compliance

- A_min only: ✓ (only class A algebraic substitution)
- No fitted/observational/literature data: ✓
- No PDG numerical comparator: ✓
- No audit-data touches: ✓ (read-only check on audit ledger)
- No merge, no main push: enforced by PR-only workflow
