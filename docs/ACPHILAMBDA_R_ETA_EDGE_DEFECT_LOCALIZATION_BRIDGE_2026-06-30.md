# AC_phi_lambda R-eta Edge-Defect Localization Bridge

**Date:** 2026-06-30
**Claim type:** positive theorem candidate / bounded bridge theorem.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit the Tier-A registry, register a primitive, refresh generated
ledgers, or claim full `AC_phi_lambda` retirement.
**Primary runner:**
[`scripts/acphilambda_r_eta_edge_defect_localization_bridge_2026_06_30.py`](../scripts/acphilambda_r_eta_edge_defect_localization_bridge_2026_06_30.py)

## Claim

On the 2026-06-29 axiom surface, plus the strict nearest-neighbor Dirac bridge
and the edge-minimal generation-context bridge, the `A_R-eta` residual is no
longer a broad "density-read-as-angle" package.

The selected generation context supplies a specific local defect:

```text
C3[111] acting on the edge-minimal hw=1 generation context.
```

For this defect, the local scalar fixed-defect density is unique. The C3
operator fixes the body diagonal, its transverse spectrum is
`{omega, omega^2}`, the forced transverse weights are `(1,2)`, and the local
Atiyah-Bott/Lefschetz density is

```text
L3(1,2) = 2/9.
```

Therefore the h-class part of `A_R-eta` can be narrowed:

```text
old h-class:
  the registered |delta| is some AB/Lefschetz fixed-locus density of the
  realized C3[111] cycle.

new h-class target:
  the charged-lepton phase readout is the local scalar defect density of the
  selected edge-minimal C3 generation context.
```

Once that target is accepted, the class, weights, and value are no longer free.
The h-unit side is also already narrowed by the retained-carrier conversion
work: no primitive conversion factor `c != 1` is supplied on the retained
registrable carrier classes, so the direct readout is the only retained-carrier
compatible member of `delta = c L`.

Thus this bridge does not add a number. It reduces `A_R-eta` to one explicit
physical coupling statement:

```text
the charged-lepton phase magnitude records the selected local C3 defect density.
```

If review accepts that coupling statement as a bridge theorem, this supplies
`|delta| = 2/9` on the charged-lepton context. If review rejects it, the exact
remaining wall is no longer broad R-eta; it is the phase-defect coupling itself.

## Inputs

- The current axioms supply physical `Z^3` nearest-neighbor locality, local
  possibility, admissible availability, and fixed record readout.
- The strict-NN bridge supplies the first-order edge-local Dirac branch and
  makes oriented nearest-neighbor edges primitive on the kinetic/readout
  surface.
- The generation-context bridge selects the `hw=1` C3 triplet as the minimal
  nontrivial oriented edge context.
- The R-eta narrowing note proves the formal `H(delta)` layer and isolates
  `A_R-eta = h-class + h-unit`.
- The fixed-locus note proves the C3[111] transverse weights and local density
  arithmetic.
- The conversion-factor note narrows h-unit by eliminating retained
  registrable carrier supply for `c != 1`.

## Finite Theorem

Let the C3[111] generator be the cyclic permutation of the three edge
directions:

```text
e_x -> e_y -> e_z -> e_x.
```

As a matrix on the edge basis, this operator has eigenvalues

```text
1, omega, omega^2.
```

The fixed eigendirection is the body diagonal. The transverse plane is the
regular representation with the singlet removed, so its weights are forced to
be `(1,2)` up to order. This is the unique trace-free pair: the exponents sum to
zero modulo 3. The equal-weight pairs `(1,1)` and `(2,2)` are not the selected
transverse representation.

The local fixed-defect density for this forced pair is

```text
L3(1,2)
  = (1/3) * sum_{j=1,2} 1 / ((1 - omega^j)(1 - omega^(2j)))
  = 2/9.
```

The contrast cells satisfy

```text
L3(1,1) = L3(2,2) = 1/9,
```

but they require equal transverse weights and therefore do not match the
selected trace-free edge context.

So after the edge-minimal generation-context bridge, there is a unique local
C3 fixed-defect scalar available from the selected context: `2/9`.

## Relation To The Formal `H(delta)` Layer

The R-eta narrowing note already proves that the registrable phase content of
the charged-lepton circulant surface is the magnitude `|delta|` on the
`cos(3 delta)` channel and that the formal layer cannot pick a value by itself.
This bridge does not alter that result.

Instead it supplies the missing geometric target for the value: the selected
generation context has exactly one local scalar defect density. Thus the
formal channel and the geometric defect now meet at a single explicit coupling
question:

```text
does the charged-lepton phase magnitude read the selected local C3 defect
density?
```

If yes:

```text
|delta| = L3(1,2) = 2/9.
```

If no, the formal layer remains value-free and the unresolved atom is exactly
the phase-defect coupling.

## What Moves

| Prior residual | Effect of this bridge |
|---|---|
| physical hw=1 generation context | supplied by the edge-minimal generation-context bridge, if retained |
| h-class as broad fixed-locus class membership | narrowed to the selected edge-minimal local C3 defect density |
| forced transverse weights | supplied by the C3[111] operator on the selected context |
| h-unit conversion factor | narrowed by retained-carrier class elimination: no `c != 1` carrier is supplied on the retained surface |
| numeric value `2/9` | arithmetic consequence of the selected local defect; no measured value imported |

## What Does Not Move

- This does not prove that all possible readout contexts must use fixed-defect
  densities.
- This does not derive record occurrence, Born weights, measurement semantics,
  theta, source/action coefficients, or metric/observable identification.
