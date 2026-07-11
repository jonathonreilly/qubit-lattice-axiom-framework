# Admissible One-Step Record-Write Class: Controlled-Copy Narrow Theorem

**Date:** 2026-07-11
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/record_write_admissible_one_step_class_controlled_copy_2026_07_11.py`](../scripts/record_write_admissible_one_step_class_controlled_copy_2026_07_11.py)
**Cache:** [`logs/runner-cache/record_write_admissible_one_step_class_controlled_copy_2026_07_11.txt`](../logs/runner-cache/record_write_admissible_one_step_class_controlled_copy_2026_07_11.txt)

## Purpose

This note supplies the class step in the rule-universality campaign: it classifies the admissible one-step write on the minimal finite representative under declared finite-surface readings of the Record clauses. A grain-universality consumer, if pursued, is a separate next-note task; no such consumer result is asserted or promised here.

## Theorem

Let `H_S = C^2` have pointer projectors `P_0` and `P_1`, with

```text
P_i P_j = delta_ij P_i,  P_i^dagger = P_i,  P_0 + P_1 = I_S.
```

Let `H_R = C^2` be one fresh record register with supplied blank vector `|b>`.
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

| Label | Verbatim Record clause | Declared finite-surface constraint |
|---|---|---|
| C1 | “When present, a record locks exactly one admissible local possibility.” | The register outputs conditioned on `P_0` and `P_1` have orthogonal support. After C3, “exactly one” and no undetermined lock are additionally read to exclude a hidden possibility-dependent Kraus label: up to fixed register phases, `|v_{a i}> = c_a |v_i>` with the same coefficient `c_a` for both `i`, and `<v_0|v_1> = 0`. This rank-one-in-Kraus-index condition is a declared assumption. |
| C2 | “A site never carries more than one record; records are permanent.” | On each admissible matched written branch, repeating the write leaves `P_i H_S tensor span(|v_i>)` fixed up to phase. The written content is neither overwritten nor sent back to the blank ray. This is branchwise idempotent stability on the classical written-record sectors. |
| C3 | “Only records are readable. A readout value is determined by record content alone.” | The write is pointer non-demolition. Memberwise, `A_a P_i = (P_i tensor I_R) A_a P_i`; equivalently all off-diagonal pointer blocks vanish, so `A_a = sum_i P_i tensor |v_{a i}>`. The write does not move the locked possibility. |
| C4 | “For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`.” | The empty/blank content has readout zero, while a written `|v_i>` has only its pointer-determined readout label; disjoint-record readouts add. This is readout normalization only. No numerical readout value is imported or inferred. |

Under C1–C4 and blank-input trace preservation, choose the common Kraus
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
general `4 x 4` Kraus family, C3 imposes

```text
(P_1 tensor I_R) K_a B P_0 = 0,
(P_0 tensor I_R) K_a B P_1 = 0.
```

The R2 symbolic linear solve finds four independent constraints. Exactly four
blank-input entries survive, arranged as two general conditional vectors:

```text
A_a = P_0 tensor |v_{a0}> + P_1 tensor |v_{a1}>.
```

C1 next imposes orthogonal conditional record support. Its explicitly flagged
no-hidden-Kraus-label reading makes the coefficient array rank one in the
Kraus index, so fixed register phases can be absorbed into vectors satisfying
`|v_{ai}> = c_a |v_i>`. Hence `A_a = c_a V`. Blank-input trace preservation
then gives

```text
I_S = sum_a A_a^dagger A_a
    = (sum_a |c_a|^2)
      (||v_0||^2 P_0 + ||v_1||^2 P_1).
```

With `sum_a |c_a|^2 = 1`, R3 solves `||v_0|| = ||v_1|| = 1`, verifies
`<v_0|v_1> = 0`, and computes `V^dagger V = I_S`. It also computes directly
that the full common-vector Kraus sum is the single channel
`rho -> V rho V^dagger`. As a scope witness, R3 also computes that the
rank-two dephasing family is trace preserving but differs from the `V` channel;
the declared no-hidden-Kraus-label condition is therefore load-bearing.

For C2, the unique allowed action of a repeat extension **on each
one-dimensional admissible written record ray** is multiplication by a phase;
therefore its content projector is fixed. R4 constructs a trace-preserving
extension that fixes both matched branch projectors and every classical
mixture of them. No uniqueness is asserted for its action off those admissible
written sectors. The same block constructs a trace-preserving eraser to the
blank ray and computes that it moves both written projectors, so the eraser is
excluded by C2. R5 finally writes a general orthonormal record pair as the
columns of a register unitary `U_R` and checks

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
- C1–C4 are declared readings at this finite surface. The runner proves their
  implication; it does not prove that the English clauses require those
  readings.
- Most importantly, C1's no-hidden-possibility-dependent-Kraus-label condition
  is assumed. Without it, orthogonal outputs, pointer non-demolition,
  normalization, and branchwise permanence admit a dephasing multi-Kraus
  counterexample and do not force an isometry channel.
- The classified object is the blank-input restriction `{K_a B}`. C2 uniquely
  fixes content on each admissible written record ray up to phase, but no
  global off-sector Kraus extension is classified or selected.
- No rule/site/weight/rate selection and no formation time, Hamiltonian,
  coupling, probability law, or register-basis selection is supplied.
- There is no `occupancy`, `r`, `delta`, or `AC_phi_lambda` value content. C4
  supplies only the empty/blank readout normalization and symbolic
  pointer-determined labels; it supplies no numerical value.

## Load-bearing dependencies

| Dependency | Consumed content |
|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Supplies the four verbatim Record-clause quotations; the operator readings remain declared here rather than imported as memo theorems. |
| [`RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md`](RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md) | Verbatim consumed surface: “In the explicit finite pointer-record model of [`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md), the nonzero controlled-copy kick on a fresh blank fragment derives the projective record-write isometry used by the target bridge `RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md`.” |
| [`RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md`](RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md) | Verbatim consumed surface: “The extracted blocks are exactly projective Kraus operators: `K_r = <r| W = P_r`.” This is the downstream Kraus bridge form matched by the classified `V`. |
| [`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md`](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md) | Load-bearing boundary authority: occurrence is axiom-supplied, while formation rule/process/state/site/weight/rate are not forced. |

## Runner verification map

| Block | Exact verification | Result |
|---|---|---:|
| R1 | Flattened-whitespace verbatim checks for all four quoted Record clauses | `PASS=4 FAIL=0` |
| R2 | General `4 x 4` operator, blank embedding, symbolic C3 solve, and exact two-vector surviving form | `PASS=4 FAIL=0` |
| R3 | Conditional orthogonality, normalization solve, isometry, common-vector Kraus-family reduction, and the weaker dephasing witness | `PASS=8 FAIL=0` |
| R4 | Branchwise repeat stability, unique record-ray content up to phase, and normalized eraser control | `PASS=8 FAIL=0` |
| R5 | General register-unitary frame and single-orbit covariance | `PASS=3 FAIL=0` |
| R6 | Non-correlating, pointer-demolishing, erasing, and contracting negative controls | `PASS=4 FAIL=0` |
| R7 | Verbatim consumed-scope sentences from the controlled-copy and Kraus-bridge dependencies | `PASS=2 FAIL=0` |

Run:

```text
python3 scripts/record_write_admissible_one_step_class_controlled_copy_2026_07_11.py
```

Cached run result:

```text
TOTAL: PASS=33 FAIL=0
```

**No check passes by literal stipulation.**
