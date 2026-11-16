lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-17T03:59Z

# gap-measured-assumptions-opus (queue row 1063): first-principles and assumptions exercise from measured physics

Branch `claude/ym4d-hard-route`, pin `a3b40f2fa`. Started 2026-11-16 15:59Z (date -u). Worker: Claude Opus 5.5, high
reasoning, Mac mini worker 1. Exercise skill: `qubit-lattice-axiom-framework` main commit `8b11ae2bb9`,
`docs/ai_methodology/skills/exercise/SKILL.md` and its reference files, fetched into a /tmp scratch folder.

Rule of this row: start from what is measured, not from any target. No lane file (parts/, library/, FINISH.md beyond
row 1063, GOAL.md) is opened before step 5, except row 1064's reading `library/prior/gap-measured-read-luna.md` when
present (absent at 15:59Z). Marks for data: MEASURED (source, error), DERIVED, BELIEF, CONTESTED. Marks for claims:
PROVED, ARGUED, OPEN, FAILS. Measured data guide or refute; they never discharge a proof step.

## Plan (at most eight steps; one step per response, appended before the next)

1. Fetch the exercise skill and its references; do skill step 0. Collect the measured record (experiment; lattice
   SU(2) then SU(3)) with sources and errors, from memory checked against fetched public sources.
2. Skill steps 1-3: what the measurements say the gap is, the scale and the bare-coupling regime where it is
   generated, and which mechanisms the data favour, with firmness.
3. Skill step 4: the assumption set (at least forty, six groups), each with what the record supports, contradicts or
   leaves open, what follows if it is wrong, and the Elon pass (who requires it, can it be deleted).
4. Skill step 5: read `parts/gap.md`, `library/gap-dichotomy.md`, `library/gap-wall-assumptions-opus.md`,
   `library/gap-direction3-max.md`; agreement and disagreement of the lane's route with the measured mechanism; is the
   lane's band where the measured crossover sits.
5. Skill step 6: re-judge discard tests and set-aside methods against the measured record.
6. Skill step 7: routes suggested by the measured mechanism; fast kills with the tests on file (grep open-core and
   FINISH rows first).
7. Skill step 8: real attempts on the best one or two.
8. Skill step 9 and close: summary table, the five assumptions most questioned and what each opens, RESULT line.

## Status log

- 15:59Z file created with plan. Memory free 72 percent.

## Header (skill output rules)

- Written by: Anthropic, Claude Opus 5.5, reasoning effort high, Mac mini worker 1 session of row 1063. No subagents.
- Commit: `a3b40f2fa` on `claude/ym4d-hard-route`. Date 2026-11-16.
- **Nothing in this file is checked by another model.**
- Skill source: `exercise/SKILL.md` at `qubit-lattice-axiom-framework` main `8b11ae2bb9`, with
  `proof-search-governance.md`, `assumption-import-audit.md`, `RULES.md`, `procedures/research.md`,
  `procedures/check.md`, `SKILL_FRESHNESS_CHECK.md`, `PRIMITIVE_REGISTRY_CHECK.md`, `review-loop/SKILL.md`,
  `CONTROLLED_VOCABULARY.md`, `MINIMAL_AXIOMS_2026-06-29.md`, `SCALE_REFERENCE_PRIMITIVE_NOTE.md`, all fetched by raw
  URL into `/tmp/ym4d-1063-skill/`. Read in full: SKILL.md, proof-search-governance.md, RULES.md section 1. The others
  were fetched and are consulted only where a step names them (listed below when used).
- Replacement made (skill, "Framework Refresher Read"): this is a standalone proof target, so the framework refresher
  is replaced by the target contract. The row forbids opening GOAL.md before step 5, so steps 0-4 state the target
  from the row text and from the published Jaffe-Witten problem statement (recalled), and step 5 reads GOAL.md.
- What this run did not cover (kept current): see the list at the end of the status block.

## Status block

