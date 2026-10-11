# The gravity wall, current state: exercise summary (2026-10-09)

**How it was run.**
- The candidate exercise skill in PR #9472 was used, at the owner's request ("run the exercise on the current state of gravity … use opus 5.5 extra agents").
- The supervisor is Claude Opus 5.5.
- **Route, kill and test agents:** Claude Opus 5.5 at extra-high (xhigh) effort.
- **Blind check and outside view:** Opus 5.5 at default effort.
- **Referee:** every FAIL or no-go was refereed by **codex gpt-5.6-sol (xhigh), another vendor**, before being reported.

**Labels.**
- **proved:** an exact derivation in this packet. Nothing is landed.
- **checked:** a computation run here.
- **suggested:** an argument.
- **reading:** an interpretation.

This exercise extends the 09-29 gravity exercise.

## 1. The wall, in plain words

We want gravity to come out of the framework's own rules instead of being added as an extra ingredient. The framework is a grid of sites whose neighbours never change. Experiments show that gravity:
- has waves that travel at light speed;
- has waves with no mass;
- has waves that stretch one way while squeezing the other;
- pulls on everything equally.

Every construction we have built fails at least one of these:
- **Sites as on/off switches:** the waves are too slow, or carry an extra sideways wobble (09-29).
- **Sites as continuous dials:** the waves gain a mass. Matter's lowest-energy state on the grid resists being sheared, the way a crystal does, and that resistance is a mass. Only a number set by hand removes it.
- **Records as the carrier:** no pull at long distances, and no waves.

All of this is seen in the models we built, for small waves and weakly interacting matter.

## 2. What the exercise found

1. **The stiffness half of the wall is a known piece of physics, not a quirk of our models.** Couple gravity to a medium whose points carry fixed labels, and the graviton gets a mass equal to the medium's shear stiffness (Rubakov–Tinyakov, Dubovsky; checked here). Only three things are known to protect it:
   - an exact gauge redundancy, as in Einstein's theory;
   - having no spatial labels at all;
   - a fluid, whose points can be relabelled continuously.

   (checked; literature.)
2. **The cause is the grid's fixed, regularly repeating sites, not its fixed neighbours.**
   - **For interacting matter:** no continuous relabelling can undo a shear when the vacuum keeps the grid's repeating pattern ("Lemma R"; proved, same-family).
   - **The smallest version:** a cutoff fixed by the grid's labels gives a stiffness of K₀⁴/(120π²) per boson. A cutoff that moves with the geometry gives exactly zero (proved; checked).
   - **Neighbours re-chosen from the geometry:** this alone does not help. A crystal and a glass stay stiff. A random scatter is unstiff only *on average*; every patch carries a random stiffness that scatters gravitational waves (checked; refereed).
3. **Granting the cosmological constant does not help.** On a cube-symmetric grid the vacuum has three separate responses: one pressure and two shear stiffnesses. Any mechanism that tunes only the pressure cannot touch the shears, and ours have opposite signs (proved; checked).
4. **Every escape we tried either keeps the stiffness or loses the one shared light speed.** All of these are refereed; details are in `ROUTES.md`.
   - **A flowing (liquid) vacuum:** it removes the stiffness. But flat space then forces the liquid to have no inertia, and its rest frame splits the speeds of different particles (dead as an untuned escape).
   - **Frozen random sites:** they fail on per-patch noise.
   - **Smooth long-range couplings on the grid:** badly obstructed; one variant survives.
   - **Keeping the grid and paying with supersymmetry or self-tuning:** dead. Supersymmetry would have to stay exact down to about 1 keV.
   - **Wetterich-style position-blind physics:** the vacuum is a saddle (dead).
5. **Test T1 (refereed): what protects the shared light speed.**
   - On a grid that treats time as a fourth grid direction with the same step as space, symmetry forces particles' speeds to stay equal.
   - With a shape-blind smooth regulator and continuous time, the speeds split by about 0.7 × g²/16π², set by the regulator's shape, not its scale (checked).
   - So in every tested form, removing the stiffness costs the protection of one light speed. That is a trilemma between positivity, one protected light speed, and zero stiffness, at the free-field level for smooth kernels.
