---
claim_id: index_pairing_not_forced_kinetic_order_selector_no_go_note_2026-06-08
claim_type_author_hint: no_go
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Gamma/Edge Index Pairing Is Not Forced by the Baseline; Residual Kinetic-Order Selector

**Date:** 2026-06-08
**Type:** no_go boundary plus conditional-theorem sharpening of the turn-1 companion
**Primary runner:**
[`scripts/frontier_index_pairing_not_forced_kinetic_order_selector_2026_06_08.py`](../scripts/frontier_index_pairing_not_forced_kinetic_order_selector_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_index_pairing_not_forced_kinetic_order_selector_2026_06_08.txt`](../logs/runner-cache/frontier_index_pairing_not_forced_kinetic_order_selector_2026_06_08.txt)

## Role

This is a turn-2 source-boundary note for the internal/external `su(2)` double-use question. The
landed turn-1 companion
[`SU2_DOUBLE_USE_REDUCES_TO_ONE_INDEX_PAIRING_ADMISSION_BOUNDED_NOTE_2026-06-08`](SU2_DOUBLE_USE_REDUCES_TO_ONE_INDEX_PAIRING_ADMISSION_BOUNDED_NOTE_2026-06-08.md)
reduced the issue to one explicit index-pairing datum:

```text
the Clifford/derivative index μ of the (Kähler-/staggered-)Dirac operator
D = Σ_μ γ_μ ∂_μ is identified with the spatial lattice edge-direction μ acted on by O_h.
```

Turn 1 proved the conditional theorem: given that pairing and the dim-2 Quantum axiom, the spin
lift is the qubit's own `su(2)` with no dim-2 spectator. This note narrows the second question:
the pairing is **not forced** by the Lattice + Quantum + Record baseline plus the tested structural
constraints (locality, `O_h` covariance, and Hermiticity). The remaining open input is the
**kinetic-order selector**: why a first-order Dirac/staggered realization should be selected over a
second-order scalar spectator. Runner **11/11** checks the finite representation and spectator
witnesses; independent audit decides the row status.

This is the **rotation-level twin** of the landed boost-faith no-go
[`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md):
local-algebra faithfulness ≠ a faithful physical (rotation) action; covariance *presupposes*
the index pairing, it does not deliver it.

## Conditional-theorem sharpening (closes the turn-1 "wrong-rep hatch")

**Given** a first-order-in-space kinetic operator, the index pairing is forced and unique among the
2-dim internal `O_h` lifts. The vector-irrep multiplicity in the conjugation representation of
`M₂(ℂ)` is (runner multiplicity check, via the `O` character formula
`mult = (1/24)Σ_R |χ_ρ(R)|² Tr R`):

```text
spin/2O lift : 1      trivial lift : 0      E-irrep lift : 0
```

so **only the spin lift hosts a first-order `O_h`-covariant vector vertex**. In that lift,
`span{I, σ_i}` splits into scalar plus vector pieces with
`U_R σ_i U_R† = Σ_j R_{ji} σ_j`, uniquely fixing the vector vertex `A_μ ∝ σ_μ`. This is
representation-theoretic and independent of the matched-3=3 count or merger/cubic-lift reading
forbidden by the turn-1 guardrails. It sharpens turn 1: given first-order kinetic order, the spin
lift is the only 2-dim lift that can carry the vertex.

## The no-go core: first-order-in-space is the unsupplied antecedent

The antecedent, *"the kinetic operator is first-order Dirac, not second-order scalar Laplacian,"*
is a **dynamics selector absent from the baseline axioms**. The staggered/Dirac realization is an
open gate outside axiom content. A genuine all-constraints-satisfying spectator realization
survives: the second-order scalar Laplacian

```text
H(p) = (Σ_μ cos p_μ) · I₂
```

is local (nearest-neighbour), **full-O_h-covariant including spatial inversion** (`cos` is
parity-even), Hermitian, has a valid dispersion, and `[H, σ_i] = 0` exactly (runner B1) — the
**qubit genuinely spectates**. The cleanest spectator witness is this parity-even second-order
Laplacian. A first-order scalar hop does not survive full `O_h`: its
`Σ_{n∈O-orbit} sin(p·n)` symbol vanishes on every orbit and is parity-excluded. The first-order
gamma vertex `D=Σ_μ σ_μ sin p_μ` is by contrast qubit-active (`[D,σ_i]≠0`).

**No axiom-permitted selector picks first-order over second-order non-circularly** (runner E):

- **Record** supplies no dynamics and no kinetic order;
- **Positivity/stability does not select first-order**: the naive first-order Dirac symbol has a
  negative branch, while the second-order scalar Laplacian is bounded on the finite lattice;
- **Nielsen–Ninomiya** doubler-control bites *within* the first-order class, it does not force
  the class;