| Step | Done | Main result |
|---|---|---|
| 0 record located, closed list | yes (16:00Z) | closed list below; row 1064's reading absent at start |
| 1 measured record + wall twice | yes (16:05Z) | 33 measured items with sources; leading strong coupling off by 5x at beta 2.3 (L9) |
| 2-3 inventory, reasoning up (row's steps 1-3) | yes (16:06Z) | C1-C10: gap = 0++ at 3.78 sqrt(sigma); generated in the crossover band beta 2.2-2.4 next to a mixed-action critical end point |
| 4 assumptions table (>= 40, six groups, Elon pass) | yes (16:09Z) | 59 rows; top five: Wilson-axis band (c2+b3), strong coupling to the band (c4), no-transition premise (e4), small boxes (c6), gap via confinement (d2, e10) |
| 5 comparison with lane files | no | |
| 6 discard tests, set-aside methods | no | |
| 7 routes, kills | no | |
| 8 attempts | no | |
| 9 report, RESULT | no | |

Not covered so far: everything after step 0.

## Step 0: where the record is; what stays closed

Located by file name only (`ls library`, `ls library/prior`), no file opened.

**Open now.** The row 1063 text (FINISH.md line 1144); the skill files; the measured record (public sources fetched
by URL into `/tmp/ym4d-1063-meas/`); row 1064's `library/prior/gap-measured-read-luna.md` when it appears; statements
of published theorems (recalled, marked so).

**Closed until step 5.** `parts/gap.md`, `GOAL.md`, every other FINISH.md row, every `library/` file, in particular the
four the row names for step 5 (`gap-dichotomy.md`, `gap-wall-assumptions-opus.md` row 1052, `gap-direction3-max.md`
row 1051, `parts/gap.md`) and the earlier exercises and assumption passes found by name: `gap-assume-opus.md`,
`gap-wall-assume-max.md`, `gap-crux-exercise*-max.md` (four rounds and checks), `gap-flux-exercise.md`,
`gap-form-exercise.md`, `gap-shape-exercise-astra.md`, `gap-direction{,2,3}-max.md`, `gap-phys-seed.md`, and the
lane's literature record `library/prior/gap-lit-*.md` (about 40 files).

Literature (skill step 0): the lane has a literature record, but it is lane-shaped and closed until step 5 under the
row's rule. This run makes its own measured-physics search now (step 1) and reads only results from it before step 5.

## Step 1a: the measured record (sources fetched 16:00-16:04Z into `/tmp/ym4d-1063-meas/`)

Reading state of sources. INSPIRE API abstracts (arXiv API returned HTTP 429) for all items cited "abstract".
Athenodorou-Teper 2106.00364 (JHEP 12 (2021)) PDF read in part: Table 1 (SU(2) parameters), Table 12 (SU(2) flux
tubes), Table 15 (Lambda), Tables 34 and 38 (continuum and N = infinity glueball masses), Table 47 (topology), eq. (20)
and (22). Items marked "recalled" were not re-read in this run. Row 1064's reading was absent when this was written.
Physical units use sqrt(sigma) = 440 MeV, a convention (SUPPLIED), not a measurement of pure gauge theory.

Marks: MEASURED (source, error) | DERIVED (computed here from MEASURED items; a guide) | BELIEF | CONTESTED.

### Experiment (real QCD with quarks; pure Yang-Mills is never measured directly)

| # | Item | Mark | Source |
|---|---|---|---|
| E1 | No isolated fractional charge found: bulk-matter searches bound free quarks below about 1e-20 to 1e-22 per nucleon | MEASURED (null result; recalled) | Perl, Lee, Loomba, Annu. Rev. Nucl. Part. Sci. 59 (2009), recalled |
| E2 | Hadrons are colour singlets; the spectrum is meson/baryon multiplets | MEASURED | PDG (recalled) |
| E3 | Regge trajectories are near-linear in M^2 with slope alpha' about 0.88-0.9 GeV^-2 | MEASURED (recalled, error a few percent) | PDG / Chew-Frautschi plots, recalled |
| E4 | String reading of E3: sigma = 1/(2 pi alpha') gives sqrt(sigma) about 0.42-0.43 GeV | DERIVED from E3 under the BELIEF that light-quark Regge slopes are flux-tube tensions | |
| E5 | Bjorken scaling with logarithmic violations in deep inelastic scattering; free-field UV behaviour with log corrections | MEASURED (HERA, SLAC; recalled); THM for the UV behaviour: Gross-Wilczek PRL 30 (1973), Politzer (1973), abstract read | |
| E6 | Running coupling alpha_s(M_Z) = 0.1180(9), measured from tau decays (~1.8 GeV) to TeV jets, consistent with the 2-to-5-loop beta function | MEASURED (PDG 2024, recalled) | |
| E7 | Pomeron trajectory alpha(t) about 1.08 + 0.25 t in total cross sections; the 2++ glueball is often placed on it | MEASURED (fit) for the cross sections; CONTESTED for the glueball reading | Donnachie-Landshoff PLB 296 (1992), abstract |
| E8 | No state is established as a glueball. Scalar candidates f0(1500), f0(1710) (mixing with q-qbar disputed); X(2370) is 0-+ with M = 2395 +- 11 (+26 -94) MeV, > 11.7 sigma, "consistent with the lightest pseudoscalar glueball" | MEASURED (X(2370) mass and J^PC); CONTESTED (glueball identity) | BESIII PRL 132 (2024), 2312.05324, abstract |

### Lattice pure gauge theory, SU(2) Wilson action (beta = 4/g^2)

| # | Item | Mark | Source |
|---|---|---|---|
| L1 | Continuum glueball masses in units of sqrt(sigma): 0++ 3.781(23), 2++ 5.349(20), 0-+ 6.017(61), 0++* 6.126(38) | MEASURED | Athenodorou-Teper 2106.00364 Table 34 |
| L2 | Lattice data, beta : a sqrt(sigma) : a m_G : m_G/sqrt(sigma): 2.2986 : 0.36778(69) : 1.224(16) : 3.33; 2.3714 : 0.29023(50) : 1.025(12) : 3.53; 2.427 : 0.24013(41) : 0.8469(76) : 3.53; 2.509 : 0.18011(22) : 0.6563(56) : 3.64; 2.60 : 0.13283(30) : 0.5001(41) : 3.77; 2.70 : 0.09737(23) : 0.3652(35) : 3.75 | MEASURED (ratio column DERIVED) | same, Table 1 |
| L3 | Deconfinement: second order, 3D Ising class; beta_c(N_t = 4) = 2.2985(6); T_c/sqrt(sigma) = 0.69(2) (FHK), 0.7091(36) (LTW, recalled) | MEASURED | Engels-Fingberg-Weber NPB 332 (1990), Fingberg-Heller-Karsch NPB 392 (1993) hep-lat/9208012, abstracts; Lucini-Teper-Wenger hep-lat/0307017 |
| L4 | Lambda_MSbar/sqrt(sigma) = 0.5806(21)[570] (3-loop fit); sqrt(sigma)/Lambda_MSbar = 1.79(12) (FHK) | MEASURED (scheme conversion is perturbative, DERIVED) | AT Table 15; FHK abstract |
| L5 | Specific heat of the Wilson action has a sharp peak where the string tension crosses over from strong to weak coupling (near beta about 2.2), with rapid growth of correlation length and slowing down there | MEASURED (peak position near 2.2 recalled, not re-read) | Lautrup-Nauenberg PRL 45 (1980); Creutz PRD 21 (1980), abstracts |
| L6 | The peak is the shadow of a nearby critical end point: in the fundamental-adjoint plane the SO(3) and Z2 first-order lines merge and end at a critical point; on the Wilson axis there is no bulk transition | MEASURED (Monte Carlo; end-point coordinates not re-read) | Bhanot-Creutz PRD 24 (1981), abstract |
| L7 | Creutz's string tension at fixed physics: bare coupling falls logarithmically with cutoff, consistent with the perturbative RG; "coexistence of confinement and asymptotic freedom" | MEASURED (1980 precision) | Creutz PRD 21 (1980), abstract |
| L8 | Asymptotic scaling is violated in the measured window: a sqrt(sigma)/f_2loop(g^2) drifts 62.0 -> 45.2 over beta 2.30-2.70 (27 percent) with the bare coupling, 6.53 -> 5.39 with the boosted coupling g^2/<plaq>; the ratio m_G/sqrt(sigma) moves 3.33 -> 3.75 (scaling of ratios holds to about 3 percent from beta 2.5) | DERIVED (guide; `/tmp/ym4d-1063-meas/scaling.out`) from L2 | script `scripts/scaling.py` |
| L9 | Leading strong coupling (u = I_2(beta)/I_1(beta), sigma a^2 = -ln u, m a = -4 ln u) at beta 2.30 gives sigma a^2 = 0.736 against 0.135 measured, m a = 2.94 against 1.22: the leading strong-coupling term is off by a factor 5 in sigma and 2.4 in m at the coarsest scaling point | DERIVED (guide) from L2 | same script |
| L10 | Roughening: estimated beta_R for SU(N) in d = 4 lies in the crossover region where the string tension leaves the strong-coupling curve; beta_R(N) -> about 0.38 (in units g^2 N) as N -> infinity | ARGUED (strong-coupling series estimate), not a measurement | Munster-Weisz NPB 180 (1981), abstract |
| L11 | Long flux tubes: string formation over 2 fm, transverse profiles measured; static potential to high accuracy | MEASURED | Bali-Schilling-Schlichter PRD 51 (1995) hep-lat/9409005, abstract |
| L12 | Luscher term gamma/r with the bosonic-string coefficient (SU(3), also d = 3); transition from perturbative to string behaviour "at surprisingly small distances" | MEASURED | Luscher-Weisz JHEP 07 (2002) hep-lat/0207003, abstract |
| L13 | Excitations around static sources: three regimes (OPE, crossover below 2 fm, string-like at 2-3 fm with pi/R gaps and fine structure) | MEASURED (SU(3)) | Juge-Kuti-Morningstar PRL 90 (2003), abstract |
| L14 | Topological susceptibility chi^(1/4)/sqrt(sigma) = 0.4773(14) (SU(2)), 0.4196(35) (SU(3)) | MEASURED | AT Table 47 |
| L15 | Centre vortices (centre projection): piercing density is RG invariant, about 2 per fm^2 | MEASURED (gauge-fixed projection) | Langfeld-Reinhardt-Tennert PLB 419 (1998), abstract |
| L16 | Random-piercing reading of L15: independent Z2 piercings of density rho give W(A) = exp(-2 rho A), so sigma = 2 rho; rho = 2 fm^-2 gives sqrt(sigma) about 400 MeV | DERIVED (arithmetic) under the BELIEF that piercings are independent | |
| L17 | Removing centre vortices removes confinement and chiral breaking, topology becomes trivial | MEASURED (operation defined by gauge fixing); CONTESTED as "proving that center vortices are responsible" | de Forcrand-D'Elia PRL 82 (1999), abstract |
| L18 | Abelian (maximal abelian gauge) string tension / full = 0.92(4) at beta 2.5115; monopole part carries the abelian string tension; Gribov copies matter | MEASURED (gauge-fixed); mechanism CONTESTED | Bali-Bornyakov-Muller-Preussker-Schilling PRD 54 (1996), abstract |
| L19 | Landau-gauge gluon propagator finite and nonzero at p = 0 in d = 3, 4 (lattices to 27 fm^4), ghost not as enhanced as the scaling solution predicts (decoupling) | MEASURED (gauge-fixed); interpretation CONTESTED | Cucchieri-Mendes 0710.0412; Bogolubsky et al. PLB 676 (2009), abstracts |

### SU(3) for comparison, and large N

| # | Item | Mark | Source |
|---|---|---|---|
| S1 | SU(3) continuum 0++ 3.405(21), 2++ 4.894(22), 0-+ 5.276(45) sqrt(sigma); in GeV (r0 = 0.472(5) fm from QCD) 0++ about 1.5-1.7, 2++ about 2.2-2.4 | MEASURED (GeV conversion SUPPLIED) | AT Table 34, eq. (22); Morningstar-Peardon PRD 60 (1999), Chen et al. PRD 73 (2006), abstracts |
| S2 | Lambda_MSbar(SU(3)) = 263(4)[9] MeV via r0 | MEASURED with SUPPLIED r0 | AT eq. (22) |
| S3 | SU(3) deconfinement first order (weak), T_c/sqrt(sigma) = 0.6462(30) (recalled); first order for N >= 3, stronger with N; T_c/sqrt(sigma) = 0.596(4) + 0.453(30)/N^2 | MEASURED | LTW hep-lat/0307017, abstract |
| S4 | Large N: 0++ 3.072(14), 2++ 4.599(14), 0-+ 4.711(26) sqrt(sigma) at N = infinity; Lambda_MSbar/sqrt(sigma) = 0.5055(7)[250] + 0.306(12)/N^2; SU(2) is within about 20 percent of N = infinity for 0++ | MEASURED (extrapolated) | AT Table 38, eq. (20) |
| S5 | SU(3) Wilson action: a dip in the step function near beta 5.6 (bulk crossover, shadow of a fundamental-adjoint end point) | MEASURED (recalled, not re-read) | Bhanot-Creutz type studies; Heller (recalled, not fetched) |
| S6 | Perturbation in renormalized couplings works from beta 5.7 (SU(3)), bare-coupling perturbation fails there | MEASURED / ARGUED | Lepage-Mackenzie PRD 48 (1993) hep-lat/9209022, abstract |

## Step 1b: the wall, stated twice (before any lane file is opened)

**Plain version** (about 140 words). Physicists have a theory of the force that holds quarks together. With the quarks
removed, the theory has only force-carriers ("gluons"). Experiments and very large computer simulations agree that this
gluon-only world has no particle lighter than a definite minimum mass: the lightest "glueball" weighs about 3.8 times a
basic energy scale set by the strength of the force. Mathematicians want a proof that the theory exists in exact form
and that this minimum mass is above zero. It matters because it is the cleanest open test of whether our methods for
such theories are sound. What keeps happening: proofs work when the force is very strong or very weak on the grid used
to define the theory, but the mass appears in between, where neither tool works. Getting past it means a proof that
covers that in-between zone, or a proof that avoids needing it.
(Analogy, marked as such: two bridges are built from both banks and stop short of the middle of the river.)

The last three sentences are this run's reading of the row's phrase "the lane's band (order-one bare coupling)"; they
are a hypothesis about the lane's wall to be checked in step 5, not a quotation.

**Precise version** (recalled Jaffe-Witten statement; GOAL.md quoted in step 5). For a compact simple gauge group G
(the lane works with SU(2)), construct a quantum Yang-Mills theory on R^4 satisfying axioms at least as strong as
Wightman's (Euclidean: Osterwalder-Schrader, with reflection positivity, Euclidean invariance, regularity, clustering),
non-trivial, and prove a mass gap Delta > 0: the energy-momentum spectrum lies in {0} union [Delta, infinity),
equivalently gauge-invariant Euclidean correlations decay at least as exp(-Delta |x|) uniformly. Allowed premises: the
mathematics; owner rule (row 1063): no computer-assisted proof steps, Lean-formalizable only. Forbidden weakenings: a
gap on a fixed lattice only; a gap in finite volume only; a gap for a different action or a different group without a
proof that transfers. Outcomes that do not count: numerics, a continuum limit without a gap, a gap without the limit, a
gap whose constant depends on the cutoff and goes to zero.

**Blind check:** no fresh agent allowed (no subagents); the plain version is corrected in step 9 if step 5 shows it
misreads the lane's wall.

- 16:05Z step 1 written (record E1-E8, L1-L19, S1-S6; wall twice). Next: steps 2-3 of the row (what the data say the gap
  is, where it is generated, by what mechanism), as skill steps 2-3.

## Step 2: inventory (skill marks) beyond the measured record of step 1a

The measured items E1-E8, L1-L19, S1-S6 enter the inventory as BELIEF in the skill's sense (from physics and
numerics; usable in no proof step), each with its source and number above. Theorems below are all **recalled** (not
re-read in this run, proofs not checked here) unless a page is named.

| # | Item | Mark | Source | Standing, reading |
|---|---|---|---|---|
| T1 | Wilson lattice SU(N) theory on Z^4 with plaquette action is reflection positive; Osterwalder-Schrader reconstruction gives a transfer matrix and a Hilbert space with H >= 0 | THM | Osterwalder-Seiler, Ann. Phys. 110 (1978) | published; recalled |
| T2 | For beta small enough (strong coupling) the infinite-volume Wilson theory has a convergent cluster expansion, area law for Wilson loops and a positive mass gap | THM | Osterwalder-Seiler (1978); Seiler, LNP 159 (1982) | published; recalled |
| T3 | Mass gap at small beta by Bakry-Emery / log-Sobolev (any d, explicit beta range far below 1) | THM | Shen-Zhu-Zhu, CMP (2023), arXiv 2204.12737 | published; recalled (range not re-read here) |
| T4 | 4D compact U(1) lattice theory has a massless (Coulomb) phase at weak coupling: no mass gap there | THM | Guth PRD 21 (1980); Frohlich-Spencer CMP 83 (1982) | published; recalled |
| T5 | Ultraviolet stability: Balaban's block-spin RG gives bounds on the effective actions of 4D lattice YM uniform in the lattice spacing in finite volume, at small bare coupling | THM (as claimed in the series) | Balaban CMP 1984-1989 | published; recalled; known to stop at the scale where the running coupling is O(1) |
| T6 | Asymptotic freedom: the one-loop beta function coefficient b0 = 11N/(48 pi^2) > 0 | THM (perturbative) | Gross-Wilczek; Politzer (1973) | abstract read |
| T7 | Effective string theory: the Luscher term -pi(d-2)/(24 r) and the next universal terms are fixed by nonlinear Lorentz invariance of the long string | THM in effective field theory (not a theorem about YM) | Luscher-Symanzik-Weisz (1980); Aharony-Komargodski JHEP 05 (2013) | recalled |
| T8 | 2D YM is exactly solvable with a gap at every coupling; 3D and 4D are not | THM | Migdal (1975), Gross-Taylor, Sengupta | recalled |
| T9 | Clay statement: existence on R^4 + mass gap Delta > 0 for every compact simple G | DEF of the target | Jaffe-Witten, Clay problem description (2000) | recalled; GOAL.md in step 5 |
| T10 | Centre-vortex free energy (twisted boundary conditions, gauge invariant) decays exponentially in box size in the confined phase | BELIEF (MEASURED numerically; Kovacs-Tomboulis PRL 85 (2000), recalled); Tomboulis' 2007 proof claim of confinement from it is CONTESTED and not accepted | recalled |
| D1 | Units convention sqrt(sigma) = 440 MeV, r0 = 0.5 fm or 0.472 fm | SUPPLIED | | |

## Steps 2-3 of the row (skill step 3): reasoning up from the inventory only

**3.1 What follows at once.**

- (a) *What the gap is, measured.* In pure SU(2) the gap is the scalar glueball, Delta = m(0++) = 3.781(23) sqrt(sigma)
  (L1); the next states are 2++ at 1.41 Delta and 0-+ at 1.59 Delta (L1). With D1, Delta is about 1.66 GeV in SU(2),
  1.50 GeV in SU(3) (S1), 1.35 GeV at N = infinity (S4). Uses L1, S1, S4, D1. Mark: MEASURED ratios, SUPPLIED units.
- (b) *One scale.* Delta/sqrt(sigma) = 3.8, Delta/T_c = 5.3, Delta/Lambda_MSbar = 6.5, chi^(1/4)/sqrt(sigma) = 0.48
  (L1, L3, L4, L14). Gap, string tension, deconfinement and topology sit within one decade: the data show no
  separation of scales between "gap" and "confinement". DERIVED (ratios of MEASURED items).
- (c) *Where on the lattice.* The lattice spacing at which a equals one correlation length (a m_G = 1) is beta about
  2.37 (L2: a m_G = 1.025 at 2.3714); a m_G = 1.22 at beta 2.30. The specific-heat peak and the strong-to-weak
  crossover of the string tension sit at beta about 2.2 (L5). So the gap scale meets the lattice scale exactly in the
  crossover band beta in about [2.1, 2.4], g^2 = 4/beta in about [1.7, 1.9]. DERIVED from L2, L5 (peak position
  recalled).
- (d) *Neither expansion holds there.* Leading strong coupling overestimates sigma a^2 by 5.4x and m a by 2.4x at
  beta 2.30 (L9); bare-coupling 2-loop scaling drifts 27 percent over 2.30-2.70 (L8); the roughening point estimate
  lies inside the crossover (L10). DERIVED (guides) + ARGUED (L10).
- (e) *Ratios scale early.* m_G/sqrt(sigma) is constant within its errors and about 3 percent from beta 2.5 on, where
  the correlation length 1/(a m_G) is only 1.5 (beta 2.509) to 2.7 (beta 2.70) lattice spacings (L2, L8). DERIVED.
- (f) *No transition on the Wilson axis, a critical point nearby.* At T = 0 the Wilson axis has no bulk transition;
  the peak is the shadow of the critical end point of first-order lines (SO(3) and Z2 transitions merged) in the
  fundamental-adjoint plane (L6). At such an end point some correlation length diverges in lattice units. Which
  channel goes soft is not stated in the abstract read (for SU(3), the known reading is the scalar glueball, recalled:
  the "scalar dip"). In L2 the ratio m_G/sqrt(sigma) at the coarsest point 2.2986 is 3.33, 12 percent below the
  continuum 3.78: a scalar-channel dip near the crossover, consistent with that reading. DERIVED from L2; channel
  reading BELIEF.
- (g) *Finite boxes in the band are deconfined.* beta_c(N_t = 4) = 2.2985 (L3): at beta 2.30 a periodic box of
  side 4 in any direction is at the deconfinement point; the box side needed to see the confined theory grows as
  1/(T_c a) = 4 (beta 2.30), 7.7 (2.51), about 14 (2.70). DERIVED from L2, L3.
- (h) *Gap is weaker than confinement.* The gap survives where confinement does not (Higgs phase, deconfined spatial
  correlators, recalled); 4D U(1) at weak coupling has neither (T4). Uses T4 (recalled).

**3.2 The least a proof must contain.** (i) A nonperturbative estimate at one scale where the effective coupling is of
order one, because the gap scale coincides with the crossover (3.1c, d) and no small parameter exists there; or a
structural property that bypasses that scale. (ii) A property that 4D compact U(1) lacks (T4): non-abelian
self-interaction with asymptotic freedom (T6), or a non-trivial centre / pi_1(G/Z) structure. (iii) A property that the
critical end point of the fundamental-adjoint plane lacks (3.1f): a hypothesis blind to the adjoint direction of the
action cannot prove a uniform gap in a neighbourhood of that point in coupling space, so a band proof must use where
the Wilson axis lies relative to the end point. (iii) is a test derived from measured physics (L6); its standing is
BELIEF until the end point and its soft channel are established by a theorem (they are not).

**3.3 The smallest object.** The data point to a two-coupling object: the effective action restricted to the
fundamental and adjoint plaquette couplings (beta_F, beta_A) at one blocking scale, together with the question "does
the RG trajectory from weak coupling pass the end point on the confining side". Toy: building a mixed-action Monte
Carlo that shows the end point would take more than an hour of careful finite-size work; not built (budget), so the
toy test of skill step 3.3 did not run.

**3.4 Where the result can come from.** Three regimes by scale (UV: T5, T6; crossover band: none; IR: T2, T3).
Measured RG distances (L2): a sqrt(sigma) doubles from 0.097 (beta 2.70) to 0.180 (2.51) to 0.368 (2.30), with
Delta beta about 0.19-0.21 per doubling. So from the edge of the scaling window to the crossover is about two blockings
by a factor 2, and the region not covered by either expansion is a finite, O(1) number of RG steps, each at O(1)
coupling. Whether the leading strong-coupling regime (where T2 applies) is reached after one or two further blockings
is not known from the items read (the measured a sqrt(sigma) below beta 2.2 was not fetched). DERIVED (guide) + open.

**3.5 Make the requirement less wrong.** The Clay consumer needs the continuum gap; none of the data suggests the gap
is the wrong object for that consumer. But (b) says gap and confinement are one-scale facts, and (h) says the gap is
the weaker one: a route that tries to prove the gap through confinement (area law) proves more than needed.

**3.6 Price.** From the inventory alone: the missing input is a decay estimate for the effective theory across O(1)
blocking steps at O(1) coupling in a region that sits near (not on) a critical point of an enlarged coupling space.
Mark: reading (rests on BELIEF items L5, L6, L8, L9).

**Conclusions.**

- C1 The gap is the 0++ glueball, 3.78 sqrt(sigma) in SU(2); one scale with sigma, T_c, Lambda (3.1a-b; L1, L3, L4).
  MEASURED.
- C2 It is generated where the running coupling is O(1); on the Wilson lattice the gap scale meets the cutoff at
  beta 2.2-2.4, the crossover band (3.1c; L2, L5). MEASURED + DERIVED.
- C3 In that band neither the strong- nor the bare weak-coupling expansion is quantitatively valid (3.1d; L8, L9, L10).
  DERIVED guide; BELIEF as a statement about proofs.
- C4 The Wilson axis has no T = 0 transition, but the band is the shadow of a critical end point nearby in the
  fundamental-adjoint plane; the measured scalar dip (12 percent) is its imprint (3.1f; L2, L6). MEASURED + BELIEF.
- C5 Continuum ratios are reached at correlation lengths of 1.5-3 lattice spacings (3.1e; L2). MEASURED.
- C6 The firm mechanism is the confining flux tube with universal string behaviour (L11-L13, E3, T7). Centre vortices
  are favoured by projected and twisted-box data (L15-L17, T10) but CONTESTED as mechanism; monopoles (L18) and
  Gribov/propagator readings (L19) are gauge dependent and CONTESTED; instantons do not track confinement (L17).
- C7 SU(2), SU(3) and N = infinity agree qualitatively; masses within about 20 percent (S1, S4). The deconfinement
  order differs (L3, S3), irrelevant to the T = 0 gap. MEASURED.
- C8 Small periodic boxes in the band are deconfined: box side >= 1/(T_c a) = 4 at beta 2.3, 8 at 2.5 (3.1g; L2, L3).
  MEASURED + DERIVED.
- C9 A gap proof must use a property absent from 4D U(1) (T4) and, in a band proof, one sensitive to the adjoint
  direction near the end point (3.2). Second part BELIEF.
- C10 The uncovered region is a finite number (about two to four) of factor-2 blockings at fixed physics (3.4). DERIVED
  guide.

- 16:06Z steps 2-3 written (C1-C10). Next: step 4, the assumptions table.

## Step 4: the assumptions table (59 rows, six groups, with the Elon pass)

Written before any lane file is opened, so "where used" names the row text, the Clay statement or "lane (located in
step 5)". Columns: **Who requires** (Elon: Clay = Jaffe-Witten statement; owner; lane = the lane's method; habit) |
**N/M/H** (needed by the target / by the method / habit) | **Record** (S = supports, C = contradicts, O = leaves open,
with items) | **If wrong** | **Delete?** (can the requirement be deleted, and at what price) | **Check**.

