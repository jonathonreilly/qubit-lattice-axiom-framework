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

## 16. Campaign C4 first wave (owner, 2026-10-11): infinite bands, preferred slicing, dressed bands

**Plain version.**
- **Infinite-band networks: FAIL (bounded, refereed).** Making momentum and boosts close exactly needs, for each particle, a whole infinite tower of bands. That is a continuum field in every cell, with unbounded energy per cell. Every finite number of bands, and every coarse-cell version of the grid, only moves the anomaly; it never removes it. A network with N bands is just a finer grid. Still open: interacting matter built as composites of qubits, which this result does not cover.
- **Preferred time slicing: INCONCLUSIVE.** The healthy Hořava graviton fits on the lattice. But one loop of lattice QED leaves the electron 0.85% slower than light, which needs a tuning to 3×10⁻¹⁷. Only putting time on the lattice with the same step as space removes that. Several escapes remain open.
- **Dressed bands: FAIL (bounded, refereed).** Dressing a particle with soft quanta shrinks any corner in its energy curve by its residue Z; it never makes one. The exact SLAC corner therefore needs non-local hopping, or Z = 0.
## 17. Campaign C4 (owner, 2026-10-11): the boost wall

**Who and what.** The campaign ran from 16:21Z, with a planned end at 22:21Z. Probes: Opus 5.5 at xhigh (same family). Every probe recorded so far has a codex gpt-5.6-sol (xhigh) referee, from another vendor. Readings were fixed before each run (`TESTS.md:1245-1877`). This section records **referee verdicts only**. It was updated at wrap-up (about 21:55Z) to include RL2, RL3/RL3b, RP, RB, RN2 and RL4. §16 covered the first wave; this section covers the whole campaign so far. The synthesis was drafted by Claude Opus 5.5 (same family) and is not refereed.

**In plain words.**
- **The question.** On the grid, can ordinary local matter carry a graviton that is massless and pulls everything alike, without tuning by hand? C4 chased every escape that lane RC left open (§15).
- **One thing blocks every route tried.** On the grid, a particle's momentum moves it by a difference taken across neighbouring sites, not by a true shift. A boost built from the energy density then does not combine with that momentum the way relativity requires. Closing the algebra would need the curve of E² against momentum to have the same curvature everywhere. A curve that repeats around the zone cannot: its curvature averages to zero, so the misfit averages to a fixed amount of order one. This is C3 (§15).
- **C4 found the same misfit five more times:**
  - in bands built from many sub-bands;
  - in bound composites;
  - on a grid with time as a fourth direction (Euclidean), at second order;
  - inside the rotation part of the constraints, when the grid's own time slicing is used;
  - in the vacuum: free matter's zero-point energy shifts under one of the two shear strains (that this has the same cause is a reading, not refereed).
