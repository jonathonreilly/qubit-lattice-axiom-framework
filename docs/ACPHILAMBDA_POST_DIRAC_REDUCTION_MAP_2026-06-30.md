# AC_phi_lambda Post-Dirac Reduction Map

**Date:** 2026-06-30
**Claim type:** source-side reduction map / partial narrowing.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit the Tier-A registry, register a primitive, refresh generated
ledgers, or claim AC_phi_lambda retirement.
**Primary runner:**
[`scripts/acphilambda_post_dirac_reduction_map_2026_06_30.py`](../scripts/acphilambda_post_dirac_reduction_map_2026_06_30.py)

## Claim

If PR #4748's strict nearest-neighbor composition bridge is retained, the
kinetic-order shortage no longer carries AC_phi_lambda. The bridge supplies the
spatial first-order Dirac/staggered kinetic spine:

```text
strict nearest-neighbor composition
  -> no face-diagonal mixed terms
  -> anticommuting one-site edge coefficients
  -> flux(-1) / Kawamoto-Smit branch K1
```

That is a real reduction, but it does not retire AC_phi_lambda. The remaining
AC_phi_lambda work is smaller and sharper:

1. **Sub-admission (i), occupancy/readout:** the value face is already reduced
   to realized-state registration, but the measure-side/statistics question
   remains: what makes the charged-lepton lane use the signed one-slot
   `r = 1/2` readout rather than the second-order modulus count?
2. **Sub-admission (ii), R-eta:** the formal `H(delta)` layer remains narrowed
   to the single atom `A_R-eta`, the physical identification that the registered
   `|delta|` is the fixed-locus density, identity-read in radians.
3. **Sub-admission (iii), species bridge:** the kinetic branch is no longer the
   missing part, but the physical locus/readout-context question remains: why
   the generation-record context is the hw=1 triplet rather than merely an
   allowed staggered/Dirac corner structure.

So #4748 changes AC_phi_lambda from a broad "carrier/kinetic/readout/species"
blocker into three explicit residual atoms. It does not erase those atoms.

## What The Dirac Bridge Moves

The pre-#4748 kinetic blocker was a one-bit choice between the scalar
flux(+1) branch and the flux(-1) staggered-Dirac branch. The strict-NN bridge
selects flux(-1), rejects scalar face-diagonal leakage, and activates the
Kawamoto-Smit kinetic spine on the selected branch. This directly removes the
old "first-order kinetic order is not supplied" pressure from downstream flavor
work.

This matters most for AC_phi_lambda sub-admission (iii), because the species
bridge notes had localized the structural carrier-locus residual onto the
recurring chirality/Dirac gate. After #4748, the kinetic-form part of that gate
has a source-side supplier. What remains is not "find a Dirac branch"; it is the
more specific physical-locus/readout question: which record context is the
generation context, and why that context is read as the hw=1 triplet.

It also matters for sub-admission (i), because the open occupancy route was the
dynamical first-order-versus-second-order question. The bridge supplies a
first-order spatial kinetic branch. It still does not by itself supply the
matter-action statistics, signed-root readout, or one-slot quotient needed to
force `r = 1/2`.

## Why This Is Not A Full AC_phi_lambda Closure

### 1. Occupancy Is Not Closed

The occupancy reduction note already splits sub-admission (i) into value and
realization:

```text
(i) = registered value face + measure-side realization frontier
```

The registered value face is handled by the realized-state primitive. The
surviving frontier is which grain the matter action's statistics implements.
The static-selector note names the remaining live opening as the dynamical
first-order/index readout, and the explicit Kähler-Dirac realization note shows
that one concrete realization gives the second-order modulus count
`|det M|^2 -> r = 1`, leaving the signed / `U(1)_b` one-slot readout open.

PR #4748 supplies the spatial kinetic order needed for that frontier to become
well-posed. It does not yet derive the signed one-slot readout.

### 2. R-eta Is Unchanged

The R-eta narrowing note already derives the formal `H(delta)` form layer and
isolates the remaining atom:

```text
A_R-eta: the registered |delta| IS the AB/Lefschetz fixed-locus density of
         the realized C3[111] cycle, identity-read in radians.
```

Strict nearest-neighbor composition does not identify a registered phase
magnitude with that density, and it does not choose the radian identity unit.
Therefore sub-admission (ii) remains narrowed but not retired.

### 3. Species Bridge Is Reduced, Not Gone

The species-bridge decomposition already removes naming and sector-assignment
pseudo-content. The genuine structural residual is the carrier-locus/readout
question. PR #4748 supplies the kinetic branch needed by that residual, but it
does not select the physical generation record context or the empirical anchor
for species records.

Thus "the kinetic branch exists and is selected" is no longer the blocker.
"This selected branch is the physical generation context read by records" is
still a separate bridge target.

## Remaining Blocker Order

The next highest-leverage target is AC_phi_lambda sub-admission (i):

```text
derive the signed/statistics one-slot readout, or prove exactly what extra
bridge is needed for it.
```

