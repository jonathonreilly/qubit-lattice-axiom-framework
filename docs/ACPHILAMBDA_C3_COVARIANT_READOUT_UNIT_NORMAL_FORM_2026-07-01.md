# AC_phi_lambda C3-Covariant Readout Unit Normal Form

**Date:** 2026-07-01
**Claim type:** bounded theorem / readout-selector narrowing.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, or claim
full `AC_phi_lambda` retirement.
**Primary runner:**
[`scripts/acphilambda_c3_covariant_readout_unit_normal_form_2026_07_01.py`](../scripts/acphilambda_c3_covariant_readout_unit_normal_form_2026_07_01.py)

## Claim

Inside the selected local C3 fixed-defect scalar class, finite additive scalar
readout has a one-parameter normal form.

The selected edge-minimal C3 context supplies one local defect-density scalar:

```text
L = L3(1,2) = 2/9.
```

For a finite collection of pairwise-disjoint selected-defect records, any scalar
readout that:

1. vanishes on the empty collection;
2. is additive over disjoint collections; and
3. depends on each selected local defect record only through this C3 scalar
   density line;

has the form

```text
I_c(R) = c * |R| * L
```

for one real scalar unit `c`.

Therefore the post-axiom `AC_phi_lambda` readout problem is narrower than a
general scalar-map problem:

```text
selected context + fixed-defect arithmetic + finite Record additivity
  -> selected defect-density line, with unit c free;

physical identity-unit readout c = 1
  -> |delta| = 2/9.
```

This theorem does not derive `c = 1`. It makes the remaining readout selector
exact: the physical charged-lepton phase readout must select the identity unit
on the selected local C3 defect-density line.

## Finite Theorem

Let `D` denote one selected local C3 fixed-defect record. The finite
fixed-defect arithmetic gives the scalar density

```text
L(D) = L3(1,2) = 2/9.
```

Let `R` be a finite pairwise-disjoint collection of selected local defect
records. If a scalar readout `I` is additive and `I(empty)=0`, then `I` is
determined by the singleton value

```text
u = I({D}).
```

For `n = |R|`,

```text
I(R) = n * u.
```

Since `L != 0`, write

```text
c = u / L.
```

Then

```text
I(R) = c * |R| * L.
```

Conversely, every real `c` defines a finite additive scalar readout on this
selected-defect record class.

The direct readout used by the phase-defect normal form is exactly the
identity-unit member:

```text
c = 1,  I({D}) = L = 2/9.
```

Other units, for example `c = 1/2` or `c = 2`, remain valid additive scalar
readouts of the same selected defect record class unless a physical readout
selector rejects them.

## What This Moves

| Prior residual | Effect of this theorem |
|---|---|
| broad physical readout-class selection | narrowed to identity-unit selection on the selected defect-density line |
| C3 arithmetic | fixed at `L3(1,2)=2/9` by the selected context |
| finite Record additivity | forces collection readout to be linear in record count once the singleton unit is supplied |
| contrast scalar values | reinterpreted as different units or different defect contexts, not new arithmetic freedom |
| `AC_phi_lambda` phase atom | becomes `W_defect_identity_unit`: why the charged-lepton phase reads `c=1` on this line |

## What Does Not Move

This note does not derive the physical identity unit `c = 1`. It does not show
that the charged-lepton phase must read the selected C3 defect density. It does
not derive occurrence, probability, measurement semantics, source/action,
theta, metric/observable semantics, or empirical species labels.

It also does not exclude future non-direct readout contexts. It only says that
inside the selected local C3 fixed-defect scalar class with finite additivity,
all remaining unit freedom is the single scalar `c`.

## Relation To Existing AC_phi_lambda Notes

The phase-defect readout normal form proves:

```text
direct local selected-defect scalar readout -> |delta| = 2/9.
```

The physical readout-selection independence theorem proves that the current
premise set does not choose the physical readout class.

This note sits between them. It proves that, after the selected C3 defect line
is accepted as the relevant local scalar class, the remaining freedom is not a
new C3 value, extra transverse arithmetic, or a general scalar map. It is the
single physical readout unit `c`.

The bridge target is therefore:

```text
W_defect_identity_unit:
  the physical charged-lepton phase readout uses the identity unit c=1 on the
  selected local C3 fixed-defect density line.
```

A same-surface source/action, eta/holonomy, or physical readout theorem could
still supply this unit. Without such a theorem or an approved primitive,
downstream rows must keep the unit selector explicit.

## Audit Consequence If Retained

Rows that need the charged-lepton phase value should use the sharpened
dependency shape:

```text
selected C3 defect-density line
  + physical identity-unit readout selector
  -> |delta| = 2/9.
```

Rows should not treat C3 covariance, local defect arithmetic, or Record
additivity as if they already select the identity unit. They reduce the target
to a one-parameter unit selector; they do not choose the physical member.

## Non-Claims

This note does not claim:

- `AC_phi_lambda` is closed;
- the identity unit `c = 1` is derived from the ontology axioms;
- the direct C3 defect scalar is false;
- non-direct readout contexts are impossible;
- future source/action, eta, holonomy, or instrument/readout routes fail;
- a new ontology axiom is required;
- probability, occurrence, theta, source/action, metric, or observable gates
  are closed.

## Minimum Foundation Update If Bridge Work Fails

