# C5 round 10, probe R10-3: an emission-cancelled classical–quantum hybrid (worker report)

**Worker.** Claude Opus 5.5, the same family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-12, 18:00Z to 18:24Z. No repository file was edited.

**Scratch folder:** `scratchpad/C5/R10-3/`.
- `scripts/r103_checks.py` and `scripts/r103_checks.out` (sections [1]–[9]) hold every number below. Runtime about 2 s.
- SHA-256 of the script: `ca33798c…880c`. SHA-256 of the output: `124448df…96e5`.
- The only warning in the output (`.out:1-7`) is a quadrature-subdivision notice from section [6]. The [6] growth exponents agree with the analytic scalings.
- No downloads. The local text of Lee et al. 2020 (`scratchpad/C5/ref_R6-4/sources_untrusted/source_Lee_2002.11761.txt`) was read as data only (cited as `LEE:`).

**Path abbreviations.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; bare `C5_*` files are in `P/agents/`.

**What I read.**
- In full: `AX`.
- C5 method and readings: `TESTS:2302-2329`.
- The set-A entries: R2-3 (`:2533-2560`, `:2721-2727`), R3-4 (`:2696-2706`, `:2774-2786`), R4-4 (`:2834-2850`, `:2930-2937`), R6-4 (`:3143-3175`, `:3409-3418`), R8-3 (`:3468-3481`, `:3559-3573`), R9-4 (`:3707-3738`, `:3909-3916`), and Round 10 (`:3958-4025`). My item is `TESTS:3997-4011`.
- `C5_R9-4_report.md`, `C5_R9-4_referee.md` and `C5_R9-4_referee_verdict.md` in full, plus `scripts/C5/R9-4/r94_checks.{py,out}`.
- `C5_R8-3_report.md`, `C5_R8-3_referee.md` and `C5_R8-3_referee_verdict.md` in full.
- `C5_R6-4_report.md` and `C5_R6-4_referee_verdict.md` in full.
- `C5_R4-4_referee.md` in full, for Lemma N and BMV.

**Labels.**
- **proved:** derived here under the stated hypotheses.
- **checked:** a number in `r103_checks.out`.
- **suggested:** argued, not proved.
- **reading:** an interpretation.
- **comparator:** literature, marked web-checked (this run), local text, via an earlier C5 file, or RECALLED.

---

## Reading against the FIXED rule (`TESTS:4007-4011`)

**Worker reading: OPEN.** The two conditional readings below need the referee.

**What passes.** An explicit model, M_E (§2), passes every *matter-side* stated test at linear, golden-rule order:
- a Newtonian limit in R6-4's window, with one new constraint;
- γ = 1 and c_T = 1;
- a vacuum-excitation rate of exactly zero;
- finite and negligible absorption;
- BMV: no entanglement.

