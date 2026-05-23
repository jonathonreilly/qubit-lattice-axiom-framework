# Persistent Record as Kraus Operator: Bridging the Record Lane to Measurement-Update Operators

**Date:** 2026-05-20
**Type:** bounded_theorem candidate
**Status:** source-side proposal — independent audit lane owns the verdict
**Supplies (proposed):** a bounded replacement candidate for the
record-as-Kraus admission in
`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` by
formally connecting the framework's persistent-record lane to the
Kraus / CPTP operator structure used by measurement-update rules. The
Born note is a downstream repair target, not an upstream dependency.

**Audit-dispatch parent candidate:** If a future independent audit
evaluates whether this Kraus-operator bridge is a non-chain-closing
alias/decorative handle, the candidate parent is
[`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md`](PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md).
This is source-side routing context only; it does not assert an
`audit_status` or `effective_status`.

## Claim

For each persistent record `r` produced by the
`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE` mesoscopic record-formation
process, there exists a Kraus operator `K_r` on the system algebra
such that:

1. **Record-conditional update is Kraus conjugation:** the
   post-record state is `σ → σ|_r = K_r σ K_r† / Tr(K_r σ K_r†)`,
   matching the standard selective-operation form and composing with
   the companion Lüders-rule candidate if that row is independently
   retained.
2. **Resolution of identity:** `Σ_r K_r† K_r = I_sys` (the
   record-outcomes are an exhaustive measurement, summing to the
   system identity).
3. **CPTP map:** the unconditional update `σ → Σ_r K_r σ K_r†` is a
   completely positive trace-preserving (CPTP) map, matching the
   standard quantum-operations formalism.

If independently retained, this supplies the record-as-Kraus input to
the Born derivation route. It does not retag or promote the Born row
by itself.

## Setup

The framework's record-formation process (per
`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md`, retained_bounded) writes
post-barrier worldtube counts into a mesoscopic record state space
`R`. Each path through the lattice contributes amplitude to a
specific record `r ∈ R`. The overlap kernel

```text
K(r, r') = exp(-γ ||r - r'||²)                                           (1)
```

parameterizes how strongly distinct records `r, r'` remain entangled
(γ = 0: coherent superposition; γ → ∞: orthogonal records).

To use this in the Born derivation, we need each record `r` to act
on the system Hilbert space as a Kraus operator `K_r`, so the
Lüders rule of the companion note applies.

## Step 1 — Record-amplitude map gives Kraus operators

For a path `|ψ⟩` propagating through the lattice and writing into
record state `|r⟩`, the joint system+record amplitude is

```text
|Ψ_joint⟩ = Σ_r A_r |φ_r⟩ ⊗ |r⟩                                          (2)
```

where `A_r` is the path amplitude into record `r` and `|φ_r⟩` is
the system state conditional on the record. The map from initial
system state `|ψ⟩` to the record-conditional system amplitude is

```text
K_r : |ψ⟩ → A_r |φ_r⟩                                                    (3)
```

This is **linear** in `|ψ⟩` (because the path-amplitude
record-writing process is linear: superposition of system inputs
gives superposition of joint amplitudes). Therefore `K_r` extends to
a bounded operator on the system Hilbert space.

For density-matrix inputs, the action is

```text
σ → K_r σ K_r†                                                           (4)
```

(unnormalized), and the record-conditional normalized state is

```text
σ|_r = K_r σ K_r† / Tr(K_r σ K_r†)                                       (5)
```

This is the standard selective Kraus-operation form. Step 1 identifies
the Kraus operator; comparison with the companion Lüders candidate is a
downstream composition, not an upstream premise of this row.

## Step 2 — Resolution of identity from path-amplitude normalization

The persistent-record lane is normalized: the total probability over
all records sums to 1 for any normalized input `|ψ⟩`:

```text
Σ_r |A_r ⟨φ_r | ψ⟩|² = ||ψ||² = 1                                       (6)
```

equivalently, in operator form,

```text
Σ_r ⟨ψ| K_r† K_r |ψ⟩ = 1                                                 (7)
```

for every normalized `|ψ⟩`. This holds iff `Σ_r K_r† K_r = I_sys`,
which is the **Kraus resolution of identity** (the requirement that
the set `{K_r}` form a valid quantum measurement).

The path-amplitude normalization on the persistent-record lane gives
this directly from (6). Step 2 verifies the resolution of identity.

## Step 3 — CPTP property of the unconditional update

The unconditional state update (averaging over record outcomes) is

```text
σ → E(σ) := Σ_r K_r σ K_r†                                              (8)
```

This is the standard Kraus form of a CPTP map. The complete
positivity follows from the Kraus structure (Kraus 1971;
Choi 1975); the trace-preserving property follows from the
resolution of identity:

