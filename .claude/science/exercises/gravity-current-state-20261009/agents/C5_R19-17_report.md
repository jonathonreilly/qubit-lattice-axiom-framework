# C5 R19-17 report: V1 + (S_ad) beyond homogeneity. Is the adiabatic-lowest-state rule local, covariant and non-signalling for lumps?

- **Worker:** Claude Opus 5.5 (Claude Code agent; same family as the supervisor). Started 05:43Z, report 06:06Z, 2026-10-13. Unrefereed. No repository file was edited.
- **Item:** `TESTS:7920-7942` (FIXED readings at `:7938-7941`; expectation at `:7942`).
- **Scratch:** `S/` = `.../scratchpad/C5/R19-17/`. Scripts and outputs are in `S/scripts/`; the runner rechecks are in `S/recheck/`. Each script runs in under 2 min at `OMP_NUM_THREADS=2`.
- **Abbreviations:** `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS` = `.claude/science/exercises/gravity-current-state-20261009/TESTS.md`; `rX` / `vX` = `agents/C5_X_report.md` / `agents/C5_X_referee_verdict.md` in that folder.
- **Labels:** proved / checked (numerics or sympy this run) / suggested / reading / comparator. RECALLED means from memory, not verified this run. Nothing was downloaded.
- **Units:** lattice units, comoving spacing 1, c = ħ = 1. Cosmology numbers are in Planck units, with ρ_Λ = 1.134e-123 as in `rR19-14:7`.

---

## 0. Reading against the FIXED readings: **LOCAL-OK** (worker), in the stated class 𝒱. No FAIL or no-go is claimed, so a referee is optional.

**Class 𝒱 (stated before the title).**
- **V1.** A fixed site set with no creation. The lattice embedding is three comoving label fields X^I(x), and the sites ride the congruence u[X]. The spacing ℓ = n^{-1/3} follows that congruence's θ, by site-number conservation.
- **H-cov.** The free lattice law is written for any embedding: link coefficients are measured by the metric. The law is diffeomorphism-invariant as a functional of (fields, g, X). This is a model hypothesis. The planar NN-scalar construction used below satisfies it.
- **State.** Free (quadratic) fields, in the adiabatic vacuum plus excitations.
- **(S_ad), local form.** Subtract T_ad = (2/√−g) δΓ_ad/δg, where Γ_ad[g, X] is the local derivative expansion of the vacuum's effective action through adiabatic order 2.
- **Matter and perturbations.** Linear perturbations of FRW with cold dust. Matter has the common limiting speed (c = 1; those cone rows are paid elsewhere and counted once).

**What is met in 𝒱.**
- **(i) A local, generally covariant (S_ad) exists.** It is a functional of the metric *and* the lattice frame, so it is not Lorentz-invariant. The status of its parts:
  - its structure is proved;
  - its order-0 content is computed exactly;
  - its order-2 locality is checked in the planar sector, both static and time-dependent (§2(a)).
- **(ii) Bianchi.** Lemma N (proved; checked) reduces Bianchi to one condition: the excitations exert no net force on the lattice, F_I = 0. For cold dust with c = 1, F_I = O(ε³) (checked), so Bianchi holds at linear order under both local readings of (S_ad) (§2(b)).
- **(iii) No instantaneous channel at linear order.**
  - The gravitating equations are GR + dust, so the Lemma-S jump is Δδ̇ = F, the GR control (`rR15-1:137`, rerun identical).
  - No global quantity (λ(t), CMC slicing, uniform E_nn) enters.
  - The vacuum's own response is causal: zero to round-off outside the lattice light cone (checked).

**What 𝒱 does not cover. These are the referee items and the limits of the reading.**
- The full order-2 basis is not computed: shear rate, vorticity, acceleration, and T₂g strain (which needs a non-NN stencil).
- Hot or relativistic matter is not covered. There F_I ≠ 0 at O((ℓp)²) at linear order. One reading of (S_ad) then breaks Bianchi at that order, and the other has an undetermined, zero-inertia lattice frame (§2(c)).
- Interacting fields, Dirac and photon content (only the NN scalar was computed), and order 4 are not covered. For massless fields order 4 is non-local (RECALLED).