### (a) Target

| ID | Assumption | Who requires | N/M/H | Record | If wrong | Delete? | Check |
|---|---|---|---|---|---|---|---|
| a1 | The mass gap is the right object (not confinement, area law, glueball spectrum, clustering) | Clay | N | S: gap is measured directly as the 0++ mass (L1); gap is the weaker of gap/confinement (3.1h) | If the consumer wanted confinement, the target is harder; if clustering, easier | No for Clay; a route that proves confinement to get the gap proves more than needed (3.5) | none needed |
| a2 | Gap = spectral gap of H above a unique vacuum, equivalently uniform exponential decay of gauge-invariant Euclidean correlations | Clay | N | S: lattice measures exactly this decay (L2) | Different definitions (e.g. without uniqueness of vacuum) change the target at theta = pi (a10) | No | none |
| a3 | For every compact simple G | Clay | N | S: SU(2), SU(3), SU(N <= 12) all gapped with similar ratios (L1, S1, S4) | An SU(2)-only proof is a partial result | Lane may delete for a first theorem; Clay may not | none |
| a4 | Existence (construction of the theory) is part of the target; gap without existence is meaningless | Clay | N | O: no measurement bears on existence; numerics presuppose it (ratio scaling L8 is evidence, not existence) | If existence is the hard part, a gap proof conditional on existence prices nothing | No | none |
| a5 | Infinite volume R^4 | Clay | N | S: finite-volume effects small once box side > 1/T_c (C8) | A torus theorem is a weaker, separate result | No | none |
| a6 | Exact mathematical statement, no bounded or numerical closure | Clay, owner | N | O (data cannot discharge it) | n/a | No | none |
| a7 | Non-triviality (not a free field) | Clay | N | S: running coupling and non-Gaussian spectrum measured (E6, L7, L1) | n/a | No | none |
| a8 | Only Delta > 0 is needed, not its value, nor the spectrum, nor Regge behaviour | Clay | N | S | A route that computes the spectrum proves more than needed | Yes: drop every spectrum ambition | none |
| a9 | Uniqueness of the vacuum (clustering) is included | Clay (via OS/Wightman) | N | S at theta = 0: no degeneracy seen (L2 correlators decay to <O>^2) | If the vacuum were degenerate, "gap" splits into gap per vacuum | No | none |
| a10 | theta = 0 | Clay (implicitly), lane | N (implicit) | O: chi measured nonzero (L14), so physics depends on theta; at theta = pi no measurement (sign problem); anomaly arguments (Gaiotto-Kapustin-Komargodski-Seiberg 2017, recalled) say SU(2) at theta = pi cannot be trivially gapped with a unique vacuum | A "for all theta" target would be false with uniqueness at theta = pi (BELIEF) | Already implicit; state it | none |

