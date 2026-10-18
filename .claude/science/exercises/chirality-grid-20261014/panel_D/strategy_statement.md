# Panel D statement: program strategist / phenomenologist lens (2026-10-14)

**Provenance.** Claude Opus 5.5 at xhigh. This is the same family as the supervisor, every exercise worker and the other panelists, so it is not independent. Nothing here is refereed.
- Web checks were made on 2026-10-14 at abstract or listing level unless noted.
- Scripts are in `panel_D/strategy/scripts/`: `z4_selection.py` (+`.out`) and `dqmc_cost.py` (+`.out`).
- **NT-1/2/3:** none had a REPORT.md when I finished; all three had only a PREREG.md. §4 says how each outcome would move me.

**Path prefixes:**
- **CH** = `origin/claude/chirality-grid-exercise-20261014:.claude/science/exercises/chirality-grid-20261014/`
- **GR** = `.claude/science/exercises/gravity-current-state-20261009/`
- **AX** = `docs/MINIMAL_AXIOMS_2026-06-29.md`
- **DD** = `origin/main:docs/repo/DEFERRED_DECISIONS.md`

**Labels:** proved / checked / suggested / reading / comparator.

---

## 0. Plain summary

1. **Chirality work gives the framework permission to exist; on its own it predicts nothing.**
   - Every surviving route ends at one of the field's two open questions (CH/ROUTES.md:48-52; CH/SUMMARY.md:26-28).
   - The only place the chirality lane touches data soon is the **side effects** of the framework's own corner package (X2), not its core mechanism.
2. **For D4, money is not the bottleneck.** My order-of-magnitude estimate for the 2+1D QMC tests is about $0.3k–$90k of cloud CPU.
   - What is missing is a specialist to design a model without a sign problem, run it, and vouch for it.
   - On a contested question such as Golterman–Shamir's, a result from an all-AI, same-family team with one other-vendor referee will not move the field.
3. **The field is working on both of our terminal questions right now.**
   - At the YITP workshop "Frontiers of Lattice Fermions" (29 June–3 July 2026), Kikukawa spoke on reflection positivity of a Spin(10) chiral lattice gauge theory with overlap Weyl fermions. That is route 1's open item, on the real target group.
   - I found no numerical test of the Golterman–Shamir composite/zero conjecture.
   - The 2026 group whose sign-free SMG simulation is closest to F4's test (He–You–Xu) did not analyse propagator zeros.
4. **Recommendations:**
   - **D1:** yes to a *counted* budget of matter per site, with the number left open for now. Do not accept a "coarse block" reading as free. Option (c) fails the observation standard.
   - **D2:** no to non-finitely-generated kernels as law content. Restate D2 as a bound on chirality violation paid for with auxiliary fields, which folds it into D1.
   - **D3:** keep set C as the working default. Do not reopen set B until NT-1/NT-2 report and a specialist has said whether gauged RP holds in 4D for non-abelian groups.
   - **D4:** targeted collaborator asks (b), and defer the rest (c). No weeks-scale QMC in-house. Fund (a) only once a specialist is attached and a sign-free formulation exists.
5. **What to stop:**
   - more same-family chirality rounds;
   - more 2D reflection-positivity proxies after NT-1/2;
   - any local QMC on the 16 GB machine.
6. **Next action:** one pre-registered "X2 observational sheet" with three rows:
   - the Z4 selection rules, which imply Dirac neutrinos;
   - the proton-decay bound on the grid scale;
   - the X2-L8 flavour–strain coefficient against clock and Lorentz-violation bounds.

   It takes hours, runs in-house, and can kill route 2 against data before any compute is spent.

---

## 1. Recommendations per decision

### D1. Matter per site

**Recommendation.** Say yes in principle to option (b), stated honestly as a counted number N of fermion modes per site. Do not fix N until a route passes its decisive test. Do not treat (a) as free. Reject (c) unless you are prepared to shelve the claim to match the Standard Model.

**Reasons, in plain words.**

- **(c) fails the standard.** The weak force is handed; that is an observed outcome. "Chirality is not realized on this lattice" means the framework cannot reproduce the weak interaction. Under "only observed outcomes need to be matched", (c) is a declaration of failure, not a neutral choice.
- **(a) is free only if the block's inner structure respects the axioms' translation rule.**
  - AX:40-41 says no site is privileged. AX:57-58 says the rule is covariant under lattice translations.
  - A block of k³ fine sites with fixed roles inside it is covariant only under kZ³.
  - Staggered fermions show one way out: a 2³ block whose unit translations act as taste transformations (shift symmetry). Nobody has shown that for 16-mode or 10³-mode blocks.
  - Until someone does, (a) is (b) under another name. [reading]
