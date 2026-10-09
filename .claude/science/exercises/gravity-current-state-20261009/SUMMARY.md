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
1. **A tuned cancellation of two vacuum numbers** (the two shear stiffnesses), to about one part in 10⁹⁸, a second cosmological-constant-sized tuning. This is checked arithmetic.
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
