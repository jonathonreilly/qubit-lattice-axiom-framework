# Physical Readout Selection Independence

**Date:** 2026-07-01
**Claim type:** bounded no-go / current-premise independence theorem.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, or claim
that a future physical readout theorem is impossible.
**Primary runner:**
[`scripts/physical_readout_selection_independence_2026_07_01.py`](../scripts/physical_readout_selection_independence_2026_07_01.py)

## Claim

The current post-axiom stack does not derive the remaining
`AC_phi_lambda` phase readout selector:

```text
W_defect_readout_selection:
  the physical charged-lepton phase readout is the direct local scalar readout
  of the selected C3 edge defect.
```

This is a current-premise independence result, not a terminal no-go. The
phase-defect normal form proves that, inside the direct local C3 fixed-defect
readout class, the selected scalar is uniquely

```text
L3(1,2) = 2/9.
```

What is not supplied by the four ontology axioms, the approved primitive
registry, or the #4760 normal form is the physical selection of that readout
class as the charged-lepton phase readout.

## Finite Witness

Record additivity fixes sums after singleton record values are supplied. It
does not fix the singleton values themselves.

Take one fixed record atom `r` in the selected C3 edge context. Two scalar
record readout surfaces on the same record set are:

```text
I_direct(empty) = 0
I_direct({r})  = 2/9
```

and

```text
I_contrast(empty) = 0
I_contrast({r})  = 1/9.
```

Both extend additively over finite pairwise-disjoint record collections. They
therefore satisfy the Record additivity clause at the tested finite-record
resolution. They also share the same Lattice, Qubit, Admissibility, selected
C3 context, and finite C3 arithmetic.

The difference is only the physical readout interpretation:

```text
I_direct:
  the record scalar is the direct selected C3 fixed-defect density.

I_contrast:
  the record scalar is a different supplied scalar on the same record atom.
```

The current premises contain no rule that rejects `I_contrast` as a scalar
record readout while accepting `I_direct` as the physical charged-lepton phase
readout. Therefore `W_defect_readout_selection` is not derivable from the
current premise set alone.

## What This Moves

This note converts the highest-priority hard gate from a broad question:

```text
derive the charged-lepton phase value
```

to the precise missing rule:

```text
derive or approve the physical readout-class selector that identifies the
charged-lepton phase scalar with the direct selected C3 fixed-defect density.
```

It does not reopen the C3 arithmetic. If that selector is later derived or
approved, #4760 already supplies the value:

```text
W_defect_readout_selection
  + phase-defect normal form
  -> |delta| = 2/9.
```

## Minimum Foundation Update If Bridge Work Fails

No ontology axiom update follows from this theorem. The four ontology axioms
remain the correct minimal base for this question.

If bridge-first routes fail, the minimum foundation update is the narrow
operational primitive candidate already isolated by the primitive-update
recommendation:

```text
P_readout_selection:
  In a supplied finite record context, a physical scalar readout is selected by
  a local covariant map from specified record/context invariants to scalar
  record values. The selector must name the context, invariant class, unit
  convention, and equivalence boundary.
```

For the `AC_phi_lambda` phase atom, the first target instance would be:

```text
the physical charged-lepton phase readout is the direct local scalar readout of
the selected C3 edge defect.
```

Until such a bridge theorem or approved primitive exists, downstream rows must
keep this selector explicit.

## Non-Claims

This note does not claim:

- the direct C3 defect scalar is false;
- `2/9` is arithmetically ambiguous inside the direct fixed-defect class;
- no future source/action, eta, holonomy, instrument, or record-facing theorem
  can derive the selector;
- the Record axiom is defective as ontology;
- probability, occurrence, theta, source/action, metric, or measured-observable
  gates are closed.

## Audit Consequence If Retained

Rows that need `|delta| = 2/9` must cite both:

```text
phase-defect normal form
physical defect-readout selector
```

The first is finite C3 arithmetic on the selected context. The second is the
remaining physical-readout bridge or primitive. The current stack supplies only
the first.

## No-Go Discipline Gate

