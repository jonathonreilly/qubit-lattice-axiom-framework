# Persistent-Record Process Stinespring Isometry on the Qubit-Lattice Substrate (Narrow)

**Date:** 2026-05-20
**Type:** bounded_theorem candidate (narrow theorem)
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Supply the named `missing_bridge_theorem` flagged in the
audit verdict on
`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20`
(`audited_conditional` on main):

> *"provide an independent formal derivation that the persistent-record
> process defines a state-independent linear system-record
> isometry/instrument whose record components satisfy `Σ_r K_r†K_r = I`."*

Identifies the persistent-record process on the qubit-lattice
substrate as the **Stinespring dilation** of a CPTP measurement
instrument, with state-independent linear isometry `V: H_sys → H_sys
⊗ H_record` whose Kraus-component decomposition gives the
resolution-of-identity condition that the Persistent-record-as-Kraus
note admitted by hand.

## Honest scope

This note **applies standard Stinespring dilation theory** (Stinespring
1955; Naimark; Holevo) to the framework's persistent-record process
on the qubit-lattice substrate. It does not re-prove Stinespring's
theorem from scratch.

If audit-retained, this row supplies a candidate upstream support
for the Persistent-record-as-Kraus instrument structure, addressing
the named missing-bridge from that note's `audited_conditional`
verdict. It does not retag the parent row by itself.

## Claim

