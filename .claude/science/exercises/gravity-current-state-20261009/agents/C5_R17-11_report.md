# C5 R17-11 report: the E₀ principle's pressure residual. Is bridge (d-i) consistent, covariant and non-signalling?

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-13, 01:11Z to 01:37Z. No repository file was edited.

**Scratch folder.** `S/` = `.../scratchpad/C5/R17-11/`. Every script runs in under 5 s at `OMP_NUM_THREADS=2`.
- `S/scripts/r1711_lemmaV_general.py/.out` (sympy, nonlinear, spherical, inhomogeneous): generalized Lemma V, the exchange current Q, and the (S) identity.
- `S/scripts/r1711_linear_signal.py/.out` (sympy, linear about FRW): dust plus a tilted lattice slicing plus the E-sector plus the grid vacuum with arbitrary W(t,x). It includes the Lemma S test and a no-exchange contrast.
- `S/scripts/r1711_absorb_class.py/.out` (sympy and arithmetic): which stresses the E-sector can absorb under (S); ultralocal Lagrangian alternatives; sizes.
- `S/scripts/r1711_unimodular_fork.py/.out` (sympy): can a unimodular Λ(x) receiver absorb Q instead?
- `S/recheck/`: the R17-7, R15-1 and R11-3 runners, copied and rerun (`S/recheck/run_all.log`). **All 19 reproduce their stored outputs.** The only differences are a "runtime" line in `r113_tadpoles.out`, and the scratch path printed inside two RuntimeWarnings (`r151_dispersion`, `r151_window`), whose stored `.out` include stderr. `r177_enthalpy_orders` needs `PYTHONPATH=recheck/R11-3`; with it, the output is identical.

**Read.**
- In full:
  - `docs/MINIMAL_AXIOMS_2026-06-29.md` (`AX`);
  - the C5 method (`TESTS:2302-2320`), the round-17 rules (`TESTS:5688-5708`) and the item (`TESTS:6230-6250`);
  - `C5_R17-7_report.md` (`R177`) and its referee verdict, which appeared during this run (`scratchpad/C5/ref_R17-7/REFEREE_VERDICT.md`, `vR17-7`: CONFIRMED WITH CORRECTIONS, OPEN);
  - `C5_R15-1_report.md` (`R151`) and `C5_R15-1_referee_verdict.md` (`vR15-1`);
  - `C5_R14-5_report.md` (`R145`) and `C5_R14-5_referee_verdict.md` (`vR14-5`);
  - `C5_R11-3_referee_verdict.md` (`vR11-3`).
- In part:
  - `C5_R11-3_report.md:90-250` (`R113`);
  - `C5_R13-3_report.md:195-225` (`R133`; Lemma G′) and `C5_R13-3_referee_verdict.md:1-12` (`vR13-3`);
  - `C5_R17-4_report.md:197-215` (the LV tadpole);
  - `C5_R13-8_report.md:191` (bill row 8);
  - `C5_R4-4_report.md:138-218` (Lemma K and the compensator Lemma C), with `vR4-4:5,11`;
  - `C5_S20_synthesis.md:350-357` (P70);
  - the Λ-lane entries in `TESTS` (R11-3 `4157-4188, 4417-4424`; R13-3 `4721-4729`; R14-5 `4876-4914`; R15-1 `4924-5006, 5164-5176`; R16-6 `5225-5245, 5477-5491, 5576-5581`; R17-3 `5786-5812, 5907-5920, 6007-6016`; R17-7 `6018-6047, 6129-6141`; R17-4 verdict `6171-6178`).

**Labels.** proved / checked (sympy or numerics this run) / suggested / reading / comparator. Literature I did not fetch is marked RECALLED. Nothing was downloaded.

**Units and subtraction rule (named before the runs).**
- κ = 1 in the scripts.
- The grid vacuum is at rest in the site frame n: T_v = V nn + p_v h = −V g + W h, where **W := ρ_v + p_v (the enthalpy)** and V := ρ_v.
- (S): λ = −κe₀, a law constant (`R177:31,253`). Λ̃ := λ + κV.
- "Absorbed" means: absent from every component of G_μν − κT^m_μν. Nothing else is subtracted.
- The signalling observable is R15-1's: the jump of the gauge-invariant comoving density rate δ̇ after a local impulse, minus the GR (g = 0) response (`R151:29-31`).

---

## 0. Verdict against the FIXED readings (`TESTS:6246-6249`)

