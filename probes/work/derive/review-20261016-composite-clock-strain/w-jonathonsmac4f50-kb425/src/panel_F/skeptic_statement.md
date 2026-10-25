# Panel F: the foundations skeptic's statement (2026-10-13, about 18:25–19:05Z)

**Provenance.** Written by a Claude Opus 5.5 panelist, the same model family as the supervisor and every C5 worker. Unrefereed. I read `docs/MINIMAL_AXIOMS_2026-06-29.md` (`AX`) in full. I edited no repository files. Scripts and outputs are in this folder: `sk_checks.py/.out`, `sk_range.py/.out` and `sk_eps.py/.out`. Peak memory was 119 MB.

**Labels.**
- **proved:** a complete short argument; unrefereed.
- **checked:** numbers I ran here.
- **suggested:** argued but not proved.
- **reading:** an interpretation.
- **comparator:** an outside reference point.
- **RECALLED:** from memory.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`.
- `rX` and `vX` = `P/agents/C5_X_report.md` and `C5_X_referee_verdict.md`.
- `SRP` = `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`.
- `F5w` = the F5 worker report, still in progress and unrefereed: `scratchpad/C5/F5/F5_report.md`.

---

## Part 1. Plain words

### The short answer

Almost nothing in this calculation comes from the four axioms.
- **What the axioms give:**
  - a cubic grid of sites;
  - one qubit's worth of possibilities at each site;
  - a nearest-neighbour rule that sets the odds;
  - records.
- **What the calculation uses from them:** only the grid's cubic symmetry.
- **What is supplied by hand:**
  - the fermion: 4 components, Dirac matrices, the Wilson term, the box-shaped momentum law and its tuned numbers;
  - the photon;
  - the graviton;
  - the way stretch enters matter (SF);
  - the critical mass;
  - continuous time;
  - the conversion from shear stiffness to graviton mass.

So F1–F5 test a supplied lattice field theory, not the axioms.

The proposed rule is not something the qubit system produces. It is an instruction: "set one coefficient to whatever value gives the observed outcome, at every amount of stretch."
- Once that value has been computed, the rule can be written as a local term at each site.
- Under Jon's standard (match observations, name the prices), it is an acceptable price.
- But it imposes the answer Einstein's theory gives instead of deriving it.
- It is one more entry in a growing list of such clauses.
- On its own it does not finish the job: the F5 worker finds a larger Higgs-side channel that the rule does not touch.

### (a) What is "grid stretching"?

**The axioms' grid has nothing to stretch.** It is Z³: integer points and which ones are neighbours (`AX:37-41`). It has no spacing variable. The only length anywhere is the single unit conversion a⁻¹ = M_Pl, one constant for the whole grid (`SRP:16-17`). So "stretching" cannot mean that sites move apart.

**In the campaign, "stretch" is a field laid on the grid.** The strain or graviton field h changes how matter hops: hops become easier along one axis and harder along another. There are two versions:
- **H-cov** scales the hops axis by axis.
- **SF** moves each particle's momenta along a flow.

Either way, h is an effective metric that matter feels. On a fixed grid, "stretching" means only this.

**Why this matters.** In Einstein's theory a uniform stretch is only a change of coordinates and does nothing physical. On a fixed grid it is physical, because the grid singles out its own coordinates. That one fact is the root cause of every shear problem in C5. Lemma H says the same thing: "the lattice vacuum behaves like an elastic solid" (`rR19-15:45,161`).

### (b) Why does the grid give fermions extra mass?

**The doublers and the trade-off.** On a grid, the simplest fermion law has 8 copies of each particle, one at each corner of the momentum zone. A smooth fermion law can either keep chiral symmetry (the symmetry that keeps a massless fermion massless) or get rid of the copies. It cannot do both. This is the Nielsen–Ninomiya theorem (RECALLED).

**Wilson's fix.** Wilson's fix adds a mass-like term that is zero for slow particles and large for the copies. On the root edge it lifts each copy by 0.355/a per axis (checked, `sk_checks.out:1`). Because the added term is a mass term, it breaks chiral symmetry. Quantum corrections then push the real fermion's mass up:
- δm = 0.0419 e²/a on the root edge;
- that is 0.0038/a at the electron's charge;
- that is about 5e16 GeV if a is one Planck length (checked).

**How big that is.**
- "Huge" is right: about 1e20 times the electron mass.
- "About the grid's own energy scale" overstates it by about 260×. The push is about 0.4% of the grid scale for the electron charge and about 2% for quarks (an estimate).
- The copies sit at the grid scale; the real fermion's push is smaller.

**The cancellation.** The model cancels the push with a hand-set bare mass, the critical mass. For the electron it must be right to about 1 part in 1e20 (checked, `sk_checks.out`). That is the step "the root already does on the unstretched grid": a tuning stated as a rule.

**It is not forced.** A staggered fermion keeps a remnant chiral symmetry at every strain and gets no extra mass at all (`rR19-34:113`, proved there for per-axis amplitudes). Staggered fermions are the kind the framework's own fermion work points to (the half-filling staggered-flux note, `docs/HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02.md:61`; the Dirac–Kähler notes). I checked two things:
- the root's own momentum law is compatible with that symmetry (s(k + π) = −s(k) to 8e-15);
- the SF flow's driving field is π-periodic (to 8e-15).

Only the Wilson term breaks the symmetry, by 0.355 (`sk_eps.out`). So the extra mass is a property of the chosen fermion, not of "the grid".

### (c) How big is the grid compared with a fermion?

Taking a = one Planck length (1.6e-35 m), each reduced Compton wavelength spans this many sites per axis (checked):

| particle | sites |
|---|---|
| electron | 2.4e22 |
| light quark | 3.5e21 |
| nucleon | 1.3e19 (proton radius: 5.2e19) |
| top quark | 7e16 |

**What this means.** A fermion is a slow, very long wave on the grid. It sits entirely inside the box of momenta where its free motion is exactly relativistic. It feels the Wilson term only through virtual excursions to grid-scale momenta in loops.

**Hidden assumption 1: a = Planck length.**
- This is a units convention. `SRP:39-41` says explicitly that it does not assert a/ℓ_P = 1; that equality is an open gravity question (`AX:189-190`).
- The size of the GW170817 conflict depends on it.
- If G is held at its observed value and a is left free, the Earth exceedance scales as ℓ_P/a. It disappears for 1/a below about 8e10 GeV (suggested; my arithmetic, `sk_checks.out`).
- Under the campaign's canonical mapping, which builds in G = a² (`P/scripts/C5/F1/f1_sizes.py:4`), the exceedance grows with a instead.
- So the hazard's size rests on a dimensionless number that the framework does not supply.

**Hidden assumption 2: one qubit per site.**
- The axioms give each site one qubit, M_2(C), which has 2 states (`AX:47`).
- The root puts 22.5 Dirac fields × 4 components = 90 fermion modes on each site. That is a space of 2^90 states.
- It also puts 12 gauge links and 4 scalars on each site, each with infinitely many states.
- So the root's "site" is at best a block of at least 90 axiom sites, and more for a local fermion encoding in 3D (RECALLED: Verstraete–Cirac; Chen–Kapustin–Radičević).
- The root's "a" is therefore not the axiom grid's spacing (proved: dimension count).

### (d) How is a fermion built on this grid?

**In the root, by hand.** The law is h(k) = Σ s(k_j)α_j + (m + Σ W(k_j))β, with 4×4 Dirac matrices (`P/scripts/C5/R18-5/dirac.py:1-5`).
- s(k) = k exactly inside the box |k_j| ≤ 0.909, with a smooth (Gevrey) step outside (`P/scripts/C5/R18-5/sublum.py:1-4`).
- W = 0 inside the box.
- The two shape numbers, 0.909 and 0.556, were tuned together with two other knobs so that the graviton's cone and shear rows come out zero (`rR18-9:49`: 4 tunings plus a window).

**Its hops are not nearest-neighbour.** The amplitudes fall more slowly than an exponential (checked, `sk_range.out`):

| distance | amplitude |
|---|---|
| 21 sites | ~6e-5 |
| 61 sites | ~1e-7 |
| 201 sites | ~2e-11 |

**Other supplied pieces:** Fermi statistics, the filled Dirac sea and continuous time.

**What the axioms do give:** a 2-state site with Pauli (Cl(3)) structure (`AX:47-50`).
- The step from that to a Dirac fermion (staggered, Dirac–Kähler or finite-Grassmann) is a named open gate (`AX:178`).
- Admissibility explicitly does not choose a Hamiltonian or "assert a Dirac-square carrier" (`AX:120-123`).

**Verdict on (d): supplied, not derived.**

### The pasted explanation, line by line

| phrase | mark | why |
|---|---|---|
| "the grid tries to give them a huge mass, about the grid's own energy scale" | **Half right** | "Huge" is right (about 1e20 m_e). "The grid's scale" overstates the real fermion's push by about 260× in QED (0.4% of 1/a); only the copies sit at the grid scale. "The grid tries" is wrong: the chosen Wilson-type law does this, and a staggered law on the same grid would not. |
| "critical mass … exactly cancels … root already does this" | **Right**, with a rider | It is a cancellation to 1 part in 1e20 for the electron, made by hand and stated as a rule. |
| "Stretch space … as a passing gravitational wave or the strain inside the Earth does" | **Wrong in the second half** | The stretch that matters is the passing wave's. The Earth supplies the matter, not the strain. The Earth's static field is, to leading order, not a traceless shear. |
| "The grid's push … changes … every fermion … picks up a tiny leftover mass" | **Conditional** | True for the U = 1/Psym realization. The F1 referee recorded OPEN because an equally admissible O(t²) dressing moves the leftover through zero (`vF1:3,5,15`). F3 confirms this (DRESS-SHIFTS, CONFIRMED WITH CORRECTIONS, `scratchpad/C5/ref_F3/REFEREE_VERDICT.md`). |
| "Added up over all the matter in the Earth" | **Misleading** | The effect is local: it is proportional to the local fermion density. Every cubic metre of rock carries the same cutoff. The Earth's thickness only sets how many decay lengths the wave must cross (about 1.7e5). |
| "a heavy 'drag' on gravitational waves" | **Wrong word** | It is a mass, not friction. Waves below the cutoff (about 0.9 MHz for \|m_g\| = 3.6e-9 eV) cannot travel through rock. They fall off by a factor e every ~54 m and are reflected; no energy is absorbed. The ionosphere reflecting long radio waves is the right picture (comparator). |
| "GW170817 could not have passed" | **Overstated** | This is conditional on all of the following: the canonical mapping; a = ℓ_P with G = a²; the nucleon ψ̄ψ estimate; F2's derived 1D medium model ("not a published … limit", `vF1:9`); and the U = 1 lift. The refereed reading is OPEN, not a conflict. |
| "fermions stay exactly as light as they are" | **Overstated** | The rule re-sets only the additive (grid-sized) push. Three leftovers remain: a piece proportional to each fermion's own tiny mass, the strain dependence of the magnetic-moment-type terms, and gradient terms for non-uniform stretch (F5w: all small). It does not touch the Higgs-side channel at all (F5w: about 5 MeV graviton mass in rock, suggested). |
| "what Einstein's theory already says" (not in the pasted text; addressed as asked) | **Right about the outcome, wrong as a derivation** | In GR, and in experiment (MICROSCOPE, \|η\| ≲ 1e-14, RECALLED), a passing wave does not change rest masses. The grid model disagrees. The rule overrides the model to agree with GR; the agreement is imported, not derived. |

### Corrected version

> **The setup.** In this grid model each fermion's law has an extra term (the Wilson term) that removes unwanted copies of the particle. That term breaks the symmetry that would keep massless particles massless, so quantum effects push every fermion's mass up by a fraction of a percent of the grid's energy scale. If the grid is one Planck length, that is about 10¹⁶ GeV for the electron's charge, some 10²⁰ times the electron mass. The model cancels it with a hand-set bare mass, the "critical mass", chosen so that the cancellation holds on the unstretched grid. For the electron that setting must be right to 1 part in 10²⁰.
>
> **What was found (conditional).** A passing gravitational wave is represented as a field that makes matter hop slightly differently along different axes; the grid itself does not move. In the simplest way of coupling that field to charged fermions, the cancellation is no longer exact, and each fermion's mass changes in proportion to the square of the stretch. Inside matter this acts as a mass for gravitational waves, set by the local density. Read through the campaign's conversion (grid = Planck length, gravity's strength set by the grid), rock would reflect gravitational waves below about 1 MHz, and GW170817 could not have reached the detectors from below the horizon. It did. But the referee found that another equally allowed way of writing the coupling moves the leftover to zero, so the finding is OPEN. Its size also rests on assumptions the framework does not supply.
>
> **The proposed rule.** Re-set the bare mass for every amount of stretch, so that the grid's own push on fermion masses cancels at every stretch, not only at zero. That gives the outcome Einstein's theory and experiment give: a passing wave does not change rest masses. It does so by stipulation, not by explaining why. A fermion law that keeps its remnant chiral symmetry (staggered type) would not need it.

### My verdict on the rule (P-R19-34a)

**Sound with conditions, as a named price under the "match observations" standard.** It is not a law the qubit system produces, and it is not sufficient on its own.

It is an outcome clause. Its realization is a local, on-site term ψ̄ψ(x)·m_c(h(x)), but its coefficient function is fixed by the requirement "the fermion comes out massless". It cannot fail the test it was written for, so passing that test is not evidence for the grid.

**Conditions:**
1. **Count it as conditions, not as zero.**
   - Under the campaign's law-functional convention it costs 0 numbers.
   - Under a codimension count it is one function of strain per fermion class per loop order: 2 per class per order at O(h²) traceless, 4 with the trace (F5w §(a6)). That is on top of the h = 0 critical tuning.
   - Without the clause, each of these would need tuning to about 6e-9 of its natural size for the Earth row (F3, conditional), or about 1e-16 for the history line (`rR19-34:152`).
   - A convention under which every desired outcome costs 0 is not a counting rule. Jon has to fix the count (owner Q2, `PRICE_NOTE:644`) before this is compared with alternatives.
2. **Restate it for quarks.** Confined quarks have no pole mass, so "pole mass at zero" must become a Ward-identity (PCAC) condition at each strain, and that restatement must be shown to be well defined.
3. **It needs a local strain field the mass term can read.** That is the supplied graviton P-N1, so the rule inherits that price, including its tension with finite-dimensional sites (`TESTS:8972`).
4. **It does not stand alone.** The F5 worker reports two remaining problems (F5w §0 item 5):
   - the Higgs-vev channel, which needs (S_loc), still OPEN;
   - the knock-on onto the vacuum's shear rows, which needs (S\*) or (Σ) or a re-solve of the root.

   Adopting P-R19-34a alone does not restore agreement with observation.
5. **Label what it is.** It imposes the equivalence principle for rest masses under stretch. After adoption, tests of that principle stop being tests of the framework.

### The strongest argument from my tradition

A clause defined by its own outcome cannot fail, so it carries no evidence.
- **If the grid were a regulator, this would be ordinary renormalization.** Lattice QCD sets its critical mass the same way, and that is fine there because the grid is removed at the end (a → 0).
- **Here the grid is physical, with a fixed spacing.** A symmetry-breaking term with a Planck-sized coefficient, which no symmetry forbids, is then a fine-tuning, whatever it is called.
- **This is a known problem.** It is the gravitational version of the Collins–Pérez–Sudarsky–Urrutia–Vucetich problem (PRL 2004, RECALLED): a Lorentz-violating cutoff feeds order-α violations into low-energy physics unless a symmetry stops it.
- **The campaign's own map shows the pattern.** "Every wall that touches gravity's source is now passed only by a stipulated clause, and the clauses together make the sector GR by construction" (`TESTS:8986`). The clauses so far are (S), (S\*), (Σ), D1∞, (S_loc) and now P-R19-34a, each of which "imposes rather than predicts" (`vR19-34:21`; `vR19-24:11`).

These are special cases of one statement: "matter and vacuum couple to the metric field only in the covariant (GR) way". If Jon wants to pay that, it is more honest to register that one statement as a primitive, say plainly that the framework does not predict how matter and gravity couple, and look for the framework's testable content elsewhere.

### The steelman against my verdict

- **From the lenient side.** Every quantum field theory fixes masses by outcomes ("pole mass = measured mass"), and nobody calls the QED mass counterterm unsound.
  - In quantum fields on a background, renormalization conditions must hold in every background, and local counterterms that depend on the background are standard (curved-space ξRφ², RECALLED).
  - P-R19-34a is exactly such a condition. It is ultralocal, its gradient corrections are about 1e-81, and it is number-free under the registered convention.
  - Under Jon's standard it is simply "sound". "Tuning" is a complaint about explanation, not about observation.
  - The symmetry alternative may not exist for the Standard Model: staggered fermions come in tastes, and 22.5 Dirac fields would be 11.25 staggered fields, which is not an integer.
- **From the strict side.** It is unsound. Under codimension counting it is infinitely many conditions, and it hides a fine-tuning behind a definition.

**My answer.** The lenient case is right that this is legitimate renormalization. But in curved-space QFT the allowed counterterms are the diffeomorphism-invariant ones. This counterterm is not invariant: it exists only to cancel a non-invariant effect produced by the grid. I keep "sound with conditions": accept it as a price, count it as conditions, and do not present the resulting agreement with GR as support for the grid.

### What would change my mind

- **Toward "sound" without riders:**
  - a derivation that strain-covariant criticality follows from a law-level symmetry or principle already in the axioms; or
  - the native-fermion test below returning NF-ZERO while the root's other rows survive. The rule would then be unnecessary rather than imposed.
- **Toward "unsound":**
  - F5's referee confirming that the Higgs-vev channel cannot be closed by any registered or number-free completion; or
  - the PCAC restatement for confined quarks failing to define m_c(h) uniquely.
- **Toward "no hazard to fix":** a principle, not a tuning, that fixes the registered interacting lift at a structural zero of the additive Hessian.

### One concrete next test (specified below as NF-1)

Rebuild F1's channel on the framework's native fermion, staggered or Dirac–Kähler, with no Wilson term. Ask:
- whether the remnant chiral symmetry survives SF strain and the gauge links, in which case the additive strain channel is zero by symmetry rather than by clause;
- what the taste count then costs.

---

## Part 2. Technical

### T1. Line-by-line audit: derived from the axioms or supplied

| Item used in F1–F5 | What the axioms say | Status | Evidence |
|---|---|---|---|
| **Lattice** Z³, nearest-neighbour adjacency, cubic rotations | `AX:37-41` | **Axiom.** Used only as a symmetry group. The root's laws are quasi-local with all-range hops (checked, `sk_range.out`), so nearest-neighbour adjacency is used only as coordinates. | `P/scripts/C5/R18-5/sublum.py:1-4` |
| **Time** (Z³ × ℝ, continuous) | No time metric (`AX:122`, `AX:185`) | **Supplied** | `rR16-1:55` |
| **Spacing** a = ℓ_P | `AX:189-190`; `SRP:16-17` (units only), `SRP:39-41` ("does not assert a/l_P = 1") | **Supplied** as a units primitive; a/ℓ_P = 1 is **open**. Load-bearing for every size in F1/F2. | `f1_sizes.py:4,20-30` |
| **Fermion: 4 components, Dirac algebra** | One-site algebra M_2(C) ≅ Cl(3,0), 2 states (`AX:47-50`). No Hamiltonian and no "Dirac-square carrier" (`AX:120-123`). Staggered/finite-Grassmann realization is an open gate (`AX:178`). | **Supplied** | `dirac.py:3-4` |
| **Fermi statistics, filled sea** | Not in the axioms (`AX:178`) | **Supplied** | `dirac.py:15` |
| **Wilson term W, box symbol, (b_f, r)** | Nothing | **Supplied and tuned:** 4 tunings plus a window (`rR18-9:49`) | `dirac.py:24-50`; `rR18-9:49-56` |
| **Matter content per site:** 90 fermion modes, 12 links, 4 scalars | One qubit per site (`AX:47`) | **Inconsistent with one qubit per site** unless coarse-grained over ≥ 90 sites (proved: dimension count) | `S26:71` |
| **Graviton / strain field h** | Nothing. A non-compact CCR is excluded by finite dimension (`vR19-22` via `TESTS:8972`). | **Supplied** (P-N1, "the only working source", `TESTS:8972`) | — |
| **TT vertex UD** | Nothing | **Supplied:** "stipulated" (`dirac.py:6`); unique only inside the stipulated family 𝔇 (`rR18-9:102`) | — |
| **Strain law SF** | Nothing | **Supplied:** "stipulated, P-R16-13a" (`rR18-9:86,103`). **Incomplete for the interacting law:** the lift is not fixed (`vF1:5,15`). | — |
| **Gauge field:** 12 vectors, non-compact U(1), Peierls, box photon Gph(2.9435) | Nothing. Links on bonds are not in a site-only algebra. | **Supplied** | `rR16-1:55`; `rR19-34:56` |
| **Chiral SM content on a Wilson edge** ("22.5 Dirac") | — | **Supplied.** The Wilson term for chiral fermions was not computed (`rR19-34:74`); it breaks SU(2)×U(1) (Nielsen–Ninomiya and the Rome approach, RECALLED) | — |
| **Critical mass at h = 0** | A law "gives exactly one answer" (`AX:94-95`), but no value is supplied | **Supplied:** a per-species tuning to about 1e-20 (electron), stated as a clause | `sk_checks.out` |
| **P-R19-34a** | Needs "retained derivation or bridge, or explicit approved-primitive registration" (`AX:87-91`) | **Supplied (proposed)**; "imposes rather than predicts" (`vR19-34:21`) | `PRICE_NOTE:679` |
| **Canonical mapping** m_g²a² = 16πμ | Source/action is open (`AX:187`); G is open (`AX:189-190`) | **Supplied, conditional**; builds in G = a² | `PRICE_NOTE:22`; `vR19-34:19` |
| **Records; admissibility distribution** | `AX:57-83` | **Not used anywhere in F1–F5** (reading) | — |

**Net (reading).**
- Of the six items Jon asked about, only the lattice is axiom content.
- The fermion, the graviton/strain field, SF, the gauge field and the critical mass are all supplied.
- Two of them, the CCR graviton and 90 modes per site, are in tension with the Qubit axiom's one-qubit site.

### T2. Numbers (checked unless marked)

All from `sk_checks.out`, `sk_range.out` and `sk_eps.out`, using the archived `dirac.py`/`sublum.py` unmodified.

**The root edge D1(0.909103708, 0.555604226):**
- W(π) = 0.355204, so the copies sit at m + 0.355n/a.
- Free-vacuum ⟨ψ̄ψ⟩ = −0.686 per Dirac field per site (m = 0, N = 64). This feeds the knock-on.
- The F5 worker finds Δμ_E = +1.689e-2 per field per e² (F5w §1), the same order as my estimate.

**Hopping range** (odd harmonics only; even harmonics are ≤ 5e-12):

| n | \|s_n\| | \|W_n\| |
|---|---|---|
| 1 | 1.24 | 0.22 |
| 21 | 5.0e-5 | 6.1e-5 |
| 61 | 3.0e-8 | 1.1e-7 |
| 201 | 1.2e-13 | 2.2e-11 |

The decay is slower than exponential (Gevrey step). The edge is not nearest-neighbour.

**Staggered compatibility:**
- max\|s(k + π) + s(k)\| = 7.8e-15;
- the SF driving field p = s·s′ is π-periodic to 8.0e-15;
- max\|W(k + π) + W(k)\| = 0.355.

So only W breaks the U(1)_ε sublattice symmetry. Whether the full SF-strained, gauged staggered law keeps it is suggested (it holds if the flow commutes with the Π-shift and the links keep hop parity) and is the first probe of NF-1.

**Additive mass:**
- δm = 0.041858 e²/a (`rR19-34:86`) = 3.84e-3/a in QED = 4.7e16 GeV at a = ℓ_P;
- for quarks, about 1.7e-2/a (estimate, C_F g_s² ≈ 0.4);
- precision needed for the electron's h = 0 critical mass: 1.1e-20.

**Sizes at a = ℓ_P** (reduced Compton wavelength, in sites):

| particle | sites |
|---|---|
| electron | 2.39e22 |
| u/d quark (3.5 MeV) | 3.49e21 |
| nucleon | 1.30e19 |
| top | 7.07e16 |

The proton radius is 5.2e19 sites.

**The F1 Earth number**, \|m_g\| = 3.63e-9 eV (conditional):
- decay length ħc/m_g = 54 m;
- cutoff frequency 8.8e5 Hz;
- 1.7e5 decay lengths across the 9,293 km L1 chord.

The 100 Hz graviton energy is 4.1e-13 eV.

**Dependence on a:**
- `f1_sizes.py` uses m_g² = 16π·n·a·w·c/4, i.e. G = a², so the hazard grows like a.
- With G fixed at its observed value: m_g² = 16πG·n·w·c/(4a), so the exceedance is 1.62e8 × ℓ_P/a. It is ≤ 1 for 1/a ≤ 7.5e10 GeV (suggested).

### T3. Law or outcome? Analysis of P-R19-34a

1. **Form.** As stated at `TESTS:9335-9337` and F5w §(a1): "on every uniformly strained law, each Dirac species' bare mass is re-set so that its pole mass at zero bare physical mass vanishes, at every order."
   - This is an implicit definition of a coefficient function m_c(h) through an observable of the full interacting theory.
   - Once solved, the Hamiltonian term is Σ_x m_c(h(x)) ψ̄ψ(x). That is ultralocal in h and on-site, with O((a·q)²) gradient corrections (F5w).
   - So the realization is local; the selection principle is outcome-referential (reading).
2. **Against the axioms' law sentence** (`AX:94-95`). If m_c(h) is unique it gives one answer per state, so it passes. Perturbative uniqueness holds by the implicit function theorem, since ∂m_pole/∂m₀ = 1 + e²z with z ≈ +0.3–0.4 (F5w §(a3)).
   - It is not derived. Under `AX:87-91` it needs registration as an approved primitive or bridge.
   - For confined quarks, "pole mass" is undefined. The clause needs restating, for example "the PCAC/axial-Ward mass vanishes at each strain", and that restatement is unchecked.
3. **Why the effect exists at all** (proved in `rR19-34:110-114`; reading here). Take the chain: no same-mass copies, plus a smooth symbol, implies broken chiral symmetry (Nielsen–Ninomiya, RECALLED). Broken chiral symmetry means δm is allowed, and a strained law breaks the Ward identity for relabelling. Together these give δm″ ≠ 0 generically.
   - The rule cancels the last link by fiat.
   - Changing the fermion law cancels it by symmetry: r = 0, staggered, Ginsparg–Wilson (comparator, RECALLED).
4. **Count** (reading; numbers from F5w):
   - **law-functional convention:** 0 numbers, 1 clause;
   - **codimension:** 2 (traceless) or 4 (with trace) per class per loop order at O(h²), unbounded over orders, plus the existing h = 0 tuning.

   The honest summary: a tuning to about 1e-8 per class per order (Earth row, conditional), re-done at every order, written as one sentence.
5. **Sufficiency (F5w, unrefereed): RULE-PARTIAL.**
   - Residual (iv), the Higgs-vev shift times the vacuum mass-slope c₁, exceeds the Earth row by about 3e38 and the IGM row by about 2e28.
   - The knock-on moves the R18-9 root unless (S\*) or (Σ) is adopted.

   So the rule is one of at least three clauses needed: P-R19-34a + (S_loc) + (S\*)/(Σ).
6. **What it removes from observation.** At h = 0 the law is unchanged (F5w §(d), proved there for every h = 0 quantity). It restores equivalence-principle and local-Lorentz behaviour that the bare grid model violates (F5w, suggested/comparator). So it is not observationally harmful. Its cost is evidential and in the count, not observational.

### T4. Next test, specified: NF-1, the native-fermion strain control

- **Plain question.** Is the strain-dependent additive mass a property of the root's Wilson-type fermion, or of the grid? Can a symmetry, which is a law, do what P-R19-34a does by clause?
- **Setting.**
  - A Kogut–Susskind staggered fermion on Z³ × ℝ: one complex component per site, η-phases (the Cl(3) site presentation).
  - Hopping symbol: the root's odd box symbol s(k) at b_f = 0.909103708, with r = 0. It already satisfies s(k + π) = −s(k) (checked).
  - Photon Gph(2.9435), Psym links, the SF flow of the staggered band E² = Σ s(k_j)², one-loop U(1), Feynman gauge.
  - Branch: F3's dressings restricted to ε-respecting generators, plus one ε-breaking generator as a control.
- **Probes.**
  - (a) Prove or disprove that U(1)_ε (ψ → e^{iθε(x)}ψ, ε = (−1)^{x+y+z}) is exact for the SF-strained, gauged law: the flow commutes with the Π-shift, and Psym links keep each hop's sublattice parity.
  - (b) The additive-mass E_g Hessian, expected 0 (≤ 1e-12); the control must give ≠ 0.
  - (c) The multiplicative channel z″ (strain dependence of Z_m), sized on F2's Earth and IGM rows.
  - (d) The taste content: 2 four-component tastes per staggered field in the 3D Hamiltonian (RECALLED). State how the 22.5-Dirac SM count maps (non-integer as it stands) and what R9-1's same-mass-copy exclusion then costs. Compute the four cone/shear rows for the staggered content and say whether an R18-9-type zero can be re-solved.
- **FIXED readings.**
  - **NF-ZERO:** U(1)_ε exact (proved, or checked ≤ 1e-12), additive Hessian ≡ 0, and the multiplicative residual below F2's Earth row.
  - **NF-BROKEN:** SF or the links break U(1)_ε, giving an additive Hessian ≥ 1e-3 e².
  - **NF-TASTE-WALL:** NF-ZERO on the strain channel, but the taste content conflicts with the SM count or R9-1, with the count stated.
  - **OPEN:** otherwise.
- **Expectation.** NF-ZERO on the strain channel, and NF-TASTE-WALL overall. If so, the hazard and P-R19-34a are both artefacts of choosing a Wilson-type fermion, and the real price is the taste or chirality wall (`AX:178`), which the gravity root has so far supplied around rather than paid.

### T5. Prior art (counted once)

- **R19-34 and its verdict:** the chiral zeros, including staggered and r = 0 (`rR19-34:110-114`), and P-R19-34a "imposes rather than predicts" (`vR19-34:21`).
- **F1 and its verdict:** OPEN, lift not fixed (`vF1:3,5,15`).
- **F3 referee:** DRESS-SHIFTS, CONFIRMED WITH CORRECTIONS.
- **F4 referee:** PATH-SHIFTS, CONFIRMED WITH CORRECTIONS; the zero is reachable by a tuned positive path ensemble (`scratchpad/C5/ref_F4/F4_referee_verdict.md:1-8`).
- **F5 worker:** RULE-PARTIAL (unrefereed).
- **R19-24 and its verdict:** the counting collision (`vR19-24:11`).
- **The C5 closing record:** W2 (`TESTS:8972`) and the shape of the map (`TESTS:8986`).
- **SRP:** a/ℓ_P = 1 is not asserted.
- **Comparators (RECALLED):** Nielsen–Ninomiya; Wilson and staggered fermions; Ginsparg–Wilson; the Rome approach; Collins et al. 2004; MICROSCOPE.
