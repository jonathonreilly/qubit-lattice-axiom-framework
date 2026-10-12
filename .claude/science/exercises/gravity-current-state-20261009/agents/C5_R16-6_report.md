# C5 R16-6 report: after R15-1's FAIL, can Λ be removed with g ≡ 0 (no signalling)?

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-12, 22:48Z to 23:22Z. No repository file was edited.

**Scratch folder.** `S/` = `.../scratchpad/C5/R16-6/`. Scripts and outputs are in `S/scripts/`; each runs in under 10 s at `OMP_NUM_THREADS=2`.
- `r166_identity.py/.out` (sympy): Lemma I re-derived; the integrating reader gives g ≡ 0 for every history; the equilibrium P-EoS identity; the converse.
- `r166_supercool.py/.out`: bag-model first-order transition with supercooling (the control), readers IE, literal P-EoS, MR.
- `r166_inflation.py/.out`: m²φ² inflation plus perturbative reheating, with the reader setting the expansion; readers G0, IE, and a two-register linear reader LIN.
- `r166_sm.py/.out`: e⁺e⁻ annihilation with neutrinos decoupled at 2 MeV (two temperatures); QCD crossover with a RECALLED HotQCD-2014 p/T⁴ parametrization.
- `r166_desi.py/.out`: matter, radiation and DESI-like CPL (w₀, w_a) = (−0.75, −0.86); readers IE and LIN.

**Read.**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (`AX`); the C5 method `TESTS.md:2302-2320`; the item `TESTS.md:5223-5245`; `agents/C5_R14-5_report.md:1-200` and `agents/C5_R14-5_referee_verdict.md:14-36` (`vR14-5`); `agents/C5_R15-1_referee_verdict.md` (`vR15-1`); `agents/C5_R15-6_report.md` (`R156`, all); the R15-4 and R15-6 referee verdicts, which appeared during this run: `scratchpad/C5/ref_R15-4/REFEREE_VERDICT.md` (`vR15-4`) and `scratchpad/C5/ref_R15-6/REFEREE_VERDICT.md` (`vR15-6`).
- The Λ entries: `TESTS.md:4157-4188, 4317-4320, 4351-4363, 4417-4424, 4505-4517, 4621-4641, 4721-4729, 4876-4914, 4924-5036, 5164-5206`; R5-3 Lemma PT `TESTS.md:2985-2988`.
- In part: `agents/C5_S17_synthesis.md` (§1.6 `:127-139`, prices `:221-224`, owner Q2 `:281-287`, scope `:458`); `SUMMARY.md:677-714` (§26); `agents/C5_R15-1_report.md` (grep: Lemma S `:43,122-147`, GR control `:137`, g ≡ 0 is GR `:216`); `agents/C5_R15-4_report.md` (grep: classes `:37-71,107,245-260`).

**Labels.** proved / checked (sympy or numerics this run) / suggested / reading / comparator (RECALLED unless stated; nothing was downloaded).

**Units and subtraction rule (named before the runs).** Homogeneous; κ = 1; u = ln a; the zero-mode law is 3H² = R (`C5_R14-5_report.md:163`). h := (ρ+p)_tot. V := ρ_tot − R, the reader's inferred vacuum (`R156:25`). ρ_v,late is the w = −1 stress after the last change. **Λ̃_late := R − (ρ_tot − ρ_v,late)**, i.e. Λ̃ measured from the late vacuum. "Λ̃_inst" means Λ̃ measured from the instantaneous w = −1 stress (R14-5's λ + κρ_v, `C5_R14-5_report.md:24`). Nothing else is subtracted.

---

## 0. Verdict against the FIXED readings (`TESTS.md:5242-5244`)

**Worker reading: PASS, scoped, for the referee.** The class is 𝒢, readers whose zero is the late vacuum supplied by the law. Two members are given:
- **G0**, a state reader: R = energy density above the T = 0 vacuum of the supplied dynamics.
- **IE**, an integrating EoS reader, which lies inside R14-5's own reader class. It reads the content's equilibrium EoS once at a first equilibrium instant, R(u₀) = ρ_EoS(T(h₀)) − ρ_EoS(0). After that it integrates R′ = −3h.

