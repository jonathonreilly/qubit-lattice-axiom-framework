# Block 29 — physical-hermitian-hamiltonian-sme-bridge

**Date:** 2026-05-17
**Branch:** `physics-loop/physical-hermitian-hamiltonian-sme-bridge-block29-2026-05-17`
**Target:** `physical_hermitian_hamiltonian_and_sme_bridge_note_2026-04-30` (698 desc, audited_conditional, bounded_theorem)
**Sister of:** block 23 (PR #1469) which closed the algebraic Hermitian-lift half (Θ_H = P K).

## Honest status

POSITIVE NARROW CLOSURE on a distinct piece of the parent bridge's SME-side
conditional. Lands a class-A bounded narrow theorem on the **lattice-side
operator-completeness substep** of the bridge's conditional item (3)
("exclusion of CPT-odd bilinear structures outside the direction-resolved
hopping proxy"). Does **not** discharge items (1), (2), (4) of the bridge's
conditional, nor the continuum-side half of item (3).

## What lands (3 source-only files + cache + this report)

1. `docs/STAGGERED_HAMILTONIAN_DIRECTION_DECOMPOSITION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md`
   — bounded_theorem source note isolating (S1)–(S6):
   - (S1) `H = H_1 + H_2 + H_3` exact direction-decomposition of `H = i D`.
   - (S2) On-site (diagonal) Hilbert-Schmidt projection of `H` vanishes.
   - (S3) Longer-range (`d_per > 1`) projection vanishes.
   - (S4) Cross-direction NN projection vanishes (axis-alignment of all
     nonzero `H` entries).
   - (S5) Pairwise Hilbert-Schmidt orthogonality of `{H_1, H_2, H_3}`.
   - (S6) Direction-completeness: HS projection of `H` onto
     `(span{H_μ})^⊥` is zero.
   Single load-bearing markdown-link upstream dependency:
   `CPT_EXACT_NOTE.md` (parent staggered-phase content, class-A clean in
   the algebraic core; the conditional half is NOT cited).
2. `scripts/audit_companion_staggered_hamiltonian_direction_decomposition_bounded_exact_2026_05_17.py`
   — Pattern A audit-companion: numpy 3-d on `L ∈ {4, 6}` exact (D entries
   are rational `± 1/2`), sympy 1-d on `L = 4` exact symbolic, sympy 3-d
   on `L = 4` exact symbolic. 29 checks total covering (S1)–(S6) and the
   sister-narrow-theorem-disjoint character of the present claim.
   `PASS=29 FAIL=0`.
3. `logs/runner-cache/audit_companion_staggered_hamiltonian_direction_decomposition_bounded_exact_2026_05_17.txt`
   — cached PASS=29 FAIL=0 runner output.
4. `.claude/science/physics-loops/filter-excluded-positive-closures-2026-05-17/blocks/block29/BLOCK_REPORT.md`
   — this report.

## Theorem isolates (S1)-(S6) (lattice operator-completeness piece)

- (S1) Direction-decomposition `H = H_1 + H_2 + H_3` (matrix identity from
  the staggered phase prescription).
- (S2) `⟨x | H | x⟩ = 0` for every `x ∈ Λ`.
- (S3) `⟨y | H | x⟩ = 0` for every `(x, y)` with periodic Manhattan
  distance `d_per(x, y) > 1`.
- (S4) Every nonzero `H` entry has axis-aligned displacement (vacuous on
  the cubic NN lattice but explicitly tabulated).
- (S5) `Tr(H_μ^† H_ν) = 0` for `μ ≠ ν ∈ {1, 2, 3}`.
- (S6) Hilbert-Schmidt projection of `H` onto orthogonal complement of
  `span_C{H_1, H_2, H_3}` is exactly zero.

## Explicitly OUT OF SCOPE (parent bridge's still-open conditional)

- Continuum SME bilinear operator dictionary on the staggered Hamiltonian
  substrate (item (1) of the bridge conditional).
- Continuum-side basis completeness for the CPT-odd SME bilinear sector
  (item (2)).
- Continuum-side exclusion of CPT-odd bilinear structures outside the
  direction-resolved hopping proxy (continuum half of item (3); the
  lattice operator-completeness substep is the piece closed here).
- SME-zero leap from operator-level vanishing to continuum coefficient-
  level vanishing (item (4)).
- The Hermitian-lift symmetry algebra (Θ_H = P K) — that is the sister
  narrow theorem (PR #1469 / block 23), explicitly disjoint from the
  present claim.
- Interacting-theory operator content (gauge fields, Yukawa couplings).
- Continuum CPT theorem (Jost 1957, Streater-Wightman).

## Disjointness from block 23 / sister narrow theorem

The sister narrow theorem
`HERMITIAN_LIFT_THETA_H_PK_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md`
proves (L1)–(L4): `Θ_H = P K` antiunitary involution, `Θ_H H Θ_H^{-1} = H`
on `H = i D`, `H_odd = 0` matrix-entrywise, and `H_{μ,odd} = 0` direction-
by-direction. The present narrow theorem is **operator-structural** and
**independent of `Θ_H = P K`**: it uses only the matrix-entry structure
of `D` per (D), (η) to prove the staggered Hamiltonian has no Hermitian-
bilinear content outside `span_C{H_1, H_2, H_3}`. The two narrow theorems
attack different conditional pieces of the same parent bridge note:

| Piece                           | Closed by              | Status     |
|---------------------------------|------------------------|------------|
| Hermitian-lift algebra (L1)-(L4)| Block 23 (sister note) | retained   |
| Lattice operator-completeness   | **Block 29 (this note)** | proposed  |
| Continuum SME dictionary (item 1)| open                   | conditional|
| Continuum basis-completeness (item 2)| open               | conditional|
| Continuum coefficient-zero leap (item 4)| open            | conditional|

## V1-V5 candidate sketch (chosen V_winner = lattice operator-completeness)

- V1: Narrow theorem on `a_μ` SME coefficient matching (REJECTED: required
  continuum dictionary input).
- V2: Symbolic CPT-parity table for Colladay-Kostelecky basis (REJECTED:
  classification not a closure claim).
- V3: Trace coefficient `Tr(H_μ) = 0` direction-resolved (REJECTED:
  already trivially implied by sister theorem's `H_{μ,odd} = 0`).
- V4: Trace-based no-go on direction-resolved sectors (REJECTED:
  overlaps with sister theorem).
- V5: **Lattice operator-completeness theorem on `H = i D`** (CHOSEN):
  distinct from block 23 (operator-structural not symmetry-algebraic),
  closes a specific conditional substep (lattice side of item (3)),
  pure class-A algebra at the matrix level, sympy/numpy exact at runner
  precision on `L ∈ {4, 6}`.

## Verification

```bash
python3 scripts/audit_companion_staggered_hamiltonian_direction_decomposition_bounded_exact_2026_05_17.py
# PASS=29  FAIL=0
```

## Hard rules compliance

- A_min only: yes (operator-level decomposition of staggered Hamiltonian).
- Source-only PR: yes (1 source note + 1 runner + 1 cache + 1 block
  report under `.claude/`).
- No atlas/harness/audit-data touches: yes.
- No main push: yes (work on
  `physics-loop/physical-hermitian-hamiltonian-sme-bridge-block29-2026-05-17`).
- No merge: yes (PR for review only).

## Branch and PR

Branch: `physics-loop/physical-hermitian-hamiltonian-sme-bridge-block29-2026-05-17`
PR title: `[physics-loop] physical-hermitian-hamiltonian-sme-bridge-block29: lattice operator-completeness piece of bridge conditional item (3) on direction-decomposition of H = iD`
