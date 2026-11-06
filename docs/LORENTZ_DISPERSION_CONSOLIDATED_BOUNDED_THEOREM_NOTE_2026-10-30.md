---
claim_id: lorentz_dispersion_consolidated_bounded_theorem_note_2026-10-30
claim_type: bounded_theorem
claim_scope: "Consolidation of 15 source notes on one question: Can the cubic lattice reproduce a common relativistic continuum and survive the resulting dispersion tests? Each result carries its own scope below; nothing here is stronger than its source."
---

# Relativistic cones and dispersion tests: consolidated results

**Question.** Can the cubic lattice reproduce a common relativistic continuum and survive the resulting dispersion tests?

**Status authority.** Independent audit lane only. These are author statements for review.

## What this theme found

# Synthesis: relativistic cones and dispersion tests

**Question.** Can the cubic lattice reproduce a common relativistic continuum and survive the resulting dispersion tests?

**A cone exists; no symmetry of a translation-invariant finite-depth tick fixes a common one.**
- #9872: a supplied tick on one-mode sites, exactly covariant under the 24 proper cubic rotations, with an isotropic cone of speed 1/sqrt3 (isotropy numerical). On its own tick (step 0.3, copy mass 0), #9913 reports a supplied photon link band equal to the massless fermion band at 200 sampled K; logged #9878 reports the match on the #9872 tick, with a zone-corner Jordan block.
- #9913: no symmetry fixes the ratio of two species' dressed speeds; for its supplied link law the electron cone lies below the photon cone by kappa alpha, kappa -0.17 to -1.01. Logged #9916 reports the matching negative for response laws.
- #10092: no such update has an exactly relativistic lowest band on an open momentum set. A free-matter history-level weight is built, relativistic to 9e-11 at sampled momenta; it needs an infinite image tower of poles, whether that fits one qubit per site being an owner decision. Its radiative protection is a condition, not a result.

**Tests**, with a supplied cubic dimension-six term (photon c_g, fermions c_g plus a copy-mass shift) and supplied light-front models:
- #10090: time-of-flight margins of at least 6.8 orders; a photon-to-pair cutoff at 8.0e16 to 1.1e17 eV, absent on body diagonals; proton emission closed to 1e21 eV off body-diagonal cones.
- #10091: with nucleons taken universal (c_N = c_q), 4He opens at 4.1 to 7.0 EeV and 56Fe at 18 to 31 EeV, times 1.47 at the bracket c_N = 0.214 c_q. The estimate: flux above at most 46 EeV is nucleons, against Auger's composition unless air showers differ.
- #10093: in a toy shower model a pure flowed-proton beam is 2.2 combined sigma from raw Xmax moments at the best preregistered corner; excluded for cross-section factor 1 or less; worst pulls 1.5 to 2.4 at factors 4 to 8 (corners added after the run).

**Failed.** Frozen parton-weight and Fermi-core nuclear walls were replaced.

**Open.** The flowed hadron's air cross section; the one-loop dimension-six coefficient on the cubic tick (#10094, theme d4-route, reports closure by symmetry for spin at most 1 on the D4 route); history-level photon and gluon weights.

## Results carried with their runners

# Kept results: relativistic cones and dispersion tests

Reading note. The source notes in this theme call their tick, link and dispersion rules "CL-1", "CL-3", "the register" and the like. In `docs/CANDIDATE_LAWS.md`, CL-1 is the lossless-influence clause, CL-2 the record-removal clause and CL-3 a pending conservation proposal, and none of them contains a tick or a dispersion rule. Those labels are therefore not used in the text written for this consolidation; each source rule is called a supplied rule and is described by its content. Quoted source text keeps its original wording. See the Corrected or replaced claims section, entry 1.

Every statement below is an author statement from the source note, for independent review. No runner was rerun.

### #9872: Cube-covariant spin-3/2 edge-hop tick on one-mode sites

**Kind of statement.** Exact finite results for a supplied tick (unitarity, anticommutation of the three hop directions, W^2 = 1, the band formula, covariance under the 24 proper cubic rotations), each checked numerically to about 1e-15 on finite lattices, plus finite numerical diagnostics (cone isotropy to about 1e-3, zero net Berry flux) and a same-runner comparison for j = 0, 1/2, 1. All results are for the supplied partition geometry, rotation action and mass parameter mu; no classification of ticks, no derivation from the axioms and no physical identification is claimed.

**Runner.** [../scripts/margolus_spin_three_halves_edge_hop_gives_a_cube_covariant_dirac_tick_2026_10_21.py](../scripts/margolus_spin_three_halves_edge_hop_gives_a_cube_covariant_dirac_tick_2026_10_21.py) (author-reported output only; not rerun in this consolidation).

**Dependencies.** No other PR. The note refers to a "candidate-law register" tick that is covariant under only 4 of the 24 rotations; the current `docs/CANDIDATE_LAWS.md` contains no tick, so that reference is not used here. Within this theme, #9878, #9888 and #9891 are written on this tick.

**Status within this theme.** Stands as written. The twofold degeneracy ("two copies") and the lack of net chirality at the massless node are statements about this tick only; the chirality question belongs to another theme.

**Scope as written in the note (verbatim `claim_scope`).**

> In a supplied Margolus tick with one fermion mode per site and rotations acting on site modes as spin-3/2 coherent states along the body diagonals, the edge hop with overlap phases is unitary, exactly covariant under the 24 proper cubic rotations about every block centre, and has bands cos w = cos^2(mu/2)(cos Kx + cos Ky + cos Kz)/3 - sin^2(mu/2); no classification of all ticks, derivation from the axioms or physical identification is established.

