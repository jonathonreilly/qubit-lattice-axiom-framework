# C5 R17-3 report: Λ after R16-6. Can anything in the four axioms force the gravitating zero, or is it necessarily a tuning?

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-13, 00:08Z to 00:33Z. No repository file was edited.

**Scratch folder.** `S/` = `.../scratchpad/C5/R17-3/`. Scripts and outputs are in `S/scripts/`; each runs in under 15 s at `OMP_NUM_THREADS=2`.
- `r173_records_inflation.py/.out`: record sourcing (i) in R16-6's inflation + reheating history, under three record rules (REC-S, REC-vac, REC-mass).
- `r173_recordmap_vacuum.py/.out`: the one record map realized on file (W1 pinching of the KS sea), applied to the vacuum; the trace zero; physical sizes.
- `r173_global_constraint.py/.out`: (ii) early-time sensitivity, final-state consistency, the causal running 4-volume average.
- `r173_avg4_inflation.py/.out`: the running 4-volume average through inflation.
- `r173_recvac_scan.py/.out`: the unrecorded-plateau rule (REC-vac) for φ₀ = 16 to 150.
- `r173_symmetry_radiative.py/.out`: (iii) shift invariance (sympy), reflection symmetries, Lemma U, one-loop sizes, the which-minimum-is-global toy.

**Read.**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (`AX`); the C5 method `TESTS:2302-2320`; the Round 17 head and the item `TESTS:5685-5812`; `agents/C5_R16-6_report.md` (`R166`) and `C5_R16-6_referee_verdict.md` (`vR16-6`); `C5_R14-5_referee_verdict.md` (`vR14-5`); `C5_R15-1_referee_verdict.md` (`vR15-1`); `C5_R5-3_report.md` (`R53`) and `C5_R5-3_referee_verdict.md` (`vR5-3`); `C5_R10-4_referee_verdict.md` (`vR10-4`); `docs/THE_RECORD_MAP_KEEPS_THE_MASS_FRACTION_..._2026-09-04.md` (`RM`); `docs/THE_VACUUM_QUESTION_IS_ONE_COEFFICIENT_OF_THE_LAW_..._2026-09-03.md`.
- In part: `C5_S20_synthesis.md` (`S20`: §1.6 `:207-230`, P92/P93 `:387-388`, Q1 `:464-475`, caveats `:852-873`); `C5_R14-5_report.md:1-200`; `C5_R15-1_report.md:122-245`; `C5_O3_report.md:95-104` and `C5_O3_referee.md:13` (`vO3`); `C5_R10-4_report.md:296-306`; `C5_R4-4_report.md:200-206`; `TESTS:2968-2993` (R5-3 record), `4157-4190`, `4297-4301`, `4417-4424` (R10-4, R11-3), `4715-4720` (R13-1); `SUMMARY.md:677-714` (§26); the R16-6 runner `scripts/C5/R16-6/r166_inflation.py/.out`.
- Memory notes on the owner's thoughts (`records-count-rises-until-frozen`, `stadium-picture-20260930`): treated as hypotheses only.

**Labels.** proved / checked (sympy or numerics this run) / suggested / reading / comparator (RECALLED unless stated; nothing was downloaded).