### (b) Formulation

| ID | Assumption | Who requires | N/M/H | Record | If wrong | Delete? | Check |
|---|---|---|---|---|---|---|---|
| b1 | Euclidean OS setting with reflection positivity | Clay allows; lane | M | S: all pure-gauge data are Euclidean lattice data (L1-L19) | Minkowski-only methods would be needed | Keep (cheapest) | T1 |
| b2 | Lattice regularization of the Euclidean theory | lane | M | S: the data come from it. But the crossover band, specific-heat peak and end point (L5, L6) are features of the lattice, not of the continuum: in the continuum nothing singular happens at the gap scale (L8, E6) | A route with no lattice theory at spacing a ~ 1/Delta never meets the bulk crossover | Partly: the lattice is needed only as a UV regulator; the joining scale need not be a lattice with Wilson action | none run |
| b3 | The Wilson plaquette action | lane, habit | H | C in part: the Wilson axis passes close to the fundamental-adjoint end point (L6), producing the scalar dip (3.1f); other actions sit at other distances from it (recalled) | An action farther from the end point has a milder band; universality (e6) says the continuum is the same | Yes in principle (universality); price: any proof must then handle that action | none run |
| b4 | SU(2) rather than SU(3) | lane | M | S: same qualitative physics (C7); SU(2) has the simplest centre Z2 and real representations | Results do not transfer automatically to SU(3) | Clay requires all G later | none |
| b5 | Pure Yang-Mills rather than QCD | Clay | N | O: experiment measures only QCD (E1-E8), whose light spectrum is gapless in the chiral limit and has string breaking; pure-gauge facts are lattice-only | Experiment cannot test the target directly; all "measured" pure-gauge facts are numerical | No | none |
| b6 | Periodic torus, then thermodynamic limit | lane, habit | M | C at small sizes: periodic boxes of side < 1/(T_c a) are deconfined (C8) | Small-box theorems describe the deconfined regime | Use boxes >= 1/(T_c a) or free b.c. | L3 |
| b7 | Only gauge-invariant observables carry meaning | Clay | N | S: gauge-fixed data (L15, L18, L19) are copy- and gauge-dependent | A gauge-fixed route must solve the Gribov problem | No | none |
| b8 | Compact gauge group, Haar measure on links | Clay (compact G), lane | N | S: compactness gives strong-coupling convergence (T2); compactness alone gives no gap (compact U(1) is gapless at weak coupling, T4) | A non-compact formulation loses T2 | No | T2, T4 |
| b9 | Exactly four dimensions | Clay | N | S: 4D is marginal (AF, T6); 5D SU(2) has a bulk first-order transition and no interacting continuum limit (Creutz 1979, recalled) | A dimension-blind tool fails in d = 5 (BELIEF) | No | none |
| b10 | The relevant channel is 0++, read from plaquette-type operators | lane | M | S: 0++ is lightest (L1) | A bound on another channel misses the gap | No | none |
| b11 | Gauge group SU(2) enters only through its Haar measure and characters | lane | M | O | Route-specific | n/a | none |

