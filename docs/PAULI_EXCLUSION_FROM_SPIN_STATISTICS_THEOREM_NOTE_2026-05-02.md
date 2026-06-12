# Pauli Exclusion Principle in a Declared CAR/Grassmann Frame

**Date:** 2026-05-02
**Type:** bounded_theorem (proposed; audit-lane to ratify)
**Claim scope:** within a declared CAR/Grassmann fermionic mode algebra, for
any single-particle mode |φ⟩, the two-fermion Fock state with both particles
in mode |φ⟩ is identically the zero vector; equivalently, the squared
creation operator (a^†_φ)² = 0 and there is no normalizable CAR-frame state
with multiplicity > 1 in any single fermionic mode (Pauli exclusion
principle).
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome; the pipeline computes `effective_status`.
**Loop:** `positive-only-retained-20260502`
**Cycle:** 2 (Block 2)
**Branch:** `physics-loop/positive-only-block02-pauli-exclusion-20260502`
**Runner:** `scripts/pauli_exclusion_check.py`
**Log:** `outputs/pauli_exclusion_check_2026-05-02.txt`

## Cited authorities (one hop)

- [`AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md) — declared audit dependency for the CAR/Grassmann-frame algebraic surface. Its live effective status and claim scope are pipeline-derived. This note consumes only the conditional CAR-frame consequence: if the relevant modes are supplied as Grassmann/CAR fermionic modes, their creation and annihilation operators obey

  ```text
      {a_φ, a_ψ}      = 0
      {a^†_φ, a^†_ψ}  = 0
      {a_φ, a^†_ψ}    = ⟨φ|ψ⟩
  ```

  for any pair of single-particle modes φ, ψ in that CAR frame. The dependency
  does **not** by itself select CAR over hard-core-boson alternatives for all
  framework matter modes.

This is the **only** load-bearing one-hop dependency.

## Admitted-context inputs

- **Vacuum state |0⟩.** Standard QFT vacuum on H_phys, defined as the
  unique state annihilated by every annihilation operator: a_φ |0⟩ = 0
  for all φ. This is a basic structural definition, not a physics
  admission.
- **Linear algebra on H_phys.** Standard finite-dimensional inner-product
  space identities.

The Grassmann/CAR frame is a declared boundary of this note. Selecting that
frame for all physical retained matter, rather than a hard-core-boson frame,
is not proved here.

## Statement

Let `a^†_φ` be the creation operator for the single-particle fermionic
mode `|φ⟩` in a declared CAR/Grassmann frame covered by the stated
anticommutation dependency. Then, conditional on that CAR-frame boundary:

**(P1) Squared creation operator vanishes.** From the CAR
fermion anticommutator `{a^†_φ, a^†_φ} = 2 (a^†_φ)² = 0`, we have

```text
    (a^†_φ)²  =  0                                                            (1)
```

as an operator identity on H_phys.

**(P2) Two-fermion same-mode state is the zero vector.** For any
single-particle mode `|φ⟩`, the candidate two-fermion state

```text
    |φ, φ⟩  :=  a^†_φ a^†_φ |0⟩  =  (a^†_φ)² |0⟩                              (2)
```

is, by (P1), the **zero vector** in H_phys. It is therefore not a
normalizable physical state.

**(P3) Pauli exclusion principle.** No two identical fermions on the
declared CAR/Grassmann surface can simultaneously occupy the same
single-particle mode. Equivalently, the occupation number
`n_φ := a^†_φ a_φ` of any CAR fermionic mode satisfies `n_φ ∈ {0, 1}`.

(P1)–(P3) constitute the Pauli exclusion principle on the declared CAR
surface. They do not select the CAR surface from the framework primitives.

## Proof

The proof is a two-line application of the declared CAR anticommutation
relations:

### Step 1 — Squared creation operator (proves P1)

The declared CAR/Grassmann-frame dependency gives the anticommutation
relation

```text
    {a^†_φ, a^†_ψ}  =  a^†_φ a^†_ψ + a^†_ψ a^†_φ  =  0                        (3)
```

for arbitrary modes `φ, ψ`. Specialise (3) to the case `φ = ψ`:

```text
    {a^†_φ, a^†_φ}  =  2 (a^†_φ)²  =  0  ⇒  (a^†_φ)²  =  0                    (4)
```

This is (P1). ∎

### Step 2 — Same-mode two-fermion state (proves P2)

Apply (P1) to the vacuum state `|0⟩`:

```text
    a^†_φ a^†_φ |0⟩  =  (a^†_φ)² |0⟩  =  0 · |0⟩  =  0                       (5)
```

The candidate two-fermion same-mode state is the zero vector. ∎

### Step 3 — Occupation number n_φ ∈ {0, 1} (proves P3)

Define the occupation operator `n_φ := a^†_φ a_φ`. From the retained
anticommutator `{a_φ, a^†_φ} = 1` (mode-orthonormal basis):

```text
    n_φ²  =  a^†_φ a_φ a^†_φ a_φ
          =  a^†_φ ({a_φ, a^†_φ} - a^†_φ a_φ) a_φ
          =  a^†_φ a_φ - (a^†_φ)² (a_φ)²
          =  a^†_φ a_φ - 0                                                   (6)
          =  n_φ
```

using `(a^†_φ)² = 0` from (P1). So `n_φ²  =  n_φ`, i.e. `n_φ` is a
projection operator. Its eigenvalues are therefore in `{0, 1}`. ∎

This completes the proof of (P1)–(P3) on the declared CAR surface.

## Hypothesis set used

- `axiom_first_spin_statistics_theorem_note_2026-04-29` (declared audit
  dependency; live status and scope are pipeline-derived): provides the
  CAR/Grassmann anticommutation surface consumed here when the relevant
  modes are already supplied as CAR fermionic modes.
- Standard QFT vacuum definition `a_φ |0⟩ = 0` (admitted-context,
  structural).
- Standard finite-dim inner-product space identities (admitted-context,
  basic linear algebra).

No fitted parameters. No observed values. No physics conventions
admitted beyond the declared CAR-frame algebra. The CAR-vs-hard-core-boson
selection bridge remains outside this note.

## Corollaries

C1. **Anti-symmetric multi-fermion states.** For `N` identical
fermions in distinct modes `|φ_1⟩, …, |φ_N⟩`, the joint state

```text
    |φ_1, …, φ_N⟩  =  a^†_{φ_1} … a^†_{φ_N} |0⟩
```

is automatically antisymmetric under any permutation of the modes
(since the creation operators anticommute). This is the Slater-
determinant structure of multi-fermion wavefunctions.

C2. **Atomic shell structure (orientation only).** Once a physical electron
sector has independently been supplied as a CAR/Grassmann matter sector, the
Pauli principle is the familiar qualitative input to shell filling. This note
does not derive the electron-sector CAR selection, Coulomb Hamiltonian, or
atomic spectrum.

C3. **Stability of bulk matter.** The Lieb-Dyson stability of bulk
matter (Lieb-Dyson 1968, Lieb-Thirring 1975) requires Pauli exclusion
as load-bearing input. This corollary is recorded for future work; the
bulk-stability theorem itself depends on additional retained matter
structure (Coulomb potential bounds, etc.) that is not yet at retained-
grade on the live ledger.

C4. **Classical-statistics boundary inside the CAR frame.** CAR-frame
occupancy is bounded by one per mode. Any thermal Fermi-Dirac ensemble or
Maxwell-Boltzmann exclusion for physical matter additionally requires a
retained thermodynamic/readout bridge and the CAR-frame selection bridge.

## Honest status

**Bounded theorem candidate on the declared CAR/Grassmann surface.** Steps
1–3 close from the CAR anticommutation dependency alone, plus the basic vacuum
definition. No retained-family status and no framework-wide CAR selection are
asserted by this source note.

The runner verifies (P1)–(P3) by:

- explicitly constructing the fermionic creation/annihilation operator
  algebra on a small toy fock space (2 modes, Hilbert dim = 4) and
  numerically confirming `{a^†_φ, a^†_φ} = 0`, `(a^†_φ)² = 0`,
  `n_φ² = n_φ`;
- attempting to construct `(a^†_φ)² |0⟩` and confirming it is the zero
  vector;
- enumerating the full 4-dim Hilbert basis and confirming no state has
  any single-mode occupation > 1.

**Honest classification fields:**

```yaml
claim_type_author_hint: bounded_theorem
claim_scope: "(a^†_φ)² = 0 in a declared CAR/Grassmann frame for any fermionic mode |φ⟩; equivalently the two-fermion same-mode state is the zero vector; occupation number n_φ ∈ {0, 1}."
admitted_context_inputs:
  - declared CAR/Grassmann frame for the relevant modes
  - QFT vacuum definition a_φ |0⟩ = 0
  - basic finite-dim linear algebra
upstream_dependencies:
  - axiom_first_spin_statistics_theorem_note_2026-04-29
audit_required_before_effective_retained: true
```

These are author-side hints only. The independent audit lane sets the audit
verdict, and the pipeline computes any retained-family effective status after
that verdict and dependency closure.

## Citations

- CAR-frame input: `docs/AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md`
- standard external references (theorem-grade, no numerical input):
  Pauli (1925) *Z. Phys.* 31, 765 (original Pauli principle);
  Pauli (1940) *Phys. Rev.* 58, 716 (spin-statistics);
  Streater-Wightman (1964) *PCT, Spin and Statistics, and All That*,
  ch. 4.
