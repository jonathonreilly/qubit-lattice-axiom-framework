# C4 lane RY, probe Y1: readout noise for lensed light, and the effective source extent for incoherent emission (worker report)

**Worker:** Claude Opus 5.5 (probe Y1), the same model family as the exercise authors. **Unrefereed.** Worked 21:10–21:45Z on 2026-10-11. OMP_NUM_THREADS=2; every run under 1 s. No repository file was edited.

**Read in full:** TESTS.md "C4 result recorded 21:01Z (RL4)", "C4 last probe (21:08Z) / lane RX", "C4 result recorded 21:14Z (X1)", "C4 final probe (21:12Z) / lane RY" (fixed readings, expectation); `C4_RL4_report.md`, `C4_RL4_referee.md`; `C4_RL2_report.md`; `C4_X1_report.md`. **Read in part:** `C4_RL3b_report.md` (verdict table, Theorem 1, Lemma D lines 1–60, 110–127), `C4_RL3b_referee.md` (items 1–4).

**Labels:** PROVED (complete argument here or in a refereed RL file, scope stated); CHECKED (my arithmetic, scripts below); ARGUED (standard step, not written out); SUGGESTED (heuristic, not proved).

## Verdict (worker): FAIL (bounded). The supervisor's "borderline/INCONCLUSIVE" expectation does not hold, because the coherence length is the wrong s.

| item | status | content |
|---|---|---|
| Variances of independent emitters add | **PROVED** (elementary) | With emitter phases independent of each other and of the sprinkling, the time-averaged intensity in each realization P is I_P = Σ_e \|φ_{e,P}(x)\|². So E_P I = S_GR + Σ_e V_e, V_e = Var_P φ_e(x). The shared-sprinkling cross-covariances drop out of the mean intensity exactly. |
| Fixed-phase total field | **PROVED** (Minkowski inequality) | Var_P(Σ_e φ_e) ≤ (Σ_e √V_e)². The per-emitter variances control the total in both readings; the source's **spatial** size cannot enter beyond them. |
| Which τ governs V_e | **PROVED** geometry; lower bound from RL4 T′ (**refereed**, bounded scope) | τ_e is the proper time from the start of e's emission to the observer event x: τ_e² = (D + cΔt_e + s_e)² − D² ≈ 2D(cΔt_e + s_e) + (cΔt_e)², where Δt_e is how much earlier than the retarded time e fired. Only the **mean** obeys Huygens. The noise of H_P(x,y) for timelike y ≺ x is not zero; it grows as e^{c√ε τ/ℓ_k} (RL4). |
| Effective s for the observed intensity | **PROVED** structure; observational lower bound | **s_eff = c × (emission duration before the retarded time)**, not the coherence length. A source seen for an observing baseline T_obs was emitting at least that long, so **s_eff ≥ c·T_obs** without any source modelling. The coherence length governs only the on-cone emitters' term. |
| Cross-covariance of two emitters at separation r | **PROVED** geometry; suppression from RL3b Lemma D (**referee-confirmed for fixed Δ**) | The shared proper time is exactly τ_× = √(τ² + r²/4) − r/2 ≈ τ − r/2. The end-rung for displaced endpoints is O(1/(z r)) against O(1/z²) coincident, a relative factor γℓ_k²/r ≈ 1e-40 at atomic r. The node-ladder part carries Ψ_e Ψ_e′*, which the phase average kills. Shared sprinkling does **not** make the source act as one macroscopic coherent unit, and the question does not decide the reading (row 1). |
| Noise for lensed light, ℓ_k = 7.9e-20 m, D = 1–5 Gpc | **CHECKED** | Proved rate c_low = 0.628: on-cone optical (s = 1 μm) 2.6e-3 to 5.8e-3 variance e-folds; radio 100 MHz band (3 m) 4.5–10; maser line (1 km) 83–185. **But** the emission-duration term at s_eff ≥ c·T_obs gives 4.5e4 (T_obs = 1 s), 7.7e6 (8 h), 2.5e8–5.7e8 (1 yr), and 8e11–1.8e12 for a 1e7-yr quasar. |
| Observational allowance | literature-level (RECALLED, not fetched) | Lensed-image radio flux ratios match smooth models to ~10–20 %; time delays come from correlated variability; VLBI fringes on lensed components are strong. Each needs in-band noise N ≲ S, i.e. n_var ≲ O(1) after prefactors. |

