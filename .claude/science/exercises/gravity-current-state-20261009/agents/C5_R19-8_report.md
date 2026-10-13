# C5 round 19, probe R19-8: set A's leak route E2 under the same source analysis (worker report)

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-13, 04:19Z to about 04:55Z. No repository file was edited.

**Scratch:** `scratchpad/C5/R19-8/`. Every runtime is under 20 s with OMP_NUM_THREADS=2. SHA-256 prefixes (script / output):
- `scripts/r198_modes.py` / `.out` (066ac27fcb5c / 15e0e10d2081), section [M]: sympy per-mode O(G·noise²) mean source of E2 + N_c in the harmonic law with friction, all six channel variables, insertion weight a.
- `scripts/r198_split.py` / `.out` (2ff8f9509b27 / 7fb6f00b9080), section [S]: the least-decoherence split with the damped response, Theorem I₀ for E2, the general-a harmonic totals, and the near-cone band.
- `scripts/r198_sink.py` / `.out` (e848a27cf27c / 2845a0dc22e0), section [K]: Π at k = 0, the frame dipole as the sink's field, the per-mode sink heating, and the budget numbers.
- `scripts/r198_cp.py` / `.out` (03f7c4b0318c / 8fb0e9226330), section [C]: a toy CP check with a dissipative readout.
- `rerun/`: copies of the archived R12-7, R14-2, R16-14, R18-7, R18-11 and R19-2 runners (14 scripts). **All 14 rerun with exit 0, and their outputs are identical to the archived `.out` files except for the printed runtime lines** (checked: `rerun/summary.txt`; the diffs are `runtime x.x s` only, in r187_ll, r1811_modes, r1811_insertions and r192_modes).
- No downloads and no web fetches. Literature is labelled RECALLED.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `rR12-7:n` = `P/agents/C5_R12-7_report.md:n`; `vR12-7:n` = `P/agents/C5_R12-7_referee_verdict.md:n` (and so on for every item).
- `vR19-2` = `P/agents/C5_R19-2_referee_verdict.md` (recorded during this run).
- `M:n`, `S:n`, `K:n`, `C:n` = line n of `r198_modes.out`, `r198_split.out`, `r198_sink.out`, `r198_cp.out`.

**What I read.**
- In full: AX; `TESTS:2302-2320` (the C5 method); the set-A entries and verdicts `TESTS:3143-3175, 3409-3418, 4218-4243, 4325, 4438-4446, 4449-4462, 4518-4560, 4682-4733, 4815-4923, 4939-4995, 5108-5140, 5177-5185, 5286-5290, 5433-5448, 5628-5666, 5875-5887, 5998-6017, 6713-6748, 6898-6955, 7020-7040, 7186-7230, 7282-7394`; R19-6..8 `TESTS:7395-7469`; the R19-6 worker line `TESTS:7568-7579` (appeared during the run).
- Reports and verdicts: `rR12-7`, `vR12-7`, `rR14-2`, `vR14-2`, `rR18-7`, `vR18-7`, `rR19-2`, `vR19-2` (and the scratch long form `ref_R19-2/C5_R19-2_referee_verdict.md`), `vR16-14`, `vR18-11`, `rR18-11:100-200`.
- Runners: `r192_modes.py`, `r192_split.py`, `r187_checks.py` [7].

**Labels.** **proved** (derived here under stated hypotheses); **checked** (a number or identity in my `.out` files); **suggested** (argued, not proved); **reading** (interpretation); **comparator** (literature, RECALLED or via an earlier referee). **Order rule:** O(G) mean field plus O(G²) static for β; Gaussian order in the matter–meter coupling for CP; O(G·noise²) for the noise mean; first order in γ where stated, otherwise exact in γ per mode.

---

## Reading against the FIXED readings (`TESTS:7466-7468`)

**Worker reading: E2-CONSTRUCTED, in a stated scope.** This is not a FAIL or a no-go, so a referee is not mandatory. One is recommended, because the registered expectation (`TESTS:7469`) was E2-OBSTRUCTED.

