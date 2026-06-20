# Record Formation to Kraus Isometry Bridge

**Date:** 2026-06-06
**Type:** bounded bridge theorem
**Claim type:** bounded_theorem
**Status:** exact-support branch-local, conditional on the finite pointer-record
model premises listed below — in particular conditional on the already-supplied
projective record-write premise (the ideal pointer-label write isometry is a
supplied premise, not derived here from the finite controlled-copy/fresh-fragment
record-formation dynamics); audit_required_before_effective_retained=true;
bare_retained_allowed=false.

Status authority: independent audit lane only. This source note does not set or
predict an audit outcome.
**Primary runner:**
[`scripts/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py`](../scripts/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.txt`](../logs/runner-cache/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.txt)

## Claim

The earlier finite Kraus note proves the following algebra:

```text
normalized record-writing isometry W
  => extracted blocks K_r form a Kraus/CPTP instrument.
```

It deliberately leaves open the harder bridge:

```text
persistent record dynamics
  => normalized record-writing isometry W.
```

This note supplies a narrow bridge for the explicit finite pointer model used
in
[`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md).

Condition on:

- a finite system Hilbert space `H_sys`;
- a pointer observable with finite spectral projectors `{P_r}` satisfying
  `P_r P_s = delta_rs P_r`, `P_r^dagger = P_r`, and `sum_r P_r = I`;
- the finite pointer-non-demolition record-formation bridge, so the pointer
  sectors are stable record sectors in the model;
- a blank finite record register `H_record` with orthonormal labels `{|r>}`;
- **the projective record-write premise** (supplied, not derived here): an ideal
  record-write step that copies the stable pointer sector label to the record
  register without rotating the pointer sector. This premise hands us the
  projective write directly; deriving it from the finite controlled-copy/
  fresh-fragment record-formation dynamics is a separate open bridge, not
  supplied here.

Define

```text
W |psi> = sum_r (P_r |psi>) tensor |r>.
```

Then:

1. `W` is a normalized isometry: `W^dagger W = I`.
2. The extracted blocks are exactly projective Kraus operators:
   `K_r = <r| W = P_r`.
3. The unconditional post-record update is the pointer-dephasing CPTP map
   `rho -> sum_r P_r rho P_r`.
4. Each nonzero selective branch
   `rho_r = P_r rho P_r / Tr(P_r rho)` is normalized, positive, and stable
   under an immediate repeat read of the same pointer record.
5. The realized record labels are orthogonal one-hot atoms, so the exact
   post-record word/count layer can consume them as realized symbols.

This is an exact finite-model bridge **from the supplied projective record-write
premise** to the Kraus-instrument algebra: given that premise, the isometry `W`
and its projective Kraus blocks follow exactly. The bridge does NOT derive the
projective write premise (the isometry `W`) from the finite controlled-copy/
fresh-fragment record-formation dynamics — that derivation is an open bridge, not
supplied here — and it does not solve the general physical production problem.

## Proof

By the projector resolution and orthonormal record labels,

```text
W^dagger W
  = sum_{r,s} P_r^dagger P_s <r|s>
  = sum_r P_r
  = I.
```

So `W` is a normalized isometry. Contracting against record label `<r|` gives

```text
K_r = <r| W = P_r.
```

The Kraus resolution is therefore

```text
sum_r K_r^dagger K_r = sum_r P_r = I.
```

Thus the unconditional update

```text
E(rho) = sum_r P_r rho P_r
```

is completely positive and trace preserving by the same finite Kraus algebra
proved in
[`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`](PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md).
For any branch with `p_r = Tr(P_r rho) > 0`, positivity of
`P_r rho P_r` and division by `p_r` give a normalized positive selective
state. Idempotence `P_r P_r = P_r` gives immediate repeat-read stability,
and orthogonality `P_s P_r = 0` for `s != r` gives cross-read exclusion.

## Relation to the formation dynamics note

The pointer-non-demolition note establishes, inside an explicit finite
`S + E_1..E_n` model and under the quantum-Darwinism record reading, that
additive + redundant + persistent + objective record formation by local
evolution is equivalent to a conserved pointer:

```text
[H_int, Pi_S] = 0.
```

