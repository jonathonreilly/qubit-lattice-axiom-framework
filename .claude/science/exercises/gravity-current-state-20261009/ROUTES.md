# Steps 4, 6 and 7: routes, kill verdicts and ranking

**Step 4 inputs.** Four independent route agents, all Claude Opus 5.5 at extra-high effort:
- R1, condensed matter;
- R2, discrete quantum gravity;
- R3, the exact price;
- R4, misframing.

Their full texts are in `agents/`. They are deduplicated below into families, by object, mechanism and terminal obligation. The supervisor's own pre-registered thread is in `agents/supervisor_thread.md`, as routes C1–C4.

## Step 4: route families

| ID | Family (object; mechanism; terminal obligation) | Source agents | Premise it drops or changes | What you would have to believe | First artifact | Status before kills |
|---|---|---|---|---|---|---|
| **F1a** | **Frozen pattern-free sites with neighbours re-chosen from the current metric.** Object: E(g) on a Poisson–Delaunay or proper-distance complex. Mechanism: the site set's law is SL(3)-invariant, so E[F(X,g)] = E[F(X,δ)] (R1 Lemma L; R2 Lemma A). Obligation: one light cone and no per-configuration TT noise | R1 Route 1; R2 Route 1 | Lattice's site set Z³ becomes a random point set with continuous positions | That self-averaging suffices: the mean is zero, while the fluctuations are a random graviton mass | Mean CHECKED to be 0 in 2D and 3D (R1 and R2). **R3: per-configuration white-noise σ·√N is constant (0.035–0.13 per site), giving a Born mean free path of 0.2–300 l_P** | wounded by R3's fluctuation check |
| **F1b** | **Flowing sites: a quantum liquid vacuum with mobile, continuous positions.** Mechanism: the exact intertwiner x → g^{1/2}x, so the stiffness is zero in every configuration (R3 L-b). Obligation: a graviton kinetic term, a conserved stress and one light cone on a fluid | R3 Route 1; supervisor C1 | Lattice's point set becomes mobile sites; S4 becomes a liquid; positions are extra continuous variables beyond M₂(C) | That the vacuum is a quantum liquid, and that the fluid's rest frame and its sound and vector modes are harmless | A mobile-site liquid against its crystal, both at ground-state E″ (1–2 days) | survives step 4; to be killed |
| **F2** | **Smooth proper-distance kernels on fixed Z³.** Mechanism: image overlap at the zone face gives a stiffness of about 0.35·e^(−π²σ²). Obligation: a reflection-positive regulator with one protected light cone | R2 Route 3 | S7 only; no axiom | That positivity and the light cone can be kept while the stiffness falls exponentially | **The one-loop speed split with a smooth spatial kernel and continuous time** (hours) | trilemma: wounded |
| **F3** | **Keep the grid and pay in vacuum energy:** two tuned counterterms; SUSY or Q-exactness; frustration-free; self-tuning | R3 Route 2; R4 Item 1; R1 Route 2; supervisor C3 | S6 or H2 | One of: two tunings at about 1e-98; SUSY unbroken down to about 0.2–1 keV; z ≥ 2 vacua; relaxation | Checks done: self-tuning leaves (k_F a)²; SUSY misses by about 9 orders in Δ; frustration-free systems have z ≥ 2 | **dead as escapes.** The two tunings remain as a price |
| **F4** | **A vacuum that breaks Z³ on the fixed grid** (incommensurate sliding density wave) | R4 Item 2 (Lemma R) | S4 | That some Z³-breaking realized state is shear-free | A 2D incommensurate vs commensurate density-wave toy (2–3 days) | expected FAIL; low rank |
| **F5** | **Wetterich position-blind actions on fixed Z³** | R2 Route 2 | S7 | — | C3: the Dirac sea falls along every shear (Lemma B2) | **killed** (mean field) |
| **F6** | **Emergent gauge redundancy** (rank-2 / fracton Gauss law) | R1 table | S2, S5 | That matter's charge equals its momentum | — | **blocked-equivalent** to K3a's exact interacting stress |
| **F7** | **A clever fixed graph** (pentamode) | R3 Route 3 | S7 | Matter blind to the shear | Done: an angle datum restores the stiffness | **dead** (universal coupling sees all 5 channels) |

