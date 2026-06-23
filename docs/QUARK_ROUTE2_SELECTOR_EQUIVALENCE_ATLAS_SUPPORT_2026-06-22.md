# Quark Route-2 Selector Equivalence Atlas Support

**Date:** 2026-06-22
**Type:** exact-support / upstream selector-equivalence atlas
**Actual current-surface status:** exact-support for an endpoint-free selector-equivalence atlas; not current-surface closure
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_selector_equivalence_atlas_support_2026_06_22.py`](../scripts/frontier_quark_route2_selector_equivalence_atlas_support_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_selector_equivalence_atlas_support_2026_06_22.txt`](../outputs/frontier_quark_route2_selector_equivalence_atlas_support_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Blocks102-146 exposed several names for the remaining Route-2 selector:

- binary source-measure `2:1` or `1:2` bias;
- sharp-record displacement `|h| = (1/2) log 2`;
- same-source one-point product `E[X]E[Y] = 1/9`;
- formal binary source-jet parameter `p in {1/3, 2/3}`;
- physical covariance score lift for `O_CR`;
- connected Hessian value `8/9`;
- `kappa=0`.

This packet records the exact endpoint-free implication map among those
selectors, and names the typed source/readout clauses needed before any formal
selector becomes physical Route-2 closure.

## General Product Selector

Assume the same physical Route-2 source supplies typed readout variables
`X,Y` with raw same-source moment

```text
E[XY] = 1.
```

Let

```text
u = E[X],  v = E[Y].
```

P-cal connected subtraction gives

```text
D^2 log Z = E[XY] - E[X]E[Y] = 1 - uv.
```

With the Route-2 normalization used by the existing support packets,

```text
kappa = 9 * ((1 - uv) - 8/9).
```

Therefore, under this same-source raw-moment contract,

```text
kappa = 0  <=>  uv = 1/9  <=>  D^2 log Z = 8/9.
```

This is the broad selector. It does not require binary outcomes by itself.

## Binary Same-Record Subcase

If a stronger same-source theorem proves a normalized binary same-record
source

```text
X = Y = epsilon in {-1,+1},
P(epsilon=+1)=q,
m = E[epsilon] = 2q - 1,
```

then `uv = m^2`. In this subcase:

```text
kappa = 0
<=> m^2 = 1/9
<=> |m| = 1/3
<=> q in {1/3, 2/3}
<=> P(+1):P(-1) is 1:2 or 2:1.
```

In the sharp-record RN chart with

```text
q/(1-q) = exp(2h),
```

this is equivalently

```text
|h| = (1/2) log 2.
```

Thus the log-odds and `2:1` formulations are exact binary subcase
representatives of the broader product selector.

## Formal Binary Source-Jet Subcase

For the formal source-jet family

```text
Z_p[J] = p exp(J) + (1-p) exp(-J),
```

the zero-source one-point and connected Hessian are

```text
D Z = 2p - 1,
D^2 log Z = 1 - (2p - 1)^2.
```

Hence

```text
p in {1/3, 2/3}
<=> (D Z)^2 = 1/9
<=> D^2 log Z = 8/9
<=> kappa = 0.
```

This is exactly the formal support identified in Block143. Block144 and
Block145 still prevent reading `p=2/3` or `p=1/3` as the physical Route-2
source without an added physical typing theorem.

## Physical Typing Boundary

The atlas is endpoint-free algebra, not a physical Route-2 closure.

To consume any node of the atlas as the cross-domain bridge, a future theorem
must prove at least one of the following on the physical same-source
`P_R/E-T` surface:

```text
T1. General product selector:
    same-source variables X,Y, raw E[XY]=1, and E[X]E[Y]=1/9.

T2. Binary bias selector:
    binary same-record source/readout plus q in {1/3, 2/3}.

T3. Log-odds selector:
    sharp-record source path with |h|=(1/2)log 2 and binary same-record typing.

T4. Source-jet selector:
    physical J_CR typing of Z_p[J] plus p in {1/3, 2/3}.

T5. Covariance-score selector:
    physical O_CR, source coordinate J_CR, tau_sc-odd RN score, and
    same-source Fisher-unit Riesz identification with the Block121 scalar.
```

Without those typed clauses, the existing formal selectors remain support or
no-go boundaries. No endpoint value is used as an input, and the atlas does
not import `c_TE=-8/9`, `rho_E`, `q_E`, observed quark values, fitted
selector choices, or endpoint-value reversal.

## Missing Primitive

The sharpened remaining primitive is:

```text
Route-2 typed selector theorem:

prove one atlas selector on the physical same-source P_R/E-T source/readout
surface, and prove the required raw-moment, connected-subtraction, covariance
score, or Fisher-unit Riesz typing without importing the endpoint value.
```

Expected runner result:

```text
TOTAL: PASS=113, FAIL=0
```