**What is shown.**
- **IE has g ≡ 0 on every homogeneous history with conserved total stress** (proved, `r166_identity.out:2`). It annihilates constants, so a constant vacuum of any size never enters it.
- **Λ̃_late = 0 holds exactly when the first reading is exact and the late vacuum is the EoS's T = 0 vacuum** (proved).
- **Checked through the stated history:**
  - the QCD crossover (identity; numerics only at the finite-difference level);
  - e⁺e⁻ annihilation with decoupled neutrinos;
  - a supercooled first-order transition (the control): g ≡ 0 for IE at every depth tried, with B/ρ_r from 0.36 to 2.3e3;
  - m²φ² inflation plus reheating: 65.2 accelerating e-folds, g ≡ 0, Λ̃_late = 0;
  - DESI-like CPL: g ≡ 0.
- **Prices are named in §5.**

**Scope, stated plainly (each item matters):**
1. **What the removal is.** With g ≡ 0 the model is exactly GR with one fixed cosmological term equal to minus the late vacuum (vR14-5 correction: g ≡ 0 on an interval ⇒ GR). So the "removal" is Lemma PT's c-number subtraction (`TESTS.md:2986`), with the number supplied by the law's T = 0 EoS normalization rather than chosen by hand.
   - It keeps R14-5's vacuum-shift symmetry. Shifting the whole law by C changes nothing, and so do the relative vacuum shifts between phases.
   - But it is a stipulated reference, not a dynamical adjustment. Whether that counts as "untuned" is an owner/referee reading. vR14-5:35 says the plain g ≡ 0 unimodular branch "retains the usual vacuum-shift problem". That holds when λ is a free datum; it does not hold when the creation law fixes λ from the EoS, which is what IE does.
2. **R14-5's machinery becomes idle.** No CMC clock is forced (Lemma C case A), there is no λ(t) dynamics and no Lemma S signalling. What remains is GR plus site creation.
3. **Earlier vacua gravitate**, exactly as in standard cosmology: the EW/QCD bag terms, a supercooled false vacuum, and the inflaton plateau. This is forced by observation for inflation (§4.2).
4. **The late vacuum must be the law's T = 0 state.**
   - The SM alone is metastable (RECALLED), so this needs absolute stability (P-r166b).
   - No later random pick may choose among late vacua of different energy (Theorem NA, P-r166c).
5. **IE needs a first instant read exactly.** An error δ there is a permanent Λ̃ = κδ. G0 avoids the first instant but needs an exact state reading at every instant.
6. **Homogeneous only.** In a lumpy universe g ≡ 0 needs the zero-mode law to be GR's averaged constraint, equivalently the local Hamiltonian constraint with source ρ − C. With R14-5's FRW-form zero-mode law, a backreaction g/H² ~ 1e-5 remains (suggested, `R156:265-267`), and that signals (vR15-1:17).

**Why not FAIL.**
- The FIXED FAIL text asks for a proof that any out-of-equilibrium vacuum drop forces g ≠ 0 "for every reader giving Λ̃ = 0".
- **With Λ̃ = Λ̃_late it is false.** IE is a counterexample: through a supercooled drop of any depth, g ≡ 0 and Λ̃_late = 0 (`r166_supercool.out:8,12,16,20,24`), and the same holds through inflation's end and reheating (`r166_inflation.out:3`).
- **With Λ̃ = Λ̃_inst (zero at every instant, the false vacuum counted as "vacuum") it is true for every reader.** But that is already the refereed Lemma C(A)/Lemma PT (`C5_R14-5_report.md:187`; `TESTS.md:2986`). In that bookkeeping a potential-driven inflation cannot inflate at all (§4.2). So "R15-1's signalling is unavoidable for every universe with inflation" does not follow in either bookkeeping.

**FAIL-type results in narrower classes (for the referee):**
- **Theorem NA** (proved, elementary): with the input the same up to u₁ and a later pick among late vacua of different energy, no causal reader has g ≡ 0 and Λ̃_late = 0 on both branches. This excludes landscape-type laws.
- **Plateau dead band** (suggested; checked on one design): finite-memory readers in R14-5's class cannot drive slow-roll inflation. LIN gives 8.8 accelerating e-folds instead of 65.2, with g/H² up to +11, above the exact ghost line 6 (`r166_inflation.out:4`). The general version rests on the refereed N0 (vR15-4:41).

