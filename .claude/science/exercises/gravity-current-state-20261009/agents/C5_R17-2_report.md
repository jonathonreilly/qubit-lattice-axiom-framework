# C5 R17-2 report: W7 in the boost bracket. Does an escape outside class 𝒞 close degree 3, and is anything physical left?

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). **Unrefereed.** Ran 2026-10-13 00:18Z to about 00:50Z. No repository file was edited. No downloads, no web lookups; every literature item is RECALLED.

**Scratch.** `S/` = `.../scratchpad/C5/R17-2/`. All scripts run in under 5 s at `OMP_NUM_THREADS=2`.
- `S/scripts/r172_dressing.py` / `.out`: (A) the dressing identity, (B) the T3 equations as dressing equations, (C) the kernel of the weak boost operator, (D) boost factorization.
- `S/scripts/r172_worldline.py` / `.out`: real-space form of R16-12's forced boost kernel.
- `S/scripts/r172_population.py` / `.out`: Boltzmann exponents.
- `S/scripts/r1612_lib.py`: R16-12's `r1612_degree3.py` up to its main block, unmodified. `S/scripts/sublum_copy.py`: R14-1's `sublum.py`, unmodified (`cmp` identical).
- `S/recheck/`: R16-12 and R16-8 archived runners, rerun.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `TESTS`, `SUMMARY` are in `P/`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md` (read in full). `vR16-12` = `P/agents/C5_R16-12_referee_verdict.md`; `refR16-12` = `P/agents/C5_R16-12_referee.md`; likewise `vR16-8`, `refR16-8`.

**Read.** `AX` in full; `TESTS:2302-2320` (C5 method), `:5685-5783` (Round 17 rules and items), `:5873-5906` (R16-10…12 verdicts); `SUMMARY:397-413` (§17), `:677-714` (§26); `C5_S20_synthesis.md:1-120,225-300`; `C5_R16-12_report.md` in full, `vR16-12`, `refR16-12`; `C5_R16-8_report.md` in full, `vR16-8`, `refR16-8`; `C5_R13-4_report.md:150-170` and `TESTS:4644-4664,4771-4777`; `C5_R12-1_report.md:205` (grep hit).

**Reruns (rechecked before use).** All five archived runners were rerun after deleting their `.out` files; each regenerated `.out` is byte-identical to the archive: `r1612_degree3`, `r1612_controls`, `r1612_population`, `r168_jets`, `r168_kernel` (exit 0 each). *Process note:* my first rerun attempt used `timeout`, which is absent on this machine; it silently did not run and `cmp` compared copies. That attempt is void; the reruns quoted here are the second, valid ones.

**Labels.** proved = complete under stated hypotheses, unrefereed; checked = numerics here; suggested = argued, not proved; reading = interpretation; comparator = literature, RECALLED.

---

## 0. In plain words

1. **The singular generator W of R16-12's Lemma W is not an arbitrary singular map. It is general relativity's own dressing.** It is exactly the linearized-ADM transformation that attaches to each matter quantum its Newtonian field (solving the Hamiltonian constraint), its gravitomagnetic field (solving the momentum constraint), and the transverse-traceless field that a uniformly moving source carries with it (proved at leading order; checked to 1e-8 or better).
2. **R16-12's translation-sector equations (Theorem T3) are exactly the equations that make this dressing remove the degree-3 matter–graviton coupling.** So undoing the dressing turns the (β) Hamiltonian into the *free* Hamiltonian plus terms proportional to the linear constraints (non-local lapse and shift, i.e. gauge). This corrects R16-12's description of the relocated Hamiltonian as "non-local": it is non-local only in its gauge (constraint-proportional) part (proved at leading order; checked to 9e-14).
3. **Plain reading of the W7 tail at degree 3.** An edge quantum's GR field moves with true translations. The lattice momentum moves the quantum by a slightly different rule. The tail is that mismatch, Φ_c = {P⁰_c, W_GR} ≠ 0 only because P⁰ is not a translation. In the bulk, at this order, it has no dynamical content beyond GR's dressing. What survives is a statement about the global (boundary) Poincaré charges (suggested; the boundary bookkeeping is not done).
4. **Lemma C restated.** The (β) repair exists exactly when the edge quantum's comoving gravitational field exists, i.e. when it does not emit gravitational Cherenkov radiation. That is GR-generic behaviour.
5. **The boost obstruction (Theorem B3) can be traded, not removed.** Using the same dressing, a boost generator without the world-line kernel satisfies the boost bracket weakly, provided the Hamiltonian representative carries weakly-vanishing, non-local, matter-dependent lapse and shift terms. B3's rigidity argument does not cover such x_b-weighted constraint-proportional terms (suggested; boundary terms not done).
6. **Escapes 2, 3, 5 are not closed.** For the world-line kernel (escape 2), the other two Poincaré brackets reduce, by a Jacobi argument, to a single condition on the zero-frequency shell q·v = 0, where the kernel itself is singular (proved under stated premises; not evaluated). Escapes 3 and 5 relocate the non-locality to infinity or into a multiplier (suggested).
7. **Reading: OPEN.** No completed degree-3 system exists, so no observable invariant under completed constraints can be certified, and no instantaneous response is demonstrated. The deciding input that is missing is a readout bridge fixing which observables are physical (`AX:82-83`).

---

## 1. Hypotheses and classes (stated before any title)

- **As R16-12 (`C5_R16-12_report.md:72-113`), unchanged:** H-grade (gravity degree 1, matter bilinears degree 2); H-conv ({h,E} = 1; R1 = −s·h with s = qq − |q|²I; ḣ = 𝒢E, Ė = −𝒦h; graviton ω = |q|); standard (undeformed) HDA as the target; H-mat: free number-conserving one-band separable matter, m = 0.3, current-aligned P = ∂(ε²/2) = εv; H-lead: leading order in the smearing momentum q (Vlasov form), ḟ = −iωf with ω = q·v, δ_c = q·Δ_c/ε.
- **Laws and whole-zone v_max (round-16/17 rule):** S(1.4) 0.99270, G(1.4) 0.99386 (`vR16-8:15`). L-box(2.0) 4.1209 appears only as R16-12's superluminal control. **Graviton symbol:** continuum at leading order, ω = |q|, v_max = 1 (the R9-9 lattice symbol has v_max 1.0000, `C5_R16-8_report.md:71-73`).
- **The dressing W.** W = −iΣ_{q,k}(E·Ξ_E + h·Ξ_h)f(q,k) with Ξ := Φ_c/δ_c from R16-12's T3 solution (c-independent by Lemma W, `vR16-12:13`). The flow F = exp({·, W}).
- **Bulk vs boundary.** "Bulk" statements hold for every smearing with Fourier support at q ≠ 0 (compactly supported lapse/shift). Global (Killing) charges involve q → 0 limits of singular symbols, i.e. boundary terms; they are flagged wherever used.
- **Ward/HDA:** the target is the standard HDA throughout. Where a result holds only weakly (constraint-proportional residuals), it is named a weak/deformed closure, per `vR16-12:5`.
- **Excluded, and not covered:** pairing; P90 matter; pair-creating or interacting matter; nonlinear gravity beyond degree 3 (degree-4 shells are discussed only as an argument, §3.6); qubit gravity; Λ; non-Killing degree-3 completions other than the dressing-defined ones of §3.4; the ADM boundary bookkeeping for the singular dressing (named as the open gap in §3.4 and §3.10).

## 2. Prior art (grep of `P/` and `docs/` for dressing / Dirac dressing / Pauli–Fierz / world-line; each counted once)

1. **R16-12 and its referee.** T3, J3 confirmed at leading order, weak (`vR16-12:5`); B3 a bounded-angular, presentation-dependent obstruction, degree −2 symbol with unbounded angular factor (`vR16-12:7-11`; `refR16-12:40-66`); Lemma W first order only, the split not physical without fixing the observable algebra (`vR16-12:13`); Lemma C: |v| < 1 sufficient, not necessary (`vR16-12:15`); population floor 1.431782/a (`vR16-12:19`).
2. **R16-8 and its referee.** 1/r² kernel, Bianchi-fixed 1/r⁴ curvature; the curvature is not invariant under the completed momentum constraint (`vR16-8:5`); a constrained elliptic auxiliary exists with a non-local multiplier (`vR16-8:7`); the fork is not exhaustive (`vR16-8:9`).
3. **R13-4(ii)(c)** (`C5_R13-4_report.md:162-166`, suggested there): a Newtonian-kernel degree-3 dressing trades the singular completion for a change of the matter energy density; within dressings plus regular matter redefinitions the non-regularity cannot be removed. **R13-4(ii)(b)** (`:157-161`): gauge generators reach across space. My §3.1–3.2 are compatible with both and sharpen them: the specific W fixed by T3 *is* the GR dressing, and it removes the degree-3 coupling from the physical Hamiltonian.
4. **R12-1** (`C5_R12-1_report.md:205`, suggested there): an order-by-order Coulomb-type dressing W builds the physical sector, "non-locality in the states, not in the law".
5. **R16-5's grading lemma** (`vR16-5:19`): pair terms cannot cancel number-conserving defects.
6. **SUMMARY §17** (`SUMMARY:397-413`): the root obstruction (zone mean −β).
7. **Comparators (RECALLED):** Dirac's Coulomb dressing; the comoving (Liénard–Wiechert-type, uniformly moving) field of a source in linearized GR, and its absence above the wave speed (Cherenkov); removal of a linear coupling to a free field by a canonical (Pauli–Fierz / Bloch–Nordsieck-type) transformation when no real transitions are kinematically allowed; Donnelly–Giddings gravitational dressings (power-law equal-time commutators of dressed operators at O(κ)); Coulomb-gauge QED (instantaneous multiplier, local physics); ADM boundary charges.

---

## 3. Results

### 3.1 Lemma D: W is the linearized-GR dressing (proved at leading order; checked)

**Statement.** With Ξ = Φ_c/δ_c from T3, for every lapse N and shift ξ with Fourier support at q ≠ 0:
- (A1) {C_s^(1)[N], W} = T00[N], since s·Ξ_E = −iε exactly;
- (A2) {C_j^(1)[ξ], W} = P^m[ξ], since q·Ξ_h = P/2 = εv/2 exactly;
- (A3) the TT part of the shift (δh, δE) = ({h,W}, {E,W}) = (−iΞ_E f, +iΞ_h f) equals minus the GR comoving TT field of the W1 stress σ₀ = (ε/2)vv moving at the group velocity: h_TT = 2σ₀^TT f/(ω² − |q|²), E_TT = −iωσ₀^TT f/(ω² − |q|²). The Newtonian part has the same ratio, −1.

So F = exp({·,W}) adds to the metric (with one overall sign) the full linearized-GR field of each matter quantum: Newtonian (from T00), gravitomagnetic/longitudinal (from P), and comoving TT (from σ₀).

**Proof.** (A1): b_T/δ_c = i(q·Δ_c)/(2|q|²)·ε/(q·Δ_c) = iε/(2|q|²) on (I − q̂q̂), and s·(I − q̂q̂) = −2|q|². With R1 = −s·h and {h,E} = 1, {∫N R1, −i∫E·Ξ_E f} = iN s·Ξ_E f = Nεf. (A2): q·Ξ_h = (q·A_c)/δ_c = ½(q·Δ_c)v·ε/(q·Δ_c) = εv/2 by Lemma J3 (referee-confirmed, `vR16-12:5`); then {∫Kill(ξ)·E, −i∫h·Ξ_h f} = ξ·P f with ∂ → iq. The overall phase of A2 depends on the Fourier sign convention for the smearing. The A1/A2 relative sign that matters is the one R16-12's sign-flip control selects (`recheck/r1612_controls.out` (A)), i.e. the helicity-0 identity, which is the energy-conservation compatibility of the two dressings (§3.3). (A3): from T3's helicity-2 solution B_TT = −2iδ_cσ₀^TT/(ω² − |q|²), A_TT = iωB_TT/2 (`C5_R16-12_report.md:174`), divided by δ_c, against the stationary solution of ḣ_TT = 2E_TT, Ė_TT = −(|q|²/2)h_TT − σ₀^TT f at frequency ω. ∎

**Checked** (`r172_dressing.out:9-13`): over 5 defect modes (S(1.4), G(1.4); |v| from 0.23 to 0.99) and 100 random q̂ each, A1 holds to ≤ 9.0e-16, A2 to ≤ 5.0e-10 (finite-difference floor of v), and all three A3 ratios equal −1 to ≤ 6.4e-8 (1600 TT samples).

**Reading.** The W7 degree-3 tail is Φ_c = {P⁰_c, W_GR}. A true translation commutes with W_GR, so in the continuum Φ ≡ 0. On the lattice the matter momentum shifts a bilinear by q_c + δ_c instead of q_c. **The tail is GR's own field of an edge quantum, transported by the lattice momentum's "fake translation".** This is a plain-words name for R16-8's "defect-Coulomb field": B_c = δ_c × (the Newtonian dressing of ε).

### 3.2 Lemma H: T3 ⇔ "the dressing removes the degree-3 coupling" (proved at leading order; checked)

**Statement.** With H = H_0 + H_int, H_int = Σh·σ₀f (τ = 0, R16-12's (β)):
  {W, H_0} = −H_int + Σ[E_L·r_E + h_T·r_h] f,
where E_L (qq, vL components) and h_T (transverse trace) are the linear-constraint directions, and r_E, r_h are homogeneous of degree −1 with bounded angular factors (1/r² kernels). Hence, to degree 3,
  F⁻¹(H) = H − {H, W} = H_0 + (constraint-proportional terms) ≈ H_0,  and  F⁻¹(P^tot_c) = P⁰_c  (Lemma W).

**Proof.** {E·Ξ_E f, H_0} = −h·(𝒦Ξ_E)f − iωE·Ξ_E f and {h·Ξ_h f, H_0} = E·(𝒢Ξ_h)f − iωh·Ξ_h f. So {W, H_0} = −i[E·(−iωΞ_E + 𝒢Ξ_h) + h·(−iωΞ_h − 𝒦Ξ_E)]f. T3's system (T) at τ = 0, divided by δ_c, states that the E-bracket vanishes modulo L and that the h-bracket equals −iσ₀ modulo T (`C5_R16-12_report.md:161,171-184`). The degrees follow from ωΞ_E and 𝒢Ξ_h both being degree −1. ∎

**Checked** (`r172_dressing.out:18-24`): the non-constraint components of {W, H_0} + H_int are ≤ 8.6e-14 relative (200 q̂ per law). The constraint-proportional coefficients are O(1) and stay bounded as q̂·v → 0 (0.747 and 0.860 at q̂·v from 2.3e-2 to 2.3e-5).

**Consequences.**
- **Correction to R16-12 Lemma W** (`C5_R16-12_report.md:226`, "non-local H′"). The relocated Hamiltonian H′ = H + {W, H_0} is *weakly the free H_0*. Its non-locality sits only in constraint-proportional terms, i.e. in a matter-dependent, non-local lapse and shift. That is the Coulomb-gauge pattern (comparator): a non-local Lagrange multiplier with local physics.
- **Generic GR comparison (rule `TESTS:5705`).** This is GR-generic. At degree 3, the only real processes are single-graviton emission or absorption by a free quantum, which are kinematically forbidden off the Cherenkov cone. So a linear coupling to a free field is removable by a canonical dressing (comparator). The same W with continuum matter does the same in linearized GR.

### 3.3 Corollary: Lemma C is the existence of the comoving field (proved, given 3.1)

- A3's TT dressing has the denominator ω² − |q|². It exists, with bounded angular factor, exactly when the quantum has no active gravitational Cherenkov cone. This matches the referee's corrected condition, "absence of an active Cherenkov zero" (`vR16-12:15`).
- The helicity-0 identity σ_qq = q̂σ₀q̂ (`C5_R16-12_report.md:181`) is the compatibility of the Newtonian and longitudinal dressings with energy conservation, ∂_tT00 + ∂·P = 0 with P = εv. That is generic GR consistency.

### 3.4 Escape 4 × escape 2: a boost without the world-line kernel, at the price of non-local gauge multipliers (suggested)

- **Construction.** Let K⁰_b be the free boost (matter ∫x_bT00 with current-aligned P, so {K⁰_b, H_0} = P⁰_b exactly, Lemma P (`vR16-8:7`); plus the free-graviton boost). F is canonical, so {F(K⁰_b), F(H_0)} = F(P⁰_b) = P^tot_b (degree 3, Lemma W).
- By Lemma H, F(H_0) = H + w̃ with w̃ = Σ C^(1)·λf, constraint-proportional with degree −1 coefficients. Then {F(K⁰_b), H} = P^tot_b − {F(K⁰_b), w̃}. At degree 3, {K⁰_b, w̃} = {K⁰_b, C^(1)}·λf + C^(1)·{K⁰_b, λf}. The first term is the linear-gravity HDA (∝ C^(1)); the second is C^(1) × degree 2. So it is ≈ 0, and {F(K⁰_b), H} ≈ P^tot_b.
- F(K⁰_b) = K⁰_b + {K⁰_b, W}. The symbols of {K⁰_b, W} are q- and k-derivatives of Ξ (Ξ_T = iε/(2|q|²), Ξ_qq = ε(q̂·v)/(2|q|), Ξ_TT ∝ 1/(ω² − |q|²)). **There is no 1/(q·v) in it.**
- **Why this does not contradict Theorem B3.** B3 takes the strong representative H = C_s[1] quasi-local and a covariant lapse-extension C_s[N]. Its rigidity step admits only translation-covariant constraint-proportional additions (`C5_R16-12_report.md:249`).
  - F(K⁰_b) is instead the lapse-moment of F(C⁰_s[N]), whose N = 1 value is H + w̃: weakly H, strongly non-local.
  - Equivalently, it carries **x_b-weighted constraint-proportional singular terms.** Bracketed with H_0, these feed the non-constraint helicity-0 components, because the x_b weight does not commute with the L/T projectors. B3 does not cover them.
  - Restoring a strongly quasi-local C_s[1] with a covariant N-extension brings the obstruction back. So the choice is between B3's world-line kernel and a non-local, field-dependent lapse/shift in the Hamiltonian representative. Physical (gauge-invariant) evolution is the same under H and H + w̃.
- **The open gap (why "suggested").** The boundary terms of the global charges under the singular F are not done.
  - With Ξ_T of degree −2 (a 1/r potential), {∫x_bR1(h), W} is a shell term whose value depends on the ADM boost boundary term.
  - R16-8's degree-2 cancellation of Δ (`C5_R16-8_report.md:199-205`) is itself a shell effect. F changes asymptotic charges (it adds 1/r and 1/r² tails), so it is not a symmetry of the boundary-charge algebra.
  - Until this is done, the construction is a bulk statement.

### 3.5 Escape 2 as registered: the world-line kernel itself

- **Real-space form (proved analytically; checked).**
  - FT⁻¹[PV 1/(q·v)] is a signed line distribution along v. Convolved with the dipole-Coulomb factor (q·Δ_b)/|q|², it gives X(x) ∝ Δ_b·∇G/|v| with G = ∫ds sgn(s)/(4π|x − sv̂|) = asinh(x_∥/ρ)/(2π), where ρ is the distance from the world-line.
  - So |X| ~ (1/r)·cotθ near the line: homogeneous degree −1 in x (−2 in q), with unbounded angular factor. This confirms the referee's correction (`vR16-12:11`).
  - Checked: G to ≤ 2e-6 (truncation L = 1e7) at six points; r|∇G| → cotθ/(2π) to 0.2% at θ = 0.03 (`r172_worldline.out`).
- **Prescription freedom (proved).** As distributions, X_T = 2ib_T[PV(1/ω) + Cδ(ω)] solves the helicity-0 equations for any C, since ωδ(ω) = 0. At exactly ω = 0 the kernel of L gains X_T and Y_vL (`r172_dressing.out:27-29`).
  - The pointwise on-shell solution is Y_qq = −b_T with X_T free. The off-shell solution is Y_qq = +b_T.
  - So the kernel is fixed only up to a δ(q·v) term on the energy shell. ±i0 choices are retarded/advanced world-line integrals. PV is the time-symmetric one.
- **Factorization (proved; checked).** (X_T, Y_qq) = δ_b·(2iΞ_T/ω, Ξ_T). That is b-independent to ≤ 2.8e-14 (`r172_dressing.out:35-36`), so K^sing_b = {P⁰_b, W_K} with W_K the time-integrated (1/ω) Newtonian dressing.
- **Jacobi lemma for {P,K} and {K,K} (proved under stated premises; ker L checked).**
  - *Premises:*
    - T3 ({P_c, H} ≈ 0);
    - escape 2's K with {K_b, H} ≈ P_b;
    - {P_c, P_d}^(3) = 0 (Lemma W);
    - degree-2 closure exact as an operator identity (R12-1/R16-8 local-germ scope);
    - the weak terms are linear constraints times degree-2 structure functions (true for T3's residuals, `C5_R16-12_report.md:103`).
  - *Argument.* Jacobi gives {H_0, R^(3)_cb} ≈ 0 for R_cb := {P_c, K_b} − δ_bcH. So R^(3) lies in the kernel of the weak operator L.
    - For ω ∉ {0, ±|q|}, that kernel is spanned by X_qq, X_vL and Y_T only, all constraint-proportional (`r172_dressing.out:27,30`). So R ≈ 0 there.
    - At ω = 0 the kernel adds X_T and Y_vL. At |ω| = |q| it adds the TT directions, which are absent for |v| < 1.
  - *Conclusion.* {P,K} = δH can fail at degree 3 only by a term supported on the zero-frequency shell q·v = 0, which is exactly where the world-line kernel is undefined.
  - The same argument applies to {K_a, K_b} − J_ab once the rotation-smeared degree-3 completion with {J, H} ≈ 0 is built. It is not built here.
  - **Not evaluated:** the on-shell residual itself (it needs the x_b-weighted brackets). **So escape 2 is not closed.**

### 3.6 Escape 3: degree-4 shell terms (suggested)

- Degree-4 terms enter the degree-3 Killing brackets only through {C^(4)[x_b], ∫R1} or {∫x_bR1, C^(4)[1]}, i.e. through shells, since s·1 = 0 and s·x_b = 0 in the bulk.
- A shell delivers an O(1) degree-3 bulk term E·K′·f only if the degree-4 kernel has an r^{1−d} tail in its gravity argument. Then K′ can be the needed degree −1 term 2b_T, which is bounded-angular, and X_T can be regular.
- But such a kernel makes H^(4) = C_s^(4)[1] non-local, unless the term is of s^T N form, which vanishes in the bulk for N = 1 and N = x_b. In that case it acts only through boundary terms at infinity.
- Reading: escape 3 relocates the world-line kernel either into a non-local H at degree 4 (an (α)-type price) or into asymptotic boundary data. That is the same boundary question as §3.4. **Not closed.**

### 3.7 Escape 5: auxiliary / second-class formulations (suggested)

- The R16-8 referee's constrained elliptic auxiliary (`vR16-8:7`) makes the constraints local. Its multiplier, or equivalently the Dirac bracket after second-class reduction, contains the inverse elliptic operator, so it is non-local.
- This is the same structural statement as Lemma H: locality of the constraints and of the physical Hamiltonian is bought with a non-local multiplier (Coulomb-gauge pattern, comparator).
- A world-line (1/ω) multiplier would be needed only if the auxiliary must also carry the boost bracket in a strong quasi-local representative (as in B3).
- **Not closed** in either direction. No auxiliary was constructed.

### 3.8 (b) Observables and the R13-4 criterion

- **No observable invariant under a completed degree-3 system exists to test,** because no such system exists (§3.4–3.7). This is the expected failure (`TESTS:5782`).
- **What can be said (proved within scope).**
  1. **The β-frame local curvature.** R^(1)(h)[g_x] is local, and under the quasi-local (β) H it evolves causally. On S/G laws v_max < 1 and the graviton has speed 1; this is a Lieb–Robinson reading. But it is **not invariant**: δ_ξR = R[ξ_cB_c∗Ô_c], which is non-zero at distance r from any edge quantum, falling as 1/r⁴ (`vR16-8:5`). By §3.1 this failure is exactly the lattice mismatch δ_c acting on the Newtonian tidal field. It vanishes on the box algebra (Lemma S scope).
  2. **The dressed curvature.** O_F := F(R^(1)(h)) = R^(1)(h − h^GR[matter]), the curvature of the metric minus the matter's own comoving linearized-GR field. It is invariant under the bulk constraints F(C^(1) + grav2) at degree 2 (Lemma D). Under F(H_0) ≈ H it evolves as a free graviton field (Lemma H), so **at degree 3 it does not respond to matter at all, at any distance.** Bounded functions of the smeared O_F (Weyl operators) are bounded.
     - But O_F is non-local in the bare variables, through h^GR (1/r Newtonian and TT near-field).
     - That non-locality is the GR-generic Dirac dressing. The same O_F in continuum linearized GR has the same equal-time power-law commutators with distant matter (Donnelly–Giddings, comparator).
- **Physical-control rule (`TESTS:5702`).**
  - R13-4's equal-time-commutator test applied to Dirac-dressed operators reports power-law non-locality in ordinary linearized GR. So it is **not a valid physical control** for gravity.
  - The right control is the retarded response of a gauge-invariant curvature to a local source in continuum linearized GR, which is causal (comparator). The lattice model must then be tested on the same observable. This needs (1) a fixed readout bridge and (2) completed constraints. Neither exists. Not run.
- **Readout bridge (rule `TESTS:5703`; `AX:82-83`).** "Only records are readable" selects which algebra is physical, but no bridge from records to either R^(1)(h) or O_F is supplied.
  - If physical readouts are bare-local (site records), the candidate responder is R^(1)(h). It is causal but not invariant when edge quanta exist anywhere.
  - If they are dressed (relational), O_F is invariant and non-responsive at degree 3.
  - Lemma W (`vR16-12:13`) and §3.1–3.2 make this choice the whole question.

### 3.9 (c) Size (reading, conditional)

- **Input.** Edge-quantum energy infimum 1.431782/a = 1.748e19 GeV at a = ℓ_P, m = 0.3 (`vR16-12:19`); a = ℓ_P is itself open (`AX:189-190`).
- **Thermal occupation e^{−ε/T}, no subtraction** (`r172_population.out`):
  - log₁₀ = −3.23e31 at T_CMB (2.348e-13 GeV);
  - −7.59e15 at 1 TeV;
  - −759 at 1e16 GeV.
- **Caveats.**
  - These numbers hold only for a thermal ensemble. Number-conserving matter can keep any initial edge population (`vR16-12:19`).
  - No response amplitude is stated, because no responder exists (§3.8). R16-8's per-quantum kernel factor at 1 m, ≲ 4e-70 in Planck units (`C5_R16-8_report.md:273`), is a reading for a response that has not been shown to exist.
- **Self-force on a moving compact body (rule `TESTS:5696`).** For a single free edge quantum at degree 3, the self-force is zero: by Lemma H the dressed dynamics is free (proved within the bulk scope). For a bound compact body it needs degree 4 (binding). Not computed.

### 3.10 (d) Lemma W's question: removable or relocated?

- **Bulk, degree 3 (proved at leading order).**
  - The relocation map is GR's own dressing (§3.1).
  - Under it, compact-smearing constraints lose their matter terms at degree 2. The (β) Hamiltonian becomes free plus constraint-proportional terms (§3.2).
  - So the tail is **removable from the physical Hamiltonian and from the bulk gauge generators, into non-local gauge multipliers.** This is the Coulomb-gauge situation, not physical non-locality.
  - The price: physical observables are the GR-dressed ones, as in GR.
- **Global charges (suggested; boundary bookkeeping not done).**
  - The lattice-specific content survives only as Φ_c = {P⁰_c, W} ≠ 0: the asymptotic momentum of a dressed edge quantum is its lattice momentum, which is not a translation. So the asymptotic Poincaré algebra needs boundary cross terms (R16-8 Lemma F) or fails by the edge defect Δ.
  - Reading: that is lattice-scale Lorentz violation of edge quanta (already present in their dispersion), carried by boundary charges. It is not a bulk instantaneous interaction.
- **Not settled.**
  - Whether the boundary-charge choice is physical. That needs a readout bridge for global charges (`AX:82-83`) and the ADM terms for the singular F.
  - Degree ≥ 4. There F⁻¹(H) acquires the instantaneous Newtonian and gravitomagnetic interaction. In GR it is compensated by the TT sector; here this is unchecked with lattice ω = q·v(k).

### 3.11 (e) Prices (named, not adopted)

| price | content | axiom touched | buys |
|---|---|---|---|
| **P-W7mult (new)** | Non-local, matter-dependent lapse/shift (constraint-proportional, degree −1 kernels) in the Hamiltonian representative, F(H_0) = H + w̃. Replaces B3's world-line kernel (§3.4) | none directly; dynamics downstream (`AX:116-130`); gauge only if the readout bridge is relational | boost bracket at degree 3, bulk (suggested) |
| **P-W7bdy (new)** | Asymptotic Poincaré charges with gravitational boundary cross terms (R16-8 Lemma F), or accept edge-quantum Lorentz violation in the global algebra | none directly; a readout bridge for global charges (`AX:82-83`) | {P,K} at degree 2–3 |
| **P-W7ro (new)** | A readout bridge fixing the physical observable algebra (bare-local vs GR-dressed) | `AX:82-83` (readout), `AX:187` (source/observable gate) | decides (b)/(d) |
| P104 (R16-12 P-W7K) | Unchanged, but now one of two options; P-W7mult is the other | `AX:57-61` | — |
| P105, P106, P50, P98, P99 | Unchanged. P106 is restated as "comoving field exists" (§3.3) | as S20 | — |

---

## 4. Against the FIXED readings (`TESTS:5779-5781`)

- **LOCAL-EQUIVALENT: not met.**
  - There is no closed degree-3 completion. The boost brackets {P,K} and {K,K} are reduced to an on-shell condition (§3.5) but not evaluated.
  - The dressing-based boost (§3.4) leaves the boundary bookkeeping open.
  - The invariant observable O_F (§3.8) does not respond at degree 3, but it is invariant only under the bulk degree-2 constraints, not under a completed degree-3 system.
- **PHYSICALLY NON-LOCAL: not met.** No bounded constraint-invariant observable responding instantaneously is constructed. The only candidate responder, R^(1)(h), is not invariant. The invariant O_F does not respond.
- **Worker reading: OPEN.**
- **Against the expectation** ("PHYSICALLY NON-LOCAL in principle and unobservable in practice, or OPEN"; `TESTS:5782`):
  - OPEN, as expected, for the expected reason (no invariant observable at this order).
  - The new results (§3.1–3.2) point the other way from "non-local in principle". In the bulk at degree 3, the tail is GR's dressing transported by a non-translation, and it is removable into gauge multipliers.
  - What is left is a boundary-charge (asymptotic Poincaré) statement about edge quanta. That is "relocated to infinity", not "physical in the bulk". This is suggested, not proved.
  - Population suppression agrees (reading).

## 5. Strong-word and rule check

- **"Proved":** Lemma D (A1–A3), Lemma H, the Lemma C corollary, the real-space kernel, the prescription freedom, factorization, and the Jacobi lemma under its premises. All are leading order in q (H-lead), free number-conserving S/G matter, unrefereed. Lemmas D and H hold for bulk smearings (q ≠ 0). Global (Killing) statements inherit R16-12's scope.
- **"Exactly":** s·Ξ_E = −iε and q·Ξ_h = P/2 (algebraic, given T3 and J3), and the ratio −1 in A3. All at leading order.
- **"Suggested":** §3.4 (boost via F), §3.6, §3.7, and §3.10's global-charge reading.
- **"Free" / "removable":** always "weakly, at degree 3, in the bulk, at leading order".
- **Round-17 rules.**
  - v_max for every law, including the graviton (§1).
  - Self-force (§3.9).
  - Ward/HDA: the standard target throughout. The weak closure and the non-local multipliers are named as deformations or gauge choices (§3.2, §3.4).
  - Counting conventions and Λ enforcement: not applicable.
  - Physical controls (§3.8): no control was run, and the equal-time criterion is shown not to be a gravity control.
  - Readout bridge (§3.8, §3.10): named as missing.
  - Forks: "world-line kernel vs non-local multiplier" (§3.4) is **not exhaustive**. It excludes non-covariant N-extensions (excluded by translation covariance), non-local strong H (P98), auxiliaries (§3.7) and deformed HDAs.
  - Generic GR comparison: §3.1–3.3 are GR-generic. §3.10's boundary residue is model-specific.
  - Changed hypothesis: B3's strong quasi-local representative with only translation-covariant constraint-proportional freedom is removed. x_b-weighted constraint-proportional (non-local multiplier) terms are allowed.
- **Numbers:** |q| = 1e-3 in (A) and |q| = 1 in (B)–(D), legitimate because the leading symbols are homogeneous. Finite-difference floor about 1e-8 (A2, A3). Nothing is subtracted anywhere except in the definition of O_F, which subtracts h^GR by construction.
- **Not claimed:** non-Killing degree-3 completions beyond the dressing-defined ones; the ADM boundary terms; degree 4; any physical (Dirac-observable) non-locality or locality certificate.

## 6. For the referee

1. **Lemma D.** Check A1–A3 signs and normalizations, especially that one W solves both linear constraints with the same sign. Also check that the TT part is the comoving field (ratio −1) rather than its negative relative to the Newtonian part.
2. **Lemma H.** Is "T3 ⇔ {W, H_0} ≈ −H_int" correct, and does it overturn R16-12's "non-local H′" (`C5_R16-12_report.md:226`) into "free H_0 plus constraint-proportional"?
3. **§3.4.** Is B3's rigidity gap real, i.e. can x_b-weighted constraint-proportional singular terms feed the helicity-0 equations? Can the boundary terms of F be made consistent with R16-8's shell cancellation?
4. **Jacobi lemma (§3.5).** Are the premises (first-class at the order, exact degree-2 closure) acceptable at R12-1's local-germ scope?

## 7. Files (all in `S/`)

- `scripts/r172_dressing.py` / `.out`: (A) lines 9-13; (B) 18-24; (C) 27-31; (D) 35-36.
- `scripts/r172_worldline.py` / `.out`: the line integral G and the cot θ growth.
- `scripts/r172_population.py` / `.out`: Boltzmann exponents (ε = 1.431782 × 1.22089e19 GeV).
- `scripts/r1612_lib.py`, `scripts/sublum_copy.py`: R16-12's solver and R14-1's symbols, unmodified.
- `recheck/`: five archived runners with byte-identical regenerated outputs; `*.out.archived` are the archive copies.
