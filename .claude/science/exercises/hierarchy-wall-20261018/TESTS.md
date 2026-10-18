# Hierarchy wall exercise: step 8 tests

**T-SPIRAL (pre-registered 2026-10-18T16:39Z, before any run). Does an irreversible, cubic-covariant, nearest-neighbour two-state rule have a complex eigenvalue pair with a small Re/Im in its coarse-graining flow?**
- **Why this test.** It is the only escape still open that does not supply the number by hand (route R4, Lemma B and the spiral finding). Unitary and reflection-positive theories forbid spirals, through the c-, a- and F-theorems. The axioms state no reflection positivity, and record formation is irreversible.
- **Model.** Kinetic Monte Carlo with an irreversible record-locking rule: once a site locks, it never unlocks. Use at least two couplings, for example a formation rate and a neighbour bias, on Z² and Z³. Run a linearised real-space RG near its fixed points: a Monte Carlo RG with block-spin matching, or an equivalent method. State the method.
- **Readings.**
  - **SPIRAL-NATIVE:** some fixed point of a rule in the class has a complex eigenvalue pair with Re/|Im| ≤ 0.05, stable under changes of block size and method.
  - **SPIRAL-ABSENT:** every fixed point found has real eigenvalues, or Re/|Im| ≥ 0.1.
  - **OPEN:** otherwise.
- **Scope.** A complex pair is necessary, not sufficient, for a hierarchy; the coupling still has to start near the spiral. No claim about v is made by this test.

**T-SPIRAL-2: dated follow-up (2026-10-18T16:56Z), registered after the kill round and without seeing any T-SPIRAL result.**
- **Why.** T-SPIRAL's readout, Re/|Im| ≤ 0.05, is the wrong criterion. A flow with Re y = 0.5 and Im y = 10 passes it and still gives no hierarchy. The passage time is about ln(range)/|Re y| (K/REPORT.md; k5 checks). The T-SPIRAL readings stand as registered; these are added beside them.
- **Readings.**
  - **SPIRAL2-NATIVE:** a fixed point has |Re y| ≤ 0.06 per e-fold and |Im y| ≥ 1, the sign of the Lyapunov coefficient is reported, and the result is stable across block size and method.
  - **SPIRAL2-ABSENT:** every fixed point found has real eigenvalues, or |Re y| ≥ 0.2.
  - **OPEN:** otherwise.
- **Report also:**
  - whether the RG acts on the spacetime process or on the frozen record pattern;
  - whether a non-trivial fixed point exists at all under absorbing states;
  - checks against complex pairs that are artefacts of truncation.

**Result (recorded 17:03Z): SPIRAL-ABSENT and SPIRAL2-ABSENT.** Same-family run, unrefereed. See T/REPORT.md.
- **Lemma C (proved).** Take any clocked, irreversible, nearest-neighbour formation rule whose rates lie in [h_min, h_max]. Its finished pattern has a finite correlation length ξ ≤ 2d·e²·h_max/h_min. So there is no critical point at finite coupling for a flow to spiral around. A long passage needs a rate ratio of at least e^35, and that ratio is supplied.
- **2D:** no interior fixed point.
- **3D:** every zero is a box-filling artefact.
- **Open:** the level-time (light-cone) reading, which has a real critical point and where Lemma C does not apply.

**T-LIGHTCONE** (pre-registered 2026-10-18T18:35Z, before any run; Jon asked to "run the light-cone level-time test").
- **Question.** In the level-time (light-cone) reading of formation, where formation time is a lattice coordinate, the 09-23 note on main finds a reflection-positive bilayer that orders above β = 0.5905. Does the flow near that critical point give a slow passage of at least 38.4 e-folds from O(1) inputs?
- **Task.**
  1. Use the landed model as written.
  2. Locate the critical point.
  3. Extract the RG eigenvalues near it, via Monte Carlo RG, finite-size scaling or an exact method; state which.
  4. Check whether any direction is marginal (y ≈ 0), which would give a logarithmic flow of transmutation type.