That result supplies stable pointer sectors for the bounded model. This note
then takes the projective record-write premise — the ideal pointer-label write
whose blocks are those sectors' projectors — as supplied, and proves the exact
Kraus-instrument algebra that follows from it. The note does not derive that
write premise (the isometry `W`) from the finite controlled-copy/fresh-fragment
record-formation dynamics; that derivation is an open bridge.

The composition is:

```text
finite quantum-Darwinism pointer model
  + pointer-non-demolition record formation
  + blank orthonormal record register
  + ideal pointer-label write                  [SUPPLIED PREMISE]
    --[open bridge: dynamics => W not supplied here]-->
    => normalized W                            [given the premise]
    => projective Kraus instrument             [exact, given the premise]
    => realized record atom for post-record word/count dynamics.
```

The first three-plus-fourth inputs are bridge/model premises; in particular the
ideal pointer-label write is the supplied projective write premise. The step from
the finite controlled-copy/fresh-fragment dynamics to that premise (`dynamics =>
W`) is an open bridge, not supplied here. The algebra after the premises — `W` is
a normalized isometry, `K_r = P_r`, and the projective Kraus instrument — is
exact.

## What this buys

- It narrows the open "record dynamics to Kraus instrument" gap for the
  projective finite pointer model: given the supplied projective record-write
  premise, the Kraus-instrument algebra is exact. The residual open step is the
  bridge from the finite controlled-copy/fresh-fragment dynamics to that write
  premise (`dynamics => W`), which this note does not supply.
- It gives a concrete interface between bounded formation dynamics and exact
  post-record information dynamics.
- It explains the pre-record/post-record distinction without making it an
  extra axiom:
  - before the record-write, the carrier state can contain coherence and
    predictive branch weights;
  - the record-write extracts an orthogonal realized label;
  - after the record-write, the word/count layer operates on realized symbols,
    not on unresolved amplitudes.
- It supplies a reusable audit target for projective measurement/instrument
  lanes: check whether the proposed physical bridge really supplies stable
  pointer projectors, orthogonal record labels, and an ideal or derived
  record-write isometry.

## What this does not claim

- It does not derive the pointer observable from the minimal axioms.
- It does not derive the physical Hamiltonian, action, coupling, clock, rate,
  or beta value.
- It does not derive arbitrary persistent-record dynamics into a normalized
  isometry.
- It does not derive the ideal pointer-label record-write isometry from the
  finite controlled-copy/fresh-fragment record-formation dynamics. That write is
  the supplied projective record-write premise; deriving it from the dynamics is
  an open bridge, not supplied here.
- It does not derive a Born rule or probability law from post-record counts.
  Branch weights are read from the pre-record density matrix through the
  supplied projective instrument.
- It does not select a generation or Koide dial location. The dial remains a
  separate stable-location question, not a forced selection.
- It does not apply any audit verdict.

## Repair history

### 2026-06-19 — missing_bridge_theorem repair (narrowing alternative)

Rescoped the bridge to be conditional on the already-supplied projective
record-write premise. The note now states that, GIVEN the projective
record-write premise (the ideal pointer-label write isometry `W`), the Kraus
isometry bridge holds exactly (`W^dagger W = I`, `K_r = P_r`, projective Kraus
instrument). The derivation of that premise from the finite controlled-copy/
fresh-fragment record-formation dynamics (`dynamics => W`) is marked an open
bridge, not supplied here. No claim that the isometry is derived from the
dynamics is made. No derived value changed.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: bounded-support for the finite
  pointer-non-demolition record model
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a finite-model bridge, not an audit-ratified framework-wide record-production theorem."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner certificate

The runner verifies:

- source-anchor boundaries in the formation, finite-isometry, instrument, and
  dynamics-reconciliation notes;
- exact projector primitives in the qubit pointer model;
- construction of `W` as the projective block-column isometry;
- extraction `K_r = P_r`;
- Kraus resolution, trace preservation, Choi positivity, selective branch
  normalization and positivity;
- pointer-dephasing of pre-record coherence into post-record realized labels;
- immediate repeat-read stability and cross-branch exclusion;
- explicit firewall flags: no general dynamics-to-`W` derivation, no physical
  Hamiltonian selection, no probability-law derivation, and no dial selection.

Run:

```text
python3 scripts/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py
```
