# C5 round 16, probe R16-14: set A, closing the noise-fed PPN test for E1 and E2 (worker report)

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-12 23:51Z to about 00:20Z (2026-10-13). No repository file was edited.

**Scratch:** `scratchpad/C5/R16-14/`.
- `r1614_checks.py` and `r1614_checks.out` (sections [0]–[10]) hold every number below. Runtime about 2 s with OMP_NUM_THREADS=2. SHA-256: script `9edf37d8…ce427`, output `d0dde6e2…beaf8` (recompute with `shasum -a 256`).
- `rerun/` holds copies of the six archived runners and their reruns; `rerun_summary.txt` gives the diff result.
- No downloads, no web fetches. Every comparator is via an earlier referee or RECALLED.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `vR12-7` = `P/agents/C5_R12-7_referee_verdict.md` (and so on); `R13-6:n` = `P/agents/C5_R13-6_report.md:n` (and so on); `out:n` = line n of `r1614_checks.out`.

**What I read.** In full: `AX`; `TESTS:2302-2320` (C5 method); the set-A entries and verdicts `TESTS:3143-3180, 3409-3418, 4218-4243, 4436-4445, 4449-4462, 4518-4560, 4682-4692, 4726-4732, 4817-4832, 4889-4897, 4939-4951, 5108-5126, 5177-5183, 5286-5294, 5433-5437`; item 14 `TESTS:5628-5653`; `SUMMARY.md:677-714` (§26); the reports `C5_R12-7_report.md`, `C5_R13-6_report.md` (§§0–2, 4–10), `C5_R14-2_report.md`, `C5_R15-2_report.md`, `C5_R16-4_report.md:1-100`, `C5_R11-5_report.md:125-260`; the verdicts `vR6-4`, `vR11-5`, `vR12-4`, `vR12-7`, `vR13-6`, `vR14-2`, `vR15-2`, `vR16-4`.

**Labels.** **proved** (derived here under stated hypotheses); **checked** (a number in `r1614_checks.out`); **suggested** (argued, not proved); **reading** (interpretation); **comparator** (literature, via an earlier referee or RECALLED). **Subtraction rule:** each output section prints its subtraction. **Order rule:** O(G) mean field with all source velocities to O(v²/c²) for α₁, α₂, γ; O(G²) for β; O(G·noise²) for the noise-fed terms.

**Recheck of the archived runners (checked, `rerun_summary.txt`).** R12-7, R13-6, R14-2, R15-2 and R16-4 rerun byte-identical. R11-5's stdout is identical; its archived `.out` also captured seven lines of scipy IntegrationWarning text.

---

## Reading against the FIXED readings (`TESTS:5647-5650`)

| Route | Worker reading | Why |
|---|---|---|
| **E1** (repaired gain P-r13b, R15-2 channel split, TT weight ¼, h_TT = 0) | **PASS, with the O(G²) completion N** (named price P-r16-14a). **OPEN** for the bare linearized route, which does not fix β. | α₁, α₂ and γ − 1 are O(G) quantities. They are computed exactly (zero in PPN form) and their non-PPN residuals pass every bound by ≥ 3.5 decades over the whole window 4e-10 to 5e-6 m (§3). β needs an O(G²) completion. Completion N gives β = 1 (§4). The noise-fed terms pass by ≥ 11.9 decades wherever the route's budget passes (§5). |
| **E2** (E2-h friction, γ ≤ 0.047 H₀, same gain) | **PASS, with completion N plus R12-7's sink in the source.** **OPEN** for the bare route. | The same as E1, plus a friction frame dipole. Its effective α₁ is ≤ 2.6e-13 (7.6 decades), and it gives no α₂ torque (parity, proved). |
| **Literal linear class** (the metric is a linear functional of records of matter T: `R13-6:146,442`) | **EXCLUDED (worker; a no-go, so a referee is required)** | With the geodesic coupling, β = 0 and Mercury's perihelion is 57.5″/cy. With the literal ½h_μνT^μν coupling, β_eff = ½ and it is 50.3″/cy. Both exceed the RECALLED |anomaly| < 0.003″/cy by ≥ 3.4 decades at every (ℓ, τ_c, γ), because these terms are parameter-independent (§4.1; checked out:47-51). |

**The tie does not break (reading).** Every PPN residual that touches the window is shared: the gain term is the same in both routes. E2's own terms are ≥ 7.6 decades below their bounds. Both routes need the same completion N.

