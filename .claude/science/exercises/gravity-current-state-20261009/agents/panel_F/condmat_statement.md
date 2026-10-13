# Panel F statement: condensed-matter / emergent-gravity lens

- **Who:** Claude Opus 5.5 panelist, the same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-13, 18:24Z to about 19:05Z. No repository file was edited and nothing was downloaded.
- **Paths:**
  - `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full;
  - `P/` = `.claude/science/exercises/gravity-current-state-20261009/`;
  - `rX` and `vX` = `P/agents/C5_X_report.md` and `C5_X_referee_verdict.md`;
  - `S/` = `scratchpad/C5/panel_F/condmat/`.
- **Read:**
  - `P/TESTS.md:9146-9379` (F1–F5);
  - rR19-34 and vR19-34 in full;
  - rF1:1-140; rF2:18-60; rF3:14-50;
  - rR19-15:100-160 (Lemma H);
  - rR19-21:1-60; rR19-31:50-70 and :196-222; rR19-27:1-40 and :185-200;
  - rR16-1:1-100; vR19-24;
  - S26:60-80; `PRICE_NOTE.md:15-30` and `:660-682`;
  - the `dirac.py` and `sublum.py` headers;
  - greps for staggered, chiral, trace and critical-mass prior art.
- **Scripts.** All of these are in `S/`. Each ran in under 1 s and used under 110 MB.
  - `cm_sizes.py/.out`, `cm_hops.py/.out` and `cm_condensate.py/.out`. These use unmodified copies of the archived `dirac.py` and `sublum.py`, kept in `S/arch/`.
  - `cm_solid.out` and `cm_powercount.out`.
- **Labels:** proved / checked / suggested / reading / comparator. RECALLED means from memory and not verified here.

---

## Part 1. Plain words

### (a) What is "stretching the grid"?

The grid cannot actually be stretched. The axioms fix the sites as the points of Z³ (`AX:37-41`). There is no "position" a site could move to, and no ruler outside the grid to measure it by.

What the calculations call "strain" is a change in the hopping rules. The rule for moving from site to site becomes slightly direction-dependent, so that waves travel as if the grid were stretched. Picture a fixed chessboard where only the rules for moving across the squares change.

This is how strain acts on electrons in real materials too. In graphene the electrons never see where the atoms are. They see only how strongly neighbouring atoms are linked, and strain changes those links. The electrons experience it as a direction-dependent speed (an effective metric) and as a fake magnetic field.

So "stretching" here is meaningful as an effective metric field, which is the graviton. It is not a change in site spacing.

Two cautions:
- In the C5 calculations the strain is put in by hand as a background. A field built out of the qubits themselves, with its own dynamics, is not derived. Its use as a graviton is conditional (`PRICE_NOTE.md:22`).
- A real crystal has phonons: the atoms move. This grid has none. Its "stiffness against stretching" is the energy of the fields living on it, not of moving sites.

### (b) Why does the grid give fermions extra mass?

A massless fermion has two halves, left-handed and right-handed, that do not talk to each other. A mass is exactly what makes them talk. If the law kept them apart by a symmetry (chiral symmetry), no mass could ever appear.

The trouble is that a grid cannot keep that symmetry while giving one fermion per field. Put a fermion naively on a cubic grid and you get 8 copies, one at each corner of the momentum cube (Nielsen–Ninomiya, RECALLED).

Wilson's fix adds a term that makes the 7 extra copies very heavy. On the root's edge each corner adds 0.355 grid units, so the copies weigh 0.36, 0.71 or 1.07 in grid units, about 4e18 to 1.3e19 GeV (checked). Those copies really are at "about the grid's own energy scale".

The cost of the fix is that it lets the two halves talk. Through quantum loops (virtual photons and gluons with grid-scale momenta), the real, light fermion then also picks up a mass:
- For QED on the root's edge: 0.0419 e² grid units = 0.0038 grid units ≈ 5e16 GeV. That is about 1e20 times the electron mass (checked, from rR19-34:13-14).
- For quarks the QCD loop is several times larger, an estimate.

So "huge" is right. For the copies, "about the grid's own scale" is right. For the light fermion's loop mass it is about 250 times too big: the loop mass is a fraction of a percent of the grid scale.

The root cancels this by hand with a bare "critical mass". In condensed-matter language, the root's fermion sits exactly on a topological phase transition: a trivial insulator on one side and a topological insulator on the other (comparator, RECALLED: the Wilson–Dirac band is the textbook lattice model of a 3D topological insulator). Masslessness there is a tuned point, not a protected phase.

### (c) How big is a fermion compared with the grid?

Take one site per Planck length (1.6e-35 m). Then a fermion's size, in sites across, is (checked):

| particle | sites across |
|---|---|
| electron (Compton wavelength) | 2.4e22 |
| light quark | ~5e21 |
| nucleon (Compton wavelength) | 1.3e19 |
| proton (charge radius) | 5e19 |
| top quark | 7e16 |

A fermion is a ripple spread over about 1e66 sites, not a thing sitting on one site.

At those wavelengths the root's law is exactly the continuum Dirac equation. Inside its "box" (momenta below 0.909 per site) the hopping is exactly linear and the Wilson term is exactly zero (`dirac.py:4`; rR19-34:50). A free electron never feels the grid. The grid reaches it only through loops, and that is where the extra mass and its strain dependence come from.

### (d) How is a fermion built on this grid?

Its structure is supplied, not derived. The root's fermion is a 4-component Dirac field with a 4×4 matrix law (`dirac.py:3-4`; class 𝒬_W, rR16-1).

The axioms give each site a qubit's algebra, M₂(C) ≅ Cl(3,0) (`AX:45-50`). They say Admissibility does not assert a "Dirac-square carrier" (`AX:120-122`). They list "the staggered-Dirac/finite-Grassmann realization" as an open gate outside the axioms (`AX:178`).

Three facts from my field bear on this:
- **A qubit is not a fermion.** On a qubit lattice in 3D, fermions are emergent excitations bound to an emergent Z₂ gauge field (Levin–Wen; Verstraete–Cirac; Chen–Kapustin; all RECALLED). That derivation is owed, and it is not trivial.
- **The axioms' own named route is staggered fermions.** These have one fermionic mode per site, which is the natural match to one qubit per site. Staggered fermions keep an exact chiral symmetry. The C5 root instead uses a Wilson-type edge, and that choice is the source of the strain problem.
- **The SM is chiral.** The "22.5 Dirac fields" (45 Weyl fields) on one Wilson edge is a way of counting fields for the vacuum calculations. It does not realize the electroweak couplings: a Wilson term pairs left and right fields that carry different SU(2)×U(1) charges, so it is not gauge invariant (rR19-34:74 leaves this uncomputed). That is a separate, known open problem. The only modern candidate I know of is mirror-fermion symmetric mass generation (Wen 2013; Wang–Wen; Tong's review; RECALLED). It wants 16 Weyl fields per generation, which means adding ν_R.

### Is the pasted explanation accurate?

**Right:**
- the grid pushes fermion masses up, and the root cancels this with a critical mass set at zero stretch;
- a direction-dependent stretch changes the push;
- the leftover is proportional to the stretch squared, it applies to every fermion, and summed over the Earth's matter it is large;
- the rule is "make the correction follow the stretch".

**Wrong or overstated:**
1. **"About the grid's own energy scale."** True of the doubler copies. The light fermion's loop mass is about 0.4% of the grid scale in QED, which is still about 1e20 electron masses.
2. **"As … the strain inside the Earth does."** The stretch that matters is the passing gravitational wave's. The Earth supplies the fermions, not the stretch.
3. **"Drag."** This is the wrong physics. The leftover acts as a stiffness, which is a mass for the wave inside matter. It is not friction.
   - Below a cutoff frequency (about 1e6 Hz in rock under the canonical reading, checked from F1's |m_g|), the wave cannot propagate at all. It dies off within about 55 m and is reflected.
   - This is how the ionosphere reflects long radio waves below the plasma frequency.
   - With the other sign the wave grows instead (an instability). In neither case is it drag.
4. **"GW170817 could not have passed through the Earth."** That holds only for the simplest version of the law, and under the conditional canonical reading.
   - The referee recorded F1 as OPEN, because an admissible unitary lift moves the effect through zero (`TESTS:9283-9285`).
   - F3 shows that zero needs tuning to about 6e-9.
   - The canonical mapping itself is conditional (`PRICE_NOTE.md:22`).
   - Accurate wording: "the simplest strained law the root admits gives a channel that conflicts with GW170817's passage through the Earth by about 1e8, if the stiffness is read as a graviton mass."
5. **"Fermions stay exactly as light as they are."** This overstates the rule. The rule re-cancels only the grid's own (additive) push, and only for uniform stretch. The real masses still change by about (coupling) × (stretch)² × (their own mass). That is harmless (see the technical part) but not zero.
6. **"What Einstein's theory already says"** (the F5 wording). This is right about rest mass: in GR a rest mass does not depend on a volume-preserving stretch, because uniform strain is a change of coordinates. But the rule does not make the grid obey GR. It imposes GR's answer in this one channel.

**Corrected version (short):**
> On a grid, fermions have a known problem. The grid's extra term that removes duplicate copies also lets quantum effects push every fermion's mass toward a large fraction of the grid's own energy, about 10^16–10^17 GeV if the grid cell is the Planck length. The root cancels this with a hand-set correction, the "critical mass", on the unstretched grid. A passing gravitational wave stretches space differently in different directions. That changes the grid's push slightly, so the correction no longer cancels exactly. Each fermion is left with a tiny extra mass proportional to the stretch squared. But the coefficient is Planck-sized, and summed over all the matter in the Earth it would make rock act like a mirror for gravitational waves, if the stiffness is read as a graviton mass. Then GW170817 could not have come up through the Earth to the detectors, yet it did. The proposed rule is to re-set the correction for the stretched grid at every stretch. Then the grid adds nothing to any fermion's mass however the grid is stretched, and the fermions' real masses change only by amounts proportional to themselves, which are far too small to see. It is a rule imposed, not something the grid does by itself.

### Verdict on the rule (strain-covariant critical mass, P-R19-34a)

**Sound with conditions.** It is the price of one corner of a three-way choice. On a grid like this you can have at most two of the following:
1. exactly one light fermion per field;
2. a symmetry that keeps it massless however the grid is stretched;
3. an ordinary local Hamiltonian on Z³ with one qubit per site.

The root chose 1 and 3, so it must pay for 2 by hand. The rule is that payment.

Lattice QCD does the same thing on lattices with different spacings in different directions: it re-tunes the critical mass for each anisotropy (comparator, RECALLED). That is how I know the rule is well defined for uniform stretch. It matches observations by construction in this channel.

My conditions are in Part 2 (§T6).

### Strongest argument from my tradition

In every material I know, a gap that stays zero however you squeeze the material is protected by a symmetry or by topology. Graphene's Dirac points and Weyl nodes move under strain but do not open. Nowhere is it kept at zero by a correction that follows the strain.

Where nothing protects it, strain moves the material off the critical point at the scale of its own band energies:
- semiconductor "deformation potentials" are a few eV per unit strain;
- strained HgTe and ZrTe5 are driven across topological transitions.

F1's result is exactly that generic behaviour, at a Planckian band scale (about 3e25 eV per unit strain², checked).

So the effect is real and expected, and only a symmetry or an imposed rule removes it. The symmetry routes each cost one of the three items above. The rule costs a by-hand clause.

### Steelman against my verdict

The rule is a renormalization condition dressed as law.
- In anisotropic QCD the anisotropy is a fake regulator setting. Here the stretch is the physical gravitational field. Re-setting the mass at every stretch means writing into the law a Planck-strength coupling between gravity and ψ̄ψ, chosen to cancel another one exactly, at every order.
- A framework that adds one such clause per leak predicts nothing about how matter responds to strain. "Matching observations" is then guaranteed, not tested.
- In my field, a material whose gap stays at zero under all strains with no symmetry would be called fine-tuned.

The opposite steelman, for "sound with no conditions": the standard is observations; every residual is negligible; the vacuum knock-on is absorbed by (Σ), which the program already uses; and every protected alternative costs more (twin copies, non-locality in time, or an extra dimension).

### What would change my mind, and the next test

**To "unsound":** if F5 finds that the rule's knock-on onto the vacuum's stretch stiffness cannot be absorbed, so the root cannot be re-solved. My order-of-magnitude estimate of that knock-on is Planckian, about 1.5e-3 grid units per field per cell (suggested). Or if no residual can be bounded.

**To "sound":** if one clause, "every zero-stretch renormalization condition holds at every uniform stretch", covers mass, speed and vacuum together without new numbers, and every residual is checked below the bounds.

**Next test (not in F5): the gluonic channel.** Most of the Earth's mass is the energy of gluons inside nucleons, not quark mass. A stretched grid renormalizes the strong coupling slightly differently along different axes. That shifts the QCD scale, and so the nucleon mass, in proportion to the nucleon mass itself.

Simple counting says such mass-proportional channels are safe by a factor of about 1e10 (checked arithmetic). Only channels enhanced by the Planck scale can reach GW170817's bound. The test confirms this for the channel that carries 99% of the Earth's mass. It is specified in §T8.

---

## Part 2. Technical

### T1. (a) What strain is in the registered texts (reading, with citations)

- **No displacement field exists.** Sites are Z³ with nearest-neighbour adjacency (`AX:37-41`). Kinetic laws, the time metric and dynamics are downstream content (`AX:114-130`).
- **SF strain (registered).** Each band's momenta flow along v = ½h·∇(E²/2), and the strained band energy is E∘Φ_t (Lemma H setting, rR19-15:127-128). For the interacting law, F1 uses D_t(k) = D(Φ_t(k)) with UD as its generator (rF1 §0).
  - On the box (s = k, W = 0) the Dirac flow is linear, v = ½h·k. The photon's flow is linear on its own box (|q| ≤ 2.94).
  - So **all species share one infrared metric at tree level** (proved: ∇(E²/2) = k wherever E² = k² + m²). Universality of the effective metric is built in at low momentum.
  - It fails only in the ultraviolet: the Dirac flow bends beyond 0.909 and the photon's beyond 2.94. Loops carry that mismatch into the infrared, which is F1's mechanism (rF1:50-53).
  - Comparator (RECALLED): this is Collins–Pérez–Sudarsky–Urrutia–Vucetich (2004). Ultraviolet Lorentz violation leaks into the infrared at O(α), unsuppressed by E/M_Pl. In analogue gravity the same thing appears as loss of a single shared metric in multi-component BECs (Barceló–Liberati–Visser).
- **H-cov** (rR19-31:56-60) writes cell lengths ℓ = (e^h, e^{−h}, 1), but implements them only as per-axis rescalings of hopping symbols. That is again a change of law, not of sites.
- **Trace (isotropic) strain** is handled differently. Per-site counterterms are fixed in lattice units, so H-cov dilation carries them with the sea: "the sea at a new spacing is the same law" (rR19-27:17-18; rR19-31:62-64,201).
  - Reading: the trace channel is protected by a real redundancy. Dilating everything is a change of units, and R19-34 checks d/dh δm = −δm (rR19-34:97).
  - That is why the traceless channel is the only open one. **P-R19-34a is the traceless analogue of the lattice-units convention that already covers dilation.** But no symmetry argument backs it: the E_g-strained law is not the same law (F1 proves no volume-preserving separable E_g flow exists on the torus, rF1:52).
- **Phonons versus gravitons (comparator, RECALLED).**
  - A crystal's strain is the gradient of the displacement Goldstone field, and uniform shear costs energy (the shear modulus).
  - A self-gravitating elastic solid gives the TT graviton a mass m_g² ≈ 16πG·μ_shear, the Lorentz-violating massive-gravity "solid" phase (Dubovsky 2004; Endlich–Nicolis–Wang). The program's canonical mapping m_g²a² = 16πμ (`PRICE_NOTE.md:22`) is the same relation with a² = G.
  - Kleinert's "world crystal" gravity had to postulate zero first-gradient elasticity to get Einstein gravity. That is the same zero-stiffness requirement the program faces, imposed there by postulate.
  - Real rock gives m_g ≈ 3e-23 eV by this relation (checked arithmetic, μ_rock ≈ 7e10 Pa RECALLED). F1's uncancelled channel corresponds to μ_eff ≈ 8e38 Pa, about 1e28 times stiffer than rock (checked, `cm_solid.out`).

### T2. (b) Masses on the root edge (checked unless stated)

All values are in grid units unless converted. With a = ℓ_P, 1/a = 1.22e19 GeV.

- **Doublers.** W(π) = 0.355204, so the corner valleys have m + n·W(π) = 0.355, 0.710, 1.066, i.e. 4.3e18 to 1.3e19 GeV (`cm_sizes.out:1`).
- **Light fermion's one-loop additive mass (QED, root):**
  - δm = 0.041858 e² = 3.84e-3 = 4.7e16 GeV = 9e19 m_e (rR19-34:13-14; converted here).
  - Its SF E_g Hessian is +2.424e-2 e² (rF1 §0; the referee confirmed the number for U = 1 with Psym, `TESTS:9284`).
- **Locality of the root's edge.** It is not nearest-neighbour. Its hop amplitudes have only odd harmonics and fall off sub-exponentially (Gevrey):
  - |s_r| = 0.11 at r = 3, 2.5e-6 at r = 31 and 3e-10 at r = 101;
  - |W_r| = 1.6e-5 at r = 31 (`cm_hops.out`).
  - Reading: on locality grounds an exponentially local Ginsparg–Wilson operator is no worse than the registered edge.
- **Topological reading (comparator, RECALLED).** M(k) = m + ΣW(k_j) with W ≥ 0 is a BHZ/QWZ-type mass.
  - For −W(π) < m < 0 the band is inverted at k = 0 only, which is the strong 3D-TI phase of the time-reversal-symmetric Wilson–Dirac model.
  - m = m_c is the transition.
  - Strain shifts the transition point (F1). Squeezed ZrTe5 and strained HgTe cross this kind of transition in experiment (RECALLED).

### T3. (c) Sizes (checked, `cm_sizes.out`)

| particle | m·a |
|---|---|
| electron | 4.2e-23 |
| u quark | 1.8e-22 |
| nucleon | 7.7e-20 |
| top quark | 1.4e-17 |

Sites across: 2.4e22, 5.5e21, 1.3e19 and 7.1e16 respectively. The proton's charge radius is 5.2e19 sites. All physical momenta lie deep inside the box, where the free law is exactly continuum Dirac (s = k, W = 0).

Per-fermion uncancelled mass shift: ½·Hess·e²/a·t² = 1.4e-17 eV at t = 1e-21. It is the coherent sum over n ~ 1e30 m⁻³ that acts as a medium stiffness.

### T4. (d) Fermion construction

- **Supplied.**
  - 𝒬_W: h = Σ s(k_j)α_j + (m + ΣW)β (rR16-1 §1);
  - D1(b_f, r) (`dirac.py:3-4`);
  - 22.5 Dirac fields on one edge (S26:71; rR19-34:54).
- **Open gates in `AX`:**
  - "staggered-Dirac/finite-Grassmann realization" (`AX:178`);
  - no Dirac-square carrier (`AX:120-122`).
- **Staggered under SF stays protected (proved; short argument, unrefereed).**
  - In the reduced-zone form, H(k) = Σ_j f_j(k)Γ_j with fixed Γ_j that anticommute with ε = (−1)^{x+y+z}.
  - SF changes only the scalar functions, f_j → f_j∘Φ_t. So εH_tε = −H_t at every t.
  - Every hop of the flowed law joins opposite sublattices, and Peierls links preserve that. So U(1)_ε is exact in the gauged strained law, and δm(t) ≡ 0 at every order. (This is R19-34's per-axis result, rR19-34:113, extended to SF.)
  - Caveat: an F3-type dressing must commute with ε. G₁ = −Σγ_j sin k_j does not, and it would re-admit a mass.
- **The root's own box symbol can be staggered (checked).**
  - SymS(b_f) has only odd harmonics: s_r ≤ 2e-16 for even r (`cm_hops`, first run). Equivalently, the mirror identity s(π − k) = s(k) holds (`sublum.py:5`).
  - So every axial hop has odd length, and the staggered phases apply exactly.
- **Bill (reading).** In the 3D Hamiltonian form, staggering leaves 2 same-mass tastes per field (RECALLED). Splitting them breaks U(1)_ε and restores the additive mass (Adams- or Hoelbling-type staggered-Wilson; RECALLED). A same-charge, same-mass twin per SM field meets R9-1's Z-width exclusion in kind (`TESTS:3840`).

### T5. Accuracy table for the pasted explanation

| phrase | status | correction |
|---|---|---|
| "grid tries to give them a huge mass" | right (checked: 4.7e16 GeV QED; doublers 4e18–1.3e19 GeV) | — |
| "about the grid's own energy scale" | overstated for the light fermion (~0.4% of 1/a in QED) | "a large fraction of the grid scale for the copies; ~1e16–1e17 GeV for the light fermion" |
| "root already does this on the unstretched grid" | right (rR19-31:62; rR19-34:69) | — |
| "as the strain inside the Earth does" | misleading | the GW supplies the stretch; matter supplies the fermions |
| "picks up a tiny leftover mass" | right per particle (1e-17 eV at t = 1e-21); its Planckian coefficient is the point | — |
| "drag" | wrong physics | reactive stiffness (a mass in matter): evanescent below ~1e6 Hz, ~55 m decay, reflection; growth in the other sign (rF2:18-21) |
| "could not have passed through the Earth" | conditional | the U = 1 lift + canonical mapping; vF1 OPEN (`TESTS:9283-9285`) |
| "fermions stay exactly as light" | overstated | "the grid adds nothing to any fermion's mass at any uniform stretch; real masses change only in proportion to themselves" |
| "what Einstein's theory already says" | right for rest mass under uniform traceless strain | the rule imposes GR's answer in one channel; it does not derive GR |

### T6. Verdict and conditions

**Verdict: SOUND WITH CONDITIONS** (reading), under the "match observations" standard.

The conditions:
1. **State it as an on-shell renormalization condition.** The pole mass at m₀ = m_c(h) vanishes at every uniform h, at every loop order, graviton loops included. With that wording it covers every lift and path family by construction (rF1 §0; F3 and F4 per `TESTS:9298-9320`).
2. **Accept the price as stated by the referee.** It "imposes rather than predicts" (vR19-34 item 6, line 21). It is number-free only under the law-functional convention (vR19-24 item 4). Under codimension counting it is a function-valued tuning.
3. **The vacuum knock-on must be absorbed and the root re-solved.**
   - The counterterm's curvature times the Wilson sea condensate is a Planckian change in the vacuum's E_g stiffness.
   - Checked: ⟨ψ̄ψ⟩_vac = −0.686 per field per cell (`cm_condensate.out`).
   - Estimate: ≈ 1.5e-3/a⁴ per unit-charge field per cell in SF units, sign convention unmatched to the rows. That is comparable to a single field's free shear row (S26:129 gives μ_E^F = −0.0172 per field) (suggested).
   - This is F5(c). Without (Σ) it moves the root.
4. **Gradient terms.** A first-gradient scalar mass term needs a vector; ψ̄ψ·∂h has none. So corrections start at O(a²∂²h) times the Planckian coefficient, i.e. a relative (qa)² ~ 1e-80 for GW wavelengths (proved by symmetry counting; size checked as arithmetic).
5. **Residual classification (proved by power counting; sizes checked).** After the rule, every remaining rest-mass strain channel is proportional to the particle's own mass, δm = ½c·m·t². This covers:
   - the multiplicative channel m_f Z_m″;
   - the gluonic channel (strain-dependent anisotropic renormalization of g², so of Λ_QCD);
   - Pauli/clover terms, which are irrelevant operators.

   For these, μ_ρ = 16πGħ²·c = 1.45e-39·c eV² m³/kg (`cm_powercount.out`). F2's Earth row allows **c ≲ 1e10**.

   F1's channel corresponds to c ≈ 1.7e18. That is the Planck enhancement M_Pl/m_N times the coupling and σ-term factors. **Only power-divergent couplings (the vacuum energy, the Higgs mass², the Wilson additive mass) and their cross terms can reach the bound.** The clause list must cover exactly those.

### T7. Arguments

**For (comparator, RECALLED, with my labels):**
- Protected zeros are robust under strain:
  - graphene by PT, where strain moves the cones; a gap needs about 20–25% strain, at Dirac-point merging (Pereira–Castro Neto–Peres 2009);
  - Weyl nodes, where strain gives an axial gauge field (Cortijo et al. 2015; Pikulin–Chen–Franz 2016).
- Unprotected ones are not:
  - 3D Dirac semimetals gap when strain breaks their protecting rotation (Na₃Bi, Cd₃As₂);
  - BHZ-type masses are tuned through zero by strain (ZrTe5, strained HgTe).
- Semiconductor deformation potentials are of order the bandwidth. For a non-degenerate cubic gap, E_g shear enters at second order, like F1's Hessian.
- Carrier contributions to elastic constants scale as n × (deformation potential)² / energy (Keyes 1967). This is the solid-state twin of "matter stiffens the medium against strain".
- **Three-way choice (reading of Nielsen–Ninomiya):**

  | option | what it keeps | what it pays |
  |---|---|---|
  | Wilson (root) | one species, local Hamiltonian | the rule |
  | staggered | protection, local Hamiltonian | same-mass taste twins |
  | overlap / domain-wall | one species, protection | non-locality in time for continuous-time overlap, or an extra dimension / enlarged site (Qubit axiom) |

  I recall recent claims of exact non-onsite chiral symmetries in Hamiltonian lattice models, but I have not checked whether any applies in 3+1D with gauge fields.

**Against** (the steelman in Part 1): a Planck-strength graviton–ψ̄ψ coupling, fixed by fiat to cancel a loop, makes matter's strain response definitional.

### T8. Evidence and next test

**Would change the verdict:**
- F5(c) knock-on unabsorbable → unsound.
- A single "strain-covariant renormalization conditions" clause covering all power-divergent channels, with checked residuals → sound.
- A checked Hamiltonian, quasi-local, single-species construction with an exact (modified) chiral symmetry on Z³ → the rule becomes dominated rather than wrong.

**Next test: G-Λ, the gluonic strain channel of the nucleon mass under the rule (not in F5's list, `TESTS:9346-9356`).**

- **Plain question.** With P-R19-34a in force, the nucleon's rest mass (about 99% gluonic) still depends on strain through the anisotropic renormalization of the strong coupling. Is it below F2's Earth row, as power counting says (c ≲ 1e10)?
- **Setting.**
  - The SF-strained root gauge edge Gph(2.9435) as an SU(3) gluon at one loop, with Psym links as F1;
  - the root's quark content on the D1 edges;
  - P-R19-34a imposed.
- **Probes.**
  - (a) The E_g Hessian K = ∂²_t(1/g²_eff) of the strained one-loop gluon self-energy at zero external momentum. Include the Ward check and the gauge-parameter check, separating the ultraviolet-finite artifact from the universal log.
  - (b) c_Λ = −(8π²/b₀)·K, from δlnΛ_QCD = −(8π²/b₀)·δ(1/g²) (comparator: Karsch-type anisotropy coefficients, RECALLED).
  - (c) μ_ρ = 1.45e-39·c_Λ, compared with F2's rows.
  - (d) A composition check: Δc between nucleons and electrons, against MICROSCOPE at the strain amplitudes available (expect irrelevant at t ~ 1e-21).
- **FIXED readings.**
  - **GLUE-SAFE:** |c_Λ| ≤ 1e8 (a 100× margin), checked.
  - **GLUE-HAZARD:** |c_Λ| > 1e10.
  - **OPEN:** branches disagree, or the strained non-abelian law cannot be built from the registered texts.
- **Expectation.** GLUE-SAFE with |c_Λ| = O(0.1–10). The gauge coupling is marginal, so its strain artifact carries no 1/a.

**Alternative if Jon wants a mechanism rather than a rule:** price the staggered version of the root's own box symbol, SymS(b_f) at r = 0, under SF.
- δm ≡ 0 is proved (T4).
- The bill is in the taste twins and in re-solving the four rows with one fewer knob (no r).
- Expected reading: excluded by twins unless they are assigned to physical species, which confirms that the rule is the price of the Wilson corner.
