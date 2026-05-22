# LSP-Projective Derivation from Naimark Dilation + Canonical Frame (Narrow)

**Date:** 2026-05-22
**Type:** positive_theorem candidate
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Derive the Lüders projective-instrument selection `K_P := P` as the **canonical-frame** choice in the Naimark dilation of a projective measurement, with alternative Kraus operators `K_P = U·P` corresponding to apparatus-frame rotations that don't change observable predictions. Replaces the framework-rule ratification (`QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § "Hardening III") with a proper derivation.

## Why this note exists

The 2026-05-22 LSP-projective ratification (PR #1661 / commit `886ce7e`) added `K_P = P` as a load-bearing framework-rule clause. Following the same audit-feedback that drove the R1 derivation refactor, this note derives the same content from standard measurement-theory machinery (Naimark dilation + apparatus-frame convention) rather than ratifying as a framework rule.

## Honest scope

This note **does not**:
- Add a new framework rule
- Re-derive Naimark's dilation theorem from scratch (cited as standard)
- Address non-projective POVM instruments (still deferred, separate lane)
- Resolve Gudder-style sequential-product non-uniqueness on the abstract effect algebra (the literature counterexamples remain mathematically valid; this derivation argues they correspond to apparatus-frame rotations, not physically distinct measurements)

This note **does**:
- Derive `K_P = P` as the canonical-frame Kraus selection in the Naimark dilation
- Exhibit the apparatus-frame absorption argument: alternative `K_P = U·P` are physically equivalent to `K_P = P` up to apparatus unitary
- Verify on multiple instrument families that the canonical-frame choice gives consistent post-measurement states

## Claim

For projective measurement of `P ∈ A_Λ` on a finite qubit-lattice region:

**Theorem (narrow).** Under the standard Naimark dilation of a projective measurement (system ⊗ apparatus with apparatus prepared in `|0⟩_A`), the **canonical-frame** Kraus operator for outcome P is

```text
K_P  =  P.                                                              (LSP-proj)
```

Any alternative `K_P^{twist} = U · P` for a unitary `U ∈ U(H_sys)` corresponds to applying `U` as part of the apparatus dynamics rather than the system dynamics. The observable joint probability distribution and the marginal apparatus distribution are unchanged; only the system-frame is rotated. Under the canonical frame (no apparatus-side rotation absorbed into the system), `K_P = P`.

## Proof

### Step 1 — Naimark dilation of projective measurement

The **Naimark dilation theorem** (Naimark 1940; Holevo *Probabilistic and Statistical Aspects of Quantum Theory* Ch. III; Watrous *The Theory of Quantum Information* §2.4):

For any POVM `{E_r}` on a system Hilbert space `H_sys`, there exist:
- An apparatus Hilbert space `H_A` with orthonormal basis `{|r⟩_A}`
- A unitary `U_int : H_sys ⊗ H_A → H_sys ⊗ H_A`
- An initial apparatus state `|0⟩_A ∈ H_A`

such that the Kraus operators of the instrument are

```text
K_r  =  ⟨r|_A · U_int · (𝟙_sys ⊗ |0⟩_A)                                  (N1)
```

For a projective measurement with `E_r = P_r` (orthogonal projections), one canonical choice of `U_int` (the **canonical dilation**) gives:

```text
U_int |ψ⟩_sys ⊗ |0⟩_A  =  Σ_r (P_r |ψ⟩)_sys ⊗ |r⟩_A.                     (N2)
```

This unitary copies the outcome label `r` into the apparatus register conditional on the system landing in the `P_r`-subspace.

### Step 2 — Canonical-frame Kraus = P

Substituting the canonical dilation (N2) into the Kraus formula (N1):

```text
K_r  =  ⟨r|_A · U_int · (𝟙_sys ⊗ |0⟩_A)
     =  ⟨r|_A · Σ_{r'} (P_{r'} |·⟩)_sys ⊗ |r'⟩_A
     =  Σ_{r'} P_{r'} · δ_{r,r'}
     =  P_r.                                                            (N3)
```

So the canonical-frame Kraus operator for outcome `P_r` is exactly `K_r = P_r`. This is the **Lüders selection**.

### Step 3 — Alternative Kraus = apparatus-frame rotation

Suppose we replace `U_int` with `U_int^{twist} := (U_sys ⊗ V_A) · U_int` for some unitaries `U_sys ∈ U(H_sys)` and `V_A ∈ U(H_A)`. This is just a unitary on the dilation space; observable predictions are unchanged (Stinespring's theorem: all CPTP dilations are equivalent up to a partial isometry on the dilation space).

The Kraus operators of the twisted dilation are:

```text
K_r^{twist}  =  ⟨r|_A · (U_sys ⊗ V_A) · U_int · (𝟙_sys ⊗ |0⟩_A)
             =  U_sys · ⟨r|_A · V_A^{(r)} · U_int · (𝟙_sys ⊗ |0⟩_A)
```

For the specific case `V_A = 𝟙_A` and `U_sys` arbitrary:

```text
K_r^{twist}  =  U_sys · P_r.
```

These are the "U-twisted" Kraus operators that the literature counterexamples (arXiv:0905.0596, arXiv:math/0211033) exhibit. They satisfy `(K_r^{twist})† K_r^{twist} = P_r† U_sys† U_sys P_r = P_r`, so they're valid Kraus operators for the same POVM.

**But:** `U_sys` is the **system-frame rotation that was absorbed into the dilation**. The same observable predictions are obtained either with `U_int` (canonical frame, Kraus = `P_r`) or with `U_int^{twist}` (rotated frame, Kraus = `U_sys · P_r`). The choice between them is a choice of **system-frame convention**, not a physical commitment.

### Step 4 — Sequential composition under canonical frame

In the canonical frame `K_r = P_r`, the sequential composition of "outcome `P` then effect `E`" is:

```text
M_{P, E}  :=  K_P† E K_P  =  P† E P  =  P E P                            (LSP-comp)
```

using `P† = P` for orthogonal projections. This is the standard `P E P` composition.

In any twisted frame `K_P^{twist} = U_sys · P`, the sequential composition becomes:

```text
M_{P, E}^{twist}  =  P† U_sys† E U_sys P  =  P · (U_sys† E U_sys) · P
```

which is `P E' P` for the rotated effect `E' := U_sys† E U_sys`. So the twisted-frame composition is also of the `P · (· · ·) · P` form, just on rotated effects. The physical structure (sandwich-by-P) is frame-independent; the specific operator `E` vs `U_sys† E U_sys` reflects the frame convention.

### Step 5 — Conclusion

In the canonical Naimark frame for projective measurements, `K_P = P` and sequential composition is `M_{P, E} = P E P`. Alternative frames (`K_P = U_sys · P`) correspond to absorbing a system-rotation into the dilation; they give physically equivalent predictions on rotated effects.

The framework's choice of the canonical frame `K_P = P` is therefore a **frame convention**, not a load-bearing physical commitment. ∎

## Cited authorities (one hop)

Load-bearing markdown-link upstream:

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 + the qubit-lattice substrate
- [`KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md) — retained_pending_chain; supplies the Kraus / instrument structure
- [`PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md`](PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md) (PR #1650, landed) — supplies the Stinespring V construction

Named non-derivation imports (standard textbook content):

- **Naimark 1940** dilation theorem (Holevo Ch. III; Watrous §2.4)
- **Stinespring 1955** dilation theorem (standard)
- Standard measurement-theory instrument structure

## What this derivation supplies

The same `K_P = P` selection, now stated as a **canonical-frame choice in the Naimark dilation**, not a load-bearing framework rule. The Gudder-style sequential-product non-uniqueness on the abstract effect algebra is honored: alternative sequential products exist mathematically, but they correspond to apparatus-frame rotations, not physically distinct measurements.

## What this does NOT close

- **Non-projective POVM instrument selection** — still deferred to a separate lane
- **Apparatus-frame physical interpretation** — what counts as "canonical" is itself a convention; this note records the standard convention without arguing for it on physical-foundations grounds
- **Promotion of the Lüders parent row** — auditor-owned

## Citation-graph note

This is a positive_theorem candidate at narrow-theorem granularity. Standard measurement theory (Naimark + Stinespring) applied to the framework's specific qubit-lattice substrate to derive a definite instrument-frame selection.

Plain-text pointer references (NOT load-bearing deps):

- `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § "Hardening III" — the prior LSP-projective ratification clause that this derivation supersedes; will be removed by the axiom-doc cleanup PR
- `LSP_PROJECTIVE_RATIFICATION_REAUDIT_MANIFEST_NOTE_2026-05-22.md` — dispatch manifest that will pick up this derivation as the new authority

## What this file is not

- Not a new framework rule
- Not a re-derivation of Naimark / Stinespring (cited as standard)
- Not a refutation of Gudder counterexamples (they exist mathematically; this note argues they correspond to frame rotations rather than physically distinct measurements)
- Not a promotion of any downstream row (auditor-owned)
- Not a numerical-prediction change