6. **Test T2 (refereed): the last keep-the-grid regulator fails.**
   - Every positive (one-step transfer), time-and-space-alike kernel coupled through true distance keeps a stiffness that falls only as a power of its width. The best is about 6×10⁻⁴ at width 10, with a 1/width² floor. Reaching about 10⁻¹⁰² would need impossibly wide couplings (checked; bounded to the families searched).
   - The only exact zero relabels momenta directly. It works for free fields, but it is outside the test's contract, and ordinary interacting laws cannot use it, because momentum stops adding up at vertices (checked; Lemma R, narrowed by the referee).
7. **None of the routes produces the graviton itself.** The liquid's displacement is a vector. Records carry only scalars and vectors (FR3). The "mediator" half of the wall is untouched (reading, as on 09-29).

## 3. Routes worth doing (at most three)

| Route | What you would have to believe | Cost | First test | What it would change |
|---|---|---|---|---|
| **Write the price down once** (a refereed note) | nothing new | 1–2 days plus a referee | assemble T0, R3's surface lemma, Lemma R, the fluid lemma, Lemma A/L plus the realization noise, Lemma N, T1, K3a″/W1 | It turns about fifteen results into one owner-level statement of what massless gravity costs on a fixed grid |
| **Decide whether to keep the grid and pay the tuning** (an owner decision, not a calculation) | that a second cosmological-constant-sized tuning is acceptable, about 1 part in 10⁹⁸ of two shear numbers | none; it is a choice | — | If yes, gravity work on the fixed grid can proceed with the stiffness carried as a tuned number (like the cosmological constant). The other walls (chirality, the mediator) remain |
| **A spacetime-event substrate** (random events scattered in space-time, causal-set-like) | that a law over sprinkled events can be shape-blind and keep one light speed in every configuration, not just on average | days | per-configuration stiffness noise for a 3+1 sprinkling. **PASS:** no long-wavelength noise and no tadpole | the one architecture no agent killed. **Reading:** "records form as events at random places and times" is exactly this kind of substrate |

## 4. What not to do next

- **Frozen random sites, or neighbours re-chosen on fixed sites:** they fail on per-configuration noise (refereed).
- **An ordinary liquid vacuum:** flat space switches it off, and its rest frame splits speeds (refereed).
- **Supersymmetry, self-tuning or frustration-free vacua on the grid:** they miss by many orders, or have no light cone.
- **Wetterich position-blind actions:** the vacuum is a saddle.
- **More record-carried gravity models,** frozen or moving: no long-range pull, no tensor waves (FR1 and FR3, refereed).
- **Long extrapolations instead of direct calculations:** K3a′'s lesson.
- **Working on an emergent graviton without a named mechanism.**

## 5. The exact price (suggested; assembled from refereed parts)

