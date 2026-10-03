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

## 21:40 A4 (filling, black holes) LANDED → c8/A4/REPORT.md (+ toys, t1lib.py)

**Bookkeeping (EXACT)**
- With no moves, every site has a final state.
- With moves and permanent records, a homogeneous grid gains ≤ 1−ρ₀ records per site in total. This matches A6.
- Events need empty sites: E ≤ 2h.
- If time is the accumulation of records, each region's record-time is bounded.

**Lone-hole criterion.** p₀ is the formation odds of an empty site enclosed by records.
- p₀ > 0: exponential freezing. EXACT wherever there is a floor; for F-spont, h = h₀(1−p)^t exactly.
- p₀ = 0 with moves: thinning. Events last forever but get sparser, t·h ≈ 5.2 in 3D (MF/CHECKED).
- A steady nonzero rate needs formation to stop for reasons beyond the record pattern (ARGUED).
- **Open question answered conditionally (EXACT):**
  - If empty sites form on their own (odds ≥ p_min > 0), every region freezes.
  - If not, the empty grid stays empty and activity spreads as fronts.

**Crowd-tilted moves**
- Above an onset there are two phases: g_c ≈ 1.0–1.25 in 2D and 0.70–0.75 in 3D (MF closed form for the comparator model K).
- No jam is sealed.
  - Edge escape odds are 1/(e^{(z−1)g}+1) > 0.
  - Interior holes move with probability 1−2^{−z} per tick, so time slows inside but does not stop.
- Jams evaporate in empty surroundings, with ~99% of escapees returning.
- The net loss is diffusion-limited: ∝ R in 3D, so lifetime ∝ N^{2/3}. That is the opposite trend to Hawking (loss ∝ 1/M²), which falsifies a literal black-hole analogy for this mechanism.

**Event-rate profile**
- At balance it is flat beyond about 4 sites (CHECKED, ±6%).
- A harmonic profile (1/r in 3D) appears only during inflow, with its strength set by the inflow. Outflow flips the sign.
- This is consistent with A6, where a net sink is required.

**Coordinator check (EXACT by hand).** Leak odds: 1/(e^{3g}+1) = 0.1824 / 0.0474 / 0.0110 at g = 0.5 / 1 / 1.5, and the 2D corner 2/(e^{2}+2) = 0.2130, both matching A4's exact table. The 3D evap/profile runs are going in the background (toys/A4_big3d.log).

## Synthesis note (coordinator, 21:45)
- A4 and A6 agree:
  - Empty space must not form on its own.
  - The time-as-records budget per region is bounded.
  - A 1/r clock profile needs a net sink or inflow.
- A5 T1.2: the formation chance must be linear in the possibilities, or it signals.
- Candidate the panel should test critically: linear + covariant + local + vacuum-quiet ⇒ formation chance = ⟨F_x⟩ with F_x ≥ 0 a local covariant operator that annihilates the vacuum. One example is local excitation-energy density, which would mean records form where energy is.
- This ties to the vacuum-ruling memory (tick = formation rate; source T_00).
- Launched A9 to test it.

## 21:55 A1 (flow, index, covariance) LANDED → c8/A1/REPORT.md (+ scripts)

**Net flow**
- Net flow is a conserved, quantized vector (D1–D6, EXACT). It is the same at every cut and cannot start or stop.
- Local schedules of finite moves cannot make flow (D5, EXACT). So if ticks are neighbourhood-local, a conveyor is impossible; it needs one global step.
- Quantum version: the GNVW index (comparator).

**Covariance (D12, EXACT)**
- Soldered C2 rotations reverse the flow vector, so a covariant tick carries ZERO net flow.
- The standing conveyor is therefore incompatible with the axioms' covariance.
- What remains are zero-net counter-passing moves: swaps and plaquette loops.

**Many-body (D24–D27, EXACT)**
- One qubit's up and down parts cannot go to different places.
- That needs ≥ 2 movers per site, or a graded split (Majorana), which is not covariant (D28).

**Walks and chirality**
- Covariant content-set sum S: not unitary (S†S ∈ [1,9]).
- Normalized S̃ = S/|S| (D14):
  - covariant and unitary, but QUASI-local with exponential tails;
  - nodes only at the 8 TRIM;
  - ν3 = +2, i.e. net handedness 2 at quasienergy 0.
