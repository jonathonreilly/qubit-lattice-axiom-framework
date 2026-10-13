# What massless gravity costs, substrate by substrate

**Status.** DRAFT v5 (G-L referee verdict added at 03:19Z). v5 applies the referee's 8 corrections (`C3_P_referee.md`: APPROVE WITH CORRECTIONS on v4), adds the Lemma L referee verdict, and logs the G-L worker FAIL as pending its codex referee. Earlier history: v4 was for the lane-P referee (lane P of campaign C3, `TESTS.md:510-512`). Not landed. No axiom is changed or proposed here. v2 fixed the ten issues of the adversarial check (`C3_P_report.md:107-167`) and added the eight C3 verdicts refereed so far (`TESTS.md:567-575,601-605`). v3 adds four logged items that are **suggested / not refereed**: the M-D worker verdict and three wall exercises (`TESTS.md:607-635,650-658`). They are kept apart from the refereed record (§3b, §5b). v4 recorded the K, X1 and X2 referee verdicts. K, X1 and X2 are now refereed (`TESTS.md:660-664`); only G-L is still pending (§6).
**Inputs.** Refereed results from the gravity exercise packet and the candidate pack, at commit `e2d77f7f0e`, plus the not-refereed items above. v1's checker confirmed only that each quoted fragment is present at its cited line (250 checks, 0 failed). It does not show that a paraphrase is faithful (`C3_P_report.md:176`). Anything not refereed is marked "reading, not refereed" (lane P's own) or "suggested / not refereed" (same-family workers and exercises).
**Drafter.** v1 by Claude Opus 5.5 (max effort); adversarial check by Opus 5.5 (xhigh); v2–v5 by Claude Opus 5.5. The workers behind these results, including M-D and the three exercises, are of the same model family. Every referee cited is codex gpt-5.6-sol at xhigh, from another vendor.

**Where the files are.** Bare file names are unique.
- **Packet:** `.claude/science/exercises/gravity-current-state-20261009/`. The `*_referee.md` and `C3_*_report.md` files are in its `agents/` folder.
- **T1 and T2 referees:** `scripts/T1/referee/REFEREE_VERDICT.md` and `scripts/T2/referee/REFEREE_VERDICT.md` in the packet, cited as T1-REF and T2-REF.
- **Candidate pack:** `TEST_LOG.md` is in `.claude/science/candidates/candidate-law-20261008/`.
- **Axioms and registry:** `docs/MINIMAL_AXIOMS_2026-06-29.md`, `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`.
- `PRIMITIVE_REGISTRY_CHECK.md` exists in the repository; it was missing only from the lane-P referee's packet copy, so its line-specific claims below were not independently checked by that referee (related available source: `SCALE_REFERENCE_PRIMITIVE_NOTE.md:47-55`).

**Conventions.** CWC means CONFIRMED WITH CORRECTIONS, the referees' own phrase. Labels are as in the sources: EXACT, CHECKED, ARGUED, COMPARATOR. "Stiffness" means the vacuum's response to a volume-preserving shear (the TT channels). M_Pl is the non-reduced Planck mass and M̄_Pl the reduced one.

## 1. In plain words

**What gravity needs.** Gravitational waves travel at light speed and carry no mass.

**The fixed grid.**
- On the framework's fixed grid, the vacuum of the matter fields resists being sheared, as a crystal does.
- If a grid cell is about one Planck length, the computed shear response is near the Planck scale. It becomes a graviton mass only for an independent dynamical metric, after a stationary background (tadpole cancellation) and a kinetic normalization are supplied; for an emergent graviton it is only a naturalness diagnostic (`TEST_LOG.md:423-428,520-528`).
- One shared light speed is protected by symmetry, in the tested one-loop theory, when time is a grid direction with the same step as space. That is sufficient, not shown necessary (`TESTS.md:85`). For the framework's own model K7a found two conditions: at that tick A25's leapfrog is unstable, and 4D staggered fermions come in 4 tastes, unlike the 3D Hamiltonian (`TEST_LOG.md:32-33`). With continuous time and a smooth regulator, the speeds split by about 0.7·g²/16π², set by the regulator's shape (T1(a2), a refereed FAIL, `T1-REF:4,19`).
- **Keeping the grid with tuning.** The mass can be removed by hand-set counterterms in two shear numbers. What remains of each must be at most about one part in 10^101 of its natural size if a⁻¹ = M_Pl with the non-reduced Planck mass, which the adversarial check reads as the framework's convention (lane P's arithmetic: reading, not refereed). The refereed figure is 5.7e-99, which takes a cell as one reduced Planck length (`B_referee.md:35`). Lane K asked whether a speed tuning is also needed. Its referee: INCONCLUSIVE, and "two shear tunings alone are not established; additional speed-sector protection/tuning remains an open, generically expected cost" (`C3_K_referee.md`).
- **Keeping the grid without tuning.** Every tested regulator gave something up: a trilemma between positivity, one protected light speed and zero stiffness (`SUMMARY.md:55`, summary prose: reading, not refereed as a sentence; each leg below is refereed). These are free-field results, bounded to the families tested.
  - Positive kernels that treat time and space alike keep a stiffness that falls at most as a power of the kernel's width (T2, a bounded FAIL, `T2-REF:29`).
  - A smooth kernel with continuous time splits the light speeds (T1(a2)).
  - A smooth Gaussian kernel on Z³ suppresses the free stiffness, but its smooth-in-Euclidean-time version breaks reflection positivity, and truncating it costs about five million couplings per site (`kill_F2_referee.md:64`).
  - The one exact zero relabels momenta. It lies outside T2's rules, and Lemma R blocks it for ordinary local interacting laws that conserve momentum additively, not for all laws (`T2-REF:5,29`).

**Frozen patterns of points.** We tested these in place of the grid, and each tested model failed:
- the ones that keep some order (a diluted grid, a quasicrystal, an evenly spread random set) are stiff on average, and the quasicrystal is unstiff only at a hand-picked coupling range;
- the ones that are unstiff on average (a random scatter, fixed or growing) carry a random stiffness patch by patch (white noise in the models tested: strong evidence, not a bound).

**A flowing liquid of sites** (the tested three-spatial-label F(b) liquid) removes the stiffness exactly, for a supplied metric. In the equal-mass, common-regulator Yukawa model its rest frame gives different particles different speeds. In exactly flat space, with only a cosmological-constant counterterm, the leading description of that liquid loses its phonons' kinetic term. These are results for the tested model, not theorems about every microscopic liquid (`kill_F1b_referee.md:5,31-41,43-70,90-92`).

**Events scattered at random in spacetime, each influenced only along links (E1′).**
- **Its averages come out right.** Its law is shape-blind, and its mean scalar kernel tends to the massless retarded one, with O(ℓ²/r²) corrections and no Yukawa factor (`E1p_referee.md:41-43,51`).
- **A scalar stand-in** for a gravitational wave (the registered scalar proxy) crosses 1 Gpc with relative noise ≲ 3.7e-29. The Fano bound behind it holds for a bounded, uniformly regular source family that crosses the cone transversely, with bounded aspect ratios and cone-normal thickness ≫ ℓ²/D (`E1p_b_referee.md:138-163`).
- **The graviton tests of campaign C3** (§3):
  - the order itself as the graviton is a FAIL scoped to the fixed-coordinate coupling and ensemble-RMS noise, "not a gauge-invariant no-go for order-based gravitons";
  - a tensor carried on links has an rms non-TT admixture of about 7.3e-28 at 1 Gpc (a controlled asymptotic ceiling for the registered single-observer, ensemble-rms, trace-reversed potential-amplitude observable and the smooth conserved superpotential source; not a curvature-polarization result, not a bound in every realization, not for generic neutron-star stresses; `C3_G-B_referee_full.md:16-38,247-256,284-301`), but its mean equals linearized GR only in the infinite-density limit, so INCONCLUSIVE;
  - protection is INCONCLUSIVE.
- **Not smooth.** In one realization the order already responds to strain in jumps, not smoothly (`E1_referee.md:31`; `E1p_referee.md:187`). Open: whether that crackle is harmless at physical strain in a coupling other than the one G-A failed.
- **Not established** (`E1p_b_referee.md:163`): tensor propagation (since tested by G-B: INCONCLUSIVE), nonlinear gravity, the strain response and stable evolution from initial data. The source-driven link field does not provide evolution from initial data (`E1p_referee.md:184-189`). That the events have no dynamics of their own is summary prose (`SUMMARY.md:229-232`): reading, not refereed.
- **Matter on the events** (§3).
  - Massive scalar matter is M-INCONCLUSIVE. Within an unproved closure, and if its noise law applied to a composite's centre of mass with the total mass (a mapping not derived), it would be in tension with qBounce neutrons (42.5 ms), Rb-87 interferometry (2.3 s) and atom-interferometer coherence up to 70 s (`C3_M-A_referee.md:66-69,73-75`).
  - **Lane M-D tested that mapping** (worker verdict INCONCLUSIVE, supported with corrections by a same-family check; no codex referee, as none is required for a non-FAIL; suggested / not refereed; `TESTS.md:607-616`). A composite's growing noise follows its constituents, not its total mass: k0·m_i·m_j·ℓ per pair channel, never k0·M²·ℓ (EXACT within the pure shared-link sector, ARGUED beyond it). Under the uncontrolled M-A chain law the outcome then turns on what carries the mass vertices: nucleons or 313 MeV constituent quarks decohere Rb-87 in about 10–90 ms; current quarks and electrons with massless binding give about 440 s. Read the other way, the 70 s experiment needs every Johnston mass-vertex scale in an atom below about 12 MeV (`C3_M-D_report.md:5-22,301`).
  - No linear source-to-readout rule with only nonnegative weights has the exact massive retarded Klein–Gordon kernel as its mean (`C3_M-C_referee.md:65`).
  - A unitary link rule is open.
  - Spin-½: order alone supplies no frame or handedness, but two constructions give the massless Dirac response in mean, in the continuum regime (`C3_D_referee.md:48`).
- **Can records forming make the events?** Three tested classes of label-free growth cannot reproduce a 4D sprinkling (one of them only asymptotically). A general no-go is not established (`C3_F_referee.md:30-36`).
- **Its costs:**
  - the Lattice axiom;
  - unboundedly many links per event;
  - a time order that records do not supply;
  - a reading of Record in which an event is not a locked value;
  - for chiral matter, an orientation and spin-transport structure.

**What the three wall exercises suggest** (suggested / not refereed: same model family, no codex referee, and not used in any refereed claim above; §3b, §5b). Each exercise tried 9 routes past one wall of the event substrate, and all 9 were killed each time.
- **Formation.** Making the event set one record at a time seems to cost either a supplied event set, or a formation law for a whole region that knows its final size in advance. The one rule known to reproduce 4D statistics fails an open-ended test at 10–19 SE: its early stages are less ordered than small diamonds (`TESTS.md:618-625`).
- **The graviton.** A massless, smooth graviton on events seems to need three things together: a covariant growth law that produces Einstein histories (the formation wall again); amplitudes not weighted by e^{iS} of interval-count actions; and link readouts that reproduce Van Vleck focusing on curved backgrounds. Lane G-L tested the last: refereed FAIL (codex sol, CWC; `C3_G-L_referee.md`): for the unweighted one-hop link mean on curved backgrounds, not extending automatically to G-B, E1′ or weighted/multi-hop readouts: link/GR = (ν·Δ)^{−1/2}, density-independent; the link mean de-magnifies where GR magnifies (`.claude/science/exercises/gravity-current-state-20261009/agents/C3_G-L_report.md`). Not refereed (`TESTS.md:627-648`).
- **Massive matter.** Single-event mass steps add noise that grows exponentially (Lemma L, refereed CONFIRMED WITH CORRECTIONS: an exact positive ladder for deterministic, strictly causal kernels; the exponential needs Lorentz invariance, nonzero normalization and nonzero ends; it does not validate the S0 prefactor; `C3_LemmaL_referee.md`). The escape on offer costs a non-locality scale plus a signed hop whose moments cancel. The pre-registered test (S0) FAILED; a post hoc profile (Z2) clears every bar, a lead only (`TESTS.md:650-658`).

**No tested substrate produces the graviton itself** (reading, not refereed; `SUMMARY.md:59` marks it "(reading, as on 09-29)"). G-B carries a supplied tensor on links; it does not produce or protect one (`TESTS.md:471`).

## 2. One row per substrate