- **Gravity is forcing the same decision.**
  - Panel F found that the root's fermion content needs at least a ~90-qubit block per site (GR/agents/panel_F/SYNTHESIS.md:52).
  - The graviton "conflicts with one M₂(C) per site" (GR/SUMMARY.md:777).
  - Gravity's owner question 5, about a supplied non-qubit graviton (GR/SUMMARY.md:795), is the same axiom pressure.
  - **Decide D1 once, with one counted N that covers both lanes.** Waking #4 lane by lane would produce three inconsistent enlargements.
- **If #4 wakes** (DD:139-142), wake it as "site-domain size N", not as "M₄(C) for γ5". Lemma R makes the γ5 motivation irrelevant (CH/SUMMARY.md:63).

**Technical: price ladder in matter per site** (cheapest first):

| Route | Matter per site | Source | Label |
|---|---|---|---|
| X2 corner package | 16 per site, plus Z4^F | CH/SUMMARY.md:57 | — |
| F2 finite-n overlap | ~60 auxiliary Dirac fields per physical field, so roughly 10³ modes per generation | CH/routes/F2/ROUTE_REPORT.md:176 | checked, free / weak U(1) |
| F4-A slab | ~10³ qubits per site | CH/routes/F4/ROUTE_REPORT.md:134 | — |
| X3 exact overlap in real time | infinite | CH/combos/X3/COMBO_REPORT.md:247 | — |

**"Fermion number only mod 4" is not an observational cost.** It is a prediction.
- **The two Z4s agree** (checked, `z4_selection.out`). On all 16 Weyl fields, X = 5(B−L) − 4Y ≡ 1 mod 4. So X2's Z4^F (CH/combos/X2/COMBO_REPORT.md:80, :172) is the same as the anomaly-free Z4^X: ΣX³ = ΣX = 0, while uniform F has F³ = 16.
- **The Standard Model's own uniform fermion number is already broken** to Z12 by SU(2) and SU(3) instantons (12 zero modes each for three generations). [reading; standard]
- **Z4^X forbids every ΔL = 2 operator** (checked):
  - ν^c ν^c, X = 10 ≡ 2;
  - L L H H, X = −10 ≡ 2;
  - (u^c d^c d^c)², X = −10 ≡ 2.
- **Z4^X allows proton decay:** QQQL and u^c u^c d^c e^c both have X = 0.
- **Consequence:** if X2's exact Spin(10) × Z4^F holds in the full law, neutrinos are Dirac, neutrinoless double-beta decay (0νββ) has zero rate, and neutron–antineutron oscillation is absent. [suggested; this needs Z4^F unbroken in the light sector, which X2 asserts but no one has audited]
- **Baryogenesis obligation** [reading]. Standard Majorana leptogenesis is unavailable; Dirac leptogenesis or another mechanism with Δ(B−L) ≡ 0 mod 4 is needed. This is an obligation, not a kill.

---

### D2. Range

**Recommendation.** Do not admit a non-finitely-generated kernel as law content. Replace the question with: *"exact chirality is not required; the chirality-violation parameter δ must sit below observational bounds."* If route 1 is pursued, pay for it with finitely many auxiliary fields per site, counted under D1. Symmetric mass generation (SMG) routes keep finite range and do not need D2 at all.

**Reasons, in plain words.**
- No experiment can tell exact chirality from chirality violated at 10⁻³⁵ or 10⁻⁹⁰.
- Keeping "one fixed nearest-neighbour rule" (AX:57) intact protects the cleanest axiom.
- The cost is a known, counted number of helper fields per site, not a change of axiom class.
- The lattice community already works this way:
  - domain-wall and Möbius fermions at finite L_s, with the residual mass as a measured number;
  - the overlap Hamiltonian via quantum signal processing, where reaching Ginsparg–Wilson (GW) error ε costs only log(1/ε) more than Wilson (Lamm–Roggero–Singh–Spagnoli, arXiv:2607.28524, which says QSP "effectively constructs an extra dimension"). [comparator]

