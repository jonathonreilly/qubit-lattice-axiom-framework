# The Unique Emergent Time AXIS is Derived from the Record Ontology, Unconditionally — Correcting the "R1 Needs a Decoherence Dynamics" Realist Slip — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** bounded_theorem (the time axis derived from the record ontology) + a realist-slip correction
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/time_axis_from_record_ontology_runner.py`](../scripts/time_axis_from_record_ontology_runner.py)
**Cached output:** [`logs/runner-cache/time_axis_from_record_ontology_runner.txt`](../logs/runner-cache/time_axis_from_record_ontology_runner.txt)

## Audit context

A companion no-go concluded that "R1 (A_min forces record formation) is not unconditionally
forcible" because the RECORD axiom *disclaims* the measurement/decoherence dynamics, with `H=0` /
energy-eigenstate "no-record" witnesses. **That reasoning is a realist slip and is corrected here.**
By the framework's own register-not-read principle
([`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05`](RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md),
meta): **reality *is* the record stack**; pre-record operators/states (a Hamiltonian `H`) are
**reconstructions**, not prerequisites. *"The axiom does not supply the dynamics"* does **not** mean
*"the time axis is not derivable."* The unique time **axis** is derived from the record ontology
**unconditionally**; only the **orientation** is residual (the past hypothesis).

## Safe statement

**Theorem (time axis from the record ontology).** Take the framework premise — there is a reality,
and reality is the record stack: a durable collection of registered outcomes with an additive
non-negative readout `I` (`I(∅)=0`, additive over disjoint records, `I ≥ 0` as a count). Then:

1. **The `I`-grading is intrinsic to the records.** `I` is computed from the record stack **alone**
   — no Hamiltonian appears — and is a **strict monotone** along the durable containment poset (a
   later stack contains earlier registrations). Its level sets are codim-1 spatial slices; its
   gradient is a **unique** direction.
2. **The axis is reconstruction-invariant (ontological).** The time-axis grading is a function of the
   record stack **only**, so *every* pre-record reconstruction `H` underlying the same stack yields
   the **same** axis. The axis is constituted in the records, not contingent on a dynamics.
3. **The spatial `Z³` is reversible.** Within a constant-`I` slice, each axis reflection `x_i ↦ −x_i`
   is an involution preserving the pairwise-distance multiset — no `I`-monotone — so **only** the
   `I`-gradient is timelike.

Therefore the **unique emergent time AXIS = the `I`-gradient of the record stack**, forced
**unconditionally** by the record ontology. The decoherence dynamics the RECORD axiom disclaims is a
**reconstruction** of how the registered `I`-values are computed, **not** a prerequisite for the
records (hence the axis) existing.

## The realist-slip correction (superseding the no-go)

The companion no-go's witnesses — `H=0`, decoupled `H`, energy eigenstates — are **pre-record
reconstructions** whose realized-outcome set is **empty**. An empty record stack is **no reality**
(vacuous), **not** "a reality without time." Treating a reconstruction (`H`) as deciding whether
**records** (reality) exist is exactly the realist slip the register-not-read principle names. So
those witnesses are **not** counterexamples to "given a reality, the time axis is forced." This note
**supersedes** that no-go's conclusion and **upgrades** the companion reduction from "generically
forced" to "**unconditionally** forced (given the record ontology)" for the **axis**.

## The genuine open piece

Only the **orientation** (which `I`-direction is the future) is residual: the `I`-count is
word-reversal invariant, so the sign is fixed by the **past hypothesis** (a low-record boundary),
the standing
[`POST_RECORD_ARROW_ORIENTATION_FIREWALL_2026-06-06`](POST_RECORD_ARROW_ORIENTATION_FIREWALL_2026-06-06.md)
(`retained_no_go`). The axis (foliation + unique gradient direction + spacelike spatial slices) is
forced; the arrow's *sign* is the one true residual, and it is a single bit, not a dynamics.

## Boundary (honest)

- **Axis, not orientation.** The time **axis** (the `I`-gradient / foliation) is forced
  unconditionally; the **orientation** is the past-hypothesis residual.
- **Given a reality.** "Reality is the record stack" is the framework premise; the empty-stack case is
  "no reality," outside the scope of "a reality's time" — not a loophole.
- **Reconstruction-invariance is the load-bearing point.** The axis is a function of the records, not
  of any `H`; the disclaimed dynamics is a reconstruction. This is the register-not-read principle,
  applied — not a new axiom.
- It corrects two prior session notes (the "generically forced" reduction and the "R1 not forcible"
  no-go), both of which mistook a pre-record reconstruction for the reality.

## Forbidden imports check

No new axiom. The record ontology (reality = records) is the framework premise; the `I`-grading is
the RECORD axiom's additive readout; the correction is the (meta) register-not-read principle. The
runner is exact. No dynamics is imported — the point is precisely that none is needed for the axis.

## Runner check breakdown

Class A: (1) the `I`-grading is intrinsic (records-only, no `H`) and strict-monotone over the durable
containment poset; (2) reconstruction-invariance (the axis function takes only the record stack); (3)
the realist-slip correction (empty stack = no reality, not a no-time reality); (4) spatial `Z³`
reversible; (5) the unconditional-axis conclusion. Expected `runner_check_breakdown = {A: N, B: 0, C:
0, D: 0, total_pass: N}`.

## Honest auditor read

By the register-not-read principle, reality is the record stack and a Hamiltonian is a reconstruction.
The additive record count `I` — a function of the records alone — is a strict monotone grading whose
gradient is the unique time axis, with the spatial `Z³` within each constant-`I` slice reversible; the
axis is reconstruction-invariant (ontological). The prior "no-record" witnesses (`H=0`, eigenstates)
are pre-record reconstructions with empty realized-outcome sets — no reality, not a no-time reality —
so they do not bound "given a reality, the time axis is forced." The unique time **axis** is thus
derived from the record ontology **unconditionally**; only the **orientation** remains (the past
hypothesis, a single bit). This corrects the "R1 not forcible" realist slip and upgrades "generically
forced" to "unconditionally forced (given the record ontology)" for the axis. Effective status
remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/time_axis_from_record_ontology_runner.py
```
