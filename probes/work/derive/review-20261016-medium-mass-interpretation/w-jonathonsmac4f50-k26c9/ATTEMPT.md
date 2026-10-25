# ATTEMPT: J:derive:review-20261016-medium-mass-interpretation:a1

Same-family (Claude Sonnet 5.5), unrefereed, owner-requested research work. Not accepted science. No status words are claimed.

## Plain-language summary

The source asks how an "environment-dependent graviton mass" (mass squared proportional to density) can be tested by waves crossing the Earth. I rebuilt the layer problem with the missing tensor structure ("mixing"). In a Fierz-Pauli-type tensor model with a position-dependent mass, which I supplied as a comparator:

- The simple one-dimensional scalar layer equation is **exactly right**, not an approximation, for the polarization perpendicular to the plane of incidence at **any angle**. It is also exact for **both** polarizations at **normal incidence**.
- The only channel where mixing can change the answer is the in-plane polarization at oblique incidence. I did not finish that channel. I derived one interface constraint for it and stopped.
- Separately: finite tachyonic layers have transmission "teeth" whose area is fixed by the light-crossing time and does not depend on the mass. A plane tachyonic layer is unstable at any strength, so a 1D layer estimate cannot give an instability threshold. A phase (dispersion) bound constrains the **signed** column integral. The hot-era damping law quoted in the source is wrong in magnitude, but the conclusion survives.

## Reads, as required

I read in full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (130 lines), both on current main (checkout `main_wt`, HEAD a77a3449c9). I also read both source objects in full at the frozen commit `6afb06951a13ca861b50f47a8faf5d5c06594109`. Both sha256 values match the task (see `RECOVERY_STATUS.json`).

The related task `J:derive:review-20261014-flavour-strain-scope:a1` concerns residual-symmetry classification of flavour strain (branch `claude/chirality-grid-exercise-20261014`). It shares no object with this task, so there is no overlap. I searched current main `docs/` and `.claude/science` for finite-layer, GW170817 and tachyonic-slab treatments and found none (`docs/SCALAR_COSMOLOGICAL_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-15.md:44,298` uses GW170817 distances only). The task catalog and `probes/work/review-science-20261016/README.md` state that the strain packet is a historical source, not accepted science.

## Premises and what is supplied

- **From the four axioms: nothing.** The axioms (Lattice, Qubit, Admissibility, Record) give no tensor wave equation, no density-proportional mass, and no propagation law (`MINIMAL_AXIOMS_2026-06-29.md:114-130`, `:173-190`). Only `scale_reference_primitive` is approved, and it supplies a units conversion (`PRIMITIVE_REGISTRY_CHECK.md:31-56`). I use `hbar c` only for unit conversion.
- **Supplied by the source lane (ASSUMED):**
  - the field equation `h'' - lap h + m^2(x) h = 0` with `m^2 = sigma mu rho(x)` (`C5_F2_report.md:75`);
  - the coefficient `mu_rho = 1.0e-21` (placeholder), which is never used here as a derived number;
  - PREM densities and the GW170817 geometry (RECALLED/WEB in the source; not re-derived by me).
- **Supplied by me (ASSUMED comparator):** a Fierz-Pauli-type tensor equation `E_{mu nu}(h) - m^2(x)(h_{mu nu} - eta_{mu nu} h) = 0`, with `E` the linearised Einstein operator and `m^2(x)` bounded, piecewise constant or smooth. This is one possible completion of the source's scalar equation; the source flags a position-dependent Fierz-Pauli mass as not gauge-consistent in general (`C5_F2_report.md:78-80`). The source's own physical stiffness is a shear-only, Lorentz-violating form (`C5_F2_report.md:220-222`). Which structure the strain model supplies is not fixed by the axioms or the source. Statements below say whether they depend on the Fierz-Pauli choice.
- **Not an assumption:** wave propagation in vacuum outside the body. I take `m^2 = 0` there as the source does (air density is not modelled).

## Steps

Labels: PROVED (argument given here), CHECKED (executed in `check.py`), ASSUMED, READING.

### A. The tensor layer problem with mixing

**S1 [PROVED + CHECKED A1].** Take fields independent of `y`. Under the reflection `y -> -y` the components `h_{ty}, h_{xy}, h_{zy}` are odd and all others even, and `m^2(x)` respects this. In the Fierz-Pauli-type equation the odd sector closes exactly into a 2+1 dimensional Proca system with position-dependent mass, `d^nu F_{nu mu} - m^2(x) V_mu = 0`, with `V_mu = h_{mu y}` for `mu = t, x, z`. `check.py` verifies this symbolically for an arbitrary function `m2(x)`: every other component of the equation vanishes identically.

