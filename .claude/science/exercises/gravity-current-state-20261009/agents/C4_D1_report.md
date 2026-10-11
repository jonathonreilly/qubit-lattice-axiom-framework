# Campaign C4, lane RD, probe D1: can a gapless-dressed band carry the SLAC face cusp? Report

**Provenance.** Worker: Claude Opus 5.5 (same model family as the supervisor). Ran 16:23Z to about 16:55Z on 2026-10-11. Not refereed. No repository files were edited.

**Scratch folder:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/D1/`

| Script | Output | What it does |
|---|---|---|
| `d1_kink_1d.py` | `d1_kink_1d.out` | Puts the exact SLAC band into the on-shell one-loop self-energy (1D gapless boson, vertex orders n = 1, 2, 3). Measures the face slope of Σ_os and compares it with s·K. Also covers the marginal log law. |
| `d1_kink_2d.py` | `d1_kink_2d.out` | The same face-slope test in d = 2 (gradient coupling, d + 2a = 3) |
| `d1_selfconsistent_1d.py` | `d1_selfconsistent_1d.out` | Solves E = ε0 + Σ_os[E] self-consistently. (a) kinked bare band: dressed slope = Z × bare slope. (b) nearest-neighbour bare band, started from exact SLAC: the kink decays to 0. (c) marginal coupling: the kink is erased logarithmically. |
| `d1_inverse_1d.py` | `d1_inverse_1d.out` | (i) The inverse problem ε0 = E_SLAC − Σ_os[E_SLAC]: its hopping tail is 1/Z times SLAC's. (ii) Σ_os of an analytic band is analytic in k, including at marginal coupling. |
| `d1_gapped_touch_1d.py` | `d1_gapped_touch_1d.out` | RC B2's remaining corner: a band touching a **gapped** continuum exactly at the face. Same Lemma K law; with the nearest-neighbour vertex, Z = 0 and a √δ cusp. |

## Reading against the FIXED lines

**PASS: not met.** No dressed band in the class has an exact SLAC face cusp with finite residue. Lemma K below proves that impossible.

**FAIL (bounded): supported, pending the codex sol referee.**
- **The face cusp needs Z = 0.** For a single band with a positive-spectral-weight self-energy whose continuum is parametrized regularly, the band's normal slopes on the two sides of the face satisfy E′(±) = Z·(the same quantity). So with finite residue the band is differentiable at the face, and a SLAC cusp is impossible. This is PROVED (same-family) for the rainbow / SCBA classes, gapped or gapless. For a general Herglotz Σ it is PROVED given the parametrization hypothesis, which is ARGUED.
- **Where Z = 0, the cusp still has the wrong form.** This is CHECKED for the rainbow class:
  - marginal coupling gives a +C|δ|log(1/|δ|) term;
  - a touching gapped continuum gives +C√δ;
  - sub-marginal coupling gives |δ|^{d+2a−1}.
  Each of these has the opposite sign to SLAC's Λ-cusp and dominates its linear term. Self-consistently, any kink is erased.
- **Fermi-sea mediators** give no exact band at all on an open set with ∇E ≠ 0. PROVED (elementary; it uses standard Lindhard support).

**Bounded to:**
- a single scalar matter band, in any d ≥ 1;
- nearest-neighbour or finite-range (Lipschitz-in-k) vertices;
- a mediator that is a gapless boson with a subsonic face, a gapped boson touching at the face, or a Fermi sea;
- self-energies of the rainbow / SCBA type with the dressed intermediate band, or a Herglotz Σ admitting a Lipschitz continuum parametrization.

**Not covered:**
- multi-band matter with a symmetry-protected crossing at the face (lane RI territory);
- non-local vertices or bare bands, which simply move the kink;
- vertex corrections whose dressed vertex is non-Lipschitz in k (ARGUED absent, via the Ward identity).

## The setting

- **Dyson equation.** E(k) = ε0(k) + Σ_os(k), where Σ_os(k) = Σ(k, E(k)).
- **Spectral form.** Σ(k, λ) = ∫ dμ(ξ) w(k, ξ; λ) / (λ − Ω(k, ξ)), with w ≥ 0.
- **Rainbow / SCBA case.**
  - ξ = q, or (q, x) when the intermediate continuum is kept;
  - Ω(k, q) = E(k−q) + ω(q) (+ x), using the **dressed** band, so the threshold is self-consistent;
  - w = |g(k, q)|² times the intermediate spectral density.
- **Notation.**
  - D := E(k) − Ω(k, ξ) < 0 is stability; for a subsonic gapless mediator, D → 0 only as q → 0, so the band sits on its soft-emission threshold.
  - K(k) := ∫ w/D² = −∂_λΣ|_os from the pole term, and Z = 1/(1 − ∂_λΣ) = 1/(1 + K) (exactly so when w does not depend on λ).
- **The SLAC face cusp.** At a face point k_f = (π, k_⊥), the band has normal slopes ±s with s = βπ/E_f. The slope jump is −2s ≠ 0.
- **Vertex power law.** A nearest-neighbour vertex to a gapless field has |g|² = |P(q)|²/(2ω) ~ |q|^{2a}. Here a = n − ½, where n is the order of vanishing of the trigonometric polynomial P at q = 0. Then:
  - Z > 0 ⇔ d + 2a > 2;
  - d + 2a = 2 is marginal: d = 3 with direct (photon-like) coupling, or d = 1 with gradient coupling;
  - Σ_os itself is finite ⇔ d + 2a > 1.

## (1) Analytic structure near the face, and which cusps are possible

### Lemma K (kink transfer). PROVED, same-family, unrefereed

**Hypotheses.** Let E be Lipschitz near k_f with one-sided normal derivatives E′(±). Assume:
- ε0 is differentiable at k_f;
- for μ-a.e. ξ, w(·, ξ; ·) is Lipschitz in (k, λ) with bound ≤ L·W(ξ), and Ω(·, ξ) is Lipschitz;
- both are differentiable at (k_f, E_f) for μ-a.e. ξ;
- **(UI)** the families W/D(k,·)² and W/|D(k,·)| are uniformly integrable for k near k_f. This is uniformly finite residue.

**Conclusion.**

Σ_os′(±) = A + B + E′(±)·∂_λΣ|_os, with

A = ∫ ∂_k w / D,  B = ∫ w ∂_kΩ / D²,

and A and B do not depend on the side. Therefore

**E′(±) = Z(k_f)·(ε0′ + A + B),**

which is side-independent. E is differentiable at the face.

*Proof.*
1. Write the difference quotient as ∫[(w_t − w_0)/(t D_t) − w_0 (D_t − D_0)/(t D_t D_0)].
2. Bound 1/|D_t D_0| ≤ ½(1/D_t² + 1/D_0²).
3. Every integrand is then dominated by a uniformly integrable family and converges a.e., so Vitali's theorem applies.
4. (D_t − D_0)/t → E′(±) − ∂_kΩ, and w's quotient → ∂_k w + ∂_λ w·E′(±).
5. Collecting the E′(±) terms gives ∂_λΣ.
6. Solve E′ = ε0′ + Σ_os′ for E′. ∎

**Notes.**
- **Rainbow and SCBA-pole classes.** Here ∂_kΩ = ∂E(k_f − q). Rademacher's theorem gives that this exists for a.e. q because E is Lipschitz, and the band's own kink sits on a null set of q. A subsonic margin D ≤ −κ|q| near q = 0 makes W/D² ≤ C|q|^{2a−2}, so UI ⇔ d + 2a > 2 ⇔ K < ∞ ⇔ Z > 0.
- **No analyticity is used.** Herglotz positivity is used only to give 1/Z ≥ 1. Even without it, a kink needs 1/Z = 0, a double root, which is not a finite residue.
- **The mechanism in words.** The band's own corner enters the self-energy only through the external energy (the λ channel). There it produces the **opposite** corner, of size −K·J. The intermediate states see the corner only on a null set of momenta, and integration smooths it. So J_E = −K·J_E, which gives J_E = 0.
- **This closes lane RC B2's open corners** for these classes: gapless continua, and a gapped continuum that touches along the face. B2 needed joint analyticity; Lemma K needs only Lipschitz regularity and finite Z.

### Checks of Lemma K's slope law (the self-energy gets a V-cusp Σ_os′(0+) = +sK when SLAC is inserted)

**1D, gapless boson, c = 2, s = 0.9529** (`d1_kink_1d.out`)

| Vertex order | K | Z | Predicted sK | Measured slope at δ = 1e-4 | Correction |
|---|---|---|---|---|---|
| n = 2 | 0.36678 | 0.7316 | 0.349497 | 0.349464 | −0.328δ (regular) |
| n = 3 | 1.03513 | 0.4914 | 0.98636 | 0.98631 | regular, O(δ) |

**2D, gradient coupling, d + 2a = 3** (`d1_kink_2d.out`)
- K = 0.08328, sK = 0.07762.
- The finite-difference slope / sK is 0.985, 0.973, 0.954, 0.923 at δ = 0.006 to 0.05.
- The deviation is about 0.50·δlog(1/δ) at all four δ, which is the predicted δ²logδ soft term.

**1D, gapped mediator touching at the face (RC B2's case)** (`d1_gapped_touch_1d.out`)
- Vertex b = 2: slope/sK = 0.99855 at δ = 1e-5.
- Vertex b = 3: slope/sK = 0.99999 at δ = 1e-5.

### Self-consistent checks (`d1_selfconsistent_1d.out`)

- **(a) A kinked bare band is dressed to Z times its kink.** Bare slope 0.952891, Z = 0.785810, dressed slope 0.748791 against Z·s0 = 0.748790, at N = 4096. The ratio is 1.00000.
- **(b) A nearest-neighbour bare band (2 − cos k), with the iteration started from exact SLAC.** The kink decays by 0.4010 per step; the prediction is 1 − α(1+K) = 0.4018. The fixed point has face slope −3e-8, which is the fit floor, and exponentially decaying Fourier coefficients (5.7e-17 at r = 20).

### Cusp catalogue (answering (1))

| Situation | Shape of the dressed dispersion near the point | Label |
|---|---|---|
| Smooth subsonic point, any IR power, including marginal | **No k-non-analyticity at all.** The soft threshold is a singularity in the energy (Σ − Σ_os ~ (E−λ)^{d+2a−1}, with a log at integers), not in momentum. For an analytic band, Σ_os is analytic: Fourier coefficients 2.5e-2, 5.9e-4, 2.5e-5, 7.3e-8, 2.6e-10, 1.0e-12 at r = 1, 3, 5, 9, 13, 17 for n = 1 (`d1_inverse_1d.out` ii) | CHECKED; ARGUED (polar-coordinate argument) |
| A pre-existing kink, Z > 0 | Kink × Z (Lemma K), plus a soft correction \|δ\|^{d+2a−1} (δ²log\|δ\| when d+2a−1 is even) | PROVED / CHECKED |
| Marginal, d + 2a = 2 (Z = 0, infraparticle) | Inserting SLAC gives Σ_os − Σ_f ≈ +Cδlog(1/δ), with C = s g²/(2πc(c−s)²): predicted 0.069159, measured 0.069159. Self-consistently the slope at distance δ is s0/(1 + C′log(1/δ)) → 0, so the kink is **erased** (grid: s0/slope grows by 0.046–0.050 per unit log(1/h); leading-log C′ is 0.044–0.048) | CHECKED |
| Sub-marginal, 1 < d+2a < 2 | +\|δ\|^{d+2a−1}, which dominates the linear term (wrong form and sign). For d+2a ≤ 1, Σ_os diverges | power counting, SUGGESTED |
| Gapped continuum touching at the face, nearest-neighbour vertex (b = 1) | K grows as 1/cut, so Z = 0. Σ_os − Σ_f = +0.2441√δ, checked over 5 decades: a V-type square-root cusp | CHECKED |
| Sonic (Cherenkov) surface \|∇E\| = c_s | Damping onset Im Σ ∝ ε^{(3d−5)/2+2a}, with ε = \|∇E\| − c_s. It sits on a level set of \|∇E\| (a sphere for SLAC), never the face, and is not a slope jump | SUGGESTED (power counting) |
| Fermi sea (d ≥ 2) | At every \|q\| < 2k_F, particle–hole pairs exist at arbitrarily low energy. So Im Σ(k, E(k)) > 0 wherever ∇E ≠ 0 and the vertex is a nonzero trigonometric polynomial: there is no exact band | PROVED (elementary) |
| Fermi sea (d = 1) | 2k_F pairs at low energy let the band at the face, which is the band maximum, decay to π − Q. An analytic vertex cannot vanish on the open set of allowed Q, so Im Σ > 0 | PROVED (elementary) |

**Is the SLAC kink attainable? No.** With Z > 0 the dressed band is differentiable at the face (Lemma K). With Z = 0 the induced singularity has the wrong form and the wrong sign, and it erases the kink.

## (2) The infrared: is finite Z compatible with the cusp?

**No (PROVED within the class).** Lemma K can be read as a dichotomy: a face cusp J_E ≠ 0 requires the uniform-integrability hypothesis to fail at the face, i.e. Z(k) → 0 there. Under the vertex power law that means:
- d + 2a ≤ 2 (the infrared catastrophe, at every k);
- or a sonic face, s = c_s, where D ~ q² and K diverges for low vertex order;
- or a threshold touching with too little vertex suppression (b = 1 above).

The finite-Z part of the reading is therefore unattainable. The Z = 0 corners also fail, on the residue clause and, in the rainbow class, on shape as well.

**Physical reading.** Dressing a particle with soft quanta smooths a corner in its energy curve by the fraction of the particle that is still bare. It never sharpens a smooth curve into a corner. When the particle is all cloud (Z = 0), the corner is wiped out completely.

## (3) Construction attempt: the inverse problem

**Set-up.** Given the target E = SLAC on the zone and any mediator (ω, w), the Dyson equation fixes the bare band uniquely: ε0 = E − Σ_os[E].

**Result (PROVED from Lemma K; CHECKED).**
- ε0 must carry the face kink J_E/Z = 2s(1+K).
- Its hopping tail is therefore t_r ≈ (−1)^r s(1+K)/(πr²). This is SLAC's own 1/r² tail amplified by 1/Z.
- Measured r²(−1)^r t_r ratio ε0 : SLAC = 1.3401, 1.3564, 1.3632, 1.3656, 1.3664 at r = 8 to 128, against 1+K = 1.36678, with N = 8192 (`d1_inverse_1d.out`).
- No trigonometric-polynomial (nearest-neighbour) ε0 solves it.

**Freeing the vertex.** A jump in A can supply the kink only if w(k, q) itself has a face kink in k. That is a non-local (1/r² in the matter leg) vertex: the non-locality moves into the vertex rather than disappearing.

**More mediators, gapped plus gapless, or several channels.** Lemma K is linear in the channel measure, so the conclusion is unchanged.

**The inverse problem has no solution in the stated class.** This also answers whether a tuned mediator dispersion can work: no. The mediator dispersion enters Σ_os only through Ω and the UI bound, and neither can create a k-jump. A mediator with its own face kink also smooths out under the q-integral, because its kink set meets the soft point only on a null set.

**Routes this analysis leaves standing** (outside D1's single-band class):
- **(i) A symmetry-protected two-band crossing at the face** (the C1 two-band touching), dressed by a gapless continuum.
  - Lemma K does not forbid it: the cusp comes from a double root, not from Σ.
  - Dressing keeps a symmetry-protected crossing and multiplies its slopes by Z (SUGGESTED).
  - B1's identity-theorem proof does not apply to the dressed sides, because Σ is non-analytic at the threshold, which here coincides with the band.
  - Whether the sides can be exactly SLAC is OPEN. It is an over-determined problem (infinitely many Taylor conditions against finitely many nearest-neighbour parameters), and the partner-band interaction obstruction from C1 is still unresolved. This belongs with lane RI.
- **(ii) Non-local vertex or bare band.** This works trivially, at SLAC's own price.
- **(iii) Z = 0 infraparticles.** Excluded by the reading, and by shape in the rainbow class.

**Side remark (SUGGESTED, not needed for the reading).**
- If the dressed band is real-analytic in the open interior (bootstrap not done), then exact SLAC on *any* open interior set propagates by the identity theorem to the whole open cube.
- Lemma K then forbids the face.
- So the open-set-including-the-face wording is probably not a restriction.

## Against the supervisor expectation

| Expectation | Outcome |
|---|---|
| The soft-emission threshold gives a cusp of the wrong form, a branch-point power law set by the coupling, or a vanishing residue. FAIL (bounded) | **Confirmed, with a sharper mechanism.** With Z > 0 the threshold makes **no** k-cusp at all: the singularity is in energy, not momentum. A face cusp is only ever inherited from the bare band, multiplied by Z (Lemma K). Coupling-set power laws (\|δ\|log, \|δ\|^{d+2a−1}, √δ) appear only where Z = 0, and they have the wrong sign. The same lemma also closes RC B2's gapped-touching corner, which was not anticipated. |

## Labels

**PROVED (same-family, unrefereed):**
- Lemma K for the rainbow and SCBA-pole classes (dressed intermediate band, Lipschitz vertices, UI ⇔ uniform Z > 0), and its general Herglotz form given a Lipschitz continuum parametrization;
- the corollary that a face cusp needs Z(k_f) = 0;
- the inverse-problem formula J_{ε0} = J_E/Z and its non-locality;
- the Fermi-sea no-exact-band statements (d ≥ 2, and d = 1 at the face).

**CHECKED:**
- the slope law Σ′(0+) = sK: 1D n = 2, 3; 2D gradient coupling; 1D gapped touching b = 2, 3;
- self-consistent Z-renormalization of a kink (ratio 1.00000);
- kink decay at rate 1 − α(1+K);
- the marginal log coefficient (5 digits) and logarithmic kink erasure;
- the √δ cusp at a Z = 0 touching;
- the inverse-problem tail ratio → 1+K;
- analyticity of Σ_os for an analytic band.

**ARGUED:**
- the parametrization hypothesis for the exact Σ (asymptotic completeness; the dressed vertex is Lipschitz by the Ward identity Γ(k,k) = ∂_k G⁻¹);
- the polar-coordinate analyticity of soft emission at smooth points.

**SUGGESTED:**
- the Cherenkov exponent;
- the sub-marginal shape;
- interior rigidity;
- that symmetry-protected crossings survive dressing with Z-scaled slopes.

**OPEN:** dressed two-band face crossings with exact SLAC sides (lane RI).

**READING:** "dressing shrinks corners by Z and never makes them". The location of the non-locality: bare band or vertex.

**COMPARATORS:**
- Vitali convergence and Rademacher;
- Bloch–Nordsieck / van Hove infrared catastrophe (Z = exp(−∫|g|²/2ω³));
- Lindhard particle–hole support;
- polaron threshold behaviour and the Cherenkov threshold (standard condensed-matter results);
- lane RC B1/B2.

**Scope of strong words.** "Impossible" applies only within Lemma K's hypotheses. "Exact" is used only for algebraic identities and theorem conclusions.