No ontology axiom update follows from this theorem.

If bridge-first routes fail and owner governance chooses an approved
operational primitive, this theorem sharpens the `P_readout_selection` target
for `AC_phi_lambda`:

```text
In the charged-lepton C3 defect context, the physical phase readout selects the
identity unit c=1 on the selected local fixed-defect density line.
```

That would be a narrow operational readout primitive, not a change to Lattice,
Qubit, Admissibility, or Record.

## No-Go Discipline Gate

**Status:** PASS for bounded unit-normal-form narrowing. This is not a
terminal no-go against deriving the identity unit. It is a positive normal-form
theorem that leaves one named physical unit selector.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| C3 arithmetic route | Derive the phase value from the selected C3 fixed-defect density. | PARTIAL: fixes `L=2/9`, but this theorem shows a scalar unit `c` remains unless identity readout is supplied. |
| Record-additivity route | Use Record additivity to select the singleton unit. | ATTEMPTED here: additivity makes collections linear in the singleton value but does not choose that value. |
| C3-covariant local scalar route | Restrict to the selected local C3 defect-density line. | ATTEMPTED here: succeeds as a one-parameter normal form `cL`. |
| Direct-unit route | Declare or derive `c=1` as the physical phase readout unit. | OPEN: this is the sharpened bridge target. |
| Source/action or eta route | Use a same-surface physical theorem to select `c=1`. | OPEN: preserved as the likely bridge-first route. |
| New primitive route | Register the identity-unit readout selector as an approved operational premise. | OWNER-GOVERNANCE ROUTE: available only if bridge-first work fails or is intentionally bypassed. |

### N2 - Wall-Independence Audit

Collapsed residual after this theorem:

```text
W_defect_identity_unit.
```

The selected context, forced transverse weights, local density arithmetic, and
finite additivity are no longer counted as independent residuals inside this
normal form. The remaining wall is the physical selection of `c = 1`.

### N3 - Hidden-Wall Scan

| Term | Classification |
|---|---|
| `selected local C3 fixed-defect scalar class` | Explicit normal-form input from the phase-defect stack; this note does not derive physical selection of that class. |
| `depends only through this C3 scalar density line` | Scope restriction of the theorem, not a claim about all possible readouts. |
| `identity unit` | The missing physical readout selector, not assumed derived. |
| `finite additivity` | Record axiom content over supplied scalar record values. |
| `approved primitive` | Checked against `docs/audit/data/axiom_premise_nodes.json`; no readout-selection primitive is registered. |

No hidden admission is used to prove `c = 1`; that result is not claimed.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|
| `ACPHILAMBDA_PHASE_DEFECT_READOUT_NORMAL_FORM_2026-07-01` | physical selection of direct local C3 defect readout remains. | narrowed to identity unit on selected defect line. | yes |
| `PHYSICAL_READOUT_SELECTION_INDEPENDENCE_2026-07-01` | current premises do not select physical readout class. | same selector, sharpened after selecting the defect-density line. | yes |
| `ACPHILAMBDA_R_ETA_EDGE_DEFECT_LOCALIZATION_BRIDGE_2026-06-30` | phase-defect coupling remains. | coupling now localized to `c=1` on selected line. | yes |
| `OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05` | Record does not choose branch-to-scalar map. | Record does not choose singleton unit. | yes |
| `MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01` | `P_readout_selection` is a fallback candidate, not registered. | same candidate, now narrowed for this lane. | yes |

### N5 - Rhetoric Audit

The proven sentence is only:

```text
Inside the selected C3 fixed-defect density line, finite additive readouts have
the one-parameter form I_c(R)=c|R|L.
```

It is tested at the finite singleton-record and finite disjoint-record
resolution. It is not a claim about all C3-covariant readouts, all holonomy
readouts, all source/action surfaces, or all physical observable maps.

### N6 - Partial-Closure Path Scan

Live closure paths remain:

- derive `c=1` from a same-surface charged-lepton source/action theorem;
- derive `c=1` from an eta/holonomy theorem that identifies the phase readout
  with the selected local defect density in identity units;
- derive `c=1` from a physical record/instrument readout theorem;
- explicitly approve and register a narrow `P_readout_selection` instance if
  owner governance chooses that route.

The primitive-registry check confirms that no current approved primitive grants
the readout identity unit.

### N7 - Steelman

A hostile reviewer can argue that this theorem is deliberately conditional:
the real physics may not first choose the C3 defect-density line and then a
unit; instead, a future source/action theorem may select the charged-lepton
phase as a different scalar surface whose numerical agreement with `2/9` is
emergent. That objection is valid and preserved. This theorem does not
foreclose such routes; it only normalizes the direct C3 defect route so the
remaining claim is exactly `c=1`.

### N8 - Cross-Cycle Echo

Earlier readout cycles often mixed three questions: which carrier/context is
selected, which scalar line is read, and which unit maps that line to a
physical observable. This theorem keeps those layers separate. It follows the
same split used by source/action, metric/observable, and record scalar-map
notes: finite algebra can reduce a selector to one parameter, but physical
readout still needs a bridge or approved primitive.

## Verification

Run:

```bash
python3 scripts/acphilambda_c3_covariant_readout_unit_normal_form_2026_07_01.py
```

Expected close:

```text
TOTAL: PASS=81 FAIL=0
```