**Worker reading: CONSISTENT, in a stated class.** The reading itself needs no referee. The fork exclusions F1, F2 and F4 (§4(a)) are no-go statements and need the referee before they are recorded. Notes for a referee are in §6.

**The class 𝒟 (stated before the title, §2).**
- R14-5/R15-1's E-sector: E_ni = 0, E^TL = 0 and E_nn = λ imposed in the lattice frame; the spatial trace is not imposed (√h fixed per site, `R145:94-98`).
- Sites ride the slice normals (`R145:167`).
- (S), so λ = −κe₀ is constant.
- A grid vacuum with any C¹ local enthalpy W(x,t) and energy V(x,t). The vacuum energy V is exchanged with matter only covariantly: ∇·(T_m − Vg) = 0.
- One-point (mean) stress only.

**What is shown in 𝒟.**
- **(a) Covariant form (proved; checked).**
  - The exchange current is **Q_ν = ∇^μ(W h_μν) = D_νW + W a_ν + Wθ n_ν**, received by E: ∇^μE_μν = −κQ_ν.
  - Its energy leg is Wθ: creation at fixed density pays W per unit of new volume. Its momentum leg is D_iW + W a_i: the gradient, plus holding the hovering vacuum up (`r1711_lemmaV_general.out:3-5`).
  - Under (S), Bianchi forces p_E = −λ − κW and **E + κT_v = −(λ + κV)g in all 16 components, for any W(x,t), N, A, B** (`:6-8`).
  - The field equations are then G_μν + Λ_* g_μν = κ(T^m_μν − V g_μν), with Λ_* = −κe₀. The site frame n is absent from them.
  - Q is unique in 𝒟: the only site-frame stresses E can absorb under (S) are pure isotropic pressures s(x,t)h_μν (`r1711_absorb_class.out:1`).
- **(b) Bianchi and causality at linear order (checked).**
  - Generalized Lemma V: for any W(t,r), N(λ + p_E + κW) = g′(t) and λ̇ = −g′θ_n (`r1711_lemmaV_general.out:1-2`). W never enters λ̇. So (S) gives g′ ≡ 0 whatever W does, including through phase transitions and across bubble walls.
  - At linear order about FRW, with dust, a tilted lattice slicing T = t + ξ and W = W₀(t) + W₁(t)cos kx (`r1711_linear_signal.out:2-8`):
    - the dust equation is exactly R15-1's, δ̈ + 2Hδ̇ − ρδ/2 = ½[(3ġ′ + 6Hg′)ξ + 3g′ξ̇], **with no W₀ or W₁ term**;
    - at g′ = 0 there is no ξ in any component, including the 0x momentum constraint.
  - The Lemma S jump is Δδ̇ = F·D/(D − 3g′/2) → F (`:13`). **There is no instantaneous channel, and no new one.**
- **(c) Predictions.** (d-i) adds no observable of its own in 𝒟. The vacuum's frame-tied enthalpy, its inertia and the lattice frame all drop out of gravity. There is no vacuum–matter-flow coupling: Q has no matter leg, and nothing accumulates in λ, unlike unimodular diffusion. The observable content is (S)'s alone (`vR17-7:74`). Details in §4(c).
- **(d) Prices.** The bridge stays stipulated (P-vac′, number-free and radiatively tracking). The receiver exists only where the spatial trace equation is not imposed (V2/V3 plus site creation). The site congruence must be hypersurface-orthogonal with θ_s ≥ 0. The partner is non-Lagrangian. **Bill:** in 𝒟, R17-4's LV-tadpole row (P-Tad, a stipulated trace counterterm) is paid by P-vac′ with 0 numbers. It is the same quantity as P70's uniform part, so it is counted once.

**Why CONSISTENT and not OPEN.** The FIXED clause asks for "a covariant, non-signalling (d-i) that absorbs the pressure exactly, checked at linear order" (`TESTS:6247`). 𝒟 gives it:
- exact absorption, as an identity;
- non-signalling, since g′ ≡ 0 and the Lemma S coefficient is 0;
- covariant on shell;
- checked nonlinearly in spherical symmetry and linearly with a tilted slicing.

Not shown, and not claimed:
- that the bridge is forced by the axioms;
- that (d-i) holds outside 𝒟: V1, V3, a vortical site flow, the anisotropic or fluctuating vacuum stress.