**Technical.**
- **Lemma R** (proved; codex-confirmed; CH/ROUTES.md:146-154): exact GW needs a kernel outside the rational, finitely-generated class. The three-way price list that came with it is not exhaustive.
- **F2's approximate form:**
  - n Zolotarev poles cost about 2n auxiliary Dirac fields per physical field, with defect δ ≈ 4e^{−2πnK/K′} (CH/routes/F2/ROUTE_REPORT.md:158).
  - Required δ (suggested, :160): ≲ 1e-35 for ρ-parameter safety, or ≲ 1e-88 for the photon-mass bound if U(1)_em is not kept exact.
  - Checked pole counts: n = 28 gives 1e-36 and n = 70 gives 1e-90 for free fields; n = 30 and n = 76 at κ = 0.107 in weak U(1) backgrounds (:169, :173).
- **What finite n does not buy:**
  - It prices only route 1's range.
  - L2α (non-perturbative locality of the non-abelian measure) stays open even with an exact kernel (CH/ROUTES.md:44).
  - The uniform approximation needs the H_W gap, i.e. hard admissibility (P-X3d), which NT-2 is now testing for RP.

---

### D3. Time

**Recommendation.** Keep set C (continuous time on Z³) as the working default. Do not reopen set B now. Record set B's full bill:
- time added to the Lattice axiom;
- Π-W or Π-NL for the gravity bridge;
- Π-W or 5D without Pauli–Villars (PV) fields for matter;
- for route 1, the non-rational kernel or an infinite real-time fibre.

Revisit only under the conditions in §4.

**Reasons, in plain words.**

- **Set B's attraction is real.** It is the one symmetry that fixes matter light cones without tuning (GR/SUMMARY.md:774).
- **But both of set B's lanes now fail reflection positivity:**
  - gravity's conserved bridge: R19-33, B-RP-FAILS (GR/TESTS.md:8909-8913);
  - the gauged overlap: K2c, codex-confirmed in the finite 2D U(1) vector-like proxy, tori included (CH/ROUTES.md:190-204).
- **What RP failure means.** Without RP there is no positive Hilbert space, so observed probability conservation is not reproduced. The target contract already forbids "Euclidean-only without a reflection-positive real-time reconstruction" (CH/WALL.md:44).
- **Set C's cost is ugly but not observationally wrong.** It costs tuned numbers: 4 per charge class to about 1e-16, reset at each order (GR/SUMMARY.md:778), or a counting rule. That is an aesthetic and credibility cost, not a mismatch with data.
- **The field is moving to Hamiltonian, continuous-time formulations.** The YITP 2026 programme included:
  - Kikukawa: the Hamiltonian formalism of Spin(10) chiral lattice gauge theory;
  - Gioia Yang: exact chiral symmetries of 3+1D Hamiltonian lattice fermions;
  - Singh: the QSP overlap Hamiltonian;
  - Thorngren: symmetry disentanglers (TPF, JHEP 07 (2026) 271);
  - Shao: lattice chiral symmetry from bosons in 3+1D.

  Set C results are what that community can check and build on. A qubit framework is natively Hamiltonian. [comparator]
- **Set C stakes chirality on SMG** (F2-T; the referee notes that other escapes are not excluded, CH/ROUTES.md:156). That is where the most active numerical work is:
  - He–You–Xu, arXiv:2603.18278 (2026);
  - Maiti–Banerjee–Chandrasekharan–Marinkovic, PRL 137, 151601 (2026);
  - Butt–Catterall–Hasenfratz, PRL 134, 031602 (2025);
  - Butt–Catterall–Hartshaw–Hasenfratz, arXiv:2608.18239;
  - Hasenfratz–Xu, arXiv:2604.02424.

  The field will settle or sharpen frontier (I) faster than we can.
- **Decide D3 together with gravity's question 6** (GR/SUMMARY.md:796). It is the same choice.

---

### D4. Compute and collaborators

**Recommendation.** Make targeted collaborator asks (b) and defer the rest (c). Do not run weeks-scale QMC in-house now. Switch to (a) only when both of these hold:
1. a specialist agrees to co-design or referee the run;
2. a sign-free formulation of X2-MB, or of F4 test A, is written down (X2:286 says "establish sign-freeness first").

Treat 4D HMC as collaborator-only.

**Reasons, in plain words.**