**Statement, copied from the note.** (Headings are demoted; text is otherwise unchanged, except that runner pass counts are dropped and the source's "Verdict" wording is replaced by "conclusion" or "gate outcome".)

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its current block-of-eight tick candidate is exactly covariant under only 4 of the 24 rotations. This note gives a supplied tick on one-mode sites that is covariant under all 24. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the tick nor the rotation action.

##### Setting

Sites of Z^3 carry one fermion mode each. The tick applies an 8x8 block unitary W on the even blocks {0,1}^3 + 2Z^3 and then on the odd blocks shifted by (1,1,1). Rotations act on site modes as corner permutations times phases, induced from a character of the corner stabiliser C3; the four cases are the spin-j coherent states along the body diagonals with j = 0, 1/2, 1, 3/2. Each action is monomial and unitary, and the 2 pi rotation acts as (-1)^(2j).

##### The spin-3/2 edge hop

Hop along each of the 12 cube edges with amplitude 1/sqrt3 and phase equal to that of the overlap of the two sites' spin-3/2 states, W = Wx + Wy + Wz. Transport around every cube face is -1 for j = 3/2, against phases -pi/3 and -2 pi/3 for j = 1/2 and 1. Hence hops along different axes anticommute, {Wa, Wb} = (2/3) delta_ab to 2.3e-15, and W is Hermitian with W^2 = 1. W commutes with the 24 spin-3/2 corner actions, and on a 6^3 lattice the tick commutes with all 24 rotations about both even and odd block centres to 2.1e-15.

With mass, W(mu) = cos(mu/2) W + i sin(mu/2) 1, all 8 bands obey

  cos w = cos^2(mu/2) (cos Kx + cos Ky + cos Kz)/3 - sin^2(mu/2)

to 1.2e-15 over 2000 K and three values of mu, so the bands are +-w, each exactly fourfold. Near K = 0, |w| = sqrt(mu^2 + k^2/3) within 1.9e-3 at |k| = 0.4, with direction spread below 4.4e-3: two degenerate isotropic Dirac bands with speed 1/sqrt3 block per tick. The global gap is mu, reached at K = 0. The massless node has zero net Berry flux (-6.7e-16), so it is not net-chiral. The only other node is w = pi at K = pi(1,1,1), which mu does not gap.

##### Comparison within the same runner

For multiplicity-free actions (j = 0, 1/2, 1) the linear K term vanishes inside every eigenspace of the K = 0 tick, to 4.6e-15. For j = 1/2 with E1/2 and G3/2 coupled, the massless cone has velocities +-sqrt(2/3), each twofold and isotropic to 1e-3, plus two zero-velocity states; with mass 0.1 the light bands follow sqrt(m^2 + (2/3)k^2) within 0.6% at |k| = 0.1. Along all four body-diagonal lines, however, a twofold level sits exactly at the G3/2 energy for random block unitaries, to 5.6e-16. The pure corner-inversion mover sends corner s to 1 - s, so each half-tick steps one block along a diagonal d in {+-1}^3.

##### Scope

Supplied: the partition geometry, the j = 3/2 action, the orientation convention and mu. Reading squared amplitudes as probabilities, interactions, the meaning of the two degenerate copies, the relay-source result for this tick, and a classification of all covariant ticks are not established. No derivation from the axioms or physical identification is claimed.

### #9913: No tick symmetry fixes the electron cone to the photon cone

**Kind of statement.** Mixed. The step-set and symmetry statements (items 1 to 3) are exact. Item 4 and the kappa values (kappa alpha, with alpha the coupling of the note's one-loop calculation) are numerical one-loop (second-order Floquet perturbation theory) results that depend on a supplied photon/link law, a supplied copy mass and step, and a supplied cell size; the comparisons with LEP and LHAASO bounds are arithmetic estimates with measured numbers.

**Runner.** [../scripts/no_tick_symmetry_fixes_one_loop_electron_cone_to_photon_cone_2026_10_21.py](../scripts/no_tick_symmetry_fixes_one_loop_electron_cone_to_photon_cone_2026_10_21.py) (author-reported output only; not rerun in this consolidation).

**Dependencies.** No other PR. It depends on a supplied link law and tick law described inside the note (Coulomb gauge, two transverse modes on the partition band, straight-bond site-phase lift, frame-block Coulomb exchange) that are not in `docs/CANDIDATE_LAWS.md`, on a "photon clause" giving the photon the edge cone, and on a "kinetic-isotropy primitive"; none of these is a PR in this set. The related #9916 (logged) reaches a compatible negative for fermion cones under a different route.

**Status within this theme.** Stands as written. The note adopts, without deriving it, the reading of each species' step from its dressed cone; the dimension-six residual and the bare-step differences quoted in the estimates follow from that adopted reading.

**Scope as written in the note (verbatim `claim_scope`).**

> No symmetry of a translation-invariant finite-depth tick on Z^3 can fix the ratio of two species' dressed limiting speeds, and in 3+1 a null-direction tick gives no protection; for the supplied link law the one-loop electron cone sits below the photon cone by kappa alpha with kappa between -0.17 and -1.01 over the copy masses scanned; reading each species' step from its dressed cone is adopted, not derived.

**Statement, copied from the note.** (Headings are demoted; text is otherwise unchanged, except that runner pass counts are dropped and the source's "Verdict" wording is replaced by "conclusion" or "gate outcome".)

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its tick law sets a shared step at which the tree-level cones of every species are the null cone of the cube edges, and its photon clause makes the photon's dressed cone the edge cone. This note computes the electron's one-loop cone under the register's link law and asks whether any symmetry of the tick can hold it to the photon's. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the tick nor the link law.

##### Statement

1. The one-tick step set (81 displacements, both time senses) is preserved, together with the edge cone, by exactly 96 linear maps for every trial cone speed: the 48 cubic rotations and reflections, each with or without time reversal. All fix the time axis.
2. Any symmetry of a translation-invariant tick maps U to U or U^-1 and K to RK with R orthogonal. Such a map preserves w^2 = c^2 K^2 for every c, so it cannot fix c_e/c_gamma.
3. In 3+1 a tick written on null directions gives no protection: a metric-sign-flipping isometry needs equal inertia, which (1,1) has and (1,3), (3,1) do not.
4. For the register's link law the one-loop electron speed is off the photon's dressed cone by dc/c = kappa alpha, with kappa negative and between -0.17 and -1.01 over the copy masses scanned.

##### Derivation

The stay step (one tick, no displacement) is the only step of its norm, so any map preserving the step set sends it to plus or minus itself; hence every such map fixes the time axis. Every step advances exactly one tick, so the Euclidean hypercubic turn t -> x, which the 4D hypercubic radiative-stability argument uses, cannot be a symmetry of any tick. Under the tick law the equality c_t = c_s of the kinetic-isotropy primitive therefore holds at tree level only. The symmetry argument covers the copy-mass CPT-type map, inversion, the 12 tetrahedral turns and the half-tick glide. The edge reading relates updates on different edge sets; it sets the tree-level cone but puts no constraint on how two species are dressed on the same edges.

In 1+1 the step-pi/2 tick dressed by any site phases is a site permutation times phases with displacements of exactly +-2 per tick, which is the 1+1 null-lattice protection. In 3+1 a power of any translation-invariant permutation tick is diagonal with phases linear in K, so its bands are planes and it has no cone. A cone needs interference, and link phases dress interference.

The one-loop computation uses the register's link law: Coulomb gauge, two transverse modes on the partition band, a straight-bond site-phase lift projected off the gauge orbit, and frame-block Coulomb exchange, with second-order Floquet perturbation theory. The Coulomb part runs with the continuum velocity log 2/(3 pi) and the transverse part with the opposite log. Because the tree cones are equal the logs cancel, so kappa is a finite lattice constant.

##### Checks


- `A1 real-space 8^3 tick = Bloch tick (M = 0, .5, 1); the copy mass leaves the light speed exactly sin(eps)/sqrt3; the partition (Yee) photon band equals the massless fermion band at every K`.
- `A2 THEOREM: the one-tick step set (81 displacements, both time senses) is kept by exactly 96 cone-preserving linear maps for every trial cone speed`.
- `A3 THEOREM: an isometry flipping the metric sign needs equal inertia: (1,1) in 1+1 has it ..., (1,3) vs (3,1) in 3+1 does not`.
- `A4 bare-mass sensitivity of the light cone at mu = 0: zero without the copy mass ..., O(K^2) relative with it ...: mass and cone conditions are independent`.
- `B1` to `B4`: the engine matches an exact many-body toy (3.3e-6), a static field on a torus (converging as amplitude^2), a real-space Coulomb sum (2e-15) and the Ward identity (9e-18).
- `C1 reference point eps = .3, M = .5: kappa is nonzero, O(1) and negative (electron slower than the photon), isotropic, p-independent, with no helicity splitting (no CPT-odd term)`: kappa = -0.8437 on an axis, -0.8415 on the diagonal, splitting 9e-15.
- `C2 the Coulomb part runs with the continuum velocity log 2/(3 pi) per ln(1/p), the transverse part with the opposite log`: slopes +0.2062 and -0.2070.
- `C3 continuous-time limit (eps = .05; r = M/eps): kappa(r) stays negative and O(1) for every copy mass, -0.17 when the copies are near-degenerate to -1.0 near r = 3`. kappa is -0.180, -0.217, -0.469, -1.011 and -0.897 at r = 0.1, 0.3, 1, 3, 10, and about -0.85 for a lattice-scale copy mass.
- `C4 photon-law variants (eps = .05): at r = 10 every variant stays negative and O(1); at near-degenerate copies (r = .1) bcc Gauss law plus linear photon crosses zero: a one-loop zero can be tuned from supplied choices, not protected`.
- `C5 with the photon faster by delta = .1 the electron speed runs towards it ... A = 0.346`.
- `D1 a step is not a response variable: the vacuum phase falls monotonically with the step, so no stationarity of the total phase selects it; and the additive mass is unprotected`.
- `E1 arithmetic: every kappa excluded by > 1e8 (LEP) and > 1e15 (LHAASO)`.

##### Estimates against measurement

Without a fix, dc_e/c is between -7.4e-3 and -1.3e-3, with the photon faster than the electron; photons above 8 to 20 MeV would decay to e+e- in vacuum. This exceeds the LHAASO bound 3e-19 by 4e15 to 2e16 and the LEP bound 1e-11 by 1e8 to 7e8. The flow from the cell scale to the electron mass suppresses the offset only by a factor 0.88, and a tuned one-loop zero still leaves O(alpha^2) ~ 5e-5. With each species' step read from its dressed cone there is no dimension-4 offset by construction; the dimension-6 residual is about 3e-25 at 1.4 PeV, and the electron's bare step comes out 0.13 to 0.74% larger than the edge step. With a fixed bare mass angle, the additive mass would shift m_e by a factor of order 1e19, so the mass angle must also be read as a dressed value or be protected by chirality.

##### Boundary

Supplied: the photon law (band, lift, gauge projection, Gauss law, frozen extra site-phase modes, continuous-time photon modes at the half-tick boundaries), the copy mass and step (scanned), the sea branch, one-loop perturbation theory, the photon cone taken from the register's photon clause, a cell size of 5 Planck lengths, and the measured bounds (estimates only). Forced: the symmetry results, the log cancellation, isotropy, the absence of helicity splitting, mass-cone independence, and kappa != 0 at every copy mass scanned for the register's law. Reading each species' step from its dressed cone is adopted to meet measurement, not derived; a vacuum-standard reading reduces to it because the dressing scales with charge squared. The size of kappa depends on the supplied law at O(1). Two loops and the quark and gluon sector were not computed. The cone problem is not the chirality problem: masses could be protected by chirality, but no tick symmetry protects cones.

### #10090: Rule-fixed dimension-six dispersion: time of flight, photon cutoff, three-body flow, nuclear dissociation

**Kind of statement.** Mixed and dependent on supplied models. The ray-by-ray inequalities for leptons and photons (items marked [T/F]) are exact or exact-in-model; the three-body proton results are finite diagnostics of a supplied light-front longitudinal model with supplied binding parameters (m = 0.3, kappa = 0.6 GeV) and a supplied gluon-dressing step; the nuclear dissociation openings are estimates that depend on supplied separation energies and on a supplied Fermi momentum; the time-of-flight margins are arithmetic with the literature bounds listed in the note.

**Runner.** [../scripts/rule_fixed_dimension_six_liv_survives_time_of_flight_by_seven_orders_and_is_testable_in_uhecr_composition_and_photon_cutoff_2026_10_26.py](../scripts/rule_fixed_dimension_six_liv_survives_time_of_flight_by_seven_orders_and_is_testable_in_uhecr_composition_and_photon_cutoff_2026_10_26.py) (author-reported output only; not rerun in this consolidation).

**Dependencies.** Inherits the cubic dimension-six coefficients c_g = -S/24 and c_q = -S/6 + 1/24, the S pattern and E* = 1.217e18 GeV unchanged from an upstream note named assumed-inputs-model in #10089 and #10092; that note is not among the PRs of this theme, and its origin is not checked here. Relies on the light-front placement of the Lorentz violation in the mass operator and on first-order Hellmann-Feynman additivity, both first set out in #10089 (superseded in part; the parts that stand are recorded in the Corrected or replaced claims section). Narrows the proton and nuclear walls of #10087 and #10088. Its nuclear statements are replaced in part by #10091 (see below).

**Status within this theme.** Parts replaced: the Fermi-core dissociation walls (Fe 100 to 160 EeV, "about 1.8 A EeV") and the survivor statement for N were withdrawn by #10091, as were the statements about breakup products (nucleons at E/A each), the 50 to 160 EeV effective Fe wall and "nuclei above Fe"; the conclusion that nothing observed is excluded was replaced by #10091 and then narrowed by #10093. Time-of-flight, photon, lepton, and the three-body hadron results are not replaced, but they rest on the assumption (set out in #10089 and not computed dynamically) that the fixed-momentum eigenstate is reached, with a formation length estimated at about 1e-4 cm. See the Corrected or replaced claims section, entries 2, 3 and 4.

**Scope as written in the note (verbatim `claim_scope`).**

> With the rule-fixed dimension-six dispersion (c_g = -S/24, c_q = -S/6 + 1/24 for quarks, leptons and neutrinos, E* = 1.217e18 GeV): (i) [F] composite universality holds for a 3-body light-front proton (Q1 FEM, converged to 3e-3, checked against an independent simplex discretisation): c_B/c_q = 0.214 (additive, HF-exact) -> 0.72-0.90 (1e19 eV) -> 0.997-0.999 (1e20 eV), with residual 1 - c_B/c_q ~ u^-1/2; gluon dressing (two Fock sectors, supplied) changes c_B by 6-8 % and the gluon is pushed to small x; (ii) [F] p -> p gamma and p -> p pi0 stay closed to 1e21 eV on axis and sky rays, but the u^-1/2 residual opens p -> p gamma at 5.3-6.0 EeV inside cones around the 8 body diagonals where |c_q| - |c_g| < ~1e-3 (1.8 % of the sky); (iii) [E] bound nuclei cannot follow the flow (the flowed state is their continuum): frozen at the nucleon level, spontaneous vacuum dissociation A -> N + (A-1) opens kinematically at d 3.5-6, He 5-9, N 9-17, Fe 19-32 EeV and reaches the Fermi core (k <= 0.25 GeV, supplied) at d 3.5-6, He 7-13, N 25-40, Fe 100-160 EeV (~1.8 A EeV); (iv) [T/F] e -> e gamma and gamma splitting are closed exactly; gamma -> e+e- opens at 8.0e16 (axis) to 1.1e17 eV (sky) and never on body diagonals; the gamma gamma_bg pair threshold shift is ray-independent (coefficient 1/96) and 5e-8 at 1.4 PeV; (v) [E] photon E_QG,2 = 4.2-7.3e18 GeV, 6.8-7.5 orders above the GRB 090510 and GRB 221009A subluminal quadratic bounds. Verdict: time of flight SURVIVES (>= 6.8 orders); UHECR composition and the photon cutoff are TESTABLE SOON.

**Statement, copied from the note.** (Headings are demoted; text is otherwise unchanged, except that runner pass counts are dropped and the source's "Verdict" wording is replaced by "conclusion" or "gate outcome".)

Criteria fixed before the run (criteria_pre_run.txt). Axioms unchanged; no CL edit; nothing adopted.
Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers, [S] reading.

##### Builds on / narrows

- agents/composite-dispersion (2-body light-front flow to the most subluminal constituent). Extended here to
  3 bodies, gluon dressing, pion, and nuclei. It is confirmed for hadrons and NARROWED in two places: the body
  cone (ii) and nuclei (iii). Its line "nuclei inherit the same flow [S]" is contradicted.
- agents/uhecr-vacuum-emission and agents/liv-auger-confrontation: their proton walls (3.2-4.4 EeV) are removed
  off the body cones. Their nuclear walls are replaced by a dissociation channel that is stronger, not weaker.
- c_g, c_q, the S pattern and E* are inherited unchanged.

##### Sources (fetched 2026-10-26)

- Vasileiou et al., PRD 87, 122001 (2013), arXiv:1305.3463: GRB 090510, E_QG,2 > 1.3e11 GeV (95 % CL, subluminal).
- LHAASO, PRL 133, 071501 (2024): GRB 221009A, E_QG,2 > 6e-8 E_Pl = 7.3e11 GeV (95 % CL, subluminal).
  Piran-Ofengeim, PRD 109, L081501 (2024), arXiv:2308.03031, give 5.8(4.6)e-8 E_Pl.
- LHAASO, PRL 128, 051102 (2022), arXiv:2106.12350: superluminal photon decay, E_QG,2 > 1e-3 M_Pl. The rules'
  photon is subluminal, so this bound does not apply; its analogue is the gamma -> e+e- threshold below.
  Highest photon about 1.4 PeV (LHAASO J2032+4102).
- Ellis et al., arXiv:1807.05155: TXS 0506+056 neutrino, M_1 >~ 3e16 GeV. The abstract gives no quadratic number.
  The n = 2 bound used here is computed from their ~10-day window, so it is mine, not theirs.

##### Results

- [F] A1, 3-body proton. Setup:
  - Light-front longitudinal model, LMV pair confinement (m = 0.3, kappa = 0.6 GeV, supplied).
  - Q1 FEM in the Jacobi chart, graded to x ~ 1e-7.
  - Checks: the two grids agree to 2e-3; a 1/N-extrapolated uniform-simplex graph Laplacian agrees to <= 7e-3;
    Hellmann-Feynman holds to 1e-6.

  c_B/c_q by ray:
  | Ray | 1e18 eV | 1e19 eV | 1e20 eV |
  |---|---|---|---|
  | Axis | 0.214 | 0.901 | 0.9990 |
  | Sky | 0.214 | 0.857 | 0.9985 |
  | Body | 0.214 | 0.719 | 0.9969 |

  The residual 1 - c_B/c_q falls as u^-1/2 (slope 0.500, u = lam|c_q|), set by the spectators' m^2/x cost.
  So universality is ROBUST for 3 bodies.
- [F] A2, gluon dressing. Setup: |qqq> + |qqqg>, contact q -> qg (supplied g, m_g = 0.5 GeV), P_g(0) = 0.17.
  - The dressed/undressed c_B ratio is 0.924 -> 0.939 for u = 0.5 -> 20 GeV^2.
  - P_g falls 0.17 -> 0.04, and P_g <x_g^3> falls 6e-3 -> 2e-3.
  - So the less-subluminal gluon is expelled to small x, and the dressing does not leave a growing residual.
  - Limits: uniform grids, u <= 20 only, and the large-u value is not computed.
- [F] A3, emission with the full eigenstate dispersion (physical masses shifted in; supplied).

  Opening energy:
  | Model | Axis | Sky | Body |
  |---|---|---|---|
  | Frozen-additive control | 6.3 EeV | 6.0 EeV | 5.0 EeV |
  | Full eigenstate | closed to 1e21 eV | closed to 1e21 eV | 5.3 EeV |

  - The frozen control reproduces the parent wall.
  - p -> p pi0 with the full eigenstate is closed on all rays.
  - Body cone: opens for S <= 0.340 and is closed at S >= 0.350. That is a sky fraction of 0.018 around the
    8 body-diagonal directions. Scanning (m, kappa) = (0.2, 0.5) and (0.4, 0.8) gives 6.0 and 5.3 EeV.
  - Mechanism: on the body diagonal c_q = c_g = -1/72 exactly. The u^-1/2 residual adds a term linear in P to
    the composite energy, i.e. a speed offset of order M sqrt(2|c|)/E*. That makes the proton marginally faster
    than the photon there.
  - This is the one non-universal residual that opens a hadron channel.
- [F] A3d, GZK. The required head-on target energy for p gamma -> p pi0 is never below 0.03-0.05 eV (minimum at
  2-3 EeV) and grows to 2-14 eV at 1e20 eV. So photopion on the CMB is closed at all energies.
  - The photopion GZK horizon is absent [T-level kinematics, F-level dispersion].
- [E] A3c, nuclei.
  - A bound nucleus cannot follow the flow, because the flowed configuration (one nucleon carrying x ~ 1) has
    GeV relative momentum and IS the nucleon continuum. So nuclei are additive at the nucleon level, while each
    nucleon flows internally.
  - Spontaneous vacuum dissociation A -> N + (A-1) (S_n supplied) therefore opens kinematically:

  | Nucleus | Kinematic opening (EeV) | Reaches Fermi core, k_min <= 0.25 GeV (EeV) |
  |---|---|---|
  | d | 3.5-6.0 | 3.5-6.3 |
  | He | 5.3-8.9 | 7.1-13 |
  | N | 9.4-17 | 25-40 |
  | Fe | 19-32 | 100-160 |

  - For Fe, k_min = 10 GeV at 1.2 E_open (rate negligible) and 0.40 GeV at 1e20 eV (short-range-correlation
    tail). So the effective Fe wall is about 50-160 EeV, depending on the unsupplied nuclear tail.
  - Coherent A -> A gamma also opens kinematically (Fe 25-32 EeV), but the parent found it form-factor dead.
  - Near threshold the products are nucleons with about E/A each.
- [T/F] A4, leptons and photons (elementary, no flow).
  - |c_g| <= |c_q| on every ray, so the photon is the faster particle.
  - e -> e gamma is closed (exact: |c_e|(1 - (1-y)^3) >= |c_g| y^3).
  - gamma -> 2, 3 gamma is closed (exact concavity).
  - gamma -> e+e- opens at 8.0e16 eV (axis) and 1.1e17 eV (sky), and NEVER on body diagonals (c_q = c_g).
  - [T] The gamma gamma_bg -> e+e- threshold coefficient |c_g| - |c_q|/4 = 1/96 on every ray. Its shift is
    +5.2e-8 at 1.4 PeV: unobservable.
  - Crab 2 PeV electrons: the LIV/mass ratio in 1 - v is 3e-5.
- [E] B, time of flight. E_QG,2 = E*/sqrt(2|c|):
  - photon 4.22e18 (axis), 5.44e18 (sky), 7.30e18 (body) GeV;
  - lepton or neutrino 2.43e18, 3.56e18, 7.30e18 GeV.

  | Source | Axis delay | Margin in E_QG,2 |
  |---|---|---|
  | GRB 090510, 31 GeV | 5e-17 s | 10^7.5 |
  | GRB 221009A, 13 TeV | 1e-12 s | 10^6.8 |
  | TXS 0506 neutrino, 290 TeV | 4e-9 s | 10^7.2 |

  - A 1 s delay from z = 1 needs a 3.9e18 eV photon, which is impossible (gamma -> e+e- and background absorption).
  - Direction pattern: cubic l = 4 in S. Delay(body)/delay(axis) = 1/3, and neutrinos arrive after photons.
    The lattice orientation relative to the sky is NOT supplied by the rules, so it is 3 free angles in any test.

##### Conclusion as stated in the note (source heading: "Verdict (pre-registered rules)")

- Time of flight (GRB, blazar, neutrino): SURVIVES, with a margin of >= 6.8 orders in E_QG,2 (>= 13.5 in delay).
  The quadratic delay can never be measured by time of flight.
- Photon sector: TESTABLE SOON.
  - The sharp prediction is a gamma -> e+e- cutoff at 0.8-1.1e17 eV, only 57x above the highest LHAASO photon.
  - It is absent within the body-diagonal cones.
  - One photon above ~1.2e17 eV from an off-body direction would falsify it. Running and planned tests: Auger/TA
    UHE photon searches, LHAASO-KM2A at its upper end, GRAND.
- UHECR sector: TESTABLE SOON. Nothing observed is excluded under the strict criterion, because protons survive to
  1e21 eV off the cones and no species-resolved flux above its dissociation energy is established. Predictions:
  - no photopion GZK horizon;
  - a mass-ordered breakup cutoff E ~ 1.8 A EeV (core) per species, with nucleons released at E/A;
  - an 8-fold set of 1.8 %-sky proton-depleted cones above ~5 EeV;
  - events above 1.6e20 eV (Amaterasu 2.44e20) must be protons, or nuclei above Fe.
  - Confronting Auger SD-DNN's heavy <lnA> ~ 3 at 50-100 EeV: N is broken up by 25-40 EeV, so survivors there
    are Si-Fe plus protons. This is IN TENSION if Auger's "no large light fraction" holds, and AugerPrime decides it.
- Overall: SURVIVES all current bounds. Sharpest LIV prediction: the composition and photon-cutoff pattern.
- [S] Coincidence, no claim: the core breakup scale of ~1.8 A EeV resembles Auger's fitted Peters-cycle cutoff
  Z x R_cut. With no GZK horizon, a 244 EeV proton from a void direction needs no nearby source.

##### Smuggling review

- Forced (upstream [F], or exact here):
  - c_g, c_q and the S pattern;
  - light-front placement of the LIV in the mass operator;
  - Hellmann-Feynman additivity;
  - the flow direction;
  - the lepton and photon inequalities;
  - the 1/96 ray-independence;
  - the body-diagonal degeneracy c_q = c_g.
- Supplied:
  - all binding models (m, kappa, g, m_g);
  - the physical masses that are shifted in;
  - S_n, k_F = 0.25 GeV, and the frozen-nucleon-level nucleus;
  - LCDM (H0 = 67.4, Om = 0.315);
  - source energies and redshifts, and all bound values;
  - the 10-day neutrino window;
  - the lattice orientation (unsupplied, so a free parameter).
- No rule is proposed, so there is no gate. Nothing is fitted.

##### Open

- Rates for vacuum dissociation and for the body-cone p -> p gamma; transverse dynamics; LIV inside the
  interaction kernel; the large-u value for gluon dressing; whether air-shower hadronic physics at 1e20 eV is
  altered (it would bias Xmax-based composition).

### #10091: Nuclear vacuum breakup under the rule-fixed dimension-six dispersion

**Kind of statement.** Mixed. T1 is exact algebra (sympy). The deuteron and the cluster-model openings are finite diagnostics in supplied exact light-front models (rank-one separable kernel with Yamaguchi parameter, two-body cluster model, measured separation energies); the decay lengths are complex-pole rates in those models; the comparison with Auger and Telescope Array composition is an estimate against measurement.

**Runner.** [../scripts/nuclear_vacuum_breakup_under_rule_fixed_dimension_six_liv_is_a_hard_wall_below_fifty_eev_2026_10_26.py](../scripts/nuclear_vacuum_breakup_under_rule_fixed_dimension_six_liv_is_a_hard_wall_below_fifty_eev_2026_10_26.py) (author-reported output only; not rerun in this consolidation).

**Dependencies.** Inherits c_q = -S/6 + 1/24 and E* = 1.217e18 GeV from the same upstream note as #10090 (not a PR here). Builds on #10090 (kinematic openings, flow of the proton) and on #10089 (nuclei contradicted). Depends on the universal-nucleon hypothesis c_N = c_q, bracketed by c_N = 0.214 c_q. Its closing statement is narrowed by #10093.

**Status within this theme.** The breakup opening energies, decay lengths and the withdrawal of the Fermi-core walls of #10090 stand in the supplied models. The statement "EXCLUDED unless the rules also alter air-shower development" is narrowed by #10093 to a tension that is decided by the air cross section of the flowed hadron, which neither note computes; see the Corrected or replaced claims section, entry 3. The minimal-rescue paragraph (a dimension-eight tick) is conditional and is qualified by #10092; see the Corrected or replaced claims section, entry 5.

**Scope as written in the note (verbatim `claim_scope`).**

> With the rule-fixed dimension-six dispersion (c_q = -S/6 + 1/24, E* = 1.217e18 GeV) and nucleons taken UNIVERSAL (c_N = c_q at all momenta; bracket c_N = 0.214 c_q): (i) [T] at matched velocities the free-nucleon and additive-bound LIV are identical (c P^3/A^2) and stationary; the breakup driver is second order, the negative curvature 6c/A of sum x^3 (convexity of x^3 with c < 0), not a first-order 'sum x^3 < 1' term; (ii) [F] exact light-front two-body diagonalisation at fixed P (rank-one separable kernel, x and k_perp, deuteron binding reproduced): the bound deuteron does not follow the flow (|c_eff|/|c| 0.253 -> 0.308, universal = 1) and dissolves at 2.5/3.0/4.3 EeV (axis/sky/body); (iii) [F] nucleon + core cluster model: breakup opens at t 3.3-5.7, 4He 4.1-7.0, 14N 8.6-15, 56Fe 18-31 EeV (x 1.47 at the weak-driver end), insensitive to the form-factor range (beta 0.2-0.4 GeV changes lam_open by < 3 %); (iv) [F] above opening the frozen nucleus is a resonance (N, Fe) or no pole at all (d, He) with decay lengths 1e-8 to 5e-3 m at 1.1-2 x P_open: a hard wall, 22 orders below kpc; (v) [E] above <= 46 EeV on every ray/beta/c_N corner the rules' UHECR flux is nucleons only, contradicting Auger's heavier-and-purer composition at 50-100 EeV. Verdict: EXCLUDED unless the rules also alter air-shower development (uncomputed).

**Statement, copied from the note.** (Headings are demoted; text is otherwise unchanged, except that runner pass counts are dropped and the source's "Verdict" wording is replaced by "conclusion" or "gate outcome".)

Criteria fixed before the run (criteria_pre_run.txt). Axioms unchanged; no CL edit; nothing adopted.
Labels: [T] exact, [F] finite diagnostic in a supplied exact model, [E] estimate vs measurement, [S] reading.
Pre-run deviation, stated: F1c's pre-written tolerance (within 10 % of additive) was too tight; the computed
slope reaches 1.23 x additive before the pole dissolves. The check was rewritten to "< 1/2 of universal" and
the number is reported. F1d was rewritten to accept the two degenerate (x*, 1-x*) minima of the symmetric case.

##### Builds on / narrows

- agents/liv-surviving-observables (A3c): its claim "nuclei cannot follow the flow" is CONFIRMED by an exact
  model, and its walls are SHARPENED DOWNWARD. Its kinematic openings (d 3.5-6, Fe 19-32 EeV) are reproduced
  (d slightly lower, 2.5-4.3). Its "Fermi core" walls (Fe 100-160 EeV) are WITHDRAWN: the exact width is not
  suppressed, so the wall is the kinematic opening.
- agents/composite-dispersion: its line "nuclei inherit the same flow [S]" stays contradicted.
- No prior main-branch work on vacuum dissociation (git grep origin/main, docs+scripts).

##### Results

- [T] T1 (sympy). A universal nucleons at P/A carry A c (P/A)^3 = c P^3/A^2, the same as the additive bound
  nucleus, and sum x^3 is stationary at x_i = 1/A. So the naive driver "sum x_i^3 < 1, nucleus less
  subluminal" is zero at matched velocities. The real driver is the Hessian 6c/A < 0: the LIV rewards
  unequal sharing. Unbound matched nucleons go locally unstable at lam|c| = M^2 A^4/3,
  P_inst = A (M^2 E*^2/6|c|)^(1/4) (A = 2: 2.3/2.8/4.0 EeV).
- [F] F1, deuteron. Exact at fixed P: separable kernel f = 1/(M0^2 - 4M^2 + 4 beta^2), beta = 0.286 GeV
  (Yamaguchi), strength fixed by B = 2.2246 MeV; the k_perp integral is closed form (matches 2D quadrature to
  2e-16), so the eigenvalue condition g I(z) = 1 is a 1D integral in x.
  - Bound-state slope dM_B^2/d(lam|c|) = -0.253, -0.260, -0.308 at 0, 0.5, 0.95 lam_open (additive -0.25,
    universal -1). The bound state barely follows.
  - The continuum minimum leaves x = 1/2 continuously (pitchfork at 16M^2/3 = 4.70 GeV^2). The pole meets it
    and dissolves at lam|c| = 6.60 GeV^2, i.e. P = 2.50e18 (axis), 3.03e18 (sky), 4.33e18 (body) eV.
- [F] F2, cluster N + (A-1), lowest single-nucleon separation energy (AME values, supplied), core at c/(A-1)^2.

  | Nucleus | lam_open|c| (GeV^2) | P_open axis / sky / body (EeV) | per nucleon, axis |
  |---|---|---|---|
  | t | 19.9 | 3.3 / 4.0 / 5.7 | 1.1 EeV |
  | 4He | 45.5 | 4.1 / 4.9 / 7.0 | 1.0 EeV |
  | 14N | 929 | 8.6 / 10.4 / 14.9 | 0.62 EeV |
  | 56Fe | 1.74e4 | 17.9 / 21.7 / 31.0 | 0.32 EeV |

  - beta = 0.2 / 0.4 GeV moves lam_open by < 3 %: the opening is kinematic (frozen pole vs the far minimum).
  - At the weak-driver end c_N = 0.214 c_q everywhere, all P x 1.47 (exact scaling): Fe <= 45.6 EeV.
  - The real nucleon has c_N(P/A) < c_q in the bound state, while the emitted fast nucleon is near c_q.
    That mixed case drives harder than either bracket, so the bracket's top is an upper bound.
- [F] R, rate. Complex pole of the exact amplitude, Gamma_M2 = 2 Im I/Re I', Gamma_lab = Gamma_M2/2P:

  | Nucleus | x1.1 P_open | x1.5 P_open | x2 P_open |
  |---|---|---|---|
  | 14N | L = 1.2 mm | 67 um | 9 um |
  | 56Fe | L = 5.1 mm | 1.3 mm | 0.27 mm |
  | 4He | no pole, L_form 2e-7 m | 2e-8 m | 7e-9 m |

  - Fe Gamma_M2 = 1.5e-3 GeV^2 at 1.1 P_open, narrow against the 1.07 GeV^2 gap.
  - The form-factor tail is power law, not exponential, so there is no Fermi-core suppression. It is a HARD
    WALL, about 22 orders below the kpc scale.
  - Products: one nucleon with most of P plus a cold core, which cascades on.
- [E] Confrontation (sources below).
  - Every nucleus t..56Fe is gone above <= 46 EeV on every ray/beta/c_N corner. Nuclei heavier than Fe extrapolate
    as P_open ~ A^0.53 (N -> Fe) and would need A ~ 250 for 100 EeV, so there are none in practice. The
    predicted flux above 50 EeV is protons and neutrons.
  - Auger SD + deep learning (arXiv:2406.06315, PRL 2025; PRD 111 companion arXiv:2406.06319): composition
    "increasingly heavier and purer", incompatible with a large light fraction between 50 and 100 EeV.
    Pure protons there would sit about 100 g/cm^2 deeper in <Xmax>, with sigma(Xmax) about 2x larger,
    several times the hadronic-model spread. EXCLUDED.
  - Amaterasu, 2.44e20 eV (TA, Science 382, 903 (2023), doi:10.1126/science.abo5095), and Fly's Eye,
    3.2 +- 0.9e20 eV (Bird et al., ApJ 441, 144 (1995); Xmax 815 g/cm^2 does not identify the primary):
    both must be protons under the rules. That is CONSISTENT on its own, since there is no GZK horizon
    upstream, but it is not a rescue.
  - TA hybrid composition is light below 10^19.1 and statistics-limited above (arXiv:1810.00431,
    arXiv:2209.03591). It is NOT in conflict, and it does not offset Auger.

##### Conclusion as stated in the note (source heading: "Verdict (pre-registered): BREAKUP REAL; HARD WALL; EXCLUDED by Auger 50-100 EeV composition")

- Caveat that could reopen it: the flowed proton (one quark at x ~ 1) might develop air showers differently,
  biasing the Xmax-based lnA. That is uncomputed and should be the next probe.
- Minimal rescue in rule terms (UNTESTED, gate below). The driver is the dimension-six term itself (the
  negative curvature of c x^3). The minimal rule-level cure is to make the update's leading lattice correction
  vanish at order p^4 for every species, e.g. a symmetric two-rung composition of the tick (zoom first). The
  first surviving term is then dimension eight. The same analysis gives
  P_inst = A (M^2 E*^4/20|c8|)^(1/6) ~ 1e21 A eV, so Fe ~ 1e22 eV, safely above every event, and time of
  flight becomes unmeasurable.
  - Gate: no number chosen, no observed structure named, bends no axiom (CL-1 condition). Its untested
    prediction is that the c pattern, the 1e17 eV gamma -> e+e- cutoff and the body cones of the parent note
    all disappear.
  - Alternatives not preferred: flipping the sign of c (superluminal; concave x^3 stabilises nuclei, but it
    reopens vacuum Cherenkov for e at ~5e16 eV) or raising E* by ~30x (a fitted number, gate FAIL).

##### Smuggling review

- Forced or exact: c_q pattern and E* (upstream); the light-front placement lam sum c x^3; T1 algebra; the
  closed-form k_perp integral; the pole and width formulas.
- Supplied:
  - the universal-nucleon hypothesis, bracketed by 0.214 c_q;
  - the rank-one separable kernel and its invariant-mass form factor (beta);
  - measured separation energies;
  - the core at its additive c/(A-1)^2, a two-body cluster model for A >= 3, and no LIV in the kernel;
  - the Auger/TA/Fly's Eye values.
- Nothing is fitted. No rule is adopted.

##### Open

- Air-shower Xmax of a flowed proton, and of nucleons from breakup.
- A three-body light-front nucleus with transverse dynamics, as a check on the cluster model.
- The LIV in the NN kernel.
- Building and testing the dimension-eight (p^4-cancelling) tick.

### #10092: Finite-band ticks cannot be exactly relativistic; an exact fixed point exists at history level

**Kind of statement.** Mixed. T1 and T2 are exact. The history-level fixed-point construction is a finite numerical diagnostic of a kernel built by proper-time image sums (dispersion to 9e-11, null cone to 4e-15, Ginsparg-Wilson relation to 4e-16, truncation overlaps, 2D U(1) index). The estimates against measurement use supplied one-loop sizes (C of order 1 assumed) and walls inherited from #10091. The proposed rule text in the note is untested and is a proposal, not a result.

**Runner.** [../scripts/zoom_fixed_point_tick_is_exactly_perfect_only_at_history_level_finite_band_ticks_keep_liv_2026_10_26.py](../scripts/zoom_fixed_point_tick_is_exactly_perfect_only_at_history_level_finite_band_ticks_keep_liv_2026_10_26.py) (author-reported output only; not rerun in this consolidation).

**Dependencies.** Inputs from #10091 (walls, the scaling of the opening energy with the coefficient, the dimension-eight formula) and from the same upstream assumed-inputs-model note as #10090. Cross-theme: the note says the overlap in #10049 (theme chirality-doublers) becomes redundant if its kernel is the fixed point; #10098 and #10111 (theme d4-route) cite T1 and T2 and reuse the method, and #10099 and #10110 (theme d4-route) reuse #10098's kernel, and #10094 (d4-route) states that it closes the radiative dimension-six item by a symmetry on that route. The index theorem in four dimensions is cited from the literature, not rederived.

**Status within this theme.** Stands as written. The tree-level rescue is complete only for free matter; radiative protection is a condition, not a result. The note itself says its exact weight needs an infinite image tower of poles, whose compatibility with one qubit per site is left as an owner decision.

**Scope as written in the note (verbatim `claim_scope`).**

> (T1) No update with finitely many bands per cell and real-analytic (exponentially local) Bloch unitary or Hamiltonian has an exactly relativistic lowest band on any open momentum set; Lorentz violation survives at some finite order, so a tick cannot be the zoom's fixed point. (T2) Block averaging keeps every physical pole; zooming sends lattice-unit coefficients to c0/B^2 but leaves the finest rung's physical Lorentz violation unchanged. (F) At history level the free blocking fixed point exists exactly in d = 3+1. It was built in momentum space by proper-time-factorised image sums: lowest band relativistic to 9e-11 (scalar and fermion, m = 0 and 0.3, |p| <= pi/2), on the metric null cone in a constant anisotropic metric (4e-15); fermion couplings exponentially local (kappa 2.7 at alpha = 1/2, 1.8 at alpha = 1); Ginsparg-Wilson exact (4e-16); no doublers; the overlap of the perfect kernel is the kernel itself (3e-16). Truncated to range R, its overlap c falls from 2e-2 to 3e-7 (R = 1..5) but is nonzero; the Wilson-kernel overlap has c = -(S+1)/6. A gauged hypercube truncation gives index Q = 0, 1, 2 exactly in 2D U(1). (E) The tree-level rescue is complete for free matter only. Radiative dimension-six terms with one-loop size alpha/4pi (5.8e-4 to 1.6e-3) would put 14N breakup at 48-84 EeV, against the < 5.5e-5 to 4.9e-4 needed; protecting them takes a dressed condition, which is not a theorem. Verdict: PARTIAL.

**Statement, copied from the note.** (Headings are demoted; text is otherwise unchanged, except that runner pass counts are dropped and the source's "Verdict" wording is replaced by "conclusion" or "gate outcome".)

Criteria were fixed before the run (criteria_pre_run.txt). It was re-run under a unique filename with identical output.

Labels: [T] exact or theorem, [F] finite diagnostic, [E] estimate against measurement, [S] reading.
The axioms are unchanged, CL is not edited, and nothing is adopted.

Pre-run deviation, stated:
- P5b used the alpha = 1/2 kernel, because the alpha = 1 truncations converge too slowly in R for an R <= 7 test (c = 0.12, 0.08, 0.05, 0.02 at R = 4..7).
- My first in-run threshold (dec[3] < 1e-4 dec[0]) was stricter than the pre-registered P5 condition. It was reset to the pre-registered "nonzero, reduced against Wilson, falling", with numbers reported.

##### Builds on, uses, contradicts

- Inputs: agents/nuclear-vacuum-breakup (walls; the scaling P_open ~ |c|^(-1/4); the dimension-eight formula) and agents/assumed-inputs-model section 3 (c_g = -S/24, c6, E* = 1.217e18 GeV).
- main: docs/ADMISSIBILITY_DIRAC_KAHLER_WICK_PHASE_FINE_SITE_STAGGERED_OS_LORENTZ_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md lists "an anisotropic/perfect action" as a live completion that it does not select. This note tests that completion and narrows it (T1).
- No main note on block-spin fixed points or perfect actions (git grep origin/main: 0 hits for perfect action, Bietenholz, or blocking fixed point). The 14 Ginsparg-Wilson notes are not contradicted.
- Open PR #10049 (overlap from the walk): P4b makes its overlap step redundant if the kernel is the fixed point.
- agents/repaired-kernel-anomaly: the repaired kernel (r_s = 1/3, T-even pieces) would be replaced.
- Literature, supplied:
  - Hasenfratz-Niedermayer, NPB 414 (1994) 785;
  - Bietenholz-Wiese, NPB 464 (1996) 319;
  - Ginsparg-Wilson, PRD 25 (1982) 2649;
  - Hasenfratz-Laliena-Niedermayer, PLB 427 (1998) 125 (index theorem for fixed-point operators);
  - Collins-Perez-Sudarsky-Urrutia-Vucetich, PRL 93 (2004) 191301;
  - Chadha-Nielsen, NPB 217 (1983) 125.

##### Theorems

**[T] T1, the finite-band no-go.**
- Setting: U(p) is an N x N Bloch unitary (or Hamiltonian), real-analytic and 2pi-periodic in p. Real-analytic is the same as exponentially local couplings.
- Claim: if one eigenvalue equals exp(-i tau sqrt(p^2 + m^2)) on an open set, then P(p, z) = det(z - U(p)) vanishes on g(p) = exp(-i tau E(p)) there.
- By analyticity, P(p, g(p)) = 0 on all of R^3 (on R^3 minus the origin for m = 0, which is still connected for d >= 2).
- By periodicity, every image g(p + 2 pi l) is also a root of P(p, .).
- Two images agree identically only if E_l - E_l' is constant on an open set, which is impossible for l != l'.
- So P has infinitely many distinct roots, against its N roots. Contradiction.
- Hence some Taylor order of the lowest band is Lorentz-violating, for any finite range or exponential tail and any number of sites per cell.
- Lemma check: 343 images are distinct at a random p (P5c).
- Corollary: an exactly perfect band needs the infinite image tower Sum_l of the perfect propagator, meaning states of every momentum |p + 2 pi l|. That is a continuum folded under the sites. It is not available to a tick on one qubit per site.

**[T] T2, zooming keeps physical poles.**
- The blocked propagator is a positive weighted sum of fine propagators at preimage momenta. So its poles are the fine poles.
- In coarse-lattice units c_B = c0/B^2. P2c gives c_B B^2 = -1/12 for B = 1..8, equal to c0 = -(S+1)/24 on the axis.
- The zoom fixed point is therefore the infrared attractor of lattice-unit coefficients. In physical units E* the finest rung's Lorentz violation is unchanged.
- "Finest tick = fixed point" means the finest rung is the zoom of an infinitely finer theory. That is T1's continuum again.

##### Finite diagnostics in d = 3+1, exact construction

- Construction:
  - G*(p) = Sum_l Prod_mu s(q_mu)^2 / q^2 (+ alpha), with q = p + 2 pi l and s(q) = sin(q/2)/(q/2), for 2x2x2-cube (factor-B) averaging.
  - Proper time factorises the image sum into 1D sums.
  - The 1D sums are done in closed Poisson/erfc form, matching a direct 4e4-term sum to 3e-16.
  - The fermion is G* = -i gamma.rho + alpha, D = G*^(-1).
- P1, exact dispersion: the lowest band read from the lattice time correlator equals sqrt(p^2 + m^2) to 9.0e-11.
  - This holds for scalar and fermion, m = 0 and 0.3, at 0.3 (axis), pi/4 (face) and pi/2 (body).
  - It is independent of alpha, which only moves the t = 0 contact term.
  - In a constant metric gamma^ii = (1.7, 0.6, 1) the pole lies on the metric null cone (4e-15).
- P2, the zoom flow: the iterated factor-2 map equals closed-form B = 4 blocking (2e-16).
  - Starting from the naive scalar, the flow converges to G*.
  - |G_B - G*| = 2.8e-2, 7.2e-3, 1.8e-3, 4.5e-4 for B = 2..16, ratio 4.00. This is the p^4 operator being irrelevant.
- P3, locality: the fermion couplings decay as exp(-kappa r), with kappa = 2.74 per spacing (alpha = 1/2) and 1.76 (alpha = 1), along the axis and similarly along the diagonal.
- P4, chiral structure:
  - Ginsparg-Wilson gamma5 D + D gamma5 = 2 alpha D gamma5 D holds to 4e-16, and gamma5-hermiticity is exact.
  - The overlap with m0 = 1/(2 alpha) returns D* itself (3e-16).
  - The 15 corners sit at D = 1/alpha (rho = 0 to 1e-10), and |rho| <= 0.40 wherever |p|_inf >= pi/2. So there is one light cone, at p = 0, and no doublers.
- P5, finite range:
  - The Wilson-kernel overlap has sinh w = |sin p|, so c = -(S+1)/6 (sympy): -1/3 on the axis, -2/9 on the body diagonal. Ginsparg-Wilson alone does not remove the dimension-six term.
  - Range-R truncations of D* (alpha = 1/2) used as overlap kernels have
    - c_axis = 2.0e-2, 7.8e-3, -9.4e-5, -2.4e-6, 3.1e-7 for R = 1..5 (body about 2/3 of these).
    - These are exponentially small but nonzero, as T1 requires.
- P6, chiral content: a 2D U(1) torus 8x8 with flux Q = 0, 1, 2 plus seeded noise of 0.25 rad per link. The overlap on the gauged hypercube-truncated perfect kernel has index 0.000000, -1.000000, -2.000000, and GW holds to 2e-15.
  - The 4D gauged index and domain-wall content were not computed. They are supplied by Hasenfratz-Laliena-Niedermayer for fixed-point operators.
- P7, sympy, range-2 improved ticks (fixed point through the first irrelevant order):
  - The link band 4s^2 + (4/3)s^4 has zero p^4; c8 = -1/180 S6, i.e. -0.0056 on the axis.
  - The fermion sin p + sin^3 p/6 has zero p^3; c8 = -(3/40) S6, i.e. -0.075 on the axis.
  - The lattice-time (step) piece must be cancelled as well, for example by a symmetric two-rung composition. That is not built here.
  - The c8 values depend on which improvement is chosen. They are illustrative, not predictions.

##### What else the rules need [S/E]

- Chirality: unchanged in kind. The perfect kernel is already Ginsparg-Wilson, so Luscher's projector and the index (P6, 2D) carry over.
- Gravity:
  - The CL-3 hinge sum, the tick fraction and offsets, and the six-edge carrier read only edges. They are unchanged.
  - The derived weak-field results (gamma = beta = 1, Nordtvedt 0, frame dragging, two tensor waves, one G) use only the dimension-<=4 matter coupling, which the perfect weight reproduces exactly (P1b: matter on the edges' null cone).
  - The tensor waves keep their tick-level (ka)^2/24 correction. That is untested and unconstrained (GW170817 probes (E/E*)^2 ~ 1e-80).
  - The wave-speed-equals-light statement still needs CL-1's tick/edge ratio clause for the edges.
- Links: the photon and gluon band c_g comes from Hamiltonian ring-exchange registers. Under T1 it cannot be made perfect at tick level. A history-level perfect gauge weight (Bietenholz-Wiese free U(1)) exists classically but is not built or tested here for the registers.
- Interactions:
  - The classically perfect action is perfect at tree level only. Loops on a lattice regulator generate every term the kept cubic group allows.
  - Dimension four, unsuppressed (Collins et al.): delta c ~ alpha/pi. This is already met by the register's dressed-cone clause, a renormalisation condition. Chadha-Nielsen infrared attraction is only logarithmic.
  - Dimension six: kappa ~ g^2/16pi^2 x C, with C uncomputed.
  - The renormalized trajectory (the quantum perfect action) would protect every order. But it is the zoom of an existing continuum theory: T1/T2 again. It is not strictly defined for non-asymptotically-free sectors (hypercharge, the Higgs quartic), and the edge sector sits at no fixed point.
  - Shown: tree-level perfection and the scaling. Not shown: radiative protection.

##### UHECR consequences [E]

- Residual dimension-six term kappa c, with walls scaling as kappa^(-1/4); axis-body EeV:

  | kappa | factor | d | 4He | 14N | 56Fe |
  |---|---|---|---|---|---|
  | 1e-2 | x3.16 | 8-14 | 13-22 | 27-47 | 57-98 |
  | 1e-3 | x5.62 | 14-24 | 23-39 | 48-84 | 101-174 |
  | 1e-4 | x10 | 25-43 | 41-70 | 86-149 | 179-310 |

  - 14N survives to 100 EeV on every ray only if kappa < 5.5e-5 (axis) or 4.9e-4 (body).
  - One-loop sizes: alpha_em/4pi 5.8e-4, alpha_s(E*)/4pi ~ 1.6e-3, (E*/M_P)^2/16pi^2 6.3e-5.
  - So an unprotected dimension-six term with C ~ 1 is EXCLUDED or borderline by Auger 50-100 EeV, and a dressed condition is needed.
- Dimension-eight residual only (dressed condition held):
  - Nuclear instability sets in above 2.1e21 (d), 4.2e21 (He), 1.5e22 (N) and 5.8e22 (Fe) eV at |c8| = 0.075. That is safe above every event, including Amaterasu at 2.4e20.
  - gamma -> e+e- opens at about 1.8e20 eV or not at all; the rules as written open it at 80 PeV.
  - Time of flight is unmeasurable (2e-51 s for a 10 GeV GRB photon).
  - Proton photopion (GZK) reopens: c8 E^6/E*^4 ~ 1e-9 GeV^2, far below m_pi m_p. This withdraws model.md's "no GZK" prediction, and cosmogenic EeV neutrinos come back.

##### Simplification ledger

The items below are conditional on the matter weight being the zoom fixed point.

- Deleted if the matter weight is the zoom fixed point (3):
  - the walk-to-Wilson-kernel identification;
  - the m0 window (0 < m0 < 2/3), since m0 = 1/2alpha is forced;
  - the repaired kernel (r_s = 1/3, T-even pieces). The overlap step itself becomes an identity (P4b).
- Absorbed (1): the dressed-cone clause becomes a special case of the dressed fixed-point clause.
- Unchanged:
  - the edge-window repairs and the window;
  - the polar split;
  - the copy mass's copy-selection role. Its dimension-six band role leaves matter propagation, but whether it is still needed for one light copy under a per-field perfect weight is UNTESTED.
- Added: alpha (a blocking-scheme constant, physically inert: P1 shows the spectrum does not depend on it; locality is best near 1/2), plus the clause.
- Net: about -3 supplied items, +1 inert constant.

##### Conclusion as stated in the note (source heading: "Verdict (pre-registered rule): PARTIAL")

- An exactly perfect TICK is impossible on finite bands (T1), and zooming cannot remove the finest rung's physical Lorentz violation (T2).
- The exact fixed point exists at HISTORY level, where the register already weights matter. There it is p^4-free to all orders for free matter, local, GW, doubler-free, index-correct (2D), and it deletes 3 items.
- Radiative protection is a condition, not a theorem.

Proposed CL text (UNTESTED, not adopted). "Each species' dressed two-point weight, link and edge dressing included, is fixed under the zoom (averaging over the even tiling's 2x2x2 cubes) through its first irrelevant order: its dressed cone is the edges' null cone and its dressed dimension-six term vanishes. The free matter history weight is the zoom's exact fixed point."

Gate:
- (1) No fitted number. The improvement coefficients are forced. alpha is inert for the spectrum.
- (2) No observed structure named.
- (3) Untested predictions:
  - no dimension-six LIV in any species;
  - gamma -> ee threshold >= ~1e20 eV;
  - nuclei stable below ~1e21 A eV;
  - GZK photopion and cosmogenic neutrinos restored;
  - cubic dimension-eight pattern.
- (4) It bends CL-1's dressed-cone clause (extended one order) and CL-1's tick reading for matter, already bent by the history-level weighting.
- Owner decision: the exact free history weight has an infinite image tower of poles, meaning states beyond the cell scale. Whether that reading bends one-qubit-per-site is an owner decision. The finite-order clause does not need it.
- The note's gate outcome is conditional on that reading.

##### Smuggling review

- Forced or exact: T1, T2; the image-sum construction; the GW, overlap-identity and doubler results; the c = -(S+1)/6 formula; the improvement coefficients.
- Supplied:
  - alpha (inert);
  - the Gaussian blocking form;
  - the literature index theorem in 4D;
  - one-loop size estimates (C ~ 1 assumed);
  - nuclear walls inherited;
  - c8 example values.
- Nothing is fitted.

##### Open

- One-loop dimension-six coefficient C on the rules' regulator. This is decisive at kappa ~ 1e-4.
- A history-level perfect weight for the link registers.
- A symmetric two-rung tick cancelling the step's dimension-six piece.
- 4D gauged index with the perfect kernel.
- Does the per-field perfect weight make the copy mass redundant?

### #10093: Raw Xmax above 46 EeV and a flowed-proton beam

**Kind of statement.** Numerical diagnostic in a supplied model. It uses a seeded generalized Heitler-Matthews toy calibrated on each hadronic model's proton and iron moments, with the flowed hadron's cross-section factor, elasticity and multiplicity factor supplied as brackets (not derived from the rules). The comparison is with published raw Xmax moments.

**Runner.** [../scripts/raw_xmax_sigma_above_46_eev_flowed_proton_beam_tension_2026_10_26.py](../scripts/raw_xmax_sigma_above_46_eev_flowed_proton_beam_tension_2026_10_26.py) (author-reported output only; not rerun in this consolidation).

**Dependencies.** Depends on #10091 (the breakup wall below 46 EeV) and on #10090 and #10089 (the leading-quark momentum fraction x_lead from the three-body residual, scaled as P^-2). All Auger data values and hadronic-model parametrizations are supplied from the literature as quoted in the note.

**Status within this theme.** Narrows the closing statement of #10091. The cross section of the flowed hadron is not computed in any note of this theme; the conclusion depends on it. The scope's "within 1.6 sigma" for f_sigma 4 to 8 holds for the better corners only: the note's results text and the cached output give worst pulls up to 1.8 (f_sigma = 4) and 2.4 (f_sigma = 8); see the Corrected or replaced claims section, entry 3.

**Scope as written in the note (verbatim `claim_scope`).**

> Against Auger's raw Xmax moments above 46 EeV (SD-DNN calibrated to FD, arXiv:2406.06319 Table 4: lgE 19.74/19.85/20.00, <Xmax> 787.2/794.5/793.9, sigma 20.7/25.1/21.8 g/cm^2; FD cross-check lgE>=19.5, 779.8 +- 5.0, sigma 26.5 +- 4.8, arXiv:1409.4809) and post-LHC p/Fe moments (generalized-Gumbel parametrization, arXiv:1903.03174), a seeded generalized Heitler-Matthews toy, calibrated two-point on each model's p and Fe, gives for a pure beam of flowed protons (x_lead = 0.995-0.998 at 46 EeV, 0.9990-0.9997 at 1e20 eV, from the upstream residual r ~ P^-2): (i) [F] a transparent flowed hadron (elasticity 1 - (1-x_lead)/2) does not make normal showers (Xmax > 1500 g/cm^2 in > 50 % of events): excluded outright; (ii) [F] every corner with flowed cross-section factor f_sigma <= 1 is excluded (worst pull >= 4.2, sigma(Xmax) decides); (iii) [F] the best pre-registered corner (f_sigma = 2) misses sigma(Xmax) by 2.2 combined sigma: TENSION; f_sigma 4-8 (post-registration extension) fits both moments within 1.6 sigma; (iv) [F] in every fitting corner N_mu is proton-like (0.97-1.01 x standard proton, while toy Fe/p = 1.19). Verdict: TENSION, not EXCLUDED; the decisive unknown is the air cross section of the flowed hadron, which the rules have not yet computed (no transverse dynamics upstream).

**Statement, copied from the note.** (Headings are demoted; text is otherwise unchanged, except that runner pass counts are dropped and the source's "Verdict" wording is replaced by "conclusion" or "gate outcome".)

Criteria fixed before any data fetch or run (criteria_pre_run.txt). Axioms unchanged; no CL edit; nothing adopted.
Labels: [T] exact, [F] finite diagnostic in a supplied model, [E] estimate vs measurement, [S] reading.

##### Builds on / narrows

- agents/nuclear-vacuum-breakup: its conclusion "EXCLUDED unless the rules also alter air-shower development
  (uncomputed)" is NARROWED to TENSION. Its stated caveat is real: the flowed state changes the first
  interactions, and through them the Xmax-based reading of lnA.
- agents/composite-dispersion and agents/liv-surviving-observables supply x_lead. The 3-body residual
  1 - c_B/c_q = 0.001-0.003 at 1e20 eV, scaled as P^-2, reproduces their 1e19 value (0.10-0.30 vs 0.10-0.28).
  With two equal soft constituents, 1 - x_lead = r/3.

##### Raw data used (RAW = detector-level moments, corrected for acceptance and resolution only)

- Auger SD-DNN, arXiv:2406.06319 (PRD 111 companion), Table 4. This Xmax is SD-estimated but calibrated to the FD
  scale; the DNN is trained on simulated showers, which is a caveat for exotic showers.

  | lgE bin | <lgE> | <Xmax> (stat; sys) | sigma (stat; sys) | N |
  |---|---|---|---|---|
  | 19.7-19.8 | 19.74 | 787.2 +- 2.0 (-7.5, +11.6) | 20.7 +- 1.4 (-4.8, +6.8) | 113 |
  | 19.8-19.9 | 19.85 | 794.5 +- 3.6 (-7.8, +12.2) | 25.1 +- 3.9 (-4.8, +6.8) | 54 |
  | > 19.9 | 20.00 | 793.9 +- 4.5 (-8.3, +13.1) | 21.8 +- 5.4 (-4.8, +6.8) | 26 |

  The DNN event-count column for 19.7-19.8 was ambiguous in the fetched text.
- Auger FD direct fluorescence, arXiv:1409.4809 (PRD 90, 122005), Table 4. The last bin is lgE >= 19.5 (<lgE> 19.62,
  N = 37): <Xmax> 779.8 +- 5.0 (+9.4/-6.9), sigma 26.5 +- 4.8 (+1.5/-1.6). The ICRC 2023 FD update
  (PoS(ICRC2023)319, 75210 events) gives its values in figures only, so it is not tabulated here.
- Model p/Fe moments: Arbeletche & de Souza, arXiv:1903.03174, Table 6 (generalized Gumbel; moments are mu + s(ln
  lam - psi(lam)) and s sqrt(psi'(lam))). As a check, the parametrization reproduces the ICRC 2013 Auger anchors
  (EPOS-LHC 806.1, QGSJetII-04 790.4 at 1e19 eV) within 1 g/cm^2.
  - At 10^19.74 the proton prediction is ~831 / 847 / 861 (QGSJetII-04 / EPOS-LHC / Sibyll2.3c), with
    sigma ~ 57-60. Iron is 736-760, with sigma 16.5-21.8.
- Muons: Auger hybrid 6-16 EeV (PRL 117, 192001; arXiv:1610.08509) found the hadronic signal 1.33 +- 0.16
  (1.61 +- 0.21) x EPOS-LHC (QGSJetII-04). There is no published muon number above 46 EeV.
- Auger arXiv:2401.10740 (10^18.5-10^19, 2239 hybrid events) prefers model Xmax shifted DEEPER (> 5 sigma). Any
  such shift only pushes every proton-like prediction further from the data, so it is not used to help the rules.
- TA hybrid above 10^19.5 is statistics-limited (parent note). It does not decide.

##### Results

- [F] A, model check: proton/iron moments as above.
- [F] C, toy calibration.
  - The toy proton has sigma 53.4.
  - The variance mapping sigma^2 = sigma_p,model^2 + (toy^2 - toy_p^2) gives Fe sigma 26.5/21.8/28.6 against the
    model 21.8/16.5/21.3. So the toy OVER-estimates sigma for multi-subshower showers by about 5-7 g/cm^2.
    This bias works AGAINST the rules.
  - The mean is mapped two-point per model (p and Fe).
- [F] D, flowed corners. Values are (f_sigma, kappa, f_N): prediction at 19.74 for <X> and sigma | worst pull
  over the three bins:
  - f_sigma = 1/3: 1018-1079, 150-185 | 5.6-6.6, 13.9-16.0. Excluded (a single-quark cross section).
  - f_sigma = 1: 823-893, 53-58 | 4.2-4.9 on sigma. Excluded (a flowed proton is still a single-particle shower).
  - kappa = 1 - (1-x_lead)/2 (transparent): Xmax 2400-3300, every shower lost. Excluded outright.
  - f_sigma = 2, standard kappa: 771-830, 32-34 | 0.4-1.7 on X, 2.2-2.5 on sigma. TENSION.
  - Extended (post-registration, stated): f_sigma = 4 gives 743-799, 27-28 | <= 1.8; f_sigma = 8 gives 731-789,
    26 | <= 2.4. Low elasticity U(0, 0.4) changes little.
  - N_mu/N_mu,p = 0.97-1.01 in every non-transparent corner, against toy Fe/p 1.19 (the toy understates the
    model value of ~1.3-1.4).
- [F] E: pure standard protons give worst pulls of 2.0 on <X> and 4.9 on sigma. <Xmax> alone does NOT exclude
  protons once the three-model spread (~30 g/cm^2) is included; sigma(Xmax) does.
- [F] G, FD cross-check (lgE >= 19.5).
  - Best pre-registered corner: 830 / 36, pulls 1.6 / 1.2.
  - Standard proton: 840 / 59, pull 5.2 on sigma.
  - The direct-fluorescence bin agrees with the DNN.

##### Conclusion as stated in the note (source heading: "Verdict (pre-registered rule: the most favourable pre-registered corner decides)")

Decision rule fixed before the run: the most favourable pre-registered corner decides.

TENSION (2.2 combined sigma). The deciding measurement is sigma(Xmax) in the SD-DNN 19.7-19.8 bin (20.7 +- 1.4, +6.8
sys, 113 events), backed by FD lgE >= 19.5 (26.5 +- 4.8).
- With the toy's known +5-7 g/cm^2 sigma over-estimate removed, or with f_sigma >= 4, it becomes CONSISTENT.
- With f_sigma <= 1 it is EXCLUDED at >= 4.2 sigma.
- So the parent's EXCLUDED rests on an assumption, not a measurement: the flowed hadron interacting like a standard
  proton.

The question becomes whether the flowed hadron's inelastic air cross section is >= ~2 x sigma_p-air (>= ~1.1 b at
1e19.7 eV), with standard (string-breaking) elasticity.
- [S] This is not implausible in rule terms. In a light-front picture with confinement in the boost-invariant
  variable zeta^2 = x(1-x) b^2, the soft constituent at x_s ~ (1-x_lead)/2 ~ 1e-3 sits at b ~ b0/sqrt(x_s), about
  30 b0. A color string from the leading quark across 10-20 fm would be broken by most passing air nuclei, which
  gives a large sigma, and each break re-fragments the leading quark (kappa ~ standard).
- If instead the cloud is stripped without disturbing the leading quark, the shower never develops (corner i),
  which is excluded.
- Neither transverse picture is derived. Upstream has longitudinal dynamics only.

##### What AugerPrime adds

SSD + WCD (+ radio) give a per-event muon/EM split above 46 EeV. A flowed-proton beam that mimics heavy Xmax keeps
a PROTON-like muon number: in the toy, N_mu is about 1.0 x proton against about 1.2-1.4 for Fe. So the falsifier is a
joint (Xmax-like-heavy, N_mu-like-proton) signature. Given the existing 6-16 EeV muon excess (1.33-1.61 x models),
a proton-like N_mu above 46 EeV would deepen the muon deficit sharply. If AugerPrime finds N_mu rising toward
heavy values with energy, the flowed-proton escape closes. A second test is the shape of the Xmax distribution: for
f_sigma = 2 the deep tail is exponential with slope ~ lambda_p/2 ~ 20 g/cm^2, which is distinguishable from a
Gaussian-like heavy peak only with >~ 1e3 events.

##### Smuggling review

- Forced or upstream: x_lead (r ~ P^-2 from the 3-body FEM); the flow threshold 5e18 eV (half-way scale); the
  breakup wall <= 46 EeV.
- Supplied:
  - the whole toy (lambda_p from Auger's 505 mb at 10^18.24 with E^0.045, N_ch = 41.2 (E/PeV)^0.2, kappa ~ U(0.1, 0.8),
    1/3 to pi0, Greisen profiles, pion decay at 20 GeV);
  - the bracket f_sigma, kappa, f_N, which is NOT derived from the rules;
  - the two-point calibration to model p/Fe;
  - the data and parametrizations.
- Nothing is fitted to the >46 EeV data. No rule is proposed, so there is no gate.
- Deviation from the pre-registration: the f_sigma >= 4 and kappa-low corners were added after the run and are
  labelled extended; the conclusion uses the pre-registered grid only.

##### Open

- Derive the flowed hadron's transverse size and its air cross section from the rules (3-body light-front with
  transverse dynamics, kernel LIV).
- The muon number above 46 EeV (AugerPrime).
- The Xmax tail slope.
- A full Monte Carlo (CONEX with a modified first-interaction generator) to replace the toy.

## Corrected or replaced claims

# Corrections and conflicts: relativistic cones and dispersion tests

Each entry gives what was withdrawn or corrected, by which PR, and the form that stands. All statements are author statements from the source notes, in their supplied models.

## 1. Labels used by the source notes do not match the reference register

Several notes in this theme (#9872, #9878, #9888, #9891, #9913, #9916, #10066, #10087 to #10093) refer to "the candidate-law register", "CL-1", "CL-3", "the register's tick law" or "the one-G clause" for a tick, a link law, a photon clause or a dimension-six dispersion rule. In `docs/CANDIDATE_LAWS.md`, CL-1 is the lossless-influence clause, CL-2 the record-removal clause and CL-3 a pending conservation proposal; the file contains no tick, link or dispersion rule. The label "CL-1" in these notes (for example "CL-1's dimension-six dispersion", "CL-1's 24 rotations", "CL-1's tick/edge ratio clause") therefore cannot be read as the entry of that name in the reference file. In this consolidation each such rule is treated as a supplied rule of the note that uses it. #10092 also contains a proposed rule text marked "UNTESTED, not adopted"; it is a proposal and not a result.

## 2. #10090, corrected by #10091: nuclear dissociation

Withdrawn by #10091: the Fermi-core dissociation walls of #10090 (reaching the core at He 7 to 13, N 25 to 40, Fe 100 to 160 EeV, "about 1.8 A EeV"), and the statement that survivors at 50 to 100 EeV are Si to Fe plus protons because N is broken up by 25 to 40 EeV.

Form that stands (#10091, supplied models: nucleons universal with c_N = c_q, bracket c_N = 0.214 c_q; a two-body cluster model; measured separation energies): breakup opens at the kinematic opening, with no Fermi-core suppression, at (axis / sky / body) t 3.3 / 4.0 / 5.7, 4He 4.1 / 4.9 / 7.0, 14N 8.6 / 10.4 / 14.9 and 56Fe 17.9 / 21.7 / 31.0 EeV; at the weak-driver end all energies are multiplied by 1.47 (Fe at most 45.6 EeV). The exact deuteron model dissolves at 2.50 / 3.03 / 4.33 EeV. Decay lengths from the complex pole: 14N 1.2 mm to 9 um and 56Fe 5.1 mm to 0.27 mm between 1.1 and 2 times the opening momentum; 4He has no pole (formation length 2e-7 m to 7e-9 m). #10091 states that #10090's kinematic openings for d (3.5 to 6 EeV) and Fe (19 to 32 EeV) are reproduced, with the deuteron slightly lower (2.5 to 4.3 EeV); its cluster model gives lower values than #10090's He (5.3 to 8.9 EeV) and N (9.4 to 17 EeV), namely He 4.1 to 7.0 and N 8.6 to 15 EeV.

Also not standing: the effective Fe wall of 50 to 160 EeV; the mass-ordered cutoff at about 1.8 A EeV with nucleons released at E/A; its resemblance to Auger's fitted cutoff; and "or nuclei above Fe" for events above 1.6e20 eV (#10091: such events must be protons under the rules, and nuclei heavier than Fe would need A of about 250 for 100 EeV). In the #10091 model the products are one nucleon with most of P plus a cold core, not nucleons at E/A each. Neither note computes the resulting flux spectrum.

Not replaced in #10090: the three-body proton results, gluon dressing, the lepton and photon inequalities, the gamma to pair opening at 8.0e16 eV (axis) to 1.1e17 eV (sky) and never on body diagonals, and the time-of-flight margins. The statement that photopion on the CMB is closed at all energies holds for the dimension-six rules only (entry 6).

## 3. #10091, narrowed by #10093: the composition conclusion

#10091 states that nuclei from t to 56Fe are gone above at most 46 EeV and that the flux is nucleons only, and concludes "EXCLUDED unless the rules also alter air-shower development (uncomputed)". #10093 narrows this. In a seeded generalized Heitler-Matthews toy, calibrated on each hadronic model's proton and iron moments, and against raw Xmax moments above 46 EeV (SD-DNN calibrated to FD): a transparent flowed hadron is excluded outright; every corner with cross-section factor f_sigma at most 1 is excluded (worst pull at least 4.2, decided by sigma(Xmax)); the best preregistered corner (f_sigma = 2) misses sigma(Xmax) by 2.2 combined sigma, which the note labels TENSION; f_sigma = 4 to 8 (corners added after the run, labelled as an extension) fits both moments. The note's own text is not uniform on how closely: its scope says within 1.6 sigma, while its results text gives worst pulls of at most 1.8 (f_sigma = 4) and 2.4 (f_sigma = 8); the cached output lists worst pulls of 1.6 to 1.8 at f_sigma = 4 and 1.5 to 2.4 at f_sigma = 8, depending on the multiplicity-factor and elasticity corner, with 1.5 at the best extended corner. The scope's 1.6 therefore holds for the better corners only. The exclusion therefore rests on the assumption that the flowed hadron interacts like a standard proton. Its air cross section is computed in no note of this theme. #10091's "about 100 g/cm^2 deeper... several times the hadronic-model spread" does not survive #10093's raw comparison. At lgE 19.74 standard protons sit 44 to 74 g/cm^2 above the data, the worst pull is 2.0 on <Xmax> and 4.9 on sigma(Xmax), and <Xmax> alone does not exclude protons. The breakup calculation of #10091 is not changed by #10093.

## 4. #10088 and #10089, superseded in part

**#10088** (superseded in part by #10089 and #10090). Stands only as conditional on the frozen, parton-additive hadron dispersion c_h = sum <x^3> c_i: the collinear golden-rule rates for p to p gamma (thresholds 3.24 to 4.44 EeV, energy-loss lengths 1 to 4e3 cm at 1.01 times threshold and about 1 cm at twice threshold, normalisation checked against Frank-Tamm to 1e-5), the later opening of p to p pi0 (6.7 to 21 EeV), and the coherent nuclear channel being negligible under a Gaussian charge form factor. The note's own caveat is part of the statement: a quark-level impulse accounting closes free-quark emission exactly, so whether protons radiate depends on how a composite's dispersion is assigned. Replaced: the wall at about A x 4 EeV per species and the incoherent-wall tables as predictions of the rules, and the claim that no proton above threshold reaches us from any source. With the full eigenstate emission is closed to 1e20 eV in #10089 (two-body models) and to 1e21 eV in #10090 (three-body), off the body-diagonal cones, and nuclei dissociate (entry 2).

**#10089** (superseded in part by #10090 and #10091). Stands in its supplied models: first-order additivity c_B = sum c_i <x_i^3> (Hellmann-Feynman, 1.000005 numerically, valid while lambda |c| is much less than M0^2); the Z^1 pair ratio of the P^4 to P^2 coefficients, -1/12 + t^2/(U^2 + 16 t^2) (0.250, 0.294, 0.625, 0.971, 1.000 times -1/12 at U/t = 0.05, 1, 4, 20, 200); the Z^3 contact-pair ratio 0.98 to 1.07 at U/U_c = 3 and 1.000 at 30 and 300 (U_c = 7.91); the two-body light-front flow (qq: 0.400 to 0.928 at 1e19 eV to 1.000, half-way near P_x of 5e18 eV); p to p gamma with the frozen additive wavefunction opening at 4.3 to 6.7 EeV and staying closed to 1e20 eV with the full eigenstate in its three models. Withdrawn or corrected: "nuclei inherit the same flow" and "incoherent walls also close" (contradicted by #10090 and #10091); the closure of emission on body rays (in the three-body model of #10090 the residual 1 - c_B/c_q, falling as u^(-1/2), opens p to p gamma at 5.3 to 6.0 EeV inside cones around the 8 body diagonals, 1.8 percent of the sky; in #10089 the two-body ratio tends to 1.000 exactly); and the title's statement that hadron emission is closed, which holds off those cones. These results, and the flow used by #10090, #10091 and #10093, assume |k_i| much less than E*, interactions smooth on the cell scale, no Lorentz violation in the exchange kernel (same order lambda; it could shift P_x), and that the fixed-P eigenstate is reached (formation length about 1e-4 cm, estimated and not computed dynamically). The half-way scale is P_x of about (M0^2 E*^2/2|c|)^(1/4). Its side consequences (GZK closed; the hadronic delta_had,2 at UHECR energies about 80 times above 1e-57 eV^-2 in magnitude) are estimates, not computed in an analysis that treats negative coefficients.

## 5. #10091's dimension-eight rescue, qualified by #10092

#10091 describes a minimal rescue in which the leading lattice correction vanishes at order p^4 for every species, for example by a symmetric two-rung composition of the tick, with the first surviving term of dimension eight (nuclear instability near 1e21 A eV). #10092 qualifies this: an exactly perfect tick is impossible on finite bands (T1); the improved range-2 ticks it works out have zero p^4 in the band, but the lattice-time (step) piece must also be cancelled and that is not built; the improvement coefficients c8 depend on the chosen improvement; and radiative dimension-six terms of one-loop size (5.8e-4 to 1.6e-3) would put 14N breakup at 48 to 84 EeV against the 5.5e-5 to 4.9e-4 needed to keep it above 100 EeV. Protection of those terms takes a dressed condition, which is not a result. Tree-level, free matter only.

## 6. Two scenarios not to be mixed: dimension six against dimension eight

#10090 states that photopion on the CMB is closed at all energies (no GZK horizon) and that gamma to pair opens at 8.0e16 eV. #10092 states that if the dimension-six term is cancelled and only dimension eight remains, photopion reopens, gamma to pair opens near 1.8e20 eV or not at all, and time of flight is unmeasurable. These are different scenarios of different supplied rules, not a contradiction; #10092 withdraws the no-GZK prediction for the cancelled scenario.

## 7. #10087 (logged): numbers conditional on frozen weights

#10087's thresholds (p to p gamma from 3.2 to 4.4 EeV, p to p pi0 from 7 to 21 EeV, nuclei near A times that threshold: He 13 to 17, N 45 to 59, Si 91 to 119, Fe 182 to 238 EeV) and its delta_had,2 values (-(0.34 to 4.3)e-57 eV^-2 sky-averaged) use parton weights frozen at the rest-frame moment (2 GeV or E*). Under the flow of #10089 and #10090 the hadron coefficient tends to c_q at UHECR energies (0.997 to 0.999 at 1e20 eV in the three-body model), so these thresholds and values do not stand as predictions of the rules; #10089 estimates the sky value at -7.9e-56 eV^-2 and says it must be rechecked. The exact parts stand: the convention map delta_had,2 = 2c/E*^2 (1.35e-54 c eV^-2), the sky averages (c_g = -1/40, c6 = -1/30, c_q = -7/120), and the sign (subluminal on every ray, outside the delta_had > 0 range that Auger scanned).

## 8. #9891 and #9888 (logged) against #10092 and #10090

#9891 reports that, in coarse-lattice units, the cubic anisotropy falls by a factor 4 per rung ("isotropy emerges"). #10092 (T2) states that zooming leaves the finest rung's physical Lorentz violation unchanged; the two are about different units and are not to be read as removal of the physical term. #9888 reports that with one shared time-step parameter photon decay into a fermion pair stays closed on its sampled grid; #10090 finds the opening at 8.0e16 eV for the physical electron mass with the dimension-six coefficients. The notes use different rules. In #9888 fermion and photon bands differ only by mass, so the margins stay positive on its finite grid. In #10090 c_q = c_g + c6 with the copy-mass shift c6 = -(1/8)(S - 1/3) (#10087), which makes the photon the faster particle and opens the decay everywhere except where c6 = 0, the body diagonals.

## 9. Two different groups of order 96

#9913's 96 is the number of linear maps preserving the 81-displacement step set and the edge cone (48 cubic rotations and reflections, each with or without time reversal). #10066's (logged) 96 is the order of the magnetic point group of node-faithful intertwiners of one family-class tick, half of 192. They are unrelated groups.

#10066's equal L and R speed is a free-band statement about states related by its group, in one tick's node space. It does not bear on c_e/c_gamma, but #9913's "two species" should be read as species that the tick symmetry does not exchange.

## Source notes carried with this consolidation

Each kept result's own note, runner and cache are carried byte-for-byte from its source PR.

- #9872: [MARGOLUS_SPIN_THREE_HALVES_EDGE_HOP_GIVES_A_CUBE_COVARIANT_DIRAC_TICK_BOUNDED_THEOREM_NOTE_2026-10-21.md](MARGOLUS_SPIN_THREE_HALVES_EDGE_HOP_GIVES_A_CUBE_COVARIANT_DIRAC_TICK_BOUNDED_THEOREM_NOTE_2026-10-21.md)
- #9913: [NO_TICK_SYMMETRY_FIXES_ONE_LOOP_ELECTRON_CONE_TO_PHOTON_CONE_BOUNDED_THEOREM_NOTE_2026-10-21.md](NO_TICK_SYMMETRY_FIXES_ONE_LOOP_ELECTRON_CONE_TO_PHOTON_CONE_BOUNDED_THEOREM_NOTE_2026-10-21.md)
- #10090: [RULE_FIXED_DIMENSION_SIX_LIV_SURVIVES_TIME_OF_FLIGHT_BY_SEVEN_ORDERS_AND_IS_TESTABLE_IN_UHECR_COMPOSITION_AND_PHOTON_CUTOFF_BOUNDED_THEOREM_NOTE_2026-10-26.md](RULE_FIXED_DIMENSION_SIX_LIV_SURVIVES_TIME_OF_FLIGHT_BY_SEVEN_ORDERS_AND_IS_TESTABLE_IN_UHECR_COMPOSITION_AND_PHOTON_CUTOFF_BOUNDED_THEOREM_NOTE_2026-10-26.md)
- #10091: [NUCLEAR_VACUUM_BREAKUP_UNDER_RULE_FIXED_DIMENSION_SIX_LIV_IS_A_HARD_WALL_BELOW_FIFTY_EEV_BOUNDED_THEOREM_NOTE_2026-10-26.md](NUCLEAR_VACUUM_BREAKUP_UNDER_RULE_FIXED_DIMENSION_SIX_LIV_IS_A_HARD_WALL_BELOW_FIFTY_EEV_BOUNDED_THEOREM_NOTE_2026-10-26.md)
- #10092: [ZOOM_FIXED_POINT_TICK_IS_EXACTLY_PERFECT_ONLY_AT_HISTORY_LEVEL_FINITE_BAND_TICKS_KEEP_LIV_BOUNDED_THEOREM_NOTE_2026-10-26.md](ZOOM_FIXED_POINT_TICK_IS_EXACTLY_PERFECT_ONLY_AT_HISTORY_LEVEL_FINITE_BAND_TICKS_KEEP_LIV_BOUNDED_THEOREM_NOTE_2026-10-26.md)
- #10093: [RAW_XMAX_SIGMA_ABOVE_46_EEV_PUTS_A_PURE_FLOWED_PROTON_BEAM_IN_TENSION_DECIDED_BY_THE_FLOWED_HADRON_AIR_CROSS_SECTION_BOUNDED_THEOREM_NOTE_2026-10-26.md](RAW_XMAX_SIGMA_ABOVE_46_EEV_PUTS_A_PURE_FLOWED_PROTON_BEAM_IN_TENSION_DECIDED_BY_THE_FLOWED_HADRON_AIR_CROSS_SECTION_BOUNDED_THEOREM_NOTE_2026-10-26.md)

## Other results

The scope text is copied verbatim from each source note. The full note, runner and cache stay on the listed branch at the listed commit.

| PR | Result | Disposition | Scope as stated in the source | Branch and commit |
|---|---|---|---|---|
| #9878 | A partition-link leapfrog matches the fermion band, and a symmetric source fixes a shared light cone | logged | For the supplied massless fermion tick and supplied link discretisations: a leapfrog with E on even-partition links and B on the dual odd-partition links at Courant number 1/sqrt(3) has exactly the fermion band at every sampled K, with static Gauss modes and a zone-corner Jordan block; link placements on the individual site hops or in continuous time match only at leading order; and a source is symmetric in g = diag(-alpha,1,1,1) only if alpha = d(w^2)/d(K^2), which is 1/3 for both the fermion and the partition links, giving c_grav = c_fermion at leading order. Comparisons with ultra-high-energy cosmic-ray, photon-decay and GW170817 bounds are estimates. No link law, placement, value of alpha or interacting light cone is established. | `claude/toe-light-cones-20261021` `e4a35f3dd32a` |
| #9888 | The staggered Margolus term is a universal time step | logged | For the supplied staggered Margolus tick with half-tick unitaries V(mu/2 +- b), the bands are cos w = A S - (cos2b - cos mu)/2 with c = cos(b)/sqrt3 as mu -> 0; the tick is exactly exp(+i(eps+mu/2)W_o) exp(-i(eps-mu/2)W_e) with eps = pi/2 - b, so b sets a time step and bandwidth; a supplied Yee link leapfrog matches the massless b-band at every K exactly when its Courant number is cos(b)/sqrt3, is a Jordan block at R when b = 0, and with one shared b keeps photon decay closed on the sampled grid while a per-species b opens it; a pi-cone particle-hole pair sits at -4b mod 2pi and two band-top pairs wrap the quasi-energy circle iff b <= pi/4; three structural clauses of the register follow as theorems. Rates and bounds from measured numbers are order-of-magnitude estimates. The value of eps, the vacuum filling and any adopted register text are not established. | `claude/toe-b-compaction-20261021` `f88efccf8e63` |
| #9891 | The Margolus tick at the next rung keeps its speed, its two copies and zero chirality | logged | For the supplied spin-3/2 Margolus tick read at rung 1 (4^3 cells of 64 one-mode sites, zoom x2 in space and time), the 64-band tick is exactly the fold of the 8 fine bands; the composite is not a two-partition Margolus circuit at rung 1 for any alignment; under the light-sector flow c is rung-invariant, the mass doubles and the cubic anisotropy falls by 4 per rung; under the stroboscopic zoom the pi-cone aliases onto the coarse zone centre; the rung-1 nodes carry zero Berry flux and every level stays fourfold, while the rung-0 cube cannot hold a single Dirac copy; a supplied covariant rung-1 block unitary with exactly one Dirac copy exists. Finite diagnostics of supplied models. The zoom convention, light projection and the rung-1 unitary are supplied; no rung-1 law, chirality, single-copy matter content or internal gauge group is established. | `claude/toe-rung-flow-20261021` `ef1848af523e` |
| #9916 | The vacuum-reference principle fixes the zero, the unit and the photon cone, but not fermion cones | logged | For the supplied free sea on static cells at second order, a supplied vacuum-reference principle (edges and links respond only to departures from the vacuum of the same edges with flat links, in the vacuum's units) removes every vacuum term from the edges, makes the subtracted link running cell-blind and puts the dressed photon cone on the edge cone at q -> 0; fixing the 4-volume per record removes none of the massless sea's shape dependence; no response law fixes charged-fermion cones; the principle is adopted, not derived. | `claude/toe-one-principle-20261021` `01548dcfa32f` |
| #10013 | Untuned all-direction massless crossings select space dimension = Bloch-ball dimension | logged | For translation-invariant local single-particle updates on Z^d with a finite cell and no imposed symmetry beyond translations, a two-fold level crossing has codimension beta+1 (2, 3, 5 for real, complex, quaternionic amplitudes), which is the Bloch-ball dimension of the corresponding two-level unit. Hence crossings that are (i) stable under every small local change of the update (no tuned parameter) and (ii) split linearly in every momentum direction (a cone: massless influence spreads in every direction) exist exactly when d = beta+1; for the complex qubit d = 3. At such a cone the linearisation J is invertible, its sign det J is the chirality (solid-angle degree +-1), the charges sum to zero (Nielsen-Ninomiya), and every Bloch rotation of the qubit is a momentum rotation for the emergent metric J^T J, so the identification of space rotations with qubit rotations is derived at low energy rather than supplied. Finite diagnostics on random nearest-neighbour two-level models confirm: gapped for d = 1, 2; isolated stable cones for d = 3; nodal lines with a flat direction for d = 4; point nodes at d = 2 for real amplitudes and d = 5 for quaternionic. The claim is free-particle level, assumes the stated two premises, and does not derive that untuned massless matter must exist; it also scores three other candidate selectors (minimal odd d with propagating response; Polya transience plus atomic stability; 2^d-cell Clifford counting). | `claude/toe-why-three-dims-20261021` `5e81aa3870c4` |
| #10066 | A family-class tick keeps a 96-element magnetic group that forbids every low-energy rotation- or Lorentz-violating dispersion term below dimension six, and leaves its time-reversal breaking in one chirality-flip term | logged | Free light bands of FREEZE (twist-local-single; W_F = (-2,1,1), the family-class tick of tick-winding-origin) on CL-1's 2x2x2 cell. (1) FREEZE's on-cell magnetic point group (node-faithful K-independent intertwiners among CL-1's 24 rotations x inversion x chiral x antiunitary) has order 96, half of CL-1's 192: an element is kept iff [R not tetrahedral] = inversion + chiral + antiunitary (mod 2). (2) On the 4-state node space (L q = 2 plus R q = 1) at K = 0 and at R the group allows 0 constant, 1 linear and 1 quadratic real coupling, each FREEZE's own: no b-type term, an isotropic cone with equal L and R speed 1/sqrt3, and one L-R term m(K) = (sqrt2/6)(Kx^2 + w Ky^2 + w^2 Kz^2). (3) m(K) is the only structure to order K^2 that is odd under C2', T and inversion. (4) FREEZE's light dispersion is exactly cos theta = mean cos K, so every level is 2-fold, even in K, with cubic anisotropy -(1/36)(Ka)^2; at order K^3 the group also allows a T-odd k_x k_y k_z term, which is 0 in FREEZE. (5) Each node keeps one protected L (q = 2). Not covered: interactions, gauge fields, the copy mass, K-dependent intertwiners, photon bands, which physical species these Weyls are. | `claude/toe-t-breaking-tick-lowenergy-20261021` `ecf617bb01a5` |
| #10087 | The rule-fixed dimension-six proton coefficient is subluminal and outside the Auger hadronic LIV sign range | logged | Conversion of CL-1's dimension-six dispersion (link band c_g = -S/24, copy-mass shift c6 = -(1/8)(S - 1/3), S = sum n_i^4; E = p + c p^3/E*^2, E* = hbar c/2L, L = sqrt(8 pi) l_P at kappa = 1) to the Auger convention E^2 - p^2 = m^2 + delta_{had,2} E^4: delta = 2c/E*^2. Sky averages exact (<S> = 3/5: c_g = -1/40, c6 = -1/30, c_q = -7/120). With supplied toy PDFs (2 GeV) and LO N = 4 evolution to E*, the parton weight sum <x^3> is 0.063 (2 GeV) or 0.0045 (E*), giving delta_had,2 = -(0.34 to 4.3)e-57 eV^-2 sky-averaged, -(0.08 to 1.2)e-57 on body diagonals, -(0.7 to 9.1)e-57 on axes: negative (subluminal) on every ray, outside the delta_had > 0 range of Auger 2022. In the pure-proton convention of Maccione et al. 2009, eta_p = -(0.013 to 1.35), beyond their -1e-3 grid edge. Parton-additive composites radiate hard photons (p -> p gamma from 3.2-4.4 EeV) and pions (7-21 EeV); kinematics only, no rates. Not covered: emission rates, nuclear structure beyond nucleon additivity, a fit of the UHECR data with this model. | `claude/toe-liv-auger-confrontation-20261021` `33381835d56b` |
| #10088 | Rule-fixed vacuum emission builds per-species walls at about A x 4 EeV, in tension with the highest UHECR events | corrected or replaced in part by #10089, #10090; see corrections | With the rule-fixed dimension-six dispersion (c_g = -S/24, c_q = -S/6 + 1/24, E* = hbar c/2L, L = sqrt(8 pi) l_P) and the supplied hadron-level parton additivity of agents/liv-auger-confrontation, the collinear golden-rule rate (normalisation checked against Frank-Tamm) for p -> p gamma, with the dipole form factor included, gives energy-loss lengths of 1-4e3 cm at 1.01 E_th and ~1 cm at 2 E_th. E_th = 3.24 (axis) to 4.44 EeV (body diagonal). Gamma_E ~ eps^1.2-1.5, so a 100 Mpc loss length sits within eps ~ 1e-19 of threshold: a sharp wall. p -> p pi0 (g^2/4pi = 13.7, axial dipole) opens later (6.7-21 EeV) and never sets the cutoff. For nuclei the coherent channel is kinematically open from ~sqrt(A) E_th but dead under a Gaussian charge form factor. The incoherent wall is A E_th/(1 + k_F/m) for a Fermi-gas core (Fe 144-188 EeV, N 36-47, He 10-13), and much lower (Fe 23-55 EeV) if the nucleon light-cone tail falls like e^{-s(alpha-1)}, s = 8-16.5 (supplied). Verdict: IN TENSION, not robustly excluded. Not covered: real nuclear large-momentum response, inelastic hadronic channels (they only shorten lengths), a spectrum/composition fit. | `claude/toe-uhecr-vacuum-emission-20261021` `faa58f83c432` |
| #10089 | A composite's dimension-six coefficient flows to its most subluminal constituent, closing hadron vacuum emission | corrected or replaced in part by #10090, #10091; see corrections | For bound states whose constituents carry the rule-fixed dimension-six dispersion (c_g = -S/24, c_q = -S/6 + 1/24, E* = 1.22e18 GeV): (i) [T] at first order in the lattice correction the composite coefficient is exactly parton-additive, c_B = sum_i c_i <x_i^3> (Hellmann-Feynman); (ii) [T] Z^1 cos-band pair with on-site attraction: P^4/P^2 ratio = -1/12 + t^2/(U^2 + 16 t^2), additive (x 1/4) for binding << bandwidth, universal for binding >> bandwidth; Z^3 contact pairs (U_c = 7.91 ~ bandwidth) are all lattice-sized and universal with the S pattern; (iii) [F] in a supplied boost-covariant light-front two-body model the LIV enters the mass operator as lambda sum c_i x_i^3, lambda = 2P^4/E*^2, and the ground state's effective coefficient rises monotonically from the additive value to min_i c_i = c_q, half-way at P_x ~ 5 EeV, the same scale as the additive emission threshold; (iv) [F] p -> p gamma (ground state -> ground state + link-band photon) opens at 4.3-6.7 EeV with the frozen additive wavefunction and stays CLOSED to 1e20 eV on axis, sky-average and body rays with the full eigenstate, in 3 models and a 4-point binding scan. Not covered: transverse dynamics, >2-body light-front states, LIV inside the interaction kernel, nuclei, relaxation dynamics. | `claude/toe-composite-dispersion-20261021` `3a4d3dc90f75` |