**Against the expectation (`TESTS:7942`).**
- **Borne out.** LOCAL-OK holds to second adiabatic order, and the price moves to the frame.
- **Refined:**
  - The frame price is a *lattice-frame law*, and the two local readings of (S_ad) choose it differently (§2(c)).
  - (S_ad) at order 2 must include gradient terms, not only θ². These terms are the vacuum's induced Newton-constant term, so subtracting them makes G entirely supplied, which is what V1 needs anyway (`rR19-14:70-74`).
  - At order 0, (S_ad)'s local form contains R19-15's (S\*) (the vacuum strain response, i.e. the shear rows).

---

## 1. Plain words

- **The vacuum's "lowest state" can be defined point by point.** On a lattice whose spacing varies from place to place, the vacuum energy at each point equals the uniform-lattice value at the local spacing, plus small corrections set by how fast the spacing changes nearby. With two numbers fitted on one lump shape, the formula predicts the vacuum energy of four other lump shapes to within 1–2%. When the lattice is stretched faster in one region, the extra vacuum energy there follows the local stretching rate, and nothing changes outside the light cone. So "subtract the adiabatic vacuum's stress" is a local rule, written in terms of the metric and of where the lattice sites are.
- **Gravity's consistency condition becomes "matter must not push on the lattice".** If the subtracted part is built this way, the conservation law gravity needs holds exactly when ordinary matter exerts no net force on the lattice sites. Slowly moving matter on a lattice that respects cubic symmetry feels the lattice only at fourth order in its velocity, so at first order the force is zero. Gravity is then plain general relativity with the matter, and nothing travels faster than light. No global clock is involved, unlike the earlier constant-mean-curvature mechanism.
- **The open choice is how the lattice itself moves.** There are two honest options:
  - The vacuum keeps its inertia but not its weight. The lattice then moves like an elastic solid made of vacuum: it is pushed by gravity but pushes nothing. Its sound speeds come out below light speed (about 0.8 and 0.5 c for scalar content).
  - The vacuum has neither weight nor inertia. The lattice's motion is then undetermined until matter's lattice-scale effects pin it.
- **One practical consequence.** The rule must also subtract the vacuum's response to spatial curvature. That response is the vacuum's contribution to Newton's constant. Without it, lumps would carry vacuum-energy patterns about 1e5 times the dark-energy density at Planck-scale spacing (suggested).

---

## 2. Results

### 2(a) A local covariant form of ⟨T⟩_ad, to adiabatic order 2

**Construction (proved, structural).**
- Let b^{IJ} = g^{μν}∂_μX^I∂_νX^J (the inverse lattice metric), n = √det b, and u^μ ∝ ε^{μνρσ}∂_νX^1∂_ρX^2∂_σX^3.
- The vacuum effective action of a free lattice law obeying H-cov is a diffeomorphism-invariant functional Γ[g, X]. Its derivative expansion in slowly varying (g, X) is local at each order:

  Γ_ad = ∫√−g [ −ε(b) + Σ_k c_k(b) 𝒪_k^{(2)} + O(∂⁴) ]

  where the 𝒪^{(2)} are the second-order scalars built from (g, u, n): θ², σ², ω², a_μa^μ, ³R, (D ln n)², u·∂θ, and so on.
- T_ad = (2/√−g)δΓ_ad/δg is then local and generally covariant. It refers to the lattice frame u[X].
- **Why order 2 is local** (reading; RECALLED for the continuum analogue). For gapless 3D fields the order-2 coefficients are UV-dominated and IR-finite: ⟨1/Ω⟩ converges. The first IR log, and with it the non-local form factors, appears at order 4 (⟨1/Ω³⟩).

**Order 0: the vacuum is an elastic cubic solid** (proved: closed form; checked: numerics). For the NN scalar,

  ε(b) = √(b₁b₂b₃) · ½⟨√(Σ_i b_i·4 sin²(k_i/2) + m²)⟩ for diagonal b.

- **Massless** (`r1917_vacuum_medium.out:2-3`):
  - ρ = 1.193801 and p = ρ/3 exactly. Exactness follows from scaling, since the only length is ℓ.
  - W = ρ + p = 1.591735.
- **Wave speeds from L = −ε(b)**, with the formulas c_L² = 1 + 4ε_{,11}/W and c_T² = 1 + 2(ε_{,11} − ε_{,12})/W:
  - The fluid check returns c_T² = 0 and c_L² = nε″/ε′ (`:1`).
  - c_L²[100] = 0.631424.
  - c_T²[110] (pure E_g strain) = 0.223568.
  - These are consistent with a cubic solid of bulk speed² 1/3: c_L² = 1/3 + (4/3)c_T².
  - A finite-difference cross-check agrees (`:12`).
  - For m = 0.1–3, both speeds stay in (0, 1) (`:4-11`).