**Status:** PASS for current-premise independence only. The no-go is scoped to
deriving `W_defect_readout_selection` from the present approved premise stack.
It is not a no-go against future bridge derivations.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| Record-additivity route | Derive the physical scalar from finite additive record readout. | ATTEMPTED here: additivity allows both `I_direct({r})=2/9` and `I_contrast({r})=1/9`; it does not fix singleton values. |
| C3-arithmetic route | Use the selected C3 edge context to force the phase value. | RULED OUT BY #4760 as full closure: it forces `2/9` only inside the direct fixed-defect readout class and leaves selection of that class open. |
| Approved-primitive route | Use an already registered primitive to supply the selector. | ATTEMPTED by primitive-registry check: scale reference, kinetic isotropy, and realized-state evaluation grant no readout selector. |
| Formal `H(delta)` / registrability route | Use the formal phase layer or determinant-character algebra to select the value. | RULED OUT BY PRIOR: the formal layer does not select the value, and determinant-character algebra is conditional on a supplied readout surface. |
| Comparator route | Use charged-lepton empirical agreement to select the readout. | RULED OUT BY POLICY for derivation: comparator data is downstream evidence, not a premise for deriving the selector. |
| Source/action or eta route | Derive the physical scalar through a future source/action, eta, or holonomy theorem. | OPEN: not a current-premise closure, and explicitly preserved as a future bridge path. |

### N2 - Wall-Independence Audit

The collapsed wall set for this theorem has one wall:

```text
W_defect_readout_selection.
```

Other hard gates, such as occurrence, source/action, theta, and
metric/observable semantics, are not counted as independent walls of this
claim. They may provide future routes to close this wall, but the present
finite witness shows the selector is not already supplied by the current
premise set.

### N3 - Hidden-Wall Scan

Terms used load-bearingly are classified as follows:

| Term | Classification |
|---|---|
| `selected C3 edge context` | Cited stack context from the strict-NN and generation-context bridges; this note does not derive it. |
| `direct fixed-defect readout class` | The conditional class isolated by #4760; it is the target, not assumed physical here. |
| `scalar record readout` | Record additivity over finite disjoint record collections; singleton scalar values remain supplied. |
| `approved primitive` | Checked against `docs/audit/data/axiom_premise_nodes.json` and the source notes for scale, kinetic isotropy, and realized state. |
| `physical` | Marks the missing selector, not a hidden assumption. |

No hidden admission is promoted into a second wall.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `ACPHILAMBDA_PHASE_DEFECT_READOUT_NORMAL_FORM_2026-07-01` | `W_defect_readout_selection` remains after C3 arithmetic. | Same selector. | yes |
| `OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05` | Record additivity does not choose the branch-to-scalar map. | Record additivity does not choose this scalar readout surface. | yes |
| `REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18` | Algebra works only inside a supplied readout surface; physical bridges remain separate. | Same supplied-surface boundary. | yes |
| `ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11` | Formal layer narrows but does not select the physical readout value. | Same value-selection residual. | yes |
| `MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01` | `P_readout_selection` is a fallback candidate, not registered. | Same missing operational selector. | yes |

### N5 - Rhetoric Audit

The proven sentence is narrow:

```text
The present finite record/additivity/selected-C3 premise stack does not derive
the physical defect-readout selector.
```

It is checked at the finite singleton-record and finite disjoint-record
resolution. The theorem does not claim that every possible global,
source/action, eta, holonomy, or metric route fails.

### N6 - Partial-Closure Path Scan

Live closure paths remain:

- derive a record-facing C3-covariant phase readout theorem;
- derive the selector from a same-surface charged-lepton source/action theorem;
- derive it from an eta or holonomy bridge that outputs the selected local
  defect scalar;
- explicitly approve and register `P_readout_selection` as an operational
  primitive if owner governance chooses that path.

The primitive-registry check confirms that no current approved primitive
already grants this selector. The candidate primitive is therefore an
owner-governance option, not a silent premise.

### N7 - Steelman

A hostile reviewer can argue that this theorem proves only a weak
model-theoretic fact: arbitrary additive scalar surfaces are easy to invent,
but the physically relevant charged-lepton phase may be the unique local,
C3-covariant, dimensionless, source-coupled scalar compatible with the
selected generation context. That objection is strong. It is not closed here.
It is exactly the next bridge route: supply the source/action, eta, holonomy,
or covariant-readout theorem that makes the direct defect scalar physical.

### N8 - Cross-Cycle Echo

Similar readout-selection walls recur across the repo: Record scalar-map
selection, flavor carrier/readout selection, minimal-block magnitude readout,
EW `kappa_EW` physical readout, quark scalar readout underdetermination, and
registrable determinant-character surfaces. Some become useful bounded
theorems once a readout class is supplied; none licenses silently treating an
unapproved physical readout class as derived. The same mechanism applies here:
the direct C3 defect scalar can close the value only after the physical readout
selector is derived or approved.

## Verification

Run:

```bash
python3 scripts/physical_readout_selection_independence_2026_07_01.py
```

Expected close:

```text
TOTAL: PASS=93 FAIL=0
```
