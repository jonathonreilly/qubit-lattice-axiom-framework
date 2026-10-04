# Staggered-Dirac Direct Three-State Algebraic Support

**Current three-state boundary (2026-10-04):** The three-state result here is the finite corner-label algebra. Any following H_phys recitation is conditional on a supplied isometric embedding of the spatially periodic corner carrier and on implementation of the specified label operators. Those are additional hypotheses, not consequences of the finite runner or RP/OS alone. On finite spatial APBC there are no exact k = pi n corner states. Vacuum cyclicity and clustering concern the chosen vacuum representation and do not exclude other superselection representations. This packet supplies neither a physical embedding nor a species identification.

**Date:** 2026-05-07; 2026-10-02 operator-scope narrowing (Steps 2-3, theorem items (a)-(b))
**Type:** bounded support theorem
**Claim type:** bounded_theorem
**Status:** bounded source support for the direct three-state algebraic
surface inside a single `H_phys`. This note salvages the runner-backed
algebraic content only. It does not close the physical-species bridge,
does not assert a positive theorem, and does not identify the three
states as the framework's SM matter generations. The DHR route remains
misframed because Reeh-Schlieder + cluster decomposition are single-sector
inputs on the canonical surface, but replacing DHR with a direct algebraic
three-state calculation leaves a narrow species-identification bridge open.
**Authority role:** source note. Audit verdict and effective status are
set only by the independent audit lane.
**Primary runner:** [`scripts/probe_three_states_direct_derivation.py`](../scripts/probe_three_states_direct_derivation.py)

## Question

Can the DHR-framed physical-species bridge be sharpened into a direct
three-state algebraic support statement inside the single reconstructed
physical Hilbert space, using RP-OS reconstruction, translation-character
data, and the no-proper-quotient result?

## Answer

**Partly.** The three hw=1 states are algebraically distinct states in
one `H_phys`, and the runner verifies their translation-character
separation and C_3 cyclic action. That salvages bounded algebraic support.
It does not by itself derive the physical-species / SM-generation reading.

## Setup

### Premises (A_min for substep 4 reformulated)

| ID | Statement | Class |
|---|---|---|
| BlockT3 | hw=1 BZ-corner triplet has M_3(C) algebra (translations + C_3[111]) with distinct joint translation characters | retained per [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) and bounded support in [`STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md) |
| NQ | M_3(C) on hw=1 has no proper exact quotient | retained per [`THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md`](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md) |
| RP | A11 RP + OS reconstruction -> physical Hilbert space `H_phys` with unique vacuum `Omega` | retained per [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md) |
| RS | Reeh-Schlieder cyclicity: `A(O) Omega` dense in `H_phys` for any open region `O` | retained per [`AXIOM_FIRST_REEH_SCHLIEDER_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_REEH_SCHLIEDER_THEOREM_NOTE_2026-05-01.md) |
| CD | Cluster decomposition + spectrum condition -> unique vacuum, no superselection sectors on canonical surface | retained per [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md) |
| LR | Lieb-Robinson microcausality | retained per [`AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md) |
| LN | Lattice Noether fermion-number Q̂ on H_phys | retained per [`AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md) |
| SC | Axis-conditional single-clock codimension-1 evolution (unitary one-parameter group under B-AXIS) | conditional source boundary in [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md); not retained authority for temporal-axis selection |

### Forbidden imports

- NO PDG observed values
- NO lattice MC empirical measurements
- NO fitted matching coefficients
- NO same-surface family arguments
- NO new axioms
- **NO HK + DHR appeal (review identified this vocabulary as misframed)**

## Derivation

### Step 1: Supplied physical embedding

Work first on the finite corner-label carrier C^3. A physical interpretation
requires a supplied isometric embedding into a specified H_phys and an
implementation of the label operators there. Neither is established by the
finite runner. RP/OS can construct a representation from its own hypotheses;
vacuum cyclicity and clustering do not prove this embedding or classify all
superselection representations.

### Step 2: hw=1 triplet is a 3-dimensional subspace of H_phys

Under the supplied embedding: the hw=1 BZ
corners (1,0,0), (0,1,0), (0,0,1) are three orthogonal momentum
eigenstates within `H_phys`, with distinct simultaneous-eigenvalues
under the plain one-site lattice translations T_x, T_y, T_z (label
operators on the corner states; at most one of them is a symmetry of
the Kawamoto-Smit operator in any representative):

```
|(1,0,0)⟩: T_x = −1, T_y = +1, T_z = +1
|(0,1,0)⟩: T_x = +1, T_y = −1, T_z = +1
|(0,0,1)⟩: T_x = +1, T_y = +1, T_z = −1
```

These are three orthogonal STATES in H_phys, spanning a 3-dim
subspace `H_hw=1 ⊂ H_phys`.

### Step 3: M_3(C) algebra acts on H_hw=1 in the GNS image

On the supplied label carrier, by BlockT3 + NQ: the lattice translations T_x, T_y, T_z combined with
the C_3[111] cyclic generator generate the full M_3(C) algebra on
`H_hw=1`. The C_3 action is implemented by a unitary on `H_phys` through
the lattice automorphism / GNS representation in the cyclic
representative of the Block 03 gauge class, where the bare cycle is a
symmetry of the Kawamoto-Smit operator and preserves the hw=1
corner-label span; in the Block 03 representative η⁰ the covering
symmetry carries a sign field and does not preserve the η⁰ hw=1 span
(exact check: `scripts/staggered_dirac_corner_label_symmetry_scope_check_2026_10_02.py`). This note does not assert
that the C_3 generator is itself a local element of `A(Λ)`.

