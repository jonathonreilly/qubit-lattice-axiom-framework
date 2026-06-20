# block05 — Route R-KINFORM-N2b (clause N2b: form↔spacing bridge)

**Date:** 2026-06-20
**Clause:** N2b (absolute clock unit `a_τ`)
**Route id:** R-KINFORM-N2b
**Outcome:** `confirms_wall_sharper` — N2b STAYS OPEN; the no-go gains a new,
independent, sharper column.
**Runner:** `scripts/single_clock_kinform_spacing_bridge_n2b_2026_06_20.py`
**Cached output:** `logs/runner-cache/single_clock_kinform_spacing_bridge_n2b_2026_06_20.txt`
**Scorecard:** `TOTAL: PASS=16 FAIL=0`

---

## The route (the tempting-but-guarded one)

Exercise-One hoped that `kinetic_isotropy_primitive` (form isotropy `c_t = c_s`)
plus `scale_reference_primitive` (`a_s = 1/M_Pl`) would jointly pin the absolute
clock step `a_τ` and discharge N2b. The HARD STOP is registry rule 5: the
kinetic-isotropy note (`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`, lines
53–54, 75–77) **explicitly disavows the spacing ratio** — it grants only the
FORM ratio `c_t/c_s` and says "any spacing ratio or reachability claim lives in
its own derivation row." So the route is legitimate ONLY if a **separate
theorem** derives a form↔spacing identity

```
    c_t / c_s  ==  a_τ / a_s   (the hoped bridge)
```

from the free Euclidean quadratic form `Q(p) = c_t·p_τ² + c_s·|p_spatial|²`
(the object `SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06` writes as
spacing-linked coefficients). If it derives cleanly: `c_t=c_s ⇒ a_τ=a_s`, then
`scale_reference` ⇒ `a_τ = 1/M_Pl` and N2b is discharged. If not: N2b stays open.

## What the runner does (exact sympy, no new axiom/primitive)

Derives `c_t(a_τ,a_s)`, `c_s(a_τ,a_s)` directly from the lattice self-energy
`D_μ(k) = (2/a_μ²)(1−cos(k a_μ))` on `Z³×Z_τ` with **independent** spacings, in
the three legitimate normalization conventions, then tests the hoped identity
and its convention-robustness.

## Findings

**1. The hoped identity is FALSE in every convention.** `c_t/c_s` is never
`a_τ/a_s`. The would-be discharge residual is nonzero in all three conventions
(Section 2, all PASS = "no crack"). So the route as literally hoped does not exist.

**2. The bare-dispersion `k²` coefficient is `1` on every axis, independent of
spacing.** This is the structural crux the runner surfaced: the lattice
derivative `Δφ/a` is built to converge to `∂φ`, so the spacing dependence of
`c_t/c_s` does NOT live in the dispersion — it lives entirely in the chosen
measure/field normalization. The three legitimate conventions give:

| convention | `c_t` | `c_s` | `c_t/c_s` |
|---|---|---|---|
| A (continuum-normalized, measure-weighted) | `a_s³a_τ/2` | `a_s³a_τ/2` | **1** |
| B (bare hopping, dimensionless field) | `a_s³/a_τ` | `a_s a_τ` | **(a_s/a_τ)²** |
| C (no-measure, `1/a_μ²` weights) | `1/a_τ²` | `1/a_s²` | **(a_s/a_τ)²** |

The spacing-dependence of `c_t/c_s` is therefore **convention-DEPENDENT**
(Conv A: 1; Conv B/C: `(a_s/a_τ)²`). A genuine form↔spacing theorem would need
`c_t/c_s` to be a fixed function of the spacings independent of normalization;
it is not. (Note: even the route-favorable Conv B/C give the inverse-square
`(a_s/a_τ)²`, **not** `a_τ/a_s` — the hoped identity is wrong even in the
convention most generous to the route.)

**3. Whether `c_t=c_s` says anything about spacings is itself a convention
choice.** In Conv A, `c_t=c_s` is a tautology (`1=1`) constraining no spacing —
`a_τ` stays completely free. In Conv B/C, `c_t=c_s ⇒ a_τ=a_s`. So even the
spacing CONCLUSION is selected by the (unsupplied) normalization choice, not
derived from A_min + the form primitive.

**4. The decisive countermodel (Section 4).** The free Euclidean action carries
an independent anisotropic kinetic weight `(κ_t, κ_s)` — exactly the
two-coefficient freedom `SPATIAL_CUBIC_..._NO_GO_2026-06-06` proves spatial
`O_h` leaves unfixed (invariant dim 2; 4D-hypercubic collapses it to dim 1).
With those weights, `c_t=c_s` is satisfied at **`a_τ ≠ a_s`** by choosing
`κ_t/κ_s = a_τ²/a_s²`. Concrete witness: at `a_τ = 2a_s`, `κ_t/κ_s = 4`
restores `c_t = c_s` while the spacings stay unequal (resid 0). So form
isotropy does **not** force spacing equality.

**5. The bridge = the primitive (circularity, Section 5).** Recovering
`a_τ = a_s` requires the EXTRA input `κ_t = κ_s` (equal hopping weights = the
4D-hypercubic kinetic normalization). But `κ_t = κ_s` IS the kinetic-isotropy
content. Using it to derive `a_τ = a_s` and then invoking the primitive for
`c_t = c_s` double-counts the same premise — exactly the circularity the
kinetic-isotropy note warns of ("treating it as derived ... would be circular").

**6. scale_reference leg (Section 6).** Even granting the bridge,
`scale_reference` is units-only: it pins `a_s = 1/M_Pl` but carries no
dimensionless content, so `a_τ = 1/M_Pl` follows ONLY through the un-derived
form↔spacing bridge. scale_reference alone pins one spacing, never the ratio.

## Verdict

**N2b STAYS OPEN.** The form↔spacing identity `c_t/c_s == a_τ/a_s` does not
hold (it is `(a_s/a_τ)²` at best, and convention-dependent). The form isotropy
`c_t = c_s` is satisfiable at unequal spacings via the unfixed anisotropic
kinetic weights; pinning `a_τ = a_s` needs the extra input `κ_t = κ_s`, which
is the same content as the form primitive (circular / double-counting). The two
approved primitives (form isotropy + units-only scale) do **not** discharge the
absolute clock unit.

Sharper no-go (the citable result): *kinetic_isotropy pins the kinetic FORM
ratio `c_t/c_s`; it does NOT pin the spacing ratio `a_τ/a_s` (a separate,
convention-dependent, and unfixed datum), so it cannot pin the absolute clock
unit. The form↔spacing bridge is not a theorem from A_min + the form primitive
— it requires `κ_t = κ_s` (4D-hypercubic kinetic normalization), which is
content-equivalent to the form primitive itself.*

## Relation to the existing unified no-go

The unified note's N2b section (`SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md`,
§4 N2b, and §8 "N2b column (5 routes)") covers Stone/spectrum, Lattice-no-scale,
Record-no-metric, post-record-counts, and the joint two-gate route — all the
same `c`-rescaling viewed through different gates. It does **NOT** cover the
kinetic-isotropy form→spacing route. This route is a **6th, independent N2b
attack vector** that reaches the same wall by a different mechanism (form-ratio
vs spacing-ratio separation), so the no-go is **not overclaimed** — it should be
**augmented** with this column, strengthening the N1 route count for N2b from 5
to 6 and adding the sharp "form ≠ spacing, bridge needs `κ_t=κ_s`" statement.

No correction to existing block02 wording is required (no prior claim is wrong);
the recommended amendment is additive.