**Scope.** It is the scope of vR18-7 (`vR18-7:26`), plus the E2-specific items:
- weak field; static and quasi-static sectors at O(G²); the stationary noise at O(G·noise²) on Minkowski;
- the harmonic gauge, which E2's friction makes physical (it is the law, not a choice);
- finite rational meter networks (`vR15-2:15`) with R14-2's damped single-port meter (`rR14-2:203-207`);
- Π causal and non-local (`vR18-7:3`);
- ohmic γ in the drag-allowed range (`vR14-2:3`; its strong-field use is suggested), or R14-2's zero-integral kernel (P-r14a);
- the noise budget at the complete split (P-r192b), which vR19-2 confirms only off the cone (`vR19-2:5`);
- FRW only through the conservation core of Lemma F0, which vR19-2 confirms (`vR19-2:7`).

| Clause of E2-CONSTRUCTED | Result | Label |
|---|---|---|
| explicit E2 + N law at O(G²) | E2 + N_c (§3.1): R18-7's law with □ replaced by □ − γu·∂ in the gothic readout, a = 2, the same Π. The friction's linear stress X̃ = −(γ/16πG)∂_t h̄ and the Π completion together are the sink. | proved (construction); checked `M:2-4`, `K:1-2` |
| conserved source | G^{αβ}[g] = 8πG T_eff, with (−g)T_eff = Π[S] − Λ + X̃. T_eff is conserved by construction. Separately, X̃ is flat-conserved at O(G) (`M:3`) and the harmonic condition propagates (`M:2`). | proved; checked |
| well-posed readout | Each order is a damped wave (telegraph) equation with a retarded kernel that is causal and boost-stable (`rR12-7:113-116`, `vR12-7:17`), plus a causal Π. The free data are zero at t₀ (P76/P88), or there is an attractor under P-r14b. | proved (structure); stability in boosted frames sampled (`vR14-2:5`) |
| CP | Kraus U_r A_r: an adaptive Gaussian meter (a = 2) followed by record-controlled feedback. The friction and the sink live entirely inside the deterministic classical record-to-metric map (`vR18-7:11`). Toy: the Choi matrix is PSD, the map is linear, and h is a function of the records alone (`C:1`). | proved (structural); checked (toy) |
| β = γ = 1 | The friction vanishes identically on static fields, so the static O(G²) sector is E1 + N_c's: β = 1 after mass renormalisation (`vR18-7:13-18`), and γ = 1 at O(G). The matter part enters as (−g)T at any a. | proved |
| noise budget | Per mode, **E2 = \|R\| × E1** exactly, with \|R\| = \|1 − x²\|/√((1 − x²)² + g²x²) ≤ 1 and g = γ/ck (`M:22-23`, `S:1-3`, `S:6-20`). Theorem I₀ carries over: spacelike modes give 0, timelike modes give \|R\|(4, −4)u₀ (`S:23-24`). | proved; checked |
| sink budget | The linear sink stress has zero monopole and is the source of the known frame dipole (`K:4-5`). At O(G²) the sink is inside Π: per mode the sink takes exactly the noise's work (`K:11`). At the complete split, spacelike modes heat it at a rate of exactly 0; timelike modes heat it at a positive rate (`K:17-18`). The homogeneous K is pressureless (`K:2`). So the sink adds nothing to p_tot, and Lemma P (Minkowski) and Lemma F0 (FRW) apply unchanged. | proved; checked |

**Caveats that bound the reading:**
1. **The near-cone band (new; proved formula, suggested size).**
   - Inside the friction band |1 − x²| ≲ g, the complete split's S-block power is P_E1/|R|, with ρ power 2√D′/(1 − x²)² (`S:46-47`). Its integral grows as γt/4 (`S:48-53`).
   - Under P-r14b (stationarity, t ≫ 1/γ), the strict complete split is therefore not record-finite at the cone. That is the local-finiteness failure of R10-3/R12-4.
   - A cap in the band is a new datum (P-r198c). The tested cap leaves an uncancelled residual of 2.31 per shell, ≈ 0.8% of the leading-log near-cone TT stress at record-noise g (`S:54-59`).
   - On a t_H history the excess is ≤ γt_H/4 ≤ 0.012 of a shell floor (`S:49-50`), so no cap is needed.
2. **FRW.** The friction's FRW lift is law data (P-r198a). If friction acted on the homogeneous or background mode, it would change the expansion law at relative O(γ/H) = 0.016–0.047 (`K:29`; suggested). Lifted relative to the FRW background in the cosmic frame, it does not.
3. **No local sink action (§3.3).**
   - Proved: no instantaneous local sink stress exists; the sink must carry memory.
   - Suggested: no local fixed-frame action gives a symmetric conserved sink stress.
   - The constructed sink is non-local through Π, as E1 + N_c's Π already is.