On the qubit-lattice substrate
([`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md):
A1 = qubit at every site = `M_2(ℂ)`; A2 = `Z^3`), the persistent-record
process inherited from
[`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md`](PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md)
(retained_bounded) defines a **state-independent linear
system-record isometry**

```text
V: H_sys → H_sys ⊗ H_record                                              (1)
```

satisfying

```text
V† · V = 𝟙_sys                                                          (2)
```

(`V` is an isometry from the system Hilbert space to the joint
system-record Hilbert space). The decomposition

```text
V = Σ_r K_r ⊗ |r⟩                                                       (3)
```

over record basis states `|r⟩ ∈ H_record` gives Kraus operators
`K_r ∈ B(H_sys)` satisfying

```text
Σ_r K_r† · K_r = 𝟙_sys                                                   (4)
```

This is the **Stinespring dilation** of the persistent-record CPTP
map. (1)–(4) supply the state-independent linearity + isometry +
resolution-of-identity structure named as the missing bridge on the
Persistent-record-as-Kraus note.

## Setup

By A1+A2, the system algebra is the quasi-local UHF algebra
`A_sys = ⊗_{x ∈ Z^3} M_2(ℂ)` with finite-region restriction
`A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)` acting on `H_sys|_Λ = ⊗_x ℂ²`.

The framework's persistent-record process (per
`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md`) writes path-amplitudes
into a mesoscopic record state space `H_record`. The record state
space carries an orthonormal basis `{|r⟩}_{r ∈ R}` indexed by
post-barrier worldtube configurations.

The joint system-record Hilbert space is
`H_joint := H_sys ⊗ H_record`.

A **measurement instrument** is a collection of bounded operators
`{K_r}_{r ∈ R}` on `H_sys` with the resolution of identity
`Σ_r K_r† K_r = 𝟙_sys`. Equivalently (Stinespring 1955), an
instrument corresponds to an isometry `V: H_sys → H_joint`.

## Step 1 — State-independence of the record-formation map

The framework's persistent-record process (per the retained
`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE`) acts on the system via the
lattice path-integral amplitude assignment:

```text
|ψ_sys⟩ → V|ψ_sys⟩ := Σ_paths α_paths · |path⟩_sys ⊗ |record(path)⟩      (5)
```

where `α_path` is the path amplitude and `|record(path)⟩` is the
record encoding of which post-barrier worldtube the path traverses.

**Key observation:** the map `V` defined by (5) **does not depend on
the initial state** `|ψ_sys⟩`. It depends only on:
- The framework's lattice path-amplitude assignment (a property of
  the dynamics, not the state).
- The record-encoding convention (the assignment of worldtubes to
  basis states `|r⟩`).

So `V` is a fixed linear map on `H_sys`, applied identically to any
state. This addresses the **state-independence** condition.

## Step 2 — Linearity of the record-formation map

The framework's lattice path-integral is **linear in the system
state**: for `|ψ⟩ = α|ψ_1⟩ + β|ψ_2⟩`, the propagated state is
`α(V|ψ_1⟩) + β(V|ψ_2⟩)` (path amplitudes superpose linearly). This
is the standard property of quantum-mechanical path integrals,
inherited from the unitary evolution structure.

So `V` is a **linear operator** `V: H_sys → H_joint`. This addresses
the **linearity** condition.

## Step 3 — Isometry property

Total probability is preserved: for any normalized initial state
`|ψ_sys⟩`, the total probability over all record outcomes equals 1:

```text
Σ_r |⟨r|⟨ψ_r|sys ⊗ ⟨r|record V|ψ_sys⟩|² = ‖ψ_sys‖² = 1                  (6)
```

Equivalently, `⟨V ψ| V ψ⟩ = ⟨ψ|ψ⟩` for all `|ψ⟩`, which is the
**isometry condition** `V† V = 𝟙_sys`.

This is the framework's commitment that the path-integral assigns
total probability 1 to any normalized state — standard quantum
mechanics, inherited from unitarity of the underlying lattice
dynamics.

## Step 4 — Kraus decomposition gives resolution of identity

Decompose `V` over the record basis `{|r⟩}`:

```text
V = Σ_r (K_r ⊗ |r⟩)                                                     (3)
```

where `K_r: H_sys → H_sys` is defined by `K_r |ψ_sys⟩ := (𝟙_sys ⊗
⟨r|) V |ψ_sys⟩`. The `K_r` are bounded linear operators on `H_sys`.

The isometry condition (2) decomposes:

```text
V† V = (Σ_r K_r† ⊗ ⟨r|)(Σ_{r'} K_{r'} ⊗ |r'⟩)
     = Σ_{r, r'} K_r† K_{r'} · ⟨r|r'⟩
     = Σ_r K_r† K_r   (using ⟨r|r'⟩ = δ_{r r'})                          (7)
     = 𝟙_sys
```

So `Σ_r K_r† K_r = 𝟙_sys`. **This is the resolution of identity (4)**
that the Persistent-record-as-Kraus note admitted by hand.

## Step 5 — Stinespring dilation (cited)

**Stinespring's Theorem** (Stinespring 1955 *Proc. Amer. Math. Soc.*
6, 211): every CPTP map `Φ: B(H_sys) → B(H_sys)` admits a dilation

```text
Φ(X) = V† (X ⊗ 𝟙_aux) V                                                  (8)
```

for some isometry `V: H_sys → H_sys ⊗ H_aux` with `V† V = 𝟙_sys`.
Conversely, any isometry of this form gives a CPTP map via (8).

The Kraus operators of `Φ` are recovered from `V` via the
decomposition (3) over an auxiliary basis.

**Application to the framework.** The persistent-record process
defines `V` via (5); Stinespring's theorem says this corresponds to a
CPTP measurement instrument with Kraus operators `K_r` given by
(7), satisfying the resolution of identity (4).

## What this can support after audit

- **The named missing_bridge_theorem** on
  `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20`'s
  `audited_conditional` verdict: state-independent linear
  system-record isometry/instrument with `Σ_r K_r† K_r = 𝟙` resolution
  of identity. Steps 1–4 supply these properties from
  framework-side content (state-independence: Step 1;
  linearity: Step 2; isometry: Step 3; resolution of identity: Step 4)
  plus the standard Stinespring dilation theorem (Step 5) as named
  non-derivation import.
- **Companion to the Kraus-Choi narrow theorem** (in flight as
  PR #1632): Stinespring dilation is the standard sister theorem
  to Kraus' operator-sum representation (both characterize CPTP maps).
  Together they supply the upstream structure for the framework's
  record-formation lane.

## What this does not close

- **Re-derivation of Stinespring's theorem from scratch** — cited as
  standard finite-dim operator-algebra content.
- **The detailed form of the persistent-record overlap kernel
  `K(r, r')`** — that's the framework's existing
  `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md` content
  (retained_bounded), inherited as named upstream.
- **Promotion of the Persistent-record-as-Kraus row** — the auditor
  still owns the verdict; this PR supplies a candidate missing-bridge
  but does not by itself promote the parent row.

## Admitted inputs

1. **Stinespring 1955 dilation theorem** for CPTP maps on
   `B(H)` for finite-dim `H` — standard math (*Proc. Amer. Math. Soc.*
   6, 211). The framework's contribution is the application to the
   qubit-lattice substrate with `H_sys = ⊗_x ℂ²` and a specific
   record space `H_record`.
2. **Framework's lattice path-amplitude linearity** — inherited from
   the unitary evolution structure of the underlying lattice dynamics.
   Standard property of quantum-mechanical path integrals.
3. **Persistent-record process structure** — admitted from
   `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md` (retained_bounded). This
   note does not re-derive the persistent-record lane; it identifies
   the Stinespring-dilation structure of the existing lane.

## Risk classification

This is a `bounded_theorem` candidate at the narrow-theorem
granularity. Standard Stinespring dilation theorem applied to the
framework's persistent-record process. The narrow contribution is
identifying that the lattice path-amplitude record-formation
process satisfies Stinespring's isometry hypotheses (state-independence,
linearity, total-probability preservation), and applying the standard
theorem to read off the Kraus-decomposition with resolution of
identity.

Standard QI content (Nielsen–Chuang Ch.8.2; Watrous Ch.2.2); the
framework's contribution is the application to its specific
record-formation lane.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra + Z^3 substrate)
- [`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`](PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md) — landed companion (audited_conditional) whose named missing_bridge_theorem this row supplies
- [`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md`](PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md) — retained_bounded record-formation lane whose Stinespring structure this row identifies

**Upstream standard-math imports** (named non-derivation):

- Stinespring 1955 *Proc. Amer. Math. Soc.* 6, 211 — original dilation theorem
- Naimark / Holevo — alternative dilation constructions
- Nielsen–Chuang Ch.8.2 — modern textbook treatment of quantum operations
- Watrous Ch.2.2 — measurement instruments and Stinespring dilation

**Plain-text pointer references** (NOT load-bearing deps):

- `KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md` — sister narrow theorem (PR #1632 in flight) on the operator-sum representation; Stinespring dilation here is the dual perspective
- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — downstream consumer

## What this file is not

- Not a re-derivation of Stinespring's theorem (cited as standard math)
- Not a closure of the Persistent-record-as-Kraus row (auditor-owned)
- Not a closure of the persistent-record lane itself
- Not a numerical-prediction change
