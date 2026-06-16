# Single-Clock KMS/APBC Axis-Supplier No-Go

**Date:** 2026-06-16
**Claim type:** no_go
**Type:** bounded support / negative route pruning
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit audit-ledger, queue,
publication-status, axiom, or Tier-A registry surfaces.
**Actual current-surface status:** exact negative boundary for the
KMS/APBC-as-axis-supplier route; conditional exact support for axis selection
if a per-axis boundary-condition asymmetry is independently supplied.
**Primary runner:**
[`scripts/single_clock_kms_apbc_axis_supplier_no_go_2026_06_16.py`](../scripts/single_clock_kms_apbc_axis_supplier_no_go_2026_06_16.py)
with cached output
[`logs/runner-cache/single_clock_kms_apbc_axis_supplier_no_go_2026_06_16.txt`](../logs/runner-cache/single_clock_kms_apbc_axis_supplier_no_go_2026_06_16.txt).

## Target

This note targets the remaining single-clock B-AXIS blocker in
`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`
(named here as context only, not as a proof dependency):
the framework still needs a supplier for the physical time step, the
axis/transfer construction, and the exclusion of independent commuting
clock factors. The earlier axis-selection no-go identified a possible pin:
a per-axis `Z_2` boundary-condition asymmetry such as APBC on the temporal
circle and PBC on spatial circles.

The tempting escape route is:

```text
finite-temperature KMS + fermionic APBC already select the temporal axis
```

This note proves the route is false as a supplier. KMS/APBC is formulated
after a time flow, trace circle, or transfer direction has already been
supplied. Fermionic APBC then follows on that supplied circle. Under the
time-space exchange certificate `W`, APBC on the supplied `tau` circle
transports exactly to APBC on the supplied `x1` circle. Therefore KMS/APBC
does not pick an axis before B-AXIS; it only decorates whichever axis was
already chosen.

## Inputs

- The B-AXIS boundary named by
  `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`,
  used as the target residual only. The finite exchange map `W` is defined and
  checked directly in the runner below.
- The retained no-go checklist
  [`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md),
  especially N2/N4/N5.
- The finite-temperature KMS source note
  `AXIOM_FIRST_KMS_CONDITION_THEOREM_NOTE_2026-05-01.md`, used here only as
  route text/context: it starts from an RP-reconstructed transfer matrix, a
  periodic Euclidean time block, and APBC fermions. It is not a proof
  dependency of this no-go.
- The finite Grassmann/Berezin support note
  [`SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md),
  used only for the fact that Grassmann signs are algebraic once the
  generators and circle are supplied.
- The existing route-pruning note
  `SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`,
  whose BC-asymmetry pin is sharpened here as context rather than as a proof
  dependency.

No observed values, fitted selectors, new axioms, new primitives, or
literature numerical inputs are used.

## Statement

On the finite staggered kinetic block with periodic boundary conditions,
the conjugated exchange

```text
W = P_{tau<->x1} diag((-1)^(x_tau x_1))
```

intertwines the time and `x1` axes. If APBC is supplied on the `tau`
circle, then `W` transports that operator exactly to the operator with APBC
on the `x1` circle. Thus:

1. APBC on a supplied circle is axis-covariant.
2. APBC on `tau` while `x1` remains periodic breaks the exchange, but the
   breaking is exactly the supplied per-axis `Z_2` boundary datum.
3. KMS and finite fermionic trace algebra do not derive that datum, because
   their hypotheses already name the trace/evolution circle.

Therefore KMS/APBC cannot discharge B-AXIS. It can only say: given a supplied
time circle and fermionic trace setup, APBC is the correct fermionic
boundary convention on that supplied circle.

## Proof Sketch

The runner constructs the antisymmetric staggered hop matrix on the even
periodic block `(L_tau, L_1, L_2, L_3) = (4,4,2,2)` using the usual
Kawamoto-Smit phases. It then computes:

- `W M_PBC W^T = M_PBC` exactly.
- `W M_APBC(tau) W^T = M_APBC(x1)` exactly.
- `W M_APBC(tau) W^T != M_APBC(tau)` when `x1` remains periodic.
- `W M_APBC(tau,x1) W^T = M_APBC(tau,x1)` exactly.

So the axis-selecting fact is not "fermions are antiperiodic" but "this
particular axis carries the antiperiodic wrap while the exchanged axis does
not." That is a boundary-condition asymmetry datum.

The runner also checks a finite cyclic-shift toy model: the antiperiodic
shift has `C^L = -I` on whichever labeled circle is supplied, while the
periodic shift has `C^L = I`. Relabeling the circle preserves the theorem.
Again, the algebra is about a supplied circle; it contains no lattice-axis
selector.

## No-Go Discipline

- **N1: alternative routes.** Five scoped routes were checked. (1) KMS trace
  might name the temporal axis; it already presupposes a transfer/time circle.
  (2) Fermionic APBC might name the temporal axis; the runner shows APBC
  transports from `tau` to `x1` under the exchange map. (3) Grassmann/Berezin
  sign algebra might name the temporal axis; it is algebraic after the
  generator and circle are supplied. (4) The zero-kernel/rank effect of APBC
  might name the temporal axis; the same effect belongs to whichever circle is
  supplied as antiperiodic. (5) Per-axis BC asymmetry can select an axis only if
  independently derived or admitted; KMS/APBC does not supply the asymmetry.
- **N2: wall independence.** KMS/APBC can supply a convention after a time
  circle is named; B-AXIS asks for the naming/supply itself. A supplied
  per-axis BC-asymmetry would be a separate bridge, not a consequence of KMS.
- **N3: hidden-wall scan.** "Thermal", "trace", "Euclidean time", and
  "fermionic APBC" all presuppose a transfer/time circle in the cited KMS
  note. This note does not consume that presupposition as an axis derivation.
- **N4: residual matching.** The residual remains B-AXIS N2/N4/N5, not the
  finite Grassmann sign and not the correctness of APBC on an already supplied
  fermionic trace circle.
- **N5: rhetoric audit.** This is not a proof that no future BC supplier can
  exist. It prunes only KMS/APBC as a supplier before the axis is supplied.
- **N6: partial closure.** A derived BC-asymmetry theorem, a non-circular
  registration-direction bridge, or a theorem excluding independent commuting
  clock factors would still close the relevant B-AXIS part.
- **N7: steelman.** If a later row derives why one lattice circle, and no
  exchanged spatial circle, carries the APBC trace wrap, that row would supply
  a real B-AXIS component. This note says current KMS/APBC text does not.
- **N8: cross-cycle echo.** This matches the Record clock/rate interface:
  post-record/KMS rate language can use a supplied clock, but does not derive
  the clock axis.

## Boundaries

- Does not derive B-AXIS.
- Does not derive APBC from the three minimal axioms.
- Does not derive the physical time step `2 a_tau`.
- Does not exclude independent commuting transfer factors.
- Does not promote, demote, retag, or apply any audit verdict.
- Does not alter the axiom count.

## Claim-Status Certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
target_claim_id: axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03
target_blocker_text: "B-AXIS.1-.3 are not discharged by any provided authority"
artifact_role: no_go
conditional_surface_status: "exact support for axis label given a supplied per-axis BC-asymmetry datum"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The artifact prunes a route and sharpens the required supplier; it does not close B-AXIS."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Reproduction

```bash
python3 scripts/single_clock_kms_apbc_axis_supplier_no_go_2026_06_16.py
```

Expected summary:

```text
SUMMARY: PASS=25 FAIL=0
```
