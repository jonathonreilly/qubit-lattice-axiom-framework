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

- **#2624 (block 6, FRONTIER CORRECTION)** — real-QFT review (2 web-research agents + sympy/numpy)
  **REFUTES blocks 4/5**. The modulus `Tr log(M†M)⊃|b|²` (Coleman-Weinberg) has a rank-2 doublet
  Hessian → 2 real modes → **r=1 robustly**, chiral/Kähler-Dirac included (Alvarez-Gaumé: Re W=½·Dirac,
  Im W=η-phase). Chirality moves only the determinant **phase** (η) → δ=arg(b), **not** r. Holomorphy
  (r=1/2) needs a SUSY superpotential the framework lacks (Seiberg). (5/5)

## Verdict (corrected by block 6)

`Koide r=1/2` is **not** a theorem of the clean dynamics — all five trace/vector routes give `(1,2)`,
`κ=1`, **r=1**. **Block 6 strengthens this with real QFT:** the magnitude `r` is set by the
fluctuation-determinant **modulus** (`|b|²`-type, 2 doublet modes), which gives **r=1 robustly** — for
chiral and Kähler-Dirac fermions too. So the framework's `Q=1` prediction (vs empirical `Q=2/3`) is a
**real-physics-backed, robust partial falsification**, not a measure artifact.

**The chiral lead (blocks 4/5) is REFUTED.** Chirality affects only the determinant **phase**
(η-invariant) → the Koide **phase** `δ=arg(b)≈2/9`, **not** the magnitude `r`. The "gated bit" was
mis-assigned: `r` is `1` regardless of chirality.

**THE FRAMEWORK DOES NOT SOLVE KOIDE.** `r=1/2` (Q=2/3) is the genuine 45-year open problem — external
literature confirms `|b|/a=1/√2` is "not from first principles" (Rivero-Gsponer); the real obstacle is
pole-vs-running mass (Koide 2018); Sumino's family gauge boson only **protects** an assumed 2/3 and needs
a **continuous** U(3) family symmetry the framework (discrete C3) **lacks**.

## The two genuine open directions (post-correction, real physics)

The Koide problem cleanly **splits into two parameters with different physical origins** (block 6):

1. **Magnitude `r = |b|²/a²` (the Q=2/3 condition).** Set by the determinant **modulus** → `r=1`
   robustly. Getting `r=1/2` is the **45-year open problem**; per the real literature it needs
   **either** a vacuum-alignment principle forcing `|b|/a=1/√2` (none exists) **or** Sumino-type
   radiative protection (continuous U(3) family gauge boson — framework has only discrete C3). The
   framework's lattice (no continuum, mass at the lattice scale) may reframe the pole-vs-running
   obstacle, but cleanly gives `r=1` — so this is a **genuine tension/falsification**, not a gap a
   gate will close.
2. **Phase `δ = arg(b)` (Brannen ≈ 2/9 rad).** This is where the chiral structure actually lives:
   the determinant **phase** = the η-invariant. New, untried direction — compute whether the
   framework's η-invariant / chiral measure phase fixes `δ`. (Caveat: external review flags `2/9`
   itself as a possible numerical coincidence; the real target is "does the chiral structure fix δ
   at all," matching ~0.222 rad.)

## Next actions (priority order, corrected)

- **(C)** The 6 narrow blocks are on main (#2591/#2601/#2607/#2611/#2614/#2617 landed; #2624
  correction in flight). Once #2624 lands, the surface is consistent; a backward synthesis note
  (repo-canonical vocab) can record: *framework robustly predicts Q=1; r=1/2 is the irreducible
  BAE admission; chirality → δ not r.*
- **(Phase-δ)** Frontier-compute the η-invariant / chiral determinant phase of the corner sector
  and test whether it fixes `δ=arg(b)` near the empirical lepton value. Partly gated (needs the
  chiral/non-Hermitian mass), but the most tractable genuinely-new positive direction.
- **(Magnitude r=1/2)** The 45-yr open problem. A real contribution must derive `|b|/a=1/√2` from a
  vacuum-alignment or dynamical principle (not a reverse-engineered potential) AND address
  pole-vs-running. The framework lacks Sumino's continuous family symmetry — so either extend it
  (new structure) or accept the tension. Hold for owner direction; this is real new physics.
- **(D)** The staggered-Dirac substep-4 mass gate is still the framework's deeper structural gate
  (governs the phase-δ computation), but per block 6 it does **not** change the magnitude `r`.

## Discipline notes for the next session
- All blocks are CONDITIONAL on the open staggered-Dirac gate; none is bare `retained`.
- Branches: `physics-loop/dirac-corner-coupling-blockNN-20260604` off origin/main; pack on
  `physics-loop/dirac-corner-coupling-20260604`.
- Reprove-from-primitives + literature-as-comparator held throughout; no PDG values as inputs;
  no audit-lane data in PRs.
