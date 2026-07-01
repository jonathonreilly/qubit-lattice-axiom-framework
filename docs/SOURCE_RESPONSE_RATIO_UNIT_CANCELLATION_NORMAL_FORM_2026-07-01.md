# Source-Response Ratio Unit-Cancellation Normal Form

**Date:** 2026-07-01
**Claim type:** bounded theorem / physical-source wall narrowing.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, or claim
source/action or `Y_T` closure.
**Primary runner:**
[`scripts/source_response_ratio_unit_cancellation_normal_form_2026_07_01.py`](../scripts/source_response_ratio_unit_cancellation_normal_form_2026_07_01.py)

## Claim

The physical-source wall splits by use case.

For a supplied physical source line on a record-facing action/RN surface,
changing the source unit rescales every first derivative with respect to that
same source by the same nonzero factor. Therefore same-source response ratios
are invariant under source-unit changes:

```text
(dA/dh) / (dB/dh)
```

does not depend on the absolute unit of `h`, provided `A` and `B` are read on
the same source surface and `dB/dh != 0`.

Absolute source coefficients still need the physical source unit. Same-source
ratios need the physical source line and the same-source response certificate,
but not the absolute unit on that line.

Thus the source-selector wall should be read as two different gates:

```text
W_source_line:
  identify the physical source deformation line / same-source surface.

W_source_unit:
  identify the absolute unit on that source line.
```

Rows that require an absolute source/action coefficient need both. Rows that
require only a strict same-source response ratio can bypass `W_source_unit`,
but they still need `W_source_line` and the response-surface evidence.

## Finite Theorem

Let `h` be a local coordinate on a supplied physical source line. Let `A(h)` and
`B(h)` be differentiable scalar responses on the same source surface, with
`B'(0) != 0`.

For any reparameterization

```text
h = f(s),   f(0)=0,   f'(0) != 0,
```

the chain rule gives:

```text
dA/ds |0 = dA/dh |0 * f'(0),
dB/ds |0 = dB/dh |0 * f'(0).
```

Therefore

```text
(dA/ds |0) / (dB/ds |0)
  = (dA/dh |0) / (dB/dh |0).
```

The special source-unit rescaling `h = lambda s` is the same result with
`f'(0)=lambda`. Absolute derivatives are not invariant:

```text
dA/ds |0 = lambda * dA/dh |0.
```

So unit-free source claims must be ratio claims on the same source line.

## Finite Witness

Let

```text
A(h) = A0 + a h + q h^2,
B(h) = B0 + b h + r h^2,
b != 0.
```

At the source origin:

```text
A'(0) = a,
B'(0) = b,
A'(0)/B'(0) = a/b.
```

Under `h = lambda s + beta s^2`:

```text
dA/ds |0 = lambda a,
dB/ds |0 = lambda b,
(dA/ds)/(dB/ds) |0 = a/b.
```

If `A` and `B` are not on the same source line, for example

```text
A(h) = A0 + lambda_A a h,
B(h) = B0 + lambda_B b h,
```

then the ratio is

```text
lambda_A a / (lambda_B b),
```

and arbitrary relative source units do not cancel. The same-source condition is
load-bearing.

## Relation To The Source Stack

The source/action RN factorization proves that record-facing action-exponent
deformations and RN/Fisher source coordinates are the same finite tangent
coordinate once a source surface is supplied.

The physical-source independence theorem proves that the present post-axiom
premise stack does not choose the physical source direction or unit.

This theorem sits between them. It proves that an absolute-unit selector is
only needed for absolute coefficients. It is not needed for ratios of responses
to the same source coordinate.

For `Y_T`, this explains why the strict top/W pole-response route has the right
shape:

```text
same physical source h
  -> (dM_t/dh)/(dM_W/dh)
```

is source-unit invariant. That route still needs the same-source pole-response
certificate, top coefficient evidence, same-scale `g_2` authority if a
numerical `y_t` is claimed, and matching/running if measured-scale output is
claimed.

## What Moves

| Prior residual | Effect of this theorem |
|---|---|
| physical source direction and unit as one broad wall | split into source-line selection and absolute-unit selection |
| absolute source coefficients | still require source unit |
| same-source response ratios | source unit cancels once same-source surface is supplied |
| `Y_T` same-source route | formally justified as a unit-bypass route, not a physical-response proof |
| finite RN/action algebra | unchanged; it supplies tangent calculus, not the physical source line |

## What Remains

The framework still needs:

- a physical source-line selector for each claimed physical deformation;
- strict same-source response evidence when using ratio claims;
- a physical absolute-unit selector for absolute coefficients;
- metric/observable semantics for measured quantities;
- gauge-coupling, matching, running, and empirical-comparator bridges where
  those are claimed.

This theorem does not supply any of those selectors. It only prevents the
source-unit wall from being overcounted in same-source ratio lanes.

## Audit Consequence If Retained

Rows should distinguish:

```text
absolute coefficient claim:
  source line + source unit + observable semantics required.

same-source ratio claim:
  source line + same-source response surface + observable semantics required;
  source unit cancels.
```

For `Y_T`, a strict top/W response-ratio certificate can bypass the absolute
source-unit selector, but cannot bypass the same-source physical surface,
top-response coefficient, gauge-coupling authority, or measured-scale bridges.

## Non-Claims

This note does not claim:

