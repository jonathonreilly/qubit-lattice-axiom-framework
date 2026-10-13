# Panel F statement: lattice field theory lens (Wilson, staggered and overlap fermions; anisotropic tuning)

**Panelist:** Claude Opus 5.5, same model family as the supervisor and every C5 worker. Not refereed. Written 2026-10-13, 18:24Z to 18:55Z. No repository file was edited.

**Read.**
- The axioms in full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (AX), lines 1–233.
- `TESTS.md:8927-9379`, covering the C5 close and F1–F5.
- The F1 report and its verdict; the R19-34 report (lines 50–196) and its verdict; the R19-31 report (lines 120–150) and its verdict; the R19-24 verdict; R16-1 (lines 30–100); S26 (lines 60–80).
- `PRICE_NOTE.md:1-40,500-622,655-682`; the header of `P/scripts/C5/R18-5/dirac.py`; `sublum.py:1-60`.

**Script.** `lattice/sizes.py`, with output in `lattice/sizes.out`. It uses the repo's D1 class unmodified.

**Labels.** proved, checked, suggested, reading, comparator. RECALLED means from memory, with no source opened today.

---

## Part 1: plain words

**The short version.**
- The extra mass comes from the particular way this root removes the grid's duplicate fermions (a "Wilson-type" term). It is not something every grid does.
- Its dependence on stretching is a short-distance artifact. Its size, and even its sign, depend on details the root does not fix.
- The proposed rule is the standard lattice-physics fix, used routinely when the grid spacing differs between directions. I call it **sound with conditions**:
  - the rule must be stated as a measurable condition;
  - it must cover every direction of stretch;
  - its natural companion, that every particle's light cone also follows the stretch, is not yet in it and has to be checked.
- A cleaner route exists. Fermion constructions with a built-in chiral symmetry make this extra mass zero at every stretch, with no rule. The axioms already list one such construction as an open gate (staggered fermions, AX:178).

### (a) What is "grid stretching" here?

- The sites do not move. The axioms fix the sites and their neighbours (AX:37-41). In grid units the spacing is 1 by definition, so "the spacing changed" means nothing on its own.
- What changes is a field living on the grid, the graviton. It alters how matter hops from site to site, so that long-wavelength particles move as if lengths were longer in one direction. That is an effective metric. Rulers are made of matter and light, so a stretch is visible only through how particles and light propagate.
- For long waves this is clean: they spread over 10^19 to 10^22 sites, see a smooth metric, and cannot tell the grid is there.
- For the shortest waves, near the grid scale, "stretching" has no unique meaning.
  - A cube-shaped grid cannot be uniformly stretched at its shortest wavelengths. F1 proved there is no volume-preserving stretch of this kind on the grid's momentum space (`rF1:52`; the referee requires the origin-fixing hypothesis, vF1 item 4).
  - So each rule for the shortest waves is a choice: R19-34's "H-cov", the root's "SF" flow, F3's dressings, F4's path families.
- The extra-mass effect lives entirely in those shortest waves. That is why the answer moved from −0.040 (H-cov) to +0.097 (SF, the same units) and can be pushed through zero (`rF1:35-38`; vF1 item 1; `TESTS:9298-9303`).

### (b) Why does the grid give fermions extra mass?

**The doubling theorem.**
- A fermion placed naively on a grid comes in 2³ = 8 copies in 3D space, because a smooth periodic "momentum" function must cross zero at the zone edge as well as at the centre. This is the Nielsen–Ninomiya theorem (comparator, RECALLED).
- The root's D1 band has the same structure (checked): its symbol is odd and periodic with S(π) = 0, so it has the 7 extra copies (`sizes.out:4`).

**The Wilson fix.**
- The root adds a "Wilson term", a momentum-dependent mass that is zero for the real particle and large for the copies.
- On the R18-9 root, W(π) = 0.355/a, so the copies weigh 0.36, 0.71 and 1.07 /a. That is 4×10^18 to 1.3×10^19 GeV if a is the Planck length (checked, `sizes.out:2-3`).
- This mass is deliberate. It is how the copies are removed.

