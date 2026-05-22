# LSP-Projective Derivation from Naimark Dilation + Canonical Frame (Narrow)

**Date:** 2026-05-22
**Type:** bounded_theorem candidate
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Derive the Lüders projective-instrument selection `K_P := P` inside the **canonical Naimark/Lüders frame** for a projective measurement. This replaces the framework-rule ratification (`QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § "Hardening III") with a narrow derivation candidate for the canonical construction, without claiming that Naimark alone uniquely selects the physical instrument.

## Why this note exists

The 2026-05-22 LSP-projective ratification (PR #1661 / commit `886ce7e`) added `K_P = P` as a load-bearing framework-rule clause. Following the same audit-feedback that drove the k=1 derivation refactor, this note derives the same formula within the standard canonical projective-measurement construction (Naimark dilation + Lüders frame) rather than ratifying it as a framework rule.

## Honest scope

This note **does not**:
- Add a new framework rule
- Re-derive Naimark's dilation theorem from scratch (cited as standard)
- Address non-projective POVM instruments (still deferred, separate lane)
- Resolve Gudder-style sequential-product non-uniqueness on the abstract effect algebra (the literature counterexamples remain mathematically valid and are outside this note's uniqueness scope)

This note **does**:
- Derive `K_P = P` as the canonical-frame Kraus selection in the Naimark dilation
- Exhibit the frame-covariance relation: alternative `K_P = U·P` can be represented as a canonical Lüders step followed by a unitary frame/update; they are not ruled out as distinct instruments if the subsequent effect is held fixed
- Verify on multiple instrument families that the canonical-frame choice gives consistent post-measurement states

## Claim

For projective measurement of `P ∈ A_Λ` on a finite qubit-lattice region:

**Theorem (narrow).** Under the standard Naimark dilation of a projective measurement (system ⊗ apparatus with apparatus prepared in `|0⟩_A`), the **canonical-frame** Kraus operator for outcome P is

```text
K_P  =  P.                                                              (LSP-proj)
```

Any alternative `K_P^{twist} = U · P` for a unitary `U ∈ U(H_sys)` gives the same first-outcome POVM element `P`, because `(U P)†(U P)=P`, but it changes the post-measurement instrument unless the subsequent effect is rotated with the frame. Thus Naimark by itself does not prove uniqueness of the physical instrument. The narrow claim is only: in the canonical Lüders/Naimark frame, with no extra post-measurement unitary inserted, `K_P = P`.

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

### Step 3 — Alternative Kraus = post-measurement unitary/frame update

Suppose we replace `U_int` with `U_int^{twist} := (U_sys ⊗ V_A) · U_int` for some unitaries `U_sys ∈ U(H_sys)` and `V_A ∈ U(H_A)`. This is still a valid dilation of the same first-outcome POVM. It is not, by itself, the same instrument on later unrotated effects.

The Kraus operators of the twisted dilation are:

```text
K_r^{twist}  =  ⟨r|_A · (U_sys ⊗ V_A) · U_int · (𝟙_sys ⊗ |0⟩_A)
             =  U_sys · ⟨r|_A · V_A^{(r)} · U_int · (𝟙_sys ⊗ |0⟩_A)
```

For the specific case `V_A = 𝟙_A` and `U_sys` arbitrary:

```text
K_r^{twist}  =  U_sys · P_r.
```

These `U`-twisted Kraus operators satisfy `(K_r^{twist})† K_r^{twist} = P_r† U_sys† U_sys P_r = P_r`, so they are valid Kraus operators for the same first-outcome POVM.

**Boundary:** if subsequent effects are held fixed, `U_sys · P_r` and `P_r` generally produce different sequential statistics. They become equivalent only after a corresponding frame update of the later effect, `E ↦ U_sys† E U_sys`. The canonical Lüders frame is the convention that no such extra post-measurement unitary is inserted.

### Step 4 — Sequential composition under canonical frame

In the canonical frame `K_r = P_r`, the sequential composition of "outcome `P` then effect `E`" is:

```text
M_{P, E}  :=  K_P† E K_P  =  P† E P  =  P E P                            (LSP-comp)
```

using `P† = P` for orthogonal projections. This is the standard `P E P` composition.

In any twisted frame `K_P^{twist} = U_sys · P`, the sequential composition against the same later effect becomes:

```text
M_{P, E}^{twist}  =  P† U_sys† E U_sys P  =  P · (U_sys† E U_sys) · P
```

which is `P E' P` for the rotated effect `E' := U_sys† E U_sys`. So the twisted-frame composition is also of the `P · (· · ·) · P` form after rotating the later effect. Without that effect-frame update, it is a distinct instrument.

### Step 5 — Conclusion

In the canonical Naimark/Lüders frame for projective measurements, `K_P = P` and sequential composition is `M_{P, E} = P E P`. Alternative frames (`K_P = U_sys · P`) have the same first-outcome POVM and the same sandwich form after rotating later effects, but they are not excluded as distinct instruments when the later effect is held fixed.

The framework's choice of the canonical frame `K_P = P` is therefore a **standard projective-measurement convention**, not a uniqueness theorem for all instruments implementing the same POVM. ∎

## Cited authorities (one hop)

Load-bearing markdown-link upstream:

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies the qubit-per-site axiom on the `Z^3` spatial substrate

Named non-derivation imports (standard textbook content):

- **Naimark 1940** dilation theorem (Holevo Ch. III; Watrous §2.4)
- **Stinespring 1955** dilation theorem (standard)
- Standard measurement-theory instrument structure

Plain-text contextual pointers (not load-bearing deps):

- `KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md` — nearby framework instrument vocabulary
- `PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md` — nearby persistent-record Stinespring construction

## What this derivation supplies

The same `K_P = P` selection, now stated as a **canonical-frame choice in the Naimark dilation**, not a load-bearing framework rule. The Gudder-style sequential-product non-uniqueness on the abstract effect algebra is honored: alternative sequential products can define distinct instruments when later effects are held fixed. This note identifies only the canonical Lüders/Naimark representative and the frame-update equivalence relation.

## What this does NOT close

- **Non-projective POVM instrument selection** — still deferred to a separate lane
- **Apparatus-frame physical interpretation** — what counts as "canonical" is itself a convention; this note records the standard convention without arguing for it on physical-foundations grounds
- **Promotion of the Lüders parent row** — auditor-owned

## Citation-graph note

This is a bounded_theorem candidate at narrow-theorem granularity. Standard measurement theory (Naimark + Stinespring) applied to the framework's specific qubit-lattice substrate to identify the canonical projective-instrument frame.

Plain-text pointer references (NOT load-bearing deps):

- `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § "Hardening III" — the prior LSP-projective ratification clause that this derivation supersedes; will be removed by the axiom-doc cleanup PR
- `LSP_PROJECTIVE_RATIFICATION_REAUDIT_MANIFEST_NOTE_2026-05-22.md` — dispatch manifest that will pick up this derivation as the new authority

## What this file is not

- Not a new framework rule
- Not a re-derivation of Naimark / Stinespring (cited as standard)
- Not a refutation of Gudder counterexamples (they exist mathematically; this note only identifies the canonical Lüders/Naimark construction)
- Not a promotion of any downstream row (auditor-owned)
- Not a numerical-prediction change