Specifically:
- T_x, T_y, T_z are plain one-site lattice translation operators acting
  on the corner states; they are not jointly symmetries of the
  represented Kawamoto-Smit dynamics (at most one of them commutes with
  it in any representative, and its translation symmetries anticommute
  pairwise)
- C_3[111] is the cyclic permutation `(1,0,0) → (0,1,0) → (0,0,1) →
  (1,0,0)` — the bare corner-label cycle, a lattice-symmetry unitary on
  the hw=1 label span in the cyclic representative

Both are single-Hilbert-space operators, not charged intertwiners between
separate DHR sectors.

### Step 4: Superselection scope remains open

The label calculation does not classify superselection representations. If
the embedding is supplied inside a chosen vacuum representation, its images
belong to that chosen representation. This is a conditional placement, not a
proof that other sectors do not exist.

### Step 5: Spectral distinctness gives algebraic separation

The three corners have DISTINCT joint translation eigenvalues (Step 2).
By the spectral theorem on H_phys (admissible standard math), states
with distinct simultaneous eigenvalues of commuting Hermitian
operators are ORTHOGONAL.

Distinct orthogonal eigenstates with the same algebraic M_3(C) structure
and different translation labels give a sharp three-state algebraic
separation. This is the bounded content checked here.

The physical-species reading, and especially the identification with SM
matter generations, is not derived by this algebraic separation alone.

### Step 6: Non-load-bearing phenomenology comparator

In the Standard Model, matter generations are distinct flavor states that
live in one Hilbert space and are not separate DHR superselection sectors.
This is a comparator only. This note does not derive masses, W-boson
couplings, Yukawa structure, or flavor-changing dynamics.

The comparator shows why the DHR-sector framing is the wrong vocabulary,
not that the direct three-state algebra has become a physical-species
theorem.

## Theorem 4-revised (Direct three-state algebraic support)

**Bounded theorem.** On A1+A2 + the bounded Grassmann/Kawamoto-Smit/
BZ-corner support chain + RP, RS, CD, LR, LN, SC + M_3(C) on hw=1 +
no-proper-quotient:

```
Conditional on a supplied isometric embedding of the spatially
periodic hw=1 corner-label triplet and its specified operators, the
three orthogonal label vectors embed in a supplied H_phys, characterized by:
  (a) distinct simultaneous-eigenvalues of the plain one-site
      translations T_x, T_y, T_z (label characters, not jointly
      symmetries of the Kawamoto-Smit operator);
  (b) connected by the bare C_3[111] corner-label cycle (a
      lattice-symmetry unitary in the cyclic representative; in η⁰ its
      covering symmetry does not preserve the hw=1 span);
  (c) carrying M_3(C) algebra structure (irreducible, no proper
      quotient);
  (d) within the chosen representation if that embedding is supplied;
      other superselection representations are not excluded.

The physical-species / SM-generation identification remains an open
bridge and is not part of this bounded theorem.
```

**Proof.** Steps 1-6 above. ∎

## Comparison to prior Block 05 framing

| Aspect | Block 05 (DHR-framed) | Block 02-revised (direct three-state) |
|---|---|---|
| Hilbert space structure | "Three superselection sectors of H_phys" | One H_phys, three states within |
| Key machinery | HK + DHR superselection (misframed for this surface) | RP+RS+CD single-Hilbert-space framing |
| Admitted-context | Broad DHR semantics | Narrow species-identification bridge remains open |
| Status tier | bounded theorem with broad AC | bounded theorem support with narrower open bridge |
| SM phenomenology comparator | DHR sectors are the wrong vocabulary | Single-Hilbert-space states are at least vocabulary-compatible |
| Compatibility with cited primitives | Incompatible with RS+CD single-sector framing | Compatible as algebraic support |

## Audit boundary

This note should seed as `bounded_theorem`. It does not write an audit
verdict, an effective status, or a retained-grade closure claim. It should
not be used to promote the parent realization gate until the narrow
physical-species bridge is derived and independently audited.

## What this supports

- DHR vocabulary is not the right way to express the three-state surface on
  the RS+CD single-sector canonical surface
- The direct hw=1 algebra gives three translation-character-distinct states
  inside one `H_phys`
- The remaining bridge is narrowed to physical-species identification rather
  than broad DHR/HK machinery

## What this does NOT close

- Substep 4 of the parent realization gate as a positive theorem
- The physical-species / SM-generation identification
- Any parent synthesis or publication status
- The g_bare = 1 normalization gate (formerly axiom A4) — separate
  campaign target

## Cross-references

- Parent open-gate (context only; parent now cites this note): `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
- BZ-corner algebraic support: [`STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md)
- RP A11: [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
- Reeh-Schlieder: [`AXIOM_FIRST_REEH_SCHLIEDER_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_REEH_SCHLIEDER_THEOREM_NOTE_2026-05-01.md)
- Cluster decomposition: [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
- Three-generation observable: [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
- Three-generation no-proper-quotient: [`THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md`](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md)

## Command

```bash
python3 scripts/probe_three_states_direct_derivation.py
```

Expected output: dependency-chain consistency check for the cited premises;
verification that three corner states are pairwise orthogonal under
translation eigenvalues; verification that C_3[111] generates a 3-cycle on
hw=1; and structural verification of the three-state-in-single-H_phys
algebraic support surface.