- **The cost is people, not dollars.** My estimate (suggested; `dqmc_cost.out`) is anchored on the He–You–Xu scale: 8 modes per cell, L ≤ 20, β = L + 30, Δτ = 0.1, flops ≈ L_τ·N³ per sweep, at 16 GFLOP/s per core.

  | Run | N | Core-hours per 15-coupling scan | Memory per process |
  |---|---|---|---|
  | Far surface only, L = 12 | 1152 | ~3e2 | 0.9 GB |
  | Far surface only, L = 20 | 3200 | ~1e4 | ~8 GB |
  | 6-layer slab, L = 12 | 6912 | ~7e4 | ~32 GB |
  | 6-layer slab, L = 20 | 19200 | ~2e6 | ~300 GB |

  - Add smaller sizes and replicas at about ×2–3.
  - At $0.01–0.05 per core-hour that is $0.3k–$90k.
  - The owner rule is ≤ 1.5 GB per process on a 16 GB machine (memory note "Memory budget for probes"). Only the L = 12 far-surface run fits locally, and L = 12 does not settle finite-size scaling.
  - 4D HMC for SMG with gauge fields is in the 10⁷–10⁸ core-hour class of allocations (the Hasenfratz–Witzel and Butt et al. lines). [reading]
- **Both decisive questions belong to the field** (CH/ROUTES.md:48-52). An outside answer is worth as much to us as our own, and it is more credible.
  - F4 test A's far surface (CH/routes/F4/ROUTE_REPORT.md:185-194) is essentially He–You–Xu's sign-free bilayer-honeycomb SMG model: 8 Dirac cones, direct transition, 19 bilinears searched.
  - Per the arXiv HTML, they measured G(k) near the Dirac points but **did not analyse propagator zeros**.
  - I found no numerical test of the Golterman–Shamir composite/zero conjecture (arXiv:2505.20436; Lattice 2025 proceedings arXiv:2603.15985).
  - So the cheapest "compute" for routes 2 and 3 is an **analysis ask on configurations that already exist**.
- **Credibility.** The program's verification is same-family workers plus one codex referee. That is adequate for internal pricing, but not for a contested numerical claim about SMG. The field will engage with small, checkable claims that come with code, not with a theory-of-everything framing.

**Collaborator map, with the ask for each (to be sent by Jon).**

| Route / question | Who (activity verified this session) | The ask |
|---|---|---|
| Route 1, D3: gauged RP of the chiral overlap measure | **Y. Kikukawa** (Tokyo). YITP talk, 29 June 2026, "On the Hamiltonian formalism of Spin(10) chiral lattice gauge theory": RP of the path-integral formulation with overlap Weyl fermions, measure defined by saturating 't Hooft vertices. His slides are a >10 MB PDF I did not download; read them first. | "Does gauged RP hold for your Spin(10) measure? Here is a reproducible 2D U(1) hard-admissibility witness that is negative, codex-confirmed (K2c). Does your construction avoid it, and how?" |
| Frontier I, routes 2 and 3: the Golterman–Shamir condition (3) in 2+1D | **Xiao Yan Xu** (SJTU), **Yi-Zhuang You** (UCSD), **Cenke Xu** (UCSB): arXiv:2603.18278, and C. Xu's YITP talk. Invite **Golterman/Shamir** to fix the readings in advance, as an adversarial collaboration. | Measure the index of the zero of G(ω = 0, k) and the three-fermion composite spectral weight at the Dirac points in the existing SMG phase. Offer F4-A's pre-registered readings (PASS-SMG / FAIL-GS / FAIL-SSB / FAIL-RELOCATE). |
| Route 2 in 4D: does an intermediate symmetry-broken phase appear? | **S. Catterall** (Syracuse), **A. Hasenfratz** (Colorado), **N. Butt**. They see an intermediate antiferromagnetic phase in 4D staggered Higgs–Yukawa (arXiv:2608.18239). TW-3 already lands on their count: 4 staggered fields = 16 Weyl (GR/TESTS.md:9731), as in Li–Wang–You, arXiv:2412.19691. | Only after NT-3. Does a light-decoupling filter like X2's change the intermediate phase? |
| Route 3 geometry | **S. Sen** (Iowa State): Dang–Karur–Sen, arXiv:2606.05306, slab domain-wall fermions with gauge-field flow; Kaplan–Sen | Whether F4-B's 1/L penalty (CH/routes/F4/ROUTE_REPORT.md:115) matches their flow numerics. |
| Lemma R novelty and correctness | **H. Fukaya** (Osaka): YITP talk "Lattice Dirac operators and K-theory"; Aoki et al., arXiv:2602.22858 | Is Lemma R new beyond Read 2017 and Chen–Mazaheri–Seidel–Tang? Check before claiming it. |
| Chirality joined with gravity | **L. Boyle and V. Vaibhav** (Edinburgh): restricted Kähler–Dirac fermions on simplicial complexes coupled to the tetrad, with exact local Lorentz (YITP and Lattice 2025 talks; no paper found) | Not a test. They are the one outside effort aimed at the program's gravity-plus-chirality coupling. |
| Qubit-sized sites for disentanglers | **Thorngren / Preskill / Fidkowski** | Truncating rotors to finite dimension (CH/OUTSIDE_VIEW.md:223) is exactly the qubit framework's D1 question. |