**S2 [PROVED + CHECKED A2, A3].** For `e^{-i w t + i q z}` dependence, set `G_mu = F_{x mu}` and `Y = (V_t, V_z, G_t, G_z)`. Then `V_x = -i (w G_t + q G_z)/m^2` is algebraic (the `mu = x` equation has no x-derivatives), and `Y' = A(m^2) Y` with the matrix printed in `check.py`. For bounded `m^2` that is nonzero on the massive side, the equations contain no delta functions only if `Y` is continuous. This gives the junction data for the odd sector: `V_t, V_z, G_t, G_z` continuous, and `m^2 V_x` continuous. Against vacuum (`m^2 = 0`), vacuum-side Gauss' law forces `V_x = 0` on the massive side of the interface. The characteristic polynomial of `A` is `(lam^2 - (m^2 + q^2 - w^2))^2`, so both polarizations share `k_x^2 = w^2 - q^2 - m^2`.

**S3 [PROVED + CHECKED A4, A5]. The s-polarization is exactly scalar.** Take `V = (q f, 0, -w f) e^{-iwt+iqz}`, the polarization normal to the plane of incidence. It solves the full odd sector for an arbitrary `m^2(x)` if and only if `f'' = (q^2 + m^2 - w^2) f`. The junction conditions of S2 reduce to continuity of `f` and `f'`, and the Gauss condition holds identically. So the source's equation with `h, h'` continuous is the **exact** s-polarization problem at any incidence angle, with `k_x^2 = w^2 - q^2 - m^2`. This holds for the Fierz-Pauli completion only. I did not check the shear-only form.

**S4 [CHECKED C1-C3].** I solved the full four-state Proca slab (vacuum, slab, vacuum) with the junction rules of S2, using a 6x6 matching system at 50 digits. The results are as follows.
- It reproduces the scalar slab reflection and transmission to 2.6e-50 at ten points, covering oblique incidence, both signs, and evanescent slabs.
- Flux `|r|^2 + |t|^2 = 1` holds to 9e-51 with no reference to the scalar formula; that is a check that the junction rules are self-adjoint.
- The matching determinant is nonzero (minimum 0.073), so the matched solution is unique at those points. Uniqueness in general is CHECKED, not proved.

**S5 [PROVED argument + CHECKED A6]. Both helicity-2 polarizations at normal incidence.** For `q = 0` the setting is invariant under rotation about the stratification axis `x`. The helicity-2 pair `(h_yy - h_zz, h_yz)` is a closed subspace. `check.py` verifies for the Einstein operator plus Fierz-Pauli mass that the pair is sourced by no other component and obeys `(box - m^2(x)) h = 0`. The argument that this holds for any local algebraic quadratic mass term covariant under the axial rotation is Schur's lemma: the helicity-2 equation is `box h - c(x) h` with one coefficient `c(x)`. A6 checks only the Fierz-Pauli instance. Hence at normal incidence the source's scalar model is the exact tensor problem, for both polarizations and for that wider class of mass terms.

**S6 [PARTLY DERIVED, B1-B3; first unresolved step].** The in-plane (p) polarization at oblique incidence lives in the even sector. This sector has three coupled channels: helicity-2, helicity-1, and the helicity-0 scalar of massive gravity. Derived so far:
- (B1, sympy) The `(x,x)` equation is `m^2(x) tr_perp(h) + S[h_perp] = 0`, with `tr_perp = -h_tt + h_yy + h_zz` and `S` a tangential second-derivative expression. It contains no x-derivative and no normal component.
- (B2, sympy) The x-second-derivatives enter only the tangential equations, through an invertible operator (determinant 2 on `tt, yy, zz`; unit on `tz`). So a jump in `h_tt, h_yy, h_zz, h_tz` at an interface would produce a `delta'` that the bounded mass term cannot cancel. These tangential components are therefore continuous.
- (B3) With `h_perp` continuous, the two sides give `m_L^2 tr + S = 0 = m_R^2 tr + S`. So whenever `m^2` jumps, `tr_perp = 0` and `S = 0` on the massive side of the interface. This is the analogue of `V_x = 0` in the odd sector.

Not done: the vacuum-side gauge matching (vacuum has gauge freedom `xi_t, xi_z`), the first-derivative jump conditions, the reduced six-dimensional transfer problem and its flux check. Until then the scalar chord model is **not shown** exact or inexact for oblique p-polarization. This is the part of the "mixing" obligation that remains open.

