# Admissible One-Step Record-Write Class: Controlled-Copy Narrow Theorem

**Date:** 2026-07-11
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/record_write_admissible_one_step_class_controlled_copy_2026_07_11.py`](../scripts/record_write_admissible_one_step_class_controlled_copy_2026_07_11.py)
**Cache:** [`logs/runner-cache/record_write_admissible_one_step_class_controlled_copy_2026_07_11.txt`](../logs/runner-cache/record_write_admissible_one_step_class_controlled_copy_2026_07_11.txt)

## Purpose

This note classifies the admissible one-step write on the minimal finite
representative under declared finite-surface readings of the Record clauses.
It does not assert grain-wide universality or any downstream consumer result.

## Theorem

Let `H_S = C^2` have pointer projectors `P_0` and `P_1`, with

```text
P_i P_j = delta_ij P_i,  P_i^dagger = P_i,  P_0 + P_1 = I_S.
```

Let `H_R = C^2` be one fresh record register with supplied blank preparation
vector `|b>`. The preparation ray is not a third orthogonal outcome and does
not by itself encode whether a record is present.
For a joint completely positive trace-preserving map with Kraus family
`{K_a}` on `H_S tensor H_R`, define the blank embedding and its restricted
Kraus blocks by

```text
B = I_S tensor |b>,
A_a = K_a B : H_S -> H_S tensor H_R.
```

The following table does not claim to derive operator constraints from English
prose. Each row is this note's **declared reading** of the quoted Record clause
on this finite surface. The theorem is conditional on all four readings, and
the runner checks their algebraic implication rather than validating the
readings themselves.

| Declared reading | Verbatim Record clause | Declared finite-surface constraint |
|---|---|---|
| **Locked-possibility/no-hidden-label reading (C1)** | “When present, a record locks exactly one admissible local possibility.” | The register outputs conditioned on `P_0` and `P_1` have orthogonal support. After the pointer non-demolition reading (C3), “exactly one” and no undetermined lock are additionally read to exclude a hidden possibility-dependent Kraus label: up to fixed register phases, `|v_{a i}> = c_a |v_i>` with the same coefficient `c_a` for both `i`, and `<v_0|v_1> = 0`. This rank-one-in-Kraus-index condition is a declared assumption. |
| **Written-projector permanence reading (C2)** | “A site never carries more than one record; records are permanent.” | On each admissible matched written branch, the repeat channel fixes the joint content projector onto `P_i H_S tensor span(|v_i>)`. No orthogonality or distinguishability between the supplied preparation ray `|b>` and a written register ray is asserted. This is branchwise idempotent stability on the classical written-record sectors. |
| **Pointer non-demolition reading (C3)** | “Only records are readable. A readout value is determined by record content alone.” | The write is pointer non-demolition. Memberwise, `A_a P_i = (P_i tensor I_R) A_a P_i`; equivalently all off-diagonal pointer blocks vanish, so `A_a = sum_i P_i tensor |v_{a i}>`. The write does not move the locked possibility. |
| **Absent-record normalization/additivity reading (C4)** | “For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`.” | The absence of a record contributes readout zero; once a record is present, its symbolic readout label depends only on its locked content, and disjoint-record readouts add. This semantic normalization imposes no additional Hilbert-space relation among `|b>`, `|v_0>`, and `|v_1>`. No numerical readout value is imported or inferred. |

Under the four declared readings (C1–C4) and blank-input trace preservation,
choose the common Kraus
normalization `sum_a |c_a|^2 = 1`. Then

```text
A_a = c_a V,
V = P_0 tensor |r_0> + P_1 tensor |r_1>,
<r_i|r_j> = delta_ij,
sum_a A_a rho A_a^dagger = V rho V^dagger,
V^dagger V = I_S.
```

Thus every admissible blank-input one-step write under these declared readings
is, up to a register basis unitary and register phase choice, in the
controlled-copy isometry class. In particular, no admissible non-isometric
one-step write exists on this declared surface.

## Proof sketch

Choose a register basis in which `|b> = |0>`. For each member of a fully
general `4 x 4` Kraus family, the pointer non-demolition reading (C3) imposes

```text
(P_1 tensor I_R) K_a B P_0 = 0,
(P_0 tensor I_R) K_a B P_1 = 0.
```

The pointer-block symbolic linear solve finds four independent constraints.
Exactly four
blank-input entries survive, arranged as two general conditional vectors:

```text
A_a = P_0 tensor |v_{a0}> + P_1 tensor |v_{a1}>.
```

The locked-possibility/no-hidden-label reading (C1) next imposes orthogonal
conditional record support. Its explicitly flagged
no-hidden-Kraus-label reading makes the coefficient array rank one in the
Kraus index, so fixed register phases can be absorbed into vectors satisfying
`|v_{ai}> = c_a |v_i>`. Hence `A_a = c_a V`. Blank-input trace preservation
then gives

```text
I_S = sum_a A_a^dagger A_a
    = (sum_a |c_a|^2)
      (||v_0||^2 P_0 + ||v_1||^2 P_1).
```

With `sum_a |c_a|^2 = 1`, the isometry check solves
`||v_0|| = ||v_1|| = 1`, verifies
`<v_0|v_1> = 0`, and computes `V^dagger V = I_S`. It also computes directly
that the full common-vector Kraus sum is the single channel
`rho -> V rho V^dagger`. As a scope witness, the same block also computes that the
rank-two dephasing family is trace preserving but differs from the `V` channel;
the declared no-hidden-Kraus-label condition is therefore load-bearing.