**Open code.**
- **ALF** (Würzburg): general auxiliary-field QMC with custom Hamiltonians, MPI/OpenMP, development docs dated February 2026.
- **SmoQyDQMC.jl:** MIT licence, SciPost Phys. Codebases 29 (2024).
- Neither has a ready-made model for this SMG test that I could verify, and He–You–Xu do not name their code.
- For 4D, Grid (Edinburgh) is open source. [comparator; recalled, not checked this session]

**What to stop doing.**
1. **Same-family breadth rounds on chirality.** 18 agents produced a map, not a mechanism (CH/ROUTES.md:48: "No combination supplies a new mechanism"). The marginal value of another round is near zero.
2. **2D or 1+1D proxies as RP or SMG evidence** once NT-1/NT-2 report. The 4D non-abelian case is a specialist's problem.
3. **More pricing of variants.** The price list is already long enough to decide on.
4. **Local QMC at decisive sizes.** It cannot fit the memory rule.
5. **Letting chirality take budget from lanes that can reach data.** One example is the E2 siren forecast: gravitational-wave distances 0.4–1.3% above light distances at z = 1 (GR/SUMMARY.md:749).

---

## 2. How the decisions interact

- **Does set B force D2? Yes, for route 1.**
  - Exact GW needs the non-rational kernel, or an infinite real-time fibre (P-X3a/b; CH/combos/X3/COMBO_REPORT.md:246-247).
  - The finite-L_s fallback has only approximate gauge invariance, i.e. F2's price of about 60 auxiliary fields per site (X3:311). That is D1 again.
  - On top of this, set B forces the RP prices (Π-W/Π-NL) in both lanes (X3:244).
  - **Set B's bill:** D2 (or a large N), plus time on the lattice, plus RP prices.
  - **Set C's bill:** D1 (16–10³), plus the tuned matter cones, plus a bet on SMG.
- **Does D1 = (a) make D2 moot?**
  - **In principle, no.** Lemma R holds for any fibre size (CH/SUMMARY.md:30, :63).
  - **In practice, yes,** under the observation standard: a large enough counted N buys δ ~ e^{−cn}. That is the reason to restate D2 as a δ bound.
  - The caveat: route 1 still needs L2α and gauged RP, which N does not buy.
- **D1 sets the scope of D3.**
  - Set B's exact real-time route needs an infinite fibre. Any finite N leaves set B's chirality approximate (finite L_s), and that branch is RP only for the bare 5D determinant, not with PV subtraction (K2c, CH/ROUTES.md:184).
- **D4 is mostly independent of D1–D3.** The outside answers (the Golterman–Shamir composite/zero question; chiral-measure RP in 4D) are needed whichever way Jon decides, so the collaborator asks are no-regret.
- **Cross-lane.** D1 is gravity's question 5 plus the ~90-mode root, and D3 is gravity's question 6. Deciding chirality alone would set gravity's premises by accident.

---

## 3. Strongest argument from my tradition, and the steelman against