**Against the expectation (`TESTS.md:5245`).**
- The expectation was "FAIL for inflation's end by Lemma C unless reheating counts as equilibrium". Equilibrium is not what decides it. IE integrates straight through out-of-equilibrium reheating and supercooling with g ≡ 0.
- What decides it is whether the reader's zero is the late vacuum, fixed in advance.
- The "sticking point" (is the inflaton potential content or vacuum?) is settled by inflation itself: if the plateau is counted as vacuum, 3H² = κR does not see it, and there is no inflation.

---

## 1. In plain words

- **What g ≡ 0 means.** By R15-6's identity, g measures how fast the reader moves energy into or out of its "vacuum" bin. g ≡ 0 means the bin never changes: the reader subtracts one and the same constant at every instant. The model is then ordinary general relativity with that constant as its cosmological term. Nothing travels instantly.
- **Which constant.** For the late universe to show no cosmological constant, the subtracted constant must be the energy of the vacuum the universe *ends up in*. Every earlier, higher vacuum then weighs normally while it lasts: the hot quark–gluon phase's bag energy, a supercooled false vacuum, and the inflaton's potential. That is exactly how standard cosmology works, and inflation needs it.
- **How the rule can know it in advance.** A rule that reads only the past history of the density cannot know which vacuum lies ahead, unless the law tells it.
  - The thermodynamic equation of state does tell it: the EoS is always quoted relative to the zero-temperature vacuum (pressure zero at T = 0). So a rule that looks up the EoS once, at a hot equilibrium start, and then simply keeps the energy books gets the zero right forever.
  - It never needs to know the absolute vacuum energy, which can be anything.
  - This works through supercooling, reheating and particle annihilations, because keeping the books (energy conservation) does not care whether things are in equilibrium.
- **The catch.**
  - This is the old "normal ordering against the true vacuum" idea, written as a rule of the creation law. It does not explain why the vacuum does not weigh; it states it.
  - It needs our vacuum to be the law's true ground state. The Standard Model alone is thought to be slightly unstable.
  - It needs no later coin-flip deciding between vacua of different energy.
  - If the first reading is off by any amount, that amount becomes a permanent cosmological constant.
- **What it gives up.** None of R14-5's machinery is used: no global clock, no instant response. The observed acceleration must then be real dark energy, which for DESI's phantom-like fits means real phantom or coupled dark energy in GR.

---

## 2. Hypotheses and classes (stated before titles)