**What fails.** M_E fails the **null-cone pumping** test (R8-3's second horn) for its *classical record*. Theorem P (§4) shows this failure holds for every member of the class, not only for M_E:
- Take an emission-cancelled linear-meter hybrid with Newton, finite radiation and a finite vacuum rate.
- Its classical metric record cannot be a locally finite random field at any regular point of the null cone.
- Its on-shell (gravitational-wave) content grows without bound.
- Matter never feels this content at linear order, because the cancellation that silences the vacuum also hides the record.

**Conditional readings** (for the referee and the owner):
- **VIABLE at linear order**, *if* price P-r10b is accepted: the record's null and timelike content is unread and does not gravitate. BMV prediction: **none** (zero entanglement in the static geometry).
- **EXCLUDED, worker reading, subclass only** (referee required): every member of 𝒯_E (defined below) in which the classical record must be a locally finite field, or must carry its own gravitational-wave energy. Basis: Theorem P plus [5]–[6].

**Against the expectation.** No expectation was registered. The decisive new structural facts are:
- **The closed loop obeys a fluctuation–dissipation identity** (§3). It makes the hybrid's timelike sector exactly a zero-temperature quantum bath, with a forced massive continuum.
- **A ground-state meter cannot write a classical record with gain** (Lemma Q).

**Class 𝒯_E (stated before any title).** R9-4's class 𝒯 (`C5_R9-4_report.md:39-45`), with the additivity assumption removed:
- linearized gravity on Minkowski space;
- translation-invariant and Lorentz-invariant stationary Gaussian statistics;
- a meter with input/backaction operator B and a self-commuting classical record J ([J(x), J(y)] = 0 for all x, y);
- zero reverse gain;
- the classical field h = G_R J, with G = −g/(s + iε p⁰) the standard massless retarded propagator, where s = p²;
- matter couples to B and to h, so it feels f = B + G_R J;
- the forward gain F has F(0) = 1 and is continuous at the cone, as forced by Newton plus finite radiation (R8-3 Lemmas 3–4; R9-4 Lemma L, refereed: `C5_R9-4_referee.md:35-49`);
- golden-rule order.

Positivity of the unsymmetrized (B, J) spectral matrix replaces (H-T). It implies (H-T) by the R9-4 referee's derivation (`C5_R9-4_referee.md:17-31`).

---

## 0. In plain words

- **The idea.** Use a classical metric for static gravity, so it can decohere and need no graviton. Then arrange the measurement noise and the feedback to cancel exactly, for every process in which empty space could give energy to matter. That cancellation is what keeps the vacuum quiet.
- **It can be built** (M_E, §2). At each 4-momentum the noise matrices are positive, the commutators are right, the vacuum gets nothing, and Newton, light bending and the speed of gravitational waves all come out right.
- **The price shows up in three places.**
  1. **The meter cannot be in its lowest-energy state.** A meter in its ground state cannot write a classical record that carries information (Lemma Q). With free-field meters, the record needs a partner sector of *negative* energy, the "quantum-mechanics-free subsystem" trick. Matter must never touch that partner, and the vacuum cancellation is exactly that condition.
  2. **What matter feels at timelike transfers is quantum.** The cancellation turns the felt field into a zero-temperature quantum bath. It is quantum gravity, plus a hidden family of massive spin-2 and spin-0 modes. Matter can lose energy into them at rates no larger than ordinary graviton emission, so harmless. The modes also change Newton's law below a length 1/μ, which must be under about 10 µm.
  3. **The classical record itself blows up on the light cone.** Gravity's record must carry noise where it pulls. Near the light cone, the quantity that would keep the record finite and the quantity that would keep the static force finite are tied together. They cannot both be finite: either the static force is infinite, or the record's gravitational waves grow without end. The model chooses the second. Matter never feels this, because the cancellation hides it.
- **So.** "Records are the metric" survives only for static (spacelike) transfers. There the record's noise is felt, gravity is classical, and BMV sees no entanglement. At light-cone and timelike transfers the record is an unread, ever-growing bookkeeping field, and the physics is quantum.

---

## 1. Prior art (each counted once)

1. **R9-4** (refereed; `TESTS:3909-3916`; `C5_R9-4_referee_verdict.md:9`).
   - Lemma E holds almost everywhere: a finite vacuum rate forces emission-side rank-one cancellation and absorption ≥ |F|²/S_JJ.
   - OWD Eq. (27) is additive.
   - The joint-meter toy is illustrative only.
   - The referee's 1/|s| non-integrability point (`C5_R9-4_referee.md:81`) is generalized here as Lemma Z.
2. **R8-3** (refereed; `TESTS:3559-3573`).
   - Lemma 1 (a Lorentz-invariant positive measure is zero or infinite).
   - Lemma 3 (a jump gives ln(1/ε)).
   - The second horn (`C5_R8-3_report.md:164-167`): P_J(0) > 0 pumps classical gravitational waves.
   - The additivity caveat (`C5_R8-3_referee.md:90-96`).
3. **R6-4** (refereed; `TESTS:3409-3418`).
   - The Newtonian least-decoherence floor.
   - The window 4e-10 to 5e-6 m.
   - The record-reading prices on all four axioms (`C5_R6-4_referee_verdict.md:19`).
4. **R4-4 Lemma N** (`TESTS:2935`; `C5_R4-4_referee.md:43`): a classical c-number channel gives zero concurrence, against 0.156 in the benchmark.
5. **R2-3 and R3-4.** Bianchi and escape bookkeeping (`TESTS:2721-2727`, `:2774-2786`). Not load-bearing here.
6. **Literature.**
   - Clerk et al., RMP 82, 1155, Eq. (90). Web-checked in R9-4 and by its referee; not re-fetched.
   - Wiseman–Milburn, PRL 70, 548 (1993): feedback master equation. Abstract confirmed by web search this run.
   - Tsang–Caves, "Evading quantum mechanics", PRX 2, 031016 (2012): quantum-mechanics-free subsystems (QMFS). Title and venue confirmed by search this run. The negative-mass construction is RECALLED.
   - Kafri–Taylor–Milburn (classical-channel gravity with local meters) and Diósi/Tilloy (least decoherence): RECALLED.
   - Existence of quasi-free CCR states given a positive two-point function (Manuceau–Verbeure/Araki): RECALLED.
   - Lee et al. 2020 ISL: local text (`LEE:13,421`), "λ < 38.6 µm" for |α| = 1.

## 2. The explicit model M_E

At each 4-momentum p, with G = G(p), F = F(p), P = S_JJ(p) = S_JJ(−p):

**Timelike p ∈ V₊ (absorption side p, emission side −p).**
- S(−p) = P·w w† with w = (−G(−p), 1): rank one, with null vector [1, G(−p)].
- S_JB(p) = iħF − Ḡ(p)P, from the commutator identity S_JB(p) − S_JB(−p)* = iħF. Zero reverse gain makes this exact, not only its spectral part.
- S_BB(p) = |S_JB(p)|²/P, the minimal choice.

**Spacelike p.** G and F are real. The model is additive, with symmetrized B–J correlation zero, and sits at the AM–GM floor: P = ħ|F|/(2|G|), S_BB = ħ|G||F|/2. This is R6-4's least-decoherence kernel.

**Free functions.**
- **Record noise on the timelike side:** P₊(s) = ħ|F|(s + μ²)/(2gλ). λ = 1 and μ = 0 continue the static floor; μ is a null-cone regulator.
- **Form factor F(s).** Lorentz-invariant and retarded, with F(0) = 1. It must be bounded, decay at large |s| on both sides, and have no real-axis pole. One example: a Källén–Lehmann form ∫dm² w(m²)/(m² − s − iε) with smooth w and superconvergence sums (suggested). The Gaussian e^{ℓ²s} is barred by R8-3.

**Checks.**
- **[1], checked.** Over 20000 random (G, F, P):
  - minimum eigenvalue/P = −2e-15 (positive up to rounding);
  - commutator error ≤ 1.8e-14;
  - emission side S_ff(−p) = 0 to 1e-15;
  - absorption S_ff(p) = ħ²|F|²/P, to 3e-9 (rounding at large |G|).
- **[1], spacelike floor:** S_ff = |G||F| = 2.160000 on both ±p.

**Realization.**
- The spectral matrices are positive and causal:
  - C_BB is odd and Lorentz-invariant, so it vanishes at spacelike p and is a superposition of Pauli–Jordan functions;
  - C_JB = iħF is retarded.
- So a quasi-free (Gaussian) CCR state realizes them (comparator, RECALLED), **wherever the spectra are locally finite**. Theorem P shows that the B and J spectra are *not* locally finite at regular null points; only f's spectrum is. So the dilation is singular on the cone, and only the matter-side influence functional (R, S_ff) is regular.
- **Operator realization (one frequency shell; [4], checked).**
  - H = ω(a†a − b†b) in |0_a, 0_b⟩, with J = x_a + x_b.
  - ⟨[J(t), J(0)]⟩ ≤ 4e-17 and ⟨J(t)J(0)⟩ = cos ωt: a symmetric (classical) spectrum.
  - A Hermitian f has emission-side weight exactly when it has a b-component (0.0200 and 0.0050 in the two b-containing examples, 0 otherwise).
- **Lemma D (proved, single shell):** emission silence holds if and only if f has no b-sector component. The negative-energy sector enters only J. Matter couples to the positive-energy sector a, in its vacuum.

## 3. Structural lemmas

**Lemma Q (a ground-state meter writes no classical record with gain).** Take any translation-invariant meter state satisfying the spectrum condition (S_XY(p) supported in V̄₊), and a self-commuting J. Then F(p) = 0 for every p ≠ 0, even if commuting classical noise is added.
- *Proof.*
  1. Self-commutation and stationarity give S_JJ(p) = S_JJ(−p).
  2. The spectrum condition then confines S_JJ to {0}.
  3. Positivity gives |S_JB(±p)|² ≤ S_BB·S_JJ = 0.
  4. So C_JB = S_JB(p) − S_JB(−p)* = 0, that is, F = 0. ∎
- [proved; no Lorentz invariance needed.]
- In the laboratory the energy comes from a carrier (a local oscillator). A carrier selects a frame, so a Lorentz-invariant meter cannot use one (reading).

**Lemma Q′ (free-field meters need negative energy).** For a meter built from free or generalized free fields, commutators are state-independent c-numbers. A positive-energy field contributes ρ_i ≥ 0 to C_JJ. So [J, J] = 0 with nonzero gain at p needs a component with negative commutator weight at p: a negative-energy sector, the QMFS type.
- [proved for free-field meters. Open for interacting meters.]

**Closed-loop FDT identity.** In 𝒯_E the matter response is R = χ_BB + G F, and it equals χ_ff exactly.
- *Proof.* The cross-term [B(x), J(z)]G(−z) is advanced, so θ(x⁰) kills it. Then C_ff = C_BB − 2ħ Im(GF), and Im R = −C_ff/(2ħ).
- [proved; checked [3]: error 2.5e-15.]
- **Consequence.** In *any* member of 𝒯_E, matter's Gaussian dynamics is that of a Hamiltonian coupling to a quantum bath field f. "Classical versus quantum" lives only in the state S_ff.
- **With emission silence on the timelike side:**
  - C_ff = S_ff(p) ≥ ħ²|F|²/P₊: a **zero-temperature quantum field**;
  - with Källén–Lehmann density ρ(s) = |Im R|/π ≥ ħ|F|²/(2πP₊) > 0;
  - plus the massless pole from G, whose Im G = πgδ(s) puts a massless quantum mode into f.
- The hybrid's timelike/null physics is therefore **linearized quantum gravity plus a forced massive spin-2/spin-0 continuum (the "tower")** [proved under 𝒯_E]. This sharpens R9-4's P-r9a from "reasonable interpretation" (`C5_R9-4_referee.md:73`) to an identity within 𝒯_E.

**General correlation bound.**
- At any p, for any correlation: σ := S_ff(p) + S_ff(−p) ≥ ħ²|F|²/(2P).
- With emission silence the absorption side alone is ≥ ħ²|F|²/P.
- [proved; checked [2]: minimum ratio 1.083 over 50000 random draws; the bound is attained exactly (ratio 1.000000) in the constructed case.]

## 4. Theorem P (the record is null-pumped)

**Lemma Z (null-cone dichotomy).** In 𝒯_E, take any regular null point p₀ ≠ 0 with F(p₀) ≠ 0 and any δ > 0. Then ∫_{0<±s<δ} σ ds and ∫_{0<±s<δ} |G|²P ds cannot both be finite.
- *Proof.* σ·|G|²P ≥ ħ²g²|F|²/(2s²). Cauchy–Schwarz then gives ∫√(σ|G|²P) ≥ (ħg/√2)∫|F|/|s| ds = ∞. ∎
- [proved. checked [5]: for P = s^a, √(∫ρ·∫rec)/ln(1/δ) ≥ 1 for all a, equal to 1 at a = 1, and the product diverges in every case.]
- Lorentz invariance is used only to reduce local finiteness of the 4D measure to integrability in s. The lemma therefore also applies to preferred-frame models near null points where F ≈ 1, such as R9-4 (iv). This generalizes the R9-4 referee's 1/|s| objection to every correlation structure.

**Theorem P.** Assume 𝒯_E plus:
- (V) a finite vacuum rate, which implies emission silence almost everywhere on the timelike region (R9-4 Lemma E, refereed);
- (N) a finite static response at some s < 0.

Then ∫_0^δ |G|²P₊ ds = ∞ for every δ. The record h = G_R J has a non-locally-finite spectral measure next to every regular null point.

*Proof.*
1. By the FDT identity, Im R = πρ with ρ ≥ ħ|F|²/(2πP₊) ≥ 0.
2. Since ρ ≥ 0, R(s < 0) contains ∫_0^δ ρ(s′)/(s′ − s) ds′. Polynomial subtractions do not change the s′ → 0 end, so (N) forces ∫_0^δ ρ < ∞.
3. Lemma Z, with the emission-silent bound, then gives the result. ∎

[proved under the stated hypotheses; a no-go, so **referee required**.]

**What it means ([6], checked).** Drive one on-shell record mode with noise of spectrum P(|ω² − k²|). Its energy grows:

| P near the cone | Growth of the mode's energy | E(T) at T = 1e1 → 1e4 |
|---|---|---|
| P(0) > 0 | linear in T | 4.9 → 5000 |
| P ~ \|s\|^0.5 | as T^(1−a) | 3.2 → 112 |
| P ~ \|s\| | as ln T | 3.4 → 7.8 |
| P ~ \|s\|² | bounded | 24.7 → 24.5 |

But bounded growth (P vanishing faster than |s|) is exactly the case where ∫ρ = ∞, so the static force becomes infinite.
- For P(0) > 0, the pumped energy summed over the Lorentz-invariant null cone is infinite (R8-3's second horn, via Lemma 1).
- For any P, the record is not a stationary random field.

**Escapes not covered.** Each fails at least one hypothesis:
- a non-massless or modified G (costs radiation);
- an F that jumps at the cone (Lemma L);
- non-Gaussian, jump or interacting meters;
- a non-stationary meter with a start time (then the secular growth is the physical statement);
- dropping the requirement that the record be finite (price P-r10b).

## 5. The stated tests for M_E (`TESTS:4000-4006`)

1. **Newtonian limit.**
   - **Spacelike sector.** It is R6-4's least-decoherence kernel, so R6-4's laboratory table carries over (reading, as in `C5_R9-4_report.md:221`).
     - The bounded, decaying, Lorentz-invariant form factor shifts the window ends at O(1) relative to R6-4's Gaussian. Not recomputed (suggested).
     - BMV-negative needs the spacelike noise to cover the total static response, tower included. That costs extra noise ≤ the tower fraction (below), negligible against R6-4's 9–22-decade margins (suggested).
   - **Tower.** ρ = (λg/π)/(s + μ²) gives δV/V_N = (2λ/π)∫x e^{−xr}/(x² + μ²)dx (attractive; suggested sign).
     - **checked [7], λ = 1, 1/μ = 1 µm:** 4.3e-4 at 38.6 µm; 6.4e-7 at 1 mm; 6.4e-9 at 1 cm; but 1.19 at 0.1 µm.
     - **1/μ = 10 µm:** 3.4e-2 at 38.6 µm; 6.4e-5 at 1 mm.
     - Lee et al. allow an |α| = 1 Yukawa only below 38.6 µm (`LEE:13,421`). So **1/μ ≲ 10 µm at λ = 1** passes at the order-of-magnitude level. The tail goes as (μr)^−2 rather than e^{−μr}, so it is not a single Yukawa and no exact fit was done.
   - **Pass, with the tower price.**
2. **γ and c_T.**
   - The mean field is linearized GR plus the tower.
   - The tower's static contribution at 1 AU is ~(2/π)(μ·1 AU)^−2 ≈ 3e-35. With the massive-spin-2 trace factor 2/3, γ − 1 ≈ −(2/3)·3e-35 (suggested arithmetic).
   - The massless pole of R is untouched; the tower is a continuum of masses ≥ 0, so subluminal. So **c_T = 1** for the pole (proved).
   - Near the cone the tower adds a log branch point, ln(−s), which gives 1/r² tails, not a ln r radiation term (suggested).
   - Tower emission by binaries relative to gravitational waves is ~(λ/π)(ω/μc)² ≲ 1e-23 (suggested).
   - **Pass.**
3. **Null-cone pumping.**
   - **For the record: FAIL** (Theorem P; [5]–[6]).
   - **For matter: no effect at linear order.** The felt field f is emission-silent, and its absorption ħ²|F|²/P₊ stays finite when P₊(0) > 0 (proved).
   - Beyond linear order, a second-order coupling of matter to h² would expose the divergent record, and nothing in the linear B cancels it (**suggested**: a likely nonlinear failure, not computed).
4. **Vacuum excitation.**
   - **Exactly 0 at golden-rule order** (proved): emission-silent on V₊; W_vac = 0 at spacelike p; W_Maxwell ∝ s² on the cone.
   - Any residual mismatch ε ≠ 0 on a set of positive measure gives an infinite rate (Lemma 1). The cancellation must be exact. In the QMFS realization it is structural: the b-sector is a decoupled spectator (Lemma D).
5. **Absorption into the meter.**
   - The rate is S_ff = ħ²|F|²/P₊, finite.
   - **Relative to the graviton-like quadrupole rate** (own order of magnitude, [8]): 2.8e-40 s⁻¹ at 10 eV and 2.8e-30 s⁻¹ at 1 keV. The tower factor (λ/π)ln(1 + ΔE²/μ²) is 2.5 at 10 eV and 5.4 at 1 keV (λ = 1, 1/μ = 1 µm).
   - **CMB photons** into the tower: about 3e-53 s⁻¹ (σ ~ λℓ_P²; O(1) suggested).
   - Matter only *loses* energy into the meter; there is no heating at timelike transfers.
   - **Pass** (suggested magnitudes).
6. **BMV.**
   - **Prediction: no gravitationally mediated entanglement** in the static BMV geometry.
     - The static transfers are spacelike, and the noise there covers the total response, so the channel is LOCC and Lemma N applies. Concurrence 0, against 0.156 in the R4-4 benchmark.
     - **checked [9]:** local-meter toy at tower fractions 0, 1e-3 and 0.1 gives negativity 0, against 0.354–0.380 for coherent coupling.
   - Timelike-sector leakage into slow BMV is suppressed by (ωΔx/c)² ≈ 4.4e-24 (checked [9], ω = 2π/2.5 s, Δx = 250 µm).
   - **A positive BMV result would exclude the spacelike classical sector, hence M_E.**

## 6. Prices (named, none adopted)

- **P-r9a, now proved within 𝒯_E.** At timelike and null transfers, matter feels a zero-temperature quantum field, with gravitons and a tower. "Records are the metric" holds only at spacelike transfers.
- **P-r10a.** A meter that is not in a ground state (Lemma Q). For free-field meters, a negative-energy (QMFS) sector, exactly decoupled from matter (Lemmas Q′ and D). The meter does not gravitate.
- **P-r10b.** The classical record is not a locally finite field near the null cone. Its on-shell content grows secularly and is never read or gravitating (Theorem P).
- **P-r10c.** Exact emission cancellation almost everywhere on V₊, at linear order only. Any residual coupling to the negative sector gives an infinite vacuum rate.
- **P-r10d.** A hidden massive spin-2/spin-0 continuum, with ρ ≥ ħ|F|²/(2πP₊). Gravity is O(1)-modified below 1/μ ≲ 10 µm (λ = 1), and there is an extra, negligible, dissipative emission channel.
- **P-r10e.** A null-cone regulator μ (P₊(0) > 0). The spacelike floor keeps R9-4's 1/|s| logarithm near the cone, regulated by finite time as ln(ωT) (R9-4 referee).
- **Carried from R6-4:** P-i1 (smearing), P-i2 (the DP floor), P-i4 and P-i5. **P-i3 ("no graviton") no longer holds** for f at null transfers.

**Axiom texts touched (reading).** R6-4's (iii) prices stand (`C5_R6-4_referee_verdict.md:19`):
- **Lattice** (`AX:37-41`): replaced by a Lorentz-invariant continuum.
- **Qubit** (`AX:45-53`): the possibility domain also needs a negative-energy meter algebra.
- **Admissibility** (`AX:57-61`): not nearest-neighbour.
- **Record** (`AX:77-83`): a readable classical value per event, but **not a finite value at null transfers** (Theorem P). This conflicts with "locks exactly one admissible local possibility" for those components.

## 7. Strong words checked

- **"Every member", "cannot" (Theorem P, Lemma Z)** mean within 𝒯_E, at golden-rule order, with Lemma E's almost-everywhere silence, F continuous with F(0) ≠ 0, and the standard G.
- **"Infinite"** means not locally integrable in s (a non-locally-finite measure), or Lemma 1's boost-orbit infinity. Each use says which.
- **"Proved"** is used for:
  - Lemmas Q, Q′ (free fields), D (single shell) and Z;
  - the FDT identity;
  - Theorem P;
  - the vacuum-zero statement;
  - c_T = 1 for the pole.
- **Suggested only:** the tower's sign, the ISL comparison (not a fit), all absorption magnitudes, γ − 1 arithmetic, the 1/r² tails, the nonlinear failure, and the O(1) shift of R6-4's window for a Lorentz-invariant F.
- **Not shown:** existence of a bounded, retarded, superconvergent F with all the decay R6-4 needs, beyond the form given; CP of the full history beyond the quasi-free realization (which itself is singular on the cone).

## 8. What would decide it

1. **A referee of Theorem P**, including the step (N) ⇒ ∫ρ < ∞ (dispersion representation and subtractions), and of the FDT identity and Lemma Q.
2. **The owner decision** on P-r10b: may a classical record be non-locally-finite and inert at null transfers? If yes, M_E is VIABLE at linear order with the prices above. If no, the subclass is EXCLUDED.
3. **The second-order coupling of matter to h²** in M_E, which decides whether the linear cancellation survives.
4. **Interacting (non-free-field) meters**, the only route around Lemma Q′.

**Sources.**
- Web search this run:
  - [Wiseman–Milburn, PRL 70, 548](https://link.aps.org/doi/10.1103/PhysRevLett.70.548) (abstract);
  - [Tsang–Caves QMFS](https://ar5iv.labs.arxiv.org/html/2308.08919) (citation via Silagadze; title and venue only).
- Via R9-4: Clerk et al. 0810.4729, Eq. (90).
- Local text: Lee et al. 2002.11761.
- RECALLED: Kafri–Taylor–Milburn; Diósi/Tilloy; quasi-free CCR state existence; graviton quadrupole rate scaling.