4. **Inherited.** The strong-field drag bound (suggested), the irrational-limit CP (conditional), Lemma CU's ansatz, the complete split (P-r192b, a price), and stationarity (P-r14b, or the P-r14a kernel).

**Against the expectation (`TESTS:7469`).** "The noiseless outgoing sink has no CP + conserving completion, because … fluctuation–dissipation": **refuted in set A's class** (proved). In set A the metric is a classical deterministic functional of records:
- a T = 0 classical sink needs no noise (classical FDT: noise ∝ k_BT·γ = 0);
- CP is decided by the instrument, not by the classical post-processing (`C:1-3`: a noiseless sink is CP, a noisy classical sink is also CP, and only the mean-field version is non-linear);
- the conserving completion exists (§3).

What forbids sink noise is AX:82-83 (a readout from record content alone), not positivity (`C:2`: with a noisy sink, h is no longer a function of the records). The FDT objection binds only a quantum or thermal sink, which R12-7 already excluded (`rR12-7:72`). **So the tie does not break toward E1.**

**Tie-break statement (reading).** On the O(G²) completion, the noise source and the sink, E2 + N_c ties with E1 + N_c:
- the same Π;
- the same a = 2 inertness, scaled by |R| ≤ 1 inside bands of width g ≈ 1e-38 to 1e-28 (`S:30-38`);
- the same homogeneous bookkeeping;
- a near-cone TT content within 3.4–5.3% (`K:22-27`);
- a split-sink at most 0.016 ρ_GW (`K:28`).

The structural differences are:
- (i) E2's gauge is physical, so Theorem G's reason for a = 2 is idle in E2. a = 2 is still the only insertion with an inert spacelike source (`S:42`).
- (ii) E2 regulates the near-cone band by friction rather than by age, but needs a band cap under P-r14b.
- (iii) E2 adds the FRW friction-lift datum.

None of these is observational at present. vR14-2:11's "no cost metric" still applies.

---

## 0. In plain words