- **Readings.**
  - **LC-SPIRAL:** a complex pair with |Re y| ≤ 0.06 and |Im y| ≥ 1, stable across methods and sizes.
  - **LC-MARGINAL:** a marginal direction with a nonzero first nonlinear coefficient. A passage of at least 38.4 e-folds then needs a starting coupling u0 ≤ 1/(b·38.4). State whether the model fixes u0 or supplies it.
  - **LC-HYPERBOLIC:** all eigenvalues are real with |y| ≥ 0.2. A hierarchy then needs a supplied distance δ ≤ e^{−38.4·y} from criticality.
  - **OPEN:** otherwise.
- **Scope.** No claim about v. This test only decides whether the class contains a native slow passage.

**T-LIGHTCONE result (recorded 19:58Z; same family; unrefereed): OPEN under the registered rule. No native slow passage.**
- **Model.** The landed level-time bilayer is a classical O(3) Heisenberg model. It is a comparator, because it re-records every site at every tick, which the Record axiom excludes. β_c = 0.5561(1).
- **Growing direction.** y_t = 1.40(1) is relevant and fast. A hierarchy would need a supplied tuning |β−β_c|/β_c ≈ 1e-22 to 1e-24.
- **No spiral.**
- **Cubic anisotropy**, the near-marginal direction in the O(3) class, is exactly zero by spin-rotation symmetry (proved).
- **Why OPEN.** The slowest irrelevant exponent ω is not resolved away from 0.2. An irrelevant direction cannot generate a scale (suggested).
- **Level time is diffusive at criticality** (z ≈ 2), not light-like.
- **Raw data** (132 MB) was not archived; the scripts and outputs were.

**LEE-1. Is the 0.03% match of v_cand = M_Pl(7/8)^{1/4}α_LM^16 to 246.22 GeV more than a coincidence?** (pre-registered 2026-10-18T21:10Z; Jon asked to probe it.)
- **(i) Look-elsewhere count.** Define the formula family before computing any number. Take the class
  M_Pl × r^{1/n} × c^k
  where:
  - r is drawn from main's own small rationals and zeta/eta ratios of the same kind as 7/8;
  - c is drawn from {α_bare = 1/4π, u₀, α_LM, ⟨P⟩, and their reduced variants};
  - n ranges over {1, 2, 4};
  - k ranges over 1..32.

  Fix the family in PREREG before evaluating anything. Count the members within 0.03% (and within 1%) of v. Report p_hit, the fraction of the family that hits.
- **(ii) Input robustness.** Recompute v_cand with:
  - the pure-gauge ⟨P⟩ (0.5934);
  - main's matter-inclusive or dynamical plaquette values, where they exist;
  - the stated uncertainty of each.

  Use dln v/dln⟨P⟩ = −4. Also use both M_Pl conventions (full and reduced).
- **Readings.**
  - **LEE-COINCIDENCE:** p_hit at 0.03% is at least 0.05; or the match moves by more than 10× its own size under any equally justified input or convention.
  - **LEE-SIGNIFICANT:** p_hit is at most 1e-3, and the match survives every equally justified input within 1%.
  - **OPEN:** otherwise.

**LEE-1 result (recorded 21:18Z; same family; unrefereed): LEE-COINCIDENCE.**
- **Look-elsewhere chance.** The chance that a random target gets a match this close within the 14,400-member registered family is p_global ≈ 0.05, with a range of 0.03–0.11 across family variants.
- **Defect in the registered p_hit.** It cannot work as a significance measure: column spacing allows at most one hit per column (proved).
- **Instability under justified inputs.**
  - Equally justified plaquette inputs (1-, 2- and 4-taste matter-inclusive values) move v_cand by 160–620× the size of the match.
  - The edge of main's own ±0.0006 band moves it by 16×.
- **A match is always available.** At each equally justified input, a different family member matches v just as well (post-hoc).
- **Reading:** the closeness of the match is generic to the family; the 0.03% is a coincidence at the registered scope.
