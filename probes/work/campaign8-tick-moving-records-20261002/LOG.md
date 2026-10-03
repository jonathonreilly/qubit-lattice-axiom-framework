# Campaign 8 log (2026-10-02 20:30 → 10-03 08:30 EDT)

## 20:30–20:45 setup
- Brief written: `c8/BRIEF.md` quotes the axioms verbatim, the decided readings Q1–Q4 and Q7, ideas I1–I6 (instincts, not positions), the prior probes, the discipline rules and the deliverable format.
- Wave 1 launched in the background, one derivation agent per question:

| Agent | Question |
|---|---|
| A1 | Flow, index, covariance |
| A2 | Chirality from ticked steps |
| A3 | Moving-record consistency |
| A4 | Filling and black holes |
| A5 | Tick vs relativity |
| A6 | Rate clocks vs gravity |

- Heartbeat timer set to 45 min.

## 20:50 coordinator toy: `toys/weyl_walk_tool.py`

The tool is an independent checker for 2x2 ticked steps U(k). It computes:
- the nodes;
- each node's quasi-energy;
- each node's chirality, as the Chern number of the band just above the touching, through a small cube using Fukui–Hatsugai–Suzuki link variables;
- W3, by central differences.

Self-tests, all CHECKED:

| U(k) | W3 | Net chirality |
|---|---|---|
| Degree-one normalized map (m = 2) | +0.995 | −1 at the 0-gap, −1 at the π-gap |
| exp(−itH) of a two-node Weyl Hamiltonian | 0 | 0 |
| Fixed-order content-set conveyors e^{ik_xσx} e^{ik_yσy} e^{ik_zσz} (finite range) | 0 | 0 at both gaps, from 16 nodes in ± pairs |

In the first row the net chirality at each gap equals −W3. The third row means the naive conveyor product keeps doubling.

The grouping bug, where 0 and 2π were counted as different quasi-energies, was patched after the run.

## 21:05 A6 (rate clocks vs gravity) LANDED → c8/A6/REPORT.md (+ g1/g2/g3 scripts)

**(i) Moves are a clock; formations are not.**
- Under a translation-invariant law with permanent one-per-site records, E[formations at a site over all time] ≤ 1. Mean inflow equals mean outflow, so formation only raises occupancy. EXACT.
- Sustained formation is therefore a surface effect.
- Move events give a steady per-site rate: 12κu(1−u) for symmetric exclusion.
- Edge hop counts reproduce the landed (unaudited) endpoint-mean sharing rule at first order in density.

**(ii) Clock potential.**
- Setup: free records wander through an inert void, with no void formation. A concentration captures them irreversibly, so it is a net sink. Free records are a minority (u∞ < 1/2).
- Result: the move-event rate is r = r∞(1+Φ). Near the concentration Φ ≤ 0, so clocks run slower. Φ satisfies Δ_lat Φ = σ ≥ 0, the Regge note's sign.
- The far field has an exact 1/r tail with coefficient equal to the net capture current: a discrete Gauss law, EXACT via Liouville.
- Detailed-balance odds give a flat far field, so a non-equilibrium sink is required.

**(iii) Source.**
- The source is the capture distribution, not the record density.
- An opaque compact lump has charge equal to its capacity, which grows like its width (∝ N^{1/3}). That is non-additive. EXACT capacities: 3.96, 11.11, 18.94, 26.97, 35.10, 43.27 for cube sides 1–6.
- A transparent weak absorber is additive (Q ≈ qN) while qΣG ≪ 1. But under Q1 carriers cannot pass through recorded sites, which is an open edge.
- A jammed perfect absorber has event rate 0 inside ("time stops") and charge ∝ radius. That is a Schwarzschild-like scaling: an analog of I5.

**(iv) Failure modes.**

| Mechanism | Effect |
|---|---|
| Void formation or capture | screening |
| Breeding re-formation, including re-formation at just-vacated sites | anti-screening and runaway |
| Exporters, or majority carriers | wrong sign |
| Half-filled background | no first-order response |

- Conditional answer to the open question: for a 1/r clock potential, empty sites far from records must NOT form on their own.

**(v) Real-physics mismatches.**
- Lapse only.
- β_eff = 1/2 against GR's 1.
- No waves: changes spread by diffusion.
- Universality is not automatic.
- Establishment-time limits.

**Coordinator verification (CHECKED).** Reran g3 with independent seed 777, 60k ticks, u∞ = 0.04.
- Capture flux ratio to the Gauss prediction: 1.0136 ± 0.0095.
- r/r∞ follows the local-equilibrium prediction within max |Δ| = 0.0082 at s.e. 0.0076.
- The profile runs 0.31 (r=3) → 0.95 (r=13), with slower clocks near the lump.
- This reproduces A6's claim.

## 21:15 A3 (moving-record consistency) LANDED → c8/A3/REPORT.md (+ t1–t9 scripts, outputs.txt)

Two readings of a move, R1 and R3, behave very differently.

**R1: a move is a fresh formation with a cut.**
- The move rule is unique and automatically consistent.
- There is no interference; records diffuse, with variance ∝ t.

**R3: a guided record over possibilities that are never cut by moves.**
- *When a consistent rule exists (EXACT, Hall/Gale):* a consistent one-site move rule exists for every state iff the tick is strictly range-1.
  - exp(−iHτ) over a whole tick leaks: the probability of landing ≥2 sites from a just-formed record is 1−J0(2τ)²−2J1(2τ)². That is 0.285 at τ=1 and ≈τ⁴/2 for small τ.
  - So I2 plus consistency forces stepwise, strictly local change.