**Against the expectation (`TESTS:5651-5653`).**
- "α₁, α₂ vanish at linear order": confirmed, and they are **exactly** zero in PPN form, because α₁ and α₂ live only at O(G) (§3.1).
- "Suppressed at second order": confirmed (§5).
- "Both PASS": confirmed only after a completion is named.
- "Likeliest failure α₂ for E2's friction": not so. The friction's frame dipole is odd in w, so it exerts no spin torque (§3.3). The tightest margin is the **shared** gain's α̂₂ residual in neutron-star self-fields: 6.9e-13 against 2e-9.
- **The failure point no one registered is β.** A metric that is linear in records of matter cannot give Mercury's perihelion.

---

## 0. In plain words

- **The two "preferred-frame" PPN numbers, α₁ and α₂, can be computed exactly without any new theory.** They multiply terms of the post-Newtonian metric that are linear in Newton's constant. So the linearized models E1 and E2 already fix them. The earlier statement "PPN unclosed, no nonlinear theory" (`vR12-7:11`; `R14-2:26`) applied to β, not to α₁ and α₂.
- **In both routes α₁ = α₂ = 0 and γ = 1 exactly, in the PPN sense.** What the frame adds is short-range or Hubble-scale junk:
  - E1's record gain adds a tiny 1/r³ correction, of relative size 6(τv/r)².
  - E2's friction adds a direction-dependent constant potential, of relative size γvr/2c².
  - Read as effective α's at the scale of each experiment, the largest is 7e-13 (neutron-star spin precession, from the gain at its largest allowed τ_c), against a bound of 2e-9.