On the framework's fixed grid of regularly repeating sites, a graviton that is massless to the observed bound needs one of the following:
1. **A tuned cancellation of two vacuum numbers** (the two shear stiffnesses), each to μ ≤ 2.4e8 eV⁴ = (124 eV)⁴. That is about one part in 10⁹⁸ of their natural size (K3a″'s coefficient of about 1.2e-3 times the reduced Planck mass to the fourth), or 1.1e-104 of M_Pl⁴. It is a second cosmological-constant-sized tuning. Checked arithmetic, confirmed by the referee (B1 c1).
2. **Giving up the fixed site set** (the Lattice axiom). The replacement must also keep one shared light speed. Frozen spatial replacements fail (E2/E3, §7). The spacetime-event substrate passes the averages exactly, but its noise question is open (E1: INCONCLUSIVE, leaning FAIL; §7).

The middle option from the draft (a regulator that keeps the grid but suppresses the stiffness parametrically) was **closed by T2** (bounded, refereed). The only non-tuned keep-the-grid loophole left is a non-ordinary interacting law that evades Lemma R, and no such law is known.

Separately, **none of these produces the graviton itself**. That still needs a mechanism nobody has named.

## 6. Appendix

**Files.**
- **History and the wall:** `WALL.md` (steps 0–1), with the blind check in `agents/blind_check.md`.
- **Ledger and reduction:** `ASSUMPTIONS.md` (steps 2–3).
- **Routes:** `ROUTES.md` and `APPROACH_REGISTRY.md` (steps 4, 6 and 7).
- **Literature:** `OUTSIDE_VIEW.md` (step 5).
- **Tests:** `TESTS.md` (T0, T1, T2).
- **Agent texts:** `agents/` (routes, kills, referees, the supervisor's thread).
- **Scripts:** `scripts/`.

**Assumptions most likely to be wrong:**
- "harmonic or weak coupling suffices" (S3);
- "the vacuum is crystal-like" (S4).

**Assumptions most expensive to be wrong:**
- the fixed site set (L1);
- naturalness (S6).

**Candidates for a physics-loop PR:** the price note (route 1).

**Literature worth translating:**
- Rubakov–Tinyakov and Dubovsky (Lorentz-violating mass taxonomy);
- Collins et al. (2004);
- Belenchia–Gambassi–Liberati (Lorentz-naturalness mechanisms);
- Bombelli–Henson–Sorkin (sprinklings);
- Bietenholz–Wiese and Hasenfratz (perfect actions).

## 7. Follow-up tests at the owner's request (2026-10-09)

The owner asked: "test the spacetime-event substrate with records as events, and test what happens if we give up the fixed repeating pattern. maybe the grid does not have all sites present? or there is no fixed pattern? or??"

Every run used a worker on Opus 5.5 at xhigh and a codex sol referee. Readings were fixed before running (`TESTS.md`).

| Test | Substrate | Verdict (refereed) | Why |
|---|---|---|---|
| E2 | the grid with sites missing at random (frozen, or appearing over time) | **FAIL** | Still stiff against shear on average in both channels at every fraction tested. Every fraction below 1 adds patch-to-patch noise that does not fade at long wavelength |
| E3a | quasicrystal (icosahedral) | **FAIL** | Quiet, but stiff on average. The stiffness is the same in all directions and is zero only at hand-picked coupling ranges |
| E3b | evenly spread random sets (hyperuniform) | **FAIL** | Even density does not give even stiffness. Noisy, and stiff on average |
| E3c | random sites that keep appearing | **FAIL** | Zero on average, but noisy at every stage; nothing ever moves to smooth it |
| E1 | records as random events in spacetime (causal-set-like; needs a Lattice change plus a supplied time order) | **INCONCLUSIVE, leaning FAIL** | The averages are perfect: no shear stiffness and one light cone, both exact. But in any single set of events the standard wave operator gathers noise from the whole past, a gain that grows with the size of the past (exact), and the step-by-step evolution blows up at the tested scales. Whether it still blows up at Planck-scale settings needs an extrapolation over about 60 decades, which the rules forbid |

**Structural reason for the frozen cases (Lemma P, referee-corrected).** If the rule that places frozen sites looks the same after any volume-preserving stretch (which is how the average stiffness is protected), the pair statistics are forced to be exactly random-like, and density noise is not suppressed. Quiet patterns (crystals, quasicrystals, evenly spread sets) lack that protection. The referee's strongest correct statement: give up *ensemble-symmetry-only protection on a frozen spatial substrate*. That is narrower than "give up the repeating pattern". An exact realization-wise identity (a stress that is a divergence) remains open.

**What this leaves.**
- **The spacetime-event substrate is the only architecture whose averages are exactly right.** Its open problem is noise, not the averages.
- **Its standard wave operator has signed weights.** Waves need signed weights in any step-by-step rule (block 122, on main), and on random events those weights amplify the substrate's noise.
- **The next test, if wanted:** an event dynamics without that gain (a stable generalized d'Alembertian, or influence passed only along links), or a direct small-ε measurement of the growth exponent.

## 8. Follow-up 2: reasoning backward from gravity to the substrate (2026-10-09)

The owner asked to "reason backward about what the substrate must be to get everything we need for gravity".

**Who did it.**
- B1 (physics-first) and B2 (framework-first), both Opus 5.5 at xhigh, working independently.
- The supervisor's own thread, written before either reported.
- The codex sol referee: **all three CONFIRMED WITH CORRECTIONS.**
- Texts: `agents/B1_report.md`, `agents/B2_report.md`, `agents/supervisor_thread.md`, `agents/backward_comparison.md`, `agents/B_referee.md`.

**In plain words.**
Working back from what gravity does, the fabric of space cannot behave like a fixed grid of positions that actually exist. A grid that physically exists resists shear, and that resistance gives the graviton a mass. Rotation or Lorentz symmetry, however large, cannot forbid that mass; Einstein's gauge symmetry can. So any substrate must either:
- carry an exact version of that gauge symmetry, so that relabelling the grain changes nothing, possibly holding in each actual arrangement or history; or
- show some other mechanism, with numbers, that keeps the graviton massless, keeps one light speed, and keeps the grain's randomness off long waves.

If it does, the rest follows: the equal pull on everything (Weinberg) and Einstein's nonlinear equations (Deser/Wald). These derivations do **not** prove that the grain must be random events, a fluid, or quantum and unrecorded. They show that those are the known ways to get the protection.

**Proved under stated hypotheses (refereed).**
- **The gauge identity forbids the mass; rotations and Lorentz symmetry do not.** Linearized gauge invariance, imposed for every momentum, forbids every local mass form of h. Point groups and the Lorentz group leave tr h² invariant. The counts of free mass numbers: cubic O has 2 in the TT channels, icosahedral 1, W(B4) 3.
- **Poisson randomness is shape-blind in law.** A Poisson process is invariant in law under every volume-preserving map.
- **Lemma Q, corrected.** A locally finite set invariant under a connected group lies in the group's fixed set. So a classical configuration with two or more points cannot be invariant under full translations, full SL(d) or the full Lorentz group. Its use survives: a classical grain carries those symmetries only in law. It does not exclude internal or gauge symmetries acting on fields over a fixed point set.
- **BHS:** no Lorentz-equivariant finite-valency neighbour map exists on a Poisson sprinkling.
- **The classic theorems,** each with its hypotheses: Weinberg–Witten, the soft theorem, and the spin-2 bootstrap.

**Supported by naturalness arguments, not logically forced (referee item 14).**
- Fixed physical labels give a dangerous shear response.
- Time and space must be exactly alike.
- The gauge identity must hold per realization.
- "Gauge or coherent" exhausts the quiet-noise mechanisms.
- Records help only as spacetime events.

The five properties (relational, spacetime-like, dynamical, no frozen labels, shared) are **a design programme**, not a theorem. The real exits are tuning, extra symmetries, non-locality, holography, constrained sectors, correlations and strong RG flows.

**New checks (refereed).**
- **4D Euclidean random lattice** (the finite-valency loophole of BHS): mean zero, but white per-site TT noise of about 0.06, flat over a 16× range in N. This is a **bounded FAIL for the tested implementation** (one kernel, a free scalar), not a class-wide exclusion.
- **Noise power counting:** mass-type noise is relevant in frozen 3D and marginal in white 4D; kinetic-type noise is irrelevant. "Noise only through dimension ≥ 4 operators" is a **sufficient** criterion, not a necessary one.
- **A frozen-box record count** (one record per Planck cell) exceeds black-hole entropy by about 2.4e38 for a solar mass, if each cell is an independent O(1)-entropy record.

**Records.**
- If every Planck-density event were a record that projects a changing matter quantity, matter would heat or Zeno-freeze. The matched bound is about 1e-151 per event.
- **The tension is resolved if** the event locks only its own occurrence and relations, or something conserved or gauge-invariant. Matter records would then be sparse and coarse.
- **Reading:** "an event happening" and "a value being locked" have to be different things if spacetime itself is made of events.

**The owner's "neighbourhood moves across the substrate (qubits too)".** In its relational reading, where the law never sees the underlying sites, this has the shape of the textbook escape: relabelling is gauge. To meet everything it would also have to treat time and space alike, and keep its fine structure off long waves, either per realization or by staying quantum. Neither is shown.

**Next tests, in the referee's order.**
1. **Link-noise propagation with matter.** Phase, amplitude and timing residuals, plus the retarded TT self-energy; E1′ is its first part.
2. **The interacting hypercubic TT Ward identity.** Does keeping the grid cost only the two shear tunings, or a graviton-speed tuning too?
3. **Extend the random-lattice check:** direct spectra, a second kernel, fermions.
4. **The response spectrum of a classical record gas.**
5. **Coherent against frozen substrate,** as a mechanism demonstration only.

## 9. Follow-up 2: influence passed along links (E1′, E1′-b; 2026-10-09)

**Setting.** The same records-as-events test setting as E1. Each event is influenced only by events **linked** to it, i.e. with nothing in between: Johnston's path-sum propagator. There is no extra non-locality scale.

**Who did it.** A worker on Opus 5.5 xhigh. The codex sol referee ruled gravity INCONCLUSIVE and matter M-INCONCLUSIVE. The supervisor's follow-up bound E1′-b was then CONFIRMED WITH CORRECTIONS, which made **gravity PASS** (`agents/E1p_*`, `agents/supervisor_E1p_b.md`).

**Massless waves (the stand-in for gravitational waves and light): PASS, for a scalar stand-in.**
- **The averages are exact.** The influence travels exactly on the light cone and is exactly massless, with only power-law corrections at the Planck scale and no mass.
- **Within any single set of events,** the wave's noise is counting noise: how many links connect the observer to the source.
- **The proved bound (E1′-b, refereed):** the noise is never more than about √3 times pure counting noise, for any source size.
- **The numbers:** for a neutron-star merger at 1 Gpc the relative noise is about 4e-29, and the arrival-time smear is about 1e-104 s.
- **Nothing outside the source-to-observer region matters,** and relays do not compound the noise.
- **E1's blow-up was the operator, not the events.** BD's signed step-by-step rule amplified the substrate's noise; positive, link-only influence does not.

**Massive matter: M-INCONCLUSIVE.**
- A mass needs signed weights in the path sum. This is block 122 again: waves that are not pure light-cone transport need signed weights.
- **Between two single events,** the massive amplitude becomes noise-dominated beyond about 3 Compton wavelengths, at any density.
- **Not computed:** whether real particles stay coherent over a kilometre, i.e. a wavepacket measured by a spread-out detector, including regeneration along the trip.
- **The mean has a slow growing mode,** about 0.61·m³ℓ². For a proton that is one e-fold per 6e22 m; the referee derived it independently.

**Not tested:**
- the graviton as a tensor (helicity-2) mode, or a gauge constraint;
- nonlinear gravity;
- E1's per-realization "crackle" of the order under strain;
- initial-value evolution, since the link field is source-driven.

**Locality.** Each event has about 5e122 past links over the age of the universe. That unbounded valency is what Lorentz invariance requires (BHS), but only the links into the source enter.

**Axiom conflicts, unchanged.**
- Lattice is replaced.
- The causal order is supplied, because records carry no time.
- Records as events conflict with "one record per site, permanent".
- At Planck density, an event happening must differ from a value being locked (§8).

**What this means for the backward reasoning (§8).** The event substrate with link-only influence now delivers, for massless scalar waves:
- shape-blindness in law;
- one light cone;
- noise-free long-range propagation.

What it still lacks:
- a graviton (a gauge mode of the geometry);
- coherent massive matter;
- a dynamics for the events themselves.

## 10. Campaign C3 (owner, 2026-10-10 00:47Z to 04:00Z): every open lane at once

**Who.** 15 research workers on Opus 5.5 at max effort, each followed by an adversarial Opus 5.5 checker at xhigh, and then a codex sol referee (another vendor) on every lane with a FAIL, a no-go or a contested claim. A compressed exercise (3 lenses, a kill round, a next test) ran on each of the three walls. Readings were fixed before every run (`TESTS.md`, "Campaign C3"). Lane reports: `agents/C3_*`.

**In plain words.**
- **Gravitational waves.** On the event substrate they travel cleanly along links, at the linearized level. But a single frozen set of events cannot carry a smooth graviton, and nothing found so far protects its masslessness.
- **Matter.** It needs signed or complex weights: that is proved. With signed weights, heavy particles pick up noise, and whether real matter stays coherent depends on what carries mass. That is unresolved, and possibly testable against atom interferometers.
- **Spacetime cannot grow itself** by any local rule tried. The event set has to be supplied, or formed by a non-local, size-aware law.
- **Keeping the grid** is not shown to cost only the two shear tunings. Further speed tunings are expected but not established.

| Lane | Question | Verdict (referee) | What it means |
|---|---|---|---|
| G-A | the event order itself as the graviton | **FAIL**, scoped to the frozen-embedding picture | On one frozen set of events a wave changes the order in jumps. The jumps' action variance exceeds the wave's own action (about 1e81 for local BD). It is sampling noise, present even without a wave |
| G-B | a spin-2 field carried on links | **INCONCLUSIVE** (the admixture is a controlled 7.3e-28; the "mean exactly GR" clause fails only at finite density) | Linearized GWs ride links cleanly |
| G-C | what protects the graviton | **INCONCLUSIVE** | The no-go holds only in the frozen picture. The quantum-sum branch is open |
| M-A | packet into detector over 1 km | **M-INCONCLUSIVE** | Exact tools, but an uncontrolled growth exponent |
| M-B | unitary matter on links | **INCONCLUSIVE** | No equivariant isometry moves amplitude between events. Link (arc) states are open |
| M-C | mass without signed weights | **CWC: no all-nonnegative linear rule gives the massive mean**, in any dimension | Mass needs a sign or a phase somewhere |
| M-D | composite coherence | INCONCLUSIVE (no codex referee needed) | The noise is per constituent, not total mass. The 70 s Rb result would need every mass-vertex scale below about 12 MeV, conditional on the uncontrolled chain law |
| D | spin-½ on links | **INCONCLUSIVE** (worker FAIL not confirmed) | Order alone gives no spinor and no handedness. Massless Dirac in mean is reachable. Chiral matter needs an orientation and a spin-transport structure (a price) |
| F | can records grow spacetime | **bounded FAIL** (CWC) | Exchangeable, frontier-only and classical DGC+Bell growth cannot give 4D |
| K | the cost of keeping the grid | **INCONCLUSIVE** | Two shear tunings alone are not established. Speed-sector tuning is generically expected, unproved |
| X1 | the random-lattice spectrum | **bounded FAIL** (CWC) | Flat noise, S ≥ 2e-3 |
| X2 | the response of a classical record gas | **bounded FAIL** (CWC) | Noise without dissipation (n_S = 0) |
| G-L | link-only lensing (Van Vleck) | **FAIL** (CWC) for the unweighted one-hop link mean | On curved backgrounds the link mean has weight ν^{−1/2} where GR has Δ^{1/2}. It de-magnifies where GR magnifies, an O(1) mismatch at any density. Flat-space results are unchanged. Weighted links, multi-hop and other readouts are open |

**The three walls, after the exercises** (27 routes, all killed; same family, not refereed):
1. **Formation:** a supplied event set, or a whole-region formation law that knows its final size.
2. **Massive matter:**
   - a non-locality scale plus a signed hop with cancelling moments. The pre-registered profile FAILs; a post-hoc profile whose first two moments vanish is a lead;
   - or composites with soft binding;
   - or a coherent quantum event dynamics.
3. **The graviton:** a covariant growth law with Einstein histories, no e^{iS} weighting by interval-count actions, and link readouts that focus like GR. **G-L (refereed FAIL) shows that unweighted one-hop links do not focus like GR.** Weighted or multi-hop readouts would be needed.

**Prices, named only as prices, nothing adopted:**
- the Lattice axiom replaced, and a causal order supplied;
- an event happening distinguished from a value being locked;
- an orientation and spin-transport structure for chiral matter;
- a formation law beyond nearest-neighbour locality;
- possibly a non-locality scale for massive matter.

**What closes next, in the referees' and the exercises' order:**
- referee Lemma L and the signed-hop ladder;
- the bound-state chain rate M_pair(R) for composites;
- re-register lane K in an implementable form.


## 11. Lane R: gauge redundancy as the primitive (owner, 2026-10-10)

**In plain words.** We asked whether a redundancy among records, a gauge symmetry, could keep the graviton massless and also make it pull on all matter equally. Four probes and three other-vendor referees say: **not shown either way (INCONCLUSIVE)**. The route was already partly explored in September; the prior-art probe found that.

- **What works.** A gauge redundancy does forbid the simple mass terms. Breaking it to let matter couple brings back exactly the two shear numbers that P0 tunes.
- **What fails, in the tested models.**
  - The simplest lattice versions give waves whose frequency rises as k² or k³, not light-like.
  - Or they carry extra spin-1 waves.
  - Or they couple to an emergent charge rather than to matter's energy.
- **What is left.** One construction has two light-like graviton modes and a 1/r pull: Gu–Wen's "weak" type with both of Einstein's constraints. Nobody has shown that lattice matter can feed it through an exactly conserved stress, or that qubits can realize it. That is the decisive next test.

Details and referee lines are in `TESTS.md` ("Lane R results").

## 12. Lane RN: feeding matter to the live graviton (owner, 2026-10-10)

**Plain version.** We coupled matter to the one graviton construction still standing (§11): the "weak" theory with both of Einstein's constraints.

- **Free particles work at first order.** They have an exactly conserved momentum on the lattice and pull with 1/r and the same G for every mass. A definite extra term, fixed by the matter law rather than tuned, cancels the graviton mass they would otherwise induce.
- **Interacting particles of the simplest kind cannot feed it.** For d ≥ 2, collisions on a lattice conserve only energy and particle number, never momentum (refereed; Spohn's theorem agrees). Whether this forces a graviton mass was not shown.
- **Escapes.** Coupling through the lapse alone fails: either matter can't move, or light isn't bent. Matter made of defects of the gravity field might escape, but nothing shows it falls universally.
- **Verdict: INCONCLUSIVE.**
- **What decides it next.** The framework's own matter, staggered fermions, carries internal "taste" structure. That might supply the extra conservation the simple case lacks. That is the next test.

Details are in `TESTS.md`, "Lane RN results".

## 13. Lane RS: does the framework's own matter supply the missing momentum? (owner, 2026-10-10)

**In plain words: no.**
- We tested staggered fermions, the framework's matter, with simple contact interactions and with electromagnetism.
- Colliding particles on the grid conserve energy and particle number, but never a momentum that could feed the graviton.
- The fermions' extra "taste" labels don't help. Their band is the simple lattice band in disguise, with momentum doubled, so the same theorem applies.

**Status.** Two refereed bounded FAILs, momentum only. The live graviton route (§11, §12) therefore needs one of:
- momentum defined non-locally (power-law tails) with interactions that never scatter across the zone boundary. Correction 2026-10-10: Admissibility fixes only the local rule, and influence can travel through chains of sites, so this is not excluded by the axiom. Whether a nearest-neighbour rule can produce it through gapless networks is untested;
- a lattice momentum added as a new primitive;
- an untested regime: strong coupling, or matter made of defects.

Each of these is an axiom price, and adopting any of them is the owner's decision.

Details are in `TESTS.md`, "Lane RS results".

## 14. Lane RG: can a network of nodes make momentum exact? (owner, 2026-10-11)

**Plain version.** The owner's idea: influence travels through chains of sites, so maybe a network can make collisions that never "wrap around" the grid. Then a spread-out momentum would be exactly conserved and could feed the graviton.

- **Exactly: no, for every well-behaved network.** Finite networks, networks of any depth built from linear links, and contact forces of any strength all give collision amplitudes smooth enough that vanishing on the wrap-around collisions forces them to vanish everywhere (refereed).
- **Still open:** strongly interacting laws whose amplitudes jump across internal walls. These are not excluded, and not constructed.
- **Approximately: yes.** Smoothing chains suppress wrap-around collisions by a factor of 16 per step, so about 80–900 steps (10⁻³³–10⁻³² m) give 10⁻¹⁰⁰. They also switch off all scattering at lattice-scale momenta.
- **A new catch.** Even with exact momentum, the graviton's constraint needs that momentum to equal the matter's energy flow. For ordinary nearest-neighbour matter it does not. It would need matter whose hopping falls off as 1/r², or a network that carries the flow itself (not yet shown).
- **Verdict: INCONCLUSIVE.**

Details are in `TESTS.md`, "Lane RG results".

## 15. Lane RC: carrying the energy flow (owner, 2026-10-11)

**Plain version.** Three probes, each refereed. One deeper result came out.

- **The deeper result (C3, refereed).** On a fixed grid, even free particles cannot keep Einstein's constraints consistent. The particles' momentum on the grid moves them by "central differences", not by true shifts. So "momentum" and "boost" do not combine the way relativity needs. No correction that depends on the metric can fix this; it sits in the global symmetry part, where all such corrections vanish. It holds for ordinary local single-band matter, and it does not need collisions at all.
- **The carrier (C1, refereed).** Feeding the graviton needs particles whose energy is exactly √(m² + c²k²) across the whole grid (the "SLAC" form), with no umklapp. No finite network of nodes can produce that band exactly. Approximations work at low momenta, but leave an order-one error at the zone edge. A two-band trick reduces that error but pushes the problem into the second band.
- **Strong coupling (C2, INCONCLUSIVE).** No model tested in 2D or 3D, Kitaev's included, has exactly conserved energy flow while respecting the cube symmetry. The survey did not settle Kitaev's full sector sum or its behaviour at finite temperature.
- **Verdict: INCONCLUSIVE.** The escapes left all go beyond regular, local, finite-band matter:
  - non-local matter, such as 1/r hopping;
  - matter with infinitely many bands, or matter built as a network;
  - matter dressed by gapless modes;
  - giving up Einstein's constraint algebra in favour of a preferred time slicing.

Details are in `TESTS.md`, under "Lane RC results".
