# Corner Fermion Determinant Does Not Select Koide r=1/2 (Narrow Dynamical-Route Obstruction)

**Date:** 2026-06-04
**Type:** no_go
**Claim type:** no_go (narrow, route-specific) — prunes the fermion-determinant
corner-coupling route; the broader dynamical class stays open (two untested routes).
**Claim scope:** on the three hw=1 cubic-BZ corners (where the kinetic staggered-Dirac
operator vanishes), the corner Grassmann integral gives the fermion weight `det(M)` for
the C3-circulant mass `M = a I + b C + b-bar C^2`. At fixed Frobenius scale the
balanced Koide value `r = |b|^2/a^2 = 1/2` (Q = 2/3) is **not** a stationary point or
extremum of `det(M)`. So the corner fermion-determinant route — flagged as the #1 OPEN
dynamical lead in the Koide no-go ledger — does **not** select r=1/2.
**actual_current_surface_status:** exact negative boundary on the fermion-determinant
route; **conditional** on the open staggered-Dirac realization gate; bounded obstruction
for the dynamical class with two named untested routes. Not retained on the current surface.
**bare_retained_allowed:** false
**Status:** independent audit required.
**Runner:** [`scripts/audit_companion_corner_fermion_determinant_not_r_half_exact.py`](./../scripts/audit_companion_corner_fermion_determinant_not_r_half_exact.py)

## Context (physics-loop dirac-corner-coupling, block 1)