**The reframe offered as a cheaper question (R2): the regulator trilemma.** Can any reflection-positive regulator keep **both** of these?
- (a) a single light cone protected by a symmetry linking time and space;
- (b) zero TT stiffness from a shape symmetry, SL(3)-invariance in law or per configuration.

**Lemma R (R4) and its twin L-b (R3), stated together.** For an interacting, translation-covariant law on Z³ with a translation-invariant vacuum and discrete translations, no continuous unitary family can implement a shear, because only GL(3,Z) points are reachable. So the strain is always felt. **What the stiffness face rests on is the fixed site set with discrete translations, not adjacency.**

## Step 6: kill verdicts

Every kill agent was Claude Opus 5.5 at xhigh. Every no-go was refereed by codex gpt-5.6-sol xhigh. Full texts are in `agents/kill_*.md` and `agents/kill_*_referee.md`.

| Route | Kill verdict | Referee | What survives |
|---|---|---|---|
| F1a, frozen random sites | **DEAD as a separate route** | CONFIRMED WITH CORRECTIONS. Ensemble-only protection is not viable: per realization there is a random TT tadpole and stiffness with S(0) > 0 that is IR-relevant beyond 25–35a, and no cutoff window exists. The chaos-expansion no-go was overstated, so mobility is sufficient but not proven necessary | Only an **exact realization-wise identity** (a coboundary or conservation identity, or a hyperuniform stress), which would be a new mechanism |
| F1b, a flowing liquid vacuum | **DEAD as an untuned escape** | CONFIRMED WITH CORRECTIONS. A flat background forces ρ + p = 0, which removes the phonon kinetic term (a degenerate EFT). The preferred frame gives dimension-4 Lorentz violation, with Ξ ≥ 1 for any regulator shape. The displacement is a vector, not the mediator. Mobile positions exceed a finite qubit. "SUSY is the only exception" was false | R3's lemma (a liquid removes m₂ for a supplied metric). **Untested different architectures:** Lorentz-covariant spacetime-event substrates, number-changing media (created sites), extra sectors |
| F2, smooth kernels on Z³ | DEAD (gauge paths give a power law; locality needs about 107-site couplings; Lemma N gives a positivity floor) | **NOT CONFIRMED as universal.** The specific Gaussian package is badly obstructed: a Euclidean-time Gaussian breaks positivity; the massless Dirac has corner zeros and a large near-zero region; the Wilson cure costs chiral mass protection; truncation needs about 5e6 couplings per site; the two gauge-path families keep power-law residuals. **Not established:** a no-go for every reflection-positive, gauge-covariant, locally generated or perfect-action construction. Lemma N's bound is correct, but its equality case is incomplete (the pure-b case), its spatial transfer needs a time-to-space interchange symmetry of the full inverse propagator, and **"face floor ⇒ TT stiffness floor" is an open lemma** | **WOUNDED.** Open: fixed-point (perfect) actions with localized transporters; divergence-free transporter currents; improved or multiscale stencils. **A 4D hypercubic variant keeps T1's one-cone protection** |
| F3, keep the grid and pay | dead as an escape (step 4) | — | **The price: two tuned counterterms**, about 1e-98 each |
| F4, a vacuum that breaks Z³ | not killed separately: expected FAIL, untested | — | Low rank (Lemma R loophole) |
| F5, Wetterich; F6, emergent gauge; F7, pentamode | killed or blocked in step 4 | — | — |

**T1 (step 8, run alongside the kill round; refereed).**
- **Sufficient protection:** one light cone is protected by the hypercubic time–space regulator (Z⁴ residual 2e-9, by symmetry).
- **Fails:** a shape-fixed smooth spatial regulator with continuous time splits fermion and scalar speeds by about −0.70 g²/16π², independent of the cutoff scale and dependent on its shape.
- **Not shown:** that a time lattice is *necessary*.

