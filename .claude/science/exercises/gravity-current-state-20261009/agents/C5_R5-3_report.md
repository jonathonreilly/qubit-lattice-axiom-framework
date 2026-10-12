# C5 R5-3: the mean of Λ. Can any set make ⟨Λ⟩ = 0 without tuning?

**Worker.** Claude Opus 5.5, the same model family as the supervisor and the R4-5 worker. Not refereed. Run 2026-10-12, 13:39Z to 14:08Z. No repository file was edited.

**Scratch.** `scratchpad/C5/R5-3/`. Scripts and outputs are in `scripts/`:
- `r53_numbers.py/.out`: phase-transition sizes, a sympy check of Lemma PT on FRW, the Baum–Hawking exponent, the fixed-4-volume saddle, and the equilibrium identity.
- `r53_sequester.py/.out`: the flat-FRW Kaloper–Padilla (KP) toy and the identity check.
- `r53_closed_scan.py/.out`: first closed-universe scan. Its quadrature columns are unreliable and superseded (see §3.3).
- `r53_closed_scan2.py/.out`: closed-universe scan with the integrals carried as ODE components (the one to use).
- `r53_curvature_bound.py/.out`: what KP's constraint demands of a universe that looks like ours.

**Read.**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md` "Campaign C5" through "C5 Round 5, items 2–3" (2302–2897); `SUMMARY.md` §§21–22; `PRICE_NOTE.md` §§1, 5, 6 and the v6 delta; `agents/C5_O3_report.md` and its referee (`C5_O3_referee.md`, the Λ lines of `C5_O3_referee_full.md`); the R4-5 report (unrefereed).
- Prior art: `docs/COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md` and its 05-17 audit note; `COSMOLOGICAL_CONSTANT_VACUUM_ENERGY_AUDIT_NOTE.md`; `UNIVERSAL_GR_INDUCED_COSMOLOGICAL_CONSTANT_BOUNDED_THEOREM_NOTE_2026-06-08.md` (the "W-native induced vacuum stress tadpole" note R4-5 cites); the head of `COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md`; the head of `DARK_ENERGY_EOS_RETAINED_COROLLARY_THEOREM_NOTE.md`; `COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md` ("Honest Remaining Gap"); `THE_VACUUM_QUESTION_IS_ONE_COEFFICIENT_OF_THE_LAW_…`; `THE_RECORD_MAP_KEEPS_THE_MASS_FRACTION_…_VACUUMS_WEIGHTLESSNESS_IS_A_REFERENCE_CHOICE_…`; the heads of the rate-ruler and half-filled-sea vacuum notes.
- Packet grep for unimodular, sequester*, Baum, Coleman, Kaloper, Weinberg, self-tun*, everpresent, Henneaux and Josset. Hits: `B_referee.md:96`, `RN_L3_report.md:249`, `C5_R2-3_report.md:104-117`, `C5_O3_report.md:98-104`, `ROUTES.md:18` and `ASSUMPTIONS.md:20,23`. The `docs/` hits for "unimodular" are the matrix sense, except the W-native tadpole note.
- The owner's thought as recorded in memory (`records-count-rises-until-frozen.md`). Treated as a hypothesis, not a rule.

**Labels.**
- **proved:** a complete argument under the stated hypotheses.
- **checked:** a numerical or symbolic check, in the scripts.
- **suggested:** argued, not proved.
- **reading:** an interpretation.
- **comparator:** outside literature. "Verified" means fetched this run; "from memory" means not checked.

---

## 0. Verdicts against the FIXED readings (`TESTS.md:2886-2898`)

| Route | Reading | One line |
|---|---|---|
| **1. Unimodular Λ, an integration constant fixed by a boundary or record condition** | **OPEN** | The axioms supply no condition that fixes Λ_c. Fixing Λ_c at the start is a tuning to 1 part in ≈ 5×10⁵⁴ at the electroweak transition alone (Lemma PT, proved; checked). Fixing Λ_eff = 0 at future infinity removes the tuning only by postulating the answer. It is non-local in time, and the observed acceleration then needs a separate dark-energy source |
| **2. Baum–Hawking/Coleman weight peaking at Λ → 0** | **OPEN** | The peak is at exactly 0⁺; Λ_obs is disfavoured against Λ_obs/2 by e^(3.3×10¹²²) (checked). The peak comes from the negative Euclidean gravitational action. A positive local weight cannot also give GR (R2-4, refereed), so in set B with Admissibility read as a positive distribution this is a bounded EXCLUDED sub-result (suggested; needs referee). Elsewhere the weight is a non-local global law, and its sign and phase are contested in the literature |
| **3. Sequestering (KP) with the record count as the global variable** | **OPEN**, with a **bounded EXCLUDED** sub-result (needs referee) | KP's own constraint ⟨R⟩ = 0 forces a closed universe (comparator, verified). Lemma S (proved) gives \|Ω_k0\| ≥ ⟨ȧ²⟩_a / ȧ0². With today's \|Ω_k\| ≲ 2×10⁻³ that needs a near-static future lasting ≳ 240 (a0/a_l) Hubble times (checked). No self-consistent history in the linear-potential toy resembles our universe (checked). The owner's thought "there is no sealed box" (an unbounded count) conflicts with the finite total count that KP needs |
| **4. A record-formation equilibrium that sets the vacuum stress to zero (owner's thought)** | **OPEN** | Zero follows only for a conserved count with a free volume, and only if gravity couples to ε − μn (Gibbs–Duhem; proved). A count that is still forming gives ε_min, a free constant (proved). In the fixed-spacing sets B and C there is no free volume. The owner's thought puts freezing only in sealed boxes (black holes), not the cosmos today. Relaxation versions need tuned initial conditions (comparator, verified: Klinkhamer–Savelainen–Volovik 2016) |

**Net (suggested).**
- No route gives ⟨Λ⟩ = 0 untuned from what the four axioms supply. R4-5's finding stands and is sharpened.
- Every untuned zero in the literature needs at least one of:
  - **(i) a law that is non-local in time**, i.e. a global or future datum: a final condition, a weight on the whole universe, or a 4-volume average;
  - **(ii) a relaxation degree of freedom.** Weinberg's no-go excludes local scalars (comparator, from memory). q-theory needs tuned initial data (comparator, verified).

  Admissibility as written is nearest-neighbour and supplies neither (`MINIMAL_AXIOMS_2026-06-29.md:57,116-123`).
- Every route that zeroes the mean but must still produce Λ_obs (1b, 2, 3) predicts w ≠ −1 at some epoch. That contradicts the w = −1 of the spectral-gap companion and triggers its falsifier (`COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md:106-107`). Route 4 sets no observed value here, and route 1a keeps w = −1 by tuning.

---

## 1. In plain words

**The problem.**
- The vacuum's own energy acts like a cosmological constant.
- The framework's lattice makes it about one Planck energy per cell, 10¹²⁰ times too big (`UNIVERSAL_GR_INDUCED_COSMOLOGICAL_CONSTANT_BOUNDED_THEOREM_NOTE_2026-06-08.md:16-20,65-68`).
- R4-5 found that the *size* of today's dark energy can come from random record counting. The *average*, however, still had to be set to zero by hand.

**What this probe finds.**
- **Moving the zero point does not help.** Any rule that subtracts a constant "vacuum reference" from the source of gravity is either invisible or inconsistent, because Einstein's equations forbid a source that changes in time unless it is rebalanced (Lemma PT, proved).
  - What remains is one free constant, Λ_c.
  - When the Higgs field settled into its vacuum, the vacuum energy dropped by about (104 GeV)⁴. That drop shows up in the expansion, whatever convention is used.
  - So if Λ_c is set at the beginning, it must be pre-set to cancel future drops to 1 part in about 10⁵⁵. That is the cosmological-constant problem in its sharpest form.
- **Ways out that need no tuning all look ahead in time.**
  - A rule fixed at the end of time ("the far future is flat").
  - A weight on whole universes (Baum–Hawking).
  - A rule that averages over the universe's entire history (sequestering).
  - Our axioms have only nearest-neighbour rules, so each of these is a new, non-local price.
- **Sequestering is the most predictive, and it fails a test.**
  - Its own constraint forces the universe to be closed and to end in a crunch.
  - Applied to a universe like ours, the bound is set by the whole history. If the universe stopped expanding now, the curvature today would have to be about 90% (the past-only value, 0.92; §3.3). Further expansion like today's only raises it.
  - The bound falls below the observed limit, about 0.2%, only if the universe later hovers almost motionless for hundreds of Hubble times.
- **The owner's "records rise until frozen".**
  - In equilibrium physics, a self-contained medium with a fixed number of grains settles at zero pressure. That would make the vacuum weightless.
  - It needs the count fixed (frozen) and the volume free. The owner's own thought says the universe is not a sealed box and its count keeps rising.
  - On a fixed grid, the volume is not free.

---

## 2. Hypotheses common to all routes (stated before titles)

- **G1 (metric bridge; supplied, not derived).** A Lorentzian metric with Levi-Civita connection obeys G_μν + Λ(x) g_μν = 8πG S_μν, with S built from matter. In GR Λ is a constant. In unimodular gravity (UG) the trace-free equations plus the Bianchi identity give this form with ∂_νΛ = 8πG ∇^μS_μν (`C5_R2-3_report.md:104-112`; `RN_L3_report.md:249`). The axioms supply no metric or source law: source/action is an open gate (`MINIMAL_AXIOMS_2026-06-29.md:187`).
- **G2.** The true matter stress T, including the potential energy V(φ) of the current vacuum, is covariantly conserved. This holds for diffeomorphism-invariant matter on shell.
- **G3.** A "vacuum reference" rule is S = T + f g, with f a state-independent c-number. f may change at phase transitions; this is P13 / R₀ / O3 rows #5 and #12 (`PRICE_NOTE.md` v6 §4; `C5_O3_report.md:97,104`).

**Outside realizations not covered.**
- Theories without a Levi-Civita metric bridge, e.g. teleparallel, or bimetric with an independent volume form.
- Non-c-number subtractions, i.e. state-dependent sources, which O3 notes the equivalence principle (EP) restricts.
- Explicit violation of the conservation in G2.

---

## 3. Results

### 3.1 Lemma PT (phase-transition transfer). **Proved; checked symbolically on FRW.**

**Statement.** Under G1–G3, the Bianchi identity gives ∂_ν(Λ − 8πG f) = 0, so Λ − 8πG f = Λ_c, a constant, and the field equation is G_μν + Λ_c g_μν = 8πG T_μν.
- **In GR** (Λ constant), a time-varying f is inconsistent.
- **In UG**, the subtraction is undone by Λ(x).
- Either way the geometry depends only on Λ_c and the true T.

**Proof.** ∇^μG_μν = 0 ⇒ ∂_νΛ = 8πG ∇^μ(T_μν + f g_μν) = 8πG ∂_ν f. ∎ The sympy check (`r53_numbers.out` §2) gives d/dt E₀₀ + 3H(E₀₀ + E_ii) = 8πG ḟ − Λ̇ on T-conserving FRW matter.

**Corollary (proved).**
- Define Λ_eff(t) ≡ Λ_c + 8πG V(φ(t)). Then Λ_eff(late) − Λ_eff(early) = −8πG ΣΔV_i, independent of every convention and of whether the theory is GR or UG.
- So ⟨Λ_eff⟩ ≈ 0 today requires one of:
  - (a) an initial datum tuned to cancel the later ΔV_i to precision ρ_Λ;
  - (b) a datum fixed at the end, i.e. non-local in time;
  - (c) a mechanism outside G1–G3: a global constraint, an extra relaxing field, or modified gravity.

**Sizes (checked, `r53_numbers.out` §1; inputs are comparators).**
- Electroweak: ΔV = m_H²v²/8 = 1.19×10⁸ GeV⁴ = (104 GeV)⁴ = **4.7×10⁵⁴ ρ_Λ**.
- QCD: 4×10⁻⁴ to 3×10⁻³ GeV⁴ = **2×10⁴³ to 1.3×10⁴⁴ ρ_Λ**.
- Inflation, if any: up to 2.6×10¹¹¹ ρ_Λ (r < 0.036; from memory).
- The constant Planck-cell tadpole, ≈ M̄_Pl⁴ = 1.4×10¹²⁰ ρ_Λ, is absorbed into Λ_c. Only the *changes* bite.

**What this does to prior art.**
- It sharpens O3's rows #5, #6 and #12 (`C5_O3_report.md:97-104`). A vacuum-referenced or "records-only" source rule cannot remove phase-transition differences in any metric theory that has the Bianchi identity.
- It is consistent with the record-map note's T4, "P0 removes any additive constant source … cannot determine the cosmological Λ" (`THE_RECORD_MAP_…_NOTE_2026-09-04.md:155-159`).
- It addresses three routes the W-native tadpole note left open: subtraction, unimodular decoupling and record unobservability (`UNIVERSAL_GR_INDUCED_…:25-27,58-63,94`). All three reduce to "Λ_c is free". The note's computed-tadpole negative is not changed.

### 3.2 Route 1: unimodular Λ fixed by a boundary or record condition — **OPEN**

**What the axioms supply.**
- Nothing that fixes Λ_c. The axioms name no metric, no action and no time metric (`MINIMAL_AXIOMS_2026-06-29.md:116-123,185-187`).
- "A site with no record cannot be read" (`:82-83`), together with the removal of I(∅) = 0 (`:220-225`), is consistent with "absolute vacuum energy is not an observable". By Lemma PT that is exactly UG's statement, and it leaves Λ_c free (reading).
- Owner's thought plus R4-5's price Λ1 (count = 4-volume): the count is unimodular time T, conjugate to Λ_c.
  - The count is readable (`:82-83`), so T is physical data, and the Λ_c-state is set by initial conditions.
  - *Reading/comparator:* if T were unobservable (gauge), integrating over all T would project onto Λ_c = 0, like ∫dt e^{−iEt} = 2πδ(E). Readable records forbid treating the count as gauge. So no record condition yields Λ_c = 0 from the axioms (suggested).

**Sub-variants.**
- **1a. Initial datum.** A tuning, by Lemma PT: 1 part in 4.7×10⁵⁴ (EW), 10⁴⁴ (QCD), up to 10¹¹¹ with inflation. Not VIABLE (fails "no fine tuning"). Not EXCLUDED (no bound violated).
- **1b. Future-asymptotic datum** (Λ_eff → 0 at future infinity, or on the frozen final configuration).
  - **What it gives.** No tuning, since the condition is imposed on the late-time total. But the datum *is* the answer, so it gives ⟨Λ⟩ = 0 by postulate, not by mechanism.
  - **Prices.**
    - It is non-local in time.
    - It sits in tension with the Qualification "A law privileges no states" (`MINIMAL_AXIOMS_2026-06-29.md:94-95`), since it singles out solutions by the value of a constant of motion (reading).
    - If the vacuum the fields end in depends on the expansion history, which depends on Λ_c, the condition becomes a fixed-point problem with no guaranteed solution (suggested).
  - **Against observation.** Λ_eff(∞) = 0 with today's acceleration requires dynamical dark energy, so w ≠ −1:
    - **Quintessence:** compatible in sign with the DESI DR2 thawing hint (w₀ > −1, w_a < 0; 3.1σ BAO+CMB, 2.8–4.2σ with SNe; comparator, verified abstract). Its potential scale ~ρ_Λ is a new unexplained small number.
    - **R4-5's everpresent fluctuation:** CMB-disfavoured in Model 1 (DNY; R4-5 §6).
  - **Disposition.** I record 1b as OPEN, not VIABLE, because a price that equals the answer does not "give" ⟨Λ⟩ = 0. If the owner counts an imposed asymptotic datum as a named price, 1b reads VIABLE-by-postulate with prices Λ6 and a dark-energy source; that is an owner call.
- **1c. Asymptotic flatness at spatial infinity.** Not available in FRW. The prior-art carrier is S³, which has no boundary (`COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md:12-20`) (reading).

**Comparators.**
- Padilla–Saltas (verified abstract): classically UG is a gauge-fixed GR and "cannot bring a new perspective" to the problem.
- Henneaux–Teitelboim, PLB 222 (1989) 195 (from memory): Λ is conjugate to 4-volume time.
- `B_referee.md:96`: "conjugacy to four-volume depends on the formulation."

### 3.3 Route 3: sequestering with the count as the global variable — **OPEN; bounded EXCLUDED sub-result (needs referee)**

**Mechanism** (comparator, verified from Kaloper–Padilla arXiv:1406.0711 via ar5iv and the PRL abstract 1309.6562).
- The matter scales depend on the spacetime 4-volume through global variables. Every constant vacuum energy, including loops and phase transitions, is cancelled.
- The residual is Λ_eff = ¼⟨τ^α_α⟩ = −((1−3w)/4)⟨ρ⟩, which is **negative for dust**.
- The 4-volume must be finite, so the universe crunches and today's acceleration is transient.
- The trace equation gives the global constraint **⟨R⟩ = 0**. KP: "having a large old approximately FRW universe does require k=1"; "small inhomogeneous universes may evade this."

**What the axioms supply.**
- A monotone record count. Under the price Λ1 it is the 4-volume, and the global variable would be N_total/ρ.
- Nothing global. Admissibility is one nearest-neighbour rule (`MINIMAL_AXIOMS_2026-06-29.md:57`), whereas KP's σ(Λ/λ⁴μ⁴) sits outside the spacetime integral: the law at here-now depends on the whole history, future included.
- The owner's thought: "there is no sealed box … it could be infinite" (memory). If the count is unbounded, the 4-volume is infinite and KP's averages and matter scales degenerate. A finite total count, i.e. a cosmic freeze or end of time, is required. The thought places freezing only in sealed boxes (black holes) (reading).

**Lemma S (FRW sequestering curvature bound). Proved.**
- *Hypotheses.*
  - Homogeneous FRW, k ∈ {0, +1}, Big Bang to crunch.
  - a³H → 0⁺ (or ≥ 0) at the bang and a³H ≤ 0 at the crunch.
  - KP's original global constraint ⟨R⟩ = 0, with the averages finite.
- *Statement.* ∫a³R dt = 6[a²ȧ] − 6∫aȧ² dt + 6k∫a dt, so
  - k∫a dt = ∫aȧ² dt + |a²ȧ|_crunch + a²ȧ|_bang ≥ ∫aȧ² dt;
  - **|Ω_k0| = k/ȧ0² ≥ ⟨ȧ²⟩_a / ȧ0²**, where ⟨·⟩_a weights by a dt over the whole history.
  - For k = 0 the constraint is impossible, and for k = −1 a fortiori. This reproduces KP's k = 1 requirement.
- *Proof.* a²ä = d(a²ȧ)/dt − 2aȧ², with R = 6(ä/a + ȧ²/a² + k/a²). ∎
- *Checks.* Flat toy: F − C equals −¼⟨R⟩ from the identity to 0.2% (`r53_sequester.out`, top). Closed toy: k∫a = ∫aȧ² − [a³H] to all printed digits, with both integrals carried as ODE components (`r53_closed_scan2.out`). Two rows that disagree (s,k) = (1,1.5), (2,2) are discontinuities in F − C, not true fixed points (reading of the mismatch).

**Against observation.**
- **Curvature data.** DESI DR2 + CMB gives Ω_K = 0.0023 ± 0.0011, a mild preference for *open*; DR2-IV gives 10³Ω_K = 2.1 ± 1.1 (comparator; secondary sources, verified only via search summaries). A closed universe with |Ω_k0| ≳ 3×10⁻³ is disfavoured at ≈ 5σ against the first value; I use |Ω_k0| ≤ 2×10⁻³ as the working bound.
- **What the bound demands** (checked, `r53_curvature_bound.out`).
  - A ΛCDM-like past (Ω_m = 0.315) alone gives ⟨ȧ²⟩_a = 0.92 ȧ0².
  - Lemma S then needs total ∫a dt ≥ 242 a0/H0 for |Ω_k0| ≤ 0.002 (142 for 0.0034, 483 for 0.001).
  - That means a future phase with ȧ ≈ 0 lasting ≳ 240 (a0/a_l) Hubble times.
  - Any future expansion at ȧ ~ ȧ0 makes it worse: continuing ΛCDM for 1/H0 already raises the bound to 2.0.
  - A long ȧ ≈ 0, ä ≈ 0 phase is an Einstein-static-like state (unstable). It needs an engineered potential (suggested), i.e. a tuning.
- **Toy class** (dust + scalar with linear potential, the trigger KP mention; flat and closed; checked).
  - **Flat:** no fixed point, since F − C ≥ 2.4–19.5 > 0 for every slope s (`r53_sequester.out`).
  - **Closed:** every self-consistent history found (s = 0.5–4, k = 0.8–2) is matter- and curvature-dominated throughout its expansion, with min Ω_m = 1.004–1.010 and q > 0. None reaches Ω_m ≤ 0.315 with q < 0 (`r53_closed_scan2.out`).
- **DESI.** The *sign* structure KP predict, a negative residual plus a thawing field and a future crunch, matches the DR2 quadrant w₀ > −1, w_a < 0. Tye et al. fit DESI+DES with a negative Λ plus an ultralight axion and get a total lifespan ≈ 33 Gyr (arXiv:2506.24011; comparator, verified via search summary). That fit is not sequestering and does not supply k = +1 at the required level.

**Disposition.**
- **Bounded EXCLUDED** (violates the curvature bound) for: KP's original constraint, homogeneous FRW, no ≳ 240-Hubble-time loiter. This needs the codex referee before it is recorded.
- **Not covered:** the Gauss–Bonnet-extended sequester (KP 2017) and the "manifestly local" version (KPSZ 2016), whose global constraints differ (from memory, not checked); inhomogeneous or small universes (KP's own escape); the Ben-Dayan et al. conformal version.
- So the route is **OPEN**. Even if a variant survives, the prices are a global law (Λ8), Λ1, and a finite total count that contradicts the owner's "no sealed box" as stated.

### 3.4 Route 2: Baum–Hawking/Coleman — **OPEN; bounded EXCLUDED sub-result in set B (suggested; needs referee)**

**Numbers (checked, `r53_numbers.out` §3).**
- I_E(S⁴) = πr²(Λr² − 6)/(3G). The stationary point r² = 3/Λ is a minimum along the overall scale (d²I/dr² = 8π/G), with I* = −3π/(GΛ).
- At Λ_obs: 3π/(ℓ_P²Λ_obs) = 3.3×10¹²². So P(Λ_obs/2)/P(Λ_obs) = e^(3.3×10¹²²).
- The weight predicts Λ_eff = 0⁺ exactly. Λ_obs needs another source, as in 1b.
- The weight is evaluated on the *final* vacuum's S⁴, so it is global and teleological. That is why it is untuned against phase transitions (reading).

**Set B (Euclidean Z⁴; Admissibility read as the conditional of a positive Gibbs weight).**
- The e^{+3π/GΛ} peak exists because the Euclidean Einstein–Hilbert action is negative on S⁴, and that action is unbounded below along conformal directions.
- Dilemma (suggested):
  - (a) If the weight is positive and normalizable, R2-4 (refereed CWC, under W1–W3) gives γ ≤ ½, so GR is not the low-energy limit (`TESTS.md:2728-2730`).
  - (b) If the conformal contour is rotated (Gibbons–Hawking–Perry), the weight is complex and the S⁴ term carries a phase. The search summary of arXiv:2506.20547 says that in 4D the phase is negative, which complicates Coleman's argument and could push Λ away from zero (comparator, secondary). Carroll's review states that Lorentzian analogues did not reproduce the peak (comparator, verified via search summary).
- Either way, "Admissibility's probability distribution yields a Λ → 0 peak together with GR" fails in the stated class. This is bounded EXCLUDED in set B (suggested; it combines the refereed R2-4 with the conformal-sign observation, so it needs a referee).

**Sets A, B′ and C (Lorentzian).**
- No Euclidean weight is supplied.
- Admissibility's distribution is per-site and nearest-neighbour (`MINIMAL_AXIOMS_2026-06-29.md:57-61`). A weight on Λ_c is a law on a global constant, which is price Λ7.

**Fixed-count variant (reading/suggested; arithmetic checked).**
- Suppose the total count is fixed (frozen), with count = 4-volume. The unimodular "microcanonical" saddle Z(V) = ∫dΛ e^{ΛV/8πG} e^{3π/GΛ} gives Λ* = √(24π²/V) > 0.
- Λ* = Λ_obs needs a total 4-volume V = 2.9×10²⁴⁵ ℓ_P⁴ = 56 (c/H0)⁴.
- This is just the de Sitter S⁴ volume at radius √(3/Λ_obs), so it restates Λ = 3/R² with R swapped for V. Λ = 3/R² is the same structure as the prior-art spectral-gap identity (`COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md:15-20`), with the same open "what fixes R" gap (`COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md:143-144`). It is not a derivation.

### 3.5 Route 4: record-formation equilibrium (owner's thought) — **OPEN**

**Identity (proved; checked symbolically, `r53_numbers.out` §5).** For an extensive energy E = V ε(N/V):
- **(b) Conserved N, free V:** equilibrium at fixed N with V free (self-sustained, no external pressure) gives ∂E/∂V|_N = ε − nε′(n) = −p = 0. So the grand-potential density ε − μn vanishes. This is Volovik's argument.
- **(a) Forming count:** if N is *not* conserved and records form while that lowers the energy, formation stops at ε′(n*) = μ = 0, or at saturation. The vacuum energy is then ε(n*) = ε_min, a free number with no zero condition.
- **(c) Fixed density:** with fixed spacing and the count saturated at one record per site, n = n_max is not a variable and nothing sets ε − μn to zero.

**What the axioms supply.**
- Records form; records are permanent; at most one record per site (`MINIMAL_AXIOMS_2026-06-29.md:77-80`). So the count is non-decreasing and capped by the sites.
- Not supplied: a Hamiltonian or energy ε(n), an equilibrium or formation rule, a free volume (Lattice fixes Z³, `:37`), or a gravitational coupling, let alone a coupling to ε − μn (`:114-123,183-187`).

**Against the owner's thought.**
- The thought ("count rises … there is no sealed box … a sealed box … frozen … black hole") places the cosmos in case (a): the count is still forming.
- Freezing, which would make the count conserved as in (b), is local and horizon-like. In a frozen region the lapse goes to 0 (memory note), so no cosmic time passes.
- In B and C the frozen state is case (c), the saturation of R4-5's Lemma C-count (R4-5 §4.1).

**What zero would need.** Case (b) needs a conserved count with free volume, i.e. dynamical spacing (a Lattice price in B/C, available in A), *and* gravity coupled to ε − μn.
- In q-theory's 4-form realization that coupling is derived. For a record density it is a new source rule, price Λ9.
- By Lemma PT any such rule must be a constant or a conserved-sector effect; a c-number reference does not do it.
- Dynamic relaxation does not reach Minkowski without tuned initial conditions (Klinkhamer–Savelainen–Volovik, arXiv:1601.04676, verified abstract: "The Minkowski asymptote still requires fine-tuning of the initial conditions"; de Sitter decay is needed).
- Weinberg's 1989 no-go for local constant scalar fields (from memory) is evaded only because q is non-fundamental (KV 0711.3170, verified abstract).

**Against observation.** At exact equilibrium Λ_eff = 0. The observed value would have to come from departures from equilibrium (KV: an "imperfect vacuum"), which gives no w(z) prediction here.

**Disposition.** OPEN. Not EXCLUDED: no bound is violated and a continuum version (set A plus prices) is not inconsistent. Not VIABLE: in every case the axioms or the owner's thought supply, the zero condition fails.

---

## 4. Per set (what is supplied → what must be added)

| Set | Route 1 (UG) | Route 2 (BH) | Route 3 (sequester) | Route 4 (equilibrium) |
|---|---|---|---|---|
| **A** (continuum + rare records) | No count-volume link (R4-5 §3: H2 fails). UG is a pure metric choice. Λ_c is free (Lemma PT) | No weight supplied | ∫√g is available from the continuum; global variables and closure needed (Lemma S) | Free volume available; needs a conserved count, ε(n), and the ε − μn coupling |
| **A+ / B′+** (inert Planck-density records, R4-5) | Count = T (Λ1); readable, so Λ_c is free (reading) | Global weight (Λ7) | Count = global variable (Λ1 + Λ8); finite total count; Lemma S | Count still forming → case (a) |
| **B** (Euclidean Z⁴) | No Lorentzian past cone (R4-5 §3) | Positive-weight dilemma with R2-4 (§3.4) | Fixed sites: 4-volume = site count (Euclidean) | Fixed spacing → case (c) |
| **C** (Z³ + ticks) | Lemma C-count caps the count at the 3-volume (R4-5 §4.1). Needs Λ5 | No weight | Same cap; Λ5 needed | Saturation → case (c) |

---

## 5. Prices named (none adopted; they extend R4-5's Λ1–Λ5)

| # | Price | Axiom text touched |
|---|---|---|
| Λ6 | A future-asymptotic (or final-configuration) datum Λ_eff = 0 on the integration constant | Qualification: "A law privileges no states" (`MINIMAL_AXIOMS_2026-06-29.md:94-95`), as a tension (reading); time metric and arrow are open gates (`:185-186`) |
| Λ7 | A global probability law on Λ_c (Baum–Hawking/Coleman), with a sign/contour choice | Admissibility: per-site, nearest-neighbour distribution (`:57-61`); in B, positivity against R2-4 |
| Λ8 | Whole-history global variables: matter scales set by the total record count (sequestering), plus a finite total count and k = +1 | Admissibility "one fixed nearest-neighbor admissibility rule" (`:57`); Lattice Z³ (`:37`) for closure; the owner's thought "no sealed box" as stated |
| Λ9 | A thermodynamic source rule: gravity couples to ε − μn of a conserved record density with free volume | Source/action open gate (`:187`); "Admissibility is not a dynamics axiom" (`:116-123`); Lattice fixed spacing (`:37`) in B/C |
| (also) | A dynamical dark-energy field for the observed acceleration in 1b, 2 and 3 | none; a new sector |

---

## 6. Relation to prior art (each counted once)

- **`COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md`** (Λ = 3/R², R supplied; w = −1, `:15-20,90-92,104-109`).
  - It identifies Λ with a geometric gap. It presupposes that the O(1)-per-cell tadpole is already gone, so it sits downstream of R5-3's question.
  - Routes 1b, 2, 3 and 4 all need w ≠ −1 for the observed acceleration and trigger its falsifier (`:106-107`).
  - Read through Lemma PT, supplying R is route 1 with the datum given as R. Its "Honest Remaining Gap" item 1 (`COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md:143-144`) is the same open datum.
- **`COSMOLOGICAL_CONSTANT_VACUUM_ENERGY_AUDIT_NOTE.md:14-21,59-62`.** Consistent: finiteness does not suppress. Lemma PT adds that re-referencing does not either.
- **W-native tadpole note (`UNIVERSAL_GR_INDUCED_…_2026-06-08.md`).** Its open routes (`:25-27,58-63,78-82,94`) are now narrowed:
  - subtraction and unimodular reduce to a free Λ_c (Lemma PT);
  - sequestering is bounded by Lemma S;
  - record unobservability is a UG restatement (reading).

  Its computed-tadpole result is unchanged. Nothing here is a framework-level no-go.
- **Record-map T4 (`…_2026-09-04.md:147-159`).** Agrees.
- **`C5_O3_report.md:97-104`** (rows #5, #6, #11, #12) and the O3 referee.
  - #6 ("value free") is confirmed and given the phase-transition number.
  - #11 (self-tuning dead): the self-tuning *scalar* is dead (Weinberg, from memory), but sequestering and q-theory are distinct and are treated here.
  - #12 is subsumed by Lemma PT.
- **R4-5 §5** (⟨Λ⟩ = 0 is a premise in every set): confirmed and sharpened. The mean has to be fixed to the fluctuation size (~H²), i.e. to precision ρ_Λ, which is the same precision as the old problem.
- **`B_referee.md:96`; `RN_L3_report.md:249`; `C5_R2-3_report.md:104-117`.** These give the UG gradient structure used in G1 and Lemma PT.

---

## 7. For the referee (FAIL / no-go items)

1. **Lemma PT.** Is it complete under G1–G3? Does any c-number reference rule outside G3 survive the EP restriction?
2. **Lemma S and the bounded EXCLUDED of route 3.**
   - Check the identity and the boundary-sign hypotheses.
   - Check the inference |Ω_k0| ≥ ⟨ȧ²⟩_a/ȧ0² and the 242 a0/H0 requirement (`r53_curvature_bound.out`).
   - Confirm KP's ⟨R⟩ = 0 in the original sequester.
   - Say whether the Gauss–Bonnet or "manifestly local" versions change the constraint. Not checked here.
3. **Route 2, set B dilemma.** Is R2-4's W1–W3 class the right one to apply to a weight on a global constant? Is the Polchinski-phase statement correctly sourced? Here it is secondary.
4. **Route 4 trichotomy.** Is case (a) (a forming count gives ε_min) correct for a monotone, non-conserved count with no reservoir?

**Not done.**
- A fit of any route to DESI DR2 data.
- The GB-extended sequester.
- An inhomogeneous sequestering model.
- A record-density realization of q-theory's 4-form.

---

## Sources

Arithmetic and code are in `scratchpad/C5/R5-3/scripts/`. Literature (comparator):
- [Kaloper–Padilla PRL abstract, arXiv:1309.6562](https://arxiv.org/abs/1309.6562) and [arXiv:1406.0711 (ar5iv)](https://ar5iv.labs.arxiv.org/html/1406.0711): Λ_eff = ¼⟨τ⟩; ⟨R⟩ = 0; k = 1; transient acceleration; collapse.
- [Padilla–Saltas, arXiv:1409.3573](https://arxiv.org/abs/1409.3573).
- [Klinkhamer–Volovik, arXiv:0711.3170](https://ar5iv.arxiv.org/html/0711.3170) and [Klinkhamer–Savelainen–Volovik, arXiv:1601.04676](https://arxiv.org/abs/1601.04676).
- [DESI DR2 BAO, arXiv:2503.14738](https://arxiv.org/abs/2503.14738).
- [Cortês–Liddle on DR2 significance](https://arxiv.org/html/2504.15336v3).
- [Curvature in light of DR2, arXiv:2505.00659](https://arxiv.org/html/2505.00659v2) and [DESI DR2 IV, arXiv:2607.27410](https://arxiv.org/pdf/2607.27410).
- [Tye et al., "The Lifespan of our Universe", arXiv:2506.24011](https://arxiv.org/pdf/2506.24011).
- [Norm of the no-boundary state, arXiv:2506.20547](https://arxiv.org/pdf/2506.20547) (Polchinski phase, secondary).
- [Carroll ARA&A review](https://ned.ipac.caltech.edu/level5/Carroll/Carroll5_1.html) (Coleman sign problem).
- [Ben-Dayan et al., arXiv:1507.04158](https://ar5iv.arxiv.org/html/1507.04158).
- From memory, not checked: Weinberg RMP 61 (1989) 1; Henneaux–Teitelboim PLB 222 (1989) 195; Baum PLB 133 (1983) 185; Hawking PLB 134 (1984) 403; Coleman NPB 310 (1988) 643; Polchinski PLB 219 (1989) 251; BICEP/Keck r < 0.036.