**Reading against the FIXED RY readings: FAIL (bounded).**
- The noise exceeds what observed lensing allows by e^{≥ 4.5e4} (1 s baseline) to e^{~1e12} (quasar lifetime). s is derived, with an observational lower bound.
- **Bounds on the reading:**
  - RL4's T′ scope: each emission event has a spacelike past edge with regular turn-on.
  - The RL4 rate is asymptotic with an uncontrolled polynomial prefactor. At these exponents this is irrelevant (§4.3).
  - The in-band fraction of the variance is not derived. A crude estimate costs at most e^{−O(150)} (SUGGESTED, §4.4), which is also irrelevant at these exponents.
- **If the referee requires the in-band spectral fraction derived, the reading is INCONCLUSIVE, leaning FAIL by many orders of magnitude in the exponent.**

**Plain summary.**
- **Independent emitters do add their noises, not their fields.** Random phases cancel every cross term in the average intensity, even though all emitters share one sprinkling. So each emitter's own noise is what matters. That half of the supervisor's expectation is right.
- **But each emitter's noise is set by how long ago it fired, not by its coherence length.** The realization's propagator obeys Huygens' principle only on average. An atom that emitted a nanosecond before the light we now see contributes nothing to the mean field at the telescope, but its noise is still there, and the noise grows with the proper time from that emission to us.
- **That proper time is large for any real source.** For a source at 1 Gpc, proper time is √(2D·cΔt). The proved rate gives one variance e-fold of noise for every emission more than about 0.5 ns earlier than the retarded time (8 ps ... 0.5 ns, depending on the constant).
- **Every real source has been on far longer.** We have watched lensed quasars for decades, so they were emitting then. With one year of observed emission the noise is e^{2.5e8} at 1 Gpc.
- **The coherence-length numbers the supervisor expected are real but beside the point.** They apply only to the emitters firing exactly on our past light cone: optical 0.003 e-folds, radio 5–10, masers ~100.
- **This is not specific to lensing.** Near a source the proper time is just the source's age, so the noise reaches one e-fold after about 3 hours of source age (proved constant) or 40 minutes (node-ladder constant). Examples:
  - a lamp on for one hour at 1 m: 0.4–1.6 e-folds;
  - the Sun: e^{1.4e13}.
- At photon ℓ_k ≤ 7.9e-20 m, the event-route readout predicts noise-dominated light from every source older than a few hours, unless the noise falls entirely outside every detector band.

## 1. Setting

- Units and law as in RL1–RL4: ε = (ℓ_P/ℓ_k)⁴. Realization field φ_P(x) = Σ_{y∈P} H_P(x,y) J(y); mean Ψ = H̄J.
- RL4 (refereed): the Palm two-point variance V_ε(τ) = Var[H_P(x,y)/ε] obeys lim inf τ⁻¹ ln V ≥ c_low √ε/ℓ_k, with c_low = 0.628 / 0.670 / 0.712. This transfers to finite sources with a spacelike past edge and a regular turn-on patch (T′); the referee's scope is "edgeless histories and finite-distance prefactors open".
- RL3b (refereed, conditional on P1): the derived node-ladder constant is k_h = 2.735 / 2.835 / 3.254.
- Incoherent source: J = Σ_e a_e J_e, where J_e is the emission of emitter e (support of extent s_e in retarded time, spatial size ≲ atomic) and a_e = e^{iθ_e} with θ_e iid uniform, independent of P.
  - The detector integrates over many coherence times, so the observed intensity is the θ-average. This is standard ergodicity for thermal light.

## 2. The effective source extent

### 2.1 Phase average: variances add, cross-covariances drop out (PROVED)

For fixed P, φ_P(x) = Σ_e a_e φ_{e,P}(x). Since E_θ[a_e a_{e′}*] = δ_{ee′} and θ is independent of P:

  I_P(x) := E_θ |φ_P(x)|² = Σ_e |φ_{e,P}(x)|²  (pointwise in P).