- physical source selection is derived;
- the absolute source unit is derived;
- `Y_T`, `y_33`, `y_t`, `m_t`, or `g_2` is derived;
- strict same-source top/W evidence exists;
- matching/running or metric/observable semantics are closed;
- record occurrence, probability, theta, readout selection, or empirical
  frequency semantics are closed;
- a new ontology axiom or registered primitive is required.

## Minimum Foundation Update If Bridge Work Fails

No ontology axiom update follows from this theorem.

If bridge-first routes fail and owner governance chooses an approved
operational primitive, the `P_physical_source` target should distinguish source
line and source unit:

```text
On a supplied record-facing action/RN surface, a physical source selector may
identify a physical source line. Absolute coefficients additionally require a
physical unit on that line; same-source response ratios do not.
```

That would be an operational primitive, not a change to Lattice, Qubit,
Admissibility, or Record.

## No-Go Discipline Gate

**Status:** PASS for bounded source-wall narrowing. This is not a terminal
no-go against source selection. It is a positive theorem showing when the
source-unit wall is load-bearing and when it cancels.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| Absolute coefficient route | Use a single derivative `dA/dh` as a physical coefficient. | UNIT REQUIRED: a source-unit selector is load-bearing. |
| Same-source ratio route | Use `(dA/dh)/(dB/dh)` on the same source line. | ATTEMPTED here: source unit cancels. |
| Different-source ratio route | Divide derivatives taken with independent source units. | ATTEMPTED here: relative units remain and the route fails without a same-source certificate. |
| RN/action factorization route | Use finite source calculus to pick the physical source line. | RULED OUT BY PRIOR as full closure: it supplies tangent algebra, not physical line selection. |
| YT top/W response route | Use strict top/W pole responses to bypass the source unit. | OPEN: algebraic unit cancellation is valid, but evidence and same-source surface remain missing. |
| New primitive route | Register physical source selection as an approved operational premise. | OWNER-GOVERNANCE ROUTE: available only if bridge-first work fails or is intentionally bypassed. |

### N2 - Wall-Independence Audit

Collapsed residuals after this theorem:

```text
W_source_line
W_source_unit
```

For absolute coefficients, both walls are load-bearing. For same-source ratios,
`W_source_unit` cancels, but `W_source_line` remains load-bearing because
"same source" is exactly the physical-line claim.

### N3 - Hidden-Wall Scan

| Term | Classification |
|---|---|
| `supplied physical source line` | Explicit theorem input; not derived here. |
| `same source surface` | Load-bearing condition for unit cancellation. |
| `observable semantics` | Downstream metric/observable bridge, not supplied here. |
| `source unit` | The absolute normalization on the source line; only needed for absolute coefficients. |
| `approved primitive` | Checked against `docs/audit/data/axiom_premise_nodes.json`; no physical-source primitive is registered. |

No hidden admission is used to select a physical source line or unit.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|
| `PHYSICAL_SOURCE_SELECTOR_INDEPENDENCE_2026-07-01` | physical source direction and unit remain. | split into line and unit use cases. | yes |
| `SOURCE_ACTION_RN_FACTORIZATION_FROM_RECORD_BORN_INTERFACE_2026-06-30` | action/RN factorization leaves physical source direction and unit. | supplies tangent surface; selectors remain. | yes |
| `YT_SOURCE_UNIT_POST_AXIOM_RN_REDUCTION_BRIDGE_2026-07-01` | physical top intervention or strict same-source response remains. | explains the ratio bypass route. | yes |
| `YT_STRICT_SAME_SOURCE_TOP_W_POLE_ROW_CONTRACT_NOTE_2026-05-30` | strict same-source evidence contract remains. | same-source condition is load-bearing. | yes |
| `YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25` | response-ratio algebra valid; physical evidence missing. | same algebra generalized. | yes |
| `MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01` | `P_physical_source` is a fallback candidate, not registered. | same candidate, refined by line/unit split. | yes |

### N5 - Rhetoric Audit

The proven sentence is only:

```text
Same-source first-derivative ratios are invariant under source-coordinate
rescaling at the source origin.
```

It is tested at the one-source-line, first-derivative, finite scalar-response
resolution. It is not a claim about all nonlinear response functions, all
finite-difference ratios, different-source ratios, absolute coefficients, or
measured observables.

### N6 - Partial-Closure Path Scan

Live closure paths remain:

- derive a physical source-line selector for the claimed deformation;
- derive a physical source-unit selector for absolute coefficient claims;
- prove strict same-source response evidence and use the unit-free ratio route;
- derive metric/observable semantics for measured responses;
- explicitly approve and register a narrow physical-source primitive if owner
  governance chooses that route.

The primitive-registry check confirms that no current approved primitive grants
physical source line or unit selection.

### N7 - Steelman

A hostile reviewer can argue that a same-source ratio is useless until the
physical source line and response observables are already identified, so this
theorem does not close the hard physics. That objection is correct. The theorem
does not claim closure; it prevents an unnecessary unit wall from being counted
after a genuine same-source response certificate is supplied.

### N8 - Cross-Cycle Echo

Earlier source/action and metric/observable rows repeatedly separated unit
normalization from normalized response ratios. This note applies that split to
the physical-source wall itself: absolute coefficients need units, while
same-source ratios cancel them. The same pattern appears in the YT top/W
response contract and in the metric/observable source-response interface.

## Verification

Run:

```bash
python3 scripts/source_response_ratio_unit_cancellation_normal_form_2026_07_01.py
```

Expected close:

```text
TOTAL: PASS=74 FAIL=0
```
