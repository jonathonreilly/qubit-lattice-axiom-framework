# J:derive:review-20261012-cq-gravity-correlated-kernels:a1
Resolve the non-Markovian CQ-gravity escape. Worker: Claude Sonnet 5.5, same family as every earlier C5 worker. Same-family, unrefereed. Date 2026-10-25.

**Verdict: PARTIAL.** The route stops at step 8. No HIT is emitted.

## Plain language first
The question was whether a "correlated" (memory-carrying) Gaussian classical-quantum gravity law can keep three things at once: a legitimate quantum-mechanical bookkeeping (complete positivity), an empty vacuum that is not kicked into excitation, and the ordinary finite gravitational-wave response of general relativity.

Answer for the one explicit kernel worked here (the "saturated emission-silent" kernel of R10-3, restated):

- The three listed properties are mutually consistent at the level of each four-momentum. Positivity data pass, the vacuum rate is exactly zero, and a form factor that is Hölder-continuous at the light cone gives a finite, regulator-independent response to a finite-bandwidth pulse.
- The price is that the classical metric's own noise is infinite near the light cone. The product of "noise felt by matter" and "noise in the metric record" is exactly ħ²g²F²/s², so they cannot both be integrable. This is R10-3's Theorem P and R12-4's Theorem U, not a new mechanism.
- The pointwise "additive floor" of R8-3 really is an extra assumption: exact data show it fails, with the vacuum-side noise equal to 0 against a floor of |G|ħ|F|. That fact is also already in the sources, numerically. What is new here is the exact form.
- What is NOT shown: that this per-momentum data is a genuine completely positive history (a dilation), and that every correlated Gaussian history has one. That is the first unresolved step.

