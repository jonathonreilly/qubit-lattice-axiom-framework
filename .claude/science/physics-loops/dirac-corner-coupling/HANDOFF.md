# HANDOFF — physics-loop dirac-corner-coupling (2026-06-04)

## Campaign goal
Derive `|b|/a` of the C3-circulant generation Yukawa `H = aI + bC + b̄C²` from the
staggered-Dirac realization on the three hw=1 cubic-BZ corners; test whether the dynamical
corner coupling gives `r = |b|²/a² = 1/2` (Koide `Q = 2/3`) for a clean color-singlet fermion.

## Status: CORE RESOLVED at best-honest-status. Clean (non-gated) science exhausted.

The campaign reached a sharp, honest terminus with **5 review PRs** and a precisely
characterized **headline open lead**.

## The arc (one line each)

- **#2591** — `r=1/2` is NOT protected by any unitary symmetry (S3 forces degeneracy, C3
  leaves r free, 1-dim vs 2-dim irreps cannot be swapped). So it must be dynamical → this campaign.
- **#2601 (block 1)** — corner **fermion determinant** `det(M)` is shape-stationary at r=1
  (det=0) and r=4, never r=1/2; the full one-loop CW potential + any scale-only scalar agree. (10/10)
- **#2607 (block 2)** — in d=3 the 2³ staggered **taste** matrices span `M₂(ℂ)` = the on-site
  qubit (simple, unique 2-dim irrep, no multiplicity); taste-breaking can't manufacture the
  (1,1) weighting. Also resolves the `2^{3/2}` taste-count subtlety. (6/6)
- **#2611 (block 3)** — **multi-factor** Connes-Lott: by Schur, any flavor-blind factor
  preserves the (1,2) ratio; (1,1) needs a flavor-dependent operator = admission. Purchases,
  doesn't derive. (9/9)
- **#2614 (block 4, HEADLINE)** — completeness-critic pass: the chirality-graded **supertrace /
  equivariant index / holomorphic** count is GENUINELY UNTESTED (Probe 25's 7 routes are all
  plain `Tr`). It is the (1,1)/r=1/2 source — it counts the **complex** doublet param `b` once
  (chiral), where the real trace counts `(Re b, Im b)` twice. `ε` is flavor-blind → escapes
  block 3's analysis. **First route that could DERIVE r=1/2.** Corrects #2611's "exhausted". (6/6)
- **#2617 (block 5)** — Frobenius-Schur sharpening: `ν(trivial)=+1` (real → `a` real, 1 mode
  either way), `ν(ω)=0` (complex → `b`, 2 real modes vector / 1 holomorphic chiral). Refutes the
  "uniform complex rescaling preserves (1,2)" objection. **Reduces the whole Koide r on the clean
  lepton lane to ONE gated bit:** `r=1/2 ⟺ chiral` Yukawa, `r=1 ⟺ vector`. (7/7)

## Verdict

`Koide r=1/2` is **not** a theorem of the clean **trace/vector** dynamics — all five
trace-based routes give the `(1,2)` real-dimension weighting `κ=1` (r=1, Q=1), exhaustively
established. On the trace side, `r=1/2` is the irreducible `(1,1)` multiplicity admission
(= BAE). This is the exact, now-exhaustive content of Probe 29's partial falsification:
**the framework predicts `κ=1` for a clean color-singlet C3-triplet, in tension with the
empirical leptons `κ=2`.**

**The one escape, and it is genuinely promising:** the chirality-graded **supertrace/index**
route (block 4). It is flavor-blind, framework-present (`ε=(−1)^{x+y+z}`, `{ε,D}=0`), and the
Record axiom is neutral between trace and supertrace. If the generation fermion's fluctuation
determinant is the **chiral (holomorphic)** one — counting `b` once — then the weighting is
`(1,1)` → **r=1/2 → Q=2/3, derived**.

## What is GATED (the next campaign)

Resolving the headline lead requires the **staggered-Dirac mass/Yukawa** structure (kinetic-only
on main; mass at the open **substep-4** gate). The sharp binary:

> **r=1/2 ⟺ the generation Yukawa fluctuation determinant is chiral/holomorphic (counts `b`
> once); r=1 ⟺ it is vector/real (counts `Re b, Im b` separately).**

**Which way the bit likely falls (not proven):** all three arrows point to *chiral* → r=1/2 —
(i) the framework already carries the chirality grading `ε` with `{ε,D}=0` (kinetic, on main);
(ii) the generation triplet is forced by the *chiral* staggered/Kawamoto-Smit operator (per
`FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED`); (iii) the empirical charged leptons sit at r=1/2.
So the chiral resolution is the natural one — but it is **gated**, not derived, until the
substep-4 mass structure is shown to make the Yukawa fluctuation holomorphic.

## Next exact actions (priority order)

- **(A)** Strengthen #2614 with the **Frobenius-Schur** sharpening: trivial irrep is real-type
  (FS=+1 → `a` is one real param), doublet is complex-type (FS=0 → `b` is one complex param);
  the (1,1) count is FS-type-respecting, which resolves the "uniform rescaling preserves (1,2)"
  objection. Fold into #2614 or ship as block 5.
- **(B)** Conditional chiral-vs-vector determinant: compute both for the corner b-mode and show
  r=1/2 ⟺ chiral, r=1 ⟺ vector — reduces the whole question to the sharp gate binary.
- **(C)** Once #2591/#2601/#2607/#2611/#2614 land on main (reviewer cherry-picks), write the
  **backward** campaign-synthesis note (repo-canonical vocab; meta-framings-land-backward rule).
- **(D)** Pivot to the **staggered-Dirac gate** itself (substep 4) — the deeper problem
  everything is conditional on. Major; recommend owner greenlight before launching.

## Discipline notes for the next session
- All blocks are CONDITIONAL on the open staggered-Dirac gate; none is bare `retained`.
- Branches: `physics-loop/dirac-corner-coupling-blockNN-20260604` off origin/main; pack on
  `physics-loop/dirac-corner-coupling-20260604`.
- Reprove-from-primitives + literature-as-comparator held throughout; no PDG values as inputs;
  no audit-lane data in PRs.