- **β is different: it needs gravity to gravitate.** β measures the U² term, gravity acting on its own field energy.
  - If the classical metric is a straight linear sum of records of matter (as R13-6 wrote it), β is 0 or ½, depending on how matter couples. Mercury's perihelion then comes out 33% or 17% too large. That is ruled out by more than 3 decades.
  - The fix is to let the records' source include gravity's own stress-energy (the Landau–Lifshitz form of Einstein's equations). Then the "linear functional of records" is exactly GR's nonlinear metric, and β = 1. That is a named price, P-r16-14a.
- **The fix has a side effect.** Once gravity's own stress gravitates, so does the record noise's field energy. The two budget premises that earlier probes treated as optional (the Isaacson premise for wave noise, and premise (iii) for constraint noise) become consequences of the completion (suggested).
- **The noise itself is far too weak to show up in orbits or pulsar timing.** Its timing jitter is below 1e-28 s. Its background at nanohertz is Ω_GW ≈ 1e-78. If its energy gravitates, it acts on Mercury like a tiny uniform density.
  - **Mercury gives a Solar-System bound on that density for the first time,** independent of cosmology: below 1.6e12 ρ_Λ.
  - Inside each route's budget-allowed window it is at most about ρ_Λ, so it passes by 12 decades.

---

## 1. Prior art (each counted once)

1. **R12-7 and verdict.** The linear frame dipole Φ₁ = (GMγ/2c²)(w·x̂) is "not of PPN form" (`R12-7:141`). "No nonlinear metric theory exists from which PPN α₁, α₂ can be derived" (`vR12-7:11`).
2. **R13-6.** "Zero frame displacement at first order", and noise-fed ⟨h²⟩ ≲ 2e-59 by power counting (`R13-6:347-348`). Class E1-H1: h = G_R·J, with matter coupled through ½h_μν(g*T) (`R13-6:146`). "The metric is a linear functional of the records" (`R13-6:442`). The repaired gain is P-r13b (`vR13-6:11-15`).
3. **R14-2 and verdict.** PPN "linear order only for both; no nonlinear theory in either" (`R14-2:191-192`). E2 needs "a nonlinear frame theory giving PPN α₁, α₂" (`R14-2:294`). The drag-allowed γ is 0.016–0.047 H₀ (`vR14-2:3`); the τ_c ceiling is 1.49e-3 m (`R14-2:168-176`, `vR14-2:7`).
4. **R15-2 and verdict.** Lemma A channel split; TT weight ¼ (`vR15-2:5,13`). ⟨h_ijh_ij⟩_TT ≤ 1.4e-49 and ⟨φ²⟩_S ≤ 3e-52 (archived `r152_checks.out` [7]; the report's 8e-59 is the τ_c case only). PPN at second order is power counting, C < 1e40 needed (`R15-2:202-210`). |u₁| = ħI_F/(32π^{3/2}ℓ³τ) is confirmed; premise (iii) is not established (`vR15-2:17`).
5. **R16-4 and verdict.** STATE-DEPENDENT for 𝒢(1, 1/ℓ); P-r16a (h_TT = ḣ_TT = 0) (`vR16-4:19`). Second-order PPN is power counting (`R16-4:79`).
6. **R11-5.** The PPN comparators and the "noise feeds the mean metric only through its own energy" estimate (`R11-5:220-221`, suggested there).
7. **R6-4.** The Newtonian window, 4e-10 to 5e-6 m (`vR6-4:7`).
8. **Comparators (RECALLED).**
   - Will's PPN metric. α₁, α₂, α₃, γ, ζ₁ − 2ξ multiply potentials linear in ρ (U, U_ij, V_i, W_i, Φ₁, A, w-terms); β and ξ multiply U², Φ₂ and Φ_W (Will 2014, Living Rev. Relativ. 17, 4).
   - Perihelion ∝ (2 + 2γ − β)/3.
   - The Landau–Lifshitz/harmonic-gauge relaxed Einstein equations □h̄^{μν} = −16πGτ^{μν} with τ = (−g)(T + t_LL) + t_H are exact GR (Poisson & Will 2014).
   - Bounds as the item states. Mercury's anomalous perihelion |δω̇| < 0.003″/cy (Pitjeva–Pitjev).
   - Isaacson/Burnett short-wave averaging.
   - Chandrasekhar's ellipsoid potential-energy tensor.
9. **Repository grep** (`P/agents/`, `P/TESTS.md`) for "beta_PPN", "β_PPN", "Landau–Lifshitz", "perihelion", "4/3", "pseudotensor". "Perihelion" hits only this item; no earlier probe computed β or a perihelion for set A. `docs/` was not grepped.

## 2. Hypotheses (class 𝒫, stated before any title)

- **P-H1.** E1: R13-6's model with the repaired gain F = e^{−k²ℓ²/2}(1 − 4iωτ)(1 − iωτ)^{−4}, τ = ℓ/c or τ_c ≤ 1.49e-3 m/c; R15-2's channels; h_TT = 0 at t₀. E2: (□ − γu·∂)h̄ = −16πG F·(source), with γ ≤ 0.047 H₀. Both on Minkowski space in the CMB frame u. Solar velocity w = 369.8 km/s.
- **P-H2 (order).** The mean metric at O(G) with source velocities to O(v²/c²); bodies in uniform or quasi-static motion; v ≪ c.
- **P-H3 (completions, stated separately).**
  - **L₀:** the metric is linear in records of matter T (g = η + h), with matter on geodesics of g.
  - **L½:** as L₀, but with the literal coupling ½h_μνT^μν (`R13-6:146`).
  - **N:** the record source is the Landau–Lifshitz total τ^μν (matter + gravitational stress), passed through F (and, for E2, the friction, plus R12-7's sink X so that ∂·τ = 0).
- **P-H4 (noise).** Gaussian, homogeneous and stationary in u (E1: stationary up to ln T); even in (ω, k).
- **Excluded realizations:** strong-field (compact-body) completions beyond O(1) factors; dynamical frames; non-Gaussian noise; α₃ and ζ's (not listed).

---

## 3. Probe (a): α₁, α₂, γ at O(G), with constants

### 3.1 Proposition P (proved; comparator for the PPN form)

In Will's metric, α₁ and α₂ appear only in four places: in g₀ⱼ, in the coefficients of V_j, W_j, w_jU and w^iU_ij; and in g₀₀, in the coefficients of w²U and w^iw^jU_ij. All of these potentials are linear in ρ. So **α₁ and α₂ are fixed by the O(G) metric of moving sources, to O(v²/c²) in g₀₀ and O(v/c) in g₀ⱼ.** No O(G²) completion is needed.

Write the routes' kernels as K = K_GR + δK, with ω = k·u for a source moving at u through the frame.
- **E1:** δK = K_GR(F − 1). F − 1 is analytic at (ω, k) = 0 with no constant term: e^{−k²ℓ²/2} − 1 and F_t − 1 = 6x² + 20ix³ − 45x⁴ − … (checked out:5-6). Every term of δK is τ^mℓ^{2n}(k·u)^m k^{2n−2}, with homogeneous degree m + 2n − 2 ≥ 0. A PPN term is degree −2 (∝ 1/k²). **So δK has no PPN-form part at any order in u.** α₁ = α₂ = 0 and γ = 1 exactly in PPN form (proved).
- **E2:** δK = Σ_{m≥1}(iγ k·u)^m/(k² − (k·u)²)^{m+1}, of degree −m − 2. These carry the new scale c²/(γu) and are not of PPN form. α₁ = α₂ = 0 and γ = 1 exactly in PPN form (proved). The static limit is untouched (`R12-7:137`).

### 3.2 Checks by exact quadrature (moving Gaussian body; checked out:8-23)

- **E1** (s = uτ/a = 0.05). The exact δΦ matches −6s²(u·∇)²Φ − 20s³(u·∇)³Φ to within 0.4–1.2% at r = 4–8a (out:11-14). The on-axis falloff slope is −2.89, −2.93, −2.95, tending to −3 (out:15). **No 1/r term.**
- **E2** (u = 0.01c, γ = 1e-3 c/a). The odd part equals the frame dipole (GMγ/2c²)u cos θ to within 0.97–0.99 at r = 6–9a (finite-size corrections at r = 3a: 0.89; out:18-21). The even part is a constant γu/2. It comes from k < γu/c², i.e. r > c²/(γu) = 2.4e30 m at γ = 0.047 H₀ (out:22-23). A constant potential exerts no force.

### 3.3 The residuals as effective α's at each test's scale (checked out:25-44; mapping suggested at O(1) except α̂₂)

- **α̂₂ (spin precession, self-field).**
  - The gain's self-energy is −3τ²u_iu_j∫ρ∂_i∂_jΦ. The α₂ self-energy is (α₂/2c²)w_iw_jW_ij.
  - For a homogeneous spheroid I computed A_i − 2/3 = −(4/5)ε_i and d(A_ia_i²)/dε_i = 8/15 numerically (out:25-26). Matching the orientation-dependent parts gives **α̂₂,eff = 45(cτ/R)²**, with K = 44.999 (out:26).
  - For E2, the frame dipole −γ(u·∇)χ is odd under x → −x. So it exerts **no torque** on a reflection-symmetric body (proved). Only the even γ² part remains, ~ (γR/c)².
- **α₁.** The anomalous companion force is compared with α₁(wv/c²)Gm/r²:
  - gain: α₁,eff = 6(cτ/r)²(w/v);
  - friction: α₁,eff = γr/(2v).
- **γ (Cassini).**
  - E1's temporal gain on the moving Sun's field: 6(τw/b)². Spatial smearing is e^{−b²/2ℓ²}, zero to double precision.
  - E2's frame dipole along a 1 AU path, against the Shapiro logarithm.

| Test (bound, RECALLED) | E1 strict (ℓ = 5e-6 m) | E1/E2 τ_c ceiling (cτ = 1.49e-3 m) | E2 friction (γ = 0.047 H₀) |
|---|---|---|---|
| α₂ solar spin, r = R_☉ (4e-7) | 2.3e-27 | 2.1e-22 | 5.7e-38 |
| **α̂₂ pulsar spin, R = 12 km (2e-9)** | 7.8e-18 | **6.9e-13 (3.5 decades)** | 1.7e-47 |
| α̂₁ J1738+0333 orbit, a = 1.74e9 m (1e-5) | 4.3e-29 | 3.8e-24 | 2.6e-16 |
| α₁ at 1 AU (1e-5) | 8.3e-32 | 7.4e-27 | 2.6e-13 |
| γ − 1, Cassini (2.3e-5) | — | 4.2e-29 | 2.2e-21 |

Every entry passes across the whole window ℓ ∈ [4e-10, 5e-6] m and γ ≤ 0.047 H₀. The gain entries are largest at the τ_c ceiling, so the table's middle column is the worst case.

---

## 4. Probe (a): β at O(G²)

### 4.1 Lemma L: a metric linear in records of matter fails Mercury (proved; checked out:46-51)

- **L₀.** The exterior metric is exactly g₀₀ = −1 + 2U, g_ij = (1 + 2U)δ_ij, so β = 0, γ = 1.
  - Exact geodesic orbit integration (a = 1000 m, e = 0.2) gives a shift ratio to GR of 1.3382. The PPN formula gives 4/3; the difference is the 1/a correction (out:47-48).
  - Mercury: 57.52″/cy, an excess of 14.54″/cy against < 0.003″/cy. **3.7 decades.** β − 1 = −1 against 8e-5.
- **L½** (the literal ½h_μνT^μν, `R13-6:146`, `R15-2:85`).
  - The 1PN test-mass Lagrangian is v⁴/8 + (3/2)Uv² with **no U² term**. Matching to geodesic PPN gives γ = 1, β_eff = ½ (sympy, out:50).
  - The orbit ratio is 1.1692 (7/6 = 1.1667). Mercury: 50.25″/cy, an excess of 7.27″/cy. **3.4 decades** (out:51).
- **Scope.** These terms are static, so frame-independent. They do not depend on ℓ, τ_c, γ or the noise, so they fail "for every parameter". They hold for E1 and E2 alike, because friction does not touch statics (`R12-7:137`).
- This is the **EXCLUDED** reading for the literal linear class. It is a no-go: **referee required.**
- Comparator (RECALLED): the classic result that a linear spin-2 theory gives 4/3 of the perihelion advance. It is reproduced here, not used.

### 4.2 Completion N (proved, given the comparator)

- Take the record source to be τ^μν = (−g)(T^μν + t_LL^μν) + t_H^μν. The routes' equations then become:
  - **E1:** h̄ = G_R·F·τ;
  - **E2:** (□ − γu·∂)h̄ = −16πG F·(τ + X).
- At F = 1, γ = 0 this is exactly GR (comparator). Here the metric is still "a linear functional of records", but of records of τ. So g is a nonlinear functional of matter.
- **β = 1, ξ = 0 in PPN form,** by the §3.1 argument applied to the U² source: F − 1 and the friction add only non-PPN-degree terms.
- Residuals:
  - E1: 6(τ_c w/R_☉)² = 4.2e-29 on the U² term (out:104);
  - E2: γwr/2c² = 3.2e-20 at 1 AU (out:103);
  - checked against |β − 1| < 8e-5.
- Bianchi holds at O(G²) because F commutes with ∂ and ∂·τ = 0 (comparator). For E2, X is R12-7's sink, P-r12b (`R12-7:104-107`).
- **The sink's local stress is negligible.** The solar self-drag (Γ = 8.8e-26 s⁻¹) deposits 2.4e16 W. Over t_H that is 6e-14 M_☉, spread along 1.7e23 m (out:102). Its FRW density is ≤ 0.016 ρ_Λ (out:101).

### 4.3 What N implies for the budget premises (suggested; reading)

- Under N, τ contains t_LL[h] of the **realized** classical field, record noise included. So:
  - the TT noise's Isaacson stress gravitates (the Isaacson premise of `R11-5`/`R13-6` becomes a consequence);
  - the S/V constraint noise's field energy gravitates (R15-2's premise (iii), `vR15-2:17`).
- Its magnitude is O(1)|u₁|. Its sign is undetermined (S negative, V positive; `R15-2` §4.5b).
- The only alternative that keeps β = 1 without this uses t_LL of the **mean** metric ⟨h⟩ (call it N̄). That makes the metric depend on an ensemble expectation, not on record content. That is in tension with "a readout value is determined by record content alone" (`AX:82-83`) (reading).

---

## 5. Probe (b): the noise-fed terms

### 5.1 The noise medium (checked out:53-82)

- A homogeneous medium at rest in u, with active density ρ_act = ρ + 3p, shifts perihelia like a cosmological term:
  - |Δω| = 4π²ρ_act a³√(1−e²)/M per orbit;
  - an exact orbit check gives −9.223427e-8 against −9.223428e-8 (out:54);
  - for Mercury that is 3.77e3 rad/orbit per kg/m³ (out:55).
- **Mercury therefore bounds any gravitating noise medium: |ρ_act| < 9.3e-15 kg/m³ = 1.56e12 ρ_Λ.** This is a local, cosmology-free comparator (out:55).
- **In-window** (budget ρ_n ≤ ρ_Λ; radiation-like ρ_act = 2ρ_n): |Δω| = 4.5e-23 rad/orbit. **11.9 decades of margin** (out:56).
- **Under N at the least-decoherence split** (|ρ_act| ≤ 6|u₁|; out:57-71; |u₁| reproduces R15-2's table to 1%):
  - strict τ = ℓ/c fails Mercury for ℓ ≲ 3e-8 m (at 3e-8 m the ratio is 1.0);
  - the τ_c ceiling fails only near 4e-10 m (×8.8).
  - Both regions are already outside R15-2's premise-(iii) budget window (ℓ ≳ 5e-8 m for τ_c, ≳ 2.5e-7 m strict, `R15-2` §4.5). So the PPN test does not shrink the window further. It does give that window's lower end a local backstop (reading).
- **Medium α's** ~ 3ρ_act/ρ̄(r), suggested at O(1).
  - In-window: ≤ 2.5e-22 (at 1 AU).
  - Worst case outside the window (strict, 4e-10 m): 6.1e-9 (J1738) and 6.5e-10 (solar spin), against 1e-5 and 4e-7 (out:79-82).
- **Relic TT data (aside; the item fixes h_TT = 0).** R16-4's one-quantum witness fails Mercury by itself for ℓ ≲ 3e-8 m: ×7.5e7 at 4e-10 m, ×12 at 2e-8 m (out:70-78). So the Solar System confirms R16-4's STATE-DEPENDENT for small ℓ without the ρ_Λ comparator.

### 5.2 O(⟨h²⟩) dressing (checked in the model, out:84-87)

- Terms in O(h_b h_n²) with no derivative on the noise are those of a constant H. Odd-derivative averages ⟨h∂h⟩ vanish for noise even in (ω, k) (P-H4; proved).
- Model: Φ(A x), A = √(1 + H), with antithetic Monte Carlo.
  - Isotropic H gives −0.050⟨H²⟩/r, a G renormalization, and a P₂ part of 0.0003 (zero within sampling).
  - An anisotropic covariance gives dc₂/dκ = −0.063.
- With a frame anisotropy κ ≤ 10(w/c)² (suggested) and ⟨h²⟩ ≤ 1.4e-49: **α₂,eff ≤ 8.8e-50.** This replaces the earlier "C < 1e40 needed" (`R15-2:209`) with C ≈ 0.6 in this model.
- Terms with two derivatives on the noise are the medium of §5.1.

### 5.3 Stochastic perihelion and timing (checked out:89-98)

| Effect | Value | Comparator (RECALLED) |
|---|---|---|
| S(+V) Shapiro-type jitter per pulse, 1 kpc (×10 envelope for V) | 5.9e-29 s (strict 4e-10 m); 1.6e-31 s (τ_c); 5.3e-31 s (5e-6 m) | PTA residuals ~1e-7 s |
| TT record noise in the PTA band (ε = 1 envelope) | Ω_GW = 2.9e-84 (1 nHz), 3.4e-78 (1/yr); h_c ≤ 5e-50 | NANOGrav h_c ~ 2.4e-15 |
| Body acceleration noise (Earth, pulsar), 10 yr | timing ≤ 5e-40 s | — |
| Mercury perihelion random walk, 1 century | 5.5e-44 rad | 1.5e-8 rad/cy |

The noise is ħ-limited, so its long-wavelength content scales as k⁴ (TT) or is bandwidth-diluted (S/V). Nothing reaches an observable level.

---

## 6. Probe (c): against the bounds

| Quantity | E1 + N | E2 + N | Bound (RECALLED) | Label |
|---|---|---|---|---|
| α₁ (PPN form) | 0 | 0 | 1e-5 | proved; checked (no 1/r term) |
| α₁ effective (worst case) | 3.8e-24 | 2.6e-13 | 1e-5 | checked; O(1) mapping suggested |
| α₂ (PPN form) | 0 | 0 | 2e-9 | proved |
| α̂₂ effective (worst case) | 6.9e-13 | 6.9e-13 (shared gain) | 2e-9 | checked (K = 45, homogeneous spheroid); strong-field O(1) suggested |
| γ − 1 | 0 (PPN); 4e-29 | 0 (PPN); 2.2e-21 | 2.3e-5 | proved; checked |
| β − 1 | 0 (PPN); 4e-29 | 0 (PPN); 3.2e-20 | 8e-5 | proved given N; checked |
| β − 1, literal linear class | −1 (L₀) or −½ (L½) | same | 8e-5; Mercury 0.003″/cy | **fails by ≥ 3.4 decades** (checked; no-go) |
| noise medium, perihelion | 4.5e-23 rad/orbit (in-window) | same + sink ≤ 1.6% | 3.5e-11 rad/orbit | checked |
| noise dressing α₂ | ≤ 8.8e-50 | same | 2e-9 | checked in model; κ suggested |
| timing jitter | ≤ 6e-29 s | same | ~1e-7 s | checked |

## 7. Probe (d): prices and the tie

**New price P-r16-14a (named, not adopted): the record's source is gravity's total stress.** The classical metric record must be sourced by the Landau–Lifshitz τ^μν (matter plus gravitational stress), or equivalently obey the full Einstein equations with the recorded matter source. It cannot be a linear functional of records of matter alone.
- *Axiom text:* the readout clause (`AX:82-83`) then reads the metric as a nonlinear functional of matter records. The open gate "source/action and physical-observable identification" (`AX:187`) gains its O(G²) content.
- *Consequences (suggested):* the Isaacson premise and premise (iii) stop being optional. R15-2's constraint-channel overshoot (`vR15-2:17`) becomes binding wherever the γ-trade does not apply.

**Carried, unchanged:** P-r1, P-r11a (E1), P-r11b, P-r13a/P-r13b, P-r13c, P-r15a/b, P-r16a (E1); P-r12a′, P-r12b, P-r12c (E2) (`R14-2:252-276`).

**The tie (reading): not broken.**
- Both routes need P-r16-14a identically.
- Their largest PPN residual (the gain's α̂₂) is identical.
- E2's own PPN terms (frame dipole α₁,eff ≤ 2.6e-13; even friction part ≤ 6e-38) are 7.6–30 decades below their bounds.
- E2 also needs its sink inside τ, but that is its existing price P-r12b.

## 8. Strong words checked

- **"Exactly zero in PPN form":** within the linear O(G) theory, all orders in u, for kernels analytic at (0, 0) (E1) or with the γ-expansion valid at r ≪ c²/(γu) = 2.4e30 m (E2). The effective-α map of non-PPN terms is order-of-magnitude, except the α̂₂ spheroid factor K = 45. Neutron stars are strong-field, so that factor is suggested at O(1); the margin is 3.5 decades.
- **"Fails Mercury for every parameter":** the U² term of the literal linear class is static and parameter-free. It is checked by exact orbit integration and the 1PN Lagrangian. **This is a no-go, so a referee is required.** It covers the classes L₀ and L½ only, not N or N̄.
- **"PASS":** conditional on completion N, which the routes as registered do not contain. Without N the routes do not define β, so they are **OPEN**.
- **"Forces premise (iii)":** suggested. It assumes N acts on the realized field. Gauge invariance of the averaged constraint-noise source is not proved.
- **"Mercury bounds the medium":** uses the RECALLED 0.003″/cy, treats the medium as uniform on 0.4 AU, and assumes p = u/3 for the S/V field energy (traceless static field stress; suggested).
- **The dressing bound** is a constant-H model with an assumed κ ≤ 10(w/c)².

## 9. What would decide it

1. **A referee of Lemma L** (EXCLUDED for the literal linear class), and of Proposition P: that α₁ and α₂ are O(G) and are zero in PPN form for both kernels.
2. **The owner's choice of completion:** N (records of the total stress, noise gravitates) or N̄ (records of the mean field's stress, in tension with `AX:82-83`). Under N, R15-2's premise-(iii) window, with its γ-trade, becomes the route window.
3. **A strong-field neutron-star version** of the gain's α̂₂ residual (realistic EOS, crust), to firm up the 3.5-decade margin at the τ_c ceiling.

**Sources.** Via earlier referees: bounds and the double-pulsar/PPN comparators (`vR11-5:12`, `R14-2:191`, `vR14-2:3`); the R15-2 formulas (`vR15-2:13,17`). RECALLED:
- Will 2014 (PPN metric, perihelion (2 + 2γ − β)/3, |β − 1| < 8e-5, solar α₂ < 4e-7);
- Shao et al. 2013 (α̂₂); Shao & Wex 2012 (α̂₁);
- Cassini (Bertotti et al. 2003);
- Pitjeva–Pitjev (Mercury, 0.003″/cy);
- Poisson & Will 2014 (Landau–Lifshitz relaxed equations);
- Chandrasekhar (ellipsoid index symbols, W_ij);
- Isaacson 1968 / Burnett 1989;
- NANOGrav 15-yr h_c;
- the linear spin-2 "4/3 perihelion" result.