- the only thing that forces first-order is the **isotropic linear Lorentz cone** `|E|=|p|`,
  which is already the Dirac-form assumption and is circular for this claim. Isotropic `SO(3)` is
  **not** supplied by the cubic `O_h` (corroborated by the landed
  [`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
  and the boost-faith no-go).

So the residual is exactly a **kinetic-order selector**, which the baseline axioms do not supply.

## Boundary Relative To Turn 1

| turn | result |
|---|---|
| 1 (#3255) | the double-use reduces to the index-pairing datum; given the pairing, spin lift = qubit `su(2)`; matched-pair no-go is refuted (`2O→O` is consistent) |
| 2 (this) | the index pairing is not forced by the Lattice + Quantum + Record baseline plus the tested structural constraints; given first-order kinetic order, the spin lift is the unique 2-dim `O_h` lift carrying the vertex |

**Net:** the internal/external `su(2)` double-use is localized to the index-pairing/kinetic-order
selector. The present note does not supply that selector; it only shows why the baseline does not
force it and why the first-order conditional branch is unique once supplied.

## Residual and downstream

- **Minimal missing principle:** a lattice-native `O_h`-Wigner-covariance lemma deriving the
  `γ_μ↔e_μ` edge pairing *and* the first-order kinetic order from the baseline plus retained bridges
  *without* presupposing the γ-edge hopping form — none exists in the repo.
- The index pairing also gates three further named-open admissions
  ([`STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md`](STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md)):
  FS fermionic statistics, the Euclidean signature/time import, and the chirality selector
  `ε(x)`.
- **Downstream:** this is exactly the dirac-weyl physical-spin-label admission; emergent
  Lorentz's boost-spinor link remains a separate conditional; the Finkelstein–Rubinstein
  rotation→exchange bridge fails on discrete `Z³`, so spin-statistics stays forced-modulo
  {emergent Lorentz + Record}; **d=3 is unchanged** (a `Z³` lattice primitive; the
  `M₂(ℂ)=Cl(3,0)=GA(3)` match is a consistency, not a derivation — #2559/#2586 protected).

## No-Go Discipline Gate (N1-N8)

**N1 - Alternative routes.** Locality plus covariance does not force the pairing because the
second-order scalar Laplacian spectates. Baseline axiom content does not force it because the
baseline supplies no dynamics. Record does not force it because Record supplies no kinetic order.
Boost-faith analogy supports the boundary but does not by itself prove it. The two-realization
witness is constructed directly: first-order gamma vertex versus second-order scalar spectator.

**N2 - Wall independence.** The scalar-hop exclusion, second-order spectator, and no-selector
catalog are independent checks. Closing one does not automatically close the others.

**N3 - Hidden-wall scan.** "First-order," "covariance," and "isotropy" are tested explicitly, not
imported. The note does not treat `SO(3)` isotropy, a Dirac action, a Wigner-covariance lemma, or a
staggered/Kähler realization as baseline content.

**N4 - Residual matching.** The cited boost-faith and cubic-anisotropy no-gos attack the same
residual shape: local algebra or cubic symmetry does not force the relevant physical action. They
are comparators only; the runner supplies the direct rotation-level spectator witness.

**N5 - Rhetoric audit.** "Not forced" means not forced by the baseline plus the tested constraints.
It does not mean the index pairing is false, unphysical, or impossible.

**N6 - Partial-closure path.** A future lattice-native `O_h`-Wigner-covariance theorem or explicit
admission could close this residual without adding a new axiom. This note does not silently perform
that closure.

**N7 - Steelman.** The strongest pro-pairing argument is accepted: if first-order kinetic order is
supplied, the spin lift is the unique 2-dim lift carrying a vector vertex. The unresolved antecedent
is first-order kinetic order itself.

**N8 - Cross-cycle echo.** This matches the boost-faith and cubic-anisotropy pattern: local structure
and cubic symmetry do not automatically supply the physical action. Similar prior walls closed only
through explicit bridge work or admissions.

Status: PASS for the narrowed no-go boundary.

## Reprove-and-cite / guards

Reproven from primitives (numpy, 11/11): the vector-irrep multiplicity {spin 1, trivial 0, E 0};
the spin-lift scalar/vector split; the first-order-scalar orbit-vanishing plus parity exclusion;
the second-order Laplacian spectator (`[H,σ_i]=0`); the gamma-vertex activity; and the negative
branch of the first-order Dirac symbol. **Comparators / landed cites only** (never used to
*supply* the pairing): O character theory, Skolem-Noether, Nielsen-Ninomiya, the boost-faith and
cubic-anisotropy no-gos. No PDG. **Turn-1 inversion guards respected:** the pairing is not forced
from the matched-3=3 count, and the merger-273 / Cl(3) cubic-lift are not cited to supply it.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- [`SU2_DOUBLE_USE_REDUCES_TO_ONE_INDEX_PAIRING_ADMISSION_BOUNDED_NOTE_2026-06-08`](SU2_DOUBLE_USE_REDUCES_TO_ONE_INDEX_PAIRING_ADMISSION_BOUNDED_NOTE_2026-06-08.md)
- [`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md)
- [`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
- [`STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md`](STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md)

## What this note does NOT claim

- It does **not** claim the index pairing is false/unphysical — only that it is **not forced** by
  the baseline plus the tested structural constraints, with the unsupplied datum = the
  kinetic-order selector.
- It does **not** force the pairing from the matched-3=3 count, nor cite the merger-273 / Cl(3)
  cubic-lift to supply it (turn-1 inversions).
- It does **not** relocate d=3 onto the matter/Dirac dynamics (the #2586-closed move).
- **No** new axiom, primitive, or repo vocabulary; no PDG input; sets no audit status.

**Independent audit required.** This note asserts no effective-status change.
