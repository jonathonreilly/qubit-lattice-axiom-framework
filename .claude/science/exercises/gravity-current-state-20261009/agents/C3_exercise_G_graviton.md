# Exercise on the wall: the graviton on the event substrate (lane G) (campaign C3; 2026-10-10)

Compressed exercise (scratchpad/c3/exercise_wall.js): 3 route lenses (Opus 5.5 max), a kill round on every route (Opus 5.5 xhigh), then a next test pre-registered and run by an Opus 5.5 max worker. Same model family throughout; no codex referee on the exercise itself.

## Routes (9)

### 0. Route 1 (rank 1): judge the graviton by what can be observed, not by the noise in the action. Re-read G-A; a misframing check was run.

- **Premise dropped:** A supplied-method premise from the middle column of G-A and G-C picture I, not an axiom. The premise: a graviton's response in one realization is the change in the total BD action of one frozen micro-order when the metric changes at fixed points, and that change must stay below the wave's kinetic action.
- **Mechanism:** Condensed-matter reading. Fixed points with a new metric is an affine deformation of a glass with no relaxation. At physical amplitude it re-draws essentially every long relation (G-A's saturation), so delta S is the difference of two nearly independent samples of the action.

PROVED (corollary of G-A's own lemmas; same-family; unrefereed). In saturation, G-A's verdict-bearing lower bound B = integral ds E(s)^2 Gamma_W(s_c/s - 1) contains no h. B is also the Last-Penrose second-chaos lower bound on Var(S_0): the same inequality applied to the flat functional, with the same containment restriction. So every FAIL ratio holds with no wave present: 2.8e81 for local BD, and 3e2 to 1.3e3 for BD smeared at 1e-19 m. They measure the sampling noise of the flat BD action over a wavelength cell.

CHECKED (G-A's code, fixed N, independent flat sprinklings):
- Var(S_BD) grows like T^(6.7 +- 0.8) from T = 10 to 13. Extensive would be T^4; G-A's chaos bound has the form L^6.
- At the largest TT amplitude, the crackle variance is 0.92 +- 0.24 (T = 10) and 0.70 +- 0.26 (T = 13) of the re-sampling variance.
- No setting showed crackle variance clearly above the re-sampling variance (the largest ratio was 1.37 +- 0.36).

READING. Comparing the total energies of two microstates of a heat bath, which differ by far more than one phonon's energy, says nothing about whether the phonon is sharp. On this reading:
- Smoothness belongs to what can be observed: propagators and readouts on one realized order. E1' and G-B pass this at the linearized level.
- Masslessness belongs to the law (G-C Theorem A) and to whatever dynamics produces the order.
- **Must believe:** (a) No physical rule weights single micro-orders by e^{iS_BD}. Growth probabilities do not depend on S. If something does, the sampling noise enters the effective action and Route 2 applies.
(b) A gravitational wave's physical content is its propagation and readout on a realized order.
(c) A per-realization TT mass that depends on an arbitrary coupling between two ensembles (fixed points vs co-moving; G-C R5) is not physical.
(d) As with the hydrodynamic modes of a noisy fluid, masslessness can hold at the level of the law, while realized observables only need to concentrate around it (self-averaging).
- **First test:** RUN, pre-registered (cm_lens/PREREG.md, stamped 02:06:19Z and 02:07:27Z).
- S1 (T = 10, 60 realizations) and S1b (T = 13, 30 realizations). Under both fixed readings the specific quantitative models were CONTRADICTED:
  - S1: R/f = 2.15 and 2.39, above the 1.6 limit. The variance saturates before the link-change fraction f does.
  - S1b: R(cs 4.0) = 0.30 +- 0.11, below 0.5. Reading: the needle-shaped strained region confounds the comparator.
- So the physical-scale claim rests on the proved bound identity, not on S1.

NEXT DECISIVE TEST (the question that replaces G-A's): the per-realization, matter-induced retarded TT self-energy on a 4D sprinkling, coarse-grained along a source-to-detector path. This is the B referee's ranked test 1.
- PASS: by a controlled law, the per-realization k -> 0 part is kinetic-type (vanishes like k^2), with noise below GW dispersion and dephasing bounds over 1 Gpc.
- FAIL: a mass-type random part with S(0) > 0 survives coarse-graining above the m_g bound.
- A cheaper companion: strain readout from the order itself. Sprinkle the Rosen metric, take longest-chain proper times between mirror events, and control them with Talagrand's Var L <= E L.
- **Cost:** S1, S1b and S1c are done (about 15 minutes of compute). The self-energy test needs 2–3 days with a referee. The chain readout needs about half a day.

### 1. Route 2 (rank 2): liquid, not glass. Leave the fine pattern of events unrecorded, so geometry stays a possibility.

- **Premise dropped:** The reading of Record in which every event and all its relations are locked (a frozen, quenched glass). This is named here only as a price: 'which events neighbour which is a possibility, not a record'. Only sparse matter records lock (B2 candidate C). It also requires a dynamics: a sum over orders.
- **Mechanism:** COMPARATOR (from memory): superfluid He-4 against a glass. Quantum zero-point motion keeps the Stückelberg positions unfrozen, so the medium has no static shear modulus.

On events, G-C Theorem A gives an exact Ward identity for the law and for every covariant sum, which forbids any local analytic TT mass.

The catch, from Route 1's identity. The sum's effective action carries the action's sampling noise: Gamma ~ E S + (i/2) Var S + ...
- Var S_BD grows faster than volume: L^6 from G-A's chaos bound, T^(6.7 +- 0.8) checked here.
- So it is a non-local functional: two-point, concentrated near the light cone, and diffeomorphism-invariant in law, of the form V2[g] = rho^2 ∫∫ E(tau_g^2(x,y))^2.
- Theorem A plus Lorentz covariance still allows a TT kernel a(k^2)P^2 with a(0) ≠ 0 once locality fails (G-C R3, 'without locality'). That would be a non-local imaginary TT mass, i.e. damping, of the 'R box^-2 R' kind.

So the variance term decides the route.
- **Must believe:** - A 4D sum over orders has a manifold-like phase (unknown: Kleitman–Rothschild orders dominate the entropy).
- The variance term is harmless at long wavelengths: a_var(k^2) -> 0 at least like k^2. Otherwise the action must be replaced by one whose variance grows only like the volume.
- Sparse matter records do not quench the geometry within one graviton transit (B referee item 7).
- The price on the Record reading is acceptable to the owner.
- **First test:** Compute the TT kernel of the second-chaos variance functional V2[g] = rho^2 ∫∫ E(tau_g^2(x,y))^2 dvol_g dvol_g for a TT plane wave of wavevector k, in a box of size L -> infinity, and extract a_var(k^2) as k -> 0.
- Use G-A's exact kernel tables (E_bd.npy, E_link.npy) and the exact smeared map E_eps(s) = eps E_1(s sqrt(eps)).
- PASS: a_var(k^2)/k^2 stays finite as L -> infinity. The variance then only renormalizes 1/G by an imaginary amount, and masslessness is kept.
- FAIL: a_var(0) ≠ 0, or it diverges with L (a non-local imaginary TT mass in the sum).
- Pre-register both readings before computing. Check first that V2 is invariant under a constant det-1 strain, as Theorem A requires.
- **Cost:** 1–2 days: an analytic reduction to hyperboloid integrals plus numerics with the existing kernel tables, then a codex referee. The question of a 4D manifold-like phase stays open-ended and is not part of this test.

### 2. Route 3 (rank 3, likely blocked-equivalent): a spin-ice or glass-phonon style graviton, with an exact constraint in every realization carried by proper-time data on relations.

- **Premise dropped:** G-C's H2: that the gravitational action is a function of the causal order, with marks on points. This route adds continuous proper-time (length) data on relations, i.e. a time metric on links. The axioms list a time metric as outside content, so this is a price.
- **Mechanism:** COMPARATOR (from memory):
- Phonons in a glass stay massless in every sample, because the whole sample can be translated.
- Spin-ice photons stay gapless under random bond strengths, because the ice-rule Gauss law holds on any graph.
- Disorder then only randomizes stiffnesses. That is kinetic-type noise, irrelevant by B1's power counting.

Event analog (PROVED, standard). For any 6 events in flat Minkowski space the Cayley–Menger determinant of their 15 squared intervals vanishes, because the Gram matrix of 5 vectors in 4D has rank at most 4. For a 6-chain all 15 intervals are timelike proper times.

Therefore:
- An action built from these determinants is zero on every flat configuration of every realization.
- Its Hessian at eta exactly annihilates every vertex displacement and the constant strain, realization by realization. That is a linearized diffeomorphism identity in each realization.
- G-C's Lemma B does not cover it, because it uses lengths, not order (G-C R10: 'Regge escapes'; the G-C checker's item 2).
- It is the event analog of Regge's exact vacuum gauge modes (W2).
- **Must believe:** (a) A signed sum of Cayley–Menger terms over chains has an Einstein–Hilbert mean (linear in R), not only an R^2 or Weyl^2 mean.
(b) The infinitely many non-metric link-length modes at each event are gapped or auxiliary.
(c) Matter can couple without breaking the identity in each realization. Prior art says it generically breaks it:
  - W1: matter on fixed combinatorics gives a cutoff-scale stiffness;
  - F1a: re-chosen neighbours leave white per-site TT noise of about 0.035–0.13.
  So the terminal obligation is blocked-equivalent to an exact per-realization matter stress (the K3a/F6 family), unless matter is itself blind to flat-space configuration details, or arises as defects of the constraint with charge equal to energy (R1's 'defects' row, argued to fail).
(d) The dispersion is linear. Compact Gauss-law tensor models give k^3 (landed note of 2026-09-14). The event substrate's unbounded link valency may evade that note's summable-moment hypothesis; this is suggested only.
- **First test:** Test the blocker first. On a 4D sprinkling with links fixed, take a scalar matter vacuum that depends smoothly on link proper times, and compute the per-realization Hessian of its vacuum energy along a TT vertex-displacement field.
- PASS only if it vanishes in each realization (matter blind to flat-space configuration details).
- Expected FAIL, by analogy with F1a and W1. A FAIL retires the route as blocked-equivalent.
- Only on a PASS: build the signed chain action and measure its mean TT kernel (k^2 against k^4) and its per-realization gauge nullity.
- **Cost:** The matter Hessian takes half a day to a day. The chain-action kernel takes 1–2 days. Expected outcome: retirement into the K3a/F6 blocked family.

### 3. Route 1: the graviton lives in the law, not in one history's action (a misframing; first test run)

- **Premise dropped:** That masslessness and smoothness must hold history by history for an action of one frozen event set. G-A's 'pin the wave on one event set' and G-C's per-realization identity both assume this, i.e. that one history's BD action is the object that must respond smoothly to the wave.
- **Mechanism:** PROVED (a corollary of G-A's own Last–Penrose inequality and its controlled saturation lemma; G-A was adversarially checked, codex referee pending). At physical amplitude e_h is e^-24-small wherever e_0 is supported. So G-A's bound rho^2∫∫(e_h−e_0)^2 equals rho^2∫∫_{y<x} e_0^2, which is also the second-chaos lower bound on Var S of the FLAT cell alone. Hence sd(S_BD of a flat wavelength cell) >= 2.1e120 hbar with no wave present. The 'crackle' is the action's own intrinsic noise and does not depend on h. Any two histories that differ in their long links differ by it: the same points with the order recomputed, a fresh sprinkling, or a grown history. Only co-moving (isometry) coupling avoids it, and a k≠0 wave has no isometry.
CHECKED (QG1, pre-registered 02:05:08Z, using G-A's own runs). The correlation between the flat-order and wave-order interval actions on the same points, after removing the dependence on N, falls monotonically with h: T=10: 0.94, 0.51, 0.38, then −0.02 [−0.21, +0.20] at h=1. T=16: 0.71, 0.67, then −0.34 [−0.62, −0.05] at h=1. Var dX/(Var X0 + Var Xh) at h=1 is 1.02 and 1.32, and sd dX is about √2·sd X0. The pre-registered reading is met: SUPPORTS.
SUGGESTED. Scaling from G-A's Γ_W ∝ L^6: the local BD noise per cell is ≈ 9e-3 (L/l)^3 hbar, against a weak-field EH signal of ≈ 0.2 h^2 (L/l_P)^2. So once histories differ in their long links, one history's local action cannot tell weak geometries apart at any macroscopic scale. This is the known reason causal-set work introduced a non-locality scale (Sorkin gr-qc/0703099, M). Masslessness then rests on law-level covariance: G-C Theorem A (exact) makes every law-level functional Diff-invariant (WTDiff for coordinate sprinkling), so no local TT mass. Smoothness rests on relational observables, which concentrate (E1′-b and G-B: counting noise √(3/N̄), about 1e-28 at 1 Gpc), not on the action.
- **Must believe:** (1) READING: no physical process reads the action of one history. Physics reads relational, coarse data: link-propagated fields and interval counts. Under the records-as-events reading the order is record content, so the action is 'readable' in principle; this is therefore a reading, not an axiom consequence. (2) A dynamics exists whose law is label-invariant and covariant and which produces manifold-like histories near Einstein solutions. This is Lane F's formation wall: Markovian label-invariant growth is a bounded FAIL, referee pending. (3) For recorded (classical) histories, an unproved theorem: the coarse-grained drift of a covariant classical law inherits Diff covariance, so it has no local TT mass. This is the dynamical analogue of Theorem A, which covers only background sprinkling laws (G-C checker's correction). (4) The E1/E1′ axiom conflicts are unchanged: Lattice replaced, order supplied (A36), records-as-events vs one record per site.
- **First test:** RUN: QG1 (above). Script: .../exercise_G_graviton_on_events/qg_lens/qg1_intrinsic_noise.py. Output: qg1_intrinsic_noise.out. Pre-registration: PREREG_QG1.md.
NEXT DECISIVE TEST (pre-register before running). On ONE frozen 4D sprinkling, send a link-only massless probe (Johnston aL) along x across an exact Rosen + wave region, using ga_core.tau2; the observer is at distance D.
- PASS: the per-realization received amplitude or arrival equals the g_h mean (GR shift (h/2)∫cos along the path) plus a residual with Var ≤ (3+o(1))·Diag in each world. Var(Δ) ≤ Var_0 + Var_h, with no excess beyond two counting draws, for h = 1e-4…1 at s/l = 6–24. Then the matched S/N h·√(N̄/F) is translated to LIGO-arm proxies.
- FAIL: an h-dependent excess that grows with region volume, i.e. action-like crackle leaking into propagated observables.
- **Cost:** QG1: done in under 1 minute, reusing G-A data. Probe test: 2–4 h, reusing ga_core.tau2 and the E1′ needle sampler. Covariance theorem for classical laws: a 1–2 day proof attempt. KILL VERDICT (self, same family): WOUNDED. The reframe is checked and proved-as-corollary. For 'massless', the terminal obligation (a covariant law with manifold-like Einstein histories) risks being blocked-equivalent to the formation wall.

### 4. Route 2: a coherent sum over orders, with its noise cumulant controlled

- **Premise dropped:** That the micro-order is recorded, i.e. that every Planck-density event is a permanent, readable record. This is a price on the Record reading (B2's candidate C: 'which events neighbour which is a possibility, not a record'), named only as a price.
- **Mechanism:** Take Γ[g] = −i log Σ_{C~g} μ(C) e^{iS(C)}, with 'C~g' defined from the isometry class of g (e.g. faithfully embeddable at density ρ). G-C Theorem A (exact, for law-level functionals) makes every cumulant Diff-invariant, so no local analytic TT mass appears at any order. The background-free version is an obligation.
NEW POINT (suggested, from the Route-1 corollary). The per-history variance of the local BD action is at least (2.1e120)^2 hbar^2 per wavelength cell. So Γ ≈ S̄[g] + (i/2)σ²[g] + … is dominated by the variance functional, not by the EH mean. Masslessness survives, because σ² is Diff-invariant too. Whether a propagating graviton survives depends on whether σ²[g] depends on curvature:
- if σ²[g] is curvature-blind (a pure volume term, an imaginary Λ), Re Γ (BD's EH mean) governs, and the graviton is massless and propagating;
- otherwise the kinetic term is noise-dominated (a complex G, i.e. damping).
- **Must believe:** (1) A 4D manifold-like phase exists in the sum. This is unknown: Kleitman–Rothschild orders dominate the entropy, and BD suppression is only partial (Loomis–Carlip 1709.00064, M). (2) σ²[g] is curvature-blind, or smearing at l_k ≳ 3e-19 m (G-A's equality point) makes it subdominant. G-A only lower-bounds the noise, so this window is open. (3) Γ is local and analytic at the graviton scale. (4) The Record price is acceptable, with matter records sparse and coarse (B referee item 16).
- **First test:** Test whether the per-history variance depends on curvature. De Sitter is conformally flat, so its order is the flat order of points sprinkled with density ρΩ^4 in conformal coordinates; G-A's mode-0 code applies directly. Take equal-proper-volume 4D diamonds in flat space and in de Sitter / anti-de Sitter with curvature radius 1–5 diamond heights. Compute E S and Var S, after removing the dependence on N, for local BD and for smeared BD (ε = 0.1–0.5), over 50–200 realizations.
- PASS: Var S[g] − Var S[η] is consistent with 0 or a pure volume term, while E S[g] − E S[η] shows the BD/EH curvature response.
- FAIL: the variance carries a curvature term at least 10× the mean's EH response at every ε tested.
2D cannot test this, because EH is topological in 2D and there is no TT mode. Caveat: boundary terms dominate small diamonds (G-A), so the curvature radius must reach the diamond scale.
- **Cost:** Variance test: 3–6 h (cheap because de Sitter's order is the flat order). The 4D phase question: weeks to months, an open research problem. KILL VERDICT (self): WOUNDED, on the unknown 4D phase and the Record price. The variance sub-question is new (not in the packet), cheap and decisive for whether a coherent sum can carry the graviton at all with the local BD action.

### 5. Route 3: Einstein's equation as the event substrate's equation of state (Jacobson on events)

- **Premise dropped:** That the graviton must be a protected mode of an action, whether per history or summed. Instead, the coarse-grained Einstein equation is a local thermodynamic identity, dQ = T dS for every local causal horizon, with S ∝ the count of horizon-crossing links.
- **Mechanism:** COMPARATOR (Jacobson PRL 75, 1260 (1995), gr-qc/9504004, M). Assume entropy ∝ area with one universal coefficient for every local Rindler horizon through every event, plus Unruh temperature and Raychaudhuri focusing. Then G_μν + Λ g_μν = 8πG T_μν follows, with Λ an integration constant. That is unimodular gravity, matching the packet's 'count = volume'.
SUGGESTED. The result is Diff-covariant by construction: no mass term, and nonlinear GR included. Its per-history content is a counting identity with noise ~(A/l^2)^{-1/2}. On a Poisson sprinkling the link density across any boosted local horizon is universal in law, which is exact by Lorentz invariance in law. On the fixed grid it is not: the candidate pack records 'Jacobson dead on the grid, coefficient varies 16–18% with cut direction' (DECISION_MATRIX.md:71, TEST_LOG.md:541; source run not traced here). That would be one picture explaining why the grid is stiff and the events are not.
- **Must believe:** (1) Horizon entropy is a horizon-link or 'horizon-molecule' count with a finite, universal coefficient that concentrates in each realization. Comparators: Dou–Sorkin gr-qc/0302009; Barton et al. 1909.08620 for expected counts in flat space; both M, unverified. B2_report.md:243 already cites Dou–Sorkin. (2) Local equilibrium: link-propagated matter near any local horizon sees the Unruh temperature. This is unproved on causal sets. (3) The formation process (records forming) is in local equilibrium. This is a supplier-content dynamics assumption. (4) A classical equation of state is enough for 'massless and smooth'. It gives no graviton quantum, and non-equilibrium corrections such as horizon shear viscosity can appear (Eling–Guedens–Jacobson gr-qc/0602001, M).
- **First test:** Count horizon links on 3+1 Poisson sprinklings, using Dou–Sorkin/Barton-type molecules: links x <* y with x maximal in J−(Σ) outside a null plane H, and y inside H in J+(Σ).
- PASS: the mean count per unit cross-section area is finite and the same within errors for ≥ 3 tilts of Σ and two curved Σ, and the per-realization relative sd scales as (A/l^2)^{-1/2}. The flat, boosted case is exact in law; the content is finiteness, independence of Σ's shape, and concentration.
- FAIL: the count diverges with the region size, or depends on Σ's tilt or shape beyond errors.
Run the same count on Z^3 × time slices for the grid contrast.
Second test (days): under a Rosen-wave shear of the null congruence, does the count track the cross-section area to second order (Raychaudhuri's σ² term)?
- **Cost:** First test: 4–8 h. The full equation-of-state chain (the Unruh step for link matter, second-order area tracking): several days. No axiom price beyond the event substrate's existing conflicts, plus a formation-equilibrium assumption. KILL VERDICT (self): WOUNDED. It gives a classical equation, not a quantum graviton. Local equilibrium is assumed, and the Σ-dependence of link counts is a known subtlety. It is not vacuous, because it already discriminates the grid (dead) from events (untested).

### 6. R1. Read the wave from one realization instead of deforming one (the 'smooth' half)

- **Premise dropped:** That smoothness means per-realization differentiability of one fixed, coordinate-labelled event set whose order an external metric bends: G-A's fixed-point coupling, i.e. Stückelberg unitary gauge (G-C R0). Under B2's candidate B ('the law never refers to event labels or positions'; records are permanent and form with their relations), a passing wave never re-draws relations that already exist. So G-A's same-events-new-order comparison is a counterfactual, not a physical process (reading).
- **Mechanism:** Each realization is a faithful sprinkling of the wave spacetime: det g = -1 in Rosen form, so a coordinate sprinkling is exact. A detector reads the wave from that one order. (a) Causal-past counts: #{y in A : y precedes_g O} for a fixed apparatus event O is exactly Poisson with mean rho*Vol_g(A ∩ J-(O)), by Poisson restriction (proved, trivial). The mean is analytic in h, and the noise does not depend on h: no crackle. (b) Link-propagated light signals: the mean is exact by Mecke, and the noise is at most (3 + C s/D) times counting noise by E1'-b/G-B (proved on flat backgrounds; refereed for the scalar). Arithmetic (suggested): a 1 m source box at 4 km read through its causal-past count has SNR ~ delta*a ~ 1e51 at h = 1e-21.
- **Must believe:** An observed gravitational wave is a readout taken on one realized order, not a comparison of two orders on the same events. E1'-b's needle-overlap geometry survives curvature radius >> link shell (about 3e16 m against 1e-104 s shell time at LIGO). Apparatus worldlines (mirrors, sources) can be supplied test worldlines; massive matter is lane M and still open.
- **First test:** Pre-register first. Reuse G-A's ga_core.py (exact Rosen causal relation) and the E1' dependence-region sampler. T about 10-16, h in {0, 0.03, 0.1, 0.3}, at least 200 independent single realizations per h, a Palm observer, and two compact sources at equal coordinate distance along the stretch and squeeze axes. Readout: the difference of the link-sums of the two arms (and of the arrival centroids). PASS: the mean is within 3 se of Mecke quadrature and linear in h at small h; at every h the per-realization sd is within 10% of its h = 0 value; Fano <= 3 + C s/D. FAIL: the sd grows with h (crackle leaks into a readout) or the Fano factor exceeds the bound.
- **Cost:** 2-4 h for one Opus worker plus a codex referee; under 10 min of CPU per run. If it passes, G-A's FAIL leaves the graviton wall: 'smooth' is closed for linearized waves at the readout level.

### 7. R2. Masslessness is a property of the law: test the locality premise it rests on

- **Premise dropped:** That masslessness must be enforced per realization (H3 in G-C). The axioms already split law from realization: the law supplies the odds and the realized state supplies the pick (Admissibility reading note 1; realized-state primitive: values that vary across realizations are registered data). Masslessness is a law-level property; the per-realization spread must be bounded, not forbidden by an identity.
- **Mechanism:** G-C Theorem A (exact; same-family; codex referee pending): every functional of a label-free law is Diff-invariant. That covers the mean, all cumulants, E e^{iS} and the induced Gamma = -i log E e^{iS}. So Gamma has no local analytic TT mass; the only loophole is a non-analytic transverse mass a(0) != 0, which needs non-locality. New threat (checked arithmetic, from G-A's own kernel at h = 0): the per-realization variance of every BD-type action on a region of size L grows like L^6 = N^{3/2} at every smearing scale, with prefactor eps^{5/2}. The flat sd over one LIGO wavelength cell is >= 2.1e120 hbar for local BD. It falls below 1 hbar only if l_k >~ 1.9e-11 m. In a quantum sum this cumulant enters Gamma as (i/2) Var_g S, which is superextensive, so the locality premise (H4) is not automatic.
- **Must believe:** The superextensive (L^6) part of the action's cumulants is g-independent, or pure volume or boundary (Lambda-type), so the TT kernel of Gamma stays analytic as k -> 0. A label-free 4D law with a manifold-like phase exists: lane F gives a bounded FAIL only for exchangeable, frontier-only and classical DGC+Bell growth, and leaves other label-free rules open.
- **First test:** Mecke/second-chaos quadrature of the O(h^2) TT response of the leading cumulant integral, rho^2 ∫∫_{y<x} e_g(y,x)^2 (G-A's kernel E(s) with the exact Rosen tau^2), for a TT wave at k != 0. Vary the region size L and the wavenumber k, with the region transported geometrically to avoid G-A's coordinate-boundary artefacts. Exact control: a constant det-1 strain must give zero. PASS: the TT response per L^4 tends to c*k^2 + O(k^4), local and with no mass, and the L^6 part does not depend on h. FAIL: the TT response scales as L^6, or stays finite as k -> 0 at fixed kL >> 1 (a non-local transverse mass).
- **Cost:** 1-2 days for one worker plus a referee; quadrature in 4D, mostly reuse of G-A's kernel code. This decides whether protection in law is real for BD-type dynamics; it is the only protection the frozen-record picture admits.

### 8. R3. Write the exact price: on events the graviton has no separate wall

- **Premise dropped:** That the graviton has its own wall on the event substrate, separate from formation (lane F) and from the locality of the law-level effective action.
- **Mechanism:** Assemble the following into a one-page refereed statement. (a) Proved corollary: at physical h, G-A's controlled crackle bound is the same integral as the second-chaos (Last-Penrose) lower bound on Var S for a single flat sprinkling of the same cell. The flat kernel E(s) and flat pair count Gamma_W enter, and h does not; by Minkowski, sd(dS) <= sd(S_h) + sd(S_0). So G-A's FAIL inequality is met by flat space with no wave, as well as by pure gauge; it measures the action's own non-self-averaging under the fixed-point coupling. Checked: at accessible sizes the BD crackle at h = 1 equals two independent draws, with corr(F_h, F_0) = -0.01 at T = 10 (30 realizations) and -0.33 at T = 16 (8 realizations), and Var(dF)/(Var F_h + Var F_0) = 1.01 and 1.29. (b) G-C R0/R5: per-realization comparisons depend on the coupling; co-moving points give zero for the zero mode, fixed points decorrelate. (c) Lemma B/Theorem C: a per-realization identity exists only for flat-blind functionals, which have no EH term. (d) Theorem A. (e) G-B/E1'-b readout bounds. (f) Lane F's bounded FAIL.
- **Must believe:** Picture II (B2 candidate B) is the intended reading of records-as-events: the realized order is registered data, the law never sees labels, and a per-realization action is never used as a classical action for a field.
- **First test:** A codex sol referee of the corollary in (a). Check that G-A's saturated bound uses only e_0, the flat kernel, and that Var F_0 >= rho^2 ∫∫_{y<_0 x} e_0^2 holds with the same containment restriction. Also referee the reduction 'graviton wall on events = F + R2 + R1'. PASS: confirmed, and G-A is re-recorded as 'FAIL of the fixed-coupling per-realization action criterion; flat space fails the same criterion'. FAIL: a load-bearing h-dependence is found in G-A's saturated bound.
- **Cost:** About half a day: about 1 h of drafting plus the referee. It changes the owner's decision list: no graviton-specific price remains on events for linearized waves. Effort moves to formation (F) and R2. In picture I (labelled events plus an external metric) the price is the Rubakov-Tinyakov/Dubovsky label mass in spacetime form, and per-realization protection with an EH mean is impossible.

## Kill round

| # | Route | Killed | Reason / survives as |
|---|---|---|---|
| 0 | Route 1 (rank 1): judge the graviton by what can be observed, not by the noise i | True | Verdict: KILLED as a route around the wall (blocked-equivalent). Its proved core survives only as a scope correction to G-A. Checker: Claude Opus 5.5, same family as the route's author, so this is not an independent referee. Files read: the full axioms memo; the exercise SKILL; SUMMARY; the G-A, G-B and G-C reports and referee verdicts; B_referee; TESTS.md lane G; cm_lens and misframing outputs. Scripts and output are in scratchpad/c3/exercise_G_graviton_on_events/kill_route1/ (kill_r1_checks.py, kill_r1_checks.out).  What holds: 1. The corollary is correct (proved, one line). G-A's saturated bound B = ∫E(s)²Γ_W contains no h. B is also the contained, flat-timelike part of the second-chaos term of Var(S_0). 2. An exact upper bound I add: B ≤ Var ΔS ≤ (sd S_h + sd S_0)². 3. Checked on the route's S1 data (T = 10): Var ΔS / (sd S_h + sd S_0)² = 0.10–0.54. From misframing/decorrelation_chec |
| 1 | Route 2 (rank 2): liquid, not glass. Leave the fine pattern of events unrecorded | True | I ran the route's own first test, with the readings written down before any numbers (PREREG_route2.md, 02:23Z). It fails on both pre-registered FAIL readings.  Who did this: Claude Opus 5.5, same family as the workers. Not refereed; a codex referee is still owed.  Prior art (step 0): - G-A: the crackle; the second-chaos bound Var >= rho^2 ∫∫(e_h - e_0)^2 with Gamma_W ∝ L^6; the kernel tables E_bd.npy and E_link.npy; the exact Rosen tau^2. - G-C: Theorem A (law-level Ward identity). R3 says that "without locality" a(0) ≠ 0 is not excluded. The referee re-scoped Theorem A to the induced effective action of a fixed background, which is exactly the object Gamma[g] = E S + (i/2) Var S tested here. - B_referee item 7 (quench is conditional). E1 (noise gain grows with the past). - Comparators from memory: Sorkin 2007 (causal-set d'Alembertian fluctuations grow, so smearing is needed), Benincasa |
| 2 | Route 3 (rank 3): a spin-ice or glass-phonon style graviton. Continuous proper-t | True | VERDICT: KILLED. The route is blocked-equivalent: its last obligation reduces to the K3a/F6/W1 family. It fails its own pre-registered first test, and it fails more strongly than the route expected.  Workers and timing: - Worker: Claude Opus 5.5, same family as the supervisor. Not refereed. - Pre-registration stamped 02:19:03Z, before any computation. - Files are under /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/exercise_G_graviton_on_events/route3_kill/. - My files there: PREREG.md, M_matter_hessian.py, M_run_T6-10.out, M_run_T12.out, M_tuned_mix.out, C_cayley_menger_tadpole.py, C_run_n300.out, C_run_n500.out. - route3_kill.py and route3_kill.out in the same folder belong to another agent (a different "Route 3", Jacobson on events). They are not part of this  |
| 3 | Route 1: the graviton lives in the law, not in one history's action (a misframin | True | KILLED as a route to a massless, smooth graviton. Its reframing survives only as a reading (see survives_as). Self-check, same family (Opus 5.5), no outside referee. None of the K1-K3 computations below was pre-registered: they are post-hoc kill checks and do not decide anything on their own.  1. ALREADY TRIED (step 0). The reframe is already on record: - The G-A codex referee says the "pure-gauge crackle is a coupling artefact" (co-moving points give dS == 0) and that G-A is "not a gauge-invariant no-go". - G-C R5: a per-realization TT mass is not an intrinsic observable. What can actually be measured is field propagation on the realized order (E1', G-B). - G-C R6/R9: Theorem A protects the law; it protects the realized world only if the micro-order is unrecorded. - The intrinsic noise of the local action is Sorkin's reason for a non-locality scale (gr-qc/0703099, cited in agents/E1_rep |
| 4 | Route 2: a coherent sum over orders, with its noise cumulant controlled. Γ[g] =  | True | VERDICT: KILLED as stated. The route claims "masslessness survives because σ² is Diff-invariant". That argument needs Γ to be local, which is its must-believe (3). Locality fails provably at the route's own second cumulant, for every action the route names.  PRIOR ART (step 0): - G-A report §(c) gives an exact Last–Penrose second-chaos bound, a containment lemma, and Γ_W ∝ L⁶. The codex referee says the bound "checks out". - G-C R3 (Theorem C): "Without locality … a non-analytic a(0) ≠ 0 (a transverse 'mass') is not excluded"; a pure k² term has the vDVZ form, which Cassini excludes. G-C R6 is Theorem A. G-C adversarial item 6 contrasts extensive noise with counting noise. - E1 report l.37: the per-element variance of the BD d'Alembertian grows like τ² in 4D and like a log in 2D. This is the same orbit-volume growth at the operator level. - SUMMARY §8: BHS (no finite-valency Lorentz-equi |
| 5 | Route 3: Einstein's equation as the event substrate's equation of state (Jacobso | True | KILL VERDICT: DEAD as a route past this wall. Formally it is blocked-equivalent: its only substrate-specific input is already proved, and its dynamical step restates the target. Kill pass by Claude Opus 5.5 (same family as the route's author, so not independent); no codex referee.  What I read: docs/MINIMAL_AXIOMS_2026-06-29.md in full, the exercise SKILL.md and packet SUMMARY.md in full. I read only parts of C3_G-A_report.md (lines 1-120), C3_G-C_report.md (R5-R7 plus a grep) and the referee headers. TESTS.md and B_referee.md were only grepped.  STEP 0, PRIOR ART (the route is largely already mapped) (a) The 09-29 gravity exercise (commit fd51a1f4c7f, PR #9363) killed route F4 (the entanglement equation of state) on Z^3. - Its kill3 check named four missing inputs: a metric to define dA, a boost-KMS (Unruh) temperature, a universal eta, and CFT or holographic matter. - I traced the '16- |
| 6 | R1. Read the wave from one realization instead of deforming one (the 'smooth' ha | True | KILLED as a route past the wall. The route fails on four counts.  1. ITS PAYOFF MISREADS G-A'S FAIL (proved, then checked). - G-A's controlled bound in the saturated regime is Var >= Int E(s)^2 Gamma_W (C3_G-A_report.md:198). It contains no h: "the bound does not depend on h" (C3_G-A_report.md:206). - That bound is exactly the Last-Penrose second-chaos lower bound (timelike, contained pairs) on Var S for ONE faithful sprinkling of the cell. Why: in Rosen form det g = -1, so G-A's S_h on fixed points has the law of S on a fresh faithful sprinkling of (W, g_h) (mapping theorem; G-C Theorem A). An elementary backup: Var(S_h - S_0) <= 2 Var S_h + 2 Var S_0. - So in R1's own picture, the order that carries the wave has an action with sd >= 2.1e120 hbar per wavelength cell:   - local BD: 2.8e81 x S_kin;   - BD smeared at 1e-19 m: >= 312 x S_kin. - Only the step function in h is a coupling arte |
| 7 | R2. Masslessness is a property of the law: test the locality premise it rests on | True | VERDICT: KILLED. The route's own pre-stated FAIL clause ("the TT response scales as L^6") is met by the leading cumulant term. Everything here is same-family (Opus 5.5) work and unrefereed.  PRIOR ART (step 0) - G-C R6, Theorem A (exact Diff invariance of every functional of the law) and R7 (zero-mode crackle is extensive, not counting noise). - G-A section (c): the second-chaos kernel E(s), the null-ray measure Gamma_W = int dx int dOmega R^2/4, and I_BD = 0.0191 L^6. - E1: BD noise gathered from the whole past, plus Sorkin 2007's non-locality estimate. - B referee item 15: protection in law, not per realization. - Main docs cite causal sets only as background (LORENTZ_BOOST notes). There is no prior computation of the TT response of Var_g S.  1. Exact scaling lemma (PROVED here, elementary). - At large L/ell the leading part of rho^2 int int E(tau_g^2)^2 is (int E^2 ds) * A[g,D]. - A[g |
| 8 | R3. Write the exact price: on events the graviton has no separate wall | True | Killed. The corollary in (a) is correct, but it shows the opposite of what the route uses it for. Kill check by Opus 5.5 at xhigh, same model family, unrefereed. Pre-registered before computing: kill_route3_price/PREREG.md.  1. Corollary (a) holds (checked; the algebra only). In saturation, G-A's bound becomes rho^2 times the integral over contained pairs y <_0 x of E(s)^2. That is one term of the Last-Penrose expansion of Var S_0 for a single flat sprinkling. h enters only through the condition hR^2 >> s_c. The misframing agent's arithmetic (misframing/flat_bound_arith.out) gives sd_flat(S_BD, wavelength cell) >= 2.13e120 hbar. The route's first test would probably PASS on this algebra.  2. That same fact defeats the route's reading of G-A. The bound is a property of the law of S on one geometry. It does not depend on how two geometries are coupled. Picture II's action-weighted sums are |

## Next test (pre-registered and run by the worker)

EXERCISE G (graviton on events), C3. Survivor ranking, the test I ran instead, and its result.

Provenance and reading:
- Written by a Claude Opus 5.5 subagent. That is the same family as the route and kill agents, so this is not an independent referee. Nothing here has been refereed.
- I read these in full: `docs/MINIMAL_AXIOMS_2026-06-29.md`, the exercise `SKILL.md`, the packet `SUMMARY.md`, and every kill-round output in scratch.
- Because of the time limit, I only searched G-A, G-B, G-C, B_referee and TESTS.md for the relevant terms.
- I edited no repository files.

**0. Prior art (step 0)**
- Main `docs/` has no Van Vleck results and no Rosen-wave interval-volume results.
- The packet has:
  - G-A report line 283, which lists as an unchecked item "the wave's curvature inside the needle".
  - TESTS.md line 282, an exact statement about kernels that depend only on the interval volume (E1).
- The kill round's V2 computation (route2_v2_tt.py) used the flat relation V = (π/24)τ⁴ inside the wave. Nothing in the packet checks that relation.

**1. Ranking of survivors: none survived, so the ranking table is empty.**
Kill evidence, all in `.../c3/exercise_G_graviton_on_events/`:

- **Route 2, all three versions (liquid; coherent sum; R2 locality): FAIL by their own pre-registered reading.**
  - `route2_v2_tt.out`: at ωL ≫ 1 the TT response of the second-cumulant functional V2 no longer depends on ω (δV2/V2 → I0(h)−1), and V2/Vol grows like L². The constant-strain control is about 1e-18.
  - `R2_phys_translation.out`: the response exceeds the EH kinetic action by 10^163 at LIGO. Making it subdominant needs a smearing scale of at least 10^-18.5 m (LIGO), rising to 10^-10.9 m (CMB tensors).
- **R3 ("no graviton-specific price"): not earned.** `kill_route3_price/k2_rosen_M.out` shows the same response carries G-A's FAIL into picture II.
- **Route 3, Cayley–Menger / spin-ice version: blocker FAIL, blocked-equivalent to the K3a/F6 family.**
  - `route3_kill/M_run_T12.out`: in each realization, the matter Hessian along a TT vertex displacement is about 5 (log det) and about 15–19 (zero-point), against a boost control of about 1e-9.
  - `M_tuned_mix.out`: after tuning the mean, the per-realization sd is still 0.11–0.18.
  - `C_run_n500.out`: there is a TT tadpole in each realization.
- **Route 3, Jacobson version: fails its own reading.** In `route3_kill.out` K1, links from one exterior point grow like R² (E/R² → 7.70), so the count diverges. K3: the shear² signal is below counting noise by a factor of about 270 per wavelength cell.
- **Route 1 / R1: the misframing corollary is checked, but the route is blocked-equivalent.**
  - Checks: `qg_lens/qg1*`, `misframing/`, and `var_R1.out` (corr(0,h) = −0.01 at T=10 and −0.33 at T=16).
  - Masslessness then needs a covariant classical growth law with Einstein histories, which is lane F's wall.
  - The flat-background readout test cannot fail, because E1′-b's proof already covers it.
  - Chain readout under Talagrand's bound needs arms of at least 3.8e7 m (`kill_route1/kill_r1_checks.out`).

With nothing to rank, I ran the cheapest test that could reverse the kills themselves. Every death except Route 3's rests on one computation that used a proxy (the flat volume relation).

**2. Test N1: pre-registration**
File: `.../top_test/PREREG_N1.md`, stamped 02:41:42Z. Run 02:42:17–02:42:39Z (22 s).

- **Setting:**
  - G-A's det-1 Rosen wave, with g⊥⁻¹ = diag(e^{−h cos ku}, e^{h cos ku}).
  - Pairs separated by U in u; τ0² = 1; h = 0.3 and 1.0; kU from 0.3 to 100; two phases.
- **Observables:**
  - (a) Closed-form needle volume (derived here, same family). V_g = (πτ⁴/8U²)∫₀^U du/√det C(u), with C = M(0,u)⁻¹/2u + M(u,U)⁻¹/2(U−u). It does not depend on the transverse offset X (by completing the square).
  - (b) A Monte Carlo interval volume that uses only `ga_core.tau2`, with at least 6e6 samples.
  - (c) R = √det M / √ν, with ν = V_g/V_flat. R is the exact factor by which the transverse integral of any kernel K(ρV) changes. The kill used √det M alone.
- **Prediction:** ν → I0(h), so R → I0(h)^{1/2}.

**3. Results against the fixed readings** (`top_test/n1_needle.out`)

- **Code check: PASS.**
  - Over 12 Monte Carlo settings the largest |z| is 2.03.
  - The X ≠ 0 checks give z = −0.21 and +0.44.
- **ν converges to I0.** At kU = 100, ν_MC is:
  - 1.0245 ± 0.0019 and 1.0203 ± 0.0019 for h = 0.3 (I0 = 1.0226);
  - 1.2625 ± 0.0030 and 1.2598 ± 0.0030 for h = 1 (I0 = 1.2661).
- **"Kill stands as computed" (ν = 1): excluded**, at at least 10.9σ for h = 0.3 and 87σ for h = 1.
- **"Kill collapses" (ν = I0², which would reopen Route 2): excluded**, at at least 11.4σ and 114σ. At kU = 100, R−1 is 100.5–100.7% of I0^{1/2}−1, far above the 10% that collapse required.
- **"Kill stands, coefficient corrected": met at kU = 100 but not at kU = 30.**
  - At kU = 100, (R−1)/(I0^{1/2}−1) is between 1.005 and 1.007 for both h. The constant-strain control goes to 0 (0.0008 and 0.023 at kU = 0.3).
  - At kU = 30 the value is 1.04–1.07, outside the 2% tolerance I fixed in advance. This is a finite-baseline end effect that shrinks by a factor of about 10 between kU = 30 and 100.
  - Strictly by the pre-registered wording, this clause is therefore INCONCLUSIVE. Both alternative readings are excluded.
- **Side observation:** the response does not rise smoothly. At kU = 3, ν falls to 0.91, and R overshoots to 2.5 times its asymptotic value.

**4. What this moves**

- **Route 2 stays dead under the exact interval volume (checked).** This holds for any action whose pair kernel depends only on the expected interval count.
  - The long-baseline TT response of the second cumulant tends to I0(h)^{1/2}−1 ≈ h²/8, not I0−1 ≈ h²/4.
  - It still does not depend on ω and still grows like L² per volume.
  - The kill's coefficient was 2.0–2.1 times too large, which moves the 10^163 figure down by about 0.3 dex.
- **New exact statement (proved for pair geometry, checked).** Over long baselines, the wave spacetime looks like flat space with transverse metric M⁻¹ and point density ρ·I0(h).
- **Not covered by N1.** G-A's four-term kernel also has cross terms involving third points. Applying the same effective-density picture to them is suggested only.
- **By-product: a possible problem for link-only readouts on curved backgrounds (suggested, not computed).**
  - Near the light cone, the mean of one-hop link propagation goes like ν^{−1/2}·Δ⁻¹ times the flat cone measure. GR's goes like Δ^{−1/2}, where Δ is the Van Vleck determinant.
  - Taking the standard plane-wave value Δ = 1/det M (not recomputed here), the link mean through the wave over long counter-propagating baselines exceeds GR by I0^{1/2}, i.e. h²/8. That is unobservable for gravitational waves.
  - With O(1) lensing, though, the mismatch would be O(1), unless the volume relation V ≈ (π/24)τ⁴Δ⁻¹ holds there.
  - This does not change G-B's or E1′'s flat-background PASS verdicts. It is the one remaining check that could fail the "smooth" half of Route 1.

**5. The price (suggested; assembled from checked parts; not refereed)**
On the event substrate, a massless and smooth graviton needs all three of:
- a classical, covariant growth law that produces Einstein histories (lane F's formation wall);
- amplitudes not weighted by e^{iS} or e^{−S} of any interval-count action (Route 2 kill plus N1);
- link-only readouts that reproduce Van Vleck focusing on curved backgrounds (open).

Per-realization protection in picture I is excluded by G-C (narrow no-go) and G-A. The axiom prices are unchanged: Lattice replaced; causal order supplied; records-as-events conflicts with one record per site; an event happening must differ from a value being locked.

**6. Next steps (at most three)**
- **(a) Revised R3 price note:** "graviton wall on events = F + curved-background readout", with route2 plus N1 as the coherent-sum exclusion. Half a day plus a codex referee.
- **(b) Link-only lensing test:** compare the one-hop link-sum mean through a thin lens or Schwarzschild background with GR's Van Vleck magnification. Half a day plus a referee. It waits on nothing.
- **(c) Route 1's terminal obligation:** waits on lane F (its referee is pending).

What not to do: re-run coherent-sum variants with other smearings (every interval-count kernel fails, and only the scale changes the numbers), or run readout tests on flat backgrounds (they cannot fail).

Files are in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/exercise_G_graviton_on_events/top_test/`:
- PREREG_N1.md
- n1_needle.py
- n1_needle.out