- Ordered products (BCC Weyl walk) (D15): strictly local, but only C2-symmetric; ν3 = 0.
- D18 (EXACT, derived here): every strictly local, exactly covariant spin-½ walk has zero long-wavelength speed. Axis speed and √3 × speed would both have to be integers.
- D20 (EXACT given Suslin's SL_N = E_N over Laurent rings, comparator): ν3 = 0 for EVERY strictly local walk on Z³, any coin, covariant or not. This is a discrete-time doubling statement.
- So net handedness needs one of:
  - faint (quasi-local) reach per tick;
  - boundaries or defects;
  - interacting many-body (Haah-type) QCAs.

**Handedness (D22)**
- Content-set (spin-locked) flows are handed: the mirror image of W_θ is W_{−θ}.
- Slot flows are achiral.

**Synthesis tension (coordinator)**
- A3: strict I2 (≤1 site/tick) plus consistent record positions forces strictly range-1 ticks.
- A1: strictly local ticks have ν3 = 0, so doubling persists in single-particle walks.
- So under strict I2, net chirality has to come from many-body structure or boundaries, OR the owner allows faint reach.
- This is an owner decision point.

## 22:10 Coordinator checks

**(a) A4 3D runs (toys/A4_big3d.log; big3d_evap_profile.py; g = 1.0).**
- Evaporation:
  - Cube of side 8 (N = 512): net loss 0.156 ± 0.003 per tick, against the diffusion-limited estimate of 0.142 (ratio 1.09), which supports diffusion-limited loss.
  - Half-lives: 120 ticks (side 4) and 1087 ticks (side 8), i.e. roughly ∝ N^1.06 between these sizes. That is not the predicted N^{2/3}, but small jams evaporate anomalously fast (Gibbs–Thomson-type), so the exponent is unsettled.
- Event-rate profiles:

| Far density | Regime | Profile fit |
|---|---|---|
| ρ_far = 0.012 ≈ ρ_v | balance | flat (A fit χ²r = 0.20) |
| ρ_far = 0 | outflow | events more frequent near the jam (A + B/r, B = +0.099, χ²r = 0.18; flat χ²r = 237) |
| ρ_far = 0.02 | inflow | events sparser near the jam (B = −0.092, χ²r = 1.07; flat χ²r = 37) |

- These confirm A4's three signs in 3D. The exact inflow shape is unsettled over r ∈ [10, 20].

**(b) A1 D20/D14, independent script toys/verify_A1_D20.py.**
- Six random strictly local walks (3–9 coin + shift layers, random axes and bases): W3 = 0 within grid error 0.002.
- Quasi-local covariant S/|S|: W3 = +1.991 ≈ 2. CHECKED.

## 22:20 A2 (chirality from ticked steps) LANDED → c8/A2/REPORT.md (+ scripts)

**Main answer: NO (EXACT within its class).** The class is translation-invariant, finite content per site, strictly finite range, reversible single-particle steps. Within it, W3 = 0 always, so doubling persists at every quasi-energy.

**Chirality and W3 (D2, D3)**
- Two-band case (EXACT): at each quasi-energy, the net chirality of the nodes equals −W3. Both the Ũ = +1 class and the Ũ = −1 class sum to −W3.
- n-band case: ARGUED via transgression, adding Fermi-surface Chern numbers.
- This is how ticks differ from continuous generators: the two classes are forced equal, not forced to zero.

**Why W3 = 0**
- **D4 (EXACT):** a continuous generator, even time-dependent or quasi-local, forces W3 = 0. So does a quasi-energy gap anywhere.
- **D5 (EXACT, self-contained):** every circuit of content-set shifts plus local mixing, at any depth, has W3 = 0, by Polyakov–Wiegmann additivity.
- **D6 (EXACT via standard K-theory):**
  - SK1(C[z1±,z2±,z3±]) = 0, so every strictly local step factors as a unit times elementary matrices.
  - Hence W3 = 0.
  - This independently matches A1 D20 (Suslin).
- **D7 (EXACT):** a W3 ≠ 0 step cannot be uniformly approximated by strictly local unitaries; the sup distance is 2.

**Covariance and the flow index (D8)**
- The flow index is the det winding m. Covariance forces m = 0, so a covariant strictly local step is null-homotopic.
- **Campaign 7's flag should be NARROWED:** in 3D the index that steps add is flow, which covariance already excludes, and the chirality index is excluded by strict locality alone.

**Readings of one qubit per site (D9)**
- **Empty/occupied, number-conserving:** a scalar walk, so it can only be a rigid conveyor, and covariance gives nothing moves. This matches A3 Step 10.
- **Majorana/pairing:** W3 = 0 even when quasi-local.

**Spin-½ soldered 2-band steps (D10)**
- Touchings are pinned at all 8 TRIM (Schur).
- A nearest-neighbour single-layer covariant step is constant.
- Parity rule: W3 ≡ n₋ (mod 2).

**Relaxations that allow W3 ≠ 0 (D12)**
- **E3:** quasi-local, covariant under all 24 rotations, W3 = −1, with a single node at Γ at quasi-energy π. Its hoppings decay ~e^{−0.8/site}. This matches the coordinator's degree-one test.
- **E4:** strictly local but not reversible, W3 = +1.

**Searches**
- Adversarial r = 1: 9 exactly unitary solutions, all W3 = 0.
- r = 2 seeded from E3: the defect does not reach 0, consistent with the theorem but not decisive.

**Budget note:** run5d_gn.py peaked at 510 MB for about 8 s, over the 300 MB cap. No harm resulted; logged honestly.

**Coordinator cross-check:** A1 and A2 reach the same theorem by different routes (Suslin SL=E, and K-theory SK1 = 0 with PW additivity). The coordinator's random strictly-local walks gave W3 = 0 and the quasi-local covariant walks gave W3 = ±1, ±2. The three are consistent.

## 22:45 A8 (additive, universal clock source) LANDED → c8/A8/REPORT.md (+ a8_* scripts)

**(i) Additivity: conditional yes.**
- **The identity (EXACT):** Q = q·Σ_i N_i. This is a lapse-weighted charge, comparable to the Tolman/Komar mass ∫(ρ+3p)N without the pressure term.
- **Bounds:** qN/(1+qḡ) ≤ Q ≤ min(qN, Cap).
- **One-parameter collapse:** t = qN/(4πR), the "compactness" (EXACT for the continuum ball; CHECKED on the lattice).
  - t ≪ 1: additive.
  - t ≫ 1: capacity ∝ R, the surface clock → 0 and the interior is frozen. This is black-hole-like, with crossover R_c = √(3/(qn)).
- **Q1 exclusion:** a packed lump captures only at its skin (area law for weak q, capacity for strong q). So additivity needs matter that is sparse at the lattice scale (CHECKED: packed-cube area law 0.3315 vs 0.3333).
- **The shared-possibility flow is not a second carrier (EXACT):**
  - B0: a fixed two-site change that keeps every locked content must be non-interacting. Keeping locks therefore means compression: the recorded site acts as a one-site field (the "push" model of the timing probes).
  - So recorded sites are walls, and a jammed region holds no flow.
  - A coherent flow gives a 1/r² shadow (Le Sage-like, ARGUED).

**(ii) Universality: conditional yes.**
- Every event must be gated by one wanderer arrival. Presence-gating gives the WRONG sign.
- The change between records must itself be event-paced, i.e. a local, influenced tick. A globally paced change leaves atomic-type clocks unslowed.
- β is locked at 1/2 under universality (EXACT, mean field). β = 1 needs a hop law that kills arrival gating, so universality and β = 1 are incompatible in this class.

**(iii) Emergent sink: conditional yes (CHECKED).**
- Rule: a wanderer stops on content agreement with STOPPED neighbours. Gauss then emerges: J_MC/J_pred = 0.97–1.01, deficit/Poisson = 1.02.
- Runaway DLA-like accretion follows.
- It needs a "stopped" status visible in the conditions. With content alone (R-all), clumps dissolve and there is no field.

**(iv) Weakness: not natural.** It needs q ≈ 10⁻¹⁸ on a Planck lattice, while the odds are O(1) (Q4 gives ½).

**Falsifiers**
- binding counted twice (Nordtvedt-type);
- composition dependence O(n);
- β = ½ and γ = 0;
- no waves;
- establishment time ~50 μm;
- runaway accretion.

**Owner-relevant synthesis**
- Gravity-like dilation that is universal needs the tick to be LOCAL and INFLUENCED: everything paced by local record events.
- A5 already showed that a global vs neighbourhood tick can't be told apart by the record network. A8 adds that if the beat is to behave like gravity, the experienced beat must vary by neighbourhood.

## 23:00 A9 (formation where the energy is) LANDED → c8/A9/REPORT.md (+ scripts)

**Theorem 1 (EXACT).** No-signalling, locality and steering (via Q1 sharing) force the per-tick formation chance to be tr(F_x ρ), with 0 ≤ F_x ≤ 1 on the star for each recorded-neighbour pattern. Dependence on the classical record contents is unrestricted.

**Theorem 2 (EXACT).** The formation step must be a local instrument. Specifically:
- **(b)** Lock odds must be computed AFTER the formation update; the product rule signals (0.08). This is a flag for Campaign-7 sentence 3, "odds from the site's own part", which must be read post-update.
- **(c)** A no-record tick must also update the possibilities (√(1−F) is the minimal choice); otherwise two-tick histories signal (0.04).
- **(d)** Menus may depend freely on RECORDS (Q7). A menu set by unrecorded or shared possibilities signals, by up to 0.47.

**Quiet vacuum**
- **Criterion (EXACT):** a vacuum is quiet iff its star marginals are rank-deficient, iff it is a frustration-free zero-energy ground state of ΣF_x.
- **Q4 plus quiet ⇒ neighbours must share.**
- **Covariant quiet vacua exist:**
  - ferromagnetic (aligned) states;
  - Klein singlet coverings (7-body star projector);
  - the cluster state (finite internal covariance only).
- **The half-filled staggered sea, the repo's vacuum ruling, is NOT quiet.** No local linear rule leaves it quiet (EXACT for the massless sea).
  - The best rank-1 vacuum rate is 5e-6 per tick; the energy-based rate is 0.012.
  - A quasi-local weight's vacuum rate falls as R^-3.
  - On Planck ticks, staying unfrozen needs ε ≲ 1e-61, a cosmological-constant-like fine-tuning (dimensional only).

**F = the change's own energy (a named conditional, not forced)**
- It forces a frustration-free change, whose gapless excitations have z ≥ 2 (comparator).
- That conflicts with photons (z = 1). Cross-link: the repo's photon velocity → 0 at the RK point.

**Other consequences**
- Records form where things happen. Covariance makes records relational.
- Soft "dark" modes escape recording: exactly |⟨u|ψ0⟩|².
- Lone-hole odds p0:
  - Klein: ≥ 1/7!, so it freezes.
  - Ferro: zero iff all six recorded neighbours agree.
  - Variant B (records not in F): thinning, but 19–55% of excitations end up caged.
- Source tracking energy density: majority carriers act as a transparent absorber with source ∝ e (closer to T00). Minority carriers act as exporters, giving the wrong sign.

**Coordinator verification (CHECKED; toys/verify_menu_signalling.py, independent)**
- Setup: x, its neighbour y, and distant b; b's menu is Z or X.
- "Own-state" menu (axis of x's own Bloch vector): TV of x's record content between b=Z and b=X is 1.0000 for the x–b singlet, and the maximum over 400 random states is 1.0000. That is MAXIMAL signalling.
- "Recorded-neighbour" menu (axis from y's record): max TV 3.6e-16. No signalling.

**CONSEQUENCES**
- **(1)** Owner's Q7 ("menu set by the conditions, incl. recorded neighbours") must be read as set by RECORDS, or by one joint linear instrument. Otherwise it signals.
- **(2)** The "own" menu rule in the 2026-10-02 timing probes (ai/probes bebecfb8fa, B2/D 'own' columns) is a signalling rule, so those columns are illustrative only. The 'field' (recorded-neighbour) results stand.
- A correction note will be added to that README.

## 23:10 A7 (readable trails and signalling) LANDED → c8/A7/REPORT.md (+ e1–e20, mtlp.py)

- **Lemma 1 (EXACT).** If each record's move odds use only local data (L_odds), multi-tick no-signalling follows automatically. The obstruction is therefore not locality.
- **Step 2 (EXACT).** Moves that are independent given the past (Bell local causality) fail consistency. CHSH reaches 2√2.
- **Step 3 (EXACT).** If no position is ever registered, a correlated "forgetful re-draw" satisfies all four conditions (C, L, NS, I).
- **Step 5 (EXACT).** The one-site limit itself registers positions: a record's later position remembers its earlier one.
- **Step 6, main result (EXACT).** Readable positions every tick plus uncut linked possibilities force signalling under EVERY rule. Wigner/triangle argument, minimal instance: B's own two-tick history moves with A's distant choice by TV ≥ √2 − 1 = 0.414. The LP attains this, with a dual certificate.
- **Step 8.**
  - A full cut of the reading record (R1) restores everything (EXACT).
  - Cutting the partner does not help.
  - Partial cuts fail for every λ < 1, with gap ≈ (1−λ)²/2 (CHECKED).
- **Step 9.**
  - Under R1, interference across ticks is lost and records diffuse.
  - The conveyor drift survives, because the index is a property of the tick.
- **Owner fork (Step 10).**
  - (A) Readable every tick ⇒ each step is a re-formation with the cut. Records behave like classical wanderers.
  - (B) Readable only when a new formation registers the position. Between registrations the possibilities move (R3) and interference survives.
  - The middle option (readable every tick, uncut) is inconsistent with no-signalling.
- **Real-physics read.** Interfering objects (electrons, molecules) cannot be readable moving records. They must be unrecorded possibilities (B). Readable macroscopic tracks behave like (A).
- **Budget note.** e3 (3 ticks, 64 setting sequences) peaked at 461 MB once, over the cap; it was replaced by smaller runs.
- **Coordinator check (EXACT by hand).**
  - P(b1≠a1) = sin²θ and P(b2≠α) = sin²(θ−φ).
  - At φ = π/4, θ ∈ {π/8, 3π/8}, P(b1≠b2) lies in [0, 0.293] vs [0.707, 1]. Gap ≥ 0.414 = √2 − 1.

## 23:30 A10 (staggered cycling ticks) LANDED → c8/A10/REPORT.md (+ t1–t11)

**Motion with one qubit per site: YES (EXACT).**
- The mechanism is cycled partial swaps G(θ) = exp(−iθ SWAP). These are the only number-conserving gates that commute with every on-site rotation (S1).
- A3's Step 10 is evaded because no single tick is covariant.
- The plain cycle is exactly covariant under (2Z)³⋊O: cube-centred rotations plus translations by 2. Unit translations hold up to relabelling which pairing comes first.
- Direction is carried by the sublattice, not the content.

**Plain cycle**
- It factorizes as U = W⊗W⊗W.
- Movers: eight one-way sheets along the body diagonals. No isotropic cone.

**An isotropic cone needs the Kogut–Susskind sign pattern (π flux).**
- Time-symmetric blocks make the cone isotropic at linear order (205 directions checked).
- Content: two Dirac cones (2L+2R Weyl), ν3 = 0. This is the 3D Hamiltonian staggered count.
- Every available mass gaps both copies equally.
- Covariance holds only up to re-phasing. That re-phasing is unavoidable (no T-invariant pattern carries π flux), but invisible to records that start from record configurations.

**Order effects**
- C3-symmetric cycles carry an energy-linear split ±sin²θ|q|²n_xn_yn_z, the A5 T6.4 class, which GRB bounds disfavour.
- Palindromic cycles remove the split but keep only 8 of the 24 rotations.

**Many-body**
- Finite depth, number-conserving, index 1 on every axis.
- With interacting records, odd rotations act only together with time reversal (schedule-word lemma).

**Admissibility**
- A "schedule-covariant" reading is a NAMED conditional.
- It brings five supplied choices: N1 global schedule phase, N2 word, N3 single angle, N4 sign pattern, N5 sublattice labelling.

**Coordinator verification (CHECKED; toys/verify_A10_1d.py, independent)**
- S1: the commutant of {u⊗u} has dimension 2 (span{1, SWAP}).
- S4: the 1D dispersion cos ω = cos θe cos θo − sin θe sin θo cos K matches exact eigenphases to 3.3e-15 for four (θe, θo) pairs, after removing the overall gate phase e^{i(θe+θo)}.

## 22:40 (real) A11 (one-way flows on record walls) LANDED → c8/A11/REPORT.md (+ check scripts)

**2D (supplied toy): YES, under the named reading SC (EXACT, CHECKED).**
- A handed 4-sub-step swap cycle (+x, +y, −x, −y on a two-sublattice pattern) is exactly the identity in the bulk.
- It carries exactly one qubit per cycle one way around EVERY recorded region, of any shape, including a single record. The direction is clockwise for the right-handed schedule. The mirror schedule is the inverse cycle and reverses it.
- The circulation is fixed by the bulk winding count (D4 loop-linking identity; D5).
- The net flow through any full line is zero, consistent with A1: this is circulation, not a conveyor.
- The cycle is covariant only up to cyclic relabelling of sub-steps (SC). Strictly covariant transfer layers do nothing (EXACT).

**3D (Z³, 24 site rotations): NO under SC (EXACT, D10).**
- The face C2 and the C3 rotations are commutators in O, so every sub-step must be invariant under the face C2 about every site. That means no transfers at all.
- Under a weaker flux-level reading:
  - the lattice Ampère law gives K = M×n̂ on periodic facets (EXACT; 12 slabs);
  - covariance forces M = 0, so no flow on periodic facets or axis hinges.
- Low-symmetry hinges are OPEN.
- 3D circulation is an AXIAL vector, so "proper rotations only" does not shelter it (unlike W3). Surface conveyors need a supplied direction.

**Consistency with A10 (coordinator).**
- A10's exact covariance of the plain cycle holds in the ONE-RECORD sector, with cube-centred rotations; unit translations are relabellings.
- In the many-body sector A10 itself finds no unit translation, and odd rotations only with time reversal (S7).
- A11's D10 concerns full transfer cycles on site contents (many-body) with site rotations. So there is no contradiction.

**Coordinator verification (CHECKED; toys/verify_A11_2d.py, independent).**
- On a 24×24 torus the bulk is the identity.
- Around an s×s locked block (s = 1–4), 2s+1 sites move as ONE orbit with winding −1 (right-handed) and +1 (mirror).
- No site farther than one site from the block moves.

## 22:55 (real) A13 (assembled model) LANDED → c8/A13/REPORT.md (+ toy1d_assembled.py, walks.py, timecount.py, pacing_noise.py, bands_weight.py)

**The assembled model, M1–M13**
- **Change:** strict pair steps G(θ) = cos θ − i sin θ·SWAP on a cycling round of pairings (A10).
- **Vacuum:** the aligned emptiness |n⟩^⊗, exactly quiet. The round fixes ONLY aligned states (EXACT).
- **Formation:**
  - chance c·⟨P_singlet⟩ on record-free pairs;
  - post-update lock odds;
  - √(1−F) no-record update;
  - menus set by records.
- **Records:** relocate by re-forming at the empty partner (option A), so they are readable every tick.
- **Interference:** stays in unrecorded possibilities (option B).
- **Optional held status (M13):** gives swallowing clumps.

**Consistency (EXACT by construction, CHECKED in 1D)**
- (C): branch law = |G|² chain to 4.4e-16.
- (L): one-site reach, strict cone.
- (NS): B's 4-tick history moves with A's choice by TV ≤ 3.2e-16.
  - Controls without the no-record update: 2.6e-3 to 3.3e-2.
  - Product rule: 2e-3 to 1.45e-2.
  - Cone control: 3.0e-3 once the cone reaches B.
- Quiet vacuum: rate exactly 0, with no breeding.
- One record per site; permanence as relocation (count preserved in every branch).

**Time (EXACT)**
- Distinct records are bounded (≤ 1−ρ0 per site).
- Formation events, relocations included, are unbounded where records move: rate s·u(1−u), CHECKED 0.07837 vs 0.07836.
- Readable accumulated time in a fixed region is ≤ |R|.
- The round tick is an opportunity, global or local only by convention. The EXPERIENCED tick is the local, event-paced formation count.
- Time stops in full AND in empty regions, and runs fastest at half filling.

**Two kinds of things**
- Readable records are persistent random walkers (dust): no momentum, E[x²] → sT/(1−s), no interference.
- Unrecorded possibilities are ballistic, interfere, and are Lorentz-like at low speed.
- Tracks are stationary fresh records formed from unrecorded movers.

**PACING FORK (new)**
- If the change advances every round, only record clocks slow: non-universal.
- If the change waits for local events, slowing is universal, but random pacing dephases heavy superpositions. Visibility is |1−p+pe^{iω}|^{2t}, giving t_coh ≈ ħ²/(M²c⁴τ_e).
- Coordinator arithmetic at τ_e = t_P:

| Object | t_coh |
|---|---|
| electron | 31 s |
| neutron | 9.3 μs |
| 100 amu | 0.93 ns |
| 25 kDa | 15 fs |

- Real interferometers are far longer (comparator), so event pacing needs ~1e9 noise suppression or sub-Planck steps.

**Other constraints**
- Formation scale c ≲ 1e-43 at Planck ticks for 1 s of interference (ARGUED).
- Failures: chirality doubled; β = ½, γ = 0; no waves; weakness unnatural; records carry no momentum.

**Owner decisions D1–D8**
1. May records move?
2. Readable every step?
3. Stepped round?
4. Which emptiness?
5. What time counts?
6. Does change wait for events?
7. Strict reach?
8. Held status?

**Budget note:** the first toy run peaked at 497 MB for ~5 s, replaced by a smaller run.

## 23:05 (real) A14 (spatial sector / light bending) LANDED → c8/A14/REPORT.md (+ g1d/w2d/s3d/d2d scripts)

**Event pacing alone (OR reading).** n = 1/N gives HALF the GR bending and delay: γ = 0 at every order (EXACT eikonal). Two caveats:
- It needs the ripple cone to sit at zero vacuum-relative quasi-energy. A10's cone sits at an offset relative to the all-0 reference, which gives colour dependence or repulsion.
- Random event timing adds noise.

**Static records as walls: FAIL.**
- Records pin, so ⟨a|h|a⟩ depends on content (EXACT lemma). That brings masses, colour dependence, and loss Γ/|δω| ≈ 1.2–2.6.
- Near a clump the long-range wall population is the wanderers, and they are DEPLETED. Ripples are therefore faster there: the wrong sign, and only O(u∞) in size.
- The crushed-ice shift −Cap₁·ρ (Cap₁ = 3.957) is CHECKED.
- New cross-constraint: if wanderers pin light-like ripples, the photon-mass bound needs u∞ ≲ 1e-47 to 1e-92 per Planck site.

**Idle sites as walls (AND reading): first-order SUCCESS as a named conditional.**
- The rule: a site with no event in its neighbourhood on a tick holds its possibilities. A two-site step then needs events at both ends in one tick.
- Transport goes as N² while one-site clocks go as N. So n = 1/N² = 1 − 2Φ + …, i.e. γ = 1. EXACT eikonal; CHECKED drift ratio AND/OR = 1.984.
- It NEEDS:
  - a GLOBAL coincidence tick (local N-paced ticks give γ = 0);
  - no one-ended steps;
  - dilute activity;
  - no triangles;
  - species with one-site rest energy and two-site motion (A10's masses are two-site, which does not fit).
- β stays ½ (EXACT, MF), so the perihelion comes out 7/6 of GR (Mercury fails).
- A fresh/spent exchange with a ratio clock would give β = 1, but no ingredient supplies it.

**Owner-relevant.** In this toy, the owner's "set tick" (a global beat) has a POSITIVE role: the coincidence window for AND gating, which is what gives full light bending.

**Coordinator check (EXACT by hand).** For n = N^{−k} with N = 1 − U, n − 1 ≈ kU, so the bending ratio AND/OR = 2 at first order. This matches the measured 1.984.

## 23:12 (real) A15 (local beats and moving records) LANDED → c8/A15/REPORT.md (+ seam/selftimed/rate/anglelapse scripts)

**Rigid local clocks.**
- Theorem A (EXACT): under the handshake rule, a bond whose two ends disagree in phase NEVER acts, for any angle or geometry.
- So every disagreement is a perfect mirror: each side evolves as if the other were recorded ("phantom lock", CHECKED as an exact permutation equality).
- In 2D A11 cycles the wall carries two counter-propagating channels with net 0.
- Transmission needs one of two things:
  - a second gate at the seam within one sub-step, which breaks the cone there (T 0.64–1.00);
  - unrecorded randomness, which destroys coherence (T = 2/9 at full swap).
- Rate differences:
  - commensurate 2:1 steps only: they refract, totally reflect half the fast band, and transmit 0.5000 at full swap (CHECKED);
  - smooth gradients become opaque stacks of walls (T 0.021 / 0.157).

**Waiting (self-timed) local clocks.**
- Seams heal: records move exactly as under one global beat (T = 1 − 2e-10).
- Theorem B (EXACT): rates lock, |c(x) − c(y)| ≤ 2p. No sustained rate differences, and a slow region throttles everything.
- Theorem C (EXACT): a waiting loop freezes the whole connected grid. Random initial phases deadlock in 40/40 runs (2D/3D).

**Event-paced, set by records.** C and NS hold; TV is 2.7e-16. Pacing by uncut possibilities signals (0.257, 0.096). The E1 variant stays ballistic; E2/E3 become diffusive.

**ANGLE LAPSE (S14, CHECKED).**
- Setup: one shared beat, with the gate angle (change per beat) set by records and varying in space.
- Smooth lapse ramps transmit 1.0000. Sharp steps transmit 0.984–0.992.
- θ_xy = θ0·N realizes A8's ΣN(x)h_x deterministically.

**Conclusion (ARGUED as a package).**
- Moving records need a beat that is SHARED in every readable respect (equal rates, no waiting loops), but no master clock.
- Neighbourhood-dependent time (gravity) must live in HOW MUCH CHANGE PER BEAT (set by records), not in HOW OFTEN the beat comes.
- Real physics: sustained redshift with no reflection of light at gradients contradicts any beat-rate lapse in these toys. The angle lapse survives.

**Coordinator note.**
- Theorem A logic checked by hand: each bond appears in exactly one layer per period, so phase-mismatched ends never coincide.
- The deterministic angle lapse also removes A13's random-pacing dephasing. A17 is examining this.

## 23:20 (real) A12 (quiet vacuum vs light) LANDED → c8/A12/REPORT.md (+ c1–c7 scripts)

**Single-tick results**
- Exactly zero is IMPOSSIBLE for any finite reach or window in the half-filled sea, because its marginals are full rank (lattice Reeh–Schlieder, EXACT).
- A9's R^-3 is INFRARED: it is the weight of states softer than 0.85/R. The best reach-R single-tick mode falls exponentially, ~e^{-4.6R} (CHECKED).

**Multi-tick windows: exponentially small IS possible**
- Instrument: time-ordered and energy-absorbing over T ticks (a one-site plus one-slot memory "register", comparable to Unruh–DeWitt/Glauber).
- Ceiling: ε ∝ e^{-2κT}, κ = arccosh(1/sin(α/2)). EXACT via Chebyshev/Bernstein–Walsh. Massless 1D: 2κ = 1.7627/tick, measured 1.7617.
- Soft excitations obey time–energy uncertainty, ε ≈ e^{-cET} with c ≈ 1–2. Power laws come only from abrupt windows.
- Budget: 5–40 cycles of the softest recorded excitation give ε ≤ 1e-61 to 1e-123.

**The catch: memory**
- A strict-cone window needs a PER-SITE MEMORY, which the axioms do not supply (an import).
- A memoryless reach-T weight is influenced from outside the past cone (CHECKED ΔP ≤ 1.07e-3).
- Without memory there is no filtering gain.

**Consequences**
- "Tick = formation rate" cannot mean the vacuum's own rate.
- The z=1 photon survives A9's z≥2 obstruction (the window is not frustration-free), at the price of a tiny nonzero rate plus memory.
- Distant light arrives coherent (VLBI/CMB), so free excitations far from matter must essentially never be recorded. That favours formation gated by existing recorded neighbours ("only when the neighbourhood calls for it").

**Budget note:** one run reached 312 MB for 1.1 s; rerun at 183 MB.

**Coordinator check (EXACT arithmetic)**
- m=0: 2·arccosh(√2) = 1.7627.
- m=0.3: 2·arccosh(1/sin((π/2−0.3)/2)) = 2.2244.
- Both match the report.

## 23:45 (real) A16 HOSTILE REVIEW LANDED → c8/A16/REVIEW.md. CORRECTIONS (these supersede earlier LOG wording)

**C1. A3, "smooth change leaks" is OVERBROAD.**
- What fails is a time-independent, homogeneous, star-local generator run for a whole tick: Campaign 7 sentence 2 as written. Uniform d=1 hopping fails for every τ > 0.
- A smooth generator on ONE partner set per tick stays range-1. A10's exp(−iθ SWAP) layers are an example.
- So Q2's "continuously evolving" is NOT forced to be re-read.
- "Lone records can't move" holds only for per-tick covariant, homogeneous, number-conserving ticks. Compass-type (non-conserving) covariant gates are not covered.

**C2. A7: "under every rule" is for one hand-built instance.**
- Correct statement: "there are linked states for which every rule signals".
- Option A IS the axiom-literal reading (a record "locks" = cut). Present it that way.
- Option B needs explicit text: any formation whose odds or menu depend on a guided record's place must cut that record. Without it, Q7 plus guided records re-open signalling.

**C3. A1/A2 scope: SINGLE-PARTICLE, translation-invariant steps.**
- "Two independent proofs" is wrong: both rest on the same algebraic K-theory (stable and unstable forms). Only A2 D5 is self-contained.
- Faint reach can tip the balance only for movers with ≥2 internal states.
- Narrowing the Campaign-7 flag must say "single-particle".

**C4. A9.**
- "Must be tr(Fρ)" holds IF no-signalling, in the supplied sharing model. H2 steering needs Campaign 7 sentences 1, 3 and 4, which are NOT adopted.
- **The coordinator's Q7 "correction" FAILS as worded.** Under linear instruments the support of the odds varies with unrecorded neighbours, as Admissibility + Q1 require. What signals is setting the menu's FRAME (which possibilities can be locked) as a NONLINEAR function of unrecorded possibilities.
- Correct reading: "Recorded neighbours may set which possibilities are on offer; unrecorded possibilities shape the odds over them only as a fixed weighted average."
- Record-set frames are safe only for records cut to agree with their site.

**C5. A4/A6/A8.**
- Bounded formation time needs a translation-invariant start.
- The move clock is stored in NO record: readable accumulated time ≤ |R|.
- "Detailed balance ⇒ flat" is shown only for neighbourhood-blind hops.
- β = ½ is a dilute mean-field result.
- Missing from the draft: γ = 0, and the establishment limit (~5e-5 m at Planck steps).

**C6. A5.**
- Out-of-step ticks ARE readable: mismatched seams are mirror walls (A15).
- The tie fraction p/(2−p) needs constant p.
- Relativity is secured only in the 1D toy. In 3D:
  - strictly covariant spin-½ walks have zero speed (A1 D18);
  - isotropic cones need KS signs, which privilege a basis, or C3 words, which split linearly (GRB-disfavoured).

**C7. A10/A13 "schedule-covariant" reading: FAILS** (A16 checks rerun by coordinator, reproduced).
- Single record: T_x = forward restart 1 and T_y = restart 3 (2.8e-17). But T_xT_y, (1,1,0), T_xT_yT_z and site-centred C2z match only the REVERSED round (forward residual 0.15). The relabellings do not form a group action.
- Two records:
  - quarter turns need reversed restarts plus a (1,1,1) shift (best TV 0.028 forward, 0 reversed+shift);
  - odd translations are not realized forward or reversed (worst best-TV 0.04–0.39 forward, 0.07–0.46 reversed).
  - So sublattices become READABLE, which conflicts with Lattice "No site is privileged", unless the round counts as supplied lattice structure.
- A13's model also has:
  - a fixed lock axis, which privileges a possibility;
  - all records locking the same content.
  - "The round fixes only aligned states" is overclaimed: the aligned family follows from quietness, not from the round.

**C8. A13 pacing fork.** M² scaling assumes the whole object shares one random pace per arm. Independent constituents give Σm_i², i.e. longer coherence. The fork is not binary: A15's angle lapse avoids it. Event pacing means no change at all where there are no records.

**C9. Jam evaporation (coordinator's own data).**
- Side 4 lost 0.27/tick (64 records, half-life 120); side 8 lost 0.24/tick (512 records, half-life 1087).
- So loss rates are about equal: lifetime ∝ N, not "big ones lose faster".
- The draft's "opposite to Hawking" framing must change to: "8× bigger lasted ~9× longer; nothing like a lifetime ∝ mass³".

**C10. All "must"s about formation and instruments rest on the unadopted Campaign 7 sentences 1, 3 and 4 (and no-signalling).** Read every such "must" as "if those hold".

## 00:05 (real) A18 (shared-beat GR package P1–P4) LANDED → c8/A18/REPORT.md (+ pn_rays.py, lapse1d.py, estimator.py, noise3d.py)

**What the package achieves (EXACT eikonal; CHECKED)**
- The ingredients:
  - a shared beat;
  - change per beat set by records, with one-site phases ∝ N and two-site angles ∝ N_xN_y;
  - one-site rest energies;
  - an exponential lapse N = e^{−U}.
- Result: EXACTLY the exponential (Yilmaz-type) metric ds² = −e^{−2U}dt² + e^{2U}dx². That gives γ = β = 1, i.e. 1PN light bending (4M/b), Shapiro delay and perihelion (factor 1.000000).
- Species with one-site masses redshift and fall universally (0.4% at σ = 200). Two-site masses fall about 2× faster, an EP violation at order one.
- Smooth gradients do not reflect (≤ 5e-9).

**What must be supplied**
- θ0 ≲ 6e-3, because γ_eff = 2θ0·cotθ0 − 1. Light then runs at ≲ 1% of the lattice cone.
- The cone must sit at the vacuum's quasi-energy.
- A10's time-symmetric word.
- Formation odds ∝ N.
- UNPACED wanderers. Paced wanderers give β = 1/4 or 0, so the carrier of gravity runs on absolute time.
- Dimension-based weights for every other term (D7). Gauge plaquettes weighted by site count would give γ = 2 for photons.

**γ and β are DIALLED IN, not derived**
- γ = b/a − 1, which needs the product composition b = 2a.
- β = (1 + FF''/F'²)/2, which needs F exponential.

**Nearest-neighbour versions fail (EXACT)**
- A finite m-site estimator gives a polynomial pace. Exponential response then yields β = 1 − 1/(2m) = 11/12 for 6 neighbours, so Mercury comes out at 44.2″ vs 42.98″.
- Shot noise needs an averaging radius R ≳ 1e9/u∞.

**Beyond 1PN**
- 2PN bending 4π(M/b)² vs 15π/4.
- No horizon (N ≥ 1/e).
- Shadow +4.6%.
- NO gravitational waves.
- NO frame dragging (g0i ≡ 0).
- **MOVING SOURCES CARRY ONLY A WAKE (D23):** upstream screening beyond D/v ~ 1e-33 m. A moving Earth would hold no Moon. This sinks the diffusive-carrier mechanism of A6/A8 for any moving source; a WAVE carrier is needed.

**Honest assessment:** a proof of possibility for static weak-field geometry, with the two GR numbers dialled in. It is not a derivation, and it fails waves, frame dragging and moving bodies.

**Coordinator check (EXACT by hand)**
- PPN: U_N = aU and g_ij = 1 + 2(b−a)U give γ = b/a − 1.
- Perihelion factor at β = 11/12: (4 − 11/12)/3 = 1.0278, giving 44.17″.

## 00:45 (real) A17 (pacing noise vs universality) LANDED → c8/A17/REPORT.md (+ z3_floor, torus_mc, dirac_pacing, predvar_check, phys_numbers, rotor_scaling)

**Redshift vs noise**
- The redshift difference between branches is a fixed, run-independent phase (COW-type). It costs NO visibility (EXACT; CHECKED |O| ≥ 0.9994).
- Dephasing comes only from SHOT NOISE in what the beat counts.
- Per-site or NN beats are effectively independent at separated places, so A13's estimate STANDS. It is optimistic by ≥ 11×: 80 ps at 100 amu, u = ½.

**Theorem 2, capacity floor (EXACT for linear drives)**
- S_N(0) ≥ 2(1−u)/(uκ·Cap(K)).
- The noise falls with capacity (∝ radius), not with volume.
- Time windows do not help, because the zero-frequency gain is 1.
- NN star at u = ½: ≥ 2.07 ticks.

**Stronger falsifier**
- A per-site beat scrambles every massive particle within each branch (EXACT 2nd-order toy, CHECKED 0.05975 vs 0.05989): an electron every ~3 s at u = ½.
- Matter would not persist.

**Requirements from experiment**
- Interferometers need a smooth average over R ≈ 4e9 (Rb) to 1.5e12 (25 kDa) sites at u = ½, up to 1.5e18 at u = 1e-6.
- No NN record rule can build this:
  - L1: same-tick reading breaks the cone;
  - L2: the snapshot holds no history;
  - L3: record relays carry the same floor.

**Way out (ARGUED, not constructed)**
- A smooth beat FIELD carried by the shared possibilities, set by record activity, with wave-like transport.
- This refines D6 from "the change waits for events" to "the change advances by a smooth dose set by record activity".
- It matches the coordinator's gravity synthesis: wave-carrying gravity must be a collective field of the possibilities.

**Other results**
- Ballistic carriers are quiet but give a 1/r² shadow.
- Rotor (deterministic) relocation gives bounded variance (Var 31–33 flat in T), but needs a mutable per-site pointer that is not a record.
- Skip pacing fixes "no change in the void" but is too noisy.

**Coordinator check (EXACT arithmetic).** Floor at u = ½, κ = 1/12, Cap = 11.62: 2.065 ticks.

## 00:20 (real) A19 (tracks and inertia) LANDED → c8/A19/REPORT.md (+ core1d, exact_sharp, mc_grid, mediated*, track3d)

**Sharp (one-site) registration: NO inertia (EXACT).**
- Each record resets the mover completely (Markov). k0 is forgotten after the first record.
- Only the sublattice/direction bit survives, with probability 1 − sin(m)/2 per record.
- Momentum is spread over the whole zone, so a slow massive mover becomes a near-light-speed zigzag.
- Zeno-type freezing appears only for lattice-heavy movers.
- Direct records formed from the mover's own neighbourhood are always star-sharp (R1, EXACT). That includes A13's c·P_singlet. So A13's model, as written, has no inertia for directly registered massive movers.

**Coarse registration (cut width σ ≫ ħ/p): NEWTON'S FIRST LAW EMERGES.**
- Mean momentum is conserved (EXACT).
- The track runs at v(k0) (CHECKED ≤ 0.011).
- Direction persists for ~4(σp/ħ)² records.
- The optimal rate gives a standard-quantum-limit precision δv ≈ √(ħ/MT) (CHECKED within ~25%).
- Sliding unsharp cuts heat but never freeze. Only fixed pixel partitions freeze slow movers.
- Recorded sites act as traps: a frozen mover stays frozen at high rate (refutes the agent's own prior).

**Mediated records give coarse cuts while keeping "a record locks exactly one possibility" (R2, EXACT structure; CHECKED).**
- The record forms on a probe that bumped the mover. The mover feels a broad partial cut plus recoil.
- Mott-track-like (comparator).

**Time-umklapp (R3, CHECKED).**
- Contact collisions put an O(1) share (~50%) of the reflected weight into the time-doubled channel (K → K+π).
- That is a falsifier unless it is suppressed or shown to be invisible.

**3D (A10 signed cycle, L=48).** Coarse cuts keep the direction (speed 1.01, cos 0.90–0.93). Sharp cuts erase it.

**Physical scales (ARGUED)**
- Heating bound: direct sharp registration of matter < 1e-90 per nucleon per Planck tick.
- Coarseness needed: about 0.2 nm for a 1 eV electron.
- A thrown ball passes easily.

**Coordinator check (EXACT numerics).** ⟨v²⟩ over the zone = 1 − sin m to 6 digits:

| m | ⟨v²⟩ | 1 − sin m |
|---|---|---|
| 0.15 | 0.850562 | 0.850562 |
| 0.6 | 0.435358 | 0.435358 |
| 1.4 | 0.014550 | 0.014550 |

## 00:40 (real) A20 (covariant motion, compass gates) LANDED → c8/A20/REPORT.md (+ t1–t9, cliff_* scripts)

**THEOREM N (EXACT).** Every nearest-neighbour (reach-1) REVERSIBLE tick on Z³ qubits that commutes with the soldered rotations about every site is the IDENTITY.
- The proof uses support algebras. It needs no number conservation and no Clifford structure, so it covers compass gates and every other gate.
- This closes the gap A16 flagged in A3 Step 10.
- Consequence: under strict I2 (NN reach), per-tick soldered covariance, one qubit per site and reversibility, NOTHING moves.

**Gate products**
- Compass gates commute up to phase only at θ ∈ (π/2)Z.
- Commuting ticks never transport.
- The star family S_x is covariant but static.

**Clifford ticks**
- Classified exactly: M = 1 + P·N0·adj(P).
- A Clifford tick moves only if det N0 ≠ 0, and then its reach is ≥ 4.
- A reach-4 covariant mover exists: U = A·B with star and face gates. It is exactly covariant with signs (24×3 checks, 0 failures), has no sublattice and no schedule, and has a light cone of 4t.
- BUT what moves is a spreading web of links (a fractal scrambler):
  - no gliders;
  - no invariant stabilizer vacuum survives a moving tick.
- Non-Clifford ticks at reach 2–3 are OPEN.

**Minimal relaxations**
1. longer reach;
2. supplied sublattice (A10; loses covariance);
3. quasi-locality;
4. statistical covariance;
5. multi-qubit sites;
6. IRREVERSIBLE covariant moves (A1 D23 lock-and-move).

**Coordinator synthesis plus verification (CHECKED; toys/verify_lock_and_move.py).**
- Theorem N covers REVERSIBLE ticks only.
- A7 already forces readable moving records to RE-FORM at each step, which is irreversible.
- The A1 D23 lock-and-move channel K_v = 3^{-1/2} P_v ⊗ T_v (six axis directions) has three properties:
  - it is complete (Σ P_v/3 = 1);
  - it is exactly covariant under all 24 soldered proper rotations;
  - it gives a persistent walk: from content +x it continues with 1/3, turns with 2/3, and never reverses.
- This is the clean covariant one-site move: the record re-forms next door and its new content points the way it stepped (content-locked, handed per A1 D22).
- Cost: a six-direction (non-orthogonal) menu, which is a named conditional, not fixed by the axioms.

## 00:55 (real) A21 SECOND HOSTILE REVIEW LANDED → c8/A21/REVIEW.md (A21 resumed to review A20 too). CORRECTIONS C11–C20 (these supersede earlier wording)

**C11. "Pace cannot be set by the shared possibilities" FAILS as worded.**
- A21's r2 check, rerun by the coordinator, compares two rules:

| Rule | TV |
|---|---|
| FIXED coupling: exp(−iθ\|1⟩⟨1\|_{a1} ⊗ SWAP_{a2a3}), a possibility sets the pace coherently | 2.7e-16 (no signal) |
| Nonlinear dial (A15) | 6.9e-2 |

- Only NONLINEAR state-set dials signal. So the field route (gravity as a collective ripple of the possibilities with FIXED dynamics) is consistent, not self-contradictory.

**C12. "Every record-based version gives only a wake" holds only for DIFFUSING carriers.**
- Ballistic carriers make no wake but give a 1/r² shadow.
- Persistence is capped by sub-mm inverse-square tests.
- Phrase the field route as "the candidate left open", not "would have to be".

**C13. Repo gravity lane (verified on origin/main).**
- Unaudited field-type graviton notes exist:
  - REGGE_SECOND_VARIATION … NATIVE_LINEARISED_GRAVITON (2026-09-03);
  - UNIVERSAL_GR_GRAVITON_DISPERSION_LORENTZ_ISOTROPY (06-08);
  - TWO_TT_GRAVITON_POLARISATIONS … PI_FLUX_SEA (09-04).
- Several rest on the half-filled/π-flux sea that point 6 puts in doubt.
- Cite these as unaudited, with that caveat.

**C14. Vacuum figure.**
- "5 per million ticks" is per UNIT formation strength. The correct statement is a RATIO: false records ≥ 5e-6 × true recordings (best case); energy rule ~1/80.
- At Planck ticks:
  - a rule strong enough to record a particle within ~1 s fills empty space within days (energy rule: ~80 s);
  - a rule weak enough to keep space clear for the universe's age needs ~70,000 years to record anything.

**C15. A12 scope and memory.**
- The lattice Reeh–Schlieder result is for record-ignoring, finite-reach/window weights. It assumes a graded (fermion-bilinear) product, which the axioms do not fix.
- The ceiling e^{−2κT} is per (T + spatial reach), for a fixed finite seed.
- Per-site memory recurs in A12, A15 S0 and A17 (accumulator/rotor). Present it as ONE owner decision.
- A memory made of matter is not excluded.
- "Records next to records" is one of two ways to keep light unrecorded; a light-blind rule is the other. Its cost: an empty grid never starts.

**C16. A14.**
- AND gating's γ = 1 holds in the averaged small-dose limit only. Real events bring the jitter floor (A17).
- Light speed ∝ wanderer activity², so light stops in voids.
- "Global" should read "shared" (in-step local ticks suffice).
- The photon-mass cross-constraint u∞ ≲ 1e-47 to 1e-92 must be stated.

**C17. A15 / A17.**
- A deterministic per-site record-set angle STILL jitters (A17 D1), which overturns A16 C8's "angle lapse avoids random pacing".
- Only a smooth wide average escapes.
- Formation odds per tick must carry the same factor N.

**C18. A18 costs to state.**
- The γ = β = 1 match holds for TWO-SITE light. Four-site loop light gets γ = 2 (1.5× too much bending) unless dimension-based weights are added.
- Light runs at < 1% of the grid limit.
- The wanderers must be unslowed (an absolute clock).
- With u∞ ≲ 1e-47, the smoothing radius reaches ~50 kpc.
- The NN β = 11/12 holds for one specific exponential rule; tuned rules can hit β = 1. The decisive NN failure is JITTER, not β.

**C19. A19.**
- In 1D the direction bit partly survives (1 − sin m/2). It is erased in 3D.
- A13's c·P_singlet is star-sharp, so A13's model as written gives massive movers NO inertia; it needs mediated records.
- The time-umklapp share falls as m², so the real-world size is not computed. It is a POTENTIAL falsifier.

**C20. Draft.**
- Use "tick" throughout.
- Restore A16's Q7 condition: menus may be set only by records cut to agree with their site.
- Add a bottom line at the top.
- Reduce jargon.
- Add decisions 9 (memory), 10 (pacing composition, and whether the carriers are slowed) and 11 (direct records lose inertia).

## 01:10 (real) A23 (field-route map) LANDED → c8/A23/REPORT.md (+ spin2_cubic_check.py)

**What any field route gets**
- No signalling: a FIXED coupling (EXACT).
- No wakes: the z=1 wave carrier makes a moving source's field the boosted static field (EXACT, continuum).
- 1/r from gaplessness alone, with no sink needed (EXACT).
- Noise ∝ G², so gravity's weakness reads as "matter is light on the grid", m_p/m_P = 7.7e-20 (ARGUED).
- Momentum lives in unrecorded possibilities.

**Scalar branch: FAILS.**
- γ = −1 (conformal); γ = 1 only with a preferred frame (stratified).
- No frame dragging.
- Wrong waves: one scalar polarization.

**Tensor branch (spin-2): the grid's symmetry FORCES Einstein's linear gravity.**
- Cubic covariance plus linearized gauge invariance leave exactly ONE O(k²) potential, the linearized Einstein–Hilbert form (CHECKED 1e-15).
- Preserving the Hamiltonian constraint (named conditional F4) forces GR's kinetic weights (−½, 1, 1): isotropy, no birefringence, no extra scalar (CHECKED; EXACT by hand). Other weights give a birefringent wave plus a ghost or unstable scalar.
- A local reversible leapfrog ("Yee for spin-2") tick:
  - preserves both constraints;
  - z = 1;
  - phases < π, so no time doubler, for τ < 1/√3;
  - exactly 2 polarizations (CHECKED, symbol level).
- γ = 1 when the lapse paces the field's own change (CHECKED 1.000000).
- Universality is FORCED by source conservation (EXACT; Weinberg comparator).
- 4D: hypercubic B4 plus gauge invariance give 4D linearized EH. The owner-approved kinetic-isotropy primitive, EXTENDED to a gauge-invariant field, would supply GR's kinetic weights. That would be an owner decision.

**New costs**
- **(f) The source must be conserved energy-momentum.** So forming a record must not change energy, or a permanent "ghost source" remains. One-site locks of moving matter inject band-scale energy, so locks must be energy-gentle (mediated/coarse). This is the same direction A19 reached from inertia.
- **(g) Payload:** how one qubit per site hosts the field. OPEN.
- **β = 1 needs second order.** OPEN; comparators HKT/Deser.

**Ranked decisive tests**
1. energy-gentle locks;
2. payload;
3. real-space covariant Yee-for-spin-2;
4. matter coupling;
5. second order.

**Repo cross-reference (all UNAUDITED at e485eab6b0)**
- The Regge "linearised graviton" note; its corrected title is "Finite spectra and metric projections of a supplied cubic-Coxeter Regge Hessian".
- The U1 Yee leapfrog tick, which is the template.
- The spatial-half (2,1) weight note, which is A18's product.
- The TT polarisation/KS-sea note: shear needs a frame.
- The ring photon: quiet only at RK.

**Coordinator verification**
- Reran spin2_cubic_check.py: C1 gives 3 kinetic forms; C2 gives 9 → 1 gauge-invariant; C3 gives (−0.5, 1, 1); C5 gives 9 → 1; C7 gives γ = 1.000000.
- Independent hand check: the 3D DeWitt kinetic term π_ijπ_ij − ½(tr π)² has weights (1 − 3/2, 1, 1) = (−½, 1, 1) on (A1, E, T2) with normalized trace. That matches C3.