- **Count once.** This is R19-15's Lemma H statement that the lattice vacuum is a cubic elastic solid (`rR19-15:45,161`; worker). The new parts here are the sound speeds and the covariant-medium form.
- **T₂g** (off-diagonal b) needs a non-NN stencil (P-r1917b). It is not covered.

**Order 2, static lumps: locality checked** (`r1917_static_lump.out`).
- **Setting.**
  - 3D NN scalar, ds² = −dt² + a(z)²dx², with link coefficient = area/length.
  - The planar lump is solved exactly per transverse momentum on a 16² midpoint grid, Nz = 128.
- **Residual after order 0:** r = ρ − ρ_hom(a(z)).
- **Order 2.** Doubling the width divides max|r| by 3.977 (m = 0) and 3.974 (m = 0.5); order 2 predicts 4 (`:9,31`).
- **Universality.** A two-coefficient local ansatz r = [α(∂ ln a)² + β∂² ln a]/a⁴ fitted on one profile predicts the other four:
  - m = 0: α = +0.164, β = −0.0497 (`:10`); every profile is predicted to within 0.9% of max|r| (`:11-21`).
  - m = 0.5: within 2% (`:33-43`).
  - The small-amplitude limit reproduces β (`:22,44`).
  - The leftover is order 4 (width⁻²).
- **Tails.** Beyond 5 widths |r| ≤ 1.3e-7, against peaks up to 1.5e-4 (`:4-8`). These tails are the profile's own Gaussian tail, not a non-local term.
- **Scope.** The coefficients depend on the stencil (the link average a_{z+½} is a stated choice). Locality does not.

**Order 2, local strain rates: tracking checked** (`r1917_dynamic_lump.out`; `r1917_dynamic_variants.out`).
- **Setting.** a(z,t) = exp(A g(z)s(t)), with a smooth ramp s. The evolution is the exact symplectic flow of the frozen midpoint Hamiltonian per step, starting from the exact ground state.
- **The lag** above the instantaneous ground state (the s = 0 frame of R19-14), compared with R19-14's homogeneous formula ⟨1/Ω⟩H_loc²/(4a²) evaluated at the *local* H_loc = ∂_t ln a:
  - At the ramp midpoint the whole profile matches to 1–3% (`dynamic:6-8,17-19`).
  - Ramp rate² scaling: 3.965, against 4 expected (`:25`).
  - The homogeneous control matches to 1–5% at all ramp phases (`variants:4-6`).
- **Shoulders.** At ramp phases 0.25 and 0.75 there are deviations of up to ±24% for w = 5. They are odd in s̈, nearly independent of the ramp time, and shrink by about 4 when w doubles once the homogeneous offset is removed (`dynamic:4,9`; `variants:9-11`). So they are a local order-4 term of type ∂_z²∂_t² ln a, which is linear in amplitude and therefore competes with the order-2 H² term at A = 0.1 (checked scaling; reading for the identification).
- **After the ramp.** The excess above the final ground state is ≤ 3.5e-8 (Tr = 16) and 4.9e-9 (Tr = 32), so the vacuum keeps no standing memory (`dynamic:12,23`).

**Answer to (a).** Yes. The "adiabatic lowest state" is definable locally for lumps and local strain rates, as T_ad[g, X] above. It is generally covariant, it refers to the lattice frame, and its locality is checked in the planar sector. The local θ² lag formula of R19-14 holds pointwise.

### 2(b) Bianchi, and the linear signalling test

**Lemma N (Noether; proved — the standard diffeomorphism argument, RECALLED form — and checked).** For any diffeomorphism-invariant Γ[g, X], with T^{μν} = (2/√−g)δΓ/δg_{μν} and E_I = δΓ/δX^I:

  ∇_μT^{μν} = (1/√−g) E_I ∇^νX^I.

- **Checked** in 1+1 dimensions with a general metric and a general X. The Lagrangian includes frame-dependent order-2 terms: √−g[−ε(n) + c(n)θ² + d(n)(u·∂n)²]. The residual is exactly 0 at two random rational points, against div T ~ 1e-1 (`r1917_noether.out:3-4`).
- The sign convention was fixed after a first run whose residual was exactly 2·div T (`r1917_noether_signcheck_v1.out`).