**The side effect: lost chiral symmetry.**
- A mass-like term in the law destroys the symmetry (chiral symmetry) that would otherwise forbid the real particle from acquiring a mass through interactions.
- Loops of photons and gluons then shift the real particle's mass by an amount proportional to coupling × (1/a).
- At one loop on this root, δm = 0.0419 e²/a (`rR19-34:86`):
  - QED: 3.8×10⁻³/a, about 4.7×10^16 GeV;
  - QCD-like coupling: 1.4–1.7×10⁻²/a, about 2×10^17 GeV (checked arithmetic, `sizes.out:5-8`).
- For comparison, a standard Wilson fermion in lattice QCD gives about 0.43 g²/a at one loop (comparator, RECALLED, Capitani's review). The root's value is about 10 times smaller, because its Wilson term is exactly zero inside the box |k| < 0.909.

**"About the grid's own energy scale."**
- This is directionally right but overstated: the shift is about 0.4% (QED) to 1.7% (QCD) of the grid scale.
- It is still 10^20 times the electron mass. Cancelling it at zero stretch needs one part in 10^20 for the electron (`sizes.out:10`). The root already pays this by fixing the critical mass at zero strain (`rR19-34:69`; `rF1:101`).

### (c) Sizes: the grid and a fermion

All with a = ℓ_P = 1.6×10⁻³⁵ m (checked, `sizes.out:11-18`).

| object | size | sites across | sites in its volume |
|---|---|---|---|
| electron (reduced Compton wavelength) | 3.9×10⁻¹³ m | 2.4×10^22 | about 10^67 |
| up quark (2.2 MeV) | — | 5.5×10^21 | — |
| top quark | — | 7×10^16 | — |
| proton (Compton) | — | 1.3×10^19 | — |
| proton (charge radius) | — | 5.2×10^19 | about 6×10^59 |
| hydrogen atom | — | 3×10^24 | — |

- A fermion is as large compared with the grid as the observable universe is compared with a large molecule.
- The grid is invisible to anything a fermion does, except through effects that grow like 1/a: the additive mass and the vacuum energy. That is exactly why only those channels feel the stretch at a dangerous level.

### (d) How is a fermion built on this grid?

- **The root's fermion is supplied, not derived.**
  - D1 is a 4-component Wilson-type band: h(k) = Σ s(k_j)α_j + (m + Σ W(k_j))β (`dirac.py:3-4`; `rR19-34:50`).
  - 22.5 copies of it, one for each Standard Model Dirac field, are placed on one edge by hand (`rR19-34:54`; S26:71).
  - The axioms say outright that they do not assert a Dirac carrier (AX:118-123), and they list "the staggered-Dirac/finite-Grassmann realization" as an open gate (AX:178).
- **Why 4 components (proved, standard algebra).**
  - A massive 3D Dirac Hamiltonian needs four mutually anticommuting matrices: three α's for motion and one β for mass. The smallest such matrices are 4×4.
  - One site's algebra, M₂(C) ≅ Cl(3,0) (AX:47-50), has only three: the Pauli matrices. That is enough for a massless 2-component Weyl particle, σ·k, but leaves no room for a mass or a Wilson term.
  - On a grid, Weyl points come in opposite-handed pairs (Nielsen–Ninomiya), so a lone Weyl fermion per site cannot exist. Removing the copies forces 4 components: two qubits' worth per site, or one component per site spread over a 2³ cell, which is the staggered construction.
- **Statistics are a second, separate gap (reading; comparator RECALLED).**
  - A qubit is a two-state system, but fermions anticommute.
  - Turning qubits into local fermions in 3D needs either non-local strings (Jordan–Wigner) or an extra Z₂ gauge constraint (exact bosonization; Levin–Wen-type emergent fermions).
  - Neither appears in the axioms.
- **The Standard Model is chiral, and that is a third gap** (reading; comparator RECALLED). A Wilson mass term ψ̄_Lψ_R is not SU(2)×U(1) gauge invariant. Treating "22.5 Dirac on a Wilson edge" as the Standard Model treats it as vector-like. F1 and R19-34 explicitly exclude the chiral edge (`rF1:149`; `rR19-34:74,76`). Their QED and QCD channels are fine; the electroweak sector is not covered by any of this.

### Accuracy of the pasted explanation

| sentence | verdict | correction |
|---|---|---|
| "the grid tries to give them a huge mass, about the grid's own energy scale" | **Half right.** | It is not "the grid" but this particular way of removing the copies (Wilson-type). Staggered and overlap grids do not do it. The size is 0.4–2% of the grid scale, about 10^16–10^17 GeV: still 10^20 times the electron mass. |
| "the law includes a correction, the critical mass … The root already does this on the unstretched grid" | **Right** (`rR19-34:69`; `rF1:101`). | — |
| "Stretch space … as a passing gravitational wave or the strain inside the Earth does" | **Acceptable** in plain words. | The stretch is a field on a fixed grid (an effective metric), not sites moving. |
| "The grid's push … changes a little … every fermion picks up a tiny leftover mass" | **Right for one choice; overstated as "the problem we found".** | The size and sign depend on how the shortest waves are stretched, which the root does not fix. The referee's recorded reading is OPEN, because a permitted dressing moves the effect through zero (vF1 item 6; F3, `TESTS:9298-9303`). Per fermion, the leftover is ½ × 0.024 e² × h²/a: about 10⁻²⁶ GeV for a gravitational wave (h ~ 10⁻²¹). The danger is the sum over matter, not any single particle. |
| "acts like a heavy 'drag' on gravitational waves" | **Wrong word.** | Nothing is absorbed or slowed by friction. The matter becomes *stiff*: it gives the graviton a mass inside it. With F1's Earth value |m_g| = 3.6×10⁻⁹ eV, every wave below about 0.9 MHz cannot propagate inside the Earth. It dies off within about 54 m and is reflected (checked arithmetic, `sizes.out:19`). The whole LIGO band is below that, so **"the Earth would act as a mirror"** is the right image, like the ionosphere reflecting AM radio. |
| "strong enough that GW170817 could not have passed through the Earth … yet it did" | **Right, with conditions.** | It holds on the U = 1 branch, the canonical mapping (`PRICE_NOTE:22`), one loop, the SM estimate, and F2's derived 1D medium model (not a published limit, vF1 item 3). The excess is 1.6×10^8 in μ (vF1 item 3), so the conclusion survives large changes in those inputs. |
| "what Einstein's theory already says" (as Jon framed it) | **Right, and it cuts both ways.** | In Einstein's theory a uniform stretch is locally just a change of coordinates, and rest mass is a scalar, so masses do not change. The rule imposes by hand what general covariance gives for free. Einstein's theory also gives matter a much smaller effect on waves: √(4πGρ) ≈ 1.4×10⁻¹⁸ eV in the Earth, or μ_ρ ≈ 4×10⁻⁴⁰. That is 11 orders below F2's bound (checked arithmetic, `sizes.out:21`). |
| "fermions stay exactly as light as they are, however the grid is stretched" | **Overstated.** | The rule guarantees one thing: a fermion that is massless at the critical point stays massless at every *uniform* stretch. It does not cover three things: (i) the mass-proportional part m_f·Z(h), a fractional change of order 10⁻³ × h²; (ii) whether each particle's light cone follows the stretch; (iii) the gradients of a non-uniform stretch, of order a·∂h, which are negligible. |

**Corrected plain version.**
- To remove the grid's duplicate copies of each fermion, the root uses a method (a Wilson term) that also removes the symmetry that would keep fermions light. Interactions then push every fermion's mass toward about 1% of the grid's energy scale. The root cancels this with a tuned "critical mass", set for the unstretched grid.
- A gravitational stretch is a field on the grid that changes how particles hop. It changes the push slightly, by an amount that depends on how the grid's shortest waves are stretched, which the root does not fix.
- On the root's most direct reading, the uncancelled remainder makes ordinary matter stiff to gravitational waves. The Earth would then be a mirror for the LIGO band, and GW170817, which came up through the Earth, would not have been seen.
- **The rule:** wherever space is uniformly stretched, set the critical mass for that stretch. A fermion that is massless on the flat grid then stays massless on the stretched grid. That is what Einstein's theory says automatically, here imposed by hand.

---

## Part 2: technical

### 2.1 Verdict on P-R19-34a: **SOUND WITH CONDITIONS**

**Why sound (comparator, RECALLED; reading).**
- This is the anisotropic-lattice procedure of lattice QCD. When the regulator breaks a symmetry the target theory has, you restore it by tuning every relevant and marginal operator that the lattice symmetry permits and the target symmetry forbids.
- On anisotropic lattices (Klassen 1998; the Hadron Spectrum Collaboration's anisotropic clover programme, Edwards–Joó–Lin 2008), m_c is re-tuned at each anisotropy ξ. So are the fermion anisotropy ν (the quark's speed of light) and the clover coefficients. The continuum results agree with isotropic lattices.
- P-R19-34a is m_c(ξ) promoted to a local field m_c(h(x)). The price is the same kind as the h = 0 critical mass the root already pays, extended rather than new.
- It is local: ψ̄ψ times an analytic function of the local h, with gradient corrections of order a·∂h. For LIGO wavelengths that is ℓ_P/λ ~ 10⁻⁴¹.
- It removes nothing observed (`rF1:291`).

**The F3/F4 results are what this tradition predicts (reading).**
- m_c is not universal. It is a power divergence, and every dimension-5 operator feeds it at order g²/a. In lattice QCD, switching on the clover term moves κ_c a lot (comparator, RECALLED).
- F3's dressing acts as a strain-dependent Pauli/clover term (`TESTS:9298-9303`), and F4's path families change the field-strength couplings. Both therefore move ∂²_h m_c.
- **Consequence:** "the grid's strain Hessian of the additive mass" is not a prediction of the framework. It is a coefficient that must be fixed by a renormalization condition. The rule is that condition.

**Conditions.**

**C1. State the rule on-shell, over all strain channels.**
- The statement in F5 is already right in form (`TESTS:9336`): the pole mass vanishes at m₀ = m_c(h).
- For confined quarks, use a PCAC or pion-mass condition, not a quark pole mass.
- It must cover all six strain components. Under proper cubic rotations, h = A₁ ⊕ E ⊕ T₂.
  - ψ̄ψ couples **linearly** to A₁ (the trace).
  - At O(h²) there are three invariants (A₁², E², T₂²), against two in the continuum (proved, character count). E and T₂ are separate tunings on the grid.
  - F1 and R19-34 computed only E_g (`rF1:149`; `rR19-34:76`).
- **The trace channel is first order.** Under H-cov, dilation gives dδm/dh = −δm (`rR19-34:97`), which is a pure change of units. Under SF it is not a unit change, so it must be checked.
- Codimension count through O(h²): 4 coefficients per gauge class per loop order (1 linear and 3 quadratic), with more at each higher order. Under the law-functional convention it is one clause with zero numbers (vR19-24 item 4).

**C2. Add the companion speed (light-cone) clause.**
- In anisotropic lattice QCD, tuning m_c(ξ) alone is never enough; ν(ξ) is tuned too.
- Here the analog is "P188 at every uniform strain": each field's dressed O(p²) form is Lorentz-invariant **with respect to the strained metric**. P188 itself is the zero-strain version (`PRICE_NOTE:606`).
- The packet already shows this channel is live:
  - scalar QED has a first-order strain response of its one-loop speed coefficient, ∂_hκ_xx = −0.196 e² (`rR19-31:135`);
  - the photon is birefringent at O(e²h) (`rR19-31:137-138`);
  - the fermion speed rows are open (vR19-31, strongest statement).
- Without this clause, "the grid stays invisible" fails at O(α·h) in a species-dependent coupling to strain.
- For gravitational waves this is negligible. For any **static** strain the grid registers, it is not (see 2.3).

**C3. The rule fixes only the additive part.**
- The multiplicative remainder is a fractional rest-mass anisotropy ½z″h², with z″ ≈ −0.072 e² on the Wilson root (`rR19-34:140`).
- It is harmless for the graviton mass (suppressed by m_f·a ~ 10⁻²⁰).
- It matters as a local Lorentz-invariance effect if static traceless grid strain exists: about 3×10⁻²¹ at h = 10⁻⁹. Clock-comparison bounds on anisotropic inertia are around 10⁻²⁷–10⁻²⁹ (comparator, RECALLED).
- F5(b)(i) sizes this residual only against F2's wave rows. It should also be sized against tests of local Lorentz invariance.

**C4. The rule is a background-field condition.**
- At the cutoff, graviton fluctuations have h ~ O(1).
- The rule therefore needs a background-field definition of "uniform strain" inside graviton loops. Lattice QCD defines m_c through a physical condition in the full fluctuating theory, so this is workable, but it is not yet written down (reading).

### 2.2 The strongest argument from my tradition: symmetry beats tuning

The cleanest lattice answer is not the rule but a fermion whose masslessness is protected.

**Staggered fermions.**
- They have one component per site, the axioms' own listed realization (AX:178).
- With continuous time (Z³ × ℝ), the protecting symmetry is the one-site shift, a discrete chiral symmetry that sends the staggered mass to minus itself (comparator, RECALLED: Kogut–Susskind/Susskind). Any translation-invariant uniform strain of the hoppings keeps it, so m_c(h) ≡ 0 at every uniform strain and every order.
- **Small correction to `rR19-34:113`** (reading, RECALLED). In continuous time the protecting symmetry is the shift, not U(1)_ε. U(1)_ε needs staggering in time too, and ψ†∂_τψ is not U(1)_ε-invariant. The conclusion δm ≡ 0 for per-axis amplitudes stands.
- Under SF in particular (suggested): the staggered E² is π-periodic in each k_j, so its SF flow commutes with the π-shifts. The strained operator then keeps only odd-length hops (bipartite), for E_g **and** T₂g. This is unchecked and is a natural F-series item.

**Ginsparg–Wilson / overlap fermions.**
- The protection is algebraic, holding configuration by configuration, so it survives any smooth strain of the kernel (comparator, RECALLED: Lüscher 1998).
- The cost is exponential locality, no worse in class than D1's Gevrey (super-polynomial) tails (`rF1:192`). The chiral gauge-theory problem remains.

**Maximal twist** is already shown to push the additive channel to O(e⁴h⁴/μ) (`rR19-34:128-141`).

The price of the chiral routes is real: leaving the root and recomputing every vacuum row (`rR19-34:182`), plus tastes for staggered. But they turn an imposed cancellation into a derived zero. **If Jon wants the rule to be a consequence rather than a clause, this is the route.**

### 2.3 Steelman against my verdict

1. **It is the hierarchy problem by fiat.**
   - In lattice QCD, m_c(ξ) is tuned because the lattice is a computing device whose spacing is sent to zero. Here a is physical, and the cancellation must be exact at finite a: to 10⁻²⁰ for the electron, for every strain value, in every channel, at every order.
   - A rule that cancels whatever the grid does in a channel carries no information about that channel.
   - Combined with C2 it amounts to "the low-energy theory at every strain is exactly the covariant one". That imposes infrared diffeomorphism invariance by hand, and the framework then predicts nothing about how gravity couples to matter.
2. **The trace channel is first order, not a Hessian.**
   - If a static Newtonian potential registers on the grid as an A₁ dilation of size Φ, the uncovered first-order shift is δm(0)·Φ. That is about 5×10^16 GeV × 7×10⁻¹⁰ ≈ 3×10⁷ GeV per fermion at the Earth's surface (suggested, arithmetic from `rR19-34:97`; `sizes.out:6`).
   - The rule must therefore carry the first-order A₁ piece exactly, and must do so consistently with redshift universality. That is more than "a strain-covariant Hessian".
3. **"One clause" hides an infinite tower.** That tower is 4 coefficients per class per order through O(h²), then the cubic invariants, then C2's speed tower (P73 is 4 per class, `PRICE_NOTE:507`). That is exactly what the axioms' "one fixed nearest-neighbour admissibility rule" (AX:57) was meant to avoid. The root's fermion is also already not nearest-neighbour (Gevrey tails), which is a separate tension with AX:57 (reading).

I keep "sound with conditions" because under Jon's standard a condition that matches observation and removes nothing observed is admissible as a named price, and the precedent (m_c at h = 0) is already paid. On cost I rank it **below** the chiral routes.

### 2.4 What would change my mind

**Towards unsound:**
- F5(c) shows that the rule's counterterm times the vacuum ⟨ψ̄ψ⟩ moves the root's rows beyond what (Σ) absorbs.
- The on-shell clause cannot be stated gauge-invariantly for the chiral electroweak sector on a Wilson edge.
- The test below finds an O(α·h) species-dependent cone response, the root registers static potentials as grid strain, and the result conflicts with equivalence-principle or local Lorentz bounds that the rule does not cover.

**Towards sound without conditions:** a symmetry of the root's own law that forces m_c(h) = m_c(0). For Wilson-type edges none exists (`rR19-34:110`); a chirally protected edge would supply one.

### 2.5 One concrete next test (suggested, for pre-registration)

**Title.** F6, strain-covariant light cone and trace channel on the root's SF law.

**Plain question.** After P-R19-34a, does each particle's light cone still follow the stretch, the same way for fermion and photon? And is the first-order trace (dilation) channel covered?

**Setting.**
- F1's law: U = 1, Psym, the R18-9 root D1(0.909103708, 0.555604226) and Gph(2.9435), Feynman gauge with a ξ check.
- F3's a* dressing as a branch: does the dressing that zeroes δm″ also move the cone?
- Fermion speeds: R16-1/R13-7's on-shell speed runner (`r1610_core.dirac_pt`, made per-axis as in `rR19-34`, on-shell check), on SF-strained symbols.
- Photon: Π_os^T as in `rR19-31:137`.

**Quantities.**
- (i) Δ_cone = ∂_t[c²_xx − c²_yy]_fermion − ∂_t[c²_xx − c²_yy]_photon at t = 0, per e², E_g. Repeat for T₂g.
- (ii) The SF isotropic-dilation slope δm′(0), against the pure-unit value −δm(0) (H-cov, `rR19-34:97`).
- (iii) The T₂g Hessian of δm, which F1 did not compute.

**Fixed readings.**
- **CONE-COVARIANT:** |Δ_cone| ≤ 1e-8 e² in E_g and T₂g, and (ii) equal to −δm(0) within 1e-8.
- **CONE-SPLITS:** report the values, and whether the strained P188 clause covers them. Size them against MICROSCOPE (η ~ 10⁻¹⁵) and the SME c_jk bounds under a **stated** mapping of static fields to grid strain.
- **OPEN:** otherwise.

**Expectation (mine).** CONE-SPLITS at 10⁻²–10⁻¹ e² per unit t, by analogy with R19-31's scalar −0.196 e². This is the strained Collins–Perez–Sudarsky–Urrutia–Vucetich mechanism (comparator, already in `TESTS:19`). So P-R19-34a would need the strained P188 as a companion.

**Alternative test, if Jon prefers derivation to clauses.** Build F1's SF law on a continuous-time staggered fermion. Check δm(t) ≡ 0 for E_g and T₂g, and recompute the four vacuum rows. That would show what leaving the Wilson edge costs.

---

**Summary of claims by label.**
- **Proved (short, unrefereed):**
  - the 4-component minimum for a massive 3D Dirac Hamiltonian;
  - M₂(C) holds only 3 anticommuting generators;
  - 3 quadratic cubic invariants against 2 in the continuum.
- **Checked:** every number in `sizes.out` (sizes, W(π), δm in GeV, the cutoff frequency and decay length, the general-relativity medium scale).
- **Suggested:**
  - the trace-channel size;
  - the SF-staggered bipartite preservation;
  - the F6 expectation;
  - the static-strain local Lorentz sizing.
- **Reading:** the verdict and conditions C1–C4.
- **Comparator (RECALLED):**
  - Nielsen–Ninomiya;
  - Wilson m_c ≈ 0.43 g²;
  - anisotropic m_c(ξ), ν and clover tuning;
  - Ginsparg–Wilson and Lüscher;
  - the staggered shift symmetry;
  - Collins et al.;
  - clock-comparison bounds;
  - exact bosonization.