| Substrate | Averages | Noise per realization | One cone | Graviton | Matter | Status (referee) | Price |
|---|---|---|---|---|---|---|---|
| **Fixed grid, untuned** (Z³ or Z⁴; rigid or dynamical lengths) | **Stiff.** Free fields: a cutoff fixed by grid labels gives K₀⁴/(120π²) per boson and −K₀⁴/(60π²) per Weyl sea, and a cutoff that moves with the geometry gives 0 (T0, EXACT, `TESTS.md:14`; reading, not refereed, except that the W1 referee confirmed the Weyl value, `TEST_LOG.md:514`). Interacting, at O(e²): c₂ per e² per cell is −0.0130 on an axis and +0.0125 on a face, about 1.2e-3 per cell at α = 1/137 (K3a″, `TEST_LOG.md:387-393,414`). Dynamical lengths: about 1.3e-3, and twice that after the referee's normalization correction (W1, `TEST_LOG.md:488,518`) | None, since there is one crystal. Its anisotropy is coherent, not random (`B_referee.md:178`) | **Protected when time is on the lattice.** In units of g²/16π²: on Z⁴ (a_t = a_s) the split is −2e-9, which is roundoff, and zero by symmetry; on Z³ with continuous time, the nearest-neighbour split is −2.50 ± 0.03, which is order one (T1 controls, `TESTS.md:59-60,82`). A smooth spatial regulator with continuous time splits them by about −0.696, set by the regulator's shape (T1(a2) FAIL, CWC, `T1-REF:4,19,27`). Z⁴ symmetry is sufficient; it is not shown to be necessary (`TESTS.md:85`). **K7a's conditions:** hypercubic means a_t = 2 fine edges, where A25's leapfrog is unstable (max\|eig\| 9.9), and the stable τ = a_s/2 is not hypercubic; 4D staggered fermions have 4 tastes, unlike the 3D H_ψ (`TEST_LOG.md:32-33`) | **Supplied only.** For K7a's staggered h on Z⁴, gauge invariance leaves 1 of 9 forms (EXACT count). That protects one TT speed only if the interacting stress is exactly conserved (`TEST_LOG.md:28,45,51`). K3a, which asks that question, is INCONCLUSIVE: in the tested bounded class at O(e), no momentum is conserved (`TEST_LOG.md:240,259`). None is produced (reading, not refereed; `SUMMARY.md:59`) | Ordinary lattice matter. One cone holds on Z⁴ by the same symmetry (`TESTS.md:60`) | **Naturalness kill** (K3a″ CWC, `TEST_LOG.md:409-411`; W1 CWC, `TEST_LOG.md:507`). It is a graviton mass only for an independent dynamical metric; for an emergent graviton it is "a naturalness diagnostic only" (`TEST_LOG.md:425,428`) | A shear response near the cutoff, unless tuned (next row). A graviton mass only for an independent dynamical metric with a supplied stationary background (tadpole cancellation) and kinetic normalization; for an emergent graviton a naturalness diagnostic only (`TEST_LOG.md:423-428,520-528`) |
| **Fixed grid, tuned** | **Zero, by tuning.** Two bare O(e²h²) contact terms, one for each TT channel (E_g and T_2g), which cubic symmetry allows separately (`TEST_LOG.md:422`). Cubic O allows 2 TT mass numbers (`B_referee.md:23`) | None | As above. **Lane K (refereed: INCONCLUSIVE; `C3_K_referee.md`):** "Two shear tunings alone are not established; additional speed-sector protection/tuning remains an open, generically expected cost." The registered setting was not computed; K-num stands only as a bounded side result for a substitute model | Supplied, not produced | As above | "An owner decision, not a calculation" (`SUMMARY.md:66`; summary prose: reading, not refereed). **Grid regulators without tuning:** T2 is a bounded FAIL, CWC. The best confirmed family with a positive one-step transfer reaches 6.45e-4 at width 10, with a σ⁻² floor; it is "not a theorem that RP plus hypercubic symmetry forces such a floor" (`T2-REF:23-29`). T2's exact zero, a relabelling of momenta, is outside the test's rules; Lemma R blocks it for ordinary local interactions that conserve momentum additively (`T2-REF:5,21`). **The trilemma** (summary prose: reading, not refereed as a sentence; its legs T1(a2), T2 and F2 are refereed): "Every tested way to protect it loses one of the other three" (`ROUTES.md:54`), at the free-field level for smooth kernels (`SUMMARY.md:55`) | **Two tunings.** For the graviton-mass bound m_g ≤ 1.27e-23 eV, what remains of each shear number after its counterterm must be at most μ = 2.39e8 eV⁴ ≈ (124 eV)⁴ = 1.08e-104 M_Pl⁴. That is 5.7e-99 of K3a″'s natural size, 1.2e-3·M̄_Pl⁴ (B1 c1, CWC, `B_referee.md:26-35`); 9.0e-102 of 1.2e-3·M_Pl⁴ (lane P arithmetic: reading, not refereed). "TT twin of the cosmological-constant problem" is "a naturalness analogy, not a theorem" (`TEST_LOG.md:530`) |
| **Frozen point sets in space** (random, diluted grid, quasicrystal, hyperuniform, growing random) | **Random scatter:** 0, by the law's SL(3) symmetry, for the ensemble average only (`kill_F1a_referee.md:58`). **Diluted Z³:** never zero in both channels at once at any p tested; the nn T_2g mean is negative for every p > 0 (`E23_referee.md:29,33`). **Icosahedral:** equal in all five TT directions, and zero only at a chosen coupling range (`E23_referee.md:62-69`). **Stealthy hyperuniform:** +0.024 at m² = 1 (`E23_referee.md:79`). **Growing random:** 0 (`TESTS.md:247`) | **Extensive (white) fluctuations,** S(0) > 0, in the random and diluted models tested. This is strong evidence, not a bound (`E23_referee.md:37`). Frozen Poisson graph: σ√N ≈ 0.064–0.084 (`kill_F1a_referee.md:8`). Diluted grid: white at p = 0.1, 0.3116 and 0.5, with no sign of suppression at other p (`E23_referee.md:35`). Hyperuniform: noise exponents −0.405 ± 0.077 and −0.504 ± 0.077, where white is −0.5 (`E23_referee.md:80-84`). Growing random: white at every stage (`TESTS.md:247`; `E23_referee.md:120`). Quasicrystal: S(0) = 0 for the full functional is not established (`E23_referee.md:71`). In 3D a white random mass reaches order one relative to k² beyond about 25–35 cells (`kill_F1a_referee.md:23`) | **Poisson–Delaunay:** at tree level the speed is exactly 1 in each realization as p → 0, for the scalar and for Wilson–Dirac (`kill_F1a_referee.md:54`; `T1-REF:33`; `TESTS.md:70`); one loop was not computed, so T1(b) is INCONCLUSIVE (`TESTS.md:83`). **Other sets:** not tested | None | Poisson–Delaunay at tree level only; the others were not tested | F1a: kill CWC, "not a viable separate solution" (`kill_F1a_referee.md:3,58`). E2: FAIL (bounded), CWC. E3: FAIL for all three, CWC (`E23_referee.md:7-8`). This is not a theorem that every frozen substrate fails (`E23_referee.md:120-122`) | A new mechanism: an identity that holds in each realization (a coboundary or conservation law for the stress), another structural cancellation, or a quenched or non-ergodic mechanism. None has been exhibited (`kill_F1a_referee.md:58`; `E23_referee.md:122`). Plus the Lattice change |
| **Flowing liquid** (mobile sites; the tested three-spatial-label F(b) liquid, not every microscopic liquid) | **Exactly 0** for a supplied metric (`kill_F1b_referee.md:5,92`) | None for the stiffness | **Lost in the tested model.** In the equal-mass Yukawa model with a common regulator, the rest frame gives δc_φ − δc_ψ = (2/3)Ξ·g²/16π², with Ξ ≥ 1 for every smooth cutoff shape. That is at least 3.872e-4 at g² = 4π/137; this floor belongs to that equal-mass, common-regulator model (`kill_F1b_referee.md:45-70`) | None. The displacement is a vector, of helicity 0 and ±1 (`kill_F1b_referee.md:74`) | Particle speeds split (see One cone) | **"Dead as a complete untuned escape,"** CWC (`kill_F1b_referee.md:3,92`) | **Flat space.** For the tested F(b) liquid, with only a cosmological-constant counterterm, an exactly flat background forces ρ + p = 0. That removes the phonon kinetic term of its leading description, unless another sector cancels it by tuning or symmetry (`kill_F1b_referee.md:19,39`). **The speed split** must be tuned or protected; experiment excludes it by many orders (`kill_F1b_referee.md:70`). **Positions.** Literal continuous positions exceed a finite qubit (`kill_F1b_referee.md:80-82`), so Lattice and Qubit both change |
| **Spacetime events, BD dynamics** (E1) | **Exact.** Under a constant volume-preserving strain, the whole distribution of every covariantly defined order observable is unchanged. There is one real massless cone in mean (`E1_referee.md:30-34`). The 4D mean operator also has complex zeros, so "one cone" does not mean "one mode" or "stable" (`E1_referee.md:34`) | **The order "crackles":** it is piecewise constant in strain, with rms ∝ s^0.507 (a five-point fit). The row noise gain is infinite for an infinite past (EXACT, as an L² statement). Its coefficient is A² → 1.674·ε(T/ℓ_k)² for a diamond-shaped past and 4× that for a slab. The naive evolution is exponentially unstable at ε = 0.2, at rate 0.645 (`E1_referee.md:5,17-21,31,40,52-53`) | In mean (exact) | None (scalar proxy). The order's own BD action as the graviton: G-A FAIL, scoped to the fixed-coordinate coupling and ensemble-RMS noise (§3) | Not tested | **"INCONCLUSIVE — leaning FAIL"** (`E1_referee.md:9,11,56`). The exclusion would need the instability exponent extrapolated to ε ≈ 7e-64 | Lattice replaced; the causal order is supplied; conflicts with Record (`TESTS.md:273`; `SUMMARY.md:218-222`) |
| **Spacetime events, influence along links only** (E1′, E1′-b, and the C3 lanes) | Shape-blind in law. That is invariance of the ensemble law, not a smooth response in one realization (`E1p_referee.md:51`). E[aL] tends to the massless retarded light-cone kernel, with O(ℓ²/r²) corrections and no Yukawa factor (`E1p_referee.md:41-43,51`) | **Bounded.** Var ≤ (3 + C′_S·s/D)·N̄, uniformly in s/ℓ and ρ, for a bounded, uniformly regular source family that crosses the cone transversely, with bounded aspect ratios, cone-normal thickness ≫ ℓ²/D, and D ≫ s ≫ ℓ. For the registered scalar proxy of a neutron-star merger at 1 Gpc, N̄ = 2.2e57 and the relative noise is ≲ 3.7e-29. For the direct massless field, nothing outside the source-to-observer intervals enters (`E1p_b_referee.md:138-163`; `E1p_referee.md:69-73`) | **In mean.** At 1 Gpc the scalar kernel's mean arrival offset is 2.2e-104 s, with spread 1.66e-104 s. That is not yet a gravitational-wave arrival spread (`E1p_referee.md:179`; `SUMMARY.md:200`) | **Scalar proxy:** PASS in its registered scope. **Tensor on links (G-B):** rms non-TT admixture 7.27e-28 at 1 Gpc, an asymptotic ceiling, but the mean is not exactly linearized GR at finite density: INCONCLUSIVE. **Protection (G-C):** INCONCLUSIVE (§3) | **Scalar (M-A):** M-INCONCLUSIVE. **Unitary on links (M-B):** INCONCLUSIVE. **Nonnegative weights (M-C):** a linear rule with only nonnegative weights cannot give the exact massive mean (CWC). **Spin-½ (D):** INCONCLUSIVE; massless Dirac response in mean (§3) | **E1′ gravity "PASS, strictly for the pre-registered scalar, source-driven" proxy**, after E1′-b (CWC) (`E1p_b_referee.md:5-6`). C3 verdicts in §3 | As for BD dynamics, plus unbounded valency: about 5.0e122 past links per event over c·t₀ (`E1p_referee.md:180,189`). **Formation (F):** bounded FAIL for three classes of growth rule, so the order stays supplied for now (`C3_F_referee.md:5,30-36`). **Chiral matter:** an orientation and spin-transport structure (`C3_D_referee.md:50`) |

**Notes on the table.**
- **How to read a FAIL.** The referee's general caution: the fixed readings are sound only as bounded-model verdicts, and a failed kernel or scalar model excludes that implementation, not a whole substrate class (`B_referee.md:205`).
- **Records as the carrier, on the fixed grid** (FR1 and FR3, both CWC). In the tested models, freezing records does not supply a mediator, an additive source charge or a universal clock coupling (`TEST_LOG.md:590,606-611`). The three moving-record models give no tensor waves (`TEST_LOG.md:631,643-647`). Both are model-specific exclusions, not no-gos (`TEST_LOG.md:613,643`). **Lane X2** (refereed: CONFIRMED WITH CORRECTIONS, bounded FAIL; `C3_X2_referee.md:3-5,9-20,30-32`) tested the FR3 gases as the stress carrier: at k = 0, on finite tori and for the tested stresses, they have a metric-independent stationary law (G_T ≡ 0) but white stress noise (n_S = 0). This is a bounded model failure, not a no-go for all classical gases or record substrates.
- **A 4D Euclidean random lattice** (B1 c5). Its graph has finite random degree almost surely, not a uniform valency bound, and its kernel is O(4)-symmetric, not Lorentzian (`B_referee.md:75-76`). It is therefore not the Lorentzian setting of BHS. Its mean is about zero. A total-box stiffness estimator, not a direct k → 0 spectrum (`B_referee.md:74`), gives sd√N ≈ 0.05–0.08 over N = 255–4087. This is a bounded FAIL for one kernel and a free scalar, not a class-wide exclusion (`B_referee.md:67-80`). **Lane X1** (refereed: bounded FAIL, CWC; `C3_X1_referee.md`) extends it with direct nonzero-q spectra: flat, S ≥ 2.07e-3, for two kernels and for scalar and fermion functionals.
- **Smooth kernels on Z³ (F2).** The kill was NOT CONFIRMED as universal (`kill_F2_referee.md:3,64`), and T2 closed only the families it tested. The route is "blocked-local", not dead (`APPROACH_REGISTRY.md:9`).
- **The event rows hold refereed entries only.** The M-D verdict and the three wall-exercise prices (formation, graviton, massive matter) are suggested / not refereed and sit in §3b and §5b (P7–P9), not in this table.
- **Paying in vacuum energy on the grid (F3).** Supersymmetry, self-tuning and frustration-free vacua were judged dead at step 4 with no referee (`ROUTES.md:18,39`). Reading, not refereed; not used above.
- **The tuning's denominator.** The refereed 5.7e-99 reads K3a″'s per-cell value in units of M̄_Pl⁴, i.e. one cell = 1/M̄_Pl (`B_referee.md:35`). The registered primitive sets a⁻¹ = M_Pl (`SCALE_REFERENCE_PRIMITIVE_NOTE.md:17`), with a/l_P = 1 left open (`SCALE_REFERENCE_PRIMITIVE_NOTE.md:39-41`). The adversarial check found the repo's docs using the non-reduced 1.22e19 GeV, in 27 lines, and none using 2.435e18 GeV (`C3_P_report.md:159,198`). In that convention μ is 9.0e-102 of 1.2e-3·M_Pl⁴, near K3a″'s own "about 1e-100" (`TEST_LOG.md:409`). The 9.0e-102 is lane P's arithmetic (reading, not refereed). a = l_P is not derived (`PRIMITIVE_REGISTRY_CHECK.md:50-52`).

## 3. Campaign C3: the graviton and matter on the events

All C3 lanes use test settings only, and the E1/E1′ axiom conflicts apply (`TESTS.md:441-445`). Verdicts are quoted as the referees gave them; the packet's own record is at `TESTS.md:567-575,601-605`.