**Corollary B (proved, given Lemma N).**
- The free-field ⟨T⟩ is the metric variation of the full effective action Γ.
- Let T_grav = ⟨T⟩ − T_ad (that is, (S_ad)) and keep the fields on shell. Then

  ∇_μT_grav^{μν} = (1/√−g) F_I ∇^νX^I,  F_I := δΓ_exc/δX^I = δΓ/δX^I − δΓ_ad/δX^I.

- So Bianchi holds iff F_I = 0: the excitations above the adiabatic vacuum exert no net force on the lattice (∇X^I has rank 3).
- **No global carrier.** The would-be carrier is X itself, which is local. Contrast R14-5/R15-1, where the subtracted object was a spatially uniform λ(t) with an elliptic lapse (`vR15-1:5,19`), and R17-11's class 𝒟 (`vR17-11:44`).

**Two local covariant readings of (S_ad)** (reading; both are new completions under literal-first, `TESTS:7124`):
- **(S_ad-W), "weightless".** T_ad is removed from the gravitating source only. The lattice keeps the vacuum's inertia, and its equation of motion is δΓ/δX = 0, i.e. δΓ_ad/δX = −F. Bianchi ⇔ F = 0.
- **(S_ad-A), "absent".** The counterterm action −Γ_ad[g, X] is added. The lattice's equation of motion is F = 0, so Bianchi holds automatically on shell (Lemma N applied to the total action).

**F_I for the stated matter** (checked, `r1917_lv_force.out`).
- A cold-dust particle with the NN lattice dispersion has lattice-frame part δL = ℓ²m³ Σ v_rel,i⁴/24 + …, which is O(v_rel⁴) (`:2-3`). So F_I = O(ε³) at linear order, and both readings are Bianchi-consistent at linear order about FRW + dust.
- With a species-speed offset c ≠ 1, δL ∝ (1 − c²)v_rel² and F = O(ε) (`:4`). This is the cone row, counted once.

**Linear signalling** (proved in 𝒱; GR control rechecked).
- At linear order T_grav = T_dust, and the equations are G_μν = κT_dust,μν, with G supplied and Λ̃ = 0 under P93, inherited.
- R15-1's Lemma-S jump is then the GR control Δδ̇ = F, ultralocal (`rR15-1:137`; `r151_signal` rerun identical, `S/recheck/recheck_summary.out`).
- The lattice displacement does not appear in any gravitating equation: it enters only through F, which is O(ε³).
- **The vacuum's own response is causal** (checked, `r1917_causality.out:4-8`). A compact strain bump is ramped fast (Tr = 4). The response at distance d beyond the bump edge stays at round-off (≤ 1.7e-13) for d > t, while inside it reaches 1e-6 to 2e-4. The front moves at or below the NN group velocity.

**Answer to (b).** Subtracting the adiabatic stress keeps Bianchi without any CMC-type global carrier. The only condition is F_I = 0, which is local, and it holds at linear order for cold dust. There is no Lemma-S jump.

### 2(c) The lattice-frame rule (P-r1914d)

- **Under (S_ad-W): the lattice is the vacuum medium** (proved: structure; checked: speeds).
  - Its equation is δΓ_ad/δX = 0: the relativistic elastic equations of the order-0 solid ε(b), plus order-2 corrections.
  - These equations are hyperbolic and local, with c_L² = 0.63 and c_T² = 0.22 for NN scalar content. That is subluminal, and stable in the computed E_g sector.
  - The rule needs no new number: every coefficient comes from the law's vacuum.
  - **Consequences (suggested):**
    - The lattice is a test medium: gravity moves it (it falls into wells and is strained by GWs), but it sources nothing. That is inertia without weight, so gravity and the lattice do not act on each other equally. This violates no identity.
    - In FRW its homogeneous solution is the cosmic frame, n ∝ a⁻³.
    - In a bound region it is pressure-supported (hydrostatic δ ln a ≈ Φ/(3c_s²) ≈ Φ). It keeps expanding with the cosmic flow, so ℓ ∝ a(t) even inside galaxies, consistent with P-r1914c.
  - **Limit.** Hot or relativistic excitations with lattice artefacts give F ≠ 0 at O((ℓp)²) at linear order; for radiation the momentum-flux term is linear in the relative velocity. Bianchi then fails at that order unless matter is lattice-blind (suggested; not computed).
