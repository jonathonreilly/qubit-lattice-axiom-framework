# Panel F, GR / gravitational-wave lens: statement (2026-10-13)

**Panelist.** Claude Opus 5.5, GR/GW lens. Same model family as the supervisor and the C5 workers; not independent. Unrefereed.
**Read.** The axioms in full (`AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`, 233 lines); `TESTS.md:9146-9379` (F1–F5 and referee records); `rR19-34` (summary, §3.3–§6); `vR19-21` (items 1–6); `rR19-21:175-193` ((S_loc), Bianchi); `rR19-15:120-140` (Lemma H); `rF1:50-52, 149, 236-290`; `rF2:75-100`; `rF3:89, 192`; `PRICE_NOTE.md:1-60, 660-682`; header of `scripts/C5/R18-5/dirac.py`. Here `P/` = `.claude/science/exercises/gravity-current-state-20261009/`, `rX`/`vX` = `P/agents/C5_X_report.md` / `_referee_verdict.md`.
**My arithmetic.** `gr/gr_numbers.py` → `gr/gr_numbers.out` (checked arithmetic; constants RECALLED).
**Labels.** proved / checked / suggested / reading / comparator; RECALLED means from memory.

---

## Part 1. Plain words

**Verdict on the rule: sound, with conditions.** In Einstein's theory, a uniform stretch of space is only a change of coordinates, so it cannot change any mass. The rule restores that for one quantity, the fermion's mass, on a grid that otherwise breaks it. Under the "match observations" standard the rule is close to unavoidable. It is not enough on its own, though. It has to be an operator in the law, not a clause saying "this does not gravitate". It has to cover both kinds of shear the cube allows, and only one of them has been computed. And it does not cover a second Earth channel of the same size (R19-21's), which still rests on an OPEN subtraction.

### (a) What is "grid stretching"?

- The sites never move. The axioms give fixed points of Z³ with nearest-neighbour adjacency and say nothing about distances (`AX:37-41`). "Stretching" is a **metric field**: a field that says how much physical distance one hop covers in each direction. It changes how matter hops.
- The root registers it as the SF flow: each band's momenta are slid along a flow that, near zero momentum, has exactly the effect of a metric change (`rR19-15:124-127`). In this framework "the cell got longer in x" and "the metric field changed" are the same statement.
- **On a fixed grid this is physical; in GR it is not.** In GR a uniform, static stretch can be undone by relabelling the coordinates. Nothing local can detect it. On a fixed grid it cannot be undone, because the grid is an absolute ruler: a uniform stretch is a real change in the shape of every cell, as seen by matter that hops on the cell. That is the whole problem in one line. **The grid is a ruler GR does not have, and the hazard measures how visible that ruler is to matter.**
- F1 found the continuum version of this exactly. If photon and fermion momenta are moved by one common volume-preserving map, the loop is just relabelled and the strain Hessian is zero. In the continuum such a map exists, and that is GR's relabelling invariance. On the periodic Brillouin zone no such map exists (`rF1:50-52`, proved there; the F1 referee notes the volume lemma needs an origin-fixing hypothesis, `TESTS:9288`). The nonzero Hessian is the grid failing to be relabelling-invariant.

### (b) Why does the grid give fermions extra mass?

- A fermion put naively on a grid comes with unwanted copies, the "doublers", at the corners of momentum space. The Wilson-type term in the root's band (`M = m + W_x + W_y + W_z`, `dirac.py:3-5`) gives those copies grid-scale masses, which is its job.
- That same term breaks chiral symmetry, the symmetry that would forbid a mass for the real fermion. So quantum loops push the real fermion's mass up by a fixed amount. On the root's edge this is δm·a = +0.04186 e² (`rR19-34:12`) ≈ 3.8e-3, i.e. **about 0.4% of the grid scale, roughly 5e16 GeV, about 1e20 times the electron mass** (checked, `gr_numbers.out`, with a = ℓ_P).
- So "huge" is right. "About the grid's own energy scale" overstates it by the coupling: the push is the grid scale times α-sized factors, not the grid scale itself. The "critical mass" cancels it. That cancellation is a tuning to about 1 part in 1e20 for the electron.
- Under stretch the push changes only at **second order** in the stretch. Cubic symmetry forbids a first-order change from a traceless stretch (proved: the E_g and T₂g representations contain no invariant). That is why F1 measures a Hessian.

### (c) Grid versus fermion size (a = Planck length, a reading per `AX:189-190`)

| object | size (ħ/mc) | grid steps across |
|---|---|---|
| electron | 3.9e-13 m | 2.4e22 |
| up quark (2.2 MeV) | 9.0e-14 m | 5.6e21 |
| proton (Compton) | 2.1e-16 m | 1.3e19; its charge radius spans 5.2e19 steps, about 6e59 sites in volume |
| top quark | 1.1e-18 m | 7.1e16 |

(checked, `gr_numbers.out`)

- A real fermion is enormously smooth on this grid. It lives within about 1e-22 of the centre of the momentum zone.
- It does not "feel" the grid through its own extent. It feels it through its virtual cloud: loop fluctuations at all momenta up to the grid scale. That cloud is where the extra mass, and its strain dependence, come from.

### (d) How is a fermion built on this grid?

- **Supplied, not derived.** One site carries one qubit, M₂(C) (`AX:47`).
- The 4-component Wilson-type Dirac band (`dirac.py:3-5`), and the 22.5 Dirac fields placed on one edge, are downstream content. The axioms list "the staggered-Dirac/finite-Grassmann realization" as an open gate outside axiom content (`AX:178`). Kinetic branches are explicitly not axiom content (`AX:114-130`).
- **Counting modes (reading, RECALLED for the fermion–qubit maps).** One qubit holds at most one fermionic mode. In three dimensions, local fermion-to-qubit maps need extra gauge structure.
  - 22.5 four-component Dirac fields need 90 complex modes per Dirac "site".
  - So either a Dirac site is a block of about 100 or more qubit sites, or the multi-component structure is supplied.
- **Why that matters from my lens.** The hazard scales as 1/a_f, where a_f is the fermion's own cutoff length.
  - A block of a few ℓ_P changes nothing that matters.
  - The Earth row would pass with no rule only if the fermion cutoff were below about 8e10 GeV (a_f ≳ 1.6e8 ℓ_P; checked arithmetic).
  - A cutoff that low would bring cubic-anisotropy artifacts near current astrophysical limits (suggested; not computed).

### Accuracy of the pasted explanation

**Right:**
- The doubler/critical-mass setup.
- "The correction was set for the unstretched grid, so it no longer cancels exactly."
- "A tiny leftover mass that depends on the stretch": +½·H·h² per fermion, about 1e-17 eV at h = 1e-21 (checked).
- The GW170817 conclusion, **conditional** on:
  - the canonical mapping;
  - a = ℓ_P;
  - the U = 1 / Psym build. The F1 referee recorded OPEN, because the registered texts do not fix the interacting lift (`TESTS:9283-9290`).

**Wrong or overstated:**

1. **"Drag."** Wrong mechanism.
   - Drag means friction: energy is taken out of the wave. This effect is a **stiffness**. It acts as a mass for the wave inside matter, which makes waves below a cutoff frequency **evanescent**: they die out without dissipating and are mostly **reflected**, the way a plasma reflects radio waves below its plasma frequency.
   - Numbers (checked):
     - |m_g| ≈ 3.6e-9 eV in rock, versus ħω ≈ 1.2e-13 to 1.7e-12 eV over GW170817's 30–400 Hz band.
     - Decay length ≈ 55 m; about 1.7e5 e-folds along a 9,300 km chord.
   - The Earth would act as a mirror, not as molasses. Even waves from overhead would meet a near-node at the ground: the amplitude at the surface is about 2e-4 of the incoming wave at 100 Hz (F2 row 2, `rF2:96`, a half-space estimate). So the conflict does not even need a source below the horizon.
   - "Added up over all the matter" is also off. It is a local stiffness proportional to local density, not a cumulative sum of small drags.
   - **The plain comparison:** without the rule, all matter, gases included, would behave toward gravitational waves like a solid about 1e27 to 1e28 times stiffer per particle than rock (checked: 1.5e27 eV per nucleon versus 0.19 eV per nucleon for 1e11 Pa rock).
2. **"…as a passing gravitational wave or the strain inside the Earth does."**
   - Half wrong. A passing GW is a traceless stretch, which is right.
   - "The strain inside the Earth" is not a GR object. The Earth's static field in the standard (harmonic/isotropic) gauge stretches space **equally in all directions** at leading order, plus a slowing of clocks, with no traceless part. In GR a static traceless "strain" is a choice of coordinates.
   - The GW170817 conflict concerns **the wave's own stretch inside the Earth's matter**, not any static strain of the Earth.
   - (On the grid there is no coordinate freedom. Whether the static field of a mass carries a traceless stretch relative to the grid is a real, uncomputed question. See Part 2 §3.)
3. **"The grid tries to give them a huge mass, about the grid's own energy scale."** About 0.4% of the grid scale, not the grid scale itself (see (b)). Acceptable as plain speech if "times the force strength" is added.
4. **"What Einstein's theory already says"** (as framed in F5(d), `TESTS:9365`): **correct in content, wrong as a mechanism.**
   - GR has no grid and no critical mass. It never cancels anything here.
   - It says a uniform stretch is a relabelling of coordinates, so no rest mass can depend on it. Only gradients of the stretch (tides) and a material's own elasticity act locally.
   - The rule copies that outcome for one operator. It is not what GR does.
5. **"Fermions stay exactly as light as they are, however the grid is stretched."** Overstated. The rule as defined (`TESTS:9329`) fixes the **critical point**: a massless fermion stays massless at every uniform stretch. Physical masses still shift by about (α-sized)·h² of themselves (the multiplicative residual, F5(b)(i)), and there are gradient corrections. Both are tiny. Correct one-liner: **"Stretching the grid cannot give a fermion mass."**

**Corrected version (paste-ready):**

> **The setup.** A fermion on a grid comes with unwanted copies. The standard fix makes the copies very heavy, but it also removes the symmetry that keeps the real fermion massless. So quantum effects push the real fermion's mass up by a fixed amount, roughly the grid's energy scale times the strength of the force: here about 0.4% of the grid scale, some 10^20 times the electron mass. The root cancels this push with a fixed correction, the "critical mass", tuned on the ordinary grid.
>
> **The problem.** A passing gravitational wave stretches distances slightly more in one direction than another. In Einstein's theory a uniform stretch is only a change of coordinates and cannot change any mass. On a grid it can, because the grid is a fixed ruler: the size of the push depends on the shape of the cells. The correction tuned for cubic cells no longer cancels exactly, so every fermion's energy rises by an amount proportional to the square of the stretch. A wave cannot stretch matter without paying that energy, so matter resists the wave like an extremely stiff solid, about 10^27 times stiffer per particle than rock. Inside the Earth, waves at LIGO's frequencies would die out within about 50 metres and mostly bounce off. GW170817 reached both LIGO sites through 9,000–11,000 km of rock, and it was seen. This holds for the most natural build of the root's strain law (the root's texts do not yet fix that build uniquely) and assumes the grid spacing is the Planck length.
>
> **The rule.** Do the cancellation for the actual cell shape: wherever the grid is stretched, use the correction that keeps a fermion massless on that stretched grid. In one sentence: stretching the grid cannot give a fermion mass. Fermion masses still change by a harmless, tiny fraction of themselves. The rule is one piece of a larger requirement, that matter must not see the grid's shape, and other pieces (one Earth channel of the same size) are not yet covered.

---

## Part 2. Technical

### 1. Static uniform TT strain: gauge in GR, physical on the grid

- **GR (proved, standard).** A constant h_ij solves the linearized vacuum equations with zero Riemann tensor. The map x^i → x^i − ½h_ij x^j removes it.
  - A point particle's action −m∫√(−g_μν ẋ^μẋ^ν)dτ, at rest in TT gauge, is −m∫dt, independent of h_ij.
  - In the detector's Fermi frame a GW is the tidal field ẍ^i = ½ḧ_ij x^j. Matter couples through Riemann (∝ ω²h), never through h itself.
- **Grid (reading).** The fixed lattice frame X^I = x^I is a set of Stückelberg fields frozen in unitary gauge. Any matter operator that depends on g_ij other than through the covariant combination g^{ij}k_ik_j sees δ_IJ as a second metric.
  - The strain-dependent additive mass is such an operator.
  - F1's lemma pair (`rF1:50-52, 216-235`) is precisely the statement that the lattice torus admits no volume-preserving relabelling. That is the momentum-space form of explicit diffeomorphism breaking.
- **Consequence (proved at linear order, standard).** A matter-energy term that depends on uniform strain is a no-derivative potential for h_ij inside matter: a medium-frame, Lorentz-violating mass term for the TT graviton.

### 2. The canonical mapping is GR's elastic-medium formula

- **Derivation (proved, linear order).** L = (1/64πG)(ḣ_ij ḣ_ij − ∂_k h_ij ∂_k h_ij) − μ_s h_ij h_ij/4 gives ḧ − ∇²h + 16πG μ_s h = 0, so **m_g² = 16πG μ_s**.
  - For a real solid with shear modulus μ_shear, the strain at fixed material coordinates is ε_ij = ½h_ij. That gives μ_s = μ_shear.
  - Comparators (RECALLED): the graviton mass from a solid's shear modulus in solid inflation (Endlich–Nicolis–Wang 2013); GW absorption by shear viscosity at rate 16πGη (Hawking 1966); Dyson's 1969 seismic response.
  - Real rock: |m_g| ≈ 2–4e-23 eV (checked). That is negligible, and it is why GR matter is transparent to GWs.
- **The repo's form** m_g²a² = 16π μ_SF, with μ_SF = Σ⟨ψ̄ψ⟩a³·w·Hess_t (`rF1:247-252`), is this formula with G = a².
  - It holds if t is the metric-perturbation amplitude (h = t·diag(1,−1,0)). Lemma H's flow v = ½h·f does correspond to the metric amplitude at small k (reading).
  - I reproduce F1's Earth value independently: **3.64e-9 eV** (checked, `gr_numbers.out`).
- **Legitimacy.**
  - The structure is legitimate under two conditions:
    - (i) the h_ij that the fermions' hopping responds to (SF/UD) is the same h_ij that propagates as the GW, i.e. universal coupling;
    - (ii) its kinetic term is normalized to the observed G.
  - Neither is a free choice under "match observations". If (i) failed, LIGO's mirrors and light would not respond to GWs. If (ii) failed, Newton's law would be wrong. So the "emergent graviton, naturalness diagnostic only" escape (`PRICE_NOTE.md:22`) does not, in my reading, remove the hazard: action equals reaction for any graviton with an action.
  - **The load-bearing conditional is the size**: a_f = ℓ_P (`AX:189-190` lists Planck-length self-consistency as open). The hazard is ∝ 1/a_f.
- **What the mapping does not cover** (suggested; F2 already flags it, `rF2:78-79`).
  - A position-dependent mass term without dynamical Stückelberg fields breaks ∇_μT^μν = 0 at first order in h wherever density varies, e.g. the Earth's surface. R19-21's Noether identity shows the exchange term with the lattice frame, E_I∇^νX^I (`rR19-21:188-189`).
  - With a frozen grid, E_I = 0 is not an equation of motion. So an Einstein-type field equation becomes over-determined in matter gradients unless the strain dependence vanishes.
  - This gives the rule **a second, structural justification** beyond GW170817: any GR-like graviton needs it for consistency.
- **vDVZ.** The term acts only on spatial components in the medium frame (the m₀ = 0 class of Lorentz-violating massive gravity; Rubakov 2004, Dubovsky 2004, RECALLED). The vDVZ discontinuity is not the operative issue for the static potential at linear order. The helicity-0/1 sector in density gradients is (above).

### 3. "Strain inside the Earth": the wrong picture, with one real open question behind it

- **GR.** At 1PN in harmonic gauge, g_ij = (1 − 2U)δ_ij. There is no static traceless strain from the Earth, Sun or Galaxy at that order. Traceless pieces are gauge, or O(U²).
- **Grid (suggested, uncomputed, potentially the largest hazard).** On the grid there is no gauge freedom. Which coordinates the lattice frame realises for a static mass is set by the framework's graviton law.
  - If the lattice frame carried a static traceless strain of order U, the uncovered additive channel would give δm_e ≈ ½·H·U²: about 7 MeV at U_Earth ≈ 7e-10, and about 1 GeV at the Sun's potential at 1 AU (checked arithmetic, conditional). That is far beyond any equivalence-principle (EP) or local-Lorentz-invariance (LLI) test.
  - With the rule, the additive part is gone. The species-dependent marginal residuals (z″·h² per species) give EP violations of about 1e-2·U² ≲ 1e-20, below MICROSCOPE's ~1e-15 (estimate).
  - **The rule therefore matters more for static fields than for GWs, if the lattice frame is not isotropic-gauge-like.** This is a reason for the rule, and a question to settle.

### 4. Is "in GR rest mass ignores shear" the right justification?

- **Partly.** The true statement is general covariance plus the Einstein equivalence principle (local Lorentz invariance): rest mass is a scalar, and a uniform h_ij is a coordinate change.
- **"Ignores shear" is too broad.** GR matter does respond to shear:
  - extended bodies feel tides;
  - solids have elastic shear energy, which gives the 16πGμ_shear in-medium term above, about 4e-23 eV for rock.

  What GR forbids is a dependence of **rest mass on uniform strain**, and more generally any dependence on the strain relative to a background ruler.
- **The right justification under Jon's standard** is observational, with GR as the comparator that satisfies all of these at once:
  - (i) GWs cross the Earth and reach ground detectors with the predicted amplitude (F2 rows 1–2: μ_ρ ≲ 1.5e-29 eV² m³/kg in rock, massive sign per vF2);
  - (ii) no anisotropic or composition-dependent mass shifts (LLI and EP tests), which matters if static traceless strain exists in the lattice frame;
  - (iii) action and reaction (§2).
- **Better wording for F5(d):** "In GR a uniform strain is a change of coordinates, so the zero-momentum gap of every species is strain-independent. The rule imposes this for the additive mass."

### 5. Verdict: **sound with conditions**

Conditions (each reading unless marked):

- **C1. Operator, not source-side.**
  - State P-R19-34a as a local term in the law, ψ̄ψ·f(h), with f fixed by criticality at each uniform h. That is how `rR19-34:177` words it.
  - Do **not** substitute P-R19-31b (⟨ψ̄ψ⟩ as an (S_loc) background), a "does not gravitate" subtraction. It leaves the rest-mass–shear coupling in the law (`rF1:290`). That is a one-way coupling: matter feels h but does not push back. No action gives that, and it violates the Noether/Bianchi identity.
- **C2. Both cubic shear channels.** Cubic symmetry allows two independent quadratic invariants, E_g and T₂g. Only E_g has been computed. T₂g is excluded in F1, F3 and F4 (`rF1:149`; `rF3:89,192`; `rF4:61`).
  - A GW from a generic direction carries both.
  - Unequal Hessians would also make matter **birefringent** for GWs, direction- and polarization-dependent.
  - The rule's "every uniform strain" wording covers both, but F5 must check T₂g explicitly.
- **C3. The rule alone does not close the Earth row.**
  - R19-21's matter channel, in which local matter shifts v and so the Wilson sea's stiffness, gives |m_g| = 1.42e-9 eV in Earth-density matter (`vR19-21:25-26`, arithmetic confirmed). That is the same order as F1's 3.6e-9 eV, and about 5e3 above F2's 2.9e-13 eV.
  - It is covered only by (S_loc), whose fixed reading is OPEN (`vR19-21:28`).
  - Nothing shows P-R19-34a removes it. The rule fixes the critical point, not the m-linear slope of the vacuum stiffness.
  - F5's RULE-WORKS clause "every residual channel is below F2's Earth row" has to include it.
- **C4. Name the price honestly.**
  - The rule is a renormalization condition: a function m_c(h) on the 5-dimensional strain space, per species, per loop order. It is "number-free" only under the law-functional convention (vR19-24 as recorded at `TESTS:9081`: "DYNAMIC-CLAUSE by construction" on the literal convention, else OPEN).
  - Its content is "the grid is invisible to the mass operator", i.e. local Lorentz invariance for one relevant operator.
  - The honest single clause is **"every relevant operator's renormalization condition holds on every uniformly strained law"**. That covers (Σ), the fermion additive mass, the scalar mass², and the R19-21 channel in one statement, and it is what GR gets from one symmetry.
- **C5. Local version.**
  - The gradient corrections are fine for every physical wave. (ka)² ≈ 1e-81 at 100 Hz (checked). Static solar-system gradients are similarly negligible.
  - The rule is adiabatic in time for ωa ≪ 1.

### 6. Strongest argument from my tradition

The continuum zero F1 proved (`rF1:50-52`) is GR's diffeomorphism Ward identity: a uniform traceless strain is a volume-preserving relabelling, so it changes nothing local. Observation demands that identity at the level of 1 part in about 1e8 in μ_ρ for the mass operator in rock (F2). It demands it far more strongly if static traceless strain exists in the lattice frame. And GR's field equation needs it for consistency (Bianchi).

A grid that fails it is visibly a preferred ruler. Something has to restore it. Of the restorers on the table:
- P-R19-34a is the only one that is local, untuned (no tuned number), and an operator rather than a one-way subtraction;
- P-F3a (a* tuned to 6e-9) and P-F4a (signed path mixtures at λ* ≈ −13 to −273) are tunings.

### 7. Steelman AGAINST my verdict

- **(a) It is imposed GR, not derived.** The rule reinstates general covariance by hand, operator by operator and loop by loop. A theory that must decree, for each relevant operator separately, that matter cannot see the grid has not explained why gravity couples universally; it has assumed it. Infinitely many conditions dressed as one clause are a fine-tuning in disguise (the vR19-24 objection, `TESTS:9081`).
- **(b) A structural fix may exist that makes the rule unnecessary** (suggested; RECALLED for the symmetry facts).
  - Chirally protected edges forbid an additive mass at every strain by symmetry, with no clause:
    - staggered fermions keep the remnant U(1)_ε for any nearest-neighbour hopping amplitudes;
    - Ginsparg–Wilson/overlap fermions keep the GW relation for any kernel.
  - The axioms' own open gate names a staggered realization (`AX:178`), and one fermionic mode per site matches one qubit per site better than a 4-component band does.
  - Caveat: whether the SF flow preserves bipartite hopping is untested. Axis-mixing flows generate even-length hops that would break U(1)_ε.
  - If a protected edge kept the root's refereed rows, it would dominate P-R19-34a.
- **(c) The hazard itself is OPEN** on the registered texts (F1 referee: an admissible unitary lift moves the Hessian through zero, `TESTS:9283-9290`). A rule written for a not-yet-fixed law may be patching an artifact of one build.

My reply:
- (c) cuts both ways, since the lift can also enlarge the value.
- (a) is a fair statement of the price, not a reason to reject the rule under "match observations".
- (b) is the real competitor, and I would prefer it if it holds.

### 8. What would change my mind

- **To "unsound":**
  - F5 finds m_c(h) not unique;
  - or it cannot be made local beyond O(a∂h);
  - or a residual covered by nothing (T₂g mismatch, Pauli/clover strain dependence, multiplicative channel) exceeds the Earth row.
- **To "sound but insufficient, needs more prices":**
  - the R19-21 channel survives after (S_loc) is settled;
  - or the lattice-frame static field of a point mass has an O(U) traceless part and the per-species marginal responses exceed LLI bounds.
- **To "unnecessary":**
  - a chirally protected edge reproduces the root's rows;
  - or the framework's fermion cutoff is shown to sit below about 8e10 GeV without conflict;
  - or it is shown that the field the fermions' hopping responds to is not the propagating TT field (but then the coupling to detectors must be re-explained).

### 9. One concrete next test (pre-registrable)

**G1. Earth-row closure budget for the rule package, with both cubic shear channels.**

- **Plain question.** With P-R19-34a adopted as an operator, does everything else that makes Earth-density matter stiff against a GW fall below F2's Earth row? Or does GW170817 still fail through a channel the rule does not touch?
- **Setting.**
  - The R18-9 root D1(0.909103708, 0.555604226), photon Gph(2.9435), and F1's law (B1, Psym).
  - Branches: F3's dressing at a = 0 and at a*, and F4's J and SL families.
  - Earth matter: ρ = 5500 kg/m³, Y_e = 0.5, nucleon weight 13 light-quark units (`rF1:248-251`).
- **Probes.**
  - (a) The T₂g additive-mass Hessian before the rule, and its ratio to E_g. Report the GW birefringence the ratio would imply without the rule.
  - (b) After P-R19-34a, confirm the E_g and T₂g additive Hessians are 0 in every branch (≤ 1e-10).
  - (c) R19-21's matter-shifted vacuum-stiffness channel (`vR19-21:25-26`), recomputed on this root:
    - with no (S_loc);
    - with (S_loc) listing ⟨φ†φ⟩ and ⟨ψ̄ψ⟩;
    - with P-R19-34a's knock-on included.
  - (d) The multiplicative residual m_f·z″, and the strain dependence of F3's Pauli/clover term.
  - (e) A Noether check at a density step (a 1D half-space), with and without the package: the first-order lattice-frame exchange term E_I∇X^I.
  - Each item is converted to μ_ρ (eV² m³/kg) and compared with 1.5e-29 (massive sign) and with F2 row 2.
- **FIXED readings.**
  - **CLOSED:** every item is ≤ 1.5e-29, checked, and the Noether term vanishes at O(h).
  - **CLOSED-WITH-(S_loc):** as CLOSED, but (c) is below the bound only with (S_loc).
  - **NOT-CLOSED:** any item exceeds the bound after the package. Name it.
  - **OPEN:** otherwise.
- **Expectation.**
  - (b) is zero by construction, and (d) is far below (m_f·a suppression).
  - (a) is nonzero and unequal to E_g.
  - (c) exceeds the bound without (S_loc), at about 1.4e-9 eV.
  - So CLOSED-WITH-(S_loc): the fermion rule is necessary but not sufficient.

---

**Numbers used (checked, `gr/gr_numbers.out`).**
- δm = 4.7e16 GeV (0.38% of 1/a).
- Earth |m_g| = 3.64e-9 eV.
- Decay length 54.8 m; 1.7e5 e-folds on a 9,293 km chord.
- Ground near-node ≈ 2.3e-4 at 100 Hz.
- Rock's own shear term: 2–4e-23 eV.
- Lattice stiffness per nucleon 1.5e27 eV, versus 0.19 eV for rock.
- (ka)² ≈ 1e-81 at 100 Hz.
- Rule-free pass would need 1/a_f < 7.6e10 GeV.