- **H-T.** Total stress is conserved and homogeneous: ρ_tot′ = −3h (`R156:84`).
- **H-Z (R14-5's model).** 3H² = κR; Lemma C: λ̇ = −gθ, and g ≡ 0 on an interval ⇔ λ constant ⇔ GR with a constant Λ_eff (`C5_R14-5_report.md:180-192`; vR14-5 correction: "on an interval").
- **H-vac-Λ.** The removed vacuum is a w = −1 c-number (`C5_R14-5_report.md:100`). The grid zero-point (w ≥ 0, R11-3) is outside scope; see P70 in §5.
- **Reader classes:**
  - **𝓗-read** (R14-5/R15-6): causal functionals of the ρ̄_tot history that annihilate constants. By Lemma B (vR15-6:5) these are functionals of the h-history.
  - **(i) literal P-EoS** (`R156:198`): R = ρ_EoS(T(h)) − ρ_EoS(0), evaluated instantaneously. This is in 𝓗-read.
  - **IE** (new): R(u₀) = ρ_EoS(T(h(u₀))) − ρ_EoS(0) at a first instant u₀ where the state is in equilibrium, then R′ = −3h. It is in 𝓗-read: it uses only h plus the law's EoS. It is causal, real, regular and linear in h after u₀. It is **not** in R15-4's 𝓡⁺ or N0 classes (integrator kernel with ∫|K|e^{4s} = ∞, start-dependent; vR15-4:41,43) and not in Theorem L's class (`R156:205`).
  - **G0** (class (ii), outside 𝓗-read): R = (energy density of the current state) − E₀, where E₀ is the T = 0 equilibrium vacuum energy of the supplied dynamics.
  - **(ii) general:** any reader with g ≡ 0.
- **Histories (`TESTS.md:5230-5235`):**
  - the QCD crossover (model EoS, RECALLED HotQCD-2014 coefficients). EW is treated analytically (§4.5);
  - e⁺e⁻ annihilation with instantaneous ν decoupling at 2 MeV (RECALLED approximation);
  - a bag-model supercooled first-order transition (control);
  - m²φ² inflation with perturbative reheating Γ = 0.05m;
  - DESI-like CPL.
- **Excluded:** a Z³ construction; inhomogeneous dynamics except the averaged-constraint remark; a BBN network; cubic or higher order; the source-bridge choice (`AX:187`).

---

## 3. Prior art (each counted once)

1. **Lemma C** (`C5_R14-5_report.md:180-196`; refereed with the "interval" correction in `vR14-5:24-25`). Case (A) g = 0 gives GR with Λ_eff = λ + κρ_v and is Lemma PT (`C5_R14-5_report.md:187`).
2. **Lemma PT** (`TESTS.md:2986`). In G1–G3, a prescribed c-number subtraction cannot protect the geometry across transitions (EW needs 1 part in 4.7e54).
   - IE/G0 *are* such a subtraction. They do not keep Λ̃_inst = 0 across transitions; they keep Λ̃_late = 0 by fixing the c-number to the late vacuum through the law.
   - The novelty claimed here is only that the c-number is the EoS's own normalization, read by the creation law. That is a price (§5), not an escape from PT.
3. **The vacuum-shift symmetry and "unimodular retains the problem"** (`vR14-5:29-35`).
4. **R15-6 Lemma I** (g/H² = V′/R) and **Lemma B** (𝓗-read readers are h-functionals), confirmed (vR15-6:5).
   - Its P-EoS suggestion (`R156:197-200`) is the starting point here. It was not run there.
   - Theorem M (MR on H1) and Theorem L are confirmed (vR15-6:7,9).
5. **R15-1 Lemma S.** The response is ultralocal at g = 0 (`C5_R15-1_report.md:137`), and there is signalling whenever g ≠ 0 (vR15-1:5,7,17).
6. **R15-4.** 𝓡⁺/N+ and the N0 dead band (vR15-4:34-43). N0 does not exclude infinite-memory readers (vR15-4:41).
7. **Comparators (RECALLED):**
   - the SM EW and QCD transitions are crossovers;
   - HotQCD 2014 (Bazavov et al., PRD 90, 094503) p/T⁴ parametrization coefficients, recalled, not fetched;
   - SM vacuum metastability at the measured m_t, m_h (Degrassi et al. 2012; Buttazzo et al. 2013), with an instability scale near 1e10–1e11 GeV;
   - Planck r < ~0.04 ⇒ ε ≲ 0.0025;
   - DESI DR2 w₀w_a preference of about 3–4σ;
   - a minimally coupled single scalar cannot cross w = −1 in GR (NEC);
   - Weinberg 1989's no-go concerns field adjustment, not a fixed reference.
8. **Repository grep** for "normal order", "ground-state energy", "integration constant" and "EoS reader" in `P/agents` (by name, in the files read). The only hits are R5-3 route 1 (unimodular integration constant, Lemma PT) and R15-6's P-EoS line. No prior IE or G0 construction was found.

---

## 4. Results

### 4.1 (a) Theorem Z: the characterization (proved; checked)

**Statement.** Under H-T and H-Z, homogeneously, with R > 0:
- (i) g = (κ/3)·dV/du with V = ρ_tot − R. This is R15-6's Lemma I, re-derived in `r166_identity.out:1` and counted once.
- (ii) Hence g ≡ 0 on an interval ⇔ R′ = −3h there ⇔ R = ρ_tot − C with one constant C (`r166_identity.out:5`).
- (iii) g ≡ 0 on the whole history together with Λ̃_late = 0 ⇔ **R ≡ ρ_tot − ρ_v,late at every instant.** The model is then GR with cosmological term −κρ_v,late (vR14-5:24).

**Answer to "does this coincide with 'the constant is a pure c-number in the EoS'?"** Yes, exactly, with one sharpening: the c-number must be the **late** vacuum's energy. Every other w = −1 stress belongs to the content's EoS and gravitates while present. That includes the QCD/EW bag terms, a false vacuum and the inflaton plateau.

**Corollary (bookkeeping; proved; this is PT, counted once).** If Λ̃_inst = 0 is demanded at every instant, then g ≡ 0 forces the instantaneous w = −1 stress to be constant. Any vacuum change then forces g ≠ 0 (Lemma C(A)).

### 4.2 Inflation needs the plateau to be content (proved, elementary; checked)

- In H-Z the expansion is 3H² = κR.
- Slow-roll inflation needs H² ≈ κ(V(φ) − V_late)/3 with H ≫ m_eff. So R must count the plateau's energy above the late vacuum.
- A reader that classes the plateau as "vacuum" (Λ̃_inst = 0) does not inflate.
- **Checked:**
  - G0 and IE give 65.2 accelerating e-folds from φ₀ = 16 (`r166_inflation.out:2-3`).
  - LIN, a two-register linear reader exact on dust and radiation (G(0) = 0, G(3) = G(4) = 1, G(0.01) = 0.0028, `:1`), gives 8.8, or 6.7 from φ₀ = 12. It reaches g/H² ∈ [−34, +11] and ends with Λ̃_late/ρ_nc = +0.18 (`:4-5`).
- **Suggested (general form):**
  - every 𝓗-read reader continuous at constants on a finite window has N0's dead band (vR15-4:41);
  - the plateau has x = 2ε ≲ 0.005 (Planck r < ~0.04, RECALLED);
  - so such readers under-read the plateau and cannot drive slow roll.
  - The quantitative size depends on the reader; only one design was run.
- **Identifiability (checked).** On the m²φ² attractor, h = φ̇² ≈ 2m²/3 regardless of φ₀. After 2 time units h = 0.6626, 0.6645 and 0.6654 for φ₀ = 12, 16 and 20, while ρ above V_min = 54, 104 and 169 (`:8-10`). An h-only reader cannot read the plateau's energy from a finite window except through O(ε) corrections. Only integration from a known start (IE), or reading the state (G0), recovers it.

**Consequence.** In R14-5's model, potential-driven inflation already requires a reader outside the finite-memory classes. The natural such reader (IE) is exactly the g ≡ 0 branch (reading).

### 4.3 The three readers

| Reader | In 𝓗-read? | g ≡ 0 on | Λ̃_late = 0 needs | Fails on |
|---|---|---|---|---|
| (i) literal P-EoS | yes | equilibrium single-T content (identity, `r166_identity.out:3-4`) | late vacuum = T = 0 EoS vacuum | decoupled sectors (e±: \|g/H²\| ≤ 0.052); supercooling (g/H² from +1.33 to −195); inflaton (h does not fix ρ) |
| **IE** | yes | **every history under H-T** (proved, `r166_identity.out:2`) | exact first reading at an equilibrium instant + late vacuum = T = 0 EoS vacuum | a first reading off by δ ⇒ permanent Λ̃ = κδ |
| **G0** | no (reads the state) | every history (R = ρ_tot − E₀ ⇒ V ≡ E₀) | late vacuum = E₀ (ground state) | metastable late vacuum ⇒ Λ̃_late = κ(V_ours − E₀) > 0 |

- **The h-blindness is not a problem for IE.** Lemma B says an 𝓗-read reader sees a w = −1 stress only through the latent heat (vR15-6:5). IE needs no more than that: the EoS supplies the false-vacuum energy at the first reading, and exact energy bookkeeping (R′ = ρ_tot′) carries it forward.
- **Scope note on `R156:142`.** That line says a supercooled false vacuum's "removal must then be absorbed, which forces g ≠ 0". This holds only for readers that remove the false vacuum, i.e. the Λ̃_inst bookkeeping. IE counts the false vacuum as content from its first reading (the false phase is the equilibrium phase above T_c), so nothing is absorbed (`r166_supercool.out:8-24`).
- **Positivity.** For G0, R = energy above the ground state ≥ 0, so H² ≥ 0 automatically. For IE with an exact first reading, R = ρ_tot − ρ_v,late, which is the same.

### 4.4 (b) Drops out of equilibrium

**Supercooled first-order transition** (bag model a_f = 1, a_t = 0.3, B = 1; nucleation at T_n with tanh width W in u). The output is `r166_supercool.out:7-26`.

| T_n/T_c, W | B/ρ_r at T_n | IE: g/H², ∫(g/H²)R du | P-EoS: g/H² range, ∫ | MR: ∫ | IE accelerating e-folds (false vacuum gravitates) |
|---|---|---|---|---|---|
| 0.9, 0.05 | 0.36 | 0, 0 | [−2.31, +1.33], 0 | −1.000 (= −B absorbed) | 0.00 |
| 0.5, 0.02 | 3.7 | 0, 0 | [−37.5, +1.33], 0 | −1.000 | 0.32 |
| 0.3, 0.02 | 29 | 0, 0 | [−70.6, +1.33], 0 | −1.000 | 0.84 |
| 0.1, 0.01 | 2.3e3 | 0, 0 | [−195, +1.33], 0 | −1.000 | 1.94 |
| 0.1, 0.20 | 2.3e3 | 0, 0 | [−12.9, +1.33], 0 | −1.000 | 1.99 |

- **IE (checked).** g/H² ≡ 0 to machine precision at every depth. Λ̃_late/ρ_nc just before nucleation is ≤ 9e-13. The constant offset (R − ρ_nc)/ρ_nc(u₀) is ≤ 1e-14 at the end.
  - The printed end values of Λ̃_late/ρ_nc (up to 3e-2) are that round-off offset divided by a density that has fallen by e^{−24}. That is the integration-constant sensitivity of P-r166d, seen numerically (`:3-4`).
- **Literal P-EoS.**
  - It first drops B from its count while the system supercools through the mixed-phase h-window. That is a reader-vacuum *rise*, g/H² = +1.33 at every depth.
  - It then restores B at nucleation, with g < 0.
  - Net ∫ = 0, but g ≠ 0, so it signals (vR15-1:17).
- **MR.** It never counts B, so it absorbs −B (Theorem M's sign, g ≤ 0). It signals during the conversion.
- **Theorem NA (non-anticipation; proved, elementary).**
  - **Setting.** Let a causal reader's output at u be a function of the realized state history up to u: any input that is a function of the realized history, including the full microstate. Let two allowed histories A and B coincide up to u₁, and then reach late vacua with ρ_v,late^A ≠ ρ_v,late^B. An example is tunnelling from a false vacuum into one of two lower minima, with the pick made by the realized state (`AX:63-66`, reading note (1)).
  - **Claim.** g ≡ 0 and Λ̃_late = 0 cannot hold on both.
  - **Proof.** By Theorem Z(iii), C_A ≡ ρ_v,late^A and C_B ≡ ρ_v,late^B. For u ≤ u₁ the states agree, so ρ_tot^A = ρ_tot^B and R^A = R^B, hence C_A(u) = C_B(u). That is a contradiction. ∎
  - **Scope.**
    - It binds G0 and IE equally.
    - It does not bind a law whose late vacuum is fixed by the law and the state at the first reading: a single minimum, or a unique endpoint of the realized branch structure.
    - For h-only inputs the same holds whenever the two histories also agree in ρ_tot up to u₁.

**Inflation's end and reheating (checked, `r166_inflation.out:2-3,6`).**
- G0 and IE give g ≡ 0 (G0 to finite-difference noise, |g/H²| ≤ 2.4e-6).
- Λ̃_late = 0, with the offset |R − ρ_nc|/ρ₀ ≤ 7e-16.
- Reheating completes (ρ_r/ρ_nc → 1).
- The perturbative inflaton decay is out of equilibrium. It needs no special treatment, because IE only keeps the books.

### 4.5 The SM history

- **EW crossover** (proved by identity, not run). With any thermodynamically consistent p(T) normalized at p(0) = 0, which includes a smooth Higgs-sector "bag" term, literal P-EoS and IE are exact (`r166_identity.out:3-4`; monotone h(T) because d(Ts)/dT = s + c_V > 0). The EW false-vacuum energy, about m_h²v²/8 ≈ (104 GeV)⁴ (RECALLED inputs), gravitates above T_EW. That is about 0.5% of the radiation at T ≈ 160 GeV with g_* = 106.75 (suggested arithmetic), exactly as in standard cosmology.
- **QCD crossover** (`r166_sm.out:9-13`; model EoS from RECALLED HotQCD coefficients).
  - The trace-anomaly ("vacuum-like") part that the EoS lets gravitate peaks at (ρ−3p)_QCD/ρ_tot = 0.31 at T ≈ 181 MeV (`:10`).
  - The numerical P-EoS check is only at spline/finite-difference level: the constructed history conserves ρ to 3.4e-3, and |g/H²| ≤ 1.3e-2 (`:11-12`).
  - Exactness rests on the identity, not on this run.
- **e⁺e⁻ annihilation with ν decoupled at 2 MeV** (`r166_sm.out:1-8`; the final T_ν/T_γ = 0.7154 against the textbook 0.7138 shows the construction is sane).
  - **Literal P-EoS** is wrong while e± are semi-relativistic: ε = R/ρ_nc − 1 reaches −1.14%, and g/H² reaches −0.052 (`:4`). It is exact again once only radiation remains, because ρ = (3/4)h for any radiation, so ΔN_eff ≈ 0 (`:6`). So literal P-EoS has a small g ≠ 0, and hence signalling, during BBN-era annihilation.
  - **MR** has ε within ±1.4% and g/H² within ±0.066, with a final −1.9e-4 (`:5,7`). For the real e± channel (annihilation into photons) MR's error is transient, not the −24% of R15-6's dust-like toy (`R156:191`; a refinement, not a correction).
  - **IE**, started above T_dec, is exact by construction (`:8`).

### 4.6 (c) What the observed acceleration must be under g ≡ 0

- **The model is GR with the late vacuum subtracted** (Theorem Z(iii); proved). A true cosmological constant equal to the late vacuum is unobservable: that is the removal. Today's acceleration must therefore be content above the late vacuum, which is true dark energy (S6, carried).
- **DESI-like CPL** (`r166_desi.out:1-3`).
  - IE gives g ≡ 0. The reading equals the truth, apart from the integration-constant round-off from a = 1e-4, which is 6e-4 of today's density (the same effect as in §4.4).
  - LIN mis-reads by −58% today, with g/H₀² = −2.2 (`:2`). That agrees with R15-6's MR −58% and R15-4's N+ (vR15-4:39).
- **R15-4's escape is unavailable at g ≡ 0** (reading). That escape was a non-phantom true DE whose *reading* equals DESI, costing g/H₀² of −0.3 to −1.1 (vR15-4:48-52). With an exact reader the reading equals the content.
  - So DESI's phantom crossing at z ≈ 0.41 (`:3`) must be real in the content: NEC-violating, non-minimally coupled or interacting dark energy in GR (comparator RECALLED).
  - Otherwise DESI's preference must be a fluctuation.
- **The dark-energy scale (about meV⁴) is not explained.** It is a separate coincidence problem: P-r166e = S6.

### 4.7 Signalling and lumps

- **Homogeneous (proved).** g ≡ 0 is GR on every interval (vR14-5:24). R15-1's Lemma S response is then ultralocal: Δδ̇ = F (`C5_R15-1_report.md:137`; vR15-1:5). The CMC clock may be kept only as a gauge clock; it carries no gauge-invariant signal at g = 0 (`C5_R15-1_report.md:216`, reading).
- **Lumpy (suggested).**
  - With R14-5's FRW-form zero-mode law and any exact homogeneous reader, Lemma I picks up −B′/(κR) with B = ½⟨R⁽³⁾⟩ − ½⟨σ²⟩. So g/H² ~ 1e-5 at late times (`R156:265-267`), which is a nonzero g and so signalling (vR15-1:17).
  - **g ≡ 0 with lumps needs the zero-mode law to be GR's averaged Hamiltonian constraint.** Equivalently, there is no separate zero-mode law: the local Hamiltonian constraint holds with source ρ − C at all k, with the same C. C is fixed once (IE) or by the ground state (G0).
  - This is then V2-type GR plus a law-fixed compensator. That is exactly R13-3's Lemma T, "unless a tuned compensator is added" (`TESTS.md:4724`). The compensator here is the law's T = 0 normalization (P-r166a).

---

## 5. Prices (named, none adopted)

| # | Price | Axiom text touched | Status |
|---|---|---|---|
| **P-r166a** | **The creation law's gravitating zero is the T = 0 vacuum of the supplied dynamics.** It enters through the EoS normalization p(0) = 0: read once (IE), or as E₀ (G0). This is "the creation law knows the EoS". | Needs supplied dynamics and an EoS, which are not axiom content (`AX:116-130`). Source/action bridge `AX:187`. Reading: `AX:94` ("a law privileges no states"); the T = 0 state is used as a reference, distinguished by supplied structure as in `AX:52`. **Not a change to the four axiom texts** unless the creation law itself (P52/P53, already a Lattice price, `AX:37`) is written into axiom text, in which case this reference goes into that text. | proved sufficient (Theorem Z, IE); reading on AX:94 |
| **P-r166b** | **Late-vacuum stability.** Our vacuum must be the law's T = 0 equilibrium state. The SM alone is metastable at the measured masses (RECALLED), so this needs stabilizing physics, or else Λ̃_late = κ(V_EW − E₀), positive and large. | `AX:187`; downstream content | suggested (comparator RECALLED) |
| **P-r166c** | **No later pick among late vacua of different energy** (Theorem NA). This excludes landscape-type laws with branching (`AX:63-66` reading note (1)). | `AX:57-62` (the distribution's form is downstream) | proved (elementary) |
| **P-r166d** | **IE only: a first exact reading** at an equilibrium instant. An error δ is a permanent Λ̃ = κδ, so a Planck-era start needs exactness to ~1e-120 of ρ₀, i.e. the reading must be an exact law identity, not an approximation. A beginning is in the same class as E1's t₀ (S17 owner Q1, `C5_S17_synthesis.md:279`). G0 trades this for an exact state reading at every instant. | `AX:94`, `AX:185-186` | proved (algebra); checked numerically as round-off growth (`r166_supercool.out:3-4`) |
| P70 (carried) | A w = −1 vacuum. Under g ≡ 0 the subtracted stress must be ∝ g_μν. Under the grid zero-point (w ≥ 0, R11-3) and without momentum exchange, ρ_v + p_v = 0 is required (vR15-1:15). | `AX:187` | carried |
| P-r166e = S6 (carried) | Late acceleration is true DE above the zero. DESI's phantom crossing must then be real (NEC-violating or coupled DE in GR). R15-4's reading-distortion escape is not available. | `AX:187` | reading |
| P52 (carried) | Site creation, if V2/V3 (fixed proper site density) is kept | `AX:37` | carried |
| **Dropped** | P68 (CMC lattice time as a physical clock; it may remain as a gauge clock), P-r15-1a (signalling), P67's global P-T reader, P-r156b (fast-transition exclusion or large \|g\|) | — | by Theorem Z with g ≡ 0 |

**Answer to (d), "is 'the creation law knows the EoS' a new axiom text?"** (reading). It is a new premise of the creation law and a source/action bridge item (P-r166a). It is not a change to Lattice, Qubit, Admissibility or Record as written. Its only axiom-text exposure is through the site-creation price, already on Lattice, and the `AX:94` reading.

---

## 6. Notes for the referee

**Check:**
1. Theorem Z(ii)–(iii): the use of Lemma I (R > 0) and "g ≡ 0 on an interval ⇒ GR" (vR14-5:24).
2. IE's membership in 𝓗-read. It uses h only, plus the law's EoS at u₀. Its exclusion from 𝓡⁺/N0/Theorem L, by its kernel and start dependence.
3. Theorem NA: whether "same realized state up to u₁, different late vacua" is an allowed history class under `AX:63-66`.
4. Whether IE/G0 "remove a constant vacuum" under the PASS text. Against: PT and vR14-5:35. For: the vacuum-shift symmetry at the law level, and insensitivity to relative phase shifts. **This is the decisive judgement.**
5. The two bookkeepings of Λ̃ and the claim that Λ̃_inst = 0 is incompatible with potential-driven inflation in H-Z.
6. The supercooling numbers, especially P-EoS's +1.33 rise and MR's −B integral.
7. The e± construction (instantaneous decoupling; T_ν/T_γ check).

**Strong-word check:**
- "Every history" for IE: homogeneous, under H-T, with R > 0.
- "Exact": analytic; numerics to round-off, with the integration-constant growth shown.
- "Removes": in the Λ̃_late bookkeeping, under P-r166a–d.
- "Cannot drive slow roll": checked for one linear design; general for N0's class only as suggested.
- "No signalling": homogeneous; lumps need the local-constraint form.
- "PASS": scoped as in §0.

**What would change the picture:**
- a ruling that a law-fixed T = 0 reference is a tuning, which makes the reading INCONCLUSIVE and, in effect, PT again;
- a ruling that the late vacuum is decided by branching (the landscape), which makes Theorem NA bind;
- confirmation of SM metastability without stabilizing physics in the supplied law (P-r166b fails);
- an inhomogeneous IE/G0 construction with the local constraint, and a Z³ encoder.

## 7. Files

- Report: `S/R16-6_report.md`.
- Scripts and outputs: `S/scripts/r166_identity`, `r166_supercool`, `r166_inflation`, `r166_sm`, `r166_desi` (each `.py` with its `.out`).