- **Under (S_ad-A): the lattice has neither weight nor inertia.** This is R19-14's reading at `rR19-14:130,180`.
  - Its equation is F_I = 0.
  - At Lorentz-invariant order and with cold dust at linear order, X is undetermined and nothing observable depends on it (proved in 𝒱).
  - At O((ℓp)²) with hot matter, F = 0 is a zero-inertia constraint that fixes X. Its well-posedness and characteristic speeds were not computed. They are the open sub-item.
- **Neither reading forces "the lattice follows the matter's θ".** Under W the lattice follows its own θ. Under A any congruence is allowed at linear order.

### 2(d) Observables

- **Gravity at linear order.** Gravity is GR with T_exc (matter plus real excitations) under both readings. It does not depend on the frame, and it has no vacuum term at orders 0 or 2 (proved in 𝒱).
- **The order-2 gradient terms are the vacuum's induced Newton-constant term** (suggested).
  - Example: under (S_ad-W) a galaxy (Φ ~ 1e-6, L ~ 10 kpc, ℓ = ℓ_P) strains the lattice by δ ln a ~ Φ. The unsubtracted β-term gives ρ₂ ~ β∂² ln a/ℓ² ≈ 1.4e-118, i.e. about 1e5 ρ_Λ (arithmetic from `static:10`). That is ≈ 4πβ(ℓ_P/ℓ)²ρ_m, an O((ℓ_P/ℓ)²) shift of G that drifts as ℓ ∝ a.
  - So (S_ad) must subtract order 2 in full, gradients included. G is then entirely supplied, which R19-14's G0-c already requires (`rR19-14:70-74`).
  - **Contrast with R19-19's (S\*\*)** (not yet run), which keeps the Lorentz-invariant part of the O(q²) response. (S_ad) at order 2 removes it as well.
- **The shear rows.** The order-0 strain response of ε(b) is the shear rows (R19-15 Lemma H). Local (S_ad) subtracts it, so it contains (S\*) (`TESTS:7995-8007`; worker; count once).
- **Frame dependence** enters only through lattice artefacts in matter (O((ℓp)²); the LV walls, counted once) and the order-4 residue (O(H⁴) and O(∂⁴); negligible per `rR19-14:122`).
  - Under W the reference frame is the vacuum medium's: ≈ the cosmic frame everywhere, including in bound systems.
  - Under A it is undetermined at the order where it is invisible.
- **New, under W only** (suggested): the lattice medium carries its own non-gravitating elastic waves (c_L ≈ 0.79, c_T ≈ 0.47 for scalar content). They are visible only through LV couplings.
- **Non-adiabatic production** is real and gravitates, as in GR. Its stock after the checked ramps is negligible (`dynamic:12,23`).

### 2(e) Prices (named, none adopted)

- **P-r1917a, local (S_ad).** "The stress of the lattice's adiabatic vacuum, as a local functional of the metric and the lattice embedding through adiabatic order 2, does not gravitate."
  - It replaces the homogeneous wording of P-r1914a.
  - At order 0 it contains (S\*) (P-R19-15a; count once). At order 2 it contains the induced-G subtraction.
  - It touches `AX:186-187` (source/action) and `AX:116-123` (no Hamiltonian or frame supplied).
- **P-r1917b, H-cov.** The lattice law on an arbitrary embedding (g, X): metric-measured links, plus the stencil for off-diagonal strain (T₂g). These are law data.
- **P-r1917c, the lattice-frame law.** Choose one:
  - **W:** a vacuum medium with inertia but no weight. Bianchi is exact only if excitations are lattice-blind (F = 0).
  - **A:** no inertia. The frame is undetermined at Lorentz-invariant order, and a zero-inertia constraint F = 0 applies at the LV order, with its health untested.

  This sharpens P-r1914d.
- **Inherited, counted once:**
  - P-r1914c (no lattice-native scale; ℓ/ℓ_P ∝ a);
  - P93;
  - J2 (`vR18-6:7`);
  - the cone rows (c = 1).

---

## 3. Prior art (each counted once)