Reason: it is adjacent to the new Dirac kinetic branch, it is the surviving
continuous `r = 1/2` lever in the charged-lepton chain, and it also cross-touches
theta's mass-side determinant/orientation readout. R-eta is the next clean
readout-identification target after that. Theta's gauge-side winding account
remains later and less directly moved by the Dirac bridge.

## No-Go Discipline Gate

**Status:** PASS for the narrow negative claim only: PR #4748 does not by itself
retire all of AC_phi_lambda. This is not a universal no-go against future
AC_phi_lambda retirement.

### N1 - Alternative Route Enumeration

| Route | Marker | Result |
|---|---|---|
| Kinetic-order route | ATTEMPTED in #4748 | Succeeds for the spatial Dirac/staggered kinetic branch; does not supply readout statistics or R-eta. |
| Realized-state route for `r` values | RULED OUT BY PRIOR as full closure | It reclasses the value face as registered data, but explicitly leaves the measure-side realization frontier open. |
| First-order determinant/statistics route | PARTIAL | The new bridge supplies first-order spatial kinetic order; existing Kähler-Dirac work shows a concrete realization still gives `|det M|^2 -> r = 1`, so the signed one-slot readout remains the target. |
| R-eta formal algebra route | RULED OUT BY PRIOR as full closure | The formal `H(delta)` layer is narrowed, but `A_R-eta` remains the physical identification atom. |
| Species-registration route | PARTIAL | Naming and assignment pseudo-content dissolve into records and supplied context; the physical hw=1 locus/readout context remains. |
| Theta-side determinant/orientation route | NOT ATTEMPTED HERE | Shares sign/readout pressure with AC(i), but gauge-side winding is a separate theta residual. |

### N2 - Wall Independence

The collapsed residual set is:

```text
W_r      = signed/statistics one-slot readout for r = 1/2
W_eta    = A_R-eta fixed-locus-density identity readout
W_locus  = physical hw=1 generation record-context/locus bridge
```

Closing `W_r` would not identify `|delta|` with a fixed-locus density or select
the physical record context. Closing `W_eta` would not choose `r = 1/2` or the
hw=1 physical locus. Closing `W_locus` would not supply the signed one-slot
statistics or the R-eta unit/readout identification. The three residuals are
therefore independent for current repo purposes.

### N3 - Hidden-Wall Scan

"Dirac bridge" means the spatial first-order kinetic spine only, as stated in
the #4748 path note. "Realized-state registration" is the registered primitive
and supplies no state-selection or weighting rule. "Readout context" is treated
as a named residual, not as something silently supplied by Record.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| Occupancy reduction note | value face vs measure-side realization | `W_r` measure-side readout/statistics | yes |
| Static r=1/2 selector no-go | tested static selectors fail; dynamical first-order opening remains | #4748 attacks that opening but does not supply signed one-slot readout | yes |
| Kähler-Dirac realization no-go | explicit realization gives second-order modulus count | prevents overclaiming #4748 as an `r = 1/2` theorem | yes |
| R-eta narrowing note | `A_R-eta` remains | `W_eta` | yes |
| Species-bridge decomposition | carrier-locus/readout residual remains | `W_locus` | yes |

### N5 - Rhetoric Audit

The claim is not "AC_phi_lambda remains impossible" or "Dirac cannot help
flavor." The claim is narrower: the new Dirac kinetic bridge removes the kinetic
piece but leaves three named readout/locus atoms.

### N6 - Partial-Closure Path Scan

Three legitimate closure paths remain:

1. a signed/statistics one-slot readout theorem for `r = 1/2`;
2. an R-eta bridge deriving h-class and h-unit for the fixed-locus density
   identification;
3. a physical locus/context theorem identifying the hw=1 generation record
   context without adding a new species primitive.

No new axiom is asserted here. If one of these is accepted as a bridge theorem,
the relevant atom can be retired by ordinary audit/registry work.

### N7 - Steelman

A hostile reviewer could argue that #4748 plus the existing Grassmann/Berezin
substep already gives the first-order determinant, and that once a first-order
Dirac branch is selected the hw=1 locus and one-slot readout should follow. That
is the strongest route against this narrowing. The current repo evidence is not
enough for that stronger claim because the explicit Kähler-Dirac realization
still lands on the second-order modulus count, and the species notes still
separate kinetic branch, physical locus, and record context. This steelman is
therefore the next route to test, not a closure already in hand.

### N8 - Cross-Cycle Echo

Prior AC_phi_lambda work repeatedly retired overbroad blockers by splitting
them into value registration, formal algebra, and physical readout/locus atoms.
This note follows that pattern. It uses #4748 to remove the kinetic atom, then
keeps the remaining atoms explicit instead of relabeling them as solved.

## Verification

Run:

```bash
python3 scripts/acphilambda_post_dirac_reduction_map_2026_06_30.py
```

Expected close:

```text
TOTAL: PASS=54 FAIL=0
```