**S7 [READING].** Consequence for the source's Earth rows. The straight-chord, normal-interface solver (`C5_F2_report.md:131`) is the exact tensor problem only for a plane-stratified body at normal incidence, or for s-polarization at any angle. The Earth is made of spherical shells, so rays meet the layers obliquely (the source places the H1 chord's closest approach at 2,981 km, `C5_F2_report.md:126`). In a spherical body the transverse wavenumber is not conserved. In the tachyonic branch the index is large (about 6e3), so strong refraction is also unmodelled (`:78-80`). So the chord solver is an approximation for the Earth even before the p-polarization question. This follows from the source's own "not modelled" list and is not a new defect.

### B. Scope of the signed inference

**S8 [PROVED + CHECKED D1, D2, D3].** For any layered profile, the first-order change in transmission is `t = t_0 (1 - i eps sum_j m_j d_j / (2k))`. Only the **signed** column integral enters. (Checked with exact rational parameters on three two-layer sets, mixed sign included.) Counterexample to an unsigned reading: take layers `(+mu, d)` and `(-mu, d)`. The first-order term vanishes identically while the second-order term is nonzero (`|t''/t| = 0.20, 3.8, 0.11` at three parameter sets). In `mpmath`, phase/eps for the pair is 5e-5 at eps = 1e-3 and 5e-6 at 1e-4, against 0.7 for one same-sign layer with the same unsigned budget. So a phase-budget bound constrains `|sum sigma_j rho_j d_j|`, not `sum rho_j d_j`. The source's Earth bound divides the phase budget by the unsigned column; that equals the signed column only if the sign is uniform along the chord, which the source's placeholder assumes (`C5_F2_report.md:86`) but its density-proportional ansatz does not force. **New relative to the source:** the explicit cancellation counterexample. The statement that dispersion limits are signed is implicit in the referee's correction (`C5_F2_referee_verdict.md:5`).

**S9 [CHECKED D4, D5; scope cleanup, not new].** The small-mass phase `-A/(2w)` is the first term of `sqrt(w^2 - A) = w (1 - A/w^2)^(1/2)`, whose series has convergence radius `|A| < w^2` for both signs (all coefficients negative; ratio 0.962 at order 39). At the quoted bound `mu = 1.5e-29` with a core density of 13,000 kg/m^3 (RECALLED, input), `M^2/w^2 = 12.7` at 30 Hz. The 1/f form is valid only for `mu <= 1.2e-30` in the core at 30 Hz. The referee already noted that the tachyonic expansion fails near the low-frequency, core-density edge (`C5_F2_referee_verdict.md:5`); I only quantify it.

**S10 [CHECKED G1; READING].** A one-sided posterior on `A >= 0` does not bound `A < 0`. The first-order phase is odd in `A` (S8), so a measured offset breaks the mirror symmetry. In a toy Gaussian likelihood the 90% bounds are 1.645 and 1.645 for a null result, but 2.378 and 1.148 for a measured offset of one sigma. This illustrates the referee's correction (`C5_F2_referee_verdict.md:5`) and is not a statement about the real LVK likelihood, which I did not use.

### C. Finite-layer resonances (tachyonic sign)

**S11 [PROVED + CHECKED E1, E3].** For a uniform slab with `k_s > k_v`, `|t|^2 = 1/(1 + s^2 sin^2(k_s d))` with `s = (k_s/k_v - k_v/k_s)/2`. Over one phase period `int |t|^2 dphi = pi/sqrt(1 + s^2)` (exact; checked to 40 digits). On the comb `w_n = sqrt((n pi/d)^2 - M^2)` one has `|t| = 1` and `r = 0` exactly, for any `M`. So no single-frequency bound on `|t|` can exclude large tachyonic `M`: the allowed set of `M` is not an interval.