- **Escapes.**
  - Infinitely many bands per cell do close the algebra, but that is a continuum field in every cell (FAIL, bounded).
  - Dressing particles with soft quanta never makes the needed corner in the energy curve (FAIL, bounded).
  - Strong dynamics can make matter's speed differences die away, but too slowly in the tested QED case, and it does nothing for the graviton's shear stiffness or speed (FAIL, bounded).
  - A preferred time slicing is not ruled out, but every version tried costs extra tunings or a large hierarchy (INCONCLUSIVE).
  - A vacuum-referenced coupling rule cancels the interaction part of the shear response, but not the free part (FAIL for the framework's own fermions).
- **Costs now have numbers.**
  - With time on the grid (Z⁴): 11 gauge-restoring tunings by the registered count, not 2.
  - With continuous time: lattice QED splits the electron and photon speeds by 0.85%, which a counterterm must cancel to 3 parts in 10¹⁷.
  - Free local matter, on its own, produces one of P0's two shear numbers.
- **A correction.** Earlier records said a determined "seagull" term cancels free matter's shear response. That holds in one shear channel only (T_2g), not in the other (E_g).
- **Nothing passed. No lane proved a no-go for all lattice matter either**: every FAIL is bounded to its class.

| Lane | Question | Verdict (referee) | What it means |
|---|---|---|---|
| RI | Infinite-band networks | **FAIL (bounded)**; I1, I2, I3 each CWC | Exact closure needs a complete tower of bands per cell (one-particle level). Any finite N, or any coarse cell, keeps a band-and-zone-averaged anomaly of −1 per mode. A uniform L³ supercell is exactly a finer grid |
| RF | Preferred foliation (the grid's slicing) | **INCONCLUSIVE**; F1, F2 NOT CONFIRMED | Projectable Hořava fails, and so does the single-band fixed-generator realization. Non-projectable Hořava matches GSS on the lattice. Cubic-only gravity allows 6 mass invariants. The QED speed split on Z³ × ℝ needs a tuning to about 3e-17; time on the grid at ξ = 1 removes it |
| RD | Gapless-dressed bands | **FAIL (bounded)**; D1, D2 CWC | J_E = Z·J_ε0: dressing scales a kink by Z and never creates one. Exact SLAC at finite Z forces a non-local 1/r² bare tail |
| RE | Emergent Lorentz invariance from strong dynamics | **FAIL (bounded)**; E1, E2 CWC | Relative matter speeds can become irrelevant. The TT vacuum response and the graviton speed cannot. F2's split runs only to 7.34e-3 by 1.4 PeV, missing the bound by 2.76e16 |
| RW | Does the anomaly force a mass; is the broken theory healthy? | W1: **FAIL bounded to its ansatz** (CWC), unrestricted question INCONCLUSIVE. W2: **INCONCLUSIVE** (NOT CONFIRMED). W3: **INCONCLUSIVE**, with bounded FAILs for two subclasses (CWC) | No lane-level line is recorded. Under the fixed lane clause (`TESTS.md:1370`), W1's bounded FAIL is the only refereed FAIL, and its referee scopes the unrestricted question as INCONCLUSIVE |
| RM | Composites and continua | **FAIL (bounded)** (CWC) | Bound states obey the same sum rule, whatever their binding or size |
| RK2 | Z⁴ tuning count; discrete-time algebra | K1: **N_tune(Z⁴) = 11** (CWC); lane K answered **NO**. K2: **INCONCLUSIVE** (CWC) | Z⁴ protects matter speeds but moves the cost into the graviton sector. The free fields close through O(κ) and fail at O(κ²) |
| RF3 | Z⁴ matter with foliated gravity at a separate UV scale | **INCONCLUSIVE** (NOT CONFIRMED) | The explicit one-grid subcases need hierarchies of order 1e9 (scale) and 1e38–1e39 (a coefficient) |
| RV, RV2, RV3 | A dressed momentum that annihilates the vacuum | V1: **INCONCLUSIVE**. V2: **INCONCLUSIVE, leaning FAIL** (both NOT CONFIRMED). V3: **(a) FAIL, (b) FAIL (bounded)** (CWC) | The interaction part cancels at O(λ²) under Rule R. The free Jacobian leaves μ_E. The supervisor's summary line: the lead closes in this form (`TESTS.md:1815`) |
| RL, RL2, RL3 | Event-route lensing, and the noise of the stable readouts | RL1: **INCONCLUSIVE, leaning FAIL**. RL2: **INCONCLUSIVE, leaning FAIL** (CWC), with a **positive mean result**: all three stable six-layer operators give GR's √Δ focusing at leading needle order. RL3: NOT CONFIRMED as FAIL, so **INCONCLUSIVE, leaning FAIL**. RL3b: CWC, **INCONCLUSIVE, leaning FAIL**. **RL4: CWC, FAIL (bounded)**, so **the noise lane is FAIL (bounded)** | Two independent methods agree that the noise grows at rate k√ε/ℓ_k with exponent ½ and k = 2.73–3.25. At the 1e-19 m bar that is 281–334 e-folds, a miss of about 0.8 decades in ℓ_k. RL4 proved both lemmas: c_low = 0.63–0.71 ≫ 0.00975, for sources with a spacelike past edge. The noise fails the 1e-19 m bar. Edgeless sources and the exact prefactor remain open |
| RP | Species sum rules for μ_E | **FAIL (bounded)** (CWC) | Cancelling needs a count rule R0 plus the mass relations R2, R4 and R6. R4 is Pauli's quartic supertrace. The SM proxy misses R0 by +22F(0). Only exactly matched spectra cancel to all orders |
| RB | Boosts that are not first moments | **FAIL (bounded)** (CWC) | A regular affine-lapse smearing forces a first-moment boost. For a cubic Morse band, [K,P] cannot close as a function of (H,P). Undeformed closure is impossible on bounded exponentiating sectors. No global smooth undeformed Lorentz action exists on the Brillouin torus. Patchwise or singular DSR, fully deformed algebras, interacting matter and touching bands remain open |
| RN2 | Interacting matter that does not conserve particle number, d ≥ 2 | **INCONCLUSIVE, leaning FAIL** (CWC) | Under closure, every fixed-mass subspace folds into a complete tower (number conservation not needed). Closure is impossible if any global eigenband has a C¹ projector (a rigorous bounded FAIL for the regular-band subclass). A gap plus asymptotic completeness does not supply that band. The d ≥ 2 index lemma is open |

### The root obstruction, precisely (one statement, six refereed appearances)

**The statement.** Assume a regular local lattice law and a boost that is the first moment of the energy density. Its momentum generates central differences, factor by factor, not translations. Closure with the boost then needs Hess(E²/2) = βI on each band. A periodic band integrates its Hessian to zero, so the anomaly averaged over the zone is −β. That the six results below are one obstruction is the drafter's reading; each appearance is refereed separately.

1. **C3, lane RC (CWC; `TESTS.md:1209-1215`).** In the constant-shift, linear-lapse and rotational sectors, every regular local gravity-dependent completion vanishes. Closure then needs a constant Hessian, which leaves only a Carroll contraction.
2. **Finite bands: I1, I2 and I3 (CWC).**
   - Every finite-dimensional periodic C² Bloch matrix has a signed band-and-zone-averaged anomaly of exactly −β per mode (`C4_I2_referee.md:15`; `C4_I3_referee.md:21`).
   - Exact closure needs a complete reciprocal-lattice tower, i.e. "an infinite-dimensional, unbounded one-particle fibre" (`C4_I1_referee.md:21`).
3. **Composites: M1 (CWC).** Every globally isolated positive-energy composite band has averaged anomaly −βI, "independently of binding, size, internal fibre dimension or Chern twisting" (`C4_M1_referee.md:15`).
4. **Euclidean Z⁴: K2 (CWC; verdict INCONCLUSIVE).** Free scalar and naive/staggered fermion couplings are exact through O(κ). Their Killing transformations fail e(4) closure at O(κ²), and a seagull cannot repair it (`C4_K2_referee.md:17`).
5. **A preferred slicing: F1 (item confirmed; verdict NOT CONFIRMED).** "The rotation sector is inside the momentum-constraint bracket"; lapse transport gives the same obstruction in the fixed-generator single-band ansatz (`C4_F1_referee.md:9`).
6. **The vacuum: V3 (CWC).**
   - The bulk-local, translation-covariant uniform-strain coupling makes the vacuum energy carry the flow's Jacobian.
   - The T_2g flow is divergence-free, so μ_T2 = 0 in the thermodynamic limit (−7.62e-5 at L = 12 for the fermion).
   - The E_g flow gives μ_E = +1.97038864e-3 for the m = 1 scalar in RN-L1 normalization. For staggered fermions, μ_E^stag(m) = −½·μ_E^KG(2m) (`C4_V3_referee.md:19-25,48`).
   - "Jacobian = C3's anomaly in the vacuum" is the supervisor's same-family reading (`TESTS.md:1817-1820`).
   - Related, and refereed: ⟨E_c − H⟩_vac = −(ρ + p) for one band, which a cosmological constant cannot cancel (`C4_I3_referee.md:5-11`; `C4_W2_referee.md:13`).

### The costs (refereed numbers)

- **K1, time on the grid (Z⁴, ξ = 1).**
  - N_tune(Z⁴) = 11 = 3 masses + 8 kinetic forms. This is the exact operator codimension of linearized gauge restoration, counted after a separate cosmological-tadpole tuning.
  - It is corroborated by a one-loop example in which every coefficient is nonzero. The loop produces one non-EH direction, not eight basis-independent ones.
  - 5 = 2 + 3 is only the rank of the Euclidean-TT restriction, "not a proved physical two-helicity floor" (`C4_K1_referee.md:9,15`).
  - Scope: "Saying P0's old '2' is globally incomplete is too broad" (`C4_K1_referee_full.md:146-148`).
- **F2 and E2, continuous time (Z³ × ℝ, non-compact naive/staggered QED).**
  - At one loop, c_e − c_γ = −8.55e-3 at α = 1/137. That allows photon decay above 7.8 MeV and exceeds the 1.4 PeV survival bound by 3.2e16. One relative-speed counterterm must be tuned to about 3e-17 of its natural loop size (`C4_F2_referee.md:62`).
  - At ξ = 1, hypercubic symmetry removes the split; ξ = 2 gives Δ = −10.26 (in units of e²/16π²).
  - Running reaches only 7.34e-3 at 1.4 PeV (`C4_E2_referee.md:19`).
- **V3, free matter alone.**
  - It produces P0's E_g shear coefficient. The coefficient is not a cosmological constant: √g·Λ enters E_g and T_2g equally.
  - Removing it needs one of: an E_g counterterm, which is P0's tuning; a selected momentum symbol, which is a tuning; or the vacuum-referenced subtraction R₀, which "enforces that result by definition" (`C4_V3_referee.md:27-29`; `C4_V2_referee.md:23`).
- **Preferred-slicing costs.**
  - Cubic-only gravity: six mass invariants, "requiring additional relations beyond P0". The static model shows two TT suppressions, one determinant cancellation and a Cassini-level ratio. It does not show five P0-level tunings (`C4_F1_referee.md:11,17`).
  - The exactly repaired khronometric completion costs the relation m₄ = −a/2, and its λ > 1 branch stays unstable below k* = μ√(2/(λ−1)) (`C4_W3_referee.md:31`).
  - One-grid Pospelov–Shang subcases: M_* and L are each a few 1e9, and the TT k⁶ coefficient is 1e38–1e39. These are "legitimate hierarchies beyond P0, though not automatically precision tunings" (`C4_F3_referee.md:17`).
- **Dressing ansatz (W1).** In the h-linear, reflection-even quartic ansatz, the E and T2 cancellation loci are codimension-one spheres: one tuning per channel (`C4_W1_referee.md:22`).
- **Q-RI, coarse cells (I3).** Meeting P0 needs L* ≈ 1.18e25, a cutoff near 0.65 keV. A 10 TeV relativistic band caps L at 7.65e14. The two are incompatible, conditional on the linear-only TT completion (`C4_I3_referee.md:13`).
- **The continuous-time total (reading, not refereed).** 2 TT masses (P0) + at least 1 QED speed (F2) + 3 graviton-speed codimensions (R2, whose lane is INCONCLUSIVE) gives at least 6. That sum is the K1 worker's assembly (`C4_K1_report.md:191-194`).

### Correction to earlier records (dated 2026-10-11; recorded at `TESTS.md:1797-1802`)

**The corrected claim.** The RN L1 referee's statement that a determined unitary seagull cancels free matter's uniform-strain TT response "exactly" (`TESTS.md:851,884`; plain version §12, `SUMMARY.md:298`) holds only:
- for T_2g; or
- for the formal finite-box unitary with its boundary/seam terms kept.

For the local, translation-covariant coupling, it is **false in E_g**.

**Why.** The f-sum substitution silently kept an extensive boundary piece, so it never evaluated the local seagull (`C4_V3_referee.md:10-12,46`).

**The same correction applies to:**
- I3's "μ = 0 at every L";
- V1's "exact eigenstate for every h", which holds only with R₀;
- W1's premise "μ = 0 for free matter" (`TESTS.md:1348`).

### What remains open (with the referee's scope)

- **RI.**
  - Interacting or composite qubit matter beyond M1's class.
  - Separate complete Poincaré sectors that do not interact (`C4_I1_referee.md:13`).
  - Nelson integrability, which is assumed.
  - Arbitrary finite networks, not shown to be fine lattices, and a universal Z_N (`C4_I2_referee.md:15`).
- **RM.** Non-first-moment generators (RB, pending); non-number-conserving embedded sectors in d ≥ 2; irrational centres; massless sectors; unbounded continuum finite-N sectors (`C4_M1_referee.md:15`).
- **RD.** General Herglotz momentum dependence; the all-orders 1D Fermi sea; singular or sonic vertices; universal Z = 0; dressed two-band crossings (`C4_D1_referee.md:17`); gauge-complete, strong-coupling and T > 0 dressing (`C4_D2_referee.md:9`).
- **RF and RF3.**
  - Non-realizability for all finite-band matter, and a separate gravitational UV scale (`C4_F1_referee.md:17`).
  - F2's realization C, and parity-odd dimension-3 terms, which only the chosen action's parity forbids (`C4_F2_referee.md:9,58`).
  - Other dimensional-transmutation mechanisms, and a dynamical khronon (R4), which remains an RF theory (`C4_F3_referee.md:11-13`).
- **RE.** Emergent diffeomorphism invariance, exact sum rules, gravitational fixed points, scale-separated matching (`C4_E1_referee.md:17`).
- **RW.**
  - The P₄ route, O(λ³) and quadratic dressings (`C4_W1_referee.md:20`).
  - The complete Dirac algorithm and the λ ≠ 1 kinetic structure (`C4_W2_referee.md:15`).
  - A window-compatible healthy region: none exhibited, and none excluded (`C4_W3_referee.md:29`).
- **RK2.**
  - Coupled reflection positivity.
  - K2's general no-go hypotheses: a compact smooth shell, a Wick-real translation symbol and a complete boost flow (`C4_K2_referee.md:11,15`).
  - K1 is not universal for every W(B4)-covariant stress.
- **RV.**
  - R and R₀ are not derived.
  - The O(λ³) feedback formula is conditional, with no X₂ computed.
  - The lapse coupling, i.e. the Eötvös observable, was not tested (`C4_V2_referee.md:17-19`).
  - QED beyond the analytic Coulomb-gauge A,E ansatz (`C4_V3_referee.md:44`).
- **RL.** Edgeless (Gaussian) sources, and the actual finite-source prefactor at 1 Gpc (`C4_RL4_referee.md`).
- **RB.** Patchwise or singular DSR; fully deformed non-first-moment algebras with extra constraints; non-Morse or touching bands.

**Against the registered expectations.**
- As expected: RI, RD and RM FAIL; K1 > 2; RF, RF3 and K2 INCONCLUSIVE (each registered as "FAIL or INCONCLUSIVE"); W1 a bounded FAIL.
- W2 was expected to FAIL; it is INCONCLUSIVE.
- RE was expected INCONCLUSIVE leaning FAIL; it is a bounded FAIL.
- RV3 was expected to PASS conditionally; it FAILs, on a free-matter term nobody registered.
- RL was expected to PASS in the mean; it is INCONCLUSIVE leaning FAIL.

Details and referee lines: `TESTS.md`, "Campaign C4".

**Late additions to §17 (21:30Z).**
- **X1 (unrefereed reading).** The 1e-19 m bar is the LHC Drell–Yan bound, and current collider bounds are tighter (≈ 4e-20 m). The event-route noise needs ℓ_k ≈ 4–7e-19 m. That is excluded if ℓ_k is shared with matter.
- **Y1 (referee: INCONCLUSIVE, strongly leaning FAIL).** The readout noise is not Huygens: light emitted earlier also adds noise. The relevant scale is therefore the source's emission history, not its coherence length. At the photon's collider-bounded ℓ_k, that is about 4.5e4 variance e-folds per second of observing a source at 1 Gpc. What is still missing is the fraction of that noise falling in the observing band, plus a finite-distance normalization.

## 18. Lane RZ: does the event-route noise land in real observing bands? (owner, 2026-10-11)

**In plain words: yes, enough to rule the route out.**
- The noise is not tied to the light's own frequency. Each random spacetime event re-emits the passing light as an instant flash, so the noise is spread evenly across all frequencies.
- Only a tiny slice falls in a real telescope band, about e^{-110} to e^{-147}. But the noise grows by more than e^{45,000} for a source at 1 Gpc that has been shining for just one second.
- So lensed quasars and radio sources would be drowned in noise.

Refereed result: FAIL at the controlled level, bounded to the scalar readout and to sources that switch on at a definite time. Combined with RL2 (lensing correct on average) and RL4 (noise growth proved), the random-events substrate with a shared non-locality scale is excluded by observation.

Two items stay open: sources with no definite switch-on, and a fully proved transfer from the scalar model to real photons.

Details: `TESTS.md`, "Lane RZ results".

## 19. Lane RV4: can a principle remove the free shear mass? (owner, 2026-10-11)

**In plain words: no principle found. Refereed FAIL, bounded.**
- **Choosing the grid's momentum.** No choice protects both shear modes. Axis hopping protects one; body-diagonal hopping protects the other.
- **Long-range (SLAC) momentum** makes it worse, not better.
- **Tuning** can cancel both modes at a single mass, but the cancellation drifts as the mass changes.
- **A density-of-states-preserving term.** One genuine local term exists that keeps the spectrum unchanged under strain and so removes the shear mass. But it works only because it imposes that invariance directly. It is not unique, and nothing in the axioms requires it. That makes it the R₀ rule in operator form, not a derivation.

**Status.** The E_g shear mass from free local matter stands. Removing it costs a tuning or an imposed rule.

**Still open.** Field-dependent gauge completions with non-uniform strain, and multi-band matter.

## 20. Lane RFW: does letting the gauge rules depend on the fields help? (owner, 2026-10-12)

**In plain words: no, within the classes tested.** Refereed FAIL, bounded.
- **The fix tried.** Letting gravity's gauge transformations depend on the metric and matter fields, the way GR's own nonlinear transformations do.
- **Why it fails.** It does not remove the boost obstruction on the grid. The obstruction is a single factor, cos k, that lattice momenta carry and continuum momenta don't. The field-dependent corrections depend on the graviton's momentum. The defect depends on the matter's momentum. So they cannot cancel.
- **The two other ways out:**
  - Absorbing the defect with new gauge fields needs an endless tower of them.
  - Adding compensating fields removes the obstruction, but then nothing fixes the shear masses.

**Still open:**
- changing the leading generators themselves;
- multi-band matter;
- quasi-local "perfect" actions.

## 21. Campaign C5, round 1: what the observations force on the rules (2026-10-12)

**In plain words** (referee-checked unless noted):
- **One light speed for all matter.** This forces the law to single out no spacetime direction that particles can feel. A hypercubic Euclidean grid does this for ordinary matter. The axioms' 3D grid with separate time does not, so it needs each speed difference tuned. The F2 example needs about 3 parts in 10¹⁷.
- **A universal graviton** needs momentum to be exactly conserved for incoming and outgoing particles. Exact continuous translations are impossible with finitely many states tied to each site. That is proved in bounded forms.
- **Gravity treats everything alike.** On a grid, a body falls with acceleration β∇Φ, where β is the curvature of its band. So all species must share one β, which is the "one light cone" condition seen from gravity's side.
- **The vacuum barely gravitates.** Cancelling its energy without tuning requires exactly matched boson and fermion spectra, which observation excludes. A qubit site can't carry both a boson and a fermion. A lattice supercharge (Fendley–Schoutens–de Boer) is a real but costly escape.
- **Interference and records.** Any record that learns "which way" degrades interference. So records must be rare, coarse, or copies of what the environment already knows. "Records copy, never measure" is a sufficient policy, not a proved necessity.
- **The event substrate.** Making it a quantum superposition doesn't remove the lensing noise in the plain version (proved). Exotic versions are still open.

**Three mutually exclusive rule sets remain:**
- **A:** a continuum with discreteness only in records.
- **B:** a Euclidean 4D grid that is hypercubic throughout.
- **C:** keep the 3D grid and tune.

None of them yet produces the graviton or explains Λ. Round 2 tests what decides between them.

## 22. Campaign C5, rounds 2–3: a Lorentz-invariant random grid (2026-10-12)

**In plain words** (referee-checked unless noted):
- **A grid that is random in its frame.** Take a crystal and rotate and boost it into a random frame. This "Lorentz-random lattice" is Lorentz-invariant on average, yet each copy is a genuine crystal. Within the low-energy band, waves on it cannot scatter off the grid at all. That fixes the lensing noise that killed Poisson sprinkling.
- **Gravity on it is cheaper, but not free.** With the Z⁴ grid, a massless graviton needed 11 separate cancellations. On the random-frame grid it needs 5, assuming the effective law exists. The two shear masses become one, and the graviton automatically travels on the matter light cone. One tuning remains: the graviton's mass is not forced to zero.
- **What is not yet built.** Nobody has shown that a single copy of the grid has a well-behaved long-distance law.
  - The usual random-sprinkling d'Alembertian gives the wrong answer on it.
  - A single copy differs slightly from the average, with a smooth, direction-dependent bias. Whether that bias builds up over long paths is open. Round 4 tests both points and their observational size.
- **The plain Z⁴ grid, ruled out in a narrow sense.** If ordinary particles on it are to carry an exact gravitational charge, each particle must have infinitely many internal states (R2-1, bounded). So in that sense the plain Z⁴ grid collapses toward set A.
- **Set A's gravity.** If records are sudden and real, gravity has to respond to them.
  - **E3** is the one explicit route that survives the checks: the records are definite configurations, guided along a preferred time slicing. The slicing is the price.
  - The others (metric jumps, classical-quantum gravity, dressed collapse, reservoirs) are open.
  - The simplest classical-quantum version is excluded by 32 orders of magnitude. *(Corrected 2026-10-12, R6-4 referee: that bound came from an invalid step in the published paper and falls. Only unsmeared point-particle coupling is excluded; gravity smeared over 1e-10 to 5e-6 m survives. See §23.)*
- **Also settled in round 2:**
  - A positive local Euclidean weight gives the wrong light bending (γ ≤ ½).
  - Snyder's curved momentum space cannot couple to a graviton.
  - Reflection positivity plus strict permanence of records forbids ongoing record formation, for one class of rules.

## 23. Campaign C5, rounds 4–7: what broke and what held (2026-10-12)

**In plain words** (referee-checked unless noted):

**First positive result against the boost wall.**
- A lattice law can carry relativity exactly for every momentum inside a "box", up to a fixed boost limit (R7-1, PASS WITH SCOPE). On a Planck grid that limit is about rapidity 45 for a proton, far beyond any cosmic ray.
- The trick is to make the energy exactly √(m² + k²) inside the box and bend it back smoothly outside. Couplings then fall faster than any power, but not exponentially.
- It escapes every earlier no-go by dropping one of their assumptions:
  - relativity on all momenta;
  - boosts of any size;
  - analytic bands.
- **Not yet shown:**
  - interacting particles (the two-body version has errors to repair);
  - particle creation and loops;
  - gravity's local constraints.
- **It costs a universality problem.** The edge modes that carry the lattice's anomaly cannot be kept from gravitating.

**Exact momentum works for fermions, not yet for qubits.**
- A fermion law on a 2D grid conserves an exactly additive momentum in genuine collisions (R6-1). This is SUGGESTED overall, because the fixed class asked for one qubit per site and fermions compose differently.
- **DERIVED in every dimension:** no finite-range qubit rule can be a continuous version, or a root, of the one-site shift.

**Records as the classical metric survive.** Gravity that stays classical, sourced by smeared mass density, fits every lab bound for smearing lengths between about 1e-10 and 5e-6 m (R6-4, VIABLE in its class). The published "32 orders of magnitude" exclusion came from an invalid step and falls. The prices are:
- no graviton;
- a Newtonian-only theory;
- a preferred time slicing;
- built-in decoherence and heating.

**The Lorentz-random lattice is losing.**
- A single copy has no long-distance law from finite rules (R4-1). The natural infinite rules fail too (R5-2), and particles made at single sites carry no momentum (R4-2, R5-1).
- Putting the frame in superposition only helps if the frame is declared unobservable (R5-5).
- Its event count fluctuates too little to give Sorkin's Λ: the fluctuation comes out too large, about 1e30 (R6-3).

**Λ.**
- Nothing in any rule set makes its average zero without tuning (R5-3).
- The original sequestering rule would need a strongly curved universe.
- "Records form until frozen" leaves the vacuum energy as a free constant.

**Producing the graviton.** No set has a mechanism yet (R6-2: all OPEN). Holographic substrates help only for negative Λ, or remain unbuilt in 4D (R7-2).

## 24. Campaign C5, rounds 8–9: how far the "box" route goes (2026-10-12)

**In plain words** (referee-checked unless noted). The box route keeps the 3D grid but gives each particle exactly relativistic energy for momenta inside a box (R7-1).

**What holds.**
- **Two interacting particles.** The repaired law keeps exact relativity in 1D, and in 2D with rotations (R8-1).
- **A correction to an earlier referee.** It had said a prefactor must be ¼; that was a convention mistake, and the original ½ is right.
- **Bound bodies fall like everything else.** With a stress tensor that puts the binding energy at the pair's centre, a bound body of any binding falls at exactly the relativistic rate inside the box. This is shown in 1D (R9-2). In 2D with spin the worker reports the same (R9-10, referee pending).
- **It can live on plain qubits.** One qubit per site carries the free box law exactly, in the sector with no vortices (R9-5). Vortices sit still in the lattice frame, and the extra term needed to keep them out is not proved enough for every configuration.

**What breaks.**
- **The grid's leftover anomaly lives at the edge, outside the box.** Over any periodic band the "boost anomaly" averages to minus one.
  - Inside the box it is zero, so outside it is not.
  - Edge quanta fall the wrong way (R8-2, Theorem E).
- **Light.** Gauge invariance forces the photon to couple to the edge with full charge (R8-5). At one loop the photon and the electron then end up on different light cones, by as much as on a plain lattice.
  - Rotating the charge frame or choosing Wilson-line paths does not help in the 17 laws tried, and every rotated law was worse (R9-8, worker; referee pending).
- **The graviton.** Given its own box, it propagates at exactly light speed at tree level. Once matter loops can create pairs, its speed shift is an average of the same edge anomaly (R9-9, Theorem T, confirmed). Whether the coupling can be fixed to remove it is open.
- **The literal box law is excluded.** Each charged particle would have 7 extra copies of the same mass, which adds about 590 MeV to the Z width (R9-1).
- **Loops in general.** Point vertices bring the light-speed difference back (R7-5). Vertices built from invariant masses fix one loop. At two loops they close only in a version that is not confined to the box (R8-4, R9-7).

**Set A (records as a classical metric).**
- The Newtonian version survives for smearing lengths between about 1e-10 and 5e-6 m (R6-4).
- Relativistic versions fail in their simplest forms (R8-3, R9-4); correlated-noise and preferred-frame versions stay open.

**The picture now.**
- The box gives exact relativity to matter, including bound bodies.
- But the grid's anomaly does not go away. It moves to the edge, and gauge fields and gravity, through their loops, carry it back.
- Fixing that seems to need either per-observable tunings or an edge that isn't periodic (an infinite tower, i.e. set A). R10-1 tests this directly.

## 25. Campaign C5, rounds 10–12: the walls, located (2026-10-12)

**In plain words** (referee-checked unless noted).

**Matter in the box behaves as GR says.**
- Bound spinning bodies in a curved field have:
  - no internal stress at rest;
  - the same light bending whatever their binding;
  - geodetic precession of 3/2 and the right frame dragging (R11-4).
- Only the body's quadrupole is left free.

**The leftover lattice anomaly lives at the edge, and loops bring it back.**
- **Pairing is necessary.** Cancelling it across a range of masses needs bosons and fermions to cancel each other (R11-1).
- **It is not sufficient.** Pairing fixes the photon's speed but not the electron's (R10-1).
- **Lattice supersymmetry has not fixed the split.**
  - In the simplest class the photon gets doublers (R10-5).
  - A doubler-free photon multiplet exists, but its Hamiltonian is long-range (R12-3).
  - A single supercharge does not set the electron/photon speed ratio.
- **The split between the electron's and the photon's light cones is the wall no route has crossed without tuning.**

**Producing the graviton from qubits.**
- With exact constraints on finite sites, its energy grows like k³, not k (R11-2), so it can't move at light speed.
- Strongly coupled phases are the only window left. No controlled regime works (R12-5, worker).

**Λ.**
- **On a fixed grid the vacuum always pushes outward** (w ≥ 0). Flat space needs two tunings (R11-3).
- **Fixed-site grids cannot expand.** Creating sites is forced, at three times the expansion rate (R12-2).
- **A rule that reads only time changes of energy** gives zero Λ without tuning, but only in idealized uniform settings, and it makes a true Λ invisible (R12-2, OPEN).
- **Set A's records as a conserved charge** need the vacuum value pre-set to about 1 part in 1e55 (R10-4).

**Records as the classical metric (set A).**
- One theorem now covers every stationary version: matter noise and the metric record can't both stay finite near the light cone (R12-4).
- The two ways out:
  - the law has a start time (R11-5, OPEN);
  - gravitational waves are slightly damped, at about the Hubble rate (R12-7, worker OPEN).

  Both pass the stated observations. Both carry the same unresolved near-cone energy budget.

**Set B with box symbols** loses reflection positivity (R10-2).

## 26. Campaign C5, rounds 13–15: subclass walls, a causal repair, and a FAIL for the global clock (2026-10-12)

**In plain words.** Referee-checked unless marked; S17 is the synthesis at `agents/C5_S17_synthesis.md`.

**The electron–photon split: every named route stopped, each in its own subclass.**
- **Literal-edge class (R13-7).** The split cannot vanish over any range of masses. That edge is already excluded by the Z width, though.
- **Exact lattice SUSY (R13-1).** It cannot hold in the class with C¹ one-body band momentum.
- **The doubler-free photon multiplet (R13-4).** It needs a physical 1/r interaction.
- **Still open:** Wilson edges, and dressed or infinite-flavour momentum.
- **Cheapest price: one tuned number.** "One is enough for all light particles" is a worker reading. R16-2 tests it.

**The graviton is still not produced.** Three more families are closed:
- plain six-pair tensors (R13-2);
- the same with position–momentum mixing (R14-4);
- extra hidden fields: two graviton modes force at least four massless modes (R15-3).

What is left:
- discontinuous or non-local rules;
- exact constraints with indefinite energy;
- strongly coupled phases.

At strong coupling (R15-5, worker), real-valued fields give exactly the two modes, but qubits give energy growing like k³ at every finite order. The deciding computation is non-perturbative and has not been done.

**The box laws used before moved faster than light at the grid scale (R13-4).** A slower-than-light box keeps every matter result (R14-1). On such an edge, one shape choice cancels the shear term per mass, or to O((ma)²) for a common setting (R14-3).

**Set A, gravity's random kicks.**
- **The start-time route.** Its literal kernel drags the double pulsar and is excluded by at least 11 orders of magnitude (R13-6). A signed kernel repairs it.
- **The leak route.** It drags too. That limits the leak to a few per cent of the Hubble rate (R14-2).
- **Both are OPEN, and they tie.**
- **Spin-2 version of the start-time route (R15-2): OPEN.** The start time matters only for the graviton waves. The large energy overshoot found there counts only if non-radiating noise also gravitates, which is unproven.

**Λ.**
- **The CMC mechanism (R14-5).** The only smooth way to soak up vacuum changes with these readers is to make lattice time a global CMC time.
- **It signals faster than light (R15-1: FAIL).** Whenever it is active, a local push changes the density everywhere at once. The referee ruled that a global time ordering does not save it.
- **The readers (R15-4, R15-6, workers).**
  - A regular reader does handle phase transitions and lumps.
  - No positive linear reader tracks DESI's phantom-like dark energy.
  - Only a nonlinear running-minimum reader keeps the clock's variable safe in sign, and only in a simplified class of histories.