**Against the expectation (SIGNALS, `TESTS:6250`).**
- **The expectation fails.** The CMC/g ≠ 0 pattern comes from absorbing *energy density*. λ̇ = −g′θ_n (Lemma C, `vR14-5:7-25`) needs λ̇ ≠ 0. The enthalpy W h carries **zero site-frame energy density**, so it enters only the unimposed spatial trace (p_E) and E's Euler equation. It never touches λ (`r1711_lemmaV_general.out:2`).
- "Unless the pressure residual is itself constant, in which case (d-i) may be trivial": partly right. (d-i) is "trivial" in having no dynamics and no observable. That holds for **any** local W(x,t), not only a constant one.

**Changed hypothesis relative to the governing prior result (`vR15-1:15`).**
- vR15-1 confirmed Lemma V for a constant uniform vacuum, with (d-i) requiring "the source bridge changed to permit energy and momentum exchange". vR17-7 confirmed invisibility "in Lemma V's homogeneous source equations" (`vR17-7:23`).
- Here the separate vacuum conservation is removed, as the item registers, and the vacuum is made inhomogeneous and time-dependent, with linear k ≠ 0 perturbations.

---

## 1. In plain words

- **The problem.** The grid's lowest state pushes outward (pressure) differently from how it weighs (energy). The rule "the lowest state weighs nothing" cancels the weight, but one number cannot also cancel a different pressure.
- **The proposed way out, (d-i).** The vacuum is allowed to trade energy and momentum with the part of the theory that makes new grid sites.
- **What I found.**
  - On this grid, space grows by adding sites, not by stretching them. The vacuum's pressure is the push it would exert if a site were stretched, and no site ever is. So that pressure has nothing physical to act on.
  - The one equation it could act on, the "stretching" equation, is exactly the one this model does not impose. The site-making sector simply pays for it: when a new site appears, it supplies the small mismatch between the vacuum energy the site needs and the work the vacuum's pressure would have done.
  - In a gravitational well the grid's sites stand still rather than fall, so something must hold the vacuum up. The same sector does that too.
- **Does this send faster-than-light signals?** No. The earlier faster-than-light problem came from soaking up *changes in vacuum energy*. That needs a slice-wide clock that reacts instantly. Pressure carries no energy in the grid's own frame, so soaking it up never needs that clock. With "the lowest state weighs nothing" in place, the equations are exactly ordinary general relativity with one fixed constant. I checked this for a lumpy universe and for small ripples on an expanding one.
- **What it predicts.** Nothing new by itself. The grid vacuum's pressure, its inertia, and the grid's own rest frame become completely invisible to gravity. The vacuum does not push on or drag moving matter. Its handover to the site-making sector does not build up into a slowly changing cosmological constant.
- **What it costs.**
  - It is still a choice about how matter sources gravity, not something the four axioms force.
  - It only works where the grid grows by adding sites.
  - The grid's sites must move without swirling.
  - The site-making sector that soaks up the pressure is not described by any ordinary action.
- **What it buys.** It removes one fine-tuned number from the graviton bill: the "Lorentz-violating tadpole", which until now needed its own counterterm.

---

## 2. Hypotheses, class and excluded alternatives (stated before titles)

- **H-imp** (`R145:94-98`). Imposed: E_ni = 0, E^TL_ij = 0 and E_nn = λ in the lattice frame. The spatial trace is not imposed, because √h is fixed per site. Here E := G − κT_tot.
- **H-site** (`R145:167`). The sites' 4-velocity is the slice normal n, so the site congruence is hypersurface-orthogonal. Proper site density is fixed, and the creation rate is c = θ_s ≥ 0 (`AX:79-80` permanence, reading).
- **H-S** (`R177:31`; `vR17-3:17`). λ = −κe₀, a law constant. This is (S) in the E-sector form. In R16-6/R17-3 language it is Theorem Z's g ≡ 0 branch.
- **H-vac.**
  - T_v = V nn + (W − V)h at rest in n.
  - V and W are C¹ local functions, of local fields, masses and phase; arbitrary otherwise.
  - Mean stress only.
  - Sign of W unrestricted. U/M vertices, Dirac sea and pairing are all covered.
- **H-m.** ∇·(T_m − Vg) = 0: covariant latent-heat exchange of the vacuum *energy* with matter fields (standard; V is a scalar function of the matter fields).
- **(d-i)** (`R151:236-238`; `vR15-1:15`): T_v has no conservation law of its own. ∇·T_v + ∂V = Q is received by E.
- **Excluded by the item:** active compensation of vacuum changes (R15-1 FAIL, `TESTS:5166-5176`).
- **Excluded from 𝒟 and not covered:**
  - V1 (spacing grows, trace imposed);
  - V3 with a fixed lapse (`vR13-3:3-12`);
  - a vortical site flow;
  - anisotropic, momentum-flux or fluctuating vacuum stress;
  - the lattice construction of creation (S1/P52/P53);
  - matter LV in the site frame (carried walls).