- **The question.** E2 says gravitational waves are slowly absorbed by a hidden sink tied to the cosmic frame. Can it be completed the way E1 was (gravity's own energy counted, a bookkeeping term Π that keeps energy conserved, the record weighted as √−g T), and does its noise or its sink weigh differently?
- **Yes, it completes.** Write the friction into the same equation that E1 + N_c uses. The friction term then behaves exactly like an extra conserved source, so Einstein's equations still hold, with the sink counted as part of the source. Π, already needed for E1, automatically stores the energy the sink absorbs. No new kind of object is required.
- **No noise is needed.** In set A the metric is computed from the records by a fixed rule. A rule with friction is still a fixed rule. A sink at zero temperature that is never fed anything back is noiseless, and quantum consistency is not affected. The fluctuation–dissipation objection applies to a quantum sink, not to this one.
- **The noise weighs the same as in E1.** With friction, every channel's coupling to gravity gets one common factor |R|. That factor is 1 everywhere except in an absurdly thin band around the light cone. So R19-2's cancellation (the noise does not gravitate on slowly varying modes) holds in E2 exactly.
- **The sink weighs nothing extra.** Its energy is part of the same conserved total that E1 already pins. Moving bodies see the sink as the tiny "frame dipole" already known.
- **Two new small loose ends.**
  - Exactly on the light cone, the least-noise recipe would make one record channel's noise grow without limit if the universe were truly stationary. A cap fixes this at a ~1% cost on an already tiny term.
  - In an expanding universe one must say whether friction also acts on the expansion itself. If it did, the expansion law would change by a few percent.

## 1. Prior art (each counted once)

1. **R12-7 / vR12-7.**
   - E2-h: (□ − γu·∂)h̄ = −16πGJ in harmonic gauge (`rR12-7:67`). It preserves harmonic gauge (`rR12-7:117`).
   - The causal telegraph kernel (`rR12-7:113`).
   - The Lamb-string sink is a toy with no field-level action, stress, FRW or gravitating completion (`vR12-7:7`).
   - E2-TT is acausal (`vR12-7:9`).
   - The frame dipole Φ₁ = (GMγ/2c²)(w·x̂) (`rR12-7:141`).
2. **R14-2 / vR14-2.**
   - Drag Γ = 2γ|U|/(3Mc²) and γ ≲ 0.016–0.047 H₀ (`vR14-2:3`).
   - P-r14a, the zero-integral kernel (`vR14-2:5`).
   - The damped single-port meter Ĥ_γ, causal (`rR14-2:203-207`).
   - T_eq = e^{−γ_E}/γ (`vR14-2:9`).
   - The tie, with no cost metric (`vR14-2:11`).
   - P-r14b (`rR14-2:244`).
3. **R16-14 / vR16-14.** N formally restores β = 1. "For E2, commuting derivatives do not construct the missing sink action and stress tensor" (`vR16-14:15`). The tie is observational; structurally E2 lacks the sink (`vR16-14:17`).
4. **R18-7 / vR18-7.**
   - E1 + N_c: S = (−g)J + Λ, retarded Π, □h = −16πGτ_rec; Π is causal and non-local (`vR18-7:3`).
   - CP by U_rA_r (`vR18-7:11`).
   - β = 1 (`vR18-7:13-18`).
   - The a = 4 zero holds only in its static scope (`vR18-7:20`).
5. **R18-11 / vR18-11.** Theorem G selects a = 2 within the contravariant density family (`vR18-11:3`). Lemma P (`vR18-11:5`).
6. **R19-2 / vR19-2.**
   - Theorem I₀ is confirmed off the cone at the complete split (P-r192b). The two TT polarizations give (2, 6)u₀; spacelike modes give (0, 0); timelike modes give (4, −4) (`vR19-2:5`).
   - The Lemma F0 conservation core and the lift dependence are confirmed. Under the registered comoving-unit stationarity, lift A is dust-like, w → 0 (`vR19-2:7-9`); the proper-unit w → −1 is a new completion.
   - I use R19-2's split closed forms (`rR19-2:183`) and re-derive them numerically for the damped kernel (`S:6-20`).
7. **R16-4.** At drag-allowed γ, E2 keeps 95.6–98.5% of initial TT energy at t_H (`rR16-4:311`). So E2 also needs P88-type data unless P-r14b holds.
8. **R19-6 (worker, recorded during the run).** W1, the weight-1 clause, by gauge-blindness (`TESTS:7569-7572`). See §6.3 for E2.
9. **Repository grep** (`P/agents/`, `P/TESTS.md`) for "E2 + N", "sink stress", "friction" with "Π", "|R|": no construction of an E2 O(G²) completion. `docs/` was not grepped.
10. **Comparators (RECALLED).**
    - The Landau–Lifshitz identity and the relaxed harmonic equations (via `rR18-7:103-104`).
    - Kostelecký 2004: explicit diffeomorphism breaking by fixed backgrounds conflicts with the Bianchi identity.
    - Belinfante–Rosenfeld: a symmetric conserved local stress needs Lorentz invariance.
    - Classical fluctuation–dissipation: noise ∝ k_BT.

## 2. Hypotheses: class ℰ₂𝒩 (stated before any title)

- **H1.** E1's record side as in R18-7/R18-11/R19-2:
  - R13-6's repaired gain;
  - R15-2's channels;
  - the a = 2 insertion (the meter adaptively measures √−g T, and the classical side multiplies by √−g);
  - the meter network rational.
- **H2 (E2).** The gothic readout obeys (□ − γ(ω)u·∂)h^{αβ} = −16πG τ_rec^{αβ}, with u = the CMB frame.
  - γ is ohmic in [0.016, 0.047] H₀, or P-r14a's passive zero-integral kernel.
  - The meter is R14-2's damped single port.
- **H3.** τ_rec = Π[S], with S = √−g J + Λ[h], Λ = (−g)t_LL + t_H from the realised h, and R18-7's retarded Π.
- **H4.** The noise is Gaussian, homogeneous, isotropic and stationary in the frame. Its least-decoherence trade-off is K = P⁻¹/4 + G P G†: backaction plus the record noise fed back through the complex response. This is R15-2's form with G → G†, as required for a dissipative response.
- **Excluded:** strong field; quantum or thermal sinks; dynamical frames (Einstein-aether); E2-TT; non-Gaussian noise.

---

## 3. Probe (a): the E2 + N construction

### 3.1 The law (proved: construction)

1. **Record.** Unchanged from E1 at a = 2: J = F·(√−g T + ξ) + B (P76).
2. **Source.** S = √−g J + Λ[h], with Λ built from the realised h.
3. **Projection.** τ_rec = Π[S]. Π satisfies i p_β K^{αβ} = −D^α for every S (`K:1`).
4. **Readout.** (□ − γu·∂)h^{αβ} = −16πG τ_rec^{αβ}. It is retarded from t₀ with zero free data (P88 extended). Under P-r14b, the attractor replaces the data.

### 3.2 Consequences (proved; checked)

- **The harmonic condition propagates.** □ − γu·∂ commutes with ∂, and ∂·τ_rec = 0, so ∂_β h^{αβ} = 0 at every order. Checked for the per-mode solution (`M:2`).
- **Einstein's equations hold.** The LL identity in harmonic gauge then gives G^{αβ}[g] = 8πG T_eff, with (−g)T_eff = τ_rec − Λ + X̃ and **X̃^{αβ} := −(γ/16πG)u·∂h^{αβ}**.
  - At O(G) this is G⁽¹⁾[h₁] = 8πG(J + X̃₁), checked in all 10 components (`M:4`).
  - X̃₁ is flat-conserved (`M:3`).
  - So **the metric is a GR metric with a recorded, conserved effective source whose friction part is the sink**.
- **The sink stress.**
  - At O(G) it is X̃₁. For a body moving at w through the frame, X̃₁⁰⁰ = (γ/4πG)w·∇U. Its monopole is zero, and its Newtonian field is exactly R12-7's frame dipole Φ₁ = (GMγ/2)(w·x̂) (`K:4-5`). The known drag and the frame dipole are the sink's linear gravity, not extra effects.
  - At O(G²), Λ obeys ∂_βΛ^{αβ} = Q^α[h₁; J + X̃₁] (the LL identity with E2's linear equation). The friction part, Q[h₁; X̃₁], is the field's energy-momentum loss to the sink. Π completes it with K_sink, ∂K_sink = −Q[h₁; X̃₁]. This is explicit, causal and non-local.
  - **Homogeneous part.** Π's k = 0 content is K⁰⁰ = −S⁰⁰ and K⁰ⁱ = −S⁰ⁱ, with **Kⁱʲ = 0** (`K:2`). So the sink is pressureless in the frame, as R12-7's anchored bath (`rR12-7:108`), and it carries any absorbed momentum in K⁰ⁱ. The "frame recoil" of P-r12b is replaced by K's momentum density.
- **Stationary balance (checked, `K:8-11`).** Per mode, ⟨Q⁰[h₁; X̃₁]⟩ = −⟨Q⁰[h₁; J]⟩ = −2πγω²|G_γ|²B/k⁴. The sink absorbs exactly the record noise's work, and the total homogeneous K is time-independent in stationarity. In E1, by contrast, it compensates a log-growing TT energy.

### 3.3 The sink action (probe (a)'s "or proof that none exists")

- **Lemma S2 (proved): no instantaneous local sink stress.**
  - Suppose Y^{αβ} is a local functional of the stationary, homogeneous fields (h₁, J) at equal times. Then ⟨∂_βY^{0β}⟩ = ∂_t⟨Y⁰⁰⟩ + ∂_i⟨Y⁰ⁱ⟩ = 0.
  - But the sink heating −⟨Q⁰[h₁; X̃₁]⟩ is nonzero per channel (TT: 8πγω²t²|G_γ|² > 0, `K:12`). At the complete split it is 0 on spacelike modes and 2πγω²|G_γ|²·4(x² − 1)/k⁴ > 0 on timelike modes (`K:16-18`).
  - So any sink stress must store energy that grows ∝ t: it needs memory. That memory is either a carrier (the Lamb string) or Π's retarded kernel.
- **No local action (suggested).**
  - A local sink field anchored to a fixed, non-dynamical frame gives a canonical stress with T^{0i} ≠ T^{i0}. The Lamb string carries momentum density but no energy flux along x.
  - Without boost invariance there is no Belinfante symmetrisation (comparator). Kostelecký's explicit-breaking/Bianchi conflict applies (comparator).
  - A local action therefore needs either a dynamical frame (Einstein-aether/khronon, outside H2 and with its own α₁, α₂ and c_T constraints) or a non-local completion.
  - **E1 + N_c is in the same position.** Its frame-tied gain also needs the non-local Π (`rR18-7:157-167`, `vR18-7:9`). So this does not separate the routes.
- **Answer to `vR16-14:15`.** The sink's stress tensor is now explicit: X̃ at O(G) and K_sink at O(G²). Its "action" is not a local Lagrangian, for the same reason E1 + N_c has none.

### 3.4 Well-posedness (proved, structure)

- Each order is a telegraph equation with a known source: the retarded G_γ, a causal kernel inside the cone (`rR12-7:113`).
- Π is causal (`vR18-7:3`).
- The O(G²) products are finite as in R18-7 (f(0) = f′(0) = 0).
- P-r14a's γ(ω) is passive and causal (`vR14-2:5`). It commutes with ∂, so the harmonic condition still propagates.

## 4. Probe (b): CP

- **Proved (structural).** The instrument at each step is:
  1. an adaptive Gaussian meter (strength set by √−g[h_{<t}], a = 2);
  2. the record;
  3. a deterministic classical update of (h, sink), causal and dissipative;
  4. the record-controlled unitary.

  The Kraus operators are U_r A_r(h_{<t}), which are CP for any classical record dependence (`vR18-7:11`). The meter is R14-2's damped single port, whose factor and inverse are both causal (`rR14-2:203-204`). The finite rational networks are as `vR15-2:15`. **The friction and the sink add no quantum operation.**
- **Toy (checked, `C:1-3`).** A qubit; 6 steps; a telegraph filter with friction γ; sink energy E_s ← E_s + γv²dt; feedback θ(h, E_s) non-linear.
  - Noiseless sink: Choi eigenvalues ≥ 0.089; TP error 3e-16; linearity defect 2.5e-16; h a function of the records: True.
  - Noisy classical sink: also CP, but h is **not** a function of the records.
  - Mean-field feedback: linearity defect 1.9e-2.
- **The FDT point (proved for this class).** A T = 0 classical sink fed only by retarded data is deterministic, so it is noiseless. The matter's decoherence trade-off K = P⁻¹/4 + GPG† only gets |R| ≤ 1 smaller (§6.1). No CQ positivity condition ties classical-classical dissipation to diffusion; the CQ trade-off binds the quantum-to-classical coupling, i.e. the record noise, which E1 already pays.

## 5. Probe (c): β, γ

- **Static (proved).** u·∂h = 0 on static fields, so the O(G²) static law is literally E1 + N_c. That gives the static point mass g₀₀ = −1 + 2M/r − 2M²/r² and β = 1 (`vR18-7:13-18`; R18-7's `r187_ll.out` reruns identical), and γ = 1 at O(G) (`vR16-14:5`). G_γ(0, k) = 1/k² (`rR12-7:137`).
- **Insensitive to a.** The matter enters as (−g)T at every a. The insertion weight changes only the noise.
- **Quasi-static (inherited).**
  - The frame dipole, ≤ 2e-20 of Newton at 1 AU at γ ≤ 0.03 H₀ (`rR14-2:191`).
  - The drag bound (`vR14-2:3`).
  - The O(G²)·γ corrections: estimated γ·w·GM/c³ ≲ 1e-28 relative (suggested).
- These are non-PPN friction terms, as in `vR16-14:5`.

## 6. Probe (d): the noise and sink active density

### 6.1 Theorem I₀ for E2 (proved; checked)

- **Per-mode structure (checked, `M:8-23`).** In the harmonic law with friction, every per-mode coefficient has the form c_hh|G_γ|² + c_hJ Re G_γ. There is no Im-part term, and no explicit γ beyond G_γ (the X̃ cross terms average to zero, `M:5`).
- **Gauge check (checked, `M:25-26`).** At γ → 0 the harmonic table equals R19-2's Poisson table at a = 2 in 10 of 10 entries: an independent harmonic-gauge check of Theorem G. The harmonic-minus-Poisson differences are ∝ (a − 2) and match R18-11's Δ.
- **Common scaling (proved, `S:1-3`).** All channels share G_γ, so every channel kernel is R·(E1 kernel), with R = (1 − x²)/(1 − x² − igx). Since Re R = |R|², every per-mode coefficient is |R|² × E1's.
- **The split scales too (proved; checked numerically, `S:6-20`).**
  - The trade-off with G = R·G₁ gives P_E2 = P_E1/|R| and K_E2 = |R|K_E1.
  - The S-block floor, the K_⊥⊥ minimum and the 1×1 floors reproduce at five (x, g) points. The P matrix agrees to ≤ 5e-2 near the cone, where the optimum is flat; K agrees to 5 digits.
- **Theorem I₀-E2.** Per mode, **τ_E2 = |R|·τ_E1** for every split defined on E1's structure. At a = 2 and the complete split, spacelike modes give 0 and timelike modes give |R|(4, −4)u₀ (`S:23-24`). Reading (U) is zero on every mode; reading (P) is −4|R|u₀ on timelike modes only.
- **What it changes.** |R| differs from 1 only for |1 − x| ≲ g, with g = 2e-38 to 8e-29 across the window and drag-allowed γ (`S:30-38`). The timelike deficit is ∫(1 − |R|) ≈ g/2 (`S:25-28`). **The noise gravitates as in E1** wherever vR19-2's off-cone result applies.
- **Through the cone.** Per mode, E2's total |R|τ_E1 tends to 0 from both sides at x = 1. Individual channels peak at ±4/g and cancel (TT against ρ, `S:23-29`). The friction thus regulates vR19-2's excluded cone point, but see caveat 1 for the record variance.

### 6.2 The near-cone band (proved formula; suggested size)

- p₁,E2 = 2√D′/(1 − x²)² ~ 2g/y² (`S:47`).
- The record variance excess is ~ γt/4 (`S:48-53`). Under P-r14b it is unbounded, so the band needs a cap (P-r198c).
- The tested cap holds the S block at its band-edge power. Its residual is 2.3115 per shell, independent of g. That is 0.7–0.8% of the leading-log TT near-cone stress 4 ln(2/g) at record-noise g (`S:54-59`).
- On a t_H history no cap is needed (excess ≤ 0.012).
- Scope: one cap model; the trapezoid TT total at g = 1e-7 is coarse (`S:56`). The residual comes from the fine band grid.

### 6.3 Which a? (proved; checked, `S:40-44`)

- In E2, the readout gauge is fixed by the law: the residual gauge needs □ξ = 0 and ∂_tξ = 0. **So Theorem G's selection (gauge-blind averages) has no content in E2** (reading on a proved fact).
- At the complete split, the harmonic-law spacelike totals are τ₀₀ = 6(a − 2)/(1 − x²)u₀ and τ_kk = 2(a − 2)(5x² − 2)/(1 − x²)u₀. **They vanish only at a = 2.** So in E2, a = 2 is selected by inertness, and through it by the budget: u₀ ≥ 1.17 ρ_Λ over the window, its minimum being at the corner (`vR18-11:17`). It is not selected by gauge-blindness.
- The harmonic ρ² coefficient has no x⁴ term for any a (`S:44`). So R18-11's IR argument for a = 2 is also idle in E2.
- **Bearing on R19-6 (reading).** E2 is consistent with W1 (`TESTS:7569-7570`) but does not force it by W1's reason; in E2 it is forced by the noise budget instead.

### 6.4 Sink active density and the FRW bookkeeping (proved; checked; vR19-2 applied)

- **Minkowski.** Lemma P holds in E2. For k = 0, harmonic gauge gives ∂_t h̄⁰⁰ = 0, so X̃⁰⁰_{k=0} = 0, and G⁽¹⁾₀₀ has no k = 0 content. So ⟨τ⁰⁰⟩ (noise + sink + K) stays at zero. **The sink has no separate homogeneous energy.**
- **FRW (lift A, friction lifted relative to the background).** The conservation core d(a³ρ_n) = −p_tot d(a³) is confirmed (`vR19-2:7`).
  - K_sink is pressureless (`K:2`), so the sink does not enter p_tot. E2 changes ρ_n only through its TT near-cone pressure, by a factor 1.034–1.053 over E1's at t_H (stationary E2), or by 0.954–0.984 on a t_H history (`K:22-27`).
  - **Following vR19-2:** under the registered comoving-unit stationarity the source pressure dilutes, and lift A gives dust-like ρ_n (w → 0), not w = −1 (`vR19-2:7-9`).
  - That holds identically for E2: the sink, being pressureless, is dust-like in either convention. **No E2-specific Λ.** I make no NOISE-IS-Λ-type claim.
- **R12-7's sink as a separate budget item.** (γ/3H)ρ_GW ≤ 0.016 ρ_GW. With R19-2's leading-log ρ_GW ≈ 3.6e-5 ρ_Λ at the corner, that is ≤ 5.6e-7 ρ_Λ (`K:28`). Under Π this is a bookkeeping split of ρ_n, not an extra term (reading on proved Lemma P/F0).

## 7. Probe (e): prices (named, not adopted) and the tie-break

**New:**
- **P-r198a (FRW lift of the friction).** "The friction acts on the metric's deviation from the FRW background in the cosmic frame." The alternative, friction on the background, changes the expansion law at O(γ/H) ≈ 2–5% (suggested). *Axiom text:* AX:185-186 (dynamics, time metric).
- **P-r198b (the sink is Π).** "The energy-momentum the friction removes is held by the conserving completion." This is a consequence of P-r12a′ + Π, not an extra sentence. It **retires P-r12b's** separate noiseless, T = 0, outgoing, gravitating, recoiling sink: noiseless = AX:82-83; outgoing = the retarded kernel; gravitating and recoil = K (reading on §3.2).
- **P-r198c (near-cone band cap).** Needed only with P-r14b; residual ≈ 0.8% of the leading-log TT near-cone stress (suggested). *Axiom text:* as P-r192c.

**Carried:**
- P-r1, P-r12a′ (the friction kernel, now with harmonic gauge as law), P-r12c (meter memory ~2/γ), P-r13b, P-r14a or P-r14b;
- P-r18-7a/P138 (Π), P145/W1 (a = 2, motivated in E2 by inertness rather than gauge-blindness);
- P-r192a (lift A), P-r192b (complete split);
- P76/P88 (needed unless P-r14b, `rR16-4:311`).

**Count, against E1 + N_c.**
- E2 + N_c adds P-r12a′, P-r12c, P-r14a or P-r14b, P-r198a, and (with P-r14b) P-r198c.
- It drops P-r12b (absorbed) and, with P-r14b, the start time and its data.
- No cost metric orders these (`vR14-2:11`).

**Tie-break statement.** **The tie holds.** The registered mechanism for breaking it (the FDT objection to a noiseless sink) does not apply in set A's class: CP is structural, the sink is noiseless because the readout is deterministic, and conservation is supplied by the same Π that E1 needs. The noise and sink gravitate as in E1 to within factors |R| ≤ 1 in bands of width g ≲ 1e-28 and few-percent log factors. The remaining differences are law data (P-r198a, P-r198c) and the stationarity price P-r14b/P-r14a, none observationally decided.

## 8. Remarks on earlier records (worker)

- **`vR16-14:15` and `vR16-14:17`** ("E2 lacks a sink action and stress tensor"): the stress tensor is now explicit (§3.2). Lemma S2 shows it cannot be an instantaneous local functional. The action question is shared with E1 + N_c (§3.3).
- **`rR12-7:24, 104-108`** ("the sink must gravitate; ρ_s = (γ/3H)ρ_GW"): under Π, the sink gravitates as part of a total whose homogeneous energy is pinned (Lemma P) or fixed by p_tot (Lemma F0). The separate ρ_s is a bookkeeping split.
- **The V channel's sink rate is negative on spacelike modes in the LL bookkeeping** (bracket −4j²(1 − x²) in `K:16`). So "the sink absorbs energy" holds for the total and for the TT and ρ channels, not for each channel.
- **Theorem I₀ (vR19-2:5) gets an independent harmonic-gauge confirmation** at a = 2 via `M:25`, and its split closed forms are re-derived numerically (`S:6-20`).

## 9. Strong words checked

- **"Constructed":** in the scope listed above, with Π non-local and finite rational networks. It is not a strong-field or non-perturbative statement.
- **"Exactly |R| × E1":** per mode, at O(G·noise²), Gaussian, for ohmic (real) γ. For P-r14a's complex γ(ω), Re R = |R|² fails at relative O(γ₀ω_c/(ck)²) ~ 1e-42 (suggested estimate, not computed).
- **"Sink is noiseless":** classical, deterministic, fed by retarded data only. Quantum sinks are excluded by H4/R12-7.
- **"No local sink action":** suggested (comparator-based). Lemma S2 (memory is required) is proved.
- **"Tie holds":** on the stated quantities and orders. The FRW lift and the band cap are data, not results.
- **"Refuted" (the expectation's FDT mechanism):** for the class ℰ₂𝒩 (classical deterministic readout). It is not a claim about E2 with a quantum or thermal sink.

## 10. What would decide it

1. **A referee** of §3.2 (the friction as a conserved effective source, and the sink inside Π), Lemma S2, Theorem I₀-E2 (the |R| scaling and the G P G† trade-off), and §6.3 (a = 2 by inertness in E2).
2. **The owner's FRW lift of the friction (P-r198a).** If friction acts on the background, the expansion law moves at O(γ/H) (a few %). That is a possible new observational test of γ, comparable to or tighter than the double-pulsar drag (suggested, not computed).
3. **Whether P-r14b is accepted.** If it is, the near-cone cap P-r198c is needed; if not, E2 is E1 plus a few percent of friction on a t_H history (`rR14-2:245`).