**Units and subtraction rule (named before the runs).** Homogeneous, κ = 1, u = ln a, 3H² = R (R16-6's H-Z). h := (ρ+p)_tot. **C := ρ_tot − R** (the non-gravitating part). **Λ̃_late := R − (ρ_tot − ρ_v,late) = ρ_v,late − C.** Nothing else is subtracted. Every tail in the runs (B3's residual, REC-mass's late ratio) is measured against V_late only.

---

## 0. Verdict against the FIXED readings (`TESTS:5809-5811`)

**Worker reading: TUNING, in the precise form of Theorem T (§4.0), for the referee. ENFORCED is not met.**

**What Theorem T says.** In a stated class 𝒦 that contains (i), (ii) and (iii), every law with g ≡ 0 and Λ̃_late = 0 uses exactly one of three things:
- **(N) an independent exact number:** C fixed apart from the matter law, so Λ̃_late = 0 holds only on a proper analytic subvariety of the matter parameters. Every loop or threshold change breaks it (one-loop sizes 1.7e31 ρ_Λ for the electron to 6.7e53 ρ_Λ for the top, checked).
- **(A) a final-state input:** C reads data after a branch point. Then a later vacuum change shifts 3H² by exactly ΔV at every earlier time. Once the vacuum pick is Hubble-sensitive (outside H-blind), a final-state rule has windows with no consistent history or with two (checked).
- **(S) the number-free ground-state reference:** C ≡ V_late(θ) identically. This is R16-6's P92. vR16-6:18-26 already classes it as the late-vacuum counterterm unless something enforces it. §4.1–4.3 find that nothing in (i), (ii), (iii) or the four axiom texts enforces it.

**Why TUNING and not OPEN, and the one point the referee must rule on.** The FIXED TUNING text asks for "an independent exact number, or an acausal (final-state) input". (S) needs neither a number nor a final-state input. It is an exact *rule* that names the matter law's endpoint energy. So TUNING holds only through the standing R16-6 ruling that (S), as supplied, is the counterterm. **If the referee instead holds that a number-free stipulated rule is not "an independent exact number", the strict reading is OPEN, and Theorem T still stands.**

**Why not ENFORCED.**
- (S) meets the inflation, causality and continuous radiative-stability clauses. It is GR with Λ_bare = −κE₀[H] (§4.4).
- But it is stipulated, not forced by a symmetry, constraint or theorem (rule `TESTS:5701`).
- It also needs our vacuum to be the global minimum (P93) and no branching among unequal late vacua (P94).

**The three candidates, one line each.**

| Candidate | Result | Labels |
|---|---|---|
| **(i) record sourcing** | In its literal form it **cannot give inflation and then reheating with g ≡ 0** (a dilemma): an unrecorded plateau inflates only through g ≠ 0 (R15-1 signalling), and a recorded plateau is permanent and never becomes radiation. In reader form it is Theorem Z with C = the unrecorded energy, so it must leave exactly V_late unrecorded, which is (S) or (N). Its natural zero ("absence weighs nothing") needs I, additivity and I(∅) = 0, which were removed from Record on 2026-08-13. The one record map on file records the vacuum, and its recorded vacuum energy jumps by (c₀/2)m²M_P² at every mass threshold | proved (dilemma, textual); checked |
| **(ii) global constraint** | Exact C = V_late from a constraint needs final-state input whenever branching is allowed (A). A causal constant constraint is (N) or (S). A causal time-dependent one (running averages) is active compensation: g ≠ 0, and through inflation it gives 1.3 accelerating e-folds with g/H² down to −5e3 | proved; checked |
| **(iii) vacuum-shift symmetry** | Λ̃_late is invariant under the shift, so the shift cannot constrain it. The shift moves C freely and has no fixed point. Reflection symmetries fix the spectral midpoint; for the KS sea that is −1.05e123 ρ_Λ. Of the symmetries checked, only supercharge positivity (H = {Q, Q†}, unbroken) or exact dilatations fix the bottom; both are excluded for our vacuum (tested subclasses; comparator) | proved; checked; comparator |

**Against the expectation (`TESTS:5812`).**
- The expectation "TUNING for (i) and (iii)" is confirmed, and (ii) needs the acausal input, as expected.
- **Two changes:**
  1. The "tuning or acausal" theorem is really a **trichotomy**. Its third branch (S) is number-free, so it is a tuning only by the R16-6 classification. With g ≡ 0, owner Q1 therefore reduces to a choice among three things, not two:
     - a tuned number (Q1(c), P51);
     - a final-state law, which is ill-posed once the vacuum pick is gravity-sensitive (B2);
     - the principle "the lowest state of the law weighs nothing" (Q1(b); Lemma U shows it is the unique number-free form).
  2. Literal record sourcing fails earlier than expected. It cannot carry a radiation era at all (Lemma M), whatever Λ does.
- **Changed hypotheses.** Each class removes one hypothesis of the governing prior no-gos:
  - (i) removes Lemma PT's state-independence (G3, `R53:79`);
  - (ii) removes Theorem NA's causal-reader hypothesis (`vR16-6:54`);
  - (iii) adds a symmetry, which PT's G1–G3 left out (`vR5-3:7`).

---

## 1. In plain words

- **The question.** Once gravity is ordinary general relativity (no faster-than-light correction), the universe's late expansion shows no cosmological constant only if gravity ignores exactly the energy of the vacuum the universe ends in. Is there a reason gravity ignores exactly that, or is it just set by hand?
- **What I found.** Within the stated class, there are only three ways to arrange it:
  1. **Set the number by hand.** Any change in any particle mass then needs a re-set, to between 31 and 54 decimal places.
  2. **Let the rule look at the end of history.** The rule then depends on the future, and with some ordinary physics it has no consistent solution at all, or two.
  3. **Write a principle: "the lowest-energy state of the law weighs nothing".** This needs no number. It automatically keeps up with every particle mass, and it is ordinary general relativity in every other respect. But nothing in the four axioms says it. Quantum mechanics cannot see absolute energy, only differences, so the principle is a new choice about gravity, not a consequence of anything already there. It also needs our vacuum to be the true lowest state, which the Standard Model alone is thought not to be.
- **"Only records are readable", as a gravity rule.** It looks promising: a site with no record cannot be read, so empty vacuum would weigh nothing for free. It fails for three reasons:
  - **Inflation.** If the inflaton's high-energy plateau is not a record, it does not weigh. Inflation then happens only through an instant, faster-than-light energy leak from the unrecorded plateau into recorded motion: 7 e-folds instead of 65 for the same potential, or 62 for a nine-times-larger field range, with the leak on throughout. If it is a record, it is permanent, so it can never turn into the hot radiation that started the Big Bang.
  - **Repository text.** "Absence weighs nothing" is exactly the I(∅) = 0 rule that the owner removed from the Record axiom on 2026-08-13.
  - **The record map on file.** It records the vacuum itself, with an energy that jumps at every particle-mass threshold, by up to 1e88 times the observed dark energy at a Planck grid spacing.
- **"Records are mass"** would make the vacuum weightless. But permanent records that each weigh a fixed positive amount can never thin out as fast as radiation does, so the universe could never have had its radiation era (needed for the light elements).
- **A symmetry.** The "shift all vacuum energies" symmetry from R14-5 says the absolute vacuum energy is invisible. But the quantity we need to be zero is itself unchanged by that symmetry, so the symmetry has nothing to say about it. The symmetries known to pin the bottom of the energy scale at zero are unbroken supersymmetry and exact scale invariance. Our world has neither.

---

## 2. Hypotheses and classes (stated before titles)

- **H-Z, H-T** (R16-6 setting, `R166:87-89`): 3H² = κR, total stress conserved, R > 0, homogeneous.
- **H-g0:** g ≡ 0 on the whole history (no R15-1 signalling; Lemma S is ultralocal at g = 0, `C5_R15-1_report.md:137`).
- **H-late:** Λ̃_late = 0.
- **H-vac-Λ:** the vacuum is a w = −1 c-number (`R166:89`). The grid zero-point (w ≥ 0, R11-3, `TESTS:4417-4420`) is outside scope except for a remark in §4.4.
- **Law family.** {L_θ : θ ∈ Θ}, with Θ ⊂ ℝⁿ connected and open: masses, couplings, the inflaton potential. A history is h = (θ, s₀, ω): parameters, initial state, and branch picks. Branch picks are allowed by `AX:63-66`, reading note (1).
- **H-blind:** ρ_tot(u; h) and ρ_v,late(h) are fixed by the matter law. They do not depend on gravity's data γ or on C. Matter does not relax toward gravity's zero.
- **H-an:** ρ_v,late(θ, s₀) is real-analytic in θ on Θ, and is not constant there (true of the SM: EW and QCD thresholds move it, `R53:107-110`).
- **Classes (all contained in 𝒦):**
  - (i) R = the recorded content, in either form:
    - (i-lit): an additive function of permanent record readouts;
    - (i-rd): any rule that decides what is recorded.
  - (ii) C fixed by a global constraint, causal or not.
  - (iii) R covariant under R14-5's shift (`vR14-5:29-33`), plus any further symmetry.
- **Excluded alternatives (rule "Forks", `TESTS:5704`):**
  - **(iv) Relaxation:** the late vacuum adjusts to C. Examples are an H-sensitive relaxing field, Brown–Teitelboim or Bousso–Polchinski steps with selection, or Admissibility weights that read the local expansion. *Why excluded:* it breaks H-blind, and it is not in (i)–(iii). §4.5 states a necessary condition it must meet.
  - **(v) Active compensation (g ≠ 0):** R15-1 FAIL (`vR15-1:17`). The item's setting excludes it.
  - **(vi) Accepting a residual** (an anthropic distribution of Λ̃_late): outside H-late.
  - **(vii) Inhomogeneous laws beyond GR's local constraint with one C** (`R166:229-235`).
  - **(viii) Non-Bianchi or non-metric source bridges:** Lemma PT's G1 outside (`R53:81-84`).
  - **(ix) A non-analytic or constant V_late(θ):** H-an. The constant case is §4.3's supercharge route.

---

## 3. Prior art (each counted once)

1. **R16-6 and its verdict.**
   - Theorem Z: g = (κ/3)(ρ_tot − R)′ (`vR16-6:5-14`).
   - IE and G0; P92 judged as the counterterm (`vR16-6:18-28`).
   - Theorem NA, narrowed (`vR16-6:52-54`).
   - Inflation needs the plateau to gravitate (`R166:143-158`; `vR16-6:50`).
   - Theorem Z is used below and not re-derived.
2. **R5-3 Lemma PT** (`TESTS:2985-2988`; `R53:90-115`; `vR5-3:5-7`).
   - A state-independent c-number subtraction is undone by Bianchi. The EW step is 4.7e54 ρ_Λ.
   - R53:113 already states that "a vacuum-referenced or 'records-only' source rule cannot remove phase-transition differences" in any Bianchi metric theory.
   - Route 1b, the future datum Λ6 (`R53:128-137`), is (A) here.
   - Route 3 (KP sequestering) is bounded EXCLUDED (`vR5-3:9-13`).
   - Route 4, records forming until frozen, leaves a free constant (`vR5-3:23-25`).
3. **R14-5's vacuum-shift symmetry** and "unimodular retains the problem" (`vR14-5:27-35`).
4. **R15-1** Lemma S and Lemma V (d-i)/(d-ii) (`vR15-1:5,15`).
5. **R10-4.**
   - The minimal q-charge needs μ chosen for the final vacuum, to 2.1e-55 at EW (`vR10-4:9,27`).
   - "Until frozen" points away from zero (`C5_R10-4_report.md:304-306`).
6. **R11-3:** the grid zero-point has w ≥ 0 (`TESTS:4417-4419`).
7. **O3's vacuum table** (`C5_O3_report.md:95-104`), with the referee's corrections (`vO3:13`):
   - #3: unbroken nilpotent SUSY gives exactly 0, but "excluded" is too strong observationally;
   - #4: broken SUSY ≥ Δ⁴;
   - #9: a frustration-free empty vacuum, class-bounded (z ≥ 2);
   - #10: the negative-energy mirror;
   - #12: **records-only sourcing, "the vacuum is not a record"**, recorded there as a reading and a source/action bridge.
8. **R13-1** (`TESTS:4715-4720`): an exact D2 supercharge algebra is forbidden in the class with C¹ periodic one-body momentum and a whole-zone Peierls vertex.
9. **The record-map note** (`RM:48-104,147-159`).
   - W1 pinching keeps the diagonal mass energy, r_v = −(m²/2)[(M²+m²)^(−1/2)]_vv.
   - T4: "P0 removes any additive constant source … cannot determine the cosmological Lambda".
10. **R4-4:** "records are mass" as weight-from-records fails composition tests by 7+ decades (`C5_R4-4_report.md:206`).
11. **The owner's thoughts** (memory; hypotheses only). Records form while neighbourhoods allow; there is no sealed box; frozen = black hole; "records are mass?".
12. **Comparators (RECALLED):**
    - Weinberg 1989 (no-go for adjustment);
    - Kaloper–Padilla sequestering;
    - Henneaux–Teitelboim;
    - Brown–Teitelboim and Bousso–Polchinski (empty-universe problem);
    - Graham–Kaplan–Rajendran relaxation (details not recalled reliably; not used);
    - SM vacuum metastability at the measured m_t and m_h;
    - SUSY vacua in supergravity have Λ ≤ 0;
    - BBN fixes the radiation-era expansion rate to a few per cent (N_eff);
    - Planck 2018 ρ_Λ.
13. **Repository grep.** I searched `P/` and `docs/` for relaxion, Graham/Kaplan, Brown–Teitelboim, Bousso, final-state, normal order, ground-state energy, "does not weigh" and weightless.
    - New hits beyond 1–12: R10-4's membrane rows (`C5_R10-4_report.md:44,54,184-197`), counted in item 5.
    - "Final-state" hits in `C5_Q1_report.md` and `C5_O5_synthesis.md` concern substrate postselection, not Λ.
    - No prior trichotomy, Lemma U, Lemma M or record-sourcing inflation dilemma was found.

---

## 4. Results

### 4.0 Theorem T, the trichotomy (proved, elementary)

**Statement.** Assume 𝒦 = H-Z, H-T, H-g0, H-late, H-vac-Λ, H-blind and H-an. By Theorem Z (counted once), R = ρ_tot − C with C constant, and C = ρ_v,late(h). Write C = Γ(γ, ·) for the gravity rule. Then exactly one of the following holds:
- **(A)** Some θ has histories h, h′ that agree up to u₁ and have ρ_v,late(h) ≠ ρ_v,late(h′). Then C at u < u₁ must differ between them, so the rule reads data after u₁ (Theorem NA, `vR16-6:54`).
- **(N)** There is no such branching, so ρ_v,late = V(θ, s₀), but Γ − V is not identically zero on Θ (for example, Γ does not depend on θ). Then Λ̃_late = 0 holds only where Γ = V. By H-an and the identity theorem, that is a proper analytic subvariety of Θ: nowhere dense, of measure zero. **That is an independent exact number**, and it fails under any perturbation of θ along ∂_θV ≠ 0.
- **(S)** Γ depends on θ with Γ ≡ V(θ, s₀) on Θ. Then the rule contains the functional θ ↦ ρ_v,late(θ): it references the matter law's endpoint vacuum energy. This uses no number. It needs no branching (P94), and if Γ = E₀[H], it needs the endpoint to be the ground state (P93).

Mixed cases (Γ ≡ V on part of Θ) are (N) on the rest.

(S) also contains an "endpoint-of-the-trajectory" reference, Γ = V(θ, s₀) for a law whose late vacuum depends on the initial basin. That rule must solve the future dynamics from s₀. It satisfies H-late without P93, but states below the endpoint then weigh negative, so it fails Lemma U's positivity (reading).

**Proof.** Theorem Z gives R = ρ_tot − C and C = ρ_v,late. Either C depends on post-branch data, which is (A), or it does not. In the second case Theorem NA (narrowed) forbids unequal late vacua among histories that share their past, so ρ_v,late = V(θ, s₀). Then Γ − V is real-analytic in θ on connected Θ. Either it vanishes identically, which is (S), or its zero set is a proper analytic subvariety, which is (N). ∎

**Where (i)–(iii) land.** (i) → (S) or (N), or fails outright in literal form (§4.1). (ii) → (A), or (N)/(S) if causal and constant (§4.2). (iii) → (N), because C is a modulus (§4.3).

**Lemma U (uniqueness of the number-free reference; proved, elementary; checked `r173_symmetry_radiative.out:4-17`).** Take a gravitating energy of the form ⟨H⟩_ψ − ref[H], with ref shift-covariant (ref[H + c·1] = ref[H] + c). It is ≥ 0 on every state and = 0 on some state **iff ref = E₀ = min spec H**.
- *Proof.* ≥ 0 on all states ⇔ ref ≤ E₀. = 0 on some state ⇔ ref ≥ inf_ψ⟨H⟩ = E₀. ∎
- *Checked* on three random 6×6 H: E₀ passes; Tr H/dim and the midpoint fail both conditions.
- *Reading.* Shift covariance is what quantum mechanics already imposes: a global phase is unobservable (`AX:82-83` read as "only readable data source gravity"). Lemma U then says (S) is the unique rule that adds "weights are never negative" and "some state weighs nothing". The last condition is the target itself, stated at the bottom of the spectrum. So (S) is the principle "the lowest state of the law weighs nothing", and nothing weaker gives it.

**What the axioms supply (proved, textual).**
- The four axiom texts name no Hamiltonian, energy, ground state or source bridge (`AX:116-130,173-190`).
- They removed the scalar functional I, finite additivity and I(∅) = 0 (`AX:148-151,220-223`).
- So no axiom text can define E₀ or V_late, and none can force C = ρ_v,late. Any forcing must be added as a source-bridge premise at `AX:187`.

### 4.1 (a) Record sourcing (i)

**(a1) The natural zero is removed structure (proved, textual).** "Unrecorded sites weigh nothing" needs two things:
- a source that is a local scalar functional of record contents, i.e. additive over sites;
- the value 0 on absence.

That is I + additivity + I(∅) = 0, removed on 2026-08-13: "it does not assign a scalar value to absence" (`AX:221-223`; `AX:148-151`). So (i)'s untuned zero is a price, not axiom content. This sharpens O3 #12 (`C5_O3_report.md:104`), counted once.

**(a2) What gravitates during inflation (proved in H-Z; checked).**
- With R = ρ_rec, Theorem Z gives C = ρ_unrec. H-g0 and H-late then force **ρ_unrec ≡ ρ_v,late at every instant**, including during inflation.
- During inflation, therefore, the plateau excess V(φ) − V_late must be recorded and V_late must not be.
- A rule that records the false vacuum and not the true one must leave exactly V_late unrecorded. That is the counterterm in record form, which is (N), or the ground-state reference, which is (S).
- **Checked** (`r173_records_inflation.out:1-2`):
  - REC-S (everything above V_late recorded) gives 65.21 accelerating e-folds with g ≡ 0. This is the physical control: GR with Λ_bare = −V_late is known to inflate and end at Λ̃ = 0. It reproduces R16-6's G0, counted once.
  - REC-vac (plateau unrecorded) gives 7.17 accelerating e-folds, with g/H² ∈ [−22.9, +1.73]. The rise in R is unrecorded potential energy leaking into recorded kinetic energy. That leak is g ≠ 0, which is R15-1 signalling.
  - **The scan over φ₀** (`r173_recvac_scan.out:1-4`) gives N_accel = 7.08, 21.1, 41.6 and 62.1 for φ₀ = 16, 50, 100 and 150. This tracks the friction-balanced estimate N ≈ φ₀/√6 (suggested). Throughout, the median g/H² is −1.5 to −0.6, with excursions to +20.5, above the exact ghost line 6 (`vR15-1:11`).
  - So an unrecorded plateau *can* inflate, but only through the g ≠ 0 channel. That excludes it under H-g0.
  - **Correction to `R166:147` ("a reader that classes the plateau as vacuum does not inflate").** The statement holds for potential-driven slow roll (`vR16-6:50`). It is false for leak-driven acceleration, which needs g ≠ 0.

**(a3) Lemma P + Lemma M: the literal record-sourcing dilemma (proved under (i-lit); checked).**
- **(i-lit) hypotheses:**
  - the gravitating source is an additive function of record readouts;
  - records are permanent and read by content alone (`AX:79-83`);
  - one record per site.
- **Lemma P (permanence).** A site whose record locks the false-vacuum possibility keeps that readout forever. Under (i-lit), its weight never converts into radiation.
- **Lemma M (monotone weight).** If every record's weight is fixed and nonnegative ("records are mass", count-type), then a³ρ_grav = Σ (weights of records formed so far) never decreases. So the gravitating source has w_eff ≤ 0 at all times (d ln(a³ρ)/d ln a = −3w ≥ 0). A radiation era (w = 1/3) is impossible for it.
- **The dilemma.** Under (i-lit) and H-g0, inflation followed by reheating is impossible:
  - an unrecorded plateau inflates only through g ≠ 0, i.e. R15-1 signalling (REC-vac and the scan above). That is excluded by H-g0;
  - a recorded plateau does inflate, but its weight is permanent and never becomes radiation.
- **Checked, REC-mass** (`r173_records_inflation.out:3-8`; records form on new sites while comoving energy grows):
  - 64.88 accelerating e-folds;
  - the min step of a³R is −4.6e-16 relative (round-off), so a³R is non-decreasing;
  - over the last 3 e-folds, w of the gravitating source is 0.0000, against 0.3333 for the true content;
  - R/ρ_nc grows 1.84 → 2.29 → 4.71 → 12.7, and g/H² ∈ [−0.29, +0.42] (signalling).
- **Against observation (comparator, RECALLED).** BBN fixes the radiation-era expansion rate to a few per cent, which needs radiation to gravitate with weight close to 1.
- **Escape.** Signed weights written by the formation law. Then the formation law must compute ρ_tot − C at every instant (Theorem Z again), which is (i-rd) → (S) or (N).
- **The owner's "records are mass" (hypothesis).** It does make the empty vacuum weightless. But as the whole gravitating source it fails Lemma M independently of Λ, consistent with R4-4's composition failure (`C5_R4-4_report.md:206`, counted once). To fix it, records would have to be "energy above the vacuum", and that is (S).

**(a4) Is the false vacuum "recorded" in the one realization on file? The vacuum is (checked).**
- The record-map note's W1 pinching (`RM:48-58,64-72`; readout bridge: rank-one projectors onto full occupation configurations, `RM:25-27`) keeps the half-filled sea's diagonal mass energy.
- **Reproduced exactly** (`r173_recordmap_vacuum.out:2-6`): r_v = −0.021413851317, −0.201703227917, −0.648782512263, −2.781026669919 at L = 8, m = 0.3, 1, 2, 6, and −0.200917464424 at L = 12, m = 1, all matching RM. This is a reproduction, not a physical control.
- **New here:**
  - r_v = −(m²/2)⟨(m² + Σ4cos²k)^(−1/2)⟩_BZ, with c₀ = lim_{m→0} ⟨…⟩ = **0.4553** (`r173_recordmap_vacuum.out:11-14`). So r_v ≈ −(c₀/2)m² per site.
  - **The recorded vacuum energy moves at every mass threshold.**
  - With the scale bridge a = ℓ_P, which is OPEN (`AX:189-190`), the shift per staggered field is (c₀/2)m²M_P²: **3.5e77 ρ_Λ (electron) to 4.0e88 ρ_Λ (top)** (`r173_recordmap_vacuum.out:22-26`). That is m²/a², far beyond the m⁴ EW step of 4.7e54. O(1) factors from the lattice light speed (c = 2 in these units, `RM:117`) are not tracked; the sizes are orders of magnitude.
- **v_max for the KS symbol** (rule `TESTS:5695`). E² = m² + Σ(2 − 2cos p_a), with v_a = 2 sin p_a/E (`RM:117`). Since Σsin²p_a ≤ 4Σsin²(p_a/2), |v| ≤ c = 2 over the whole zone, with the bound approached at p → 0, m = 0 (proved). So v_max/c = 1.
- **Reading.** In the only realized record map, the vacuum is a record configuration with m-dependent weight. "The vacuum is not a record" (O3 #12) is false in that realization.

**(a5) Answer to probe (a).**
- What gravitates during inflation: the plateau above V_late, recorded.
- Why is the late vacuum not recorded? Only because a rule says so, and the rule must name V_late: (N) or (S).
- An unrecorded false vacuum means inflation only through g ≠ 0 (signalling).
- In literal form, a recorded false vacuum means no reheating.

### 4.2 (b) A global constraint (ii)

**(b1) Exact cancellation of an unknown late vacuum needs post-branch data, and then early gravity depends on the late vacuum (proved; checked).**
- On two branches that share their history up to u₁, H-late gives C = V_late on each. So **3H²(u) differs by exactly ΔV_late at every u < u₁**.
- Checked: the difference is 0.020000 = ΔV at u = 0, 1, 1.9, with relative size 2e-2, 1.09 and 40 (`r173_global_constraint.out:2-4`).
- So **yes: a late vacuum change alters early-time gravity**, by ΔV in 3H² at all earlier times. This is generic: it holds for any final-boundary-condition law in GR, not just this model. For ΔV ~ ρ_Λ it is about 7e-36 of ρ at BBN (arithmetic, RECALLED inputs), so it is acausal in principle and invisible in practice.
- KP's ⟨R⟩ = 0 rule is bounded EXCLUDED (`vR5-3:9-13`, counted once). Local and Gauss–Bonnet sequesters are not covered here. Any of them that cancels the late vacuum exactly under branching falls under (b1).

**(b2) A final-state rule is not an initial-value law (checked; the toy is exact).**
- Set C = V_late and a decay at u₁ triggered by H²(u₁), a Hubble-sensitive tunnelling rate (comparator: Hawking–Moss-type rates depend on H). **Scope:** H² depends on C, so this matter law is *not* H-blind. It is a type-(iv) coupling, and B2 lies outside Theorem T's class. Its point: (A) is ill-posed as soon as the vacuum pick is gravity-sensitive at all, and generic rates are.
- **No consistent history** for a type-1 trigger (decay iff H² < H_*²) with H_*² ∈ (0.00011, 0.00678): rows H_*² = 0.0025 and 0.0050.
- **Two consistent histories** for type 2 (decay iff H² > H_*²) in the same window (`r173_global_constraint.out:6-33`).
- Outside the window exactly one history exists. That is the control.
- **Consequence.** With gravity-sensitive matter, (A) needs a further selection rule to be a law at all. This sharpens R5-3's "fixed-point problem with no guaranteed solution" (`R53:133`) from suggested to checked, in a toy.

**(b3) A causal but time-dependent global constraint is active compensation (checked).**
- **The rule.** C(t) = the a³-weighted running average of the w = −1 part. The vacuum detector is granted here.
- **Late times.** C − V_late = ΔV(t_tr/T)³ → 0, but g = C′/3 ≠ 0 at every finite time (g/H² = −3.4e-2 down to −6.8e-8 as T goes from 2 to 1e6; `r173_global_constraint.out:35-40`). That is R15-1 signalling.
- **Today.** Order-of-magnitude residuals are tiny: 1e-19 ρ_Λ (EW), 2e-15 (QCD), 6e-27 (inflation) (`r173_global_constraint.out:42-44`, RECALLED epochs). It is a near-miss, killed by the g ≠ 0 rule.
- **Through inflation** (`r173_avg4_inflation.out:1-2`). With the plateau counted as vacuum, the average relaxes onto the plateau within about 1/(3H):
  - 1.27 accelerating e-folds (1.23 from φ₀ = 12);
  - g/H² ∈ [−5.2e3, −22], far past the ghost line 6.
- Only a reader told which w = −1 stress is the *late* one avoids this, and that is (S).

**(b4) Answer to probe (b).**
- A constraint that fixes C = ρ_v,late exactly, in a class with branching, is a final-state law (A): early gravity depends on later vacuum changes (b1), and consistency can fail (b2).
- Without branching, a causal constant constraint is (N) or (S).
- A causal varying one is R15-1.

### 4.3 (c) The vacuum-shift symmetry (iii) and its extensions

**(c1) Shift invariance cannot select C (proved; sympy).**
- Under S_c: ρ_v → ρ_v + c, λ → λ − κc, every vacuum level is shifted and **Λ̃_late = λ + κρ_v,late is invariant**: difference 0 (`r173_symmetry_radiative.out:1`). A symmetry places no constraint on its invariants.
- Extended to the creation law:
  - 𝓗-read readers annihilate constants, and IE's R′ = −3h is invariant because h_vac = 0.
  - The datum C is translated, C → C + c (`:2-3`). A free translation action has no fixed point, so no value of C is selected.
  - C is a modulus. This generalizes `vR14-5:35`.

**(c2) Reflection symmetries fix the midpoint, not the bottom (proved; checked).**
- An affine self-map E → 2s − E of a bounded spectrum fixes only s = (E₀ + E_max)/2. Such a symmetry selects E₀ only if the spectrum is a point.
- The bipartite KS lattice's chiral symmetry ({M, Γ} = 0, checked 0) selects the trace zero.
- The half-filled sea sits **1.1938 per site below it** at m → 0 (1.3000 at m = 1; `r173_recordmap_vacuum.out:17-20`). That is **−1.05e123 ρ_Λ** at a = ℓ_P (`r173_recordmap_vacuum.out:27`).
- The mirror construction (O3 #10) puts the vacuum *at* the midpoint by doubling with negative energies. Its price is ghost-like instability (counted once).

**(c3) Symmetries that fix the bottom: supercharge positivity, and exact dilatations (comparator; prior art).**
- If H = {Q, Q†} with Q unbroken, then E₀ = 0 exactly and stays so under loops. In Theorem T this is the excluded case "V_late constant on Θ" (H-an fails), and C = 0 still has to be gravity's zero. In supergravity, SUSY vacua have Λ ≤ 0 (RECALLED).
- **Status for our vacuum.**
  - Exact supercharge algebras are forbidden in R13-1's class (`TESTS:4717`).
  - O3 #3's exact Q-doublets are not observationally excluded as stated (`vO3:13`).
  - But an unbroken Q needs a degenerate charged partner of the electron. Comparator, RECALLED: that would shift the running of α and g − 2 at O(α/π), so it is excluded.
  - Broken SUSY leaves ≥ Δ⁴, i.e. (N) again (O3 #4).
- Exact dilatations would also fix the bottom, but Z³ with fixed adjacency has no continuous scale symmetry (`AX:37`; reading), and masses break it.

**(c4) Answer to probe (c).** The shift makes ρ_v's absolute value unobservable and leaves C a free datum. No creation-law extension selects it. TUNING for (iii), as expected.

### 4.4 (d) Radiative stability

| Structure | Number needed | Radiatively stable? | Causal (g ≡ 0, k ≠ 0 sector) | Inflation |
|---|---|---|---|---|
| **(N)** C = law constant | 1, exact | **No.** One-loop vacuum terms n m⁴/(64π²): electron 1.7e31, muon 3.1e40, b 2.3e47, W/Z/h ≈ 1.5e52, top 6.7e53 ρ_Λ. A fractional mass change of 1.5e-32 (e) to 3.7e-55 (t) shifts Λ̃ by ρ_Λ (checked arithmetic, RECALLED inputs, `r173_symmetry_radiative.out:18-26`). EW tree step 4.7e54 (counted once) | yes (GR) | yes |
| **(S)** C = E₀[H] (P92) | 0 | **Yes under continuous changes of θ**: E₀[H] is recomputed from the full law, so every loop and threshold is matched (proved, definitional). This sharpens vR16-6:26's "nor makes it radiatively stable" for (S) as defined. **No** when the ordering of minima flips: in a tilted double well with the universe in the + well, Λ̃_late jumps 0 → 2εv as ε crosses 0 (checked, `r173_symmetry_radiative.out:27-32`). With the SM alone (metastable, RECALLED), Λ̃_late = V_EW − E₀ > 0 and enormous, so P93 needs stabilizing physics (counted once) | yes (GR with Λ_bare = −κE₀; Lemma S ultralocal at g = 0, `C5_R15-1_report.md:137`) | yes (65.2, REC-S) |
| **(A)** C = lim ρ_tot, or a whole-history average | 0 | yes (tracks any final vacuum) | locally GR; the constant is set by the future (b1); consistency can fail (b2) | yes |
| (i-lit) record weights | — | no (realized map: m²M_P² thresholds) | no (g ≠ 0) | only via g ≠ 0 (unrecorded plateau) or without reheating (recorded): dilemma |
| (ii) causal running average | — | — | no (g ≠ 0) | no (1.3 e-folds) |

**A remark on the grid zero-point.** (S) subtracts the full ground-state stress. Bianchi conservation of the subtracted term needs it to be ∝ g_μν, i.e. ρ₀ + p₀ = 0. Under R11-3's w ≥ 0 tadpole that is one further condition: pairing or one enthalpy tuning (`vR15-1:15`, P70, counted once).

### 4.5 What would work, and where it sits

- **Inside 𝒦, only (S) satisfies every ENFORCED clause except "forced".** It is GR with Λ_bare := −κE₀[H].
  - It is local and causal in its dynamics (this is generic GR behaviour);
  - it needs no number;
  - it is stable under every continuous change of the law;
  - it lets every false vacuum and the inflaton plateau gravitate.
  - It needs P93 and P94, and a source-bridge principle that the axioms do not contain.
  - Lemma U shows it is the unique number-free option once "weights are never negative" is added.
- **(iv) Relaxation, outside 𝒦: a necessary condition (proved from Lemma PT's corollary, counted once).**
  - In GR, Λ̃_late − Λ̃(t_r) = −κΣ_{t_i > t_r} ΔV_i. So a relaxation that ends at t_r must come after the last vacuum change larger than ρ_Λ: the QCD step, 1e43–1e44 ρ_Λ at T ~ 150 MeV.
  - A trigger that sees only H² separates Λ from radiation at that time only to about ρ_Λ/ρ_tot ~ 1e-44 (suggested). This is the empty-universe problem (comparator: Brown–Teitelboim, Bousso–Polchinski, `vR10-4:15`).
  - Within the axioms, the candidate carrier would be Admissibility weights for the final vacuum pick that vary with the local expansion (`AX:60-61`). This is not built or tested here.
  - The owner's "rise until frozen" points the wrong way: it stops at saturation, not at zero (`vR5-3:25`; `C5_R10-4_report.md:304`).
- **A primordial record of C** (the "law-supplied endpoint record" escape, `vR16-6:54`). Permanence makes a record the natural carrier of a constant of motion. Its value is written by the formation law ((S)) or drawn as an initial datum ((N)). Reading.

---

## 5. Prices (named, none adopted)

| # | Price | Axiom text touched | Status |
|---|---|---|---|
| **P-r173a = P92, restated** | **"The lowest state of the law weighs nothing"**: the source bridge is T − E₀[H]g (S). By Lemma U it is equivalent to shift covariance + nonnegative weights + one weightless state. Needs P93 (our vacuum is the global minimum) and P94 (no branching among unequal late vacua). With the grid zero-point it also needs P70 | Source/action `AX:187`; the axioms supply no H or E₀ (`AX:116-130`). On `AX:94` ("a law privileges no states"), reading: E₀ is distinguished by supplied structure, as at `AX:52` | proved sufficient (R16-6 Thm Z); unique number-free form (Lemma U, proved); **stipulated, not enforced** (§4.1–4.3). Classed as the counterterm by vR16-6:18-26 |
| **P-r173b** | **Final-state datum** C = V_late (= R5-3 Λ6, counted once), **plus a consistency-selection rule** for windows with no or several self-consistent histories (b2, new) | `AX:94` (tension, `R53:132`); arrow and time metric open (`AX:185-186`) | proved acausal (b1); inconsistency checked in a toy (b2) |
| **P-r173c** | **Record sourcing re-adds I, additivity and I(∅) = 0** (removed 2026-08-13). In literal form it also excludes inflation + reheating at g ≡ 0 (dilemma) and any radiation era (Lemma M) | `AX:148-151,220-223`; `AX:79-83` (permanence, content readout) | **No-go in (i-lit), for the referee.** Not payable as stated |
| P-r173d | **Matter-side relaxation (iv)**: an H-sensitive selection of the final vacuum that finishes after the QCD step | `AX:60-61` (distribution varies with neighbourhood conditions) if carried by Admissibility; record-production dynamics open (`AX:185`) | outside 𝒦; necessary condition proved; not built |
| P93, P94, P70, P51 (carried) | As S20 (`S20:387-388`) | — | carried |

**Counting convention (rule `TESTS:5700`).** (N) is one cosmological counterterm for the whole law, not one per species. It must be re-fixed after every change of any matter parameter (§4.4). (S) uses zero numbers. (A) uses one final-state datum.

---

## 6. Round-17 rules

- **Whole-zone v_max:** the KS symbol only. v_max/c = 1 (proved, §4.1 a4). No other lattice symbol is used, and no gauge-field symbol.
- **Self-force:** none. No frame-tied kernel is used; (S), (N) and (A) are GR locally.
- **Ward:** standard (diffeomorphism / Bianchi).
- **Counting conventions:** §5.
- **Enforced or stipulated:**
  - (N) is stipulated, a number;
  - (S) is stipulated, a rule;
  - (A) is stipulated, a boundary datum;
  - supercharge positivity would be enforced, but its premise is excluded for our vacuum;
  - radiative stability is checked in §4.4.
- **Physical controls:**
  - REC-S / G0 is GR with Λ_bare = −V_late, which is known to inflate with Λ̃_late = 0;
  - B2's outside-window rows give exactly one history;
  - the record-map values are a reproduction, not a physical control.
- **Readout bridges:** the record-map energy uses W1 pinching (`RM:25-27`). No stiffness claim is made.
- **Forks:** §2, items (iv)–(ix).
- **Generic GR comparison:**
  - (b1) is generic to any final-boundary-condition law in GR;
  - (S), (N) and (A) are generic GR with a constant;
  - the dilemma and Lemma M are specific to record sourcing;
  - (b3)/(b4) are specific to R14-5-type readers.
- **Changed hypotheses:** §0.

---

## 7. Notes for the referee (FAIL / no-go items)

1. **Theorem T.**
   - Is H-blind + H-an the right class, and does it contain (i)–(iii) as stated?
   - **The decisive ruling:** does (S), a number-free stipulated rule, count as "an independent exact number" under `TESTS:5810`, as vR16-6:18-26 suggests? If it does, the reading is TUNING. If it does not, it is OPEN with Theorem T.
2. **Lemma U.** Correctness, and whether "shift covariance from global-phase invisibility" is a fair reading of `AX:82-83`.
3. **The (i-lit) dilemma and Lemma M.**
   - Are permanence and content-only readout (`AX:79-83`) correctly applied to a gravitating source?
   - Is REC-mass a fair count-type model? It is a running maximum of comoving energy.
   - REC-vac's e-folds (7.17 at φ₀ = 16; 62.1 at φ₀ = 150) come from R growing as kinetic energy is pumped by the unrecorded potential (g ≠ 0), not from slow roll. Is the correction to `R166:147` right?
4. **The record-map vacuum.** c₀ = 0.4553 and the m² threshold law. Is the scale bridge a = ℓ_P used only for sizes?
5. **(b2).** The trigger reads H, which depends on C, so the toy is outside H-blind (type iv). Does it establish non-existence and non-uniqueness for final-state rules once the vacuum pick is gravity-sensitive?
6. **(c1)–(c3).** Invariance, the midpoint lemma, and the RECALLED supercharge status.
7. **Strong-word check.**
   - "Exactly one of": partition by construction.
   - "Cannot": in (i-lit), under its three stated hypotheses.
   - "Unique" (Lemma U): among shift-covariant references with the two stated conditions.
   - "Every loop": continuous changes of θ only.
   - "Nothing in the four axioms": textual, `AX:116-130,148-151,173-190`.

**What would change the picture.**
- A symmetry or constraint that makes ρ_v,late(θ) constant on Θ with gravity's zero equal to it (supercharge-type positivity in our vacuum).
- A built relaxation (iv) that ends after QCD without an empty universe.
- A ruling that (S) is a principle, not a tuning (owner Q1(b)).
- An inhomogeneous construction with the local constraint (`R166:229-235`).

## 8. Files

- Report: `S/R17-3_report.md`.
- Scripts and outputs (each `.py` with its `.out`) in `S/scripts/`: `r173_records_inflation`, `r173_recordmap_vacuum`, `r173_global_constraint`, `r173_avg4_inflation`, `r173_symmetry_radiative`, `r173_recvac_scan`.