```text
Tr(E(σ)) = Σ_r Tr(K_r σ K_r†) = Σ_r Tr(K_r† K_r σ) = Tr(σ · I) = Tr(σ)   (9)
```

Step 3 verifies CPTP.

## Step 4 — Bridge to the overlap kernel

The overlap kernel `K(r, r')` of equation (1) is a parameter of the
*record state space*, controlling how distinct records remain
entangled in the joint system+record amplitude. The Kraus operators
`K_r` themselves are independent of γ — they describe the
record-conditional system action, not the inter-record entanglement.

The γ parameter enters the Born derivation only through the
**effective POVM** on the system: when γ = ∞ (orthogonal records),
each `K_r` is a sharp projection; when γ < ∞, the effective POVM
elements `E_r = K_r† K_r` are POVM effects that are not projections
(they describe unsharp records).

This matches the existing Born-derivation framing exactly: Gleason's
projective theorem handles the γ = ∞ limit; the Busch POVM extension
handles the γ < ∞ case. Both are admitted in the Born derivation.

Step 4 verifies the bridge is consistent with the Born route's
admitted inputs.

## What this can close after audit

- **The record-as-Kraus admission** in
  `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` —
  formally connects `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE` to Kraus
  operators. Parent-row dependency repair is a downstream step after
  this row is audited.

## What this does not close

- **Asymptotic closure of the persistent-record lane.** The
  `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md` is itself a bounded
  positive pilot, not asymptotic closure (per its own status line).
  This note inherits that bounded scope: the Kraus identification is
  valid on the bounded pilot surface, not on a fully closed
  record-formation theory.
- **The specific form of `K_r` for any particular system observable.**
  Step 1 identifies that `K_r` exists; specific forms depend on which
  observable is being measured. This is a structural claim about the
  family of Kraus operators, not a particular calculation.
- **The remaining admitted inputs of the Born derivation**, including
  Gleason 1957, Busch 2003 POVM extension, Lüders/record-update
  structure if not separately retained, and no-extra-structure
  pre-record identification. Each is handled by its own row/import.

## Admitted inputs

1. **`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md`** (retained_bounded)
   — supplies the persistent-record-formation process. This note
   identifies the Kraus structure of that process; it does not
   re-derive the persistent-record lane.
2. **Linearity of the path-amplitude record-writing process.**
   Required for `K_r` to extend to a bounded linear operator on the
   system Hilbert space. Standard property of the lattice
   path-integral; admitted from the framework's underlying linear
   amplitude structure.
3. **Standard Kraus / Choi structure for CPTP maps.** Standard
   operator-algebraic background (Kraus 1971, Choi 1975).

## Risk classification

This is a `bounded_theorem` candidate. The steps are textbook
operator-algebraic content (Kraus / Choi formalism is mainstream),
applied to the framework's existing persistent-record lane. The
narrow contribution is the explicit identification of `K_r` from
the record-amplitude map.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links so the citation graph records them as deps):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra and `Z^3` substrate)
- [`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md`](PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md) — supplies the persistent-record-formation process to which Kraus operators are attached

**Upstream standard-math imports** (named non-derivation; not framework rows):

- Kraus 1971 *Ann. Phys.* — operator-sum representation of CPTP maps
- Choi 1975 *Lin. Alg. Appl.* — Choi-Jamiołkowski isomorphism / CP characterization
- Nielsen-Chuang Ch.8 (Quantum Operations) — modern textbook treatment

**Plain-text pointer references** (NOT load-bearing deps; deliberately not markdown links):

- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` —
  downstream Born note that this Kraus identification may repair after
  audit / dependency-chain update
- `LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md` —
  companion selective-update candidate; not load-bearing for this
  Kraus-identification row while that row remains in flight
- `PERSISTENT_RECORD_MATCHED_COMPARE_NOTE.md`, `PERSISTENT_RECORD_REFINEMENT_NOTE.md`, `PERSISTENT_RECORD_SIDEBIT_NOTE.md` — adjacent lane notes; not load-bearing for this Kraus identification
- `TELEPORTATION_MEASUREMENT_RECORD_NOTE.md`, `TELEPORTATION_NATIVE_RECORD_APPARATUS_NOTE.md` — related apparatus models; not load-bearing here

## What this file is not

- Not a closure of the persistent-record lane itself (still bounded pilot per upstream).
- Not a derivation of Kraus / Choi structure (admitted as standard math).
- Not a numerical-prediction change.
- Not a unilateral retagging. The bounded-theorem candidacy depends on independent audit acceptance of the linearity admission and the Kraus structure import.
