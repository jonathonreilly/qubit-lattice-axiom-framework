# Redundancy / Local Observability Is Not Forced by Pointer-Non-Demolition + Locality — No-Go Note

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** named-obstruction no-go
**Claim type:** no_go
**Status:** no-go proposal. Confirms and **quantifies** the standing open gate in
[`DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE_NOTE_2026-06-05.md`](DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE_NOTE_2026-06-05.md):
local observability of a determined outcome is **not** derivable from
record durability + lattice locality + a leading-range coupling restriction. Adds
no axiom, no fitted/imported value. Audit verdict and downstream effective status
are set only by the independent audit lane.
**Authority role:** no-go source proposal.
**Primary runner:**
[`scripts/audit_companion_redundancy_not_forced_pnd_locality_2026_06_07.py`](../scripts/audit_companion_redundancy_not_forced_pnd_locality_2026_06_07.py)
(SCORECARD PASS=7 FAIL=0, exact numpy).

## Question

[`DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE_NOTE_2026-06-05.md`](DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE_NOTE_2026-06-05.md)
names **local observability of a determined outcome** (the realized per-site
pointer value is independently recoverable by each spatially-disjoint local
observer — a redundant broadcast) as an open premise not supplied by the
`{Lattice, Quantum, Record}` axioms. This note asks the sharper, dynamical
question: is local observability **forced** by the record-formation dynamics the
framework already has — namely

