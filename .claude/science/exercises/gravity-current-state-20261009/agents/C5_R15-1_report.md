# C5 R15-1 report: the CMC lattice-time model (R14-5): causality, stability, collapse, and its vacuum

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-12, 21:40Z to about 22:20Z. No repository file was edited.

**Scratch folder.** `S/` = `.../scratchpad/C5/R15-1/`. Scripts and outputs are in `S/scripts/`. Each runs in under a minute at `OMP_NUM_THREADS=2`.
- `r151_quadratic.py/.out` (sympy): the second-order ADM action of GR + a canonical scalar χ + the R14-5 E-sector, written as S_E = ∫√h [g(t) − Nλ(t)]. It also gives the background equations and the kinetic matrix of (ζ, δχ).
- `r151_reduce.py/.out`: reduction to the single scalar. It integrates out ζ and checks that the auxiliary solution is regular as g → 0.
- `r151_dispersion.py/.out`: A(k), the GR-limit check against Mukhanov–Sasaki, the high-k expansion, and a scan in g.
- `r151_window.py/.out`: the ghost and tachyon map in (g/H², χ̇²/H²).
- `r151_homog_gsign.py/.out`: R14-5's `r145_homog.py`, copied unchanged except for one print that gives the **sign** of g/H² during each step.
- `r151_signal.py/.out`: (a) the instantaneous-jump formula, checked numerically, and the real-space response.
- `r151_acg_tail.py/.out`: (a) a comparator test of Afshordi–Chung–Geshnizjani's own coupled cuscuton–scalar system (their eqs. 53–56). Does the response leak outside the light cone?
- `r151_throat.py/.out`: (c) the lapse floor in a black-hole throat, CMC with ⟨N⟩ = 1 against maximal slicing.
- `r151_gridvac.py/.out` (sympy): (d) the grid zero-point inside the Lemma-C bookkeeping.
- `downloads_acg/` (untrusted data, only text-extracted and read): the hep-th/0609150 PDF and its text.

**Read.**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (`AX`); `TESTS.md:2302-2320` (the C5 method); the item `TESTS.md:4927-4938`; `agents/C5_R14-5_report.md` (`R145`); and the R14-5 referee verdict, which appeared during this run: `scratchpad/C5/ref_R14-5/REFEREE_VERDICT.md` (`vR14-5`; archived as `P/agents/C5_R14-5_referee_verdict.md`), **NOT CONFIRMED, reading OPEN**.
- In part:
  - `TESTS.md:4860-4923` (R14 items and readings), `:4621-4641` and `:4721-4729` (R13-3);
  - `C5_R11-3_referee_verdict.md` (`vR11-3`) in full, and `C5_R11-3_report.md:40-160`;
  - `C5_R13-3_report.md:205-225` (Lemma G′);
  - `RN_L3_report.md:225-300` and `RN_L3_referee.md`;
  - the R14-5 scripts.

**Labels.** proved / checked (sympy or numerics this run) / suggested / reading / comparator. A comparator is **V** if fetched this run, otherwise **RECALLED**.

**Subtraction rule (named before the runs).**
- g(t) := N(λ + p_E) is the Lemma-C number of the *observable* combination (G − κT_matter). Under the grid vacuum this is g′ (§4(d)).
- "Response outside the cone" is the full response minus the g = 0 response of the same system. The control is GR (g = 0) or Klein–Gordon (V_φψ = 0).
- In `r151_window`, "tachyon" means ω² < −H², at a frozen background.

---

## 0. Verdict against the FIXED readings (`TESTS.md:4935-4938`)

**Worker reading: FAIL, for the referee.** Test (a) fails: there is signalling whenever g ≠ 0. Lemma C (refereed-confirmed, `vR14-5:5-25`) makes g ≠ 0 necessary during every vacuum change the model absorbs.

**Fallback.** If the referee rules that an instantaneous influence ordered by a global time does not count as "signalling" in the reading's sense, the reading falls to **INCONCLUSIVE**, not PASS. In that case (b) holds only under a new condition on the reader, and (c) rests on an assumed existence.