### (c) Reduction

| ID | Assumption | Who requires | N/M/H | Record | If wrong | Delete? | Check |
|---|---|---|---|---|---|---|---|
| c1 | Multi-scale RG frame: UV control (T5) + IR cluster expansion (T2, T3), joined in a band | lane | M | S for the three-regime picture; the uncovered region is about 2-4 factor-2 blockings at fixed physics (C10) | Other frames (stochastic quantization, bootstrap) avoid the band but have their own walls | Partly (c2) | none |
| c2 | The band is the order-one *bare* coupling of the Wilson action (row text) | lane | M | S that the gap scale meets the cutoff there (C2); C in part: the band is where the *Wilson* action is near-critical in the extended plane (C4). An RG frame joins at a scale where the *effective* action is O(1), which need not be Wilson | If the joining action is not Wilson, the end point may be farther or nearer | Yes: the joining scale can be chosen; the joining action is the RG's, not Wilson's | step 5 |
| c3 | One fixed bare coupling at a time, then uniformity | lane | M | O: lattice gap varies smoothly (L2) | A pointwise-in-beta bound without uniformity proves nothing about the continuum | No (uniformity is the content) | none |
| c4 | The strong-coupling (IR) side can be extended up to the band | lane (if used) | M | C: leading strong coupling is off by 5.4x in sigma a^2 and 2.4x in m a at beta 2.30 (L9); the roughening point estimate is inside the crossover (L10) | IR tools must be applied after further blockings, not at the band | Yes: block until the effective coupling is truly strong | L9 (guide) |
| c5 | The UV side (perturbative RG) can be run down to the band | lane (if used) | M | S partly: renormalized perturbation theory works from beta about 2.5 (SU(2)) / 5.7 (SU(3)) (S6, L8 boosted); bare-coupling scaling does not (L8) | UV control must use renormalized couplings | n/a | L8 (guide) |
| c6 | A finite-volume criterion (gap in a box implies gap) at band couplings with small boxes | lane (if used) | M | C for boxes of side < 1/(T_c a): they are deconfined (C8) | Small-box checks measure deconfined physics | Use boxes >= 4 (beta 2.3), >= 8 (2.5), >= 14 (2.7) | L3 |
| c7 | One inequality (log-Sobolev, Bakry-Emery, correlation inequality) proves it all | habit | M | C (BELIEF test): a tool blind to the adjoint direction cannot hold uniformly near the end point (C9) | One-tool routes have a range bounded by the end point | Yes | none |
| c8 | Reduction to the centre (Z2) or a finite subgroup | lane (if used) | M | O: Z2 gauge theory alone has a first-order transition (recalled, Creutz-Jacobs-Rebbi 1979) and is a different universality class; the SU(2) end point is where the Z2 and SO(3) lines merge (L6) | A Z2-only argument meets the Z2 transition | n/a | none |
| c9 | A gauge fixing inside the proof | (if used) | M | C as a warning: Gribov copies change gauge-fixed numbers (L18, L19) | Gribov problem | Avoid gauge fixing at the joining scale | none |
| c10 | Numerical checks on small lattices (4^4) guide the lane | habit | H | C at beta >= 2.3 (C8) | Wrong-phase guidance | Use L >= 1/(T_c a) | L3 |