1. **pointer-non-demolition** `[H_int, Z_S] = 0`, sourced from the Record axiom's
   **durability** clause ("the recorded outcome does not change") via the
   Heisenberg necessity argument of
   [`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md);
2. **lattice locality** (`Z^3` finite-range coupling); and
3. a **leading-range** restriction (the same minimality
   [`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`](DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md)
   uses for "smallest loop = plaquette")?

If yes, local observability would be a corollary at no new admission. The answer
is **no**.

## Answer

**NO.** Redundant broadcast (local observability) is **not** forced by
`{durability/pointer-non-demolition + lattice locality + leading-range}`. It
occurs only on a **measure-zero, doubly fine-tuned** set, while the *generic*
pointer-non-demolition coupling is non-redundant (`R_delta<N`; in the finite
witnesses it is 0 or 1). The premise that **would** force it — that the coupling is a
pure sum of **independent single-site** monitorings (conditional independence /
multiplicity) — is exactly local observability **restated**, not derived. So the
open gate stands; this note quantifies how sharply.

## What the runner verifies (PASS=7, FAIL=0)

The recoverable pointer information of a fragment `F` is the **Holevo** content of
the pointer ensemble `chi_F` (accessible classical information about `Z_S`); a
fragment carries a quantum-Darwinism **record** iff `chi_F >= (1 - delta) H_S`
with the standard information deficit `delta = 0.1` and pointer entropy `H_S`.
Redundancy `R_delta` is the number of disjoint single-site fragments that each
carry the record. All Holevo / entropy / redundancy facts are reproven in the
runner, not imported.

1. **The correct measure (this refinement survives).** For the determined,
   durable, locally-blind anti-witness `Z_S Z_1 Z_2 = +1`, fragment `{1}` has
   **full** quantum mutual information `I(S:1) = 1` bit yet **zero** Holevo pointer
   information `chi = 0`. Quantum mutual information is **not** the
   quantum-Darwinism record measure; the Holevo deficit is.
2. **The broadcast is fine-tuned in time.** The pure single-site-sum monitoring
   `Sum_k Z_S (x) X_k` gives `R_delta = N` only at the CNOT point `g t = pi/4`;
   at `g t = pi/6` the same coupling gives `chi = 0.811 < 0.9 H_S` (trace distance
   `0.866`) per fragment, so `R_delta = 0`.
3. **The broadcast is measure-zero in the coupling.** Over the generic
   pointer-non-demolition family `H = c_0 Z_S X_1 + c_1 Z_S X_2 + c_2 Z_S X_1 X_2`
   (random Gaussian `c`), `R_delta = N` (both single fragments reach the deficit)
   occurs in `~1-2 / 300` samples at the deficit `delta = 0.1` — i.e. a generic
   pointer-non-demolition coupling is **not** a redundant
   broadcast.
4. **The leading-range term being present does not rescue it.**
   `H = 0.5 (Z_S X_1 + Z_S X_2) + Z_S X_1 X_2` has the range-2 monitoring present
   (coefficient `0.5`) yet gives `R_delta = 0`: a higher-range admixture destroys
   redundancy.
5. **Pointer-non-demolition alone does not force redundancy.** `Z_S X_1 X_2` is
   pointer-non-demolition (`[H, Z_S] = 0`) yet gives `R_delta = 0` for
   disjoint single-site fragments at the tested time.

## Reconciliation with the landed notes

- **Confirms and quantifies the open gate.** This is the dynamical companion of
  [`DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE_NOTE_2026-06-05.md`](DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE_NOTE_2026-06-05.md):
  that note shows the **axioms** do not supply local observability; this note
  shows the **record-formation dynamics** do not force it either, and that the
  redundant set is measure-zero in the pointer-non-demolition coupling space.
- **Sharpens (corrects) the record-formation note.**
  [`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  item 1 states `[H_int, Pi_S] = 0 => R_delta = n`. That holds only for the
  **single-site-sum** coupling demonstrated there; for a general
  pointer-non-demolition coupling it is false, witnessed by `Z_S X_1 X_2`
  (pointer-non-demolition, `R_delta = 0` for disjoint single-site fragments).
  The honest statement is
  `pointer-non-demolition + conditional-independence (single-site multiplicity)
  => R_delta = n`, and conditional independence is local observability restated.

## What is and is not claimed

- **Is:** local observability / redundant broadcast is an **irreducible
  admission** — not derivable from `{durability/pointer-non-demolition + lattice
  locality + leading-range}`; the redundant region is measure-zero and the
  premise that selects it is local observability itself.
- **Is not:** this does **not** claim local observability is false, nor that no
  future principle could supply it; nor that pointer-non-demolition is circular
  (it is sourced cleanly from the Record axiom's durability via the Heisenberg
  necessity leg, which is well-defined on a bare single qubit, redundancy-free).
- It introduces **no** new axiom and changes **no** numerical prediction.

## No-Go Discipline Gate

**Status:** PASS for the scoped no-go only. The claim is not "local
observability is impossible" and not "no future principle can derive redundant
broadcast." It is the narrower statement that durability/pointer-non-demolition,
lattice locality, and leading-range structure do not force redundant local
observability.

### N1 — Alternative route enumeration

| route | what it would attempt | result | marker |
|---|---|---|---|
| Mutual-information route | Use full `I(S:F)` as the record criterion | Fails: the anti-witness has `I(S:1)=1` but Holevo pointer information `chi=0` | ATTEMPTED |
| Pure single-site monitoring | Derive broadcast from `sum_k Z_S X_k` | Exists only at the CNOT time; off-time it gives `R_delta=0` | ATTEMPTED |
| Generic PND family | Let arbitrary PND couplings force broadcast | Fails: random `c0 Z_S X1 + c1 Z_S X2 + c2 Z_S X1X2` is overwhelmingly non-redundant | ATTEMPTED |
| Leading-range present | Add leading single-site terms and hope locality rescues redundancy | Fails: the explicit mixed coupling has range-2 monitoring present but `R_delta=0` | ATTEMPTED |
| PND-alone witness | Use joint PND monitoring as enough structure | Fails: `Z_S X1X2` commutes with `Z_S` but gives no disjoint single-site broadcast | ATTEMPTED |
| Conditional independence | Require a pure independent single-site monitoring sum | Succeeds, but this is the missing local-observability/multiplicity premise restated | NOT DERIVED |

### N2 — Wall-independence audit

The failures are independent: the Holevo-vs-mutual-information correction is a
record-measure issue; the CNOT-time failure is time fine-tuning; the generic-PND
failure is coupling-form dependence; and the mixed-coupling witness shows that
leading-range presence is not enough. Closing one does not close the others.

### N3 — Hidden-wall scan

The note does not use "generic," "record," or "local" as hidden authority.
`generic` is restricted to the sampled finite PND family; `record` is measured
by the explicit Holevo deficit; and `locality` is only the finite-range coupling
constraint, not redundant broadcast.

### N4 — Residual matching

The residual matches the cited open gate exactly: local observability of a
determined outcome by spatially disjoint local observers. The note does not
substitute a different residual such as mere system-fragment mutual information.

### N5 — Rhetoric audit

The no-go is scoped to the tested premise set
`{durability/PND + lattice locality + leading-range}`. It does not say
redundancy is false, impossible, or underivable from a future independent
principle.

### N6 — Partial-closure path scan

The positive path remains explicit: an independent single-site monitoring /
conditional-independence principle would force redundancy. This note records
that such a principle is not supplied by the current premise set; it does not
promote it to an axiom or silently use it.

### N7 — Steelman

The strongest counter-argument is that physical environments may dynamically
select independent monitoring channels by stability, coarse graining, or
predictability-sieve pressure. That could be a real future route. It is not in
the present premises, and the runner shows the finite PND family alone does not
force it.

### N8 — Cross-cycle echo

This agrees with the standing Darwinism local-observability open gate and
sharpens the pointer-non-demolition formation note. No prior retained row is
used to claim redundant broadcast without the missing local-observability
premise.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) supplies the
  Record axiom durability clause used to source pointer-non-demolition. The axiom
  baseline chain-satisfies as an approved premise; it is not a source of bounded
  status.
- [`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  supplies the durability-to-pointer-non-demolition necessity argument; this note
  sharpens its item-1 redundancy claim and does not enlarge it.
- [`DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE_NOTE_2026-06-05.md`](DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE_NOTE_2026-06-05.md)
  is the open gate this note confirms and quantifies.
- [`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`](DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  supplies the leading-range minimality whose insufficiency (for redundancy) is
  the subject here.

## Forbidden-imports check

No PDG values, literature numerical comparators, or fitted selectors are used as
derivation inputs. Standard quantum Darwinism (Zurek; Brandão–Piani–Horodecki
generic emergence of objectivity) is named as the comparator physics content —
the Holevo information deficit and redundancy `R_delta` are reproven in the runner
from primitives (partial trace, von Neumann / Holevo information), never imported
as a result.