## What I read
I read `docs/MINIMAL_AXIOMS_2026-06-29.md` (all 233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (all 130 lines) on current main (`main_wt`, HEAD a77a3449c9). I read the five task source objects (all five sha256 verified, see `RECOVERY_STATUS.json`). I also read the later branch objects R9-4, R10-3, R11-5 and R12-4 (reports and verdicts; hashes recorded) because they supersede R8-3's reading. I read `TESTS.md` at the branch tip for the fixed readings.

Ownership and overlap: `git ls-remote` shows no `refs/probes/claims/*` for this unit. No open PR matches CQ gravity (only #10009, #9973, #10043, unrelated). `probes/work/derive/` has no directory for this problem.

## Layers kept apart
**What the four axioms say.**
- Lattice: sites are the points of Z³ with cubic adjacency, translations and rotations (`docs/MINIMAL_AXIOMS_2026-06-29.md:37-41`).
- Record: one record per site, permanent, only records readable (`:79-83`).
- Admissibility is not dynamics: it chooses no Hamiltonian, no time metric, no decoherence mechanism (`:114-130`, `:181-187`).
- Axioms and approved primitives are the complete supplied foundation (`:108-112`). Nothing in them mentions a classical field, Gaussianity, stationarity, a Lorentz-invariant continuum, or a "classical metric record".

**What approved primitives add.**
- `scale_reference_primitive`: one conversion to Planck units; no dimensionless content (`PRIMITIVE_REGISTRY_CHECK.md:31-56`). It fixes the unit for g, not the form factor.
- `kinetic_isotropy_primitive`: c_t = c_s on the regulator block (`:58-96`). It is not Lorentz invariance of a continuum limit.
- `realized_state_primitive`: pointwise evaluation only (`:98-129`).

**What the lane supplied (all ASSUMED below).**
- Linearized Gaussian CQ gravity on a Lorentz-invariant continuum, stationarity, a classical record field, the OSSW/OWD/Layton structure, and the Maxwell stress as the vacuum probe.
- This contradicts the Z³ Lattice text (`AX:37-41`), as R6-4 and R12-4 already price (`C5_R12-4_report.md:176-186`).
- The Record text changes too: a metric record is dense and per event (`C5_R6-4_report.md:227-252`).

**What is proved.** Only what is marked PROVED below, plus what the sources prove in their own scopes (marked "source").

## Setting and premises (ASSUMED)
- **P1.** Linearized CQ gravity on Minkowski space, one spin channel at a time, second (golden-rule) order in the matter coupling. Source: `C5_R12-4_report.md:66-68`.
- **P2.** Translation-stationary statistics. Lorentz invariance is added only where stated. Source: `:70`.
- **P3.** A classical record J: self-commuting, with zero reverse gain (Belavkin non-demolition). The felt field is f = B + G_R·J, with G_R the standard undamped massless retarded propagator, |G_R|² = g²/s². Source: `:74-77`, `C5_R10-3_report.md:56-66`.
- **P4.** The forward gain F is the Kubo gain, F(0) = 1 and F is continuous at the cone (Newton plus finite radiation). Source: `C5_R12-4_report.md:76-77`.
- **P5.** Vacuum excitation rate = ∫ S_ff(−p) W(p), with W the vacuum Wightman weight of the stress. Source: `C5_R8-3_report.md:106-107`.

## Reconciliation of current attempts (READING, from the sources)
| Source | In its own scope | Bears on the stated question |
|---|---|---|
| R8-3 report | Lemma 1 (boost orbit), Lemma 3 (cone jump gives ln) | Treated additivity H3′ as part of class 𝒞 (`C5_R8-3_report.md:97-101`). |
| R8-3 referee/verdict | Narrow additive scalar or GR-normalized spin-2 subclass excluded; H3′ "not class-wide"; light-cone counterterms to be excluded explicitly (`C5_R8-3_referee_verdict.md:7,9,11,19`). | This task. |
| R9-4 verdict | Under (H-T): spacelike-only noise gives (ln r)/r; scalar noise cannot pay for spin-2; finite cone-supported delta derivatives cannot cancel the log. Correlated emission-cancelled histories remain open (`C5_R9-4_referee_verdict.md:5,7,9,15`). | Closes the finite-order counterterm question for the jump case. |
| R10-3 | Explicit model M_E: emission-silent, vacuum rate exactly 0, Newton and c_T pass; Theorem P: the classical record is not locally finite at the cone (`C5_R10-3_report.md:108-140,171-189`). Referee confirmed the dispersion step (`C5_R12-4_referee_verdict.md:11`). | **This is the "specified correlated kernel" the task asks for.** |
| R12-4 | Lemma K (any stationary state, non-demolition record): σ̄·P̄ ≥ ħ²\|F\|²/4. Theorem U: not both locally finite near a regular cone point. Referee: DERIVED in 𝒰 (`C5_R12-4_report.md:81-114`; `C5_R12-4_referee_verdict.md:5,7,19`). | Unified no-go. Open: E4, histories without a stationary non-demolition dilation (`:165`). |

So the stated escape has already been worked in R10-3 and bounded in R12-4. This attempt does not reinstate the withdrawn 32-orders exclusion, and does not call any preferred-frame smearing interval an allowed window.

## Numbered steps
**1. [ASSUMED]** P1–P5, plus: the "scalar" and "spin-2" channels are kept separate through steps 5 and 7; the retarded product G_R·F is a distribution on s = p² near the cone, for which step 6 states the prescription.

**2. [PROVED, source; CHECKED A1–A3b]** Product bound. Wightman positivity gives a_±·P ≥ |z_±|². The Kubo commutator gives |z₊ − z̄₋| = ħ|F|. Hence (a₊ + a₋)·P ≥ ħ²|F|²/2, and with emission silence (a₋ = 0 forces z₋ = 0) a₊·P ≥ ħ²|F|².
- This is R12-4 Lemma K in this notation (`C5_R12-4_report.md:83-89`).
- Here: the AM-QM identity is exact, an equality case is attained in rational data, and 6000 random exact rational feasible data have minimum ratio 1.0075 (emission-silent: 1.000000).

**3. [PROVED + CHECKED A4–A7] Exact sub-floor datum.** Take real gain G and record noise P. Emission side (−p): Σ₋ = P [[G², −G], [−G, 1]]. Absorption side (+p): S_BJ(p) = iħF − GP and S_BB(p) = (G²P² + ħ²F²)/P. Then:
- both Gram matrices are rank one, hence PSD;
- the Kubo commutator holds;
- the felt noise is S_ff(−p) = 0 and S_ff(+p) = ħ²F²/P exactly.

The additive (uncorrelated) minimum of the emission-side noise is |G|ħ|F|, at P* = ħ|F|/(2|G|). So 0 < |G|ħ|F|: positivity plus the commutator do **not** imply R8-3's pointwise additive floor. The product bound survives: (S₊ + S₋)P = ħ²F², ratio 2 to the minimum, which is the emission-silent value.
- *New relative to sources:* the exact symbolic form in (P, G, ħF). The sources give the same structure numerically (`C5_R12-4_report.md:97`; `C5_R10-3_report.md:110-130`). **This is not a new result.**

**4. [PROVED, source; CHECKED B1–B4]** Boost-orbit lemma (`C5_R8-3_report.md:116-123`, referee: essentially confirmed). Here: the invariant shell measure V(Λ) = π(Λ√(Λ²+m²) − m² asinh(Λ/m)) has V′ = 2πΛ²/E and V/Λ² → π; nine boosted copies of an energy window are disjoint in exact integers. A kernel with S_ff(−p) > 0 on a positive-measure subset of V₊ therefore gives an infinite rate, while an emission-silent kernel has integrand 0 (bookkeeping).

**5. [CHECKED exact C1–C7] Channels, kept separate.**
- The two-photon matrix element of the Maxwell stress is traceless and conserved in the pair rest frame, so it populates only the spin-2 channel.
- Spin-2 weight: W^{μνρσ} = a s² Π₂^{μνρσ} with a = 1/(40π), in the convention W = Σ_n (2π)⁴δ⁴ ⟨0|T|n⟩⟨n|T|0⟩, identical-photon factor ½, dΦ₂ = dΩ/(32π²).
- A conformally coupled real scalar run through the same code gives 1/(480π); the ratio is exactly 12, the standard c_T ratio. So the code reproduces a known number.
- *New relative to sources:* the coefficient, which R8-3 had only "recalled" as ≈ N_eff/960 (`C5_R8-3_report.md:104,216`). R8-3 gave no normalization convention, so I do **not** claim a mismatch.
- Barnes–Rivers contractions, exact:
  - Static mass–mass: spin-2 2/3, scalar 1/3, GR numerator 1/2.
  - A scalar coefficient 3/2 reproduces Newton's numerator with the spin-2 factor 0.
  - Mass–photon beam: scalar contribution exactly 0, spin-2 contribution equals the GR amplitude. So a scalar-only kernel cannot bend light.
  - This is the referee's point (`C5_R8-3_referee.md:137-156`) made exact.
- READING: scalar and spin-2 channels carry different physics. The photon vacuum excitation lives in spin-2 only, via a ∝ s². A trace-only kernel (OWD Eq. 25 as read by the referee) does not touch it, but it cannot give GR-normalized radiation (R9-4 (ii)). Everything below is per spin-2 channel; the TT tensor structure of the kernel is not built (step 8).

**6. [PROVED (lemma) + CHECKED D1–D7] Light-cone prescription and finite-bandwidth sources.**

*Prescription.* The retarded product G_R·F is defined as the Sokhotski–Plemelj limit
F(s)/(−s ∓ iε) → PV[F(s)/(−s)] ± iπF(0)δ(s).

*Lemma.* If F is Hölder-continuous at s = 0, that is |F(s) − F(0)| ≤ C|s|^α with α > 0, then:
- (F(s) − F(0))/s is locally integrable (checked: ∫₀¹ s^{α−1} ds = 1/α);
- the limit exists for every Schwartz test source;
- no cone-supported counterterm is needed or allowed beyond the fixed normalization F(0) = 1.

*Proof.* Split F = F(0) + (F − F(0)). The first term is the standard retarded Green function. The second has an integrable kernel, so dominated convergence applies to ε → 0.

*Numerics, finite-bandwidth source.* Gaussian pulse centred at ω = 2 with width 0.35, point source, observer at r = 3, 28 Gauss–Legendre nodes. Results of the ε sweep 1e-4, 1e-6, 1e-8:
- F = 1 matches the cutoff-weighted residue to 1e-6.
- A retarded massive-pole form factor F = μ²/(μ² − s) (so G_R·F = massless minus massive, GR-normalized at the cone) matches the residue form to 1e-6 and is ε-independent.
- A continuous kink form factor has an ε-limit (|I(1e-8) − I(1e-6)| = 1.7e-5, within quadrature accuracy of the integrals).
- A spacelike projector (jump) grows as ln(1/ε) with slope −0.07067, equal to the predicted ∫A(ω) sin(ωr)/2 g(ω) dω, with only the real (cone-delta) part divergent.

*Honest scope.*
- A finite-bandwidth pulse does not remove the jump log. This matches R8-3's lemma 3 and the referee's pulse coefficient (`C5_R8-3_referee.md:110-115`).
- The Hölder side is the part new here, checked numerically and not only argued. It is only as strong as the Gaussian-cutoff, point-source test, not a general theorem about all sources.
- READING: removing the jump log by an ε-dependent cone term would make the radiated amplitude depend on an arbitrary scale and on frequency. The finite-order delta-derivative case is closed in R9-4 (`C5_R9-4_referee_verdict.md:5`).

**7. [PROVED (algebra) + CHECKED E1–E8] The explicit kernel through the noise integrals.** Take P₊(s) = ħF(s + μ²)/(2gλ) on the timelike side (null-cone regulator μ, λ = 1 continues the static floor), S_ff(−p) = 0 and G = −g/s. Then:
- The absorption noise is 2ħgλF/(s + μ²).
- The vacuum excitation integrand is identically zero. The Gram matrices are rank one at every p.
- **σ·M = ħ²g²F²/s² exactly**, for every μ and λ. This saturates Cauchy–Schwarz, so no choice of profile improves it.
- ∫M ds = (ħgF/2λ)[ln(δ/η) + μ²(1/η − 1/δ)] → ∞ as η → 0. The divergence is logarithmic at μ = 0 and a 1/η power at μ > 0, which is the null-pumping case of R10-3's table (`C5_R10-3_report.md:191-198`).
- Absorption of a smooth finite-bandwidth source grows as ln(1/μ²): the increment per two decades in μ² is 2 ln 10 to 0.002. So the null regulator cannot be removed, and the absorbed-energy log is the matter-side cost.

**8. [FIRST UNRESOLVED] History-level realization.** Steps 2–7 are statements at each four-momentum p, at golden-rule order. Three things are not shown here.
- (a) That the saturated kernel is a genuine completely positive history: a stationary Gaussian dilation with self-commuting J, zero reverse gain and a TT-valued gain. The sources give a one-shell operator model (negative-energy partner, `C5_R10-3_report.md:136-140`, Lemma Q at `:144-151`) and say the full spectra are singular at the cone (`:135`). No full dilation is built or checked here.
- (b) E4: whether every stationary CP Gaussian CQ history has a non-demolition dilation. If it does, Lemma K applies to all of them and the escape is closed class-wide in the stationary Gaussian linear setting; if not, the failing history is the escape. `C5_R12-4_report.md:165` lists it as open; I did not advance it.
- (c) Orders above golden-rule and the nonlinear completion (`C5_R12-4_report.md:164`).

SUGGESTED, not checked: for stationary kernels all bilinear terms are frequency-diagonal, so Hamiltonian cross terms of the Wiseman–Milburn type cannot create pairs from the vacuum at this order. I did not examine higher orders.

## What is new, and what is not
**Not new (retrieval, reconciliation, scope cleanup):**
- the kernel M_E and its properties (R10-3);
- the product bound and Theorem U (R12-4);
- the jump log (R8-3, R9-4);
- the 32-orders and preferred-frame-window cautions (kept off).

**New, small, checked:**
- the exact symbolic sub-floor datum (step 3);
- the Maxwell spin-2 weight a = 1/(40π) in a stated convention, with a scalar cross-check at ratio 12 (step 5);
- exact Barnes–Rivers contractions (step 5);
- the Hölder-form-factor prescription lemma, with finite-bandwidth numerical confirmation of both the finite and the divergent side (step 6);
- the exact identity σ·M = ħ²g²F²/s² and the 1/η form of the μ > 0 divergence (step 7).

No new demonstrated defect in a source was found, so no HIT line is printed.

## Strong words checked
"Exactly zero" refers to golden-rule order and to the emission-silent per-momentum data only. "Finite response" refers to a Hölder-continuous F and the Gaussian-cutoff point-source test. "Not locally finite" means the one-sided cone-neighbourhood integral of M diverges, as in R12-4 (`C5_R12-4_report.md:195`). Nothing here is a retained result, and the Lorentz-invariant continuum premise conflicts with the Z³ Lattice axiom (`AX:37-41`).
