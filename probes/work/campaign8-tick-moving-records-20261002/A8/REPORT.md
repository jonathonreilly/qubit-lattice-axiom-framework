# Lane A8 report: can the clock potential be additive and universal, and does it explain why gravity is weak?

All checks ran within budget: each run took under 8 s and under 95 MB, under `nice -n 10` with the four thread caps set to 1. Scripts are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A8/`.

## 1. Question

Lane G built a supplied toy in which wandering free records give each place a steady move-event clock. A clump that captures them for good slows the clocks around it, with a 1/r tail fixed by the capture current.

Using only odds set by neighbourhood conditions (Admissibility-like), within I1–I3 and Q1:
- (i) Can that mechanism be **additive** in the number of records for ordinary matter?
- (ii) Can it be **universal**, with every local event type slowed by the same factor?
- (iii) Does the **weakness** of gravity then come out naturally?

Sub-questions:
- weak-capture additivity and its crossover to capacity scaling (the I5-like regime);
- whether the shared-possibility flow can carry the effect through recorded regions;
- the universality condition and whether Admissibility makes it natural;
- whether capture set by content agreement (Q7 menus) gives an irreversible sink and a Gauss law;
- weakness;
- which of lane G's falsifiers each variant fixes or worsens.

## 2. Answer

**(i) Additivity: conditional yes.** Grades: EXACT identity, bounds and continuum solution; CHECKED on exact Z³ and in a 31³ box.
- Suppose each record captures a visiting wanderer with weak odds q, drawn afresh at every visit. Then the far-field charge is exactly Q = q·Σᵢ Nᵢ, where Nᵢ is the clock rate at record i. Each record counts in proportion to its own clock rate.
- Two-sided bound: qN/(1+q·ḡ) ≤ Q ≤ min(qN, Cap(B)).
- Everything collapses onto one number, the body's own surface potential t = qN/Cap(B) ≈ qN/(4πR).
  - For t ≪ 1, Q ≈ qN with a deficit ≈ 1.2t.
  - For t ≫ 1, Q tends to the capacity, which is proportional to radius. The surface clock rate tends to zero and the centre is frozen. This is the black-hole-like regime.
  - The natural crossover is where the body's radius equals its own "lapse radius", qN/4π. For matter filling a fraction n of sites this is R_c = √(3/(qn)).
- Under Q1, no wanderer ever enters a recorded site. A packed lump therefore captures only at its skin:
  - charge ∝ area for weak q;
  - charge ∝ width for strong q;
  - for any q, it is not ∝ N.
- So additivity needs ordinary matter to be sparse at the lattice scale, with every record touching empty sites.
- The shared-possibility flow is not a second carrier through packed matter:
  - recorded sites are walls for it (EXACT, for two-site change that keeps locks);
  - a packed region holds no shared possibilities at all;
  - a coherent flow would cast a 1/r² shadow, not a 1/r field (ARGUED).

**(ii) Universality: conditional yes.** Grades: EXACT bookkeeping; ARGUED naturalness.
- The condition: every readable event (formations, stops, moves of matter records, and each step of the change between records) is triggered by exactly one wanderer arrival in its neighbourhood, with odds that do not depend on how many wanderers are around. All clocks then slow by the same N(x), up to O(u∞·Φ).
- The trigger must be a record *event*, not record *presence*. Presence-gating makes clocks run fast near matter (EXACT sign).
- The trigger must not depend on content species.
- Admissibility does not supply this: its reading note 2 leaves rates aside. A homogeneous change running at a global pace (Campaign-7 sentence 2) would break it.
- Under universality the readable clock rate is the event-rate field. That field is exactly linear-harmonic outside matter for any hop law, so **β_eff = 1/2 is locked** (EXACT, mean field).

**(iii) Emergent sink: conditional yes.** Grade: CHECKED.
- Rule: a wandering record stops when its content agrees with all its *stopped* neighbours. Capture is then irreversible from permanence alone.
- The clock deficit equals the lattice Green potential of the measured capture current to 1–2% (Gauss).
- The capture current matches the value computed from the odds.
- But if the rule cannot tell stopped neighbours from wandering ones (content only):
  - the seed lump dissolves;
  - the void forms and dissolves clusters;
  - there is no far field (CHECKED).
- A sink also accretes without bound (diffusion-limited-aggregation-like growth).

**(iv) Weakness: no; it does not come out naturally.** Grade: ARGUED.
- The coupling per record is q in lattice units.
- Matching G_N for a proton-mass record on a Planck-spacing lattice needs q ≈ 1×10⁻¹⁸.
- Neighbourhood odds are O(1): Q4 gives 1/2 for an uninfluenced stop-or-continue choice. Nothing in the axioms fixes q.

## 3. Derivation

**3.0 Supplied toy (nothing adopted).** This is lane G's toy.
- Wanderers hop with odds κ per tick (κ = 1/12): lazy 1/2, then a uniform direction.
- One record per site. Contention is settled by equal odds. There are no swaps.
- The far gas density is u∞. The clock rate is N = u/u∞; the move-event rate is r/r∞ = N + O(u∞Φ).
- Capture is "stopping for good".
- I2 is read as relocation of a permanent record (lane G 3.0, lane M Step 13). That is a reading, not axiom text.

**3.1 Lapse-weighted charge (Task 1a; EXACT).**
- Let record i capture with odds q per visit. Its capture rate is then proportional to the local wanderer density: σᵢ = q·Nᵢ.
- With N = 1 − Gσ, where G is the exact Z³ Green's function, σ = (G_BB + I/q)⁻¹·1.
- Summing (I + qG)σ = q·1 gives the identity **Q = Σσᵢ = q·Σᵢ Nᵢ**.
- The non-additive part is exactly the depth of the clock potential at the records:
  - Q = qN(1 + ⟨Φ⟩_records);
  - to first order the deficit is q·ḡ, with ḡ = 1ᵀG1/N.
- A single isolated record has charge q₁ = q/(1+qG(0)), with G(0) = 0.2527.
- Consequences:
  - the coupling per record is q₁;
  - each record contributes in proportion to its own clock rate;
  - interposed matter casts no line-of-sight shadow. The mutual effect is that each record's capture is reduced by the others' potential, isotropically (EXACT within the linear toy).

**3.2 Bounds (EXACT).** G restricted to a finite set is positive definite, so:
- Q ≤ qN, because (I+qG)⁻¹ ≤ I;
- Q ≤ Cap(B) = 1ᵀG⁻¹1, by operator monotonicity;
- Q ≥ qN/(1+qḡ), by Cauchy–Schwarz;
- ḡ ≥ N/Cap(B).

So the charge is additive when qḡ ≪ 1, and capacity-limited when t = qN/Cap(B) ≫ 1.

**3.3 One-parameter collapse and the I5-like regime (EXACT for the continuum ball; CHECKED on the lattice).**
- Uniform ball of filling n, with k² = qn:
  - inside, ΔN = k²N, so N(r) = sinh(kr)/(kr·cosh kR);
  - Q = 4πR(1 − tanh(kR)/(kR));
  - Q/(qN) = F(t) = (1/t)(1 − tanh√(3t)/√(3t)), with t = qnR²/3 = qN/(4πR).
- Small t: the deficit is (6/5)t.
- At t = 1: qN = Cap, the surface clock rate tanh√3/√3 = 0.542, and the mean rate over records is 0.458. This is the natural crossover, R_c = √(3/(qn)).
- Large t:
  - Q → 4πR, so charge ∝ radius;
  - the surface rate ≈ 1/(kR) and the centre rate is sech(kR), so the interior is frozen.
- In GR terms (comparator), qN/4π plays the role of GM/c², and t plays the role of compactness.
- Two separate conditions:
  - Jamming alone freezes a lump's interior: no moves, no formation (EXACT).
  - The black-hole-like *exterior* (surface rate → 0, charge ∝ radius) needs t ≳ 1.
  - A packed lump with weak capture is frozen inside but barely changes the clocks around it.

**3.4 What Q1 does to additivity (EXACT).**
- One record per site plus permanence means wanderers never occupy recorded sites. A stop or a formation can happen only at an unrecorded site.
- So Q counts *exposed contacts*, weighted by the clock rate:
  - a packed lump with weak contact odds q has Q ≈ q·Σ_contacts(arrivals) ∝ area;
  - with strong q, Q ≤ Cap(B∪∂B) ∝ width.
- Additivity in N requires each record to have empty neighbours that wanderers can reach (sparse or porous matter).
  - Per-record charge then scales with the record's exposed contacts.
  - Packing-fraction dependence is O(n).
  - Sparse matter follows the same t-collapse (CHECKED, a8_2).

**3.5 The flow is not a second carrier through packed matter (Task 1b).**
- **(B0, EXACT)** Take one qubit per site and a fixed two-site change h_xy. If that change is to keep *every* possible locked content at x, then ⟨a⊥|h_xy|a⟩ ∝ 1 for all a. The vectors ⟨a⊥|σ_μ|a⟩ span ℂ³, so h_xy is non-interacting. Keeping locks therefore means the record constrains (compresses) the change.
- **(B1, EXACT)** Under that compression, a recorded site acts on each neighbour y only through the one-site term ⟨a|h_xy|a⟩. No term couples two neighbours through x. Recorded sites are walls for the flow, and act on neighbours as fixed conditions (Q7-like).
- Q1 puts shared possibilities only on unrecorded sites, so a jammed region contains no flow at all (EXACT).
- Caveats:
  - Three-site star terms could relay content across an isolated record (conditional), but never inside a jammed region.
  - Under lane M's guided reading R3, possibilities at recorded sites keep changing. Even so, a recorded site can neither form a second record nor change content, so it cannot capture (EXACT).
  - A coherent, uncut flow spreads ballistically (lane M t4: variance ∝ t²). Absorption by a body then leaves a geometric deficit ∝ (solid angle) ≈ a²/4r², a 1/r² shadow (ARGUED; comparator: Le Sage).
  - 1/r needs a direction reset each step. With a cut every step (R1) the flow is just lane G's wanderer.
  - Lane M Step 10 adds that a covariant, homogeneous, one-possibility-per-site range-1 tick cannot move a record, so an I4 conveyor needs extra structure.

**3.6 Universality condition U (Task 2; EXACT bookkeeping).**
- Let A(x) be the wanderer arrival rate in the closed neighbourhood of x.
- Suppose each event type e (formation, stop, matter move, each step of the change) occurs only together with an arrival, with conditional odds p_e that depend only on contents in the neighbourhood.
- Then λ_e(x) = p_e·A(x), so λ_e(x)/λ_e(∞) = A(x)/A∞ ≡ N(x) for every e.
- Since lane G's 1/r already needs a quiet void, the answer to the brief's open question is conditional: if U holds, empty sites far from records never form on their own.
- I1's tick is then local and influenced: one arrival is one local tick.

**3.7 How universality fails (EXACT, mean field).**
- Events needing k coincident arrivals run at N^k. Vacancy factors (1−u) and exclusion give O(u∞Φ). Both are small for dilute wanderers, the same regime lane G needs for the right sign.
- Events not gated at all run at N⁰ and must be absent.
- Presence-gating counts static records. Near a lump the record density is high, so clocks run *fast* (wrong sign). The trigger must therefore be events.
- With carried content, depletion is species-selective: a content-0 lump depletes only species 0. Gating must be species-blind, which is the natural default when no possibility is privileged.
- If Q4's equal odds are read as covering the decision "form now or not", static neighbourhoods get a nonzero hazard and gating fails. U needs Q4 read as conditional on formation, as reading note 2 suggests.

**3.8 β is locked at 1/2 under universality (EXACT, dilute mean field).**
- Suppose the hop odds D depend on local conditions. Then ∂ₜu = Δ_lat w/6, with w = D·u.
- In the steady state, w is lattice-harmonic outside matter. The event rate is departures plus arrivals, which equals 2w there.
- So an event-rate clock gives N = 1 − U exactly, hence N² = 1 − 2U + U², and β_eff = 1/2 for every hop law.
- A clock based on density instead (with D ∝ u^a) gives N² = 1 − 2U + (1−a)U², so β = (1−a)/2.
  - β = 1 needs a = −1: wanderers hop faster in depleted regions.
  - That makes the arrival rate D·u flat, so arrival-gated clocks see no potential at all.
- Presence- and arrival-gated processes agree only if D is constant.
- Within this class, universality and β = 1 cannot both hold.

**3.9 The change must be event-paced (ARGUED).**
- If the change between records runs at a global pace, the phases of possibilities (atomic-clock analogs) are not slowed at all.
- Universality needs an effective generator Σ N(x)·h_x: "influence between records" happening only on record events.
- Then influence advances at most one site per local event. Its speed is constant in local units and ∝ N in global units.
- That gives Shapiro delay ∫U and bending 2GM/(bc²): half of GR (γ_eff = 0, as lane G found).

**3.10 Is it natural under Admissibility? (ARGUED)**
- U is expressible as one fixed, covariant neighbourhood menu rule: "menu = {no event} unless a record event occurred in the neighbourhood".
- But "an event occurred" is a neighbourhood *condition* only if the snapshot carries it. Q1's agreement-change of the shared possibilities next to a fresh arrival, together with Q3 (odds depend on possibilities relative to the menu), could carry it. Otherwise one tick of memory is needed, beyond Q2's snapshot rule.
- Rates are outside Admissibility (reading note 2), so gating is a named conditional, not a consequence.
- Its ingredients coincide with lane G's conditions (dilute wanderers, quiet void, frozen jammed regions). That makes it coherent, not forced.

**3.11 Emergent capture (Task 3).**
- Rule R-held: a free record with at least one stopped neighbour, all carrying its content, gets the menu {stay}. Stopped records never move and contents never change, so the condition once met stays met. Irreversibility follows from permanence; no sink is imposed (EXACT logic).
- Two readings:
  - *Carried content:* a matching wanderer stops on its first contact. That is a perfect absorber for that species and none for the others: charge = Cap/k per species, capacity-limited, strong.
  - *Re-formed content* (each arrival is a fresh formation, R1-like): capture odds are q = 1/k per arrival.
- In both, J is computed from the odds and the geometry, and the depletion field is the Poisson potential of the capture current (CHECKED).
- The sink grows like diffusion-limited aggregation (comparator).
- Rule R-all (content-only, all neighbouring records counted, re-checked each tick):
  - disagreeing arrivals unlock surface records, so the seed erodes;
  - agreeing wanderers lock each other in the void, then get unlocked;
  - no net sink, flat field (CHECKED).
- Making stops sticky while letting free records lock each other would turn the void into a distributed sink. That screens the field with m² ≈ 72·u∞·q′ (via lane G 3.9's linearization; ARGUED).
- So an inert void plus an irreversible lump needs a "stopped" status visible in the conditions. Record content alone does not carry one (named conditional).

**3.12 Weakness (Task 4; ARGUED).**
- With Φ = −q₁Na/(4πr), matching G·m_rec/c² = q₁a/4π gives q₁ = 4π(m_rec/m_P)(l_P/a).
- On a Planck-spacing lattice: about 9.7×10⁻¹⁹ for a proton mass and 5.3×10⁻²² for an electron mass (EXACT arithmetic, given the identification).
- Neighbourhood odds are O(1):
  - Q4 gives 1/2 for an uninfluenced stop-or-continue choice;
  - k-content agreement gives 1/k, so a dilute contact would need k ≈ 10¹⁸;
  - in the continuum domain M₂(ℂ), exact agreement has odds 0 and overlap-type agreement averages 1/2.
- Exponential smallness from a long coincidence chain (p^m with m ≈ 60) is the generic way to get such a number. But a dilute contact has one recorded neighbour, not 60.
- q is a free number of the supplied capture rule. A small q also slows accretion, and under sticky free-record locking it would quiet the void: one small number would control both. It remains unexplained.

**3.13 Falsifier ledger (Task 5; ARGUED unless marked).**

| Variant | β | Waves | Establishment time | Other |
|---|---|---|---|---|
| A. Weak re-drawn capture, sparse matter | 1/2, unchanged | none | unchanged | Fixes additivity to O(t) and O(n). Weak q slows accretion. Lapse-weighted source counts binding twice relative to GR. |
| B. Packed lumps under Q1 | 1/2 | none | unchanged | Not additive (area or capacity law). Frozen interior (I5). |
| C. Emergent R-held sink | 1/2 | none | unchanged | Gauss emerges (CHECKED). Runaway accretion worsens secular growth. Carried content is species-selective and strong. |
| C′. Content-only R-all | no field | — | — | No sink (CHECKED). |
| D. Event gating (universality) | locked at 1/2 (EXACT, mean field) | none | unchanged | Fixes universality to O(u∞Φ). Local light speed constant in local units; bending and Shapiro delay at half GR. |
| E. Density-dressed hops, clock = density | (1−a)/2: worse for a > 0; 1 only for a = −1, which breaks D | none (finite-speed fronts) | slower | |
| F. Coherent flow as carrier | n/a | damped waves only for r < ℓ | ballistic within ℓ | 1/r² shadow within ℓ; 1/r only for r ≫ ℓ. Cannot cross packed matter. |

No variant makes static 1/r and propagation at light speed coexist on the same scales. With lattice-scale steps, one per Planck time, the 1/r profile is established in the age of the universe only out to about √(T/t_P)·l_P ≈ 5×10⁻⁵ m (EXACT arithmetic, given that identification).

## 4. Checks

**`a8_lib.py`** contains the exact Z³ Green's function, copied from lane G's g1 (validated there against Watson to 6e-13).

**`a8_1_transparent.py`** (0.7 s, 91 MB): volume absorbers on exact Z³.

Identity and bounds (s=5 cube, q from 1e-3 to 10):
- Q = qΣNᵢ to ≤ 3.0e-15 relative.
- The bounds hold at every q.
- Cap = 35.10, ḡ = 3.88 ≥ N/Cap = 3.56.

Collapse onto F(t), with t = 0.1, 0.3, 1, 3, 10:
- max |Q/(qN) − F(t)|: 0.042 (cube2), 0.035 (cube3), 0.029 (cube4), 0.020 (cube6), 0.014 (cube8), 0.013 (ball5). Deviations shrink with size.
- Crossover q_c = Cap/N compared with continuum 3/R_eff²: cube8 0.1166 vs 0.1218; ball5 0.1144 vs 0.1213.
- Mean clock rate at records at the crossover: 0.47–0.50, against the continuum 0.458.

Sparse sublattice balls (d = 2–4, N = 123–257):
- At q = 0.01 the deficit equals qḡ to first order: 0.0143 vs qḡ = 0.0145 (d=3).
- Deficits are 0.86–0.97 of the uniform-ball curve, across t = 0.01–2.1.

**`a8_2_contact_box.py`** (0.6 s, 77 MB; CG relative residual 1e-11): contact capture under Q1 exclusion, 31³ box, reservoir boundary.

- Single record: Q/q → 29.96 at q = 0.001. That equals 6 contacts × 5 free neighbours (exact leading order). Q(q=1) = 12.28 (Z³: 11.62).

Packed cubes at q = 0.001, A = Q/(N·Q₁) against the area-law prediction:

| cube side | A (measured) | area-law prediction |
|---|---|---|
| 3 | 0.3315 | 0.3333 |
| 5 | 0.1979 | 0.2000 |
| 7 | 0.1408 | 0.1429 |

Sparse lumps:
- A = 0.997, 0.990, 0.981 (N = 7, 33, 123; spacing 3) and 0.994 (spacing 4) at q = 0.001.
- 0.97, 0.91, 0.84 at q = 0.01.
- The deficit scales with t, at 0.66–0.94 of the uniform-ball value.

**`a8_3_agree_mc.py`** (5.5–7 s and ~83 MB per run): emergent R-held capture.
- Settings: k = 4, u∞ = 0.004, 3000 burn-in ticks plus 8×4000 ticks, seeds 20261002 and 11–14.
- Each block is compared with a mean-field solve on the block-start geometry, and with a Poisson solve sourced by the measured capture sites. Only free sites connected to the reservoir are used.

| Reading | Lump (start → end) | J_MC / J_pred | Deficit / Poisson(j_MC) | Other |
|---|---|---|---|---|
| carried | 27 → 231–389 | 0.97 ± 0.03 | 1.02 ± 0.05 | other-species deficit −0.008 ± 0.024 |
| re-formed | 27 → 3265–4386 (reaches reservoir) | 1.011 ± 0.007 | 1.020 ± 0.005 | — |

- In the re-formed run the 2% excess comes from growth within blocks. With 1000-tick blocks (2 seeds) the ratios become 0.990 and 0.986, and the clock ratios 0.992 and 0.990. Tolerance stated: 2%.
- No-capture control: zero captures; the deficits fluctuate by ±0.03–0.08. That is the noise floor of the carried reading.
- An earlier long run (84k ticks): 27 → 3593 records reaching radius 24, with J rising from 0.0058 to 0.128 per tick. This is runaway accretion.

**`a8_4_allnbr_mc.py`** (2.3–3.3 s, 62 MB): content-only rule R-all, four runs.
- The seed dissolves within 2000–10000 ticks in every run.
- Fraction of records locked in the void (r > 6): 0.6–0.8 at k = 4; 0.1–0.2 at k = 16.
- Free-record density relative to u∞ is flat: 0.97–1.01; 0.89–0.99 at u∞ = 0.001; 0.97–1.00 at k = 16. The re-formed variant shows an excess (1.04–1.22), not a deficit.

**Should be run (bigger, not run)**
- a8_3 at L = 63 with u∞ = 0.001 and re-formed k = 16, to get compact growth and a longer 1/r range. Change `L, C` (about 8× the cost).
- A universality toy with presence- and arrival-gated processes and density-dependent hops, to test 3.8 beyond mean field.
- Porous lumps (n = 0.1–0.7): charge per record against filling.
- Sticky free–free locking: measure the screening length against u∞ and q′.

## 5. Real-physics match (comparators, not adopted; values from memory, not re-verified)

**Matches**
- **Lapse-weighted source.** Q = qΣNᵢ has the structure of the Tolman/Komar mass ∫(ρ+3p)N dV, without the pressure term.
- **Additivity deficit of compactness order.** Earth 7×10⁻¹⁰, Sun 2×10⁻⁶, neutron star ~0.2. That is negligible for ordinary bodies.
- **Crossover at compactness ~1.** This mirrors the black-hole threshold. That is by construction of the identification, not a prediction.
- **No geometric shielding** for diffusive carriers.
- **Universality by gating** gives every clock the same redshift and a light speed that is constant when measured locally.

**Falsifiers**
- **Binding counted twice.** The toy's source carries twice the Newtonian binding (no stress or virial term). If inertia were the plain record count, this would be a Nordtvedt-type violation of order one in η. Lunar laser ranging gives |η| ≲ 10⁻⁴ (Earth binding fraction 4.6×10⁻¹⁰), and pulsar triple-system strong-equivalence tests constrain it further. The toy has no notion of inertia yet, so this is a conditional falsifier.
- **Composition dependence O(n)** from exposed contacts. MICROSCOPE bounds this at ~10⁻¹⁵. It fails outright if matter has packed sub-structure at lattice scale.
- **β = 1/2 and γ_eff = 0.** Mercury's perihelion would be half of GR, and bending and Shapiro delay would be half. Cassini bounds γ − 1 at ~2×10⁻⁵.
- **No waves.** GW170817 bounds the speed of gravity to ~10⁻¹⁵.
- **Establishment time.** About 50 μm for Planck-scale steps.
- **Runaway accretion and secular mass growth** ∝ κu∞q₁.
- **Local position invariance.** Different clock types agree on the redshift to roughly 10⁻⁶, which needs u∞ ≲ 10⁻⁶.
- **Weakness.** q ≈ 10⁻¹⁸ must be supplied.

## 6. Open edges and next steps

1. **A stopped-status mark.** The inert-void sink needs one, or a relational substitute. Candidate: Q1's agreement state of the shared possibilities next to an old record versus a just-moved one, with Q3 odds.
2. **An event-paced change.** Universality needs the change between records to run on record events. Test this against Campaign-7 sentence 2 and Q2's film reading.
3. **Inertia.** There is no notion yet. Additivity tests (Nordtvedt-type, composition dependence) need one.
4. **Where q comes from.** It could come from menu size or coincidence chains. Explore whether one agreement odds sets both the coupling and how quiet the void is.
5. **Bounded growth.** Is there an odds rule whose sink accretes boundedly? For example, surface poisoning by mixed contents.
6. **β, γ, waves, establishment.** These need a spatial sector and a wave carrier that this mechanism does not supply.

## 7. Plain-language summary

- If each record only rarely catches a passing wanderer, a clump slows nearby clocks in step with how many records it holds, as weight should. This holds only if the records are spread out so wanderers can reach every one of them.
- A tightly packed clump catches wanderers only at its skin, so it does not count its records properly. Once a clump slows its own clocks almost to a stop, it acts like the black-hole picture.
- All clocks slow by the same amount if nothing in a neighbourhood can change until a wanderer arrives. Wanderers are then the beat for everything, and empty places stay quiet.
- Records that stop when they match their stopped neighbours build such a catching clump on their own, and the slowing then follows exactly from how fast it catches. But a record must be able to tell a stopped neighbour from a wandering one; otherwise clumps melt away and the slowing vanishes.
- Nothing in the rules makes catching rare, so the weakness of gravity does not come out by itself; it would have to be put in. These are toy results under ideas that have not been adopted.