- This does not claim `AC_phi_lambda` is retired unless the context selector,
  durable `r = 1/2` bridge, and this phase-defect coupling are independently
  accepted and then audited together.
- This does not consume PDG masses, fitted values, lattice-MC values, beta=6
  values, or a new primitive.

## Audit Consequence If Retained

The remaining `A_R-eta` atom should be restated from

```text
registered |delta| is the AB/Lefschetz fixed-locus density of the realized
C3[111] cycle, identity-read in radians
```

to the narrower statement

```text
the charged-lepton phase magnitude records the local scalar fixed-defect
density of the selected edge-minimal C3 generation context.
```

Everything else in the old package is supplied or narrowed by existing bridge
work: context selection, forced weights, local density arithmetic, sign strip,
`cos(3 delta)` channel, and retained-carrier-compatible direct unit.

## No-Go Discipline Gate

**Status:** PASS for the bounded boundary. This is a positive bridge candidate
with one named residual if rejected. It is not a no-go against future R-eta
closure and not a claim that the phase-defect coupling is already audit-retained.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| Formal `H(delta)` route | Select `|delta|` from the circulant symmetric functions alone. | RULED OUT BY PRIOR as full closure: the formal layer admits many constant magnitudes. |
| Edge-minimal defect route | Use the strict-NN selected hw=1 context to identify the unique local C3 defect density. | ATTEMPTED here: succeeds as a finite theorem for the selected context. |
| Conversion-factor route | Supply `delta = c L` with `c != 1`. | RULED OUT BY PRIOR on retained carrier classes: no retained registrable carrier supplies primitive `c != 1`. |
| Periodic `q*pi` route | Read the value as a periodic phase source. | RULED OUT BY PRIOR for the rational-density route; `2/9` is outside that bin. |
| Equal-weight fixed-locus route | Use `(1,1)` or `(2,2)` instead of `(1,2)`. | RULED OUT on the selected context: equal weights are not trace-free and do not match the C3 transverse spectrum. |
| Direct comparator route | Use charged-lepton mass agreement to choose the value. | NOT USED: comparator remains downstream evidence, not a derivation input. |

### N2 - Wall Independence Audit

Collapsed residual after this note:

```text
W_coupling = charged-lepton phase magnitude records the selected local C3
             defect density.
```

The old `h-class` and `h-unit` split is no longer a two-wall surface on the
retained carrier route: h-class has been narrowed to the selected local defect
and h-unit has no retained-carrier conversion supply beyond direct readout.
The remaining coupling does not automatically follow from record fixedness,
from the formal `H(delta)` algebra, or from the finite fixed-locus arithmetic.

### N3 - Hidden-Wall Scan

"Selected context" means selected by the strict-NN generation-context bridge,
not by this note. "Defect density" means the local scalar fixed-defect density
computed from the C3[111] transverse operator. "Direct readout" means no
retained `c != 1` carrier is supplied on the retained classes; it is not a
proof that no future readout context can supply a factor. "Records" are fixed
readables; this note does not use record occurrence or probability.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING...` | `A_R-eta = h-class + h-unit` | narrows h-class/h-unit to `W_coupling` | yes |
| `GENERATION_CONTEXT_SELECTOR_FROM_STRICT_NN_DIRAC_RECORD_ORIENTATION...` | physical hw=1 context selector | supplies selected context | yes |
| `KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS...` | fixed-locus weights and density, not physical readout | supplies local defect arithmetic | yes |
| `RETA_CONVERSION_FACTOR_CARRIER_CLASS_ELIMINATION...` | no retained carrier factor `c != 1`; R-eta still open | narrows h-unit only | yes |
| `CONTINUUM_EQUIVARIANT_ETA_STANDARD_FORM...` | localization value independent of mass phase | shows coupling is not automatic | yes |

### N5 - Rhetoric Audit

The claim is not "R-eta is derived from C3" at every resolution. The tested
resolution is the selected edge-minimal C3 generation context. The theorem does
not say other contexts cannot have other defect scalars, and it does not say
the mass phase must couple to this defect without the named coupling bridge.

### N6 - Partial-Closure Path Scan

This is a bridge theorem path, not a new axiom. The import-retirement shape is:

```text
explicit coupling statement
  -> finite selected-context defect theorem
  -> carrier-class direct-unit narrowing
  -> audit review
  -> registry narrowing or retirement
```

No primitive is expanded. The current axioms, strict-NN bridge, generation
context bridge, fixed-locus arithmetic, and carrier-class conversion note do
their named work only.

### N7 - Steelman

A hostile reviewer can object that this bridge still does not derive the
physical coupling between the charged-lepton mass phase and the local C3 defect
density. The finite theorem proves the selected context has a unique local
defect scalar, and the conversion note blocks retained `c != 1` carriers, but
neither fact alone says the phase variable of `H(delta)` must equal that scalar.
That objection is correct. This note's value is that it makes the coupling the
only remaining atom instead of leaving R-eta as a broad package.

### N8 - Cross-Cycle Echo

Prior R-eta and radian cycles failed when they hid a readout class, a unit
factor, or a comparator inside the value claim. This bridge keeps the value
source separate: the number is fixed-locus arithmetic, the unit is narrowed by
carrier-class elimination, and the unresolved physical statement is the
phase-defect coupling.

## Verification

Run:

```bash
python3 scripts/acphilambda_r_eta_edge_defect_localization_bridge_2026_06_30.py
```

Expected close:

```text
TOTAL: PASS=80 FAIL=0
```