Writing φ_{e,P} = Ψ_e + η_{e,P} with E_P η = 0:

  E_P I = Σ_e |Ψ_e|² + Σ_e V_e = S_GR + N,  where V_e = Var_P φ_{e,P}(x) ≥ 0.

- The cross-covariances Cov_P(φ_e, φ_{e′}) induced by the shared sprinkling multiply E_θ[a_e a_{e′}*] = 0. So they do not enter the mean intensity. This is exact.
- N is a sum of nonnegative terms, so **N ≥ V_{e*} for any single emitter e*.** This monotonicity is what lets a one-emitter lower bound transfer to the whole source. It fails for a fixed-phase J, where cross terms can cancel, which is why the phase average matters.

### 2.2 Fixed phases (PROVED)

For a fixed phase draw, ‖Σ_e a_e η_e‖_{L²(P)} ≤ Σ_e ‖η_e‖ (Minkowski), so Var_P φ ≤ (Σ_e √V_e)².
- So, either way, the per-emitter variances control the total.
- The spatial size of the source enters only through which emitters exist, not through a "macroscopic coherent extent".

### 2.3 Which proper time governs V_e (geometry PROVED; bound from RL4 T′)

- **Geometry.** Let x be the observer event at distance D, and let e fire at Δt_e before the retarded time of x, with retarded-time extent s_e. Every point of supp J_e lies inside J⁻(x), with τ(y,x)² ≤ (D + cΔt_e + s_e)² − D² = 2D(cΔt_e + s_e) + (cΔt_e + s_e)².
  - Its past edge sits at proper time τ_e ≈ √(2D(cΔt_e + s_e)) below x when cΔt_e ≪ D, and τ_e ≈ cΔt_e when cΔt_e ≫ D.
