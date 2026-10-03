# A28 report: gated formation under Option R

Scratch directory: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A28/`. It holds scripts `c1`–`c5`, outputs `out_*.txt`, timings `time_*.txt` and `run.sh`. There were no git operations and no repo edits. Every model is a supplied toy. Gated formation is a named conditional (a candidate), not framework content.

## 1. Question

**Candidate G (gated formation).** F_x = Σ_R |R⟩⟨R| ⊗ F^(R), where R is the pattern of recorded neighbours:
- F^(∅) = 0: no formation without a recorded neighbour;
- for R ≠ ∅, F^(R) is a linear local weight (A9 Theorem 1), which may depend on the recorded contents.

G is combined with Option R (A27): smooth compressed change, SW steps and CL claims.

Does G deliver:
- (a) empty space that is exactly quiet for any vacuum, including z = 1 seas;
- (b) no-signalling and A9's linear-instrument constraints;
- (c) no freezing;
- (d) distant light arriving unrecorded?

At what cost?

## 2. Answer

**Conditional.** Gating does everything asked of it in voids, but it does not reach the edges of recorded regions, and freezing is decided by a separate choice.

- **(a) [EXACT]** A site with no recorded neighbour never forms a record, whatever its possibilities hold. The minimal no-record update there is the identity, so a void's possibilities evolve by the smooth change alone. A12's lattice Reeh–Schlieder result does not apply, because its weights ignore records.
  - The same positivity bound reappears one site away. Next to any record, a full-rank sea (z = 1 seas included) is recorded at a positive rate by every nonzero gated weight [EXACT; full rank next to walls CHECKED in 1D and 3D]. So records breed into such a sea.
- **(b) [EXACT; CHECKED]** Gating is classical control by records, and Option R keeps every record cut to agree with its site (CHECKED to 1.05e-15).
  - A 3-tick package toy gives TV ≤ 4.1e-16.
  - A record place set without the cut signals: TV ≥ (c/z)p/4 [EXACT].
  - Gating on the records present at the start of the tick gives a strict record cone of one site per tick [EXACT].
- **(c) [CHECKED toys; EXACT dark sector]** Gating alone does not prevent freezing behind fronts. Three outcomes appear in the toys:
  - open enclosure: the toy universe fills and freezes;
  - blind enclosure (lone-hole odds p0 = 0): it thins;
  - a weight that vanishes on a quiet (aligned) emptiness, with record contents on its axis: formation stops once the excitations are used up, and records keep moving at a steady rate forever.
- **(d) [EXACT in voids; ARGUED near matter]** Near matter:
  - the intergalactic medium and galaxies impose nothing for records up to nucleon size;
  - dense transparent media do impose a limit if records are extended: κ ≲ 4e-6 per contact tick for nucleon-sized recorded balls.

**Costs.**
- An empty world never starts, so a preparation is required [EXACT].
- For a full-rank sea, the edge floor has three consequences:
  - records breed into the sea;
  - A6's screening turns into anti-screening;
  - each sharp edge record injects about J of energy (CHECKED). With Planck-scale J (ARGUED), A19's heating bound pushes the formation strength below about 1e-86 per tick. So a z = 1 sea still needs a quiet emptiness or energy-absorbing windows at matter's edges.
- Q4 must be read as conditional on formation, and under gating it never applies to an actual formation.
- The enclosure rule and the start-of-tick rule are further named choices.

## 3. Derivation

**Step 0. Setup (supplied package).** Each tick:
1. Every empty site x whose recorded-neighbour pattern R_x is non-empty at the start of the tick applies one joint instrument (A27 open edge 1) with outcomes:
   - form and lock k, effect E_k = √F^(R) P_k √F^(R), with P_k in a menu set by records (Q7);
   - claim record i, Kraus √(c/z)·√W_i, followed later by a SWAP (SW);
   - nothing, Kraus √(1 − F − Σ(c/z)W_i).
2. Sites with R_x = ∅ apply the identity.
3. CL resolves contested claims uniformly at random, then the SWAPs are applied.
4. The smooth change e^{−i Q_R H Q_R τ} acts.

**Step 1. Record reach [EXACT].**
- Claim: V_{t+1} ⊆ V_t ∪ ∂V_t, where V_t is the recorded set.
- Proof: a formation needs a recorded neighbour at the start of the tick, and a step moves a record one site.
- Corollaries:
  - V_0 = ∅ ⇒ V_t = ∅ for all t.
  - Every record at tick t lies within distance t of the preparation, and descends from it through a chain of gating and steps.
- Sub-rule needed:
  - If formation were gated by post-step positions, the reach would be 2 sites per tick.
  - If gating were updated inside a tick, chains of formations could cross any distance in one tick, with odds ∏F.
  - So "gate on the records present at the start of the tick" is a named choice.

**Step 2. Void quietness and void transparency [EXACT].**
- If dist(x, V_t) ≥ 2, then P(form at x) = 0 for every ρ, x makes no claims, and its minimal no-record update is √(1 − 0) = 1.
- A9 Theorem 2(c) is satisfied: the no-record branch has weight 1, so no quadratic term arises.
- Sites at distance ≥ 3 are touched by no instrument at all.
- So in voids the tick is the identity and the possibilities evolve by e^{−iHτ}. Light in voids is never recorded and never disturbed by the record machinery.
- **Comparison (ARGUED arithmetic, `c4`).** An ungated sharp one-tick rule on a full-rank sea injects 0.21–0.85 J per false record (Step 7). Keeping the injected energy below the observed dark-energy density over the age of the universe would need ε_void ≲ 1.7e-184 to 6.8e-184 per site per tick. That is about 120 orders below A12/A4's freezing figure of 1.2e-61. Gating makes the void rate exactly 0.

**Step 3. Where A12's Reeh–Schlieder result stands.**
- (a) [EXACT] A9 Theorem 1 leaves the dependence on records free, so F^(∅) = 0 is allowed; A9 §3.3 item 4 is its state-independent special case.
  - The zero weight sits at the apex of A9's quiet cone 0 ≤ F ≤ Π_ker for every vacuum.
  - A12's theorem, as scoped by C15, covers record-ignoring weights; A21 already listed gating as an exemption.
- (b) [EXACT] At an edge, P(form | R) = tr(F^(R)ρ_U) ≥ λ_min(ρ_U)·tr F^(R), where U is the unrecorded part of the star.
- (c) Is ρ_U full rank next to a record? Under Option R a record is a wall (A27 Step 1a); for free fermions a locked site is a hard (Dirichlet) wall.
  - [EXACT] For a free-fermion sea with a planar wall, a finitely supported v with Pv = v or Pv = 0 has a sine/Fourier transform that is a trigonometric polynomial vanishing on an open set, so v = 0. Hence every restricted eigenvalue lies in (0,1).
  - [CHECKED, `c2`]

    | Sea | Unrecorded star next to the wall | Smallest many-body marginal eigenvalue | Bulk star for contrast | Size check |
    |---|---|---|---|---|
    | 1D half-filled chain (the 1D massless Dirac sea) | 2 sites; ν = {0.0756, 0.9244} | 5.71e-3 | 3-site star: 1.24e-3 | stable for N = 200–800 |
    | 3D simple-cubic, planar wall | 6 sites; ν ∈ [0.092, 0.908] | 5.27e-4 | 7-site star: 2.58e-4 | stable for L = 16 → 24 |

  - [ARGUED] interacting seas, and the staggered sea with a wall.
- (d) [EXACT] Consequence: with a full-rank sea, a gated rule that records anything next to records also records the emptiness there, at rate ≥ λ_min·tr F^(R). A9's quiet-vacuum criterion (rank deficiency) does not go away; it moves to the edge.

**Step 4. No-signalling.**
- (a) [EXACT] The gate is a function of the record pattern on the star, which is a classical fact. Each step is a classically controlled local instrument.
  - Summing a distant region's unread outcomes gives a channel that commutes with the local backward cone (A13 S3; A9 Theorem 2(e); comparator: Beckman–Gottesman–Nielsen–Preskill 2001).
  - A9 Theorem 2(a)–(c) hold pattern by pattern. This is Theorem 2(d)'s "dependence on records is free", applied to the chance.
  - Gating adds no reach beyond Option R's own Lieb–Robinson tails (A27 Step 9).
- (b) [EXACT, Option R] Records are cut to agree with their sites:
  - formation leaves the site in the locked menu vector;
  - SWAP·√W carries the pure content to the claimant's site.

  So the A16 C2/C4 and A21 condition holds.
- (c) [CHECKED, `c1`/`c1b`]

  | Item | Result |
  |---|---|
  | Setup | 6 seeds; 3 ticks; 294 histories; distant b gated by a record at d; three distant choices: no record, Z menu, X menu |
  | Record-history TV across the choices | ≤ 4.1e-16 |
  | Total probability | within 2e-15 of 1 |
  | Recorded sites vs their content (981 branches) | worst deviation 1.05e-15 |
  | Formations without a start-of-tick recorded neighbour | 0 of 786 |
  | New records left with no recorded neighbour (their gating record stepped away the same tick) | 96 of 786; harmless |

- (d) [EXACT] Contrast: a record place set without the cut, i.e. step odds (c/z)⟨W⟩ taken from the snapshot with no √W.
  - Take a GHZ state on (y, x, b), W = |0⟩⟨0|_y and F = p|1⟩⟨1|_x.
  - P(step, then form) = (c/z)p/4 if b has no record, and 0 if b holds a Z record. So TV ≥ (c/z)p/4, which is 0.25 at c/z = p = 1.
  - The random toy gives 1.2e-3 to 8.9e-3.

**Step 5. Fronts, freezing, thinning, a living state.**
- (a) [EXACT] An enclosed hole's gate is open, so p0 = tr(F^(R_full)ρ_hole). A4's criterion then applies:
  - p0 > 0 ⇒ freezing;
  - p0 = 0 with steps ⇒ thinning (mean field).
- (b) [EXACT positivity] For a full-rank sea, p0 ≥ λ_min(ρ_hole)·tr F^(R_full) > 0 unless F^(R_full) = 0. That the hole's possibility stays mixed through its earlier links is ARGUED.
  - Weights that act only on pairs of unrecorded sites (weight B) have F^(R_full) = 0 automatically [EXACT].
- (c) [CHECKED, `c3`] 2D torus, L = 128, c_m = 0.4, ε = 0.01, p_e = 0.5, records act as walls for excitations.

  | Variant | Formation odds at a gate-open site | Outcome |
  |---|---|---|
  | V0, ungated control | ε everywhere | Full by t ≈ 1200; frozen from 1500 |
  | V1, gated sea, open enclosure | ε (p0 = ε) | Front from a disc; full at 1500; no events from 1800. From 45 sparse seeds: full by 1200 |
  | V2, gated sea, blind enclosure | ε if not enclosed | Thinning: holes 356 → 34 over t = 2000–20000; t·N_holes ≈ 5.4e5–6.8e5 against a mean-field 4.1e5; events per site per tick 2.3e-2 → 8.8e-4 |
  | V3, gated quiet | p_e on excitations only | 197 + 834 → 1031 records; no formation after t ≈ 2000; steps steady at 2.05e-2 events per site per tick (four digits, t = 4000–20000); about 90% of sites active in every 200-tick window. Sparse seeds: 45 + 820 = 865, then steady |
  | V4, V3 plus an edge floor ε | p_e on excitations + ε if not enclosed | Invades: 98.8% full at t = 3000, then thins |
  | V5, V3 plus excitation supply | as V3, with excitations added | Keeps accreting toward full (98.3% at t = 20000) |

  - Front advance in V1: 0.086 sites per tick, against the Fisher–KPP estimate 2√(Dr) = 0.12 (D = 0.086, r = 4ε) [ARGUED].
  - Under blind steps, the V3 disc dissolves into a record gas.

**Step 6. The quiet class's dark sector [EXACT; CHECKED].**
- Let D = {unrecorded sites in |n⟩; records with contents ±n}.
- Under these conditions, D is invariant and F annihilates it, so nothing ever forms:
  - weight B, F = c Σ_{unrecorded z} P_singlet(x,z)/2;
  - the compressed change, whose record fields |r⟩⟨r| are diagonal in the n basis;
  - SW-blind steps;
  - null updates.
- `c5` (6-site ring, 6 ticks), P(any formation within 6 ticks):

  | Emptiness | Weight | r = n | r = −n | r = \|+⟩ (off axis) |
  |---|---|---|---|---|
  | aligned | B | 0 | 8.9e-16 | 6.6e-2 |
  | aligned | A | 0 | 0.72 | 0.43 |
  | random entangled | B | 0.40 | 0.39 | 0.39 |
  | random entangled | A | 0.66 | 0.66 | 0.61 |

- Readings:
  - an off-axis record's field excites the emptiness (A27 Step 4), and the open gate then records it: breeding;
  - content-dependent weight A gives a halo around a −n record (A9 §3.7g).

**Step 7. Costs at the edge of a full-rank sea.**
- (a) Breeding: each record nucleates new records at a rate ≥ z·λ_min·‖F‖ per tick; with steps, Fisher–KPP fronts (V1).
- (b) [ARGUED via A6 §3.9] f0 = 0 holds exactly, but A6's carriers are records and open the gate around themselves. So P_b > 0 and m² = (k − P_b)/κ < 0: anti-screening.
  - A12's line "gating ⇒ A6's 1/r and A4's no-freezing hold exactly in voids" should be narrowed. A6's 1/r also needs P_b = 0, which holds in the quiet class (Step 6), not in a full-rank sea.
- (c) Heating. One sharp lock next to a wall injects (CHECKED, `c2`):
  - 8/(3π)J = 0.849J under the old generator (EXACT closed form 2C_01);
  - 0.21J above the new walled ground state.

  With J ~ E_P (ARGUED), apply A19's bound (sharp events < 1e-90 per nucleon per tick, which `c4` converts to ≈ 2.2e-11 W/kg) to edge false records:
  - c ≲ 3e-86 per tick for one isolated record per nucleon (λ_min = 5e-6);
  - c ≲ 6e-128 per tick for nucleon-sized recorded balls (λ_min = 5.3e-4);
  - then a genuine excitation next to a record would be recorded once per ≳ 1.6e42 s, against an age of 4.4e17 s.

  Ways out that stay open:
  - a rank-deficient emptiness at edges;
  - A12 windows at edges, whose vacuum rate falls as e^{−2κT} and whose cuts are soft, with the memory made of matter (C15);
  - coarse records (A19 R2).
- (d) Creep without steps (`c4`):
  - 3.5e-23 m over the age at c = 5.4e-44 (strong enough to record a particle in about 1 s);
  - 6.5e17 to 6.9e19 m at c = 1e-3.

**Step 8. Light near matter [ARGUED model; EXACT arithmetic, `c4`].**
- **Model.** Per tick, a photon is recorded with chance κ times its weight on gate-open sites. So α_rec = κ·s_rec/v_L, with s_rec the record surface area per unit volume, and the cross-section per recorded object is σ = κA/v_L.
- **Largest allowed κ per contact tick** (v_L = 1):

  | Medium | One isolated recorded site per nucleon | Nucleon-sized recorded ball | Atom-sized recorded ball |
  |---|---|---|---|
  | Silica fibre, 0.2 dB/km | 2e34 | **3.9e-6** | 1e-15 |
  | Water or air | 5e36 | **9e-4** | 2e-13 |
  | Path since recombination (CMB) | 5e37 | **8e-3** | 2e-12 |
  | Intergalactic medium, z < 6 | 9e40 | 16 | 4e-9 |
  | Galactic gas, 1 kpc | 1e42 | 260 | 7e-8 |

- **Allowed recording cross-section per nucleon:** 3.5e-35 m² (fibre), 7.3e-32 m² (CMB path), 1.4e-28 m² (intergalactic medium).
- **Does gated F with modest κ (1e-3–1e-1) pass?**
  - Intergalactic medium and galaxies: yes, for any record geometry up to nucleon size.
  - CMB path: only for κ < 8e-3 with nucleon-sized balls.
  - Fibre and water: no, by 10²–10⁵, with nucleon-sized balls, unless the weight ignores light.
  - With sparse records: everything passes.
- **Ways to keep light unrecorded near matter:**
  - sparse records;
  - an energy-selective weight: A12 windows, or record "cavities" acting as matter memory with Lorentzian off-resonance suppression (ARGUED, not computed);
  - a charge-type weight, if light is a gauge ripple (ARGUED pointer);
  - small κ.

**Step 9. Origins.**
- (a) [EXACT] An empty preparation stays empty, and every record descends from the preparation. The initial condition must contain records. Per the brief, the Campaign 7 package already lists a preparation as supplied.
- (b) [EXACT] The preparation supplies the first menu frame. After that, every formation has a recorded neighbour that can set its menu (Q7, cut to agree). So the case "the conditions point nowhere" (A13 E2) never arises. In the quiet class, the preparation's contents must lie on the emptiness's axis (Step 6).
- (c) Record density over cosmic time:
  - at most one record per site, and a homogeneous gain of at most 1 − ρ0 [EXACT, A4 §3.1b];
  - full-rank sea: fills from sparse seeds (like Kolmogorov–Johnson–Mehl–Avrami nucleation, comparator), then freezes or thins (V1, V2);
  - quiet emptiness: saturates at seeds plus recorded excitations (V3);
  - quiet emptiness with a steady supply: accretes toward full (V5).
- (d) [ARGUED + toy] "No final":
  - from a finite preparation on the infinite grid, the frontier is never exhausted;
  - the quiet class is the natural local "no final": formation ends when nothing is left to record, motion never ends;
  - A4's thinning class appears with blind enclosure.

**Step 10. Fit with the axioms and owner readings.**
- Reading note 2 leaves the formation site and chance outside Admissibility, so the gate is a choice about formation [EXACT, textual].
- Q3: the gate is invariant under turning space alone and under turning possibilities alone [EXACT].
- Q4 must be read as conditional on formation (A8 said the same). Under gating no uninfluenced site ever forms, so Q4 only constrains the law's even-handedness [ARGUED].
- "A law privileges no states": the empty configuration becomes absorbing, as the full one already is. The law names no state; whether this counts as privilege is the owner's reading [ARGUED].
- The owner's open question becomes "no, by the gating rule". That differs from A13's "no, because a quiet emptiness never calls for it", and it does not depend on the emptiness.

## 4. Checks

Every run used `nice -n 10`, the four thread caps set to 1, and a 55 s alarm.

| Script | Checks | Key numbers | Time, memory |
|---|---|---|---|
| `c1_nosignal.py` | Gated package toy against a distant choice; uncut contrast; GHZ closed form | Cut TV ≤ 4.1e-16 (tolerance 1e-14); uncut 1.2e-3–8.9e-3; GHZ 0.25 | 8.8 s, 58 MB |
| `c1b_agree.py` | Records agree with their sites; start-of-tick gating | 1.05e-15; 0 of 786 violations; 96 orphans | 0.6 s, 57 MB |
| `c2_edge_rank.py` | Full rank next to walls (1D, 3D); energy of one sharp lock | Step 3c and Step 7c numbers | 0.3 s, 86 MB |
| `c3_growth2d.py V0–V5` | 2D growth, freezing, thinning, living | Step 5c table | ≤ 8.2 s, ≤ 40 MB |
| `c4_scales.py` | Transparency, heating, creep, void-heating arithmetic | Step 8 table; Step 7c/d; Step 2 | 0.7 s, 75 MB |
| `c5_dark_sector.py` | Invariance of the quiet class | Step 6 table | 1.3 s, 58 MB |

- The first version of `c5` (unmerged branches) was killed by the 55 s alarm (70 MB). The rewritten version merges branches by record configuration.
- `c2` initially kept coherences after a lock, which gave 0 J. That was fixed; the post-lock average now matches dephasing exactly (asserted).
- Not run: a 3D version of `c3`, with crowd-tilted steps and the quiet class.

## 5. Real-physics match

**Gains (EXACT within the toy).**
- Voids never record or disturb light, consistent with VLBI fringes and the CMB.
- The void-heating requirement disappears.
- Records form only beside records, like detectors only at apparatus.

**Comparators (not adopted).**
- The absorbing empty state of the contact process.
- Eden/Richardson growth and Fisher–KPP fronts.
- Diffusion-limited aggregation for growth fed by excitations.

**Falsifiers.**
- Any localization or decoherence of light in deep voids.
- Anomalous heating of, or Planck-energy emission from, matter surfaces. This would be expected if the vacuum next to records is full rank and the weights are sharp.
- A frequency-independent ("gray") loss in transparent media of size κ·s_rec, if records are extended.
- If records were identified with conserved matter, the record count's growth by absorbed excitations would conflict with conservation (ARGUED). Records must be facts, not matter quanta.

**Inherited.**
- The quiet aligned emptiness has z = 2 ripples (A9).
- The tension between z = 1 and quietness now sits at the edges.

## 6. Open edges and next steps

1. **A z = 1 emptiness that is rank-deficient next to records.** Charge-detecting gated weights would vanish on all pure-gauge (photon) states and record only matter beside records. Check the repo's ice/photon lane (not consulted here), and whether one qubit per site can carry the constraint.
2. **Edge windows with matter memory.** Records act as walls, so they make cavities. Compute the vacuum rate (expected power law, about (g/Δ)²) and the capture efficiency.
3. **A covariant menu rule** when several recorded neighbours with different contents surround a forming site.
4. **3D `c3`** with crowd tilt (bound matter), the fraction of excitations that escape through transience, and halos of stray records.
5. **Energy per false record** for windowed or coarse records, to see how far the edge requirement relaxes.
6. **Owner decisions**, in plain terms:
   - adopt the gate;
   - accept a starting set of records;
   - read Q4 as "given a record forms";
   - gate on the records present at the start of the tick;
   - choose what a fully enclosed spot does;
   - choose a tidy emptiness or the half-filled sea at edges;
   - choose how light near matter escapes recording;
   - decide whether "no records at all" may be a state the law never leaves.

## 7. Plain-language summary

Suppose a record could form only at a spot that already has a recorded neighbour. Then empty space far from every record never forms one, whatever its possibilities are doing, and light crossing it is left completely alone, which fits light from distant galaxies arriving unrecorded. The rule cannot carry news from far away, because it looks only at the records next door, and those always agree with the spot they sit on. The price is that a world with no records would stay empty forever, so the world must start with some. The spots right next to records still need care: if empty space there is the half-filled kind, records creep into it and each new one heats its surroundings, so empty space there would have to be the tidy, lined-up kind. Whether everything fills up and stops depends on one more choice: if a spot fully surrounded by records may still form one, the grid fills and stops; if it may not, or if records form only where something is going on, records stop multiplying but keep moving forever.

---

## ERRATA from the fourth hostile review (A34/REVIEW.md), added by the coordinator

- Lines ~25 and ~74: add 'on average over unread outcomes elsewhere; per outcome they change at once to agree with distant records (Q1)' (C74).
- Line ~169: λ_min = 5e-6 is a conservative stand-in; A28's computed 3D value 5.3e-4 gives 3e-88. The heating chain is ARGUED, order of magnitude (C73).
- The Q4 consequence is a reading (ARGUED), not a result (C75).
- Edge floor: EXACT for the uniform sea; A34 checked the staggered (KS) sea full rank (ν ∈ [0.015, 0.985]) (C72).