For the written-projector permanence reading (C2), a CPTP repeat family
`{L_mu}` that fixes a one-dimensional admissible written ray obeys
`L_mu|q_i> = lambda_{mu i}|q_i>` memberwise, with
`sum_mu |lambda_{mu i}|^2 = 1`. Individual coefficients need not be phases;
the channel-level content projector is fixed. The permanence block constructs
a trace-preserving extension that fixes both matched branch projectors and
every classical mixture of them. No uniqueness is asserted for its action off
those admissible written sectors. The same block constructs a trace-preserving
reset to the supplied blank register ray and computes that it overwrites the
`P_1` written projector while leaving the already coincident `P_0` register ray
unchanged, so the reset is excluded by C2. The unitary-orbit block finally
writes a general orthonormal record pair as the columns of a register unitary
`U_R` and checks

```text
(I_S tensor U_R) V_canonical
  = P_0 tensor U_R|0> + P_1 tensor U_R|1>.
```

The class is therefore one register-unitary orbit, with column phases included
in `U_R`.

## What is not derived

The boundary authority
[`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md`](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md)
states: “The surviving no-go is only: the current minimal axioms do **not**
force the formation rule/process/state/site/weight/rate.” This theorem respects
that boundary. “Records form.” supplies occurrence; the present result only
classifies the admissible one-step write **class**, conditional on C1–C4's
declared finite-surface readings.

It does not select which admissible possibility is recorded, when a write
occurs, the formation process or triggering state, at which site it occurs,
or with what probability/weight/rate. It does not select the register basis.
Those are precisely the unforced formation rule/process/state/site/weight/rate
and convention slots, not outputs of this classification.

## Scope boundary

- The carrier is only the minimal finite representative `C^2 tensor C^2`: one
  system-qubit possibility pair and one fresh blank record register.
- The four named readings (C1–C4) are declared at this finite surface. The runner proves their
  implication; it does not prove that the English clauses require those
  readings.
- Most importantly, the locked-possibility/no-hidden-label reading (C1)
  assumes the no-hidden-possibility-dependent-Kraus-label condition. Without
  it, orthogonal outputs, pointer non-demolition,
  normalization, and branchwise permanence admit a dephasing multi-Kraus
  counterexample and do not force an isometry channel.
- The classified object is the blank-input restriction `{K_a B}`. The
  written-projector permanence reading (C2) fixes the channel-level content
  projector on each admissible written record ray, but no
  global off-sector Kraus extension is classified or selected.
- The supplied preparation ray may coincide with a written register ray. This
  two-dimensional carrier does not model a separate record-presence flag, and
  no blank-versus-written Hilbert-space distinguishability is claimed.
- No rule/site/weight/rate selection and no formation time, Hamiltonian,
  coupling, probability law, or register-basis selection is supplied.
- There is no `occupancy`, `r`, `delta`, or `AC_phi_lambda` value content. The
  absent-record normalization/additivity reading (C4) supplies only
  `I(empty)=0`, additivity, and symbolic content-determined labels; it supplies
  no numerical value or blank/output-ray constraint.

## Load-bearing dependencies

| Dependency | Consumed content |
|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Supplies the four verbatim Record-clause quotations; the operator readings remain declared here rather than imported as memo theorems. |
| [`RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md`](RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md) | Verbatim consumed surface: “In the explicit finite pointer-record model of [`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md), the nonzero controlled-copy kick on a fresh blank fragment derives the projective record-write isometry used by the target bridge `RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md`.” |
| [`RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md`](RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md) | Verbatim consumed surface: “The extracted blocks are exactly projective Kraus operators: `K_r = <r| W = P_r`.” This is the downstream Kraus bridge form matched by the classified `V`. |
| [`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md`](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md) | Load-bearing boundary authority: occurrence is axiom-supplied, while formation rule/process/state/site/weight/rate are not forced. |

## Runner verification map

| Verification block | Exact verification | Result |
|---|---|---:|
| Record-clause quotations | Flattened-whitespace verbatim checks for all four quoted Record clauses | `PASS=4 FAIL=0` |
| Pointer non-demolition block solve | General `4 x 4` operator, blank embedding, symbolic pointer-block solve, and exact two-vector surviving form | `PASS=4 FAIL=0` |
| Rank-one Kraus/isometry classification | Conditional orthogonality, normalization solve, isometry, common-vector Kraus-family reduction, and the weaker dephasing witness | `PASS=8 FAIL=0` |
| Written-projector permanence | Branchwise repeat stability, channel-level record-projector preservation, and normalized reset-to-blank control | `PASS=8 FAIL=0` |
| Register-unitary orbit | General register-unitary frame and single-orbit covariance | `PASS=3 FAIL=0` |
| Named negative controls | Non-correlating, pointer-demolishing, resetting, and contracting controls | `PASS=4 FAIL=0` |
| Dependency-scope quotations | Verbatim consumed-scope sentences from the controlled-copy and Kraus-bridge dependencies | `PASS=2 FAIL=0` |

Run:

```text
python3 scripts/record_write_admissible_one_step_class_controlled_copy_2026_07_11.py
```

Cached run result:

```text
TOTAL: PASS=33 FAIL=0
```

**No check passes by literal stipulation.**