- **R19-14** (worker; `rR19-14:12-38,114-147,166-184`): homogeneous (S_V)/(S_ad), the s = 0 lag formula, G0-c and P-r1914a–d. This run extends its §2.3 "not built" items (`:128-130`).
- **R19-10 and its verdict** (`vR19-10:40`): for a growing law, the axioms supply no instantaneous Hamiltonian or energy comparator. Here, V1 has no creation.
- **R17-11 and its verdict** (`vR17-11:3,25-26,44`): class 𝒟, the exchange current, and a zero Lemma-S parameter. Here no E-sector is used.
- **R15-1 and its verdict** (`vR15-1:5,19`; `rR15-1:122-143`): Lemma S, the Yukawa jump at g ≠ 0, and the GR control.
- **R13-3, R11-3 and R12-2:** the smooth-continuum exclusion, V1 SOURCED with w ≥ 0, and L-CR. These are not re-derived.
- **R19-15** (worker; `rR19-15:45,127,161,213-233`): Lemma H, the lattice vacuum as a cubic solid, and (S\*).
- **Comparators (RECALLED):**
  - Parker–Fulling adiabatic regularization;
  - the DeWitt–Schwinger / Hadamard local counterterms, which are local and conserved through order 4, with non-local log form factors beyond;
  - Sakharov induced gravity (the order-2 vacuum term ∝ R/ℓ²);
  - the relativistic elasticity / solid EFT (Lagrangian labels X^I);
  - the Noether identity for diffeomorphism-invariant actions with auxiliary scalars.

---

## 4. Archived runners rechecked (before relying on them)

- The 20 runners of R19-14 (2), R17-11 (4), R11-3 (5) and R15-1 (9) were copied to `S/recheck/` and rerun there; nothing was run in the repository.
- All reproduce their stored outputs (`S/recheck/recheck_summary.out`).
- The only differences are in `r151_dispersion` and `r151_window`, whose stored `.out` include stderr: the scratch path printed inside a RuntimeWarning differs. `r151_quadratic` matches on stdout; its `open(__file__)` writes only a `.pkl`.
- One methodological note: the first recheck pass was invalid because macOS has no `timeout`, and was redone. Only the second pass is reported.

---

## 5. Scope and strong words

- **"proved":**
  - Lemma N and Corollary B, for any diffeomorphism-invariant Γ[g, X] (standard; checked in 1+1);
  - p = ρ/3 for the massless NN lattice under isotropic stretch (scaling);
  - the fluid-limit sound-speed formulas;
  - F_I = O(ε³) for cold dust with c = 1 and an even, cubic dispersion;
  - "GR at linear order", in 𝒱.
- **"checked":**
  - order-2 locality and universality in the static planar sector;
  - local H² tracking in the dynamic planar sector;
  - causality of the vacuum response;
  - the order-0 sound speeds.

  All of these are for the NN scalar only.
- **"exactly":** p = ρ/3; the Noether residual being 0. Nothing else.
- **"covariant"** means generally covariant (diffeomorphism-invariant) *with a lattice frame field*. It does not mean Lorentz-invariant. This is the same status as R17-11's "covariant embedding" (`vR17-11:44`).
- **"no instantaneous channel"** holds at linear order about FRW + cold dust in 𝒱. It is not claimed for hot matter at O((ℓp)²).
- **Not covered:**
  - the full 3D order-2 basis (σ², ω², a², T₂g);
  - Wilson-Dirac and photon content;
  - interactions;
  - order 4;
  - the zero-inertia frame constraint of reading A;
  - the Bianchi defect of reading W at O((ℓp)²) for radiation;
  - nonlinear lumps;
  - site creation (excluded by the item).

## 6. Files (`S/scripts/`)

- `r1917_static_lump.py/.out`: static planar lumps; order-0 subtraction; the width-scaling and universality fits; m = 0 and 0.5.
- `r1917_dynamic_lump.py/.out`: time-dependent local strain; the lag against the local H² formula; rate scaling; after-ramp excess; a loose cone check.
- `r1917_dynamic_variants.py/.out`: homogeneous and w = 10 controls, separating the order-4 shoulder term.
- `r1917_causality.py/.out`: compact bump, fast ramp; the response beyond the light cone.
- `r1917_vacuum_medium.py/.out`: ε(b) for the NN scalar; W, w, c_L² and c_T²; fluid-limit check (sympy); finite-difference cross-check.
- `r1917_noether.py/.out` (+ `r1917_noether_signcheck_v1.out`): the Noether identity in 1+1 with frame-dependent order-2 terms (sympy, exact).
- `r1917_lv_force.py/.out`: the lattice-dependent part of the dust Lagrangian, as a series in the relative velocity (sympy).
- `../recheck/`: copies of the archived runners, `.rerun` outputs, `stored/` originals, `run_all.sh`, and `recheck_summary.out`.
