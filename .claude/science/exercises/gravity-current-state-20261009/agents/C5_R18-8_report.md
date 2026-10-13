# C5 R18-8 report: W7 at infinity. Does the off-box tail survive in the global Poincaré charges, and is that observable?

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). **Unrefereed.** Ran 2026-10-13 02:48Z to about 03:15Z. No repository file was edited. No downloads, no web lookups; every literature item is RECALLED.

**Scratch.** `S/` = `.../scratchpad/C5/R18-8/`. Every script runs in under 5 s at `OMP_NUM_THREADS=2`.
- `S/scripts/r188_vlasov_algebra.py` / `.out`: (A) symbolic check of every degree-2 Killing-charge bracket, generic separable band.
- `S/scripts/r188_quantum_ring.py` / `.out`: (B) the anomaly identity for genuine lattice operators on a ring.
- `S/scripts/r188_surface.py` / `.out`: (C) the tail's ADM boost surface integral; Lemma T; Newtonian control.
- `S/scripts/r188_observable.py` / `.out`: (D) boost orbits, far-field mass, composite bodies, closure rank, sizes.
- `S/scripts/sublum_copy.py`, `S/scripts/r1612_lib.py`: R14-1's symbols and R16-12's solver, unmodified copies.
- `S/recheck/`: the archived R16-8, R16-12 and R17-2 runners, rerun.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `TESTS`, `SUMMARY` are in `P/`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md` (read in full). `vX` = `P/agents/C5_X_referee_verdict.md`, `refX` = `P/agents/C5_X_referee.md`.

**Read.** `AX` in full; `TESTS:2302-2320` (C5 method and readings), R12-1 (`:4335-4348`, verdict `:4477-4485`), R13-4 (`:4644-4664`, verdict `:4771-4777`), R16-8 (`:5339-5358`, `:5514-5525`, verdict `:5587-5591`), R16-12 (`:5529-5549`, `:5654-5665`, verdict `:5900-5906`), R17-2 (`:5749-5783`, `:5987-5997`, verdict `:6167-6170`), this item (`:6749-6778`); `SUMMARY:397-413` (§17 root obstruction); `C5_R17-2_report.md`, `vR17-2`, `refR17-2`; `C5_R16-12_report.md`, `vR16-12`, `refR16-12`; `C5_R16-8_report.md`, `vR16-8`, `refR16-8`, all in full.

**Rechecks (before use).** The eight archived runners (`r168_jets`, `r168_kernel`, `r1612_degree3`, `r1612_controls`, `r1612_population`, `r172_dressing`, `r172_worldline`, `r172_population`) were copied to `S/recheck/`, their `.out` files moved aside, and rerun (exit 0 each). Every regenerated `.out` is byte-identical to the archive (`cmp`). R17-2's `r1612_lib.py` is identical to the head of R16-12's `r1612_degree3.py`; the three `sublum_copy.py` files are identical. (`timeout` is absent on this machine; no run used it.)

**Labels.** proved = complete under stated hypotheses, unrefereed; checked = numerics here; suggested = argued, not proved; reading = interpretation; comparator = literature, RECALLED.

---

## 0. In plain words

1. **The tail does not hide the defect at infinity; it carries it there.** The asymptotic (ADM) Poincaré charges of a system with edge quanta do **not** satisfy the Poincaré algebra. The failure is exactly the defect charge: {K_b, P_c} = δ_bc E + Q_D,cb, with Q_D,cb = Σ_k ε(k)(∂_bP_c(k) − δ_bc) n_k (proved; checked).
2. **No completion can change this at leading order.** The failure sits at degree 2 (κ²Q_D in R16-8's normalization). At that degree the asymptotic charges are just the matter and free-graviton charges, because the linear (degree-1) parts of the Killing-smeared constraints vanish identically. The gravitational completion is degree ≥ 3 and cannot enter (proved).
3. **Why R16-8's Lemma F looked like a cancellation.** The same shell term at infinity does two jobs. In the regulated (compact-lapse) constraint bracket it cancels the matter defect; that is what makes the bulk constraints first class. In the boost *charge*, which is the constraint plus its surface term, it is read with the opposite sign and reproduces the defect. Bulk closure and boundary anomaly are one statement (proved).
4. **Seen from infinity, the tail is a mass dipole.** Up to a linearized gauge transformation, the tail field of a point defect is exactly the Newtonian field of a mass dipole M·a = −Δ (proved; checked to 1e-17). So no boundary term built from the metric can tell the tail apart from a real displacement of energy. The anomaly cannot be removed by changing surface terms (proved in the stated class).
5. **At degree 3 the anomaly is the dressed defect charge.** In R17-2's dressed presentation the degree-3 correction is {Q_D, W}, i.e. the anomaly through degree 3 is F(Q_D). This is proved by the Jacobi identity, conditional on the boundary admissibility of R17-2's singular dressing (the gap its referee flagged). In the world-line presentation an extra term with a 1/(q·v) kernel appears; it is not evaluated.
6. **Observable form.** The far-field mass M² = E² − |P|² of a body with edge content depends on its velocity relative to the lattice frame: M(V) = M[1 − Q_D,bb V_b²/(2(E + Q_D,bb)) + O(V⁴)], anisotropic through the axis b (proved from the algebra; checked on composite bodies to 1e-3 or better). Bodies without edge content have exactly velocity-independent M.
7. **Size.** Edge quanta cost ≥ 1.40/a to 1.43/a (1.7e19 GeV at a = ℓ_P). For thermal populations the effect is ≤ 10^(−3.2e31) at T_CMB, 10^(−7.4e15) at 1 TeV, 10^(−733) at 1e16 GeV, and still ≤ 1e-8 at 1e18 GeV (Earth's CMB speed). A primordial relic population is not fixed by the theory (number conservation) and is not bounded here.
8. **Reading (worker): ANOMALY, pending referee.** This matches the expectation. It is not a new effect: it is the edge quanta's lattice Lorentz violation (SUMMARY §17's root, count once), now shown to survive intact into the asymptotic charges.

---

## 1. Hypotheses and classes (stated before any title)

- **H-R17 (setting, as registered `TESTS:6757-6762`).** R16-8/R16-12/R17-2's completion: R12-1's ansatz with R16-8's Lemma-P placement, R16-12's T3 translation repair, and R17-2's dressing W. Free, number-conserving, one-band separable matter in d = 3. Linearized gravity with asymptotically flat falloff (h ~ 1/r with even leading part, E ~ 1/r²). Degree 3 in the Killing sector. Excluded: nonlinear gravity, pairing, P90.
- **Laws and whole-zone v_max (refereed, `vR16-8:15`).** S(1.4): 0.99270; G(1.4): 0.99386; m = 0.3. Graviton: continuum symbol at leading order, v = 1. The L-box is not used.
- **H-mat.** Current-aligned momentum P = ∂(ε²/2) = εv (R16-8 Lemma P); defect Δ_cb = ε(∂_bP_c − δ_bc), diagonal for separable bands (R16-8 `C5_R16-8_report.md:33`; `r188_vlasov_algebra.out`). Q_D,cb := Σ_k Δ_cb(k) n_k, the forward (q = 0) defect charge.
- **H-lead.** Matter charges in leading (Vlasov / Lie–Poisson) form: a charge ∫a(x,k)f with {∫af, ∫bf} = ∫{a,b}f and {a,b} = ∂_xa·∂_kb − ∂_ka·∂_xb. The one-body identities are also checked as exact lattice-operator identities (§3.1, ring check).
- **Poincaré values (this bracket convention).** {K_b,H} = P_b; {K_b,P_c} = δ_bcH; {K_a,K_b} = −J_ab; {J_ab,P_c} = δ_acP_b − δ_bcP_a; {J_ab,K_c} = δ_acK_b − δ_bcK_a; {P,P} = {P,H} = {J,H} = 0.
- **H-charge (the global charges).** The asymptotic charges are the *improved* (differentiable, Regge–Teitelboim) generators with Killing smearings: H = C_s[1], P_c = C_j[e_c], K_b = C_s[x_b], J = C_j[ω×x], with every derivative moved onto the smearing. On shell they equal the ADM surface integrals; in particular K_b ≈ K_∂b := −S_b[h], S_b[h] = ∮[x_b(∂_jh_ij − ∂_ih_kk) − (h_ib − δ_ibh_kk)]n_i dS = ∫x_bR1(h) (comparator: Regge–Teitelboim; Beig–Ó Murchadha, RECALLED). The *unimproved* generator ∫N(R1(h) + T00 + …) with N = x_b is weakly zero.
- **H-reg.** The regulated lapse N_R = x_b w(|x|/R) of R16-8 Lemma F (`C5_R16-8_report.md:199-206`; scope corrected at `refR16-8:69-77`: localized sources, R → ∞).
- **Not covered:** lattice-momentum gravitons (the R9-9 graviton symbol is used only at leading order, where it is the continuum one; a lattice graviton band would add its own Q_D of the same form); non-Killing smearings beyond what is cited; the ADM boost term of the singular canonical map F as a convergent functional (named as the open condition of §3.5); the world-line presentation's q·v = 0 shell; degree ≥ 4; interacting or pair-creating matter; qubit gravity; Λ.

## 2. Prior art (each counted once)

1. **R16-8 and verdict.** Tail kernel B = sD/|s|², 1/r² with Bianchi-fixed 1/r⁴ curvature (`vR16-8:5`). Lemma F: the regulated JS bracket gets −κ²Q_D from the cutoff shell, "Consequence: the completion cancels the matter's Poincaré defect … by a term supported at infinity" (`C5_R16-8_report.md:199-206`); referee: a boundary-limit identity, "not evidence of physical action at infinity" (`refR16-8:69-77`).
2. **R16-12 and verdict.** T3/J3 weak translation repair; Lemma W: Φ_c = {P⁰_c, W}; B3 a bounded-angular, presentation-dependent obstruction (`vR16-12:5-13`). Population floor 1.431782/a (`vR16-12:19`).
3. **R17-2 and verdict.** Lemma D: W is the inverse of one particular linearized-GR Coulomb/comoving dressing; Lemma H: {W, H₀} = −H_int + constraint terms (`vR17-2:5-7`). The B3 gap is real but the ADM boost boundary algebra is unconstructed (`vR17-2:9`). The Jacobi reduction assumes exact lower-order closure, which is absent (`vR17-2:11`; `refR17-2:69-85`). R17-2's suggested reading: what is lattice-specific is relocated to the global Poincaré charges (`C5_R17-2_report.md:172-184`); P-W7bdy (`:191`).
4. **R12-1 verdict.** Only local-germ necessity; exact degree-2 operator closure not established (`TESTS:4477-4485`).
5. **SUMMARY §17** (`SUMMARY:397-413`): the root obstruction; a periodic band integrates its Hessian to zero, so the zone-averaged anomaly is −β.
6. **R16-8 §3.8 / P-pf1.** Sawtooth (SLAC) matter removes the Killing defect off the zone face (`vR16-8:13`).
7. **Comparators (RECALLED).** Regge–Teitelboim improved generators; Brown–Henneaux theorem (the charge algebra is a central extension of the asymptotic symmetry algebra *when the bulk algebra closes for the asymptotic smearings*); Beig–Ó Murchadha Poincaré charges; Newtonian mass dipole = centre of energy; Bloch oscillation under a uniform force.

---

## 3. Results

### 3.1 Theorem A: the degree-2 asymptotic algebra (proved; checked)

**Statement.** Under H-R17, H-mat, H-lead and H-charge, for *every* completion whose added terms have total degree ≥ 3 (gravity degree ≥ 1, matter bilinear degree ≥ 2), the asymptotic charges satisfy, through degree 2:
- {K_b, H} = P_b, {K_a, K_b} = −J_ab, {P, P} = {P, H} = {J, H} = 0 (closed);
- **{K_b, P_c} = δ_bc H + Q_D,cb**;
- {J_ab, P_c} = δ_acP_b − δ_bcP_a + ∫(v_bΔ_ca − v_aΔ_cb)f;
- {J_ab, K_c} = δ_acK_b − δ_bcK_a − ∫(x_aΔ_bc − x_bΔ_ac)f;
- {J_ab, J_cd} = Poincaré + a defect bilinear in (x, v, Δ).

All defect terms vanish on states with no defect-carrying quanta.

**Proof.**
1. The degree-1 parts of the improved Killing charges vanish identically: ∫(sᵀx_b)·h = 0 and ∫(sᵀ1)·h = 0 (second differences of affine functions, also for lattice differences); ∫Kill(e_c)·E = 0 and ∫Kill(ω×x)·E = 0 (Killing vectors).
2. So the degree-2 part of any bracket of two Killing charges is {Q^(2), Q′^(2)}: the free-graviton charges (continuum symbol; Poincaré) plus the matter charges H_m = ∫εf, P^m = ∫Pf, K^m = ∫x_bεf, J^m = ∫x×P f. Any completion term has degree ≥ 3, and its bracket with a degree-1 piece would be needed to reach degree 2; those pieces are zero.
3. The matter brackets are pointwise symbol identities, e.g. {x_bε, P_c(k)} = ε∂_bP_c = δ_bcε + Δ_cb, and {x_bε, ε} = ε∂_bε = P_b. ∎

**Checked.**
- `r188_vlasov_algebra.out`: every listed identity holds symbolically for a generic separable band ε² = m² + Σu_i(k_i). Negative controls (dropping Δ, flipping a sign) fail as they should. The continuum control u_i = k_i² gives Δ ≡ 0.
- `r188_quantum_ring.out`: on a ring of 2048 sites, with K = ½(Xε + εX) and Gaussian packets (width 24 sites), [K,P] = i(H + Q_D) holds as an operator identity on the packet to ≤ 2.6e-13 relative for every sampled carrier except the G(1.4) zone corner (5.9e-7, where both sides nearly vanish because εP′ → 0). [K,P] = iH fails by O(1) on edge packets: relative residual 1.1 for S(1.4) at k = 1.6, where ⟨Q_D⟩ = −27.1. It holds to ≤ 2.6e-13 on box and mirror-box packets, where ⟨Q_D⟩ ≤ 1e-28. [K,H] = iP holds to ≤ 6e-12, except at the same G(1.4) corner (≤ 6.8e-4 relative).

**Remarks.**
- **The plateau.** On box states the algebra closes exactly, and so does every nested bracket. Δ vanishes on the open box, and K acts on k as the first-order operator ε∂_k, so K never moves a box-supported state's support (proved).
- **The zone-mean root** (SUMMARY §17): ∮(∂_cP_c − 1)dk_c = −2π for continuous periodic P, so Q_D cannot vanish on every state of any continuous one-band law. And {K,H} = P forces P = ∂(ε²/2) once K = ∫x_bεf. (Proved; count once with §17.)

### 3.2 Lemma S∞: one shell term, two roles (proved; checked)

**Statement.** Let the completion close the regulated JS bracket (R16-8/R12-1 design): {P^tot_c, C_s[N_R]} ≈ −δ_bc C_s[1], with the tail's shell contribution cancelling the matter defect. Then the tail's contribution to the boost *charge* is {Φ_c, K_∂b} = +(matter defect), with the same sign as the defect, not the opposite. Hence:
- the surface-charge computation of {K_∂b, P^tot_c} gives δ_bc E (from translating the Newtonian field) plus Q_D,cb (from the tail);
- the bulk improved computation of Theorem A gives the same result.

**Proof.** For a localized source inside the plateau of N_R, R1 of the tail field is supported at the source. So ∫N_R R1(tail) = ∫x_b R1(tail) = S_b[tail], independent of R. The regulated constraint's gravity part is ∫N_R R1(h), and its bracket with Φ_c equals −(matter defect) by design. K_∂b = −S_b[h], so {Φ_c, K_∂b} = −{Φ_c, ∫N_R R1(h)} = +(matter defect). The translation part of P^tot moves the Newtonian field and shifts K_∂ by δ_bcE. ∎

**Checked** (`r188_surface.out`, analytic kernel of `C5_R16-8_report.md:175`, point defect Δ = diag(−6.91, −0.085, −39.2)):
- R1(B) = 0 off source (≤ 3.4e-17);
- S_b[B_c] = Δ_cb to 1e-10 on spheres of radius 0.5, 3 and 50 (R-independent);
- Newtonian control: S_b[h_N] = −M a_b to 1e-8 at R = 5 and 50.

**Consequences (corrections to prior wording).**
- **R16-8 Lemma F's "Consequence"** (`C5_R16-8_report.md:204`) holds only for the regulated constraint generator, which is weakly zero. In the charge algebra the same shell term carries the defect. The constraint algebra closes *because* the boundary charges inherit the anomaly. This sharpens `refR16-8:69-77`.
- **Brown–Henneaux does not apply.** Its hypothesis, bulk closure for the asymptotic smearings, fails: {C_j[e_c], C_s[x_b]} has the Q_D term. That is why a non-central anomaly is possible.

### 3.3 Lemma T: the tail at infinity is a mass dipole (proved; checked)

**Statement.** For a point defect Δ_cb (fixed c), B_c = Kill(ζ) + δ_ij φ_d exactly on ℝ³∖{0}, with φ_d = −(Δ_cb/8π)∂_b(1/r) and ζ_i = ∂_i(∂_b r)Δ_cb/(32π). This is the Newtonian field of a mass dipole M a_b = −Δ_cb.

**Proof.** In B = ½[∂_i∂_j∂_b r/(8π) − δ_ij∂_b(1/(4πr))]Δ_cb, the first term is ∂_i∂_j(∂_b r)/(16π) = Kill(ζ). The second is δ_ijφ_d. ∎

**Checked** (`r188_surface.out` (4)): the linearized Ricci tensor of B − δφ_d is ≤ 3.5e-17 at random off-source points, against max|Ric(B)| = 0.13, 8.3e-5 and 5.8e-2 for the three c. r⁴|Ric(B)| is constant along a ray from r = 2 to r = 200.

**Corollary N (no boundary repair; proved in the stated class).** Consider surface functionals of h that are linear and invariant under linearized spatial gauge transformations with decaying ζ (ζ here falls as 1/r). Every such functional responds to the tail exactly as to a displacement of the body's energy by −Q_D/E. So no such boundary term can be added to K to cancel Q_D in {K,P} while still reading the energy dipole. Not covered: E-dependent or nonlinear boundary terms, and non-gravitational redefinitions. P-pf1's change of the matter momentum is such a redefinition (§3.7).

**Corollary N′ (no matter-moment repair; proved).** Try K′_b = K_b + ∫x_b g_b(k) f with g_b continuous and periodic (separable band).
- {K′_b, P_b} = δ_bbH requires εP_b′ + g_bP_b′ = ε, i.e. g_b = ε(1/P_b′ − 1).
- That is singular wherever P_b′ = 0. Such zeros exist on every continuous periodic band, since ∮P_b′dk_b = 0 and P_b′ = 1 on the box.
- Independently, {K′_b, H} = P_b + ∫g_b v_b f ≠ P_b, so the centre-of-energy theorem is lost.
- This is SUMMARY §17's obstruction again (count once).

### 3.4 What the asymptotic algebra fails by (probe (b))

- **Through degree 2, in every presentation** (Theorem A): {K_b,P_c} − δ_bcH = Q_D,cb. The rotation brackets fail by the moments ∫vΔ f and ∫xΔ f. {K,H} and {K,K} close.
- **Not a central or redefinable term.** Δ(k) is not in span{1, ε, P_b} on the zone: the relative least-squares residual is 0.86 (S) and 0.48 (G) (`r188_observable.out` (D3)). So Q_D is neither a central charge (∝ particle number) nor a recombination of E and P.
- **The generated algebra grows.** The numerical rank of {1, ε, P, (ε∂)P, …, (ε∂)⁶P} rises by one per bracket, 4 → 9 (checked; derivative noise not controlled, so "never closes" is only suggested). The algebra generated by the asymptotic charges is not finite-dimensional on edge content. On the box it is Poincaré.

### 3.5 Degree 3 (probe (a): the surface terms of W)

**What W's surface terms do (proved, given Lemma D, q → 0).** W's A1/A2 identities (s·Ξ_E = −iε, q·Ξ_h = P/2; `C5_R17-2_report.md:60-61`) are q-independent. Through Gauss's law, the dressing's asymptotic field carries:
- monopole E_∂ = H_m (from the Newtonian part);
- boost dipole K_∂ = ∫x_bT00 (from the Newtonian part);
- gravitomagnetic monopole P_∂ = P⁰ (from the Ξ_h part).

So W's surface terms convert the bare matter charges into the ADM charges. By canonical covariance, the ADM algebra is then the bare lattice algebra.

**Theorem A3 (proved by the Jacobi identity; conditional on boundary admissibility).**
- **Setup.** Write the degree-3 boost as K^(3)_b = {K⁰_b, W} + Y_b. Use Φ_c = {P⁰_c, W} (Lemma W) and {H₀, W} = H_int − w̃ (Lemma H, w̃ constraint-proportional).
- **Steps.** The degree-3 anomaly is
  A^(3)_cb = {K^(3)_b, P⁰_c} + {K⁰_b, Φ_c} − δ_bcH_int.
  Since ad_W is a derivation, this equals {{K⁰_b, P⁰_c}, W} + {Y_b, P⁰_c} − δ_bcH_int.
  Substituting {K⁰_b, P⁰_c} = δ_bcH₀ + Q_D,cb gives
  **A^(3)_cb = {Q_D,cb, W} + {Y_b, P⁰_c} − δ_bc w̃ ≈ {Q_D,cb, W} + {Y_b, P⁰_c}.**
- **Dressed presentation (P-W7mult; Y = 0).** The same steps give {K,H}^(3) = Φ_b + {K⁰, w̃} ≈ P_b^(3), so Y = 0 is consistent. Then **the anomaly through degree 3 is F(Q_D) = Q_D + {Q_D, W}**, the defect charge of the dressed matter.
  - The symbol of {Q_D, W} is (q·∂_kΔ)·Ξ. It has degree −1 (a 1/r² kernel) with a bounded angular factor for subluminal S/G.
  - Suggested size: the gravitational-potential correction to Q_D, of relative order GM/(Rc²).
- **World-line presentation (B3).** Y_b ⊃ K^sing_b = {P⁰_b, W_K} (R17-2's factorization). Then {Y_b, P⁰_c} = −{P⁰_b, {P⁰_c, W_K}} carries δ_bδ_c Ξ_T/ω, which is singular on q·v = 0. **Not evaluated.** This is R17-2's open shell, now seen to sit inside the degree-3 anomaly rather than to decide closure.
- **Condition.** The identities use the Jacobi identity for {K⁰, W}, i.e. a convergent ADM boost term for the singular F. That is the gap flagged at `vR17-2:9`. It is not closed here.
- **Correction to R17-2's Jacobi lemma** (`C5_R17-2_report.md:116-126`). Its premise "degree-2 closure exact" fails for the global charges (Theorem A). The corrected statement is {H₀, A^(3)} ≈ −{H_int, Q_D}. A particular solution is {Q_D, W}: {H₀,{Q_D,W}} = {Q_D, H_int} − {Q_D, w̃} (proved, using {H₀,Q_D} = 0). So the degree-3 failure is not confined to ker L or to the q·v = 0 shell. R17-2's q·v = 0 localization applies only to the part beyond F(Q_D).

### 3.6 Probe (c): observable form and size

**Frame-dependent far-field mass (proved from the algebra; checked).**
- **Derivation.** Along the orbit of K_b from a rest frame (P = 0), using {K_b,E} = P_b and {K_b,P_c} = δ_bcE + Q_D,cb:
  - d²(E² − P²)/dη² = −2(E + Q_D,bb)Q_D,bb;
  - the centre-of-energy velocity is V = P/E = (1 + Q_D,bb/E)η;
  - hence **M(V) = M[1 − Q_D,bb V_b²/(2(E + Q_D,bb)) + O(V⁴)]**, and to first order in Q_D/M, δM/M = −V·Q_D·V/(2M).
- **Checked** (`r188_observable.out` (D2)), composite bodies of 80 box quanta plus 2 or 8 edge quanta (pairs ±k, so P = 0):
  - d²M²/dη² matches the prediction to 2e-3 (S) and 8e-5 (G);
  - at η = 0.002, δM/M matches to ≤ 1e-3 (S) and ≤ 1e-4 (G);
  - V matches (1 + Q/E)η to ≤ 1.1e-3 (S) and ≤ 3e-5 (G);
  - **controls:** boosts along an axis where all quanta are in the box give δM/M ≤ 3e-16, and box-only bodies give ≤ 3e-16 on every axis.
- **Signs and extremes.** When Q_D,bb < −E (the S strip; Q_D,bb/E = −1.70 for the 2-edge body), the boost reverses the body's velocity: V = −1.40e-3 at η = +0.002. The far-field mass of a single quantum, E² − P² = ε²(1 − v²), is the lattice dispersion read at infinity (`r188_observable.out` (D1)).
- **Reading.** This is the edge quanta's own Lorentz violation, seen by far fields. It is not a bulk instantaneous interaction.

**Compact boost (proved; checked).**
- On a single quantum, K_b generates dk_b/dη = ε(k) > 0 on a circle. So the orbit is periodic, with period ∮dk/ε: 9.43 (S) and 6.22 (G) at m = 0.3.
- Boosting a quantum past the edge brings it back through the zone (a Bloch-oscillation-type orbit). After one period the state returns to (E, P_b) = (0.3, 0) to 3e-12.
- Reading: on the lattice the asymptotic "rapidity" of a single quantum is compact. On box states, a boost of rapidity up to asinh(b/m) (≈ 2.25 at m = 0.3) is exactly Lorentzian.

**Size (reading; a = ℓ_P is open, `AX:189-190`).**
- **Inputs.** Edge floor 1.400/a (m = 0) to 1.431782/a (m = 0.3), i.e. 1.709e19 to 1.748e19 GeV (`vR16-12:19`). Per quantum and axis, |Q_D,bb|/ε = |P_b′ − 1| ≤ 18.84 (S) and 3.35 (G) over the whole zone (checked, `r188_observable.out` (D4a)); 40 is used as a ceiling.
- **Thermal edge fraction** (Boltzmann factor with an x³ phase-space allowance; `r188_observable.out` (D4)): log₁₀ ≤ −3.2e31 at T_CMB, −7.4e15 at 1 TeV, −733 at 1e16 GeV, −3.7 at 1e18 GeV.
- **Effect at the Earth's CMB speed** (V = 1.23e-3): log₁₀|δM/M| ≤ −3.2e31, −7.4e15, −737, and −8.2 respectively.
- **Relic population.** Number-conserving matter can carry any initial edge population (`vR16-12:19`). For an edge energy fraction f, δM/M ≈ −f⟨P′ − 1⟩V²/2. No observational bound is computed here.
- **Subtractions.** None anywhere.

### 3.7 Probe (d): prices (named, not adopted)

| price | content | axiom touched | buys |
|---|---|---|---|
| **P-W7anom (new)** | Accept that the asymptotic Poincaré algebra fails on edge content: {K_b,P_c} = δ_bcE + F(Q_D)_cb, plus rotation-sector moments. Observable as a velocity-dependent, anisotropic far-field mass of bodies with edge content | none directly; a consequence of the matter law (Admissibility range, `AX:57-61`) and of reading the global charges as gravitational surface integrals (source/observable gate, `AX:187`; readout, `AX:82-83`) | consistency of the bulk constraint algebra (R16-8/R16-12) with the asymptotic charges |
| **P-W7edge0 (state condition)** | Physical states carry no edge quanta. On the box algebra the asymptotic algebra is exactly Poincaré, including nested brackets (§3.1). Number conservation preserves it; pair creation or interactions would not (excluded here) | none (an initial-state condition); record/formation rules are downstream (`AX:183-185`) | exact asymptotic Poincaré algebra |
| P-pf1 (alternative, unchanged) | SLAC/sawtooth matter: Δ = 0 off the face, so the degree-2 asymptotic algebra closes there. Face delta and no-umklapp remain (`vR16-8:13`) | `AX:57-58`, `AX:187` | CLOSES at degree 2 off the face, outside the registered S/G setting |
| P-W7bdy (R17-2) | **Its first branch ("boundary cross terms") is excluded** at degree 2 by Theorem A and Corollary N in the stated class. It reduces to its second branch, which is P-W7anom | — | — |
| P-W7mult, P-W7ro, P104–P106, P50 | unchanged; P-W7mult is the presentation in which Theorem A3 gives F(Q_D) | as cited | — |

---

## 4. Against the FIXED readings (`TESTS:6773-6777`)

- **CLOSES: not met, and excluded at degree 2 in the registered class.** Theorem A: no completion of degree ≥ 3 can alter the degree-2 asymptotic brackets. Corollary N: no linear, linearized-gauge-invariant boundary term in h can remove Q_D. Corollary N′: no continuous matter-moment redefinition of K can remove it. Closure requires leaving the setting: P-pf1 matter, or states without edge content (P-W7edge0).
- **ANOMALY: worker demonstration offered; pending referee.** The reading requires refereeing, so it is not claimed as met.
  - **Degree 2** (proved; checked): {K_b,P_c} = δ_bcE + Q_D,cb, in every presentation.
  - **Degree 3** (proved, conditional on the boundary admissibility of F): F(Q_D) in the dressed presentation. In the world-line presentation an extra 1/(q·v) term appears; not evaluated.
  - **Observable form** (proved; checked): the velocity-dependent anisotropic far-field mass of §3.6.
- **Worker reading: ANOMALY (pending referee).** If the referee does not accept the degree-2 statement as the registered "degree 3 in the Killing sector", or the dressed-presentation condition, the fallback is OPEN with Theorem A, Lemma S∞ and Lemma T as bounded results.
- **Against the expectation** (`TESTS:6778`: "ANOMALY ∝ Q_D in {K, P} … unobservable for any thermal population below ~1e19 GeV"):
  - **As expected:** {K,P} carries exactly Q_D. Thermal populations are invisible.
  - **Refinements:**
    - the anomaly is already present at degree 2, and is completion-independent there;
    - the rotation brackets fail by defect moments, not by Q_D itself;
    - {K,H} and {K,K} close at degree 2;
    - the thermal threshold is ~1e18 GeV (δM/M ≈ 1e-8 at the Earth's speed), not 1e19.

## 5. Strong-word and rule check

- **"Proved":** Theorem A (H-R17, H-mat, H-lead, H-charge; any completion of degree ≥ 3); Lemma S∞ (given the completion's regulated cancellation, localized source); Lemma T (exact, point defect, continuum kernel); Corollary N (linear, linearized-gauge-invariant surface functionals of h only); Corollary N′ (continuous periodic matter-moment redefinitions of K, separable bands); Theorem A3 (Jacobi/derivation identity; conditional on a convergent ADM boost term for the singular F); the M(V) formula (from the algebra, leading order in η); compact K-orbits (single quanta).
- **"Checked":** symbolic identities (generic band); ring operator identity (≤ 2.6e-13; 5.9e-7 at the G corner where both sides nearly vanish); surface integrals (1e-10, R-independent); Lemma T (≤ 3.5e-17); orbit and M(V) agreement (§3.6).
- **"Completion-independent":** only through degree 2, and only for completions of degree ≥ 3 with standard degree-1 constraints and improved Killing charges.
- **"Exactly":** S_b[B] = Δ (any R enclosing the source); B − δφ_d is pure linearized gauge off source; [K,P] = i(H + Q_D) as a one-body lattice-operator identity (infinite lattice; on the ring up to seam terms ≤ 3e-13 on the packets used).
- **"Suggested":** the size of {Q_D,W} (∼GM/(Rc²) × Q_D); unbounded rank growth of the generated algebra.
- **"Reading":** "the tail carries the defect to infinity"; "same root as SUMMARY §17"; all sizes at a = ℓ_P.
- **Round rules.** v_max stated for every law (§1). Ward/HDA: the standard algebra is the target. The constraint algebra's closure is the regulated (compact-lapse) statement of R16-8/R16-12; the asymptotic algebra is shown *not* to close. No deformed identity is used. Generic GR comparison: in continuum GR Δ ≡ 0 and Theorem A gives exact Poincaré (the control u = k²), so the anomaly is model-specific. Forks: "CLOSES requires P-pf1 or P-W7edge0" is not exhaustive. It excludes E-dependent or nonlinear boundary terms, multi-band matter with signed axes (the six-band counter-route of `vR16-5`), and deformed asymptotic symmetry algebras.
- **Not claimed:** the world-line presentation at degree 3; convergence of F's boundary terms; degree ≥ 4; a physical bulk non-locality (none is implied: the anomaly sits in global charges); any observational bound on relic edge populations.

## 6. For the referee

1. **Theorem A.** Is the identification of the asymptotic charges with the improved Killing generators correct, so that the degree-1 parts vanish identically and the degree-2 algebra is completion-independent? Is any admissible boundary term missed that could act at degree 2?
2. **Lemma S∞.** Check the sign argument: the regulated shell term cancels the matter defect, and the same functional enters K_∂ with the opposite sign. Does the surface computation agree with the bulk one?
3. **Lemma T / Corollary N.** Is the class of boundary terms (linear in h, linearized-gauge invariant, decaying ζ) the right one for the ADM boost charge?
4. **Theorem A3.** Is the derivation step legitimate given the singular W, and is "anomaly = F(Q_D)" acceptable as the degree-3 statement with the boundary condition named?
5. **Reading.** Does the degree-2 anomaly plus the degree-3 dressed statement meet "a demonstration that the asymptotic algebra fails by a term ∝ Q_D, with an observable form"?

## 7. Files (all in `S/`)

- `scripts/r188_vlasov_algebra.py` / `.out`: (A) symbolic brackets, negative and continuum controls.
- `scripts/r188_quantum_ring.py` / `.out`: (B) ring operator identities, box/edge/corner packets.
- `scripts/r188_surface.py` / `.out`: (C) R1(B) = 0, S_b[B] = Δ at R = 0.5, 3, 50; Lemma T; Newtonian control.
- `scripts/r188_observable.py` / `.out`: (D1) single-quantum orbits, (D1b) orbit periods, (D2) composite bodies and M(V), (D3) closure rank, (D4a) zone scan of |P′ − 1|, (D4) sizes.
- `scripts/sublum_copy.py`, `scripts/r1612_lib.py`: unmodified copies.
- `recheck/R16-8`, `recheck/R16-12`, `recheck/R17-2`: archived runners, regenerated `.out` (byte-identical to `*.out.archived`).