- **Huygens is a property of the mean only.** H̄ is concentrated where τ(y,x) ≲ ℓ_k (it tends to the retarded Green function). So Ψ_e(x) ≈ 0 once cΔt_e ≫ s_e. The noise is a different matter: V_ε(τ) grows with τ for every timelike pair (RL4's theorem is about τ → ∞).
- **Lower bound per emitter (RL4 T′, refereed scope).** An emission event that starts at a definite time, such as an excitation, has a spacelike past edge. On ℓ_k scales its current is locally constant (the optical period is ~1e12 ℓ_k), so a regular turn-on patch exists. That gives

  V_e ≥ C_e τ_e^{−p} exp(c_low √ε τ_e/ℓ_k)  as τ_e√ε/ℓ_k → ∞ (polynomial prefactor not controlled).

  The per-emitter edge hypothesis is ARGUED; it is much weaker than requiring the whole quasar to have a past edge.
- **Consequence.** N ≥ max_e V_e, and that maximum is attained by the **earliest** emitters, not by the on-cone ones. So

  **s_eff = c·T_emit**, the emission duration before the retarded time, plus the s_e of the earliest emitters.

  The coherence length controls only the on-cone term Σ_{on-cone} V_e, which is what the supervisor's expectation computed.
- **Observational lower bound (no source modelling).** A source observed for a baseline T_obs was emitting during the T_obs before the current retarded time. At the end of the observation those emission events are ≥ T_obs inside the observer's past cone. So s_eff ≥ c·T_obs.

### 2.4 Cross-covariance of two emitters at separation r (task item; does not change 2.1–2.3)

The supervisor asked whether the shared sprinkling correlates different emitters' noise. It does, but in a limited way.
- **Shared proper time (PROVED, exact; CHECKED in `y1_A`).** Take y, y′ at transverse separation r, each at proper time τ from x. Then

  max_{z ∈ J⁺(y)∩J⁺(y′)} τ(z,x) = √(τ² + r²/4) − r/2 ≈ τ − r/2  (r ≪ τ).

  Work in the frame where x is at rest over the midpoint; a boost along the line of sight leaves r unchanged.
  - By the renewal structure (RL3b Theorem 1, which cuts at the last shared vertex), the cross-moment's exponential rate is at most that of the shared segment, γτ_×. So the correlation coefficient falls at least as e^{−γ r/2}·(prefactors), with 2/γ = 1.4e12 m (k_h) to 6.0e12 m (c_low).
  - Pairs separated along the line of sight at the same retarded time are null-separated, and they share the later point's full τ.
- **End-rung suppression (RL3b Lemma D; referee: correct for fixed Δ, nonuniform as Δ → 0 or near null).** For distinct endpoints, the last pair-segment is O(1/(z|Δ⃗|)) against 4πI_h/z² when the endpoints coincide. The relative factor is z/|Δ| = γℓ_k²/r:
  - 9e-41 at r = 1e-10 m;
  - 9e-45 at r = 1 μm.
  So, apart from (null) line-of-sight pairs, distinct source points' noises are nearly uncorrelated. This is consistent with RL4's lower bound, which carries the end weight J(z_k)², integrated over the source: an incoherent sum over source points.
- **The node-ladder part.** Its cross term carries Ψ_e(z_k)Ψ_{e′}*(z_k), the overlap of the two emitters' mean fields at the last shared node. The phase average removes it exactly (2.1).
- **Answer to the task's question.** The noise of different emitters is correlated through the shared sprinkling only weakly (factor γℓ_k²/r), or along null lines. This does not make the macroscopic spatial extent the relevant s. What enlarges s is the emission history in **time**, through each emitter's own τ_e.

## 3. Numbers (CHECKED; `y1_A_efolds.out`, `y1_B_observed_baseline.out`)

ℓ_k = 7.9e-20 m and ℓ = ℓ_P give ε = 1.75e-63 and √ε/ℓ_k = 5.30e-13 m⁻¹.
- The variance rate is γ = 3.33e-13 m⁻¹ (c_low, op0, proved) or 1.45e-12 m⁻¹ (k_h, op0, derived).
- n_var = γτ is in variance e-folds; sd e-folds = n_var/2.
- Flat-space proper-time formula. FRW corrections are O(1) factors in τ.

**On-cone emitters only (the supervisor's quantity: s = coherence length):**

| source extent s | 1 Gpc: n_var (c_low / k_h) | 3 Gpc | 5 Gpc |
|---|---|---|---|
| atom size, 1e-10 m | 2.6e-5 / 1.1e-4 | 4.5e-5 / 2.0e-4 | 5.8e-5 / 2.5e-4 |
| optical thermal coherence, 1 μm | 2.6e-3 / 1.1e-2 | 4.5e-3 / 2.0e-2 | 5.8e-3 / 2.5e-2 |
| optical line (10 ns lifetime) or radio 100 MHz band, 3 m | 4.5 / 20 | 7.8 / 34 | 10 / 44 |
| radio 1 MHz channel, 300 m | 45 / 200 | 78 / 340 | 100 / 440 |
| maser line, ~1 km | 83 / 360 | 140 / 620 | 180 / 800 |
| 1 kHz maser channel or FRB (1 ms), 3e5 m | 1.4e3 / 6.2e3 | 2.5e3 / 1.1e4 | 3.2e3 / 1.4e4 |

- **Supervisor arithmetic.** τ(s = 1 m, 1 Gpc) = 7.9e12 m, not 2.5e13 m (that value corresponds to s ≈ 10 m). The resulting n_var is 2.6 (c_low) to 11 (k_h).
- **Threshold for n_var = 1 at 1 Gpc:**
  - s = 0.15 m (c_low) or 7.7 mm (k_h), i.e. 0.49 ns or 26 ps of retarded time;
  - at 5 Gpc: 2.9 cm or 1.5 mm.

**Emission-duration term (the governing one, s_eff = c·T):**

| case | τ (m) | n_var c_low | n_var k_h |
|---|---|---|---|
| lensed source, 1 Gpc, T_obs = 1 s | 1.4e17 | 4.5e4 | 2.0e5 |
| lensed source, 1 Gpc, T_obs = 8 h | 2.3e19 | 7.7e6 | 3.3e7 |
| lensed source, 1 Gpc, T_obs = 1 yr | 7.6e20 | 2.5e8 | 1.1e9 |
| lensed source, 5 Gpc, T_obs = 1 yr | 1.7e21 | 5.7e8 | 2.5e9 |
| lensed SN, ~100 d of emission, 1 Gpc | 4.0e20 | 1.3e8 | 5.8e8 |
| quasar, 1e7 yr, 1 / 5 Gpc | 2.4e24 / 5.4e24 | 8.0e11 / 1.8e12 | 3.5e12 / 7.8e12 |
| (not lensed) star at 10 pc, 1 s | 1.4e13 | 4.5 | 20 |
| (not lensed) lab lamp at 1 m, on 1 h | 1.1e12 | 0.36 | 1.6 |
| (not lensed) Sun, 4.6 Gyr | 4.3e25 | 1.4e13 | 6.3e13 |

## 4. Comparison with observations

### 4.1 What observations require (RECALLED, not fetched this session)
- **Image flux ratios.** Radio and mid-IR flux ratios of quad lenses match smooth lens models to ~10–20 %. Deviations at that level are attributed to substructure. The ratios differ strongly from 1 and are stable over years. A steady in-band excess N comparable to S in each image would drive ratios toward the ratio of the noise terms. So this needs N/S ≲ 0.1.
- **Time delays.** Delays are measured to a few % by cross-correlating variable light curves, with variability amplitudes of 0.1–1 mag. A steady N ≫ S would dilute variability by S/(S+N). This needs N ≲ S.
- **VLBI.** Lensed radio components give strong fringes on 1e6–1e7 m baselines.
  - The same Lemma-D structure at the observer end (two antennas = two displaced top endpoints) suggests the noise at the two antennas is uncorrelated up to a factor γℓ_k²/b ~ 1e-57 (SUGGESTED).
  - Noise would then add to the autocorrelations but not to the cross-correlation, cutting visibility to ≈ S/(S+N). Observed visibilities of O(0.1–1) need N ≲ few × S.
- **Combined:** n_var ≲ O(1) in band, up to O(1) prefactors.

### 4.2 Model prediction
In-band question aside, n_var ≥ 4.5e4 (1 s baseline, proved constant) and ~1e8–1e12 for real lensed sources. That exceeds the allowance by that many e-folds.

### 4.3 Prefactors (ARGUED)
RL4's rate is asymptotic with an uncontrolled polynomial prefactor. Here τ√ε/ℓ_k ≥ 1e5 is deep in the asymptotic regime. The logs of all plausible prefactors are each ≲ 10³:
- powers of τ/ℓ_k (τ/ℓ_k ≲ 1e44, ln ≈ 100 per power);
- the number of emitters (ln ≲ 140);
- the 1/D² geometric dilution of the mean signal, which the τ-only noise kernel does not share and which favours the noise (ln ≈ 200).

These matter only against n_var ≲ 10³, i.e. the on-cone radio and maser rows. They do not affect the emission-duration rows.

### 4.4 In-band fraction (SUGGESTED; the one open physics step)
Var φ(x) is a pointwise, all-frequency quantity. The variance-dominating ladders have legs of proper time 0.1–0.6 ℓ_k at rapidities up to ln(1/z) ≈ 73. That suggests the noise is mostly far above optical frequencies. Two further points:
- In the rest frame of x − y, which moves toward the observer at γ_b = √(D/2s), the noise arrives isotropically. In the observer frame it is beamed within ~1/γ_b of the source direction. So it appears in the image, not as a diffuse background.
- Restricting the top leg to observer-frame-soft rapidities costs a crude end factor ~ e^{−2 ln(1/z)} ≈ e^{−144}, plus a band fraction (ℓ_kω/c ≈ 8e-13 optical, 8e-18 at 5 GHz, i.e. e^{−28} to e^{−39} per power).
- So a penalty of order e^{−10²}–e^{−10³} is plausible. It cannot offset n_var ≥ 4.5e4 unless the noise spectrum has a hard gap at observable frequencies, for which nothing in the RL files gives a reason.
- I did not compute the noise spectrum. A referee could reasonably require it.

## 5. Map to the FIXED readings (TESTS.md, lane RY)

- **PASS** ("for realistic incoherent sources, the noise is below 1 e-fold at ℓ_k ≤ 7.9e-20 m, with the derivation of s controlled"): **not met.**
  - Below 1 e-fold holds only for the on-cone optical term (2.6e-3).
  - The derivation of s shows that the on-cone term is not the governing one.
- **FAIL** ("the noise exceeds what observed lensing allows, with s derived"): **met, bounded.**
  - s_eff = c·T_emit ≥ c·T_obs is derived: the phase average is PROVED, the per-emitter geometry is PROVED, and the observational baseline is a fact.
  - The noise bound is RL4 T′ (refereed). It is applied per emitter, which needs only that individual emissions have a past edge (ARGUED).
  - Its magnitude, e^{≥4.5e4} to e^{~1e12}, swamps any polynomial prefactor.
  - **Bounded to:** (i) T′'s edged-emission scope; (ii) the variance being observable in band (§4.4, SUGGESTED penalty ≤ e^{−O(10³)}).
- **INCONCLUSIVE:** applies if the referee requires §4.4's in-band fraction derived. It would lean FAIL by ≥ 4 decades in the exponent.
- **Against the supervisor expectation:**
  - "Variances add" is confirmed (PROVED).
  - "Each grows with that emitter's own τ ≈ √(2D·s_atom)" holds only for emitters firing on the observer's past cone. The intensity sums over all emitters in J⁻(x), and earlier ones carry noise without signal.
  - So the answer does not depend on the coherence length, and the expected "borderline" is not what happens.

## 6. Consequences beyond RY (SUGGESTED; for the supervisor)

1. **Not lensing-specific.** For nearby sources τ ≈ c × source age. So every field sourced by anything older than ~3 h (c_low) or ~40 min (k_h) is noise-dominated at photon ℓ_k = 7.9e-20 m. This includes, by the same per-point incoherence (§2.4), the static fields of long-lived charges, if their histories have edges. This is a stronger and simpler FAIL route than lensing.
   - To get one e-fold per Hubble time (τ = 1.3e26 m), the variance rate must fall by 1/(γ·1.3e26) ≈ 2e-14. That needs ℓ_k ≳ 7.9e-20 × (4.3e13)^{1/3} ≈ 2.8e-15 m, i.e. non-locality at ~70 MeV, which is excluded for the photon by every collider bound in X1.
2. **The GW lane's source scale.** RL2–RL4 used s = 10 km, the merger. By §2.3 the binary's inspiral, emitting for years before merger, sets s_eff for GW too. That only strengthens lane RL3's FAIL; the verdict does not change.
3. **Edgeless loophole.** The only escape inside the RL4 framework is that no emission has a past edge, for example Gaussian-tailed histories (referee: open). For the per-emitter argument this would require every atomic emission to be edgeless. Even then, §2.1 shows N ≥ V_e for any one emitter that satisfies T′.

## 7. Flags for the referee

1. §2.1's ergodic step: the detector's time average equals the θ-average.
2. §2.3's per-emitter application of T′: the regular turn-on patch for an oscillating current on ℓ_k scales; emission events treated as edged.
3. §2.4's use of RL3b Lemma D as a statement about the cross-moment's end rung, carried through the renewal pole. This is heuristic for the residue ratio, but it is not needed for the verdict (2.1 makes cross terms irrelevant).
4. §4.1's observational allowances are RECALLED, not fetched or cited line by line.
5. §4.4's in-band penalty is a crude estimate. The noise spectrum and its direction are not computed.
6. Flat-space τ formula at Gpc distances; FRW changes are O(1) in τ.

## Files (scratch: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/Y1/`)

| script | output | content |
|---|---|---|
| `y1_A_efolds.py` | `y1_A_efolds.out` | ε, γ, decorrelation length; on-cone and duration tables at 1, 3, 5 Gpc; n = 1 thresholds; Lemma-D suppression γℓ_k²/r; τ_× check; band parameters |
| `y1_B_observed_baseline.py` | `y1_B_observed_baseline.out` | s_eff ≥ c·T_obs rows; non-lensed sanity rows (star, lab lamp, Sun); crude in-band end penalty |
