# Persistent Record as Kraus Operator: Bridging the Record Lane to Measurement-Update Operators

**Date:** 2026-05-20
**Type:** bounded_theorem
**Status:** source-side proposal — independent audit lane owns the verdict
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/persistent_record_kraus_instrument_certificate.py`](../scripts/persistent_record_kraus_instrument_certificate.py)
**Runner cache:** [`logs/runner-cache/persistent_record_kraus_instrument_certificate.txt`](../logs/runner-cache/persistent_record_kraus_instrument_certificate.txt)
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

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The Kraus/CPTP algebra closes once a normalized linear isometry W is assumed, and the runner verifies that algebra on a finite sampled isometry. The restricted packet does not derive W from the retained persistent-record overlap-kernel pilo"*

with repair: *"missing_bridge_theorem: derive or cite a retained normalized linear record-writing isometry theorem for the persistent-record overlap-kernel lane; then re-audit the finite Kraus/CPTP algebra as a bounded bridge."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The finite-instrument algebraic certificate — that if a normalized linear isometry `W : H_sys → H_sys ⊗ H_record` is given, then extracting record blocks `K_r` yields (a) resolution of identity `Σ_r K_r†K_r = I`, (b) a CPTP unconditional update, and (c) normalized selective post-record states — all verified by the runner on a concrete `C^4 → C^4 ⊗ C^3` example.
- **NON-load-bearing (split off / admitted):** The derivation of a normalized linear record-writing isometry W from the retained `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE` overlap-kernel pilot lane; the packet assumes W as an external input and does not construct it from the overlap-kernel dynamics, so the Kraus bridge is conditional on a retained isometry theorem that is not yet supplied.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## Claim

On the bounded finite record-pilot surface, if the record-writing stage is
represented by a normalized linear isometry

```text
W : H_sys -> H_sys \otimes H_record,
W = sum_r K_r \otimes |r>
```

then each record outcome `r` defines a Kraus operator `K_r` on the system
algebra such that:

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

If independent audit accepts this row, it supplies the finite
normalized-instrument bridge needed by the record-as-Kraus input to the Born
derivation route. It does not retag or promote the Born row by itself, and it
does not claim asymptotic closure of record formation.

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

To use this in the Born derivation, the bounded record-writing stage must be a
normalized linear map from system amplitudes into system-plus-record
amplitudes. The 2026-05-26 certificate makes that bridge explicit at the finite
instrument level.

## 2026-05-26 finite-instrument certificate

The primary runner constructs a finite normalized record-writing isometry
`W : C^4 -> C^4 \otimes C^3`, extracts the record blocks `K_r`, and verifies:

- `W^\dagger W = I`;
- `sum_r K_r^\dagger K_r = I`;
- the Choi matrix of `rho -> sum_r K_r rho K_r^\dagger` is positive;
- for sampled arbitrary density matrices, the unconditional update is
  trace-preserving and positive;
- for each nonzero record probability, the selective state
  `K_r rho K_r^\dagger / Tr(K_r rho K_r^\dagger)` is normalized and positive.

This is the load-bearing finite algebra certificate for the note. The
mesoscopic overlap-kernel dynamics remains the upstream bounded pilot.

## Step 1 — Record-amplitude map gives Kraus operators

For a finite normalized record-writing map, a path `|ψ⟩` propagating through
the lattice and writing into record state `|r⟩` has joint system+record
amplitude

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

The finite normalized record-writing condition is that the total probability
over all records sums to 1 for any normalized input `|ψ⟩`:

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

The certificate checks this directly as `W^\dagger W = I`, equivalently
`Σ_r K_r† K_r = I`.

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
**effective POVM** on the system. The orthogonal-record limit
(`γ = ∞`) is compatible with the projective special case when the
record instrument is sharp. At finite overlap (`γ < ∞`), the effective
POVM elements `E_r = K_r† K_r` need not be projections and can describe
unsharp records.

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
2. **Finite normalized linear record-writing map.** Required for `K_r` to
   extend to a bounded linear operator on the system Hilbert space. This branch
   certifies the finite instrument algebra once that map is present; it does
   not separately prove asymptotic record formation.
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

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies the one-qubit operator algebra and `Z^3` spatial substrate
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