## Step 7: ranking

The ranking is by what a route would change, divided by what it costs to find out.

| Rank | Route | Family | Premise challenged | What you would have to believe | Terminal obligation | Strength vs target | Kill verdict | Cost | First artifact | What it changes | Stop or reopen |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Write the price down once** (a refereed note) | price | none | nothing new | a lemma bundle (below) | weaker (a statement of price) | — | 1–2 days plus a referee | a note bundling T0, R3's surface lemma, Lemma R, the fluid lemma (R4, OUTSIDE_VIEW), Lemma A/L with F1a's realization noise, Lemma N, T1 and K3a″/W1 | It turns about 15 results into one owner-level statement. On a regulator with fixed sites, discrete translations, positivity and a hypercubic light-cone protection, the vacuum's TT modulus is unprotected. Every tested way to protect it loses one of the other three | — |
| 2 | ~~Keep the grid: a 4D hypercubic, reflection-positive, smooth-kernel or perfect-action regulator~~ **closed by T2** (a bounded FAIL, refereed): the best RP family has a σ⁻² floor (6.45e-4 at σ = 10). The only exact zero is a free-level relabelling, outside the contract and blocked by Lemma R for ordinary interacting laws | F2 on Z⁴ | S7 | — | — | — | **T2 FAIL (bounded)** | done | T2 | Keeping the grid now costs the tuning, unless a non-ordinary interacting law evades Lemma R | reopen only for a new mechanism |
| 3 | **A spacetime-event substrate** (a Lorentz-covariant sprinkling; causal-set-like). This is the one architecture no agent killed | changes Lattice (and the nearest-neighbour reading) | L1, plus Admissibility's "nearest neighbour" | That a law over Poisson-sprinkled spacetime events can give shape-blindness and one light cone in law, and suppress per-realization noise | (A) zero TT noise per realization, (B) one cone, (C) a local enough rule | stronger than the target (unsolved continuum limit) | not killed. Known costs: no finite-valency Lorentz-invariant neighbour rule (Bombelli–Henson–Sorkin), realization noise as in F1a | days | the per-realization TT stiffness noise of a 3+1 Poisson sprinkling with a causal-set d'Alembertian. **PASS:** S(0) = 0 and no tadpole. **FAIL:** S(0) > 0, as in F1a | It is the only route left with both protections in law. **Reading:** "records form as events at random places and times" is this substrate | stop if S(0) > 0 |
| 4 | **Name a mediator mechanism, or stop** | emergent graviton (G) | S2, S5 | That a mechanism produces a massless helicity-2 mode with an exact protecting constraint | the graviton itself | target-equivalent | none of the tested routes produce a mediator: F1b's displacement is a vector, and records carry scalars and vectors (FR3) | open-ended | none known | everything, if found | **do not spend without a named mechanism** (as 09-29 also concluded) |

## Follow-up at the owner's request (2026-10-09): E1–E3

The tests and referee verdicts are in `TESTS.md`.

- **E2 (sites missing) and E3 (quasicrystal, hyperuniform set, growing random set): FAIL (refereed).** This retires the frozen-spatial-substrate family, F9 in `APPROACH_REGISTRY.md`. Lemma P, corrected by the referee, is the structural reason for the ensemble-symmetry case. The one reopen condition is an exact realization-wise coboundary or conservation identity for the stress.
- **E1 (records as spacetime events, rank 3 above): INCONCLUSIVE, leaning FAIL (refereed).**
  - Mean shape-blindness and one mean cone hold exactly. This is the only tested substrate where both come from symmetry.
  - The row noise gain grows with the size of the past (EXACT), and the standard BD evolution is exponentially unstable at the tested ε.
  - The exclusion at physical scales needs an exponent extrapolated over about 60 decades, so the fixed reading gives INCONCLUSIVE.
  - **Rank 3 stays open** but is wounded. Its next test would be a dynamics that avoids the signed-weight noise gain (a stable generalized d'Alembertian, or link path sums), or a direct small-ε exponent.