| Test | Finding | Label |
|---|---|---|
| **(a) signalling** | **Yes, whenever g ≠ 0.** A local impulse F on dust gives an instantaneous jump in the gauge-invariant comoving density rate at every distance: Δδ̇(y) = F(y) + (3/2)g ∫ G_Q̄(y−x)F(x)d³x, where G_Q̄ is a positive Yukawa kernel with Q̄ = (3/2)κ(ρ+p)_nc. In GR (g = 0) the response is ultralocal (Δδ̇ = F). No closed signal loops: CMC time is a global time function. | proved (linear, within the model's equations); checked |
| (a) literature | ACG's "no signalling" rests on two things: the cuscuton's degenerate phase space, and a WKB group-velocity bound for the coupled field. Their own coupled system leaks outside the light cone at about 1e-2·V_φψ², against a 1e-15 control. | checked (comparator V) |
| **(b) ghost / gradient / strong coupling** | One local scalar (rank-1 kinetic matrix). No UV gradient instability (c_s → 1). Healthy for g ≤ 0. **Ghost for g > 6H²** at k < aχ̇√(g−6H²)/(2H). **Tachyonic (ω² < −H²) for g ≳ 2–5H²**. A smooth vacuum drop has g < 0, but the R14-5 reader reaches g/H² up to +1.0e3, above 6 for 1.8–7.4% of step samples. No Hořava scalar. Smooth at g → 0 (quadratic order). | proved (closed form) / checked |
| **(c) collapse** | The lapse cannot collapse: N_min ≥ S/sup Q̃ with S = 1/⟨N₁⟩ > 0. In a throat N ≥ 1.1·S·m², of order (mH₀)². This corrects R14-5's "lattice time freezes". The E-curvature 3g/N stays bounded. CMC existence remains a hypothesis: in GR there are cosmological counterexamples. | proved (given N > 0, bounded Q̃); checked; comparator V |
| **(d) grid vacuum** | **Two readings.** (d-i): if the vacuum stress has no separate conservation law, any uniform isotropic site-frame vacuum (any w ≥ 0) is absorbed. E + κT_grid is a Lemma-C fluid, and g′ = −2Ḣ − κ(ρ+p)_matter is not Planckian (R14-5 K5 corrected). (d-ii): if the vacuum must conserve momentum by itself (R13-3 Lemma G′), (ρ+p)_v ∂N = 0 forces (ρ+p)_v = 0. That means exact B–F pairing or one tuning. | proved (sympy) / reading for the bridge choice |

**Against the expectation in the item** ("the cuscuton literature argues no" for (a)): the argument does not cover influence mediated by the constraint. That influence is present and proportional to g.

---

## 1. In plain words

- **(a) Faster-than-light influence.**
  - The model's clock is set by solving one equation across all of space at once.
  - When the extra number g is zero, that clock is pure bookkeeping, and the model is ordinary general relativity.
  - When g is not zero, it is not bookkeeping. Push matter here, and the expansion rate of matter a billion light-years away changes at the same instant, weakened only by a Yukawa factor over about half a Hubble radius.
  - The model needs g ≠ 0 exactly when it is absorbing a change in vacuum energy, which is its whole purpose. So the influence comes with the mechanism.
  - The influence can never loop back into the past, because the grid's time orders everything.
  - Today it is tiny: of order one part in a million of the local effect, if g is the size of the backreaction residual (suggested). During early-universe phase transitions it is of order one or larger.
- **(b) Stability.** With ordinary matter, the model has no extra field and no runaway at short wavelengths. It goes bad only if g is positive and larger than a few times H²: then long waves of matter grow too fast or carry negative energy. A smooth drop in vacuum energy makes g negative, which is safe. The prototype reader in R14-5 overshoots into the bad region for a few percent of each transition, so the reader must be built to stay out of it.
- **(c) Black holes.** Because the average tick rate is fixed at one, the clock inside a black hole cannot stop completely. It slows to about (black-hole light-crossing time × Hubble rate)², which is 1e-46 for a stellar black hole. So nothing blows up there. Whether a constant-mean-curvature clock exists for the whole universe through all of structure formation is still assumed. In general relativity there are known universes where no such clock exists.
- **(d) The grid's vacuum.** The model's equations never look at the vacuum's pressure, and they put its energy into λ. So a grid vacuum with positive pressure is as invisible as a cosmological constant, *provided* the vacuum's energy and momentum may be traded with the creation sector. If instead the vacuum must keep its own momentum, the grid's sites would have to fall freely, while the clock needs them to hover. Then the vacuum must have ρ + p = 0, which needs boson–fermion pairing or one tuning.

---

## 2. Hypotheses and class (stated before titles)

- **Class 𝒵** (`R145:34-41`): a smooth continuum; fixed proper site density; E_ni = 0 and E^TL = 0 imposed; E_nn = λ(t) uniform; ⟨N⟩ = 1; the CMC clock where g ≠ 0; P-T creation reading the global ρ̄. Lemma C holds there (refereed, `vR14-5:7-25`).
- **H-act (used in (b)).** For k ≠ 0 the E-sector is generated by S_E = ∫dt d³x √h [g(t) − Nλ(t)], with background functions g and λ.
  - Its N-variation gives E_nn = λ, and its h_ij-variation gives p_E = g/N − λ. This is exactly Lemma C's stress (`R145:177`).
  - It is the cuscuton in unitary gauge, with V(φ(t)) = λ and μ²φ̇ = g (comparator, Afshordi 0907.5201 via `R145:178`).
  - The zero mode (k = 0) is excluded: there the creation law replaces the Friedmann equation.
- **H-matter.** For (a): pressureless dust in synchronous-comoving gauge, as R14-5 §4.5. For (b): one canonical scalar χ with potential V(χ).
- **H-pos.** N > 0 on each slice (R14-5 Lemma P). Per `vR14-5:55-62` this needs Q̃ ≥ 0 with the dropped term (−½⟨R⟩ + ½⟨σ²⟩) restored. It is a hypothesis here.
- **H-CMC-exist** (`R145:102`): carried. It is not proved.
- **Excluded:** a Z³ construction; nonlinear (cubic) interactions; fluids other than dust and a scalar; inhomogeneous bubble dynamics; records as a q-charge; a regularized reader.

---

## 3. Prior art (each counted once)

1. **R14-5 and its referee** [ref; NOT CONFIRMED, OPEN].
   - Lemma C, the conditional maximum principle and the g ≡ 0 GR limit are confirmed (`vR14-5:3-25,48-53,70`).
   - Causality and Hamiltonian stability for g ≠ 0 were left open (`vR14-5:86-88`). This item answers those two.
   - Also: "CMC for all time is an additional clock law" (`vR14-5:25`); and H² < 0 in transitions (`vR14-5:41`).
2. **R14-5 worker claims tested here:**
   - K2, no extra scalar (`R145:311-313`);
   - K3, causality not cleared (`R145:314-316`);
   - K5, H-vac-grid kills the model (`R145:317-320`);
   - "lattice time freezes" (`R145:51,222,227,303`).
3. **RN L3** [ref]. In projectable Hořava the scalar has ω² = −(1−2c)Jgk² (RN's own symbols), which is a ghost, a tachyon, or strongly coupled at λ = 1 (`RN_L3_report.md:252-266`; `RN_L3_referee.md`, item 5).
4. **R11-3 and its referee** [ref].
   - U has w ≥ 0 for every positive dispersion; M only when its spatial kinetic contribution is nonnegative. A flat band gives w_M = −1 (`vR11-3:35-41`).
   - V2/V3 absorb the homogeneous pressure, and V3 also the energy (`vR11-3:51`).
5. **R13-3 Lemma G′** [worker, suggested] (`C5_R13-3_report.md:217-221`). Under a separately conserved grid vacuum, sites are geodesic.
6. **O3** [ref] (`TESTS.md:2399-2404`): pairing needs matched B/F spectra; the qubit-pairing test is INCONCLUSIVE; FS M1 lattice SUSY is an escape.
7. **Comparators.**
   - Afshordi–Chung–Geshnizjani hep-th/0609150 (V, full text): §III and §VI B (`downloads_acg/acg.txt:282-373, 803-858`).
   - Gomes–Guariento 1703.08226 (V, abstract): regular only as a global degree of freedom on CMC, with lapse conditions.
   - Kim–Geshnizjani 2010.06645 and Boruah et al. (V, via a search summary): the cuscuton+scalar denominator [(k/a)²H² + P(3H² + P + Ḣ)] with P = χ̇²/2, and a ghost-freedom argument for the cuscuton's sign.
   - Bhattacharyya et al. 1612.01824 (V, abstract; detail via `vR14-5:88`).
   - Beig–Ó Murchadha gr-qc/9706046 (V): maximal Schwarzschild slices cover r > 3m/2; the central lapse decays exponentially with e-folding time (3√6/4)m.
   - Chruściel–Isenberg–Pollack gr-qc/0409047 (V): vacuum cosmological maximal globally hyperbolic spacetimes with no CMC Cauchy surface.
   - Isenberg–Rendall gr-qc/9710053 (V): Einstein–dust spacetimes with a CMC slice but no covering CMC foliation.
   - The maximal limiting-surface constant C = 3√3m²/4 (RECALLED).
8. **Repository grep.** R14-5 already grepped "cuscuton", "CMC", "York time" and "maximal slicing" (`R145:148`). I added "signalling" and "cuscuton" in `P/agents`. "Cuscuton" hits only R14-5 and its verdict, which is now archived as `agents/C5_R14-5_referee_verdict.md`. The "signalling" hits, each counted once, show that the campaign treats in-principle faster-than-light signalling as a failure:
   - `B1_report.md:65` (R11 "no signalling" as a quantum-consistency requirement);
   - `C5_R4-4_report.md:87` (CG "signals faster than light in principle, against the campaign's no-signalling" requirement);
   - `C5_R3-4_report.md:188` (O(1) superluminal signalling in semiclassical collapse);
   - `C5_R13-4_report.md:253` (operational signalling from tails).

   None treats a lapse-mediated instantaneous stress.

---

## 4. Results

### 4(a) Signalling through the lapse when g ≠ 0

**Lemma S (proved at linear order within 𝒵; checked).**
- **Setup.** Take dust in synchronous-comoving gauge, with CMC time T = t + ξ. R14-5's equations (`R145:266-272`) were re-derived here:
  - the transformation δf^sync = δf^CMC + ḟξ;
  - δN^CMC = −ξ̇;
  - the tilt term +k²ξ/a² in θ_n.
- They give:
  - D_k ξ = δ̇, with D_k = k²/a² − 3Ḣ;
  - δ̈ + 2Hδ̇ = (κ/2)ρδ + ½[(3ġ + 2gθ)ξ + 3gξ̇] + F(x)δ_D(t − t₀).
- **The jump.** Here F is a local external impulse (Alice). Because ξ̇ carries D_k⁻¹δ̈, the jump across the impulse is

  Δδ̇_k = F_k · D_k/(D_k − 3g/2) = F_k [1 + (3g/2)/(k²/a² + Q̄)].

  The step uses −3Ḣ = Q̄ + 3g/2 and Q̄ = (3/2)κ(ρ+p)_nc. In real space:

  **Δδ̇(y) = F(y) + (3g/2) ∫ d³x G_Q̄(y − x) F(x),  G_Q̄ = a² e^{−√Q̄ a r}/(4πr) > 0.**
- **GR control.** For g = 0, Δδ̇ = F exactly. Linear dust is ultralocal in this gauge.
- **Consequence.** For g ≠ 0, the comoving density rate (gauge-invariant) at y jumps at the same lattice instant as the impulse at x, for every separation. That is information transfer outside the light cone.
- **Checked** (`r151_signal.out:1-12`). Numerical integration through a narrow pulse matches the formula to about 2e-3 relative. The residual is the H × pulse-window term. This holds for g/H² = −50, −1, +2e-6, +1 and k = 0.3, 1, 5.
- **Monopole response** (`r151_signal.out:15-17`; per unit monopole impulse, c = H = 1):
  - at r = 0.1 c/H: 3.2e-6 if g/H² = 3e-6 (the size of today's backreaction residual, suggested from `R145:59`, RECALLED magnitude); 1.06 if g = H²; 1.1e2 if g = 100H².
  - A momentum-conserving push removes the monopole and the dipole. The far field is then the quadrupole of G_Q̄. It is still nonzero (reading).
- **Why g ≠ 0 is unavoidable** (proved, by combining with Lemma C, `vR14-5:18-25`). Absorbing a vacuum change needs λ̇ ≠ 0, which forces g ≠ 0 and so a nonzero kernel. Homogeneously, with an exact reader, g = κρ̇_v/(3H) during the change (proved; from H² = κρ_nc/3 and ρ̇_nc = −3H(ρ+p)_nc − ρ̇_v).
- **Late times** (suggested). In a lumpy universe Λ̃ = ½⟨R⟩ − ½⟨σ²⟩ (`R145:257`; `vR14-5:44`) evolves, so g = −Λ̃̇/θ ≠ 0 generically.
- **A further global channel** (suggested). S(t) = 1/⟨N₁⟩ and the reader's ρ̄ are whole-slice averages, so any local change shifts them at once, suppressed by 1/V.

**Causal order (proved, elementary).** Given H-pos, the CMC time is a global time function. Every influence is either within a slice (Lemma S) or inside the light cone, so it has dt ≥ 0. No closed signal curve can form. This is the preferred-frame situation of khronometric theories (comparator RECALLED; C4 F1 rows).

**The literature's "no".**
- **ACG §III** argues that the cuscuton's degenerate phase space carries no microscopic information (`acg.txt:458-460`). They also say the causal behaviour of the fields it couples to is "a model dependent problem" (`acg.txt:369-373`).
- **ACG §VI B** shows only that the WKB group velocity of the coupled field is < 1 (`acg.txt:803-858`). It does not compute the support of the retarded Green's function.
- **Checked** (`r151_acg_tail.out`). In ACG's own system, eqs. (54)–(56) in 1+1D, a compact source gives |ψ| outside |x| > t + w + 0.25 of 1.2e-4 to 4.1e-2 for V_φψ = 0.1–0.9. That is about 1e-2·V_φψ² (t = 2, 5). The Klein–Gordon control (V_φψ = 0) gives at most 1.9e-15.
- **Mechanism.** The constraint's (k² + V_φφ)⁻¹ is the same Yukawa kernel that Lemma S produces.
- **So.** The cuscuton's own perturbations carry no independent data, but the cuscuton *mediates* instantaneous influence between fields that do. The referee had already said ACG's argument "applies to its particular degenerate scalar action" (`vR14-5:88`). This run shows that the coupled case leaks as well.

**Answer to (a).** Yes. Signalling happens whenever g ≠ 0: instantaneous, of strength g, ordered by the preferred time. Lemma C makes it unavoidable during every absorbed vacuum change.

### 4(b) Ghosts, gradient instabilities and strong coupling

**Mode count (checked, `r151_quadratic.out`).**
- The background equations reproduce 3H² = ½χ̇² + V + λ and g = −2Ḣ − χ̇² (κ = 1), i.e. `R145:196`.
- After solving the α and β constraints, the kinetic matrix of (ζ, δχ) is a³/2 · [[χ̇²/H², −χ̇/H], [−χ̇/H, 1]] (×½ from the x-average). Its determinant is 0.
- **So there is exactly one scalar degree of freedom with matter, and none without matter.** K_ζζ ∝ χ̇², and ζ is then auxiliary, with Z² coefficient ∝ g·k² (`r151_reduce.out:2`).
- **The projectable-Hořava scalar of RN L3 is absent**, because the local Hamiltonian constraint is kept for k ≠ 0.

**Reduced action (proved, closed form; checked).**
- With q = δχ − (χ̇/H)ζ (q = −(χ̇/H)ℛ):
  - A(k) = a³H²(3a²χ̇² + 2k²) / [4H²k² + a²χ̇²(6H² − g)]  (×½ average; `r151_dispersion.out:5`).
- **GR limit (g = 0):** A = a³/2, and M equals the flat-gauge Mukhanov–Sasaki mass exactly, with the same factor ½ (`r151_dispersion.out:4`, which shows M_GR − MS = −MS/2, i.e. M = MS/2).
- **Comparator (V via search summary).** ×4a² of [(k/a)²H² + P(3H² + P + Ḣ)] with P = χ̇²/2 is 4H²k² + a²χ̇²(6H² − g), identical to this denominator.
- **High k:** ω²a²/k² = 1 + O(a²H²/k²). There is no UV gradient instability, and the front speed is 1 (`r151_dispersion.out:7`).
- **Ghost (proved):** A < 0 iff g > 6H², for k < k_g = aχ̇√(g − 6H²)/(2H). A has a pole at k_g.
- **Tachyon (checked, frozen background, `r151_window.out`):** ω² < −H² appears for g ≳ 4–5H² (χ̇²/H² = 0.1), ≳ 3–4H² (χ̇²/H² = 1) and ≳ 1–2H² (χ̇²/H² = 3). V″ = H² moves the thresholds only slightly. Example: g = 5.9H² gives min ω² = −2.0e2 H² (χ̇²/H² = 1).
- **g ≤ 0:** no ghost and ω² > 0 in every sampled background, g/H² from −1000 to 0. This agrees with the cuscuton literature's ghost-freedom argument, which applies to its fixed sign (−g ∝ μ²|φ̇| > 0, comparator).

**Which g does the model produce?**
- A smooth vacuum *drop* with an exact reader has g = κρ̇_v/(3H) < 0 (proved, above). That is healthy.
- An upward change, or reader error, gives g > 0.
- **Checked** (`r151_homog_gsign.out:7,16,25,34,43`). R14-5's own runs reach g/H² of +3.3e2 to +1.0e3, with g > 6H² in 1.8%, 1.8%, 2.9%, 3.3% and 7.4% of step samples. These are reader excursions. The referee notes that H² < 0 at some of those points anyway (`vR14-5:41`).
- **So (b) holds only under a new reader condition, g < g_crit ≈ (1–6)H²** (price P-r15b, §5). That is stronger than the ρ̂ > 0 clamp.
- **Dust under a fast drop (checked, `r151_signal.out:1-3`).** When Ḣ > 0 (g < −κ(ρ+p)_nc), the jump factor in Lemma S is negative for k²/a² < 3Ḣ: −46 and −29 at g = −50H². The instantaneous response is reversed and amplified by |g|/Q̄.
  - I do not call this a ghost: the scalar test at the same g has A > 0. It is reading-level only.

**Static star (proved, from the closed form).** For static matter (χ̇ = 0), A = a³/2 independent of g. The lapse equation is g-independent at linear order (`R145:196`, C4). The star's potential is changed only at O(g r²) (suggested).

**Strong coupling.**
- **Checked** (`r151_reduce.out:last 2`). The auxiliary solution Z = −B₁/(2A₂) has denominator −4H²k² − a²χ̇²(6H² − g). It contains no 1/g, and its g → 0 limit is finite. A and M are analytic at g = 0. So the passage through g = 0 (`vR14-5:88`) is smooth at quadratic order.
- **The only degenerate point is D(k) = 0**, the ghost threshold.
- **Cubic order was not computed** (OPEN).
- **Non-perturbatively** (suggested; comparator Gomes–Guariento V): the pair H(x) − ⟨H⟩ and the CMC condition is second class, with bracket equal to the lapse operator −D² + Q̃. It is regular iff that operator is invertible, i.e. under H-pos.

**Answer to (b).**
- No extra local scalar, no UV gradient instability, and smooth at g → 0, all at quadratic order.
- But there is a proved ghost for g > 6H², and a tachyonic window for g ≳ 1–5H².
- These are reached by R14-5's unregularized reader. They are avoidable only by a further condition on the creation law.

### 4(c) Does the CMC foliation exist through collapse?

**Lemma F′, lapse floor (proved, given H-pos and sup Q̃ < ∞ on the slice).**
- From −D²N + Q̃N = S with ⟨N⟩ = 1 we have S = 1/⟨N₁⟩ > 0. This holds automatically, since N₁ > 0 (`R145:201`).
- At the minimum of N, −D²N ≤ 0, so Q̃(x_min)N_min ≥ S. Hence **N_min ≥ S / sup Q̃**.
- Maximal slicing has S = 0, so this floor is absent there. That is why the GR lapse collapses exponentially in that case.
- **Throat value.** On the limiting maximal surface r = 3m/2, K_ijK^ij = 6(C/r³)² = 0.889/m², with C = 3√3m²/4 (RECALLED; `r151_throat.out:1`). So N_throat ≥ 1.125·S·m². With S ≈ Q̄ ≈ 1.35H₀²:
  - N ≥ ≈ 1.5(mH₀)²;
  - 1.9e-46 for a solar-mass black hole (m = 4.93e-6 s);
  - 3.5e-33 for Sgr A* (m ≈ 21 s; arithmetic with H₀ = 2.27e-18 s⁻¹).
- **Checked** (`r151_throat.out`). In a 1D throat attached to a "cosmos", N_min/(S/sup Q̃) → 1.0000 by throat length 20m, for two cosmos values of Q̃. Maximal slicing in the same throat falls to 3.5e-33 at length 80m, consistent with Beig–Ó Murchadha's exponential collapse (V).
- **Correction to R14-5.** "Lattice time freezes / N → 0" (`R145:51,222,227,303`) becomes: lattice time **slows to N ≈ S/Q̃_lim**, it does not stop. Over a Hubble time the throat's proper time advances by about (mH₀)²·t_H, so the model never evolves the interior beyond the limiting surface (reading).
- **E-curvature stays bounded** (proved, same hypotheses). tr E = 3g/N − 4λ, so |3g/N| ≤ 3|g|·sup Q̃/S ≈ 2.7(|g|/Q̄)/m² in throats. That is about 6e-6/m² if |g|/Q̄ ~ 2e-6 (suggested magnitude). There is no new curvature singularity at the limiting surface.
  - I had suspected one, from g/N with N → 0 exponentially. Lemma F′ removes it.

**Existence (comparator V; not proved).**
- In GR, global CMC foliations can fail. Chruściel–Isenberg–Pollack build vacuum cosmological spacetimes with no CMC Cauchy surface. Isenberg–Rendall give Einstein–dust spacetimes with a CMC slice but no covering CMC foliation.
- Gerhardt's theorem needs compact Cauchy surfaces, barriers and the timelike convergence condition (`vR14-5:64`).
- Here the slicing is physical, so a failure of existence means the model has no solution, not merely a bad gauge (reading).
- On intervals with g ≡ 0 the model is GR, and CMC there is a chosen clock law (`vR14-5:25`). The GR counterexamples are spatially compact and engineered. Their relevance to a near-FRW lumpy universe is open.

**Answer to (c).**
- Through black-hole formation, the lapse stays positive with an explicit floor, and the E-stress stays bounded (proved under H-pos).
- Global existence of the CMC foliation through structure formation remains a hypothesis, with GR counterexamples in other settings. So (c) is not "clean"; it is OPEN.

### 4(d) The vacuum the model needs: can it live with the grid zero-point (w ≥ 0)?

**Lemma V (proved; sympy, `r151_gridvac.out:1-2,5-6`).**
- Let the grid vacuum be a uniform, isotropic stress at rest in the site frame (= CMC normals, `R145:167`): T_grid = ρ_v nn + p_v h, with constants ρ_v and p_v and any w. Matter is separately conserved.
- Then ∇·(E + κT_grid) = 0 holds iff:
  - p_E = g′/N − λ − κ(ρ+p)_v, and
  - λ̇ + g′θ_n = 0.
- That is, E′ := E + κT_grid is a Lemma-C fluid with uniform energy density Λ̃ = λ + κρ_v and parameter g′.
- Homogeneously, **g′ = −2Ḣ − κ(ρ+p)_matter**, and (λ + κρ_v)˙ + 3Hg′ = 0 for any a(t).
- **The vacuum's (ρ+p)_v does not enter any observable.** Geometry depends only on G − κT_matter = E′.
- The P-T reader sees ρ_v as a constant and subtracts it (`R145:101`), whatever p_v is.
- **Correction to R14-5 K5** (`R145:317-320`). The value g ≈ −κ(ρ+p)_v ≈ 1e122 H² comes from applying the H-T formula (`R145:196`) to a vacuum that, with fixed site density, is *not* conserved: its energy is created with the sites. That Planckian "g" is E's own share, N(λ + p_E) = g′ − κN(ρ+p)_v. It is N-dependent and unobservable. The observable g′ is not Planckian.
- This extends R11-3's refereed V2/V3 absorption (`vR11-3:51`) to the nonlinear zero-mode-released model.

**Two readings of the source bridge (`AX:187`).**
- **(d-i) Resolved.** The vacuum stress is a c-number site-frame source with no conservation law of its own. Its energy and momentum imbalance is exchanged with the creation/E sector.
  - Then the model coexists with the grid zero-point for **any** w. No w = −1 vacuum and no pairing are needed. P-vac (`R145:338`) is replaced by the bridge statement in this bullet.
- **(d-ii) Priced.** The vacuum must conserve its own momentum (R13-3 Lemma G′: creation injects energy, no momentum).
  - Its Euler equation is (ρ+p)_v ∂_r ln N = 0 (`r151_gridvac.out:3`, checked). That contradicts the CMC lapse in any potential well (N − 1 ≈ Φ_N, `R145:216-220`) unless **(ρ+p)_v = 0** in the site frame.
  - Routes to (ρ+p)_v = 0:
    - **exact boson–fermion pairing on identical bands**, so that ρ_v = p_v = 0 (`C5_R11-3_report.md:41`; O3 refereed: the FS M1 lattice SUSY escape, with the qubit-pairing test INCONCLUSIVE, `TESTS.md:2399-2404`);
    - **one** tuning of (ρ+p)_v. That is one condition, not R11-3's two (`vR11-3:45-47`), because ρ_v itself is absorbed by λ.
  - The flat-band M-vertex w = −1 (`vR11-3:41`) is a dispersionless partition artifact, not a physical resolution (reading).
- Which reading holds is set by the source/action bridge. It is not decided here.

---

## 5. Prices (named, none adopted)

| # | Price | Axiom text touched | Status |
|---|---|---|---|
| **P-r15a** | **Instantaneous influence of strength g** (Lemma S), present in every absorbed vacuum change; ordered by the preferred time | `AX:57` (nearest-neighbour rule; here a simultaneous slice-wide response); `AX:186` (arrow/time metric) | proved within 𝒵 at linear order; **the FAIL candidate** |
| **P-r15b** | **Reader stability condition:** the creation law must keep g < g_crit ≈ (1–6)H² (no fast upward vacuum changes; no reader overshoot) | `AX:186-187` (P-T) | new; stronger than P-r13d |
| P-r15c | H-CMC-exist stays a hypothesis; GR has counterexamples | `AX:116-130` (no time metric) | carried |
| P-vac′ | The vacuum stress has no separate momentum conservation (d-i). Otherwise (ρ+p)_v = 0 by pairing or one tuning (d-ii) | `AX:187` | replaces P-vac |

---

## 6. Notes for the referee

**Items to check:**
1. **Lemma S:**
   - the synchronous-gauge E-fluid terms (R14-5 §4.5 equations; I re-derived the gauge transformation, δN^CMC = −ξ̇, and the tilt sign);
   - the jump formula;
   - whether an external impulse F is an admissible signalling source. A conserved device's own stress adds a localized δ(ρ+3p) source, which also couples through G_Q̄.
2. **Is preferred-time-ordered instantaneous influence "signalling" under `TESTS.md:4936-4937`?** The reading lists signalling as a pathology. No closed loops arise.
3. **H-act:** whether S_E = ∫√h(g − Nλ) represents the k ≠ 0 sector of 𝒵. The model does not impose the trace equation, but Lemma C reproduces the same p_E.
4. **A(k) and the ghost threshold g = 6H²:** the closed form, and the identification with the cuscuton+scalar denominator.
5. **Lemma F′:** the minimum-principle floor and the throat constant 0.889/m² (RECALLED C).
6. **Lemma V:** the D1/D2 sympy, and whether (d-i) is a legitimate reading of the model's own imposed equations.

**Strong-word check:**
- "Signalling": instantaneous change of a gauge-invariant local observable outside the light cone, at linear order, for g ≠ 0, in class 𝒵 with dust. Not closed loops.
- "Unavoidable": during intervals with λ̇ ≠ 0 (Lemma C), under H-imp/H-T.
- "Ghost": the scalar-matter test, frozen background, quadratic order, g > 6H².
- "Cannot collapse": given H-pos and bounded Q̃.
- "Resolved" (d): only under reading (d-i).

**What would change the picture:**
- an argument that the impulse source cannot be localized in the presence of the E-sector (I see none);
- a cubic-order computation (strong coupling);
- a regularized reader with g < g_crit throughout transitions;
- a CMC existence theorem for near-FRW lumpy data in this modified theory;
- the bridge decision between (d-i) and (d-ii).

## 7. Files

- Report: `S/R15-1_report.md`.
- Scripts and outputs: `S/scripts/r151_*.py/.out` (the .pkl files are intermediates).
- Downloads: `S/downloads_acg/` (untrusted; text extraction only).
