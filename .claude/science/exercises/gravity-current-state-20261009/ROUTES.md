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
