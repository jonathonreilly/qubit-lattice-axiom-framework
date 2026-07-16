# The Quantum-Darwinism Record Bridge Remains An Open Local-Observability Gate

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-05
**Claim type:** open_gate
**Status authority:** independent audit lane only. This source note does not
set, predict, or assert an audit verdict and does not claim "retained" or
"promoted" standing.
**Primary runner:**
[`scripts/frontier_darwinism_bridge_residual_2026_06_05.py`](../scripts/frontier_darwinism_bridge_residual_2026_06_05.py)
**Cached log:**
[`logs/runner-cache/frontier_darwinism_bridge_residual_2026_06_05.txt`](../logs/runner-cache/frontier_darwinism_bridge_residual_2026_06_05.txt)
(PASS=19, FAIL=0, peak RSS ~29 MB).

---

## Question

The record-formation pointer-non-demolition note
([`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md))
and the envariance Born note
([`BORN_FROM_ENVARIANCE_CONDITIONAL_ON_STATE_FUNCTIONAL_PROBABILITY_NOTE_2026-06-05.md`](BORN_FROM_ENVARIANCE_CONDITIONAL_ON_STATE_FUNCTIONAL_PROBABILITY_NOTE_2026-06-05.md))
both analyze the same Zurek "Darwinism bridge": that a *record* is a
**redundant, objective** imprint of a system observable broadcast over many
environment fragments. Both notes flag this bridge as outside the current
axiom content.

Is the bridge **forced** from {Quantum, Lattice, Record}, or a genuine
open premise? If open, what is the minimal extra premise, named precisely?

## Result

The Darwinism bridge is **not supplied by the current axioms**. The minimal
extra premise is

> **Local observability of a determined outcome:** the realized record value is
> independently recoverable by each spatially-disjoint local observer
> (many-fragment observer consensus). Equivalently, the determined outcome is
> not merely single-valued but is imprinted *accessibly on each local fragment*.

Neither the Lattice axiom, the Quantum axiom, nor the Record axiom (in either
the 2026-06-04 or the 2026-06-05 wording) supplies this premise. This note does
not register that premise as an approved axiom, primitive, or Tier-A admission.
The runner
proves the classification on an explicit one-system-qubit + four-environment-qubit
model (exact `numpy`, dense `complex128`).

## The four candidate properties of a "record"

| Property | Meaning | Source | In {Quantum, Lattice, Record}? |
|---|---|---|---|
| **Additivity** | `I(R_1 |_| R_2) = I(R_1) + I(R_2)` over **disjoint** records; info **adds** | Record axiom (both wordings) | **yes** |
| **Locality** | observers read **spatially-disjoint** fragments (finite support) | Lattice axiom | **yes** |
| **Objectivity** | a single **determined** value, the same for all who read it | Record 06-05 "realized outcome" clause; **not** in 06-04 | partial (wording-dependent) |
| **Redundancy** | the **same** value recoverable from **many** fragments; info **saturates** at `H_S` | Darwinism bridge | **no** |

The decisive tension: **additivity** is over *distinct* records (independent
information **adds**, scaling with the number of records), whereas
**redundancy** is the *same* record on many fragments (information
**saturates** at the pointer entropy `H_S` and does **not** add). These are
*different* set-function behaviours, so redundancy is prima facie not a
consequence of the additivity axiom — and the runner confirms it is not.

## What the runner verifies (PASS=19, FAIL=0)

### A. Axiom content: additivity vs determined-durable outcome

- The 2026-06-04 Record axiom supplies **only** additive scalar readout
  (`I(R_1 |_| R_2)=I(R_1)+I(R_2)`, `I(empty)=0`). The runner exhibits two
  distinct outcome-label assignments with the **same** additive `I`: additivity
  is **blind to which value** each record carries. So the 06-04 wording carries
  **no** objectivity.
- The 2026-06-05 Record axiom **adds** "a record is the durable registration of
  the realized outcome ... does not change," i.e. a **determined, durable**
  single value. The runner records this as a logically independent attribute:
  additivity can hold with or without it. Objectivity is therefore an extra
  axiom-wording commitment, not a consequence of additivity.

### B. Additivity != redundancy (the counterexample)

- **Redundant broadcast** `a_0|0>_S|0..0>_E + a_1|1>_S|1..1>_E`: each single
  environment fragment carries the **full** pointer record `H_S=0.9183`, and two
  fragments carry **no more** (info **saturates**).
- **Independent records** `prod_k (|00>+|11>)_{S_k E_k}/sqrt2`: Record additivity
  holds exactly (`I_total = sum_k I(pair_k) = 4` bits, info **adds**), yet there
  is **zero** redundancy — a second observer reading a foreign fragment `E_2`
  learns **nothing** about `S_1` (`I(S_1:E_2)=0`).
- Both states are valid records under the additivity axiom; only one is
  redundant. **The additivity axiom does not entail redundant broadcast.**

### C. Objectivity + locality ==> redundancy

- With locality (observers read disjoint single-qubit fragments), requiring that
  **every** local observer recover the **same** determined value from **their
  own** fragment forces each fragment to carry the full record `H_S` — which
  **is** redundancy. So objectivity-under-locality and redundancy are the same
  property.
- **Contrapositive (anti-redundancy witness).** A record whose determined value
  is encoded only in the **global parity** of the environment is additive and
  single-valued, yet **every proper subset** of fragments (1, 2, or 3 of 4)
  recovers **exactly zero** pointer information; only the **complete**
  environment recovers `H_S`. A local observer is **blind**, so local
  objectivity fails maximally. Determinacy + additivity do **not** by themselves
  make the value locally readable.

Conclusion of A-C: redundancy is forced **iff** objectivity is taken in the
strong **operational** sense (a determined value that each local observer can
read from their disjoint fragment). That operational clause -- local readability
/ many-observer consensus -- is exactly the **local-observability** premise, and
it is in **neither** axiom wording.

### D. Classification

- Redundancy is **not** entailed by additivity alone (Test B).
- Redundancy **is** forced by (determined outcome) + (local observability) +
  locality (Test C).
- **Neither** Record wording supplies local observability of the determined
  outcome: 06-04 supplies additivity only; 06-05 supplies a determined, durable
  value for **one** readout context but **no per-fragment local-readability**
  clause.

## Honest scope and impact

- The Record axiom carries **additivity** (both wordings) and, in 06-05,
  **objectivity in the weak determinacy sense** (one durable realized value).
  It does **not** carry **local observability** (broadcast accessibility on each
  disjoint fragment), which is the operational half of Zurek objectivity.
- Under the **06-04** Record wording the open bridge is **larger**: the bridge
  must supply both the determined single value **and** its local broadcast.
  Under the **06-05** wording only the **local-observability** half remains
  outstanding. Either way the bridge remains outside the axioms.
- **Impact on the two notes.** This **confirms** (does not weaken) the open premise
  both notes already flag, and **sharpens** it from "the QD reading of a record
  is a model convention" to a **single named open premise**: *local observability
  of a determined outcome*. The record-formation note's pointer-non-demolition
  equivalence and any envariance/Born work remain **conditional on this same
  bridge**; their conditional status is unchanged, now with the open premise named.
- This is **consistent** with
  [`FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md`](FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md):
  that note showed redundancy/objectivity fixes the pointer **basis** but not
  the sector **weight**; this note shows that the redundancy/objectivity
  machinery **itself** is an open bridge, not derived from the axioms.

## What this note does not claim

- It does **not** derive the Darwinism bridge from {Quantum, Lattice, Record};
  the verdict is the opposite: the bridge remains an open premise.
- It does **not** weaken or contradict the pointer-non-demolition equivalence; it
  pins the shared upstream local-observability premise.
- It does **not** assert that no future principle could supply local
  observability; it states that the **current** three axioms do not.
- It introduces **no** new axiom and changes **no** numerical prediction.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) supplies the
  live Record wording. The 2026-06-04 wording is historical context only. The
  axiom baseline chain-satisfies as an approved premise; it is not a source of
  bounded status.
- The quantum-Darwinism reading of a *record* (recoverable pointer information,
  redundancy, plateau) is the open input under analysis, not a premise this
  note grants.
- All linear-algebra facts (partial trace, von Neumann / mutual information,
  pointer dephasing) are reproven in the runner, not imported.

## Forbidden-imports check

- No PDG values, literature numerical comparators, or fitted selectors consumed.
- Zurek quantum Darwinism is named as standard physics content (the
  framework-scoped machinery already exists in the prior QD note); it is the
  object being classified, not a derivation input.
