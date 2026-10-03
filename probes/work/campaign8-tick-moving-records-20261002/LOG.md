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
