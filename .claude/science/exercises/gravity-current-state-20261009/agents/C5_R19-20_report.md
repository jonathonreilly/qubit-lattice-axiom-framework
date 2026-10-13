# C5 R19-20 report: do the source clauses reduce to one statement, and does the grid then predict anything about gravity?

**Author and provenance.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. Run 2026-10-13, 06:05Z to about 06:30Z. I edited no repository file and downloaded nothing.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `TESTS` = `P/TESTS.md`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`. `SP/` = the session scratchpad `.../scratchpad/C5/`. `S/` = `SP/R19-20/` (this folder). `vX` = the referee record of item X in `TESTS`, or `P/agents/C5_X_referee_verdict.md` where a line is cited there. `rX` = `P/agents/C5_X_report.md`.

**Labels.** Each claim carries one of these labels:
- **proved**: a complete argument under stated hypotheses (mine, so unrefereed);
- **checked**: numerics run here;
- **suggested**: argued, not proved;
- **reading**: interpretation;
- **comparator**: an outside reference;
- **RECALLED**: from memory.

I also mark each source: **[ref]** means the referee record, and **[worker]** means an unrefereed worker report.

**Naming collision.** C5 uses "W1" for two different things:
- **W1-Ward** is the conservation identity, as in R13-5, R19-5 and R19-9.
- **W1-weight** is R19-6's clause, "the gravitating source is the weight-1 density" (`TESTS:7570`).

This item's W1 is W1-weight, and I use that name throughout.

**Pending inputs, used only as unrefereed claims.**
- R19-17 [worker] (`rR19-17`).
- R19-19 [worker; referee running] (`rR19-19`, `TESTS:8133-8143`).
- R19-16 [worker], which is not source-side and is not used.

R19-15's referee verdict arrived during this run. It is recorded at `TESTS:8127-8132` and used as [ref].

---

## 0. Reading against the FIXED readings (`TESTS:8090-8093`)

**Reading: IRREDUCIBLE** (literal reading; same-family, so I recommend a referee).
- **The registered candidate clause** is "the gravitating source is ⟨T⟩ minus the lowest state's response through O(q²), replaced by its Lorentz-invariant form", called (Σ) below.
  - It implies (S), (S\*) and (S\*\*) (proved, definitional).
  - On V1 it plausibly implies (S_ad) (suggested).
  - It does **not** imply W1-weight, the gravitational-self-stress part of N_red, or (d-i)'s receiver.
- **Two listed clauses are logically independent of (S\*) (§2.3).** Each side of each pair has a model built from refereed laws (one only in its refereed scope). In the set-A models, (S\*) holds by the continuum vacuum's Lorentz invariance (comparator; count checked):
  - **D1:** W1-weight and (S\*).
  - **D2:** completion N, which is inside N_red, and (S\*).

  The reasons are stated there.
- **The minimal bridge is three mutually independent clauses with zero numbers:**
  - (Σ), the vacuum renormalization;
  - W1-weight, with gravity's own stress (the source density, GR's self-coupling);
  - a carrier, which is (d-i) with site creation in C-box-E, or the lattice-frame law on V1.

**A registration collision.**
- ONE-CLAUSE and IRREDUCIBLE are not mutually exclusive as written. Independent clauses can both follow from a stronger one.
- One sentence does imply every listed clause: "the gravity sector is GR, sourced gauge-independently by the state's stress above the law's lowest state" (§2.5). But that sentence is the conjunction of the independent parts. It is GR stipulated, not a reduction.
- Under literal-first (`TESTS:7124`) and the campaign's clause counting (R19-6's "4 clauses", `TESTS:7575`), I report IRREDUCIBLE. I flag the collision for the referee, as with `vR17-12:17`.

**Against the expectation (`TESTS:8094`).**
- **Borne out for the vacuum family.** The vacuum-defect clauses (constant, enthalpy of the lowest state, shear, O(q²) rows, the lowest state's gauge-dependent zero point) are one statement.
- **Not borne out for the whole list.** W1-weight and N carry content about every state and about GR's nonlinearity, which no vacuum clause supplies.
- **The residual prediction list in (b) is borne out in kind, with one change.** Its largest entry is not a residual LV signal. It is a hazard: the subtraction is tied to today's lowest state (§4, item 2).

---

## 1. In plain words

- **The vacuum pieces really are one rule.** "The lowest state weighs nothing" (S), "its response to uniform stretching does not gravitate" (S\*), and "its response through two derivatives does not gravitate" (S\*\*) are three truncations of one sentence: the vacuum's own gravitational effect, up to two derivatives, is replaced by what a relativistic vacuum would give, with zero cosmological constant.
- **Two other pieces are not vacuum rules.**
  - **W1-weight** says which density gravitates, for every state, not only the vacuum.
  - **N** says gravity's own energy gravitates. That is Einstein's nonlinearity, and it is what gets Mercury's orbit right.

  A growing grid also needs somewhere to put what the vacuum rule removes: site creation, or the lattice's own motion.
- **The vacuum rule imposes relativity rather than deriving it.**
  - Count the numbers that describe how a cubic lattice vacuum can respond to gravity, up to two derivatives. There are 34 (checked).
  - A relativistic vacuum has 2: the cosmological constant and a Newton-constant shift.
  - The rule sets all 34. Of these:
    - 30 are gravity's gauge (Ward) identities, which free local lattice matter does not supply in any class tested (W15);
    - 2 are Lorentz conditions;
    - 1 is Λ = 0 for the lowest state, which is (S);
    - 1 is a convention for G.

  So, apart from (S) and the G convention, the rule imposes on the lattice vacuum what symmetry gives a continuum theory for free.
- **What the grid still predicts beyond GR plus the Standard Model:**
  - **Today's vacuum: nothing observable.** The graviton speed changes by about 1e-84 at LIGO frequencies.
  - **Any epoch when the universe was not in today's lowest state: a large unsubtracted lattice effect.**
    - On the current root edges it is a tachyonic graviton mass of about 6e10 GeV before the electroweak crossover (worker estimate; R19-21 tests it).
    - There is also a pressure term, up to about 1e106 ρ_Λ on Wilson-type edges, which only (d-i) absorbs (suggested).

    This looks like a conflict, not a prediction to welcome.
  - **Planck-mass relics and a far-field mass anomaly.** Both depend on history and are bounded.
  - **In a site-creating grid,** a conditional energy injection that tracks the Hubble rate.
- **The one sharp, testable prediction on the source side is M_t ≤ 170.9 GeV, or new particles.** It comes from (S), which a continuum theory can adopt equally. It is not evidence for the grid.

---

## 2. (a) The single clause, and what it implies

### 2.1 The clause (Σ), as an equation

**Hypotheses (stated before titles).**
- **The source composite.** Let 𝔗^{μν} be the gravitating composite, weight unspecified. ⟨·⟩_state is its expectation in the actual state.
- **The lowest state's local data.** Let s₀(ḡ) = ⟨𝔗⟩ in the law's lowest state in the uniform static background ḡ, to all orders in ḡ. Let Π_vac(p; ḡ) be that state's linear response to h, and T₂[Π_vac] its Taylor polynomial through total degree 2 in p = (ω, q). Degree 1 is excluded by inversion parity.
- **Fixed lattice frame (C-box).** On V1 the frame X^I is dynamical, and the same subtraction is R19-17's T_ad[g, X] through adiabatic order 2 (`rR19-17:18,61-71`).

**(Σ):**

  S_grav^{μν}[h] = ⟨𝔗^{μν}⟩_{state,h} − s₀^{μν}(ḡ) − ( T₂[Π_vac] − Z·E_EH )^{μνρσ} h_ρσ ,

where E_EH is the linearized Einstein operator and Z is a convention: Z = 0 for (S\*\*₀); a free Z is absorbed into G (`AX:189-190`).

**In words.** The law's lowest state contributes to the gravitating source only through its Lorentz-invariant local form: Z·(Einstein–Hilbert), with zero cosmological term. This holds through two derivatives, to all orders in a uniform metric, and to linear order in h for the derivative terms.

**Properties.**
- **Local** (proved): a finite-order differential operator, provided T₂ exists. Existence is refereed analyticity for the root content (vR19-11, `TESTS:7988-7990`). For gapless fields, the degree-2 coefficients are IR-finite (suggested, `rR19-17:69`; `rR19-19` §3.2).
- **Number-free** (proved): its coefficients are functionals of the law.
- **Not forced** by the four texts (reading, as in `vR17-3`, `TESTS:6015-6016`). "The lowest state" needs a Hamiltonian, which the axioms do not name (`AX:116-123`). For a growing law the axioms do not select one at all (`vR19-10`, `TESTS:7878`).

### 2.2 Implications, clause by clause

| Listed clause | Does (Σ) imply it? | Label and reason |
|---|---|---|
| **(S)**: C = E₀[H], "the lowest state weighs nothing" (`TESTS:6015`) | **Yes** | **Proved (definitional).** The one-point part s₀ = −e₀ḡ + W₀h is subtracted. One caveat: e₀ equals E₀[H]/V only when 𝔗^{00} integrates to H. For gravity's own stress that holds at weight 1 (c = 1 in every gauge; `vR19-3`, `TESTS:7535-7540`, conditional). With another composite, (Σ) still makes the lowest state weigh nothing *in that composite* |
| **(S\*)**: no contribution in any uniform static background (`TESTS:7999-8000`) | **Yes** | **Proved (definitional).** This is s₀(ḡ) to all orders in ḡ. Its Hessian is the shear rows [ref, Lemma H; `vR19-15` item 1, `P/agents/C5_R19-15_referee_verdict.md:3`]. Note: R19-19's (S\*\*₀) is linear in h, so it implies only (S\*)'s quadratic order. The all-orders form above is needed to contain (S\*) whole |
| **(S\*\*₀)** (`rR19-19:23`) | **Yes** | **Proved** (linearization in h, with Z = 0). That all six rows depend only on T₂ is R19-19's Lemma R [worker] |
| **(d-i)**: the vacuum enthalpy is exchanged with site creation (`vR17-11`, `TESTS:6590-6600`) | **No.** (Σ) implies only (d-i)'s lowest-state *effect*, removing W₀h | **Proved by countermodel.** (i) A static C-box with (Σ) and no receiver: (d-i) is not posed, and nothing is inconsistent. (ii) (Σ) leaves the non-lowest-state ΔW·h, which (d-i) absorbs (§4, item 3). (d-i) is a receiver, a statement about where the stress goes. (Σ) is a statement about what gravitates |
| **(S_ad)** on V1, local form (P-r1917a, `rR19-17:180`) | **Yes, if** the derivative expansion built from the static lowest state's response equals R19-17's adiabatic order-2 T_ad | **Suggested.** Both are the derivative expansion of the same effective action. R19-17 [worker] finds that (S_ad) contains (S\*) at order 0 and the induced-G subtraction at order 2 (`rR19-17:42,167-169`). So the registered slot "(d-i) or (S_ad)" is met on V1 only, and only at the suggested level |
| **N_red**: the source is T_m − (V − e₀)g plus gravity's own stress (`vR18-6`, `TESTS:6969-6977`) | **Only its vacuum term** | **Proved by countermodel (§2.3, D2).** The self-stress term, completion N (β = 1), is not a vacuum statement. N_red's exclusion of the receiver is the carrier's bookkeeping (D3) |
| **W1-weight** (`TESTS:7570`) | **Only its lowest-state job,** the J2 zero point, and only if the subtraction uses the same composite and gauge | **Proved by countermodel (§2.3, D1).** By Lemma L, a weight w ≠ 1 makes averages gauge-dependent in *every* homogeneous state [ref, `vR19-6`, `TESTS:7665`]. (Σ) speaks only of the lowest state |

### 2.3 Independence demonstrations (the IRREDUCIBLE clause)

**D1. W1-weight and (S\*) are logically independent** (proved by the two models below; the models' own status is as cited).
- **W1-weight ∧ ¬(S\*): the refereed C-box-E bridge with the weight clause.** "(S), (d-i), N_red, and the weight clause cannot change A = μ_E − μ_T2" [ref; `P/agents/C5_R19-15_referee_verdict.md:5`; `TESTS:8129`]. A = 3.496e-19 per cell at SM masses (`P/agents/C5_R19-15_referee_verdict.md:16`).
- **(S\*) ∧ ¬W1-weight: set A's E1 + N_c at insertion weight a = 4 in harmonic gauge, with (S).**
  - The law is CONSTRUCTED in its weak-field static/quasi-static scope [ref; `TESTS:7020-7027`]. (S) is S26's option-A Λ clause (`P/agents/C5_S26_synthesis.md:455`).
  - Set A's matter vacuum is the continuum's, with a Lorentz-invariant regulator. After (S), its uniform-strain response is zero. Two supports:
    - comparator: μ = 0 by Lorentz invariance (`rR19-15` §3.3);
    - checked: with the Lorentz group plus the Ward identity, the allowed degree-0 response kernels number 0 (`S/r1920_count.out:8`).
  - So (S\*) holds. a = 4 ≠ 2, so W1-weight fails: "W1 replaces R18-7's registered a = 4 law instead of staying consistent with it" [ref; `TESTS:7663`; `P/agents/C5_R19-6_referee_verdict.md:15`].
- **Reason.** W1-weight constrains the weight of the gravitating density, and Lemma L makes that bite in every homogeneous state, including record noise and graviton excitations. (S\*) constrains only the lowest state's uniform-strain response. Neither sentence mentions the other's object.
- **A second instance of (S\*) ∧ ¬W1-weight** (reading). Inside C-box, take the harmonic-gauge Landau–Lifshitz composite (c = 2) with its own lowest-state value subtracted (`TESTS:7537`). The lowest state then weighs nothing in every term, but excited homogeneous states are gauge-dependent.

**D2. Completion N (gravity's own stress gravitates; inside N_red, and stated inside W1-weight's wording) and (S\*) are logically independent.**
- **N ∧ ¬(S\*):** the same C-box-E bridge [ref; `TESTS:6969-6977`; `TESTS:8129`].
- **(S) ∧ (S\*) ∧ ¬N:** R16-14's literal linear completions L0 and L1/2, in set A with (S). They give β = 0 or ½, which Mercury excludes; observation excludes them, not logic [ref; `TESTS:6000-6006`]. The continuum vacuum supplies (S\*), as in D1.
- **Reason.** N fixes the metric's nonlinear response to any source (β). (S\*) fixes which vacuum stress enters at all.

**D3 (reading; arena-dependent). The carrier is independent of (Σ).**
- **(Σ) without a carrier:** a static C-box.
- **(d-i) without (S\*):** the refereed bridge (above).
- **Why a carrier is a separate clause.** (Σ) removes a piece that is not separately conserved once the lattice frame expands: ∇(W₀h) ∝ W₀θ ≠ 0. Bianchi then needs something to carry it.
  - In C-box-E the carrier is the receiver of (d-i) [ref, `TESTS:6590-6600`].
  - On V1 it is the lattice frame. R19-17's Corollary B [worker]: ∇T_grav = F_I∇X^I, so Bianchi holds iff F_I = 0. The frame law (W or A) is new completion data (`rR19-17:122-135,149-162`).

**Minimal clause set (reading, from D1–D3).** Three mutually independent clauses, with zero numbers:
- **(Σ);**
- **W1-weight, with gravity's own stress.** This is W1-weight as worded at `TESTS:7570`, which already says how gravity's own stress enters.
- **A carrier.**

This replaces the five to six listed clauses. Count once with R19-19 §3.7's "three clauses for the lowest state" (`rR19-19` §3.7).

### 2.4 What (Σ) imposes, counted (checked; independent of R19-19's code)

`S/r1920_count.py` → `S/r1920_count.out`. My own construction:
- Kernels Π^{μνρσ}(p) = C + D·pp, with the symmetries (μν), (ρσ), (μν)↔(ρσ) and (αβ), invariant under O_h × T (generators: 90° rotations about z and x, inversion, time reversal).
- The one-point part is a symmetric 2-tensor.
- The Ward identity is p_μΠ^{μνρσ}(p) ≡ 0, imposed by symmetrizing over the three contracted momentum slots.
- The rows are defined as in `rR19-19` §1: Ξ(n, e) = e·(∂_{ω²} + ∂_{q²})Π·e, and μ = e·Π(0)·e.

| Quantity | O_h × T (the grid) | Lorentz (the continuum) |
|---|---|---|
| One-point tensors | 2 (e₀, W₀) | 1 (Λ) |
| Degree-0 response kernels | 6 | 2 |
| Degree-2 response kernels | 26 | 4 |
| Ward-exact, degree 0 | 0 | 0 |
| Ward-exact, degree 2 | 2 | 1 (Einstein–Hilbert; its rows are 0) |
| Image of the Ward-exact kernels in the six rows (Ξ_Eg, Ξ_T2g, face1, face2, μ_E, μ_T2) | the line (1, 1, 1, 1, 0, 0) | 0 |
| Spatial-only Ward: allowed kernels; image | 8 at degree 2, 1 at degree 0; rank 2, a span equal to R19-19's {(1,1,1,1,0,0), (1,0,¾,0,0,0)} (I checked the span by hand from `S/r1920_count.out:11-14`) | — |

This reproduces R19-19's Lemma G (`rR19-19` §3.2) and the 26 + 6 count of its Lemma E, by an independent construction (checked).

**So (Σ) fixes 34 local numbers.** The conditions are ordered with the one-point part set to zero first, so the Ward identity on the response is homogeneous (`S/r1920_count.out:2,5-9`):
- **30** are the linearized-diffeomorphism Ward identity on the response (32 response kernels, of which 2 are Ward-exact).
- **2** are Lorentz conditions: W₀ = 0 at one point, and the isotropic graviton speed, i.e. the second Ward-exact kernel.
- **1** is Λ = 0 for the lowest state, which is (S).
- **1** is the Z convention.

A Lorentz- and diffeomorphism-invariant continuum vacuum has only the last two as free data (Λ, Z); the other 32 come from its symmetry (checked count; comparator for "the continuum gets them free"). On the six cone rows: 5 are Ward conditions and 1 is Lorentz (checked).

### 2.5 The strongest single sentence, and why it is not a reduction

**C_GR:** "The metric obeys Einstein's equations, with G supplied and no cosmological term, sourced gauge-independently by the stress of the actual state minus that of the law's (adiabatic) lowest state."

**It implies every listed clause** (reading, with the steps labelled):
- (S), (S\*) and (S\*\*): by subtracting the lowest state.
- (S_ad) on V1: through "adiabatic" (suggested).
- N: Einstein's equations carry gravity's own stress (the Landau–Lifshitz identity; comparator).
- W1-weight: from "gauge-independently", by Lemma L, within the contravariant power-density family [ref, `vR19-6`].
- A carrier: Bianchi requires one, though not specifically (d-i).

**Two catches.**
- **Locality.** Subtracting the whole lowest-state response is non-local for massless loops (P-R19-15b, `rR19-15:304`). The local version of C_GR is "Einstein's equations through two derivatives", which is (Σ) plus N plus W1-weight.
- **It is not a reduction.** By D1 and D2, C_GR is the conjunction of independent parts. It is the answer to question (i), not a reduction of the list.

---

## 3. (i) Is the clause imposing relativity at the source? Yes, by construction, with three limits

**Reading, supported by §2.4 (checked) and by refereed precedents.**
- **What (Σ) is.** For the lowest state, through two derivatives, (Σ) states that the vacuum's gravitating response equals that of a Lorentz- and diffeomorphism-invariant vacuum with Λ = 0. That is GR's vacuum, imposed.
- **What it adds beyond the continuum.** Its only content beyond what GR + SM with a Lorentz-invariant regulator must also fix is Λ = 0 for the lowest state, i.e. (S). The rest (32 of 34) duplicates symmetry the continuum has automatically.
- **A sharpening (checked; R19-19 Lemma G reproduced).** Most of what is imposed is gauge invariance rather than Lorentz invariance proper: 30 Ward conditions against 2 Lorentz conditions. Free local lattice matter does not supply the Ward part in any class tested: W15 is DERIVED for free finite-band local analytic matter (`P/agents/C5_S26_synthesis.md:275`). Whether the five Ward-violating cone rows are physical is R19-23's question (`TESTS:8221-8250`; count once).
- **Precedents, counted once.**
  - **C4 V3:** R₀ "imposes μ = 0 as a renormalization condition", and extended to the exact interacting strained energy it is "explicitly tautological" [ref; `P/agents/C4_V3_referee.md:29`].
  - **vR19-15:** (S\*) is "a stipulated renormalization/source definition, not a derived Ward mechanism" [ref; `TESTS:8131`; `P/agents/C5_R19-15_referee_verdict.md:14,18`].
  - **R19-19, Lemma E [worker]:** at O(p²), (S\*\*) "cannot fail a cone observation".
  - **vR17-3:** (S) is "genuine, consistent, number-free", and unforced [ref; `TESTS:6015-6016`]. (Σ) is the same logical type as (S) (number-free; radiatively exact by construction, `rR19-19` §3.5).
  - **Lemma PT / vR16-6:** a stipulated c-number is a counterterm [ref; `TESTS:2985-2988`; `TESTS:5576-5581`]. vR17-3 exempted (S) because it tracks radiative shifts by definition. (Σ) inherits that exemption on the same grounds (reading).
- **N and W1-weight are GR's structure.** They are, respectively, its self-coupling (β = 1) and the covariant source density. The graviton itself is supplied (P-N1; `P/agents/C5_S26_synthesis.md:262`). So, with the three clauses and P-N1, **the gravity sector is GR by stipulation**. The grid derives none of it.
- **Limits of "exactly GR's":**
  - **(L1) Lowest state only.** Any other state keeps its unsubtracted lattice response (§4, items 2 and 3).
  - **(L2) Through two derivatives only.** The O(p⁴) remainder is Lorentz-violating (§4, item 1).
  - **(L3) Linear order only.** The nonlinear completion and Bianchi beyond linear order are not established [ref; `TESTS:8132`]. The linear Ward defect moves from O(p) to O(p⁵), and is not removed [worker; `rR19-19` §3.3].

---

## 4. (b) What the grid still predicts beyond GR + SM with a Lorentz-invariant regulator, at a = ℓ_P

Units: one per cell = 1/ℓ_P⁴ ≈ 8.8e122 ρ_Λ (`rR19-17:8` convention). Here ρ_rad(T = 160 GeV) ≈ 2.3e10 GeV⁴ ≈ 1e57 ρ_Λ, and H(160 GeV) ≈ 4e-14 GeV (comparators, RECALLED standard radiation era; my arithmetic).

| # | Observable | Grid + clauses | GR + SM (LI) | Size | Bound / comparator | Status |
|---|---|---|---|---|---|---|
| 1 | O(q⁴) graviton dispersion, lowest state | ω² = q²[1 + α(qa)²], α = 16πc₄ | no LV term | One NN scalar (m = 0.3): α = 1.7e-3, \|δc/c\| ≈ 1e-84 at 100 Hz, E_QG,2 ≈ 3e20 GeV. SM envelope: α ≈ 5, \|δc/c\| ≤ 3e-81, E_QG,2 ≥ 5e18 GeV | GW170817: −3e-15 ≤ δc/c ≤ 7e-16; Fermi-LAT-type E_QG,2 ≳ 1e11 GeV (RECALLED) | [worker] R19-19, checked for one species (`SP/R19-19/r1919_bounds.out`); envelope suggested. **Unobservable by ≥ 66 decades.** The LI O(q⁴) terms (curvature²) are common to both theories |
| 2 | Shear mismatch in any non-lowest state (state-tied subtraction) | Pre-electroweak-crossover Δμ = −4.70e-19 and −1.20e-19 per cell on R19-11's root edges: tachyonic in both channels. Twisted mass: Δμ_E ≈ −4.4e-36 | none | \|m_g\| ≈ 6e10 GeV (\|m_g\|/H ~ 1e24), or ≈ 180 GeV with twisted mass (\|m_g\|/H ~ 4e15) | A tachyon with rate ≫ H is catastrophic | [worker] R19-19 §3.6, from refereed R19-11 residuals (`TESTS:7986-7994`). Conditional on the canonical-mass reading (vR19-11 item 4) and on R19-23. **R19-21 tests it (`TESTS:8144-8173`); count once.** The largest grid-specific item, and it reads as a hazard, not a prediction |
| 3 | Enthalpy mismatch in any non-lowest state (one-point) | ΔW = Δ(ρ + p) of the lattice vacuum when masses change | none. With an LI regulator W ≡ 0 for every vacuum | Illustration on naive Wilson r = 1 (not D1): dp/dm = 0 exactly at m = 0 and dρ/dm = −2⟨R/ε₀⟩ = −1.767 per 4-component field. Top quark alone: \|ΔW\| ~ 7.5e-17 per cell ~ 7e106 ρ_Λ. With a chirally good edge, O(m²a²): ~1e89 ρ_Λ (suggested) | ρ_rad(T_EW) ~ 1e57 ρ_Λ | **Prior art (count once):** R17-11 already found that W(T) changes across crossovers are Planckian without exchange, and that (d-i) absorbs any W(x,t) "exactly at all times" [worker `rR17-11:186,259`; central result [ref] `TESTS:6590-6600`]. **New here:** (1) on Wilson-type edges the change is linear in m and pressureless (dp/dm = 0; checked as an illustration: `S/r1920_wilson_dW.out`; the root-edge value is not computed, and D1 is smaller because it is exact continuum inside its box); (2) (S\*), (S\*\*) and (S_ad) do not absorb it, because they are tied to the lowest state (proved for (S\*)/(S\*\*) by definition; suggested for (S_ad)). So on V1, where (d-i) cannot be posed (`TESTS:7893-7902`), it is unaddressed. Its Lorentz-invariant half is a Planckian Higgs tadpole: a matter-sector tuning missing from the bill (suggested) |
| 4 | Site-creation injection (C-box-E only) | a standing H-tracking excess ρ_ins ≥ 5.5e59/Γ ρ_Λ | none | ≥ 1e59 ρ_Λ for Γ ≤ 1/t_P | ρ_Λ | Conditional (vR19-10 OPEN: not universal, `TESTS:7873-7879`). R19-13 NO-LOCAL-ESCAPE for the NN scalar: R > 256a (`TESTS:8111-8118`). Under (Σ) these excitations gravitate. V1 avoids this, at P-r1914c's price (no lattice-native scale) |
| 5 | W7 boundary anomaly | far-field √(E² − P²) is frame-dependent for bodies carrying edge quanta | Poincaré-exact | lab ≤ 3e-30 [worker, R18-12]; thermally tiny below about 1e18 GeV under stated assumptions | — | [ref] ANOMALY (`TESTS:7095-7103`). The population is set by history, and is zero under P142 |
| 6 | Planck-mass relics | stable corner states: charged doublers, or corner photons at 2–2√3 /a | none | Y ≤ 3.76e-28 (doubler) or 1.79e-29 (corner photon) | Ωh² ≤ 0.12 | [ref] BOUNDED (`TESTS:7492-7504`). Abundance not predicted: exponentially small for T_RH ≪ 1/a [worker; the T_RH brackets are not confirmed] |
| 7 | Matter LV (charge block) | 4 tunings per class, 10 per species, 2 q²-correlated | none needed | tuned to zero at about 1e-16 precision | photon decay, vacuum Cherenkov (RECALLED) | [ref] vR19-12 (`TESTS:8099-8110`). **Inputs, not predictions.** Radiative stability is not covered. On the root's box edges, matter dispersion is exact continuum below the box edge (R19-11 Lemma B, `rR19-11:30`; vR19-11 `TESTS:7989`), so there is no O((pa)²) matter LV at accessible energies (reading) |
| 8 | Matter's own graviton-loop speed | c_m² − 1 = 4κm²J₂ (prescription dD-M) | the same structure | ~(m/M_P)² ≲ 1e-34 | — | [worker] R19-19 §3.2, reading; negligible |
| 9 | M_t(pole) ≤ 170.88 GeV, or new content below about 1e11 GeV | from (S) ⊂ (Σ) | **the same, if the continuum theory adopts (S)** | tension 1.48–3.09σ | measured M_t (RECALLED) | [ref] vR18-2 OPEN (`TESTS:6806-6813`). **Not grid-specific** |
| 10 | Late acceleration is content above e₀ (Λ̃_late ≥ 0, = 0 under P93) | from (S) | the same with (S) | — | DESI (RECALLED) | [ref] vR17-7 (`TESTS:6297-6309`). **Not grid-specific** |
| 11 | E1/E2 record noise, sirens | **not present on the grid**; set A (option A, continuum base) only | — | E2: d_L^GW/d_L^EM − 1 ≤ 0.44–1.30% at z = 1 near the drag ceiling | ET forecast (RECALLED) | [worker] R19-18; [ref] R18-11 and R19-2 OPEN. A set-A property, not a grid prediction |

**What is not on the list, and why.**
- **G.** (Σ) with Z = 0 removes the induced G, and R19-17 finds that (S_ad) must do so [worker]. So G is supplied (`AX:189-190`); it is not predicted.
- **β = γ = 1.** This is GR, through N.
- **The graviton.** It is supplied (P-N1).

**Answer to (ii).** For today's vacuum the grid adds nothing observable: item 1 is about 1e-84.
- Items 2–4 are effects of the grid where the clauses cannot reach. On the computed numbers they are threats (a tachyonic shear and an enormous pressure in non-lowest states; a creation excess in C-box-E), not confirmations.
- Items 5 and 6 depend on history and are bounded.
- Item 7 is a cost, not a prediction.
- Items 9 and 10 are (S)'s, and a continuum theory shares them.

---

## 5. (c) The minimal honest statement for the owner (reading)

> The grid does not predict gravity. To reproduce what we observe, we add three rules:
> 1. the law's lowest state gravitates only as a relativistic vacuum with zero cosmological constant, up to two derivatives;
> 2. the gravitating source is the weight-1 stress, including gravity's own;
> 3. the lattice (site creation, or its own motion) absorbs what rule 1 removes.
>
> With a supplied graviton, these rules make gravity Einstein's by construction. Rule 1 alone sets 34 numbers of the lattice vacuum. 32 of them are what Lorentz and gauge symmetry give a continuum theory for free. One is Λ = 0, which is new physics and a genuine claim, but it is not specific to the grid. The last is a convention for G.
>
> What the grid adds beyond Einstein plus the Standard Model:
> - for today's vacuum, nothing measurable (about 1e-84 in graviton speed);
> - for any earlier epoch with different particle masses, a large unsubtracted lattice effect. On the current numbers it is a tachyonic graviton mass of about 6e10 GeV before the electroweak crossover, plus a pressure term (up to about 1e106 times today's dark-energy density, estimated) that only site creation absorbs. That is a likely conflict, and R19-21 tests it.
> - history-dependent Planck relics and a far-field anomaly, both bounded.
>
> The matter side costs 4 tuned numbers per charge class.
>
> The only sharp test the source rules make (the top-quark mass at or below 170.9 GeV, or new particles) comes from rule 1's Λ = 0 part, and holds equally without a grid.

---

## 6. Prices and bill (named, none adopted; counted once)

- **No new price.**
  - (Σ) is P-R19-19a extended from linear order to all orders in uniform h. It contains P-R19-15a (S\*) and P92 (S). It is P-r1917a on V1 (suggested).
  - W1-weight is R19-6's merged P145 + P-r193a. N is P135's self-stress part.
  - The carrier is P70(d-i) with P52 (C-box-E), or P-r1917c (V1).
- **Bill (reading, count once with R19-19 §3.7).**
  - Gravity block: 0 numbers and 3 clauses.
  - Charge block: 4 per class, 10 per species [ref, vR19-12].
  - CC: 0 numbers by (S).
  - Not on the bill: the supplied graviton (P-N1), and the non-lowest-state items 2–3 (a possible conflict, not a count). Item 3's Higgs-tadpole tuning on Wilson-type edges is not in any bill (suggested).
- **Axiom lines touched, as before.**
  - Source/action identification: `AX:187`, and `AX:140-146`, which require a separate authority.
  - "A law privileges no states" (`AX:94`), through "the lowest state". Count once with S26 Q1(ii).
  - No Hamiltonian, energy or ground state is supplied (`AX:116-123`).
  - The scale primitive for G (`AX:189-190`).
  - Qualification: an unfixed choice remains a named conditional (`AX:87-90`).

## 7. Prior art (each counted once)

- **R16-6 / Lemma PT:** a c-number subtraction is a counterterm (`TESTS:2985-2988,5576-5581`).
- **R17-3:** (S) is number-free and unforced (`TESTS:6007-6016`).
- **R17-7:** conditions on (S) (`TESTS:6297-6309`).
- **R17-11:** (d-i) CONSISTENT in 𝒟 (`TESTS:6590-6600`).
- **R18-6:** literal N conflicts with (d-i); N_red is a new completion (`TESTS:6969-6977`).
- **R18-7:** a = 4 CONSTRUCTED in scope (`TESTS:7020-7027`).
- **R19-3:** J2-GAUGE-BRIDGE (`TESTS:7535-7540`).
- **R19-6:** OPEN; Lemma L confirmed; a = 4 replaced (`TESTS:7663-7672`).
- **R19-10:** OPEN, conditional injection (`TESTS:7873-7879`).
- **R19-11:** residuals (`TESTS:7986-7994`).
- **R19-13:** NO-LOCAL-ESCAPE (`TESTS:8111-8118`).
- **R19-14 [worker]:** (S_ad), V1 (`TESTS:7893-7902`).
- **R19-15:** STRUCTURAL-ZERO by stipulation (`TESTS:8127-8132`).
- **R19-17 [worker]:** local (S_ad), Lemma N (`rR19-17`).
- **R19-19 [worker]:** (S\*\*₀), Lemmas R, G and E, the O(q⁴) bounds, §3.6 (`rR19-19`).
- **SUMMARY §17:** the root obstruction (lattice momentum generates central differences, not translations), which lies behind W15. That it is also the cause of the five Ward rows is a reading.
- **C4 V3:** the tautology precedent (`P/agents/C4_V3_referee.md:29`).
- **S26 §§1, 2, 4.**
- **PRICE_NOTE:** P0 and its "TT twin of the CC problem" caveat.
- **Overlap with running items:**
  - **R19-21:** history; items 2–3 here. I suggest it add the one-point ΔW of item 3, not only the shear.
  - **R19-23:** whether the Ward rows are physical.

  Neither is duplicated here.

## 8. Strong-word check and scope

- **"Proved":**
  - the implication table's definitional entries;
  - the countermodel logic of D1 and D2 (the models' status is as cited: refereed, or refereed in scope);
  - dp/dm = 0 at m = 0 for any law whose ε(k; ℓ, m) has the form √(S/ℓ² + (m + R/ℓ)²): ∂ε/∂m at m = 0 is ℓ-independent.
- **"Checked":**
  - the kernel counts and the Ward images (`S/r1920_count.out`);
  - the naive-Wilson illustration (`S/r1920_wilson_dW.out`).
- **"Logically independent"** means that each of the two combinations has an explicit model. It does not mean both models are viable: R16-14's model is excluded by Mercury.
- **"Imposing GR"** holds for the lowest state, through two derivatives, at linear order (L1–L3).
- **"Exactly"** is used only for the counts.
- **Not established:**
  - (Σ) ⇒ (S_ad) (suggested);
  - item 3's root-edge magnitude;
  - that (d-i) absorbs a time-dependent ΔW rests on R17-11's "any W(x,t)" (`rR17-11:186,218`; worker statement, central result refereed);
  - the sign conventions of item 2, which come from R19-19 [worker].
- **Machine use.** Each run took under 15 s with `OMP_NUM_THREADS=2`.

## 9. For the referee

1. Is IRREDUCIBLE met by D1 and D2, given that ONE-CLAUSE is met only by the conjunction C_GR (the registration collision, §0)?
2. Is the (S\*) ∧ ¬W1-weight model admissible? It is set A at a = 4 with (S), with the continuum vacuum supplying (S\*).
3. The count 34 = 30 Ward + 2 Lorentz + Λ + Z (§2.4), and its reading that (Σ) duplicates the continuum's symmetry except for (S).
4. Item 3, the one-point enthalpy mismatch: does it belong with R19-21?

## 10. Files (`S/`)

- `r1920_count.py` / `.out`: invariant-kernel counts (O_h × T and Lorentz), the Ward-exact spaces, and the images in the six rows.
- `r1920_wilson_dW.py` / `.out`: the naive-Wilson linear-in-m vacuum enthalpy (an illustration, not the root edge).
- `R19-20_report.md`: this report.