### (d) Discard tests (as used generically; the lane's own list is read in step 5 and audited in step 6)

| ID | Assumption | Who requires | N/M/H | Record | If wrong | Delete? | Check |
|---|---|---|---|---|---|---|---|
| d1 | "A tool that also proves a gap for 4D compact U(1) at weak coupling is wrong" | lane | M (valid test) | S: T4 is a theorem | n/a: valid in the refutation form | Keep | T4 |
| d2 | "A tool that also gives a gap in the deconfined (high-T or small-box) theory is wrong" | habit (if used) | H | C: the deconfined theory still has a spatial gap (magnetic and Debye screening, recalled; C8); deconfinement kills the area law, not the gap | Tests against deconfined models discard gap tools wrongly; they test confinement tools only | Restrict to area-law tools | none run (needs reading of spatial screening masses) |
| d3 | "It needs a small number" (small beta or small g) | lane | M | S that the band has no small bare parameter (C3); O whether a small parameter exists in another variable (distance from the end point, 1/xi, 1/N) | Range form only: write the proved range | Keep in range form | none |
| d4 | "Its constant depends on the answer" (circular) | lane | M | O | Not circular when the constant depends on a smaller scale (induction over blockings) | Keep in valid form | none |
| d5 | "It bounds the wrong quantity" (string tension, free energy, plaquette, instead of the gap) | lane | M | S: sigma and Delta are distinct (ratio 3.8, L1) though one-scale | n/a | Keep | none |
| d6 | "It was tried" (Balaban plus cluster expansions since the 1980s) | habit | H | O: a failed search rules out nothing | n/a | Delete as a reason | none |
| d7 | NEW from data: "a tool whose hypothesis is blind to the adjoint direction of the action holds also at the fundamental-adjoint critical end point, where some lattice correlation length diverges; so it cannot give a uniform lattice gap in a neighbourhood of the end point" | this run | M | S: L6 (end point exists, MEASURED); channel of the soft mode BELIEF | If the soft mode at the end point is not gauge-invariant-local or not 0++, the test binds a different quantity | Keep as BELIEF test until the end point is a theorem | none (see step 8) |
| d8 | "A tool that holds also for pure Z2 or SO(3) lattice gauge theory meets their first-order transitions" | lane (if used) | M | S: L6 | n/a | Keep | none |
| d9 | "A dimension-blind tool fails in d = 5" | habit | M | S (MEASURED bulk transition in 5D SU(2), recalled; not a theorem) | Test rests on BELIEF | Keep as BELIEF test | none |
| d10 | "Numerics on small lattices decide between routes" | habit | H | C (C8) | Wrong-phase guidance | Delete for beta >= 2.3 with L < 1/(T_c a) | L3 |

