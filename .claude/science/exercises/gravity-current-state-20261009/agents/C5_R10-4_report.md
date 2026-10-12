# C5 R10-4: Λ's mean in set A with records as a conserved q-charge and free volume (q-theory)

**Worker.** Claude Opus 5.5, the same model family as the supervisor and the R4-5 and R5-3 workers. Not refereed. Run 2026-10-12, 18:00Z to 18:23Z. No repository file was edited.

**Scratch.** `scratchpad/C5/R10-4/`. Scripts and their outputs are in `scripts/`:
- `r104_variation.py/.out`: the metric variation at fixed record count (FRW and a generic metric); the count's field equation; phase transitions at fixed μ; the conserved-current (3-form) variant.
- `r104_minkowski.py/.out`: the Minkowski condition with q-dependent gravity couplings Ω(q)R + β(q)R².
- `r104_numbers.py/.out`: the sizes of μ tuning, record-q noise, the Klinkhamer–Volovik electroweak remnant, Brown–Teitelboim steps, and the trace thermostat.
- `r104_thermostat.py/.out`: an FRW toy of a dissipative trace thermostat, plus its analytic fast limit.

**Read.**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md` "Campaign C5" method (2302–2320); R4-5, R5-3 and R6-3 pre-registrations and results (2847–2858, 2886–2898, 2938–2945, 2985–2993, 3106–3130, 3420–3428); R10-4 (4000–4012).
- Agents: `C5_R5-3_report.md`, `C5_R5-3_referee.md`, `C5_R5-3_referee_verdict.md` (all in full); `C5_R4-5_report.md` §§0–3 and its verdict; `C5_R6-3_referee_verdict.md`; `C5_R6-4_referee_verdict.md`; `C5_O5_synthesis.md` §2.1 (set A); `C5_S8_synthesis.md` (Λ lines).
- Prior art: `docs/COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md`, `UNIVERSAL_GR_INDUCED_COSMOLOGICAL_CONSTANT_BOUNDED_THEOREM_NOTE_2026-06-08.md`, `COSMOLOGICAL_CONSTANT_VACUUM_ENERGY_AUDIT_NOTE.md` (all in full); record-map note T4 (`THE_RECORD_MAP_…_2026-09-04.md`, §T4).
- Grep of `docs/` for q-theory, Klinkhamer, Volovik, four-form, 4-form, 3-form and three-form. Every docs hit is the mathematical sense (Chern character, F∧F, strong-CP form degree, Koide) or Klinkhamer–Schreck/Klinkhamer–Manton. **No repository note treats q-theory or a four-form vacuum compensator.**
- Packet hits: `OUTSIDE_VIEW.md:44` (q-theory cancels the tadpole only, never a modulus); `B1_report.md:111`; `supervisor_thread.md:31`; R5-3 route 4.
- The owner's thought (`memory/records-count-rises-until-frozen.md`), as a hypothesis only.

**Labels.**
- **proved:** a complete argument under the stated hypotheses.
- **checked:** symbolic or numerical, in the scripts.
- **suggested:** argued, not proved.
- **reading:** interpretation.
- **comparator:** outside literature. "Verified" means fetched this run; "from memory" means not checked.

---

## 0. Verdict against the FIXED readings (`TESTS.md:4009-4012`): **OPEN**

**Not EXCLUDED.**
- The reading's own example of an exclusion, "records cannot be a conserved q-charge under the Record axiom", is **false in set A** (§2, proved).
- Permanent records make the accumulated record count a 3-form potential A, whose exterior derivative F = dA is the formation-event density.
- Varying the metric at fixed records gives the Gibbs–Duhem vacuum stress ρ_V = ε − qε′ exactly (checked).
- No stated bound is violated by the minimal version: a four-form with constant G, μ chosen, w = −1.

**Not VIABLE.**
- No record q-model found here gives ⟨Λ⟩ = 0 across phase transitions without tuning.
- **Lemma PT-q (§3, proved; checked).** Take any local action in which the count enters only through F = dA, with any q-dependent gravity couplings. Then the chemical potential μ is a conserved Noether charge.
  - Minkowski space exists only for μ = μ₀[final ε].
  - A transition that shifts the vacuum energy by Δ after the data are set moves μ₀ by Δ/q₀, while μ stays put.
  - So zero after the electroweak (EW) transition needs μ pre-set to 1 part in 4.7×10⁵⁴, or μ fixed by the final vacuum. The final-vacuum choice is R5-3's price Λ6.
  - Klinkhamer–Volovik's own electroweak paper assumes μ = μ₀ (comparator, verified), and KSV state that the Minkowski asymptote needs fine-tuned initial conditions (comparator, verified).
- The escapes from Lemma PT-q each fail or move the problem elsewhere (§4):
  - membrane steps (Brown–Teitelboim);
  - a dissipative thermostat;
  - count-dependent laws;
  - a fixed global count.

**So OPEN**, with these bounded sub-results. Each is FAIL-type, so each needs the codex referee before it is recorded.
- **(B1)** Conserved record-number currents (3-form) and conserved comoving counts are not compensators in expanding FRW (proved).
- **(B2)** Lemma PT-q, in the local shift-symmetric class (proved).
- **(B3)** On fixed sites (sets B and C), one record per site plus permanence forbids a steady q₀ > 0 (proved).
- **(B4)** A trace thermostat leaves a negative vacuum energy that tracks dust. In its fast limit dust redshifts as a⁻⁴ (proved for the stated model; checked).
- **(B5)** Single-flux record membranes (Brown–Teitelboim): meV-scale steps and tension. At zero temperature there is an EW dilemma (suggested; comparator problems verified).
- **(B6)** Poisson-distributed record q gives white-noise potential fluctuations δΦ ≈ Gχ⁻¹/√q₀. That is 1.6×10⁻³ at Planck compressibility and Planck density (suggested; Newtonian heuristic).

---

## 1. In plain words

**What q-theory does.** Klinkhamer and Volovik treat the vacuum like a drop of liquid. A drop floating in empty space settles where its pressure is zero. If gravity sees only that pressure, the vacuum's weight is zero, whatever the zero-point energies are. Two ingredients make this work: a "charge" that is counted, not measured in volume, and a volume that is free to adjust.

**Records can be that charge.** Records never disappear. So the number of records accumulated in a patch is a running total, and the rate at which new ones appear per unit spacetime volume is exactly the field strength of q-theory.
- If the geometry is varied while the records are held fixed, which is natural since records are fixed reality, the right Gibbs–Duhem combination appears by itself.
- R5-3 said this coupling had to be added as a separate rule. With records as the charge it comes out of the variation; only an energy function ε(q) is new.

**But the zero is not automatic.** In any local law of this kind, a "chemical potential" μ is conserved, like a total charge.
- The vacuum ends weightless only if μ has one special value, and that value depends on every vacuum-energy drop still to come: the Higgs, QCD, and so on.
- So μ must be set at the start to 55 digits, or set by the final state, which assumes the answer.
- This is the old cosmological-constant problem again, now living in μ instead of in Λ.

**The owner's "count rises until frozen."**
- q-theory needs records to keep forming at a steady rate in empty space. That fits "count rises".
- A frozen region (no new records) loses the compensation and is left with an uncancelled vacuum energy. That conflicts with "until frozen" as the route to zero weight.

**Ways around it.** Each one fails or moves the problem:
- **Stepwise drops in the formation rate** (membranes). These need steps and wall tensions at the meV scale of Λ itself, and they hit the "empty universe" problem.
- **A thermostat that pushes the total trace to zero.** It leaves a negative vacuum energy that follows the matter. In its fast form, matter thins out like radiation.
- **A rule tied to the total count of all history.** This is non-local in time, and it needs a sealed, finite universe.

**One positive lead.**
- Klinkhamer–Volovik's electroweak "kick": if μ is right, the leftover vacuum energy is about E_ew⁸/E_P⁴. That matches today's value for an effective electroweak scale of about 2.3 TeV (comparator; arithmetic checked).
- Separately, the q-records give Sorkin's count–Λ conjugacy for free: the record count A and μ are a canonical pair (§5.3).

---

## 2. Records as a q-charge: the identification

### 2.1 Three candidates named in the item (`TESTS.md:4005`)

**(a) Conserved record-number current (a 3-form J = n u, dJ = 0).** **Bounded EXCLUDED as a vacuum compensator (proved; checked `r104_variation.out:27-31`).**
- A conserved current is a fluid: ρ = ε(n), p = nε′ − ε, so ρ + p = nε′(n).
- A Lorentz-invariant vacuum (T ∝ g) needs nε′ = 0. Then ρ_vac = Λ_b + f(n_*) at a stationary point, or Λ_b + f(0). This is R5-3's case (a); no zero condition follows.
- In expanding FRW, n ∝ a⁻³ → 0, so ρ → Λ_b + f(0), a free constant.
- This matches KV's remark that a global charge "must be zero in the Lorentz-invariant vacuum" (comparator, verified, 0711.3170 §V). There it is made for B−L, not for a liquid.

**(c) Record count per comoving volume.** Under permanence plus formation, ∂_μJ^μ = Γ ≥ 0.
- It is conserved only when formation stops (Γ = 0), and then it is case (a), which fails.
- While formation continues, the comoving count is the potential A of (b) below, not a conserved charge (proved).

**(b) The 4-form record density.** **This one works formally.**

### 2.2 The 4-form identification (proved; checked)

**Setting.** Set A sites are the points of Minkowski space (`C5_O5_synthesis.md:324`). Records are formation events, and a record once formed is permanent (`MINIMAL_AXIOMS_2026-06-29.md:79-80`).

**Definitions.**
- **Γ:** the formation 4-form, i.e. events per 4-cell. Then q = ∗Γ is the number of formation events per proper 4-volume, a Lorentz scalar.
- **J:** the 3-form current of persisting records.

**Identity (proved).** Permanence gives dJ = Γ. So, for any 4-region R:

N_formed(R) = ∫_R Γ = ∮_∂R J.

So **A ≡ J is a 3-form potential and F ≡ Γ = dA**, which is q-theory's field strength (`F = q√−g ε`).
- Permanence (no erasure) ⇔ A is non-decreasing along the time orientation ⇔ q ≥ 0.
- "Count rises" ⇔ q > 0. "Frozen" ⇔ q = 0.

**Gibbs–Duhem from fixed records (proved; checked).** Take a vacuum action −∫√−g ε(q) and vary the metric at fixed records. The count per coordinate cell c = q√−g does not depend on the metric, so δq = −½ q g^{μν} δg_{μν}. This gives:

T^{(q)}_{μν} = −(ε − qε′) g_{μν}

- FRW minisuperspace: ρ = ε − qε′, p = −ρ (`r104_variation.out:1-5`).
- Generic 4×4 metric, by Jacobi's formula: the residual is 5.9×10⁻¹⁰ on a scale of 1.6. If q were metric-independent instead, the residual would be O(1) (`:10-12`).
- **Consequence.** R5-3's "coupling gravity to ε − μn needs an extra q-type source rule" (`TESTS.md:2992`; `C5_R5-3_referee.md:70`) reduces to one sharper price, Q1 in §6: an energy function ε(q) of the record density in the gravitational action, varied at fixed records. The ε − μq form is then derived, not postulated.

**Field equation for the count (proved; checked `r104_variation.out:7-8`).** If the accumulated count A is a dynamical variable that enters only through F, then ∂L/∂Ȧ = −ε′(q) is conserved, so **ε′(q) = μ is constant** (KV 0711.3170 Eqs. 53–54, "plays the role of a chemical potential"; comparator, verified).
- In records language this is a formation-rate law: the formation density is such that ε′(q) is uniform in spacetime.
- For constant μ, q is uniform: records form at a constant rate per proper 4-volume.

**Reading: the free volume.** Set A's metric is a supplied dynamical field (A5, `C5_O5_synthesis.md`). The "free volume" is realised by varying the metric at fixed counts. In sets B and C the spacing is fixed, so this term has no analogue (consistent with R5-3 §4, row "route 4").

### 2.3 Against the Record axiom

- **Permanence:** used, and gives q ≥ 0.
- **One record per site:**
  - In set A the sites are continuum points, so the clause imposes no cap on a density.
  - **(B3), proved.** On fixed sites (B: Z⁴ events; C: Z³ with permanent one-per-site records), A ≤ the number of sites per comoving cell. A steady q₀ > 0 then lasts at most n_site/q₀. At KV's Planckian q₀ (about 1.6×10⁻³ per Planck 4-volume, §6 Q3) and one site per Planck 3-volume, that is about 600 Planck times on Z³ (R4-5's Lemma C-count, `TESTS.md:2941`). A frozen q = 0 leaves ρ_V uncompensated (§3).
- **"Only records are readable":** A, the count, is readable (`MINIMAL_AXIOMS_2026-06-29.md:82`), so A is not a gauge field. Nothing in q-theory needs A to be unobservable, as long as the law depends on A only through dA (§4.4 is the exception).
- **Formation rate:**
  - Admissibility "does not supply the formation site, probability, or rate" (`:67-69`).
  - The rate is downstream supplier content (`:183-184`), and "Admissibility is not a dynamics axiom" (`:116-123`).
  - So the law ε′(q) = μ is a new downstream formation-rate law: price Q2.
- **Vacuum records:** q₀ > 0 in Minkowski space means records form in empty space at a uniform 4-density.
  - That is not A4's "rare, coarse, matter-following" flash layer (`C5_O5_synthesis.md:327`).
  - It is R4-5's A+ variant: inert records that lock nothing which decoheres matter or steers light (R4-5 §3; RL4/RZ lensing).
  - This is price Q3.

---

## 3. Lemma PT-q: phase transitions with a conserved μ (proved; checked)

**Hypotheses.**
- **H-q1.** Local diffeomorphism-invariant action L(g, A, matter). The count A enters only through F = dA (shift symmetry A → A + closed form). Arbitrary q-dependent gravity couplings Ω(q)R + β(q)R² are allowed (higher-curvature terms behave the same way at flat space).
- **H-q2.** The late-time state of interest is Minkowski (R_{μνρσ} = 0), with q constant.
- **H-q3.** A phase transition is a change of the matter vacuum energy, Λ_b → Λ_b + Δ, after the initial data are set.

**Statement.**
- **(i) μ is conserved.** By Noether's theorem for the shift symmetry, μ ≡ −∂L/∂Ȧ is conserved.
- **(ii) Minkowski condition.** A static flat solution exists iff ε(q₀) − q₀ε′(q₀) + Λ_b = 0 and μ = ε′(q₀). Ω and β drop out (`r104_minkowski.out:1-5`).
- **(iii) Sensitivity.** Along that family, dμ₀/dΛ_b = 1/q₀ (`r104_variation.out:20`). Equivalently, along ε′(q) = μ, dρ_V/dμ = −q (`:17`).
- **(iv) No compensation at fixed μ.**
  - At fixed μ, a q-independent shift Δ leaves q unchanged and shifts ρ_V by exactly Δ (`:18`).
  - A q-dependent kick changes ρ_V by P_old(μ) − P_new(μ), with no zero condition (`:24`).
  - Only a term exactly linear in q drops out of ρ_V (`:25`), and §4.5 shows that route conflicts with matter dynamics.

**Corollary (proved; arithmetic checked).** A late-time zero needs μ to anticipate every later transition. Relative to the EW shift that is a precision of ρ_Λ/ΔV_EW = 2.1×10⁻⁵⁵ (`r104_numbers.out:9`), the same number as R5-3's Lemma PT (`TESTS.md:2986`).
- The constant Planck tadpole (1.4×10¹²⁰ ρ_Λ, `r104_numbers.out:5`) is absorbed into the choice of μ. Only the *changes* bite.
- The alternative is to fix μ by the final vacuum, which is R5-3's 1b and price Λ6.
- **So the four-form route, in its local conserved-μ form, is unimodular gravity with μ in place of Λ_c (reading).** This matches the known equivalence: Henneaux–Teitelboim, Λ as a 3-form integration constant (comparator, from memory).

**Comparators (verified this run).**
- **KV 0711.3170** derives the readjustment of q₀ after a transition (their Eq. 14) from the zero-pressure condition P = 0 (Eqs. 7, 10), not from the dynamics. That static argument assumes μ is free to re-equilibrate.
- **KV 0905.1919** sets μ = μ₀ by assumption: "our assumption is that the Minkowski-spacetime vacuum is a self-sustained system". Zero external pressure then fixes μ₀.
- **KSV 1601.04676:** with reversible dynamics, Minkowski is approached only if the Big Bang began in equilibrium. With dissipation, the outcomes are de Sitter or collapse, and "the decay of the de-Sitter vacuum is a necessary condition".

**What Lemma PT-q adds to R5-3.** Lemma PT covered prescribed c-number subtractions within G1–G3. The referee left four-form fluxes and dynamical compensators outside (`TESTS.md:2987`; `C5_R5-3_referee.md:20`). Lemma PT-q closes the local shift-symmetric four-form part of that gap, for any q-dependent gravity couplings, at the Minkowski endpoint.
- **Not covered:** μ-changing sources (membranes, §4.1), dissipative laws (§4.2), A-dependent laws (§4.4), global constraints (§4.3), and non-Minkowski asymptotes (de Sitter with small H as a function of μ − μ₀ is suggested, not computed with G(q)).

---

## 4. The escape routes, tried in turn

### 4.1 Membrane steps (Brown–Teitelboim): "freezing fronts" that lower the formation rate

**Mechanism (comparator).** Membranes charged under A change F, and so μ, in jumps. Nucleation lowers the vacuum energy step by step, and relaxation stops within one step of zero.
- **Records reading.** A membrane is a 2+1D front across which the formation density drops. Repeated fronts read naturally as "count rises, ever more slowly". As a lattice-free mechanism it is untuned with respect to the initial data.

**Single flux (suggested, numbers checked; problems verified in BP hep-th/0004134 §§2.3, 3.1, 3.2.1).**
- **The step must be ≲ ρ_Λ.** The flat-space thin-wall bounce B = 27π²σ⁴/(2δ³) ≤ 10²–10³ then needs membrane tension σ ≲ (2.2–2.7 meV)³ (`r104_numbers.out:35-36`).
  - That is the Λ scale reappearing as a new small input: BP's charges "enormously small compared to the ordinary scales of microphysics" (comparator, verified).
- **Empty universe.** The final steps release ≲ ρ_Λ, so reheating after the last step reaches T ≈ 2 meV (`:39`), against the T ≳ 1 MeV that BBN needs (comparator BP §3.2.1, verified: "lead to an empty universe").
- **EW dilemma at zero temperature (suggested).** CDL nucleation from Minkowski or AdS only goes down. Two cases:
  - If relaxation completes before EW, the transition leaves ρ_V = −ΔV_EW. Radiation falls below |ρ_V| at T ≈ 43 GeV, and the AdS time scale is 2.6×10⁻¹⁰ s, so the universe crunches long before BBN (`:38`).
  - If relaxation happens after the last transition, the empty-universe problem applies.
  - With a meV tension, membranes would be thermally active in the hot plasma. That regime is **not analysed** here.
- **Many fluxes (Bousso–Polchinski).** About 100 incommensurate fluxes give a discretuum, with inflation after landing (comparator, verified).
  - **Records reading:** record "types" over the continuous M₂(C) possibility domain could supply many fluxes.
  - The price is anthropic selection, which is not "without tuning" in the fixed reading's sense. OPEN.

### 4.2 A dissipative thermostat on the formation law

**Idea.** The formation rate drifts μ in response to the vacuum's weight, dμ/dt ∝ ρ_V. This is local and untuned at its fixed point, and it lies outside Lemma PT (state-dependent, with energy exchange).

**The record sector cannot see the matter vacuum energy except through gravity** (reading). In a matter-filled region the vacuum/matter split of T is not unique. The only invariant local signal is curvature, i.e. the trace T^μ_μ, which is what KV's G(q) coupling responds to.

**Lemma Tr (proved for the stated model; checked).** Let the thermostat relax the total trace to zero: dρ_V/dt = −Γ(ρ_V − y), with y = −(ρ_m − 3p_m)/4 (`r104_numbers.out:42`).
- **(i)** The fixed point is y ≤ 0 for ordinary matter. For dust today it is −0.115 ρ_Λ (`:43`): the wrong sign.
- **(ii)** As y rises toward 0, the lag keeps ρ_V < y. With z = ρ_V − y, ż = −Γz − ẏ, and ẏ > 0. FRW toy: ρ_V/ρ_dust settles at −0.26 (c = 100) to −0.36 (c = 10) wherever the integration runs (`r104_thermostat.out`).
- **(iii) Fast limit.** Total conservation with ρ_V = −ρ_m/4 forces **ρ_m ∝ a⁻⁴**: dust redshifts like radiation, with no matter era (sympy dsolve, `r104_thermostat.out`, last lines). That is excluded by the CMB and structure growth (comparator, from memory).
- **(iv) Slow limit.** For c ≤ 1 a positive initial ρ_V is not removed.
- **(v) Local action (suggested).** The same thermostat acting locally gives the vacuum stress p_V = +ρ_m/4 inside matter. Inside rock that is |ρ_V| ≈ 2.4×10²⁹ ρ_Λ (`:44`). Its gradient force on matter is about 10⁸ times Earth's gravity at the surface, unless the vacuum sector itself is out of balance.
- This is the local relative of Kaloper–Padilla's global residual Λ_eff = ¼⟨τ⟩ < 0 for dust (R5-3 §3.3, comparator verified there). The global version is bounded by Lemma S (`TESTS.md:2989`).
- **Disposition.** A trace thermostat is no route to ⟨Λ⟩ = 0 with the observed positive Λ. The case in (iii) is bounded EXCLUDED; the rest is suggested. A thermostat that senses only the "vacuum part" needs a local vacuum/matter decomposition, which is not defined (reading). **OPEN.**

### 4.3 A fixed total count (the whole history; "sealed universe")

- Suppose the total record count N_tot is fixed and the total 4-volume V₄ is free. Then q = N_tot/V₄, and the metric variation gives Λ_eff = 8πG[Λ_b + ε(q) − qε′(q)] with q set by the whole history (proved: the same variation as §2.2 with a global q).
- This is a global, sequestering-type law: price Λ8 (R5-3 §5).
  - It needs finite V₄. A future de Sitter phase has V₄ = ∞, so q → 0 and the compensation is lost.
  - It contradicts the owner's "there is no sealed box" as stated (reading).
- Whether a self-consistent history with Λ_eff ≈ 0 exists is not computed. The original global KP constraint is bounded by Lemma S (`TESTS.md:2989`). **OPEN.**

### 4.4 Count-dependent laws (the owner's "until frozen" as a law on A)

- If the law depends on the readable count A itself, through the proper accumulated density s = A/a³, the shift symmetry breaks. With N = 1, μ̇ = ∂ε/∂s (derivation as §2.2; suggested — not in the scripts).
- At late times s grows without bound (ṡ = q − 3Hs, and in Minkowski space ṡ = q₀ > 0). So the drift must die off: ε_s → 0. The endpoint μ_∞ = μ_i + ∫ε_s dt is set by the history, and ρ_V(μ_∞) is generically nonzero (suggested).
- A zero needs ε_s to vanish exactly where ρ_V does: two conditions on one endpoint, i.e. a coincidence or tuning, unless the drift senses ρ_V. Sensing ρ_V is §4.2.
- In cosmology, s is a cosmic clock: a preferred frame through the record history (reading). **OPEN, leaning no.**

### 4.5 Vacuum energy "per record" (a term linear in q)

**Algebra (checked `r104_variation.out:25`).** A matter vacuum energy proportional to q, ε ⊃ V(φ)q/q*, drops out of ρ_V identically. It survives any change in V. It is metric-independent: ∫√−g q V = ∫c·V.

**Inconsistency (proved).** Take a kinetic stress for φ.
- **If A is varied:** ∂(V/q*) = 0 forces V(φ) constant. A rolling or transitioning φ is then impossible.
- **If records are held fixed:** ∇^μT^{kin}_{μν} = (q/q*)∂_νV ≠ 0, which breaks Bianchi in GR. In unimodular gravity the shift reappears in Λ(x), by Lemma PT.
- Either way the transition is not protected. This also means the inflaton's potential would not gravitate (reading). **EXCLUDED within G1–G3 plus this form** (bounded; needs referee).

### 4.6 Stochastic records as q (records form at random)

**The noise.** If q is a random point-process density rather than a field obeying ε′ = μ, then ρ_V fluctuates. In a region of 4-size ℓ, δρ_V ≈ χ⁻¹/√(q₀ℓ⁴), with χ⁻¹ = q²ε″, the vacuum's inverse compressibility.
- The Newtonian potential noise δΦ ≈ Gδρ_Vℓ² = Gχ⁻¹/√q₀ **does not depend on ℓ**: white noise at every scale down to the record spacing (`r104_numbers.out:12`; suggested, Newtonian and instantaneous; the retarded IR cut adds a √4π).

**Numbers (checked arithmetic).**
- At KV's Planck compressibility and one record per Planck 4-volume, δΦ ≈ 1.6×10⁻³ (`:16`).
- Clocks at 10⁻¹⁸ would need 2.5×10³⁰ records per Planck 4-volume (`:15`).
- Compensating only EW, with Δln q ≈ 1, needs q₀ ≳ 1.3×10⁴⁷ m⁻³ s⁻¹ (spacing 2×10⁻¹⁰ m) for δΦ ≤ 10⁻¹⁸ (`:19`).
- Matter-following flash densities give δΦ ≈ 2×10¹⁰ (`:25`): impossible.

**Bianchi.** A locally fluctuating ρ_V is not conserved, so it needs an exchange current. This is R4-5's Bianchi-completion problem (`TESTS.md:2944`).

**What survives.** Only formation whose count fluctuations are strongly suppressed: deterministic, or hyperuniform in 4D. R6-3's V′ (`TESTS.md:3426`) gives the Lorentz-invariant-in-law route to sub-volume variance, a reciprocal gap that excludes the null cone, and strict lensing silence is open (`:3427`). This is suggested; Q2 must be a law, not a coin toss per site.

---

## 5. What sets today's small Λ, and the observational checks

### 5.1 Residual from non-equilibrium formation (KV electroweak kick; comparator, verified)

- With μ = μ₀ assumed, the EW crossover kicks the vacuum. The remnant is ρ_V ≈ E_ew⁸/E_P⁴, equivalently ∝ κ_M²H⁴ at the crossover, with w_V = −1 afterwards.
- Arithmetic (checked, reduced E_P = 2.44×10¹⁸ GeV): E_ew = 1 TeV gives 1.1×10⁻³ ρ_Λ = (0.41 meV)⁴, and E_ew = 2 TeV gives 0.29 ρ_Λ (`r104_numbers.out:28-31`). ρ_Λ itself needs E_ew ≈ 2.3 TeV.
- The prefactor is not fixed, and the result scales as E⁸, so a factor 2 in the scale is a factor 256.
- **Records reading:** the remnant is the lag of the formation rate behind the expansion during a crossover.
- **Status: conditional on μ = μ₀**, which is the tuning of §3. It explains the *size* of the remnant, not the zero.

### 5.2 Observations, per variant

| Variant | w(z) | DESI DR2 (verified abstract: w₀ > −1, w_a < 0 preferred at 2.8–4.2σ by SN choice; 3.1σ BAO+CMB) | BBN | CMB | Status |
|---|---|---|---|---|---|
| Four-form, constant G, μ chosen (§3) | −1 exactly | In tension at that level, not excluded (< 5σ, SN-dependent) | No new propagating degree of freedom (a 4-form has none in 4D; comparator, from memory) | ΛCDM | Allowed; tuned |
| KV with G(q) (0806.2805, verified summary) | Planck-frequency oscillations decaying; average ~ near-critical, "could make up … CDM" | Not computed | G(q) must sit at its equilibrium by BBN; \|ΔG/G\| ≲ 0.1 (from memory) | Not computed | Tuned μ |
| KV EW remnant (§5.1) | −1 | As row 1 | As row 1 | As row 1 | Conditional |
| BT single-flux records (§4.1) | Piecewise −1 | — | **Fails (empty universe; T ≈ 2 meV)** | — | Bounded EXCLUDED (suggested) |
| Trace thermostat (§4.2) | Tracks −ρ_m/4 | Wrong sign | — | **Fails (fast limit: ρ_m ∝ a⁻⁴)** | Bounded EXCLUDED (needs referee) |
| Poisson record q (§4.6) | — | — | — | Clock/metric noise | Excluded at Planck χ⁻¹ (suggested) |

**R5-3's falsifier.** Every untuned-zero route that must still produce Λ_obs predicts w ≠ −1 at some epoch, which triggers the spectral-gap companion's falsifier (`COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md:106-107`). The q-routes above that keep w = −1 do so by tuning μ, so that observation stands.

### 5.3 Fluctuations: a link to R4-5 (suggested)

- The count A and −μ are canonically conjugate: ∂L/∂Ȧ = −ε′ (`r104_variation.out:8`). So ΔN·Δμ̄ ≥ ½ for the count N in a region, and Δρ_V = q₀Δμ̄ ≥ q₀/(2ΔN).
- With a Poisson-size ΔN = √(q₀V₄), Δρ_V ≈ √q₀/(2√V₄). At q₀ ≈ Planck density that is ≈ M_P²H², Sorkin's everpresent size.
- So the q-record sector *derives* R4-5's premises H1 (conjugacy) and H2 (count = q₀ × 4-volume, from the field equation's uniform q) (`TESTS.md:2939`). It does not derive H3: Poisson-size ΔN conflicts with §4.6's need to suppress fluctuations, and R6-3's lensing-versus-count trade-off applies (`TESTS.md:3420-3428`).
- The mean, μ − μ₀, is still free.

---

## 6. Prices (named, none adopted)

| # | Price | Axiom text touched |
|---|---|---|
| Q1 | Gravity's action contains an energy function ε(q) of the record formation density per proper 4-volume, varied at fixed records. The ε − μq coupling is then derived. This replaces R5-3's Λ9 by a sharper form | Source/action open gate (`MINIMAL_AXIOMS_2026-06-29.md:187`); Record "only records are readable" (`:82`) is compatible |
| Q2 | Formation-rate law: the formation density obeys d(ε′(q)) = 0, deterministic or hyperuniform, not a per-site coin toss | Formation rate is downstream (`:67-69,183-184`); "Admissibility is not a dynamics axiom" (`:116-123`) |
| Q3 | Vacuum records at about Planck 4-density (KV's q₀ ≈ E_P⁴; about 1.6×10⁻³ per unreduced Planck 4-volume), inert: locking nothing that decoheres matter or steers light | Record (`:77-80`); set A's A4 (`C5_O5_synthesis.md:327`); R4-5 A+ |
| Q4 | The zero datum μ = μ₀[final vacuum], KV's "self-sustained Minkowski vacuum". It equals R5-3's Λ6 (final datum) or an initial tuning to 1 part in 4.7×10⁵⁴ | Qualification "A law privileges no states" (`:94-95`) as a tension (reading) |
| Q5 | Alternatives to Q4: a membrane sector with meV charges and tension (BT), or many fluxes plus anthropic selection (BP); or a whole-history fixed count (Λ8) with a sealed, finite universe; or a dissipative thermostat with exchange current | Admissibility "one fixed nearest-neighbor admissibility rule" (`:57`) for global laws; arrow and record-production dynamics are open gates (`:185`) |

---

## 7. The owner's thought, tested as a hypothesis

- **"Count rises"** (q > 0) is *required*. The q-theory equilibrium is a vacuum that keeps forming records at a constant rate per proper 4-volume. The record count then equals q₀ × the 4-volume, i.e. it is unimodular time. "Time is the creation of records" becomes the Henneaux–Teitelboim clock (reading; §5.3).
- **"Until frozen"** (q → 0) gives ρ_V = Λ_b + ε(0), uncompensated. A frozen region is not weightless unless ε(0) = −Λ_b, which is a tuning (proved within Q1).
- **"Frozen = black hole" (reading).** Since ε′(q) = μ must be uniform, a frozen region (q = 0) cannot border a forming region (q₀ > 0) without a membrane. A frozen black-hole interior would then be a different flux phase behind a wall. Not tested.
- **"No sealed box"** rules out §4.3's global version as stated.
- **Net (suggested).** The thought fits q-theory's *steady-formation* equilibrium. It does not supply the zero: the zero needs μ = μ₀, which nothing in the thought fixes. "Until frozen" points away from zero, not toward it.

---

## 8. For the referee (FAIL/no-go items)

1. **§2.2 identification and the metric variation.** Is "records fixed under metric variation" the correct and only reading of fixed reality in set A? Is the Jacobi-formula check sufficient?
2. **Lemma PT-q (§3).**
   - Is the Noether conservation of μ complete for shift-symmetric local actions with Ω(q)R + β(q)R²?
   - Is (ii) correct with matter at the Minkowski endpoint?
   - Is "unimodular with μ ↔ Λ_c" a fair reading?
   - Are the KV quotes correctly attributed? (0711.3170 Eq. 14 is static readjustment; 0905.1919 assumes μ = μ₀.)
3. **B1.** Is the conserved-current exclusion fully general for Lorentz-invariant vacua?
4. **B4 (Lemma Tr).**
   - Is the fast-limit ρ_m ∝ a⁻⁴ derivation right?
   - Is "only curvature/trace is locally sensible" a fair premise, or is there an invariant local vacuum signal?
5. **B5.** Is the zero-temperature EW dilemma sound? The thermal-membrane regime was not analysed.
6. **B6.** Is the scale-independent δΦ ≈ Gχ⁻¹/√q₀ estimate right, including the IR factor?
7. **§4.5.** Is the inconsistency of linear-in-q vacuum energy correct in both cases (A varied; records fixed)?

**Not done.**
- No G(q) dynamical integration of KV-type models with records.
- No thermal BT regime.
- No BP multi-flux record construction.
- No fit to DESI data.
- No de Sitter asymptote as a function of μ − μ₀ with G(q).

---

## Sources

**Repository.** All citations above are to files in this worktree. Scripts and outputs: `scratchpad/C5/R10-4/scripts/`.

**Comparators verified this run:**
- [KV, Self-tuning vacuum variable…, PRD 77 085015, arXiv:0711.3170](https://arxiv.org/abs/0711.3170) and the [ar5iv full text](https://ar5iv.labs.arxiv.org/html/0711.3170): Eq. 11 ε̃ = ε − q dε/dq; Eq. 14 readjustment; Eqs. 53–54 the four-form.
- [KV, Dynamic vacuum variable…, PRD 78 063528, arXiv:0806.2805](https://arxiv.org/abs/0806.2805).
- [KV, Vacuum energy density kicked by the electroweak crossover, PRD 80 083001, arXiv:0905.1919](https://ar5iv.labs.arxiv.org/html/0905.1919).
- [KSV, Relaxation of vacuum energy in q-theory, arXiv:1601.04676](https://arxiv.org/abs/1601.04676).
- [KV, Brane realization of q-theory, arXiv:1604.06060](https://arxiv.org/abs/1604.06060).
- [Bousso–Polchinski, arXiv:hep-th/0004134](https://arxiv.org/abs/hep-th/0004134) and the [ar5iv text](https://ar5iv.labs.arxiv.org/html/hep-th/0004134).
- [DESI DR2 Results II, arXiv:2503.14738](https://arxiv.org/abs/2503.14738).

**From memory, not checked:**
- Brown–Teitelboim, PLB 195 (1987) 177 and NPB 297 (1988) 787.
- Henneaux–Teitelboim, PLB 222 (1989) 195.
- Weinberg, RMP 61 (1989) 1.
- BBN \|ΔG/G\| ≲ 0.1.
- That a 4-form has no propagating degrees of freedom in 4D.