- *Rule (EXACT):* follow the net flow, T = J⁺/P, with J the time-symmetric (Margenau–Hill) flow of the tick.
- *On a line (EXACT):* the rule is always valid. It is unique given locality + consistency + no counterflow (flow-not-swap). Records ride a conveyor at +1/tick.
- *Where the rule is not fixed:*
  - On loops (2D/3D), the time-symmetric flow can break the outflow bound: 68 of 570 plaquette ticks. Repairs exist.
  - With several linked records a joint rule is needed. Literal I3 (independent proposals plus relative-odds collisions) misses by up to TV 0.50.
- *Lemma L1 (EXACT):* with one possibility per site on a ring, every range-1 tick is either pair-mixing (index 0) or a uniform shift (index ±1).
- *Step 10 (EXACT):* a covariant (proper rotations), homogeneous, number-conserving, range-1 tick with one possibility per site is U = e^{iθ}, so a single record never moves.
  - Moving records therefore need one of: cycling partitions, multi-site cells, or non-conserving ticks.
  - This is the analog of Meyer's scalar no-go.
- *No-signalling:* single-tick odds are always fine. Two-tick histories under natural guided rules depend on a distant choice by up to 0.32. So the trail must not be readable, or the rule must be "forgetful".
- *Record axiom fit:*
  - "records are permanent" would have to read as "never destroyed; may relocate".
  - Under R3, "locks" becomes "names".
  - Sentence 2's "keeps locked possibilities" conflicts with R1 and R3.

**Coordinator verification**
- **(a) Leak numbers, EXACT by hand.** For nearest-neighbour hopping the amplitudes are Bessel functions. 1 − J0(2)² − 2J1(2)² = 0.2847 matches A3's 0.285. At τ = 0.1, 2J2(0.2)² ≈ 5.0e-5 matches.
- **(b) Independent script `toys/verify_A3_line_rule.py`, written from the statement and not from A3's code.**
  - 800 random range-1 ticks on ring N=8: coin–shift–coin with d=2, and brickwork with d=1, 2, 3.
  - Continuity error ≤ 1.2e-15.
  - Outflow bound max excess 8.9e-16, 0 violations. CHECKED.
- **(c) Step 10 re-derived (EXACT).**
  - A unimodular Laurent polynomial on the torus is a monomial.
  - Rotation covariance equalizes the six neighbour coefficients, so the monomial is the constant term.

## 21:20 A5 (tick vs relativity) LANDED → c8/A5/REPORT.md (+ check_*.py)

**Conditions.** The result holds when two things are true:
- (a) menus and odds at a tick are set only by records from earlier ticks;
- (b) formation chance is linear in the site's possibilities. A nonlinear chance would signal outside the cone, Gisin-type. That gives a consistency condition on any formation-rate rule.

**Kept, EXACT.**
- Strict light cone: one site per tick per star-local layer. Continuous change has Bessel tails instead.
- Order of events outside each other's cone is unreadable.

**Schedule independence (T3.1, EXACT).**
- Schedules that order every linked pair alike give identical record statistics.
- So a global tick and neighbourhood ticks that rebuild the same event network cannot be told apart by records. Absolute simultaneity has no readable content.
- What is readable:
  - coincidences of linked formations (a fact about the network);
  - seams between regions whose ticks run at different rates.
- A global tick "rate" is unreadable.

**1D Dirac step (EXACT, CHECKED).**
- Dispersion: cos ω = cos m cos k. Deformed shell: ℰ² = μ² + 𝒫².
- Expansion: ω² = k² + m² − k²m²/3 + …
- Speeds: limiting speed cos m per species; massless content has v ≡ 1.
- Time dilation: R(v) = √(1 − v²/cos²m), which is Lorentzian with the species' own limiting speed.
- Inertial mass is tan m while rest energy is m.
- Universality caveat: an internal rotation locked to the tick does not dilate, so internal energy must enter as mass-like mixing.

**Quasi-energy (EXACT).**
- Quasi-energy is periodic, and there is a time doubler at (π, π).
- A winding band carries W sites per tick across every cut.
- No continuous local generator exists for an index ≠ 0 step: the Campaign 7 ARGUED flag becomes EXACT, modulo the GNVW and RWW theorems.

**Visibility of the beat.**
- Misaligned linked pairs make up p/(2−p) (EXACT under Q7).
- Estimator: p = 2F/(1+F).
- Triggered growth shows facets above the oriented-percolation threshold: p ≈ 0.645 on the square lattice, 0.382 on the cubic.

**Preferred frame and 3D (EXACT).**
- No new preferred frame: a covariant drift must vanish.
- 1D departures from relativity are quadratic and mass-suppressed, never linear.
- In 3D, covariance gives det U constant, and the lowest odd invariant has degree 9. So rotation-invariant two-band cones depart only at quadratic order.
- A strictly covariant six-ordering conveyor step splits at linear order: ω = |k| ± |k|²·n_x n_y n_z, with the two branches swapped by 90° rotations. For photon-like content that would be excluded by GRB timing/birefringence (LHAASO GRB 221009A: E_QG,1 > 10 E_Pl).

**Gravity link.** A pure rate field gives half the observed light bending (PPN γ = 0). This agrees with A6's β_eff = 1/2: rate or lapse alone cannot be all of gravity.

**Coordinator verification (EXACT by hand).**
- Tr U = 2 cos m cos k with det U = 1 gives the dispersion.
- R(v) identity: sin²ω − sin²k = cos²k sin²m, so R = |cos k| sin m / sin ω = |∂ω/∂m|.
- Small-k expansion of the conveyor product, cos ω = c_x c_y c_z ∓ s_x s_y s_z, gives the ±|k|² n_x n_y n_z split.
- A 90° rotation flips n_x n_y n_z.