---

## 3. Prior art (each counted once)

1. **R15-1 and vR15-1.**
   - Lemma S (`R151:122-147`; `vR15-1:5-7`), with signalling ⇔ g ≠ 0 in the elliptic CMC constraint-fluid model.
   - Lemma V (d-i)/(d-ii) (`R151:224-245`; `vR15-1:15`), which this probe generalizes.
   - `r151_gridvac.out` D3, the energy leg "energy injected by creation".
2. **R14-5 and vR14-5.**
   - Lemma C (`vR14-5:7-25`), with g = 0 ⇒ GR (`vR14-5:70`).
   - The missing action, and the causality question (`vR14-5:84-88`).
3. **R17-7 and vR17-7.**
   - The enthalpy residual (0, ρ₀+p₀) after (S) (`R177:184-187`; `vR17-7:16-21`).
   - (d-i) is homogeneous-only and bridge-specific (`vR17-7:23`).
   - (S-T) ≠ (d-i) (`R177:211`; `vR17-7:32`).
   - A varying C(x) needs a carrier (`vR17-7:44-50`).
   - The covariant form G + Λ_*g = κT is a covariant embedding (`vR17-7:52-58`).
4. **R11-3 and vR11-3.**
   - Identity W and Corollary P (`R113:117-129`; `vR11-3:7-41`).
   - Two tadpoles in V1 (`vR11-3:45-47`).
   - Lemma BR: V2 absorbs the homogeneous pressure into f(t) (`vR11-3:51`).
   - Fixed-site V2/V3 cannot expand without creation (`vR11-3:57`).
5. **R13-3.**
   - Lemma F, the N = 1 caustic in the smooth class (`vR13-3:3-12`).
   - Lemma G′, a separately conserved grid vacuum ⇒ geodesic sites ⇒ destruction (`R133:217-221`, suggested).
6. **R17-4 / R13-8.** The LV tadpole row is "strictly positive and separately payable" by a trace counterterm c_h∫h_ii (`C5_R17-4_report.md:197-203`; `TESTS:6175`; `C5_R13-8_report.md:191`).
7. **R4-4.**
   - Lemma K: a localized non-conservation is never a gradient (`C5_R4-4_report.md:140-155`; `vR4-4:5`).
   - Lemma C: "a compensator always exists … the check has teeth only if the compensator must satisfy positivity" (`:205-218`). The referee notes the ghost claim is not derived from an action (`vR4-4:11`).
8. **S20 P70** (`C5_S20_synthesis.md:355-357`).
9. **Comparators (RECALLED):**
   - interacting vacuum with a covariant exchange Q^μ (Wands, De-Santiago and Wang 2012; Salvatelli et al. 2014; Gómez-Valent and Solà running vacuum), where Q couples the vacuum to dark matter or matter flows;
   - unimodular gravity with energy diffusion (Josset, Perez and Sudarsky 2017), where non-conservation J = ∂Λ accumulates into an observable Λ(t);
   - the cuscuton (Afshordi et al.), counted via R14-5/R15-1.
10. **Repository grep** (docs + packet; "interacting vacuum", "exchange current", "vacuum enthalpy", "Josset", "non-conservation", "(d-i)").
    - Hits beyond 1–9: K3a″/W1 interacting-vacuum TT stiffness (`WALL.md:38,97`, a different object: the anisotropic response, see §4(d)); C4_V2's interacting-vacuum reference (`C4_V2_report.md:18`, a different object); R2-3's charge-conservation analogy (`C5_R2-3_report.md:134`).
    - No prior covariant exchange current for the grid vacuum, and no inhomogeneous or linear test of (d-i), was found.

---

## 4. Results

### 4(a) A covariant form of (d-i), and which Q absorbs ρ₀+p₀ exactly

**Decomposition (proved, elementary).** T_v = V nn + p_v h = −V g + W h. The first piece is covariant. The second is frame-tied and has zero n-frame energy density.

