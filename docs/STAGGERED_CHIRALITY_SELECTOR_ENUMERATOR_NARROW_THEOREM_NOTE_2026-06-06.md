# One-Link Chirality-Selector Enumerator: the Staggered ε(x) is a Free Selector (Located at the Chiral Anticommutation)

**Date:** 2026-06-06
**Claim type:** bounded_theorem (decisive enumerator; resolves an exercise route)
**Status:** review-loop source proposal. Adds no axiom, no fitted input, no audit
verdict.
**Primary runner:**
[`scripts/frontier_staggered_chirality_selector_enumerator_2026_06_06.py`](../scripts/frontier_staggered_chirality_selector_enumerator_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_staggered_chirality_selector_enumerator_2026_06_06.txt`](../logs/runner-cache/frontier_staggered_chirality_selector_enumerator_2026_06_06.txt)

---

## Role

Builds the decisive artifact (route **R1**) that the `/exercise` on the
staggered-Dirac gate
([STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md](STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md))
isolated as the open atom: is the on-site staggered chirality field
`ε(x) = (−1)^{Σ x_i}` **forced**, or a **free selector** (admission)?

**Protocol / stop condition** (from the exercise): enumerate on-site chirality
assignments on a single nearest-neighbour bond; count inequivalent survivors —
**≥ 2 ⟹ free selector (admission); exactly 1 (up to global gauge) ⟹ a forcing
lemma exists.**

## Setup

A single bond = two sites `A, B = A + μ̂` of opposite sublattice parity.
Single-particle picture: `D = [[0,t],[t,0]]` (massless `A↔B` Dirac hop); the
lattice chirality is `γ₅ = diag(ω_A, ω_B)`, `ω ∈ {+1,−1}`. The staggered chiral
symmetry is the anticommutation `{D, γ₅} = 0` (the exact massless `U(1)_ε`).

## Result (runner SCORECARD 17/17 PASS)

- **Without** the chiral-anticommutation constraint, all four `ω`-assignments are
  valid on-site sign fields, in **two inequivalent classes**:
  - **trivial** `γ₅ = ±I` (`ω_A = ω_B`): **non-chiral / vector-like** matter
    (`{D,γ₅} ≠ 0`);
  - **staggered** `γ₅` (`ω_A = −ω_B`): **chiral** — the ε-staggering (`{D,γ₅}=0`).

  Both are consistent with the bare hop, so **≥ 2 inequivalent survivors ⟹ ε(x)
  is a FREE SELECTOR** on the `{Lattice, Quantum, Record}` surface. The chirality
  is an admission (`H_staggered_chirality`), a *second* staggered admission beyond
  `AC_φλ`.

- **With** the constraint `{D, γ₅} = 0`, only the staggered class survives
  (`ω_A = −ω_B`): two assignments = **one up to global gauge**. Extended to the
  bipartite lattice, `ω(x)ω(x+μ) = −1` on every bond has **exactly two** solutions
  `ω(x) = ±(−1)^{Σ x_i}` (verified for chains `N = 4,6,8` — the two sublattice
  2-colorings of the connected bipartite graph). So **`ε(x) = (−1)^{Σ x_i}` is
  forced up to global gauge — but only once the chiral anticommutation is
  imposed.**

## The pivot (synthesis)

> **`ε` is forced ⟺ the chiral anticommutation `{D, γ₅} = 0` is required.**

The framework does **not** currently require it: chirality is "out of scope" in
the staggered substeps and the `axiom_first_spin_statistics_theorem` is
**unaudited**. Therefore, on the current surface, **`ε(x)` is a free selector — a
genuine staggered admission, precisely located at the chiral-symmetry
requirement.** The retirement path is exact: a retained spin-statistics /
graded-locality theorem that supplies `{D, γ₅} = 0` forces `ε` up to global gauge
(the unique bipartite 2-coloring) — **no new axiom** beyond that theorem.

**Downstream:** once `ε` is fixed, the KS phases `η_μ(x)` follow deterministically
from spin-diagonalization — so `η` is *not* a separate atom; `ε` (equivalently,
the chiral symmetry) is the whole residual.

## Teeth / honest scope

- **Teeth:** the trivial `γ₅ = ±I` survivor is a genuine alternative — non-chiral
  (vector-like) matter, admissible on the bare surface. SM matter is chiral, so
  physics *needs* `ε`; but that need is the admission, not a derivation.
- **Scope:** finite-bond + bipartite-graph enumeration. It *locates* the
  admission (the chiral anticommutation) and gives the conditional forcing; it
  does not derive the chiral symmetry (that is the unaudited spin-statistics
  theorem). No new axiom.

## Reprove-and-cite ledger

- **Reproven here** (runner): the one-bond enumeration (trivial vs staggered
  classes; `{D,γ₅}=0` selecting staggered); the bipartite-graph 2-coloring count
  (`N = 4,6,8` → exactly 2 = `±(−1)^{Σx}`); the conditional forcing.
- **Cited**: the `/exercise` re-assessment that isolated R1; the staggered-Dirac
  substeps (chirality "out of scope"); the `axiom_first_spin_statistics_theorem`
  (unaudited) as the retirement target; `MINIMAL_AXIOMS_2026-06-05`.

## Audit dependency repair links

- [STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md](STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md)
- [STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
