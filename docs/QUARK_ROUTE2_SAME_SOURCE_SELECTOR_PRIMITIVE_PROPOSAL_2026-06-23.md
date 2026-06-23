# Quark Route-2 Same-Source Selector Primitive Proposal

**Date:** 2026-06-23
**Type:** open / candidate Route-2 primitive proposal
**Actual current-surface status:** open; candidate primitive proposal pending external adoption
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_same_source_selector_primitive_proposal_2026_06_23.py`](../scripts/frontier_quark_route2_same_source_selector_primitive_proposal_2026_06_23.py)
**Cached output:** [`outputs/frontier_quark_route2_same_source_selector_primitive_proposal_2026_06_23.txt`](../outputs/frontier_quark_route2_same_source_selector_primitive_proposal_2026_06_23.txt)
**Panel certificate:** [`.claude/science/physics-loops/s3-route2-same-source-selector-primitive-proposal/PANEL_CERTIFICATE.md`](../.claude/science/physics-loops/s3-route2-same-source-selector-primitive-proposal/PANEL_CERTIFICATE.md)

This is not an audit verdict. It does not run audit workers, does not apply
audit outcomes, and does not edit the primitive registry.

## Primitive Statement

The proposed primitive is the following Route-2 source/readout interface:

```text
Route-2 same-source selector primitive:

There is one physical Route-2 source/readout surface with:

```text
Omega_R: finite Route-2 record source space;
P_0: strictly positive normalized reference law on Omega_R;
P_h: normalized Route-2 source path with P_h << P_0 near h=0;
J_CR: physical center-ratio source coordinate for that path;
X,Y: physical P_R/E-T center-ratio readout variables on Omega_R.
```

The primitive states that these objects satisfy:

S1. same-source typing:
    X and Y are measurable readouts of this one physical Route-2
    source/readout surface, and the connected response is formed on P_0;

S2. sharp co-record raw moment:
    X^2 = Y^2 = 1 and X = Y P_0-almost surely, hence E_0[XY] = 1;

S3. cubic one-axis one-point magnitude:
    E_0[X] = s/3 and E_0[Y] = s/3 for a common orientation sign
    s in {-1,+1};

S4. connected-subtraction typing:
    the physical connected readout is the P_0 covariance
    E_0[XY] - E_0[X]E_0[Y], equivalently the mixed second derivative of
    log Z for the typed X,Y source insertion on the same source law;

S5. source/readout unit identification:
    the normalized Fisher/Riesz source unit of J_CR is identified with the
    physical P_R/E-T center-ratio readout unit, so the source-to-readout
    coupling is mu = 1 rather than a fitted or external scale;

S6. orientation separation:
    the primitive includes the Route-2 E-to-T orientation datum sigma_TE = -1
    and applies it only after kappa=0 is fixed by S1-S5.
```

The primitive is intentionally a single Route-2 bridge premise. It is not a
claim that the six clauses are already derived from `Lattice + Quantum +
Record`, from the existing approved framework primitives, or from the
previous Route-2 support stack.

## Why This Is A Candidate Primitive

Block150 showed that the current non-duplicative source/readout route queue is
exhausted unless a new physical same-source selector realization is supplied.
Blocks147-149 also show exactly what the missing object must contain:

- same-source physical variables;
- `Omega_R`, positive `P_0`, normalized `P_h << P_0`, and physical `J_CR`;
- raw moment `E[XY]=1`;
- connected-subtraction typing;
- one-point product `E[X]E[Y]=1/9`;
- physical unit identification `mu=1`;
- orientation datum `sigma_TE=-1` consumed after the connected magnitude is
  fixed.

This proposal packages those conditions in their smallest current
source/readout form. Clause S3 supplies the product selector through a cubic
one-axis one-point magnitude:

```text
E_0[X]E_0[Y] = (s/3)(s/3) = 1/9.
```

It does not quote the endpoint value. The fraction `1/3` is stated as a
Route-2 source/readout primitive magnitude on the cubic physical readout
surface, not as a fitted comparator or reverse-engineered mass ratio.

## Consequence If Accepted

Under S1-S4:

```text
C_conn = E_0[XY] - E_0[X]E_0[Y]
       = 1 - 1/9
       = 8/9.
```

Using the existing Block147 normalization,

```text
kappa = 9 * (C_conn - 8/9) = 0.
```

With S5 and the already separated orientation convention of S6, the signed
Route-2 center-ratio readout becomes

```text
c_TE = -1 * 1 * C_conn = -8/9.
```

The proposal therefore supplies exactly the bridge object that Block150 names.
It should be judged as a candidate primitive first. Only after explicit
acceptance could downstream notes cite it as an adopted input.

## What This Does Not Do

- It does not add or amend the framework axioms.
- It does not edit `docs/audit/data/axiom_premise_nodes.json`.
- It does not assert that this primitive is already accepted.
- It does not import `rho_E`, `q_E`, observed quark values, fit-derived
  source weights, a target comparator, or endpoint-value reversal.
- It does not derive a probability law from the current framework baseline.
- It does not permit a weakened bridge: omitting any of S1-S6 reopens the
  countermodels from Blocks148-150.
- It does not hide source-law, unit, or orientation premises: those are part
  of the proposed primitive clauses.
- It does not change any audit verdict.

## Panel Acceptance Gate

The branch-local panel asks only whether the statement is valid as a proposed
primitive:

```text
P1. Is the primitive mathematically coherent?
P2. Is it endpoint-independent?
P3. Is it non-circular relative to kappa=0 and c_TE=-8/9?
P4. Is it narrow enough to be a single Route-2 source/readout premise?
P5. Are the non-laundering boundaries clear enough to prevent silent status
    promotion?
```

The panel certificate is required before this branch may describe the proposal
as panel-passed. Even panel passage does not make the primitive accepted by
the repo; it only records that the candidate is clean enough to submit for
human adoption/rejection.

Expected runner result after panel passage:

```text
TOTAL: PASS=95, FAIL=0
VERDICT: the candidate Route-2 same-source selector primitive is internally coherent, endpoint-independent, panel-passed as a primitive proposal, and still open pending external adoption.
```