**Exchange current (proved; checked symbolically in spherical symmetry with arbitrary N, A, B, W(t,r), `r1711_lemmaV_general.out:3-5`):**

  ∇^μT^v_μν = −∂_νV + Q_ν,  **Q_ν = ∇^μ(W h_μν) = D_νW + W a_ν + Wθ_n n_ν**, a = D ln N.

- **Energy leg:** −n^νQ_ν = Wθ_n (`:4`). At fixed proper density the vacuum created with new volume is short by W per unit volume, its "missing p dV work". There is no ∂_tW term: a time-varying W needs no energy.
- **Momentum leg:** D_iW + W a_i (`:5`). This is the force needed to keep the vacuum at rest in the site frame, which hovers in wells.

**Receiver and the (S) identity (proved; checked, `:1-2, 6-8`).**
- With H-m, Bianchi reads ∇·(E + κW h) = 0.
- So E′ := E + κW h is R14-5's Lemma-C fluid: **N(λ + p_E + κW) = g′(t), λ̇ = −g′θ_n**. This is generalized Lemma V, now with W(t,r) and V(t,r) arbitrary. The control W = 0 is R14-5 Lemma C (`:9`).
- Under (S), λ̇ = 0, so g′θ_n = 0, so **g′ ≡ 0** on every slice where θ_n ≠ 0 somewhere (expansion).
- Then p_E = −λ − κW, and **E + κT_v = −(λ + κV)g identically**, in all components.
- The gravitational equations are G + Λ_*g = κ(T_m − Vg) with Λ_* = −κe₀.
- **Exactly at all times:** this is an algebraic identity for any history W(x,t). Through phase transitions the false-vacuum energy V still gravitates (Λ̃ = κ(V − e₀) ≥ 0, `vR17-7:7-12`); only its frame-tied enthalpy is absorbed.

**Uniqueness (proved, elementary; `r1711_absorb_class.out:1`).**
- A site-frame stress S = ρ_S nn + 2q_(μn_ν) + p_S h + π can be absorbed under (S), with E_nn = λ₀ fixed, E_ni = 0 and E^TL = 0, iff ρ_S = q = π = 0.
- So **the absorbable class is exactly {s(x,t) h_μν[n]}**. The split T_v = (−Vg) + (Wh) into a gravitating and an absorbed part is unique, and Q = ∇·(Wh) is the only exchange current in 𝒟.
- Absorbing energy density instead needs λ̇ ≠ 0, i.e. g′ ≠ 0. That is R15-1's channel, counted once.

**Covariance (proved in 𝒟; reading for its meaning).**
- On shell the equations are generally covariant, and n appears in no gravitational equation.
- The input W is computed from the lattice H in the lattice frame. Like e₀, it is a "covariant embedding", not a covariant derivation (`vR17-7:58`, same status).
- Off shell, the imposed equations are frame-split (H-imp). That is the E-sector's existing structure, not new to (d-i).

**Forks: other receivers (the rule at `TESTS:5704`). Each alternative is listed, with why it is excluded.**
- **(F1) The 4D trace / unimodular Λ(x)** (R5-3 route 1).
  - It needs κQ = dΛ, so Q must be closed. Q is not closed in general: dQ_tr = W∂_t∂_r ln(N√h), which is 0.165 at a sample inhomogeneous point (`r1711_unimodular_fork.out:2-3`); compare R4-4 Lemma K.
  - In FRW Q is closed, but Λ(t) then drifts by 3κW per e-fold, ~1e123 ρ_Λ (`:4`; `r1711_absorb_class.out:7-9`).
  - **Excluded** (checked symbolically; the magnitude is arithmetic).