### (e) Beliefs

| ID | Assumption | Who requires | N/M/H | Record | If wrong | Delete? | Check |
|---|---|---|---|---|---|---|---|
| e1 | Centre vortices are the confinement mechanism | field (part) | H | CONTESTED: projected data favour (L15-L17), twisted-box free energy (T10) gauge invariant; gauge dependence of projection | A vortex-based proof route would aim at a non-mechanism | Not needed for the gap | none |
| e2 | Dual superconductor / monopole condensation | field (part) | H | CONTESTED (L18: 92 percent abelian, Gribov-sensitive) | same | Not needed | none |
| e3 | Gribov-Zwanziger horizon / propagator mass is the mechanism | field (part) | H | CONTESTED (L19: decoupling, not scaling) | same | Not needed | none |
| e4 | No bulk phase transition on the SU(2) Wilson axis at T = 0 | everyone | M (every route joining strong coupling to the continuum along the Wilson axis needs it) | S strongly (L5-L7, L2 smooth) but it is NOT a theorem | If false, the strong-coupling phase (T2) is not the continuum phase on the Wilson axis | Cannot delete on the Wilson axis; can be avoided by joining at an RG effective action instead (c2) | open (mathematics) |
| e5 | Asymptotic freedom holds non-perturbatively: beta -> infinity is the continuum limit | everyone | N in practice | S (L7, L8 ratio scaling, E6) | No continuum limit at g -> 0 | No | none |
| e6 | Universality: actions in a neighbourhood give the same continuum theory | everyone | M | S (ratio scaling L8; action comparisons recalled) | Action choice would matter for the target | No | none |
| e7 | A continuum limit exists with the measured ratios | everyone | N | S (L8) | n/a | No | none |
| e8 | Large N as a guide: the gap persists at N = infinity | field | H | S (S4: 0++ 3.072 sqrt(sigma)) | n/a | n/a | none |
| e9 | Glueballs are closed flux tubes (string models) | field (part) | H | CONTESTED as dynamics; long open strings are firm (L11-L13) | n/a | Not needed | none |
| e10 | The gap is caused by confinement | field (habit) | H | O: one scale (C1) but the gap holds where confinement fails (3.1h) | A route proving the gap through the area law proves more than needed and is harder | Yes | none |
| e11 | Instantons do not drive the gap or confinement | field | H | S in part (L17: topology follows vortices) | n/a | n/a | none |

