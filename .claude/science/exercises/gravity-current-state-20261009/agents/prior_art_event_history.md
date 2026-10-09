# Prior art: the repo's event/DAG substrate history (sweep; Claude Opus 5.5 xhigh; 2026-10-09)

**Plain summary.**
- **The event era (about 2026-03-13 to 04-10) was never a causal set** in the Bombelli–Sorkin sense. Events had Euclidean coordinates, and the rules (edge lengths, angles, connection radius, a sorted "time" axis) came from those coordinates. That built in a preferred frame. On the 2D lattice the free dispersion is Schrödinger, not Klein–Gordon.
- **No causal-set test had been run before E1:** no Lorentzian sprinkling, no Benincasa–Dowker operator, and no study of noise per realization.
- **A date correction.** The move to Z³ was mid-April (`docs/MINIMAL_AXIOMS_2026-04-11.md:44-48`, inserted 04-15). The June 29 reset only reworded the axioms.

## What the event era established, and why it was dropped

- **Lorentz invariance** was built in by definition. The grid broke rotations by 8.2% at every scale. The later boost theorems hold only on the regular Hamiltonian lattice.
- **Gravity was a scalar phase-valley deflection only:**
  - it peaked at 5.1 SE at N = 30 and was "lost to CLT" at N = 60;
  - the distance law was flat on every random DAG;
  - light bending ×2 came from a supplied conformal metric;
  - **there was never a TT sector.**
- **Interference and Born.**
  - I₃ = 0 on a fixed DAG. The earlier I₃ up to 1e9 came from the DAG rebuilding itself when the setup changed.
  - |ψ|² follows from assumed linearity and reversibility.
- **Fluctuations.** On random DAGs the transfer matrices collapse to rank 1 (σ₂ < 1e-30). This "ceiling theorem" is a spectral no-go: random structure averages away.
- **Abandoned (04-06 frontier map: "EXHAUSTED").** The reasons:
  - no growth rule forces d = 3;
  - the angle-kernel anisotropy is intrinsic;
  - growth rules fail asymptotically;
  - the random-DAG distance law is a structural negative.

  The staggered-lattice lane won, followed by Cl(3)/Z³.

## Causal-set literature in the repo

- **Bombelli–Henson–Sorkin** is cited only as a contrast. The Benincasa–Dowker operator was named but never implemented.
- **The closest prior art** (archived, conditional PASS): `archive/.../CAUSAL_ORDER_RECORD_DENSITY_METRIC_RECONSTRUCTION_CYCLE46_NOTE_2026-07-14.md`. **Causal order plus a known uniform record density fixes the Lorentzian metric** (Hawking–King–McCarthy/Malament). Order alone leaves the conformal factor free. Continuum faithfulness and gravity dynamics are OPEN.
- **Classical sequential growth** gives "a broad family … rather than one member" (archived).

## Constraints from the axioms and campaign 8 (relevant to E1)

- **Record:** "A site never carries more than one record; records are permanent." Events sprinkled per 4-volume break "one record per site", and A6 shows one record per site plus permanence caps formations per site at one (EXACT).
- **A36:** "Records carry no time"; formation order cannot be recovered from a snapshot (EXACT). **So a causal order among record events is supplied, not read from records.**
- **The consequence:** E1 needs a change to Lattice *and* a supplied causal order. TESTS.md already marks E1 as a test setting only.

## What a new test must not repeat, and what to build on

**Must not:**
- put coordinates, angles, a radius or a sorted axis into the law;
- build the order from arrival times, or let it rebuild when the setup changes;
- report finite-N means across seeds as laws (the CLT and rank-1 collapse killed those). **Measure how the per-realization variance scales;**
- treat graph or BFS dimension as spatial dimension;
- claim E1 is compatible with the axioms.

**Build on:**
- Cycle 46's condition: show that the record density is uniform, or the scale factor stays free.
- R179/R181/R191 for E2: the density thresholds, and the induced EH coefficient surviving at p = 0.85. **Add S(0) and the TT channel, which nobody has measured.**
- **E1's tensor (TT) question is new:** the event era only ever had scalar gravity.