- **(F2) Matter or dark matter as receiver** (Q-coupled interacting vacuum). It injects Wθ ~ 3HW, ~1e123 ρ_Λ per Hubble time, into matter. **Excluded** (arithmetic; reading).
- **(F3) No receiver for the momentum leg, (d-ii).** This needs W a = 0.
  - With CMC forced (g ≠ 0) the sites hover, so W = 0 (`vR15-1:15`).
  - Under (S) the slicing is free, so geodesic sites (a = 0) look possible. But geodesic site congruences focus in bound regions: R13-3's Lemma F in the smooth N = 1 class (`vR13-3:3-12`), and Lemma G′'s site destruction against `AX:80`.
  - So **(d-ii) still needs W = 0 (pairing) under (S)** (suggested, conditional on R13-3's smooth class). This answers the free-slicing gap that vR17-7:23 leaves implicit.
- **(F4) A Lagrangian (ultralocal khronon P(X), X = 1/N²) vacuum or partner** (`r1711_absorb_class.out:2-5`):
  - a lapse-independent pressure forces W = 0 (proved);
  - zero energy density, the partner's case, forces p = C/N: the cuscuton g/N term, not a lapse-independent −W (proved);
  - a lapse-independent energy forces W = C/N with c_s = ∞, and conservation then forces θ_nW = 0 (proved).
  - **No ultralocal Lagrangian frame vacuum with fixed (V, W ≠ 0) survives expansion.** The energy leg is unavoidable, as r151_gridvac D3 already shows (counted once). So (d-i)'s partner is necessarily non-Lagrangian in this class (P-r1711c).
- **(F5) A propagating compensator** (R4-4 Lemma C). It has indefinite energy (`C5_R4-4_report.md:205-218`); the referee notes the ghost claim is not derived (`vR4-4:11`). Not needed here.
- **Not covered:** non-ultralocal khronon actions (derivative terms), discrete or lattice-scale receivers, records as a receiver.

### 4(b) Bianchi beyond homogeneity, and causality (the Lemma S test)

**Nonlinear, inhomogeneous (proved; checked).** Generalized Lemma V holds for arbitrary spherical N(t,r), A, B, W(t,r) and V(t,r) (`r1711_lemmaV_general.out:1-2`). Bianchi is consistent beyond homogeneity, and under (S) g′ ≡ 0 for every such W.

**Linear about FRW with a tilted lattice slicing (checked; `r1711_linear_signal.out`).**
- **Setting.** Dust in synchronous-comoving gauge. Lattice time T = t + ξ(t)cos kx, so the lattice lapse is N = 1 − ξ̇ cos kx, as in R15-1 (`:1`). λ(T) and g′(T) are evaluated on lattice time. W = W₀(t) + W₁(t)cos kx is arbitrary.
- **L1.** E + T_v − [−(λ(T)+V)g + (g′(T)/N)h] = 0 in all 16 components, and at g′ = 0 E + T_v = −(λ+V)g (`:2-4`). No ξ, W₀, W₁ or n appears in any component, including the 0x momentum constraint.
- **L2.** The O(ε) 00 equation is exactly **δ̈ + 2Hδ̇ − ρδ/2 = ½[(3ġ′ + 6Hg′)ξ + 3g′ξ̇]**, R15-1's equation (`R151:129`) with g → g′ (`:6`).
  - It has **no W₀ or W₁ dependence** (`:7`), and no ξ dependence at g′ = 0 (`:8`).
  - Background: ä/a = (λ+V)/3 − g′/2 − ρ/6 (`:5`), which is GR with Λ̃ at g′ = 0.
- **Lemma S test.** With the R15-1 kernel unchanged, Δδ̇ = F·D_k/(D_k − 3g′/2) (`R151:132`), which is **F** at g′ = 0 for every W and every slicing (`:13`). That is the GR control: ultralocal, no response outside the light cone.
- **Contrast, no exchange** (E conserved alone, so Bianchi fails by Q):
  - the background gets −W₀/2 (Planckian deceleration, `:9`);
  - the O(ε) equation gets −3W₁/2 (`:10`);
  - the momentum constraint gets −W₀kξ sin kx (`:15`), so the lattice tilt carries a Planckian momentum density and the frame becomes visible;
  - Q_x = εk(W₀ξ̇ − W₁) sin kx (`:11`) is the momentum leg that (d-i) hands to E.
- **Physical control.** At g′ = 0 the δ equation is GR's dust equation, known to be non-signalling. The g′ terms reproduce the refereed R15-1 kernel, which serves as a check of the machinery.

**Answers to (b).**
- **Bianchi:** consistent, nonlinearly in spherical symmetry and at linear order, for any W(x,t) (checked).
- **R15-1's g ≠ 0 channel:** not reintroduced. Its strength is g′ = −2Ḣ − κ(ρ+p)_m (`R151:230`), independent of W. (d-i) neither creates nor cures it, and under (S) g′ ≡ 0 (proved in 𝒟).
- **A new instantaneous channel:** none.
  - E_nn = λ₀ is a law constant, not a global reading.
  - p_E = −λ − κW(x,t) is local and cancels.
  - The lattice lapse is gauge for gravity.
  - Creation is local number balance, c = θ_s.
  - Under (S) the zero mode is GR's, so R14-5's global reader P-r13b is not needed (reading).

### 4(c) Observable consequences

All of these hold within 𝒟 and are proved from §4(a)–(b) unless marked otherwise.

- **(c1) No gravitational trace of the vacuum's enthalpy, at any order in 𝒟.** H(z), growth, lensing, PPN and GW propagation are GR + Λ_* on T_m − Vg. The 1e123 ρ_Λ-per-scalar enthalpy (`r1711_absorb_class.out:7-12`) is invisible. So is the U/M vertex ambiguity of that tadpole, R17-4's Lemma M (`TESTS:6177`): any W is absorbed.
- **(c2) No vacuum–matter-flow coupling.** Q has no matter leg: E receives it, and matter exchanges only ∂V. Unlike Q-coupled interacting-vacuum models (comparator, RECALLED) there is no modified growth, σ₈ or H(z) from this sector: the coupling q = 0.
- **(c3) No Λ drift from the exchange.** λ̇ = −g′θ = 0. This contrasts with unimodular energy diffusion (comparator, RECALLED), and with fork F1, where the same Q would drive Λ by 3κW per e-fold.
- **(c4) No preferred-frame gravity from the vacuum.** n drops out (L1), so this sector contributes nothing to PPN α₁, α₂ or vacuum drag. The self-force on a moving compact body is zero, since T_v + T_X = −Vg has no body-dependent kernel. Matter LV in the site frame is carried, not changed.
- **(c5) What (d-i) does not absorb.** By the uniqueness lemma, anisotropic vacuum responses are not absorbable, because E^TL = 0 is imposed:
  - the TT/shear stiffness (K3a″/W1, `WALL.md:38,97`);
  - the E_g/T₂g/K₆/μ_E rows (R16-9/R17-4/R17-10);
  - momentum flux relative to the slices.

  The graviton walls are unchanged.
- **(c6) Distinguishing tests.**
  - Against (d-ii)/no exchange: those give Planckian H(z) and BBN shifts as W(T) changes across crossovers, plus frame-visible momentum densities. Observation already selects (d-i) or W ≡ 0, the latter by pairing, which predicts matched B/F spectra (O3).
  - Against ΛCDM: nothing beyond (S)'s own predictions (`vR17-7:74`). Λ̃_late ≥ 0, P93, and DE content above e₀ need not be temporary.
  - **(d-i) is observationally silent** (reading).

### 4(d) Prices (named, none adopted)

| # | Price | Axiom text touched | Status |
|---|---|---|---|
| **P-vac′ (carried; sharpened)** | (d-i): the grid vacuum has no separate conservation. In 𝒟 under (S) it is equivalent to the source rule "gravity sees the vacuum only through −(V − e₀)g; the site-frame enthalpy W h[n] is exchanged with the creation sector". Number-free. It tracks radiative changes of W by construction (any W(x,t)) | `AX:187` (source/action) | stipulated, not enforced; consistent and non-signalling in 𝒟 (checked) |
| **P-r1711a** | A receiver exists only where the spatial trace equation is not imposed: √h fixed per site plus site creation (V2-type with λ fixed). V1 has none (`R177:209`, counted once) | `AX:37-41` (site creation = Lattice price; = P52/P53, P-V2c carried) | needed |
| **P-r1711b** | The site congruence is hypersurface-orthogonal (= slice normals) with θ_s ≥ 0 everywhere. Under (S) its choice is gravitationally invisible, but one must exist through collapse (CMC is one choice; existence = P-r15c) | `AX:79-80` (permanence, reading); `AX:185` (time metric) | carried form of P-r15c |
| **P-r1711c** | A non-Lagrangian partner: no ultralocal action yields the lapse-independent pure pressure −W h (F4). Consistency rests on H-imp plus Bianchi. vR14-5:84 already notes that no action exists for the E-sector | `AX:187` | named; not a no-go |
| **Bill update** | In 𝒟, **P-Tad** (R17-4's LV-tadpole row, one shared trace counterterm, `C5_R17-4_report.md:200,276`) and P70's uniform part (`R177:297-299`) are the same quantity, ρ+p of the site-frame vacuum, counted once. Under (d-i) it is paid by P-vac′ with **0 numbers**. Under V1 or (d-ii) it is unchanged | — | conditional on 𝒟; reading |

**Counting convention (`TESTS:5700`).** (d-i) uses 0 numbers. The tadpole row is shared by all species (`C5_R13-8_report.md:218`), so the bill drops by one shared stipulated number in 𝒟. (S) carries 0 numbers. P93 and the rest of R17-7's prices are unchanged.

---

## 5. Round-17 rules

- **Whole-zone v_max.** No new law. The W inputs are R11-3's L/G/NN bands and R17-4's zero laws, not recomputed (v_max as stated there). No gauge-field symbol is used.
- **Self-force.** The frame-tied pair T_v + T_X = −Vg exerts zero self-force on a moving compact body. Without exchange, a tilt-proportional Planckian momentum density appears (`r1711_linear_signal.out:15`).
- **Ward.** The gravitational Bianchi identity is standard. E is non-conserved by exactly −κQ (deformed by the exchange, as declared).
- **Enforced or stipulated.**
  - (d-i) and (S) are stipulated rules with no number.
  - Radiative stability: (d-i) holds for any W, so it is stable by construction. (S) tracks loops by definition (`TESTS:6014`), except across a flip in the ordering of minima (`R177:320`).
- **Physical controls.** The g′ = 0 GR dust equation is the known non-signalling GR phase. The W = 0 limit reproduces R14-5 Lemma C (`r1711_lemmaV_general.out:9`), and the g′ terms reproduce R15-1's kernel; those two are consistency checks, not physical controls.
- **Readout bridges.** No susceptibility or stiffness claim is made.
- **Forks.** §4(a) F1–F5, with "not covered" listed.
- **Generic GR comparison.** Everything at g′ = 0 is generic GR + Λ_*. The cancellation of the frame-tied enthalpy, and the receiver's existence, are specific to the grid.
- **Changed hypothesis.** §0: separate vacuum conservation is removed (the item's), and the vacuum is inhomogeneous and time-dependent beyond vR15-1/vR17-7's homogeneous Lemma V.

---

## 6. Notes for a referee (no FAIL or no-go is claimed; these are the load-bearing steps)

1. **Generalized Lemma V** (`r1711_lemmaV_general.out:1-2`). Is the reduction Bianchi ⇔ ∇·(E + κWh) = 0 right given H-m? The symbolic check uses spherical symmetry; the covariant identity is general.
2. **The (S) step g′ ≡ 0.** It uses λ constant and θ_n ≠ 0. An instant with θ_n = 0 everywhere, e.g. a static universe, is excluded by expansion.
3. **The linear check** (`r1711_linear_signal.py`). The lattice tilt is ξ(t)cos kx in dust-synchronous gauge, and the fields are evaluated on lattice time. The background relation λ̇ = −3Hg′ is used.
4. **Uniqueness** (`r1711_absorb_class.out:1`) and **F4** (ultralocal only).
5. **F3.** Under (S) with a free slicing, does (d-ii) still need W = 0? I rely on R13-3's conditional Lemma F/G′.
6. **Whether 𝒟 is a fair stand-in for "R14-5/R15-1's E-sector equations with C = E₀".** With λ fixed, the E-sector reduces to "spatial trace not imposed". This is V2 + (S) + site creation.

**Strong-word check.**
- "Exactly": an algebraic identity in 𝒟, for C¹ W(x,t), mean stress.
- "At all times": every history in which λ stays the (S) constant.
- "Non-signalling": no Lemma S term (g′ ≡ 0), no physical elliptic equation, and no global number read after the start, since e₀ is a law constant.
- "Covariant": on shell; n is absent from the gravitational equations; W's computation is lattice-frame-based, like e₀.
- "Unique": within H-imp under (S).
- "Silent" / "no observable": the gravitational sector at the one-point level, in 𝒟. Matter LV and the anisotropic vacuum response are excluded.
- "Excluded" (F1, F2): magnitude arithmetic with R11-3/R17-4 inputs at a = ℓ_P.

**What would change the reading.**
- **To OPEN:** a referee ruling that 𝒟's "trace not imposed" receiver is not R14-5/R15-1's E-sector, or that a non-Lagrangian partner disqualifies "consistent".
- **To INCONSISTENT:** a demonstration that the site congruence must be vortical somewhere (H-site fails), or that the E-sector must carry anisotropic grid stress at one-point level.

## 7. Files

- Report: `S/R17-11_report.md`.
- Scripts and outputs: `S/scripts/r1711_lemmaV_general`, `r1711_linear_signal`, `r1711_absorb_class`, `r1711_unimodular_fork` (each `.py` with its `.out`).
- Reruns: `S/recheck/{R17-7,R15-1,R11-3}/*.rerun`, with the originals in `orig/`, and `S/recheck/run_all.log`.