### (f) Working rules (questioned on paper only; all obeyed)

| ID | Rule | Who requires | Record | What a different rule would give (not used) |
|---|---|---|---|---|
| f1 | No computer-assisted proofs; Lean-formalizable only | owner | O | With interval arithmetic allowed, a finite-volume criterion checked at one band coupling (if one existed) could be certified; not used |
| f2 | Measured data never discharge a proof step | owner, skill | n/a | n/a |
| f3 | SU(2) first | lane | S (C7) | SU(3) first would add a first-order deconfinement and a weaker Z3 analogy; no gain |
| f4 | Lattice first, Wilson action | lane | C in part (b3, c2) | A route that joins at an RG effective action (b2, c2) |
| f5 | Jaffe-Witten target as the frame | Clay, row 1052 | S that the gap is the measured object (a1); O on theta (a10) | A confinement target is harder; a lattice-uniform target is the honest intermediate |
| f6 | No subagents; one response <= 128k tokens; write as you go | owner | n/a | n/a |
| f7 | No lane file before step 5 | row 1063 | n/a | n/a |

### Elon pass (who requires each requirement; what can be deleted)

Required by Clay and not deletable: a1-a7, a9, b5, b7, b9 (and a10 as implicit). Required only by the lane's method
and deletable at a price: b2 (lattice at the joining scale), b3 (Wilson action), b6 (periodic small boxes), c2 (the
band in *bare* Wilson coupling), c4 (pushing strong coupling to the band), c6 (small-box criteria), c7 (one tool),
c10 (small-lattice numerics), d2, d6, d10 (invalid or weak tests), e10 (gap through confinement). Habits with no
requirer: e1-e3, e9 (mechanism beliefs; no route needs them for the gap).

### Ranking (by how much the problem changes if dropped)

1. **c2 + b3: the band is the Wilson action at order-one bare coupling.** The data place the crossover where the
   *Wilson* action passes a critical end point of the extended plane (C4). The lane would instead choose the joining
   action and scale from the RG, and ask how far that action is from the end point.
2. **c4: strong coupling reaches the band.** Contradicted quantitatively (L9). The lane would block further before
   using cluster expansions and count the extra blockings (C10).
3. **e4: no Wilson-axis transition.** Supported but unproved; every Wilson-axis join needs it. The lane would mark it
   as an open premise of any such route.
4. **c6/c10/b6: small periodic boxes.** Contradicted at beta >= 2.3 (C8). The lane would re-check any finite-box
   criterion or numerical guide against 1/(T_c a). (Changes an owner decision if a lane verdict rests on 4^4 data.)
5. **d2/e10: gap through confinement, and deconfined models as tests.** The data say the gap is the weaker property;
   the lane would drop area-law intermediates and stop using deconfined models as counterexamples to gap tools.

Rows whose drop would change an owner decision: c2/b3 (the lane's choice of the band), c6/c10 (verdicts from small
lattices), and a10 (theta stated explicitly in the target).

- 16:09Z step 4 written (59 rows). Next: step 5, open the lane files.