| Lane | Question | Referee verdict, as given | Established | Not established | Where |
|---|---|---|---|---|---|
| G-A | The order itself as the graviton, with points fixed in coordinates (picture I) | "FAIL, narrowly scoped to the fixed-coordinate coupling and ensemble-RMS noise specified by G‑A" | The second-chaos bound and the Rosen causal-order formula check out. The local BD action alone triggers FAIL. The smeared BD action FAILs up to ℓ_k ≈ 3.15e-19 m, then is INCONCLUSIVE | "Variance does not establish typical-realization behavior." The pure-gauge crackle is an artefact of the coupling: co-moving points and window give ΔS ≡ 0. "This is not a gauge-invariant no-go for order-based gravitons" | `C3_G-A_referee.md:5-14` |
| G-B | A tensor h_μν carried along links from a conserved source | "INCONCLUSIVE under the fixed reading" | Exactly conserved mean. Controlled rms non-TT admixture A_rms = 7.27e-28 at 1 Gpc, an asymptotic ceiling far below 1e-3, scoped to the registered single-observer, ensemble-rms, trace-reversed potential-amplitude observable for the smooth conserved superpotential source | The mean is K̄_ρ∗T, which equals G_R∗T only as density goes to infinity, so the "exactly" clause fails. Also not established: a curvature-polarization observable, a bound in every realization, generic neutron-star stresses, initial-value propagation, protection, nonlinear gravity, the strain response | `C3_G-B_referee.md:3-9`; `C3_G-B_referee_full.md:16-38,247-256,284-301` |
| G-C | An exact per-realization identity, or a quantum sum, that forbids a TT mass | "INCONCLUSIVE under the single fixed G‑C reading" | A narrow no-go "only for frozen picture-I, fixed-point, point-marked order functionals with uniform per-realization invariance and an EH ensemble mean". The law-level Ward identity is exact | Independent link fields, picture II, alternative couplings, a background-free quantum sum. The Ward identity "does not establish the physical quantum-sum branch" | `C3_G-C_referee.md:3-5` |
| M-A | Massive scalar packet to detector (Johnston's path sum) | "CONFIRMED WITH CORRECTIONS"; "Correct M-reading: M-INCONCLUSIVE" | The add-one identity and the Poisson chaos and Poincaré inequalities are exact. The pure shared-link subkernel has exponent k₀m²ℓ, k₀ = 0.25490 | The full variance exponent (E₂, signed cross terms, end factors). Within that unproved closure: R = 1 by 1 km below about 0.31–0.39 MeV/c for protons, and tension with qBounce (42.5 ms), Rb-87 interferometry (2.3 s) and atom-interferometer coherence up to 70 s if applied to a composite's centre of mass, "but that mapping has not been derived" | `C3_M-A_referee.md:3-5,18-19,55-61,66-69,73-75` |
| M-B | A norm-preserving matter rule on links | "CONFIRMED WITH CORRECTIONS"; the lane is "correctly **INCONCLUSIVE**" | No jointly Poincaré-equivariant isometry with finite-dimensional event fibers and a positive event-local norm moves a basis state to another event. The sprinkling cannot intrinsically select a nonempty antichain. The greedy nearest-continuation chain alone reaches γ ≥ 2 in median 9.75 ℓ_P | Dynamics on supplied slices, and states on links (arcs). An arc unitary, a massive one-cone mean and 1 km coherence are all open | `C3_M-B_referee.md:3-5,21,29` |
| M-C | Massive matter from nonnegative weights | "CONFIRMED WITH CORRECTIONS"; the decision table "formally returns **FAIL**" | No linear source-to-readout rule with only nonnegative weights has the exact massive retarded KG Green function as its ensemble mean, in any dimension (zero-mode proof, sin(mt)/m) | "a taxonomy-driven FAIL, not a theorem that C1 cannot have a massive mean". Not excluded: positive massive transport, a massive pole with a positive carrier, nonlinear observables | `C3_M-C_referee.md:3-5,17-22,61,65` |
| D | Spin-½ matter on links | "NOT CONFIRMED"; "Corrected lane verdict: INCONCLUSIVE" | Order alone gives no per-event spinor or frame mark, no handedness, and no γ·Δ mean of a fixed-fiber kernel. Scalar link propagation plus apparatus differentiation, and the order-only Kähler–Dirac cochain dG, give the massless Dirac response in mean, in the continuum regime | Controlled massive coherence. Genuinely chiral matter needs an orientation or chiral selector and a spin (Clifford) transport structure | `C3_D_referee.md:3,7,48-50` |
| F | Can label-free growth produce the event set? | "CONFIRMED WITH CORRECTIONS"; "a **bounded FAIL**, not a universal no-go" | Three classes cannot reproduce 4D sprinkling: exchangeable generating-subset growth (the tested link means), frontier-only growth (L ≤ N − 1), and every classical DGC+Bell dynamics, VR towers included (asymptotically: 2+2 and 3+1 densities vanish) | "records forming cannot produce the event set" is not established. A surviving rule must use the order nonexchangeably, or leave the Markovian, classical or Bell-causal scope | `C3_F_referee.md:3,5,30-36` |

### 3b. Not refereed: the M-D worker verdict and three wall exercises (suggested / not refereed)

Same model family throughout; no codex referee has seen any of these. Nothing in this subsection supports a refereed claim elsewhere in the note. Lemma S, T-F1 and N1 are proved or checked only by the same family. Lemma L is the exception: its codex referee returned CONFIRMED WITH CORRECTIONS (scope in the exercise M row).

| Item | Verdict as logged | Suggested result | Scope and caveats | Where |
|---|---|---|---|---|
| M-D (composite centre-of-mass coherence) | INCONCLUSIVE "(worker; the adversarial check supports it with corrections)" | In the pure shared-link sector the exponential noise is per constituent, rate k0·m_i·m_j·ℓ per pair channel, at most k0·ℓ·Σm_i², never k0·M²·ℓ (EXACT in that sector, ARGUED beyond). First chaos follows total mass and is negligible (about 1e-79). Under the M-A chain law: nucleons or 313 MeV constituent quarks give Rb-87 about 10–90 ms (conflict); current quarks and electrons with massless binding give about 440 s (pass). The 70 s bar needs every Johnston mass-vertex scale below about 12 MeV | The chain exponent is uncontrolled; the substrate does not fix what carries hadron mass; binding-vertex channels in 4D were not computed. Checker corrections: the 1+1 toy exceeds the composite law by a factor of 1.1–1.6 that grows with time, so channel additivity is not checked; the 1+1 visibility check is circular; cross-species non-growth is ARGUED in 4D, not CHECKED. The total-mass mapping is "not produced by the shared-link sector", not "removed" | `TESTS.md:607-616`; `C3_M-D_report.md:5-22,301` |
| Exercise F_formation (records cannot grow the event set) | "all 9 routes killed" | Herm(2)/Löwner order needs one global identification of every record's algebra, a supplied flat arena; local bulk nucleation clusters (Fano64 6.6 → 34.6, N = 500 → 2000); real-weight action sums meet an entropy bound; Lorentzian sums have no coupling window; BD-tilted growth meets the kill reading in 74/75 settings. Test T-F1 (pre-registered, run): Lemma G's rule, the only known one that reproduces 4D statistics, is TELEOLOGICAL at 10–19 SE | Only diamond regions tested; an asymptotically diamond-like rule and non-label-invariant rules (e.g. growth in advanced time along an axis, which needs a frame) escape. Lemma S (elementary sketch): one-at-a-time growth of an infinite set with a non-compact invariance group is impossible, so it needs a preferred frame or centre, or a compact section. T-F1 and Lemma S are no-go-type and need the codex referee | `TESTS.md:618-625`; `C3_exercise_F_formation.md:172-176,255-276` |
| Exercise G_graviton_on_events | "all 9 routes killed" | Route 1: G-A's FAIL ratio holds with no wave present (sampling noise of the flat BD action), so masslessness needs a covariant growth law with Einstein histories. Route 2 (coherent sum over orders): dead under the exact interval volume. Route 3 (spin-ice / Cayley–Menger): blocked-equivalent to K3a/F6. N1 (pre-registered, run): the needle volume in the Rosen wave tends to ρ·I0(h); "kill collapses" and "kill as computed" both excluded; corrected coefficient about 2× smaller | N1's "coefficient corrected" clause is met at kU = 100 but not at kU = 30, so strictly INCONCLUSIVE on its own wording; third-point cross terms not covered. Link-only readout on curved backgrounds may mis-lens (ν^{−1/2}·Δ⁻¹ against GR's Δ^{−1/2}; suggested, not computed): lane G-L, refereed FAIL (codex sol, CWC; `C3_G-L_referee.md`): for the unweighted one-hop link mean on curved backgrounds, not extending automatically to G-B, E1′ or weighted/multi-hop readouts: link/GR = (ν·Δ)^{−1/2}, density-independent; the link mean de-magnifies where GR magnifies (`.claude/science/exercises/gravity-current-state-20261009/agents/C3_G-L_report.md`) | `TESTS.md:627-648`; `C3_exercise_G_graviton.md:217-253` |
| Exercise M_massive_matter | "all 9 routes killed as written" | Dead: positive smeared hops (mean grows by e^(1.7e4) for Rb at 2.3 s), SJ/Wightman readout, extinction scoring. Wounded: soft-binding compositeness (misses Rb at 2.3 s by 15–25×; passes only with ≥ 15–81 soft re-emitters per nucleon) and a coherent quantum substrate (open research). Lemma L: for hop weights depending only on the two events, the variance is exactly a sum of positive ladders, so it grows exponentially, at rate κ_F. Lemma L referee: CONFIRMED WITH CORRECTIONS (`C3_LemmaL_referee.md`). Scope: an exact positive ladder for deterministic, strictly causal kernels; the exponential growth needs in addition Lorentz invariance, a nonzero light-cone normalization and nonzero ends; it does not validate the S0 prefactor, so S0 stays a conditional FAIL. S0 (pre-registered, signed hop with first moment zero): **FAIL**, an empty ℓ_k window at the 25 kDa molecule bar | Post hoc, not pre-registered, a lead only: Z2 profiles (first two moments zero) clear every bar at ℓ_k ≈ 1e-28 to 1e-25 m, conditional on κ_F (Lemma L itself is refereed, but not the M-A packet prefactor it would need), M-A's prefactor form, and bar figures partly from memory; particles treated as elementary scalars | `TESTS.md:650-658`; `C3_exercise_M_massive_matter.md:144-149,167-184` |

## 4. What is proved, and what is only a naturalness argument

**Proved under stated hypotheses** (the referee's list, `B_referee.md:147-154`).
- **The gauge identity forbids an h-only mass; symmetry does not.** A linearized gauge (Ward) identity imposed for every momentum forbids every local, momentum-independent mass term built from h alone. Point-group and Lorentz symmetry do not forbid it, because invariants such as tr h² survive (`B_referee.md:20-22`).
  - **The counts of free mass numbers:** 2 in TT for cubic O, 1 for icosahedral, 3 for W(B4) (`B_referee.md:23`).
  - **"Only a gauge redundancy forbids it" is too strong.** Shift symmetries, Stückelberg fields, custodial identities, topological constraints and non-local mechanisms lie outside the calculation. A Stückelberg theory can be gauge-invariant and still massive (`B_referee.md:24`).
- **Poisson randomness is shape-blind in law.** A Poisson process is invariant in law under every measurable volume-preserving bijection. This holds for the point process only, not automatically for a metric, order or dynamics built on it (`B_referee.md:94`).
- **Lemma Q, corrected.** No locally finite set of two or more points is invariant under full translations, full SL(d) or the full Lorentz group. It does not exclude internal or gauge symmetries acting on fields over a fixed point set (`B_referee.md:126-132`).
- **BHS.** No Lorentz-equivariant, intrinsic, finite-valency neighbour map exists on a Poisson sprinkling. That is all it shows. It does not show that the grain must have unbounded valency (`B_referee.md:52,209`).
- **The classic theorems,** each only with its listed assumptions: Weinberg–Witten, the soft theorem, and the spin-2 bootstrap (`B_referee.md:47-50`).

**Other refereed results used above.**
- **Lemma R, narrowed.** On a fixed grid, a continuous shear relabelling cannot be extended to an ordinary local interacting law that conserves momentum additively. Only GL(3,Z) points are reachable. Not every conceivable interacting law is excluded (`T2-REF:21`).
- **Lemma P, corrected.** Take a stationary simple point process in d ≥ 2, with finite local second moments. If SL(d) or AN symmetry of its law protects the mean, its ensemble density cannot be hyperuniform. "Density noise ⇒ stiffness noise" was withdrawn as too strong (`E23_referee.md:90-112`).
- **The fluid lemma.** A covariant liquid removes the TT mass for a supplied metric (`kill_F1b_referee.md:92`).
- **Lemma N.** The bound is confirmed and its equality case corrected (`kill_F2_referee.md:28-52`). Its step "face floor ⇒ stiffness floor" was an open lemma; T2 disproved it as stated, with a relabelling that lies outside the test's rules (`TESTS.md:120-126`; `T2-REF:5,29`).
- **The event substrate.** E1: shape-blindness in law, and the divergence of the L² row gain (`E1_referee.md:30-31,52-53`). E1′-b: the Fano bound (`E1p_b_referee.md:140-154`). C3: the exact pieces in §3.
- **Symmetry that treats time and space alike.** T1: Z⁴ symmetry suffices for one cone in the tested one-loop theory (`TESTS.md:85`). K7a: hypercubic covariance and the 9/4/1 count are exact (`TEST_LOG.md:39-45`).

**Supported by naturalness, not logically forced** (`B_referee.md:156-163`).
1. Generic fixed physical labels give a dangerous shear response.
2. Microscopic time and space must be exactly alike.
3. Gauge invariance must hold in each realization, not only statistically.
4. "Gauge or coherent" exhausts the mechanisms that keep the noise quiet.
5. Records can help only as spacetime events.
6. S1–S5 and B1's G+C are each necessary for every UV completion.

**Related qualifiers.**
- K3a″ is a naturalness kill (`TEST_LOG.md:409,428`).
- Collins et al. is a radiative-naturalness argument, not a no-go (`B_referee.md:51`).
- The F1a cutoff-window contradiction is conditional (`kill_F1a_referee.md:48`).
- ρ + p ∼ M_P⁴ is dimensional naturalness only (`kill_F1b_referee.md:41`).
- "Noise only through operators of dimension ≥ 4, with bounded gain" (Property N) is a conservative sufficient criterion, not a necessary one (`B_referee.md:65`).
- A fixed-connectivity network can have exactly zero shear, e.g. a pentamode network (`B_referee.md:42`). The pentamode route (F7) died at step 4 with no referee (`ROUTES.md:22`): reading, not refereed.

**The exits the referee named:** tuning, extra symmetries, non-locality, holography, constrained sectors, correlations, strong renormalization flows, and having no local graviton variable (`B_referee.md:165`).

**The referee's strongest combined statement** (`B_referee.md:209`), in plain words:
- **The conditions:** a local, weakly coupled 3+1 effective theory; a single long-range massless helicity-2 pole, a Lorentz-invariant S-matrix and ordinary factorization; universal coupling, and no compensator or custodial sector; a local analytic description in terms of h_μν.
- **What follows.** An exact linearized-diffeomorphism Ward identity forbids an h-only nonderivative mass. Generic physical reference labels instead permit shear responses that need protection or extreme tuning. With the soft-theorem and consistent two-derivative self-coupling hypotheses, leading universality and GR's nonlinear structure follow.
- **What a discrete substrate must do:** realize the relevant Ward identities, possibly relationally or in each realized history; or demonstrate another mechanism suppressing mass, Lorentz violation and low-frequency noise, with numbers.
- **What it does not prove:** that the grain must be events, a fluid, coherent, or of unbounded valency.

## 5. The axiom prices (named as prices; none is adopted)

Adopting any of these is an owner decision. The event settings were run as test settings only (`TESTS.md:147,303,445`). Any primitive absent from the registry is unapproved (`PRIMITIVE_REGISTRY_CHECK.md:17-19`).

| # | Price | Axiom or primitive touched | Substrate that pays it | What the refereed record says it buys |
|---|---|---|---|---|
| P0 | **Keep all four axioms and tune.** Two TT counterterms of natural size, leaving each net shear number at most 5.7e-99 of its natural size (refereed, reduced-Planck cell) or 9.0e-102 (framework convention; reading, not refereed). **Lane K (refereed: INCONCLUSIVE; `C3_K_referee.md`):** "Two shear tunings alone are not established; additional speed-sector protection/tuning remains an open, generically expected cost." The registered setting was not computed; K-num stands only as a bounded side result for a substitute model | none | Fixed grid, tuned | A graviton massless to the observed bound, *if* a graviton is supplied. None is produced (reading, not refereed; `SUMMARY.md:59,87`) |
| P1 | **Replace Z³ by a Poisson sprinkling of Minkowski spacetime** | Lattice: "Physical sites are the points of the cubic lattice `Z^3`" (`MINIMAL_AXIOMS_2026-06-29.md:37`) | Both event rows | Exact averages; for the link rule, bounded scalar noise (`E1p_b_referee.md:5-6`) and, for a tensor on links, a controlled admixture bound but not the exact GR mean (`C3_G-B_referee.md:3-8`) |
| P2 | **Unbounded link valency:** about 5e122 past links per event | Admissibility: "one fixed nearest-neighbor admissibility rule" (`MINIMAL_AXIOMS_2026-06-29.md:57`) | Event rows | On a Poisson sprinkling, a finite-valency Lorentz-equivariant map is excluded (BHS, `B_referee.md:52`). "Unbounded causal-set link valency also does not realize a fixed finite-neighborhood admissibility rule" (`E1p_referee.md:189`) |
| P3 | **A supplied causal order** (records carry no time, A36) | a new primitive, not in the registry | Event rows | Needed by both E1 and E1′ (`TESTS.md:273,303`). Lane F: the three tested classes of label-free growth do not supply it; a surviving rule must use the order nonexchangeably, or leave the Markovian, classical or Bell-causal scope (`C3_F_referee.md:5,30-36`) |
| P4 | **Records as events** | Record: "A site never carries more than one record; records are permanent" (`MINIMAL_AXIOMS_2026-06-29.md:79-80`) | Event rows | **A conflict as stated** (`SUMMARY.md:221`). If each Planck-density event locked an energetic matter value, the matched heating bound at Planck spacing gives a per-event fraction nearer 4e-151 (`B_referee.md:103`). It can be reconciled if an event locks only its occurrence and relations, or a conserved or gauge-invariant variable (`B_referee.md:185-190`) |
| P5 | **Continuous mobile positions** | Qubit (and Lattice) | Flowing liquid | Exact zero stiffness, but the route is dead as an untuned escape (`kill_F1b_referee.md:80-82,92`) |
| P6 | **An orientation and spin-transport structure** | a new primitive, not in the registry | Event rows, for chiral matter | Order alone gives no handedness. As finite physical event frames it sacrifices Lorentz invariance in law; supplied relationally or as link or cochain data it is "an additional substrate primitive whose locality, noise, spin connection, and taste reduction must be proved" (`C3_D_referee.md:50`) |

### 5b. Prices suggested by the wall exercises (suggested / not refereed)

These come from same-family exercises with no codex referee (§3b). They are listed so the referee can see them, not as part of the refereed record above. Each restates or sharpens a refereed price rather than replacing it.

| # | Price (suggested / not refereed) | Axiom or primitive touched | Relation to P0–P6 | Where |
|---|---|---|---|---|
| P7 | **Formation:** either a supplied event set, or a whole-region formation law that knows its final size in advance. The exercise file also lists a physical birth order that carries a frame, and a short rule that is not Bell-causal (none found) | Admissibility ("Admissibility's nearest-neighbour locality is given up for formation") | Sharpens P3: the refereed lane F leaves the order supplied; the exercise suggests what supplying it, or growing it, would cost | `TESTS.md:625`; `C3_exercise_F_formation.md:272-276` |
| P8 | **Graviton, three parts together:** (i) a classical, covariant growth law with Einstein histories; (ii) no amplitude weighting by e^{iS} (or e^{−S}) of interval-count actions; (iii) link-only readouts that reproduce Van Vleck focusing on curved backgrounds — lane G-L: refereed FAIL (codex sol, CWC; `C3_G-L_referee.md`): for the unweighted one-hop link mean on curved backgrounds, not extending automatically to G-B, E1′ or weighted/multi-hop readouts: link/GR = (ν·Δ)^{−1/2}, density-independent; the link mean de-magnifies where GR magnifies (`.claude/science/exercises/gravity-current-state-20261009/agents/C3_G-L_report.md`) | As P1, P3 and P4 ("The axiom prices are unchanged"); (i) is P7's wall | Adds conditions on top of P1–P4; does not change the refereed G-A, G-B or G-C verdicts | `TESTS.md:632-635`; `C3_exercise_G_graviton.md:247-253` |
| P9 | **Massive matter:** a non-locality scale ℓ_k plus a signed hop profile whose moments cancel. The pre-registered S0 FAILED; only the post hoc Z2 lead clears every bar | Admissibility ("strained further"); two new law data not in the registry | Adds to P2's non-locality; addresses the refereed M-A/M-C gap only as a lead | `TESTS.md:658`; `C3_exercise_M_massive_matter.md:184` |

**Not a price, a conditional requirement** (M-D, suggested / not refereed). If the M-A chain law holds, the 70 s Rb-87 experiment requires every Johnston mass vertex in an atom below about 12 MeV (2.3 s: about 63 MeV; qBounce: about 460 MeV) (`C3_M-D_report.md:55`).

**Reading** (lane P, reading, not refereed). The registered `kinetic_isotropy_primitive` is defined on the Z³ × Z_τ regulator block (`PRIMITIVE_REGISTRY_CHECK.md:63-71`), the block T1 found sufficient for one cone. Under P1, one cone would rest on Lorentz invariance in law instead, and the primitive would need re-reading.

## 6. Open questions

**C3 items refereed since v3** (`TESTS.md:660-664`). Readings are fixed in `TESTS.md`.
- **Lane K: INCONCLUSIVE (refereed, `C3_K_referee.md:3-7`).** Three-part disposition: K-num is rejected as a lane-K FAIL and accepted only as a bounded side result for a substitute model; K-ana is partially supported (its INCONCLUSIVE stands; its "PASS-by-identity branch is closed" no-go is not established); lane K is INCONCLUSIVE because the registered setting was neither computed nor defined well enough to compute. Open: re-register it in an implementable form: an interacting W(B4)-covariant stress on Z⁴. Do the 5 forms that are not gauge-invariant vanish?
- **Lane X1: bounded FAIL (refereed, CWC; `C3_X1_referee.md`).** Every ensemble-averaged nonzero-q TT stiffness spectrum is flat, with S ≥ 2.07e-3, for two kernels and for the scalar and fermion functionals in finite periodic Poisson ensembles. This is not an asymptotic no-go for random lattices.
- **Lane X2: bounded FAIL (refereed, CWC; `C3_X2_referee.md`).** Result incorporated in §2 (notes, records as the carrier).

**C3 item still with its referee.**
- **Lane G-L: refereed FAIL (codex sol, CWC; `C3_G-L_referee.md`): for the unweighted one-hop link mean on curved backgrounds, not extending automatically to G-B, E1′ or weighted/multi-hop readouts: link/GR = (ν·Δ)^{−1/2}, density-independent; the link mean de-magnifies where GR magnifies (`.claude/science/exercises/gravity-current-state-20261009/agents/C3_G-L_report.md`).** Not refereed. Question: link-only lensing: does the mean link-sum amplitude behind a lens reproduce GR's √Δ (Van Vleck) magnification to O(ℓ²/r²) for O(1) focusing? A density-independent O(1) mismatch would be a FAIL (`TESTS.md:637-648`). It decides part (iii) of P8.

**Logged since v2, not refereed** (§3b, §5b). M-D closed as a worker INCONCLUSIVE with no codex referee, since none is required for a non-FAIL (`TESTS.md:607`). The three wall exercises are logged as same-family results (`TESTS.md:618-635,650-658`). Their own "needs" lists ask for a codex referee of T-F1 and Lemma S (`C3_exercise_F_formation.md:278-281`) and of Lemma L and κ_F (`C3_exercise_M_massive_matter.md:189`). Lemma L has since been refereed (CONFIRMED WITH CORRECTIONS, `C3_LemmaL_referee.md`); T-F1, Lemma S and κ_F have no referee recorded as running.

**Other open questions.**
1. **The mediator.** No tested route produces a massless helicity-2 mode with a protecting constraint (reading, not refereed; `ROUTES.md:57`; `SUMMARY.md:87`). After lane G: picture II, independent link fields, alternative couplings and a background-free quantum sum are uncovered (`C3_G-C_referee.md:5`), and G-A's FAIL is "not a gauge-invariant no-go for order-based gravitons" (`C3_G-A_referee.md:14`).
2. **Dynamics on the events.** The source-driven link field does not cover evolution from initial data (`E1p_referee.md:184-189`). That nothing yet gives the events' own dynamics is summary prose (`SUMMARY.md:229-232`): reading, not refereed.
3. **Matter on the events.** An arc unitary, a massive one-cone mean and 1 km coherence are open (`C3_M-B_referee.md:29`); the massive variance exponent is uncontrolled (`C3_M-A_referee.md:73`); controlled massive coherence for spin-½ is open (`C3_D_referee.md:48`). Suggested / not refereed: what carries the mass vertices decides composite coherence (M-D); binding-vertex channels in 4D are uncomputed; Lemma L is refereed (CWC, scoped as in §3b) but κ_F and the S0 prefactor are not, and the Z2 lead needs a pre-registered test (§3b).
4. **Formation.** A rule that uses the order nonexchangeably, or leaves the Markovian, classical or Bell-causal scope, and matches all prescribed observables (`C3_F_referee.md:36`). Suggested / not refereed: the exercise narrows the open options to a frame-carrying birth order or a short non-Bell-causal rule (P7).
5. **Frozen substrates.** Can an exact identity hold in each realization, as a coboundary or conservation law for the stress (`E23_referee.md:122`; `kill_F1a_referee.md:58`)?
6. **The one-loop speed split on a Poisson–Delaunay lattice.** It was not run; T1(b) checked only tree level (`TESTS.md:83`).
7. **Keep-the-grid loopholes.**
   - **The registry's reopen conditions:** a non-ordinary interacting law that evades Lemma R; perfect actions with a positive one-step transfer (`APPROACH_REGISTRY.md:9`).
   - **The W1 referee's escapes:** exact emergent diffeomorphism constraints, position-blind (Wetterich) actions, covariance of the embedding together with the reciprocal cutoff, protected field-content cancellations, and suitably dynamical adjacency, "which alone is not sufficient" (`TEST_LOG.md:523-528`).
   - **One cone with stable evolution:** at the hypercubic tick A25's leapfrog is unstable, and the stable tick is not hypercubic (`TEST_LOG.md:32`).
   - **Untested:** a Z³-breaking vacuum (F4) (`ROUTES.md:40`).
8. **Beyond Poisson.** BHS does not cover other point processes, or events that carry marks or state (`B_referee.md:52`).
9. **A reading for the referee** (lane P, reading, not refereed). The registered `realized_state_primitive` makes a value that would change under a different realized state "registered data, not derivation output" (`PRIMITIVE_REGISTRY_CHECK.md:112-114`). That is a rule about what counts as derived. Whether it gives the framework a reason to require control in each realization is open; the B referee lists that requirement as supported by naturalness, not forced (`B_referee.md:160`).

## 7. Provenance

Every referee is codex gpt-5.6-sol (xhigh), from another vendor. Verdicts are quoted as the referee files give them.

| Result | Referee verdict as given | Where |
|---|---|---|
| T1, the one-cone test | **T1:** CONFIRMED WITH CORRECTIONS. **(a1):** CONFIRMED WITH CORRECTIONS — INCONCLUSIVE. **(a2):** CONFIRMED WITH CORRECTIONS — FAIL. **Controls:** CONFIRMED. **(b):** CONFIRMED — INCONCLUSIVE | `T1-REF:1-6`; `TESTS.md:74-85` |
| T2, the stiffness floor on Z⁴ | CONFIRMED WITH CORRECTIONS (a bounded FAIL) | `T2-REF:1-3,29`; `TESTS.md:130-141` |
| F1a kill (frozen random sites) | CONFIRMED WITH CORRECTIONS | `kill_F1a_referee.md:3` |
| F1b kill (flowing liquid) | CONFIRMED WITH CORRECTIONS | `kill_F1b_referee.md:3` |
| F2 kill (smooth kernels on Z³) | NOT CONFIRMED | `kill_F2_referee.md:3` |
| E2 / E3 / Lemma P | each CONFIRMED WITH CORRECTIONS | `E23_referee.md:7-9` |
| E1 (events, BD dynamics) / S1 | INCONCLUSIVE — leaning FAIL / CONFIRMED WITH CORRECTIONS | `E1_referee.md:9,13` |
| B1 / B2 / supervisor thread (backward reasoning) | each CONFIRMED WITH CORRECTIONS | `B_referee.md:9-11` |
| E1′ (link-only influence) | gravity INCONCLUSIVE; matter M-INCONCLUSIVE | `E1p_referee.md:3,9-10` |
| E1′-b (Poincaré bound) | CONFIRMED WITH CORRECTIONS. E1′ gravity after E1′-b: "PASS, strictly for the pre-registered scalar, source-driven G₀=aL proxy" | `E1p_b_referee.md:5-6` |
| K7a (one cone by symmetry; candidate pack) | CONFIRMED WITH CORRECTIONS | `TEST_LOG.md:37` |
| K3a (is the interacting stress exactly conserved?) | NOT CONFIRMED as a theorem; K3a stays INCONCLUSIVE | `TEST_LOG.md:240` |
| K3a″ (interacting shear response) | CONFIRMED WITH CORRECTIONS | `TEST_LOG.md:411` |
| W1 (dynamical lengths) | CONFIRMED WITH CORRECTIONS | `TEST_LOG.md:507` |
| FR1 / FR3 (records as the carrier) | CONFIRMED WITH CORRECTIONS ("FR1 remains a FAIL") / CONFIRMED WITH CORRECTIONS | `TEST_LOG.md:590,631` |
| C3 G-A (order as the graviton) | "FAIL, narrowly scoped to the fixed-coordinate coupling and ensemble-RMS noise specified by G‑A." | `C3_G-A_referee.md:5`; `TESTS.md:601` |
| C3 G-B (tensor on links) | "INCONCLUSIVE under the fixed reading." | `C3_G-B_referee.md:3`; `TESTS.md:603` |
| C3 G-C (protection) | "INCONCLUSIVE under the single fixed G‑C reading." | `C3_G-C_referee.md:3`; `TESTS.md:605` |
| C3 M-A (massive packet) | "CONFIRMED WITH CORRECTIONS". "Correct M-reading: M-INCONCLUSIVE." | `C3_M-A_referee.md:3,5`; `TESTS.md:575` |
| C3 M-B (unitary matter) | "CONFIRMED WITH CORRECTIONS". "The lane verdict is correctly **INCONCLUSIVE**" | `C3_M-B_referee.md:3,5`; `TESTS.md:569` |
| C3 M-C (nonnegative weights) | "CONFIRMED WITH CORRECTIONS". "The preregistered decision table formally returns **FAIL**" | `C3_M-C_referee.md:3,5`; `TESTS.md:567` |
| C3 D (spin-½) | "NOT CONFIRMED". "Corrected lane verdict: INCONCLUSIVE" | `C3_D_referee.md:3,7`; `TESTS.md:571` |
| C3 F (formation) | "CONFIRMED WITH CORRECTIONS". "The fixed reading supports a **bounded FAIL**, not a universal no-go" | `C3_F_referee.md:3,5`; `TESTS.md:573` |
| C3 K (speed sector on the tuned grid) | K-num: "REJECT as a lane-K FAIL; ACCEPT only as a bounded side result". K-ana: "PARTIALLY SUPPORTED". "Lane K: INCONCLUSIVE." | `C3_K_referee.md:3-7`; `TESTS.md:660` |
| C3 X1 (random-lattice TT spectra) | "CONFIRMED WITH CORRECTIONS — bounded FAIL." Not an asymptotic no-go for random lattices | `C3_X1_referee.md:3-7`; `TESTS.md:662` |
| C3 X2 (FR3 gases as stress carrier) | "CONFIRMED WITH CORRECTIONS — bounded FAIL." Not a general no-go for classical record substrates | `C3_X2_referee.md:3-5`; `TESTS.md:664` |
| Lemma L (exercise M, massive matter) | CONFIRMED WITH CORRECTIONS. Exact positive ladder for deterministic, strictly causal kernels; exponential needs Lorentz invariance, nonzero normalization and ends; does not validate the S0 prefactor | `C3_LemmaL_referee.md` |

**Suggested / not refereed (same model family, no codex referee; §3b, §5b):** M-D, INCONCLUSIVE "(worker; the adversarial check supports it with corrections)" (`TESTS.md:607`); exercise F_formation, "all 9 routes killed" (`TESTS.md:618`); exercise G_graviton_on_events, "all 9 routes killed" (`TESTS.md:627`); exercise M_massive_matter, "all 9 routes killed as written" (`TESTS.md:650`); with them Lemma S, T-F1, N1 and S0. Lane G-L: refereed FAIL (codex sol, CWC; `C3_G-L_referee.md`): for the unweighted one-hop link mean on curved backgrounds, not extending automatically to G-B, E1′ or weighted/multi-hop readouts (`C3_G-L_report.md`).

**Context only, not refereed:** T0 (`TESTS.md:11-15`), whose Weyl value is confirmed inside the W1 referee; the F3 and F7 checks at step 4 (`ROUTES.md:18,22,39`); W2 (`TEST_LOG.md:460`), not used; the trilemma sentence (`SUMMARY.md:55`; `ROUTES.md:54`), built from refereed T1(a2), T2 and F2; lane P's denominator arithmetic (`arith_check.py`); the Planck-convention grep (`C3_P_report.md:198`).

---

# PRICE_NOTE v6 delta (proposed): lanes R–RC and campaign C4

**Status.** This is a proposed delta to `PRICE_NOTE.md` (DRAFT v5). It is not applied and not landed, and nothing in it is adopted. Every item is named only as a price. It was drafted by Claude Opus 5.5 (same family as the workers) and is not refereed.

**Inputs.**
- The refereed lines in `TESTS.md`, lane R through campaign C4 (`TESTS.md:685-1877`), at commit `c92d127da9`.
- The `agents/C4_*_referee.md` files. Every referee is codex gpt-5.6-sol at xhigh, from another vendor.

**Pending.** RL2, RP and RB have no referee line; they appear only under open questions.

**Paths.** Bare `C4_*` file names live in `.claude/science/exercises/gravity-current-state-20261009/agents/`.

## 0. In plain words (add to §1, after "Keeping the grid with tuning", `PRICE_NOTE.md:24`)

**The boost wall.**
- On the grid, ordinary local matter has no boost that fits with its own momentum the way relativity needs. The momentum moves things by differences across neighbours, not by true shifts.
- Every way tried of feeding the grid's matter to a graviton runs into this, unless the matter stops being ordinary local lattice matter.
- The refereed cases: free particles; finitely many bands; bound composites; time as a grid direction, at second order. The vacuum shows a related effect; linking it to the same cause is a reading.

**Ways around it, each a price:**
- a continuum of bands in every cell;
- matter with long-range (1/r²) hopping;
- giving up relativity's full constraint algebra for the grid's own time slicing;
- a coupling rule defined against the vacuum.

**What keeping the grid costs.** Counted honestly, it costs more than the two shear tunings P0 stated:
- 11 gauge-restoring tunings with time on the grid;
- at least 6 with continuous time, by a sum the referees did not check as a total.

Free matter alone already produces one of the two shear numbers.

## 1. Status line (replace `PRICE_NOTE.md:3`)

> **Status.** DRAFT v6. It adds the refereed results of lanes R, RN, RS, RG and RC and of campaign C4 (`TESTS.md:685-1877`). It records the correction to the RN L1 seagull claim (`TESTS.md:1797-1802`). It names five new prices, P10–P14. RL2, RL3, RL3b, RL4, RP, RB and RN2 were folded in at wrap-up. Earlier history is unchanged from v5.

## 2. "One row per substrate" (§2, `PRICE_NOTE.md:69-76`)

### 2a. Fixed grid, untuned (`PRICE_NOTE.md:71`): cells to append

- **Averages.** Free matter with the local, translation-covariant strain coupling (V3, CWC):
  - μ_E = +1.97038864e-3 per cell for the m = 1 scalar (RN-L1 normalization);
  - staggered fermions: μ_E^stag(m) = −½·μ_E^KG(2m);
  - μ_T2 = 0 in the thermodynamic limit (`C4_V3_referee.md:19-25,48`).

  This is an E_g shear coefficient, not a cosmological constant: √g·Λ enters E_g and T_2g equally (`C4_V3_referee.md:27`).
- **One cone.** On Z³ × ℝ, non-compact naive/staggered QED gives c_e − c_γ = −8.55e-3 at α = 1/137 (F2; `C4_F2_referee.md:62`). One-loop running reaches only 7.34e-3 at 1.4 PeV (E2; `C4_E2_referee.md:19`).
- **Status.** Boost obstruction for regular local matter:
  - C3: C-FAIL, single band (`TESTS.md:1209-1215`);
  - I1, I2, I3: finite bands, band-and-zone-averaged anomaly −β (`C4_I2_referee.md:15`);
  - M1: composites (`C4_M1_referee.md:15`);
  - K2: Euclidean Z⁴, fails at O(κ²) (`C4_K2_referee.md:17`).

  Each result is bounded to its class.

### 2b. Fixed grid, tuned (`PRICE_NOTE.md:72`): cells to replace

- **Averages.** Zero, by tuning. The E_g counterterm now also absorbs the free-matter term of 2a. The other routes to removing it are a selected momentum symbol, which is itself a tuning, or R₀ (P13), which holds by definition (`C4_V3_referee.md:29`).
- **One cone.** At ξ = 1, hypercubic symmetry removes rank-2, dimension-4 matter speed splits; ξ = 2 gives −10.26 in units of e²/16π² (`C4_F2_referee.md:62`). Lane K is now answered **NO** (K1, below).
- **Price: the count is revised.**
  - **Z⁴, ξ = 1.** N_tune = 11 = 3 + 8. This is the exact operator codimension of linearized gauge restoration, after a separate cosmological-tadpole tuning. A one-loop example has every coefficient nonzero, though it produces one non-EH direction, not eight. 5 = 2 + 3 is the Euclidean-TT restriction rank, "not a proved physical two-helicity floor" (`C4_K1_referee.md:9,15`).
  - **Z³ × ℝ.** At least 6, assembled as follows:
    - 2 TT masses (`B_referee.md:26-35`);
    - at least 1 QED speed counterterm, to about 3e-17 (`C4_F2_referee.md:62`);
    - 3 graviton-speed directions, a local codimension (R2; `TESTS.md:757`; lane R INCONCLUSIVE).

    That total is the K1 worker's assembly (`C4_K1_report.md:193`): reading, not refereed.
  - **The referee's caution.** "Saying P0's old '2' is globally incomplete is too broad" (`C4_K1_referee_full.md:146-148`).

### 2c. New rows (insert after `PRICE_NOTE.md:72`)

| Substrate | Averages | Noise per realization | One cone | Graviton | Matter | Status (referee) | Price |
|---|---|---|---|---|---|---|---|
| **Fixed grid + exact-constraint VS (N-type) graviton** (lanes R–RC) | Free scalar: exact local stress, first class at linear order, 1/r with the same G (RN L1, `TESTS.md:843-850`). Its E_g response is not cancelled under the local coupling (§3 below) | None (one crystal) | γ = c_m²/c_g², equal to 1 only with R2's speed match (`TESTS.md:848`) | Two linear TT modes and a 1/r response to a supplied source (`TESTS.md:759`) | No conserved local momentum, in each tested class: single-band interacting matter in d ≥ 2 (`TESTS.md:857`); staggered fermions with contact or QED (`TESTS.md:959-960`); exact umklapp-free interactions in the analytic and meromorphic classes (`TESTS.md:1080`); free single-band matter cannot close the algebra (C3, `TESTS.md:1209-1215`) | R, RN, RG, RC: INCONCLUSIVE (`TESTS.md:767,873,1079,1226`). RS: bounded FAIL, momentum only (`TESTS.md:959`) | P14, or an exact additive lattice momentum not in the axioms (`TESTS.md:988`), or matter beyond regular local finite-band (P10) |
| **Fixed grid, N bands per cell or coarse cells of L³ sites** (RI, RM) | Band-and-zone-averaged C3 anomaly exactly −1 per mode at every finite N or L. Linear-only TT falls as L⁻⁴ in the radial comparator, and is completion-dependent. One φ⁴ calculation gives a speed shift of about 2e-5·λ² through L = 16, with no proven limit (`C4_I3_referee.md:17,21`) | None | As the fixed grid | Supplied | Composites obey the same sum rule (`C4_M1_referee.md:15`) | RI: **FAIL (bounded)**, for regular positive-energy free one-particle Bloch theories and finite-band periodic quadratic networks (`TESTS.md:1402-1424`). M1: **FAIL (bounded)** | P10. Q-RI: P0 needs L* ≈ 1.18e25 (cutoff about 0.65 keV), against L ≤ 7.65e14 from a 10 TeV band; conditional on the linear-only completion (`C4_I3_referee.md:13`) |
| **Fixed grid, preferred foliation** (RF, RF3, W2, W3) | Cubic-only gravity: six O(k⁰) mass invariants. The static model shows 2 TT suppressions, 1 determinant cancellation and a Cassini-level ratio, not 5 P0-level tunings (`C4_F1_referee.md:11`) | None | Z³ × ℝ QED needs a counterterm to about 3e-17; ξ = 1 removes it (`C4_F2_referee.md:62`) | Projectable fails. Non-projectable matches GSS. The rotation sector stays obstructed in the single-band fixed-generator ansatz (`C4_F1_referee.md:9,17`). Minimal λ = 1 broken theory: a ghost for a < 0, not unique (`C4_W2_referee.md:17`). Khronometric completion: pathological. Repaired m₄ = −a/2: unstable for λ > 1 below k*. General quadratic search: 4 healthy candidates, all far from GR (`C4_W3_referee.md:31`) | Parity-odd b₀ and (k_AF)₀ are forbidden only by the chosen action's parity (`C4_F2_referee.md:9`) | RF: **INCONCLUSIVE** (F1, F2 NOT CONFIRMED). RF3: **INCONCLUSIVE**. W2: **INCONCLUSIVE**. W3: **INCONCLUSIVE**, with bounded FAILs for 2 subclasses | P11. Explicit one-grid subcases also need M_* and L of a few 1e9, and a k⁶ coefficient of 1e38–1e39: hierarchies, "not automatically precision tunings" (`C4_F3_referee.md:17`) |

### 2d. Events, influence along links only (`PRICE_NOTE.md:76`): graviton cell to append

**RL1: INCONCLUSIVE, leaning FAIL** (NOT CONFIRMED as FAIL). For regular pre-caustic scalar propagation:
- the massless 4D Johnston sum is exactly the one-hop link kernel;
- extra hops add tails, but no direct-cone term;
- normalizable one-hop kernels in ρV keep the ν^{-1/2} coefficient;
- the BD mean has the unstable pair 0.375598 ± 5.052239i;
- no scalar density repairs a thin Ricci lens at first order;
- three stable L = 6 operators remain open (`C4_RL1_referee.md:24`); RL2 is pending.

This gives part (iii) of P8 refereed sub-results. P8 itself stays suggested.

## 3. Correction carried into the note (dated 2026-10-11)

**The claim corrected.** The RN L1 referee's statement that a determined unitary seagull cancels free matter's uniform-strain TT response "exactly" (`TESTS.md:851`) holds only:
- for T_2g; or
- for the formal finite-box unitary that keeps its boundary/seam terms.

**For the local, translation-covariant coupling it fails in E_g** (`C4_V3_referee.md:10-12,46`; `C4_V2_referee.md:9`).

**The same correction applies to:**
- I3's "μ = 0 at every L";
- V1's "exact eigenstate for every h", which holds only with R₀;
- W1's premise (`TESTS.md:1348`).

**Effect on the note.** v5 never relied on the seagull. The only effect is the larger natural size of P0's E_g number recorded in 2a.

## 4. "The axiom prices" (§5, `PRICE_NOTE.md:160-168`)

**P0, revised (replace `PRICE_NOTE.md:162`).** Keep all four axioms and tune.
- **Shear.** Two TT counterterms, each leaving at most 5.7e-99 of natural size (`B_referee.md:35`). The E_g natural size now includes the free-matter term (V3).
- **Count.** Z⁴: 11 by operator codimension (5 as the Euclidean-TT rank). Z³ × ℝ: at least 6 including matter speeds, assembled; the total is a reading (§2b).
- **Speed sector.** One refereed instance: F2's non-compact naive/staggered QED on Z³ × ℝ needs one counterterm at about 3e-17, and ξ = 1 removes it. The full speed count stays unrefereed.
- **Touches:** no axiom. **Status:** as in v5, "an owner decision, not a calculation" (`SUMMARY.md:66`).

| # | Price | Axiom or primitive touched | Substrate that pays it | What the refereed record says it buys |
|---|---|---|---|---|
| P10 | **A continuum tower per cell:** an infinite-dimensional, unbounded one-particle fibre in each cell (a complete reciprocal-lattice tower) | Qubit: "The full one-site possibility domain has algebraic presentation `M_2(C)`" (`MINIMAL_AXIOMS_2026-06-29.md:47`), at the one-particle level. The microscopic claim is open: it "does not prove an infinite microscopic on-site Hilbert space" (`C4_I1_referee.md:15`) | Fixed grid, N bands | Exact C1 + C3 closure for free matter, given an integrated positive-energy Poincaré representation or band-gluing assumptions; Nelson integrability is assumed. Patches within one tower cannot be decoupled; separate sectors may be (`C4_I1_referee.md:7,13,21`) |
| P11 | **A preferred foliation:** keep the grid's slicing and give up GR's hypersurface-deformation algebra | No axiom. A time metric is downstream content (`MINIMAL_AXIOMS_2026-06-29.md:185`); the slicing would need a bridge or primitive | Fixed grid, preferred foliation | It removes the boost leg of C3, but not the rotation sector in the single-band fixed-generator ansatz (`C4_F1_referee.md:9`). It costs six cubic mass invariants (`C4_F1_referee.md:11`), the exact relation m₄ = −a/2 when repaired (`C4_W3_referee.md:31`), and one-grid hierarchies (`C4_F3_referee.md:17`). No window-compatible healthy region has been exhibited or excluded. INCONCLUSIVE |
| P12 | **Time on the grid with the space step (Z⁴, ξ = 1)** | Lattice names Z³ (`MINIMAL_AXIOMS_2026-06-29.md:37`). The Z³ × Z_τ block is that of the registered `kinetic_isotropy_primitive` (`PRICE_NOTE.md:182`, a lane-P reading) | Fixed grid | Matter speeds protected exactly (`C4_F2_referee.md:33`). Costs: N_tune = 11 in the graviton sector (K1); Euclidean, so no boosts; κ² Killing failure (`C4_K2_referee.md:17`); coupled reflection positivity unproved; 9.899 is a real-time leapfrog instability only (`C4_K2_referee.md:13`) |
| P13 | **A vacuum-referenced coupling rule** (Rule R; R₀ subtracts the strained vacuum energy) | No axiom. A coupling choice the supplied structure does not fix "remains a named conditional" (`MINIMAL_AXIOMS_2026-06-29.md:89-90`) | Fixed grid, all rows | R: the interaction part of μ cancels at O(λ²) with no tunable number, conditionally (`C4_V1_referee.md:17`). R₀: μ = 0 "by definition" (`C4_V3_referee.md:29`). Neither is basis-free or derived (Kato does not fix them; Gell-Mann–Low is non-local, `C4_V2_referee.md:11`). They leave an O(λε) scattering Ward defect, with relative size (ka)² (`C4_V1_referee.md:13`; `C4_V2_referee.md:19`) |
| P14 | **Non-local (SLAC-type) matter:** 1/r² hopping, or a momentum density with power-law tails and umklapp-free interactions | Not Admissibility as worded, which fixes only the local odds rule (`TESTS.md:979-981`). But no finite-component analytic network produces it (C1, `TESTS.md:1168-1177`), and dressing in D1's class cannot (`C4_D1_referee.md:17`) | N-type row | It can feed the shift constraint: the SLAC stress satisfies the linear first-class identities, but is power-law non-local (`TESTS.md:1066-1067`). Exact SLAC at finite Z forces a 1/r² bare tail amplified by 1/Z (`C4_D1_referee.md:11`) |

## 5. Open questions (append to §6, `PRICE_NOTE.md:184-209`)

- **Pending lanes, pre-registered, no referee line yet.**
  - **RL2:** the curved mean and the physical variance of the three stable L = 6 operators. It decides part (iii) of P8 (`TESTS.md:1755-1771`).
  - **RP:** Pauli-type species sum rules for μ_E. Can matter content cancel the free E_g term order by order (`TESTS.md:1822-1851`)?
  - **RB:** boosts that are not first moments. This is the one hypothesis shared by C3, I1/I2, M1 and K2 (`TESTS.md:1853-1877`).
- **Open within refereed scope.**
  - Composite matter outside M1's class: non-number-conserving embedded sectors, massless sectors, unbounded continua (`C4_M1_referee.md:15`).
  - Decoupled Poincaré sectors (`C4_I1_referee.md:13`).
  - The Z⁴ general no-go hypotheses, and coupled reflection positivity (`C4_K2_referee.md:11,15`).
  - Strong-dynamics routes outside E1's spectator class (`C4_E1_referee.md:17`).
  - QED dressing beyond the analytic Coulomb-gauge ansatz (`C4_V3_referee.md:44`).
  - Kitaev at all sectors and T > 0 (`TESTS.md:1192-1205`).

## 6. Provenance (append to §7)

| Result | Referee verdict as given | Where |
|---|---|---|
| R1, R2 / R3 | NOT CONFIRMED → INCONCLUSIVE / CWC; lane R INCONCLUSIVE | `TESTS.md:736-767` |
| RN L1 / L2 / L3 | CWC (F-FAIL by binary) / NOT CONFIRMED / CWC; lane INCONCLUSIVE | `TESTS.md:843-873` |
| RS S1, S2 | each CWC; bounded FAIL, momentum only | `TESTS.md:935-959` |
| RG G1 / G2 / G3 | NOT CONFIRMED / main checks pass / CWC; lane INCONCLUSIVE | `TESTS.md:1042-1079` |
| RC C1 / C2 / C3 | CWC FAIL / NOT CONFIRMED / CWC C-FAIL; lane INCONCLUSIVE | `TESTS.md:1168-1226` |
| C4 I1, I2, I3, M1, D1, D2, E1, E2 | each CONFIRMED WITH CORRECTIONS | `C4_{I1,I2,I3,M1,D1,D2,E1,E2}_referee.md:1` |
| C4 F1, F2, F3 | each NOT CONFIRMED (INCONCLUSIVE) | `C4_F{1,2,3}_referee.md:1` |
| C4 K1 / K2 | CWC (N_tune = 11) / CWC (INCONCLUSIVE) | `C4_K{1,2}_referee.md:1` |
| C4 W1 / W2 / W3 | CWC (bounded FAIL) / NOT CONFIRMED / CWC (INCONCLUSIVE) | `C4_W{1,2,3}_referee.md:1` |
| C4 V1 / V2 / V3 | NOT CONFIRMED / NOT CONFIRMED / CWC, (a) and (b) FAIL | `C4_V{1,2,3}_referee.md:1` |
| C4 RL1 | NOT CONFIRMED → INCONCLUSIVE, leaning FAIL | `C4_RL1_referee.md:1` |

### Wrap-up additions to the v6 delta (21:05Z)

These were refereed after the delta was drafted. All verdicts are from codex sol.

- **RP (Pauli-type species sum rules for μ_E): FAIL (bounded).** Cancelling E_g needs the count rule R0 plus the mass relations R2, R4 and R6. R4 is Pauli's quartic supertrace. Only exactly matched spectra cancel to all orders. This turns P0's E_g tuning into the same kind of naturalness problem as the cosmological constant (`C4_P1_referee.md`).
- **RB (boosts that are not first moments): FAIL (bounded).**
  - Gravity's affine-lapse smearing forces a first-moment boost.
  - On the Brillouin torus there is no global undeformed Lorentz action, so no DSR/κ-Poincaré escape on the lattice.
  - The lattice is therefore a preferred-frame theory (`C4_B1_referee.md`).
- **RN2 (interacting matter without number conservation): INCONCLUSIVE, leaning FAIL.** A regular-band subclass is a rigorous bounded FAIL (`C4_N1_referee.md`).
- **Event row update: lensing passes in the mean; noise fails at the bar.**
  - RL2: GR's √Δ lensing holds in the mean for all three stable layer operators. This is a positive result, and it settles part (iii) of P8 in the mean (`C4_RL2_referee.md`).
  - RL3, RL3b and RL4: the noise fails the 1e-19 m locality bar for edged sources over 1 Gpc. This is a bounded FAIL, and it needs ℓ_k ≈ 7e-19 m (`C4_RL4_referee.md`).
  - Price reading: on the event substrate (P1–P4), lensing works if the non-locality scale is about 7e-19 m instead of 1e-19 m. That is a miss of less than one decade.

# PRICE_NOTE v7 delta (proposed): campaign C5, P15–P191

**Status.** This is a proposed delta to `PRICE_NOTE.md`. It is not applied and not landed, and nothing in it is adopted. Every item is named only as a price.
- Drafted by S29, Claude Opus 5.5. That is the same family as every worker and every earlier synthesis. **This draft is not refereed.**
- It replaces the v7 drafts in S23 §8.2 and S26 §8.2, neither of which was applied: `PRICE_NOTE.md` still ends at the v6 delta (`PRICE_NOTE.md:251-413`).

**Inputs.**
- The refereed lines in `TESTS.md` for campaign C5, rounds 1–19 (`TESTS.md:2302-8545`; the file at commit `e265c3a717` plus the 07:03Z–07:07Z additions for R19-26, R19-27 and R19-28).
- The `agents/C5_*_referee_verdict.md` files.
- Three verdicts read from the scratchpad and not yet recorded in `TESTS`: vR19-21, vR19-23 and vR19-24 (`SP/ref_R19-{21,23,24}/REFEREE_VERDICT.md`).
- Every referee is codex gpt-5.6-sol at xhigh, from another vendor.

**Pending.**
- R19-26 has a worker reading (PHOTON-EXACT, `TESTS.md:8532-8545`), priced as P191 [worker]; its referee is running.
- R19-25 and R19-28 have no reading yet. P192 onward is reserved for them.
- R19-27 has a worker reading, priced as P190 [worker]; its referee is running.
- [see the close addendum, 10:41Z]

**Paths.**
- Bare `C5_*` file names live in `.claude/science/exercises/gravity-current-state-20261009/agents/`.
- `vX` = `C5_X_referee_verdict.md`. `rX` = `C5_X_report.md`.
- `S23`, `S26` = `C5_S23_synthesis.md`, `C5_S26_synthesis.md`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.

**Labels.**
- **[ref]**: referee-confirmed, in its stated scope.
- **[ref, bounded]**: a refereed no-go in a stated class.
- **[worker]**: not confirmed or not ruled on.

---

## 0. In plain words (add to §1, after the v6 "boost wall" text)

**What campaign C5 found, in one paragraph.**
- Every gravitational observation we checked can be met on the grid, but only by adding rules that state the answer.
- Gravity's source can be made exactly Einstein's with no tuned number. One rule, (Σ), says the lowest state gravitates only as a relativistic vacuum with zero cosmological constant, up to two derivatives. Two more rules are needed: the gravitating density is the weight-1 one, gravity's own included; and something carries away what (Σ) removes as space grows.
- (Σ) fixes 34 numbers of the lattice vacuum's gravitational response:
  - 30 by gauge (Ward) identities;
  - 2 by Lorentz conditions;
  - 1 by Λ = 0;
  - 1 is a convention for G.

  A continuum theory gets the first 32 from symmetry (vR19-20:20-37).
- So the rules impose relativity; they do not derive it. With them, the grid predicts nothing new for today's vacuum (vR19-20:74).

**What it costs, by the same yardstick.**
- **The same move pays the light cones of matter.** The rule "the law's lowest state contributes only its Lorentz-invariant dressing" is a number-free clause under the campaign's own convention. On that convention it pays the electron–photon block just as (Σ) pays gravity (vR19-24:37,41).
- **Counted as conditions, both cost numbers:**
  - the charge block, 4 per class, re-set at each loop order;
  - gravity, 33 conditions.
- **Which count applies is a bookkeeping choice the owner must make.** It is not physics (vR19-24:35,39).

**What no rule here pays.**
- **A graviton made from qubits.** The graviton is supplied (P-N1).
- **Epochs other than today's lowest state.** There the subtraction misses enormous lattice shear and pressure: a severe conflict, conditional on reading the shear as a graviton mass (vR19-21:42).
- **Growing space without leftover energy.** No refereed mode shows it. A worker finds that a growing-spacing lattice (V1) manages the pressure part if the Higgs-sector counterterms are written per site (R19-27; referee running). That still leaves V1's free length scale and its frame law.

## 1. Status line (replace `PRICE_NOTE.md:3`)

> **Status.** DRAFT v7. It adds campaign C5's refereed results (`TESTS.md:2302-8545`) and names its prices, P15–P191 (syntheses S5–S29). Every price is named; none is adopted. Prices that were refereed as FAIL, non-local, non-conserved or not payable stay listed so the owner can see them; they are not payable under the registered readings. They are P74, P120, P123, P126, P127 (as a covariant vertex with R9-9's graviton), and P108's V0 half. Rows marked [worker] rest on unrefereed items. Earlier history is unchanged from v6.

## 2. "One row per substrate" (§2): new rows (insert after the v6 §2c rows)

| Substrate | Averages | Noise per realization | One cone | Graviton | Matter | Status (referee) | Price |
|---|---|---|---|---|---|---|---|
| **Z³ × ℝ, box-exact law, SM content (C-box), with or without (Σ)** (C5 rounds 9–19) | **Without (Σ):** the shear rows are the full uniform-strain Hessian of the lowest-state energy (Lemma H; vR19-15:3), with A = μ_E − μ_T2 ≈ 3.5e-19 per cell at SM masses. A zero needs a radiatively unstable ~1e-98 tuning, conditional on the graviton bridge (vR19-15:16,18). **With (Σ):** zero for the lowest state by stipulation (vR19-19:15; vR19-20:74) | None (one crystal) | **Graviton cone:** all axial and off-axis rows zero at one loop, with 7 knobs, in the O(q) convention (vR18-13:11). Exact W1 exists for the massive species (vR19-5:17); the photon's exact completion is OPEN (vR19-16:13). **Matter cone:** 4 per class (vR19-12:3,17). One law across SM masses: OPEN (vR19-11:29) | Supplied (P-N1). Its Ward-violating rows are invariant pole shifts (vR19-23:76) | Charge block 4 per class / 10 per species / 2 q²-correlated (vR19-12:17) | R18-9, R18-13, R19-5, R19-12, R19-15, R19-19, R19-23: CWC. R19-11: OPEN. R19-20: IRREDUCIBLE. R19-24: NOT CONFIRMED (fixed reading DYNAMIC-CLAUSE by construction on the literal convention) | **Route A, per class:** 11 equalities + photon window + CC; 10 + window + CC under (d-i) (vR19-12:17). **Or:** P179 (Σ) + P73 (4 per class) + CC by (S). **Or:** P179 + P188, zero numbers by convention |
| **C-box-E** (C-box + site creation, √h fixed per site, E-sector) | (S) + (d-i) + N_red: exact classical GR on T_m − (V − e₀)g (vR18-6:13). Site creation leaves a creation energy under completed-law accounting (conditional; vR19-10:3,34). The D1 symmetric-phase enthalpy is 2.68e106 ρ_Λ; (d-i) absorbs it only in this class (vR19-21:32-38) | — | As C-box | Supplied | As C-box | R18-6: literal CONFLICT, N_red consistent. R19-10: OPEN. R19-13: NO-LOCAL-ESCAPE (NN scalar). R19-21: OPEN | P92, P70(d-i), P135, P52, plus P165 or P171 |
| **V1: fixed sites, growing spacing** | e₀ ∝ a⁻⁴. (S_ad) closes Bianchi homogeneously, but it is not a checked global completion (vR19-14:6). Conditionally local for planar NN-scalar cold dust (vR19-17:3) | — | As C-box | Supplied; G must be supplied in metric units | Free fields only tested | R19-14: OPEN. R19-17: CWC (conditional LOCAL-OK). R19-27: worker V1-RECEIVER in 𝒱_ct (referee running) | P172 + P174 (ℓ/ℓ_P drifts by 4.86e36 since 10 MeV reheating; vR19-14:7) + P175 (+ P176). Enthalpy receiver: P190 [worker, R19-27 V1-RECEIVER; referee running] |
| **Set A: continuum base, records as the metric (E1, E2)** | **E1 + N_c CONSTRUCTED** in the weak-field static/quasi-static scope (R18-7). **At a = 2 with the complete split, the record noise cancels on every spacelike mode** (Theorem I₀; vR19-2:5,19). Not shown to become Λ (vR19-2:3) | Per mode, E2's noise = \|R\| × E1's (vR19-8:9) | Exact (continuum) | Supplied | Continuum matter | R18-11: OPEN. R19-2, R19-6, R19-8: NOT CONFIRMED → OPEN. **R19-18: literal TIE-BROKEN**: E2 predicts d_L^GW/d_L^EM = exp(γt_lb/2), 0.44–1.30% at z = 1 (vR19-18:5,9) | E1: P138–P140, or P157 + P154–P156. E2: add P162–P164 |
| **Z₂ qubit window (graviton production)** | — | — | — | **RK point:** a k⁰ f-sum, so the SMA gives a flat gap (vR19-1:7,17). [worker, R19-7] Off RK: no linear T₂ at ≤ 8-site ED. **Finite-S truncation of P-N1:** the constraints are destroyed (Lemma J; vR19-22:7). A finite-site graviton is OPEN (vR19-22:17) | — | R19-1: NEITHER (CWC). R19-22: OPEN (CWC). R19-25: [pending] | P-N1 (`AX:47`), or P183 + P184/P185 (none built) |

**Note on the table.** The "with (Σ)" entries are stipulations. The "Averages" zero for the lowest state is imposed, not predicted (vR19-19:15). A Ward-complete source definition can set the five Ward-violating rows to zero (vR19-23:74).

## 3. Corrections carried into the note (dated 2026-10-13)

- **Exact conservation is available.** S26's named gap "no exact W1 completion exists for any vertex" (`S26:427`) is withdrawn for the massive species. U, and every admissible smooth massive Wilson–Dirac pair kernel, have exact completions in class 𝒢 (vR19-5:3,5,17). W15 prices the translation Ward identity W2, not W1 (vR19-5:3).
- **The face1 payment is conditional.** face1 is not itself a pole. It enters through the A₁ Schur complement, so the R18-13/R19-12 face1 zero must be recomputed (vR19-23:26-38).
- **Set A's overshoot is withdrawn.** It was not established (vR18-11:19). The γ-trade P-r15c is not "now necessary" (`S26:181`). At a = 2 with the complete split, the spacelike noise cancels (vR19-2:5).
- **Creation energy is conditional,** not a universal P93 failure (vR19-10:3,36).
- **The R19-20 owner statement** is corrected in seven places (vR19-20:62-70). See `TESTS` closing §3.
- **The charge block is not a refereed counterterm no-go.** Its 4-per-class count stands in the registered basis (vR19-12). Whether it is "numbers" depends on the counting rule (vR19-24:41).
- **(Σ)'s linear part is a general local quadratic graviton counterterm through O(p²),** with mass-like pieces included. That is R19-24's Lemma E, with corrected terminology and sign (vR19-24:27,33).

## 4. "The axiom prices" (§5)

Format: number, price, then the axiom text touched, the status, and the source. "None" means a dynamical, tuning or history choice that the axioms leave downstream (`AX:114-130`). Nothing is adopted.

### 4a. P15–P106 (carried)

As S23 §8.2 (`S23:1034-1127`), with S26's replacement rows (`S26:864-869`) for P52, P70, P92, P93 and P96. Round-19 status changes to these:
- **P0** (tune the shear). The tuning is ~1e-98 and radiatively unstable in the registered bridge, conditional on the graviton bridge (vR19-15:16). Counted once with P167.
- **P52** (site creation). A conditional creation-energy obstruction (vR19-10:34). Entangled birth needs R > 256a (vR19-13:15). See P165 and P171.
- **P70(d-i).** It absorbs the D1 symmetric-phase enthalpy, 2.68e106 ρ_Λ, only in class 𝒟/C-box-E; it cannot be posed on V1 (vR19-21:38; vR19-14). Other carriers are not excluded (vR19-20:65). [worker, R19-27] That figure assumes fixed physical-unit Higgs counterterms. With per-site counterterms the state-dependent part vanishes on V1, and suggestedly in C-box-E. Then (d-i) would be needed only for the lowest state's W₀ (`rR19-27:230`).
- **P73** (charge counterterms). On one law: 4 per class, 10 per species, or 2 q²-correlated (vR19-12:17). The values are re-set at each loop order (vR19-24:43). See P188.
- **P92** ((S)). One truncation of (Σ). (Σ) ⇒ (S) only under a source/Hamiltonian identification (vR19-20:8).
- **P93** (late-vacuum stability). It belongs to the stipulated Λ = 0 rule and is not evidence for the grid. OPEN (vR19-20:69,74).
- **P96** (emergent constraint). At the RK point the SMA gives a flat gap (vR19-1:7). A light-like branch would need a non-RK phase. [worker, R19-7] None was seen off RK at ED sizes.

### 4b. P107–P128 (carried from S23, with status at close)

- **P107. Completion N.** `AX:82-83`; `AX:187`.
  - Literal N conflicts with (d-i) when W ≠ 0 (vR18-6:5).
  - N_c is CONSTRUCTED in scope (R18-7).
  - **Its self-stress part is logically independent of (S\*)** (vR19-20:16, D2).
- **P108. V0 + SF.** `AX:187`. **The V0 half is withdrawn** (vR18-5:3). SF stays a stipulation.
- **P109. Wilson–Dirac μ_T2 row.** None, or `AX:47`. A shape row (vR17-13). Twisted mass (P169) makes the Dirac rows even in m (vR19-11:27).
- **P110. Z₂-clock reading.** `AX:47`; `AX:57-61`. RK point: NEITHER (vR19-1:17).
- **P111. Uniform-strain-conserving dynamics.** `AX:57-61`. Unchanged.
- **P112. Shift action.** `AX:37-41`. Unchanged.
- **P113. N = 2 metric readout.** `AX:82-90`. Unchanged.
- **P114. Composite T₂ labels.** `AX:82-90`. Unchanged.
- **P115. Low-symmetry slots plus block encoding.** `AX:37-47`. Unchanged.
- **P116. Non-local multipliers (W7).** `AX:116-130`. Unchanged.
- **P117. Boundary Poincaré charges.** `AX:82-83`. [worker] Reduces to P141 within Corollary N (R18-8).
- **P118. Observable-algebra readout bridge.** `AX:82-83`; `AX:187`. Unchanged.
- **P119. Consistency-selection rule for final-state Λ laws.** `AX:94`; `AX:185-186`. Unchanged.
- **P120. Record sourcing with re-added I.** **Not payable as stated.** Unchanged.
- **P121. Matter-side relaxation.** `AX:60-61`; `AX:185`. Unchanged.
- **P122. K₆ off-axis condition.** None; `AX:187`. Extended to fermions [ref, vR18-9:19]. **face1 is to be paid as the A₁-completed pole** (vR19-23:38; P186).
- **P123. M vertex.** **Not payable under a local law.**
- **P124. Non-canonical shift action.** `AX:187`; `AX:116-123`. Unchanged (W15).
- **P125. (S′-start) with P94′.** `AX:116-130`; `AX:94`; `AX:185-186`. Unchanged.
- **P126. VU.** **Not conserved; withdrawn** (vR17-12).
- **P127. VM placement.** **Not covariant with R9-9's graviton** (vR17-12:13).
- **P128. Non-Lagrangian partner for (d-i).** `AX:187`. Excluded only for a single ultralocal P(X) (vR17-11:35).

### 4c. P129–P147 (carried from S26, with status at close)

- **P129. VW placement stencils, signed.** `AX:187`. Used by the refereed four-row and all-row roots, in the O(q) convention (vR18-9:21; vR18-13:11).
- **P130. Move set that unfreezes the charge-free Z₂ sector.** `AX:57-61`. Unchanged.
- **P131. Higgs-portal singlet.** Content. Unchanged.
- **P132. Vector-like 5-plets, n5 ≥ 2.** Content. Unchanged.
- **P133. Dirac pair block (family 𝔇).** `AX:187`. Exact W1 for UD is in class 𝒢 (vR19-5:17).
- **P134. Dirac O(q²) placement.** `AX:187`. [worker] Unchanged.
- **P135. N_red.** `AX:82-83`; `AX:187`. Its self-stress part is independent of (Σ) (vR19-20:16).
- **P136. J2.** `AX:47`; `AX:187`. **J2-GAUGE-BRIDGE:** at free one loop, conditional on H-V3, P136(ii), P157 and the class-𝒟 receiver, (S) removes the graviton zero point (vR19-3:8,12).
- **P137. Meter-sector stress for set A's injection.** `AX:185`; `AX:187`. [worker] Unchanged.
- **P138. Causal conserving projection Π.** `AX:187`. Its FRW lift is law data (P154; vR19-2:19).
- **P139. Harmonic gauge.** `AX:82-83`. Immaterial for the mean at a = 2 (vR18-11:21).
- **P140. Insertion weight a.** `AX:82-83`; `AX:187`. **Replaced at a = 2 by P157** (vR19-6:3,21). Not literally consistent with R18-7.
- **P141. Accept the asymptotic Poincaré anomaly.** `AX:57-61`; `AX:82-83`; `AX:187`. Unchanged.
- **P142. No edge quanta initially.** None. Made concrete as P149 (vR18-12:19).
- **P143. Dipole conservation on the moves.** Unchanged.
- **P144. Planar diagonal-label laws.** Unchanged.
- **P145. The record as √−g T (a = 2).** `AX:82-83`; `AX:187`. [ref] Theorem G selects a = 2 (vR18-11:3). The overshoot is not established (vR18-11:19). **Merged into P157.**
- **P146. The S/V noise's energy history.** `AX:92-95`; `AX:185`. (U) is not a closed zero-start solution (vR18-11:5).
- **P147. Photon window.** `AX:187`. A fifth continuous knob, a finite-window selection (vR18-9:17). Route B spends it as an equality (vR19-12:17).

### 4d. New prices P148–P191 (rounds 18–19; named only, none adopted)

| # | Price (worker label) | Axiom text touched | What the record says it buys or costs | Source |
|---|---|---|---|---|
| P148 | **Corner dichotomy** (P-r1812a): light corner copies or stable lattice-scale corner relics | `AX:37-41`; `AX:57-61` | [worker] The universal dichotomy is **not confirmed** (vR18-12:5). Listed so the owner can see it | `rR18-12:231` |
| P149 | **History bound on corner relics** (P-r1812b; P142 made concrete) | None (a history condition); `AX:181-186` downstream | [ref] Y ≤ 3.76e-28 (doubler) or 1.79e-29 (2/a corner photon) from Ωh². The T_RH brackets are not confirmed (vR18-12:13,19) | `rR18-12:232` |
| P150 | **Expansion law that dilates crystal momentum** (P-r1812c) | `AX:37-41`; `AX:185-186` | [worker, conditional] Self-cleaning. The referee says FRW can conserve comoving crystal momentum while physical momentum redshifts (vR18-12:15) | `rR18-12:233` |
| P151 | **Signed own-direction stress placement** (P-R18-13a): w_d ≈ −1.17, w_o ≈ −0.196 | `AX:187`; `AX:114-130`; `AX:85-90` | [ref, O(q) convention] Pays face1 and face2 (vR18-13:7,11). **The face1 part is conditional on the A₁ completion** (vR19-23:38) | `rR18-13:348-352` |
| P152 | **VW off-axis extension** (P-R18-13b, VWa-geo) | `AX:187` | [ref] A unique VW extension is not established (`TESTS.md:7513`) | `rR18-13:353` |
| P153 | **RK tuning v = t** (P-r19-1a): one number for the Hamiltonian | `AX:57-61`; `AX:114-123` | [ref, NEITHER] Buys exact relaxational dynamics, but a flat SMA gap, not a cone (vR19-1:7,17) | `rR19-1:315` |
| P154 | **FRW lift of Π** (P-r192a) | `AX:185`; `AX:187` | [ref] "The FRW lift is genuine law data". Lifts A and B differ in sign and w (vR19-2:7,19) | `rR19-2:252` |
| P155 | **Complete least-decoherence split** (P-r192b) | `AX:82-83`; `AX:60-61` | [ref, newly stipulated] The spacelike four-channel source cancels exactly (Theorem I₀; vR19-2:5) | `rR19-2:253` |
| P156 | **Near-cone record split** (P-r192c) | As P155 | [worker] Decides the sign and size of any noise Λ. The near-cone term is incomplete (vR19-2:3) | `rR19-2:254` |
| P157 | **W1-weight: the gravitating source is the weight-1 density √−g T^{μν}, gravity's own included** (P-r196a; **merges P145 and P-r193a**, counted once) | `AX:187`; `AX:82-83` | [ref] Lemma L. A coherent number-free common source for set A's noise and the graviton vacuum; it replaces R18-7's a = 4 (vR19-6:5,21). Independent of (S\*) (vR19-20:15) | `rR19-6:249`; `rR19-3:265` |
| P158 | **Lattice graviton's cubic forward vertex** (P-r193b) | `AX:47` (supplied sector) | [worker] Needed for the c = 1 calibration on the lattice. Rides on P-N1 and W7's degree 3 | `rR19-3:266` |
| P159 | **Channel-decoupled stress, class 𝒢** (P-R19-5a): independent pair and scattering law data | `AX:187`; `AX:114-130`; `AX:85-90` | [ref] Exact W1 for the massive species with the root's placement data; rows unchanged (vR19-5:11,17) | `rR19-5:276-279` |
| P160 | **Photon soft-corner continuum clause** (P-R19-5b) | `AX:187` | [ref] Proposition K: corner cost C_e r⁴ (vR19-9:11). The exact torus-wide kernel is not yet smooth at the wrap cut (vR19-16:7,13). [worker, R19-26] Smooth after the re-placement P191 | `rR19-5:280-283` |
| P161 | **Off-RK ratio v/t** (P-r19-7a) | `AX:57-61` | [worker] At accessible sizes it buys nothing: no linear T₂ | `rR19-7:330` |
| P162 | **FRW lift of E2's friction: L0** (P-r198a = P-r1918a, counted once) | `AX:185-186`; `AX:187` | [ref] Under L0, d_L^GW/d_L^EM = exp(γt_lb/2): E2's siren signature (vR19-18:9) | `rR19-8:257`; `rR19-18:258` |
| P163 | **The sink is Π** (P-r198b; retires P-r12b) | `AX:82-83` | [ref] The formal law is stipulable. **No physical sink action or stress with a unique homogeneous budget is constructed** (vR19-8:5,17) | `rR19-8:258` |
| P164 | **Near-cone band cap** (P-r198c) | As P156 | [worker] Needed only with P-r14b | `rR19-8:259` |
| P165 | **Site-insertion energy** (P-r1910a): super-Planckian insertion, a per-species ~1e-62 tuning, or an unbuilt principle | `AX:37,40`; `AX:43-53`; `AX:186-187` | [ref, conditional] The Lemma S-ins inequality is confirmed; the physical normalization is not selected by the axioms (vR19-10:15-26,34) | `rR19-10:209-214` |
| P166 | **Dislocation-core energy** (P-r1910b) | `AX:37`; `AX:40-41` | [ref, arithmetic] −3.42e61/v ρ_Λ for the supplied bond rule. It is negative, so it is a model-dependent energy, not injection (vR19-10:30) | `rR19-10:215` |
| P167 | **Spectrum-tuned gravity block** (P-R19-11a) | `AX:187`; `AX:114-130` | [ref, conditional] The IFT root needs a C¹ massive-vector completion (vR19-11:25). It encodes the SM mass sums to ~1e-98 (= P0's tuning, counted once) | `rR19-11:231-235` |
| P168 | **Mass-blind gravity block** (P-R19-11b; contains P-R19-21b, counted once) | `AX:187` | [worker] ~14–17 extra conditions, a suggestion only (vR19-11:27). A tuning, unstable at higher loops (suggested) | `rR19-11:236-242`; `rR19-21:243` |
| P169 | **Twisted-mass Dirac edge** (P-R19-11c) | `AX:187`; `AX:47` (Clifford direction) | [ref] Dirac rows even in m, exact in the displayed representation. The speed residuals become ~1e-35, but the conditional shear stays ~1.4e62 above the 100 Hz bound (vR19-11:27) | `rR19-11:243-250` |
| P170 | **Photon-to-neutral row** (P-R19-12a; variant P-R19-12b, a charged Higgs component) | None (a tuning) | [ref] On one law the photon shift must be removed absolutely: κ_γ ≈ −5.3e-4, or the route-B Σ = 0 equality (vR19-12:5,17) | `rR19-12:308-321` |
| P171 | **Entangled-birth radius** (P-r1913a) | `AX:37-41`; `AX:57-58` | [ref, bounded: NN free scalar, plane insertion] R > 256a for every deterministic CPTP slab operation. 1.7e23 a is an estimate (vR19-13:15,17) | `rR19-13:188-192` |
| P172 | **(S_ad): the adiabatic lowest state weighs nothing** (P-r1914a; local form P-r1917a, counted once) | `AX:186-187`; `AX:116-123` | [ref] Not a checked global homogeneous completion (vR19-14:6). Conditionally local for planar NN-scalar cold dust (vR19-17:3-5) | `rR19-14:168-171`; `rR19-17:180-183` |
| P173 | **Frame number s** (P-r1914b), the alternative to P172 | None (a tuning to 1e-21–1e-38) | [ref, arithmetic] The lag coefficient reproduces (vR19-14:8) | `rR19-14:172` |
| P174 | **No lattice-native scale** (P-r1914c): G and masses supplied in metric units; ℓ/ℓ_P drifts | `AX:189-190` | [ref] The drift is 4.86e36 at 10 MeV reheating, not ≥ 1e50 (vR19-14:7) | `rR19-14:173-179` |
| P175 | **Lattice-frame law, W or A** (P-r1917c; sharpens P-r1914d, counted once) | `AX:116-123`; `AX:185-186` | [ref] "A newly priced W/A completion" (vR19-17:5) | `rR19-17:185-189`; `rR19-14:180` |
| P176 | **H-cov: the lattice law on an arbitrary embedding** (P-r1917b) | `AX:57-61`; `AX:187` | [worker] Law data. The full order-2/T₂g sector is uncomputed (vR19-17:6) | `rR19-17:184` |
| P177 | **(S\*): the lowest state in any uniform static background does not gravitate** (P-R19-15a) | `AX:187`; `AX:94` (counted once with (S)) | [ref] **STRUCTURAL-ZERO by construction; tautological as a mechanism** (vR19-15:14,18). Pays both shear rows for the lowest state | `rR19-15:298-303` |
| P178 | **(S\*\*): the whole linear response does not gravitate** (P-R19-15b) | `AX:187` | [worker, suggested] A non-local (retarded) subtraction | `rR19-15:304` |
| P179 | **(S\*\*₀), and its all-orders form (Σ)**: the lowest state gravitates only through its Lorentz-invariant two-derivative form with Λ = 0 (P-R19-19a; contains P177 and P92) | `AX:187`; `AX:94`; `AX:116-123` | [ref] Removes all six lowest-state cone rows wherever the Taylor jet exists. TAUTOLOGY-OR-CONFLICT, tautology branch (vR19-19:9,15). **(Σ) imposes 33 physical conditions plus a Z convention, and predicts nothing new for today's vacuum** (vR19-20:37,74). **By R19-24's Lemma E its linear part is a local quadratic graviton counterterm** (vR19-24:27) | `rR19-19:281-284`; `rR19-20:101-112` |
| P180 | **Z rule** (P-R19-19b), optional | `AX:189-190` | [worker] Changes only the induced G | `rR19-19:285` |
| P181 | **L1-H: friction on the homogeneous mode** (P-r1918b), the alternative to P162 | As P162, plus P154 | [ref] Not derived: valid only if the constant-pressure L1 law is separately stipulated (vR19-18:6) | `rR19-18:259` |
| P182 | **(S_loc): the LV strain response, re-evaluated at the actual state's local mean fields, does not gravitate** (P-R19-21a) | `AX:187`; `AX:94` (state-dependent) | [ref] Shown only at O(λ) in one NN scalar model. The gauge/Yukawa thermal terms, the cone rows, the all-orders UV/IR split and the hot-frame dynamics are unresolved. **OPEN** (vR19-21:3,28-30,42) | `rR19-21:239-242` |
| P183 | **Block site algebra** (P-r19-22a): M_{(2S+1)^6}(C) per cell, or blocking ~6 log₂(2S+1) sites | `AX:47`, or `AX:37` + `AX:57` | [ref] Insufficient alone: the literal HP truncation destroys the constraints (Lemma J; vR19-22:7) | `rR19-22:253` |
| P184 | **Unbuilt protection mechanism** (P-r19-22b) | None named | [worker] The conditional ~30–2000 qubits per cell rests on it | `rR19-22:254` |
| P185 | **Metastable graviton sector** (P-r19-22c) | `AX:77-83` (state selection) | [worker] A lifetime-limited graviton. Open per vR19-22:17 | `rR19-22:255` |
| P186 | **A₁ completion of face1** (P-R19-23a): stated seagulls for h₀₀, h₀ₙ, h_nn | `AX:187` | [ref] Required: face1 enters through the A₁ Schur complement (vR19-23:26-38) | `rR19-23:241` |
| P187 | **π⁰ health** (P-R19-23b) | None (sign conditions) | [ref] π⁰ propagation for the actual law is OPEN; no new wall (vR19-23:70) | `rR19-23:242` |
| P188 | **D1∞: every law-level field's lowest-state dressing contributes only its Lorentz-invariant form through O(p²), at all orders** (P-R19-24a; = P73 restated as a clause) | `AX:57`; `AX:114-130`; `AX:94` | [ref] **A number-free DYNAMIC-CLAUSE by construction on the campaign's literal convention. Under a codimension count: P73's 4 per class, re-set each order** (vR19-24:37,39,43). The bare e-class law is superluminal, v_max ≥ 1.003 [worker] | `rR19-24:316-320` |
| P189 | **(Σ_γ): the photon's source analogue of (Σ)** (P-R19-24b) | `AX:187` | [ref] At linear order it is the photon kinetic counterterm, under the same bookkeeping choice (vR19-24:39). Pays only the photon row | `rR19-24:321` |
| P190 | **Per-site Higgs-sector counterterms with fixed lattice-unit coefficients, and log running on the line of constant physics, on V1** (P-R19-27a) | `AX:57-58` (the rule fixed as a functional of the local spacing); `AX:189-190` (counted once with P174) | [worker; referee running] **0 new numbers.** The counterterm values are the Higgs-sector tuning any arena needs, counted once with R19-20's missing matter-sector tuning (`rR19-20:231`). Within 𝒱_ct it cancels the state-dependent vacuum enthalpy to O(φ⁵ℓ) (Theorem R), with no lattice force and no signalling. Isotropic only: the shear channels are untouched (`TESTS.md:8492-8499`) | `rR19-27:162-170` |
| P191 | **Local re-placement of VW's off-diagonal photon stress to R9-9's plaquette centre** (P-R19-26a): a 4-point average F(q) = (9cos(q/2) − cos(3q/2))/8, with F(0) = 1 and F″(0) = 0 | `AX:187` (law data; joins R19-9's r, glue profile, scattering kernel, I) | [worker; unrefereed] Zero numbers; no row depends on the member chosen. Locality with R9-9's placement forces some such re-placement. Makes the exact photon completion smooth and quasi-local across q = ±π | `SP/R19-26/R19-26_report.md:233-240` |

**Named gaps, not prices.**
- P-R19-19c: the nonlinear O(h²∂²) extension of (Σ), and a non-lowest-state prescription (vR19-19:15). "Exact Bianchi completion" does not close.
- P-R18-13c: corrected to class-scoped (vR19-5:11); not a price.
- The QED two-loop coefficients A_s, B_s, C_s (vR19-24:15).
- A physical sink action for E2 (vR19-8:5).
- A smooth photon completion across the wrap cut (vR19-16:7). [worker, R19-26] Claimed by the local re-placement P191; unrefereed.

**Count once.**
- **(Σ) ⊃ P177 ⊃ P92.** P179 (Σ) on V1 is P172 at order 0 [worker; (Σ) ⇒ (S_ad) is not checked, vR19-20:10].
- **P157 = P145 + P-r193a.**
- **P73 = P188 under a codimension count.**
- **Lemma E's consistency demand** (R19-24, referee-confirmed at equation level, vR19-24:35). P179 and P188 are the same inverse-kernel move in different sectors. Count both as clauses, or both as conditions (33 and 4 per class respectively). Not one of each.
- P162 = P-r1918a. P175 ⊃ P-r1914d. P168 ⊃ P-R19-21b. P167 = P0's ~1e-98 tuning.
- P191 is counted once with R19-9's photon law data (P160).
- P190's counterterm values are counted once with the Higgs-sector tuning (`rR19-20:231`); its scale clause is counted once with P174.

**Spelling hazards (use S-numbers only).**
- P-r19-1a (R19-1) vs P-r1910a (R19-10) vs P-r1913a (R19-13).
- P-r19-22a (hyphenated) vs P-r192a (R19-2).
- P-r19-7a vs P-r197…
- Uppercase P-R19-x vs lowercase P-r19x.
- "W1" means four things: the wall; W1-Ward; W1-weight; the C4 lane.
- "Lemma E" means three things: R19-19's, R19-24's and R19-27's.

## 5. Open questions (append to §6)

**C5 items still running.** [see the close addendum, 10:41Z]
- **R19-25.** Can weakly imposed (Gupta–Bleuler/BRST) constraints on spin-S or clock slots give two light-like helicity-±2 branches with positive norm and the 1/r pull (`TESTS.md:8324-8353`)? It decides whether P183–P185 can replace P-N1.
- **R19-26** (worker reading at `TESTS.md:8532-8545`; referee running). Is the photon kernel's wrap-cut jump intrinsic, or removable (`TESTS.md:8403-8418`)? [worker] PHOTON-EXACT. The jump came from VW's placement, not from R1 or a twist, and a local re-placement removes it with the rows unchanged. It suggests the same placement test for R19-5's U and UD completions.
- **R19-27** (worker reading in; referee running). Does V1 have any receiver for the vacuum enthalpy mismatch (`TESTS.md:8438-8460`)? [worker] Yes, in class 𝒱_ct: per-site, lattice-unit Higgs-sector counterterms on a line of constant physics (P190). The mismatch was an artefact of fixed physical-unit counterterms, which would make the vev drift ~2e51 per e-fold (`TESTS.md:8492-8499`). The referee must rule on "absorbs" versus "does not arise" (`rR19-27:222`).
- **R19-28** (worker running). Set B (Z⁴) with (Σ): do set B's walls survive once (Σ) handles the source (`TESTS.md:8504-8531`)? Expectation: B-STILL-WALLED, because RP and record walls are not source walls.

**Open within refereed scope.**
- The counting rule (vR19-24:35,41). It is the owner's to fix. See §0.
- (S_loc) beyond O(λ), with gauge/Yukawa thermal masses g²T² (vR19-21:20,42).
- The face1 A₁ recomputation (vR19-23:38).
- The π⁰ spectrum for the actual vacuum (vR19-23:70).
- One law for every SM mass (vR19-11:29). Twisted mass fixes the speeds, not the shear (vR19-11:27).
- A finite-site graviton beyond the literal HP truncation: modular constraints, emergent phases, weak constraints (vR19-22:17).
- E2's sink action and FRW lift (vR19-8:15). The siren test of E1 against E2 near γ's ceiling (vR19-18:9).
- A light-like branch off the RK point (vR19-1:19). [worker, R19-7] None at ED sizes.

**Suggested, not run.**
- Set B (Z⁴) with (Σ). Its charge rows are zero by symmetry, its gravity rows by stipulation. Its own walls (R2-4, R2-5, R2-1, RK2) would need re-reading (`rR19-24:75-79`, worker).

## 6. Provenance (append to §7)

| Result | Referee verdict as given | Where |
|---|---|---|
| R18-9 / R18-11 | CWC; FOUR-ROW-ZERO in the O(q) convention / CWC; OPEN | `vR18-9:1,21`; `vR18-11:1,19` |
| R18-12 / R18-13 | CWC; BOUNDED (narrowly) / CWC; ALL-ROWS-ZERO in the O(q) convention | `vR18-12:1,3`; `vR18-13:1,11` |
| R19-1 / R19-2 / R19-3 | CWC; NEITHER / NOT CONFIRMED; OPEN / CWC; J2-GAUGE-BRIDGE | `vR19-1:1,17`; `vR19-2:1,3`; `vR19-3:1,8` |
| R19-5 / R19-6 / R19-8 | CWC; OPEN / NOT CONFIRMED; OPEN / NOT CONFIRMED; OPEN | `vR19-5:1,15`; `vR19-6:1,3`; `vR19-8:1,3` |
| R19-9 / R19-10 / R19-11 | NOT CONFIRMED; OPEN / NOT CONFIRMED; OPEN / CWC; OPEN | `vR19-9:1,19`; `vR19-10:1,3`; `vR19-11:1,29` |
| R19-12 / R19-13 / R19-14 | CWC; ONE-LAW-BILL (route A) / CWC; NO-LOCAL-ESCAPE / CWC; OPEN | `vR19-12:1,19`; `vR19-13:1,15`; `vR19-14:1` |
| R19-15 / R19-16 / R19-17 | CWC; STRUCTURAL-ZERO by stipulation / NOT CONFIRMED; OPEN / CWC; conditional LOCAL-OK | `vR19-15:1,14`; `vR19-16:1,13`; `vR19-17:1,3` |
| R19-18 / R19-19 / R19-20 | NOT CONFIRMED; literal TIE-BROKEN / CWC; TAUTOLOGY-OR-CONFLICT / CWC; IRREDUCIBLE | `vR19-18:1,5`; `vR19-19:1,9`; `vR19-20:1,3` |
| R19-21 / R19-22 / R19-23 / R19-24 | NOT CONFIRMED; OPEN / CWC; OPEN / CWC; PHYSICAL (in scope) / NOT CONFIRMED; DYNAMIC-CLAUSE by construction (literal), else OPEN | `SP/ref_R19-21/REFEREE_VERDICT.md:1,3`; `vR19-22:1,17`; `SP/ref_R19-23/REFEREE_VERDICT.md:1,74`; `SP/ref_R19-24/REFEREE_VERDICT.md:1,41` |

**Suggested / not refereed** (same model family, no codex referee):
- R19-7: worker OPEN; no referee by design.
- R19-27: a worker reading (V1-RECEIVER); referee running. P190 rests on it.
- R19-26: a worker reading (PHOTON-EXACT); referee running. P191 rests on it.
- R19-25, R19-28: [pending].
- P148, P150, P156, P158, P161, P164, P168, P176, P178, P180, P184 and P185 rest on worker text only.
- The P148–P191 numbering and its count-once merges are S29's (same family).

**v7 close addendum (10:41Z).** These prices are named, not adopted:
- **P-R19-34a:** a strain-covariant critical mass. Its hazard reading is OPEN per vR19-34.
- **P-R19-35a:** the O(h²) one-point counterterm completion. It is unregistered, and λ_nn depends on it (worker, unrefereed).

R19-33's D2 bridge is a non-conserved alternative; the conserved bridge fails site RP (refereed).