The Koide value `r=1/2` (Q=2/3) was just shown (#2591) to be **not protected by any
unitary symmetry** — it is a dynamical norm-balance, so it can only come from the corner
coupling. The 30-probe BAE campaign exhausted the operator/measure/symmetry routes (all
give `kappa=1`, r=1) and Probe 29 records the resulting partial falsification. The Koide
no-go ledger flags the **fermion-determinant / corner-coupling** route as the #1 OPEN
dynamical lead. This block tests it.

## Statement

The hw=1 corner mass matrix is `M = a I + b C + b-bar C^2`, `b = |b| e^{i delta}`, with
circulant determinant `det(M) = a^3 - 3 a |b|^2 + 2 |b|^3 cos(3 delta)`. At fixed
Frobenius scale `3 a^2 + 6 |b|^2 = 1` (parametrize by singlet energy fraction `x = 3 a^2`,
so `r = (1-x)/(2x)` and `x = 1/2 <-> r = 1/2`):

1. (**NG**) `det(M)` is **not stationary** at `r = 1/2`: `d(det)/dx != 0` at `x = 1/2`
   on both `cos 3 delta = +1` and `cos 3 delta = -1` branches.
2. Its stationary points in the shape are `r = 1` (at `cos 3 delta = +1`, where
   `det = 0` — a two-fold mass degeneracy) and `r = 4` (at `cos 3 delta = -1`); its
   extrema otherwise sit at the boundaries `r -> 0` (all-equal) and `r -> inf`.
3. (**Contrast**) `r = 1/2` IS the max-sector-entropy point (equal singlet/doublet energy
   `3 a^2 = 6 |b|^2`, `S = log 2`, `dS/dx = 0`), but it is **not** a `det(M)` stationary
   point — the dynamical (determinant) criterion and the balanced (entropy) criterion
   **disagree**.
4. (**Cycle 2: full one-loop effective potential**) Upgrading from the bare determinant to
   the fermion one-loop Coleman-Weinberg potential `V_ferm = -Tr log M = -log det(M)`: since
   `-log` is strictly monotonic, `V_ferm` has the **same** shape-stationary points as
   `det(M)` (r=1, r=4, boundaries), so `dV_ferm/dx != 0` at `x=1/2` too. Moreover, **any**
   scalar potential that is a function of the Frobenius **scale** invariant
   `s = 3a^2 + 6|b|^2` alone is `x`-flat on the fixed-scale slice (`dV_scalar/dx ≡ 0`), so it
   **cannot** move the shape-stationary point onto `r=1/2`. Hence the combined
   `V_eff = V_scalar(s) + V_ferm` still has no `r=1/2` vacuum.

All ten checks pass exactly (sympy). (Scope note on check 7b: this covers the fermion CW
plus *scale-only* scalar additions exactly. The framework's actual trace-mode scalar
potential `V(m=Tr K_Z3)` lives on a **different** coordinate — the frozen-bank slice
`K_frozen + m T_m` — and is treated as a separate cited ingredient below, not folded into
this single-coordinate computation.)

## Synthesis with the other dynamical ingredients

The corner determinant joins the other leading corner-sector ingredients, all of which
**fail to select r=1/2**:

- **Free Gaussian measure** on Herm_circ(3) -> the (1,2) real-dimension weighting = F3 =
  `kappa = 1`, r = 1 (Probe 25; robust). RULED OUT BY PRIOR.
- **Fermion determinant** `det(M)` -> stationary at r=1, r=4 (this block). RULED OUT.
- **Z3 scalar potential** -> the framework's own
  `KOIDE_Z3_SCALAR_POTENTIAL_LEPTON_MASS_TOWER_NOTE_2026-04-19.md` Section 5 concedes
  "the V_eff minimum does not coincide with the physical selected point... requires an
  additional microscopic selector" (V_eff min at `m_V ≈ -0.433`, physical `m_* ≈ -1.16`).
  RULED OUT (by the framework's own concession).

So the **three leading dynamical routes do not rescue r=1/2**, extending Probe 29's
partial falsification from the measure routes to the dynamical routes. The charged-lepton
masses still fit Q=2/3 at the admitted physical point `m_*` (that note's Section 6, <0.05%
on sqrt-mass), but **the selection of that point is not produced by these dynamics** — it
is the BAE admission.

## NO-GO DISCIPLINE GATE (N1-N8)

| # | Check | Result |
|---|---|---|
| N1 | >= 5 attack routes named | 5: (1) free measure -> kappa=1 [RULED OUT BY PRIOR, Probe 25]; (2) fermion determinant -> r=1,4 [ATTEMPTED, ruled out, this block]; (3) Z3 scalar potential -> V_eff min != physical point [RULED OUT, framework Section 5]; (4) taste-breaking scalar normalization [**UNTESTED**]; (5) multi-factor Connes-Lott [**UNTESTED**]. **3 ruled out, 2 untested** -> NOT a universal no-go; this note prunes route (2) only. |
| N2 | wall independence | The three ruled-out walls are independent mechanisms (measure-dimension-weighting; determinant-stationarity; scalar-potential-gap). None follows from another. |
| N3 | hidden-wall scan | The sole admission is explicit: CONDITIONAL on the open staggered-Dirac realization gate. No "by construction"/"naturally"/"standard QFT" hidden inputs; the corner det is reproven from the circulant primitive. |
| N4 | residual matching | Witnesses (Probe 25 kappa=1; Probe 29 partial falsification; Section 5 concession) all match the r=1 / not-selected residue exactly. |
| N5 | rhetoric resolution | The phrase is scoped to "at fixed Frobenius scale, det(M) has no stationary point at r=1/2" — verified exactly; not broadened to "no dynamics can give r=1/2". |
| N6 | partial-closure path | No labeling-convention path applies (this is a dynamical computation, not a definition refactor). |
| N7 | steelman | "An untested route (taste-breaking normalization, or multi-factor Connes-Lott with chirality on a separate factor) might supply an F1-weighting / select r=1/2 via a mechanism the determinant and measure lack." This steelman is **valid** -> the note claims only narrow route-pruning, not universal impossibility. |
| N8 | cross-cycle echo | The 30-probe measure routes all gave kappa=1; this block extends the same residue to the determinant route, consistent. No structurally-similar wall has been retired by an un-considered mechanism. |

**Verdict:** narrow route-pruning (fermion-determinant route), embedded in a bounded
obstruction for the dynamical class. The honest residual is the two **untested** routes.

## What this claims / does NOT claim

- Claims: `det(M)` does not stationary-select r=1/2 (exact, at fixed Frobenius scale);
  the three leading dynamical ingredients do not rescue r=1/2.
- Does **not** claim a universal no-go: the taste-breaking-normalization and
  multi-factor-Connes-Lott routes are untested (the open residual).
- Does **not** claim Q=2/3 is wrong empirically (the masses fit it at the admitted m_*);
  it claims the *selection* is not produced by these dynamics.
- Conditional on the open staggered-Dirac realization gate.

## Trace gate

```yaml
trace_class: negative_route_pruning
target_blocker_text: "BAE admission |b|^2/a^2=1/2 (r=1/2) on the charged-lepton lane"
source_of_blocker_text: audit_ledger
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "test the two untested dynamical routes (taste-breaking normalization; multi-factor Connes-Lott)"
```

## Forbidden imports

- No PDG values as derivation inputs (the charged-lepton Q=2/3 and m_* fit appear as
  comparators only, via the cited scalar-potential note). Reproven from the circulant
  primitive. No fitted selectors, no literature as a proof input.

## Cross-references

- `KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md`
  (#2591) — why r=1/2 must be dynamical, redirecting here.
- `KOIDE_Z3_SCALAR_POTENTIAL_LEPTON_MASS_TOWER_NOTE_2026-04-19.md` Section 5 — the
  framework's own "V_eff minimum != physical point" concession.
- `KOIDE_BAE_30_PROBE_CAMPAIGN_NOTE_2026-05-09.md` — the measure/symmetry routes (kappa=1).
- The staggered-Dirac realization gate — the open gate this result is conditional on.