**The phenomenologist's argument.** A construction earns credibility by touching data, not by surviving internal kill rounds.
- Chirality gives the framework permission to exist. Its observable content lives in side effects.
- **X2 has three side effects that touch data, and each is cheap to compute:**
  1. **Exact Z4^F forbids all ΔL = 2 operators** (checked arithmetic): Dirac neutrinos, zero 0νββ, no n–n̄ oscillation.
     - LEGEND-1000, nEXO and similar experiments cover the inverted-ordering band in the 2030s. [comparator]
     - A 0νββ signal would force Z4^F breaking, and with it the loss of X2's mod-16 basis for "ν_R is forced".
  2. **Eichten–Preskill leakage** is "present, cannot be forbidden, irrelevant (dim-6)" (CH/ROUTES.md:43). But dimension-6 operators with X = 0 (QQQL) are exactly what proton-decay searches test.
     - At a = ℓ_P the rate is invisible.
     - Panel F says a = ℓ_P is load-bearing and not asserted (GR/agents/panel_F/SYNTHESIS.md:44). Super-K's τ(p→e⁺π⁰) bound therefore sets a lower bound on 1/a for the X2 package once the leakage coefficient is computed. [suggested; coefficient uncomputed]
  3. **X2-L8:** non-trivial CKM forces a first-order flavour–strain channel (proved, checked over 1120 subgroups; CH/combos/X2/COMBO_REPORT.md:132-136); its size is uncomputed.
     - The analogous TW-2 coefficient sits ×4.7–17.8 above the clock bound on its minimal branch. The referee rules that real but branch-dependent (GR/TESTS.md:9726-9728).
     - **So X2-L8 plausibly lands near current clock sensitivity:** either a kill or a near-term prediction.
- **Compute these first.** They can kill route 2 at no cost before anyone spends weeks of QMC on its dynamics.

**Steelman against my recommendations.**
1. **Against deferring compute.**
   - Compute is cheap, and the program's comparative advantage is speed.
   - Nobody outside will ever simulate the filtered-walker package, so deferring abandons the only framework-specific test.
   - Cold asks from an unknown, AI-driven program get low response rates and months of latency.
   - The Golterman–Shamir vs SMG dispute has run since 2023 without resolution, so waiting may mean years.
2. **Against "Z4 implies Dirac neutrinos" as evidence.** Any Dirac-neutrino model predicts the same, and so do Spin(10)-SMG proposals in general. It falsifies but does not discriminate.
3. **Against set C.** The classic objection to Planck-lattice quantum gravity is the Collins–Perez–Sudarsky–Urrutia–Vucetich fine-tuning problem (PRL 93, 191301 (2004)) [comparator, recalled]. Set C pays it with tuned numbers at every order, which is precisely what quantum-gravity phenomenologists reject. Set B answers it by symmetry. To that audience set B is the credible gravity story, and K2c is still only a finite 2D vector-like proxy.
4. **Against D2-as-δ.**
   - Approximate gauge invariance in a chiral theory is dangerous non-perturbatively: gauge-variant terms are relevant and amplified by Λ², as the history of the Rome gauge-fixing approach shows.
   - "δ ≤ 1e-35" is itself a tuning of n.
   - The consensus since Lüscher is that chiral gauge theories need exact gauge invariance.

My answers to the steelman:
- **(1):** the asks cost one email each and the money is held back, not refused. The trigger for (a) is explicit.
- **(3):** under Jon's standard, failing RP fails observed probability conservation, while tuned numbers fail no observation.
- **(4):** that is why I price only route 1's *range* this way and leave L2α and RP as its real obstacles.

---

## 4. What would change my mind

**NT-1 (chiral-measure RP).**
- **CHI-RP-PASS-at-power:** the 2D failure may be specific to the vector-like measure. I would move D3 to "keep both sets open", send the Kikukawa ask first, and treat D2 as live for set B.
- **CHI-RP-FAIL:** set B's real-time chirality needs Π-W or 5D without PV. I would recommend recording set B as priced out for chirality and stopping work there.
- **OPEN:** no change.

**NT-2 (3D hard plaquette bound).**
- **PG3-NEG:** the admissibility bound itself is not RP. Route 1 in set B then needs a different gauge measure, which strengthens "stop set B".
- **PG3-PSD:** removes one hazard only.

**NT-3 (T-G1).**
- **Note the asymmetry.** NT-3 is exact diagonalisation on 1D rings with L ≤ 7 plus one 2×2×2 cube (NT3/PREREG.md:37-39). CH/SUMMARY.md:65 itself says not to treat 1+1D gapping toys as 4D evidence. So a SYMMETRIC reading is weak support, while BROKEN is informative.
- **TG1-BROKEN:** route 2 fails its precondition. No QMC for X2-MB; the A3 ask to Catterall/Hasenfratz becomes "does your unfiltered SMG avoid this?"
- **TG1-SYMMETRIC:** only a precondition is met. X2-MB becomes worth a collaborator ask, and I would fund (a) if a sign-free formulation exists.