**S12 [PROVED argument + CHECKED E2, E4, E5]. Tooth area is independent of M.** In the regime `k_s >> k_v`, the area of one tooth is `(pi k_s/(w d)) * 2 k_v k_s/(k_v^2 + k_s^2) -> 2 pi k_v/(w d)`, which at `q = 0` is `2 pi/d` in `w` (that is, `c/d` in Hz), whatever `M` is. `mpmath` integration of one tooth gives 0.3103 against the predicted 0.3111 (the 2pi/d limit is 0.3142). For the source's H1 chord (11,260.65 km, taken from the source) the tooth area is `c/d = 26.6` Hz. At the placeholder `M = 2.36e-9 eV` the comb phase advance over 30-1000 Hz is 0.21 rad, less than pi, so there is at most one tooth in the band. Consequently, for a weight `w(f) >= 0` (the SNR-squared density) and an isolated tooth, `S^2 = int w |t|^2 / int w <= (c/d) w_max / int w df`. With the toy analytic PSD fit (RECALLED form, illustration only) the effective bandwidth is 140 Hz, giving `S^2 <= 0.19`. So for the placeholder, and for any `M` with isolated teeth, resonances cannot rescue an amplitude consistent with the EM distance; the exclusion by amplitude (not by dispersion) stands. This depends on the bandwidth through the PSD, so it is a conditional bound. **New relative to the source:** the M-independent tooth area and the resulting bound. The source's remark of "internal resonances" (`C5_F2_report.md:141`) and the referee's remark (`C5_F2_referee_verdict.md:7`) are qualitative. Note that the source's S_SNR weights `|t|`, not `|t|^2`.

### D. Instability scope

**S13 [PROVED + CHECKED F1-F4].**
- (F1) A tachyonic plane layer of any thickness and any strength has an even bound state with growth exponent `kappa in (0, M)`, from `k tan(k d/2) = kappa`, `k^2 + kappa^2 = M^2`. At weak coupling `kappa -> M^2 d/2` (ratio minus 1 is -1.7e-9 at `M d = 1e-4`).
- (F2) A disjoint finite-difference calculation converges to `-kappa^2` (errors 1.1e-5, 2.7e-6, 6.8e-7 at three grid spacings).
- (F3) With transverse wavenumber `q` the growth rate satisfies `Gamma^2 = kappa^2 - q^2`. A body of transverse size L is unstable only above a threshold.
- (F4) The uniform ball (`l = 0`) threshold is `M R = pi/2`, matching the source's rule (`C5_F2_report.md:97`).

So a one-dimensional layer estimate by itself gives no instability threshold. The threshold comes from the transverse (3D) confinement, which the source's radial calculation did include. This clarifies the scope of row 3; it does not change the source's number. The nonlinear end state is not computed here.

### E. Hot-era assumptions

**S14 [CHECKED G2, G3; refines a known correction].** For super-horizon tensors with `m^2 = A H^2`, the exact power laws are `t^{-1/4} = a^{-1/2}` in the radiation era (for `A > 1/4`) and `t^{-1/2} = a^{-3/4}` in the matter era (for `A > 9/16`), independent of `A` beyond those thresholds. They are not the constant-mass law `a^{-3/2}` that the source applied (report line 213 per the referee's pointer; the referee noted WKB gives `a^{-3/2} m^{-1/2}`, `C5_F2_referee_verdict.md:13`). Over 34.1 e-folds from 150 GeV to today, `a^{-3/2}` gives `e^{-51.1}` (the source's figure), while the exact exponents give `e^{-19.1}` (radiation 25.9 e-folds, matter 8.1). Assumptions: adiabatic tensor-only model, `m^2 = A H^2` through both eras, super-horizon modes, T-equality 0.8 eV, `1 + z_eq = 3400`, no Lambda era. The qualitative conclusion (primordial tensors strongly damped, `r` near 0, so no bound from the upper limit on `r`) is unchanged within these assumptions. It is model-restricted, as the referee already stated.

## What is new, and what is not

**Not new:** the source numbers and the referee's corrections (positive-mass LVK limit; tachyonic expansion failure; resonances exist; WKB damping); the Earth/PREM geometry; any Born, Fabry-Perot or Poynting formula by itself.

**New relative to the sources (all in a supplied comparator, same-family, unrefereed):**
1. S1-S5: the explicit mixing structure (odd sector is Proca), junction data, and the exactness theorem for s-polarization at any angle and for helicity-2 at normal incidence.
2. S6: the interface constraint `tr_perp = 0`, `S = 0` for the even sector, as a partial derivation.
3. S8: the exact cancellation counterexample to an unsigned reading of a dispersion budget.
4. S12-S13: the M-independent tooth area with its conditional SNR bound, and the threshold-free plane-layer instability.

## First unresolved step

**S6:** the in-plane (p) polarization at oblique incidence in the even sector. Completing it requires the vacuum gauge matching, the first-derivative jump conditions, the reduced six-dimensional transfer problem, and a flux-conservation check. Beyond that, open items are: the actual mass-term structure of the strain model (Lorentz-invariant versus shear-only), spherical-shell geometry, a signed waveform likelihood for the tachyonic sign, and the nonlinear end state of any instability.

## Files

`check.py` (30 checks, all PASS; run time about 100 s on this machine, one process), `RECOVERY_STATUS.json`, this file.