**Other evidence that would move me.**
- **A specialist agrees to co-run:** switch D4 to (a) immediately. The money is small.
- **X2-L8 or the proton-decay row exceeds bounds on every branch with no symmetric zero:** route 2 is excluded or needs another counted rule. D1's chirality motivation then rests on route 3 and the field.
- **The field confirms the Golterman–Shamir composite/zero mechanism numerically:** routes 2 and 3 both die, and (c) becomes the honest record for SMG routes. Only route 1 would remain, which pushes D3 back toward set B and D2 back to the table.
- **0νββ is observed:** X2's exact Z4^F is excluded.

---

## 5. One concrete next action

**Register and run one "X2 observational sheet"** (in-house, same machinery as TW-2 and panel F; hours to a day). Readings are fixed before running.

| Row | What it does | Readings |
|---|---|---|
| **R1. X2-L8 size** | Compute the first-order traceless-strain coefficient of the minimal CKM-generating breaking on the hw1 corners. Map it, as TW-2 and panel F did, onto (i) the m_p/m_e drift under the measured nHz background against the clock bound (~4e-17 per year, GR/agents/panel_F/SYNTHESIS.md:98), and (ii) flavour-sector Lorentz-violation bounds from neutral-meson oscillations [comparator: the SME data tables]. | **FLAV-KILL:** above 10× a bound on every symmetry-allowed branch, with no symmetric zero. **FLAV-NEAR:** within 10× of a bound on some branch; this becomes a prediction. **FLAV-SAFE:** below 1e-2 of all bounds. |
| **R2. Z4 audit** | Confirm that the full X2 law, including Yukawas and Higgs, keeps Z4^F exact on the light sector. If it does, record "Dirac neutrinos, zero 0νββ, no n–n̄" as a falsifiable output. | — |
| **R3. Proton-decay floor** | Bound the coefficient of the QQQL operator from Eichten–Preskill leakage and turn Super-K's τ(p→e⁺π⁰) bound into a lower bound on 1/a. | — |

**If Jon will send only one email instead,** it should be the Kikukawa ask (§1, D4): one specialist reply on chiral-measure RP in Spin(10) settles more of D3 than any further 2D proxy we could run.

---

## Sources

- YITP "Frontiers of Lattice Fermions" (29 June–3 July 2026): https://indico.yukawa.kyoto-u.ac.jp/event/78/ , contribution list https://indico.yukawa.kyoto-u.ac.jp/event/78/contributions/
- Kikukawa, YITP talk (29 June 2026): https://indico.yukawa.kyoto-u.ac.jp/event/78/contributions/1982/ ; Kikukawa–Usui, free overlap RP: https://arxiv.org/abs/1012.0152
- Thorngren, YITP talk: https://indico.yukawa.kyoto-u.ac.jp/event/78/contributions/1971/ ; TPF: https://arxiv.org/abs/2601.04304
- Boyle–Vaibhav, YITP abstract: https://indico.yukawa.kyoto-u.ac.jp/event/78/contributions/1976/
- Lamm–Roggero–Singh–Spagnoli, QSP overlap: https://arxiv.org/abs/2607.28524
- He–You–Xu, bilayer-honeycomb SMG DQMC: https://arxiv.org/abs/2603.18278 (HTML v2 read for sizes, sign-freeness and Green's-function content)
- Maiti–Banerjee–Chandrasekharan–Marinkovic: https://arxiv.org/abs/2512.24836
- Hasenfratz–Xu: https://arxiv.org/abs/2604.02424
- Butt–Catterall–Hasenfratz: https://arxiv.org/abs/2409.02062 ; Butt et al. 2608.18239 (via aggregator https://papers.cool/arxiv/2608.18239)
- Li–Wang–You: https://arxiv.org/abs/2412.19691
- Golterman–Shamir: https://arxiv.org/abs/2505.20436 ; https://arxiv.org/abs/2603.15985
- Dang–Karur–Sen: https://arxiv.org/abs/2606.05306
- Murayama, YITP abstract: https://indico.yukawa.kyoto-u.ac.jp/event/78/contributions/1983/
- ALF: https://alf.physik.uni-wuerzburg.de/page/about ; SmoQyDQMC.jl: https://scipost.org/SciPostPhysCodeb.29
